from exceptions import argument_exception, operation_exception
from datetime import datetime
from Models.abstract_reference import abstract_reference
from pathlib import Path
import os
import sys
import uuid

sys.path.append(Path(__file__).parent.parent)


class range_model(abstract_reference):
    __recount_ratio: int = 1
    __base_range = None
    __creation_date = None

    def __init__(self, name: str = "untituled", ratio: int = 1, base=None):
        self.name = name
        self.recount_ratio = ratio
        self.__id = self.create_id()
        self.__creation_date = datetime.now()
        if base:
            self.base_range = base

    # дата создания

    @property
    def creation_date(self):
        return self.__creation_date

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

    # коэффициент пересчёта
    @property
    def recount_ratio(self):
        return self.__recount_ratio
    # сеттер

    @recount_ratio.setter
    def recount_ratio(self, value):
        if not isinstance(value, int):
            raise argument_exception("некорректный тип данных!")
        # если, он ниже 0 вызываем исключение
        if value <= 0:
            raise argument_exception("некорректный аргумент")

        self.__recount_ratio = value

    # базовая единица
    @property
    def base_range(self):
        return self.__base_range

    # сеттер

    @base_range.setter
    def base_range(self, value):
        if value is None:
            return None

        if not isinstance(value, range_model):
            raise argument_exception("некорректный аргумент")

        self.__base_range = value

    @staticmethod
    def _load(data: dict):
        if data is None:
            return None

        if len(data) == 0:
            raise argument_exception("wrong parameters")
        source_fields = ["id", "name", "recount_ratio",
                         "base_range", "creation_date"]
        if set(source_fields).issubset(list(data.keys())) == False:
            raise operation_exception(
                f"Невозможно загрузить данные в объект. {data}!")

        res = range_model()
        res.id = uuid.UUID(data["id"])
        res.name = data["name"]
        res.recount_ratio = int(data["recount_ratio"])
        date = data["creation_date"].split(' ')[0]

        # баг
        try:
            res.__creation_date = datetime.strptime(date, "%Y-%m-%d")
        except:
            res.__creation_date = datetime.strptime(date, "%d-%m-%Y")

        if data["base_range"] == "None":
            res.base_range = None
        else:
            res.base_range = range_model()._load(data["base_range"])

        return res

    @staticmethod
    def create_gramm():
        item = range_model("Грамм", 1)
        return item

    @staticmethod
    def create_kilogram():
        return range_model("Килограм", 1000, range_model.create_gramm())

    @staticmethod
    def create_mililitr():
        item = range_model("Милилитр", 1)
        return item

    @staticmethod
    def create_litr():
        return range_model("Литр", 1000, range_model.create_mililitr())

    @staticmethod
    def create_shtuka():
        return range_model("Штука", 1)

    @staticmethod
    def create_spoon():
        return range_model("Столовая ложка", 67, range_model.create_kilogram())
