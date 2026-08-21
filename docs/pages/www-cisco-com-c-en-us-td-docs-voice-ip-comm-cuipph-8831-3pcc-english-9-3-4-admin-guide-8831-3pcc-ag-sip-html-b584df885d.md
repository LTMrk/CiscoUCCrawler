---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-english-9-3-4-admin-guide-8831-3pcc-ag-sip-html-b584df885d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/english/9_3_4/admin-guide/8831-3pcc-ag/sip.html
retrieved_at: 2026-08-21T02:09:22.036323+00:00
---

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

# Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

Updated: October 22, 2014

Chapter: Configure SIP and NAT

## Chapter: Configure SIP and NAT

## Configure SIP and NAT

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control uses the following protocol:

- Session Initiation Protocol (SIP)

This chapter describes how to configure the SIP phone protocol:

## SIP and Cisco Unified IP Conference Phone 8831 for Third-Party Call Control

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control uses Session Initiation Protocol (SIP), which allows interoperation with all IT service providers that support SIP. SIP is an IETF-defined signaling protocol that controls voice communication sessions in an IP network.

SIP handles signaling and session management within a packet telephony network. Signaling allows call information to be carried across network boundaries. Session management controls the attributes of an end-to-end call.

In typical commercial IP telephony deployments, all calls go through a SIP proxy server. The requesting phone is called the SIP user agent server (UAS), while the receiving phone is called the user agent client (UAC).

SIP message routing is dynamic. If a SIP proxy receives a request from a UAS for a connection but cannot locate the UAC, the proxy forwards the message to another SIP proxy in the network. When the UAC is located, the response is routed back to the UAS, and a direct peer-to-peer session is established between the two UAs. Voice traffic is transmitted between UAs over dynamically-assigned ports using Real-time Protocol (RTP).

RTP transmits real-time data such as audio and video; it does not guarantee real-time delivery of data. RTP provides mechanisms for the sending and receiving applications to support streaming data. Typically, RTP runs on top of UDP.

### SIP Over TCP

To guarantee state-oriented communications, Cisco conference phone can use TCP as the transport protocol for SIP. This protocol provides guaranteed delivery that assures that lost packets are retransmitted. TCP also guarantees that the SIP packages are received in the same order that they were sent.

TCP overcomes the problem UDP ports have of being blocked by corporate firewalls. With TCP, new ports do not need to be opened or packets dropped, because TCP is already in use for basic activities, such as Internet browsing or e-commerce.

### SIP Proxy Redundancy

An average SIP proxy server can handle tens of thousands of subscribers. A backup server allows an active server to be temporarily switched out for maintenance. Cisco phones support the use of backup SIP proxy servers to minimize or eliminate service disruption.

A static list of proxy servers is not always adequate. If your user agents are served by different domains, for example, you would not want to configure a static list of proxy servers for each domain into every Cisco IP phone.

A simple way to support proxy redundancy is to configure a SIP proxy server in the Cisco conference phone configuration profile. The DNS SRV records instruct the phones to contact a SIP proxy server in a domain named in SIP messages. The phone consults the DNS server. If configured, the DNS server returns an SRV record that contains a list of SIP proxy servers for the domain, with their host names, priority, listening ports, and so forth. The Cisco conference phone tries to contact the hosts in the order of their priority.

If the Cisco conference phone currently uses a lower-priority proxy server, the phone periodically probes the higher-priority proxy and switches to the higher-priority proxy when available.

### Dual Registration

The phone always registers to both primary (or primary outbound) and alternate (or alternate outbound) proxies. After registration, the phone sends out Invite and Non-Invite SIP messages via primary proxy first. If there is no response for the new INVITE from the primary proxy, after timeout, the phone should attempt with the alternate proxy.

Dual registration is supported per line basis. Three new parameters are added which can be configured via Web GUI and remote provisioning:

- Alternate Proxy—Default is empty

- Alternate Outbound Proxy—Default is empty

- Dual Registration—Default is NO (turned off)

Upon configuring the parameters, reboot the phone for the feature to take effect.

Note The administrator should specify a value for primary proxy (or primary outbound proxy) and alternate proxy (or alternate outbound proxy) for the feature to function properly.

### Limitations for Dual Registration and DNS SRV Redundancy

The limitations for Dual Registration and DNS SRV redundancy are as follows:

- When Dual Registration is enabled, DNS SRV Proxy Fallback/Recovery must be disabled.

- Do not use Dual Registration in conjunction with other Fallback/Recovery mechanisms. For example: Broadsoft mechanism.

- There is no recovery mechanism for feature request. However, the administrator can adjust the re-registration time for a prompt update of the registration state for primary and alternate proxy.

### Alternate Proxy and Dual Registration

When the Dual Register parameter is set to No, Alternate Proxy is ignored.

### Register Upon Failover/Recovery

- Failover—The phone performs a failover to secondary proxy when the SIP request gets no response from primary proxy.

- Recovery—The phone attempts to re-register with the primary proxy while registered or actively connected to the secondary proxy.

### Fallback Behavior

The fallback occurs when the current registration expires or Proxy Fallback Intvl fires.

If the Proxy Fallback Intvl exceeds, all the new SIP messages go to primary proxy.

For example, when the value for Register Expires is 3600 seconds and Proxy Fallback Intvl is 600 seconds, the fallback is triggered 600 seconds later.

When the value for Register Expires is 800 seconds and Proxy Fallback Intvl is 1000 seconds, the fallback is triggered at 800 seconds.

After successfully registering back to primary server, all the SIP messages go to primary server.

### RFC3261 Support

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control supports RFC-3261, the SIP UPDATE Method.

### Support for SIP NOTIFY XML-Service

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control support the SIP NOTIFY XML-Service event. On receipt of a SIP NOTIFY message with an XML-Service event, the phone challenges the NOTIFY with a 401 response if the message does not contain correct credentials. The client must be furnish the correct credentials using MD5 digest with the SIP account password for the corresponding line of the IP phone.

The body of the message can contain the XML event Message. For example:

Authentication:

## Configure SIP

SIP settings for the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control are configured for the phone in general and for the extensions.

### Configure Basic SIP Parameters

To configure general SIP parameters, navigate to Admin Login > advanced > Voice > SIP . Under SIP Parameters , make these changes:

Max Forward

The number of proxies or gateways that can forward the request to the next downstream server. The Max-Forwards value is an integer in the range of 0 to 255 indicating the remaining number of times the request message is allowed to be forwarded. This count is decremented by each server that forwards the request. The initial value is 70.

Max Redirection

Number of times an invite can be redirected to avoid an infinite loop. The default is 5.

SIP User Agent Name

User-Agent header used in outbound requests. The default is $VERSION. If empty, the header is not included. Macro expansion of $A to $D corresponding to GPP_A to GPP_D allowed.

SIP Server Name

Server header used in responses to inbound responses. The default is $VERSION .

SIP Reg User Agent Name

User-Agent name used in a REGISTER request. If not specified, the SIP User Agent Name is used for the REGISTER request.

SIP Accept Language

The preferred languages for reason phrases, session descriptions, or status responses carried as message bodies in the response. If blank, the header is not included and the server assumes that all languages are acceptable to the client. Defaults to blank.

RFC 2543 Call Hold

If set to Yes , the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control includes Session Description Protocol (SDP) syntax c=0.0.0.0 when sending a SIP re-INVITE to a peer to hold the call. If set to No, the phone does not include the c=0.0.0.0 syntax in the SDP. With either setting, the phone includes a=sendonly syntax in the SDP. Defaults to Yes.

SIP TCP Port Min

Lowest TCP port number that can be used for SIP sessions. Defaults to 5060.

SIP TCP Port Max

Highest TCP port number that can be used for SIP sessions. Defaults to 5080.

Caller ID Header

Select from where the IP phone gets the caller ID:

PAID-RPID-FROM

PAID-FROM

RPID-PAID-FROM

RPID-FROM

FROM header

Defaults to PAID-RPID-FROM.

Max INVITE Retry Attempts

Maximum number of INVITE retry attempts by the phone.

Defaults to 6.

Max NON-INVITE Retry Attempts

Maximum number of NON-INVITE retry attempts by the phone.

Defaults to 6.

### Configure SIP Timer Values

All SIP timer values are in seconds. To configure SIP timer values, navigate to Admin Login > advanced > Voice > SIP. Under SIP Timer Values (sec), make these changes:

SIP T1

RFC-3261 T1 value (RTT estimate). Ranges from 0 to 64 seconds. Defaults to 0.5 seconds.

SIP T2

RFC-3261 T2 value, the maximum retransmit interval for non-INVITE requests and INVITE responses. Ranges from 0 to 64 seconds. Defaults to 4 seconds.

INVITE Expires

The length of time the INVITE is valid. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000. Defaults to 240 seconds.

ReINVITE Expires

ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000. Defaults to 30

Reg Retry Intvl 1

Interval to wait before the phone retries registration after failing during the previous registration. The range is from 1 to 2147483647. Do not enter 0. Defaults to 30 seconds.

Reg Retry Long Intvl

When registration fails with a SIP response code that does not match the Retry Reg response status code (RSC) value (see next table), the phone waits for this length of time before retrying.

If this interval is 0, the phone stops trying. This value should be much larger than the Reg Retry Intvl value. The range is from 0 to 2147483647. Defaults to 1200 seconds.

Reg Retry Random Delay

Random delay added to the Register Retry Intvl value when retrying REGISTER after a failure. Minimum and maximum random delay to be added to the short timer. The range is from 0 to 2147483647. Defaults to 0, which disables this feature.

Reg Retry Long Random Delay

Random delay added to Register Retry Long Intvl value when retrying REGISTER after a failure.

Minimum and maximum random delay to be added to the long timer. Random delay range (in seconds) to add to the Register Retry Long Intvl when retrying REGISTER after a failure. Defaults to 0, which disables this feature.

Reg Retry Intvl Cap

Reg_Retry_Intvl_Cap—Maximum value of the exponential delay. The maximum value to cap the exponential backoff retry delay (which starts at the Register Retry Intvl and doubles every retry). Defaults to 0, which disables the exponential backoff (that is, the error retry interval is always at the Register Retry Intvl). When this feature is enabled, the Reg Retry Random Delay is added to the exponential backoff delay value. The range is from 0 to 2147483647.

1. The phone can use a RETRY-AFTER value when it is received from a SIP proxy server that is too busy to process a request (503 Service Unavailable message). If the response message includes a RETRY-AFTER header, the phone waits for the specified length of time before to REGISTER again. If a RETRY-AFTER header is not present, the phone waits for the value specified in the Reg Retry Interval or the Reg Retry Long Interval.

### Configure Response Status Code Handling

To configure response status code handling, under Response Status Code Handling make these changes:

- Try Backup RSC —SIP response code that retries a backup server for the current request. Defaults to blank.

- Retry Reg RSC —Interval the device waits before re-trying registration after a failed registration. Defaults to blank.

### Configure RTP Parameters

To configure Real-time Transport Protocol (RTP), navigate to Admin Login > advanced > Voice > SIP . Under RTP Parameters , configure these fields:

- RTP Port Min —Minimum port number for RTP transmission and reception. <RTP Port Min> and <RTP Port Max> defines a range that contains at least 10 even number ports (twice the number of lines); for example, 100–106. Defaults to 16384.

- RTP Port Max —Maximum port number for RTP transmission and reception. <RTP Port Min> and <RTP Port Max> should define a range that contains at least 10 even number ports (twice the number of lines); for example, 100–106. Defaults to 16482.

- RTP Packet Size —Packet size in seconds. The range is from 0.01 to 0.16. Valid values must be a multiple of 0.01 seconds. Defaults to 0.02.

- RTCP Tx Enable —To enable Real-Time Transport Control Protocol (RTCP) sender report on an active connection. Defaults to no.

During an active connection, the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control sends out compound RTCP packets. Each compound RTP packet, except the last one, contains a sender report (SR) and a source description (SDES). The last RTCP packet contains an additional BYE packet. Each SR, except the last one, contains one receiver report (RR); the last SR carries no RR.

The SDES contains CNAME, NAME, and TOOL identifiers:

– CNAME — User ID@Proxy

– NAME — Display Name (or Anonymous if user blocks caller ID)

– TOOL —Vendor/Hardware-platform-software-version.

### Configure SDP Payload Types

Configured dynamic payloads are used for outbound calls only when the conference phone presents a Session Description Protocol (SDP) offer. For inbound calls with a SDP offer, the phone follows the caller’s assigned dynamic payload type.

The IP phone conference phones use the configured codec names in outbound SDP. For incoming SDP with standard payload types of 0-95, the IP conference phone ignores the codec names. For dynamic payload types, the phone identifies the codec by the configured codec names (comparison is case-sensitive).

To configure SDP payload types, navigate to Admin Login > advanced > Voice > SIP . Under SDP Payload Types , configure these parameters:

AVT Dynamic Payload

Any non-standard data. Both sender and receiver must agree on a number. Ranges from 96 to 127. Defaults to 101.

### Configure SIP Settings for Extensions

To configure SIP settings, navigate to Admin Login > advanced > Voice > Extension . Under SIP Settings , configure the following fields:

SIP Transport

Select from UDP , TCP or TLS . Defaults to UDP.

SIP Port

Port number of the SIP message listening and transmission port. Defaults to 5060.

SIP 100REL Enable

Support of 100REL SIP extension for reliable transmission of provisional responses (18x) and use of PRACK requests. Select Yes to enable. Defaults to No.

Auth Resync-Reboot

The Cisco Unified IP Conference Phone 8831 authenticates the sender when it receives a NOTIFY message with the following requests:

- resync

- reboot

- report

- restart

- XML-service

Select Yes to enable. Defaults to Yes.

SIP Remote-Party-ID

The Remote-Party-ID header to use instead of the From header. Select Yes to enable. Defaults to Yes.

Refer-To Target Contact

Indicates the refer-to target. Select Yes to send the SIP Refer to the contact. Defaults to No.

SIP Debug Option

How SIP messages are received at or sent from the proxy listen port to the log. Select:

- Default—No messages.

- Current—Logs all the current SIP messages in full text

- Full—Logs all SIP messages in full text.

Sticky 183

When enabled, the IP telephony ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound INVITE. To enable this feature, select Yes . Otherwise, select No . Defaults to No.

Auth INVITE

When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy. To enable this feature, select Yes . Defaults to No.

When a tel URL is converted to a SIP URL and the telephone number is represented by the user portion of the URL, the SIP URL includes the optional :user=phone parameter (RFC3261). For example:

To: sip:+12325551234@example.com;user=phone

To enable this optional parameter, select Yes . The default value is No.

### Configure a SIP Proxy Server

To configure SIP proxy and registration parameters, navigate to Admin Login > advanced > Voice > Extension . Under Proxy and Registration , configure the following fields:

Proxy

SIP proxy server and port number set by the service provider for all outbound requests. For example: 192.168.2.100:6060.

The port number is optional. The default is port 5060.

Outbound Proxy

All outbound requests are sent as the first hop. Enter an IP address or domain name.

Alternate Proxy

Alternate Outbound Proxy

This feature provides fast fallback when there is network partition at he Internet or when the primary proxy (or primary outbound proxy) is not responsive or available. The feature works well in a Verizon deployment environment as the alternate proxy is the Integrated Service Router (ISR) with analog outbound phone connection.

Enter the proxy server addresses and port numbers in these fields. After the phone is registered to the primary proxy and the alternate proxy (or primary outbound proxy and alternate outbound proxy), the phone always sends out INVITE and Non-INVITE SIP messages (except registration) via the primary proxy. The phone always registers to both the primary and alternate proxies. If there is no response from the primary proxy after timeout (per the SIP RFC spec) for a new INVITE, the phone attempts to connect with the alternate proxy. The phone always tries the primary proxy first, and immediately tries the alternate proxy if the primary is unreachable.

Active transactions (calls) never fall back between the primary and alternate proxies. If there is fallback for a new INVITE, the subscribe/notify transaction will fall back accordingly so that the phone's state can be maintained properly. You must also set Dual Registration in the Proxy and Registration section to Yes.

Register

Enables periodic registration with the proxy. This parameter is ignored if a proxy is not specified. To enable this feature, select Yes . Defaults to Yes.

Make Call Without Reg

Enables making outbound calls without successful (dynamic) registration by the phone. If set to no, the dial tone plays only when registration is successful. To enable this feature, select Yes . Defaults to No.

Register Expires

Defines how often the phone renews registration with the proxy. If the proxy responds to a REGISTER with a lower expires value, the phone renews registration based on that lower value instead of the configured value.

If registration fails with an “Expires too brief” error response, the phone retries with the value specified in the Min-Expires header of the error.

The range is from 32 to 2000000. Defaults to 3600 seconds.

Use DNS SRV

Enables DNS SRV lookup for the proxy and outbound proxy. To enable this feature, select Yes . Otherwise, select No . Defaults to No.

Proxy Fallback Intvl

Sets the delay after which the phone retries from the highest priority proxy (or outbound proxy) after it has failed over to a lower priority server.

The phone should have the primary and backup proxy server list from a DNS SRV record lookup on the server name. It needs to know the proxy priority; otherwise, it does not retry.

The range is from 0 to 65535. Defaults to 3600 seconds.

Dual Registration

Set to Yes to enable the Dual registration/Fast Fallback feature. To enable the feature you must also configure the alternate proxy/alternate outbound proxy fields in the Proxy and Registration section.

### Configure Subscriber Information Parameters

To configure subscriber information parameters for each extension, navigate to Admin Login > advanced > Voice > Extension . Under Subscriber Information , configure the following fields:

Display Name

Name displayed as the caller ID.

User ID

Extension number for this line.

Password

Password for this line. Defaults to blank (no password required).

Auth ID

Authentication ID for SIP authentication. Defaults to blank.

Reversed Auth Realm

The IP address for an authentication realm other than the proxy IP address. The default value is blank; the proxy IP address is used as the authentication realm.

The parameter for extension 1 appears as follows in the phone configuration file:

## Configure NAT Support Parameters

Network Address Translation (NAT) allows multiple devices to share a single, public, routable, IP address to establish connections over the Internet. NAT is present in many broadband access devices to translate public and private IP addresses.

To configure NAT support parameters on the phone:

Step 1 Click Voice > SIP and navigate to NAT Support Parameters .

Step 2 Set a value to the parameter NAT Keep Alive Intvl .

Step 3 Enter the public IP address for your router.

Step 4 Click the Extension tab and navigate to NAT Settings .

Step 5 Set NAT Keep Alive Enable to Yes .

The service provider might require the phone to send NAT keep alive messages to keep the NAT ports open. Check with your service provider to determine the requirements.

Step 6 Click Submit All Changes .

Step 7 Configure the firewall settings on your router to allow SIP traffic. See the “Configure SIP” section .

| Parameter | Description |
|---|---|
| Max Forward | The number of proxies or gateways that can forward the request to the next downstream server. The Max-Forwards value is an integer in the range of 0 to 255 indicating the remaining number of times the request message is allowed to be forwarded. This count is decremented by each server that forwards the request. The initial value is 70. |
| Max Redirection | Number of times an invite can be redirected to avoid an infinite loop. The default is 5. |
| SIP User Agent Name | User-Agent header used in outbound requests. The default is $VERSION. If empty, the header is not included. Macro expansion of $A to $D corresponding to GPP_A to GPP_D allowed. |
| SIP Server Name | Server header used in responses to inbound responses. The default is $VERSION . |
| SIP Reg User Agent Name | User-Agent name used in a REGISTER request. If not specified, the SIP User Agent Name is used for the REGISTER request. |
| SIP Accept Language | The preferred languages for reason phrases, session descriptions, or status responses carried as message bodies in the response. If blank, the header is not included and the server assumes that all languages are acceptable to the client. Defaults to blank. |
| RFC 2543 Call Hold | If set to Yes , the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control includes Session Description Protocol (SDP) syntax c=0.0.0.0 when sending a SIP re-INVITE to a peer to hold the call. If set to No, the phone does not include the c=0.0.0.0 syntax in the SDP. With either setting, the phone includes a=sendonly syntax in the SDP. Defaults to Yes. |
| SIP TCP Port Min | Lowest TCP port number that can be used for SIP sessions. Defaults to 5060. |
| SIP TCP Port Max | Highest TCP port number that can be used for SIP sessions. Defaults to 5080. |
| Caller ID Header | Select from where the IP phone gets the caller ID: PAID-RPID-FROM PAID-FROM RPID-PAID-FROM RPID-FROM FROM header Defaults to PAID-RPID-FROM. |
| Max INVITE Retry Attempts | Maximum number of INVITE retry attempts by the phone. Defaults to 6. |
| Max NON-INVITE Retry Attempts | Maximum number of NON-INVITE retry attempts by the phone. Defaults to 6. |

| Parameter | Description |
|---|---|
| SIP T1 | RFC-3261 T1 value (RTT estimate). Ranges from 0 to 64 seconds. Defaults to 0.5 seconds. |
| SIP T2 | RFC-3261 T2 value, the maximum retransmit interval for non-INVITE requests and INVITE responses. Ranges from 0 to 64 seconds. Defaults to 4 seconds. |
| INVITE Expires | The length of time the INVITE is valid. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000. Defaults to 240 seconds. |
| ReINVITE Expires | ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000. Defaults to 30 |
| Reg Retry Intvl 1 | Interval to wait before the phone retries registration after failing during the previous registration. The range is from 1 to 2147483647. Do not enter 0. Defaults to 30 seconds. |
| Reg Retry Long Intvl | When registration fails with a SIP response code that does not match the Retry Reg response status code (RSC) value (see next table), the phone waits for this length of time before retrying. If this interval is 0, the phone stops trying. This value should be much larger than the Reg Retry Intvl value. The range is from 0 to 2147483647. Defaults to 1200 seconds. |
| Reg Retry Random Delay | Random delay added to the Register Retry Intvl value when retrying REGISTER after a failure. Minimum and maximum random delay to be added to the short timer. The range is from 0 to 2147483647. Defaults to 0, which disables this feature. |
| Reg Retry Long Random Delay | Random delay added to Register Retry Long Intvl value when retrying REGISTER after a failure. Minimum and maximum random delay to be added to the long timer. Random delay range (in seconds) to add to the Register Retry Long Intvl when retrying REGISTER after a failure. Defaults to 0, which disables this feature. |
| Reg Retry Intvl Cap | Reg_Retry_Intvl_Cap—Maximum value of the exponential delay. The maximum value to cap the exponential backoff retry delay (which starts at the Register Retry Intvl and doubles every retry). Defaults to 0, which disables the exponential backoff (that is, the error retry interval is always at the Register Retry Intvl). When this feature is enabled, the Reg Retry Random Delay is added to the exponential backoff delay value. The range is from 0 to 2147483647. |

| 1. The phone can use a RETRY-AFTER value when it is received from a SIP proxy server that is too busy to process a request (503 Service Unavailable message). If the response message includes a RETRY-AFTER header, the phone waits for the specified length of time before to REGISTER again. If a RETRY-AFTER header is not present, the phone waits for the value specified in the Reg Retry Interval or the Reg Retry Long Interval. |
|---|

| Parameter | Description |
|---|---|
| AVT Dynamic Payload | Any non-standard data. Both sender and receiver must agree on a number. Ranges from 96 to 127. Defaults to 101. |

| Parameter | Description |
|---|---|
| SIP Transport | Select from UDP , TCP or TLS . Defaults to UDP. |
| SIP Port | Port number of the SIP message listening and transmission port. Defaults to 5060. |
| SIP 100REL Enable | Support of 100REL SIP extension for reliable transmission of provisional responses (18x) and use of PRACK requests. Select Yes to enable. Defaults to No. |
| Auth Resync-Reboot | The Cisco Unified IP Conference Phone 8831 authenticates the sender when it receives a NOTIFY message with the following requests: resync reboot report restart XML-service Select Yes to enable. Defaults to Yes. |
| SIP Remote-Party-ID | The Remote-Party-ID header to use instead of the From header. Select Yes to enable. Defaults to Yes. |
| Refer-To Target Contact | Indicates the refer-to target. Select Yes to send the SIP Refer to the contact. Defaults to No. |
| SIP Debug Option | How SIP messages are received at or sent from the proxy listen port to the log. Select: Default—No messages. Current—Logs all the current SIP messages in full text Full—Logs all SIP messages in full text. |
| Sticky 183 | When enabled, the IP telephony ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound INVITE. To enable this feature, select Yes . Otherwise, select No . Defaults to No. |
| Auth INVITE | When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy. To enable this feature, select Yes . Defaults to No. |
| User Equal Phone | When a tel URL is converted to a SIP URL and the telephone number is represented by the user portion of the URL, the SIP URL includes the optional :user=phone parameter (RFC3261). For example: To: sip:+12325551234@example.com;user=phone To enable this optional parameter, select Yes . The default value is No. |

| Parameter | Description |
|---|---|
| Proxy | SIP proxy server and port number set by the service provider for all outbound requests. For example: 192.168.2.100:6060. The port number is optional. The default is port 5060. |
| Outbound Proxy | All outbound requests are sent as the first hop. Enter an IP address or domain name. |
| Alternate Proxy Alternate Outbound Proxy | This feature provides fast fallback when there is network partition at he Internet or when the primary proxy (or primary outbound proxy) is not responsive or available. The feature works well in a Verizon deployment environment as the alternate proxy is the Integrated Service Router (ISR) with analog outbound phone connection. Enter the proxy server addresses and port numbers in these fields. After the phone is registered to the primary proxy and the alternate proxy (or primary outbound proxy and alternate outbound proxy), the phone always sends out INVITE and Non-INVITE SIP messages (except registration) via the primary proxy. The phone always registers to both the primary and alternate proxies. If there is no response from the primary proxy after timeout (per the SIP RFC spec) for a new INVITE, the phone attempts to connect with the alternate proxy. The phone always tries the primary proxy first, and immediately tries the alternate proxy if the primary is unreachable. Active transactions (calls) never fall back between the primary and alternate proxies. If there is fallback for a new INVITE, the subscribe/notify transaction will fall back accordingly so that the phone's state can be maintained properly. You must also set Dual Registration in the Proxy and Registration section to Yes. |
| Register | Enables periodic registration with the proxy. This parameter is ignored if a proxy is not specified. To enable this feature, select Yes . Defaults to Yes. |
| Make Call Without Reg | Enables making outbound calls without successful (dynamic) registration by the phone. If set to no, the dial tone plays only when registration is successful. To enable this feature, select Yes . Defaults to No. |
| Register Expires | Defines how often the phone renews registration with the proxy. If the proxy responds to a REGISTER with a lower expires value, the phone renews registration based on that lower value instead of the configured value. If registration fails with an “Expires too brief” error response, the phone retries with the value specified in the Min-Expires header of the error. The range is from 32 to 2000000. Defaults to 3600 seconds. |
| Use DNS SRV | Enables DNS SRV lookup for the proxy and outbound proxy. To enable this feature, select Yes . Otherwise, select No . Defaults to No. |
| Proxy Fallback Intvl | Sets the delay after which the phone retries from the highest priority proxy (or outbound proxy) after it has failed over to a lower priority server. The phone should have the primary and backup proxy server list from a DNS SRV record lookup on the server name. It needs to know the proxy priority; otherwise, it does not retry. The range is from 0 to 65535. Defaults to 3600 seconds. |
| Dual Registration | Set to Yes to enable the Dual registration/Fast Fallback feature. To enable the feature you must also configure the alternate proxy/alternate outbound proxy fields in the Proxy and Registration section. |

| Parameter | Description |
|---|---|
| Display Name | Name displayed as the caller ID. |
| User ID | Extension number for this line. |
| Password | Password for this line. Defaults to blank (no password required). |
| Auth ID | Authentication ID for SIP authentication. Defaults to blank. |
| Reversed Auth Realm | The IP address for an authentication realm other than the proxy IP address. The default value is blank; the proxy IP address is used as the authentication realm. The parameter for extension 1 appears as follows in the phone configuration file: <Reversed_Auth_Realm_1_ ua="na"> </Reversed_Auth_Realm_1_> |