// because of autocomplete bug
// if the answer starts with a number, need to precede it with a space (" ")
// otherwise it won't be available

let songs = [
  {
    url: "https://soundcloud.com/nayeon-music/abcd-extended-version?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NAYEON - ABCD (Extended Version)"
  },
  {
    url: "https://soundcloud.com/vcreamy/kara-mr?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "lmDaawn - KARA - Mr."
  },
  {
    url: "https://soundcloud.com/twice-57013/alcohol-free",
    answer: "Twice - Alcohol Free"
  },
  {
    url: "https://soundcloud.com/tm-950004586/orange-caramel-catallena",
    answer: "Orange Caramel - Catallena"
  },
  {
    url: "https://soundcloud.com/le-sserafim/1-800-hot-n-fun?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - 1-800-hot-n-fun"
  },
  {
    url: "https://soundcloud.com/skkzyx/pristin-v-get-it",
    answer: "Pristin V - Get It"
  },
  {
    url: "https://soundcloud.com/mina-anh-967372179/very-very-very-ioi",
    answer: "I.O.I - Very Very Very"
  },
  {
    url: "https://soundcloud.com/ive59257/my-satisfaction?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "IVE - My Satisfaction"
  },
  {
    url: "https://soundcloud.com/afiqashura/t-ara-so-crazy-korean-ver?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "AfiqAshura - T-ARA - So Crazy (Korean ver.)"
  },
  {
    url: "https://soundcloud.com/whdans860/rainbow-a?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "whdans860 - Rainbow - A"
  },
  {
    url: "https://soundcloud.com/chungha_official/chung-ha-sparkling",
    answer: "Chung Ha - Sparkling"
  },
  {
    url: "https://soundcloud.com/niziu-music/heartris?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NiziU - HEARTRIS"
  },
  {
    url: "https://soundcloud.com/itzy-music/wannabe",
    answer: "ITZY - Wannabe"
  },
  {
    url: "https://soundcloud.com/l2share59/exid-lady",
    answer: "EXID - Lady"
  },
  {
    url: "https://soundcloud.com/fromis_9/miracle?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "fromis_9 - Miracle"
  },
  {
    url: "https://soundcloud.com/rororomeo/fx-nu-nu-abo",
    answer: "F(X) - Nu Abo"
  },
  {
    url: "https://soundcloud.com/l2share131/aespa-next-level-1",
    answer: "Aespa - Next Level"
  },
  {
    url: "https://soundcloud.com/l2share131/fromis_9-we-go",
    answer: "fromis_9 - We Go"
  },
  {
    url: "https://soundcloud.com/xoxoamira23/stellar-marionette?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "AmiraS_23 - Stellar - Marionette"
  },
  {
    url: "https://soundcloud.com/kusumahusnina/f-x-hot-summer",
    answer: "F(X) - Hot Summer"
  },
  {
    url: "https://soundcloud.com/wfxb0pd3jqyx/brave-girls-rollin",
    answer: "Brave Girls - Rollin'"
  },
  {
    url: "https://soundcloud.com/susan/vibrato-stellar?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "s - Vibrato (떨려요) - Stellar (스텔라)"
  },
  {
    url: "https://soundcloud.com/hoxl1e5ylvbp/miss-a-bad-girl-good-girl",
    answer: "Miss A - Bad Girl Good Girl"
  },
  {
    url: "https://soundcloud.com/fromis_9/be-with-you?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "fromis_9 - Be With You"
  },
  {
    url: "https://soundcloud.com/josedestroy/exid-updown",
    answer: "EXID - Up & Down"
  },
  {
    url: "https://soundcloud.com/shwi_wie/cherry-bullet-love-so-sweet",
    answer: "Cherry Bullet - Love So Sweet"
  },
  {
    url: "https://soundcloud.com/twice-57013/the-feels",
    answer: "Twice - The Feels"
  },
  {
    url: "https://soundcloud.com/aylin-leandro-ferre/weki-meki-i-dont-like-your-girlfriend",
    answer: "Weki Meki - I Don't Like Your Girlfriend"
  },
  {
    url: "https://soundcloud.com/l2share86/fanatics-sunday",
    answer: "Fanatics - Sunday"
  },
  {
    url: "https://soundcloud.com/genrse/blackpink-whistle",
    answer: "Blackpink - Whistle"
  },
  {
    url: "https://soundcloud.com/le-sserafim/crazy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - CRAZY"
  },
  {
    url: "https://soundcloud.com/xiz-thic/ioi-whatta-man-good-man",
    answer: "I.O.I - Whatta Man"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/how-you-like-that",
    answer: "Blackpink - How You Like That"
  },
  {
    url: "https://soundcloud.com/2ne1official/i-am-the-best",
    answer: " 2NE1 - I Am The Best"
  },
  {
    url: "https://soundcloud.com/twice-57013/cheer-up",
    answer: "Twice - Cheer Up"
  },
  {
    url: "https://soundcloud.com/user-674947085/hq-secret-im-in-love-official-audio?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Sebas Mares - [HQ] 시크릿(SECRET) - I'm In Love (Official Audio)"
  },
  {
    url: "https://soundcloud.com/le-sserafim/pierrot?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - Pierrot"
  },
  {
    url: "https://soundcloud.com/l2share77/loona-butterfly",
    answer: "Loona - Butterfly"
  },
  {
    url: "https://soundcloud.com/ohmygirl-music/nonstop",
    answer: "Oh My Girl - Nonstop"
  },
  {
    url: "https://soundcloud.com/l2share44/fromis_9-love-bomb",
    answer: "fromis_9 - Love Bomb"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/roller-coaster?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NMIXX - Roller Coaster"
  },
  {
    url: "https://soundcloud.com/seasaltfishes/red-velvet-rbb-really-bad",
    answer: "Red Velvet - Really Bad Boy"
  },
  {
    url: "https://soundcloud.com/sophia-jesa/hows-this-hyuna",
    answer: "Hyuna - How's This?"
  },
  {
    url: "https://soundcloud.com/miss-a-official/bad-girl-good-girl-kor",
    answer: "Miss A - Bad Girl Good Girl"
  },
  {
    url: "https://soundcloud.com/zii-kaka/twice-scientist?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "Zii Kaka Music - TWICE - SCIENTIST"
  },
  {
    url: "https://soundcloud.com/junmin501/t-ara-i-go-crazy-because-of-you?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "junmin501 - T-ara - I Go Crazy Because of You"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/shut-down",
    answer: "Blackpink - Shut Down"
  },
  {
    url: "https://soundcloud.com/ph-ng-vy-35477112/im-so-sick",
    answer: "APink - I'm So Sick"
  },
  {
    url: "https://soundcloud.com/ernchern/like-a-cat-aoa",
    answer: "AOA - Like A Cat"
  },
  {
    url: "https://soundcloud.com/sunmi-sc/24-hours?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "SUNMI - 24 Hours"
  },
  {
    url: "https://soundcloud.com/l2share95/red-velvet-queendom",
    answer: "Red Velvet - Queendom"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/sonar-breaker?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NMIXX - Soñar (Breaker)"
  },
  {
    url: "https://soundcloud.com/user-55808555/blackpink?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "BLACKPINK - 마지막처럼 - BLACKPINK"
  },
  {
    url: "https://soundcloud.com/9flawless/blackpink-as-if-its-your-last",
    answer: "Blackpink - As If It's Your Last"
  },
  {
    url: "https://soundcloud.com/girlsday-sc/something?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "Girl's Day - Something"
  },
  {
    url: "https://soundcloud.com/katseye-music/touch?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "KATSEYE - Touch"
  },
  {
    url: "https://soundcloud.com/user-913229388/f-x-4-walls",
    answer: "F(X) - 4 Walls"
  },
  {
    url: "https://soundcloud.com/marshall_line/kill-bill",
    answer: "Brown Eyed Girls - Kill Bill"
  },
  {
    url: "https://soundcloud.com/kekkun89/t-ara-roly-poly",
    answer: "T-ara - Roly Poly"
  },
  {
    url: "https://soundcloud.com/wahyu_putra/sistar-touch-my-body-at-wahyoe",
    answer: "Sistar - Touch My Body"
  },
  {
    url: "https://soundcloud.com/vdtpin/9muses-hurt-locker?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "PIN - 9muses - 다쳐(Hurt Locker)"
  },
  {
    url: "https://soundcloud.com/mungikim/pristin-wee-woo",
    answer: "Pristin - Wee Woo"
  },
  {
    url: "https://soundcloud.com/twice-57013/i-cant-stop-me",
    answer: "Twice - I Can't Stop Me"
  },
  {
    url: "https://soundcloud.com/elxi-aj/girls-day-ring-my-bell-jpn-ver?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "cheezy7 - Girl's Day - Ring My Bell (Japanese Ver.)"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/dice?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NMIXX - DICE"
  },
  {
    url: "https://soundcloud.com/faiz-zarul/dia-will-you-go-out-with-me-1",
    answer: "DIA - Will You Go Out With Me"
  },
  {
    url: "https://soundcloud.com/le-sserafim/hot",
    answer: "LE SSERAFIM - HOT"
  },
  {
    url: "https://soundcloud.com/shxhrol-amy/playingwithfire?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "BLACKPINK - 불장난 - BLΛƆKPIИK (블랙핑크)"
  },
  {
    url: "https://soundcloud.com/l2share138/kep1er-wa-da-da",
    answer: "Kep1er - Wa Da Da"
  },
  {
    url: "https://soundcloud.com/handa-vempire-chanjuan/wonder-girls-tell-me-2012-korean-version",
    answer: "Wonder Girls - Tell Me"
  },
  {
    url: "https://soundcloud.com/l2share47/weki-meki-crush",
    answer: "Weki Meki - Crush"
  },
  {
    url: "https://soundcloud.com/aespaofficial/drama",
    answer: "Aespa - Drama"
  },
  {
    url: "https://soundcloud.com/aespaofficial/better-things?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "aespa - Better Things"
  },
  {
    url: "https://soundcloud.com/h-ng-d-ng-qu-t/magic-girl-orange-caramel?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Hướng Dương Quỳ Tử - Magic Girl - Orange Caramel"
  },
  {
    url: "https://soundcloud.com/62442magic/dholic-chewy?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "45CM - D.Holic - Chewy"
  },
  {
    url: "https://soundcloud.com/aespaofficial/armageddon?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "aespa - Armageddon"
  },
  {
    url: "https://soundcloud.com/lukas-moskalis-293120113/stellar-sting?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "스텔라 - 찔려 Stellar Sting"
  },
  {
    url: "https://soundcloud.com/itzy-music/snowy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "ITZY - Snowy"
  },
  {
    url: "https://soundcloud.com/somi_official/birthday-2",
    answer: "Somi - Birthday"
  },
  {
    url: "https://soundcloud.com/l2share95/red-velvet-psycho",
    answer: "Red Velvet - Psycho"
  },
  {
    url: "https://soundcloud.com/interscope/girls-generation-the-boys-8",
    answer: "Girl's Generation - The Boys"
  },
  {
    url: "https://soundcloud.com/not_ur_sepai/girls-generation-party",
    answer: "Girl's Generation - Party"
  },
  {
    url: "https://soundcloud.com/eohu/abracadabra-brown-eyed-girls?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Myrai Kotoba - Abracadabra - Brown Eyed Girls"
  },
  {
    url: "https://soundcloud.com/lightsum/honey-or-spice?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LIGHTSUM - Honey or Spice"
  },
  {
    url: "https://soundcloud.com/twice-57013/fancy",
    answer: "Twice - Fancy"
  },
  {
    url: "https://soundcloud.com/kep1er-music/giddy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "Kep1er - Giddy"
  },
  {
    url: "https://soundcloud.com/quan-mai-anh/lovelyz-obliviate",
    answer: "LovelyZ - Obliviate"
  },
  {
    url: "https://soundcloud.com/itsvee/short-hair-aoa",
    answer: "AOA - Short Hair"
  },
  {
    url: "https://soundcloud.com/eohu/abracadabra-brown-eyed-girls",
    answer: "Brown Eyed Girls - Abracadabra"
  },
  {
    url: "https://soundcloud.com/ohmygirl-music/coloring-book",
    answer: "Oh My Girl - Coloring Book"
  },
  {
    url: "https://soundcloud.com/le-sserafim/crazier?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - Crazier"
  },
  {
    url: "https://soundcloud.com/l2share55/t-ara-whats-my-name?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "티아라 (T-ARA) - 티아라 (T-ARA) - 내 이름은 (What's My Name?)"
  },
  {
    url: "https://soundcloud.com/user-339323148/stayc-stereotype",
    answer: "StayC - Stereotype"
  },
  {
    url: "https://soundcloud.com/le-sserafim/chasing-lightning?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - Chasing Lightning"
  },
  {
    url: "https://soundcloud.com/greenmusic-channel/bo-peep-bo-peep-t-ara",
    answer: "T-ara - Bo Peep Bo Peep"
  },
  {
    url: "https://soundcloud.com/hotaru-le-huynh/dal-shabet-joker-engromhan-picture-color-coded-hd?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Hotaru Le Huynh - Dal Shabet - Joker"
  },
  {
    url: "https://soundcloud.com/user-782826028/billlie-flippng-a-coin",
    answer: "Billlie - Flipping A Coin"
  },
  {
    url: "https://soundcloud.com/mcnlight/hyuna-babe",
    answer: "Hyuna - Babe"
  },
  {
    url: "https://soundcloud.com/sakura97fati/4minute-whatcha-doin-today?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: ".Lotus.Fati. - 4MINUTE - Whatcha Doin' Today"
  },
  {
    url: "https://soundcloud.com/emi-oneill/after-school-weeekly",
    answer: "Weeekly - After School"
  },
  {
    url: "https://soundcloud.com/twice-57013/talk-that-talk?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "TWICE - Talk that Talk"
  },
  {
    url: "https://soundcloud.com/l2share47/loona-favorite",
    answer: "Loona - favOriTe"
  },
  {
    url: "https://soundcloud.com/tokkitokkii/audio-tara-sugar-free?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "WhiteRabbit - T-ARA - Sugar Free"
  },
  {
    url: "https://soundcloud.com/etsuko-hime/kara-lupin?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Etsuko Hime - KARA - LUPIN(루팡)"
  },
  {
    url: "https://soundcloud.com/meovv-music/meow?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "MEOVV - MEOW"
  },
  {
    url: "https://soundcloud.com/boatbanana/red-velvet-dumb-dumb",
    answer: "Red Velvet - Dumb Dumb"
  },
  {
    url: "https://soundcloud.com/le-sserafim/impurities?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - Impurities"
  },
  {
    url: "https://soundcloud.com/somi_official/what-you-waiting-for",
    answer: "Somi - What You Waiting For"
  },
  {
    url: "https://soundcloud.com/wonder-girls/rewind?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "Wonder Girls - Rewind"
  },
  {
    url: "https://soundcloud.com/destinee-nsombe/wjsn-cosmic-girls-i-wish",
    answer: "WJSN - I Wish"
  },
  {
    url: "https://soundcloud.com/sophia-jesa/la-vie-en-rose-izone",
    answer: "IZONE - La Vie En Rose"
  },
  {
    url: "https://soundcloud.com/crystal7t/crazy-4minute",
    answer: "4Minute - Crazy"
  },
  {
    url: "https://soundcloud.com/karina-irgintya/gfriend-glass-bead",
    answer: "GFriend - Glass Bead"
  },
  {
    url: "https://soundcloud.com/twice-57013/tt",
    answer: "Twice - TT"
  },
  {
    url: "https://soundcloud.com/aespaofficial/illusion?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "aespa - Illusion"
  },
  {
    url: "https://soundcloud.com/fromis_9/glass-shoes-from-fromis_9-pre?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "fromis_9 - Glass Shoes (From fromis_9 Pre-Debut)"
  },
  {
    url: "https://soundcloud.com/user746128857/aoa-heart-attack",
    answer: "AOA - Heart Attack"
  },
  {
    url: "https://soundcloud.com/l2share52/izone-violeta",
    answer: "IZONE - Violeta"
  },
  {
    url: "https://soundcloud.com/l2share128/taeyeon-weekend",
    answer: "Taeyeon - Weekend"
  },
  {
    url: "https://soundcloud.com/itzy-music/mr-vampire?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "ITZY - Mr. Vampire"
  },
  {
    url: "https://soundcloud.com/rodsepp/we-like",
    answer: "Pristin - We Like"
  },
  {
    url: "https://soundcloud.com/nicollette-prince/girls-day-something?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "$K - Girls day: something"
  },
  {
    url: "https://soundcloud.com/absinthe-330735846/twice-doughnut-1?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "z ? - doughnut by twice"
  },
  {
    url: "https://soundcloud.com/ive59257/ive-accendio?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "IVE - Accendio"
  },
  {
    url: "https://soundcloud.com/faby-queen/hyuna-red",
    answer: "Hyuna - Red"
  },
  {
    url: "https://soundcloud.com/l2share49/red-velvet-zimzalabim",
    answer: "Red Velvet - Zimzalabim"
  },
  {
    url: "https://soundcloud.com/ella-marie/t-ara-like-the-first-time?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Ella Marie 12 - T-ara - Like The First Time"
  },
  {
    url: "https://soundcloud.com/l2share106/sunmi-pporappippam",
    answer: "Sunmi - pporappippam"
  },
  {
    url: "https://soundcloud.com/l2share140/ive-eleven",
    answer: "IVE - Eleven"
  },
  {
    url: "https://soundcloud.com/dani-martins-neves/girls-generation-i-got-a-boy",
    answer: "Girl's Generation - I Got A Boy"
  },
  {
    url: "https://soundcloud.com/4minute/hot-issue",
    answer: "4Minute - Hot Issue"
  },
  {
    url: "https://soundcloud.com/chic-el/wonder-girls-nobody-english-version",
    answer: "Wonder Girls - Nobody"
  },
  {
    url: "https://soundcloud.com/twice-57013/set-me-free?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "TWICE - SET ME FREE"
  },
  {
    url: "https://soundcloud.com/xikanist/fromis_9-glass-shoes",
    answer: "fromis_9 - Glass Shoes"
  },
  {
    url: "https://soundcloud.com/z_u_z_u_n_i/stayc-asap",
    answer: "StayC - ASAP"
  },
  {
    url: "https://soundcloud.com/seasaltfishes/power-up",
    answer: "Red Velvet - Power Up"
  },
  {
    url: "https://soundcloud.com/my-ng-c-867287818/girls-generation-forever-1",
    answer: "Girl's Generation - FOREVER 1"
  },
  {
    url: "https://soundcloud.com/exo-baekhyun/miss-a-hush",
    answer: "Miss A - Hush"
  },
  {
    url: "https://soundcloud.com/triples46067/girls-never-die?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "tripleS - Girls Never Die"
  },
  {
    url: "https://soundcloud.com/twice-57013/more-more",
    answer: "Twice - More and More"
  }
];