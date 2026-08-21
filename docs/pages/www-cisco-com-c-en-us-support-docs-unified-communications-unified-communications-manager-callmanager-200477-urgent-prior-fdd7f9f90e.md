---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200477-urgent-prior-fdd7f9f90e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200477-Urgent-Priority-Configuration-on-Directo.html
retrieved_at: 2026-08-21T13:55:26.274329+00:00
---

Urgent Priority Configuration on Directory Number

# Urgent Priority Configuration on Directory Number

### Download Options

Updated: May 12, 2016

Document ID: 200477

Contents

## Contents

## Introduction

This document describes the feature Urgent Priority Configuration on Directory Number (DN). With this feature in use, administrator can avoid the T302 timer delay.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unified Communications Manager (CUCM) version 10.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Up until CUCM version 9, even if a caller dialed a fully qualified DN, you had to hit the T302 timer and wait for the user to dial futher digits, before the T302 timer expireed.

An administrator will now be able to configure DNs as urgent patterns to avoid T302 timer delay. In case a fully qualified DN is dialed, and overlap patterns exisits in the system, it hits the T302 timer and waits for the user to dial further digits before the timer expires.

## Configure

Check the Urgent Priority box to configure as shown in this image.

## User Experience

When Urgent Priority is enabled on Directory Number Configuration Page, the call is routed at once to the fully qualified DN without any necessity to wait for inter-digit-timeout. If the Urgent Priority checkbox is disabled and you have overlap patterns configured, then CUCM waits for the user to dial further digits.

- Before 10.0 CUCM release, the user had to observe the T302 (inter digit timer) before the call got routed to the dialed directory number, if there was an overlap pattern configured on the CUCM system. This happened even if the directory number pattern was a best match for the dialed digits. Without the urgent priority option configured on Directory Number, you observed post-dial delay after you dialled the directory number, in case of an overlap pattern in the dial plan.

- This features forces a call routing decision at once (without T302 timer started ) upon the directory number to be matched, even if there is an overlap pattern in the dial plan.

## Call Scenarios

- You have configured globalized dial plans like internal directory number that are configured in the E.164 format.

- You also have non urgent Route pattern \+.! in order to dial international destinations addressed by same calling search space as internal DNs

- In such cases whenever internal DN is dialed digit by digit in its E.164 format, CUCM starts inter digit timer because route pattern for international destination is also a potential match for the dialed digits. CUCM then routes the call to DN only after inter digit timer is expired

- Inter digit timer value is specified in service parameter T302 present under Clusterwide Parameters (Device - General) section. (Default Value = 15 seconds)

### Scenario 1

You configured a Translation Pattern (TP) (for example. 666X) with called party transformation mask set to 7770.

You configured a DN (7770) with urgent priority enabled. You have an overlap Route Pattern (RP) (for example. 777XX) configured. Hit New Call and then dial the digits. The call will be routed and you don't have to wait for inter-digit timeout.

### Scenario 2

You have configured a DN (for example. 919555888899) with urgent priority enabled. You have configured overlap Translation Pattern (for example. 91XXX XXXX XXX) with UP enabled.

Hit New Call and then dial the digits. The call will be routed and you don't have to wait for inter-digit timeout.

## Interaction with Speed Dial Parameter (SP)

- When speed dial (configured with a particular destination number) is pressed, CUCM would route the call to the destination configured with immediate effect.

- But if service parameter Speed Dial Await Further Digits  = true and, there is a further potential match present for the speed dial number apart from the best match, then CUCM waits for inter digit time out, so that user can dial additional digits manually.

- However, if this service parameter is true and pattern (best match) is marked as urgent, then CUCM does not wait for inter digit timer to expire, and routes the call to the destination.

- For example, if CUCM system has these patterns:

\+ 19195558888 ( Non Urgent DN )

\+.! ( Non urgent route pattern  for international calls )

- If SP = true and +1 9195558888 is configured as speed dial and speed dial is hit, CUCM will wait for inter digit timeout to allow users to dial additional digits and call will be routed using route pattern if additional digits are dialed

- But if DN is marked as urgent, CUCM will immediately route the call to DN without starting inter digit timer

For Example:

Configure Speed Dial No. +8536247900 Configure 2 Patterns: 1. +8536247900 2. +85!   [Non Urgent]

- Set SP Await Further Digits = true and make +8536247900 Non urgent. Speed Dial +8536247900. The call goes to the pattern +8536247900 after the inter-digit-timeout has expired.

- Set SP Await Further Digits = true and make +8536247900 Urgent. Speed Dial +8536247900. The call goes to the pattern +8536247900 while you dont have to wait for inter-digit timeout.

- Set SP Await Further Digits = false and make +8536247900 Non urgent. Speed Dial +8536247900. The call goes to the pattern +8536247900 while you dont have to wait for inter-digit timeout.

- Set SP Await Further Digits = false and make +8536247900 Urgent. Speed Dial +8536247900. The call goes to the pattern +8536247900 while you dont have to wait for inter-digit timeout.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration