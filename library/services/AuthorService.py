from flask import jsonify
from library.models.Author import Author
from library.repo.AuthorRepo import AuthorRepo
from library import db


class AuthorService:
    @staticmethod
    def add_author(name, surname):
        try:
            author = Author(
                name=name,
                surname=surname
            )
            AuthorRepo.add_author(author)
            return jsonify({
                "message": "Author {} --was added".format(name)
            }), 201
        except:
            db.session.rollback()
            return jsonify("Author {} cannot be added".format(name))

    @staticmethod
    def get_author_by_id(id):
        try:
            author = AuthorRepo.get_author_by_id(id)
            return jsonify({
                "author_id": author.id,
                "author_name": author.name,
                "author_surname": author.surname
            }), 201
        except:
            return jsonify("Authors not found")

    @staticmethod
    def get_authors():
        try:
            authors = AuthorRepo.get_authors()
            resp = []
            for author in authors:
                resp.append({
                    "author_id": author.id,
                    "author_name": author.name,
                    "author_surname": author.surname
                })

            return jsonify(resp), 201
        except:
            return jsonify("Authors not found")
