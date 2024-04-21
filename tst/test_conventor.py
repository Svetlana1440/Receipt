import unittest
from Logic.start_factory import start_factory
from Storage.storage import storage
from error_proxy import error_proxy
from settings_manager import settings_manager
from Models.range_model import range_model
from Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from Logic.Reporting.Json_convert.date_time_convertor import date_time_conventor
from Logic.Reporting.Json_convert.basic_conventor import basic_conventor
import json
from pathlib import Path
import os
import sys
from datetime import date, datetime
from uuid import uuid4
sys.path.append(os.path.join(Path(__file__).parent.parent, 'Src'))


class test_convert(unittest.TestCase):

    def test_convert_int(self):
        # подготовка
        conv = basic_conventor()
        name = 'exmaple'
        value = 1234567

        # действие
        item = conv.convert(name, value)
        print(item)

        # проверка
        assert isinstance(item, dict)
        assert name in list(item.keys())
        assert str(value) in list(item.values())

    def test_convert_str(self):
        # подготовка
        conv = basic_conventor()
        name = 'exmaple'
        value = '1232aswdaedwsed'

        # действие
        item = conv.convert(name, value)
        print(item)

        # проверка
        assert isinstance(item, dict)
        assert name in list(item.keys())
        assert str(value) in list(item.values())

    def test_convert_uuid(self):
        # подготовка
        conv = basic_conventor()
        name = 'exmaple'
        value = uuid4().hex

        # действие
        item = conv.convert(name, value)
        print(item)

        # проверка
        assert isinstance(item, dict)
        assert name in list(item.keys())
        assert str(value) in list(item.values())

    def test_convert_date(self):
        # подготовка
        conv = date_time_conventor()
        name = 'exmaple'
        value = datetime.now()

        # действие
        item = conv.convert(name, value)
        print(item)

        # проверка
        assert isinstance(item, dict)
        assert name in list(item.keys())
        assert "%s-%s-%s" % (value.day, value.month,
                             value.year) in list(item.values())

    def test_convert_range_model(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()

        item = reference_conventor(
            type(factory.storage.data[storage.unit_key()][0]), type(error_proxy()))

        # Действие
        res = item.convert(factory.storage.data[storage.unit_key()][0])
        print(res)
        assert isinstance(res, dict)

    def test_convert_nomenclature(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = reference_conventor(type(factory.storage.data[storage.nomenclature_key()][0]), type(error_proxy()), type(
            factory.storage.data[storage.group_key()][0]), type(factory.storage.data[storage.unit_key()][0]))

        # Действие
        res = item.convert(factory.storage.data[storage.nomenclature_key()][0])
        print(res)
        assert isinstance(res, dict)

    def test_convert_nomenclature_group(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)

        factory.create()
        item = reference_conventor(type(factory.storage.data[storage.nomenclature_key()][0]), type(error_proxy()), type(
            factory.storage.data[storage.group_key()][0]), type(factory.storage.data[storage.unit_key()][0]))

        # Действие
        res = item.convert(factory.storage.data[storage.group_key()][0])

        print(res)

        assert isinstance(res, dict)

    def test_convert_reciepe(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()

        print(type(list((factory.storage.data[storage.reciepe_key(
        )][0].ingridient_proportions).values())[0][2]))
        item = reference_conventor(type(error_proxy()), range_model)

        # Действие
        # конвертируем рецепт
        res = item.convert(factory.storage.data[storage.reciepe_key()][0])
        print(res)
        with open(Path(__file__).parent.parent/'Json.json', 'w') as source:
            json.dump(res, source)
        assert isinstance(res, dict)
