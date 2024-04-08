from Src.reference import reference
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model
from Src.exceptions import exception_proxy, operation_exception
from Src.Models.storage_row_model import storage_row_model
from Src.Models.storage_model import storage_model

from datetime import datetime

#
# Класс описание одной строки рецепта
#
class receipe_row_model(reference):
    __nomenclature: nomenclature_model = None
    __size: int = 0
    __unit: unit_model = None
    
    def __init__(self):
        super().__init__()
    
    @property
    def nomenclature(self):
        """
            Номенклатура
        Returns:
            _type_: _description_
        """
        return self.__nomenclature
    
    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        exception_proxy.validate(value, nomenclature_model)
        self._name = f"{value.name}"
        self.__nomenclature = value
    
    
    @property
    def size(self) -> float:
        """
            Размер

        Returns:
            _type_: _description_
        """
        return self.__size
    
    
    @size.setter
    def size(self, value ):
        exception_proxy.validate(value, (float, int))
        self.__size = value
    
    
    @property    
    def unit(self) -> unit_model:
        """
           Единица измерения

        Returns:
            _type_: _description_
        """
        return self.__unit    
    
    @unit.setter
    def unit(self, value: unit_model):
        exception_proxy.validate(value, unit_model)
        self.__unit = value
    
    def load(self,  source: dict):
        """
            Загрузить из словаря
        Args:
            source (dict): словарь
        """
        super().load(source)
        if source is None:
            return None
        
        source_fields = ["unit", "size", "nomenclature"]
        if set(source_fields).issubset(list(source.keys())) == False:
            raise operation_exception(f"Невозможно загрузить данные в объект {source}!")
        
        self.__size = source["size"]
        self.__nomenclature = nomenclature_model().load( source[ "nomenclature"])
        self.__unit = unit_model().load(source["unit"])
    
        return self
    
    @staticmethod
    def create_debit_transaction( row, period : datetime, storage: storage_model ) -> storage_row_model:
        """
            Сформировать транзакцию списания
        Args:
            row (receipe_row_model): исходная запись рецепта
            period (datetime): период
            storage (storage_model): склад

        Returns:
            storage_row_model: _description_
        """
        exception_proxy.validate(period , datetime)
        exception_proxy.validate(storage, storage_model)
        
        item = storage_row_model(f"debit transaction")
        item.nomenclature = row.nomenclature
        item.period  = period
        item.storage = storage
        item.storage_type = False
        item.value = row.size
        item.unit = row.unit
        
        return item
        
