#!/bin/bash
cd "$( dirname "${BASH_SOURCE[0]}" )"
apt-get install python3 sqlite3 python-virtualenv python3-pip
virtualenv -p /usr/bin/python3 env
. ./env/bin/activate
pip install -r req.txt
cd doctorapp
./manage.py migrate
./manage.py loaddata initial.json
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:80 


