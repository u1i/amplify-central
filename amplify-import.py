import yaml

# Config

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

print apis
