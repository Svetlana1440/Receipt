from Src.Logics.reporting import reporting
from Src.reference import reference

class csv_reporting(reporting):
    def create(self, TypeKey: str):
        """
        Функция возвращает csv строку
        """
        super().create(TypeKey)

        result = ""
        #Исходные данные
        items = self.data[TypeKey]

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
        for item in items:
            list = []
            for field in fields:
                getattr_name = getattr(item, field)
                if isinstance(getattr_name, reference):
                    list.append(getattr_name.name)
                elif isinstance(getattr_name, str):
                    if getattr_name != "":
                        list.append(getattr_name)
                    else:
                        list.append(" ")
                elif isinstance(getattr_name, int):
                    list.append(str(getattr_name))
                elif isinstance(getattr_name, bool):
                    list.append(str(getattr_name))
                elif  getattr_name is None:
                    list.append(" ")
            result += ';'.join(list) + "\n" 

        return result
                
                    


                    
                
                    


                    


