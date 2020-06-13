from library import db


class Author(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)

    name = db.Column(db.String(45),
                     nullable=False)

    surname = db.Column(db.String(45),
                     nullable=False)
