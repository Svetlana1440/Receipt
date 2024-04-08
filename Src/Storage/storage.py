import json
import os

from Src.exceptions import operation_exception
from Src.Logics.convert_factory import convert_factory
from Src.reference import reference


#
# Класс хранилище данных
#
class storage():
    __data = {}
    __storage_file = "storage.json"
    __mapping = {}
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)

        return cls.instance  
    
    def __init__(self) -> None:
        # Связка для всех моделей
        for  inheritor in reference.__subclasses__():
            self.__mapping[inheritor.__name__] = inheritor

    
    @property
    def data(self) -> dict:
        """
         Данные по моделям

        Returns:
            _type_: _description_
        """
        return self.__data
    
    def load(self):
        """
            Загрузить данные из хранилища
        Raises:
            operation_exception: _description_
        """
        try:
            file_path = os.path.split(__file__)
            data_file = "%s/%s" % (file_path[0], self.__storage_file)
            if not os.path.exists(data_file):
                raise operation_exception(f"Невозможно загрузить данные! Не найден файл {data_file}")

            with open(data_file, "r") as read_file:
                source =  json.load(read_file)   
                
                self.__data = {}
                for key in storage.storage_keys(storage):
                    if key in source.keys():
                        source_data = source[key]
                        self.__data[key] = []
                        
                        for item in source_data:
                            object = self.__mapping[key]
                            instance = object().load(item)
                            self.__data[key].append(instance)

        except Exception as ex:
            raise operation_exception(f"Ошибка при чтении данных. Файл {self.__storage_file}\n{ex}")
        
        
    def save(self):
        """
            Сохранить данные в хранилище
        Raises:
            operation_exception: _description_
        """
        try:
            factory = convert_factory()
            with open(self.__storage_file, "w") as write_file:
                data = factory.serialize( self.data )
                json_text = json.dumps(data, sort_keys = True, indent = 4, ensure_ascii = False)  
                write_file.write(json_text)
                
                return True
        except Exception as ex:
            raise operation_exception(f"Ошибка при записи файла {self.__storage_file}\n{ex}")
            
        return False    

 
    @staticmethod
    def nomenclature_key():
        """
            Ключ для хранения номенклатуры
        Returns:
            _type_: _description_
        """
        return "nomenclature_model"

  
    @staticmethod
    def group_key():
        """
            Списк номенклатурных групп
        Returns:
            _type_: _description_
        """
        return "group_model"
      
      
    @staticmethod
    def storage_transaction_key():
        """
            Список складских проводок
        Returns:
            _type_: _description_
        """
        return "storage_row_model"  
    

    @staticmethod  
    def unit_key():
        """
              Список единиц измерения
        Returns:
            _type_: _description_
        """
        return "unit_model"
    
    @staticmethod
    def receipt_key():
        """
            Список рецептов
        Returns:
            _type_: _description_
        """
        return "receipe_model"
    
    # Код взят: https://github.com/UpTechCompany/GitExample/blob/6665bc70c4933da12f07c0a0d7a4fc638c157c40/storage/storage.py#L30
    
    @staticmethod
    def storage_keys(cls):
        """
            Получить список ключей
        Returns:
            _type_: _description_
        """
        keys = []
        methods = [getattr(cls, method) for method in dir(cls) if callable(getattr(cls, method))]
        for method in methods:
            if method.__name__.endswith("_key") and callable(method):
                keys.append(method())
        return keys
    