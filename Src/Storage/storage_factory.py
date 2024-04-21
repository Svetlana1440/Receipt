
from exceptions import argument_exception
from Models.nomenclature_model import nomenclature_model
from Models.range_model import range_model
from Storage.storage_journal_transaction import storage_journal_transaction
from Storage.storage_model import storage_model
from Storage.storage_journal_row import storage_journal_row
from Storage.storage_turn_model import storage_turn_model
import uuid

from datetime import datetime


class storage_factory:
    @staticmethod
    def create_turn(stor: uuid.UUID, amount: int, nom: nomenclature_model, ran: range_model):
        result = storage_turn_model()
        result.amount = amount
        result.storage_id = stor
        result.nomenclature = nom
        result.range = ran
        return result

    @staticmethod
    def create_row(target_storage: storage_model, operation: storage_journal_transaction):
        result = storage_journal_row()

        result.operation_id = operation.id
        result.period = (operation.period)
        result.operation_type = (operation.type == "add")
        result.nomenclature = operation.nomenclature
        result.amount = operation.amount

        result.location = target_storage.location
        result.storage_id = target_storage.id

        return result

    @staticmethod
    def create_transaction(type_arg: bool, nomenclature: nomenclature_model, how_many: int, date: datetime):
        result = storage_journal_transaction()

        result.type = type_arg
        result.nomenclature = nomenclature
        result.period = date
        result.amount = how_many
        result.id = uuid.uuid4()

        return result
