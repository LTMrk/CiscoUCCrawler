---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-consoles-118860-technote-cuacs-00-html-859650320d
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-consoles/118860-technote-cuacs-00.html
retrieved_at: 2026-09-07T15:49:24.534722+00:00
---

Cisco Unified Attendant Console Standard Compatibility Matrix

# Cisco Unified Attendant Console Standard Compatibility Matrix

### Download Options

Updated: September 27, 2018

Document ID: 118860

Contents

## Contents

## Introduction

This document describes the compatibility between Cisco Unified Attendant Console Standard (CUACS) with Cisco Unified Communications Manager (CUCM) and a Microsoft Windows machine. It does not provide information in regards to installation. Refer to the Release Notes and Install Guide in order to learn about all the requirements before server installation.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUCM and CUAC.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## How to Use the Matrix

Look for the CUACS version that you run on the Y-axis in the table. Check for the supported CUCM version on the X-axis. In the tables X means supported.

## Compatibility Matrix

### CUACS Compatibility with CUCM

This is the CUACS Compatibility Matrix with CUCM:

7.1(5)**

8.O.1*

8.0(3)*

8.5***

8.6

9.0.1

9.1(1)

9.1(2)

10.0(1)****

10.5(1)****

10.5(2)

11.0.1

11.5.X

12.0.1

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

* Not supported when you run under a 64-bit Operating System (OS). ** Not supported when you run under Windows 7 (32-bit) or any other 64-bit OS. Cisco Unified Presence Version 7.1.5 is not supported. *** Supported on Service Update (SU) 1 and above. **** The only CUCM release supported under Windows 8 (64-bit). Supported on Windows 8.1 when you run with CUCM 10.5.1 and later.

### CUACS Compatibility with CUCM and Windows

This is the compatibility matrix for specific versions of CUACS with CUCM and Windows.

#### CUACS Version 10.0.1 Compatibility with CUCM and Windows

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

* CUP Version 7.1(5) is not supported. ** CUCM Version 8.5(1) is supported on SU1 and later.

#### CUACS Version 10.5.1 Compatibility with CUCM and Windows

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

* CUP Version 7.1(5) is not supported.

** CUCM Version 8.5(1) is supported on SU1 and later.

#### CUACS Version 10.5.1 SR1 Compatibility with CUCM and Windows

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

* CUP Version 7.1(5) is not supported.

** CUCM Version 8.5(1) is supported on SU1 and later.

#### CUACS Version 10.6.0 Compatibility with CUCM and Windows

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

* CUP Version 7.1(5) is not supported.

** CUCM Version 8.5(1) is supported on SU1 and later.

#### CUACS Version 11.0.1 Compatibility with CUCM and Windows

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

#### CUACS Version 11.0.2 Compatibility with CUCM and Windows

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

Refer to defect CSCva24885 if you run a CUCM 11.5 version earlier than 11.5 (1.13032-4).

#### CUACS Version 11.0.3 Compatibility with CUCM and Windows

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

Refer to defect CSCva24885 if you run a CUCM 11.5 version earlier than 11.5 (1.13032-4).

* Supported for CUCM version 10.5.2.14900-16 or later

The requirements outlined under Further Problem Description must be satisfied before new installations and upgrades to CUACS 11.0(3).

#### CUACS Version 12.0.X Compatibility with CUCM and Windows

X

X

X

X

X

X

X

X

X

X

X

* Supported for CUCM version 10.5.2.14900-16 or later.

** Supported for CUCM version 11.0.1.22900-14 or later.

### Contributed by Cisco Engineers

Alok Singh

Cisco TAC Engineer

Manjunath Sheregar

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| CUCM | >>>>> |
|---|---|
| CUACS | 7.1(5)** | 8.O.1* | 8.0(3)* | 8.5*** | 8.6 | 9.0.1 | 9.1(1) | 9.1(2) | 10.0(1)**** | 10.5(1)**** | 10.5(2) | 11.0.1 | 11.5.X | 12.0.1 |
| 10.0.1 | X | X | X | X | X | X | X | X | X |  |  |  |  |  |
| 10.5.1 | X | X | X | X | X | X | X | X | X | X |  |  |  |  |
| 10.5.1SR1 | X | X | X | X | X | X | X | X | X | X |  |  |  |  |
| 10.6.0 | X | X | X | X | X | X | X | X | X | X | X |  |  |  |
| 11.0.1 |  |  |  |  |  | X | X | X | X | X | X | X |  |  |
| 11.0.2 |  |  |  |  |  | X | X | X | X | X | X | X | X |  |
| 11.0.3 |  |  |  |  |  | X | X | X | X | X | X | X | X |  |
| 12.0.X |  |  |  |  |  |  |  |  | X | X | X | X | X | X |

| CUCM Version | Windows XP 32-bit | Windows Vista 32-bit | Windows 7 32-bit | Windows 7 64-bit | Windows 8 64-bit |
|---|---|---|---|---|---|
| 7.1(5)* | X | X |  |  |  |
| 8.0(1) | X | X | X |  |  |
| 8.0(3) | X | X | X |  |  |
| 8.5(1) ** | X | X | X | X |  |
| 8.6(1) | X | X | X | X |  |
| 8.6(2) | X | X | X | X |  |
| 9.0(1) | X | X | X | X |  |
| 9.1(1) | X | X | X | X |  |
| 9.1.(2) | X | X | X | X |  |
| 10.0(1) | X | X | X | X | X |

| CUCM Version | Windows Vista 32-bit and Wow64 | Windows 7 32-bit and Wow64 | Windows 8 32-bit and Wow64 | Windows 8.1 |
|---|---|---|---|---|
| 7.1(5)* | X |  |  |  |
| 8.0(1) | X |  |  |  |
| 8.0(3) | X |  |  |  |
| 8.5(1) ** | X | X |  |  |
| 8.6(1) | X | X |  |  |
| 8.6(2) | X | X |  |  |
| 9.0(1) | X | X |  |  |
| 9.1(1) | X | X |  |  |
| 9.1.(2) | X | X |  |  |
| 10.0(1) | X | X | X |  |
| 10.5(1) | X | X | X | X |

| CUCM Version | Windows Vista 32-bit and Wow64 | Windows 7 32-bit and Wow64 | Windows 8 32-bit and Wow64 | Windows 8.1 32-bit and Wow64 |
|---|---|---|---|---|
| 7.1(5)* | X |  |  |  |
| 8.0(1) | X |  |  |  |
| 8.0(3) | X |  |  |  |
| 8.5(1) ** | X | X |  |  |
| 8.6(1) | X | X |  |  |
| 8.6(2) | X | X |  |  |
| 9.0(1) | X | X |  |  |
| 9.1(1) | X | X |  |  |
| 9.1.(2) | X | X |  |  |
| 10.0(1) | X | X | X |  |
| 10.5(1) | X | X | X | X |

| CUCM Version | Windows Vista 32-bit and Wow64 | Windows 7 32-bit and Wow64 | Windows 8 32-bit and Wow64 | Windows 8.1 32-bit and Wow64 |
|---|---|---|---|---|
| 7.1(5)* | X |  |  |  |
| 8.0(1) | X |  |  |  |
| 8.0(3) | X |  |  |  |
| 8.5(1) ** | X | X |  |  |
| 8.6(1) | X | X |  |  |
| 8.6(2) | X | X |  |  |
| 9.0(1) | X | X |  |  |
| 9.1(1) | X | X |  |  |
| 9.1.(2) | X | X |  |  |
| 10.0(1) | X | X | X |  |
| 10.5(x) | X | X | X | X |

| CUCM Version | Windows Vista 32-bit and Wow64 | Windows 7 32-bit and Wow64 | Windows 8 32-bit and Wow64 | Windows 8.1 32-bit and Wow64 |
|---|---|---|---|---|
| 9.0(1) | X | X |  |  |
| 9.1(1) | X | X |  |  |
| 9.1.(2) | X | X |  |  |
| 10.0(1) | X | X | X |  |
| 10.5.1 | X | X | X | X |
| 10.5.2 | X | X | X | X |
| 11.0.1 | X | X | X | X |

| CUCM Version | Windows Vista 32-bit and Wow64 | Windows 7 32-bit and Wow64 | Windows 8 32-bit and Wow64 | Windows 8.1 32-bit and Wow64 |
|---|---|---|---|---|
| 9.0(1) | X | X |  |  |
| 9.1(1) | X | X |  |  |
| 9.1.(2) | X | X |  |  |
| 10.0(1) | X | X | X |  |
| 10.5.1 | X | X | X | X |
| 10.5.2 | X | X | X | X |
| 11.0.1 | X | X | X | X |
| 11.5.1* | X | X | X | X |

| CUCM Version | Windows Vista 32-bit and Wow64 | Windows 7 32-bit and Wow64 | Windows 8 32-bit and Wow64 | Windows 8.1 32-bit and Wow64 | Windows 10 32-bit and Wow64 |
|---|---|---|---|---|---|
| 9.0(1) | X | X |  |  |  |
| 9.1(1) | X | X |  |  |  |
| 9.1.(2) | X | X |  |  |  |
| 10.0(1) | X | X | X |  |  |
| 10.5.1 | X | X | X | X |  |
| 10.5.2 | X | X | X | X | X* |
| 11.0.1 | X | X | X | X | X |
| 11.5.1* | X | X | X | X | X |

| CUCM Version | Windows 7 SP-1 | Windows 8.1 Update 1 | Windows 10 (desktop Mode) |
|---|---|---|---|
| 10.0(1) | X |  |  |
| 10.5.1 | X | X |  |
| 10.5.2 | X | X | X* |
| 11.0.1 | X | X | X** |
| 11.5.1 | X | X | X |
| 12.0.1 | X | X | X |