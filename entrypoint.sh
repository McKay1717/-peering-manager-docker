#!/bin/bash
/peering-manager/scripts/upgrade.sh

if [ ! -f "./install.lock" ]; then

    python3 manage.py createsuperuser --no-input
    touch ./install.lock
fi

python3 manage.py runserver 0.0.0.0:8000 --insecure

