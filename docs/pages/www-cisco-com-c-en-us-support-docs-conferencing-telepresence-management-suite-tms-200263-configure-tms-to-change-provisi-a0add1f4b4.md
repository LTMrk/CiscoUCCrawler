---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-telepresence-management-suite-tms-200263-configure-tms-to-change-provisi-a0add1f4b4
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-suite-tms/200263-Configure-TMS-to-change-Provisioning-of.html
retrieved_at: 2026-08-21T06:28:06.692758+00:00
---

Configure TMS to change Provisioning of an endpoint from TMS to CUCM

# Configure TMS to change Provisioning of an endpoint from TMS to CUCM

### Download Options

Updated: November 28, 2015

Document ID: 200263

Contents

## Contents

## Introduction

This document describes configuration changes and requirements when migrating Telepresence Codec (TC) endpoints from Video communication Server (VCS) to Cisco Unified Communications Manager (CUCM) and specific requirements of changing the provisioning on the endpoint from Telepresence Management Suite (TMS) to CUCM. Post the migration software Upgrade, Directory and registration is expected to work through the CUCM.

The document also discusses some of the known limitations when provisioning is changed from TMS to CUCM.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- The endpoint is provisioned with TMS and the following services with TMS work fine

- Phonebook Service

- Backup and Restore performed by TMS

- Software Upgrade from TMS

- Persistent Template

### Components Used

The information in this document is based on Cisco Telepresence Endpoint runing TC 7.3.x, TMS 14.6.x and CUCM 10.x

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any configuration.

## Configure

Changing provisioning from TMS to CUCM requires the following configuration changes on the TMS and CUCM.

Step 1. Configure Device for the endpoint on CUCM

Refer to the document in order to configure the Device on the CUCM

Endpoint administration with CUCM

Step 2. Phonebook or Directory need to be configure on CUCM

The CUCM has support for both User Data Service(UDS) and TMS for directory integration.

To ensure that TMS is used for directory integration these must be done :

- Alternate Phonebook server type field must be selected as TMS under the Product Specific Configuration Layout of the Device

- Configure Alternate phone book server address to have correct URL of the TMS for example https://IP_ADDR_OF_TMS/tms/public/external/phonebook/phonebookservice.asmx

Navigate to Device > Phone. Find the phone and click it, as shown in the image.

Step 3. Change Provisioning on Endpoint from TMS to CUCM

Endpoint Provisioning needs to be changed  from TMS to CUCM . The endpoint will then get all further information from CUCM regarding registration, phonebook and other configuartion requirements as per phone profile configured on the endpoint.

Provisioning on the endpoint can be changed using these procedures:

- Using Web interface

- Navigate to Configuration > System Configuration > Provisioning on the endpoint.

- Navigate to ExternalManager section and enter the Address, which can be an IP address, DNS name or the path of the External Manager which is the CUCM cluster TFTP server address . Click Save .

- Navigate to Mode and set the provisioning mode to CUCM. Click Save.

- Using the Endpoint CLI

```
xConfiguration Provisioning Mode: [must be CUCM]
xConfiguration Provisioning ExternalManager Address: [the CUCM cluster TFTP server address]
xConfiguration Provisioning ExternalManager Protocol: [must be HTTP for UCM mode]
xConfiguration Provisioning HttpMethod: [both GET and POST work in UCM mode]
xCommand Provisioning CUCM CTL Delete
```

Step 4. Add or Re-Add Endpoint on the TMS

The endpoint can already exist in the TMS database if it was previously provisioned with the VCS , or it can be a new deployment in which case the endpoint is added to the TMS as a New endpoint.

Add the endpoint for the first time on TMS (Endpoint provisioned and registered to CUCM)

Ensure that device is registered to CUCM otherwise it cannot be added to the TMS. CUCM must also be added to the TMS.

- Verify that you can find the endpoint on the CUCM managed system

Navigate to Systems > Navigator and locate the CUCM on the TMS.

All the endpoints not added to the TMS show as System not in TMS.

- Add the Endpoint provisioned with the CUCM.

On System Navigator of TMS click Add system , look for Add from Unified CM or TMS.

Note : The username/password configured under the Admin username and password on the phone configuration on the CUCM needs to be the same as the admin username/password on the endpoint .The same username / password needs to be used on the TMS else the TMS will report a wrong username and password error.

Re-add the endpoint on TMS to be provisioned to the CUCM

To re-add an endpoint on the TMS to be provisioned to the CUCM , follow the steps above to Add from Unified CM or TMS.

Step 5. Assign Phonebook to the endpoint added in the previous step

You need to assign phonebook to the endpoint on the TMS.

Navigate to the endpoint on the TMS and then go to the Phonebook tab.

After saving the phonebook on TMS , the phonebook appears on the endpoint.

## Verify

Check Provisioning Status On the Endpoint

- Using the Web interface

. 1. Access Endpoint using Web interface.

. 2. Navigate to Configuration > System Status the status should show as Provisioned as shown in this image.

- Using the Endpoint CLI

1. SSH/Telnet to endpoint.

2. Log in as admin user.

3. Execute xstatus // provisiong.

Check Phonebook Status

- Using the Endpoint CLI

1. SSH/Telnet to endpoint

2. Login as admin user

3. Execute xstatus // phonebook

This must show the URL of the TMS.

Check the Endpoint Satus on the TMS

The status of the endpoint should show Connectivity: Reachable on LAN on the TMS

Endpoint should be registered on the CUCM

## Troubleshoot

- On TMS Endpoint status shows Wrong provisioning mode

This problem is related to how endpoint has been aded to TMS. When Endpoint is provisioned with CUCM endpoint shouldn't be added in TMS using ip address directly instead should be added through the Add from Unified CM or TMS on TMS .

Step 4 of configuration steps above must be used to add endpoints provisioned with CUCM.

- On TMS message related to "Auto answer is switched off" is shown

When endpoint is added to the CUCM , you have to ensure that auto answer is configured as per the requirement.

Steps to be followed to make changes related to auto answer:

1. Locate the endpoint on CUCM under Device > Phone.

2. Locate Auto Answer , by default it is Auto Answer Off on the DN settings, configure this as per the requirement.

- On TMS  error Wrong username or password is shown.

This issue happens when you have a different username and password configured on the endpoint configuration on the CUCM and endpoint itself

- To Verify Configuration on Endpoint for the user:

1. Navigate to web interface of the endpoint

2. Navigate to Configuration > User Administration

3. Create or change credential of the user

- To Verify Correct credential for the Endpoint on CUCM phone configuration:

1. Go to Device > Phone on the CUCM and select the phone you are trying to provision.

2. Locate Admin username and password.

. Enter correct information, then save and apply configuration.

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- TelePresence Management Suite (TMS)

- TelePresence SX Series

- Unified Communications Manager (CallManager)