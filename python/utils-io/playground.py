from io import open
from utils.ospathex import list_files

files = list_files(r'E:\ThinkGeo\MapSuite\MapSuite', '.projitems')
for file_path in files:
    with open(file_path, 'r') as file:
        for line in file:
            if 'Resources.Designer.cs' in line:
                print(file_path)
                break

print('done')
