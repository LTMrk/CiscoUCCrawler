---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-212052-configure-di-62ce3d33ae
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/212052-Configure-Display-Name-in-Communications.html
retrieved_at: 2026-08-21T13:56:37.011631+00:00
---

Configure Display Name in Communications Manager (CUCM) Self-Care Portal

# Configure Display Name in Communications Manager (CUCM) Self-Care Portal

### Download Options

Updated: September 13, 2017

Document ID: 212052

Contents

## Contents

## Introduction

This documented describes the new Display Name feature introduced in Communications Manager (CUCM) 11.5. You can now assign a personal Display Name in the self-care portal instead of the CUCM End User configuration page.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics: • Cisco CallManager End User configuration • Cisco Self-Care Portal

### Components Used

The information in this document is based on Cisco CallManager 11.5 and later.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live ensure that you understand the potential impact of any command.

## Configure

Configure Display Name in Self-Care Portal

Step 1. Log in to the Self- Care portal page with the required credentials.

Step 2. Navigate to General Settings > Display Name.

Display Name Image

Step 3. Enter the required value in the space and select Save.

Note : For a LDAP integrated User the Display Name field is greyed out and cannot be edited.

Step 4. As soon as you select Save the End User configuration page on the CUCM End User Configuration Administration page updates.

Architecture between Self-Care Portal and CUCM

The communication between CUCM and the Self-Care Portal takes place through a RESTful Application Programming Interface (API) based set of operations known as User Data Services (UDS). It is represented in this image:

UDS runs the database queries on CUCM to save the Display Name Data as entered on the Self-Care Portal.

## Verify

Query the XML file from the browser for a specific User object. View the XML file the UDS uses for data exchange with the URL, https://{host}:8443/cucm-uds/users?displayname=” enter_text_here ”

Image: The Display Name field (boxed in red) automatically updates with the same value entered on the Self-Care portal page

## Troubleshoot

Step 1. Verify the changes to Display Name on the Self-Care Portal are Saved.

Step 2. Verify there are no database replication problems with the command utils dbreplication runtimestate in the command line interface (CLI) of the CUCM publisher.

Step 3. Before you can access the Cisco Unified Communications Self Care Portal, you must use Cisco Unified Communications Manager Administration to add the user to a standard Cisco Unified Communications Manager End User group.

### Contributed by Cisco Engineers

Animesh Lochan

Cisco TAC

Eric Leite

Cisco TAC

### This Document Applies to These Products

- Unified Communications Manager (CallManager)