jwt=$(cat access_token.jwt | tr -d "\n")

curl -F "config=@export_Currency.yaml;type=text/yaml" -F "specification=@swagger_Currency.json;type=application/json" -H "Authorization: Bearer $jwt" https://apicentral.axway.com/api/apiAggregator/v1/proxies
