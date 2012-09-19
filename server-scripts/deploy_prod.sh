#!/bin/bash

cd /sites/accounts.appsbylift.com
. bin/activate

cd website
git pull

pip install -r requirements.txt

export PROD=1

python manage.py syncdb --migrate

python manage.py collectstatic --noinput

touch website/wsgi.py