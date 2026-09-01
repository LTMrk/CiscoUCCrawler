---
doc_id: developer-cisco-com-site-user-data-services-sso-8bc5022705
source_url: https://developer.cisco.com/site/user-data-services/sso/
retrieved_at: 2026-09-01T17:35:02.635243+00:00
---

# Using Cisco Collaboration Single
                Sign-On with User Data Services

The Unified Communications Manager (Unified CM) User Data Services (UDS) API provides a client-side
                interface allowing end-users to read and update Unified CM information and settings specific to their
                devices and account. For more information on UDS, see: https://developer.cisco.com/index/overview

Starting with version 10.5, several Cisco Unified Communications (Cisco UC) product APIs, including UDS,
                support authentication via the Cisco UC Single Sign-On (SSO) mechanism. This has several advantages
                including allowing users to sign in to Unified CM once and reuse their session across multiple Unified
                CM web applications and API interfaces.

This document provides a browser-based example showing how to use a SSO token to access a UDS API. Note
                that a prerequisite to using a SSO API, like UDS, is that the application must first interact with Cisco
                UC SSO to authenticate the user and obtain a SSO token. For further background on Cisco UC SSO and an
                example showing how to obtain a SSO token via a browser application, see the Cisco Unified Communications Single Sign-On Tutorial .

Once you have a SSO access token, you are ready to use it with UDS.

# Using a SSO Access Token with UDS

Not all UDS APIs require user authentication, but you will need to use either username/password or SSO
                token with the APIs that do, including:

- Credentials

- Device(s)

- Extenstion(s)

- RemoteDestination(s)

- SpeedDial(s)

- SubscribedService(s)

- User

- UserPolicy

## Standard Basic Authorization

```
//Basic Authorization Example GET /cucm-uds/user/user1 HTTP / 1.1 Host : ds-ucm105.cisco.com User-Agent : Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0 Accept : text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language : en-US,en;q=0.5 Accept-Encoding : gzip, deflate DNT : 1 Authorization : Basic dXNlcjE6Y2lzY28hMTIz Referer : https://app.example.com/ssouds.html Origin : https://app.example.com Connection : keep-alive
```

By default, UDS authenticates users via the HTTP Basic Authorization mechanism. This requires that the
                HTTP request to UDS include an Authorization header, with value of Basic plus a base64-encoded username:password, for example: Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==

## SSO Bearer Authorization

```
//Bearer Authorization Example GET /cucm-uds/user/user1 HTTP / 1.1 Host : ds-ucm105.cisco.com User-Agent : Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0 Accept : text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language : en-US,en;q=0.5 Accept-Encoding : gzip, deflate DNT : 1 Authorization : Bearer Mjo1NTU5ZmFkYS02MjYwLTQ0YTktOTRhNS1iY2RmNzcwZWQzZDE Referer : https://app.example.com/ssouds.html Origin : https://app.example.com Connection : keep-alive
```

In order to use SSO, the same Authorization header is used. But, the Authorization type becomes Bearer plus the SSO token (not base64-encoded), for example: Authorization: Bearer Mjo1NTU5ZmFkYS02MjYwLTQ0YTktOTRhNS1iY2RmNzcwZWQzZDE

# Cross-Origin Resource Sharing

For security reasons, web browsers by default prevent Javascript served by one origin (web site) from
                accessing data served by another origin, where an origin is a combination of scheme (an example of a
                scheme is HTTPS), hostname, and port.

For example, Javascript on a page served from https://app.example.com cannot access data retrieved via XMLHttpRequest from https://ucmanager.example.com (for instance, to make a UDS request.)

To allow these types of requests securely, the Cross-Origin Resource Sharing (CORS) standard was
                developed: http://www.w3.org/TR/cors . CORS is supported in modern browsers.

CORS involves the use of special HTTP request headers and ‘pre-flight’ OPTIONS requests,
                and is generally handled transparently by browsers. However, it is necessary to configure the web server
                (in this case Cisco Unified CM) to allow Cross-Origin requests, on an origin-by-origin basis.

Unified CM supports configuration of CORS applications via the System/Cross-Origin Resource
                    Sharing (CORS) menu:

For each browser-based application web site using a Unified CM CORS-supported API, an entry in the CORS
                configuration area will need to be created. Include the protocol scheme (such as HTTPS), domain, and
                port (if not the default port :80 or :443), for example https://app.example.com .

# Preparing Your Environment

Successfully accessing UC SSO APIs from an application assumes that some general system services and
                configurations are in place:

- HTTPS - All connections involved with SSO and UDS are secured with HTTPS.
                    Applications and browsers must be configured with the correct certificates in order to connect
                    securely. For lab testing, you may be able to temporarily accept certificates in the browser.

- DNS - HTTPS certificates and the URLs involved in the SSO API sequence typically
                    use hostnames (vs. IP addresses). The UC and application hosts should be configured in DNS. For lab
                    testing, you may be able to use your PC’s ‘hosts’ file to map hostnames to IPs
                    locally.

- UC SSO - SSO should be fully configured and working with Unified CM. For example,
                    end-users can access UC web apps like the ‘Self Care Portal’ using their SSO
                    credentials.

# Example Browser-based UDS REST Request

The example HTML/javascript covered in this document gathers a Unified CM host name, SSO token
                (previously obtained, as above), and UDS user name from browser input fields, and makes a UDS API GET request to the User resource,
                gathering some information about the user. The UDS XML response is shown in the browser upon success.

## Get Ready…

Note: In order for this sample to work, the following setup steps should be completed:

Confirm that SSO is available and running in your environment. Take note of the Unified CM host
                        name.

Make sure the Unified CM host and your web server host can be resolved via DNS (manual entries in
                        your PC’s ‘hosts’ file can help during testing).

Obtain a valid set of SSO login credentials that will work with your SSO Identity Provider (IdP).
                        With this set of credentials, obtain a UC SSO access token, for example using the sample
                        application found in the Common SSO Tutorial .

Confirm that you have a web server capable of serving HTTPS requests for files you supply.

Copy ssouds.html to the correct directory for your web server’s HTTPS
                        site.

Verify that CORS has been enabled on Unified CM for your web server’s origin/domain.

Verify that SSL certificates for Unified CM and your web server have been imported/enabled in
                        your web browser.

# Sample Code Walk-Through

## Creating the XMLHttpRequest Object

```
var xmlhttp = new XMLHttpRequest (); //Create XML request object xmlhttp . open ( 'GET' , "https://" + ucHost + "/cucm-uds/user/" + udsUser ); //UDS REST API to retrieve user info
```

After retrieving the Unified CM host, UDS user name, and SSO token from the HTML input fields, the
                Javascript code creates the XMLHttpRequest object used to make the UDS request.

## Adding the Accept Header

```
xmlhttp . setRequestHeader ( 'Accept' , 'application/xml' );
```

The next step adds the Accept: application/xml header to the HTTP
                request, to indicate to UDS that the application expects an XML response.

## Adding the Authorization: Bearer Header

```
xmlhttp . setRequestHeader ( "Authorization" , "Bearer " + ssoToken ); //Add 'Authorization' header with 'Bearer' and token
```

Next, the code adds the Authorization header, including the Bearer type and the SSO token to authenticate the UDS user.

## Handling the XMLHttpRequest Completion Event

```
xmlhttp . onreadystatechange = function () { //Handle completion event of the XML request if ( xmlhttp . readyState == 4 ) { //State is complete if ( xmlhttp . status == 200 ) { //Status is 200 OK var xml = new XMLSerializer (). serializeToString ( xmlhttp . responseXML ); //Extract the XML string from the response document . getElementsByName ( "response" )[ 0 ]. value = xml ; //Display the XML in the text area } } }
```

This block of code sets an event handler for the XMLHttpRequest objects’s completion event. If the
                event is called with state=4 (complete) and status=200 (200 OK), then the code extracts the XML response and displays
                it in the web page text area.

## Launching the XMLHttpRequest

```
xmlhttp . send (); //Launch the XML request
```

Once the XMLHttpRequest has been prepared and the event handler is in place, the actual request is
                launched as the final step.

# Sample REST Response

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> <user uri= "https://ds-ucm105.cisco.com/cucm-uds/user/user1" version= "10.5.1" > <id> 34d8f2ed-6075-7e51-9753-2b1c6875a13f </id> <userName> user1 </userName> <firstName> user1 </firstName> <lastName> ln1 </lastName> <middleName/> <nickName/> <phoneNumber/> <homeNumber/> <mobileNumber/> <mobileConnect> false </mobileConnect> <remoteDestinationLimit> 4 </remoteDestinationLimit> <userLocale uri= "https://ds-ucm105.cisco.com/cucm-uds/options/installedLocales" value= "" appliesToAllDevices= "true" > English, United States </userLocale> <email/> <directoryUri/> <msUri/> <department/> <manager/> <title/> <pager/> <selfServiceId/> <accountType useLdapAuth= "false" > ldap </accountType> <homeCluster enableImAndPresence= "false" enableCalendarPresence= "false" > false </homeCluster> <imAndPresence/> <enableDoNotDisturb appliesToAllDevices= "true" > false </enableDoNotDisturb> <serviceProfile> <uri> http://DS-UCM105:6970/SPDefault.cnf.xml </uri> </serviceProfile> <devices uri= "https://ds-ucm105.cisco.com/cucm-uds/user/user1/devices" /> <credentials uri= "https://ds-ucm105.cisco.com/cucm-uds/user/user1/credentials" /> <extensions uri= "https://ds-ucm105.cisco.com/cucm-uds/user/user1/extensions" /> <subscribedServices uri= "https://ds-ucm105.cisco.com/cucm-uds/user/user1/subscribedServices" /> <speedDials uri= "https://ds-ucm105.cisco.com/cucm-uds/user/user1/speedDials" /> </user>
```

If everything went well, UDS should respond to the request with a 200 OK status and include some XML info about the UDS user. For full details about the contents of the UDS User resource response, see the UDS API Reference