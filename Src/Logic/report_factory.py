from src.Logic.Reporting.Abstract_reporting import abstract_reporting
from src.Logic.Reporting.CSV_reporting import CSV_reporting
from src.Logic.Reporting.MD_reporting import MD_reporting
from src.Logic.Reporting.JSON_reporting import Json_reporting
from exceptions import argument_exception,operation_exception


class report_factory:
    __maps={}


    def __build_structure(self):
        self.__maps["CSV"]=CSV_reporting
        self.__maps["MD"]=MD_reporting
        self.__maps["Json"]=Json_reporting


    def  __init__(self):

        self.__build_structure()

    def create(self,format:str,data,key)->abstract_reporting:
        if not isinstance(format,str) or not isinstance(key,str):
            raise argument_exception("Wrong argument")
        
        if data is None:
            raise argument_exception("No argument")
        
        if  len(data)==0:
            raise argument_exception("No DATA")
        
        if format not in self.__maps.keys():
            raise operation_exception(f"for wrong obrabotka")
        

        report_type=self.__maps[format]

        result=report_type(data)

        return result.create(key)
