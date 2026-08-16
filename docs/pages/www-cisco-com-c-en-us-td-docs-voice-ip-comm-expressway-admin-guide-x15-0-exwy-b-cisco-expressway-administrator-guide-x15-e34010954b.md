---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x15-0-exwy-b-cisco-expressway-administrator-guide-x15-e34010954b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X15-0/exwy_b_cisco-expressway-administrator-guide-x15/exwy_m_call-types-and-licensing.html
retrieved_at: 2026-08-16T22:31:50.676390+00:00
---

Cisco Expressway Administrator Guide (X15.0)

# Cisco Expressway Administrator Guide (X15.0)

Updated: December 19, 2023

Chapter: Call Types and Licensing

## Chapter: Call Types and Licensing

# Call Types and Licensing

## Call Types

Expressway distinguishes between the following types of call:

Registered. That is, room and desktop registrations

Rich Media Sessions (RMS)

### Registered

Calls between locally registered endpoints (registered to Unified CM or Expressway) do not consume licenses, as that entitlement
                              is included within the registration. The call entitlement within the registration license includes the following scenarios:

Calls to other endpoints registered to Unified CM or Expressway within the same network, when the call is routed through a
                                    neighbor or traversal zone.

Unified CM remote sessions. These are Mobile and Remote Access (MRA) calls – video or audio calls from devices located outside
                                    the enterprise that are routed via the Expressway firewall traversal solution to endpoints registered to Unified CM.

Calls to Cisco conferencing resources (CMR, TelePresence Server/ TelePresence Conductor, or Acano servers).

These calls are still counted against the physical limit of the box.

Expressway does not support ICE candidates in the SDP of a 1xx Provisional Message

### RMS

These calls consume RMS licenses and consist of every other type of video or audio call that is routed through the Expressway.
                              RMS licenses are consumed on the exit node of the Expressway in the following scenarios:

B2B

Jabber Guest

Interworked or gatewayed calls to third-party solutions (If the third-party endpoint is not registered to Cisco infrastructure)

Expressway may take the media or just the signaling.

Audio-only SIP calls are treated distinctly from video SIP calls. Each RMS license allows either 1 video call or 2 audio only
                              SIP calls. So for example, a 100 RMS license would allow 90 video and 20 SIP audio-only simultaneous calls. Any other type
                              of audio-only call uses an RMS license.

Expressway defines an "audio-only" SIP call as one that was negotiated with a single "m=" line in the SDP. For example, if a person makes a "telephone" call but the SIP UA includes an additional m= line in the SDP, the call will use a video call license.

While an "audio-only" SIP call is being established, it is treated (licensed) as a video call. It only becomes licensed as "audio-only" when the call setup has completed. This means that if your system approaches its maximum licensed limit, you may be unable
                                                to connect some "audio-only" calls if they are made simultaneously.

The Expressway does not require RMS licenses for calls to VIMT: It does require Rich Media Session licenses for calls to and
                                                from Cloud-based CMRs. This includes SIP/ H.323 calls between the Collaboration Cloud and the CMR Hybrid solution.

The Expressway does not support midcall license optimization.

For deployments with TelePresence Conductor, license consumption is only applicable when TelePresence Conductor is deployed
                                                with a B2BUA base configuration and not in a policy server base deployment.

SIP to H.323 interworking uses an RMS license (if any of the endpoints are not registered to cisco infrastructure) on the
                                                node where interworking takes place.

WebRTC, MRA, and Cisco Webex sessions do not consume RMS licenses.

### Limitation

#### Resource Usage Call Counters Increment Incorrectly for "audio-only" Calls

Condition: Expressway should ideally keep the video counters at zero if a video call is never made.

Explanation: The call counters in the Expressway Web User Interface under Status > Overview page can increment non-intuitively under certain scenarios. Before a call connects, the counters are incremented as video
                                 calls.  After the call connects, if no video is negotiated, the video counter decrements, and "audio-only" call counter increments. It is observed on early-offer calls as well when the Expressway never sees video capabilities.

The following behaviors are observed:

If an endpoint makes an "audio-only" call through an Expressway and the far-end does not answer, the call is counted as a "Current video" call while it is ringing. Subsequently, the call is counted towards the "Peak video" calls as well.

If multiple "audio-only" calls occur simultaneously: For example, 4 endpoints joining a meeting at once, the "Current video" counter increments 4 times before the calls connect. The "Peak video" counter will permanently increase to 4 . After the calls connect, the "Current video" counter is decremented to 0 and the audio call counters are incremented correctly.

These counters increasing can lead to confusion about video calls unexpectedly traversing an Expressway pair that is only
                                 supposed to handle audio calls. The Expressway should ideally keep the video counters at zero if a video call is never made.

## Room and Desktop Registrations on Expressway

If Expressway is configured as a SIP registrar or H.323 Gatekeeper, it needs to be licensed for concurrent systems (the Unified
                              CM model) and not for concurrent calls.

For SIP deployments, you do this by adding either or both of the following license types to the Cisco Expressway-C or Cisco
                              Expressway-E:

TelePresence Room System License

Desktop System License

The following SIP devices register as desktop systems; all other devices are considered room systems:

Cisco TelePresence EX60

Cisco TelePresence EX90

Cisco Webex DX70

Cisco Webex DX80

If you use Cisco Jabber Video for TelePresence (Movi) soft clients (now end-of-sale), they also register to Expressway as
                                    desktop systems.

To register as desktop systems (for SIP), DX systems must be running version CE8.2 or later, and EX systems must be running
                                          TC7.3.6 or later. DX and EX systems running earlier versions still register for SIP, but will consume a room system license.

For H.323 deployments, all endpoints consume a TelePresence Room System License. This is due to a limitation in H.323, which
                              does not determine the difference between desktop and room type endpoints. We therefore recommend SIP as the preferred signaling
                              protocol, although H.323 is available as a fall back for endpoints that do not support SIP.

### Licensing considerations when Expressway is the SIP registrar / H.323 Gatekeeper

Option keys containing licenses for local registrations are installed on the Cisco Expressway-C and/or the Cisco Expressway-E
                                    depending on where the endpoints are registered. These licenses are pooled in a cluster, which means that Expressway peers
                                    can use each others' licenses. However, rooms cannot use desktop licenses, and desktop systems cannot use room licenses.

Registrations from outside the network are proxied to Expressway-C by the Expressway-E. The same domain cannot also be used
                                    for direct Expressway-E registrations.

If you have existing licenses on the Expressway-C and want to register some or all of your existing licensed endpoints to
                                    the Expressway-E, manually delete the relevant licenses from the Expressway-C and reload them on the Expressway-E.

The Large VM and the CE1200 and CE1100 appliances can support up to 5000 registrations, subject to the appropriate licensing.
                                    For MRA registrations (proxied to CUCM) the limits are 5000 for the CE1200, and 2500 for the Large VM and the CE1100. Local
                                    registrations, proxy registrations (via Expressway-E) and MRA registrations all count towards the registration limit.

Proxy registration is possible with SIP endpoints only and does not apply to H.323 endpoints.

FindMe device provisioning is supported with Cisco TMSPE (although this support is deprecated from Expressway version X12.5).

### Licensing considerations if device registers as both SIP and H.323

Be aware that multiple licenses are consumed if the same device registers to Expressway both as SIP and as H.323. For example,
                              say a DX80 is registered on Expressway-C as a SIP user agent, and also as an H.323 endpoint (with the same or different URL/DN).
                              A Desktop System License will be consumed for the SIP registration, and a TelePresence Room System License will be consumed
                              for the H.323 endpoint registration. The same dual license usage would apply, for example, if a Cisco Webex Room similarly
                              registers for both SIP and H.323.

### RMS license usage

The licensing model reduces the usage of Rich Media Session (RMS) licenses in the following scenarios:

If you have already paid for a registration license, RMS licenses are not used for the following call types:

Calls between registered systems. Here, "registered systems" means systems registered directly to the Expressway, by proxy to the Expressway-C through the Expressway-E, or by proxy through
                                          the Expressway pair (MRA) to neighbored Unified CMs.

Calls from registered systems (as above) to Cisco infrastructure. Currently, this extends only to Cisco Meeting Server, and
                                          to CiscoTelePresence Server and TelePresence MCUs that are managed by TelePresence Conductor. However, calls from MCUs that
                                          are not managed by Conductor do use RMS licenses.

Calls from registered systems (as above) to Cisco Collaboration Cloud.

Calls from registered systems to all other systems use one RMS license. Including, but not limited to, the following call
                                    types:

Business to business calls. Require one RMS license on Expressway-E.

Business to consumer calls (Jabber Guest). Require one RMS license on the Expressway-E.

Interoperability gateway calls, including Microsoft Lync / Skype for Business and third-party call control servers require
                                          one RMS license on the Expressway-C.

### Limitation

#### Proxy Registration Resulting in Incorrect Registration License Consumption On Expressway C Cluster

Proxy registrations may consume duplicate registration licenses on a cluster Expressway C deployment. This results in proxy
                                 registering on more than one Expressway C at the same time (refresh register proxy to different Expressway C than active registered
                                 Expressway C).

This is due to the Expressway C cluster nodes not sharing awareness of existing registrations for the same Call-ID.

Duplicate registration status (and consumption of duplicate registration license) will clear out once registration TTL expires.

## License Usage for Device Registrations

Devices that are directly registered on Expressway (Cisco Expressway-C or Cisco Expressway-E) consume licenses as follows:

SIP. Cisco TelePresence EX60, Cisco TelePresence EX90, Cisco DX70, and Cisco DX80 endpoints consume a desktop license. Other
                                 SIP endpoints consume a room system license.

H.323. Each registered H.323 endpoint consumes a room system license.

SIP proxy registrations on the Cisco Expressway-C consume the same licenses as for direct SIP registrations. SIP proxy registrations
                           on the Cisco Expressway-E do not consume licenses.

Registrations are counted per alias , not per device (IP address). So a registration request with multiple aliases, like an MCU, consumes multiple room licenses
                                       even if only a single device is registered on Expressway.

## RMS License Consumption Table

This table lists the scenarios in which Expressway consumes RMS licenses. References to "Third-party Gatekeeper" mean the gatekeeper is connected to Expressway-C; references to "External" mean the gatekeeper is connected to Expressway-E.

Calling endpoint registered to ...

Called endpoint registered to...

Expressway-C

Expressway-E

Unified CM

Expressway-C (Lync)

1 Expressway-C (Lync Gateway)

0

Unified CM

External

0

1

Unified CM

Third-party Gatekeeper

1

0

Expressway-C

External

0

1

Expressway-C (Remote [SIP] - proxy)

External

0

1

Expressway-C (SIP)

Third-party Gatekeeper

1

0

Expressway-C (H323)

Third-party Gatekeeper

1

0

Expressway-C (Remote [SIP]) - proxy

Third-party Gatekeeper

1

0

Expressway-C

Expressway-C (Lync)

0

1 Expressway-C (Lync Gateway)

Expressway-C (Remote)

Expressway-C (Lync)

0

1 Expressway-C (Lync Gateway)

Expressway-C (SIP)

Third-party SIP server

1

0

Expressway-C (H323)

Third-party SIP server

1

0

Expressway-E (SIP)

External

-

1

Expressway-E (H.323)

External

-

1

## License Bypass for Calls to Collaboration Meeting Rooms (CMRs)

The Expressway no longer requires rich media session licenses for calls to and from cloud-based CMRs. This includes SIP/ H.323
                              calls between Collaboration Cloud and the CMR Hybrid solution.

This only applies when the dialed string does not need transformation on the Expressway (for example, user@sitename.webex.com).

Although untransformed SIP calls to cloud-based CMRs do not use licenses, they do use resources and may not progress if the
                              Expressway is at full capacity.

There is no license bypass for CMR Premises calls. H.323 calls to cloud-based CMRs consume CMR licenses but not RMS licenses.

## License Usage for Cisco Video Integration (CVI) Calls

Cisco Video Integration (CVI) on Expressway does not require any licenses. It will raise an alarm that licenses have expired,
                              but functionality will remain intact.

## Intracluster Calls

License usage when endpoints are registered to different peers in the same cluster, depends on call media traversal across
                              the cluster:

If call media does not traverse the cluster peers, a call between the endpoints does not use any RMS licenses (it's a "Registered" call).

If any of the endpoint is not registered to Cisco infrastructure then calls will use RMS license.

If call media does traverse the cluster peers, a call between the endpoints uses an RMS license on the Expressway where the
                                    B2BUA is engaged.

If both the endpoints are registered to Cisco infrastructure then call will not use RMS license.

### Usage Limits

Usage limits have two aspects: physical capacity and licensing. The physical constraints of the Expressway cluster determine
                                 the ultimate limits, and within that the capacity available to the system is determined by its licensing.

#### Physical capacity limits

The maximum number of licenses that each Expressway peer can actually use depends on the physical capacity of the appliance
                                 or VM. For example, the maximum capacity supported by a large Expressway VM is 500 concurrent video calls.

Capacity alarms are raised if either of the following usage thresholds are reached:

Number of concurrent calls reaches 90% of the capacity of the cluster.

Number of concurrent calls on any one unit reaches 90% of the physical capacity of the unit.

#### License limits

The licensed capacity of a cluster will depend on whether the system uses classic PAK-based licensing, or smart licensing.
                                 For PAK-based, for example, if two large VMs are clustered and each has 300 RMS licenses installed, the effective capacity
                                 of the cluster is 600 concurrent video calls. If one peer is removed from the cluster, the remaining peer retains all 600
                                 RMS licenses for 14 days, but only supports up to 500 concurrent video calls.

For smart licensed systems, the licensed capacity depends on the license pool that's assigned to your organization's registered
                                 account with the Cisco Smart Software Manager.

## Limitations

### Licensing Behavior with Chained Expressway-Es

If you chain Expressway-Es to traverse firewalls (from X8.10), be aware of this licensing behavior:

If you connect through the firewall to the Cisco Webex cloud, each of the additional Expressway-Es which configure a traversal zone with the traversal client role, will consume a Rich Media Session license
                                    (per call). As before, the original Expressway-C and Expressway-E pair do not consume a license.

If you connect through the firewall to a third-party organization (Business to Business call), all of the Expressway-Es in the chain, including the original one in the traversal pair, will consume a Rich Media Session license
                                    (per call). As before, the original Expressway-C does not consume a license.

### Option Keys Only Take Effect for 65 Keys or Fewer

If you try to add more than 65 option keys (licenses), they appear as normal in the  web interface ( Maintenance > Option keys ). However, only the first 65 keys take effect. Additional keys from 66 onwards appear to be added, but actually the  does
                              not process them. Bug ID CSCvf78728 refers.

| Note | These calls are still counted against the physical limit of the box. Expressway does not support ICE candidates in the SDP of a 1xx Provisional Message |
|---|---|

| Note | Expressway defines an "audio-only" SIP call as one that was negotiated with a single "m=" line in the SDP. For example, if a person makes a "telephone" call but the SIP UA includes an additional m= line in the SDP, the call will use a video call license. While an "audio-only" SIP call is being established, it is treated (licensed) as a video call. It only becomes licensed as "audio-only" when the call setup has completed. This means that if your system approaches its maximum licensed limit, you may be unable
                                                to connect some "audio-only" calls if they are made simultaneously. The Expressway does not require RMS licenses for calls to VIMT: It does require Rich Media Session licenses for calls to and
                                                from Cloud-based CMRs. This includes SIP/ H.323 calls between the Collaboration Cloud and the CMR Hybrid solution. The Expressway does not support midcall license optimization. For deployments with TelePresence Conductor, license consumption is only applicable when TelePresence Conductor is deployed
                                                with a B2BUA base configuration and not in a policy server base deployment. SIP to H.323 interworking uses an RMS license (if any of the endpoints are not registered to cisco infrastructure) on the
                                                node where interworking takes place. WebRTC, MRA, and Cisco Webex sessions do not consume RMS licenses. |
|---|---|

| Note | To register as desktop systems (for SIP), DX systems must be running version CE8.2 or later, and EX systems must be running
                                          TC7.3.6 or later. DX and EX systems running earlier versions still register for SIP, but will consume a room system license. |
|---|---|

| Note | Registrations are counted per alias , not per device (IP address). So a registration request with multiple aliases, like an MCU, consumes multiple room licenses
                                       even if only a single device is registered on Expressway. |
|---|---|

| Calling endpoint registered to ... | Called endpoint registered to... | Expressway-C | Expressway-E |
|---|---|---|---|
| Unified CM | Expressway-C (Lync) | 1 Expressway-C (Lync Gateway) | 0 |
| Unified CM | External | 0 | 1 |
| Unified CM | Third-party Gatekeeper | 1 | 0 |
| Expressway-C | External | 0 | 1 |
| Expressway-C (Remote [SIP] - proxy) | External | 0 | 1 |
| Expressway-C (SIP) | Third-party Gatekeeper | 1 | 0 |
| Expressway-C (H323) | Third-party Gatekeeper | 1 | 0 |
| Expressway-C (Remote [SIP]) - proxy | Third-party Gatekeeper | 1 | 0 |
| Expressway-C | Expressway-C (Lync) | 0 | 1 Expressway-C (Lync Gateway) |
| Expressway-C (Remote) | Expressway-C (Lync) | 0 | 1 Expressway-C (Lync Gateway) |
| Expressway-C (SIP) | Third-party SIP server | 1 | 0 |
| Expressway-C (H323) | Third-party SIP server | 1 | 0 |
| Expressway-E (SIP) | External | - | 1 |
| Expressway-E (H.323) | External | - | 1 |

| Note | This only applies when the dialed string does not need transformation on the Expressway (for example, user@sitename.webex.com). |
|---|---|