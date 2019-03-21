# Export, Publish & Consume APIM 7.x APIs with Amplify Central

## Scenario

You're running a setup of Axway API Manager v7 to manage, protect & consume on premise APIs. [Amplify Central](https://apicentral.axway.com) gives you a control plane on the cloud – manage, consume & analyze. This guide shows you how to make existing API endpoints (managed by an API v7 environment) available in Amplify Central and gives you the necessary tools & steps to accomplish this.

![](./resources/v7apic1.png)

## You need

* An existing setup of API Manager / Gateway v7
* Some virtualized endpoints in API Manager. 
* Access to [Amplify Central](https://apicentral.axway.com)
* Python 2.7 runtime environment on your local machine to run the helper scripts
* Bearer Token for API Access - see [Getting Started Guide](api-getting-started.md)

## Starting Point: API Manager v7

Let's look at our initial state, we have two API endpoints (from the [Yoisho Open Banking Project](https://github.com/u1i/yoisho)) virtualized in API Manager:

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

You could choose to change the password for 'apiadmin' temporarily for this exercise.

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
