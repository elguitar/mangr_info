#!/bin/bash

apt-get update &&

## Install essential packages
apt-get install -y curl screen python3 &&

# Add all .cron files from cronfolder to crontab
cd /vagrant/ &&
cat cron/*.cron | crontab -u vagrant - &&

## Install node and npm
curl -sL https://deb.nodesource.com/setup_6.x | bash - &&
apt-get install nodejs &&

# Run scripts
python3 bussiapi_to_file.py;
python3 ruokaapi_to_file.py;

# Install and run webserver
npm install http-server -g &&
screen http-server --cors -c-1 -p 8080 &
