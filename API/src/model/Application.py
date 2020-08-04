import json
from src.model import RequestHeader as header
from src.model import Business as bis
from src.model import Owner as own
from src.model import CFApplicationData as app_data

class Application:
    def __init__(self,data):
        if(data["RequestHeader"]!=None):
            self.RequestHeader=header.RequestHeader(data["RequestHeader"])
        else:
            raise Exception("RequestHeader is none")
        
        if(data["Business"]!=None): 
            self.Business=bis.Business(data["Business"])
        else:
            raise Exception("Business is none")
        owners=data["Owners"]
        if(owners!=None):
            if(len(owners)>0):
                self.owners=[]
                for owner in owners:
                    self.owners.append(own.Owner(owner))
            else:
                raise Exception("No owners found for the business")
        else:
            raise Exception("No owners found")

        if(data["CFApplicationData"]!=None):
            self.CFApplicationData=app_data.CFApplicationData(data["CFApplicationData"])
        else:
            raise Exception("CFApplicationData is none")
        
