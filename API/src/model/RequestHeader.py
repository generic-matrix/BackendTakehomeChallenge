class RequestHeader:
    def __init__(self,data):
        self.CFRequestId=data["CFRequestId"]
        if(self.CFRequestId==None):
            raise Exception("Request ID can't be none")
        self.RequestDate=data["RequestDate"]
        if(data["CFApiUserId"]==None):
            data["CFApiUserId"]='null'
        self.CFApiUserId=data["CFApiUserId"]
        if(data["CFApiPassword"]==None):
            data["CFApiPassword"]='null'
        self.CFApiPassword=data["CFApiPassword"]
        if(data["IsTestLead"]==None):
            data["IsTestLead"]='null'
        self.IsTestLead=data["IsTestLead"]