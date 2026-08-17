---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-apis-pages-b-cuc-rest-api-faq-html-d2a2e2cf4b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/APIs_Pages/b_CUC-REST-API-FAQ.html
retrieved_at: 2026-08-17T02:23:40.641893+00:00
---

Cisco Unity Connection REST API FAQ

# Cisco Unity Connection REST API FAQ

### Download Options

Updated: December 28, 2018

# Cisco Unity
            	 Connection REST API FAQ

Links to Other API pages: Cisco_Unity_Connection_APIs

## What can cause a
               	 415 error?

415 errors are generally caused by
                  		not specifying the requested content type. Try setting the "Content-Type"
                  		header to "application/xml".

## What can cause a
               	 503 error?

A 503 error will result if there are too many requests queued up on the
                  		server.

The system will process a maximum of 5 web application requests at one
                  		time. The throttle uses a global variable for this, so any request in any
                  		process using the throttle will count towards 1 of the 5.

Any request that comes in while 5 or more others are processing will get
                  		queued and processed as soon as one of the active requests is complete.

We can queue up to 255 requests (or the thread limit in tomcat, which is
                  		150).

As long as requests process at a rate of 1 request per second, the other
                  		requests will remain in the queue. If the requests start processing at a rate
                  		slower than 1 per second, the queue wait mechanism times out and the client
                  		will get a "server busy" (HTTP 503) response.

## How do I GET the
               	 guid (objectid) of a user?

Search by alias to get the user
                  		XML, then extract the ObjectId field. For example, to find the user John Doe
                  		with alias jdoe:

```
GET http://<connection-server>/vmrest/users?query=(alias%20is%20jdoe)
```

Some languages and/or libraries require the URL to be escaped
                              		  first, in which case the spaces need to be converted to %20.

## How do I find out
               	 which networked cluster a user is on?

Search for the user in the global
                     		  user list, and look at the user's location (LocationObjectId):

```
GET http://<connection-server>/vmrest/globalusers?query=(alias%20is%20jdoe)
```

## What is returned
               	 from a PUT?

A successful PUT operation returns an HTTP status code of 204 No
                  		Content.

All HTTP 2xx status codes mean success. Status code 204 means (quoting
                  		from RFC
                     		  2616 ): "The server has fulfilled the request but does not need to return
                  		an entity-body (aka content)."

A PUT operation sends a request to the server to change/update a
                  		resource, so the server does not need to send back anything except a success
                  		code, which is what 204 is appropriate for.

## Is there support
               	 for paging?

Yes. Paging is supported via two query parameters:

- rowsPerPage : Indicates how many objects to return in a single
                        		  query.

- pageNumber : Indicates which page of objects to return.

For example:

```
GET http://<connection-server>/vmrest/users?rowsPerPage=100&pageNumber=1
GET http://<connection-server>/vmrest/users?rowsPerPage=100&pageNumber=2
```

## What causes a 302
               	 error?

An HTTP 302 response is very often
                  		caused by a client trying to connect to a web application by using HTTP
                  		protocol when the web application requires HTTPS. The web server sends back a
                  		302 response to the client in an attempt to redirect it to the secure HTTPS
                  		port.

## What recording
               	 wave file formats are supported with the API?

The Codecs supported for the REST API are the same as the ones supported
                  		for recording over the phone line. The supported list is -

- PCM linear

- G.711 mu-law (default)

- G.711 a-law

- G.729a

- G.726

- GSM 6.10

### This Document Applies to These Products

- Unity Connection

| GET http://<connection-server>/vmrest/users?query=(alias%20is%20jdoe) |
|---|

| Note | Some languages and/or libraries require the URL to be escaped
                              		  first, in which case the spaces need to be converted to %20. |
|---|---|

| GET http://<connection-server>/vmrest/globalusers?query=(alias%20is%20jdoe) |
|---|

| GET http://<connection-server>/vmrest/users?rowsPerPage=100&pageNumber=1
GET http://<connection-server>/vmrest/users?rowsPerPage=100&pageNumber=2 |
|---|