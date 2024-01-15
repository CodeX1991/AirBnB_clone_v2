#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade

# Install nginx
sudo apt-get -y install nginx

# Create directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Change the body of the index.html page
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic to the folder above
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static)
sudo sed -i '38i\\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
