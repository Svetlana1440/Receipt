from pathlib import Path
import os
import sys
from abc import ABC
from settings import settings
from exceptions import argument_exception
sys.path.append(Path(__file__).parent.parent)


class abstract_reporting(ABC):
    # инкапсуляция настроек
    __settings = None

    # Данные из start_factory
    __data = {}

    def __init__(self, data_examp: list):
        self.data = data_examp

    @property
    def data(self):
        return self.__data

    # сеттер
    @data.setter
    def data(self, value: dict):
        if not isinstance(value, dict):
            raise argument_exception("Неверный аргумент")
        self.__data = value

    @property
    def hidden_settings(self):
        return self.__settings

    @hidden_settings.setter
    def hidden_settings(self, value: settings):
        if not isinstance(value, settings):
            raise argument_exception("Неверный аргумент")

        self.__settings = value

    def create(self, value: str):
        return "string"

    def get_fields(self, value: str):
        if not isinstance(value, str):
            raise argument_exception("Неверный аргумент")
        fields = list(filter(lambda x: not x.startswith("_") and not x.startswith(
            'create_'), dir(self.data[value][0].__class__)))
        print(fields)

        return fields

    def dict_to_str(self, inp_dict: dict):
        result = {}
        for key in list(inp_dict.keys()):
            if isinstance(inp_dict[key], dict):
                result[str(key)] = self.dict_to_str(inp_dict[key])
            else:
                result[str(key)] = str(inp_dict[key])

        return result

    # выгрузка в файл
    def load(self, name: str, result):
        with open(Path(__file__).parent.parent.parent.parent/f'report.{name}', 'w') as loader:
            loader.write(result)
