---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-api-html-61bec8371a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-api.html
retrieved_at: 2026-08-17T03:48:47.507228+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- User Management API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- User Management API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- User Management API

## User API

Administrator can use this API to create/update/delete/fetch the user with mailbox. Various attributes of user, for example
                           notification device, greetings, contact, private list, phone menu, call transfer, screening, or personal data, can also be
                           updated using this API .

### Listing the
                           	 Users

The request can be used to fetch
                                 		  the list of all users.

```
GET https://<connection-server>/vmrest/users
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<Users total="2">
 <User>
  <URI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</URI>
  <ObjectId>4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</ObjectId>
  <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
  <Alias>undeliverablemessagesmailbox</Alias>
  <DisplayName>Undeliverable Messages</DisplayName>
  <TimeZone>0</TimeZone>
  <CreationTime>2013-03-05T10:54:38Z</CreationTime>
  <CosObjectId>610c9c71-32be-4465-b61a-523f24a9d828</CosObjectId>
  <CosURI>/vmrest/coses/610c9c71-32be-4465-b61a-523f24a9d828</CosURI>
  <Language>0</Language>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <ListInDirectory>false</ListInDirectory>
  <IsVmEnrolled>true</IsVmEnrolled>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <CallHandlerObjectId>13a3c5fc-f706-4bd0-aeeb-32dad2c4a29b</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/13a3c5fc-f706-4bd0-aeeb-32dad2c4a29b</CallhandlerURI>
  <DtmfAccessId>99999</DtmfAccessId>
  <VoiceNameRequired>false</VoiceNameRequired>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <Inactive>false</Inactive>
  <MwisURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/privatelists</PrivateListsURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%204d5df6e3-a036-4f16-8f1e- d48e7e9b73c1)</SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%204d5df6e3-a036-4f16-8f1e-d48e7e9b73c1)              
</AlternateNamesURI>
 </User>
 <User>
  <URI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce</URI>
  <ObjectId>671fd8d1-7240-4e60-9194-0ec9c4a626ce</ObjectId>
  <Alias>operator</Alias>
  <DisplayName>Operator</DisplayName>
  <TimeZone>0</TimeZone>
  <CreationTime>2013-03-05 10:54:39.02</CreationTime>
  <CosObjectId>610c9c71-32be-4465-b61a-523f24a9d828</CosObjectId>
  <CosURI>/vmrest/coses/610c9c71-32be-4465-b61a-523f24a9d828</CosURI>
  <Language>0</Language>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <ListInDirectory>false</ListInDirectory>
  <IsVmEnrolled>true</IsVmEnrolled>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <CallHandlerObjectId>4546d6df-5120-4fb3-9719-8d521b8a5796</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/4546d6df-5120-4fb3-9719-8d521b8a5796</CallhandlerURI>
  <DtmfAccessId>99990</DtmfAccessId>
  <VoiceNameRequired>false</VoiceNameRequired>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId> 
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <Inactive>false</Inactive>
  <MwisURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/privatelists</PrivateListsURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%20671fd8d1-7240-4e60-9194-0ec9c4a626ce)</SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%20671fd8d1-7240-4e60-9194-0ec9c4a626ce) </AlternateNamesURI>
</User>
<User>
  <URI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9</URI>
  <ObjectId>8321097e-cca4-483f-b24c-0f2175e6e4c9</ObjectId>
  <FirstName>John</FirstName>
  <LastName>10000</LastName>
  <Alias>John10000</Alias>
  <City/>
  <Department/>
  <EmployeeId/>
  <DisplayName>John 10000</DisplayName>
  <EmailAddress>john@cisco.com</EmailAddress>
  <TimeZone>190</TimeZone>
  <CreationTime>2015-06-01T05:03:15Z</CreationTime>
  <CosObjectId>0a987b74-acf0-4310-ab81-4ebe0190cca4</CosObjectId>
  <CosURI>/vmrest/coses/0a987b74-acf0-4310-ab81-4ebe0190cca4</CosURI>
  <Language>1033</Language>
  <LocationObjectId>17f9c794-d4e4-453b-a9df-771c48c0590e</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/17f9c794-d4e4-453b-a9df-771c48c0590e</LocationURI>
  <ListInDirectory>true</ListInDirectory>
  <IsVmEnrolled>false</IsVmEnrolled>
  <MediaSwitchObjectId>6f37f783-437a-4c9b-aefe-74201f33deab</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/6f37f783-437a-4c9b-aefe-74201f33deab</PhoneSystemURI>
  <CallHandlerObjectId>be938317-6c75-4d67-9c9e-642ba90d85d1</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/be938317-6c75-4d67-9c9e-642ba90d85d1</CallhandlerURI>
  <DtmfAccessId>10000</DtmfAccessId>
  <VoiceNameRequired>false</VoiceNameRequired>
  <PartitionObjectId>30c21994-bd80-4992-97ce-601ca93bf3da</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/30c21994-bd80-4992-97ce-601ca93bf3da</PartitionURI>
  <Inactive>false</Inactive> 
  <MwisURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/privatelists</PrivateListsURI>
  <VideoServiceAccountsURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/videoserviceaccounts</VideoServiceAccountsURI>
  <UserWebPasswordURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/credential/password</UserWebPasswordURI>
  <UserMailboxURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/mailboxattributes</UserMailboxURI>
  <MailboxStoreName>Unity Messaging Database -1</MailboxStoreName>
  <UserVoicePinURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/credential/pin</UserVoicePinURI>
  <UserRoleURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/userroles</UserRoleURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%208321097e-cca4-483f-b24c-0f2175e6e4c9)         </SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%208321097e-cca4-483f-b24c-0f2175e6e4c9)</AlternateNamesURI>
</User>
</Users>
```

```
Response Code: 200
```

JSON Example

To view the list of users, do the following:

```
GET https://<connection-server>/vmrest/users
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
  "Users": {
    "-total": "1",
    "User": {
      "URI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9",
      "ObjectId": "8321097e-cca4-483f-b24c-0f2175e6e4c9",
      "FirstName": "John",
      "LastName": "10000",
      "Alias": "John10000",
      "DisplayName": "John 10000",
      "EmailAddress": "john@cisco.com",
      "TimeZone": "190",
      "CreationTime": "2015-06-01T05:03:15Z",
      "CosObjectId": "0a987b74-acf0-4310-ab81-4ebe0190cca4",
      "CosURI": "/vmrest/coses/0a987b74-acf0-4310-ab81-4ebe0190cca4",
      "Language": "1033",
      "LocationObjectId": "17f9c794-d4e4-453b-a9df-771c48c0590e",
      "LocationURI": "/vmrest/locations/connectionlocations/17f9c794-d4e4-453b-a9df-771c48c0590e",
      "ListInDirectory": "true",
      "IsVmEnrolled": "false",
      "MediaSwitchObjectId": "6f37f783-437a-4c9b-aefe-74201f33deab",
      "PhoneSystemURI": "/vmrest/phonesystems/6f37f783-437a-4c9b-aefe-74201f33deab",
      "CallHandlerObjectId": "be938317-6c75-4d67-9c9e-642ba90d85d1",
      "CallhandlerURI": "/vmrest/handlers/callhandlers/be938317-6c75-4d67-9c9e-642ba90d85d1",
      "DtmfAccessId": "10000",
      "VoiceNameRequired": "false",
      "PartitionObjectId": "30c21994-bd80-4992-97ce-601ca93bf3da",
      "PartitionURI": "/vmrest/partitions/30c21994-bd80-4992-97ce-601ca93bf3da",
      "Inactive": "false",
      "MwisURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/mwis",
      "NotificationDevicesURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/notificationdevices",
      "MessageHandlersURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/messagehandlers",
      "ExternalServiceAccountsURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/externalserviceaccounts",
      "AlternateExtensionsURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/alternateextensions",
      "PrivateListsURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/privatelists",
      "VideoServiceAccountsURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/videoserviceaccounts",
      "UserWebPasswordURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/credential/password",
     "UserMailboxURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/mailboxattributes",
      "MailboxStoreName": "Unity Messaging Database -1",
      "UserVoicePinURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/credential/pin",
      "UserRoleURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/userroles",
      "SmtpProxyAddressesURI": "/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%208321097e-cca4-483f-b24c-0f2175e6e4c9)",
      "AlternateNamesURI": "/vmrest/alternatenames?query=(GlobalUserObjectId%20is%208321097e-cca4-483f-b24c-0f2175e6e4c9)"
    }
  }
}
```

```
Response Code: 200
```

#### Listing Users
                              	 based on Email Address

In Cisco Unity Connection 11.5(1)
                                    		  and later, the system administrator can use email address to list the users
                                    		  using following URI:

```
GET https://<connection-server>/vmrest/users?query=(emailaddress is <emailaddress@domain.com>)

GET https://<connection-server>/vmrest/users?query=(emailaddress startswith <emailaddress@domain.com>)

GET https://<connection-server>/vmrest/users?query=(emailaddress isnull)

GET https://<connection-server>/vmrest/users?query=(emailaddress isnotnull)
```

The following is an example of the GET request that lists the details
                                    		  of specific user based on the email address (emailaddress is
                                    		  <emailaddress@domain.com>:

```
<User>
    <URI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1</URI>
    <ObjectId>fc78a2c6-3065-46a5-b5cb-0bba363280d1</ObjectId>
    <FirstName>abc</FirstName>
    <LastName></LastName>
    <Alias>abc</Alias>
    <City>
    </City>
    <Department>
    </Department>
    <EmployeeId>
    </EmployeeId>
    <DisplayName>abc</DisplayName>
    <EmailAddress>abc@cisco.com</EmailAddress>
    <TimeZone>190</TimeZone>
    <CreationTime>2016-05-11T09:51:04Z</CreationTime>
    <CosObjectId>4e1c04f4-eb53-4f19-aaa2-0982121fa8fd</CosObjectId>
    <CosURI>/vmrest/coses/4e1c04f4-eb53-4f19-aaa2-0982121fa8fd</CosURI>
    <Language>1033</Language>
    <LocationObjectId>44471f12-f7cb-4d99-80fe-672bf039faef</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/44471f12-f7cb-4d99-80fe-672bf039faef</LocationURI>
    <ListInDirectory>true</ListInDirectory>
    <IsVmEnrolled>false</IsVmEnrolled>
    <MediaSwitchObjectId>cf3e31a0-979f-4011-b239-0881cd9c4292</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/cf3e31a0-979f-4011-b239-0881cd9c4292</PhoneSystemURI>
    <CallHandlerObjectId>5e6a0ef4-4ffb-4654-a1ba-1a595ae76f7a</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5e6a0ef4-4ffb-4654-a1ba-1a595ae76f7a</CallhandlerURI>
    <DtmfAccessId>9899</DtmfAccessId>
    <VoiceNameRequired>false</VoiceNameRequired>
    <PartitionObjectId>7c789d46-449b-4ae4-b3f4-176e3b46bd18</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/7c789d46-449b-4ae4-b3f4-176e3b46bd18</PartitionURI>
    <Inactive>false</Inactive>
    <MwisURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/mwis</MwisURI>
    <NotificationDevicesURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/notificationdevices</NotificationDevicesURI>
    <MessageHandlersURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/messagehandlers</MessageHandlersURI>
    <ExternalServiceAccountsURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/externalserviceaccounts</ExternalServiceAccountsURI>
    <AlternateExtensionsURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/alternateextensions</AlternateExtensionsURI>
    <PrivateListsURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/privatelists</PrivateListsURI>
    <VideoServiceAccountsURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/videoserviceaccounts</VideoServiceAccountsURI>
    <UserWebPasswordURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/credential/password</UserWebPasswordURI>
    <UserMailboxURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/mailboxattributes</UserMailboxURI>
    <MailboxStoreName>Unity Messaging Database -1</MailboxStoreName>
    <UserVoicePinURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/credential/pin</UserVoicePinURI>
    <UserRoleURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/userroles</UserRoleURI>
    <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%20fc78a2c6-3065-46a5-b5cb-0bba363280d1)</SmtpProxyAddressesURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%20fc78a2c6-3065-46a5-b5cb-0bba363280d1)</AlternateNamesURI>
  </User>
```

```
Response Code: 200
```

JSON Example

To view the details of particular user based on email address
                                    		  (emailaddress is <emailaddress@domain.com>), do the following:

```
GET https://<connection-server>/vmrest/users?query=(emailaddress is abc@cisco.com)
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "Users": {
    "-total": "1",
       "User": {
        "URI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1"
        "ObjectId":"fc78a2c6-3065-46a5-b5cb-0bba363280d1"
        "FirstName":"abc"
        "Alias":"abc"
        "DisplayName":"abc"
        "EmailAddress":"abc@cisco.com"
        "TimeZone":"190"
        "CreationTime":"2016-05-11T09:51:04Z"
        "CosObjectId":"4e1c04f4-eb53-4f19-aaa2-0982121fa8fd"
        "CosURI":"/vmrest/coses/4e1c04f4-eb53-4f19-aaa2-0982121fa8fd"
        "Language":"1033"
        "LocationObjectId":"44471f12-f7cb-4d99-80fe-672bf039faef"
        "LocationURI":"/vmrest/locations/connectionlocations/44471f12-f7cb-4d99-80fe-672bf039faef"
        "ListInDirectory":"true"
        "IsVmEnrolled":"false"
        "MediaSwitchObjectId":"cf3e31a0-979f-4011-b239-0881cd9c4292"
        "PhoneSystemURI":"/vmrest/phonesystems/cf3e31a0-979f-4011-b239-0881cd9c4292"
        "CallHandlerObjectId":"5e6a0ef4-4ffb-4654-a1ba-1a595ae76f7a"/CallHandlerObjectId"
        "CallhandlerURI":"/vmrest/handlers/callhandlers/5e6a0ef4-4ffb-4654-a1ba-1a595ae76f7a"
        "DtmfAccessId":"9899"
        "VoiceNameRequired":"false"
        "PartitionObjectId":"7c789d46-449b-4ae4-b3f4-176e3b46bd18"
        "PartitionURI":"/vmrest/partitions/7c789d46-449b-4ae4-b3f4-176e3b46bd18"
        "Inactive":"false"
        "MwisURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/mwis"
        "NotificationDevicesURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/notificationdevices"
        "MessageHandlersURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/messagehandlers"
        "ExternalServiceAccountsURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/externalserviceaccounts"
        "AlternateExtensionsURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/alternateextensions"
        "PrivateListsURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/privatelists"
        "VideoServiceAccountsURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/videoserviceaccounts"
        "UserWebPasswordURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/credential/password"
        "UserMailboxURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/mailboxattributes"
        "MailboxStoreName":"Unity Messaging Database -1"
        "UserVoicePinURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/credential/pin"
        "UserRoleURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/userroles"
        "SmtpProxyAddressesURI":"/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%20fc78a2c6-3065-46a5-b5cb-0bba363280d1)"
        "AlternateNamesURI":"/vmrest/alternatenames?query=(GlobalUserObjectId%20is%20fc78a2c6-3065-46a5-b5cb-0bba363280d1)"
       }
      }
     }
```

#### Listing Specific
                              	 Tenant Related Users by System Administrator

In Cisco Unity Connection 10.5(2)
                                    		  and later, the system administrator can use TenantObjectID to list the specific
                                    		  tenant related user using the following URI:

```
GET https://<connection-server>/vmrest/users?query=(TenantObjectId is <Tenant-ObjectId>)
```

To get the TenantObjectID, use the following URI:

```
GET https://<connection-server>/vmrest/tenants
```

### Viewing the
                           	 Details of a Specific User

The following is an example of the GET request that lists the details of specific user represented by the provided value of
                                 object ID:

```
GET https://<connection-server>/vmrest/users/<user-objectId>
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
<User>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</URI>
  <ObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectId>
  <UseDefaultLanguage>true</UseDefaultLanguage>
  <FirstName>jsdghj</FirstName>
  <Initials>efjoe</Initials>
  <LastName>djghfjk</LastName>
  <Alias>Texoma</Alias>
  <City/>
  <State/>
  <Country>US</Country>
  <PostalCode/>
  <Department/>
  <Manager/>
  <Title>eoufowe</Title>
  <Building/>
  <EmployeeId>2343</EmployeeId>
  <Address/>
  <DisplayName>user_Opera_1</DisplayName>
  <BillingId/>
  <TimeZone>190</TimeZone>
  <CreationTime>2013-03-05T11:24:33Z</CreationTime>
  <IsTemplate>false</IsTemplate>
  <DtmfNameFirstLast>5734453544355</DtmfNameFirstLast>
  <DtmfNameLastFirst>3544355573445</DtmfNameLastFirst>
  <CosObjectId>8ab2b94d-1531-4589-865f-27bd3eea8adc</CosObjectId>
  <CosURI>/vmrest/coses/8ab2b94d-1531-4589-865f-27bd3eea8adc</CosURI>
  <Language>1033</Language>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <AddressMode>0</AddressMode>
  <ClockMode>0</ClockMode>
  <ConversationTui>SubMenu</ConversationTui>
  <GreetByName>true</GreetByName>
  <ListInDirectory>true</ListInDirectory>
  <IsVmEnrolled>true</IsVmEnrolled>
  <SayCopiedNames>true</SayCopiedNames>
  <SayDistributionList>true</SayDistributionList>
  <SayMsgNumber>true</SayMsgNumber>
  <SaySender>true</SaySender>
  <SayTimestampAfter>true</SayTimestampAfter>
  <SayTimestampBefore>false</SayTimestampBefore>
  <SayTotalNew>false</SayTotalNew>
  <SayTotalNewEmail>false</SayTotalNewEmail>
  <SayTotalNewFax>false</SayTotalNewFax>
  <SayTotalNewVoice>true</SayTotalNewVoice>
  <SayTotalReceipts>false</SayTotalReceipts>
  <SayTotalSaved>true</SayTotalSaved>
  <Speed>100</Speed>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <Undeletable>false</Undeletable>
  <UseBriefPrompts>false</UseBriefPrompts>
  <Volume>50</Volume>
  <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
  <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
  <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
  <EncryptPrivateMessages>false</EncryptPrivateMessages>
  <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
  <SayAltGreetWarning>false</SayAltGreetWarning>
  <SaySenderExtension>false</SaySenderExtension>
  <SayAni>false</SayAni>
  <XferString/>
  <CallAnswerTimeout>4</CallAnswerTimeout>
  <CallHandlerObjectId>287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</CallhandlerURI>
  <MessageTypeMenu>false</MessageTypeMenu>
  <NewMessageSortOrder>1</NewMessageSortOrder>
  <SavedMessageSortOrder>2</SavedMessageSortOrder>
  <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
  <NewMessageStackOrder>1234567</NewMessageStackOrder>
  <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
  <EnablePersonalRules>true</EnablePersonalRules>
  <RecordUnknownCallerName>true</RecordUnknownCallerName>
  <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHGreeting</ExitTargetConversation>
  <PromptSpeed>100</PromptSpeed>
  <ExitTargetHandlerObjectId>55af319d-7a26-40ad-9b20-153ee1f39e99</ExitTargetHandlerObjectId>
  <RepeatMenu>1</RepeatMenu>
  <FirstDigitTimeout>5000</FirstDigitTimeout>
  <InterdigitDelay>3000</InterdigitDelay>
  <PromptVolume>50</PromptVolume>
  <ExitCallActionObjectId>2b3566bd-0339-43a4-85a1-09ab3177f0e9</ExitCallActionObjectId>
  <AddressAfterRecord>false</AddressAfterRecord>
  <DtmfAccessId>99934</DtmfAccessId>
  <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
  <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
  <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
  <IsClockMode24Hour>false</IsClockMode24Hour>
  <SynchScheduleObjectId>58dce2eb-9d6d-4621-b81d-a56c80b83897</SynchScheduleObjectId>
  <SynchScheduleURI>/vmrest/schedules/58dce2eb-9d6d-4621-b81d-a56c80b83897</SynchScheduleURI>
  <RouteNDRToSender>true</RouteNDRToSender>
  <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
  <VoiceNameRequired>false</VoiceNameRequired>
  <SendBroadcastMsg>false</SendBroadcastMsg>
  <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
  <ConversationVui>VuiStart</ConversationVui>
  <ConversationName>SubMenu</ConversationName>
  <SpeechCompleteTimeout>0</SpeechCompleteTimeout> 
  <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
  <UseVui>false</UseVui>
  <SkipPasswordForKnownDevice>true</SkipPasswordForKnownDevice>
  <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
  <UseDefaultTimeZone>true</UseDefaultTimeZone>
  <EnableMessageLocator>false</EnableMessageLocator>
  <DtmfNameFirst>573445</DtmfNameFirst>
  <DtmfNameLast>3544355</DtmfNameLast>
  <AssistantRowsPerPage>5</AssistantRowsPerPage>
  <InboxMessagesPerPage>20</InboxMessagesPerPage>
  <InboxAutoRefresh>15</InboxAutoRefresh>
  <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
  <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
  <ReadOnly>false</ReadOnly>
  <EnableTts>true</EnableTts>
  <SmtpAddress>user_operator_1@ucbu-aricent-vm463.cisco.com</SmtpAddress>
  <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
  <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
  <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
  <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
  <SpeechSensitivity>50</SpeechSensitivity>
  <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
  <ContinuousAddMode>false</ContinuousAddMode>
  <NameConfirmation>false</NameConfirmation>
  <CommandDigitTimeout>1500</CommandDigitTimeout>
  <SaveMessageOnHangup>false</SaveMessageOnHangup>
  <SendMessageOnHangup>1</SendMessageOnHangup>
  <SkipForwardTime>5000</SkipForwardTime>
  <SkipReverseTime>5000</SkipReverseTime>
  <UseShortPollForCache>true</UseShortPollForCache>
  <SearchByExtensionSearchSpaceObjectId>5d004dee-14ef-4fc4-83b8-850274628286</SearchByExtensionSearchSpaceObjectId>
  <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/5d004dee-14ef-4fc4-83b8-850274628286</SearchByExtensionSearchSpaceURI>
  <SearchByNameSearchSpaceObjectId>5d004dee-14ef-4fc4-83b8-850274628286</SearchByNameSearchSpaceObjectId>
  <SearchByNameSearchSpaceURI>/vmrest/searchspaces/5d004dee-14ef-4fc4-83b8-850274628286</SearchByNameSearchSpaceURI>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <Inactive>false</Inactive> 
  <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
  <LdapType>1</LdapType>
  <FaxServerObjectId>1564dbbc-002f-47b9-a0f3-38f2cd6e2d87</FaxServerObjectId>
  <FaxServerURI>/vmrest/faxservers/1564dbbc-002f-47b9-a0f3-38f2cd6e2d87</FaxServerURI>
  <MwisURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/9375d893-c8eb-437b-90bf-    7de4b1d0c3e8/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists</PrivateListsURI>
  <UserWebPasswordURI>/vmrest/users/7e048531-acdf-460b-884e-415be712d0bc/credential/password</UserWebPasswordURI>
  <UserVoicePinURI>/vmrest/users/7e048531-acdf-460b-884e-415be712d0bc/credential/pin</UserVoicePinURI>
  <UserRoleURI>/vmrest/users/7e048531-acdf-460b-884e-415be712d0bc/userroles</UserRoleURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%209375d893-c8eb-437b-90bf-7de4b1d0c3e8)</SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%209375d893-c8eb-437b-90bf-7de4b1d0c3e8)  </AlternateNamesURI>
</User>
```

```
Response Code: 200
```

JSON Example

To view the details of particular user, do the following:

```
GET https://<connection-server>/vmrest/users?query=(emailaddress is abc@cisco.com)
Accept: application/json
Connection: keep_alive
```

```
{
  "URI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1"
  "ObjectId":"6c91a90f-0771-492b-a7a5-083ea246a7e1"
  "UseDefaultLanguage":"true"
  "Alias":"Texoma"
  "DisplayName":"Texoma"
  "TimeZone":"190"
  "CreationTime":"2013-03-14T10:54:47Z"
  "IsTemplate":"false"
  "CosObjectId":"844e18ef-884c-4f43-b9ce-1dc0d53196c2"
  "CosURI":"/vmrest/coses/844e18ef-884c-4f43-b9ce-1dc0d53196c2"
  "Language":"1033"
  "LocationObjectId":"42a9ab40-490d-4819-9bfb-8ddce4f430ff"
  "LocationURI":"/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff"
  "AddressMode":"0"
  "ClockMode":"0"
  "ConversationTui":"SubMenu"
  "GreetByName":"true"
  "ListInDirectory":"true"
  "IsVmEnrolled":"true"
  "SayCopiedNames":"true"
  "SayDistributionList":"true"
  "SayMsgNumber":"true"
  "SaySender":"true"
  "SayTimestampAfter":"true"
  "SayTimestampBefore":"false"
  "SayTotalNew":"true"
  "SayTotalNewEmail":"true"
  "SayTotalNewFax":"false"
  "SayTotalNewVoice":"true"
  "SayTotalReceipts":"false"
  "SayTotalSaved":"true"
  "Speed":"100"
  "MediaSwitchObjectId":"ec1e2636-fc14-44fc-8cda-d6c1a3d61150"
  "PhoneSystemURI":"/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150"
  "Undeletable":"false"
  "UseBriefPrompts":"false"
  "Volume":"50"
  "EnAltGreetDontRingPhone":"false"
  "EnAltGreetPreventSkip":"false"
  "EnAltGreetPreventMsg":"false"
  "EncryptPrivateMessages":"false"
  "DeletedMessageSortOrder":"2"
  "SayAltGreetWarning":"false"
  "SaySenderExtension":"false"
  "SayAni":"false"
  "CallAnswerTimeout":"4"
  "CallHandlerObjectId":"fc2f99c4-31ac-465b-b143-5d21c760439c"
  "CallhandlerURI":"/vmrest/handlers/callhandlers/fc2f99c4-31ac-465b-b143-5d21c760439c"
  "MessageTypeMenu":"false"
  "NewMessageSortOrder":"1"
  "SavedMessageSortOrder":"2"
  "MessageLocatorSortOrder":"1"
  "NewMessageStackOrder":"1234567"
  "SavedMessageStackOrder":"1234567"
  "EnablePersonalRules":"true"
  "RecordUnknownCallerName":"true"
  "RingPrimaryPhoneFirst":"false"
  "ExitAction":"2"
  "ExitTargetConversation":"PHGreeting"
  "PromptSpeed":"100"
  "ExitTargetHandlerObjectId":"939d4d12-cec8-4fee-ae47-fbf0cf20c33e"
  "RepeatMenu":"1"
  "FirstDigitTimeout":"5000"
  "InterdigitDelay":"3000"
  "PromptVolume":"50"
  "ExitCallActionObjectId":"a5ab392f-dce6-4de2-af7f-92f9ebd14300"
  "AddressAfterRecord":"false"
  "DtmfAccessId":"12345"
  "ConfirmDeleteMessage":"false"
  "ConfirmDeleteDeletedMessage":"false"
  "ConfirmDeleteMultipleMessages":"true"
  "IsClockMode24Hour":"false"
  "SynchScheduleObjectId":"214cc45c-db48-44c6-a239-aa4c5e65e32a"
  "SynchScheduleURI":"/vmrest/schedules/214cc45c-db48-44c6-a239-aa4c5e65e32a"
  "RouteNDRToSender":"true"
  "IsSetForVmEnrollment":"true"
  "VoiceNameRequired":"false"
  "SendBroadcastMsg":"false"
  "UpdateBroadcastMsg":"false"
  "ConversationVui":"VuiStart"
  "ConversationName":"SubMenu"
  "SpeechCompleteTimeout":"0"
  "SpeechIncompleteTimeout":"750"
  "UseVui":"false"
  "SkipPasswordForKnownDevice":"false"
  "JumpToMessagesOnLogin":"false"
  "UseDefaultTimeZone":"true"
  "EnableMessageLocator":"false"
  "AssistantRowsPerPage":"5"
  "InboxMessagesPerPage":"20"
  "InboxAutoRefresh":"15"
  "InboxAutoResolveMessageRecipients":"true"
  "PcaAddressBookRowsPerPage":"5"
  "ReadOnly":"false"
  "EnableTts":"true"
  "SmtpAddress":"vishu11@ucbu-aricent-vm463.cisco.com"
  "ConfirmationConfidenceThreshold":"60"
  "AnnounceUpcomingMeetings":"60"
  "SpeechConfidenceThreshold":"40"
  "SpeechSpeedVsAccuracy":"50"
  "SpeechSensitivity":"50"
  "EnableVisualMessageLocator":"false"
  "ContinuousAddMode":"false"
  "NameConfirmation":"false"
  "CommandDigitTimeout":"1500"
  "SaveMessageOnHangup":"false"
  "SendMessageOnHangup":"1"
  "SkipForwardTime":"5000"
  "SkipReverseTime":"5000"
  "UseShortPollForCache":"false"
  "SearchByExtensionSearchSpaceObjectId":"877942bf-6600-4b7a-809d-159199cfc2ec"
  "SearchByExtensionSearchSpaceURI":"/vmrest/searchspaces/877942bf-6600-4b7a-809d-159199cfc2ec"
  "SearchByNameSearchSpaceObjectId":"877942bf-6600-4b7a-809d-159199cfc2ec"
  "SearchByNameSearchSpaceURI":"/vmrest/searchspaces/877942bf-6600-4b7a-809d-159199cfc2ec"
  "PartitionObjectId":"da2114bf-cde7-43d8-9709-cd3895a9d41b"
  "PartitionURI":"/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b"
  "Inactive": "false",
  "UseDynamicNameSearchWeight":"false"
  "LdapType":"0"
  "MwisURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/mwis"
  "NotificationDevicesURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/notificationdevices"
  "MessageHandlersURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/messagehandlers"
  "ExternalServiceAccountsURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/externalserviceaccounts"
  "AlternateExtensionsURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/alternateextensions"
  "PrivateListsURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/privatelists"
  "SmtpProxyAddressesURI":"/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%206c91a90f-0771-492b-a7a5-083ea246a7e1)"
  "AlternateNamesURI":"/vmrest/alternatenames?query=(GlobalUserObjectId%20is%206c91a90f-0771-492b-a7a5-083ea246a7e1)"
}
```

```
Response Code: 200
```

### Creating a
                           	 User

This request can be used to
                                 		  create a new user. The mandatory fields for creation of a user are alias and
                                 		  DtmfAccessId. The URI for getting user template alias is:

```
https://<connection-server>/vmrest/usertemplates.
```

The URI for getting MailboxStoreObjectId is:

```
https://<connection-server>/vmrest/mailboxstores.
```

The ObjectId field in the response body of above URI is used as
                                 		  MailboxStoreObjectId. Users can be created in two ways:

This creates the user using default mailbox store:

```
POST https://<connection-server>/vmrest/users?templateAlias=<usertemplatealias>
```

This creates the user using specified mailbox store object ID:

```
POST https://<connection-server>/vmrest/users?templateAlias=<usertemplateAlias>&MailboxStoreObjectId=<mailboxStore-ObjectId>
```

```
<User>
  <Alias>texoma</Alias>
  <DtmfAccessId >123422</DtmfAccessId >
</User>
```

The following is the response from the above *POST* request and
                                          				the actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/f82b301d-1ec8-44c6-a3ee-0012269439bf
```

JSON Example

To create user, do the following:

```
POST https://<Connection-server>/vmrest/users?templateAlias=voicemailusertemplate
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
  "Alias":"voicemailusertemplate1",
  "DisplayName":"Voice Mail User Template 1"
}
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/f82b301d-1ec8-44c6-a3ee-0012269439bf
```

### Updating a
                           	 User

The following is an example of
                                 		  the PUT request that update details of a user:

```
PUT https://<connection-server>/vmrest/users/<user-objectid>
```

```
<User> 
  <Alias>Texoma</Alias>
  <UseShortPollForCache> true</UseShortPollForCache>
  <ListInDirectory>true </ListInDirectory>
  <SkipPasswordForKnownDevice>true </SkipPasswordForKnownDevice>
  <IsVmEnrolled> true</IsVmEnrolled>
  <RouteNDRToSender >true</RouteNDRToSender >
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150 </MediaSwitchObjectId>
  <DtmfAccessId>99934</DtmfAccessId>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <Inactive>false</Inactive> 
  <CosObjectId>8ab2b94d-1531-4589-865f-27bd3eea8adc</CosObjectId>
  <SearchByExtensionSearchSpaceObjectId>877942bf-6600-4b7a-809d-159199cfc2ec</SearchByExtensionSearchSpaceObjectId>
</User>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update details of a user:

```
PUT https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
  "DtmfAccessId":"123”
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Update Language
                              	 and TimeZone:

URI for timezone:

```
https://<Connection-server>/vmrest/timezones
```

URI for installed Languages:

```
https://<Connection-server>/vmrest/installedlanguages
```

URI to get Language code:

```
https://<Connection-server>/vmrest/languagemap
```

```
<User>
 <UseDefaultTimeZone>false</UseDefaultTimeZone>
 <TimeZone>175</TimeZone>
 <UseDefaultLanguage>false</UseDefaultLanguage>
 <Language>1034</Language>
</User>
```

```
Response Code: 204
```

JSON Example

To delete a user, do the following:

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep_alive
```

```
Response Code: 204
```

### Delete a
                           	 User

The following is an example of
                                 		  the DELETE request that can be used to delete a user:

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>
```

```
Response Code: 204
```

JSON Example

To delete a user, do the following:

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep_alive
```

```
Response Code: 204
```

### Explanation of
                           	 Data Fields:

Possible values:

- true: if user is inactive.

- false: if user is active.

Default Value: false

The administrators enter the alias to sign in to Cisco Unity Connection Administration.

- true: if default time zone is to be used

- false: to use specific time zone, if false is selected timezone should be also specified.

- 0-Do not Integrate with LDAP directory.

- 1-Integrate with LDAP directory

- 2-Authenticate

- 4-Inactive

Default Value: 0

Possible values:

- true: if user template

- false: if user

Default Value: false

Possible values:

- false: The enrollment conversation is not played for the subscriber when they login.

- true: The enrollment conversation is played for the subscriber when they login.

Default value: true

Possible values:

- false: Do not Skip PIN When Calling From a Known Extension

- true: Skip PIN When Calling From a Known Extension

Default value: false

Possible values:

- false: Do not list in Directory

- true: List in directory

Default value: false

Possible values:

- false: The subscriber's polling cycle is determined by the system default polling cycle. (System configuration setting "Normal
                                                   Calendar Caching Poll Interval").

- true: The shorter "power user" polling cycle is used. (System configuration setting "Short Calendar Caching Poll Interval").

Default value : false

Possible values:

- true: Send Non-Delivery Receipts on Failed Message Delivery.

- false: Do not Send Non-Delivery Receipts on Failed Message Delivery.

Default value: true

Possible values:

- true: For default users

- false: For other created users

Possible values:

- false: Do not create matching SMTP proxy address.

- true: Create matching SMTP proxy address.

Default value: false MailboxStoreName Read Only String Mailbox store name used by the user

## Admin User API

Cisco Unity Connection 12.5 SU3 and later, supports Admin User API. Administrator can use this API to create/update/delete/fetch
                           the users who does not have mailbox using Admin User API. Various attributes of user without mailbox, for example first name,
                           last name, display name, alias, time zone, language, password, roles, password settings, can also be updated using this API
                           .

### Listing Admin Users without Mailbox

The request can be used to fetch the list of all users without mailbox.

```
GET https://<connection-server>/vmrest/adminusers
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
<Users total="4">
   <User>
      <URI>/vmrest/adminusers/c8a3a38b-df1a-4612-9679-d1fddc790e95</URI>
      <ObjectId>c8a3a38b-df1a-4612-9679-d1fddc790e95</ObjectId>
      <UseDefaultLanguage>true</UseDefaultLanguage>
      <Alias>admin</Alias>
      <DisplayName>admin</DisplayName>
      <TimeZone>190</TimeZone>
      <CreationTime>2020-07-28T10:13:15Z</CreationTime>
      <IsTemplate>false</IsTemplate>
      <Language>1033</Language>
      <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
      <Undeletable>true</Undeletable>
      <UseDefaultTimeZone>true</UseDefaultTimeZone>
      <ReadOnly>true</ReadOnly>
      <SmtpAddress>admin@ucbu-aricent-vm405.cisco.com</SmtpAddress>
      <LdapType>0</LdapType>
      <UserWebPasswordURI>/vmrest/users/c8a3a38b-df1a-4612-9679-d1fddc790e95/credential/password</UserWebPasswordURI>
      <UserRoleURI>/vmrest/users/c8a3a38b-df1a-4612-9679-d1fddc790e95/userroles</UserRoleURI>
   </User>
   <User>
      <URI>/vmrest/adminusers/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2</URI>
      <ObjectId>0b008d28-a8ce-4d14-aa6f-3b584d3d43d2</ObjectId>
      <UseDefaultLanguage>true</UseDefaultLanguage>
      <FirstName>Cisco Unity Connection</FirstName>
      <LastName>Messaging System</LastName>
      <Alias>UnityConnection</Alias>
      <DisplayName>Cisco Unity Connection Messaging System</DisplayName>
      <TimeZone>190</TimeZone>
      <CreationTime>2020-07-28T10:13:15Z</CreationTime>
      <IsTemplate>false</IsTemplate>
      <Language>1033</Language>
      <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
      <Undeletable>true</Undeletable>
      <UseDefaultTimeZone>true</UseDefaultTimeZone>
      <ReadOnly>true</ReadOnly>
      <SmtpAddress>unityconnection@ucbu-aricent-vm405.cisco.com</SmtpAddress>
      <LdapType>0</LdapType>
      <UserWebPasswordURI>/vmrest/users/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2/credential/password</UserWebPasswordURI>
      <UserRoleURI>/vmrest/users/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2/userroles</UserRoleURI>
   </User>
   <User>
      <URI>/vmrest/adminusers/6fd02048-a02c-4bb8-a440-c6c063cb3dcd</URI>
      <ObjectId>6fd02048-a02c-4bb8-a440-c6c063cb3dcd</ObjectId>
      <UseDefaultLanguage>true</UseDefaultLanguage>
      <FirstName>Replication</FirstName>
      <LastName>Agent</LastName>
      <Alias>Replication</Alias>
      <DisplayName>Replication Agent (ucbu-aricent-vm405)</DisplayName>
      <TimeZone>190</TimeZone>
      <CreationTime>2020-07-28T10:13:18Z</CreationTime>
      <IsTemplate>false</IsTemplate>
      <Language>1033</Language>
      <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
      <Undeletable>true</Undeletable>
      <UseDefaultTimeZone>true</UseDefaultTimeZone>
      <ReadOnly>true</ReadOnly>
      <SmtpAddress>replication@ucbu-aricent-vm405.cisco.com</SmtpAddress>
      <LdapType>0</LdapType>
      <UserWebPasswordURI>/vmrest/users/6fd02048-a02c-4bb8-a440-c6c063cb3dcd/credential/password</UserWebPasswordURI>
      <UserRoleURI>/vmrest/users/6fd02048-a02c-4bb8-a440-c6c063cb3dcd/userroles</UserRoleURI>
   </User>
   <User>
      <URI>/vmrest/adminusers/0347d21e-c238-4079-8d77-662499c058ba</URI>
      <ObjectId>0347d21e-c238-4079-8d77-662499c058ba</ObjectId>
      <UseDefaultLanguage>true</UseDefaultLanguage>
      <FirstName>George</FirstName>
      <Initials>GD</Initials>
      <LastName>Davis</LastName>
      <Alias>Davis</Alias>
      <State>Mumbai</State>
      <Title>Trainee</Title>
      <Address>HNo4 Street Ville Parle</Address>
      <DisplayName>George</DisplayName>
      <TimeZone>190</TimeZone>
      <CreationTime>2020-07-29T09:03:42Z</CreationTime>
      <IsTemplate>false</IsTemplate>
      <Language>1033</Language>
      <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
      <Undeletable>false</Undeletable>
      <UseDefaultTimeZone>true</UseDefaultTimeZone>
      <ReadOnly>false</ReadOnly>
      <SmtpAddress>davis@ucbu-aricent-vm405.cisco.com</SmtpAddress>
      <LdapType>3</LdapType>
      <UserWebPasswordURI>/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/credential/password</UserWebPasswordURI>
      <UserRoleURI>/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/userroles</UserRoleURI>
   </User>
</Users>
```

```
Response Code: 200
```

JSON Example

To view the list of admin users, do the following:

```
GET https://<connection-server>/vmrest/adminusers
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
{
   "@total": "4",
   "User":    [
            {
         "URI": "/vmrest/adminusers/c8a3a38b-df1a-4612-9679-d1fddc790e95",
         "ObjectId": "c8a3a38b-df1a-4612-9679-d1fddc790e95",
         "UseDefaultLanguage": "true",
         "Alias": "admin",
         "DisplayName": "admin",
         "TimeZone": "190",
         "CreationTime": "2020-07-28T10:13:15Z",
         "IsTemplate": "false",
         "Language": "1033",
         "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
         "Undeletable": "true",
         "UseDefaultTimeZone": "true",
         "ReadOnly": "true",
         "SmtpAddress": "admin@ucbu-aricent-vm405.cisco.com",
         "LdapType": "0",
         "UserWebPasswordURI": "/vmrest/users/c8a3a38b-df1a-4612-9679-d1fddc790e95/credential/password",
         "UserRoleURI": "/vmrest/users/c8a3a38b-df1a-4612-9679-d1fddc790e95/userroles"
      },
            {
         "URI": "/vmrest/adminusers/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2",
         "ObjectId": "0b008d28-a8ce-4d14-aa6f-3b584d3d43d2",
         "UseDefaultLanguage": "true",
         "FirstName": "Cisco Unity Connection",
         "LastName": "Messaging System",
         "Alias": "UnityConnection",
         "DisplayName": "Cisco Unity Connection Messaging System",
         "TimeZone": "190",
         "CreationTime": "2020-07-28T10:13:15Z",
         "IsTemplate": "false",
         "Language": "1033",
         "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
         "Undeletable": "true",
         "UseDefaultTimeZone": "true",
         "ReadOnly": "true",
         "SmtpAddress": "unityconnection@ucbu-aricent-vm405.cisco.com",
         "LdapType": "0",
         "UserWebPasswordURI": "/vmrest/users/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2/credential/password",
         "UserRoleURI": "/vmrest/users/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2/userroles"
      },
            {
         "URI": "/vmrest/adminusers/6fd02048-a02c-4bb8-a440-c6c063cb3dcd",
         "ObjectId": "6fd02048-a02c-4bb8-a440-c6c063cb3dcd",
         "UseDefaultLanguage": "true",
         "FirstName": "Replication",
         "LastName": "Agent",
         "Alias": "Replication",
         "DisplayName": "Replication Agent (ucbu-aricent-vm405)",
         "TimeZone": "190",
         "CreationTime": "2020-07-28T10:13:18Z",
         "IsTemplate": "false",
         "Language": "1033",
         "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
         "Undeletable": "true",
         "UseDefaultTimeZone": "true",
         "ReadOnly": "true",
         "SmtpAddress": "replication@ucbu-aricent-vm405.cisco.com",
         "LdapType": "0",
         "UserWebPasswordURI": "/vmrest/users/6fd02048-a02c-4bb8-a440-c6c063cb3dcd/credential/password",
         "UserRoleURI": "/vmrest/users/6fd02048-a02c-4bb8-a440-c6c063cb3dcd/userroles"
      },
            {
         "URI": "/vmrest/adminusers/0347d21e-c238-4079-8d77-662499c058ba",
         "ObjectId": "0347d21e-c238-4079-8d77-662499c058ba",
         "UseDefaultLanguage": "true",
         "FirstName": "George",
         "Initials": "GD",
         "LastName": "Davis",
         "Alias": "Davis",
         "State": "Mumbai",
         "Title": "Trainee",
         "Address": "HNo4 Street Ville Parle",
         "DisplayName": "George",
         "TimeZone": "190",
         "CreationTime": "2020-07-29T09:03:42Z",
         "IsTemplate": "false",
         "Language": "1033",
         "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
         "Undeletable": "false",
         "UseDefaultTimeZone": "true",
         "ReadOnly": "false",
         "SmtpAddress": "davis@ucbu-aricent-vm405.cisco.com",
         "LdapType": "3",
         "UserWebPasswordURI": "/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/credential/password",
         "UserRoleURI": "/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/userroles"
      }
   ]
}
```

```
Response Code: 200
```

### Viewing Details of Admin User without Mailbox

The following is an example of the GET request that lists the details of specific user without mailbox represented by the
                                 provided value of object ID:

```
GET https://<connection-server>/vmrest/adminusers/<user-objectId>
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
<User>
   <URI>/vmrest/adminusers/0347d21e-c238-4079-8d77-662499c058ba</URI>
   <ObjectId>0347d21e-c238-4079-8d77-662499c058ba</ObjectId>
   <UseDefaultLanguage>true</UseDefaultLanguage>
   <FirstName>George</FirstName>
   <Initials>GD</Initials>
   <LastName>Davis</LastName>
   <Alias>Davis</Alias>
   <State>Mumbai</State>
   <Title>Trainee</Title>
   <Address>HNo4 Street Ville Parle</Address>
   <DisplayName>George</DisplayName>
   <TimeZone>190</TimeZone>
   <CreationTime>2020-07-29T09:03:42Z</CreationTime>
   <IsTemplate>false</IsTemplate>
   <Language>1033</Language>
   <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
   <Undeletable>false</Undeletable>
   <UseDefaultTimeZone>true</UseDefaultTimeZone>
   <ReadOnly>false</ReadOnly>
   <SmtpAddress>davis@ucbu-aricent-vm405.cisco.com</SmtpAddress>
   <LdapType>3</LdapType>
   <UserWebPasswordURI>/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/credential/password</UserWebPasswordURI>
   <UserRoleURI>/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/userroles</UserRoleURI>
</User>
```

```
Response Code: 200
```

JSON Example

To view the details of particular user, do the following:

```
GET https://<connection-server>/vmrest/adminusers/{user-objectId}
Accept: application/json
Connection: keep_alive
```

```
{
   "URI": "/vmrest/adminusers/0347d21e-c238-4079-8d77-662499c058ba",
   "ObjectId": "0347d21e-c238-4079-8d77-662499c058ba",
   "UseDefaultLanguage": "true",
   "FirstName": "George",
   "Initials": "GD",
   "LastName": "Davis",
   "Alias": "Davis",
   "State": "Mumbai",
   "Title": "Trainee",
   "Address": "HNo4 Street Ville Parle",
   "DisplayName": "George",
   "TimeZone": "190",
   "CreationTime": "2020-07-29T09:03:42Z",
   "IsTemplate": "false",
   "Language": "1033",
   "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
   "Undeletable": "false",
   "UseDefaultTimeZone": "true",
   "ReadOnly": "false",
   "SmtpAddress": "davis@ucbu-aricent-vm405.cisco.com",
   "LdapType": "3",
   "UserWebPasswordURI": "/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/credential/password",
   "UserRoleURI": "/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/userroles"
}
```

```
Response Code: 200
```

### Creating Admin User without Mailbox

This request can be used to create a new user who does not have a mailbox.The mandatory fields for creation of a user are
                                 alias and templateAlias.

This creates the admin user using default administratortemplate:

```
POST https://<connection-server>/vmrest/adminusers?templateAlias=<administratortemplate>
```

```
<user>
<Alias>Davis</Alias>
<DisplayName>George</DisplayName>
<FirstName>George</FirstName>
<LastName>Davis</LastName>
<TimeZone>190</TimeZone>
<UseDefaultTimeZone>true</UseDefaultTimeZone>
<IsTemplate>false</IsTemplate>
<Language>1033</Language>
<UseDefaultLanguage>true</UseDefaultLanguage>
<LdapType>3</LdapType>
<Initials>GD</Initials>
<Title>Trainee</Title>
<Address>HNo4 Street Ville Parle</Address>
<State>Mumbai</State>
<Undeletable>false</Undeletable>
</user>
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                          by you:

```
Response Code: 201
/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba
```

JSON Example

To create user, do the following:

```
POST https://<Connection-server>/vmrest/adminusers?templateAlias=administratortemplate
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
  "UseDefaultLanguage" : "true"
  "Alias":"Davis",
  "DisplayName":"George"
  "FirstName" : "George"
  "LastName" : "Davis"
  "TimeZone":"190"
  "UseDefaultTimeZone" : "true"
  "IsTemplate" : "false"
  "Language" : "1033"
  "LdapType" : "3"
  "Initials" : "GD"
  "Title" : "Trainee"
  "Address" : "HNo4 Street Ville Parle"
  "State" : "Mumbai"
  "Undeletable" : "false"
}
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 201
/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba
```

### Updating Admin User without Mailbox

The following is an example of the PUT request that update details of a user without mailbox:

```
PUT https://<connection-server>/vmrest/adminusers/<user-objectid>
```

```
<user>
<Alias>Texoma</Alias>
<DisplayName>richardtexoma</DisplayName>
<IsTemplate>false</IsTemplate>
<Language>1020</Language>
<LocationObjectId>35ac99ba-e098-4195-9ffb-cecb5a7cab65</LocationObjectId>
<Undeletable>true</Undeletable>
<UseDefaultTimeZone>true</UseDefaultTimeZone>
<ReadOnly>true</ReadOnly>
<TimeZone>140</TimeZone>
</user>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

JSON Example

To update details of a user:

```
PUT https://<connection-server>/vmrest/adminusers/<user-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
  "TimeZone":"170”
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

### Deleting Admin User without Mailbox

The following is an example of the DELETE request that can be used to delete a user who does not have a mailbox:

```
DELETE https://<connection-server>/vmrest/adminusers/<user-objectid>
```

```
Response Code: 204
```

JSON Example

To delete a user, do the following:

```
DELETE https://<connection-server>/vmrest/adminusers/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep_alive
```

```
Response Code: 204
```

### Explanation of Data Fields

Possible values:

- true: if user is inactive.

- false: if user is active.

Default Value: false

- true: if default time zone is to be used

- false: to use specific time zone, if false is selected timezone should be also specified.

- 0-Not integrated with LDAP directory.

- 3-Integrated with LDAP directory

Default Value: 0

Possible values:

- true: if user template

- false: if user

Default Value: false

Possible values:

- true: For default users

- false: For other created users

| GET https://<connection-server>/vmrest/users |
|---|

| <Users total="2">
 <User>
  <URI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</URI>
  <ObjectId>4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</ObjectId>
  <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
  <Alias>undeliverablemessagesmailbox</Alias>
  <DisplayName>Undeliverable Messages</DisplayName>
  <TimeZone>0</TimeZone>
  <CreationTime>2013-03-05T10:54:38Z</CreationTime>
  <CosObjectId>610c9c71-32be-4465-b61a-523f24a9d828</CosObjectId>
  <CosURI>/vmrest/coses/610c9c71-32be-4465-b61a-523f24a9d828</CosURI>
  <Language>0</Language>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <ListInDirectory>false</ListInDirectory>
  <IsVmEnrolled>true</IsVmEnrolled>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <CallHandlerObjectId>13a3c5fc-f706-4bd0-aeeb-32dad2c4a29b</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/13a3c5fc-f706-4bd0-aeeb-32dad2c4a29b</CallhandlerURI>
  <DtmfAccessId>99999</DtmfAccessId>
  <VoiceNameRequired>false</VoiceNameRequired>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <Inactive>false</Inactive>
  <MwisURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/privatelists</PrivateListsURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%204d5df6e3-a036-4f16-8f1e- d48e7e9b73c1)</SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%204d5df6e3-a036-4f16-8f1e-d48e7e9b73c1)              
</AlternateNamesURI>
 </User>
 <User>
  <URI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce</URI>
  <ObjectId>671fd8d1-7240-4e60-9194-0ec9c4a626ce</ObjectId>
  <Alias>operator</Alias>
  <DisplayName>Operator</DisplayName>
  <TimeZone>0</TimeZone>
  <CreationTime>2013-03-05 10:54:39.02</CreationTime>
  <CosObjectId>610c9c71-32be-4465-b61a-523f24a9d828</CosObjectId>
  <CosURI>/vmrest/coses/610c9c71-32be-4465-b61a-523f24a9d828</CosURI>
  <Language>0</Language>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <ListInDirectory>false</ListInDirectory>
  <IsVmEnrolled>true</IsVmEnrolled>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <CallHandlerObjectId>4546d6df-5120-4fb3-9719-8d521b8a5796</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/4546d6df-5120-4fb3-9719-8d521b8a5796</CallhandlerURI>
  <DtmfAccessId>99990</DtmfAccessId>
  <VoiceNameRequired>false</VoiceNameRequired>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId> 
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <Inactive>false</Inactive>
  <MwisURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/671fd8d1-7240-4e60-9194-0ec9c4a626ce/privatelists</PrivateListsURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%20671fd8d1-7240-4e60-9194-0ec9c4a626ce)</SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%20671fd8d1-7240-4e60-9194-0ec9c4a626ce) </AlternateNamesURI>
</User>
<User>
  <URI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9</URI>
  <ObjectId>8321097e-cca4-483f-b24c-0f2175e6e4c9</ObjectId>
  <FirstName>John</FirstName>
  <LastName>10000</LastName>
  <Alias>John10000</Alias>
  <City/>
  <Department/>
  <EmployeeId/>
  <DisplayName>John 10000</DisplayName>
  <EmailAddress>john@cisco.com</EmailAddress>
  <TimeZone>190</TimeZone>
  <CreationTime>2015-06-01T05:03:15Z</CreationTime>
  <CosObjectId>0a987b74-acf0-4310-ab81-4ebe0190cca4</CosObjectId>
  <CosURI>/vmrest/coses/0a987b74-acf0-4310-ab81-4ebe0190cca4</CosURI>
  <Language>1033</Language>
  <LocationObjectId>17f9c794-d4e4-453b-a9df-771c48c0590e</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/17f9c794-d4e4-453b-a9df-771c48c0590e</LocationURI>
  <ListInDirectory>true</ListInDirectory>
  <IsVmEnrolled>false</IsVmEnrolled>
  <MediaSwitchObjectId>6f37f783-437a-4c9b-aefe-74201f33deab</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/6f37f783-437a-4c9b-aefe-74201f33deab</PhoneSystemURI>
  <CallHandlerObjectId>be938317-6c75-4d67-9c9e-642ba90d85d1</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/be938317-6c75-4d67-9c9e-642ba90d85d1</CallhandlerURI>
  <DtmfAccessId>10000</DtmfAccessId>
  <VoiceNameRequired>false</VoiceNameRequired>
  <PartitionObjectId>30c21994-bd80-4992-97ce-601ca93bf3da</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/30c21994-bd80-4992-97ce-601ca93bf3da</PartitionURI>
  <Inactive>false</Inactive> 
  <MwisURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/privatelists</PrivateListsURI>
  <VideoServiceAccountsURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/videoserviceaccounts</VideoServiceAccountsURI>
  <UserWebPasswordURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/credential/password</UserWebPasswordURI>
  <UserMailboxURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/mailboxattributes</UserMailboxURI>
  <MailboxStoreName>Unity Messaging Database -1</MailboxStoreName>
  <UserVoicePinURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/credential/pin</UserVoicePinURI>
  <UserRoleURI>/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/userroles</UserRoleURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%208321097e-cca4-483f-b24c-0f2175e6e4c9)         </SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%208321097e-cca4-483f-b24c-0f2175e6e4c9)</AlternateNamesURI>
</User>
</Users> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users
Accept: application/json
Connection: keep_alive |
|---|

| {
  "Users": {
    "-total": "1",
    "User": {
      "URI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9",
      "ObjectId": "8321097e-cca4-483f-b24c-0f2175e6e4c9",
      "FirstName": "John",
      "LastName": "10000",
      "Alias": "John10000",
      "DisplayName": "John 10000",
      "EmailAddress": "john@cisco.com",
      "TimeZone": "190",
      "CreationTime": "2015-06-01T05:03:15Z",
      "CosObjectId": "0a987b74-acf0-4310-ab81-4ebe0190cca4",
      "CosURI": "/vmrest/coses/0a987b74-acf0-4310-ab81-4ebe0190cca4",
      "Language": "1033",
      "LocationObjectId": "17f9c794-d4e4-453b-a9df-771c48c0590e",
      "LocationURI": "/vmrest/locations/connectionlocations/17f9c794-d4e4-453b-a9df-771c48c0590e",
      "ListInDirectory": "true",
      "IsVmEnrolled": "false",
      "MediaSwitchObjectId": "6f37f783-437a-4c9b-aefe-74201f33deab",
      "PhoneSystemURI": "/vmrest/phonesystems/6f37f783-437a-4c9b-aefe-74201f33deab",
      "CallHandlerObjectId": "be938317-6c75-4d67-9c9e-642ba90d85d1",
      "CallhandlerURI": "/vmrest/handlers/callhandlers/be938317-6c75-4d67-9c9e-642ba90d85d1",
      "DtmfAccessId": "10000",
      "VoiceNameRequired": "false",
      "PartitionObjectId": "30c21994-bd80-4992-97ce-601ca93bf3da",
      "PartitionURI": "/vmrest/partitions/30c21994-bd80-4992-97ce-601ca93bf3da",
      "Inactive": "false",
      "MwisURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/mwis",
      "NotificationDevicesURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/notificationdevices",
      "MessageHandlersURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/messagehandlers",
      "ExternalServiceAccountsURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/externalserviceaccounts",
      "AlternateExtensionsURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/alternateextensions",
      "PrivateListsURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/privatelists",
      "VideoServiceAccountsURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/videoserviceaccounts",
      "UserWebPasswordURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/credential/password",
     "UserMailboxURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/mailboxattributes",
      "MailboxStoreName": "Unity Messaging Database -1",
      "UserVoicePinURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/credential/pin",
      "UserRoleURI": "/vmrest/users/8321097e-cca4-483f-b24c-0f2175e6e4c9/userroles",
      "SmtpProxyAddressesURI": "/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%208321097e-cca4-483f-b24c-0f2175e6e4c9)",
      "AlternateNamesURI": "/vmrest/alternatenames?query=(GlobalUserObjectId%20is%208321097e-cca4-483f-b24c-0f2175e6e4c9)"
    }
  }
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users?query=(emailaddress is <emailaddress@domain.com>)

GET https://<connection-server>/vmrest/users?query=(emailaddress startswith <emailaddress@domain.com>)

GET https://<connection-server>/vmrest/users?query=(emailaddress isnull)

GET https://<connection-server>/vmrest/users?query=(emailaddress isnotnull) |
|---|

| <User>
    <URI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1</URI>
    <ObjectId>fc78a2c6-3065-46a5-b5cb-0bba363280d1</ObjectId>
    <FirstName>abc</FirstName>
    <LastName></LastName>
    <Alias>abc</Alias>
    <City>
    </City>
    <Department>
    </Department>
    <EmployeeId>
    </EmployeeId>
    <DisplayName>abc</DisplayName>
    <EmailAddress>abc@cisco.com</EmailAddress>
    <TimeZone>190</TimeZone>
    <CreationTime>2016-05-11T09:51:04Z</CreationTime>
    <CosObjectId>4e1c04f4-eb53-4f19-aaa2-0982121fa8fd</CosObjectId>
    <CosURI>/vmrest/coses/4e1c04f4-eb53-4f19-aaa2-0982121fa8fd</CosURI>
    <Language>1033</Language>
    <LocationObjectId>44471f12-f7cb-4d99-80fe-672bf039faef</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/44471f12-f7cb-4d99-80fe-672bf039faef</LocationURI>
    <ListInDirectory>true</ListInDirectory>
    <IsVmEnrolled>false</IsVmEnrolled>
    <MediaSwitchObjectId>cf3e31a0-979f-4011-b239-0881cd9c4292</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/cf3e31a0-979f-4011-b239-0881cd9c4292</PhoneSystemURI>
    <CallHandlerObjectId>5e6a0ef4-4ffb-4654-a1ba-1a595ae76f7a</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5e6a0ef4-4ffb-4654-a1ba-1a595ae76f7a</CallhandlerURI>
    <DtmfAccessId>9899</DtmfAccessId>
    <VoiceNameRequired>false</VoiceNameRequired>
    <PartitionObjectId>7c789d46-449b-4ae4-b3f4-176e3b46bd18</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/7c789d46-449b-4ae4-b3f4-176e3b46bd18</PartitionURI>
    <Inactive>false</Inactive>
    <MwisURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/mwis</MwisURI>
    <NotificationDevicesURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/notificationdevices</NotificationDevicesURI>
    <MessageHandlersURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/messagehandlers</MessageHandlersURI>
    <ExternalServiceAccountsURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/externalserviceaccounts</ExternalServiceAccountsURI>
    <AlternateExtensionsURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/alternateextensions</AlternateExtensionsURI>
    <PrivateListsURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/privatelists</PrivateListsURI>
    <VideoServiceAccountsURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/videoserviceaccounts</VideoServiceAccountsURI>
    <UserWebPasswordURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/credential/password</UserWebPasswordURI>
    <UserMailboxURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/mailboxattributes</UserMailboxURI>
    <MailboxStoreName>Unity Messaging Database -1</MailboxStoreName>
    <UserVoicePinURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/credential/pin</UserVoicePinURI>
    <UserRoleURI>/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/userroles</UserRoleURI>
    <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%20fc78a2c6-3065-46a5-b5cb-0bba363280d1)</SmtpProxyAddressesURI>
    <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%20fc78a2c6-3065-46a5-b5cb-0bba363280d1)</AlternateNamesURI>
  </User> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users?query=(emailaddress is abc@cisco.com)
Accept: application/json
Connection: keep_alive |
|---|

| {
  "Users": {
    "-total": "1",
       "User": {
        "URI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1"
        "ObjectId":"fc78a2c6-3065-46a5-b5cb-0bba363280d1"
        "FirstName":"abc"
        "Alias":"abc"
        "DisplayName":"abc"
        "EmailAddress":"abc@cisco.com"
        "TimeZone":"190"
        "CreationTime":"2016-05-11T09:51:04Z"
        "CosObjectId":"4e1c04f4-eb53-4f19-aaa2-0982121fa8fd"
        "CosURI":"/vmrest/coses/4e1c04f4-eb53-4f19-aaa2-0982121fa8fd"
        "Language":"1033"
        "LocationObjectId":"44471f12-f7cb-4d99-80fe-672bf039faef"
        "LocationURI":"/vmrest/locations/connectionlocations/44471f12-f7cb-4d99-80fe-672bf039faef"
        "ListInDirectory":"true"
        "IsVmEnrolled":"false"
        "MediaSwitchObjectId":"cf3e31a0-979f-4011-b239-0881cd9c4292"
        "PhoneSystemURI":"/vmrest/phonesystems/cf3e31a0-979f-4011-b239-0881cd9c4292"
        "CallHandlerObjectId":"5e6a0ef4-4ffb-4654-a1ba-1a595ae76f7a"/CallHandlerObjectId"
        "CallhandlerURI":"/vmrest/handlers/callhandlers/5e6a0ef4-4ffb-4654-a1ba-1a595ae76f7a"
        "DtmfAccessId":"9899"
        "VoiceNameRequired":"false"
        "PartitionObjectId":"7c789d46-449b-4ae4-b3f4-176e3b46bd18"
        "PartitionURI":"/vmrest/partitions/7c789d46-449b-4ae4-b3f4-176e3b46bd18"
        "Inactive":"false"
        "MwisURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/mwis"
        "NotificationDevicesURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/notificationdevices"
        "MessageHandlersURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/messagehandlers"
        "ExternalServiceAccountsURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/externalserviceaccounts"
        "AlternateExtensionsURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/alternateextensions"
        "PrivateListsURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/privatelists"
        "VideoServiceAccountsURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/videoserviceaccounts"
        "UserWebPasswordURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/credential/password"
        "UserMailboxURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/mailboxattributes"
        "MailboxStoreName":"Unity Messaging Database -1"
        "UserVoicePinURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/credential/pin"
        "UserRoleURI":"/vmrest/users/fc78a2c6-3065-46a5-b5cb-0bba363280d1/userroles"
        "SmtpProxyAddressesURI":"/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%20fc78a2c6-3065-46a5-b5cb-0bba363280d1)"
        "AlternateNamesURI":"/vmrest/alternatenames?query=(GlobalUserObjectId%20is%20fc78a2c6-3065-46a5-b5cb-0bba363280d1)"
       }
      }
     } |
|---|

| GET https://<connection-server>/vmrest/users?query=(TenantObjectId is <Tenant-ObjectId>) |
|---|

| GET https://<connection-server>/vmrest/tenants |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectId> |
|---|

| <User>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</URI>
  <ObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</ObjectId>
  <UseDefaultLanguage>true</UseDefaultLanguage>
  <FirstName>jsdghj</FirstName>
  <Initials>efjoe</Initials>
  <LastName>djghfjk</LastName>
  <Alias>Texoma</Alias>
  <City/>
  <State/>
  <Country>US</Country>
  <PostalCode/>
  <Department/>
  <Manager/>
  <Title>eoufowe</Title>
  <Building/>
  <EmployeeId>2343</EmployeeId>
  <Address/>
  <DisplayName>user_Opera_1</DisplayName>
  <BillingId/>
  <TimeZone>190</TimeZone>
  <CreationTime>2013-03-05T11:24:33Z</CreationTime>
  <IsTemplate>false</IsTemplate>
  <DtmfNameFirstLast>5734453544355</DtmfNameFirstLast>
  <DtmfNameLastFirst>3544355573445</DtmfNameLastFirst>
  <CosObjectId>8ab2b94d-1531-4589-865f-27bd3eea8adc</CosObjectId>
  <CosURI>/vmrest/coses/8ab2b94d-1531-4589-865f-27bd3eea8adc</CosURI>
  <Language>1033</Language>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <AddressMode>0</AddressMode>
  <ClockMode>0</ClockMode>
  <ConversationTui>SubMenu</ConversationTui>
  <GreetByName>true</GreetByName>
  <ListInDirectory>true</ListInDirectory>
  <IsVmEnrolled>true</IsVmEnrolled>
  <SayCopiedNames>true</SayCopiedNames>
  <SayDistributionList>true</SayDistributionList>
  <SayMsgNumber>true</SayMsgNumber>
  <SaySender>true</SaySender>
  <SayTimestampAfter>true</SayTimestampAfter>
  <SayTimestampBefore>false</SayTimestampBefore>
  <SayTotalNew>false</SayTotalNew>
  <SayTotalNewEmail>false</SayTotalNewEmail>
  <SayTotalNewFax>false</SayTotalNewFax>
  <SayTotalNewVoice>true</SayTotalNewVoice>
  <SayTotalReceipts>false</SayTotalReceipts>
  <SayTotalSaved>true</SayTotalSaved>
  <Speed>100</Speed>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <Undeletable>false</Undeletable>
  <UseBriefPrompts>false</UseBriefPrompts>
  <Volume>50</Volume>
  <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
  <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
  <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
  <EncryptPrivateMessages>false</EncryptPrivateMessages>
  <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
  <SayAltGreetWarning>false</SayAltGreetWarning>
  <SaySenderExtension>false</SaySenderExtension>
  <SayAni>false</SayAni>
  <XferString/>
  <CallAnswerTimeout>4</CallAnswerTimeout>
  <CallHandlerObjectId>287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</CallhandlerURI>
  <MessageTypeMenu>false</MessageTypeMenu>
  <NewMessageSortOrder>1</NewMessageSortOrder>
  <SavedMessageSortOrder>2</SavedMessageSortOrder>
  <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
  <NewMessageStackOrder>1234567</NewMessageStackOrder>
  <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
  <EnablePersonalRules>true</EnablePersonalRules>
  <RecordUnknownCallerName>true</RecordUnknownCallerName>
  <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHGreeting</ExitTargetConversation>
  <PromptSpeed>100</PromptSpeed>
  <ExitTargetHandlerObjectId>55af319d-7a26-40ad-9b20-153ee1f39e99</ExitTargetHandlerObjectId>
  <RepeatMenu>1</RepeatMenu>
  <FirstDigitTimeout>5000</FirstDigitTimeout>
  <InterdigitDelay>3000</InterdigitDelay>
  <PromptVolume>50</PromptVolume>
  <ExitCallActionObjectId>2b3566bd-0339-43a4-85a1-09ab3177f0e9</ExitCallActionObjectId>
  <AddressAfterRecord>false</AddressAfterRecord>
  <DtmfAccessId>99934</DtmfAccessId>
  <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
  <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
  <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
  <IsClockMode24Hour>false</IsClockMode24Hour>
  <SynchScheduleObjectId>58dce2eb-9d6d-4621-b81d-a56c80b83897</SynchScheduleObjectId>
  <SynchScheduleURI>/vmrest/schedules/58dce2eb-9d6d-4621-b81d-a56c80b83897</SynchScheduleURI>
  <RouteNDRToSender>true</RouteNDRToSender>
  <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
  <VoiceNameRequired>false</VoiceNameRequired>
  <SendBroadcastMsg>false</SendBroadcastMsg>
  <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
  <ConversationVui>VuiStart</ConversationVui>
  <ConversationName>SubMenu</ConversationName>
  <SpeechCompleteTimeout>0</SpeechCompleteTimeout> 
  <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
  <UseVui>false</UseVui>
  <SkipPasswordForKnownDevice>true</SkipPasswordForKnownDevice>
  <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
  <UseDefaultTimeZone>true</UseDefaultTimeZone>
  <EnableMessageLocator>false</EnableMessageLocator>
  <DtmfNameFirst>573445</DtmfNameFirst>
  <DtmfNameLast>3544355</DtmfNameLast>
  <AssistantRowsPerPage>5</AssistantRowsPerPage>
  <InboxMessagesPerPage>20</InboxMessagesPerPage>
  <InboxAutoRefresh>15</InboxAutoRefresh>
  <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
  <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
  <ReadOnly>false</ReadOnly>
  <EnableTts>true</EnableTts>
  <SmtpAddress>user_operator_1@ucbu-aricent-vm463.cisco.com</SmtpAddress>
  <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
  <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
  <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
  <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
  <SpeechSensitivity>50</SpeechSensitivity>
  <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
  <ContinuousAddMode>false</ContinuousAddMode>
  <NameConfirmation>false</NameConfirmation>
  <CommandDigitTimeout>1500</CommandDigitTimeout>
  <SaveMessageOnHangup>false</SaveMessageOnHangup>
  <SendMessageOnHangup>1</SendMessageOnHangup>
  <SkipForwardTime>5000</SkipForwardTime>
  <SkipReverseTime>5000</SkipReverseTime>
  <UseShortPollForCache>true</UseShortPollForCache>
  <SearchByExtensionSearchSpaceObjectId>5d004dee-14ef-4fc4-83b8-850274628286</SearchByExtensionSearchSpaceObjectId>
  <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/5d004dee-14ef-4fc4-83b8-850274628286</SearchByExtensionSearchSpaceURI>
  <SearchByNameSearchSpaceObjectId>5d004dee-14ef-4fc4-83b8-850274628286</SearchByNameSearchSpaceObjectId>
  <SearchByNameSearchSpaceURI>/vmrest/searchspaces/5d004dee-14ef-4fc4-83b8-850274628286</SearchByNameSearchSpaceURI>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <Inactive>false</Inactive> 
  <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
  <LdapType>1</LdapType>
  <FaxServerObjectId>1564dbbc-002f-47b9-a0f3-38f2cd6e2d87</FaxServerObjectId>
  <FaxServerURI>/vmrest/faxservers/1564dbbc-002f-47b9-a0f3-38f2cd6e2d87</FaxServerURI>
  <MwisURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/9375d893-c8eb-437b-90bf-    7de4b1d0c3e8/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/privatelists</PrivateListsURI>
  <UserWebPasswordURI>/vmrest/users/7e048531-acdf-460b-884e-415be712d0bc/credential/password</UserWebPasswordURI>
  <UserVoicePinURI>/vmrest/users/7e048531-acdf-460b-884e-415be712d0bc/credential/pin</UserVoicePinURI>
  <UserRoleURI>/vmrest/users/7e048531-acdf-460b-884e-415be712d0bc/userroles</UserRoleURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%209375d893-c8eb-437b-90bf-7de4b1d0c3e8)</SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%209375d893-c8eb-437b-90bf-7de4b1d0c3e8)  </AlternateNamesURI>
</User> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users?query=(emailaddress is abc@cisco.com)
Accept: application/json
Connection: keep_alive |
|---|

| {
  "URI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1"
  "ObjectId":"6c91a90f-0771-492b-a7a5-083ea246a7e1"
  "UseDefaultLanguage":"true"
  "Alias":"Texoma"
  "DisplayName":"Texoma"
  "TimeZone":"190"
  "CreationTime":"2013-03-14T10:54:47Z"
  "IsTemplate":"false"
  "CosObjectId":"844e18ef-884c-4f43-b9ce-1dc0d53196c2"
  "CosURI":"/vmrest/coses/844e18ef-884c-4f43-b9ce-1dc0d53196c2"
  "Language":"1033"
  "LocationObjectId":"42a9ab40-490d-4819-9bfb-8ddce4f430ff"
  "LocationURI":"/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff"
  "AddressMode":"0"
  "ClockMode":"0"
  "ConversationTui":"SubMenu"
  "GreetByName":"true"
  "ListInDirectory":"true"
  "IsVmEnrolled":"true"
  "SayCopiedNames":"true"
  "SayDistributionList":"true"
  "SayMsgNumber":"true"
  "SaySender":"true"
  "SayTimestampAfter":"true"
  "SayTimestampBefore":"false"
  "SayTotalNew":"true"
  "SayTotalNewEmail":"true"
  "SayTotalNewFax":"false"
  "SayTotalNewVoice":"true"
  "SayTotalReceipts":"false"
  "SayTotalSaved":"true"
  "Speed":"100"
  "MediaSwitchObjectId":"ec1e2636-fc14-44fc-8cda-d6c1a3d61150"
  "PhoneSystemURI":"/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150"
  "Undeletable":"false"
  "UseBriefPrompts":"false"
  "Volume":"50"
  "EnAltGreetDontRingPhone":"false"
  "EnAltGreetPreventSkip":"false"
  "EnAltGreetPreventMsg":"false"
  "EncryptPrivateMessages":"false"
  "DeletedMessageSortOrder":"2"
  "SayAltGreetWarning":"false"
  "SaySenderExtension":"false"
  "SayAni":"false"
  "CallAnswerTimeout":"4"
  "CallHandlerObjectId":"fc2f99c4-31ac-465b-b143-5d21c760439c"
  "CallhandlerURI":"/vmrest/handlers/callhandlers/fc2f99c4-31ac-465b-b143-5d21c760439c"
  "MessageTypeMenu":"false"
  "NewMessageSortOrder":"1"
  "SavedMessageSortOrder":"2"
  "MessageLocatorSortOrder":"1"
  "NewMessageStackOrder":"1234567"
  "SavedMessageStackOrder":"1234567"
  "EnablePersonalRules":"true"
  "RecordUnknownCallerName":"true"
  "RingPrimaryPhoneFirst":"false"
  "ExitAction":"2"
  "ExitTargetConversation":"PHGreeting"
  "PromptSpeed":"100"
  "ExitTargetHandlerObjectId":"939d4d12-cec8-4fee-ae47-fbf0cf20c33e"
  "RepeatMenu":"1"
  "FirstDigitTimeout":"5000"
  "InterdigitDelay":"3000"
  "PromptVolume":"50"
  "ExitCallActionObjectId":"a5ab392f-dce6-4de2-af7f-92f9ebd14300"
  "AddressAfterRecord":"false"
  "DtmfAccessId":"12345"
  "ConfirmDeleteMessage":"false"
  "ConfirmDeleteDeletedMessage":"false"
  "ConfirmDeleteMultipleMessages":"true"
  "IsClockMode24Hour":"false"
  "SynchScheduleObjectId":"214cc45c-db48-44c6-a239-aa4c5e65e32a"
  "SynchScheduleURI":"/vmrest/schedules/214cc45c-db48-44c6-a239-aa4c5e65e32a"
  "RouteNDRToSender":"true"
  "IsSetForVmEnrollment":"true"
  "VoiceNameRequired":"false"
  "SendBroadcastMsg":"false"
  "UpdateBroadcastMsg":"false"
  "ConversationVui":"VuiStart"
  "ConversationName":"SubMenu"
  "SpeechCompleteTimeout":"0"
  "SpeechIncompleteTimeout":"750"
  "UseVui":"false"
  "SkipPasswordForKnownDevice":"false"
  "JumpToMessagesOnLogin":"false"
  "UseDefaultTimeZone":"true"
  "EnableMessageLocator":"false"
  "AssistantRowsPerPage":"5"
  "InboxMessagesPerPage":"20"
  "InboxAutoRefresh":"15"
  "InboxAutoResolveMessageRecipients":"true"
  "PcaAddressBookRowsPerPage":"5"
  "ReadOnly":"false"
  "EnableTts":"true"
  "SmtpAddress":"vishu11@ucbu-aricent-vm463.cisco.com"
  "ConfirmationConfidenceThreshold":"60"
  "AnnounceUpcomingMeetings":"60"
  "SpeechConfidenceThreshold":"40"
  "SpeechSpeedVsAccuracy":"50"
  "SpeechSensitivity":"50"
  "EnableVisualMessageLocator":"false"
  "ContinuousAddMode":"false"
  "NameConfirmation":"false"
  "CommandDigitTimeout":"1500"
  "SaveMessageOnHangup":"false"
  "SendMessageOnHangup":"1"
  "SkipForwardTime":"5000"
  "SkipReverseTime":"5000"
  "UseShortPollForCache":"false"
  "SearchByExtensionSearchSpaceObjectId":"877942bf-6600-4b7a-809d-159199cfc2ec"
  "SearchByExtensionSearchSpaceURI":"/vmrest/searchspaces/877942bf-6600-4b7a-809d-159199cfc2ec"
  "SearchByNameSearchSpaceObjectId":"877942bf-6600-4b7a-809d-159199cfc2ec"
  "SearchByNameSearchSpaceURI":"/vmrest/searchspaces/877942bf-6600-4b7a-809d-159199cfc2ec"
  "PartitionObjectId":"da2114bf-cde7-43d8-9709-cd3895a9d41b"
  "PartitionURI":"/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b"
  "Inactive": "false",
  "UseDynamicNameSearchWeight":"false"
  "LdapType":"0"
  "MwisURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/mwis"
  "NotificationDevicesURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/notificationdevices"
  "MessageHandlersURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/messagehandlers"
  "ExternalServiceAccountsURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/externalserviceaccounts"
  "AlternateExtensionsURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/alternateextensions"
  "PrivateListsURI":"/vmrest/users/6c91a90f-0771-492b-a7a5-083ea246a7e1/privatelists"
  "SmtpProxyAddressesURI":"/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%206c91a90f-0771-492b-a7a5-083ea246a7e1)"
  "AlternateNamesURI":"/vmrest/alternatenames?query=(GlobalUserObjectId%20is%206c91a90f-0771-492b-a7a5-083ea246a7e1)"
} |
|---|

| Response Code: 200 |
|---|

| https://<connection-server>/vmrest/usertemplates. |
|---|

| https://<connection-server>/vmrest/mailboxstores. |
|---|

| POST https://<connection-server>/vmrest/users?templateAlias=<usertemplatealias> |
|---|

| POST https://<connection-server>/vmrest/users?templateAlias=<usertemplateAlias>&MailboxStoreObjectId=<mailboxStore-ObjectId> |
|---|

| <User>
  <Alias>texoma</Alias>
  <DtmfAccessId >123422</DtmfAccessId >
</User> |
|---|

| Response Code: 201
/vmrest/users/f82b301d-1ec8-44c6-a3ee-0012269439bf |
|---|

| POST https://<Connection-server>/vmrest/users?templateAlias=voicemailusertemplate
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
  "Alias":"voicemailusertemplate1",
  "DisplayName":"Voice Mail User Template 1"
} |
|---|

| Response Code: 201
/vmrest/users/f82b301d-1ec8-44c6-a3ee-0012269439bf |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| <User> 
  <Alias>Texoma</Alias>
  <UseShortPollForCache> true</UseShortPollForCache>
  <ListInDirectory>true </ListInDirectory>
  <SkipPasswordForKnownDevice>true </SkipPasswordForKnownDevice>
  <IsVmEnrolled> true</IsVmEnrolled>
  <RouteNDRToSender >true</RouteNDRToSender >
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150 </MediaSwitchObjectId>
  <DtmfAccessId>99934</DtmfAccessId>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <Inactive>false</Inactive> 
  <CosObjectId>8ab2b94d-1531-4589-865f-27bd3eea8adc</CosObjectId>
  <SearchByExtensionSearchSpaceObjectId>877942bf-6600-4b7a-809d-159199cfc2ec</SearchByExtensionSearchSpaceObjectId>
</User> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
  "DtmfAccessId":"123”
} |
|---|

| Response Code: 204 |
|---|

|  | UseCallLanguage | UseDefaultLanguage | Language |
|---|---|---|---|
| Use System Default Language | false | true | NULL/LanguageCode |
| Inherit Language from Caller | true | true/false | NULL/LanguageCode |
| Particular Language | false | false | Language Code |

| https://<Connection-server>/vmrest/timezones |
|---|

| https://<Connection-server>/vmrest/installedlanguages |
|---|

| https://<Connection-server>/vmrest/languagemap |
|---|

| <User>
 <UseDefaultTimeZone>false</UseDefaultTimeZone>
 <TimeZone>175</TimeZone>
 <UseDefaultLanguage>false</UseDefaultLanguage>
 <Language>1034</Language>
</User> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| Field Name | Operation | Data Type | Description |
|---|---|---|---|
| Inactive | Read/Write | Boolean | A flag displays the status of a user. Possible values: true: if user is inactive. false: if user is active. Default Value: false Note You can only change the status from true to false. | Note | You can only change the status from true to false. |
| Note | You can only change the status from true to false. |
| Alias | Read/Write | String(64) | A unique text name of a user. Users enter the alias to sign in to the Cisco Personal Communications Assistant (Cisco PCA). The administrators enter the alias to sign in to Cisco Unity Connection Administration. |
| DisplayName | Read/Write | String(64) | Descriptive name of the user. |
| FirstName | Read/Write | String(64) | The first name (i.e., given name) of the user. |
| LastName | Read/Write | String(64) | The last name (i.e., surname or family name) of the user, by which a user is commonly known. |
| SmtpAddress | Read/Write | String(320) | The full SMTP address for the user |
| TimeZone | Read/Write | Integer(4) | The time zone to which this user account is associated. URI for timezone is: https://<Connection-server>/vmrest/timezones. |
| UseDefaultTimeZone | Read/Write | Boolean | Indicates if the default timezone is being used. Possible values: true: if default time zone is to be used false: to use specific time zone, if false is selected timezone should be also specified. |
| Language | Read/Write | Integer | The preferred language of this user. For a user with a voice mailbox, it is the language in which the subscriber hears instructions
                                          played to them. If the subscriber has TTS enabled by their class of service, it is the language used for TTS. |
| UseDefaultLanguage | Read/Write | Boolean | Set to true, if the call handler is using default language from the location it belongs to. If false, you need to specify
                                          the language, so set the particular language |
| LdapType | Read/Write | Integer | The LDAP configuration information for the user. Possible Value: 0-Do not Integrate with LDAP directory. 1-Integrate with LDAP directory 2-Authenticate 4-Inactive Default Value: 0 |
| LocationObjectId | Read Only | String(36) | The unique identifier of the LocationVMS object to which the user belongs to. |
| IsTemplate | Read Only | Boolean | A flag indicating whether this instance of a user object is a "template" for creating new users. Possible values: true: if user template false: if user Default Value: false |
| Initials | Read/Write | String(64) | The initial letters of some or all of the names of the user. |
| Title | Read/Write | String(64) | The position or function of a user within an organization, such as 'Vice President'. |
| EmployeeId | Read/Write | String(64) | The numeric or alphanumeric identifier assigned to a person, typically based on order of hire or association with an organization. |
| Address | Read/Write | String(128) | The physical address such as a house number and street name where the user is located, or with which a user is associated. |
| Building | Read/Write | String(64) | The name of the building where the user is based. |
| City | Read/Write | String(64) | The name of a locality, such as a city, county or other geographic region where the user is located, or with which a user
                                          is associated. |
| State | Read/Write | String(64) | The full name of the state or province where this user is located, or with which a user is associated. |
| PostalCode | Read/Write | String(40) | For users in the United States, the zip code where the user is located. For users in Canada, Mexico, and other countries,
                                          the postal code where the user is located. |
| Country | Read/Write | String(2) | The two-letter ISO 3166-1 country code where the user is located, or with which a user is associated. URI to fetch available
                                          country code: https://<Connection-server>/vmrest/languagemap. From the response fetch last 2 letter of the Languagetag parameter. |
| Department | Read/Write | String(64) | The name or number for the department or subdivision of an organization to which a person belongs to. |
| Manager | Read/Write | String(64) | The name of the person who is the manager or supervisor of the user. Any character except non-printing ASCII characters can
                                          be used here. |
| BillingId | Read/Write | String(32) | Accounting information or project code associated with the user. Any ASCII or Unicode character can be used here. |
| EmailAddress | Read/Write | String(320) | The corporate email address of the user. |
| DtmfAccessId | Read/Write | String(40) | The DTMF access id (i.e., extension) of the subscriber. |
| XferString | Read/Write | String(40) | The cross-server transfer extension. If NULL, the user's primary extension is used. |
| FaxServerObjectId | Read/Write | String(36) | The unique identifier of the FaxServer object for the subscriber. |
| PartitionObjectId | Read/Write | String(36) | The unique identifier of the partition associated with the user |
| MediaSwitchObjectId | Read/Write | String(36) | The unique identifier of the MediaSwitch object associated with the user |
| SearchByExtensionSearchSpaceObjectId | Read/Write | String(36) | The unique identifier of the SearchSpace which is used to limit the visibility to dialable/addressable objects when searching
                                          by extension (dial string). |
| SearchByNameSearchSpaceObjectId | Read/Write | String(36) | The unique identifier of the SearchSpace which is used to limit the visibility to dialable/addressable objects when searching
                                          by name (character string). |
| CosObjectId | Read/Write | String(36) | The unique identifier of the class of service object to which this user account is associated. |
| CallHandlerObjectId | Read/Write | String(36) | The unique identifier of the primary CallHandler object for the subscriber. |
| ScheduleSetObjectId | Read/Write | String(36) | The unique identifier of the schedule set Cisco Unity Connection will use for making standard versus off hours decisions within
                                          this call handler. Note To update the ScheduleSetObjectId ,first go to the user URI, then go to the callhandler URI, and then update the scheduleset. | Note | To update the ScheduleSetObjectId ,first go to the user URI, then go to the callhandler URI, and then update the scheduleset. |
| Note | To update the ScheduleSetObjectId ,first go to the user URI, then go to the callhandler URI, and then update the scheduleset. |
| TenantObjectId | Read Only | String(36) | The unique identifier of the tenant to which the user belongs. This field is reflected in the response only if the user belongs
                                          to a particular tenant. |
| IsVmEnrolled | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection plays the enrollment conversation (record a voice name, indicate if they
                                          are listed in the directory, etc.) for the subscriber when they login. Possible values: false: The enrollment conversation is not played for the subscriber when they login. true: The enrollment conversation is played for the subscriber when they login. Default value: true |
| SkipPasswordForKnownDevice | Read/Write | Boolean | A flag indicating whether the subscriber will be asked for his/her PIN when attempting to sign-in from a known device. Possible values: false: Do not Skip PIN When Calling From a Known Extension true: Skip PIN When Calling From a Known Extension Default value: false |
| ListInDirectory | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection should list the subscriber in the phone directory for outside callers. Possible values: false: Do not list in Directory true: List in directory Default value: false |
| UseShortPollForCache | Read/Write | Boolean | A flag indicating whether the user's polling cycle for retrieving the calendar information will be the shorter "power user"
                                          polling cycle. Possible values: false: The subscriber's polling cycle is determined by the system default polling cycle. (System configuration setting "Normal
                                                   Calendar Caching Poll Interval"). true: The shorter "power user" polling cycle is used. (System configuration setting "Short Calendar Caching Poll Interval"). Default value : false |
| RouteNDRToSender | Read/Write | Boolean | Flag indicating whether to Send Non-Delivery Receipts on Failed Message Delivery. Possible values: true: Send Non-Delivery Receipts on Failed Message Delivery. false: Do not Send Non-Delivery Receipts on Failed Message Delivery. Default value: true |
| Undeletable | Read Only | Boolean | Flag indicating whether a user cannot be deleted or not. Possible values: true: For default users false: For other created users |
| VoiceName | Read/Write | String(40) | The name of the WAV file containing the recorded audio (voice name, greeting, etc.) for the parent object. |
| DialablePhoneNumber | Read/Write | String(255) | The phone number of the fax machine that the user sends faxes to for printing. |
| PhoneNumber | Read Only | String(255) | The corporate Phone number. |
| CreateSmtpProxyFromCorp | Read/Write | Boolean | Flag indicating whether an SMTP proxy address matching the corporate e-mail address (column EmailAddress) should be created
                                          for the user. Possible values: false: Do not create matching SMTP proxy address. true: Create matching SMTP proxy address. Default value: false MailboxStoreName Read Only String Mailbox store name used by the user |

| Note | You can only change the status from true to false. |
|---|---|

| Note | To update the ScheduleSetObjectId ,first go to the user URI, then go to the callhandler URI, and then update the scheduleset. |
|---|---|

| GET https://<connection-server>/vmrest/adminusers |
|---|

| <Users total="4">
   <User>
      <URI>/vmrest/adminusers/c8a3a38b-df1a-4612-9679-d1fddc790e95</URI>
      <ObjectId>c8a3a38b-df1a-4612-9679-d1fddc790e95</ObjectId>
      <UseDefaultLanguage>true</UseDefaultLanguage>
      <Alias>admin</Alias>
      <DisplayName>admin</DisplayName>
      <TimeZone>190</TimeZone>
      <CreationTime>2020-07-28T10:13:15Z</CreationTime>
      <IsTemplate>false</IsTemplate>
      <Language>1033</Language>
      <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
      <Undeletable>true</Undeletable>
      <UseDefaultTimeZone>true</UseDefaultTimeZone>
      <ReadOnly>true</ReadOnly>
      <SmtpAddress>admin@ucbu-aricent-vm405.cisco.com</SmtpAddress>
      <LdapType>0</LdapType>
      <UserWebPasswordURI>/vmrest/users/c8a3a38b-df1a-4612-9679-d1fddc790e95/credential/password</UserWebPasswordURI>
      <UserRoleURI>/vmrest/users/c8a3a38b-df1a-4612-9679-d1fddc790e95/userroles</UserRoleURI>
   </User>
   <User>
      <URI>/vmrest/adminusers/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2</URI>
      <ObjectId>0b008d28-a8ce-4d14-aa6f-3b584d3d43d2</ObjectId>
      <UseDefaultLanguage>true</UseDefaultLanguage>
      <FirstName>Cisco Unity Connection</FirstName>
      <LastName>Messaging System</LastName>
      <Alias>UnityConnection</Alias>
      <DisplayName>Cisco Unity Connection Messaging System</DisplayName>
      <TimeZone>190</TimeZone>
      <CreationTime>2020-07-28T10:13:15Z</CreationTime>
      <IsTemplate>false</IsTemplate>
      <Language>1033</Language>
      <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
      <Undeletable>true</Undeletable>
      <UseDefaultTimeZone>true</UseDefaultTimeZone>
      <ReadOnly>true</ReadOnly>
      <SmtpAddress>unityconnection@ucbu-aricent-vm405.cisco.com</SmtpAddress>
      <LdapType>0</LdapType>
      <UserWebPasswordURI>/vmrest/users/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2/credential/password</UserWebPasswordURI>
      <UserRoleURI>/vmrest/users/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2/userroles</UserRoleURI>
   </User>
   <User>
      <URI>/vmrest/adminusers/6fd02048-a02c-4bb8-a440-c6c063cb3dcd</URI>
      <ObjectId>6fd02048-a02c-4bb8-a440-c6c063cb3dcd</ObjectId>
      <UseDefaultLanguage>true</UseDefaultLanguage>
      <FirstName>Replication</FirstName>
      <LastName>Agent</LastName>
      <Alias>Replication</Alias>
      <DisplayName>Replication Agent (ucbu-aricent-vm405)</DisplayName>
      <TimeZone>190</TimeZone>
      <CreationTime>2020-07-28T10:13:18Z</CreationTime>
      <IsTemplate>false</IsTemplate>
      <Language>1033</Language>
      <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
      <Undeletable>true</Undeletable>
      <UseDefaultTimeZone>true</UseDefaultTimeZone>
      <ReadOnly>true</ReadOnly>
      <SmtpAddress>replication@ucbu-aricent-vm405.cisco.com</SmtpAddress>
      <LdapType>0</LdapType>
      <UserWebPasswordURI>/vmrest/users/6fd02048-a02c-4bb8-a440-c6c063cb3dcd/credential/password</UserWebPasswordURI>
      <UserRoleURI>/vmrest/users/6fd02048-a02c-4bb8-a440-c6c063cb3dcd/userroles</UserRoleURI>
   </User>
   <User>
      <URI>/vmrest/adminusers/0347d21e-c238-4079-8d77-662499c058ba</URI>
      <ObjectId>0347d21e-c238-4079-8d77-662499c058ba</ObjectId>
      <UseDefaultLanguage>true</UseDefaultLanguage>
      <FirstName>George</FirstName>
      <Initials>GD</Initials>
      <LastName>Davis</LastName>
      <Alias>Davis</Alias>
      <State>Mumbai</State>
      <Title>Trainee</Title>
      <Address>HNo4 Street Ville Parle</Address>
      <DisplayName>George</DisplayName>
      <TimeZone>190</TimeZone>
      <CreationTime>2020-07-29T09:03:42Z</CreationTime>
      <IsTemplate>false</IsTemplate>
      <Language>1033</Language>
      <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
      <Undeletable>false</Undeletable>
      <UseDefaultTimeZone>true</UseDefaultTimeZone>
      <ReadOnly>false</ReadOnly>
      <SmtpAddress>davis@ucbu-aricent-vm405.cisco.com</SmtpAddress>
      <LdapType>3</LdapType>
      <UserWebPasswordURI>/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/credential/password</UserWebPasswordURI>
      <UserRoleURI>/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/userroles</UserRoleURI>
   </User>
</Users> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/adminusers
Accept: application/json
Connection: keep_alive |
|---|

| {
   "@total": "4",
   "User":    [
            {
         "URI": "/vmrest/adminusers/c8a3a38b-df1a-4612-9679-d1fddc790e95",
         "ObjectId": "c8a3a38b-df1a-4612-9679-d1fddc790e95",
         "UseDefaultLanguage": "true",
         "Alias": "admin",
         "DisplayName": "admin",
         "TimeZone": "190",
         "CreationTime": "2020-07-28T10:13:15Z",
         "IsTemplate": "false",
         "Language": "1033",
         "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
         "Undeletable": "true",
         "UseDefaultTimeZone": "true",
         "ReadOnly": "true",
         "SmtpAddress": "admin@ucbu-aricent-vm405.cisco.com",
         "LdapType": "0",
         "UserWebPasswordURI": "/vmrest/users/c8a3a38b-df1a-4612-9679-d1fddc790e95/credential/password",
         "UserRoleURI": "/vmrest/users/c8a3a38b-df1a-4612-9679-d1fddc790e95/userroles"
      },
            {
         "URI": "/vmrest/adminusers/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2",
         "ObjectId": "0b008d28-a8ce-4d14-aa6f-3b584d3d43d2",
         "UseDefaultLanguage": "true",
         "FirstName": "Cisco Unity Connection",
         "LastName": "Messaging System",
         "Alias": "UnityConnection",
         "DisplayName": "Cisco Unity Connection Messaging System",
         "TimeZone": "190",
         "CreationTime": "2020-07-28T10:13:15Z",
         "IsTemplate": "false",
         "Language": "1033",
         "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
         "Undeletable": "true",
         "UseDefaultTimeZone": "true",
         "ReadOnly": "true",
         "SmtpAddress": "unityconnection@ucbu-aricent-vm405.cisco.com",
         "LdapType": "0",
         "UserWebPasswordURI": "/vmrest/users/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2/credential/password",
         "UserRoleURI": "/vmrest/users/0b008d28-a8ce-4d14-aa6f-3b584d3d43d2/userroles"
      },
            {
         "URI": "/vmrest/adminusers/6fd02048-a02c-4bb8-a440-c6c063cb3dcd",
         "ObjectId": "6fd02048-a02c-4bb8-a440-c6c063cb3dcd",
         "UseDefaultLanguage": "true",
         "FirstName": "Replication",
         "LastName": "Agent",
         "Alias": "Replication",
         "DisplayName": "Replication Agent (ucbu-aricent-vm405)",
         "TimeZone": "190",
         "CreationTime": "2020-07-28T10:13:18Z",
         "IsTemplate": "false",
         "Language": "1033",
         "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
         "Undeletable": "true",
         "UseDefaultTimeZone": "true",
         "ReadOnly": "true",
         "SmtpAddress": "replication@ucbu-aricent-vm405.cisco.com",
         "LdapType": "0",
         "UserWebPasswordURI": "/vmrest/users/6fd02048-a02c-4bb8-a440-c6c063cb3dcd/credential/password",
         "UserRoleURI": "/vmrest/users/6fd02048-a02c-4bb8-a440-c6c063cb3dcd/userroles"
      },
            {
         "URI": "/vmrest/adminusers/0347d21e-c238-4079-8d77-662499c058ba",
         "ObjectId": "0347d21e-c238-4079-8d77-662499c058ba",
         "UseDefaultLanguage": "true",
         "FirstName": "George",
         "Initials": "GD",
         "LastName": "Davis",
         "Alias": "Davis",
         "State": "Mumbai",
         "Title": "Trainee",
         "Address": "HNo4 Street Ville Parle",
         "DisplayName": "George",
         "TimeZone": "190",
         "CreationTime": "2020-07-29T09:03:42Z",
         "IsTemplate": "false",
         "Language": "1033",
         "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
         "Undeletable": "false",
         "UseDefaultTimeZone": "true",
         "ReadOnly": "false",
         "SmtpAddress": "davis@ucbu-aricent-vm405.cisco.com",
         "LdapType": "3",
         "UserWebPasswordURI": "/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/credential/password",
         "UserRoleURI": "/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/userroles"
      }
   ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/adminusers/<user-objectId> |
|---|

| <User>
   <URI>/vmrest/adminusers/0347d21e-c238-4079-8d77-662499c058ba</URI>
   <ObjectId>0347d21e-c238-4079-8d77-662499c058ba</ObjectId>
   <UseDefaultLanguage>true</UseDefaultLanguage>
   <FirstName>George</FirstName>
   <Initials>GD</Initials>
   <LastName>Davis</LastName>
   <Alias>Davis</Alias>
   <State>Mumbai</State>
   <Title>Trainee</Title>
   <Address>HNo4 Street Ville Parle</Address>
   <DisplayName>George</DisplayName>
   <TimeZone>190</TimeZone>
   <CreationTime>2020-07-29T09:03:42Z</CreationTime>
   <IsTemplate>false</IsTemplate>
   <Language>1033</Language>
   <LocationObjectId>58b236f7-3c20-4e61-89a0-809740c05de5</LocationObjectId>
   <Undeletable>false</Undeletable>
   <UseDefaultTimeZone>true</UseDefaultTimeZone>
   <ReadOnly>false</ReadOnly>
   <SmtpAddress>davis@ucbu-aricent-vm405.cisco.com</SmtpAddress>
   <LdapType>3</LdapType>
   <UserWebPasswordURI>/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/credential/password</UserWebPasswordURI>
   <UserRoleURI>/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/userroles</UserRoleURI>
</User> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/adminusers/{user-objectId}
Accept: application/json
Connection: keep_alive |
|---|

| {
   "URI": "/vmrest/adminusers/0347d21e-c238-4079-8d77-662499c058ba",
   "ObjectId": "0347d21e-c238-4079-8d77-662499c058ba",
   "UseDefaultLanguage": "true",
   "FirstName": "George",
   "Initials": "GD",
   "LastName": "Davis",
   "Alias": "Davis",
   "State": "Mumbai",
   "Title": "Trainee",
   "Address": "HNo4 Street Ville Parle",
   "DisplayName": "George",
   "TimeZone": "190",
   "CreationTime": "2020-07-29T09:03:42Z",
   "IsTemplate": "false",
   "Language": "1033",
   "LocationObjectId": "58b236f7-3c20-4e61-89a0-809740c05de5",
   "Undeletable": "false",
   "UseDefaultTimeZone": "true",
   "ReadOnly": "false",
   "SmtpAddress": "davis@ucbu-aricent-vm405.cisco.com",
   "LdapType": "3",
   "UserWebPasswordURI": "/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/credential/password",
   "UserRoleURI": "/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba/userroles"
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/adminusers?templateAlias=<administratortemplate> |
|---|

| <user>
<Alias>Davis</Alias>
<DisplayName>George</DisplayName>
<FirstName>George</FirstName>
<LastName>Davis</LastName>
<TimeZone>190</TimeZone>
<UseDefaultTimeZone>true</UseDefaultTimeZone>
<IsTemplate>false</IsTemplate>
<Language>1033</Language>
<UseDefaultLanguage>true</UseDefaultLanguage>
<LdapType>3</LdapType>
<Initials>GD</Initials>
<Title>Trainee</Title>
<Address>HNo4 Street Ville Parle</Address>
<State>Mumbai</State>
<Undeletable>false</Undeletable>
</user> |
|---|

| Response Code: 201
/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba |
|---|

| POST https://<Connection-server>/vmrest/adminusers?templateAlias=administratortemplate
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
  "UseDefaultLanguage" : "true"
  "Alias":"Davis",
  "DisplayName":"George"
  "FirstName" : "George"
  "LastName" : "Davis"
  "TimeZone":"190"
  "UseDefaultTimeZone" : "true"
  "IsTemplate" : "false"
  "Language" : "1033"
  "LdapType" : "3"
  "Initials" : "GD"
  "Title" : "Trainee"
  "Address" : "HNo4 Street Ville Parle"
  "State" : "Mumbai"
  "Undeletable" : "false"
} |
|---|

| Response Code: 201
/vmrest/users/0347d21e-c238-4079-8d77-662499c058ba |
|---|

| PUT https://<connection-server>/vmrest/adminusers/<user-objectid> |
|---|

| <user>
<Alias>Texoma</Alias>
<DisplayName>richardtexoma</DisplayName>
<IsTemplate>false</IsTemplate>
<Language>1020</Language>
<LocationObjectId>35ac99ba-e098-4195-9ffb-cecb5a7cab65</LocationObjectId>
<Undeletable>true</Undeletable>
<UseDefaultTimeZone>true</UseDefaultTimeZone>
<ReadOnly>true</ReadOnly>
<TimeZone>140</TimeZone>
</user> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/adminusers/<user-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
  "TimeZone":"170”
} |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/adminusers/<user-objectid> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/adminusers/<user-objectid>
Accept: application/json
Content-type: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| Field Name | Operation | Data Type | Description |
|---|---|---|---|
| Alias | Read/Write | String(64) | A unique text name of a user. |
| Inactive | Read/Write | Boolean | A flag displays the status of a user. Possible values: true: if user is inactive. false: if user is active. Default Value: false Note You can only change the status from true to false. | Note | You can only change the status from true to false. |
| Note | You can only change the status from true to false. |
| DisplayName | Read/Write | String(64) | Descriptive name of the user. |
| FirstName | Read/Write | String(64) | The first name (i.e., given name) of the user. |
| LastName | Read/Write | String(64) | The last name (i.e., surname or family name) of the user, by which a user is commonly known. |
| SmtpAddress | Read/Write | String(320) | The full SMTP address for the user |
| TimeZone | Read/Write | Integer(4) | The time zone to which this user account is associated. URI for timezone is: https://<Connection-server>/vmrest/timezones. |
| UseDefaultTimeZone | Read/Write | Boolean | Indicates if the default timezone is being used. Possible values: true: if default time zone is to be used false: to use specific time zone, if false is selected timezone should be also specified. |
| Language | Read/Write | Integer | The preferred language of  user. |
| UseDefaultLanguage | Read/Write | Boolean | Set to true, if the call handler is using default language from the location it belongs to. If false, you need to specify
                                          the language, so set the particular language |
| LdapType | Read/Write | Integer | The LDAP configuration information for the user. Possible Values: 0-Not integrated with LDAP directory. 3-Integrated with LDAP directory Default Value: 0 |
| LocationObjectId | Read Only | String(36) | The unique identifier of the LocationVMS object to which the user belongs to. |
| IsTemplate | Read Only | Boolean | A flag indicating whether this instance of a user object is a "template" for creating new users. Possible values: true: if user template false: if user Default Value: false |
| Initials | Read/Write | String(64) | The initial letters of some or all of the names of the user. |
| Title | Read/Write | String(64) | The position or function of a user within an organization, such as 'Vice President'. |
| Address | Read/Write | String(128) | The physical address such as a house number and street name where the user is located, or with which a user is associated. |
| Building | Read/Write | String(64) | The name of the building where the user is based. |
| City | Read/Write | String(64) | The name of a locality, such as a city, county or other geographic region where the user is located, or with which a user
                                          is associated. |
| State | Read/Write | String(64) | The full name of the state or province where this user is located, or with which a user is associated. |
| PostalCode | Read/Write | String(40) | For users in the United States, the zip code where the user is located. For users in Canada, Mexico, and other countries,
                                          the postal code where the user is located. |
| Country | Read/Write | String(2) | The two-letter ISO 3166-1 country code where the user is located, or with which a user is associated. URI to fetch available
                                          country code: https://<Connection-server>/vmrest/languagemap. From the response fetch last 2 letter of the Languagetag parameter. |
| Department | Read/Write | String(64) | The name or number for the department or subdivision of an organization to which a person belongs to. |
| Manager | Read/Write | String(64) | The name of the person who is the manager or supervisor of the user. Any character except non-printing ASCII characters can
                                          be used here. |
| BillingId | Read/Write | String(32) | Accounting information or project code associated with the user. Any ASCII or Unicode character can be used here. |
| EmailAddress | Read/Write | String(320) | The corporate email address of the user. |
| Undeletable | Read Only | Boolean | Flag indicating whether a user cannot be deleted or not. Possible values: true: For default users false: For other created users |

| Note | You can only change the status from true to false. |
|---|---|