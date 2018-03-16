import os, shutil, os.path

def OpenFile(file_path):
    os.startfile(file_path)

def CopyFile(file_path, target_path):
    shutil.copy2(file_path, target_path)

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

def MakeDir(path = os.getcwd()):
    os.mkdir(path)

while True:
    dir_info = next(os.walk(os.getcwd()))
    print('current_path :', dir_info[0], '\navailable directories :', dir_info[1], '\navailable files :', dir_info[2])
    command = input('Enter a number to enter a file(2) or dir(1), b to get to parrent dir, d to change drive :')
    if command == 'b' or command == 'B':
        back = os.path.dirname(os.getcwd())
        os.chdir(back)
    elif command[0] == 'd' or command[0] == 'D':
        new_drive = command[1].capitalize() + ':/'
        os.chdir(new_drive)
    else:
        new_path = dir_info[0] + '\\' + dir_info[int(command[0])][int(command[1:]) - 1]
        if int(command[0]) == 1:
            os.chdir(new_path)
        elif int(command[0]) == 2:
            OpenFile(new_path)
        else:
            print('Invalid entry')
