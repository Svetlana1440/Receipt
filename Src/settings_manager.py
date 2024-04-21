import os
from pathlib import Path
import json
import uuid
from settings import settings
from exceptions import argument_exception, operation_exception
from Logic.Reporting.Json_convert.reference_conventor import reference_conventor


class settings_manager(object):
    # Имя файла настроек
    __file_name = "settings.json"
    # Уникальный номер
    __unique_number = None
    # Словарь с данными
    __data = {}
    # Настройки инстанс
    __settings = settings()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __convert(self):
        if len(self.__data) == 0:
            raise operation_exception(
                "Невозможно создать объект типа settings.py")

        fields = dir(self.__settings.__class__)
        field_keys = list(self.__data.keys())

        # по ключам json подставляет атрибуты для класса и проверяет их
        for cur_key in field_keys:
            if cur_key in fields:
                value = self.__data[cur_key]
                print(value, type(value), cur_key)
                setattr(self.__settings, cur_key, value)
        return True

    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()

    def open(self, file_name='settings.json', file_path=Path(__file__).parent) -> bool:
        if not isinstance(file_name, str):
            raise argument_exception("ERROR: Неверный аргумент!")

        if file_name == "":
            raise argument_exception("ERROR: Неверный аргумент!")

        self.__file_name = file_name.strip()
        self.__file_path = file_path
        try:
            self.__open()
            self.__convert()
            return True
        except:
            return False

    @property
    def settings(self):
        return self.__settings

    @property
    def data(self):
        """
            Текущие данные 
        Returns:
            _type_: словарь
        """
        return self.__data

    @property
    def number(self) -> str:
        return str(self.__unique_number.hex)

    def __open(self):
        """
            Открыть файл с настройками
        Raises:
            Exception: Ошибка при открытии файла
        """
        file_path = os.path.join(self.__file_path, self.__file_name)

        settings_file = file_path
        if not os.path.exists(settings_file):
            raise operation_exception(
                "ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file)

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)

    # настройки в json

    def _make_json(self):
        saved = {}
        
        for cur_key in list(self.__data.keys()):
            saved[cur_key] = str(getattr(self.settings, cur_key))
            print(getattr(self.settings, cur_key))

        return json.dumps(saved, ensure_ascii=False)

    # сохранить настройки и записать их в файл
    def save_settings(self):
        res = self._make_json()
        file = os.path.join(self.__file_path, self.__file_name)

        with open(file, 'w') as saved:
            saved.write(res)

        return True
