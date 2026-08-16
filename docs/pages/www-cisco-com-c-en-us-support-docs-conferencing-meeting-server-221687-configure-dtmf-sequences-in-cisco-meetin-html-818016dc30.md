---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-221687-configure-dtmf-sequences-in-cisco-meetin-html-818016dc30
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/221687-configure-dtmf-sequences-in-cisco-meetin.html
retrieved_at: 2026-08-16T14:21:16.245683+00:00
---

Configure DTMF Sequences in Cisco Meeting Server Spaces

# Configure DTMF Sequences in Cisco Meeting Server Spaces

Log in to Save Content

### Download Options

Updated: February 15, 2024

Document ID: 221687

Contents

## Contents

## Introduction

This document describes the steps to configure DTMF sequences to allow users to perform actions on Cisco Meeting Server (CMS) spaces.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Meeting Server

- DTMF

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Meeting Server running software version 3.8

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

It is possible to define custom DTMF sequences in CMS for space participants to use to to invoke actions that affect the space and its participants. For example, a DTMF sequence can be used by a participant to toggle their own audio mute, to start or stop streaming the meeting, or to end the meeting.

A dtmfProfile defines the DTMF sequences to be used to invoke each specific action available. By assigning a dtmfProfile to system/profiles via the CMS API, the DTMF sequences become available globally. Restrictions for the DTMF actions can be fine tuned by creating callLegProfiles with different with permissions for each of the actions, and by applying them at different levels of the API.

## Configure

### 1. Create a dtmfProfile object and apply it globally

To create the dtmfProfile object:

1. Log in to the CMS web admin page.

2. Navigate to Configuration > API .

3. Navigate to the /api/v1/dtmfProfiles section and expand it.

4. Click Create new .

5. Define the DTMF sequences to be used to perform the required action(s). In this example, DTMF sequences are defined for the toggleMuteSelfAudio and endCall actions.

6. Click Create .

To apply the dtmfProfile globally:

1. Navigate to Configuration > API .

2. Navigate to the /api/v1/system/profiles section and expand it.

3. Click View or edit .

4. On the dtmfProfile setting, click Choose and select the previously created object.

5. Click Modify .

### 2. Fine tune permissions to perform the DTMF actions

Granular control of permissions to execute the DTMF action can be achieved by configuring callLegProfiles , which can be applied at different levels in the API. This diagram illustrates all possible levels:

The level at which the callLegProfile is applied determines its scope. Profiles assigned at lower levels override those set above. These examples illustrate how this principle can be utilized to allow invoking DTMF actions to only certain spaces or users.

#### Allow Actions in a Specific Space Only

A callLegProfile negating permissions to execute the DTMF actions can be created and applied at the /system/profiles level. Then, another callLegProfile allowing the actions can be created and applied at the coSpace level, therefore limiting the scope of the permissions to a specific coSpace (or a set of coSpaces , if applied to several).

1. Navigate to Configuration > API .

2. Navigate to the /api/v1/callLegProfiles section and expand it.

3. Click Create new .

4. Navigate to the actions that need to be disallowed, and set them to false.

5. Click Create .

In this example a callLegProfile has been created to disallow ending the meeting by setting endCallAllowed to false :

Tip : If a suitable callLegProfile already exists, it can be modified instead of creating a new one.

6. Assign it to system/profile to globally disallow the action:

7. Create a new callLegProfile, this time to allow the action. In this example a callLegProfile has been created with endCallAllowed set to true :

8. Navigate to Configuration > API > /api/v1/coSpaces and expand it.

9. Find the coSpace that you want to assign it to, and under callLegProfile , choose the one you created to allow the actions.

Since this callLegProfile is applied at a lower API level, it overrides the callLegProfile previously applied to /system/profiles , resulting in the DTMF actions being invokable from this particular coSpace only.

#### Allow Only Users With a Password to Perform the Actions

The scope of the permissions can be narrowed down to a group of users requiring special rights, like video operators. An accessMethod can be created, with its own directory number, to access a coSpace with a specific callLegProfile in effect that allows the DTMF actions.

1. Navigate to Configuration > API > /api/v1/coSpaces and expand it.

2. From the list, choose the coSpace you want to create the accessMethod for.

3. from the Related objects list, click the /api/v1/coSpaces/<coSpace ID>/accessMethods link:

4. On the uri field, enter a number for privileged users to dial into this space.

5. Create a passcode . When privileged users dial the accessMethod number, they need to enter this code followed by the # sign to be allowed into the meeting.

6. Under callLegProfile , choose the one that allows ending the call.

7. Optionally, enter a name for the accessMethod to make it easily recognizable from within the API explorer.

In this example an accessMethod with number 3001 is created for video operators to use when joining the coSpace (the directory number 3000 has been assigned to the coSpace , regular users dial this number to join meetings on this space). It is protected by a password, and the callLegProfile that allows ending the call is assigned to it exclusively.

8. Apply the callLegProfile that disallows the actions is globally by assigning it to system/profiles .

In this example, there is no need to assign a callLegProfile to the coSpace itself. It inherits the globally applied profile, and therefore users that join the meeting by dialing the coSpace number (3000) do not have permission to end the call via DTMF.

As a result of this configuration, video operators can join the meeting by dialing the accessMethod number (3001) instead of the coSpace number (3000). Their call legs use the callLegProfile that allows the action to be applied, therefore only they can use the defined DTMF sequence to end the call.

## Related Information

CMS 3.8 API Reference Guide

### Revision History

1.0

15-Feb-2024

Initial Release

### Contributed by Cisco Engineers

Fabio Achi

Technical Consulting Engineer

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

### This Document Applies to These Products

- Meeting Server

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 15-Feb-2024 | Initial Release |