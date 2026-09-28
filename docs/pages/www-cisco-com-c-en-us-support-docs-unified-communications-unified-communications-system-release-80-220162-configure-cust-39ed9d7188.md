---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-system-release-80-220162-configure-cust-39ed9d7188
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-system-release-80/220162-configure-customer-voice-portal-cvp-re.html
retrieved_at: 2026-09-01T20:43:02.562391+00:00
---

Configure Customer Voice Portal (CVP) Reporting Server Database User Password

# Configure Customer Voice Portal (CVP) Reporting Server Database User Password

### Download Options

Updated: January 27, 2023

Document ID: 220162

Contents

## Contents

## Introduction

This document describes the procedure to change the Customer Voice Portal (CVP) Reporting Server Database User password in UCCE or PCCE deployment.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

Cisco Unified Contact Center Enterprise (UCCE)

Cisco Packaged Contact Center Enterprise (PCCE)

Cisco Unified Customer Voice Portal (CVP)

Cisco Unified Customer Voice Portal Reporting Server

Cisco Unified Customer Voice Portal Operations Console (OAMP)

### Components Used

The information in this document is based on these software and hardware versions:

Cisco Unified Customer Voice Portal (CVP) Reporting Server 12.6

CVP Operations Console (OAMP) 12.6

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Overview

CVP Reporting Server  is comprised of the reporting service and the reporting database. The reporting service receives reporting data from the Interactive Voice Response (IVR) service, the Session Initiation Protocol (SIP) service (if used), and the VoiceXML (VXML) server and transforms and writes this data to the Informix reporting database to provide historical reporting in a call center environment. CVP operations console helps to operate, administer, maintain, and provision the Reporting Server.

## Configure

### UCCE

You must perform these procedures to change the reporting database administrator (cvp_dbadmin) password in UCCE deployment.

Step 1 Log in to the CVP Reporting Server  and click of Start to start the Services snap-in , in the Start Search box, enter services.msc , and then press Enter .

Step 2 Stop the Cisco CVP CallServer , Cisco CVP SNMP Management, and Informix  IDS cvp services. Do not stop the Cisco CVP WebServicesManager .

Step 3 Click the Start menu, open the Windows Administrative Tools , and click Computer Management .

Step 4 Navigate to Local Users and Group > Users .

Step 5 Right-click cvp_dbadmin user , select Set Password , and click Proceed in the warning window.

Step 6 In the New Password field, enter the new password to a temporary password.

Step 7 In the Confirm Password field, retype the new password and click OK .

Note : Password must meet Reporting Server and local machine password requirements.

Step 8 Log in to  the CVP Operations Console server https:// ServerIP :9443/oamp where ServerIP is hostname or IP address of the server.

Step 9 Select Device Management > Unified CVP Reporting Server .

The Find, Add, Delete, Edit window opens.

Step 10 Click the link in the Hostname field or the radio button that precedes it to select a Reporting Server, and then click Edit .

The Edit Reporting Server Configuration window opens with the current settings displayed.

Step 11 Select the Database Administration menu in the toolbar, then select Change User Passwords .

The Reporting Server: Change User Passwords page opens, displays the IP address and hostname for the currently selected Reporting Server.

Step 12 In the User field, use the drop-down menu to select User Database Administrator .

Step 13 In the Old Password field, enter the password created for that user in Step 6.

Step 14 In the New Password field, enter the new password.

Note : Password must meet Reporting Server and local machine password requirements.

Step 15 In the Reconfirm Password field, retype the new password.

Step 16 Click Save & Deploy to save the changes to the Operations Console database and deploy them to the Reporting Server.

Note : In the backend, it executes the cvp4dbBackend.bat file, located in C:\Cisco\CVP\bin which internally executes changeuserpassword.exe from the C:\Cisco\CVP\bin folder. This c hangeuserpassword.exe updates the Windows local user password for the user provided in the OAMP page. Once this is updated at the Windows level, the CVP code invokes the encrypt functions that encrypt the password for the user and stores it in the reporting.properties file ( RPT.DBPassword or RPT.DBAdminPassword depends on the user name selected).

Step 17 Restart the CVP Reporting Server.

### PCCE

You must perform these procedures to change the reporting database administrator (cvp_dbadmin) and database user (cvp_dbuser) password in PCCE deployment.

Step 1 Log in to the CVP Reporting Server  and click Start to start the Services snap-in in the Start Search box, type services.msc , and then press Enter .

Step 2 Stop the Cisco CVP CallServer , Cisco CVP SNMP Management, and Informix IDS CVP services. Do not stop the Cisco CVP WebServicesManager .

Step 3 Click the Start menu, open the Windows Administrative Tools and click Computer Management .

Step 4 Navigate to Local Users and Group > Users .

Step 5 Right-click cvp_dbadmin user , select Set Password , and click Proceed in the warning window.

Step 6 In the New Password field, enter the new password to a temporary password.

Step 7 In the Confirm Password field, retype the new password and click OK .

Note : Password must meet Reporting Server and local machine password requirements.

Step 8 Repeat Steps 4 to 7 to change the cvp_dbuser password.

Note : Make sure cvp_dbadmin and cvp_dbuser passwords are the same.

Step 9 Open the Windows command prompt and navigate to the C:\Cisco\CVP\bin directory.

Step 10 Run the command report-init.bat -reporthashpw YourPassword (YourPassword is the password set in the Step 6).

Note : The report-init.bat encrypts the cvp_dbuser and cvp_dbadmin password and stores it in the reporting.properties file located at the C:\Cisco\CVP\conf folder on the CVP Reporting Server. Both the RPT.DBPassword and RPT.DBAdminPassword get updated in this process.

Step 11 Ignore the log4J error that pops up when  you run the command.

Step 12 Restart the CVP Reporting Server.

## Verify

### UCCE

Step 1 Access the CVP Informix Database through the cvp_dbadmin account to verify the database administrator log in works.

Step 2 Make a test call and verify that data gets populated.

### PCCE

Step 1 Verify if the reporting.properties file is updated.

Step 2 Access the CVP Informix Database through the cvp_dbadmin and cvp_dbuser account and verify the database administrator and user log in works.

Step 3 Make a test call and verify that data gets populated.

## Troubleshoot

Issue 1: CVP Reporting Server is in Workgroup and database password change from CVP Operations console fails with error message : password does not meet system security requirement .

Solution::Confirm if the password meets the CVP Reporting Server and local machine password requirements.Secondly, check the value set for the security policy Minimum Password Age under Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy in the local machine. If the security policy has a value greater than 0 and the password change is for the second time in the day, then you can see the error: password does not meet system security requirement . To fix the error, change the Minimum Password Age value to 0 . If this policy cannot be changed, wait for the window to expire before the next try.

Note : The CVP Reporting Server password requires that the Minimum Password Age parameter be set to 0 days for both local and / or the domain security policy and is subject to both the CVP password policy and the password policy enforced by the operating system on which the Reporting Server resides.

Issue 2: CVP Reporting Server is in domain and database password change from CVP Operation console fails with error message: password does not meet system security requirement .

Solution: Confirm the password meets the CVP Reporting Server and local machine password requirements. If the password meets the guidelines, then check the value set for the security policy Minimum Password Age in the local machine. If the security policy has a value greater than 0 and the password change is for the second time in the day, then you can see the error: password does not meet system security requirement . To fix the error, change the Minimum Password Age value to 0. If this policy cannot be changed, wait for the window to expire before the next try. Still, if you see the same error, then it is the domain security policy that blocks it. To solve this, you can move the CVP Reporting Server out of the domain and change the password.

## Related Information

- Install Unified CVP Reporting Server

### Revision History

1.0

30-Jan-2023

Initial Release

### Contributed by Cisco Engineers

Binu Santhakumaran

TAC Engineer

### This Document Applies to These Products

- Unified Customer Voice Portal 12.6(1)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 30-Jan-2023 | Initial Release |