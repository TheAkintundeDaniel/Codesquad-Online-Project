from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    interest = db.Column(db.String(150), nullable=False)
    skill_level = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.String(150), nullable=True)
