from ast import Dict
from urllib.request import urlopen
import json
from pprint import pprint


url = "https://random-data-api.com/api/commerce/random_commerce?size=100"

response = urlopen(url)
data = json.loads(response.read())
dic= dict()
dic["product_name"] = []
dic["id"] = []
dic["uid"] = []
dic["department"] = []

 
for i in data:
    print(i)
    break

for i in data:
    #print(i)
    if i ["uid"] not in dic["uid"]:
        
        dic["uid"].append(i["uid"]),
        dic["product_name"].append(i["product_name"]),
        dic["id"].append(i["id"]),
        dic["department"].append(i["department"])

pprint(dic)