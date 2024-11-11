# Task REST API (Clone of Trello)

# DataBase Model
https://dbdiagram.io/d/Task-project-65cb1b85ac844320ae049344

## Task REST API
WHAT YOU NEED TO RUN THE APP LOCALLY
### Clone the Project From GitHub


- pip install django 
- pip install mysqlclient 
- pip install djangorestframework 
- pip install python-dotenv (connect it)

## Example
```bash
# Clone the repository
git clone https://github.com/WaveGuide1/task_restful_api.git
cd task_restful_api
```
```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
```bash
# Install dependencies
pip install -r requirements.txt
```
```bash
# Run migrations
python manage.py migrate
```
```bash
# Start the development server
python manage.py runserver
```
- SECRET_KEY=your_secret_key
- DEBUG=True  # Set to False in production

### Create a Database (MySQL database was used in this project). You can use Postgresql or any other sql db

### Linux os

```bash
sudo apt update
sudo apt install mysql-server
```
```bash
mysql -u root -p
```

```bash
CREATE DATABASE task_restful_db;
CREATE USER 'taskuser'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON task_restful_db.* TO 'taskuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
### In setting.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'task_restful_db',
        'USER': 'taskuser',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

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
