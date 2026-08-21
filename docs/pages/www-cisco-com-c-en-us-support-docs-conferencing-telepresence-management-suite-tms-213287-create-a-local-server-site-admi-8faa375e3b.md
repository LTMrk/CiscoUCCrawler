---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-telepresence-management-suite-tms-213287-create-a-local-server-site-admi-8faa375e3b
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-suite-tms/213287-create-a-local-server-site-administrator.html
retrieved_at: 2026-08-21T06:29:17.662134+00:00
---

Configure a Local Server Site Administrator Account for TMSPE Installation

# Configure a Local Server Site Administrator Account for TMSPE Installation

Updated: July 2, 2018

Document ID: 213287

Contents

## Contents

## Introduction

This document describes how to create and configure a local server site administrator account on Cisco Telepresence management Suit (TMS) , that it is required prior TMS Provisoning Extension (TMSPE) installation.  That account is used in the TMSPE installator to have access to TMS.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- TMS

- Windows Server

- TMSPE

### Components Used

The information in this document is based on Windows 2012, but it applies for other Windows Server versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

The account is created as a local admin account in the server where the TMS is installed, then it is added to the TMS users as Site Admininstrator.

Note : Use a Admin account to log in to the server where TMS is installed.

## Configure

Step 1. Connect to your server. You can use any domain or local account with Administrator permissions.

Step 2. Navigate to Run and type MMC.exe

Step 3. In the Console window, click File > Add/Remove Snap-in , as shown in the image.

Step 4. Select Computer Management module and click Add , as shown in the image.

Step 5. Select Local computer and click Finish , as shown in the image.

Step 6. Click OK.

Step 7. Expand the Computer Management > System Tools tree as shown in the image.

Step 8. Expand Local users and Group s and select Users .

Step 9. Right click in the User area and select New User .

Step 10. Fill the fields in the New User window, then click Create . Select User cannot change password and Password never expires .

Step 11. Return  to Local Users and Groups , right-click on  the new account created and select Properties .

>

Step 12.Ensure that the Users membership is associated to the account created.

## Verify

Once the local account has been created, you can proceed to create a new account in TMS to be used as Site Administrator.

Step 1. Navigate to the TMS web UI page and log in with a site administrator account.

Step 2. Navigate to Administrative Tools > User Administration > Users .

Step 3. Click in New .

Step 4. Type the account name created in the Configure section and select Site Administrator membership. C lick Save .

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Pablo Acosta

Cisco TAC Engineer

### This Document Applies to These Products

- TelePresence Management Suite (TMS)