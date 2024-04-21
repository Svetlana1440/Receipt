import uuid
from exceptions import argument_exception


class storage_model:
    __location: str = ""

    __id: uuid = None

    @property
    def location(self):
        return self.__location

    @property
    def id(self):
        return self.__id

    @location.setter
    def location(self, value: str):
        value_stripped = value.strip()

        if not isinstance(value, str) or (value_stripped == ""):
            raise argument_exception("Некорректный аргумент")

        self.__location = value_stripped

    def __init__(self, loc: str) -> None:
        self.__id = uuid.uuid4()
        self.location = loc
