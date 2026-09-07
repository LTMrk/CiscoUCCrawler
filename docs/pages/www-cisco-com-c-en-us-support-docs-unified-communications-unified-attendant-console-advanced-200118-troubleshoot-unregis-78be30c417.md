---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-advanced-200118-troubleshoot-unregis-78be30c417
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-advanced/200118-Troubleshoot-unregistered-CTI-ports-afte.html
retrieved_at: 2026-09-07T15:49:32.602832+00:00
---

Troubleshoot unregistered CTI ports after upgrade to CUAC 10.5 or Re-install of TSP

# Troubleshoot unregistered CTI ports after upgrade to CUAC 10.5 or Re-install of TSP

### Download Options

Updated: September 8, 2015

Document ID: 200118

Contents

## Contents

## Introduction

This document describes troubleshooting steps in scenarios when Computer Telephony Integration (CTI) ports go into unknown or none state after an upgrade to Cisco Unified Attendant Console(CUAC) 10.5.2 version or re-installation of Telephony Service Provider(TSP).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUAC Advanced

- Cisco Unified Communications Manager

- CUAC TSP configuration

### Components Used

The information in this document is based on these software and hardware versions:

- CUAC Advanced 10.5.2

- Cisco Unified Communications Manager 10.5.2.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem

Post upgrade of CUAC to 10.5.2 from earlier versions of software the CTI ports move into unknown/none state

Note : These steps must be performed in the order to troubleshoot the problem. Incase, the problem is solved with any step, then further steps are not required.

## Solution 1. Verify CUAC configuration and check whether TSP installed is compatible with CUAC version in use

- Navigate to CUAC Administration page > Engineering > CUCM Connectivity.

2. Verify the CUCM Information and Application User Credentials are correct. Click on Test connection and verify connectivity.

3. Click on Start > Cisco TSPx64 configuration > Configure.

4. Verify Version Information in General tab as shown in this image.

5. Uninstall the TSP from Control Panel if it does not match the CUCM version.

6. Install the correct version of TSP.  Navigate to CUCM Pub >Cisco Unified CM Administration page>Application > Plugin Click on Find. Download and move the setup of 32 bit or 64 bit client based on your CUAC server Windows OS Bit size.

7. Double click and install TSP.

8. Enter the correct Values during installation of TSP. Verify that application user credentials entered match the application user credentials created on CUCM.

9. Restart the CUAC server once the TSP installation is complete.

10. Check whether CTI ports are registered once the server is back online.

## Solution 2. Delete the CTI ports on CUCM and sync CUAC with CUCM

1. Navigate to CUCM Administration page > Device > Phones. Delete all the CTI ports synced previously for CUAC.

2. Navigate to CUAC Administration page > System Configuration > Synchronize with CUCM. Click Synchronize with CUCM tab.

3. Verify Sync by clicking on CUCM Sync Report.

4.Verify whether the Sync is completed.

5. Verify status of CTI ports on CUCM once Sync is completed.

## Solution 3. Create a new Application user

- Navigate to CUCM Administration page > User management.

- Select the Application user used in CUAC, Click the Copy option which will create a new Application user with old details carried to the New user.

- Re-name it and change the password of this user (make sure that you use a different username and password than the original Application user).

- Click Save.

- Roles and Permissions will be carried to this new Application user once you copy it in CUCM.

- Delete the Old Application user.

- Navigate to CUAC Administration page > Engineering > CUCM Connectivity and change username and password to New Application User Created in the above Steps .

- Navigate to CUAC server > TSP configuration > User Tab > and change the username and password accordingly and Click OK.

9. Reboot the CUAC Server once to re-initialize the CT link.

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- Unified Attendant Consoles