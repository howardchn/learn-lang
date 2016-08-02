import os

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def check_isvalid_dir(file_path):
    basename = os.path.basename(file_path)
    return os.path.isdir(file_path) and not basename.lower() == 'bin' and not basename.lower() == 'obj'


def check_isvalid_file(file_path, extsExclude = ['.suo', '.user', '.userprefs']):
    if not os.path.isfile(file_path):
        return False
    elif os.path.basename(file_path).startswith('.'):
        return False
    elif os.path.splitext(file_path)[1] in extsExclude:
        return False
    return True

def get_file_list(dir):
    for each_file in os.listdir(dir):
        each_file_full = os.path.join(dir, each_file)
        if check_isvalid_dir(each_file_full):
            for sub_item in get_file_list(each_file_full): yield sub_item
        elif check_isvalid_file(each_file_full):
            yield each_file_full

def repcontent(file, new_content):
    file.seek(0)
    file.truncate()
    file.write(new_content)
