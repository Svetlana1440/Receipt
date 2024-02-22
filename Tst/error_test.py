from Src.errors import error_proxy 
import unittest

#
# Набор автотестов для проверки работы класса error_proxy
#
class error_proxy_test(unittest.TestCase):
    
    #
    # Проверить простой сбособ  создания объекта с ошибкой
    #
    def test_create_error_proxy(self):
        # Подготовка
        proxy = error_proxy()
        
        # Действие
        proxy.error = "test"
        
        # Проверка
        assert proxy.error == "test"
        
    def test_create_exception_error_proxy(self):
        # Подготовка
        proxy = error_proxy()
        
        try:
            # Действие
            proxy.error = ""
        except Exception as ex:
            proxy.set_error(ex)
            
        # Проверка
        print(proxy.error)
        assert proxy.error != ""    
            
            
    