---
doc_id: developer-cisco-com-site-unity-connection-sso-96304fe46d
source_url: https://developer.cisco.com/site/unity-connection/sso/
retrieved_at: 2026-08-25T21:11:38.292681+00:00
---

# Using
                Cisco Collaboration Single Sign-On with Cisco Unity Connection Messaging Interface

The ‘Cisco Unity Connection Messaging Interface’ (CUMI) provides a client-side interface
                allowing end-users to read and update Unity Connection messaging information and settings specific to
                their mailbox and account. For more information on CUMI, please see the CUMI DevCenter

Starting with version 10.5, several Cisco UC APIs, including CUMI, support authentication via the Cisco
                UC Single Sign-On mechanism. This has several advantages, allowing users to sign in to CUC once and
                re-use their session across multiple UC web applications and API interfaces.

This document provides a browser-based example showing how to use a SSO token to access a CUMI API. Note
                that a pre-requisite to using a SSO API like CUMI, is that the application must first interact with
                Cisco UC SSO to authenticate the user and obtain a SSO token. For further background on Cisco UC SSO and
                an example showing how to obtain a SSO token via browser app, please see the Cisco
                    Unified Communications Single Sign-On Tutorial .

Once you have an SSO access token, you are ready to use it with CUMI.

### Standard Basic Authorization

```
//Basic Auth Example GET https://ds-cuc105.cisco.com/vmrest/mailbox/folders/inbox/messages HTTP / 1.1 Host : ds-cuc105.cisco.com User-Agent : Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/32.0 Accept : text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language : en-US,en;q=0.5 Accept-Encoding : gzip, deflate Authorization : Basic dXNlcjE6Y2lzY28hMTIz Referer : https://app.example.com/ssocumi.html Origin : https://app.example.com Connection : keep-alive
```

By default, CUMI authenticates users via the HTTP ‘Basic Authorization’ mechanism. This
                requires that the HTTP request to CUMI include an ‘Authorization’ header, with value of
                ‘Basic’ plus a base64-encoded username:password, e.g: Authorization:
                    Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==

### SSO Bearer Authorization

```
//Bearer Auth Example GET https://ds-cuc105.cisco.com/vmrest/mailbox/folders/inbox/messages HTTP / 1.1 Host : ds-cuc105.cisco.com User-Agent : Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/32.0 Accept : text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language : en-US,en;q=0.5 Accept-Encoding : gzip, deflate Authorization : Bearer MjpkMTI2NDgyOS1mMDg1LTRhY2UtOGM3Yy1hMmY0ZjQ0ODUxNGQ Referer : https://app.example.com/ssocumi.html Origin : https://app.example.com Connection : keep-alive
```

In order to use SSO, the same ‘Authorization’ header is used, but the auth type becomes
                ‘Bearer’ plus the SSO token (NOT base64-encoded), e.g.: Authorization:
                    Bearer Mjo1NTU5ZmFkYS02MjYwLTQ0YTktOTRhNS1iY2RmNzcwZWQzZDE

## Cross-Origin Resource Sharing

For security reasons, web browsers by default prevent Javascript served by one 'origin' from
                accessing data served by another origin (an origin is a combination of scheme - e.g. 'HTTPS' -
                hostname, and port.) For example Javascript on a page served from https://app.example.com cannot access data retrieved via XMLHttpRequest from https://unityconnection.example.com (e.g. to make a CUMI request.)

To allow these types of requests securely, the Cross-Origin Resource Sharing standard was developed
                (supported in all modern browsers:) http://www.w3.org/TR/cors

CORS involves the use of special HTTP request headers and ‘pre-flight’ OPTIONS requests,
                and is generally handled transparently by browsers. However, it is necessary to configure the web server
                (in this case Cisco UCM) to allow Cross-Origin requests, on an origin-by-origin basis.

CUC supports configuration of CORS applications via the Cross-Origin Resource Sharing (CORS) menu:

For each browser-based application that will be using CUC SSO APIs, configure a CORS entry: include the
                protocol scheme (i.e. ‘https://’) domain and port (if not default :80 or :443), e.g. https://app.example.com

## Preparing Your Environment

Successfully accessing UC SSO APIs from an application assumes that some general system services and
                configurations are in place:

- HTTPS - All connections involved with SSO and CUMI are secured with HTTPS.
                    Applications and browsers must be configured with the correct certificates in order to connect
                    securely. (For lab testing, you may be able to temporarily accept certificates in the browser).

- DNS - HTTPS certificates and the URLs involved in the SSO API sequence typically
                    use hostnames (vs. IP addresses). The UC and application hosts should be configured in DNS. (For
                    lab/testing, you may be able to use your PC’s ‘hosts’ file to map hostnames to
                    IPs locally)

- UC SSO - SSO should be fully configured and working with CUC, e.g. end-users can
                    access CUC web apps like ‘Inbox’ using their SSO credentials.

## Example Browser-based CUMI REST Request

The example HTML/javascript covered in this document gathers a CUC host name and SSO token (previously
                obtained, as above) from browser input fields, and makes a CUMI API ‘GET’ request to the Inbox resource, gathering some information about the users voicemail
                inbox. The CUMI XML response is shown in the browser upon success.

### Get Ready...

Note: in order for this sample to work, the following setup steps should be completed:

1) Confirm that SSO is available and running in your environment. Take note of the CUC host name.

2) Make sure the CUC host and your web server host can be resolved via DNS (manual entries in your
                PC’s
                ‘hosts’ file can help during testing).

3) Obtain a valid set of SSO login credentials that will work with your SSO Identity Provider (IdP). With
                this set of credentials, obtain a UC SSO access token, e.g. using the sample application found in the
                Common SSO Tutorial[link].

4) Confirm that you have a web server capable of serving HTTPS requests for files you supply. Copy ssocumi.html to the correct directory for your web server’s HTTPS site.

6) Verify that CORS has been enabled on CUC for your web server’s origin/domain.

7) Verify that SSL certificates for CUC and your web server have been imported/enabled in your web
                browser.

## Sample Code Walk-Through

### Creating the XMLHttpRequest Object

```
var xmlhttp = new XMLHttpRequest (); //Create XML request object xmlhttp . open ( 'GET' , 'https://' + cucHost + '/vmrest/mailbox/folders/inbox/messages' ); //CUC REST API to retrieve mailbox info
```

After retrieving the UCM host SSO token from the HTML input fields, the Javascript code creates the XMLHttpRequest object used to make the CUMI request.

### Adding the Accept Header

```
xmlhttp . setRequestHeader ( 'Accept' , 'application/xml' );
```

The next step adds the Accept: application/xml header to the HTTP
                request, to indicate to CUMI that the application expects an XML response.

### Adding the Authorization: Bearer Header

```
xmlhttp . setRequestHeader ( "Authorization" , "Bearer " + ssoToken ); //Add 'Authorization' header with 'Bearer' and token
```

Next, the code adds the Authorization header, including the Bearer type and the SSO token to authenticate the CUC user.

### Handling the XMLHttpRequest Completion Event

```
xmlhttp . onreadystatechange = function () { //Handle completion event of the XML request if ( xmlhttp . readyState == 4 ) { //State is complete if ( xmlhttp . status == 200 ) { //Status is 200 OK var xml = new XMLSerializer (). serializeToString ( xmlhttp . responseXML ); //Extract the XML string from the response document . getElementsByName ( "response" )[ 0 ]. value = xml ; //Display the XML in the text area } } }
```

This block of code sets an event handler for the XMLHttpRequest objects’s completion event. If the
                event is called with state=4 (complete) and status=200 (200 OK), then the code extracts the XML response and displays it in the web page text area.

### Launching the XMLHttpRequest

```
xmlhttp . send (); //Launch the XML request
```

Once the XMLHttpRequest has been prepared, and the event handler is in place, the actual request is
                launched as the final step.

## Sample REST Response

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> <Messages total= "1" > <Message> <Subject> test </Subject> <Read> true </Read> <Dispatch> false </Dispatch> <Secure> false </Secure> <Priority> Normal </Priority> <Sensitivity> Normal </Sensitivity> <URI> /vmrest/messages/0:66c77193-73bf-4da3-a0c2-5b04d8af9f0b </URI> <MsgId> 0:66c77193-73bf-4da3-a0c2-5b04d8af9f0b </MsgId> <From> <DisplayName> user </DisplayName> <SmtpAddress> user1@ds-cuc105.cisco.com </SmtpAddress> <DtmfAccessId> 2000 </DtmfAccessId> </From> <CallerId> <CallerNumber> 2000 </CallerNumber> <CallerName> user </CallerName> </CallerId> <ArrivalTime> 1412103349000 </ArrivalTime> <Size> 21174 </Size> <Duration> 1880 </Duration> <IMAPUid> 1 </IMAPUid> <FromSub> true </FromSub> <MsgType> Voice </MsgType> </Message> </Messages>
```

If everything went well, CUMI should respond to the request with a 200
                OK status and include some XML info about the user’s inbox. For full details about the
                contents of the CUMI inbox resource response, see the CUMI API Reference