import unittest
from exceptions import argument_exception, operation_exception
from error_proxy import error_proxy
from pathlib import Path
import os
import sys
sys.path.append(os.path.join(Path(__file__).parent.parent, 'Src'))


class test_errors(unittest.TestCase):
    def test_check_set_error_text(self):
        # Подготовка"
        error = error_proxy("Test", 'test')
        assert error.if_error == True

    def test_check_set_exception(self):
        # Подготовка
        error = error_proxy()

        try:
            result = 1/0
        except Exception as ex:
            error.create_error(ex)
        assert error.if_error

    def test_check_argument_exception(self):
        # Подготовка
        try:
            raise argument_exception

        except Exception as ex:
            assert True == True
            return

    def test_check_operation_exception(self):
        # Подготовка
        try:
            raise operation_exception

        except Exception as ex:
            assert True == True
            return
