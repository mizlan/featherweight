import file_management, os
from pathlib import Path

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
		print(f'playlist does not exist: {playlist_dest}')
		raise KeyError

	playlist = open(playlist_dest, 'a')
	playlist.write(song_id + '\n')

def remove_song_from_playlist(song_id: str, playlist_name):
	filename = f'{playlist_name}.playlist'
	playlist_dir = file_management.get_playlists_path()
	playlist_dest = os.path.join(playlist_dir, filename)

	if not os.path.exists(playlist_dest):
		print(f'playlist does not exist: {playlist_dest}')
		raise KeyError
	
	util.purge_id(song_id, playlist_dest)
