from backend import db, models
from backend.database import init_db
from flask import Flask

app = Flask(__name__)
init_db(app)

with app.app_context():
    db.create_all()