from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)


@routes.route("/")
def grade():
    return render_template("grade.html")

@routes.route("/home")
def home():
    return render_template("index.html")

@routes.route("/iq")
def iq():
    return render_template("iq.html")

@routes.route("/subjects")
def subjects():
    return render_template("subjects.html")

@routes.route("/postsubjects")
def postsubjects():
    return render_template("subjects2.html")

@routes.route("/news")
def news():
    return render_template("news.html")
