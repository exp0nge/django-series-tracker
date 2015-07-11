1. Add 'tracker' to INSTALLED_APPS. Install the django-registration-redux package.
2. Include the URLconf url(r'^tracker/', include('tracker.urls')) in settings.py
3. Run python manage.py migrate
4. Run python manage.py runserver and visit http://127.0.0.1:8080/tracker
