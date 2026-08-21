---
doc_id: www-cisco-com-c-en-us-support-docs-voice-dial-plan-118822-configure-cucm-00-html-2635fef122
source_url: https://www.cisco.com/c/en/us/support/docs/voice/dial-plan/118822-configure-cucm-00.html
retrieved_at: 2026-08-21T13:54:05.727736+00:00
---

CUCM Dial Plan Considerations for CMR in CUCM-Centric Deployment Configuration Example

# CUCM Dial Plan Considerations for CMR in CUCM-Centric Deployment Configuration Example

### Download Options

Updated: March 10, 2015

Document ID: 118822

Contents

## Contents

## Introduction

This document describes the dial plan considerations on Cisco Unified Communications Manager (CUCM) when Collaboration Meeting Rooms (CMR) are used in a CUCM-centric deployment. It discusses the different options, the implications, and the configuration.

## Prerequisites

### Requirements

CMR is supported as of TelePresence Conductor Version XC2.3 and TelePresence Management Suite Provisioning Extension (TMSPE) Version 1.2. This document does not cover the configuration of CMR, which is covered in Cisco TelePresence Management Suite Provisioning Extension Deployment Guide .

### Components Used

The solution in this example uses TelePresence Management Suite (TMS), TMSPE, TelePresence Conductor, TelePresence Server (TS), and CUCM. The other illustrated components (Expressway-C and Expressway-E) are optional and provide connectivity to endpoints on the Internet and/or Business-To-Business Calls.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Network Diagram

Since this document uses a CUCM-centric deployment, the Expressway series is used and the Conductor is integrated with CUCM. A typical deployment is illustrated here:

In this example, the Session Initiation Protocol (SIP) domain in the deployment is company.com and users can be reached via Uniform Resource Identifier (URI) dialing, for example user1@company.com .

### Configurations

The CMR are hosted by the TelePresence Servers. In order for users to dial into them, calls must be routed towards the SIP Trunk to the Conductor. There are two options for the format of the URI for the CMR.

#### Option 1: CMR Format - user1@meet.company.com

The first option uses a subdomain of company.com as the domain portion in the URIs of the CMR: meet.company.com .

This makes the dial plan configuration on CUCM straighforward; you can configure a new SIP Route Pattern with Domain Routing for this subdomain as illustrated here:

Note that in this example, no Route Partition is configured on the SIP Route Pattern and is hence reachable to all devices. Class Of Control using Call Search Spaces (CSS) and Partitions can be used in order to restrict certain users/devices to dial these patterns.

#### Option 2: CMR Format - meet.user1@company.com

The second option uses the main domain as the domain portion in the SIP URIs of the CMR: company.com .

SIP Route Patterns do not support regular expressions, so you could configure the SIP Route Pattern as illustrated here:

With this configuration, every URI that matches the domain portion company.com that is not in the CUCM database (locally-registered endpoints) is routed to the Conductor. It is important to note that calls to URIs not registered on CUCM are sent to the Conductor (even for URIs the Conductor is not aware about). In order to overcome this, you can use the InterCluster Lookup Service (ILS) import, which is described later.

The previous solution works when the deployment does not have any endpoints registered to the Video Communication Server (VCS) that shares the same domain or Lync integration that shares the same domain. In case there are endpoints or a Lync integration that share the same domain, some calls with the domain portion company.com must be sent to Expresssway-C/VCS-C, while calls towards the CMR (which also have the domain portion company.com ) must be routed to the Conductor. An example deployment where the same domain is shared between endpoints registered to CUCM and a third-party Call Control system is shown here:

In this situation, you must use the ILS import feature in order to import Conductor SIP URIs as Global Catalog into the CUCM ILS table. As the source for this import, you can export the room data in TMS. This option is available under System > Provisioning > Users .

It is important to note, however, that if the CMR has not been created by the user, the room is not listed in this export. This means that you must perform this procedure every time a new room is created or export data from Active Directory (AD) in order to build the list for all users.

On CUCM, you must complete these steps:

- Make sure the Cisco ILS and the Cisco Bulk Provisioning Service are activated and run.

```
PatternType,PSTNFailover,Pattern URI,,meet.user1@company.com URI,,meet.user2@company.com
```

Once the job has been completed, calls to URIs in the text file are routed to the SIP trunk to the Conductor.

## Verify

When no URIs are imported in the Global Catalog, you can test if you call the URI of a CMR that has been created. On CUCM, you must make sure:

- The CSS of the calling device must contain the partition configured on the SIP Route Pattern.

In case URIs have been imported into the Global Catalog, you also must make sure that:

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

- TelePresence Management Suite Provisioning Extension Guides

- CUCM Maintain and Operate Guides

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

10-Mar-2015

Initial Release

### Contributed by Cisco Engineers

Kristof Van Coillie

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Mar-2015 | Initial Release |