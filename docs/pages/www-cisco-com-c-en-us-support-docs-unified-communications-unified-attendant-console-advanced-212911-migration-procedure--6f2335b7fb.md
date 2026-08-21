---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-advanced-212911-migration-procedure--6f2335b7fb
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-advanced/212911-migration-procedure-for-cuaca-10-5-x-to.html
retrieved_at: 2026-08-21T13:57:27.032786+00:00
---

Migration Procedure For CUACA (10.5.X to 11.X.X)

# Migration Procedure For CUACA (10.5.X to 11.X.X)

### Download Options

Updated: March 19, 2018

Document ID: 212911

Contents

## Contents

## Introduction

This document describes the procedure to migrate Cisco Unified Attendant Console (CUAC) Advance version 10.5.2 with SQL Express 2008 from Microsoft Server 2008 to CUAC Advance version 11.0.2 with SQL Express 2008 on Microsoft Server 2012.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Attendant Console Advanced

- Microsoft SQL Server 2008 Express

### Components Used

The information in this document is based on these software and hardware versions:

- CUAC Advanced 10.5.2

- CUAC Advanced 11.0.2

- Cisco Unified Communications Manager 10.5.2.

- Microsoft SQL Server 2008 Express

- Microsoft Windows Server 2008 R2 Enterprise

- Microsoft Windows Server 2012 R2 Standard

The information in this document is based on devices in specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any Configuration change.

## Configure

This table shows the specifications of both from and to systems.

From

To

Version

CUACA 10.5.2

CUACA 11.0.2

Server OS

Server 2008 R2 Enterprise – SP1 64-bit

Server 2012 R2 Standard – 64-bit

Database

SQL 2008 Express Server SP3

SQL 2008 Express Server SP3

Step 1. Ensure that the server to which you wish to migrate meets Cisco Unified Attendant Console Advance hardware and software requirements.

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cucmac/cuaca/11_0_2/install_admin_guide/CUACA110201WAG.pdf

Step 2. Based on supported SQL Express Databases, install respective SQL Express Database. In the Lab Environment, SQL 2008 Express Server SP3 is installed.

Step 3. Refer to CUAC Advanced Administration and Installation Guide for installation of SQL Server 2008.

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cucmac/cuaca/11_0_2/install_admin_guide/CUACA110201WAG.pdf

Note : During the selection of the default instance while installation, the selection of the named instance, names the SQL instance as <Computer name\SQLEXPRESS> . This in turn is an issue while you install Attendant Console Server as it by default assumes SQL Db instance to be <Computername> only this cannot be changed either.

Step 4. After you install the required SQL Express Server, ensure that you can login to it using Microsoft SQL Server Management Studio. In order to enable SA User  navigate to Microsoft SQL Server Management Studio > Object Explorer > Expand Security > Expand Logins . Now right click sa then select properties and enter Password. Click on Status page Select Enabled under Login, as shown in the image:

Step 5. Restore ATTCFG and ATTLOG from the old CUAC system.

Note : This step is based on SQL database migration procedures in place; however, involvement of a SQL Admin is advised.

Step 6. After the SQL installation is complete with ATTCFG and ATTLOG restored, proceed with installation of CUAC 11.0.2

Follow Cisco Unified Attendant Console Advanced Administration and Installation Guide for CUAC installation.

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cucmac/cuaca/11_0_2/install_admin_guide/CUACA110201WAG.pdf

During installation (Database Wizard), an option on whether you want to overwrite the existing database is asked. This option is because installation setup recognizes the existence of SQL 2008 Express with ATTCFG and ATTLOG. Hence, it needs input from Admin on whether this Db be overwritten.

Click on NO as shown in the image and let the installation proceed further.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Manjunath Sheregar

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

|  | From | To |
|---|---|---|
| Version | CUACA 10.5.2 | CUACA 11.0.2 |
| Server OS | Server 2008 R2 Enterprise – SP1 64-bit | Server 2012 R2 Standard – 64-bit |
| Database | SQL 2008 Express Server SP3 | SQL 2008 Express Server SP3 |