import os
home = os.path.expanduser('~')
currentdir = '/home/ali'



#change directory
def cd(filename):
    global currentdir

    currentdir = os.path.join(currentdir , filename)


#lists files in curernt directory
def ls ():
    q = os.listdir(currentdir)
    print(q)

#supose to finde out if its dir or file!
def filehandle (filename) :
    (shortname , extension) = os.path.splitext(filename)

#making newfolder in given path without name
def newfolder(path):
    tmp = os.path.join(path , 'new folder')
    os.mkdir(tmp)

#renaming folder and files
def rename(expath , newpath):
    os.rename(expath , newpath)

#basic file manager
while True:
    ls()
    inp = input()

    # .. means back !
    if inp == '..':
        currentdir = os.path.split(currentdir)[0]

    else :
        cd(inp)


