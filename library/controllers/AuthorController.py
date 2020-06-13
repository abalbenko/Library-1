from flask import Blueprint, request
from library.services.AuthorService import AuthorService

author = Blueprint('author', __name__, url_prefix='/author')


@author.route("", methods=['POST'])
def add_author():
    name = request.json.get("name")
    surname = request.json.get("surname")
    return AuthorService.add_author(name, surname)


@author.route("/<id>", methods=['GET'])
def get_author(id):
    return AuthorService.get_author_by_id(id)


@author.route("", methods=['GET'])
def get_authors():
    return AuthorService.get_authors()
