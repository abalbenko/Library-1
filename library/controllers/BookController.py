from flask import Blueprint, request
from library.services.BookService import BookService

book = Blueprint('book', __name__, url_prefix='/books')


@book.route("/<id>", methods=['GET'])
def get_book_by_id(id):
    return BookService.get_book_by_id(id)


@book.route("", methods=['GET'])
def get_books():
    return BookService.get_books()


@book.route("/", methods=['POST'])
def create_book():
    year = request.json.get("year")
    author_id = request.json.get("author_id")
    rubric_id = request.json.get("rubric_id")
    return BookService.create_book(year, author_id, rubric_id)


@book.route("/<id>", methods=['PUT'])
def edit_book(id):
    year = request.json.get("year")
    author_id = request.json.get("author_id")
    rubric_id = request.json.get("rubric_id")
    return BookService.edit_book(id, year, author_id, rubric_id)


@book.route("/search", methods=['GET'])
def search():
    author = request.args.get('author')
    press = request.args.get('press')
    rubric = request.args.get('rubric')
    annotation = request.args.get('annotation')
    title = request.args.get('title')
    year = request.args.get('year')

    return BookService.search(author, year, rubric, press, title, annotation)
