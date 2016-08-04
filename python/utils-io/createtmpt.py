import io
import os
import io_util_old
import shutil
import sys
import stat

def clone_to(source_folder, target_name):
    source_name = os.path.basename(source_folder)
    root_folder = os.path.dirname(source_folder)
    os.chmod(root_folder, stat.S_IREAD | stat.S_IWRITE)

    target_folder = os.path.join(root_folder, target_name)

    if os.path.exists(target_folder):
        shutil.rmtree(target_folder)

    shutil.copytree(source_folder, target_folder)

    for file_path in io_util_old.get_file_list(target_folder):
        new_filepath = file_path.replace(source_name, target_name)
        new_filefolder = os.path.dirname(new_filepath)
        if not os.path.exists(new_filefolder):
            os.mkdir(new_filefolder)

        shutil.move(file_path, new_filepath)

        lines = []
        file = io.open(new_filepath, 'r+')
        for line in file:
            is_empty = line.strip('\n') == ''
            if not is_empty:
                line = str(line).replace(source_name, target_name)
                if not line.strip() == '':
                    lines.append(line)
            else: lines.append(line)

        file.seek(0)
        file.truncate()
        file.writelines(lines)

    for folder in os.listdir(target_folder):
        if source_name in folder:
            shutil.rmtree(os.path.join(target_folder, folder))

if len(sys.argv) == 3:
    src_folder = sys.argv[1]
    tgt_name = sys.argv[2]
    clone_to(src_folder, tgt_name)

