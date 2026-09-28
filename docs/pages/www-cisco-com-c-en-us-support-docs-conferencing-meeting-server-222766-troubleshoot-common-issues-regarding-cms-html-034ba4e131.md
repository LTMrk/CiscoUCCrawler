---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-222766-troubleshoot-common-issues-regarding-cms-html-034ba4e131
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html
retrieved_at: 2026-08-18T23:50:18.271634+00:00
---

Troubleshoot common issues regarding CMS conference bridge registration on CUCM

# Troubleshoot common issues regarding CMS conference bridge registration on CUCM

### Download Options

Updated: February 13, 2025

Document ID: 222766

Contents

## Contents

## Introduction

This document describes common issues faced when trying to register Cisco Meeting Server (CMS) as a conference bridge on Cisco Unified Call Manager (CUCM).

## Prerequisits

- Have configured a SIP Trunk from CUCM to CMS using CMS's FQDN rather than IP

- Have configured the CMS conference bridge on CUCM, having enabled the Override SIP Trunk Destination as HTTPS Address Hostname.

1. TLS version mismatch It can happen that CUCM is using TLS 1.0 whereas CMS is using TLS 1.2 From version 2.3, the Meeting Server uses a minimum of TLS 1.2 and DTLS 1.2 for all services: SIP, LDAP, HTTPS (inbound connections: API, Web Admin and Web Bridge; outbound connections: CDRs) and XMPP.

Solution If needed for interop with older software that has not implemented TLS 1.2, a lower version of the protocol can be set as the minimum TLS version for the SIP, LDAP and HTTPS services. See tls <service> min-tls-version <minimum version string> and tls min-dtls-version <minimum version string> commands in the MMP Command reference guide for CMS. Note: A Call Bridge restart is required for changes to the tls configuration to be applied.

2. CUCM not sending any TCP traffic to CMS It can happen that you see no traffic arriving from CUCM on CMS.

Solution

The reason this can happen is because CUCM is unable to resolve the URL to connect to CMS. Make sure the URL used in the Override SIP Trunk Destination as HTTPS Address Hostname on the conference bridge has a corresponding A record on the DNS which the CUCM is using.

Alternatively, m ake sure that the Primary DNS of CUCM is able to resolve the FQDN of CMS. The secondary DNS node configured on CUCM will not be used unless the primary DNS node is completly not reachable.

In the CUCM SDL logs you will see this:

```
87042368.004 |15:18:18.129 |AppInfo |ConnectionFailureToPDP - A connection request from Unified CM to the policy decision point failed Policy Decision Point: https://webbridge_test.test.com:445/RPC2/ The cause of the connection failure:Invalid URI App ID:Cisco CallManager Cluster ID:StandAloneCluster Node ID:TPCUCMPUB 87042368.005 |15:18:18.129 |AlarmErr |AlarmClass: CallManager, AlarmName: ConnectionFailureToPDP, AlarmSeverity: Error, AlarmMessage: , AlarmDescription: A connection request from Unified CM to the policy decision point failed, AlarmParameters: PolicyDecisionPoint: https://webbridge.test.com:445/RPC2/ , FailedToConnectReason:Invalid URI, AppID:Cisco CallManager, ClusterID:StandAloneCluster, NodeID:TPCUCMPUB,
```

3. CMS not regitsering becasue of certificate issue

You see the TCP traffic being exchanged between CUCM and CMS, however CUCM is resetting the TCP cpnnection.

Solution

During the 3 way handshake to set up the TCP connection between CMS and CUCM, CMS is presenting its webadmin certificate to CUCM. The URL used in the ovverride prameter needs to be present in the WebAdmin certificate either as CN or in the SAN field.

### Revision History

1.0

13-Feb-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 13-Feb-2025 | Initial Release |