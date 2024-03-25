from Src.Logics.convert_factory import convert_factory
from Src.Logics.process_factory import process_factory
from Src.Logics.storage_prototype import storage_prototype
from Src.exceptions import argument_exception, exception_proxy, operation_exception
from datetime import datetime
import json
from Src.Models.receipe_model import receipe_model
from Src.Models.storage_model import storage_model
class storage_service:
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.__data = data
        
        
    def create_turns(self, start_period: datetime, stop_period:datetime ) -> dict:
        """
            Получить обороты за период
        Args:
            start_period (datetime): _description_
            stop_period (datetime): _description_

        Returns:
            dict: _description_
        """
        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        
        if start_period > stop_period:
            raise argument_exception("Некорректно переданы параметры!")
        
        # Фильтруем      
        prototype = storage_prototype(  self.__data )  
        filter = prototype.filter( start_period, stop_period)
            
        # Подобрать процессинг    
        key_turn = process_factory.turn_key()
        processing = process_factory().create( key_turn  )
    
        # Обороты
        turns =  processing().process( filter.data )
        return turns
    

    def create_turns_by_nomen(self, start_period: datetime, stop_period:datetime, nomen_id: str) -> dict:
        """
            Получить обороты за период по номенклатуре
        Args:
            start_period (datetime): _description_
            stop_period (datetime): _description_

        Returns:
            dict: _description_
        """
        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        
        if start_period > stop_period:
            raise argument_exception("Некорректно переданы параметры!")
        
        # Фильтруем      
        prototype = storage_prototype(  self.__data )  
        filter = prototype.filter( start_period, stop_period)
        filter = filter.filter_by_nomenclature(nomen_id)
            
        # Подобрать процессинг    
        key_turn = process_factory.turn_key()
        processing = process_factory().create( key_turn  )
    
        # Обороты
        turns =  processing().process( filter.data )
        return turns

    def create_transactions(self, receipt: receipe_model, storage: storage_model):


        prototype = storage_prototype(  self.__data )  
        filter = prototype.filter_by_receipt(receipt)
        filter = filter.filter_by_storage(storage)
        if len(self.__data) != len(filter.data):
            raise operation_exception("Отсутствует на складе")
        
        data = receipt.consist.values()

        # Подобрать процессинг    
        transaction_key = process_factory.transaction_key()
        processing = process_factory().create( transaction_key )
    
        # Транзакции
        transactions =  processing().process( data )
        return transactions


    @staticmethod        
    def create_response( data: list, app):
        """"
            Сформировать данные для сервера
        """
        if app is None:
            raise argument_exception("Некорректно переданы параметры!")

        # Преоброзование
        data = convert_factory().serialize( data )
        json_text = json.dumps( data, sort_keys = True, indent = 4,  ensure_ascii = False)  
   
        # Подготовить ответ    
        result = app.response_class(
            response = f"{json_text}",
            status = 200,
            mimetype = "application/json; charset=utf-8"
        )
        
        return result