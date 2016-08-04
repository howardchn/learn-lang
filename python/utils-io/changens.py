import os
import io
import io_util_old
import stat
import sys

def changens(dir, oldns, newns):
    os.chmod(dir, stat.S_IREAD | stat.S_IWRITE)
    filepaths = io_util_old.get_file_list(dir)
    for filepath in filepaths:
        file = None
        try:
            os.chmod(filepath, stat.S_IREAD | stat.S_IWRITE)
            file = io.open(filepath, 'r+', encoding='utf8')
            content = file.read()
            content = content.replace('namespace %s' % (oldns), 'namespace %s' % (newns))
            file.seek(0)
            file.truncate()
            file.write(content)
        except:
            print(os.path.basename(filepath) + ' ' + sys.exc_info())
        finally:
            if not file == None:
                file.close()

if len(sys.argv) == 4 and __name__ == '__main__':
    dir = sys.argv[1]
    oldns = sys.argv[2]
    newns = sys.argv[3]
    changens(dir, oldns, newns)
