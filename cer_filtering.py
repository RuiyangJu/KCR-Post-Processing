import argparse
import os

import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description="Remove pages with CER > 25% and calculate average CER."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV file."
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=0.25,
        help="CER threshold. Default: 0.25."
    )

    args = parser.parse_args()

    csv_path = args.input
    threshold = args.threshold

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"File not found: {csv_path}")

    df = pd.read_csv(csv_path)

    if "CER" not in df.columns:
        raise ValueError("The input CSV file must contain a 'CER' column.")

    df_filtered = df[df["CER"] <= threshold].copy()

    average_cer = df_filtered["CER"].mean()

    print(f"Input file: {csv_path}")
    print(f"CER threshold: {threshold}")
    print(f"Original pages: {len(df)}")
    print(f"Removed pages with CER > {threshold * 100:.0f}%: {len(df) - len(df_filtered)}")
    print(f"Remaining pages: {len(df_filtered)}")
    print(f"Average CER after filtering: {average_cer:.6f}")
    print(f"Average CER after filtering (%): {average_cer * 100:.2f}%")


if __name__ == "__main__":
    main()