# Featherweight Music Manager

Manage music from the terminal.

## Set a Directory

Set environment variable `FWMM_DIR` as shown below in rc file

```bash
$ export FWMM_DIR="$HOME/code/fwmm"
```

## Song-related Functions

```bash
$ python songs.py -h
usage: songs.py [-h] [-l | -a <URL> | -d <ID>]

Song configuration

optional arguments:
  -h, --help            show this help message and exit
  -l, --list
  -a <URL>, --add-url <URL>
  -d <ID>, --delete <ID>
```

## Playlist-related Functions

```bash
$ python playlists.py -h
usage: playlists.py [-h]
                    [-l | -c <PLAYLIST> | -d <PLAYLIST> | -
a <PLAYLIST> | -r <PLAYLIST>]
                    [-s <SONG NAME>]

Playlist configuration

optional arguments:
  -h, --help            show this help message and exit
  -l, --list
  -c <PLAYLIST>, --create <PLAYLIST>
  -d <PLAYLIST>, --delete <PLAYLIST>
  -a <PLAYLIST>, --add-song <PLAYLIST>
  -r <PLAYLIST>, --remove-song <PLAYLIST>
  -s <SONG NAME>, --song <SONG NAME>
```

*Tested on python 3.8*
