
from src.exceptions import argument_exception
from models.nomenclature_model import nomenclature_model
from src.models.range_model import range_model
from src.storage.storage_journal_transaction import storage_journal_transaction
from src.storage.storage_model import storage_model
from storage.storage_journal_row import storage_journal_row
from src.storage.storage_turn_model import storage_turn_model
import uuid

from datetime import datetime


class storage_factory:



    #CDELAT POLNOCENNOY FABRIKOY CHEREZ NASLEDOVANIYE CLASSOV METODA
    #POTOM SOBRAT FABRIKOY  METODY POLIMORFIZMOM
    
    @staticmethod
    def create_turn(stor:uuid.UUID,amount:int,nom:nomenclature_model,ran:range_model):
        result=storage_turn_model()

        result.amount=amount

        result.storage_id=stor

        result.nomenclature=nom
        
        result.range=ran

        return result
    

    @staticmethod 
    def create_row(target_storage:storage_model,operation:storage_journal_transaction):
        result=storage_journal_row()

    
        #Берём от операции
        result.operation_id=operation.id
        result.period=(operation.period)
        result.operation_type=(operation.type=="add")
        result.nomenclature=operation.nomenclature
        result.amount=operation.amount

        #Бёрём от склада
        result.location=target_storage.location
        result.storage_id=target_storage.id


        return result
    
    @staticmethod 
    def create_transaction(type_arg:bool,nomenclature:nomenclature_model,how_many:int,date:datetime):
        result=storage_journal_transaction()

        result.type=type_arg
        result.nomenclature=nomenclature
        result.period=date
        result.amount=how_many
        result.id=uuid.uuid4()

        return result


