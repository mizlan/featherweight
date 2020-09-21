import os, json, glob
import download
import rng
import file_management
import playlists
import util
from pathlib import Path
import argparse

def get_song_info(song_id):
    songs_dir = file_management.get_songs_path()
    
    filename = f'{song_id}.info.json'

    dest = os.path.join(songs_dir, filename)

    if not os.path.exists(dest):
        raise KeyError(f'song does not exist: {dest}')

    return json.load(open(dest))

def song_exists(link) -> bool:
    songs_dir = file_management.get_songs_path()
    for filepath in glob.glob(os.path.join(songs_dir, '*.info.json')):
        # print(filepath)
        abspath = os.path.join(songs_dir, filepath)
        with open(abspath) as file:
            obj = json.load(file)
            if obj['webpage_url'] == link:
                return True
    return False

def add_song(link):
    if song_exists(link):
        raise FileExistsError("song already exists")

    all_song_ids = set(file_management.get_song_ids())
    code = rng.random_code()

    while code in all_song_ids:
        code = rng.random_code()
    
    title = download.download(link, code)
    #TODO: check if song already exists (by link)

    print(f'downloaded {title} from link {link} with code {code}')

    # add song to ids.txt
    id_path = file_management.get_ids_path()

    with open(id_path, 'a') as f:
        f.write(code + '\n')

def remove_song(song_id):
    playlists_dir = file_management.get_playlists_path()
    for filename in os.listdir(playlists_dir):
        print(f'examining {filename}')
        suf = Path(filename).suffix
        print(suf)
        if suf == 'playlist':
            playlist_name = os.path.splitext(filename)[0]
            playlists.remove_song(song_id, playlist_name)
    
    #TODO: function to delete song from ids, then delete the files from songs/
    ids_dest = file_management.get_ids_path()
    util.purge_id(song_id, ids_dest)
    
    # delete relevant files
    songs_dir = file_management.get_songs_path()
    for filepath in glob.glob(os.path.join(songs_dir, f'{song_id}.*')):
        abspath = os.path.join(songs_dir, filepath)
        print(f'deleting {abspath}')
        os.remove(abspath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Song configuration')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', action="store_true")
    group.add_argument('-a', '--add-url', type=str)
    args = parser.parse_args()
    print(args)
    if args.list:
        ids_path = file_management.get_ids_path()
        all_ids = util.lines(open(ids_path))
        if len(all_ids) == 0:
            print('no songs!')
        for song_id in all_ids:
            json_data = get_song_info(song_id)
            print(json_data['title'])
    elif args.add_url is not None:
        link = args.add_url
        add_song(link)
