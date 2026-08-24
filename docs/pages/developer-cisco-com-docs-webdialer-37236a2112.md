---
doc_id: developer-cisco-com-docs-webdialer-37236a2112
source_url: https://developer.cisco.com/docs/webdialer/
retrieved_at: 2026-08-24T22:13:01.326925+00:00
---

# Overview

WebDialer is a Cisco Unified Communications Manager (Unified CM) service that provides a Click-to-Dial (C2D) API for web services-based and browser-based applications.

Developers should have knowledge or experience in the following areas:

- SOAP

- XML

- HTML

- WSDL

There are two implementations of WebDialer:

- SOAP - XML over HTTP which can be used from almost any application platform

- URL - an HTML implementation which is a browser-based/URL-invoked user interface which can easily be added to any web page

For both interfaces, 8443 is the secure/HTTPS port and 8080 is the
insecure/HTTP (not-recommended) port.

## Accessing the Cisco WebDialer service

Accessing the WebDialer API from your application or with a testing tool, such as SoapUI, requires sending a request to the Cisco WebDialer node where the Cisco WebDialer service is running.

The most current Cisco WebDialer service is included with Cisco Unified CM and can be accessed by your application using these URLs:

- SOAP: https://[cucm]:8443/webdialer/services/WebdialerSoapservice70

- HTML: https://[cucm]:8443/webdialer/Webdialer

Note: Please refer to the 'New and Changed Information for Cisco Unified CM 15 SU5' Section for changes to these URLs

Replace [cucm] with the Cisco Unified CM node name (typically a Publisher
node) or IP address.

In order to access the Cisco WebDialer service, be sure that all required services are turned on. See Service Activation .

WebDialer enables developers to add click-to-dial functionality to almost any application, such as a corporate directory browser or an email application plug-in. WebDialer can make calls using either an end-user's credentials or with an application-user on-behalf-of an
end-user (proxy).  The call is launched directly from the end-user's phone.

Note: Any phones supported by Cisco Unified CM Computer Telephony Integration (CTI) (TAPI or JTAPI) can be used with WebDialer.

For applications serving multiple Cisco Unified CM clusters, WebDialer can
determine an end-user's home cluster in order to place the click-to-dial call
correctly. This is accomplished for the SOAP implementation using the <isClusterUserSoap> request, and performed automatically for the HTML
implementation via the WebDialer Redirector service.

Note: For information on WebDialer and Redirector service
configuration, refer to the Features and services Guide for
Cisco Unified Communications Manager.

## SOAP client application workflow

Obtain the SOAP Webdialer service URL (for example, https://[cucm]:8443/webdialer/services/WebdialerSoapservice70 ). This is typically pre-configured in the application

Obtain the target phone number and the end-user's username/password
credentials (or the credentials of an application-user with the
'Standard EM Authentication Proxy Rights' role), typically using an
Application UI

Send a <getProfileSoap> (supports proxy) or <getProfileDetailSoap> request, which returns a listing of the user's available phone devices/lines

Select the desired device profile, for example, through application
interaction with the user

Send a <makeCallSoap> request to the configured WebDialer service URL, including the credentials, target phone number, and device/line
information.

## Multi-cluster SOAP client application workflow

Obtain a list of WebDialer service URLs for each cluster. This is
typically pre-configured in the application

Obtain the target phone number and the end-user's username/password
credentials (or the credentials of an application-user with the
'Standard EM Authentication Proxy Rights' role), typically using an
Application UI

For each WebDialer service URL, send an <isClusterUserSoap> request
specifying the end-user's username, until a true result is found - use this WebDialer URL for the subsequent requests, as below

Send a <getProfileSoap> (supports proxy) or <getProfileDetailSoap> request, which returns a listing of the user's available phone devices/lines

Select the desired device profile, for example, through application
interaction with the user

Send a <makeCallSoap> request to the configured WebDialer service URL, including the credentials, target phone number, and device/line
information.

Note: Applications may wish to persist the end-user's phone/line
preference and home cluster WebDialer service URL for future operations.

## Browser-Based HTML client application workflow (single-cluster or multi-cluster)

Obtain a WebDialer service URL from any node, e..g the Publisher. If the WebDialer Redirector service is configured for multi-cluster use, additional WebDialer service URLs are not needed

The browser application opens the WebDialer HTML service URL (typically by launching a pop-up window), specifying the
target phone number

The WebDialer service on Cisco Unified CM will then determine the
end-user's home cluster, and reply with a new HTML page providing a
user-interface for viewing/selecting the desired device/line,
launching the call, and optionally ending the call

The WebDialer service includes a cookie in the HTML response, which
will cache the user login session and device preferences, used automatically for any subsequent requests

Note: The HTML user-interface for selecting device/line and launching the call is hosted by CUCM and is not customizable. The duration of the End Call dialog is configurable in the WebDialer service parameters

## Cisco product security overview

Cisco provides a free online Security Vulnerability Policy portal at
this URL:

http://www.cisco.com/en/US/products/products_security_vulnerability_policy.html

From this site, you can perform these tasks:

- Report security vulnerabilities in Cisco products

- Obtain assistance with security incidents that involve Cisco products

- Register to receive security information from Cisco

A current list of security advisories and notices for Cisco products is
available at this URL:

http://www.cisco.com/go/psirt

If you prefer to see advisories and notices as they are updated in real
time, you can access a Product Security Incident Response Team (PSIRT) RSS feed from this URL:

http://tools.cisco.com/security/center/rss.x?i=44

# Development guidelines

These guidelines are recommendations for developers to reduce the number and extent of updates:

Developers should not depend on the order of events or messages unless that order is documented. The order of events and/or messages may change. For example, if:

A feature invocation involves two or more independent transactions; the events or messages may be interleaved

In such cases, events related to the second transaction may precede messages related to the first

Or, events or messages may be delayed due to situations beyond control of the interface (for example, network or transport failures)

Applications should be able to recover from out-of-order events or messages, even when the order is required for protocol operation

Developers must avoid unnecessary dependence on the order of elements when interpreting data. The order of elements within the interface event or message may change, within the constraints of the protocol specification

Developers must disregard or provide generic treatments for any unknown elements or unknown values of known elements encountered. New interface events, methods, responses, headers, parameters, attributes, other elements, or new values of existing elements may be introduced

Previous interface events, methods, responses, headers, parameters, attributes, and other elements will remain and maintain their previous stated meaning and behavior in every way possible. They will remain consistent even when defects with them need to be corrected

Applications must never be dependent on interface behavior resulting from defects. That is, not consistent with the published interface specifications. Application behavior might change when a defect is fixed

Remove deprecated methods, handlers, events, responses, headers, parameters, attributes, or other elements from applications as soon as possible to avoid issues when those deprecated items are removed from Cisco Unified CM

Application Developers must be aware that not all new features or new supported devices will be forward compatible. New features and devices (for example, phones) may require application modifications to work properly

# New and changed

This section provides information on new and changed Information for the UC Manager WebDialer interfaces:

New and Changed Information for Cisco Unified CM 15.5

No changes for Cisco Unified CM 14

New and Changed Information for Cisco Unified CM 12.5

No changes for Cisco Unified CM 12.0

No changes for Cisco Unified CM 11.5

No changes for Cisco Unified CM 11.0

New and Changed Information for Cisco Unified CM 10.5

New and Changed Information for Cisco Unified CM 10.0

See WebDialer Operations by Release .

# New and changed information for Cisco Unified CM 15su5

Starting with Cisco Unified CM 15su5, the WebDialer service will be updated with a new WSDL implementation using Axis2 framework.

## Important Migration Notice

The legacy WebDialer WSDL URLs will no longer be supported starting from Cisco Unified CM 15su5. Developers must migrate to the new WSDL implementation.

New WSDI : XML

xml

```
<?xml version="1.0" encoding="UTF-8"?> < wsdl: definitions xmlns: wsdl = " http://schemas.xmlsoap.org/wsdl/ " xmlns: ns = " http://webdialer.ccm.cisco.com " xmlns: xs = " http://www.w3.org/2001/XMLSchema " xmlns: soap = " http://schemas.xmlsoap.org/wsdl/soap/ " targetNamespace = " http://webdialer.ccm.cisco.com " > < wsdl: types > < xs: schema xmlns: ax22 = " http://webdialer.ccm.cisco.com " attributeFormDefault = " qualified " elementFormDefault = " qualified " targetNamespace = " http://webdialer.ccm.cisco.com " > < xs: element name = " getPrimaryLine " > < xs: complexType > < xs: sequence > < xs: element name = " args0 " type = " ns:Credential " minOccurs = " 0 " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " getPrimaryLineResponse " > < xs: complexType > < xs: sequence > < xs: element name = " return " type = " xs:string " minOccurs = " 0 " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " isClusterUserSoap " > < xs: complexType > < xs: sequence > < xs: element name = " args0 " nillable = " false " type = " xs:string " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " isClusterUserSoapResponse " > < xs: complexType > < xs: sequence > < xs: element name = " return " type = " xs:boolean " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: complexType name = " Credential " > < xs: sequence > < xs: element name = " userID " type = " xs:string " /> < xs: element name = " password " type = " xs:string " /> < xs: element name = " token " type = " xs:string " minOccurs = " 0 " /> </ xs: sequence > </ xs: complexType > < xs: complexType name = " UserProfile " > < xs: sequence > < xs: element name = " user " type = " xs:string " /> < xs: element name = " deviceName " type = " xs:string " /> < xs: element name = " lineNumber " type = " xs:string " /> < xs: element name = " supportEM " type = " xs:boolean " /> < xs: element name = " locale " type = " xs:string " /> < xs: element name = " dontAutoClose " type = " xs:boolean " /> < xs: element name = " dontShowCallConf " type = " xs:boolean " /> </ xs: sequence > </ xs: complexType > < xs: complexType name = " CallResponse " > < xs: sequence > < xs: element name = " responseCode " type = " xs:int " /> < xs: element name = " responseDescription " type = " xs:string " /> </ xs: sequence > </ xs: complexType > < xs: complexType name = " WDDeviceInfo " > < xs: sequence > < xs: element name = " deviceName " type = " xs:string " /> < xs: element name = " lines " type = " xs:string " maxOccurs = " unbounded " /> </ xs: sequence > </ xs: complexType > < xs: complexType name = " GetConfigResponse " > < xs: sequence > < xs: element name = " description " type = " xs:string " /> < xs: element name = " deviceInfoList " type = " ns:WDDeviceInfo " maxOccurs = " unbounded " /> < xs: element name = " responseCode " type = " xs:int " /> </ xs: sequence > </ xs: complexType > < xs: complexType name = " WDDeviceInfoDetail " > < xs: sequence > < xs: element name = " deviceName " type = " xs:string " minOccurs = " 0 " /> < xs: element name = " lines " type = " xs:string " maxOccurs = " unbounded " minOccurs = " 0 " /> < xs: element name = " phoneDesc " type = " xs:string " minOccurs = " 0 " /> < xs: element name = " phoneType " type = " xs:string " minOccurs = " 0 " /> </ xs: sequence > </ xs: complexType > < xs: complexType name = " ConfigResponseDetail " > < xs: sequence > < xs: element name = " description " type = " xs:string " minOccurs = " 0 " /> < xs: element name = " deviceInfoListDetail " type = " ns:WDDeviceInfoDetail " maxOccurs = " unbounded " minOccurs = " 0 " /> < xs: element name = " responseCode " type = " xs:int " /> </ xs: sequence > </ xs: complexType > < xs: element name = " makeCallSoap " > < xs: complexType > < xs: sequence > < xs: element name = " args0 " type = " ns:Credential " /> < xs: element name = " args1 " type = " xs:string " /> < xs: element name = " args2 " type = " ns:UserProfile " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " makeCallSoapResponse " > < xs: complexType > < xs: sequence > < xs: element name = " return " type = " ns:CallResponse " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " endCallSoap " > < xs: complexType > < xs: sequence > < xs: element name = " args0 " type = " ns:Credential " /> < xs: element name = " args1 " type = " ns:UserProfile " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " endCallSoapResponse " > < xs: complexType > < xs: sequence > < xs: element name = " return " type = " ns:CallResponse " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " getProfileSoap " > < xs: complexType > < xs: sequence > < xs: element name = " args0 " type = " ns:Credential " /> < xs: element name = " args1 " type = " xs:string " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " getProfileSoapResponse " > < xs: complexType > < xs: sequence > < xs: element name = " return " type = " ns:GetConfigResponse " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " getProfileDetailSoap " > < xs: complexType > < xs: sequence > < xs: element name = " args0 " type = " ns:Credential " /> </ xs: sequence > </ xs: complexType > </ xs: element > < xs: element name = " getProfileDetailSoapResponse " > < xs: complexType > < xs: sequence > < xs: element name = " return " type = " ns:ConfigResponseDetail " /> </ xs: sequence > </ xs: complexType > </ xs: element > </ xs: schema > </ wsdl: types > < wsdl: message name = " getPrimaryLineRequest " > < wsdl: part name = " parameters " element = " ns:getPrimaryLine " /> </ wsdl: message > < wsdl: message name = " getPrimaryLineResponse " > < wsdl: part name = " parameters " element = " ns:getPrimaryLineResponse " /> </ wsdl: message > < wsdl: message name = " isClusterUserSoapRequest " > < wsdl: part name = " parameters " element = " ns:isClusterUserSoap " /> </ wsdl: message > < wsdl: message name = " isClusterUserSoapResponse " > < wsdl: part name = " parameters " element = " ns:isClusterUserSoapResponse " /> </ wsdl: message > < wsdl: message name = " makeCallSoapRequest " > < wsdl: part name = " parameters " element = " ns:makeCallSoap " /> </ wsdl: message > < wsdl: message name = " makeCallSoapResponse " > < wsdl: part name = " parameters " element = " ns:makeCallSoapResponse " /> </ wsdl: message > < wsdl: message name = " endCallSoapRequest " > < wsdl: part name = " parameters " element = " ns:endCallSoap " /> </ wsdl: message > < wsdl: message name = " endCallSoapResponse " > < wsdl: part name = " parameters " element = " ns:endCallSoapResponse " /> </ wsdl: message > < wsdl: message name = " getProfileSoapRequest " > < wsdl: part name = " parameters " element = " ns:getProfileSoap " /> </ wsdl: message > < wsdl: message name = " getProfileSoapResponse " > < wsdl: part name = " parameters " element = " ns:getProfileSoapResponse " /> </ wsdl: message > < wsdl: message name = " getProfileDetailSoapRequest " > < wsdl: part name = " parameters " element = " ns:getProfileDetailSoap " /> </ wsdl: message > < wsdl: message name = " getProfileDetailSoapResponse " > < wsdl: part name = " parameters " element = " ns:getProfileDetailSoapResponse " /> </ wsdl: message > < wsdl: portType name = " WDSoapInterfacePortType " > < wsdl: operation name = " getPrimaryLine " > < wsdl: input message = " ns:getPrimaryLineRequest " /> < wsdl: output message = " ns:getPrimaryLineResponse " /> </ wsdl: operation > < wsdl: operation name = " isClusterUserSoap " > < wsdl: input message = " ns:isClusterUserSoapRequest " /> < wsdl: output message = " ns:isClusterUserSoapResponse " /> </ wsdl: operation > < wsdl: operation name = " makeCallSoap " > < wsdl: input message = " ns:makeCallSoapRequest " /> < wsdl: output message = " ns:makeCallSoapResponse " /> </ wsdl: operation > < wsdl: operation name = " endCallSoap " > < wsdl: input message = " ns:endCallSoapRequest " /> < wsdl: output message = " ns:endCallSoapResponse " /> </ wsdl: operation > < wsdl: operation name = " getProfileSoap " > < wsdl: input message = " ns:getProfileSoapRequest " /> < wsdl: output message = " ns:getProfileSoapResponse " /> </ wsdl: operation > < wsdl: operation name = " getProfileDetailSoap " > < wsdl: input message = " ns:getProfileDetailSoapRequest " /> < wsdl: output message = " ns:getProfileDetailSoapResponse " /> </ wsdl: operation > </ wsdl: portType > < wsdl: binding name = " WDSoapInterfaceSoapBinding " type = " ns:WDSoapInterfacePortType " > < soap: binding style = " document " transport = " http://schemas.xmlsoap.org/soap/http " /> < wsdl: operation name = " getPrimaryLine " > < soap: operation soapAction = " getPrimaryLine " /> < wsdl: input > < soap: body use = " literal " /> </ wsdl: input > < wsdl: output > < soap: body use = " literal " /> </ wsdl: output > </ wsdl: operation > < wsdl: operation name = " isClusterUserSoap " > < soap: operation soapAction = " isClusterUserSoap " /> < wsdl: input > < soap: body use = " literal " /> </ wsdl: input > < wsdl: output > < soap: body use = " literal " /> </ wsdl: output > </ wsdl: operation > < wsdl: operation name = " makeCallSoap " > < soap: operation soapAction = " makeCallSoap " /> < wsdl: input > < soap: body use = " literal " /> </ wsdl: input > < wsdl: output > < soap: body use = " literal " /> </ wsdl: output > </ wsdl: operation > < wsdl: operation name = " endCallSoap " > < soap: operation soapAction = " endCallSoap " /> < wsdl: input > < soap: body use = " literal " /> </ wsdl: input > < wsdl: output > < soap: body use = " literal " /> </ wsdl: output > </ wsdl: operation > < wsdl: operation name = " getProfileSoap " > < soap: operation soapAction = " getProfileSoap " /> < wsdl: input > < soap: body use = " literal " /> </ wsdl: input > < wsdl: output > < soap: body use = " literal " /> </ wsdl: output > </ wsdl: operation > < wsdl: operation name = " getProfileDetailSoap " > < soap: operation soapAction = " getProfileDetailSoap " /> < wsdl: input > < soap: body use = " literal " /> </ wsdl: input > < wsdl: output > < soap: body use = " literal " /> </ wsdl: output > </ wsdl: operation > </ wsdl: binding > < wsdl: service name = " webdialer " > < wsdl: port name = " WDSoapInterfacePortType " binding = " ns:WDSoapInterfaceSoapBinding " > < soap: address location = " https://localhost/webdialer/services/webdialer " /> </ wsdl: port > </ wsdl: service > </ wsdl: definitions >
```

### Legacy URLs (Deprecated)

- https://[cucm]:8443/webdialer/services/WebdialerSoapservice?wsdl

- https://[cucm]:8443/webdialer/services/WebdialerSoapService70?wsdl

### New WSDL URL (Cisco Unified CM 15su5 and later)

The new standard WSDL URL is:

- https://[cucm]:8443/webdialer/services/webdialer?wsdl

Replace [cucm] with the Cisco Unified CM node name (typically a Publisher node) or IP address.

## Updated SOAP Interface Operations

The new Axis2-based implementation provides the same 6 core SOAP operations with updated request/response structures. All operations continue to provide the same functionality but with different XML namespace structures.

## <isClusterUserSoap>

This SOAP request determines if a user is a member of the queried cluster - useful in a multi-cluster environment. Send the request to at least one Subscriber running the WebDialer service in each cluster. The cluster which is the home cluster for the user will respond with a <return> value of true .

Once the user's home cluster is identified, all further requests for that user should be sent to that cluster's WebDialer service URL.

This request does not require any authentication/credentials.

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: web = " http://webdialer.ccm.cisco.com " > < soapenv: Header /> < soapenv: Body > < web: isClusterUserSoap > < web: args0 > johndoe </ web: args0 > </ web: isClusterUserSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Header /> < soapenv: Body > < ns2: isClusterUserSoapResponse xmlns: ns2 = " http://webdialer.ccm.cisco.com " > < ns2: return > true </ ns2: return > </ ns2: isClusterUserSoapResponse > </ soapenv: Body > </ soapenv: Envelope >
```

## <getProfileSoap>

Retrieve a list of devices associated with the specified end-user. Details include device names and lines.

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: web = " http://webdialer.ccm.cisco.com " > < soapenv: Header /> < soapenv: Body > < web: getProfileSoap > < web: args0 > < web: userID > testAppUser </ web: userID > < web: password > password </ web: password > </ web: args0 > < web: args1 > johndoe </ web: args1 > </ web: getProfileSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Header /> < soapenv: Body > < ns2: getProfileSoapResponse xmlns: ns2 = " http://webdialer.ccm.cisco.com " > < ns2: return > < ns2: description > Success </ ns2: description > < ns2: deviceInfoList > < ns1: deviceName xmlns: ns1 = " http://webdialer.ccm.cisco.com " > SEP5405DB45B96F </ ns1: deviceName > < ns1: lines xmlns: ns1 = " http://webdialer.ccm.cisco.com " > 1000 ; Global Learned E164 Numbers </ ns1: lines > </ ns2: deviceInfoList > < ns2: responseCode > 0 </ ns2: responseCode > </ ns2: return > </ ns2: getProfileSoapResponse > </ soapenv: Body > </ soapenv: Envelope >
```

## <getPrimaryLine>

Retrieve a user's primary line.

Note: this request does not support proxy authentication

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: web = " http://webdialer.ccm.cisco.com " > < soapenv: Header /> < soapenv: Body > < web: getPrimaryLine > < web: args0 > < web: userID > bill </ web: userID > < web: password > 123 </ web: password > </ web: args0 > </ web: getPrimaryLine > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Header /> < soapenv: Body > < ns2: getPrimaryLineResponse xmlns: ns2 = " http://webdialer.ccm.cisco.com " > < ns2: return > 1000 </ ns2: return > </ ns2: getPrimaryLineResponse > </ soapenv: Body > </ soapenv: Envelope >
```

## <getProfileDetailSoap>

Retrieve a list of devices (including additional details) associated with the specified end-user. Details include device name, lines, description and phone type.

Note: this request does not support proxy authentication

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: web = " http://webdialer.ccm.cisco.com " > < soapenv: Header /> < soapenv: Body > < web: getProfileDetailSoap > < web: args0 > < web: userID > bill </ web: userID > < web: password > 123 </ web: password > </ web: args0 > </ web: getProfileDetailSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Header /> < soapenv: Body > < ns2: getProfileDetailSoapResponse xmlns: ns2 = " http://webdialer.ccm.cisco.com " > < ns2: return > < ns1: description xmlns: ns1 = " http://webdialer.ccm.cisco.com/ " > Success </ ns1: description > < ns1: deviceInfoListDetail xmlns: ns1 = " http://webdialer.ccm.cisco.com/ " > < ns1: deviceName > SEP5405DB45B96F </ ns1: deviceName > < ns1: lines > 1000 ; Global Learned E164 Numbers </ ns1: lines > < ns1: phoneDesc > Auto 1000 </ ns1: phoneDesc > < ns1: phoneType > Cisco IP Communicator </ ns1: phoneType > </ ns1: deviceInfoListDetail > < ns1: responseCode xmlns: ns1 = " http://webdialer.ccm.cisco.com/ " > 0 </ ns1: responseCode > </ ns2: return > </ ns2: getProfileDetailSoapResponse > </ soapenv: Body > </ soapenv: Envelope >
```

## <makeCallSoap>

Place a call.

The <args0> Credential username must match the username specified in the <args2> UserProfile, unless the Credential user has the proxy authentication role. See Authentication

WebDialer does not provide any validation of the destination number. The phone handles the required validation. If an invalid dial string is provided, the SOAP request will succeed, but the phone may not place a call or may place a call that fails to complete.

Note: WebDialer does not support SIP URI dialing.

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: web = " http://webdialer.ccm.cisco.com " > < soapenv: Header /> < soapenv: Body > < web: makeCallSoap > < web: args0 > < web: userID > bill </ web: userID > < web: password > 123 </ web: password > </ web: args0 > < web: args1 > 1002 </ web: args1 > < web: args2 > < web: user > bill </ web: user > < web: deviceName > SEPF01FAF38ABC2 </ web: deviceName > < web: lineNumber > 1001 </ web: lineNumber > < web: supportEM > true </ web: supportEM > < web: locale > ? </ web: locale > < web: dontAutoClose > ? </ web: dontAutoClose > < web: dontShowCallConf > ? </ web: dontShowCallConf > </ web: args2 > </ web: makeCallSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Note: the optional <args2> elements <supportEM> , <locale> , <dontAutoClose> and <dontShowCallConf> are deprecated/ignored

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Header /> < soapenv: Body > < ns2: makeCallSoapResponse xmlns: ns2 = " http://webdialer.ccm.cisco.com " > < ns2: return > < ns2: responseCode > 0 </ ns2: responseCode > < ns2: responseDescription > Success </ ns2: responseDescription > </ ns2: return > </ ns2: makeCallSoapResponse > </ soapenv: Body > </ soapenv: Envelope >
```

## <endCallSoap>

End a call previously launched via <makeCallSoap> .

The <args0> Credential username must match the username specified in the <args1> UserProfile, unless the Credential user has the proxy authentication role. See Authentication

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: web = " http://webdialer.ccm.cisco.com " > < soapenv: Header /> < soapenv: Body > < web: endCallSoap > < web: args0 > < web: userID > bill </ web: userID > < web: password > 123 </ web: password > </ web: args0 > < web: args1 > < web: user > bill </ web: user > < web: deviceName > SEPF01FAF38ABC2 </ web: deviceName > < web: lineNumber > 1001 </ web: lineNumber > < web: supportEM > false </ web: supportEM > < web: locale > ? </ web: locale > < web: dontAutoClose > ? </ web: dontAutoClose > < web: dontShowCallConf > ? </ web: dontShowCallConf > </ web: args1 > </ web: endCallSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Header /> < soapenv: Body > < ns2: endCallSoapResponse xmlns: ns2 = " http://webdialer.ccm.cisco.com " > < ns2: return > < ns2: responseCode > 0 </ ns2: responseCode > < ns2: responseDescription > Success </ ns2: responseDescription > </ ns2: return > </ ns2: endCallSoapResponse > </ soapenv: Body > </ soapenv: Envelope >
```

## New and changed information for Cisco Unified CM release 12.5

- The SOAP interface API <getProfileSoap> was removed from deprecation

## New and changed information for Cisco Unified CM release 10.5

Support for Single Sign-On (SSO) introduced.  Changes affect the following SOAP implementation requests:

- <makeCallSoap>

- <endCallSoap>

- <getProfileDetailSoap>

- <getPrimaryLine>

Support for Client Matter Codes (CMC) and Forced Authorization Codes
(FAC) introduced, see FAC and CMC support

## New and changed information for Cisco Unified CM release 10.0

There were no programmatic changes to the WSDL or API

The SOAP Interface API <getProfileSoap> was deprecated. Use <getProfileDetailSoap> instead

The following elements of the urn:UserProfile type were deprecated:

- <supportEM>

- <locale>

- <dontAutoClose>

- <dontShowCallConf>

# Authentication

Refer to WebDialer Authentication

# FAC and CMC support

Starting with version 10.5, Web Dialer supports Forced Authorization Codes (FAC) and Client Matter Codes (CMC) in two ways:

By performing the HTML or SOAP dial request specifying only the destination number, then manually entering the FAC or CMC code via the phone keypad once the call is started

By providng the destination number + FAC + CMC code in the dial request.

For example, if destination Number = 5555, FAC = 111, and CMC = 222, the user can make a call by providing:

- 5555111# (FAC only)

- 5555222# (CMC only)

- 5555111222# (Both FAC and CMC)

Note: # is optional

If the user does not provide any FAC/CMC code or provides an invalid code, the call itself will fail; however the HTML/SOAP interfaces will return a success response

See more about the FAC/CMC features and configuration in the UC Manager Features and services Guide .

# SOAP interface

You should use the WebDialer SOAP interface when full control over the user experience is desired. The SOAP client is responsible for collecting the end-user’s credentials, obtaining the devices and lines associated with the user account, and specifying which device and line should be used when placing the call.

Use the WebDialer HTML (web-based) Interfaces if Cisco Unified CM should be responsible for these operations.

The WebDialer WSDL is included with each implementation of Cisco Unified CM at:

Code Snippet

```
https://[cucm]:8443/webdialer/wsdl/wd70.wsdl
```

## <isClusterUserSoap>>

This SOAP request determines if a user is a member of the queried cluster - useful in a multi-cluster environment.  Send the request to at least one Subscriber running the WebDialer service in each cluster. The cluster which is the home cluster for the user will respond with a <isClusterUserSoapReturn> value of true .

Once the user's home cluster is identified, all further requests for that user should be sent to that cluster's WebDialer service URL.

This request does not require any authentication/credentials.

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: urn = " urn:WD70 " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Header /> < soapenv: Body > < urn: isClusterUserSoap soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < in0 xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " soapenc:string " > johndoe </ in0 > </ urn: isClusterUserSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Body > < ns1: isClusterUserSoapResponse xmlns: ns1 = " urn:WD70 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < isClusterUserSoapReturn xsi: type = " xsd:boolean " > true </ isClusterUserSoapReturn > </ ns1: isClusterUserSoapResponse > </ soapenv: Body > </ soapenv: Envelope >
```

## <makeCallSoap>

Place a call.

The <in0> Credential username must match the username specified in the <in2> UserProfile, unless the Credential user has the proxy authentication role.  See Authentication

WebDialer does not provide any validation of the destination number. The phone handles the required validation. If an invalid dial
string is provided, the SOAP request will succeed, but the phone may not place a call or may place a call that fails to complete.

Note: WebDialer does not support SIP URI dialing.

When a SIP phone initiates a <makeCallSoap> request, the dial string is passed to the CUCM Digital Analyzer (DA). If it encounters invalid digits, the DA returns an error immediately.  When a SCCP phone initiates a <makeCall> request, the device layer in the Cisco Unified CM server checks for valid numbers, strips any invalid characters, and proceeds with the call.

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: urn = " urn:WD70 " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Header /> < soapenv: Body > < urn: makeCallSoap soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < in0 xsi: type = " urn:Credential " > < userID xsi: type = " xsd:string " > bill </ userID > < password xsi: type = " xsd:string " > 123 </ password > </ in0 > < in1 xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " soapenc:string " > 1002 </ in1 > < in2 xsi: type = " urn:UserProfile " > < user xsi: type = " xsd:string " > bill </ user > < deviceName xsi: type = " xsd:string " > SEPF01FAF38ABC2 </ deviceName > < lineNumber xsi: type = " xsd:string " > ? </ lineNumber > </ in2 > </ urn: makeCallSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Note: the optional <in2> elements <supportEM> , <locale> , <dontAutoClose> and <dontShowCallConf> are deprecated/ignored

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Body > < ns1: makeCallSoapResponse xmlns: ns1 = " urn:WD70 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < makeCallSoapReturn href = " #id0 " /> </ ns1: makeCallSoapResponse > < multiRef xmlns: ns2 = " urn:WD70 " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " id = " id0 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " ns2:CallResponse " > < responseCode xsi: type = " xsd:int " > 0 </ responseCode > < responseDescription xsi: type = " xsd:string " > Success </ responseDescription > </ multiRef > </ soapenv: Body > </ soapenv: Envelope >
```

For a list of possble response codes/descriptions, see Response result codes .

## <endCallSoap>

End a call previously launched via <makeCallSoap> .

The <in0> Credential username must match the username specified in the <in1> UserProfile, unless the Credential user has the proxy authentication role.  See Authentication

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: urn = " urn:WD70 " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Header /> < soapenv: Body > < urn: endCallSoap soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < in0 xsi: type = " urn:Credential " > < userID xsi: type = " xsd:string " > bill </ userID > < password xsi: type = " xsd:string " > 123 </ password > </ in0 > < in1 xsi: type = " urn:UserProfile " > < user xsi: type = " xsd:string " > bill </ user > < deviceName xsi: type = " xsd:string " > SEPF01FAF38ABC2 </ deviceName > < lineNumber xsi: type = " xsd:string " > 1002 </ lineNumber > </ in1 > </ urn: endCallSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Body > < ns1: endCallSoapResponse xmlns: ns1 = " urn:WD70 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < endCallSoapReturn href = " #id0 " /> </ ns1: endCallSoapResponse > < multiRef xmlns: ns2 = " urn:WD70 " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " id = " id0 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " ns2:CallResponse " > < responseCode xsi: type = " xsd:int " > 0 </ responseCode > < responseDescription xsi: type = " xsd:string " > Success </ responseDescription > </ multiRef > </ soapenv: Body > </ soapenv: Envelope >
```

For a list of possble response codes/descriptions, see Response result codes .

## <getProfileSoap>

Retrieve a list devices associated with the specified end-user.  Details include device names and lines.

Request

xml

```
< soapenv: Envelope xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: urn = " urn:WD70 " > < soapenv: Header /> < soapenv: Body > < urn: getProfileSoap soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < in0 xsi: type = " urn:Credential " > < userID xsi: type = " xsd:string " > testAppUser </ userID > < password xsi: type = " xsd:string " > password </ password > </ in0 > < in1 xsi: type = " soapenc:string " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " > johndoe </ in1 > </ urn: getProfileSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Body > < ns1: getProfileSoapResponse soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xmlns: ns1 = " urn:WD70 " > < getProfileSoapReturn href = " #id0 " /> </ ns1: getProfileSoapResponse > < multiRef id = " id0 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " ns2:GetConfigResponse " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " xmlns: ns2 = " urn:WD70 " > < description xsi: type = " xsd:string " > Success </ description > < deviceInfoList soapenc: arrayType = " ns3:WDDeviceInfo[1] " xsi: type = " soapenc:Array " xmlns: ns3 = " urn:WebdialerSoap " > < item href = " #id1 " /> </ deviceInfoList > < responseCode href = " #id2 " /> </ multiRef > < multiRef id = " id2 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " xsd:int " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " > 0 </ multiRef > < multiRef id = " id1 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " ns4:WDDeviceInfo " xmlns: ns4 = " urn:WebdialerSoap " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " > < deviceName xsi: type = " xsd:string " > IPCMRAEU5UCM5X7 </ deviceName > < lines soapenc: arrayType = " xsd:string[1] " xsi: type = " soapenc:Array " > < item xsi: type = " xsd:string " > 1251 ; no partition </ item > </ lines > </ multiRef > </ soapenv: Body > </ soapenv: Envelope >
```

For a list of possble response codes/descriptions, see Response result codes .

## <getProfileDetailSoap>

Retrieve a list of devices (including additional details) associated with the specified end-user.  Details include device name, lines, description and phone type.

Note: this request does not support proxy authentication

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: urn = " urn:WD70 " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Header /> < soapenv: Body > < urn: getProfileDetailSoap soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < in0 xsi: type = " urn:Credential " > < userID xsi: type = " xsd:string " > bill </ userID > < password xsi: type = " xsd:string " > 123 </ password > </ in0 > </ urn: getProfileDetailSoap > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Body > < ns1: getProfileDetailSoapResponse xmlns: ns1 = " urn:WD70 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < getProfileDetailSoapReturn href = " #id0 " /> </ ns1: getProfileDetailSoapResponse > < multiRef xmlns: ns2 = " urn:WD70 " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " id = " id0 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " ns2:ConfigResponseDetail " > < description xsi: type = " soapenc:string " > Success </ description > < deviceInfoListDetail soapenc: arrayType = " ns2:WDDeviceInfoDetail[3] " xsi: type = " soapenc:Array " > < item href = " #id1 " /> < item href = " #id2 " /> < item href = " #id3 " /> </ deviceInfoListDetail > < responseCode xsi: type = " xsd:int " > 0 </ responseCode > </ multiRef > < multiRef xmlns: ns3 = " urn:WD70 " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " id = " id2 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " ns3:WDDeviceInfoDetail " > < deviceName xsi: type = " soapenc:string " > SEPE8B7480316D6 </ deviceName > < lines soapenc: arrayType = " soapenc:string[1] " xsi: type = " soapenc:Array " > < item xsi: type = " soapenc:string " > 1000 ; no partition </ item > </ lines > < phoneDesc xsi: type = " soapenc:string " > SEPE8B7480316D6 </ phoneDesc > < phoneType xsi: type = " soapenc:string " > Cisco 6961 </ phoneType > </ multiRef > < multiRef xmlns: ns4 = " urn:WD70 " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " id = " id3 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " ns4:WDDeviceInfoDetail " > < deviceName xsi: type = " soapenc:string " > SEPF01FAF38ABC2 </ deviceName > < lines soapenc: arrayType = " soapenc:string[1] " xsi: type = " soapenc:Array " > < item xsi: type = " soapenc:string " > 1002 ; no partition </ item > </ lines > < phoneDesc xsi: type = " soapenc:string " /> < phoneType xsi: type = " soapenc:string " > Cisco IP Communicator </ phoneType > </ multiRef > < multiRef xmlns: ns5 = " urn:WD70 " xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " id = " id1 " soapenc: root = " 0 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " ns5:WDDeviceInfoDetail " > < deviceName xsi: type = " soapenc:string " > CSFuserBill </ deviceName > < lines soapenc: arrayType = " soapenc:string[1] " xsi: type = " soapenc:Array " > < item xsi: type = " soapenc:string " > 1001 ; no partition </ item > </ lines > < phoneDesc xsi: type = " soapenc:string " /> < phoneType xsi: type = " soapenc:string " > Cisco Unified Client services Framework </ phoneType > </ multiRef > </ soapenv: Body > </ soapenv: Envelope >
```

For a list of possble response codes/descriptions, see Response result codes .

## <getPrimaryLine>

Retrieve a user’s primary line.

Note: this request does not support proxy authentication

Request

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: urn = " urn:WD70 " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Header /> < soapenv: Body > < urn: getPrimaryLine soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < in0 xsi: type = " urn:Credential " > < userID xsi: type = " xsd:string " > bill </ userID > < password xsi: type = " xsd:string " > 123 </ password > </ in0 > </ urn: getPrimaryLine > </ soapenv: Body > </ soapenv: Envelope >
```

Response

xml

```
< soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: xsd = " http://www.w3.org/2001/XMLSchema " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv: Body > < ns1: getPrimaryLineResponse xmlns: ns1 = " urn:WD70 " soapenv: encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < getPrimaryLineReturn xmlns: soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " xsi: type = " soapenc:string " > 1002 </ getPrimaryLineReturn > </ ns1: getPrimaryLineResponse > </ soapenv: Body > </ soapenv: Envelope >
```

For a list of possble response codes/descriptions, see Response result codes .

## SOAP response result codes

The possible response result codes from the SOAP interface are:

## Hello World (SOAP)

A sample Java project demonstrating usage of the Cisco WebDialer SOAP API and Apache Axis to call <makeCallSoap> , available on GitHub: webdialer-java-sample

# HTML Interface

The WebDialer HTML interface is intended for use by browser-based applications, and provides a basic user interface where the user can interact with Cisco Unified CM to authenticate, select the device/line with which to make a call, and launch/end a call using their chosen device.

The WebDialer HTML UI is typically accessed by launching a browser pop-up window with the WebDialer HTML service URL (HTTP GET), or by submitting an HTML form (HTTP POST).

WebDialer stores a cookie in the browser which persists the user credentials and device/line preference, so that the user does not need to provide/select them for subsequent make call requests.

## makeCall

Place a call.

Note: WebDialer does not support SIP URI dialing.

Navigate the browser or pop-up window to the WebDialer HTML service URL, providing the parameter below.  The URL should point to a CUCM node running the WebDialer service.

Single cluster URL : https://[cucm]:8443/webdialer/Webdialer

Multi cluster URL : https://[cucm]:8443/webdialer/WebdialerRedirector

HTTP methods : GET , POST (recommended)

makeCall sample page

html

```
< html > < head > < title > Web Dialer - makeCall Sample </ title > </ head > < body lang = " EN-US " > < div class = " codesample " > < p class = MsoNormal > Web Dialer - makeCall Sample </ p > < form action = " https://{cucm}/webdialer/Webdialer " method = " POST " > < p > Destination: < input type = " text " name = " destination " value = " 1002 " /> < input type = " submit " value = " Make Call " > </ p > </ form > </ div > </ body > </ html >
```

The above sample should look something like:

## makeCallProxy

Place a call on behalf of an end-user; providing a proxy application-user's username/password, e.g. via hidden fields in a form.

Note: WebDialer does not support SIP URI dialing.

Navigate the browser or pop-up window to the WebDialer HTML service URL, providing the parameters below.  The URL should point to a CUCM node running the WebDialer service.

Single cluster URL : https://[cucm]:8443/webdialer/Webdialer Multi cluster URL : https://[cucm]:8443/webdialer/WebdialerRedirector

HTTP methods : GET , POST (recommended)

makeCallProxy sample page

xml

```
< html > < head > < title > Web Dialer - makeCallProxy Sample </ title > </ head > < body lang = " EN-US " > < div > < p > Web Dialer - makeCallProxy Sample </ p > < form action = " https://{cucm}/webdialer/Webdialer " method = " POST " > < p > < table width = " 50% " > < tr > < td align = " right " > Destination: </ td > < td > < input type = " text " name = " destination " value = " 1002 " /> </ td > </ tr > < tr > < td align = " right " > User ID: </ td > < td > < input type = " text " name = " uid " /> (Same as userid) < input type = " text " name = " appid " > </ td > </ tr > < tr > < td align = " right " > Password: </ td > < td > < input type = " password " name = " pwd " > < input type = " submit " value = " Make Call " > </ td > </ tr > </ table > </ p > </ form > </ div > </ body > </ html >
```

The above sample should look something like:

## Hello World (HTML)

This example shows how to click-to-dial an extension from a web page using makeCall.

### Prerequisites

For this example to work, make sure the following items are completed in Cisco Unified CM:

- Web Dialer service is running on the server

- An end-user account is created and you have the credentials

- A phone device with at least one line is configured and associated to the end-user

html

```
<! DOCTYPE html > < html > < head > < meta content = " text/html;charset=utf-8 " http-equiv = " Content-Type " > < title > WebDialer HTML Example </ title > < script > function launchWebDialerWindow ( url ) { webdialer = window . open ( url , "webdialer" , "status=no, width=420, height=300, scrollbars=no, resizable=yes, toolbar=no" ) ; } < ! -- Rename the server below to the Unified CM server you are using . -- > function launchWebDialerServlet ( destination ) { url = 'https://{cucm}:8443/webdialer/Webdialer?destination=' + escape ( destination ) ; launchWebDialerWindow ( url ) ; } </ script > </ head > < body > < div > < p > Sample WebDialer HTML Application </ p > < p > Make sure the Web Dialer service is running on the Unified CM server , that you have a provisioned phone/device, and that you have added a valid user name, password, and server in the HTML code. </ p > < p > Click the number below to call Bill Smith's phone. </ p > Bill Smith Ext.: < a href = " javascript:launchWebDialerServlet('1002') " > 1002 </ a > </ div > </ body > </ html >
```

Copy and paste the example into a text file with the extension .html , update the appropriate values for your enviroment/users/devices/lines, then open the file with your browser.

# WebDialer service activation

By the default, the WebDialer service is not activated on a new CUCM install.  WebDialer service activation is controlled in the UC Manager Serviceability admin pages.

For WebDialer service activation and redirector/cluster configuration details, see the CUCM Feature Configuration Guide

# Securing WebDialer CTI connections

The WebDialer API is a service hosted on one or more UC Manager nodes.  It connects to another service, the CTI Manager service, which may or not be running on the same node. By default, the connection between the WebDialer service and a CTI Manager service is unencrypted. If the UC Manager node hosting the WebDialer service is in a different location from the CTI Manager node, requiring CTI traffic to travel over unprotected paths or if an encrypted connection is otherwise required, see the Configure Secure TLS Connection to CTI step of the CUCM Feature Configuration Guide for configuration details.

# WebDialer service parameters

The following WebDialer service parameters may be of interest to application developers:

Maximum Concurrent Call Requests parameter of the Cisco WebDialer service controls the maximum number of concurrent WebDialer call requests per second allowed by the WebDialer service:

Default : 3

Minimum : 1

Maximum : 8

Enter a lower value if RTMT alerts, alarms, or performance counters suggest that the hardware associated with WebDialer is over-utilized (for example, high CPU and/or memory usage). Enter a higher value to allow more simultaneous WebDialer call requests. Higher values can add more load to the CPU.

User Session Expiry - the life time (in hours) of a WebDialer service user login session/cookie. A value of 0 indicates that the session never expires:

Default : 0

Minimum : 0

Maximum : 168

Duration of End Call Dialog - the time (in seconds) to display the HTML interface dialog allowing the user to end the call:

Note: the user can override this behaviour by checking the the Disable Auto-Close option in the UI

Default : 15

Minimum : 10

Maximum : 60

Apply Application Dial Rules on Dial / Apply Application Dial Rules on SOAP Dial Request - Dial rules for applications automatically strip numbers from or add numbers to telephone numbers that a user dials. For more details on this feature and its configuration, see the Application Dial Rule Configuration chapter of the CUCM Administration Guide

## Confguring service parameters

Use the following steps to access the WebDialer service parameters:

In Cisco Unified CM Administration choose System / Service Parameters

From the Server drop-down list, choose the UC Manager server on which you want to configure the WebDialer service

From the Service drop-down list, choose Cisco WebDialer Web service

For new service parameter values to take effect, restart the Cisco WebDialer Web service

# Supported phone models

Any phone type supported by Unified CM CTI (TAPI or JTAPI) can be used with WebDialer.

See the CTI Supported Device Matrix

| Parameter | Type | Required | Description |
|---|---|---|---|
| <args0> | string | Required | The user ID of the user or proxy user |

| Parameter | Type | Description |
|---|---|---|
| <return> | boolean | true or false if the user is present in the directory of the cluster |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <args0> | Credential | Required | API user credentials, see Authentication |
| <args1> | string | Required | User for whom to retrieve device details |

| Response element | Type | Description |
|---|---|---|
| <description> | string | Response description |
| <deviceInfoList> | Array of WDDeviceInfo | List of available devices for calling |
| <deviceName> | string | Device name |
| <lines> | string | Directory number + ; + partition of the line appearance |
| <responseCode> | int | Response code (see Response result codes) |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <args0> | Credential | Required | User credentials, see Authentication |

| Response element | Type | Description |
|---|---|---|
| <return> | string | The primary line DN of the user (can be empty) |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <args0> | Credential | Required | User credentials, see Authentication |

| Response element | Type | Description |
|---|---|---|
| <description> | string | Response description |
| <deviceInfoListDetail> | Array of WDDeviceInfoDetail | List of available devices for calling |
| <deviceName> | string | Device name |
| <lines> | string | Directory number + ; + partition of the line appearance |
| <phoneDesc> | string | Phone description |
| <phoneType> | string | Phone type |
| <responseCode> | int | Response code (see Response result codes) |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <args0> | Credential | Required | API user credentials, see Authentication |
| <args1> | string | Required | Destination dial string |
| <args2> | UserProfile | Required | The <user> , <deviceName> , and <lineNumber> used to place the call |

| Response element | Type | Description |
|---|---|---|
| <responseCode> | int | Response code (see Response result codes) |
| <responseDescription> | string | Response description |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <args0> | Credential | Required | API user credentials, see Authentication |
| <args1> | UserProfile | Required | The <user> , <deviceName> , and <lineNumber> of the call to end |

| Response element | Type | Description |
|---|---|---|
| <responseCode> | int | Response code (see Response result codes) |
| <responseDescription> | string | Response description |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <in0> | soapenc:string | Required | The user ID of the user or proxy user |

| Parameter | Type | Description |
|---|---|---|
| <isClusterUserSoapReturn> | xsd:boolean | true or false if the user is present in the directory of the cluster |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <in0> | urn:Credential | Required | API user credentials, see Authentication |
| <in1> | soapenc:string | Required | Destination dial string |
| <in2> | urn:UserProfile | Required | The <user >, <deviceName> , and <lineNumber> used to place the call |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <in0> | urn:Credential | Required | API user credentials, see Authentication |
| <in1> | urn:UserProfile | Required | The <user >, <deviceName> , and <lineNumber> of the call to end |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <in0> | urn:Credential | Required | API user credentials, see Authentication |
| <in1> | soapenc:string | Required | User for whome to retrieve device details |

| Response element | Type | Description |
|---|---|---|
| <deviceInfoList> | soapenc:Array of ns2:WDDeviceInfo | List of available devices for calling |
| <deviceName> | soapenc:string | Device name |
| <lines> | soapenc:Array of soapenc:string | List of directory numbers on the device |
| <item> | soapenc:string | Directory number + ; + partition of the line appearance |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <in0> | urn:Credential | Required | User credentials, see Authentication |

| Response element | Type | Description |
|---|---|---|
| <deviceInfoListDetail> | soapenc:Array of ns2:WDDeviceInfoDetail | List of available devices for calling |
| <deviceName> | soapenc:string | Device name |
| <lines> | soapenc:Array of soapenc:string | List of directory numbers on the device |
| <item> | soapenc:string | Directory number + ; + partition of the line appearance |
| <phoneDesc> | soapenc:string | Phone description |
| <phoneType> | soapenc:string | Phone type |

| Parameter | Type | Required | Description |
|---|---|---|---|
| <in0> | urn:Credential | Required | User credentials, see Authentication |

| Response element | Type | Description |
|---|---|---|
| <getPrimaryLineReturn> | soapenc:string | The primary line DN of the user (can be empty) |

| Code | Description |
|---|---|
| 0 | Success |
| 1 | Call failure error |
| 2 | Authentication error |
| 3 | No authentication proxy rights |
| 4 | Directory error |
| 5 | No device is configured for the user or missing parameters exist in the request |
| 6 | Service temporarily unavailable |
| 7 | Destination cannot be reached |
| 8 | Service error |
| 9 | Service overloaded |

| Parameter | Description |
|---|---|
| destination | Destination dial string |

| Parameter | Description |
|---|---|
| destination | Destination dial string |
| uid | The user on who's behalf to make the call |
| appid | The proxy user ID |
| pwd | The proxy user password |