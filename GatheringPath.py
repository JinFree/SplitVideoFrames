import os
import pathlib

## Need to fix _ext_, fileDir, txt_name for each case
_ext_ = "avi"
fileDir = r"f:\Home\Downloads\video_split\Split_Video_frames"
txt_name = "filePath.txt"
fileExt = r"**\*."+_ext_

def print_list(a_list):
    for member in a_list:
        print(member)

def gathering_path(file_dir, file_ext):
    src = list(pathlib.Path(file_dir).glob(file_ext))
    a_list = []
    for a in src:
        a_list.append(str(a))
    return a_list

def save_path(file_list_txt, file_path):    
    f = open(file_list_txt, 'w')
    for i in range(len(file_path)):
        f.write(file_path[i]+'\n')
    f.close()

a_list = gathering_path(fileDir, fileExt)
print_list(a_list)
save_path(txt_name, a_list)
