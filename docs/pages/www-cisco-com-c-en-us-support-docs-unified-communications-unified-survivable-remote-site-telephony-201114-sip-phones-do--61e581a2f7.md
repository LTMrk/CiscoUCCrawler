---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-survivable-remote-site-telephony-201114-sip-phones-do--61e581a2f7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-survivable-remote-site-telephony/201114-SIP-Phones-do-not-Register-to-SRST-route.html
retrieved_at: 2026-08-21T21:30:06.661027+00:00
---

SRST Manager - SIP Phones do not Register to SRST Router

# SRST Manager - SIP Phones do not Register to SRST Router

### Download Options

Updated: March 16, 2017

Document ID: 201114

Contents

## Contents

## Introduction

This document describes solution for the issue when Session Initiation Protocol (SIP) phones do not register to Survivability Remote Site Telephony (SRST) gateway after provisioned by SRST Manager

## Problem

SIP phones do not register with SRST gateway after the site is provisioned using SRST manager. To register the phone, the administrator has to manually go and change the id mac to id ip in SRST gateway configuration under voice register pool. This will particularly happen if the phones are in different subnet

## Solution

Step 1 .  Clear all configuration (telephony service and voice register global) from router

Step 2 .  Log in to Cisco Unified Communication Manager (CUCM) administration

Step 3 .  Navigate to System->Security->Phone Security Profile and Check Enable Digest Authentication Step 4 .  On  CUCM, for each SIP phone, create a user with User ID = Device Name( Complete Media Access Control (MAC) address in format SEPAAAABBBBCCCC) and digest credentials = "Cisco" Step 5 .  Associate respective phones to respective users. On Phone setting page, select the respective user for Digest User Field Step 6 .  Now provision the site from SRST Manager Step 7 .  Go to router and configure

```
Voice register global
  authenticate register
  authenticate realm ccmsipline
```

Step 8 .  Do not do any other manual configuration Step 9 .  Now let the phones failover and they should register with the router

## Explanation

As per SRST Manager current design:

- If Phone is not attached to an end user (in CUCM under phone properties Owner field), SRST Manager makes use of MAC address as the username and configures on the router.

- For password SRST Manger by default pushes "Cisco" as the password is not going to be fetched from CUCM.

## Workaround

- Ensure that under phone configuration page Owner and Digest user is same.

- For password either manually edit the SRST router config to match the CUCM or specify "Cisco" as digest password for all users created in CUCM.

### Contributed by Cisco Engineers

Stuti Desai

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Survivable Remote Site Telephony