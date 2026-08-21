---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-enterprise-117777-config-ucce-00-html-a9105cbd5c
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-enterprise/117777-config-ucce-00.html
retrieved_at: 2026-08-21T04:21:23.816350+00:00
---

UCCE Integration with CM Configuration Example

# UCCE Integration with CM Configuration Example

Updated: March 23, 2016

Document ID: 117777

Contents

## Contents

## Introduction

This document describes to end users how to quickly walk through a Communications Manager (CM) server setup and verify that all the proper settings for a Unified Contact Center Enterprise (UCCE)/Cisco Unified Contact Center Express (UCCX) integration with CM are in place. If any of these settings are incorrect, then various different problems are expected to occur (such as you are not able to control the agent line, you receive a duplicate Distinguished Name (DN) error/Share Line error, and so on). The Technical Assistance Center (TAC) requests the modification of the parameters if any are incorrect. This document is also necessary for UCCX integrations.

## Prerequisites

### Requirements

Cisco recommends that you have agents configured with DNs already configured on CM and integrated within UCCE.

### Components Used

The information in this document is based on these software and hardware versions:

- CM 6.X Revision 11.x, installed

- UCCE 7.x Revision 10.5, installed

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

If your agents use 8900 Series or 9900 Series phones, you must enable Multi-Line on the Unified Communications Manager peripheral. Since this configuration option is a peripheral-wide option, if you enable Multi-Line for even one agent who uses an 8900 Series or 9900 Series phone then you must enable it for all agents. You must configure all phones with these settings: • Set Maximum number of calls to 2. • Set Busy trigger to 1.

### Network Diagram

UCCE and CM configured with a 'PGUser' type associated on both sides.

### Configuration

As shown in this example, there is a 'pguser' configured within the Application User and not End User. This is very important.

The five Groups and Roles selected here are the only Groups/Roles that should be selected for the vast majority of integrations. If any else are needed, let the TAC make that recommendation.

Do not choose the 'Standard CTI Allow Control of All Devices' selection because this causes other issues. The 'Standard CTI Allow Control of Phones supporting Connected Xfer and conf' selection is necessary for newer SIP phone models to work properly.

- Duplicate DNs are not supported

- Duplicate DNs with different partitions are not supported

- Call Park and call pickup is not supported

- Hunt Groups are not supported

- Computer Telephony Integration (CTI) Route Points and CTI ports should never be duplicated because that causes issues

In order to verify these values, click the agent phone and choose Agent DN.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Unsupported Configurations

Call pickup and call park are not supported with UCCE/UCCX monitored extensions. Hunt groups are not supported either.

### Revision History

1.0

17-Jun-2014

Initial Release

### Contributed by Cisco Engineers

William Ryan Bennett

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Contact Center Enterprise

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Jun-2014 | Initial Release |