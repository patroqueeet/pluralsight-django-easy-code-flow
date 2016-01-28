#!/bin/bash

source .ve/bin/activate

git pull --no-edit && pip install -r requirements.txt | grep -v "Requirement already satisfied" && ./demo/manage.py migrate && ./demo/manage.py collectstatic --noinput
echo "touching to reload uwsgi..."
touch /tmp/pluralsight1-develop.pid
echo "...finished"
