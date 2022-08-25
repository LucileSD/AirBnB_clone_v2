#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if [ ! -x /usr/sbin/nginx ]; then
    apt-get update
    apt-get -y upgrade
    apt-get -y install nginx
fi
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "hello, you succeed" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current 
chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server;/a\ \n\t location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
