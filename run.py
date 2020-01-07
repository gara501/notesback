from flask import Flask, render_template
from db import getData

app = Flask(__name__)

@app.route("/")

def hello():
  users = getUsers()
  return render_template('home.html', users=users)

def getUsers():
  users = getData('get_users')
  return users

if __name__ == "__main__":
  app.run(debug="True")