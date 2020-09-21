import subprocess, os, json, sys

import file_management

def download(link, code):

    song_dir = file_management.get_songs_path()
    dest = os.path.join(song_dir, f'{code}.%(ext)s')
    cmd = ['youtube-dl']
    cmd.append('-f')
    cmd.append('bestaudio[ext=m4a]')
    cmd.append('--write-info-json')
    cmd.append('-o')
    cmd.append(dest)
    cmd.append(link)
    print('running', cmd)
    sp = subprocess.run(cmd, capture_output=True)

    if sp.returncode != 0:
        raise

    # return title
    info_file = f'{code}.info.json'
    try:
        with open(os.path.join(song_dir, info_file)) as file:
            title = json.load(file)['title']
            return title
    except FileNotFoundError:
        sys.exit(f'Cannot find json file info_file')
