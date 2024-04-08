import abc
from Src.errors import error_proxy
from Src.exceptions import argument_exception

#
# Абстрактный класс для наследования.
# Используется для реализации различных процессов обработки данных по складским транзакциям
#
class processing(error_proxy):
    
    @abc.abstractmethod
    def process(self, transactions: list) -> list:
        """
            Выполнить процесс обработки списка транзакций
        Args:
            source (_type_): Любой тип данных
        """
        
        if transactions == None:
            raise argument_exception("Некорректно передан параметр!")
        
        if len(transactions) == 0:
            raise argument_exception("Некорректно передан параметр!")
        
        self.clear()