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
