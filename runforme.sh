python manage.py makemigrations
python manage.py migrate

echo "makemigrations ve migrate islemleri tamamlandi"

python manage.py createsuperuser --username="admin" --email="ucok.umut@gmail.com" --noinput

python manage.py runserver 8000
