import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "https://apicentral.axway.com/api/apiAggregator/v1/proxies"

with open("access_token.jwt", mode='r') as tfile:
        access_token = tfile.read()
tfile.close()

headers = {
    'Authorization': "Bearer " + access_token,
    'cache-control': "no-cache"
    }

files = {
    'config': ('export_Currency.yaml', open('export_Currency.yaml', 'rb'), 'text/yaml'),
    'specification': ('swagger_Currency.json', open('swagger_Currency.json', 'rb'), 'application/json'),
}
r = requests.post(url, files=files, headers=headers)

print r.text
