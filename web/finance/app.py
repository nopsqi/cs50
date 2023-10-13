import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, get_symbol_id

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    cash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]["cash"]
    # datas = db.execute("SELECT p.shares, s.symbol;")
    print(lookup("tsla"))

    return "index"


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") and not request.form.get("shares"):
            return apology("All field empty.")
        if not request.form.get("symbol"):
            return apology("Enter stock symbol.")

        result = lookup(request.form.get("symbol"))
        if result is None:
            return apology(f"Can't get {request.form.get('symbol')}")

        if not request.form.get("shares"):
            return apology("Enter amount of share.")

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        if result["price"] * int(request.form.get("shares")) > cash:
            return apology("Not enough cash.")
        cash = cash - (result["price"] * int(request.form.get("shares")))

        db.execute("UPDATE users SET cash = ? WHERE id = ?;", cash, session["user_id"])

        symbol_id = get_symbol_id(db, result["symbol"])
        if not symbol_id:
            symbol_id = db.execute("INSERT INTO symbols (symbol, name) VALUES (?, ?)", result["symbol"], result["name"])
        db.execute("INSERT INTO histories (user_id, transacted, symbol_id, price, shares) VALUES (?, ?, ?, ?, ?)", session["user_id"], datetime.datetime.now(), symbol_id, result["price"], int(request.form.get("shares")))
        rows = db.execute("SELECT shares FROM portofolios WHERE user_id = ? AND symbol_id = ? LIMIT 1;", session["user_id"], symbol_id)
        if len(rows) != 1:
            db.execute("INSERT INTO portofolios (user_id, symbol_id, shares) VALUES (?, ?, ?);", session["user_id"], symbol_id, int(request.form.get("shares")))
        else:
            db.execute("UPDATE portofolios SET shares = ? WHERE user_id = ? AND symbol_id = ?;", rows[0]["shares"] + int(request.form.get("shares")), session["user_id"], symbol_id)

        return redirect("/buy")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Enter stock symbol.")
        result = lookup(request.form.get("symbol"))
        if result is None:
            return apology(f"Can't get {request.form.get('symbol')}")
        result["price"] = usd(result["price"])
        print(get_symbol_id(db, result["symbol"]))
        if not get_symbol_id(db, result["symbol"]):
            db.execute("INSERT INTO symbols (symbol, name) VALUES (?, ?)", result["symbol"], result["name"])
        return render_template("quoted.html", result=result)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username or not password or not confirmation:
            return apology("Please fill all field.")
        is_username_exist = db.execute("SELECT username FROM users WHERE username = ?;", username)
        if is_username_exist:
            return apology("username exist.")
        if password != confirmation:
            return apology("password is not match.")

        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")