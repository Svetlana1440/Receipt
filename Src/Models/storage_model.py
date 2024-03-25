from Src.reference import reference
from Src.exceptions import exception_proxy

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