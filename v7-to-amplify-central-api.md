# Export, Publish & Consume APIM 7.x APIs with Amplify Central

## Scenario

You're running a setup of Axway API Manager v7 to manage, protect & consume on premise APIs. [Amplify Central](https://apicentral.axway.com) gives you a control plane on the cloud – manage, consume & analyze. This guide gives you an overview and a couple of tools (scripts & Postman collection) for making existing API endpoints (managed by an API v7 environment) available in Amplify Central.

We'll use a simplified setup for this exercise to illustrate the concept and show you the tools you can use. Of course, your environment will be different in the way you've set up and configured API Management, particularly around security, firewalling, virtual hosts & integration of identity management.

![](./resources/v7apic1.png)

## You need

* An existing setup of API Manager / Gateway v7
* Some virtualized endpoints in API Manager.
* Access to [Amplify Central](https://apicentral.axway.com)
* Python 2.7 runtime environment on your local machine to run the helper scripts
* Bearer Token for API Access - see [Getting Started Guide](api-getting-started.md)

## Starting Point: API Manager v7

Let's look at our initial state, we have two API endpoints (from the [Yoisho Open Banking Project](https://github.com/u1i/yoisho)) virtualized in API Manager running in a dockerized environment on my local machine:

![](./resources/v7-1.png)

If you use API Portal, the typical consumer will see something like this when selecting one of the APIs:

![](./resources/v7-2.png)

Let's use cURL commands to see the APIs in action:

`curl -k "https://localhost:8065/curr/currency?currency=USD"`

> {"sell": "489.111", "timestamp": "2019-03-21 07:09:47.407662", "buy": "389.108"}

`curl -k "https://localhost:8065/banking/v2/atm"`

> {"result": [{"lat": "35.6684231", "lon": "139.6833085", "location": "Ebisu Station", "id": "2"}, {"lat": "35.6284713", "lon": "139.736571", "location": "Shinagawa Station", "id": "1"}]}

# Step 1: Export APIs

Let's use the [API Manager v7 API](http://apidocs.axway.com/api_documentation/apimanager/7.5.3/api-manager-V_1_3-swagger.json) to export the APIs that are managed by this instance.

You could choose to temporarily change the password for 'apiadmin' for this exercise.

The [Postman Collection](apimv7-postman.json) contains the examples for listing all virtualized APIs, getting details and the Swagger definitions for each API.

A cURL command to retrieve all API endpoints could look like this, assuming the credentials for 'apiadmin' include the default password:

`curl -X GET https://127.0.0.1:8075/api/portal/v1.3/discovery/apis -H 'Accept: application/json' -H 'Authorization: Basic YXBpYWRtaW46Y2hhbmdlbWU='`

> [
    {
        "name": "ATM Locator",
        "summary": null,
        "id": "61b0ddf9-f0b3-43aa-b984-be2b789749c6",
        "uri": "https://127.0.0.1:8075/api/portal/v1.3/discovery/swagger/api/ATM+Locator",
        "type": "rest"
    },
    {
        "name": "Currency",
        "summary": null,
        "id": "d6c9ec45-889d-4ba5-9a79-ef800c95dbc6",
        "uri": "https://127.0.0.1:8075/api/portal/v1.3/discovery/swagger/api/Currency",
        "type": "rest"
    }
]

For this exercise, we're using the export tool from this repository to export all APIs into a YAML file. 

In v7-export.py change the following settings so it matches your setup:

`apim_host="https://127.0.0.1:8075"`   
`apim_user="apiadmin"`   
`apim_password="changeme"`

Then run this command:

`python -W ignore v7-export.py`

This should create `export.yaml` along with Swagger and YAML files for each API the tool finds in API Manager, so in our case:

* `swagger_Currency.json`
* `export_Currency.yaml`
* `swagger_ATMLocator.json`
* `export_ATMLocator.yaml`

The content `export.yaml` looks like this:

> apis:   
> .... ATM Locator: /api/portal/v1.3/discovery/swagger/api/ATM Locator   
> .... Currency: /api/portal/v1.3/discovery/swagger/api/Currency

And `export_Currency.yaml` contains some more information about the API we extracted from API Manager (similar for `export_ATMLocator.yaml`):

> apiVersion: v1   
proxy:   
....name: 'Currency'   
....basePath: /curr   
....policy:   
........type: pass-through   
....team:   
........name: 'Default Team'   

## Step 2: Import Endpoints into Amplify Central

As a next step, we'd like to get these API endpoints into Amplify Central. The [Postman Collection](amplify-postman.json) in this repository gives you examples on working with the API for Amplify Central in order to accomplish this.

This is the moment where reviewing the exported data is a good idea & making necessary modifications. The `host` fields in the Swagger documents are of particular importance: **Amplify Central must be able to access the endpoints**. In a default setup of API Manager this is the listener on port 8065 for virtualized APIs. Depending on your setup there are several options for making this available to the outside world (and your Axway architect will be glad to give you advice on this).

Let's look at `swagger_Currency.json` and the relevant key:

> "host" : "api.demo.axway.com:8065"

For my scenario I'm going to use an API Manager on AWS to serve the API, so I'm changing the value accordingly [1]:

> "host" : "52.221.197.254.nip.io"

After this, we can use the Python script in this repository to import the endpoints into Amplify Central. For this you need your [Amplify Central Access Token]([Getting Started Guide](api-getting-started.md)), the script `get_access_token.sh` helps you to retrieve it and store it in a file called `access_token.jwt` which the Python script expects. Whatever your way might be to get the token, make sure `access_token.jwt` looks similar to this before you continue:

> eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTTFpLQmpKbDdmQVpFRDFONzF5S21oZkc3YzJrVm9IREQwdVlQWndEXXXX0IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJjbGllbnRJZCI6IkRPU0FfZTkxMjIxYWYwNTFlNGE1NDkzYjY4MGRjODY4NGRlOTgiLCJlbnZpcm9ubWVudElkIjoiZTkxMjIxYWYwNTFlNGE1NDkzYjY4MGRjODY4NGRlOTgiLCJjbGllbnRIb3N0IjoiMTExLjY1LjcxLjIzNCIsImNsaWVudEFkZHJlc3MiOiIxMTEuNjUuNzEuMjM0Iiwib3JnSWQiOiI5NjY5ODE5OTI4MjgzNzcifQ.AM37pO8RS_bETJtTtIYAGHboRCl1tZ5bWZo5a5fwf28kftzZRAc802A55xvYK27XXaQkP0eAMR7YrCmhv2ekWu4T0NU-eAUX6YoqDaPKZUYQ9geDqi4aPBF6vGAKmjR0p-iO7R0_7_Igbv_9jbXXXXltC243EhqjbN4pSlsGNfVLoyNxH-YvEXduHGLdcjaDfYd5Hw-vuyXvBwtWk5sXXXq_fR2yAAtlsJRMObzrU0mGAnZP8zv6g3Y1laesdhkNMtagWRobxLDCT2JnOJgFszuo1xi5aAowRGRcO-h9c2UZ4ZaaJoqJw

Now you can start the import by issuing this command (make sure that the exported files from the previous step are in the same directory):

`python amplify-import.py`

(Python script to import YAML into Amplify Central - each one imported as a Proxy - work in progress)

## Step 3: Verify Imported Proxies and Publish

(Proxies now appear in Amplify Central - review & publish - work in progress)

## Step 4: Consume APIs

(login as 'user' into Amplify Central - download Swagger - consume API - work in progress)

#### Annotations

[1] nip.io helps you 'convert' IP addresses into FQDNs. Use it with [letsencrypt](https://letsencrypt.org/) to get a free HTTPS certificate!
