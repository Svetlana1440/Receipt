from Src.reference import reference

#
# Модель группу номенклатуры
# 
class group_model(reference):
    def create_default_group():
        """
        Фабричный метод. Создать группу по умолчанию

        Returns:
            _type_: _description_
        """
        item = group_model("Ингредиенты")
        return item
    