#!/bin/bash

apt-get update &&

## Install essential packages
apt-get install -y curl screen python3&&


# Cron expressions
bussicron="* * * * * /vagrant/bussiapi_to_file.py"
ruokacron="5 0 * * * /vagrant/ruokaapi_to_file.py"


crons="/vagrant/"

# Check if there are two /vagrant/ cronjobs
if [[ $(crontab -u vagrant -l | grep $crons | wc -l) -eq 2 ]] ;
  then
    echo "Crontabs already exists. Exiting..."
    exit
  else
    # Write out current crontab into temp file
    crontab -u vagrant -l > mycron
    # Append new cron into cron file
    echo "$bussicron" >> mycron
    echo "$ruokacron" >> mycron
    # Install new cron file
    crontab -u vagrant mycron
    # Remove temp file
    rm mycron
fi

## Install node and npm
curl -sL https://deb.nodesource.com/setup_6.x | bash - &&
apt-get install nodejs &&

## Install and start the webserver
cd /vagrant &&
npm install http-server -g &&
screen http-server --cors -c-1 -p 8080 &
