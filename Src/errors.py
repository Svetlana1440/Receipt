# Набор классов для обработки информации связанной с ошибками

#
# Класс для обработки и хранения текстовой информации об ошибке
#
class error_proxy:
    " Текст с описание ошибки "
    _error_text = ""
    
    def __init__(self, exception: Exception = None):
        if exception is not None:
            self.set_error(exception)
    
    @property
    def error(self):
        """
            Получить текстовое описание ошибки
        Returns:
            str: _description_
        """
        return self._error_text
    
    @error.setter
    def error(self, value: str):
        if value == "":
            raise Exception("Некорректно переданы параметры!")
            
        self._error_text = value
        
    @classmethod
    def set_error(self, exception: Exception):
        """
            Сохранить текстовое описание ошибки из исключения
        Args:
            exception (Exception): входящее исключение
        """
        
        if exception  is None:
            self._error_text = ""
            return
            
        self._error_text = "Ошибка! " + str(exception)    
            
    @property        
    def is_empty(self) -> bool:
        """
            Флаг. Есть ошибка
        Returns:
            bool: _description_
        """
        if len(self._error_text) != 0:
            return False
        else:
            return True         
            