import os
import io
import stat
import io_util_old
import sys

'''
Replace a string to another in specific extension files. 
'''
def replace(folder, source_str, target_str, ext):
    files = os.listdir(folder)
    for item in files:
        full_path = os.path.join(folder, item)
        if os.path.isfile(full_path) and os.path.splitext(full_path)[1] == ext:
            replaceStr(full_path, source_str, target_str)
        elif os.path.isdir(full_path):
            replace(full_path, source_str, target_str, ext)

def replaceStr(full_path, source_str, target_str):
    os.chmod(full_path, stat.S_IREAD|stat.S_IWRITE)
    file = None
    try:
        file = io.open(full_path, 'r+')
        content = file.read()
        content = str(content).replace(source_str, target_str)

        io_util_old.repcontent(file, content)
    finally:
        if not file == None:
            file.close()

if len(sys.argv) == 5 and __name__ == '__main__':
    full_path = sys.argv[1]
    src_str = sys.argv[2]
    tgt_str = sys.argv[3]
    ext = sys.argv[4]
    replace(full_path, src_str, tgt_str, ext)