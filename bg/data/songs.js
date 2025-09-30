// Boy Group K-Pop Heardle Songs Database
// because of autocomplete bug
// if the answer starts with a number, need to precede it with a space (" ")
// otherwise it won't be available

let songs = [
  {
    url: "https://soundcloud.com/bts-music/dynamite",
    answer: "BTS - Dynamite"
  },
  {
    url: "https://soundcloud.com/bts-music/butter",
    answer: "BTS - Butter"
  },
  {
    url: "https://soundcloud.com/bts-music/boy-with-luv",
    answer: "BTS - Boy With Luv"
  },
  {
    url: "https://soundcloud.com/bts-music/dna",
    answer: "BTS - DNA"
  },
  {
    url: "https://soundcloud.com/bts-music/fake-love",
    answer: "BTS - Fake Love"
  },
  {
    url: "https://soundcloud.com/bts-music/idol",
    answer: "BTS - IDOL"
  },
  {
    url: "https://soundcloud.com/bts-music/mic-drop",
    answer: "BTS - MIC Drop"
  },
  {
    url: "https://soundcloud.com/bts-music/spring-day",
    answer: "BTS - Spring Day"
  },
  {
    url: "https://soundcloud.com/bts-music/blood-sweat-tears",
    answer: "BTS - Blood Sweat & Tears"
  },
  {
    url: "https://soundcloud.com/bts-music/fire",
    answer: "BTS - Fire"
  },
  {
    url: "https://soundcloud.com/exo-music/ko-ko-bop",
    answer: "EXO - Ko Ko Bop"
  },
  {
    url: "https://soundcloud.com/exo-music/tempo",
    answer: "EXO - Tempo"
  },
  {
    url: "https://soundcloud.com/exo-music/love-shot",
    answer: "EXO - Love Shot"
  },
  {
    url: "https://soundcloud.com/exo-music/monster",
    answer: "EXO - Monster"
  },
  {
    url: "https://soundcloud.com/exo-music/call-me-baby",
    answer: "EXO - Call Me Baby"
  },
  {
    url: "https://soundcloud.com/exo-music/growl",
    answer: "EXO - Growl"
  },
  {
    url: "https://soundcloud.com/exo-music/overdose",
    answer: "EXO - Overdose"
  },
  {
    url: "https://soundcloud.com/exo-music/wolf",
    answer: "EXO - Wolf"
  },
  {
    url: "https://soundcloud.com/exo-music/mama",
    answer: "EXO - MAMA"
  },
  {
    url: "https://soundcloud.com/exo-music/history",
    answer: "EXO - History"
  },
  {
    url: "https://soundcloud.com/seventeen-music/dont-wanna-cry",
    answer: "SEVENTEEN - Don't Wanna Cry"
  },
  {
    url: "https://soundcloud.com/seventeen-music/very-nice",
    answer: "SEVENTEEN - Very Nice"
  },
  {
    url: "https://soundcloud.com/seventeen-music/clap",
    answer: "SEVENTEEN - Clap"
  },
  {
    url: "https://soundcloud.com/seventeen-music/boom-boom",
    answer: "SEVENTEEN - Boom Boom"
  },
  {
    url: "https://soundcloud.com/seventeen-music/left-right",
    answer: "SEVENTEEN - Left & Right"
  },
  {
    url: "https://soundcloud.com/seventeen-music/home-run",
    answer: "SEVENTEEN - Home Run"
  },
  {
    url: "https://soundcloud.com/seventeen-music/rocket",
    answer: "SEVENTEEN - Rocket"
  },
  {
    url: "https://soundcloud.com/seventeen-music/thanks",
    answer: "SEVENTEEN - Thanks"
  },
  {
    url: "https://soundcloud.com/seventeen-music/oh-my",
    answer: "SEVENTEEN - Oh My!"
  },
  {
    url: "https://soundcloud.com/seventeen-music/ready-to-love",
    answer: "SEVENTEEN - Ready to love"
  },
  {
    url: "https://soundcloud.com/straykids-music/gods-menu",
    answer: "Stray Kids - God's Menu"
  },
  {
    url: "https://soundcloud.com/straykids-music/back-door",
    answer: "Stray Kids - Back Door"
  },
  {
    url: "https://soundcloud.com/straykids-music/thunderous",
    answer: "Stray Kids - Thunderous"
  },
  {
    url: "https://soundcloud.com/straykids-music/miroh",
    answer: "Stray Kids - Miroh"
  },
  {
    url: "https://soundcloud.com/straykids-music/side-effects",
    answer: "Stray Kids - Side Effects"
  },
  {
    url: "https://soundcloud.com/straykids-music/hellevator",
    answer: "Stray Kids - Hellevator"
  },
  {
    url: "https://soundcloud.com/straykids-music/district-9",
    answer: "Stray Kids - District 9"
  },
  {
    url: "https://soundcloud.com/straykids-music/my-pace",
    answer: "Stray Kids - My Pace"
  },
  {
    url: "https://soundcloud.com/straykids-music/levanter",
    answer: "Stray Kids - Levanter"
  },
  {
    url: "https://soundcloud.com/straykids-music/chronosaurus",
    answer: "Stray Kids - Chronosaurus"
  },
  {
    url: "https://soundcloud.com/nct-music/kick-it",
    answer: "NCT 127 - Kick It"
  },
  {
    url: "https://soundcloud.com/nct-music/regular",
    answer: "NCT 127 - Regular"
  },
  {
    url: "https://soundcloud.com/nct-music/simon-says",
    answer: "NCT 127 - Simon Says"
  },
  {
    url: "https://soundcloud.com/nct-music/limitless",
    answer: "NCT 127 - Limitless"
  },
  {
    url: "https://soundcloud.com/nct-music/fire-truck",
    answer: "NCT 127 - Fire Truck"
  },
  {
    url: "https://soundcloud.com/nct-music/chewing-gum",
    answer: "NCT DREAM - Chewing Gum"
  },
  {
    url: "https://soundcloud.com/nct-music/we-go-up",
    answer: "NCT DREAM - We Go Up"
  },
  {
    url: "https://soundcloud.com/nct-music/boom",
    answer: "NCT DREAM - Boom"
  },
  {
    url: "https://soundcloud.com/nct-music/ridin",
    answer: "NCT DREAM - Ridin'"
  },
  {
    url: "https://soundcloud.com/nct-music/hot-sauce",
    answer: "NCT DREAM - Hot Sauce"
  },
  {
    url: "https://soundcloud.com/got7-music/just-right",
    answer: "GOT7 - Just Right"
  },
  {
    url: "https://soundcloud.com/got7-music/hard-carry",
    answer: "GOT7 - Hard Carry"
  },
  {
    url: "https://soundcloud.com/got7-music/never-ever",
    answer: "GOT7 - Never Ever"
  },
  {
    url: "https://soundcloud.com/got7-music/lullaby",
    answer: "GOT7 - Lullaby"
  },
  {
    url: "https://soundcloud.com/got7-music/you-are",
    answer: "GOT7 - You Are"
  },
  {
    url: "https://soundcloud.com/got7-music/look",
    answer: "GOT7 - Look"
  },
  {
    url: "https://soundcloud.com/got7-music/if-you-do",
    answer: "GOT7 - If You Do"
  },
  {
    url: "https://soundcloud.com/got7-music/fly",
    answer: "GOT7 - Fly"
  },
  {
    url: "https://soundcloud.com/got7-music/stop-stop-it",
    answer: "GOT7 - Stop Stop It"
  },
  {
    url: "https://soundcloud.com/got7-music/confession-song",
    answer: "GOT7 - Confession Song"
  },
  {
    url: "https://soundcloud.com/monstax-music/hero",
    answer: "MONSTA X - Hero"
  },
  {
    url: "https://soundcloud.com/monstax-music/all-in",
    answer: "MONSTA X - All In"
  },
  {
    url: "https://soundcloud.com/monstax-music/dramarama",
    answer: "MONSTA X - Dramarama"
  },
  {
    url: "https://soundcloud.com/monstax-music/jealousy",
    answer: "MONSTA X - Jealousy"
  },
  {
    url: "https://soundcloud.com/monstax-music/shoot-out",
    answer: "MONSTA X - Shoot Out"
  },
  {
    url: "https://soundcloud.com/monstax-music/fighter",
    answer: "MONSTA X - Fighter"
  },
  {
    url: "https://soundcloud.com/monstax-music/beautiful",
    answer: "MONSTA X - Beautiful"
  },
  {
    url: "https://soundcloud.com/monstax-music/trespass",
    answer: "MONSTA X - Trespass"
  },
  {
    url: "https://soundcloud.com/monstax-music/rush",
    answer: "MONSTA X - Rush"
  },
  {
    url: "https://soundcloud.com/monstax-music/rotate",
    answer: "MONSTA X - Rotate"
  },
  {
    url: "https://soundcloud.com/winner-music/really-really",
    answer: "WINNER - Really Really"
  },
  {
    url: "https://soundcloud.com/winner-music/empty",
    answer: "WINNER - Empty"
  },
  {
    url: "https://soundcloud.com/winner-music/color-ring",
    answer: "WINNER - Color Ring"
  },
  {
    url: "https://soundcloud.com/winner-music/ah-yeah",
    answer: "WINNER - Ah Yeah"
  },
  {
    url: "https://soundcloud.com/winner-music/millions",
    answer: "WINNER - Millions"
  },
  {
    url: "https://soundcloud.com/winner-music/la-la",
    answer: "WINNER - La La"
  },
  {
    url: "https://soundcloud.com/winner-music/so-so",
    answer: "WINNER - So So"
  },
  {
    url: "https://soundcloud.com/winner-music/remember",
    answer: "WINNER - Remember"
  },
  {
    url: "https://soundcloud.com/winner-music/air",
    answer: "WINNER - Air"
  },
  {
    url: "https://soundcloud.com/winner-music/ssong",
    answer: "WINNER - Ssong"
  },
  {
    url: "https://soundcloud.com/ikon-music/love-scenario",
    answer: "iKON - Love Scenario"
  },
  {
    url: "https://soundcloud.com/ikon-music/rhythm-ta",
    answer: "iKON - Rhythm Ta"
  },
  {
    url: "https://soundcloud.com/ikon-music/my-type",
    answer: "iKON - My Type"
  },
  {
    url: "https://soundcloud.com/ikon-music/apology",
    answer: "iKON - Apology"
  },
  {
    url: "https://soundcloud.com/ikon-music/airplane",
    answer: "iKON - Airplane"
  },
  {
    url: "https://soundcloud.com/ikon-music/killing-me",
    answer: "iKON - Killing Me"
  },
  {
    url: "https://soundcloud.com/ikon-music/goodbye-road",
    answer: "iKON - Goodbye Road"
  },
  {
    url: "https://soundcloud.com/ikon-music/why-why-why",
    answer: "iKON - Why Why Why"
  },
  {
    url: "https://soundcloud.com/ikon-music/name",
    answer: "iKON - Name"
  },
  {
    url: "https://soundcloud.com/ikon-music/but-you",
    answer: "iKON - But You"
  },
  {
    url: "https://soundcloud.com/blockb-music/very-good",
    answer: "Block B - Very Good"
  },
  {
    url: "https://soundcloud.com/blockb-music/nillili-mambo",
    answer: "Block B - Nillili Mambo"
  },
  {
    url: "https://soundcloud.com/blockb-music/zero-for-conduct",
    answer: "Block B - Zero for Conduct"
  },
  {
    url: "https://soundcloud.com/blockb-music/toy",
    answer: "Block B - Toy"
  },
  {
    url: "https://soundcloud.com/blockb-music/be-the-light",
    answer: "Block B - Be The Light"
  },
  {
    url: "https://soundcloud.com/blockb-music/several-occasions",
    answer: "Block B - Several Occasions"
  },
  {
    url: "https://soundcloud.com/blockb-music/mental-breaker",
    answer: "Block B - Mental Breaker"
  },
  {
    url: "https://soundcloud.com/blockb-music/action",
    answer: "Block B - Action"
  },
  {
    url: "https://soundcloud.com/blockb-music/where-are-you",
    answer: "Block B - Where Are You"
  },
  {
    url: "https://soundcloud.com/blockb-music/one-way",
    answer: "Block B - One Way"
  },
  {
    url: "https://soundcloud.com/bigbang-music/bang-bang-bang",
    answer: "BIGBANG - Bang Bang Bang"
  },
  {
    url: "https://soundcloud.com/bigbang-music/fantastic-baby",
    answer: "BIGBANG - Fantastic Baby"
  },
  {
    url: "https://soundcloud.com/bigbang-music/lies",
    answer: "BIGBANG - Lies"
  },
  {
    url: "https://soundcloud.com/bigbang-music/haruharu",
    answer: "BIGBANG - Haru Haru"
  },
  {
    url: "https://soundcloud.com/bigbang-music/last-farewell",
    answer: "BIGBANG - Last Farewell"
  },
  {
    url: "https://soundcloud.com/bigbang-music/we-belong-together",
    answer: "BIGBANG - We Belong Together"
  },
  {
    url: "https://soundcloud.com/bigbang-music/sunset-glow",
    answer: "BIGBANG - Sunset Glow"
  },
  {
    url: "https://soundcloud.com/bigbang-music/blue",
    answer: "BIGBANG - Blue"
  },
  {
    url: "https://soundcloud.com/bigbang-music/bad-boy",
    answer: "BIGBANG - Bad Boy"
  },
  {
    url: "https://soundcloud.com/bigbang-music/love-song",
    answer: "BIGBANG - Love Song"
  },
  {
    url: "https://soundcloud.com/superjunior-music/sorry-sorry",
    answer: "Super Junior - Sorry Sorry"
  },
  {
    url: "https://soundcloud.com/superjunior-music/mr-simple",
    answer: "Super Junior - Mr. Simple"
  },
  {
    url: "https://soundcloud.com/superjunior-music/bonamana",
    answer: "Super Junior - Bonamana"
  },
  {
    url: "https://soundcloud.com/superjunior-music/its-you",
    answer: "Super Junior - It's You"
  },
  {
    url: "https://soundcloud.com/superjunior-music/u",
    answer: "Super Junior - U"
  },
  {
    url: "https://soundcloud.com/superjunior-music/dont-don",
    answer: "Super Junior - Don't Don"
  },
  {
    url: "https://soundcloud.com/superjunior-music/miracle",
    answer: "Super Junior - Miracle"
  },
  {
    url: "https://soundcloud.com/superjunior-music/beautiful",
    answer: "Super Junior - Beautiful"
  },
  {
    url: "https://soundcloud.com/superjunior-music/way-to-go",
    answer: "Super Junior - Way to Go"
  },
  {
    url: "https://soundcloud.com/superjunior-music/rockstar",
    answer: "Super Junior - Rockstar"
  },
  {
    url: "https://soundcloud.com/shinee-music/ring-ding-dong",
    answer: "SHINee - Ring Ding Dong"
  },
  {
    url: "https://soundcloud.com/shinee-music/lucifer",
    answer: "SHINee - Lucifer"
  },
  {
    url: "https://soundcloud.com/shinee-music/sherlock",
    answer: "SHINee - Sherlock"
  },
  {
    url: "https://soundcloud.com/shinee-music/replay",
    answer: "SHINee - Replay"
  },
  {
    url: "https://soundcloud.com/shinee-music/juliette",
    answer: "SHINee - Juliette"
  },
  {
    url: "https://soundcloud.com/shinee-music/hello",
    answer: "SHINee - Hello"
  },
  {
    url: "https://soundcloud.com/shinee-music/amigo",
    answer: "SHINee - Amigo"
  },
  {
    url: "https://soundcloud.com/shinee-music/stand-by-me",
    answer: "SHINee - Stand By Me"
  },
  {
    url: "https://soundcloud.com/shinee-music/jojo",
    answer: "SHINee - JoJo"
  },
  {
    url: "https://soundcloud.com/shinee-music/why-so-serious",
    answer: "SHINee - Why So Serious?"
  },
  {
    url: "https://soundcloud.com/tvxq-music/mirotic",
    answer: "TVXQ - Mirotic"
  },
  {
    url: "https://soundcloud.com/tvxq-music/rising-sun",
    answer: "TVXQ - Rising Sun"
  },
  {
    url: "https://soundcloud.com/tvxq-music/hug",
    answer: "TVXQ - Hug"
  },
  {
    url: "https://soundcloud.com/tvxq-music/balloons",
    answer: "TVXQ - Balloons"
  },
  {
    url: "https://soundcloud.com/tvxq-music/tonight",
    answer: "TVXQ - Tonight"
  },
  {
    url: "https://soundcloud.com/tvxq-music/keep-your-head-down",
    answer: "TVXQ - Keep Your Head Down"
  },
  {
    url: "https://soundcloud.com/tvxq-music/catch-me",
    answer: "TVXQ - Catch Me"
  },
  {
    url: "https://soundcloud.com/tvxq-music/something",
    answer: "TVXQ - Something"
  },
  {
    url: "https://soundcloud.com/tvxq-music/spellbound",
    answer: "TVXQ - Spellbound"
  },
  {
    url: "https://soundcloud.com/tvxq-music/truth",
    answer: "TVXQ - Truth"
  },
  {
    url: "https://soundcloud.com/2pm-music/hands-up",
    answer: "2PM - Hands Up"
  },
  {
    url: "https://soundcloud.com/2pm-music/again-again",
    answer: "2PM - Again & Again"
  },
  {
    url: "https://soundcloud.com/2pm-music/heartbeat",
    answer: "2PM - Heartbeat"
  },
  {
    url: "https://soundcloud.com/2pm-music/without-u",
    answer: "2PM - Without U"
  },
  {
    url: "https://soundcloud.com/2pm-music/10-out-of-10",
    answer: "2PM - 10 Out of 10"
  },
  {
    url: "https://soundcloud.com/2pm-music/only-you",
    answer: "2PM - Only You"
  },
  {
    url: "https://soundcloud.com/2pm-music/my-house",
    answer: "2PM - My House"
  },
  {
    url: "https://soundcloud.com/2pm-music/gentleman",
    answer: "2PM - Gentleman"
  },
  {
    url: "https://soundcloud.com/2pm-music/comeback-when-you-hear-this-song",
    answer: "2PM - Comeback When You Hear This Song"
  },
  {
    url: "https://soundcloud.com/2pm-music/put-your-hands-up",
    answer: "2PM - Put Your Hands Up"
  },
  {
    url: "https://soundcloud.com/2am-music/cant-say-i-love-you",
    answer: "2AM - Can't Say I Love You"
  },
  {
    url: "https://soundcloud.com/2am-music/dead-of-night",
    answer: "2AM - Dead of Night"
  },
  {
    url: "https://soundcloud.com/2am-music/this-song",
    answer: "2AM - This Song"
  },
  {
    url: "https://soundcloud.com/2am-music/one-spring-day",
    answer: "2AM - One Spring Day"
  },
  {
    url: "https://soundcloud.com/2am-music/confession",
    answer: "2AM - Confession"
  },
  {
    url: "https://soundcloud.com/2am-music/i-was-wrong",
    answer: "2AM - I Was Wrong"
  },
  {
    url: "https://soundcloud.com/2am-music/even-if-i-die-i-cant-send-you-away",
    answer: "2AM - Even If I Die I Can't Send You Away"
  },
  {
    url: "https://soundcloud.com/2am-music/phone",
    answer: "2AM - Phone"
  },
  {
    url: "https://soundcloud.com/2am-music/you-wouldnt-answer-my-calls",
    answer: "2AM - You Wouldn't Answer My Calls"
  },
  {
    url: "https://soundcloud.com/2am-music/i-love-you",
    answer: "2AM - I Love You"
  },
  {
    url: "https://soundcloud.com/beast-music/fiction",
    answer: "BEAST - Fiction"
  },
  {
    url: "https://soundcloud.com/beast-music/beautiful",
    answer: "BEAST - Beautiful"
  },
  {
    url: "https://soundcloud.com/beast-music/breath",
    answer: "BEAST - Breath"
  },
  {
    url: "https://soundcloud.com/beast-music/shock",
    answer: "BEAST - Shock"
  },
  {
    url: "https://soundcloud.com/beast-music/bad-girl",
    answer: "BEAST - Bad Girl"
  },
  {
    url: "https://soundcloud.com/beast-music/mystery",
    answer: "BEAST - Mystery"
  },
  {
    url: "https://soundcloud.com/beast-music/on-rainy-days",
    answer: "BEAST - On Rainy Days"
  },
  {
    url: "https://soundcloud.com/beast-music/lightless",
    answer: "BEAST - Lightless"
  },
  {
    url: "https://soundcloud.com/beast-music/12-30",
    answer: "BEAST - 12:30"
  },
  {
    url: "https://soundcloud.com/beast-music/ribbon",
    answer: "BEAST - Ribbon"
  },
  {
    url: "https://soundcloud.com/infinite-music/be-mine",
    answer: "INFINITE - Be Mine"
  },
  {
    url: "https://soundcloud.com/infinite-music/paradise",
    answer: "INFINITE - Paradise"
  },
  {
    url: "https://soundcloud.com/infinite-music/before-the-dawn",
    answer: "INFINITE - Before the Dawn"
  },
  {
    url: "https://soundcloud.com/infinite-music/nothing-to-overcome",
    answer: "INFINITE - Nothing to Overcome"
  },
  {
    url: "https://soundcloud.com/infinite-music/come-back-again",
    answer: "INFINITE - Come Back Again"
  },
  {
    url: "https://soundcloud.com/infinite-music/shes-back",
    answer: "INFINITE - She's Back"
  },
  {
    url: "https://soundcloud.com/infinite-music/bt-d",
    answer: "INFINITE - BTD"
  },
  {
    url: "https://soundcloud.com/infinite-music/beautiful",
    answer: "INFINITE - Beautiful"
  },
  {
    url: "https://soundcloud.com/infinite-music/only-tears",
    answer: "INFINITE - Only Tears"
  },
  {
    url: "https://soundcloud.com/infinite-music/voice-of-my-heart",
    answer: "INFINITE - Voice of My Heart"
  },
  {
    url: "https://soundcloud.com/teentop-music/crazy",
    answer: "TEEN TOP - Crazy"
  },
  {
    url: "https://soundcloud.com/teentop-music/no-more-perfume-on-you",
    answer: "TEEN TOP - No More Perfume On You"
  },
  {
    url: "https://soundcloud.com/teentop-music/sup-luv",
    answer: "TEEN TOP - Sup Luv"
  },
  {
    url: "https://soundcloud.com/teentop-music/miss-right",
    answer: "TEEN TOP - Miss Right"
  },
  {
    url: "https://soundcloud.com/teentop-music/rocking",
    answer: "TEEN TOP - Rocking"
  },
  {
    url: "https://soundcloud.com/teentop-music/to-you",
    answer: "TEEN TOP - To You"
  },
  {
    url: "https://soundcloud.com/teentop-music/ah-ah",
    answer: "TEEN TOP - Ah-Ah"
  },
  {
    url: "https://soundcloud.com/teentop-music/clap",
    answer: "TEEN TOP - Clap"
  },
  {
    url: "https://soundcloud.com/teentop-music/i-wanna-love",
    answer: "TEEN TOP - I Wanna Love"
  },
  {
    url: "https://soundcloud.com/teentop-music/beautiful-girl",
    answer: "TEEN TOP - Beautiful Girl"
  },
  {
    url: "https://soundcloud.com/cnblue-music/i-m-sorry",
    answer: "CNBLUE - I'm Sorry"
  },
  {
    url: "https://soundcloud.com/cnblue-music/lonely",
    answer: "CNBLUE - Lonely"
  },
  {
    url: "https://soundcloud.com/cnblue-music/youre-so-fine",
    answer: "CNBLUE - You're So Fine"
  },
  {
    url: "https://soundcloud.com/cnblue-music/can-t-stop",
    answer: "CNBLUE - Can't Stop"
  },
  {
    url: "https://soundcloud.com/cnblue-music/cinderella",
    answer: "CNBLUE - Cinderella"
  },
  {
    url: "https://soundcloud.com/cnblue-music/you-are-so-beautiful",
    answer: "CNBLUE - You Are So Beautiful"
  },
  {
    url: "https://soundcloud.com/cnblue-music/young-forever",
    answer: "CNBLUE - Young Forever"
  },
  {
    url: "https://soundcloud.com/cnblue-music/radio",
    answer: "CNBLUE - Radio"
  },
  {
    url: "https://soundcloud.com/cnblue-music/coffee-shop",
    answer: "CNBLUE - Coffee Shop"
  },
  {
    url: "https://soundcloud.com/cnblue-music/be-my-girl",
    answer: "CNBLUE - Be My Girl"
  },
  {
    url: "https://soundcloud.com/ftisland-music/love-love-love",
    answer: "FTISLAND - Love Love Love"
  },
  {
    url: "https://soundcloud.com/ftisland-music/after-love",
    answer: "FTISLAND - After Love"
  },
  {
    url: "https://soundcloud.com/ftisland-music/hello-hello",
    answer: "FTISLAND - Hello Hello"
  },
  {
    url: "https://soundcloud.com/ftisland-music/severely",
    answer: "FTISLAND - Severely"
  },
  {
    url: "https://soundcloud.com/ftisland-music/you-dont-know-who-i-am",
    answer: "FTISLAND - You Don't Know Who I Am"
  },
  {
    url: "https://soundcloud.com/ftisland-music/beautiful-journey",
    answer: "FTISLAND - Beautiful Journey"
  },
  {
    url: "https://soundcloud.com/ftisland-music/paper-plane",
    answer: "FTISLAND - Paper Plane"
  },
  {
    url: "https://soundcloud.com/ftisland-music/always-be-mine",
    answer: "FTISLAND - Always Be Mine"
  },
  {
    url: "https://soundcloud.com/ftisland-music/paradise",
    answer: "FTISLAND - Paradise"
  },
  {
    url: "https://soundcloud.com/ftisland-music/take-me-now",
    answer: "FTISLAND - Take Me Now"
  },
  {
    url: "https://soundcloud.com/ss501-music/love-like-this",
    answer: "SS501 - Love Like This"
  },
  {
    url: "https://soundcloud.com/ss501-music/ur-man",
    answer: "SS501 - U R Man"
  },
  {
    url: "https://soundcloud.com/ss501-music/find",
    answer: "SS501 - Find"
  },
  {
    url: "https://soundcloud.com/ss501-music/never-again",
    answer: "SS501 - Never Again"
  },
  {
    url: "https://soundcloud.com/ss501-music/deja-vu",
    answer: "SS501 - Deja Vu"
  },
  {
    url: "https://soundcloud.com/ss501-music/song-calling-for-you",
    answer: "SS501 - Song Calling For You"
  },
  {
    url: "https://soundcloud.com/ss501-music/obsess",
    answer: "SS501 - Obsess"
  },
  {
    url: "https://soundcloud.com/ss501-music/4-chance",
    answer: "SS501 - 4 Chance"
  },
  {
    url: "https://soundcloud.com/ss501-music/wanted",
    answer: "SS501 - Wanted"
  },
  {
    url: "https://soundcloud.com/ss501-music/let-me-be-the-one",
    answer: "SS501 - Let Me Be The One"
  },
  {
    url: "https://soundcloud.com/2ne1-music/i-am-the-best",
    answer: "2NE1 - I Am The Best"
  },
  {
    url: "https://soundcloud.com/2ne1-music/fire",
    answer: "2NE1 - Fire"
  },
  {
    url: "https://soundcloud.com/2ne1-music/come-back-home",
    answer: "2NE1 - Come Back Home"
  },
  {
    url: "https://soundcloud.com/2ne1-music/lonely",
    answer: "2NE1 - Lonely"
  },
  {
    url: "https://soundcloud.com/2ne1-music/clap-your-hands",
    answer: "2NE1 - Clap Your Hands"
  },
  {
    url: "https://soundcloud.com/2ne1-music/go-away",
    answer: "2NE1 - Go Away"
  },
  {
    url: "https://soundcloud.com/2ne1-music/ugly",
    answer: "2NE1 - Ugly"
  },
  {
    url: "https://soundcloud.com/2ne1-music/hate-you",
    answer: "2NE1 - Hate You"
  },
  {
    url: "https://soundcloud.com/2ne1-music/cant-nobody",
    answer: "2NE1 - Can't Nobody"
  },
  {
    url: "https://soundcloud.com/2ne1-music/do-you-love-me",
    answer: "2NE1 - Do You Love Me"
  },
  {
    url: "https://soundcloud.com/4minute-music/hot-issue",
    answer: "4Minute - Hot Issue"
  },
  {
    url: "https://soundcloud.com/4minute-music/muzik",
    answer: "4Minute - Muzik"
  },
  {
    url: "https://soundcloud.com/4minute-music/what-a-girl-wants",
    answer: "4Minute - What A Girl Wants"
  },
  {
    url: "https://soundcloud.com/4minute-music/i-my-me-mine",
    answer: "4Minute - I My Me Mine"
  },
  {
    url: "https://soundcloud.com/4minute-music/huh",
    answer: "4Minute - Huh"
  },
  {
    url: "https://soundcloud.com/4minute-music/volume-up",
    answer: "4Minute - Volume Up"
  },
  {
    url: "https://soundcloud.com/4minute-music/whats-your-name",
    answer: "4Minute - What's Your Name"
  },
  {
    url: "https://soundcloud.com/4minute-music/name-is-4minute",
    answer: "4Minute - Name Is 4Minute"
  },
  {
    url: "https://soundcloud.com/4minute-music/ready-go",
    answer: "4Minute - Ready Go"
  },
  {
    url: "https://soundcloud.com/4minute-music/superstar",
    answer: "4Minute - Superstar"
  }
];