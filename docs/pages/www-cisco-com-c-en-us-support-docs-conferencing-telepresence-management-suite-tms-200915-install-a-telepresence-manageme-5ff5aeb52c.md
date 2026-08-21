---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-telepresence-management-suite-tms-200915-install-a-telepresence-manageme-5ff5aeb52c
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-suite-tms/200915-Install-a-Telepresence-Management-Suite.html
retrieved_at: 2026-08-21T06:28:52.417700+00:00
---

Install a Telepresence Management Suite (TMS) Release Key

# Install a Telepresence Management Suite (TMS) Release Key

### Download Options

Updated: January 2, 2017

Document ID: 200915

Contents

## Contents

## Introduction

This document describes how to install a Telepresence Management Suite (TMS) release key.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

Have reviewed TMS installation guide p rere quisites TMS guide

Have deployed Windows 2K12 server or similar version

Have installed a web browser such as Firefox, Chrome or Internet Explorer on Windows 2K12 server (optional)

Have successfully installed SQL on Windows 2K12 Server

Have downloaded and installed Telepresence Management Suite TMS software

Have obtained access to the web interface using Administrator privileges

Have applied for and received a license email with a Cisco Telepresence Management Suite Release Key

### Components Used

The information in this document is based on these software versions: Windows 2K12 server

Windows SQL Server

Telepresence Management Suite (TMS) version 15.3.X

A Remote Desktop application

A web browser such as Firefox, Chrome or Internet Explorer on Windows 2K12 server (optional)

Licensing email with a Release Key

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

This web interface example video supplements this document:

Note : An example license email is not available to show for this lab environment device.

Note : TMS Release Key should be the following format: XXXXXXXX-XX-XXXXXXXX where the X values represent the unique characters in your release key.

### Access the Web Interface From Windows Server

Step 1: Access the Windows Server which hosts TMS via Remote Desktop. Open a web broweser and navigate to https://localhost/tms:

Step2: Log in with an account with Administrator privileges when prompted:

Step 3: Click Advanced then Add Exception when you first log in to the web interface:

Step 4: Click Confirm Security Exception:

Note : Disable pop-up blockers if you do not receive this prompt.

Note : At this point you should have access to the TMS web interface.

### Access Web Interface Remotely

Step 1: Open a web browser on your local computer and enter the URL for TMS https://X.X.X.X/tms .

Note : Replace X.X.X.X with your Windows Server IP address.

Step 2:  Log in with an Administrator account when prompted:

Step 3: Click Advanced then Add Exception when you first log in to the web interface:

Step 4: Click Confirm Security Exception: as noted in the Access the Web Interface From Windows Server section of this document.

Note : Disable pop-up blockers if you do not receive this prompt.

Note : At this point you should have access to the TMS web interface.

### Install Release Key

Step 1: Navigate to Administrative Tools > Configuration > General Settings :

Step 2: Verify a release key has not been applied previously. Confirm at the bottom right hand corner of the General Settings web page the TMS serial number is labeled TRIAL :

Step 3: Copy your TMS release key from your license email and enter it in the TMS Release Key field. Click Save on the bottom left of the web interface.

Note : TMS Release Key should be the following format: XXXXXXXX-XX-XXXXXXXX where the X values represent the unique characters in your release key.

## Verify

Verify the release key added correctly. View the lower right of the web interface and notice that S/N: TRIAL (VMname)s now shows S/N: [SerialNumber] (VMname) :

## Troubleshoot

If you encounter an error, contact Cisco TAC.

### Contributed by Cisco Engineers

Travis Edwards

Cisco TAC Engineer

### This Document Applies to These Products

- TelePresence Management Suite (TMS)