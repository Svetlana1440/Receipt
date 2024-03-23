from Src.errors import error_proxy

# Набор классов для генерации собственных исключений

#
# Абстрактный класс для наследования
#
class exception_proxy(Exception):
    _error : error_proxy = error_proxy()
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self._error.set_error(self)
        
    @property    
    def error(self):
        """
            Информация об ошибке
        Returns:
            _type_: _description_
        """
        return self._error    
    
    # -> Источник: https://github.com/zhbr112/Restaurant-automation/blob/b2db73872c4c126155ad52b82db79223943aca29/src/abstract_reference.py#L16
    
    @staticmethod
    def validate( value, type_, len_= None):
        """
            Валидация аргумента по типу и длине
        Args:
            value (any): Аргумент
            type_ (object): Ожидаемый тип
            len_ (int): Максимальная длина
        Raises:
            arguent_exception: Некорректный тип
            arguent_exception: Неулевая длина
            arguent_exception: Некорректная длина аргумента
        Returns:
            True или Exception
        """
        
        if value is None:
            raise argument_exception("Пустой аргумент")

        # Проверка типа
        if not isinstance(value, type_):
            raise argument_exception("Некорректный тип")

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            raise argument_exception("Пустой аргумент")

        if len_ is not None and len(str(value).strip()) >= len_:
            raise argument_exception("Некорректная длина аргумента")

        return True
     
   
         
     
#
# Исключение при проверки аргументов
#     
class argument_exception(exception_proxy):
    pass     
    
#
# Исключение при выполнении операции
#    
class operation_exception(exception_proxy):
    pass    
    