---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-interview-handler-api-html-84debcd0a8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-interview-handler-api.html
retrieved_at: 2026-08-17T03:49:45.122444+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API--Interview Handler APIs

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API--Interview Handler APIs

# Cisco Unity Connection Provisioning Interface (CUPI) API--Interview Handler APIs

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Interview Handler APIs

### Interview Handler
                           	 APIs

Interview Handler APIs

Interview Handler Questions APIs

#### Listing the
                              	 Interview Handlers

The following is an example of
                                    		  the GET request that fetch the list of interview handlers:

```
GET https://<connection-server>/vmrest/handlers/interviewhandlers
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<InterviewHandlers total="1">
  <InterviewHandler>
    <URI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-1cfac4ae0226</URI>
    <CreationTime>2013-01-10T12:02:20Z</CreationTime>
    <Language>1033</Language>
    <DisplayName>Texoma_IH2</DisplayName>
    <Undeletable>false</Undeletable>
    <VoiceName>7b904f83-2b9c-4283-a22e-6e28028b2750.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/ccb35746-d253-42ed-b481-
    4d906ae2e882</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-
    1cfac4ae0226/voicename</VoiceNameURI>
    <LocationObjectId>312f6d60-f9e8-447a-b7d9-a25040fa0ca2</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/312f6d60-f9e8-447a-b7d9-
    a25040fa0ca2</LocationURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <ObjectId>9153ef65-c38a-4588-b041-1cfac4ae0226</ObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <RecipientDistributionListObjectId>80b13e8d-1dbe-4389-ba97-
    91aaa10512fe</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/80b13e8d-1dbe-4389-ba97-
    91aaa10512fe</RecipientDistributionListURI>
    <AfterMessageAction>1</AfterMessageAction>
    <UseCallLanguage>true</UseCallLanguage>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <DispatchDelivery>false</DispatchDelivery>
    <PartitionObjectId>d3c659f3-27f7-43c8-bb25-778cec9fba21</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d3c659f3-27f7-43c8-bb25-
    778cec9fba21</PartitionURI>
    <InterviewQuestionsURI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-1cfac4ae0226/interviewquestions</InterviewQuestionsURI>
  </InterviewHandler>
</InterviewHandlers>
```

```
Response Code: 200
```

JSON Example

To view the list of interview handlers, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/handlers/interviewhandlers
Accept: application/json
Connection: Keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total": "1",
  "InterviewHandler":[
  {
    "URI": "/vmrest/handlers/interviewhandlers/f1d0640b-f268-4725-87bb-e1762314fee6",
    "CreationTime": "2013-02-13T10:10:43Z",
    "Language": "1033",
    "DisplayName": "Taxoma_Interviewer_1",
    "Undeletable": "false",
    "LocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
    "LocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-4f7e-b5fc-
    8346df0ffee1",
    "SendUrgentMsg": "0",
    "ObjectId": "f1d0640b-f268-4725-87bb-e1762314fee6",
    "TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438",
    "RecipientSubscriberObjectId": "47749981-5ceb-4674-a6b7-0b0afde4bfcc",
    "RecipientUserURI": "/vmrest/users/47749981-5ceb-4674-a6b7-0b0afde4bfcc",
    "AfterMessageAction": "4",
    "UseCallLanguage": "true",
    "UseDefaultLanguage": "true",
    "DispatchDelivery": "false",
    "PartitionObjectId": "30438c03-e8de-4584-bb5b-0dae05faf0af",
    "PartitionURI": "/vmrest/partitions/30438c03-e8de-4584-bb5b-0dae05faf0af",
    "InterviewQuestionsURI": "/vmrest/handlers/interviewhandlers/f1d0640b-f268-4725-
    87bb-e1762314fee6/interviewquestions"
  },
  ]
}
```

```
Response Code: 200
```

##### Listing Specific
                                 	 Tenant Related Interview Handlers by System Administrator

In Cisco Unity Connection 10.5(2)
                                       		  and later, the system administrator can use TenantObjectID to list the specific
                                       		  tenant related interview handlers using the following URI:

```
GET https://<connection-server>/vmrest/handlers/interviewhandlers?query=(TenantObjectId is <Tenant-ObjectId>)
```

To get the TenantObjectID, use the following URI:

```
GET https://<connection-server>/vmrest/tenants
```

#### Viewing the
                              	 Details of Specific Interview Handler

The following is an example of
                                    		  the GET request that lists the details of interview handler represented by the
                                    		  provided value of interview handler ID:

```
GET https://< connection-server>/vmrest/handlers/interviewhandlers/<InterviewHandlerObject-Id>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<InterviewHandler>
    <URI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-1cfac4ae0226</URI>
    <CreationTime>2013-01-10T12:02:20Z</CreationTime>
    <Language>1033</Language>
    <DisplayName>Texoma_IH2</DisplayName>
    <Undeletable>false</Undeletable>
    <VoiceName>7b904f83-2b9c-4283-a22e-6e28028b2750.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/ccb35746-d253-42ed-b481-4d906ae2e882</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-
1cfac4ae0226/voicename</VoiceNameURI>
    <LocationObjectId>312f6d60-f9e8-447a-b7d9-a25040fa0ca2</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/312f6d60-f9e8-447a-b7d9-
a25040fa0ca2</LocationURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <ObjectId>9153ef65-c38a-4588-b041-1cfac4ae0226</ObjectId>
    <RecipientDistributionListObjectId>80b13e8d-1dbe-4389-ba97-
91aaa10512fe</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/80b13e8d-1dbe-4389-ba97-
91aaa10512fe</RecipientDistributionListURI>
    <AfterMessageAction>1</AfterMessageAction>
    <UseCallLanguage>true</UseCallLanguage>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <DispatchDelivery>false</DispatchDelivery>
    <PartitionObjectId>d3c659f3-27f7-43c8-bb25-778cec9fba21</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d3c659f3-27f7-43c8-bb25-778cec9fba21</PartitionURI>
    <InterviewQuestionsURI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-
1cfac4ae0226/interviewquestions</InterviewQuestionsURI>
</InterviewHandler>
```

```
Response Code: 200
```

JSON Example

To view the list of interview handlers, do the following:

```
Request URI:
GET https://< connection-server>/vmrest/handlers/interviewhandlers/<InterviewHandlerObject-Id>
Accept: application/json
Connection: Keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "URI": "/vmrest/handlers/interviewhandlers/f1d0640b-f268-4725-87bb-e1762314fee6",
    "CreationTime": "2013-02-13T10:10:43Z",
    "Language": "1033",
    "DisplayName": "Texoma_IH2",
    "Undeletable": "false",
    "LocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
    "LocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-4f7e-b5fc-
8346df0ffee1",
    "SendUrgentMsg": "0",
    "ObjectId": "f1d0640b-f268-4725-87bb-e1762314fee6",
    "RecipientSubscriberObjectId": "47749981-5ceb-4674-a6b7-0b0afde4bfcc",
    "RecipientUserURI": "/vmrest/users/47749981-5ceb-4674-a6b7-0b0afde4bfcc",
    "AfterMessageAction": "4",
    "UseCallLanguage": "true",
    "UseDefaultLanguage": "true",
    "DispatchDelivery": "false",
    "PartitionObjectId": "30438c03-e8de-4584-bb5b-0dae05faf0af",
    "PartitionURI": "/vmrest/partitions/30438c03-e8de-4584-bb5b-0dae05faf0af",
    "InterviewQuestionsURI": "/vmrest/handlers/interviewhandlers/f1d0640b-f268-4725-87bb-
e1762314fee6/interviewquestions"
}
```

```
Response Code: 200
<pre>

=== Creating a New Interview Handler ===

The following is an example of the POST request that creates a new interview handler: 
<pre>
  POST https://<connection-server>/vmrest/handlers/interviewhandlers
  Request Body:
  <InterviewHandler>
    <DisplayName>Texoma_IH2</DisplayName>
    <RecipientDistributionListObjectId>80b13e8d-1dbe-4389-ba97-
    91aaa10512fe</RecipientDistributionListObjectId>
  </InterviewHandler>
```

```
Response Code: 200
<pre>

'''JSON Example'''

To create a new interview handler:
<pre>
POST https://<connection-server>/vmrest/handlers/interviewhandlers
Accept: application/json
Content-Type: application/json
Connection: Keep-alive
{
    "DisplayName": "Taxoma_Interviewer",
    "RecipientDistributionListObjectId": "c596c45c-00a3-4714-a359-4ac45da38232"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

#### Delete the
                              	 Interview Handler

This request can be used to
                                    		  delete an interview handler specified by an object ID.

```
DELETE: https://<connection-server>/vmrest/ handlers/interviewhandlers/<interviewhandler-objectid>
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To delete interview handler, do the following:

```
Request URI:
DELETE https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>
Accept: application/json
Connection: Keep-alive
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Updating the
                              	 Interview Handler

Example 1: Modify the Interview Handler The following is an example of the PUT request that can be used to modify the interview handler.

```
PUT https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>
  Request Body:
  <InterviewHandler>
    <UseCallLanguage>true</UseCallLanguage>
    <UseDefaultLanguage>false</UseDefaultLanguage> 
    <Language>1033</Language>
  </InterviewHandler>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

JSON Example

To update the interview handler, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>
Accept: application/json
Content-Type: application/json
Connection: Keep-alive
Request Body:
{
    "Language": "1033",
    "UseCallLanguage": "true",
    "UseDefaultLanguage": "false"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

```
Request Body:
<InterviewHandler>
    <RecipientDistributionListObjectId>68d149ff-59f6-4394-8103-
f3c2bf75d8bb</RecipientDistributionListObjectId> 
</InterviewHandler>
```

```
Response Code: 204
```

RecipientSubscriberObjectId and RecipientUserURI fields are replaced with RecipientDistributionListObjectId and RecipientDistributionListURI
                                    The table given below lists the possible values of the After Interview Action:

- SystemTransfer

- GreetingsAdministrator

- SubSignIn

- SubSysTransfer

#### Explanation of
                              	 Data Fields

```
https://<connection-server>/vmrest/languagemap
```

Possible values:

- false: The
                                                         						  handler can be deleted by an administrator (with the required privilege) via an
                                                         						  administrative application such as Cisco Unity Connection Administration or
                                                         						  Cisco Unity Connection Bulk Administration Manager.

- true: The
                                                         						  handler cannot be deleted by an administrator via Cisco Unity Connection
                                                         						  Administration or Cisco Unity Connection Bulk Administration Manager.

Possible values :-

- 2 Ask - Cisco
                                                         						  Unity Connection asks unidentified callers whether to mark their interview
                                                         						  messages normal or urgent.

- 0 Normal -
                                                         						  interview messages left by unidentified calls are always marked normal.

- 1 Urgent - all
                                                         						  interview messages left by unidentified calls are always marked urgent.

- 0 Ignore - no
                                                         						  action taken.

- 1 Hangup - the
                                                         						  call is immediately terminated.

- 2 Goto - go to
                                                         						  an object such as a call handler, directory handler or interview handler.

- 3 Error - play
                                                         						  the error greeting.

- 4 Take a
                                                         						  message.

- 5 Skip greeting.

- 6
                                                         						  RestartGreeting

- 7 Transfer to
                                                         						  Alternate Contact Number

- 8 Route From
                                                         						  Next Call Routing Rule

Default value: 4

Possible values:

- true: Use the
                                                         						  language specified by the system call routing rule to play prompts for users.

- false: Do not
                                                         						  use the language specified by the system call routing rule to play prompts for
                                                         						  users.

Default value: true

Default value: true.

Possible values:-

- true: Messages
                                                         						  left for interview handler is for dispatch delivery.

- false: Messages
                                                         						  left for interview handler is not for dispatch delivery

Default value: false

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Interview Handler Questions
                        	 APIs

### Interview Handler
                           	 Questions APIs

Administrator can use this API to
                              		fetch/update the interview questions of a particular interview handler. You can
                              		update various attributes of interview handler questions as well using this
                              		API.

#### Listing the
                              	 Interview Handler Questions

The following is an example of
                                    		  the GET request that fetch the list of interview handler questions:

```
GET https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-
  objectid>/interviewquestions
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<InterviewQuestions total="1">
  <InterviewQuestion>
    <InterviewHandlerObjectId>9fa58ed4-af0b-4de5-977c-
  8c080b0727c1</InterviewHandlerObjectId>
    <InterviewHandlerURI>/vmrest/handlers/interviewhandlers/9fa58ed4-af0b-4de5-977c-
  8c080b0727c1</InterviewHandlerURI>
    <QuestionNumber>1</QuestionNumber>
    <MaxMsgLength>30</MaxMsgLength>
    <StreamText>1</StreamText>
    <IsActive>true</IsActive>
  </InterviewQuestion>
</InterviewQuestions>
```

```
Response Code: 200
```

JSON Example

To update the interview handler, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>/interviewquestions
Accept: application/json
Connection: Keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{ 
 },{
"@total": "2",
"InterviewQuestion":	[
  {
    "InterviewHandlerObjectId": "99800fcc-e8df-42d3-ac3f-5117483b293e",         
    "InterviewHandlerURI": "/vmrest/handlers/interviewhandlers/99800fcc-e8df-42d3-ac3f-
    5117483b293e",
    "QuestionNumber": "1",
    "MaxMsgLength": "30",
    "StreamText": "1",
    "IsActive": "true"
  },
  {
  "InterviewHandlerObjectId": "99800fcc-e8df-42d3-ac3f-5117483b293e",
  "InterviewHandlerURI": "/vmrest/handlers/interviewhandlers/99800fcc-e8df-42d3-ac3f-
  5117483b293e",
  "QuestionNumber": "2",
  "MaxMsgLength": "30",
  "StreamText": "2",
  "IsActive": "true"
  }
  ]
}
```

```
Response Code: 200
```

#### Viewing the
                              	 Specific Interview Handler Question

The following is an example of
                                    		  the GET request that lists the details of interview handler question
                                    		  represented by the provided value of interview handler ID:

```
GET https://< connection-server>/vmrest/handlers/interviewhandlers/<Interviewhandler-
  objectid>/interviewquestions/<questionnumber>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<InterviewQuestion>
      <InterviewHandlerObjectId>9fa58ed4-af0b-4de5-977c-
  8c080b0727c1</InterviewHandlerObjectId>
      <InterviewHandlerURI>/vmrest/handlers/interviewhandlers/9fa58ed4-af0b-4de5-977c-
  8c080b0727c1</InterviewHandlerURI>
      <QuestionNumber>2</QuestionNumber>
      <MaxMsgLength>30</MaxMsgLength>
      <StreamText>2</StreamText>
      <IsActive>true</IsActive>
  </InterviewQuestion>
```

```
Response Code: 200
```

#### Updating the
                              	 Interview Handler Questions

The following is an example of
                                    		  the PUT request that can be used to modify an interview handler questions.

```
PUT https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>/interviewquestions/<questionnumber>
Request Body:
<InterviewQuestion>
    <IsActive>false</IsActive>
</InterviewQuestion>
```

```
Response Code: 204
```

JSON Example

To update the interview handler, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>/interviewquestions/<questionnumber>
Accept: application/json
Content-Type: application/json
Connection: Keep-alive
Request Body:
{
    "IsActive": "false"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

Value can range from 1 to 1200. Default value: 30 seconds

Possible values:

- true: activate
                                                         						  question

- false:
                                                         						  Inactivate question

Default Value: true

#### Update the
                              	 Interview question using the Input Stream

The Interview question can also
                                    		  be updated using the Input Stream. An input stream can be created from the wav
                                    		  file and passed as the request body. The URL for this should be :

```
PUT https://<connectionserver>/vmrest/handlers/interviewhandlers/<interviewhandlerobjectid>/interviewquestions/
<QuestionNumber>/audio.
```

The request body will contain an attachment with media type audio/wav.
                                    		  Attachment can be uploaded via application to upload the wave file over HTTPS.
                                    		  Also add the header "content-type" for the request which value will be passed
                                    		  as "audio/wav".

Following URL can be used to listen/get to the question associated
                                    		  with the interview handler: Paste the URL in the browser and listen to the
                                    		  uploaded question.

```
https://<connectionserver>/vmrest/handlers/interviewhandlers/<interviewhandlerobjectid>/interviewquestions/<QuestionNumber>/audio.
```

| GET https://<connection-server>/vmrest/handlers/interviewhandlers |
|---|

| <InterviewHandlers total="1">
  <InterviewHandler>
    <URI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-1cfac4ae0226</URI>
    <CreationTime>2013-01-10T12:02:20Z</CreationTime>
    <Language>1033</Language>
    <DisplayName>Texoma_IH2</DisplayName>
    <Undeletable>false</Undeletable>
    <VoiceName>7b904f83-2b9c-4283-a22e-6e28028b2750.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/ccb35746-d253-42ed-b481-
    4d906ae2e882</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-
    1cfac4ae0226/voicename</VoiceNameURI>
    <LocationObjectId>312f6d60-f9e8-447a-b7d9-a25040fa0ca2</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/312f6d60-f9e8-447a-b7d9-
    a25040fa0ca2</LocationURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <ObjectId>9153ef65-c38a-4588-b041-1cfac4ae0226</ObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <RecipientDistributionListObjectId>80b13e8d-1dbe-4389-ba97-
    91aaa10512fe</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/80b13e8d-1dbe-4389-ba97-
    91aaa10512fe</RecipientDistributionListURI>
    <AfterMessageAction>1</AfterMessageAction>
    <UseCallLanguage>true</UseCallLanguage>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <DispatchDelivery>false</DispatchDelivery>
    <PartitionObjectId>d3c659f3-27f7-43c8-bb25-778cec9fba21</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d3c659f3-27f7-43c8-bb25-
    778cec9fba21</PartitionURI>
    <InterviewQuestionsURI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-1cfac4ae0226/interviewquestions</InterviewQuestionsURI>
  </InterviewHandler>
</InterviewHandlers> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/handlers/interviewhandlers
Accept: application/json
Connection: Keep-alive |
|---|

| {
  "@total": "1",
  "InterviewHandler":[
  {
    "URI": "/vmrest/handlers/interviewhandlers/f1d0640b-f268-4725-87bb-e1762314fee6",
    "CreationTime": "2013-02-13T10:10:43Z",
    "Language": "1033",
    "DisplayName": "Taxoma_Interviewer_1",
    "Undeletable": "false",
    "LocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
    "LocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-4f7e-b5fc-
    8346df0ffee1",
    "SendUrgentMsg": "0",
    "ObjectId": "f1d0640b-f268-4725-87bb-e1762314fee6",
    "TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438",
    "RecipientSubscriberObjectId": "47749981-5ceb-4674-a6b7-0b0afde4bfcc",
    "RecipientUserURI": "/vmrest/users/47749981-5ceb-4674-a6b7-0b0afde4bfcc",
    "AfterMessageAction": "4",
    "UseCallLanguage": "true",
    "UseDefaultLanguage": "true",
    "DispatchDelivery": "false",
    "PartitionObjectId": "30438c03-e8de-4584-bb5b-0dae05faf0af",
    "PartitionURI": "/vmrest/partitions/30438c03-e8de-4584-bb5b-0dae05faf0af",
    "InterviewQuestionsURI": "/vmrest/handlers/interviewhandlers/f1d0640b-f268-4725-
    87bb-e1762314fee6/interviewquestions"
  },
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/handlers/interviewhandlers?query=(TenantObjectId is <Tenant-ObjectId>) |
|---|

| GET https://<connection-server>/vmrest/tenants |
|---|

| GET https://< connection-server>/vmrest/handlers/interviewhandlers/<InterviewHandlerObject-Id> |
|---|

| <InterviewHandler>
    <URI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-1cfac4ae0226</URI>
    <CreationTime>2013-01-10T12:02:20Z</CreationTime>
    <Language>1033</Language>
    <DisplayName>Texoma_IH2</DisplayName>
    <Undeletable>false</Undeletable>
    <VoiceName>7b904f83-2b9c-4283-a22e-6e28028b2750.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/ccb35746-d253-42ed-b481-4d906ae2e882</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-
1cfac4ae0226/voicename</VoiceNameURI>
    <LocationObjectId>312f6d60-f9e8-447a-b7d9-a25040fa0ca2</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/312f6d60-f9e8-447a-b7d9-
a25040fa0ca2</LocationURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <ObjectId>9153ef65-c38a-4588-b041-1cfac4ae0226</ObjectId>
    <RecipientDistributionListObjectId>80b13e8d-1dbe-4389-ba97-
91aaa10512fe</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/80b13e8d-1dbe-4389-ba97-
91aaa10512fe</RecipientDistributionListURI>
    <AfterMessageAction>1</AfterMessageAction>
    <UseCallLanguage>true</UseCallLanguage>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <DispatchDelivery>false</DispatchDelivery>
    <PartitionObjectId>d3c659f3-27f7-43c8-bb25-778cec9fba21</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/d3c659f3-27f7-43c8-bb25-778cec9fba21</PartitionURI>
    <InterviewQuestionsURI>/vmrest/handlers/interviewhandlers/9153ef65-c38a-4588-b041-
1cfac4ae0226/interviewquestions</InterviewQuestionsURI>
</InterviewHandler> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://< connection-server>/vmrest/handlers/interviewhandlers/<InterviewHandlerObject-Id>
Accept: application/json
Connection: Keep-alive |
|---|

| {
    "URI": "/vmrest/handlers/interviewhandlers/f1d0640b-f268-4725-87bb-e1762314fee6",
    "CreationTime": "2013-02-13T10:10:43Z",
    "Language": "1033",
    "DisplayName": "Texoma_IH2",
    "Undeletable": "false",
    "LocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
    "LocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-4f7e-b5fc-
8346df0ffee1",
    "SendUrgentMsg": "0",
    "ObjectId": "f1d0640b-f268-4725-87bb-e1762314fee6",
    "RecipientSubscriberObjectId": "47749981-5ceb-4674-a6b7-0b0afde4bfcc",
    "RecipientUserURI": "/vmrest/users/47749981-5ceb-4674-a6b7-0b0afde4bfcc",
    "AfterMessageAction": "4",
    "UseCallLanguage": "true",
    "UseDefaultLanguage": "true",
    "DispatchDelivery": "false",
    "PartitionObjectId": "30438c03-e8de-4584-bb5b-0dae05faf0af",
    "PartitionURI": "/vmrest/partitions/30438c03-e8de-4584-bb5b-0dae05faf0af",
    "InterviewQuestionsURI": "/vmrest/handlers/interviewhandlers/f1d0640b-f268-4725-87bb-
e1762314fee6/interviewquestions"
} |
|---|

| Response Code: 200
<pre>

=== Creating a New Interview Handler ===

The following is an example of the POST request that creates a new interview handler: 
<pre>
  POST https://<connection-server>/vmrest/handlers/interviewhandlers
  Request Body:
  <InterviewHandler>
    <DisplayName>Texoma_IH2</DisplayName>
    <RecipientDistributionListObjectId>80b13e8d-1dbe-4389-ba97-
    91aaa10512fe</RecipientDistributionListObjectId>
  </InterviewHandler> |
|---|

| Response Code: 200
<pre>

'''JSON Example'''

To create a new interview handler:
<pre>
POST https://<connection-server>/vmrest/handlers/interviewhandlers
Accept: application/json
Content-Type: application/json
Connection: Keep-alive
{
    "DisplayName": "Taxoma_Interviewer",
    "RecipientDistributionListObjectId": "c596c45c-00a3-4714-a359-4ac45da38232"
} |
|---|

| Response Code: 201 |
|---|

| DELETE: https://<connection-server>/vmrest/ handlers/interviewhandlers/<interviewhandler-objectid> |
|---|

| Response Code: 204 |
|---|

| Request URI:
DELETE https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>
Accept: application/json
Connection: Keep-alive |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>
  Request Body:
  <InterviewHandler>
    <UseCallLanguage>true</UseCallLanguage>
    <UseDefaultLanguage>false</UseDefaultLanguage> 
    <Language>1033</Language>
  </InterviewHandler> |
|---|

| Response Code: 204 |
|---|

| Note | The Inherit Language field from the call is selected and the UseDefaultLanguage field will get updated in the database as
                                                the Language field is specified. |
|---|---|

| Request URI:
PUT https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>
Accept: application/json
Content-Type: application/json
Connection: Keep-alive
Request Body:
{
    "Language": "1033",
    "UseCallLanguage": "true",
    "UseDefaultLanguage": "false"
} |
|---|

| Response Code: 204 |
|---|

| Request Body:
<InterviewHandler>
    <RecipientDistributionListObjectId>68d149ff-59f6-4394-8103-
f3c2bf75d8bb</RecipientDistributionListObjectId> 
</InterviewHandler> |
|---|

| Response Code: 204 |
|---|

| AfterInterviewAction | AfterMessageAction | AfterMessageTargetConversation | AfterMessageTargetHandlerObjectId |
|---|---|---|---|
| CallAction (Refer to the table given below) | 1-8 | NA | NA |
| CallHandler | 2 | PHTransfer/PHGreeting | <object-id> of call handler having IsPrimary parameter as true. URI to get object id of call handlers: https://<connection-server>/vmrest/handlers/callhandlers?query=(IsPrimary%20is%201) |
| Interview Handler | 2 | PHInterview | <object-id> of interview handler. URI to get object id of Interview handlers: https://<connection-server>/vmrest/handlers/interviewhandlers. |
| Directory Handler | 2 | AD | <object-id> of directory handler. URI to get object id of directory handlers: https://<connection-server>/vmrest/handlers/directoryhandlers |
| Conversation | 2 | BroadcastMessageAdministrator SystemTransfer GreetingsAdministrator SubSignIn SubSysTransfer | NA |
| User with Mailbox | 2 | PHTransfer/PHGreeting | <object-id> which can be captured from /vmrest/users. |

| Name | Call Action Value | Description |
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

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | Interview Handler URI |
| Creation Time | Read Only | Datetime | Stores the time of creation of Interview
                                                					 Handler |
| Language | Read/Write | Integer | Stores code for language where valid values
                                                					 range from 1024 to 58378 and 0 is not allowed. All possible language code
                                                					 values can be fetched using https://<connection-server>/vmrest/languagemap | https://<connection-server>/vmrest/languagemap |
| https://<connection-server>/vmrest/languagemap |
| DisplayName | Read/Write | String (64) | Name of an interview handler |
| Undeletable | Read/Write | Boolean | A flag indicating whether this handler can
                                                					 be deleted via an administrative application such as Cisco Unity Connection
                                                					 Administration. It is used to prevent the deletion of factory defaults such as
                                                					 the "Opening Greeting" call handler. Possible values: false: The
                                                         						  handler can be deleted by an administrator (with the required privilege) via an
                                                         						  administrative application such as Cisco Unity Connection Administration or
                                                         						  Cisco Unity Connection Bulk Administration Manager. true: The
                                                         						  handler cannot be deleted by an administrator via Cisco Unity Connection
                                                         						  Administration or Cisco Unity Connection Bulk Administration Manager. |
| VoiceName | Read/Write | String (40) | The name of the .wav file containing the
                                                					 recorded audio of the name of an interview handler. |
| VoiceFileURI | Read Only | String | Specifies the URI of voice file. |
| VoiceNameURI | Read Only | String | Specifies the URI of voice name. |
| LocationObjectID | Read Only | String (36) | The unique identifier of the Location
                                                					 object to which this handler belongs. |
| LocationURI | Read Only | String | Specifies the URI of locations |
| SendUrgentMsg | Read/Write | Integer | A flag indicating whether an unidentified
                                                					 caller is given a choice to mark a message as Urgent or Normal, or if not given
                                                					 the choice, whether the message is always marked Normal (default value) or
                                                					 Urgent. Possible values :- 2 Ask - Cisco
                                                         						  Unity Connection asks unidentified callers whether to mark their interview
                                                         						  messages normal or urgent. 0 Normal -
                                                         						  interview messages left by unidentified calls are always marked normal. 1 Urgent - all
                                                         						  interview messages left by unidentified calls are always marked urgent. |
| ObjectId | Read Only | String (36) | Object ID of interview handler. |
| TenantObjectId | Read Only | String (36) | The unique identifier of the tenant to
                                                					 which the interview handler belongs. This field is reflected in the response
                                                					 only if the interview handler belongs to a particular tenant. |
| RecipientDistributionListObjectId | Read/Write | String (36) | Object ID of distribution list if the
                                                					 recipient of interview handler is set to distribution list. |
| RecipientDistributionListURI | Read Only | String | URI of the distribution list. |
| RecipientSubscriberObjectId | Read/Write | String (36) | Object ID of the subscriber if the
                                                					 recipient of interview handler is set to a user. |
| RecipientSubscriberURI | Read/Write | String | URI of the subscriber. |
| AfterMessageAction | Read/Write | Integer | Possible types of call action to take,
                                                					 e.g., hang-up, go to another object, etc. 0 Ignore - no
                                                         						  action taken. 1 Hangup - the
                                                         						  call is immediately terminated. 2 Goto - go to
                                                         						  an object such as a call handler, directory handler or interview handler. 3 Error - play
                                                         						  the error greeting. 4 Take a
                                                         						  message. 5 Skip greeting. 6
                                                         						  RestartGreeting 7 Transfer to
                                                         						  Alternate Contact Number 8 Route From
                                                         						  Next Call Routing Rule Default value: 4 |
| AfterMessageTargetConversation | Read/Write | String (64) | The name of the conversation used to set
                                                					 up, send, and retrieve messages. |
| AfterMessageTargetHandlerObjectId | Read/Write | String (36) | Specifies the URI of the target specified. |
| UseCallLanguage | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                                					 Connection will use the language assigned to the call. Possible values: true: Use the
                                                         						  language specified by the system call routing rule to play prompts for users. false: Do not
                                                         						  use the language specified by the system call routing rule to play prompts for
                                                         						  users. Default value: true |
| UseDefaultLanguage | Read/Write | Boolean | A flag that is dependent on the value of
                                                					 Language Field. If Language is set to Null, UseDefaultLanguage is set to
                                                					 true(1). If any language is specified, UseDefaultLanguage is set to false(0). Default value: true. |
| DispatchDelivery | Read/Write | Boolean | A flag indicating that all messages left
                                                					 for the interview handler is for dispatch delivery. Possible values:- true: Messages
                                                         						  left for interview handler is for dispatch delivery. false: Messages
                                                         						  left for interview handler is not for dispatch delivery Default value: false |
| PartitionObjectId | Read/Write | String (36) | The unique identifier of the Partition to
                                                					 which the InterviewHandler is assigned. |
| PartitionURI | Read Only | String | Specifies the partition URI. |
| InterviewQuestionsURI | Read Only | String | Specifies the URI of interview questions of
                                                					 an interview handler |
| DtmfAccessId | Read/Write | Integer | Specifies an extension number where minimum
                                                					 length can be 1 and maximum length can be 40. |

| https://<connection-server>/vmrest/languagemap |
|---|

| GET https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-
  objectid>/interviewquestions |
|---|

| <InterviewQuestions total="1">
  <InterviewQuestion>
    <InterviewHandlerObjectId>9fa58ed4-af0b-4de5-977c-
  8c080b0727c1</InterviewHandlerObjectId>
    <InterviewHandlerURI>/vmrest/handlers/interviewhandlers/9fa58ed4-af0b-4de5-977c-
  8c080b0727c1</InterviewHandlerURI>
    <QuestionNumber>1</QuestionNumber>
    <MaxMsgLength>30</MaxMsgLength>
    <StreamText>1</StreamText>
    <IsActive>true</IsActive>
  </InterviewQuestion>
</InterviewQuestions> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>/interviewquestions
Accept: application/json
Connection: Keep-alive |
|---|

| { 
 },{
"@total": "2",
"InterviewQuestion":	[
  {
    "InterviewHandlerObjectId": "99800fcc-e8df-42d3-ac3f-5117483b293e",         
    "InterviewHandlerURI": "/vmrest/handlers/interviewhandlers/99800fcc-e8df-42d3-ac3f-
    5117483b293e",
    "QuestionNumber": "1",
    "MaxMsgLength": "30",
    "StreamText": "1",
    "IsActive": "true"
  },
  {
  "InterviewHandlerObjectId": "99800fcc-e8df-42d3-ac3f-5117483b293e",
  "InterviewHandlerURI": "/vmrest/handlers/interviewhandlers/99800fcc-e8df-42d3-ac3f-
  5117483b293e",
  "QuestionNumber": "2",
  "MaxMsgLength": "30",
  "StreamText": "2",
  "IsActive": "true"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://< connection-server>/vmrest/handlers/interviewhandlers/<Interviewhandler-
  objectid>/interviewquestions/<questionnumber> |
|---|

| <InterviewQuestion>
      <InterviewHandlerObjectId>9fa58ed4-af0b-4de5-977c-
  8c080b0727c1</InterviewHandlerObjectId>
      <InterviewHandlerURI>/vmrest/handlers/interviewhandlers/9fa58ed4-af0b-4de5-977c-
  8c080b0727c1</InterviewHandlerURI>
      <QuestionNumber>2</QuestionNumber>
      <MaxMsgLength>30</MaxMsgLength>
      <StreamText>2</StreamText>
      <IsActive>true</IsActive>
  </InterviewQuestion> |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>/interviewquestions/<questionnumber>
Request Body:
<InterviewQuestion>
    <IsActive>false</IsActive>
</InterviewQuestion> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/handlers/interviewhandlers/<interviewhandler-objectid>/interviewquestions/<questionnumber>
Accept: application/json
Content-Type: application/json
Connection: Keep-alive
Request Body:
{
    "IsActive": "false"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| InterviewHandlerObjectId | Read Only | String | Object id of the parent interview handler. |
| InterviewHandlerURI | Read Only | String | URI of the parent interview handler. |
| QuestionNumber | Read Only | Integer | Specifies the question number.Questions are
                                                					 numbered from 1 to 20. |
| MaxMsgLength | Read/Write | Integer | The maximum recording length (in seconds)
                                                					 allowed for caller responses to the question. Value can range from 1 to 1200. Default value: 30 seconds |
| StreamText | Read/Write | String | Specifies the question text. Defaults to
                                                					 the index "1", "2", etc. |
| IsActive | Read/Write | Boolean | Specifies whether question is active or not Possible values: true: activate
                                                         						  question false:
                                                         						  Inactivate question Default Value: true |
| VoiceFile | Read/Write | NA | Specifies the name of the .wav file. |

| PUT https://<connectionserver>/vmrest/handlers/interviewhandlers/<interviewhandlerobjectid>/interviewquestions/
<QuestionNumber>/audio. |
|---|

| https://<connectionserver>/vmrest/handlers/interviewhandlers/<interviewhandlerobjectid>/interviewquestions/<QuestionNumber>/audio. |
|---|