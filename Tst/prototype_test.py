from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.start_factory import start_factory
import unittest
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.Logics.storage_service import storage_service
from datetime import datetime

class prototype_test(unittest.TestCase):
    
    
    def test_check_prototype(self):
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
        result = prototype.filter(   start_date, stop_date ) 
        
        # Проверка
        assert isinstance(result, storage_prototype)
        assert prototype.is_empty
        assert len(result) > 0


    def test_check_prototype_nomenclature(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
        prototype = storage_prototype( data)
        id = start.storage.data[storage.nomenclature_key()][0].id
        
        # Дейтсвие
        result = prototype.filter(   start_date, stop_date ) 
        result = result.filter_by_nomenclature(id)
        
        # Проверка
        assert isinstance(result, storage_prototype)
        assert prototype.is_empty


    def test_storage_service(self):
       # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-03-10", "%Y-%m-%d")
        prototype = storage_prototype( data)
        id = start.storage.data[storage.nomenclature_key()][0].id
      
        service = storage_service(data)
        
        # Дейтсвие
        filtered = service.create_turns_by_nomen(start_date, stop_date, id)
        
        # Проверка
        print(filtered)
        assert filtered is not None
        assert len(filtered)>0
        assert isinstance(filtered, list)


    def test_service_transactions(self):
            # Подготовка
            manager = settings_manager()
            start = start_factory(manager.settings)
            start.create()
            key = storage.storage_transaction_key()
            data = start.storage.data[ key ]
            receipt = start.storage.data[storage.receipt_key()][0]
            service = storage_service(data)
            storage_ = data[0].storage
            
            # Дейтсвие
            result = service.create_transactions(receipt, storage_)
            
            # Проверка
            print(result)
            assert len(result) > 0
        



