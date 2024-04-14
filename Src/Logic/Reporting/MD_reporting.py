from pathlib import Path
import os
import sys

from settings import settings

sys.path.append(Path(__file__).parent.parent)

from Logic.Reporting.Abstract_reporting import abstract_reporting


class MD_reporting(abstract_reporting):

    def __init__(self, data_examp: list):
        super().__init__(data_examp)
    
    def load(self, name: str, result):
        return super().load(name, result)

    def __dict_to_str(self, inp_dict: dict):
        return super().dict_to_str(inp_dict)



    def create(self, value):


        #берём ключи
        keys=super().get_fields(value)


        result_md="|"



        #Разделение шапки и ячеек
        bottom_line='|'


        #шапка таблицы
        for cur_key in keys:
            result_md+=cur_key+'|'
            bottom_line+='-'*len(cur_key)+'|'
        
        
        result_md+='\n'+bottom_line+'\n'
        




        #добавляем значения
        for cur_val in self.data[value]:

            result_md+='|'
            for cur_key in keys:
                cur_atr=getattr(cur_val,cur_key)
                if isinstance(cur_atr,dict):
                    result_md+=str(self.__dict_to_str(cur_atr))+'|'
                else:
                    result_md+=str(cur_atr)+'|'
            
            result_md+='\n'
        

        #self.hidden_settings.Report_format["CSV"]=result_csv

        self.load('md',result_md)


        return result_md
        