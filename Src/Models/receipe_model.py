from Src.reference import reference
from Src.Models.receipe_row_model import receipe_row_model
from Src.exceptions import exception_proxy , operation_exception, argument_exception
from Src.Models.nomenclature_model import nomenclature_model

#
# Класс описание рецепта приготовления блюда
#
class receipe_model(reference):
    # Вес брутто
    _brutto: int = 0
    
    # Вес нетто
    _netto: int = 0

    # Состав рецепта
    _rows = {}
    
    # Инструкции
    _instructions = list()
    
    # Описание
    _comments: str = ""
    
    def __init__(self, name = None):
        super().__init__(name)
        self._rows = {}
        self._instructions = []
        self._brutto = 0
            
    def add(self, row: receipe_row_model):
        """
            Добавить/ изменить состав блюда
        Args:
            row (receipe_row_model): _description_
        """
        exception_proxy.validate(row, receipe_row_model)
        self._rows[row.name] = row
        self.__calc_brutto()
        
    def delete(self, row: receipe_row_model):
        """
            Удалить из состава блюда
        Args:
            row (receipe_row_model): _description_
        """
        exception_proxy.validate(row, receipe_row_model)
        
        if row.name in self._rows.keys():
            self._rows.pop(row.name)
            
        self.__calc_brutto()    
        
    def __calc_brutto(self):
        """
            Перерасчет брутто
        """
        self._brutto = 0
        for position  in self._rows:
            # Получаем свойство size
            self._brutto += self._rows[position].size 
            
    @property     
    def brutto(self) -> int:
        """
            Вес брутто
        Returns:
            int : _description_
        """
        return self._brutto
    
    @brutto.setter
    def brutto(self, value: int):
        exception_proxy.validate(value, int)
        self._brutto = value     
            
    @property         
    def netto(self) -> int:
        return self._netto                        
        
    @netto.setter
    def netto(self, value: int):
        """
            Вес нетто
        Args:
            value (int): _description_
        """
        exception_proxy.validate(value, int)
        
        self._netto = value
        
    @property    
    def instructions(self) -> list:
        """
           Инструкции для приготовления
        Returns:
            _type_: _description_
        """
        return self._instructions  
    
    @property
    def comments(self) -> str:
        return self._comments
    
      
    @comments.setter
    def comments(self, value: str):
        """
            Описание блюда
        Args:
            value (str): _description_
        """
        exception_proxy.validate(value, str)
        self._comments = value   
        
    @property            
    def consist(self) -> list:
        """
            Состав рецепта
        Returns:
            _type_: _description_
        """
        return self._rows    
    
    def rows(self) -> list:
        """
            Получить состав рецепта (read only)
        Returns:
            _type_: _description_
        """
        result = []
        for key in self._rows.keys():
            result.append( self._rows[key] )
            
        return result
    
    def load(self,  source: dict):
        """
            Загрузить данные из словаря
        Args:
            source (dict): исходный словарь

        """
        super().load(source)
        if source is None:
            return None
        
        source_fields = ["comments", "consist", "instructions","netto", "brutto"]
        if set(source_fields).issubset(list(source.keys())) == False:
            raise operation_exception(f"Невозможно загрузить данные в объект {source}!")
        
        self._netto = source["netto"]
        self._brutto = source["brutto"]
        
        # Загрузим состав
        for item in source["consist"].items():
            row = item[1]
            if row is not None:
                value = receipe_row_model().load(row)
                self.add(value)
            
        # Загрузим инструкции
        self._instructions = source["instructions"]
        return self
            
    
    
    @staticmethod
    def create_receipt(name: str, comments: str, items: list, data: list):
        """
            Фабричный метод. Сформировать рецепт
        Args:
            name (str): Наименование рецепта
            comments (str): Приготовление
            items (list): Состав рецепта
            data (list): Список номенклатуры

        Returns:
            receipe_model: _description_
        """
        exception_proxy.validate(name, str)
        if len(items) == 0:
            raise argument_exception(f"Некорректно передан параметр {items}. Список пуст!")
        
        
        # Подготовим словарь со списком номенклатуры
        nomenclatures = reference.create_dictionary(data)    
        receipt = receipe_model(name)
        if comments != "":
            receipt.comments = comments    
        
        for position in items:
            
            if len(position) < 2:
                raise operation_exception("Невозможно сформировать элементы рецепта! Некорректный список исходных элементов!")
            
            nomenclature_name = position[0]
            size = position[1]            
            nomenclature = nomenclature_model.get( nomenclature_name, nomenclatures )
            
            # Определяем единицу измерения
            if nomenclature.unit.base_unit is None:
                unit = nomenclature.unit
            else:
                unit = nomenclature.unit.base_unit    
            
            # Создаем запись в рецепте
            row = receipe_row_model()
            row.nomenclature = nomenclature
            row.size = size
            row.unit = unit
            receipt.add(row)
        
        return receipt