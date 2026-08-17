---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-unified-messaging-html-66a044be57
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-unified-messaging.html
retrieved_at: 2026-08-17T03:49:57.614068+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for Unified Messaging

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for Unified Messaging

# Cisco Unity Connection Provisioning Interface (CUPI) API for Unified Messaging

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Unified Messaging
                        	 Account

### Create a Unified
                           	 Messaging Account

To add a new unified messaging
                                 		  account to user, server must have Unified Messaging Services Configured. The
                                 		  following URI can be used to view the user object ID:

```
GET https://<connection-server>/vmrest/users/<user-objectid
```

From the above URI, get the unified messaging account:

```
GET https://<connection-server>/vmrest/users/<user-objectid>/externalserviceaccounts
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<ExternalServiceAccount>
     <URI>/vmrest/users/9375d893-c8eb-437b-90bf-
   7de4b1d0c3e8/externalserviceaccounts/39871e30-849a-4dcf-b868-2faf360d503a</URI>
     <ObjectId>39871e30-849a-4dcf-b868-2faf360d503a</ObjectId>
     <ExternalServiceObjectId>1cd78b6c-1e6e-4542-a6e7-14f431d6569c</ExternalServiceObjectId>
     <SubscriberObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</SubscriberObjectId>
     <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
     <EnableCalendarCapability>true</EnableCalendarCapability>
     <EnableMeetingCapability>false</EnableMeetingCapability>
     <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
     <IsPrimaryMeetingService>false</IsPrimaryMeetingService>
     <LoginType>0</LoginType>
     <UserPassword/>
     <EmailAddress>chhavi@com</EmailAddress>
     <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
     <EmailAddressUseCorp>false</EmailAddressUseCorp>
</ExternalServiceAccount>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/users/<user-objectid>/externalserviceaccounts/<objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 200
```

### Updating the
                           	 Unified Messaging Account

JSON Example

To view the unified messaging account, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/users/<userobjectid>/
externalserviceaccounts/<externalserviceaccountsobjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
{
     "EmailAddressUseCorp":"true"
     "EnableCalendarCapability":"true"
     "EnableMailboxSynchCapability":"true"
       "EnablTtsOfEmailCapability":"true"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

Default value: False

Default value: False

Default value: False

Default value: False

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Unified Messaging
                        	 Account

### Unified Messaging
                           	 Account API

The following URI can be used to
                                 		  view the user template object ID:

```
GET https://<connection-server>/vmrestvmrest/usertemplates/<usertemplateobjectid>
```

From the above URI, get the unified messaging account:

```
GET https://<connection-
    server>/vmrestvmrest/usertemplates/<usertemplateobjectid>/templateexternalserviceacco
    unts
```

#### Updating the
                              	 Unified Messaging Account

```
Request Body: 
<TemplateExternalServiceAccount>
    <EmailAddressUseCorp>true</EmailAddressUseCorp>
    <EnableCalendarCapability>true</EnableCalendarCapability>
    <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
    <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
</TemplateExternalServiceAccount>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To view the unified messaging account, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/templateexternalserviceaccounts/<templateexternalserviceaccountsobjectId 
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "EmailAddressUseCorp":"true"
    "EnableCalendarCapability":"true"
    "EnableMailboxSynchCapability":"true"
     "EnablTtsOfEmailCapability":"true"
}
```

```
Response Code: 200
```

#### Explanation of
                              	 Data Fields

Default value: False

Default value: False

Default value: False

Default value: False

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template External
                        	 Services

### About External
                           	 Services

This page contains information on how to use the API to create, list,
                              		modify, and delete Unified Messaging Services (also known as external
                              		services). When you create Unified Messaging Service Accounts, you base each
                              		account on a Unified Messaging Service. Creating a new Unified Messaging
                              		service is based on any one of the following:

- Exchange/BPOS-D

- MeetingPlace

- Office 365

Google Workspace (applicable with Unity Connection 14 and later)

Unity Connection 14 and later provides a new way to users for accessing the voice messages on their Gmail account. For this,
                              you need to configure unified messaging with Google Worspace to synchronize the voice messages between Unity Connection and
                              Gmail server.

### Listing External
                           	 Services

Example 1

The following is an example of the GET request that lists the Unified
                                 		  Messaging Services:

```
https://<connection_server>/vmrest/externalservices
```

The following is an example of the response from the above *GET*
                                 		  request and the actual response will depend upon the information given by you:

```
<ExternalServices total="3">
  <ExternalService>
    <URI>/vmrest/externalservices/53a7675f-94c2-4596-ae3a-69b9287d119d</URI>
    <ObjectId>53a7675f-94c2-4596-ae3a-69b9287d119d</ObjectId>
    <AuthenticationMode>3</AuthenticationMode>
    <DisplayName>exchange_1</DisplayName>
    <IsEnabled>true</IsEnabled>
    <SecurityTransportType>1</SecurityTransportType>
    <Server>10.78.171.187</Server>
    <ServiceAlias>admin</ServiceAlias>
    <ServicePassword/>
    <ServerType>4</ServerType>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <SupportsTtsOfEmailCapability>true</SupportsTtsOfEmailCapability>
    <ValidateServerCertificate>false</ValidateServerCertificate>
    <UseServiceCredentials>true</UseServiceCredentials>
    <SupportsMailboxSynchCapability>true</SupportsMailboxSynchCapability>
    <ExchDoAutodiscover>false</ExchDoAutodiscover>
    <MailboxSynchFaxAction>1</MailboxSynchFaxAction>
    <MailboxSynchEmailAction>2</MailboxSynchEmailAction>
    <ExternalServiceResetURI>/vmrest/externalservices/53a7675f-94c2-4596-ae3a-69b9287d119d/reset</ExternalServiceResetURI>
  </ExternalService>
  <ExternalService>
    <URI>/vmrest/externalservices/bc1dbc08-bfdb-46e8-acb4-12cb511ebb01</URI>
    <ObjectId>bc1dbc08-bfdb-46e8-acb4-12cb511ebb01</ObjectId>
    <AuthenticationMode>1</AuthenticationMode>
    <DisplayName>ofc_365</DisplayName>
    <IsEnabled>true</IsEnabled>
    <ServiceAlias>admin</ServiceAlias>
    <ServicePassword/>
    <ServerType>5</ServerType>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <SupportsTtsOfEmailCapability>true</SupportsTtsOfEmailCapability>
    <ValidateServerCertificate>false</ValidateServerCertificate>
    <UseServiceCredentials>true</UseServiceCredentials>
    <SupportsMailboxSynchCapability>true</SupportsMailboxSynchCapability>
    <ExchDoAutodiscover>true</ExchDoAutodiscover>
    <ExchOrgDomain>10.78.171.70</ExchOrgDomain>
    <ExchSite/>
    <MailboxSynchFaxAction>1</MailboxSynchFaxAction>
    <MailboxSynchEmailAction>2</MailboxSynchEmailAction>
    <ProxyServer/>
    <ExternalServiceResetURI>/vmrest/externalservices/bc1dbc08-bfdb-46e8-acb4-12cb511ebb01/reset</ExternalServiceResetURI>
  </ExternalService>
  <ExternalService>
    <URI>/vmrest/externalservices/9d7f6b48-19fc-446a-8afe-6d454a0b3de1</URI>
    <ObjectId>9d7f6b48-19fc-446a-8afe-6d454a0b3de1</ObjectId>
    <DisplayName>meeting_place</DisplayName>
    <IsEnabled>true</IsEnabled>
    <Server>10.78.171.87</Server>
    <ServiceAlias>admin</ServiceAlias>
    <ServicePassword/>
    <ServerType>1</ServerType>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <SupportsMeetingCapability>true</SupportsMeetingCapability>
    <TransferExtensionDialString>12112</TransferExtensionDialString>
  </ExternalService>
</ExternalServices>
```

Example 2

The following is an example of another GET request that lists the
                                 		  Unified Messaging Service based on <externalservice-id>:

```
https://<connection_server>/vmrest/externalservices/<objectId>
```

The following is an example of the response from the above *GET*
                                 		  request and the actual response will depend upon the information given by you:

```
<ExternalService>
 <URI>/vmrest/externalservices/6f4f7023-e9e5-4cd0-bf55-e20a0be6fd78</URI>
 <ObjectId>6f4f7023-e9e5-4cd0-bf55-e20a0be6fd78</ObjectId>
 <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
 <AuthenticationMode>1</AuthenticationMode>
 <DisplayName>UMS_API</DisplayName>
 <IsEnabled>true</IsEnabled>
 <SecurityTransportType>1</SecurityTransportType>
 <Server>10.65.156.190</Server>
 <ServiceAlias>clientteam\administrator</ServiceAlias>
 <ServicePassword/>
 <ServerType>4</ServerType>
 <SupportsCalendarCapability>true</SupportsCalendarCapability>
 <SupportsTtsOfEmailCapability>true</SupportsTtsOfEmailCapability>
 <ValidateServerCertificate>false</ValidateServerCertificate>
 <UseServiceCredentials>true</UseServiceCredentials>
 <SupportsMailboxSynchCapability>true</SupportsMailboxSynchCapability>
 <ExchDoAutodiscover>false</ExchDoAutodiscover>
 <MailboxSynchFaxAction>1</MailboxSynchFaxAction>
 <MailboxSynchEmailAction>2</MailboxSynchEmailAction>
</ExternalService>
```

```
Response Code: 200
```

#### Listing Specific
                              	 Tenant Related User Template External Services by System Administrator

In Cisco Unity Connection 10.5(2)
                                    		  and later, the system administrator can use TenantObjectID to list the specific
                                    		  tenant related user template external services using the following URI:

```
GET https://<connection-server>/vmrest/externalservices?query=(TenantObjectId is <Tenant-ObjectId>)
```

To get the TenantObjectID, use the following URI:

```
GET https://<connection-server>/vmrest/tenants
```

### Adding Unified
                           	 Messaging Service

This section contains information on how to create External Services:

- Adding Exchange/BPOS-D
                                       			 External Service

- Adding Meeting Place
                                       			 External Service

- Adding Office 365 External
                                       			 Service

#### Adding
                              	 Exchange/BPOS-D External Service

The following is an example of
                                    		  the POST request that adds the Exchange/BPOS-D Unified Messaging Service:

```
https://<connection_server>/vmrest/externalservices
```

The request parameters will depend upon the information given by you.

```
<ExternalService>
 <DisplayName>UMS_API</DisplayName>
 <ServiceAlias> client-team\administrator</ServiceAlias>
 <ServicePassword>Ecsbulab12</ServicePassword>
 <ServerType>4</ServerType> 
 <Server>10.65.156.190</Server>
 <AuthenticationMode>1</AuthenticationMode>
 <SecurityTransportType>1</SecurityTransportType>
</ExternalService>
```

```
Response Code: 201
```

The following are the list of mandatory parameters required to create
                                    		  a Unified Messaging Service:

- Display Name: The display
                                          			 name of the unified messaging service

- Service Alias: The alias
                                          			 of the unified messaging service

- Service Password: The
                                          			 password of the unified messaging service

- Server Type: The type of
                                          			 unified messaging service account (Exchange/BPOS-D: 4)

- Server: The IP address of
                                          			 the Exchange server

- Authentication Mode: The
                                          			 web-based Authentication Mode of the Unified Messaging Service: Basic (1),
                                          			 Digest (2), and NTLM (3)

- Exchange Server Type: The
                                          			 Exchange Server Type of the Unified Messaging Account: Exchange 2003 (0) and
                                          			 Exchange 2007/2010/2013 (1)

- Security Transport Type:
                                          			 The web-based protocol of the Unified Messaging Account: HTTP (0) and HTTPS (1)

#### Adding Meeting
                              	 Place External Service

The following is an example of
                                    		  the POST request that adds the Meeting Place Unified Messaging Service:

```
https://<connection_server>/vmrest/externalservices
```

The request parameters will depend upon the information given by you.

```
<ExternalService>
 <DisplayName>MeetingPlace</DisplayName>
 <ServiceAlias> admin</ServiceAlias>
 <ServicePassword>ecsbulab</ServicePassword>
 <ServerType>1</ServerType>
 <Server>10.76.175.167</Server>
 <TransferExtensionDialString>111111</TransferExtensionDialString>
</ExternalService>
```

```
Response Code: 201
```

#### Adding Office 365
                              	 External Service

Unity Connection 12.5(1) SU2 and later supports OAuth2 web authentication mode for configuring Unified Messaging with Office 365 service. For using OAuth2 web authentication mode
                                    for configuring Unified Messaging, you must create and register an application on Microsoft Azure portal corresponding to
                                    the Unified Messaging Service. After registering the application, you will get the values of Application (Client) ID , Directory ID and Client Secret on Azure portal.

With Unity Connection 11.5(1) SU9 and later, two new fields, AdAuthenticationEndpoint and ResourceURI are introduced in this API. These fields are auto populated with default values which can be modified according to required
                                    Active Directory.

For more information on configuring Unified Messaging with OAuth2 authentication mode, see Task List for Configuring Unified Messaging section of "Configuring Unified Messaging" chapter in Unified Messaging Guide for Cisco Unity Connection Release 12.x guide available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/unified_messaging/b_12xcucumgx.html.

The following is an example of
                                    		  the POST request that adds the Office 365 Unified Messaging Service:

```
https://<connection_server>/vmrest/externalservices
```

The request parameters will depend upon the information given by you.

```
<ExternalService>
    <DisplayName>OFC_Service</DisplayName>
    <IsEnabled>true</IsEnabled>
    <ExchDoAutodiscover>true</ExchDoAutodiscover>
    <ExchOrgDomain>domain.com</ExchOrgDomain>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <ServiceAlias>admin</ServiceAlias>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <SupportsTtsOfEmailCapability>true</SupportsTtsOfEmailCapability>
    <SupportsMeetingCapability>false</SupportsMeetingCapability>
    <ValidateServerCertificate>false</ValidateServerCertificate>
    <UseServiceCredentials>true</UseServiceCredentials>
    <AuthenticationMode>4</AuthenticationMode>
    <ServicePassword>password123</ServicePassword>
    <ServerType>5</ServerType>
    <ClientId>d64ea56b-1d60-47c7-a26d-7bcbee3a09c3</ClientId>
    <ClientSecret> </ClientSecret>
    <DirectoryID>cafae64a-ffb2-4585-8c11-2d86aa8b3bf5</DirectoryID>
    <AdAuthenticationEndpoint>https://login.microsoftonline.com</AdAuthenticationEndpoint>
    <ResourceURI>https://outlook.office365.com</ResourceURI></ExternalService>
```

```
Response Code: 201
```

The following are the list of mandatory parameters required to create
                                    		  a Unified Messaging Service:

- Display Name: The display
                                          			 name of the unified messaging service

- Service Alias: The
                                          			 administrator account name of active directory

- Service Password: The
                                          			 administrator account password of active directory

- Server Type: The type of
                                          			 unified messaging service account. The value of Server Type for Office 365 is 5

- ExchOrgDomain: The domain
                                          			 name of hosted exchange server

- ExchDoAutodiscover: The
                                          			 Auto Discovery flag that should always be true for Office 365

AuthenticationMode: The web authentication mode for Unified Messaging. The possible authentication mode can be Basic (1),
                                                   NTLM (3) and OAuth2 (4) for Office 365 service. By default, the Authentication Mode is set to Basic (1).

If you select OAuth2 authentication mode for Office 365 service, you must provide the values of DirectoryID, ClientId and
                                                ClientSecret from Azure portal.

(Applicable to 12.5SU7 and later releases) If you select OAuth2 authentication mode for Office 365 service, Service Alias and Service Password fields are not required in API request body for adding Unified Messaging Service.

### Modifying Unified
                           	 Messaging Service

```
https://<connection_server>/vmrest/externalservices/<objectId>
```

```
<ExternalService>
 <ServiceAlias> client-team\administrator</ServiceAlias>
 <ServicePassword>Ecsbulab13</ServicePassword>
 <ServerType>4</ServerType> 
 <Server>10.65.156.190</Server>
 <AuthenticationMode>1</AuthenticationMode>
 <SecurityTransportType>1</SecurityTransportType>
</ExternalService>
```

```
<ExternalService>
 <ServiceAlias> client-team\administrator</ServiceAlias>
 <ServicePassword></ServicePassword>
 <ServerType>4</ServerType> 
 <Server>10.65.156.190</Server>
 <AuthenticationMode>4</AuthenticationMode>
 <SecurityTransportType>1</SecurityTransportType>
 <ClientId>d64ea56b-1d60-47c7-a26d-7bcbee3a09c3</ClientId>
 <ClientSecret></ClientSecret>
 <DirectoryID>cafae64a-ffb2-4585-8c11-2d86aa8b3bf5</DirectoryID>
</ExternalService>
```

```
Successful Response Code: 204
```

(Applicable to 12.5SU7 and later releases) If you select OAuth2 authentication mode for Office 365 service, Service Alias and Service Password fields are not relevant in modification of  Unified Messaging Service.

### Deleting Unified
                           	 Messaging Service

The following is an example of
                                 		  the DELETE request that deletes a Unified Messaging Service as represented by
                                 		  < externalserviceobject-id >:

```
https://<connection_server>/vmrest/usertemplates/externalservices/<objectId >
```

The output for this request returns the successful response code.

```
Response Code: 204
```

### Explanation of Data Fields

Field

Description

Display Name

The display name of the unified messaging service

Service Alias

The administrator account name of active directory

Service Password

The administrator account password of active directory

Server Type

The type of unified messaging service account. Possible values are:

1: For Meeting Place

4: For Exchange /BPOS-D

5: For Office 365

Server

The IP address of the Exchange server

Authentication Mode

The web-based Authentication Mode of the Unified Messaging Service. Possible value are:

1: For Basic

2: For Digest

3: For NTLM

4: OAuth2

By default, the Authentication Mode is set to Basic (1)

Exchange Server Type

The Exchange Server Type of the Unified Messaging Account. Possible values are:

0: Exchange 2003

1: Exchange 2007/2010/2013 and above

Security Transport Type

The web-based protocol of the Unified Messaging Account. Possible values are:

0: For HTTP

1: For HTTPS

TransferExtensionDialString

The digits that Cisco Unity Connection must dial to transfer users on the phone to the opening of the Cisco Unified Meeting
                                             Place Server

ExchOrgDomain

The domain name of hosted exchange server

ExchDoAutodiscover

The Auto Discovery flag that should always be true for Office 365

DirectoryID

(Applicable only when OAuth2 authentication mode is selected) Directory id of the application registered on Microsoft Azure portal

ClientID

(Applicable only when OAuth2 authentication mode is selected) Client id of the application registered on the Microsoft Azure portal

(Applicable only when OAuth2 authentication mode is selected) The value of Client Secret of the application registered on the Microsoft Azure portal.

AD Authentication Endpoint

(Applicable only when OAuth2 authentication mode is selected) This field is optional . Its value depend on Active Directory chosen on Microsoft Azure Portal. For different values of AD
                                             Authentication Endpoint, refer Endpoints of the registered application at Azure portal. Default value of AD Authentication
                                             Endpoint field is https://login.microsoftonline.com

Resource URI

(Applicable only when OAuth2 authentication mode is selected) This field is optional . Its value depend on Active Directory chosen on Microsoft Azure Portal.  Default value of Resource
                                             URI field is https://outlook.office365.com

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template External Service
                        	 Accounts

### About External
                           	 Service Accounts

A user template may have zero or more unified messaging service accounts
                              		(also known as external service accounts). Examples of these services include
                              		Cisco Unified MeetingPlace 8.0, Exchange 2003, Exchange 2007, and Exchange
                              		2010. Using CUPI for user templates, an administrator can:

- Retrieve a list of its
                                    		  unified messaging service accounts,

- Retrieve one of its unified
                                    		  messaging service accounts, and

- Change the password for one
                                    		  of its unified messaging service accounts

### Listing External
                           	 Service Accounts

To retrieve a list of unified
                                 		  messaging service accounts, use the GET method with URI:

```
https://<connection_server>/vmrest/usertemplates/usertemplateobject-id/templateexternalserviceaccounts
```

In the following example, the user has two unified messaging service
                                 		  accounts, Exchange2K3 and Exchange2K7:

```
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobject-id>/externalserviceaccounts
```

```
<TemplateExternalServiceAccounts total="1">
<TemplateExternalServiceAccount>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/templateexternalserviceaccounts/c4e7b01f-8b6e-4a08-9d57-856e81919c66</URI>
 <EmailAddressUseCorp>false</EmailAddressUseCorp>
 <EnableCalendarCapability>true</EnableCalendarCapability>
 <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
 <EnableMeetingCapability>false</EnableMeetingCapability>
 <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
 <ExternalServiceObjectId>26f20913-af8d-465a-8437-707028d376bd</ExternalServiceObjectId>
 <IsPrimaryMeetingService>false</IsPrimaryMeetingService>
 <LoginType>0</LoginType>
 <ObjectId>c4e7b01f-8b6e-4a08-9d57-856e81919c66</ObjectId>
 <UserTemplateObjectId>85a845d3-063d-4641-aa70-8b536282bffb</UserTemplateObjectId>
 <UserTemplateURI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb</UserTemplateURI>
 <DisplayName>UMS_AP1111I</DisplayName>
 <ServerType>4</ServerType>
 <UserTemplateDisplayName>Template</UserTemplateDisplayName>
</TemplateExternalServiceAccount>
</TemplateExternalServiceAccounts>
```

```
Response Code: 200
```

For each unified messaging service account, CUPI returns the following
                                 		  information:

- URI - The URI for
                                       			 retrieving the unified messaging service account

- IsEnabled - A flag to
                                       			 indicate whether the unified messaging service account is enabled

- UseServiceCredentials - A
                                       			 flag to indicate whether service credentials or user credentials are used to
                                       			 sign in the unified messaging service account

- LoginType - A flag to
                                       			 indicate whether the user alias (0), a guest account (1), or a specified user
                                       			 ID (2) is used to sign in the account

- UserId - The user ID to
                                       			 sign in to the unified messaging service account, if one is used

- ObjectId - The unique ID
                                       			 of the unified messaging service account

- Display Name - The display
                                       			 name of the unified messaging service account

To retrieve a specific unified messaging service account, use the GET
                                 		  method with the URI field from above as follows:

```
GET http://<connection_server>/vmrest/usertemplates/<objectId>/templateexternalserviceaccounts/<objectId>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<TemplateExternalServiceAccount>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/templateexternalserviceaccounts/c4e7b01f-8b6e-4a08-9d57-856e81919c66</URI>
 <EmailAddressUseCorp>false</EmailAddressUseCorp>
 <EnableCalendarCapability>true</EnableCalendarCapability>
 <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
 <EnableMeetingCapability>false</EnableMeetingCapability>
 <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
 <ExternalServiceObjectId>26f20913-af8d-465a-8437-707028d376bd</ExternalServiceObjectId>
 <IsPrimaryMeetingService>false</IsPrimaryMeetingService>
 <LoginType>0</LoginType>
 <ObjectId>c4e7b01f-8b6e-4a08-9d57-856e81919c66</ObjectId>
 <UserTemplateObjectId>85a845d3-063d-4641-aa70-8b536282bffb</UserTemplateObjectId>
 <UserTemplateURI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb</UserTemplateURI>
 <DisplayName>UMS_AP1111I</DisplayName>
 <ServerType>4</ServerType>
 <UserTemplateDisplayName>Template</UserTemplateDisplayName>
</TemplateExternalServiceAccount>
```

```
Response Code: 200
```

### Adding New
                           	 External Service Account

The following is an example of
                                 		  the POST request that adds a Unified Messaging Account:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/templateexternalserviceaccounts/<objectId>
```

The actual response will depend upon the information given by you. The
                                 		  following are the mandatory parameters that you need to enter to create a
                                 		  Unified Messaging Account:

```
<TemplateExternalServiceAccount>
 <ExternalServiceObjectId>NewUnfiedServiceAccount </ExternalServiceObjectId>
 <EnableCalendarCapability>true</EnableCalendarCapability>
 <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
 <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
</TemplateExternalServiceAccount>
```

```
Response Code: 201
```

### Modifying
                           	 External Service Account

The following is an example of
                                 		  the PUT request that modifies a Unified Messaging Account as represented by
                                 		  <unifiedmessagingaccountid>:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/ templateexternalserviceaccounts /<objectId>
```

The following is an example of the response from the above *PUT*
                                 		  request and the actual response will depend upon the information given by you:

```
<TemplateExternalServiceAccount>
 <EnableCalendarCapability>true</EnableCalendarCapability>
 <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
 <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
</TemplateExternalServiceAccount>
```

```
Response Code: 204
```

### Deleting External
                           	 Service Account

The following is an example of
                                 		  the DELETE request that deletes a Unified Messaging Account as represented by
                                 		  < externalserviceaccount-id >:

```
https://<connection_server>/vmrest/usertemplates/<template-object-id>/ templateexternalserviceaccounts /< objectId>
```

The output for this request returns the successful response code.

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

The following chart lists all of
                                 		  the data fields available on External Service Accounts.

0-Login using user's Connection alias used for login

1- Login as guest 2-Login as UserId| Base, Phone, Pager

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- End User Unified Messaging
                        	 Accounts

### Unified Messaging
                           	 Account API

#### Updating the
                              	 Unified Messaging Account

JSON Example

To view the unified messaging account, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/users/<userobjectid>/
externalserviceaccounts/<externalserviceaccountsobjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
{
     "EmailAddressUseCorp":"true"
     "EnableCalendarCapability":"true"
     "EnableMailboxSynchCapability":"true"
       "EnablTtsOfEmailCapability":"true"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

- false: The
                                                         						  external service is disabled.

- true: The
                                                         						  external service is enabled.

Default value: false.

- false: Use user
                                                         						  credentials.

- true: Use
                                                         						  service credentials.

| GET https://<connection-server>/vmrest/users/<user-objectid |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid>/externalserviceaccounts |
|---|

| <ExternalServiceAccount>
     <URI>/vmrest/users/9375d893-c8eb-437b-90bf-
   7de4b1d0c3e8/externalserviceaccounts/39871e30-849a-4dcf-b868-2faf360d503a</URI>
     <ObjectId>39871e30-849a-4dcf-b868-2faf360d503a</ObjectId>
     <ExternalServiceObjectId>1cd78b6c-1e6e-4542-a6e7-14f431d6569c</ExternalServiceObjectId>
     <SubscriberObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</SubscriberObjectId>
     <UserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</UserURI>
     <EnableCalendarCapability>true</EnableCalendarCapability>
     <EnableMeetingCapability>false</EnableMeetingCapability>
     <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
     <IsPrimaryMeetingService>false</IsPrimaryMeetingService>
     <LoginType>0</LoginType>
     <UserPassword/>
     <EmailAddress>chhavi@com</EmailAddress>
     <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
     <EmailAddressUseCorp>false</EmailAddressUseCorp>
</ExternalServiceAccount> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/users/<user-objectid>/externalserviceaccounts/<objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| Response Code: 200 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/users/<userobjectid>/
externalserviceaccounts/<externalserviceaccountsobjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
{
     "EmailAddressUseCorp":"true"
     "EnableCalendarCapability":"true"
     "EnableMailboxSynchCapability":"true"
       "EnablTtsOfEmailCapability":"true"
} |
|---|

| Response Code: 204 |
|---|

| Device Name | Data Type | Operation | Comments |
|---|---|---|---|
| EmailAddressUseCorp | Boolean | Read/Write | Use Corporate Email Address Default value: False |
| EnableTtsOfEmailCapability | Boolean | Read/Write | Access Exchange Email by Using Text to
                                             					 Speech (TTS) Default value: False |
| EnableCalendarCapability | Boolean | Read/Write | Access Exchange Calendar and Contacts Default value: False |
| EnableMailboxSynchCapability | Boolean | Read/Write | Synchronize Connection and Exchange
                                             					 Mailboxes (Single Inbox) Default value: False |

| GET https://<connection-server>/vmrestvmrest/usertemplates/<usertemplateobjectid> |
|---|

| GET https://<connection-
    server>/vmrestvmrest/usertemplates/<usertemplateobjectid>/templateexternalserviceacco
    unts |
|---|

| Request Body: 
<TemplateExternalServiceAccount>
    <EmailAddressUseCorp>true</EmailAddressUseCorp>
    <EnableCalendarCapability>true</EnableCalendarCapability>
    <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
    <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
</TemplateExternalServiceAccount> |
|---|

| Response Code: 204 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/usertemplates/<usertemplateobjectid>/templateexternalserviceaccounts/<templateexternalserviceaccountsobjectId 
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
    "EmailAddressUseCorp":"true"
    "EnableCalendarCapability":"true"
    "EnableMailboxSynchCapability":"true"
     "EnablTtsOfEmailCapability":"true"
} |
|---|

| Response Code: 200 |
|---|

| Device Name | Data Type | Operation | Comments |
|---|---|---|---|
| EmailAddressUseCorp | Boolean | Read/Write | Use Corporate Email Address Default value: False |
| EnableTtsOfEmailCapability | Boolean | Read/Write | Access Exchange Email by Using Text to
                                                					 Speech (TTS) Default value: False |
| EnableCalendarCapability | Boolean | Read/Write | Access Exchange Calendar and Contacts Default value: False |
| EnableMailboxSynchCapability | Boolean | Read/Write | Synchronize Connection and Exchange
                                                					 Mailboxes (Single Inbox) Default value: False |

| https://<connection_server>/vmrest/externalservices |
|---|

| <ExternalServices total="3">
  <ExternalService>
    <URI>/vmrest/externalservices/53a7675f-94c2-4596-ae3a-69b9287d119d</URI>
    <ObjectId>53a7675f-94c2-4596-ae3a-69b9287d119d</ObjectId>
    <AuthenticationMode>3</AuthenticationMode>
    <DisplayName>exchange_1</DisplayName>
    <IsEnabled>true</IsEnabled>
    <SecurityTransportType>1</SecurityTransportType>
    <Server>10.78.171.187</Server>
    <ServiceAlias>admin</ServiceAlias>
    <ServicePassword/>
    <ServerType>4</ServerType>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <SupportsTtsOfEmailCapability>true</SupportsTtsOfEmailCapability>
    <ValidateServerCertificate>false</ValidateServerCertificate>
    <UseServiceCredentials>true</UseServiceCredentials>
    <SupportsMailboxSynchCapability>true</SupportsMailboxSynchCapability>
    <ExchDoAutodiscover>false</ExchDoAutodiscover>
    <MailboxSynchFaxAction>1</MailboxSynchFaxAction>
    <MailboxSynchEmailAction>2</MailboxSynchEmailAction>
    <ExternalServiceResetURI>/vmrest/externalservices/53a7675f-94c2-4596-ae3a-69b9287d119d/reset</ExternalServiceResetURI>
  </ExternalService>
  <ExternalService>
    <URI>/vmrest/externalservices/bc1dbc08-bfdb-46e8-acb4-12cb511ebb01</URI>
    <ObjectId>bc1dbc08-bfdb-46e8-acb4-12cb511ebb01</ObjectId>
    <AuthenticationMode>1</AuthenticationMode>
    <DisplayName>ofc_365</DisplayName>
    <IsEnabled>true</IsEnabled>
    <ServiceAlias>admin</ServiceAlias>
    <ServicePassword/>
    <ServerType>5</ServerType>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <SupportsTtsOfEmailCapability>true</SupportsTtsOfEmailCapability>
    <ValidateServerCertificate>false</ValidateServerCertificate>
    <UseServiceCredentials>true</UseServiceCredentials>
    <SupportsMailboxSynchCapability>true</SupportsMailboxSynchCapability>
    <ExchDoAutodiscover>true</ExchDoAutodiscover>
    <ExchOrgDomain>10.78.171.70</ExchOrgDomain>
    <ExchSite/>
    <MailboxSynchFaxAction>1</MailboxSynchFaxAction>
    <MailboxSynchEmailAction>2</MailboxSynchEmailAction>
    <ProxyServer/>
    <ExternalServiceResetURI>/vmrest/externalservices/bc1dbc08-bfdb-46e8-acb4-12cb511ebb01/reset</ExternalServiceResetURI>
  </ExternalService>
  <ExternalService>
    <URI>/vmrest/externalservices/9d7f6b48-19fc-446a-8afe-6d454a0b3de1</URI>
    <ObjectId>9d7f6b48-19fc-446a-8afe-6d454a0b3de1</ObjectId>
    <DisplayName>meeting_place</DisplayName>
    <IsEnabled>true</IsEnabled>
    <Server>10.78.171.87</Server>
    <ServiceAlias>admin</ServiceAlias>
    <ServicePassword/>
    <ServerType>1</ServerType>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <SupportsMeetingCapability>true</SupportsMeetingCapability>
    <TransferExtensionDialString>12112</TransferExtensionDialString>
  </ExternalService>
</ExternalServices> |
|---|

| https://<connection_server>/vmrest/externalservices/<objectId> |
|---|

| <ExternalService>
 <URI>/vmrest/externalservices/6f4f7023-e9e5-4cd0-bf55-e20a0be6fd78</URI>
 <ObjectId>6f4f7023-e9e5-4cd0-bf55-e20a0be6fd78</ObjectId>
 <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
 <AuthenticationMode>1</AuthenticationMode>
 <DisplayName>UMS_API</DisplayName>
 <IsEnabled>true</IsEnabled>
 <SecurityTransportType>1</SecurityTransportType>
 <Server>10.65.156.190</Server>
 <ServiceAlias>clientteam\administrator</ServiceAlias>
 <ServicePassword/>
 <ServerType>4</ServerType>
 <SupportsCalendarCapability>true</SupportsCalendarCapability>
 <SupportsTtsOfEmailCapability>true</SupportsTtsOfEmailCapability>
 <ValidateServerCertificate>false</ValidateServerCertificate>
 <UseServiceCredentials>true</UseServiceCredentials>
 <SupportsMailboxSynchCapability>true</SupportsMailboxSynchCapability>
 <ExchDoAutodiscover>false</ExchDoAutodiscover>
 <MailboxSynchFaxAction>1</MailboxSynchFaxAction>
 <MailboxSynchEmailAction>2</MailboxSynchEmailAction>
</ExternalService> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/externalservices?query=(TenantObjectId is <Tenant-ObjectId>) |
|---|

| GET https://<connection-server>/vmrest/tenants |
|---|

| https://<connection_server>/vmrest/externalservices |
|---|

| <ExternalService>
 <DisplayName>UMS_API</DisplayName>
 <ServiceAlias> client-team\administrator</ServiceAlias>
 <ServicePassword>Ecsbulab12</ServicePassword>
 <ServerType>4</ServerType> 
 <Server>10.65.156.190</Server>
 <AuthenticationMode>1</AuthenticationMode>
 <SecurityTransportType>1</SecurityTransportType>
</ExternalService> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/externalservices |
|---|

| <ExternalService>
 <DisplayName>MeetingPlace</DisplayName>
 <ServiceAlias> admin</ServiceAlias>
 <ServicePassword>ecsbulab</ServicePassword>
 <ServerType>1</ServerType>
 <Server>10.76.175.167</Server>
 <TransferExtensionDialString>111111</TransferExtensionDialString>
</ExternalService> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/externalservices |
|---|

| <ExternalService>
    <DisplayName>OFC_Service</DisplayName>
    <IsEnabled>true</IsEnabled>
    <ExchDoAutodiscover>true</ExchDoAutodiscover>
    <ExchOrgDomain>domain.com</ExchOrgDomain>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <ServiceAlias>admin</ServiceAlias>
    <SupportsCalendarCapability>true</SupportsCalendarCapability>
    <SupportsTtsOfEmailCapability>true</SupportsTtsOfEmailCapability>
    <SupportsMeetingCapability>false</SupportsMeetingCapability>
    <ValidateServerCertificate>false</ValidateServerCertificate>
    <UseServiceCredentials>true</UseServiceCredentials>
    <AuthenticationMode>4</AuthenticationMode>
    <ServicePassword>password123</ServicePassword>
    <ServerType>5</ServerType>
    <ClientId>d64ea56b-1d60-47c7-a26d-7bcbee3a09c3</ClientId>
    <ClientSecret> </ClientSecret>
    <DirectoryID>cafae64a-ffb2-4585-8c11-2d86aa8b3bf5</DirectoryID>
    <AdAuthenticationEndpoint>https://login.microsoftonline.com</AdAuthenticationEndpoint>
    <ResourceURI>https://outlook.office365.com</ResourceURI></ExternalService> |
|---|

| Response Code: 201 |
|---|

| Note | AuthenticationMode: The web authentication mode for Unified Messaging. The possible authentication mode can be Basic (1),
                                                   NTLM (3) and OAuth2 (4) for Office 365 service. By default, the Authentication Mode is set to Basic (1). |
|---|---|

| Note | If you select OAuth2 authentication mode for Office 365 service, you must provide the values of DirectoryID, ClientId and
                                                ClientSecret from Azure portal. |
|---|---|

| Note | (Applicable to 12.5SU7 and later releases) If you select OAuth2 authentication mode for Office 365 service, Service Alias and Service Password fields are not required in API request body for adding Unified Messaging Service. |
|---|---|

| https://<connection_server>/vmrest/externalservices/<objectId> |
|---|

| <ExternalService>
 <ServiceAlias> client-team\administrator</ServiceAlias>
 <ServicePassword>Ecsbulab13</ServicePassword>
 <ServerType>4</ServerType> 
 <Server>10.65.156.190</Server>
 <AuthenticationMode>1</AuthenticationMode>
 <SecurityTransportType>1</SecurityTransportType>
</ExternalService> |
|---|

| <ExternalService>
 <ServiceAlias> client-team\administrator</ServiceAlias>
 <ServicePassword></ServicePassword>
 <ServerType>4</ServerType> 
 <Server>10.65.156.190</Server>
 <AuthenticationMode>4</AuthenticationMode>
 <SecurityTransportType>1</SecurityTransportType>
 <ClientId>d64ea56b-1d60-47c7-a26d-7bcbee3a09c3</ClientId>
 <ClientSecret></ClientSecret>
 <DirectoryID>cafae64a-ffb2-4585-8c11-2d86aa8b3bf5</DirectoryID>
</ExternalService> |
|---|

| Successful Response Code: 204 |
|---|

| Note | (Applicable to 12.5SU7 and later releases) If you select OAuth2 authentication mode for Office 365 service, Service Alias and Service Password fields are not relevant in modification of  Unified Messaging Service. |
|---|---|

| https://<connection_server>/vmrest/usertemplates/externalservices/<objectId > |
|---|

| Response Code: 204 |
|---|

| Field | Description |
|---|---|
| Display Name | The display name of the unified messaging service |
| Service Alias | The administrator account name of active directory |
| Service Password | The administrator account password of active directory |
| Server Type | The type of unified messaging service account. Possible values are: 1: For Meeting Place 4: For Exchange /BPOS-D 5: For Office 365 |
| Server | The IP address of the Exchange server |
| Authentication Mode | The web-based Authentication Mode of the Unified Messaging Service. Possible value are: 1: For Basic 2: For Digest 3: For NTLM 4: OAuth2 By default, the Authentication Mode is set to Basic (1) |
| Exchange Server Type | The Exchange Server Type of the Unified Messaging Account. Possible values are: 0: Exchange 2003 1: Exchange 2007/2010/2013 and above |
| Security Transport Type | The web-based protocol of the Unified Messaging Account. Possible values are: 0: For HTTP 1: For HTTPS |
| TransferExtensionDialString | The digits that Cisco Unity Connection must dial to transfer users on the phone to the opening of the Cisco Unified Meeting
                                             Place Server |
| ExchOrgDomain | The domain name of hosted exchange server |
| ExchDoAutodiscover | The Auto Discovery flag that should always be true for Office 365 |
| DirectoryID | (Applicable only when OAuth2 authentication mode is selected) Directory id of the application registered on Microsoft Azure portal |
| ClientID | (Applicable only when OAuth2 authentication mode is selected) Client id of the application registered on the Microsoft Azure portal |
| ClientSecret | (Applicable only when OAuth2 authentication mode is selected) The value of Client Secret of the application registered on the Microsoft Azure portal. |
| AD Authentication Endpoint | (Applicable only when OAuth2 authentication mode is selected) This field is optional . Its value depend on Active Directory chosen on Microsoft Azure Portal. For different values of AD
                                             Authentication Endpoint, refer Endpoints of the registered application at Azure portal. Default value of AD Authentication
                                             Endpoint field is https://login.microsoftonline.com |
| Resource URI | (Applicable only when OAuth2 authentication mode is selected) This field is optional . Its value depend on Active Directory chosen on Microsoft Azure Portal.  Default value of Resource
                                             URI field is https://outlook.office365.com |

| https://<connection_server>/vmrest/usertemplates/usertemplateobject-id/templateexternalserviceaccounts |
|---|

| GET https://<connection-server>/vmrest/usertemplates/<usertemplateobject-id>/externalserviceaccounts |
|---|

| <TemplateExternalServiceAccounts total="1">
<TemplateExternalServiceAccount>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/templateexternalserviceaccounts/c4e7b01f-8b6e-4a08-9d57-856e81919c66</URI>
 <EmailAddressUseCorp>false</EmailAddressUseCorp>
 <EnableCalendarCapability>true</EnableCalendarCapability>
 <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
 <EnableMeetingCapability>false</EnableMeetingCapability>
 <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
 <ExternalServiceObjectId>26f20913-af8d-465a-8437-707028d376bd</ExternalServiceObjectId>
 <IsPrimaryMeetingService>false</IsPrimaryMeetingService>
 <LoginType>0</LoginType>
 <ObjectId>c4e7b01f-8b6e-4a08-9d57-856e81919c66</ObjectId>
 <UserTemplateObjectId>85a845d3-063d-4641-aa70-8b536282bffb</UserTemplateObjectId>
 <UserTemplateURI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb</UserTemplateURI>
 <DisplayName>UMS_AP1111I</DisplayName>
 <ServerType>4</ServerType>
 <UserTemplateDisplayName>Template</UserTemplateDisplayName>
</TemplateExternalServiceAccount>
</TemplateExternalServiceAccounts> |
|---|

| Response Code: 200 |
|---|

| GET http://<connection_server>/vmrest/usertemplates/<objectId>/templateexternalserviceaccounts/<objectId> |
|---|

| <?xml version="1.0" encoding="UTF-8"?>
<TemplateExternalServiceAccount>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/templateexternalserviceaccounts/c4e7b01f-8b6e-4a08-9d57-856e81919c66</URI>
 <EmailAddressUseCorp>false</EmailAddressUseCorp>
 <EnableCalendarCapability>true</EnableCalendarCapability>
 <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
 <EnableMeetingCapability>false</EnableMeetingCapability>
 <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
 <ExternalServiceObjectId>26f20913-af8d-465a-8437-707028d376bd</ExternalServiceObjectId>
 <IsPrimaryMeetingService>false</IsPrimaryMeetingService>
 <LoginType>0</LoginType>
 <ObjectId>c4e7b01f-8b6e-4a08-9d57-856e81919c66</ObjectId>
 <UserTemplateObjectId>85a845d3-063d-4641-aa70-8b536282bffb</UserTemplateObjectId>
 <UserTemplateURI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb</UserTemplateURI>
 <DisplayName>UMS_AP1111I</DisplayName>
 <ServerType>4</ServerType>
 <UserTemplateDisplayName>Template</UserTemplateDisplayName>
</TemplateExternalServiceAccount> |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/templateexternalserviceaccounts/<objectId> |
|---|

| <TemplateExternalServiceAccount>
 <ExternalServiceObjectId>NewUnfiedServiceAccount </ExternalServiceObjectId>
 <EnableCalendarCapability>true</EnableCalendarCapability>
 <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
 <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
</TemplateExternalServiceAccount> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/ templateexternalserviceaccounts /<objectId> |
|---|

| <TemplateExternalServiceAccount>
 <EnableCalendarCapability>true</EnableCalendarCapability>
 <EnableTtsOfEmailCapability>true</EnableTtsOfEmailCapability>
 <EnableMailboxSynchCapability>true</EnableMailboxSynchCapability>
</TemplateExternalServiceAccount> |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/usertemplates/<template-object-id>/ templateexternalserviceaccounts /< objectId> |
|---|

| Response Code: 204 |
|---|

| Field Name | Writable? | Available Value | Explanation/Comments |
|---|---|---|---|
| EmailAddressUseCorp | Read/Write | True/False | Use Corporate Email Address |
| EnableCalendarCapability | Read/Write | True/False | Enables users to hear notification of
                                             					 upcoming meetings on the phone. |
| EnableMailboxSynchCapability | Read/Write | True/False | Synchronizes voice messages in Connection
                                             					 and Exchange. |
| EnableMeetingCapability | Read Only | True/False | Enables Meeting Capability |
| EnableTtsOfEmailCapability | Read/Write | True/False | Enables users to access Exchange email
                                             					 messages by using text to speech. |
| ExternalServiceObjectId | Read Only | 36 characters | Displays External Service ObjectId |
| IsPrimaryMeetingService read | Read Only | True/False | Displays Primary Meeting Service |
| LoginType | Read/Write | 0-Login using user's Connection alias used for login 1- Login as guest 2-Login as UserId\| Base, Phone, Pager | Dipslays the type of login done by the |
| ObjectId | All | Read Only | ObjectId of the Device |
| UserTemplateURI | Read Only |  | Displays user template URI |
| UserTemplateObjectId | Read Only | 36 characters | Displays user template ObjectId |
| DisplayName | All | Read/Write | Friendly name for the Device like "Mobile
                                             					 Phone" |
| ServerType | Read Only | 1-MeetingPlace
                                             					 8.x,4-Exchange/BPOS-D,5-Office 365 | Displays the name of the external service
                                             					 account |
| UserTemplateDisplayName | Read Only | 1-64 characters | Display Name for User Template. |

| Request URI:
PUT https://<connection-server>/vmrest/users/<userobjectid>/
externalserviceaccounts/<externalserviceaccountsobjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
{
     "EmailAddressUseCorp":"true"
     "EnableCalendarCapability":"true"
     "EnableMailboxSynchCapability":"true"
       "EnablTtsOfEmailCapability":"true"
} |
|---|

| Response Code: 204 |
|---|

| Parameters | Operation | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | URI of the Unified Messaging Account. |
| ObjectId | Read Only | String (36) | Unique Identifier of the Unified Messaging
                                                					 Account. |
| IsEnabled | Read Only | Boolean | A flag indicating whether the external
                                                					 service is enabled. false: The
                                                         						  external service is disabled. true: The
                                                         						  external service is enabled. Default value: false. |
| UseServiceCredentials | Read Only | Boolean | A flag indicating whether to use service
                                                					 credentials rather than user credentials to logon to the external service. false: Use user
                                                         						  credentials. true: Use
                                                         						  service credentials. |
| Login Type | Read Only | Integer | A flag to indicate whether the user alias
                                                					 (0), a guest account (1), or a specified user ID (2) is used to sign in the
                                                					 account . |
| Display Name | Read/Write | String (64) | The display name of the unified messaging
                                                					 service account. |
| UserId | Read Only | String | The user ID to sign in to the unified
                                                					 messaging service account, if one is used |