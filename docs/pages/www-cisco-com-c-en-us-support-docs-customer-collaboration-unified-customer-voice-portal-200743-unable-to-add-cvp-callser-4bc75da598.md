---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-200743-unable-to-add-cvp-callser-4bc75da598
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal/200743-Unable-to-Add-CVP-CallServer-in-the-CVP.html
retrieved_at: 2026-08-16T19:24:23.278788+00:00
---

Unable to Add CVP CallServer in the CVP OAMP Server

# Unable to Add CVP CallServer in the CVP OAMP Server

### Download Options

Updated: September 12, 2018

Document ID: 200743

Contents

## Contents

## Introduction

This document describes an issue found when a Cisco Customer Voice Portal (CVP) Call Server is added via CVP Cisco Operations Console (OAMP) and also provides a feasible solution to it.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CVP Call Server

- CVP OAMP

### Components Used

The information in this document is based on CVP version 10.0.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Error is Reported when CVP Call Server is Added to CVP OAMP

When CVP Call Server is added to the CVP OAMP, an error is reported. This error is seen when you click on Save and Deploy .

Step 1. In order to add the CVP Call Server into CVP OAMP, sign in to CVP OAMP and navigate to Device Management > Unified CVP Call Server as shown in this image.

Step 2. Click Save and Deploy . You get an error which indicates that the CVP Call Server cannot be created because it already exist in another CVP Operations Console (OPSConsole) as seen in this image.

The target CVP Call Server has an OAMP id in its configuration and hence it will not let the second OAMP deploy it as seen in this image.

Step 3. Open the file C:\Cisco\CVP\conf\orm.properties . You can verify the OAMP Id as shown in this image.

## Solution

Step 1. Stop the Cisco CVP Resource Manager Service in the CVP Call Server.

Step 2. Comment out the orm.oamp.id line in C:\Cisco\CVP\conf\orm.properties as shown in this image.

Step 3. Start the Cisco CVP Resource Manager Service in the CVP Call Server.

Step 4. Click Save and Deploy as shown in this image.

### Contributed by Cisco Engineers

Ricardo Mancera

Cisco TAC Engineer

Ramiro Amaya

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Customer Voice Portal