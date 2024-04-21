from Models.nomenclature_model import nomenclature_model, nomenclature_group_model, range_model
import unittest
from settings_manager import settings_manager
from settings import settings
from Models.organisation_model import organisation_model
from Models.reciepe_model import reciepe_model
from pathlib import Path
import os
import sys
import json
import uuid

a = os.path.join(Path(__file__).parent.parent, 'Src')
sys.path.append(os.path.join(Path(__file__).parent.parent, 'Src'))
sys.path.append(os.path.join(Path(__file__).parent.parent, 'Src', 'Models'))


class test_models(unittest.TestCase):
    def test_abstract_name_length(self):
        # подготовка
        k = "a"*51

        # действие
        try:
            item = range_model(k)

        except Exception as ex:
            assert True == True
            return

        assert False == True

    def test_inheritance_abstract(self):
        # подготовка
        item = range_model("  name_example    ")

        # действие

        # проверка
        assert item.name == "name_example"

    # range model tests

    def test_range_model_name(self):
        # подготовка
        item = range_model("  name_example    ", 1)

        # действие

        # проверка
        assert item.name == "name_example"

    def test_range_model_base(self):
        # подготовка
        item = range_model(" Грамм ", 1)

        # действие
        item2 = range_model("Килограмм  ", 1000, item)

        # проверка
        assert item2.base_range.name == "Грамм"

    def test_range_model_recount(self):
        # подготовка
        item = range_model(" Грамм ", 1)

        # действие
        item2 = range_model("Килограмм  ", 1000, item)

        # проверка
        assert item2.recount_ratio*5 == 5000

    def test_range_model_recount_two_sons(self):
        # подготовка
        item = range_model(" Грамм ", 1)

        # действие
        item2 = range_model("Килограмм  ", 1000, item)
        item3 = range_model("Тонна ", 1000000, item)
        # проверка
        assert item2.recount_ratio*5 == item3.recount_ratio/200

    def test_organisation_model_import_abort(self):
        # подготовка

        # действие
        try:
            company = organisation_model("aweaw")
        except Exception as ex:
            assert True == True
            return

        assert False == True

    def test_organisation_model_import_BIK(self):
        # подготовка
        manager = settings_manager()
        manager.open("settings.json")

        # действие
        company = organisation_model(manager.settings)

        # проверка
        assert company.BIK == manager.settings.BIK

    def test_organisation_model_import_INN(self):
        # подготовка
        manager = settings_manager()
        manager.open("settings.json")

        # действие
        company = organisation_model(manager.settings)

        # проверка
        assert company.INN == manager.settings.INN

    def test_organisation_model_import_account(self):
        # подготовка
        manager = settings_manager()
        manager.open("settings.json")

        # действие
        company = organisation_model(manager.settings)

        # проверка
        assert company.account == manager.settings.account

    def test_organisation_model_import_property_type(self):
        # подготовка
        manager = settings_manager()
        manager.open("settings.json")

        # действие
        company = organisation_model(manager.settings)

        # проверка
        assert company.property_type == manager.settings.property_type

    def test_nomenclature_atributes(self):
        # подготовка
        item = nomenclature_group_model("  name_example    ")

        # действие

        # проверка
        assert item.name == "name_example"

    def test_nomenclature(self):
        # подготвка

        item1 = nomenclature_group_model("some_nome")
        item2 = range_model("model_name", 2)
        k = 'f'*100

        # действие
        item3 = nomenclature_model("name_nome", k, item1, item2)

        # проверка
        assert item3.nom_group.name == item1.name and item2.name == item3.ran_mod.name

    def test_nomenclature_length(self):
        # подготвка
        item1 = nomenclature_group_model("some_name")
        item2 = range_model("model_name")

        # действие

        try:
            item3 = nomenclature_model("name_nome", "f"*256, item1, item2)

        except Exception as ex:
            assert True == True
            return

        assert False == True

    def test_reciepe(self):
        # подготвка
        algoritm = """Способ приготовления:
                Картофель хорошо вымойте и очистите. С лука снимите шелуху, ополосните головку водой.
                Картофель и лук натрите на крупной терке.
                Овощную массу выложите в дуршлаг, оставьте на 10 минут и удалите выделившийся сок, хорошо отжав картофель с луком.
                Переложите в объемную миску, добавьте муку. Посолите и поперчите по вкусу. По желанию добавьте другие специи.
                В сковороду влейте масло, хорошо разогрейте на сильном огне. 
                Выкладывайте массу большой ложкой, формируя оладьи, прижимая сверху лопаткой.
                Убавьте огонь до среднего и жарьте с обеих сторон по 4 минуты, до золотистости.
                Драники получаются хорошо прожаренными и хрустящими. Сразу подавайте к столу!"""

        # действие
        item = reciepe_model("     Драники         ",
                             algoritm, {"a": "b", "b": "c"})

        # проверка
        assert item.name == "Драники"
        assert item.coocking_algoritm == algoritm
        assert len(item.ingrident_proportions) != 0

    def test_id_setter(self):
        # подготвка
        item1 = nomenclature_group_model("some_nome")
        id = uuid.uuid4()

        # действие
        item1.id = id

        assert id == item1.id

    def test_reciepe_loader(self):
        # подготовка
        path_j = Path(__file__).parent/'JSONS'

        with open(path_j/('reciepe_test.json')) as j_file:
            data = json.load(j_file)

        # действие
        rec = reciepe_model._load(data['0'])

        # проверка
        assert rec.name == data['0']["name"]
        assert rec.id == uuid.UUID(data['0']["id"])

    def test_range_loader(self):
        # подготовка
        path_j = Path(__file__).parent/'JSONS'

        with open(path_j/('range_test.json')) as j_file:
            data = json.load(j_file)

        # действие

        rec = range_model._load(data['0'])
        print(rec.creation_date)

        # проверка
        assert rec.name == data['0']["name"]
        assert rec.id == uuid.UUID(data['0']["id"])

    def test_nomenclature_loader(self):
        # подготовка
        path_j = Path(__file__).parent/'JSONS'
        with open(path_j/('nomenclature_test.json')) as j_file:
            data = json.load(j_file)

        # действие
        rec = nomenclature_model._load(data['0'])

        # проверка
        assert rec.name == data['0']["name"]
        assert rec.id == uuid.UUID(data['0']["id"])

    def test_nomenclature_group_loader(self):
        # подготовка
        path_j = Path(__file__).parent/'JSONS'
        with open(path_j/('group_test.json')) as j_file:
            data = json.load(j_file)

        # действие
        rec = nomenclature_group_model._load(data['0'])

        # проверка
        assert rec.name == data['0']["name"]
        assert rec.id == uuid.UUID(data['0']["id"])
