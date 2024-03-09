from Src.reference import reference
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model
from Src.exceptions import exception_proxy

#
# Класс описание одной строки рецепта
#
class receipe_row_model(reference):
    __nomenclature: nomenclature_model = None
    __size: int = 0
    __unit: unit_model = None
    
    def __init__(self, _nomenclature: nomenclature_model, _size: int, _unit: unit_model):
        """

        Args:
            _nomenclature (nomenclature_model): Объект номенклатура
            _size (int): Размер части
            _unit (unit_model): Объект единица измерения
        """
        exception_proxy.validate(_nomenclature, reference)
        exception_proxy.validate(_unit, reference)
         
        self.__nomenclature = _nomenclature
        self.__size = _size
        self.__unit = _unit
        
        super().__init__( f"{_nomenclature.name} , {_unit.name} ")
    
    @property
    def nomenclature(self):
        """
            Номенклатура
        Returns:
            _type_: _description_
        """
        return self.__nomenclature
    
    
    @property
    def size(self):
        """
            Размер

        Returns:
            _type_: _description_
        """
        return self.__size
    
    
    @size.setter
    def size(self, value: int):
        self.__size = value
    
    
    @property    
    def unit(self):
        """
           Единица измерения

        Returns:
            _type_: _description_
        """
        return self.__unit    
        
    