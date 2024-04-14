from pathlib import Path
import sys



sys.path.append(Path(__file__).parent.parent)

from Logic.Reporting.Abstract_reporting import abstract_reporting
from error_proxy import error_proxy
from Logic.Reporting.Json_convert.convert_factory import convert_factory
import json 



class Json_reporting(abstract_reporting):

    __factory=None

    def load(self, name: str, result):
        return super().load(name, result)

    #отдаём типы сложных классов в convert factory
    def __build_references(self):
        types=[error_proxy]
        for cur_ref_key in (list(self.data.keys())):

            types.append(type(self.data[cur_ref_key][0]))
        self.__factory=convert_factory(types)

    def __init__(self, data_examp: list):
        super().__init__(data_examp)
        self.__build_references()


    def create(self, value):

        Json_return={}

        #по делаем json по индексам
        for index,cur_val in enumerate(self.data[value]):

            Json_return[index]=self.__factory.create(cur_val)

        
        self.load('json',json.dumps(Json_return))


        return json.dumps(Json_return,ensure_ascii=False)
