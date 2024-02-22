from Src.exceptions import exception_proxy

#
# Класс для описания настроек
#
class settings():
    _inn = 0
    _short_name = ""
    _first_start = True
    
    
    @property
    def inn(self):
        """
            ИНН
        Returns:
            int: 
        """
        return self._inn
    
    @inn.setter
    def inn(self, value: int):
        exception_proxy.validate(value, int)
        self._inn = value
         
    @property     
    def short_name(self):
        """
            Короткое наименование организации
        Returns:
            str:
        """
        return self._short_name
    
    @short_name.setter
    def short_name(self, value:str):
        exception_proxy.validate(value, str)
        self._short_name = value
        
        
    @property    
    def is_first_start(self):
        """
           Флаг Первый старт
        """
        return self._first_start    
            
    @is_first_start.setter        
    def is_first_start(self, value: bool):
        self._first_start = value
    