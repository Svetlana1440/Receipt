

from exceptions import argument_exception
from storage.storage_journal_row import storage_journal_row
from src.storage.storage import storage
from src.storage.storage_factory import storage_factory
from datetime import datetime

class process_factory:

    __maps={}


    def __build_structure(self):
        self.__maps[storage.process_turn_key()]=process_factory.process_storage_turn


    @staticmethod
    def process_storage_turn(journal:list):
        if not isinstance(journal,list) :
            raise argument_exception("Неверный аргумент")
        
        if len(journal)==0:
            return[]
        
        if not isinstance(journal[0],storage_journal_row):
            raise argument_exception("Неверный массив")
        

        result={}
        
        for cur_line in journal:
            #айди склада и имя номенклатуры, для того чтобы рассортировать строки складского журнала
            key=cur_line.nomenclature.name+' '+str(cur_line.storage_id)
            keys=list(result.keys())

            koef=1-2*( cur_line.operation_type=="delete")
            

            if key in keys:
                result[key].amount+=cur_line.amount*koef
            else:
                
                #в turnmodel хранятся данные о складе, а также  количестве,  типе и единицах измерения номенклатуры
                result[key]=storage_factory.create_turn(cur_line.storage_id,cur_line.amount*koef,cur_line.nomenclature,cur_line.nomenclature.ran_mod)

        #по требованию задания мы возвращаем список, поэтому list(result.values())
        return list(result.values())
    


    def create(self,key:str,journal:list):
        if not isinstance(key,str):
            raise argument_exception("Неверный аргумент")




        operation=self.__maps[key]



        return operation(journal)



    def __init__(self) -> None:
        self.__build_structure()

        

        

