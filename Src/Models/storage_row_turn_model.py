from Src.reference import reference
from Src.exceptions import exception_proxy, argument_exception
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.storage_model import storage_model
from Src.Models.unit_model import unit_model

#
# Модель складского оборота
#
class storage_row_turn_model(reference):
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
    
        
    def storage(self) -> storage_model:
        """
            Склад
        Returns:
            storage_model: _description_
        """
        return self._storage
    
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
        
    @staticmethod
    def create(nomenclature  : nomenclature_model, storage: storage_model, unit: unit_model) -> reference:
        """
            Фабричный метод для создания складского оборота
        Args:
            nomenclature (nomenclature_model): _description_
            storage (storage_model): _description_
            unit (unit_model): _description_

        Returns:
            storage_row_turn_model: _description_
        """
        row = storage_row_turn_model("-")
        row.storage = storage
        row.unit = unit
        row.nomenclature = nomenclature
        
        return row 