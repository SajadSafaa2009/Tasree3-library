from app import db


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    study_type = db.Column(db.Boolean, nullable=False)
    grade = db.Column(db.Boolean, nullable=False)
    origin = db.Column(db.String(255), nullable=False)

    text = db.Column(db.Text)
    author = db.Column(db.String(2048))
    link = db.Column(db.String(2048), nullable=False)

    significance = db.Column(db.Integer, nullable=False, default=1)
    description = db.Column(db.Text)


class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    study_type = db.Column(db.Boolean, nullable=False)
    grade = db.Column(db.Boolean, nullable=False)
    origin = db.Column(db.String(255), nullable=False)

    text = db.Column(db.Text)
    author = db.Column(db.String(2048))
    link = db.Column(db.String(2048), nullable=False)

    significance = db.Column(db.Integer, nullable=False, default=1)
    title = db.Column(db.Text, nullable=False)
