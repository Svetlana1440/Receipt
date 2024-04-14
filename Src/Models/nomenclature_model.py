from pathlib import Path
import os
import sys
import uuid 

sys.path.append(Path(__file__).parent.parent)



from src.models.abstract_reference import abstract_reference
from src.exceptions import argument_exception,operation_exception
from src.models.nomenclature_group_model import nomenclature_group_model
from src.models.range_model import range_model





class nomenclature_model(abstract_reference):
    __full_name:str=""
    __nom_group:nomenclature_group_model
    __ran_mod:range_model

    
    def __init__(self, name:str="untituled", f_NAME:str="untituled", nom:nomenclature_group_model=nomenclature_group_model(),ran:range_model=range_model()):
        self.name=name 
        self.__id=self.create_id()
        self.full_name=f_NAME

        self.nom_group=nom

        self.ran_mod=ran
        

    @property    
    def id(self):
        """
            Уникальный код
        Returns:
            _type_: _description_
        """
        return self.__id    

    @id.setter
    def id(self,value:uuid.UUID):
        if not isinstance(value,uuid.UUID):
            raise argument_exception('Wrong type of argument')
        self.__id=value 

    @property
    def full_name(self):
        return self.__full_name
    
    @property
    def nom_group(self):
        return self.__nom_group
    
    @property
    def ran_mod(self):
        return self.__ran_mod
    
    #полное имя
    @full_name.setter
    def full_name(self,value:str):
        if not isinstance(value,str):
            raise argument_exception("Неверный аргумент!")
        
        value_striped=value.strip()
        
        if value_striped== "" or len(value_striped)>255:
            raise argument_exception("Некорректное значение наименование!")
        
        self.__full_name = value_striped


    #группа номенклатуры
    @nom_group.setter
    def nom_group(self,value: nomenclature_group_model):
        print(type(value))

        if not isinstance(value, nomenclature_group_model):
            raise argument_exception("Неверный аргумент")
        

        self.__nom_group=value



    #еденица измерения
    @ran_mod.setter
    def ran_mod(self,value:range_model):
        if not isinstance(value,range_model):
            raise argument_exception("Неверный аргумент")
        
        self.__ran_mod=value


    @staticmethod
    def _load(data: dict):
        if data is None:
            return None
        
        if len(data)==0:
            raise argument_exception("wrong parameters")
        

        source_fields = ["id", "name","full_name","nom_group","ran_mod"]
        if set(source_fields).issubset(list(data.keys())) == False:
            raise operation_exception(f"Невозможно загрузить данные в объект. {data}!")
        
        res=nomenclature_model()
        
        res.id=uuid.UUID(data["id"])

        res.name=data["name"]

        res.full_name=data["full_name"]

        res.nom_group=nomenclature_group_model._load(data["nom_group"])

        res.ran_mod=range_model._load(data["ran_mod"])

        return res
