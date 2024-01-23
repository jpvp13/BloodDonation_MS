# BloodDonation_MS
Blood donation management system to practice SQL. Potentially will create GUI + host via AWS to be accessible

## Create environment FIRST
    py -3 -m venv .venv -- Create Environment

## Active environment 
    py -3 -m venv .venv .venv\scripts\activate

## Install Flask + other dependencies AFTER setting up environment + activating it
    pip install Flask -- After activing environment
    pip install python-dotenv -- enables support for Environment Variables From dotenv when running flask command (https://github.com/theskumar/python-dotenv#readme) (https://flask.palletsprojects.com/en/3.0.x/cli/#dotenv)
    pip install -U Flask-SQLAlchemy
    pip install flask login
    pip install flask-admin
    pip install flask-Bcrypt
    pip install flask-WTF
    pip install flask-Migrate
    pip install flask-testing

## How to run the flask environment
**$ flask run** (if name of main app is "app.py") 

flask --app "*insert name of main app*" run



## if appropriate permissions are applicable to your user account, you may access the admin area of the page using
    /admin/