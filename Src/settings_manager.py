import os
import json
import uuid

from Src.settings import settings
from Src.errors import error_proxy
from Src.exceptions import exception_proxy, operation_exception
from Src.Logics import convert_factory

#
# Менеджер настроек
#   
class settings_manager(object):
    # Наименование файла по умолчанию
    _settings_file_name = "settings.json"
    # Словарь с исходными данными
    _data = None
    # Внутренний уникальный номер
    _uniqueNumber = None
    # Данные с настройками
    _settings = None
    # Описание ошибок
    _error = error_proxy()
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance  
      

    def __init__(self):
        if self._uniqueNumber is None:
            self._uniqueNumber = uuid.uuid4()
            self.open(self._settings_file_name)
            
            # После загрузки создаем объект класса settings
            self._settings = settings()
            self.__load()
                

    def __open(self):
        """
            Открыть файл с настройками
        """
        file_path = os.path.split(__file__)
        settings_file = "%s/%s" % (file_path[0], self._settings_file_name)
        if not os.path.exists(settings_file):
            self._error.set_error( Exception("ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file))

        try:
            with open(settings_file, "r", encoding = 'utf8') as read_file:
                self._data = json.load(read_file)     
        except:
            self._error.set_error( Exception("ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file))     

    def open(self, file_name: str):
        """
            Открыть файл с настройками
        Args:
            file_name (str):
        """
        exception_proxy.validate( file_name, str)
            
        self._settings_file_name = file_name
        self.__open()
        self.__load()
    
    
    def __load(self):
        """
            Private: Загрузить словарь в объект
        """
        
        if len(self._data) == 0:
            return
        
        # Список полей от типа назначения    
        fields = list(filter(lambda x: not x.startswith("_"), dir(self._settings.__class__)))
        
        # Заполняем свойства 
        for field in fields:
            keys = list(filter(lambda x: x == field, self._data.keys()))
            if len(keys) != 0:
                value = self._data[field]
                
                # Если обычное свойство - заполняем.
                if not isinstance(value, list) and not isinstance(value, dict):
                    setattr(self._settings, field, value)
                
    def save(self):
        """
            Сохранить данные в хранилище
        Raises:
            operation_exception: _description_
        """
        try:
            file_path = os.path.split(__file__)
            settings_file = "%s/%s" % (file_path[0], self._settings_file_name)
            with open(settings_file, "w", encoding = 'utf8') as write_file:
                json_text = json.dumps(self._data, sort_keys = True, indent = 4, ensure_ascii = False)  
                write_file.write(json_text)
                return True
        except Exception as ex:
            raise operation_exception(f"Ошибка при записи файла {self._settings_file_name}\n{ex}")
            
        return False   
    
    @property    
    def settings(self) -> settings:
        """
            Текущие настройки в приложении
        Returns:
            settings: _
        """
        return self._settings 
    
    @property
    def data(self):
        """
            Словарь, который содержит данные из настроек
        Returns:
            dict:
        """
        return self._data
    
    @property
    def error(self) -> error_proxy:
        """
            Текущая информация об ошибке
        Returns:
            error_proxy: 
        """
        return self._error


    