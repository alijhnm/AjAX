import os
home = '/home/ali'
currentdir = '/home/ali'



#change directory
def cd(filename):
    global currentdir
    currentdir = os.path.join(currentdir , filename)


#lists files in curernt directory
def ls ():
    q = os.listdir(currentdir)
    print(q)



#basic file manager
while True:
    ls()
    inp = input()

    # .. means back !
    if inp == '..':
        currentdir = os.path.split(currentdir)[0]

    else :
        cd(os.listdir(currentdir)[int(inp)])


