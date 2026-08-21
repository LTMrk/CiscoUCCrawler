---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200978-how-to-enabl-a4b182986b
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200978-How-to-Enable-Common-PIN-for-UCM-and-UC.html
retrieved_at: 2026-08-21T13:55:47.084125+00:00
---

How to Enable  Common PIN for CUCM and UCXN.

# How to Enable  Common PIN for CUCM and UCXN.

### Download Options

Updated: May 25, 2017

Document ID: 200978

Contents

## Contents

## Introduction

This document describes the procedure to configure the common pin set up for Cisco Unified Communication Manager (CUCM) and Cisco Unity Connection (UCXN) in version 11.5.

## Prerequisites

### Requirements

Cisco recommends that you know how to create users and associate devices to the users.

Before you start configure the common pin you need to integrate the CUCM to UCXN.

### Components Used

The information in this document is based on these software and hardware versions

- Cisco CallManager 11.5

- Cisco Unity 11.5

Note : The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The user needs to access UC application such as Meet Me conference, Extension Mobility, and Voicemail when use same PIN, so you don’t have to manage multiple PIN credentials. The user would like the ability to set/change a (common) PIN on the self-care portal.

The administrator needs the ability to specify when a common PIN between CUCM/Unity must be used, in order to choose when the PINs are different or synchronized. The administrator wants the ability to enable the common PIN for all users assigned to the specific Unity.

In CUCM version 11.5 there is a new check box Enable End User Pin Synchronization under Application Server page when we select Application Server Type as Cisco Unity Connection.

## Feature overview

- Provision to enable end user pin synchronization between CUCM and UCXN through Application Server page from CUCM Administration UI

- If pin synchronization is enabled and when a user updates the pin from CUCM, BAT (Buk Administration Tool), AXL (Administrativve Extensible Markup Language), UDS (User Data Service) or Self Care Portal the pin must synchronized with UCXN

- Pin must syncronized  between CUCM and UCXN and vice versa when Pin synchronization is enabled in both Applications

- By default, Pin synchronization should be disabled when you try to create a new Unity Connection record or when you do an upgrade and try to load any current unity connection record.

## Configuration

Step 1.

Create an end user on CUCM and associate that with a device

Step 2.

Import that User to Unity

Step 3.

Navigate to OS Administration in CUCM

Step 4.

Download the Tomcat certificate

Step 5.

Upload this as tomcat trust in Unity

Step 6.

Now Download the Tomcat certificate from Unity and upload this as tomcat trust in CUCM

Step 7.

Create an application user in CUCM with credential of Unity

Step 8.

Assign this user the role of AXL

Step 9.

Assign AXL role to the CUCM app user as well

Step 10.

Now navigate to Cisco Unity Connection and check the Enable End User Pin Synchronization

Step 11.

From the CUCM navigate to System>Application server>Add the new application server as Csico Unity Connection  (if not already added)

Step 12.

Check the check box Enable End User Pin Synchronization

Step 13.

Click on Save

The message Pin Synchronization successful is received.

## Troubleshoot

### Issue 1.

Error message “Pin synchronization is not enabled due to Certificate not verified.”

Troubleshoot steps

- Check certificates are uploaded properly.

- Check the Unity Connection is reachable and we are able to successfully log in.

### Issue 2.

Error message ”Pin synchronization is not enabled due to HttpsURLConnection response code: 401 : Unauthorized"

Troubleshoot Steps

- Ensure that you have checked the Enable End User Pin Synchronization on

- Ensure that you have assigned the AXL role to App users.

## Related Information

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/administration/guide/b_cucsag/b_cucsag_appendix_01111.html#id_16699

### Contributed by Cisco Engineers

Vineet Kumar Gautam

Cesar Alonso

Cisco TAC Engineers

### This Document Applies to These Products

- Unified Communications Manager (CallManager)