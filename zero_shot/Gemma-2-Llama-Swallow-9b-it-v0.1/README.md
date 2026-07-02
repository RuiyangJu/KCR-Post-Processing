# Gemma-2-Llama-Swallow-9b-it-v0.1
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
100249376_00010_2.txt,114,1223,1113,9.763157894736842
100249376_00041_2.txt,41,39,15,0.36585365853658536
100249416_00027_1.txt,130,116,26,0.2
100249416_00034_1.txt,121,128,32,0.2644628099173554
100249476_00004_1.txt,204,210,46,0.22549019607843138
200006663_00006_2.txt,11,24,14,1.2727272727272727
200017458_00008_1.txt,384,300,85,0.22135416666666666
200017458_00037_2.txt,387,300,94,0.24289405684754523
200020019_00077_1.txt,262,214,119,0.4541984732824427
200021763_00006_2.txt,56,56,33,0.5892857142857143
200021763_00008_2.txt,44,44,37,0.8409090909090909
200021763_00009_1.txt,71,71,35,0.49295774647887325
200021763_00020_1.txt,86,85,71,0.8255813953488372
200021763_00025_1.txt,94,88,53,0.5638297872340425
200021869_00003_1.txt,3,3,1,0.3333333333333333
200021869_00007_1.txt,122,140,30,0.2459016393442623
200021869_00012_1.txt,74,87,22,0.2972972972972973
200022050_00002_2.txt,188,195,84,0.44680851063829785
200022050_00006_1.txt,496,300,206,0.4153225806451613
200022050_00007_2.txt,414,300,120,0.2898550724637681
200022050_00010_2.txt,468,300,176,0.37606837606837606
```

## 100249376_00010_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/100249376_00010_2.jpg" width="512" title="details">
  </p>
  
### Input
古今名物御前菓子秘伝抄<ins>さた</ins>一あるへいたう上〻氷沙糖一返洗捨沙糖壱升に水二升入さたうのとけ申程せん絹にてこ其後せんしつめさじにてすこしす<ins>ゝ</ins>ひ水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひ

### Pred
古今名物御前菓子秘伝抄<ins>さた</ins>一あるへいたう上〻氷沙糖一返洗捨沙糖壱升に水二升入さたうのとけ申程せん絹にてこ其後せんしつめさじにてすこしす<ins>ゝ</ins>ひ水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひ<ins>やしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひやしうすくのはしはり〱とおれ申時平</ins>

### GT
古今名物御前菓子秘伝抄一あるへいたう上〻氷沙糖一返洗捨沙糖壱升に水二升入さたうのとけ申程せんし絹にてこし其後せんしつめさじにてすこしすくひ水にひやしうすくのはしはり〱とおれ申時平銅なへにくるみの油をぬり其中へうつし鍋こしに水にひ

## 100249376_00041_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/100249376_00041_2.jpg" width="512" title="details">
  </p>
  
### Input
にしてなまた<ins>い</ins>に入む申<ins>申せ</ins>八二やうかり粉にいたしかんの<ins>と</ins>くに<ins>は</ins>八十三唐あめ拾匁わらひ<ins>や</ins>

### Pred
にしてなまた<ins>い</ins>に<ins>ゅう</ins>む申<ins>申せ</ins>八二やうかり<ins>こな</ins>し<ins>と</ins>くに<ins>は</ins>八十三唐あめ拾匁わらひ<ins>や</ins>

### GT
にしてなまたに入むし申候八十二やうかり粉にいたしかんのくに八十三唐あめ拾匁わらひの

## 100249416_00027_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/100249416_00027_1.jpg" width="512" title="details">
  </p>
  
### Input
○かるめろう氷砂糖一斤水<ins>ひたく</ins>に入玉子少し入よくせんじ<ins>ま</ins>いのうにて<ins>と</ins>しそ<ins>る</ins>水を又せんじ手をはなさずねりつめあはだ<ins>ぢ</ins>たる時火をはな鍋のまにてよくさましのみにておろ切るなり○<ins>美</ins>寒赤<ins>に</ins>豆二升砂糖斤一葛の粉七合鍋ず少々こせう少<ins>し</ins>丁子少<ins>し</ins>肉桂少<ins>し</ins>

### Pred
かるめろ氷砂糖一斤水<ins>ひたく</ins>に入玉子少し入よくせんじ<ins>ま</ins>いのうにて<ins>と</ins>しそ<ins>る</ins>水を又せんじ手をはなさずねりつめあはだ<ins>ぢ</ins>たる時火をはな鍋のまにてよくさましのみにておろ切るなり○<ins>美</ins>寒赤<ins>に</ins>豆二升砂糖斤一葛の粉七合鍋ず少々こせう少<ins>し</ins>丁子少<ins>し</ins>肉桂少<ins>し</ins>

### GT
○かるめろう一氷砂糖一斤水すこしに入玉子少し入よくせんじすいのうにてこしその水を又せんじ手をはなさずねりつめあはだちたる時火をはなし鍋のまゝにてよくさましのみにておろし切るなり○羙寒一赤小豆二升一砂糖一斤一葛の粉七合一鍋ずみ少々一こせう少々一丁子少々一肉桂少々

## 100249416_00034_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/100249416_00034_1.jpg" width="512" title="details">
  </p>
  
### Input
糀を少入れおけば風味よき甘酒と<ins>ゐ</ins>なる也○上飴<ins>鍋心</ins>一<ins>歯</ins>餅米一升一糀<ins>た</ins>升七合一水七合<ins>此</ins>此水にて糀をあらひは<ins>あふの</ins>ばり取かすを去<ins>は段</ins>米<ins>ど</ins>あま酒につくりなれたる時布にてしよく<ins>練</ins>り是へしるあめ少しかすをよくすりて入れ三<ins>け</ins>日置なり但し折<ins>〱王こ</ins>廻てよし<ins>餅菓子手制衣集終候</ins>

### Pred
糀を少入れおけば風味よき甘酒と<ins>ゐ</ins>なる也○上飴<ins>鍋心</ins>一<ins>歯</ins>餅米一升一糀<ins>た</ins>升七合一水七合<ins>此</ins>此水にて糀をあらひは<ins>あふの</ins>ばり取かすを去<ins>は段</ins>米<ins>ど</ins>あま酒につくりなれたる時布にてしよく<ins>練</ins>り是へしるあめ少しかすをよくすりて入れ三<ins>け</ins>日置なり但し折<ins>〱王こ</ins>廻てよし<ins>餅菓子手制衣集終候</ins>

### GT
糀を少し入れおけば風味よき甘酒ともなる也○上飴練やう一上白餅米一升一糀一升七合一水七合此水にて糀をあらひはなばかり取かすを去右餅米とあま酒につくりなれたる時布にてこしよくねり是へしるあめ少しかすをよくすりて入れ三日置なり但し折々かき廻してよし

## 100249476_00004_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/100249476_00004_1.jpg" width="512" title="details">
  </p>
  
### Input
常に如此て米を喰のばすなり分量は米壱舛にきらず壱舛入てよし米壱<ins>耳</ins>の手まへにておよそ四合余<ins>針れら</ins>なれば大<ins>宗</ins>に益あり○<ins>声車</ins>唐なす京に<ins>豊</ins>てかぼち<ins>ヤ南京瓜飯</ins>西国すじにてはぼうぶ<ins>か</ins>といふ南京瓜をいつもにしめにする時よりは細かにき<ins>か</ins>て米と一所に釜へ入常の水かげん<ins>生ゝ</ins>塩を入い<ins>し</ins>れ<ins>や</ins>て<ins>う</ins>も<ins>ゆ</ins>よ<ins>を</ins>したきあげしばらく熟し杓子にてよくまぜ合<ins>か</ins>つして食すべし随分よきも<ins>るも</ins>分量は見合に入てよし米一舛の手まへにて三四合は徳分なり

### Pred
常に如此て米を喰のばすなり<ins>。</ins>分量は米壱舛にきらず<ins>。</ins>壱舛入てよし<ins>。</ins>米壱<ins>耳</ins>の手まへにておよそ四合余<ins>針れら</ins>なれば大<ins>宗</ins>に益あり<ins>。</ins>○<ins>声車</ins>唐なす京に<ins>豊</ins>てかぼち<ins>ヤ南京瓜飯</ins>西国すじにてはぼうぶ<ins>か</ins>といふ南京瓜をいつもにしめにする時よりは細かにき<ins>か</ins>て米と一所に釜へ入<ins>。</ins>常の水かげん<ins>生ゝ</ins>塩を入い<ins>し</ins>れ<ins>や</ins>て<ins>う</ins>も<ins>ゆ</ins>よ<ins>を</ins>したきあげしばらく熟し杓子にてよくまぜ合<ins>か</ins>つして食すべし<ins>。</ins>随分よきも<ins>るも</ins>分量は見合に入てよし<ins>。</ins>米一舛の手まへにて三四合は徳分なり<ins>。</ins>

### GT
常に如此して米を喰のばすなり分量は米壱舛にきらず壱舛入てよし米壱舛の手まへにておよそ四合余の徳分なれば大に益あり○南京瓜飯江戸にて唐なす京にてかぼちや西国すじにてはぼうぶらといふ南京瓜をいつもにしめにする時よりは細かにきりて米と一所に釜へ入常の水かげんにて塩を入しやうゆをいれてもよしたきあげしばらく熟し杓子にてよくまぜ合しうつして食すべし随分よきもの也分量は見合に入てよし米一舛の手まへにて三四合は徳分なり

## 200006663_00006_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200006663_00006_2.jpg" width="512" title="details">
  </p>
  
### Input
夜番たゞ<ins>出</ins>のぶ<ins>ツれえりレけかまさゞ</ins>ゑびす廻国<ins>ま重お</ins>

### Pred
夜番た<ins>だ出</ins>のぶ<ins>つれえりけかまさざ</ins>ゑびす廻国<ins>ま重お</ins>

### GT
夜番たゞのぶゑびす廻国

## 200017458_00008_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200017458_00008_1.jpg" width="512" title="details">
  </p>
  
### Input
御へりなくてひゑいんのふをのといふろにとぢこもせ給ひけりろかづきすゑゆきげのそのあらにさしぐるくものまなくやにゆきかふ人もまれなりりいはんやをの御すまゐ思ひやられてあはれなりこにさいちうじやうありはのなりひらはむの御なさけあさかざり人なりけれ〱たるゆきをふみけなく〱御あをたづねまいて<ins>ん</ins>らすれはまうとつりきたりてうえうあにたりゐんけんしやく〱たりおりにませ人めもくさもかれぬればいびきにみなしろたえのにはのおもあみつくる人なみはぢくいでさせ給ひてんでんの御かう三げんばりあげての山を御らんめぐしげにやははあをくなつはしげりあきはそめふゆはおつといふせめい太のおぼめつねろほのゆきをばすだれをかげてみん

### Pred
御へりなくてひゑいんのふをのといふろにとぢこもせ給ひけりろかづきすゑゆきげのそのあらにさしぐるくものまなくやにゆきかふ人もまれなりりいはんやをの御すまゐ思ひやられてあはれなりこにさいちうじやうありはのなりひらはむの御なさけあさかざり人なりけれ〱たるゆきをふみけなく〱御あをたづねまいて<ins>ん</ins>らすれはまうとつりきたりてうえうあにたりゐんけんしやく〱たりおりにませ人めもくさもかれぬればいびきにみなしろたえのにはのおもあみつくる人なみはぢくいでさせ給ひてんでんの御かう三げんばりあげての山を御らんめぐしげにやははあをくなつはしげりあきはそめふゆはおつといふせめい太のおぼめつねろほのゆきをばすだれをかげてみん

### GT
御かへりなくしてひゑいざんのふもとをのといふところにとぢこもらせ給ひけりころはかみなづきすゑゆきげのそらのあらしにさえしぐるゝくものたえまなくみやこにゆきかふ人もまれなりけりいはんやをのゝ御すまゐ思ひやられてあはれなりこゝにさいごちうじやうありはらのなりひらはむかしの御なさけあさからざりし人なりければふん〱たるゆきをふみわけなく〱御あとをたづねまいりて見まいらすれはまうとううつりきたりてこうえうあらしにたえりうゐんけんがとうしやく〱たりおりにまかせ人めもくさもかれぬれば山ざといとゞさびしきにみなしろたえのにはのおもあとふみつくる人もなしみこははしぢかくいでさせ給ひてなんでんの御かうし三げんばかりあげてよもの山を御らんじめぐらしげにやはるはあをくなつはしげりあきはそめふゆはおつるといふせうめい太しのおぼしめしつらねかうろほうのゆきをばすだれをかゝげてみるらんと

## 200017458_00037_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200017458_00037_2.jpg" width="512" title="details">
  </p>
  
### Input
<ins>ば</ins>へんるろにや五郎ひなくつつきち<ins>ら</ins>たをいてはなしろにおすたりいきほひたたきぐちあへなくまけしばしばらすまふなりけるや五郎はげんしつたきぐちにかちて百<ins>干</ins>ばんのまけもものなずれにつそれけれなにものなりともと思ふ<ins>の</ins>につら山の又七いで手にもたますまけてのちくつきやうのすふ五ばんまでかちてたつたるありさまはきほひあまりてぞ見けるにさのくにのぢ人やきしたの小六郎出てあひはのや五をはめてよきすまふ六ばんつるのくにのぢう人たけのしたのまご八いで<ins>く</ins>小六郎をめてきすまふ九<ins>は</ins>んつていんろにがしやまたの五郎いで<ins>く</ins>まご八をめてよきすふばんかちければいでとんいふのなするがのくにたのち六いざやとんいふそにありけるゑびなのひ

### Pred
<ins>ば</ins>へんるろにや五郎ひなくつつきち<ins>ら</ins>たをいてはなしろにおすたりいきほひたたきぐちあへなくまけしばしばらすまふなりけるや五郎はげんしつたきぐちにかちて百<ins>干</ins>ばんのまけもものなずれにつそれけれなにものなりともと思ふ<ins>の</ins>につら山の又七いで手にもたますまけてのちくつきやうのすふ五ばんまでかちてたつたるありさまはきほひあまりてぞ見けるにさのくにのぢ人やきしたの小六郎出てあひはのや五をはめてよきすまふ六ばんつるのくにのぢう人たけのしたのまご八いで<ins>く</ins>小六郎をめてきすまふ九<ins>は</ins>んつていんろにがしやまたの五郎いで<ins>く</ins>まご八をめてよきすふばんかちければいでとんいふのなするがのくにたのち六いざやとんいふそにありけるゑびなのひ

### GT
はうさへんとするところにや五郎ひまなくつつといりたきぐちがこまたをかいてはなしろにおしすへたりいきほひたるたきぐちあへなくまけしかばしばらくすまふぞなかりけるや五郎はかうげんしつるたきぐちにかちて百千ばんのまけもものならずこれにかつこそうれしけれなにものなりともと思ふところにがつら山の又七いでゝ手にもたまらすまけてのちくつきやうのすまふ五ばんまでかちてたつたるありさまはいきほひあまりてぞ見えけるこゝにさがみのくにのぢう人やきしたの小六郎出てあひざはのや五郎をはじめとしてよきすまふ六ばんかつするがのくにのぢう人たけのしたのまご八いでゝ小六郎をはじめとしてよきすまふ九ばんかつていらんとするところに大ばがしやていまたのゝ五郎いでゝまご八をはじめとしてよきすまふ十ばんかちければいでゝとらんといふものなしするがのくにたかはしのちう六いざやとらんといふそばにありけるゑびなのひ

## 200020019_00077_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200020019_00077_1.jpg" width="512" title="details">
  </p>
  
### Input
かみ申也この御てらのさんがう寺ごうはかた<ins>じ</ins>しけなくもぜんたう大しのしんゑんごんゑんそうじやうゑんのこ<ins>くつ</ins>なるべし竹さいも江戸てねをまふけ<ins>形</ins>ば家をもち女をむかへみつのゑんをむすびしんだいをもをしなを人<ins>ら</ins>くもなりたゝむところのうちによろこひけりさてそ<ins>そ</ins>れよりも過行<ins>ん</ins>をとに聞えし日のもとのはしをみな人わたりかね世をもたずみかねたりし事のためしもおほかりしこゝはいづ<ins>ゝ</ins>そかんだのだいみなみにあたりてながむれは天下のぶしやうの御ざなさる御しろの<ins>方</ins>見<ins>ん</ins>事さ<ins>に太衛</ins>銀るりの玉ぎをはり<ins>き</ins>ねあけたるらうかくは雲につらな<ins>ひ</ins>有さまはもろ<ins>み</ins>し

### Pred
<ins>上</ins>申也<ins>此</ins>御寺<ins>の三号寺号</ins>は<ins>片時無</ins>くも<ins>全</ins>大<ins>僧正</ins>の<ins>真言円宗状延命</ins>の<ins>故実</ins>なるべし竹<ins>斎</ins>も江戸にて家を<ins>構え</ins>女を<ins>迎</ins>へ<ins>三</ins>の<ins>宴</ins>を<ins>結</ins>び<ins>死</ins>んだいをも<ins>惜</ins>しなを人<ins>楽</ins>もなり<ins>立っ</ins>たゝむ<ins>処</ins>の<ins>中</ins>に<ins>喜び</ins>けりさてそれよりも過行<ins>ん</ins>をとに聞えし日の<ins>本</ins>のはしを<ins>皆</ins>人<ins>渡</ins>りかね世をもたずみかねたりし事のためしもおほかりし<ins>此処</ins>はい<ins>つ</ins>そ<ins>神田</ins>の<ins>大名南</ins>にあたりて<ins>眺</ins>むれ<ins>ば</ins>天下の<ins>武士</ins>の御<ins>座</ins>なさ<ins>れ</ins>る御<ins>城</ins>の<ins>方</ins>見<ins>ん</ins>事さ<ins>に太衛</ins>銀るりの玉ぎをはり<ins>き</ins>ねあけたるらうかくは雲につらな<ins>ひ</ins>有さまはもろ<ins>み</ins>し

### GT
かみ申也この御てらのさんがう寺ごうはかたしけなくもぜんたう大しのしんゑんごんゑんそうじやうゑんのこゝろなるべし竹さいも江戸にてかねをまふけなば家をもち女をむかへみつのゑんをむすびしんだいをもをしなをし人〻しくもなりたゝむとこゝろのうちによろこひけりさてそれよりも過行はをとに聞えし日のもとのはしをみな人わたりかね世をもたゝずみかねたりし事のためしもおほかりしこゝはいづくそかんだのだいみなみにあたりてながむれは天下のぶしやうの御ざなさる御しろの見事さよ金銀るりの玉ぎをはりかさねあけたるらうかくは雲につらなる有さまはもろこし

## 200021763_00006_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200021763_00006_2.jpg" width="512" title="details">
  </p>
  
### Input
平皿<ins>飯鉢</ins>七ツ目<ins>蓋台</ins>中合サ汁再進<ins>煎物</ins>島台土器<ins>飯鉢押肴二種蓋台箸汁再進銚子島台土器提子</ins>押肴二種箸杯台<ins>銚子</ins>平銚子台<ins>提子</ins>

### Pred
平皿<ins>飯鉢</ins>七ツ目<ins>蓋台</ins>中合サ汁再進<ins>煎物</ins>島台土器<ins>飯鉢押肴二種蓋台箸汁再進銚子島台土器提子</ins>押肴二種箸杯台<ins>銚子</ins>平銚子台<ins>提子</ins>

### GT
平皿七ツ目中合サ煎物飯鉢蓋台汁再進島台土器押肴二種箸銚子提子飯鉢蓋台汁再進島台土器押肴二種箸銚子提子杯台平銚子台

## 200021763_00008_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200021763_00008_2.jpg" width="512" title="details">
  </p>
  
### Input
飯鉢<ins>飯鉢蓋台</ins>蓋台汁再進汁再進置杯<ins>置杯平銚子</ins>平銚子吸物<ins>吸物肴二種</ins>肴二種湯水<ins>湯水</ins>茶菓子<ins>茶菓子</ins>

### Pred
飯鉢<ins>飯鉢蓋台</ins>蓋台汁再進汁再進置杯<ins>置杯平銚子</ins>平銚子吸物<ins>吸物肴二種</ins>肴二種湯水<ins>湯水</ins>茶菓子<ins>茶菓子</ins>

### GT
飯鉢蓋台汁再進置杯平銚子吸物肴二種湯水茶菓子飯鉢蓋台汁再進置杯平銚子吸物肴二種湯水茶菓子

## 200021763_00009_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200021763_00009_1.jpg" width="512" title="details">
  </p>
  
### Input
濃茶濃茶後菓子<ins>後菓子薄茶</ins>薄茶以上七詰五詰に次たる尊<ins>る々</ins>の御方の<ins>饗</ins>応御料理なり二汁七菜二汁五菜本膳<ins>本膳膾直汁</ins>膾汁<ins>黍</ins>香物箸煎物<ins>香物箸</ins>坪皿飯<ins>坪以皿飯</ins>

### Pred
濃茶濃茶後菓子<ins>後菓子薄茶</ins>薄茶以上七詰五詰に次たる尊<ins>る々</ins>の御方の<ins>饗</ins>応御料理なり二汁七菜二汁五菜本膳<ins>本膳膾直汁</ins>膾汁<ins>黍</ins>香物箸煎物<ins>香物箸</ins>坪皿飯<ins>坪以皿飯</ins>

### GT
濃茶後菓子薄茶濃茶後菓子薄茶以上七詰五詰に次たる尊貴の御方の餐応御料理なり二汁七菜本膳膾汁小皿香物箸煎物坪皿飯二汁五菜本膳膾汁香物箸煎物坪皿飯

## 200021763_00020_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200021763_00020_1.jpg" width="512" title="details">
  </p>
  
### Input
引向おま<ins>半</ins>鯛二玉子ふわ〱<ins>長皿ふた物</ins>薄鳥<ins>平皿御所麩</ins>猪口薄<ins>モ</ins>雪<ins>主花かつ尾</ins>ふ<ins>くる之</ins>焼物一しほかれゐ懸下け<ins>肴一鳥鴨</ins>銚子<ins>すれんこん</ins>吸物花<ins>以</ins>か<ins>ぜらかし</ins>こせ<ins>銚子</ins>肴<ins>湯</ins>鯖粧漬湯<ins>石</ins>する<ins>州する</ins>

### Pred
引向おま<ins>半</ins>鯛二玉子ふわ〱<ins>長皿ふた物</ins>薄鳥<ins>平皿御所麩</ins>猪口薄<ins>モ</ins>雪<ins>主花かつ尾</ins>ふ<ins>くる之</ins>焼物一しほかれゐ懸下け<ins>肴一鳥鴨</ins>銚子<ins>すれんこん</ins>吸物花<ins>以</ins>か<ins>ぜらかし</ins>こせ<ins>銚子</ins>肴<ins>湯</ins>鯖粧漬湯<ins>石</ins>する<ins>州する</ins>

### GT
引向長皿おまつ鯛平皿御所麩花かつおくるミ肴一鳥鴨一すれんこんせうか銚子湯する二ふた物玉子ふわ〱薄鳥猪口薄雪もミふし焼物一しほかれゐ懸下け銚子吸物花いかこせう肴一鯖粧漬湯する

## 200021763_00025_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200021763_00025_1.jpg" width="512" title="details">
  </p>
  
### Input
七詰五詰の組合<ins>花</ins>積立<ins>ミ</ins>略図本膳鯛作り身<ins>も錦鱠</ins>細作り魚<ins>汁小かふ</ins>く大根<ins>しい茸</ins>せか<ins>皮牛房</ins>房風<ins>青な</ins>杉小<ins>金</ins>角<ins>此かん</ins>なら漬瓜<ins>香物</ins>ミそ漬大根<ins>之</ins>もり口漬花塩山升杉曲物焼魚<ins>煮物</ins>花ゑひ<ins>飯</ins>くしこ敷葛

### Pred
七詰五詰の組合<ins>花</ins>積立<ins>ミ</ins>略図本膳鯛作り身<ins>も錦鱠</ins>細作り魚<ins>汁小かふ</ins>く大根<ins>しい茸</ins>せか<ins>皮牛房</ins>房風<ins>青な</ins>杉小<ins>金</ins>角<ins>此かん</ins>なら漬瓜<ins>香物</ins>ミそ漬大根<ins>之</ins>もり口漬花塩山升杉曲物焼魚<ins>煮物</ins>花ゑひ<ins>飯</ins>くしこ敷葛

### GT
七詰五詰の組合并積立之略図本膳膾煮物香物汁飯膾鯛作り身細作り魚くり大根せうか房風金かん杉小角香物なら漬瓜ミそ漬大根もり口漬花塩山升杉曲物煮物焼魚花ゑひくしこ敷葛汁鶴小かふしい茸皮牛房青な飯

## 200021869_00003_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200021869_00003_1.jpg" width="512" title="details">
  </p>
  
### Input
<ins>ゝ</ins>右一<ins>は</ins>

### Pred
右一<ins>は</ins>

### GT
右一水

## 200021869_00007_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200021869_00007_1.jpg" width="512" title="details">
  </p>
  
### Input
玉子そふめん拵方<ins>リ</ins>事玉子久助半<ins>く</ins>に入砂唐<ins>へん</ins>合に入べし<ins>しし</ins>よく<ins>我き</ins>きて玉子焼に入鍋に<ins>湯</ins>をにへ<ins>ねつ</ins>し其中へ曲らぬ様に入<ins>七ふ</ins>はら<ins>て</ins>置湯の中へとつふりいれしはら<ins>〱</ins>く<ins>人</ins>置上<ins>て</ins>て水にはなし何れなり共用べ<ins>しししし</ins>し水仙拵方之事久助をとき色付なりす<ins>具りの</ins>なり共是を玉子焼にて前<ins>にて</ins>用べし<ins>しししし</ins>

### Pred
玉子そふめん拵方<ins>リ</ins>事玉子久助半<ins>く</ins>に入砂唐<ins>へん</ins>合に入べし<ins>しし</ins>よく<ins>我き</ins>きて玉子焼に入鍋に<ins>湯</ins>をにへ<ins>ねつ</ins>し其中へ曲らぬ様に入<ins>七ふ</ins>はら<ins>て</ins>置湯の中へとつふりいれしはら<ins>〱</ins>く<ins>人</ins>置上<ins>て</ins>て水にはなし何れなり共用べ<ins>しししし</ins>し水仙拵方之事久助をとき色付なりす<ins>具りの</ins>なり共是を玉子焼にて前<ins>にて</ins>用べし<ins>しししし</ins>

### GT
玉子そふめん拵方之事玉子久助半々に入砂唐見合に入べしよくときて玉子焼に入鍋に揚をにへ返し其中へ曲らぬ様に入しはらく置湯の中へとつふりいれしはらく置上て水にはなし何れなり共用べし水仙拵方之事久助をとき色付なりすくになり共是を玉子焼にて前如く用べし

## 200021869_00012_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200021869_00012_1.jpg" width="512" title="details">
  </p>
  
### Input
かまほこ拵方<ins>し</ins>事玉子そふめんの如にそれを<ins>ほ</ins>竹の<ins>れ同比ほ</ins>二ツ割し両方<ins>て更</ins>ふ<ins>し</ins>しを付其中へ入さ<ins>しそ</ins>をうす<ins>て</ins>そきもよふなる<ins>に</ins>ふに入へしそれをふ<ins>ゝ</ins>かし外へ玉子を<ins>ぬ</ins>るへ<ins>へ</ins>し<ins>青意ケわしぞ</ins>

### Pred
かまほこ拵方<ins>し</ins>事玉子そふめんの如にそれを<ins>ほ</ins>竹の<ins>れ同比ほ</ins>二ツ割し両方<ins>て更</ins>ふ<ins>し</ins>しを付其中へ入さ<ins>しそ</ins>をうす<ins>て</ins>そきもよふなる<ins>に</ins>ふに入へしそれをふ<ins>ゝ</ins>かし外へ玉子を<ins>ぬ</ins>るへ<ins>へ</ins>し<ins>青意ケわしぞ</ins>

### GT
かまほこ拵方之事玉子そふめんの如にそれを竹の筒を二ツ割し両方へふしを付其中へ入さかなをうすくそきもよふなるよふに入へしそれをふかし外へ玉子をふるへし

## 200022050_00002_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200022050_00002_2.jpg" width="512" title="details">
  </p>
  
### Input
▲祝言引渡之次第一<ins>歌</ins>栗ほそきかたをむ<ins>に也んレ一三ツかわらけ</ins>成やうに三かくにお<ins>ゝ</ins>也<ins>也</ins>一のし二本<ins>寸すま</ins>ひろきかたをきやくのひだりの<ins>ぶ</ins>かたへしておきて<ins>こか</ins>し昆布切かぶなて<ins>りたに</ins>也一てうしひさ<ins>けきりお</ins>一まきずるめ<ins>のさ</ins>か<ins>なかレ事</ins>すミ一か<ins>かす</ins>こしもちくしこむすびこんぶ<ins>一むめぼし三ツざうに</ins>いもひ<ins>ら</ins>かつうほくしあ<ins>げひ</ins>一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとす<ins>ま</ins>也一ねぶか二本しろに<ins>ね</ins>一か<ins>かん</ins>んざけ<ins>とも</ins>

### Pred
祝言引渡之次第一<ins>歌</ins>栗<ins>細</ins>き<ins>方</ins>を<ins>もに也んレ一三ツかわらけ</ins>成やうに三かくにお<ins>ゝ</ins>也<ins>也</ins>一のし二本<ins>寸すま</ins>ひろきかたをきやくのひだりの<ins>ぶ</ins>かたへしておきて<ins>こか</ins>し昆布切かぶなて<ins>りたに</ins>也一てうしひさ<ins>けきりお</ins>一まきずるめ<ins>のさ</ins>か<ins>なかレ事</ins>すミ一か<ins>かす</ins>こしもちくしこむすびこんぶ<ins>一むめぼし三ツざうに</ins>いもひ<ins>ら</ins>かつうほくしあ<ins>げひ</ins>一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとす<ins>ま</ins>也一ねぶか二本しろに<ins>ね</ins>一か<ins>かん</ins>んざけ<ins>とも</ins>

### GT
▲祝言引渡之次第一栗ほそきかたをむふへ成やうに三かくにおく也一三ツかわらけ一のし二本ひろきかたをきやくのひだりのかたへしておきてよし一昆布二切かぶなりにきりておく也一てうしひさげ一さかな一まきずるめ一からすミ一かずのこ一むめぼし三ツざうにもちくしこむすびこんぶいもひゝかつうほくしあわび一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとする也一ねぶか二本しろねともに一かんざけ

## 200022050_00006_1
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200022050_00006_1.jpg" width="512" title="details">
  </p>
  
### Input
をなどふたどきてい候是すてひの入吉立ハふたのくあん汁ハかハをはぎおろきて<ins>は</ins>おもミをも<ins>人</ins>入した時あげて水にてひや酒をかけをく汁時入ぶをしほげんすい合出又すまの<ins>斗</ins>にけ少候此時ハおきくしだい入せ中そにだをくに候どぶをさて吉<ins>に</ins>大ん外<ins>入</ins>但久くたきてハのあぢ悪候あきそをたきの也いつれもそをかうて久敷に候しるにハ此ちすい口さんせのこ同葉<ins>鶉</ins>の汁だにほねを入せんそにて仕立さん大也つまハその時のけい<ins>ふ</ins>つ吉きの<ins>は</ins>いほ数入吉何時もすぢをおびゆ又<ins>し</ins>めゟ中そにてしたてゟすに汁中て仕立候又につま時の物也り次入いんにてもかにてをいだを入ねを生たれ少てを入しほ<ins>け</ins>んすい合出是もつまハ時の物惣のこハ鳥汁にい入吉いびゆ吉あをちのたを

### Pred
をなどふたどきてい候是すてひの入吉立ハふたのくあん汁ハかハをはぎおろきて<ins>は</ins>おもミをも<ins>人</ins>入した時あげて水にてひや酒をかけをく汁時入ぶをしほげんすい合出又すまの<ins>斗</ins>にけ少候此時ハおきくしだい入せ中そにだをくに候どぶをさて吉<ins>に</ins>大ん外<ins>入</ins>但久くたきてハのあぢ悪候あきそをたきの也いつれもそをかうて久敷に候しるにハ此ちすい口さんせのこ同葉<ins>鶉</ins>の汁だにほねを入せんそにて仕立さん大也つまハその時のけい<ins>ふ</ins>つ吉きの<ins>は</ins>いほ数入吉何時もすぢをおびゆ又<ins>し</ins>めゟ中そにてしたてゟすに汁中て仕立候又につま時の物也り次入いんにてもかにてをいだを入ねを生たれ少てを入しほ<ins>け</ins>んすい合出是もつまハ時の物惣のこハ鳥汁にい入吉いびゆ吉あをちのたを

### GT
うをなどもふくたうもどきとていたし候是もかわをはぎすてひぶくのかわ入吉立やうハふくたうのくあんかう汁ハかハをはぎおろしきりてかハおもミをもにゑゆへ入しらミたる時あげて水にてひやし其後酒をかけをくミそ汁にへ立候時うをゝ入どぶをさししほかげんすい合出し候也又すましの時ハだし計にかけも少おとし候此時ハうハおきさくしだいに入どせう汁中ミそにだしをくハへよくに申候どぶをさして吉つまハごぼう大こん其外色々但久しくたき候てハミそのあぢ悪候左候へハあたらしきミそをたてさしニて出しよきもの也いつれもミそをかうして久敷に申候しるにハ此こゝろもち入る也すい口さんせうのこ同葉鶴の汁ハだしにほねを入せんじさしミそにて仕立候さしかげん大事也つまハその時のけいぶつ吉きのこハいかほど数入候ても吉何時もすぢをおくすい口わさびゆ又はじめゟ中ミそにてもしたてゟすましにも白鳥汁中ミそにて仕立候又すましにもつまハ時分の物也つくり次第入かハいりハがんにてもかもにてもかハをいりだしを入ほねをせんじ生たれ少さして身を入しほかげんすい合出し候是もつまハ時の物惣別木のこハ鳥汁にいつも入候て吉すい口わさびゆ吉あをかちハきじのわたを

## 200022050_00007_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200022050_00007_2.jpg" width="512" title="details">
  </p>
  
### Input
ほをつけうち<ins>書</ins>べてや也しぎやきなすびゆでよき比ににさんせミそをけてや也やき竹の子竹の子のふをぬきへまぼこたまごまろにて入かハにやて切まぼこのほか<ins>ぬ</ins>にして吉りきを大きにつくりりかけをきてかハをい身をはさ入なべてまいならびにやりしるなくハけをきたるたいべきなり第四すい物の部の花いのせのたをすぢい十文まに切け又大さよき<ins>比</ins>に切はゆにをしてつまにのりなにけをおふせすい合いたみのにたまごをあげしにけくをにゆ入候是もつま色汁同前のよき比に切すミそにだを入ふき時わたを入すい合出候也まだこしゆにてさ〱いりさかけのなき時白水をだたまくハふせてすい口ゆを切其入第五酒の部玉子酒玉子をあけひやざけを入てしほを少入んをて

### Pred
ほをつけうち<ins>書き</ins>てや也しぎやきなすびゆでよき比ににさんせ<ins>味噌</ins>をけてや也やき竹の子竹の子のふをぬきへまぼこたまごまろにて入かハにやて切まぼこのほか<ins>ぬ</ins>にして吉りきを大きにつくりりかけをきてかハをい身をはさ入なべてまいならびにやりしるなくハけをきたるたいべきなり第四すい物の部の花いのせのたをすぢい十文まに切け又大さよき<ins>比</ins>に切はゆにをしてつまにのりなにけをおふせすい合いたみのにたまごをあげしにけくをにゆ入候是もつま色汁同前のよき比に切すミそにだを入ふき時わたを入すい合出候也まだこしゆにてさ〱いりさかけのなき時白水をだたまくハふせてすい口ゆを切其入第五酒の部玉子酒玉子をあけひやざけを入てしほを少入んをて

### GT
ほをつけうちくべてやく也しぎやきなすびをゆでよき比に切くしにさしさんせうミそをつけてやく也やき竹の子竹の子のふしをぬき中へかまぼこたまごまろにして入かハともにやきて切かまぼこのしほからめにして吉いりやきかもを大きにつくりたまりかけをきてかハをいり身をはさミ入なべにて一まいならびにやく也あまりしるなくハかけをきたるたまりすこしいるべきなり第四すい物の部うの花いかのせのかたをすぢかい十文字にこまかに切かけ又大さよき此に切はなしゆにをしてつまにのりなど入だしにかけをおとしふかせすい合いたし候也みのにたまごをあげしやくしにてうけくだけしをにへゆへ入候是もつま色々汁同前このわたよき比に切うすミそにだしを入ふき立候時わたを入すい合其まゝ出し候也まつだけこしゆにてさハ〱といりさかけのなき時白水をさしだしたまりくハへふかせ候てすい口ゆを切其まゝ入てよし第五りやうり酒の部玉子酒玉子をあけひやざけを少ツヽ入よくときてしほを少入かんをして

## 200022050_00010_2
  <p align="left">
    <img src="/zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/imgs/200022050_00010_2.jpg" width="512" title="details">
  </p>
  
### Input
も有そべまのげんハなをなてあにすのおほくあまり候ハぬか候のしろ鱠ふな<ins>〱</ins>ま<ins>ふ</ins>きふななすを入すにあひり鱠あめのを三まおろ身ハすきてつ両のを打合かハめやききざ入たのいのくきをさがき入すしほげんてあへ候い也ハもしきばきあゆにてもあめのをの<ins>シ</ins>く仕候れも身すきてつり候しやきぬなしをよてさけのくすりあ<ins>にて</ins>にても<ins>出</ins>にまづすにていそのすをすてのちにぬたをすにてのべすんてあへ後のすおほきハ悪候たしあゆにて<ins>は</ins>あをまのぬたにゆのはミ入あ鱠ほのいあいりいりざけすたにてあへ候たあのちに入<ins>さ</ins>けも吉花つほ三月大木くげなどきざ吉<ins>酔</ins>いのうすほねやきむ取て田つりいて川ゑひ木くりしお入てすしほげんしてあ候わびがんかも同けなどつすにて

### Pred
も有そべまのげんハなをなてあにすのおほくあまり候ハぬか候のしろ鱠ふな<ins>〱</ins>ま<ins>ふ</ins>きふななすを入すにあひり鱠あめのを三まおろ身ハすきてつ両のを打合かハめやききざ入たのいのくきをさがき入すしほげんてあへ候い也ハもしきばきあゆにてもあめのをの<ins>シ</ins>く仕候れも身すきてつり候しやきぬなしをよてさけのくすりあ<ins>にて</ins>にても<ins>出</ins>にまづすにていそのすをすてのちにぬたをすにてのべすんてあへ後のすおほきハ悪候たしあゆにて<ins>は</ins>あをまのぬたにゆのはミ入あ鱠ほのいあいりいりざけすたにてあへ候たあのちに入<ins>さ</ins>けも吉花つほ三月大木くげなどきざ吉<ins>酔</ins>いのうすほねやきむ取て田つりいて川ゑひ木くりしお入てすしほげんしてあ候わびがんかも同けなどつすにて

### GT
も有そうべつなますのかげんハなますをミなもりてあとにすのおほくあまり候ハぬかよく候このしろ鱠ふなのくやまぶきあへハふななますをからし入すにあへ申事也ひてり鱠あめのうを三まいにおろし身ハすきてつくり両のかハを打合かハめよりやきてきざミ入たうのいものくきをさゝがき入すしほかげんしてあへ候をいふ也かハもしらやき也かばやき鱠あゆにてもあめのうをのく仕候事也これも身ハすきてつくり候かハしらやきぬたなますからしをよくすりてさけのかすをよくすりあゆにてもいわしにてもなよしにてもまづすにていためそのすをすてのちにぬたをすにてのべすかげんしてあへ候也後のすおほきハ悪候たゞしあゆにてハあをまめのぬたにゆのはきざミ入あへ申事も有太郎助鱠一しほのたいあわひなどいかにもうすくつくりいりざけすたうぶんにしてあへ候たゞしあわひハのちに入吉ますざけも吉花がつほ三月大こん木くらげなどきざミ入て吉やきほね鱠たいのうすミほねなとやきむしり取て田つくりいりて川ゑひ木くらげくりしやうがおろしなと入てすしほかげんしてあへ申候わさびあへがんかも同もゝけなどつくりすにて

## Error Type Summary

The categories below are based on a three-way comparison among `Input`, `Pred`, and `GT`. In short, `Input` is the noisy OCR source, `Pred` is the model's attempted correction, and `GT` is the target transcription.

### 1. Repetition / Runaway Generation

The clearest example is `100249376_00010_2`. The prediction follows the beginning of the text reasonably well, but then repeatedly generates content around `水にひやしうすくのはしはり...`. As a result, `Pred_Length` grows to 1223 while `GT_Length` is only 114, and CER rises to 9.76. This is not a normal single-character OCR error; it is a generation failure where the model falls into a repetition loop.

### 2. List and Reading-Order Errors

This pattern is especially visible in `200021763_00006_2`, `200021763_00008_2`, `200021763_00009_1`, `200021763_00020_1`, and `200021763_00025_1`. These samples mostly contain lists of dishes, vessels, or menu items. The model often preserves many local terms, but the overall order, grouping, and repetition structure are wrong. For example, in `200021763_00008_2`, `Input` and `Pred` look like adjacent items have been repeated locally, while `GT` contains two complete ordered sequences. This suggests that the model is still weak at recovering the correct reading order from layout-sensitive text.

### 3. Over-Copying the Input

In many cases, `Pred` is almost identical to `Input` even though both differ substantially from `GT`. Typical examples include `100249416_00034_1`, `200017458_00008_1`, `200017458_00037_2`, `200021869_00007_1`, `200021869_00012_1`, `200022050_00006_1`, and `200022050_00010_2`. This indicates that when the input is long or noisy, the model tends to copy the OCR text conservatively instead of actively correcting it from context. The output length may look reasonable, but the CER remains high.

### 4. Degradation on Long Texts

`200017458_00008_1`, `200017458_00037_2`, `200020019_00077_1`, `200022050_00002_2`, `200022050_00006_1`, `200022050_00007_2`, and `200022050_00010_2` are relatively long samples. In these cases, the first part of the prediction is usually more stable, while later sections are more likely to contain missed corrections, wrong substitutions, semantic drift, or direct copying from `Input`. Some outputs also stop around 300 characters, which looks like truncation-like behavior.

### 5. Classical Kana and Premodern Japanese Character Confusions

Short and medium-length samples also contain many fine-grained character errors, such as `100249376_00041_2`, `200006663_00006_2`, and `200021869_00003_1`. Common issues include mistakes around repetition marks such as `ゝ`, voicing-mark differences, confusion among functional characters such as `候`, `申`, and `入`, and substitutions among visually similar kana or kanji such as `粉`, `こ`, `し`, and `す`. Each individual error may be small, but in short texts these errors can raise CER sharply.

### 6. Modernization or Normalization

Some predictions shift the text toward modern Japanese, modern punctuation, or more common kanji. For example, `100249476_00004_1` adds Japanese periods, while `200020019_00077_1` includes modernized or semantic substitutions such as `上申也`, `三号寺号`, and `天下の武士`. These outputs may be easier to read, but the target is a faithful transcription matching `GT`, so these plausible-looking rewrites still increase edit distance.

### 7. Domain Vocabulary Errors

Vocabulary related to cooking, confectionery, menus, vessels, ingredients, procedures, and measurement units is a frequent source of errors. Relevant samples include `100249416_00027_1`, `100249416_00034_1`, `100249476_00004_1`, `200022050_00002_2`, `200022050_00006_1`, `200022050_00007_2`, and `200022050_00010_2`. Classical culinary texts contain many specialized terms, and OCR noise often creates visually similar or linguistically plausible alternatives. As a result, the model may misread, omit, or normalize domain-specific words.

### Overall

Overall, the main failure modes of Gemma-2-Llama-Swallow-9b-it-v0.1 can be summarized in three points. First, some samples show severe repetition failures. Second, for list-like, long, or layout-sensitive texts, the model often copies `Input` or disrupts the correct reading order. Third, fine-grained details such as classical kana, culinary terminology, vessel names, and measurement units are still not corrected reliably. Future improvements should focus on repetition suppression, layout-aware reading-order modeling, and stronger domain adaptation for classical cooking and confectionery texts.
