from library import db


class Book(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)

    title = db.Column(db.String(45),
                                 nullable=False)

    annotation = db.Column(db.String(1000),
                      nullable=False)

    year = db.Column(db.Integer,
                     nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    rubric_id = db.Column(db.Integer, db.ForeignKey('rubric.id'))

    press_id = db.Column(db.Integer, db.ForeignKey('press.id'))
