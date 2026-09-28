---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-211288-mobile-and-remote-access-mra-license-k-html-132d7d59de
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/211288-Mobile-and-Remote-Access-MRA-License-K.html
retrieved_at: 2026-08-21T13:39:43.060832+00:00
---

Mobile and Remote Access (MRA) License Key Requirements Guide

# Mobile and Remote Access (MRA) License Key Requirements Guide

### Download Options

Updated: December 11, 2017

Document ID: 211288

Contents

## Contents

## Introduction

This document describes Mobile and Remote Access (MRA) license key requirements.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge on these topics:

- Expressway Series and Video Communication Server (VCS) Series application.

- Successfully installed a VCS Series or Expressway Series server and applied a valid IP address reachable via web interface and or Command Line Interface (CLI).

- Applied for and received a licensing email with any option or release keys valid for the device application serial number.

- Accessed the web interface with an admin account.

- Reviewed 'Install a VCS Option Key via the Web Interface and CLI Configuration Example'

- Install VCS Option Key

- Reviewed 'Install a VCS Release Key via the Web Interface and CLI Configuration Example'

- Install VCS Release Key

- Reviewed 'Install a Cisco Expressway Series Release Key via the Web Interface and CLI Configuration Example'

- Install Expressway Series Release Key

- Reviewed 'Install an Expressway Series Option Key via the Web Interface and CLI Configuration Example'

- Install Expressway Series Option Key

Note : VCS Installation guides can be found here: VCS Installation Guides

Note : Expressway Series Installation guides can be found here: Expressway Series Installation Guides

### Components Used

The information in this document is based on these software versions:

- Cisco VCS Series versions X8.1 and higher.

- Expressway Series versions X8.1 and higher.

- PuTTY (terminal emulation software)

- Alternatively, you could use any terminal emulation software that supports Secure Shell (SSH) such as Secure CRT, TeraTerm and so on.

- Licensing email with an Option Key or Release Key .

- A web browser, such as Firefox, Internet Explorer or Chrome.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Network Diagram

Cisco recommends a Dual NIC VCS Series or Expressway Series deployment as shown in the image.

Note : More information on Video Communication Server deployments found here, (Pg. 63-72): Deployment Scenarios

## Configure

These web interface example videos supplement this document:

VCS Release Key Install

VCS Option Key Install

Expressway Release Key Install

Expressway Option Key Install

### Required Keys

#### Video Communication Server - Control or Expressway - Core

- X.8 VCS Release Key for Control

- LIC-EXP-SERIES for Expressway Core

#### Video Communication Server - Expressway or Expressway - Edge

- X.8 VCS Release Key for VCS - Expressway

- LIC-EXP-SERIES for Expressway - Edge

- LIC-VCSE-E

### Optional Keys

#### Video Communication Server - Control or Expressway - Core

- LIC-EXP-RMS

#### Video Communication Server - Expressway or Expressway - Edge

- LIC-EXP-RMS

- LIC-VCS-DI /LIC-EXP-AN (Recommended)

- LIC-EXP-TURN

- LIC-EXP-GWY

### Key Description

X.8 Video Communication Server Release Key

LIC-EXP-SERIES

LIC-VCSE-E

**LIC-VCS-DI / LIC-EXP-AN

**LIC-EXP-RMS

**LIC-EXP-TURN

Note : Indicates Not Required For Mobile and Remote Access functionality

## Verify

Use this section in order to confirm that your configuration works properly.

Add the required MRA option and release keys to the VCS Series Device or Expressway Series Device. Navigate to Maintenance > Option Keys and note the keys displayed in the Option keys section.

Note : For VCS Series, review Install a VCS Option Key via the Web Interface and CLI Configuration Example Install VCS Option Key .

Also review Install a VCS Release Key via the Web Interface and CLI Configuration Example Install VCS Release Key .

Alternatively for Expressway Series, review Install a Cisco Expressway Series Release Key via the Web Interface and CLI Configuration Example Install Expressway Series Release Key and Install an Expressway Series Option Key via the Web Interface and CLI Configuration Example Install Expressway Series Option Key

Note : This example shows and Expressway Series Core and Edge device.

### Expressway-C

### Expressway-E

Note : Adding an Expressway Series key LIC-EXP-SERIES requires a RESTART of the Expressway Series device.

## Troubleshoot

This section provides information you can use in order  to troubleshoot your configuration.

You should not have any issues when you install a release key onto a Cisco VCS Series or Expressway Series. Enter an option key in the Release key field of the device or enter an option key when you upgrade are the most common causes for failure. An error occurs when an option key is entered in the Release Key field:

A VCS Series or Expressway Series accepts any value in the Release key field. Reboot the device with an incorrect value entered and you receive an error " Invalid release key ":

Install a release key as noted in guides recommended for review in the Requirements section of this guide to correct this condition.

Engage Cisco TAC for assistance for any other types of failure.

### Contributed by Cisco Engineers

Travis Edwards

Cisco TAC Engineer

| X.8 Video Communication Server Release Key | Activates Cisco Video Communication Server |
|---|---|
| LIC-EXP-SERIES | Enables Expressway Series |
| LIC-VCSE-E | Enables Expressway-E Feature Set |
| **LIC-VCS-DI / LIC-EXP-AN | Enables Dual NIC interfaces for Expressway-Edge |
| **LIC-EXP-RMS | Required for concurrent calls to and from any endpoint or application not registered to Cisco Unified Communications Manager. For example, business-to-business calls, Cisco Collaboration Meeting Rooms, Cisco Jabber Guest, and interworked calls (H.323 to SIP, H.264 AVC to H.264 SVC) |
| **LIC-EXP-TURN | Enables TURN Relay Option |
| **LIC-EXP-GWY | Enables Interworking Gateway Feature (H323-SIP) |