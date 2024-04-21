from error_proxy import error_proxy
from datetime import datetime
from Models.nomenclature_model import nomenclature_model
from Models.reciepe_model import reciepe_model
import uuid


class storage_prototype(error_proxy):
    __data = []

    @property
    def data(self):
        return self.__data

    def __init__(self, data: list) -> None:
        if len(data) <= 0:
            self.error_text = "Wrong argument"
        self.__data = data

    # фильтер по дате
    def filter_date(self, start: datetime, finish: datetime):
        if len(self.__data) <= 0:
            self.error_text = "Wrong argument"

        if start > finish:
            self.error_text = "Incorrect period"

        if self.if_error:
            return self.__data

        result = []
        for cur_line in self.__data:
            if cur_line.period >= start and cur_line.period < finish:
                result.append(cur_line)

        return storage_prototype(result)

    # фильтер по номенклатуре
    def filter_nom(self, nom: nomenclature_model):
        if not isinstance(nom, nomenclature_model):
            self.error_text = "Wrong argument"

        if self.if_error:
            return self.__data

        result = []
        for cur_line in self.__data:
            if cur_line.nomenclature == nom:
                result.append(cur_line)

        return storage_prototype(result)

    # фильтер по айди номенклатуры
    def filter_nom_id(self, id: uuid.UUID):
        if not isinstance(id, uuid.UUID):
            self.error_text = "Wrong argument"

        if self.if_error:
            return self.__data

        result = []
        # ищем сходные айди
        for cur_line in self.__data:
            if cur_line.nomenclature.id == id:
                result.append(cur_line)

        return storage_prototype(result)

    # фильтер по рецепту
    def filter_reciepe(self, recepy: reciepe_model):
        if not isinstance(recepy, reciepe_model):
            self.error_text = "Wrong argument"

        ingridients = recepy.ingridient_proportions

        result = []
        # берем только записи с номенклатурой из рецепта
        for cur_ing in list(ingridients.keys()):
            for cur_line in self.__data:
                if cur_ing == cur_line.nomenclature.id:
                    result.append(cur_line)

        return storage_prototype(result)

    def filter_storage(self, storage_id: uuid.UUID):
        if not isinstance(storage_id, uuid.UUID):
            self.error_text = "Wrong argument"

        if self.if_error:
            return self.__data

        result = []

        # ищем сходные айди
        for cur_line in self.__data:
            print(cur_line.storage_id, storage_id)
            if cur_line.storage_id == storage_id:
                result.append(cur_line)

        return storage_prototype(result)
