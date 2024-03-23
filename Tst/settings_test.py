from Src.settings_manager import settings_manager 
import unittest


#
# Набор автотестов для проверки работы модуmeля настроек
#
class settings_test(unittest.TestCase):
    
 
    
    #
    # Проверить на корректность создания и загрузки файла с настройками
    #
    def test_create_app_settings(self):
        # Подготовка
        manager = settings_manager()

        # Действие
        result = manager.data

        # Проверки
        print(manager.data)
        print(type(manager.data))
        assert result is not None
        assert manager.settings.inn > 0
        assert manager.settings.short_name != ""
        
    #
    # Проверить тип создания объекта как singletone
    #    
    def test_double_create_app_setting(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        # Действие
        
        # Проверки
        print(manager1._uniqueNumber)
        print(manager2._uniqueNumber)
        assert manager1._uniqueNumber == manager2._uniqueNumber
        
    #
    # Проверить работу менеджера загрузки настроек при не корректном файле настроек
    #    
    def test_fail_open_settings(self):
        # Подготовка
        manager = settings_manager()
        
        # Действие
        manager.open("test.json")
        
        # Проверки
        assert manager.error.is_empty == False
        
        
            

        

 

