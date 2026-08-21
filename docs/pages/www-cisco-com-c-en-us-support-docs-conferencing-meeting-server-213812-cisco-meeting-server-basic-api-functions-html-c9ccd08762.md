---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-213812-cisco-meeting-server-basic-api-functions-html-c9ccd08762
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/213812-cisco-meeting-server-basic-api-functions.html
retrieved_at: 2026-08-21T13:12:15.783402+00:00
---

Cisco Meeting Server Basic API Functions

# Cisco Meeting Server Basic API Functions

### Download Options

Updated: January 19, 2021

Document ID: 213812

Contents

## Contents

## Introduction

This document describes the four basic API (Application Program Interface) functions GET, POST, PUT, DELETE used on CMS (Cisco Meeting Server). As of CMS 2.9, the web admin GUI has an API menu available under the Configuration menu. This document reviews that new menu and also describes two different API tools: Poster and Postman and how to use them for CMS configuration.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document can be used with CMS 2.9 and later or with different API clients like Postman or Poster. These third-party tools are described in the API clients section of the document.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

The API for the CMS is an extremely flexible way to configure many of its features. There are far too many API features to memorize or cover here, so be sure to reference the current API Reference documentation. As of the time of this writing, the current API Reference guides are available here .

### API Request and Response

API communication is a request-response relationship between clients and servers. The client makes a request of the server. After handling the request (completing an action, or refusing to do so) a response is returned.

The four requests described in this article are:

- GET - Retrieves existing information

- POST - Creates new information

- PUT - Modifies existing information

- DELETE - Deletes existing information.

These are the basic API requests used to configure CMS.

The most common response is a 200 OK. Other responses are 4xx and 5xx, which are error responses.

## Configure

### CMS 2.9 and Later

CMS 2.9 introduced a new API menu that makes it much easier for administrators to modify settings and fine tune settings in CMS.  When using the menu, all available parameters are displayed, which makes it quick and easy to change settings and enable new features.

#### Configure an API Object

Once in the API menu, you can filter the API objects to what you are looking to edit/create and then click the black arrow next to the object to make those changes. This example shows how to look up callLegProfiles and create a new callLegProfile.

When you click Create New , you are presented with this screen which displays all available parameters for CallLegProfiles. When you hover over a particular parameter, you will get a popup that shows the purpose of each option.

#### Modify an API Object That is Already Created

When you change settings in an object, you will see the Modify button at the bottom. This is the same as a PUT from the third-party tools.

#### Delete an API Object from the API Menu

In order to delete an object, on the main Object List page, you can enable the ability to delete items. Click Allow delete in order to enable the option to delete, as shown in this example:

### API Requests Explained (using 3rd party tools)

The four basic requests are explained through a configuration example.

#### HTTP POST

Step 1. Use POST to create an object.

In this example, a CMS Space is created using this request. In order to create the Space via API, consult the API documentation. For this example I used the CMS 2.4 API guide, but you should use the latest API guides, found here

Section 6.2 has information on how to create and modify a cospace.

The first sentence says that to create a Space, you need to send a post to /coSpaces. Then, it says the ID of the Space will be in the Location header of the 200 OK. Great, you now know how to create a Space. You just send a POST to https://<WebAdminIP>/api/v1/coSpaces .

Specify the parameters for the POST .

In section 6.2 of the documentation you see a table that lists all of the parameters you can use.

For example: Create a Space with the name APITest and a URI user part of APITestURI

The content type is application/x-www-form-urlencoded and the content is name=APITest&uri=APITestURI

When you add this parameters the request is complete, as shown in the image.

```
POST https://<WebAdminIP>/api/v1/coSpaces HTTP/1.1
Host: <WebAdminIP>
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
Authorization: Basic YWRtaW46QzFzYzBDMXNjMA==
Connection: keep-alive

name=APITest&uri=APITestURI
```

The image shows a response to the previous request.

```
HTTP/1.1 200 OK
Server: Apache
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000; includeSubDomains
Location: /api/v1/coSpaces/ 70ca0ed7-4e50-428c-b9ab-4e68faeb86ae Vary: Accept-Encoding
Content-Encoding: gzip
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Transfer-Encoding: chunked
```

Notice the Location header in the response.

```
Location: /api/v1/coSpaces/ 70ca0ed7-4e50-428c-b9ab-4e68faeb86ae
```

70ca0ed7-4e50-428c-b9ab-4e68faeb86ae is the ID of the new created Space. The ID is useful  when you need to make future API requests that target the same Space.

The Space can be seen in the WebAdmin of CMS. Navigate to Configuration > Spaces.

The image summarizes the request POST .

#### HTTP GET

Step 2. After the Space has been created, pull the configuration for it.

Use the HTTP GET method for this purpose.

Use the ID for the Space created from the Location header. The URL is https://<WebAdminIP>/api/v1/coSpaces/70ca0ed7-4e50-428c-b9ab-4e68faeb86ae.  Perform a GET on this page.

Example GET request:

```
GET https://<WebAdminIP>/api/v1/coSpaces/70ca0ed7-4e50-428c-b9ab-4e68faeb86ae HTTP/1.1
Host: <WebAdminIP>
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: session=logout
Authorization: Basic YWRtaW46QzFzYzBDMXNjMA==
Connection: keep-alive
```

Response for the GET request:

```
HTTP/1.1 200 OK
Server: Apache
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Type: text/xml
Vary: Accept-Encoding
Content-Length: 159
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive

<?xml version="1.0"?><coSpace id="70ca0ed7-4e50-428c-b9ab-4e68faeb86ae"><name>APITest</name><autoGenerated>false</autoGenerated><uri>apitesturi</uri></coSpace>
```

Note : The response is an XML encoded configuration of the Space.

The image summarizes the request GET .

#### HTTP PUT

Step 3. Make a change to the Space (if needed).

This example shows how to modify the space created. Imagine a secondary User portion needs to be added to the Space.

Refer to the API document. It tells the parameter needed to use that is: secondaryUri .

Add a URI of asdf. Write a request that looks  similar to the request created for POST.

Example PUT request:

```
PUT https://172.18.105.244/api/v1/coSpaces/70ca0ed7-4e50-428c-b9ab-4e68faeb86ae HTTP/1.1
Host: 172.18.105.244
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 17
Cookie: session=b810c447daaeab6cdc6e019c
Authorization: Basic YWRtaW46QzFzYzBDMXNjMA==
Connection: keep-alive

secondaryUri=asdf
```

Response for the PUT request:

```
HTTP/1.1 200 OK
Date: Tue, 12 Apr 2016 19:11:02 GMT
Server: Apache
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000; includeSubDomains
Vary: Accept-Encoding
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Length: 0
```

The changes can be seen in the WebAdmin of CMS. Navigate to Configuration > Spaces.

and via a GET :

```
<?xml version="1.0"?><coSpace id="70ca0ed7-4e50-428c-b9ab-4e68faeb86ae"><name>APITest</name><autoGenerated>false</autoGenerated><uri>apitesturi</uri><secondaryUri>asdf</secondaryUri></coSpace>
```

The image summarizes the request PUT .

#### HTTP DELETE

Step 4. Delete the Space (if needed).

The DELETE method is similar to the GET method.

Example DELETE request:

```
DELETE https://172.18.105.244/api/v1/coSpaces/70ca0ed7-4e50-428c-b9ab-4e68faeb86ae HTTP/1.1
Host: 172.18.105.244
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: session=4d13c7ebe739b662dc6e019c
Authorization: Basic YWRtaW46QzFzYzBDMXNjMA==
Connection: keep-alive
```

Response for the DELETErequest:

```
HTTP/1.1 200 OK
Date: Tue, 12 Apr 2016 19:16:37 GMT
Server: Apache
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000; includeSubDomains
Vary: Accept-Encoding
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Length: 0
```

The changes can be seen in the WebAdmin of CMS. Navigate to Configuration > Spaces.

and via a GET :

```
<?xml version="1.0"?><failureDetails><coSpaceDoesNotExist /></failureDetails>
```

The image summarizes the request DELETE .

## API Clients

#### POSTER

The top box in Poster is where you enter the URL for the requests.

The User Auth fields are where you enter the username and password in that order. Then, if you are doing a GET or a DELETE , choose the respective buttons. For example: click GET and a popup appears with your response. For DELETE , ensure DELETE is selected and click the green button.

For POST and PUT , content needs to be added. Select the Parameters tab and add the names and values for your parameters. Then, go back to the Content to send button and choose Body from Parameters .

Send your POST and/or PUT.

#### POSTMAN

In Postman, in the top-left, choose the Method you would like to use from the drop-down box and enter the request URL.

For Authorization, choose Basic-Auth and enter your username and password. Then, choose Update Request . In the Headers tab you see an Authorization Header.

If your request is a POST/PUT, navigate to the Body tab, choose x-www-form-urlencoded and enter your parameters and values. When you are finished, choose Send .

## Verify

The verification method is explained in each request.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Vernon Depee

Cisco TAC Engineer

Darren McKinnon

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server