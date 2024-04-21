from exceptions import argument_exception, operation_exception
from error_proxy import error_proxy
from abc import ABC
import uuid
from pathlib import Path
import sys

sys.path.append(Path(__file__).parent.parent)


class abstract_reference(ABC):
    __id: uuid.UUID
    __name: str = " "
    __error: error_proxy = error_proxy()

    def __init__(self, name: str = "untituled") -> None:
        self.name = name
        self.__id = self.create_id()

    def __str__(self):
        return str(self.id)

    @property
    def error(self):
        """
           Работа с ошибками

        Returns:
            _type_: _description_
        """
        return self.__error

    @property
    def id(self):
        """
            Уникальный код
        Returns:
            _type_: _description_
        """
        return self.__id

    @id.setter
    def id(self, value: uuid.UUID):
        if not isinstance(value, uuid.UUID):
            raise argument_exception('Wrong type of argument')
        self.__id = value

    def create_id(self):
        return uuid.uuid4()

    @property
    def name(self):
        """
           Наименование
        Returns:
            _type_: _description_
        """
        return self.__name.strip()

    @name.setter
    def name(self, value: str):

        if not isinstance(value, str):
            raise argument_exception("Неверный аргумент!")

        value_striped = value.strip()

        if value_striped == "" or len(value_striped) > 50:
            raise argument_exception("Некорректное значение наименование!")

        self.__name = value_striped

    @staticmethod
    def _load(data: dict):
        if data is None:
            return None

        if len(data) == 0:
            raise argument_exception("wrong parameters")

        res = abstract_reference()

        source_fields = ["id", "name"]
        if set(source_fields).issubset(list(data.keys())) == False:
            raise operation_exception(
                f"Невозможно загрузить данные в объект. {data}!")

        res.id = uuid.UUID(data["id"])
        res.name = data["name"]

        return res
