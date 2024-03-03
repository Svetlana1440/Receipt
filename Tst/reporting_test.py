import unittest
from Src.Logics.reporting import reporting
from Src.Models.unit_model import unit_model
from Src.Storage.storage import storage
from Src.Logics.csv_reporting import csv_reporting
from Src.settings_manager import settings_manager



class reporting_test(unittest.TestCase):
    def test_check_reporting_build(self):
        #Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        data[storage.unit_key()] = list

        #Действие
        result = reporting.build(storage.unit_key(), data)

        #Проверки
        assert result is not None 
        assert len(result) > 0 

#Проверка формирования отчетности
    def test_check_csv_create(self):
        #Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        item1 = unit_model.create_killogram()
        manager = settings_manager()
        list.append(item)
        list.append(item1)
        data[storage.unit_key()] = list
        report = csv_reporting(manager.settings, data)

        # действие
        result = report.create( storage.unit_key())
        print('')
        print(result)
        # Проверка
        assert result is not None
        assert len(result) > 0




