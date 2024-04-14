from pathlib import Path
import os
import sys

sys.path.append(Path(__file__).parent.parent)


from abc import ABC
from settings import settings
from exceptions import argument_exception

#range model, nomenclatur model, nomenclature group model v str csv 
class abstract_reporting(ABC):
    #инкапсуляция настроек
    __settings=None
    
 
    #Данные из start_factory
    __data={}

    @property
    def data(self):
        return self.__data


    #сеттер
    @data.setter
    def data(self,value:dict):
        if not isinstance(value,dict):
            raise argument_exception("Неверный аргумент")
        
        self.__data=value

    #,settings_examp:settings=settings()
    def __init__(self,data_examp:list):
        self.data=data_examp
        #self.hidden_settings=settings_examp



    @property
    def hidden_settings(self):
        return self.__settings
    

    @hidden_settings.setter
    def hidden_settings(self,value:settings):
        if not isinstance(value,settings):
            raise argument_exception ("Неверный аргумент")
        
        self.__settings=value



    
    def create(self,value:str):
        return "string"
    

    #возвращает ключи для отчёта
    def get_fields(self,value:str):
        if not isinstance(value,str):
            raise argument_exception("Неверный аргумент")

        fields = list(filter(lambda x: not x.startswith("_") and not x.startswith('create_'), dir(self.data[value][0].__class__)))
        print(fields)

        return fields
    

    #если в словаре сложный тип данных, или другой словарь - переводим всё в str (нужно для markdown и csv, чтобы небыло <object at ...>)
    def dict_to_str(self,inp_dict:dict):
        result={}
        for key in list(inp_dict.keys()):
            if isinstance(inp_dict[key],dict):
                result[str(key)]=self.dict_to_str(inp_dict[key])
            else:
                result[str(key)]=str(inp_dict[key])

        return result
    

    #выгрузка в файл
    def load(self,name:str,result):
        with open(Path(__file__).parent.parent.parent.parent/f'report.{name}','w') as loader:
            loader.write(result)
        
            
