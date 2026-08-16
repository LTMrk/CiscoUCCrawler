---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x15-4-exwy-b-cisco-expressway-administrator-guide-x15-6e833b918e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X15-4/exwy_b_cisco-expressway-administrator-guide-x154/exwy_m_expressway-capacity-and-sizing.html
retrieved_at: 2026-08-16T22:26:03.196062+00:00
---

Cisco Expressway Administrator Guide (X15.4)

# Cisco Expressway Administrator Guide (X15.4)

Updated: February 9, 2026

Chapter: Expressway Capacity and Sizing

## Chapter: Expressway Capacity and Sizing

# Expressway Capacity and Sizing

## Overview

The maximum supported capacities / sizing for Cisco Expressway Series (not Cisco VCS) are listed in the tables below. These
                              figures/values are guidelines only and are NOT guaranteed, because many factors affect performance in real-life deployments.
                              Expressway supports so many different use cases that it is not possible to provide capacity limits for individual, specific
                              deployments.

Expressway sizing / capacity information is categorized on the basis of the number of supported concurrent registrations and/or
                              calls.

## Important Caveats

The figures/values provided here assume all necessary software licenses are applied.

The figures/values are tested for specific, dedicated Expressway scenarios. Based on an Expressway or cluster being used for
                                    a single service or scenario, such as just for MRA or just for B2B calling. It is not possible to provide tested capacity
                                    guidelines for multi-service deployments.

N+1 Model

Prior to the X14.2 release, up to 6 Expressway systems can be clustered to yield a total cluster capacity of four times that of a single system (except for Small VMs, which have no gain).

From the X14.2 release, in the 4+1 redundancy model, up to 5 Expressway systems can be clustered to yield a total cluster
                                          capacity of four times that of a single system (with 1 redundancy server) (except for Small VMs, which have no gain).

From the X14.2 release, in the 5+1 redundancy model, up to 6 Expressway systems can be clustered to yield a total cluster
                                          capacity of five times that of a single system (with 1 redundancy server) (except for Small VMs, which have no gain).

For Small VMs, clustering is only for redundancy and not for scale and there is no capacity gain from clustering .

The figures/values provided for video calls and audio-only calls are alternatives - the stated capacity is available either
                                    for video or for audio, not for both.

## Dependencies

The figures/values for calls refer to concurrent calls.

Concurrent calls and Rich Media Session (RMS) licenses do not have a one-to-one relationship. Various factors determine RMS
                              license usage, which means that some calls may be "free" and others may use multiple licenses.

To support 6000 TURN relays on a large system (Large VM or CE1200) you need to enable "TURN Port Multiplexing on Large Expressway" ( Configuration > Traversal > TURN ).

Small VMs are supported on the Cisco Business Edition 6000 platform, or on general purpose hardware / ESXi which matches the
                              Cisco Business Edition 6000 specification. The figures/values for Small VMs are for M5-based BE6000 appliances.

## Capacity Guidelines for Standalone Systems

The table lists the base capacity for a standalone Expressway.

Expressway Select can exceed 2500 encrypted signaling sessions. There is no encrypted session limit/capping on the number
                                                of registrations/calls/sessions (hardware limit still applies).

Values with PRRH = OFF.

X15.x

Platform

Native Registrations (room/desktop)

Calls (Video or Audio-only)

RMS Licenses

MRA Registrations (proxied)

TURN Relays

CE1200

5000

500 video or 1000 audio

500

7000

6000

CE1300

5000

500 video or 1000 audio

500

8500

6000

Large VM

5000

500 video or 1000 audio

500

3500

6000

Medium VM

2500

150 video or 300 audio

150

2500

1800

Small VM

2000

20 video or 40 audio (40 non-MRA video)

75

200

1800

## Capacity Guidelines for Clustered Systems

To determine the capacity for cluster of size n+1 , 1 node will be counted towards redundancy and the cluster capacity will be a factor of n x single node capacity in table Standalone Capacity Guidelines .

The maximum cluster size supported is 6.

For Small VMs, where the figures/values for clustered systems and for standalone systems are always the same (because there's
                                          no capacity gain from clustering Small VMs).

## Fast Path Registration for MRA (Caching Optimization for Registrations)

From X12.7, Expressway supports Fast Path Registration for MRA-based devices. This optimizes routing processes, reducing the
                              server workload, so leading to increased capacities. Expressway caches the initial routing calculation and then uses a Pre-Routed
                              Route Header to forward subsequent packets to the destination using the cached routing result. This has the following benefits:

Reduces the routing workload.

Increases registration capacity.

Ensures that each media packet follows the same route path.

Important

This feature only applies to MRA deployments. The increased capacity and other benefits do not apply to non-MRA Expressway
                                          deployments.

Fast Path Registration is supported for the following SIP methods: REGISTER. Configuration is through the command line interface,
                              and detailed instructions are provided in the latest Expressway MRA Deployment Guide .

Remember

Make sure you restart Expressway.

The tested results for a standalone Expressway MRA deployment (Expressway-C + Expressway-E) when this feature is configured
                              are:

Expressway Select can exceed 2500 encrypted signaling sessions. There is no encrypted session limit/capping on the number
                                                of registrations/calls/sessions (hardware limit still applies).

Values with PRRH = ON.

You can only enable PreRoutedRouteHeader (PRRH) on the Expressway Select image. In the Expressway image, PRRH is disabled, and the Command Line
                                                Interface (CLI) option is unavailable.

X14.x

Platform

Calls (Video or Audio-only)

RMS Licenses

MRA Registrations (proxied)

CE1200

500 video or 1000 audio

500

7500

Large VM

500 video or 1000 audio

500

4000

Medium VM

150 video or 300 audio

150

3000

Small VM

20 video or 40 audio (40 non-MRA video)

75

200

To determine the capacity for cluster of size n+1 , 1 node will be counted towards redundancy and the cluster capacity will be a factor of n x single node capacity in table Standalone Capacity Guidelines ..

The maximum cluster size supported is 6.

For Small VMs, where the figures/values for clustered systems and for standalone systems are always the same (because there's
                                          no capacity gain from clustering Small VMs).

## Intracluster Calls

License usage when endpoints are registered to different peers in the same cluster, depends on call media traversal across
                              the cluster:

If call media does not traverse the cluster peers, a call between the endpoints does not use any RMS licenses (it's a "Registered" call).

If any of the endpoint is not registered to Cisco infrastructure then calls will use RMS license.

If call media does traverse the cluster peers, a call between the endpoints uses an RMS license on the Expressway where the
                                    B2BUA is engaged.

If both the endpoints are registered to Cisco infrastructure then call will not use RMS license.

More information about how licenses are used in clustered systems is provided in the licensing section of this guide.

| Note | Expressway Select can exceed 2500 encrypted signaling sessions. There is no encrypted session limit/capping on the number
                                                of registrations/calls/sessions (hardware limit still applies). Values with PRRH = OFF. |
|---|---|

| X15.x |
|---|
| Platform | Native Registrations (room/desktop) | Calls (Video or Audio-only) | RMS Licenses | MRA Registrations (proxied) | TURN Relays |
| CE1200 | 5000 | 500 video or 1000 audio | 500 | 7000 | 6000 |
| CE1300 | 5000 | 500 video or 1000 audio | 500 | 8500 | 6000 |
| Large VM | 5000 | 500 video or 1000 audio | 500 | 3500 | 6000 |
| Medium VM | 2500 | 150 video or 300 audio | 150 | 2500 | 1800 |
| Small VM | 2000 | 20 video or 40 audio (40 non-MRA video) | 75 | 200 | 1800 |

| Note | For Small VMs, where the figures/values for clustered systems and for standalone systems are always the same (because there's
                                          no capacity gain from clustering Small VMs). |
|---|---|

| Important | This feature only applies to MRA deployments. The increased capacity and other benefits do not apply to non-MRA Expressway
                                          deployments. |
|---|---|

| Remember | Make sure you restart Expressway. |
|---|---|

| Note | Expressway Select can exceed 2500 encrypted signaling sessions. There is no encrypted session limit/capping on the number
                                                of registrations/calls/sessions (hardware limit still applies). Values with PRRH = ON. You can only enable PreRoutedRouteHeader (PRRH) on the Expressway Select image. In the Expressway image, PRRH is disabled, and the Command Line
                                                Interface (CLI) option is unavailable. |
|---|---|

| X14.x |
|---|
| Platform | Calls (Video or Audio-only) | RMS Licenses | MRA Registrations (proxied) |
| CE1200 | 500 video or 1000 audio | 500 | 7500 |
| Large VM | 500 video or 1000 audio | 500 | 4000 |
| Medium VM | 150 video or 300 audio | 150 | 3000 |
| Small VM | 20 video or 40 audio (40 non-MRA video) | 75 | 200 |

| Note | For Small VMs, where the figures/values for clustered systems and for standalone systems are always the same (because there's
                                          no capacity gain from clustering Small VMs). |
|---|---|