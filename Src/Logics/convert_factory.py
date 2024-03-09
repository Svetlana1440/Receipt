from abc import ABC
from Src.exceptions import operation_exception
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.reference_convertor import reference_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.reference import reference
from datetime import datetime


class convert_factory(ABC):
    __maps = {}


    def __init__(self) -> None:
        self.__build_structure()


    def __build_structure(self):
        """
            Сформировать структуру    
        """
        self.__maps[int] = basic_convertor
        self.__maps[float] = basic_convertor
        self.__maps[bool] = basic_convertor
        self.__maps[str] = basic_convertor
        self.__maps[reference] = reference_convertor
        self.__maps[datetime] = datetime_convertor


    """
        Фабричный метод convert
    """
    def convert(self, object) -> dict:
        obj = None
        if object is None:
            return ""
        
        if len(self.__maps) == 0:
            self.__build_structure()

        for i in self.__maps.keys():
            if isinstance(object, i):
                obj = self.__maps[i]
        
        if obj is None:
            raise operation_exception(f"Для {type(object)} нет конвертора")
        
        converter = obj()


        result = converter.convert(object)

        return result