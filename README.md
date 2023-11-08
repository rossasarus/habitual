# habitual
A visual habit tracker

`conda activate habitual` to activate my conda env
`python manage.py runserver` to run the server

helpful tuition https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8

install steps

python -m pip install Django
python manage.py startapp testdb
pip install django-environ
pip install psycopg2
add app to settings.py installed_apps

python manage.py migrate habitual // idk why this is needed to make the migrations.

// it would be great to have shell_plus!
python manage.py shell
from habitual.models import Habit
Habit.objects.create(name="Brush Teeth", amount=3)

pip install django-extensions
pip install ipython

python manage.py shell_plus// NEW HOT SHIT!!



drf tutorial -> https://www.django-rest-framework.org/tutorial/quickstart/
pip install djangorestframework
python manage.py createsuperuser --email admin@example.com --username admin // create superuser