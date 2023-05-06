# Nitrogen
A Pygame ModernGL topdown multiplayer survival game.

This game is still in development.

If you want to play, you can try to run the portable version.
On Windows just run `Nitrogen.exe`. 
(you will need to let this program through Windows Defender as I have not paid Microsoft to sign it)

On all platforms you can run the source code `Nitrogen.py` with your own python environment.
You should use pygame 2.1.2 (SDL 2.0.18, Python 3.10) with the modules found in `requirements.txt`:

For easy install do `pip install -r requirements.txt`

Your system needs OpenGL 330 or greater.

Source code has been tested on Windows 10/11 (AMD/Nvidia graphics), macOS Catalina (Intel graphics), and Arch Linux (AMD graphics).

To run a private server you can simply run server.py on your machine using any python environment.
You can also run the server as a Docker container by pulling `cabbageman/nitrogenserver` from dockerhub.
Alternatively you can build the Docker image yourself using the included DOCKERFILE.


Features:
As of writing; there are 62 distinct plants, each with its own proper name, growth stage, dropped item, substrate compatibility, moisture range, temperature range, salinity range, special flags, model type, tile size, and vertical height range
A crafting system which allows materials to be combined into items, tools, food, tiles, and objects
A nutrition system with 6 dietary needs: water, carbohydrates, protein, fattyacid, vitamins, and minerals. This encourages a diverse diet and hense an interesting growing/harvesting experience
Tools allow actions, eg the axe lets you cut trees, spade lets you dig channels for water, leaf rake lets you clear dirt, hoe lets you till dirt into farmland
Infinite world size (or at least larger than 2*10^10 x 2*10^10)
Climate system with continuous functions for temperature, moisture, and altitude
Climate based biome system with 9 biome families
Reflections in water will show the sky and geometricly accurate paralaxed reflections of objects such as walls and trees
Custom use of UDP sockets to allow real-time multiplayer via the game server, and the game world is downloaded in real time as your friends build it
Spawnkey system allows you to spawn in the same place as your friends by sharing the key, or keep it private and play on your own
Server selection defaults to cabbage.moe server, but hosting a private server is as easy as launching the server script and changing ip to localhost
A Docker image is provided, making dedicated servers as easy as pressing a button
Intelligent game loop which caches update progress and devides the work among multiple frames to eliminate fps lag, only sending the game state update to be rendered once it is finished
Intelligent render pre-processor which keeps track of what has changed since the last game state, allowing only changed data to be sent to the gpu
Custom geometry system for sending assets to the gpu to be rendered, including 9 geometry presets with texture ID, 3d position, length, width, mirroring, orthoganal rotation, and motion
Random selection of objects over time allows for the dynamic change of the world around the player such as plants growing
Adjustable zoom lets you render more or less of the world at once as desired
Day night cycle with realistic lighting, sky, and moving shadows
Lighting shader with support for 128 light sources of any colour and strength
A sound-stage system which plays ambience according to in-game environment, such as day/night, rain storms, flowing water, sea waves, forest, desert
Movement system with acceleration, velocity, difficult terrain, object collisions, walking, and sprinting
Save states for character and game settings
Variable window size and resolution as well as fullscreen
Vsync can be set off or on to eliminate screen tearing
A JSON inspired data format is used to store all game data (such as plants, tiles, objects, items, food) separate to the code, meaning you can add content without editing any game code
Adjustable ui font size
Supports OpenGL 3 and later, which should be just about every device
Pre-loads all textures into a 2^14 x 2^14 texture pack which is stored on the gpu for lightning fast graphics
Menu ui screens are drawn in a separate routine and sent to the gpu to be overlayed
Sound effects for just about everything in-game, including terrain editing, footsteps, object interactions, swimming, plant interactions
Gamepad support (beta)
Multiplayer ID system with 10000 player slots
Persistent hotbar for held items, used to interact with crafting menu and health menu
Auto save on exit, and auto restore upon launch
Tiered tile data structure with slots for ground material, object + object data, item + item count, and roof material. This allows multiple types of things to stack in a single location (eg, 5 cookies on top of an old table, on a wood floor under a tiled roof)
Animated player sprites which synchronise between players, and interpolate to account for network lag
Animated textures such as flowing water
Plant growth depends on climate and substrate compatibility, with biome determining substrate
As of writing; there are 70 distinct objects, 11 types of dirt, 22 types of tree, 14 foods, 11 items, and 15 crafting recipes
Atmospheric effects such as clouds seen in reflections which cast shadows on the world, thick fog, and rain with geometrically accurate parallax / doppler shift
Pressing F2 will instantly save a screenshot to the games screenshots folder
