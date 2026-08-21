---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200571-customised-o-54bc4bfa52
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200571-Customised-Organizational-Unit-for-LDAP.html
retrieved_at: 2026-08-21T13:55:00.852395+00:00
---

Customized Organizational Unit for LDAP Integration Between Call Manager and Active Directory

# Customized Organizational Unit for LDAP Integration Between Call Manager and Active Directory

### Download Options

Updated: July 20, 2020

Document ID: 200571

Contents

## Contents

## Introduction

This document describes the procedure to create a new customized Organizational Unit ( OU) for special users when you have a primary OU.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Active Directory (AD) server.

### Components Used

The information in this document is based on Cisco Unified Call Manager (CUCM) Release 10.5.2.13900-12.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Configuration on AD server

Step 1. Create a new OU.

Right-click the primary OU and choose New > Organizational Unit .

Step 2. Check the newly created OU. (In this example, the newly created OU is "CIsco_TAC.")

Step 3. Add users in the new OU.

Right-click the new OU and choose New > User .

Step 4. Create a user who will bridge the gap between the AD server and CUCM.

Right-click Users and choose New > User .

The new user is created. This user must be a member of domain admin.

Step 5. Right-click User > Properties.

On the Properties dialog, select the Member Of tab.

On the Member Of tab, click Add .

Step 6. For the "object names to select," enter "domain admin" and click Check Names.

Step 7. Select Domain Admins and click Set Primary Group; then remove Domain Users .

Step 8. Right-click the new OU (Cisco_TAC in this example) and choose Properties.

Step 9. On the Properties dialog, select the Managed By tab and click Change.

Step 10. Enter the object name to select (the user name created to bridge the AD server and CUCM in step 4) and then click Check Names.

### Configuration on CUCM

Step 11. Go to System > LDAP > LDAP System .

Step 12. Select the checkbox labeled Enable Synchronizing from LDAP Server .

Step 13. Go to System > LDAP > LDAP Directory .

Step 14. Click Add new .

Note : LDAP Configuration Name : This value is any name of an LDAP Configuration. LDAP Manager Distinguished Name : This value should be the user name of the AD and CUCM bridge user. LDAP Password : This value is the password of the bridge user created in step 4. LDAP User Search Base : To find this value, follow this procedure on the AD server: A) Right-click on the OU and select Properties .

B) On the Properties dialog, select the Attribute Editor tab and find the "distinguishedName" value.

Step 15. Here, keep the LDAP Server IP address and Port .

Step 16. Click Save .

Step 17. Click Perform Full Sync Now .

## Verify

In order to verify the user on CUCM, navigate to User Management > End User .

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Sachin Kalekar

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)