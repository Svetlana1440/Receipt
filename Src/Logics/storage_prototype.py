from Src.exceptions import argument_exception, exception_proxy
from Src.errors import error_proxy
from datetime import datetime
from Src.Models.nomenclature_model import nomenclature_model

#
# Прототип для обработки складских транзакций
#
class storage_prototype(error_proxy):
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) <= 0:
            self.error = "Набор данных пуст!"
        
        exception_proxy.validate(data, list)
        self.__data = data
        self.clear()

    # Методы фильтрации

    def filter_by_period( self,start_period: datetime, stop_period: datetime  ):
        """
            Отфильтровать по периоду
        Args:
            start_period (datetime): начало
            stop_period (datetime): окончание

        Returns:
            storage_prototype: _description_
        """
        self.clear()
        
        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"
            
        if start_period > stop_period:
            self.error = "Некорректный период!"
            
         
        if not self.is_empty:
            return self.__data
        
        result = []
        for item in self.__data:
            if item.period > start_period and item.period <= stop_period:
                result.append(item)
                
        return   storage_prototype( result )
    
    
    def filter_by_nomenclature(self, nomenclature:  nomenclature_model):
        """
            Отфильтровать по номенклатуре
        Args:
            nomenclature (nomenclature_model): _description_

        Returns:
            storage_prototype: _description_
        """
        self.clear()
        
        exception_proxy.validate(nomenclature, nomenclature_model)
        
        result = []
        for item in self.__data:
            if item.nomenclature.id == nomenclature.id:
                result.append(item)
                
        return   storage_prototype( result )
        
    # Методы фильтрации    
    
    @property
    def data(self):
        """
            Полученные данные
        Returns:
            _type_: _description_
        """
        return self.__data         
                
    @data.setter            
    def data(self, value: list):
        """
            Исходные данные
        Args:
            value (list): _description_
        """
        exception_proxy.validate(value, list)
        self.__data = value            
                   
            
            
        
    