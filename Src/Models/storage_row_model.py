from random import randrange

from Src.exceptions import argument_exception, exception_proxy, operation_exception
from Src.reference import reference
from Src.Models.storage_model import storage_model
from Src.Models.storage_row_turn_model import storage_row_turn_model
from Src.Storage.storage import storage
from datetime import datetime, timedelta
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model

#
# Модель складской проводки
#
class storage_row_model(reference):
    # Тип складской проводки
    _storage_type: bool = False
    # Период
    _period : datetime
     # Номенклатура
    _nomenclature: nomenclature_model = None
    # Склад
    _storage: storage_model = None
    # Единица измерений
    _unit: unit_model = None
    # Значение
    _value: float = 0
    
    
    @property
    def value(self) -> float:
        """
            Значение
        Returns:
            float: _description_
        """
        return self._value
    
    @value.setter
    def value(self, value: float) -> float:
        """
            Значение
        Args:
            value (float): _description_

        Raises:
            argument_exception: _description_

        Returns:
            float: _description_
        """
        exception_proxy.validate(value, (float, int))
        if value <= 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self._value = value

    @property
    def nomenclature(self) -> nomenclature_model:
        """
            Номенклатура
        Returns:
            nomenclature_model: _description_
        """
        return self._nomenclature
    
    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model) -> nomenclature_model:
        """
            Номенклатура
        Args:
            value (nomenclature_model): _description_
        """
        exception_proxy.validate(value, nomenclature_model)
        self._nomenclature = value
        
    
    @property    
    def unit(self) -> unit_model:
        """
            Единица измерения
        Returns:
            unit_model: _description_
        """
        return self._unit
    
    @unit.setter
    def unit(self, value: unit_model) -> unit_model:
        """
            Единица измерения
        Args:
            value (unit_model): _description_

        Returns:
            unit_model: _description_
        """
        exception_proxy.validate(value, unit_model)
        self._unit = value
    
    @property    
    def storage(self) -> storage_model:
        """
            Склад
        Returns:
            storage_model: _description_
        """
        return self._storage
    
    @storage.setter
    def storage(self, value: storage_model) -> storage_model:
        """
            Склад
        Args:
            value (storage_model): _description_

        Returns:
            storage_model: _description_
        """
        exception_proxy.validate(value, storage_model)
        self._storage = value
    
    @property
    def storage_type(self) -> bool:
        """
            Тип складской проводки (True - приход, False - расход)
        Returns:
            bool: _description_
        """
        return self._storage_type
    
    @storage_type.setter
    def storage_type(self, value) -> bool:
        """
            Тип складской проводки (True - приход, False - расход)
        Args:
            value (_type_): _description_

        Raises:
            argument_exception: _description_

        Returns:
            bool: _description_
        """
        if isinstance(value, int):
            self._storage_type = True if value > 0 else False
            
        elif isinstance(value, bool):
            self._storage_type = value
            
        else:
            raise argument_exception("Некорректно переданы параметры!")
        
    @property    
    def period(self) -> datetime:
        """
            Дата транзакции
        Returns:
            datetime: _description_
        """
        return self._period
    
    @period.setter
    def period(self, value: datetime) -> datetime:
        """
            Дата транзакции
        """             
        exception_proxy.validate(value, datetime)
        self._period = value
        
        
    def load(self, source: dict):
        """
            Десериализовать свойства 
        Args:
            source (dict): исходный слова
        """
        if source is None:
            return None
        super().load(source)
        
        source_fields = ["period", "storage_type",  "nomenclature", "value", "unit", "storage"  ]
        if set(source_fields).issubset(list(source.keys())) == False:
            raise operation_exception(f"Невозможно загрузить данные в объект {source}!")   
        
        self._value = source["value"]
        self._period =  datetime.strptime(source["period"], "%Y-%m-%d")
        self._nomenclature = nomenclature_model().load( source["nomenclature"])
        self._storage = storage_model().load( source["storage"] )
        self._unit = unit_model().load( source["unit"])
        self._storage_type = source["storage_type"]
        
        return self
        
    # Фабричные методы    
        
    @staticmethod    
    def create_credit_row(nomenclature_name: str, quantity, unit_name: str, data: dict, _storage: storage_model) -> reference:
        """
            Фабричный метод для создания транзакции на поступление
            Используется в start_factory
        Args:
            nomenclature_name (str): Наименование номенклатуры
            quantity(int, float): Количество
            unit_name (str): Наименование единицы измерения
            data (dict): исходный набор данных
            storage(storage_model): склад
        Returns:
            reference: _description_
        """
        exception_proxy.validate(nomenclature_name, str)
        exception_proxy.validate(_storage, storage_model)
        exception_proxy.validate(quantity, (int, float))
        exception_proxy.validate(unit_name, str)
        
        
        # Определим номенклатуру
        items = data[ storage.nomenclature_key() ]    
        nomenclatures = reference.create_dictionary(items)
        nomenclature = nomenclature_model.get( nomenclature_name, nomenclatures)

        # Определяем единицу измерения
        items = data[ storage.unit_key()]
        units = reference.create_dictionary(items)
        unit = unit_model.get(unit_name, units )
        
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-02-01", "%Y-%m-%d")

        # Создаем транзакцию
        item = storage_row_model("sample_credit_transaction")
        item.nomenclature = nomenclature
        item.unit = unit
        item.storage_type = True
        item.value = quantity
        item.storage = _storage
        item.period = storage_row_model.random_date(start_date, stop_date)
        
        return item
    
    # Источник https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    @staticmethod
    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
            
        
    
    
    

