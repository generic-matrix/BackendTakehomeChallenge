class Business:
    def __init__(self,data):
        self.Name=data["Name"]
        self.SelfReportedCashFlow=data["SelfReportedCashFlow"]
        self.Address=data["Address"]
        self.TaxID=data["TaxID"]
        self.Phone=data["Phone"]
        self.NAICS=data["NAICS"]
        self.HasBeenProfitable=data["HasBeenProfitable"]
        self.HasBankruptedInLast7Years=data["HasBankruptedInLast7Years"]
        self.InceptionDate=data["InceptionDate"]