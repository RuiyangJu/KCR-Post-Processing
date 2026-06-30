# Llama-3-ELYZA-JP-8B
## Error Case Analysis on Synthetic Test Set (Overall CER: 15.19%)

This README summarizes the zero-shot OCR correction results of Llama-3-ELYZA-JP-8B on the synthetic test set. The overall CER is 15.19%. Each case shows the source image, the OCR input, the model prediction, and the ground-truth transcription so that the main errors can be inspected directly.

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
100241706_00028_1.txt,142,93,100,0.704225352112676
100249416_00034_1.txt,121,125,32,0.2644628099173554
200006663_00006_2.txt,11,24,15,1.3636363636363635
200015843_00110_1.txt,300,300,81,0.27
200017458_00008_1.txt,384,297,88,0.22916666666666666
200017458_00037_2.txt,387,300,94,0.24289405684754523
200021763_00002_2.txt,17,13,5,0.29411764705882354
200021763_00006_2.txt,56,56,33,0.5892857142857143
200021763_00008_2.txt,44,36,35,0.7954545454545454
200021763_00009_1.txt,71,72,34,0.4788732394366197
200021763_00020_1.txt,86,84,71,0.8255813953488372
200021763_00025_1.txt,94,88,53,0.5638297872340425
200021869_00003_1.txt,3,3,1,0.3333333333333333
200021869_00012_1.txt,74,87,22,0.2972972972972973
200022050_00002_2.txt,188,198,78,0.4148936170212766
200022050_00006_1.txt,496,300,206,0.4153225806451613
200022050_00007_2.txt,414,296,122,0.2946859903381642
200022050_00010_2.txt,468,299,176,0.37606837606837606
```

## 100241706_00028_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/100241706_00028_1.jpg" width="512" title="details">
  </p>
  
### Input
すもの干ぐわしといふ<ins>へ仕</ins>んぢう又饅頭いづれの御代の御事なりか止事なき御かた米の御ことぶきを祝奉てあ<ins>た</ins>らげをせいあぐへきよしを仰せ出されけりい<ins>り</ins>ゞ致申べくと伺ひける所八十八才のうへまでも御<ins>果有</ins>をいわ井ま然るべくとにより一つ百の数をかたどり種工夫をめぐらけ所一<ins>ツ</ins>白のは<ins>〱</ins>

### Pred
すもの干ぐわしといふ<ins>へ�assistantすもの干すわしといふへから</ins>んぢう又饅頭いづれの御代の御事なりか止事なき御かた米の御ことぶきを祝奉てあ<ins>た</ins>らげをせいあぐへきよしを仰せ出されけり

### GT
すもの干ぐわしといふ▲まんぢう又饅頭いづれの御代の御事なりしか止事なき御かた米の御ことぶきを祝し奉るとてあふらげをせいしあぐへきよしを仰せ出されけりいかゞ致し申べくと伺ひける所八十八才のうへまでも御寿をいわ井まし然るべくとにより一つ百の数をかたどり種々工夫をめぐらしける所一つ白のはく

## 100249416_00034_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/100249416_00034_1.jpg" width="512" title="details">
  </p>
  
### Input
糀を少入れおけば風味よき甘酒と<ins>ゐ</ins>なる也○上飴<ins>鍋心</ins>一<ins>歯</ins>餅米一升一糀<ins>た</ins>升七合一水七合<ins>此</ins>此水にて糀をあらひは<ins>あふの</ins>ばり取かすを去<ins>は段</ins>米<ins>ど</ins>あま酒につくりなれたる時布にてしよく<ins>練</ins>り是へしるあめ少しかすをよくすりて入れ三<ins>け</ins>日置なり但し折<ins>〱王こ</ins>廻てよし<ins>餅菓子手制衣集終候</ins>

### Pred
糀を少入れおけば風味よき甘酒と<ins>ゐ</ins>なる也○上飴<ins>鍋心</ins>一<ins>歯</ins>餅米一升一糀<ins>た</ins>升七合一水七合<ins>此</ins>此水にて糀をあらひは<ins>あふの</ins>ばり取かすを去<ins>は段</ins>米<ins>ど</ins>あま酒につくりなれたる時布にてしよく<ins>練</ins>り是へしるあめ少しかすをよくすりて入れ三<ins>け</ins>日置なり但し折<ins>り</ins>てよし<ins>餅菓子手制衣集終候</ins>

### GT
糀を少し入れおけば風味よき甘酒ともなる也○上飴練やう一上白餅米一升一糀一升七合一水七合此水にて糀をあらひはなばかり取かすを去右餅米とあま酒につくりなれたる時布にてこしよくねり是へしるあめ少しかすをよくすりて入れ三日置なり但し折々かき廻してよし

## 200006663_00006_2
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200006663_00006_2.jpg" width="512" title="details">
  </p>
  
### Input
夜番たゞ<ins>出</ins>のぶ<ins>ツれえりレけかまさゞ</ins>ゑびす廻国<ins>ま重お</ins>

### Pred
夜番た<ins>だ出</ins>のぶ<ins>つれえりれけかまさず</ins>びす廻国<ins>まさお</ins>

### GT
夜番たゞのぶゑびす廻国

## 200015843_00110_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200015843_00110_1.jpg" width="512" title="details">
  </p>
  
### Input
着物は<ins>もも</ins>より<ins>内多ろ</ins>葉も<ins>敷き</ins>もしらず<ins>てし也がししがは置吉</ins>とい<ins>つ</ins>る家は蔵<ins>ん長</ins>九つ持て<ins>其もぐに代すへ正</ins>のか<ins>さ</ins>りぞか万屋はひそかなる手<ins>ざて</ins>独り<ins>に</ins>に吉太郎とて有しが十三<ins>具</ins>の時鼻<ins>頭小</ins>小杉<ins>人</ins>しを見て<ins>初楽も衛間</ins>の網干に姨有し<ins>かは記</ins>に遣は<ins>か</ins>置那<ins>及</ins>屋<ins>ゑ</ins>と云分限を見ならへと我子は捨て其<ins>る味</ins>が<ins>は</ins>子を<ins>元</ins>立二十五六迄も手代並にはたかせけるに其始末<ins>は</ins>たれ<ins>か参</ins>履迄も拾ひ集め瓜種の用に里へ<ins>迄也</ins>を見て気に<ins>金</ins>是<ins>呼</ins>子分にして家を渡し相<ins>気</ins>の娵を尋<ins>年</ins>けるに世<ins>る</ins>と替り成程悋気つよき女房ならば<ins>元</ins>娵にとり<ins>さ随</ins>と<ins>しれ</ins>ひ<ins>ぜ</ins>は広し思ふま<ins>く</ins>ゝなる娘有<ins>か嫁き</ins>をすまし夫婦は隠<ins>器</ins>をかまへ残らず<ins>後</ins>され<ins>け</ins>けるに此<ins>仁</ins>取金銀有に<ins>ろ</ins>て<ins>分</ins>取出手掛者を聞立旅子<ins>住</ins>ひを心

### Pred
着物は<ins>もも</ins>より<ins>内多ろ</ins>葉も<ins>敷き</ins>もしらず<ins>てし也がししがは置吉</ins>とい<ins>つ</ins>る家は蔵<ins>ん長</ins>九つ持て<ins>其もぐに代すへ正</ins>のか<ins>さ</ins>りぞか万屋はひそかなる手<ins>ざて</ins>独り<ins>に</ins>に吉太郎とて有しが十三<ins>具</ins>の時鼻<ins>頭小</ins>小杉<ins>人</ins>しを見て<ins>初楽も衛間</ins>の網干に姨有し<ins>かは記</ins>に遣は<ins>か</ins>置那<ins>及</ins>屋<ins>ゑ</ins>と云分限を見ならへと我子は捨て其<ins>る味</ins>が<ins>は</ins>子を<ins>元</ins>立二十五六迄も手代並にはたかせけるに其始末<ins>は</ins>たれ<ins>か参</ins>履迄も拾ひ集め瓜種の用に里へ<ins>迄也</ins>を見て気に<ins>金</ins>是<ins>呼</ins>子分にして家を渡し相<ins>気</ins>の娵を尋<ins>年</ins>けるに世<ins>る</ins>と替り成程悋気つよき女房ならば<ins>元</ins>娵にとり<ins>さ随</ins>と<ins>しれ</ins>ひ<ins>ぜ</ins>は広し思ふま<ins>く</ins>ゝなる娘有<ins>か嫁き</ins>をすまし夫婦は隠<ins>器</ins>をかまへ残らず<ins>後</ins>され<ins>け</ins>けるに此<ins>仁</ins>取金銀有に<ins>ろ</ins>て<ins>分</ins>取出手掛者を聞立旅子<ins>住</ins>ひを心

### GT
着物は花色より外は紅葉も藤色もしらず幾春をか送りぬ蔵合といへる家は蔵の数九つ持て富貴なれば是又国のかざりぞかし万屋はひそかなる手前者独り子に吉太郎とて有しが十三才の時鼻紙に小杉入しを見て勘当切幡州の網干に姨有しが此許に遣はし置那波屋殿と云分限を見ならへと我子は捨て其後妹が一子を見立二十五六迄も手代並にはたらかせけるに其始末すたれる草履迄も拾ひ集め瓜種の用に里へ送るを見て気に入是を子分にして家を渡し相応の娵を尋ねけるに世間と替り成程悋気つよき女房ならば我娵にとりたきとの願ひ世は広し思ふまゝなる娘有て縁組をすまし夫婦は隠居をかまへ残らず渡されけるに此跡取金銀有に任て少し取出手掛者を聞立旅子狂ひを心

## 200017458_00008_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200017458_00008_1.jpg" width="512" title="details">
  </p>
  
### Input
御へりなくてひゑいんのふをのといふろにとぢこもせ給ひけりろかづきすゑゆきげのそのあらにさしぐるくものまなくやにゆきかふ人もまれなりりいはんやをの御すまゐ思ひやられてあはれなりこにさいちうじやうありはのなりひらはむの御なさけあさかざり人なりけれ〱たるゆきをふみけなく〱御あをたづねまいて<ins>ん</ins>らすれはまうとつりきたりてうえうあにたりゐんけんしやく〱たりおりにませ人めもくさもかれぬればいびきにみなしろたえのにはのおもあみつくる人なみはぢくいでさせ給ひてんでんの御かう三げんばりあげての山を御らんめぐしげにやははあをくなつはしげりあきはそめふゆはおつといふせめい太のおぼめつねろほのゆきをばすだれをかげてみん

### Pred
御へりなくてひゑいんのふをのといふろにとぢこもせ給ひけりろかづきすゑゆきげのそのあらにさしぐるくものまなくやにゆきかふ人もまれなりりいはんやをの御すまゐ思ひやられてあはれなりこにさいちうじやうありはのなりひらはむの御なさけあさかざり人なりけれたるゆきをふみけなく御あをたづねまいて<ins>ん</ins>らすれはまうとつりきたりてうえうあにたりゐんけんしやくたりおりにませ人めもくさもかれぬればいびきにみなしろたえのにはのおもあみつくる人なみはぢくいでさせ給ひてんでんの御かう三げんばりあげての山を御らんめぐしげにやははあをくなつはしげりあきはそめふゆはおつといふせめい太のおぼめつねろほのゆきをばすだれをかげてみん

### GT
御かへりなくしてひゑいざんのふもとをのといふところにとぢこもらせ給ひけりころはかみなづきすゑゆきげのそらのあらしにさえしぐるゝくものたえまなくみやこにゆきかふ人もまれなりけりいはんやをのゝ御すまゐ思ひやられてあはれなりこゝにさいごちうじやうありはらのなりひらはむかしの御なさけあさからざりし人なりければふん〱たるゆきをふみわけなく〱御あとをたづねまいりて見まいらすれはまうとううつりきたりてこうえうあらしにたえりうゐんけんがとうしやく〱たりおりにまかせ人めもくさもかれぬれば山ざといとゞさびしきにみなしろたえのにはのおもあとふみつくる人もなしみこははしぢかくいでさせ給ひてなんでんの御かうし三げんばかりあげてよもの山を御らんじめぐらしげにやはるはあをくなつはしげりあきはそめふゆはおつるといふせうめい太しのおぼしめしつらねかうろほうのゆきをばすだれをかゝげてみるらんと

## 200017458_00037_2
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200017458_00037_2.jpg" width="512" title="details">
  </p>
  
### Input
<ins>ば</ins>へんるろにや五郎ひなくつつきち<ins>ら</ins>たをいてはなしろにおすたりいきほひたたきぐちあへなくまけしばしばらすまふなりけるや五郎はげんしつたきぐちにかちて百<ins>干</ins>ばんのまけもものなずれにつそれけれなにものなりともと思ふ<ins>の</ins>につら山の又七いで手にもたますまけてのちくつきやうのすふ五ばんまでかちてたつたるありさまはきほひあまりてぞ見けるにさのくにのぢ人やきしたの小六郎出てあひはのや五をはめてよきすまふ六ばんつるのくにのぢう人たけのしたのまご八いで<ins>く</ins>小六郎をめてきすまふ九<ins>は</ins>んつていんろにがしやまたの五郎いで<ins>く</ins>まご八をめてよきすふばんかちければいでとんいふのなするがのくにたのち六いざやとんいふそにありけるゑびなのひ

### Pred
<ins>ば</ins>へんるろにや五郎ひなくつつきち<ins>ら</ins>たをいてはなしろにおすたりいきほひたたきぐちあへなくまけしばしばらすまふなりけるや五郎はげんしつたきぐちにかちて百<ins>干</ins>ばんのまけもものなずれにつそれけれなにものなりともと思ふ<ins>の</ins>につら山の又七いで手にもたますまけてのちくつきやうのすふ五ばんまでかちてたつたるありさまはきほひあまりてぞ見けるにさのくにのぢ人やきしたの小六郎出てあひはのや五をはめてよきすまふ六ばんつるのくにのぢう人たけのしたのまご八いで<ins>く</ins>小六郎をめてきすまふ九<ins>は</ins>んつていんろにがしやまたの五郎いで<ins>く</ins>まご八をめてよきすふばんかちければいでとんいふのなするがのくにたのち六いざやとんいふそにありけるゑびなのひ

### GT
はうさへんとするところにや五郎ひまなくつつといりたきぐちがこまたをかいてはなしろにおしすへたりいきほひたるたきぐちあへなくまけしかばしばらくすまふぞなかりけるや五郎はかうげんしつるたきぐちにかちて百千ばんのまけもものならずこれにかつこそうれしけれなにものなりともと思ふところにがつら山の又七いでゝ手にもたまらすまけてのちくつきやうのすまふ五ばんまでかちてたつたるありさまはいきほひあまりてぞ見えけるこゝにさがみのくにのぢう人やきしたの小六郎出てあひざはのや五郎をはじめとしてよきすまふ六ばんかつするがのくにのぢう人たけのしたのまご八いでゝ小六郎をはじめとしてよきすまふ九ばんかつていらんとするところに大ばがしやていまたのゝ五郎いでゝまご八をはじめとしてよきすまふ十ばんかちければいでゝとらんといふものなしするがのくにたかはしのちう六いざやとらんといふそばにありけるゑびなのひ

## 200021763_00002_2
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200021763_00002_2.jpg" width="512" title="details">
  </p>
  
### Input
七詰膳並据様五詰膳並据様<ins>く</ins>

### Pred
七詰膳並据様五詰膳並据様<ins>く</ins>

### GT
七詰膳並据様五詰膳並据様膳部料理抄

## 200021763_00006_2
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200021763_00006_2.jpg" width="512" title="details">
  </p>
  
### Input
平皿<ins>飯鉢</ins>七ツ目<ins>蓋台</ins>中合サ汁再進<ins>煎物</ins>島台土器<ins>飯鉢押肴二種蓋台箸汁再進銚子島台土器提子</ins>押肴二種箸杯台<ins>銚子</ins>平銚子台<ins>提子</ins>

### Pred
平皿<ins>飯鉢</ins>七ツ目<ins>蓋台</ins>中合サ汁再進<ins>煎物</ins>島台土器<ins>飯鉢押肴二種蓋台箸汁再進銚子島台土器提子</ins>押肴二種箸杯台<ins>銚子</ins>平銚子台<ins>提子</ins>

### GT
平皿七ツ目中合サ煎物飯鉢蓋台汁再進島台土器押肴二種箸銚子提子飯鉢蓋台汁再進島台土器押肴二種箸銚子提子杯台平銚子台

## 200021763_00008_2
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200021763_00008_2.jpg" width="512" title="details">
  </p>
  
### Input
飯鉢<ins>飯鉢蓋台</ins>蓋台汁再進汁再進置杯<ins>置杯平銚子</ins>平銚子吸物<ins>吸物肴二種</ins>肴二種湯水<ins>湯水</ins>茶菓子<ins>茶菓子</ins>

### Pred
<ins>飯鉢</ins>飯鉢蓋台<ins>蓋台</ins>汁<ins>次汁次置杯</ins>置杯平銚子平銚子吸物<ins>吸物肴二種</ins>肴二種湯水<ins>湯水</ins>

### GT
飯鉢蓋台汁再進置杯平銚子吸物肴二種湯水茶菓子飯鉢蓋台汁再進置杯平銚子吸物肴二種湯水茶菓子

## 200021763_00009_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200021763_00009_1.jpg" width="512" title="details">
  </p>
  
### Input
濃茶濃茶後菓子<ins>後菓子薄茶</ins>薄茶以上七詰五詰に次たる尊<ins>る々</ins>の御方の<ins>饗</ins>応御料理なり二汁七菜二汁五菜本膳<ins>本膳膾直汁</ins>膾汁<ins>黍</ins>香物箸煎物<ins>香物箸</ins>坪皿飯<ins>坪以皿飯</ins>

### Pred
濃茶濃茶後菓子<ins>後菓子薄茶</ins>薄茶以上七詰五詰に次たる尊<ins>る々</ins>の御方の<ins>饗</ins>応御料理なり二汁七菜<ins>二汁五菜本膳</ins>本膳膾<ins>直</ins>汁<ins>膾汁黍香物箸煎物</ins>香物箸煎物坪皿飯<ins>以</ins>皿飯

### GT
濃茶後菓子薄茶濃茶後菓子薄茶以上七詰五詰に次たる尊貴の御方の餐応御料理なり二汁七菜本膳膾汁小皿香物箸煎物坪皿飯二汁五菜本膳膾汁香物箸煎物坪皿飯

## 200021763_00020_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200021763_00020_1.jpg" width="512" title="details">
  </p>
  
### Input
引向おま<ins>半</ins>鯛二玉子ふわ〱<ins>長皿ふた物</ins>薄鳥<ins>平皿御所麩</ins>猪口薄<ins>モ</ins>雪<ins>主花かつ尾</ins>ふ<ins>くる之</ins>焼物一しほかれゐ懸下け<ins>肴一鳥鴨</ins>銚子<ins>すれんこん</ins>吸物花<ins>以</ins>か<ins>ぜらかし</ins>こせ<ins>銚子</ins>肴<ins>湯</ins>鯖粧漬湯<ins>石</ins>する<ins>州する</ins>

### Pred
引向おま<ins>半</ins>鯛<ins>二玉子ふわ長皿ふた物薄鳥</ins>平皿御所麩猪口薄も<ins>雪主花かつ尾</ins>ふ<ins>くる之</ins>焼物一しほかれ<ins>居</ins>懸下け<ins>肴一鳥鴨</ins>銚子<ins>すれんこん</ins>吸物花<ins>以</ins>か<ins>ぜらかし</ins>こせ<ins>銚子</ins>肴<ins>湯</ins>鯖粧漬湯<ins>石</ins>する<ins>州する</ins>

### GT
引向長皿おまつ鯛平皿御所麩花かつおくるミ肴一鳥鴨一すれんこんせうか銚子湯する二ふた物玉子ふわ〱薄鳥猪口薄雪もミふし焼物一しほかれゐ懸下け銚子吸物花いかこせう肴一鯖粧漬湯する

## 200021763_00025_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200021763_00025_1.jpg" width="512" title="details">
  </p>
  
### Input
七詰五詰の組合<ins>花</ins>積立<ins>ミ</ins>略図本膳鯛作り身<ins>も錦鱠</ins>細作り魚<ins>汁小かふ</ins>く大根<ins>しい茸</ins>せか<ins>皮牛房</ins>房風<ins>青な</ins>杉小<ins>金</ins>角<ins>此かん</ins>なら漬瓜<ins>香物</ins>ミそ漬大根<ins>之</ins>もり口漬花塩山升杉曲物焼魚<ins>煮物</ins>花ゑひ<ins>飯</ins>くしこ敷葛

### Pred
七詰五詰の組合<ins>花</ins>積立<ins>ミ</ins>略図本膳鯛作り身<ins>も錦鱠</ins>細作り魚<ins>汁小かふ</ins>く大根<ins>しい茸</ins>せか<ins>皮牛房</ins>房風<ins>青な</ins>杉小<ins>金</ins>角<ins>此かん</ins>なら漬瓜<ins>香物</ins>ミそ漬大根<ins>之</ins>もり口漬花塩山升杉曲物焼魚<ins>煮物</ins>花ゑひ<ins>飯</ins>くしこ敷葛

### GT
七詰五詰の組合并積立之略図本膳膾煮物香物汁飯膾鯛作り身細作り魚くり大根せうか房風金かん杉小角香物なら漬瓜ミそ漬大根もり口漬花塩山升杉曲物煮物焼魚花ゑひくしこ敷葛汁鶴小かふしい茸皮牛房青な飯

## 200021869_00003_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200021869_00003_1.jpg" width="512" title="details">
  </p>
  
### Input
<ins>ゝ</ins>右一<ins>は</ins>

### Pred
右一<ins>は</ins>

### GT
右一水

## 200021869_00012_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200021869_00012_1.jpg" width="512" title="details">
  </p>
  
### Input
かまほこ拵方<ins>し</ins>事玉子そふめんの如にそれを<ins>ほ</ins>竹の<ins>れ同比ほ</ins>二ツ割し両方<ins>て更</ins>ふ<ins>し</ins>しを付其中へ入さ<ins>しそ</ins>をうす<ins>て</ins>そきもよふなる<ins>に</ins>ふに入へしそれをふ<ins>ゝ</ins>かし外へ玉子を<ins>ぬ</ins>るへ<ins>へ</ins>し<ins>青意ケわしぞ</ins>

### Pred
かまほこ拵方<ins>し</ins>事玉子そふめんの如にそれを<ins>ほ</ins>竹の<ins>れ同比ほ</ins>二ツ割し両方<ins>て更</ins>ふ<ins>し</ins>しを付其中へ入さ<ins>しそ</ins>をうす<ins>て</ins>そきもよふなる<ins>に</ins>ふに入へしそれをふ<ins>ゝ</ins>かし外へ玉子を<ins>ぬ</ins>るへ<ins>へ</ins>し<ins>青意ケわしぞ</ins>

### GT
かまほこ拵方之事玉子そふめんの如にそれを竹の筒を二ツ割し両方へふしを付其中へ入さかなをうすくそきもよふなるよふに入へしそれをふかし外へ玉子をふるへし

## 200022050_00002_2
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200022050_00002_2.jpg" width="512" title="details">
  </p>
  
### Input
▲祝言引渡之次第一<ins>歌</ins>栗ほそきかたをむ<ins>に也んレ一三ツかわらけ</ins>成やうに三かくにお<ins>ゝ</ins>也<ins>也</ins>一のし二本<ins>寸すま</ins>ひろきかたをきやくのひだりの<ins>ぶ</ins>かたへしておきて<ins>こか</ins>し昆布切かぶなて<ins>りたに</ins>也一てうしひさ<ins>けきりお</ins>一まきずるめ<ins>のさ</ins>か<ins>なかレ事</ins>すミ一か<ins>かす</ins>こしもちくしこむすびこんぶ<ins>一むめぼし三ツざうに</ins>いもひ<ins>ら</ins>かつうほくしあ<ins>げひ</ins>一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとす<ins>ま</ins>也一ねぶか二本しろに<ins>ね</ins>一か<ins>かん</ins>んざけ<ins>とも</ins>

### Pred
▲祝言引渡之次第一<ins>歌</ins>栗ほそきかたをむ<ins>に也んレ一三ツかわらけ</ins>成やうに三かくにお<ins>ゝ</ins>也<ins>也</ins>一のし二本<ins>寸すま</ins>ひろきかたをきやくのひだりの<ins>ぶ</ins>かたへしておきて<ins>こか</ins>し昆布切かぶなて<ins>りたに</ins>也一てうしひさ<ins>けきりお</ins>一まきずるめ<ins>のさ</ins>か<ins>なかレ事</ins>すミ一か<ins>かす</ins>こしもちくしこむすびこんぶ<ins>一むめぼし三ツざうに</ins>いもひ<ins>ら</ins>かつうほくしあ<ins>げひ</ins>一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとす<ins>ま</ins>也一ねぶか二本しろに<ins>ね</ins>一か<ins>かん</ins>んざけ<ins>とも</ins>

### GT
▲祝言引渡之次第一栗ほそきかたをむふへ成やうに三かくにおく也一三ツかわらけ一のし二本ひろきかたをきやくのひだりのかたへしておきてよし一昆布二切かぶなりにきりておく也一てうしひさげ一さかな一まきずるめ一からすミ一かずのこ一むめぼし三ツざうにもちくしこむすびこんぶいもひゝかつうほくしあわび一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとする也一ねぶか二本しろねともに一かんざけ

## 200022050_00006_1
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200022050_00006_1.jpg" width="512" title="details">
  </p>
  
### Input
をなどふたどきてい候是すてひの入吉立ハふたのくあん汁ハかハをはぎおろきて<ins>は</ins>おもミをも<ins>人</ins>入した時あげて水にてひや酒をかけをく汁時入ぶをしほげんすい合出又すまの<ins>斗</ins>にけ少候此時ハおきくしだい入せ中そにだをくに候どぶをさて吉<ins>に</ins>大ん外<ins>入</ins>但久くたきてハのあぢ悪候あきそをたきの也いつれもそをかうて久敷に候しるにハ此ちすい口さんせのこ同葉<ins>鶉</ins>の汁だにほねを入せんそにて仕立さん大也つまハその時のけい<ins>ふ</ins>つ吉きの<ins>は</ins>いほ数入吉何時もすぢをおびゆ又<ins>し</ins>めゟ中そにてしたてゟすに汁中て仕立候又につま時の物也り次入いんにてもかにてをいだを入ねを生たれ少てを入しほ<ins>け</ins>んすい合出是もつまハ時の物惣のこハ鳥汁にい入吉いびゆ吉あをちのたを

### Pred
をなどふたどきてい候是すてひの入吉立ハふたのくあん汁ハかハをはぎおろきて<ins>は</ins>おもミをも<ins>人</ins>入した時あげて水にてひや酒をかけをく汁時入ぶをしほげんすい合出又すまの<ins>斗</ins>にけ少候此時ハおきくしだい入せ中そにだをくに候どぶをさて吉<ins>に</ins>大ん外<ins>入</ins>但久くたきてハのあぢ悪候あきそをたきの也いつれもそをかうて久敷に候しるにハ此ちすい口さんせのこ同葉<ins>鶉</ins>の汁だにほねを入せんそにて仕立さん大也つまハその時のけい<ins>ふ</ins>つ吉きの<ins>は</ins>いほ数入吉何時もすぢをおびゆ又<ins>し</ins>めゟ中そにてしたてゟすに汁中て仕立候又につま時の物也り次入いんにてもかにてをいだを入ねを生たれ少てを入しほ<ins>け</ins>んすい合出是もつまハ時の物惣のこハ鳥汁にい入吉いびゆ吉あをちのたを

### GT
うをなどもふくたうもどきとていたし候是もかわをはぎすてひぶくのかわ入吉立やうハふくたうのくあんかう汁ハかハをはぎおろしきりてかハおもミをもにゑゆへ入しらミたる時あげて水にてひやし其後酒をかけをくミそ汁にへ立候時うをゝ入どぶをさししほかげんすい合出し候也又すましの時ハだし計にかけも少おとし候此時ハうハおきさくしだいに入どせう汁中ミそにだしをくハへよくに申候どぶをさして吉つまハごぼう大こん其外色々但久しくたき候てハミそのあぢ悪候左候へハあたらしきミそをたてさしニて出しよきもの也いつれもミそをかうして久敷に申候しるにハ此こゝろもち入る也すい口さんせうのこ同葉鶴の汁ハだしにほねを入せんじさしミそにて仕立候さしかげん大事也つまハその時のけいぶつ吉きのこハいかほど数入候ても吉何時もすぢをおくすい口わさびゆ又はじめゟ中ミそにてもしたてゟすましにも白鳥汁中ミそにて仕立候又すましにもつまハ時分の物也つくり次第入かハいりハがんにてもかもにてもかハをいりだしを入ほねをせんじ生たれ少さして身を入しほかげんすい合出し候是もつまハ時の物惣別木のこハ鳥汁にいつも入候て吉すい口わさびゆ吉あをかちハきじのわたを

## 200022050_00007_2
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200022050_00007_2.jpg" width="512" title="details">
  </p>
  
### Input
ほをつけうち<ins>書</ins>べてや也しぎやきなすびゆでよき比ににさんせミそをけてや也やき竹の子竹の子のふをぬきへまぼこたまごまろにて入かハにやて切まぼこのほか<ins>ぬ</ins>にして吉りきを大きにつくりりかけをきてかハをい身をはさ入なべてまいならびにやりしるなくハけをきたるたいべきなり第四すい物の部の花いのせのたをすぢい十文まに切け又大さよき<ins>比</ins>に切はゆにをしてつまにのりなにけをおふせすい合いたみのにたまごをあげしにけくをにゆ入候是もつま色汁同前のよき比に切すミそにだを入ふき時わたを入すい合出候也まだこしゆにてさ〱いりさかけのなき時白水をだたまくハふせてすい口ゆを切其入第五酒の部玉子酒玉子をあけひやざけを入てしほを少入んをて

### Pred
ほをつけうち<ins>書け</ins>てや也しぎやきなすびゆでよき比ににさんせミそをけてや也やき竹の子竹の子のふをぬきへまぼこたまごまろにて入かハにやて切まぼこのほか<ins>ぬ</ins>にして吉りきを大きにつくりりかけをきてかハをい身をはさ入なべてまいならびにやりしるなくハけをきたるたいべきなり第四すい物の部の花いのせのたをすぢい十文まに切け又大さよき<ins>比</ins>に切はゆにをしてつまにのりなにけをおふせすい合いたみのにたまごをあげしにけくをにゆ入候是もつま色汁同前のよき比に切すミそにだを入ふき時わたを入すい合出候也まだこしゆにてさかけのなき時白水をだたまくハふせてすい口ゆを切其入第五酒の部玉子酒玉子をあけひやざけを入てしほを少入んをて

### GT
ほをつけうちくべてやく也しぎやきなすびをゆでよき比に切くしにさしさんせうミそをつけてやく也やき竹の子竹の子のふしをぬき中へかまぼこたまごまろにして入かハともにやきて切かまぼこのしほからめにして吉いりやきかもを大きにつくりたまりかけをきてかハをいり身をはさミ入なべにて一まいならびにやく也あまりしるなくハかけをきたるたまりすこしいるべきなり第四すい物の部うの花いかのせのかたをすぢかい十文字にこまかに切かけ又大さよき此に切はなしゆにをしてつまにのりなど入だしにかけをおとしふかせすい合いたし候也みのにたまごをあげしやくしにてうけくだけしをにへゆへ入候是もつま色々汁同前このわたよき比に切うすミそにだしを入ふき立候時わたを入すい合其まゝ出し候也まつだけこしゆにてさハ〱といりさかけのなき時白水をさしだしたまりくハへふかせ候てすい口ゆを切其まゝ入てよし第五りやうり酒の部玉子酒玉子をあけひやざけを少ツヽ入よくときてしほを少入かんをして

## 200022050_00010_2
  <p align="left">
    <img src="/zero_shot/Llama-3-ELYZA-JP-8B/imgs/200022050_00010_2.jpg" width="512" title="details">
  </p>
  
### Input
も有そべまのげんハなをなてあにすのおほくあまり候ハぬか候のしろ鱠ふな<ins>〱</ins>ま<ins>ふ</ins>きふななすを入すにあひり鱠あめのを三まおろ身ハすきてつ両のを打合かハめやききざ入たのいのくきをさがき入すしほげんてあへ候い也ハもしきばきあゆにてもあめのをの<ins>シ</ins>く仕候れも身すきてつり候しやきぬなしをよてさけのくすりあ<ins>にて</ins>にても<ins>出</ins>にまづすにていそのすをすてのちにぬたをすにてのべすんてあへ後のすおほきハ悪候たしあゆにて<ins>は</ins>あをまのぬたにゆのはミ入あ鱠ほのいあいりいりざけすたにてあへ候たあのちに入<ins>さ</ins>けも吉花つほ三月大木くげなどきざ吉<ins>酔</ins>いのうすほねやきむ取て田つりいて川ゑひ木くりしお入てすしほげんしてあ候わびがんかも同けなどつすにて

### Pred
も有そべまのげんハなをなてあにすのおほくあまり候ハぬか候のしろ鱠ふなま<ins>ふ</ins>きふななすを入すにあひり鱠あめのを三まおろ身ハすきてつ両のを打合かハめやききざ入たのいのくきをさがき入すしほげんてあへ候い也ハもしきばきあゆにてもあめのをの<ins>シ</ins>く仕候れも身すきてつり候しやきぬなしをよてさけのくすりあ<ins>にて</ins>にても<ins>出</ins>にまづすにていそのすをすてのちにぬたをすにてのべすんてあへ後のすおほきハ悪候たしあゆにて<ins>は</ins>あをまのぬたにゆのはミ入あ鱠ほのいあいりいりざけすたにてあへ候たあのちに入<ins>さ</ins>けも吉花つほ三月大木くげなどきざ吉<ins>酔</ins>いのうすほねやきむ取て田つりいて川ゑひ木くりしお入てすしほげんしてあ候わびがんかも同けなどつすにて

### GT
も有そうべつなますのかげんハなますをミなもりてあとにすのおほくあまり候ハぬかよく候このしろ鱠ふなのくやまぶきあへハふななますをからし入すにあへ申事也ひてり鱠あめのうを三まいにおろし身ハすきてつくり両のかハを打合かハめよりやきてきざミ入たうのいものくきをさゝがき入すしほかげんしてあへ候をいふ也かハもしらやき也かばやき鱠あゆにてもあめのうをのく仕候事也これも身ハすきてつくり候かハしらやきぬたなますからしをよくすりてさけのかすをよくすりあゆにてもいわしにてもなよしにてもまづすにていためそのすをすてのちにぬたをすにてのべすかげんしてあへ候也後のすおほきハ悪候たゞしあゆにてハあをまめのぬたにゆのはきざミ入あへ申事も有太郎助鱠一しほのたいあわひなどいかにもうすくつくりいりざけすたうぶんにしてあへ候たゞしあわひハのちに入吉ますざけも吉花がつほ三月大こん木くらげなどきざミ入て吉やきほね鱠たいのうすミほねなとやきむしり取て田つくりいりて川ゑひ木くらげくりしやうがおろしなと入てすしほかげんしてあへ申候わさびあへがんかも同もゝけなどつくりすにて

## Error Type Summary

The categories below are based on a three-way comparison among `Input`, `Pred`, and `GT`. In short, `Input` is the noisy OCR source, `Pred` is the model's attempted correction, and `GT` is the target transcription.

### 1. Input-copying without sufficient correction

The largest group of errors comes from copying the noisy Input almost directly. This is visible in `100249416_00034_1`, `200015843_00110_1`, `200017458_00008_1`, `200017458_00037_2`, `200022050_00006_1`, `200022050_00007_2`, and `200022050_00010_2`. Pred often preserves the same OCR-like corruptions as Input, while GT contains substantial corrections. This behavior keeps the output superficially close to the source length, but it does not solve the correction task.

### 2. Generation or cleaning artifacts

`100241706_00028_1` contains an unusual artifact: the prediction includes a replacement character and the literal string `assistant`. This looks different from ordinary OCR or transcription error and suggests a generation-format, tokenization, or output-cleaning issue. Because the sample is also shortened relative to GT, the artifact combines with omission and causes a very high CER.

### 3. Layout/order errors in list-like text

The `200021763_*` cases are dominated by list-structure problems. These samples contain menu items, vessels, dish names, and repeated ordered groups. The model often keeps recognizable local tokens, but the grouping and reading order do not match GT. `200021763_00008_2`, `200021763_00020_1`, and `200021763_00025_1` show that the model is weak at reconstructing structured lists from a noisy or layout-dependent input.

### 4. Long-context degradation and length-limit behavior

Several difficult cases are long passages: `200017458_00008_1`, `200017458_00037_2`, `200022050_00002_2`, `200022050_00006_1`, `200022050_00007_2`, and `200022050_00010_2`. Pred lengths often cluster near 296-300 characters, which suggests an output cap or truncation-like behavior. The beginning of the prediction is usually more stable, while later parts are copied from Input, omitted, or only lightly corrected. This produces high CER even when the local text looks plausible.

### 5. Classical kana and short-text character confusions

Short samples such as `200006663_00006_2`, `200021763_00002_2`, and `200021869_00003_1` expose fine-grained character-level errors. These include voicing differences, small marks, historical kana, and visually similar characters. In very short texts, a few character substitutions or omissions can produce a large CER, even when the absolute number of mistakes is small.

### 6. Modernization and semantic normalization

The model sometimes shifts historical forms toward more familiar modern-looking Japanese. This is especially visible in cases where the predicted text uses cleaner or more regular forms than the diplomatic GT would allow. Such normalization may improve readability, but it is penalized because the target is faithful transcription rather than modernized interpretation.

### 7. Domain vocabulary errors

Recipe and culinary terminology remains a major source of errors. Cases such as `100249416_00034_1`, `200022050_00002_2`, `200022050_00006_1`, `200022050_00007_2`, and `200022050_00010_2` contain ingredients, preparation steps, vessels, seasonings, measurements, and dish names. The model frequently copies noisy domain terms or makes only partial corrections, indicating that general Japanese knowledge is not enough for stable recovery of specialized classical culinary vocabulary.

### Overall

Llama-3-ELYZA-JP-8B shows three main weaknesses on these error cases. First, it often copies the noisy input instead of performing robust correction. Second, it struggles with layout-sensitive lists and long passages, especially when output length approaches the 300-character range. Third, it has some model/output artifact risk, as shown by `100241706_00028_1`. Future improvements should focus on stricter output cleaning, stronger correction behavior, layout-aware reading-order recovery, explicit long-output handling, and domain adaptation for classical culinary and menu texts.
