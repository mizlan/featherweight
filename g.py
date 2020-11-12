import argparse
import os
import util
import subprocess
import file_management

plp = file_management.get_playlists_path()
sgp = file_management.get_songs_path()

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--playlist', type=str, metavar='<TITLE>')
args = parser.parse_args()

playlist = args.playlist

aspath = os.path.join(plp, f'{playlist}.playlist')

with open(aspath) as f:
    for line in util.lines(f):
        song_dest = os.path.join(sgp, f'{line}.m4a')
        # subprocess.run(['ffplay', '-nodisp', '-nostats', '-hide_banner', song_dest])
        subprocess.run(['afplay', song_dest])
