import os

def list_files(dirname, ext='.*'):
    for path in os.listdir(dirname):
        fullpath = os.path.join(dirname, path)
        if os.path.isdir(fullpath):
            for sub_path in list_files(fullpath, ext): yield sub_path
        else:
            if ext == '.*' or fullpath.endswith(ext): yield fullpath

if __name__ == '__main__':
    for path in list_files(r'E:\ThinkGeo\MapSuite\MapSuite\Layers', '.csproj'):
        print(path)