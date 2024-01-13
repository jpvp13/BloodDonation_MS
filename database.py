from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, VARCHAR


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)
    
class Sites(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    SiteName: Mapped[VARCHAR] = mapped_column(VARCHAR, unique = True, nullable = False)
    Address: Mapped[VARCHAR] = mapped_column(VARCHAR, unique = True, nullable = False)
    # PhoneNumber: Mapped[int] = mapped_column(Integer, unique = True, nullable = True)
    
    
def createDB():
  with app.app_context():
    db.create_all()