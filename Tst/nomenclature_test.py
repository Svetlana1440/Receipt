from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import  nomenclature_model
from Src.Models.unit_model import unit_model
from Src.exceptions import argument_exception

import unittest

#
# Набор автотестов для проверки работы моделей связанных с номенклатурой
#
class nomenclature_test(unittest.TestCase):

    # 
    # Проверить создание новой карточки номенклатуры
    #
    def test_create_nomenclature(self):
        # Подготовка
        group = group_model("test group")
        item = nomenclature_model("test")
        unit = unit_model("test unit")

        # Действие
        item.description = "test description"
        item.group = group
        item.unit = unit

        # Проверка
        assert item is not None

    # 
    # Проверить создание новой карточки номенклатуры с ошибкой
    #
    def test_create_nomenclature_fail_name(self):
        # Подготовка
        group = group_model("test group")
        item = nomenclature_model("test nomenclature")
        unit = unit_model("test unit")
        item.description = "test description"
        item.group = group
        item.unit = unit

        # Действие
        with self.assertRaises(argument_exception) as context:
            item.name = "11111111111111111111111111111111111111111111111111111111111111111111111111"
        
        # Проверка    
        self.assertTrue(f'Есть нужное исключение - {context.exception}')    


    
if __name__ == '__main__':
    unittest.main()    