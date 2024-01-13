from flask import Flask
from markupsafe import escape #used when allowing input or returning a value to prevent of code injection 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from database import * #importing database.py to cleanly create/alter tables + models


# create the app
app = Flask(__name__)

#create/alter tables call from database.py
createDB() 




@app.route("/")
def hello_world():
    return "<p> Hello, World!</p>"