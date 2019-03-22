## Export APIs from API Manager v7
## Please note: this is a conceptual prototype and not an officially supported script
## Author: uli@axway.com

import requests, json, io, urllib

# Config
apim_host="https://127.0.0.1:8075"
apim_user="apiadmin"
apim_password="changeme"
url = apim_host + "/api/portal/v1.3/discovery/apis"


auth = requests.auth.HTTPBasicAuth(apim_user, apim_password)
headers = {
    'Accept': "application/json",
    'cache-control': "no-cache"
    }

# Get All Frontend APIs
response = requests.request("GET", url, headers=headers, auth=auth, verify=False)
frontend_apis = json.loads(response.text)

with io.open('export.yaml', encoding='utf-8', mode='w') as f:

    f.write(u"apis:\n")

    # Loop through all APIs
    for api in frontend_apis:

        # Get Swagger for this API
        swagger_org = apim_host +"/api/portal/v1.3/discovery/swagger/api/" + api["name"]
        swagger = swagger_org.replace(apim_host, '')
        querystring = {"swaggerVersion":"2.0","filename":"Currency.json"}

        response = requests.request("GET", swagger_org, headers=headers, params=querystring, auth=auth, verify=False)
        swagger_doc = json.loads(response.text)

        # Write Swagger file
        export_sname="swagger_" + api["name"].replace(" ", "") + ".json"
        with io.open(export_sname, encoding='utf-8', mode='w') as s:
            s.write(response.text)
        s.close()

        # Upload Swagger
        # url = "https://transfer.sh"

        # payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"" + export_sname + "\"\r\nContent-Type: application/json\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        #headers = {
        #    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        #    'Content-Type': "application/x-www-form-urlencoded",
        #    'cache-control': "no-cache"
        #    }

        #response = requests.request("POST", url, data=payload, headers=headers)
        #tsh_swagger_url = response.text

        print api["name"] + ": " + swagger + " " + swagger_doc["basePath"] + " " + swagger_doc["host"]

        # Write API info to export file
        f.write("    " + api["name"] + ": " + swagger + "\n")

        # Create a YAML file for API
        export_fname="export_" + api["name"].replace(" ", "") + ".yaml"
        with io.open(export_fname, encoding='utf-8', mode='w') as x:
            x.write(u"apiVersion: v1\n")
            x.write(u"proxy:\n")
            x.write(u"    name: '" + api["name"] + "'\n")
            x.write(u"    basePath: " + swagger_doc["basePath"] + "\n")
            x.write(u"    policy:\n")
            x.write(u"        type: pass-through\n")
            x.write(u"    team:\n")
            x.write(u"        name: 'Default Team'\n")
        x.close()
    f.close()
