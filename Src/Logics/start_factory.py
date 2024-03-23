# Модели
from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.reference import reference
from Src.Models.receipe_model import receipe_model
from Src.Models.storage_row_model import storage_row_model
from Src.Models.storage_model import storage_model

# Системное
from Src.settings import settings
from Src.Storage.storage import storage
from Src.exceptions import exception_proxy, operation_exception, argument_exception

#
# Класс для обработки данных. Начало работы приложения
#
class start_factory:
    __oprions: settings = None
    __storage: storage = None
    
    def __init__(self, _options: settings,
                 _storage: storage = None) -> None:
        
        exception_proxy.validate(_options, settings)
        self.__oprions = _options
        self.__storage = _storage
        
    
    def __save(self, key:str, items: list):
        """
            Сохранить данные
        Args:
            key (str): ключ доступ
            items (list): список
        """
        exception_proxy.validate(key, str)
        
        if self.__storage == None:
            self.__storage = storage()
            
        self.__storage.data[ key ] = items
        
    @property            
    def storage(self):
        """
             Ссылка на объект хранилище данных
        Returns:
            _type_: _description_
        """
        return self.__storage
    
    # Статические методы
    
    @staticmethod
    def create_units() -> list:
        """
            Сформировать список единиц измерения
        Returns:
            _type_: _description_
        """
        items = []
        items.append( unit_model.create_gram() )
        items.append( unit_model.create_killogram() )
        items.append( unit_model.create_liter() )
        items.append( unit_model.create_milliliter() )
        items.append( unit_model.create_ting() )
        
        return items
    
    @staticmethod
    def create_nomenclatures() -> list:
        """
          Сформировать список номенклатуры
        """
        
        group = group_model.create_default_group()
        items = [ {"Мука пшеничная": "киллограмм"}, 
                  {"Сахар":"киллограмм"}, 
                  {"Сливочное масло" : "киллограмм"}, 
                  {"Яйца": "штука"}, {"Ванилин": "грамм"}, 
                  {"Куринное филе": "киллограмм"}, 
                  {"Салат Романо": "грамм"},
                  {"Сыр Пармезан" : "киллограмм"}, 
                  {"Чеснок": "киллограмм"}, 
                  {"Белый хлеб": "киллограмм"},
                  {"Соль": "киллограмм"}, {"Черный перец": "грамм"}, 
                  {"Оливковое масло": "литр"}, 
                  {"Лимонный сок": "литр"},
                  {"Горчица дижонская": "грамм"},
                  {"Сахарная пудра": "грамм"},{"Ванилиин": "грамм"},
                  {"Корица": "грамм"},
                  {"Какао": "киллограмм"}]
        
        # Подготовим словарь со список единиц измерения
        units = reference.create_dictionary(start_factory.create_units())
        
        result = []
        for position in items:
            # Получаем список кортежей и берем первое значение
            _list =  list(position.items())
            if len(_list) < 1:
                raise operation_exception("Невозможно сформировать элементы номенклатуры! Некорректный список исходных элементов!")
            
            tuple = list(_list)[0]
            
            # Получаем неименование номенклатуры и единицы измерения
            if len(tuple) < 2:
                raise operation_exception("Невозможно сформировать элемент номенклатуры. Длина кортежа не корректна!")
            
            name   = tuple[0]
            unit_name = tuple[1]
            
            if not unit_name in units.keys():
                raise operation_exception(f"Невозможно найти в списке указанную единицу измерения {unit_name}!")
            
            # Создаем объект - номенклатура
            item = nomenclature_model( name, group, units[unit_name])
            result.append(item)
          
        return result
      
    @staticmethod      
    def create_groups() -> list:
        """
            Сформировать список групп номенклатуры
        Returns:
            _type_: _description_
        """
        items = []
        items.append( group_model.create_default_group())
        return items         
    
    @staticmethod
    def create_receipts(_data: list = None) -> list:
        """
            Сформировать список рецептов
        Args:
            _data (list, optional): Список номенклатуры. Defaults to None.

        Raises:
            argument_exception: _description_

        Returns:
            _type_: Массив объектов receipe_model
        """
        result = []
        
        if _data is None:
            data = start_factory.create_nomenclatures()
        else:
            data = _data
            
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры! Список номенклатуры пуст.")        
        
        # Вафли хрустящие в вафильнице
        items = [ {"Мука пшеничная": 100}, {"Сахар": 80}, {"Сливочное масло": 70},
                  {"Яйца": 1} , {"Ванилин": 5 }
                ]
        item = receipe_model.create_receipt("Вафли хрустящие в вафильнице", "", items, data)
        
        # Шаги приготовления
        item.instructions.extend([
            "Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке.",
            "Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает.",
            "Добавьте в масло яйцо. Предварительно все-таки проверьте масло, не горячее ли оно, иначе яйцо может свариться. Перемешайте яйцо с маслом до однородности.",
            "Всыпьте муку, добавьте ванилин.",
            "Перемешайте массу венчиком до состояния гладкого однородного теста."])
        
        item.comments = "Время приготовления: 20 мин. 8 порций"
        result.append( item )
        
        # Цезарь с курицей
        items = [ {"Куринное филе": 200}, {"Салат Романо": 50}, {"Сыр Пармезан": 50},
                  {"Чеснок": 10} , {"Белый хлеб": 30 }, {"Соль": 5}, {"Черный перец": 2},
                  {"Оливковое масло": 10}, {"Лимонный сок": 5}, {"Горчица дижонская": 5},
                  {"Яйца": 2}
                ]
        item =  receipe_model.create_receipt("Цезарь с курицей", "", items, data)
        item.instructions.extend([
            "Нарезать куриное филе кубиками, нарубите чеснок, нарежьте хлеб на кубики."
            "Очистить салат и обсушить его."
            "Натереть сыр Пармезан на терке."
            "Обжарить на сковороде куриное филе с чесноком до готовности."
            "На той же сковородке обжарьить кубики хлеба до золотистости."
            "В миске смешайте оливковое масло, лимонный сок, горчицу, измельченный чеснок, соль и перец."
            "В большой миске смешайте кубики курицы, хлеба, листья салата."
            "Добавить заправку и тщательно перемешать"])
            
        result.append(item)
        
        # Безе
        items = [ {"Яйца": 3}, {"Сахарная пудра":180}, {"Ванилиин" : 5}, {"Корица": 5} ,{"Какао": 20} ]
        result.append( receipe_model.create_receipt("Безе", "", items, data))
        return result
        
    @staticmethod
    def create_storage_transactions(data: dict) -> list:
        """
            Сформировать список складских транзакций
        Returns:
            _type_: Массив объектов storage_row_model
        """
        result = []
        default_storage = storage_model.create_default()
            
        if len(data.keys()) == 0:
            raise operation_exception("Набор данных пуст. Невозможно сформировать список транзакций!")  
        
        items = [ { "Мука пшеничная": [1, "киллограмм"] }, 
                  { "Черный перец": [50, "грамм" ] },
                  { "Сахар" :[0.5, "киллограмм"] },
                  { "Яйца": [6,"штука" ] },
                  { "Оливковое масло": [0.2,"литр" ] },
                  { "Куринное филе": [0.5, "киллограмм"] },
                  { "Салат Романо": [1, "штука"] },
                  { "Белый хлеб" : [3, "штука"] },
                  { "Сыр Пармезан": [0.2, "киллограмм" ] },
                  { "Горчица дижонская" : [0.1, "литр"] },
                  { "Черный перец": [10, "грамм" ] },
                  { "Лимонный сок": [1, "литр"] },
                  { "Какао": [1,"киллограмм"] },
                  { "Сыр Пармезан": [0.3, "киллограмм" ] },
                  { "Ванилиин": [100, "грамм"] }  ]
        
        for element in items:
            key = list(element.keys())[0]
            values = list(element.values())[0]
            
            row = storage_row_model.create_credit_row(key, values, data, default_storage)
            result.append(row)
        
        return result
        
    
    # Основной метод
    def create(self) -> bool:
        """
           В зависимости от настроек, сформировать или загрузить набор данных
        Returns:
            _type_: _description_
        """
        if self.__oprions.is_first_start == True:
            # 1. Формируем и зпоминаем номеклатуру
            nomenclatures = start_factory.create_nomenclatures()
            self.__save( storage.nomenclature_key(), nomenclatures )
            
            # 2. Формируем и запоминаем рецепты
            items = start_factory.create_receipts(nomenclatures)
            self.__save( storage.receipt_key(), items)
      
            # 3. Формируем и запоминаем единицы измерения
            items = start_factory.create_units()
            self.__save( storage.unit_key(), items)
            
            # 4. Формируем и запоминаем группы номенклатуры
            items = start_factory.create_groups()
            self.__save( storage.group_key(), items)
            
            # 5. Формируем типовые складские проводки
            items = start_factory.create_storage_transactions( self.storage.data )
            self.__save( storage.storage_transaction_key(), items)
            
            return True
           
           
        else:
            # Другой вариант. Загрузка из источника данных    
            return False
        
        
    
        
        
        
        
    
    
    
    