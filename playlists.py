import file_management, os, glob
import argparse
from pathlib import Path
import sys
import songs

import util

def create_playlist(name):
    filename = f'{name}.playlist'
    playlist_dir = file_management.get_playlists_path()
    playlist_dest = os.path.join(playlist_dir, filename)

    if os.path.exists(playlist_dest):
        print(f'playlist already exists: {playlist_dest}')
        raise KeyError

    Path(playlist_dest).touch()
    # playlist = open(playlist_dest, 'w')
    # return playlist

def delete_playlist(name):
    filename = f'{name}.playlist'
    playlist_dir = file_management.get_playlists_path()
    playlist_dest = os.path.join(playlist_dir, filename)

    if not os.path.exists(playlist_dest):
        print(f'playlist does not exist: {playlist_dest}')
        raise KeyError

    os.remove(playlist_dest)

def playlist_exists(name):
    filename = f'{name}.playlist'
    playlist_dir = file_management.get_playlists_path()
    playlist_dest = os.path.join(playlist_dir, filename)

    return os.path.exists(playlist_dest)

def playlist_contains(song_id, playlist_name):
    if not playlist_exists(playlist_name):
        raise KeyError(f'playlist {playlist_name} doesn\'t exist')

    playlist_dir = file_management.get_playlists_path()
    playlist_dest = os.path.join(playlist_dir, playlist_name)

    return song_id in util.lines(open(playlist_dest))

def add_song_to_playlist(song_id: str, playlist_name):
    filename = f'{playlist_name}.playlist'
    playlist_dir = file_management.get_playlists_path()
    playlist_dest = os.path.join(playlist_dir, filename)

    if not os.path.exists(playlist_dest):
        raise KeyError(f'playlist does not exist: {playlist_dest}')

    if song_id not in file_management.get_song_ids():
        raise KeyError('song id does not exist')

    current_songs = util.lines(open(playlist_dest))

    if song_id in current_songs:
        print('warning! song {song_id} already in current songs! type "y" to continue')
        if input('>') != 'y':
            return

    with open(playlist_dest, 'a') as playlist:
        playlist.write(song_id + '\n')

def remove_song_from_playlist(song_id: str, playlist_name):
    filename = f'{playlist_name}.playlist'
    playlist_dir = file_management.get_playlists_path()
    playlist_dest = os.path.join(playlist_dir, filename)

    if not os.path.exists(playlist_dest):
        print(f'playlist does not exist: {playlist_dest}')
        raise KeyError

    util.purge_id(song_id, playlist_dest)

def show_playlist(playlist_name):
    filename = f'{playlist_name}.playlist'
    playlist_dir = file_management.get_playlists_path()
    playlist_dest = os.path.join(playlist_dir, filename)

    if not os.path.exists(playlist_dest):
        print(f'playlist does not exist: {playlist_dest}')
        raise KeyError

    res = [playlist_name]
    for song_id in util.lines(open(playlist_dest)):
        res.append(f'[{song_id}] {songs.get_song_info(song_id)["title"]}')

    return res

def playlist_names():
    playlist_path = os.path.join(playlist_dir, filename)
    res = []
    for filepath in glob.glob(playlist_path, '*.playlist'):
        res.append(Path(os.path.join(playlist_path, filepath)).suffix)

    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Playlist configuration')
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-l', '--list', action="store_true")
    group.add_argument('-c', '--create', type=str, metavar='<PLAYLIST>')
    group.add_argument('-d', '--delete', type=str, metavar='<PLAYLIST>')
    group.add_argument('-a', '--add-song', type=str, metavar='<PLAYLIST>')
    group.add_argument('-r', '--remove-song', type=str, metavar='<PLAYLIST>')

    parser.add_argument('-s', '--song', type=str, metavar='<SONG NAME>')
    args = parser.parse_args()
    # print(args)
    if args.list:
        playlist_dir = file_management.get_playlists_path()
        for filename in os.listdir(playlist_dir):
            abspath = os.path.join(playlist_dir, filename)
            print(os.path.splitext(filename)[0])
            for song_id in util.lines(open(abspath)):
                print(f'[{song_id}] {songs.get_song_info(song_id)["title"]}')

    elif args.create is not None:
        create_playlist(args.create)

    elif args.delete is not None:
        delete_playlist(args.delete)

    elif args.add_song is not None:
        if args.song is None:
            sys.exit('provide a song (-s)')
        add_song_to_playlist(args.song, args.add_song)

    elif args.remove_song is not None:
        if args.song is None:
            sys.exit('provide a song (-s)')
        remove_song_from_playlist(args.song, args.remove_song)
