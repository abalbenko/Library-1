from flask import jsonify

from library.repo.RubricRepo import RubricRepo


class RubricService:

    @staticmethod
    def get_rubrics():
        try:
            rubrics = RubricRepo.get_rubrics()
            resp = []

            for rubric in rubrics:
                resp.append({
                    "rubric_id": rubric.id,
                    "rubric_name": rubric.rubric
                })

            return jsonify(resp), 201
        except:
            return jsonify("Rubrics not found"), 404
