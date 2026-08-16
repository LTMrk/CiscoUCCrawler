---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-118779-configure-cu-4f3c524699
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/118779-configure-cucm-00.html
retrieved_at: 2026-08-16T23:42:24.382868+00:00
---

CUCM Third-Party CA-Signed LSCs Generation and Import Configuration Example

# CUCM Third-Party CA-Signed LSCs Generation and Import Configuration Example

### Download Options

Updated: March 9, 2015

Document ID: 118779

Contents

## Contents

## Introduction

Certificate Authority Proxy Function (CAPF) Locally Significant Certificates (LSCs) are locally-signed. However, you might require phones to use third-party Certificate Authority (CA)-signed LSCs. This document describes a procedure that helps you achieve this.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unified Communication Manager (CUCM).

### Components Used

The information in this document is based on CUCM Version 10.5(2); however, this feature works from Version 10.0 and later.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Here are the steps involved in this procedure, each of which is detailed in its own section:

### Upload the CA-Root Certificate

- Log into the Cisco Unified Operating System (OS) Administration web GUI.

- Navigate to Security Certificate Management .

- Click Upload Certificate/Certificate chain .

- Choose CallManager-trust under Certificate Purpose.

### Set Offline CA for Certificate Issue to Endpoint

- Log into the CUCM Administration web GUI.

- Navigate to System > Service Parameter .

- Choose the CUCM Server and select Cisco Certificate Authority Proxy Function for the Service.

### Generate a Certificate Signing Request (CSR) for the Phones

- Log into the CUCM Administration web GUI.

- Navigate to Device Phones .

- Choose the phone whose LSC must be signed by the external CA.

- Change the Device security profile to a secured one (if not present, add one system on the Security Phone Security profile).

Note : The Certificate Operation Status under the phone's CAPF section remains in the Operation Pending state.

### Get the Generated CSR from the CUCM to the FTP (or TFTP) Server

- SSH into the CUCM server.

### Get the Phone Certificate

- Send the phone's CSRs to the CA.

Note : You can use a Microsoft Windows 2003 server as the CA. The procedure to sign the CSR with a Microsft Windows 2003 CA is explained later in this document.

### Convert .cer to .der Format

If the received certificates are in .cer format, then rename them to .der.

### Compress the Certificates (.der) to .tgz Format

You can use CUCM server's root (Linux) in order to compress the certificate format. You can also do this in a normal Linux system.

```
tar -zcvf <file_name>.tgz    *.der
```

### Transfer the .tgz File to the SFTP Server

Complete the steps shown in the screen shot in order to transfer the .tgz file to the SFTP server.

### Import the .tgz File to the CUCM Server

- SSH into the CUCM server.

### Sign the CSR With Microsoft Windows 2003 Certificate Authority

This is optional information for Microsoft Windows 2003 - CA.

- In order to download the certificate, choose Issued Certificate .

- Get the certificates for other phones under the Issued Certificate section with this procedure.

### Get the Root Certificate from the CA

- Open Certification Authority .

## Verify

Use this section in order to confirm that your configuration works properly.

- Go to the phone configuration page.

Note : Refer to Generate and Import Third Party CA-Signed LSCs for more information.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

09-Mar-2015

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 09-Mar-2015 | Initial Release |