## Student Registration APP on Django and Mongodb.

### Features:

- Students can register their firstName, lastName, age and location.
- Register Students can view thier registration with their roll number.

## How to start app:

1. Clone the repo.
2. Open the settings.py file there you will see DATABASES dictionary which has a key 'name' which will be the name of the database when the app will try to connect your mongodb locally, if you want so you can even change it.
3. Make sure you Mongodb server is running.
4. To install the required packages run this command:

```
$ pip install -r requirements.txt
```

5. To perform the migrations and start server, run these commands

```
$ python manage.py makemigrations studentData
$ python manage.py migrate
$ python manage.py runserver
```

6. (Optional) If you want to access the admin panel to just hit http://localhost:8000/admin, then enter the username and password.

- Username: admin
- Password: admin
