from flask import Blueprint, request

from library.services.RubricService import RubricService

rubric = Blueprint('rubric', __name__, url_prefix='/rubric')


@rubric.route("", methods=['GET'])
def get_rubrics():
    return RubricService.get_rubrics()
