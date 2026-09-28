---
doc_id: developer-cisco-com-site-user-data-services-documents-developer-guide-e0e7a01eea
source_url: https://developer.cisco.com/site/user-data-services/documents/developer-guide/
retrieved_at: 2026-09-07T14:18:30.097901+00:00
---

# Overview

The User Data Services (UDS) API is a REST-based set of operations that provide authenticated access to user resources and entities, such as user's devices, subscribed services, and speed dials, from the Unified Communications configuration database.

UDS provides Cisco clients with the ability to:

- Version number

- List of servers running UDS in the Cisco Unified CM cluster

- Supported locales and time zones

- System options for preferences and settings

- Available IP Phone services

- Perform Directory Searches for users. Filters can be applied to the user search.

- Credentials

- Speed dial information

- Destination devices for call forwarding

- Device settings

- Manage subscriptions to IP Phone Services

- Other personal settings

UDS is installed by default and activated on all Cisco Unified CM nodes.

## Cisco Product Security Overview

This product contains cryptographic features and is subject to United States and local country laws governing import, export, transfer, and use. Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute, or use encryption. Importers, exporters, distributors, and users are responsible for compliance with U.S. and local country laws. By using this product you agree to comply with applicable laws and regulations. If you are unable to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at: http://www.cisco.com/wwl/export/crypto/tool/stqrg.html . If you require further assistance please contact us by sending e-mail to export@cisco.com.

# Development Guidelines

Cisco maintains a policy of interface backward compatibility for at least one previous major release of Cisco Unified CM. Cisco still requires Cisco Solution Partner Program member applications to be retested and updated as necessary to maintain compatibility with each new major release of Cisco Unified CM.

The following practices are recommended to all developers, including those in the Cisco Solution Partner Program , to reduce the number and extent of any updates that may be necessary:

The order of events and/or messages may change. Developers should not depend on the order of events or messages. For example, where a feature invocation involves two or more independent transactions, the events or messages may be interleaved. Events related to the second transaction may precede messages related to the first. Additionally, events or messages can be delayed due to situations beyond control of the interface (for example, network or transport failures). Applications should be able to recover from out of order events or messages, even when the order is required for protocol operation.

The order of elements within the interface event or message may change, within the constraints of the protocol specification. Developers must avoid unnecessary dependence on the order of elements to interpret information.

New interface events, methods, responses, headers, parameters, attributes, other elements, or new values of existing elements may be introduced. Developers must disregard or provide generic treatments where necessary for any unknown elements or unknown values of known elements encountered.

Previous interface events, methods, responses, headers, parameters, attributes, and other elements will remain, and will maintain their previous meaning and behavior to the extent possible and consistent with the need to correct defects.

Applications must not be dependent on interface behavior resulting from defects (behavior not consistent with published interface specifications) since the behavior can change when the defect is fixed.

Use of deprecated methods, handlers, events, responses, headers, parameters, attributes, or other elements must be removed from applications as soon as possible to avoid issues when those deprecated items are removed from Cisco Unified CM.

Application Developers must be aware that not all new features and new supported devices (for example, phones) will be forward compatible. New features and devices may require application modifications to be compatible and/or to make use of the new features/devices.

# New and Changed

New and Changed Information in Cisco Unified CM Release 14

Four tags added :

URI : /cucm-uds/user/{userid}/device/{deviceid}/devicetoken

Tag added : <application> <payloadVersion> <deviceToken> <isCallKitDisabled> under <devicetoken>

UDS API : devicetoken

Example Request Body :

user request

```
<token> <pushNotifyToken> ABCD12345 </pushNotifyToken> <pushChannelType> APNS/FCM </pushChannelType> <key> key1 </key> <algorithm> algorithm </algorithm> <application> application3 </application> <payloadVersion> v2 </payloadVersion> <deviceToken> EFGH12345 </deviceToken> <isCallKitDisabled> true </isCallKitDisabled> <isMultilineSupported; true </isMultilineSupported> </token>
```

Responses :

Status Code : 200

Message : <rowsUpdated> : row(s) updated

Status Code : 404

Not Found

New and Changed Information in Cisco Unified CM Release 12.5(1)

One tag added :

URI : /cucm-uds/user/{userId}/

Tag added : <jabberProfile> under <user>

UDS API : user

user Request Format :

user request

```
GET https:­//{host}:8443/cucm-uds/user/{userId}
Content-Type: application/xml
```

user Response Format :

user response

```
<user version= "{version}" uri= "https://{host}:8443/cucm-uds/user/{userId}" > <id> {userPkid} </id> <userName> {userId} </userName> <firstName> firstName </firstName> <lastName> lastName </lastName> <selfServiceId> 1000*1 </selfServiceId> <middleName> middleName </middleName> <nickName> nickName </nickName> <displayName> displayName </displayName> <phoneNumber> 8134567 </phoneNumber> <homeNumber> 8134455 </homeNumber> <mobileNumber> 8131111 </mobileNumber> <mobileConnect> true|false </mobileConnect> <remoteDestinationLimit> 4 </remoteDestinationLimit> <userLocale uri= "https://{host}:8443/cucm-uds/installedLocales" value= "1" appliesToAllDevices= "true|false" > English, United States </userLocale> <email> someone@example.com </email> <directoryUri> someone@example.com </directoryUri> <msUri> someone@example.com </msUri> <department> department </department> <manager> manager </manager> <title> title </title> <pager> 8137777 </pager> <accountType useLdapAuth= "true|false" > ldap|local </accountType> <homeCluster enableCalendarPresence= "true|false" enableImAndPresence= "true|false" > true|false </homeCluster> <primaryExtension> <description> extensionDescription </description> <directoryNumber> 81134953 </directoryNumber> <callForwardAllDestination> <sendToVoiceMailPilotNumber> true|false </sendToVoiceMailPilotNumber> <destination> 4352134 </destination> </callForwardAllDestination> <messageWaitingVisualAlert> true|false </messageWaitingVisualAlert> <messageWaitingVisualAlertPreference appliesToAllLineAppearances= "true|false" value= "" > Use System Policy </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference appliesToAllLineAppearances= "true|false" value= "1" > Default </messageWaitingAudibleAlertPreference> <onACallRingPreference appliesToAllLineAppearances= "true|false" value= "" > Use System Default </onACallRingPreference> <notOnACallRingPreference appliesToAllLineAppearances= "true|false" value= "4" > Ring </notOnACallRingPreference> <voiceMailPilotNumber> 5555 </voiceMailPilotNumber> <label> label </label> <logMissedCalls> true|false </logMissedCalls> </primaryExtension> <callForwardAllDestination appliesToAllExtensions= "true|false" > <sendToVoiceMailPilotNumber> true|false </sendToVoiceMailPilotNumber> <destination> 43521 </destination> </callForwardAllDestination> <enableDoNotDisturb appliesToAllDevices= "true|false" > true|false </enableDoNotDisturb> <devices uri= "https://{host}:8443/cucm-uds/user/{userId}/devices" /> <credentials uri= "https://{host}:8443/cucm-uds/user/{userId}/credentials" /> <extensions uri= "https://{host}:8443/cucm-uds/user/{userId}/extensions" /> <subscribedServices uri= "https://{host}:8443/cucm-uds/user/{userId}/subscribedServices" /> <speedDials uri= "https://{host}:8443/cucm-uds/user/{userId}/speedDials" /> <serviceProfile> <uri> http://{host}:6970/SPDefault.cnf.xml </uri> </serviceProfile> <jabberProfile> <uri> https://{host}:6972/JAB_{serviceProfileID}.cnf.xml </uri> </jabberProfile> </user>
```

New and Changed Information in Cisco Unified CM Release 12.0(1)

One api was added :

UDS API : devicetoken

The devicetoken resource allows to create an device token.As an APNS customer, want to share a token with a trusted server. The Token is device centric, but it is also tied to an user . Each device can only ever have 1 user associated at a given time. When a device is created, a token entry will automatically be created for it with fkenduser set to null.

devicetoken supports PUT and DELETE methods.

Update a devicetoken format :

Update a devicetoken request

```
PUT https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/devicetoken
Accept: application/xml
Content-Type: application/xml
```

Path Parameters :

User authentication required.

Example Request Body :

Update a devicetoken example request body

```
<token> <pushNotifyToken> ABCD12345 </pushNotifyToken> <pushChannelType> channelOne </pushChannelType> <key> key1 </key> <algorithm> algorithm </algorithm> </token>
```

Error Responses :

Status Code : 200

Message : <rowsUpdated> : row(s) updated

Status Code : 404

Not Found

Delete a devicetoken format :

Delete a devicetoken request

```
DELETE https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/devicetoken/{token}
Accept: application/xml
Content-Type: application/xml
```

Path Parameters :

User authentication required.

Error Responses :

Status Code : 204

The server has completed the request and does not need to send a response body.

Status Code : 404

Not Found

One get tag added :

URI : /cucm-uds/user/{userId}/remoteDestinations

Tag added : <model> under <associatedDevice>

UDS API : remoteDestinations

remoteDestinations Request Format :

remoteDestinations request

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/remoteDestinations
Content-Type: application/xml
```

remoteDestinations Response Format :

remoteDestinations response

```
<remoteDestinations version= "12.0.0" uri= "https:­//{host}:8443/cucm-uds/user/{userId}/remoteDestinations" > <remoteDestination uri= "https:­//{host}/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}" > <id> {remoteDestinationPkid} </id> <name> RemoteDestination1 </name> <destination> 12345678901 </destination> <ringWhenExtensionDialed> true|false </ringWhenExtensionDialed> <allowTransferToMobile> true|false </allowTransferToMobile> <allowControlFromApplication> true|false </allowControlFromApplication> <associatedDevices> <associatedDevice> <usage uri= "https:­//{host}:8443/cucm-uds/options/remoteDestinationUsage" value= "0" > Single Number Reach </usage> <name> My Cell </name> <description> cell phone </description> <model> Cisco Dual Mode for Android </model> </associatedDevice> </associatedDevices> </remoteDestination> </remoteDestinations>
```

The above tag is also found under :

URI : /cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}

Tag added : <model> under <associatedDevice>

UDS API : remoteDestination

Get remoteDestinations for a device request

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}
Content-Type: application/xml
```

Path Parameters :

User authentication required.

Get remoteDestination for a Device Response Format :

get remoteDestinations for a device request

```
<remoteDestination version= "12.0.0" uri= "https://{host}/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}" > <id> {remoteDestinationPkid} </id> <name> Adrienne's Cell </name> <destination> 5555555 </destination> <ringWhenExtensionDialed> true|false </ringWhenExtensionDialed> <allowTransferToMobile> true|false </allowTransferToMobile> <allowControlFromApplication> true|false </allowControlFromApplication> <associatedDevices> <associatedDevice> <name> TestRDP1 </name> <usage uri= "https://{host}/cucm-uds/options/remoteDestinationUsage" value= "0" > <option value= "0" > Single Number Reach </option> <option value= "1" > Application Control </option> <option value= "2" > Dual Mode Mobile </option> </usage> <description> This is a test remote destination profile </description> <associatedExtensions> <associatedExtension enable= "false" > 7778 </associatedExtension> </associatedExtensions> <model> Cisco Dual Mode for Android </model> </associatedDevice> </associatedDevices> <advancedSettings> <delayBeforeRingTimer> 4.0 </delayBeforeRingTimer> <voiceMailAvoidanceSettings> <answerTooSoonTimer> 1.5 </answerTooSoonTimer> <voiceMailAvoidancePolicy uri= "https://{host}/cucm-uds/options/voiceMailAvoidancePolicy" value= "0" > Use System Default </voiceMailAvoidancePolicy> </voiceMailAvoidanceSettings> <answerTooLateTimer> 19.0 </answerTooLateTimer> </advancedSettings> </remoteDestination>
```

New and Changed Information in Cisco Unified CM Release 11.5(1)

users includes displayname as a search parameter in a users search. Filter the user search by the displayname starting with the search string. For example, https://{host}:8443/cucm-uds/users?displayname=Bill .

users includes displayname as a filter in search by name. For example, https://{host}:8443/cucm-uds/users?name=Jon . Note:

- When the search criteria contains one space, the rules for searching for the user name are: Assuming a search for "x y" (first starts with x AND last starts with y) OR (last starts with x AND first starts with y) OR (last starts with "x y") OR (first starts with "x y") OR (displayname starts with “x y”).

- When the search criteria does not contain a space, then it means displayname starts with x.

user API provides the option to update displayname with a PUT request. Refer to the example in the right hand panel.

Update displayname with a PUT request

```
<user> <displayName> Bill </displayName> </user>
```

- The version API is modified to return the userResourceAuthEnabled value indicating whether authentication is needed for contact search. For example, refer to the sample in the right hand panel.

version API returns userResourceAuthEnabled value

```
<?xml version="1.0" encoding="UTF-8"?> <versionInformation uri= "https://{host}/cucm-uds/version" version= "10.0.0" > <version> 11.5.1 </version> <capabilities> <usersResourceAuthEnabled> true </usersResourceAuthEnabled> </capabilities> </versionInformation>
```

New and Changed Information in Cisco Unified CM Release 11.0(1)

conferencing resource added, including GET and PUT operations.  This user-level resource allows users to access and update their Conference Now access codes.

user and users resources now return the displayName attribute.

groups resource added.  For Unified CM systems integrated with Microsoft Active Directory (AD), this resource allows the user to query the list of AD groups available.

New and Changed Information in Cisco Unified CM Release 10.5(2)

- GET operation support added to the Credentials resource, allowing a user to obtain login information, such as successful time and IP,  unsuccessful time and IP, and login failures.

New and Changed Information in Cisco Unified CM Release 10.5(1)

Cross-Origin Resource Sharing (CORS) support added. See the Cross-Origin Resource Sharing section for more information.

Single Sign-On (SSO) support added. See the Authentication section for more information.

Users resource now includes the new numeric value return field selfServiceId .

Devices and Device resources which return description now include a new field, source= , which can be set to either user or admin .

New and Changed Information in Cisco Unified CM Release 10.0(1)

The User Data Services are a new feature available in Unified Communications Manager Release 10.0.

# Example Use Cases

UDS is primarily useful for integrating personal CUCM settings access into user-facing applications and web pages.  Some examples include:

Directory search - find other users both local and remote

- search using first, last, name, number, numberLast, email, uri (directoryUri or msUri)

Manage preferences and settings - configure a user's speed dials, mobility and remote destinations, call forward all, and do not disturb

- user settings can be queried from any server in any cluster in your network

Create collaboration widgets - allow users to update their UC feature status and message waiting indicator (MWI) status

- users can manage their settings in a user-centric way

In this mock-up of a collaboration widget, you can see that this application allows a user to manage their own personal settings, enable and disable features, and search users by name and number.

# Cross-Origin Resource Sharing

What is CORS?

For security reasons, web browsers by default prevent Javascript served by one origin (web site) from accessing data served by another origin, where an origin is a combination of scheme (an example of a scheme is HTTPS), hostname, and port.

For example, Javascript on a page served from https://app.example.com cannot access data retrieved via XMLHttpRequest from https://ucmanager.example.com (for example, to make a UDS request.)

To allow these types of requests securely, the Cross-Origin Resource Sharing (CORS) standard was developed: http://www.w3.org/TR/cors . CORS is supported in modern browsers.

CORS involves the use of special HTTP request headers and 'pre-flight' OPTIONS requests, and is generally handled transparently by browsers.  However, it is necessary to configure the web server (in this case Cisco Unified CM) to allow Cross-Origin requests, on an origin-by-origin basis.

UCM supports configuration of CORS applications via the System/Cross-Origin Resource Sharing (CORS) menu:

For each browser-based application web site using an Unified CM CORS-supported API, an entry in the CORS configuration area will need to be created. Include the protocol scheme (such as HTTPS), domain, and port (if not the default port :80 or :443), for example https://app.example.com .

# Hello World

To get started with using UDS, lets look at an API request for a simple example.

An API request consists of a HTTP method and a URI. The HTTP method designates the type of activity to perform. Operations use standard HTTP methods to retrieve, update, create, and delete resources or data. The URI identifies the resource or resources that the request targets, and can include various parameters to further refine the operation.

Most API requests require that a HTTP Accept header be included. In addition, PUT and POST requests require a HTTP Content-Type header. The Accept and Content-Type header can specify xml.

To invoke an API operation, you send a HTTP request from any client that supports the creation of such a request to a Cisco Unified CM server.

Example Scenario: To get a user's settings and preferences.

For this task, we need to make one REST API request to the server. Visit Explore the UDS APIs to see exactly how this is done.

To get the list of servers in XML format, make a HTTP GET request with the Accept header set to "application/xml".
                            Refer to the Request sample code in the right-hand panel.

Request

```
GET https:­//{host}:8443/cucm-uds/user/{userId}
Accept: application/xml
```

You'll receive a Response in XML format similar to the example in the right-hand panel.

Response

```
<user version= "{version}" uri= "https:­//{host}:8443/cucm-uds/user/{userId}" > <id> {userPkid} </id> <userName> {userId} </userName> <firstName> firstName </firstName> <lastName> lastName </lastName> <middleName> middleName </middleName> <nickName> nickName </nickName> <phoneNumber> 8134567 </phoneNumber> <homeNumber> 8134455 </homeNumber> <mobileNumber> 8131111 </mobileNumber> <mobileConnect> true|false </mobileConnect> <userLocale uri= "https:­//{host}:8443/cucm-uds/installedLocales" value= "0" appliesToAllDevices= "true|false" > English, United States </userLocale> <email> someone@example.com </email> <directoryUri> someone@example.com </directoryUri> <msUri> someone@example.com </msUri> <department> department </department> <manager> manager </manager> <title> title </title> <pager> 8137777 </pager> <primaryExtension uri= "https:­//{host}:8443/cucm-uds/user/{userId}/userExtension/{extensionPkid}" > <description> extensionDescription </description> <directoryNumber> 81134953 </directoryNumber> <callForwardAllDestination> <sendToVoiceMailPilotNumber> true|false </sendToVoiceMailPilotNumber> <destination> 4352134 </destination> </callForwardAllDestination> <messageWaitingVisualAlert> true|false </messageWaitingVisualAlert> <messageWaitingVisualAlertPreference appliesToAllLineAppearances= "true|false" value= "" > Use System Default </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference appliesToAllLineAppearances= "true|false" value= "1" > On </messageWaitingAudibleAlertPreference> <onACallRingPreference appliesToAllLineAppearances= "true|false" value= "0" > Use System Default </onACallRingPreference> <notOnACallRingPreference appliesToAllLineAppearances= "true|false" value= "0" > Use System Default </notOnACallRingPrefence> <voiceMailPilotNumber> 5555 </voiceMailPilotNumber> <label appliesToAllLineAppearances= "true|false" > label </label> <logMissedCalls appliesToAllLineAppearances= "true|false" > true|false </logMissedCalls> </primaryExtension> <accountType useLdapAuth= "true|false" > ldap|local </accountType> <homeCluster enableCalendarPresence= "true|false" enableImAndPresence= "true|false" > true|false </homeCluster> <devices uri= "https:­//{host}:8443/cucm-uds/user/{userId}/devices" /> <credentials uri= "https:­//{host}:8443/cucm-uds/user/{userId}/credentials" /> <userExtensions uri= "https:­//{host}:8443/cucm-uds/user/{userId}/userExtensions" /> <enableDoNotDisturb appliesToAllDevices= "true|false" > true|false </enableDoNotDisturb> <callForwardAllDestination appliesToAllExtensions= "true|false" > <sendToVoiceMailPilotNumber> true|false </sendToVoiceMailPilotNumber> <destination> 43521 </destination> </callForwardAllDestination> <speedDials uri= "https:­//{host}:8443/cucm-uds/user/{userId}/speedDials" /> <serviceProfile uri= "http:­//{host}:6970/SPDefault.cnf.xml" /> </user>
```

# API Reference

See Cisco User Data Services (UDS) API Reference .

# Authentication

See UDS Authentication .

# Response and Error Codes

HTTP status codes are returned by the API with the responses.

Success Status Codes

Error Status Codes

# Troubleshooting

If you have questions or need support, check the UDS Developer Forums and the UDS FAQs .

The following are some basic troubleshooting hints when using UDS.

Cannot connect to the server or the connection times out .

To safeguard user credentials and information, UDS requires a secure link when conducting transactions. Verify the client application is setting up an SSL session properly.

HTTP 401 error occurs when attempting to access a UDS resource.

Certain UDS resources require authentication credentials. Information on the authentication process and which resources require authorization can be found in the Authentication section of this Developer Guide. Confirm that the end user's name and password are correct. Check that the client is producing an Authorization header with the proper credentials.

HTTP 404 error occurs when attempting to access a UDS resource.

Check that the URL is not misspelled or confirm that the resource exists in the API Reference .

HTTP 405 or 409 error occurs when attempting to access a UDS resource.

An incorrect HTTP method is being used in the request. Consult the API Reference as to the method(s) that the resource supports.

HTTP 415 error occurs when attempting to access a UDS resource .

The parameters in the resource link (GET method) or request body (POST, PUT, and DELETE methods) are missing or invalid. Check the API Reference to determine what parameters and values the resource requires.

HTTP 503 error occurs when attempting to access a UDS resource.

The service is experiencing a heavy load. Wait and try again later.

To further troubleshoot the HTTP transactions that occur between your application and UDS, we suggest using traffic monitoring tools.

If you need additional help with UDS, you can open a developer support case .

## Enable and Gather UDS Logs

This article explains how to enable and gather UDS logs from Cisco Unified CM. UDS logs are useful for debugging service issues. They provide details on exactly what services were invoked, when they were invoked, and what they actually did, including any run time errors.

The system writes the UDS trace logs to the Tomcat logs directory accessible via RTMT. File names are cucm-uds####.log, where # represents a number from 0000 (zero) to the maximum number of files allowed. The maximum file size is 1 MB by default. The maximum number of stored files defaults to 10. You can change these settings through the Serviceability windows.

#### Enabling UDS Logs from the Serviceability Window

From the Cisco Unified CM Administration window, choose Navigation > Cisco Unified Serviceability .

Choose Trace > Configuration .

From the Servers selection box, select the server and click Go .

From the Service Group box, select CM Services and click Go .

From the Services box, select the Cisco User Data Services and click Go .

If you want the trace to apply to all Cisco Unified CM servers in the cluster, select the Apply to All Nodes check box.

Check the Trace On check box.

In the Debug Trace Level box, select Debug .

Check the Enable All Trace check box.

NOTE: When you change either the Maximum No. of Files or the Maximum File Size settings in the Trace Configuration window, the system deletes all service log files except for the current file, if the service is running. If the service has not been activated, the system deletes the files immediately after you activate the service. Before you change the Maximum No. of Files setting or the Maximum File Size setting, download and save the service log files to another server if you want to keep a record of the log files. To perform this task, use Trace and Log Central in RTMT.

#### Gathering UDS Logs through Real-time Monitoring Tool (RTMT)

To use this tool, you must download it from Cisco Unified CM.

Log into Cisco Unified CM Administration.

Click Application > Plugins .

Search and find the Cisco Unified Real-Time Monitoring Tool.

Click Download adjacent to:

- Cisco Unified Real-Time Monitoring Tool-Linux, if your OS is Linux

- Cisco Unified Real-Time Monitoring Tool-Windows, if your OS is Windows

Install the RTMT tool.

Start the RTMT tool.

In the Host IP Address box, enter the IP address of the Cisco Unified CM server you want to monitor.

In the User Name box, enter the user name for the Cisco Unified CM server you want to monitor

In the Password box, enter the password for the Cisco Unified CM server you want to monitor

To collect logs and traces, go to System , click Trace & Log Central , and double-click Collect Files .

Select the Cisco CallManager check boxes in both columns.

Select the Cisco User Data Services check boxes in both columns.

Click Next.

Click Next.

On the Collect File Options screen, select an Absolute Range approximately 30 minutes before and after your test run.

Click Finish .

For convenience, zip the resulting files.

If you need additional support you can open a developer support case .

# FAQs

General

What type of applications can be integrated with the UDS API resources?

What security measures do the UDS APIs provide?

Why are some of the API names nearly identical? 'Devices' versus 'device' and 'users' versus 'user', for example?

Does the UDS API support XML and JSON requests and responses?

Error Responses

The client receives a 401 response when it attempts to access a UDS resource.

The client receives a 409 response when it attempts to add a service or a device.

The client receives a 415 response when it attempts to modify an item.

General

What type of applications can be integrated with the UDS API resources?

Because UDS is implemented via REST transactions over HTTP, any HTTP-savvy application can potentially access the API. A suitable application could be a native PC program, a mobile OS application with network/HTTP request capability, or a browser-based web application using Javascript.

What security measures do the UDS APIs provide?

UDS resources that manage user-specific information and device configuration require authentication prior to their use. UDS resources that provide general information, such as UDS server features, time zone, and supported locales, do not require authentication. Note that the restricted resources use HTTP Basic authentication, where the username and password information are sent essentially in the clear (base64 encoded). Cisco strongly recommends that all UDS transactions be performed through a secure session via HTTPS and/or within a secure intranet.

Why are some of the API names nearly identical? Devices versus device and users versus user, for example?

In general, a plural UDS resource name (ends with a s character) provides general information. This information can then be used with the singular API name to drill down for more detailed information. For example, a user might access the devices resource to obtain a list of the devices that can be managed. Then use the information on the list, along with the device resource, to manage the settings and configuration of a specific device.

Does the UDS API support XML and JSON requests and responses?

The Cisco UDS API supports only the XML format for all requests and responses.

Error Responses

The client receives a 401 response when it attempts to access a UDS resource.

An attempt was made to access a restricted resource with missing or  invalid credentials. The resource might have been accessed by accident, or an invalid username and password may have been provided. The client should obtain the correct credentials and retry the request.

The client receives a 409 response when it attempts to add a service or a device.

An attempt was made to add an information item (for example, a service or device) that already exists in the UDS system. This message is possible when the POST method is used with a resource. Note, to update existing items in the UDS system, the PUT method must be used.

The client receives a 415 response when it attempts to modify an item.

There was an error in one of the parameters in the request body. Correct the parameter information and try again.

Please visit UDS FAQs online for the latest updates.

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to update. |
| {devicePkid} | The ID of the specific device requiring the update. |

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to update. |
| {devicePkid} | The ID of the specific device requiring the update. |
| {token} | The ID of spcific token to be deleted. |

| Parameter | Description |
|---|---|
| {userId} | The user whose remote destination device information you want to retrieve. |
| {remoteDestinationPkid} | The ID of the remote destination device. |

| Function | Response |
|---|---|
| GET | Requests return a 200 response if the resource is successfully retrieved. |
| POST | Requests return a 201 response if successful. Certain resources return a response that can be used to confirm that the information was added. |
| PUT | Requests return a 200 response if successful. Certain resources return a response that can be used to confirm that the information was added. |
| DELETE | Requests return a 204 response if successful. |

| Function | Response |
|---|---|
| 401 | Unauthorized Access. The client must submit authorization credentials before the request can be carried out. |
| 404 | Resource does not exist. This error occurs when the URL used in the request does not match a UDS resource. |
| 405 | The resource does not support this HTTP method. The common cause of this error is when a POST or a PUT method is attempted with a resource that only supports a GET method. |
| 409 | A conflict has occurred when attempting to carry out the request. Once source of this error is when a POST method attempts to add information to the database that already exists. |
| 500 | An internal exception has occurred. |
| 503 | The server is temporarily overloaded. Please wait and try your request later. |