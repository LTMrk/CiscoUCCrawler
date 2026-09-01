---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-end-to-end-planning-chcs-b-hcs-125-e2e-planning-chcs-b-4b1b70b70a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/End_to_End_Planning/chcs_b_hcs-125-e2e-planning/chcs_b_hcs-125-e2e-planning_chapter_01011.html
retrieved_at: 2026-09-01T20:57:12.283324+00:00
---

Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

# Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

Updated: June 25, 2019

Chapter: Video

## Chapter: Video

# Video

## Prerequisites

Before you plan the video deployment, make sure that you review the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

Complete the actions
                           		outlined in previous sections of this guide including:

- Initial system requirements
                              		  and planned growth

- Data center requirements

- Licensing

- Customer premise equipment

- Service fulfillment

- Service assurance

## Video Workflow

## Plan the Video
                        	 Network

Cisco Hosted Collaboration Solution supports dedicated deployment of Video Conferencing on a per tenant basis using TMS, Conductor, and Telepresence Servers
                                       (virtual and Physical). Determine whether you intend to offer dedicated TP services along with Centralized TP services using
                                       CTX.

Plan the
                                       			 capacity requirements for dedicated and shared deployment.

Determine the
                                       			 inter-enterprise and intra-enterprise networking requirements for video
                                       			 dialing.

- Determine if you want to
                                          				allow video calls between enterprises. To allow outside video calls, set up
                                          				your video network and set up the SBCs to allow users to place calls outside of
                                          				the enterprise.

- Decide if you want to do
                                          				the inter-enterprise routing within the SBC or in the service provider's
                                          				softswitch.

- Consider policies on
                                          				selectively enabling inter-enterprise video dialing.

- Investigate and understand
                                          				the limitations of Lawful Intercept (LI) for inter-enterprise video dialing and
                                          				the LI exemption for video dialing.

Determine if
                                       			 you will use scheduled conferencing or virtual meeting rooms.

Cisco offers
                                          				virtual meeting rooms only for Cisco HCS. Scheduled meetings with Cisco HCS are
                                          				done through a third-party portal. This portal is supported, but is not
                                          				validated.

Scheduled
                                          				Conferencing, Rendezvous Conferencing, and Adhoc Video Conferencing are
                                          				supported when there are dedicated deployments of Conductor, TMS, and
                                          				TelePresence servers. For CTX-based Video deployment, Scheduled Video
                                          				Conferencing is not natively supported in HCS. However, with the use of a
                                          				third-party portal with CTX, Scheduled Conferencing can be supported.

If you are
                                          				planning for a third-party portal, evaluate the third-party portal and validate
                                          				it against your requirements.

Determine your
                                       			 port capacity for video conferencing based on the following estimations. These
                                       			 estimates provide you with an estimate of the number of users that are expected
                                       			 to take part in a video conference at any time. Base these considerations on
                                       			 whether a centralized or dedicated video conferencing solution is being
                                       			 planned.

- Number of customers using
                                          				video conferencing.

- Number of video endpoints
                                          				each customer will use.

- Number of simultaneous
                                          				video conferences that you expect.

- The average number of
                                          				participants in each video conference.

- Average duration of video
                                          				conference.

- Number of ports needed.
                                          				This is the (number of video-enabled customers) x (number of simultaneous video
                                          				meetings per customer) x (number of participants per meeting) x (average number
                                          				of ports per participant).

- For example: (10
                                          				customers) x (2 simultaneous meetings per customer) x (6 participants per
                                          				meeting) x (1 port per participant) = 120 ports.

The average
                                          				number of ports per participant must take into account the distribution of
                                          				different types of endpoints (number of screens), the quality of the video (HD,
                                          				SD, Audio only), and presentation sharing. Each port is assumed to provide a
                                          				1080p HD quality video.

Determine
                                       			 the type of video endpoints supported in the network.

- Immersive video
                                          				endpoints.

- Nonimmersive video
                                          				endpoints.

Immersive
                                          				video endpoints enable the best possible in-person TelePresence video
                                          				collaboration experience, where attendees across multiple locations feel as
                                          				though they are in the same room. Due to the high quality of the video media,
                                          				immersive video endpoints consume higher amounts of bandwidth and network
                                          				resources than nonimmersive video endpoints.

Determine
                                       			 whether to provide video dialing between different service providers.

- To provide video dialing
                                          				between different service providers, set up the SBC to provide connectivity
                                          				between the different service providers.

- Make sure that agreements
                                          				and routing policies are in place for interprovider video dialing.

Determine
                                       			 whether you want to support over-the-top (OTT) connectivity for guest clients
                                       			 from other enterprises and integrate Microsoft Lync along with Dedicated Video
                                       			 Conferencing with Conductor/TMS/Virtual TS.

You can use
                                          				Cisco Expressway to set up connectivity.

Determine if
                                       			 you need to transcode codecs within your video network.

- If yes, you need to
                                          				implement the Cisco TelePresence MSE 8710 server for transcoding.

- If no, you can use
                                          				Multipoint Switch (CTMS). CTMS is a less expensive option than the MSE, but
                                          				DTLS is not supported with CTMS. Any CTX-based calls are unsecure if you choose
                                          				CTMS.

Determine
                                       			 your bandwidth and QoS requirements for video, using the following information:

- Number of ports

- Number of endpoints

- Types of endpoints.

- For every (shared)
                                          				three-screen TelePresence room at 1080p, add 16.7 Mbps (assumes 100-percent
                                          				utilization because these are shared services).

- For every single-screen
                                          				TelePresence at 1080p, add 4.5 Mbps (assumes 100-percent utilization).

- For every single-screen
                                          				TelePresence at 720p, add 1.68 Mbps (assumes 100-percent utilization).

- For shared EX90 at 720p,
                                          				add 1.5 Mbps (assumes 100-percent utilization).

- For personal (nonshared)
                                          				EX90 at 720p, add 136 Kbps (assumes much lower utilization).

Determine your
                                       			 security requirements for signaling and media.

- TLS for signaling
                                          				encryption.

- DTLS for media encryption.

- SRTP media encryption.

Determine the
                                       			 CTX model to use.

- Starter Package—If you
                                          				choose the Starter Package, there is a maximum of 250 ports with no active
                                          				meeting management license. Active video calls are not preserved. ACE is not
                                          				required with the Starter Package.

- Classic Package—If you
                                          				choose the Classic Package, ACE is implemented.

Consider the
                                       			 following when determining networking requirements:

- Data Center Network for
                                          				video infrastructure.

- VLANs.

- Virtual routing and
                                          				forwarding (VRF).

- TPaas network devices and
                                          				applications which are deployed in a shared environment.

|  |
|---|

| Step 1 | Cisco Hosted Collaboration Solution supports dedicated deployment of Video Conferencing on a per tenant basis using TMS, Conductor, and Telepresence Servers
                                       (virtual and Physical). Determine whether you intend to offer dedicated TP services along with Centralized TP services using
                                       CTX. |
|---|---|
| Step 2 | Plan the
                                       			 capacity requirements for dedicated and shared deployment. |
| Step 3 | Determine the
                                       			 inter-enterprise and intra-enterprise networking requirements for video
                                       			 dialing. Determine if you want to
                                          				allow video calls between enterprises. To allow outside video calls, set up
                                          				your video network and set up the SBCs to allow users to place calls outside of
                                          				the enterprise. Decide if you want to do
                                          				the inter-enterprise routing within the SBC or in the service provider's
                                          				softswitch. Consider policies on
                                          				selectively enabling inter-enterprise video dialing. Investigate and understand
                                          				the limitations of Lawful Intercept (LI) for inter-enterprise video dialing and
                                          				the LI exemption for video dialing. |
| Step 4 | Determine if
                                       			 you will use scheduled conferencing or virtual meeting rooms. Cisco offers
                                          				virtual meeting rooms only for Cisco HCS. Scheduled meetings with Cisco HCS are
                                          				done through a third-party portal. This portal is supported, but is not
                                          				validated. Scheduled
                                          				Conferencing, Rendezvous Conferencing, and Adhoc Video Conferencing are
                                          				supported when there are dedicated deployments of Conductor, TMS, and
                                          				TelePresence servers. For CTX-based Video deployment, Scheduled Video
                                          				Conferencing is not natively supported in HCS. However, with the use of a
                                          				third-party portal with CTX, Scheduled Conferencing can be supported. If you are
                                          				planning for a third-party portal, evaluate the third-party portal and validate
                                          				it against your requirements. |
| Step 5 | Determine your
                                       			 port capacity for video conferencing based on the following estimations. These
                                       			 estimates provide you with an estimate of the number of users that are expected
                                       			 to take part in a video conference at any time. Base these considerations on
                                       			 whether a centralized or dedicated video conferencing solution is being
                                       			 planned. Number of customers using
                                          				video conferencing. Number of video endpoints
                                          				each customer will use. Number of simultaneous
                                          				video conferences that you expect. The average number of
                                          				participants in each video conference. Average duration of video
                                          				conference. Use the
                                       			 following calculation to determine the port capacity. Number of ports needed.
                                          				This is the (number of video-enabled customers) x (number of simultaneous video
                                          				meetings per customer) x (number of participants per meeting) x (average number
                                          				of ports per participant). For example: (10
                                          				customers) x (2 simultaneous meetings per customer) x (6 participants per
                                          				meeting) x (1 port per participant) = 120 ports. The average
                                          				number of ports per participant must take into account the distribution of
                                          				different types of endpoints (number of screens), the quality of the video (HD,
                                          				SD, Audio only), and presentation sharing. Each port is assumed to provide a
                                          				1080p HD quality video. |
| Step 6 | Determine
                                       			 the type of video endpoints supported in the network. Immersive video
                                          				endpoints. Nonimmersive video
                                          				endpoints. Immersive
                                          				video endpoints enable the best possible in-person TelePresence video
                                          				collaboration experience, where attendees across multiple locations feel as
                                          				though they are in the same room. Due to the high quality of the video media,
                                          				immersive video endpoints consume higher amounts of bandwidth and network
                                          				resources than nonimmersive video endpoints. |
| Step 7 | Determine
                                       			 whether to provide video dialing between different service providers. To provide video dialing
                                          				between different service providers, set up the SBC to provide connectivity
                                          				between the different service providers. Make sure that agreements
                                          				and routing policies are in place for interprovider video dialing. |
| Step 8 | Determine
                                       			 whether you want to support over-the-top (OTT) connectivity for guest clients
                                       			 from other enterprises and integrate Microsoft Lync along with Dedicated Video
                                       			 Conferencing with Conductor/TMS/Virtual TS. You can use
                                          				Cisco Expressway to set up connectivity. |
| Step 9 | Determine if
                                       			 you need to transcode codecs within your video network. If yes, you need to
                                          				implement the Cisco TelePresence MSE 8710 server for transcoding. If no, you can use
                                          				Multipoint Switch (CTMS). CTMS is a less expensive option than the MSE, but
                                          				DTLS is not supported with CTMS. Any CTX-based calls are unsecure if you choose
                                          				CTMS. |
| Step 10 | Determine
                                       			 your bandwidth and QoS requirements for video, using the following information: Number of ports Number of endpoints Immersive or nonimmersive
                                          				video. Note Immersive video has higher bandwidth requirements. Types of endpoints. Use the
                                       			 following guidelines to evaluate bandwidth requirements: For every (shared)
                                          				three-screen TelePresence room at 1080p, add 16.7 Mbps (assumes 100-percent
                                          				utilization because these are shared services). For every single-screen
                                          				TelePresence at 1080p, add 4.5 Mbps (assumes 100-percent utilization). For every single-screen
                                          				TelePresence at 720p, add 1.68 Mbps (assumes 100-percent utilization). For shared EX90 at 720p,
                                          				add 1.5 Mbps (assumes 100-percent utilization). For personal (nonshared)
                                          				EX90 at 720p, add 136 Kbps (assumes much lower utilization). | Note | Immersive video has higher bandwidth requirements. |
| Note | Immersive video has higher bandwidth requirements. |
| Step 11 | Determine your
                                       			 security requirements for signaling and media. TLS for signaling
                                          				encryption. DTLS for media encryption. SRTP media encryption. |
| Step 12 | Determine the
                                       			 CTX model to use. Starter Package—If you
                                          				choose the Starter Package, there is a maximum of 250 ports with no active
                                          				meeting management license. Active video calls are not preserved. ACE is not
                                          				required with the Starter Package. Classic Package—If you
                                          				choose the Classic Package, ACE is implemented. |
| Step 13 | Consider the
                                       			 following when determining networking requirements: Data Center Network for
                                          				video infrastructure. VLANs. Virtual routing and
                                          				forwarding (VRF). TPaas network devices and
                                          				applications which are deployed in a shared environment. |

| Note | Immersive video has higher bandwidth requirements. |
|---|---|