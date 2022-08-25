#!/usr/bin/python3
"""
    generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo
"""
from fabric.api import local, put, run, env
import time

env.hosts = ['52.204.236.97', '54.242.115.107']


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo
    """
    date = time.strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(date))
        return 'versions/web_static_{}.tgz'.format(date)
    except Exception:
        return None


def do_deploy(archive_path):
    """
        distributes an archive to your web servers
    """
    path_version = archive_path.split('/')
    filename_tgz = path_version[1]
    justname = filename_tgz.split('.')
    nameWithoutExt = justname[0]

    try:
        put(archive_path, '/tmp/{}'.format(filename_tgz))
        run('mkdir -p /data/web_static/releases/{}'.format(nameWithoutExt))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format
            (filename_tgz, nameWithoutExt))
        run('rm /tmp/{}'.format(filename_tgz))
        run('mv /data/web_static/releases/{}/web_static/* '.
            format(nameWithoutExt) +
            '/data/web_static/releases/{}'.format(nameWithoutExt))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(nameWithoutExt))
        run('rm -rf /data/web_static/current')
        run('ln -s  /data/web_static/releases/{}/ /data/web_static/current'
            .format(nameWithoutExt))
        return True
    except Exception:
        return False
