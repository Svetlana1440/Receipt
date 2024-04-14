
from uuid import UUID
from datetime import datetime
from models.nomenclature_model import nomenclature_model
from src.exceptions import argument_exception
from src.storage.storage_journal_transaction import storage_journal_transaction
from src.storage.storage_model import storage_model

#IZ IH SPISKA SOSTOIT J\Lyrnal
class storage_journal_row:
    #Transaction
    __operation_id=None 

    __operation_type=None

    __nomenclature_model=None

    __period=None

    __amount=None

    #storage
    __location=""

    __storage_id=None
    
    #номенклатура
    @property
    def nomenclature(self):
        return self.__nomenclature_model
    
    #дата
    @property
    def period(self):
        #"%s-%s-%s" % (self.__period.date,self.__period.month,self.__period.year) 
        return self.__period
    
    #id операции
    @property
    def operation_id(self):
        return self.__operation_id
    
    #id склада
    @property
    def storage_id(self):
        return self.__storage_id
    
    #тип операции
    @property
    def operation_type(self):
        return self.__operation_type*"add" +(not (self.__operation_type))*"delete"
    
    #место
    @property 
    def location(self):
        return self.__location
    
    #количсество
    @property
    def amount(self):
        return self.__amount


    #так как конструктор формирует класс через классы storage_model и storage_journal_transaction, наши аргументы уже проверены, но на всякий случай
    @nomenclature.setter
    def nomenclature(self,value:nomenclature_model):
        if not isinstance(value,nomenclature_model):
            raise  argument_exception("Некорректный аргумент")
        

        self.__nomenclature_model=value

    @storage_id.setter
    def storage_id(self,value:UUID):
        if not isinstance(value,UUID):
            raise  argument_exception("Некорректный аргумент")
        
        
        self.__storage_id=value


    @location.setter
    def location(self,value:str):
        if not isinstance(value,str):
            raise  argument_exception("Некорректный аргумент")
        

        self.__location=value

    @operation_type.setter
    def operation_type(self,value:bool):
        if not isinstance(value,bool):
            raise  argument_exception("Некорректный аргумент")
        
        self.__operation_type=value

    @period.setter
    def period(self,value:datetime):
        if not isinstance(value,datetime):
            raise  argument_exception("Некорректный аргумент")
        
        self.__period=value

    @operation_id.setter
    def operation_id(self,value:UUID):
        if not isinstance(value,UUID):
            raise  argument_exception("Некорректный аргумент")
        
        
        self.__operation_id=value
   

   
    @amount.setter
    def amount(self,value:int):
        if not isinstance(value,int) or value<0:
            raise argument_exception("Wrong argument")
        self.__amount=value


