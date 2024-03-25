#
# Класс хранилище данных
#
class storage:
    __data = {}
    
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance  
    
    @property
    def data(self) -> dict:
        """
         Данные по моделям

        Returns:
            _type_: _description_
        """
        return self.__data

 
    @staticmethod
    def nomenclature_key():
        """
            Ключ для хранения номенклатуры
        Returns:
            _type_: _description_
        """
        return "nomenclatures"

  
    @staticmethod
    def group_key():
        """
            Списк номенклатурных групп
        Returns:
            _type_: _description_
        """
        return "groups"
      
      
    @staticmethod
    def storage_transaction_key():
        """
            Список складских проводок
        Returns:
            _type_: _description_
        """
        return "transactions"  
    

    @staticmethod  
    def unit_key():
        """
              Список единиц измерения
        Returns:
            _type_: _description_
        """
        return "units"
    
    @staticmethod
    def receipt_key():
        """
            Список рецептов
        Returns:
            _type_: _description_
        """
        return "receipts"
    
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
    