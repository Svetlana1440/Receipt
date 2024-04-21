import unittest
from Logic.report_factory import report_factory
from settings_manager import settings_manager
from Models.range_model import range_model
from Logic.start_factory import start_factory
from Storage.storage import storage
from pathlib import Path
import os
import sys
sys.path.append(os.path.join(Path(__file__).parent.parent, 'Src'))


class test_factory(unittest.TestCase):
    def test_check_first_start(self):

        # preparation
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Tester.json', address)
        item = start_factory(unit.settings)

        # action
        check = item.create()

        # check
        if unit.settings.is_first_start == True:

            assert len(check) > 0
            return

        assert not item.storage is None

        assert storage().nomenclature_key() in item.storage.data
        assert storage().unit_key() in item.storage.data
        assert storage().group_key() in item.storage.data
        assert storage().reciepe_key() in item.storage.data

    def test_check_not_first_start(self):
        # preparation
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test1.json', address)
        item = start_factory(unit.settings)

        check = item.create()

        assert item.storage is not None
        assert len(check) == 5

    def test_check_factory_report_create(self):
        # preparation
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        item = start_factory(unit.settings)
        item.create()
        factory = report_factory()

        # action
        result = factory.create("CSV", item.storage.data, storage.unit_key())
        print(result)
        assert result is not None

    def test_check_factory_report_create_MD(self):
        # preparation
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        item = start_factory(unit.settings)
        item.create()
        factory = report_factory()

        # action
        result = factory.create("MD", item.storage.data, storage.reciepe_key())
        print(result)
        assert result is not None

    def test_check_factory_report_create_Json(self):
        # preparation
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        item = start_factory(unit.settings)
        item.create()
        factory = report_factory()

        # action
        result = factory.create("Json", item.storage.data, storage.unit_key())
        print(result)
        assert result is not None
