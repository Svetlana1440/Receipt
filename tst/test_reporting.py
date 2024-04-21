import unittest
from Logic.Reporting.JSON_reporting import Json_reporting
from Logic.Reporting.MD_reporting import MD_reporting
from Logic.Reporting.CSV_reporting import CSV_reporting
from datetime import datetime
from Logic.start_factory import start_factory
from Storage.storage import storage
from settings_manager import settings_manager
from pathlib import Path
import os
import sys
import json

sys.path.append(os.path.join(Path(__file__).parent.parent, 'Src'))


class test_reporting(unittest.TestCase):

    def test_check_take_row_range(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.get_fields(storage.unit_key())
        print(k)

        # Проверка
        assert len(k) == 6

    def test_check_take_row_group(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.get_fields(storage.group_key())
        print(k)

        # Проверка
        assert len(k) == 3

    def test_check_take_row_nomenclature(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.get_fields(storage.nomenclature_key())
        print(k)

        # Проверка
        assert len(k) == 6

    def test_check_take_row_reciepe(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.get_fields(storage.reciepe_key())
        print(k)

        # Проверка
        assert len(k) == 5

    def test_check_to_csv_range(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.unit_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    def test_check_to_csv_group(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.group_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    def test_check_to_csv_nomenclature(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.nomenclature_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    def test_check_to_csv_reciepe(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.reciepe_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    def test_check_to_csv_journal(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()
        item = CSV_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.journal_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    # проверка на перевод в MD единиц измерения

    def test_check_to_MD_range(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = MD_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.unit_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    # проверка на перевод в MD группы номенклатуры

    def test_check_to_MD_group(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = MD_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.group_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    # проверка на перевод в MD номенклатуры

    def test_check_to_MD_nomenclature(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = MD_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.nomenclature_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    # проверка на перевод в MD рецепта

    def test_check_to_MD_reciepe(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = MD_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.reciepe_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    # проверка на перевод в MD журнала
    def test_check_to_MD_journal(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = MD_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.journal_key())
        print(k)

        # Проверка
        assert isinstance(k, str)

    # проверка на перевод в Json единиц измерения

    def test_check_to_Json_range(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = Json_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.unit_key())
        print(k)

        # Проверка
        try:
            json.loads(k)
            assert True == True
            return
        except:
            assert False == True

    # проверка на перевод в Json группы номенклатуры

    def test_check_to_Json_group(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = Json_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.group_key())
        print(k)

        # Проверка
        try:
            json.loads(k)
            assert True == True
            return
        except:
            assert False == True

    # проверка на перевод в Json номенклатуры

    def test_check_to_Json_nomenclature(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = Json_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.nomenclature_key())
        print(k)

        # Проверка
        try:
            json.loads(k)
            assert True == True
            return
        except:
            assert False == True

    # проверка на перевод в Json рецепта

    def test_check_to_Json_reciepe(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = Json_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.reciepe_key())
        print(k)

        # Проверка
        try:
            json.loads(k)
            assert True == True
            return
        except:
            assert False == True

    # проверка на перевод в Json журнала

    def test_check_to_Json_journal(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        factory = start_factory(unit.settings)

        factory.create()

        item = Json_reporting(factory.storage.data)

        # Действие
        k = item.create(storage.journal_key())
        print(k)

        # Проверка
        try:
            json.loads(k)
            assert True == True
            return
        except:
            assert False == True
