from Src.Logics.processing import processing
from Src.Logics.turn_processing import turn_processing
from Src.exceptions import exception_proxy, argument_exception, operation_exception
from Src.Logics.debit_processing import debit_processing

#
# Фабрика процессов обработки складских транзакций
#
class process_factory:
    __maps = {}

    def __init__(self) -> None:
       self.__build_structure()

    def __build_structure(self):
        """
            Сформировать структуру
        """
        self.__maps[ process_factory.turn_key()]  = turn_processing
        self.__maps[ process_factory.debit_key()] = debit_processing
        
    
    def create(self, process_key:str) -> processing:
        """
            Подобрать нужный процессинг
        Args:
            process_key (str): Ключ
            data (list[storage_row_model]): Исходные данные
        Returns:
            processing: нужный процессинг
        """
        exception_proxy.validate(process_key , str)
        if process_key not in self.__maps.keys():
            raise argument_exception(f"Указанный процесс {process_key} не реализован!")
        
        current_processing = self.__maps[process_key]
        if current_processing is None:
            raise operation_exception("Некорректно сконфигурирована текущая фабрика!")
      
        return current_processing
    
    # Статические методы
        
    @staticmethod
    def turn_key() -> str:
        """
            Сформировать обороты
        Returns:
            str: _description_
        """
        return "turns"  
    
    def debit_key() -> str:
        """
            Сформировать проводки списания
        Returns:
            str: _description_
        """
        return "debits"  
    
      
    # Код взят: https://github.com/UpTechCompany/GitExample/blob/6665bc70c4933da12f07c0a0d7a4fc638c157c40/storage/storage.py#L30
    
    @staticmethod
    def process_keys(cls):
        """
            Получить список ключей
        Returns:
            _type_: _description_
        """
        keys = []
        methods = [getattr(cls, method) for method in dir(cls) if callable(getattr(cls, method))]
        for method in methods:
            if method.__name__.endswith("_key") and callable(method):
                keys.append(method())
        return keys