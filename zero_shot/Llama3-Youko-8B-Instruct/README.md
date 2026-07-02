# Llama3-Youko-8B-Instruct
## Error Case Analysis on Synthetic Test Set
### How to Read the Cases

- `Input`: the raw OCR text given to the model. It may already contain recognition errors.
- `Pred`: the model's corrected output based on `Input`.
- `GT`: the human-corrected ground-truth transcription used as the evaluation target.
- `GT_Length` / `Pred_Length`: the number of characters in `GT` and `Pred`.
- `Edit_Distance`: the minimum number of character edits needed to transform `Pred` into `GT`.
- `CER`: Character Error Rate, calculated as `Edit_Distance / GT_Length`. Lower is better.
- Underlined spans in `Input` and `Pred` mark segments that differ from `GT` after alignment. `GT` is left unmarked as the reference text.

```
File,GT_Length,Pred_Length,Edit_Distance,CER
100241706_00020_1.txt,105,106,36,0.34285714285714286
100241706_00028_1.txt,142,143,86,0.6056338028169014
100249376_00017_2.txt,108,129,65,0.6018518518518519
100249376_00018_1.txt,114,112,51,0.4473684210526316
100249376_00053_2.txt,137,174,98,0.7153284671532847
100249416_00034_1.txt,121,136,59,0.48760330578512395
100249476_00007_2.txt,157,169,67,0.4267515923566879
200006663_00006_2.txt,11,25,15,1.3636363636363635
200017458_00003_1.txt,61,46,36,0.5901639344262295
200017458_00008_1.txt,384,293,217,0.5651041666666666
200020019_00034_2.txt,263,256,149,0.5665399239543726
200020019_00057_1.txt,270,239,111,0.4111111111111111
200020019_00070_2.txt,181,165,90,0.4972375690607735
200020019_00077_1.txt,262,230,176,0.6717557251908397
200020019_00082_2.txt,102,96,47,0.46078431372549017
200021086_00025_2.txt,288,448,329,1.1423611111111112
200021763_00006_2.txt,56,56,33,0.5892857142857143
200021763_00008_2.txt,44,50,39,0.8863636363636364
200021763_00009_1.txt,71,83,44,0.6197183098591549
200021763_00042_2.txt,198,238,88,0.4444444444444444
200021802_00016_2.txt,141,106,77,0.5460992907801419
200021869_00003_1.txt,3,4,2,0.6666666666666666
200021869_00012_1.txt,74,107,62,0.8378378378378378
200022050_00002_2.txt,188,180,83,0.44148936170212766
200022050_00006_1.txt,496,284,263,0.530241935483871
200022050_00010_2.txt,468,295,189,0.40384615384615385
```

## 100241706_00020_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/100241706_00020_1.jpg" width="512" title="details">
  </p>
  
### Input
売買を定めものなり則魚を角ど<ins>と</ins>りてさすゆへに鯨さの名今も残れり其のちは量りにてまた〱うりかいをなし目方<ins>か</ins>へなり<ins>を</ins>右の鯨になひ何魚にても角どり並ぶを差身といひならはせりこのゆゑにさし身なるべし<ins>海嘩</ins>虚南留別志巻之上終

### Pred
売買を定めものなり<ins>、</ins>則<ins>ち</ins>魚を角<ins>取っ</ins>て<ins>差</ins>すゆ<ins>え</ins>に鯨さの名今も残れり<ins>。そ</ins>の<ins>後</ins>は量りにてまた<ins>売買</ins>をなし<ins>、</ins>目方<ins>替わ</ins>り<ins>を</ins>右の鯨に<ins>引く、</ins>何魚にても角<ins>取る</ins>を差身といひならはせり<ins>。</ins>このゆ<ins>え</ins>に<ins>差</ins>身なるべし<ins>。海嘔</ins>虚南留別志巻之上終<ins>。</ins>

### GT
売買を定めしものなり則魚を角どりてさすゆへに鯨さしの名今も残れり其のちは量りにてまた〱うりかいをなし目方がへなり右の鯨にならひ何魚にても角どり並ぶを差身といひならはせりこのゆゑにさし身なるべし虚南留別志巻之上終

## 100241706_00028_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/100241706_00028_1.jpg" width="512" title="details">
  </p>
  
### Input
すもの干ぐわしといふ<ins>へ仕</ins>んぢう又饅頭いづれの御代の御事なりか止事なき御かた米の御ことぶきを祝奉てあ<ins>た</ins>らげをせいあぐへきよしを仰せ出されけりい<ins>り</ins>ゞ致申べくと伺ひける所八十八才のうへまでも御<ins>果有</ins>をいわ井ま然るべくとにより一つ百の数をかたどり種工夫をめぐらけ所一<ins>ツ</ins>白のは<ins>〱</ins>

### Pred
すもの干ぐわしといふ<ins>へ仏像</ins>ま<ins>た</ins>饅頭いづれの御代の御事なりか<ins>存知</ins>なき御<ins>方</ins>米の御ことぶきを祝<ins>っ</ins>て<ins>新</ins>し<ins>く作らせ</ins>よ<ins>との</ins>仰せ<ins>あ</ins>りけ<ins>れば、入りにて申し上げ</ins>る<ins>ところ、</ins>八十八才まで御<ins>果報があ</ins>り<ins>ますようにとお祈りいたしますれば、</ins>一つ百の数をかたどり種々工夫をめぐらし<ins>、</ins>所<ins>々に</ins>白のは<ins>ちまきを結びつけました。</ins>

### GT
すもの干ぐわしといふ▲まんぢう又饅頭いづれの御代の御事なりしか止事なき御かた米の御ことぶきを祝し奉るとてあふらげをせいしあぐへきよしを仰せ出されけりいかゞ致し申べくと伺ひける所八十八才のうへまでも御寿をいわ井まし然るべくとにより一つ百の数をかたどり種々工夫をめぐらしける所一つ白のはく

## 100249376_00017_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/100249376_00017_2.jpg" width="512" title="details">
  </p>
  
### Input
にてあけ申候十七さん<ins>幾</ins>もちう<ins>め之</ins>し上白米を一粒つゝゑり粉にて絹ふるひにかけ粉一升に氷沙糖の粉三十目の積りにいれ水少入もみ合壱尺四方の箱に内に十<ins>又</ins>字にしきりをして高五寸に仕箱の内に長横共に三分程つゝ間を置のこきりめを付

### Pred
にてあけ申候十七さん<ins>幾</ins>もちう<ins>めの</ins>白米を一粒<ins>ず</ins>つ<ins>糸で引くよう</ins>にして<ins>、</ins>粉一升に氷<ins>砂</ins>糖の粉三十目<ins>ずつ</ins>の積りに入<ins>れ、水を少し入れて混ぜ</ins>合<ins>わせ、一</ins>尺四方の箱<ins>の中</ins>に十字に<ins>敷</ins>き<ins>詰め</ins>て<ins>、</ins>高<ins>さ</ins>五寸に仕<ins>上げます。</ins>箱の内<ins>側</ins>に<ins>は、</ins>長<ins>さと</ins>横共に三分<ins>ほどの隙</ins>間を<ins>残し、切</ins>り<ins>目</ins>を付<ins>けます。</ins>

### GT
にてあけ申候十七さんきもちうるし上白米を一粒つゝゑり粉にして絹ふるひにかけ粉一升に氷沙糖の粉三十目の積りにいれ水少入もみ合壱尺四方の箱に内に十文字にしきりをして高五寸に仕箱の内に長横共に三分程つゝ間を置のこきりめを付

## 100249376_00018_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/100249376_00018_1.jpg" width="512" title="details">
  </p>
  
### Input
右の粉をいれ箱の内にて右ののこきり目のとをりをうすき板のやうなるかねにて切めを付箱ともにむし一夜をきとり出しほし申候<ins>一</ins>八せんへい丸きかね二<ins>つ</ins>くひちかへにしてはさみのことくゑを付餅を少つゝはさみ火の上にてやき申候へは右のかねの大き

### Pred
右の粉を<ins>入</ins>れ箱の内にて右の<ins>残</ins>り目の<ins>通</ins>り<ins>に薄</ins>き板の<ins>よ</ins>うな<ins>金</ins>にて切めを付<ins>、</ins>箱ともに<ins>虫</ins>一夜を<ins>切り取</ins>り出しほしい<ins>と存じます。一八銭平</ins>丸き<ins>金</ins>二<ins>つ掘立</ins>かへにしてはさみの<ins>具合</ins>を付<ins>、</ins>餅を少<ins>し</ins>はさみ火の上にて<ins>焼</ins>き申<ins>しますれば、</ins>右のかねの大き<ins>さ</ins>

### GT
右の粉をいれ箱の内にて右ののこきり目のとをりをうすき板のやうなるかねにて切めを付箱ともにむし一夜をきとり出しほし申候十八せんへい丸きかね二ツくひちかへにしてはさみのことくゑを付餅を少つゝはさみ火の上にてやき申候へは右のかねの大き

## 100249376_00053_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/100249376_00053_2.jpg" width="512" title="details">
  </p>
  
### Input
たき大麦のもやしの粉九合右の食少さまし<ins>し一一</ins>粉を入水ひた〱に入候てあま酒に作り一夜置明朝あまく成申候其時い<ins>り</ins>きにあけ成程よくしほり其汁を布袋に入少<ins>し</ins>もかすなきやうにこ扨なへ<ins>二</ins>入せん<ins>し</ins>し候火をほそくいたしゆる<ins>く</ins>とせんしよき時分にへらに付見申候へは<ins>く</ins>す紙のやうにへらに付申候其時さまし成

### Pred
たき大麦のもやしの粉九合<ins>、</ins>右の食少さまし<ins>し、一一</ins>粉を入<ins>れ</ins>て<ins>水</ins>に<ins>浸したものを</ins>作り<ins>、</ins>一夜置<ins>き、</ins>明朝<ins>甘</ins>く成<ins>りました。その</ins>時<ins>、入り</ins>き<ins>り</ins>に<ins>開</ins>け<ins>て</ins>程よく<ins>塩味がつき、その</ins>汁を布袋に入<ins>れ、</ins>少<ins>し</ins>も<ins>カスナキよ</ins>うに<ins>漉</ins>し<ins>ました。</ins>扨<ins>、鍋</ins>に<ins>二度</ins>入<ins>れ煮し</ins>し候<ins>。</ins>火を<ins>細</ins>くいたし<ins>、</ins>ゆる<ins>く</ins>と<ins>煮</ins>しよき時分に<ins>、</ins>へらに付<ins>けて</ins>見まし<ins>たら、白絹のようになっていました。その時、塩味がつきました。</ins>

### GT
たき大麦のもやしの粉九合右の食少さまし粉を入水ひた〱に入候てあま酒に作り一夜置明朝あまく成申候其時いかきにあけ成程よくしほり其汁を布袋に入少もかすなきやうにこし扨なへに入せんし候火をほそくいたしゆる〱とせんしよき時分にへらに付見申候へはうす紙のやうにへらに付申候其時さまし成

## 100249416_00034_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/100249416_00034_1.jpg" width="512" title="details">
  </p>
  
### Input
糀を少入れおけば風味よき甘酒と<ins>ゐ</ins>なる也○上飴<ins>鍋心</ins>一<ins>歯</ins>餅米一升一糀<ins>た</ins>升七合一水七合<ins>此</ins>此水にて糀をあらひは<ins>あふの</ins>ばり取かすを去<ins>は段</ins>米<ins>ど</ins>あま酒につくりなれたる時布にてしよく<ins>練</ins>り是へしるあめ少しかすをよくすりて入れ三<ins>け</ins>日置なり但し折<ins>〱王こ</ins>廻てよし<ins>餅菓子手制衣集終候</ins>

### Pred
糀を少<ins>々</ins>入れ<ins>て</ins>おけば風味よき甘酒となる也<ins>。</ins>上飴<ins>鍋心</ins>一<ins>歯</ins>餅米一升<ins>、</ins>一糀<ins>た</ins>升七合<ins>、</ins>一水七合<ins>。この</ins>水にて糀を<ins>洗い</ins>は<ins>あふの</ins>ばり取<ins>り</ins>去<ins>れば、段</ins>米<ins>ど</ins>あま酒につくり<ins>慣</ins>れたる時<ins>、</ins>布にてよく<ins>練</ins>り<ins>、これ</ins>へ<ins>白砂糖</ins>少しかすをよくすりて入れ<ins>、</ins>三日置<ins>く。</ins>但し<ins>、</ins>折々<ins>王が</ins>廻<ins>っ</ins>てよし<ins>、餅菓子手製衣集終候。</ins>

### GT
糀を少し入れおけば風味よき甘酒ともなる也○上飴練やう一上白餅米一升一糀一升七合一水七合此水にて糀をあらひはなばかり取かすを去右餅米とあま酒につくりなれたる時布にてこしよくねり是へしるあめ少しかすをよくすりて入れ三日置なり但し折々かき廻してよし

## 100249476_00007_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/100249476_00007_2.jpg" width="512" title="details">
  </p>
  
### Input
<ins>し</ins>○大根飯大根飯は常たく<ins>組た</ins>中又は麦飯の中にても大根を鱠のごくきざ<ins>きを</ins>の吹あがる時蓋をとり飯の上へ入塩をも程よくいれ蓋をて焚あげ扨暫く熟しおきうつす時かきま<ins>ぶ</ins>食してよし○常年食するには大根飯に<ins>専</ins>油の出し汁かけて食すれども米價高き時は米のすくな<ins>した</ins>い<ins>る</ins>やうする<ins>と汁</ins>なれば大根を多<ins>し</ins>入塩も喰かげんに入かけ汁なしに食すべし

### Pred
<ins>しいたけ</ins>大根飯大根飯は常たく<ins>組た</ins>中又は麦飯の中にても大根を<ins>小さ</ins>く<ins>切ったも</ins>の<ins>を</ins>吹<ins>き上</ins>がる時蓋を<ins>取</ins>り飯の上へ入<ins>れ、</ins>塩を<ins>ほど</ins>よく<ins>入</ins>れ<ins>て</ins>蓋をして<ins>炊上</ins>げ<ins>、</ins>暫く熟し<ins>置いてから</ins>かき<ins>混</ins>ぜ<ins>て</ins>食<ins>べ</ins>てよし<ins>。</ins>常年食するには大根飯に<ins>専用</ins>の出し汁<ins>を</ins>かけて食すれども<ins>、</ins>米<ins>価が</ins>高<ins>い</ins>時は米の<ins>少</ins>ない<ins>よ</ins>う<ins>に</ins>する<ins>と汁</ins>な<ins>ので、</ins>大根を多<ins>め</ins>に入<ins>れ、塩も控えめに</ins>かけ<ins>て</ins>汁なし<ins>で</ins>食すべし<ins>。</ins>

### GT
○大根飯大根飯は常たく飯の中又は麦飯の中にても大根を鱠のごとくきざみ飯の吹あがる時蓋をとり飯の上へ入塩をも程よくいれ蓋をして焚あげ扨暫く熟しおきうつす時かきまぜ食してよし○常年食するには大根飯に醤油の出し汁かけて食すれども米價高き時は米のすくなくいかやうする事なれば大根を多く入塩も喰かげんに入かけ汁なしに食すべし

## 200006663_00006_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200006663_00006_2.jpg" width="512" title="details">
  </p>
  
### Input
夜番たゞ<ins>出</ins>のぶ<ins>ツれえりレけかまさゞ</ins>ゑびす廻国<ins>ま重お</ins>

### Pred
夜番た<ins>だ出</ins>のぶ<ins>つれえりれけかまさざ</ins>ゑびす廻国<ins>ま重お</ins>

### GT
夜番たゞのぶゑびす廻国

## 200017458_00003_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200017458_00003_1.jpg" width="512" title="details">
  </p>
  
### Input
十二ひちやうばうが事十三かはづの三郎<ins>き</ins>たれし事十四いとうがし<ins>白</ins>つけの事十五をんばうがむまる<ins>こし</ins>事十六女ばうに<ins>か</ins>へうつりし事

### Pred
十二<ins>兵衛房</ins>が事十三<ins>河内</ins>三郎<ins>来</ins>た<ins>る</ins>事十四<ins>伊藤</ins>が<ins>白竹</ins>の事十五<ins>温坊</ins>が<ins>村六</ins>事十六女<ins>房</ins>に<ins>か</ins>へり<ins>居つる</ins>事

### GT
十二ひちやうばうが事十三かはづの三郎がうたれし事十四いとうがしゆつけの事十五をんばうがむまるゝ事十六女ばうにがへうつりし事

## 200017458_00008_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200017458_00008_1.jpg" width="512" title="details">
  </p>
  
### Input
御へりなくてひゑいんのふをのといふろにとぢこもせ給ひけりろかづきすゑゆきげのそのあらにさしぐるくものまなくやにゆきかふ人もまれなりりいはんやをの御すまゐ思ひやられてあはれなりこにさいちうじやうありはのなりひらはむの御なさけあさかざり人なりけれ〱たるゆきをふみけなく〱御あをたづねまいて<ins>ん</ins>らすれはまうとつりきたりてうえうあにたりゐんけんしやく〱たりおりにませ人めもくさもかれぬればいびきにみなしろたえのにはのおもあみつくる人なみはぢくいでさせ給ひてんでんの御かう三げんばりあげての山を御らんめぐしげにやははあをくなつはしげりあきはそめふゆはおつといふせめい太のおぼめつねろほのゆきをばすだれをかげてみん

### Pred
御<ins>返事</ins>なくて<ins>日々</ins>の<ins>不自由</ins>の<ins>苦労</ins>とい<ins>う</ins>こと<ins>を思い、御隠居の所に籠</ins>も<ins>り</ins>給ひけ<ins>る。鹿</ins>づき<ins>末行方</ins>のその<ins>辺</ins>に<ins>差</ins>し<ins>越</ins>え<ins>る月の光</ins>なくやに<ins>行</ins>きかふ人もまれなり<ins>。里</ins>はんやをの御<ins>住居と</ins>思ひやられてあはれなり<ins>。小</ins>に<ins>西遊寺</ins>やうありはのなり<ins>平家</ins>は<ins>無</ins>の御<ins>情浅</ins>から<ins>ず</ins>人なりけれ<ins>ど。行く道</ins>を<ins>踏</ins>みけなく<ins>。</ins>御<ins>愛慕尋</ins>ねまいて<ins>天下一の名手</ins>と<ins>知</ins>り<ins>来</ins>たりて<ins>上手</ins>あにたり<ins>。院賢</ins>しく<ins>。</ins>たりおりにませ人<ins>目</ins>も<ins>草</ins>も<ins>枯</ins>れぬれば<ins>、</ins>いびきに<ins>身を</ins>なし<ins>て寝</ins>たえの<ins>日を思ひ</ins>つくる人<ins>並び</ins>は<ins>じ</ins>くいでさせ給ひて<ins>、門</ins>の御<ins>門</ins>三<ins>度</ins>ばかり<ins>上</ins>げての山を御<ins>覧</ins>めぐし<ins>け</ins>にやははあをくなつはしげり<ins>。秋</ins>は<ins>染</ins>め<ins>冬</ins>は<ins>落とす</ins>という<ins>常の習</ins>い太の<ins>望</ins>めつねろ<ins>。</ins>ほの<ins>行く</ins>をば<ins>簾</ins>をかげて<ins>見む。</ins>

### GT
御かへりなくしてひゑいざんのふもとをのといふところにとぢこもらせ給ひけりころはかみなづきすゑゆきげのそらのあらしにさえしぐるゝくものたえまなくみやこにゆきかふ人もまれなりけりいはんやをのゝ御すまゐ思ひやられてあはれなりこゝにさいごちうじやうありはらのなりひらはむかしの御なさけあさからざりし人なりければふん〱たるゆきをふみわけなく〱御あとをたづねまいりて見まいらすれはまうとううつりきたりてこうえうあらしにたえりうゐんけんがとうしやく〱たりおりにまかせ人めもくさもかれぬれば山ざといとゞさびしきにみなしろたえのにはのおもあとふみつくる人もなしみこははしぢかくいでさせ給ひてなんでんの御かうし三げんばかりあげてよもの山を御らんじめぐらしげにやはるはあをくなつはしげりあきはそめふゆはおつるといふせうめい太しのおぼしめしつらねかうろほうのゆきをばすだれをかゝげてみるらんと

## 200020019_00034_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200020019_00034_2.jpg" width="512" title="details">
  </p>
  
### Input
申ける若もさまのおほせにはかやう<ins>小ツか</ins>せ<ins>ば罷</ins>みをふしたるやうにおぼめさんもはづかしけれ<ins>と</ins>ども今われ<ins>き</ins>ふらひて又あひ<ins>も</ins>たらんもかたいとのよりあふ事もさだめなかきりならねば跡さきの事をはかたり申也わ身の事はたのみをくだんなのな<ins>き</ins>けふかうしてしうとしたしくする事はほうばいのおもふところ又はうき世の取さたも一たんりじゆんにま<ins>う</ins>ひはわかきものゝしん中にはいにと人にきたなまれ<ins>づ</ins>まはじきをせられんはくちおし<ins>さ</ins>しだい也たとへかんた<ins>り</ins>かうふると<ins>と</ins>此事におゐてはゆるし給へとたび〱にわび事は<ins>んお</ins>もしるこのみちのな<ins>中</ins>らひしうとおもひな

### Pred
申ける若も<ins>様</ins>のおほせにはか<ins>よ</ins>う<ins>小使か</ins>せ<ins>ば罷</ins>みを<ins>休め</ins>たる<ins>よ</ins>うに<ins>思召す</ins>もは<ins>ず</ins>かし<ins>と思ひながら、と</ins>も今われ<ins>帰り果</ins>て<ins>てま</ins>た<ins>会</ins>も<ins>たランも叶い</ins>たいとの<ins>由</ins>あ<ins>りて足すくむことの定</ins>めなき<ins>次第</ins>ならねば<ins>、</ins>跡<ins>先</ins>の事をはかたり申<ins>す</ins>也<ins>。</ins>わ<ins>が</ins>身の事は<ins>頼</ins>みを<ins>下</ins>さ<ins>れたぬ今日こ</ins>うして<ins>仕置きを</ins>したしくする<ins>こと</ins>は<ins>、方便</ins>のおもふところ<ins>、また浮</ins>世の取<ins>り沙汰</ins>も一<ins>旦離縁</ins>に<ins>参</ins>ひは<ins>若</ins>き<ins>者</ins>の<ins>一心</ins>中には<ins>嫌疑</ins>にと人に<ins>軽々しくさ</ins>れんは<ins>口惜</ins>し<ins>さ</ins>しだい也<ins>。例えば</ins>かんた<ins>りこ</ins>うふると<ins>ころ、この</ins>事にお<ins>い</ins>ては<ins>許</ins>し給へとたび〱に<ins>詫</ins>び事は<ins>ん、お</ins>もしるこの<ins>道</ins>の<ins>中</ins>らひしうとおもひな<ins>す。</ins>

### GT
申ける若もしさまのおほせにはかやうに申せは我みをふかしたるやうにおぼしめさんもはづかしけれども今わかれさふらひて又あひみかたらんもかたいとのよりあふ事もさだめなしかきりならねば跡さきの事をはかたり申也わか身の事はたのみをくだんなのなさけふかうしてしうとしたしくする事はほうばいのおもふところ又はうき世の取さたも一たんりじゆんにまよひしはわかきものゝしん中にはいかにと人にきたなまれつまはじきをせられんはくちおしきしだい也たとへかんたうかうふるとも此事におゐてはゆるし給へとたび〱にわび事は人もしるこのみちのならひしうとおもひな

## 200020019_00057_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200020019_00057_1.jpg" width="512" title="details">
  </p>
  
### Input
た<ins>見</ins>のくろやき十四五年のふるがみこのくろやきなりかやうのやくしゆはめづらし<ins>と</ins>ゝしさいはいかにと<ins>ら</ins>ひけれ<ins>は</ins>我<ins>リの</ins>のばうずにかゝりし時此やまひをやみけれはわなゝきふ<ins>さ</ins>ひにて有ぞとてふるきかみこを四五でうかぶせその上にたゝみを四五でうかぶせられければやまひは其まゝなをりけりさてそのゆへにかくの<ins>と</ins>くつ<ins>り</ins>まつりたるといひければみな〱どつとわらひけりま<ins>ことと</ins>にどくやくへんじてくすりとなれはつみのふかきもほとけにやなるとむらさきのゝ<ins>こさ</ins>もじさまの仰れしも此事にてや有らんとてそゞろにわらひけり又あるかたのかぢ<ins>ば</ins>人有けるかまなこにせんくず入たりとてま<ins>じ</ins>なこはれ

### Pred
た<ins>見</ins>の<ins>黒焼</ins>き十四五年の<ins>古味</ins>この<ins>黒焼</ins>きなりか<ins>よ</ins>う<ins>な薬師</ins>は<ins>珍</ins>し<ins>くと申</ins>さ<ins>れ</ins>はいかにと<ins>ら</ins>ひけれ<ins>は</ins>我<ins>儘</ins>の<ins>婆夫子</ins>にか<ins>か</ins>りし時此<ins>病</ins>をやみけれはわな<ins>な</ins>き<ins>不相応</ins>にて有ぞとて<ins>古</ins>き<ins>紙子</ins>を四五<ins>度重ね</ins>かぶせその上に<ins>畳</ins>を四五<ins>度重ね</ins>かぶせられければ<ins>病</ins>は其ま<ins>ま</ins>な<ins>お</ins>りけりさてその<ins>故</ins>にかくの<ins>如</ins>つ<ins>り纏</ins>りたるといひければ<ins>皆々</ins>ど<ins>っ</ins>と<ins>笑</ins>ひけり<ins>真実と</ins>に<ins>毒薬変</ins>じて<ins>薬</ins>となれ<ins>ば罪</ins>の<ins>深</ins>きも<ins>仏</ins>にやな<ins>らん</ins>とむらさきの<ins>野小路様</ins>の仰れしも此事にてや有らんとてそゞろに<ins>笑</ins>ひけり<ins>また</ins>ある<ins>方</ins>のかぢ<ins>場</ins>人有けるかまなこに<ins>先駆</ins>ず入たりとて<ins>間</ins>なこはれ

### GT
たゝみのくろやき十四五年のふるがみこのくろやきなりかやうのやくしゆはめづらしゝしさいはいかにとゝひければ我らのばうずにかゝりし時此やまひをやみけれはわなゝきふるひにて有ぞとてふるきかみこを四五でうかぶせその上にたゝみを四五でうかぶせられければやまひは其まゝなをりけりさてそのゆへにかくのくつかまつりたるといひければみな〱どつとわらひけりまにどくやくへんじてくすりとなれはつみのふかきもほとけにやなるとむらさきのゝきうもじさまの仰られしも此事にてや有らんとてそゞろにわらひけり又あるかたのかぢが一人有けるかまなこにせんくず入たりとてまなこはれ

## 200020019_00070_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200020019_00070_2.jpg" width="512" title="details">
  </p>
  
### Input
またこゆとおもふもはかなゆめ<ins>め</ins>の世にさよの中山なか〱の<ins>まし</ins>にらみのすけもさすかになかし<ins>千まあしり</ins>はとてねぶたや<ins>即</ins>さ<ins>み</ins>のなかやまなか〱にあしはいたくていねもせれすかくてかなやにつき<ins>な</ins>れはきしにまさる大井川みるがうちにもきてふ<ins>ら</ins>は<ins>ず</ins>になるはや川のあ<ins>ら</ins>にわたりしたび人やいかに川せにまよふんと一しゆかくはつら<ins>ゑ</ins>けりみる〱にふちはせになる大<ins>ゐ</ins>川さだめなきよのためなるらん

### Pred
またこ<ins>のように思う</ins>もはかな<ins>い夢幻</ins>の世にさよ<ins>う</ins>の中山<ins>中</ins>の<ins>まし</ins>に<ins>見</ins>のすけも<ins>差</ins>すかなら<ins>ず千万あり</ins>はとて<ins>寝</ins>ぶたや<ins>即</ins>さ<ins>ま</ins>のなかやま<ins>中のま</ins>し<ins>に足</ins>は<ins>痛</ins>くて<ins>寝</ins>も<ins>さ</ins>れ<ins>ず</ins>かくて<ins>悲しく</ins>な<ins>り</ins>つき<ins>な</ins>れ<ins>ば帰り</ins>にまさる大井川<ins>見</ins>るが<ins>内</ins>にも<ins>来</ins>て<ins>下らず</ins>なるは<ins>早</ins>川の<ins>荒</ins>に<ins>渡</ins>りしたび人や<ins>如何</ins>川<ins>瀬</ins>に<ins>迷</ins>ふと一し<ins>行</ins>かくは<ins>憂へ</ins>けり<ins>見</ins>る<ins>中</ins>に<ins>深くなり</ins>なる大井川<ins>定</ins>めなき<ins>世</ins>の<ins>為</ins>なるらん

### GT
またこゆとおもふもはかなゆめの世にさよの中山なか〱の事にらみのすけもさすかになからましかはとてねぶたやなさよのなかやまなか〱にあしはいたくていねもせられすかくてかなやにつきぬれはきゝしにまさる大井川みるがうちにもきてふちは世になるはや川のあとにわたりしたび人やいかに川せにまよふらんと一しゆかくはつらねけりみる〱にふちはせになる大井川さだめなきよのためしなるらん

## 200020019_00077_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200020019_00077_1.jpg" width="512" title="details">
  </p>
  
### Input
かみ申也この御てらのさんがう寺ごうはかた<ins>じ</ins>しけなくもぜんたう大しのしんゑんごんゑんそうじやうゑんのこ<ins>くつ</ins>なるべし竹さいも江戸てねをまふけ<ins>形</ins>ば家をもち女をむかへみつのゑんをむすびしんだいをもをしなを人<ins>ら</ins>くもなりたゝむところのうちによろこひけりさてそ<ins>そ</ins>れよりも過行<ins>ん</ins>をとに聞えし日のもとのはしをみな人わたりかね世をもたずみかねたりし事のためしもおほかりしこゝはいづ<ins>ゝ</ins>そかんだのだいみなみにあたりてながむれは天下のぶしやうの御ざなさる御しろの<ins>方</ins>見<ins>ん</ins>事さ<ins>に太衛</ins>銀るりの玉ぎをはり<ins>き</ins>ねあけたるらうかくは雲につらな<ins>ひ</ins>有さまはもろ<ins>み</ins>し

### Pred
かみ申<ins>や、</ins>この御<ins>手</ins>らの<ins>山</ins>寺は<ins>形ば</ins>か<ins>りでは片付</ins>け<ins>られず、全道</ins>大<ins>真言権現</ins>の<ins>国主</ins>なるべし<ins>。</ins>竹<ins>斎</ins>も江戸<ins>店</ins>を<ins>廻って形</ins>を<ins>持</ins>ち<ins>、</ins>女を<ins>迎えて三</ins>つの<ins>縁</ins>を<ins>結</ins>び<ins>、身代</ins>をも<ins>増や</ins>したこ<ins>とを人々も喜びました。</ins>さて<ins>、</ins>それよりも過<ins>去</ins>に<ins>行ったことを知らせ</ins>し日の<ins>元</ins>の<ins>端</ins>を<ins>見れば、</ins>人<ins>通</ins>り<ins>ができず</ins>世をも<ins>立て</ins>ず<ins>、</ins>みかねたりし事の<ins>例</ins>も<ins>多</ins>かりしこ<ins>こ</ins>は<ins>、</ins>い<ins>ずれぞ</ins>かんだの<ins>大御代皆並んで眺め</ins>れ<ins>ば、</ins>天下の<ins>武将</ins>の御<ins>座</ins>なさ<ins>れ</ins>る御<ins>城</ins>の<ins>方を</ins>見<ins>んこと</ins>さ<ins>に太衛</ins>銀るりの玉<ins>櫛</ins>を<ins>張</ins>り<ins>き</ins>ね<ins>開</ins>けたるらうかくは雲に<ins>連</ins>な<ins>り</ins>有<ins>様</ins>は<ins>諸見</ins>し<ins>。</ins>

### GT
かみ申也この御てらのさんがう寺ごうはかたしけなくもぜんたう大しのしんゑんごんゑんそうじやうゑんのこゝろなるべし竹さいも江戸にてかねをまふけなば家をもち女をむかへみつのゑんをむすびしんだいをもをしなをし人〻しくもなりたゝむとこゝろのうちによろこひけりさてそれよりも過行はをとに聞えし日のもとのはしをみな人わたりかね世をもたゝずみかねたりし事のためしもおほかりしこゝはいづくそかんだのだいみなみにあたりてながむれは天下のぶしやうの御ざなさる御しろの見事さよ金銀るりの玉ぎをはりかさねあけたるらうかくは雲につらなる有さまはもろこし

## 200020019_00082_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200020019_00082_2.jpg" width="512" title="details">
  </p>
  
### Input
人にもよこさまならすしてこゝろにねいなる事もなしつねにかゝみのかけを見よゆかめはかけもゆか<ins>見</ins>ぬしかくおもひて<ins>こし</ins>しゆくれ竹のすぐなるみよに<ins>う</ins>ひぬ<ins>す</ins>ばやふくすしまてたのもしきかな新竹<ins>歌讃し取</ins>冊享保<ins>芝</ins>二年<ins>拵こう外り四二十そ</ins>

### Pred
人にも<ins>寄る</ins>さまなら<ins>ず</ins>して<ins>心</ins>に<ins>念</ins>なる事もなし<ins>常</ins>にかゝみの<ins>河</ins>を見よ<ins>行</ins>かめは<ins>河</ins>も<ins>行</ins>か<ins>見</ins>ぬしかく<ins>思</ins>ひて<ins>過</ins>し<ins>し夕暮</ins>竹のすぐなる<ins>水</ins>に<ins>浮</ins>ぬす<ins>早吹きす</ins>まてたのもしきかな新竹<ins>歌讃し取り</ins>冊享保<ins>芝</ins>二年<ins>拵え外り四二十</ins>

### GT
人にもよこさまならすしてこゝろにねいなる事もなしつねにかゝみのかけを見よゆかめはかけもゆかみぬへしかくおもひて一しゆくれ竹のすぐなるみよにあひぬればやふくすしまてたのもしきかな新竹斉譚五冊享保十二年板アリ

## 200021086_00025_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200021086_00025_2.jpg" width="512" title="details">
  </p>
  
### Input
或時し王其<ins>廻へ</ins>にくゐぜを立其難義に及ける時<ins>が</ins>なしミの余はすとりの辺に近付はすとる是をおそれて我ひ<ins>すば</ins>をあたへてけりしゝ王羊ををか<ins>る</ins>ず我足をはすとり<ins>六窮</ins>にもたくはすとる是を心得て其くゐぜをぬいて<ins>てらゝ</ins>薬を付てあたへぬ<ins>出</ins>それよりしゝ王山中にかくれぬある時しゝ<ins>玉</ins>狩にとら<ins>は</ins>れて篭に入られ罪人を入て是を喰しむ又<ins>皮</ins>はすとり其罪有によりて彼し<ins>ら</ins>篭に押入るし<ins>う</ins>王あへて是ををかさず還て涙を流て<ins>髭生</ins>ぬ暫有て人<ins>々</ins>篭の内を見るにさしもにたけきしゝ王耳をたれひさををつて彼はすとるをけいごすものぐを入て犯さんとするにしゝ王是をかなぐりすつ主此事を<ins>やは壱〻</ins>汝何の故にかかく獣に愛まれけるぞと云けれバ件の子細<ins>申</ins>露

### Pred
或時<ins>、</ins>王<ins>が回国中</ins>に<ins>逗留された所で、</ins>難<ins>儀</ins>な<ins>こ</ins>と<ins>がおあ</ins>り<ins>になった折がありました。その時、私は須磨</ins>の辺に近付<ins>きました。これ</ins>をおそれて<ins>、</ins>我<ins>が家の牛</ins>を<ins>差</ins>し<ins>上げておりました。しかるに、</ins>王<ins>は</ins>羊を<ins>飼われていましたが、</ins>足を<ins>須磨</ins>の<ins>崖に踏み外され、六窮</ins>にも<ins>迫っておられまし</ins>た<ins>。これ</ins>を心得て<ins>、その逗留所</ins>を<ins>抜け</ins>て<ins>、手当ての</ins>薬を付<ins>けさせ</ins>て<ins>差し上げまし</ins>た<ins>。</ins>それ<ins>以来、</ins>王<ins>は</ins>山中にかくれ<ins>られておりましたが、</ins>ある時<ins>、</ins>王<ins>は玉</ins>狩<ins>り</ins>に<ins>捕</ins>ら<ins>わ</ins>れて篭に入られ<ins>、</ins>罪人を入<ins>れられ</ins>て<ins>食わせる</ins>よ<ins>うにな</ins>り<ins>ま</ins>し<ins>た。また、皮を須磨の崖に押し込まれるという罪があり、またしても</ins>篭に押し<ins>込まれたのでした。</ins>王<ins>は</ins>あ<ins>え</ins>て<ins>これ</ins>を<ins>諦め</ins>ず<ins>、</ins>還<ins>っ</ins>て涙を流<ins>され</ins>て<ins>、髭を生やされるまで</ins>暫<ins>くありました。</ins>人<ins>々が</ins>篭の<ins>中</ins>を見る<ins>と、</ins>さしも<ins>威厳のあっ</ins>た王<ins>の</ins>耳を<ins>垂らし、髪</ins>を<ins>下げ</ins>て<ins>、</ins>彼は<ins>須磨</ins>の<ins>崖を懸命に登ろうとしている者</ins>を入<ins>れ</ins>て犯<ins>そう</ins>と<ins>したので</ins>す<ins>が、王はこれを投げ捨てられたのです。このことを、主上はどう思召されたのか、一度に御尋ねにな</ins>るに<ins>は、</ins>何故かく獣に愛<ins>さ</ins>れ<ins>ら</ins>れ<ins>た</ins>の<ins>かと仰せになりました。</ins>

### GT
或時しゝ王其足にくゐぜを立其難義に及ける時かなしミの余はすとりの辺に近付はすとる是をおそれて我ひつじをあたへてけりしゝ王羊ををかさず我足をはすとりの前にもたくはすとる是を心得て其くゐぜをぬいて薬を付てあたへぬそれよりしゝ王山中にかくれぬある時しゝ王狩にとらハれて篭に入られ罪人を入て是を喰しむ又彼はすとり其罪有によりて彼しゝ篭に押入るしゝ王あへて是ををかさず還て涙を流て畏りぬ暫有て人〻篭の内を見るにさしもにたけきしゝ王耳をたれひさををつて彼はすとるをけいごすものゝぐを入て犯さんとするにしゝ王是をかなぐりすつ主此事を聞て汝何の故にかかく獣に愛まれけるぞと云けれバ件の子細中露

## 200021763_00006_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200021763_00006_2.jpg" width="512" title="details">
  </p>
  
### Input
平皿<ins>飯鉢</ins>七ツ目<ins>蓋台</ins>中合サ汁再進<ins>煎物</ins>島台土器<ins>飯鉢押肴二種蓋台箸汁再進銚子島台土器提子</ins>押肴二種箸杯台<ins>銚子</ins>平銚子台<ins>提子</ins>

### Pred
平皿<ins>飯鉢</ins>七ツ目<ins>蓋台</ins>中合サ汁再進<ins>煎物</ins>島台土器<ins>飯鉢押肴二種蓋台箸汁再進銚子島台土器提子</ins>押肴二種箸杯台<ins>銚子</ins>平銚子台<ins>提子</ins>

### GT
平皿七ツ目中合サ煎物飯鉢蓋台汁再進島台土器押肴二種箸銚子提子飯鉢蓋台汁再進島台土器押肴二種箸銚子提子杯台平銚子台

## 200021763_00008_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200021763_00008_2.jpg" width="512" title="details">
  </p>
  
### Input
飯鉢<ins>飯鉢蓋台</ins>蓋台汁再進汁再進置杯<ins>置杯平銚子</ins>平銚子吸物<ins>吸物肴二種</ins>肴二種湯水<ins>湯水</ins>茶菓子<ins>茶菓子</ins>

### Pred
<ins>飯鉢</ins>飯鉢蓋台<ins>蓋台</ins>汁<ins>椀汁椀再進汁椀</ins>再進置<ins>き盆置き盆平銚子</ins>平銚子吸物吸物肴二種<ins>肴二種湯水</ins>湯水茶菓子<ins>茶菓子</ins>

### GT
飯鉢蓋台汁再進置杯平銚子吸物肴二種湯水茶菓子飯鉢蓋台汁再進置杯平銚子吸物肴二種湯水茶菓子

## 200021763_00009_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200021763_00009_1.jpg" width="512" title="details">
  </p>
  
### Input
濃茶濃茶後菓子<ins>後菓子薄茶</ins>薄茶以上七詰五詰に次たる尊<ins>る々</ins>の御方の<ins>饗</ins>応御料理なり二汁七菜二汁五菜本膳<ins>本膳膾直汁</ins>膾汁<ins>黍</ins>香物箸煎物<ins>香物箸</ins>坪皿飯<ins>坪以皿飯</ins>

### Pred
濃茶濃茶後菓子<ins>後菓子薄茶</ins>薄茶以上七詰五詰に次たる尊<ins>る々</ins>の御方の<ins>饗</ins>応御料理なり<ins>、</ins>二汁七菜<ins>、</ins>二汁五菜<ins>、</ins>本膳<ins>、本膳、膾直汁、</ins>膾汁<ins>、黍</ins>香物<ins>、</ins>箸煎物<ins>、香物、箸、</ins>坪皿飯<ins>、坪以皿飯</ins>

### GT
濃茶後菓子薄茶濃茶後菓子薄茶以上七詰五詰に次たる尊貴の御方の餐応御料理なり二汁七菜本膳膾汁小皿香物箸煎物坪皿飯二汁五菜本膳膾汁香物箸煎物坪皿飯

## 200021763_00042_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200021763_00042_2.jpg" width="512" title="details">
  </p>
  
### Input
桜貝椀貝の事も見知たる品なれとも此部内衣次に記す一三<ins>詳</ins>宝<ins>久</ins>高位の方に用る品也其用ゆるに<ins>ふる</ins>下のある事は伝書ニて弁へ尤食事膳部には薄盤なり一客に出々用ゆるは熨<ins>計</ins>三方杯三方なと又三方を用ゆ其時ハ薄盤なり是等の事<ins>し</ins>伝書にて心得へし一薄盤三方に異な事なし三方ハ縁二寸以上の物也其縁の薄きをいふ本膳鏡一尺三寸縁一寸五分又<ins>位</ins>壱<ins>有</ins>寸の<ins>ふる</ins>サ九寸三分<ins>れ</ins>二三膳ハ段<ins>こ</ins>入子になる寸法也一二三と大中小也縁高サハ同じ

### Pred
桜貝椀貝の<ins>こと</ins>も見知<ins>っ</ins>た品なれ<ins>ど</ins>も<ins>、この</ins>部内<ins>では</ins>衣次に記す一三<ins>詳</ins>宝<ins>久</ins>高位の方に用<ins>い</ins>る品<ins>である。その</ins>用<ins>い</ins>るに<ins>ふさわしい</ins>下のある<ins>こと</ins>は伝書<ins>に</ins>て弁へ<ins>、</ins>尤食事膳部には薄盤なり<ins>。</ins>一客に出々用<ins>い</ins>る<ins>の</ins>は熨<ins>計</ins>三方杯三方な<ins>ど、また</ins>三方を用<ins>いるその</ins>時<ins>は</ins>薄盤なり<ins>。これら</ins>の事<ins>は</ins>伝書にて心得<ins>よ</ins>し<ins>、</ins>一薄盤三方に異なる<ins>こと</ins>なし<ins>。</ins>三方<ins>は</ins>縁二寸以上の物<ins>である。その</ins>縁の薄きをい<ins>う。</ins>本膳鏡一尺三寸縁一寸五分<ins>、また位</ins>壱<ins>有</ins>寸の<ins>ふるさ</ins>九寸三分<ins>、れ</ins>二三膳<ins>は</ins>段<ins>こ</ins>入子になる寸法<ins>である。</ins>一二三と大中小<ins>である。</ins>縁高<ins>さは</ins>同じ<ins>。</ins>

### GT
一桜貝椀貝の事も見知りたる品なれとも此一部内衣次に記す一三宝ハ高位の方に用る品也其用ゆるに高下のある事は伝書ニて弁へし尤食事膳部には薄盤なり一客に出々用ゆるは熨斗三方杯三方なと又三方を用ゆ其時ハ薄盤なり是等の事伝書にて心得へし一薄盤三方に異なる事なし三方ハ縁二寸以上の物也其縁の薄きをいふ本膳鏡一尺三寸縁一寸五分又壱寸の位有高サ九寸三分二三ノ膳ハ段々入子になる寸法也一二三と大中小也縁と高サハ同じ

## 200021802_00016_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200021802_00016_2.jpg" width="512" title="details">
  </p>
  
### Input
茶うこ<ins>き</ins>右同前にら汁あへもの<ins>おね</ins>汁さみなま<ins>く十も</ins>みそすいくち根深汁いり鳥さしみ杉やき<ins>恩</ins>汁あへ物すあへなますさしみあさつきなますさしみ野びるさみあ<ins>へ</ins>へもの竹子しゆんかん汁からあへかうの物さみすつけ物や<ins>て</ins>むしても色〱よし野竹<ins>事</ins>もつかひ<ins>る</ins>あしのこもにが竹の子はかわともにやきてつかひ候也

### Pred
茶<ins>漬け</ins>右同前に<ins>も</ins>ら汁あへもの<ins>おね</ins>汁さ<ins>ま</ins>なま<ins>く十も</ins>みそすいくち根深汁<ins>入</ins>り鳥<ins>差</ins>し<ins>身</ins>杉<ins>焼</ins>き<ins>恩</ins>汁あへ物すあへなます<ins>差</ins>し<ins>身浅茅菜差</ins>し<ins>身</ins>野<ins>平差</ins>し物や<ins>手向け</ins>ても色<ins>々</ins>よし野竹<ins>事</ins>も<ins>使</ins>ひ<ins>る足</ins>の<ins>小物</ins>にが竹の子は<ins>河童</ins>ともに<ins>焼い</ins>て<ins>使</ins>ひ候也

### GT
茶うこぎ右同前にら汁あへもの蒜汁さしみなますみそすいくち根深汁いり鳥さしみ杉やき葱汁あへ物すあへなますさしみあさつきなますさしみ野びるさしみあへもの竹子しゆんかん汁からしあへかうの物さしみすしつけ物やくむしても色〱よし野竹子もつかひ候あしのこもにが竹の子はかわともにやきてつかひ候也

## 200021869_00003_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200021869_00003_1.jpg" width="512" title="details">
  </p>
  
### Input
<ins>ゝ</ins>右一<ins>は</ins>

### Pred
<ins>ゝ</ins>右一<ins>は</ins>

### GT
右一水

## 200021869_00012_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200021869_00012_1.jpg" width="512" title="details">
  </p>
  
### Input
かまほこ拵方<ins>し</ins>事玉子そふめんの如にそれを<ins>ほ</ins>竹の<ins>れ同比ほ</ins>二ツ割し両方<ins>て更</ins>ふ<ins>し</ins>しを付其中へ入さ<ins>しそ</ins>をうす<ins>て</ins>そきもよふなる<ins>に</ins>ふに入へしそれをふ<ins>ゝ</ins>かし外へ玉子を<ins>ぬ</ins>るへ<ins>へ</ins>し<ins>青意ケわしぞ</ins>

### Pred
かまほこ拵方<ins>し</ins>事<ins>、</ins>玉子そふめんの如<ins>く、</ins>それを<ins>ほ</ins>竹の<ins>れ同比ほ</ins>二ツ割し<ins>、</ins>両方<ins>て更</ins>ふ<ins>し</ins>しを付<ins>、その</ins>中<ins>に挿</ins>入さ<ins>し、</ins>そ<ins>こを薄手細</ins>きも<ins>の</ins>よ<ins>う</ins>にし<ins>たが、入</ins>れ<ins>たその中身</ins>を<ins>取り出す際、</ins>外へ玉子を<ins>抜く際には、青意気をわ</ins>し<ins>ずかみにした。</ins>

### GT
かまほこ拵方之事玉子そふめんの如にそれを竹の筒を二ツ割し両方へふしを付其中へ入さかなをうすくそきもよふなるよふに入へしそれをふかし外へ玉子をふるへし

## 200022050_00002_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200022050_00002_2.jpg" width="512" title="details">
  </p>
  
### Input
▲祝言引渡之次第一<ins>歌</ins>栗ほそきかたをむ<ins>に也んレ一三ツかわらけ</ins>成やうに三かくにお<ins>ゝ</ins>也<ins>也</ins>一のし二本<ins>寸すま</ins>ひろきかたをきやくのひだりの<ins>ぶ</ins>かたへしておきて<ins>こか</ins>し昆布切かぶなて<ins>りたに</ins>也一てうしひさ<ins>けきりお</ins>一まきずるめ<ins>のさ</ins>か<ins>なかレ事</ins>すミ一か<ins>かす</ins>こしもちくしこむすびこんぶ<ins>一むめぼし三ツざうに</ins>いもひ<ins>ら</ins>かつうほくしあ<ins>げひ</ins>一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとす<ins>ま</ins>也一ねぶか二本しろに<ins>ね</ins>一か<ins>かん</ins>んざけ<ins>とも</ins>

### Pred
栗ほそきかたをむに<ins>也</ins>三かくにお<ins>ゝ</ins>也<ins>也</ins>一のし二本<ins>寸すま</ins>ひろきかたをきやくのひだりの<ins>ぶ</ins>かたへしておきて<ins>こか</ins>し昆布切かぶなて<ins>りたに</ins>也一てうしひさ<ins>けきりお</ins>一まきずるめ<ins>のさ</ins>か<ins>なかレ事</ins>すミ一か<ins>かす</ins>こしもちくしこむすびこんぶ<ins>一むめぼし三ツざうに</ins>いもひ<ins>ら</ins>かつうほくしあ<ins>げひ</ins>一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとす<ins>ま</ins>也一ねぶか二本しろに<ins>ね</ins>一か<ins>かん</ins>んざけ<ins>とも</ins>

### GT
▲祝言引渡之次第一栗ほそきかたをむふへ成やうに三かくにおく也一三ツかわらけ一のし二本ひろきかたをきやくのひだりのかたへしておきてよし一昆布二切かぶなりにきりておく也一てうしひさげ一さかな一まきずるめ一からすミ一かずのこ一むめぼし三ツざうにもちくしこむすびこんぶいもひゝかつうほくしあわび一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとする也一ねぶか二本しろねともに一かんざけ

## 200022050_00006_1
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200022050_00006_1.jpg" width="512" title="details">
  </p>
  
### Input
をなどふたどきてい候是すてひの入吉立ハふたのくあん汁ハかハをはぎおろきて<ins>は</ins>おもミをも<ins>人</ins>入した時あげて水にてひや酒をかけをく汁時入ぶをしほげんすい合出又すまの<ins>斗</ins>にけ少候此時ハおきくしだい入せ中そにだをくに候どぶをさて吉<ins>に</ins>大ん外<ins>入</ins>但久くたきてハのあぢ悪候あきそをたきの也いつれもそをかうて久敷に候しるにハ此ちすい口さんせのこ同葉<ins>鶉</ins>の汁だにほねを入せんそにて仕立さん大也つまハその時のけい<ins>ふ</ins>つ吉きの<ins>は</ins>いほ数入吉何時もすぢをおびゆ又<ins>し</ins>めゟ中そにてしたてゟすに汁中て仕立候又につま時の物也り次入いんにてもかにてをいだを入ねを生たれ少てを入しほ<ins>け</ins>んすい合出是もつまハ時の物惣のこハ鳥汁にい入吉いびゆ吉あをちのたを

### Pred
をなど<ins>二度炊</ins>て候是<ins>末広</ins>の入吉立ハ<ins>二</ins>の<ins>具</ins>汁ハ<ins>火</ins>を<ins>払下</ins>きて<ins>は思</ins>をも<ins>人</ins>入した時<ins>上</ins>げて水にて<ins>冷</ins>酒をかけ<ins>置</ins>く汁時<ins>に</ins>入ぶを<ins>仕上</ins>すい合出又すまの<ins>斗</ins>にけ少候<ins>。</ins>此時ハ<ins>置</ins>くしだい入せ中そにだをくに候どぶをさて吉<ins>に</ins>大ん外<ins>入。</ins>但久く<ins>炊</ins>てハの<ins>味</ins>悪候<ins>秋草</ins>を<ins>炊</ins>の也いつれもそをかうて久敷に候しるにハ此ちすい口<ins>三寸程</ins>の<ins>小</ins>同葉<ins>鶉</ins>の汁だに<ins>骨</ins>を入せんそにて仕立<ins>て</ins>さん大也つまハその時の<ins>形付</ins>吉きの<ins>は</ins>いほ数入吉何時も<ins>種</ins>をおびゆ<ins>。また締</ins>中そにてしたてゟすに汁中に仕立<ins>て</ins>候<ins>。</ins>ま<ins>た</ins>につま時の物也り次入いんにてもかにてをいだを入ねを生たれ少てを入しほ<ins>け</ins>んすい合出是もつまハ時の物惣のこハ鳥汁にい入吉いびゆ吉あをちのたを

### GT
うをなどもふくたうもどきとていたし候是もかわをはぎすてひぶくのかわ入吉立やうハふくたうのくあんかう汁ハかハをはぎおろしきりてかハおもミをもにゑゆへ入しらミたる時あげて水にてひやし其後酒をかけをくミそ汁にへ立候時うをゝ入どぶをさししほかげんすい合出し候也又すましの時ハだし計にかけも少おとし候此時ハうハおきさくしだいに入どせう汁中ミそにだしをくハへよくに申候どぶをさして吉つまハごぼう大こん其外色々但久しくたき候てハミそのあぢ悪候左候へハあたらしきミそをたてさしニて出しよきもの也いつれもミそをかうして久敷に申候しるにハ此こゝろもち入る也すい口さんせうのこ同葉鶴の汁ハだしにほねを入せんじさしミそにて仕立候さしかげん大事也つまハその時のけいぶつ吉きのこハいかほど数入候ても吉何時もすぢをおくすい口わさびゆ又はじめゟ中ミそにてもしたてゟすましにも白鳥汁中ミそにて仕立候又すましにもつまハ時分の物也つくり次第入かハいりハがんにてもかもにてもかハをいりだしを入ほねをせんじ生たれ少さして身を入しほかげんすい合出し候是もつまハ時の物惣別木のこハ鳥汁にいつも入候て吉すい口わさびゆ吉あをかちハきじのわたを

## 200022050_00010_2
  <p align="left">
    <img src="/zero_shot/Llama3-Youko-8B-Instruct/imgs/200022050_00010_2.jpg" width="512" title="details">
  </p>
  
### Input
も有そべまのげんハなをなてあにすのおほくあまり候ハぬか候のしろ鱠ふな<ins>〱</ins>ま<ins>ふ</ins>きふななすを入すにあひり鱠あめのを三まおろ身ハすきてつ両のを打合かハめやききざ入たのいのくきをさがき入すしほげんてあへ候い也ハもしきばきあゆにてもあめのをの<ins>シ</ins>く仕候れも身すきてつり候しやきぬなしをよてさけのくすりあ<ins>にて</ins>にても<ins>出</ins>にまづすにていそのすをすてのちにぬたをすにてのべすんてあへ後のすおほきハ悪候たしあゆにて<ins>は</ins>あをまのぬたにゆのはミ入あ鱠ほのいあいりいりざけすたにてあへ候たあのちに入<ins>さ</ins>けも吉花つほ三月大木くげなどきざ吉<ins>酔</ins>いのうすほねやきむ取て田つりいて川ゑひ木くりしお入てすしほげんしてあ候わびがんかも同けなどつすにて

### Pred
も有そべまの<ins>源</ins>ハなをなてあにすのおほくあまり候ハぬか候の<ins>白</ins>鱠ふな<ins>〱</ins>ま<ins>ふ</ins>きふななすを入<ins>れ</ins>すにあひり鱠<ins>雨</ins>のを三まおろ身ハすきてつ両のを打合かハめやききざ入たのいのくきをさがき入すしほ<ins>源</ins>てあへ候い也ハもしきばきあゆにても<ins>雨</ins>のをの<ins>シ</ins>く仕候れも身すきてつり候しやきぬなしをよてさけのくすりあ<ins>にて</ins>にても<ins>出</ins>にまづすにていそのすをすてのちにぬたをすにてのべすんてあへ後のすおほきハ悪候たしあゆにて<ins>は</ins>あをまのぬたにゆのはミ入あ鱠ほのいあいりいりざけすたにてあへ候たあのちに入<ins>さ</ins>けも吉花つほ三月大木くげなどきざ吉<ins>酔</ins>いのうすほねやきむ取て田つりいて川ゑひ木くりしお入てすしほ<ins>源</ins>してあ候わびがんかも同けなどつすにて

### GT
も有そうべつなますのかげんハなますをミなもりてあとにすのおほくあまり候ハぬかよく候このしろ鱠ふなのくやまぶきあへハふななますをからし入すにあへ申事也ひてり鱠あめのうを三まいにおろし身ハすきてつくり両のかハを打合かハめよりやきてきざミ入たうのいものくきをさゝがき入すしほかげんしてあへ候をいふ也かハもしらやき也かばやき鱠あゆにてもあめのうをのく仕候事也これも身ハすきてつくり候かハしらやきぬたなますからしをよくすりてさけのかすをよくすりあゆにてもいわしにてもなよしにてもまづすにていためそのすをすてのちにぬたをすにてのべすかげんしてあへ候也後のすおほきハ悪候たゞしあゆにてハあをまめのぬたにゆのはきざミ入あへ申事も有太郎助鱠一しほのたいあわひなどいかにもうすくつくりいりざけすたうぶんにしてあへ候たゞしあわひハのちに入吉ますざけも吉花がつほ三月大こん木くらげなどきざミ入て吉やきほね鱠たいのうすミほねなとやきむしり取て田つくりいりて川ゑひ木くらげくりしやうがおろしなと入てすしほかげんしてあへ申候わさびあへがんかも同もゝけなどつくりすにて

## Error Type Summary

The categories below are based on a three-way comparison among `Input`, `Pred`, and `GT`. In short, `Input` is the noisy OCR source, `Pred` is the model's attempted correction, and `GT` is the target transcription.

### 1. Modernization and explanatory rewriting

The most distinctive failure mode is that the model often rewrites the source from Input into modern or explanatory Japanese instead of preserving a faithful transcription. This appears in `100241706_00020_1`, `100241706_00028_1`, `100249376_00017_2`, `100249376_00018_1`, `100249476_00007_2`, `200022050_00006_1`, and `200022050_00010_2`. Pred frequently adds punctuation, uses modern kanji, inserts particles, or paraphrases the content into a more readable form. These outputs can be semantically plausible, but they diverge from the GT transcription target and therefore produce high CER.

### 2. Semantic hallucination and over-interpretation

Several predictions go beyond modernization and introduce content that is not supported by the input. For example, `100241706_00028_1` turns the historical text into a more polished explanatory passage, and `100249376_00017_2` rewrites the preparation procedure with invented or normalized phrasing. This indicates that the model is sometimes solving the task as interpretation or translation rather than OCR correction.

### 3. Input-copying mixed with partial correction

Some long samples combine copied noisy input with selective normalization. `200020019_00034_2`, `200020019_00057_1`, `200020019_00070_2`, `200020019_00077_1`, `200020019_00082_2`, `200022050_00002_2`, `200022050_00006_1`, and `200022050_00010_2` show this pattern. The model keeps large spans of the noisy input, then locally changes some words into common kanji or modern expressions. The result is neither a faithful copy nor a correct transcription.

### 4. Layout/order errors in list-like text

The `200021763_*` samples still show ordering and grouping problems, especially `200021763_00006_2`, `200021763_00008_2`, `200021763_00009_1`, and `200021763_00042_2`. These are structured lists of menu items, vessels, or dish names. The model retains many recognizable texts but fails to reconstruct the correct list sequence and group boundaries. This suggests limited robustness to layout-dependent reading order.

### 5. Length expansion and unstable long-output behavior

Unlike models that mainly truncate near 300 characters, Youko sometimes expands the output substantially. `200021086_00025_2` is the clearest case: Pred_Length is 448 while GT_Length is 288, producing CER above 1.0. This expansion is mostly caused by over-generation and explanatory rewriting. Other long samples also show compression, omission, or semantic drift, so the model is unstable on long passages rather than simply capped at a fixed length.

### 6. Classical kana and short-text character confusions

Short samples such as `200006663_00006_2`, `200017458_00003_1`, `200021869_00003_1`, and `200021869_00012_1` reveal fine-grained errors in historical kana, voicing, small marks, and visually similar characters. Because these samples are short, a few substitutions or omissions can create a high CER. The model also tends to normalize historical forms into familiar modern-looking forms, which compounds the character-level errors.

### 7. Domain vocabulary errors

Cooking, confectionery, menu, and recipe vocabulary is a major source of mistakes. Examples include `100249376_00017_2`, `100249376_00018_1`, `100249416_00034_1`, `100249476_00007_2`, `200022050_00002_2`, `200022050_00006_1`, and `200022050_00010_2`. The model often turns specialized terms, ingredients, measurements, and preparation steps into more common modern expressions. This makes the text easier to read but less faithful to the source.

### Overall

Llama-3-Youko-8B-Instruct has a different error profile from the more copy-oriented models. Its main weakness is over-normalization: it often rewrites or explains the text instead of transcribing it. This creates high CER even when the output is fluent. The model also struggles with list layouts, long passages, short historical-kana fragments, and specialized culinary vocabulary. Future improvements should emphasize strict transcription instructions, suppression of paraphrasing and modernization, layout-aware ordering, and domain adaptation for classical cooking and confectionery texts. 
