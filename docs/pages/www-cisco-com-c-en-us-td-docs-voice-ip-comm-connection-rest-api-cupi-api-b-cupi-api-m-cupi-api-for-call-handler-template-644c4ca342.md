---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-for-call-handler-template-644c4ca342
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-cupi-api-for-call-handler-templates.html
retrieved_at: 2026-08-17T03:49:24.297185+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for Call Handler Template

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for Call Handler Template

# Cisco Unity Connection Provisioning Interface (CUPI) API for Call Handler Template

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Caller Input APIs

### Caller Inputs
                           	 API

To get the caller input URI, follow
                              		the steps given below:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

From above URI get the call handler URI:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

To edit caller inputs, you need to get the menu entries:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/menuentries
```

#### Listing the Caller
                              	 Inputs

The following is an example of
                                    		  the GET request that fetch the list of caller inputs:

```
GET https://<connection-server>/vmrest/ callhandlertemplates/<callhandlertemplate-
  objectid>/templatemenuentries
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<TemplateMenuEntries total="2">
  <TemplateMenuEntry>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templatemenuentries/*</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <TouchtoneKey>*</TouchtoneKey>
    <Locked>false</Locked>
    <Action>4</Action>
    <ObjectId>de3dce46-1887-489c-9244-ae8b421fe107</ObjectId>
  </TemplateMenuEntry>
  <TemplateMenuEntry>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templatemenuentries/#</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <TouchtoneKey>#</TouchtoneKey>
    <Locked>false</Locked>
    <Action>5</Action>
    <ObjectId>17ec06a9-6990-4a95-8417-6e22957fcbe5</ObjectId>
  </TemplateMenuEntry>
</TemplateMenuEntries>
```

```
Response Code: 200
```

JSON Example

To view the list of caller inputs, do the following:

```
Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templatemenuentries
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total":"2"
  "TemplateMenuEntry":    
  {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templatemenuentries/*"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "TouchtoneKey":"*"
    "Locked":"true"
    "Action":"2"
    "TargetConversation":"SubSignIn"
    "ObjectId":"17184311-90ac-4654-8e26-cfbe08138851"
  },
  {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a/templatemenuentries/#"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "TouchtoneKey":"#"
    "Locked":"true"
    "Action":"5"
    "ObjectId":"27eb298c-22a1-4ed7-813b-61c144bc0fdc"
  },
  ]
}
```

```
Response Code: 200
```

#### Viewing the
                              	 Details of Specific Caller Input

The following is an example of
                                    		  the GET request that lists the details of specific caller input:

```
GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
  objectid>/templatemenuentries/<TouchToneKey>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<TemplateMenuEntry>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
836910ac1a4c/templatemenuentries/5</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
836910ac1a4c</CallhandlerURI>
    <TouchtoneKey>5</TouchtoneKey>
    <Locked>false</Locked>
    <Action>0</Action>
    <ObjectId>f076155c-80b1-4538-bcc7-c901a6eafbae</ObjectId>
</TemplateMenuEntry>
```

```
Response Code: 200
```

JSON Example

To view a particular caller input, do the following:

```
Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templatemenuentries/<TouchToneKey>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templatemenuentries/*"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "TouchtoneKey":"*"
    "Locked":"true"
    "Action":"2"
    "TargetConversation":"SubSignIn"
    "ObjectId":"17184311-90ac-4654-8e26-cfbe08138851"
}
```

```
Response Code: 200
```

#### Updating a Caller
                              	 Input

The following is an example of
                                    		  the PUT request that updates a specific caller input:

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
objectid>/templatemenuentries/<TouchToneKey>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
<TemplateMenuEntry>
    <Action>7</Action>
    <TransferNumber>1000</TransferNumber>
    <TransferType> 1</TransferType>
    <TransferRings>2</TransferRings>
</TemplateMenuEntry>
```

```
Response Code: 204
```

JSON Example

To update a particular caller input, do the following:

```
Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templatemenuentries/<TouchToneKey>
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

A locked menu entry does not allow additional dialing after
                                                   						this choice is entered, but Cisco Unity Connection will immediately take the
                                                   						associated action. If the action is set to "Ignore" (0), the key is thrown out
                                                   						and the greeting continues playing as normal. Any other action is taken
                                                   						immediately without waiting to determine if the caller is going to dial an
                                                   						extension. Possible Values:

- false: Unlocked
                                                         						  - Additional dialing after this choice is entered is allowed

- true: Locked -
                                                         						  Additional dialing is ignored

Default value: false

Default value: 0

Default value: 0

Default value: 0

Possible value can range from 2-20 Default Value: 4

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Call Handler Template
                        	 APIs

### Call Handler
                           	 Templates APIs

Each call handler that you add in Cisco Unity Connection is based on a
                              		template. Settings from the template are applied as the call handler is
                              		created. Unity Connection comes with one default call handler template, which
                              		has settings that are suitable for most call handlers. You can also create new
                              		templates. Before you create call handlers, review the settings in the template
                              		that you plan to use and determine whether you need to make changes or create
                              		new templates. For each template, you should consider enabling the transfer,
                              		caller input, greetings, and message settings that will be needed for the call
                              		handlers that you plan to create. Following Points should be noted:-

- If you change settings on a
                                    		  call handler template, the new settings are in effect only for new call
                                    		  handlers that are created by using that template. Changes to template settings
                                    		  do not affect existing call handlers.

- Deleting a call handler
                                    		  template does not affect any call handlers that were based on that template
                                    		  when they were created.

- Default Template cannot be
                                    		  deleted.

Administrator can use this API to create/update/delete/fetch the system
                              		call handler templates. Various attributes of a call handler template can also
                              		be updated using this API.

#### Listing the Call
                              	 Handler Templates

The following is an example of
                                    		  the GET request that fetch the list of call handler templates:

```
GET https://<connection-server>/vmrest/callhandlertemplates
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<CallhandlerTemplates total="1">
  <CallhandlerTemplate>
    <URI>/vmrest/callhandlertemplates/5024347a-aac2-463a-98c8-a745a805dc3b</URI>
    <CreationTime>2013-01-10T09:23:20Z</CreationTime>
    <Language>1033</Language>
    <DisplayName>System Call Handler Template1</DisplayName>
    <UseDefaultLanguage>false</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Undeletable>true</Undeletable>
    <LocationObjectId>22646a82-1f17-4b42-beec-9cdfd69508c5</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/22646a82-1f17-4b42-beec-
    9cdfd69508c5</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <MaxMsgLen>300</MaxMsgLen>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>10fee566-b137-4652-a378-
    db8a872a161d</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/10fee566-b137-4652-a378-
    db8a872a161d</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <IsTemplate>true</IsTemplate>
    <ObjectId>5024347a-aac2-463a-98c8-a745a805dc3b</ObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <RecipientDistributionListObjectId>f7408e6e-822e-494b-ab29-
    cff3cf9e0bd9</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/f7408e6e-822e-494b-ab29-
    cff3cf9e0bd9</RecipientDistributionListURI>
    <AfterMessageAction>2</AfterMessageAction>
    <AfterMessageTargetConversation>PHGreeting</AfterMessageTargetConversation>
    <AfterMessageTargetHandlerObjectId>16cf736f-7254-4654-ab09-
    08fe743332a9</AfterMessageTargetHandlerObjectId>
    <TimeZone>190</TimeZone>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</PhoneSystemURI>
    <UseCallLanguage>false</UseCallLanguage>
    <SendSecureMsg>false</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>f3beb4e4-0be5-417f-9491-
    e233c6d4a40e</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/f3beb4e4-0be5-417f-9491-
    e233c6d4a40e</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>5ec15c45-ace9-41ad-a6c4-b56081c79717</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/5ec15c45-ace9-41ad-a6c4-
    b56081c79717</PartitionURI>
    <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
    <SendPrivateMsg>0</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/callhandlertemplates/5024347a-aac2-463a-98c8-
    a745a805dc3b/templategreetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/callhandlertemplates/5024347a-aac2-463a-98c8-
    a745a805dc3b/templatetransferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/callhandlertemplates/5024347a-aac2-463a-98c8-
    a745a805dc3b/templatemenuentries</MenuEntriesURI>
  </CallhandlerTemplate>
</CallhandlerTemplates>
```

```
Response Code: 200
```

JSON Example

To view the list of call handler templates, do the following:

```
Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total":"1"
  "CallhandlerTemplate":  [
  {
    "URI":"/vmrest/callhandlertemplates/7a022382-8d0a-4289-880d-d2a432494b02"
    "CreationTime":"2013-02-25T09:39:23Z"
    "Language":"1033"
    "DisplayName":"System Call Handler Template"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"true"
    "Undeletable":"true"
    "LocationObjectId":"cff1347e-87af-4409-bead-d1970625f82e"
    "LocationURI":"/vmrest/locations/connectionlocations/cff1347e-87af-4409-bead-
    d1970625f82e"
    "EditMsg":"true"
    "IsPrimary":"false"
    "MaxMsgLen":"300"
    "OneKeyDelay":"1500"
    "ScheduleSetObjectId":"5fc5a5d7-eaf6-4f4d-80cf-f76f3893ac0e"
    "ScheduleSetURI":"/vmrest/schedulesets/5fc5a5d7-eaf6-4f4d-80cf-f76f3893ac0e"
    "SendUrgentMsg":"0"
    "IsTemplate":"true"
    "ObjectId":"7a022382-8d0a-4289-880d-d2a432494b02"
    "TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438",
    "RecipientDistributionListObjectId":"dea18b5b-4493-4715-a558-cb85778fd823"
    "RecipientDistributionListURI":"/vmrest/distributionlists/dea18b5b-4493-4715-a558-
    cb85778fd823"
    "AfterMessageAction":"2"
    "AfterMessageTargetConversation":"PHGreeting"
    "AfterMessageTargetHandlerObjectId":"c6af281b-dc8b-45b4-a1e9-eccc523d5fb2"
    "TimeZone":"190"
    "MediaSwitchObjectId":"0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "PhoneSystemURI":"/vmrest/phonesystems/0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "UseCallLanguage":"true"
    "SendSecureMsg":"false"
    "EnablePrependDigits":"false"
    "DispatchDelivery":"false"
    "CallSearchSpaceObjectId":"2e836e16-f715-4a18-bb7c-ee5e33281706"
    "CallSearchSpaceURI":"/vmrest/searchspaces/2e836e16-f715-4a18-bb7c-
    ee5e33281706"
    "InheritSearchSpaceFromCall":"true"
    "PartitionObjectId":"97bf6afe-346e-4275-967e-43c50be79d32"
    "PartitionURI":"/vmrest/partitions/97bf6afe-346e-4275-967e-43c50be79d32"
    "PlayPostGreetingRecording":"0"
    "SendPrivateMsg":"0"
    "PlayAfterMessage":"1"
    "GreetingsURI":"/vmrest/callhandlertemplates/7a022382-8d0a-4289-880d-
    d2a432494b02/templategreetings"
    "TransferOptionsURI":"/vmrest/callhandlertemplates/7a022382-8d0a-4289-880d-
    d2a432494b02/templatetransferoptions"
    "MenuEntriesURI":"/vmrest/callhandlertemplates/7a022382-8d0a-4289-880d-
    d2a432494b02/templatemenuentries"
  }
  ]
}
```

```
Response Code: 200
```

#### Listing Specific Tenant Related Call Handler Templates by System Administrator

In Cisco Unity Connection 10.5(2) and later, the system administrator can use TenantObjectID to list the specific tenant related
                                    call handler templates using the following URI:

```
GET https://<connection-server>/vmrest/callhandlertemplates?query=(TenantObjectId is <Tenant-ObjectId>)
```

To get the TenantObjectID, use the following URI:

```
GET https://<connection-server>/vmrest/tenants
```

### Viewing the
                           	 Details of Specific Call Handler Template

The following is an example of
                                 		  the GET request that lists the details of specific call handler template
                                 		  represented by the provided value of call handler template object ID:

```
GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<CallhandlerTemplate>
    <URI>/vmrest/callhandlertemplates/edcd2336-2c01-49d1-89ff-8746466e0a5e</URI>
    <CreationTime>2013-01-12T11:40:19Z</CreationTime>
    <Language>1033</Language>
    <DisplayName>CallHandler1</DisplayName>
    <UseDefaultLanguage>false</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Undeletable>false</Undeletable>
    <LocationObjectId>22646a82-1f17-4b42-beec-9cdfd69508c5</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/22646a82-1f17-4b42-beec-
    9cdfd69508c5</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <MaxMsgLen>300</MaxMsgLen>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>10fee566-b137-4652-a378-db8a872a161d</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/10fee566-b137-4652-a378-
    db8a872a161d</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <IsTemplate>true</IsTemplate>
    <ObjectId>edcd2336-2c01-49d1-89ff-8746466e0a5e</ObjectId>
    <RecipientSubscriberObjectId>f74c4f98-598e-4c47-bf1a-
    2b78fc2c2953</RecipientSubscriberObjectId>
    <RecipientUserURI>/vmrest/users/f74c4f98-598e-4c47-bf1a-2b78fc2c2953</RecipientUserURI>
    <AfterMessageAction>1</AfterMessageAction>
    <TimeZone>190</TimeZone>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</PhoneSystemURI>
    <UseCallLanguage>false</UseCallLanguage>
    <SendSecureMsg>false</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>f3beb4e4-0be5-417f-9491-e233c6d4a40e</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/f3beb4e4-0be5-417f-9491-
    e233c6d4a40e</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>5ec15c45-ace9-41ad-a6c4-b56081c79717</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/5ec15c45-ace9-41ad-a6c4-b56081c79717</PartitionURI>
    <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
    <SendPrivateMsg>0</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/callhandlertemplates/edcd2336-2c01-49d1-89ff-
    8746466e0a5e/templategreetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/callhandlertemplates/edcd2336-2c01-49d1-89ff-
    8746466e0a5e/templatetransferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/callhandlertemplates/edcd2336-2c01-49d1-89ff-
    8746466e0a5e/templatemenuentries</MenuEntriesURI>
</CallhandlerTemplate>
```

```
Response Code: 200
```

JSON Example

To view a specific call handler template, do the following:

```
Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
    "URI":"/vmrest/callhandlertemplates/93b8ada5-c92f-47e6-8d24-9c269293d63c"
    "CreationTime":"2013-02-26T06:45:09Z"
    "Language":"1033"
    "DisplayName":"Call_Handler1"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"false"
    "Undeletable":"false"
    "LocationObjectId":"cff1347e-87af-4409-bead-d1970625f82e"
    "LocationURI":"/vmrest/locations/connectionlocations/cff1347e-87af-4409-bead-
    d1970625f82e"
    "EditMsg":"true"
    "IsPrimary":"false"
    "MaxMsgLen":"500"
    "OneKeyDelay":"1500"
    "ScheduleSetObjectId":"5c42abd2-84a5-4fcf-84cf-d0a19c70f207"
    "ScheduleSetURI":"/vmrest/schedulesets/5c42abd2-84a5-4fcf-84cf-d0a19c70f207"
    "SendUrgentMsg":"1"
    "IsTemplate":"true"
    "ObjectId":"93b8ada5-c92f-47e6-8d24-9c269293d63c"
    "RecipientDistributionListObjectId":"8337a757-b074-42ff-85bd-acda2dfd5d28"
    "RecipientDistributionListURI":"/vmrest/distributionlists/8337a757-b074-42ff-85bd-
    acda2dfd5d28"
    "AfterMessageAction":"2"
    "AfterMessageTargetConversation":"AD"
    "AfterMessageTargetHandlerObjectId":"4783cb28-79a6-409a-bf57-18f8208b4e61"
    "TimeZone":"190"
    "MediaSwitchObjectId":"343dc222-2d1a-4a19-a5b6-894725542475"
    "PhoneSystemURI":"/vmrest/phonesystems/343dc222-2d1a-4a19-a5b6-894725542475"
    "UseCallLanguage":"true"
    "SendSecureMsg":"false"
    "EnablePrependDigits":"false"
    "DispatchDelivery":"true"
    "CallSearchSpaceObjectId":"2e836e16-f715-4a18-bb7c-ee5e33281706"
    "CallSearchSpaceURI":"/vmrest/searchspaces/2e836e16-f715-4a18-bb7c-ee5e33281706"
    "InheritSearchSpaceFromCall":"true"
    "PartitionObjectId":"44bdcf73-d5c1-4866-957d-fb35686cbe76"
    "PartitionURI":"/vmrest/partitions/44bdcf73-d5c1-4866-957d-fb35686cbe76"
    "PlayPostGreetingRecording":"2"
    "SendPrivateMsg":"0"
    "PlayAfterMessage":"2"
    "GreetingsURI":"/vmrest/callhandlertemplates/93b8ada5-c92f-47e6-8d24-
    9c269293d63c/templategreetings"
    "TransferOptionsURI":"/vmrest/callhandlertemplates/93b8ada5-c92f-47e6-8d24-
    9c269293d63c/templatetransferoptions"
}
```

```
Response Code: 200
```

### Creating a New
                           	 Call Handler Template

Mandatory parameters are:

- Display Name

- Phone System - Fetch phone systems using URI: https://<connection-server>/vmrest/phonesystems

- Message recipient - The
                                       			 message recipient can be a distribution list or a user. Use the following URI
                                       			 to fetch users or distribution lists respectively.

- https://<connection-server>/vmrest/users

- https://<connection-server>/vmrest/distributionlists

The following is an example of the POST request that creates a new
                                 		  call handler template:

```
POST https://<connection-server>/vmrest/callhandlertemplates
Request Body:
  <CallhandlerTemplate>
    <DisplayName>System Call Handler Template1</DisplayName>
    <RecipientSubscriberObjectId>f74c4f98-598e-4c47-bf1a-
    2b78fc2c2953</RecipientSubscriberObjectId>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-d3b13f5040f5</MediaSwitchObjectId>
  </CallhandlerTemplate>
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
```

JSON Example

To create a new call handler template, do the following:

```
Request URI:
POST: https://<connection-server>/vmrest/callhandlertemplates
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
"DisplayName":"Tenant",
"RecipientDistributionListObjectId":"8337a757-b074-42ff-85bd-acda2dfd5d28",
"MediaSwitchObjectId":"343dc222-2d1a-4a19-a5b6-894725542475"
}
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
```

### Delete the Call
                           	 Handler Template

The following is an example of
                                 		  the DELETE request that can be used to delete a call handler template:

```
DELETE https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To delete a call handler template, do the following:

```
Request URI:
DELETE: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Assigning a
                           	 Schedule to a Call Handler Template

The following is an example of
                                 		  the PUT request that can be used to assign a schedule to a call handler
                                 		  template:

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
The ScheduleSetObjectId can be fetched using the URI https://<connection-server>/vmrest/schedulesets.
```

```
<CallhandlerTemplate>
    <ScheduleSetObjectId>eb11c6cc-fc9e-4651-8c01-8f0b2e421918</ScheduleSetObjectId>
</CallhandlerTemplate>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To assign a schedule to a call handler template, do the following:

```
Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

```
{
    "ScheduleSetObjectId":"5c42abd2-84a5-4fcf-84cf-d0a19c70f207"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Updating Partition
                           	 of the Call Handler Template

This PUT request can be used to
                                 		  assign partition to a call handler template.

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
```

To fetch PartitionObjectId, use the URI https://<connection-server>/vmrest/partitions.

```
<CallhandlerTemplate>
    <PartitionObjectId>46a0377b-00d7-40a0-8738-81106fc730ea</PartitionObjectId>
</CallhandlerTemplate>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update partition of call handler template, do the following:

```
<pre>
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
</pre>
```

```
{
"PartitionObjectId":"fe2fe907-bdcb-416e-89b7-c1bb130d0f98"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Updating Language
                           	 Option of the Call Handler Template

This PUT request can be used to
                                 		  update language for a call handler template. To know languages installed on the
                                 		  server following URI can be used:

```
PUT https://<connection-server>/vmrest/installedlanguages
PUT https://<connection-server>/vmrest/callhandlertemplates<callhandlertemplate-objectid>
```

Example 1: The Inherit language field from the call is selected but
                                    			 the UseDefaultLanguage field is not updated

```
<CallhandlerTemplate>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseCallLanguage>false</UseCallLanguage>
</CallhandlerTemplate>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: The Inherit language field from the call is selected and
                                    			 the UseDefaultLanguage field is updated

```
Request Body:
<CallhandlerTemplate>
    <UseCallLanguage>true</UseCallLanguage>
    <UseDefaultLanguage>false</UseDefaultLanguage> 
    <Language>1033</Language>
</CallhandlerTemplate>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update language option of call handler template, do the follwoing:

```
Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "UseCallLanguage":"true",
    "UseDefaultLanguage":"false",
    "Language":"1033"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Updating Timezone
                           	 of a Call Handler Template

This PUT request can be used to update timezone for a call handler
                                 		  template. It can be set to default or particular timezone. The mandatory fields
                                 		  for this request are:

- UseDefaultTimeZone

- TimeZone

To know timzones installed on the server following URI can be used: https://<connection-server>/vmrest/timezones

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Request Body:
<CallhandlerTemplate>
    <UseDefaultTimeZone>false</UseDefaultTimeZone>
    <TimeZone>190</TimeZone>
</CallhandlerTemplate>
```

```
Response Code: 204
```

JSON Example

To update timezone of call handler template, do the following:

```
Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "UseDefaultTimeZone":"false",
    "TimeZone":"190"
}
```

```
Response Code: 204
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

### Explanation of
                           	 Data Fields

Default value:1

Possible Values Refer to the table 11 under the section Enum type as given at the end of document.

URI To fetch possible values of CallSearchspaceObjectId :https://<connection-server>//vmrest/searchspaces

Possible Values

- false:- specifies no dispatch delivery.

- true:- specifies dispatch delivery.

Default value is false

Possible Values

- false : Callers cannot edit messages

- true : Callers can edit messages

Default value is true.

Possible Values

- false:- System will not prepend digits when dialing the transfer extension

- true:- System will prepend digits when dialing the transfer extension

Default value is false

Possible Values:

- true:- Inherit from call.

- false:- Do not inherit from call.

Default value is true

Note:- Each subscriber is associated with a call handler, which is referred to as the "primary call handler" for that subscriber.
                                             An "application call handler" is just a normal call handler.

Possible Values:

- false: Not a primary call handler

- true: Primary call handler

Default value is false.

Possible Values:

- false: Not a template

- true: Is a template

Default value is true

Possible Values: Range 1-3600

default value is 300

URI To fetch MediaSwitchObjectId :https://<connection-server>/vmrest/phonesystems

If a key is "locked" then this value does not apply. Instead action is taken immediately on that key instead of allowing more
                                             digits. A value of 0 disables one key input.

Possible Values: Range:- 0 - 10000 Default value is1500

URI To fetch PartitionObjectId :https://<connection-server>/vmrest/partitions

Possible Values: Refer to the table 3 under the section Enum Type as given at the end of the document Default Value:1

URI To fetch its value :https://<connection-server>/vmrest/postgreetingrecordings from above URI get objectid.

Possible Values: Refer to the table 2 under the section Enum type as given at the end of document. Default value is 0

URI To fetch its value: https://<connection-server>/vmrest/postgreetingrecordings from above URI get objectid.

URI To fetch its value: https://<connection-server>/vmrest/ from above URI get objectid.

Possible Values: Refer to the table 4 under the section Enum type as given at the end of document. Default value is 0

Default value is false

Possible Values: Refer to the table 5 under the section Enum type as given at the end of document. Default value is 0(Never)

Example: 190 is the code for (GMT+05:30) Asia/Kolkata

Possible values:

- true

- false

Default value is true

Possible values:

- true

- false

Default value is false

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Enumeration Types

### Enumeration
                           	 Type

#### Call
                              	 Actions

#### Play Post Greeting
                              	 Recording

#### Play After Message
                              	 Recording

#### Send Private
                              	 Message

#### Send Urgent
                              	 Message

#### Play What

Name

Value

Description

SystemGreeting

0

Cisco Unity Connection plays a prerecorded greeting along with the recorded name of the subscriber (for example, "Sorry, <subscriber
                                                name> is not available"). If the subscriber does not have a recorded name, Cisco Unity Connection plays the subscriber extension
                                                instead. When a greeting is enabled but not recorded, Cisco Unity Connection plays a prerecorded system greeting.

Recorded Greeting

1

Use a personal recording for the call handler (or subscriber). This can be recorded over the phone or from the Cisco Unity
                                                Connection Administration and CPCA administrative interfaces on the call handler/subscriber.

NoGreeting

2

No greeting is played.

#### Transfer Rule
                              	 Action

#### Call Handler RNA
                              	 Action

#### Call Handler Hold
                              	 Mode

#### Transfer
                              	 Type

#### AfterMessageTargetConversation/ AfterGreetingTargetConversation/
                              	 TargetConversation

The
                                    		  AfterMessageTargetConversation/AfterGreetingTargetConversation/TargetConversation
                                    		  fields are read/write, and can take the following values. Although it is not an
                                    		  enumeration type, only certain string values are valid conversation names. For
                                    		  some conversations, it is required to specify their respective
                                    		  TargetHandlerObjectIds as well AfterMessageHandlerObjectid,
                                    		  AfterGreetingHandlerObjectId, and TargethandlerObjectId.

#### Greeting
                              	 Type

## Cisco Unity Connection Provisioning Interface (CUPI) API -- Greetings APIs

### Greetings
                           	 API

The following URI can be used to
                              		view the user template object ID:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

From the above URI, get the call handler object ID:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

The following URI can be used to view the greetings:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings
```

The following URI can be used to view the alternate greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Alternate
```

The following URI can be used to view the busy greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Busy
```

The following URI can be used to view the error greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Error
```

The following URI can be used to view the closed greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Off%20Hours
```

The following URI can be used to view the standard greeting:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Standard
```

The following URI can be used to view the holiday greeting:

```
GET https://<connection-server>/vmrest/callhandlers/<CallhandlerObjectId>/greetings/Holiday
```

#### Listing the Greetings

The following is an example of the GET request that fetch the list of greetings:

```
GET https://<connection-server>/vmrest/ callhandlertemplates/<callhandlertemplate-
  objectid>/templategreetings
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
<TemplateGreetings total="2">
  <TemplateGreeting>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templategreetings/Alternate</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <IgnoreDigits>false</IgnoreDigits>
    <PlayWhat>0</PlayWhat>
    <RepromptDelay>2</RepromptDelay>
    <Reprompts>0</Reprompts>
    <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
    <GreetingType>Alternate</GreetingType>
    <AfterGreetingAction>4</AfterGreetingAction>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
    <EnableTransfer>false</EnableTransfer>
  </TemplateGreeting>
  <TemplateGreeting>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templategreetings/Busy</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <IgnoreDigits>false</IgnoreDigits>
    <PlayWhat>0</PlayWhat>
    <RepromptDelay>2</RepromptDelay>
    <Reprompts>0</Reprompts>
    <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
    <GreetingType>Busy</GreetingType>
    <AfterGreetingAction>4</AfterGreetingAction>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
    <EnableTransfer>false</EnableTransfer>
  </TemplateGreeting>
</TemplateGreetings>
```

```
Response Code: 200
```

JSON Example

To view the list of greetings, do the following:

```
Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templategreetings
Accept: appliaction/json
Conenction: keep_alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
{
  "@total":"2"
  "TemplateGreeting": [
  {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templategreetings/Alternate"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "IgnoreDigits":"false"
    "PlayWhat":"0"
    "RepromptDelay":"2"
    "Reprompts":"0"
    "TimeExpires":"1972-01-01 00:00:00.0"
    "GreetingType":"Alternate"
    "AfterGreetingAction":"4"
    "PlayRecordMessagePrompt":"true"
    "EnableTransfer":"false"
  },
  {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templategreetings/Busy"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "IgnoreDigits":"false"
    "PlayWhat":"0"
    "RepromptDelay":"2"
    "Reprompts":"0"
    "TimeExpires":"1972-01-01 00:00:00.0"
    "GreetingType":"Busy"
    "AfterGreetingAction":"4"
    "PlayRecordMessagePrompt":"true"
    "EnableTransfer":"false"
  },
  ]
}
```

```
Response Code: 200
```

#### Viewing the
                              	 Details of Specific Greeting

The following is an example of
                                    		  the GET request that lists the details of specific greeting:

```
GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
  objectid>/templategreetings/<Greetingname>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<TemplateGreeting>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
836910ac1a4c/templategreetings/Alternate</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
836910ac1a4c</CallhandlerURI>
    <IgnoreDigits>false</IgnoreDigits>
    <PlayWhat>0</PlayWhat>
    <RepromptDelay>2</RepromptDelay>
    <Reprompts>0</Reprompts>
    <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
    <GreetingType>Alternate</GreetingType>
    <AfterGreetingAction>4</AfterGreetingAction>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
    <EnableTransfer>false</EnableTransfer>
</TemplateGreeting>
```

```
Response Code: 200
```

JSON Example

To view a specific greeting, do the following:

```
Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<Callhandlertemplate-objectid>/templategreetings/<Greetingname>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templategreetings/Alternate"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "IgnoreDigits":"false"
    "PlayWhat":"0"
    "RepromptDelay":"2"
    "Reprompts":"0"
    "TimeExpires":"1972-01-01 00:00:00.0"
    "GreetingType":"Alternate"
    "AfterGreetingAction":"4"
    "PlayRecordMessagePrompt":"true"
    "EnableTransfer":"false"
}
```

```
Response Code: 200
```

#### Updating a
                              	 Greeting

The following is an example of
                                    		  the GET request that updates the details of specific greeting:

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templategreetings/<Greetingname>
Response Body:
<TemplateGreeting>
    <PlayWhat>1</PlayWhat>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
</TemplateGreeting>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update a particular greeting, do the following:

```
Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<Callhandlertemplate-objectid>/templategreetings/<Greetingname>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "PlayWhat":"1",
    "PlayRecordMessagePrompt":"true"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

This column overrides all the Menu Entry settings when this
                                                   						greeting is active. This has the same effect as setting all the menu entry keys
                                                   						for this handler to "locked". It is a shorthand way of locking callers into the
                                                   						greeting so they cannot get out until it completes. Possible values:

- false: Caller
                                                         						  input enabled during greeting

- true: Caller
                                                         						  input ignored during greeting

Default Value: false

Refer to the section Enumeration Type.<<Link will be
                                                   						mentioned later>> Default Value: 0

Possible values:

- 0: Do wait
                                                         						  without receiving caller input and do not replay greeting.

- 1 or greater:
                                                         						  Wait this number of seconds without receiving any input from the caller before
                                                         						  playing the greeting again.

Default Value: 2

This column is typically used when an audio text application
                                                   						is expecting input from a caller. The range of this field can vary from 0 to
                                                   						100. Possible values:

- 0: Do not
                                                         						  re-prompt - Cisco Unity Connection will play the greeting once and then the
                                                         						  after-greeting action is taken.

- 1 or greater:
                                                         						  Number of times to re-prompt.

The "RepromptDelay" value determines how many seconds to
                                                   						wait in between replays. Default Value: 0

Default value: Standard

Refer to the section Enumeration Type.<<Link will be
                                                   						mentioned later>> Default value: 4

Refer to the section Enumeration Type.<<Link will be
                                                   						mentioned later>

The "Enhanced Alternate Greeting" feature uses this column
                                                   						to specify how long the subscriber wants their alternate greeting enabled. The
                                                   						standard greeting rule should never be disabled. The field is not displayed
                                                   						when the Greeting field is enabled with no end date and end time.

Values:

- true - Play
                                                         						  Record Message prompt is enabled.

- false - Play
                                                         						  Record prompt is disabled.

Default Value: true

Values:

- true: Allows
                                                         						  transfer

- false: Does not
                                                         						  allow

Default Value: false

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Message Settings APIs

### Message Settings
                           	 APIs

Administrator can use this API to
                                 		  fetch the message settings.

#### Updating a Message
                              	 Setting

The following is an example of
                                    		  the PUT request that updates the message settings:

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandler-objectid>
Request Body:
<CallhandlerTemplate>
    <AfterMessageAction>2</AfterMessageAction>
    <AfterMessageTargetConversation>SystemTransfer</AfterMessageTargetConversation>
</CallhandlerTemplate>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update message setting, do the following:

```
Request URI:
PUT:  https://<connection-server>/vmrest/callhandlertemplates/<calhandler-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
"AfterMessageAction":"2",
"AfterMessageTargetConversation":"SystemTransfer"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Post Greeting Recordings APIs

### Post Greeting
                           	 Recordings APIs

Administrator can use this API to
                                 		  fetch the post greeting recordings. It can be used to fetch the list of post
                                 		  greeting recordings and also a single instance of post greeting recordings.

#### Updating a Post
                              	 Greeting Recordings

The following is an example of
                                    		  the PUT request that updates the post greeting recordings:

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Request Body:
<CallhandlerTemplate>
    <PlayPostGreetingRecording>2</PlayPostGreetingRecording>
    <PostGreetingRecordingObjectId>0c6ab589-f289-4d4b-b3b7-
e4ec96bb783e</PostGreetingRecordingObjectId>
</CallhandlerTemplate>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update post greeting recordings, do the following:

```
Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: applicaiton/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
"PlayPostGreetingRecording":"1",
"PostGreetingRecordingObjectId":"0c6ab589-f289-4d4b-b3b7-e4ec96bb783e"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Transfer Rule APIs

### TransferRulesAPIs

Administrator can use this API to
                                 		  fetch the transfer rules. It can be used to fetch the list of transfer rules
                                 		  and also a single instance of transfer rules.

#### Listing the
                              	 Transfer Rules

The following is an example of
                                    		  the GET request that fetch the list of transfer rules:

```
GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
  objectid>/templatetransferoptions
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<TemplateTransferOptions total="2">
  <TemplateTransferOption>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templatetransferoptions/Alternate</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <TransferOptionType>Alternate</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
  </TemplateTransferOption>
  <TemplateTransferOption>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templatetransferoptions/Off Hours</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <TransferOptionType>Off Hours</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
  </TemplateTransferOption>
</TemplateTransferOptions>
```

```
Response Code: 200
```

JSON Example

To list the transfer rules, do the following:

```
Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templatetransferoptions
Accept: application/json
Connection: keep_alive
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
{
  "@total":"2"
  "TemplateTransferOption":   [
  {
    "URI":"/vmrest/callhandlertemplates/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7/templatetransferoptions/Alternate"
    "CallHandlerObjectId":"e07ee639-bf8a-4c37-9d6a-0b51beee65c7"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7"
    "TransferOptionType":"Alternate"
    "Action":"0"
    "RnaAction":"1"
    "TransferAnnounce":"false"
    "TransferConfirm":"false"
    "TransferDtDetect":"false"
    "TransferHoldingMode":"0"
    "TransferIntroduce":"false"
    "TransferRings":"4"
    "TransferScreening":"false"
    "TransferType":"1"
    "MediaSwitchObjectId":"f92e948f-6bd4-4891-ab8b-a3d930688305"
    "PhoneSystemURI":"/vmrest/phonesystems/f92e948f-6bd4-4891-ab8b-a3d930688305"
    "UsePrimaryExtension":"true"
    "PlayTransferPrompt":"true"
    "PersonalCallTransfer":"false"
    "Enabled":"true"
  },
  {
    "URI":"/vmrest/callhandlertemplates/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7/templatetransferoptions/Off Hours"
    "CallHandlerObjectId":"e07ee639-bf8a-4c37-9d6a-0b51beee65c7"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7"
    "TransferOptionType":"Off Hours"
    "Action":"0"
    "RnaAction":"1"
    "TransferAnnounce":"false"
    "TransferConfirm":"false"
    "TransferDtDetect":"false"
    "TransferHoldingMode":"0"
    "TransferIntroduce":"false"
    "TransferRings":"4"
    "TransferScreening":"false"
    "TransferType":"0"
    "MediaSwitchObjectId":"f92e948f-6bd4-4891-ab8b-a3d930688305"
    "PhoneSystemURI":"/vmrest/phonesystems/f92e948f-6bd4-4891-ab8b-a3d930688305"
    "UsePrimaryExtension":"true"
    "PlayTransferPrompt":"true"
    "PersonalCallTransfer":"false"
    "Enabled":"true"
  }
  ]
}
```

```
Response Code: 200
```

#### Viewing the
                              	 Details of Specific Transfer Rule

The following is an example of
                                    		  the GET request that lists the details of specific transfer rule:

```
GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
  objectId>/templatetransferoptions/<TransferOptionType>
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
<TemplateTransferOption>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
836910ac1a4c/templatetransferoptions/Alternate</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
836910ac1a4c</CallhandlerURI>
    <TransferOptionType>Alternate</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
d3b13f5040f5</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
</TemplateTransferOption>
```

```
Response Code: 200
```

JSON Example

To view the details of a specific transfer rule, do the following:

```
Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<Callhandlertemplate-
objectid>/templatetransferoptions/<TransferOptionType>
Accept: applciation/json
Connection: keep_alive
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
{
    "URI":"/vmrest/callhandlertemplates/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7/templatetransferoptions/Alternate"
    "CallHandlerObjectId":"e07ee639-bf8a-4c37-9d6a-0b51beee65c7"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7"
    "TransferOptionType":"Alternate"
    "Action":"0"
    "RnaAction":"1"
    "TransferAnnounce":"false"
    "TransferConfirm":"false"
    "TransferDtDetect":"false"
    "TransferHoldingMode":"0"
    "TransferIntroduce":"false"
    "TransferRings":"4"
    "TransferScreening":"false"
    "TransferType":"1"
    "MediaSwitchObjectId":"f92e948f-6bd4-4891-ab8b-a3d930688305"
    "PhoneSystemURI":"/vmrest/phonesystems/f92e948f-6bd4-4891-ab8b-a3d930688305"
    "UsePrimaryExtension":"true"
    "PlayTransferPrompt":"true"
    "PersonalCallTransfer":"false"
    "Enabled":"true"
}
```

```
Response Code: 200
```

#### Updating a
                              	 Transfer Rule

The following is an example of
                                    		  the PUT request that updates a transfer rule:

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
objectid>/templatetransferoptions/<TransferOptionType>
Request Body: 
<TemplateTransferOption>
    <Action>1</Action>
    <Extension>1000</Extension>
    <TimeExpires>2012-12-31 12:00:00.0</TimeExpires>
    <Enabled>true</Enabled>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <TransferAnnounce>true</TransferAnnounce>
    <TransferConfirm>true</TransferConfirm>
    <TransferIntroduce>true</TransferIntroduce>
    <TransferScreening>true</TransferScreening>
    <TransferType>1</TransferType>
</TemplateTransferOption>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update a particular transfer rule, do the following:

```
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
objectid>/templatetransferoptions/<TransferOptionType>
Accept: applciation/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Action":"1",
    "TimeExpires":"2012-12-31 12:00:00.0",
    "Extension":"1002",
    "PlayTransferPrompt":"true",
    "TransferAnnounce":"true",
    "TransferConfirm":"true"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

- Alternate - in effect at all times, overrides standard and offhours.

- OffHours - off or closed hours based on specified schedule.

- Standard - standard hours based on specified schedule.

Refer to the section Enumeration Type.<<Link will be mentioned later>> Default value: 0

Refer to the section Enumeration Type.<<Link will be mentioned later>>

The "Standard" transfer option should never be disabled. For primary call handlers associated with subscribers, the "Alternate"
                                                transfer option should always be enabled since subscribers have only one transfer option used currently.

Values can be:

- false: Do not say "Transferring call" when the subscriber answers the phone

- true: Say "Transferring call" when the subscriber answers the phone

Default value: false

Requires a "TransferType" of supervised.

- Unsupervised transfer (also referred to as "Release to Switch" transfer) - Cisco Unity Connection puts the caller on hold,
                                                      dials the extension, and releases the call to the phone system. When the line is busy or is not answered, the phone system
                                                      (not Cisco Unity Connection) forwards the call to the subscriber or handler greeting. To use "Unsupervised" transfer, call
                                                      forwarding must be enabled on the phone system

- Supervised transfer - Cisco Unity Connection acts as a receptionist, handling the transfer. If the line is busy or the call
                                                      is not answered, Cisco Unity Connection (not the phone system) forwards the call to the subscriber or handler greeting. Supervised
                                                      transfer can be used regardless if the phone system forwards calls or not.

Typically TransferConfirm is used in conjunction with the call screening option ("TransferScreening" column) enabled. This
                                                combination enables the subscriber to hear the name of the caller and then decide if they want to take the call or not. Default
                                                Value: false. Values can be:

- false: Transfer confirm disabled

- true: Transfer confirm enabled

Default value: false

This is usually used for phone systems that do not have "positive disconnect" capabilities to avoid sending terminated calls
                                                to the operator console, for instance. Possible values can be:

- false: Do not check for dial tone prior to transferring a call

- true: Check for dial tone prior to transferring a call

Default value:false

Requires a TransferType column value = "Supervised" (1). Default Value: 0

Requires a "TransferType" of supervised (1). This functionality is normally used when a single extension number is being shared
                                                by multiple subscribers or a scenario where the subscriber who is the message recipient takes calls for more than one dialed
                                                extension. The introduction alerts the subscriber who answers that the call is for the call handler. Default Value: false.

Requires a "TransferType" of supervised (1). The value of this column should never be less than 2 for a supervised transfer.
                                                The range can vary from 2 to 20. Default Value: 4

Requires a "TransferType" of supervised (1). Normally this column is used along with "TransferConfirm" to allow the subscriber
                                                to screen calls. Values can be:

- false: Call screening disabled

- true: Ask and record caller name

Default Value: false

- Unsupervised transfer (also referred to as "Release to Switch" transfer) - Cisco Unity Connection puts the caller on hold,
                                                      dials the extension, and releases the call to the phone system. When the line is busy or is not answered, the phone system
                                                      (not Cisco Unity Connection) forwards the call to the subscriber or handler greeting. To use "Unsupervised" transfer, call
                                                      forwarding must be enabled on the phone system.

- Supervised transfer - Cisco Unity Connection acts as a receptionist, handling the transfer. If the line is busy or the call
                                                      is not answered, Cisco Unity Connection (not the phone system) forwards the call to the subscriber or handler greeting. Supervised
                                                      transfer can be used regardless if the phone system forwards calls or not.

Default value: 0

Possible Values:

- false

- true

Default value: true

Note - Digits, hash, comma, asterisk, plus are allowed.

Values can be:

- true - Play Transfer prompt is enabled.

- false - Play transfer prompt is disabled.

Default Value: true

Values can be:

- false: Not enabled

- true: Enabled

Default value: false

Possible value:

- true: enabled

- false: disabled

Default value: true This means transfer rules are enabled with no end date by default.

| GET https://<connection-server>/vmrest/ callhandlertemplates/<callhandlertemplate-
  objectid>/templatemenuentries |
|---|

| <TemplateMenuEntries total="2">
  <TemplateMenuEntry>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templatemenuentries/*</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <TouchtoneKey>*</TouchtoneKey>
    <Locked>false</Locked>
    <Action>4</Action>
    <ObjectId>de3dce46-1887-489c-9244-ae8b421fe107</ObjectId>
  </TemplateMenuEntry>
  <TemplateMenuEntry>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templatemenuentries/#</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <TouchtoneKey>#</TouchtoneKey>
    <Locked>false</Locked>
    <Action>5</Action>
    <ObjectId>17ec06a9-6990-4a95-8417-6e22957fcbe5</ObjectId>
  </TemplateMenuEntry>
</TemplateMenuEntries> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templatemenuentries
Accept: application/json
Connection: keep_alive |
|---|

| {
  "@total":"2"
  "TemplateMenuEntry":    
  {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templatemenuentries/*"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "TouchtoneKey":"*"
    "Locked":"true"
    "Action":"2"
    "TargetConversation":"SubSignIn"
    "ObjectId":"17184311-90ac-4654-8e26-cfbe08138851"
  },
  {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a/templatemenuentries/#"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "TouchtoneKey":"#"
    "Locked":"true"
    "Action":"5"
    "ObjectId":"27eb298c-22a1-4ed7-813b-61c144bc0fdc"
  },
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
  objectid>/templatemenuentries/<TouchToneKey> |
|---|

| <TemplateMenuEntry>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
836910ac1a4c/templatemenuentries/5</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
836910ac1a4c</CallhandlerURI>
    <TouchtoneKey>5</TouchtoneKey>
    <Locked>false</Locked>
    <Action>0</Action>
    <ObjectId>f076155c-80b1-4538-bcc7-c901a6eafbae</ObjectId>
</TemplateMenuEntry> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templatemenuentries/<TouchToneKey>
Accept: application/json
Connection: keep_alive |
|---|

| {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templatemenuentries/*"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "TouchtoneKey":"*"
    "Locked":"true"
    "Action":"2"
    "TargetConversation":"SubSignIn"
    "ObjectId":"17184311-90ac-4654-8e26-cfbe08138851"
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
objectid>/templatemenuentries/<TouchToneKey> |
|---|

| <TemplateMenuEntry>
    <Action>7</Action>
    <TransferNumber>1000</TransferNumber>
    <TransferType> 1</TransferType>
    <TransferRings>2</TransferRings>
</TemplateMenuEntry> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templatemenuentries/<TouchToneKey>
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | URI of the call handler menu entries. |
| CallHadlerObjectId | Read Only | String | A transfer rule can belong only to a call
                                                					 handler object. No other object can own a menu entry. |
| CallHandlerURI | Read Only | String | URI of the call handler that is being
                                                					 referenced. |
| TouchtoneKey | Read Only | String | The character on the touch-tone keypad that
                                                					 this menu entry corresponds to (*, #, 0,1...9). |
| Locked | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                                					 Connection ignores additional input after callers press this key. A locked menu entry does not allow additional dialing after
                                                   						this choice is entered, but Cisco Unity Connection will immediately take the
                                                   						associated action. If the action is set to "Ignore" (0), the key is thrown out
                                                   						and the greeting continues playing as normal. Any other action is taken
                                                   						immediately without waiting to determine if the caller is going to dial an
                                                   						extension. Possible Values: false: Unlocked
                                                         						  - Additional dialing after this choice is entered is allowed true: Locked -
                                                         						  Additional dialing is ignored Default value: false |
| Action | Read/Write | Integer | Specifies the action to be taken in the
                                                					 event of the key press. Default value: 0 |
| TargetConversion | Read/Write | String | Specifies the conversation to go to after
                                                					 taking a message. Default value: 0 |
| TargetHandlerObjectId | Read/Write | String | The unique identifier of the specific
                                                					 object to send along to the target conversation. |
| ObjectId | Read Only | String | Object ID of the caller input. |
| TransferNumber | Read/Write | Integer | The phone number associated with the
                                                					 alternate contact. |
| DisplayName | Read/Write | String | The display name associated with the
                                                					 alternate contact number. |
| TransferType | Read/Write | Integer | The type of call transfer Cisco Unity
                                                					 Connection will perform - supervised or unsupervised (also referred to as
                                                					 "Release to Switch" transfer). Default value: 0 |
| TransferRings | Read/Write | Integer | The number of times the extension rings
                                                					 before Cisco Unity Connection considers it a "ring no answer" and plays the
                                                					 subscriber or handler greeting Possible value can range from 2-20 Default Value: 4 |

| GET https://<connection-server>/vmrest/callhandlertemplates |
|---|

| <CallhandlerTemplates total="1">
  <CallhandlerTemplate>
    <URI>/vmrest/callhandlertemplates/5024347a-aac2-463a-98c8-a745a805dc3b</URI>
    <CreationTime>2013-01-10T09:23:20Z</CreationTime>
    <Language>1033</Language>
    <DisplayName>System Call Handler Template1</DisplayName>
    <UseDefaultLanguage>false</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Undeletable>true</Undeletable>
    <LocationObjectId>22646a82-1f17-4b42-beec-9cdfd69508c5</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/22646a82-1f17-4b42-beec-
    9cdfd69508c5</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <MaxMsgLen>300</MaxMsgLen>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>10fee566-b137-4652-a378-
    db8a872a161d</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/10fee566-b137-4652-a378-
    db8a872a161d</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <IsTemplate>true</IsTemplate>
    <ObjectId>5024347a-aac2-463a-98c8-a745a805dc3b</ObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <RecipientDistributionListObjectId>f7408e6e-822e-494b-ab29-
    cff3cf9e0bd9</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/f7408e6e-822e-494b-ab29-
    cff3cf9e0bd9</RecipientDistributionListURI>
    <AfterMessageAction>2</AfterMessageAction>
    <AfterMessageTargetConversation>PHGreeting</AfterMessageTargetConversation>
    <AfterMessageTargetHandlerObjectId>16cf736f-7254-4654-ab09-
    08fe743332a9</AfterMessageTargetHandlerObjectId>
    <TimeZone>190</TimeZone>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</PhoneSystemURI>
    <UseCallLanguage>false</UseCallLanguage>
    <SendSecureMsg>false</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>f3beb4e4-0be5-417f-9491-
    e233c6d4a40e</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/f3beb4e4-0be5-417f-9491-
    e233c6d4a40e</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>5ec15c45-ace9-41ad-a6c4-b56081c79717</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/5ec15c45-ace9-41ad-a6c4-
    b56081c79717</PartitionURI>
    <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
    <SendPrivateMsg>0</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/callhandlertemplates/5024347a-aac2-463a-98c8-
    a745a805dc3b/templategreetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/callhandlertemplates/5024347a-aac2-463a-98c8-
    a745a805dc3b/templatetransferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/callhandlertemplates/5024347a-aac2-463a-98c8-
    a745a805dc3b/templatemenuentries</MenuEntriesURI>
  </CallhandlerTemplate>
</CallhandlerTemplates> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates
Accept: application/json
Connection: keep_alive |
|---|

| {
  "@total":"1"
  "CallhandlerTemplate":  [
  {
    "URI":"/vmrest/callhandlertemplates/7a022382-8d0a-4289-880d-d2a432494b02"
    "CreationTime":"2013-02-25T09:39:23Z"
    "Language":"1033"
    "DisplayName":"System Call Handler Template"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"true"
    "Undeletable":"true"
    "LocationObjectId":"cff1347e-87af-4409-bead-d1970625f82e"
    "LocationURI":"/vmrest/locations/connectionlocations/cff1347e-87af-4409-bead-
    d1970625f82e"
    "EditMsg":"true"
    "IsPrimary":"false"
    "MaxMsgLen":"300"
    "OneKeyDelay":"1500"
    "ScheduleSetObjectId":"5fc5a5d7-eaf6-4f4d-80cf-f76f3893ac0e"
    "ScheduleSetURI":"/vmrest/schedulesets/5fc5a5d7-eaf6-4f4d-80cf-f76f3893ac0e"
    "SendUrgentMsg":"0"
    "IsTemplate":"true"
    "ObjectId":"7a022382-8d0a-4289-880d-d2a432494b02"
    "TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438",
    "RecipientDistributionListObjectId":"dea18b5b-4493-4715-a558-cb85778fd823"
    "RecipientDistributionListURI":"/vmrest/distributionlists/dea18b5b-4493-4715-a558-
    cb85778fd823"
    "AfterMessageAction":"2"
    "AfterMessageTargetConversation":"PHGreeting"
    "AfterMessageTargetHandlerObjectId":"c6af281b-dc8b-45b4-a1e9-eccc523d5fb2"
    "TimeZone":"190"
    "MediaSwitchObjectId":"0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "PhoneSystemURI":"/vmrest/phonesystems/0ad0b88c-4a70-4cf7-913e-d5d7a921caca"
    "UseCallLanguage":"true"
    "SendSecureMsg":"false"
    "EnablePrependDigits":"false"
    "DispatchDelivery":"false"
    "CallSearchSpaceObjectId":"2e836e16-f715-4a18-bb7c-ee5e33281706"
    "CallSearchSpaceURI":"/vmrest/searchspaces/2e836e16-f715-4a18-bb7c-
    ee5e33281706"
    "InheritSearchSpaceFromCall":"true"
    "PartitionObjectId":"97bf6afe-346e-4275-967e-43c50be79d32"
    "PartitionURI":"/vmrest/partitions/97bf6afe-346e-4275-967e-43c50be79d32"
    "PlayPostGreetingRecording":"0"
    "SendPrivateMsg":"0"
    "PlayAfterMessage":"1"
    "GreetingsURI":"/vmrest/callhandlertemplates/7a022382-8d0a-4289-880d-
    d2a432494b02/templategreetings"
    "TransferOptionsURI":"/vmrest/callhandlertemplates/7a022382-8d0a-4289-880d-
    d2a432494b02/templatetransferoptions"
    "MenuEntriesURI":"/vmrest/callhandlertemplates/7a022382-8d0a-4289-880d-
    d2a432494b02/templatemenuentries"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/callhandlertemplates?query=(TenantObjectId is <Tenant-ObjectId>) |
|---|

| GET https://<connection-server>/vmrest/tenants |
|---|

| GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid> |
|---|

| <CallhandlerTemplate>
    <URI>/vmrest/callhandlertemplates/edcd2336-2c01-49d1-89ff-8746466e0a5e</URI>
    <CreationTime>2013-01-12T11:40:19Z</CreationTime>
    <Language>1033</Language>
    <DisplayName>CallHandler1</DisplayName>
    <UseDefaultLanguage>false</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <Undeletable>false</Undeletable>
    <LocationObjectId>22646a82-1f17-4b42-beec-9cdfd69508c5</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/22646a82-1f17-4b42-beec-
    9cdfd69508c5</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <MaxMsgLen>300</MaxMsgLen>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>10fee566-b137-4652-a378-db8a872a161d</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/10fee566-b137-4652-a378-
    db8a872a161d</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <IsTemplate>true</IsTemplate>
    <ObjectId>edcd2336-2c01-49d1-89ff-8746466e0a5e</ObjectId>
    <RecipientSubscriberObjectId>f74c4f98-598e-4c47-bf1a-
    2b78fc2c2953</RecipientSubscriberObjectId>
    <RecipientUserURI>/vmrest/users/f74c4f98-598e-4c47-bf1a-2b78fc2c2953</RecipientUserURI>
    <AfterMessageAction>1</AfterMessageAction>
    <TimeZone>190</TimeZone>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</PhoneSystemURI>
    <UseCallLanguage>false</UseCallLanguage>
    <SendSecureMsg>false</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>f3beb4e4-0be5-417f-9491-e233c6d4a40e</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/f3beb4e4-0be5-417f-9491-
    e233c6d4a40e</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>5ec15c45-ace9-41ad-a6c4-b56081c79717</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/5ec15c45-ace9-41ad-a6c4-b56081c79717</PartitionURI>
    <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
    <SendPrivateMsg>0</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/callhandlertemplates/edcd2336-2c01-49d1-89ff-
    8746466e0a5e/templategreetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/callhandlertemplates/edcd2336-2c01-49d1-89ff-
    8746466e0a5e/templatetransferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/callhandlertemplates/edcd2336-2c01-49d1-89ff-
    8746466e0a5e/templatemenuentries</MenuEntriesURI>
</CallhandlerTemplate> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Connection: keep_alive |
|---|

| {
    "URI":"/vmrest/callhandlertemplates/93b8ada5-c92f-47e6-8d24-9c269293d63c"
    "CreationTime":"2013-02-26T06:45:09Z"
    "Language":"1033"
    "DisplayName":"Call_Handler1"
    "UseDefaultLanguage":"true"
    "UseDefaultTimeZone":"false"
    "Undeletable":"false"
    "LocationObjectId":"cff1347e-87af-4409-bead-d1970625f82e"
    "LocationURI":"/vmrest/locations/connectionlocations/cff1347e-87af-4409-bead-
    d1970625f82e"
    "EditMsg":"true"
    "IsPrimary":"false"
    "MaxMsgLen":"500"
    "OneKeyDelay":"1500"
    "ScheduleSetObjectId":"5c42abd2-84a5-4fcf-84cf-d0a19c70f207"
    "ScheduleSetURI":"/vmrest/schedulesets/5c42abd2-84a5-4fcf-84cf-d0a19c70f207"
    "SendUrgentMsg":"1"
    "IsTemplate":"true"
    "ObjectId":"93b8ada5-c92f-47e6-8d24-9c269293d63c"
    "RecipientDistributionListObjectId":"8337a757-b074-42ff-85bd-acda2dfd5d28"
    "RecipientDistributionListURI":"/vmrest/distributionlists/8337a757-b074-42ff-85bd-
    acda2dfd5d28"
    "AfterMessageAction":"2"
    "AfterMessageTargetConversation":"AD"
    "AfterMessageTargetHandlerObjectId":"4783cb28-79a6-409a-bf57-18f8208b4e61"
    "TimeZone":"190"
    "MediaSwitchObjectId":"343dc222-2d1a-4a19-a5b6-894725542475"
    "PhoneSystemURI":"/vmrest/phonesystems/343dc222-2d1a-4a19-a5b6-894725542475"
    "UseCallLanguage":"true"
    "SendSecureMsg":"false"
    "EnablePrependDigits":"false"
    "DispatchDelivery":"true"
    "CallSearchSpaceObjectId":"2e836e16-f715-4a18-bb7c-ee5e33281706"
    "CallSearchSpaceURI":"/vmrest/searchspaces/2e836e16-f715-4a18-bb7c-ee5e33281706"
    "InheritSearchSpaceFromCall":"true"
    "PartitionObjectId":"44bdcf73-d5c1-4866-957d-fb35686cbe76"
    "PartitionURI":"/vmrest/partitions/44bdcf73-d5c1-4866-957d-fb35686cbe76"
    "PlayPostGreetingRecording":"2"
    "SendPrivateMsg":"0"
    "PlayAfterMessage":"2"
    "GreetingsURI":"/vmrest/callhandlertemplates/93b8ada5-c92f-47e6-8d24-
    9c269293d63c/templategreetings"
    "TransferOptionsURI":"/vmrest/callhandlertemplates/93b8ada5-c92f-47e6-8d24-
    9c269293d63c/templatetransferoptions"
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/callhandlertemplates
Request Body:
  <CallhandlerTemplate>
    <DisplayName>System Call Handler Template1</DisplayName>
    <RecipientSubscriberObjectId>f74c4f98-598e-4c47-bf1a-
    2b78fc2c2953</RecipientSubscriberObjectId>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-d3b13f5040f5</MediaSwitchObjectId>
  </CallhandlerTemplate> |
|---|

| Response Code: 201 |
|---|

| Request URI:
POST: https://<connection-server>/vmrest/callhandlertemplates
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
"DisplayName":"Tenant",
"RecipientDistributionListObjectId":"8337a757-b074-42ff-85bd-acda2dfd5d28",
"MediaSwitchObjectId":"343dc222-2d1a-4a19-a5b6-894725542475"
} |
|---|

| Response Code: 201 |
|---|

| DELETE https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid> |
|---|

| Response Code: 204 |
|---|

| Request URI:
DELETE: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
The ScheduleSetObjectId can be fetched using the URI https://<connection-server>/vmrest/schedulesets. |
|---|

| <CallhandlerTemplate>
    <ScheduleSetObjectId>eb11c6cc-fc9e-4651-8c01-8f0b2e421918</ScheduleSetObjectId>
</CallhandlerTemplate> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| {
    "ScheduleSetObjectId":"5c42abd2-84a5-4fcf-84cf-d0a19c70f207"
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid> |
|---|

| <CallhandlerTemplate>
    <PartitionObjectId>46a0377b-00d7-40a0-8738-81106fc730ea</PartitionObjectId>
</CallhandlerTemplate> |
|---|

| Response Code: 204 |
|---|

| <pre>
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
</pre> |
|---|

| {
"PartitionObjectId":"fe2fe907-bdcb-416e-89b7-c1bb130d0f98"
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/installedlanguages
PUT https://<connection-server>/vmrest/callhandlertemplates<callhandlertemplate-objectid> |
|---|

| <CallhandlerTemplate>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseCallLanguage>false</UseCallLanguage>
</CallhandlerTemplate> |
|---|

| Response Code: 204 |
|---|

| Note | The Inherit Language field from the call is selected but this the UseDefaultLanguage field is not updated in the database
                                          as the language field is missing as the Language field is NULL and UseDefaultLanguage is by default set to TRUE. |
|---|---|

| Request Body:
<CallhandlerTemplate>
    <UseCallLanguage>true</UseCallLanguage>
    <UseDefaultLanguage>false</UseDefaultLanguage> 
    <Language>1033</Language>
</CallhandlerTemplate> |
|---|

| Response Code: 204 |
|---|

| Note | The Inherit Language field from the call is selected but the UseDefaultLanguage field is updated in the database as the Language
                                          field is specified. The Inherit Language field from the call is selected but the UseDefaultLanguage field is updated in the
                                          database as the Language field is specified. Language code for installed language can be fetched from: https://<connection-server>/vmrest/installedlanguages
                                          Language code can be fetched from the URI: https://<connection-server>/vmrest/languagemap The below table specify the details
                                          of value for each field: |
|---|---|

| UseCallLanguage | UseDefaultLanguage | Language | Description |
|---|---|---|---|
| false | true | Null/Language Code | This will select the default language. |
| true | true/false | Null/Language Code | This will inherit the language from user. |
| false | false | Language Code | This will select the particular language as per the code. |

| Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "UseCallLanguage":"true",
    "UseDefaultLanguage":"false",
    "Language":"1033"
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Request Body:
<CallhandlerTemplate>
    <UseDefaultTimeZone>false</UseDefaultTimeZone>
    <TimeZone>190</TimeZone>
</CallhandlerTemplate> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "UseDefaultTimeZone":"false",
    "TimeZone":"190"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | Call Handler Template URI |
| AfterMessageAction | Read/Write | Integer | Specifies the after message action.Possible Values Refer to the table 1 under the section Enum Type as given at the end of
                                          the document Default value:1 |
| AfterMessageTargetConversation | Read/Write | String | Specifies DisplayName of the conversation to go to after taking a message. Possible Values Refer to the table 11 under the section Enum type as given at the end of document. |
| AfterMessageTargetHandlerObjectId | Read/Write | String(36) | The Unique Identifier of the call action object that Cisco Unity Connection performs after taking a message. |
| CallSearchspaceObjectId | Read/Write | String(36) | Is present only if a search space is selected. URI To fetch possible values of CallSearchspaceObjectId :https://<connection-server>//vmrest/searchspaces |
| CallSearchSpaceURI | Read Only | String | URL for search spaces |
| CreationTime | Read Only | Datetime | Specifies the creation date and time of the call handler. Format: YYYY-MM-DDThh:mm:ssZ. The default value is the current system
                                          date and time |
| DispatchDelivery | Read/Write | Boolean | A flag indicating that all messages left for the call handler is for dispatch delivery. Possible Values false:- specifies no dispatch delivery. true:- specifies dispatch delivery. Default value is false |
| DisplayName | Read/Write | String(64) | Name of the Call Handler Template |
| EditMsg | Read/Write | Boolean | A flag that determines whether the caller can edit messages. Possible Values false : Callers cannot edit messages true : Callers can edit messages Default value is true. |
| EnablePrependDigits | Read/Write | Boolean | Specifies if Prepend Digits to Dialed Extensions is enabled. Possible Values false:- System will not prepend digits when dialing the transfer extension true:- System will prepend digits when dialing the transfer extension Default value is false |
| InheritSeachSpaceFromCall | Read/Write | Boolean | Specifies if the search space is to be inherited from the call. Possible Values: true:- Inherit from call. false:- Do not inherit from call. Default value is true |
| IsPrimary | Read Only | Boolean | A flag indicating whether this is a "primary" call handler for a subscriber, or an "application" call handler. Note:- Each subscriber is associated with a call handler, which is referred to as the "primary call handler" for that subscriber.
                                             An "application call handler" is just a normal call handler. Possible Values: false: Not a primary call handler true: Primary call handler Default value is false. |
| IsTemplate | Read Only | Boolean | Used to provide default values for selected columns when creating new call handlers. Possible Values: false: Not a template true: Is a template Default value is true |
| Language | Read/Write | Integer | The Windows Locale ID (LCID) which identifies the language that Cisco Unity Connection plays the handler system prompts. |
| LocationObjectId | Read Only | String(36) | The unique identifier of the Location object to which this handler belongs. |
| LocationURI | Read Only | String | Specifies the URI of locations |
| MaxMsgLen | Read/Write | Integer | The maximum recording length (in seconds) for messages left by unidentified callers. This value is used when the call handler
                                          is set to an action of "Take Message" (either by an after greeting action in the messagingrule table or via a user input action
                                          in the menuentry table. This value only gets applied to unidentified callers leaving a message. This value is not used for
                                          subscriber-subscriber messaging. Instead the COS for the calling subscriber determines the maximum recorded message length. Possible Values: Range 1-3600 default value is 300 |
| MediaSwitchObjectId | Read/Write | String(36) | Specifies the object Id of the Phone System the call handler belongs to. URI To fetch MediaSwitchObjectId :https://<connection-server>/vmrest/phonesystems |
| PhoneSystemURI | Read Only | String | Specifies the URI of Phone Systems |
| ObjectId | Read Only | String(36) | Object Id of the Call Handler Template. |
| TenantObjectId | Read Only | String(36) | The unique identifier of the tenant to which the call handler templates belong. This field is reflected in the response only
                                          if the call handler template belong to a particular tenant. |
| OneKeyDelay | Read/Write | Integer | The amount of time (in milliseconds) that Cisco Unity Connection waits for additional input after callers press a single key
                                          that is not locked. If there is no input within this time, Cisco Unity Connection performs the action assigned to the single
                                          key. When a caller interrupts a greeting with a digit, Cisco Unity Connection will wait this number of milliseconds to see
                                          if they are going to enter more digits. Once this timeout is reached (or the caller terminates the input with a #), Cisco
                                          Unity Connection will do a look-up of the resulting string of numbers for a match with a DTMFAccessID value in the dialing
                                          domain. If a match is found, the call is sent to the matching object. If no match is found, the "Error greeting" for the call
                                          handler is invoked. If a key is "locked" then this value does not apply. Instead action is taken immediately on that key instead of allowing more
                                             digits. A value of 0 disables one key input. Possible Values: Range:- 0 - 10000 Default value is1500 |
| PartitionObjectId | Read/Write | String(36) | Specifies the object Id of the partition the Call Handler belongs to. URI To fetch PartitionObjectId :https://<connection-server>/vmrest/partitions |
| PartitionURI | Read Only | String | Specifies the URI of partitions. |
| PlayAfterMessage | Read/Write | Integer | Specifies what should be played after the message Possible Values: Refer to the table 3 under the section Enum Type as given at the end of the document Default Value:1 |
| PlayAfterMessageRecodingObjectId | Read/Write | String(36) | Object Id of the recording. URI To fetch its value :https://<connection-server>/vmrest/postgreetingrecordings from above URI get objectid. |
| PlayPostGreetingReording | Read/Write | Integer | Indicates whether the recording referenced by PostGreetingRecordingObjectId should be played. Possible Values: Refer to the table 2 under the section Enum type as given at the end of document. Default value is 0 |
| PostGreetingRecordingObjectId | Read/Write | String(36) | Specifies the object Id of the Post Greeting recording. URI To fetch its value: https://<connection-server>/vmrest/postgreetingrecordings from above URI get objectid. |
| PostGreetingURI | Read Only | String | URI of the Post Greeting Recording |
| PrependDigits | Read/Write | String | Touch-Tone digits to be prepended to extension when dialing transfer number ( #, 0,1...9,*). Digits, plus, hash and asterisk
                                          only are allowed |
| RecipientDistributionListObjectId | Read/Write | String(36) | Object Id of the distribution list that is the message recipient. URI To fetch its value: https://<connection-server>/vmrest/ from above URI get objectid. |
| RecipientDistributaionListURI | Read Only | String | URI of distribution lists |
| RecipientSubscriberObjectId | Read/Write | String(36) | Object id of a User with a mailbox that is the message recipient. |
| SchduleSetObjectId | Read/Write | String(36) | Object Id of the schedule set assigned to the Call Handler. |
| SchduleSetURI | Read Only | String | Specifies the URI of schedule sets. |
| SendPrivateMsg | Read/Write | Integer | Determines if an outside caller can mark their message as private. Possible Values: Refer to the table 4 under the section Enum type as given at the end of document. Default value is 0 |
| SendSecureMsg | Read/Write | Boolean | A flag indicating whether an unidentified caller can mark a message as "secure." Default value is false |
| SendUrgentMsg | Read/Write | Integer | A flag indicating whether an unidentified caller can mark a message as "urgent." Possible Values: Refer to the table 5 under the section Enum type as given at the end of document. Default value is 0(Never) |
| TimeZone | Read/Write | Integer | Used when the UseDefaultTimezone is set to false. To know the Integer Time Zone codes for the Time Zones installed on the
                                          server following URI can be used: https://<connection-server>/vmrest/timezones Example: 190 is the code for (GMT+05:30) Asia/Kolkata |
| UseCallLanguage | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection will use the language assigned to the call. Possible values: true false Default value is true |
| UseDefaultLanguage | Read/Write | Boolean | A flag that is dependent on the value of Language Field. if Language is set to Null, UseDefaultLanguage is set to true.if
                                          any language is specified, UseDefaultLanguage is set to false |
| UseDefaultTimeZone | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection will use the system default Time Zone. Possible values: true false Default value is false |
| GreetingsURI | Read Only | String | Specifies the URI of greetings. |
| TransferOptionsURI | Read Only | String | Specifies the URI of transfer options. |
| MenuEntriesURI | Read Only | String | Specifies the URI of menu entries. |

| Name | Value | Description |
|---|---|---|
| Ignore | 0 | Ignore - no action taken. |
| Hangup | 1 | Hangup - the call is immediately terminated. |
| Goto | 2 | Goto - go to an object such as a call handler, directory handler or interview handler. |
| Error | 3 | Error - play the error greeting. |
| TakeMsg | 4 | Take a message. |
| SkipGreeting | 5 | Skip greeting. |
| RestartGreeting | 6 | RestartGreeting - restart greeting on current handler |
| TransferAltContact | 7 | Transfer to Alternate Contact Number |
| RouteFromNextRule | 8 | Route From Next Call Routing Rule |

| Name | Value | Description |
|---|---|---|
| No | 0 | Don't play the recording |
| Always | 1 | Always play the configured recording |
| External | 2 | Play the recording for external calls only |

| Name | Value | Description |
|---|---|---|
| No | 0 | Don't play the recording |
| Always | 1 | Play system default |
| Standard | 2 | Play recording |

| Name | Value | Description |
|---|---|---|
| Never | 0 | No messages are marked private. |
| Always | 1 | All messages are marked private. |
| Ask | 2 | Ask the outside caller if they wish to mark the message as private. |

| Name | Value | Description |
|---|---|---|
| Never | 0 | Messages left by unidentified calls are never marked urgent. |
| Always | 1 | All messages left by unidentified callers are marked urgent. |
| Ask | 2 | Cisco Unity Connection asks unidentified callers whether to mark their messages urgent. |

| Name | Value | Description |
|---|---|---|
| SystemGreeting | 0 | Cisco Unity Connection plays a prerecorded greeting along with the recorded name of the subscriber (for example, "Sorry, <subscriber
                                                name> is not available"). If the subscriber does not have a recorded name, Cisco Unity Connection plays the subscriber extension
                                                instead. When a greeting is enabled but not recorded, Cisco Unity Connection plays a prerecorded system greeting. |
| Recorded Greeting | 1 | Use a personal recording for the call handler (or subscriber). This can be recorded over the phone or from the Cisco Unity
                                                Connection Administration and CPCA administrative interfaces on the call handler/subscriber. |
| NoGreeting | 2 | No greeting is played. |

| Name | Value | Description |
|---|---|---|
| PlayGreeting | 0 | Cisco Unity Connection transfers the call to the call handler greeting. |
| Transfer | 1 | Cisco Unity Connection transfers the call to the number in the "Extension" column in tbl_TransferOption. |

| Name | Value | Description |
|---|---|---|
| PlayGreeting | 1 | After the number of rings (as defined by "TransferRings" column), pull back the call and transfer the call to the appropriate
                                             greeting. |
| Release | 0 | Release the call to the phone system. |

| Name | Value | Description |
|---|---|---|
| No | 0 | Cisco Unity Connection prompts the caller to leave a message and allows the caller to dial another extension. |
| Yes | 1 | Cisco Unity Connection plays a prompt indicating that the extension is busy. The caller is put on hold. Note that this hold
                                             is not performed by the phone system. |
| Ask | 2 | Cisco Unity Connection gives the caller the options of holding, leaving a message, or dialing another extension. |

| Name | Value | Description |
|---|---|---|
| Supervised | 1 | Listen for busy, ring no answer. |
| Unsupervised | 0 | Just let the switch to do the transfer, and do not stay on the line and take action on RNA or busy. |

| Value | Description | Target Handler |
|---|---|---|
| AD | Directory conversation | Directory Handler |
| PHTransfer | Transfer to a user or call handler | Use or Call Handler |
| PHGreeting | Play greeting of a user or call handler | Use or Call Handler |
| PHInterview | Interview Conversation | Interview Handler |
| Attempt Forward | Forwards the call to the user's greeting if the forwarding number matches a user | NA |
| Attempt SignIn | Sends the call to a user's sign-in if the calling number matches a user | NA |
| BroadcastMessageAdministrator | Sends the call to a conversation for sending broadcast messages | NA |
| SystemTransfer | Sends the call to a conversation allowing the caller to transfer to a number they specify (assuming the restriction table
                                             allows it). | NA |
| CheckedOutGuest | Sends the call to a conversation for checked-out hotel guests. | NA |
| GreetingsAdministrator | Sends the call to a conversation allowing changing greetings by phone. | NA |
| ReverseTrapConv | Connects to Visual Voicemail. | NA |
| SubSignIn | Sends the call to the sign-in conversation, which prompts the user to enter their ID. | NA |
| ConvUtilsLiveRecord | Sends the call to the live-record pilot number configured on Call Manager. | NA |
| SubSysTransfer | Sends the call to a conversation allowing the caller to transfer to a number they specify (assuming the restriction table
                                             allows it). However, requires user sign-in first, so unknown callers cannot use it. | NA |

| Greeting | Description |
|---|---|
| Alternate | Alternate - can be used for a variety of special situations, such as vacations, leave of absence, or a holiday. An alternate
                                             greeting overrides all other greetings. |
| Busy | Busy - plays when the extension is busy. A busy greeting overrides the standard, off hours, and internal greetings. |
| Error | Error - plays when a caller attempts to dial an extension that does not exist on the system during a greeting. |
| Internal | Internal - plays to internal callers only. An internal greeting overrides the standard and off hours greetings. |
| Off Hours | Off hours - plays during the closed (non business) hours defined for the active schedule. An off hours greeting overrides
                                             the standard greeting, and thus limits the standard greeting to the open hours defined for the active schedule. |
| Standard | Standard - plays at all times unless overridden by another greeting. You cannot disable the standard greeting. |
| Holiday | Holiday - plays when holiday schedule is encountered unless overridden by an alternate greeting. |

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Alternate |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Busy |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Error |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Off%20Hours |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>/greetings/Standard |
|---|

| GET https://<connection-server>/vmrest/callhandlers/<CallhandlerObjectId>/greetings/Holiday |
|---|

| GET https://<connection-server>/vmrest/ callhandlertemplates/<callhandlertemplate-
  objectid>/templategreetings |
|---|

| <TemplateGreetings total="2">
  <TemplateGreeting>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templategreetings/Alternate</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <IgnoreDigits>false</IgnoreDigits>
    <PlayWhat>0</PlayWhat>
    <RepromptDelay>2</RepromptDelay>
    <Reprompts>0</Reprompts>
    <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
    <GreetingType>Alternate</GreetingType>
    <AfterGreetingAction>4</AfterGreetingAction>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
    <EnableTransfer>false</EnableTransfer>
  </TemplateGreeting>
  <TemplateGreeting>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templategreetings/Busy</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <IgnoreDigits>false</IgnoreDigits>
    <PlayWhat>0</PlayWhat>
    <RepromptDelay>2</RepromptDelay>
    <Reprompts>0</Reprompts>
    <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
    <GreetingType>Busy</GreetingType>
    <AfterGreetingAction>4</AfterGreetingAction>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
    <EnableTransfer>false</EnableTransfer>
  </TemplateGreeting>
</TemplateGreetings> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templategreetings
Accept: appliaction/json
Conenction: keep_alive |
|---|

| {
  "@total":"2"
  "TemplateGreeting": [
  {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templategreetings/Alternate"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "IgnoreDigits":"false"
    "PlayWhat":"0"
    "RepromptDelay":"2"
    "Reprompts":"0"
    "TimeExpires":"1972-01-01 00:00:00.0"
    "GreetingType":"Alternate"
    "AfterGreetingAction":"4"
    "PlayRecordMessagePrompt":"true"
    "EnableTransfer":"false"
  },
  {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templategreetings/Busy"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a"
    "IgnoreDigits":"false"
    "PlayWhat":"0"
    "RepromptDelay":"2"
    "Reprompts":"0"
    "TimeExpires":"1972-01-01 00:00:00.0"
    "GreetingType":"Busy"
    "AfterGreetingAction":"4"
    "PlayRecordMessagePrompt":"true"
    "EnableTransfer":"false"
  },
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
  objectid>/templategreetings/<Greetingname> |
|---|

| <TemplateGreeting>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
836910ac1a4c/templategreetings/Alternate</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
836910ac1a4c</CallhandlerURI>
    <IgnoreDigits>false</IgnoreDigits>
    <PlayWhat>0</PlayWhat>
    <RepromptDelay>2</RepromptDelay>
    <Reprompts>0</Reprompts>
    <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
    <GreetingType>Alternate</GreetingType>
    <AfterGreetingAction>4</AfterGreetingAction>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
    <EnableTransfer>false</EnableTransfer>
</TemplateGreeting> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<Callhandlertemplate-objectid>/templategreetings/<Greetingname>
Accept: application/json
Connection: keep_alive |
|---|

| {
    "URI":"/vmrest/callhandlertemplates/a2f8fb8f-68ee-4a17-90a0-
    bff0308b5b1a/templategreetings/Alternate"
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a"
    "IgnoreDigits":"false"
    "PlayWhat":"0"
    "RepromptDelay":"2"
    "Reprompts":"0"
    "TimeExpires":"1972-01-01 00:00:00.0"
    "GreetingType":"Alternate"
    "AfterGreetingAction":"4"
    "PlayRecordMessagePrompt":"true"
    "EnableTransfer":"false"
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templategreetings/<Greetingname>
Response Body:
<TemplateGreeting>
    <PlayWhat>1</PlayWhat>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
</TemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<Callhandlertemplate-objectid>/templategreetings/<Greetingname>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "PlayWhat":"1",
    "PlayRecordMessagePrompt":"true"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | URI of greetings |
| CallHandlerObjectId | Read Only | String | The unique identifier of the call handler
                                                					 object to which this greeting rule belongs. |
| TemplateCallHandlerURI | Read/Write | String | URI of the call handler. |
| IgnoreDigits | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                                					 Connection takes action in response to touchtone keys pressed by callers during
                                                					 the greeting. This column overrides all the Menu Entry settings when this
                                                   						greeting is active. This has the same effect as setting all the menu entry keys
                                                   						for this handler to "locked". It is a shorthand way of locking callers into the
                                                   						greeting so they cannot get out until it completes. Possible values: false: Caller
                                                         						  input enabled during greeting true: Caller
                                                         						  input ignored during greeting Default Value: false |
| PlayWhat | Read/Write | Integer | The source for the greeting when this
                                                					 greeting is active. Refer to the section Enumeration Type.<<Link will be
                                                   						mentioned later>> Default Value: 0 |
| RepromptDelay | Read/Write | Integer | The amount of time (in seconds) that Cisco
                                                					 Unity Connection waits without receiving any input from a caller before Cisco
                                                					 Unity Connection prompts the caller again. The range of this field can vary
                                                					 from 0 to 100. Possible values: 0: Do wait
                                                         						  without receiving caller input and do not replay greeting. 1 or greater:
                                                         						  Wait this number of seconds without receiving any input from the caller before
                                                         						  playing the greeting again. Default Value: 2 |
| Reprompts | Read/Write | Integer | The number of times to reprompt a caller.
                                                					 After the number of times indicated here, Cisco Unity Connection performs the
                                                					 after-greeting action. This column is typically used when an audio text application
                                                   						is expecting input from a caller. The range of this field can vary from 0 to
                                                   						100. Possible values: 0: Do not
                                                         						  re-prompt - Cisco Unity Connection will play the greeting once and then the
                                                         						  after-greeting action is taken. 1 or greater:
                                                         						  Number of times to re-prompt. The "RepromptDelay" value determines how many seconds to
                                                   						wait in between replays. Default Value: 0 |
| GreetingType | Read Only | String | Specifies the greeting type. Refer to the
                                                					 section Enumeration Type.<<Link will be mentioned later>> Default value: Standard |
| AfterGreetingAction | Read/Write | Integer | The type of call action to take, e.g.,
                                                					 hang-up, goto another object, etc. Refer to the section Enumeration Type.<<Link will be
                                                   						mentioned later>> Default value: 4 |
| AfterGreetingTargetConversation | Read/Write | String | Specifies the conversation to go to after
                                                					 the greeting is played. Refer to the section Enumeration Type.<<Link will be
                                                   						mentioned later> |
| AfterGreetingTargetHandlerObjectId | Read/Write | String | The unique identifier of the call action
                                                					 object that Cisco Unity Connection performs after the greeting is played. |
| TimeExpires | Read/Write | DateTime | The date and time when the greeting rule
                                                					 expires. The greeting rule is considered not expired (enabled), if the value is
                                                					 NULL or a future date. The greeting rule is considered expired (disabled), the
                                                					 value is in the past. The "Enhanced Alternate Greeting" feature uses this column
                                                   						to specify how long the subscriber wants their alternate greeting enabled. The
                                                   						standard greeting rule should never be disabled. The field is not displayed
                                                   						when the Greeting field is enabled with no end date and end time. |
| PlayRecordMessagePrompt | Read/Write | Boolean | A flag indicating whether the "Record your
                                                					 message at the tone…" prompt prior to recording a message. Values: true - Play
                                                         						  Record Message prompt is enabled. false - Play
                                                         						  Record prompt is disabled. Default Value: true |
| EnableTransfer | Read/Write | Boolean | A flag indicating when an extension is
                                                					 dialed at the greeting and the extension is not available whether to transfer
                                                					 to another extension. Values: true: Allows
                                                         						  transfer false: Does not
                                                         						  allow Default Value: false |

| PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandler-objectid>
Request Body:
<CallhandlerTemplate>
    <AfterMessageAction>2</AfterMessageAction>
    <AfterMessageTargetConversation>SystemTransfer</AfterMessageTargetConversation>
</CallhandlerTemplate> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT:  https://<connection-server>/vmrest/callhandlertemplates/<calhandler-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
"AfterMessageAction":"2",
"AfterMessageTargetConversation":"SystemTransfer"
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Request Body:
<CallhandlerTemplate>
    <PlayPostGreetingRecording>2</PlayPostGreetingRecording>
    <PostGreetingRecordingObjectId>0c6ab589-f289-4d4b-b3b7-
e4ec96bb783e</PostGreetingRecordingObjectId>
</CallhandlerTemplate> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>
Accept: applicaiton/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
"PlayPostGreetingRecording":"1",
"PostGreetingRecordingObjectId":"0c6ab589-f289-4d4b-b3b7-e4ec96bb783e"
} |
|---|

| Response Code: 204 |
|---|

| GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
  objectid>/templatetransferoptions |
|---|

| <TemplateTransferOptions total="2">
  <TemplateTransferOption>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templatetransferoptions/Alternate</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <TransferOptionType>Alternate</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
  </TemplateTransferOption>
  <TemplateTransferOption>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
    836910ac1a4c/templatetransferoptions/Off Hours</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
    836910ac1a4c</CallhandlerURI>
    <TransferOptionType>Off Hours</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
    d3b13f5040f5</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
  </TemplateTransferOption>
</TemplateTransferOptions> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-objectid>/templatetransferoptions
Accept: application/json
Connection: keep_alive
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
{
  "@total":"2"
  "TemplateTransferOption":   [
  {
    "URI":"/vmrest/callhandlertemplates/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7/templatetransferoptions/Alternate"
    "CallHandlerObjectId":"e07ee639-bf8a-4c37-9d6a-0b51beee65c7"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7"
    "TransferOptionType":"Alternate"
    "Action":"0"
    "RnaAction":"1"
    "TransferAnnounce":"false"
    "TransferConfirm":"false"
    "TransferDtDetect":"false"
    "TransferHoldingMode":"0"
    "TransferIntroduce":"false"
    "TransferRings":"4"
    "TransferScreening":"false"
    "TransferType":"1"
    "MediaSwitchObjectId":"f92e948f-6bd4-4891-ab8b-a3d930688305"
    "PhoneSystemURI":"/vmrest/phonesystems/f92e948f-6bd4-4891-ab8b-a3d930688305"
    "UsePrimaryExtension":"true"
    "PlayTransferPrompt":"true"
    "PersonalCallTransfer":"false"
    "Enabled":"true"
  },
  {
    "URI":"/vmrest/callhandlertemplates/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7/templatetransferoptions/Off Hours"
    "CallHandlerObjectId":"e07ee639-bf8a-4c37-9d6a-0b51beee65c7"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7"
    "TransferOptionType":"Off Hours"
    "Action":"0"
    "RnaAction":"1"
    "TransferAnnounce":"false"
    "TransferConfirm":"false"
    "TransferDtDetect":"false"
    "TransferHoldingMode":"0"
    "TransferIntroduce":"false"
    "TransferRings":"4"
    "TransferScreening":"false"
    "TransferType":"0"
    "MediaSwitchObjectId":"f92e948f-6bd4-4891-ab8b-a3d930688305"
    "PhoneSystemURI":"/vmrest/phonesystems/f92e948f-6bd4-4891-ab8b-a3d930688305"
    "UsePrimaryExtension":"true"
    "PlayTransferPrompt":"true"
    "PersonalCallTransfer":"false"
    "Enabled":"true"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
  objectId>/templatetransferoptions/<TransferOptionType>
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
<TemplateTransferOption>
    <URI>/vmrest/callhandlertemplates/5f6e1043-5edf-4646-90ac-
836910ac1a4c/templatetransferoptions/Alternate</URI>
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-
836910ac1a4c</CallhandlerURI>
    <TransferOptionType>Alternate</TransferOptionType>
    <Action>0</Action>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>abf4b7d1-89d5-45c2-bdc8-d3b13f5040f5</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/abf4b7d1-89d5-45c2-bdc8-
d3b13f5040f5</PhoneSystemURI>
    <UsePrimaryExtension>true</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
</TemplateTransferOption> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET: https://<connection-server>/vmrest/callhandlertemplates/<Callhandlertemplate-
objectid>/templatetransferoptions/<TransferOptionType>
Accept: applciation/json
Connection: keep_alive
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
{
    "URI":"/vmrest/callhandlertemplates/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7/templatetransferoptions/Alternate"
    "CallHandlerObjectId":"e07ee639-bf8a-4c37-9d6a-0b51beee65c7"
    "CallhandlerURI":"/vmrest/handlers/callhandlers/e07ee639-bf8a-4c37-9d6a-
    0b51beee65c7"
    "TransferOptionType":"Alternate"
    "Action":"0"
    "RnaAction":"1"
    "TransferAnnounce":"false"
    "TransferConfirm":"false"
    "TransferDtDetect":"false"
    "TransferHoldingMode":"0"
    "TransferIntroduce":"false"
    "TransferRings":"4"
    "TransferScreening":"false"
    "TransferType":"1"
    "MediaSwitchObjectId":"f92e948f-6bd4-4891-ab8b-a3d930688305"
    "PhoneSystemURI":"/vmrest/phonesystems/f92e948f-6bd4-4891-ab8b-a3d930688305"
    "UsePrimaryExtension":"true"
    "PlayTransferPrompt":"true"
    "PersonalCallTransfer":"false"
    "Enabled":"true"
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
objectid>/templatetransferoptions/<TransferOptionType>
Request Body: 
<TemplateTransferOption>
    <Action>1</Action>
    <Extension>1000</Extension>
    <TimeExpires>2012-12-31 12:00:00.0</TimeExpires>
    <Enabled>true</Enabled>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <TransferAnnounce>true</TransferAnnounce>
    <TransferConfirm>true</TransferConfirm>
    <TransferIntroduce>true</TransferIntroduce>
    <TransferScreening>true</TransferScreening>
    <TransferType>1</TransferType>
</TemplateTransferOption> |
|---|

| Response Code: 204 |
|---|

| GET: https://<connection-server>/vmrest/callhandlertemplates/<callhandlertemplate-
objectid>/templatetransferoptions/<TransferOptionType>
Accept: applciation/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Action":"1",
    "TimeExpires":"2012-12-31 12:00:00.0",
    "Extension":"1002",
    "PlayTransferPrompt":"true",
    "TransferAnnounce":"true",
    "TransferConfirm":"true"
} |
|---|

| Response Code: 204 |
|---|

| Parameters | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | URI of the call handler transfer options. |
| CallHandlerTemplateObjectId | Read Only | String | Specifies the call handler object ID |
| CallHandlerTemplateURI | Read Only | String | URI of the call handler being referenced. |
| TransferOptionType | Read Only | String | Specifies the transfer option type. There are 3 transfer option type available: Alternate - in effect at all times, overrides standard and offhours. OffHours - off or closed hours based on specified schedule. Standard - standard hours based on specified schedule. |
| Action | Read/Write | Integer | Specifies the transfer rule action. Custom type is Transfer Rule Action. Refer to the section Enumeration Type.<<Link will be mentioned later>> Default value: 0 |
| RnaAction | Read/Write | Integer | Action to take on Ring-No-Answer (RNA) condition. Refer to the section Enumeration Type.<<Link will be mentioned later>> |
| TimeExpires | Read/Write | Datetime | Rather than use a simple on and off scheme for enabling transfer options and greetings, Cisco Unity Connection employs a date
                                             scheme. If the value is NULL or a date is in the future then the transfer option is considered enabled. If the date is sometime
                                             in the past, then the transfer option is considered disabled. The "Standard" transfer option should never be disabled. For primary call handlers associated with subscribers, the "Alternate"
                                                transfer option should always be enabled since subscribers have only one transfer option used currently. |
| TransferAnnounce | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection plays "transferring call" when the subscriber answers the phone. This field
                                             requires a "TransferType" of supervised (1). Values can be: false: Do not say "Transferring call" when the subscriber answers the phone true: Say "Transferring call" when the subscriber answers the phone Default value: false |
| TransferConfirm | Read/Write | Boolean | The type of call transfer Cisco Unity Connection will perform - supervised or unsupervised (also referred to as "Release to
                                             Switch" transfer). Requires a "TransferType" of supervised. Unsupervised transfer (also referred to as "Release to Switch" transfer) - Cisco Unity Connection puts the caller on hold,
                                                      dials the extension, and releases the call to the phone system. When the line is busy or is not answered, the phone system
                                                      (not Cisco Unity Connection) forwards the call to the subscriber or handler greeting. To use "Unsupervised" transfer, call
                                                      forwarding must be enabled on the phone system Supervised transfer - Cisco Unity Connection acts as a receptionist, handling the transfer. If the line is busy or the call
                                                      is not answered, Cisco Unity Connection (not the phone system) forwards the call to the subscriber or handler greeting. Supervised
                                                      transfer can be used regardless if the phone system forwards calls or not. Typically TransferConfirm is used in conjunction with the call screening option ("TransferScreening" column) enabled. This
                                                combination enables the subscriber to hear the name of the caller and then decide if they want to take the call or not. Default
                                                Value: false. Values can be: false: Transfer confirm disabled true: Transfer confirm enabled Default value: false |
| TransferDtDetect | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection will check for dial tone before attempting to transfer the call. Requires
                                             a "TransferType" of supervised (1). This is usually used for phone systems that do not have "positive disconnect" capabilities to avoid sending terminated calls
                                                to the operator console, for instance. Possible values can be: false: Do not check for dial tone prior to transferring a call true: Check for dial tone prior to transferring a call Default value:false |
| TransferHoldingMode | Read/Write | Integer | The action Cisco Unity Connection will take when the extension is busy. Requires a TransferType column value = "Supervised" (1). Default Value: 0 |
| TransferIntroduce | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection will say "call for <recorded name of the call handler>" when the subscriber
                                             answers the phone. Requires a "TransferType" of supervised (1). This functionality is normally used when a single extension number is being shared
                                                by multiple subscribers or a scenario where the subscriber who is the message recipient takes calls for more than one dialed
                                                extension. The introduction alerts the subscriber who answers that the call is for the call handler. Default Value: false. |
| TransferRings | Read/Write | Integer | The number of times the extension rings before Cisco Unity Connection considers it a "ring no answer" and plays the subscriber
                                             or handler greeting. Requires a "TransferType" of supervised (1). The value of this column should never be less than 2 for a supervised transfer.
                                                The range can vary from 2 to 20. Default Value: 4 |
| TransferScreening | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection will prompt callers to say their names. When the phone is answered, the subscriber
                                             hears "Call from…" before Cisco Unity Connection transfers the call. Requires a "TransferType" of supervised (1). Normally this column is used along with "TransferConfirm" to allow the subscriber
                                                to screen calls. Values can be: false: Call screening disabled true: Ask and record caller name Default Value: false |
| TransferType | Read/Write | Integer | The type of call transfer Cisco Unity Connection will perform - supervised or unsupervised (also referred to as "Release to
                                             Switch" transfer). Unsupervised transfer (also referred to as "Release to Switch" transfer) - Cisco Unity Connection puts the caller on hold,
                                                      dials the extension, and releases the call to the phone system. When the line is busy or is not answered, the phone system
                                                      (not Cisco Unity Connection) forwards the call to the subscriber or handler greeting. To use "Unsupervised" transfer, call
                                                      forwarding must be enabled on the phone system. Supervised transfer - Cisco Unity Connection acts as a receptionist, handling the transfer. If the line is busy or the call
                                                      is not answered, Cisco Unity Connection (not the phone system) forwards the call to the subscriber or handler greeting. Supervised
                                                      transfer can be used regardless if the phone system forwards calls or not. Default value: 0 |
| MediaSwitchObjectId | Read Only | String | The unique identifier of the MediaSwitch object that Cisco Unity Connection uses for transferring the call to the subscriber
                                             phone. |
| PhoneSystemURI | Read Only | String | Specifies the URI of the phone systems |
| UsePrimaryExtension | Read/Write | Boolean | If extension is null this will be set to 1 (true) to indicate we are using instead the DtmfAccessId for the owning handler
                                             or subscriber. Possible Values: false true Default value: true |
| Extension | Read/Write | Integer | If an administrator using Cisco Unity Connection Administration chooses to transfer to the extension of a subscriber or call
                                             handler, Cisco Unity Connection will automatically enter the DtmfAccessId value pulled from the DtmfAccessId table for the
                                             call handler into this column. Note - Digits, hash, comma, asterisk, plus are allowed. |
| PlayTransferprompt | Read/Write | Boolean | A flag indicating whether the "Wait while I transfer your call" prompt should be played prior to transferring a call. Values can be: true - Play Transfer prompt is enabled. false - Play transfer prompt is disabled. Default Value: true |
| PersonalCallTransfer | Read/Write | Boolean | A flag indicating whether or not Personal Call Transfer Rules are used for the specific Transfer Option. Values can be: false: Not enabled true: Enabled Default value: false |
| Enabled | Read/Write | Boolean | Indicate whether the transfer option is enabled or not.To enable rule till particular end date TimeExpires should also be
                                             specified and to enable transfer rule with no end date, the TimeExpires field should be empty. Possible value: true: enabled false: disabled Default value: true This means transfer rules are enabled with no end date by default. |