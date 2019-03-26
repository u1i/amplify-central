## Import APIs into Amplify Central
## Please note: this is a conceptual prototype and not an officially supported script
## Author: uli@axway.com
import yaml, requests

# Get access_token from file
with open("access_token.jwt", mode='r') as tfile:
        access_token = tfile.read()
tfile.close()

# Get the list of APIs to import
apis=[]
with open("export.yaml", 'r') as stream:
    try:
        export_config = yaml.load(stream, Loader=yaml.FullLoader)

        for api in export_config["apis"]:
            apis.append(api)
    except yaml.YAMLError as exc:
        print(exc)
stream.close()

for api in apis:
    api_urlsafe = api.replace(" ", "")
    print "Importing & Deploying API " + api

    headers = {
        'Authorization': "Bearer " + access_token,
        'cache-control': "no-cache"
        }

    cfgfile = "export_" + api_urlsafe + ".yaml"
    swaggerfile = "swagger_" + api_urlsafe + ".json"

    # Import API
    url = "https://apicentral.axway.com/api/apiAggregator/v1/proxies"

    files = {
        'config': (cfgfile, open(cfgfile, 'rb'), 'text/yaml'),
        'specification': (swaggerfile, open(swaggerfile, 'rb'), 'application/json'),
    }

    r = requests.post(url, files=files, headers=headers)
    print "--- " + r.text

    # Promote API
    url = "https://apicentral.axway.com/api/apiAggregator/v1/promote"

    files = {
        'source': 'Test Runtime',
        'target': 'Test Runtime',
        'config': (cfgfile, open(cfgfile, 'rb'), 'text/yaml'),
    }

    data = { 'target': 'Test Runtime'}

    r = requests.post(url, data=data, files=files, headers=headers)
    print "--- " + r.text
