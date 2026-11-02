---
doc_id: help-webex-com-en-us-article-ipxxr2-bff03d1383
source_url: https://help.webex.com/en-us/article/ipxxr2
retrieved_at: 2026-11-02T12:57:22.374881+00:00
---

## Component versions

The following table lists the component and version used for testing support for video compatibility.

The absence of a device or release does not imply a lack of interoperability.

We deprecated support for Skype for Business joining Webex meetings in January 2023.

Component

Version

Cisco Unified Communications Manager (Cisco UCM)

11.5.1

Cisco Video Communication Server (Cisco VCS)

8.10

Polycom Converged Management Application (CMA) / Video Border Proxy (VBP)

6.2.5 / 11.2.16

Polycom Distributed Media Application (DMA) / RealPresence Access Director (RPAD)

6.0.4_Build_1 / 3.1.0_build_13773

## Video system and application compatibility

Webex Video supports most relevant standards-based systems, software, and infrastructure. The following table lists the software and system releases that were tested for interoperability with the latest Webex Video release. This document is updated as additional systems and software are tested.

Compatibility test results

Compatibility status

Works

Partial

Does Not Work

The absence of a device or release does not imply a lack of interoperability.

Video System or Software

Model

Registered to

Version

Compatibility Status

Cisco TelePresence room system

Cisco 1300/3000/3200

Cisco UCM

1.10.13

Works

For CTS 1xxx systems running version 1.10.x, content sharing doesn’t work as expected due to lack of H.264 support on the content channel.

Cisco TX9000/9200

Cisco UCM

6.1.10

Works

Cisco IX5000/IX5200

Cisco UCM

8.1

Partial

IX is designed for on-premises conferencing and is very sensitive to packet loss over the Internet. Users can experience video loss even with 1% packet loss.

Cisco MX200/300/700/800

Cisco UCM / Cisco VCS

9.2

Works

Cisco C20/40/60/90

Cisco UCM / Cisco VCS

7.3

Works

Cisco SX10/20/80

Cisco UCM

9.2

Works

Cisco TelePresence desktop system

Cisco EX60/EX90

Cisco UCM / Cisco VCS

TC7.3

Works

Cisco DX650

Cisco UCM

10.2.5

Works

Cisco DX70

Cisco UCM

9.2

Works

Cisco DX80

Cisco UCM

9.2

Works

Cisco IP Phone

Cisco 8845

Cisco UCM

11.0.1

Works

Cisco 8941

Cisco UCM

9.2.3

Works

Cisco 9951

Cisco UCM

9.4.2

Works

Cisco 9971

Cisco UCM

9.4.2

Works

Cisco Jabber

Windows 7

Cisco UCM / Cisco Unified Personal Communicator (UPC)

11.5

Works

Mac

Cisco UCM / Cisco UPC

11.5

Works

iPad

Cisco UCM / Cisco UPC

11.5

Works

iPhone

Cisco UCM / Cisco UPC

11.5

Works

Android (Mobile Phone Only)

Cisco UCM / Cisco UPC

11.5

Works

Cisco Jabber Guest

Windows 7

Cisco VCS

4.8.6

Works

Mac

Cisco VCS

4.8.6

Works

iPhone

Cisco VCS

9.3.6

Works

iPad

Cisco UCM / Cisco UPC

9.3.6

Works

Webex App

Windows 7

Webex App

Works

Mac

Webex App

Works

iPad

Webex App

Works

iPhone

Webex App

Works

Android

Webex App

Works

Firefox (Windows)

Webex App

Partial

Firefox (Mac)

Webex App

Partial

Other 3rd Party Video Systems

Polycom HDX Series (SIP)

Polycom CMA

3.1.6

Works

Polycom HDX (SIP and H.323)

Polycom DMA

3.1.6

Works

Polycom HDX (SIP and H.323)

Cisco VCS

3.1.9

Works

LifeSize (SIP)

Cisco VCS

5.0.9

Works

H.323 Annex-O DNS SRV based URI dialing (unregistered)

Polycom HDX Series

Unregistered

3.1.9

Works

Polycom RealPresence Group Series

Unregistered

4.1.5

Works

LifeSize

Unregistered

5.0.9

Works

Avaya XT5000

Unregistered

Does Not Work

H.323 Stand-alone IP dialing

Polycom HDX series (on a public IP address)

Unregistered

3.1.11

Partial

Users cannot see any video after entering meeting.

Workaround:

Host can start and stop desktop sharing. This will restore the main video stream.

Polycom HDX series (behind a NAT)

Unregistered

3.1.11

Does Not Work

Polycom RealPresence Group Series

Unregistered

6.1.2

Partial

Users cannot see any video after entering meeting.

Workaround:

User can hold and resume the call. This will restore the main video stream.

LifeSize ICON

Unregistered

2.6.1

Partial

First few seconds of IVR audio prompt clipped.

Workaround:

Continue entering the meeting number followed by the # key; call will connect.

For Lifesize-specific issues, see this article: https://help.webex.com/WBX000020461/Lifesize-Endpoints-won-t-Connect-Using-H-323

For Polycom-specific issues see this article: https://help.webex.com/WBX86490/I-Get-Audio-Only-or-360p-video-quality-in-Cisco-Webex-Video-Platform-Joined-from-a-Polycom-Endpoint

For all other known issues, refer to Known Issues and Limitations for Webex Video .

| Component | Version |
|---|---|
| Cisco Unified Communications Manager (Cisco UCM) | 11.5.1 |
| Cisco Video Communication Server (Cisco VCS) | 8.10 |
| Polycom Converged Management Application (CMA) / Video Border Proxy (VBP) | 6.2.5 / 11.2.16 |
| Polycom Distributed Media Application (DMA) / RealPresence Access Director (RPAD) | 6.0.4_Build_1 / 3.1.0_build_13773 |

| Compatibility status |
|---|
| Works |
| Partial |
| Does Not Work |

| Video System or Software | Model | Registered to | Version | Compatibility Status |
|---|---|---|---|---|
| Cisco TelePresence room system | Cisco 1300/3000/3200 | Cisco UCM | 1.10.13 | Works For CTS 1xxx systems running version 1.10.x, content sharing doesn’t work as expected due to lack of H.264 support on the content channel. |
| Cisco TX9000/9200 | Cisco UCM | 6.1.10 | Works |
| Cisco IX5000/IX5200 | Cisco UCM | 8.1 | Partial IX is designed for on-premises conferencing and is very sensitive to packet loss over the Internet. Users can experience video loss even with 1% packet loss. |
| Cisco MX200/300/700/800 | Cisco UCM / Cisco VCS | 9.2 | Works |
| Cisco C20/40/60/90 | Cisco UCM / Cisco VCS | 7.3 | Works |
| Cisco SX10/20/80 | Cisco UCM | 9.2 | Works |
| Cisco TelePresence desktop system | Cisco EX60/EX90 | Cisco UCM / Cisco VCS | TC7.3 | Works |
| Cisco DX650 | Cisco UCM | 10.2.5 | Works |
| Cisco DX70 | Cisco UCM | 9.2 | Works |
| Cisco DX80 | Cisco UCM | 9.2 | Works |
| Cisco IP Phone | Cisco 8845 | Cisco UCM | 11.0.1 | Works |
| Cisco 8941 | Cisco UCM | 9.2.3 | Works |
| Cisco 9951 | Cisco UCM | 9.4.2 | Works |
| Cisco 9971 | Cisco UCM | 9.4.2 | Works |
| Cisco Jabber | Windows 7 | Cisco UCM / Cisco Unified Personal Communicator (UPC) | 11.5 | Works |
| Mac | Cisco UCM / Cisco UPC | 11.5 | Works |
| iPad | Cisco UCM / Cisco UPC | 11.5 | Works |
| iPhone | Cisco UCM / Cisco UPC | 11.5 | Works |
| Android (Mobile Phone Only) | Cisco UCM / Cisco UPC | 11.5 | Works |
| Cisco Jabber Guest | Windows 7 | Cisco VCS | 4.8.6 | Works |
| Mac | Cisco VCS | 4.8.6 | Works |
| iPhone | Cisco VCS | 9.3.6 | Works |
| iPad | Cisco UCM / Cisco UPC | 9.3.6 | Works |
| Webex App | Windows 7 | Webex App |  | Works |
| Mac | Webex App |  | Works |
| iPad | Webex App |  | Works |
| iPhone | Webex App |  | Works |
| Android | Webex App |  | Works |
| Firefox (Windows) | Webex App |  | Partial |
| Firefox (Mac) | Webex App |  | Partial |
| Other 3rd Party Video Systems | Polycom HDX Series (SIP) | Polycom CMA | 3.1.6 | Works |
| Polycom HDX (SIP and H.323) | Polycom DMA | 3.1.6 | Works |
| Polycom HDX (SIP and H.323) | Cisco VCS | 3.1.9 | Works |
| LifeSize (SIP) | Cisco VCS | 5.0.9 | Works |
| H.323 Annex-O DNS SRV based URI dialing (unregistered) | Polycom HDX Series | Unregistered | 3.1.9 | Works |
| Polycom RealPresence Group Series | Unregistered | 4.1.5 | Works |
| LifeSize | Unregistered | 5.0.9 | Works |
| Avaya XT5000 | Unregistered |  | Does Not Work |
| H.323 Stand-alone IP dialing | Polycom HDX series (on a public IP address) | Unregistered | 3.1.11 | Partial Users cannot see any video after entering meeting. Workaround: Host can start and stop desktop sharing. This will restore the main video stream. |
| Polycom HDX series (behind a NAT) | Unregistered | 3.1.11 | Does Not Work |
| Polycom RealPresence Group Series | Unregistered | 6.1.2 | Partial Users cannot see any video after entering meeting. Workaround: User can hold and resume the call. This will restore the main video stream. |
|  | LifeSize ICON | Unregistered | 2.6.1 | Partial First few seconds of IVR audio prompt clipped. Workaround: Continue entering the meeting number followed by the # key; call will connect. |