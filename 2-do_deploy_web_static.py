#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import *
from datetime import datetime
from os.path import exists


# Declare a variable to hold the host ip
env.hosts = ['18.204.10.148', '54.172.94.100']


def do_deploy(archive_path):
    """
    Distributes an archive to my web servers
    """
    if exists(archive_path) is False:
        # Return False if the file at archive_paath doesnt exist
        return False

    # Declare a variable to hold the archive file
    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        # Upload the archive to the /tmp/ directory of the server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder /data/we_static/releases/
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -c {}/".format(tmp, no_tgz))

        # ^ Delete the archive from the web_server
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))

        # Delete the symbolic link /data/web_static/current from the web server
        run("ln -s {}/ /data/web_static/current".format(no_tgz))

        return True
    except Exception:
        return False
