from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask("app")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLALchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_kay=True)
  username = db.Column(db.String(120), Unique=True, nullable=False)
  email = db.Column(db.String(120), Unique=True, nullable=False)
  about_me =db.Column(db.String(500), Unique=False, nullable=False)

def __repr__(self):
  return "<Welcome to the profile of" + self.username + ">"
@app.route("/")
def hello_world():
  return render_template("index.html")

app.run(host="0.0.0.0", port=8080)