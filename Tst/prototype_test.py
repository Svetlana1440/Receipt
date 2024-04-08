from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.exceptions import operation_exception

from datetime import datetime
import unittest

class prototype_test(unittest.TestCase):
    
    #
    # Проверить метод filter_by_period
    #
    def test_check_filter_by_period(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
        prototype = storage_prototype( data)
        
        
        # Дейтсвие
        result = prototype.filter_by_period( start_date, stop_date ) 
        
        # Проверка
        assert isinstance(result, storage_prototype)
        assert prototype.is_empty == True
        assert len(result.data) > 0
        
    #
    # Проверить метод  filter_by_nomenclature
    #   
    def test_check_filter_by_nomenclature(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        if len(data) == 0:
            raise operation_exception("Данные не подготовлены!")
        
        element = data[0]
        nomenclature = element.nomenclature
        prototype = storage_prototype( data)
        
        # Действие
        result = prototype.filter_by_nomenclature( nomenclature )
        
        # Проверка
        assert isinstance(result, storage_prototype)
        assert prototype.is_empty == True   
        assert len(result.data) > 0    
        
            