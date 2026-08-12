[![](https://blog.webex.com/wp-content/uploads/2024/08/webex-primary-logo.svg)](https://blog.webex.com)
[![](https://blog.webex.com/wp-content/uploads/2024/08/webex-secondary-logo.svg)](https://blog.webex.com)
  * [Collaboration](https://blog.webex.com/category/collaboration/)
  * [Workspaces](https://blog.webex.com/category/workspaces/)
  * [Customer Experience](https://blog.webex.com/category/customer-experience/)
  * [Event Management](https://blog.webex.com/category/event-management/)
  * [Innovation & AI](https://blog.webex.com/category/innovation-ai/)


[![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2024%22%3E%3C/svg%3E)](https://blog.webex.com)
[![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2079%2024%22%3E%3C/svg%3E)](https://blog.webex.com)
[ ](https://twitter.com/intent/tweet?url=https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions) [ ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions&title=Proprietary%20RTCP%20Messages%20and%20Key%20Extensions) [ ](https://www.facebook.com/sharer/sharer.php?u=https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions)
[ ](https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions/ "Copy Link") [ ](https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions/ "Print")
[Engineering](https://blog.webex.com/category/engineering/)
# Proprietary RTCP Messages and Key Extensions
On Jul 28, 2025Jul 28, 2025By [Rob Hanton](https://blog.webex.com/contributors/robhanton/)8 Min Read
[ ](https://twitter.com/intent/tweet?url=https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions) [ ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions&title=Proprietary%20RTCP%20Messages%20and%20Key%20Extensions) [ ](https://www.facebook.com/sharer/sharer.php?u=https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions)
[ ](https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions/ "Copy Link") [ ](https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions/ "Print")
![](https://blog.webex.com/wp-content/uploads/2025/07/proprietary-rtcp-feature.jpg)
In the [previous](https://blog.webex.com/engineering/introducing-rtcp-the-rtp-control-protocol/) [blogs](https://blog.webex.com/engineering/rtcp-receiver-reports-and-stream-synchronization/) in this series, we looked at what RTCP is and its key standard messages as defined in [RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550). In this final series entry we will look at how applications can send their own proprietary RTCP messages, and some widely supported RTCP extensions.
### Application-Defined (APP)
**Application-Defined** packets are designed for proprietary and experimental extensions that have not been standardized.
![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201648%20433%22%3E%3C/svg%3E)
The regular header has a **Payload Type** of 204 and an **Item Count** that is extension-dependent. It then includes a 32-bit SSRC or CSRC which it is associated with in a fashion that is also extension-dependent.
There is then a 32-bit field containing a 4 character ASCII string; this is the Name of the extension, which is used to identify the format of the extension in question, and so should be chosen to be unique among APP packets the application supports receiving.
The format of the remainder of the RTCP packet is then defined by the extension in question, as identified by the **Name** , which also defines the purpose of the **item count** and SSRC/CSRC.
A receiver should ignore **Application-Defined** packets with a **Name** it does not recognize.
### Feedback (FB)
Feedback messages are defined in [RFC 4585](https://datatracker.ietf.org/doc/html/rfc%204585), which adds a mechanism for negotiating and sending RTCP feedback that can be used to respond to media issues. These feedback messages are sent by the  _recipient_ of the RTP media stream. Two messages in particular, which are used to request new video keyframes, are extremely important if video is being used.
![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201640%20462%22%3E%3C/svg%3E)
The regular header can have a **Payload Type** of 205 or 206 depending on the feedback message in question – 205 corresponds to a  _Transport Layer_ message while 206 corresponds to a  _Payload-Specific_ message (which to use is defined in their specification). For feedback messages, the **Item Count** is named the **Feedback Message Type** , or **FMT** , and also plays a role in differentiating between different types of feedback messages.
Subsequent to this is a 32-bit field for the **SSRC of packet sender** of the feedback message (e.g., the same value as the **Reporter SSRC** in the Sender Report or Receiver Report), followed by the **SSRC of media source** : the RTP media stream being received by the sender of the feedback message on which feedback is being provided.
Finally, there is a **Feedback Control Information (FCI)** portion, the contents and length of which are dependent on the type of feedback message.
A number of feedback messages are defined in [RFC 4585](https://datatracker.ietf.org/doc/html/rfc54585), but there are further specifications that define other messages, of which [RFC 5104](https://datatracker.ietf.org/doc/html/rfc5104) contains several key types. This document will list some of the most important and when they are used but will not go through the **FCI** format for each – these are generally straightforward and can be found in their relevant specifications.
Note that Feedback messages of any given type should not be sent unless they have been negotiated by both sides in SDP – see the ‘’rtcp-fb’ portion of the [SDP attributes blog](https://blog.webex.com/engineering/understanding-session-description-protocol-attributes/) for more details.  
|  **Name**  | **Defined by**  | P  | FMR  |  
| --- | --- | --- | --- |  
| Picture Loss Indication (PLI)  | [RFC 4585](https://datatracker.ietf.org/doc/html/rfc4585)  | 206  | 1  |  
| Full Intra Request (FIR)  | [RFC 5104](https://datatracker.ietf.org/doc/html/rfc5104)  | 206  | 4  |  
| Generic NACK (NACK)  | [RFC 4585](https://datatracker.ietf.org/doc/html/rfc4585)  | 205  | 1  |  
| Application Layer  | [RFC 4585](https://datatracker.ietf.org/doc/html/rfc4585)  | 206  | 15  |  
| Temporary Maximum Media Stream Bit Rate Request (TMMBR)  | [RFC 5104](https://datatracker.ietf.org/doc/html/rfc5104)  | 205  | 3  |  
| Temporary Maximum Media Stream Bit Rate Notification (TMMBN)  | [RFC 5104](https://datatracker.ietf.org/doc/html/rfc5104)  | 205  | 4  |  
_Some key RTCP feedback messages for video conferencing_
**PLI** and **FIR** messages both generally request a new video keyframe from the far end, but have different semantic meanings. A **Picture Loss Indication** feedback message signals that one or more packets required to decode a frame of video have been lost, while a **Full Intra Request** feedback message explicitly requests a keyframe. However, since the response of almost all receivers to a **PLI** is to send a keyframe, many implementations do not differentiate between them. Technically speaking, **PLI** is meant to be sent when a keyframe is required due to loss, and **FIR** when a keyframe is required because none have been received (e.g., at the start of a stream where the keyframe was missed) but many implementations treat them interchangeably, and indeed have the same code to handle receiving either message.
Implementing a method for requesting keyframes is a fundamental requirement of sending video over a lossy medium such as RTP over UDP, and **PLI** /**FIR** is the most common method for doing so in the field. An implementation concerned with wide interoperability should advertise and negotiate support for both; otherwise, of the two, **PLI** is most commonly supported and used.
Another mechanism for dealing with packet loss is the **Generic NACK** message, which is similar to **PLI** but allows the sender to specify exactly which RTP packets were not successfully received. In the simplest case this can serve as yet another mechanism for prompting a keyframe, but a more sophisticated media sender can instead choose to instead **retransmit** the missing packets. **NACK** is most commonly used in WebRTC devices, while **PLI** /**FIR** tends to be used in SIP devices.
**Application Layer** feedback messages are a way to include proprietary or non-standard feedback messages. The **Feedback Control Information** portion of these messages is application-dependent, but note that it is recommended that there is some mechanism for a receiver to identify what type of non-standard feedback message is being received. This is absolutely necessary for any implementation that supports two or more **Application Layer** messages and can negotiate both at the same time so they can be differentiated, but it is highly recommended, even if currently your implementation only has one **Application Layer** message, as changing the format if you later look to add another can pose significant concerns with backwards-compatibility. Not doing so often leads to ugly workarounds such as defining (and advertising) two versions of the same message with different formats. For instance, **REMB** , which will be discussed later in this section, achieves this by defining that the first 32 bits of the **FCI** contain the US-ASCII string “REMB”.
**TMMBR** and **TMMBN** are feedback messages related to bitrate control, used to throttle the media to avoid loss. Note that **TMMBN** messages are unusual in that, while most feedback messages are sent by the recipient of the RTP media stream, **TMMBN** messages are sent as feedback in response to receiving a **TMMBR** message, and hence are sent by the media _sender_.
**TMMBR** and **TMMBN** messages are most commonly seen in SIP devices. WebRTC devices instead use an application-level message named **Receiver Estimated Maximum Bitrate (REMB)**. This is  _not_ an IETF standard, but is instead documented as an IETF  _draft,_ [draft-alvestrand-rmcat-remb](https://datatracker.ietf.org/doc/html/draft-alvestrand-rmcat-remb). It is very similar to **TMMBR** , but is designed to allow more fine-grained control for use cases where multiple media streams are being received on a single RTP session. Note that while still supported this is an older method of bandwidth control; in most cases WebRTC implementations now use [Transport-Wide Congestion Control](https://webrtc.googlesource.com/src/+/refs/heads/main/docs/native-code/rtp-hdrext/transport-wide-cc-02/README.md) (TWCC or TransportCC) to do sender-side rate control.
### Sending RTCP Messages
RTCP messages are generally sent using the same transport as the RTP messages they accompany, by convention with RTP being received on an even-numbered port and RTCP being received on a port number one higher. The “a=rtcp” attribute defined in [RFC 3605](https://datatracker.ietf.org/doc/html/rfc3605) allows a receiver to advertise to receive RTCP on a different IP and/or port to the RTP, but support for this should not be assumed.
Meanwhile, [RFC 5761](https://datatracker.ietf.org/doc/html/rfc5761) defines advertising support for multiplexing RTP and RTCP onto the same port via the “a=rtcp-mux” attribute, which does have a good level of support among various implementations (and is used in WebRTC), and reduces the number of ports a receiver must open. The specification goes into detail about the complexities of demultiplexing RTCP from RTP, STUN and other types that might be received on the same port.
## Compounding
Thanks to each RTCP packet header containing a **length** parameter, a single RTCP packet can contain multiple RTCP messages— referred to as a  _compound RTCP packet_. Each message can be processed individually, and there is no significance to the ordering of the messages within the packet. Messages of a given type can appear more than once if desired.
Less intuitively, the RTCP specification ([RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550)) **mandates** that all RTCP messages are sent as compound packets of two or more messages, with the first message always being an **SR** or **RR** messageand the second always being an **SDES** message containing a **CNAME**. This is the case even if the device sending the RTCP packet has not received or sent any media, in which case the initial message must be a **Receiver Report** with zero **report blocks**.
Thus, to send a **BYE** or **PLI** feedback message, the RTCP sender must construct an RTCP packet containing an SR or RR message, an SDES message, and  _then_ the **BYE** or **PLI** message. For these non-scheduled messages [RFC 4585](https://datatracker.ietf.org/doc/html/rfc4585) suggests using a **Minimal compound RTCP** packet, which contains no additional **RR** s and limits the **SDES** message to just the **CNAME** , though in practice most implementations do not need an additional **RR** or use **SDES** items beyond the **CNAME** , making this optimization moot.
This requirement is not too onerous for normal RTCP transmission, which is generally relatively infrequent, even when using feedback messages. However, if an implementation is choosing to use proprietary RTCP messaging with a much higher transmission rate, the extra bandwidth the compounding requirements impose can impose a very high cost. In such circumstances, an implementation might choose to send RTCP packets which do not comply with [RFC 3550’s](https://datatracker.ietf.org/doc/html/rfc3550) requirements on compounding, though care should be taken when doing so with regards to demultiplexing, and this should only be done when using these application-specific messages; standard messages should be sent following the compounding requirements.
### Transmission Intervals
[RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550) also defines a complex set of rules for calculating the **transmission interval** (the periodic rate at which regular RTCP updates should be sent) based on a database of participants in the meeting as determined via the SSRCs/CSRCs received.
The reason for this is to cope with distributed meetings where a server propagates RTCP across all participants, and there is a desire to prevent the bandwidth requirements for RTCP to escalate too much in conferences with very large numbers of participants.
In practice though, in modern conferencing, media servers generally do not forward all RTCP in this fashion, and participant information is shared via some other mechanism such as a roster list distributed over the signaling channel. As such, careful management of the transmission interval is much less relevant, and many devices do not implement the complex system defined in [RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550). Instead, they use a static transmission internal, often of 5 seconds, at which they send the **SR** /**RR** and **SDES** , and then send **feedback** messages and **BYE** s as necessary.
If there is the possibility of an implementation being used in large meetings in which all RTCP information is aggregated and forwarded to each receiver, then implementors should read [RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550) carefully and follow the detailed guidance and algorithms provided therein to calculate an appropriate transmission time based on the RTCP received.​​​​​​​
#### About The Author
![Rob Hanton](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2096%22%3E%3C/svg%3E)
Rob Hanton Principal Engineer and Architect Cisco
Rob Hanton is a Principal Engineer and Architect for Webex.
[Learn more](https://blog.webex.com/contributors/robhanton/)
#### Topics
[ASCII](https://blog.webex.com/tag/ascii/)[Audio-video synchronization](https://blog.webex.com/tag/audio-video-synchronization/)[BYE](https://blog.webex.com/tag/bye/)[CNAME](https://blog.webex.com/tag/cname/)[CSRC](https://blog.webex.com/tag/csrc/)[NACK](https://blog.webex.com/tag/nack/)[Receiver Report](https://blog.webex.com/tag/receiver-report/)[Report Block](https://blog.webex.com/tag/report-block/)[RFC 3550](https://blog.webex.com/tag/rfc-3550/)[RFC 3605](https://blog.webex.com/tag/rfc-3605/)[RFC 4585](https://blog.webex.com/tag/rfc-4585/)[RFC 5761](https://blog.webex.com/tag/rfc-5761/)[RTCP](https://blog.webex.com/tag/rtcp-2/)[RTCP format](https://blog.webex.com/tag/rtcp-format/)[RTP](https://blog.webex.com/tag/rtp/)[SDES](https://blog.webex.com/tag/sdes/)[Sender Report](https://blog.webex.com/tag/sender-report/)[SSRC](https://blog.webex.com/tag/ssrc/)[TMMBR](https://blog.webex.com/tag/tmmbr/)
* * *
## More like this
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%201200%22%3E%3C/svg%3E)simple Engineering Building voice AI that can keep up with real conversations By Gergely Lukacsy, Vibhor Jain5 Min Read ](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/)
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%20961%22%3E%3C/svg%3E)simple Engineering Resilience by Design: How Webex Contact Center Stays Up When the ... By Iyer Venkataraman, Divyesh Khandeshi5 Min Read ](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/)
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%201200%22%3E%3C/svg%3E)simple Engineering LRAC Challenge 2025: Pushing the limits of speech coding By Ivana Balic4 Min Read ](https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding/)
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%201200%22%3E%3C/svg%3E)simple Engineering RTCP Receiver Reports and Stream Synchronization. By Rob Hanton8 Min Read ](https://blog.webex.com/engineering/rtcp-receiver-reports-and-stream-synchronization/)
Products
  * [Webex Suite](https://www.webex.com/suite/collaboration-suite.html)
  * [Meetings](https://www.webex.com/meetings.html)
  * [Calling](https://www.webex.com/enterprise-cloud-calling.html)
  * [Messaging](https://www.webex.com/team-collaboration.html)
  * [Events](https://www.webex.com/events.html)
  * [Video Messaging](https://vidcast.io/)
  * [Polling](https://www.webex.com/suite/polling.html)
  * [Webinars](https://www.webex.com/webinar.html)
  * [Whiteboarding](https://www.webex.com/suite/whiteboard.html)
  * [Cloud Contact Center](https://www.webex.com/us/en/products/customer-experience/contact-center.html)
  * [CPaaS](https://www.webex.com/us/en/products/customer-experience/cpaas.html)


Footer Terms Menu
  * [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
  * [Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
  * [Cookies](https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies)
  * [Trademarks](https://www.cisco.com/web/siteassets/legal/trademark.html)
  * [English](https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions/)


Devices
  * [Room Devices](https://www.webex.com/us/en/devices/room-devices.html)
  * [Desk Devices](https://www.webex.com/us/en/devices/desk-series.html)
  * [Digital Whiteboards](https://www.webex.com/us/en/devices/digital-whiteboards.html)
  * [Phones](https://www.webex.com/us/en/devices/phone-series.html)
  * [Cameras](https://www.webex.com/us/en/devices/cameras.html)
  * [Headsets](https://www.webex.com/us/en/devices/headsets.html)
  * [Room Accessories](https://www.webex.com/us/en/devices/accessories.html)


Resources
  * [Pricing](https://pricing.webex.com/us/en/)
  * [Downloads](https://www.webex.com/downloads.html)
  * [Help Center](https://help.webex.com/)
  * [Webex Community](https://cs.co/webexcommunity)
  * [Product Essentials](https://essentials.webex.com/)
  * [Watch Webinars](https://www.webex.com/learn/webinars-demos.html)
  * [App Hub](https://apphub.webex.com/)
  * [Accessibility](https://www.webex.com/accessibility.html)
  * [Developers](https://developer.webex.com/)


Company
  * [Cisco](https://www.cisco.com/c/en/us/solutions/collaboration/index.html#~stickynav=1)
  * [Webex Customer Advocacy Program](https://www.webex.com/us/en/dg/customer-advocacy-program.html)
  * [Contact Support](https://help.webex.com/contact/)
  * [Contact Sales](https://www.webex.com/contact-sales.html?locale=US)
  * [Webex Merch Store](https://merchandise.cisco.com/featured/webex-by-cisco.html)
  * [Careers](https://www.webex.com/company/careers.html)


  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://twitter.com/webex)
  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://www.linkedin.com/company/webex)
  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://www.facebook.com/webex)
  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://www.youtube.com/c/webex)
  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://www.instagram.com/webex/)


©2026 Cisco and/or its affiliates. All Rights Reserved.
  * [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
  * [Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
  * [Cookies](https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies)
  * [Trademarks](https://www.cisco.com/web/siteassets/legal/trademark.html)
  * [English](https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions/)


