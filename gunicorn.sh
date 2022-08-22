#! /bin/bash
set -e

# git pull origin main

# Activate the virtualenv for this project
source ../website_env/bin/activate
pip3 install -r requirements.txt
# sudo mkdir -pv /var/log/venya/
sudo mkdir -pv ./static

sudo mkdir -pv /var/www/venya.com/static
# sudo chown -cR thevenya:thevenya /var/log/venya
sudo chown -cR thevenya:thevenya /var/www/venya.com/static
sudo chown -cR thevenya:thevenya /var/www/venya.com/media

# Start gunicorn going
python3 manage.py collectstatic --noinput
# python3 manage.py makemigrations --noinput
# python3 manage.py migrate --noinput

sudo service supervisor restart
sudo service nginx restart

