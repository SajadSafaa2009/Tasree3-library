from app import db
from app.models.models import Tip , Source

def get_sources(origin):
    return Source.query.filter(Source.origin == origin,Source.video == False).all()

def get_videos(origin):
    return Source.query.filter(Source.origin == origin,Source.video == True).all()

def get_tips(origin):
    return Tip.query.filter(Tip.origin == origin).all()

def add_source(study_type, grade, origin, text, author, link, significance, description):
    new_source = Source(
        study_type=study_type,
        grade=grade,
        origin=origin,
        text=text,
        author=author,
        link=link,
        significance=significance,
        description=description,
        video=False
    )
    db.session.add(new_source)
    db.session.commit()