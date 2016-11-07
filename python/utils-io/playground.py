#coding=utf-8

from io import open
from utils.ospathex import list_files

# files = list_files(r'E:\ThinkGeo\MapSuite\MapSuite', '.projitems')
# for file_path in files:
#     with open(file_path, 'r') as file:
#         for line in file:
#             if 'Resources.Designer.cs' in line:
#                 print(file_path)
#                 break

file_path = r"C:\Users\howar\Desktop\temp.txt"
with open(file_path, 'r+') as file:
    newLines = []
    for line in file:
        if line.strip():
            if not '粤语版' in line:
                newLines.append(line)
    file.seek(0)
    file.truncate()
    file.writelines(newLines)

print('done.')

