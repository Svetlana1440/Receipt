from Src.Logics.convertor import convertor

class basic_convertor(convertor):
    def __init__(self) -> None:
        pass

        
    @staticmethod
    def convert(object):
        """
            Конвертер базовый
        """
        return {str(type(object)): str(object)}