---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-212084-troubleshoot-cisco-jabber-directory-sear-html-d6fa1eaa65
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/212084-Troubleshoot-Cisco-Jabber-Directory-Sear.html
retrieved_at: 2026-08-21T07:06:23.086860+00:00
---

Troubleshoot Cisco Jabber Directory Search Problems

# Troubleshoot Cisco Jabber Directory Search Problems

### Download Options

Updated: September 14, 2017

Document ID: 212084

Contents

## Contents

## Introduction

This document describes how to troubleshoot Cisco Jabber directory search problem when Secure Socket Layer (SSL) is configured.

Contributed by Khushbu Shaikh, Cisco TAC Engineers. Edited by Sumit Patel and Jasmeet Sandhu

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Jabber for Windows

- Wireshark

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

Jabber directory search does not work when SSL is configured.

## Jabber Log Analysis

Jabber logs show this error:

```
Directory searcher LDAP://gbllidmauthp01.sealedair.corp:389/ou=Internal,ou=Users,o=SAC not found, adding server gbllidmauthp01.sealedair.corp to blacklist. 2016-10-21 08:35:47,004 DEBUG [0x000034ec] [rdsource\ADPersonRecordSourceLog.cpp(50)] [csf.person.adsource] [WriteLogMessage] - ConnectionManager::GetDirectoryGroupSearcher - Using custom credentials to connect [LDAP://gbllidmauthp02.sealedair.corp:389] with tokens [1] 2016-10-21 08:35:47,138 DEBUG [0x000034ec] [rdsource\ADPersonRecordSourceLog.cpp(50)] [csf.person.adsource] [WriteLogMessage] - ConnectionManager::GetDirectoryGroupSearcher - failed to get a searcher - COMException [0x80072027]
```

## Packet Capture Analysis

In this packet capture, it can be seen that the Transmission Control Protcol (TCP) connection to the Active Directory (AD) server is successful but the SSL handshake between the client and the Lightweight Directory Access Protocol (LDAP) server fails. This causes Jabber to send a FIN message instead of the encrypted session key for the communication.

The issue still persists even though the signed AD certificate is uploaded to the client PC’s trust store.

Further analyzes of the packet capture reveals that Server Authentication is gone in Enhanced Key Usage section of the AD server certificate.

## Solution

A scenario was recreated with a certificate that has the Server Authentication in Enhanced Key Usage which resolved the issue. See the images of the certificates for comparison.

The Server Authentication identifier in the certificate is a prerequisite for a successful SSL handshake.

## Related Information

https://www.petri.com/enable-secure-ldap-windows-server-2008-2012-dc

### Contributed by Cisco Engineers

Khushbu Shaikh

Cisco TAC Engineer

Edited by Sumit Patel

Cisco TAC Engineer

Jasmeet Sandhu

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber