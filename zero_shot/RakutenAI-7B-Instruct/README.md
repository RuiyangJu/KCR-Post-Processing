# RakutenAI-7B-Instruct
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
100249376_00022_2.txt,123,106,91,0.7398373983739838
100249376_00050_1.txt,126,74,74,0.5873015873015873
100249416_00034_1.txt,121,107,87,0.71900826446281
100249476_00007_2.txt,157,113,119,0.7579617834394905
200006663_00006_2.txt,11,25,15,1.3636363636363635
200015843_00110_1.txt,300,300,81,0.27
200021086_00005_1.txt,267,340,251,0.9400749063670412
200021763_00002_2.txt,17,11,7,0.4117647058823529
200021763_00006_2.txt,56,56,33,0.5892857142857143
200021763_00008_2.txt,44,44,37,0.8409090909090909
200021763_00009_1.txt,71,65,36,0.5070422535211268
200021763_00020_1.txt,86,85,71,0.8255813953488372
200021763_00025_1.txt,94,86,54,0.574468085106383
200021763_00042_1.txt,149,163,104,0.697986577181208
200021869_00003_1.txt,3,3,1,0.3333333333333333
200021869_00012_1.txt,74,64,36,0.4864864864864865
200022050_00002_2.txt,188,197,79,0.42021276595744683
200022050_00006_1.txt,496,298,211,0.4254032258064516
200022050_00010_2.txt,468,299,178,0.3803418803418803
```

## 100249376_00022_2
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/100249376_00022_2.jpg" width="512" title="details">
  </p>
  
### Input
のくろみにはあん壱升にくすの粉弐合いれあつさ四分程にのそへこきにてむ二時程さまし形は色<ins>ら</ins>に切申候<ins>ン</ins>十いもまき上白の米を一粒つ<ins>た見</ins>り粉にして絹ふるひにかけ粉一升に氷さたうの粉弐合いれ湯にてこねひ<ins>くく</ins>はゝ四寸に長さ壱尺程にのし山のいもを丸ほそく壱

### Pred
<ins>黒味</ins>には<ins>、1</ins>升<ins>の餅粉</ins>に<ins>2合分の</ins>くす粉<ins>、4</ins>分の<ins>1</ins>程<ins>の藁を混ぜ、2時間ほど寝かせてから、</ins>色<ins>々な形</ins>に切<ins>り、</ins>上白米を<ins>1</ins>粒<ins>ず</ins>つ<ins>見るように</ins>粉にし<ins>、</ins>絹<ins>で擦って</ins>粉<ins>1</ins>升に氷<ins>砂糖</ins>の粉<ins>2</ins>合<ins>、</ins>湯<ins>で混ぜ</ins>て<ins>、4</ins>寸に長さ<ins>1</ins>尺程の<ins>芋</ins>を丸く<ins>細く1</ins>

### GT
のくろみにはあん壱升にくすの粉弐合いれあつさ四分程にのしそへこしきにてむし二時程さまし形は色〻に切申候三十いもまき上白の米を一粒つゝえり粉にして絹ふるひにかけ粉一升に氷さたうの粉弐合いれ湯にてこねひてはゝ四寸に長さ壱尺程にのし山のいもを丸ほそく壱
## 100249376_00050_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/100249376_00050_1.jpg" width="512" title="details">
  </p>
  
### Input
<ins>左</ins>七かや餅の方いりや壱升能<ins>ミ</ins>た<ins>記</ins>有馬とをにてかすの残らさる様にふるひもち米の粉五合白沙<ins>う</ins>糖五合右のかやの粉と一つに合せいろうにうすくひろけむし申候能むせ候は<ins>た</ins>あけうすにてつき切はんの上に餅の粉をふりめんほうにてあつさ五分斗にをしのはし少さまし切申候

### Pred
<ins>左</ins>七かや餅の方いりや壱升の<ins>米を炊き、</ins>残らさる様にふるひ<ins>、</ins>もち米の粉五合<ins>、</ins>白<ins>砂</ins>糖五合<ins>、</ins>右のかやの粉と一つに合せ<ins>、搗</ins>き切<ins>った</ins>上に餅の粉をふり<ins>、餅</ins>を<ins>搗く。</ins>

### GT
九十七かや餅の方いりかや壱升能はたき有馬とをしにてかすの残らさる様にふるひもち米の粉五合白沙糖五合右のかやの粉と一つに合せいろうにうすくひろけむし申候能むせ候はゝあけうすにてつき切はんの上に餅の粉をふりめんほうにてあつさ五分斗にをしのはし少さまし切申候
## 100249416_00034_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/100249416_00034_1.jpg" width="512" title="details">
  </p>
  
### Input
糀を少入れおけば風味よき甘酒と<ins>ゐ</ins>なる也○上飴<ins>鍋心</ins>一<ins>歯</ins>餅米一升一糀<ins>た</ins>升七合一水七合<ins>此</ins>此水にて糀をあらひは<ins>あふの</ins>ばり取かすを去<ins>は段</ins>米<ins>ど</ins>あま酒につくりなれたる時布にてしよく<ins>練</ins>り是へしるあめ少しかすをよくすりて入れ三<ins>け</ins>日置なり但し折<ins>〱王こ</ins>廻てよし<ins>餅菓子手制衣集終候</ins>

### Pred
糀を少<ins>量</ins>入れ<ins>れ</ins>ば風味<ins>の</ins>よ<ins>い</ins>甘酒<ins>に</ins>な<ins>ります。鍋に</ins>飴<ins>を入れ、</ins>米一升<ins>、</ins>糀七合<ins>、</ins>水七合<ins>を入れ、</ins>糀をあら<ins>っ</ins>て<ins>、あふのばりを取って、米を</ins>よく<ins>練</ins>り<ins>、これを飴</ins>少<ins>量、</ins>かすをよくすり<ins>、</ins>三日置<ins>いて、</ins>折<ins>〱王こ</ins>廻てよし<ins>餅菓子手制衣集終候</ins>

### GT
糀を少し入れおけば風味よき甘酒ともなる也○上飴練やう一上白餅米一升一糀一升七合一水七合此水にて糀をあらひはなばかり取かすを去右餅米とあま酒につくりなれたる時布にてこしよくねり是へしるあめ少しかすをよくすりて入れ三日置なり但し折々かき廻してよし
## 100249476_00007_2
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/100249476_00007_2.jpg" width="512" title="details">
  </p>
  
### Input
<ins>し</ins>○大根飯大根飯は常たく<ins>組た</ins>中又は麦飯の中にても大根を鱠のごくきざ<ins>きを</ins>の吹あがる時蓋をとり飯の上へ入塩をも程よくいれ蓋をて焚あげ扨暫く熟しおきうつす時かきま<ins>ぶ</ins>食してよし○常年食するには大根飯に<ins>専</ins>油の出し汁かけて食すれども米價高き時は米のすくな<ins>した</ins>い<ins>る</ins>やうする<ins>と汁</ins>なれば大根を多<ins>し</ins>入塩も喰かげんに入かけ汁なしに食すべし

### Pred
大根飯は大根を<ins>刻んで</ins>ご飯の上<ins>にのせて、</ins>塩を<ins>少し入</ins>れ<ins>て</ins>蓋をして<ins>炊き、しばら</ins>く熟<ins>成させ</ins>て<ins>から食べる。</ins>常食する<ins>場合</ins>は<ins>、</ins>大根飯に油<ins>だし</ins>の<ins>だ</ins>し汁<ins>を</ins>かける<ins>が、米が高価</ins>な<ins>ときは、</ins>大根を多く入<ins>れて、</ins>塩<ins>を少なめ</ins>に入<ins>れて炊き、だし</ins>汁なし<ins>で</ins>食べ<ins>る。</ins>

### GT
○大根飯大根飯は常たく飯の中又は麦飯の中にても大根を鱠のごとくきざみ飯の吹あがる時蓋をとり飯の上へ入塩をも程よくいれ蓋をして焚あげ扨暫く熟しおきうつす時かきまぜ食してよし○常年食するには大根飯に醤油の出し汁かけて食すれども米價高き時は米のすくなくいかやうする事なれば大根を多く入塩も喰かげんに入かけ汁なしに食すべし
## 200006663_00006_2
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200006663_00006_2.jpg" width="512" title="details">
  </p>
  
### Input
夜番たゞ<ins>出</ins>のぶ<ins>ツれえりレけかまさゞ</ins>ゑびす廻国<ins>ま重お</ins>

### Pred
夜番たゞ<ins>出で</ins>ぶ<ins>ツれえりレけかまさゞ</ins>ゑびす廻国<ins>ま重お</ins>

### GT
夜番たゞのぶゑびす廻国
## 200015843_00110_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200015843_00110_1.jpg" width="512" title="details">
  </p>
  
### Input
着物は<ins>もも</ins>より<ins>内多ろ</ins>葉も<ins>敷き</ins>もしらず<ins>てし也がししがは置吉</ins>とい<ins>つ</ins>る家は蔵<ins>ん長</ins>九つ持て<ins>其もぐに代すへ正</ins>のか<ins>さ</ins>りぞか万屋はひそかなる手<ins>ざて</ins>独り<ins>に</ins>に吉太郎とて有しが十三<ins>具</ins>の時鼻<ins>頭小</ins>小杉<ins>人</ins>しを見て<ins>初楽も衛間</ins>の網干に姨有し<ins>かは記</ins>に遣は<ins>か</ins>置那<ins>及</ins>屋<ins>ゑ</ins>と云分限を見ならへと我子は捨て其<ins>る味</ins>が<ins>は</ins>子を<ins>元</ins>立二十五六迄も手代並にはたかせけるに其始末<ins>は</ins>たれ<ins>か参</ins>履迄も拾ひ集め瓜種の用に里へ<ins>迄也</ins>を見て気に<ins>金</ins>是<ins>呼</ins>子分にして家を渡し相<ins>気</ins>の娵を尋<ins>年</ins>けるに世<ins>る</ins>と替り成程悋気つよき女房ならば<ins>元</ins>娵にとり<ins>さ随</ins>と<ins>しれ</ins>ひ<ins>ぜ</ins>は広し思ふま<ins>く</ins>ゝなる娘有<ins>か嫁き</ins>をすまし夫婦は隠<ins>器</ins>をかまへ残らず<ins>後</ins>され<ins>け</ins>けるに此<ins>仁</ins>取金銀有に<ins>ろ</ins>て<ins>分</ins>取出手掛者を聞立旅子<ins>住</ins>ひを心

### Pred
着物は<ins>もも</ins>より<ins>内多ろ</ins>葉も<ins>敷き</ins>もしらず<ins>てし也がししがは置吉</ins>とい<ins>つ</ins>る家は蔵<ins>ん長</ins>九つ持て<ins>其もぐに代すへ正</ins>のか<ins>さ</ins>りぞか万屋はひそかなる手<ins>ざて</ins>独り<ins>に</ins>に吉太郎とて有しが十三<ins>具</ins>の時鼻<ins>頭小</ins>小杉<ins>人</ins>しを見て<ins>初楽も衛間</ins>の網干に姨有し<ins>かは記</ins>に遣は<ins>か</ins>置那<ins>及</ins>屋<ins>ゑ</ins>と云分限を見ならへと我子は捨て其<ins>る味</ins>が<ins>は</ins>子を<ins>元</ins>立二十五六迄も手代並にはたかせけるに其始末<ins>は</ins>たれ<ins>か参</ins>履迄も拾ひ集め瓜種の用に里へ<ins>迄也</ins>を見て気に<ins>金</ins>是<ins>呼</ins>子分にして家を渡し相<ins>気</ins>の娵を尋<ins>年</ins>けるに世<ins>る</ins>と替り成程悋気つよき女房ならば<ins>元</ins>娵にとり<ins>さ随</ins>と<ins>しれ</ins>ひ<ins>ぜ</ins>は広し思ふま<ins>く</ins>ゝなる娘有<ins>か嫁き</ins>をすまし夫婦は隠<ins>器</ins>をかまへ残らず<ins>後</ins>され<ins>け</ins>けるに此<ins>仁</ins>取金銀有に<ins>ろ</ins>て<ins>分</ins>取出手掛者を聞立旅子<ins>住</ins>ひを心

### GT
着物は花色より外は紅葉も藤色もしらず幾春をか送りぬ蔵合といへる家は蔵の数九つ持て富貴なれば是又国のかざりぞかし万屋はひそかなる手前者独り子に吉太郎とて有しが十三才の時鼻紙に小杉入しを見て勘当切幡州の網干に姨有しが此許に遣はし置那波屋殿と云分限を見ならへと我子は捨て其後妹が一子を見立二十五六迄も手代並にはたらかせけるに其始末すたれる草履迄も拾ひ集め瓜種の用に里へ送るを見て気に入是を子分にして家を渡し相応の娵を尋ねけるに世間と替り成程悋気つよき女房ならば我娵にとりたきとの願ひ世は広し思ふまゝなる娘有て縁組をすまし夫婦は隠居をかまへ残らず渡されけるに此跡取金銀有に任て少し取出手掛者を聞立旅子狂ひを心
## 200021086_00005_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021086_00005_1.jpg" width="512" title="details">
  </p>
  
### Input
五人として重からざる時は威勢な敵かなら<ins>ず</ins>れをあな<ins>ご</ins>る然といへ共親しき<ins>く</ins>にはかろくや<ins>は</ins>らかにむかふべ六妻女に常に勇を可作都て女は邪路に入安能道入難七けんどんはういつのものにともなふ<ins>青し</ins>なかれ八悪人<ins>以</ins>の威勢無<ins>い</ins>羨故<ins>め</ins>何のぼるものは終にはくだる物也九我言葉をすくなくして<ins>化</ins>人の語をきくべし十つねに我口に能道のくつわをふくむべし<ins>と</ins>に酒宴の座につ<ins>く</ins>らなる時は物いふ<ins>と</ins>をつゝしむべし故何となれば酒<ins>爰</ins>の習能<ins>朝</ins>を退けて<ins>比三崎</ins>語をもちゆる物也十一能道を学する時其憚を<ins>辰さ</ins>れ習を<ins>い</ins>れば君子と成物也<ins>春</ins>権<ins>成</ins>を以て人を従んよりはしかし柔にして人になつかしんせられよ

### Pred
五人<ins>では</ins>重<ins>くない</ins>時は<ins>、</ins>威勢<ins>の</ins>ない<ins>敵は必ず負けます。しかし、</ins>親し<ins>み深</ins>く<ins>、穏</ins>やかに<ins>向き合えば、</ins>六<ins>人では楽しく、</ins>妻<ins>や</ins>女に<ins>は</ins>常に勇<ins>気</ins>を<ins>与え、</ins>女は邪路に入<ins>ること</ins>は<ins>できません。七人では、青いものは、</ins>いつ<ins>も</ins>のものに<ins>付き合います。</ins>八人<ins>では、悪い人でも</ins>威勢<ins>がない</ins>の<ins>で、羨ましが</ins>るものは<ins>、何の取り柄もないので、</ins>終<ins>い</ins>にはくだる<ins>ものです。</ins>九<ins>人では、自分の</ins>言葉を<ins>謙虚に</ins>して<ins>、化</ins>人の<ins>言葉</ins>を<ins>聞</ins>き<ins>ま</ins>し<ins>ょう。</ins>十<ins>人では、常</ins>に<ins>自分の</ins>口に道<ins>徳</ins>の<ins>冠</ins>を<ins>かぶって、</ins>酒宴の<ins>席で</ins>は<ins>、</ins>物<ins>言</ins>いをつ<ins>つ</ins>しむべ<ins>きです。</ins>な<ins>ぜなら、</ins>酒<ins>の席</ins>の習<ins>慣は、朝</ins>を退けて<ins>、三崎の</ins>言<ins>葉</ins>を<ins>口に</ins>する<ins>ものです。十一人で</ins>は<ins>、道徳を学ぶ時は、その恥ずかしさを捨て、習い事をす</ins>れば<ins>、</ins>君子<ins>になれます。春</ins>権<ins>成のように、</ins>人を従<ins>わせるので</ins>は<ins>なく、</ins>柔<ins>らかく、</ins>人に<ins>親</ins>し<ins>ま</ins>れ<ins>ましょう。</ins>

### GT
五人として重からざる時は威勢なし敵かならすこれをあなどる然といへ共親しき人にはかろくやワらかにむかふべし六妻女に常に勇を可作都て女は邪路に入安能道入難七けんどんはういつのものにともなふ事なかれ八悪人の威勢無羨故如何のぼるものは終にはくだる物也九我言葉をすくなくして他人の語をきくべし十つねに我口に能道のくつわをふくむべしに酒宴の座につらなる時は物いふをつゝしむべし故何となれば酒宴の習能詞を退けて狂言綺語をもちゆる物也十一能道を学する時其憚を顧ざれ習をはれば君子と成物也十二権威を以て人を従んよりはしかし柔にして人になつかしんせられよ
## 200021763_00002_2
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021763_00002_2.jpg" width="512" title="details">
  </p>
  
### Input
七詰膳並据様五詰膳並据様<ins>く</ins>

### Pred
七膳並据様五膳並据様<ins>く</ins>

### GT
七詰膳並据様五詰膳並据様膳部料理抄
## 200021763_00006_2
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021763_00006_2.jpg" width="512" title="details">
  </p>
  
### Input
平皿<ins>飯鉢</ins>七ツ目<ins>蓋台</ins>中合サ汁再進<ins>煎物</ins>島台土器<ins>飯鉢押肴二種蓋台箸汁再進銚子島台土器提子</ins>押肴二種箸杯台<ins>銚子</ins>平銚子台<ins>提子</ins>

### Pred
平皿<ins>飯鉢</ins>七ツ目<ins>蓋台</ins>中合サ汁再進<ins>煎物</ins>島台土器<ins>飯鉢押肴二種蓋台箸汁再進銚子島台土器提子</ins>押肴二種箸杯台<ins>銚子</ins>平銚子台<ins>提子</ins>

### GT
平皿七ツ目中合サ煎物飯鉢蓋台汁再進島台土器押肴二種箸銚子提子飯鉢蓋台汁再進島台土器押肴二種箸銚子提子杯台平銚子台
## 200021763_00008_2
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021763_00008_2.jpg" width="512" title="details">
  </p>
  
### Input
飯鉢<ins>飯鉢蓋台</ins>蓋台汁再進汁再進置杯<ins>置杯平銚子</ins>平銚子吸物<ins>吸物肴二種</ins>肴二種湯水<ins>湯水</ins>茶菓子<ins>茶菓子</ins>

### Pred
飯鉢<ins>飯鉢蓋台</ins>蓋台汁再進汁再進置杯<ins>置杯平銚子</ins>平銚子吸物<ins>吸物肴二種</ins>肴二種湯水<ins>湯水</ins>茶菓子<ins>茶菓子</ins>

### GT
飯鉢蓋台汁再進置杯平銚子吸物肴二種湯水茶菓子飯鉢蓋台汁再進置杯平銚子吸物肴二種湯水茶菓子
## 200021763_00009_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021763_00009_1.jpg" width="512" title="details">
  </p>
  
### Input
濃茶濃茶後菓子<ins>後菓子薄茶</ins>薄茶以上七詰五詰に次たる尊<ins>る々</ins>の御方の<ins>饗</ins>応御料理なり二汁七菜二汁五菜本膳<ins>本膳膾直汁</ins>膾汁<ins>黍</ins>香物箸煎物<ins>香物箸</ins>坪皿飯<ins>坪以皿飯</ins>

### Pred
濃茶後菓子後菓子<ins>薄茶</ins>薄茶以上七詰五詰に次<ins>ぐ</ins>尊<ins>い</ins>方の<ins>饗</ins>応御料理なり二汁七菜二汁五菜本膳<ins>本膳膾直汁</ins>膾汁<ins>黍</ins>香物箸煎物<ins>香物箸</ins>坪皿飯<ins>坪以皿飯</ins>

### GT
濃茶後菓子薄茶濃茶後菓子薄茶以上七詰五詰に次たる尊貴の御方の餐応御料理なり二汁七菜本膳膾汁小皿香物箸煎物坪皿飯二汁五菜本膳膾汁香物箸煎物坪皿飯
## 200021763_00020_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021763_00020_1.jpg" width="512" title="details">
  </p>
  
### Input
引向おま<ins>半</ins>鯛二玉子ふわ〱<ins>長皿ふた物</ins>薄鳥<ins>平皿御所麩</ins>猪口薄<ins>モ</ins>雪<ins>主花かつ尾</ins>ふ<ins>くる之</ins>焼物一しほかれゐ懸下け<ins>肴一鳥鴨</ins>銚子<ins>すれんこん</ins>吸物花<ins>以</ins>か<ins>ぜらかし</ins>こせ<ins>銚子</ins>肴<ins>湯</ins>鯖粧漬湯<ins>石</ins>する<ins>州する</ins>

### Pred
引向おま<ins>半</ins>鯛二玉子ふわ〱<ins>長皿ふた物</ins>薄鳥<ins>平皿御所麩</ins>猪口薄<ins>モ</ins>雪<ins>主花かつ尾</ins>ふ<ins>くる之</ins>焼物一しほかれゐ懸下け<ins>肴一鳥鴨</ins>銚子<ins>すれんこん</ins>吸物花<ins>以</ins>か<ins>ぜらかし</ins>こせ<ins>銚子</ins>肴<ins>湯</ins>鯖粧漬湯<ins>石</ins>する<ins>州する</ins>

### GT
引向長皿おまつ鯛平皿御所麩花かつおくるミ肴一鳥鴨一すれんこんせうか銚子湯する二ふた物玉子ふわ〱薄鳥猪口薄雪もミふし焼物一しほかれゐ懸下け銚子吸物花いかこせう肴一鯖粧漬湯する
## 200021763_00025_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021763_00025_1.jpg" width="512" title="details">
  </p>
  
### Input
七詰五詰の組合<ins>花</ins>積立<ins>ミ</ins>略図本膳鯛作り身<ins>も錦鱠</ins>細作り魚<ins>汁小かふ</ins>く大根<ins>しい茸</ins>せか<ins>皮牛房</ins>房風<ins>青な</ins>杉小<ins>金</ins>角<ins>此かん</ins>なら漬瓜<ins>香物</ins>ミそ漬大根<ins>之</ins>もり口漬花塩山升杉曲物焼魚<ins>煮物</ins>花ゑひ<ins>飯</ins>くしこ敷葛

### Pred
七詰五詰の組合<ins>花</ins>積立<ins>ミ</ins>略図本膳鯛作り身<ins>も錦鱠</ins>細作り魚<ins>汁小鍋</ins>大根<ins>しい茸</ins>せか<ins>皮牛房</ins>房風<ins>青な</ins>杉小<ins>金</ins>角<ins>此かん</ins>なら漬瓜<ins>香物味噌</ins>漬大根<ins>之</ins>もり口漬花塩山升杉曲物焼魚<ins>煮物</ins>花ゑひ<ins>飯</ins>くしこ敷葛

### GT
七詰五詰の組合并積立之略図本膳膾煮物香物汁飯膾鯛作り身細作り魚くり大根せうか房風金かん杉小角香物なら漬瓜ミそ漬大根もり口漬花塩山升杉曲物煮物焼魚花ゑひくしこ敷葛汁鶴小かふしい茸皮牛房青な飯
## 200021763_00042_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021763_00042_1.jpg" width="512" title="details">
  </p>
  
### Input
柿ゑた柿<ins>楊</ins>栗かや<ins>棹</ins>子橙柑くるみこんふ右の類なり此外色々あるへし一汁なとには一通り菓子出る時は茶菓子<ins>色</ins>と此菓子と交て盛合する事もあり向略儀にて餅菓子蒸菓<ins>ふ</ins>を盛合す<ins>わメ</ins>もあり<ins>す</ins>時の心得なり一濃茶極昔極抄の類薄茶は初むかしほとの銘ある茶を出すなり以上の趣ハ献立の肴組の荒増なれも此心を以取合せへ

### Pred
柿<ins>、楊</ins>栗<ins>、棹</ins>子<ins>、</ins>橙柑<ins>、</ins>くるみ<ins>、</ins>こんふ<ins>、</ins>右の類な<ins>どが</ins>あ<ins>り、他にも様々な菓子があります。</ins>一汁には一通り菓子<ins>が</ins>出<ins>て、</ins>茶菓子<ins>、色</ins>菓子<ins>、この菓子など</ins>と<ins>合わせ</ins>て盛合<ins>せを</ins>する<ins>こと</ins>もあり<ins>ま</ins>す<ins>。</ins>時の心得<ins>として、餅菓子、蒸菓子を合わせて出すこともあ</ins>り<ins>ます。</ins>極昔極抄の類<ins>、</ins>薄茶は<ins>、</ins>銘<ins>の</ins>ある茶を出す<ins>ものです。</ins>以上の趣<ins>は、</ins>献立の肴組の荒増<ins>で</ins>も<ins>あります。</ins>

### GT
柿ゑた柿搗栗かや掉子橙柑くるみこんふ右の類なり此外色々あるへし一汁なとには一通り菓子出る時は茶菓子の品と此菓子と交て盛合する事もあり一向略儀にて餅菓子蒸菓子を盛合する事もあり其時の心得なり一濃茶は極昔極抄の類薄茶は初むかしほとの銘ある茶を出すなり以上の趣ハ献立の肴組の荒増なれとも此心を以取合せへし
## 200021869_00003_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021869_00003_1.jpg" width="512" title="details">
  </p>
  
### Input
<ins>ゝ</ins>右一<ins>は</ins>

### Pred
右一<ins>は</ins>

### GT
右一水
## 200021869_00012_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200021869_00012_1.jpg" width="512" title="details">
  </p>
  
### Input
かまほこ拵方<ins>し</ins>事玉子そふめんの如にそれを<ins>ほ</ins>竹の<ins>れ同比ほ</ins>二ツ割し両方<ins>て更</ins>ふ<ins>し</ins>しを付其中へ入さ<ins>しそ</ins>をうす<ins>て</ins>そきもよふなる<ins>に</ins>ふに入へしそれをふ<ins>ゝ</ins>かし外へ玉子を<ins>ぬ</ins>るへ<ins>へ</ins>し<ins>青意ケわしぞ</ins>

### Pred
かまほこ拵方<ins>し</ins>事玉子そふめんの如にそれを<ins>ほ</ins>竹の<ins>れ同比ほ</ins>二ツ割し両方を付其中へ入へしそれをふ<ins>ゝ</ins>かし外へ玉子を<ins>ぬ</ins>るへ<ins>へ</ins>し<ins>青意ケわしぞ</ins>

### GT
かまほこ拵方之事玉子そふめんの如にそれを竹の筒を二ツ割し両方へふしを付其中へ入さかなをうすくそきもよふなるよふに入へしそれをふかし外へ玉子をふるへし
## 200022050_00002_2
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200022050_00002_2.jpg" width="512" title="details">
  </p>
  
### Input
▲祝言引渡之次第一<ins>歌</ins>栗ほそきかたをむ<ins>に也んレ一三ツかわらけ</ins>成やうに三かくにお<ins>ゝ</ins>也<ins>也</ins>一のし二本<ins>寸すま</ins>ひろきかたをきやくのひだりの<ins>ぶ</ins>かたへしておきて<ins>こか</ins>し昆布切かぶなて<ins>りたに</ins>也一てうしひさ<ins>けきりお</ins>一まきずるめ<ins>のさ</ins>か<ins>なかレ事</ins>すミ一か<ins>かす</ins>こしもちくしこむすびこんぶ<ins>一むめぼし三ツざうに</ins>いもひ<ins>ら</ins>かつうほくしあ<ins>げひ</ins>一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとす<ins>ま</ins>也一ねぶか二本しろに<ins>ね</ins>一か<ins>かん</ins>んざけ<ins>とも</ins>

### Pred
祝言引渡之次第一<ins>歌</ins>栗ほそきかたをむ<ins>に也んレ一三ツかわらけ</ins>成やうに三かくにお<ins>ゝ</ins>也<ins>也</ins>一のし二本<ins>寸すま</ins>ひろきかたをきやくのひだりの<ins>ぶ</ins>かたへしておきて<ins>こか</ins>し昆布切かぶなて<ins>りたに</ins>也一てうしひさ<ins>けきりお</ins>一まきずるめ<ins>のさ</ins>か<ins>なかレ事</ins>すミ一か<ins>かす</ins>こしもちくしこむすびこんぶ<ins>一むめぼし三ツざうに</ins>いもひ<ins>ら</ins>かつうほくしあ<ins>げひ</ins>一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとす<ins>ま</ins>也一ねぶか二本しろに<ins>ね</ins>一か<ins>かん</ins>んざけ<ins>とも</ins>

### GT
▲祝言引渡之次第一栗ほそきかたをむふへ成やうに三かくにおく也一三ツかわらけ一のし二本ひろきかたをきやくのひだりのかたへしておきてよし一昆布二切かぶなりにきりておく也一てうしひさげ一さかな一まきずるめ一からすミ一かずのこ一むめぼし三ツざうにもちくしこむすびこんぶいもひゝかつうほくしあわび一たつくり三ツ一ぬりさかづき一吸物ひれの物をほんとする也一ねぶか二本しろねともに一かんざけ
## 200022050_00006_1
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200022050_00006_1.jpg" width="512" title="details">
  </p>
  
### Input
をなどふたどきてい候是すてひの入吉立ハふたのくあん汁ハかハをはぎおろきて<ins>は</ins>おもミをも<ins>人</ins>入した時あげて水にてひや酒をかけをく汁時入ぶをしほげんすい合出又すまの<ins>斗</ins>にけ少候此時ハおきくしだい入せ中そにだをくに候どぶをさて吉<ins>に</ins>大ん外<ins>入</ins>但久くたきてハのあぢ悪候あきそをたきの也いつれもそをかうて久敷に候しるにハ此ちすい口さんせのこ同葉<ins>鶉</ins>の汁だにほねを入せんそにて仕立さん大也つまハその時のけい<ins>ふ</ins>つ吉きの<ins>は</ins>いほ数入吉何時もすぢをおびゆ又<ins>し</ins>めゟ中そにてしたてゟすに汁中て仕立候又につま時の物也り次入いんにてもかにてをいだを入ねを生たれ少てを入しほ<ins>け</ins>んすい合出是もつまハ時の物惣のこハ鳥汁にい入吉いびゆ吉あをちのたを

### Pred
をなどふたどきてい候是すてひの入吉立ハふた<ins>蓋</ins>汁ハかハをはぎおろきて<ins>は</ins>おもミをも<ins>人</ins>入した時あげて水にてひや酒をかけをく汁時入ぶをしほげんすい合出又すまの<ins>斗</ins>にけ少候此時ハおきくしだい入せ中そにだをくに候どぶをさて吉<ins>に</ins>大ん外<ins>入</ins>但久くたきてハのあぢ悪候あきそをたきの也いつれもそをかうて久敷に候しるにハ此ちすい口さんせのこ同葉<ins>鶉</ins>の汁だにほねを入せんそにて仕立さん大也つまハその時のけい<ins>ふ</ins>つ吉きの<ins>は</ins>いほ数入吉何時もすぢをおびゆ又<ins>し</ins>めゟ中そにてしたてゟすに汁中て仕立<ins>た</ins>候又につま時の物也り次入いんにてもかにてをいだを入ねを生たれ少てを入しほ<ins>け</ins>んすい合出是もつまハ時の物惣のこハ鳥汁にい入吉いびゆ吉あをちのたを

### GT
うをなどもふくたうもどきとていたし候是もかわをはぎすてひぶくのかわ入吉立やうハふくたうのくあんかう汁ハかハをはぎおろしきりてかハおもミをもにゑゆへ入しらミたる時あげて水にてひやし其後酒をかけをくミそ汁にへ立候時うをゝ入どぶをさししほかげんすい合出し候也又すましの時ハだし計にかけも少おとし候此時ハうハおきさくしだいに入どせう汁中ミそにだしをくハへよくに申候どぶをさして吉つまハごぼう大こん其外色々但久しくたき候てハミそのあぢ悪候左候へハあたらしきミそをたてさしニて出しよきもの也いつれもミそをかうして久敷に申候しるにハ此こゝろもち入る也すい口さんせうのこ同葉鶴の汁ハだしにほねを入せんじさしミそにて仕立候さしかげん大事也つまハその時のけいぶつ吉きのこハいかほど数入候ても吉何時もすぢをおくすい口わさびゆ又はじめゟ中ミそにてもしたてゟすましにも白鳥汁中ミそにて仕立候又すましにもつまハ時分の物也つくり次第入かハいりハがんにてもかもにてもかハをいりだしを入ほねをせんじ生たれ少さして身を入しほかげんすい合出し候是もつまハ時の物惣別木のこハ鳥汁にいつも入候て吉すい口わさびゆ吉あをかちハきじのわたを
## 200022050_00010_2
  <p align="left">
    <img src="/zero_shot/RakutenAI-7B-Instruct/imgs/200022050_00010_2.jpg" width="512" title="details">
  </p>
  
### Input
も有そべまのげんハなをなてあにすのおほくあまり候ハぬか候のしろ鱠ふな<ins>〱</ins>ま<ins>ふ</ins>きふななすを入すにあひり鱠あめのを三まおろ身ハすきてつ両のを打合かハめやききざ入たのいのくきをさがき入すしほげんてあへ候い也ハもしきばきあゆにてもあめのをの<ins>シ</ins>く仕候れも身すきてつり候しやきぬなしをよてさけのくすりあ<ins>にて</ins>にても<ins>出</ins>にまづすにていそのすをすてのちにぬたをすにてのべすんてあへ後のすおほきハ悪候たしあゆにて<ins>は</ins>あをまのぬたにゆのはミ入あ鱠ほのいあいりいりざけすたにてあへ候たあのちに入<ins>さ</ins>けも吉花つほ三月大木くげなどきざ吉<ins>酔</ins>いのうすほねやきむ取て田つりいて川ゑひ木くりしお入てすしほげんしてあ候わびがんかも同けなどつすにて

### Pred
有そべまのげんハなをなてあにすのおほくあまり候ハぬか候のしろ鱠ふな<ins>〱</ins>ま<ins>ふ</ins>きふななすを入すにあひり鱠あめのを三まおろ身ハすきてつ両のを打合かハめやききざ入たのいのくきをさがき入すしほげんてあへ候い也ハもしきばきあゆにてもあめのをの<ins>シ</ins>く仕候れも身すきてつり候しやきぬなしをよてさけのくすりあにてに<ins>で</ins>も<ins>出</ins>にまづすにていそのすをすてのちにぬたをすにてのべすんてあへ後のすおほきハ悪候たしあゆにて<ins>は</ins>あをまのぬたにゆのはミ入あ鱠ほのいあいりいりざけすたにてあへ候たあのちに入<ins>さ</ins>けも吉花つほ三月大木くげなどきざ吉<ins>酔</ins>いのうすほねやきむ取て田つりいて川ゑひ木くりしお入てすしほげんしてあ候わびがんかも同けなどつすにて

### GT
も有そうべつなますのかげんハなますをミなもりてあとにすのおほくあまり候ハぬかよく候このしろ鱠ふなのくやまぶきあへハふななますをからし入すにあへ申事也ひてり鱠あめのうを三まいにおろし身ハすきてつくり両のかハを打合かハめよりやきてきざミ入たうのいものくきをさゝがき入すしほかげんしてあへ候をいふ也かハもしらやき也かばやき鱠あゆにてもあめのうをのく仕候事也これも身ハすきてつくり候かハしらやきぬたなますからしをよくすりてさけのかすをよくすりあゆにてもいわしにてもなよしにてもまづすにていためそのすをすてのちにぬたをすにてのべすかげんしてあへ候也後のすおほきハ悪候たゞしあゆにてハあをまめのぬたにゆのはきざミ入あへ申事も有太郎助鱠一しほのたいあわひなどいかにもうすくつくりいりざけすたうぶんにしてあへ候たゞしあわひハのちに入吉ますざけも吉花がつほ三月大こん木くらげなどきざミ入て吉やきほね鱠たいのうすミほねなとやきむしり取て田つくりいりて川ゑひ木くらげくりしやうがおろしなと入てすしほかげんしてあへ申候わさびあへがんかも同もゝけなどつくりすにて

## Error Type Summary

The categories below are based on a three-way comparison among `Input`, `Pred`, and `GT`. In short, `Input` is the noisy OCR source, `Pred` is the model's attempted correction, and `GT` is the target transcription.

### 1. Modernization and explanatory rewriting

The most prominent failure mode is strong modernization or explanatory rewriting from Input. In `100249376_00022_2`, `100249376_00050_1`, `100249416_00034_1`, and `100249476_00007_2`, the model rewrites the original text into modern recipe-like Japanese rather than preserving the historical transcription. It also converts measurements into modern forms such as `1升`, `2合`, and `4分の1`, adds punctuation, and inserts explanatory phrasing. These outputs may be readable, but they are far from the GT transcription target.

### 2. Semantic hallucination and over-interpretation

Several predictions introduce content that is not supported by the source. For example, `100249376_00022_2` turns a noisy confectionery procedure into a modernized recipe with inferred ingredients and preparation steps. Similar over-interpretation appears in `100249476_00007_2`, where the model summarizes the cooking method in modern terms. This indicates that the model sometimes treats the task as explanation or translation instead of OCR correction.

### 3. Input-copying mixed with partial normalization

Other samples show the opposite behavior: the model copies noisy Input while making small local normalizations. This appears in `200015843_00110_1`, `200022050_00002_2`, `200022050_00006_1`, and `200022050_00010_2`. The result is a hybrid output: long spans remain corrupted, but individual words are modernized or replaced. This neither preserves the source faithfully nor recovers the GT.

### 4. Layout/order errors in list-like text

The `200021763_*` samples reveal persistent problems with structured lists. These texts contain menu items, vessels, and serving sequences. The model often keeps recognizable texts, but the grouping and reading order remain wrong. `200021763_00006_2`, `200021763_00008_2`, `200021763_00020_1`, and `200021763_00042_1` are representative layout-sensitive failures.

### 5. Length instability on long passages

Long samples show both expansion and compression. `200021086_00005_1` expands from GT_Length 267 to Pred_Length 340, while `200022050_00006_1` and `200022050_00010_2` are closer to the 300-character range and still miss large parts of the GT. The model is therefore not simply capped; it is unstable, sometimes explaining too much and sometimes copying or truncating long recipe-like text.

### 6. Classical kana and short-text character confusions

Short samples such as `200006663_00006_2`, `200021763_00002_2`, `200021869_00003_1`, and `200021869_00012_1` show fine-grained errors in historical kana, small marks, voicing, and visually similar characters. Because these texts are short, a few substitutions or omissions create a high CER.

### 7. Domain vocabulary errors

Cooking, confectionery, menu, and vessel terminology is a major source of mistakes. The model often replaces specialized historical terms with modern recipe vocabulary or guesses plausible ingredients and procedures. This is visible in `100249376_00022_2`, `100249376_00050_1`, `100249416_00034_1`, `100249476_00007_2`, `200022050_00002_2`, `200022050_00006_1`, and `200022050_00010_2`. Domain-specific adaptation is likely necessary.

### Overall

RakutenAI-7B-Instruct has a strongly interpretive error profile. Its main weakness is not only copying noisy input, but also rewriting historical culinary text into modern explanatory Japanese. This causes high CER because the target is faithful transcription, not translation or summarization. The model also struggles with list layouts, long passages, short historical-kana fragments, and specialized cooking vocabulary. Future improvements should emphasize strict transcription constraints, suppression of paraphrasing and measurement normalization, layout-aware reading-order recovery, and stronger domain adaptation for classical recipe and confectionery texts.
