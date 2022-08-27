# Red Velvet Heardle

One of my fave Kpop groups ever.

OK, I love Heardles.

This one is remixed and extended from the original [Red Velvet Heardle](https://rvheardle.me/), which ran out of songs.

If you have any questions DM me on Twitter at [@derekahmedzai](https://twitter.com/derekahmedzai).

I also made the [Harry Styles Heardle](https://harry-styles-heardle.glitch.me) and run the updated [Kpop Girl Group Heardle](https://kpopgg-heardle-round2.glitch.me/)

If you have a dead Heardle let me know and I can help you resurrect it.

## Want to create your own Heardle?

A few things to know before you start

- you'll need to be comfortable editing some HTML, Javascript and CSS
- the songs need to be hosted on Soundcloud and be publicly accessible
- you'll need a Glitch account (free!) to remix and host yours (or you can download the code and host wherever)

## How to remix and create your own

1. Register a Glitch account.
2. Remix this project (or another existing custom Heardle project on Glitch) and rename the project to what you want the game link to be (e.g. artist-heardle).
3. In the `index.html` file, change every instance of 'Red Velvet' to your artist's name. You can find and replace by hitting command+option+F on Mac, or ctrl+F on Windows.
4. In the `index.html` file, there is a long link to an image. Replace every instance of this link with a URL to an image of your choice. You can upload an image to glitch by clicking the Assets link in the sidebar.
5. Songs and answers are defined in the `songs.js` file. The songs should go in the order you want the game to go. You can manually enter the songs or if you know how to, you can write a separate script to randomize the tracks and then just copy and paste. **Note: These tracks have to follow the format `Artist - Track Title` for it to display correctly in the SoundCloud widget.**
6. In the `main.js` file, search for every instance of 'K-Pop Girl Group'. These will include the text for the info tab, support tab, game link, game messages, etc. Replace these with your artist and customize the text to your liking. **Important:** Change the game link in the clipboard copy to your custom Heardle link. If you forget, users who copy their results will copy the link to this Heardle instead. Search "red-velvet-heardle.glitch.me" if you can't find the line of code.
7. In the `main.js` file, find where `const Vt` is defined. Below that, there will be a list of game messages that will show depending on how many tries the user guesses the song in. Customize these to your liking.
8. Also in this section is the variable `startDate`. Change this to the current date so that the game starts with the first track in your songs list.

Now you're done with all the necessary changes. Congrats! Read on for optional edits.

1. In the `bundle.css` file, go to line 788. Here you can change the different accent colors for your game. Simply replace the HEX color codes with ones you want.
2. If you want to track usage in Google Analytics, sign up for an account and create a property for this website. In the `index.html` file, edit line 9355 and change the id in the `properties: ["your-code-here"],` bit.
3. If you don't want to use Google Analytics, delete the bit of code that is commented at the bottom of the page.

## Good luck! 

And don't forget to share your custom Heardle! 

Reddit, WhatsApp, Facebook and Twitter are good places to share.
