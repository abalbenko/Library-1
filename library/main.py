from library import app
from library.controllers.AuthorController import author
from library.controllers.BookController import book
from library.controllers.RubricController import rubric


def register_blueprints(app):
    app.register_blueprint(author)
    app.register_blueprint(book)
    app.register_blueprint(rubric)


register_blueprints(app)


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='localhost')
