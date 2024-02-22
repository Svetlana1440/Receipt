from Src.reference import reference
from Src.exceptions import exception_proxy, argument_exception

#
# Модель единицы измерения для номенклатуры
#
class unit_model(reference):
    
    # Базовая единица измерения
    __base_unit: reference = None
    
    # Коэффициент пересчета к базовой единице измерения
    __coefficient: int = 1
    
    def __init__(self, name: str, base: reference = None, coeff: int = 1 ):
        super().__init__(name)
        
        if base != None:
            self.base_unit = base
            
        if coeff != 1:
            self.coefficient = coeff   
        
    
    @property
    def base_unit(self):
        """
            Базовая единица измерения
        Returns:
            _type_: _description_
        """
        return self.__base_unit
    
    
    @base_unit.setter
    def base_unit(self, value: reference ):
        exception_proxy.validate(value, reference)
        self.__base_unit = value
        
    
    @property    
    def coefficient(self):
        """
            Коэффициент пересчета
        Returns:
            _type_: _description_
        """
        return self.__coefficient
    
    @coefficient.setter
    def   coefficient(self, value:int):
        exception_proxy.validate(value, int)
        
        if(value <= 0):
            raise argument_exception("Значение коэффициента должно быть > 1!")
        
        self.__coefficient = value  
        
        
    @staticmethod    
    def create_gram():
        """
            Создать единицу измерения грамм

        Returns:
            _type_: _description_
        """
        item = unit_model("грамм", None, 1)
        return item    
    
    @staticmethod
    def create_killogram():
        """
            Создать единицу килограмм
        Returns:
            _type_: _description_
        """
        base = unit_model.create_gram()
        item = unit_model("киллограмм", base, 1000)
        return item

    @staticmethod
    def create_amount():
        """
            Создать единицу штука
        Returns:
            _type_: _description_
        """
        item = unit_model("штука")
        
        return item
    
    @staticmethod
    def create_milliliter():
        """
            Создать единицу миллилитр
        Returns:
            _type_: _description_
        """
        item = unit_model("миллилитр", None, 1)
        return item
    
    @staticmethod
    def create_liter():
        """
            Создать единицу литр
        Returns:
            _type_: _description_
        """
        base = unit_model.create_milliliter()
        item = unit_model("литр", base, 1000)
        return item
        
        
        
        
        
        
    
    