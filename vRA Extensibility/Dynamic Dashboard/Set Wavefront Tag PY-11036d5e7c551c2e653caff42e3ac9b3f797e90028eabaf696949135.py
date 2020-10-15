import requests
import json
import random
import time

def handler(context, inputs):
    
    jsonInputs = json.loads(json.dumps(inputs["wavefront"]))
    headers = {"Accept":"application/json","Content-Type":"application/json","Authorization": inputs["bearer"]}
    if "resourceNames" in inputs:
        resourceName = inputs["resourceNames"][0]
        print("resource is a machine")
    else:
        print("resource is a LB")
        resourceName = inputs["externalIds"][0]
    for key in jsonInputs:
        print(jsonInputs[key])
        url = "https://(something).wavefront.com/api/v2/source/" + resourceName + "/tag/" + jsonInputs[key];
        num = random.randint(1,60)
        time.sleep(num)
        results = requests.put(url,headers=headers).json()
        print("This is the result: " + json.dumps(results))


    