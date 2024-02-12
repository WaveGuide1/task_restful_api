# Task REST API (Clone of Trello)

# DataBase Model

## Task REST API
WHAT YOU NEED TO RUN THE APP LOCALLY
### Clone the Project From GitHub


.. pip install django 
.. pip install mysqlclient 
.. pip install djangorestframework 
.. pip install python-dotenv (connect it)

### Create a Database (MySQL database was used in this project). You can use Postgresql or any other sql db

## Migrate Project to the Database

.. python3 manage.py makemigrations

.. python3 manage.py migrate
## Run the Project

.. python manage.py runserver

.. If there are no errors, open http://127.0.0.1:8000/ in a web browser.

# Database model design link

# Available Local Routes

## User Account Route

[GET] http://127.0.0.1:8000/api/account/users/

[GET] http://127.0.0.1:8000/api/account/users/<ID>/

[POST] http://127.0.0.1:8000/api/account/users/

[PUT] http://127.0.0.1:8000/api/account/users/<ID>/

[DELETE] http://127.0.0.1:8000/api/account/users/<ID>/

## House Route

[Get] http://127.0.0.1:8000/api/house/houses/

Authentication is required
[POST] http://127.0.0.1:8000/api/house/houses/

[GET] http://127.0.0.1:8000/api/house/houses/<ID>/

Authentication is required
[PUT] http://127.0.0.1:8000/api/house/houses/<ID>/

Authentication is required
[DELETE] http://127.0.0.1:8000/api/house/houses/<ID>/

## Task Route (Authentication is required)

[GET] http://127.0.0.1:8000/api/task/tasks/

[POST] http://127.0.0.1:8000/api/task/tasks/

[GET] http://127.0.0.1:8000/api/task/tasks/<ID>/

[PUT] http://127.0.0.1:8000/api/task/tasks/<ID>/

[DELETE] http://127.0.0.1:8000/api/task/tasks/<ID>/

## Authentication Route

Login
[POST] http://127.0.0.1:8000/api/auth/verify/login/


## Task List Route (Authentication is required)

[POST] http://127.0.0.1:8000/api/task/tasklist/

Permission is required
[GET] http://127.0.0.1:8000/api/task/tasklist/

Permission is required
[GET] http://127.0.0.1:8000/api/task/tasklist/<ID>/

Permission is required
[PUT] http://127.0.0.1:8000/api/task/tasklist/<ID>/

Permission is required
[DELETE] http://127.0.0.1:8000/api/task/tasklist/<ID>/


## Attachment Route (Authentication and Permission is Required)

[POST] http://127.0.0.1:8000/api/task/attachments/

[GET] http://127.0.0.1:8000/api/task/attachments/<ID>/

[PUT] http://127.0.0.1:8000/api/task/attachments/<ID>/

[DELETE] http://127.0.0.1:8000/api/task/attachments/<ID>/

## Special Routes (Authentication and Permission is Required)

Join House
[POST] http://127.0.0.1:8000/api/main/houses/<ID>/join/

Leave House
[POST] http://127.0.0.1:8000/api/main/houses/<ID>/leave/

Remove Member (Permission is Required)
[POST] http://127.0.0.1:8000/api/main/houses/<ID>/remove/

Update Task Status (Permission is Required)
[PATCH] http://127.0.0.1:8000/api/task/tasks/2/update_task_status/
