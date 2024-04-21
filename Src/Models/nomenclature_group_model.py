from Models.abstract_reference import abstract_reference
import uuid
from exceptions import argument_exception, operation_exception


class nomenclature_group_model(abstract_reference):
    @staticmethod
    def _load(data: dict):
        if data is None:
            return None

        if len(data) == 0:
            raise argument_exception("wrong parameters")

        res = nomenclature_group_model()

        source_fields = ["id", "name"]
        if set(source_fields).issubset(list(data.keys())) == False:
            raise operation_exception(
                f"Невозможно загрузить данные в объект. {data}!")

        res.id = uuid.UUID(data["id"])
        res.name = data["name"]

        return res

    @staticmethod
    def create_group():
        return nomenclature_group_model("Ингридиенты")

    @staticmethod
    def create_group_eggs():
        return nomenclature_group_model("яйца")

    @staticmethod
    def create_group_meat():
        return nomenclature_group_model("мясо")

    @staticmethod
    def create_group_vegs():
        return nomenclature_group_model("Овощи")
