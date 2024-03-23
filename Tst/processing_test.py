import unittest
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Logics.process_factory import process_factory
from Src.Storage.storage import storage
from Src.Logics.processing import processing

#
# Набор содульных тестов для проверки процессов обработки данных
#
class processing_test(unittest.TestCase):
    
    #
    # Проверить работу фабрики процессов
    # Запустить расчет складских оборотов
    #
    def test_check_process_factory(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = process_factory()

        # Действие
        result = factory.create( process_factory.turn_key() )
        
        # Проверка
        assert result is not None
        
        
    #
    # Проверить работу процесса расчета оборотов
    #    
    def test_check_process_turn(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = process_factory()
        key = storage.storage_transaction_key()
        transactions = start.storage.data[ key ]
        processing = factory.create( process_factory.turn_key() )
        
        # Действие
        result = processing().process(transactions)
        
        # Проверка
        assert result is not None
        assert len(result) > 0   
        turn = list(filter(lambda x: x.nomenclature.name == "Сыр Пармезан", result ))
        assert turn[0].value == 0.5
        
        
    
    
    
   