from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent,'models'))

from datetime import datetime
from models.range_model import range_model
from models.reciepe_model import reciepe_model
from storage.storage import storage
from exceptions import argument_exception
from models.nomenclature_model import nomenclature_model,nomenclature_group_model,range_model
from src.storage.storage_factory import storage_factory
from src.Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from src.Logic.storage_sevice import storage_service
from src.storage.storage_turn_model import storage_turn_model
from storage.storage_model import storage_model
from settings import settings
from error_proxy import error_proxy
import json

class start_factory:

    __options:settings=None
    __storage:storage=None
    __storage_path=Path(__file__).parent.parent/'storage'/'saved_models'

    def __init__(self,options:settings,stor:storage=None):
        self.__options=options
        self.__storage=stor


    def __save(self):
            reference=reference_conventor(nomenclature_model,
                                          reciepe_model,
                                            nomenclature_group_model,
                                            range_model,
                                            error_proxy,
                                            storage_turn_model)
            for cur_key in list(self.__storage.data.keys()):
                result_json={}
                for index,cur_val in enumerate(self.__storage.data[cur_key]):
                    result_json[index]=reference.convert(cur_val)

                with open(self.__storage_path/f'{cur_key}.json','w') as saving:
                    saving.write(json.dumps(result_json))



            


    def __build(self,nom:list):
        if self.__storage==None:
            self.__storage=storage()






        nom=start_factory.create_nomenclature()
        #добавляем в data 
        self.__storage.data[storage.nomenclature_key()]=nom[0]
        self.__storage.data[storage.unit_key()]=nom[1]      
        self.__storage.data[storage.group_key()]=nom[2]
        self.__storage.data[storage.reciepe_key()]=nom[3]

        serv=storage_service(nom[4])
        serv.options=self.__options
        self.__storage.data[storage.b_turn_key()]=serv.create_blocked_turns()


        #сохраняем
        self.__save()

        self.__storage.data[storage.journal_key()]=nom[4]
                                                       


    @property
    def storage(self):
        return self.__storage

    @staticmethod
    def create_nomenclature():
        #создаём группы
        group=nomenclature_group_model.create_group()
        group_meat=nomenclature_group_model.create_group_meat()
        group_eggs=nomenclature_group_model.create_group_eggs()
        group_vegs=nomenclature_group_model.create_group_vegs()

        Output=[]

        journal=[]


        #создаём еденицы
        sp=range_model.create_spoon()
        kg=sp.base_range
        gr=kg.base_range
        
        l=range_model.create_litr()
        ml=l.base_range

       
        
        sht=range_model.create_shtuka()


        #создаём рецепты через фабричный метод в reciepe_model
        draniki=reciepe_model.create_draniki()
        


        #добавляем в номенклатуру
        Output.append(nomenclature_model('Пшеничная мука','Пшеничная мука',group,kg))
        Output.append(nomenclature_model('сахар','сахар',group,kg))
        Output.append(nomenclature_model('масло','масло',group,gr))
        Output.append(nomenclature_model('яйца','яйца',group_eggs,sht))
        Output.append(nomenclature_model('ванилин','ванилин',group,gr))
        Output.append(nomenclature_model('яичный белок','яичный белок',group_eggs,sht))
        Output.append(nomenclature_model('сахарная пудра','сахарная пудра',group,kg))
        Output.append(nomenclature_model('корица','корица',group,gr))
        Output.append(nomenclature_model('какао','какао',group,gr))
        Output.append(nomenclature_model("куринное филе","куринное филе",group_meat,kg))
        Output.append(nomenclature_model("салат романо","салат романо",group_vegs, gr))
        Output.append(nomenclature_model("сухари","сухари",group,kg))
        Output.append(nomenclature_model('картофель','картофель',group,sht))
        Output.append(nomenclature_model('лук репчатый','лук репчатый',group,sht))
        Output.append(nomenclature_model('соль','соль',group,gr))



        #создаём журнал ******ПЕРЕНЕСТИ В ОТДЕЛЬНУЮ ФУНКЦИЮ********
        stor1=storage_model('переулок штукатуров 212')
        stor2=storage_model('проспект блин-не-туда-свернул 11')
        date1=datetime(2024,1,15)
        date2=datetime(2023,12,12)
        date3=datetime(2024,2,20)
        date4=datetime(2023,11,20)
        date5=datetime(2023,3,4)
        

        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(True,Output[2],242,date1)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(False,Output[2],202,date2)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(True,Output[5],100,date3)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(True,Output[6],2,date4)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(False,Output[2],300,date5)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(True,Output[1],122,date1)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(False,Output[0],451,date2)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(True,Output[6],4652,date3)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(False,Output[8],1231,date4)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(True,Output[7],12,date5)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(False,Output[8],213,date1)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(True,Output[4],451,date2)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(False,Output[4],231,date3)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(True,Output[3],4512,date4)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(True,Output[2],10,date5)))
        journal.append(storage_factory.create_row(stor2,storage_factory.create_transaction(False,Output[1],218,date1)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(True,Output[3],5456,date2)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(False,Output[7],123,date3)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(True,Output[9],54,date4)))
        journal.append(storage_factory.create_row(stor1,storage_factory.create_transaction(False,Output[2],242,date5)))





        #создаём пропорции для рецептов (словарь типа {ингридиент:{количество : единица измерения}})
        draniki_prop={Output[2].id:{2:sp},Output[0].id:{2:sp},Output[12].id:{7:sht},Output[13].id:{1:sht},Output[14].id:{2:gr}}

        draniki.ingridient_proportions=draniki_prop

        return [Output,[kg,gr,l,ml,sht,sp],[group,group_eggs,group_vegs,group_meat],[draniki],journal]


    def create(self):
        if self.__options.is_first_start:
            self.__options.is_first_start='False'
            ret=start_factory.create_nomenclature()
            self.__build(ret)
            return ret
        
        else:
            items=self.__load_models()
            self.__build(items)
            return items
        

    def save(self):
        self.__load_models()
        

    def __load_models(self):
        res=[]
        loader=[nomenclature_model._load,range_model._load,nomenclature_group_model._load,reciepe_model._load]
        keys=[storage.nomenclature_key(),storage.unit_key(),storage.group_key(),storage.reciepe_key()]

        for index,cur_key in enumerate(keys):
            print(index)
            with open(self.__storage_path/f'{cur_key}.json') as source:
                cur_json=json.load(source)
                tmp_res=[]
                for cur_value in list(cur_json.values()):
                    tmp_res.append(loader[index](cur_value))
                res.append(tmp_res)
        res.append([])
        return res





    @property
    def options(self):
        return self.__options
    
    @options.setter
    def options(self,value):
        if not isinstance(value,settings):
            raise argument_exception("Неверный аргумент")
        
        self.__options=value

