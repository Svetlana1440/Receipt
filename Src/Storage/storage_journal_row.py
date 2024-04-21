
from uuid import UUID
from datetime import datetime
from Models.nomenclature_model import nomenclature_model
from exceptions import argument_exception
from Storage.storage_journal_transaction import storage_journal_transaction
from Storage.storage_model import storage_model


class storage_journal_row:
    __operation_id = None
    __operation_type = None
    __nomenclature_model = None
    __period = None
    __amount = None
    __location = ""
    __storage_id = None

    # номенклатура
    @property
    def nomenclature(self):
        return self.__nomenclature_model

    # дата
    @property
    def period(self):
        return self.__period

    # id операции
    @property
    def operation_id(self):
        return self.__operation_id

    # id склада
    @property
    def storage_id(self):
        return self.__storage_id

    # тип операции
    @property
    def operation_type(self):
        return self.__operation_type*"add" + (not (self.__operation_type))*"delete"

    # место
    @property
    def location(self):
        return self.__location

    # количество
    @property
    def amount(self):
        return self.__amount

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        if not isinstance(value, nomenclature_model):
            raise argument_exception("Некорректный аргумент")
        self.__nomenclature_model = value

    @storage_id.setter
    def storage_id(self, value: UUID):
        if not isinstance(value, UUID):
            raise argument_exception("Некорректный аргумент")
        self.__storage_id = value

    @location.setter
    def location(self, value: str):
        if not isinstance(value, str):
            raise argument_exception("Некорректный аргумент")
        self.__location = value

    @operation_type.setter
    def operation_type(self, value: bool):
        if not isinstance(value, bool):
            raise argument_exception("Некорректный аргумент")
        self.__operation_type = value

    @period.setter
    def period(self, value: datetime):
        if not isinstance(value, datetime):
            raise argument_exception("Некорректный аргумент")
        self.__period = value

    @operation_id.setter
    def operation_id(self, value: UUID):
        if not isinstance(value, UUID):
            raise argument_exception("Некорректный аргумент")
        self.__operation_id = value

    @amount.setter
    def amount(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise argument_exception("Wrong argument")
        self.__amount = value
