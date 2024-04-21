class storage:
    __data = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance

    @property
    def data(self):
        return self.__data

    # ключ хранения номенклатуры
    @staticmethod
    def nomenclature_key():
        return "nomenclature"

    # ключ хранения группы
    @staticmethod
    def group_key():
        return "group"

    # ключ хранения единиц измерения
    @staticmethod
    def unit_key():

        return "unit"

    # ключ хранения рецептов
    @staticmethod
    def reciepe_key():
        return "reciepe"

    # ключ хранения журнала
    @staticmethod
    def journal_key():
        return "journal"

    # ключ оборота
    @staticmethod
    def process_turn_key():
        return "process_turn"

    # ключ оборота до блокировки
    @staticmethod
    def b_turn_key():
        return "block_turn"
