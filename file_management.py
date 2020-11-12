import os, sys
from pathlib import Path

import util

def get_path():
    FWMM_PATH = os.environ.get('FWMM_DIR')
    HOME_PATH = os.environ.get('HOME')

    if FWMM_PATH is None:
        FWMM_PATH = os.path.join(HOME_PATH, '.fwmmd')
        if 'FWMM_SUPPRESS_HOME' not in os.environ:
            print(f'FWMM_PATH is not defined, resorting to default path: {FWMM_PATH}')

    if not os.path.isdir(FWMM_PATH):
        os.makedirs(FWMM_PATH)

    return FWMM_PATH

def get_songs_path():

    ROOT = get_path()

    SONG_DIRECTORY = os.path.join(ROOT, 'songs')
    if not os.path.isdir(SONG_DIRECTORY):
        print(f'song directory doesnt exist: {SONG_DIRECTORY}')
        print(f'-> creating directory {SONG_DIRECTORY}')

        os.makedirs(SONG_DIRECTORY)
    
    return SONG_DIRECTORY

def get_playlists_path():

    ROOT = get_path()

    PLAYLIST_DIRECTORY = os.path.join(ROOT, 'playlists')
    if not os.path.isdir(PLAYLIST_DIRECTORY):
        print(f'playlist directory doesnt exist: {PLAYLIST_DIRECTORY}')
        print(f'-> creating directory {PLAYLIST_DIRECTORY}')

        os.makedirs(PLAYLIST_DIRECTORY)
    
    return PLAYLIST_DIRECTORY


def get_ids_path():

    ROOT = get_path()

    SONG_ID_PATH = os.path.join(ROOT, 'ids.txt')
    if not os.path.exists(SONG_ID_PATH):
        print(f'ids.txt doesnt exist')
        print(f'-> creating ids.txt')
    
        Path(SONG_ID_PATH).touch()
    
    return SONG_ID_PATH

def get_song_ids():

    dest = get_ids_path()
    
    with open(dest) as f:
        return util.lines(f)

if __name__ == '__main__':
    get_songs_path()
    get_playlists_path()
    print(get_song_ids())
