from flask import Flask,send_file,request
from pathlib import Path
from datetime import datetime
import os
import sys
import uuid
sys.path.append(os.path.join(Path(__file__).parent,'src'))
from error_proxy import error_proxy
from pathlib import Path
from storage.storage import storage
from Logic.start_factory import start_factory
from src.settings_manager import settings_manager
from Logic.report_factory import report_factory
from src.Logic.storage_sevice import storage_service
from src.Logic.nomenclature_service import nomenclature_service
from models.nomenclature_model import nomenclature_model

app=Flask(__name__)
unit=settings_manager()
address=os.path.join(Path(__file__).parent,'Jsons')
unit.open('Tester.json',address)
item=start_factory(unit.settings)
item.create()


@app.route("/api/report/<storage_key>",methods=["GET"])
def get_report(storage_key:str):
    check=[storage.unit_key(),storage.group_key(),storage.reciepe_key(),storage.nomenclature_key(),storage.journal_key()]
    factory=report_factory()

    report_type=item.options.report_type

    if storage_key in check:
        result=factory.create(report_type,item.storage.data,storage_key)
        return send_file(f'report.{report_type.lower()}')
    
    else:
        return error_proxy.create_response(app,'Ошибка ввода ключа',404)

    
@app.route("/api/storage/<nomenclature_id>/turns",methods=["GET"])
def get_nomenclature_rests(nomenclature_id:uuid.UUID):
    key=storage.journal_key()

    try:
        data=storage_service(item.storage.data[key]).create_id_turns(uuid.UUID(nomenclature_id))
    except:
        return error_proxy.create_response(app,'Ошибка ввода айди',500)

    responce_type=storage_service.create_response(data,app)
    return responce_type
    

@app.route("/api/storage/rests",methods=["GET"])
def get_rests():
    key=storage.journal_key()

    args=request.args
    if "start_period" not in args.keys():
        return error_proxy.create_response(app,'Ошибка ввода ключа',404)
    if "stop_period" not in args.keys():
        return error_proxy.create_response(app,'Ошибка ввода ключа',404)
    
    start_date= datetime.strptime(args["start_period"], "%Y-%m-%d")
    finish_date=datetime.strptime(args["stop_period"], "%Y-%m-%d")

    serv=storage_service(item.storage.data[key])
    serv.options=unit.settings
    data=serv.create_turns(start_date,finish_date)
    response_type=storage_service.create_response(data,app)

    return response_type
   

@app.route("/api/storage/<receipt_id>/debits",methods=["GET"])
def get_debits(receipt_id:str):
    response_type=app.response_class(
        response=f"not_found",
        status=404,
        mimetype="application/text"
    )

    try:
        id=uuid.UUID(receipt_id)
    except:
        return response_type
    
    journal=storage.journal_key()
    rec=storage.reciepe_key()

    for cur_reciepe in item.storage.data[rec]:
        print(id,cur_reciepe.id)

        if id==cur_reciepe.id:
            data=storage_service(item.storage.data[journal]).create_reciepe_transactions(cur_reciepe)
            response_type=storage_service.create_response(data,app)
            break 

    return response_type

@app.route("/api/storage/<nomenclature_id>/rests",methods=["GET"])
def get_sorted_turn(nomenclature_id:str):

    args=request.args
    storage_id=None

    key=storage.journal_key()
    if "storage_id" in args.keys():
        storage_id=args["storage_id"]

    try:
        #генерация работает, однако столкнулся с проблемой - тк айди каждый раз генериться случайно, узнать актуальный айди для фильтрации - можно  только из других запросов
        data=storage_service(item.storage.data[key]).create_id_turns_storage(uuid.UUID(nomenclature_id),storage_id)
    except:
        return error_proxy.create_response(app,'Ошибка ввода айди',404)
    responce_type=storage_service.create_response(data,app)

    return responce_type
    

@app.route("/api/settings/mode/<mode_type>",methods=["GET"])
def switch_mode(mode_type):
    try:
        unit.settings.is_first_start=mode_type 
        unit.save_settings()
        response=storage_service.create_response({'is_first_start':str(str(mode_type).lower()=='true')},app)
        return response
    except:
        return error_proxy.create_response(app,"wrong argument",500)


@app.route("/api/settings/mode/period",methods=["GET"])
def change_block_period():
    args=request.args
    if "block_period" not in args.keys():
        response=storage_service.create_response({'block_period':str(unit.settings.block_period)},app)
        return response
    try:
        unit.settings.block_period=args["block_period"]
        unit.save_settings()
        response=storage_service.create_response({'block_period':str(unit.settings.block_period)},app)
        return response
    except Exception as ex:
        return error_proxy.create_response(app,ex,500)


@app.route("/api/nomenclature/add",methods=["PUT"])
def add_nomenclature():
    args=request.get_json()
    if args is None:
        return error_proxy.create_response(app,"Не передан аргумент",404)

    try:
        nom=nomenclature_model._load(args)
        serv=nomenclature_service(item.storage.data[storage.nomenclature_key()])
        added=serv.add_nom(nom)
        item.storage.data[storage.nomenclature_key()]=added

        item.save()
        return nomenclature_service.create_response(args,app)

    except:
        return error_proxy.create_response(app,"Ошибка обработки",500)
    

@app.route("/api/nomenclature/change",methods=["PATCH"])
def change_nomenclature():
    args=request.get_json()
    if args is None:
        return error_proxy.create_response(app,"Не передан аргумент",404)
    try:
        nom=nomenclature_model._load(args)
        serv=nomenclature_service(item.storage.data[storage.nomenclature_key()])
        added=serv.change_nome(nom)
        item.storage.data[storage.nomenclature_key()]=added

        item.save()
        return nomenclature_service.create_response(args,app)
    except:
        return error_proxy.create_response(app,"Ошибка обработки",500)


@app.route("/api/nomenclature/delete",methods=["DELETE"])
def delete_nomenclature():
    args=request.args
    try:
        if "id" not in args.keys():
            return error_proxy.create_response(app,"не найден аргумент",404)
        nom_id=args["id"]
        serv=nomenclature_service(item.storage.data[storage.nomenclature_key()])
        added,result=serv.delete_nom(nom_id)

        if result:
            item.storage.data[storage.nomenclature_key()]=added
            item.save()
        return nomenclature_service.create_response({"result":result},app)
    except:
        return error_proxy.create_response(app,"Ошибка обработки",500)
    

@app.route("/api/nomenclature/get",methods=["GET"])
def get_nomenclature():
    args=request.args
    try:
        if "id" not in args.keys():
            factory=report_factory()
            result=factory.create("Json",item.storage.data,storage.nomenclature_key())
            return nomenclature_service.create_response(result,app)
        nom_id=args["id"]
        serv=nomenclature_service(item.storage.data[storage.nomenclature_key()])
        added=serv.get_nom(nom_id)
        return nomenclature_service.create_response(added,app)
    except:
        return error_proxy.create_response(app,"Ошибка обработки",500)

if __name__=="__main__":
    app.run(debug=True)