// because of autocomplete bug
// if the answer starts with a number, need to precede it with a space (" ")
// otherwise it won't be available

let songs = [
  {
    url: "https://soundcloud.com/soffi-58611342/xg-shooting-star?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "S_owu - XG - SHOOTING STAR"
  },
  {
    url: "https://soundcloud.com/corny-tran/come-back-home-2ne1?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Corny Tran - COME BACK HOME - 2NE1"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/dice?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NMIXX - DICE"
  },
  {
    url: "https://soundcloud.com/girlsday-sc/something?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "Girl's Day - Something"
  },
  
  {
    url: "https://soundcloud.com/kusumahusnina/f-x-hot-summer",
    answer: "F(X) - Hot Summer"
  },
  {
    url: "https://soundcloud.com/seasaltfishes/psycho-red-velvet?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Psycho - Red Velvet"
  },
  {
    url: "https://soundcloud.com/roya-jafarli/iu-winter-sleep?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "sirius - IU - Winter Sleep"
  },
  {
    url: "https://soundcloud.com/twice-57013/tt",
    answer: "Twice - TT"
  },
  {
    url: "https://soundcloud.com/everglow-sc/slay?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "EVERGLOW - SLAY"
  },
  {
    url: "https://soundcloud.com/iprincess15/sunmi-gashina?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Iprincess15 - SUNMI - GASHINA"
  },
  {
    url: "https://soundcloud.com/itzy-music/wannabe",
    answer: "ITZY - Wannabe"
  },
  {
    url: "https://soundcloud.com/seasaltfishes/power-up",
    answer: "Red Velvet - Power Up"
  },
  {
    url: "https://soundcloud.com/izone-music/violeta?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IZ*ONE - Violeta"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/sonar-breaker?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NMIXX - Soñar (Breaker)"
  },
  {
    url: "https://soundcloud.com/sunmi-sc/heart-burn?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "SUNMI - Heart Burn"
  },
  {
    url: "https://soundcloud.com/skyflay5/i-do-2-mp3?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "5C357 - (G)I-DLE - I DO"
  },
  {
    url: "https://soundcloud.com/newjeans-music/attention?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - Attention"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/kill-this-love?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - Kill This Love"
  },
  {
    url: "https://soundcloud.com/yuju-music/dalala?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "YUJU - DALALA"
  },
  {
    url: "https://soundcloud.com/mungikim/pristin-wee-woo",
    answer: "Pristin - Wee Woo"
  },
  {
    url: "https://soundcloud.com/twice-57013/feel-special?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - Feel Special"
  },
  {
    url: "https://soundcloud.com/karina-irgintya/gfriend-glass-bead",
    answer: "GFriend - Glass Bead"
  },
  {
    url: "https://soundcloud.com/huhyunjin/love-you-twice?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "HUH YUNJIN - love you twice"
  },
  {
    url: "https://soundcloud.com/twice-57013/what-is-love?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - What is Love?"
  },
  {
    url: "https://soundcloud.com/twice-57013/the-feels?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - The Feels"
  },
  {
    url: "https://soundcloud.com/gi-dle/latata?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - LATATA"
  },
  {
    url: "https://soundcloud.com/ph-ng-vy-35477112/im-so-sick",
    answer: "APink - I'm So Sick"
  },
  {
    url: "https://soundcloud.com/itzy-music/twenty?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - #Twenty"
  },
  {
    url: "https://soundcloud.com/study-with-sasha/bol4-some?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "lu_linni - bol4 - some"
  },
  {
    url: "https://soundcloud.com/sophia-jesa/hows-this-hyuna",
    answer: "Hyuna - How's This?"
  },
  {
    url: "https://soundcloud.com/nayeon-music/pop?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NAYEON - POP!"
  },
  {
    url: "https://soundcloud.com/2ne1official/i-am-the-best",
    answer: " 2NE1 - I Am The Best"
  },
  {
    url: "https://soundcloud.com/twice-57013/talk-that-talk?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "TWICE - Talk that Talk"
  },
  {
    url: "https://soundcloud.com/itzy-music/snowy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "ITZY - Snowy"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/sonar-breaker?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NMIXX - Soñar (Breaker)"
  },
  {
    url: "https://soundcloud.com/l2share128/taeyeon-weekend?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TAEYEON 태연 - TAEYEON (태연) - Weekend"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/dont-know-what-to-do?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - Don't Know What To Do"
  },
  {
    url: "https://soundcloud.com/itzy-music/not-shy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - Not Shy"
  },
  {
    url: "https://soundcloud.com/lightsum/honey-or-spice?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LIGHTSUM - Honey or Spice"
  },
  {
    url: "https://soundcloud.com/l2share52/izone-violeta",
    answer: "IZONE - Violeta"
  },
  {
    url: "https://soundcloud.com/gi-dle/nxde?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - Nxde"
  },
  {
    url: "https://soundcloud.com/aespaofficial/armageddon?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "aespa - Armageddon"
  },
  {
    url: "https://soundcloud.com/aylin-leandro-ferre/weki-meki-i-dont-like-your-girlfriend",
    answer: "Weki Meki - I Don't Like Your Girlfriend"
  },
  {
    url: "https://soundcloud.com/2nexx1/lonely?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "2NE1 - Lonely"
  },
  {
    url: "https://soundcloud.com/interscope/girls-generation-the-boys-8",
    answer: "Girl's Generation - The Boys"
  },
  {
    url: "https://soundcloud.com/chaelincl/tie-a-cherry?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CL - Tie a Cherry"
  },
  {
    url: "https://soundcloud.com/lisa96578/money?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LISA - MONEY"
  },
  {
    url: "https://soundcloud.com/babymonster1/batter-up?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BABYMONSTER - BATTER UP"
  },
  {
    url: "https://soundcloud.com/user-782826028/billlie-flippng-a-coin",
    answer: "Billlie - Flipping A Coin"
  },
  {
    url: "https://soundcloud.com/genrse/blackpink-whistle",
    answer: "Blackpink - Whistle"
  },
  {
    url: "https://soundcloud.com/l2share77/loona-butterfly",
    answer: "Loona - Butterfly"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/pretty-savage?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - Pretty Savage"
  },
  {
    url: "https://soundcloud.com/ive59257/either-way?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - Either Way"
  },
  {
    url: "https://soundcloud.com/yena57148/hate-rodrigo-feat-yuqi?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "YENA feat. YUQI - Hate Rodrigo (feat. YUQI)"
  },
  {
    url: "https://soundcloud.com/4minute/hot-issue",
    answer: "4Minute - Hot Issue"
  },
  {
    url: "https://soundcloud.com/moonbyulkiki27/taeyeon-to-x?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Moonbyulkiki27 𓂆 - TAEYEON 태연 - 'To. X'"
  },
  {
    url: "https://soundcloud.com/sunmi-sc/you-cant-sit-with-us?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "SUNMI - You can't sit with us"
  },
  {
    url: "https://soundcloud.com/aespaofficial/drama?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "aespa - Drama"
  },
  {
    url: "https://soundcloud.com/user-913229388/f-x-4-walls",
    answer: "F(X) - 4 Walls"
  },
  {
    url: "https://soundcloud.com/twice-57013/the-feels",
    answer: "Twice - The Feels"
  },
  {
    url: "https://soundcloud.com/ive59257/after-like?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - After LIKE"
  },
  {
    url: "https://soundcloud.com/le-sserafim/impurities?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - Impurities"
  },
  {
    url: "https://soundcloud.com/exo-baekhyun/miss-a-hush",
    answer: "Miss A - Hush"
  },
  {
    url: "https://soundcloud.com/miss-a-official/bad-girl-good-girl-kor",
    answer: "Miss A - Bad Girl Good Girl"
  },
  {
    url: "https://soundcloud.com/leehi-music/red-lipstick-feat-yoon-mi-rae?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LeeHi feat. YOON MI RAE - Red Lipstick (feat. YOON MI RAE)"
  },
  {
    url: "https://soundcloud.com/izone-music/secret-story-of-the-swan-1?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IZ*ONE - Secret Story of the Swan"
  },
  {
    url: "https://soundcloud.com/wahyu_putra/sistar-touch-my-body-at-wahyoe",
    answer: "Sistar - Touch My Body"
  },
  {
    url: "https://soundcloud.com/le-sserafim/fearless?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LE SSERAFIM - FEARLESS"
  },
  {
    url: "https://soundcloud.com/kekkun89/t-ara-roly-poly",
    answer: "T-ara - Roly Poly"
  },
  {
    url: "https://soundcloud.com/everglow-sc/dun-dun?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "EVERGLOW - DUN DUN"
  },
  {
    url: "https://soundcloud.com/twice-57013/happy-happy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - HAPPY HAPPY"
  },
  {
    url: "https://soundcloud.com/sophia-jesa/la-vie-en-rose-izone",
    answer: "IZONE - La Vie En Rose"
  },
  {
    url: "https://soundcloud.com/soojin-sc/agassy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "SOOJIN - AGASSY"
  },
  {
    url: "https://soundcloud.com/l2share59/exid-lady",
    answer: "EXID - Lady"
  },
  {
    url: "https://soundcloud.com/le-sserafim/1-800-hot-n-fun?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - 1-800-hot-n-fun"
  },
  {
    url: "https://soundcloud.com/itzy-music/sneakers?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - SNEAKERS"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/lovesick-girls?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - Lovesick Girls"
  },
  {
    url: "https://soundcloud.com/absinthe-330735846/twice-doughnut-1?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "z ? - doughnut by twice"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/shut-down?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - Shut Down"
  },
  {
    url: "https://soundcloud.com/fromis_9/miracle?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "fromis_9 - Miracle"
  },
  {
    url: "https://soundcloud.com/tokkitokkii/audio-tara-sugar-free?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "WhiteRabbit - T-ARA - Sugar Free"
  },
  {
    url: "https://soundcloud.com/nayeon-music/abcd-extended-version?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NAYEON - ABCD (Extended Version)"
  },
  {
    url: "https://soundcloud.com/meovv-music/meow?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "MEOVV - MEOW"
  },
  {
    url: "https://soundcloud.com/ernchern/like-a-cat-aoa",
    answer: "AOA - Like A Cat"
  },
  {
    url: "https://soundcloud.com/greenmusic-channel/bo-peep-bo-peep-t-ara",
    answer: "T-ara - Bo Peep Bo Peep"
  },
  {
    url: "https://soundcloud.com/jessi99517/cold-blooded?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Jessi - Cold Blooded"
  },
  {
    url: "https://soundcloud.com/genrse/blackpink-whistle?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Genna - BLACKPINK - WHISTLE"
  },
  {
    url: "https://soundcloud.com/gi-dle/track-3?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - Eyes Roll"
  },
  {
    url: "https://soundcloud.com/iew-v-828617851/red-velvet-russian-roulette?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet (레드벨벳) 러시안 룰렛(Russian Roulette)"
  },
  {
    url: "https://soundcloud.com/soffi-58611342/xg-left-right?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "XG - Left Right"
  },
  {
    url: "https://soundcloud.com/tuy-t-nhung-346654452/red-velvet-bad-boy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - Bad Boy"
  },
  {
    url: "https://soundcloud.com/le-sserafim/unforgiven-feat-nile-rodgers?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LE SSERAFIM, Nile Rodgers - UNFORGIVEN (feat. Nile Rodgers)"
  },
  {
    url: "https://soundcloud.com/genrse/blackpink-bombayah?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - BLACKPINK - BOOMBAYAH"
  },
  {
    url: "https://soundcloud.com/gi-dle/allergy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - Allergy"
  },
  {
    url: "https://soundcloud.com/hwasa-sc/chili?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "HWASA - Chili"
  },
  {
    url: "https://soundcloud.com/chungha_official/stay-tonight?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CHUNG HA - Stay Tonight"
  },
  {
    url: "https://soundcloud.com/twice-57013/tt?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - TT"
  },
  {
    url: "https://soundcloud.com/not_ur_sepai/girls-generation-party",
    answer: "Girl's Generation - Party"
  },
  {
    url: "https://soundcloud.com/twice-57013/set-me-free?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "TWICE - SET ME FREE"
  },
  {
    url: "https://soundcloud.com/stanlakpoplol/hwasa-twit?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "1theK () - Hwasa - TWIT"
  },
  {
    url: "https://soundcloud.com/aespaofficial/spicy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "aespa - Spicy"
  },
  {
    url: "https://soundcloud.com/blink-demon/stayc-beautiful-monster?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "STAYC - BEAUTIFUL MONSTER"
  },
  {
    url: "https://soundcloud.com/aespaofficial/illusion?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "aespa - Illusion"
  },
  {
    url: "https://soundcloud.com/stanaespa/viviz-bop-bop?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "viviz - bop bop!"
  },
  {
    url: "https://soundcloud.com/chic-el/wonder-girls-nobody-english-version",
    answer: "Wonder Girls - Nobody"
  },
  {
    url: "https://soundcloud.com/l2share128/wheein-water-color?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "L2Share♫128 - Whee In (휘인) - water color"
  },
  {
    url: "https://soundcloud.com/eohu/abracadabra-brown-eyed-girls?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Myrai Kotoba - Abracadabra - Brown Eyed Girls"
  },
  {
    url: "https://soundcloud.com/susan/vibrato-stellar?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "s - Vibrato (떨려요) - Stellar (스텔라)"
  },
  {
    url: "https://soundcloud.com/lisa96578/lalisa-1?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LISA - LALISA"
  },
  {
    url: "https://soundcloud.com/9flawless/blackpink-as-if-its-your-last",
    answer: "Blackpink - As If It's Your Last"
  },
  {
    url: "https://soundcloud.com/itzy-music/in-the-morning?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - In the morning"
  },
  {
    url: "https://soundcloud.com/twice-57013/yes-or-yes?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - YES or YES"
  },
  {
    url: "https://soundcloud.com/l2share106/red-velvet-irene-seulgi-monster?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - IRENE & SEULGI - Monster"
  },
  {
    url: "https://soundcloud.com/redvelvet-music/chill-kill?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - Chill Kill"
  },
  {
    url: "https://soundcloud.com/sunmi-sc/stranger?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "SUNMI - STRANGER"
  },
  {
    url: "https://soundcloud.com/sundays_ss/aespa-savage?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "aespa - Savage"
  },
  {
    url: "https://soundcloud.com/tm-950004586/orange-caramel-catallena",
    answer: "Orange Caramel - Catallena"
  },
  {
    url: "https://soundcloud.com/itzy-music/ringo?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - RINGO"
  },
  {
    url: "https://soundcloud.com/dirty-bts/mamamoo-gogobebe?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NohemiGuevara - Mamamoo-gogobebe"
  },
  {
    url: "https://soundcloud.com/ive59257/i-am?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - I AM"
  },
  {
    url: "https://soundcloud.com/96vnmlzgyip6/bubble?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "imanun - STAYC - Bubble"
  },
  {
    url: "https://soundcloud.com/gi-dle/queencard?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - Queencard"
  },
  {
    url: "https://soundcloud.com/chungha_official/chung-ha-sparkling?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CHUNG HA - Sparkling"
  },
  {
    url: "https://soundcloud.com/l2share131/fromis_9-we-go",
    answer: "fromis_9 - We Go"
  },
  {
    url: "https://soundcloud.com/twice-57013/signal?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - SIGNAL"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/love-me-like-this?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NMIXX - Love Me Like This"
  },
  {
    url: "https://soundcloud.com/h-ng-d-ng-qu-t/magic-girl-orange-caramel?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Hướng Dương Quỳ Tử - Magic Girl - Orange Caramel"
  },
  {
    url: "https://soundcloud.com/mina-anh-967372179/very-very-very-ioi",
    answer: "I.O.I - Very Very Very"
  },
  {
    url: "https://soundcloud.com/le-sserafim/crazier?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - Crazier"
  },
  {
    url: "https://soundcloud.com/twice-57013/alcohol-free?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - Alcohol-Free"
  },
  {
    url: "https://soundcloud.com/my-ng-c-867287818/girls-generation-forever-1",
    answer: "Girl's Generation - FOREVER 1"
  },
  {
    url: "https://soundcloud.com/ive59257/my-satisfaction?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "IVE - My Satisfaction"
  },
  {
    url: "https://soundcloud.com/somi_official/birthday-2",
    answer: "Somi - Birthday"
  },
  {
    url: "https://soundcloud.com/whdans860/rainbow-a?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "whdans860 - Rainbow - A"
  },
  {
    url: "https://soundcloud.com/twice-57013/i-cant-stop-me",
    answer: "Twice - I Can't Stop Me"
  },
  {
    url: "https://soundcloud.com/momoland-scmusic/ready-or-not?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "MOMOLAND - Ready Or Not"
  },
  {
    url: "https://soundcloud.com/user-459528629/mamamoo-starry-night?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TO_THE_A - MAMAMOO - Starry Night"
  },
  {
    url: "https://soundcloud.com/hwasa-sc/i-love-my-body?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "HWASA - I Love My Body"
  },
  {
    url: "https://soundcloud.com/svetlana-volkova-345109535/hwasa-i-m-a-b?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "cute чел - Hwasa-I m a B"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/how-you-like-that?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - How You Like That"
  },
  {
    url: "https://soundcloud.com/le-sserafim/perfect-night?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LE SSERAFIM - Perfect Night"
  },
  {
    url: "https://soundcloud.com/chungha_official/bicycle?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CHUNG HA - Bicycle"
  },
  {
    url: "https://soundcloud.com/everglow-sc/first?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "EVERGLOW - FIRST"
  },
  {
    url: "https://soundcloud.com/newjeans-music/cool-with-you?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - Cool With You"
  },
  {
    url: "https://soundcloud.com/l2share42/playing-with-fire?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - PLAYING WITH FIRE"
  },
  {
    url: "https://soundcloud.com/user-151356257/gfriend-mago?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "GFRIEND - GFRIEND - MAGO"
  },
  {
    url: "https://soundcloud.com/twice-57013/breakthrough?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - Breakthrough"
  },
  {
    url: "https://soundcloud.com/twice-57013/heart-shaker?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - Heart Shaker"
  },
  {
    url: "https://soundcloud.com/62442magic/dholic-chewy?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "45CM - D.Holic - Chewy"
  },
  {
    url: "https://soundcloud.com/itzy-music/icy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - ICY"
  },
  {
    url: "https://soundcloud.com/ive_official/ive-love-dive?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - LOVE DIVE"
  },
  {
    url: "https://soundcloud.com/twice-57013/dance-the-night-away?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - Dance The Night Away"
  },
  {
    url: "https://soundcloud.com/aespaofficial/better-things?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "aespa - Better Things"
  },
  {
    url: "https://soundcloud.com/biposhy-barua/girls-generation-forever1-song?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Kim Jisoo - Girls' Generation forever1 song"
  },
  {
    url: "https://soundcloud.com/aster-su/iu-strawberry-moon?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "보미 - IU _ strawberry moon"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/pink-venom?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - Pink Venom"
  },
  {
    url: "https://soundcloud.com/twice-57013/more-more?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - MORE & MORE"
  },
  {
    url: "https://soundcloud.com/gi-dle/track-2?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - I Want That"
  },
  {
    url: "https://soundcloud.com/hotaru-le-huynh/dal-shabet-joker-engromhan-picture-color-coded-hd?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Hotaru Le Huynh - Dal Shabet - Joker"
  },
  {
    url: "https://soundcloud.com/user-901873654/stayc-run2u?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "minasnovia - STAYC - RUN2U"
  },
  {
    url: "https://soundcloud.com/leehi-music/only?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LeeHi - ONLY"
  },
  {
    url: "https://soundcloud.com/itzy-music/weapon?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - Weapon"
  },
  {
    url: "https://soundcloud.com/mita-umitahrizah/step-back-got-the-beat?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "31음악 - Step Back - GOT The Beat"
  },
  {
    url: "https://soundcloud.com/nhh-b/stayc-stereotype?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Bảo bối - STAYC - STEREOTYPE"
  },
  {
    url: "https://soundcloud.com/seasaltfishes/red-velvet-rbb-really-bad?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - RBB (Really Bad Boy)"
  },
  {
    url: "https://soundcloud.com/itzy-music/mr-vampire?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "ITZY - Mr. Vampire"
  },
  {
    url: "https://soundcloud.com/twice-57013/more-more",
    answer: "Twice - More and More"
  },
  {
    url: "https://soundcloud.com/96vnmlzgyip6/seulgi-28-reasons?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "imanun - SEULGI-28 Reasons"
  },
  {
    url: "https://soundcloud.com/rororomeo/fx-nu-nu-abo",
    answer: "F(X) - Nu Abo"
  },
  {
    url: "https://soundcloud.com/l2share86/fanatics-sunday",
    answer: "Fanatics - Sunday"
  },
  {
    url: "https://soundcloud.com/gi-dle/tomboy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - TOMBOY"
  },
  {
    url: "https://soundcloud.com/zoloo-zoljargal-848585997/jessi-nunu-nana?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Schtimm - Jessi- Nunu Nana"
  },
  {
    url: "https://soundcloud.com/twice-57013/set-me-free?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - SET ME FREE"
  },
  {
    url: "https://soundcloud.com/elxi-aj/girls-day-ring-my-bell-jpn-ver?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "cheezy7 - Girl's Day - Ring My Bell (Japanese Ver.)"
  },
  {
    url: "https://soundcloud.com/gi-dle/my-bag?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - MY BAG"
  },
  {
    url: "https://soundcloud.com/l2share47/weki-meki-crush",
    answer: "Weki Meki - Crush"
  },
  {
    url: "https://soundcloud.com/twice-57013/likey?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - LIKEY"
  },
  {
    url: "https://soundcloud.com/marshall_line/kill-bill",
    answer: "Brown Eyed Girls - Kill Bill"
  },
  {
    url: "https://soundcloud.com/ive59257/ive-baddie?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - Baddie"
  },
  {
    url: "https://soundcloud.com/fromis_9/dm?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "fromis_9 - DM"
  },
  {
    url: "https://soundcloud.com/le-sserafim/the-hydra?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LE SSERAFIM - The Hydra"
  },
  {
    url: "https://soundcloud.com/newjeans-music/super-shy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - Super Shy"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/how-you-like-that",
    answer: "Blackpink - How You Like That"
  },
  {
    url: "https://soundcloud.com/sunmi-sc/24-hours?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "SUNMI - 24 Hours"
  },
  {
    url: "https://soundcloud.com/destinee-nsombe/wjsn-cosmic-girls-i-wish",
    answer: "WJSN - I Wish"
  },
  {
    url: "https://soundcloud.com/leechaeyeon-music/knock?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LEE CHAE YEON - KNOCK"
  },
  {
    url: "https://soundcloud.com/itzy-music/cheshire?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - Cheshire"
  },
  {
    url: "https://soundcloud.com/le-sserafim/chasing-lightning?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - Chasing Lightning"
  },
  {
    url: "https://soundcloud.com/yining-153721834/moon-byul-lunatic?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ʏɴ' ¨̮ - Moon Byul - LUNATIC"
  },
  {
    url: "https://soundcloud.com/newjeans-music/new-jeans?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - New Jeans"
  },
  {
    url: "https://soundcloud.com/le-sserafim/sour-grapes?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LE SSERAFIM - Sour Grapes"
  },
  {
    url: "https://soundcloud.com/boatbanana/red-velvet-dumb-dumb",
    answer: "Red Velvet - Dumb Dumb"
  },
  {
    url: "https://soundcloud.com/ohmygirl-music/coloring-book",
    answer: "Oh My Girl - Coloring Book"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/typa-girl?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - Typa Girl"
  },
  {
    url: "https://soundcloud.com/somi_official/what-you-waiting-for",
    answer: "Somi - What You Waiting For"
  },
  {
    url: "https://soundcloud.com/everglow-sc/la-di-da?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "EVERGLOW - LA DI DA"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/the-girls-blackpink-the-game?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - THE GIRLS (BLACKPINK THE GAME OST)"
  },
  {
    url: "https://soundcloud.com/aespaofficial/girls?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "aespa - Girls"
  },
  {
    url: "https://soundcloud.com/kep1er-music/wa-da-da?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Kep1er - WA DA DA"
  },
  {
    url: "https://soundcloud.com/twice-57013/hello?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - HELLO (NAYEON, MOMO, CHAEYOUNG)"
  },
  {
    url: "https://soundcloud.com/chungha_official/chung-ha-sparkling",
    answer: "Chung Ha - Sparkling"
  },
  {
    url: "https://soundcloud.com/sakura97fati/4minute-whatcha-doin-today?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: ".Lotus.Fati. - 4MINUTE - Whatcha Doin' Today"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/forever-young?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - Forever Young"
  },
  {
    url: "https://soundcloud.com/shadowjay44/mamamoo-illella?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JayTheShadow - MAMAMOO - ILLELLA"
  },
  {
    url: "https://soundcloud.com/kep1er-music/giddy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "Kep1er - Giddy"
  },
  {
    url: "https://soundcloud.com/izone-music/fiesta?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IZ*ONE - FIESTA"
  },
  {
    url: "https://soundcloud.com/ive_official/ive-take-it?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - Take It"
  },
  {
    url: "https://soundcloud.com/le-sserafim/antifragile?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LE SSERAFIM - ANTIFRAGILE"
  },
  {
    url: "https://soundcloud.com/etsuko-hime/kara-lupin?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Etsuko Hime - KARA - LUPIN(루팡)"
  },
  {
    url: "https://soundcloud.com/ive59257/kitsch?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - Kitsch"
  },
  {
    url: "https://soundcloud.com/emi-oneill/after-school-weeekly?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Weeekly - after school - weeekly"
  },
  {
    url: "https://soundcloud.com/twice-57013/like-ooh-ahh?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - Like OOH-AHH"
  },
  {
    url: "https://soundcloud.com/l2share106/sunmi-pporappippam",
    answer: "Sunmi - pporappippam"
  },
  {
    url: "https://soundcloud.com/jini-music/cmon-feat-amine?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JINI - C'mon (feat. Aminé)"
  },
  {
    url: "https://soundcloud.com/twice-57013/talk-that-talk?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - Talk that Talk"
  },
  {
    url: "https://soundcloud.com/genn-sis/apink-dillema?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "genn - apink - dilemma"
  },
  {
    url: "https://soundcloud.com/everglow-sc/pirate?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "EVERGLOW - Pirate"
  },
  {
    url: "https://soundcloud.com/mcnlight/hyuna-babe",
    answer: "Hyuna - Babe"
  },
  {
    url: "https://soundcloud.com/tracimp/honey-solar?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "T R A C I M P - HONEY - SOLAR"
  },
  {
    url: "https://soundcloud.com/l2share47/loona-favorite",
    answer: "Loona - favOriTe"
  },
  {
    url: "https://soundcloud.com/chungha_official/chung-ha-killing-me?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CHUNG HA - Killing Me"
  },
  {
    url: "https://soundcloud.com/wonder-girls/rewind?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "Wonder Girls - Rewind"
  },
  {
    url: "https://soundcloud.com/sundays_ss/red-velvet-feel-my-rhythm?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - Feel My Rhythm"
  },
  {
    url: "https://soundcloud.com/vcreamy/kara-mr?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "KARA - Mr."
  },
  {
    url: "https://soundcloud.com/twice-57013/scientist?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - SCIENTIST"
  },
  {
    url: "https://soundcloud.com/kris-tin-677841441/jessi-what-type-of-x?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "_yoonraries_ - Jessi - What Type Of X"
  },
  {
    url: "https://soundcloud.com/misamo-music/marshmallow?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "MISAMO - Marshmallow"
  },
  {
    url: "https://soundcloud.com/eohu/abracadabra-brown-eyed-girls",
    answer: "Brown Eyed Girls - Abracadabra"
  },
  {
    url: "https://soundcloud.com/rosemusic65184/on-the-ground?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ROSÉ - On The Ground"
  },
  {
    url: "https://soundcloud.com/hoxl1e5ylvbp/miss-a-bad-girl-good-girl",
    answer: "Miss A - Bad Girl Good Girl"
  },
  {
    url: "https://soundcloud.com/aespaofficial/dreams-come-true?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "aespa - Dreams Come True"
  },
  {
    url: "https://soundcloud.com/wfxb0pd3jqyx/brave-girls-rollin",
    answer: "Brave Girls - Rollin'"
  },
  {
    url: "https://soundcloud.com/516024456homie/i-am-shampoo?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BIBI - BIBI-I AM SHAMPOO"
  },
  {
    url: "https://soundcloud.com/itzy-music/swipe?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - SWIPE"
  },
  {
    url: "https://soundcloud.com/l2share140/ive-eleven",
    answer: "IVE - Eleven"
  },
  {
    url: "https://soundcloud.com/l2share78/iu-bbibbi?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "아이유 (IU) - IU - BBIBBI"
  },
  {
    url: "https://soundcloud.com/li-sumiko/lapillus-hit-ya?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "cherry - lapillus - hit ya"
  },
  {
    url: "https://soundcloud.com/le-sserafim/pierrot?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - Pierrot"
  },
  {
    url: "https://soundcloud.com/chungha_official/chung-ha-gotta-go?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CHUNG HA - Gotta Go"
  },
  {
    url: "https://soundcloud.com/stanaespa/wjsn-unnatural?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "WJSN - Unnatural"
  },
  {
    url: "https://soundcloud.com/newjeans-music/hype-boy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - Hype Boy"
  },
  {
    url: "https://soundcloud.com/gi-dle/lion?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - LION"
  },
  {
    url: "https://soundcloud.com/twice-57013/rewind?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - REWIND"
  },
  {
    url: "https://soundcloud.com/jaytheshadow33/got-the-beat-stamp-on-it?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "GOT the beat - Got The Beat - Stamp On It"
  },
  {
    url: "https://soundcloud.com/rvred-velvet/bye-bye?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "red velvet - bye bye"
  },
  {
    url: "https://soundcloud.com/le-sserafim/ash",
    answer: "LE SSERAFIM - Ash"
  },
  {
    url: "https://soundcloud.com/twice-57013/cheer-up?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - CHEER UP"
  },
  {
    url: "https://soundcloud.com/ohmygirl-music/nonstop",
    answer: "Oh My Girl - Nonstop"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/ice-cream?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK, Selena Gomez - Ice Cream (with Selena Gomez)"
  },
  {
    url: "https://soundcloud.com/itzy-music/loco?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - LOCO"
  },
  {
    url: "https://soundcloud.com/user746128857/aoa-heart-attack",
    answer: "AOA - Heart Attack"
  },
  {
    url: "https://soundcloud.com/l2share49/red-velvet-zimzalabim?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - Zimzalabim"
  },
  {
    url: "https://soundcloud.com/chungha_official/chung-ha-roller-coaster?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CHUNG HA - Roller Coaster"
  },
  {
    url: "https://soundcloud.com/ive59257/ive-off-the-record?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - Off The Record"
  },
  {
    url: "https://soundcloud.com/gi-dle/hann-alone?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - HANN (Alone)"
  },
  {
    url: "https://soundcloud.com/zii-kaka/twice-scientist?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "Zii Kaka Music - TWICE - SCIENTIST"
  },
  {
    url: "https://soundcloud.com/le-sserafim/hot",
    answer: "LE SSERAFIM - HOT"
  },
  {
    url: "https://soundcloud.com/niziu-music/heartris?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NiziU - HEARTRIS"
  },
  {
    url: "https://soundcloud.com/le-sserafim/crazy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "LE SSERAFIM - CRAZY"
  },
  {
    url: "https://soundcloud.com/crystal7t/crazy-4minute",
    answer: "4Minute - Crazy"
  },
  {
    url: "https://soundcloud.com/fiftyfifty99499/cupid?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "FIFTY FIFTY - Cupid"
  },
  {
    url: "https://soundcloud.com/reveluv-stuff/red-velvet-peek-a-boo?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - Peek-A-Boo"
  },
  {
    url: "https://soundcloud.com/dani-martins-neves/girls-generation-i-got-a-boy",
    answer: "Girl's Generation - I Got A Boy"
  },
  {
    url: "https://soundcloud.com/bibi-scmusic/bibi-vengeance?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BIBI - 나쁜년"
  },
  {
    url: "https://soundcloud.com/l2share77/loona-butterfly?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "L2Share♫77 - LOONA - Butterfly"
  },
  {
    url: "https://soundcloud.com/z_u_z_u_n_i/stayc-asap",
    answer: "StayC - ASAP"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/roller-coaster?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NMIXX - Roller Coaster"
  },
  {
    url: "https://soundcloud.com/jisoo-scmusic/flower?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JISOO - FLOWER"
  },
  {
    url: "https://soundcloud.com/newjeans-music/ditto?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - Ditto"
  },
  {
    url: "https://soundcloud.com/twice-57013/cry-for-me?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - CRY FOR ME"
  },
  {
    url: "https://soundcloud.com/l2share44/fromis_9-love-bomb",
    answer: "fromis_9 - Love Bomb"
  },
  {
    url: "https://soundcloud.com/twice-57013/i-cant-stop-me?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - I CAN'T STOP ME"
  },
  {
    url: "https://soundcloud.com/user-405539708/jeon-somi-o-xoxo-sped-up?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "༘⋆🫀₊˚ෆ - jeon somi • xoxo (sped up)"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/o-o?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NMIXX - O.O"
  },
  {
    url: "https://soundcloud.com/everglow-sc/adios?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "EVERGLOW - Adios"
  },
  {
    url: "https://soundcloud.com/user-674947085/hq-secret-im-in-love-official-audio?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Sebas Mares - [HQ] 시크릿(SECRET) - I'm In Love (Official Audio)"
  },
  {
    url: "https://soundcloud.com/josedestroy/exid-updown",
    answer: "EXID - Up & Down"
  },
  {
    url: "https://soundcloud.com/junmin501/t-ara-i-go-crazy-because-of-you?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "junmin501 - T-ara - I Go Crazy Because of You"
  },
  {
    url: "https://soundcloud.com/triples46067/girls-never-die?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "tripleS - Girls Never Die"
  },
  {
    url: "https://soundcloud.com/rodsepp/we-like",
    answer: "Pristin - We Like"
  },
  {
    url: "https://soundcloud.com/xiz-thic/ioi-whatta-man-good-man",
    answer: "I.O.I - Whatta Man"
  },
  {
    url: "https://soundcloud.com/dreamaboutthvk95/stayc-so-bad?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "dreamaboutthv - STAYC- SO BAD"
  },
  {
    url: "https://soundcloud.com/izone-music/la-vie-en-rose?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IZ*ONE - La Vie en Rose"
  },
  {
    url: "https://soundcloud.com/le-sserafim/come-over",
    answer: "LE SSERAFIM - Come Over"
  },
  {
    url: "https://soundcloud.com/aespaofficial/black-mamba?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "aespa - Black Mamba"
  },
  {
    url: "https://soundcloud.com/gi-dle/senorita?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - Senorita"
  },
  {
    url: "https://soundcloud.com/twice-57013/fancy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - FANCY"
  },
  {
    url: "https://soundcloud.com/newjeans-music/cookie?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - Cookie"
  },
  {
    url: "https://soundcloud.com/twice-57013/moonlight-sunrise?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - MOONLIGHT SUNRISE"
  },
  {
    url: "https://soundcloud.com/ive_official/ive-eleven?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "IVE - ELEVEN"
  },
  {
    url: "https://soundcloud.com/joyuri-music/taxi?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JO YURI - TAXI"
  },
  {
    url: "https://soundcloud.com/newjeans-music/zero?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - Zero"
  },
  {
    url: "https://soundcloud.com/xoxoamira23/stellar-marionette?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "AmiraS_23 - Stellar - Marionette"
  },
  {
    url: "https://soundcloud.com/shwi_wie/cherry-bullet-love-so-sweet",
    answer: "Cherry Bullet - Love So Sweet"
  },
  {
    url: "https://soundcloud.com/joyuri-music/glassy?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JO YURI - GLASSY"
  },
  {
    url: "https://soundcloud.com/l2share95/red-velvet-queendom",
    answer: "Red Velvet - Queendom"
  },
  {
    url: "https://soundcloud.com/faiz-zarul/dia-will-you-go-out-with-me-1",
    answer: "DIA - Will You Go Out With Me"
  },
  {
    url: "https://soundcloud.com/yena57148/smiley-feat-bibi?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "YENA feat. BIBI - SMILEY (feat. BIBI)"
  },
  {
    url: "https://soundcloud.com/twice-57013/alcohol-free",
    answer: "Twice - Alcohol Free"
  },
  {
    url: "https://soundcloud.com/skkzyx/pristin-v-get-it",
    answer: "Pristin V - Get It"
  },
  {
    url: "https://soundcloud.com/twice-57013/cheer-up",
    answer: "Twice - Cheer Up"
  },
  {
    url: "https://soundcloud.com/reveluv-stuff/red-velvet-red-flavor?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - Red Flavor"
  },
  {
    url: "https://soundcloud.com/jisoo-scmusic/all-eyes-on-me?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JISOO - All Eyes On Me"
  },
  {
    url: "https://soundcloud.com/l2kpop12/maria_hwasa?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Hwasa - Maria"
  },
  {
    url: "https://soundcloud.com/moon-dust-156576908/hyo-deep?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "HYO - Deep"
  },
  {
    url: "https://soundcloud.com/quan-mai-anh/lovelyz-obliviate",
    answer: "LovelyZ - Obliviate"
  },
  {
    url: "https://soundcloud.com/chungha_official/play-feat-changmo?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CHUNG HA feat. CHANGMO - PLAY (feat. CHANGMO)"
  },
  {
    url: "https://soundcloud.com/jihyo-music/killin-me-good?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JIHYO - Killin′ Me Good"
  },
  {
    url: "https://soundcloud.com/sadeofficial/kiss-of-love?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Sade - Kiss of Life"
  },
  {
    url: "https://soundcloud.com/aijon-disband/viviz-loveade?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Revv - Viviz - LOVEADE"
  },
  {
    url: "https://soundcloud.com/faby-queen/hyuna-red",
    answer: "Hyuna - Red"
  },
  {
    url: "https://soundcloud.com/chungha_official/chung-ha-snapping?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "CHUNG HA - Snapping"
  },
  {
    url: "https://soundcloud.com/user-945980444/mamamoo-aya?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Mamamoo - Mamamoo - AYA"
  },
  {
    url: "https://soundcloud.com/jennie-music/solo?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JENNIE - SOLO"
  },
  {
    url: "https://soundcloud.com/le-sserafim/eve-psyche-the-bluebeards-wife?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "LE SSERAFIM - Eve, Psyche & The Bluebeard’s wife"
  },
  {
    url: "https://soundcloud.com/user-574951661/stayc-teddy-bear?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "mb - STAYC - Teddy Bear"
  },
  {
    url: "https://soundcloud.com/fromis_9/be-with-you?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "fromis_9 - Be With You"
  },
  {
    url: "https://soundcloud.com/katseye-music/touch?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "KATSEYE - Touch"
  },
  {
    url: "https://soundcloud.com/afiqashura/t-ara-so-crazy-korean-ver?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "AfiqAshura - T-ARA - So Crazy (Korean ver.)"
  },
  {
    url: "https://soundcloud.com/user-306544001/blueming?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "아이유 - IU ~ Blueming"
  },
  {
    url: "https://soundcloud.com/seasaltfishes/power-up?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Red Velvet - Power Up"
  },
  {
    url: "https://soundcloud.com/jamie48593/pity-party?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JAMIE - Pity Party"
  },
  {
    url: "https://soundcloud.com/ella-marie/t-ara-like-the-first-time?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "Ella Marie 12 - T-ara - Like The First Time"
  },
  {
    url: "https://soundcloud.com/everglow-sc/bon-bon-chocolat?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "EVERGLOW - Bon Bon Chocolat"
  },
  {
    url: "https://soundcloud.com/itsvee/short-hair-aoa",
    answer: "AOA - Short Hair"
  },
  {
    url: "https://soundcloud.com/newjeans-music/get-up?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - Get Up"
  },
  {
    url: "https://soundcloud.com/angel-j3nnie-457590955/y2mate-is-jeon-somi-xoxo-sped?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "_o._nii - jeon somi - xoxo"
  },
  {
    url: "https://soundcloud.com/vdtpin/9muses-hurt-locker?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "PIN - 9muses - 다쳐(Hurt Locker)"
  },
  {
    url: "https://soundcloud.com/newjeans-music/omg?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - OMG"
  },
  {
    url: "https://soundcloud.com/handa-vempire-chanjuan/wonder-girls-tell-me-2012-korean-version",
    answer: "Wonder Girls - Tell Me"
  },
  {
    url: "https://soundcloud.com/huhyunjin/i-doll?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "HUH YUNJIN - I ≠ DOLL"
  },
  {
    url: "https://soundcloud.com/xikanist/fromis_9-glass-shoes",
    answer: "fromis_9 - Glass Shoes"
  },
  {
    url: "https://soundcloud.com/l2share131/aespa-next-level-1",
    answer: "aespa - Next Level"
  },
  {
    url: "https://soundcloud.com/lukas-moskalis-293120113/stellar-sting?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "스텔라 - 찔려 Stellar Sting"
  },
  {
    url: "https://soundcloud.com/emi-oneill/after-school-weeekly",
    answer: "Weeekly - After School"
  },
  {
    url: "https://soundcloud.com/aijon-disband/mave-pandora?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "Revv - MAVE - PANDORA"
  },
  {
    url: "https://soundcloud.com/itzy-music/dalla-dalla?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - DALLA DALLA"
  },
  {
    url: "https://soundcloud.com/ive59257/ive-accendio?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "IVE - Accendio"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/roller-coaster?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NMIXX - Roller Coaster"
  },
  {
    url: "https://soundcloud.com/twice-57013/kura-kura?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "TWICE - Kura Kura"
  },
  {
    url: "https://soundcloud.com/user-339323148/stayc-stereotype",
    answer: "StayC - Stereotype"
  },
  {
    url: "https://soundcloud.com/twice-57013/fancy",
    answer: "Twice - Fancy"
  },
  {
    url: "https://soundcloud.com/l2share128/taeyeon-weekend",
    answer: "Taeyeon - Weekend"
  },
  {
    url: "https://soundcloud.com/nmixx-scmusic/dice?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
    answer: "NMIXX - DICE"
  },
  {
    url: "https://soundcloud.com/nicollette-prince/girls-day-something?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "$K - Girls day: something"
  },
  {
    url: "https://soundcloud.com/itzy-music/cake?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "ITZY - CAKE"
  },
  {
    url: "https://soundcloud.com/jennie-music/you-me?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "JENNIE - You & Me"
  },
  {
    url: "https://soundcloud.com/newjeans-music/eta?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "NewJeans - ETA"
  },
  {
    url: "https://soundcloud.com/l2share55/t-ara-whats-my-name?in=user-255046189/sets/2nd-generation-kpop-gg",
    answer: "티아라 (T-ARA) - 티아라 (T-ARA) - 내 이름은 (What's My Name?)"
  },
  {
    url: "https://soundcloud.com/gi-dle/oh-my-god?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "(G)I-DLE - Oh my god"
  },
  {
    url: "https://soundcloud.com/blackpinkofficial/ddu-du-ddu-du?in=niuro/sets/best-of-kpop-girl-groups",
    answer: "BLACKPINK - DDU-DU DDU-DU"
  },
  {
    url: "https://soundcloud.com/le-sserafim/so-cynical-badum",
    answer: "LE SSERAFIM - So Cynical (Badum)"
  },
  {
    url: "https://soundcloud.com/kep1er-music/shooting-star",
    answer: "Kep1er - Shooting Star"
  },
  {
    url: "https://soundcloud.com/kep1er-music/tipi-tap",
    answer: "Kep1er - TIPI-TAP"
  },
  {
    url: "https://soundcloud.com/kep1er-music/up",
    answer: "Kep1er - Up!"
  },
  {
    url: "https://soundcloud.com/fromis_9/supersonic",
    answer: "fromis_9 - Supersonic"
  },
  {
    url: "https://soundcloud.com/fromis_9/menow",
    answer: "fromis_9 - #menow"
  },
  {
    url: "https://soundcloud.com/illit-music/cherish-my-love",
    answer: "ILLIT - Cherish (My Love)"
  },
  {
    url: "https://soundcloud.com/illit-music/lucky-girl-syndrome",
    answer: "ILLIT - Lucky Girl Syndrome"
  },
  {
    url: "https://soundcloud.com/illit-music/tick-tack",
    answer: "ILLIT - Tick-Tack"
  },
  {
    url: "https://soundcloud.com/illit-music/magnetic",
    answer: "ILLIT - Magnetic"
  },
  {
    url: "https://soundcloud.com/illit-music/midnight-fiction",
    answer: "ILLIT - Midnight Fiction"
  },
  {
    url: "https://soundcloud.com/illit-music/midnight-fiction",
    answer: "ILLIT-Midnight Fiction"
  }

];