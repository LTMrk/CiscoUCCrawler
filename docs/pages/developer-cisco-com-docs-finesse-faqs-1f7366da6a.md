---
doc_id: developer-cisco-com-docs-finesse-faqs-1f7366da6a
source_url: https://developer.cisco.com/docs/finesse/faqs/
retrieved_at: 2026-09-01T17:34:14.031262+00:00
---

# Finesse FAQ

## General

## Finesse REST API

## Finesse Notification Service

## Finesse JavaScript Library

### Q: What is Finesse?

### Q. What can a developer do with Finesse?

There are three paths for customization:

- Integrate Finesse into your existing application (whether it is thick or thin)

- Create a completely custom agent desktop

- Use the Finesse JavaScript Library APIs to create gadgets to be added to the Finesse out of the box agent desktop. These gadgets do not have to be Finesse or Cisco specific.

- Create gadgets of existing applications to be added to the Finesse out of the box agent desktop without using any Finesse specific APIs.

### Q: What is the difference between the Finesse REST API and the Finesse JavaScript API?

The Finesse JavaScript API is a JavaScript wrapper on top of the Finesse REST APIs, but also includes other classes and methods to seamlessly handle the Finesse Notification Service events and communicate to other gadgets within the Finesse out of the box desktop. These APIs can only be used within a custom Finesse gadget for the Finesse out of the box desktop.

### Q. Where can I find the Finesse documentation?

- The Finesse REST API: Finesse Web Services Developer Guide

- The Finesse JavaScript Library API: Finesse JavaScript Library API Reference

- For Finesse versions 10.6(1) or higher, the Finesse JavaScript Library API documentation can be referenced directly from the Finesse server via URL: http(s)://<FQDN>:<port>/desktop/assets/js/doc/index.html

Documentation for older versions of Finesse can be found in the Previous Documentation section under Docs -> Downloads -> Previous Documentation (PDFs).

### Q. How do you use the Finesse Web Services Developer Guide?

- Cisco Finesse Desktop APIs

- Cisco Finesse Configuration APIs

- Cisco Finesse Serviceability APIs

Each section is then categorized to the individual objects, which are further broken down to each REST API.

Each REST API is documented with a table that provides the necessary information needed to make the REST API request. The following image defines each row of the table:

### Q. I need to build an application that works for both UCCE and UCCX, can I build one application for both deployments?

### Q. Does Finesse support High-Availability installations?

### Q. Does Finesse support 2-Way SSL Web Service calls?

### Q. Does Finesse support Cross-Origin Resource Sharing (CORS)?

In Finesse 11.5(1) & 11.6(1), in order to enable CORS support, Finesse expects the third-party web server to send a specific header that contains the Origin Host name. The Host name value in Origin is used by Finesse to populate the Response Header named Access-Control-Allow-Origin.

Starting Finesse 12.0(1), CORS support needs to be enabled by an administrator via the CLI. Please see the CORS Support for Finesse REST APIs section of the Finesse Web Services Developer Guide for more details.

### Q. I created a workflow that makes a non-Finesse HTTP request. Where do I enter in the authentication credentials for the HTTP request?

### Q. Can the columns of the desktop layout be different widths?

### Q. What are the supported browsers for Finesse version XX.X(X)?

### Q. How do I add additional filters to the Live Data Gadget?

### Q. How do I add a Historical Report to the Finesse desktop?

### Q. None of the above answers my question. Help!

If you still have an issue, ask your question in the Finesse forum .

### Q. I want to use the Finesse REST APIs, but where do I start?

### Q. Does Finesse have an API to _________?

### Q. What port should I use for my REST APIs?

For a UCCX deployment:

- Finesse 12.5 or above: HTTP is not supported

- Finesse 12.0 and below: 8082

- HTTPS port is 8445

For a UCCE deployment:

- Finesse 12.5 or above: HTTP is not supported

- Finesse 12.0 and below: 80 or 8082 (You do not need to include the port number in the URI for HTTP requests)

- Finesse 11.0 or above: 8445

- Finesse 10.5 or below: 8443

### Q. What type of authentication do the REST APIs use?

SSO for REST API is supported starting Finesse 12.0(1). For all SSO users, Finesse APIs use Bearer Token authentication, where the token is the access token provided by the Cisco Identity Service (IdS). For more information about SSO with Finesse REST APIs, take a look at the Single Sign-On section of the Finesse Web Services Developer Guide .

### Q. How do I authenticate Finesse REST APIs with SSO?

SSO support is also available for the Finesse out of the box desktop and custom gadgets.

### Q. How do I get the access token from the Cisco Identity Service?

- Follow server issued redirects

- Store and forward cookies

- Honor the various cookie attributes

- Execute JavaScript in HTML responses

For instructions on the SSO token retrieval procedure, take a look at the Client Integration section of the Finesse Web Services Developer Guide .

Notes In Finesse 11.6(1) and 12.0(1):

- HYBRID mode is not supported (must be SSO only).

- The Single Sign-On—Get User Authentication Mode API is not available.

- The username must be provided in a cookie with a key of cc_username for the Single Sign-On—Fetch Access Token API.

### Q. Which role (agent, supervisor, administrator) can use _________ API?

### Q. Can I use the credentials/token for one user to make REST API requests on behalf of multi users?

### Q. What format is the Finesse REST API request/response?

### Q. Some values in the Finesse responses are a pass through from UCCE or UCCX. Where can I find more information about these values?

- For UCCE: CTI Server Message Reference Guide

- For UCCX: UCCX CTI Protocol Guide

### Q. Where can I find the supported agent state transitions?

### Q. What languages can I use to develop an application that uses Finesse REST APIs?

### Q: What is the Finesse Notification Service?

For a better understanding on how the Finesse Notification service works, it is best to manually make a Finesse REST API request via a HTTP REST Client tool and view the resulting event via a XMPP client application. Please see the Environment and Tools section in the Finesse Web Services Developer Guide for more details.

For details about the Cisco Finesse Notification Service, please see the Cisco Finesse Notification Service section in the Finesse Overview page.

For details about the Finesse notifications, please see the Cisco Finesse Notifications section in the Finesse Web Services Developer Guide .

For details about how to connect to the Cisco Finesse Notification Service, please see the Managing Notifications in Third-Party Applications section in the Finesse Web Services Developer Guide .

### Q. What port should I use to connect to the Finesse Notification Service?

Starting Cisco Finesse 12.5(1), the non-secure 5222 port is disabled by default. Set the utils finesse set_property webservices enableInsecureOpenfirePort to true to enable this port.

For more information about the Finesse Notification Service over TCP, see the Connect to XMPP over TCP section of the Finesse Web Services Developer Guide .

To connect to the Finesse Notification Service over HTTP (WebSocket), the port will depend on the Finesse version.

- For Finesse 12.0(1) & 12.5(1): 7443

- For Finesse 12.6(1) and above: 8445

Starting Cisco Finesse 12.6(1), support for notifications over BOSH (long polling) and the usage of port 7443 are deprecated. Applications should switch to WebSocket-based notifications and use port 8445 or notifications over direct XMPP (over TCP).

For more information about the Finesse Notification over HTTP, see the Connect to XMPP over HTTP (BOSH/WebSocket) using Finesse EventTunnel section of the Finesse Web Services Developer Guide .

### Q. How do I connect to the Finesse Notification Service with SSO?

### Q. My application needs to receive Finesse notifications. Do I need to subscribe to the nodes to get notifications?

- User - /finesse/api/User/{id}

- Dialogs - /finesse/api/User/{id}/Dialogs

- Media - /finesse/api/User/{id}/Media/{mrd-id}

- SystemInfo - /finesse/api/SystemInfo

The user must explicitly subscribe to the other nodes. Please see the Cisco Finesse Notifications section of the Finesse Web Services Developer Guide for more info.

### Q. Can the same user log into the Finesse Agent Desktop and also establish a connection to the Finesse Notification Service to receive Finesse notifications?

### Q: Which XMPP/BOSH/WebSocket library should I use to communicate to the Finesse Notification Service?

Based on feedback from the community, DevNet has seen a lot of developers use the Smack and the Strophe.js libraries to communicate with the Finesse Notification Service. Please note that Cisco does not provide support for any issues specific to the XMPP library.

### Q. I want to build a gadget using the Finesse JavaScript Library, but where do I start?

### Q. Where do I get the Finesse JavaScript Library file (finesse.js) for Finesse 10.6 and above?

The jQuery library is also hosted on the Finesse server under: http(s)://<FQDN>:<port>/desktop/assets/js/jquery.min.js

Third-party gadgets that are hosted on the Finesse server via the 3rdpartygadgets account can reference the JavaScript library accordingly:

javascript

```
< ! -- jQuery -- > < script type = "text/javascript" src = "/desktop/assets/js/jquery.min.js" > < / script > < ! -- Finesse Library -- > < script type = "text/javascript" src = "/desktop/assets/js/finesse.min.js" > < / script >
```

Third-party gadgets that are hosted on a separate web server can reference the JavaScript library accordingly:

javascript

```
< UserPref name = "scheme" display_name = "scheme" default_value = "" / > < UserPref name = "host" display_name = "host" default_value = "" / > < UserPref name = "hostPort" display_name = "hostPort" default_value = "" / > < ! -- jQuery -- > < script type = "text/javascript" src = "__UP_scheme__://__UP_host__:__UP_hostPort__/desktop/assets/js/jquery.min.js" > < / script > < ! -- Finesse Library -- > < script type = "text/javascript" src = "__UP_scheme__://__UP_host__:__UP_hostPort__/desktop/assets/js/finesse.min.js" > < / script >
```

### Q. Where can I find sample gadgets?

### Q. Where do I upload my third-party gadget that I built?

- Use the Finesse server as the webserver:

- Enable the 3rdpartygadget account .

- Upload your third-party gadget to the Finesse server.

- Use your own web server. Ensure that the Finesse server has access to your web server.

### Q. What are these handlers/callbacks in the sample gadgets?

For more information about handlers, please see the Request Handlers section of the Finesse JavaScript Library API Reference .

### Q. How do I create/update gadgets to work with SSO?

### Q. None of the sample gadgets are working. Help!

### Q. After I upgraded Finesse, my gadget stopped working. What happened?

### Q: I made code changes to my gadget, why don't I see the changes on the desktop?

### Q: I want to modify an out of the box gadget, where do can I get the code?

All Finesse gadgets (Team Performance, Call Control and Queue Stats) are powered by public Finesse REST APIs, so you would need to build your own gadget.

All product specific out of the box gadgets (Live Data, Chat and Email, MediaSense, etc.) use internal REST APIs, so it is not possible to build a gadget with similar capabilities.

### Q. How do I get the loading indicator (the spinning circle) for my gadget like the Finesse gadgets?

### Q. How do I change the height of the team performance gadget?

Starting Finesse 11.5(1), the height of the team performance gadget is configurable by modifying the desktop layout XML in the Finesse Administration Console. Add the maxRows parameter to the desktop layout: <gadget>/desktop/gadgets/TeamPerformance.jsp?maxRows=20</gadget> , where the number of rows determines the height of the gadget. If you do not set or if you set the height to less than 10 rows, then default value of 10 is applied.

### Q. How do I change the height of the Embedded WebApp Sample Gadget ?

javascript

```
var html = '<iframe src="' + _urlToLoad + '" id="displayFrame"></iframe>' ;
```

to

javascript

```
var html = '<iframe src="' + _urlToLoad + '" id="displayFrame" width="100%" height="600"></iframe>' ;
```

### Q. How do I call a third-party REST API from a Finesse gadget?

Alternatively, the third-party server can be configured to allow CORS requests from the Finesse domain by configuring a CA signed certificate or a pre-imported X.509 certificate. This will allow the gadget to directly call a third-party REST API. This route will provide better performance.