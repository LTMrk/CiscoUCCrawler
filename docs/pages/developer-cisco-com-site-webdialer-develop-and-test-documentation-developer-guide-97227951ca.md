---
doc_id: developer-cisco-com-site-webdialer-develop-and-test-documentation-developer-guide-97227951ca
source_url: https://developer.cisco.com/site/webdialer/develop-and-test/documentation/developer-guide/
retrieved_at: 2026-09-01T15:34:02.653646+00:00
---

# Overview

WebDialer is a Cisco Unified Communications Manager (Unified CM) service that provides a Click-to-Dial
                (C2D) API for web services-based and browser-based applications.

Developers should have knowledge or experience in the following areas:

- SOAP

- XML

- HTML

- WSDL

There are two implementations of WebDialer:

- a basic

- which can be used from almost any application platform

- an HTML implementation which is a browser-based/URL-invoked user interface which can easily be added
                    to any web page

For both interfaces, 8443 is the secure/HTTPS port and 8080 is the
                insecure/HTTP (not-recommended) port.

## Accessing the Cisco WebDialer Service

Accessing the WebDialer API from your application or with a testing tool, such as SoapUI, requires
                sending a request to the Cisco WebDialer node where the Cisco WebDialer Service is running.

The most current Cisco WebDialer Service is included with Cisco Unified CM and can be accessed by your
                application using these URLs:

- SOAP: https://[cucm]:8443/webdialer/services/WebdialerSoapService70

- HTML: https://[cucm]:8443/webdialer/Webdialer

Replace [cucm] with the Cisco Unified CM node name (typically a Publisher
                node) or IP address and your secured port number.

In order to access the Cisco WebDialer Service, be sure that all required services are turned on. See Service Activation .

WebDialer enables developers to add C2D (Click-to-Dial) functionality to almost any application, such as
                a corporate directory browser or an email application plug-in. WebDialer can make calls using either
                end-user’s credentials or an application-user to make calls on-behalf of an
                end-user.The C2D call is launched directly from the end-user’s phone.

Note: Any phones supported by Cisco Unified CM Computer Telephony
                Integration (CTI) (TAPI or JTAPI) can be used with WebDialer.

For applications serving multiple Cisco Unified CM clusters, WebDialer can
                determine an end-user’s home cluster in order to place the C2D call
                correctly. This is accomplished for the SOAP implementation using the isClusterUserSoap request, and performed automatically for the HTML
                implementation with the WebDialer Redirector service.

Note: For information on WebDialer and Redirector service
                configuration, refer to the Features and Services Guide for
                    Cisco Unified Communications Manager

## Web Services-Based Client Application Workflow

- Obtain the SOAP Webdialer service URL (for example,
                    https://[cucm]:8443/webdialer/services/WebdialerSoapService70). This is typically pre-configured in
                    the application.

- Obtain the target phone number and the end-user’s username/password
                    credentials (or the credentials of an Application-User with the
                    ‘Standard EM Authentication Proxy Rights’ role), typically using an
                    Application UI.

- Send a getProfileDetailSoap request, which returns a listing of the
                    end-user’s available phone devices/lines.

- Select the desired device profile, for example, through application
                    interaction with the end-user.

- Send a makeCallSoap request to the configured WebDialer service
                    URL, including the credentials, target phone number, and device/line
                    information.

## Multi-Cluster Web Services-Based
                Client Application Workflow

- Obtain a list of WebDialer service URLs for each cluster. This is
                    typically pre-configured in the application.

- Obtain the target phone number and the end-user’s username/password
                    credentials (or the credentials of an Application-User with ‘Standard
                    EM Authentication Proxy Rights’ role), typically through an application
                    user Interface.

- For each WebDialer service, send an isClusterUserSoap request
                    specifying the end-user’s Name, until a true result is
                    found. Once
                    the correct address is found, use this WebDialer URL for the subsequent
                    requests, as below.

- Send a getProfileDetailSoap request, which returns a listing of the
                    user’s available phone devices/lines.

- Select the desired device profile, for example, through application
                    interaction with the user.

- Send a makeCallSoap request to the configured WebDialer service
                    URL, including the credentials, target phone number, and device/line
                    information.

Note: Applications may wish to persist the end-user’s phone/line
                preference and home cluster WebDialer service URL for future C2D
                operations.

## Browser-Based Client
                Application Workflow (Single-Cluster or Multi-Cluster)

- Obtain a WebDialer service URL. If the WebDialer Redirector service
                    is configured for multi-cluster use, additional WebDialer service URLs
                    are not needed.

- The browser application sends a HTTP request to the WebDialer
                    service URL (typically by launching a pop-up window), specifying the
                    target phone number.

- The WebDialer service on Cisco Unified CM will then determine the
                    end-user’s home cluster, and reply with a new HTML page providing a
                    user-interface for viewing/selecting the desired device/line,
                    launching the call, and optionally ending the call.

- The WebDialer service includes a cookie in the HTML response, which
                    will cache the user login session and device preferences for any
                    subsequent requests.

Note: The HTML user-interface for selecting device/line and
                launching the call is hosted by Cisco Unified CM and is not customizable. The
                duration of the End Call dialog is configurable in the WebDialer
                service parameters.

## Cisco Product Security Overview

Cisco provides a free online Security Vulnerability Policy portal at
                this URL: http://www.cisco.com/en/US/products/products_security_vulnerability_policy.html

From this site, you can perform these tasks:

- Report security vulnerabilities in Cisco products.

- Obtain assistance with security incidents that involve Cisco
                    products.

- Register to receive security information from Cisco.

A current list of security advisories and notices for Cisco products is
                available at this URL: http://www.cisco.com/go/psirt

If you prefer to see advisories and notices as they are updated in real
                time, you can access a Product Security Incident Response Team Really Simple Syndication (PSIRT RSS)
                feed from this URL:

http://www.cisco.com/en/US/products/products_psirt_rss_feed.html

# Development Guidelines

These guidelines are recommendations for developers to reduce the number and extent of updates.

Developers should never depend on the order of events or messages. The order of events and/or
                    messages may change. For example:

- A feature invocation involves two or more independent transactions;
                            the events or messages may be interleaved.

- In such cases, events related to the second transaction may precede
                            messages related to the first.

- Or, events or messages may be delayed due to situations beyond
                            control of the interface (for example, network or transport failures).

- Applications should be able to recover from out-of-order events or
                            messages, even when the order is required for protocol operation.

Developers must avoid unnecessary dependence on the order of
                    elements to interpret information. The order of elements within the
                    interface event or message may change, within the constraints of the
                    protocol specification.

Developers must disregard or provide generic treatments for any
                    unknown elements or unknown values of known elements encountered. New
                    interface events, methods, responses, headers, parameters, attributes,
                    other elements, or new values of existing elements may be introduced.

Previous interface events, methods, responses, headers, parameters,
                    attributes, and other elements will remain and maintain their previous
                    stated meaning and behavior in every way possible. They will remain
                    consistent even when defects with them need to be corrected.

Applications must never be dependent on interface behavior resulting
                    from defects. That is, not consistent with the published interface
                    specifications. Application behavior might change when a defect is
                    fixed.

Remove deprecated methods, handlers, events, responses, headers,
                    parameters, attributes, or other elements from applications as soon as
                    possible to avoid issues when those deprecated items are removed from
                    Cisco Unified CM.

Application Developers must be aware that not all new features or
                    new supported devices will be forward compatible. New features and
                    devices (for example, phones) may require application modifications to work
                    properly.

# New and Changed

This section provides information on New and Changed Information for the Cisco Unified CM WebDialer
                Interface:

No changes for Cisco Unified CM 14

No changes for Cisco Unified CM 12.0

No changes for Cisco Unified CM 11.0

New and Changed Information for Cisco Unified CM 10.5(1)

New and Changed Information for Cisco Unified CM 10.0(1)

New and Changed Information for Cisco Unified CM 9.0(1)

New and Changed Information for Cisco Unified CM
                    8.6(1)

New and Changed Information for Cisco Unified CM
                    8.0(1)

See WebDialer Operations by Release .

## New and Changed Information for
                Cisco Unified CM Release 10.5(1)

Support for Single Sign-On (SSO) introduced.  Changes affect
                    the following SOAP implementation requests: makeCallSoap , endCallSoap , getProfileDetailSoap , getPrimaryLine .

Support for Client Matter Codes (CMC) and Forced Authorization Codes
                    (FAC) introduced.

## New and Changed Information for
                Cisco Unified CM Release 10.0(1)

There were no programmatic changes to the WSDL or API.

The SOAP Interface API getProfileSoap was deprecated. Use gerProfileDetailSoap instead.

The parameter elements supportEM , locale , dontAutoClose , and dontShowCallConf of the complexType in2 (“User Profile”) were
                    deprecated.

# Authentication

Refer to WebDialer Authentication .

# FAC and CMC Support

Starting with version 10.5, Web Dialer supports Forced Authorization Codes (FAC) and Client Matter Codes
                (CMC) in two ways:

By entering the Destination number in Dial text box in WebDialer HTML
                    page (or) SOAP request and then manually enter the FAC (or) CMC code on the phone.

By entering the Destination number followed by FAC (or) CMC
                    code in Dial text box in WebDialer HTML page (or) SOAP request.

For example, if Destination Number = 5555, FAC = 111, and CMC = 222, the User can make a call by
                providing 5555111# (FAC enabled) / 5555222# (CMC enabled) / 5555111222# (Both FAC and CMC enabled), # is
                optional here.

Note:

If the user does not provide any FAC/CMC code or provides an
                    invalid code, the call will fail. But, the HTML UI and SOAP UI will
                    return a success response.

If the user makes a call from HTML using any special characters in
                    the Destination Number (DN), the call will complete successfully after
                    stripping the special characters. This rule does not apply to use of the SOAP API.

See more about FAC/CMC in Features and Services Guide for Cisco Unified Communications Manager .

# SOAP Interface

You should use WebDialer SOAP interfaces when full control over the user experience is desired. The SOAP
                client is responsible for collecting the end-user’s credentials, obtaining the devices and lines
                associated with the user account, and specifying which device and line should be used when placing the
                call.

Use the WebDialer HTML (web-based) Interfaces if Cisco Unified CM should be responsible for these
                operations.

## Get the WSDL

The WebDialer WSDL is included with each implementation of Cisco Unified CM.

Follow these steps to get the WSDL for WebDialer:

Copy the address below into your browser: https://[cucm]:8443/webdialer/wsdl/wd70.wsdl

Replace [cucm] with the Cisco Unified CM node (typically a
                    Publisher node) or IP address and your secured port.

When the WSDL is accessed by your browser, you can save it to a
                    text file for review or testing later.

## isClusterUserSoap

This SOAP request determines a User’s home cluster in a
                multi-cluster environment. Send the request to at least one Subscriber
                running the WebDialer service for each cluster. The cluster which has
                the user account will respond with a Boolean value of true. Once the
                User’s home cluster is identified, all further requests for that user
                should be sent to that cluster.

### isClusterUserSoap Request

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header/> <soapenv:Body> <urn:isClusterUserSoap soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "soapenc:string" > bill </in0> </urn:isClusterUserSoap> </soapenv:Body> </soapenv:Envelope>
```

A provisioned user ID is the only request parameter for this API.

in0 is the required parameter. It is a string variable that must
                contain the ID of the user or proxy user whose membership in a cluster
                is to be returned.

### isClusterUserSoap Response

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Body> <ns1:isClusterUserSoapResponse xmlns:ns1= "urn:WD70" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <isClusterUserSoapReturn xsi:type= "xsd:boolean" > true </isClusterUserSoapReturn> </ns1:isClusterUserSoapResponse> </soapenv:Body> </soapenv:Envelope>
```

## makeCallSoap

Use this interface to place a call.

The makeCallSoap interface is a SOAP request to the Cisco Unified
                CM server where the WebDialer service is running, typically on a Subscriber node.

Note: WebDialer does not provide any validation of the destination
                number. The phone handles the required validation. If an invalid dial
                string is provided, the SOAP request will succeed. But, the phone may not place a call or may place a
                call that results in a reorder. WebDialer does not support SIP URI dialing. When a SIP phone
                initiates a makeCallSoap request, the numbers dialed get passed to the Digital Analyst (DA). If it
                receives invalid numbers the DA returns a ‘Block’ immediately. When a SCCP phone initiates
                a makeCall request, the device layer in the Cisco Unified CM server checks for valid numbers and strips
                the dialed digits if they contain special characters.

### makeCallSoap Request

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header /> <soapenv:Body> <urn:makeCallSoap soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xsi:type= "urn:Credential" > <userID xsi:type= "xsd:string" > bill </userID> <password xsi:type= "xsd:string" > 123 </password> </in0> <in1 xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "soapenc:string" > 1002 </in1> <in2 xsi:type= "urn:UserProfile" > <user xsi:type= "xsd:string" > bill </user> <deviceName xsi:type= "xsd:string" > SEPF01FAF38ABC2 </deviceName> <lineNumber xsi:type= "xsd:string" > ? </lineNumber> </in2> </urn:makeCallSoap> </soapenv:Body> </soapenv:Envelope>
```

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header /> <soapenv:Body> <urn:makeCallSoap soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xsi:type= "urn:Credential" > <token xsi:type= "xsd:string" > MjpjMTAzNDk4NC00ZjhhLTQzMTMtYjdlNS0xMTI2MDgzNzNlZDg </token> </in0> <in1 xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "soapenc:string" > 1002 </in1> <in2 xsi:type= "urn:UserProfile" > <user xsi:type= "xsd:string" > bill </user> <deviceName xsi:type= "xsd:string" > SEPF01FAF38ABC2 </deviceName> <lineNumber xsi:type= "xsd:string" > ? </lineNumber> </in2> </urn:makeCallSoap> </soapenv:Body> </soapenv:Envelope>
```

in0 (Credential) is the required input parameter.

in0 is composed of either:

- a userID and password pair

- a SSO token (see Authentication )

in1 (destination) is a string that represents the destination number
                being dialed.

in2 (UserProfile) represents the user, device, and line to be used. This
                information can be obtained using the getProfileDetailSoap and getPrimaryLine requests.

in2 is composed of:

- true

- false

- true

- false

- true

- false

### makeCallSoap Response

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Body> <ns1:makeCallSoapResponse xmlns:ns1= "urn:WD70" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <makeCallSoapReturn href= "#id0" /> </ns1:makeCallSoapResponse> <multiRef xmlns:ns2= "urn:WD70" xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" id= "id0" soapenc:root= "0" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "ns2:CallResponse" > <responseCode xsi:type= "xsd:int" > 0 </responseCode> <responseDescription xsi:type= "xsd:string" > Success </responseDescription> </multiRef> </soapenv:Body> </soapenv:Envelope>
```

This API will dial a number using the request parameters above. If a
                required condition is not met, a status result message consisting of an integer value and a string
                description of what was encountered will be returned.

### Status Result Codes

## endCallSoap

Use this interface to end a call.

You access the endCallSoap interface by initiating a SOAP request to the Cisco Unified CM server where
                the WebDialer service is
                running, typically on a Subscriber node.

### endCallSoap Request

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header /> <soapenv:Body> <urn:endCallSoap soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xsi:type= "urn:Credential" > <userID xsi:type= "xsd:string" > bill </userID> <password xsi:type= "xsd:string" > 123 </password> </in0> <in1 xsi:type= "urn:UserProfile" > <user xsi:type= "xsd:string" > bill </user> <deviceName xsi:type= "xsd:string" > SEPF01FAF38ABC2 </deviceName> <lineNumber xsi:type= "xsd:string" > 1002 </lineNumber> </in1> </urn:endCallSoap> </soapenv:Body> </soapenv:Envelope>
```

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header /> <soapenv:Body> <urn:endCallSoap soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xsi:type= "urn:Credential" > <token xsi:type= "xsd:string" > MjpjMTAzNDk4NC00ZjhhLTQzMTMtYjdlNS0xMTI2MDgzNzNlZDg </token> </in0> <in1 xsi:type= "urn:UserProfile" > <user xsi:type= "xsd:string" > bill </user> <deviceName xsi:type= "xsd:string" > SEPF01FAF38ABC2 </deviceName> <lineNumber xsi:type= "xsd:string" > 1002 </lineNumber> </in1> </urn:endCallSoap> </soapenv:Body> </soapenv:Envelope>
```

in0 (Credential) is a complexType.

in0 is composed of either:

- a userID and password pair

- a SSO token (see Authentication )

in1 (UserProfile) defines the line number and user identifcation to end.

in1 is composed of:

- true

- false

- true

- false

- true

- false

### endCallSoap Response

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Body> <ns1:endCallSoapResponse xmlns:ns1= "urn:WD70" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <endCallSoapReturn href= "#id0" /> </ns1:endCallSoapResponse> <multiRef xmlns:ns2= "urn:WD70" xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" id= "id0" soapenc:root= "0" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "ns2:CallResponse" > <responseCode xsi:type= "xsd:int" > 0 </responseCode> <responseDescription xsi:type= "xsd:string" > Success </responseDescription> </multiRef> </soapenv:Body> </soapenv:Envelope>
```

### Status Result Codes

## getProfileDetailSoap

Use this interface to obtain a list of devices and lines associated with the end-user.

You access the getProfileDetailSoap interface by initiating a SOAP
                request to the URL to the Cisco Unified CM server
                where the WebDialer service is running, typically on a Subscriber node.

### getProfileDetailSoap Request

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header /> <soapenv:Body> <urn:getProfileDetailSoap soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xsi:type= "urn:Credential" > <userID xsi:type= "xsd:string" > bill </userID> <password xsi:type= "xsd:string" > 123 </password> </in0> </urn:getProfileDetailSoap> </soapenv:Body> </soapenv:Envelope>
```

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header /> <soapenv:Body> <urn:getProfileDetailSoap soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xsi:type= "urn:Credential" > <token xsi:type= "xsd:string" > MjpjMTAzNDk4NC00ZjhhLTQzMTMtYjdlNS0xMTI2MDgzNzNlZDg </token> </in0> </urn:getProfileDetailSoap> </soapenv:Body> </soapenv:Envelope>
```

in0 (Credential) is a complexType.

in0 is composed of either:

- a userID and password pair

- a SSO token (see Authentication )

### getProfileDetailSoap Response

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Body> <ns1:getProfileDetailSoapResponse xmlns:ns1= "urn:WD70" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <getProfileDetailSoapReturn href= "#id0" /> </ns1:getProfileDetailSoapResponse> <multiRef xmlns:ns2= "urn:WD70" xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" id= "id0" soapenc:root= "0" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "ns2:ConfigResponseDetail" > <description xsi:type= "soapenc:string" > Success </description> <deviceInfoListDetail soapenc:arrayType= "ns2:WDDeviceInfoDetail[3]" xsi:type= "soapenc:Array" > <item href= "#id1" /> <item href= "#id2" /> <item href= "#id3" /> </deviceInfoListDetail> <responseCode xsi:type= "xsd:int" > 0 </responseCode> </multiRef> <multiRef xmlns:ns3= "urn:WD70" xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" id= "id2" soapenc:root= "0" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "ns3:WDDeviceInfoDetail" > <deviceName xsi:type= "soapenc:string" > SEPE8B7480316D6 </deviceName> <lines soapenc:arrayType= "soapenc:string[1]" xsi:type= "soapenc:Array" > <item xsi:type= "soapenc:string" > 1000 ; no partition </item> </lines> <phoneDesc xsi:type= "soapenc:string" > SEPE8B7480316D6 </phoneDesc> <phoneType xsi:type= "soapenc:string" > Cisco 6961 </phoneType> </multiRef> <multiRef xmlns:ns4= "urn:WD70" xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" id= "id3" soapenc:root= "0" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "ns4:WDDeviceInfoDetail" > <deviceName xsi:type= "soapenc:string" > SEPF01FAF38ABC2 </deviceName> <lines soapenc:arrayType= "soapenc:string[1]" xsi:type= "soapenc:Array" > <item xsi:type= "soapenc:string" > 1002 ; no partition </item> </lines> <phoneDesc xsi:type= "soapenc:string" /> <phoneType xsi:type= "soapenc:string" > Cisco IP Communicator </phoneType> </multiRef> <multiRef xmlns:ns5= "urn:WD70" xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" id= "id1" soapenc:root= "0" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "ns5:WDDeviceInfoDetail" > <deviceName xsi:type= "soapenc:string" > CSFuserBill </deviceName> <lines soapenc:arrayType= "soapenc:string[1]" xsi:type= "soapenc:Array" > <item xsi:type= "soapenc:string" > 1001 ; no partition </item> </lines> <phoneDesc xsi:type= "soapenc:string" /> <phoneType xsi:type= "soapenc:string" > Cisco Unified Client Services Framework </phoneType> </multiRef> </soapenv:Body> </soapenv:Envelope>
```

### Status Result Codes

## getPrimaryLine

Use this interface to retrieve the user’s primary line.

The getPrimaryLine interface is accessed by initiating a SOAP request to the Cisco Unified CM server
                where the WebDialer service is running, typically on a Subscriber node.

### getPrimaryLine Request

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header /> <soapenv:Body> <urn:getPrimaryLine soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xsi:type= "urn:Credential" > <userID xsi:type= "xsd:string" > bill </userID> <password xsi:type= "xsd:string" > 123 </password> </in0> </urn:getPrimaryLine> </soapenv:Body> </soapenv:Envelope>
```

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn= "urn:WD70" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header /> <soapenv:Body> <urn:getPrimaryLine soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <in0 xsi:type= "urn:Credential" > <token xsi:type= "xsd:string" > MjpjMTAzNDk4NC00ZjhhLTQzMTMtYjdlNS0xMTI2MDgzNzNlZDg </token> </in0> </urn:getPrimaryLine> </soapenv:Body> </soapenv:Envelope>
```

in0 (Credential) is a complexType.

in0 is composed of either:

- a userID and password pair

- a SSO token (see Authentication )

### getPrimaryLine Response

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Body> <ns1:getPrimaryLineResponse xmlns:ns1= "urn:WD70" soapenv:encodingStyle= "http://schemas.xmlsoap.org/soap/encoding/" > <getPrimaryLineReturn xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/" xsi:type= "soapenc:string" > 1002 </getPrimaryLineReturn> </ns1:getPrimaryLineResponse> </soapenv:Body> </soapenv:Envelope>
```

## Hello World (SOAP)

### Example Scenario

We want to call a phone using a custom application. This Hello World
                uses makeCallSoap from the WebDialer SOAP Interface.

### Prerequisites

For this example to work, make sure the following items are
                completed in Cisco Unified CM:

- Web Dialer Service is running on the server.

- End-user account is created.

- Device and Line are configured and associated to the end user
                    account.

The first step is to import the WebDialer WSDLs into Java classes. The
                WSDLs for WebDialer use a deprecated feature that Axis2 and the current
                Java-included wsimport utility do not understand. So you’ll have to
                blend Axis1 with some Axis2 libraries in order to do the job.

- Download Axis2 here .

- Unzip it into a directory, such as “Axis2”

- Download the compressed file for Axis1 (version 1.4) here .

- Unzip it into a directory, such as “Axis1”

This project needs the Axis1 libraries (jar files) and two more jar
                files from Axis2. Here’s an example of how you can combine the two, plus
                add the WebDialer WSDL.

- cd \Axis1\lib

- copy \Axis2\lib\activation-1.1.jar .

- copy \Axis2\lib\mail-1.4.jar .

- copy \wherever\WebDialer.wsdl \Axis1\lib

Now you need to create the Java classes from the WSDL. The easiest way
                to do this is directly from the Axis1\lib directory, and then move the
                Java package you will create to your project directory.

You can use this command to convert the WSDL files into Java classes:

java -cp
                axis.jar;commons-logging-1.0.4.jar;commons-discovery-0.2.jar;jaxrpc.jar;saaj.jar;wsdl4j-1.5.1.jar;activation-1.1.jar;mail-1.4.jar
                org.apache.axis.wsdl.WSDL2Java WebDialer.wsdl

This assumes you have a local copy of the WSDL file. You can specify a
                URL instead of the name of the local WSDL file in the above command, if
                you prefer.

Now you should be able to use the following application to make a call.
                Run the application with the command-line parameters < username >
                < password > < origin >
                < destination > to make the call.

For a more complex application, it might be a good idea to include all
                of the Axis1\lib jar files in the build path of your project. Here is a list:

- activation-1.1.jar

- axis-ant.jar

- axis.jar

- commons-discovery-0.2.jar

- commons-logging-1.0.4.jar

- jaxrpc.jar

- log4j-1.2.8.jar

- log4j.properties

- mail-1.4.jar

- saaj.jar

- WebDialer.wsdl

- wsdl4j-1.5.1.jar

```
package com.yourcompany.yoursystem.sample;

        import WD70.*;
        import org.apache.axis.AxisFault;
        import java.rmi.RemoteException;
        import javax.xml.rpc.Service;
        import java.net.*;

        public class MakeCall {

            protected static String wdHost = null;
            protected static String wdUser = null;
            protected static String wdPwd = null;
            protected static String wdOrigin = null;
            protected static String wdDestination = null;

            public static void main(String[] args) {
                if ( args.length &lt; 5 ) {
                    System.out.println ( &quot; Usage: MakeACall &quot; );
                    System.exit ( 1 );
                }
                wdUser = args[0];
                wdPwd = args[1];
                wdHost = args[2];
                wdOrigin = args[3];
                wdDestination = args[4];
                String lineNumber = &quot;&quot; ;
                String response;

                try {
                    /*
                     * Get the Axis client service object for use later
                     */

                    Service service = new org.apache.axis.client.Service();

                    /*
                     * Establish the calling user &#39; s credentials
                     */
                    Credential userCred = new Credential(wdUser, wdPwd);

                    /*
                     * Insert the hostname into the full https URL
                     */
                    URL soapURL = new URL( &quot; https:// &quot; + wdHost + &quot; :8443/webdialer/services/WebdialerSoapService70 &quot; );

                    /*
                     * Create the Webdialer stub using the URL and the service we established earlier
                     *
                     */
                    WebdialerSoapServiceSoapBindingStub stub = new WebdialerSoapServiceSoapBindingStub(soapURL,service);
                    /*
                     * Get the primary line for the outgoing call
                     */
                    lineNumber = stub.getPrimaryLine(userCred);

                    /*
                     * Create a phone user profile, and set the originating phone for the call
                     *
                     */
                    UserProfile uProfile = new UserProfile();
                    uProfile.setDeviceName(wdOrigin);
                    uProfile.setUser(wdUser);
                    uProfile.setLineNumber(lineNumber);
                    uProfile.setLocale( &quot; local &quot; );

                    /*
                     * Make the call to the destination phone
                     * Wait a bit for it to ring
                     *
                     */
                    stub.makeCallSoap(userCred, wdDestination, uProfile);
                    try {
                        Thread.sleep(3000);
                    } catch (InterruptedException e) {
                        // handle the exception...
                    }

                    /*
                     * Look for the API response and print it to the console
                     */
                    CallResponse cResponse = new CallResponse();
                    response = cResponse.getResponseDescription();
                    System.out.println(response);

                } catch (AxisFault e) {
                    // Exception handling code
                } catch (RemoteException e1 ) {
                    // Exception handling code
                } catch (MalformedURLException e2) {
                    // Exception handling code
                }
            }
        } </destination></origin></host></password></username>
```

# HTML Interface

The WebDialer HTML interface is intended for use by browser-based
                applications, and provides a basic user interface so the user can
                interact with Cisco Unified CM to authenticate, select the device/line with which to make a call, and
                launch/end a call using their chosen device. The WebDialer HTML UI is typically accessed by
                launching a browser pop-up window with a URL plus parameters (HTTP GET) or by submitting an HTML form
                (HTTP POST.)

WebDialer stores a cookie in the browser (if enabled) which persists the user credentials and device/line
                preference for subsequent requests.

## makeCall

Use this interface to place calls.

An HTTPS request is made to https://[cucm]:8443/webdialer/Webdialer

where [cucm] specifies the fully-qualified name or IP address of the
                Cisco Unified CM node where the WebDialer service is running. This
                server will typically be a Subscriber node.

Note: WebDialer does not provide any validation of the destination
                number. The phone handles the required validation. If an invalid dial
                string is provided, the SOAP request will succeed. But, the phone may not place a call or may place a
                call that results in a reorder. WebDialer does not support SIP URI dialing. When a SIP phone
                initiates a makeCallSoap request, the numbers dialed get passed to the Digital Analyst (DA). If it
                receives invalid numbers, the DA returns a ‘Block’ immediately. When a SCCP phone
                initiates a makeCall request, the device layer in the Cisco Unified CM server checks for valid numbers
                and strips the dialed digits if they contain special characters.

### makeCall Request

```
<html> <head> <meta http-equiv= Content-Type content= "text/html; charset=utf-8" > <title> Web Dialer - makeCall Sample </title> </head> <body lang= "EN-US" > <div class= "codesample" > <p class= MsoNormal > Web Dialer - makeCall Sample </p> <FORM action= "https://192.168.168.27/webdialer/Webdialer" method= "POST" > <P> Destination: <INPUT type= "text" name= "destination" value= "1002" /> <INPUT type= "submit" value= "Make Call" > </P> </FORM> </div> </body> </html>
```

See (in the right hand panel) sample code for a simple HTML page which displays a simple form UI for
                submitting a request to the WebDialer service.  When the user clicks the Make Call button, the HTML form is submitted to WebDialer as a POST request. The HTML response from the WebDialer
                service is displayed in the browser as an HTML page where the user can authenticate and launch the call.

### makeCall Response

The makeCall HTML request will generate a form in your
                application similar to the following:

## makeCallProxy

C2D (Click-to-Dial) applications which authenticate end users can use the makeCallProxy
                interface, so end users are not prompted to enter their credentials
                multiple times. The C2D application sends the end users ID, Application
                User ID, and Application User Password in the body of the POST message to proxy the request on
                behalf of the end user.

Note: WebDialer does not provide any validation of the destination
                number. The phone handles the required validation. If an invalid dial
                string is provided, the SOAP request will succeed. But, the phone may not place a call or may place a
                call that results in a reorder. WebDialer does not support SIP URI dialing. When a SIP phone initiates a
                makeCallSoap request, the numbers dialed get passed to the Digital Analyst (DA). If it receives invalid
                numbers, the DA returns a ‘Block’ immediately. When a SCCP phone initiates a makeCall
                request, the device layer in the Cisco Unified CM server checks for valid numbers and strips the dialed
                digits if they contain special characters.

### makeCallProxy Request

```
<html> <head> <meta http-equiv= Content-Type content= "text/html; charset=utf-8" > <title> Web Dialer - makeCallProxy Sample </title> </head> <body lang= "EN-US" > <div class= "codesample" > <p class= MsoNormal > Web Dialer - makeCallProxy Sample </p> <form action= "https://cucm3.kpiint.com/webdialer/Webdialer" method= "POST" > <p> <table width= "50%" > <tr> <td align= "right" > Destination: </td> <td> <input type= "text" name= "destination" value= "1002" /> </td> </tr> <tr> <td align= "right" > User ID: </td> <td> <input type= "text" name= "uid" /> (Same as userid) <input type= "text" name= "appid" > </td> </tr> <tr> <td align= "right" > Password: </td> <td> <input type= "password" name= "pwd" > <input type= "submit" value= "Make Call" > </td> </tr> </table> </p> </form> </div> </body> </html>
```

See (in the right hand panel) sample code for a simple HTML page which displays a simple form UI for
                submitting a request to the WebDialer service. When the user clicks the Make Call button, the HTML form is submitted to WebDialer as a POST request. The HTML response from the WebDialer
                service is displayed in the browser as an HTML page where the user can select the preferred calling
                device, and launch/end the call.

### makeCallProxy Response

## Hello World (HTML)

### Example Scenario

This example shows how to click-to-dial an extension from a web page.

```
<html> <head> <meta http-equiv= Content-Type content= "text/html; charset=windows-1252" > <title> WebDialer HTML Example </title> <script> function launchWebDialerWindow( url ) {
                webdialer=window.open( url, "webdialer", "status=no, width=420, height=300, scrollbars=no, resizable=yes, toolbar=no" );
              } function launchWebDialerServlet( destination ) {
                  url = 'https://cucm3.kpiint.com:8443/webdialer/Webdialer?destination=' + escape(destination);
                  launchWebDialerWindow( url );
                } </script> </head> <body lang= EN-US > <div class= Section1 > <p class= MsoNormal > Sample WebDialer HTML Application </p> </p> Make sure the Web Dialer Service is running on the Unified CM server , that you have a provisioned phone/device,
            and that you have added a valid user name, password, and server in the HTML code. </p> </p> </p> </p> Click the number below to call Bill Smith's phone. </p> </p> </p> </p> Bill Smith    Ext. <TD> <A href= "javascript:launchWebDialerServlet('1002')" > 1002 </A> </TD> </div> </body> </html>
```

### Prerequisites

Before this example will work make sure the following items are
                completed in Unified CM:

- Web Dialer Service is running on the server.

- End-user account is created.

- Device and Line are configured and associated to the End User
                    account.

You can copy and paste the example into a text file with the extension HTML, or you can download the text
                file here.

### Sample Code Snippets

The sample code snippets enable WebDialer from a directory search page.

#### Single-Cluster Applications

1 Use this snippet for single-cluster applications if all users are in
                    only one cluster.

```
<FORM action= "https://42.88.86.1/webdialer/Webdialer" method= "post" > <P> <INPUT type= "hidden" name= "destination" value= "+666" > <INPUT type= "submit" value= "Send" > </P> </FORM>
```

Refer to example 1 in the right-hand panel.
                Use this snippet for single-cluster applications if all users are in
                only one cluster.

#### Multiple-Cluster Applications

Refer to example 2 in the right-hand panel.
                Use this snippet if all users are spread across different clusters.

2 Use this snippet if all users are spread across different clusters.

```
function launchWebDialerWindow( url ) {
            webdialer=window.open( url, "webdialer", "status=no, width=420, height=300, scrollbars=no, resizable=yes, toolbar=no" );
          }
         function launchWebDialerServlet( destination ) {
            url= 'https:// <0.0.0.0:8080> /webdialer/Redirector?destination='+escape(destination);
            launchWebDialerWindow( url );
          }
```

Refer to example 3 in the right-hand panel.
                This function can be called from a HTML page which has a hyperlink to
                a phone number to be called.

3 This function can be called from a HTML page which has a hyperlink to
                    a phone number to be called.

```
<TD><A href= "javascript:launchWebDialerServlet( <%= userInfo.TelephoneNumber %> )" > < %=
        userInfo.TelephoneNumber %> </A> </TD>
```

# Service Activation

Service Activation is handled in Communications Manager Serviceability.
                You will need to activate the WebDialer service. For a cluster
                configuration, review Cluster Service activation recommendations.

From the Cisco Unified CM Administration window, choose Cisco Unified Serviceability .

Then select Tools > Service Activation .

Ensure the Cisco WebDialer Web Service is activated.

# Security

## Overview

The WebDialer API is a service hosted on one or more Cisco Unified CM nodes that uses the CTI
                capabilities of Cisco Unified CM, as provided by the CTI Manager service. By default, the
                connection between the WebDialer service and the CTI Manager service is unencrypted. If the UC Manager
                node hosting the WebDialer service is in a different location from the CTI Manager node, requiring
                CTI traffic to travel over unprotected paths, or if an encrypted connection is otherwise required, see
                the below procedure for configuring and enabling WebDialer to use a secure CTI connection.

## Cisco WebDialer Security Support

The Cisco IP telephony network establishes and maintains authenticated
                communication streams, digitally signs files before transferring the
                file to the phone, and encrypts media streams and call signaling between Cisco Unified IP Phones. This
                prevents identity theft of the phones on the Cisco Unified CM server, data tampering, and
                call-signal/media-stream tampering.

Device, file, and signaling authentication rely on the creation of the
                Certificate Trust List (CTL) file, which is created when you install and configure the Cisco Certificate
                Trust List (CTL) Client on a single
                Windows workstation or server that has a USB port. The CTL file contains a server certificate, public
                key, serial number, signature, issuer name, subject name, server function, DNS name, and IP address for
                each server.

When multiple instances of a CTI/JTAPI/TAPI application are running, CTI TLS support requires you to
                configure a unique instanceID (IID) for
                every application instance to secure signaling and media communication
                streams between CTI Manager and JTAPI/TSP/CTI applications.

The WebDialer API is a service hosted on one or more UC Manager nodes,
                and uses the CTI capabilities of UC Manager, as provided by the CTI
                Manager service.  By default, the connection between the WebDialer
                service and the CTI Manager service is unencrypted.  If the UC Manager
                node hosting the WebDialer service is in a different location than the
                CTI Manager node, requiring CTI traffic to travel over unprotected
                paths, or if an encrypted connection is otherwise required, see the
                below procedure for configuring and enabling WebDialer to use a secure
                CTI connection.

The following configuration must be completed before WebDialer can be
                configured to open a CTI connection in secure mode.

Log on to the Cisco Unified CM Server with an Admin ID and
                    password. In the Navigation dialog, select Cisco Unified
                        Serviceability and click Go . Select Tools , then
                    select Service Activation. Activate the Cisco CTL Provider service
                    in the Security Services section on the page.

Activate the Cisco Certificate Authority Proxy Function service.

From the Cisco Unified CM Administration page, click on the Application menu and select Plugins . Click the Find button without selecting any search options and you will be provided with a
                    list of all plugins. Download the Cisco CTL Client.

Run the CTL Client. If your server is part of a cluster, enable Cluster Security and follow the instructions that display. This will require USB E-tokens.

To verify that cluster security is enabled, go to Cisco Unified
                    Communications Manager Administration and look at System > Enterprise Parameter
                        configuration . Look at the Security Parameters;
                    the cluster security should be set to 1.

In Cisco Unified CM Administration, from the User Management drop-down menu, select User Settings , click Application User CAPF Profile , Click Add New .

In the Application User CAPF Profile Configuration window:

- For Certificate Operation , select Install/Upgrade from the
                            drop-down menu.

- For Authentication Mode , select By Authentication String from the drop-down menu.

- For Authentication String , enter the value of authorization string; for
                            example, 12345.

- For Key Size , select key size from drop-down menu; for example, 1024.

- For Operation Completes By , enter the vlaue in the format yyyy:mm:dd:hh:mn,
                            for example 2015:07:30:12:30.

Press Save .

Note: If the date and time has passed, the certificate update
                operation will fail.

WebDialer supports secure connections to CTI (TLS- transport layer
                security connection.) For this feature, WebDialer uses the security API
                that JTAPI provides. Refer to Unified CM JTAPI Developers Guide for
                    the JTAPI API .

For comprehensive details about how to implement Cisco Security for your application(s) and environment,
                see the Cisco Unified Communications Manager Security Guide, Release
                    10.0(1) .

# Performance

## Maximum Concurrent Call Requests

The maximum concurrent call request parameter signals the maximum number
                of concurrent WebDialer call requests per second supported by the
                WebDialer service. The minimum and maximum values for this throttle are
                one and eight.

Enter a lower value if RTMT alerts, alarms, or performance counters
                suggest that the hardware associated with WebDialer is over-utilized
                (for example, high CPU and/or memory usage). Enter a higher value to
                allow more simultaneous WebDialer call requests. Higher values can add
                more load to the CPU. The default value for this parameter is three.

Cisco Unified CM provides the following service
                parameters for the WebDialer service:

The CAPF Profile Instance ID for Secure Connection to CTI Manager parameter specifies the Instance ID of the Application CAPF Profile for application user WDSecureSysUser that this Cisco Web Dialer
                    server will use to open a secure connection to CTI Manager .

For Primary Cisco CTIManager , enter the IP address of the
                    primary Cisco CTIManager .

The default IP address of the Cisco CTI Manager is 127.0.0.1, which
                    is the LocalHost server used to set up Cisco Web Dialer. The maximum
                    length is 15 digits.

To use Backup Cisco CTIManager , enter the IP address of the backup Cisco CTIManager . The maximum length is 15 digits. No IP address
                    implies no backup Cisco CTIManager exists.

User Session Expiry is calculated in hours. Enter the duration, in
                    hours, for how long the user login session is valid. A default value of
                    0 indicates that the login session is valid for an indefinite time,
                    until the next Cisco Web Dialer Web Service restart. The minimum
                    length is represented as 0 hours, but the actual maximum length
                    duration is 168 hours.

To use Duration of End Call Dialog , enter the duration, in seconds, to display the
                    dialog to end a call. This dialog indicates
                    that the user must end the call if the user dialed out in error. The
                    default value is 15 seconds, with a maximum value of 60 seconds and a
                    minimum value of 10 seconds. To disable the Duration of End Call
                        Dialog service parameter, the user checks the Disable Auto-Close check box in the User Options window. If the Disable Auto-Close check box is checked, the End Call dialog does not close
                    automatically, and the Hangup button returns the user to the Make
                        Call window.

The Apply Application Dial Rules on Dial default is set to True .
                    If you do not need Cisco Web Dialer to use application dial rules,
                    change the setting to False .

The CTI Manager Connection Security Flag is a cluster-wide
                    parameter which indicates whether security for the Cisco WebDialer service CTI Manager connection gets disabled or complies with the
                    security mode of the cluster. If security is enabled, Cisco
                        WebDialer opens a secure connection to CTI Manager by using the Application CAPF profile that is configured in Application CAPF
                        Profile Instance Id for the Secure Connection to CTI Manager parameter.

In Cisco Unified CM Administration choose System > Service Parameters .

From the Server drop-down list, choose the Cisco Unified
                    Communications Manager server on which you want to configure Cisco
                    WebDialer service parameters.

From the Service drop-down list, choose Cisco WebDialer Web
                    Service . Default values already exist for the parameters Primary Cisco CTIManager , Duration of End Call Dialog , User
                        SessionExpiry (InHours), and Apply Application Dial Rules (True). Enter new values if your application requires them.
                    The parameter Backup Cisco CTIManager does not have any default values assigned.
                    Enter values for this parameter if your application requires a backup of Cisco CTIManager.

For new parameter values to take effect, restart the Cisco
                    WebDialer Web Service.

# Supported Phones

## Phone Support For Cisco WebDialer

Any phones supported by Unified CM CTI (TAPI or JTAPI) can be used with
                WebDialer.

Click here for a list.

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| in0 | <soapenc:string> | Required | <user ID> | The user ID of the user or proxy user. |

| Parameter Name | Type | Description |
|---|---|---|
| isClusterUserSoapReturn | <xsd:boolean> | The result is true if the user is present in the directory of the cluster. The result is false
                        if the user is not present in the directory. |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| in0 | <xsd:complexType> | Required |  | Credential |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| userID | <xsd:string> | Required | <user ID> | The user ID of the user or proxy user. |
| password | <xsd:string> | Required | <password> | The password of the user or proxy user. |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| token | <xsd:string> | Required | <token> | A SSO token |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| in1 | <soapenc:string> | Required | <destination number> | The destination number being dialed. Format: +1 408 5551212 or for extensions, 2222. |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| in2 | <xsd:complexType> | Required | <userprofile> | The user, device, and line to be used |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| user | <xsd:string> | Required | <user> | The user from the profile used to make a call. The type in2 represents the userProfile. |
| deviceName | <xsd:string> | Required | <device name> | A device such as an IP phone or line. |
| lineNumber | <xsd:string> | Optional | <line number> | This line number should be in the same format as returned by getProfileSoap—<number>;
                        <partition>. |
| supportEM | <xsd:boolean> | Optional | true false | (Not used) / Deprecated |
| locale | <xsd:string> | Optional | <locale> | (Not used) / Deprecated |
| dontAutoClose | <xsd:string> | Optional | true false | (Not used) / Deprecated |
| dontShowCallConf | <xsd:string> | Optional | true false | (Not used) / Deprecated |

| Status Code | Name | Type | Description | Action by application |
|---|---|---|---|---|
| 0 | responseCode | Integer | Success | Displays a dialog box. |
|  | responseDescription | String | Success |  |
| 1 | responseCode | Integer | Call failure error | Displays a general error message. |
|  | responseDescription | String | Call failure error |  |
| 2 | responseCode | Integer | Authentication error | Displays the authentication dialog where the user enters ID and password information. |
|  | responseDescription | String | User authentication error |  |
| 3 | responseCode | Integer | No authentication proxy rights | Void for user-based applications. |
|  | responseDescription | String | No authentication proxy rights |  |
| 4 | responseCode | Integer | Directory error | Displays an appropriate directory error message. |
|  | responseDescription | String | Directory error |  |
| 5 | responseCode | Integer | No device is configured for the user, or missing parameters exist in the request. | The application initiates a getProfileSoap request and displays the selected device and line to
                        the user. |
|  | responseDescription | String | No device is configured for the user, or missing parameters exist in the request. |  |
| 6 | responseCode | Integer | Service temporarily unavailable | Displays the appropriate error dialog with an option to try again. |
|  | responseDescription | String | Service temporarily unavailable |  |
| 7 | responseCode | Integer | Destination cannot be reached. | Displays the appropriate error dialog that allows the user to edit the dialed number. |
|  | responseDescription | String | Destination cannot be reached. |  |
| 8 | responseCode | Integer | Service error | Displays the appropriate error dialog. |
|  | responseDescription | String | Service error |  |
| 9 | responseCode | Integer | Service overloaded | Displays the appropriate error dialog with an option to try again. |
|  | responseDescription | String | Service overloaded |  |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| in0 | <xsd:complexType> | Required |  | Credential |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| userID | <xsd:string> | Required | <user ID> | The user ID of the user or proxy user. |
| password | <xsd:string> | Required | <password> | The password of the user or proxy user. |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| token | <xsd:string> | Required | <token> | A SSO token |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| in1 | <xsd:complexType> | Required | <userprofile> | The line number and user identification to end |

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| user | <xsd:string> | Required | <user> | The user from the profile used to make a call. The type “in2” represents the
                        UserProfile. |
| deviceName | <xsd:string> | Required | <device name> | A device such as an IP phone or line. |
| lineNumber | <xsd:string> | Optional | <line number> | The line should be in the same format as returned by getProfileSoap—<number>; <partition>. |
| supportEM | <xsd:boolean> | Optional | true false | (Not used) / Deprecated |
| locale | <xsd:string> | Optional | <locale> | (Not used) / Deprecated |
| dontAutoClose | <xsd:string> | Optional | true false | (Not used) / Deprecated |
| dontShowCallConf | <xsd:string> | Optional | true false | (Not used) / Deprecated |

| Status Code | Name | Type | Description | Action by application |
|---|---|---|---|---|
| 0 | responseCode | Integer | Success | Displays a dialog box on the computer screen. |
|  | responseDescription | String | Success |  |
| 1 | responseCode | Integer | Call failure error | Displays a relevant error message. |
|  | responseDescription | String | Call failure error. |  |
| 2 | responseCode | Integer | Authentication error | Displays authentication dialog for user to enter user ID and password. |
|  | responseDescription | String | User authentication error. |  |
| 3 | responseCode | Integer | No authentication proxy rights | Void for user-based applications. |
|  | responseDescription | String | No authentication proxy rights. |  |
| 4 | responseCode | Integer | Directory error | Displays an appropriate directory error message. |
|  | responseDescription | String | Directory error. |  |
| 5 | responseCode | Integer | No device is configured for the user, or missing parameters exist in the request. | The Application initiates a getProfileSoap request and displays the selected device
                        and line to the user. |
|  | responseDescription | String | No device is configured for the user, or missing parameters exist in the request. |  |
| 6 | responseCode | Integer | Service temporarily unavailable | Displays the appropriate error dialog with an option to try again. |
|  | responseDescription | String | Service temporarily unavailable. |  |
| 7 | responseCode | Integer | Destination cannot be reached. | Displays the appropriate error dialog that allows the user to edit the dialed
                        number. |
|  | responseDescription | String | Destination cannot be reached. |  |
| 8 | responseCode | Integer | Service error | Displays appropriate error dialog. |
|  | responseDescription | String | Service error. |  |
| 9 | responseCode | Integer | Service overloaded | Displays the appropriate error dialog with an option to try again. |
|  | responseDescription | String | Service overloaded. |  |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| in0 | <xsd:complexType> | Required |  | Credential |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| userID | <xsd:string> | Required | <user ID> | The user ID of the user or proxy user. |
| password | <xsd:string> | Required | <password> | The password of the user or proxy user. |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| token | <xsd:string> | Required | <token> | A SSO token |

| Parameter Name | Type | Description |
|---|---|---|
| deviceInfoListDetail | soapenc:Array | Devices returned with multi-reference array name. |
| responseCode | xsd:int | The Status Result Code for the overall query. |
| deviceName | soapenc:string of multiRef Array | The unique name of the device being returned. |
| lines | soapenc:string of soapenc:Array of multiRef Array | Directory number(s) configured on the device. |
| phoneDesc | soapenc:string of multiRef Array | Description of phone(s). |
| phoneType | soapenc:string of multiRef Array | The type of phone (model). |

| Status Code | Name | Type | Description | Action by application |
|---|---|---|---|---|
| 0 | responseCode | Integer | Returns an array of phones or lines on the phone that is associated with the user. Also returns
                        Phone Description and the Phone type for each device. | Displays a dialog box. |
|  | responseDescription | String | Success |  |
|  | deviceInfoListDetail | Array | Returns an array of the WDDeviceInfoDetail data type |  |
| 1 | responseCode | Integer | No device configured for the user | Displays an appropriate error message. |
|  | responseDescription | String | No device configured for the user |  |
| 2 | responseCode | Integer | Authentication error | Displays the authentication dialog where the user enters ID and password information. |
|  | responseDescription | String | User authentication error |  |
| 3 | responseCode | Integer | No authentication proxy rights | Void for user-based applications. |
|  | responseDescription | String | No authentication proxy rights |  |
| 4 | responseCode | Integer | Directory error | Displays an appropriate directory error message. |
|  | responseDescription | String | Directory error |  |
| 6 | responseCode | Integer | Service temporarily unavailable | Displays the appropriate error dialog with an option to try again. |
|  | responseDescription | String | Service temporarily unavailable |  |
| 9 | responseCode | Integer | Service overloaded | Displays the appropriate error dialog with an option to try again. |
|  | responseDescription | String | Service overloaded |  |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| in0 | <xsd:complexType> | Required |  | Credential |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| userID | <xsd:string> | Required | <user ID> | The user ID of the user or proxy user. |
| password | <xsd:string> | Required | <password> | The password of the user or proxy user. |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| token | <xsd:string> | Required | <token> | A SSO token |

| Name | Type | Description |
|---|---|---|
| getPrimaryLineReturn | <soapenc:string> | The result returns the number that is configured by the Cisco Unified CM
                        Administrator as the primary line for the user. |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| destination | <string> | Required | <Phone number or extension> | Destination number called by the application. |

| Parameter Name | Description |
|---|---|
| result | The WebDialer service responds with an HTML page providing a user interface for the
                        user to login (if no valid cookie is found), select the preferred calling device, and launch/end
                        the call. |

| Parameter Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| uid | <string> | Yes | <user ID> | The user ID for which the request is made |
| appid | <string> | Yes | <application ID> | This is the user ID of the application user account making a request on behalf of
                        the end-user. For example, consider a server-based corporate directory application where the
                        application first authenticates the end-user during login, then uses a single Application
                        Account to make requests on behalf of the end-user. |
| pwd | <string> | Yes | <password> | The password of the appid |
| destination | <string> | Yes | <phone number> | The number to be called. |

| Name | Description |
|---|---|
| result | The WebDialer service responds with an HTML page providing a user interface for the
                        user to login (if no valid cookie is found), select the preferred calling device, and launch/end
                        the call. |