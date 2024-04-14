from pathlib import Path
import sys
from datetime import datetime   

sys.path.append(Path(__file__).parent.parent.parent)

from src.exceptions import argument_exception
from src.Logic.Reporting.Json_convert.abstract_convertor import abstract_convertor
from src.Logic.Reporting.Json_convert.basic_conventor import basic_conventor
from src.Logic.Reporting.Json_convert.date_time_convertor import date_time_conventor

class reference_conventor(abstract_convertor):
    

    #конвертация разных типов данных
    def __convert_None(self,value):
        return "None"


    def __convert_dt(self,value:datetime):
        return date_time_conventor().get_str(value) 

    def __convert_basic(self,value):
        return basic_conventor().get_str(value)
    

    #конвертация словаря с проверкой на сложные типы в нём
    def __convert_dict(self,value:dict):

        result={}
        for cur_key in list(value.keys()):
            atr=value[cur_key]


            result[str(cur_key)]=self.__converts[type(atr)](atr)


        
        return result


    def __build_structure(self):
        #конвертации взятые с других типов
        self.__converts={datetime:self.__convert_dt,dict:self.__convert_dict,type(None):self.__convert_None}
        for i in basic_conventor().type_arg:
            self.__converts[i]=self.__convert_basic
    
    #словарь для типов конвертации
    __converts=None

    def __init__(self,*args):

        

        self.__build_structure()




        
        #типы полученные конструктором 
        for i in args:
            self.type_arg=i
            self.__converts[i]=self.convert

        
    

    #конверт 
    def convert(self, reference):
        result=super().convert()
        #получаем данный
        fields = list(filter(lambda x: not x.startswith("_") and not x.startswith('create_'), dir(reference.__class__)))

        for cur_field in (fields):
            atr=getattr(reference,cur_field)
            result_key=str(cur_field)

            result[result_key]=self.__converts[type(atr)](atr)


        
        return result



            
