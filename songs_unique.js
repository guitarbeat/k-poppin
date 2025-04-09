// because of autocomplete bug
// if the answer starts with a number, need to precede it with a space (" ")
// otherwise it won't be available

let songs = [

{
"url": "https://soundcloud.com/kiiikiii-music/debut-song",
"answer": "KiiiKiii - DEBUT SONG"
},
{
"url": "https://soundcloud.com/kiiikiii-music/one-off",
"answer": "KiiiKiii - 한 개뿐인 (ONE OFF)"
},
{
"url": "https://soundcloud.com/kiiikiii-music/there-they-go",
"answer": "KiiiKiii - THERE THEY GO"
},
{
"url": "https://soundcloud.com/kiiikiii-music/btg",
"answer": "KiiiKiii - BTG"
},
{
"url": "https://soundcloud.com/kiiikiii-music/groundwork",
"answer": "KiiiKiii - GROUNDWORK"
},
{
"url": "https://soundcloud.com/aespaofficial/spicy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa - Spicy"
},
{
"url": "https://soundcloud.com/ohhhhyeahhhh/im-gonna-be-a-star?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "트와이스 - I'm Gonna Be A Star"
},
{
"url": "https://soundcloud.com/aespaofficial/drama?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa - Drama"
},
{
"url": "https://soundcloud.com/aespaofficial/girls?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa - Girls"
},
{
"url": "https://soundcloud.com/aespaofficial/black-mamba?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa - Black Mamba"
},
{
"url": "https://soundcloud.com/gi-dle/super-lady?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "(G)I-DLE - Super Lady"
},
{
"url": "https://soundcloud.com/l2share106/hwasa-maria-hwa-sa?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "hwasa-maria - 화사 (HwaSa) - Maria (마리아)"
},
{
"url": "https://soundcloud.com/le-sserafim/antifragile?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - ANTIFRAGILE"
},
{
"url": "https://soundcloud.com/clc-official/hobgoblin?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "CLC - Hobgoblin"
},
{
"url": "https://soundcloud.com/user-188414680/savage-aespa?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Piwonssaessak - SAVAGE | AESPA"
},
{
"url": "https://soundcloud.com/moonbyulkiki22/jessi-gum?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "RIIZE (라이즈) - 제시(Jessi) - Gum(껌)"
},
{
"url": "https://soundcloud.com/le-sserafim/unforgiven-feat-nile-rodgers?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM, Nile Rodgers - UNFORGIVEN (feat. Nile Rodgers)"
},
{
"url": "https://soundcloud.com/frizzy-28638240/xg-grl-gvng?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "prod. raf0 - XG · GRL GVNG"
},
{
"url": "https://soundcloud.com/itzy-music/untouchable?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - UNTOUCHABLE"
},
{
"url": "https://soundcloud.com/clc-official/like-it?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "CLC - Like It"
},
{
"url": "https://soundcloud.com/gi-dle/tomboy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "(G)I-DLE - TOMBOY"
},
{
"url": "https://soundcloud.com/clc-official/no?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "CLC - No"
},
{
"url": "https://soundcloud.com/itzy-music/born-to-be?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - BORN TO BE"
},
{
"url": "https://soundcloud.com/itzy-music/in-the-morning?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - In the morning"
},
{
"url": "https://soundcloud.com/l2share95/everglow-dun-dun?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "everglow-dun-dun - EVERGLOW - DUN DUN"
},
{
"url": "https://soundcloud.com/le-sserafim/eve-psyche-the-bluebeards-wife?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - Eve, Psyche & The Bluebeard’s wife"
},
{
"url": "https://soundcloud.com/itzy-music/sorry-not-sorry?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - Sorry Not Sorry"
},
{
"url": "https://soundcloud.com/itzy-music/kill-shot?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - Kill Shot"
},
{
"url": "https://soundcloud.com/guhipminju/swz-a0xtvkn6wwjo?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "국힙원탑 김민주 - GODS - NewJeans (뉴진스), League of Legends (2023 리그 오브 레전드 월드 챔피언십 주제곡)"
},
{
"url": "https://soundcloud.com/thecreati0nist/cl-hello-bitches?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "theCreati0nist - CL (이채린) - Hello Bitches"
},
{
"url": "https://soundcloud.com/ive59257/ive-heya?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "IVE - 해야 (HEYA)"
},
{
"url": "https://soundcloud.com/itzy-music/loco?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - LOCO"
},
{
"url": "https://soundcloud.com/gi-dle/my-bag?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "(G)I-DLE - MY BAG"
},
{
"url": "https://soundcloud.com/bibi-scmusic/bibi-vengeance?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "BIBI - 나쁜년"
},
{
"url": "https://soundcloud.com/itzy-music/cheshire?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - Cheshire"
},
{
"url": "https://soundcloud.com/karainz-p/blackpink-pink-venom-1?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "𝐊 𝐀 𝐑 𝐀 𝐈 𝐍 𝐙 - BLACKPINK - Pink Venom"
},
{
"url": "https://soundcloud.com/ive59257/ive-baddie?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "IVE - Baddie"
},
{
"url": "https://soundcloud.com/ive59257/i-am?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "IVE - I AM"
},
{
"url": "https://soundcloud.com/maria-eduarda-andrade-da-silva-174609320/im-not-cool-hyuna?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Duda Silva - I'm Not Cool- HyunA"
},
{
"url": "https://soundcloud.com/user-510284300/lisa-rockstar-1?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Mia - LISA - ROCKSTAR"
},
{
"url": "https://soundcloud.com/misamo-music/do-not-touch?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "MISAMO - Do not touch"
},
{
"url": "https://soundcloud.com/itzy-music/cake?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - CAKE"
},
{
"url": "https://soundcloud.com/gi-dle/queencard?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "(G)I-DLE - Queencard"
},
{
"url": "https://soundcloud.com/gi-dle/nxde?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "(G)I-DLE - Nxde"
},
{
"url": "https://soundcloud.com/lee-seungri-751943596/blackpink-boombayah?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ゆめこちゃん〜🎀 - BLACKPINK - BOOMBAYAH (붐바야)"
},
{
"url": "https://soundcloud.com/le-sserafim/fearless?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - FEARLESS"
},
{
"url": "https://soundcloud.com/dearwish9/f-x-electric-shock-1?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "DEARWISH9 - f(x) – Electric Shock"
},
{
"url": "https://soundcloud.com/4minute/hot-issue?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "4Minute - Hot Issue"
},
{
"url": "https://soundcloud.com/4minute/crazy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "4Minute - Crazy"
},
{
"url": "https://soundcloud.com/user-652664872/bboom-bboom-momoland?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "shrooms - Bboom Bboom ~ Momoland"
},
{
"url": "https://soundcloud.com/laodeofficial/hyuna-lip-hip?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LAODÉ - HyunA - Lip & Hip"
},
{
"url": "https://soundcloud.com/mita-umitahrizah/pandora-mave?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "31음악 - PANDORA - MAVE"
},
{
"url": "https://soundcloud.com/bossrainn/xg-xgalx-woke-up?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Bass |R - XG (XGALX) - WOKE UP"
},
{
"url": "https://soundcloud.com/aespaofficial/supernova?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa - Supernova"
},
{
"url": "https://soundcloud.com/phi-v-h-181890575/mamamoo-hip-color-coded-eng?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Phi Vũ Hà - MAMAMOO (마마무) - HIP (Color Coded Eng/Rom/Han/가사)"
},
{
"url": "https://soundcloud.com/aespa-music/die-trying?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa & TOKiMONSTA - Die Trying"
},
{
"url": "https://soundcloud.com/milana-kudakova/badvillain?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "BADVILLAIN - BADVILLAIN"
},
{
"url": "https://soundcloud.com/user-545527839/nayeon-abcd-2?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "𝚃𝚊𝚖𝚖𝚒:) - Nayeon -ABCD"
},
{
"url": "https://soundcloud.com/leseraafims/babymonster-sheesh-demo-rap-1?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "amorphine - BABYMONSTER - ‘SHEESH’ (+DEMO RAP PART)"
},
{
"url": "https://soundcloud.com/user-565240779/heya-ive?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "asya 🎵 - heya - ive"
},
{
"url": "https://soundcloud.com/kep1er-music/wa-da-da?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Kep1er - WA DA DA"
},
{
"url": "https://soundcloud.com/everglow-sc/la-di-da?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "EVERGLOW - LA DI DA"
},
{
"url": "https://soundcloud.com/yena57148/wicked-love?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "YENA - WICKED LOVE"
},
{
"url": "https://soundcloud.com/zpmpiz5d3tto/stayc-so-bad?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Kiki - STAYC (스테이씨) 'SO BAD'"
},
{
"url": "https://soundcloud.com/tinker-ben/stayc-like-this?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "zinna - STAYC 'LIKE THIS'"
},
{
"url": "https://soundcloud.com/user-565240779/cheeky-icy-thang-stayc?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "asya 🎵 - cheeky icy thang - STAYC"
},
{
"url": "https://soundcloud.com/chaeist/1-thing-stayc?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "✿ - 1 Thing - STAYC (스테이씨)"
},
{
"url": "https://soundcloud.com/user-901873654/stayc-run2u?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "minasnovia - STAYC - RUN2U"
},
{
"url": "https://soundcloud.com/nhh-b/stayc-stereotype?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Bảo bối - STAYC - STEREOTYPE"
},
{
"url": "https://soundcloud.com/user-386256050/stayc-fancy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "zy - STAYC-fancy"
},
{
"url": "https://soundcloud.com/gi-dle/klaxon?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "(G)I-DLE - Klaxon"
},
{
"url": "https://soundcloud.com/gi-dle/wife?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "(G)I-DLE - Wife"
},
{
"url": "https://soundcloud.com/gi-dle/hwaa?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "(G)I-DLE - HWAA"
},
{
"url": "https://soundcloud.com/newjeans-music/how-sweet?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - How Sweet"
},
{
"url": "https://soundcloud.com/newjeans-music/supernatural?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Supernatural"
},
{
"url": "https://soundcloud.com/newjeans-music/right-now?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Right Now"
},
{
"url": "https://soundcloud.com/newjeans-music/bubble-gum?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Bubble Gum"
},
{
"url": "https://soundcloud.com/newjeans-music/new-jeans?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - New Jeans"
},
{
"url": "https://soundcloud.com/newjeans-music/super-shy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Super Shy"
},
{
"url": "https://soundcloud.com/newjeans-music/cool-with-you?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Cool With You"
},
{
"url": "https://soundcloud.com/newjeans-music/get-up?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Get Up"
},
{
"url": "https://soundcloud.com/newjeans-music/asap?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - ASAP"
},
{
"url": "https://soundcloud.com/newjeans-music/attention?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Attention"
},
{
"url": "https://soundcloud.com/newjeans-music/hype-boy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Hype Boy"
},
{
"url": "https://soundcloud.com/newjeans-music/cookie?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Cookie"
},
{
"url": "https://soundcloud.com/newjeans-music/ditto?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NewJeans - Ditto"
},
{
"url": "https://soundcloud.com/vufgv6b2jtdj/twice-alcohol-free?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "수진 - TWICE - Alcohol-Free"
},
{
"url": "https://soundcloud.com/le-sserafim/swan-song?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - Swan Song"
},
{
"url": "https://soundcloud.com/le-sserafim/perfect-night?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - Perfect Night"
},
{
"url": "https://soundcloud.com/le-sserafim/sour-grapes?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - Sour Grapes"
},
{
"url": "https://soundcloud.com/thanh-le-110000981/ma-boy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Sistar19 - SISTAR19 (씨스타19) - Ma Boy"
},
{
"url": "https://soundcloud.com/saebyeokk/illit-magnetic?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "𝗺𝗼𝗼𝗻𝗶𝗲𝗲🧸 - ILLIT - MAGNETIC"
},
{
"url": "https://soundcloud.com/lam-le-479022895/10-minutes?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Lee Hyori - 10 Minutes - Lee Hyori (이효리)"
},
{
"url": "https://soundcloud.com/itzy-music/not-shy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - Not Shy"
},
{
"url": "https://soundcloud.com/itsmekey/girls-generation-snsd-gee?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Girls' Generation - Girls' Generation SNSD - Gee"
},
{
"url": "https://soundcloud.com/blackvaderofficial/twice-like-ohh-ahh-ooh-ahh-blackvs-remix-1?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "𝔹𝕃𝔸ℂ𝕂𝕍𝔸𝔻𝔼ℝ - TWICE - Like OHH - AHH (OOH - AHH하게) (BLACKVS Remix)"
},
{
"url": "https://soundcloud.com/official_vcha/only-one?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "VCHA - Only One"
},
{
"url": "https://soundcloud.com/official_vcha/y-o-universe?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "VCHA - Y.O.Universe"
},
{
"url": "https://soundcloud.com/official_vcha/girls-of-the-year?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "VCHA - Girls of the Year"
},
{
"url": "https://soundcloud.com/yrlocation/nobody-knows-kiss-of-life-born?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "send me your location. - Nobody Knows - KISS OF LIFE (키스오브라이프) [Born to be XX]"
},
{
"url": "https://soundcloud.com/twice-57013/set-me-free?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "TWICE - SET ME FREE"
},
{
"url": "https://soundcloud.com/twice-57013/talk-that-talk?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "TWICE - Talk that Talk"
},
{
"url": "https://soundcloud.com/katseye-music/touch?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "KATSEYE - Touch"
},
{
"url": "https://soundcloud.com/wonder-girls/rewind?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Wonder Girls - Rewind"
},
{
"url": "https://soundcloud.com/absinthe-330735846/twice-doughnut-1?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "z ? - doughnut by twice"
},
{
"url": "https://soundcloud.com/sunmi-sc/24-hours?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "SUNMI - 24 Hours"
},
{
"url": "https://soundcloud.com/niziu-music/heartris?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NiziU - HEARTRIS"
},
{
"url": "https://soundcloud.com/girlsday-sc/something?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Girl's Day - Something"
},
{
"url": "https://soundcloud.com/nmixx-scmusic/roller-coaster?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NMIXX - Roller Coaster"
},
{
"url": "https://soundcloud.com/aespaofficial/better-things?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa - Better Things"
},
{
"url": "https://soundcloud.com/le-sserafim/impurities?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - Impurities"
},
{
"url": "https://soundcloud.com/aespaofficial/illusion?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa - Illusion"
},
{
"url": "https://soundcloud.com/zii-kaka/twice-scientist?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Zii Kaka Music - TWICE - SCIENTIST"
},
{
"url": "https://soundcloud.com/ive59257/my-satisfaction?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "IVE - My Satisfaction"
},
{
"url": "https://soundcloud.com/itzy-music/snowy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - Snowy"
},
{
"url": "https://soundcloud.com/fromis_9/be-with-you?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "fromis_9 - Be With You"
},
{
"url": "https://soundcloud.com/fromis_9/glass-shoes-from-fromis_9-pre?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "fromis_9 - Glass Shoes (From fromis_9 Pre-Debut)"
},
{
"url": "https://soundcloud.com/fromis_9/miracle?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "fromis_9 - Miracle"
},
{
"url": "https://soundcloud.com/nmixx-scmusic/sonar-breaker?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NMIXX - Soñar (Breaker)"
},
{
"url": "https://soundcloud.com/shxhrol-amy/playingwithfire?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "BLACKPINK - 불장난 - BLΛƆKPIИK (블랙핑크)"
},
{
"url": "https://soundcloud.com/user-55808555/blackpink?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "BLACKPINK - 마지막처럼 - BLACKPINK"
},
{
"url": "https://soundcloud.com/lightsum/honey-or-spice?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LIGHTSUM - Honey or Spice"
},
{
"url": "https://soundcloud.com/le-sserafim/crazy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - CRAZY"
},
{
"url": "https://soundcloud.com/le-sserafim/pierrot?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - Pierrot"
},
{
"url": "https://soundcloud.com/le-sserafim/1-800-hot-n-fun?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - 1-800-hot-n-fun"
},
{
"url": "https://soundcloud.com/le-sserafim/chasing-lightning?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - Chasing Lightning"
},
{
"url": "https://soundcloud.com/le-sserafim/crazier?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "LE SSERAFIM - Crazier"
},
{
"url": "https://soundcloud.com/aespaofficial/armageddon?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "aespa - Armageddon"
},
{
"url": "https://soundcloud.com/ive59257/ive-accendio?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "IVE - Accendio"
},
{
"url": "https://soundcloud.com/nayeon-music/abcd-extended-version?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NAYEON - ABCD (Extended Version)"
},
{
"url": "https://soundcloud.com/meovv-music/meow?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "MEOVV - MEOW"
},
{
"url": "https://soundcloud.com/triples46067/girls-never-die?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "tripleS - Girls Never Die"
},
{
"url": "https://soundcloud.com/nmixx-scmusic/dice?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "NMIXX - DICE"
},
{
"url": "https://soundcloud.com/itzy-music/mr-vampire?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "ITZY - Mr. Vampire"
},
{
"url": "https://soundcloud.com/kep1er-music/giddy?in=sarah-vue-960537035/sets/my-gg-kpop-playlist",
"answer": "Kep1er - Giddy"
},
{
"url": "https://soundcloud.com/eohu/abracadabra-brown-eyed-girls?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "Myrai Kotoba - Abracadabra - Brown Eyed Girls"
},
{
"url": "https://soundcloud.com/etsuko-hime/kara-lupin?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "Etsuko Hime - KARA - LUPIN(루팡)"
},
{
"url": "https://soundcloud.com/xoxoamira23/stellar-marionette?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "AmiraS_23 - Stellar - Marionette"
},
{
"url": "https://soundcloud.com/whdans860/rainbow-a?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "whdans860 - Rainbow - A"
},
{
"url": "https://soundcloud.com/susan/vibrato-stellar?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "s - Vibrato (떨려요) - Stellar (스텔라)"
},
{
"url": "https://soundcloud.com/tokkitokkii/audio-tara-sugar-free?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "WhiteRabbit - T-ARA - Sugar Free"
},
{
"url": "https://soundcloud.com/afiqashura/t-ara-so-crazy-korean-ver?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "AfiqAshura - T-ARA - So Crazy (Korean ver.)"
},
{
"url": "https://soundcloud.com/ella-marie/t-ara-like-the-first-time?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "Ella Marie 12 - T-ara - Like The First Time"
},
{
"url": "https://soundcloud.com/junmin501/t-ara-i-go-crazy-because-of-you?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "junmin501 - T-ara - I Go Crazy Because of You"
},
{
"url": "https://soundcloud.com/vcreamy/kara-mr?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "lmDaawn - KARA - Mr."
},
{
"url": "https://soundcloud.com/vdtpin/9muses-hurt-locker?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "PIN - 9muses - 다쳐(Hurt Locker)"
},
{
"url": "https://soundcloud.com/62442magic/dholic-chewy?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "45CM - D.Holic - Chewy"
},
{
"url": "https://soundcloud.com/elxi-aj/girls-day-ring-my-bell-jpn-ver?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "cheezy7 - Girl's Day - Ring My Bell (Japanese Ver.)"
},
{
"url": "https://soundcloud.com/l2share55/t-ara-whats-my-name?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "티아라 (T-ARA) - 티아라 (T-ARA) - 내 이름은 (What's My Name?)"
},
{
"url": "https://soundcloud.com/lukas-moskalis-293120113/stellar-sting?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "스텔라 - 찔려 Stellar Sting"
},
{
"url": "https://soundcloud.com/nicollette-prince/girls-day-something?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "$K - Girls day: something"
},
{
"url": "https://soundcloud.com/hotaru-le-huynh/dal-shabet-joker-engromhan-picture-color-coded-hd?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "Hotaru Le Huynh - Dal Shabet - Joker"
},
{
"url": "https://soundcloud.com/sakura97fati/4minute-whatcha-doin-today?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": ".Lotus.Fati. - 4MINUTE - Whatcha Doin' Today"
},
{
"url": "https://soundcloud.com/user-674947085/hq-secret-im-in-love-official-audio?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "Sebas Mares - [HQ] 시크릿(SECRET) - I'm In Love (Official Audio)"
},
{
"url": "https://soundcloud.com/h-ng-d-ng-qu-t/magic-girl-orange-caramel?in=user-255046189/sets/2nd-generation-kpop-gg",
"answer": "Hướng Dương Quỳ Tử - Magic Girl - Orange Caramel"
},
]
