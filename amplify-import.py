import yaml

# Config

with open("export.yaml", 'r') as stream:
    try:
        export_config = yaml.load(stream, Loader=yaml.FullLoader)

        for api in export_config["apis"]:
            print api
    except yaml.YAMLError as exc:
        print(exc)
