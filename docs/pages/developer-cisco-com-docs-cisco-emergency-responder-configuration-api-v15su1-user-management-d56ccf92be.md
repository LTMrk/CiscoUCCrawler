---
doc_id: developer-cisco-com-docs-cisco-emergency-responder-configuration-api-v15su1-user-management-d56ccf92be
source_url: https://developer.cisco.com/docs/cisco-emergency-responder-configuration-api-v15su1/user-management/
retrieved_at: 2026-08-25T21:01:14.983322+00:00
---

# User Management

This section of API document provides all the operations that can be performed as part of User Management API in CER. This includes user, user group and user role management.

## User Management

### Fetch all users in CER

#### /user

http

```
GET https://{CER-IP}/cerappservices/service/user/
```

The /user resource retrieves all the users currently available in CER.

Response examples

XML response

xml

```
< userDetailsResponse > < status > User Details Info </ status > < users > < user > < pKid > 06bae444-79f0-34bc-0b73-042e90ad941b </ pKid > < userName > admin </ userName > < isStandard > true </ isStandard > < isRemoteAuth > 0 </ isRemoteAuth > < links > < publisherURL > https://unity-pri/cerappservices/service/user?userName=admin </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/user?userName=admin </ subscriberURL > </ links > < userGroups > < userGroup > CER Admin Utility </ userGroup > < userGroup > CER Audit Administrator </ userGroup > < userGroup > CER Serviceability </ userGroup > < userGroup > CER System Administrator </ userGroup > < userGroup > CER User </ userGroup > </ userGroups > < userRoles > < userRole > CER System Admin </ userRole > < userRole > CER Serviceability </ userRole > < userRole > CER Admin Utility </ userRole > < userRole > CER User </ userRole > < userRole > CER Audit Admin </ userRole > </ userRoles > </ user > </ users > </ userDetailsResponse >
```

JSON response

JSON

```
{ "status" : "User Details Info" , "users" : { "user" : { "pKid" : "06bae444-79f0-34bc-0b73-042e90ad941b" , "userName" : "admin" , "isStandard" : "true" , "isRemoteAuth" : "0" , "links" : { "publisherURL" : "https://cer151/cerappservices/service/user?userName=admin" , "subscriberURL" : "https://unity-sec/cerappservices/service/user?userName=admin" } , "userGroups" : { "userGroup" : [ "CER Admin Utility" , "CER Audit Administrator" , "CER Serviceability" , "CER System Administrator" , "CER User" ] } , "userRoles" : { "userRole" : [ "CER System Admin" , "CER Serviceability" , "CER Admin Utility" , "CER User" , "CER Audit Admin" ] } } } }
```

### Fetch single user in CER

#### /user?userName=admin

http

```
GET https://{CER-IP}/cerappservices/service/user?userName=admin
```

This URL retrieves details for the user mentioned in userName parameter. If user is not present, 404 Not found error is returned.

#### Path parameters

Response examples

XML response

xml

```
< userDetailsResponse > < status > User Details Info </ status > < users > < user > < pKid > 06bae444-79f0-34bc-0b73-042e90ad941b </ pKid > < userName > admin </ userName > < isStandard > true </ isStandard > < isRemoteAuth > 0 </ isRemoteAuth > < links > < publisherURL > https://unity-pri/cerappservices/service/user?userName=admin </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/user?userName=admin </ subscriberURL > </ links > < userGroups > < userGroup > CER Admin Utility </ userGroup > < userGroup > CER Audit Administrator </ userGroup > < userGroup > CER Serviceability </ userGroup > < userGroup > CER System Administrator </ userGroup > < userGroup > CER User </ userGroup > </ userGroups > < userRoles > < userRole > CER System Admin </ userRole > < userRole > CER Serviceability </ userRole > < userRole > CER Admin Utility </ userRole > < userRole > CER User </ userRole > < userRole > CER Audit Admin </ userRole > </ userRoles > </ user > </ users > </ userDetailsResponse >
```

JSON response

JSON

```
{ "status" : "User Details Info" , "users" : { "user" : { "pKid" : "06bae444-79f0-34bc-0b73-042e90ad941b" , "userName" : "admin" , "isStandard" : "true" , "isRemoteAuth" : "0" , "links" : { "publisherURL" : "https://cer151/cerappservices/service/user?userName=admin" , "subscriberURL" : "https://unity-sec/cerappservices/service/user?userName=admin" } , "userGroups" : { "userGroup" : [ "CER Admin Utility" , "CER Audit Administrator" , "CER Serviceability" , "CER System Administrator" , "CER User" ] } , "userRoles" : { "userRole" : [ "CER System Admin" , "CER Serviceability" , "CER Admin Utility" , "CER User" , "CER Audit Admin" ] } } } }
```

### Add a new user in CER

#### /user

http

```
POST https://{CER-IP}/cerappservices/service/user
```

This URL adds new user in CER. The request should be made using HTTP POST method with a body in below mentioned format. On successful insertion, a 200 OK response will be sent along with the direct url for the user in response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request examples

XML request

xml

```
< newUserRequest > < userName > {{newUser}} </ userName > < userPassword > {{newUser}} </ userPassword > < authenticationMode > Local </ authenticationMode > < ccmClusterID > </ ccmClusterID > < resetOnLogon > f </ resetOnLogon > </ newUserRequest >
```

JSON request

JSON

```
{ "userName" : "{{newUser}}" , "userPassword" : "{{newUser}}" , "authenticationMode" : "Local" , "ccmClusterID" : "" , "resetOnLogon" : "f" }
```

Response examples

XML response

xml

```
< userInsertResponse > < status > AddSuccess </ status > < pKid > 2ad17c50-bb87-479e-b757-ac7aae055807 </ pKid > < links > < publisherURL > https: //unity-pri/cerappservices/service/user?userName=TestUserCERTeamLocal_662 </ publisherURL > < subscriberURL > https: //cucm207/cerappservices/service/user?userName=TestUserCERTeamLocal_662 </ subscriberURL > </ links > </ userInsertResponse >
```

JSON response

JSON

```
{ "status" : "AddSuccess" , "pKid" : "f684e35b-5fb7-45d5-8310-6b3531e0d974" , "links" : { "publisherURL" : "https://cer151/cerappservices/service/user?userName=TestUserCERTeamLocal_889" , "subscriberURL" : "https://unity-sec/cerappservices/service/user?userName=TestUserCERTeamLocal_889" } }
```

### Update an existing user in CER

#### /user

http

```
PUT https://{CER-IP}/cerappservices/service/user
```

This URL updates an existing user in CER. The request should be made using HTTP PUT method with a body in below mentioned format. On successful insertion, a 200 OK response will be sent along with the direct url for the user in response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request examples

XML request

xml

```
< updateUserRequest > < userName > {{newUser}} </ userName > < userPassword > TestUserCERTeamLocal_178 </ userPassword > < authenticationMode > Local </ authenticationMode > < ccmClusterID > 10.77.34.169 </ ccmClusterID > < resetOnLogon > f </ resetOnLogon > </ updateUserRequest >
```

JSON request

JSON

```
{ "userName" : "{{newUser}}" , "userPassword" : "{{newUser}}" , "authenticationMode" : "Local" , "ccmClusterID" : "" , "resetOnLogon" : "f" }
```

Response examples

XML response

xml

```
< userUpdateResponse > < status > UpdateSuccess </ status > < pKid > f684e35b-5fb7-45d5-8310-6b3531e0d974 </ pKid > < links > < href > https://cer151/cerappservices/service/user?userName=TestUserCERTeamLocal_889 </ href > < href > https://unity-sec/cerappservices/service/user?userName=TestUserCERTeamLocal_889 </ href > </ links > </ userUpdateResponse >
```

JSON response

JSON

```
{ "status" : "UpdateSuccess" , "pKid" : "f684e35b-5fb7-45d5-8310-6b3531e0d974" , "links" : { "href" : [ "https://cer151/cerappservices/service/user?userName=TestUserCERTeamLocal_889%20" , "https://unity-sec/cerappservices/service/user?userName=TestUserCERTeamLocal_889%20" ] } }
```

### Delete list of users in CER

#### /user

http

```
DELETE https://{CER-IP}/cerappservices/service/user/
```

This URL deletes a list of existing users in CER. The request should be made using HTTP DELETE method with a body in below mentioned format. On successful deletion, a 200 OK response will be sent along with appropriate status, message for the respective user in response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request examples

XML request

xml

```
< deleteAppUserRequest > < users > < name > AdMiN </ name > < name > TestUserCERTeamLocal_301 </ name > < name > TestUserCERTeamLocal_49 </ name > </ users > </ deleteAppUserRequest >
```

JSON request

JSON

```
{ "users" : { "name" : [ "AdMiN" , "TestUserCERTeamLocal_301" , "TestUserCERTeamLocal_49" ] } }
```

Response examples

XML response

xml

```
< deleteAppUserResponse > < status > Some User(s) Deletion was not successful </ status > < users > < user > < name > AdMiN </ name > < status > Failure </ status > < message > Cannot delete standard user AdMiN </ message > </ user > < user > < name > TestUserCERTeamLocal_301 </ name > < status > Failure </ status > < message > Failed to read TestUserCERTeamLocal_301 from database </ message > </ user > < user > < name > TestUserCERTeamLocal_49 </ name > < status > Failure </ status > < message > Failed to read TestUserCERTeamLocal_49 from database </ message > </ user > </ users > </ deleteAppUserResponse >
```

JSON response

JSON

```
{ "status" : "Some User(s) Deletion was not successful" , "users" : { "user" : [ { "name" : "AdMiN" , "status" : "Failure" , "message" : "Cannot delete standard user AdMiN" } , { "name" : "TestUserCERTeamLocal_301" , "status" : "Failure" , "message" : "Failed to read TestUserCERTeamLocal_301 from database " } , { "name" : "TestUserCERTeamLocal_49" , "status" : "Failure" , "message" : "Failed to read TestUserCERTeamLocal_49 from database " } ] } }
```

### Delete single user in CER

#### /user?userName=admin

http

```
DELETE https://{CER-IP}/cerappservices/service/user?userName=admin
```

This URL deletes an existing CER user as mentioned in userName parameter. On successful deletion, a 200 OK response will be sent along with appropriate status, message for the respective user in response. In case of failure appropriate message will be present in the status field with relevant HTTP return code.

#### Path parameters

Response examples

XML response

xml

```
< deleteAppUserResponse > < status > Some User(s) Deletion was not successful </ status > < users > < user > < name > AdMiN </ name > < status > Failure </ status > < message > Cannot delete standard user AdMiN </ message > </ user > </ users > </ deleteAppUserResponse >
```

JSON response

JSON

```
{ "status" : "Some User(s) Deletion was not successful" , "users" : { "user" : { "name" : "admin" , "status" : "Failure" , "message" : "Cannot delete standard user admin" } } }
```

## User Role Management

### Fetch all user roles in CER

#### /userrole

http

```
GET https://{CER-IP}/cerappservices/service/userrole
```

The /userrole resource retrieves all the user roles currently available in CER.

Response examples

XML response

xml

```
< userRoleDetailsResponse > < status > User Role Details Info </ status > < userRoles > < userRole > < pKid > e42580ba-bd7b-4811-98d6-7e148515ee0a </ pKid > < roleName > CER System Admin </ roleName > < description > All System Configurations </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20System%20Admin </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=CER%20System%20Admin </ subscriberURL > </ links > < resourcePermissions > < resourcePermission > Access Point </ resourcePermission > < resourcePermission > Add Subscriber </ resourcePermission > < resourcePermission > ALI Formatting Tool </ resourcePermission > < resourcePermission > Call History </ resourcePermission > < resourcePermission > Call Manager Details </ resourcePermission > < resourcePermission > CER Groups in Cluster </ resourcePermission > < resourcePermission > Device Snmp Settings </ resourcePermission > < resourcePermission > ERL </ resourcePermission > < resourcePermission > ERL Audit Trail </ resourcePermission > < resourcePermission > ERL Debug Tool </ resourcePermission > < resourcePermission > ERL Migration </ resourcePermission > < resourcePermission > File Management Utility </ resourcePermission > < resourcePermission > Functional role </ resourcePermission > < resourcePermission > Intrado ERL </ resourcePermission > < resourcePermission > IP Subnet </ resourcePermission > < resourcePermission > License Management </ resourcePermission > < resourcePermission > Mail Alert Configurations </ resourcePermission > < resourcePermission > Manually Configured Phones </ resourcePermission > < resourcePermission > Off-Premises ERL </ resourcePermission > < resourcePermission > OnsiteContact </ resourcePermission > < resourcePermission > Pager and Email Alert Configurations </ resourcePermission > < resourcePermission > PS ALI Convert </ resourcePermission > < resourcePermission > PS ALI Export </ resourcePermission > < resourcePermission > Purge </ resourcePermission > < resourcePermission > Run Tracking </ resourcePermission > < resourcePermission > Saml Sso </ resourcePermission > < resourcePermission > Tracking Schedule </ resourcePermission > < resourcePermission > Server </ resourcePermission > < resourcePermission > Server Group </ resourcePermission > < resourcePermission > LAN Switches </ resourcePermission > < resourcePermission > Switch Port </ resourcePermission > < resourcePermission > Synthetic Phone </ resourcePermission > < resourcePermission > Telephony </ resourcePermission > < resourcePermission > Unlocated Phones </ resourcePermission > < resourcePermission > Application User </ resourcePermission > < resourcePermission > User Setting </ resourcePermission > < resourcePermission > User Group </ resourcePermission > < resourcePermission > Intrado VUI Settings </ resourcePermission > </ resourcePermissions > </ userRole > < userRole > < pKid > 40a64db9-4dfe-46ad-b8da-044ba68a521e </ pKid > < roleName > CER ERL Admin </ roleName > < description > ERL Configurations </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20ERL%20Admin </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=CER%20ERL%20Admin </ subscriberURL > </ links > < resourcePermissions > < resourcePermission > ERL </ resourcePermission > < resourcePermission > IP Subnet </ resourcePermission > < resourcePermission > Manually Configured Phones </ resourcePermission > < resourcePermission > OnsiteContact </ resourcePermission > < resourcePermission > Switch Port </ resourcePermission > < resourcePermission > Synthetic Phone </ resourcePermission > < resourcePermission > Unlocated Phones </ resourcePermission > </ resourcePermissions > </ userRole > < userRole > < pKid > 8aca4d79-cbf2-40ec-8785-1fe7f7afc004 </ pKid > < roleName > CER Network Admin </ roleName > < description > Network Configurations </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20Network%20Admin </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=CER%20Network%20Admin </ subscriberURL > </ links > < resourcePermissions > < resourcePermission > Call Manager Details </ resourcePermission > < resourcePermission > Device Snmp Settings </ resourcePermission > < resourcePermission > Run Tracking </ resourcePermission > < resourcePermission > Tracking Schedule </ resourcePermission > < resourcePermission > LAN Switches </ resourcePermission > </ resourcePermissions > </ userRole > < userRole > < pKid > 3c7b4c98-6b3d-4a7f-8504-5a56a011619c </ pKid > < roleName > CER Serviceability </ roleName > < description > Serviceability Pages </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20Serviceability </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=CER%20Serviceability </ subscriberURL > </ links > < resourcePermissions > < resourcePermission > All Logs </ resourcePermission > < resourcePermission > Control Centre </ resourcePermission > < resourcePermission > CPU &amp; Memory Usage </ resourcePermission > < resourcePermission > Disk Usage </ resourcePermission > < resourcePermission > Event Viewer </ resourcePermission > < resourcePermission > Processes </ resourcePermission > < resourcePermission > MIB2 system group configuration </ resourcePermission > < resourcePermission > SNMP V1/V2c configuration </ resourcePermission > < resourcePermission > SNMP v3 configuration </ resourcePermission > </ resourcePermissions > </ userRole > < userRole > < pKid > ef706d90-85ad-490c-ae7d-1b9f860d1d52 </ pKid > < roleName > CER Admin Utility </ roleName > < description > Admin utility Pages </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20Admin%20Utility </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=CER%20Admin%20Utility </ subscriberURL > </ links > < resourcePermissions > < resourcePermission > Cluster DB Host setting </ resourcePermission > < resourcePermission > Change CCM Version </ resourcePermission > </ resourcePermissions > </ userRole > < userRole > < pKid > 9662de2c-907a-44d2-ac23-c2dedb4e818f </ pKid > < roleName > CER User </ roleName > < description > Security User Pages </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20User </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=CER%20User </ subscriberURL > </ links > < resourcePermissions > < resourcePermission > Phone Search </ resourcePermission > < resourcePermission > User Call History </ resourcePermission > < resourcePermission > Web Alert </ resourcePermission > </ resourcePermissions > </ userRole > < userRole > < pKid > f5abe25f-432c-445d-8f0e-5a74c2ed7e25 </ pKid > < roleName > CER Audit Admin </ roleName > < description > Audit page in serviceability </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20Audit%20Admin </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=CER%20Audit%20Admin </ subscriberURL > </ links > < resourcePermissions > < resourcePermission > Audit Log Configuration </ resourcePermission > </ resourcePermissions > </ userRole > </ userRoles > </ userRoleDetailsResponse >
```

JSON response

JSON

```
{ "status" : "User Role Details Info" , "userRoles" : { "userRole" : [ { "pKid" : "e42580ba-bd7b-4811-98d6-7e148515ee0a" , "roleName" : "CER System Admin" , "description" : "All System Configurations" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20System%20Admin" , "subscriberURL" : "https://cucm207/cerappservices/service/userrole?userRoleName=CER%20System%20Admin" } , "resourcePermissions" : { "resourcePermission" : [ "Access Point" , "Add Subscriber" , "ALI Formatting Tool" , "Call History" , "Call Manager Details" , "CER Groups in Cluster" , "Device Snmp Settings" , "ERL" , "ERL Audit Trail" , "ERL Debug Tool" , "ERL Migration" , "File Management Utility" , "Functional role" , "Intrado ERL" , "IP Subnet" , "License Management" , "Mail Alert Configurations" , "Manually Configured Phones" , "Off-Premises ERL" , "OnsiteContact" , "Pager and Email Alert Configurations" , "PS ALI Convert" , "PS ALI Export" , "Purge" , "Run Tracking" , "Saml Sso" , "Tracking Schedule" , "Server" , "Server Group" , "LAN Switches" , "Switch Port" , "Synthetic Phone" , "Telephony" , "Unlocated Phones" , "Application User" , "User Setting" , "User Group" , "Intrado VUI Settings" ] } } , { "pKid" : "40a64db9-4dfe-46ad-b8da-044ba68a521e" , "roleName" : "CER ERL Admin" , "description" : "ERL Configurations" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20ERL%20Admin" , "subscriberURL" : "https://cucm207/cerappservices/service/userrole?userRoleName=CER%20ERL%20Admin" } , "resourcePermissions" : { "resourcePermission" : [ "ERL" , "IP Subnet" , "Manually Configured Phones" , "OnsiteContact" , "Switch Port" , "Synthetic Phone" , "Unlocated Phones" ] } } , { "pKid" : "8aca4d79-cbf2-40ec-8785-1fe7f7afc004" , "roleName" : "CER Network Admin" , "description" : "Network Configurations" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20Network%20Admin" , "subscriberURL" : "https://cucm207/cerappservices/service/userrole?userRoleName=CER%20Network%20Admin" } , "resourcePermissions" : { "resourcePermission" : [ "Call Manager Details" , "Device Snmp Settings" , "Run Tracking" , "Tracking Schedule" , "LAN Switches" ] } } , { "pKid" : "3c7b4c98-6b3d-4a7f-8504-5a56a011619c" , "roleName" : "CER Serviceability" , "description" : "Serviceability Pages" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20Serviceability" , "subscriberURL" : "https://cucm207/cerappservices/service/userrole?userRoleName=CER%20Serviceability" } , "resourcePermissions" : { "resourcePermission" : [ "All Logs" , "Control Centre" , "CPU & Memory Usage" , "Disk Usage" , "Event Viewer" , "Processes" , "MIB2 system group configuration" , "SNMP V1/V2c configuration" , "SNMP v3 configuration" ] } } , { "pKid" : "ef706d90-85ad-490c-ae7d-1b9f860d1d52" , "roleName" : "CER Admin Utility" , "description" : "Admin utility Pages" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20Admin%20Utility" , "subscriberURL" : "https://cucm207/cerappservices/service/userrole?userRoleName=CER%20Admin%20Utility" } , "resourcePermissions" : { "resourcePermission" : [ "Cluster DB Host setting" , "Change CCM Version" ] } } , { "pKid" : "9662de2c-907a-44d2-ac23-c2dedb4e818f" , "roleName" : "CER User" , "description" : "Security User Pages" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20User" , "subscriberURL" : "https://cucm207/cerappservices/service/userrole?userRoleName=CER%20User" } , "resourcePermissions" : { "resourcePermission" : [ "Phone Search" , "User Call History" , "Web Alert" ] } } , { "pKid" : "f5abe25f-432c-445d-8f0e-5a74c2ed7e25" , "roleName" : "CER Audit Admin" , "description" : "Audit page in serviceability" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/userrole?userRoleName=CER%20Audit%20Admin" , "subscriberURL" : "https://cucm207/cerappservices/service/userrole?userRoleName=CER%20Audit%20Admin" } , "resourcePermissions" : { "resourcePermission" : "Audit Log Configuration" } } ] } }
```

### Fetch single user role in CER

#### /userrole?userRoleName=CER%20System%20Admin

http

```
GET https://{CER-IP}/cerappservices/service/userrole?userRoleName=CER%20System%20Admin
```

This URL retrieves details for the user role mentioned in userRoleName parameter. If user role is not present, 404 Not found error is returned.

#### Path parameters

Response examples

XML response

xml

```
< userRoleDetailsResponse > < status > User Role Details Info </ status > < userRoles > < userRole > < pKid > de4ad40d-dc89-4580-a8e3-99deec1a67d5 </ pKid > < roleName > CER System Admin </ roleName > < description > All System Configurations </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://cer151/cerappservices/service/userrole?userRoleName=CER%20System%20Admin </ publisherURL > < subscriberURL > https://unity-sec/cerappservices/service/userrole?userRoleName=CER%20System%20Admin </ subscriberURL > </ links > < resourcePermissions > < resourcePermission > Access Point </ resourcePermission > < resourcePermission > Add Subscriber </ resourcePermission > < resourcePermission > ALI Formatting Tool </ resourcePermission > < resourcePermission > Call History </ resourcePermission > < resourcePermission > Call Manager Details </ resourcePermission > < resourcePermission > CER Groups in Cluster </ resourcePermission > < resourcePermission > Device Snmp Settings </ resourcePermission > < resourcePermission > ERL </ resourcePermission > < resourcePermission > ERL Audit Trail </ resourcePermission > < resourcePermission > ERL Debug Tool </ resourcePermission > < resourcePermission > ERL Migration </ resourcePermission > < resourcePermission > File Management Utility </ resourcePermission > < resourcePermission > Functional role </ resourcePermission > < resourcePermission > Intrado ERL </ resourcePermission > < resourcePermission > IP Subnet </ resourcePermission > < resourcePermission > License Management </ resourcePermission > < resourcePermission > Mail Alert Configurations </ resourcePermission > < resourcePermission > Manually Configured Phones </ resourcePermission > < resourcePermission > Off-Premises ERL </ resourcePermission > < resourcePermission > OnsiteContact </ resourcePermission > < resourcePermission > Pager and Email Alert Configurations </ resourcePermission > < resourcePermission > PS ALI Convert </ resourcePermission > < resourcePermission > PS ALI Export </ resourcePermission > < resourcePermission > Purge </ resourcePermission > < resourcePermission > Run Tracking </ resourcePermission > < resourcePermission > Saml Sso </ resourcePermission > < resourcePermission > Tracking Schedule </ resourcePermission > < resourcePermission > Server </ resourcePermission > < resourcePermission > Server Group </ resourcePermission > < resourcePermission > LAN Switches </ resourcePermission > < resourcePermission > Switch Port </ resourcePermission > < resourcePermission > Synthetic Phone </ resourcePermission > < resourcePermission > Telephony </ resourcePermission > < resourcePermission > Unlocated Phones </ resourcePermission > < resourcePermission > Application User </ resourcePermission > < resourcePermission > User Setting </ resourcePermission > < resourcePermission > User Group </ resourcePermission > < resourcePermission > Intrado VUI Settings </ resourcePermission > </ resourcePermissions > </ userRole > </ userRoles > </ userRoleDetailsResponse >
```

JSON response

JSON

```
{ "status" : "User Role Details Info" , "userRoles" : { "userRole" : { "pKid" : "de4ad40d-dc89-4580-a8e3-99deec1a67d5" , "roleName" : "CER System Admin" , "description" : "All System Configurations" , "isStandard" : "true" , "links" : { "publisherURL" : "https://cer151/cerappservices/service/userrole?userRoleName=CER%20System%20Admin" , "subscriberURL" : "https://unity-sec/cerappservices/service/userrole?userRoleName=CER%20System%20Admin" } , "resourcePermissions" : { "resourcePermission" : [ "Access Point" , "Add Subscriber" , "ALI Formatting Tool" , "Call History" , "Call Manager Details" , "CER Groups in Cluster" , "Device Snmp Settings" , "ERL" , "ERL Audit Trail" , "ERL Debug Tool" , "ERL Migration" , "File Management Utility" , "Functional role" , "Intrado ERL" , "IP Subnet" , "License Management" , "Mail Alert Configurations" , "Manually Configured Phones" , "Off-Premises ERL" , "OnsiteContact" , "Pager and Email Alert Configurations" , "PS ALI Convert" , "PS ALI Export" , "Purge" , "Run Tracking" , "Saml Sso" , "Tracking Schedule" , "Server" , "Server Group" , "LAN Switches" , "Switch Port" , "Synthetic Phone" , "Telephony" , "Unlocated Phones" , "Application User" , "User Setting" , "User Group" , "Intrado VUI Settings" ] } } } }
```

### Add a new user role in CER

#### /userrole

http

```
POST https://{CER-IP}/cerappservices/service/userrole/
```

This URL adds an admin user defined role in CER. The request should be made using HTTP POST method with a body in below mentioned format. On successful insertion, a 200 OK response will be sent along with the direct url for the role in response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request examples

XML request

xml

```
< insertUserRoleRequest > < name > {{newUserRole}} </ name > < selectAllResourceGroups > y </ selectAllResourceGroups > < desc > {{newUserRole}} </ desc > < CERAdminUtility > < ClusterDBHostsetting > </ ClusterDBHostsetting > < ChangeCCMVersion > </ ChangeCCMVersion > </ CERAdminUtility > < CERAuditAdministrator > < AuditLogConfiguration > </ AuditLogConfiguration > </ CERAuditAdministrator > < CERServiceability > < AllLogs > </ AllLogs > < ControlCentre > </ ControlCentre > < CPUMemoryUsage > </ CPUMemoryUsage > < DiskUsage > </ DiskUsage > < EventViewer > </ EventViewer > < Processes > </ Processes > < MIB2systemgroupconfiguration > </ MIB2systemgroupconfiguration > < SNMPV1V2configuration > </ SNMPV1V2configuration > < SNMPv3configuration > </ SNMPv3configuration > </ CERServiceability > < CERSystemAdministrator > < AccessPoint > </ AccessPoint > < AddSubscriber > </ AddSubscriber > < ALIFormattingTool > </ ALIFormattingTool > < CallHistory > </ CallHistory > < CallManagerDetails > </ CallManagerDetails > < CERGroupsinCluster > </ CERGroupsinCluster > < DeviceSnmpSettings > </ DeviceSnmpSettings > < ERL > </ ERL > < ERLAuditTrail > </ ERLAuditTrail > < ERLDebugTool > </ ERLDebugTool > < ERLMigration > </ ERLMigration > < FileManagementUtility > </ FileManagementUtility > < Functionalrole > </ Functionalrole > < IntradoERL > </ IntradoERL > < IPSubnet > </ IPSubnet > < LicenseManagement > </ LicenseManagement > < MailAlertConfigurations > </ MailAlertConfigurations > < ManuallyConfiguredPhones > </ ManuallyConfiguredPhones > < OffPremisesERL > </ OffPremisesERL > < OnsiteContact > </ OnsiteContact > < PagerandEmailAlertConfigurations > </ PagerandEmailAlertConfigurations > < PSALIConvert > </ PSALIConvert > < PSALIExport > </ PSALIExport > < Purge > </ Purge > < RunTracking > </ RunTracking > < SamlSso > </ SamlSso > < TrackingSchedule > </ TrackingSchedule > < Server > </ Server > < ServerGroup > </ ServerGroup > < LANSwitches > </ LANSwitches > < SwitchPort > </ SwitchPort > < SyntheticPhone > </ SyntheticPhone > < Telephony > </ Telephony > < UnlocatedPhones > </ UnlocatedPhones > < ApplicationUser > </ ApplicationUser > < UserSetting > </ UserSetting > < UserGroup > </ UserGroup > < IntradoVUISettings > </ IntradoVUISettings > </ CERSystemAdministrator > < CERUser > < PhoneSearch > </ PhoneSearch > < UserCallHistory > </ UserCallHistory > < WebAlert > </ WebAlert > </ CERUser > </ insertUserRoleRequest >
```

JSON request

JSON

```
{ "name" : "{{newUserRole}}" , "selectAllResourceGroups" : "y" , "desc" : "{{newUserRole}}" , "CERAdminUtility" : { "ClusterDBHostsetting" : "y" , "ChangeCCMVersion" : "" } , "CERAuditAdministrator" : { "AuditLogConfiguration" : "" } , "CERServiceability" : { "AllLogs" : "" , "ControlCentre" : "" , "CPUMemoryUsage" : "" , "DiskUsage" : "" , "EventViewer" : "" , "Processes" : "" , "MIB2systemgroupconfiguration" : "" , "SNMPV1V2configuration" : "ty" , "SNMPv3configuration" : "" } , "CERSystemAdministrator" : { "AccessPoint" : "ysfgsgdt" , "AddSubscriber" : "" , "ALIFormattingTool" : "" , "CallHistory" : "" , "CallManagerDetails" : "" , "CERGroupsinCluster" : "" , "DeviceSnmpSettings" : "" , "ERL" : "" , "ERLAuditTrail" : "" , "ERLDebugTool" : "" , "ERLMigration" : "" , "FileManagementUtility" : "" , "Functionalrole" : "" , "IntradoERL" : "" , "IPSubnet" : "" , "LicenseManagement" : "" , "MailAlertConfigurations" : "" , "ManuallyConfiguredPhones" : "" , "OffPremisesERL" : "" , "OnsiteContact" : "" , "PagerandEmailAlertConfigurations" : "" , "PSALIConvert" : "" , "PSALIExport" : "" , "Purge" : "" , "RunTracking" : "" , "SamlSso" : "" , "TrackingSchedule" : "" , "Server" : "" , "ServerGroup" : "" , "LANSwitches" : "" , "SwitchPort" : "" , "SyntheticPhone" : "" , "Telephony" : "" , "UnlocatedPhones" : "" , "ApplicationUser" : "" , "UserSetting" : "" , "UserGroup" : "" , "IntradoVUISettings" : "" } , "CERUser" : { "PhoneSearch" : "" , "UserCallHistory" : "" , "WebAlert" : "" } }
```

Notes:

- For all the permission fields the accepted value is "Y" or "y". All values otherwise are considered as false/not selected.

- A user role with standard role name cannot be created.

Response examples

XML response

xml

```
< insertUserRoleResponse > < status > Success </ status > < message > Added role 'TestUserRole_171' with description 'TestUserRole_171' and Resource Permissions '[Cluster DB Host setting, Change CCM Version, Audit Log Configuration, All Logs, Control Centre, CPU &amp; Memory Usage, Disk Usage, Event Viewer, Processes, MIB2 system group configuration, SNMP V1/V2c configuration, SNMP v3 configuration, Access Point, Add Subscriber, ALI Formatting Tool, Call History, Call Manager Details, CER Groups in Cluster, Device Snmp Settings, ERL, ERL Audit Trail, ERL Debug Tool, ERL Migration, File Management Utility, Functional role, Intrado ERL, IP Subnet, License Management, Mail Alert Configurations, Manually Configured Phones, Off-Premises ERL, OnsiteContact, Pager and Email Alert Configurations, PS ALI Convert, PS ALI Export, Purge, Run Tracking, Saml Sso, Tracking Schedule, Server, Server Group, LAN Switches, Switch Port, Synthetic Phone, Telephony, Unlocated Phones, Application User, User Setting, User Group, Intrado VUI Settings, Phone Search, User Call History, Web Alert]' </ message > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=TestUserRole_171 </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=TestUserRole_171 </ subscriberURL > </ links > </ insertUserRoleResponse >
```

JSON response

JSON

```
{ "status" : "Success" , "message" : "Added role 'TestUserRole_919' with description 'TestUserRole_919' and Resource Permissions '[Cluster DB Host setting, Change CCM Version, Audit Log Configuration, All Logs, Control Centre, CPU & Memory Usage, Disk Usage, Event Viewer, Processes, MIB2 system group configuration, SNMP V1/V2c configuration, SNMP v3 configuration, Access Point, Add Subscriber, ALI Formatting Tool, Call History, Call Manager Details, CER Groups in Cluster, Device Snmp Settings, ERL, ERL Audit Trail, ERL Debug Tool, ERL Migration, File Management Utility, Functional role, Intrado ERL, IP Subnet, License Management, Mail Alert Configurations, Manually Configured Phones, Off-Premises ERL, OnsiteContact, Pager and Email Alert Configurations, PS ALI Convert, PS ALI Export, Purge, Run Tracking, Saml Sso, Tracking Schedule, Server, Server Group, LAN Switches, Switch Port, Synthetic Phone, Telephony, Unlocated Phones, Application User, User Setting, User Group, Intrado VUI Settings, Phone Search, User Call History, Web Alert]'" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/userrole?userRoleName=TestUserRole_919" , "subscriberURL" : "https://cucm207/cerappservices/service/userrole?userRoleName=TestUserRole_919" } }
```

### Update existing user role in CER

#### /userrole

http

```
PUT https://{CER-IP}/cerappservices/service/userrole/
```

This URL updates an existing user role in CER. The request should be made using HTTP PUT method with a body in below mentioned format. On successful insertion, a 200 OK response will be sent along with the direct url for the user role in response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request examples

XML request

xml

```
< updateUserRoleRequest > < name > TestUserRole_171 </ name > < selectAllResourceGroups > </ selectAllResourceGroups > < desc > new desc 1 </ desc > < CERAdminUtility > < ClusterDBHostsetting > </ ClusterDBHostsetting > < ChangeCCMVersion > </ ChangeCCMVersion > </ CERAdminUtility > < CERAuditAdministrator > < AuditLogConfiguration > </ AuditLogConfiguration > </ CERAuditAdministrator > < CERServiceability > < AllLogs > </ AllLogs > < ControlCentre > </ ControlCentre > < CPUMemoryUsage > </ CPUMemoryUsage > < DiskUsage > </ DiskUsage > < EventViewer > </ EventViewer > < Processes > </ Processes > < MIB2systemgroupconfiguration > </ MIB2systemgroupconfiguration > < SNMPV1V2configuration > </ SNMPV1V2configuration > < SNMPv3configuration > </ SNMPv3configuration > </ CERServiceability > < CERSystemAdministrator > < AccessPoint > </ AccessPoint > < AddSubscriber > </ AddSubscriber > < ALIFormattingTool > </ ALIFormattingTool > < CallHistory > </ CallHistory > < CallManagerDetails > </ CallManagerDetails > < CERGroupsinCluster > </ CERGroupsinCluster > < DeviceSnmpSettings > </ DeviceSnmpSettings > < ERL > </ ERL > < ERLAuditTrail > </ ERLAuditTrail > < ERLDebugTool > </ ERLDebugTool > < ERLMigration > </ ERLMigration > < FileManagementUtility > </ FileManagementUtility > < Functionalrole > </ Functionalrole > < IntradoERL > </ IntradoERL > < IPSubnet > </ IPSubnet > < LicenseManagement > </ LicenseManagement > < MailAlertConfigurations > </ MailAlertConfigurations > < ManuallyConfiguredPhones > </ ManuallyConfiguredPhones > < OffPremisesERL > </ OffPremisesERL > < OnsiteContact > </ OnsiteContact > < PagerandEmailAlertConfigurations > </ PagerandEmailAlertConfigurations > < PSALIConvert > </ PSALIConvert > < PSALIExport > </ PSALIExport > < Purge > </ Purge > < RunTracking > </ RunTracking > < SamlSso > </ SamlSso > < TrackingSchedule > </ TrackingSchedule > < Server > </ Server > < ServerGroup > </ ServerGroup > < LANSwitches > </ LANSwitches > < SwitchPort > </ SwitchPort > < SyntheticPhone > </ SyntheticPhone > < Telephony > </ Telephony > < UnlocatedPhones > </ UnlocatedPhones > < ApplicationUser > </ ApplicationUser > < UserSetting > </ UserSetting > < UserGroup > </ UserGroup > < IntradoVUISettings > </ IntradoVUISettings > </ CERSystemAdministrator > < CERUser > < PhoneSearch > </ PhoneSearch > < UserCallHistory > </ UserCallHistory > < WebAlert > </ WebAlert > </ CERUser > </ updateUserRoleRequest >
```

JSON request

JSON

```
{ "name" : "{{newUserRole}}" , "selectAllResourceGroups" : "y" , "desc" : "{{newUserRole}}" , "CERAdminUtility" : { "ClusterDBHostsetting" : "" , "ChangeCCMVersion" : "" } , "CERAuditAdministrator" : { "AuditLogConfiguration" : "" } , "CERServiceability" : { "AllLogs" : "" , "ControlCentre" : "" , "CPUMemoryUsage" : "" , "DiskUsage" : "" , "EventViewer" : "" , "Processes" : "" , "MIB2systemgroupconfiguration" : "" , "SNMPV1V2configuration" : "" , "SNMPv3configuration" : "" } , "CERSystemAdministrator" : { "AccessPoint" : "" , "AddSubscriber" : "" , "ALIFormattingTool" : "" , "CallHistory" : "" , "CallManagerDetails" : "" , "CERGroupsinCluster" : "" , "DeviceSnmpSettings" : "" , "ERL" : "" , "ERLAuditTrail" : "" , "ERLDebugTool" : "" , "ERLMigration" : "" , "FileManagementUtility" : "" , "Functionalrole" : "" , "IntradoERL" : "" , "IPSubnet" : "" , "LicenseManagement" : "" , "MailAlertConfigurations" : "" , "ManuallyConfiguredPhones" : "" , "OffPremisesERL" : "" , "OnsiteContact" : "" , "PagerandEmailAlertConfigurations" : "" , "PSALIConvert" : "" , "PSALIExport" : "" , "Purge" : "" , "RunTracking" : "" , "SamlSso" : "" , "TrackingSchedule" : "" , "Server" : "" , "ServerGroup" : "" , "LANSwitches" : "" , "SwitchPort" : "" , "SyntheticPhone" : "" , "Telephony" : "" , "UnlocatedPhones" : "" , "ApplicationUser" : "" , "UserSetting" : "" , "UserGroup" : "" , "IntradoVUISettings" : "" } , "CERUser" : { "PhoneSearch" : "" , "UserCallHistory" : "" , "WebAlert" : "" } }
```

Notes:

- For all the permission fields the accepted value is "Y" or "y". All values otherwise are considered as false/not selected.

- A standard user role permissions cannot be modified.

Response examples

XML response

xml

```
< updateUserRoleResponse > < status > Success </ status > < message > Update Successful for role TestUserRole_171 </ message > < changeRequested > < from > < description > TestUserRole_171 </ description > < resource > < resourcePermission > Access Point </ resourcePermission > < resourcePermission > Add Subscriber </ resourcePermission > < resourcePermission > ALI Formatting Tool </ resourcePermission > < resourcePermission > All Logs </ resourcePermission > < resourcePermission > Audit Log Configuration </ resourcePermission > < resourcePermission > Call History </ resourcePermission > < resourcePermission > Call Manager Details </ resourcePermission > < resourcePermission > CER Groups in Cluster </ resourcePermission > < resourcePermission > Cluster DB Host setting </ resourcePermission > < resourcePermission > Control Centre </ resourcePermission > < resourcePermission > CPU &amp; Memory Usage </ resourcePermission > < resourcePermission > Device Snmp Settings </ resourcePermission > < resourcePermission > Disk Usage </ resourcePermission > < resourcePermission > ERL </ resourcePermission > < resourcePermission > ERL Audit Trail </ resourcePermission > < resourcePermission > ERL Debug Tool </ resourcePermission > < resourcePermission > ERL Migration </ resourcePermission > < resourcePermission > Event Viewer </ resourcePermission > < resourcePermission > File Management Utility </ resourcePermission > < resourcePermission > Functional role </ resourcePermission > < resourcePermission > Intrado ERL </ resourcePermission > < resourcePermission > IP Subnet </ resourcePermission > < resourcePermission > License Management </ resourcePermission > < resourcePermission > Mail Alert Configurations </ resourcePermission > < resourcePermission > Manually Configured Phones </ resourcePermission > < resourcePermission > Change CCM Version </ resourcePermission > < resourcePermission > Off-Premises ERL </ resourcePermission > < resourcePermission > OnsiteContact </ resourcePermission > < resourcePermission > Pager and Email Alert Configurations </ resourcePermission > < resourcePermission > Phone Search </ resourcePermission > < resourcePermission > Processes </ resourcePermission > < resourcePermission > PS ALI Convert </ resourcePermission > < resourcePermission > PS ALI Export </ resourcePermission > < resourcePermission > Purge </ resourcePermission > < resourcePermission > Run Tracking </ resourcePermission > < resourcePermission > Saml Sso </ resourcePermission > < resourcePermission > Tracking Schedule </ resourcePermission > < resourcePermission > Server </ resourcePermission > < resourcePermission > Server Group </ resourcePermission > < resourcePermission > MIB2 system group configuration </ resourcePermission > < resourcePermission > SNMP V1/V2c configuration </ resourcePermission > < resourcePermission > SNMP v3 configuration </ resourcePermission > < resourcePermission > LAN Switches </ resourcePermission > < resourcePermission > Switch Port </ resourcePermission > < resourcePermission > Synthetic Phone </ resourcePermission > < resourcePermission > Telephony </ resourcePermission > < resourcePermission > Unlocated Phones </ resourcePermission > < resourcePermission > Application User </ resourcePermission > < resourcePermission > User Setting </ resourcePermission > < resourcePermission > User Call History </ resourcePermission > < resourcePermission > User Group </ resourcePermission > < resourcePermission > Intrado VUI Settings </ resourcePermission > < resourcePermission > Web Alert </ resourcePermission > </ resource > </ from > < to > < description > new desc 1 </ description > < resource > < resourcePermission > Change CCM Version </ resourcePermission > < resourcePermission > Cluster DB Host setting </ resourcePermission > < resourcePermission > Audit Log Configuration </ resourcePermission > < resourcePermission > All Logs </ resourcePermission > < resourcePermission > Phone Search </ resourcePermission > < resourcePermission > User Call History </ resourcePermission > < resourcePermission > Web Alert </ resourcePermission > </ resource > </ to > </ changeRequested > < links > < publisherURL > https://unity-pri/cerappservices/service/userrole?userRoleName=TestUserRole_171 </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/userrole?userRoleName=TestUserRole_171 </ subscriberURL > </ links > </ updateUserRoleResponse >
```

JSON response

JSON

```
{ "status" : "Success" , "message" : "Update Successful for role TestUserRole_651" , "changeRequested" : { "from" : { "description" : "TestUserRole_651" , "resource" : { "resourcePermission" : [ "Access Point" , "Add Subscriber" , "ALI Formatting Tool" , "All Logs" , "Audit Log Configuration" , "Call History" , "Call Manager Details" , "CER Groups in Cluster" , "Cluster DB Host setting" , "Control Centre" , "CPU & Memory Usage" , "Device Snmp Settings" , "Disk Usage" , "ERL" , "ERL Audit Trail" , "ERL Debug Tool" , "ERL Migration" , "Event Viewer" , "File Management Utility" , "Functional role" , "Intrado ERL" , "IP Subnet" , "License Management" , "Mail Alert Configurations" , "Manually Configured Phones" , "Change CCM Version" , "Off-Premises ERL" , "OnsiteContact" , "Pager and Email Alert Configurations" , "Phone Search" , "Processes" , "PS ALI Convert" , "PS ALI Export" , "Purge" , "Run Tracking" , "Saml Sso" , "Tracking Schedule" , "Server" , "Server Group" , "MIB2 system group configuration" , "SNMP V1/V2c configuration" , "SNMP v3 configuration" , "LAN Switches" , "Switch Port" , "Synthetic Phone" , "Telephony" , "Unlocated Phones" , "Application User" , "User Setting" , "User Call History" , "User Group" , "Intrado VUI Settings" , "Web Alert" ] } } , "to" : { "description" : "new desc 1" , "resource" : { "resourcePermission" : [ "Change CCM Version" , "Cluster DB Host setting" , "Audit Log Configuration" , "All Logs" , "Phone Search" , "User Call History" , "Web Alert" ] } } } , "links" : { "publisherURL" : "https://cer151/cerappservices/service/userrole?userRoleName=TestUserRole_651" , "subscriberURL" : "https://unity-sec/cerappservices/service/userrole?userRoleName=TestUserRole_651" } }
```

### Delete list of user roles in CER

#### /userrole

http

```
DELETE https://{CER-IP}/cerappservices/service/userrole/
```

This URL deletes a list of existing user roles in CER. The request should be made using HTTP DELETE method with a body in below mentioned format. On successful deletion, a 200 OK response will be sent along with appropriate status, message for the respective user role in response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request examples

XML request

xml

```
< deleteUserRolesRequest > < userRoles > < userRoleName > </ userRoleName > < userRoleName > CER System Admin </ userRoleName > </ userRoles > </ deleteUserRolesRequest >
```

JSON request

JSON

```
{ "userRoles" : { "userRoleName" : [ "" , "CER System Admin" ] } }
```

Response examples

XML response

xml

```
< deleteUserRolesResponse > < status > Some UserRole(s) Deletion was not successful </ status > < userRoles > < userRole > < userRoleName > </ userRoleName > < status > Failure </ status > < message > Failed as UserRole cannot be empty or null '' </ message > </ userRole > < userRole > < userRoleName > CER System Admin </ userRoleName > < status > Failure </ status > < message > Cannot delete standard UserRole 'CER System Admin' </ message > </ userRole > </ userRoles > </ deleteUserRolesResponse >
```

JSON response

JSON

```
{ "status" : "Some UserRole(s) Deletion was not successful" , "userRoles" : { "userRole" : [ { "userRoleName" : "" , "status" : "Failure" , "message" : "Failed as UserRole cannot be empty or null ''" } , { "userRoleName" : "CER System Admin" , "status" : "Failure" , "message" : "Cannot delete standard UserRole 'CER System Admin'" } ] } }
```

### Delete single user role in CER

#### /userrole?userRoleName=CER%20System%20Admin

http

```
DELETE https://{CER-IP}/cerappservices/service/userrole?userRoleName=CER%20System%20Admin
```

This URL deletes an existing CER user role as mentioned in userRoleName parameter. On successful deletion, a 200 OK response will be sent along with appropriate status, message for the respective user role in response. In case of failure appropriate message will be present in the status field with relevant HTTP return code.

#### Path parameters

Response examples

XML response

xml

```
< deleteUserRolesResponse > < status > Some UserRole(s) Deletion was not successful </ status > < userRoles > < userRole > < userRoleName > CER System Admin </ userRoleName > < status > Failure </ status > < message > Cannot delete standard UserRole 'CER System Admin' </ message > </ userRole > </ userRoles > </ deleteUserRolesResponse >
```

JSON response

JSON

```
{ "status" : "Some UserRole(s) Deletion was not successful" , "userRoles" : { "userRole" : { "userRoleName" : "CER System Admin" , "status" : "Failure" , "message" : "Cannot delete standard UserRole 'CER System Admin'" } } }
```

## User Group Management

### Fetch all user group

#### /usergroup

http

```
GET https://{CER-IP}/cerappservices/service/usergroup
```

The /usergroup resource retrieves all the user groups currently available in CER.

Response examples

XML response

xml

```
< userGroupDetailsResponse > < status > User Group Details Info </ status > < userGroups > < userGroup > < pKid > f2124656-7a28-4bcf-93f5-17d29a5819b5 </ pKid > < userGroupName > CER System Administrator </ userGroupName > < description > ER Administrator for all system configurations </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup/CER System Administrator </ publisherURL > </ links > < usersInGroup > < userName > admin </ userName > </ usersInGroup > < userRolesInGroup > < userRoleName > CER System Admin </ userRoleName > </ userRolesInGroup > </ userGroup > < userGroup > < pKid > e280ae83-1889-438d-b039-c4527e7bb4c4 </ pKid > < userGroupName > CER ERL Administrator </ userGroupName > < description > ER Administrator for ERL configurations </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup/CER ERL Administrator </ publisherURL > </ links > < usersInGroup /> < userRolesInGroup > < userRoleName > CER ERL Admin </ userRoleName > </ userRolesInGroup > </ userGroup > < userGroup > < pKid > 3cb72a32-723a-44a8-9208-b97c88c33943 </ pKid > < userGroupName > CER Network Administrator </ userGroupName > < description > ER Administrator for network configurations </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup/CER Network Administrator </ publisherURL > </ links > < usersInGroup /> < userRolesInGroup > < userRoleName > CER Network Admin </ userRoleName > </ userRolesInGroup > </ userGroup > < userGroup > < pKid > 26f0fcc1-a440-4a3c-9c97-c86d5115bf09 </ pKid > < userGroupName > CER Serviceability </ userGroupName > < description > ER Serviceability user for serviceability pages </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup/CER Serviceability </ publisherURL > </ links > < usersInGroup > < userName > admin </ userName > </ usersInGroup > < userRolesInGroup > < userRoleName > CER Serviceability </ userRoleName > </ userRolesInGroup > </ userGroup > < userGroup > < pKid > 83b2334d-6948-455b-b8b8-b5c084fe8fff </ pKid > < userGroupName > CER Admin Utility </ userGroupName > < description > ER Admin utility user for admin utility pages </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup/CER Admin Utility </ publisherURL > </ links > < usersInGroup > < userName > admin </ userName > </ usersInGroup > < userRolesInGroup > < userRoleName > CER Admin Utility </ userRoleName > </ userRolesInGroup > </ userGroup > < userGroup > < pKid > 3dd9a00c-55f1-4ea7-ad84-50f1a8169d04 </ pKid > < userGroupName > CER User </ userGroupName > < description > ER security user who attends to emergency calls </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup/CER User </ publisherURL > </ links > < usersInGroup > < userName > admin </ userName > </ usersInGroup > < userRolesInGroup > < userRoleName > CER User </ userRoleName > </ userRolesInGroup > </ userGroup > < userGroup > < pKid > b3251c14-c7d8-4934-b8c7-aac8f5a9d802 </ pKid > < userGroupName > CER Audit Administrator </ userGroupName > < description > ER Auditor </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup/CER Audit Administrator </ publisherURL > </ links > < usersInGroup > < userName > admin </ userName > </ usersInGroup > < userRolesInGroup > < userRoleName > CER Audit Admin </ userRoleName > </ userRolesInGroup > </ userGroup > < userGroup > < pKid > c53f3aca-f0a8-42df-bbdc-da0d466cf5ce </ pKid > < userGroupName > TestUserGroup_440 </ userGroupName > < description > TestUserGroup_440 </ description > < isStandard > false </ isStandard > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup/TestUserGroup_440 </ publisherURL > </ links > < usersInGroup /> < userRolesInGroup > < userRoleName > CER Admin Utility </ userRoleName > < userRoleName > CER Audit Admin </ userRoleName > </ userRolesInGroup > </ userGroup > </ userGroups > </ userGroupDetailsResponse >
```

JSON response

JSON

```
{ "status" : "User Group Details Info" , "userGroups" : { "userGroup" : [ { "pKid" : "f2124656-7a28-4bcf-93f5-17d29a5819b5" , "userGroupName" : "CER System Administrator" , "description" : "ER Administrator for all system configurations" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup/CER System Administrator" } , "usersInGroup" : { "userName" : "admin" } , "userRolesInGroup" : { "userRoleName" : "CER System Admin" } } , { "pKid" : "e280ae83-1889-438d-b039-c4527e7bb4c4" , "userGroupName" : "CER ERL Administrator" , "description" : "ER Administrator for ERL configurations" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup/CER ERL Administrator" } , "usersInGroup" : "" , "userRolesInGroup" : { "userRoleName" : "CER ERL Admin" } } , { "pKid" : "3cb72a32-723a-44a8-9208-b97c88c33943" , "userGroupName" : "CER Network Administrator" , "description" : "ER Administrator for network configurations" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup/CER Network Administrator" } , "usersInGroup" : "" , "userRolesInGroup" : { "userRoleName" : "CER Network Admin" } } , { "pKid" : "26f0fcc1-a440-4a3c-9c97-c86d5115bf09" , "userGroupName" : "CER Serviceability" , "description" : "ER Serviceability user for serviceability pages" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup/CER Serviceability" } , "usersInGroup" : { "userName" : "admin" } , "userRolesInGroup" : { "userRoleName" : "CER Serviceability" } } , { "pKid" : "83b2334d-6948-455b-b8b8-b5c084fe8fff" , "userGroupName" : "CER Admin Utility" , "description" : "ER Admin utility user for admin utility pages" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup/CER Admin Utility" } , "usersInGroup" : { "userName" : "admin" } , "userRolesInGroup" : { "userRoleName" : "CER Admin Utility" } } , { "pKid" : "3dd9a00c-55f1-4ea7-ad84-50f1a8169d04" , "userGroupName" : "CER User" , "description" : "ER security user who attends to emergency calls" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup/CER User" } , "usersInGroup" : { "userName" : "admin" } , "userRolesInGroup" : { "userRoleName" : "CER User" } } , { "pKid" : "b3251c14-c7d8-4934-b8c7-aac8f5a9d802" , "userGroupName" : "CER Audit Administrator" , "description" : "ER Auditor" , "isStandard" : "true" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup/CER Audit Administrator" } , "usersInGroup" : { "userName" : "admin" } , "userRolesInGroup" : { "userRoleName" : "CER Audit Admin" } } , { "pKid" : "c53f3aca-f0a8-42df-bbdc-da0d466cf5ce" , "userGroupName" : "TestUserGroup_440" , "description" : "TestUserGroup_440" , "isStandard" : "false" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup/TestUserGroup_440" } , "usersInGroup" : "" , "userRolesInGroup" : { "userRoleName" : [ "CER Admin Utility" , "CER Audit Admin" ] } } ] } }
```

### Fetch Single user group

#### /usergroup?userGroupName=CER%20System%20Administrator

http

```
GET https://{CER-IP}/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator
```

This URL retrieves details for the user group mentioned in userGroupName parameter. If user group is not present, 404 Not found error is returned.

#### Path parameters

Response examples

XML response

xml

```
< userGroupDetailsResponse > < status > User Group Details Info </ status > < userGroups > < userGroup > < pKid > 8b094e67-a5f2-4393-a1cb-e1e91aafb596 </ pKid > < userGroupName > CER System Administrator </ userGroupName > < description > ER Administrator for all system configurations </ description > < isStandard > true </ isStandard > < links > < publisherURL > https://cer151/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator </ publisherURL > < subscriberURL > https://unity-sec/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator </ subscriberURL > </ links > < usersInGroup > < userName > admin </ userName > </ usersInGroup > < userRolesInGroup > < userRoleName > CER System Admin </ userRoleName > </ userRolesInGroup > </ userGroup > </ userGroups > </ userGroupDetailsResponse >
```

JSON response

JSON

```
{ "status" : "User Group Details Info" , "userGroups" : { "userGroup" : { "pKid" : "8b094e67-a5f2-4393-a1cb-e1e91aafb596" , "userGroupName" : "CER System Administrator" , "description" : "ER Administrator for all system configurations" , "isStandard" : "true" , "links" : { "publisherURL" : "https://cer151/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator" , "subscriberURL" : "https://unity-sec/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator" } , "usersInGroup" : { "userName" : "admin" } , "userRolesInGroup" : { "userRoleName" : "CER System Admin" } } } }
```

### Add New UserGroup

#### /usergroup

http

```
POST https://{CER-IP}/cerappservices/service/usergroup
```

This URL adds new usergroup in CER. The request should be made using HTTP POST method with a body in below mentioned format. On successful insertion, a 200 OK response will be sent along with the direct url for the user group in response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request examples

XML request

xml

```
< newUserGroupRequest > < userGroupName > {{newUserGroup}} </ userGroupName > < description > {{newUserGroup}} </ description > < addUsersToGroup > < user > TestUserCERTeamRemote_490 </ user > < user > </ user > < user > TestUserCERTeamRemote_790 </ user > < user > fdfdfd </ user > < user > </ user > < user > TestUserCERTeamLocal_151 </ user > < user > </ user > </ addUsersToGroup > < assignRolesToGroup > < userRole > TestUserRole_119 </ userRole > < userRole > CER Admin Utility </ userRole > < userRole > CER Audit Admin </ userRole > < userRole > dfdfdf </ userRole > < userRole > </ userRole > </ assignRolesToGroup > </ newUserGroupRequest >
```

JSON request

JSON

```
{ "userGroupName" : "{{newUserGroup}}" , "description" : "{{newUserGroup}}" , "addUsersToGroup" : { "user" : [ "TestUserCERTeamRemote_490" , "" , "TestUserCERTeamRemote_790" , "fdfdfd" , "" , "TestUserCERTeamLocal_151" , "" ] } , "assignRolesToGroup" : { "userRole" : [ "TestUserRole_119" , "CER Admin Utility" , "CER Audit Admin" , "dfdfdf" , "" ] } }
```

Response examples

XML response

xml

```
< userGroupInsertResponse > < status > AddSuccess </ status > < pkid > 7ca4ac33-75ea-498b-8a20-ec9cb01f971e </ pkid > < links > < publisherURL > https://cer151/cerappservices/service/usergroup?userGroupName=TestUserGroup_938 </ publisherURL > < subscriberURL > https://unity-sec/cerappservices/service/usergroup?userGroupName=TestUserGroup_938 </ subscriberURL > </ links > </ userGroupInsertResponse >
```

JSON response

JSON

```
{ "status" : "AddSuccess" , "pkid" : "58cd9c64-341e-4da7-9d51-a0609e932197" , "links" : { "publisherURL" : "https://cer151/cerappservices/service/usergroup?userGroupName=TestUserGroup_813" , "subscriberURL" : "https://unity-sec/cerappservices/service/usergroup?userGroupName=TestUserGroup_813" } }
```

### Delete list of UserGroups

#### /usergroup

http

```
DELETE https://{CER-IP}/cerappservices/service/usergroup
```

This URL deletes a list of existing usergroups in CER. The request should be made using HTTP DELETE method with a body in below mentioned format. On successful deletion, a 200 OK response will be sent along with appropriate status, message for the respective usergroup in the response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request example

XML request

xml

```
< deleteUserGroupsRequest > < userGroups > < userGroupName > TestUserGroup_354 </ userGroupName > < userGroupName > TestUserGroup_691 </ userGroupName > < userGroupName > TestUserGroup_965 </ userGroupName > </ userGroups > </ deleteUserGroupsRequest >
```

JSON request

JSON

```
{ "userGroups" : { "userGroupName" : [ "TestUserGroup_354" , "TestUserGroup_691" , "TestUserGroup_965" ] } }
```

Response examples

XML response

xml

```
< deleteUserGroupsResponse > < status > Some UserGroup(s) Deletion was not successful </ status > < userGroups > < userGroup > < userGroupName > TestUserGroup_354 </ userGroupName > < status > Failure </ status > < message > UserGroup is not present in DB 'TestUserGroup_354' </ message > </ userGroup > < userGroup > < userGroupName > TestUserGroup_691 </ userGroupName > < status > Failure </ status > < message > UserGroup is not present in DB 'TestUserGroup_691' </ message > </ userGroup > < userGroup > < userGroupName > TestUserGroup_965 </ userGroupName > < status > Failure </ status > < message > UserGroup is not present in DB 'TestUserGroup_965' </ message > </ userGroup > </ userGroups > </ deleteUserGroupsResponse >
```

JSON response

JSON

```
{ "status" : "Some UserGroup(s) Deletion was not successful" , "userGroups" : { "userGroup" : [ { "userGroupName" : "TestUserGroup_354" , "status" : "Failure" , "message" : "UserGroup is not present in DB 'TestUserGroup_354'" } , { "userGroupName" : "TestUserGroup_691" , "status" : "Failure" , "message" : "UserGroup is not present in DB 'TestUserGroup_691'" } , { "userGroupName" : "TestUserGroup_965" , "status" : "Failure" , "message" : "UserGroup is not present in DB 'TestUserGroup_965'" } ] } }
```

### Delete Single UserGroup

#### /usergroup?userGroupName=CER%20System%20Administrator

http

```
DELETE https://{CER-IP}/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator
```

This URL deletes an existing CER usergroup as mentioned in userGroupName parameter. On successful deletion, a 200 OK response will be sent along with appropriate status, message for the respective usergroup in response. In case of failure appropriate message will be present in the status field with relevant HTTP return code.

#### Path parameters

Response example

XML response

xml

```
< deleteUserGroupsResponse > < status > Some UserGroup(s) Deletion was not successful </ status > < userGroups > < userGroup > < userGroupName > CER System Administrator </ userGroupName > < status > Failure </ status > < message > Cannot delete standard UserGroup 'CER System Administrator' </ message > </ userGroup > </ userGroups > </ deleteUserGroupsResponse >
```

JSON response

JSON

```
{ "status" : "Some UserGroup(s) Deletion was not successful" , "userGroups" : { "userGroup" : { "userGroupName" : "CER System Administrator" , "status" : "Failure" , "message" : "Cannot delete standard UserGroup 'CER System Administrator'" } } }
```

### Update User Group

#### /usergroup

http

```
PUT https://{CER-IP}/cerappservices/service/usergroup
```

This URL updates an existing usergroup in CER. The request should be made using HTTP PUT method with a body in below mentioned format. On successful insertion, a 200 OK response will be sent along with the direct url for the usergroup in response. In case of failures appropriate message will be present in the status field with relevant HTTP return code.

Request examples

XML request

xml

```
< updateUserGroupRequest > < userGroupName > CER System Administrator </ userGroupName > < description > TestUserGroup_207 </ description > < addUsersToGroup > < user > TestUserCERTeamLocal_167 </ user > < user > </ user > < user > TestUserCERTeamLocal_166 </ user > < user > fdfdfd </ user > < user > admin </ user > < user > TestUserCERTeamLocal_413 </ user > < user > TestUserCERTeamLocal_611 </ user > < user > TestUserCERTeamLocal_815 </ user > </ addUsersToGroup > < assignRolesToGroup > < userRole > TestUserRole_247 </ userRole > < userRole > CER Admin Utility </ userRole > < userRole > dfdfdf </ userRole > < userRole > CER System Admin </ userRole > </ assignRolesToGroup > </ updateUserGroupRequest >
```

JSON request

JSON

```
{ "userGroupName" : "CER System Administrator" , "description" : "TestUserGroup_207" , "addUsersToGroup" : { "user" : [ "TestUserCERTeamLocal_167" , "" , "TestUserCERTeamLocal_166" , "fdfdfd" , "admin" , "TestUserCERTeamLocal_413" , "TestUserCERTeamLocal_611" , "TestUserCERTeamLocal_815" ] } , "assignRolesToGroup" : { "userRole" : [ "TestUserRole_247" , "CER Admin Utility" , "dfdfdf" , "CER System Admin" ] } }
```

Response examples

XML response

xml

```
< updateUserGroupResponse > < status > Success </ status > < message > Update of user group 'CER System Administrator' was successful, Default group roles assignment cannot be edited </ message > < links > < publisherURL > https://unity-pri/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator </ publisherURL > < subscriberURL > https://cucm207/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator </ subscriberURL > </ links > </ updateUserGroupResponse >
```

JSON response

JSON

```
{ "status" : "Success" , "message" : "Update of user group 'CER System Administrator' was successful, Default group roles assignment cannot be edited" , "links" : { "publisherURL" : "https://unity-pri/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator" , "subscriberURL" : "https://cucm207/cerappservices/service/usergroup?userGroupName=CER%20System%20Administrator" } }
```

Next

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| users | Lists all the user currently present in CER |
| user | Individual block for user details |
| pKid | PKID for the user as saved in CER |
| userName | User name for the user |
| isStandard | 1 means user is the install admin and 0 otherwise |
| isRemoteAuth | 0 value is for Local user, 1 is for Remote user and 2 is for IDP user |
| links | publisherURL and subscriberURL are the direct urls for the user in  publisher and subscriber respectively |
| userGroups | Lists userGroup (s) the user is currently part of |
| userRoles | Lists all the userRole (s) assigned to the user |

| Parameters | Description |
|---|---|
| userName | User name as stored in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| pKid | PKID for the user as saved in CER |
| userName | User name for the user |
| isStandard | 1 means user is the install admin and 0 otherwise |
| isRemoteAuth | 0 value is for Local user, 1 is for Remote user and 2 is for IDP user |
| links | publisherURL and subscriberURL are the direct urls for the user in  publisher and subscriber respectively |
| userGroups | Lists userGroup (s) the user is currently part of |
| userRoles | Lists all the userRole (s) assigned to the user |

| Fields | Description |
|---|---|
| userName | User name for the new user |
| userPassword | Password for the new user |
| authenticationMode | Specify user type Local , Remote or IdP |
| ccmClusterID | CUCM cluser IP Address or Hostname for Remote and IdP users |
| resetOnLogon | Specify if the user need to reset password after first login. Possible values "t" (for true) or "f" (for false) |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| pKid | PKID for the user as stored in CER |
| links | Lists direct URLs for the user in publisher and subscriber ( publisherURL , subscriberURL ) |

| Fields | Description |
|---|---|
| userName | User name of the existing user |
| userPassword | New password for the existing user |
| authenticationMode | Specify user type Local , Remote or IdP |
| ccmClusterID | CUCM cluser IP Address or Hostname for Remote and IdP users |
| resetOnLogon | Specify if the user need to reset password after first login. Possible values "t" (for true) or "f" (for false) |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| pKid | PKID for the user as stored in CER |
| links | Lists direct URLs for the user in publisher and subscriber |

| Fields | Description |
|---|---|
| users | List of user names to be deleted |
| name | Individual user name |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| users | Lists all the user blocks |
| user | Individual block for user details |
| name | User name |
| status | Status corresponding to current user |
| message | Message related to the delete operation on the current user |

| Parameters | Description |
|---|---|
| userName | User name as stored in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| user | Individual block for user details |
| name | User name |
| status | Status corresponding to current user |
| message | Message related to the delete operation on the current user |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| userRoles | Lists all the user roles currently available in CER |
| userRole | Individual block for user role details |
| pKid | PKID for the user role as saved in CER |
| roleName | Role name |
| description | Description for the particular user role |
| isStandard | " true " for standard role in CER and " false " for user created roles |
| links | publisherURL and subscriberURL are the direct urls for the roles in  publisher and subscriber respectively |
| resourcePermissions | List of resource permissions as part of the role |
| resourcePermission | Individual resource permission |

| Parameters | Description |
|---|---|
| userRoleName | User role name as stored in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| userRoles | Lists all the user roles currently available in CER |
| userRole | Individual block for user role details |
| pKid | PKID for the user role as saved in CER |
| roleName | Role name |
| description | Description for the particular user role |
| isStandard | " true " for standard role in CER and " false " for user created roles |
| links | publisherURL and subscriberURL are the direct urls for the roles in  publisher and subscriber respectively |
| resourcePermissions | List of resource permissions as part of the role |
| resourcePermission | Individual resource permission |

| Fields | Description |
|---|---|
| name | Name of the user role |
| selectAllResourceGroups | Option to provide permissions for all the resource groups. "Y" or "y" are accepted values. |
| desc | Description for the new user role |
| CERAdminUtility | All permissions as part of CER Admin Utility |
| ClusterDBHostsetting | Cluster DB Host setting permission |
| ChangeCCMVersion | Change CCM Version permission |
| CERAuditAdministrator | All permissions as part of CER Audit Administrator |
| AuditLogConfiguration | Audit Log Configuration permission |
| CERServiceability | All permissions as part of CER Serviceability |
| AllLogs | All Logs permission |
| ControlCentre | Control Centre permission |
| CPUMemoryUsage | CPU & Memory Usage permission |
| DiskUsage | Disk Usage permission |
| EventViewer | Event Viewer permission |
| Processes | Processes permission |
| MIB2systemgroupconfiguration | MIB2 system group configuration permission |
| SNMPV1V2configuration | SNMP V1/V2c configuration permission |
| SNMPv3configuration | SNMP v3 configuration permission |
| CERSystemAdministrator | All permissions as part of CER System Administrator |
| AccessPoint | Access Point permission |
| AddSubscriber | Add Subscriber permission |
| ALIFormattingTool | ALI Formatting Tool permission |
| CallHistory | Call History permission |
| CallManagerDetails | Call Manager Details permission |
| CERGroupsinCluster | CER Groups in Cluster permission |
| DeviceSnmpSettings | Device Snmp Settings permission |
| ERL | ERL  permission |
| ERLAuditTrail | ERL Audit Trail permission |
| ERLDebugTool | ERL Debug Tool permission |
| ERLMigration | ERL Migration permission |
| FileManagementUtility | File Management Utility permission |
| Functionalrole | Functional role permission |
| IntradoERL | Intrado ERL permission |
| IPSubnet | IP Subnet permission |
| LicenseManagement | License Management permission |
| MailAlertConfigurations | Mail Alert Configurations permission |
| ManuallyConfiguredPhones | Manually Configured Phones permission |
| OffPremisesERL | Off-Premises ERL permission |
| OnsiteContact | OnsiteContact permission |
| PagerandEmailAlertConfigurations | Pager and Email Alert Configurations permission |
| PSALIConvert | PS ALI Convert permission |
| PSALIExport | PS ALI Export permission |
| Purge | Purge permission |
| RunTracking | Run Tracking permission |
| SamlSso | Saml Sso permission |
| TrackingSchedule | Tracking Schedule permission |
| Server | Server permission |
| ServerGroup | Server Group permission |
| LANSwitches | LAN Switches permission |
| SwitchPort | Switch Port permission |
| SyntheticPhone | Synthetic Phone permission |
| Telephony | Telephony permission |
| UnlocatedPhones | Unlocated Phones permission |
| ApplicationUser | Application User permission |
| UserSetting | User Setting permission |
| UserGroup | User Group permission |
| IntradoVUISettings | Intrado VUI Settings permission |
| CERUser | All permissions as part of CER User |
| PhoneSearch | Phone Search permission |
| UserCallHistory | User Call History permission |
| WebAlert | Web Alert permission |

| Fields | Description |
|---|---|
| status | Overall status of the response |
| message | message details all the permission given as part of the role |
| links | Lists direct URLs for the user role in publisher and subscriber ( publisherURL , subscriberURL ) |

| Fields | Description |
|---|---|
| name | Name of the existing user role |
| selectAllResourceGroups | Option to provide permissions for all the resource groups. "Y" or "y" are accepted values. |
| desc | Description for the new user role |
| CERAdminUtility | All permissions as part of CER Admin Utility |
| ClusterDBHostsetting | Cluster DB Host setting permission |
| ChangeCCMVersion | Change CCM Version permission |
| CERAuditAdministrator | All permissions as part of CER Audit Administrator |
| AuditLogConfiguration | Audit Log Configuration permission |
| CERServiceability | All permissions as part of CER Serviceability |
| AllLogs | All Logs permission |
| ControlCentre | Control Centre permission |
| CPUMemoryUsage | CPU & Memory Usage permission |
| DiskUsage | Disk Usage permission |
| EventViewer | Event Viewer permission |
| Processes | Processes permission |
| MIB2systemgroupconfiguration | MIB2 system group configuration permission |
| SNMPV1V2configuration | SNMP V1/V2c configuration permission |
| SNMPv3configuration | SNMP v3 configuration permission |
| CERSystemAdministrator | All permissions as part of CER System Administrator |
| AccessPoint | Access Point permission |
| AddSubscriber | Add Subscriber permission |
| ALIFormattingTool | ALI Formatting Tool permission |
| CallHistory | Call History permission |
| CallManagerDetails | Call Manager Details permission |
| CERGroupsinCluster | CER Groups in Cluster permission |
| DeviceSnmpSettings | Device Snmp Settings permission |
| ERL | ERL  permission |
| ERLAuditTrail | ERL Audit Trail permission |
| ERLDebugTool | ERL Debug Tool permission |
| ERLMigration | ERL Migration permission |
| FileManagementUtility | File Management Utility permission |
| Functionalrole | Functional role permission |
| IntradoERL | Intrado ERL permission |
| IPSubnet | IP Subnet permission |
| LicenseManagement | License Management permission |
| MailAlertConfigurations | Mail Alert Configurations permission |
| ManuallyConfiguredPhones | Manually Configured Phones permission |
| OffPremisesERL | Off-Premises ERL permission |
| OnsiteContact | OnsiteContact permission |
| PagerandEmailAlertConfigurations | Pager and Email Alert Configurations permission |
| PSALIConvert | PS ALI Convert permission |
| PSALIExport | PS ALI Export permission |
| Purge | Purge permission |
| RunTracking | Run Tracking permission |
| SamlSso | Saml Sso permission |
| TrackingSchedule | Tracking Schedule permission |
| Server | Server permission |
| ServerGroup | Server Group permission |
| LANSwitches | LAN Switches permission |
| SwitchPort | Switch Port permission |
| SyntheticPhone | Synthetic Phone permission |
| Telephony | Telephony permission |
| UnlocatedPhones | Unlocated Phones permission |
| ApplicationUser | Application User permission |
| UserSetting | User Setting permission |
| UserGroup | User Group permission |
| IntradoVUISettings | Intrado VUI Settings permission |
| CERUser | All permissions as part of CER User |
| PhoneSearch | Phone Search permission |
| UserCallHistory | User Call History permission |
| WebAlert | Web Alert permission |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| message | Shows reason for success or failure |
| changeRequested | Block comprising of all requested changes. |
| from | Lists all the details prior to the update request |
| description | Description for the user role |
| resource | List of resource permissions |
| resourcePermission | Individual resource permission |
| to | Lists all the details post the changes |
| links | Lists direct URLs for the user role in publisher and subscriber ( publisherURL , subscriberURL ) |

| Fields | Description |
|---|---|
| userRoles | List of user role names to be deleted |
| userRoleName | Individual user role name |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| userRoles | Lists all the user roles block |
| userRole | Individual block for user role details |
| userRoleName | User role name |
| status | Status corresponding to current user role |
| message | Message related the current user role delete operation |

| Parameters | Description |
|---|---|
| userRoleName | User role name as stored in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| userRole | Individual block for user role details |
| userRoleName | User role name |
| status | Status corresponding to current user role |
| message | Message related the current user role delete operation |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| userGroups | Lists all the usergroup currently present in CER |
| userGroup | Individual block for usergroup details |
| pKid | PKID for the usergroup as saved in CER |
| userGroupName | User group name |
| description | Descriptoin of the user group |
| isStandard | "true" means user group is system defined and "false" is user defined |
| links | publisherURL and subscriberURL are the direct urls for the user group in  publisher and subscriber respectively |
| usersInGroup | Lists user (s) currently part of the usergroup |
| userRolesInGroup | Lists userRole (s) currently part of the usergroup |

| Parameters | Description |
|---|---|
| userGroupName | User group name as stored in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| userGroup | Individual block for usergroup details |
| pKid | PKID for the usergroup as saved in CER |
| userGroupName | User group name |
| description | Descriptoin of the user group |
| isStandard | "true" means user group is system defined and "false" is user defined |
| links | publisherURL and subscriberURL are the direct urls for the user group in  publisher and subscriber respectively |
| usersInGroup | Lists user (s) currently part of the usergroup |
| userRolesInGroup | Lists userRole (s) currently part of the usergroup |

| Fields | Description |
|---|---|
| userGroupName | UserGroup name for the new userGroup |
| description | Description of the new userGroup |
| addUsersToGroup | Specify users that needs to be added to Group |
| user | User name as present in CER |
| assignRolesToGroup | Specify userroles that needs to be assigned to the Group |
| userRole | User role as present in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| pKid | PKID for the userGroup as stored in CER |
| links | Lists direct URLs for the usergroup in publisher and subscriber ( publisherURL , subscriberURL ) |

| Fields | Description |
|---|---|
| userGroups | List of usergroup names to be deleted |
| userGroupName | Individual usergroup name as present in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| userGroups | Lists all the userGroup blocks |
| userGroup | Individual block for userGroup details |
| userGroupName | UserGroup name |
| status | Status corresponding to the current user group |
| message | Message related to the delete operation on the current user group |

| Parameters | Description |
|---|---|
| userGroupName | UserGroup name as stored in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| userGroup | Individual block for userGroup details |
| userGroupName | UserGroup name |
| status | Status corresponding to the current user group |
| message | Message related to the delete operation on the current user group |

| Fields | Description |
|---|---|
| userGroupName | User group name of the existing user group |
| description | New/modified description for the existing usergroup |
| addUsersToGroup | Specify user (s) to be made part of the usergroup |
| user | Individual user name as present in CER |
| assignRolesToGroup | Specify roles that needs to be updated which are part of usergroup |
| userRole | Individual user role as present in CER |

| Fields | Description |
|---|---|
| status | Overall status message for the response |
| message | Detailed status message for the response |
| links | Lists direct URLs for the user group in publisher and subscriber |