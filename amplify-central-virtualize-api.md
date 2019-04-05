# Virtualize, Publish & Consume an API with Amplify Central

## Objectives

In this lab you will:

* import an API Swagger into Amplify Central
* add API Key authentication
* deploy the API endpoint
* publish the API in Amplify Central Catalog
* consume using Postman and cURL

## You need:

* Access to [https://apicentral.axway.com](https://apicentral.axway.com)
* Browser, cURL, Postman

## Step 1: Use Open Banking Endpoint

For this exercise you're going to use an endpoint from the [Yoisho Open Banking project](https://github.com/u1i/yoisho). Let's check out the live endpoints here: [https://backend.yoisho.dob.jp/](https://backend.yoisho.dob.jp/)

![](./resources/ampc00.png)

Have a look at the ATM Locator API which exposes a full CRUD interface:

Swagger: [https://backend.yoisho.dob.jp/banking/v2/swagger](https://backend.yoisho.dob.jp/banking/v2/swagger)

Example Request:

> curl https://backend.yoisho.dob.jp/banking/v2/atm/1
> 
> {"lat": "35.6284713", "lon": "139.736571", "location": "Shinagawa Station"}

## Step 2: Import API into Amplify Central

When you login into Amplify Central, you should see a 'Welcome' dialog that looks like this:

![](./resources/ampc01.png)

Let's click on 'Register an API' and paste the Swagger URL from the ATM endpoint into the upcoming dialog:

![](./resources/ampc02.png)

Amplify Central should pull all the information and display it:

![](./resources/ampc03.png)

Click 'Save' and the endpoint should now have been imported successfully as a 'Proxy'.

![](./resources/ampc04.png)

## Step 3: Add API Key Authentication

In the 'Policy' tab for the API you can now click on 'Client Authentication': 

![](./resources/ampc05.png)

This opens a dialog where you can select 'API Key' - leave the API Key Location at the default setting with is the Header section.

![](./resources/ampc06.png)

## Step 4: Deploy API Proxy to 'Test'

Go back to the API Proxy and navigate on the 'Deployments' tab. Click the 'Deploy' button next to the 'Test Runtime':

![](./resources/ampc07.png)

After a moment you should see an updated view that shows the newly provisioned URL of the endpoint:

![](./resources/ampc08.png)

## Step 5: Create an App so you can use the API

If you go to 'Test Methods' Amplify Central will tell you that you need an app along with an API Key to use the API:

![](./resources/ampc09.png)

So let's do exactly that. Click on 'Apps' in the top navigation on the left side and create an app named 'app1' (or any other name you like):

![](./resources/ampc10.png)
![](./resources/ampc11.png)
![](./resources/ampc12.png)

After that, click on 'API Keys' and generate one by clicking the + button:

![](./resources/ampc13.png)
![](./resources/ampc14.png)
![](./resources/ampc15.png)

Now you can add the 'ATM Locations' API to this app:

![](./resources/ampc16.png)

## Step 6: Test API with API Key

Now head back to 'Test Methods' - you should see that 'Test Runtime' and your API Key is automatically selected.

![](./resources/ampc17.png)

The methods should all work (please note: the live endpoints cannot be used to add, delete or update data but they will give the correct response codes:

![](./resources/ampc18.png)

Amplify Central also gives you the cURL command - try it out! There is also a Swagger download which you can import into Postman.

![](./resources/ampc19.png)

# Step 7: Add API to Amplicy Central Catalog

Click the 'Add to Catalog' button next to the Proxy Runtime:

![](./resources/ampc20.png)

You can change the name and add a thumbnail image for the catalog:

![](./resources/ampc21.png)

When you're done click 'Add to Catalog':

![](./resources/ampc22.png)

Voila! We now have 'ATM Locations' published:

![](./resources/ampc23.png)
![](./resources/ampc24.png)






