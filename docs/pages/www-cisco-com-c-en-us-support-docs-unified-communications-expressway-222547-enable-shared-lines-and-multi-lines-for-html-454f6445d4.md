---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-222547-enable-shared-lines-and-multi-lines-for-html-454f6445d4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/222547-enable-shared-lines-and-multi-lines-for.html
retrieved_at: 2026-08-16T15:43:31.553313+00:00
---

Enable Shared Lines and Multi Lines for MRA Devices

# Enable Shared Lines and Multi Lines for MRA Devices

### Download Options

Updated: October 25, 2024

Document ID: 222547

Contents

## Contents

## Introduction

This document describes how to enable shared lines and multi lines for MRA devices.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

Cisco Expressway Server Mobile and Remote Access (MRA)

### Components Used

This document is not restricted to specific hardware and software versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

In Cisco Unified Communications environments, shared lines and multi lines are features that allow users to manage multiple calls more effectively and provide greater flexibility in call handling. To configure this feature in MRA environments, it is mandatory to enable SIP Path Headers in the Expressway C server.

The default behavior for Expressway-C is to rewrite the Contact header in SIP REGISTER messages. When you enable SIP Path Headers, Expressway-C adds its address into the Path header but does not rewrite the Contact header. This setting is required for some features to work over MRA, including:

- Shared Lines and Multiple Lines

- BiB Call Recording

- Silent Monitoring

- Key Expansion Modules

## Configure

Step 1. On the Expressway-C, navigate to Configuration > Unified Communications > Configuration .

Step 2. Change SIP Path headers to On and save the change.

Step 3. Navigate to Configuration > Unified Communications > Unified CM servers .

Step 4. Click Refresh servers .

## Verify

Log out from your account on the MRA device and log back in to test the change.

### Revision History

1.0

25-Oct-2024

Initial Release

### Contributed by Cisco Engineers

Fernando Garrido Tapia

Technical Consulting Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 25-Oct-2024 | Initial Release |