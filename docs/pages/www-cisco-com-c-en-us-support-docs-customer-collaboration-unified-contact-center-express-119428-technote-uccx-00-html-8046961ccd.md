---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-119428-technote-uccx-00-html-8046961ccd
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/119428-technote-uccx-00.html
retrieved_at: 2026-08-16T15:05:24.613976+00:00
---

Configure Post Call Treatment on Cisco Unified Contact Center Express (UCCX) 11.0(1) or Later

# Configure Post Call Treatment on Cisco Unified Contact Center Express (UCCX) 11.0(1) or Later

Updated: June 13, 2018

Document ID: 119428

Contents

## Contents

## Introduction

This document describes Post Call Treatment, which allows Unified Contact Center Express (Unified CCX) to provide treatment to a Unified CCX script routed call once the agent ends the call from the Finesse Desktop. The Unified CCX administrator has an option to configure the Post Call Treatment via the Cisco Unified CCX Script Editor. This functionality will not be available if the agent ends the call from the phone rather than through Finesse, or when the customer hangs up before the agent to end the call. If there is a second agent that continues to talk to the caller, the caller is not transferred to the post call treatment at that time. Also, if the caller happens to be an agent themselves, the call will not be transferred to the Post Call Survey script.

### How It Works

When Unified CCX receives the disconnect event from an agent hangup (with the Finesse End button rather than the phone), it checks whether there is a call variable named PostCallTreatment. If there was only one agent in the call at hangup, it redirects the caller to the directory number (DN) which was stored in the PostCallTreatment variable.

## Prerequisites

### Requirements

A system administrator must configure at least one Script, Application, and Trigger in order to receive the call once the Post Call Treatment feature is activated. The call will be redirected from the agent phone to this Trigger in order to receive Post Call Treatment.

### Components Used

The information in this document is based on these software and hardware versions:

- Unified CCX must be version 11.0(1) or later and agents must use Finesse Desktop. This feature is not available on Finesse IP Phone Agent (FIPPA).

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Install a Custom Post Call Treatment Script

Create a Unified CCX script with the desired Post Call Survey treatment. Install it as an application with an associated Trigger.

### Define an ECC Variable to Hold the Trigger DN for a Post Call Treatment Script

With the script editor, define an Expanded Call Variable for the post call treatment.

Choose Settings > Expanded Call Variable . Click the arrow icon in order to create a new variable. Name this new variable PostCallTreatmen t and provide the type as scalar .

Note : The name of the variable must be a case sensitive exact match to " PostCallTreatment ". Click Ok .

From the Cisco Unified CCX Editor application, open an existing script that contains a Select Resource step.

From the Script Variables panel, create a new script variable. Set the type as int from the dropdown list available for the new variable PostCallTreatment.

Enter a number value in the Value field. This number is the Trigger DN that is to receive the call and provide the Post Call Treatment (assigned as the Trigger for the previously installed Post Call Survey application).

Check the Final checkbox.

From the Call Contact palette, choose Set Enterprise Call Info. Drag and drop the selected step in the script before the Select Resource . Alternatively, edit an existing Set Enterprise Call Info step in the script before the Select Resource step.

Add the new Expanded Call Context Variable created to the Set Enterprise Call Info step. Right-click the Set Enterprise Call Info step and then click Properties . In the Expanded Call Variables tab, click Add . Select the variable you defined as an Int in the Values field and the Expanded Call Context Variable PostCallTreatment in the Names field, Array Indexes is Scalar, and Tokens is All. Click Ok > Apply > Ok .

## Verify

Use this section to confirm that your configuration works properly.

In order to verify, call the Unified CCX Trigger that corresponds to the script that sets the PostCallTreatment Enterprise Variable. Once the call is connected to the agent, have the agent disconnect the call with the End button in Finesse. Verify the caller is redirected to the Trigger defined in the script as the PostCallTreatment variable value.

## Troubleshoot

This section provides information you can use to troubleshoot your configuration.

If after the agent ends the call, the call is not transferred to the Post Call Treatment Trigger:

- Run a Reactive Debug of the script in order to verify the PostCallTreatment variable value is being set appropriately in the script.

Additional Information

When you use the Set Enterprise Call Info step in order to pass a value to Finesse to display in the Call Variable Layout, or use it in a Workflow action, you must be mindful that the interface in Finesse Administration always prepends "user" to the variable if it is not one of the standard predefined Expanded Call Context Variables (exposed in the dropdown list). Therefore you must add the Expanded Call Context Variable with a user prefix if you want it to match what is defined in Finesse Administration.

For example, the Post Call Survey feature uses a special name defined as PostCallTreatment. This is hard coded so must be added to match.

When a call is disconnected by the Finesse agent, the disconnect event is sent to the Unified CCX Engine's Resource Manager/Contact Manager (RMCM) Subsystem and it checks to see if the Call object has a value assigned to PostCallTreatment and handles it accordingly.

On the other hand, if you wanted that value to also be displayed on the Finesse Desktop, you would need a different Expanded Call Context variable defined with a "user" prefix.

These screenshots show the ability to also display the Survey DN to the Agent by adding the user PostCallTreatment Expanded Call Context variable to the Set Enterprise Call Info step, as well as to the Finesse Call Variable Layout in Finesse Administration.

- Verify the agent phone can dial the Post Call Treatment trigger DN.

2015-12-09T13:29:52.225 -04:00: : dsbccx11p.dbicknel.com: Dec 09 2015 12:37:06.077 -0500: Header : [WorkflowEngine] Converting event to xml document. Type: Dialog Action: delete Uri: /finesse/api/Dialog/16783327 Event: {"Dialog":{"associatedDialogUri":null,"fromAddress":"1007","id":"16783327","mediaProperties":{"DNIS":"101 0","callType":"ACD_IN","dialedNumber":"5001",...., {"name":"PostCallTreatment","value":"5002"}, ........."state":"DROPPED","stateCause":null,"stateChangeTime":"2015-12-09T17:37:06.057Z"}]},"state":"ACTIVE","toAddress":"5001", "uri":"/finesse/api/Dialog/16783327"}}

- Check the Unified CCX Engine (MIVR) logs on Unified CCX or Reactive Debug the Post Call Treatment script in order to determine if the call is being redirected to Unified CCX and the script is being applied.

These two MIVR log snippets show a working and non-working scenario.

Working Scenario

A Place Call step from a test script to put a call in queue:

```
10231: Dec 05 19:01:36.215 EST %MIVR-SS_RM-7-UNK:ClearConnectionReqMsgHandler - isPostCallSurveyEnabled postCallSurveyDN: 5002 10232: Dec 05 19:01:36.215 EST %MIVR-SS_RM-7-UNK:ClearConnectionReqMsgHandler: runHandler connectedAgents.size: 1 10233: Dec 05 19:01:36.215 EST %MIVR-SS_RM-7-UNK:ClearConnectionReqMsgHandler - isPostCallSurveyEnabled. Only agent. Transferring the call to survey 10234: Dec 05 19:01:36.215 EST %MIVR-SS_RM-7-UNK:isCTIRoutePoint, addr: 5002:true
```

Non-Working Scenario

Call placed from an Agents DN:

```
7754: Dec 05 18:26:31.845 EST %MIVR-SS_RM-7-UNK:ClearConnectionReqMsgHandler - isPostCallSurveyEnabled postCallSurveyDN: 5002 7755: Dec 05 18:26:31.845 EST %MIVR-SS_RM-7-UNK:ClearConnectionReqMsgHandler: runHandler connectedAgents.size: 2 7756: Dec 05 18:26:31.845 EST %MIVR-SS_RM-7-UNK:ClearConnectionReqMsgHandler - isPostCallSurveyEnabled: calling clearConnection. returning false
```

### Revision History

1.0

13-Jan-2016

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 13-Jan-2016 | Initial Release |