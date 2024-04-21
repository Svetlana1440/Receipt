from Logic.Reporting.Abstract_reporting import abstract_reporting
from pathlib import Path
import os
import sys
from settings import settings
sys.path.append(Path(__file__).parent.parent)


class CSV_reporting(abstract_reporting):

    def __init__(self, data_examp: list):
        super().__init__(data_examp)

    def load(self, name: str, result):
        return super().load(name, result)

    def __dict_to_str(self, inp_dict: dict):
        return super().dict_to_str(inp_dict)

    def create(self, value):

        # берём ключи
        keys = super().get_fields(value)

        result_csv = ""

        # шапка таблицы
        for cur_key in keys:
            result_csv += cur_key+';'

        result_csv = result_csv.strip(';')+'\n'

        # добавляем значения
        for cur_val in self.data[value]:
            for cur_key in keys:
                cur_atr = getattr(cur_val, cur_key)

                # проверяем на словари
                if isinstance(cur_atr, dict):
                    result_csv += str(self.__dict_to_str(cur_atr))+';'
                else:
                    result_csv += str(cur_atr)+';'
            result_csv = result_csv.strip(';')
            result_csv += '\n'

        self.load('csv', result_csv)

        return result_csv
