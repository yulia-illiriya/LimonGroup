# LimonGroup

# Installation 
git clone git@github.com:Maksat-developer/LimonGroup.git

# Create virtualenv venv and install requirements.txt
pip3 install -r requirements.txt

# Create migrations
python3 manage.py makemigrations accounts
python3 manage.py makemigrations employees
python3 manage.py makemigrations client
python3 manage.py makemigrations factory

python3 manage.py migrate

# For admin panel 
python3 manage.py createsuperuser
.
.
.
.

# create file .env and write 

SECRET_KEY=NFKDSNFKDSFDSMLK
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://db_username:sb_password@localhost:5432/db_name
DJANGO_SETTINGS_MODLE=config.settings
DEBUG=True

# Run server 
python3 manage.py runserver

