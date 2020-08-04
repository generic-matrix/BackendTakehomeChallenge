#To set the loan and save it into the db

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from src.model import Application as app
import datetime
from dateutil.parser import parse
#Firebase admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate(__file__.replace("/src/API.py","serviceaccount.json"))
firebase_admin.initialize_app(cred,{'databaseURL': 'https://backendtakehomechallenge.firebaseio.com'})
import traceback

#function to find the diffrence between dates
def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

#function to check if the request is available in the db in prior
def check_application_exists(application,ref):
    doc=ref.child(application.RequestHeader.CFRequestId).get()
    if(doc!=None):
        return doc
    else:
        return None
#this automaticslly updates the new changed keys and kepps the old keys same as it is
def update(ref,raw_json,data):
    obj={}
    obj[data.RequestHeader.CFRequestId]=raw_json
    ref.set(obj)

@csrf_exempt
def add_loan_application(request):
    if request.method == 'POST':
        try:
            data=request.body.decode('utf-8')
            raw_json=json.loads(json.loads(data))
            data=app.Application(raw_json)
            ref = db.reference('applications')
            logs = db.reference('log')
            doc=check_application_exists(data,ref)
            if(doc!=None):
                #save to logs
                logs.set({"CFRequestId":data.RequestHeader.CFRequestId,"action":"sending an application"})
                #check if difference between dates is more than 4 month
                now=datetime.datetime.now()
                prior_date_string=data.RequestHeader.RequestDate
                prior_date=parse(prior_date_string)
                if(diff_month(now,prior_date)>4):
                    #checking if the phone number is same
                    req_id=data.RequestHeader.CFRequestId
                    saved_data=app.Application(json.loads(json.dumps(doc)))
                    if(data.Business.Phone==saved_data.Business.Phone):
                        return HttpResponse(str({"status":"Cannot add a new application ,please add a new number and reapply"}))
                    else:
                        update(ref,raw_json,data)
                        return HttpResponse(str({"status":"ok"}))
                else:
                    return HttpResponse(str({"status":"Please reapply after 4 months"}))
            else:
                update(ref,raw_json,data)
                return HttpResponse(str({"status":"ok"}))
        except:
            #report this issue in the logs
            track = traceback.format_exc()
            print(track)
            return HttpResponse(str({"status":"Error to ingest the data as the payload is missing or invalid"}))


#function to check if the request is available in the db in prior
def get_doc_by_id(id,ref):
    doc=ref.child(id).get()
    if(doc!=None):
        obj=app.Application(json.loads(json.dumps(doc)))
        if(obj.RequestHeader.CFApiUserId=='null'):
            return HttpResponse(str({"status":"Yet to process the request"}))
        else:
            return HttpResponse(str({"status":"The reuqest is processed ,please invoke the approiate the endpoint to get the username and password"}))
    else:
        return HttpResponse(str({"status":"No such id found"}))
    

@csrf_exempt
def get_loan_application(request):
    if request.method == 'GET':
        try:
            CFRequestId=request.META['HTTP_PAYLOAD']
            ref = db.reference('applications')
            return get_doc_by_id(CFRequestId,ref)
        except Exception as e:
            #report this issue in the logs
            print(str(e))
            return HttpResponse(str({"status":"Error to process the data as the payload is missing or invalid"}))
