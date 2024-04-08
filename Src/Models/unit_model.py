from Src.reference import reference
from Src.exceptions import exception_proxy, argument_exception, operation_exception



#
# Модель единицы измерения для номенклатуры
#
class unit_model(reference):
    
    # Базовая единица измерения
    __base_unit: reference = None
    
    # Коэффициент пересчета к базовой единице измерения
    __coefficient: int = 1
    
    def __init__(self, name: str = None, base: reference = None, coeff: int = 1 ):
        super().__init__(name)
        
        if base != None:
            self.base_unit = base
            
        if coeff != 1:
            self.coefficient = coeff   
        
    
    @property
    def base_unit(self) -> reference:
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
    def coefficient(self) -> int:
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
        
    def load(self, source: dict):
        """
            Загрузить данные
        Args:
            source (dict): исходный словарь

        """
        super().load(source)
        if source is None:
            return None
        
        source_fields = ["coefficient", "base_unit"]
        if set(source_fields).issubset(list(source.keys())) == False:
            raise operation_exception(f"Невозможно загрузить данные в объект {source}!")
        
        self.__coefficient = source["coefficient"]
        self.__base_unit = unit_model().load(source["base_unit"])
            
        return self    
             
        
        
    # Фабричные методы    
        
    @staticmethod    
    def create_gram():
        """
            Создать единицу измерения - грамм

        Returns:
            _type_: _description_
        """
        item = unit_model("грамм", None, 1)
        return item    
    
    @staticmethod
    def create_killogram():
        """
            Создать единицу измерения - киллограмм
        Returns:
            _type_: _description_
        """
        base = unit_model.create_gram()
        item = unit_model("киллограмм", base, 1000)
        return item
    
    @staticmethod
    def create_ting():
        """
            Создать единицу изменения - штуки
        Returns:
            _type_: _description_
        """
        return unit_model("штука")
    
    def create_milliliter():
        """
            Создать единицу измерения - миллилитр
        Returns:
            _type_: _description_
        """
        return unit_model("миллилитр")
    
    def create_liter():
        """
            Создать единицу измерения - литр
        Returns:
            _type_: _description_
        """
        base = unit_model.create_milliliter()
        item = unit_model("литр", base, 1000)
        return item
    
    
    @staticmethod
    def get(unit_name: str, units: dict):
        """
            Получить значение элемента единицы измерения из словаря
        Args:
            nomenclature_name (str): наименование
            nomenclatures (dict): исходный словарь storage.data

        Returns:
            nomenclature_model: _description_
        """
        exception_proxy.validate(unit_name, str)
        
        keys = list(filter(lambda x: x == unit_name, units.keys() ))
        if len(keys) == 0:
            raise operation_exception(f"Некоректно передан список. Не найдена номенклатура {unit_name}!")
                
        return units[keys[0]]
  
    

        
        
        
        
        
        
    
    