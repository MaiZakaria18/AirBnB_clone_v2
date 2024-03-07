#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env
import os


env.hosts = ['54.237.37.1', '54.145.80.76']
def do_deploy(archive_path):
    """fabric function"""
    if os.path.exists(archive_path) == False:
        return False
    name_without_tgz = archive_path[:-4]
    try:
        put(archive_path, "/tmp/")
        run("tar -xvC /data/web_static/releases/{} -f /tmp/".format(
            name_without_tgz))
        run("rm {}".format(archive_path))
        run("rm -f /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current".format(
            name_without_tgz
        ))
        return True
    except Exception:
        return False
