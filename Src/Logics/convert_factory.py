from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.exceptions import exception_proxy, operation_exception
from Src.reference import reference
from Src.Logics.convertor import convertor


import datetime

#
# Конвертор reference в словарь
#
class reference_convertor(convertor):
    
    def serialize(self, field: str, object: reference) -> dict:
        """
            Подготовить словарь 
        Args:
            field (str): поле
            object (_type_): значение
        """
        super().serialize(field, object)
        
        factory = convert_factory()
        return factory.serialize(object)
    
#
# Фабрика для конвертация данных
#
class convert_factory:
    _maps = {}
    
    def __init__(self) -> None:
        # Связка с простыми типами
        self._maps[datetime.datetime] = datetime_convertor
        self._maps[int] = basic_convertor
        self._maps[float] = basic_convertor
        self._maps[str] = basic_convertor
        self._maps[bool] = basic_convertor
        
        # Связка для всех моделей
        for  inheritor in reference.__subclasses__():
            self._maps[inheritor] = reference_convertor
    
        
    def serialize(self, object) -> dict:
        """
            Подготовить словарь
        Args:
            object (_type_): произвольный тип

        Returns:
            dict: словарь
        """
        
        # Сконвертируем данные как список
        result = self.__convert_list("data", object)
        if result is not None:
            return result
        
        # Сконвертируем данные как значение
        result = {}
        fields = reference.create_fields(object)
        
        for field in fields:
            attribute = getattr(object.__class__, field)
            if isinstance(attribute, property):
                value = getattr(object, field)
                
                # Сконвертируем данные как список
                dictionary =  self.__convert_list(field, value)
                if dictionary is None:
                    # Сконвертируем данные как значение
                    dictionary = self.__convert_item(field, value)
                    
                if len(dictionary) == 1:
                    result[field] =  dictionary[field]
                else:
                    result[field] = dictionary       
          
        return result  
    
    def __convert_item(self, field: str,  source):
        """
            Сконвертировать элемент        
        Args:
            field (str): Наименование поля
            source (_type_): Значение

        Returns:
            dict: _description_
        """
        exception_proxy.validate(field, str)
        if source is None:
            return {field: None}
        
        if type(source) not in self._maps.keys():
            raise operation_exception(f"Не возможно подобрать конвертор для типа {type(source)}")

        # Определим конвертор
        convertor = self._maps[ type(source)]()
        dictionary = convertor.serialize( field, source )
        
        if not convertor.is_empty:
            raise operation_exception(f"Ошибка при конвертации данных {convertor.error}")
        
        return  dictionary
            
    def __convert_list(self, field: str,  source) -> list:
        """
            Сконвертировать список
        Args:
            source (_type_): _description_

        Returns:
            dict: _description_
        """
        exception_proxy.validate(field, str)
        
        # Сконвертировать список
        if isinstance(source, list):
            result = []
            for item in source:
                result.append( self.__convert_item( field,  item ))  
            
            return result 
        
        # Сконвертировать словарь
        if isinstance(source, dict):
            result = {}
            for key in source:
                object = source[key]
                value = self.__convert_item( key,  object )
                result[key] = value
                
            return result    
