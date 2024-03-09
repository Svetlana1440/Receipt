from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception
from Src.Logics.convert_factory import convert_factory
import json

class json_reporting(reporting):
    def create(self, typeKey: str):
        result = []

        #Исходные данные
        items = self.data[ typeKey]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")
        
        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")
        
        data = {}
        
        for item in items:
            for field in self.fields:
                value = getattr(item, field)
                if value is None:
                    value = ""
                value = convert_factory.convertor(value)
                data[field] = value
                result.append(data)
        data = json.dumps(result)
        return data
            

