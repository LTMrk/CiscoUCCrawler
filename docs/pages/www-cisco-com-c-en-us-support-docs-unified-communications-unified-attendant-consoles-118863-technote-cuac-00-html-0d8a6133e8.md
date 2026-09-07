---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-consoles-118863-technote-cuac-00-html-0d8a6133e8
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-consoles/118863-technote-cuac-00.html
retrieved_at: 2026-09-07T15:49:16.034589+00:00
---

CUAC Compatibility Matrix with Microsoft Server and SQL

# CUAC Compatibility Matrix with Microsoft Server and SQL

Updated: May 17, 2018

Document ID: 118863

Contents

## Contents

## Introduction

This document describes the compatibility between different Cisco Unified Attendant Console (CUAC) versions (Business, Department, Enterprise, Premium, and Advanced) with Microsoft Servers and the Structured Query Language (SQL) Server. It does not provide information in regards to installation. Refer to the Release Notes and Install Guide in order to know about all the requirements before server installation.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager ( CUCM)

- CUAC

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## CUAC - Microsoft Server Compatibility

Here are the compatibility matrices between the different CUAC versions and Microsoft Servers.

### Naming Conventions

- CUCM - Cisco Unified Communications Manager

- CUBAC - Cisco Unified Business Attendant Console

- CUDAC - Cisco Unified Department Attendant Console

- CUEAC - Cisco Unified Enterprise Attendant Console

- CUPAC - Cisco Unified Premium Attendant Console

- CUACA - Cisco Unified Attendant Console Advanced Edition

- 2003 SP2 - Microsoft Windows Server 2003 SP2

- 2008 R1 (32-bit) - Microsoft Windows Server 2008 R1 (32-bit)

- 2008 R2 (64-bit) - Microsoft Windows Server 2008 R2 (64-bit)

- 2012 R1 (64-bit) - Microsoft Windows Server 2012 R1 (64-bit)

- 2012 R2 (64-bit) - Microsoft Windows Server 2012 R2 (64-bit)

- 2014

### How to Use the Matrix

Look for the CUAC version that you run on on Y-axis in the table. Check for the supported Microsoft Server on the X-axis.

X - Supported only on Physical Servers XX - Supported on both the Physical Server and in a virtual environment (VMware)

### Compatibility between CUAC (Business/Department/Enterprise/Premium) and Microsoft Server

2003 SP2

2008 R1 (32-bit)

2008 R2 (64-bit)

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

XX

X

XX

X

XX

X

XX

X

XX

XX

XX

XX

XX

Notes : - 64-bit installations are supported only in conjunction with CUCM versions 8.5(1) or later. - Windows 2012 is only supported for CUCM 10.0 (1) or later. - Windows 2012 R2 is only supported for CUCM 10.5 (1) or later.

### Compatibility between CUACA and Microsoft Server

2008 R1 (32-bit)

2008 R2 (64-bit)

2012 R1 (64-bit)

2012 R2 (64-bit)

2016 (64-bit)

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

XX

Notes : - 64-bit installations are supported only in conjunction with CUCM versions 8.5 (1) or later. - Windows 2012 is only supported for CUCM 10.0 (1) or later. - Windows 2012 R2 is only supported for CUCM 10.5 (1) or later. - Microsoft Windows 10 for CUACA client is supported on CUAC 11.0.1 and onwards.

## CUAC - SQL Server Compatibility

Here are the compatibility matrices between the different CUAC versions and SQL Servers.

### Naming Conventions

- CUBAC - Cisco Unified Business Attendant Console

- CUDAC - Cisco Unified Department Attendant Console

- CUEAC - Cisco Unified Enterprise Attendant Console

- CUPAC - Cisco Unified Premium Attendant Console

- CUACA - Cisco Unified  Attendant Console Advanced Edition

- 20YY Exp - SQL  Express 20YY

- 20YY Std - SQL Standard 20YY

- 20YY Ent - SQL Enterprise 20YY

where YY could be either 05, 08, 12, or 14.

### How to Use the Matrix

Look for the CUAC version on the Y-axis in the table. Check for the supported SQL version on the X-axis. In the table X means Supported.

### Compatibility between CUAC (Business/Department/Enterprise/Premium) and Microsoft SQL

2005 Exp, Std, Ent

2008 Exp, Std, Ent (32-bit)

2008 Exp, Std, Ent (64-bit)

2008 R2 Exp, Std, Ent (32-bit)

2008 R2 Exp, Std, Ent (64-bit)

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

Only SQL Express is supported.

Notes : - 64-bit SQL installations are not supported on a 32-bit server. - SQL Express is not supported with resilient deployment. - SQL should not be installed on a Domain Controller.

### Compatibility between CUACA and Microsoft Server

2008 Exp, Std, Ent (32-bit)

2008 Exp, Std, Ent (64-bit)

2008 R2 Exp, Std, Ent (32-bit)

2008 R2 Exp, Std, Ent (64-bit)

2008 SP3 Exp, Std, Ent (32/64-bit)

2012 Exp, Std, Ent (32/64-bit)

2014 Exp, Std, Ent (32/64-bit)

2016 Exp,Std,Ent (32/64-bit)

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

Notes : - 64-bit SQL installations are not supported on a 32-bit server. - SQL Express is not supported with resilient deployment. - SQL should not be installed on a Domain Controller. - Microsoft Windows 10 for CUACA client is supported on CUAC 11.0.1 and onwards.

### Contributed by Cisco Engineers

Alok Singh

Cisco TAC Engineer

Manjunath Sheregar

Cisco TAC Engineer

|  |  |  | MS >>>>>> |  |  |
|---|---|---|---|---|---|
| CUBAC/CUDAC | CUEAC | CUPAC | 2003 SP2 | 2008 R1 (32-bit) | 2008 R2 (64-bit) |
| 2.0.0.11 | 3.0.0.2 |  | X |  |  |
| 2.0.1.14 | 3.0.1.4 |  | X |  |  |
| 3.1.1.5 | 3.1.1.5 |  | X | X |  |
| 3.1.1.8 | 3.1.1.8 |  | X | X |  |
| 3.1.1.10 | 3.1.1.10 |  | X | X |  |
| 8.0.0.5 | 8.0.0.5 |  | X | X |  |
| 8.0.3.9 | 8.0.3.9 |  | X | X |  |
| 8.5.1.5 | 8.5.1.5 |  | X | X |  |
| 8.6.1.9 | 8.6.1.9 |  | X | XX |  |
| 8.6.2.11 | 8.6.2.11 |  | X | XX |  |
| 8.6.2.20 | 8.6.2.20 |  | X | XX |  |
| 9.0.1.10 | 9.0.1.10 | 9.0.1.10 | X | XX |  |
| 9.0.1.20 | 9.0.1.20 | 9.0.1.20 | X | XX |  |
| 9.1.1.10 | 9.1.1.10 | 9.1.1.10 |  | XX | XX |
| 9.1.1.20 | 9.1.1.20 | 9.1.1.20 |  | XX | XX |

|  | MS >>>>>> |  |  |  |  |
|---|---|---|---|---|---|
| CUACA | 2008 R1 (32-bit) | 2008 R2 (64-bit) | 2012 R1 (64-bit) | 2012 R2 (64-bit) | 2016 (64-bit) |
| 10.0.1.10 | XX | XX | XX |  |  |
| 10.5.1 | XX | XX | XX | XX |  |
| 10.5.2 | XX | XX | XX | XX |  |
| 11.0.1 | XX | XX | XX | XX |  |
| 11.0.2 | XX | XX | XX | XX |  |
| 12.0.2 |  |  |  | XX | XX |

|  |  |  | SQL >> |  |  |  |  |
|---|---|---|---|---|---|---|---|
| CUBAC / CUDAC | CUEAC | CUPAC | 2005 Exp, Std, Ent | 2008 Exp, Std, Ent (32-bit) | 2008 Exp, Std, Ent (64-bit) | 2008 R2 Exp, Std, Ent (32-bit) | 2008 R2 Exp, Std, Ent (64-bit) |
| 2.0.0.11* | 3.0.0.2* |  | X |  |  |  |  |
| 2.0.1.14* | 3.0.1.4* |  | X |  |  |  |  |
| 3.1.1.5* | 3.1.1.5* |  |  | X |  |  |  |
| 3.1.1.8* | 3.1.1.8* |  |  | X |  |  |  |
| 3.1.1.10* | 3.1.1.10* |  |  | X |  |  |  |
| 8.0.0.5* | 8.0.0.5* |  |  | X |  |  |  |
| 8.0.3.9* | 8.0.3.9* |  |  | X |  |  |  |
| 8.5.1.5 | 8.5.1.5 |  | X | X |  |  |  |
| 8.6.1.9 | 8.6.1.9 |  | X | X |  |  |  |
| 8.6.2.11 | 8.6.2.11 |  | X | X |  |  |  |
| 8.6.2.20 | 8.6.2.20 |  | X | X |  |  |  |
| 9.0.1.10 | 9.0.1.10 | 9.0.1.10 | X | X |  |  |  |
| 9.0.1.20 | 9.0.1.20 | 9.0.1.20 | X | X |  |  |  |
| 9.1.1.10 | 9.1.1.10 | 9.1.1.10 |  | X | X | X | X |
| 9.1.1.20 | 9.1.1.20 | 9.1.1.20 |  | X | X | X | X |

|  | SQL >>> |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| CUACA | 2008 Exp, Std, Ent (32-bit) | 2008 Exp, Std, Ent (64-bit) | 2008 R2 Exp, Std, Ent (32-bit) | 2008 R2 Exp, Std, Ent (64-bit) | 2008 SP3 Exp, Std, Ent (32/64-bit) | 2012 Exp, Std, Ent (32/64-bit) | 2014 Exp, Std, Ent (32/64-bit) | 2016 Exp,Std,Ent (32/64-bit) |
| 10.0.1.10 | X | X | X | X |  | X |  |  |
| 10.5.1 | X | X | X | X | X | X | X |  |
| 10.5.2 | X | X | X | X | X | X | X |  |
| 11.0.1 | X | X | X | X | X | X | X |  |
| 11.0.2 | X | X | X | X | X | X | X |  |
| 12.0.2 |  |  |  |  |  | X | X | X |