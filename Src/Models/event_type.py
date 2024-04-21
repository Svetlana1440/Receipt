from Models.abstract_reference import abstract_reference


#
# Типы событий
#
class event_type(abstract_reference):
    @staticmethod
    def changed_block_period() -> str:
        """
            Событие изменения даты блокировки
        Returns:
            str: _description_
        """
        return "changed_block_period"
