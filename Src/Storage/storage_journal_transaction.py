
import uuid
from datetime import datetime
from Models.nomenclature_model import nomenclature_model
from exceptions import argument_exception


class storage_journal_transaction:
    __type: bool = None
    __period: datetime = None
    __nomenclature: nomenclature_model = None
    __id: uuid = None
    __amount: int = None

    # id
    @property
    def id(self):
        return self.__id

    # период
    @property
    def period(self):
        return self.__period

    # тип операции
    @property
    def type(self):
        return self.__type*"add" + (not (self.__type))*"delete"

    # количество

    @property
    def amount(self):
        return self.__amount

    # номенклатура
    @property
    def nomenclature(self):
        return self.__nomenclature

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: uuid.UUID):
        if not isinstance(value, uuid.UUID):
            raise argument_exception("Некорректный аргумент")

        self.__id = value

    @type.setter
    def type(self, value: bool):
        if not isinstance(value, bool):
            raise argument_exception("Некорректный аргумент")
        self.__type = value

    @period.setter
    def period(self, value: datetime):
        if not isinstance(value, datetime):
            raise argument_exception("Некорректный аргумент")
        self.__period = value

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        if not isinstance(value, nomenclature_model):
            raise argument_exception("Wrong argument")
        self.__nomenclature = value

    @amount.setter
    def amount(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise argument_exception("Wrong argument")
        self.__amount = value
