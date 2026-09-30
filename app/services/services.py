from app import db
from app.models.models import Tip , Source

def get_sources():
    return Source.query.all()

def get_tips():
    return Tip.query.all()