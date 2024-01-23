import os.path
from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from markupsafe import escape #used when allowing input or returning a value to prevent of code injection 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from database import * #importing database.py to cleanly create/alter tables + models


# create the app
app = Flask(__name__)

login_manager = LoginManager()


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

#secrete key
app.config["SECRET_KEY"] = "skwuial;!fbwj02s"

# bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'United'

# initialize the app with the sqlalchemy extension
db.init_app(app)
login_manager.init_app(app)



#Initialize flask-sqlalchemy extension
# db = SQLAlchemy()



#Check to see if database exists. calls method created in database.py. If db does NOT exist create/alter tables. If file exists, skip db creation
if(os.path.isfile("instance/project.db")):
  print("### DATABASE STATUS: EXISTS ###")
  print("### Project database exists. Skipping step ###")
else:
  print("### DATABASE STATUS: DOES NOT EXIST ###")
  print("### Databse does not exist or was updated. Creating database now.... ###")
  createDB()

#admin views
admin = Admin(app, name = 'Admin Portal', template_mode = 'bootstrap3')
admin.add_views(ModelView(User, db.session))
admin.add_views(ModelView(Sites, db.session))



@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


#work on getting login page set up


@app.route("/signup")
def signUp():
    return "<p> Sign Up page </p> <script>alert('AHHH')</script>"

@app.route("/")
def hello_world():
    return "<p> Hello, World!</p>"