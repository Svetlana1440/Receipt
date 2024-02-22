from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.settings import settings
from Src.Storage.storage import storage
from Src.exceptions import exception_proxy, argument_exception
from Src.reference import reference
from Src.Models.receipe_row_model import receipe_model

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
    
    @staticmethod
    def create_nomenclature():
        """
          Фабричный метод Создать список номенклатуры
        """
        
        result = []
        
        
        item1 = nomenclature_model("Мука пшеничная")
        item1.group = group_model.create_group()
        item1.unit = unit_model.create_killogram()

        item2 = nomenclature_model("Яичный белок")
        item2.group = group_model.create_group()
        item2.unit = unit_model.create_amount()

        item3 = nomenclature_model("Сахарная пудра")
        item3.group = group_model.create_group()
        item3.unit = unit_model.create_gram()

        item4 = nomenclature_model("Ванилин")
        item4.group = group_model.create_group()
        item4.unit = unit_model.create_gram()

        item5 = nomenclature_model("Корица")
        item5.group = group_model.create_group()
        item5.unit = unit_model.create_gram()

        item6 = nomenclature_model("Какао")
        item6.group = group_model.create_group()
        item6.unit = unit_model.create_gram()

        item7 = nomenclature_model("Куриное филе")
        item7.group = group_model.create_group()
        item7.unit = unit_model.create_killogram()

        item8 = nomenclature_model("Салат Романо")
        item8.group = group_model.create_group()
        item8.unit = unit_model.create_gram()

        item9 = nomenclature_model("Сыр Пармезан")
        item9.group = group_model.create_group()
        item9.unit = unit_model.create_killogram()

        item10 = nomenclature_model("Чеснок")
        item10.group = group_model.create_group()
        item10.unit = unit_model.create_gram()

        item11 = nomenclature_model("Белый хлеб")
        item11.group = group_model.create_group()
        item11.unit = unit_model.create_killogram()

        item12 = nomenclature_model("Соль")
        item12.group = group_model.create_group()
        item12.unit = unit_model.create_killogram()

        item13 = nomenclature_model("Черный перец")
        item13.group = group_model.create_group()
        item13.unit = unit_model.create_gram()

        item14 = nomenclature_model("Оливковое масло")
        item14.group = group_model.create_group()
        item14.unit = unit_model.create_liter()

        item15 = nomenclature_model("Лимонный сок")
        item15.group = group_model.create_group()
        item15.unit = unit_model.create_milliliter()

        item16 = nomenclature_model("Горчица дижонская")
        item16.group = group_model.create_group()
        item16.unit = unit_model.create_gram()

        item17 = nomenclature_model("Яйца")
        item17.group = group_model.create_group()
        item17.unit = unit_model.create_amount()

        item18 = nomenclature_model("Сахар")
        item18.group = group_model.create_group()
        item18.unit = unit_model.create_killogram()

        item19 = nomenclature_model("Сливочное масло")
        item19.group = group_model.create_group()
        item19.unit = unit_model.create_gram()

        item20 = nomenclature_model("Ванилин")
        item20.group = group_model.create_group()
        item20.unit = unit_model.create_gram()

        result.append(item1)
        result.append(item2)
        result.append(item3)
        result.append(item4)
        result.append(item5)
        
        result.append(item6)
        result.append(item7)
        result.append(item8)
        result.append(item9)
        result.append(item10)
        
        result.append(item11)
        result.append(item12)
        result.append(item13)
        result.append(item14)
        result.append(item15)
        
        result.append(item16)
        result.append(item17)
        result.append(item18)
        result.append(item19)
        result.append(item20)
        
        return result
    
    @classmethod
    def create_unit(list):
        diction = {}
        for i in list:
            if i.unit.name in diction.keys():
                diction[i.unit.name].append(i)
            else:
                diction[i.unit.name] = [i]
    
    @classmethod
    def create_group(list):
        diction = {}
        for i in list:
            if i.unit.group in diction.keys():
                diction[i.unit.group].append(i)
            else:
                diction[i.unit.group] = [i]

    @classmethod
    def create_receipts(self):
            receipt = []
            if storage.nomenclature_key() in self.__storage.data.keys():
                    #
                    #
                    #
                    #
                    item = receipe_model(_nomenclature=i.name, _size = "из жсона", _unit=i.unit.name)
                    receipt.append(item)


    def create(self):
        """
           В зависимости от настроек, сформировать начальную номенклатуру

        Returns:
            _type_: _description_
        """
        
        result = []
        if self.__oprions.is_first_start == True:
            self.__oprions.is_first_start = False
            
            # Формируем и зпоминаем номеклатуру
            result = start_factory.create_nomenclature()
            self.__save( storage.nomenclature_key(), result )
            unit = start_factory.create_unit(result)
            self.__save(storage.unit_key(), unit)
            group = start_factory.create_group(result)
            self.__save(storage.group_key(), group)
            receipts = self.create_receipts()


        return result

    
        
    
    
        
        
        
        
    
    
    
    