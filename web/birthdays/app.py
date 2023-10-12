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
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        is_valid = {};
        data = request.form
        if data.get("name") is None:
            is_valid["name"] = 0

        try:
            month = int(data.get("month"))
        except:
            is_valid["month"] = 0
        if is_valid.get("month") not in [None, 0] and month not in range(1, 13):
            is_valid["month"] = 0

        try:
            day = int(data.get("day"))
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays;")
        return render_template("index.html", birthdays=birthdays)


