#This is a simple file exlporer and is only used to show how to search and explore different parts of disk

import os
import shutil
import os.path


def OpenFile(file_path):
    """Opens a file at file_path. Works exactly as double clicking in windows"""
    os.startfile(file_path)


def CopyFile(file_path, target_path):
    """Copies the file file_path to the file or directory target_path. file_path and target_path should be strings.If
     file_path specifies a directory,the file will be copied into target_path using the base filename from file_path"""
    shutil.copy2(file_path, target_path)


def RenameFile(old_name, new_name):
    """Renames file old_name to new_name. new_name and old_name are either names at current working directory or
    full paths. If new name is a directory at a different path file will not rename"""
    try:
        os.rename(old_name, new_name)
    except OSError:
        print('File name already exists')


def RemoveFile(file_path):
    """Deletes file file_path"""
    os.remove(file_path)


def RemoveDir(dir_path):
    """Removes an entire directory"""
    shutil.rmtree(dir_path)


def CutFile(file_path, target_path):
    """Cuts a file from file_path and pastes it at target_path"""
    shutil.move(file_path, target_path)


def MakeZip(dir_path, target_path , name):
    """Compreses a dir at dir_path into a zip file and moves it to target_path"""
    tmp_dir = os.getcwd()
    os.chdir(target_path)
    shutil.make_archive(name, 'zip', dir_path, dir_path)
    os.chdir(tmp_dir)


def ExtractZip(archieve_path, extract_path):
    """Extracts a zip file from archieve_path to extract_path"""
    shutil.unpack_archive(archieve_path, extract_path)


def MakeDir(path = os.getcwd()):
    """Makes a new directory at current working directory. If path is provided,
     the new directory will be created there"""
    os.mkdir(path)


def Search(dir, file_or_dir_name):
    """Searches for file_or_dir_name in directory and its subdirectories"""
    searching_for = file_or_dir_name.lower()
    search_generator = os.walk(dir)
    search_result = []
    while True:
        try:
            gen_result = next(search_generator)
            found = gen_result[1] + gen_result[2]
            for i in range(len(found)):
                found_result = found[i].lower()
                if searching_for in found_result:
                    search_result.append(os.path.join(gen_result[0], found[i]))
        except StopIteration:
            break
    if len(search_result) == 0:
        return 'No results found'
    else:
        return search_result


def Back():
    """Returns to parrent directory of current working directory"""
    back = os.path.dirname(os.getcwd())
    os.chdir(back)


def ChangeDrive(new_drive):
    """Changes the working directory to a new drive"""
    tmp = new_drive.capitalize() + ':\\'
    os.chdir(tmp)


while True:
    dir_info = next(os.walk(os.getcwd()))
    print('Current path :', dir_info[0], '\nAvailable directories :', dir_info[1], '\nAvailable files :', dir_info[2])
    command = input('Enter a number to enter a file(2) or dir(1), b to get to parent dir, d to change drive, s to '
                    'search for a file or dir :')
    if command == 'b' or command == 'B':
        Back()
    elif command[0] == 'd' or command[0] == 'D':
        ChangeDrive(command[1])
    elif command[0] == 's' or command[0] == 'S':
        print(Search(os.getcwd(), command[1:]))
    else:
        try:
            new_path = os.path.join(dir_info[0], dir_info[int(command[0])][int(command[1:]) - 1])
            if int(command[0]) == 1:
                os.chdir(new_path)
            elif int(command[0]) == 2:
                OpenFile(new_path)
        except:
            print('Invalid entry')
