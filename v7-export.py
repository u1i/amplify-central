## Export APIs from API Manager v7
## Please note: this is a conceptual prototype and not an officially supported script
## Author: uli@axway.com

import requests, json, io, urllib

apim_host="https://127.0.0.1:8075"
apim_user="apiadmin"
apim_password="changeme"
url = apim_host + "/api/portal/v1.3/discovery/apis"

auth = requests.auth.HTTPBasicAuth(apim_user, apim_password)

headers = {
    'Accept': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, auth=auth, verify=False)

frontend_apis = json.loads(response.text)
#print(response.text)

with io.open('export.yaml', encoding='utf-8', mode='w') as f:
    for api in frontend_apis:

        swagger = apim_host +"/api/portal/v1.3/discovery/swagger/api/" + api["name"]

        print api["name"] + ": " + swagger
        f.write(api["name"] + ": " + swagger + "\n")
    f.close()
