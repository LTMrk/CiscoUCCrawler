---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-ip-phones-220248-configure-cucm-to-provide-screensaver-ca-htm-076197d917
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/ip-phones/220248-configure-cucm-to-provide-screensaver-ca.html
retrieved_at: 2026-08-21T13:59:33.176232+00:00
---

Configure CUCM to Provide Screensaver Capabilities to IP Phones

# Configure CUCM to Provide Screensaver Capabilities to IP Phones

### Download Options

Updated: February 22, 2023

Document ID: 220248

Contents

## Contents

## Introduction

This document describes how to implement screensaver capabilities on Cisco Internet Protocol (IP) phones.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Configure a web server to provide XML files and images to the phones.

- IP connectivity to the phone for access from the phone to the web server.

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM version 14.0.1.12900-161.

- Microsoft Internet Information Services (IIS) configured on a Windows server 2016.

- In this example, a Cisco IP Communicator softphone is used; however, the screensaver feature is available on other phone models.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Configurations

Step 1. In the CUCM administration page, go to device and then phone and select the IP phone intended to be modified.

Step 2. Populate the Idle field with the URL to be used by the phone to reach out to the external web server for eXtensible Markup Language (XML) instructions.

Step 3. Create an XML file with the URL to be used to fetch the image from:

Step 4. Upload the XML file and the image to the web server for IP phones to be able to fetch it.

## Verify

Leave the IP phone idle until the idle timer is reached and check in the IP phone screen if the desired image is displayed as screensaver:

## Troubleshoot

Perform a packet capture and confirm that:

- The IP phone is able to reach the web server.

- The web server is able to provide the XML file to the IP phone.

- The IP phone is able to request the image file to be displayed as screensaver.

- The file is provided by the web server in the expected resolution.

### Revision History

1.0

22-Feb-2023

Initial Release

### Contributed by Cisco Engineers

Leonardo Correa

Cisco TAC Engineer

Anthony Nunez

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 22-Feb-2023 | Initial Release |