from Src.Logics.start_factory import start_factory
from Src.Logics.convert_factory import convert_factory
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.receipe_model import receipe_model
from Src.Storage.storage import storage
from Src.settings_manager import settings_manager

import unittest
import json

class convert_test(unittest.TestCase):

    #
    # Проверить загрузку одного элемента номенклатуры в объект
    #
    def test_check_load_nomenclature(self):
        try:
            with open("nomenclature_deserialize.json", "r") as read_file:
                # Подготовка
                source = json.load(read_file) 
                nomenclature = nomenclature_model()
                
                # Действие
                result = nomenclature.load(source)
                
                # Проверки
                assert result is not None
                assert result.id == "8446fdc4ce4441d8b1dcaeedb6a676c4"
                    
        except Exception as ex:
            raise Exception(f"Ошибка: {ex}")   
        
    #
    # Проверить загрузку элемента рецепта в объект
    #      
    def test_check_load_receipt(self):
        try:
            with open("receipt_deserialize.json", "r") as read_file:
                # Подготовка
                source = json.load(read_file) 
                receipt = receipe_model()
                
                # Действие
                result = receipt.load(source)
                
                # Проверки
                assert result is not None
                assert len(result.consist) > 0
                    
        except Exception as ex:
            raise Exception(f"Ошибка: {ex}")       

    #
    # Проверить формирование словаря и преобразование в json номенклатуры
    #
    def test_check_serialize_nomenclature(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()
        if len(items) == 0:
            raise Exception("Список номенклатуры пуст!")
        
        item = items[0]
        
        # Действие
        result = factory.serialize(item)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("nomenclature.json", "w")
        file.write(json_text)
        file.close()
        
    #
    # Проверить формирование словаря по списку номенклатуры и конвертацию в json
    #
    def test_check_serialize_nomenctalures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()
        
        # Действие
        result = factory.serialize(items)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("nomenclatures.json", "w")
        file.write(json_text)
        file.close()
            
    #
    # Проверить формирование словаря по списку рецептов и конвертация в json
    #        
    def test_check_serialize_receipts(self):
        # Подготовка
        items = start_factory.create_receipts()
        factory = convert_factory()
        
        # Действие
        result = factory.serialize(items)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("receipts.json", "w")
        file.write(json_text)
        file.close()
                
    #
    # Выгрузить один рецепт
    #            
    def test_check_serialize_receipt(self):
        # Подготовка
        options = settings_manager()
        start = start_factory(  options.settings )
        start.create()
        factory = convert_factory()
        items = start.storage.data[ storage.receipt_key() ]
        if len(items) == 0:
            raise Exception("Набор рецептов пуст!")
        item = items[0]
        
        # Действие
        result = factory.serialize(item)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("receipt_deserialize.json", "w")
        file.write(json_text)
        file.close()        

    #
    # Выгрузить одну транзакцию
    #    
    def test_check_serialize_transaction(self):
        # Подготовка
        options = settings_manager()
        start = start_factory(  options.settings )
        start.create()
        factory = convert_factory()
        items = start.storage.data[ storage.storage_transaction_key() ]
        if len(items) == 0:
            raise Exception("Набор транзакций пуст!")
        item = items[0]
        
        # Действие
        result = factory.serialize(item)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("transaction_deserialize.json", "w")
        file.write(json_text)
        file.close()        
