---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-applications-cisco-unified-application-environment-220161-trou-1702779532
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/applications-cisco-unified-application-environment/220161-troubleshoot-customer-voice-portal-cvp.html
retrieved_at: 2026-08-16T19:21:41.950129+00:00
---

Troubleshoot Customer Voice Portal (CVP) Transfers Wrong Automatic Number Identification (ANI)

# Troubleshoot Customer Voice Portal (CVP) Transfers Wrong Automatic Number Identification (ANI)

### Download Options

Updated: January 26, 2023

Document ID: 220161

Contents

## Contents

## Introduction

This document describes how Customer Voice Portal (CVP) extracts Automatic Number Identification (ANI) from inbound call.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Contact Center Enterprise (UCCE)

- Cisco Unified Customer Voice Portal (CVP)

### Components Used

The information in this document is based on these software and hardware versions:

Cisco Unified Contact Center Enterprise (UCCE) 12.6

Cisco Unified Customer Voice Portal (CVP) 12.6

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

CVP by design extracts ANI from the user portion of the P-Asserted-Identity header (PAI) or From header of inbound INVITE in the order of PAI header followed by From header (if no is PAI present) and sends this information in the NEW-CALL request to UCCE. In versions before 11.0, CVP only checks From header. This logic broke in version 11.6 and was addressed as part of the Engineering Special(ES)11.

## Problem:

Why Customer Voice Portal (CVP) passes wrong Automatic Number Identification (ANI) to UCCE?

CVP does not extract the correct ANI from the incoming INVITE if the Telecommunication carrier sends additional information in the PAI header or a different ANI than the actual ANI in the PAI header.This causes CVP to send incorrect ANI to UCCE and can cause business logic to fail.

Example 1

PAI header has additional information in the user portion.

P-Asserted-Identity: "NETWORK" <sip:+13067890000;rn=303357;oli=00@192.168.1.1:5060;user=phone>

Example 2

ANI is different in PAI and From headers.

From: <sip:12567891234@192.168.1.1:5060;user=phone;isup-oli=00>;tag=a3df5c45 P-Asserted-Identity: "NETWORK" <sip:+13067890000@192.168.1.1:5060;user=phone>

## Solution

- If call originates from Cisco Unified Border Element (CUBE) use the SIP profile to change Automatic Number Identification (ANI) to actual ANI in the PAI or From header and apply on the outbound dial-peer to CVP/Cisco Unified SIP Proxy Server (CUSP).

- For Cisco Unified Communication Manager (CUCM) originated calls configure SIP Normalization Script in SIP trunk toward CVP/CUSP.

- Use micro application Expanded Call Context (ECC) variable user.microapp.override_cli in the Unified Contact Center Enterprise script to override ANI in outbound transfers from CVP.

## Related Information

- How to configure Expanded Call Context (ECC) variable

- Configure SIP Normalization Script in CUCM

- Configure SIP profiles in CUBE

### Revision History

1.0

30-Jan-2023

Initial Release

### Contributed by Cisco Engineers

Binu Santhakumaran

TAC Engineer

### This Document Applies to These Products

- Unified Contact Center Enterprise

- Unified Customer Voice Portal

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 30-Jan-2023 | Initial Release |