import os

def lines(fileIO):
    return list(map(str.strip, fileIO.readlines()))

def purge_id(song_id, filepath):
    tmpfile = f'{filepath}_tmp'
    with open(filepath) as ids:
        with open(tmpfile, 'w+') as upd:
            print(f'creating temporary file {tmpfile}')
            for candidate in lines(ids):
                if candidate != song_id:
                    tmpfile.write(candidate + '\n')
    os.remove(filepath)
    print(f'removing {filepath}')
    os.rename(tmpfile, filepath)
    print(f'renaming {tmpfile} to {filepath}')
