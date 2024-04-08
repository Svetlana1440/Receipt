from Src.Logics.processing import processing
from Src.Models.receipe_row_model import receipe_row_model

from datetime import datetime
from Src.Models.storage_model import storage_model

#
# Сформировать набор проводок для списание по рецепту
# Код взят https://github.com/Illikan/popov_design_patterns/blob/aee55cd86f5414d72bdb039b95b4b68771858a3d/Src/Logics/transaction_processing.py#L17
#
class debit_processing(processing):
    
      def process(self, source: list) -> list:
        """
            Сформировать проводки списания
        Args:
            transactions (list): Список объектов типа receipe_row_model

        Returns:
            list: _description_
        """
        super().process(source)
        result = []
        storage_default = storage_model.create_default()
          
        for row in source:
            debit_transaction = receipe_row_model.create_debit_transaction( row, datetime.now(), storage_default )
            result.append( debit_transaction )
            
        return result    