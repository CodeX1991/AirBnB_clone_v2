#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents
    of the web_static
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))

    if result.succeeded:
        size = os.stat(filename).st_size
        print("web_static packed: {} -> {}Bytes".format(filename, size))
        return filename
    else:
        return None
