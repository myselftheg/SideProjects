
import os

folders_path = r'C:\Users\mysel\Pictures\PhoneBackup\Folders'

folders_list = os.listdir(folders_path)
for folder in folders_list:
    nested_path = os.path.join(folders_path, folder)
    files = os.listdir(nested_path)
    print(nested_path)
    print(len(files))
    print(files)
    if (len(files) == 1) & (files[0] == '.deletemarkers'):
        # os.remove(os.path.join(nested_path, files[0]))
        print('Removing {} file'.format(os.path.join(nested_path, files[0])))
# print()
