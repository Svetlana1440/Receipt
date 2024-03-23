from Src.reference import reference
from Src.Models.receipe_row_model import receipe_row_model
from Src.exceptions import exception_proxy , operation_exception, argument_exception

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
    
    def  rows_ids(self):
        result = []
        for item in self._rows:
            result.append(item.value.id)
    
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
    def brutto(self):
        """
            Вес брутто
        Returns:
            int : _description_
        """
        return self._brutto
    
    @brutto.setter
    def brutto(self, value: int) -> int:
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
    def instructions(self):
        """
           Инструкции для приготовления
        Returns:
            _type_: _description_
        """
        return self._instructions  
    
    @property
    def comments(self):
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
    
    
    @staticmethod
    def create_receipt(name: str, comments: str, items: list, data: list):
        """
            Фабричный метод. Сформировать рецепт
        Args:
            name (str): Наименование рецепта
            comments (str): Приготовление
            items (list): Состав рецепта
            data (list): Список номенклатуры
        Raises:
            operation_exception: _description_
            operation_exception: _description_

        Returns:
            receipe_model: _description_
        """
        exception_proxy.validate(name, str)
        if len(items) == 0:
            raise argument_exception(f"Некорректно передан параметр {items}. Список пуст!")
        
        
        # Подготовим словарь со списком номенклатуры
        nomenclatures = reference.create_dictionary(data)    
                
        receipt = receipe_model(name)
        
        for position in items:
            # Получаем список кортежей и берем первое значение
            _list =  list(position.items())
            if len(_list) < 1:
                raise operation_exception("Невозможно сформировать элементы рецепта! Некорректный список исходных элементов!")
            
            tuple = list(_list)[0]
            if len(tuple) < 2:
                raise operation_exception("Невозможно сформировать элемент рецепта. Длина кортежа не корректна!")
            
            nomenclature_name = tuple[0]
            size = tuple[1]
            
            # Определеяем номенклатура
            keys = list(filter(lambda x: x == nomenclature_name, nomenclatures.keys() ))
            if len(keys) == 0:
                raise operation_exception(f"Некоректно передан список. Не найдена номенклатура {nomenclature_name}!")
            
            nomenclature = nomenclatures[nomenclature_name]
            
            # Определяем единицу измерения
            if nomenclature.unit.base_unit is None:
                unit = nomenclature.unit
            else:
                unit = nomenclature.unit.base_unit    
            
            # Создаем запись в рецепте
            row = receipe_row_model(nomenclature, size, unit)
            receipt.add(row)
        
        return receipt