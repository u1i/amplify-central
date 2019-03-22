# A little Helper Script to get your Amplify Central Access Token
# You need: amplify command line tool, jq, your key.pem and DOSA_XXX.json file in order for this to work

dosa=$(ls DOSA* | sed "s/\.json//")
echo $dosa

amplify auth login --realm AppcID --json --secret-file key.pem --client-id DOSA_e91221af051e4a5493b680dc8684de98 | jq ".tokens.access_token" | tr -d '"' > access_token.jwt
