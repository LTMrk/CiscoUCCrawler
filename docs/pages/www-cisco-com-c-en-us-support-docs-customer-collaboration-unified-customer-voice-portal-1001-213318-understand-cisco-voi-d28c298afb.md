---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-1001-213318-understand-cisco-voi-d28c298afb
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal-1001/213318-understand-cisco-voice-portal-courtesy-c.html
retrieved_at: 2026-08-21T06:52:00.925917+00:00
---

Understand Cisco Voice Portal Courtesy Callback Status Information

# Understand Cisco Voice Portal Courtesy Callback Status Information

### Download Options

Updated: January 10, 2022

Document ID: 213318

Contents

## Contents

## Introduction

The document describes the different call status involved in a Cisco Voice Portal (CVP) Courtesy Callback (CCB) deployment.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CVP

- CVP Call Studio

- CVP Courtesy Callback

### Components Used

The information in this document is based on these software and hardware versions:

- CVP Version 10

- Call Studio Version 10

The information in this document was created from the devices in a specific lab environment. All the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Courtesy Callback Call Flow And Applications Involved

When you place a call to a system where Courtesy Callback is implemented, several applications and processes are involved in order to offer you a callback, so you do not have to wait on the phone while an agent becomes available.

1. The call needs first to be validated so CCB can be offered if validation pass.

The call is added to memory queue and different parameters are validated in order to offer a callback. For instance, the minimum Estimated Wait Time allowed (EWT), ingress gateway configuration required, current callbacks, number of Ingress gateway trunks assigned for callback, and so on.

The CVP Call Studio application related to this validation process is CallbackEntry.

2. If validation passes, Courtesy Callback is offer. If the Courtesy Callback is accepted by the caller, the CVP CCB solution collects the caller information. After the information is collected, a good bye message is played to the caller.

The Call studio applications related to this process are CallbackEntry and CallbackEngine . At this moment, since the callback has been added to the database the status of the call is: Callback Pending (21).

3. The Courtesy Callback solution waits for the EWT to expire in order to place the call back ( Callback in progress (22 )). The callback occurs and the call is accepted. At this moment the status of the callback changes to Completed/Connected (Status 24) .

The application related to this process is CallbackWait . The status of the call is: Callback Completes (24).

4. The caller waits on queue while an agent becomes available. As soon as an agent becomes available the call is sent to the agent and the callback is removed from memory queue. The application related to this process is CallbackQueue .

## Analyze Activity Logs, Reporting Logs, And Database Output

### CallbackEntry

CallbackEntry Activity logs: Call starts

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,newcall,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,ani,5008
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,areacode,NA
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,exchange,NA
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,dnis,8013
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,uui,NA
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,iidigits,NA
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,_userCourtesyCallbackEnabled=1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,ani=5008
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,qname=billing
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,callid=064CD880000100000000025308C6C90A
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,queueapp=BillingQueue
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,_dnis=8013
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,_ccbServlet=http://10.201.198.11:8000/cvp/CallbackServlet
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,ewt=180
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,_ani=5008
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,,start,parameter,_ccbServletReqTimeout=10
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.607,CVP Subdialog Start_01,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.747,CVP Subdialog Start_01,exit,done
```

CallbackEntry Activity logs: Call added to memory queue:

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.747,Enter Queue_01,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.747,Enter Queue_01,custom,Callback_Enter_Queue,ELEMENT_ENTRY
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.763,Enter Queue_01,custom,thishost,10.201.198.11
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.825,Enter Queue_01,custom,Callback_Enter_Queue,ELEMENT_EXIT
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.825,Enter Queue_01,data,ewt,0
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.825,Enter Queue_01,exit,done
```

CVP Reporting Server logs show the call has been added to memory:

```
15202: 10.201.198.11: Dec 14 2015 11:41:18.810 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor41} EnterQueueHandler:validate: validate guid=064CD880000100000000025308C6C90A icmewt=180
15203: 10.201.198.11: Dec 14 2015 11:41:18.810 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor41} EnterQueueHandler:EnterQueueHandler.exec: EnterQueueHandler CALLGUID=064CD880000100000000025308C6C90A CallStartDate=Mon Dec 14 11:41:18 CST 2015
15204: 10.201.198.11: Dec 14 2015 11:41:18.810 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor41} EnterQueue CALLGUID=064CD880000100000000025308C6C90A QueueName=billing ani=5008
15205: 10.201.198.11: Dec 14 2015 11:41:18.810 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor41} QueueStats putEntry: 064CD880000100000000025308C6C90A<List size:0>
15206: 10.201.198.11: Dec 14 2015 11:41:18.810 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor41} JdbcCallbackQueueDAO:store: Request to store CallbackQueue record. CallGUID=064CD880000100000000025308C6C90A CallbackQueueDTO=CallbackQueueDTO::' SurrogateId: '-1' QueueName: 'billing' QueueId: '-1' DbDateTime: 'null' QueueStatus: '0' ValidationStatus: '0' EnterDateTime: 'Mon Dec 14 11:41:18 CST 2015' LeaveDateTime: 'null' CVPEstimatedWaitTime: '0' ICMEstimatedWaitTime: '180' CallStartDate: 'Mon Dec 14 11:41:18 CST 2015'
15207: 10.201.198.11: Dec 14 2015 11:41:18.810 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor41} JdbcCallbackQueueDAO:store: Responded with retCode: 0 to request to store CallbackQueue record CALLGUID=064CD880000100000000025308C6C90A
```

CallbackEntry Activity logs: EWT is calculated in minutes scale:

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.825,ewt in Minutes,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.825,ewt in Minutes,custom,Result,4.0
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.825,ewt in Minutes,exit,done
```

CallbackEntry Activity logs: Validate the call to see if a callback can be offered

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.825,Validate_01,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.825,Validate_01,custom,Callback_Validate,ELEMENT_ENTRY
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.872,Validate_01,custom,Callback_Validate,ELEMENT_ENTRY
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.872,Validate_01,custom,probe outcome,id:10.201.198.21;loc:doclab;trunks:100
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,Validate_01,custom,Callback_Validate,ELEMENT_EXIT
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,Validate_01,data,gw,10.201.198.21
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,Validate_01,data,loc,doclab
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,Validate_01,data,capacity,100
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,Validate_01,data,result,refresh
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,Validate_01,exit,refresh
```

CVP Reporting Server logs show validation refresh:

```
15208: 10.201.198.11: Dec 14 2015 11:41:18.888 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor33} ValidateHandler:ValidateHandler.exec: ValidateHandler GUID=064CD880000100000000025308C6C90A
15209: 10.201.198.11: Dec 14 2015 11:41:18.888 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor33} ValidateHandler:ValidateHandler.exec: ValidateHandler GUID=064CD880000100000000025308C6C90A refresh
```

CallbackEntry Activity logs: Use the SetQueueDefault values to validate the call:

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,SetQueueDefaults_01,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,SetQueueDefaults_01,custom,Callback_Set_Queue_Defaults,ELEMENT_ENTRY
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,SetQueueDefaults_01,custom,Callback_Set_Queue_Defaults,ELEMENT_EXIT
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,SetQueueDefaults_01,exit,done
```

CVP Reporting Server  logs show SetQueue :

```
15210: 10.201.198.11: Dec 14 2015 11:41:18.888 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor39} SetQueueDefaultsHandler:SetQueueDefaultsHandler.exec: SetQueueDefaultsHandler QueueName=billing
```

CallbackEntry Activity logs: Validate again since the previous result was refresh:

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,Validate_02,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.888,Validate_02,custom,Callback_Validate,ELEMENT_ENTRY
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.935,Validate_02,custom,Callback_Validate,ELEMENT_ENTRY
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.935,Validate_02,custom,probe outcome,id:10.201.198.21;loc:doclab;trunks:100
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.950,Validate_02,custom,Callback_Validate,ELEMENT_EXIT
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.950,Validate_02,data,gw,10.201.198.21
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.950,Validate_02,data,loc,doclab
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.950,Validate_02,data,capacity,100
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.950,Validate_02,data,result,preemptive
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.950,Validate_02,exit,preemptive
```

CVP Reporting Server logs show validation:

```
15211: 10.201.198.11: Dec 14 2015 11:41:18.935 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor23} ValidateHandler:ValidateHandler.exec: ValidateHandler GUID=064CD880000100000000025308C6C90A
15212: 10.201.198.11: Dec 14 2015 11:41:18.935 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor23} JdbcCallbackDAO:isExceededCapacity: Request to check if exceeded capacity in Callback. Gateway=10.201.198.21 NumOfGatewayAllowed=2 inteval=60
15213: 10.201.198.11: Dec 14 2015 11:41:18.935 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor23} JdbcCallbackDAO:isExceededCapacity: Returning true for query on whether capacity is exceeded. Input parameters: Gateway=10.201.198.21 NumberOfGatewayCallbacksAllowed=2 inteval=60
15214: 10.201.198.11: Dec 14 2015 11:41:18.935 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor23} willQueueHandleCallback: QueueName: billing pendingCallBacks: 0 MaxCalls: 9999999 CurrentQueueSize: 1 MaxPercent: 100
15215: 10.201.198.11: Dec 14 2015 11:41:18.935 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor23} willQueueHandleCallback: percent: 10015216: 10.201.198.11: Dec 14 2015 11:41:18.935 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor23} JdbcCallbackQueueDAO:updateValidationStatus: Request to update validation status in CallbackQueue. CallGUID=064CD880000100000000025308C6C90A validationStatus=2
15217: 10.201.198.11: Dec 14 2015 11:41:18.935 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor23} JdbcCallbackQueueDAO:updateValidationStatus: Validation status of 1 rows were updated in CallbackQueue. CALLGUID=064CD880000100000000025308C6C90A
15218: 10.201.198.11: Dec 14 2015 11:41:18.935 -0600: %CVP_10_0_RPT-7-LOW_LEVEL: {Thrd=http-processor23} ValidateHandler:ValidateHandler.exec: ValidateHandler GUID=064CD880000100000000025308C6C90A results:preemptive validation status bitmask=0x00000003
```

CallbackEntry Activity logs: Prompt caller phone number and name:

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.950,PreemptivePrompt1,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.954,PreemptivePrompt1,interaction,audio_group,initial_audio_group
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.981,PreemptivePrompt1,exit,done
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.981,PreemptivePrompt2,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:18.981,PreemptivePrompt2,interaction,audio_group,initial_audio_group
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.057,PreemptivePrompt2,interaction,utterance,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.061,PreemptivePrompt2,interaction,inputmode,dtmf
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.061,PreemptivePrompt2,interaction,interpretation,true
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.061,PreemptivePrompt2,interaction,confidence,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.233,PreemptivePrompt2,data,value,yes
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.233,PreemptivePrompt2,data,confidence,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.233,PreemptivePrompt2,data,value_confidence,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.233,PreemptivePrompt2,exit,yes
```

CallbackEntry Activity logs: Record name:

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.233,Record Name,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:37.233,Record Name,interaction,audio_group,initial_audio_group
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,Record Name,data,duration,4400
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,Record Name,data,size,34560
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,Record Name,data,termchar,#
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,Record Name,data,maxtime,false
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,Record Name,data,filename,audio1450114906328288.wav
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,Record Name,data,filepath,C:\Cisco\CVP\VXMLServer\Tomcat\webapps\CVP\audio\recordings\audio1450114906328288.wav
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,Record Name,exit,done
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,ANI existence check,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,ANI existence check,exit,exists
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.328,Confirm Callback Number 1,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:46.332,Confirm Callback Number 1,interaction,audio_group,initial_audio_group
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.120,Confirm Callback Number 1,interaction,utterance,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.120,Confirm Callback Number 1,interaction,inputmode,dtmf
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.120,Confirm Callback Number 1,interaction,interpretation,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.120,Confirm Callback Number 1,interaction,confidence,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.283,Confirm Callback Number 1,data,value,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.283,Confirm Callback Number 1,data,selection,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.283,Confirm Callback Number 1,data,confidence,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.283,Confirm Callback Number 1,data,value_confidence,1
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.283,Confirm Callback Number 1,exit,option1
```

CallbackEntry Activity logs: Call passed validation. Caller accepted the CCB offer and information was collected. Now, this call is added to the database table Callback:

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.283,Add Callback to DB 1,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.283,Add Callback to DB 1,custom,Callback_Add,ELEMENT_ENTRY
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.314,Add Callback to DB 1,custom,Callback_Add,ELEMENT_EXIT
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.314,Add Callback to DB 1,data,result,valid
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.314,Add Callback to DB 1,exit,done
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.314,Is valid 1,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.314,Is valid 1,exit,validated
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.314,Application_Modifier_02,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.314,Application_Modifier_02,exit,done
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.314,Return to ICM,enter,
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.345,Return to ICM,exit,
```

CVP Reporting Server logs show when the call was added to the database:

```
15223: 10.201.198.11: Dec 14 2015 11:41:55.314 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor47} AddCallbackHandler:AddCallbackHandler.exec: AddCallbackHandler CALLGUID=064CD880000100000000025308C6C90A
15224: 10.201.198.11: Dec 14 2015 11:41:55.314 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor47} JdbcCallbackDAO:store: Request to store Callback record. CallbackDTO=CallbackDTO:: SurrogateId: '-1' CallGUID: '064CD880000100000000025308C6C90A' ANI: '5008' DbDateTime: 'null' EventTypeId: '21' CauseId: '0' CallBackType: 'p' OldGUID: 'null' Gateway: '10.201.198.21' Location: 'doclab' NbrAttempts: '0' ScheduledCallBackDateTime: 'null' ScheduledCallBackDN: 'null' CallStartDate: 'Mon Dec 14 11:41:18 CST 2015' RecordingURL: 'http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav' QueueName: 'null' eventDateTime: Mon Dec 14 11:41:18 CST 2015
15225: 10.201.198.11: Dec 14 2015 11:41:55.314 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor47} JdbcCallbackDAO:store: Responded with retCode: 0 to request to store Callback record CALLGUID=064CD880000100000000025308C6C90A
```

EventTypeId: '21' CauseId: '0' is Callback pending.

Note : The information for the event type can be found on EventTypeRef table.

The next query output shows the information stored in the callback table. Surrogate ID is a primary key which help to identify the call in different callback tables:

Information added to the callback event table, as shown in the image.

CallbackEntry Activity logs: Application finish and results are returned to CVP

```
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.345,,custom,Callback_Leave_Queue,ELEMENT_ENTRY
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.345,,custom,Callback_Leave_Queue,Skipping the rest of Callback_Leave_Queue
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.345,,end,how,app_session_complete
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.345,,end,result,normal
10.201.198.11.1450114878607.81.CallbackEntry,12/14/2015 11:41:55.345,,end,duration,37
```

### CallbackEngine

CallbackEngine: Play goodbye message and the call is disconnected. Invoke CallbackWait application.

```
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,newcall,
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,ani,5008
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,areacode,NA
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,exchange,NA
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,dnis,8013
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,uui,NA
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,iidigits,NA
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,CallbackType=preemptive
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,_userCourtesyCallbackEnabled=1
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,qname=billing
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,callid=064CD880000100000000025308C6C90A
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,queueapp=BillingQueue
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,_dnis=8013
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,qtime=1450114878747
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,_ccbServlet=http://10.201.198.11:8000/cvp/CallbackServlet
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,_ani=5008
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,,start,parameter,_ccbServletReqTimeout=10
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.719,Intercept caller hangup,enter,
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.907,Intercept caller hangup,custom,result,done
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.907,Intercept caller hangup,data,result,done
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.907,Intercept caller hangup,exit,done
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.907,Goodbye,enter,
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.907,Goodbye,interaction,audio_group,initial_audio_group
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.938,Goodbye,exit,done
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:41:55.938,Disconnect Caller_01,enter,
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,Disconnect Caller_01,custom,result,done
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,Disconnect Caller_01,data,result,done
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,Disconnect Caller_01,exit,done
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,Do not leave queue,enter,
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,Do not leave queue,exit,done
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,,custom,Callback_Leave_Queue,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,,custom,Callback_Leave_Queue,Skipping the rest of Callback_Leave_Queue
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,,end,how,application_transfer:CallbackWait
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,,end,result,normal
10.201.198.11.1450114915719.82.CallbackEngine,12/14/2015 11:42:00.399,,end,duration,5
```

### CallbackWait

CallbackWait:  Application starts

```
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.399,,start,source,CallbackEngine
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.399,,start,ani,5008
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.399,,start,areacode,NA
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.399,,start,exchange,NA
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.399,,start,dnis,8013
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.399,,start,uui,NA
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.399,,start,iidigits,NA
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.399,CVP Subdialog Start_01,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,CVP Subdialog Start_01,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,From CallbackEngine,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,From CallbackEngine,exit,done
```

CallbackWait: Status of the call, and EWT verification:

```
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,data,startCallback,false
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,data,ewt,145
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,data,qpos,0
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,data,cli,8005551212
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,data,rna,30
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,data,dn,5008
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Get Status_01,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Is Callback Ready,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Is Callback Ready,exit,no
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Is wait more than 3 mins,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Is wait more than 3 mins,exit,no
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Short Wait,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:00.571,Short Wait,custom,Callback_Wait,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.609,Short Wait,custom,Callback_Wait,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.609,Short Wait,custom,Callback_Wait,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.609,Short Wait,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.609,Get Status_01,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.609,Get Status_01,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,data,startCallback,false
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,data,ewt,35
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,data,qpos,0
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,data,cli,8005551212
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,data,rna,30
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,data,dn,5008
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Get Status_01,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Is Callback Ready,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Is Callback Ready,exit,no
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Is wait more than 3 mins,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Is wait more than 3 mins,exit,no
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Short Wait,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:15.641,Short Wait,custom,Callback_Wait,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.679,Short Wait,custom,Callback_Wait,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.679,Short Wait,custom,Callback_Wait,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.679,Short Wait,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.679,Get Status_01,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.679,Get Status_01,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,data,startCallback,false
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,data,ewt,25
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,data,qpos,0
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,data,cli,8005551212
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,data,rna,30
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,data,dn,5008
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Get Status_01,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Is Callback Ready,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Is Callback Ready,exit,no
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Is wait more than 3 mins,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Is wait more than 3 mins,exit,no
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Short Wait,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:30.726,Short Wait,custom,Callback_Wait,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.764,Short Wait,custom,Callback_Wait,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.764,Short Wait,custom,Callback_Wait,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.764,Short Wait,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.764,Get Status_01,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.764,Get Status_01,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,data,startCallback,false
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,data,ewt,5
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,data,qpos,0
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,data,cli,8005551212
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,data,rna,30
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,data,dn,5008
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Get Status_01,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Is Callback Ready,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Is Callback Ready,exit,no
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Is wait more than 3 mins,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Is wait more than 3 mins,exit,no
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Short Wait,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:42:45.796,Short Wait,custom,Callback_Wait,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.834,Short Wait,custom,Callback_Wait,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.834,Short Wait,custom,Callback_Wait,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.834,Short Wait,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.834,Get Status_01,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.834,Get Status_01,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,data,startCallback,true
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,data,ewt,0
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,data,qpos,0
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,data,cli,8005551212
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,data,rna,30
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,data,dn,5008
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Get Status_01,exit,done
```

CVP Reporting Server logs show status of the call verification.

```
15227: 10.201.198.11: Dec 14 2015 11:42:00.431 -0600: %CVP_10_0_RPT-7-createNewCallEvent: {Thrd=Thread-54}  
15228: 10.201.198.11: Dec 14 2015 11:42:00.571 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor52} GetStatusHandler:GetStatusHandler.exec: GetStatusHandler CALLGUID=064CD880000100000000025308C6C90A
15229: 10.201.198.11: Dec 14 2015 11:42:03.254 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=45 reconnectTime=30 SLA_time=60 RemainingTime=45
15230: 10.201.198.11: Dec 14 2015 11:42:13.394 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=55 reconnectTime=30 SLA_time=60 RemainingTime=35
15231: 10.201.198.11: Dec 14 2015 11:42:15.641 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor37} GetStatusHandler:GetStatusHandler.exec: GetStatusHandler CALLGUID=064CD880000100000000025308C6C90A
15232: 10.201.198.11: Dec 14 2015 11:42:23.534 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=65 reconnectTime=30 SLA_time=60 RemainingTime=25
15233: 10.201.198.11: Dec 14 2015 11:42:30.726 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor27} GetStatusHandler:GetStatusHandler.exec: GetStatusHandler CALLGUID=064CD880000100000000025308C6C90A
15234: 10.201.198.11: Dec 14 2015 11:42:33.674 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=75 reconnectTime=30 SLA_time=60 RemainingTime=15
15235: 10.201.198.11: Dec 14 2015 11:42:43.814 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=85 reconnectTime=30 SLA_time=60 RemainingTime=5
15236: 10.201.198.11: Dec 14 2015 11:42:45.796 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor40} GetStatusHandler:GetStatusHandler.exec: GetStatusHandler CALLGUID=064CD880000100000000025308C6C90
15237: 10.201.198.11: Dec 14 2015 11:42:53.954 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} Queuetats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=95 reconnectTime=30 SLA_time=60 RemainingTime=-5
15238: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor45} GetStatusHandler:GetStatusHandler.exec: GetStatusHandler CALLGUID=064CD880000100000000025308C6C90
```

CallbackWait: Verify if the system is ready to place a callback and update the database

```
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Is Callback Ready,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Is Callback Ready,exit,yes
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Update DB to INPROGRESS,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Update DB to INPROGRESS,custom,Callback_Update_Status,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Update DB to INPROGRESS,custom,Callback_Update_Status,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Update DB to INPROGRESS,data,result,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Update DB to INPROGRESS,exit,done
```

CVP Reporting Server logs show call in progress status:

```
15238: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor45} GetStatusHandler:GetStatusHandler.exec: GetStatusHandler CALLGUID=064CD880000100000000025308C6C90A
15239: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor28} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A status=22 reason=0
15240: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor28} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90Areturning stauts=done
```

Update Callbackqueue with status of the call and the time:

Note : queueStatus=0 is the same as New call based on the information found in the EventTyperef.

```
15241: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor28} JdbcCallbackQueueDAO:updateQueueStatus: Request to update CallbackQueue status. CallGUID=064CD880000100000000025308C6C90A queueStatus=0 leaveDateTime=Mon Dec 14 11:43:00 CST 2015
15242: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor28} JdbcCallbackQueueDAO:updateQueueStatus: Queue status of 1 rows were updated in CallbackQueue. CALLGUID=064CD880000100000000025308C6C90A
15243: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor28} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A updateQueueStatus status=0 returns=1
```

Update callback event table:

status=22 reason=0 is Callback in progress.

Note : The information for the status is the same as the event type and can be found on EventTypeRef table.

```
15244: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor28} JdbcCallbackDAO:updateEvent: Request to update event on Callback record. CallGUID=064CD880000100000000025308C6C90A eventDateTime: Mon Dec 14 11:43:00 CST 2015 CauseID=0
15245: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor28} JdbcCallbackDAO:updateEvent: Responded with retCode: 1 to request to update event on Callback record CALLGUID=064CD880000100000000025308C6C90A
15246: 10.201.198.11: Dec 14 2015 11:43:00.850 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor28} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A updateEvent status=22 returns=1 Callback Event table:
```

CallbackWait: Request CVP via the Ingress Gateway to place the callback to original caller.

```
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Reconnect Caller,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:00.850,Reconnect Caller,custom,Callback_Reconnect,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.316,Reconnect Caller,custom,Callback_Reconnect,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.316,Reconnect Caller,custom,Callback_Reconnect,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.316,Reconnect Caller,data,result,connected
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.316,Reconnect Caller,exit,connected
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.316,Intercept Call Hangup 2,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.394,Intercept Call Hangup 2,custom,result,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.394,Intercept Call Hangup 2,data,result,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.394,Intercept Call Hangup 2,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.394,Announce Callback,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.398,Announce Callback,interaction,audio_group,initial_audio_group
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.425,Announce Callback,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.425,Announce Name,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.429,Announce Name,interaction,audio_group,initial_audio_group
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.456,Announce Name,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.456,Ask if ready,enter
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:12.460,Ask if ready,interaction,audio_group,initial_audio_group
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.548,Ask if ready,interaction,utterance,1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.548,Ask if ready,interaction,inputmode,dtmf
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.548,Ask if ready,interaction,interpretation,1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.548,Ask if ready,interaction,confidence,1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.710,Ask if ready,data,value,1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.710,Ask if ready,data,selection,1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.710,Ask if ready,data,confidence,1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.710,Ask if ready,data,value_confidence,1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.710,Ask if ready,exit,option1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.710,Caller Choice Result,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.710,Caller Choice Result,exit,option 1
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.710,Allow Caller Hangup1,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.772,Allow Caller Hangup1,custom,result,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.772,Allow Caller Hangup1,data,result,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.772,Allow Caller Hangup1,exit,done
```

CallbackWait: Caller accepted the callback and now the call is completed. Database is updated:

```
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.772,Update DB to COMPLETED connected,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.772,Update DB to COMPLETED connected,custom,Callback_Update_Status,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.788,Update DB to COMPLETED connected,custom,Callback_Update_Status,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.788,Update DB to COMPLETED connected,data,result,success
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.788,Update DB to COMPLETED connected,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.788,You are Number1 in Q,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.792,You are Number1 in Q,interaction,audio_group,initial_audio_group
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.819,You are Number1 in Q,exit,done
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.819,UpdateStatus_01,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.819,UpdateStatus_01,custom,Callback_Update_Status,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.819,UpdateStatus_01,custom,Callback_Update_Status,ELEMENT_EXIT
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.819,UpdateStatus_01,data,result,success
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.835,UpdateStatus_01,exit,done
```

CVP Reporting Server logs show the database update:  Update callbackqueue with queuestatus=0.

```
15249: 10.201.198.11: Dec 14 2015 11:43:19.772 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor54} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A status=24 reason=27
15250: 10.201.198.11: Dec 14 2015 11:43:19.772 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor54} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90Areturning stauts=success
15251: 10.201.198.11: Dec 14 2015 11:43:19.772 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor54} JdbcCallbackQueueDAO:updateQueueStatus: Request to update CallbackQueue status. CallGUID=064CD880000100000000025308C6C90A queueStatus=0 leaveDateTime=Mon Dec 14 11:43:19 CST 2015
15252: 10.201.198.11: Dec 14 2015 11:43:19.788 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor54} JdbcCallbackQueueDAO:updateQueueStatus: Queue status of 1 rows were updated in CallbackQueue. CALLGUID=064CD880000100000000025308C6C90A
15253: 10.201.198.11: Dec 14 2015 11:43:19.788 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor54} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A updateQueueStatus status=0 returns=1
```

Update callback event with status=24 and reason status=27.

```
15254: 10.201.198.11: Dec 14 2015 11:43:19.788 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor54} JdbcCallbackDAO:updateEvent: Request to update event on Callback record. CallGUID=064CD880000100000000025308C6C90A eventDateTime: Mon Dec 14 11:43:19 CST 2015 CauseID=27
15255: 10.201.198.11: Dec 14 2015 11:43:19.788 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor54} JdbcCallbackDAO:updateEvent: Responded with retCode: 1 to request to update event on Callback record CALLGUID=064CD880000100000000025308C6C90A
15256: 10.201.198.11: Dec 14 2015 11:43:19.788 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor54} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A updateEvent status=24 returns=1
15257: 10.201.198.11: Dec 14 2015 11:43:19.819 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor48} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A status=27 reason=0
15258: 10.201.198.11: Dec 14 2015 11:43:19.819 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor48} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90Areturning stauts=retry
15259: 10.201.198.11: Dec 14 2015 11:43:19.819 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor48} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A Drop From Queue
```

CallbackWait: Application finishes and results are sent to CVP

```
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:19.835,Return to ICM connected,enter,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:24.515,Return to ICM connected,exit,
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:24.515,,custom,Callback_Leave_Queue,ELEMENT_ENTRY
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:24.515,,custom,Callback_Leave_Queue,Skipping the rest of Callback_Leave_Queue
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:24.515,,end,how,app_session_complete
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:24.515,,end,result,normal
10.201.198.11.1450114915719.82.CallbackWait,12/14/2015 11:43:24.515,,end,duration,84
```

### CallbackQueue

CallbackQueue: Application starts

```
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,newcall,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,ani,5008
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,areacode,NA
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,exchange,NA
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,dnis,8013
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,uui,NA
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,iidigits,NA
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,CallbackType=preemptive
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,_userCourtesyCallbackEnabled=1
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,qname=billing
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,callid=064CD880000100000000025308C6C90A
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,queueapp=BillingQueue
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,_dnis=8013
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,qtime=1450114878747
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,_ccbServlet=http://10.201.198.11:8000/cvp/CallbackServlet
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,_ani=5008
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,,start,parameter,_ccbServletReqTimeout=10
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.780,CVP Subdialog Start_01,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.920,CVP Subdialog Start_01,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.920,Decision_01,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.920,Decision_01,exit,done
```

CallbackQueue: Update status of call in queue. Agent is not ready to take the call yet:

```
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.920,UpdateStatus_01,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.920,UpdateStatus_01,custom,Callback_Update_Status,ELEMENT_ENTRY
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.967,UpdateStatus_01,custom,Callback_Update_Status,ELEMENT_EXIT
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.967,UpdateStatus_01,data,result,success
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.967,UpdateStatus_01,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:43:24.967,Queue1,enter,
```

CVP Reporting Server logs information: Status 28 means that the Callback is added to queue.

```
15261: 10.201.198.11: Dec 14 2015 11:43:24.811 -0600: %CVP_10_0_RPT-7-createNewCallEvent: {Thrd=Thread-54}  
15262: 10.201.198.11: Dec 14 2015 11:43:24.967 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor65} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A status=28 reason=0
15263: 10.201.198.11: Dec 14 2015 11:43:24.967 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor65} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90Areturning stauts=retry
15264: 10.201.198.11: Dec 14 2015 11:43:24.967 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor65} UpdateStatusHandler:UpdateStatusHandler.exec: UpdateStatusHandler CALLGUID=064CD880000100000000025308C6C90A Add To Queue
```

```
15265: 10.201.198.11: Dec 14 2015 11:43:25.154 -0600: %CVP_10_0_RPT-7-createNewCallEvent: {Thrd=Thread-54}  
15266: 10.201.198.11: Dec 14 2015 11:43:34.514 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=136 reconnectTime=30 SLA_time=60 RemainingTime=-46
15267: 10.201.198.11: Dec 14 2015 11:43:44.654 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=146 reconnectTime=30 SLA_time=60 RemainingTime=-56
15268: 10.201.198.11: Dec 14 2015 11:43:54.794 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=156 reconnectTime=30 SLA_time=60 RemainingTime=-66
15269: 10.201.198.11: Dec 14 2015 11:44:04.934 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=166 reconnectTime=30 SLA_time=60 RemainingTime=-76
15270: 10.201.198.11: Dec 14 2015 11:44:15.074 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=177 reconnectTime=30 SLA_time=60 RemainingTime=-87
15271: 10.201.198.11: Dec 14 2015 11:44:25.214 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=187 reconnectTime=30 SLA_time=60 RemainingTime=-97
15272: 10.201.198.11: Dec 14 2015 11:44:35.355 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=197 reconnectTime=30 SLA_time=60 RemainingTime=-107
15273: 10.201.198.11: Dec 14 2015 11:44:45.495 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=207 reconnectTime=30 SLA_time=60 RemainingTime=-117
15274: 10.201.198.11: Dec 14 2015 11:44:55.635 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=217 reconnectTime=30 SLA_time=60 RemainingTime=-127
15275: 10.201.198.11: Dec 14 2015 11:45:05.775 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=227 reconnectTime=30 SLA_time=60 RemainingTime=-137
15276: 10.201.198.11: Dec 14 2015 11:45:08.208 -0600: %CVP_10_0_RPT-7-CallRegistry: {Thrd=Timer-3} RemovedCallDesc = 0 CallRegistry remaining size = 3
15277: 10.201.198.11: Dec 14 2015 11:45:15.915 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=237 reconnectTime=30 SLA_time=60 RemainingTime=-147
15278: 10.201.198.11: Dec 14 2015 11:45:26.055 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=CallbackTimerThread} QueueStats:recalculateRemainingWaitTimes: recalculateRemainingWaitTimes CALLGUID=064CD880000100000000025308C6C90A queuePos=0 dqRateA=180 timeInFirstPlace(Secs)=248 reconnectTime=30 SLA_time=60 RemainingTime=-158
```

CallbackQueue: Call enters and leave the queue in order to maintain the call active in the system and prevent the call to be categorized as a ghost or zombie call.

```
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Queue1,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,data,startCallback,true
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,data,ewt,0
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,data,qpos,0
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,data,cli,8005551212
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,data,rna,30
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,data,dn,5008
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Get Status_01,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:45:28.925,Queue2,enter,
```

CVP Reporting logs show GetStatus :

```
15279: 10.201.198.11: Dec 14 2015 11:45:28.925 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor64} GetStatusHandler:GetStatusHandler.exec: GetStatusHandler CALLGUID=064CD880000100000000025308C6C90A
```

CallbackQueue: Call enters and leave the queue in order to maintain the call active in the system and prevent the call to be categorized as a ghost or zombie call.

```
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.023,Queue2,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.023,Get Status_02,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.023,Get Status_02,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,data,startCallback,true
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,data,ewt,0
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,data,qpos,0
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,data,cli,8005551212
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,data,rna,30
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,data,dn,5008
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Get Status_02,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:47:33.039,Queue1,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Queue1,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,data,startCallback,true
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,data,ewt,0
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,data,qpos,0
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,data,cli,8005551212
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,data,rna,30
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,data,dn,5008
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Get Status_01,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:49:36.934,Queue2,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.845,Queue2,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.845,Get Status_02,enter,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.845,Get Status_02,custom,Callback_Get_Status,ELEMENT_ENTRY
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,custom,Callback_Get_Status,ELEMENT_EXIT
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,data,startCallback,true
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,data,ewt,0
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,data,qpos,0
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,data,cli,8005551212
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,data,rna,30
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,data,dn,5008
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,data,rec,http://10.201.198.11:7000/CVP/audio/recordings/audio1450114906328288.wav
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Get Status_02,exit,done
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:40.861,Queue1,enter,
```

CallbackQueue: Call is sent to agent and call leaves the queue:

```
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:43.700,Queue1,exit,
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:43.700,,custom,Callback_Leave_Queue,ELEMENT_ENTRY
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:43.700,,custom,Callback_Leave_Queue,ELEMENT_EXIT
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:43.700,,end,how,hangup
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:43.700,,end,result,normal
10.201.198.11.1450115004780.83.CallbackQueue,12/14/2015 11:51:43.700,,end,duration,499
```

CVP Reporting Server logs show call leaving the queue:

```
15325: 10.201.198.11: Dec 14 2015 11:51:43.700 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor62} LeaveQueue CALLGUID=064CD880000100000000025308C6C90A
15326: 10.201.198.11: Dec 14 2015 11:51:43.700 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor62} JdbcCallbackQueueDAO:updateQueueStatus: Request to update CallbackQueue status. CallGUID=064CD880000100000000025308C6C90A queueStatus=0 leaveDateTime=Mon Dec 14 11:51:43 CST 2015
15327: 10.201.198.11: Dec 14 2015 11:51:43.700 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor62} JdbcCallbackQueueDAO:updateQueueStatus: Queue status of 1 rows were updated in CallbackQueue. CALLGUID=064CD880000100000000025308C6C90A
15328: 10.201.198.11: Dec 14 2015 11:51:43.700 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor62} removeQueueEntry CALLGUID=064CD880000100000000025308C6C90A
15329: 10.201.198.11: Dec 14 2015 11:51:43.700 -0600: %CVP_10_0_RPT-7-CALL: {Thrd=http-processor62} QueueStats removeEntry: 064CD880000100000000025308C6C90A
```

The status and process flow of Courtesy Callback provides the caller with useful reference point for the feature implementation and troubleshoot as well as a give a fine description of how the feature operates and interact with the caller.

### Revision History

2.0

10-Jan-2022

Fixed formatting issue.

1.0

03-Jul-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 10-Jan-2022 | Fixed formatting issue. |
| 1.0 | 03-Jul-2018 | Initial Release |