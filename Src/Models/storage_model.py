from Src.reference import reference
from Src.exceptions import exception_proxy, operation_exception

#
# Модель склада
#
class storage_model(reference):
    _address: str = ""
    
    @property
    def address(self) -> str:
        """
            Адрес

        Returns:
            _type_: _description_
        """
        return self._address
    
    @address.setter
    def address(self, value:str):
        """
            Адрес
        Args:
            value (str): _description_
        """
        exception_proxy.validate(value, str)
        self._address = value
        
         
    def load(self, source: dict):
        """
            Десериализовать свойства 
        Args:
            source (dict): исходный слова
        """
        if source is None:
            return None
        super().load(source)
        
        source_fields = ["address"]
        if set(source_fields).issubset(list(source.keys())) == False:
            raise operation_exception(f"Невозможно загрузить данные в объект {source}!")
        
        self._address = source["address"]
        return self
        
    # Фабричные методы
        
    @staticmethod    
    def create_default() -> reference:
        """
            Сформировать склад по умолчанию
        Returns:
            reference: _description_
        """
        storage = storage_model("default")
        storage.address = "г. Москва. ул. Академика Королева, 10"
        
        return storage    
   