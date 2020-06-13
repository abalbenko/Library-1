from library import db


class Press(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)

    name = db.Column(db.String(45),
                   nullable=False)
