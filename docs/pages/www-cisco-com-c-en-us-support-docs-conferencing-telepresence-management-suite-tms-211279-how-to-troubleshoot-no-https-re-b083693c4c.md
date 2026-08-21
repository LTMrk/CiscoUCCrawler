---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-telepresence-management-suite-tms-211279-how-to-troubleshoot-no-https-re-b083693c4c
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-suite-tms/211279-How-to-Troubleshoot-No-HTTPS-response.html
retrieved_at: 2026-08-21T06:29:26.392750+00:00
---

How to Troubleshoot "No HTTPS response" Error on TMS After TC/CE Endpoints Upgrade

# How to Troubleshoot "No HTTPS response" Error on TMS After TC/CE Endpoints Upgrade

### Download Options

Updated: May 23, 2017

Document ID: 211279

Contents

## Contents

## Introduction

This document describes how to troubleshoot "no HTTPS response" message on Telepresence Management Suite (TMS).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco TMS

- Windows Server

### Components Used

The information in this document is based on these software versions:

TC 7.3.6 and above

CE 8.1.0 and above

TMS 15.2.1

Windows Server 2012 R2

SQL Server 2008 R2 and 2012

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

This issue occurs when the endpoints are migrated to TC 7.3.6 and Collaboration Endpoint  (CE) 8.1.0 software or above.

## Problem

After an endpoint upgrade to TC7.3.6 or above or  8.1.0 or above and the communication method between the endpoint and the TMS is set up as Transport Layer Security (TLS), the error message "no HTTPS response" pops up on TMS by selecting the Endpoint, under System > Navigator .

This happens as a result of this situations.

- TC 7.3.6 and CE 8.1.0 and above no longer support TLS 1.0 as per the release notes.

http://www.cisco.com/c/dam/en/us/td/docs/telepresence/endpoint/software/tc7/release_notes/tc-software-release-notes-tc7.pdf

- Microsoft Windows server has TLS version 1.1 and 1.2 disabled by default.

- TMS tools uses Medium Communication Security in its Transport Layer Security Options by default.

- When TLS version 1.0 is disabled and both TLS version 1.1 and 1.2 are enabled, TMS doesn’t send Secure Socket Layer (SSL) Client hello after TCP 3-Way handshake succeeds with the Endpoint. However still able to encrypt data using TLS version 1.2.

- Enabling TLS version 1.2 using a Tool or in the Windows Registry is not enough, as the TMS will still only send or advertise 1.0 in its Client hello messages.

## Solution

The Windows server where the TMS is installed, needs to have TLS version 1.1 and 1.2 enabled, this can be achieved with the next procedure.

### Enable TLS 1.1 and 1.2 on TMS Windows Server for TMS 15.x and higher

Step 1. Open a Remote Desktop Connection to Windows Server where TMS is installed.

Step 2. Open Windows Registry editor ( Start -> Run -> Regedit ).

Step 3. Take backup of Registry.

If you're prompted for an administrator password or confirmation, type the password or provide confirmation.

Locate and click the key or subkey that you want to back up.

Click the File menu, and then click Export .

In the Save in box, select the location where you want to save the backup copy to, and then type a name for the backup file in the File name box.

Click Save .

Step 4. Enable TLS 1.1 and TLS 1.2.

- Open Registry

- Navigate to HKEY_LOCAL_MACHINE --> SYSTEM --> CurrentControlSet --> Control --> Se curityProviders --> SCHANNEL --> Protocols

- Add TLS 1.1 and TLS 1.2 support

- Create TLS 1.1 and TLS 1.2 folders

- Create sub-keys as client' and 'server

- Create DWORDs for both Client and Server for each TLS key created.

```
DisabledByDefault [Value = 0]
 Enabled [Value = 1]
```

Step 5. Restart TMS Windows server to ensure TLS take effect.

Note : Visit this link for specific information on aplicable versions https://technet.microsoft.com/en-us/library/dn786418%28v=ws.11%29.aspx#BKMK_SchannelTR_TLS12

Tip : NARTAC tool can be used to disable the TLS needed versions after you do that you need to restart the server. You can download it from this link https://www.nartac.com/Products/IISCrypto/Download

### Security change on TMS Tool

When the correct versions are enabled, change the Security settings on TMS Tools with this procedure.

Step 1. Open TMS tools

Step 2. Navigate to Security Settings > Advanced Security Settings

Step 3. Under Transport Layer Security Options , set the Communication Security to Medium-High

Step 4. Click Save

Step 5. Then restart both the Internet Information Services (IIS) on the server and TMSDatabaseScannerService and start TMSPLCMDirectoryService (if it’s stopped)

Warning : : When TLS option is changed to Medium-High from Medium, telnet and Simple Network Management Protocol (SNMP) will be disabled. This will cause to TMSSNMPservice to stop and an alert will be raised on TMS web interface.

### Considerations in order to upgrade security settings

When SQL 2008 R2 is in use and installed on TMS windows server, we need to ensure TLS1.0 and SSL3.0 should also be enabled or else SQL service stop and it won't start.

You must see this errors on the event log:

When SQL 2012 is in use it requires to be updated to tackle TLS change if installed on TMS windows server ( https://support.microsoft.com/en-us/kb/3052404 )

Endpoints managed using SNMP or Telnet show "Security violation: Telnet communication is not allowed".

## Verify

When you change the TLS option from Medium to Medium-High, this ensures that TLS version 1.2 is advertised in the Client Hello after the TCP 3-Way handshake suceeds from TMS:

TLS version 1.2 advertised:

If it's left at medium TMS will only send version 1.0 in the SSL Client hello during the negotiation phase which specifies the highest TLS protocol version it supports as a client, which TMS is, in this case.

## For TMS versions lower than 15

Step 1. Even though the TLS version 1.2 is added in the registry

Step 2. The TMS server still doesn’t send the version supported by the Endpoint in its SSL client hello

Step 3. The problem then lies in the fact that we cannot change the TLS Options in TMS tools as this option is not available

Step 4. Then the workaround for this issue is either upgrade TMS to 15.x or downgrade your TC/CE endpoints to 7.3.3, this issue is tracked in software defect CSCuz71542 created for version 14.6.X.

### Contributed by Cisco Engineers

Joshua Alero

Cisco TAC Engineer

Geovanny Olivares

Cisco TAC Engineer

### This Document Applies to These Products

- TelePresence Management Suite (TMS)