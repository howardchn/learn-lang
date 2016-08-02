#!/usr/bin/env python

import io
import os
import sys

def clean(path):
    file = None

    try:
        file = io.open(path, 'r+')
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
    finally:
        file.close()

path = None
if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    print('Input path to clean comments. using: cleancmt [path]')
    path = input('path=')
    if not os.path.exists(path):
        raise Exception('File not found.')

if __name__ == "__main__":
    clean(path)


