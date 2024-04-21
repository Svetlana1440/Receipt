from exceptions import argument_exception
from Storage.storage_journal_row import storage_journal_row
from Storage.storage import storage
from Storage.storage_factory import storage_factory


class process_factory:
    __maps = {}

    def __init__(self) -> None:
        self.__build_structure()

    def __build_structure(self):
        self.__maps[storage.process_turn_key()] = process_factory.process_storage_turn

    @staticmethod
    def process_storage_turn(journal: list):
        if not isinstance(journal, list):
            raise argument_exception("Неверный аргумент")
        if len(journal) == 0:
            return []
        if not isinstance(journal[0], storage_journal_row):
            raise argument_exception("Неверный массив")

        result = {}
        for cur_line in journal:
            key = cur_line.nomenclature.name+' '+str(cur_line.storage_id)
            keys = list(result.keys())

            coeff = 1-2*(cur_line.operation_type == "delete")

            if key in keys:
                result[key].amount += cur_line.amount*coeff
            else:
                result[key] = storage_factory.create_turn(
                    cur_line.storage_id, cur_line.amount*coeff, cur_line.nomenclature, cur_line.nomenclature.ran_mod)
        return list(result.values())

    def create(self, key: str, journal: list):
        if not isinstance(key, str):
            raise argument_exception("Неверный аргумент")
        operation = self.__maps[key]
        return operation(journal)

