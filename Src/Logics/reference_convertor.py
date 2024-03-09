from Src.Logics.convertor import convertor
from Src.reference import reference
class reference_convertor(convertor):
    def __init__(self):
        pass


    def convert(self, object: reference):
        """
            Конвертор Reference
        """
        super().__init__(object)
        result = {}
        fields = self.fields
        for field in fields:
            field_data = getattr(object, field)
            if isinstance(field_data, reference):
                field_data = self.convert(field_data)
            
            result[field] = field_data

        return result