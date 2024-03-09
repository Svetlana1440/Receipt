from abc import ABC


class convertor(ABC):
    __fields = None

    @property
    def fields(self):
        return self.__fields
    
    @staticmethod
    def __get_fields(object):
        fields = list(filter(lambda x: not x.startswith("_") and not x.startswith("create_") , dir(object)))
        return fields
    

    def __init__(self, object) -> None:
        self.__fields = convertor.__get_fields(object)
