from library.models.Author import Author
from library import db

class AuthorRepo:

    @staticmethod
    def add_author(author):
        db.session.add(author)
        db.session.commit()
        return author

    @staticmethod
    def get_author_by_id(author_id):
        return Author.query.filter(Author.id == author_id).first()

    @staticmethod
    def get_authors():
        return Author.query.all()
