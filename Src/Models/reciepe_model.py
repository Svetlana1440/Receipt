from pathlib import Path
import os
import sys
import uuid


sys.path.append(Path(__file__).parent.parent)


from models.range_model import range_model
from src.models.abstract_reference import abstract_reference
from exceptions import argument_exception,operation_exception

class reciepe_model(abstract_reference):
    __coocking_algoritm=""
    __ingridient_proportions={}



    def __init__(self,name:str="untituled",algrotim:str="do whatever", propotions:dict={"a":"v"}):
        self.name=name

        self.__id=self.create_id()

        self.coocking_algoritm=algrotim

        self.ingrident_proportions=propotions


    @property    
    def id(self):
        """
            Уникальный код
        Returns:
            _type_: _description_
        """
        return self.__id    

    @id.setter
    def id(self,value:uuid.UUID):
        if not isinstance(value,uuid.UUID):
            raise argument_exception('Wrong type of argument')
        self.__id=value


    #описание рецепта
    @property
    def coocking_algoritm(self):
        return self.__coocking_algoritm
    
    @coocking_algoritm.setter 
    def coocking_algoritm(self,value: str):
        if not isinstance(value,str):
            raise argument_exception("Некорректный аргумент")
        
        value_stripped=value.strip() 

        if value_stripped=="":
            raise argument_exception("Некорректный аргумент")
        
        self.__coocking_algoritm=value_stripped

    #Пропорции ингридиентов
    @property
    def ingridient_proportions(self):
        return self.__ingridient_proportions
    
    @ingridient_proportions.setter
    def ingridient_proportions(self,value:dict):

        if not isinstance(value,dict) or len(value)==0:
            raise argument_exception("Некорректный аргумент")
        
        self.__ingridient_proportions=value

    @staticmethod
    def create_draniki():
        algoritm="""
Картофель хорошо вымойте и очистите. С лука снимите шелуху, ополосните головку водой.
Картофель и лук натрите на крупной терке.
Овощную массу выложите в дуршлаг, оставьте на 10 минут и удалите выделившийся сок, хорошо отжав картофель с луком.
Переложите в объемную миску, добавьте муку. Посолите и поперчите по вкусу. По желанию добавьте другие специи.
В сковороду влейте масло, хорошо разогрейте на сильном огне. 
Выкладывайте массу большой ложкой, формируя оладьи, прижимая сверху лопаткой.
Убавьте огонь до среднего и жарьте с обеих сторон по 4 минуты, до золотистости.
Драники получаются хорошо прожаренными и хрустящими. Сразу подавайте к столу!"""
        return reciepe_model("Драники",algoritm.replace('\n',''))
    

    @staticmethod
    def _load(data: dict):

        if data is None:
            return None
        
        if len(data)==0:
            raise argument_exception("wrong parameters")
        

        source_fields = ["id", "name","coocking_algoritm","ingridient_proportions"]

        res=reciepe_model()


        if set(source_fields).issubset(list(data.keys())) == False:
            raise operation_exception(f"Невозможно загрузить данные в объект. {data}!")
        
        res.id=uuid.UUID(data["id"])

        res.name=data["name"]

        res.coocking_algoritm=data["coocking_algoritm"]





        res.ingrident_proportions={}
        for cur_key in list(data["ingridient_proportions"].keys()):
            amount=list(data["ingridient_proportions"][cur_key].keys())


            ran_mod=list(data["ingridient_proportions"][cur_key].values())[0]


            tmp_rm=range_model._load(ran_mod)
            res.ingrident_proportions[cur_key]={amount[0]:tmp_rm}

        return res
