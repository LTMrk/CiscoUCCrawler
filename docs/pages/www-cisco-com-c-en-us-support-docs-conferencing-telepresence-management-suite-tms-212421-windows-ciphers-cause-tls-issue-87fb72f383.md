---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-telepresence-management-suite-tms-212421-windows-ciphers-cause-tls-issue-87fb72f383
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-suite-tms/212421-windows-ciphers-cause-tls-issue-between.html
retrieved_at: 2026-08-21T06:29:21.857981+00:00
---

Windows Ciphers Cause TLS Issue between TMS and OpenSSL Based Devices

# Windows Ciphers Cause TLS Issue between TMS and OpenSSL Based Devices

### Download Options

Updated: November 7, 2017

Document ID: 212421

Contents

## Contents

## Introduction

This document describes the issue that is caused when Cisco Telepresence Management Suite (TMS) is unable to connect to its managed devices and there is a "no https response" error reported in Cisco TMS. Cisco TMS fails to start/manage/monitor meetings.

## Background Information

Troubleshoot connectivity between TMS and the managed device itself should be done before you attempt this solution.

These steps should include:

1. Use capture software on the TMS Server (ex. Wireshark) to ensure network connectivity between TMS and the managed device.

2. Follow these Tech Notes:

- https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-server/118387-technote-tms-00.html

- https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-suite-tms/211279-How-to-Troubleshoot-No-HTTPS-response.html

## Problem

The analysis of a packet capture indicates that there is an issue with Cipher suite negotiations and usages between the Windows server that host TMS and Cisco TMS managed devices that include conferencing bridges and endpoints.

## Solution

When some of the Ciphers used for a Transport Layer Security (TLS) connection from Windows Servers that hosts TMS were disabled, it resolved some issues of Cisco TMS that reports "no https response" error for the managed devices. This could enable the meetings to be launched and monitored correctly. When you utilize the details noted in https://support.microsoft.com/en-us/help/2992611/ms14-066-vulnerability-in-schannel-could-allow-remote-code-execution-november-11,-2014 , if you disable these Ciphers, as per Microsoft's recommendation, it could alleviate the issue:

```
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 TLS_RSA_WITH_AES_256_GCM_SHA384 TLS_RSA_WITH_AES_128_GCM_SHA256
```

It has also been found that there might be other Ciphers that could cause issues when a TLS connection negotiates from a Windows client. For more information, refer to KB3172605 issues and its solution from this site: https://social.technet.microsoft.com/Forums/en-US/ccb5a498-ab3b-441d-a854-06b5e5af3bd7/kb3172605-issues-and-solution?forum=w7itprosecurity . When these Ciphers are disabled , that have been used for a TLS connection from Windows Server that hosts TMS, it can resolve some issues of the "no https response" errors with TMS managed devices:

```
TLS_DHE_RSA_WITH_AES_128_CBC_SHA TLS_DHE_RSA_WITH_AES_256_CBC_SHA
```

How to remove the Ciphers?

The simplest way to remove the Ciphers from the TMS Server is to use a third party tool called Internet Information Services (IIS) Crypto. Remove these Ciphers from the list and then you will have to reboot the TMS Server for the changes to take affect. It is recommended that this be done at off peak hours at the time of a maintenance window to ensure users are not affected by this change.

https://www.nartac.com/Products/IISCrypto

### Contributed by Cisco Engineers

Brian Pettis

Cisco TAC Engineer

### This Document Applies to These Products

- TelePresence Management Suite (TMS)