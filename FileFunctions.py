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

def Search(dir, file_or_dirname):
    searching_for = file_or_dirname.lower()
    search_generator = os.walk(dir)
    search_result = []
    while True:
        try:
            gen_result = next(search_generator)
            found = gen_result[1] + gen_result[2]
            for i in range(len(found)):
                found_result = found[i].lower()
                if searching_for in found_result:
                    search_result.append(gen_result[0] + '\\' + found[i])
        except StopIteration:
            break
    if len(search_result) == 0:
        return 'No results found'
    else:
        return search_result

def Back():
    back = os.path.dirname(os.getcwd())
    os.chdir(back)

def ChangeDrive(new_drive):
    tmp = new_drive.capitalize() + ':\\'
    os.chdir(tmp)

while True:
    dir_info = next(os.walk(os.getcwd()))
    print('Current path :', dir_info[0], '\nAvailable directories :', dir_info[1], '\nAvailable files :', dir_info[2])
    command = input('Enter a number to enter a file(2) or dir(1), b to get to parrent dir, d to change drive, s to search for a file or dir :')
    if command == 'b' or command == 'B':
        Back()
    elif command[0] == 'd' or command[0] == 'D':
        ChangeDrive(command[1])
    elif command[0] == 's' or command[0] == 'S':
        print(Search(os.getcwd(), command[1:]))
    else:
        try:
            new_path = dir_info[0] + '\\' + dir_info[int(command[0])][int(command[1:]) - 1]
            if int(command[0]) == 1:
                os.chdir(new_path)
            elif int(command[0]) == 2:
                OpenFile(new_path)
        except:
            print('Invalid entry')
