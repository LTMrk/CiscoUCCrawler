---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-119337-technote-cuc-00-html-a25a1cc326
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/119337-technote-cuc-00.html
retrieved_at: 2026-08-16T18:58:01.446858+00:00
---

Troubleshoot Toll Fraud via Unity Connection

# Troubleshoot Toll Fraud via Unity Connection

### Download Options

Updated: September 1, 2015

Document ID: 119337

Contents

## Contents

## Introduction

This document describes the different options available in Cisco Unity Connection (CUC) that can be used to transfer a call outside, which helps the caller achieve toll fraud. This document also provides CLI queries to check User's or Call Handler's configuration.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUC.

### Components Used

The information in this document is based on CUC Release 8.X or later.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Call Transfer

In CUC, the calls can be transferred to Cisco Unified Communications Manager (CUCM) by one of these different methods:

Ensure that these points are taken into consideration in order to use this option:

- Only administrators can enable this option and define the extension number via the CUC Admin page. Users cannot enable this option. However, when an administrator enables this option, the users can change the extension number via the Telephone User Interface (TUI).

- The restriction table is checked when a user changes the extension number via a TUI conversation.

- The restriction table is not checked when an administrator changes the extension number via the CUC admin page.

- Dial any number if the Allow Transfers to Numbers Not Associated with Users or Call Handlers check box is checked on the Greeting page. CUC performs the transfer only when the Default System Transfer restriction table permits it.

There are two types of conversations which can be used for this purpose:

- Caller System Transfer : This conversation prompts callers to enter the number that they want to transfer to. CUC performs the transfer only when the Default System Transfer restriction table permits it.

- User System Transfer : This conversation prompts callers to log on to CUC. After the caller enters their user ID and PIN, CUC prompts them to enter the number that they want to transfer to. CUC performs the transfer only when permitted by the transfer restriction table that is associated with the user.

- Dial any User or Call Handler's extension while the Call Handler's Greeting is played. The User or Call Handler's 'Transfer Rules can be modified in order to send the call to any number.

- Use the 'After Greeting' action of a User or Call Handler in order to transfer the call to the 'Transfer Rules' of any User or Call Handler. T he User or Call Handler's 'Transfer Rules' can be modified in order to send the call to any number.

### Integration Requirements for Transfers from CUC to Work

- If the integration between CUCM and CUC is Skinny Call Control Protocol (SCCP) - The Voicemail Port's Calling Search Space (CSS) must have the partition of the Route Pattern (RP) to the Public Switched Telephone Network (PSTN) number.

- If the integration between CUCM and CUC is Session Initiation Protocol (SIP) - The SIP trunk's Rerouting CSS must have the partition of the RP to the PSTN number.

- If the call is transferred via a CTI RP/Translation pattern - The voicemail port/SIP trunk must have access to it and the CSS of CTI RP/Translation pattern must have the partition of the RP to the PSTN number.

## Configuration Checks

The User or Call Handler configuration can be verified with CLI queries. A few methods have been mentioned in the Call Transfer section. This section provides details on how to verify the configuration for all the methods.

### Case 1: 'Transfer to Alternate Contact Number' Option

In order to check if a User or Call Handler is configured with the 'Transfer to Alternate Contact Number' Option in the 'Caller Input' section, refer to the CLI Queries section of the Unity Connection: Restriction Tables Effect on 'Transfer to Alternate Contact Number' Feature document.

### Case 2: 'Allow Transfers to Numbers Not Associated with Users or Call Handlers' Option

In order to check if a User or Call Handler is configured with the 'Allow Transfers to Numbers Not Associated with Users or Call Handlers' Option in the Greetings page, run these queries on the CLI:

In order to check for Users:

```
admin:run cuc dbquery unitydirdb select c.displayname, g.greetingtype from vw_callhandler as c inner join vw_greeting as g on c.objectid=g.callhandlerobjectid where enabletransfer = 1 and isprimary = 1 displayname  greetingtype -----------  ------------ Anirudh      Off Hours Anirudh      Standard
```

In order to check for Call Handlers:

```
admin:run cuc dbquery unitydirdb select c.displayname, g.greetingtype from vw_callhandler as c inner join vw_greeting as g on c.objectid=g.callhandlerobjectid where enabletransfer = 1 and isprimary = 0 displayname       greetingtype ----------------  ------------ Opening Greeting  Standard
```

### Case 3: 'After Greeting' Transfer to a Conversation Option

There are two types of Conversations that can be used to transfer the call after the greeting of the User or the Call Handler is played:

- Caller System Transfer - This conversation is identified as SystemTransfer in the Output.

- User System Transfer - This conversation is identified as SubSysTransfer in the Output .

Note : In earlier versions of CUC, a Voice Enabled Directory Handler can also be used to transfer a call out of CUC. This issue is documented in CSCuq64179 . In the case, the call is transfered to the 'Directory Handler' option after the Greeting is played. This type of conversation is identified as AD in the Output.

In order to check for Users:

```
admin:run cuc dbquery unitydirdb select c.displayname, g.greetingtype, aftergreeting_targetconversation from vw_callhandler as c inner join vw_greeting as g on c.objectid=g.callhandlerobjectid where isprimary = 1 and aftergreeting_targetconversation IN ('SystemTransfer','SubSysTransfer','AD') displayname  greetingtype  aftergreeting_targetconversation -----------  ------------  -------------------------------- Anirudh      Standard      SystemTransfer Anirudh      Alternate     SubSysTransfer test3        Off Hours     AD
```

In order to check for Call Handlers:

```
admin:run cuc dbquery unitydirdb select c.displayname, g.greetingtype, aftergreeting_targetconversation from vw_callhandler as c inner join vw_greeting as g on c.objectid=g.callhandlerobjectid where isprimary = 0 and aftergreeting_targetconversation IN ('SystemTransfer','SubSysTransfer','AD') displayname  greetingtype  aftergreeting_targetconversation -----------  ------------  -------------------------------- test2        Standard      SystemTransfer test3        Alternate     SystemTransfer test2        Alternate     SubSysTransfer
```

### Case 4 : 'Caller Input' Transfer to a Conversation Option

There are two types of conversations that can used to transfer the call during the greeting of the User or the Call Handler by provision of Dual Tone Multi Frequency (DTMF) input.

- Caller System Transfer - This conversation is identified as SystemTransfer in the Output.

- User System Transfer - This conversation is identified as SubSysTransfer in the Output .

Note : In earlier versions of CUC, a Voice Enabled Directory Handler can also be used to transfer a call out of CUC. This issue is documented in CSCuq64179 . In the case, the call is transfered to the 'Directory Handler' conversation during the Greeting by provision of DTMF input. This type of conversation is identified as AD in the Output.

In order to check for Users:

```
admin:run cuc dbquery unitydirdb select gu.alias, gu.dtmfaccessid, me.touchtonekey, me.targetconversation from vw_callhandler as ch inner join vw_menuentry as me on me.callhandlerobjectid=ch.objectid inner join vw_globaluser as gu on ch.recipient_globaluserobjectid=gu.objectid and ch.isprimary='1' where targetconversation IN ('SubSysTransfer','SystemTransfer','AD') alias    dtmfaccessid  touchtonekey  targetconversation -------  ------------  ------------  ------------------ Anirudh  8553          5             SubSysTransfer Anirudh  8553          8             SystemTransfer Test     8023          7             SystemTransfer
```

In order to check for Call Handlers:

```
admin:run cuc dbquery unitydirdb select ch.displayname, ch.dtmfaccessid, me.touchtonekey, me.targetconversation from vw_callhandler as ch inner join vw_menuentry as me on ch.objectid=me.callhandlerobjectid and ch.isprimary='0' where targetconversation IN ('SubSysTransfer', 'SystemTransfer','AD') displayname       dtmfaccessid  touchtonekey  targetconversation ----------------  ------------  ------------  ------------------ test2             4321          4             SubSysTransfer test2             4321          3             SystemTransfer test3             5321          5             SystemTransfer Opening Greeting  null          4             AD
```

### Case 5: User or Call Handler 'Transfer Rules'

A User or Call Handler's Transfer Rules has two options. The call can be transferred to the Greetings, or the User or Call Handler's extension. In the defaut configuration, a User or Call Handler's Transfer Rules is set to go to its Greetings. The extension field is prepopulated with the same extension configured for the User or Call Handler. In order to transfer the calls out, the extension field is selected. The extension field can be modified to send the call to any number.

During a greeting, a caller can dial any User or Call Handler's extension. The transfer rules determine the destination of the call and will send it to the configured extension instead of the dialed User or Call Handler's Greeting.

After a greeting, the call can be transferred to any User or Call Handler's Transfer Rules. In order to enable this, select the User or Call Handler in the 'After Greetings' section and choose 'Attempt Transfer'. The transfer rules determine the destination of the call and will send it to the configured extension instead of the dialed User or Call Handler's Greeting.

In order to check for Users:

```
admin:run cuc dbquery unitydirdb select gu.alias, gu.dtmfaccessid, t.transferoptiontype, t.extension from vw_globaluser as gu inner join vw_callhandler as ch on ch.recipient_globaluserobjectid=gu.objectid inner join vw_transferoption as t on ch.objectid=t.callhandlerobjectid and t.extension NOT in (select dtmfaccessid from vw_globaluser where dtmfaccessid != 'null') and t.extension NOT in (select dtmfaccessid from vw_callhandler where dtmfaccessid != 'null') alias    dtmfaccessid  transferoptiontype  extension -------  ------------  ------------------  --------- Anirudh  8553          Alternate           88553 Test4    8033          Standard            1111
```

Note : This query returns results of those Users whose transfer extension is not a known User or Call Handler.

In order to check for Call Handlers:

```
admin:run cuc dbquery unitydirdb select ch.displayname, ch.dtmfaccessid, t.transferoptiontype, t.extension from vw_callhandler as ch inner join vw_transferoption as t on ch.objectid=t.callhandlerobjectid and t.extension NOT in (select dtmfaccessid from vw_globaluser where dtmfaccessid != 'null') and t.extension NOT in (select dtmfaccessid from vw_callhandler where dtmfaccessid != 'null') and isprimary='0' displayname  dtmfaccessid  transferoptiontype  extension -----------  ------------  ------------------  ----------- test3        5321          Alternate           91408111222
```

Note : This query returns results of those Call Handlers whose transfer extension is not a known User or Call Handler.

## Solutions

The queries help the Administrator look out for configurations that are not authorized. However, it is not feasible to keep track of the configuration at regular intervals. Here are two options to prevent toll fraud on a system level.

### Option 1

The calls can be blocked as per the settings in the restriction table. More details on Restriction tables can be found in the Restriction Tables in Cisco Unity Connection section of the Call Management Overview in Cisco Unity Connection document. The Managing Restriction Tables in Cisco Unity Connection document provides details on the configuration aspects.

### Option 2

An alternate option is to modify the CSS on the Voicemail port or the Rerouting CSS on the trunk in the CUCM side. Include only the required partitions in the CSS.

### Revision History

1.0

01-Sep-2015

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 01-Sep-2015 | Initial Release |