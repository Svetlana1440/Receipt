from Src.Logics.processing import processing
from Src.Models.storage_row_turn_model import storage_row_turn_model


#
# Процесс получения оборотов по списку транзакций
#
class turn_processing(processing):
    
    def process(self, source: list) -> list:
        """
            Сформировать складские обороты
        Args:
            transactions (list): Список объектов типа storage_row_model

        Returns:
            list: _description_
        """
        super().process(source)
        result = []
        
        # Код взят https://github.com/AItEKS/Design-patterns/pull/9/files#diff-401a63dd40e843c86f4a13a76fc390dac87de5ab5e65afc30cd5bcede4893f94

        grouped_transactions = {}
        for transaction in source:
            key = (transaction.nomenclature, transaction.storage,transaction.unit )
            if key not in grouped_transactions.keys():
                grouped_transactions[key] = []
                
            grouped_transactions[key].append(transaction)

        for key, transactions in grouped_transactions.items():
            first_transaction = transactions[0]
            
            # Расчитываем оборот
            turnover = sum(transaction.value if transaction.storage_type else -transaction.value for transaction in transactions)
               
            # Создаем модель   
            row = storage_row_turn_model.create( first_transaction.nomenclature, first_transaction.storage, first_transaction.unit)
            row.value = turnover
            
            # Добавляем в список
            result.append(row)

        return result
 
  