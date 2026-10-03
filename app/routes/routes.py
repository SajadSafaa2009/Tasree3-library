from flask import Blueprint, render_template , redirect, url_for, request
from app.services.services import get_sources,get_tips,get_videos
routes = Blueprint("routes", __name__)


@routes.route("/")
def grade():
    return render_template("grade.html")

@routes.route("/home")
def home():
    return render_template("index.html")

@routes.route("/iq")
def iq():
    sources = get_sources(origin="iq")
    tips = get_tips(origin="iq")
    videos = get_videos(origin="iq")
    return render_template("iq.html",sources = sources ,tips = tips, videos = videos)

@routes.route("/subjects")
def subjects():
    return render_template("subjects.html")

@routes.route("/postsubjects")
def postsubjects():
    return render_template("subjects2.html")

@routes.route("/news")
def news():
    return render_template("news.html")

@routes.route("/add")
def add():
    return render_template("add.html")

@routes.route("/source/create", methods=["POST"])
def create_source():
    study_type = request.form.get("study_type") == "true"
    grade = request.form.get("grade") == "true"
    origin = request.form.get("origin")
    text = request.form.get("text")
    author = request.form.get("author")
    link = request.form.get("link")
    significance = int(request.form.get("significance", 1))
    description = request.form.get("description")

    from app.services.services import add_source
    add_source(study_type, grade, origin, text, author, link, significance, description)

    return redirect(url_for("routes.add"))