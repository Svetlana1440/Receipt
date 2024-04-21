from abc import ABC
from Storage.storage_journal_transaction import storage_journal_transaction
from Storage.storage_journal_row import storage_journal_row
from Storage.storage_factory import storage_factory
from Models.reciepe_model import reciepe_model
from Models.nomenclature_group_model import nomenclature_group_model
from Models.range_model import range_model
from Models.nomenclature_model import nomenclature_model
from Storage.storage_turn_model import storage_turn_model
from Logic.process_factory import process_factory
from exceptions import argument_exception
from Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from Logic.storage_prototype import storage_prototype
from settings import settings
from Storage.storage import storage
from error_proxy import error_proxy
from pathlib import Path
from datetime import datetime
import os
import json
import uuid
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
