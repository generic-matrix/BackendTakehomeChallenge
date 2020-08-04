class CFApplicationData:
    def __init__(self,data):
        self.RequestedLoanAmount=data["RequestedLoanAmount"]
        self.StatedCreditHistory=data["StatedCreditHistory"]
        self.LegalEntityType=data["LegalEntityType"]
        self.FilterID=data["FilterID"]
	