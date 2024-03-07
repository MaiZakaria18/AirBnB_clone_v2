#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """fabric function"""
    tgz_name = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    result = local("tar -cvz web_static -f versions/web_static_{}.tgz".format(
        tgz_name))
    if result.succeeded:
        return tgz_name
    else:
        return None
