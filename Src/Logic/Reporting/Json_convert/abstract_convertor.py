from pathlib import Path

import sys

sys.path.append(Path(__file__).parent.parent.parent)

from src.exceptions import argument_exception
from abc import ABC

class abstract_convertor(ABC):
    #типы конвертируемых данных
    __type_arg=[]


    def convert(Self):
        return 
    
    #конструктор позволяет взять несколько типов
    def __init__(self,*type_value:type):
        for cur_type in type_value:
            self.type_arg=cur_type


    def convert(self):
        return{}
    


    #тип конвертируемых данных
    @property
    def type_arg(self):
        return self.__type_arg
    
    @type_arg.setter
    def type_arg(self,value:type):
        if not isinstance(value,type) :
            raise argument_exception("Неверный аргумент!")
        self.__type_arg.append(value)