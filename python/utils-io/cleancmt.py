#!/usr/bin/env python

import io
import os
import sys
from ospathex import list_files

def clean_file(path):
    with io.open(path, 'r+') as file:
        lines = []
        for line in file:
            is_empty = line.strip('\n') == ''
            if not is_empty:
                for slash in ['//', '///']:
                    start = line.find(slash)
                    if start >= 0:
                        line = line[0:start]

                if not line.strip() == '':
                    lines.append(line)
            else: lines.append(line)

        file.seek(0)
        file.truncate()
        file.writelines(lines)

def clean_dir(dir):
    for file_path in list_files(dir, '.cs'):
        clean_file(file_path)

def clean(path):
    if os.path.isdir(path): clean_dir(path)
    else: clean_file(path)

path = r'C:\Users\Howard\Source\Repos\SlimHill\SlimHill.MapKit.Kernel\SlimHill.MapKit.Kernel.Windows\Layers\Index\RTree'
# if len(sys.argv) == 2:
#     path = sys.argv[1]
# else:
#     print('Input path to clean comments. using: cleancmt [path]')
#     path = input('path=')
#     if not os.path.exists(path):
#         raise Exception('File not found.')

if __name__ == "__main__":
    clean(path)
    print('Complete.')


