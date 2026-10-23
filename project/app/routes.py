from . import app, engine
from flask import render_template, flash, redirect, url_for
from sqlalchemy import text
from .forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Erick"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The movie was good!"},
    ]
    return render_template("index.html", title="home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me {}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT 1")).scalar_one()
        return {"database connected": results == 1}
