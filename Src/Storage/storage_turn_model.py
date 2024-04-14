
from src.exceptions import argument_exception
from models.nomenclature_model import nomenclature_model
from src.models.range_model import range_model
import uuid

class storage_turn_model:
    #склад
    __storage_id:uuid.UUID=None

    #оборот
    __amount:int=0


    #период
    __nomenclature:nomenclature_model=None

    #еденица измерения
    __range:range_model=None

    @property
    def storage_id(self):
        return self.__storage_id
    
    @property 
    def amount(self):
        return self.__amount
    
    @property
    def nomenclature(self):
        return self.__nomenclature
    
    @property
    def range(self):
        return self.__range

    
    @storage_id.setter
    def storage_id(self,value:uuid.UUID):
        if not isinstance(value,uuid.UUID):
            raise argument_exception("Невереный аргумент!")
        
        self.__storage_id=value

    
    @amount.setter
    def amount(self,value:int):
        if not isinstance(value,int):
            raise argument_exception("Невереный аргумент!")
        
        self.__amount=value


    @nomenclature.setter
    def nomenclature(self,value:nomenclature_model):
        if not isinstance(value,nomenclature_model):
            raise argument_exception("Невереный аргумент!")
        
        self.__nomenclature=value


    @range.setter
    def range(self,value:range_model):
        if not isinstance(value,range_model):
            raise argument_exception("Невереный аргумент!")
        
        self.__range=value

        