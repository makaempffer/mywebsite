import os

os.environ['DJANGO_SUPERUSER_USERNAME'] = 'lalasoja'
os.environ['DJANGO_SUPERUSER_EMAIL'] = 'la.ancapi@duocuc.cl'
os.environ['DJANGO_SUPERUSER_PASSWORD'] = 'cartera123'

os.system('python -m pip install -r requirements.txt')
os.system('python manage.py flush')
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system(f'manage.py createsuperuser --noinput')
os.system(f'manage.py collectstatic')
os.system('python manage.py runserver')

