from Src.Logics.processing import processing
from Src.Models.storage_row_model import storage_row_model
from datetime import datetime

#
# Процесс получения оборотов по списку транзакций
#
class transaction_processing(processing):
    
    def process(self, source: list):
        """
            Сформировать транзакции
        """
        super().process(source)
        result = []

        for element in source:
            object = storage_row_model("element")
            object.period = datetime.now()
            object.nomenclature = element.nomenclature
            object.value = element.size
            object.unit = element.unit
            object.storage_type = False
            result.append(object)
        
        return result