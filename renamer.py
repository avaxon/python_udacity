import os, sys
def rename_files(sciezka):
    file_list=os.listdir(sciezka)
    print file_list
    print(os.getcwd())
    i=0
    for file_name in file_list:
        os.rename(file_name,file_name+str(i))
        i=i+1
sciezka="C:\\temp\\test"
os.chdir(sciezka)

rename_files(sciezka)
