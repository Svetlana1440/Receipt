from pathlib import Path
from uuid import UUID
import sys

sys.path.append(Path(__file__).parent.parent.parent)

from exceptions import argument_exception
from Logic.Reporting.Json_convert.abstract_convertor import abstract_convertor

class basic_conventor(abstract_convertor):


    def __init__(self):
        super().__init__(str,int,float,UUID,bool)


    def convert(self,name,basic_type_argument):
        result=super().convert()

        if not  type(basic_type_argument)  in self.type_arg:
            raise argument_exception("Неверный аргумент")
        
        result[name]=self.get_str(basic_type_argument)
        return result
    
    def get_str(self,arg):
        return str(arg)

