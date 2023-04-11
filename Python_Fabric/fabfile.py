# install fabric: pip install fabric(fabric installation is tricky, and dependth on alot, invenstiagte more on this)
# create file: fabfile.py
# wirte functions: inside 'def do_pack():' in fabfile.py
# run function: 'fab do_pack' in terminal inside the folder with fabfile.py to run the function
# if functions is in 'haha.py' file, run: fab -f haha.py do_pack
# if need to connect to a server and server details not in file, run: fab -f haha.py do_pack -i ~/.ssh/sshkeypath -u serverusername


from fabric.api import * #import all functions from fabric. eg; local, run, env, put, get, sudo, cd, lcd, prefix, settings, hide, warn, abort, require, roles, execute, task, runs_once, parallel, serial, hosts, shell_env

"""SERVER DETAILS if need be"""
env.hosts = "107.23.106.187" #ip address of the server
env.user = "ubuntu" #username of the server
env.key_filename = "~/.ssh/school" #path to the ssh key file
env.password = "password" #password of the server if ssh key is not used


"""local = This function is used to run a command on the local system"""
def check1(): 
    local("ls /etc/nginx") # list the content of the folder /etc/nginx
    
"""run = This function is used to run a command on the remote system"""
def check2():
    run("ls /var/www/html") # list the content of the folder /etc/nginx on the server

"""get = This function is used to get a file from the remote system"""
def check3():
     get("/backup/db.bak", "./db.bak") # get the file db.bak from the server /backup directory and save it in the current directory as db.bak(overwrites if already exist)
     
"""put = This function is used to put a file on the remote system"""
def check4():
    with cd('/tmp'): #change the working directory on the remote host to /tmp
        put('/path/to/local/test.txt', 'files') # put the file test.txt from the local directory /path/to/local/ to the remote directory /tmp/files
        
"""sudo = This function is used to run a command on the remote system with sudo privileges"""
def check5():
    sudo("apt-get -y update") # update the server os
    
"""prompt = This function is used to prompt the user for input"""
def check6():
    path_to = prompt('Please specify path to file you wish to see its contents:')
    output = run('cat {}'.format(path_to)) # cat the file the user specified and saves the output in the variable 'output'
    print("-----")
    print(output) # print the output of the cat command


def all(): # to create a function that runs all the functions above
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()
    

    
    
