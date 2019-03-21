# Getting Started with Amplify Central API

## Goal

Programmatic access to Amplify Central via API calls for importing APIs, managing the catalog & DevOps processes. This guide shows you how you authenticate against the API endpoints and has a couple of examples on how to use them to accomplish common tasks.

## Requirements

* Access to [Amplify Central](https://apicentral.axway.com)
* [NodeJS](https://nodejs.org/en/) and OpenSSL installed on your machine to generate keys & access tokens
* cURL, Postman etc. for interacting with the API endpoints

## How Authentication Works

Amplify Central API endpoints require a "Bearer' token in the HTTP header - it's a JWT token that expires after a while. To get an access token, you''l need to create a service account in Amplify Central, download a JSON config file and use a command line tool to generate the token.


## Step 1 - Create Service Account

Login into Amplify Central and select 'Service Accounts' in the 'Access' tab.

![](./resources/apic-api1.png)

You're going to create a new service account, choose any name (ideally without spaces or special characters). The dialog expects a public key, you can generate one on the command line using OpenSSL:

`openssl genrsa -out key.pem 2048`   
`openssl rsa -in key.pem -outform PEM -pubout -out public.pem`

Open the file `public.pem` in a text editor, and copy/paste it from there into the form:

![](./resources/apic-api2.png)

Once this is done, you can download a JSON config file from Amplify Central. Save the Client ID ("DOSA_XXXX") in a text editor.

![](./resources/apic-api3.png)

## Step 2 - Generate Access Token with the CLI

The Amplify command line tool takes in the configuration file & keys you've created in the previous step to generate an access token. Install it with:

`npm i -g @axway/amplify-cli`

You can then use the following command to get the token:

`amplify auth login --realm AppcID --json --secret-file key.pem --client-id DOSA_e91221af051e4a5493b680dc8684de98 | jq ".tokens.access_token" | tr -d '"'`

The result should look like this:

> {
  "authenticator": "SignedJWT",
  "baseUrl": "https://login.axway.com",
  "clientId": "DOSA_e91221XXXXXXXXXXXXXX",
  "env": "prod",
  "expires": {
    "access": 1553146464862,
    "refresh": 1553166264862
  },
  "hash": "DOSA_e91221af051e4a5493b680dc8684de98:526247f236dacc0879ea1921fe664fc4",
  "name": "DOSA_e91221af051e4a5493b680dc8684de98:526247f236dacc0879ea1921fe664fc4",
  "realm": "AppcID",
  "tokens": {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTTFpLQmpKbDdmQVpFRDFONzF5S21oZkc3YzJrVm9IREQwdVlQWndEOXpnIn0.eyJqdGkiOiI5MDg2NmJmNC0xY2M2LTQwZjUtOGU3YS0yZjE2ZmI0OWJmYzgiLCJleHAiOjE1NTMxNDY0NjQsIm5iZiI6MCwiaWF0IjoxNTUzMTQ0NjY0LCJpc3MiOiJodHRwczovL2xvZ2luLmF4d2F5LmNvbS9hdXRoL3JlYWxtcy9BcHBjSUQiLCJhdWQiOiJET1NBX2U5MTIyMWFmMDUxZTRhNTQ5M2I2ODBkYzg2ODRkZTk4Iiwic3ViIjoiYTJmODk5MWYtNjZmNy00NzhmLTkzNzctNzg2MGUxMjQ5NTZiIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiRE9TQV9lOTEyMjFhZjA1MWU0YTU0OTNiNjgwZGM4Njg0ZGU5OCIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImY4YmE4ZTU1LWI2N2YtNDUwMS05YjJmLTM4ZGEyMjA2YTIzOCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOltdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJjbGllbnRJZCI6IkRPU0FfZTkxMjIxYWYwNTFlNGE1NDkzYjY4MGRjODY4NGRlOTgiLCJlbnZpcm9ubWVudElkIjoiZTkxMjIxYWYwNTFlNGE1NDkzYjY4MGRjODY4NGRlOTgiLCJjbGllbnRIb3N0IjoiNDMuMjQ4LjIxMi4xOSIsImNsaWVudEFkZHJlc3MiOiI0My4yNDguMjEyLjE5Iiwib3JnSWQiOiI5NjY5ODE5OTI4MjgzNzcifQ.K0M_4MHuflDGUwO-25aPkEo0RHLfXvRB0RSXdGNJnNrUl6Dm5kHs3kuoxCTp6I1boLtM89wcsZEU5IOiPbtAMCsm7JCFcfRNdWKin-Ls6SrEllF5sFUyhCdtoXbfeirOvIjXKFXvt3tjZ8BTIYQL9iNJ8CYoHhiEFAV79X7n16UeToQxbzQ4JwqZeeO2rsWEGSsUgHdERao1B0rAnucv00AWqfr8OPu8sHuMQiUhDkEhYPyLMXNM4EYqKnPXdry5CjB5hdN6pD-BwfyCq_EZZxEfNYqnYiPOAjifXXXXXXXXXX63J1b6dsQ",
    "expires_in": 1800,
    "refresh_expires_in": 21600,
    "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTTFpLQmpKbDdmQVpFRDFONzF5S21oZkc3YzJrVm9IREQwdVlQWndEOXpnIn0.eyJqdGkiOiI4MTQwZDM5Yi02N2MyLTQwNWQtYmI1Zi1lMWM5ZDUwZDdhYjciLCJleHAiOjE1NTMxNjYyNjQsIm5iZiI6MCwiaWF0IjoxNTUzMTQ0NjY0LCJpc3MiOiJodHRwczovL2xvZ2luLmF4d2F5LmNvbS9hdXRoL3JlYWxtcy9BcHBjSUQiLCJhdWQiOiJET1NBX2U5MTIyMWFmMDUxZTRhNTQ5M2I2ODBkYzg2ODRkZTk4Iiwic3ViIjoiYTJmODk5MWYtNjZmNy00NzhmLTkzNzctNzg2MGUxMjQ5NTZiIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6IkRPU0FfZTkxMjIxYWYwNTFlNGE1NDkzYjY4MGRjODY4NGRlOTgiLCJhdXRoX3RpbWUiOjAsInNlc3Npb25fc3RhdGUiOiJmOGJhOGU1NS1iNjdmLTQ1MDEtOWIyZi0zOGRhMjIwNmEyMzgiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19fQ.LjpPCzZ_eLXuU0KiqJ5Q3eF0ZFY3cNcIP8G3QJbdYQDHoBtOXI5ptdk7BWB_s39-0VLmgk7kJQHRuYenpHRUcfEkzyR1NE8_wB7TmQN_dfB998BU1Vd_iBBC1qMHgxbm8Iz8nX1ySUHkvW-jVCryQV7F0c96KjN_FvouXTp-sfq1wr_r18yW0e5RP-u8NDfublM88Ortl4VptMH3uwLPq25s8u9NZ3xFSwUUydpeud4bXEv355clISxw59lEd2tlGgk7IdLgT5bh29XDFczVghnDgVOXXXXXXXXXTvquVcn-nchNM06h2e2Q42uKo3JQMfZqTDoh-TS7Q",
    "token_type": "bearer",
    "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTTFpLQmpKbDdmQVpFRDFONzF5S21oZkc3YzJrVm9IREQwdVlQWndEOXpnIn0.eyJqdGkiOiI2ZGMyMzljZi1lMWJjLTQ2ZjYtOTQ2YS04MzExYzQzZmEzNDAiLCJleHAiOjE1NTMxNDY0NjQsIm5iZiI6MCwiaWF0IjoxNTUzMTQ0NjY0LCJpc3MiOiJodHRwczovL2xvZ2luLmF4d2F5LmNvbS9hdXRoL3JlYWxtcy9BcHBjSUQiLCJhdWQiOiJET1NBX2U5MTIyMWFmMDUxZTRhNTQ5M2I2ODBkYzg2ODRkZTk4Iiwic3ViIjoiYTJmODk5MWYtNjZmNy00NzhmLTkzNzctNzg2MGUxMjQ5NTZiIiwidHlwIjoiSUQiLCJhenAiOiJET1NBX2U5MTIyMWFmMDUxZTRhNTQ5M2I2ODBkYzg2ODRkZTk4IiwiYXV0aF90aW1lIjowLCJzZXNzaW9uX3N0YXRlIjoiZjhiYThlNTUtYjY3Zi00NTAxLTliMmYtMzhkYTIyMDZhMjM4IiwiYWNyIjoiMSIsImNsaWVudElkIjoiRE9TQV9lOTEyMjFhZjA1MWU0YTU0OTNiNjgwZGM4Njg0ZGU5OCIsImVudmlyb25tZW50SWQiOiJlOTEyMjFhZjA1MWU0YTU0OTNiNjgwZGM4Njg0ZGU5OCIsImNsaWVudEhvc3QiOiI0My4yNDguMjEyLjE5IiwiY2xpZW50QWRkcmVzcyI6IjQzLjI0OC4yMTIuMTkiLCJvcmdJZCI6Ijk2Njk4MTk5MjgyODM3NyJ9.TNuzOKeo4D0LP1MCto9JjsdODDbQwtJLPhHvp8i5FyqVv_nC-t5kBunceCeWrfpnd0K_XfSqbpskXXXXXovZszR0uiOAt3AoA-Po417AMzWoAjy4w5fCU0hrkXk1ngGazgcu7rp0ILHuvIqexbQ7CCfy7A6__IsLM8wp2v6d5iXh7VE_DFEY0mr7n4oSTD2jLPbXXXXXXXimr2MxNaId-pkhP70IcoGHV2hKAGRGkoviyzxFcyRYmMPqn1tFcVrSw18r3_mlrTd4MEEkGC_g0-8JS-xhidCvBi8-tKq94ubIMC0y9DsZb_YxtorKDydgJxTqBLGGEIqJmWcDvuPwbOQg1g",
    "not-before-policy": 0,
    "session_state": "f8ba8e55-b67f-4501-9b2f-38da2206a238",
    "scope": ""
  },
  "org": {
    "name": "96698XXX828377",
    "org_id": "9669XXX8377"
  },
  "orgs": [
    {
      "name": "966XXX828377",
      "org_id": "9669XXX28377"
    }
  ],
  "user": {
    "axwayId": null,
    "organization": null
  },
  "active": true
}

If you have [jq](https://stedolan.github.io/jq/) installed you could also use this shortcut to get just the token:

`amplify auth login --realm AppcID --json --secret-file key.pem --client-id DOSA_e91221af051e4a5493b680dc8684de98 | jq ".tokens.access_token" | tr -d '"'`

> eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTTFpLQmpKbDdmQVpFRDFONzF5S21oZkc3YzJrVm9IREQwdVlQWndEOXpnIn0.eyJqdGkiOiI5MDg2NmJmNC0xY2M2LTQwZjUtOGU3YS0yZjE2ZmI0OWJmYzgiLCJleHAiOjE1NTMxNDY0NjQsIm5iZiI6MCwiaWF0IjoxNTUzMTQ0NjY0LCJpc3MiOiJodHRwczovL2xvZ2luLmF4d2F5LmNvbS9hdXRoL3JlYWxtcy9BcHBjSUQiLCJhdWQiOiJET1NBX2U5MTIyMWFmMDUxZTRhNTQ5M2I2ODBkYzg2ODRkZTk4Iiwic3ViIjoiYTJmODk5MWYtNjZmNy00NzhmLTkzNzctNzg2MGUxMjQ5NTZiIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiRE9TQV9lOTEyMjFhZjA1MWU0YTU0OTNiNjgwZGM4Njg0ZGU5OCIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImY4YmEXXXXXXDUwMS05YjJmLTM4ZGEyMjA2YTIzOCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOltdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJjbGllbnRJZCI6IkRPU0FfZTkxMjIxYWYwNTFlNGE1NDkzYjY4MGRjODY4NGRlOTgiLCJlbnZpcm9ubWVudElkIjoiZTkxMjIxYWYwNTFlNGE1NDkzYjY4MGRjODY4NGRlOTgiLCJjbGllbnRIb3N0IjoiNDMuMjQ4LjIxMi4xOSIsImNsaWVudEFkZHJlc3MiOiI0My4yNDguMjEyLjE5Iiwib3JnSWQiOiI5NjY5ODE5OTI4MjgzNzcifQ.K0M_4MHuflDGUwO-25aPkEo0RHLfXvRB0RSXdGNJnNrUl6Dm5kHs3kuoxCTp6I1boLtM89wcsZXXXXXsm7JCFcfRNdWKin-Ls6SrEllF5sFUyhCdtoXbfeirOvIjXKFXvt3tjZ8BTIYQL9iNJ8CYoHhiEFAV79X7n16UeToQxbzQ4JwqZeeO2rsWEGSsUgHdERao1B0rAnucv00AWqfr8OPu8sHuMQiUhDkEhYPyLMXNM4EYqKnPXdry5CjB5hdN6pD-BwfyCq_EZZxEfNYqnYiPOAjifV09OhHLYLiT2B7f5WTwBrDM9AlduIaJBTE7qbj8LR63J1b6dsQ

Save this one in a text editor - it's your Bearer token for the requests against the endpoints you're going to make in the next step.

If you're curious what the token contains you could use base64 to decode it:

> {"jti":"90866bf4-1cc6-XXX-8e7a-2f16fbXbfc8","exp":1553146464,"nbf":0,"iat":15XXX44664,"iss":"https://login.axway.com/auth/realms/AppcID","aud":"DOSA_e91221aXXXXXX84de98","sub":"a2f8991XXX478f-9377-7860e124956b","typ":"Bearer","azp":"DOSA_e91221af051e4a5493b680dc8684de98","auth_time":0,"session_state":"f8ba8e55-b67f-4501-9b2f-XXXX06a238","acr":"1","allowed-origins":[],"realm_access":{"roles":["uma_authorization"]},"resource_access":{"account":{"roles":["manage-account","manage-account-links","view-profile"]}},"clientId":"DOSA_e9XXXXXX684de98","environmentId":"e91221af051e4a5493XXXe98","clientHost":"X.X.X.X","clientAddress":"X.X.X.X","orgId":"966981XXXXXX28377"

## Step 3 - Use Amplify Central API Endpoints

The tab 'API Proxies' shows the list of APIs that are managed by your organization/user in Amplify Central:

![](./resources/apic-api4.png)

Now we'd like to get that same information – with an API call!
You can use the attached Postman Collection, or simply do it in cURL like this:

`curl -H 'Authorization: Bearer __TOKEN__ https://apicentral.axway.com/api/v1/apis`

In my case, this would look like this:

`curl https://apicentral.axway.com/api/v1/apis -H 'Authorization: Bearer eyJhbGciOiJSUzI1NXXXXX2lkIiA6ICJTTFpLQmpKbDdmQVpFRDFONzF5S21oZkc3YzJrVm9IREQwdVlQWndEOXpnIn0.eyJqdGkiOiI5MDg2NmJmNC0xY2M2LTQwZjUtOGU3YS0yZjE2ZmI0OWJmYzgiLCJleHAiOjE1NTMxNDY0NjQsIm5iZiI6MCwiaWF0IjoxNTUzMTQ0NjY0LCJpc3MiOiJodHRwczovL2xvZ2luLmF4d2F5LmNvbS9hdXRoL3JlYWxtcy9BcHBjSUQiLCJhdWQiOiJET1NBX2U5MTIyMWFmMDUxZTRhNTQ5M2I2ODBkYzg2ODRkZTk4Iiwic3ViIjoiYTJmODk5MWYtNjZmNy00NzhmLTkzNzctNzg2MGUxMjQ5NTZiIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiRE9TQV9lOTEyMjFXXXXXXXmF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImY4YmE4ZTU1LWI2N2YtNDUwMS05YjJmLTM4ZGEyMjA2YTIzOCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOltdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJjbGllbnRJZCI6IkRPU0FfZTkxMjIxYWYwNTFlNGE1NDkzXXXXXXXiNDMuMjQ4LjIxMi4xOSIsImNsaWVudEFkZHJlc3MiOiI0My4yNDguMjEyLjE5Iiwib3JnSWQiOiI5NjY5ODE5OTI4MjgzNzcifQ.K0M_4MHuflDGUwO-25aPkEo0RHLfXvRB0RSXdGNJnNrUl6Dm5kHs3kuoxCTp6I1boLtM89wcsZEU5IOiPbtAMCsm7JCFcfRNdWKin-Ls6SrEllF5sFUyhCdtoXbfeirOvIjXKFXvt3tjZ8BTIYQL9iNJ8CYoHhiEFAV79X7n16UeToQxbzQ4JwqZeeO2rsWEGSsUgHdERao1B0rAnucv00AWqfr8OPu8sHuMQiUhDkEhYPyLMXNM4EYqKnPXdry5CjB5hdN6pD-BwfyCq_EZZxEfXXXBrDM9AlduIaJBTE7qbj8LR63J1b6dsQ'`

> [
    {
        "id": "e4e6dfdXXXXX4d71f60002",
        "name": "Musical Instruments",
        "state": {
            "value": "ACTIVE"
        },
        "metadata": {
            "createTimestamp": "2019-03-20T04:13:03.359Z",
            "createUserId": "DOSA_e9XXXX3b680dc8684de98",
            "modifyTimestamp": "2019-03-20T04:30:23.919Z",
            "modifyUserId": "DOSA_e9XXXXX493bXX84de98"
        },
        "revision": [
            1,
            2
        ],
        "tags": [
            "musical",
            "instruments"
        ],
        "owningTeamId": "e4f50cXXXXXf8fb620186"
    },
    {
        "id": "e4f8XXXX7a0227d4007d",
        "name": "Yoisho Currency Exchange",
        "state": {
            "value": "ACTIVE"
        },
        "description": "simple currency API",
        "metadata": {
            "createTimestamp": "2019-03-14T02:22:35.478Z",
            "createUserId": "e4fXXXXXX74f8fe5a01d5",
            "modifyTimestamp": "2019-03-14T02:22:35.478Z",
            "modifyUserId": "e4fXXXXf8fe5a01d5"
        },
        "revision": [
            1
        ],
        "tags": [],
        "owningTeamId": "e4fXXXXX20186"
    },
    {
        "id": "e4f8d6XXXX753960290219",
        "name": "apibuilder-autobuild",
        "state": {
            "value": "PUBLISHED"
        },
        "description": "An API Builder service",
        "metadata": {
            "createTimestamp": "2019-03-13T04:04:48.312Z",
            "createUserId": "eXXXXX3016974f8fe5a01d5",
            "modifyTimestamp": "2019-03-13T04:05:34.851Z",
            "modifyUserId": "e4fXXXXXf8fe5a01d5"
        },
        "revision": [
            1
        ],
        "tags": [],
        "owningTeamId": "e4XXXXXX8fb620186"
    }
]

With this, you should be able to use all the other [API endpoints](http://swagger.sotong.io/?url=https://apicentral.axway.com/api/v1/docs) in Amplify Central.



