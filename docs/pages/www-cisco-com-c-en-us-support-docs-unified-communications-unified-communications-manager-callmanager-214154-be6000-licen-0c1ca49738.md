---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214154-be6000-licen-0c1ca49738
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214154-be6000-licensing-support-on-cucm.html
retrieved_at: 2026-08-21T13:58:21.966911+00:00
---

BE6000 Licensing Support on CUCM

# BE6000 Licensing Support on CUCM

### Download Options

Updated: March 5, 2019

Document ID: 214154

Contents

## Contents

## Introduction

This document describes the License Support for Business Edition 6000 (BE6000) starter Licenses on Cisco Unified Communications Manager (CUCM) version 12.5.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM version 12.5

- BE6000

### Components Used

The information in this document is based on Cisco Call Manager version 12.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Along with the Bootable ISO, OVA’s, BE6000 also comes with some starter license bundle. These Starter License bundle can be of two types:

- UCL – Licenses adjusted among Enhanced, Basic & Essential

- UWL- Licenses adjusted among CUWL, Enhanced Plus, Enhanced, Basic & Essential

UCM when setup in BE6000 mode to request and consume BE6000 specific license so to avoid cross usage in other solution offers. The administrator can enable/disable BE6000 mode through CLI.

While the mode is selected confirm which Starter Pack licenses are required (None/UCL/UWL). Starter Pack licenses will be BE6000 UCL Starter Bundle or BE6000 UWL Starter Bundle or None.

This is the procedure to enable BE6000 licensing mode

- utils BE6000Mode disable

- utils BE6000Mode enable

- utils BE6000Mode status

- While BE6000 mode is enabled, the administrator selects UCL or UWL starter bundle or NONE.

- UCL – Licenses adjusted among Enhanced, Basic & Essential

- UWL- Licenses adjusted among CUWL, Enhanced Plus, Enhanced, Basic and Essential

- License Management UI displays the license consumption and deployment mode.

- Only 35 licenses are adjusted to UCL & UWL starter pack.

Note : Product instance must be deregistered from Cisco Smart Software Manager or satellite before this utils BE6000Mode enable command is executed.

BE6000 Mode is enabled only when the product instance is in Enterprise Mode.

### License Management UI

After BE6000 mode is enabled, you can observe these changes on License Management UI:

- Displays the licensing mode as BE6000.

- BE6000 UCL Starter Bundle.

- BE6000 UWL Starter Bundle.

- When you add more devices or associated with the user, the license is fulfilled first from the start pack bundle.

- Once the starter pack bundle is exhausted which means we have used all 35 licenses then the next license fulfilment would be from normal via CSSM.

- The Current Usage column shows as 0 until it has exhausted all the 35 starter pack licenses.

Note : License Consumption will be adjusted among CUWL, Enhanced Plus, Enhanced, Basic & Essential based on starter bundle chosen. ‘*’ symbol is displayed against licenses that are adjusted from a BE6000 starter bundle.

## Verify

In this image, BE6000 Mode is disabled.

BE6000 Mode is enabled with UCL Starter Bundle, as shown in the image.

BE6000 Mode is enabled and UWL starter pack is Selected.

BE6000 Mode enabled and none is selected.

## Troubleshoot

In case of any issue, you need to collect these logs :

- Smart agent logs are a part of slm.log ( activelog/cm/trace/slm/log4j/slm.log )

- activelog/cm/trace/slm/log4j/gch.log

- activelog/cm/trace/slm/log4j/tp.log

### Contributed by Cisco Engineers

Abhineet Kumar

Cisco TAC Engineer

Divya Jain

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)