from Src.Models.unit_model import unit_model
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.Logics.report_factory import report_factory
import unittest
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Logics.convertor import convertor
from datetime import datetime
from Src.Logics.convert_factory import convert_factory
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.reference_convertor import reference_convertor
from Src.Logics.datetime_convertor import datetime_convertor
#
# Набор автотестов для проверки работы фабричного метода
# 
class factory_test(unittest.TestCase):

    def test_check_report_factory_create(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory( manager.settings )
        start.create()
        factory = report_factory()
        key = storage.unit_key()

        # Действие
        result = factory.create(manager.settings.report_mode, start.storage.data).create(key)

        # Проверка
        assert result is not None
        print(result)
        assert len(result)
        

    #
    # Проверка создания начальных рецептов
    #    
    def test_check_create_receipts(self):
        # Подготовка
        items = start_factory.create_receipts()
        
        # Действие
        
        # Проверки
        assert len(items) > 0     
        
    # 
    # Проверка создание начальной номенклатуры
    #    
    def test_check_create_nomenclatures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        
        # действие
        
        # Прверки
        assert len(items) > 0 
        
        
    #
    # Проверка создание списка единиц измерения
    #    
    def test_check_create_units(self):
        # Подготовка
        items = start_factory.create_units()
        
        # Действие
        
        # Проверки
        assert len(items) > 0    
     
    #
    # Проверка создания списка групп
    # 
    def test_check_create_groups(self):
        # Подготовка
        items = start_factory.create_groups()
        
        # Действие
        
        # Проверки    
        assert len(items) > 0
        
        
    #      
    # Проверка работы класса start_factory. Метод create
    #
    def test_check_factory_create(self):
        # Подготовка
        manager = settings_manager()
        factory = start_factory( manager.settings )
        
        
        # Действие
        result = factory.create()
        
        
        # Проверка
        if manager.settings.is_first_start == False:
            assert result == True
            assert not factory.storage is None
            assert storage.nomenclature_key() in factory.storage.data
            assert storage.receipt_key() in factory.storage.data
            assert storage.group_key() in factory.storage.data
            assert storage.unit_key() in factory.storage.data
        else:
            assert result == False 


    #
    # Проверка конвертора (int, float, str, datetime, reference)
    #   
    def test_check_convertor(self):
        group = group_model("test group")
        nomen = nomenclature_model("test")
        unit = unit_model("test unit")
        date = datetime.now()
        item = unit.create_gram()
        num = 1
        float = 1.34
        str = "123"
        ref = reference_convertor()
        dat = datetime_convertor()
        bas = basic_convertor()
        
        
        res1 = ref.convert(item)
        res2 = ref.convert(nomen)
        res3 = ref.convert(group)
        res4 = ref.convert(unit)
        res5 = dat.convert(date)
        res6 = bas.convert(num)
        res7 = bas.convert(float)
        res8 = bas.convert(str)

        assert len(res1) > 0 and len(res2) > 0 and len(res3) > 0 and len(res4)  > 0 and len(res5) > 0 \
        and len(res6) > 0 and len(res7) > 0 and len(res8) > 0
        print(res4)


    #
    # Проверка фабричного ковертора
    #
    def test_fabric_convertor(self):
        group = group_model("test group")
        nomen = nomenclature_model("test")
        unit = unit_model("test unit")
        date = datetime.now()
        item = unit.create_gram()
        item1 = item.create_killogram()
        num = 1
        float = 1.34
        str = "123"
        con_fact = convert_factory()
        
        
        res1 = con_fact.convert(item)
        res2 = con_fact.convert(nomen)
        res3 = con_fact.convert(group)
        res4 = con_fact.convert(unit)
        res5 = con_fact.convert(date)
        res6 = con_fact.convert(num)
        res7 = con_fact.convert(float)
        res8 = con_fact.convert(str)
        res9 = con_fact.convert(item1)

        assert len(res1) > 0 and len(res2) > 0 and len(res3) > 0 and len(res4)  > 0 and len(res5) > 0 \
        and len(res6) > 0 and len(res7) > 0 and len(res8) > 0
        print(res9)
        