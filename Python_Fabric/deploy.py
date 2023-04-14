#!/usr/bin/python3
# Fabscript to distributes an archive to a web server.->1-pack_web_static.py
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ['52.72.12.225', '100.24.205.73']


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1] # archive path is versions/web_static_20170315003959.tgz, split by / and get the last element to get the file name 'web_static_20170315003959.tgz'
    name = file.split(".")[0] # split by . and get the first element to create name for folder to unpack the archive 'web_static_20170315003959'

    if put(archive_path, "/tmp/{}".format(file)).failed is True: # put the archive in the /tmp/ directory of the web server, puts web_static_20170315003959.tgz
        return False
    if run("rm -rf /data/web_static/releases/{}/". # remove the release folder if it exists , and recursively remove all files and directories in the release folder
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/". # create the release folder again
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/". # unpack the archive to folder with same name as file release folder, unpacked webstatic folder inside web_static_20170315003959 
           format(file, name)).failed is True:                  # +--tar -xzf web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959
        return False
    if run("rm /tmp/{}".format(file)).failed is True: # remove the archive from the web server
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True: # move all files from webstatic folder to web_static_20170315003959 folder
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static". # remove the webstatic folder
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True: # remove the symbolic link
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current". # create a new symbolic link to the web_static_20170315003959 folder
           format(name)).failed is True:
        return False
    return True
