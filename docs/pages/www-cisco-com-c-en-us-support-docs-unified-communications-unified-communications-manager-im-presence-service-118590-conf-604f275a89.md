---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-118590-conf-604f275a89
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/118590-config-cucm-00.html
retrieved_at: 2026-08-16T23:36:37.383200+00:00
---

Configure DNS SRV in CUCM for IM & Presence Service

# Configure DNS SRV in CUCM for IM & Presence Service

### Download Options

Updated: November 20, 2014

Document ID: 118590

Contents

## Contents

## Introduction

This document describes the configuration of the Cisco Unified Communications Manager (CUCM) SPA Interface Processor (SIP) Trunk with the Domain Name System Server (DNS SRV) record of the IM & Presence.

For High Availability purposes, multiple IM & Presence server node destinations are configured in the IM & Presence Publish trunk of CUCM. A maximum of 16 destination IP addresses can be added in the SIP Trunk configuration. However, administrators prefer the use of SRV records instead of IP addresses, as SRV records are easier to manage. SRV records are populated in the DNS server, and thus centralized management is achieved when you point the SIP trunk destination to the DNS SRV record.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- DNS SRV

- Cisco IM & Presence Server

- Cisco Unified Communications Manager

### Components Used

The information in this document is based on these software and hardware versions:

- Active Directory 2008 and later

- CUCM Version 10

- IM & Presence Server Version 10

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Note : Use the Command Lookup Tool ( registered customers only) in order to obtain more information on the commands used in this section.

### Configure the DNS Server

Complete these steps in order to configure the DNS server:

In this example, the CUCM and IM & Presence sub-domains were created in the test lab for demonstration.

- _sip._tcp.subdomain1.domain

- _sip._tcp.subdomain2.domain

In the test lab, the domains are:

- _sip._tcp.cup.ccie.com

- _sip._tcp.cucm.ccie.com

In order to verify SRV lookup from a Microsoft Windows command prompt, enter the nslookup command.

```
nslookup set type=srv sip._tcp.cup.domain.com
```

For example, refer to this code example:

### Configure the CUCM Server

Complete these steps in order to configure the CUCM server:

Note : Only the subdomain.domain part of the SRV record should be added here. The CCM service prefixes _sip._tcp to the SRV request when it generates the request.

- Save the SIP Trunk configuration.

### Configure the IM & Presence Server

Complete these steps in order to configure the IM & Presence server:

From the IM & Presence server administration page, select P resence > Presence Gateway . Configure a CUCM PRESENCE gateway as shown here.

This configuration specifies the servers from where Phone presence is accepted.

Note : The complete name of the CUCM SRV record should be added in the Presence Gateway configuration.

### Signal Path

This section provides information in regards to signalling between the different components involved in this configuration.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

20-Nov-2014

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 20-Nov-2014 | Initial Release |