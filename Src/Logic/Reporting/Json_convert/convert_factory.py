from pathlib import Path
import os
import sys

sys.path.append(Path(__file__).parent.parent)



from src.Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from src.exceptions import argument_exception

class convert_factory:
    __conventor=None    


    def __init__(self,references:list) -> None:
        if not isinstance(references,list):
            raise argument_exception("Неверный аргумент")
        self.__conventor=reference_conventor(*references)



    def create(self,value):
        
        return self.__conventor.convert(value)

