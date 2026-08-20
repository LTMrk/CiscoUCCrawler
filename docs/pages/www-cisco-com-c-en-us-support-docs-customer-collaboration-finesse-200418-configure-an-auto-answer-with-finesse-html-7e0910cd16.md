---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-finesse-200418-configure-an-auto-answer-with-finesse-html-7e0910cd16
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/finesse/200418-Configure-an-Auto-Answer-with-Finesse.html
retrieved_at: 2026-08-20T21:16:30.692573+00:00
---

Configure an Auto Answer with Finesse

# Configure an Auto Answer with Finesse

Updated: April 11, 2016

Document ID: 200418

Contents

## Contents

## Introduction

This document describes how to configure an auto answer with Finesse.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Some contact centers that have upgraded to Unified Contact Center Express (UCCX) 10 or 11 and are using Finesse, have previously configured Cisco Agent Desktop (CAD) to auto answer incoming calls.  This is configured through CAD workflows in the previous release where there is a need to replicate the same with Finesse. Finesse gives more control to the admin to auto answer the calls as compared to Cisco Unified Communications Manager's (CUCM's) auto answer configuration.

## Configure

Navigate to Finesse Administration and click on the Workflows link to view the Manage Workflows page.

Create a new Action as shown in the image,

The dialogID and extension variables are used to populate the action with the information that Finesse needs to automate the answering of the call on the agent's extension.

Create a new Workflow as follows, which will be executed when a call arrives. The Answer Action configured above must be assigned to this worfklow as shown in the image.

Finally, assign this workflow to the desired Teams via Finesse Admin's Team Resources page.

If you would like auto answer to apply to only certain agents within a team, add conditions to the workflow to match particular agents.The same can be done to have only certain call flows auto answered, using any of the call information presented to Finesse.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

31-Mar-2016

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 31-Mar-2016 | Initial Release |