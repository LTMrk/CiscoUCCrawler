---
doc_id: developer-cisco-com-docs-user-data-services-67db9977e9
source_url: https://developer.cisco.com/docs/user-data-services/
retrieved_at: 2026-08-24T22:12:49.438446+00:00
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

A summary of U.S. laws governing Cisco cryptographic products may be found at: http://www.cisco.com/wwl/export/crypto/tool/stqrg.html . If you require further assistance please contact us by sending e-mail to export@cisco.com .

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

## New and Changed Information in Cisco Unified CM Release 12.5(1)

Resources modified :

Resource : User

URL : /cucm-uds/user/{userId}/

Tag added : <jabberProfile> under <user>

Example:*

xml

```
< user > ... < jabberProfile > < uri > https://{host}:6972/JAB_{serviceProfileID}.cnf.xml </ uri > </ jabberProfile > ... </ user >
```

## New and Changed Information in Cisco Unified CM Release 12.0(1)

Resources added :

Resource : Device Token

URL : /cucm-uds/user/devicetoken

Methods : PUT / DELETE

Example:*

xml

```
< token > < pushNotifyToken > ABCD12345 </ pushNotifyToken > < pushChannelType > channelOne </ pushChannelType > < key > key1 </ key > < algorithm > algorithm </ algorithm > </ token >
```

Resources modified :

Resource : User Remote Destination

URL : /cucm-uds/user/{userID}/remoteDestination/{remoteDestinationId}

Tag added : <model> under <associatedDevice>

Example:*

xml

```
< remoteDestination uri = " https:­//{host}/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid} " > ... < associatedDevices > < associatedDevice > ... < model > Cisco Dual Mode for Android </ model > </ associatedDevice > </ associatedDevices > </ remoteDestination >
```

Note: this change is also present for /cucm-uds/user/{userId}/remoteDestinations

## New and Changed Information in Cisco Unified CM Release 11.5(1)

Resources modified :

Resource : User

URL : /cucm-uds/user/{userId}

Method : PUT

Tag added : <displayName> under <user>

Example:*

xml

```
< user > ... < displayName > Bill </ displayName > ... </ user >
```

Resource : Users

URL : /cucm-uds/users

Method : GET

Parameter added : displayName

Example:*

Code Snippet

```
GET https://{host}:8443/cucm-uds/users?displayname=Bill
```

Resource : Version

URL : /cucm-uds/version

Tag added : <userResourceEnabled>

Example:*

xml

```
< versionInformation uri = " https://{host}/cucm-uds/version " version = " 10.0.0 " > < version > 11.5.1 </ version > < capabilities > < usersResourceAuthEnabled > true </ usersResourceAuthEnabled > </ capabilities > </ versionInformation >
```

## New and Changed Information in Cisco Unified CM Release 11.0(1)

Resrouces added :

Resource : User Conferencing

URL : /cucm-uds/user/{userId}/conferencing

Methods : GET / PUT

Example:*

xml

```
< conferencing uri = " https://{hostname}/cucm-uds/user/{userid}/conferencing " version = " 11.0.0 " > < conferenceNow > < enabled > true </ enabled > < accessCode > 1234 </ accessCode > </ conferenceNow > </ conferencing >
```

Resource : Groups

URL : /cucm-uds/groups

Methods : GET

Parameters : name

Example:*

xml

```
< groups uri = " {host}:8443/cucm-uds/groups " version = " 11.0.0 " returnedCount = " 5 " > < group > < groupName > Phoenix1 </ groupName > < distinguishedName > CN=Phoenix1,OU=dhanush,DC=adtest,DC=com </ distinguishedName > < groupType > Active LDAP Synchronized Group </ groupType > </ group > </ groups >
```

Resrouces modified :

Resource : User

URL : /cucm-uds/user/{userId}

Method : GET

Tag added : <displayName> under <user>

Example:*

xml

```
< user > ... < displayName > Bill </ displayName > ... </ user >
```

Note: this change is also present for /cucm-uds/users

## New and Changed Information in Cisco Unified CM Release 10.5(2)

Resources modified : User Credentials

URL : /cucm-uds/user/{userId}/credentials

Method added : GET

Example:*

xml

```
< credentials uri = " https://{hostname}/cucm-uds/user/{userid}/conferencing " version = " 10.5.2 " > < credential > < loginDetails > < lastSuccessfulLogin > 2015-04-17T19:36:42.000Z </ lastSuccessfulLogin > < lastSuccessfulLoginIp > 172.30.223.139 </ lastSuccessfulLoginIp > </ loginDetails > < loginFailures > 0 </ loginFailures > </ credential > </ credentials >
```

## New and Changed Information in Cisco Unified CM Release 10.5(1)

Cross-Origin Resource Sharing (CORS) support added. See the Cross-Origin Resource Sharing section for more information.

Single Sign-On (SSO) support added. See the Authentication section for more information.

Resources modified :

Resource : Users

URL : /cucm-uds/users

Method : GET

Tag added : <selfServiceId>

Example* :

xml

```
< user uri = " https://ds-ucm1251.cisco.com:8443/cucm-uds/user/dstaudt " version = " 10.5.1 " > ... < selfServiceId > 234523 </ selfServiceId > ... </ user >
```

Resource : User Device

URL : /cucm-uds/user/{userId}/device/{deviceId}

Method : GET

Attribute added : source in the <description> tag

Example:*

xml

```
< device uri = " https://ds-ucm1251.cisco.com:8443/cucm-uds/user/dstaudt/device/0351e852-641e-fc47-467d-234b927f9a3b " version = " 12.5.1 " hasPrimaryNumber = " false " > ... < description editable = " true " source = " admin " > SEP098234098234 </ description > ... </ device >
```

Note: this change is also present for /cucm-uds/user/{userId}/devices

## New and Changed Information in Cisco Unified CM Release 10.0(1)

- The User Data Services are a new feature available in Unified Communications Manager Release 10.0.

# Example Use Cases

UDS is primarily useful for integrating personal CUCM settings access into user-facing applications and web pages.  Some examples include:

Directory search - find other users both local and remote

- search using first, last, name, number, numberLast, email, uri (directoryUri or msUri)

Manage preferences and settings - configure a user's speed dials, mobility and remote destinations, call forward all, and do not disturb

- user settings can be queried from any server in any cluster in your network

Create collaboration widgets - allow users to update their UC feature status and message waiting indicator (MWI) status

- users can manage their settings in a user-centric way

# Cross-Origin Resource Sharing

What is CORS?

For security reasons, web browsers by default prevent Javascript served by one origin (web site) from accessing data served by another origin, where an origin is a combination of scheme (an example of a scheme is HTTPS), hostname, and port.

For example, Javascript on a page served from https://app.example.com cannot access data retrieved via XMLHttpRequest from https://ucmanager.example.com (for example, to make a UDS request.)

To allow these types of requests securely, the Cross-Origin Resource Sharing (CORS) standard was developed: http://www.w3.org/TR/cors . CORS is supported in all modern browsers.

CORS involves the use of special HTTP request headers and 'pre-flight' OPTIONS requests, and is generally handled transparently by browsers.  However, it is necessary to configure the web server (in this case Cisco Unified CM) to allow Cross-Origin requests, on an origin-by-origin basis.

UCM supports configuration of CORS applications via the System/Cross-Origin Resource Sharing (CORS) menu:

For each browser-based application using a Unified CM CORS-supported API, an entry in the CORS configuration area will need to be created. Include the protocol scheme (such as HTTPS), domain name, and port (if not the default port :80 or :443), for example https://app.example.com:8443 .

# Hello World

To get started with using UDS, lets look at an API request for a simple example.

An API request consists of a HTTP method and a URI. The HTTP method designates the type of activity to perform. Operations use standard HTTP methods to retrieve, update, create, and delete resources or data. The URI identifies the resource or resources that the request targets, and can include various parameters to further refine the operation.

Most API requests require that a HTTP Accept header be included. In addition, PUT and POST requests require a HTTP Content-Type header. The Accept and Content-Type header can specify xml.

To invoke an API operation, you send a HTTP request from any client that supports the creation of such a request to a Cisco Unified CM server.

Example Scenario: To get a user's settings and preferences.

For this task, we need to make one REST API request to the server. Visit Explore the UDS APIs to see exactly how this is done.

To get the list of servers in XML format, make a HTTP GET request with the Accept header set to "application/xml".

Refer to the Request sample code in the right-hand panel.

Example request:

xml

```
GET https:­//{host}:8443/cucm-uds/user/{userId}
Accept: application/xml
```

You'll receive a Response in XML format similar to the example in the right-hand panel.

Example response:

xml

```
< user version = " {version} " uri = " https:­//{host}:8443/cucm-uds/user/{userId} " > < id > {userPkid} </ id > < userName > {userId} </ userName > < firstName > firstName </ firstName > < lastName > lastName </ lastName > < middleName > middleName </ middleName > < nickName > nickName </ nickName > < phoneNumber > 8134567 </ phoneNumber > < homeNumber > 8134455 </ homeNumber > < mobileNumber > 8131111 </ mobileNumber > < mobileConnect > true|false </ mobileConnect > < userLocale uri = " https:­//{host}:8443/cucm-uds/installedLocales " value = " 0 " appliesToAllDevices = " true|false " > English, United States </ userLocale > < email > someone@example.com </ email > < directoryUri > someone@example.com </ directoryUri > < msUri > someone@example.com </ msUri > < department > department </ department > < manager > manager </ manager > < title > title </ title > < pager > 8137777 </ pager > < primaryExtension uri = " https:­//{host}:8443/cucm-uds/user/{userId}/userExtension/{extensionPkid} " > < description > extensionDescription </ description > < directoryNumber > 81134953 </ directoryNumber > < callForwardAllDestination > < sendToVoiceMailPilotNumber > true|false </ sendToVoiceMailPilotNumber > < destination > 4352134 </ destination > </ callForwardAllDestination > < messageWaitingVisualAlert > true|false </ messageWaitingVisualAlert > < messageWaitingVisualAlertPreference appliesToAllLineAppearances = " true|false " value = " " > Use System Default </ messageWaitingVisualAlertPreference > < messageWaitingAudibleAlertPreference appliesToAllLineAppearances = " true|false " value = " 1 " > On </ messageWaitingAudibleAlertPreference > < onACallRingPreference appliesToAllLineAppearances = " true|false " value = " 0 " > Use System Default </ onACallRingPreference > < notOnACallRingPreference appliesToAllLineAppearances = " true|false " value = " 0 " > Use System Default </ notOnACallRingPrefence > < voiceMailPilotNumber > 5555 </ voiceMailPilotNumber > < label appliesToAllLineAppearances = " true|false " > label </ label > < logMissedCalls appliesToAllLineAppearances = " true|false " > true|false </ logMissedCalls > </ primaryExtension > < accountType useLdapAuth = " true|false " > ldap|local </ accountType > < homeCluster enableCalendarPresence = " true|false " enableImAndPresence = " true|false " > true|false </ homeCluster > < devices uri = " https:­//{host}:8443/cucm-uds/user/{userId}/devices " /> < credentials uri = " https:­//{host}:8443/cucm-uds/user/{userId}/credentials " /> < userExtensions uri = " https:­//{host}:8443/cucm-uds/user/{userId}/userExtensions " /> < enableDoNotDisturb appliesToAllDevices = " true|false " > true|false </ enableDoNotDisturb > < callForwardAllDestination appliesToAllExtensions = " true|false " > < sendToVoiceMailPilotNumber > true|false </ sendToVoiceMailPilotNumber > < destination > 43521 </ destination > </ callForwardAllDestination > < speedDials uri = " https:­//{host}:8443/cucm-uds/user/{userId}/speedDials " /> < serviceProfile uri = " http:­//{host}:6970/SPDefault.cnf.xml " /> </ user >
```

# Authentication

See UDS Authentication .

# Response and Error Codes

HTTP status codes are returned by the API with the responses, and provide ifnormation on the success or failure category.

Success Status Codes:

Error Status Codes

# Troubleshooting

## Checklist

The following are some basic troubleshooting hints when using UDS:

Cannot connect to the server or the connection times out

To safeguard user credentials and information, UDS requires a secure link when conducting transactions. Verify the client application is connecting to UDS via HTTPS and that it is not using outdated crypto protocols or algorithms.

HTTP 401 error occurs when attempting to access a UDS resource

Most UDS resources require authentication. Information on the authentication process and which resources require authorization can be found in the Authentication section of this Developer Guide. Confirm that the end user's name and password are correct. Check that the UDS HTTP request is including an Authorization header with the proper Base64 encoded username/password or Bearer access token.

Users with accounts that are locked/expired or 'must change password/pin on next login' may also fail to authenticate.

HTTP 404 error occurs when attempting to access a UDS resource

Check that the resource URL is not misspelled in the API Reference.  For resrouces that retrieve specific objects, ensure that the object ID is included in the URL, and that the specific object Id exists in the system.

HTTP 405 or 409 error occurs when attempting to access a UDS resource

An incorrect HTTP method is being used in the request (for example, attempting a PUT on a resource that only supports GET ). Consult the API Reference as to the method(s) that the resource supports.

HTTP 415 error occurs when attempting to access a UDS resource

Required URL parameters in the resource link ( GET method) or required tags in the request body ( POST , PUT ) are missing or invalid. Check the to determine what parameters and values the resource requires.

HTTP 503 error occurs when attempting to access a UDS resource

The service is experiencing a heavy load. Wait and try again later.

To further troubleshoot the HTTP transactions that occur between your application and UDS, we suggest using HTTP message monitoring tools such as Fidder or mitmproxy .

## Getting help

If you have questions about using UDS, check the UDS community forums and the FAQs .

For help and support, please explore the DevNet Developer Support options.

## Enabling and gathering UDS logs

This article explains how to enable and gather UDS logs from Cisco Unified CM. UDS logs are useful for debugging service issues. They provide details on exactly what services were invoked, when they were invoked, and what they actually did, including any run time errors.  Logs may be requested by DevNet Developer Support in the course of working with you to resolve a support ticket.

The system writes the UDS trace logs to the Tomcat logs directory accessible via RTMT. File names are of the form cucm-uds####.log , where #### represents a number from 0000 to the maximum number of files allowed. The maximum file size is 1 MB by default. The maximum number of stored files defaults to 10. You can change these settings through the CUCM Serviceability admin UI.

### Enabling UDS Logs from the Cisco Unified Serviceability pages

From the Cisco Unified CM Administration page, choose Navigation > Cisco Unified Serviceability .

Choose Trace > Configuration .

From the Servers selection box, select the server and click Go .

From the Service Group box, select CM Services and click Go .

From the Services box, select the Cisco User Data Services and click Go .

If you want the trace to apply to all Cisco Unified CM servers in the cluster, select the Apply to All Nodes check box.

Check the Trace On check box.

In the Debug Trace Level box, select Debug .

Check the Enable All Trace check box.

When you change either the Maximum No. of Files or the Maximum File Size settings in the Trace Configuration window, the system deletes all service log files except for the current file, if the service is running. If the service has not been activated, the system deletes the files immediately after you activate the service.

Before you change the Maximum No. of Files setting or the Maximum File Size setting, download and save the service log files to another server if you want to keep a record of the log files. To perform this task, use Trace and Log Central in RTMT.

### Gathering UDS Logs through Real-time Monitoring Tool (RTMT)

To use this tool, you must download it from Cisco Unified CM host:

Log into Cisco Unified CM Administration.

Click Application > Plugins .

Search and find the Cisco Unified Real-Time Monitoring Tool .

Click Download link for the RTMT version for your OS (Windows/Linux)

See this discussion for hints on using RTMT with Mac Os

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

# FAQs

What type of applications can be integrated with the UDS API resources?

What security measures do the UDS APIs provide?

Why are some of the API names nearly identical? 'Devices' versus 'device' and 'users' versus 'user', for example?

Does the UDS API support XML and JSON requests and responses?

What type of applications can be integrated with the UDS API resources?

Because UDS is implemented via REST transactions over HTTP, any HTTP-savvy application can potentially access the API. A suitable application could be a native PC program, a mobile OS application with network/HTTP request capability, or a browser-based web application using Javascript.

What security measures do the UDS APIs provide?

UDS resources that manage user-specific information and device configuration require authentication prior to their use. UDS resources that provide general information, such as UDS server features, time zone, and supported locales, do not require authentication. Note that the restricted resources use HTTP Basic authentication, where the username and password information are sent essentially in the clear (base64 encoded). Cisco strongly recommends that all UDS transactions be performed through a secure session via HTTPS.

Why are some of the API names nearly identical? Devices versus device and users versus user, for example?

In general, a plural UDS resource name (ends with a s character) provides general information. This information can then be used with the singular API name to drill down for more detailed information.

For example, a user might access the devices resource to obtain a list of the devices that can be managed. Then use the information on the list, along with the device resource, to manage the settings and configuration of a specific device.

Does the UDS API support XML and JSON requests and responses?

The Cisco UDS API supports only XML format for all requests and responses.

Next

| Method | Response |
|---|---|
| GET/POST/PUT | Requests return a 200 response if the resource is successfully retrieved.  This response includes a body. |
| POST/PUT | Requests return a 201 response if successful. No body is returned. |
| DELETE | Requests return a 204 response if successful. |

| Function | Response |
|---|---|
| 401 | Unauthorized Access. The client must submit authorization credentials before the request can be carried out.  Locked/expired or 'must change password/pin on new login' accounts may also fail with this code. |
| 404 | Resource does not exist. This error occurs when the URL used in the request does not match a UDS resource. |
| 405 | The resource does not support this HTTP method. The common cause of this error is when a POST or a PUT method is attempted with a resource that only supports a GET method. |
| 409 | A conflict has occurred when attempting to carry out the request. Once source of this error is when a POST method attempts to add information to the database that already exists, for example a duplicate object. |
| 500 | An internal exception has occurred. |
| 503 | The server is temporarily overloaded. Please wait and try your request later. |