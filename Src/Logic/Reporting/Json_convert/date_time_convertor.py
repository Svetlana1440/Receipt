from pathlib import Path
from datetime import datetime,date
import sys

sys.path.append(Path(__file__).parent.parent.parent)

from src.exceptions import argument_exception
from src.Logic.Reporting.Json_convert.abstract_convertor import abstract_convertor

class date_time_conventor(abstract_convertor):

    def __init__(self):
        super().__init__(datetime,date)


    def convert(self,name,datetime_type_argument):

        result=super().convert()

        if not  type(datetime_type_argument)  in self.type_arg:
            raise argument_exception("Неверный аргумент")
        
        result[name]=self.get_str(datetime_type_argument)

        return  result
    
    def get_str(self,arg:datetime):
        return "%s-%s-%s" % (arg.day,arg.month,arg.year) 