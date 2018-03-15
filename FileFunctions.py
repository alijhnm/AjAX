import os, shutil

def OpenFile(file_path):
    os.startfile(file_path)

def CopyFile(file_path, target_path):
    os.copy2(file_path, target_path)

def RenameFile(old_name, new_name):
    try:
        os.rename(old_name, new_name)
    except OSError:
        print('File name already exists')

def RemoveFile(file_path):
    os.remove(file_path)

def RemoveDir(dir_path):
    shutil.rmtree(dir_path)

def CutFile(file_path, target_path):
    shutil.move(file_path, target_path)

def MakeZip(dir, target_path, name):
    tmp_dir = os.getcwd()
    os.chdir(target_path)
    shutil.make_archive(name, 'zip', dir, dir)
    os.chdir(tmp_dir)

def ExtractZip(archieve_path, extract_path):
    shutil.unpack_archive(archieve_path, extract_path)

#ExtractZip('D:/testCompressed.zip', 'D:/')
#MakeZip('D:/test-compress', 'D:/', 'testCompressed')
#CopyFile('D:/Document/Untitled.png', 'D:/Aks.png')
#RenameFile('D:/Server.bmp', 'D:/Siroos.bmp')
#RemoveFile('D:/test.bmp')
#RemoveDir('D:/test')
#CutFile('D:/Server.py','D:/Git')
