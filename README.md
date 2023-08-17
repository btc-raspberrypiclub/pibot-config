# PiBot Config

This is the command to run a docker container (run in the parent directory)
This has been tested on Windows, might not work on Linux

```sh
docker run --mount type=bind,source=$(pwd)/pibot-config,target=/app/botconf --mount type=bind,source=$(pwd)/secrets.ini,target=/app/secrets.ini --name piclub-bot agente11/basic-discord-bot:<tag>
```
