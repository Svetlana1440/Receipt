from Models.event_type import event_type
from exceptions import argument_exception


#
# Наблюдатель для складских операций
#
class storage_observer:
    observers = []

    @staticmethod
    def raise_event(handle_event: str):
        """
            Сформировать события
        Args:
            handle_event (str): _description_
        """
        if not isinstance(handle_event, str):
            raise argument_exception("Неверный тип аргумента")

        for object in storage_observer.observers:
            if object is not None:
                object.handle_event(handle_event)
