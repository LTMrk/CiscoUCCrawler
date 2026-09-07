---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-advanced-202617-technote-on-attendan-07ba5894d9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-advanced/202617-technote-on-attendant-console-multiple-t.html
retrieved_at: 2026-09-07T15:49:28.307802+00:00
---

TechNote on Attendant Console Multiple TSP Instance

# TechNote on Attendant Console Multiple TSP Instance

### Download Options

Updated: November 2, 2017

Document ID: 202617

Contents

## Contents

## Introduction

This document describes how to troubleshoot the scenario where one or more Telephony Service Provider (TSP) instance still exists in Advance tab ( control panel > phone and modem > Advance tab ) even after TSP application is uninstalled from that server.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Attendant Console (CUAC) Advanced 10.5.2 / 11.0.1

- Unified Communications Manager IM & Presence Service 10.5.2/11.X

- TSP Configuration

### Components Used

This document is not restricted to specific hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem: Issue with the Multiple TSP Instance

As shown in the image, one or more TSP instance is still visible while you navigate to phone and Modem > Advance tab even after un-installation of TSP

Both, Remove and Configure buttons are greyed out and hence deletion is not possible.

## Solution

Step 1. Initiate installation of TSP.  Navigate to CUCM Pub > Cisco Unified CM Administration page > Application > Plugin . Click in Download as shown in the image and move the setup of 32 bit or 64 bit client based on your CUAC server Windows OS Bit size.

Step 2. Enter the value two for How many Cisco Unified Communications Manager TSP’s to instal l (Choose from 1 to 10) ?

This value defers on the number of instances left over. In our scenario it is CiscoTSP002.tsp which means that there were at least two instances installed initially. Instance left over can also be CiscoTSP003.tsp and in such cases value three is selected. There can also be scenarios where in CiscoTSP002.tsp , CiscoTSP003.tsp and CiscoTSP004.tsp is left over, select four, which is the highest value.

Step 3. After installation and restart of Attendant console server navigate to Phone and Modem > Advance tab . Now you can see three instances CiscoTSP001.tsp, CiscoTSP002.tsp and CiscoTSP002.tsp . Select any one CiscoTSP002.tsp and click Remove , as shown in the image:

Step 4. Uninstall and install TSP once again as per the procedure mentioned in Cisco Administration Guide.

### Contributed by Cisco Engineers

Manjunath Sheregar

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Attendant Consoles