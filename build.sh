#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
echo "Installing the latest version of poetry..."
pip install --upgrade pip
pip install poetry==1.4.2
rm poetry.lock
poetry lock
python -m poetry install

python manage.py collectstatic --no-input
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi