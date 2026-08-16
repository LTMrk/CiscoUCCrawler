---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x14-2-exwy-b-cisco-expressway-administrator-guide-x14-1458bda989
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-2/exwy_b_cisco-expressway-administrator-guide-x142/exwy_m_expressway-capacity-and-sizing-x142.html
retrieved_at: 2026-08-16T22:37:39.020885+00:00
---

Cisco Expressway Administrator Guide (X14.2)

# Cisco Expressway Administrator Guide (X14.2)

Updated: August 11, 2022

Chapter: Expressway Capacity and Sizing X142

## Chapter: Expressway Capacity and Sizing X142

# Expressway Capacity and Sizing X142

## Overview

The maximum supported capacities / sizing for Cisco Expressway Series (not Cisco VCS) are listed in the tables below. These
                              figures are guidelines only and are NOT guaranteed, because many factors affect performance in real-life deployments. Expressway
                              supports so many different use cases that it is not possible to provide capacity limits for individual, specific deployments.

Expressway sizing / capacity information is categorized on the basis of the number of supported concurrent registrations and/or
                              calls.

## Important Caveats

The figures provided here assume all necessary software licenses are applied.

The figures are tested for specific, dedicated Expressway scenarios. Based on an Expressway or cluster being used for a single
                                    service or scenario, such as just for MRA or just for B2B calling. It's not possible to provide tested capacity guidelines
                                    for multi-service deployments.

Up to six Expressway systems can be clustered, but this only increases capacity by a maximum factor of four (except for Small VMs, which have no gain).

From the X14.2 release, in the 4+1 redundancy model, up to 4 Expressway systems can be clustered (1 redundancy server), but
                                    this only increases capacity by a maximum factor of four (except for Small VMs, which have no gain).

From the X14.2 release, in the 5+1 redundancy model, up to 5 Expressway systems can be clustered (1 redundancy server), but
                                    this only increases capacity by a maximum factor of five (except for Small VMs, which have no gain).

For Small VMs, clustering is only for redundancy and not for scale and there is no capacity gain from clustering .

The figures provided for video calls and audio-only calls are alternatives - the stated capacity is available either for video
                                    or for audio, not for both.

## Dependencies

The figures for calls refer to concurrent calls.

Concurrent calls and Rich Media Session (RMS) licenses do not have a one-to-one relationship. Various factors determine RMS
                              license usage, which means that some calls may be "free" and others may use multiple licenses.

To support 6000 TURN relays on a large system (Large VM or CE1200) you need to enable "TURN Port Multiplexing on Large Expressway" ( Configuration > Traversal > TURN ).

Small VMs are supported on the Cisco Business Edition 6000 platform, or on general purpose hardware / ESXi which matches the
                              Cisco Business Edition 6000 specification. The figures for Small VMs are for M5-based BE6000 appliances.

## Capacity Guidelines for Standalone Systems

The table lists the base capacity for a standalone Expressway.

Platform

Registrations (room/desktop)

Calls (video or audio-only)

RMS Licenses

MRA Registrations (proxied)

TURN Relays

CE1200

5000

500 video or 1000 audio

500

7000

6000

Large VM

5000

500 video or 1000 audio

500

3500

6000

Medium VM

2500

100 video or 200 audio

100

3000

1800

Small VM

2000

40 non-MRA video, or 20 MRA video or 40 audio

75

200

1800

## Capacity Guidelines for Clustered Systems

This table illustrates the increased capacity for a clustered system with four Expressways (the maximum cluster size for scale
                              gain).

To determine the capacity for clusters with two or three nodes, apply a factor of 2 or 3 respectively to the standalone figures.
                              Except for Small VMs, where the figures for clustered systems and for standalone systems are always the same (because there's
                              no capacity gain from clustering Small VMs).

The table lists the increased capacity for a clustered system with six Expressways (the maximum cluster size for scale gain). Each cluster can have up to six Expressway nodes and a maximum of N+2 physical redundancy. All nodes are active in the cluster.

Platform

Registrations (room/desktop)

Calls (video or audio-only)

RMS Licenses

MRA Registrations (proxied)

TURN Relays

CE1200

20,000

2000 video or 4000 audio

2000

20,000

24,000

Large VM

20,000

2000 video or 4000 audio

2000

10,000

24,000

Medium VM

10,000

400 video or 800 audio

400

10,000

7200

Small VM

2000

40 non-MRA video, or 20 MRA video or 40 audio

75

200

1800

## Fast Path Registration for MRA (Caching Optimization for Registrations)

From X12.7, Expressway supports Fast Path Registration for MRA-based devices. This optimizes routing processes, reducing the
                              server workload, so leading to increased capacities. Expressway caches the initial routing calculation and then uses a Pre-Routed
                              Route Header to forward subsequent packets to the destination using the cached routing result. This has the following benefits:

Reduces the routing workload.

Increases registration capacity.

Ensures that each media packet follows the same route path.

This feature only applies to MRA deployments. The increased capacity and other benefits do not apply to non-MRA Expressway
                                          deployments.

Fast Path Registration is supported for the following SIP methods: REGISTER. Configuration is through the command line interface,
                              and detailed instructions are provided in the latest Expressway MRA Deployment Guide .

The tested results for a standalone Expressway MRA deployment (Expressway-C + Expressway-E) when this feature is configured
                              are:

Platform

MRA Registrations

MRA Video Calls

MRA Audio Calls

CE 1200

7000

500

1000

Large OVA

3500

500

1000

Medium OVA

3000

150

300

Small OVA

2500

100

200

Small OVA BE6K

2500

100

200

## Example Deployment

Say you want to deploy a resilient cluster that can handle up to 750 concurrent desktop registrations and 250 Rich Media Sessions.
                              In this case you could configure 4 peers as follows:

Peer 1

Peer 2

Peer 3

Peer 4

Total cluster capacity

Desktop registration licenses

250

250

250

0

750

Rich Media Sessions

100

100

50

0

250

In this example it doesn't matter which peer an endpoint registers to, as the licenses are shared across all of the peers.
                              If any one peer is temporarily taken out of service the full set of call licenses remain available to the entire cluster.

## Intracluster Calls

License usage when endpoints are registered to different peers in the same cluster, depends on call media traversal across
                              the cluster:

If call media does not traverse the cluster peers, a call between the endpoints does not use any RMS licenses (it's a "Registered" call).

If any of the endpoint is not registered to Cisco infrastructure then calls will use RMS license.

If call media does traverse the cluster peers, a call between the endpoints uses an RMS license on the Expressway where the
                                    B2BUA is engaged.

If both the endpoints are registered to Cisco infrastructure then call will not use RMS license.

More information about how licenses are used in clustered systems is provided in the licensing section of this guide.

| Platform | Registrations (room/desktop) | Calls (video or audio-only) | RMS Licenses | MRA Registrations (proxied) | TURN Relays |
|---|---|---|---|---|---|
| CE1200 | 5000 | 500 video or 1000 audio | 500 | 7000 | 6000 |
| Large VM | 5000 | 500 video or 1000 audio | 500 | 3500 | 6000 |
| Medium VM | 2500 | 100 video or 200 audio | 100 | 3000 | 1800 |
| Small VM | 2000 | 40 non-MRA video, or 20 MRA video or 40 audio | 75 | 200 | 1800 |

| Platform | Registrations (room/desktop) | Calls (video or audio-only) | RMS Licenses | MRA Registrations (proxied) | TURN Relays |
|---|---|---|---|---|---|
| CE1200 | 20,000 | 2000 video or 4000 audio | 2000 | 20,000 | 24,000 |
| Large VM | 20,000 | 2000 video or 4000 audio | 2000 | 10,000 | 24,000 |
| Medium VM | 10,000 | 400 video or 800 audio | 400 | 10,000 | 7200 |
| Small VM | 2000 | 40 non-MRA video, or 20 MRA video or 40 audio | 75 | 200 | 1800 |

| Important | This feature only applies to MRA deployments. The increased capacity and other benefits do not apply to non-MRA Expressway
                                          deployments. |
|---|---|

| Platform | MRA Registrations | MRA Video Calls | MRA Audio Calls |
|---|---|---|---|
| CE 1200 | 7000 | 500 | 1000 |
| Large OVA | 3500 | 500 | 1000 |
| Medium OVA | 3000 | 150 | 300 |
| Small OVA | 2500 | 100 | 200 |
| Small OVA BE6K | 2500 | 100 | 200 |

|  | Peer 1 | Peer 2 | Peer 3 | Peer 4 | Total cluster capacity |
|---|---|---|---|---|---|
| Desktop registration licenses | 250 | 250 | 250 | 0 | 750 |
| Rich Media Sessions | 100 | 100 | 50 | 0 | 250 |