from Src.Logics.reporting import reporting
from Src.Logics.markdown_reporting import markdown_reporting
from Src.Logics.csv_reporting import csv_reporting
from Src.exceptions import exception_proxy, argument_exception, operation_exception
from Src.Logics.json_reporting import json_reporting
#Фабрика для отчетов
class report_factory:
    # словарь
    __maps = {}
 
    def __init__(self)-> None:
        self.__build_structure()


    #Создаем структуру словаря
    def __build_structure(self):
        self.__maps["csv"] = csv_reporting
        self.__maps["markdown"] = markdown_reporting
        self.__maps["json"] = json_reporting

    def create(self, format: str, data) -> reporting:
        """
        Сформировать объект отчет

        """
        exception_proxy.validate(format, str)
        if data is None:
            raise argument_exception("Данные не переданы")
        if  len(data) == 0:
            raise argument_exception("Пустые данные")
        if format not in self.__maps.keys():
            raise operation_exception (f"Для{format}нет обработчика")
        report_type = self.__maps[format]
        result = report_type(data)
        return result



