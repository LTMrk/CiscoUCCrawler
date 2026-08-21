---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-management-218237-configure-dial-blast-on-cisco-meeting-ma-html-2d1563db41
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-management/218237-configure-dial-blast-on-cisco-meeting-ma.html
retrieved_at: 2026-08-21T06:27:54.254794+00:00
---

Configure Dial Blast on Cisco Meeting Manager

# Configure Dial Blast on Cisco Meeting Manager

### Download Options

Updated: October 5, 2022

Document ID: 218237

Contents

## Contents

## Introduction

This document describes how to configure the dial blast feature that enables a User to dial out to multiple meeting participants from a Space.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Meeting Server (CMS)

- Cisco Meeting Manager (CMM)

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Workflow

A Space is enabled for dial blast A space owner or a guest dials into blast dial enabled space.

Space dials out to multiple participants at once. Broadcast calls are made to all Endpoint addresses which are added under the Blast Dial configuration page.

Supports only SIP dial-out (use an interworking gateway to interwork into SIP > H323, like VCS/Expressway).

### Configurations

Navigate to Settings > Blast dial monitoring and select Primary .

Note : If you have multiple CMMs in your environment, select your primary CMM to initiate a Dial blast outbound calls. If for some reason, primary CMM is down, and Secondary CMM has to be used to blast dial-out calls, select secondly. In this example, there is 1 CMM in the lab, so make this primary CMM dial out.

Now, since Blast dial has been enabled, select the CMS cluster (if you have added multiple clusters on 1 CMM) and space from where you want to initiate blast dial.

Click on Space name and enable the space for blast dial. Now you have allowed blast dial for a space as shown in the image.

Note : This configuration enables a broadcast dial-out from a chosen Space.

Add Sip address/URL to be dialled out from Space 22222. Click on Add contact .

Add contact as shown in the image.

You can add as many as 100 contacts. 100 Endpoints are dialled out as soon as 1 participant dials into this space. Blast dial is initiated only when space gets activated when some user/sip device calls into this space. Here you can set the list of contacts to be called simultaneously whenever someone dials into this space. A maximum of 100 dial-out contacts can be configured.

Another essential configuration for blast dial is Outbound rules. Ensure that the outbound rule is configured correctly to route the call from CMS to the next hop (call control). Calls can fail if outbound rules are missing or incorrectly configured.

For this lab, outbound rules are configured to route the domain s.com to call control 10.106.80.57 (Expressway).

## Verify

Use this section in order to confirm that your configuration works properly.

In order to test the blast dial, initiate a webrtc call to space 22222. CMS dials out to add contacts under the dial blast space page on CMM.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

06-Oct-2022

Initial Release

### Contributed by Cisco Engineers

Vikram Dutta

Cisco TAC Engineer

Arun Rajendran

Cisco TAC Engineer

### Customers Also Viewed

- Deferral Advisory Notice for Cisco Meeting Management Release 3.13.0

### This Document Applies to These Products

- Meeting Management

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 06-Oct-2022 | Initial Release |