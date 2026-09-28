---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-221044-configure-and-troubleshoot-survey-featur-html-e2bdf9fe24
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/221044-configure-and-troubleshoot-survey-featur.html
retrieved_at: 2026-08-18T23:49:53.557481+00:00
---

Configure and Troubleshoot Survey Feature in Cisco Meeting Server

# Configure and Troubleshoot Survey Feature in Cisco Meeting Server

### Download Options

Updated: October 5, 2023

Document ID: 221044

Contents

## Contents

## Introduction

This document describes the steps to configure and troubleshoot Survey Feature on Cisco Meeting Server (CMS).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Meeting Server version 3.8 and later.

### Components Used

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

In Cisco Meeting Server Version 3.8 , Survey feature is introduced which allows meeting app host to create survey in a meeting and participants can take part in survey and share their opinion and it makes meeting more interactive.

- Survey Feature was introduced in Cisco Meeting Server 3.8, WebApp Meeting Hosts can create a survey in meetings.

- Participants can take part in a survey activated by the meeting host.

- WebApp meetings can have one survey at a time.

- Each survey can have a maximum of 5 questions and can have a minimum of 2 or a maximum of 5 choices.

- Multiple answer entries or free-form text answers are not allowed in this release.

- A meeting organizer who creates a survey cannot take part in the survey.

- Meeting participants can take the survey anytime till it ends even after the participant disconnects from the meeting and joins back.

- Users cannot edit/modify the survey once it is submitted.

## Configure

- Survey Feature uses meetingapps services in CMS, it acts as prerequistes, meetingapps services can be configure by refering given link

- The Survey Feature can be enabled on the call level for a specific call or on the callprofile level which can be applied to a coSpace or System level using the new field surveyAllowed introduced in CMS 3.8 which can be set to false|true .

### Enable survey feature for participants

#### Option 1. To enable Survey Feature on callprofile level.

Step 1. Login in CMS GUI and navigate to Configuration > API > callprofile and set surveyAllowed to true .

Note : Once callprofile is enabled with Survery Feature, apply the callprofile on coSpace/<coSpace ID> or system/profiles to take effect

#### Option 2. To enable Survey Feature on call level.

Step 1. Login in CMS GUI and navigate to Configuration > API > calls and set surveyAllowed to true for specific call.

Step 2. The survey icon is visible to the participants in the right side pane once surveyAllowed is set to True in callprofile/call level :

### Enable Survey Feature for host

Survey Feature for host allow the meeting host to create/launch/delete/view surveys in meetings and this can be enabled in callleg profile and call leg by setting surveyOpsAllowed to true or false

#### Option 1. To enable Survey Feature on  call leg id .

Step 1. Login in CMS GUI and navigate to Configuration > API > calls and set surveyOpsAllowed to true for specific call leg id.

#### Option 2. To enable Survey Feature on  calllegProfile .

Step 1.Login in CMS GUI and navigate to Configuration > API > callLegProfiles and set surveyOpsAllowed to true .

Note :Enabling surveyOpsAllowed at calllegprofile gives the Survey Dashboard option to all the participants and all the participants can create/launch/delete/view the survey in the meeting.

We can restrict surveyOpsAllowed to only the intended users or host by using access methods in the Meeting organizers space:

Step 1. Create a host callLegProfile ( surveyOpsAllowed = true )

Step 2. Create a guest callLegProfile (surveyOpsAllowed = false )

Step 3. Create a new accessMethod on Meeting organizers space and assign host and guest callLegProfile .

Step 4. Users joining space as a Host have Survey Dashboard option and be able to create/launch/delete/view surveys in meetings.

## Verify

- Schedule a meeting using WebApp.

- Enable " surveyAllowed "  as described in the configuration section.

- Enable “ surveyOpsAllowed ” as described  in the configuration section for participants to create/launch/delete/view the survey.

- Once “ surveyOpsAllowed ” is activated for the user, the user can view “ Survey Dashboard ” once the user clicks on the Survey Icon

- Host can create a Survey by clicking “ Survey Dashboard " followed by “ Create Survey ":

- Once Survey questions are created host clicks on “Save” and after that Survey can be launched using the red highlighted icon in te screenshot

- Once the host launches the survey, other participants sees the icon and once the participant clicks on this icon, they can take the survey and submit a response.

- The survey organizer/Host can end the survey using the icon and view the survey results using the icon and “close” the survey.

## Troubleshoot

- Make sure meetingapps are properly configured and we can check the connection using URL and get the ping result:

https://<meetingapps FQDN/IP >:port/api/ping.

- CMS logs once survey is enabled:

```
2023-09-13  17:46:17.258  Info     API trace 83: GET for "/api/v1/callProfiles/0cc3a91c-ddad-45e3-a1e0-64f7dd34c8ab" (from API Explorer)
2023-09-13  17:46:17.258  Info     httpServerOperation_getContentInfo
2023-09-13  17:46:17.259  Info     API trace 83: sending 200 response, size 238
2023-09-13  17:46:17.259  Info     API trace 83:  <callProfile id="0cc3a91c-ddad-45e3-a1e0-64f7dd34c8ab">
2023-09-13  17:46:17.259  Info     API trace 83:  <name>Survey Profile</name>
2023-09-13  17:46:17.259  Info     API trace 83:  <participantLimit>1000</participantLimit>
2023-09-13  17:46:17.259  Info     API trace 83:  <fileReceiveAllowed>true</fileReceiveAllowed>
2023-09-13  17:46:17.259  Info     API trace 83:  <surveyAllowed>true</surveyAllowed>
```

- Client Browser HAR File:

callLegProfileTrace :

If user see the error message which can be due to certificate issue or Service not reachable.

If you get this message than click on the " link " and it pops up to accept the certificate , once certificate accepted it shows {"ping": "pong!"} if no issues with connectivity.

## Related Information

CMS 3.8 Release Notes

### Revision History

1.0

05-Oct-2023

Initial Release

### Contributed by Cisco Engineers

Vikas Kumar

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Oct-2023 | Initial Release |