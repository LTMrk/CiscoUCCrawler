---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-telepresence-video-communication-server-vcs-119398-configure-m-348597ecd3
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/telepresence-video-communication-server-vcs/119398-configure-mra-00.html
retrieved_at: 2026-08-21T13:39:59.230122+00:00
---

Configure an MRA Hybrid Deployment

# Configure an MRA Hybrid Deployment

### Download Options

Updated: January 6, 2016

Document ID: 119398

Contents

## Contents

## Introduction

This document describes how to configure a hybrid Mobile and Remote Access (MRA) deployment and how to troubleshoot problems that might be encountered with this deployment.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

This section provides some background information that is useful for the procedures that are described in this document.

### Hybrid Service Discovery Flow

This is the hybrid service discovery flow, as described in the Cisco Jabber DNS Configuration Guide :

Once Cisco Jabber successfully logs in to the Cisco WebEx Messenger for Instant Message and Phone (IM&P) services, it checks to see whether the user is associated with a Cisco Unified Communications Manager (CUCM) cluster. If the user is associated to a CUCM cluster, and a _collab-edge Service (SRV) record is found for either the voiceservicesdomain or the WebEx Messenger domain, then the Jabber client attempts to retrieve the phone services from the configured CUCM cluster through the Cisco Expressways that are indicated in the _collab-edge query.

### DNS Requirements

The only Domain Name System (DNS) requirement for an MRA hybrid deployment is that a collab-edge._tls.<domain> SRV record be created on an external DNS server, and that it points to the Expressway-E external IP address on port 8443.

You are not required to create a _cuplogin._tcp.<domain> SRV record internally. Cisco recommends that you create a _cisco-uds._tcp.<domain> so that the Expressway-C can look up the home cluster of the Jabber clients that register via MRA.

As described in the Cisco Jabber DNS Deployment Guide :

In hybrid deployments the domain required to discover Cisco WebEx domain through CAS lookup may be different to the domain where the DNS records are deployed. In this scenario you set the ServicesDomain to be the domain used to discover Cisco WebEx and set the VoiceServicesDomain to be the domain where DNS records are deployed. The voice services domain is configured as follows:

- The client uses the VoiceServicesDomain parameter in the configuration file. This option is available in clients that support the jabber-config.xml file.

- Cisco Jabber for Android version 9.6 or later

- Cisco Jabber for Mac version 9.6 or later

- Cisco Jabber for iPhone and iPad version 9.6.1 or later

- Cisco Jabber for Windows version 9.6 or later

See the appropriate version of the Installation and Configuration guide, for more detailed information.

After Cisco Jabber gets the services domain, it queries the name server that is configured to the client computer or device.

## Configure

This section describes how to configure the Expressways C and E, and also how to configure Cisco WebEx so that the MRA hybrid deployment works properly.

### Network Diagram

A cloud hybrid deployment uses this network topology:

### Expressway C/E Configuration

These items must be configured on the Expressway-C and Expressway-E so that the MRA hybrid deployment works:

- Unified communications traversal zone

- Signed server certificates

- MRA enablement

- CUCM server and Cisco Unity server (Expressway-C only) additions

Complete the procedures that are described in the Unified Communications Mobile and Remote Access via Cisco Expressway Deployment Guide in order to configure the Expressways and prepare them for hybrid MRA phone services.

### WebEx Configuration

The configuration of the WebEx Messenger Administration Tool requires that you create a CUCM cluster and assign each user to that CUCM cluster.

Complete these steps in order to create a CUCM cluster on the WebEx Messenger Administration Tool:

- Log in to the Cisco WebEx Messenger Administration Tool .

- Click the Configuration tab:

- Click the Clusters tab in the Unified Communications area, and then click Add :

- Select the Enable Cisco UC Manager integration with Messenger Service Client radio button in the CUCM Cluster window.

Note : For advanced deployments, you can (optionally) specify up to three IP addresses or hostnames for the TFTP server, two IP addresses or hostnames for the Cisco Telephony Integration (CTI) servers, and two IP addresses or hostnames for the CCMCIP server.

Once a CUCM cluster is created, it must be assigned to a user. You can complete this via a Comma Separated Value (CSV) import and directory synchronization, or via the web interface (as described here).

Note : The CUCM cluster cannot be set or changed via the Single Sign On Auto Account Update or Create functions.

Complete these steps in order to assign a user via the web interface:

- Navigate to the User tab of the Org Admin tool and search for the user:

- Edit the user, navigate to the Unified Communications tab, and select the appropriate CUCM cluster:

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

This section provides information that you can use in order to troubleshoot your configuration.

### Phone Service Icon Does Not Appear on Jabber

If you sign in to a WebEx Messenger Jabber account and discover that the phone service icon does not appear in the lower corner of Jabber, it indicates that you do not have a CUCM cluster assigned to your user profile in WebEx.

Complete these steps in order to resolve this problem:

- Sign in to the WebEx Messenger administrative portal.

- Navigate to Users , select your user account, and then click Edit .

- Navigate to the Unified Communications tab and select the appropriate CUCM cluster.

- Sign out of Jabber, and then sign in.

### Phone Service Fails to Connect

If you encounter this issue, then refer to the Collaboration Edge Most Common Issues Cisco document for likely issues that cause the phone registration to the CUCM to fail.

### Revision History

1.0

06-Jan-2016

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- TelePresence Video Communication Server (VCS)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 06-Jan-2016 | Initial Release |