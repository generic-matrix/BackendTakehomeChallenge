#Basic unit testing using cURL using basic request framework
import urllib.request
import json
DEBUG_URL="https://backendservice-5nf433gcyq-uc.a.run.app/"
SAMPLE_JSON_DIR="/Users/kaustubh/Desktop/BackendTakehomeChallenge/sample.json"

file=open(SAMPLE_JSON_DIR,"r")
payload=file.read()
file.close()

print("---- Post the sample data from the JSON to the /loanapp---- \n ")
req = urllib.request.Request(DEBUG_URL+"loanapp/")
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(payload)
jsondataasbytes = jsondata.encode('utf-8')
req.add_header('Content-Length', len(jsondataasbytes))
response = urllib.request.urlopen(req, jsondataasbytes)
print(response.read().decode("utf-8"))
print("-----------------------")


print("---- POSTING JSON but application date  > 4 month /loanapp (sending the same data)---- \n ")
req = urllib.request.Request(DEBUG_URL+"loanapp/")
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(payload)
jsondataasbytes = jsondata.encode('utf-8')
req.add_header('Content-Length', len(jsondataasbytes))
response = urllib.request.urlopen(req, jsondataasbytes)
print(response.read().decode("utf-8"))
print("-----------------------")


print("---- Getting the application data by taking the id : if available --- \n ")
req = urllib.request.Request(DEBUG_URL+"status/")
req.add_header('payload',"500653901")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
print("-----------------------")

print("---- Getting the application data by taking the id : if available --- \n ")
req = urllib.request.Request(DEBUG_URL+"status/")
req.add_header('payload',"50065390100")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8") )
print("-----------------------")



