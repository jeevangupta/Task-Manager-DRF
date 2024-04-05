TaskManager  -  built with Django (DRF - Django Rest Framework), Postgres.

    TaskManager is a Django web application for managing tasks. It allows you to create, read, update, and delete tasks, change their status, filter tasks by status, and search by task title. Additionally, it includes user registration, login, and authentication functionalities.

API End Point
    1. / (GET, POST)
    2. 

NOTE: Try to use python version >= 9

Setup:
    1. Clone the repository:
        git clone https://github.com/jeevangupta/Task-Manager-DRF.git
        cd Task-Manager

    2. Create a virtual environment:

        python3 -m venv env
        source ./env/bin/activate

    3. Install dependencies:

        pip install -r requirements.txt

    4. Install Postgres and create the database
        1. Install Postgres and pgAdmin4 .
        2. Create a database named "TaskManagerDRF".

    5. Run database migrations:
        cd TaskProject
        python manage.py migrate

    6. Start the development server:

        python manage.py runserver

    The Django server will start running at http://localhost:8000.








