import abc
from Src.errors import error_proxy
from Src.exceptions import exception_proxy, argument_exception

# 
# Абстрактный класс для наследования.
# Используется для сериализации и десериализации
#
class convertor(error_proxy):
    
    @abc.abstractmethod
    def serialize(self, field: str, object) -> dict:
        """
            Сериализовать объект в словарь
        Args:
            source (_type_): Любой тип данных
        """
        exception_proxy.validate(field, str)
        self.clear()
        
            
         
        
        
        
        
    
