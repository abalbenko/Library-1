from library import db
from library.models.Author import Author
from library.models.Book import Book
from library.models.Press import Press
from library.models.Rubric import Rubric


class BookRepo:

    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.filter(Book.id == book_id).first()

    @staticmethod
    def get_books():
        return Book.query.all()

    @staticmethod
    def update_book(id, year, author_id, rubric_id):
        return db.session.query(Book)\
            .filter(Book.id == id)\
            .update({Book.year: year, Book.author_id: author_id, Book.rubric_id: rubric_id})

    @staticmethod
    def search_book(author, year, rubric, press, title, annotation):
        book_query = Book.query\
            .join(Author)\
            .join(Rubric)\
            .join(Press)

        if author is not None:
            book_query = book_query.filter(Author.name.like('%' + author + '%'))

        if rubric is not None:
            book_query = book_query.filter(Rubric.rubric.like('%' + rubric + '%'))

        if year is not None:
            book_query = book_query.filter(Book.year == year)

        if title is not None:
            book_query = book_query.filter(Book.title.like('%' + title + '%'))

        if press is not None:
            book_query = book_query.filter(Press.name.like('%' + press + '%'))

        if annotation is not None:
            book_query = book_query.filter(Book.annotation.like('%' + annotation + '%'))

        return book_query.all()
