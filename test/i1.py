import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "https://apicentral.axway.com/api/apiAggregator/v1/proxies"

with open("access_token.jwt", mode='r') as tfile:
        access_token = tfile.read()
tfile.close()

#payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"config\"; filename=\"export_Currency.yaml\"\r\nContent-Type: text/yaml\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"specification\"; filename=\"swagger_Currency.json\"\r\nContent-Type: application/json\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

headers = {
    'Authorization': "Bearer " + access_token,
    'cache-control': "no-cache"
    }
files = {'config': open('export_Currency.yaml', 'rb').read(), 'specification': open('swagger_Currency.json', 'rb').read()}


#response = requests.request("POST", url, data=payload, headers=headers)
#print files
#response = requests.post(url, headers=headers, files=files)

#print(response.text)


m = MultipartEncoder(fields={'config': ('filename', open('export_Currency.yaml', 'rb'), 'text/yaml'), 'specification': ('filename', open('swagger_Currency.json', 'rb'), 'application/json')})

r = requests.post(url, data=m, headers=headers)

print r.text
