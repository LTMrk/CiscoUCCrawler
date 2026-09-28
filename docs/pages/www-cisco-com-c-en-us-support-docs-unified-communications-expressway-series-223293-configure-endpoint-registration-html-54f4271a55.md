---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-series-223293-configure-endpoint-registration-html-54f4271a55
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway-series/223293-configure-endpoint-registration.html
retrieved_at: 2026-08-16T15:41:46.498953+00:00
---

Configure Endpoint Registration Failover to Expressway Cluster

# Configure Endpoint Registration Failover to Expressway Cluster

### Download Options

Updated: July 28, 2025

Document ID: 223293

Contents

## Contents

## Introduction

This document describes the basic configuration steps for SIP Endpoints to work with an Expressway Cluster to achieve Registration Failover.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Expressway series.

- Telepresence endpoints.

- SIP protocol.

- DNS.

## Components Used

The information in this document is based on these software and hardware versions:

- Telepresence endpoints running software version RoomOS 11.27.3.

- Expressway cluster of 2 nodes running software version X15.2 (EXP C).

- Windows Server 2016.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

- Expressway can act as the registrar and call control server for Telepresence Endpoints over the SIP and H.323 protocols. This document focuses on SIP Registration.

- Specifying Expressway peers as SIP proxy 1, 2, 3, and 4 using either DNS names or IP addresses-on Cisco SIP endpoints does not provide redundancy. This configuration only works when the SIP outbound option is enabled, which has been deprecated as of Cisco Endpoint version CE8.0.

- Relying on DNS is the most reliable method to ensure redundancy and enable successful failover to other Expressway peers within the cluster.

- Failover test can be done by several ways for ex: Put Expressway in Maintenance mode, Disconnect network or shutdown the expressway.

## Configure

### Option 1: Using DNS SRV Records

- There must be a DNS SRV record available for the domain name of the Expressway that defines an equal weighting and priority for each cluster peer.

- The format of DNS SRV queries for sip (RFC 3263) and H.323 typically used by an endpoint are: • _sips._tcp. • _sip._tcp.<domain>. • _sip._udp.<domain> - not recommended for video calls, only use for audio-only calls. • _h323ls._udp.<domain> - for UDP location (RAS) signaling, such as LRQ. • _h323cs._tcp.<domain> - for H.323 call signaling. • _h323rs._udp.<domain> - for H.323 registrations.

- UDP is not a recommended transport medium for video signaling; SIP messaging for video system is too large to be reliably carried on datagram-based (rather than stream-based) transports.

- _sips._tcp is for secure SIP signaling over TCP with TLS, while _sip._tcp is for standard, non-encrypted SIP signaling over TCP.

- On internal DNS, we need to create SRV records for _sip._tcp.domain , _sips._tcp.domain that point to all Expressway peers.

1. Configure DNS

- Open DNS, under the domain Right Click then choose Other New Records and click Service Locations (SRV) .

- Fill the data for the service, protocol, Priority, Weight and the host .

- By the end, you can have both TCP and TLS SRV records configured for the two peers (as shown in this example).

2. Configure the Telepresence Endpoint

- Log in to the web GUI of your telepresence endpoint.

- Navigate to Settings > Configurations > SIP .

- Set ANAT to Off . This feature is not supported by Expressway.

- In the Proxy 1 Address, Enter the Domain Name .

- Set TlsVerify to Off and DefaultTransport to TCP (this document uses TCP).

- Set Type to Standard .

- In the URI field, enter the URI that your device uses to identify itself. This is the URI that must be dialed in order to call the device. This must be in the host@domain format, where the host part is an alphanumeric string, and the domain part is the domain previously configured on Expressway.

- Click Save .

### Option 2: Using DNS Round-Robin

- To use this option, there must be a DNS A-record available for the DNS name of the Expressway cluster that supplies a round-robin list of Expressway Peers IP addresses.

- If the endpoint does not support DNS SRV, on startup the endpoint performs a DNS A-record lookup. Configure the DNS server to support round-robin DNS, ensuring that each cluster peer member is included in the round-robin list.

- The endpoint takes the address returned by the DNS lookup and attempts to register with the relevant cluster peer. If that peer is unavailable, the endpoint performs another DNS lookup and tries to connect to the next Expressway peer provided. (The DNS server provides the IP address of the next cluster peer) This process repeats until the endpoint successfully registers with an Expressway.

- The endpoint continues to use the first Expressway it registered with for re-registrations and calls. If the connection to its Expressway is lost, the endpoint performs another DNS lookup to find a new Expressway for registration, with the DNS server providing another Expressway in the round-robin sequence.

- DNS cache timeout can be set to a fairly short time (for example, 1 minute or less) so that if a Expressway is not accessible the endpoint is quickly pointed at a different Expressway.

1. Configure DNS

- In your DNS management console, right-click the desired domain and select "New Host (A) Record".

- Enter the Expressway cluster name and the corresponding Expressway peer IP address . (In the example below, two records are created for the two cluster peers.)

2. Configure the Telepresence Endpoint

- Apply the same SIP settings as in the previous example, but set the proxy address to the cluster name .

## Verify

Option 1: Using DNS SRV Records

- The endpoint is configured with the proxy address set to the domain name, as described above.

Snippet from the endpoint logs demonstrates DNS SRV resolution and registration; the endpoint skips the first two DNS results because TLS is not configured.

```
2025-07-13T10:19:27.683+00:00 main[2467]: DnsLocator I: locatedAt() Uri 'uctest.local', profile 0, strategy 1: tls '10.48.53.127:5061' (internal) 2025-07-13T10:19:27.683+00:00 main[2467]: DnsLocator I: locatedAt() Uri 'uctest.local', profile 0, strategy 1: tls '10.48.53.128:5061' (internal) 2025-07-13T10:19:27.740+00:00 main[2467]: DnsLocator I: locatedAt() Uri 'uctest.local', profile 0, strategy 2: tcp '10.48.53.127:5060' (internal) 2025-07-13T10:19:28.349+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Registering', URI: '1001@uctest.local', Reason: '' 2025-07-13T10:19:28.439+00:00 main[2467]: SipReg I: Registered as '1001@uctest.local' to '10.48.53.127:5060' 2025-07-13T10:19:28.439+00:00 main[2467]: SipStack I: Setting 'uctest.local'/10.48.53.127:5060 as new default proxy 2025-07-13T10:19:28.440+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Registered', URI: '1001@uctest.local', Reason: ''
```

- Endpoint is registered with Peer 1 (Settings > Statuses > SIP).

- Setting Expressway Peer 1 to Maintenance mode results in the registration status showing as "failed."

- After the existing registration expired, the endpoint re-registered to the second Expressway peer.

- The snippet from the endpoint logs demonstrates DNS resolution to the second peer, followed by a failover event.

```
2025-07-13T10:25:30.840+00:00 main[2467]: SipPacket W: SIP Msg: Warning: 382 10.48.53.127 "System in Maintenance Mode" 2025-07-13T10:25:30.843+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Failed', URI: '1001@uctest.local', Reason: '503 Service Unavailable / System in Maintenance Mode' 2025-07-13T10:25:30.844+00:00 main[2467]: DnsLocator I: locatedAt() Uri 'uctest.local', profile 0, strategy 2: tcp '10.48.53.128:5060' (internal) 2025-07-13T10:25:30.855+00:00 main[2467]: SipStack I: SIP config is new and 0 active sessions; reconfiguring SIP stack 2025-07-13T10:25:30.861+00:00 main[2467]: SipStack I: SIP stack successfully configured; now ready 2025-07-13T10:25:31.096+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Registering', URI: '1001@uctest.local', Reason: '' 2025-07-13T10:25:31.180+00:00 main[2467]: SipReg I: Registered as '1001@uctest.local' to '10.48.53.128:5060' 2025-07-13T10:25:31.181+00:00 main[2467]: SipStack I: Setting 'uctest.local'/10.48.53.128:5060 as new default proxy 2025-07-13T10:25:31.181+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Registered', URI: '1001@uctest.local', Reason: '' 2025-07-13T10:25:31.182+00:00 main[2467]: SipSubscriber I: Resetting locator since reg_ind.status is registered
```

Option 2: Using DNS Round-Robin

- The endpoint is configured with the proxy address set to the Expressway cluster name, as described above.

- Snippet from Endpoint logs showing successful DNS resolution to Expressway Cluster Name and Registration to Peer 1.

```
2025-07-13T11:16:34.789+00:00 main[2467]: CuilApp[1]: Successfully changed configuration 'Configuration/SIP/Proxy[1]/Address' to 'habibexpc-cluster.uctest.local' by user=admin/web-config-app host=10.61.106.234 2025-07-13T11:16:34.990+00:00 main[2467]: SipSubscriber I: [p=0] Need to resolve 'habibexpc-cluster.uctest.local' before sending config to SIP stack (restarted locator) 2025-07-13T11:16:35.056+00:00 main[2467]: DnsLocator I: locatedAt() Uri 'habibexpc-cluster.uctest.local', profile 0, strategy 4: unspec '10.48.53.127' (internal).2025-07-13T11:16:35.058+00:00 main[2467]: SipStack I: SIP config is new and 0 active sessions; reconfiguring SIP stack 2025-07-13T11:16:35.070+00:00 main[2467]: SipStack I: SIP stack successfully configured; now ready 2025-07-13T11:16:35.372+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Registering', URI: '1001@uctest.local', Reason: '' 2025-07-13T11:16:35.461+00:00 main[2467]: SipReg I: Registered as '1001@uctest.local' to '10.48.53.127' 2025-07-13T11:16:35.461+00:00 main[2467]: SipStack I: Setting 'habibexpc-cluster.uctest.local'/10.48.53.127 as new default proxy 2025-07-13T11:16:35.462+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Registered', URI: '1001@uctest.local', Reason: ''
```

- Endpoint is registered with Peer 1 (Settings > Statuses > SIP).

- Upon shutting down Expressway Peer 1, the endpoint registered with the second Expressway peer.

- Snippet from the endpoint logs shows a successful failover

```
2025-07-13T11:20:48.897+00:00 main[2467]: SipReg W: SipTransport indicates that connection to 10.48.53.127 was lost. 2025-07-13T11:20:48.898+00:00 main[2467]: SipStack I: Failed to find new default outbound proxy at present time. 2025-07-13T11:20:48.901+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Failed', URI: '1001@uctest.local', Reason: 'Connection lost' 2025-07-13T11:20:48.907+00:00 main[2467]: SipSubscriber I: [p=0] Need to resolve 'habibexpc-cluster.uctest.local' before sending config to SIP stack (restarted locator) 2025-07-13T11:20:48.990+00:00 main[2467]: DnsLocator I: locatedAt() Uri 'habibexpc-cluster.uctest.local', profile 0, strategy 4: unspec '10.48.53.128' (internal) 2025-07-13T11:20:48.993+00:00 main[2467]: SipStack I: SIP config is new and 0 active sessions; reconfiguring SIP stack 2025-07-13T11:20:49.006+00:00 main[2467]: SipStack I: SIP stack successfully configured; now ready 2025-07-13T11:20:49.210+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Registering', URI: '1001@uctest.local', Reason: '' 2025-07-13T11:20:49.332+00:00 main[2467]: SipReg I: Registered as '1001@uctest.local' to '10.48.53.128' 2025-07-13T11:20:49.337+00:00 main[2467]: SipStack I: Setting 'habibexpc-cluster.uctest.local'/10.48.53.128 as new default proxy 2025-07-13T11:20:49.338+00:00 main[2467]: SipSubscriber I: [p=0] Registration Status: 'Registered', URI: '1001@uctest.local', Reason: '' 2025-07-13T11:20:49.339+00:00 main[2467]: SipSubscriber I: Resetting locator since reg_ind.status is registered
```

## Related Information

https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/telepresence-system-ex-series/221630-configure-telepresence-endpoint-sip-regi.html

### Revision History

1.0

29-Jul-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 29-Jul-2025 | Initial Release |