from library.models.Rubric import Rubric


class RubricRepo:

    @staticmethod
    def get_rubric_by_id(rubric_id):
        return Rubric.query.filter(Rubric.id == rubric_id).first()

    @staticmethod
    def get_rubrics():
        return Rubric.query.all()
