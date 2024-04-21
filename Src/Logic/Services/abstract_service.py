from abc import ABC
from exceptions import argument_exception
from Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent, 'Src'))


class abstract_sevice(ABC):

    __data = []
    # конструктор

    def __init__(self, data: list):
        if len(data) == 0:
            raise argument_exception("Wrong argument")
        self.__data = data

    def handle_event(self, handle_type: str):
        if not isinstance(handle_type, str):
            raise argument_exception("Неверный тип аргумента")
        pass
