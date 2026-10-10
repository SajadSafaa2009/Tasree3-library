from flask import (
    Blueprint,
    app,
    render_template,
    redirect,
    url_for,
    request,
    make_response,
)
from app.services.services import add_tip, get_sources, get_tips, get_videos

routes = Blueprint("routes", __name__)


@routes.before_request
def check_cookies():
    if request.endpoint == "routes.grade" or request.endpoint == "routes.set_cookie":
        return

    if not request.cookies.get("grade-cookie") or not request.cookies.get(
        "study-type-cookie"
    ):
        return redirect(url_for("routes.grade"))


@routes.route("/")
def grade():
    return render_template("grade.html")


@routes.route("/home")
def home():
    grade = request.cookies.get("grade-cookie")
    return render_template("index.html", grade=grade)


@routes.route("/iq")
def iq():
    grade = request.cookies.get("grade-cookie")
    study_type = request.cookies.get("study-type-cookie")
    sources = get_sources(origin="iq", grade=grade, study_type=study_type)
    tips = get_tips(origin="iq", grade=grade, study_type=study_type)
    videos = get_videos(origin="iq", grade=grade, study_type=study_type)
    return render_template("iq.html", sources=sources, tips=tips, videos=videos)


@routes.route("/subjects")
def subjects():
    grade = request.cookies.get("grade-cookie")
    return render_template("subjects.html",grade=grade)


@routes.route("/subject")
def subject():
    origin = request.args.get("origin")
    grade = request.cookies.get("grade-cookie")
    study_type = request.cookies.get("study-type-cookie")
    sources = get_sources(origin=origin, grade=grade, study_type=study_type)
    tips = get_tips(origin=origin, grade=grade, study_type=study_type)
    videos = get_videos(origin=origin, grade=grade, study_type=study_type)

    origin_arabic = ""
    if origin == "math":
        origin_arabic = "الرياضيات"
    elif origin == "biology":
        origin_arabic = "الاحياء"
    elif origin == "chemistry":
        origin_arabic = "الكيمياء"
    elif origin == "physics":
        origin_arabic = "الفيزياء"
    elif origin == "english":
        origin_arabic = "اللغة الانكليزية"
    elif origin == "arabic":
        origin_arabic = "اللغة العربية"
    elif origin == "french":
        origin_arabic = "اللغة الفرنسية"
    elif origin == "religion":
        origin_arabic = "التربية الاسلامية"
    elif origin == "math2":
        origin_arabic = "الرياضيات"
    elif origin == "physics2":
        origin_arabic = "الفيزياء"
    elif origin == "chemistry2":
        origin_arabic = "الكيمياء"
    elif origin == "biology2":
        origin_arabic = "الاحياء"
        
    return render_template(
        "subject.html",
        sources=sources,
        tips=tips,
        videos=videos,
        origin_arabic=origin_arabic,
    )


@routes.route("/postsubjects")
def postsubjects():
    grade = request.cookies.get("grade-cookie")
    return render_template("subjects2.html",grade=grade)


@routes.route("/news")
def news():
    return render_template("news.html")


@routes.route("/add")
def add():
    return render_template("add.html")

@routes.route("/add_source")
def add_source():
    return render_template("add source.html")

@routes.route("/add_advice")
def add_advice():
    return render_template("add tip.html")

@routes.route("/add_video")
def add_video():
    return render_template("add video.html")


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

@routes.route("/video/create", methods=["POST"])
def create_video():
    study_type = request.form.get("study_type") == "true"
    grade = request.form.get("grade") == "true"
    origin = request.form.get("origin")
    text = request.form.get("text")
    author = request.form.get("author")
    link = request.form.get("link")
    significance = int(request.form.get("significance", 1))
    description = request.form.get("description")

    from app.services.services import add_video

    add_video(study_type, grade, origin, text, author, link, significance, description)

    return redirect(url_for("routes.add"))


@routes.route("/tip/create", methods=["POST"])
def create_tip():
    study_type = request.form.get("study_type") == "true"
    grade = request.form.get("grade") == "true"
    origin = request.form.get("origin")
    text = request.form.get("text")
    author = request.form.get("author")
    significance = int(request.form.get("significance", 1))
    title = request.form.get("title")

    from app.services.services import add_video

    add_tip(study_type, grade, origin, title, author, significance, text)

    return redirect(url_for("routes.add"))


@routes.route("/set-cookie", methods=["GET"])
def set_cookie():
    grade = request.args.get("grade")
    study_type = request.args.get("study_type")

    response = make_response(redirect(url_for("routes.home")))

    response.set_cookie(
        "grade-cookie",
        grade,
        max_age=60 * 60 * 24 * 30,
    )

    response.set_cookie(
        "study-type-cookie",
        study_type,
        max_age=60 * 60 * 24 * 30,
    )

    return response
