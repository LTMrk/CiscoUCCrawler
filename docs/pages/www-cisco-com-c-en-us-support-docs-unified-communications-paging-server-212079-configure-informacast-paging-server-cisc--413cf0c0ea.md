---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-paging-server-212079-configure-informacast-paging-server-cisc--413cf0c0ea
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/paging-server/212079-Configure-InformaCast-Paging-Server-Cisc.html
retrieved_at: 2026-08-21T12:40:15.801210+00:00
---

Configure InformaCast Paging Server Cisco Unified Communications Manager (CUCM) 12.0

# Configure InformaCast Paging Server Cisco Unified Communications Manager (CUCM) 12.0

### Download Options

Updated: September 14, 2017

Document ID: 212079

Contents

## Contents

## Introduction

This document describes Cisco IP Paging and Emergency Notification functionality. CUCM integrates with InformaCast Paging Server in order to provide this functionality.

Contributed by Alejandra Gonzalez Romero, Cisco TAC Engineer, edited by Gurpreet Kukreja

## Prerequisites

### Requirements

CUCM 11.5.3SU3/ 12.0

InformaCast 12.0.1

For Panic Button,  phones must have speed dial assigned.

InformaCast Paging Server must be installed with the OVA.

### Components Used

The information in this document is based on the software and hardware versions listed in the Requirements section.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Since the InformaCast Paging Server runs on a separate application (virtual machine), manual configuration is needed on both applications: CUCM and InformaCast Paging. CUCM 12.0 automates the provisioning of Emergency Notification through a wizard in CUCM for initial configuration.

## Feature overview

### Navigate to CCMAdmin User Inteface (UI) > Advanced Features > Emergency Notifications Paging

### CCMAdmin UI provides a link in order to run the Emergency Notifications Paging Wizard.

The one time wizard automates the configuration in CUCM and in the InformaCast server.  Once the wizard completes, CUCM and InformaCast can be modified if any changes are need it.

The two main features that are configured with the Paging wizard are the Panic Button Alerting and Emergency Call Alerting .

Panic Button Alerting

A speed dial is created in the caller phone/s.  The speed dial sends the call toward the InformaCast server using a SIP trunk.  The originating phone hears an audio from the informacast server.   Then the InformaCast server sends a recorded audio (multicast) and text notification toward the destination phones.

Emergency Call Alerting

CallAware for InformaCast monitors the calls in Communications Manager.  When you call a number that CallAware has been configured to monitor (e.g. 911), the call recording software triggers a text/audio mass notification toward any supported InformaCast device (IP phones, analog/IP speakers, desktops, etc.).  The phones receives a pre-defined audio.  For example,  "Extension 1234 Dialed 911 at 10/11/17  2:34pm"     There is also an option in order to record the RTP stream but that is not enabled by the wizard in CUCM.

When the wizard in CUCM is run, select a Route Pattern.  The Route Pattern contains the number that CallAware does monitor.

## Configuration

Run the Emergency Notifications wizard and enter the requested information.

### Step 1. Before run the wizard, install InformaCast 12.0 with the OVA template

### Step 2. Enter the ip address of the InformaCast server, username (Admin) and the password.

The follow happens in the background:

CUCM

1. Activate the SNMP service (each node in the cluster)

2. Configure SNMP community-string   as version 3    - InformaCast

3. Activate CTI Manager Service (3 nodes or less)

4. Create New Region  -  ICVA

5. Create New Route Group - ICVA_RG

6. Create New Device Pool - ICVA

7. Create SIP trunk -  InformaCast

8. Create Route Group/Route List  ICVA_RG, ICVA_RL

9. Create role - AXL

10. Create application user -   InformaCast

InformaCast

1. Create the CUCM cluster

2. Refresh recipient groups

3. Set SIP access and deny all ips,  and allow just the CUCM ip

4. Enable SIP for the call

- Configure a Panic Button

1. Select the pre-recorded message for the panic button.  In the wizard there is only one option for the pre-recorded message that

contains audio and text message that is sent toward the phones.  The message can be changed afterwards in the InformaCast server.

2. Enter the speed dial number for the target phones.  When that speed dial is pressed, the paging is activated.

3. Select the Route Partition that is applied in the Route Pattern that sends the call toward informacast.

4. Select the phones that contains the speed dial (panic button).

5. Set the rules andselect the phones that receives the paging.  This phones are added into the recepient group in InformaCast.

- Configure CallAware Emergency call Alerting

1. Select the pre-recorded message for the CallAware Emergency call.

2. Select the Route P attern/s with the number that CallAware does monitor.

3. Set the rules and select the phones that receives the paging.   When Call these Route Patterns a notification is generated and sent by InformaCast toward the phones that match the rules.

## Verify

-  For the Panic Button feature  press the speed dial created in the phone.    The phones selected as destination (with the Test Rules)  must play the audio through the speaker.

-  For the CallAware notification,  call  the Route Pattern that was selected and the phones selected as destination must receive an audio prompt that indicates which device made the call.

## Troubleshoot

If there is no audio but the speaker gets activated on the phone, this is probably a multicast issue in the network.  But all the configuration in CUCM and Informacast if fine.

Cisco TAC troubleshoots only the wizard part for the Emergeny Notification feature in CCM 12.x

If for any reason the Emergency Notification wizard fails, and you need to restore it to start the configuration again, we can do as follow:

1. Delete all the informacast configuration that was created in CUCM:  Region, Device Pool, SIP trunk, route pattern,  application user and snmp community string.

2. Delete the Informacast entries from scratch table to allow the wizard to be re-run.

Note : {Be careful deleting information from the Scratch table since it is a BLOB that contains device specific information, service parameter specification, dependancy results, etc. Some records are temporary, some need to persist.  So please be cautious while deleting the entries from it, ensure “WHERE” clause in delete statement is correct.    WHERE clause must be referring to deleting  information in the wizard.}

- Before deletion, check how many records exists for EmergencyNotification Wizard.

```
admin: run sql select * from scratch where name like ‘wiz%informacast%’
```

- Delete the informacast wizard informacation from the scratch table.  Do NOT forget teh where statement

```
admin: run sql delete from scratch where name like ‘wiz%informacast%’
```

### Contributed by Cisco Engineers

Contributed by Alejandra Gonzalez Romero

Cisco TAC

Edited by Gurpreet Kukreja

Cisco TAC

Edited by Luis Yanes

Cisco TAC

### This Document Applies to These Products

- Paging Server

- Unified Communications Manager (CallManager)