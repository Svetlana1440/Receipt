from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception


#
# Класс - реализация построение данных в формате csv
#
class csv_reporting(reporting):
<<<<<<< HEAD
    
    def create(self, typeKey: str):
        super().create(typeKey)
=======
    def create(self, TypeKey: str):
        """
        Функция возвращает csv строку
        """
        super().create(TypeKey)

>>>>>>> c3fda05bbfb4918ad4df535ace3fbf54be41ab73
        result = ""
        delimetr = ";"

<<<<<<< HEAD
        # Исходные данные
        items = self.data[ typeKey ]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")
        
        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")
        
        # Заголовок 
        header = delimetr.join(self.fields)
        result += f"{header}\n"
        
        # Данные
=======
        #Список
        for field in self.fields:
            result += f"{field};"
        result = result[:-1]+"\n"
        result += self.__csv__create(self.fields, items)

        #Результат csv
        return result 
    @staticmethod
    def __csv__create(fields, items):
        """
        Функция формирует csv строку
        """
        result = ""
>>>>>>> c3fda05bbfb4918ad4df535ace3fbf54be41ab73
        for item in items:
            row = ""
            for field in self.fields:
                value = getattr(item, field)
                if value is None:
                    value = ""
                    
                row +=f"{value}{delimetr}"
                
            result += f"{row[:-1]}\n"
            
        
        # Результат csv
        return result
        
        
        