from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class EditStats:
    substitutions: int
    deletions: int
    insertions: int
    hits: int

    @property
    def edit_distance(self) -> int:
        return self.substitutions + self.deletions + self.insertions

    @property
    def mer_denominator(self) -> int:
        return self.hits + self.edit_distance


def edit_stats(reference: str, hypothesis: str) -> EditStats:
    m, n = len(reference), len(hypothesis)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            substitution_cost = 0 if reference[i - 1] == hypothesis[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + substitution_cost,
            )

    substitutions = 0
    deletions = 0
    insertions = 0
    hits = 0
    i, j = m, n

    while i > 0 or j > 0:
        if (
            i > 0
            and j > 0
            and reference[i - 1] == hypothesis[j - 1]
            and dp[i][j] == dp[i - 1][j - 1]
        ):
            hits += 1
            i -= 1
            j -= 1
        elif (
            i > 0
            and j > 0
            and dp[i][j] == dp[i - 1][j - 1] + 1
        ):
            substitutions += 1
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            deletions += 1
            i -= 1
        else:
            insertions += 1
            j -= 1

    return EditStats(
        substitutions=substitutions,
        deletions=deletions,
        insertions=insertions,
        hits=hits,
    )


def rate(numerator: int | float, denominator: int | float) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def summary_csv_path(out_csv: Path) -> Path:
    return out_csv.with_name(f"{out_csv.stem}_summary{out_csv.suffix}")


def main(args: argparse.Namespace) -> None:
    gt_dir = Path(args.gt_dir)
    pred_dir = Path(args.pred_dir)
    baseline_dir = Path(args.baseline_dir) if args.baseline_dir else None
    out_csv_path = Path(args.out_csv)

    gt_files = {path.name: path for path in gt_dir.glob("*.txt")}
    pred_files = {path.name: path for path in pred_dir.glob("*.txt")}
    common_files = sorted(set(gt_files) & set(pred_files))

    print(f"GT txt files: {len(gt_files)}")
    print(f"Pred txt files: {len(pred_files)}")
    print(f"Common files: {len(common_files)}")

    if not common_files:
        raise RuntimeError("No common txt files found between gt_dir and pred_dir.")

    baseline_files = {}
    if baseline_dir is not None:
        baseline_files = {path.name: path for path in baseline_dir.glob("*.txt")}
        missing_baselines = sorted(set(common_files) - set(baseline_files))
        if missing_baselines:
            preview = ", ".join(missing_baselines[:5])
            raise RuntimeError(
                f"Missing {len(missing_baselines)} baseline txt files in "
                f"{baseline_dir}. Examples: {preview}"
            )
        print(f"Baseline txt files: {len(baseline_files)}")

    rows = []
    total_gt_chars = 0
    total_edit_distance = 0
    total_mer_denominator = 0
    total_baseline_edit_distance = 0
    total_baseline_mer_denominator = 0
    total_refiner_cer_reduction = 0.0
    preference_points = 0.0

    for fname in common_files:
        gt_text = read_text(gt_files[fname])
        pred_text = read_text(pred_files[fname])
        stats = edit_stats(gt_text, pred_text)

        gt_length = len(gt_text)
        pred_length = len(pred_text)
        cer = rate(stats.edit_distance, gt_length)
        cmer = rate(stats.edit_distance, stats.mer_denominator)

        total_gt_chars += gt_length
        total_edit_distance += stats.edit_distance
        total_mer_denominator += stats.mer_denominator

        row = {
            "File": fname,
            "GT_Length": gt_length,
            "Pred_Length": pred_length,
            "Edit_Distance": stats.edit_distance,
            "Substitutions": stats.substitutions,
            "Deletions": stats.deletions,
            "Insertions": stats.insertions,
            "Hits": stats.hits,
            "CER": cer,
            "cMER": cmer,
        }

        if baseline_dir is not None:
            baseline_text = read_text(baseline_files[fname])
            baseline_stats = edit_stats(gt_text, baseline_text)
            baseline_cer = rate(baseline_stats.edit_distance, gt_length)
            baseline_cmer = rate(
                baseline_stats.edit_distance,
                baseline_stats.mer_denominator,
            )
            cer_reduction = (
                rate(baseline_cer - cer, baseline_cer)
                if baseline_cer > 0
                else 0.0
            )

            if cmer < baseline_cmer:
                preference = 1.0
            elif cmer == baseline_cmer:
                preference = 0.0
            else:
                preference = -1.0

            total_refiner_cer_reduction += cer_reduction
            total_baseline_edit_distance += baseline_stats.edit_distance
            total_baseline_mer_denominator += baseline_stats.mer_denominator
            preference_points += preference

            row.update(
                {
                    "Baseline_Length": len(baseline_text),
                    "Baseline_Edit_Distance": baseline_stats.edit_distance,
                    "Baseline_CER": baseline_cer,
                    "Baseline_cMER": baseline_cmer,
                    "CER_Reduction": cer_reduction,
                    "Preference": preference,
                }
            )

        rows.append(row)
        print(f"{fname} | CER: {cer:.4f} | cMER: {cmer:.4f}")

    macro_cer = sum(row["CER"] for row in rows) / len(rows)
    micro_cer = rate(total_edit_distance, total_gt_chars)
    micro_cmer = rate(total_edit_distance, total_mer_denominator)

    summary_rows = [
        {"Metric": "Total Files", "Value": len(common_files)},
        {"Metric": "Total GT Characters", "Value": total_gt_chars},
        {"Metric": "Total Edit Distance", "Value": total_edit_distance},
        {"Metric": "Macro CER", "Value": macro_cer},
        {"Metric": "Micro CER", "Value": micro_cer},
        {"Metric": "Micro cMER", "Value": micro_cmer},
    ]

    print(f"Total Files: {len(common_files)}")
    print(f"Total GT Characters: {total_gt_chars}")
    print(f"Total Edit Distance: {total_edit_distance}")
    print(f"Macro CER: {macro_cer:.4f}")
    print(f"Micro CER: {micro_cer:.4f}")
    print(f"Micro cMER: {micro_cmer:.4f}")

    if baseline_dir is not None:
        baseline_macro_cer = sum(row["Baseline_CER"] for row in rows) / len(rows)
        baseline_micro_cer = rate(total_baseline_edit_distance, total_gt_chars)
        baseline_micro_cmer = rate(
            total_baseline_edit_distance,
            total_baseline_mer_denominator,
        )
        micro_cer_reduction = (
            rate(baseline_micro_cer - micro_cer, baseline_micro_cer)
            if baseline_micro_cer > 0
            else 0.0
        )
        macro_cer_reduction = (
            rate(baseline_macro_cer - macro_cer, baseline_macro_cer)
            if baseline_macro_cer > 0
            else 0.0
        )
        mean_per_file_cer_reduction = total_refiner_cer_reduction / len(rows)
        preference_score = preference_points / len(rows)
        summary_rows.extend(
            [
                {"Metric": "Baseline Macro CER", "Value": baseline_macro_cer},
                {"Metric": "Baseline Micro CER", "Value": baseline_micro_cer},
                {"Metric": "Baseline Micro cMER", "Value": baseline_micro_cmer},
                {"Metric": "Micro CER Reduction", "Value": micro_cer_reduction},
                {"Metric": "Macro CER Reduction", "Value": macro_cer_reduction},
                {"Metric": "Mean Per-file CER Reduction", "Value": mean_per_file_cer_reduction},
                {"Metric": "Preference Score", "Value": preference_score},
            ]
        )
        print(f"Baseline Macro CER: {baseline_macro_cer:.4f}")
        print(f"Baseline Micro CER: {baseline_micro_cer:.4f}")
        print(f"Baseline Micro cMER: {baseline_micro_cmer:.4f}")
        print(f"Micro CER Reduction: {micro_cer_reduction:.4f}")
        print(f"Macro CER Reduction: {macro_cer_reduction:.4f}")
        print(f"Mean Per-file CER Reduction: {mean_per_file_cer_reduction:.4f}")
        print(f"Preference Score: {preference_score:.4f}")

    out_csv_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with out_csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    out_summary_csv_path = summary_csv_path(out_csv_path)
    with out_summary_csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Metric", "Value"])
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"\nSaved CSV: {out_csv_path}")
    print(f"Saved summary CSV: {out_summary_csv_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gt_dir", type=str, required=True, help="Directory containing ground-truth txt files")
    parser.add_argument("--pred_dir", type=str, required=True, help="Directory containing predicted txt files")
    parser.add_argument("--out_csv", type=str, required=True, help="Path to save output CSV file")
    parser.add_argument("--baseline_dir", type=str, help="Optional baseline txt directory for refiner CER reduction and preference score")
    main(parser.parse_args())
