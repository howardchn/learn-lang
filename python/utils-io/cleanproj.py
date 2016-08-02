import zipfile
import os
import sys

# comments by howard.
def compress_project(source_path, target_path=None):
    if target_path is None:
        target_path = source_path.rstrip('/') + '.zip'
    zf = zipfile.ZipFile(target_path, mode='w')

    for each_file in get_file_list(source_path):
        rel_name = os.path.relpath(each_file, source_path)
        zf.write(each_file, arcname=rel_name)
    zf.close()

ignore_suffix = ['.suo', '.user', '.userprefs']
def check_isvalid_dir(file_path):
    basename = os.path.basename(file_path)
    if basename.startswith('.'):
        return False
    else:
        return os.path.isdir(file_path) and not basename.lower() == 'bin' and not basename.lower() == 'obj'


def check_isvalid_file(file_path):
    if not os.path.isfile(file_path):
        return False
    elif os.path.basename(file_path).startswith('.'):
        return False
    elif os.path.splitext(file_path)[1] in ignore_suffix:
        return False
    return True


def get_file_list(dir):
    for each_file in os.listdir(dir):
        each_file_full = os.path.join(dir, each_file)
        if check_isvalid_dir(each_file_full):
            for sub_item in get_file_list(each_file_full): yield sub_item
        elif check_isvalid_file(each_file_full):
            yield each_file_full

if __name__ == '__main__':
    arguments = sys.argv
    source_path = None

    if len(arguments) == 2:
        source_path = arguments[1]
    else:
        source_path = input('Input source path:')

    compress_project(source_path)
