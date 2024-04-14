from pathlib import Path
import os
import sys

sys.path.append(Path(__file__).parent.parent)



from src.models.abstract_reference import abstract_reference
from exceptions import argument_exception
from settings import settings
import uuid


class organisation_model(abstract_reference):
    __BIK=""
    __INN=""
    __account=""
    __property_type=""
    

    def __init__(self,value:settings):

        self.__id=self.create_id()
        self.__convert_to_model(value)



    #обьявление атрибутов
    @property
    def BIK(self):
        return self.__BIK

    @property
    def INN(self):
        return self.__INN
    
    @property
    def account(self):
        return self.__account

    @property 
    def property_type(self):
        return self.__property_type
        

    

    @BIK.setter
    def BIK(self,value:str):
        value_stripped=value.strip().replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=9:
            raise argument_exception("Некорректная длинна")
            
        self.__BIK=value_stripped


    @INN.setter
    def INN(self,value: str):
        #value_stripped=value.replace(' ','')
        value_stripped=value.strip().replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=12:
            raise argument_exception("Некорректная длинна")
            
        self.__INN=value_stripped

    @account.setter
    def account(self,value:str):
        #делаем через replace на случай введения с пробелами
        value_stripped=value.strip().replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=11:
            raise argument_exception("Некорректная длинна")
            
        self.__account=value_stripped



    @property_type.setter
    def property_type(self,value:str):
        value_stripped=value.strip()
        if not isinstance(value,str):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=5:
            raise argument_exception("Некорректная длинна")
            
        self.__property_type=value_stripped

    def __convert_to_model(self, value:settings):
        if not isinstance(value,settings):
            raise argument_exception("Неверный аргумент")
        
        settings_names=dir(settings)
        #берем общие атрибуты с property и передаём их классу
        for pr_name in (dir(self)):
            if (pr_name in settings_names) and  isinstance(getattr(organisation_model,pr_name),property)  :
                setattr(self,pr_name,getattr(value,pr_name))
                print (getattr(self,pr_name))

