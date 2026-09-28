---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-subscriber-dependency-htm-741a6a757d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi_api-subscriber-dependency.html
retrieved_at: 2026-08-17T03:47:36.213166+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Subscriber Dependency

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Subscriber Dependency

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Subscriber Dependency

Links to Other API pages: Cisco_Unity_Connection_APIs

## Subscriber
                        	 Dependency API

Administrator can use this API to
                           		list the objects that reference a specified user. Using this API administrator
                           		can also replace the dependencies with another user.

### Listing
                           	 Dependencies of All Users

```
GET https://<connection-server>/vmrest/subscriberdependencies
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
<SubscriberDependencies total="2">
  <SubscriberDependency>
   <DependencyType>TT2</DependencyType>
   <DependentEntityObjectId>43205549-0127-48c9-9261-f84102a5890f</DependentEntityObjectId>
   <DependentEntityObjectType>3</DependentEntityObjectType>
   <DependentEntityOwner>Donald_UserTemplate_1 </DependentEntityOwner>
   <DependencyDestinationType>2</DependencyDestinationType>
   <SubscriberObjectId>10b494ca-56ff-4430-a49f-747a33abbd09</SubscriberObjectId>
   <UserURI>/vmrest/users/10b494ca-56ff-4430-a49f-747a33abbd09</UserURI>
   <DependentEntityOwnerType>User Template </DependentEntityOwnerType>
   </SubscriberDependency>
  <SubscriberDependency>
   <DependencyType>Recipient</DependencyType>
   <DependentEntityObjectId>beb9623b-60e4-439d-8fe3-b4c7eec42dfc</DependentEntityObjectId>
   <DependentEntityObjectType>3</DependentEntityObjectType>
   <DependentEntityOwner>Operator </DependentEntityOwner>
   <DependencyDestinationType>5</DependencyDestinationType>
   <SubscriberObjectId>cfbb6680-f028-4282-8740-ba7531e574cf</SubscriberObjectId>
   <UserURI>/vmrest/users/cfbb6680-f028-4282-8740-ba7531e574cf</UserURI>
   <DependentEntityOwnerType>Call Handler </DependentEntityOwnerType>
  </SubscriberDependency>
<SubscriberDependencies>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/subscriberdependencies
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
{
  "@total": "2",
  "SubscriberDependency": 
[       
  {
   "DependencyType": "TT2",
   "DependentEntityObjectId": "43205549-0127-48c9-9261-f84102a5890f",
   "DependentEntityObjectType": "3",
   "DependentEntityOwner": "Donald_UserTemplate_1",
   "DependencyDestinationType": "2",
   "SubscriberObjectId": "10b494ca-56ff-4430-a49f-747a33abbd09",
   "UserURI": "/vmrest/users/10b494ca-56ff-4430-a49f-747a33abbd09",
   "DependentEntityOwnerType": "User Template"
  },
 {
   "DependencyType": "Recipient",
   "DependentEntityObjectId": "beb9623b-60e4-439d-8fe3-b4c7eec42dfc",
   "DependentEntityObjectType": "3",
   "DependentEntityOwner": "Operator",
   "DependencyDestinationType": "5",
   "SubscriberObjectId": "cfbb6680-f028-4282-8740-ba7531e574cf",
   "UserURI": "/vmrest/users/cfbb6680-f028-4282-8740-ba7531e574cf",
   "DependentEntityOwnerType": "Call Handler"
  }
]
}
```

```
Response Code: 200
```

Viewing Dependency of a Specific User

```
GET https://<connection-server>/vmrest/subscriberdependencies/<subscriber-objectid>
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
<SubscriberDependencies total="1">
  <SubscriberDependency>
  <DependencyType>Standard Greeting</DependencyType>
  <DependentEntityObjectId>7ea0ecb6-4125-4866-a0f6-5308a5a4b3d1</DependentEntityObjectId>
  <DependentEntityObjectType>66</DependentEntityObjectType>
  <DependentEntityOwner>Texoma_SystemCallhandlerTemplate_1</DependentEntityOwner>
  <DependencyDestinationType>0</DependencyDestinationType>
  <SubscriberObjectId>4bc6f97a-0c97-4ed9-a7e2-05e611bb02d3</SubscriberObjectId>
  <UserURI>/vmrest/users/4bc6f97a-0c97-4ed9-a7e2-05e611bb02d3</UserURI>
  <DependentEntityOwnerType>Call Handler Template</DependentEntityOwnerType>
 </SubscriberDependency>
</SubscriberDependencies>
```

```
Response code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/subscriberdependencies/<subscriber-objectid>
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
{
  "@total": "1",
  "SubscriberDependency": 
  {
  "DependencyType": "Standard Greeting",
  "DependentEntityObjectId": "7ea0ecb6-4125-4866-a0f6-5308a5a4b3d1",
  "DependentEntityObjectType": "66",
  "DependentEntityOwner": "Texoma_SystemCallhandlerTemplate_1",
  "DependencyDestinationType": "0",
  "SubscriberObjectId": "4bc6f97a-0c97-4ed9-a7e2-05e611bb02d3",
  "UserURI": "/vmrest/users/4bc6f97a-0c97-4ed9-a7e2-05e611bb02d3",
  "DependentEntityOwnerType": "Call Handler Template"
  }
}
```

```
Response Code: 200
```

### Finding
                           	 Dependencies

Example 1:

Suppose following is the dependent object of a particular user and it is
                              		required to find the complete dependency, then below are the steps that should
                              		be followed. Dependent Object:

```
<SubscriberDependency>
  <DependencyType>Standard Greeting</DependencyType>
  <DependentEntityObjectId>7ea0ecb6-4125-4866-a0f6-5308a5a4b3d1</DependentEntityObjectId>
  <DependentEntityObjectType>66</DependentEntityObjectType>
  <DependentEntityOwner>Texoma_SystemCallhandlerTemplate_1 </DependentEntityOwner>
  <DependencyDestinationType>0</DependencyDestinationType>
  <SubscriberObjectId>4bc6f97a-0c97-4ed9-a7e2-05e611bb02d3</SubscriberObjectId>
  <UserURI>/vmrest/users/4bc6f97a-0c97-4ed9-a7e2-05e611bb02d3</UserURI>
  <DependentEntityOwnerType>Call Handler Template</DependentEntityOwnerType>
</SubscriberDependency>
```

Steps to be followed:

- Check
                                 		  DependentEntityOwnerType and DependentEntityObjectId from the response, which
                                 		  depicts the type of object referencing the user. In the example, the
                                 		  referencing object entity is call handler template, whose name is
                                 		  'Texoma_SystemCallhandlerTemplate_1' and object id is
                                 		  '7ea0ecb6-4125-4866-a0f6-5308a5a4b3d1'.

- Check DependencyType, which
                                 		  specifies type of dependency. In this example, it is Standard Greeting. For
                                 		  more information, see the Possible Value of DependencyType section.

- Check
                                 		  DependencyDestinationType, where user is actually referred. In the example, it
                                 		  is 0 that is After Greeting Action. For more information, see the Possible
                                 		  Values of DependencyDestinationType section.

- Therefore, user is
                                 		  referenced in the After Greeting action of Standard Greeting of callhandler
                                 		  template(Texoma_SystemCallhandlerTemplate_1)

Example 2:

Dependent Object:

```
<SubscriberDependency>
  <DependencyType>PCTRCaller</DependencyType>
  <DependentEntityObjectId>476dd400-4130-4795-9e15-c8ce3dd57ff3</DependentEntityObjectId>
  <DependentEntityObjectType>45</DependentEntityObjectType>
  <DependentEntityOwner>Donald_Operator_1</DependentEntityOwner>
  <DependencyDestinationType>4</DependencyDestinationType>
  <SubscriberObjectId>cfbb6680-f028-4282-8740-ba7531e574cf</SubscriberObjectId>
  <UserURI>/vmrest/users/cfbb6680-f028-4282-8740-ba7531e574cf</UserURI>
  <DependentEntityOwnerType>User</DependentEntityOwnerType>
</SubscriberDependency>
```

Steps to be followed:

- Check the
                                    		  DependentEntityOwnerType and DependentEntityObjectId from response, which
                                    		  depicts the type of object referencing the user. In the example, the
                                    		  referencing object entity is user whose name is 'Donald_Operator_1' and object
                                    		  id is '476dd400-4130-4795-9e15-c8ce3dd57ff3'. For more information, see the
                                    		  Possible Value of DependencyType section.

- Check DependencyType, which
                                    		  specifies type of dependency. In this example, the PCTRCaller is
                                    		  DependencyType.

- Check
                                    		  DependencyDestinationType, where user is actually referred. In the example, it
                                    		  is 4 that is refrrenced by personal rule caller. For more information, see the
                                    		  Possible Values of DependencyDestinationType section.

- In above example specified
                                    		  user is referenced in the personal call transfer rule of user
                                    		  (Donald_Operator_1).

### Moving
                           	 Dependencies of One User to Another

Example 1:

Suppose following is the dependent object of a particular user and it is
                              		required to move dependencies to another user, then below are the steps that
                              		should be followed. Dependent Object:

```
<SubscriberDependency>
  <DependencyType>Standard Greeting</DependencyType>
  <DependentEntityObjectId>7ea0ecb6-4125-4866-a0f6-5308a5a4b3d1</DependentEntityObjectId>
  <DependentEntityObjectType>66</DependentEntityObjectType>
  <DependentEntityOwner>Texoma_SystemCallhandlerTemplate_1 </DependentEntityOwner>
  <DependencyDestinationType>0</DependencyDestinationType>
  <SubscriberObjectId>4bc6f97a-0c97-4ed9-a7e2-05e611bb02d3</SubscriberObjectId>
  <UserURI>/vmrest/users/4bc6f97a-0c97-4ed9-a7e2-05e611bb02d3</UserURI>
  <DependentEntityOwnerType>Call Handler Template</DependentEntityOwnerType>
</SubscriberDependency>
```

Steps to be followed:

- Check the
                                    		  DependentEntityOwnerType and DependentEntityObjectId from response. In this
                                    		  example, DependentEntityOwnerType is Call Handler Template, and
                                    		  DependentEntityObjectId is 7ea0ecb6-4125-4866-a0f6-5308a5a4b3d1.

Perform GET Operation on Dependent Object with
                                       			 DependentEntityObjectId as Object ID of dependent object entity. In this
                                       			 example use URI:

```
https://<connection-server>/vmrest/callhandlertemplates/<DependentEntityObjectId>
```

Check DependencyType, which specifies type of dependency. In this
                                       			 example it is Greeting (Standard), therefore, use GET on

```
https://<connection-server>/vmrest/callhandlertemplates/<DependentEntityObjectId>/templategreetings/Standard
```

Check DependencyDestinationType.In this example it is 0 that is
                                       			 After Greeting therefore, perform PUT operation to move the dependency to new
                                       			 user.

```
PUT https://<connection-server>/vmrest/callhandlertemplates/<DependentEntityObjectId>/templategreetings/Standard
```

```
<TemplateGreeting>
  <AfterGreetingAction>2</AfterGreetingAction>
  <AfterGreetingTargetConversation>PHGreeting</AfterGreetingTargetConversation>
  <AfterGreetingTargetHandlerObjectId>9b121ddf-8ce4-4bbd-b179-ab75ab63eb15</AfterGreetingTargetHandlerObjectId>
</TemplateGreeting>
```

Where, AfterGreetingTargetHandlerObjectId is the call handler of new
                                       			 user. In above example After Greeting action of Standard Greeting of call
                                       			 handler template is now referencing callhandler of new user.

### Explanation of
                           	 Data Fields

### Possible Value of
                           	 Dependency Type

### Possible Values of
                           	 DependentEntityObjectType

### Possible Values of
                           	 DependencyDestinationType

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| UserURI | Read Only | String | URI of referenced User |
| DependencyType | Read Only | String(24) | Type of dependency (e.g., After Greeting,
                                          					 After Message, Routing Rule, etc.). Possible values are specified in the table
                                          					 given under the Possible Value of DependencyType section. |
| DependentEntityObjectId | Read Only | String(32) | The unique identifier of the entity that is
                                          					 dependent on the user. |
| DependentEntityObjectType | Read Only | Integer | The type of object that is dependent on the
                                          					 user. Possible values are specified in the table given under the Possible
                                          					 Values of DependentEntityObjectType section. |
| DependentEntityOwner | Read Only | String(36) | The unique identifier of the entity that
                                          					 owns the object which is dependent on the user. For example, a user's call
                                          					 handler may be the dependent entity, but the call handler is owned by another
                                          					 user. |
| DependencyDestinationType | Read Only | Integer | Possible values are specified in the table
                                          					 given under the Possible Values of DependencyDestinationType section. |
| SubscriberObjectId | Read Only | String(36) | Unique Object Id of referenced User |
| DependentEntityOwnerType | Read Only | String(24) | The entity owner type of object (e.g.,
                                          					 User, Call Handler Template) |

| Name | Value | Description | DisplayName |
|---|---|---|---|
| NotificationRuleCaller | NotificationRuleCaller | Reference from notification rule caller | Notification |
| GreetingOffHours | GreetingOffHours | Reference from closed greeting | Closed Greeting |
| GreetingInternal | GreetingInternal | Reference from internal greeting | Internal Greeting |
| GreetingError | GreetingError | Reference from error greeting | Error Greeting |
| GreetingHoliday | GreetingHoliday | Reference from holiday greeting | Holiday Greeting |
| GreetingAlternate | GreetingAlternate | Reference from alternate greeting | Alternate Greeting |
| GreetingBusy | GreetingBusy | Reference from busy greeting | Busy Greeting |
| GreetingStandard | GreetingStandard | Reference from standard greeting | Standard Greeting |
| UserExit | UserExit | Reference from user's call handler's exit
                                          					 action | Exit Action |
| PCTRCaller | PCTRCaller | Reference from personal rule caller | PCTR Caller |
| SMPPProvider | SMPP | Reference from SMPP Provider SMPP Provider | SMPP Provider |
| TT_Pound | TT# | Reference from call handler's TT# menu
                                          					 entry | # |
| TT_Star | TT* | Reference from call handler's TT* menu
                                          					 entry | * |
| TT_0 | TT0 | Reference from call handler's TT0 menu
                                          					 entry | 0 |
| TT_1 | TT1 | Reference from call handler's TT1 menu
                                          					 entry | 1 |
| TT_2 | TT2 | Reference from call handler's TT2 menu
                                          					 entry | 2 |
| TT_3 | TT3 | Reference from call handler's TT3 menu
                                          					 entry | 3 |
| TT_4 | TT4 | Reference from call handler's TT4 menu
                                          					 entry | 4 |
| TT_5 | TT5 | Reference from call handler's TT5 menu
                                          					 entry | 5 |
| TT_6 | TT6 | Reference from call handler's TT6 menu
                                          					 entry | 6 |
| TT_7 | TT7 | Reference from call handler's TT7 menu
                                          					 entry | 7 |
| TT_8 | TT8 | Reference from call handler's TT8 menu
                                          					 entry | 8 |
| TT_9 | TT9 | Reference from call handler's TT9 menu
                                          					 entry | 9 |
| AfterGreeting | After Greeting | Reference from call handler's
                                          					 "AfterGreeting" action | After Greeting |
| AfterMessage | AfterMessage | Reference from call handler's
                                          					 "AfterMessage" action | AfterMessage |
| Exit | Exit | Reference from call handler's "Exit" action | Exit |
| NoInput | NoInput | Reference from call handler's "NoInput"
                                          					 action | NoInput |
| NoSelection | NoSelection | Reference from call handler's "NoSelection"
                                          					 action | AfterMessage |
| Zero | Zero | Reference from call handler's "Zero" action | Zero |
| RoutingRule | RoutingRule | Reference from a routing rule's "Action". | RoutingRule |

| Name | Value | Description |
|---|---|---|
| CallHandler | 3 | CallHandler |
| DirectoryHandler | 6 | Directory Handler used to search a subset
                                          					 of the directory. Formerly referred to as "NameLookupHandler." |
| GreetingRule | 66 | Defines the greeting to play and the action
                                          					 to take for a call handler |
| InterviewHandler | 5 | Special case handler that asks the caller
                                          					 up to 20 questions |
| PersonalRuleCaller | 45 | A caller that drives a personal rule. |
| MenuEntry | 67 | Touch-tone menu entry for a call handler |
| NotificationRule | 72 | Specifies when and which notification
                                          					 device is used for notification of a new message. |
| Subscriber | 21 | User that has a subscription to a voice
                                          					 mail service and as such also is assigned at least one mailbox. |
| UserTemplate | 10 | Template for creating a new user. |
| RoutingRule | 103 | System call routing rule. |
| GlobalUser | 104 | Global user account type. |
| SMPPProvider | 53 | A provider of Short Message Peer-To-Peer
                                          					 services |
| CallHandlerTemplate | 135 | Template for creating new call handlers |
| NotificationRuleCaller | 152 | User triggering a notification rule |

| Name | Value | Description |
|---|---|---|
| AfterGreeting | 0 | The user is an After Greeting destination |
| AfterMessage | 1 | The user is an After Message destination |
| CallerInputKey | 2 | The user is a destination of a caller input
                                          					 key |
| DirectoryHandlerCallerInputKey | 3 | The user is a destination of a directory
                                          					 handler |
| PCTR | 4 | The user is referenced by a personal rule
                                          					 caller |