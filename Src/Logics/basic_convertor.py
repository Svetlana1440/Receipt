from Src.Logics.convertor import convertor

#
# Конвертор простых значений в словарь
#
class basic_convertor(convertor):
   
   def serialize(self, field: str, object) -> dict:
      """
            Подготовить словарь 
        Args:
            field (str): поле
            object (_type_): значение
      """
      super().serialize( field, object)
      
      if not isinstance(object, (int, str, bool, float)):
          self.error = f"Некорректный тип данных передан для конвертации. Ожидается: (int, str, bool). Передан: {type(object)}"
          return None
      
      try:
            return { field: object }
      except Exception as ex:
            self.set_error(ex)  
            
      return None        
        
    