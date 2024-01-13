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

## How to run the flask environment
**$ flask run** (if name of main app is "app.py") 

flask --app "*insert name of main app*" run

