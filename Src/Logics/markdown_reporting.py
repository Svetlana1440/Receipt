from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception

class markdown_reporting(reporting):
    
      def create(self, typeKey: str):
        super().create(typeKey)
        result = []

        # Исходные данные
        items = self.data[ typeKey ]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")
        
        
        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")
        
        # Заголовок
        result.append(f"# {typeKey}")
        
        # Шапка таблицы
        header = ""
        line = ""
        for field in self.fields:
            header += f"|{field}"
            line += "|--"
        
        result.append(f"{header}|")
        result.append(f"{line}|")
        
        # Данные
        for item in items:
            row = ""
            for field in self.fields:
                value = getattr(item, field)
                if value is None:
                    value = ""
                    
                row +=f"|{value}"    
            result.append(f"{row}|")
            
        return "\n".join(result)        