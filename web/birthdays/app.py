import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    birthdays = db.execute("SELECT * FROM birthdays;")
    is_valid = {"name": 1, "month": 1, "day": 1};
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        data = request.form
        name = data.get("name")
        if len(name) == 0:
            is_valid["name"] = 0

        month = data.get("month")
        try:
            month = int(month)
        except:
            is_valid["month"] = 0
        if is_valid.get("month") is None and month not in range(1, 13):
            is_valid["month"] = 0

        day = data.get("day")
        try:
            day = int(day)
        except:
            is_valid["day"] = 0
        if is_valid.get("day") is None and day not in range(1, 32):
            is_valid["day"] = 0

        if 0 not in is_valid.values():
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        return render_template("index.html", birthdays=birthdays, is_valid=is_valid)

    else:

        # TODO: Display the entries in the database on index.html
        return render_template("index.html", birthdays=birthdays, is_valid=is_valid)


