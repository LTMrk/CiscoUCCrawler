---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-tdm-gateways-223040-troubleshoot-dsp-pvdm-issue-on-voice-html-65b4b70f05
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/tdm-gateways/223040-troubleshoot-dsp-pvdm-issue-on-voice.html
retrieved_at: 2026-08-21T07:08:42.390311+00:00
---

Troubleshoot DSP (PVDM) Issue on Voice Gateway

# Troubleshoot DSP (PVDM) Issue on Voice Gateway

### Download Options

Updated: June 3, 2025

Document ID: 223040

Contents

## Contents

## Introduction

This document describes solutions to common PVDM Card issues and provides methods to determine whether the issue is hardware-related or not.

## Troubleshoot

### Types of Packet Voice Digital Signal Processor Modules (PVDMs)

Supported Cisco Routers

Type of PVDM

28xx,38xx

PVDM2

29xx,39xx

PVDM2 and PVDM3

ISR 4Ks

PVDM4 and SM-X

C8300

PVDM4 , NIM-PVDM and SM-X

Note : PVDMs can be installed on the motherboard for ISR G1 and ISR G2.

For ISR 4K, PVDM can be installed on the motherboard and NIM slots.

For C8300, PVDM can be installed on NIM slots.

- Show voice dsp group all is the first command that everyone uses to check the state of a Digital Signal Processor (DSP).

- UP is a good state.

- FAIL and APP_DOWNLOADING are the bad states which one must be concerned about.

DSP is not in UP State.

1. Collect the output of the show voice dsp group all command.

2. A soft reset can be performed if DSPs are in a bad state. Enter the test dsp device <slot> <dsp-id> reset command for ISR G1(28xx, 38xx) and G2(29xx, 39xx) . For ISR 4Ks , use hw-module subslot x/y reload .

3. Check the PVDM slot from the inventory by applying the command Show inventory .

If the show inventory output shows this information, it signifies that the PVDM card is installed on the motherboard .

NAME: "PVDM subslot 0/4", DESCR: "PVDM4-32 Voice DSP Module"

PID: PVDM4-32          , VID: V02, SN: FOC13YYXXAVD

Once the PVDM card is placed on the NIM , the show inventory command indicates:

NAME: "subslot 0/1 db module 0" , DESCR: "PVDM4-128 Voice DSP Module"

PID: PVDM4-128         , VID: V01, SN: FOC1YYXXBLL

4. If the DSPs do not return to a UP state, RESEAT of PVDM card can be considered.

RESEAT means: Turning off the router, unplug the PVDM card, and plug it back in and then power on the router. It has to be done during off-hours .

Note : PVDM4 installed on NIM are hot swappable but the router must me shut down to insert or remove PVDM4 on the motherboard.

5. If one of the DSPs fails and cannot be recovered when you use any of these methods, enter the test dsp device <slot#> <DSP_ID> remove (G1/G2) and hw-module subslot x/y stop (ISR 4K/8K) commands in order to minimize the impact of DSPs that go into a DOWN state. This command will remove the particular DSP from participation and the router would not consider it for processing any calls or media resource activities.

Scenario: Suppose if you got DSP issue in Production hours. If you do not remove the particular subslot, call processed by those slot is affected. In order to avoid this it is removed from taking and making the calls,  not processing them.

6. If the steps mentioned in this article do not resolve the issue, Return material authorize ( RMA ) any DSP that does not return to a UP state.

### Revision History

2.0

03-Jun-2025

Initial Release

1.0

02-Jun-2025

Initial Release

### Contributed by

Ritesh Mishra

Cisco Consulting Engineer

### Customers Also Viewed

- Configure PRI Multi-clocking on C8300

### This Document Applies to These Products

- TDM Gateways

| Supported Cisco Routers | Type of PVDM |
|---|---|
| 28xx,38xx | PVDM2 |
| 29xx,39xx | PVDM2 and PVDM3 |
| ISR 4Ks | PVDM4 and SM-X |
| C8300 | PVDM4 , NIM-PVDM and SM-X |

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 03-Jun-2025 | Initial Release |
| 1.0 | 02-Jun-2025 | Initial Release |