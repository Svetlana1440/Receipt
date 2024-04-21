import unittest
from Logic.Services.storage_sevice import storage_service
from Logic.start_factory import start_factory
from Storage.storage import storage
from datetime import datetime
from settings_manager import settings_manager
from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent, 'Src'))


class test_sevice(unittest.TestCase):

    # проверка работ получения оборота
    def test_check_get_block_turns(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        factory = start_factory(unit.settings)
        factory.create()

        key = storage.journal_key()
        service = storage_service(factory.storage.data[key])
        service.options = unit.settings

        # действие
        res = service.create_blocked_turns()

        # проверка
        assert res is not None
        assert len(res) > 0
        assert res[0].storage_id == factory.storage.data[storage.b_turn_key()
                                                         ][0].storage_id

    def test_check_date_turns(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        unit.settings.block_period = "2024-1-1"
        factory = start_factory(unit.settings)

        factory.create()

        key = storage.journal_key()
        sevice = storage_service(factory.storage.data[key])
        sevice.options = unit.settings

        # дейсвтие
        sevice.create_blocked_turns()
        res = sevice.create_turns(datetime(2022, 1, 1), datetime(2024, 1, 2))

        # проверка
        print(res)
        assert res is not None
        assert len(res) > 0

    def test_check_date_turns_nom(self):
        # Подготовка
        unit = settings_manager()
        address = os.path.join(Path(__file__).parent.parent, 'Jsons')
        unit.open('Test.json', address)
        unit.settings.block_period = "2024-1-1"
        factory = start_factory(unit.settings)
        factory.create()

        key = storage.journal_key()
        sevice = storage_service(factory.storage.data[key])
        sevice.options = unit.settings

        # действие
        sevice.create_blocked_turns()
        res = sevice.create_turns_by_nomenclature(datetime(2022, 1, 1), datetime(
            2024, 1, 2), factory.storage.data[storage.nomenclature_key()][4].id)

        # проверка
        print(res)
        assert res is not None
        assert len(res) > 0
