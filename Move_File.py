import os
import shutil

from_dir = "/Downloads"
to_dir = "/Document_Files"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
file_name = list_of_files[0] 
for i in list_of_files():
    os.path.splitext()
    if list_of_files == "":
        list_of_files.append()
path1 = from_dir+"/"+file_name
path2 = to_dir+"/"+"Document_Files"
path3 = to_dir + '/' + "Document_Files" + '/' + file_name
if os.path.exists(path2):
    print("Moving"+file_name+".....")
    shutil.move(path1,path3)
else:
    os.makedirs(path2)
    print("Moving"+file_name+".....")
    shutil.move(path1,path3)