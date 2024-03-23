import uuid
from abc import ABC
from Src.errors import error_proxy
from Src.exceptions import exception_proxy, argument_exception

#
# Абстрактный класс для наследования
#
class reference(ABC):
    " Readonly: Уникальный код "
    _id = None
    " Краткое наименование "
    _name = ""
    " Описание "
    _description = ""
    " Информация об ошибке "
    _error = error_proxy()
    
    def __init__(self, name):
        self._id = uuid.uuid4()
        self.name = name
    
    @property
    def name(self):
        "Краткое наименование"
        return self._name
    
    @name.setter
    def name(self, value: str):
        "Краткое наименование"
        exception_proxy.validate( value.strip(), str, 50)
        self._name = value.strip()
        
    @property    
    def description(self):
        " Полное наименование "
        return self._description
    
    @description.setter
    def description(self, value: str):
        " Полное наименование "
        exception_proxy.validate( value.strip(), str)
        self._description = value.strip()
        
    @property
    def id(self):
        " Уникальный код записи "
        return str(self._id.hex)  

    @property
    def is_error(self):
        " Флаг. Есть ошибка "
        return self._error.error != ""  
    
    @staticmethod
    def create_dictionary(items: list):
        """
            Сформировать словарь из списка элементов reference 
        Args:
            items (list): _description_
        """
        exception_proxy.validate(items, list)
        
        result = {}
        for position in items:
            result[ position.name ] = position
           
        return result   
   
    @staticmethod
    def create_fields(source) -> list:
        """
            Сформировать список полей от объекта типа reference
        Args:
            source (_type_): _description_

        Returns:
            list: _description_
        """
        
        if source is None:
            raise argument_exception("Некорректно переданы параметры!")
        
        items = list(filter(lambda x: not x.startswith("_") and not x.startswith("create_") , dir(source))) 
        result = []
        
        for item in items:
            attribute = getattr(source.__class__, item)
            if isinstance(attribute, property):
                result.append(item)
                    
        return result
    
    def __str__(self) -> str:
        """
            Изменим строковое представление класса
        Returns:
            str: _description_
        """
        return self.id
    
    def __hash__(self) -> int:
        """
            Формирование хеш по коду
        Returns:
            int: _description_
        """
        return hash(self.id)
    
    
                
            
        
    
    
    
    