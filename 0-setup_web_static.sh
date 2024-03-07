#!/usr/bin/env bash
#set up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Helle from Ngnix" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current/
ln -sf /data/web_static/releases/test/ /data/web_static/current
# -R to change owner to the directory and all files
# user:group
sudo chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    server_name _;

    location / {
        index index.html index.nginx-debian.html;
        }
    location /hbnb_static {
        alias /data/web_static/current/;
    }
} " > /etc/nginx/sites-available/default
sudo service nginx restart
