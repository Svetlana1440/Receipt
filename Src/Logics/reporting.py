from abc import ABC
from Src.settings import settings
from Src.exceptions import exception_proxy, operation_exception
from Src.reference import reference


#
# Абстрактный класс для реализации отчетности
#
class reporting(ABC):
    # Набор данных
    __data = {}
    # Список полей
    __fields = []    

    
    def __init__(self, _data):
        """

        Args:
            _setting (settings): Настройки
            _data (_type_): Словарь с данными
        """
        
        exception_proxy.validate(_data, dict)
        
        self.__data = _data
        

 
    def create(self, typeKey: str):
        """
            Сформировать отчет
        Args:
            typeKey (str): Ключ тип данных
        """
        exception_proxy.validate(typeKey, str)
        self.__fields = self.build(typeKey, self.__data)
        
        return ""
    
        
    
    @staticmethod
    def build( typeKey: str, data: dict) -> list:
        """
            Предобработка. Получить набор полей
        Args:
            typeKey (str): ключ в словаре_
            data (dict): Данные - словарь

        Returns:
            list: список
        """
        
        exception_proxy.validate(typeKey, str)
        if data is None:
            raise operation_exception("Набор данных не определен!")
        
        if len(data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        item = data[typeKey][0]
        result = list(filter(lambda x: not x.startswith("_") and not x.startswith("create_") , dir(item)))
       
        return result    
    
    def _build(self, typeKey: str) -> list:
        """
           Предобработка данных. Возвращает набор полей класса typeKey
        Args:
            typeKey (str): ключ для выборки данных
        Returns:
            list: список
        """
        return reporting.build(typeKey, self.__data)
        
        
    @property    
    def fields(self) -> list:
        """
        Набор полей от исходного объекта на основании которого формируем отчет
        """    
        return self.__fields    
            
    @property         
    def data(self) -> dict:
        """

        Returns:
            dict: словарь с данными
        """
        return self.__data    