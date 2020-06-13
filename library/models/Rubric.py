from library import db


class Rubric(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)

    rubric = db.Column(db.String(100),
                       nullable=False)
