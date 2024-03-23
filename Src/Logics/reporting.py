import abc 
from Src.settings import settings
from Src.exceptions import exception_proxy, operation_exception
from Src.reference import reference


#
# Абстрактный класс для реализации отчетности
#
class reporting(abc.ABC):
    # Набор данных
    __data = {}
    # Список полей
    __fields = []    

    
    def __init__(self, _data):
        """

        Args:
            _data (_type_): Словарь с данными
        """
        
        exception_proxy.validate(_data, dict)
        self.__data = _data
        

    @abc.abstractmethod
    def create(self, storage_key: str):
        """
            Сформировать отчет
        Args:
            storage_key (str): Ключ для отбора данных
        """
        exception_proxy.validate(storage_key, str)
        self.__fields = self.build(storage_key, self.__data)
        
        return ""
    
    def mimetype(self) -> str:
        """
          Тип данных для формирования ответа Web сервера
        Returns:
            str: _description_
        """
        return "application/text"    
    
    @staticmethod
    def build( storage_key: str, data: dict) -> list:
        """
            Предобработка. Получить набор полей
        Args:
            storage_key (str): ключ в словаре_
            data (dict): Данные - словарь

        Returns:
            list: список
        """
        
        exception_proxy.validate(storage_key, str)
        if data is None:
            raise operation_exception("Набор данных не определен!")
        
        if len(data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        item = data[storage_key][0]
        result = reference.create_fields( item )
        return result    
    
    def _build(self, storage_key: str) -> list:
        """
           Предобработка данных. Возвращает набор полей класса typeKey
        Args:
            storage_key (str): ключ для выборки данных
        Returns:
            list: список
        """
        return reporting.build(storage_key, self.__data)
        
        
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