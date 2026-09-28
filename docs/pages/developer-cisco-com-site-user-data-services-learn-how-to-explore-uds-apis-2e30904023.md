---
doc_id: developer-cisco-com-site-user-data-services-learn-how-to-explore-uds-apis-2e30904023
source_url: https://developer.cisco.com/site/user-data-services/learn/how-to/explore-uds-apis/
retrieved_at: 2026-09-01T17:34:58.109873+00:00
---

# Explore the UDS APIs using a browser plugin

Browser plugins such as the REST Client add-on for Firefox, Poster  and the Chrome Advanced REST client can be useful tools for experimenting with the UDS REST APIs.  This article walks through how to get a user's settings and preferences.

## To complete this exercise, you will need:

1. The URL for a CUCM system that you can access. You will need the following credentials for this system:

- a valid username and password for an end user

- This example will use the REST Client add-on for Firefox .

- Another good REST client is the Chrome Advanced REST client

- Poster is another option for Firefox

## Testing the API with the REST Client

This example shows you how to test the UDS "Hello World" use case using a browser plugin. This is an outline of the steps we will follow:

1. Enter the request URL and method 2. Add the HTTP headers 3. Send the request and view the response

1. Enter the request URL and method

Launch the Firefox browser. Click on the RESTClient icon or choose Tools > RESTClient to start the RESTClient add-on. Enter the URL for the UDS servers resource into the URL field. For example, enter https://{host}:8443/cucm-uds/user/{userId} . See Figure 1.

Figure 1.Entering the UDS servers URL into the RESTClient.

2. Add the HTTP headers

UDS conducts transactions using XML-formatted requests and responses. The HTTP headers need to be configured to indicate that this format is in use. Choose Headers > Custom Headers . A dialog box appears. Enter Content-Type in the Name field and application/xml in the Value field for the dialog box. Click OK . A Content-Type entry should appear in the Headers section of the RESTClient tool.

Choose Headers > Custom Headers again. A dialog box appears. Enter Accept in the Name field and application/xml in the Value field of the dialog box. Click OK . An Accept entry should appear in the Headers section of the RESTClient tool. Figure 2 shows the RESTClient with both of these headers added.

Figure 2. The RESTClient after the HTTP headers are added.

This resources requires a username and password. Add the credentials into the Authentication section of the REST client.

- Click on the Authentication link at the top

- Select Basic

- Enter the username and password

- Click Okay

3. Send the request and view the response.

Ensure that the GET is selected for the Method and click Send . A Response section pane appears and indicates that a HTTP 200 OK response was received. Click on the Response Body (Preview) tab for this pane to view the XML-formatted response that contains the phone service information. See Figure 3.

Figure 3. Viewing the XML response to the GET method for the service.

You're Done!