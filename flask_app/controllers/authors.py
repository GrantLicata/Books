"""
#REMINDERS
1. The data we access will be instance(s) of objects and require dot notation to target informaiton and methods.

#TO-DO:
1. Update the object name in the import statement
2. Generate necessary routes
"""

from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.object import User

@app.route("/")
def index():
    return render_template("index.html")
            
@app.route('/NAME-ROUTE')
def show():
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)

@app.route('/NAME-ROUTE', methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/NAME-ROUTE')