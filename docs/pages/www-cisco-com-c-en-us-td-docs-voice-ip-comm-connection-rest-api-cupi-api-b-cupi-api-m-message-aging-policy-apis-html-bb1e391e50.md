---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-message-aging-policy-apis-html-bb1e391e50
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-message-aging-policy-apis.html
retrieved_at: 2026-08-17T03:49:53.792141+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API--Message Aging Policy APIs

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API--Message Aging Policy APIs

# Cisco Unity Connection Provisioning Interface (CUPI) API--Message Aging Policy APIs

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Mailbox Store API

### Mailbox Stores
                           	 Configuration

Administrator can use this APIs for creating, reading, modifying and
                                 		  deleting mailbox stores for listing,viewing, creation, selection, and deletion.
                                 		  During installation, Cisco Unity Connection automatically creates:

- A mailbox store database
                                       			 for information on voice messages (who each message was sent to,when it was
                                       			 sent, the location of the WAV file on the hard disk, and so on).

- An operating-system
                                       			 directory for voice message WAV files.

- An administrator with the
                                       			 required permissions can create up to four additional mailbox stores. Each
                                       			 additional mailbox store includes:

- Another mailbox-store
                                       			 database for information on voice messages that are saved in that mailbox
                                       			 store. The database is pre-sized for an average of approximately 40 messages
                                       			 each for 10,000 users, or about 1.25 GB. (The database application currently
                                       			 being used for Connection cannot dynamically resize a database after it is
                                       			 created.)

- Another operating-system
                                       			 directory for the voice message WAV files and other message attachments.

### Listing the
                           	 Mailbox Stores

The following is an example of
                                 		  the GET request that lists all the mailbox stores:

```
GET https://<connection-server>/vmrest/mailboxstores
```

The following is the response from the above *GET* request.

```
<MailboxStores total="1">
  <MailboxStore>
     <URI>/vmrest/mailboxstores/fd3ad7cd-805d-4727-82dd-c05dae4261c0</URI>
     <MailDatabase>UnityMbxDb1</MailDatabase>
     <Server>ucbu-aricent-vm256.cisco.com</Server>
     <ObjectId>fd3ad7cd-805d-4727-82dd-c05dae4261c0</ObjectId>
     <Mounted>true</Mounted>
     <RequiredSecurity>0</RequiredSecurity>
     <MailboxStoreType>0</MailboxStoreType>
     <DisplayName>Unity Messaging Database -1</DisplayName>
     <DbInstance>ciscounity</DbInstance>
     <Status>0</Status>
     <Undeletable>true</Undeletable>
     <LastError>0</LastError>
     <MaxSizeMB>15000</MaxSizeMB>
     <TotalSizeOfMailbox>0.0 Kilobytes</TotalSizeOfMailbox>
     <TimeAtWhichSizeCalculated>2013-04-10 22:59:23.323</TimeAtWhichSizeCalculated>
     <MailboxURI>/vmrest/mailboxstores/fd3ad7cd-805d-4727-82ddc05dae4261c0/
     mailboxes</MailboxURI>
  </MailboxStore>
</MailboxStores>
```

```
Response Code: 200
```

JSON Example

To list all mailboxstores(GET), do the following:

```
Request URI:
GET https://<connection-server>/vmrest/mailboxstores
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
  "@total": "1",
  "MailboxStore": {
     "URI": "/vmrest/mailboxstores/2668cf73-c234-4fb4-82e1-8b7299485b3c",
     "MailDatabase": "UnityMbxDb1",
     "Server": "ucbu-aricent-vm506.cisco.com",
     "ObjectId": "2668cf73-c234-4fb4-82e1-8b7299485b3c",
     "Mounted": "true",
     "RequiredSecurity": "0",
     "MailboxStoreType": "0",
     "DisplayName": "Unity Messaging Database -1",
     "DbInstance": "ciscounity",
     "Status": "0",
     "Undeletable": "true",
     "LastError": "0",
     "MaxSizeMB": "15000",
     "TotalSizeOfMailbox": "0.0 Kilobytes",
     "TimeAtWhichSizeCalculated":"2013-04-10 22:59:23.323",
     "MailboxURI": "/vmrest/mailboxstores/2668cf73-c234-4fb4-82e1-
     8b7299485b3c/mailboxes"
     }
  }
```

```
Response Code: 200
```

### Viewing the
                           	 Specific Mailbox Stores

The following is an example of
                                 		  the GET request that lists the details of specific mailbox stores represented
                                 		  by the provided value of mailbox store object ID:

```
GET https://<connection-server>/vmrest/mailboxstores /<mailboxstore-objectid>
```

The following is the response from the above *GET* request:

```
<MailboxStore>
     <URI>/vmrest/mailboxstores/fd3ad7cd-805d-4727-82dd-c05dae4261c0</URI>
     <MailDatabase>UnityMbxDb1</MailDatabase>
     <Server>ucbu-aricent-vm256.cisco.com</Server>
     <ObjectId>fd3ad7cd-805d-4727-82dd-c05dae4261c0</ObjectId>
     <Mounted>true</Mounted>
     <RequiredSecurity>0</RequiredSecurity>
     <MailboxStoreType>0</MailboxStoreType>
     <DisplayName>Unity Messaging Database -1</DisplayName>
     <DbInstance>ciscounity</DbInstance>
     <Status>0</Status>
     <Undeletable>true</Undeletable>
     <LastError>0</LastError>
     <MaxSizeMB>15000</MaxSizeMB>
     <TotalSizeOfMailbox>0.0 Kilobytes</TotalSizeOfMailbox>
     <TimeAtWhichSizeCalculated>2013-04-10 22:59:23.323</TimeAtWhichSizeCalculated>
     <MailboxURI>/vmrest/mailboxstores/fd3ad7cd-805d-4727-82ddc05dae4261c0/
     mailboxes</MailboxURI>
  </MailboxStore>
```

```
Response Code: 200
```

JSON Example

To view individual mailbox store (GET), do the following:

```
Request URI:
GET https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
     "URI": "/vmrest/mailboxstores/2668cf73-c234-4fb4-82e1-8b7299485b3c",
     "MailDatabase": "UnityMbxDb1",
     "Server": "ucbu-aricent-vm506.cisco.com",
     "ObjectId": "2668cf73-c234-4fb4-82e1-8b7299485b3c",
     "Mounted": "true",
     "RequiredSecurity": "0",
     "MailboxStoreType": "0",
     "DisplayName": "Unity Messaging Database -1",
     "DbInstance": "ciscounity",
     "Status": "0",
     "Undeletable": "true",
     "LastError": "0",
     "MaxSizeMB": "15000",
     "TotalSizeOfMailbox": "0.0 Kilobytes",
     "TimeAtWhichSizeCalculated":"2013-04-10 22:59:23.323",
     "MailboxURI": "/vmrest/mailboxstores/2668cf73-c234-4fb4-82e1-8b7299485b3c/mailboxes"
}
```

```
Response Code: 200
```

### Viewing the Number
                           	 of Mailboxes in a Mailbox Store

The following is an example of
                                 		  the GET request that lists the number of mailboxes in a mailbox store
                                 		  represented by the provided value of mailbox store object ID:

```
GET https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>/mailboxes
```

The following is the response from the above *GET* request:

```
Response Code: 200
<Mailboxes total="3"/>
```

JSON Example

To view the number of mailboxes in a mailbox store, do the following:

```
Request URI
GET https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>/mailboxes
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{
     "@total": "3"
}
```

```
Response Code: 200
```

### Creating the
                           	 Mailbox Store

The parameters that can be given
                                 		  as part of the POST Request Body are : DisplayName, MaxSizeMB,Mounted,
                                 		  Undeletable. Even If the other values such as "server" are mentioned as part of
                                 		  the request body , the values will not be used while creation and default
                                 		  values will be used. The following is an example of the POST request that
                                 		  creates a mailbox store:

```
POST https://<connection-server>/vmrest/mailboxstores
  Request Body:
  <MailboxStore>
     <DisplayName>Unity Messaging Database</DisplayName>
     <MaxSizeMB>15000</MaxSizeMB>
  </MailboxStore>
```

The following is the example of the response from the above *POST*
                                 		  request:

```
Response Code: 201
/vmrest/voicemailboxstores /2668cf73-c234-4fb4-82e1-8b7299485b3ce
```

JSON Example

To create a new mailbox store, do the following:

```
Request URI:
POST https://<connection-server>/vmrest/mailboxstores
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
     "DisplayName":"Unity Messaging Database",
     "MaxSizeMB":"15000"
}
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/voicemailboxstores /2668cf73-c234-4fb4-82e1-8b7299485b3ce
```

### Updating the
                           	 Mailbox Stores

The following is an example of
                                 		  the PUT request that allows you to update the content of the mailbox store:

```
PUT https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>
Request Body:
  <MailboxStore>
     <Mounted>false</Mounted>
  </MailboxStore>
</pre
<pre>
Response Body: 204
```

The output for this request returns the successful response code.

JSON Example

To update mounted field of mailbox store, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
     "Mounted":"false"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Deleting the
                           	 Mailbox Store

The following is an example of
                                 		  the DELETE request that deletes a specific mailbox store where you need to
                                 		  mention the mailbox store object ID:

```
DELETE https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

The output for this request returns the successful response code.

JSON Example

To delete mailbox store, do the following:

```
DELETE https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

The following chart lists all of
                                 		  the data fields:

Default Value: true

- 0: No
                                                      						  encryption.

- 1: TLS level
                                                      						  encryption.

- 2: SSL
                                                      						  encryption.

- 3: IPSec
                                                      						  encryption.

Default Value: 0

- 0: UMSS - Cisco
                                                      						  Unity Connection message store solution.

- 1: IMAP

- 2: POP3

- 3: WebDAV

- 4: MPE_WS Used
                                                      						  by the Common Calendaring Library to retrieve calendaring and meeting
                                                      						  information from the Meeting Place Express web service.

Default Value: 0

Default Value: ciscounity Status Read Only String Current
                                                						status of the mailbox store. Possible values are:

- 0: OK

- 1: Moving

- 2: MoveFailed

- 3: MoveRequested

Default Value: true

- 0: OK

- 1: UnknownError

- 2:
                                                      						  DuplicateDisplayName

- 3:
                                                      						  InternalNameError

- 4: DatabaseError

- 5:
                                                      						  InsufficientDiskSpace

- 6:
                                                      						  MailstoreNotEmpty

- 7:
                                                      						  MailstoreStillReferenced:This error is returned when deleting an mbx database
                                                      						  is still referenced by another object (user template,etc).

- 8:
                                                      						  MailstoreOverMaxSize

- 9:
                                                      						  MailstoreNotFound

- 10:
                                                      						  MailstoreUndeletable

- 11:
                                                      						  RemoteServerOffline

- 12:
                                                      						  MailstoreNotMounted

- 13:
                                                      						  InvalidRequest

- 14:
                                                      						  MailboxNotMounted

- 15:
                                                      						  MustRunOnPublisher

Default Value: 0

Default Value: 15000

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Mailbox Quota alert

### Mailbox Quota
                           	 Alert

These APIs are capable of retrieving and updating the email notification
                              		Mailbox Quota Alert text from CUC.

Acceptance criteria :

- GET API to view the "header"
                                    		  and body of the quota alert text in specified language.

- API to set the "header" and
                                    		  body of the quota alert text for specified language.

#### GET : https://
                              	 <connection-server>/vmrest/mailboxquotatexts

This API can be used by
                                 		Administrator to fetch the list of Mailbox Quota alerts that will be used as
                                 		email notification alert texts for end user. Currently, there is only one
                                 		Mailbox Quota Alert which is Warning Quota, that can be configured in different
                                 		languages. Output of this API will be:

```
<MailboxQuotaTexts total="1">

                <MailboxQuotaText>

                        <URI>/vmrest/mailboxquotatexts/da9d6130-baf7-4b8b-8aa5-1d973567d0b6</URI>

                        <ObjectId>da9d6130-baf7-4b8b-8aa5-d973567d0b6</ObjectId>

                        <Body/>

                        <DefaultBody>Your mailbox has exceeded the quota warning threshold specified by your administrator.
\n\nCurrent Usage: %CURRENTUSAGE%\nQuota Warning Threshold: %THRESHOLD%\nQuota Size Limit: %LIMIT%\n\
nPlease reduce your mailbox size by deleting few items from your mailbox.</DefaultBody>

                        <DefaultSubject>Voicemail Mailbox Quota Warning</DefaultSubject>

                        <LanguageCode>1033</LanguageCode>

                        <Subject/>

                        <UseDefault>true</UseDefault>

                       <RuleDescription>Text for Mailbox Warning Quota</RuleDescription>

               </MailboxQuotaText>

</MailboxQuotaTexts>
```

#### GET :https://
                              	 <connection-server>/vmrest/mailboxquotatexts/<mailboxQuotaTextObjectId>

This API can be used by
                                    		  Administrator to fetch the details of a particular Mailbox Quota Alert.

Output of this API will be:

```
<MailboxQuotaText>

          <URI>/vmrest/mailboxquotatexts/da9d6130-baf7-4b8b-8aa5-1d973567d0b6</URI>

          <ObjectId>da9d6130-baf7-4b8b-8aa5-1d973567d0b6</ObjectId>

          <Body/>

          <DefaultBody>Your mailbox has exceeded the quota warning threshold specified by your administrator.\n\nCurrent Usage: %CURRENTUSAGE%\nQuota 
Warning Threshold: %THRESHOLD%\nQuota Size Limit: %LIMIT%\n\nPlease reduce your mailbox size by deleting few items 
from your mailbox.</DefaultBody>

          <DefaultSubject>Voicemail Mailbox Quota Warning</DefaultSubject>

          <LanguageCode>1033</LanguageCode>

          <Subject/>

          <UseDefault>true</UseDefault>

          <RuleDescription>Text for Mailbox Warning Quota</RuleDescription>

</MailboxQuotaText>
```

#### PUT : https://
                              	 <connection-server>/vmrest/mailboxquotatexts/<mailboxQuotaTextObjectId>

This API can be used by an
                                    		  administrator to modify the subject line, body and Use Default flag for the
                                    		  email notification alert for the end users. If an administrator updates
                                    		  "UseDefault" option to false and if "Subject" and "Body" (customized subject
                                    		  and body texts) of the Alert are null in the database or in input XML, then it
                                    		  is mandatory to provide both of them. Input will be an XML with following data
                                    		  :

```
<MailboxQuotaText>

           <Body>changed body content</Body>

           <Subject>Changed subject line</Subject>

           <UseDefault>false</UseDefault>

</MailboxQuotaText>
```

```
Output: HTTP response code : 204
```

#### Explanation of
                              	 Data Fields

The following chart lists all of
                                    		  the data fields:

Values can be:

- false -0

- true -1

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Message Aging Policy

### Message Aging
                           	 Policy

In Cisco Unity Connection, the Message Aging Policies ensures that the
                                 		  hard disk where voice messages are stored does not get filled up. Each policy
                                 		  allows you to specify message aging rules to automatically:

- Move new messages to the
                                       			 Saved Items folder after a specified number of days.

- Move read messages to the
                                       			 Deleted Items folder after a specified number of days.

- Permanently delete
                                       			 messages in the Deleted Items folder after a specified number of days. In the
                                       			 Default System Policy message aging policy, this is the only rule that is
                                       			 enabled.

- Based on the age of the
                                       			 messages, permanently delete secure messages that have been touched in any way
                                       			 (for example by saving, deleting, or opening but then saving messages as new).

- Based on the age of the
                                       			 messages, permanently delete all secure messages regardless of whether users
                                       			 have listened to or touched the messages in any way.

- Default System Policy

- Do Not Age Messages

Administrator can use this API to create/update/delete/fetch the
                                 		  message aging policy. Various attributes of message aging policy can also be
                                 		  updated using this API.

#### Listing the
                              	 Message Aging Policies

The following is an example of
                                    		  the GET request that lists all the message aging policies:

```
GET https://<connection-server>/vmrest/messageagingpolicies
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<MessageAgingPolicies total="2">
  <MessageAgingPolicy>
    <URI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-ce14ede90ac0</URI>
    <ObjectId>0f02be4e-5d70-4a1d-b182-ce14ede90ac0</ObjectId>
    <Enabled>true</Enabled>
    <DisplayName>Default System Policy</DisplayName>
    <MessageAgingRuleURI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0/messageagingrules</MessageAgingRuleURI>
  </MessageAgingPolicy>
  <MessageAgingPolicy>
    <URI>/vmrest/messageagingpolicies/7f762fe2-ef33-4664-afb9-bd47c2ef7e41</URI>
    <ObjectId>7f762fe2-ef33-4664-afb9-bd47c2ef7e41</ObjectId>
    <Enabled>false</Enabled>
    <DisplayName>Do Not Age Messages</DisplayName>
    <MessageAgingRuleURI>/vmrest/messageagingpolicies/7f762fe2-ef33-4664-afb9-
    bd47c2ef7e41/messageagingrules</MessageAgingRuleURI>
  </MessageAgingPolicy>
</MessageAgingPolicies>
```

```
Response Code: 200
```

JSON Example

To list all the message aging policies, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/messageagingpolicies
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total":"2"
  "MessageAgingPolicy":[
  {
    "URI":"/vmrest/messageagingpolicies/adac77f4-8a77-430d-8836-0fc9aef3fef5"
    "ObjectId":"adac77f4-8a77-430d-8836-0fc9aef3fef5"
    "Enabled":"true"
    "DisplayName":"Default System Policy"
    "MessageAgingRuleURI":"/vmrest/messageagingpolicies/adac77f4-8a77-430d-8836-
    0fc9aef3fef5/messageagingrules"
  }
  {
    "URI":"/vmrest/messageagingpolicies/2e02eca6-270b-4b7f-a153-f03ea74d403d"
    "ObjectId":"2e02eca6-270b-4b7f-a153-f03ea74d403d"
    "Enabled":"false"
    "DisplayName":"Do Not Age Messages"
    "MessageAgingRuleURI":"/vmrest/messageagingpolicies/2e02eca6-270b-4b7f-a153-
    f03ea74d403d/messageagingrules"
  }
  ]
}
```

```
Response Code: 200
```

#### Viewing the
                              	 Specific Message Aging Policy

The following is an example of
                                    		  the GET request that lists the details of specific message aging policy
                                    		  represented by the provided value of object ID:

```
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-id>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<MessageAgingPolicy>
    <URI>/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c</URI>
    <ObjectId>3f3f9297-e1eb-46a5-bbdf-d86298e2531c</ObjectId>
    <Enabled>true</Enabled>
    <DisplayName>Texoma_Message_Policy</DisplayName>
    <MessageAgingRuleURI>/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-
d86298e2531c/messageagingrules</MessageAgingRuleURI>
</MessageAgingPolicy>
```

```
Response Code: 200
```

JSON Example

To list details of an individual message aging policy, do the
                                    		  following:

```
Request URI:
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-id>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "URI":"/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c"
    "ObjectId":"3f3f9297-e1eb-46a5-bbdf-d86298e2531c"
    "Enabled":"true"
    "DisplayName":"Default System Policy"
    "MessageAgingRuleURI":"/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-
d86298e2531c/messageagingrules"
}
```

```
Response Code: 200
```

#### Creating a
                              	 Message Aging Policy

Example 1: The following is an example of the POST request that
                                    		  creates a message aging policy:

```
*POST https://<connection-server>/vmrest/messageagingpolicies
Request Body:
<MessageAgingPolicy>
    <DisplayName>Texoma_Message_Policy</DisplayName>
</MessageAgingPolicy>
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c
```

JSON Example

To create new message aging policy, do the following:

```
Request URI:
POST https://<connection-server>/vmrest/messageagingpolicies
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "DisplayName":"Texoma_Message_Policy"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c
```

Example 2: The following is the example of the create a new
                                    		  message aging policy with some more parameter

```
*POST https://<connection-server>/vmrest/messageagingpolicies
Request Body:
<MessageAgingPolicy>
    <DisplayName>Texoma_New_Message_Policy</DisplayName>
    <Enabled>false</Enabled>
</MessageAgingPolicy>
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c
```

#### Updating a
                              	 Message Aging Policy Parameters

The following is an example of
                                    		  the PUT request that allows you to update the display name of message aging
                                    		  policy:

```
*PUT https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-id>
Request Body:
<MessageAgingPolicy>
    <DisplayName>Texoma_Message_Policy_2</DisplayName>
</MessageAgingPolicy>
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update the display name of message aging policy, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-id>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "DisplayName":"Texoma_Message_Policy_2"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Deleting a
                              	 Message Aging Policy

The following is an example of
                                    		  the DELETE request that deletes a message aging policy with a valid object ID:

```
DELETE https://<connection-server>/vmrest/messageagingpolicies<messageagingpolicyobject-id>
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To delete a message aging policy with a valid object ID, do the
                                    		  following:

```
DELETE https://<connection-server>/vmrest/messageagingpolicies<messageagingpolicyobject-id>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

The following chart lists all of
                                    		  the data fields:

Maximum length: 64

Possible values:

- true: If message
                                                         						  aging rules to be enforced.

- false: If
                                                         						  message aging rules to be ignored.

Default value is true.

Maximum length : 36

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Message Aging Rules

### Message Aging
                           	 Rules

Administrator can use this API to
                                 		  update/ fetch the message aging rules. Various attributes of message aging
                                 		  rules can also be updated using this API.

#### Listing the
                              	 Message Aging Rules

The following is an example of
                                    		  the GET request that lists all the message aging rules:

```
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-Id>/messageagingrules
```

The following is the response from the above *GET* request:

```
<MessageAgingRules total="2">
  <MessageAgingRule>
    <URI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0/messageagingrules/6951ad4c-a16c-4bf2-b61a-300bbf24519d</URI>
    <MessageAgingPolicyObjectId>0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyURI>
    <ObjectId>6951ad4c-a16c-4bf2-b61a-300bbf24519d</ObjectId>
    <Days>7</Days>
    <Enabled>true</Enabled>
    <Secure>false</Secure>
    <SendNotification>true</SendNotification>
    <NotificationDays>3</NotificationDays>
    <RuleDescription>Move Saved Messages to the Deleted Items</RuleDescription>
  </MessageAgingRule>
  <MessageAgingRule>
    <URI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0/messageagingrules/8792058b-cf27-4c10-8ac1-e903b8d18065</URI>
    <MessageAgingPolicyObjectId>0f02be4e-5d70-4a1d-b182-ce14ede90ac0</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyURI>
    <ObjectId>8792058b-cf27-4c10-8ac1-e903b8d18065</ObjectId>
    <Days>15</Days>
    <Enabled>true</Enabled>
    <Secure>false</Secure>
    <SendNotification>false</SendNotification>
    <NotificationDays>3</NotificationDays>
    <RuleDescription>Permanently Delete Messages in the Deleted Items </RuleDescription>
  </MessageAgingRule>
</MessageAgingRules>
```

```
Response Code: 200
```

JSON Example

To list all message aging rules, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-Id>/messageagingrules
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{ 
  "@total":"2"
  "MessageAgingRule":
  [
  {
    "URI":"/vmrest/messageagingpolicies/2fcb9e34-bb41-41e3-b212-
    1bff3e1d93ed/messageagingrules/230f8ab1-1dba-45db-8e2c-dbd22cad718a"
    "MessageAgingPolicyObjectId":"2fcb9e34-bb41-41e3-b212-    1bff3e1d93ed"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/2fcb9e34-bb41-41e3-b212-
    1bff3e1d93ed"
    "ObjectId":"230f8ab1-1dba-45db-8e2c-dbd22cad718a"
    "Days":"30"
    "Enabled":"true"
    "Secure":"true"
    "SendNotification":"false"
    "NotificationDays":"3"
    "RuleDescription":"Permanently Delete Secure Touched Messages "
  }
  {
    "URI":"/vmrest/messageagingpolicies/2fcb9e34-bb41-41e3-b212-
    1bff3e1d93ed/messageagingrules/b0bc585c-7704-4f36-b7f6-8e8319d89da3"
    "MessageAgingPolicyObjectId":"2fcb9e34-bb41-41e3-b212-1bff3e1d93ed"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/2fcb9e34-bb41-41e3-b212-
    1bff3e1d93ed"
    "ObjectId":"b0bc585c-7704-4f36-b7f6-8e8319d89da3"
    "Days":"60"
    "Enabled":"false"
    "Secure":"true"
    "SendNotification":"false"
    "NotificationDays":"3"
    "RuleDescription":"Permanently Delete All Secure Messages "
  }
  ]
}
```

```
Response Code: 200
```

#### Viewing the
                              	 Specific Message Aging Rule

The following is an example of
                                    		  the GET request that lists the details of specific message aging rule
                                    		  represented by the provided value of object ID:

```
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-
  Id>/messageagingrules/<messageagingruleobject-Id>
```

The following is the response from the above *GET* request:

```
<MessageAgingRule>
    <URI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0/messageagingrules/c160becb-0042-441e-a021-4bb4aeb05da4</URI>
    <MessageAgingPolicyObjectId>0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyURI>
    <ObjectId>c160becb-0042-441e-a021-4bb4aeb05da4</ObjectId>
    <Days>30</Days>
    <Enabled>false</Enabled>
    <Secure>true</Secure>
    <SendNotification>false</SendNotification>
    <NotificationDays>3</NotificationDays>
    <RuleDescription>Permanently Delete Secure Touched Messages </RuleDescription>
</MessageAgingRule>
```

```
Response Code: 200
```

JSON Example

To list details of an individual message aging rule, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-
Id>/messageagingrules/<messageagingruleobject-Id>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
    "URI":"/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
ce14ede90ac0/messageagingrules/c160becb-0042-441e-a021-4bb4aeb05da4"
    "MessageAgingPolicyObjectId":"0f02be4e-5d70-4a1d-b182-ce14ede90ac0"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
ce14ede90ac0"
    "ObjectId":"c160becb-0042-441e-a021-4bb4aeb05da4"
    "Days":"60"
    "Enabled":"false"
    "Secure":"true"
    "SendNotification":"false"
    "NotificationDays":"3"
    "RuleDescription":"Permanently Delete Secure Touched Messages"
}
```

```
Response Code: 200
```

#### Updating a
                              	 Message Aging Rule

The following is an example of
                                    		  the PUT request that allows you to update the days parameter of enabled message
                                    		  aging rule:

```
PUT https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-Id>/messageagingrules/<messageagingruleobject-Id>
Request Body:
<MessageAgingRule>
    <Days>25</Days>
</MessageAgingRule>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update the days parameter of enabled message aging rule, do the
                                    		  following:

```
PUT https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-Id>/messageagingrules/<messageagingruleobject-Id>
Accept : application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "Days":"25"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

The following chart lists all of
                                    		  the data fields:

Default Value: 0 Values:

- 0: Soft Delete

- 1: Hard Delete

- 2: ToSaved

Values : true or false Default Value: true.

Default Value: 10 Values:

- 10:
                                                         						  MoveSeenToDeleted

- 11:
                                                         						  HardDeleteDeleted

- 12:
                                                         						  HardDeleteSecureTouched

- 13:
                                                         						  HardDeleteAllSecure

- 14:
                                                         						  MoveNewToSaved

Default Value: 0 Value:

- 0:
                                                         						  ModificationTime

- 1: ArrivalTime

Range: 0 to 365. Default Value: 3.

Values: true or false. Default Value: false.

Default Value: 3

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Message Aging Text

### Message Aging
                           	 Text

Administrator can use this API to create/update/delete/fetch the message
                              		aging text.Various attributes of message aging text can also be updated using
                              		this API.

#### Listing the
                              	 Message Aging Texts

The following is an example of
                                    		  the GET request that lists all the message aging texts:

```
GET https://<connection-server>/vmrest/messageagingtexts
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<MessageAgingTexts total="1">
  <MessageAgingText>
     <URI>/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d</URI>
     <ObjectId>0220cac9-6df0-48c2-929f-e38d7ff88e3d</ObjectId>
     <LanguageCode>1033</LanguageCode>
     <DefaultSubject>Your message from %SENDER% will be moved to the Saved Messages
    folder in %DAYSUNTIL% day(s).</DefaultSubject>
     <Subject/>
     <DefaultBody>Your message from %SENDER%, which was received on
     %MODIFICATIONTIME%, will be moved to the Saved Messages folder in %DAYSUNTIL%
     day(s).</DefaultBody>
     <Body/>
     <UseDefault>false</UseDefault>
     <RuleDescription>Text for Move New Messages to the Saved Messages Folder
   Rule</RuleDescription>
  </MessageAgingText>
<MessageAgingTexts>
```

```
Response Code: 200
```

JSON Example

To list all the message aging texts, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/messageagingtexts
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
     "@total":"1"
     "MessageAgingText":[
{
     "URI": "/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "ObjectId": "0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "LanguageCode": "1033",
     "DefaultSubject": "Your message from %SENDER% will be moved to the Saved Messages
   folder in %DAYSUNTIL% day(s).",
     "Subject": [],
     "DefaultBody": "Your message from %SENDER%, which was received on
   %MODIFICATIONTIME%, will be moved to the Saved Messages folder in %DAYSUNTIL% day(s).",
     "Body": [],
     "UseDefault": "false",
     "RuleDescription": "Text for Move New Messages to the Saved Messages Folder Rule"
  }
  ]
}
```

```
Response Code: 200
```

JSON Example

To list all the message aging texts, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/messageagingtexts
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
     "@total":"1"
     "MessageAgingText":[
{
     "URI": "/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "ObjectId": "0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "LanguageCode": "1033",
     "DefaultSubject": "Your message from %SENDER% will be moved to the Saved Messages
   folder in %DAYSUNTIL% day(s).",
     "Subject": [],
     "DefaultBody": "Your message from %SENDER%, which was received on
   %MODIFICATIONTIME%, will be moved to the Saved Messages folder in %DAYSUNTIL% day(s).",
     "Body": [],
     "UseDefault": "false",
     "RuleDescription": "Text for Move New Messages to the Saved Messages Folder Rule"
  }
  ]
}
```

```
Response Code: 200
```

#### Viewing the
                              	 Specific Message Aging Text

The following is an example of
                                    		  the GET request that lists the details of specific message aging policy
                                    		  represented by the provided value of object ID:

```
GET https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobject-id>
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<MessageAgingText>
     <URI>/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d</URI>
     <ObjectId>0220cac9-6df0-48c2-929f-e38d7ff88e3d</ObjectId>
     <LanguageCode>1034</LanguageCode>
     <DefaultSubject>Your message from %SENDER% will be moved to the Saved Messages folder in
   %DAYSUNTIL% day(s).</DefaultSubject>
     <Subject/>
     <DefaultBody>Your message from %SENDER%, which was received on %MODIFICATIONTIME%,
   will be moved to the Saved Messages folder in %DAYSUNTIL% day(s).</DefaultBody>
     <Body/>
     <UseDefault>true</UseDefault>
     <RuleDescription>Text for Move New Messages to the Saved Messages Folder
   Rule</RuleDescription>
</MessageAgingText>
```

```
Response Code: 200
```

JSON Example

To list details of an individual message aging text, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobject-id>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
     "URI": "/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "ObjectId": "0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "LanguageCode": "1034",
     "DefaultSubject": "Your message from %SENDER% will be moved to the Saved Messages folder in
   %DAYSUNTIL% day(s).",
     "Subject": [],
     "DefaultBody": "Your message from %SENDER%, which was received on %MODIFICATIONTIME%,
   will be moved to the Saved Messages folder in %DAYSUNTIL% day(s).",
    "Body": [],
    "UseDefault": "true",
    "RuleDescription": "Text for Move New Messages to the Saved Messages Folder Rule"
}
```

```
Response Code: 200
```

#### Updating a Message
                              	 Aging Text

Example 1: Update UseDefault Parameter

The following is an example of the PUT request that allows you to
                                    		  update the parameters of message aging text:

```
PUT https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobjectid>
Request Body:
<MessageAgingText>
     <UseDefault>Message Aging Text</UseDefault>
</MessageAgingText>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update the parameter of message aging text, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobjectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
     "UseDefault":"Message Aging Text"
}
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: Update Subject and Body of Message Aging Text

The following is an example of the PUT request that allows you to
                                    		  update the parameters of message aging text:

```
PUT https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobjectid>
Request Body:
<MessageAgingText>
     <UseDefault>false</UseDefault>
     <Subject>Message aging text</Subject>
     <Body>Message aging Text</Body>
</MessageAgingText>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update the subject and body of message aging text, do the
                                    		  following:

```
Request URI:
PUT https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobjectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
     "UseDefault": "False",
     "Subject": "Message Aging test",
     "Body": "Message Aging Text"
}
The following is the response from the above *PUT* request and the actual response will depend upon the information given by you:
<pre>
Response Code: 204
```

#### Explanation of
                              	 Data Fields

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Message Expiration

### Message
                           	 Expiration

Administrator can use this API to set number of days after which message
                              		will be expired and hard deleted from the system. Message Expiration value is
                              		applicable for both audio as well as video messages.

### Fetching Message
                           	 Expiration field value

The following is an example of
                                 		  the GET request to fetch Message Expiration field value of audio and video
                                 		  messages:

```
GET https://<connection-server>/vmrest/messageexpirations
```

The following is the response from the above *GET* request:

```
<MessageExpirations total="1">
<MessageExpiration>
<URI>/vmrest/messageexpirations/72269af8-7376-48d2-bf23-9abf6e98b303</URI>
<ObjectId>72269af8-7376-48d2-bf23-9abf6e98b303</ObjectId>
<Enabled>false</Enabled>
<MaximumAgeDays>180</MaximumAgeDays>
<MaxVideoMsgAgeDays>30</MaxVideoMsgAgeDays>
</MessageExpiration>
</MessageExpirations>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/messageexpirations
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request:

```
{
   "@total": "1",
   "MessageExpiration":    {
      "URI": "/vmrest/messageexpirations/72269af8-7376-48d2-bf23-9abf6e98b303",
      "ObjectId": "72269af8-7376-48d2-bf23-9abf6e98b303",
      "Enabled": "true",
      "MaximumAgeDays": "180",
      "MaxVideoMsgAgeDays": "30"
   }
}
```

```
Response Code: 200
```

### Enabling and
                           	 Updating Message Expiration field value

The following is an example of
                                 		  the PUT request that allows you to enable message expiration and update the
                                 		  number of days for Message Expiration of audio and video messages:

```
PUT https://<connection-server>/vmrest/messageexpirations/<messageexpirationobjectid>
Request Body:
<MessageExpiration>
<Enabled>true</Enabled>
<MaximumAgeDays>23</MaximumAgeDays>
<MaxVideoMsgAgeDays>11</MaxVideoMsgAgeDays>
</MessageExpiration>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/messageexpirations/<messageexpirationobjectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
      "Enabled": "true",
      "MaximumAgeDays": "55",
      "MaxVideoMsgAgeDays": "44"
}
```

The following is the response from the above *PUT* request:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

The following chart lists all of
                                 		  the data fields:

Values can be:

- false - Message
                                                      						  Expiration is not applicable.

- true - Message
                                                      						  Expiration is applicable.

Default Value - false

- Range - 1-999
                                                      						  Days

Default Value - 180

Note: It is recommended that the number of days entered in
                                                						MaxVideoMsgAgeDays should be less than the number of days entered in
                                                						MaximumAgeDays field.

- Range - 1-999
                                                      						  Days

Default Value - 30

| GET https://<connection-server>/vmrest/mailboxstores |
|---|

| <MailboxStores total="1">
  <MailboxStore>
     <URI>/vmrest/mailboxstores/fd3ad7cd-805d-4727-82dd-c05dae4261c0</URI>
     <MailDatabase>UnityMbxDb1</MailDatabase>
     <Server>ucbu-aricent-vm256.cisco.com</Server>
     <ObjectId>fd3ad7cd-805d-4727-82dd-c05dae4261c0</ObjectId>
     <Mounted>true</Mounted>
     <RequiredSecurity>0</RequiredSecurity>
     <MailboxStoreType>0</MailboxStoreType>
     <DisplayName>Unity Messaging Database -1</DisplayName>
     <DbInstance>ciscounity</DbInstance>
     <Status>0</Status>
     <Undeletable>true</Undeletable>
     <LastError>0</LastError>
     <MaxSizeMB>15000</MaxSizeMB>
     <TotalSizeOfMailbox>0.0 Kilobytes</TotalSizeOfMailbox>
     <TimeAtWhichSizeCalculated>2013-04-10 22:59:23.323</TimeAtWhichSizeCalculated>
     <MailboxURI>/vmrest/mailboxstores/fd3ad7cd-805d-4727-82ddc05dae4261c0/
     mailboxes</MailboxURI>
  </MailboxStore>
</MailboxStores> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/mailboxstores
Accept: application /json
Connection: keep-alive |
|---|

| {
  "@total": "1",
  "MailboxStore": {
     "URI": "/vmrest/mailboxstores/2668cf73-c234-4fb4-82e1-8b7299485b3c",
     "MailDatabase": "UnityMbxDb1",
     "Server": "ucbu-aricent-vm506.cisco.com",
     "ObjectId": "2668cf73-c234-4fb4-82e1-8b7299485b3c",
     "Mounted": "true",
     "RequiredSecurity": "0",
     "MailboxStoreType": "0",
     "DisplayName": "Unity Messaging Database -1",
     "DbInstance": "ciscounity",
     "Status": "0",
     "Undeletable": "true",
     "LastError": "0",
     "MaxSizeMB": "15000",
     "TotalSizeOfMailbox": "0.0 Kilobytes",
     "TimeAtWhichSizeCalculated":"2013-04-10 22:59:23.323",
     "MailboxURI": "/vmrest/mailboxstores/2668cf73-c234-4fb4-82e1-
     8b7299485b3c/mailboxes"
     }
  } |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/mailboxstores /<mailboxstore-objectid> |
|---|

| <MailboxStore>
     <URI>/vmrest/mailboxstores/fd3ad7cd-805d-4727-82dd-c05dae4261c0</URI>
     <MailDatabase>UnityMbxDb1</MailDatabase>
     <Server>ucbu-aricent-vm256.cisco.com</Server>
     <ObjectId>fd3ad7cd-805d-4727-82dd-c05dae4261c0</ObjectId>
     <Mounted>true</Mounted>
     <RequiredSecurity>0</RequiredSecurity>
     <MailboxStoreType>0</MailboxStoreType>
     <DisplayName>Unity Messaging Database -1</DisplayName>
     <DbInstance>ciscounity</DbInstance>
     <Status>0</Status>
     <Undeletable>true</Undeletable>
     <LastError>0</LastError>
     <MaxSizeMB>15000</MaxSizeMB>
     <TotalSizeOfMailbox>0.0 Kilobytes</TotalSizeOfMailbox>
     <TimeAtWhichSizeCalculated>2013-04-10 22:59:23.323</TimeAtWhichSizeCalculated>
     <MailboxURI>/vmrest/mailboxstores/fd3ad7cd-805d-4727-82ddc05dae4261c0/
     mailboxes</MailboxURI>
  </MailboxStore> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>
Accept: application/json
Connection: keep-alive |
|---|

| {
     "URI": "/vmrest/mailboxstores/2668cf73-c234-4fb4-82e1-8b7299485b3c",
     "MailDatabase": "UnityMbxDb1",
     "Server": "ucbu-aricent-vm506.cisco.com",
     "ObjectId": "2668cf73-c234-4fb4-82e1-8b7299485b3c",
     "Mounted": "true",
     "RequiredSecurity": "0",
     "MailboxStoreType": "0",
     "DisplayName": "Unity Messaging Database -1",
     "DbInstance": "ciscounity",
     "Status": "0",
     "Undeletable": "true",
     "LastError": "0",
     "MaxSizeMB": "15000",
     "TotalSizeOfMailbox": "0.0 Kilobytes",
     "TimeAtWhichSizeCalculated":"2013-04-10 22:59:23.323",
     "MailboxURI": "/vmrest/mailboxstores/2668cf73-c234-4fb4-82e1-8b7299485b3c/mailboxes"
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>/mailboxes |
|---|

| Response Code: 200
<Mailboxes total="3"/> |
|---|

| Request URI
GET https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>/mailboxes
Accept: application/json
Connection: keep-alive |
|---|

| {
     "@total": "3"
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/mailboxstores
  Request Body:
  <MailboxStore>
     <DisplayName>Unity Messaging Database</DisplayName>
     <MaxSizeMB>15000</MaxSizeMB>
  </MailboxStore> |
|---|

| Response Code: 201
/vmrest/voicemailboxstores /2668cf73-c234-4fb4-82e1-8b7299485b3ce |
|---|

| Request URI:
POST https://<connection-server>/vmrest/mailboxstores
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
     "DisplayName":"Unity Messaging Database",
     "MaxSizeMB":"15000"
} |
|---|

| Response Code: 201
/vmrest/voicemailboxstores /2668cf73-c234-4fb4-82e1-8b7299485b3ce |
|---|

| PUT https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>
Request Body:
  <MailboxStore>
     <Mounted>false</Mounted>
  </MailboxStore>
</pre
<pre>
Response Body: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
     "Mounted":"false"
} |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/mailboxstores/<mailboxstore-objectid>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| Parameter | Data Type | Operations | Description |
|---|---|---|---|
| URI | String | Read Only | The URI of the mailbox store. |
| MailDatabase | String (512) | Read Only | The name of the mailbox database,such as
                                             					 "UnityMbxDb1". For external IMAP mailstores this value will be NULL. |
| Server | String (256) | Read Only | The name of the server on which the mailbox
                                             					 store resides. |
| ObjectId | String (36) | Read Only | A globally unique, system-generated
                                             					 identifier for a MailboxStore object. |
| Mounted | Boolean | Read/Write | A flag indicating whether the mailbox store
                                             					 is mounted. You should check this setting before accessing the mailbox store
                                             					 database. Tools can set it to denote that a mailbox store is offline when
                                             					 offline database maintenance needs to be performed. Default Value: true |
| RequiredSecurity | String | Read Only | The method of encryption that Cisco Unity
                                             					 Connection will use on a mailbox store connection. Possible values are: 0: No
                                                      						  encryption. 1: TLS level
                                                      						  encryption. 2: SSL
                                                      						  encryption. 3: IPSec
                                                      						  encryption. Default Value: 0 |
| MailboxStoreType | String | Read Only | The type of mailbox store (e.g.,UMSS).
                                             					 Possible values are: 0: UMSS - Cisco
                                                      						  Unity Connection message store solution. 1: IMAP 2: POP3 3: WebDAV 4: MPE_WS Used
                                                      						  by the Common Calendaring Library to retrieve calendaring and meeting
                                                      						  information from the Meeting Place Express web service. Default Value: 0 |
| DisplayName | String (64) | Read/Write | A descriptive name for the message Store. |
| DbInstance | String (256) | Read Only | The name of the dbinstance on which the
                                             					 mailbox store resides. Default Value: ciscounity Status Read Only String Current
                                                						status of the mailbox store. Possible values are: 0: OK 1: Moving 2: MoveFailed 3: MoveRequested |
| Undeletable | Boolean | Read/Write | A flag indicating whether this mailbox
                                             					 store can be deleted. It is used to prevent deletion of factory defaults. Default Value: true |
| LastError | String | Read Only | Last error result from a mailbox store
                                             					 maintenance action, that is create or delete. Possible values are: 0: OK 1: UnknownError 2:
                                                      						  DuplicateDisplayName 3:
                                                      						  InternalNameError 4: DatabaseError 5:
                                                      						  InsufficientDiskSpace 6:
                                                      						  MailstoreNotEmpty 7:
                                                      						  MailstoreStillReferenced:This error is returned when deleting an mbx database
                                                      						  is still referenced by another object (user template,etc). 8:
                                                      						  MailstoreOverMaxSize 9:
                                                      						  MailstoreNotFound 10:
                                                      						  MailstoreUndeletable 11:
                                                      						  RemoteServerOffline 12:
                                                      						  MailstoreNotMounted 13:
                                                      						  InvalidRequest 14:
                                                      						  MailboxNotMounted 15:
                                                      						  MustRunOnPublisher Default Value: 0 |
| MaxSizeMB | Integer | Read/Write | This is the max size in MB for the mailbox
                                             					 store. The range can vary from 1 to 2147483647. Default Value: 15000 |
| TotalSizeOfMailbox | String | Read Only | Total Size of the voicemail messages and
                                             					 the mailbox attachments in the mailbox store. |
| TimeAtWhichSizeCalculated | String | Read Only | Time at which the total size of mailbox
                                             					 store was calculated. |
| MailboxesURI | String | Read Only | The URI of the mailboxes. |

| <MailboxQuotaTexts total="1">

                <MailboxQuotaText>

                        <URI>/vmrest/mailboxquotatexts/da9d6130-baf7-4b8b-8aa5-1d973567d0b6</URI>

                        <ObjectId>da9d6130-baf7-4b8b-8aa5-d973567d0b6</ObjectId>

                        <Body/>

                        <DefaultBody>Your mailbox has exceeded the quota warning threshold specified by your administrator.
\n\nCurrent Usage: %CURRENTUSAGE%\nQuota Warning Threshold: %THRESHOLD%\nQuota Size Limit: %LIMIT%\n\
nPlease reduce your mailbox size by deleting few items from your mailbox.</DefaultBody>

                        <DefaultSubject>Voicemail Mailbox Quota Warning</DefaultSubject>

                        <LanguageCode>1033</LanguageCode>

                        <Subject/>

                        <UseDefault>true</UseDefault>

                       <RuleDescription>Text for Mailbox Warning Quota</RuleDescription>

               </MailboxQuotaText>

</MailboxQuotaTexts> |
|---|

| <MailboxQuotaText>

          <URI>/vmrest/mailboxquotatexts/da9d6130-baf7-4b8b-8aa5-1d973567d0b6</URI>

          <ObjectId>da9d6130-baf7-4b8b-8aa5-1d973567d0b6</ObjectId>

          <Body/>

          <DefaultBody>Your mailbox has exceeded the quota warning threshold specified by your administrator.\n\nCurrent Usage: %CURRENTUSAGE%\nQuota 
Warning Threshold: %THRESHOLD%\nQuota Size Limit: %LIMIT%\n\nPlease reduce your mailbox size by deleting few items 
from your mailbox.</DefaultBody>

          <DefaultSubject>Voicemail Mailbox Quota Warning</DefaultSubject>

          <LanguageCode>1033</LanguageCode>

          <Subject/>

          <UseDefault>true</UseDefault>

          <RuleDescription>Text for Mailbox Warning Quota</RuleDescription>

</MailboxQuotaText> |
|---|

| <MailboxQuotaText>

           <Body>changed body content</Body>

           <Subject>Changed subject line</Subject>

           <UseDefault>false</UseDefault>

</MailboxQuotaText> |
|---|

| Output: HTTP response code : 204 |
|---|

| Parameter | Data Type | Operations | Description |
|---|---|---|---|
| URI | String | Read Only | URI of Mailbox Quota alert |
| ObjectId | Char (36) | Read Only | Acts as a primary key for the API. The
                                                					 ObjectID is a unique system-generated identifier for a Mailbox Quota Alert
                                                					 object. |
| Body | String | Read/Write | Customized body text for Mailbox Quota
                                                					 Alert. |
| DefaultBody | String | Read Only | Default body text for the Mailbox Quota
                                                					 Alert |
| DefaultSubject | String | Read Only | Default subject line for Mailbox Quota
                                                					 Alert |
| LanguageCode | Integer | Read/Write | Specified the language code in which the
                                                					 alert will be displayed |
| Subject | String | Read/Write | Customized subject line for Mailbox Quota
                                                					 Alert |
| UseDefault | Boolean | Read/Write | Specify that whether DefaultSubject and
                                                					 DefaultBody is used or not. Values can be: false -0 true -1 |
| RuleDescription | String | Read Only | Specified the type of Mailbox Quota Alert |

| Note | There are total numbers of 2 Default Message Aging Policies: Default System Policy Do Not Age Messages |
|---|---|

| GET https://<connection-server>/vmrest/messageagingpolicies |
|---|

| <MessageAgingPolicies total="2">
  <MessageAgingPolicy>
    <URI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-ce14ede90ac0</URI>
    <ObjectId>0f02be4e-5d70-4a1d-b182-ce14ede90ac0</ObjectId>
    <Enabled>true</Enabled>
    <DisplayName>Default System Policy</DisplayName>
    <MessageAgingRuleURI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0/messageagingrules</MessageAgingRuleURI>
  </MessageAgingPolicy>
  <MessageAgingPolicy>
    <URI>/vmrest/messageagingpolicies/7f762fe2-ef33-4664-afb9-bd47c2ef7e41</URI>
    <ObjectId>7f762fe2-ef33-4664-afb9-bd47c2ef7e41</ObjectId>
    <Enabled>false</Enabled>
    <DisplayName>Do Not Age Messages</DisplayName>
    <MessageAgingRuleURI>/vmrest/messageagingpolicies/7f762fe2-ef33-4664-afb9-
    bd47c2ef7e41/messageagingrules</MessageAgingRuleURI>
  </MessageAgingPolicy>
</MessageAgingPolicies> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/messageagingpolicies
Accept: application/json
Connection: keep-alive |
|---|

| {
  "@total":"2"
  "MessageAgingPolicy":[
  {
    "URI":"/vmrest/messageagingpolicies/adac77f4-8a77-430d-8836-0fc9aef3fef5"
    "ObjectId":"adac77f4-8a77-430d-8836-0fc9aef3fef5"
    "Enabled":"true"
    "DisplayName":"Default System Policy"
    "MessageAgingRuleURI":"/vmrest/messageagingpolicies/adac77f4-8a77-430d-8836-
    0fc9aef3fef5/messageagingrules"
  }
  {
    "URI":"/vmrest/messageagingpolicies/2e02eca6-270b-4b7f-a153-f03ea74d403d"
    "ObjectId":"2e02eca6-270b-4b7f-a153-f03ea74d403d"
    "Enabled":"false"
    "DisplayName":"Do Not Age Messages"
    "MessageAgingRuleURI":"/vmrest/messageagingpolicies/2e02eca6-270b-4b7f-a153-
    f03ea74d403d/messageagingrules"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-id> |
|---|

| <MessageAgingPolicy>
    <URI>/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c</URI>
    <ObjectId>3f3f9297-e1eb-46a5-bbdf-d86298e2531c</ObjectId>
    <Enabled>true</Enabled>
    <DisplayName>Texoma_Message_Policy</DisplayName>
    <MessageAgingRuleURI>/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-
d86298e2531c/messageagingrules</MessageAgingRuleURI>
</MessageAgingPolicy> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-id>
Accept: application/json
Connection: keep-alive |
|---|

| {
    "URI":"/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c"
    "ObjectId":"3f3f9297-e1eb-46a5-bbdf-d86298e2531c"
    "Enabled":"true"
    "DisplayName":"Default System Policy"
    "MessageAgingRuleURI":"/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-
d86298e2531c/messageagingrules"
} |
|---|

| Response Code: 200 |
|---|

| *POST https://<connection-server>/vmrest/messageagingpolicies
Request Body:
<MessageAgingPolicy>
    <DisplayName>Texoma_Message_Policy</DisplayName>
</MessageAgingPolicy> |
|---|

| Response Code: 201
/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c |
|---|

| Request URI:
POST https://<connection-server>/vmrest/messageagingpolicies
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "DisplayName":"Texoma_Message_Policy"
} |
|---|

| Response Code: 201
/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c |
|---|

| *POST https://<connection-server>/vmrest/messageagingpolicies
Request Body:
<MessageAgingPolicy>
    <DisplayName>Texoma_New_Message_Policy</DisplayName>
    <Enabled>false</Enabled>
</MessageAgingPolicy> |
|---|

| Response Code: 201
/vmrest/messageagingpolicies/3f3f9297-e1eb-46a5-bbdf-d86298e2531c |
|---|

| *PUT https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-id>
Request Body:
<MessageAgingPolicy>
    <DisplayName>Texoma_Message_Policy_2</DisplayName>
</MessageAgingPolicy> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-id>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "DisplayName":"Texoma_Message_Policy_2"
} |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/messageagingpolicies<messageagingpolicyobject-id> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/messageagingpolicies<messageagingpolicyobject-id>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| Parameters | Operations | Data Type | Comments |
|---|---|---|---|
| DisplayName | Read/Write | String | Name of the Message Aging Policy Maximum length: 64 |
| Enabled | Read/Write | Boolean | Specifies if message aging rules to be
                                                					 applied or not. Possible values: true: If message
                                                         						  aging rules to be enforced. false: If
                                                         						  message aging rules to be ignored. Default value is true. |
| MessageAgingRuleURI | Read Only | String | Specifies the URI of message aging rules. |
| ObjectId | Read Only | String | Object Id of the message aging policy. Maximum length : 36 |
| URI | Read Only | String | Specifies the message aging policy URI. |

| GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-Id>/messageagingrules |
|---|

| <MessageAgingRules total="2">
  <MessageAgingRule>
    <URI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0/messageagingrules/6951ad4c-a16c-4bf2-b61a-300bbf24519d</URI>
    <MessageAgingPolicyObjectId>0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyURI>
    <ObjectId>6951ad4c-a16c-4bf2-b61a-300bbf24519d</ObjectId>
    <Days>7</Days>
    <Enabled>true</Enabled>
    <Secure>false</Secure>
    <SendNotification>true</SendNotification>
    <NotificationDays>3</NotificationDays>
    <RuleDescription>Move Saved Messages to the Deleted Items</RuleDescription>
  </MessageAgingRule>
  <MessageAgingRule>
    <URI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0/messageagingrules/8792058b-cf27-4c10-8ac1-e903b8d18065</URI>
    <MessageAgingPolicyObjectId>0f02be4e-5d70-4a1d-b182-ce14ede90ac0</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyURI>
    <ObjectId>8792058b-cf27-4c10-8ac1-e903b8d18065</ObjectId>
    <Days>15</Days>
    <Enabled>true</Enabled>
    <Secure>false</Secure>
    <SendNotification>false</SendNotification>
    <NotificationDays>3</NotificationDays>
    <RuleDescription>Permanently Delete Messages in the Deleted Items </RuleDescription>
  </MessageAgingRule>
</MessageAgingRules> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-Id>/messageagingrules
Accept: application/json
Connection: keep-alive |
|---|

| { 
  "@total":"2"
  "MessageAgingRule":
  [
  {
    "URI":"/vmrest/messageagingpolicies/2fcb9e34-bb41-41e3-b212-
    1bff3e1d93ed/messageagingrules/230f8ab1-1dba-45db-8e2c-dbd22cad718a"
    "MessageAgingPolicyObjectId":"2fcb9e34-bb41-41e3-b212-    1bff3e1d93ed"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/2fcb9e34-bb41-41e3-b212-
    1bff3e1d93ed"
    "ObjectId":"230f8ab1-1dba-45db-8e2c-dbd22cad718a"
    "Days":"30"
    "Enabled":"true"
    "Secure":"true"
    "SendNotification":"false"
    "NotificationDays":"3"
    "RuleDescription":"Permanently Delete Secure Touched Messages "
  }
  {
    "URI":"/vmrest/messageagingpolicies/2fcb9e34-bb41-41e3-b212-
    1bff3e1d93ed/messageagingrules/b0bc585c-7704-4f36-b7f6-8e8319d89da3"
    "MessageAgingPolicyObjectId":"2fcb9e34-bb41-41e3-b212-1bff3e1d93ed"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/2fcb9e34-bb41-41e3-b212-
    1bff3e1d93ed"
    "ObjectId":"b0bc585c-7704-4f36-b7f6-8e8319d89da3"
    "Days":"60"
    "Enabled":"false"
    "Secure":"true"
    "SendNotification":"false"
    "NotificationDays":"3"
    "RuleDescription":"Permanently Delete All Secure Messages "
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-
  Id>/messageagingrules/<messageagingruleobject-Id> |
|---|

| <MessageAgingRule>
    <URI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0/messageagingrules/c160becb-0042-441e-a021-4bb4aeb05da4</URI>
    <MessageAgingPolicyObjectId>0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyObjectId>
    <MessageAgingPolicyURI>/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
    ce14ede90ac0</MessageAgingPolicyURI>
    <ObjectId>c160becb-0042-441e-a021-4bb4aeb05da4</ObjectId>
    <Days>30</Days>
    <Enabled>false</Enabled>
    <Secure>true</Secure>
    <SendNotification>false</SendNotification>
    <NotificationDays>3</NotificationDays>
    <RuleDescription>Permanently Delete Secure Touched Messages </RuleDescription>
</MessageAgingRule> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-
Id>/messageagingrules/<messageagingruleobject-Id>
Accept: application/json
Connection: keep-alive |
|---|

| {
    "URI":"/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
ce14ede90ac0/messageagingrules/c160becb-0042-441e-a021-4bb4aeb05da4"
    "MessageAgingPolicyObjectId":"0f02be4e-5d70-4a1d-b182-ce14ede90ac0"
    "MessageAgingPolicyURI":"/vmrest/messageagingpolicies/0f02be4e-5d70-4a1d-b182-
ce14ede90ac0"
    "ObjectId":"c160becb-0042-441e-a021-4bb4aeb05da4"
    "Days":"60"
    "Enabled":"false"
    "Secure":"true"
    "SendNotification":"false"
    "NotificationDays":"3"
    "RuleDescription":"Permanently Delete Secure Touched Messages"
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-Id>/messageagingrules/<messageagingruleobject-Id>
Request Body:
<MessageAgingRule>
    <Days>25</Days>
</MessageAgingRule> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/messageagingpolicies/<messageagingpolicyobject-Id>/messageagingrules/<messageagingruleobject-Id>
Accept : application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "Days":"25"
} |
|---|

| Response Code: 204 |
|---|

| Note | You can't update the days as well as the NotificationDays
                                                			 parameter if message aging rule is disabled. |
|---|---|

| Parameter | Operation | Data Type | Comments |
|---|---|---|---|
| Days | Read/Write | Integer | Age message older than this number of days.
                                                					 Range: 1 to 365. |
| Action | Read/Write | Integer | Describes the action to take when the rule
                                                					 is applied. Default Value: 0 Values: 0: Soft Delete 1: Hard Delete 2: ToSaved |
| Enabled | Read/Write | Boolean | It specifies whether the particular rule is
                                                					 enabled or not. Values : true or false Default Value: true. |
| MessageAgingPolicyObjectId | Read Only | String (36) | It specifies the object id of respective
                                                					 Message Aging Policy |
| MessageAgingPolicyURI | Read/Write | String | URI of Message Aging Policy. |
| AgingRuleType | Read/Write | Integer | Contains the type or purpose of the aging
                                                					 rule. Default Value: 10 Values: 10:
                                                         						  MoveSeenToDeleted 11:
                                                         						  HardDeleteDeleted 12:
                                                         						  HardDeleteSecureTouched 13:
                                                         						  HardDeleteAllSecure 14:
                                                         						  MoveNewToSaved |
| AgingTimeType | Read/Write | Integer | This defines what column to use
                                                					 (modificationtime or arrivaltime) when calculating messages to age. Default Value: 0 Value: 0:
                                                         						  ModificationTime 1: ArrivalTime |
| LastMessageNotifiedMarker | Read/Write | datetime | A marker used by the sysagent task so we
                                                					 don't send more than one notification per message. |
| NotificationDays | Read/Write | Integer | If SendNotification is True, send the
                                                					 notification this many days before the rule takes place. It is always less than
                                                					 equal to Days parameter. Range: 0 to 365. Default Value: 3. |
| ObjectId | Read Only | String (36) | Object id of Message Aging Rule |
| RuleDescription | Read Only | String | It describes the action taken by rule. |
| Secure | Read Only | Boolean | It specifies whether the message is secured
                                                					 type or not. |
| SendNotification | Read/Write | Boolean | It specifies whether notification is sent
                                                					 prior to taking action. Values: true or false. Default Value: false. |
| Seen | Read/Write | Integer | Apply this rule to messages where
                                                					 tbl_FolderItem. Seen is equal to this value. Default Value: NULL |
| Recent | Read/Write | Integer | If SendNotification is True, send the
                                                					 notification this many days before the rule takes place. Default Value: 3 |
| URI | Read Only | string | URI of Message Aging Rule. |

| GET https://<connection-server>/vmrest/messageagingtexts |
|---|

| <MessageAgingTexts total="1">
  <MessageAgingText>
     <URI>/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d</URI>
     <ObjectId>0220cac9-6df0-48c2-929f-e38d7ff88e3d</ObjectId>
     <LanguageCode>1033</LanguageCode>
     <DefaultSubject>Your message from %SENDER% will be moved to the Saved Messages
    folder in %DAYSUNTIL% day(s).</DefaultSubject>
     <Subject/>
     <DefaultBody>Your message from %SENDER%, which was received on
     %MODIFICATIONTIME%, will be moved to the Saved Messages folder in %DAYSUNTIL%
     day(s).</DefaultBody>
     <Body/>
     <UseDefault>false</UseDefault>
     <RuleDescription>Text for Move New Messages to the Saved Messages Folder
   Rule</RuleDescription>
  </MessageAgingText>
<MessageAgingTexts> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/messageagingtexts
Accept: application/json
Connection: keep-alive |
|---|

| {
     "@total":"1"
     "MessageAgingText":[
{
     "URI": "/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "ObjectId": "0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "LanguageCode": "1033",
     "DefaultSubject": "Your message from %SENDER% will be moved to the Saved Messages
   folder in %DAYSUNTIL% day(s).",
     "Subject": [],
     "DefaultBody": "Your message from %SENDER%, which was received on
   %MODIFICATIONTIME%, will be moved to the Saved Messages folder in %DAYSUNTIL% day(s).",
     "Body": [],
     "UseDefault": "false",
     "RuleDescription": "Text for Move New Messages to the Saved Messages Folder Rule"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/messageagingtexts
Accept: application/json
Connection: keep-alive |
|---|

| {
     "@total":"1"
     "MessageAgingText":[
{
     "URI": "/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "ObjectId": "0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "LanguageCode": "1033",
     "DefaultSubject": "Your message from %SENDER% will be moved to the Saved Messages
   folder in %DAYSUNTIL% day(s).",
     "Subject": [],
     "DefaultBody": "Your message from %SENDER%, which was received on
   %MODIFICATIONTIME%, will be moved to the Saved Messages folder in %DAYSUNTIL% day(s).",
     "Body": [],
     "UseDefault": "false",
     "RuleDescription": "Text for Move New Messages to the Saved Messages Folder Rule"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobject-id> |
|---|

| <MessageAgingText>
     <URI>/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d</URI>
     <ObjectId>0220cac9-6df0-48c2-929f-e38d7ff88e3d</ObjectId>
     <LanguageCode>1034</LanguageCode>
     <DefaultSubject>Your message from %SENDER% will be moved to the Saved Messages folder in
   %DAYSUNTIL% day(s).</DefaultSubject>
     <Subject/>
     <DefaultBody>Your message from %SENDER%, which was received on %MODIFICATIONTIME%,
   will be moved to the Saved Messages folder in %DAYSUNTIL% day(s).</DefaultBody>
     <Body/>
     <UseDefault>true</UseDefault>
     <RuleDescription>Text for Move New Messages to the Saved Messages Folder
   Rule</RuleDescription>
</MessageAgingText> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobject-id>
Accept: application/json
Connection: keep-alive |
|---|

| {
     "URI": "/vmrest/messageagingtexts/0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "ObjectId": "0220cac9-6df0-48c2-929f-e38d7ff88e3d",
     "LanguageCode": "1034",
     "DefaultSubject": "Your message from %SENDER% will be moved to the Saved Messages folder in
   %DAYSUNTIL% day(s).",
     "Subject": [],
     "DefaultBody": "Your message from %SENDER%, which was received on %MODIFICATIONTIME%,
   will be moved to the Saved Messages folder in %DAYSUNTIL% day(s).",
    "Body": [],
    "UseDefault": "true",
    "RuleDescription": "Text for Move New Messages to the Saved Messages Folder Rule"
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobjectid>
Request Body:
<MessageAgingText>
     <UseDefault>Message Aging Text</UseDefault>
</MessageAgingText> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobjectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
     "UseDefault":"Message Aging Text"
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobjectid>
Request Body:
<MessageAgingText>
     <UseDefault>false</UseDefault>
     <Subject>Message aging text</Subject>
     <Body>Message aging Text</Body>
</MessageAgingText> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/messageagingtexts/<messageagingtextobjectid>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
     "UseDefault": "False",
     "Subject": "Message Aging test",
     "Body": "Message Aging Text"
}
The following is the response from the above *PUT* request and the actual response will depend upon the information given by you:
<pre>
Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| ObjectId | Read Only | String (36) | Object id of message aging text |
| LanguageCode | Read/Write | Integer | the language identifier for this row |
| DefaultSubject | Read Only | String (84) | Default data supplied subject |
| Subject | Read/Write | String (84) | Admin supplied subject. Can be modified or
                                                					 updated only if UseDefault parameter is false. |
| DefaultBody | Read Only | String (2048) | Default data supplied default body. |

| GET https://<connection-server>/vmrest/messageexpirations |
|---|

| <MessageExpirations total="1">
<MessageExpiration>
<URI>/vmrest/messageexpirations/72269af8-7376-48d2-bf23-9abf6e98b303</URI>
<ObjectId>72269af8-7376-48d2-bf23-9abf6e98b303</ObjectId>
<Enabled>false</Enabled>
<MaximumAgeDays>180</MaximumAgeDays>
<MaxVideoMsgAgeDays>30</MaxVideoMsgAgeDays>
</MessageExpiration>
</MessageExpirations> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/messageexpirations
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| {
   "@total": "1",
   "MessageExpiration":    {
      "URI": "/vmrest/messageexpirations/72269af8-7376-48d2-bf23-9abf6e98b303",
      "ObjectId": "72269af8-7376-48d2-bf23-9abf6e98b303",
      "Enabled": "true",
      "MaximumAgeDays": "180",
      "MaxVideoMsgAgeDays": "30"
   }
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/messageexpirations/<messageexpirationobjectid>
Request Body:
<MessageExpiration>
<Enabled>true</Enabled>
<MaximumAgeDays>23</MaximumAgeDays>
<MaxVideoMsgAgeDays>11</MaxVideoMsgAgeDays>
</MessageExpiration> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/messageexpirations/<messageexpirationobjectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
      "Enabled": "true",
      "MaximumAgeDays": "55",
      "MaxVideoMsgAgeDays": "44"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| ObjectId | Read Only | String (36) | A globally unique, system-generated
                                             					 identifier for Message Expiration Policy. |
| Enabled | Read/Write | Boolean | A flag indicating whether the Message
                                             					 Expiration is applicable or not. Values can be: false - Message
                                                      						  Expiration is not applicable. true - Message
                                                      						  Expiration is applicable. Default Value - false |
| MaximumAgeDays | Read/Write | Integer | The number of days after which the
                                             					 audio/video message will be marked as expired from the Cisco Unity Connection. Range - 1-999
                                                      						  Days Default Value - 180 |
| MaxVideoMsgAgeDays | Read/Write | Integer | The number of days after which the video
                                             					 part of a video message will be deleted and only audio part will be retained. Note: It is recommended that the number of days entered in
                                                						MaxVideoMsgAgeDays should be less than the number of days entered in
                                                						MaximumAgeDays field. Range - 1-999
                                                      						  Days Default Value - 30 |