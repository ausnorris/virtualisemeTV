import requests
import json
import random
import time

def handler(context, inputs):
    if 'resourceNames' not in inputs:
        resourceName = inputs["externalIds"][0]
    else:
        resourceName = inputs["resourceNames"][0]
        
    #resourceName = inputs["resourceNames"][0]
    headers = {"Accept":"application/json","Content-Type":"application/json","Authorization": inputs["bearer"]}
    url = "https://(something).wavefront.com/api/v2/source/" + resourceName;
    num = random.randint(1,10)
    time.sleep(num)
    results = requests.delete(url,headers=headers).json()
    print("This is the result: " + json.dumps(results))


    
