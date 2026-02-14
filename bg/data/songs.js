// Boy Group K-Pop Heardle Songs Database
// because of autocomplete bug
// if the answer starts with a number, need to precede it with a space (" ")
// otherwise it won't be available

const songs = [
  {
    url: 'https://soundcloud.com/schwd/really-really-winner?in=ap4zljw02nzh/sets/k-pop',
    answer: 'SONGABTME - REALLY REALLY - WINNER',
  },
  {
    url: 'https://soundcloud.com/officialbts/bts-dimple-illegal-2?in=ap4zljw02nzh/sets/k-pop',
    answer: 'BTS ARMY - BTS - Dimple/ Illegal (보조개)',
  },
  {
    url: 'https://soundcloud.com/kim-xiautaro/seventeen-hot-face-the-sun?in=ap4zljw02nzh/sets/k-pop',
    answer: 'Adinda Ayu Cahyani - SEVENTEEN (세븐틴) - HOT',
  },
  {
    url: 'https://soundcloud.com/yeshi-pelden-4156496/mv-pentagon-shine-mp3?in=ap4zljw02nzh/sets/k-pop',
    answer: 'Yeshi Pelden - [MV] PENTAGON(펜타곤)Shine(빛나리).mp3',
  },
  {
    url: 'https://soundcloud.com/user-68689579/exo-love-me-right-tender-love-first-love?in=ap4zljw02nzh/sets/k-pop',
    answer: 'Rays2008 - EXO - LOVE ME RIGHT & TENDER LOVE & FIRST LOVE',
  },
  {
    url: 'https://soundcloud.com/moonjaypark/shinee-replay?in=ap4zljw02nzh/sets/k-pop',
    answer: 'moonjaypark - SHINee(샤이니) 누난 너무 예뻐 (Replay)',
  },
  {
    url: 'https://soundcloud.com/12-gabriel-mathew-d/oh-my?in=ap4zljw02nzh/sets/k-pop',
    answer: 'SEVENTEEN - 어쩌나 (Oh My!)',
  },
  {
    url: 'https://soundcloud.com/kd_parkwoojin/oh-little-girl?in=ap4zljw02nzh/sets/k-pop',
    answer: '슬레이트 - Oh Little Girl',
  },
  {
    url: 'https://soundcloud.com/user-53485921/nice?in=ap4zljw02nzh/sets/k-pop',
    answer: '. - 세븐틴 - 아주 NICE',
  },
  {
    url: 'https://soundcloud.com/minie-minie-659240429/ov0horqoxj91?in=ap4zljw02nzh/sets/k-pop',
    answer: 'Minie Minie - 낙원',
  },
  {
    url: 'https://soundcloud.com/l2share000/stray-kids-back-door?in=ap4zljw02nzh/sets/k-pop',
    answer: 'L2Share♫000 - Stray Kids - Back Door',
  },
  {
    url: 'https://soundcloud.com/cocominji_35/kangaroo?in=ap4zljw02nzh/sets/k-pop',
    answer: '[Wanna One] Triple Position - Kangaroo (캥거루)',
  },
  {
    url: 'https://soundcloud.com/user-55808555/flower-road-bigbang?in=ap4zljw02nzh/sets/k-pop',
    answer: 'BIGBANG - 꽃길 (FLOWER ROAD) - BIGBANG',
  },
  {
    url: 'https://soundcloud.com/satgotnick4/rh1?in=ap4zljw02nzh/sets/k-pop',
    answer: '𝙣𝙞𝙘𝙝𝙤𝙡𝙖𝙨 - Rush Hour (Feat. j-hope of BTS) - Crush (크러쉬)',
  },
  {
    url: 'https://soundcloud.com/user-879984599/say-my-name-say-yes-boys?in=ap4zljw02nzh/sets/k-pop',
    answer: ' ૮ ᴗ͈ ̫ ᴗ͈ ྀིა - Say My Name - Say Yes! 보이즈 플래닛 Boys Planet 원본 음원',
  },
];
