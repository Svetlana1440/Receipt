from Src.Logics.convertor import convertor
from datetime import datetime


class datetime_convertor(convertor):
    def __init__(self):
        pass
        

    @staticmethod
    def convert(object: datetime):
        """
            Корвертор datetime
        """
        return {
            'year': object.year,
            'month': object.month,
            'day': object.day,
            'hour': object.hour,
            'minute': object.minute,
            'second': object.second,
            'microsecond': object.microsecond
        }