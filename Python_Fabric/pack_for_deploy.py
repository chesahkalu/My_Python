#!/usr/bin/python3
# Fabscript to generates a .tgz archive from the contents of web_static.

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S") #generate current date time using strftime format
        if isdir("versions") is False: #check if versions directory exists
            local("mkdir versions") #create versions directory in local current directory
        file_name = "versions/web_static_{}.tgz".format(date) #create file name with date time and .tgz extension
        local("tar -cvzf {} web_static".format(file_name)) #create tgz archive, a compressed file of all files in "web_static" directory
        return file_name #return file name
    except:
        return None
