---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-221698-enable-secure-communication-between-cms-html-f589f3a961
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/221698-enable-secure-communication-between-cms.html
retrieved_at: 2026-08-16T14:21:53.844636+00:00
---

Enable Secure Communication Between CMS and CUCM

# Enable Secure Communication Between CMS and CUCM

Log in to Save Content

### Download Options

Updated: February 16, 2024

Document ID: 221698

Contents

## Contents

## Introduction

This document describes how to enable communication between the Cisco Meeting Server (CMS) and the Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CMS version 3.8 and later

- CUCM and IM&P

- Jabber

### Components Used

The information in this document is based on these software and hardware versions:

- CMS version 3.8

- CUCM and IM&P 14 SU (3)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document outlines the process of establishing secure communication between CMS and CUCM for Jabber/Web app presence sharing. It explains the detailed steps for configuring and troubleshooting the updating status of Jabber users during web app meetings on the CMS. The Meeting Server can be configured in order to update the presence status of Jabber users while they are engaged in a Cisco Meeting Server web app meeting.

## Configure

### Enabling Secure Communication between CMS and CUCM/IMP Server

Log into CUCM on the OS admin page, navigate to Security > Certificate Management , and download the TOMCAT certificate.

CUCM Tomcat Certificate

Log into the Cisco Unified Presence Server (CUPS) on the OS admin page, navigate to Security > Certificate Management , and download the CUPS certificate.

Presence CUPS certificate

Download the ROOT CA Certificate which signed the Tomcat and Cup certificate.

Root certificate of Tomcat

Root certificate for CUPS

Create a certificate bundle of CUCM certificates. A bundle certificate means, placing the Server certificate on top, the intermediate certificate (any) in the middle, and the ROOT certificate at the bottom, followed by one (1) carriage return.

Here is a sample for the BUNDLE certificate:

Tomcat certificate bundle

Create a certificate bundle of CUPS certificates. A Bundle certificate means, placing the Server certificate on top, the intermediate certificate (any) in the middle, and the ROOT certificate at the bottom, followed by one (1) carriage return.

CUPS certificate bundle

Push the bundle certificates created earlier to the CMS server via WinSCP.

Copying Certificates Bundle to CMS

Assign TOMCAT bundle certificate on Callbridge using callbridge ucm certs <cert-bundle> .

Callbrigde cert trust

Assign CUP server bundle certificate on Callbridge using callbridge imps certs <cert-bundle> .

Run the callbridge command in order to check if the certificate bundles are assigned.

Callbridge trust cert check

Log into CUCM as CM Administrator, navigate to User Management > User Settings > Access Control Group , click Add New and create an Access control Group CUCM_AXL_Group .

Creating AXL group

Assign the role Standard  AXL API Access to the Access Control Group created earlier.

Assigning API access to AXL group

Navigate to User Management > Application User , click Add New and create an Application User AXLuser . Then, assign the access control group, which was created earlier.

Creating a user and assigning AXL group

Create a CUP user and assign these two roles: Third Party Application Users and Admin-3rd Party API .

Creating CUP user

Enable certificate verification for the CUCM and Cisco Unified Communications Manager IM & Presence Service (IMPS) certificate on the CMS using:

callbridge ucm verify <enable/disable>

callbridge imps verify <enable/disable>

Callbridge verify CUCM and CUPS cert

Verify it by running the callbridge command.

Callbrdge command check

Now add CUCM Fully Qualified Domain Name (FQDN) and the User AXL and CUPS created earlier on CMS using callbridge ucm add <hostname/IP> <axl_user> <presence_user> .

axl_user = AXL user on CUCM

presence_user = CUP user created earlier

Adding CUCM to Callbridge

Now, verify if CMS trusts CUCM services with the help of:

callbridge ucm <hostname/IP> axl_service status

callbridge ucm cucm14test.test.com axl_service status

Callbridge AXL status

callbridge imps <hostname/IP> <presence_user> presence_service status

wb3> callbridge imps impnew.test.com cisco presence_service status

Callbridge presence status

Services available means CUCM and CMS trust each other for AXL and Presence services.

Note : CUCM has Lightweight Directory Access Protocol (LDAP) users synced and also updated on the CUPS. The users must have the same web app user ID and Jabber JID and must be signed into the web app with the same user ID, for presence to be updated on Jabber.

### CUCM Specific Configuration for Presence Sharing between Webapp and Jabber Client

CUCM must have LDAP configured.

LDAP System:

CUCM LDAP configuration 1

LDAP Directory:

CUCM LDAP configuration 2

LDAP Authentication:

CUCM LDAP configuration 1 CUCM LDAP configuration 1 CUCM LDAP configuration 1 CUCM LDAP configuration 3

Users pulled from LDAP into CUCM with Mail-ID configured:

Users in CUCM

CUCM user updated on CUPS server:

Users in CUPS

The same LDAP Directory is also configured on the CMS. The user database is pulled and synced on CMS.

CMS users

Now, since you have already validated that CMS can trust CUCM, you can proceed with testing Presence.

Adding CUPS and CUCM to CMS

## Verify

Signed on two clients with the same user (synced from the same LDAP):

User login in Jabber and webapp

Both clients signed into the same user test@test.com .

Presence in Jabber and Webapp before call

Presence status changes when call is joined from webapp

When a Jabber user signs into the web app and joins a meeting, the Meeting Server updates the Jabber status to ‘In a meeting, In a call’ and reverts to its previous status after the user ends the meeting. For example, if the status of the user on Jabber is showing ‘Available’, it is updated to ‘In a meeting, In a call’ when in a web app meeting. After the user leaves the meeting, the Jabber status is set to ‘Available’ again. If the Jabber user is in another meeting/call while joining the web app meeting, the Meeting Server does not update the Jabber status. If the Jabber user has set their status to 'DND - Do not disturb' before joining the web app meeting, the Meeting Server does not update the Jabber status. If the user updates the Jabber status manually anytime during the web app meeting, the Meeting Server does not override the manually updated user status.

### Revision History

1.0

16-Feb-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 16-Feb-2024 | Initial Release |