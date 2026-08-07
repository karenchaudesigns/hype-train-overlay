# Hype Train Overlay

A Hype Train Overlay.

## ⚠️ Important Note About Usage & Licensing

I am thrilled to share the code for this project so you can build your own custom overlay! However, please note that this repository uses a split license:

* The Code (MIT License): The underlying code is open-source. You are free to use, modify, and distribute the code to run the overlay for your own streams.

* The Art (CC BY 4.0 License): All custom graphics, image files, animations, and branding assets (including the custom duck designs) are licensed under the Creative Commons Attribution 4.0 International License.

You are free to use, share, and adapt my custom assets for your own stream, but you must give clear credit to Karen Chau Designs, LLC and provide a link back to me.

**Want to use your own art instead?**

1. The duck graphic is drawn procedurally. You can change its design by editing the `drawRubberDuck` function in `index.html`.
2. The items (bits, subs, gifts) use emojis. You can update these by modifying the `ASSETS` dictionary in `index.html`.

Have fun building your own setup, and I can't wait to see what custom characters you add!

## OBS Setup Instructions

To use this overlay in OBS, you need to add it as a Browser Source and provide the necessary Twitch credentials via URL parameters. Never hardcode your credentials into the files.

1. Add a new **Browser Source** in OBS.
2. Check **Local file** and browse to the `index.html` file of this repository, OR host it locally (e.g., via `python3 -m http.server 8080`) and enter the local URL.
3. Append the required query parameters to the URL to authenticate with Twitch and enable OBS mode. The URL should look like this (if hosted locally):
   `http://localhost:8080/?token=YOUR_TWITCH_TOKEN&clientId=YOUR_CLIENT_ID&broadcasterId=YOUR_BROADCASTER_ID&obs=true`
   * `token`: Your Twitch Access Token (needs `user:read:chat` scope)
   * `clientId`: Your Twitch Client ID
   * `broadcasterId`: Your Twitch Broadcaster ID
   * `obs=true`: Enables transparent background and hides UI controls for a clean overlay.
4. Set the Width and Height to match your canvas (e.g., 1920x1080).
5. Check **Refresh browser when scene becomes active**.

## Chat Commands
The overlay supports chat commands for the broadcaster to manually trigger events. Only the broadcaster can use these.
* `!hype bits` - Spawns a bit
* `!hype sub` - Spawns a sub
* `!hype giftsub` - Spawns a gift sub
* `!hypetrain start` - Starts the hype train
* `!hypetrain ++` - Levels up the hype train
* `!hypetrain end` - Ends the hype train
* `!hypeborder` - Toggles the visibility of the active area border
* `!hypescatter` - Randomizes the placement of any currently spawned fruits (useful if spawned in awkward locations)
