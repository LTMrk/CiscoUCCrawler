---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-1000-217205-how-to-configure-meeting-title-displayed-html-95bcbcac97
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server-1000/217205-how-to-configure-meeting-title-displayed.html
retrieved_at: 2026-08-21T13:11:58.785828+00:00
---

How to Configure Meeting Title Displayed in the Lobby for CMS

# How to Configure Meeting Title Displayed in the Lobby for CMS

### Download Options

Updated: June 18, 2021

Document ID: 217205

Contents

## Contents

## Introduction

This document describes the steps required to configure the meeting name to be displayed in the lobby of the conference for Cisco Meeting Server (CMS).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CMS general configuration

- CMS Application Programing Interface (API)

### Components Used

The information in this document is based on CMS version 3.2.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configuration

Step 1. Create a new CallLegProfile via API.

- Access CMS via Webadmin and naavigate to Configuration/api/v1/callLegProfiles .

- Create new CallLegProfile and modify next parameters as shown in the image:

name : TECHZONE

meetingTitlePosition : middle

Note : The meetingTitlePosition has the next options available to be configured: top , bottom and middle .

Step 2. Assign the CallLegProfile to the space.

- Open the Webadmin and  navigate to Configuration/api/v1/coSpaces .

- Select the space required to assign the CallLegProfile created in Step 1.

CallLegProfile : 127874d9-ee5a-4679-8173-97b80bd06754

## Verify

Step 1. Verify if the configuration is applied successfully..

- Start a call to the space where the CallLegProfile is assigned and you must see the meeting title displayed in the lobby as shown in the image:

The parameter meetingTitleDisplayed configured with Top option is shown in the next image:.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Moises Martinez