from flask import Blueprint, render_template

core = Blueprint("core", __name__)


@core.get("/")
def root():
    return render_template("index.html")

@core.route("/registration")
def registration():
    return render_template("register.html")

