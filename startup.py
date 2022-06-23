import os

USERNAME = 'lalasoja'
EMAIL = 'la.ancapi@duocuc.cl'
PASSWORD = 'cartera123'

os.system('python -m pip install -r requirements.txt')
os.system('python manage.py flush')
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system(f'python manage.py collectstatic')
os.system(f'set DJANGO_SUPERUSER_PASSWORD={PASSWORD}')
os.system(f'python manage.py createsuperuser --username {USERNAME} --email {EMAIL} --noinput')
os.system('python manage.py runserver')

