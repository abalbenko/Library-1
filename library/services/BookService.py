from sqlalchemy import update

from library.repo.BookRepo import BookRepo
from library.repo.AuthorRepo import AuthorRepo
from library.repo.RubricRepo import RubricRepo
from library.models.Book import Book
from flask import jsonify
from library import db


class BookService:

    @staticmethod
    def get_book_by_id(book_id):
        try:
            book = BookRepo.get_book_by_id(book_id)
            author = AuthorRepo.get_author_by_id(book.author_id)
            rubric = RubricRepo.get_rubric_by_id(book.rubric_id)

            return jsonify({
                "book_id": book.id,
                "book_author": {
                    "author_name": author.name
                },
                "book_rubric": rubric.rubric,
                "book_year": book.year
            }), 200
        except:
            return jsonify("Book with id {0} not found".format(book_id)), 404

    @staticmethod
    def get_books():
        try:
            books = BookRepo.get_books()
            response_book = []

            for book in books:
                response_book.append(
                    {
                        "book_id": book.id,
                        "rubric_id": book.rubric_id,
                        "author_id": book.author_id,
                        "book_year": book.year
                    })
            return jsonify(response_book), 200
        except:
            return jsonify("Books not found"), 404

    @staticmethod
    def create_book(year, author_id, rubric_id):
        try:
            book = Book(
                author_id=author_id,
                rubric_id=rubric_id,
                year=year
            )
            db.session.add(book)
            db.session.commit()
            return jsonify({
                "message": "Book was added"
            }), 200
        except:
            db.session.rollback()
            return jsonify("Books can not be added"), 404

    @staticmethod
    def edit_book(id, year, author_id, rubric_id):
        try:
            BookRepo.update_book(id, year, author_id, rubric_id)
            db.session.commit()
            return jsonify({
                "message": "Book {0} was updated".format(id)
            }), 200
        except:
            db.session.rollback()
            return jsonify("Book {0} cannot be updated".format(id)), 404

    @staticmethod
    def search(author, year, rubric, press, title, annotation):
        try:
            books = BookRepo.search_book(author, year, rubric, press, title, annotation)
            resp_books = []
            for book in books:
                resp_books.append({
                    "id": book.id,
                    "title": book.title,
                    "year": book.year
                })
            return jsonify(resp_books), 200
        except:
            return jsonify("Books not found"), 404
