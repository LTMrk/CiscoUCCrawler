---
doc_id: developer-cisco-com-site-user-data-services-develop-and-test-api-reference-c957c24931
source_url: https://developer.cisco.com/site/user-data-services/develop-and-test/api-reference/
retrieved_at: 2026-09-07T14:10:01.061843+00:00
---

# Overview

The User Data Services (UDS) API is a REST-based set of operations that provide authenticated access to user resources and entities, such as user’s devices, subscribed services, speed dials, and much more from the Cisco Unified Communications Manager (Unified CM) configuration database.

To learn more about UDS, visit What is UDS?

## Naming Conventions

Resource names represent the object

- User

- Device

- Extension

Singular resources mean exactly one.

- A single user: resource = user

- A single device: resource = device

- A single extension: resource = extension

Plural resources mean more than one.

- A list of users: resource = users

- A list of devices: resource = devices

- A list of extensions: resource = extensions

## Policy Behavior

When using the UDS APIs, the default policy behavior is as follows:

- When a value appears in the field for a setting, the field is updated with the supplied value.

- When the value for the field is left empty, the field is updated to the default setting value.

- Any field absent from the request body leaves the setting value unchanged.

### Examples

The following XML samples demonstrate the policy behavior regarding the presence or lack of fields in a XML request body.

Refer to the examples in the right-hand panel.

PUT /user/{userid}

```
<user> <primaryExtension> <callForwardAllDestination> <sendToVoiceMailPilotNumber> true </sendToVoiceMailPilotNumber> <destination> 673285 </destination> </callForwardAllDestination> </primaryExtension> </user>
```

The XML code updates the call forward all sendToVoiceMailPilotNumber and destination fields for the user’s primary extension, and leaves all other settings untouched.

```
<user> <primaryExtension> <callForwardAllDestination> <destination> 673285 </destination> </callForwardAllDestination> </primaryExtension> </user>
```

This updates the destination field only, and leaves all other settings untouched.

```
<user> <primaryExtension> <callForwardAllDestination> <sendToVoiceMailPilotNumber /> <destination> 673285 </destination> </callForwardAllDestination> </primaryExtension> </user>
```

This sets the destination field, and resets the sendToVoiceMailPilotNumber field to the
                system default. The default settings are typically configurable by the system administrator.

# Authentication

View UDS Authentication.

# Developer Guide

The UDS Developer Guide is a comprehensive guide to using the UDS API. It contains information about authentication, troubleshooting, and code samples.

You can browse the Cisco User Data Services (UDS) Developer Guide.

To find other UDS developers, visit the UDS forum.

# UDS Response Status Codes

HTTP status codes are returned by the API with the responses.

## Success Response Codes

## Error Response Codes

# System-level Resources

# clusterUser

The clusterUser resource returns the domain name of the user’s home cluster. UDS first scans the local cluster and then fans out to search remote clusters. A parameter is required to use this resource. If you are unsure of the username or email address, you can search using the users resource. The response contains the publisher of the home cluster for that end user.

## clusterUser Request Format

```
GET https://{host}:8443/cucm-uds/clusterUser?username={userId}
        Content-Type: application/xml
```

### Query String Parameter

No authentication required. One parameter is required.

## clusterUser Response Format

Refer to response examples in the right-hand panel.

Example Responses

If user is found

```
<clusterUser version= "10.0.0" uri= "https://{host}/cucm-uds/clusterUser?username={userId}" > <result found= "true" uri= "https://{host}:8443/cucm-uds/user/{userId}" version= "10.0.0" /> <homeCluster serversUri= "https://{host}:8443/cucm-uds/servers" > {host} </homeCluster> <homeClusterDetails> <selfProvisioningSecureMode> true </selfProvisioningSecureMode> <adminProvisionMode> false </adminProvisionMode> </homeClusterDetails> </clusterUser>
```

If user is not found

```
<clusterUser version= "10.0.0" uri= "https://{host}/cucm-uds/clusterUser?username={userId}" > <result found= "false" /> </clusterUser>
```

# dayOfWeek

The dayOfWeek resource returns a list of values for each day of the week. It is used by a remote destination profile to obtain a schedule. For more information on remote destination profiles, consult the documentation about the remoteDestination resource.

## dayOfWeek Request Format

```
GET https://{host}:8443/cucm-uds/options/dayOfWeek
        Accept: application/xml
        Content-Type: application/xml
```

No authentication required.

## dayOfWeek Response Format

Example Response

```
<dayOfWeek> <option> <value> 0 </value> <name> Sunday </name> </option> <option> <value> 1 </value> <name> Monday </name> </option> <option> <value> 2 </value> <name> Tuesday </name> </option> <option> <value> 3 </value> <name> Wednesday </name> </option> <option> <value> 4 </value> <name> Thursday </name> </option> <option> <value> 5 </value> <name> Friday </name> </option> <option> <value> 6 </value> <name> Saturday </name> </option> </dayOfWeek>
```

Refer to the response example in the right-hand panel.

# groups

Invoke the groups resource by passing the search string containing the group name as a query parameter to the URL.

## groups Request Format

```
GET https:­//{host}:8443/cucm-uds/groups?name=pho
        Content-Type: application/xml
```

## groups Response Format

groups Example Response

```
<?xml version="1.0" encoding="UTF-8"?> <groups uri= "{host}:8443/cucm-uds/groups" version= "11.0.0" returnedCount= "5" > <group> <groupName> Phoenix1 </groupName> <distinguishedName> CN=Phoenix1,OU=dhanush,DC=adtest,DC=com </distinguishedName> <groupType> Active LDAP Synchronized Group </groupType> </group> <group> <groupName> Phoenix2 </groupName> <distinguishedName> CN=Phoenix2,OU=dhanush,DC=adtest,DC=com </distinguishedName> <groupType> Active LDAP Synchronized Group </groupType> </group> <group> <groupName> Phoenix3 </groupName> <distinguishedName> CN=Phoenix3,OU=dhanush,DC=adtest,DC=com </distinguishedName> <groupType> Active LDAP Synchronized Group </groupType> </group> <group> <groupName> Phoenix4 </groupName> <distinguishedName> CN=Phoenix4,OU=dhanush,DC=adtest,DC=com </distinguishedName> <groupType> Active LDAP Synchronized Group </groupType> </group> <group> <groupName> Phoenix5 </groupName> <distinguishedName> CN=Phoenix5,OU=dhanush,DC=adtest,DC=com </distinguishedName> <groupType> Active LDAP Synchronized Group </groupType> </group> </groups>
```

Refer to the example response in the right-hand panel.

# options

The options resource returns information that a client application uses to implement menu choices in its UI, such as the ring settings

## options Request Format

```
GET https://{host}:8443/cucm-uds/options
        Content-Type: application/xml
```

No authentication required.

## options Response Format

Example Response

```
<options version= "10.0.0" uri= "https://{host}/cucm-uds/options" > <messageWaitingVisualAlertPreference uri= "https://{host}/cucm-uds/options/messageWaitingVisualAlertPreference" > <option> <value> 0 </value> <name> Use System Policy </name> </option> <option> <value> 1 </value> <name> Light and Prompt </name> </option> <option> <value> 2 </value> <name> Prompt Only </name> </option> <option> <value> 3 </value> <name> Light Only </name> </option> <option> <value> 4 </value> <name> None </name> </option> </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference uri= "https://{host}/cucm-uds/options/messageWaitingAudibleAlertPreference" > <option> <value> 0 </value> <name> Off </name> </option> <option> <value> 1 </value> <name> On </name> </option> <option> <value> 2 </value> <name> Default </name> </option> </messageWaitingAudibleAlertPreference> <onACallRingPreference uri= "https://{host}/cucm-uds/options/onACallRingPreference" > <option> <value> 0 </value> <name> Use System Default </name> </option> <option> <value> 1 </value> <name> Disable </name> </option> <option> <value> 2 </value> <name> Flash Only </name> </option> <option> <value> 3 </value> <name> Ring Once </name> </option> <option> <value> 4 </value> <name> Ring </name> </option> <option> <value> 5 </value> <name> Beep Only </name> </option> </onACallRingPreference> <notOnACallRingPreference uri= "https://{host}/cucm-uds/options/notOnACallRingPreference" > <option> <value> 0 </value> <name> Use System Default </name> </option> <option> <value> 1 </value> <name> Disable </name> </option> <option> <value> 2 </value> <name> Flash Only </name> </option> <option> <value> 3 </value> <name> Ring Once </name> </option> <option> <value> 4 </value> <name> Ring </name> </option> <option> <value> 5 </value> <name> Beep Only </name> </option> </notOnACallRingPreference> <doNotDisturbSettings uri= "https://{host}/cucm-uds/options/doNotDisturbSettings" > <option> <value> 0 </value> <name> Ringer Off </name> </option> <option> <value> 1 </value> <name> Call Reject </name> </option> <option> <value> 2 </value> <name> Use Common Phone Profile Setting </name> </option> </doNotDisturbSettings> <voiceMailAvoidancePolicy uri= "https://{host}/cucm-uds/options/voiceMailAvoidancePolicy" > <option> <value> 0 </value> <name> Use System Default </name> </option> <option> <value> 1 </value> <name> Timer Control </name> </option> <option> <value> 2 </value> <name> User Control </name> </option> </voiceMailAvoidancePolicy> ... </options>
```

Refer to the example response in the right-hand panel.

## installedLocales

The installedLocales resource returns a list of installed locale information on the server.

### installedLocales Request Format

```
GET https://{host}:8443/cucm-uds/options/installedLocales
        Content-Type: application/xml
```

No authentication required.

### installedLocales Response Format

Example Response

```
<installedLocales> <option> <value> 1 </value> <name> English, United States </name> </option> ... </installedLocales>
```

Refer to the example response in the right-hand panel.

## models

The models resource returns a list of device models supported by the Cisco Unified CM and their related information. The response list contains a link to a localized user guide for each device model.

### models Request Format

```
GET https://{host}:8443/cucm-uds/options/models
        Content-Type: application/xml
```

No authentication required.

### models Response Format

Example Response

```
<models> <option> <value> 20 </value> <name> SCCP Phone </name> <productId> 33 </productId> <userGuides/> </option> <option> <value> 72 </value> <name> CTI Port </name> <productId> 25 </productId> <userGuides/> </option> <option> <value> 30027 </value> <name> Analog Phone </name> <productId> 30065 </productId> <userGuides/> </option> <option> <value> 9 </value> <name> Cisco 7935 </name> <productId> 32 </productId> <userGuides> <userGuide uri= "https://{host}/PhoneOnlineGuide/7935/7935user.pdf" protocol= "SCCP" /> </userGuides> </option> <option> <value> 6 </value> <name> Cisco 7910 </name> <productId> 34 </productId> <userGuides/> </option> <option> <value> 7 </value> <name> Cisco 7960 </name> <productId> 35 </productId> <userGuides> <userGuide uri= "https://{host}/PhoneOnlineGuide/7960/6040sccp.pdf" protocol= "SCCP" /> <userGuide uri= "https://{host}/PhoneOnlineGuide/7960/6040sip.pdf" protocol= "SIP" /> </userGuides> </option> <option> <value> 8 </value> <name> Cisco 7940 </name> <productId> 36 </productId> <userGuides> <userGuide uri= "https://{host}/PhoneOnlineGuide/7960/6040sccp.pdf" protocol= "SCCP" /> <userGuide uri= "https://{host}/PhoneOnlineGuide/7960/6040sip.pdf" protocol= "SIP" /> </userGuides> </option> ... </models>
```

Refer to the example response in the right-hand panel.

## timeZones

The timeZones resource returns a list of time zones recognized by the server.

### timeZones Request Format

```
GET https://{host}:8443/cucm-uds/options/timeZones
        Content-Type: application/xml
```

No authentication required.

### timeZones Response Format

Example Response

```
<timeZones> <option> <value> 359 </value> <name> (GMT-11:00) Etc/GMT+11 </name> </option> ... </timeZones>
```

Refer to the example response in the right-hand panel.

## userPolicy

The userPolicy resource returns a list of parameters that display the current settings for each user. The interface does not enforce userPolicy settings, but may do so in a future release. Developers should show or hide client features based on the settings returned by this resource. For example, if userPolicy indicates ShowChangePassword = true , then Users are allowed to perform this action. If ShowChangePassword = false , Developers should not offer this capability from the User Interface.

### userPolicy Request Format

```
GET https://{host}:8443/cucm-uds/options/userPolicy
        Content-Type: application/xml
```

Authentication required.

### userPolicy Response Format

Example Response

```
<userPolicy version= "10.0.0" uri= "https://{host}/cucm-uds/options/userPolicy" > <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowCallForward" > <name> ShowCallForward </name> <value> 1 </value> <options> <option value= "1" > Show All Settings </option> <option value= "2" > Hide All Settings </option> <option value= "3" > Show Only Forward All </option> </options> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowChangePassword" > <name> ShowChangePassword </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowChangePin" > <name> ShowChangePin </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowDirectorySearch" > <name> ShowDirectorySearch </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowApplications" > <name> ShowApplications </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowIPPhoneServices" > <name> ShowIPPhoneServices </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowLineLabel" > <name> ShowLineLabel </name> <value> false </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowHistorySettings" > <name> ShowHistorySettings </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowConferencingScheduler" > <name> ShowConferencingScheduler </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowVoicemailIVROption" > <name> ShowVoicemailIVROption </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowMessageWaitingAlertPreference" > <name> ShowMessageWaitingAlertPreference </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowExternalPhoneSettings" > <name> ShowExternalPhoneSettings </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowOnlinePhoneGuide" > <name> ShowOnlinePhoneGuide </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowPhoneContacts" > <name> ShowPhoneContacts </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowRingPreferences" > <name> ShowRingPreferences </name> <value> false </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowSpeedDials" > <name> ShowSpeedDials </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/OnACallRingPreferenceDefault" > <name> OnACallRingPreferenceDefault </name> <value> 5 </value> <options> <option value= "1" > Disable </option> <option value= "2" > Flash Only </option> <option value= "3" > Ring Once </option> <option value= "4" > Ring\ </option> <option value= "5" > Beep Only\ </option> </options> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/NotOnACallRingPreferenceDefault" > <name> NotOnACallRingPreferenceDefault </name> <value> 4 </value> <options> <option value= "1" > Disable </option> <option value= "2" > Flash Only </option> <option value= "3" > Ring Once </option> <option value= "4" > Ring </option> </options> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/MessageWaitingAlertAudioPreferenceDefault" > <name> MessageWaitingAlertAudioPreferenceDefault </name> <value> 0 </value> <options> <option value= "0" > OFF </option> <option value= "1" > ON </option> </options> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/MessageWaitingAlertVisualPreferenceDefault" > <name> MessageWaitingAlertVisualPreferenceDefault </name> <value> 0 </value> <options> <option value= "0" > Primary Line - Light and Prompt </option> <option value= "1" > Primary Line - Prompt Only </option> <option value= "2" > Primary Line - Light Only </option> <option value= "3" > Light and Prompt </option> <option value= "4" > Prompt Only </option> <option value= "5" > Light Only </option> <option value= "6" > None </option> </options> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/UserLocalDefault" > <name> UserLocalDefault </name> <value> 1 </value> <range> <default> 250 </default> <min> 50 </min> <max> 9999 </max> </range> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/VoiceMailAvoidancePolicy" > <name> VoiceMailAvoidancePolicy </name> <value> 1 </value> <options> <option value= "1" > Timer Control </option> <option value= "2" > User Control </option> </options> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/PhoneServiceDisplay" > <name> PhoneServiceDisplay </name> <value> 0 </value> <options> <option value= "0" > Internal </option> <option value= "1" > External URL </option> <option value= "2" > Both </option> </options> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/EnableAllUserSearch" > <name> EnableAllUserSearch </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/UserSearchLimit" > <name> UserSearchLimit </name> <value> 500 </value> <range> <default> 64 </default> <min> 1 </min> <max> 500 </max> </range> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/NumberofDigitstoMatch" > <name> NumberofDigitstoMatch </name> <value> 4 </value> <range> <default> 4 </default> <min> 3 </min> <max> 256 </max> </range> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/URILookupPolicy" > <name> URILookupPolicy </name> <value> 0 </value> <options> <option value= "0" > Case Sensitive </option> <option value= "1" > Case Insensitive </option> </options> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowCalendarPreference" > <name> ShowCalendarPreference </name> <value> true </value> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowCallHistory" > <name> ShowCallHistory </name> </policy> <policy uri= "https://{host}/cucm-uds/options/userPolicy/ShowVideoConferencingScheduler" > <name> ShowVideoConferencingScheduler </name> <value> true </value> </policy> </userPolicy>
```

Refer to the example response in the right-hand panel.

# phoneServices

Returns a list of the IP Phone Services currently configured in the  Cisco Unified CM system. This resource provides only a list of the services. To obtain detailed information for a particular service, use the PhoneService resource.

## phoneServices Request Format

```
GET https://{host}:8443/cucm-uds/phoneServices
        Content-Type: application/xml
```

No authentication required.

## phoneServices Response Format

Example Response

```
<phoneServices uri= "https://{host}:8443/cucm-uds/phoneServices" version= "{version}" > <phoneService uri= "https://{host}:8443/cucm-uds/phoneService/{phoneServicePkid}" > <id> {phoneServicePkid} </id> <name> serviceName </name> <description> serviceDescription </description> <category> XML Service </category> <vendor /> <serviceVersion /> <enabled> true|false </enabled> </phoneService> ... </phoneServices>
```

Refer to the example response in the right-hand panel.

# phoneService

The PhoneService resource returns the detailed information for a particular IP Phone Service. The URL for accessing the PhoneService resource should be retrieved from the PhoneServices response.

## phoneService Request Format

```
GET https://{host}:8443/cucm-uds/phoneService/{phoneServiceid}
        Content-Type: application/xml
```

No authentication required.

### Path Parameters

## phoneService Response Format

Example Response

```
<phoneService uri= "https://{host}:8443/cucm-uds/phoneService/{phoneServicePkid}" version= "{version}" > <id> {phoneServicePkid} </id> <name> serviceName </name> <description> serviceDescription </description> <urlTemplate> http://www.example.com/service/template/url </urlTemplate> <secureUrlTemplate> https://www.example.com/service </secureUrlTemplate> <category> XML Service </category> <type> Standard IP Phone Service </type> <vendor /> <serviceVersion /> <enabled> true </enabled> <parameters> <parameter> <paramId> {phoneServiceParamPkid} </paramId> <displayName> TestParam </displayName> <description> test </description> <defaultValue /> <isRequired> true|false </isRequired> <isCredential> true|false </isCredential> </parameter> </parameters> </phoneService>
```

Refer to the example response in the right-hand panel.

# servers

The servers resource returns a list of all the Cisco Unified CM nodes within that cluster. This resource is used to load balance requests. Cisco recommends your application make a request to the first server in the list. If the server is busy, then pick another server until your application can successfully make a request.

## servers Request Format

```
GET https://{host}:8443/cucm-uds/servers
        Content-Type: application/xml
```

No authentication required.

## servers Response Format

Example Response

```
<servers version= "{version}" uri= "https:://{host}:8443/cucm-uds/servers" > <server> {host} </server> <server> {host1} </server> <server> {host2} </server> ... </servers>
```

Refer to the example response in the right-hand panel.

# timeOfDay

The timeOfDay resource returns a list of values for each time of the day in 15 minute increments. It is used by a remote destination profile to obtain a schedule. For more information on remote destination profiles, consult the documentation about the remoteDestination resource.

## timeOfDay Request Format

```
GET https://{host}:8443/cucm-uds/options/timeOfDay
        Accept: application/xml
        Content-Type: application/xml
```

No authentication required.

## timeofDay Response Format

Example Response

```
<timeOfDay> <option> <value> 0 </value> <name> No office hours </name> </option> <option> <value> 1 </value> <name> 00:00 </name> </option> <option> <value> 2 </value> <name> 00:15 </name> </option> <option> <value> 3 </value> <name> 00:30 </name> </option> </timeOfDay>
```

Refer to the example response in the right-hand panel.

Note that the time of day value is an integer that specifies a fifteen minute interval within a 24 hour period, where:

0 = 00:00

1 = 00:15

2 = 00:30

…

95 = 23:30

96 = 23:45

97 = 24:00

# users

The users resource provides search functions to locate users stored in the Cisco Unified CM database. It is highly recommended that query string parameters be used to filter the search results.

## users Request Format

```
GET https://{host}:8443/cucm-uds/users
        Content-Type: application/xml
```

The default number of users returned is 64. The number of users returned can be controlled through Enterprise Parameters > User Data Services > User Search Limit Settings in Unified CM. The user count starts at 0. If the user search result exceeds the number specified, it returns only partial results up to the specified search limit. Therefore, it is recommended to use the start and max parameter to paginate the results.

### Query String Parameters

- For an input text string without spaces, the search should be performed as a ‘starting with’ search to match the user’s first name, last name, or email.

- When there is space detected in the input text, below is the expected behavior for search:

- When the search criteria contains one space, these are the rules for searching within the user name: When searching for “x y” (first starts with x AND last starts with y) OR (last starts with x AND first starts with y) OR (last starts with “x y”) OR (first starts with “x y”)

- When the search criteria contains two spaces, these are the rules for searching within the user name: When searching for “x y z” (first starts with x AND last starts with “y z”) OR (first starts with “x y” AND last starts with z) OR (last starts with x AND first starts with “y z”) OR (last starts with “x y” AND first starts with z)

- When the search criteria contains more than two spaces, only the first three sets of characters are considered as in #2.

No authentication required.

Example: Retrieve users who have a first name beginning with “u” and a number that starts with “214” https://{host}:8443/cucm-uds/users?first=u&number=214

## users Response Format

Example Response

```
<users uri= "https://{host}/cucm-uds/users" version= "10.0.0" start= "0" requestedCount= "10" returnedCount= "10" totalCount= "100" > <user uri= "https://{host}:8443/cucm-uds/user/{userId}" > <id> ec9d96b1-ad1a-dfd6-0e89-ec1cfff26aff </id> <userName> johndoe </userName> <firstName> John </firstName> <lastName> Doe </lastName> <middleName /> <nickName /> <displayName /> <phoneNumber /> <homeNumber /> <mobileNumber /> <email /> <directoryUri /> <msUri /> <department /> <manager /> <title /> <pager /> </user> ... </users>
```

Refer to the example response in the right-hand panel.

In the example:

- requested count is equal to the max parameter in the request

- returned count is the total number of users displayed in this request

- total count is the total number of users

# version

Returns the currently installed Cisco Unified CM product name and version (x.x.x).

## version Request Format

```
GET https://{host}:8443/cucm-uds/version
        Content-Type: application/xml
```

No authentication required.

## version Response Format

Example Response

```
<?xml version="1.0" encoding="UTF-8"?> <versionInformation uri= "https://{host}/cucm-uds/version" version= "10.0.0" > <version> 10.0.0 </version> </versionInformation>
```

Refer to the example response in the right-hand panel.

# User Resources

# user

The user resource allows a user to access and manage their personal information. Common settings can be applied across all of a user’s devices and extensions. Look for the “appliesToAll” attribute within the device and extension tags. It supports GET and PUT methods.

## Display user Information

Returns detailed information about the specified user.

Note: UDS does not support user IDs that have the ‘/’ character in them.

### Display user Information Request Format

```
GET https://{host}:8443/cucm-uds/user/{userid}
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Display user Information Response Format

Example Response

```
<user version= "{version}" uri= "https://{host}:8443/cucm-uds/user/{userId}" > <id> {userPkid} </id> <userName> {userId} </userName> <firstName> firstName </firstName> <lastName> lastName </lastName> <selfServiceId> 1000*1 </selfServiceId> <middleName> middleName </middleName> <nickName> nickName </nickName> <displayName> {userId} displayName </displayName> <phoneNumber> 8134567 </phoneNumber> <homeNumber> 8134455 </homeNumber> <mobileNumber> 8131111 </mobileNumber> <mobileConnect> true|false </mobileConnect> <remoteDestinationLimit> 4 </remoteDestinationLimit> <userLocale uri= "https://{host}:8443/cucm-uds/installedLocales" value= "1" appliesToAllDevices= "true|false" > English, United States </userLocale> <email> someone@example.com </email> <directoryUri> someone@example.com </directoryUri> <msUri> someone@example.com </msUri> <department> department </department> <manager> manager </manager> <title> title </title> <pager> 8137777 </pager> <accountType useLdapAuth= "true|false" > ldap|local </accountType> <homeCluster enableCalendarPresence= "true|false" enableImAndPresence= "true|false" > true|false </homeCluster> <primaryExtension> <description> extensionDescription </description> <directoryNumber> 81134953 </directoryNumber> <callForwardAllDestination> <sendToVoiceMailPilotNumber> true|false </sendToVoiceMailPilotNumber> <destination> 4352134 </destination> </callForwardAllDestination> <messageWaitingVisualAlert> true|false </messageWaitingVisualAlert> <messageWaitingVisualAlertPreference appliesToAllLineAppearances= "true|false" value= "" > Use System Policy </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference appliesToAllLineAppearances= "true|false" value= "1" > Default </messageWaitingAudibleAlertPreference> <onACallRingPreference appliesToAllLineAppearances= "true|false" value= "" > Use System Default </onACallRingPreference> <notOnACallRingPreference appliesToAllLineAppearances= "true|false" value= "4" > Ring </notOnACallRingPreference> <voiceMailPilotNumber> 5555 </voiceMailPilotNumber> <label> label </label> <logMissedCalls> true|false </logMissedCalls> </primaryExtension> <callForwardAllDestination appliesToAllExtensions= "true|false" > <sendToVoiceMailPilotNumber> true|false </sendToVoiceMailPilotNumber> <destination> 43521 </destination> </callForwardAllDestination> <enableDoNotDisturb appliesToAllDevices= "true|false" > true|false </enableDoNotDisturb> <devices uri= "https://{host}:8443/cucm-uds/user/{userId}/devices" /> <credentials uri= "https://{host}:8443/cucm-uds/user/{userId}/credentials" /> <extensions uri= "https://{host}:8443/cucm-uds/user/{userId}/extensions" /> <subscribedServices uri= "https://{host}:8443/cucm-uds/user/{userId}/subscribedServices" /> <speedDials uri= "https://{host}:8443/cucm-uds/user/{userId}/speedDials" /> <serviceProfile> <uri> http://{host}:6970/SPDefault.cnf.xml </uri> </serviceProfile> </user>
```

Refer to the example response in the right-hand panel.

## Update user Information

Allows the user to modify their personal information.

UDS allows PUT methods only when homeCluster is true for the user.

### Update user Information Request Format

```
PUT https://{host}:8443/cucm-uds/user/{userid}
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Update user Information Request Body

Example Request Body

```
<user> <primaryExtension> <callForwardAllDestination> <sendToVoiceMailPilotNumber> true|false </sendToVoiceMailPilotNumber> <destination> 673285 </destination> </callForwardAllDestination> <messageWaitingVisualAlertPreference> 0 </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference> 0 </messageWaitingAudibleAlertPreference> <onACallRingPreference> 0 </onACallRingPreference> <notOnACallRingPreference> 0 </notOnACallRingPreference> </primaryExtension> <userLocale appliesToAllDevices= "true|false" > 0 </userLocale> <enableCalendarPresence> true|false </enableCalendarPresence> <enableDoNotDisturb> true|false </enableDoNotDisturb> <callForwardAllDestination> <sendToVoiceMailPilotNumber> true|false </sendToVoiceMailPilotNumber> <destination> 43521 </destination> </callForwardAllDestination> <logMissedCalls> true|false </logMissedCalls> </user>
```

All fields are optional.

Refer to the example request body in the right-hand panel.

If sendToVoiceMailPilotNumber is set to true, then the call will not be forwarded to the destination number. If sendToVoiceMailPilotNumber is set to false, then the call will be forwarded to the destination number. The sendToVoiceMailPilotNumber and destination tags can:

- both be declared

- neither be declared

- one be declared

### Update user Information Response Format

The response is identical to the one returned by a user GET method.

# conferencing

The conferencing resource allows a user to access and update conference access codes. The conferencing resource supports GET and PUT methods.

## conferencing GET Request Format

```
GET https://{host}:8443/cucm-uds/user/{userId}/conferencing
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

## conferencing GET Example Response

GET Example Response Body

```
<?xml version="1.0" encoding="UTF-8"?> <conferencing uri= "https://{hostname}/cucm-uds/user/{userid}/conferencing" version= "11.0.0" > <conferenceNow> <enabled> true </enabled> <accessCode> 1234 </accessCode> </conferenceNow> </conferencing>
```

## conferencing PUT Request Format

```
PUT https://{host}:8443/cucm-uds/user/{userId}/conferencing
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

## conferencing PUT Request Body

Example PUT Request Body

```
<?xml version="1.0" encoding="UTF-8"?> <conferencing> <conferenceNow> <enabled> true </enabled> <accessCode> 9876 </accessCode> </conferenceNow> </conferencing>
```

## conferencing PUT Example Response

PUT Example Response Body

```
<?xml version="1.0" encoding="UTF-8"?> <conferencing uri= "https://{hostname}/cucm-uds/user/{userid}/conferencing" version= "11.0.0" > <conferenceNow> <enabled> true </enabled> <accessCode> 9876 </accessCode> </conferenceNow> </conferencing>
```

# credentials

The credentials resource provides the ability to update the user’s credential information, which consists of either a password or PIN number.

The GET method allows users to retrieve the last successful login-time/IP-address, and the number of unsuccessful login attempts

## credentials GET Request Format

```
GET https://{host}:8443/cucm-uds/user/{userId}/credentials
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

## credentials GET Example Response

```
<credentials uri= "https://{hostname}/cucm-uds/user/{userid}/conferencing" version= "11.0.0" > <credential> <loginDetails> <lastSuccessfulLogin> 2015-04-17T19:36:42.000Z </lastSuccessfulLogin> <lastSuccessfulLoginIp> 172.30.223.139 </lastSuccessfulLoginIp> </loginDetails> <loginFailures> 0 </loginFailures> </credential> </credentials>
```

## credentials PUT Request Format

```
PUT https://{host}:8443/cucm-uds/user/{userId}/credentials
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

## credentials PUT Request Body

Example PUT Request Body

```
<credentials> <credential type= "password" > 1234 </credential> <credential type= "pin" > 4321 </credential> </credentials>
```

At least one credentials element is required.

Note that the ‘password’ type credential for users authenticated via LDAP cannot be updated. See the GET /user/ response and the accountType element useLdapAuth attribute.

## credentials PUT Example Response

Status Code:204

No Content

The server has completed the request and does not need to send a response body.

# devices

The devices resource returns an unordered list of devices associated to the user.

If the user has entered information into the description field for a device, it is returned with this call. Otherwise, it returns the default description as set by the administrator.

## devices Request Format

```
GET https://{host}:8443/cucm-uds/user/{userId}/devices
        Content-Type: application/xml
```

### Path Parameter

### Query String Parameter

User authentication required.

## devices Response Format

Example Response

```
<devices uri= "https://{host}/cucm-uds/user/{userId}/devices" version= "10.0.0" > <device uri= "https://{host}/cucm-uds/user/{userId}/device/2a610c78-6754-2c56-bd4d-5a8d972c7a43" > <id> 2a610c78-6754-2c56-bd4d-5a8d972c7a43 </id> <name> SEP00DEADBEEF01 </name> <type> Phone </type> <model> Cisco 7965 </model> <description editable= "true" > SEP00DEADBEEF01 </description> <protocol> SCCP </protocol> </device> <device uri= "https://{host}/cucm-uds/user/{userId}/device/5ebe75fb-43ac-b458-5539-bc57806a4d19" > <id> 5ebe75fb-43ac-b458-5539-bc57806a4d19 </id> <name> SEP00DEADBEEF05 </name> <type> Phone </type> <model> Cisco 7965 </model> <description editable= "true" > SEP00DEADBEEF05 </description> <protocol> SCCP </protocol> </device> <device uri= "https://{host}/cucm-uds/user/{userId}/device/61d8d4f9-aa7e-698f-7f46-263be7e44d69" > <id> 61d8d4f9-aa7e-698f-7f46-263be7e44d69 </id> <name> SEP00DEADBEEF03 </name> <type> Phone </type> <model> Cisco 7965 </model> <description editable= "true" > SEP00DEADBEEF03 </description> <protocol> SCCP </protocol> </device> </devices>
```

A description set by the user takes precedence over the description set by the administrator.

Refer to the example response in the right-hand panel.

# extensions

The extensions resource returns a listing of all of the extension information from the associated user. Note the following:

- Label is a field whose value is set by the user. It is not an administrator field.

- If the user has a primary extension, it is displayed first.

- For client devices, having sendToVoiceMailPilotNumber set to true takes precedence over the setting in callForwardAllDestination .

## extensions Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userid}/extensions
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

## extensions Response Format

Example Response

```
<extensions version= "10.0.0" uri= "https://{host}:8443/cucm-uds/user/{userId}/extensions" > <extension isPrimary= "false" uri= "https://{host}:8443/cucm-uds/user/{userId}/extension/0d896090-483e-f472-065b-aa2163fc6efa" > <id> 0d896090-483e-f472-065b-aa2163fc6efa </id> <directoryNumber> 1111 </directoryNumber> <voiceMailPilotNumber /> <callForwardAllDestination> <sendToVoiceMailPilotNumber> false </sendToVoiceMailPilotNumber> <sendToCustomDestination> 5555 </sendToCustomDestination> </callForwardAllDestination> <messageWaitingVisualAlert> false </messageWaitingVisualAlert> <messageWaitingVisualAlertPreference appliesToAllLineAppearances= "true" value= "" > Use System Policy </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference appliesToAllLineAppearances= "true" value= "" > Default </messageWaitingAudibleAlertPreference> <onACallRingPreference appliesToAllLineAppearances= "true" value= "" > Use System Default </onACallRingPreference> <notOnACallRingPreference appliesToAllLineAppearances= "true" value= "" > Use System Default </notOnACallRingPreference> <label appliesToAllLineAppearances= "true" /> <logMissedCalls appliesToAllLineAppearances= "true" > true </logMissedCalls> </extension> ... </extensions>
```

Refer to the example response in the right-hand panel.

# remoteDestinations

The remoteDestinations resource manages the configuration of how calls are transferred to another destination device, which could be a mobile device that has Cisco Mobility Client installed. The remoteDestinations resource obtains information about remote destination device configurations.

There are four scenarios:

- Dual mode case

- Remote Destination Profile (RDP) only

- CTI Remote Device only

- RDP and CTI Remote Device share the same destination

Each scenario has a slightly different response. See the example response section for more information.

Note: This resource does not provide results if the user does not have remote destination information stored in the database.

## remoteDestinations Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/remoteDestinations
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

## remoteDestinations Response Format

Example Response

```
<remoteDestinations version= "10.0.0" uri= "https:­//{host}:8443/cucm-uds/user/{userId}/remoteDestinations" > <remoteDestination uri= "https:­//{host}/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}" > <id> {remoteDestinationPkid} </id> <name> RemoteDestination1 </name> <destination> 12345678901 </destination> <ringWhenExtensionDialed> true|false </ringWhenExtensionDialed> <allowTransferToMobile> true|false </allowTransferToMobile> <allowControlFromApplication> true|false </allowControlFromApplication> <associatedDevices> <associatedDevice> <usage uri= "https:­//{host}:8443/cucm-uds/options/remoteDestinationUsage" value= "0" > Single Number Reach </usage> <name> My Cell </name> <description> cell phone </description> </associatedDevice> </associatedDevices> </remoteDestination> </remoteDestinations>
```

Refer to the response example in the right-hand panel.

# remoteDestination

The remoteDestination resource manages the configuration of how calls are transferred to another destination device, which could be a mobile device. It supports GET , POST , and PUT methods.

Note: The user must already have a remote destination profile or a CTI remote device configured in UCM.

## Get remoteDestination for a Device

Returns detailed configuration information about the remote destination device, including a weekly schedule of calls that are to be transferred to the remote destination. For the weekly schedule, if:

- A day is not present, then the remote device is not enabled for that day.

- For a timeOfDayStart value of “00:00” and a timeOfDayEnd value of “24:00”, this equates to “all day”. No special tag is used to specify this interval.

### Get remoteDestination for a Device Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Get remoteDestination for a Device Response Format

Example Response

```
<remoteDestination version= "10.0.0" uri= "https://{host}/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}" > <id> {remoteDestinationPkid} </id> <name> Adrienne's Cell </name> <destination> 5555555 </destination> <ringWhenExtensionDialed> true|false </ringWhenExtensionDialed> <allowTransferToMobile> true|false </allowTransferToMobile> <allowControlFromApplication> true|false </allowControlFromApplication> <associatedDevices> <associatedDevice> <name> TestRDP1 </name> <usage uri= "https://{host}/cucm-uds/options/remoteDestinationUsage" value= "0" > <option value= "0" > Single Number Reach </option> <option value= "1" > Application Control </option> <option value= "2" > Dual Mode Mobile </option> </usage> <description> This is a test remote destination profile </description> <associatedExtensions> <associatedExtension enable= "false" > 7778 </associatedExtension> </associatedExtensions> </associatedDevice> </associatedDevices> <advancedSettings> <delayBeforeRingTimer> 4.0 </delayBeforeRingTimer> <voiceMailAvoidanceSettings> <answerTooSoonTimer> 1.5 </answerTooSoonTimer> <voiceMailAvoidancePolicy uri= "https://{host}/cucm-uds/options/voiceMailAvoidancePolicy" value= "0" > Use System Default </voiceMailAvoidancePolicy> </voiceMailAvoidanceSettings> <answerTooLateTimer> 19.0 </answerTooLateTimer> </advancedSettings> </remoteDestination>
```

Refer to the example response in the right-hand panel.

## Add a Device as a remoteDestination

Adds the specified device as a remote destination.

Requirements for a successful request:

- The remote destination must already be assigned to a user.

- If the remote destination is currently associated with the user, use the PUT method instead of the POST method. That is, instead of adding a destination, perform an update on an existing destination.

### Add a Device as a remoteDestination Request Format

```
POST https:­//{host}:8443/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Add a Device as a remoteDestination Request Body

Example Request Body

```
<remoteDestination> <name> Home </name> <destination> +12345678901 </destination> <ringWhenExtensionDialed> true|false </ringWhenExtensionDialed> <allowTransferToMobile> true </allowTransferToMobile> <allowControlFromApplication> true|false </allowControlFromApplication> <associatedDevices> <associatedDevice> <name> RD02 </name> <usage> 2 </usage> </associatedDevice> </associatedDevices> </remoteDestination>
```

Refer to the example request body in the right-hand panel.

## Update remoteDestination Information

Updates existing call destination information for the specified remote device.

Requirements for a successful request:

- The remote destination already exists.

- The description field cannot be updated.

### Update remoteDestination Information Request Format

```
PUT https:­//{host}:8443/cucm-uds/user/{userId}/remoteDestination/{remoteDestinationPkid}
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Update remoteDestination Information Request Body

Example Request Body

```
<remoteDestination> <name> Adrienne's Cell </name> <destinationNumber> +12121212121 </destinationNumber> <ringWhenExtensionDialed> true|false </ringWhenExtensionDialed> <allowTransferToMobile> true </allowTransferToMobile> <allowControlFromApplication> true|false </allowControlFromApplication> <associatedDevices> <associatedDevice> <name> RD01 </name> <usage> 0 </usage> </associatedDevice> </associatedDevices> </remoteDestination>
```

Refer to the example request body in the right-hand panel.

# speedDials

The speedDials resource manages speed dial information for a user. It supports GET , POST , PUT , and DELETE methods.

## Get the User’s speedDials

Returns a summary of all of the user’s speed dial information.

If all of the speed dial information on every device that is owned or associated to the user is identical, the list is considered to be unified.

- If the list is unified, speedDials returns a list of speed dials as well as a device listing that displays drill down links to speed dial information for each device.

- If the list is not unified, speedDials returns only a device listing that displays drill down links to the speed dial information for each device.

### Get the User’s speedDials Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/speedDials
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Get the User’s speedDials Response Format

Refer to the response examples in the right-hand panel:

Example Responses

If speed dials are unified

- If speed dials are unified (“appliesToAllDevices=true”).

```
<userSpeedDials uri= "https:­//{host}:8443/cucm-uds/user/{userId}/speedDials" version= "{version}" > <speedDials appliesToAllDevices= "true" totalCount= "3" > <speedDial> <index> 1 </index> <number> 1234567890 </number> <label> Manager </label> </speedDial> <speedDial> <index> 2 </index> <number> 1234567899 </number> <label> Assistant </label> </speedDial> <speedDial> <index> 3 </index> <number> 1234567 </number> <label> VP </label> </speedDial> </speedDials> <devices> <device name= "SEP000001000003" description= "Auto 100002" speedDialsUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/speedDials" /> <device name= "SEP000001000004" description= "Auto 100003" speedDialsUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/speedDials" /> <device name= "SEP000001000005" description= "Auto 100004" speedDialsUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/speedDials" /> </devices> </userSpeedDials>
```

- If speed dials are not unified (“appliesToAllDevices=false”).

If speed dials are not unified

```
<userSpeedDials uri= "https:­//{host}:8443/cucm-uds/user/{userId}/speedDials" version= "{version}" > <speedDials appliesToAllDevices= "false" totalCount= "0" /> <devices> <device name= "SEP000001000003" description= "Auto 100002" speedDialsUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/speedDials" /> <device name= "SEP000001000004" description= "Auto 100003" speedDialsUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/speedDials" /> <device name= "SEP000001000005" description= "Auto 100004" speedDialsUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/speedDials" /> </devices> </userSpeedDials>
```

## Add speedDials

The speedDials POST method adds new speed dials.

The number of displayable speed dials supported may vary by device model and configuration. Speed dials added to a device may be converted into abbreviated dials based on the device settings.

### Add speedDials Request Format

```
POST https:­//{host}:8443/cucm-uds/user/{userId}/speedDials
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Add speedDials Request Body

Example Request Body

```
<speedDials> <speedDial> <index> 1 </index> <number> 1234567890 </number> <label> Manager </label> </speedDial> <speedDial> <index> 2 </index> <number> 1234567899 </number> <label> Assistant </label> </speedDial> </speedDials>
```

The index indicates the order in which speed dials appear on the device. The index is required.

## Update speedDials

The speedDials PUT method updates the speed dial list with the specified speed dials.

If a device in the group of devices owned or associated with the user does not support enough displayable speed dials, the speed dial entries are created anyway. Speed dials that cannot be displayed are treated as “abbreviated dials”.

### Update speedDials Request Format

```
PUT https:­//{host}:8443/cucm-uds/user/{userId}/speedDials
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Update speedDials Request Body

Example Request Body

```
<speedDials> <speedDial> <index> 1 </index> <number> 1234567890 </number> <label> Manager </label> </speedDial> <speedDial> <index> 2 </index> <number> 1234567899 </number> <label> Assistant </label> </speedDial> <speedDial> <index> 3 </index> <number> 0001 </number> <label> CEO </label> </speedDial> </speedDials>
```

Refer to the example request body in the right-hand panel.

The index is required.

## Remove a speedDial

Clears the speed dial information using the specified index and userId. It performs this operations across all of the devices owned by the user.

### Remove a speedDial Request Format

```
DELETE https:­//{host}:8443/cucm-uds/user/{userId}/speedDials?index={index}
        Accept: application/xml
        Content-Type: application/xml
```

User authentication required.

### Path Parameters

### Query String Parameter

### Error Responses

Status Code:204

No Content

The server has completed the request and does not need to send a response body.

# subscribedServices

The subscribedServices resource accesses the consolidated subscribed IP phone services for a user. If the user has different subscribed IP phone services on different devices, the response includes the URL for accessing the subscribed services for those devices. subscribedServices supports GET , POST , PUT , and DELETE methods.

## Get a User’s subscribedServices

Returns a list of subscribed services for the specified user.

### Get a User’s subscribedServices Request Format

```
GET https://{host}:8443/cucm-uds/user/{userId}/subscribedServices
        Content-Type: application/xml
```

### Path Parameter

User authentication required.

### Get a User’s subscribedServices Response Format

Example Response

```
<userSubscribedServices uri= "https://{host}/cucm-uds/user/{userId}/subscribedServices" version= "10.0.0" > <subscribedServices appliesToAllDevices= "true" totalCount= "1" > <subscribedService> <name> udsTestService1 </name> <url> http://udsTestService1 </url> <secureUrl> </secureUrl> <phoneServiceName phoneServiceId= "292ab26b-5052-dd46-325f-45b12d4822a7" > udsTestService1 </phoneServiceName> </subscribedService> </subscribedServices> <devices> <device name= "SEP000001000003" description= "Auto 100002" subscribedServicesUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/subscribedServices" /> <device name= "SEP000001000004" description= "Auto 100003" subscribedServicesUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/subscribedServices" /> <device name= "SEP000001000005" description= "Auto 100004" subscribedServicesUri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/subscribedServices" /> </devices> </userSubscribedServices>
```

Refer to the example response in the right-hand panel.

## Add subscribedServices

The subscribedServices POST method adds a new subscribed service to a user’s subscribedServices list.

Requests can be made in two formats:

- url/secureUrl Either a url or a secureUrl must be present in the request. subscribedServices parses any parameters from the provided url/secureUrl. The url/secureUrl must match the phoneService template definition.

- parameter list The parameter pkid must match the pkid returned by a GET phoneService response.

Note: If both request format styles are present (url/secureUrl and parameter list), they must be equivalent.

### Add subscribedServices Request Format

```
POST https:­//{host}:8443/cucm-uds/user/{userId}/subscribedServices
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameter

User authentication required.

### Add subscribedServices Request Body

The phoneServiceId is required and must exist.

- URL/secure URL format

Example Request Body

```
<subscribedServices> <subscribedService> <name> InternalTechSupport </name> <phoneServiceId> {phoneServiceId} </phoneServiceId> <url> http:­//{host}/servlet/GTRCService?menuname=US </url> <secureUrl> https:­//{host}/servlet/GTRCService?menuname=US </secureUrl> </subscribedService> <subscribedService> <name> Service2 </name> <phoneServiceId> {phoneServiceId} </phoneServiceId> <url> http:­//{host}/servlet/GTRCService2?menuname=US </url> <secureUrl> https:­//{host}/servlet/GTRCService2?menuname=US </secureUrl> </subscribedService> </subscribedServices>
```

Refer to the response example in the right-hand panel.

- Parameter list

Example Request Body

```
<subscribedServices> <subscribedService> <name> InternalTechSupport </name> <phoneServiceId> {phoneServicePkid} </phoneServiceId> <parameters> <parameter> <paramId> {pkid} </paramId> <value> 5 </value> </parameter> </parameters> </subscribedService> <subscribedService> <name> Service2 </name> <phoneServiceId> {phoneServicePkid} </phoneServiceId> <parameters> <parameter> <paramId> {pkid} </paramId> <value> 5 </value> </parameter> </parameters> </subscribedService> </subscribedServices>
```

Refer to the example response in the right-hand panel.

## Update subscribedServices

The subscribedServices PUT method replaces the subscribedServices list with the specified services.

Requests can be made in two formats:

- url/secureUrl: Either a url or a secureUrl must be present in the request. subscribedServices parses any parameters from the provided url/secureUrl. The url/secureUrl must match the phoneService template definition.

- parameter list: The parameter pkid must match the pkid returned by a GET phoneService response.

Note: If both request format styles are present (url/secureUrl and parameter list), they must be equivalent.

### Update subscribedServices Request Format

```
PUT https:­//{host}:8443/cucm-uds/user/{userId}/subscribedServices
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameter

User authentication required.

### Update subscribedServices Request Body

The phoneServiceId is required and must exist.

- URL/secure URL format

Example Request Body - URL format

```
<subscribedServices> <subscribedService> <name> InternalTechSupport </name> <phoneServiceId> {phoneServiceId} </phoneServiceId> <url> http:­//{host}/servlet/GTRCService?menuname=US </url> <secureUrl> https:­//{host}/servlet/GTRCService?menuname=US </secureUrl> </subscribedService> <subscribedService> <name> Service2 </name> <phoneServiceId> {phoneServiceId} </phoneServiceId> <url> http:­//{host}/servlet/GTRCService2?menuname=US </url> <secureUrl> https:­//{host}/servlet/GTRCService2?menuname=US </secureUrl> </subscribedService> </subscribedServices>
```

Refer to the example request body in the right-hand panel.

- Parameter list

Example Request Body - Parameter List

```
<subscribedServices> <subscribedService> <name> InternalTechSupport </name> <phoneServiceId> {phoneServicePkid} </phoneServiceId> <parameters> <parameter> <paramId> {pkid} </paramId> <value> 5 </value> </parameter> </parameters> </subscribedService> <subscribedService> <name> Service2 </name> <phoneServiceId> {phoneServicePkid} </phoneServiceId> <parameters> <parameter> <paramId> {pkid} </paramId> <value> 5 </value> </parameter> </parameters> </subscribedService> </subscribedServices>
```

Refer to the example request body in the right-hand panel.

## Remove subscribedServices

The subscribedServices DELETE method deletes all of the subscribed services from all of the user’s devices.

### Remove subscribedServices Request Format

```
DELETE https:­//{host}:8443/cucm-uds/user/{userId}/subscribedServices/{subscribedServicePkid}
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Error Responses

Status Code:204

No Content

The server has completed the request and does not need to send a response body.

# Device Resources

# device

The device resource manages a user’s device information. Device supports GET and PUT methods. When the device has been associated with a user, its editable description field is set to true and can be changed by the user. See the PUT method for more detail.

If the user has entered information into the description field, it is returned with this call. Otherwise, it returns the default description as set by the administrator.

## Get device Information

The device GET method returns detailed information about a user’s device.

### Get device Information Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Get device Information Response Format

Example Response

```
<device uri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}" version= "10.0.0" hasPrimaryNumber= "true" > <id> {devicePkid} </id> <name> SEP000001000003 </name> <type> Phone </type> <description editable= "true" > Auto 100002 </description> <model> Cisco 7970 </model> <protocol> SCCP </protocol> <requireCerLocation> false </requireCerLocation> <doNotDisturbSettings> <enable> false </enable> <option value= "0" > <supportedDndOptions> <option value= "0" > Ringer Off </option> <option value= "1" > Call Reject </option> <option value= "2" > Use Common Phone Profile Setting </option> </supportedDndOptions> </option> <incomingCallAlertSetting value= "" > <supportedRingSettings> <option value= "1" > Disable </option> <option value= "2" > Flash Only </option> <option value= "5" > Beep Only </option> </supportedRingSettings> </incomingCallAlertSetting> </doNotDisturbSettings> <userGuide uri= "https://{host}/PhoneGuides/locales/en_us/PhoneOnlineGuide/7970/7970user.pdf" /> <phoneLocale uri= "https://{host}/cucm-uds/options/installedLocales" value= "1" > English, United States </phoneLocale> <extensions uri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/extensions" /> <subscribedServices uri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/subscribedServices" /> <speedDials uri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/speedDials" /> </device>
```

Refer to the example response in the right-hand panel.

## Update device Information

The device PUT method allows the user to modify the information of several options in the device. When the method completes, it returns a response with results identical those obtained with a GET Device request.

### Update device Information Request Format

```
PUT https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Update device Information Request Body

Example Request Body

```
<device> <description> description </description> <doNotDisturbSettings> <enable> true </enable> </doNotDisturbSettings> </device>
```

Refer to the example request body in the right-hand panel.

# extensions

The extensions resource returns a listing of all of the extension information about a device associated to the user. Note the following:

- Label is a field whose value is set by the user. It is not an administrator field.

- If the user has a primary extension, it is displayed first.

- For client devices, having sendToVoiceMailPilotNumber set to “true” takes precedence over the setting in callForwardAllDestination .

## extensions Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userid}/device/{devicePkid}/extensions
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

## extensions Response Format

Example Response

```
<extensions version= "10.0.0" uri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/extensions" > <extension uri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/extension/{extensionPkid}" isPrimary= "true" > <id> {extensionPkid} </id> <directoryNumber> 100002 </directoryNumber> <voiceMailPilotNumber> </voiceMailPilotNumber> <callForwardAllDestination> <sendToVoiceMailPilotNumber> true </sendToVoiceMailPilotNumber> <sendToCustomDestination> </sendToCustomDestination> </callForwardAllDestination> <messageWaitingVisualAlert> false </messageWaitingVisualAlert> <messageWaitingVisualAlertPreference value= "" > Use System Policy </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference value= "" > Default </messageWaitingAudibleAlertPreference> <onACallRingPreference value= "" > Use System Default </onACallRingPreference> <notOnACallRingPreference value= "4" > Ring </notOnACallRingPreference> <logMissedCalls> true </logMissedCalls> <label> </label> </extension> ... </extensions>
```

Refer to the example response in the right-hand panel.

# extension

The extension resource allows you to display and manage a device’s dialing and forwarding characteristics. GET and PUT methods are supported.

## Get a Device’s extension

The extension resource GET method returns information about the device’s dialling and forwarding information. It does not provide description field information–this is only accessible by the administrator.

### Get a Device’s extension Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/extension/{extensionPkid}
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Get a Device’s extension Response

Example Response

```
<extension version= "10.0.0" uri= "https://{host}/cucm-uds/user/{userId}/device/{devicePkid}/extension/{extensionPkid}" isPrimary= "true" > <id> {extensionPkid} </id> <directoryNumber> 100002 </directoryNumber> <voiceMailPilotNumber> </voiceMailPilotNumber> <callForwardAllDestination> <sendToVoiceMailPilotNumber> true </sendToVoiceMailPilotNumber> <sendToCustomDestination> </sendToCustomDestination> </callForwardAllDestination> <forwardBusyExternalCallDestination> <sendToVoiceMailPilotNumber> false </sendToVoiceMailPilotNumber> <sendToCustomDestination> </sendToCustomDestination> </forwardBusyExternalCallDestination> <forwardNoAnswerExternalCallDestination> <sendToVoiceMailPilotNumber> false </sendToVoiceMailPilotNumber> <sendToCustomDestination> </sendToCustomDestination> </forwardNoAnswerExternalCallDestination> <forwardBusyInternalCallDestination> <sendToVoiceMailPilotNumber> false </sendToVoiceMailPilotNumber> <sendToCustomDestination> </sendToCustomDestination> </forwardBusyInternalCallDestination> <forwardNoAnswerInternalCallDestination> <sendToVoiceMailPilotNumber> false </sendToVoiceMailPilotNumber> <sendToCustomDestination> </sendToCustomDestination> </forwardNoAnswerInternalCallDestination> <messageWaitingVisualAlert> false </messageWaitingVisualAlert> <messageWaitingVisualAlertPreference value= "" > <option value= "1" > Light and Prompt </option> <option value= "2" > Prompt Only </option> <option value= "3" > Light Only </option> <option value= "4" > None </option> </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference value= "" > <option value= "0" > Off </option> <option value= "1" > On </option> </messageWaitingAudibleAlertPreference> <onACallRingPreference value= "" > <option value= "1" > Disable </option> <option value= "2" > Flash Only </option> <option value= "3" > Ring Once </option> <option value= "4" > Ring </option> <option value= "5" > Beep Only </option> </onACallRingPreference> <notOnACallRingPreference value= "4" > <option value= "1" > Disable </option> <option value= "2" > Flash Only </option> <option value= "3" > Ring Once </option> <option value= "4" > Ring </option> <option value= "5" > Beep Only </option> </notOnACallRingPreference> <logMissedCalls> true </logMissedCalls> <label> </label> </extension>
```

Refer to the example response in the right-hand panel.

## Update a Device’s extension

The extension resource PUT method allows the user to modify the call forwarding characteristics of the user’s device. When the method completes, it returns a response with results identical to those obtained with a GET extension request.

All fields are optional. Sending a blank element clears the current setting for the element and restores it to a default value. Elements not specified in the request are left unchanged.

When the request specifies both sendToVoiceMailPilotNumber and destination, it updates both. However, note that sendToVoiceMailPilotNumber has higher precedence over destination in the client behavior.

### Update a Device’s extension Request Format

```
PUT https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/extension/{extensionPkid}
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Update a Device’s extension Request Body

Example Request Body

```
<extension> <callForwardAllDestination> <sendToVoiceMailPilotNumber> false </sendToVoiceMailPilotNumber> <sendToCustomDestination> 43521 </sendToCustomDestination> </callForwardAllDestination> <logMissedCalls> false </logMissedCalls> <label> label </label> <messageWaitingVisualAlertPreference> 1 </messageWaitingVisualAlertPreference> <messageWaitingAudibleAlertPreference> 1 </messageWaitingAudibleAlertPreference> <onACallRingPreference> 1 </onACallRingPreference> <notOnACallRingPreference> 1 </notOnACallRingPreference> </extension>
```

Refer to the example request body in the right-hand panel.

# speedDials

The device-specific speedDials resource manages speed dial information for a device. It supports GET , POST , and PUT methods.

## Get a Device’s speedDials

Returns a list of all of the speed dial information for a device.

### Get a Device’s speedDials Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDials
        Content-Type: application/xml
```

### Path Parameters

### Query String Parameters

User authentication required.

### Get a Device’s speedDials Response Format

Example Response

```
<speedDials totalCount= "1" uri= "https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDials" version= "{version}" > <speedDial uri= "https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDial/{speedDialPkid}" > <id> {speedDialPkid} </id> <index> 1 </index> <number> +1234567890 </number> <label> Manager </label> </speedDial> ... </speedDials>
```

Refer to the example response in the right-hand panel.

## Add speedDials to a Device

Adds speedDials for the specified device.

- Index and number parameters are required.

- Label is optional.

### Add speedDials to a Device Request Format

```
POST https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDials
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Add speedDials to a Device Request Body

Example Request Body

```
<speedDials> <speedDial> <index> 1 </index> <number> 1234 </number> <label> My Label </label> </speedDial> <speedDial> <index> 5 </index> <number> 5555 </number> <label> My Label2 </label> </speedDial> ... </speedDials>
```

Refer to the example request body in the right-hand panel.

## Update speedDials

Replaces the current speed dial list for a particular device.

### Update speedDials Request Format

```
PUT https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDials
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Update speedDials Request Body

Example Request Body

```
<speedDials> <speedDial> <index> 1 </index> <number> 1234 </number> <label> My Label </label> </speedDial> <speedDial> <index> 5 </index> <number> 5555 </number> <label> My Label2 </label> </speedDial> ... </speedDials>
```

Refer to the example request body in the right-hand panel.

# speedDial

The speedDial resource manages speed dial information for devices. It supports GET , POST , and PUT methods.

## Get a Device’s speedDial

Returns detailed information about a device’s speed dial characteristics.

### Get a Device’s speedDial Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDial/{speedDialPkid}
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Get a Device’s speedDial Response Format

Example Response

```
<speedDial uri= "https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDial/{speedDialPkid}" version= "{version}" > <id> {devicePkid} </id> <index> 1 </index> <number> 1234567890 </number> <label> Manager </label> </speedDial>
```

Refer to the example response in the right-hand panel.

## Add a New speedDial

Adds one new speedDial entry to the specified device.

### Add a New speedDial Request Format

```
POST https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDial
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Add a New speedDial Request Body

Example Request Body

```
<speedDial> <index> 2 </index> <number> 01010101 </number> <label> Home </label> </speedDial>
```

The fields index and number are required. The label field is optional. Refer to the example request body in the right-hand panel.

## Update an Existing speedDial

Updates the speedDial entry for the specified device.

### Update an Existing speedDial Request Format

```
PUT https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDial
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Update an Existing speedDial Request Body

Example Request Body

```
<speedDial> <index> 1 </index> <number> +1234567890 </number> <label> Manager </label> </speedDial>
```

The fields index and number are required. The label field is optional. If the label field is present yet empty in the request, then its value is cleared on the device.

Refer to the example request body in the right-hand panel.

### Error Responses

Status Code:204

No Content

The server has completed the request and does not need to send a response body.

Status Code:409

Conflict

This error occurs when attempting to update the speed dial’s index to an existing index.

# subscribedServices

The subscribedServices resource accesses the consolidated subscribed IP phone services for a user. If the user has different subscribed IP phone services on different devices, the response includes the URL for accessing the subscribed services for those devices. subscribedServices supports GET , POST/PUT , and DELETE methods.

## Obtain subscribedServices Information for a User’s Device

Returns a list of subscribed services for the specified device.

### Obtain subscribedServices Info for a User’s Device Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/subscribedServices
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Obtain subscribedServices Info for a User’s Device Response Format

Example Response

```
<subscribedServices uri= "https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/subscribedServices" version= "{version}" > <subscribedService uri= "https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/subscribedService/{subscribedServicePkid}" > <id> {subscribedServicePkid} </id> <name> InternalTechSupport </name> <url> http:­//{host}/GTRC/ipgtrc/servlet/GTRCService?menuname=US </url> <secureUrl/> <phoneServiceName phoneServiceId= "{phoneServicePkid}" > InternalTechSupport </phoneServiceName> </subscribedService> ... </subscribedServices>
```

Refer to the example response in the right-hand panel.

## Add subscribedServices to a Device

For the specified device, the subscribedServices POST method adds a new subscribed service to a user’s subscribedServices list.

For the specified device, the subscribedServices PUT method replaces the subscribedServices list with the specified services.

Requests can be made in two formats:

- url/secureUrl : Either a url or a secureUrl must be present in the request. subscribedServices parses any parameters from the provided provided url/secureUrl. The url/secureUrl must match the phoneService template definition.

- parameter list : The parameter pkid must match the pkid returned by a GET phoneService response.

Note: If both request format styles are present (url/secureUrl and parameter list), they must be equivalent.

### Add subscribedServices to a Device Request Format

```
POST/PUT https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/subscribedServices
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameter

User authentication required.

### Add subscribedServices to a Device Request Body

Example Request Body

The phoneServiceId is required and must exist.

- URL/secure URL format

```
<subscribedServices> <subscribedService> <name> InternalTechSupport </name> <phoneServiceId> {phoneServiceId} </phoneServiceId> <url> http:­//{host}/GTRC/ipgtrc/servlet/GTRCService?menuname=US </url> <secureUrl> https:­//{host}/GTRC/ipgtrc/servlet/GTRCService?menuname=US </secureServiceUrl> </subscribedService> <subscribedService> <name> Service2 </name> <phoneServiceId> {phoneServiceId} </phoneServiceId> <url> http:­//{host}/GTRC/ipgtrc/servlet/GTRCService?menuname=US </url> <secureUrl> https:­//{host}/GTRC/ipgtrc/servlet/GTRCService?menuname=US </secureServiceUrl> </subscribedService> ... </subscribedServices>
```

Refer to the example request body in the right-hand panel.

- Parameter list

```
<subscribedServices> <subscribedService> <name> InternalTechSupport </name> <phoneServiceId> {phoneServicePkid} </phoneServiceId> <parameters> <parameter> <paramId> {pkid} </paramId> <value> 5 </value> </parameter> ... </parameters> </subscribedService> <subscribedService> <name> Service2 </name> <phoneServiceId> {phoneServicePkid} </phoneServiceId> <parameters> <parameter> <paramId> {pkid} </paramId> <value> 5 </value> </parameter> ... </parameters> </subscribedService> ... </subscribedServices>
```

Refer to the example request body in the right-hand panel.

## Remove subscribedServices From a Device

The subscribedServices DELETE method deletes all of the subscribed services for the specified device.

### Remove subscribedServices From a Device Request Format

```
DELETE https:­//{host}:8443/cucm-uds/ser/{userId}/device/{devicePkid}/subscribedServices
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Error Responses

Status Code:204

No Content

The server has completed the request and does not need to send a response body.

# subscribedService

The subscribedService resource manages the detailed information of a subscribed IP Phone Service. subscribedService supports GET , POST , and PUT methods. The URI for accessing the subscribedService resource should be retrieved from the subscribedServices response.

## Obtain subscribedService Information

Obtain detailed information about a subscribed service.

### Obtain subscribedService Information Request Format

```
GET https:­//{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/subscribedService/{subscribedServicePkid}
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Obtain subscribedService Information Response Format

Example Response

```
<subscribedService uri= "https:­//{host}:8443/cucm-uds/user/{userId}/device/{deviceId}/subscribedService/{subscribedServiceId}" version= "{version}" > <id> {subscribedServicePkid} </id> <name> InternalTechSupport </name> <url> http:­//{host}/GTRC/ipgtrc/servlet/GTRCService?menuname=US </url> <phoneServiceName phoneServiceId= "{phoneServiceId}" > InternalTechSupport </phoneServiceName> <parameters> <parameter> <paramId> {parameterId} </paramId> <value> myval </value> <displayName> TestParam </displayName> <description> test </description> <isRequired> true|false </isRequired> <isCredential> true|false </isCredential> </parameter> ... </parameters> </subscribedService>
```

Refer to the example response in the right-hand panel.

## Add a subscribedService to a Device

The subscribedService resource creates a new subscribed service on a device.

### Add a subscribedService to a Device Request Format

```
POST https:­//{host}:8443/cucm-uds/user/{userid}/device/{deviceid}/subscribedService
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Add a subscribedService to a Device Request Body

Example Request Body

```
<subscribedService> <name> My Subscribed Service </name> <phoneServiceId> {pkid} </phoneServiceId> <parameters> <parameter> <paramId> {pkid} </paramId> <value> 5 </value> </parameter> ... </parameters> </subscribedService>
```

Fields supported for POST:

- name (required)

- phoneServiceId (required)

- serviceID

- paramId

- value

Refer to the example request body in the right-hand panel.

## Update a Device’s subscribedService

The subscribedService resource updates an existing subscribed service on a device.

Requests can be made in two formats:

- url/secureUrl: Either a url or a secureUrl must be present in the request. subscribedService parses any parameters from the provided url/secureUrl. The url/secureUrl must match the phoneService template definition.

- parameter list: The parameter pkid must match the pkid returned by a GET phoneService response.

Note: If both request format styles are present (url/secureUrl and parameter list). they must be equivalent.

### Update a Device’s subscribedService Request Format

```
PUT https:­//{host}:8443/cucm-uds/ser/{userId}/device/{devicePkid}/subscribedService/{subscribedServicePkid}
        Accept: application/xml
        Content-Type: application/xml
```

### Path Parameters

User authentication required.

### Update a Device’s subscribedService Request Body

Example Request Body

- URL/secure URL format

```
<subscribedservice> <name> My Subscribed Service </name> <url> http:­//{host}/GTRC/ipgtrc/servlet/GTRCService?menuname=US </url> <secureurl> https:­//{host}/GTRC/ipgtrc/servlet/GTRCService?menuname=US </secureurl> </subscribedservice>
```

Refer to the example request body in the right-hand panel.

- Parameter list

```
<subscribedService> <name> My Subscribed Service </name> <parameters> <parameter> <paramId> {parameterPkid} <paramId> <value> 5 </value> </parameter> ... </parameters> </subscribedService>
```

Refer to the example request body in the right-hand panel.

# DeviceToken

The devicetoken resource allows to create an device token.As an APNS customer, want to share a token with a trusted server. The Token is device centric, but it is also tied to an user. Each device can only ever have 1 user associated at a given time. When a device is created, a token entry will automatically be created for it with fkenduser set to null.

devicetoken supports PUT and DELETE methods.

### Update a devicetoken format :Device Request Format

### Path Parameters

user request

```
<token> <pushNotifyToken> ABCD12345 </pushNotifyToken> <pushChannelType> APNS/FCM </pushChannelType> <key> key1 </key> <algorithm> algorithm </algorithm> <application> application3 </application> <payloadVersion> v2 </payloadVersion> <deviceToken> EFGH12345 </deviceToken> <isCallKitDisabled> true </isCallKitDisabled> </token>
```

Responses :

Status Code : 200

Message : <rowsUpdated> : row(s) updated

Status Code : 404

Not Found

| Action | Response |
|---|---|
| GET | Requests return a 200 response if the resource is successfully retrieved. |
| POST | Requests return a 201 response if successful. Certain resources return a response that can be used to confirm that the information was added. |
| PUT | Requests return a 200 response if successful. Certain resources return a response that can be used to confirm that the information was added. |
| DELETE | Requests return a 204 response if successful. |

| Action | Response |
|---|---|
| 401 | Unauthorized Access. The client must submit authorization credentials before the request can be carried out. |
| 404 | Resource does not exist. This error occurs when the URL used in the request does not match a UDS resource. |
| 405 | The resource does not support this HTTP method. The common cause of this error is when a POST or a PUT method is attempted with a resource that only supports a GET method. |
| 409 | A conflict has occurred when attempting to carry out the request. One source of this error is when a POST method attempts to add information to the database that already exists. |
| 500 | An internal exception has occurred. |
| 503 | The server is temporarily overloaded. Please wait and try your request later. |

| Parameter | Description |
|---|---|
| username | Filter by username. https://{host}:8443/cucm-uds/clusterUser?username={userId} |
| email | Filter by email address. https://{host}:8443/cucm-uds/clusterUser?email={mailId} |
| useridentifier | Filter by user identifier. If the user is synced with Active Directory, the useridentifier value is associated with the UserPrincipleName. https://{host}:8443/cucm-uds/clusterUser?useridentifier={useridentifier} |

| Parameter | Description |
|---|---|
| {phoneServiceid} | The ID of the phone service for which you want to retrieve data. |

| Parameter | Description |
|---|---|
| name | Filter the name search using a search string that consists of a first and last name and is tokenized by whitespace. The tokenizing rules are as follows: For an input text string without spaces, the search should be performed as a ‘starting with’ search to match the user’s first name, last name, or email. When there is space detected in the input text, below is the expected behavior for search: When the search criteria contains one space, these are the rules for searching within the user name: When searching for “x y” (first starts with x AND last starts with y) OR (last starts with x AND first starts with y) OR (last starts with “x y”) OR (first starts with “x y”) When the search criteria contains two spaces, these are the rules for searching within the user name: When searching for “x y z” (first starts with x AND last starts with “y z”) OR (first starts with “x y” AND last starts with z) OR (last starts with x AND first starts with “y z”) OR (last starts with “x y” AND first starts with z) When the search criteria contains more than two spaces, only the first three sets of characters are considered as in #2. https://{host}:8443/cucm-uds/users?name=Jon |
| first | Filter the user search by the first name starting with the search string. https://{host}:8443/cucm-uds/users?first=Jon |
| last | Filter the user search by the last name starting with the search string. https://{host}:8443/cucm-uds/users?last=Smit |
| number | Filter the user search by any of the user’s telephone numbers (telephoneNumber, Home, or Mobile) starting with the search string. It ignores spaces and the characters (, ), +, and -. https://{host}:8443/cucm-uds/users?number=123 |
| numberlast | Filter the user search by the right-most digits of one of the user’s telephone numbers (telephoneNumber, Home, or Mobile). Minimum of 4 characters is recommended. It ignores spaces and the characters (, ), +, and -. https://{host}:8443/cucm-uds/users?numberlast=1234 |
| username | Filter by username. The search string must match the username exactly. Minimum of 3 characters is recommended. https://{host}:8443/cucm-uds/users?username=user1 |
| email | Filter by user’s email address. The search string must match the email address exactly. https://{host}:8443/cucm-uds/users?email=user1@test.com |
| uri | Filter by user’s msUri (OcsPrimaryUserAddress) or DirectoryURI attribute. The search string must match the URI exactly. https://{host}:8443/cucm-uds/users?uri=sampleURI |
| start | Used for pagination of displayed search results. Specifies where, in the full list of items, to start returning items. https://{host}:8443/cucm-uds/users?start=20 |
| max | Used for the pagination of displayed search results. Specifies the maximum number of user items to return. Must be less than what is specified in Enterprise Parameters, User Data Services, User Search Limit Setting. https://{host}:8443/cucm-uds/users?max=10 |

| Parameter | Description |
|---|---|
| {userid} | The ID of the user for which you want to retrieve information. |

| Parameter | Description |
|---|---|
| {userid} | The ID of the user whose information is to be modified. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose credentials are to be updated. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose credentials are to be updated. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose credentials are to be updated. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose credentials are to be updated. |

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to retrieve. |

| Parameter | Description |
|---|---|
| model | Filter list results by phone model. https:­//{host}:8443/cucm-uds/user/{userid}/devices?model="Cisco 7965" |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose extension information is to be retrieved. |

| Parameter | Description |
|---|---|
| {userId} | The user whose remote destination configuration information you want to retrieve. |

| Parameter | Description |
|---|---|
| {userId} | The user whose remote destination device information you want to retrieve. |
| {remoteDestinationPkid} | The ID of the remote destination device. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user for whom you want to add a remote destination device. |
| {remoteDestinationPkid} | The ID of the remote destination. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose remote destination information you want to update. |
| {remoteDestinationPkid} | The ID of the device. |

| Parameter | Description |
|---|---|
| {userId} | The user whose speed dial information you want to retrieve. |

| Parameter | Description |
|---|---|
| {userId} | The user whose speed dial information you want to add. |

| Parameter | Description |
|---|---|
| {userId} | The user whose speed dial information you want to update. |

| Parameter | Description |
|---|---|
| {userId} | The user whose speed dial information you want to delete. |

| Parameter | Description |
|---|---|
| index | The index for the speed dial information to be deleted on all devices owned by the user. Example: https:­//{host}:8443/cucm-uds/user/{userId}/speedDials?index=3 |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose services you want to see. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose subscribed services you want to modify. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose subscribed services you want to modify. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose subscribed services you want to delete. |
| {subscribedServicePkid} | The ID of the subscribed services you want to delete. |

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to retrieve. |
| {devicePkid} | The ID of the device. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user modifying the information. |
| {devicePkid} | The ID of the device. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose extension information is to be retrieved. |
| {devicePkid} | The ID of the device for which extension information is to be retrieved. |

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to retrieve. |
| {devicePkid} | The ID of the specific device to query for information. Use the devices resource to obtain this information. |
| {extensionPkid} | The ID of the specific extension to query for information. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user modifying the information. |
| {devicePkid} | The ID of the device whose information is to be modified. Use the device resource to obtain this information. |
| {extensionPkid} | The ID of the extension whose information is to be modified. |

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to retrieve. |
| {devicePkid} | The ID of the specific device to query for information. |

| Parameter | Description |
|---|---|
| index | Filter results by speed dial index. https:­//{host}:8443/cucm-uds/{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDials?index=7 |
| number | Filter results by the speed dial destination number. https:­//{host}:8443/cucm-uds/{host}:8443/cucm-uds/user/{userId}/device/{devicePkid}/speedDials?number=6035551234 |

| Parameter | Description |
|---|---|
| {userId} | The user whose speed dial information you want to update. |
| {devicePkid} | The ID of the specific device to update. |

| Parameter | Description |
|---|---|
| {userId} | The user whose speed dial information you want to replace. |
| {devicePkid} | The ID of the specific device to update. |

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to retrieve. |
| {devicePkid} | The ID of the specific device to query for information. |
| {speedDialPkid} | The ID of the specific speed dial storage to query for information. |

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to update. |
| {devicePkid} | The ID of the specific device requiring the update. |

| Parameter | Description |
|---|---|
| {userId} | The user whose device information you want to update. |
| {devicePkid} | The ID of the specific device requiring the update. |

| Parameter | Description |
|---|---|
| {userid} | The ID of the user whose services you want to see. |
| {devicePkid} | The ID of the device whose services you want to see. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose subscribed services you want to modify. |
| {devicePkid} | The ID of the device whose subscribed services you want to modify. |

| Parameter | Description |
|---|---|
| {userId} | The ID of the user whose subscribed services you want to delete. |
| {devicePkid} | The ID of the device whose subscribed services you want to delete. |

| Parameter | Description |
|---|---|
| {userId} | The user ID of the user whose services you want to see. |
| {devicePkid} | The ID of the device with the services. |
| {subscribedServicePkid} | The ID of the subscribed service. |

| Parameter | Description |
|---|---|
| {userid} | The user ID of the user whose services you want to see. |
| {devicePkid} | The ID of the device with the services. |

| Parameter | Description |
|---|---|
| {userid} | The user ID of the user whose services you want to see. |
| {devicePkid} | The ID of the device with the services. |
| {subscribedServicePkid} | The ID of the service to update. |

| Parameter | Description |
|---|---|
| {userid} | The ID of the user whose services you want to see. |
| {devicePkid} | The ID of the device whose services you want to see. |