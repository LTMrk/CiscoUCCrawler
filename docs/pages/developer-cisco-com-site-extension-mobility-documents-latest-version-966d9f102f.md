---
doc_id: developer-cisco-com-site-extension-mobility-documents-latest-version-966d9f102f
source_url: https://developer.cisco.com/site/extension-mobility/documents/latest-version/
retrieved_at: 2026-08-25T21:05:10.149388+00:00
---

# Overview

## Cisco Extension Mobility API

The Cisco Unified Communications Manager (Unified CM) Extension Mobility feature (E/M)
                                allows end-users to access their personal Cisco Unified IP Phone configuration,
                                including directory number, line appearances, phone services, and speed dials, from any
                                other E/M-enabled phone on the UCM system via a simple login user interface on the
                                phone.

For more on the Cisco Unified CM Extension Mobility feature, including setup and
                                configuration steps, refer to the Cisco Unified Communications Manager
                                    Administration Guide or the Cisco Unified Communications Manager Features
                                    and Services Guide.

The Cisco Extension Mobility API (E/M API) provides an HTTP/XML interface enabling
                                applications to automate E/M actions, including:

- Logging a user into a specific phone

- Logging out a user

- Forcing E/M logout for all users

- Querying for the E/M login status of specific users or devices

The E/M API can be used in conjunction with the on-phone E/M login service, or customers
                                may choose to remove the default E/M login service from user phones in favor of using a
                                custom developed IP Phone Services API appliction which uses the E/M API to manage or
                                automate logins.

This Developer Guide provides information for developers building applications that
                                extend the functionality of the Cisco Extension Mobility service. Developers should be
                                familiar with Extensible Markup Language (XML) and secure HTTP network requests.

## Use Cases

Examples of applications which can be developed using the E/M API include:

- “Hot desk seating” for visiting employees in office situations

- Providing personalized phone service to patients’ rooms in a hospital or
                                    clinic

- Hotel/hospitality solutions, which can automate customized phone settings for guest
                                    rooms

- Scheduling conference calls for specific rooms/phones via an automated reservation
                                    system

Note: The Extension Mobility API does not support the Extension Mobility
                                Cross Cluster feature.

Note: Extension Mobility logouts performed via an E/M API logout request
                                will not automatically remove call history entries from the phone. See the Cisco
                                    Extension Mobility service parameter Clear Call Logs on Intra-Cluster
                                    EM for more info.

If removing call history entries is desired, entries can be removed from the phone after
                                an E/M API logout operation by using either the AXL or IP Phone Services APIs:

- Reset the device via the AXL SOAP <doDeviceReset> request, specifying the isHardReset parameter as true . See Cisco
                                        AXL Developer Site .

- POST a <CiscoIPPhoneExecute> XML request object to the phone's onboard
                                    web server, specifying a URI of Init:CallHistory . See Cisco IP Phone Service
                                        Developer .

## Cisco Product Security Overview

This product contains cryptographic features and is subject to United States and local
                                country laws governing import, export, transfer and use.

Note: Delivery of Cisco cryptographic products does not imply third-party authority to
                                import, export, distribute or use encryption. Importers, exporters, distributors, and
                                users are responsible for compliance with U.S. and local country laws. By using this
                                product you agree to comply with applicable laws and regulations. If you are unable to
                                comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at http://www.cisco.com/wwl/export/crypto/tool/stqrg.html .
                                If you need further assistance, contact us by sending e-mail to export@cisco.com.

# Development Guidelines

## Compatibility

Cisco Unified Communications Manager (Unified CM):

- Maintains interface backwards compatibility for at least one previous major release.

- Cisco Solutions Partner Program partner applications must be retested and updated
                                    with each new major release of Cisco Unified CM to ensure compatibility.

## Recommendations for Developers to Reduce the Number and Extent of Updates

Developers should never depend on the order of events or messages. The order of events
                                and/or messages may change.

For example,

- A feature invocation involves two or more independent transactions; the events or
                                    messages may be interleaved.

- In such cases, events related to the second transaction may precede messages related
                                    to the first.

- Or events or messages may be delayed due to situations beyond control of the
                                    interface (for example, network or transport failures).

- Applications should be able to recover from out-of-order events or messages, even
                                    when the order is required for protocol operation.

Developers must avoid unnecessary dependence on the order of elements to interpret
                                information. The order of elements within the interface event or message may change,
                                within the constraints of the protocol specification.

Developers must disregard or provide generic treatments for any unknown elements or
                                unknown values of known elements encountered. New interface events, methods, responses,
                                headers, parameters, attributes, other elements, or new values of existing elements may
                                be introduced.

Previous interface events, methods, responses, headers, parameters, attributes, and other
                                elements will remain and maintain their previous stated meaning and behavior in every
                                way possible. They will remain consistent even when defects with them need to be
                                corrected.

Applications must never be dependent on interface behavior resulting from defects. That
                                is, not consistent with the published interface specifications. Application behavior
                                might change when a defect is fixed.

Remove deprecated methods, handlers, events, responses, headers, parameters, attributes,
                                or other elements from applications as soon as possible to avoid issues when those
                                deprecated items are removed from Cisco Unified CM.

Application Developers must be aware that not all new features or new supported devices
                                will be forward compatible. New features and devices (for example, phones) may require
                                application modifications to work properly.

# New and Changed

## New and Changed
                                Information in Unified CM Release 14.

There are no changes for Unified CM Release 14.

## New and Changed
                                Information in Unified CM Release 12.5

There are no changes for Unified CM Release 12.5.

## New and Changed
                                Information in Unified CM Release 12.0

There are no changes for Unified CM Release 12.0.

## New and Changed
                                Information in Unified CM Release 11.5

There are no changes for Unified CM Release 11.5.

## New and Changed
                                Information in Unified CM Release 11.0

There are no changes for Unified CM Release 11.0.

## New and Changed
                                Information in Previous Releases of Unified CM

### New and Changed Information for Unified CM 10.0(1)

### New and Changed Information for Unified CM 9.1(1)

### New and Changed Information for Unified CM 9.0(1)

# How It Works

## Extension Mobility API Functionality

This section describes what happens when an application sends a message to the Extension
                                Mobility API service to use its functionality.

An E/M API login application submits an HTTP/HTTPS POST request containing
                                the XML request to the E/M API service URL hosted on UCM:

- https://ucmanager:8443/emservice/EMServiceServlet (secure) or

- http://ucmanager:8080/emservice/EMServiceServlet (insecure)

The request is made using the HTML form pattern (for more info, refer to http://www.w3.org/TR/html401/interact/forms.html#h-17.13.3 )
                                where the HTTP Content-Type header must be application/x-www-form-urlencoded :

```
Content-Type: application/x-www-form-urlencoded
```

and the request body contains a single control-name xml with the value equal
                                to the E/M API XML content, in URL-encoded/escaped format:

```
xml=%3cquery%3e%3cappInfo%3e%3cappID%3eemproxy%3c%2fappID%3e%3cappCertificate%3epassword%3c%2fappCertificate%3e%3c%2fappInfo%3e%3cdeviceUserQuery%3e%3cdeviceName%3eSEP010203040506%3c%2fdeviceName%3e%3c%2fdeviceUserQuery%3e%3c%2fquery%3e
```

Note the example request body above contains the URL encoded XML below:

```
<query> <appInfo> <appID> emproxy </appID> <appCertificate> password </appCertificate> </appInfo> <deviceUserQuery> <deviceName> SEP010203040506 </deviceName> </deviceUserQuery> </query>
```

The following is an example of a complete HTTP request to the E/M API service:

```
POST /emservice/EMServiceServlet HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: ucmanager:8443
Content-Length: 249
```

```
xml=%3cquery%3e%3cappInfo%3e%3cappID%3eemproxy%3c%2fappID%3e%3cappCertificate%3epassword%3c%2fappCertificate%3e%3c%2fappInfo%3e%3cdeviceUserQuery%3e%3cdeviceName%3eSEP010203040506%3c%2fdeviceName%3e%3c%2fdeviceUserQuery%3e%3c%2fquery%3e
```

The EMService checks the user credentials provided in the <appInfo> element where - appID is the user name - appCertificate is the password to ensure the corresponding UCM user has authorization to perform E/M API requests.

For example, either an individual end user with E/M feature enabled (in which case they
                                can perform E/M API operations only on their own device profiles), or a user who is a
                                member of the Standard EM Authentication Proxy Rights group (which allows
                                the user to perform E/M API operations for any user.) Typically E/M API applications
                                will use a UCM "Application User" account with proxy rights to access the
                                service, performing E/M actions on-behalf-of individual end users.

In normal operation, the E/M API service returns an HTTP 200 OK response to all valid
                                requests. If the requested E/M operation was successful, the response will contain a success XML response body:

```
<response> <success/> </response>
```

If the operation was not successful, the response body will contain an appropriate error
                                message:

```
<response> <failure> <error code= "3" > DB Query Error: Application Authentication Error: Could not authenticate" </error> </failure> </response>
```

## Character
                                Encoding Support for the <userId> element

As CUCM supports creating user IDs which include extended characters (like ' @ '),
                                E/M API requests/responses which include a <userId> element provide
                                the content of the field as UTF-8 encoded text:

Note: the <userId> element value is the only part of a
                                    request/response that will be UTF-8 encoded

```
<response> <deviceUserResults> <device name= "SEP402CF4915265" > <userID> em%40cisco.com </userID> <lastlogin> em </lastlogin> <emccDevice> no </emccDevice> </device> </deviceUserResults> </response>
```

# Authentication

## Set Up and Configuration

All necessary Cisco Extension Mobility service API components are installed with the
                                standard Unified CM installation.

To use the Cisco Extension Mobility service, create a device profile for the user who is
                                logging in and associate it to the target device. Use the following steps to configure
                                Cisco Extension Mobility service:

- Activate the service. You can do this in Unified CM by selecting the Cisco
                                    Unified Serviceability in the navigation bar of the Cisco Unified CM Admin
                                    web interface. Next, select the Tools menu and select Service
                                        Activation . You will see a list of services. Make sure the Cisco
                                    Extension Mobility Interface is checked.

- Create Extension Mobility IP phone service

- Create a user device profile

- Assign the user device profile to an end user

- Optional: Assign an application user to the standard EM authentication proxy rights
                                    user group

- Enable Cisco Extension Mobility and associate the user device profile to the target
                                    device

- Subscribe to Cisco Extension Mobility IP phone service on the target device and the
                                    device profile

- Assign a logout device profile to a target device

## Overview

To login and logout end users from devices an application user must be assigned to the
                                Standard EM Authentication Proxy Rights user group. The application user's
                                credentials are passed in the request body.

The end user can also use the Extension Mobility API (EMAPI) to login and logout of their
                                device profiles using their own credentials. End users cannot login or logout other end
                                users from devices. The end user does not need to be in a specific user group.
                                Application users must be in the Application User group.

Service Activation and User/Group management is handled in the CUCM
                                Serviceability and Administration sections of the CUCM admin interface,
                                respectively. Make sure the Extention Mobility services is started.

## Security

Cisco recommends that all EMAPI transactions be conducted over a secure session using
                                HTTPS.

Depending on the connection technology used, manually installing a Unified CM self-signed
                                certificate into a local trust store for your application may be needed.

# Request Types Reference

Developers create login applications to communicate with the Cisco Extension Mobility
                                service by sending and receiving XML messages. The XML messages sent must follow the
                                schema defined by the Message DTDs that are described in the Message Document Type Definitions .

## Login

The Login operation logs in a single user using the specified device profile.

The following example logs in userID john to device SEP003094C25B15 using the user-associated device profile UserDevProf .

### Request

```
<request> <appInfo> <appID> appid </appID> <appCertificate> apppasswd </appCertificate> </appInfo> <login> <deviceName> SEP003094C25B15 </deviceName> <userID> john </userID> <deviceProfile> UserDevProf </deviceProfile> <exclusiveDuration> <time> 60 </time> </exclusiveDuration> </login> </request>
```

### Success Response

```
<response> <success/> </response>
```

### Failure Response

```
<response> <failure> <error code= "3" > Could not authenticate 'appid' </error> </failure> </response>
```

## Logout

The following example logs out a user who is logged into device SEP003094C25B15 .

### Request

```
<request> <appInfo> <appID> appid </appID> <appCertificate> apppasswd </appCertificate> </appInfo> <logout> <deviceName> SEP003094C25B15 </deviceName> </logout> </request>
```

### Success Response

```
<response> <success/> </response>
```

### Failure Response

```
<response> <failure> <error code= "3" > Could not authenticate 'appid' </error> </failure> </response>
```

## LogoutAll

The following example logs out a user from all devices. This is useful for system
                                updates. Use of logoutAll API may lead to the generation of large number of
                                database change notifications. This could have a momentary impact on system performance.
                                The number of change notifications will be directly proportionate to the number of users
                                logged in. It is recommended to use this API outside of peak business hours.

### Request

```
<request> <appInfo> <appID> appid </appID> <appCertificate> apppasswd </appCertificate> </appInfo> <logoutAll> </logoutAll> </request>
```

### Success Response

```
<response> <success/> </response>
```

### Failure Response

```
<response> <failure> <error code= "3" > Could not authenticate 'appid' </error> </failure> </response>
```

## UserQuery

### Request

```
<query> <appInfo> <appID> appid </appID> <appCertificate> apppasswd </appCertificate> </appInfo> <deviceUserQuery> <deviceName> SEP003094C25B15 </deviceName> </deviceUserQuery> </query>
```

### Success Response

If you log in to the phone for the first time, the response is as follows:

```
<response> <deviceUserResults> <device name= "SEP003094C25B15" > <userID> one </userID> <none/> </device> </deviceUserResults> </response>
```

If you have previously logged in to the phone, the response is as follows: xml
                                    <response>
                                    <userDevicesResults>
                                    <user id="em%40cisco.com">
                                    <deviceName>SEP402CF4915265</deviceName>
                                    </user>
                                    </userDevicesResults>
                                    </response>

Note: <userId> field data is encoded in UTF-8 format, see Response Encoding .

### Failure Response

```
<response> <failure> <error code= "3" > Could not authenticate 'appid' </error> </failure> </response>
```

## DeviceQuery

The DeviceQuery operation returns all device IDs (MAC addresses) for the specified user
                                ID.

The following example finds the devices that user ID john is logged in to:

### Request

```
<query> <appInfo> <appID> appid </appID> <appCertificate> apppasswd </appCertificate> </appInfo> <userDevicesQuery> <userID> john </userID> </userDevicesQuery> </query>
```

### Success Response

```
<response> <deviceUserResults> <device name= "SEP402CF4915265" > <userID> em%40cisco.com </userID> <lastlogin> em </lastlogin> <emccDevice> no </emccDevice> </device> </deviceUserResults> </response>
```

Note: <userId> field data is encoded in UTF-8 format, see Response Encoding .

### Failure Response

```
<response> <failure> <error code= "3" > Could not authenticate 'appid' </error> </failure> </response>
```

## DeviceProfileQuery

The DeviceProfileQuery API gets information of all the device profiles associated to an
                                user.

### Request

```
<query> <appInfo> <appID> appid </appID> <appCertificate> apppasswd </appCertificate> </appInfo> <userDeviceProfileQuery> <userID> john </userID> </userDeviceProfileQuery> </query>
```

### Success Response

```
<response> <deviceProfileResults> <user id= "em%40cisco.com" > <deviceProfile> <deviceProfileName> EM-SCCP-Profile-7970 </deviceProfileName> <isDefaultDeviceProfile> f </isDefaultDeviceProfile> </deviceProfile> <deviceProfile> <deviceProfileName> EM-SCCP-7975-Profile </deviceProfileName> <isDefaultDeviceProfile> f </isDefaultDeviceProfile> </deviceProfile> </user> </deviceProfileResults> </response>
```

Note: <userId> field data is encoded in UTF-8 format, see Response Encoding .

### Failure Response

```
<response> <failure> <error code= "3" > Could not authenticate 'appid' </error> </failure> </response>
```

# Message Document Type Definitions

## Messages

An E/M API application communicates with the E/M API service by sending and receiving XML
                                messages. The XML messages must follow the schema defined by the Message DTDs.

A Message Document Type Definition (DTD) designates an XML list that specifies which
                                elements can appear in a request, query, or response document. It also specifies the
                                contents and attributes of the elements. For more information on XML DTD schema, refer
                                to http://www.w3.org/TR/2004/REC-xml11-20040204/#NT-doctypedecl .

For examples of E/M API XML requests based on the Message DTDs, see the Message Examples.

### Request DTD

The Request DTD defines the login and logout messages that your application can send to
                                the Cisco Exchange Mobility service.

<!ELEMENT request (appInfo, (login | logout | logoutAll))> <!ELEMENT appInfo (appID, (appCertificate |
                                    appEncryptedCertificate))> <!ELEMENT appID (#PCDATA)> <!ELEMENT appCertificate (#PCDATA)> <!ELEMENT appEncryptedCertificate (#PCDATA)> <!ELEMENT login (deviceName, userID, deviceProfile?, exclusiveDuration?,
                                    remoteIPAddr?, isViaHeaderSet?)> <!ELEMENT logout (deviceName, remoteIPAddr?, isViaHeaderSet?)> <!ELEMENT logoutAll (remoteIPAddr?, isViaHeaderSet?)> <!ELEMENT deviceName (#PCDATA)> <!ELEMENT userID (#PCDATA)> <!ELEMENT deviceProfile (#PCDATA)> <!ELEMENT remoteIPAddr (#PCDATA)> <!ELEMENT isViaHeaderSet (#PCDATA)> <!ELEMENT exclusiveDuration (time | indefinite)> <!ELEMENT time (#PCDATA)> <!ELEMENT indefinite EMPTY>

### Login or Logout Response DTD

Login or Logout Response DTD defines the messages that your application receives from the
                                Cisco Extension Mobility service when it sends a login or logout request message.

<!ELEMENT response (success | failure)> <!ELEMENT success EMPTY> <!ELEMENT failure (error)> <!ELEMENT error (#PCDATA)> <!ATTLIST error code NMTOKEN #REQUIRED>

### Query DTD

The Query DTD defines the Device-User and User-Devices messages that your application
                                sends the Cisco Extension Mobility service to find out which user is logged in to a
                                device or to which devices users are logged in.

<!ELEMENT query (appInfo, (deviceUserQuery | userDevicesQuery | checkUser |
                                    deviceProfileQuery))> <!ELEMENT appInfo (appID, (appCertificate |
                                    appEncryptedCertificate))> <!ELEMENT appID (#PCDATA)> <!ELEMENT appCertificate (#PCDATA)> <!ELEMENT appEncryptedCertificate (#PCDATA)> <!ELEMENT deviceUserQuery (deviceName+,remoteIPAddr?)> <!ELEMENT userDevicesQuery (userID+,remoteIPAddr?)> <!ELEMENT checkUser (userID+,remoteIPAddr?,isViaHeaderSet?)> <!ELEMENT deviceProfileQuery (userID+,remoteIPAddr?,isViaHeaderSet?)> <!ELEMENT deviceName (#PCDATA)> <!ELEMENT userID (#PCDATA)> <!ELEMENT remoteIPAddr (#PCDATA)> <!ELEMENT isViaHeaderSet (#PCDATA)>

### Query Response DTD

The Query Response DTD defines the messages that your application receives from the Cisco
                                Extension Mobility service when it sends the service a Device-User or User-Devices
                                query.

<!ELEMENT response (deviceUserResults | userDevicesResults |
                                    deviceProfileResults| failure)> <!ELEMENT deviceUserResults (device+)> <!ELEMENT userDevicesResults (user+)> <!ELEMENT deviceProfileResults (userID+)> <!ELEMENT device (userID | lastlogin | none | doesNotExist)> <!ATTLIST device name NMTOKEN #REQUIRED> <!ELEMENT user (deviceName+ | none | doesNotExist)> <!ATTLIST user id NMTOKEN #REQUIRED> <!ELEMENT userID (#PCDATA)> <!ELEMENT lastlogin (#PCDATA)> <!ELEMENT deviceName (#PCDATA)> <!ELEMENT none EMPTY> <!ELEMENT doesNotExist EMPTY> <!ELEMENT failure (errorMessage)> <!ELEMENT errorMessage (#PCDATA)>

For examples of messages see the Response Types
                                Reference section of this guide.

# Response Codes

The following table describes the response codes and messages that can be returned by the
                                Extension Mobility service. A response contains a code and a response string, formatted
                                as an XML string.

Cisco Extension Mobility Service Response Codes

| Response Code | Message | Description |
|---|---|---|
| 0 | Unknown Error | Generic error, which does not belong to the known error types. |
| 1 | Error on Parsing | Invalid XML request. The XML passed does not conform to the DTD. |
| 2 | Cannot authorize App user | Blank UserID or PIN, NULL_PARAM—Shows the user login page with
                                        error title. |
| 3 | Invalid App User | The appid supplied in the XML is not a valid user. |
| 4 | Policy Validation error | Does not conform to the policy set up for the user. For example, multiple log in
                                        not allowed. |
| 5 | Device logon disabled | Extension Mobility is not enabled on the device at the time of log out. |
| 6 | Database Error | Database is unable to process the Extension Mobility request. |
| 7 | Logout Request Error | Could not set auto-logout duration during log in. |
|  |  | Could not remove the device from the auto-logout list after log out. |
| 8 | Query type undetermined | Unrecognized Query type. The query type provided in the XML is not supported. |
| 9 | Dir. User Info Error | Could not authenticate user. This error is a for various authentication related
                                        failures. |
| 10 | User lacks app proxy rights | If a userID also is used as an appID, the userID should have proxy rights. |
| 11 | Device does not exist | Trying to perform an operation on a device that does not exist. |
| 12 | Dev. Profile not found | Trying to use a User Device Profile that does not exist. |
| 18 | Another user logged in | Another user is logged in to the device where login is being performed. |
| 19 | No user logged in | Trying to perform log out on a device where no user is currently logged in. |
| 20 | Hoteling flag error | Could not retrieve the Extension Mobility “Enabled” status for the
                                        specified device (DB error). |
| 21 | Hoteling Status error | Could not verify the login status of the specified device (DB error). |
| 22 | Device logon disabled | Extension Mobility is not enabled on the device. |
| 23 | User not found | Given user ID is invalid. |
| 25 | User logged in elsewhere | User is trying to log in to a device, but is already logged in to another device
                                        and multiple log in is not allowed. |
| 26 | Busy, please try again | The server currently is processing the maximum number of log in/log out
                                        requests. Additional requests will be accepted after pending ones are processes. |
| 27 | Change Password | Password must change on first use or password has expired. User must change
                                        password from the User page in Unified CM Administration. |
| 28 | Untrusted IP Error | Trying to log in or log out from an untrusted IP address. |
| 29 | RIS down-contact admin | The RIS Data Collector service is down. An administrator must turn it on. |
| 30 | Proxy not allowed | Log in or Log out using a proxy server is not allowed. |