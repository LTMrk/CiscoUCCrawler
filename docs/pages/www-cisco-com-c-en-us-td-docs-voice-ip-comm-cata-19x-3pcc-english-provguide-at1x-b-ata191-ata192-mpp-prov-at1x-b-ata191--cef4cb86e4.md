---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-provguide-at1x-b-ata191-ata192-mpp-prov-at1x-b-ata191--cef4cb86e4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/provguide/at1x_b_ata191-ata192-mpp-prov/at1x_b_ata191-ata192-mpp-prov_chapter_0101.html
retrieved_at: 2026-08-22T01:05:27.671462+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Voice Parameters

## Chapter: Voice Parameters

- Voice Parameters

- Voice Parameter Numbering

- Voice Parameters

# Voice Parameters

## Voice Parameter Numbering

Certain types of parameters apply to multiple elements, such as users and lines. In the configuration file, the parameter
                              name is appended with a number, such as <Line_Enable_1> and <Line_Enable_2>. To understand this numbering system, use the
                              following key:

1—User 1 or Line1 (PHONE1 port)

2—User 2 or Line 2 (PHONE2 port)

FXS port 1 uses <Proxy_1_>

FXS port 2 used <Proxy_2_>

## Voice Parameters

<Restricted_Access_Domains>

Domain of the service provider to which the ATA is connected to. It prevents the ATA from connecting to other service providers.

<Enable_Web_Admin_Access>

This feature is not available in ATA web voice.

<IVR_Admin_Password>

Password for the administrator to manage the ATA by using the built-in IVR through a connected phone.

<Network_Startup_Delay>

The number of seconds of delay between restarting the voice module and initializing network interface.

Default setting—3

<DNS_Query_TTL_Ignore>

In DNS packages, the server will suggest a TTL value to the client; if this parameter is set to yes, the value from the server
                                          will be ignored.

Default setting—Yes

<Survivability_Test_Mode>

Determines whether the ATA will always register to the Local Survivability Gateway (LSG) nodes even though the Webex Calling
                                          Session Signaling Engine (SSE) nodes are reachable.

This test mode is used to verify the functions of the LSG nodes.

Default setting—No

<FIPS_Mode>

To enable the Federal Information Processing Standards (FIPS 140-3) mode on the ATA to meet the security requirements for
                                          cryptographic modules. Allowed values are Disabled and Enabled .

Default setting—Disabled

<TLS_Min_Version>

Select the minimum protocol version for the TLS connections.

Allowed values: TLS 1.0 , TLS 1.1 , TLS 1.2 , and TLS 1.3 .

Default setting—TLS 1.1

<Provision_Enable>

Controls all resync actions independently of firmware upgrade actions. Set to yes to enable remote provisioning.

Default setting—Yes

<Resync_On_Reset>

Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades.

Default setting—Yes

<Resync_Random_Delay>

The maximum value for a random time interval that the ATA waits before making its initial contact with the provisioning server.
                                          This delay is effective only on the initial configuration attempt following power-on or reset. The delay is a pseudorandom
                                          number between zero and this value. This parameter is in units of 20 seconds; the default value of 2 represents 40 seconds.

This feature is disabled when this parameter is set to zero. This feature can be used to prevent an overload of the provisioning
                                          server when a large number of devices power-on simultaneously.

Default setting—2 (40 seconds)

<Resync_At_HHmm>

The time of day when the device tries to resync. The resync is performed each day. Used in conjunction with the Resync At
                                          Random Delay.

Default setting—blank

<Resync_At_Random_Delay>

Used in conjunction with the Resync At (HHmm) setting, this parameter sets a range of possible values for the resync delay.
                                          The system randomly chooses a value from this range and waits the specified number of seconds before attempting to resync.
                                          This feature is intended to prevent the network jam that would occur if all resynchronizing devices began the resync at the
                                          exact same time of day.

Default setting—600

<Resync_Periodic>

The time interval between periodic resyncs with the provisioning server. The associated resync timer is active only after
                                          the first successful synchronization with the server. Setting this parameter to zero disables periodic resynchronization.

Default setting—3600 seconds

<Resync_Error_Retry_Delay>

Resync retry interval (in seconds) applied in case of resync failure. The ATA has an error retry timer that activates if the
                                          previous attempt to sync with the provisioning server fails. The ATA waits to contact the server again until the timer counts
                                          down to zero. This parameter is the value that is initially loaded into the error retry timer. If this parameter is set to
                                          zero, the ATA does not try to resync with the provisioning server following a failed attempt.

Default setting—3600 seconds

<Forced_Resync_Delay>

Maximum delay (in seconds) that the ATA waits before performing a resync. The ATA does not resync while one of its lines is
                                          active. Because a resync can take several seconds, it is desirable to wait until the ATA has been idle for an extended period
                                          before resynchronizing. This allows a user to make calls in succession without interruption. The ATA has a timer that begins
                                          counting down when all of its lines become idle. This parameter is the initial value of the counter.

Resync events are delayed until this counter decrements to zero.

Default setting—14400 seconds

<Resync_From_SIP>

Enables a resync to be triggered via a SIP NOTIFY message.

Default setting—yes

<Resync_After_Upgrade_Attempt>

Triggers a resync after every firmware upgrade attempt.

Default setting—Yes

<Resync_Trigger_1>

<Resync_Trigger_2>

Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE.

Default setting—blank

<Resync_Fails_On_FNF>

Determines whether a file-not-found response from the provisioning server constitutes a successful or a failed resync.

A failed resync activates the error resync timer.

Default setting—Yes

<Profile_Rule>

This parameter is a profile script that evaluates to the provisioning resync command. The command is a TCP/IP operation and
                                          an associated URL. The TCP/IP operation can be TFTP, HTTP, or HTTPS. If the command is not specified, TFTP is assumed, and
                                          the address of the TFTP server is obtained through DHCP option 66.

In the URL, either the IP address or the FQDN of the server can be specified. The file name can have macros, such as $MA,
                                          which expands to the ATA MAC address.

Default setting—/ata$PSN.cfg

<Profile_Rule_B>

<Profile_Rule_C>

<Profile_Rule_D>

Defines second, third, and fourth resync commands and associated profile URLs.

These profile scripts are executed sequentially after the primary Profile Rule resync operation has completed. If a resync
                                          is triggered and Profile Rule is blank, Profile Rule B, C, and D are still evaluated and executed.

Default setting—blank

<Log_Resync_Request_Msg>

This parameter contains the message that is sent to the Syslog server at the start of a resync attempt.

Default setting—$PN $MAC – Requesting resync $SCHEME://$SERVIP:$PORT$PATH

<Log_Resync_Success_Msg>

Syslog message issued upon successful completion of a resync attempt.

Default setting—$PN $MAC – Successful resync $SCHEME://$SERVIP:$PORT$PATH

<Log_Resync_Failure_Msg>

Syslog message issued after a failed resync attempt.

Default setting—$PN $MAC -- Resync failed: $ERR

<Report_Rule>

The target URL to which configuration reports are sent. This parameter has the same syntax as the Profile_Rule parameter,
                                          and resolves to a TCP/IP command with an associated URL.

A configuration report is generated in response to an authenticated SIP NOTIFY message, with Event: report. The report is
                                          an XML file containing the name and value of all the device parameters.

This parameter may optionally contain an encryption key.

For example:

[ --key $K ] tftp://ps.callhome.net/$MA/rep.xml.enc

Default setting—blank

<Upgrade_Enable>

Determines whether or not firmware upgrade operations can occur independently of resync actions.

Default setting—Yes

<Upgrade_Error_Retry_Delay>

The upgrade retry interval (in seconds) applied in case of upgrade failure. The ATA has a firmware upgrade error timer that
                                          activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next firmware
                                          upgrade attempt occurs when this timer counts down to zero.

Default setting—3600 seconds

<Downgrade_Rev_Limit>

Enforces a lower limit on the acceptable version number during a firmware upgrade or downgrade. The ATA does not complete
                                          a firmware upgrade operation unless the firmware version is greater than or equal to this parameter.

Default setting—blank

<Upgrade_Rule>

This parameter is a firmware upgrade script with the same syntax as Profile_Rule. Defines upgrade conditions and associated
                                          firmware URLs.

Default setting—blank

<Log_Upgrade_Request_Msg>

Syslog message issued at the start of a firmware upgrade attempt.

Default setting—$PN $MAC – Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH

<Log_Upgrade_Success_Msg>

Syslog message issued after a firmware upgrade attempt completes successfully.

Default setting—$PN $MAC – Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR

<Log_Upgrade_Failure_Msg>

Syslog message issued after a failed firmware upgrade attempt.

Default setting—$PN $MAC – Upgrade failed: $ERR

<License_Keys>

This field is not currently used.

<Custom_CA_URL>

The URL of a file location for a custom Certificate Authority (CA) certificate. Either the IP address or the FQDN of the server
                                          can be specified. The file name can have macros, such as $MA, which expands to the ATA MAC address.

Default setting—blank

<GPP_A> to <GPP_P>

General purpose provisioning parameters. These parameters can be used as variables in provisioning and upgrade rules. They
                                          are referenced by prepending the variable name with a ‘$’ character, such as $A for GPP_A.

Default setting—blank

<GPP_SA> to <GPP_SD>

The two-letter upper-case macro names SA through SD identify GPP_SA through GPP_SD as a special case when used as arguments
                                          of the key URL option.

<MIC_Cert_Refresh_Enable>

Controls whether to enable the MIC certificate renewal procedure.

Default setting—No

<MIC_Cert_Refresh_Rule>

HTTP URL for requesting the renewed MIC certificate from the SUDI server.

Default setting—http://sudirenewal.cisco.com/

<Max_Forward>

The maximum times a call can be forwarded. The valid range is from 1 to 255.

Default setting—70

<Max_Redirection>

Number of times an invite can be redirected to avoid an infinite loop.

Default setting—5.

<Max_Auth>

The maximum number of times (from 0 to 255) a request may be challenged.

Default setting—2

<SIP_User_Agent_Name>

The User-Agent header used in outbound requests. If empty, the header is not included. Macro expansion of $A to $D corresponding
                                          to GPP_A to GPP_D allowed.

Default setting—$VERSION

<SIP_Server_Name>

The server header used in responses to inbound responses.

Default setting—$VERSION

<SIP_Reg_User_Agent_Name>

The User-Agent name to be used in a REGISTER request. If this value is not specified, the SIP User Agent Name parameter is
                                          also used for the REGISTER request.

Default setting—blank

<SIP_Accept_Language>

Accept-Language header used. There is no default (this indicates that the ATA does not include this header) If empty, the
                                          header is not included.

Default setting—blank

<DTMF_Relay_MIME_Type>

The MIME Type used in a SIP INFO message to signal a DTMF event.

Default setting—application/dtmf-relay.

<Hook_Flash_MIME_Type>

The MIME Type used in a SIP INFO message to signal a hook flash event.

Default setting—application/hook-flash

<Remove_Last_Reg>

Determines whether or not the ATA removes the last registration before submitting a new one, if the value is different. Select
                                          yes to remove the last registration, or select no to omit this step.

Default setting—no

<Use_Compact_Header>

Determines whether or not the ATA uses compact SIP headers in outbound SIP messages. Select yes or no from the dropdown list.
                                          Select yes to use compact SIP headers in outbound SIP messages. Select no to use normal SIP headers. If inbound SIP requests
                                          contain compact headers, the ATA reuses the same compact headers when generating the response regardless the settings of the
                                          Use Compact Header parameter. If inbound SIP requests contain normal headers, the ATA substitutes those headers with compact
                                          headers (if defined by RFC 261) if Use Compact Header parameter is set to yes.

Default setting—no

<Escape_Display_Name>

Determines whether or not the Display Name is private. Select yes if you want the ATA to enclose the string (configured in
                                          the Display Name) in a pair of double quotes for outbound SIP messages. If the display name includes " or \, these will be
                                          escaped to \" and \\ within the double quotes. Otherwise, select no.

Default setting—no

<RFC_2543_Call_Hold>

Configures the type of call hold: a:sendonly or 0.0.0.0. Do not use the 0.0.0.0 syntax in a HOLD SDP; use the a:sendonly syntax.

Default setting—no

<Mark_all_AVT_Packets>

Select yes if you want all AVT tone packets (encoded for redundancy) to have the marker bit set for each DTMF event. Select
                                          no to have the marker bit set only for the first packet.

Default setting—yes

<SIP_TCP_Port_Min>

The lowest TCP port number that can be used for SIP sessions.

Default setting—5060

<SIP_TCP_Port_Max>

The highest TCP port number that can be used for SIP sessions.

Default setting—5080

<CTI_Enable>

Enables or disables the Computer Telephone Interface feature provided by some servers.

Default setting—no

<SIP_T1>

RFC 3261 T1 value (round-trip time estimate), which can range from 0 to 64 seconds.

Default setting—0.5

<SIP_T2>

RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses), which can range from 0 to 64
                                          seconds.

Default setting—4

<SIP_T4>

RFC 3261 T4 value (maximum duration a message remains in the network), which can range from 0 to 64 seconds.

Default setting—5

<SIP_Timer_B>

INVITE time-out value, which can range from 0 to 64 seconds.

Default setting—32

<SIP_Timer_F>

Non-INVITE time-out value, which can range from 0 to 64 seconds.

Default setting—32

<SIP_Timer_H>

H INVITE final response, time-out value, which can range from 0 to 64 seconds.

Default setting—32

<SIP_Timer_D>

ACK hang-around time, which can range from 0 to 64 seconds.

Default setting—32

<SIP_Timer_J>

Non-INVITE response hang-around time, which can range from 0 to 64 seconds.

Default setting—32

<INVITE_Expires>

INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Range: 0–(231–1)

Default setting—240

<ReINVITE_Expires>

ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Range: 0–(231–1)

Default setting—30

<Reg_Min_Expires>

Minimum registration expiration time allowed from the proxy in the Expires header or as a Contact header parameter. If the
                                          proxy returns a value less than this setting, the minimum value is used.

Default setting—1

<Reg_Max_Expires>

Maximum registration expiration time allowed from the proxy in the Min-Expires header. If the value is larger than this setting,
                                          the maximum value is used.

Default setting—7200

<Reg_Retry_Intvl>

Interval to wait before the ATA retries registration after failing during the last registration.

Default setting—30

<Reg_Retry_Long_Intvl>

When registration fails with a SIP response code that does not match Retry Reg RSC, the ATA waits for the specified length
                                          of time before retrying. If this interval is 0, the ATA stops trying. This value should be much larger than the Reg Retry
                                          Intvl value, which should not be 0.

Default setting—1200

<Reg_Retry_Random_Delay>

Random delay range (in seconds) to add to Register Retry Intvl when retrying REGISTER after a failure.

Default setting—0 (disabled)

<Reg_Retry_Long_Random_Delay>

Random delay range (in seconds) to add to Register Retry Long Intvl when retrying REGISTER after a failure.

Default setting—0 (disabled)

<Reg_Retry_Intvl_Cap>

The maximum value to cap the exponential back-off retry delay (which starts at Register Retry Intvl and doubles on every REGISTER
                                          retry after a failure) In other words, the retry interval is always at Register Retry Intvl seconds after a failure. If this
                                          feature is enabled, Reg Retry Random Delay is added on top of the exponential back-off adjusted delay value.

Default setting—0, which disables the exponential backoff

<SIT1_RSC>

<SIT2_RSC>

<SIT3_RSC>

<SIT4_RSC>

SIP response status code for the corresponding Special Information Tone (SIT), SIT1 through SIT4. For example, if you set
                                          the SIT1 RSC to 404, when the user makes a call and a failure code of 404 is returned, the SIT1 tone is played. Reorder or
                                          Busy tone is played by default for all unsuccessful response status code for SIT 1 RSC through SIT 4 RSC.

Default setting—blank

<Try_Backup_RSC>

SIP response code that retries a backup server for the current request.

Default setting—blank

<Retry_Reg_RSC>

Interval to wait before the ATA retries registration after failing during the last registration.

Default setting—blank

<RTP_Port_Min>

Minimum port number for RTP transmission and reception. The RTP Port Min and RTP Port Max parameters should define a range
                                          that contains at least 4 even number ports, such as 100 –106.

Default setting—16384.

<RTP_Port_Max>

Maximum port number for RTP transmission and reception.

Default setting—16482.

<RTP_Packet_Size>

Packet size in seconds, which can range from 0.01 to 0.16. Valid values must be a multiple of 0.01 seconds.

Default setting—0.030

<Max_RTP_ICMP_Err>

Number of successive ICMP errors allowed when transmitting RTP packets to the peer before the ATA terminates the call. If
                                          value is set to 0, the ATA ignores the limit on ICMP errors.

Default setting—0

<RTCP_Tx_Interval>

Interval for sending out RTCP sender reports on an active connection. It can range from 0 to 255 seconds. During an active
                                          connection, the ATA can be programmed to send out compound RTCP packet on the connection. Each compound RTP packet except
                                          the last one contains a SR (Sender Report) and a SDES (Source Description) The last RTCP packet contains an additional BYE
                                          packet. Each SR except the last one contains exactly 1 RR (Receiver Report); the last SR carries no RR. The SDES contains
                                          CNAME, NAME, and TOOL identifiers. The CNAME is set to <User ID>@<Proxy>, NAME is set to <Display Name> (or Anonymous if user
                                          blocks caller ID), and TOOL is set to the Vendor/Hardwareplatform-softwareversion. The NTP timestamp used in the SR is a snapshot
                                          of the local time for the ATA, not the time reported by an NTP server. If the ATA receives a RR from the peer, it attempts
                                          to compute the round trip delay and show it as the Call Round Trip Delay value (ms) on the Information page.

Default setting—0

<No_UDP_Checksum>

Select yes if you want the ATA to calculate the UDP header checksum for SIP messages. Otherwise, select no.

Default setting—no

<Stats_In_BYE>

Determines whether the ATA includes the PRTP-Stat header or response in a BYE message. The header contains the RTP statistics
                                          of the current call. Select yes or no from the dropdown list.

Default setting—yes

The format of the P-RTP-Stat header is:

P-RTP-State: PS=<packets sent>,OS=<octets sent>,PR=<packets received>,OR=<octets eceived>,PL=<packets lost>,JI=<jitter in
                                          ms>,LA=<delay in ms>,DU=<call durationins>,EN=<encoder>,DE=<decoder>.

<NSE_Dynamic_Payload>

NSE dynamic payload type. The valid range is 96-127.

Default setting—100

<AVT_Dynamic_Payload>

AVT dynamic payload type. The valid range is 96-127.

Default setting—101

<INFOREQ_Dynamic_Payload>

INFOREQ dynamic payload type.

Default setting—blank

<G726r32_Dynamic_Payload>

G726r32 dynamic payload type.

Default setting—2

<EncapRTP_Dynamic_Payload>

EncapRTP Dynamic Payload type.

Default setting—112

<RTP-Start-Loopback_Dynamic_Payload>

RTP-Start-Loopback Dynamic Payload type.

Default setting—113

<RTP-Start-Loopback_Codec>

RTP-Start-Loopback Codec. Select one of the following: G711u, G711a, G726-32, G729a.

Default setting—G711u

<NSE_Codec_Name>

NSE codec name used in SDP.

Default setting—NSE

<AVT_Codec_Name>

AVT codec name used in SDP.

Default setting—telephone-event

<G711u_Codec_Name>

G.711u codec name used in SDP.

Default setting—PCMU

<G711a_Codec_Name>

G.711a codec name used in SDP.

Default setting—PCMA

<G726r32_Codec_Name>

G.726-32 codec name used in SDP.

Default setting—G726-32

<G729a_Codec_Name>

G.729a codec name used in SDP.

Default setting—G729a

<G722_Codec_Name> G.722 codec name used in SDP.

Default setting—G722

<EncapRTP_Codec_Name>

EncapRTP codec name used in SDP.

Default setting—encaprtp

<Handle_VIA_received>

If you select yes, the ATA processes the received parameter in the VIA header (this value is inserted by the server in a response
                                          to any one of its requests) If you select no, the parameter is ignored. Select yes or no from the drop-down menu.

Default setting—no

<Handle_VIA_rport>

If you select yes, the ATA processes the rport parameter in the VIA header (this value is inserted by the server in a response
                                          to any one of its requests) If you select no, the parameter is ignored. Select yes or no from the drop-down menu.

Default setting—no

<Insert_VIA_received>

Inserts the received parameter into the VIA header of SIP responses if the receivedfrom IP and VIA sent-by IP values differ.
                                          Select yes or no from the drop-down menu.

Default setting—no

<Insert_VIA_rport>

Inserts the rport parameter into the VIA header of SIP responses if the receivedfrom IP and VIA sent-by IP values differ.
                                          Select yes or no from the drop-down menu.

Default setting—no

<Substitute_VIA_Addr>

Lets you use NAT-mapped IP:port values in the VIA header. Select yes or no from the drop-down menu.

Default setting—no

<Send_Resp_To_Src_Port>

Sends responses to the request source port instead of the VIA sent-by port. Select yes or no from the drop-down menu.

Default setting—no

<STUN_Enable>

Enables the use of STUN to discover NAT mapping. Select yes or no from the dropdown menu.

Default setting—no

<STUN_Test_Enable>

If the STUN Enable feature is enabled and a valid STUN server is available, the ATA can perform a NAT-type discovery operation
                                          when it powers on. It contacts the configured STUN server, and the result of the discovery is reported in a Warning header
                                          in all subsequent REGISTER requests. If the ATA detects symmetric NAT or a symmetric firewall, NAT mapping is disabled.

Default setting—no

<STUN_Server>

IP address or fully-qualified domain name of the STUN server to contact for NAT mapping discovery.

Default setting—blank

<EXT_IP>

External IP address to substitute for the actual IP address of the ATA in all outgoing SIP messages. If 0.0.0.0 is specified,
                                          no IP address substitution is performed. If this parameter is specified, the ATA assumes this IP address when generating SIP
                                          messages and SDP (if NAT Mapping is enabled for that line) However, the results of STUN and VIA received parameter processing,
                                          if available, supersede this statically configured value. This option requires that you have (1) a static IP address from
                                          your Internet Service Provider and (2) an edge device with a symmetric NAT mechanism. If the ATA is the edge device, the second
                                          requirement is met.

Default setting—blank

<EXT_RTP_Port_Min>

External port mapping number of the RTP Port Min. number. If this value is not zero, the RTP port number in all outgoing SIP
                                          messages is substituted for the corresponding port value in the external RTP port range.

Default setting—blank

<NAT_Keep_Alive_Intvl>

Interval between NAT-mapping keep alive messages.

Default setting—15

<Redirect_Keep_Alive>

Interval between NAT Redirect keep alive messages.

Default setting—15

<Line_Enable_1>

<Line_Enable_2>

To enable this line for service, select yes. Otherwise, select no.

Default setting—yes

<SAS_Enable_1>

<SAS_Enable_2>

To enable the use of the line as a streaming audio source, select yes. Otherwise, select no. If enabled, the line cannot be
                                          used for outgoing calls. Instead, it auto-answers incoming calls and streams audio RTP packets to the caller.

Default setting—no

<SAS_DLG_Refresh_Intvl_1>

<SAS_DLG_Refresh_Intvl_2>

If this value is not zero, it is the interval at which the streaming audio server sends out session refresh (SIP re-INVITE)
                                          messages to determine whether the connection to the caller is still active. If the caller does not respond to the refresh
                                          message, the ATA ends this call with a SIP BYE message. The range is 0 to 255 seconds (0 means that the session refresh is
                                          disabled.)

Default setting—30

<SAS_Inbound_RTP_Sink_1>

<SAS_Inbound_RTP_Sink_2>

The purpose of this parameter is to work around devices that do not play inbound RTP if the SAS line declares itself as a
                                          send-only device and tells the client not to stream out audio. This parameter is an FQDN or IP address of an RTP sink to be
                                          used by the SAS line in the SDP of its 200 response to inbound INVITE from a client. It will appear in the c = line and the
                                          port number, if specified, will appear in the m = line of the SDP. If this value is not specified or is equal to 0, then c
                                          =0.0.0.0 and a=sendonly will be used in the SDP to tell the SAS client to not to send any RTP to this SAS line. If a non-zero
                                          value is specified, then a=sendrecv and the SAS client will stream audio to the given address. Special case: If the value
                                          is $IP, then the SAS line’s own IP address is used in the c = line and a=sendrecv. In that case the SAS client will stream
                                          RTP packets to the SAS line.

Default setting—blank

<NAT_Mapping_Enable_1>

<NAT_Mapping_Enable_2>

To use externally mapped IP addresses and SIP/RTP ports in SIP messages, select yes. Otherwise, select no.

Default setting—no

<NAT_Keep_Alive_Enable_1>

<NAT_Keep_Alive_Enable_2>

To send the configured NAT keep alive message periodically, select yes. Otherwise, select no.

Default setting—no

<NAT_Keep_Alive_Msg_1>

<NAT_Keep_Alive_Msg_2>

Enter the keep alive message that should be sent periodically to maintain the current NAT mapping. If the value is $NOTIFY,
                                          a NOTIFY message is sent. If the value is $REGISTER, a REGISTER message without contact is sent.

Default setting—$NOTIFY

<NAT_Keep_Alive_Dest_1>

<NAT_Keep_Alive_Dest_2>

Destination that should receive NAT keep alive messages. If the value is $PROXY, the messages are sent to the current proxy
                                          server or outbound proxy server.

Default setting—$PROXY

<Blind_Attn-Xfer_Enable_1>

<Blind_Attn-Xfer_Enable_2>

Enables the ATA to perform an attended transfer operation by ending the current call leg and performing a blind transfer of
                                          the other call leg. If this feature is disabled, the ATA performs an attended transfer operation by referring the other call
                                          leg to the current call leg while maintaining both call legs. To use this feature, select yes. Otherwise, select no.

Default setting—no

<MOH_Server_1>

<MOH_Server_2>

User ID or URL of the auto-answering streaming audio server. When only a user ID is specified, the current or outbound proxy
                                          is contacted. Music-on-hold is disabled if the MOH Server is not specified.

Default setting—blank

<Xfer_When_Hangup_Conf_1>

<Xfer_When_Hangup_Conf_2>

Makes the ATA perform a transfer when a conference call has ended. Select yes or no from the drop-down menu.

Default setting—yes

<Conference_Bridge_URL_1>

<Conference_Bridge_URL_2>

This feature supports external conference bridging for n-way conference calls (n>2), instead of mixing audio locally. To use
                                          this feature, set this parameter to that of the server's name. For example: conf@mysefver.com:12345 or conf (which uses the
                                          Proxy value as the domain).

Default setting—blank

<Conference_Bridge_Ports_1>

<Conference_Bridge_Ports_2>

Select the maximum number of conference call participants. The range is 3 to 10.

Default setting—3

<Enable_IP_Dialing_1>

<Enable_IP_Dialing_2>

Enable or disable IP dialing. If IP dialing is enabled, one can dial [userid@] a.b.c.d[:port], where

‘@’, ‘.’, and ‘:’ are dialed by entering *

user-id must be numeric (like a phone number)

a, b, c, d must be between 0 and 255

port must be larger than 255. If port is not given, 5060 is used.

Port and User-Id are optional. If the user-id portion matches a pattern in the dial plan, then it is interpreted as a regular
                                          phone number according to the dial plan. The INVITE message, however, is still sent to the outbound proxy if it is enabled.

Default setting—no

<Emergency_Number_1>

<Emergency_Number_2>

Comma separated list of emergency number patterns. If outbound call matches one of the pattern, the ATA will disable hook
                                          flash event handling. The condition is restored to normal after the call ends. Blank signifies that there is no emergency
                                          number. Maximum number length is 63 characters.

Default setting—blank

<Mailbox_ID_1>

<Mailbox_ID_2>

Enter the ID number of the mailbox for this line.

Default setting—blank

<Feature_Key_Sync_1>

Allows the phone to synchronize with the call server. If Do Not Disturb or Call Forwarding settings are changed on the phone,
                                          the changes are also made on the server. If changes are made on the server, they are propagated to the phone.

Default setting: no

<Secure_Call_Option_1>

<Secure_Call_Option_2>

Configures a line to only accept secure calls. Options are:

Optional: Retains the current secure call option for the phone adapter.

Strict: Allows SRTP only when SIP transport is set to TLS and if the ATA receives an unsecure call, the call fails. Allows
                                          RTP only when SIP transport is UDP/TCP and if the ATA receives an unsecure call, the call fails.

Default setting: Optional

<Company_UUID_1>

<Company_UUID_2>

The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider.

For example:

19c8168c-a366-44b5-853c-960fcaa19592

Allowed values: Maximum identifier length is 128 characters.

Default setting—blank

<Primary_Request_URL_1>

<Primary_Request_URL_2>

URL of the primary location server that provides the emergency call services.

The location server returns an HELD response to the phone with the requested location URI that is tied to the user phone IP
                                          address.

This parameter must be in the form of a valid HTTP or HTTPS URL.

Allowed values: A valid URL not exceeding 255 characters.

Default setting—blank

<Secondary_Request_URL_1>

<Secondary_Request_URL_2>

URL of the backup server to obtain the user's phone location.

If the primary request URL fails, ATA tries to send the secondary request URL to the emergency call services provider.

This parameter must be in the form of a valid HTTP or HTTPS URL.

Allowed values: A valid URL not exceeding 255 characters.

Default setting—blank

<Proxy_1>

<Proxy_2>

SIP proxy server for all outbound requests.

Default setting—blank

<Outbound_Proxy_1>

<Outbound_Proxy_2>

SIP Outbound Proxy Server where all outbound requests are sent as the first hop.

Default setting—blank

<Survivability_Proxy_1>

<Survivability_Proxy_2>

Specifies a DNS A record of the Local Survivability Gateway (LSG) nodes.

String syntax:

```
hostname[:port][:p=priority][:w=weight][:A=ip-list]
[| hostname2[:port][:p=priority][:w=weight][:A=ip-list]]
```

```
ip-list: ip-addr[,ip-addr[,ip-addr…]]
```

Default setting—blank

<Use_Outbound_Proxy_1>

<Use_Outbound_Proxy_2>

Enables the use of an Outbound Proxy. If set to no, the Outbound Proxy and Use OB Proxy in Dialog parameters are ignored.

Default setting—no

<Use_OB_Proxy_In_Dialog_1> through <Use_OB_Proxy_In_Dialog_2>

Whether to force SIP requests to be sent to the outbound proxy within a dialog. Ignored if the parameter Use Outbound Proxy
                                          is no, or the Outbound Proxy parameter is empty.

Default setting—yes

<Register_1>

<Register_2>

Enable periodic registration with the Proxy parameter. This parameter is ignored if Proxy is not specified.

Default setting—yes

<Make_Call_Without_Reg_1>

<Make_Call_Without_Reg_2>

Allow making outbound calls without successful (dynamic) registration by the unit. If No, dial tone will not play unless registration
                                          is successful.

Default setting—no

<Register_Expires_1>

<Register_Expires_2>

Expires value in sec in a REGISTER request. The ATA will periodically renew registration shortly before the current registration
                                          expired. This parameter is ignored if the Register parameter is no.

Range: 0 – (231 – 1) sec.

Default setting—3600

<Ans_Call_Without_Reg_1>

<Ans_Call_Without_Reg_2>

Allow answering inbound calls without successful (dynamic) registration by the unit.

Default setting—no

<Use_DNS_SRV_1>

<Use_DNS_SRV_2>

Whether to use DNS SRV lookup for Proxy and Outbound Proxy.

Default setting—no

<DNS_SRV_Auto_Prefix_1>

<DNS_SRV_Auto_Prefix_2>

If enabled, the ATA will automatically prepend the Proxy or Outbound Proxy name with _sip._udp when performing a DNS SRV lookup
                                          on that name.

Default setting—no

<Proxy_Fallback_Intvl_1>

<Proxy_Fallback_Intvl_2>

After failing over to a lower priority server, the ATA waits for the specified Proxy Fallback Interval, in seconds, before
                                          retrying the highest priority proxy (or outbound proxy) servers. This parameter is useful only if the primary and backup proxy
                                          server list is provided to the ATA via DNS SRV record lookup on the server name.

Using multiple DNS A records per server name does not allow the notion of priority, so all hosts will be considered at the
                                          same priority and the ATA will not attempt to fall back after a failover.

If the value is 0, the SIP proxy fallback feature is disabled.

Default setting—3600

<Survivability_Proxy_Fallback_Intvl_1>

<Survivability_Proxy_Fallback_Intvl_2>

Specifies the interval (in seconds) after which the ATA will try to fallback to the SSE nodes.

Default setting—30 seconds

<Proxy_Redundancy_Method_1>

<Proxy_Redundancy_Method_2>

The method that the ATA uses to create a list of proxies returned in the DNS SRV records. If you select Normal, the list will
                                          contain proxies ranked by weight and priority. If you select Based on SRV port, the ATA also inspects the port number based
                                          on 1st proxy’s port.

Default setting—Normal

<Mailbox_Subscribe_URL_1>

<Mailbox_Subscribe_URL_2>

The URL or IP address of the voicemail server.

Default setting—blank

<Mailbox_Subscribe_Expires_1>

<Mailbox_Subscribe_Expires_2>

The subscription interval for voicemail message waiting indication. When this time period expires, the ATA sends another subscribe
                                          message to the voice mail server.

Default: 2147483647

<Display_Name_1>

<Display_Name_2>

Display name for caller ID.

Default setting—blank

<User_ID_1>

<User_ID_2>

User ID for this line.

Default setting—blank

<Password_1>

<Password_2>

Password for this line.

Default setting—blank

<Use_Auth_ID_1>

<Use_Auth_ID_2>

To use the authentication ID and password for SIP authentication, select yes. Otherwise, select no to use the user ID and
                                          password.

Default setting—no

<Auth_ID_1>

<Auth_ID_2>

Authentication ID for SIP authentication.

Default setting—blank

<Reversed_Auth_Realm_1>

<Reversed_Auth_Realm_2>

Specify a realm that is used for the authentications of the INVITE and NOTIFY requests.

Default setting—blank

<Resident_Online_Number_1>

<Resident_Online_Number_2>

This setting allows you to associate a "local" telephone number with this line using a valid Skype Online Number from Skype.
                                          Calls made to that number will ring your phone. Enter the number without spaces or special characters.

Default setting—blank

<SIP URI>

The SIP URI, in the following format:

sip:<username>@<WAN_IP>:<port> or

sip:<username>@<domain>:<port>

<Call_Waiting_Serv_1>

<Call_Waiting_Serv_2>

Enable Call Waiting Service.

Default setting—yes

<Block_CID_Serv_1>

<Block_CID_Serv_2>

Enable Block Caller ID Service.

Default setting—yes

<Block_ANC_Serv_1>

<Block,_ANC_Serv_2>

Enable Block Anonymous Calls Service.

Default setting—yes

<Dist_Ring_Serv_1>

<Dist_Ring_Serv_2>

Enable Distinctive Ringing Service.

Default setting—yes

<Cfwd_All_Serv_1>

<Cfwd_All_Serv_2>

Enable Call Forward All Service.

Default setting—yes

<Cfwd_Busy_Serv_1>

<Cfwd_Busy_Serv_2>

Enable Call Forward Busy Service.

Default setting—yes

<Cfwd_No_Ans_Serv_1>

<Cfwd_No_Ans_Serv_2>

Enable Call Forward No Answer Service.

Default setting—yes

<Cfwd_Sel_Serv_1>

<Cfwd_Sel_Serv_2>

Enable Call Forward Selective Service.

Default setting—yes

<Cfwd_Last_Serv_1>

<Cfwd_Last_Serv_2>

Enable Forward Last Call Service

Default setting—yes

<Block_Last_Serv_1>

<Block_Last_Serv_2>

Enable Block Last Call Service.

Default setting—yes

<Accept_Last_Serv_1>

<Accept_Last_Serv_2>

Enable Accept Last Call Service.

Default setting—yes

<DND_Serv_1>

<DND_Serv_2>

Enable Do Not Disturb Service.

Default setting—yes

<CID–Serv_1>

<CID–Serv_2>

Enable Caller ID Service.

Default setting—yes

<CWCID_Serv_1>

<CWCID_Serv_2>

Enable Call Waiting Caller ID Service.

Default setting—yes

<Call_Return_Serv_1>

<Call_Return_Serv_2>

Enable Call Return Service.

Default setting—yes

<Call_Redial_Serv_1>

<Call_Redial_Serv_2>

Enable Call Redial Service.

<Call_Back_Serv_1>

<Call_Back_Serv_2>

Enable Call Back Service.

<Three_Way_Call_Serv_1>

<Three_Way_Call_Serv_2>

Enable Three Way Calling Service. Three Way Calling is required for Three Way Conference and Attended Transfer.

Default setting—yes

<Three_Way_Conf_Serv_1>

<Three_Way_Conf_Serv_2>

Enable Three Way Conference Service.

Three Way Conference is required for Attended Transfer.

Default setting—yes

<Attn_Transfer_Serv_1>

<Attn_Transfer_Serv_2>

Enable Attended Call Transfer Service.

Three Way Conference is required for Attended Transfer.

Default setting—yes

<Unattn_Transfer_Serv_1>

<Unattn_Transfer_Serv_2>

Enable Unattended (Blind) Call Transfer Service.

Default setting—yes

<MWI_Serv_1>

<MWI_Serv_2>

Enable MWI Service. MWI is available only if a Voice Mail Service is set-up in the deployment.

Default setting—yes

<VMWI_Serv_1>

<VMWI_Serv_2>

Enable VMWI Service (FSK)

Default setting—yes

<Speed_Dial_Serv_1>

<Speed_Dial_Serv_2>

Enable Speed Dial Service.

Default setting—yes

<Secure_Call_Serv_1>

<Secure_Call_Serv_2>

Secure Call Service. If this feature is enabled, a user can make a secure call by entering an activation code (*18 by default)
                                          before dialing the target number. Then audio traffic in both directions is encrypted for the duration of the call.

Default setting—yes

<Referral_Serv_1>

<Referral_Serv_2>

Enable Referral Service. See the Referral Services Codes parameter for more information.

Default setting—yes

<Feature_Dial_Serv_1>

<Feature_Dial_Serv_2>

Enable Feature Dial Service. See the Feature Dial Services Codes parameter for more information.

Default setting—yes

<Service_Announcement_Serv_1>

<Service_Announcement_Serv_2>

Enable Service Announcement Service.

Default setting—no

<Reuse_CID_Number_As_Name_1>

<Reuse_CID_Number_As_Name_2>

Use the Caller ID number as the caller name.

Default settings: yes

<Preferred_Codec_1>,  <Preferred_Codec_2>

<Second_Preferred_Codec_1>, <Second_Preferred_Codec_2>

<Third_Preferred_Codec_1>, <Third_Preferred_Codec_2>

Up to three codecs to be used for all calls from the specified line/handset, listed order of preference. The actual codec
                                          used in a call depends on the outcome of the codec negotiation protocol. Select one of the following: G711u, G711a, G726-32,
                                          G729a, or G722.

Default setting for Preferred Codec: G711u

Default setting for Second and Third Preferred Codec: Unspecified

<Use_Pref_Codec_Only_1>

<Use_Pref_Codec_Only_2>

To use only the preferred codec for all calls, select yes. (The call fails if the far end does not support this codec.) Otherwise,
                                          select no.

Default setting—no

<Use_Remote_Pref_Codec_1>

<Use_Remote_Pref_Codec_2>

To use the preferred codec specified by the remote peer, select yes. Otherwise, select no.

Default setting:

<Codec_Negotiation_1>

<Codec_Negotiation_2>

Specify the codecs for codec negotiation:

Default or List All.

Default setting—Default

<G729a_Enable_1>

<G729a_Enable_2>

To enable the use of the G.729a codec at 8 kbps, select yes. Otherwise, select no.

Default setting—yes

<Silence_Supp_Enable_1>

<Silence_Supp_Enable_2>

To enable silence suppression so that silent audio frames are not transmitted, select yes. Otherwise, select no.

Default setting—no

<G726-32_Enable_1>

<G726-32_Enable_2>

To enable the use of the G.726 codec at 32 kbps, select yes. Otherwise, select no.

Default setting—yes

<Silence_Threshold_1>

<Silence_Threshold_2>

Select the appropriate setting for the threshold: high, medium, or low.

Default setting—medium

<FAX_V21_Detect_Enable_1>

<FAX_V21_Detect_Enable_2>

To enable detection of V21 fax tones, select yes. Otherwise, select no.

Default setting—yes

<Echo_Canc_Enable_1>

<Echo_Canc_Enable_2>

To enable the use of the echo canceller, select yes. Otherwise, select no.

Default setting—yes

<FAX_CNG_Detect_Enable_1>

<FAX_CNG_Detect_Enable_2>

To enable detection of the fax Calling Tone (CNG), select yes. Otherwise, select no.

Default setting—yes

<FAX_Passthru_Codec_1>

<FAX_Passthru_Codec_2>

Select the codec for fax passthrough, G711u or G711a.

Default setting—G711u

<FAX_Codec_Symmetric_1> through <FAX_Codec_Symmetric_2>

To force the ATA to use a symmetric codec during fax passthrough, select yes. Otherwise, select no.

Default setting—yes

<DTMF_Process_INFO_1>

<DTMF_Process_INFO_2>

To use the DTMF process info feature, select yes. Otherwise, select no.

Default setting—yes

<FAX_Passthru_Method_1>

<FAX_Passthru_Method_2>

Select the fax passthrough method: None, NSE, or ReINVITE.

Default setting—NSE

<DTMF_Process_AVT_1>

<DTMF_Process_AVT_2>

To use the DTMF process AVT feature, select yes. Otherwise, select no.

Default setting—yes

<FAX_Process_NSE_1>

<FAX_Process_NSE_2>

To use the fax process NSE feature, select yes. Otherwise, select no.

Default setting—yes

<DTMF_Tx_Method_1>

<DTMF_Tx_Method_2>

Select the method to transmit DTMF signals to the far end: InBand, AVT, INFO, or Auto. InBand sends DTMF by using the audio
                                          path. AVT sends DTMF as AVT events. INFO uses the SIP INFO method. Auto uses InBand or AVT based on the outcome of codec negotiation.

Default setting—Auto

<FAX_Disable_ECAN_1>

<FAX_Disable_ECAN_2>

If enabled, this feature automatically disables the echo canceller when a fax tone is detected. To use this feature, select
                                          yes. Otherwise, select no.

Default setting—no

<DTMF_Tx_Mode_1>

<DTMF_Tx_Mode_2>

DTMF Detection Tx Mode is available for SIP information and AVT. Options are: Strict or Normal.

Default setting—Strict for which the following are true:

A DTMF digit requires an extra hold time after detection.

The DTMF level threshold is raised to -20 dBm.

The minimum and maximum duration thresholds are:

strict mode for AVT: 70 ms

normal mode for AVT: 40 ms

strict mode for SIP info: 90 ms

normal mode for SIP info: 50 ms

<DTMF_Tx_Strict_Hold_Off_Time_1>

<DTMF_Tx_Strict_Hold_Off_Time_2>

This parameter is in effect only when DTMF Tx Mode is set to strict, and when DTMF Tx Method is set to out-ofband; i.e. either
                                          AVT or SIP-INFO. The value can be set as low as 40 ms. There is no maximum limit. A larger value will reduce the chance of
                                          talk-off (beeping) during conversation, at the expense of reduced performance of DTMF detection, which is needed for interactive
                                          voice response systems (IVR).

Default: 70 ms

<FAX_Enable_T38_1>

<FAX_Enable_T38_2>

To enable the use of ITU-T T.38 standard for FAX Relay, select yes. Otherwise select no.

Default setting—no

<Hook_Flash_Tx_Method_1>

<Hook_Flash_Tx_Method_2>

Select the method for signaling hook flash events: None, AVT, or INFO. None does not signal hook flash events. AVT uses RFC2833
                                          AVT (event = 16) INFO uses SIP INFO with the single line signal=hf in the message body. The MIME type for this message body
                                          is taken from the Hook Flash MIME Type setting.

Default setting—None

<FAX_T38_Redundancy_1>

<FAX_T38_Redundancy_2>

Select the appropriate number to indicate the number of previous packet payloads to repeat with each packet. Choose 0 for
                                          no payload redundancy. The higher the number, the larger the packet size and the more bandwidth consumed.

Default setting—1

<FAX_T38_ECM_Enable_1>

<FAX_T38_ECM_Enable_2>

Select yes to enable T.38 Error Correction Mode. Otherwise select no.

Default setting—yes

<FAX_Tone_Detect_Mode_1>

<FAX_Tone_Detect_Mode_2>

This parameter has three possible values:

caller or callee: The ATA will detect FAX tone whether it is callee or caller

caller only: The ATA will detect FAX tone only if it is the caller

callee only: The ATA will detect FAX tone only if it is the callee

Default setting—caller or callee.

<Symmetric_RTP_1>

<Symmetric_RTP_2>

Enable symmetric RTP operation. If enabled, the ATA sends RTP packets to the source address and port of the last received
                                          valid inbound RTP packet. If disabled (or before the first RTP packet arrives) the ATA sends RTP to the destination as indicated
                                          in the inbound SDP.

Default setting—no

<FAX_T38_Return_to_Voice_1>

<FAX_T38_Return_to_Voice_2>

When this feature is enabled, upon completion of the fax image transfer, the connection remains established and reverts to
                                          a voice call using the previously designated codec. Select yes to enable this feature, or select no to disable it.

Default setting—no

<Dial_Plan_1>

<Dial_Plan_2>

The allowed number patterns for outbound calls. The default dial plan script for the line is as follows: (*xx|[3469]11|0|00|[2-9]xxxxxx|1xxx[2-9]xxxxxx|xxxxxxxxxxxx.)

Each parameter is separated by a semicolon (;)

Examples of Dial Plan Entry and Functionality

International Operator

<Encryption_Method_1>

<Encryption_Method_2>

Select the encryption algorithm for the SRTP sessions (secure calls).

Allowed values: AES 128 and AES 256 GCM .

Default setting—AES 128

<Gateway_1_1

<Gateway_4_1>

The first of 4 gateways that can be specified to be used in the <Dial Plan> to facilitate call routing specification (that
                                          overrides the given proxy information). This gateway is represented by gw1 in the <Dial Plan>. For example, the rule 1408xxxxxxx<:@gw1>
                                          can be added to the dial plan such that when the user dials 1408+7digits, the call will be routed to Gateway 1. Without the
                                          <:@gw1> syntax, all calls are routed to the given proxy by default (except IP dialing).

Default setting—blank

<GW1_NAT_Mapping_Enable_1>

<GW4_NAT_Mapping_Enable_1>

If enabled, the ATA uses NAT mapping when contacting Gateway 1.

Default setting—no

<GW1_Auth_ID_1_ >

<GW4_Auth_ID_1_ >

This value is the authentication user-id to be used by the ATA to authenticate itself to Gateway 1.

Default setting—blank

<GW1_Password_1>

<GW4_Password_1>

This value is the password to be used by the ATA to authenticate itself to Gateway 1.

Default setting—blank

<Auto_PSTN_Fallback_1>

<Auto_PSTN_Fallback_2>

If enabled, the ATA automatically routes all calls to the PSTN gateway when the SIP proxy is down (registration failure or
                                          network link down).

Default setting—yes

<Cfwd_No_Ans_Dest_1>

<Cfwd_No_Ans_Dest_2>

Forward number for Call Forward No Answer Service. Same as Cfwd All Dest.

Default setting—blank

<Cfwd_No_Ans_Delay_1>

<Cfwd_No_Ans_Delay_2>

Delay in sec before Call Forward No Answer triggers. Same as Cfwd All Dest.

Default setting—20

<Idle_Polarity_1>

<Idle_Polarity_2>

Polarity before a call is connected: Forward or Reverse.

Default setting—Forward

<Caller_Conn_Polarity_1>

<Caller_Conn_Polarity_2>

Polarity after an outbound call is connected: Forward orReverse.

Default setting—Forward.

<Callee_Conn_Polarity_1>

<Callee_Conn_Polarity_2>

Polarity after an inbound call is connected: Forward or Reverse.

Default setting—Forward

<Cfwd_All_Dest_1>

<Cfwd_All_Dest_2>

Forward number for Call Forward All Service.

Default setting—blank

<Cfwd_Busy_Dest_1>

<Cfwd_Busy_Dest_2>

Forward number for Call Forward Busy Service. Same as Cfwd All Dest.

Default setting—blank

<Cfwd_Sel1_Caller_1>,  <Cfwd_Sel8_Caller_1>

<Cfwd_Sel1_Caller_1>, <Cfwd_Sel8_Caller_2>

Caller number pattern to trigger Call Forward Selective service. When the caller’s phone number matches the entry, the call
                                          is forwarded to the corresponding Cfwd Selective Destination (Cfwd Sel1-8 Dest).

Use ? to match any single digit.

Use * to match any number of digits

Example : 1408*, 1512???1234

In the above example, a call is forwarded to the corresponding destination if the caller ID either starts with 1408 or is
                                          an 11-digit numbering starting with 1512 and ending with 1234.

Default setting—blank

<Cfwd_Sel1_Dest_1>, <Cfwd_Sel8_Dest_1>

<Cfwd_Sel1_Dest_2>, <Cfwd_Sel8_Dest_2>

The destination for the corresponding Call Forward Selective caller pattern (Cfwd Sel1-8 Caller).

Default setting—blank

<Cfwd_Last_Caller_1>

<Cfwd_Last_Caller_2>

The number of the last caller; this caller is actively forwarded to the Cfwd Last Dest via the Call Forward Last service.

Default setting—blank

<Cfwd_Last_Dest_1>

<Cfwd_Last_Dest_2>

The destination for the Cfwd Last Caller.

<Block_Last_Caller_1>

<Block_Last_Caller_2>

The number of the last caller; this caller is blocked via the Block Last Caller Service.

Default setting—blank

<Accept_Last_Caller_1>

<Accept_Last_Caller_2>

The number of the last caller; this caller is accepted via the Accept Last Caller Service.

Default setting—blank

<Speed_Dial_2_1>, <Speed_Dial_9_1>

<Speed_Dial_2_2>, <Speed_Dial_9_2>

Target phone number (or URL) assigned to speed dial 2, 3, 4, 5, 6, 7, 8, or 9.

Default setting—blank

<CW_Setting_1>

<CW_Setting_2>

Call Waiting on/off for all calls.

Default setting—yes

<Block_CID_Setting_1>

<Block_CID_Setting_2>

Block Caller ID on/off for all calls.

Default setting—no

<Block_ANC_Setting_1>

<Block_ANC_Setting_2>

Block Anonymous Calls on or off.

Default setting—no

<DND_Setting_1>

<DND_Setting_2>

DND on or off.

Default setting—no

<CID_Setting_1>

<CID_Setting_2>

Caller ID Generation on or off.

Default setting—yes

<CWCID_Setting_1>

<CWCID_Setting_2>

Call Waiting Caller ID Generation on or off.

Default setting—yes

<Dist_Ring_Setting_1>

<Dist_Ring_Setting_2>

Distinctive Ring on or off.

Default setting—yes

<Secure_Call_Setting_1>

<Secure_Call_Setting_2>

If yes, all outbound calls are secure calls by default, without requiring the user to dial a star code first.

Default setting—no

If Secure Call Setting is set to yes, all outbound calls are secure. However, a user can disable security for a call by dialing
                                                *19 before dialing the target number.

If Secure Call Setting is set to No, the user can make a secure outbound call by dialing *18 before dialing the target number.

A user cannot force inbound calls to be secure or not secure; that depends on whether the caller has security enabled or not.

This setting is applicable only if Secure Call Serv is set to yes on the line interface.

<Message_Waiting_1>

<Message_Waiting_2>

Setting this value to yes can activate stutter tone and VMWI signal. This parameter is stored in long term memory and will
                                          survive after reboot or power cycle.

Default setting—no

<Accept_Media_Loopback_Request_1>

<Accept_Media_Loopback_Request_2>

Controls how to handle incoming requests for loopback operation.

Default setting—automatic

never: Never accepts loopback calls; replies 486 to the caller.

automatic: Automatically accepts the call without ringing.

manual: Rings the phone first, and the call must be picked up manually before loopback starts.

Default setting—Automatic

<Media_Loopback_Mode_1>

<Media_Loopback_Mode_2>

The loopback mode to assume locally when making call to request media loopback. Choices are: Source and Mirror.

Default setting—source

If the ATA answers the call, the mode is determined by the caller.

<Media_Loopback_Type_1>

<Media_Loopback_Type_2>

The loopback type to use when making call to request media loopback operation. Choices are Media and Packet.

Default setting—media

Note that if the ATA answers the call, then the loopback type is determined by the caller (the ATA always picks the first
                                          loopback type in the offer if it contains multiple type.)

<Ring1_Caller_1_ > through <Ring8_Caller_1_ >

<Ring1_Caller_2_ > through <Ring8_Caller_2_ >

<FAX_CNG_Detect_Enable_1>

Caller number pattern to play Distinctive Ring/CWT 1, 2, 3, 4, 5, 6, 7, or 8. Caller number patterns are matched from Ring
                                          1 to Ring 8. The first match (not the closest match) will be used for alerting the subscriber.

Default setting—blank

<Default_Ring_1>

<Default_Ring_2>

Default ringing pattern, 1–8, for all callers.

Default setting—1

<Default_CWT_1>

<Default_CWT_2>

Default CWT pattern, 1–8, for all callers.

Default setting—1

<Hold_Reminder_Ring_1>

<Hold_Reminder_Ring_2>

Ring pattern for reminder of a holding call when the phone is on-hook.

Default setting—8

<Hold_Reminder_Ring_1>

<Hold_Reminder_Ring_2>

Ring pattern for reminder of a holding call when the phone is on-hook.

Default setting—8

<Call_Back_Ring_1>

<Call_Back_Ring_2>

Ring pattern for call back notification.

Default setting—7

<Cfwd_Ring_Splash_Len_1>

<Cfwd_Ring_Splash_Len_2>

Duration of ring splash when a call is forwarded (0 – 10.0s)

Default setting—0

<Cblk_Ring_Splash_Len_1>

<Cblk_Ring_Splash_Len_2>

Duration of ring splash when a call is blocked (0 – 10.0s)

Default setting—0

<VMWI_Ring_Policy_1>

<VMWI_Ring_Policy_2>

Duration of ring splash when new messages arrive before the VMWI signal is applied (0 – 10.0s)

Default setting: 0

<Ring_On_No_New_VM_1>

<Ring_On_No_New_VM_2>

The parameter controls when a ring splash is played when a the VM server sends a SIP NOTIFY message to the ATA indicating
                                          the status of the subscriber’s mail box. Three settings are available.

New VM Available: Ring as long as there new voicemail messages.

New VM Becomes Available: Ring at the point when the first new voicemail message is received.

New VM Arrives: Ring when the number of new voicemail messages increases.

Default setting—New VM Available

<VMWI_Ring_Splash_Len_1>

<VMWI_Ring_Splash_Len_2>

Duration of ring splash when new messages arrive before the VMWI signal is applied (0 – 10.0s)

Default setting—0

<Ring_On_No_New_VM_1>

<Ring_On_No_New_VM_2>

If enabled, the ATA plays a ring splash when the voicemail server sends SIP NOTIFY message to the ATA indicating that there
                                          are no more unread voice mails. Some equipment requires a short ring to precede the FSK signal to turn off VMWI lamp.

Default setting—no

<PSTN_Line_Enable_3>

To enable this line for service, select yes. Otherwise, select no.

Default setting—yes

<Incoming_Handset_List_3>

<Incoming_Handset_List_2>

The devices that ring when an incoming call is received on the specified line.

Default setting—fxs,1,2,3,4,5,6,7,8,9,10

<SIP_ToS/DiffServ_Value_1>

<SIP_ToS/DiffServ_Value_2>

TOS/DiffServ field value in UDP IP packets carrying a SIP message.

Default setting—0x68

<SIP_CoS_Value_1>

<SIP_CoS_Value_2>

CoS value for SIP messages. Valid values are 0 through 7.

Default setting—3

<RTP_ToS/DiffServ_Value_1>

<RTP_ToSDiffServ_Value_2>

ToS/DiffServ field value in UDP IP packets carrying RTP data.

Default setting—0xb8

<RTP_CoS_Value_1>

<RTP_CoS_Value_2>

CoS value for RTP data. Valid values are 0 through 7.

Default setting—6

<Network_Jitter_Level_1>

<Network_Jitter_Level_2>

Determines how jitter buffer size is adjusted by the ATA. Jitter buffer size is adjusted dynamically. The minimum jitter buffer
                                          size is 30 milliseconds or (10 milliseconds + current RTP frame size), whichever is larger, for all jitter level settings.
                                          However, the starting jitter buffer size value is larger for higher jitter levels. This setting controls the rate at which
                                          the jitter buffer size is adjusted to reach the minimum. Select the appropriate setting: low, medium, high, very high, or
                                          extremely high.

Default setting—high

<Jitter_Buffer_Adjustment_1>

<Jitter_Buffer_Adjustment_2>

Choose yes to enable or no to disable this feature.

Default setting—yes

<SIP_Transport_1>

<SIP_Transport_2>

The TCP choice provides “guaranteed delivery”, which assures that lost packets are retransmitted. TCP also guarantees that
                                          the SIP packages are received in the same order that they were sent. As a result, TCP overcomes the main disadvantages of
                                          UDP.

In addition, for security reasons, most corporate firewalls block UDP ports. With TCP, new ports do not need to be opened
                                          or packets dropped, because TCP is already in use for basic activities such as Internet browsing or e-commerce. Options are:
                                          UDP, TCP, TLS , AUTO .

AUTO allows the ATA to select the appropriate protocol automatically, based on the NAPTR records on the DNS server.

Default setting—UDP

<SIP_Port_1>

<SIP_Port_2>

Port number of the SIP message listening and transmission port.

Default setting—5060

<SIP_100REL_Enable_1>

<SIP_100REL_Enable_2>

To enable the support of 100REL SIP extension for reliable transmission of provisional responses (18x) and use of PRACK requests,
                                          select yes. Otherwise, select no.

Default setting—no

<EXT_SIP_Port_1>

<EXT_SIP_Port_2>

The external SIP port number.

Default setting—blank

<Auth_Resync-Reboot_1>

<Auth_Resync-Reboot_2>

If this feature is enabled, the ATA authenticates the sender when it receives the NOTIFY resync reboot (RFC 2617) message.
                                          To use this feature, select yes. Otherwise, select no.

Default setting—yes

<SIP_Proxy-Require_1>

<SIP_Proxy-Require_2>

The SIP proxy can support a specific extension or behavior when it sees this header from the user agent. If this field is
                                          configured and the proxy does not support it, it responds with the message, unsupported. Enter the appropriate header in the
                                          field provided.

Default setting—blank

<SIP_Remote-Party-ID_1>

<SIP_Remote-Party-ID_2>

To use the Remote-Party-ID header instead of the From header, select yes. Otherwise, select no.

Default setting—yes

<SIP_GUID_1>

<SIP_GUID_2>

This feature limits the registration of SIP accounts. The Global Unique ID is generated for each line for each ATA. When it
                                          is enabled, the ATA adds a GUID header in the SIP request. The GUID is generated the first time the unit boots up and stays
                                          with the unit through rebooting and even factory reset.

Default setting—no

<RTP_Log_Intvl_1>

<RTP_Log_Intvl_2>

The interval for the RTP log.

Default setting—0

<Restrict_Source_IP_1>

<Restrict_Source_IP_2>

If configured, the ATA drops all packets sent to its SIP Ports from an untrusted IP address. A source IP address is untrusted
                                          if it does not match any of the IP addresses resolved from the configured Proxy (or Outbound Proxy if Use Outbound Proxy is
                                          yes)

Default setting—no

<Referor_Bye_Delay_1>

<Referor_Bye_Delay_2>

The number of seconds to wait before sending a BYE to the referrer to terminate a stale call leg after a call transfer.

<Refer_Target_Bye_Delay_1>

<Refer_Target_Bye_Delay_2>

The number of seconds to wait before sending a BYE to the refer target to terminate a stale call leg after a call transfer.

<Referee_Bye_Delay_1>

<Referee_Bye_Delay_2>

The number of seconds to wait before sending a BYE to the referee to terminate a stale call leg after a call transfer.

<Refer-To_Target_Contact_1>

<Refer-To_Target_Contact_2>

To contact the refer-to target, select yes. Otherwise, select no.

Default setting—no

<Sticky_183_1>

<Sticky_183_2>

If this feature is enabled, the ATA ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound
                                          INVITE. To enable this feature, select yes. Otherwise, select no.

Default setting—no

<Auth_INVITE_1>

<Auth_INVITE_2>

When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy.

Default setting—no

<Reply_182_On_Call_Waiting_1>

<Reply_182_On_Call_Waiting_2>

When enabled, the ATA replies with a SIP182 response to the caller if it is already in a call and the line is off-hook. To
                                          use this feature select yes.

Default setting—no

<Use_Anonymous_With_RPID_1>

<Use_Anonymous_With_RPID_2>

Determines whether or not the ATA uses “Anonymous” when Remote Party ID is requested in the SIP message.

Default setting—yes

<Use_Local_Addr_In_From_1>

<Use_Local_Addr_In_From_2>

Use the local ATA IP address in the SIP FROM message.

Default setting—no

<Broadsoft_ALTC_1>

<Broadsoft_ALTC_2>

Use Broadsoft ALTC SDP negotiation.

Default setting—No

<Auth_Support_RFC8760_1>

<Auth_Support_RFC8760_2>

When enabled, the ATA authorization supports RFC-8760 that specifies the digest algorithms SHA256, SHA-512/256, and MD5. To
                                          enable this feature, select yes. Otherwise, select no.

Default setting—No

<MediaSec_Request_1>

<MediaSec_Request_2>

Determines whether the ATA can initiate media plane security negotiations with the server. When set to Yes, the ATA can initiate
                                          the negotiations. When set to No, ATA can only handle the negotiation requests from the server.

Default setting—No

<MediaSec_Over_TLS_Only_1>

<MediaSec_Over_TLS_Only_2>

Determines how the ATA initiates or handles the media plane security negotiations. When set to Yes, the ATA can initiate or
                                          handle the mediasec negotiations with SIP over TCP only. When set to No, the ATA can initiate or handle the negotiations regardless
                                          of the protocol (UDP/TCP/TLS) for SIP messages.

Default setting—No

<Dial_Plan_1_3> through <Dial_Plan_8_3>

The PSTN dial plan pool. You can associate a dial plan with a VoIP Caller or a PSTN Caller by referencing the index number
                                          (1~8).

Default setting—(xx.)

<VoIP-To-PSTN_Gateway_Enable_3>

Choose yes to enable or choose no to disable the VoIP-To-PSTN Gateway functionality.

Default setting—yes

<VoIP_Caller_Auth_Method_3>

The method to authenticate a VoIP Caller to access the PSTN gateway. Choose from none, PIN, or HTTP Digest.

Default setting—none

<VoIP_PIN_Max_Retry_3>

The number of times that a VoIP caller can attempt to enter a PIN, if the VoIP Caller Auth Method is set to PIN.

Default setting—3

<One_Stage_Dialing_3>

Choose yes to enable or choose no to disable one-stage dialing. This setting applies if the VoIP Caller Auth Method is none
                                          or HTTP Digest, or if caller is in the Access List.

Default setting—yes

<Line_1_VoIP_Caller_DP_3>

The index number of the dial plan to use when the VoIP Caller is calling from Line 1 of the same ATA during normal operation
                                          (in other words, not due to fallback to PSTN service when Line 1 VoIP service is down). The Authentication is skipped for
                                          Line 1 VoIP caller.

Default setting—1

<VoIP_Caller_Default_DP_3>

The index number of the dial plan to use when the VoIP Caller is not authenticated.

Default setting—1

<Line_1_Fallback_DP_3>

The index number of the dial plan to use when the VoIP Caller is calling from Line 1 of the same ATA due to fallback to PSTN
                                          service when Line 1 VoIP service is down.

Default setting—none

<VoIP_Caller_ID_Pattern_3>

A comma-separated list of caller phone number patterns that is used to allow or block access to the PSTN gateway based on
                                          the caller ID. If the caller ID does not match a specified pattern, access is rejected, regardless of the authentication method.
                                          This comparison is applied before the access list is applied. If this parameter is blank (not specified), all callers are
                                          considered for VoIP service.

Use ? to match any single digit.

Use * to match any number of digits.

Example : 1408*, 1512???1234

In the above example, the caller ID either must start with 1408 or must be an 11-digit numbering starting with 1512 and ending
                                          with 1234.

Default setting—blank

<VoIP_Access_List_3>

A comma-separated list of number patterns that is used to allow or block access to the PSTN gateway based on the source IP
                                          address. If the IP address matches a specified pattern, service is allowed without further authentication.

Example : 192.168.*.*, 66.43.12.1??.

In the above example, the source IP address either must begin with 192.168 or must be in the range of 66.43.12.100-199.

Default setting—blank

<VoIP_Caller_1_PIN_3> through <VoIP_Caller_8_PIN_3>

A PIN number that a VoIP caller can use to access the PSTN gateway, when the VoIP Caller Auth Method is set to PIN.

Default setting—blank

<VoIP_Caller_1_DP_3> through <VoIP_Caller_8_DP_3>

The index number of the dial plan to use upon successful entry of the corresponding VoIP Caller PIN.

Default setting—1

<VoIP_User_1_Auth_ID_3> through <VoIP_User_8_Auth_ID_3>

A user ID that a VoIP Caller can use for authentication by using the HTTP Digest method (in other words, by embedding an Authorization
                                          header in the SIP INVITE message sent to the ATA. If the credentials are missing or incorrect, the ATA will challenge the
                                          caller with a 401 response).

The VoIP caller whose authentication userid equals to this ID is referred to VoIP User 1 of this ATA. If the caller specifies
                                          an authentication user-id that does not match any of the VoIP User Auth ID’s, the INVITE will be rejected with a 403 response.

Default setting—blank.

<VoIP_User_1_Password_3> through <VoIP_User_8_Password_3>

The password to be used with VoIP User 1. The user assumes the identity of VoIP User 1 must therefore compute the credentials
                                          using this password, or the INVITE will be challenged with a 401 response

Default setting—blank.

<VoIP_User_1_DP_3> through <VoIP_User_8_DP_3>

For up to 8 VoIP users, specify the index of the dial plan to be used after successful authentication. If authentication is
                                          disabled, the default dial plan is used for all unknown VoIP users.

Default setting—1.

<PSTN-To-VoIP_Gateway_Enable_3>

Select yes to enable or select no to disable PSTN-To-VoIP Gateway functionality.

Default setting—yes

<PSTN_Caller_Auth_Method_3>

The method to authenticate a PSTN Caller to access the VoIP gateway. Choose from none or PIN.

Default setting—none

<PSTN_Ring_Thru_1_3>

To enable ring through to Line 1 based on caller number patterns, choose yes. Otherwise choose no.

For more information about PSTN Caller number patterns, see <PSTN_Caller_ID_Pattern_3>.

Default setting—yes

<PSTN_PIN_Max_Retry_3>

The number of times that a PSTN caller can attempt to enter a PIN number, if the authentication method is set to PIN.

Default setting—3

<PSTN_CID_for_VoIP_CID_3>

Choose yes or no.

Default setting—no

<PSTN_CID_Number_Prefix_3>

A dialing prefix, if needed, to add to the caller ID number on the PBX to ensure that a callback goes to the correct number.

Default setting—blank

<PSTN_Caller_Default_DP_3>

The index number of the dial plan that is used when the PSTN Caller Auth Method is set to none.

Default settings: 1

<Line_1_Signal_Hook_Flash_to_PSTN_3>

Specify the operation of the hook flash on the analog phone when a PSTN-to-VoIP call is active. Choose Disabled or Double
                                          Hook Flash.

Default setting—Disabled

<PSTN_CID_Name_Prefix_3>

The prefix to add to the caller ID name that is sent to the PBX. Enter the characters to add to the caller ID name.

Default setting—blank

<PSTN_Caller_ID_Pattern_3>

A comma-separated list of phone number patterns that is used to allow or block access to the VoIP gateway based on the caller
                                          ID. If the caller ID does not match a specified pattern, access is rejected, regardless of the authentication method. This
                                          comparison is applied before the access list is applied. If this parameter is blank (not specified), all callers are considered
                                          for VoIP service.

Use ? to match any single digit.

Use * to match any number of digits.

Example : 1408*, 1512???1234

In the above example, the caller ID either must start with 1408 or must be an 11-digit numbering starting with 1512 and ending
                                          with 1234.

Default setting—blank

<PSTN_Access_List_3>

A comma-separated list of number patterns that is used to allow or block access to the VoIP gateway based on the destination
                                          IP address. If the destination IP address matches a specified pattern, service is allowed without further authentication.

Example : 192.168.*.*, 66.43.12.1??.

In the above example, the IP address either must begin with 192.168 or must be in the range of 66.43.12.100-199.

The default is blank.

<PSTN_Caller_1_PIN_3> through <PSTN_Caller_8_PIN_3>

A PIN number that allows a PSTN caller to access to the VoIP gateway. Calls will be subject to the dial plan specified by
                                          the corresponding PSTN Caller DP setting (see below). These settings apply when the PSTN Caller Authentication Method parameter
                                          is set to PIN.

Default setting—blank

<PSTN_Caller_1_DP_3> through <PSTN_Caller_8_DP_3>

The index number of the dial plan to use upon successful entry of the corresponding PSTN Caller PIN.

Default setting—1

<VoIP_Answer_Delay_3>

The number of seconds to wait before autoanswering an inbound VoIP call for the FXO account. The range is 0-255.

Default setting—0

<VoIP_PIN_Digit_Timeout_3>

After a VoIP caller is prompted for a PIN or enters a digit, the number of seconds to wait for an entry. The range is 0-255.

Default setting—10

<PSTN_Answer_Delay_3>

After an inbound PSTN call starts ringing, the number of seconds to wait before autoanswering the call. The range is 0-255.

Default setting—16

<PSTN_PIN_Digit_Timeout_3>

After a PSTN caller is prompted for a PIN or enters a digit, the number of seconds to wait for an entry. The range is 0-255.

Default setting—10

<PSTN-To-VoIP_Call_Max_Dur_3>

The limit on the duration of a PSTN-To-VoIP Gateway Call. Unit is in seconds. 0 means unlimited. The range is 0-2147483647.

Default setting—0

<PSTN_Ring_Thru_Delay_3>

After a PSTN call starts ringing, the number of seconds to wait before ring through to Line 1. In order for Line 1 to have
                                          the caller ID information, this value must be greater than the time required to complete the PSTN caller ID delivery. The
                                          range is 0-255.

Default setting—1

<VoIP-To-PSTN_Call_Max_Dur_3>

The limit on the duration of a VoIP-To-PSTN Gateway Call. Unit is in seconds. 0 means unlimited. The range is 0-2147483647.

Default setting—0

<PSTN_Ring_Thru_CWT_Delay_3>

When a call is active and a new PSTN call starts ringing, the number of seconds to wait before ring through to Line 1 with
                                          a Call Waiting Tone.

Default setting—3

<VoIP_DLG_Refresh_Intvl_3>

The interval between (SIP) Dialog refresh messages sent by the ATA to detect if the VoIP call-leg is still up. If this value
                                          is set to 0, the VoIP call-leg status will not be checked by the ATA. The refresh message is a SIP ReINVITE, and the VoIP
                                          peer must response with a 2xx response. If the VoIP peer does not reply or the response is not greater than 2xx, the ATA will
                                          disconnect both call legs automatically. The range is 0-255.

Default setting—0

<PSTN_Ring_Timeout_3>

After a ring burst, the number of seconds to wait before concluding that PSTN ring has ceased. The range is 0-255.

Default setting—5

<PSTN_Dialing_Delay_3>

After hook, the number of seconds to wait before dialing a PSTN number. The range is 0-255.

Default setting—1

<PSTN_Dial_Digit_Len_3>

The on/off time when the Gateway transmits digits through the Line (FXO) port. The syntax is on-time/off-time, expressed in
                                          seconds. The permitted range is 0.05 to 3.00 (up to two decimal places only).

Default setting—.1/.1

<PSTN_Hook_Flash_Len_3>

The length of the hook flash in seconds.

Default setting—.25

<Detect_CPC_3>

Choose yes to enable or choose no to disable this feature. CPC is a brief removal of tip-and-ring voltage. If enabled, the
                                          ATA will disconnect both call legs when this signal is detected during a gateway call.

Default setting—yes

<Detect_Polarity_Reversal_3>

Choose yes to enable or choose no to disable this feature. If enabled, the ATA will disconnect both call legs when this signal
                                          is detected during a gateway call. If it is a PSTN gateway call, the first polarity reversal is ignored and the second one
                                          triggers the disconnection. For VoIP gateway call, the first polarity reversal triggers the disconnection.

Default setting—yes

<Detect_PSTN_Long_Silence_3>

Choose yes to enable or choose no to disable this feature. If enabled, the ATA will disconnect both call legs when the PSTN
                                          side has no voice activity for a duration longer than the length specified in the Long Silence Duration parameter during a
                                          gateway call.

Default setting—no

<Detect_VoIP_Long_Silence_3>

Choose yes to enable or choose no to disable this feature. If enabled, the ATA will disconnect both call legs when the VoIP
                                          side has no voice activity for a duration longer than the length specified in the Long Silence Duration parameter during a
                                          gateway call.

Default setting—no

<PSTN_Long_Silence_Duration_3>

This value is minimum length of PSTN silence (or inactivity) in seconds to trigger a gateway call disconnection if Detect
                                          Long Silence is enabled.

Default setting—30

<VoIP_Long_Silence_Duration_3>

This value is minimum length of VoIP silence (or inactivity) in seconds to trigger a gateway call disconnection if Detect
                                          Long Silence is enabled.

Default setting—30

<PSTN_Silence_Threshold_3>

This parameter adjusts the sensitivity of PSTN silence detection. Choose from {very low, low, medium, high, very high}. The
                                          higher the setting, the easier to detect silence and hence easier to trigger a disconnection.

Default setting—medium

<Min_CPC_Duration_3>

Specify the minimum duration of a low tip and ring voltage (below 1V) for the Gateway to recognize it as a CPC signal or PSTN
                                          line removal.

Default setting—0.2

<Detect_Disconnect_Tone_3>

Choose yes to enable or choose no to disable this feature. If enabled, the ATA will disconnect both call legs when it detects
                                          the disconnect tone from the PSTN side during a gateway call. Disconnect tone is specified in the Disconnect Tone parameter,
                                          which depends on the region of the PSTN service.

Default setting—yes

<Disconnect_Tone_3>

This value is the tone script which describes to the ATA the tone to detect as a disconnect tone. The syntax follows a standard
                                          Tone Script with some restrictions.

Default value is standard US reorder (fast busy) tone, for 4 seconds.

Default setting—480@-30,620@-30;4(.25/.25/1+2)

Restrictions:

Two frequency components must be given. If single frequency is desired, the same frequency is used for both.

The tone level value is not used. –30 (dBm) should be used for now.

Only 1 segment set is allowed.

Total duration of the segment set is interpreted as the minimum duration of the tone to trigger detection.

6 segments of on/off time (seconds) can be specified. A 10% margin is used to validated cadence characteristics of the tone.

<Disconnect_Tone_3>

Disconnect Tone Script values:

US—480@-30,620@-30;4(.25/.25/1+2)

UK—400@-30,400@-30; 2(3/0/1+2)

France—440@-30,440@-30; 2(0.5/0.5/1+2)

Germany—440@-30,440@-30; 2(0.5/0.5/1+2)

Netherlands—425@-30,425@-30; 2(0.5/0.5/1+2)

Sweden—425@-10; 10(0.25/0.25/1)

Norway—425@-10; 10(0.5/0.5/1)

Italy—425@-30,425@-30; 2(0.2/0.2/1+2)

Spain—425@-10; 10(0.2/0.2/1,0.2/0.2/1,0.2/0.6/1)

Portugal—425@-10; 10(0.5/0.5/1)

Poland—425@-10; 10(0.5/0.5/1)

Denmark—425@-10; 10(0.25/0.25/1)

New Zealand—400@-15; 10(0.25/0.25/1)

Australia—425@-13; 10(0.375/0.375/1)

<FXO_Country_Setting_3>

The country of deployment. This setting applies the relevant regional settings for PSTN calls.

Default setting—USA

<Tip_Ring_Voltage_Adjust_3>

Voltage adjustment. The choices are 3.1V, 3.2V, 3.35V, and 3.5V.

Default setting—3.5V.

<Ring_Frequency_Min_3>

The lower limit of the ring frequency used to detect the ring signal.

Default setting—10

<SPA_To_PSTN_Gain_3>

dB of digital gain (or attenuation if negative) to be applied to the signal sent from the ATA to the PSTN side. The range
                                          is -15 to 12.

Default setting—0

<Ring_Frequency_Max_3>

The higher limit of the ring frequency used to detect the ring signal.

Default setting—100

<PSTN_To_SPA_Gain_3>

dB of digital gain (or attenuation if negative) to be applied to the signal sent from the PSTN side to the ATA. The range
                                          is -15 to 12.

Default setting—0

<Ring_Validation_Time_3>

The minimum signal duration required by the Gateway for recognition as a ring signal.

Default setting—256 ms

<Ring_Indication_Delay_3>

Choose from {0, 512, 768, 1024, 1280, 1536, 1792} (ms).

Default setting—512ms

<Ring_Timeout_3>

Choose from {0, 128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280, 1408, 1536, 1664, 1792, 1920} (ms).

Default setting—640 ms

<Ring_Threshold_3>

Choose from {13.5–16.5, 19.35–2.65, 40.5–49.5} (Vrms).

Default setting—13.5-16.5 Vrms

<Line-In-Use_Voltage_3>

The voltage threshold at which the ATA assumes the PSTN is in use by another handset sharing the same line (and will declare
                                          PSTN gateway service not available to incoming VoIP callers).

Default setting—30

<Dial_Tone>

Prompts the user to enter a phone number. Reorder Tone is played automatically when Dial Tone or any of its alternatives times
                                          out.

Default setting—350@-5,440@-5;10(*/0/1+2)

<Second_Dial_Tone>

Alternative to the Dial Tone when the user dials a three-way call.

Default setting—420@-5,520@-5;10(*/0/1+2)

<Outside_Dial_Tone>

Alternative to the Dial Tone. It prompts the user to enter an external phone number, as opposed to an internal extension.
                                          It is triggered by a comma character encountered in the dial plan.

Default setting—420@-4;10(*/0/1)

<Prompt_Tone>

Prompts the user to enter a call forwarding phone number.

Default setting—520@-5,620@-5;10(*/0/1+2)

<Busy_Tone>

Played when a 486 RSC is received for an outbound call.

Default setting—480@-5,620@-5;10(.5/.5/1+2)

<Reorder_Tone>

Played when an outbound call has failed, or after the far end hangs up during an established call. Reorder Tone is played
                                          automatically when Dial Tone or any of its alternatives times out.

Default setting—480@-5,620@-5;10(.25/.25/1+2)

<Off_Hook_Warning_Tone>

Played when the caller has not properly placed the handset on the cradle. Off Hook Warning Tone is played when the Reorder
                                          Tone times out.

Default setting—480@-3,620@3;10(.125/.125/1+2)

<Ring_Back_Tone>

Played during an outbound call when the far end is ringing.

Default setting—440@-5,480@-5;*(2/4/1+2)

<Ring_Back_2_Tone>

Your ATA plays this ringback tone instead of Ring Back Tone if the called party replies with a SIP 182 response without SDP
                                          to its outbound INVITE request.

Default setting—the same as Ring Back Tone, except the cadence is 1s on and 1s off.

Default setting—440@-5,480@-5;*(1/1/1+2)

<Confirm_Tone>

Brief tone to notify the user that the last input value has been accepted.

Default setting—600@-4;1(.25/.25/1)

<SIT1_Tone> through <SIT4_Tone>

Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                          is configurable on the SIP screen.

Default setting—985@-4,1428@-4,1777@-4;20(.380/0/1,.380/0/2,.380/0/3,0/4/0)

<MWI_Dial_Tone>

Played instead of the Dial Tone when there are unheard messages in the caller’s mailbox.

Default setting—350@-5,440@-5;2(.1/.1/1+2);10(*/0/1+2)

<Cfwd_Dial_Tone>

Played when all calls are forwarded.

Default setting—350@-5,440@-5;2(.2/.2/1+2);10(*/0/1+2)

<Holding_Tone>

Informs the local caller that the far end has placed the call on hold.

Default setting—600@-5;*(.1/.1/1,.1/.1/1,.1/9.5/1)

<Conference_Tone>

Played to all parties when a three-way conference call is in progress.

Default setting—350@-5;20(.1/.1/1,.1/9.7/1)

<Secure_Call_Indication_Tone>

Played when a call has been successfully switched to secure mode. It should be played only for a short while (less than 30
                                          seconds) and at a reduced level (less than -19 dBm) so it does not interfere with the conversation.

Default setting—397@-5,507@-5;15(0/2/0,.2/.1/1,.1/2.1/2)

<VoIP_PIN_Tone>

This tone is played to prompt a VoIP caller to enter a PIN number.

<PSTN_PIN_Tone>

This tone is played to prompt a PSTN caller to enter a PIN number.

<Feature_Invocation_Tone>

Played when a feature is implemented.

Default setting—350@-4;*(.1/.1/1)

<Ring1_Cadence>

Cadence script for distinctive ring 1.

Default setting—60(2/4)

<Ring2_Cadence>

Cadence script for distinctive ring 2.

Default setting—60(.8/.4,.8/4)

<Ring3_Cadence>

Cadence script for distinctive ring 3.

Default setting—60(.4/.2,.4/.2,.8/4)

<Ring4_Cadence>

Cadence script for distinctive ring 4.

Default setting—60(.3/.2,1/.2,.3/4)

<Ring5_Cadence>

Cadence script for distinctive ring 5.

Default setting—1(.5/.5)

<Ring6_Cadence>

Cadence script for distinctive ring 6.

Default setting—60(.2/.4,.2/.4,.2/4)

<Ring7_Cadence>

Cadence script for distinctive ring 7.

Default setting—60(.4/.2,.4/.2,.4/4)

<Ring8_Cadence>

Cadence script for distinctive ring 8.

Default setting—60(0.25/9.75)

<CWT1_Cadence>

Cadence script for distinctive CWT 1.

Default setting—30(.3/9.7)

<CWT2_Cadence>

Cadence script for distinctive CWT 2.

Default setting—30(.1/.1, .1/9.7)

<CWT3_Cadence>

Cadence script for distinctive CWT 3.

Default setting—30(.1/.1, .1/.1, .1/9.7)

<CWT4_Cadence>

Cadence script for distinctive CWT 4.

Default setting—30(.1/.1, .3/.1, .1/9.3)

<CWT5_Cadence>

Cadence script for distinctive CWT 5.

Default setting—1(.5/.5)

<CWT6_Cadence>

Cadence script for distinctive CWT 6.

Default setting—30(.3/.1,.3/.1,.1/9.1)

<CWT7_Cadence>

Cadence script for distinctive CWT 7.

Default setting—30(.3/.1,.3/.1,.1/9.1)

<CWT8_Cadence>

Cadence script for distinctive CWT 8.

Default setting—2.3(.3/2)

<Ring1_Name>

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 1 for the inbound call.

Default setting—Bellcore-r1

<Ring2_Name>

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 2 for the inbound call.

Default setting—Bellcore-r2

<Ring3_Name>

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 3 for the inbound call.

Default setting—Bellcore-r3

<Ring4_Name>

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 4 for the inbound call.

Default setting—Bellcore-r4

<Ring5_Name>

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 5 for the inbound call.

Default setting—Bellcore-r5

<Ring6_Name>

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 6 for the inbound call.

Default setting—Bellcore-r6

<Ring7_Name>

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 7 for the inbound call.

Default setting—Bellcore-r7

<Ring8_Name>

Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 8 for the inbound call.

Default setting—Bellcore-r8

<Ring_Waveform>

Waveform for the ringing signal. Choices are Sinusoid or Trapezoid.

Default setting—Sinusoid

<Ring_Frequency>

Frequency of the ringing signal. Valid values are 10–100 (Hz)

Default setting—20

<Ring_Voltage>

Ringing voltage. Choices are 60–90 (V)

Default setting—85

<CWT_Frequency>

Frequency script of the call waiting tone. All distinctive CWTs are based on this tone.

Default setting—440@-10

<Synchronized_Ring>

If this is set to yes, when the ATA is called, all lines ring at the same time (similar to a regular PSTN line) After one
                                          line answers, the others stop ringing.

Default setting—no

<Hook_Flash_Timer_Min>

Minimum on-hook time before off-hook qualifies as hook flash. Less than this the onhook event is ignored. Range: 0.1–0.4 seconds.

Default setting—0.1

<Hook_Flash_Timer_Max>

Maximum on-hook time before off-hook qualifies as hook flash. More than this the onhook event is treated as on hook (no hookflash
                                          event) Range: 0.4–1.6 seconds.

Default setting—0.9

<Callee_On_<Hook_Delay>

Phone must be on-hook for at this time in sec. before the ATA will tear down the current inbound call. It does not apply to
                                          outbound calls. Range: 0–255 seconds.

Default setting—0

<Reorder_Delay>

Delay after far end hangs up before reorder tone is played. 0 =plays immediately, inf =never plays. Range: 0–255 seconds.

Default setting—5.

<Call_Back_Expires>

Expiration time in seconds of a call back activation. Range: 0–65535 seconds.

Default setting—1800

<Call_Back_Retry_Intvl>

Call back retry interval in seconds. Range: 0–255 seconds.

Default setting—30

<Call_Back_Delay>

Delay after receiving the first SIP 18x response before declaring the remote end is ringing. If a busy response is received
                                          during this time, the ATA still considers the call as failed and keeps on retrying. Range: 0–65 seconds

Default setting—0.5

<VMWI_Refresh_Intvl>

Interval between VMWI refresh to the device. Range: 0–65535 seconds

Default setting—0

<Interdigit_Long_Timer>

Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit_Long_Timer
                                          is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Range: 0–64 seconds.

Default setting—10

<Interdigit_Short_Timer>

Short timeout between entering digits when dialing. The Interdigit_Short_Timer is used after any one digit, if at least one
                                          matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Range: 0–64
                                          seconds.

Default setting—3

<CPC_Delay>

Delay in seconds after caller hangs up when the ATA starts removing the tip-and-ring voltage to the attached equipment of
                                          the called party. The range is 0–255 seconds.

This feature is generally used for answer supervision on the caller side to signal to the attached equipment when the call
                                          has been connected (remote end has answered) or disconnected (remote end has hung up) This feature should be disabled for
                                          the called party (in other words, by using the same polarity for connected and idle state) and the CPC feature should be used
                                          instead. Without CPC enabled, reorder tone will is played after a configurable delay. If CPC is enabled, dial tone will be
                                          played when tip-to-ring voltage is restored. Resolution is 1 second.

Default setting—2

<CPC_Duration>

Duration in seconds for which the tip-to-ring voltage is removed after the caller hangs up. After that, tip-to-ring voltage
                                          is restored and the dial tone applies if the attached equipment is still off-hook. CPC is disabled if this value is set to
                                          0. Range: 0 to 1.000 second. Resolution is 0.001 second.

Default setting—0 (CPC disabled)

<Call_Return_Code>

Call Return Code This code calls the last caller.

Default setting—*69

<Call_Redial_Code>

Redials the last number called.

Default setting—*07

<Blind_Transfer_Code>

Begins a blind transfer of the current call to the extension specified after the activation code.

Default setting—*98

<Call_Back_Act_Code>

Starts a callback when the last outbound call is not busy.

Default setting—*66

<Call_Back_Deact_Code>

Cancels a callback.

Default setting—*86

<Call_Back_Busy_Act_Code>

Starts a callback when the last outbound call is busy.

Default setting—*05

<Cfwd_All_Act_Code>

Forwards all calls to the extension specified after the activation code.

Default setting—*72

<Cfwd_All_Deact_Code>

Cancels call forwarding of all calls.

Default setting—*73

<Cfwd_Busy_Act_Code>

Forwards busy calls to the extension specified after the activation code.

Default setting—*90

<Cfwd_Busy_Deact_Code>

Cancels call forwarding of busy calls.

Default setting—*91

<Cfwd_No_Ans_Act_Code>

Forwards no-answer calls to the extension specified after the activation code.

Default setting—*92

<Cfwd_No_Ans_Deact_Code>

Cancels call forwarding of no-answer calls.

Default setting—*93

<Cfwd_Last_Act_Code>

Forwards the last inbound or outbound call to the number that the user specifies after entering the activation code.

Default setting—*63

<Cfwd_Last_Deact_Code>

Cancels call forwarding of the last inbound or outbound call.

Default setting—*83

<Block_Last_Act_Code>

Blocks the last inbound call.

Default setting—*60

<Block_Last_Deact_Code>

Cancels blocking of the last inbound call.

Default setting—*80

<Accept_Last_Act_Code>

Accepts the last outbound call. It lets the call ring through when do not disturb or call forwarding of all calls are enabled.

Default setting—*64

<Accept_Last_Deact_Code>

Cancels the code to accept the last outbound call.

Default setting—*84

<CW_Act_Code>

Enables call waiting on all calls.

Default setting—*56

<CW_Deact_Code>

Enables call waiting on all calls.

Default setting—*57

<CW_Per_Call_Act_Code>

Enables call waiting for the next call.

Default setting—*71

<CW_Per_Call_Deact_Code>

Disables call waiting for the next call.

Default setting—*70

<Block_CID_Act_Code>

Blocks caller ID on all outbound calls.

Default setting—*67

<Block_CID_Deact_Code>

Removes caller ID blocking on all outbound calls.

Default setting—*68

<Block_CID_Per_Call_Act_Code>

Blocks caller ID on the next outbound call.

Default setting—*81

<Block_CID_Per_Call_Deact_Code>

Removes caller ID blocking on the next inbound call.

Default setting—*82

<Block_ANC_Act_Code>

Blocks all anonymous calls.

Default setting—*77

<Block_ANC_Deact_Code>

Removes blocking of all anonymous calls.

Default setting—*87

<DND_Act_Code>

Enables the do not disturb feature.

Default setting—*78

<DND_Deact_Code>

Disables the do not disturb feature.

Default setting—*79

<CID_Act_Code>

Enables caller ID generation.

Default setting—*65

<CID_Deact_Code>

Disables caller ID generation.

Default setting—*85

<CWCID_Act_Code>

Enables call waiting, caller ID generation.

Default setting—*25

<CWCID_Deact_Code>

Disables call waiting, caller ID generation.

Default setting—*45

<Dist_Ring_Act_Code>

Enables the distinctive ringing feature.

Default setting—*26

<Dist_Ring_Deact_Code>

Disables the distinctive ringing feature.

Default setting—*46

<Speed_Dial_Act_Code>

Assigns a speed dial number.

Default setting—*74

<Paging_Code>

Used for paging other clients in the group.

Default setting—*96

<Secure_All_Call_Act_Code>

Makes all outbound calls secure.

Default setting—*16

<Secure_No_Call_Act_Code>

Makes all outbound calls not secure.

Default setting—*17

<Secure_One_Call_Act_Code>

Makes the next outbound call secure. (It is redundant if all outbound calls are secure by default.)

Default setting—*18

<Secure_One_Call_Deact_Code>

Makes the next outbound call not secure. (It is redundant if all outbound calls are not secure by default.)

Default setting—*19

<Conference_Act_Code>

If this code is specified, the user must enter it before dialing the third party for a conference call. Enter the code for
                                          a conference call.

Default setting—blank

<Attn-Xfer_Act_Code>

If the code is specified, the user must enter it before dialing the third party for a call transfer. Enter the code for a
                                          call transfer.

Default setting—blank

<Modem_Line_Toggle_Code>

Toggles the line to a modem. Modem passthrough mode can be triggered only by pre-dialing this code.

Default setting—*99

<FAX_Line_Toggle_Code>

Toggles the line to a fax machine.

Default setting—#99

<Media_Loopback_Code>

Use for media loopback.

Default setting—*03

<Referral_Services_Codes>

These codes tell the ATA what to do when the user places the current call on hold and is listening to the second dial tone.
                                          One or more *codes can be configured into this parameter, such as *98, or *97|*98|*123, etc. The maximum length is 79 characters.

This parameter applies when the user places the current call on hold by pressing the hook flash button. Each *code (and the
                                          following valid target number according to current dial plan) triggers the ATA to perform a blind transfer to a target number
                                          that is prepended by the service *code.

For example, after the user dials *98, the ATA plays a special dial tone called the Prompt Tone while waiting for the user
                                          to enter a target number (which is checked according to dial plan as in normal dialing). When a complete number is entered,
                                          the ATA sends a blind REFER to the holding party with the Refer-To target equal to *98 target_number.

This feature allows the ATA to hand off a call to an application server to perform further processing, such as call park.

The *codes should not conflict with any of the other vertical service codes internally processed by the ATA. You can empty
                                          the corresponding *code that you do not want the ATA to process.

Default setting—blank

<Feature_Dial_Services_Codes>

These codes tell the ATA what to do when the user is listening to the first or second dial tone.

One or more *codes can be configured into this parameter, such as *72, or *72|*74|*67|*82, etc. The maximum length is 79 characters.
                                          This parameter applies when the user has a dial tone (first or second dial tone.) After receiving dial tone, a user enters
                                          the *code and the target number according to current dial plan.

For example, after user dials *72, the ATA plays a special tone called a Prompt tone while awaiting the user to enter a valid
                                          target number. When a complete number is entered, the ATA sends a INVITE to *72 target_number as in a normal call. This feature
                                          allows the proxy to process features like call forward (*72) or Block Caller ID (*67.)

The *codes should not conflict with any of the other vertical service codes internally processed by the ATA. You can remove
                                          a corresponding *code that you do not want the ATA to process.

You can add a parameter to indicate which tone plays after the *code is entered, such as *72‘c‘|*67‘p‘. Below is a list of
                                          allowed tone parameters. (Note the use of open quotes surrounding the parameter, without spaces.)

‘c‘ = <Cfwd Dial Tone>

‘d‘ = <Dial Tone>

‘m‘ = <MWI Dial Tone>

‘o‘ = <Outside Dial Tone>

‘p‘ = <Prompt Dial Tone>

‘s‘ = <Second Dial Tone>

‘x‘ = No tones are place, x is any digit not used above

If no tone parameter is specified, the ATA plays Prompt tone by default. If the *code is not to be followed by a phone number,
                                          such as *73 to cancel call forwarding, do not include this parameter. Instead, add the code in the dial plan and the ATA send
                                          INVITE *73@..... as usual when user dials *73.

Default setting—blank

<Service_Annc_Base_Number>

Base number for service announcements.

Default setting—blank

<Service_Annc_Extension_Codes>

Extension codes for service announcements.

Default setting—blank

<Prefer_G711u_Code>

Dial prefix to make G.711u the preferred codec for the call.

Default setting—*017110

<Force_G711u_Code>

Dial prefix to make G.711u the only codec that can be used for the call.

Default setting—*027110

<Prefer_G711a_Code>

Dial prefix to make G.711a the preferred codec for the call.

Default setting—*017111

<Force_G711a_Code>

Dial prefix to make G.711a the only codec that can be used for the call.

Default setting—*027111

<Prefer_G726r32_Code>

Dial prefix to make G.726r32 the preferred codec for the call.

Default setting—*0172632

<Force_G726r32_Code>

Dial prefix to make G.726r32 the only codec that can be used for the call.

Default setting—*0272632

<Prefer_G729a_Code>

Dial prefix to make G.729a the preferred codec for the call.

Default setting—*01729

<Force_G729a_Code>

Dial prefix to make G.729a the only codec that can be used for the call.

Default setting—*02729

<Prefer_G722_Code>

Dial prefix to make G.722 the preferred codec for the call.

Default setting—*01722

<Force_G722_Code>

Dial prefix to make G.722 the only codec that can be used for the call.

Default setting—*02722

<FXS_Port_Impedance>

Sets the electrical impedance of the PHONE port. Choices are: 600, 900, 600+2.16uF, 900+2.16uF, 270+750||150nF, 220+850||120nF,
                                          220+820||115nF, or 200+600||100nF.

Default setting—600

For New Zealand impedance (370+620||310nF), use 270+750||150nF.

<FXS_Port_Input_Gain>

Input gain in dB, up to three decimal places. The range is 6.000 to -12.000.

Default setting—-3

<FXS_Port_Output_Gain>

Output gain in dB, up to three decimal places. The range is 6.000 to -12.000. The Call Progress Tones and DTMF playback level
                                          are not affected by the FXS Port Output Gain parameter.

Default setting—-3

<DTMF_Playback_Level>

Local DTMF playback level in dBm, up to one decimal place. Range: -30–0.

Default setting—-16.0

<DTMF_Playback_Length>

Local DTMF playback duration in milliseconds. Range: 0–65 seconds.

Default setting—0.1

<Detect_ABCD>

To enable local detection of DTMF ABCD, select yes. Otherwise, select no. Default setting—yes

This setting has no effect if DTMF Tx Method is INFO; ABCD is always sent OOB regardless in this setting.

<Playback_ABCD>

To enable local playback of OOB DTMF ABCD, select yes. Otherwise, select no.

Default setting—yes

<Caller_ID_Method>

Default setting—Bellcore(N.Amer, China)

The choices are described below.

Default setting—Bellcore (N.Amer, China)

Bellcore(N.Amer,China): CID, CIDCW, and VMWI. FSK sent after first ring (same as ETSI FSK sent after first ring) (no polarity
                                                reversal or DTAS)

DTMF(Finland, Sweden): CID only. DTMF sent after polarity reversal (and no DTAS) and before first ring.

DTMF(Denmark): CID only. DTMF sent before first ring with no polarity reversal and no DTAS.

ETSI DTMF: CID only. DTMF sent after DTAS (and no polarity reversal) and before first ring.

ETSI DTMF With PR: CID only. DTMF sent after polarity reversal and DTAS and before first ring.

ETSI DTMF After Ring: CID only. DTMF sent after first ring (no polarity reversal or DTAS)

ETSI FSK: CID, CIDCW, and VMWI. FSK sent after DTAS (but no polarity reversal) and before first ring. Waits for ACK from a
                                                device after DTAS for CIDCW.

ETSI FSK With PR (UK): CID, CIDCW, and VMWI. FSK is sent after polarity reversal and DTAS and before first ring. Waits for
                                                ACK from a device after DTAS for CIDCW. Polarity reversal is applied only if equipment is on hook.

DTMF (Denmark) with PR: CID only. DTMF sent after polarity reversal (and no DTAS) and before first ring.

Default setting—Bellcore(N.Amer, China)

<FXS_Port_Power_Limit>

The choices are from 1 to 8.

Default setting—3

<Caller_ID_FSK_Standard>

The ATA supports bell 202 and v.23 standards for caller ID generation.

Default setting—bell 202

<Feature_Invocation_Method>

Select the method you want to use, Default or Sweden default.

Default setting—Default

<DECT_Enable>

To enable this handset for service, select yes. Otherwise, select no.

Default setting—yes

<Call_Park_Enable>

Enables or disables Call Park.

Default setting—No

<Call_Pickup_Enable>

Enables or disables Call Pickup.

Default setting—No

<Call_Group_Pickup_Enable>

Enables or disables Group Pickup.

Default setting—No

<Outgoing_Lines>

A comma-separated list of the index numbers (1~10) for the lines that are available from this handset for an outgoing call.
                                          These lines will be listed on the phone screen when the user displays the call options or holds down the green call button.

Example : 1,2,8

In this example, a user can select DECT line 1, 2, or 8 for an outbound call.

Default setting—1

You also can choose these lines from the DECT Handset Outgoing Line Selection section of the Quick Setup page.

<Failover>

When this feature is enabled and a call fails through the selected line, the ATA automatically attempts to place the call
                                          over another enabled DECT line. Select yes to enable this feature or select no to disable it.

Default setting—no

<Deregister>

To deregister a handset, select yes. After you submit the settings and the voice module reboots, then the handset is deregistered.
                                          At that point, this parameter is reset to the default value.

Default setting—no

<Bound_IPEI>

Enter the device’s IPEI number (a unique hardware identifier comparable to a MAC address) if you want to bind this device
                                          to the specified handset ID, such as Handset 3. The IPEI can be found in the Settings > Phone Info menu on the handset.

Default setting—blank

| <Restricted_Access_Domains> | Domain of the service provider to which the ATA is connected to. It prevents the ATA from connecting to other service providers. |
|---|---|
| <Enable_Web_Admin_Access> | This feature is not available in ATA web voice. |
| <IVR_Admin_Password> | Password for the administrator to manage the ATA by using the built-in IVR through a connected phone. |
| <Network_Startup_Delay> | The number of seconds of delay between restarting the voice module and initializing network interface. Default setting—3 |

| <DNS_Query_TTL_Ignore> | In DNS packages, the server will suggest a TTL value to the client; if this parameter is set to yes, the value from the server
                                          will be ignored. Default setting—Yes |
|---|---|
| <Survivability_Test_Mode> | Determines whether the ATA will always register to the Local Survivability Gateway (LSG) nodes even though the Webex Calling
                                          Session Signaling Engine (SSE) nodes are reachable. This test mode is used to verify the functions of the LSG nodes. Default setting—No |

| <FIPS_Mode> | To enable the Federal Information Processing Standards (FIPS 140-3) mode on the ATA to meet the security requirements for
                                          cryptographic modules. Allowed values are Disabled and Enabled . Default setting—Disabled |
|---|---|
| <TLS_Min_Version> | Select the minimum protocol version for the TLS connections. Allowed values: TLS 1.0 , TLS 1.1 , TLS 1.2 , and TLS 1.3 . Default setting—TLS 1.1 |

| <Provision_Enable> | Controls all resync actions independently of firmware upgrade actions. Set to yes to enable remote provisioning. Default setting—Yes |
|---|---|
| <Resync_On_Reset> | Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades. Default setting—Yes |
| <Resync_Random_Delay> | The maximum value for a random time interval that the ATA waits before making its initial contact with the provisioning server.
                                          This delay is effective only on the initial configuration attempt following power-on or reset. The delay is a pseudorandom
                                          number between zero and this value. This parameter is in units of 20 seconds; the default value of 2 represents 40 seconds. This feature is disabled when this parameter is set to zero. This feature can be used to prevent an overload of the provisioning
                                          server when a large number of devices power-on simultaneously. Default setting—2 (40 seconds) |
| <Resync_At_HHmm> | The time of day when the device tries to resync. The resync is performed each day. Used in conjunction with the Resync At
                                          Random Delay. Default setting—blank |
| <Resync_At_Random_Delay> | Used in conjunction with the Resync At (HHmm) setting, this parameter sets a range of possible values for the resync delay.
                                          The system randomly chooses a value from this range and waits the specified number of seconds before attempting to resync.
                                          This feature is intended to prevent the network jam that would occur if all resynchronizing devices began the resync at the
                                          exact same time of day. Default setting—600 |
| <Resync_Periodic> | The time interval between periodic resyncs with the provisioning server. The associated resync timer is active only after
                                          the first successful synchronization with the server. Setting this parameter to zero disables periodic resynchronization. Default setting—3600 seconds |
| <Resync_Error_Retry_Delay> | Resync retry interval (in seconds) applied in case of resync failure. The ATA has an error retry timer that activates if the
                                          previous attempt to sync with the provisioning server fails. The ATA waits to contact the server again until the timer counts
                                          down to zero. This parameter is the value that is initially loaded into the error retry timer. If this parameter is set to
                                          zero, the ATA does not try to resync with the provisioning server following a failed attempt. Default setting—3600 seconds |
| <Forced_Resync_Delay> | Maximum delay (in seconds) that the ATA waits before performing a resync. The ATA does not resync while one of its lines is
                                          active. Because a resync can take several seconds, it is desirable to wait until the ATA has been idle for an extended period
                                          before resynchronizing. This allows a user to make calls in succession without interruption. The ATA has a timer that begins
                                          counting down when all of its lines become idle. This parameter is the initial value of the counter. Resync events are delayed until this counter decrements to zero. Default setting—14400 seconds |
| <Resync_From_SIP> | Enables a resync to be triggered via a SIP NOTIFY message. Default setting—yes |
| <Resync_After_Upgrade_Attempt> | Triggers a resync after every firmware upgrade attempt. Default setting—Yes |
| <Resync_Trigger_1> <Resync_Trigger_2> | Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE. Default setting—blank |
| <Resync_Fails_On_FNF> | Determines whether a file-not-found response from the provisioning server constitutes a successful or a failed resync. A failed resync activates the error resync timer. Default setting—Yes |
| <Profile_Rule> | This parameter is a profile script that evaluates to the provisioning resync command. The command is a TCP/IP operation and
                                          an associated URL. The TCP/IP operation can be TFTP, HTTP, or HTTPS. If the command is not specified, TFTP is assumed, and
                                          the address of the TFTP server is obtained through DHCP option 66. In the URL, either the IP address or the FQDN of the server can be specified. The file name can have macros, such as $MA,
                                          which expands to the ATA MAC address. Default setting—/ata$PSN.cfg |
| <Profile_Rule_B> <Profile_Rule_C> <Profile_Rule_D> | Defines second, third, and fourth resync commands and associated profile URLs. These profile scripts are executed sequentially after the primary Profile Rule resync operation has completed. If a resync
                                          is triggered and Profile Rule is blank, Profile Rule B, C, and D are still evaluated and executed. Default setting—blank |
| <Log_Resync_Request_Msg> | This parameter contains the message that is sent to the Syslog server at the start of a resync attempt. Default setting—$PN $MAC – Requesting resync $SCHEME://$SERVIP:$PORT$PATH |
| <Log_Resync_Success_Msg> | Syslog message issued upon successful completion of a resync attempt. Default setting—$PN $MAC – Successful resync $SCHEME://$SERVIP:$PORT$PATH |
| <Log_Resync_Failure_Msg> | Syslog message issued after a failed resync attempt. Default setting—$PN $MAC -- Resync failed: $ERR |
| <Report_Rule> | The target URL to which configuration reports are sent. This parameter has the same syntax as the Profile_Rule parameter,
                                          and resolves to a TCP/IP command with an associated URL. A configuration report is generated in response to an authenticated SIP NOTIFY message, with Event: report. The report is
                                          an XML file containing the name and value of all the device parameters. This parameter may optionally contain an encryption key. For example: [ --key $K ] tftp://ps.callhome.net/$MA/rep.xml.enc Default setting—blank |
| <Upgrade_Enable> | Determines whether or not firmware upgrade operations can occur independently of resync actions. Default setting—Yes |
| <Upgrade_Error_Retry_Delay> | The upgrade retry interval (in seconds) applied in case of upgrade failure. The ATA has a firmware upgrade error timer that
                                          activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next firmware
                                          upgrade attempt occurs when this timer counts down to zero. Default setting—3600 seconds |
| <Downgrade_Rev_Limit> | Enforces a lower limit on the acceptable version number during a firmware upgrade or downgrade. The ATA does not complete
                                          a firmware upgrade operation unless the firmware version is greater than or equal to this parameter. Default setting—blank |
| <Upgrade_Rule> | This parameter is a firmware upgrade script with the same syntax as Profile_Rule. Defines upgrade conditions and associated
                                          firmware URLs. Default setting—blank |
| <Log_Upgrade_Request_Msg> | Syslog message issued at the start of a firmware upgrade attempt. Default setting—$PN $MAC – Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH |
| <Log_Upgrade_Success_Msg> | Syslog message issued after a firmware upgrade attempt completes successfully. Default setting—$PN $MAC – Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR |
| <Log_Upgrade_Failure_Msg> | Syslog message issued after a failed firmware upgrade attempt. Default setting—$PN $MAC – Upgrade failed: $ERR |
| <License_Keys> | This field is not currently used. |

| <Custom_CA_URL> | The URL of a file location for a custom Certificate Authority (CA) certificate. Either the IP address or the FQDN of the server
                                          can be specified. The file name can have macros, such as $MA, which expands to the ATA MAC address. Default setting—blank |
|---|---|
| <GPP_A> to <GPP_P> | General purpose provisioning parameters. These parameters can be used as variables in provisioning and upgrade rules. They
                                          are referenced by prepending the variable name with a ‘$’ character, such as $A for GPP_A. Default setting—blank |
| <GPP_SA> to <GPP_SD> | The two-letter upper-case macro names SA through SD identify GPP_SA through GPP_SD as a special case when used as arguments
                                          of the key URL option. |

| <MIC_Cert_Refresh_Enable> | Controls whether to enable the MIC certificate renewal procedure. Default setting—No |
|---|---|
| <MIC_Cert_Refresh_Rule> | HTTP URL for requesting the renewed MIC certificate from the SUDI server. Default setting—http://sudirenewal.cisco.com/ |

| <Max_Forward> | The maximum times a call can be forwarded. The valid range is from 1 to 255. Default setting—70 |
|---|---|
| <Max_Redirection> | Number of times an invite can be redirected to avoid an infinite loop. Default setting—5. |
| <Max_Auth> | The maximum number of times (from 0 to 255) a request may be challenged. Default setting—2 |
| <SIP_User_Agent_Name> | The User-Agent header used in outbound requests. If empty, the header is not included. Macro expansion of $A to $D corresponding
                                          to GPP_A to GPP_D allowed. Default setting—$VERSION |
| <SIP_Server_Name> | The server header used in responses to inbound responses. Default setting—$VERSION |
| <SIP_Reg_User_Agent_Name> | The User-Agent name to be used in a REGISTER request. If this value is not specified, the SIP User Agent Name parameter is
                                          also used for the REGISTER request. Default setting—blank |
| <SIP_Accept_Language> | Accept-Language header used. There is no default (this indicates that the ATA does not include this header) If empty, the
                                          header is not included. Default setting—blank |
| <DTMF_Relay_MIME_Type> | The MIME Type used in a SIP INFO message to signal a DTMF event. Default setting—application/dtmf-relay. |
| <Hook_Flash_MIME_Type> | The MIME Type used in a SIP INFO message to signal a hook flash event. Default setting—application/hook-flash |
| <Remove_Last_Reg> | Determines whether or not the ATA removes the last registration before submitting a new one, if the value is different. Select
                                          yes to remove the last registration, or select no to omit this step. Default setting—no |
| <Use_Compact_Header> | Determines whether or not the ATA uses compact SIP headers in outbound SIP messages. Select yes or no from the dropdown list.
                                          Select yes to use compact SIP headers in outbound SIP messages. Select no to use normal SIP headers. If inbound SIP requests
                                          contain compact headers, the ATA reuses the same compact headers when generating the response regardless the settings of the
                                          Use Compact Header parameter. If inbound SIP requests contain normal headers, the ATA substitutes those headers with compact
                                          headers (if defined by RFC 261) if Use Compact Header parameter is set to yes. Default setting—no |
| <Escape_Display_Name> | Determines whether or not the Display Name is private. Select yes if you want the ATA to enclose the string (configured in
                                          the Display Name) in a pair of double quotes for outbound SIP messages. If the display name includes " or \, these will be
                                          escaped to \" and \\ within the double quotes. Otherwise, select no. Default setting—no |
| <RFC_2543_Call_Hold> | Configures the type of call hold: a:sendonly or 0.0.0.0. Do not use the 0.0.0.0 syntax in a HOLD SDP; use the a:sendonly syntax. Default setting—no |
| <Mark_all_AVT_Packets> | Select yes if you want all AVT tone packets (encoded for redundancy) to have the marker bit set for each DTMF event. Select
                                          no to have the marker bit set only for the first packet. Default setting—yes |
| <SIP_TCP_Port_Min> | The lowest TCP port number that can be used for SIP sessions. Default setting—5060 |
| <SIP_TCP_Port_Max> | The highest TCP port number that can be used for SIP sessions. Default setting—5080 |
| <CTI_Enable> | Enables or disables the Computer Telephone Interface feature provided by some servers. Default setting—no |

| <SIP_T1> | RFC 3261 T1 value (round-trip time estimate), which can range from 0 to 64 seconds. Default setting—0.5 |
|---|---|
| <SIP_T2> | RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses), which can range from 0 to 64
                                          seconds. Default setting—4 |
| <SIP_T4> | RFC 3261 T4 value (maximum duration a message remains in the network), which can range from 0 to 64 seconds. Default setting—5 |
| <SIP_Timer_B> | INVITE time-out value, which can range from 0 to 64 seconds. Default setting—32 |
| <SIP_Timer_F> | Non-INVITE time-out value, which can range from 0 to 64 seconds. Default setting—32 |
| <SIP_Timer_H> | H INVITE final response, time-out value, which can range from 0 to 64 seconds. Default setting—32 |
| <SIP_Timer_D> | ACK hang-around time, which can range from 0 to 64 seconds. Default setting—32 |
| <SIP_Timer_J> | Non-INVITE response hang-around time, which can range from 0 to 64 seconds. Default setting—32 |
| <INVITE_Expires> | INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Range: 0–(231–1) Default setting—240 |
| <ReINVITE_Expires> | ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Range: 0–(231–1) Default setting—30 |
| <Reg_Min_Expires> | Minimum registration expiration time allowed from the proxy in the Expires header or as a Contact header parameter. If the
                                          proxy returns a value less than this setting, the minimum value is used. Default setting—1 |
| <Reg_Max_Expires> | Maximum registration expiration time allowed from the proxy in the Min-Expires header. If the value is larger than this setting,
                                          the maximum value is used. Default setting—7200 |
| <Reg_Retry_Intvl> | Interval to wait before the ATA retries registration after failing during the last registration. Default setting—30 |
| <Reg_Retry_Long_Intvl> | When registration fails with a SIP response code that does not match Retry Reg RSC, the ATA waits for the specified length
                                          of time before retrying. If this interval is 0, the ATA stops trying. This value should be much larger than the Reg Retry
                                          Intvl value, which should not be 0. Default setting—1200 |
| <Reg_Retry_Random_Delay> | Random delay range (in seconds) to add to Register Retry Intvl when retrying REGISTER after a failure. Default setting—0 (disabled) |
| <Reg_Retry_Long_Random_Delay> | Random delay range (in seconds) to add to Register Retry Long Intvl when retrying REGISTER after a failure. Default setting—0 (disabled) |
| <Reg_Retry_Intvl_Cap> | The maximum value to cap the exponential back-off retry delay (which starts at Register Retry Intvl and doubles on every REGISTER
                                          retry after a failure) In other words, the retry interval is always at Register Retry Intvl seconds after a failure. If this
                                          feature is enabled, Reg Retry Random Delay is added on top of the exponential back-off adjusted delay value. Default setting—0, which disables the exponential backoff |
| <SIT1_RSC> <SIT2_RSC> <SIT3_RSC> <SIT4_RSC> | SIP response status code for the corresponding Special Information Tone (SIT), SIT1 through SIT4. For example, if you set
                                          the SIT1 RSC to 404, when the user makes a call and a failure code of 404 is returned, the SIT1 tone is played. Reorder or
                                          Busy tone is played by default for all unsuccessful response status code for SIT 1 RSC through SIT 4 RSC. Default setting—blank |
| <Try_Backup_RSC> | SIP response code that retries a backup server for the current request. Default setting—blank |
| <Retry_Reg_RSC> | Interval to wait before the ATA retries registration after failing during the last registration. Default setting—blank |

| <RTP_Port_Min> | Minimum port number for RTP transmission and reception. The RTP Port Min and RTP Port Max parameters should define a range
                                          that contains at least 4 even number ports, such as 100 –106. Default setting—16384. |
|---|---|
| <RTP_Port_Max> | Maximum port number for RTP transmission and reception. Default setting—16482. |
| <RTP_Packet_Size> | Packet size in seconds, which can range from 0.01 to 0.16. Valid values must be a multiple of 0.01 seconds. Default setting—0.030 |
| <Max_RTP_ICMP_Err> | Number of successive ICMP errors allowed when transmitting RTP packets to the peer before the ATA terminates the call. If
                                          value is set to 0, the ATA ignores the limit on ICMP errors. Default setting—0 |
| <RTCP_Tx_Interval> | Interval for sending out RTCP sender reports on an active connection. It can range from 0 to 255 seconds. During an active
                                          connection, the ATA can be programmed to send out compound RTCP packet on the connection. Each compound RTP packet except
                                          the last one contains a SR (Sender Report) and a SDES (Source Description) The last RTCP packet contains an additional BYE
                                          packet. Each SR except the last one contains exactly 1 RR (Receiver Report); the last SR carries no RR. The SDES contains
                                          CNAME, NAME, and TOOL identifiers. The CNAME is set to <User ID>@<Proxy>, NAME is set to <Display Name> (or Anonymous if user
                                          blocks caller ID), and TOOL is set to the Vendor/Hardwareplatform-softwareversion. The NTP timestamp used in the SR is a snapshot
                                          of the local time for the ATA, not the time reported by an NTP server. If the ATA receives a RR from the peer, it attempts
                                          to compute the round trip delay and show it as the Call Round Trip Delay value (ms) on the Information page. Default setting—0 |
| <No_UDP_Checksum> | Select yes if you want the ATA to calculate the UDP header checksum for SIP messages. Otherwise, select no. Default setting—no |
| <Stats_In_BYE> | Determines whether the ATA includes the PRTP-Stat header or response in a BYE message. The header contains the RTP statistics
                                          of the current call. Select yes or no from the dropdown list. Default setting—yes The format of the P-RTP-Stat header is: P-RTP-State: PS=<packets sent>,OS=<octets sent>,PR=<packets received>,OR=<octets eceived>,PL=<packets lost>,JI=<jitter in
                                          ms>,LA=<delay in ms>,DU=<call durationins>,EN=<encoder>,DE=<decoder>. |

| <NSE_Dynamic_Payload> | NSE dynamic payload type. The valid range is 96-127. Default setting—100 |
|---|---|
| <AVT_Dynamic_Payload> | AVT dynamic payload type. The valid range is 96-127. Default setting—101 |
| <INFOREQ_Dynamic_Payload> | INFOREQ dynamic payload type. Default setting—blank |
| <G726r32_Dynamic_Payload> | G726r32 dynamic payload type. Default setting—2 |
| <EncapRTP_Dynamic_Payload> | EncapRTP Dynamic Payload type. Default setting—112 |
| <RTP-Start-Loopback_Dynamic_Payload> | RTP-Start-Loopback Dynamic Payload type. Default setting—113 |
| <RTP-Start-Loopback_Codec> | RTP-Start-Loopback Codec. Select one of the following: G711u, G711a, G726-32, G729a. Default setting—G711u |
| <NSE_Codec_Name> | NSE codec name used in SDP. Default setting—NSE |
| <AVT_Codec_Name> | AVT codec name used in SDP. Default setting—telephone-event |
| <G711u_Codec_Name> | G.711u codec name used in SDP. Default setting—PCMU |
| <G711a_Codec_Name> | G.711a codec name used in SDP. Default setting—PCMA |
| <G726r32_Codec_Name> | G.726-32 codec name used in SDP. Default setting—G726-32 |
| <G729a_Codec_Name> | G.729a codec name used in SDP. Default setting—G729a |
| <G722_Codec_Name> G.722 codec name used in SDP. | Default setting—G722 |
| <EncapRTP_Codec_Name> | EncapRTP codec name used in SDP. Default setting—encaprtp |

| <Handle_VIA_received> | If you select yes, the ATA processes the received parameter in the VIA header (this value is inserted by the server in a response
                                          to any one of its requests) If you select no, the parameter is ignored. Select yes or no from the drop-down menu. Default setting—no |
|---|---|
| <Handle_VIA_rport> | If you select yes, the ATA processes the rport parameter in the VIA header (this value is inserted by the server in a response
                                          to any one of its requests) If you select no, the parameter is ignored. Select yes or no from the drop-down menu. Default setting—no |
| <Insert_VIA_received> | Inserts the received parameter into the VIA header of SIP responses if the receivedfrom IP and VIA sent-by IP values differ.
                                          Select yes or no from the drop-down menu. Default setting—no |
| <Insert_VIA_rport> | Inserts the rport parameter into the VIA header of SIP responses if the receivedfrom IP and VIA sent-by IP values differ.
                                          Select yes or no from the drop-down menu. Default setting—no |
| <Substitute_VIA_Addr> | Lets you use NAT-mapped IP:port values in the VIA header. Select yes or no from the drop-down menu. Default setting—no |
| <Send_Resp_To_Src_Port> | Sends responses to the request source port instead of the VIA sent-by port. Select yes or no from the drop-down menu. Default setting—no |
| <STUN_Enable> | Enables the use of STUN to discover NAT mapping. Select yes or no from the dropdown menu. Default setting—no |
| <STUN_Test_Enable> | If the STUN Enable feature is enabled and a valid STUN server is available, the ATA can perform a NAT-type discovery operation
                                          when it powers on. It contacts the configured STUN server, and the result of the discovery is reported in a Warning header
                                          in all subsequent REGISTER requests. If the ATA detects symmetric NAT or a symmetric firewall, NAT mapping is disabled. Default setting—no |
| <STUN_Server> | IP address or fully-qualified domain name of the STUN server to contact for NAT mapping discovery. Default setting—blank |
| <EXT_IP> | External IP address to substitute for the actual IP address of the ATA in all outgoing SIP messages. If 0.0.0.0 is specified,
                                          no IP address substitution is performed. If this parameter is specified, the ATA assumes this IP address when generating SIP
                                          messages and SDP (if NAT Mapping is enabled for that line) However, the results of STUN and VIA received parameter processing,
                                          if available, supersede this statically configured value. This option requires that you have (1) a static IP address from
                                          your Internet Service Provider and (2) an edge device with a symmetric NAT mechanism. If the ATA is the edge device, the second
                                          requirement is met. Default setting—blank |
| <EXT_RTP_Port_Min> | External port mapping number of the RTP Port Min. number. If this value is not zero, the RTP port number in all outgoing SIP
                                          messages is substituted for the corresponding port value in the external RTP port range. Default setting—blank |
| <NAT_Keep_Alive_Intvl> | Interval between NAT-mapping keep alive messages. Default setting—15 |
| <Redirect_Keep_Alive> | Interval between NAT Redirect keep alive messages. Default setting—15 |

| <Line_Enable_1> <Line_Enable_2> | To enable this line for service, select yes. Otherwise, select no. Default setting—yes |
|---|---|

| <SAS_Enable_1> <SAS_Enable_2> | To enable the use of the line as a streaming audio source, select yes. Otherwise, select no. If enabled, the line cannot be
                                          used for outgoing calls. Instead, it auto-answers incoming calls and streams audio RTP packets to the caller. Default setting—no |
|---|---|
| <SAS_DLG_Refresh_Intvl_1> <SAS_DLG_Refresh_Intvl_2> | If this value is not zero, it is the interval at which the streaming audio server sends out session refresh (SIP re-INVITE)
                                          messages to determine whether the connection to the caller is still active. If the caller does not respond to the refresh
                                          message, the ATA ends this call with a SIP BYE message. The range is 0 to 255 seconds (0 means that the session refresh is
                                          disabled.) Default setting—30 |
| <SAS_Inbound_RTP_Sink_1> <SAS_Inbound_RTP_Sink_2> | The purpose of this parameter is to work around devices that do not play inbound RTP if the SAS line declares itself as a
                                          send-only device and tells the client not to stream out audio. This parameter is an FQDN or IP address of an RTP sink to be
                                          used by the SAS line in the SDP of its 200 response to inbound INVITE from a client. It will appear in the c = line and the
                                          port number, if specified, will appear in the m = line of the SDP. If this value is not specified or is equal to 0, then c
                                          =0.0.0.0 and a=sendonly will be used in the SDP to tell the SAS client to not to send any RTP to this SAS line. If a non-zero
                                          value is specified, then a=sendrecv and the SAS client will stream audio to the given address. Special case: If the value
                                          is $IP, then the SAS line’s own IP address is used in the c = line and a=sendrecv. In that case the SAS client will stream
                                          RTP packets to the SAS line. Default setting—blank |

| <NAT_Mapping_Enable_1> <NAT_Mapping_Enable_2> | To use externally mapped IP addresses and SIP/RTP ports in SIP messages, select yes. Otherwise, select no. Default setting—no |
|---|---|
| <NAT_Keep_Alive_Enable_1> <NAT_Keep_Alive_Enable_2> | To send the configured NAT keep alive message periodically, select yes. Otherwise, select no. Default setting—no |
| <NAT_Keep_Alive_Msg_1> <NAT_Keep_Alive_Msg_2> | Enter the keep alive message that should be sent periodically to maintain the current NAT mapping. If the value is $NOTIFY,
                                          a NOTIFY message is sent. If the value is $REGISTER, a REGISTER message without contact is sent. Default setting—$NOTIFY |
| <NAT_Keep_Alive_Dest_1> <NAT_Keep_Alive_Dest_2> | Destination that should receive NAT keep alive messages. If the value is $PROXY, the messages are sent to the current proxy
                                          server or outbound proxy server. Default setting—$PROXY |
| <Blind_Attn-Xfer_Enable_1> <Blind_Attn-Xfer_Enable_2> | Enables the ATA to perform an attended transfer operation by ending the current call leg and performing a blind transfer of
                                          the other call leg. If this feature is disabled, the ATA performs an attended transfer operation by referring the other call
                                          leg to the current call leg while maintaining both call legs. To use this feature, select yes. Otherwise, select no. Default setting—no |
| <MOH_Server_1> <MOH_Server_2> | User ID or URL of the auto-answering streaming audio server. When only a user ID is specified, the current or outbound proxy
                                          is contacted. Music-on-hold is disabled if the MOH Server is not specified. Default setting—blank |
| <Xfer_When_Hangup_Conf_1> <Xfer_When_Hangup_Conf_2> | Makes the ATA perform a transfer when a conference call has ended. Select yes or no from the drop-down menu. Default setting—yes |
| <Conference_Bridge_URL_1> <Conference_Bridge_URL_2> | This feature supports external conference bridging for n-way conference calls (n>2), instead of mixing audio locally. To use
                                          this feature, set this parameter to that of the server's name. For example: conf@mysefver.com:12345 or conf (which uses the
                                          Proxy value as the domain). Default setting—blank |
| <Conference_Bridge_Ports_1> <Conference_Bridge_Ports_2> | Select the maximum number of conference call participants. The range is 3 to 10. Default setting—3 |
| <Enable_IP_Dialing_1> <Enable_IP_Dialing_2> | Enable or disable IP dialing. If IP dialing is enabled, one can dial [userid@] a.b.c.d[:port], where ‘@’, ‘.’, and ‘:’ are dialed by entering * user-id must be numeric (like a phone number) a, b, c, d must be between 0 and 255 port must be larger than 255. If port is not given, 5060 is used. Port and User-Id are optional. If the user-id portion matches a pattern in the dial plan, then it is interpreted as a regular
                                          phone number according to the dial plan. The INVITE message, however, is still sent to the outbound proxy if it is enabled. Default setting—no |
| <Emergency_Number_1> <Emergency_Number_2> | Comma separated list of emergency number patterns. If outbound call matches one of the pattern, the ATA will disable hook
                                          flash event handling. The condition is restored to normal after the call ends. Blank signifies that there is no emergency
                                          number. Maximum number length is 63 characters. Default setting—blank |
| <Mailbox_ID_1> <Mailbox_ID_2> | Enter the ID number of the mailbox for this line. Default setting—blank |
| <Feature_Key_Sync_1> | Allows the phone to synchronize with the call server. If Do Not Disturb or Call Forwarding settings are changed on the phone,
                                          the changes are also made on the server. If changes are made on the server, they are propagated to the phone. Default setting: no |
| <Secure_Call_Option_1> <Secure_Call_Option_2> | Configures a line to only accept secure calls. Options are: Optional: Retains the current secure call option for the phone adapter. Strict: Allows SRTP only when SIP transport is set to TLS and if the ATA receives an unsecure call, the call fails. Allows
                                          RTP only when SIP transport is UDP/TCP and if the ATA receives an unsecure call, the call fails. Default setting: Optional |

| <Company_UUID_1> <Company_UUID_2> | The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider. For example: 19c8168c-a366-44b5-853c-960fcaa19592 Allowed values: Maximum identifier length is 128 characters. Default setting—blank |
|---|---|
| <Primary_Request_URL_1> <Primary_Request_URL_2> | URL of the primary location server that provides the emergency call services. The location server returns an HELD response to the phone with the requested location URI that is tied to the user phone IP
                                          address. This parameter must be in the form of a valid HTTP or HTTPS URL. Allowed values: A valid URL not exceeding 255 characters. Default setting—blank |
| <Secondary_Request_URL_1> <Secondary_Request_URL_2> | URL of the backup server to obtain the user's phone location. If the primary request URL fails, ATA tries to send the secondary request URL to the emergency call services provider. This parameter must be in the form of a valid HTTP or HTTPS URL. Allowed values: A valid URL not exceeding 255 characters. Default setting—blank |

| <Proxy_1> <Proxy_2> | SIP proxy server for all outbound requests. Default setting—blank |
|---|---|
| <Outbound_Proxy_1> <Outbound_Proxy_2> | SIP Outbound Proxy Server where all outbound requests are sent as the first hop. Default setting—blank |
| <Survivability_Proxy_1> <Survivability_Proxy_2> | Specifies a DNS A record of the Local Survivability Gateway (LSG) nodes. String syntax: hostname[:port][:p=priority][:w=weight][:A=ip-list]
[\| hostname2[:port][:p=priority][:w=weight][:A=ip-list]] Where: ip-list: ip-addr[,ip-addr[,ip-addr…]] Default setting—blank |
| <Use_Outbound_Proxy_1> <Use_Outbound_Proxy_2> | Enables the use of an Outbound Proxy. If set to no, the Outbound Proxy and Use OB Proxy in Dialog parameters are ignored. Default setting—no |
| <Use_OB_Proxy_In_Dialog_1> through <Use_OB_Proxy_In_Dialog_2> | Whether to force SIP requests to be sent to the outbound proxy within a dialog. Ignored if the parameter Use Outbound Proxy
                                          is no, or the Outbound Proxy parameter is empty. Default setting—yes |
| <Register_1> <Register_2> | Enable periodic registration with the Proxy parameter. This parameter is ignored if Proxy is not specified. Default setting—yes |
| <Make_Call_Without_Reg_1> <Make_Call_Without_Reg_2> | Allow making outbound calls without successful (dynamic) registration by the unit. If No, dial tone will not play unless registration
                                          is successful. Default setting—no |
| <Register_Expires_1> <Register_Expires_2> | Expires value in sec in a REGISTER request. The ATA will periodically renew registration shortly before the current registration
                                          expired. This parameter is ignored if the Register parameter is no. Range: 0 – (231 – 1) sec. Default setting—3600 |
| <Ans_Call_Without_Reg_1> <Ans_Call_Without_Reg_2> | Allow answering inbound calls without successful (dynamic) registration by the unit. Default setting—no |
| <Use_DNS_SRV_1> <Use_DNS_SRV_2> | Whether to use DNS SRV lookup for Proxy and Outbound Proxy. Default setting—no |
| <DNS_SRV_Auto_Prefix_1> <DNS_SRV_Auto_Prefix_2> | If enabled, the ATA will automatically prepend the Proxy or Outbound Proxy name with _sip._udp when performing a DNS SRV lookup
                                          on that name. Default setting—no |
| <Proxy_Fallback_Intvl_1> <Proxy_Fallback_Intvl_2> | After failing over to a lower priority server, the ATA waits for the specified Proxy Fallback Interval, in seconds, before
                                          retrying the highest priority proxy (or outbound proxy) servers. This parameter is useful only if the primary and backup proxy
                                          server list is provided to the ATA via DNS SRV record lookup on the server name. The ATA can contain up to 10 A records for an SRV record. Using multiple DNS A records per server name does not allow the notion of priority, so all hosts will be considered at the
                                          same priority and the ATA will not attempt to fall back after a failover. If the value is 0, the SIP proxy fallback feature is disabled. Default setting—3600 |
| <Survivability_Proxy_Fallback_Intvl_1> <Survivability_Proxy_Fallback_Intvl_2> | Specifies the interval (in seconds) after which the ATA will try to fallback to the SSE nodes. Default setting—30 seconds |
| <Proxy_Redundancy_Method_1> <Proxy_Redundancy_Method_2> | The method that the ATA uses to create a list of proxies returned in the DNS SRV records. If you select Normal, the list will
                                          contain proxies ranked by weight and priority. If you select Based on SRV port, the ATA also inspects the port number based
                                          on 1st proxy’s port. Default setting—Normal |
| <Mailbox_Subscribe_URL_1> <Mailbox_Subscribe_URL_2> | The URL or IP address of the voicemail server. Default setting—blank |
| <Mailbox_Subscribe_Expires_1> <Mailbox_Subscribe_Expires_2> | The subscription interval for voicemail message waiting indication. When this time period expires, the ATA sends another subscribe
                                          message to the voice mail server. Default: 2147483647 |
| <Display_Name_1> <Display_Name_2> | Display name for caller ID. Default setting—blank |
| <User_ID_1> <User_ID_2> | User ID for this line. Default setting—blank |
| <Password_1> <Password_2> | Password for this line. Default setting—blank |
| <Use_Auth_ID_1> <Use_Auth_ID_2> | To use the authentication ID and password for SIP authentication, select yes. Otherwise, select no to use the user ID and
                                          password. Default setting—no |
| <Auth_ID_1> <Auth_ID_2> | Authentication ID for SIP authentication. Default setting—blank |
| <Reversed_Auth_Realm_1> <Reversed_Auth_Realm_2> | Specify a realm that is used for the authentications of the INVITE and NOTIFY requests. Default setting—blank |
| <Resident_Online_Number_1> <Resident_Online_Number_2> | This setting allows you to associate a "local" telephone number with this line using a valid Skype Online Number from Skype.
                                          Calls made to that number will ring your phone. Enter the number without spaces or special characters. Default setting—blank |
| <SIP URI> | The SIP URI, in the following format: sip:<username>@<WAN_IP>:<port> or sip:<username>@<domain>:<port> |

| <Call_Waiting_Serv_1> <Call_Waiting_Serv_2> | Enable Call Waiting Service. Default setting—yes |
|---|---|
| <Block_CID_Serv_1> <Block_CID_Serv_2> | Enable Block Caller ID Service. Default setting—yes |
| <Block_ANC_Serv_1> <Block,_ANC_Serv_2> | Enable Block Anonymous Calls Service. Default setting—yes |
| <Dist_Ring_Serv_1> <Dist_Ring_Serv_2> | Enable Distinctive Ringing Service. Default setting—yes |
| <Cfwd_All_Serv_1> <Cfwd_All_Serv_2> | Enable Call Forward All Service. Default setting—yes |
| <Cfwd_Busy_Serv_1> <Cfwd_Busy_Serv_2> | Enable Call Forward Busy Service. Default setting—yes |
| <Cfwd_No_Ans_Serv_1> <Cfwd_No_Ans_Serv_2> | Enable Call Forward No Answer Service. Default setting—yes |
| <Cfwd_Sel_Serv_1> <Cfwd_Sel_Serv_2> | Enable Call Forward Selective Service. Default setting—yes |
| <Cfwd_Last_Serv_1> <Cfwd_Last_Serv_2> | Enable Forward Last Call Service Default setting—yes |
| <Block_Last_Serv_1> <Block_Last_Serv_2> | Enable Block Last Call Service. Default setting—yes |
| <Accept_Last_Serv_1> <Accept_Last_Serv_2> | Enable Accept Last Call Service. Default setting—yes |
| <DND_Serv_1> <DND_Serv_2> | Enable Do Not Disturb Service. Default setting—yes |
| <CID–Serv_1> <CID–Serv_2> | Enable Caller ID Service. Default setting—yes |
| <CWCID_Serv_1> <CWCID_Serv_2> | Enable Call Waiting Caller ID Service. Default setting—yes |
| <Call_Return_Serv_1> <Call_Return_Serv_2> | Enable Call Return Service. Default setting—yes |
| <Call_Redial_Serv_1> <Call_Redial_Serv_2> | Enable Call Redial Service. |
| <Call_Back_Serv_1> <Call_Back_Serv_2> | Enable Call Back Service. |
| <Three_Way_Call_Serv_1> <Three_Way_Call_Serv_2> | Enable Three Way Calling Service. Three Way Calling is required for Three Way Conference and Attended Transfer. Default setting—yes |
| <Three_Way_Conf_Serv_1> <Three_Way_Conf_Serv_2> | Enable Three Way Conference Service. Three Way Conference is required for Attended Transfer. Default setting—yes |
| <Attn_Transfer_Serv_1> <Attn_Transfer_Serv_2> | Enable Attended Call Transfer Service. Three Way Conference is required for Attended Transfer. Default setting—yes |
| <Unattn_Transfer_Serv_1> <Unattn_Transfer_Serv_2> | Enable Unattended (Blind) Call Transfer Service. Default setting—yes |
| <MWI_Serv_1> <MWI_Serv_2> | Enable MWI Service. MWI is available only if a Voice Mail Service is set-up in the deployment. Default setting—yes |
| <VMWI_Serv_1> <VMWI_Serv_2> | Enable VMWI Service (FSK) Default setting—yes |
| <Speed_Dial_Serv_1> <Speed_Dial_Serv_2> | Enable Speed Dial Service. Default setting—yes |
| <Secure_Call_Serv_1> <Secure_Call_Serv_2> | Secure Call Service. If this feature is enabled, a user can make a secure call by entering an activation code (*18 by default)
                                          before dialing the target number. Then audio traffic in both directions is encrypted for the duration of the call. Default setting—yes |
| <Referral_Serv_1> <Referral_Serv_2> | Enable Referral Service. See the Referral Services Codes parameter for more information. Default setting—yes |
| <Feature_Dial_Serv_1> <Feature_Dial_Serv_2> | Enable Feature Dial Service. See the Feature Dial Services Codes parameter for more information. Default setting—yes |
| <Service_Announcement_Serv_1> <Service_Announcement_Serv_2> | Enable Service Announcement Service. Default setting—no |
| <Reuse_CID_Number_As_Name_1> <Reuse_CID_Number_As_Name_2> | Use the Caller ID number as the caller name. Default settings: yes |

| <Preferred_Codec_1>,  <Preferred_Codec_2> <Second_Preferred_Codec_1>, <Second_Preferred_Codec_2> <Third_Preferred_Codec_1>, <Third_Preferred_Codec_2> | Up to three codecs to be used for all calls from the specified line/handset, listed order of preference. The actual codec
                                          used in a call depends on the outcome of the codec negotiation protocol. Select one of the following: G711u, G711a, G726-32,
                                          G729a, or G722. Default setting for Preferred Codec: G711u Default setting for Second and Third Preferred Codec: Unspecified |
|---|---|
| <Use_Pref_Codec_Only_1> <Use_Pref_Codec_Only_2> | To use only the preferred codec for all calls, select yes. (The call fails if the far end does not support this codec.) Otherwise,
                                          select no. Default setting—no |
| <Use_Remote_Pref_Codec_1> <Use_Remote_Pref_Codec_2> | To use the preferred codec specified by the remote peer, select yes. Otherwise, select no. Default setting: |
| <Codec_Negotiation_1> <Codec_Negotiation_2> | Specify the codecs for codec negotiation: Default or List All. Default setting—Default |
| <G729a_Enable_1> <G729a_Enable_2> | To enable the use of the G.729a codec at 8 kbps, select yes. Otherwise, select no. Default setting—yes |
| <Silence_Supp_Enable_1> <Silence_Supp_Enable_2> | To enable silence suppression so that silent audio frames are not transmitted, select yes. Otherwise, select no. Default setting—no |
| <G726-32_Enable_1> <G726-32_Enable_2> | To enable the use of the G.726 codec at 32 kbps, select yes. Otherwise, select no. Default setting—yes |
| <Silence_Threshold_1> <Silence_Threshold_2> | Select the appropriate setting for the threshold: high, medium, or low. Default setting—medium |
| <FAX_V21_Detect_Enable_1> <FAX_V21_Detect_Enable_2> | To enable detection of V21 fax tones, select yes. Otherwise, select no. Default setting—yes |
| <Echo_Canc_Enable_1> <Echo_Canc_Enable_2> | To enable the use of the echo canceller, select yes. Otherwise, select no. Default setting—yes |
| <FAX_CNG_Detect_Enable_1> <FAX_CNG_Detect_Enable_2> | To enable detection of the fax Calling Tone (CNG), select yes. Otherwise, select no. Default setting—yes |
| <FAX_Passthru_Codec_1> <FAX_Passthru_Codec_2> | Select the codec for fax passthrough, G711u or G711a. Default setting—G711u |
| <FAX_Codec_Symmetric_1> through <FAX_Codec_Symmetric_2> | To force the ATA to use a symmetric codec during fax passthrough, select yes. Otherwise, select no. Default setting—yes |
| <DTMF_Process_INFO_1> <DTMF_Process_INFO_2> | To use the DTMF process info feature, select yes. Otherwise, select no. Default setting—yes |
| <FAX_Passthru_Method_1> <FAX_Passthru_Method_2> | Select the fax passthrough method: None, NSE, or ReINVITE. Default setting—NSE |
| <DTMF_Process_AVT_1> <DTMF_Process_AVT_2> | To use the DTMF process AVT feature, select yes. Otherwise, select no. Default setting—yes |
| <FAX_Process_NSE_1> <FAX_Process_NSE_2> | To use the fax process NSE feature, select yes. Otherwise, select no. Default setting—yes |
| <DTMF_Tx_Method_1> <DTMF_Tx_Method_2> | Select the method to transmit DTMF signals to the far end: InBand, AVT, INFO, or Auto. InBand sends DTMF by using the audio
                                          path. AVT sends DTMF as AVT events. INFO uses the SIP INFO method. Auto uses InBand or AVT based on the outcome of codec negotiation. Default setting—Auto |
| <FAX_Disable_ECAN_1> <FAX_Disable_ECAN_2> | If enabled, this feature automatically disables the echo canceller when a fax tone is detected. To use this feature, select
                                          yes. Otherwise, select no. Default setting—no |
| <DTMF_Tx_Mode_1> <DTMF_Tx_Mode_2> | DTMF Detection Tx Mode is available for SIP information and AVT. Options are: Strict or Normal. Default setting—Strict for which the following are true: A DTMF digit requires an extra hold time after detection. The DTMF level threshold is raised to -20 dBm. The minimum and maximum duration thresholds are: strict mode for AVT: 70 ms normal mode for AVT: 40 ms strict mode for SIP info: 90 ms normal mode for SIP info: 50 ms |
| <DTMF_Tx_Strict_Hold_Off_Time_1> <DTMF_Tx_Strict_Hold_Off_Time_2> | This parameter is in effect only when DTMF Tx Mode is set to strict, and when DTMF Tx Method is set to out-ofband; i.e. either
                                          AVT or SIP-INFO. The value can be set as low as 40 ms. There is no maximum limit. A larger value will reduce the chance of
                                          talk-off (beeping) during conversation, at the expense of reduced performance of DTMF detection, which is needed for interactive
                                          voice response systems (IVR). Default: 70 ms |
| <FAX_Enable_T38_1> <FAX_Enable_T38_2> | To enable the use of ITU-T T.38 standard for FAX Relay, select yes. Otherwise select no. Default setting—no |
| <Hook_Flash_Tx_Method_1> <Hook_Flash_Tx_Method_2> | Select the method for signaling hook flash events: None, AVT, or INFO. None does not signal hook flash events. AVT uses RFC2833
                                          AVT (event = 16) INFO uses SIP INFO with the single line signal=hf in the message body. The MIME type for this message body
                                          is taken from the Hook Flash MIME Type setting. Default setting—None |
| <FAX_T38_Redundancy_1> <FAX_T38_Redundancy_2> | Select the appropriate number to indicate the number of previous packet payloads to repeat with each packet. Choose 0 for
                                          no payload redundancy. The higher the number, the larger the packet size and the more bandwidth consumed. Default setting—1 |
| <FAX_T38_ECM_Enable_1> <FAX_T38_ECM_Enable_2> | Select yes to enable T.38 Error Correction Mode. Otherwise select no. Default setting—yes |
| <FAX_Tone_Detect_Mode_1> <FAX_Tone_Detect_Mode_2> | This parameter has three possible values: caller or callee: The ATA will detect FAX tone whether it is callee or caller caller only: The ATA will detect FAX tone only if it is the caller callee only: The ATA will detect FAX tone only if it is the callee Default setting—caller or callee. |
| <Symmetric_RTP_1> <Symmetric_RTP_2> | Enable symmetric RTP operation. If enabled, the ATA sends RTP packets to the source address and port of the last received
                                          valid inbound RTP packet. If disabled (or before the first RTP packet arrives) the ATA sends RTP to the destination as indicated
                                          in the inbound SDP. Default setting—no |
| <FAX_T38_Return_to_Voice_1> <FAX_T38_Return_to_Voice_2> | When this feature is enabled, upon completion of the fax image transfer, the connection remains established and reverts to
                                          a voice call using the previously designated codec. Select yes to enable this feature, or select no to disable it. Default setting—no |
| <Dial_Plan_1> <Dial_Plan_2> | The allowed number patterns for outbound calls. The default dial plan script for the line is as follows: (*xx\|[3469]11\|0\|00\|[2-9]xxxxxx\|1xxx[2-9]xxxxxx\|xxxxxxxxxxxx.) Each parameter is separated by a semicolon (;) Examples of Dial Plan Entry and Functionality (*xx Allow arbitrary 2 digit star code [3469]11 Allow x11 sequences 0 Operator 00 International Operator [2-9]xxxxxx US local number 1xxx[2-9]xxxxxx US 1 + 10-digit long distance xxxxxxxxxxxx. Everything else |
| <Encryption_Method_1> <Encryption_Method_2> | Select the encryption algorithm for the SRTP sessions (secure calls). Allowed values: AES 128 and AES 256 GCM . Default setting—AES 128 |

| <Gateway_1_1 <Gateway_4_1> | The first of 4 gateways that can be specified to be used in the <Dial Plan> to facilitate call routing specification (that
                                          overrides the given proxy information). This gateway is represented by gw1 in the <Dial Plan>. For example, the rule 1408xxxxxxx<:@gw1>
                                          can be added to the dial plan such that when the user dials 1408+7digits, the call will be routed to Gateway 1. Without the
                                          <:@gw1> syntax, all calls are routed to the given proxy by default (except IP dialing). Default setting—blank |
|---|---|
| <GW1_NAT_Mapping_Enable_1> <GW4_NAT_Mapping_Enable_1> | If enabled, the ATA uses NAT mapping when contacting Gateway 1. Default setting—no |
| <GW1_Auth_ID_1_ > <GW4_Auth_ID_1_ > | This value is the authentication user-id to be used by the ATA to authenticate itself to Gateway 1. Default setting—blank |
| <GW1_Password_1> <GW4_Password_1> | This value is the password to be used by the ATA to authenticate itself to Gateway 1. Default setting—blank |
| <Auto_PSTN_Fallback_1> <Auto_PSTN_Fallback_2> | If enabled, the ATA automatically routes all calls to the PSTN gateway when the SIP proxy is down (registration failure or
                                          network link down). Default setting—yes |

| <Cfwd_No_Ans_Dest_1> <Cfwd_No_Ans_Dest_2> | Forward number for Call Forward No Answer Service. Same as Cfwd All Dest. Default setting—blank |
|---|---|
| <Cfwd_No_Ans_Delay_1> <Cfwd_No_Ans_Delay_2> | Delay in sec before Call Forward No Answer triggers. Same as Cfwd All Dest. Default setting—20 |
| <Idle_Polarity_1> <Idle_Polarity_2> | Polarity before a call is connected: Forward or Reverse. Default setting—Forward |
| <Caller_Conn_Polarity_1> <Caller_Conn_Polarity_2> | Polarity after an outbound call is connected: Forward orReverse. Default setting—Forward. |
| <Callee_Conn_Polarity_1> <Callee_Conn_Polarity_2> | Polarity after an inbound call is connected: Forward or Reverse. Default setting—Forward |

| <Cfwd_All_Dest_1> <Cfwd_All_Dest_2> | Forward number for Call Forward All Service. Default setting—blank |
|---|---|
| <Cfwd_Busy_Dest_1> <Cfwd_Busy_Dest_2> | Forward number for Call Forward Busy Service. Same as Cfwd All Dest. Default setting—blank |
| <Cfwd_Sel1_Caller_1>,  <Cfwd_Sel8_Caller_1> <Cfwd_Sel1_Caller_1>, <Cfwd_Sel8_Caller_2> | Caller number pattern to trigger Call Forward Selective service. When the caller’s phone number matches the entry, the call
                                          is forwarded to the corresponding Cfwd Selective Destination (Cfwd Sel1-8 Dest). Use ? to match any single digit. Use * to match any number of digits Example : 1408*, 1512???1234 In the above example, a call is forwarded to the corresponding destination if the caller ID either starts with 1408 or is
                                          an 11-digit numbering starting with 1512 and ending with 1234. Default setting—blank |
| <Cfwd_Sel1_Dest_1>, <Cfwd_Sel8_Dest_1> <Cfwd_Sel1_Dest_2>, <Cfwd_Sel8_Dest_2> | The destination for the corresponding Call Forward Selective caller pattern (Cfwd Sel1-8 Caller). Default setting—blank |
| <Cfwd_Last_Caller_1> <Cfwd_Last_Caller_2> | The number of the last caller; this caller is actively forwarded to the Cfwd Last Dest via the Call Forward Last service. Default setting—blank |
| <Cfwd_Last_Dest_1> <Cfwd_Last_Dest_2> | The destination for the Cfwd Last Caller. |
| <Block_Last_Caller_1> <Block_Last_Caller_2> | The number of the last caller; this caller is blocked via the Block Last Caller Service. Default setting—blank |
| <Accept_Last_Caller_1> <Accept_Last_Caller_2> | The number of the last caller; this caller is accepted via the Accept Last Caller Service. Default setting—blank |
| <Speed_Dial_2_1>, <Speed_Dial_9_1> <Speed_Dial_2_2>, <Speed_Dial_9_2> | Target phone number (or URL) assigned to speed dial 2, 3, 4, 5, 6, 7, 8, or 9. Default setting—blank |

| <CW_Setting_1> <CW_Setting_2> | Call Waiting on/off for all calls. Default setting—yes |
|---|---|
| <Block_CID_Setting_1> <Block_CID_Setting_2> | Block Caller ID on/off for all calls. Default setting—no |
| <Block_ANC_Setting_1> <Block_ANC_Setting_2> | Block Anonymous Calls on or off. Default setting—no |
| <DND_Setting_1> <DND_Setting_2> | DND on or off. Default setting—no |
| <CID_Setting_1> <CID_Setting_2> | Caller ID Generation on or off. Default setting—yes |
| <CWCID_Setting_1> <CWCID_Setting_2> | Call Waiting Caller ID Generation on or off. Default setting—yes |
| <Dist_Ring_Setting_1> <Dist_Ring_Setting_2> | Distinctive Ring on or off. Default setting—yes |
| <Secure_Call_Setting_1> <Secure_Call_Setting_2> | If yes, all outbound calls are secure calls by default, without requiring the user to dial a star code first. Default setting—no If Secure Call Setting is set to yes, all outbound calls are secure. However, a user can disable security for a call by dialing
                                                *19 before dialing the target number. If Secure Call Setting is set to No, the user can make a secure outbound call by dialing *18 before dialing the target number. A user cannot force inbound calls to be secure or not secure; that depends on whether the caller has security enabled or not. Note This setting is applicable only if Secure Call Serv is set to yes on the line interface. | Note | This setting is applicable only if Secure Call Serv is set to yes on the line interface. |
| Note | This setting is applicable only if Secure Call Serv is set to yes on the line interface. |
| <Message_Waiting_1> <Message_Waiting_2> | Setting this value to yes can activate stutter tone and VMWI signal. This parameter is stored in long term memory and will
                                          survive after reboot or power cycle. Default setting—no |
| <Accept_Media_Loopback_Request_1> <Accept_Media_Loopback_Request_2> | Controls how to handle incoming requests for loopback operation. Default setting—automatic never: Never accepts loopback calls; replies 486 to the caller. automatic: Automatically accepts the call without ringing. manual: Rings the phone first, and the call must be picked up manually before loopback starts. Default setting—Automatic |
| <Media_Loopback_Mode_1> <Media_Loopback_Mode_2> | The loopback mode to assume locally when making call to request media loopback. Choices are: Source and Mirror. Default setting—source Note If the ATA answers the call, the mode is determined by the caller. | Note | If the ATA answers the call, the mode is determined by the caller. |
| Note | If the ATA answers the call, the mode is determined by the caller. |
| <Media_Loopback_Type_1> <Media_Loopback_Type_2> | The loopback type to use when making call to request media loopback operation. Choices are Media and Packet. Default setting—media Note that if the ATA answers the call, then the loopback type is determined by the caller (the ATA always picks the first
                                          loopback type in the offer if it contains multiple type.) |
| <Ring1_Caller_1_ > through <Ring8_Caller_1_ > <Ring1_Caller_2_ > through <Ring8_Caller_2_ > <FAX_CNG_Detect_Enable_1> | Caller number pattern to play Distinctive Ring/CWT 1, 2, 3, 4, 5, 6, 7, or 8. Caller number patterns are matched from Ring
                                          1 to Ring 8. The first match (not the closest match) will be used for alerting the subscriber. Default setting—blank |

| Note | This setting is applicable only if Secure Call Serv is set to yes on the line interface. |
|---|---|

| Note | If the ATA answers the call, the mode is determined by the caller. |
|---|---|

| <Default_Ring_1> <Default_Ring_2> | Default ringing pattern, 1–8, for all callers. Default setting—1 |
|---|---|
| <Default_CWT_1> <Default_CWT_2> | Default CWT pattern, 1–8, for all callers. Default setting—1 |
| <Hold_Reminder_Ring_1> <Hold_Reminder_Ring_2> | Ring pattern for reminder of a holding call when the phone is on-hook. Default setting—8 |
| <Hold_Reminder_Ring_1> <Hold_Reminder_Ring_2> | Ring pattern for reminder of a holding call when the phone is on-hook. Default setting—8 |
| <Call_Back_Ring_1> <Call_Back_Ring_2> | Ring pattern for call back notification. Default setting—7 |
| <Cfwd_Ring_Splash_Len_1> <Cfwd_Ring_Splash_Len_2> | Duration of ring splash when a call is forwarded (0 – 10.0s) Default setting—0 |
| <Cblk_Ring_Splash_Len_1> <Cblk_Ring_Splash_Len_2> | Duration of ring splash when a call is blocked (0 – 10.0s) Default setting—0 |
| <VMWI_Ring_Policy_1> <VMWI_Ring_Policy_2> | Duration of ring splash when new messages arrive before the VMWI signal is applied (0 – 10.0s) Default setting: 0 |
| <Ring_On_No_New_VM_1> <Ring_On_No_New_VM_2> | The parameter controls when a ring splash is played when a the VM server sends a SIP NOTIFY message to the ATA indicating
                                          the status of the subscriber’s mail box. Three settings are available. New VM Available: Ring as long as there new voicemail messages. New VM Becomes Available: Ring at the point when the first new voicemail message is received. New VM Arrives: Ring when the number of new voicemail messages increases. Default setting—New VM Available |
| <VMWI_Ring_Splash_Len_1> <VMWI_Ring_Splash_Len_2> | Duration of ring splash when new messages arrive before the VMWI signal is applied (0 – 10.0s) Default setting—0 |
| <Ring_On_No_New_VM_1> <Ring_On_No_New_VM_2> | If enabled, the ATA plays a ring splash when the voicemail server sends SIP NOTIFY message to the ATA indicating that there
                                          are no more unread voice mails. Some equipment requires a short ring to precede the FSK signal to turn off VMWI lamp. Default setting—no |

| <PSTN_Line_Enable_3> | To enable this line for service, select yes. Otherwise, select no. Default setting—yes |
|---|---|
| <Incoming_Handset_List_3> <Incoming_Handset_List_2> | The devices that ring when an incoming call is received on the specified line. Default setting—fxs,1,2,3,4,5,6,7,8,9,10 |

| <SIP_ToS/DiffServ_Value_1> <SIP_ToS/DiffServ_Value_2> | TOS/DiffServ field value in UDP IP packets carrying a SIP message. Default setting—0x68 |
|---|---|
| <SIP_CoS_Value_1> <SIP_CoS_Value_2> | CoS value for SIP messages. Valid values are 0 through 7. Default setting—3 |
| <RTP_ToS/DiffServ_Value_1> <RTP_ToSDiffServ_Value_2> | ToS/DiffServ field value in UDP IP packets carrying RTP data. Default setting—0xb8 |
| <RTP_CoS_Value_1> <RTP_CoS_Value_2> | CoS value for RTP data. Valid values are 0 through 7. Default setting—6 |
| <Network_Jitter_Level_1> <Network_Jitter_Level_2> | Determines how jitter buffer size is adjusted by the ATA. Jitter buffer size is adjusted dynamically. The minimum jitter buffer
                                          size is 30 milliseconds or (10 milliseconds + current RTP frame size), whichever is larger, for all jitter level settings.
                                          However, the starting jitter buffer size value is larger for higher jitter levels. This setting controls the rate at which
                                          the jitter buffer size is adjusted to reach the minimum. Select the appropriate setting: low, medium, high, very high, or
                                          extremely high. Default setting—high |
| <Jitter_Buffer_Adjustment_1> <Jitter_Buffer_Adjustment_2> | Choose yes to enable or no to disable this feature. Default setting—yes |

| <SIP_Transport_1> <SIP_Transport_2> | The TCP choice provides “guaranteed delivery”, which assures that lost packets are retransmitted. TCP also guarantees that
                                          the SIP packages are received in the same order that they were sent. As a result, TCP overcomes the main disadvantages of
                                          UDP. In addition, for security reasons, most corporate firewalls block UDP ports. With TCP, new ports do not need to be opened
                                          or packets dropped, because TCP is already in use for basic activities such as Internet browsing or e-commerce. Options are:
                                          UDP, TCP, TLS , AUTO . AUTO allows the ATA to select the appropriate protocol automatically, based on the NAPTR records on the DNS server. Default setting—UDP |
|---|---|
| <SIP_Port_1> <SIP_Port_2> | Port number of the SIP message listening and transmission port. Default setting—5060 |
| <SIP_100REL_Enable_1> <SIP_100REL_Enable_2> | To enable the support of 100REL SIP extension for reliable transmission of provisional responses (18x) and use of PRACK requests,
                                          select yes. Otherwise, select no. Default setting—no |
| <EXT_SIP_Port_1> <EXT_SIP_Port_2> | The external SIP port number. Default setting—blank |
| <Auth_Resync-Reboot_1> <Auth_Resync-Reboot_2> | If this feature is enabled, the ATA authenticates the sender when it receives the NOTIFY resync reboot (RFC 2617) message.
                                          To use this feature, select yes. Otherwise, select no. Default setting—yes |
| <SIP_Proxy-Require_1> <SIP_Proxy-Require_2> | The SIP proxy can support a specific extension or behavior when it sees this header from the user agent. If this field is
                                          configured and the proxy does not support it, it responds with the message, unsupported. Enter the appropriate header in the
                                          field provided. Default setting—blank |
| <SIP_Remote-Party-ID_1> <SIP_Remote-Party-ID_2> | To use the Remote-Party-ID header instead of the From header, select yes. Otherwise, select no. Default setting—yes |
| <SIP_GUID_1> <SIP_GUID_2> | This feature limits the registration of SIP accounts. The Global Unique ID is generated for each line for each ATA. When it
                                          is enabled, the ATA adds a GUID header in the SIP request. The GUID is generated the first time the unit boots up and stays
                                          with the unit through rebooting and even factory reset. Default setting—no |
| <RTP_Log_Intvl_1> <RTP_Log_Intvl_2> | The interval for the RTP log. Default setting—0 |
| <Restrict_Source_IP_1> <Restrict_Source_IP_2> | If configured, the ATA drops all packets sent to its SIP Ports from an untrusted IP address. A source IP address is untrusted
                                          if it does not match any of the IP addresses resolved from the configured Proxy (or Outbound Proxy if Use Outbound Proxy is
                                          yes) Default setting—no |
| <Referor_Bye_Delay_1> <Referor_Bye_Delay_2> | The number of seconds to wait before sending a BYE to the referrer to terminate a stale call leg after a call transfer. |
| <Refer_Target_Bye_Delay_1> <Refer_Target_Bye_Delay_2> | The number of seconds to wait before sending a BYE to the refer target to terminate a stale call leg after a call transfer. |
| <Referee_Bye_Delay_1> <Referee_Bye_Delay_2> | The number of seconds to wait before sending a BYE to the referee to terminate a stale call leg after a call transfer. |
| <Refer-To_Target_Contact_1> <Refer-To_Target_Contact_2> | To contact the refer-to target, select yes. Otherwise, select no. Default setting—no |
| <Sticky_183_1> <Sticky_183_2> | If this feature is enabled, the ATA ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound
                                          INVITE. To enable this feature, select yes. Otherwise, select no. Default setting—no |
| <Auth_INVITE_1> <Auth_INVITE_2> | When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy. Default setting—no |
| <Reply_182_On_Call_Waiting_1> <Reply_182_On_Call_Waiting_2> | When enabled, the ATA replies with a SIP182 response to the caller if it is already in a call and the line is off-hook. To
                                          use this feature select yes. Default setting—no |
| <Use_Anonymous_With_RPID_1> <Use_Anonymous_With_RPID_2> | Determines whether or not the ATA uses “Anonymous” when Remote Party ID is requested in the SIP message. Default setting—yes |
| <Use_Local_Addr_In_From_1> <Use_Local_Addr_In_From_2> | Use the local ATA IP address in the SIP FROM message. Default setting—no |
| <Broadsoft_ALTC_1> <Broadsoft_ALTC_2> | Use Broadsoft ALTC SDP negotiation. Default setting—No |
| <Auth_Support_RFC8760_1> <Auth_Support_RFC8760_2> | When enabled, the ATA authorization supports RFC-8760 that specifies the digest algorithms SHA256, SHA-512/256, and MD5. To
                                          enable this feature, select yes. Otherwise, select no. Default setting—No |
| <MediaSec_Request_1> <MediaSec_Request_2> | Determines whether the ATA can initiate media plane security negotiations with the server. When set to Yes, the ATA can initiate
                                          the negotiations. When set to No, ATA can only handle the negotiation requests from the server. Default setting—No |
| <MediaSec_Over_TLS_Only_1> <MediaSec_Over_TLS_Only_2> | Determines how the ATA initiates or handles the media plane security negotiations. When set to Yes, the ATA can initiate or
                                          handle the mediasec negotiations with SIP over TCP only. When set to No, the ATA can initiate or handle the negotiations regardless
                                          of the protocol (UDP/TCP/TLS) for SIP messages. Default setting—No |

| <Dial_Plan_1_3> through <Dial_Plan_8_3> | The PSTN dial plan pool. You can associate a dial plan with a VoIP Caller or a PSTN Caller by referencing the index number
                                          (1~8). Default setting—(xx.) |
|---|---|
| <VoIP-To-PSTN_Gateway_Enable_3> | Choose yes to enable or choose no to disable the VoIP-To-PSTN Gateway functionality. Default setting—yes |
| <VoIP_Caller_Auth_Method_3> | The method to authenticate a VoIP Caller to access the PSTN gateway. Choose from none, PIN, or HTTP Digest. Default setting—none |
| <VoIP_PIN_Max_Retry_3> | The number of times that a VoIP caller can attempt to enter a PIN, if the VoIP Caller Auth Method is set to PIN. Default setting—3 |
| <One_Stage_Dialing_3> | Choose yes to enable or choose no to disable one-stage dialing. This setting applies if the VoIP Caller Auth Method is none
                                          or HTTP Digest, or if caller is in the Access List. Default setting—yes |
| <Line_1_VoIP_Caller_DP_3> | The index number of the dial plan to use when the VoIP Caller is calling from Line 1 of the same ATA during normal operation
                                          (in other words, not due to fallback to PSTN service when Line 1 VoIP service is down). The Authentication is skipped for
                                          Line 1 VoIP caller. Default setting—1 |
| <VoIP_Caller_Default_DP_3> | The index number of the dial plan to use when the VoIP Caller is not authenticated. Default setting—1 |
| <Line_1_Fallback_DP_3> | The index number of the dial plan to use when the VoIP Caller is calling from Line 1 of the same ATA due to fallback to PSTN
                                          service when Line 1 VoIP service is down. Default setting—none |
| <VoIP_Caller_ID_Pattern_3> | A comma-separated list of caller phone number patterns that is used to allow or block access to the PSTN gateway based on
                                          the caller ID. If the caller ID does not match a specified pattern, access is rejected, regardless of the authentication method.
                                          This comparison is applied before the access list is applied. If this parameter is blank (not specified), all callers are
                                          considered for VoIP service. Use ? to match any single digit. Use * to match any number of digits. Example : 1408*, 1512???1234 In the above example, the caller ID either must start with 1408 or must be an 11-digit numbering starting with 1512 and ending
                                          with 1234. Default setting—blank |
| <VoIP_Access_List_3> | A comma-separated list of number patterns that is used to allow or block access to the PSTN gateway based on the source IP
                                          address. If the IP address matches a specified pattern, service is allowed without further authentication. Example : 192.168.*.*, 66.43.12.1??. In the above example, the source IP address either must begin with 192.168 or must be in the range of 66.43.12.100-199. Default setting—blank |
| <VoIP_Caller_1_PIN_3> through <VoIP_Caller_8_PIN_3> | A PIN number that a VoIP caller can use to access the PSTN gateway, when the VoIP Caller Auth Method is set to PIN. Default setting—blank |
| <VoIP_Caller_1_DP_3> through <VoIP_Caller_8_DP_3> | The index number of the dial plan to use upon successful entry of the corresponding VoIP Caller PIN. Default setting—1 |
| <VoIP_User_1_Auth_ID_3> through <VoIP_User_8_Auth_ID_3> | A user ID that a VoIP Caller can use for authentication by using the HTTP Digest method (in other words, by embedding an Authorization
                                          header in the SIP INVITE message sent to the ATA. If the credentials are missing or incorrect, the ATA will challenge the
                                          caller with a 401 response). The VoIP caller whose authentication userid equals to this ID is referred to VoIP User 1 of this ATA. If the caller specifies
                                          an authentication user-id that does not match any of the VoIP User Auth ID’s, the INVITE will be rejected with a 403 response. Default setting—blank. |
| <VoIP_User_1_Password_3> through <VoIP_User_8_Password_3> | The password to be used with VoIP User 1. The user assumes the identity of VoIP User 1 must therefore compute the credentials
                                          using this password, or the INVITE will be challenged with a 401 response Default setting—blank. |
| <VoIP_User_1_DP_3> through <VoIP_User_8_DP_3> | For up to 8 VoIP users, specify the index of the dial plan to be used after successful authentication. If authentication is
                                          disabled, the default dial plan is used for all unknown VoIP users. Default setting—1. |

| <PSTN-To-VoIP_Gateway_Enable_3> | Select yes to enable or select no to disable PSTN-To-VoIP Gateway functionality. Default setting—yes |
|---|---|
| <PSTN_Caller_Auth_Method_3> | The method to authenticate a PSTN Caller to access the VoIP gateway. Choose from none or PIN. Default setting—none |
| <PSTN_Ring_Thru_1_3> | To enable ring through to Line 1 based on caller number patterns, choose yes. Otherwise choose no. Note For more information about PSTN Caller number patterns, see <PSTN_Caller_ID_Pattern_3>. Default setting—yes | Note | For more information about PSTN Caller number patterns, see <PSTN_Caller_ID_Pattern_3>. |
| Note | For more information about PSTN Caller number patterns, see <PSTN_Caller_ID_Pattern_3>. |
| <PSTN_PIN_Max_Retry_3> | The number of times that a PSTN caller can attempt to enter a PIN number, if the authentication method is set to PIN. Default setting—3 |
| <PSTN_CID_for_VoIP_CID_3> | Choose yes or no. Default setting—no |
| <PSTN_CID_Number_Prefix_3> | A dialing prefix, if needed, to add to the caller ID number on the PBX to ensure that a callback goes to the correct number. Default setting—blank |
| <PSTN_Caller_Default_DP_3> | The index number of the dial plan that is used when the PSTN Caller Auth Method is set to none. Default settings: 1 |
| <Line_1_Signal_Hook_Flash_to_PSTN_3> | Specify the operation of the hook flash on the analog phone when a PSTN-to-VoIP call is active. Choose Disabled or Double
                                          Hook Flash. Default setting—Disabled |
| <PSTN_CID_Name_Prefix_3> | The prefix to add to the caller ID name that is sent to the PBX. Enter the characters to add to the caller ID name. Default setting—blank |
| <PSTN_Caller_ID_Pattern_3> | A comma-separated list of phone number patterns that is used to allow or block access to the VoIP gateway based on the caller
                                          ID. If the caller ID does not match a specified pattern, access is rejected, regardless of the authentication method. This
                                          comparison is applied before the access list is applied. If this parameter is blank (not specified), all callers are considered
                                          for VoIP service. Use ? to match any single digit. Use * to match any number of digits. Example : 1408*, 1512???1234 In the above example, the caller ID either must start with 1408 or must be an 11-digit numbering starting with 1512 and ending
                                          with 1234. Default setting—blank |
| <PSTN_Access_List_3> | A comma-separated list of number patterns that is used to allow or block access to the VoIP gateway based on the destination
                                          IP address. If the destination IP address matches a specified pattern, service is allowed without further authentication. Example : 192.168.*.*, 66.43.12.1??. In the above example, the IP address either must begin with 192.168 or must be in the range of 66.43.12.100-199. The default is blank. |
| <PSTN_Caller_1_PIN_3> through <PSTN_Caller_8_PIN_3> | A PIN number that allows a PSTN caller to access to the VoIP gateway. Calls will be subject to the dial plan specified by
                                          the corresponding PSTN Caller DP setting (see below). These settings apply when the PSTN Caller Authentication Method parameter
                                          is set to PIN. Default setting—blank |
| <PSTN_Caller_1_DP_3> through <PSTN_Caller_8_DP_3> | The index number of the dial plan to use upon successful entry of the corresponding PSTN Caller PIN. Default setting—1 |

| Note | For more information about PSTN Caller number patterns, see <PSTN_Caller_ID_Pattern_3>. |
|---|---|

| <VoIP_Answer_Delay_3> | The number of seconds to wait before autoanswering an inbound VoIP call for the FXO account. The range is 0-255. Default setting—0 |
|---|---|
| <VoIP_PIN_Digit_Timeout_3> | After a VoIP caller is prompted for a PIN or enters a digit, the number of seconds to wait for an entry. The range is 0-255. Default setting—10 |
| <PSTN_Answer_Delay_3> | After an inbound PSTN call starts ringing, the number of seconds to wait before autoanswering the call. The range is 0-255. Default setting—16 |
| <PSTN_PIN_Digit_Timeout_3> | After a PSTN caller is prompted for a PIN or enters a digit, the number of seconds to wait for an entry. The range is 0-255. Default setting—10 |
| <PSTN-To-VoIP_Call_Max_Dur_3> | The limit on the duration of a PSTN-To-VoIP Gateway Call. Unit is in seconds. 0 means unlimited. The range is 0-2147483647. Default setting—0 |
| <PSTN_Ring_Thru_Delay_3> | After a PSTN call starts ringing, the number of seconds to wait before ring through to Line 1. In order for Line 1 to have
                                          the caller ID information, this value must be greater than the time required to complete the PSTN caller ID delivery. The
                                          range is 0-255. Default setting—1 |
| <VoIP-To-PSTN_Call_Max_Dur_3> | The limit on the duration of a VoIP-To-PSTN Gateway Call. Unit is in seconds. 0 means unlimited. The range is 0-2147483647. Default setting—0 |
| <PSTN_Ring_Thru_CWT_Delay_3> | When a call is active and a new PSTN call starts ringing, the number of seconds to wait before ring through to Line 1 with
                                          a Call Waiting Tone. Default setting—3 |
| <VoIP_DLG_Refresh_Intvl_3> | The interval between (SIP) Dialog refresh messages sent by the ATA to detect if the VoIP call-leg is still up. If this value
                                          is set to 0, the VoIP call-leg status will not be checked by the ATA. The refresh message is a SIP ReINVITE, and the VoIP
                                          peer must response with a 2xx response. If the VoIP peer does not reply or the response is not greater than 2xx, the ATA will
                                          disconnect both call legs automatically. The range is 0-255. Default setting—0 |
| <PSTN_Ring_Timeout_3> | After a ring burst, the number of seconds to wait before concluding that PSTN ring has ceased. The range is 0-255. Default setting—5 |
| <PSTN_Dialing_Delay_3> | After hook, the number of seconds to wait before dialing a PSTN number. The range is 0-255. Default setting—1 |
| <PSTN_Dial_Digit_Len_3> | The on/off time when the Gateway transmits digits through the Line (FXO) port. The syntax is on-time/off-time, expressed in
                                          seconds. The permitted range is 0.05 to 3.00 (up to two decimal places only). Default setting—.1/.1 |
| <PSTN_Hook_Flash_Len_3> | The length of the hook flash in seconds. Default setting—.25 |
| <Detect_CPC_3> | Choose yes to enable or choose no to disable this feature. CPC is a brief removal of tip-and-ring voltage. If enabled, the
                                          ATA will disconnect both call legs when this signal is detected during a gateway call. Default setting—yes |
| <Detect_Polarity_Reversal_3> | Choose yes to enable or choose no to disable this feature. If enabled, the ATA will disconnect both call legs when this signal
                                          is detected during a gateway call. If it is a PSTN gateway call, the first polarity reversal is ignored and the second one
                                          triggers the disconnection. For VoIP gateway call, the first polarity reversal triggers the disconnection. Default setting—yes |
| <Detect_PSTN_Long_Silence_3> | Choose yes to enable or choose no to disable this feature. If enabled, the ATA will disconnect both call legs when the PSTN
                                          side has no voice activity for a duration longer than the length specified in the Long Silence Duration parameter during a
                                          gateway call. Default setting—no |
| <Detect_VoIP_Long_Silence_3> | Choose yes to enable or choose no to disable this feature. If enabled, the ATA will disconnect both call legs when the VoIP
                                          side has no voice activity for a duration longer than the length specified in the Long Silence Duration parameter during a
                                          gateway call. Default setting—no |
| <PSTN_Long_Silence_Duration_3> | This value is minimum length of PSTN silence (or inactivity) in seconds to trigger a gateway call disconnection if Detect
                                          Long Silence is enabled. Default setting—30 |
| <VoIP_Long_Silence_Duration_3> | This value is minimum length of VoIP silence (or inactivity) in seconds to trigger a gateway call disconnection if Detect
                                          Long Silence is enabled. Default setting—30 |
| <PSTN_Silence_Threshold_3> | This parameter adjusts the sensitivity of PSTN silence detection. Choose from {very low, low, medium, high, very high}. The
                                          higher the setting, the easier to detect silence and hence easier to trigger a disconnection. Default setting—medium |
| <Min_CPC_Duration_3> | Specify the minimum duration of a low tip and ring voltage (below 1V) for the Gateway to recognize it as a CPC signal or PSTN
                                          line removal. Default setting—0.2 |
| <Detect_Disconnect_Tone_3> | Choose yes to enable or choose no to disable this feature. If enabled, the ATA will disconnect both call legs when it detects
                                          the disconnect tone from the PSTN side during a gateway call. Disconnect tone is specified in the Disconnect Tone parameter,
                                          which depends on the region of the PSTN service. Default setting—yes |
| <Disconnect_Tone_3> | This value is the tone script which describes to the ATA the tone to detect as a disconnect tone. The syntax follows a standard
                                          Tone Script with some restrictions. Default value is standard US reorder (fast busy) tone, for 4 seconds. Default setting—480@-30,620@-30;4(.25/.25/1+2) Restrictions: Two frequency components must be given. If single frequency is desired, the same frequency is used for both. The tone level value is not used. –30 (dBm) should be used for now. Only 1 segment set is allowed. Total duration of the segment set is interpreted as the minimum duration of the tone to trigger detection. 6 segments of on/off time (seconds) can be specified. A 10% margin is used to validated cadence characteristics of the tone. |
| <Disconnect_Tone_3> | Disconnect Tone Script values: US—480@-30,620@-30;4(.25/.25/1+2) UK—400@-30,400@-30; 2(3/0/1+2) France—440@-30,440@-30; 2(0.5/0.5/1+2) Germany—440@-30,440@-30; 2(0.5/0.5/1+2) Netherlands—425@-30,425@-30; 2(0.5/0.5/1+2) Sweden—425@-10; 10(0.25/0.25/1) Norway—425@-10; 10(0.5/0.5/1) Italy—425@-30,425@-30; 2(0.2/0.2/1+2) Spain—425@-10; 10(0.2/0.2/1,0.2/0.2/1,0.2/0.6/1) Portugal—425@-10; 10(0.5/0.5/1) Poland—425@-10; 10(0.5/0.5/1) Denmark—425@-10; 10(0.25/0.25/1) New Zealand—400@-15; 10(0.25/0.25/1) Australia—425@-13; 10(0.375/0.375/1) |

| <FXO_Country_Setting_3> | The country of deployment. This setting applies the relevant regional settings for PSTN calls. Default setting—USA |
|---|---|
| <Tip_Ring_Voltage_Adjust_3> | Voltage adjustment. The choices are 3.1V, 3.2V, 3.35V, and 3.5V. Default setting—3.5V. |
| <Ring_Frequency_Min_3> | The lower limit of the ring frequency used to detect the ring signal. Default setting—10 |
| <SPA_To_PSTN_Gain_3> | dB of digital gain (or attenuation if negative) to be applied to the signal sent from the ATA to the PSTN side. The range
                                          is -15 to 12. Default setting—0 |
| <Ring_Frequency_Max_3> | The higher limit of the ring frequency used to detect the ring signal. Default setting—100 |
| <PSTN_To_SPA_Gain_3> | dB of digital gain (or attenuation if negative) to be applied to the signal sent from the PSTN side to the ATA. The range
                                          is -15 to 12. Default setting—0 |
| <Ring_Validation_Time_3> | The minimum signal duration required by the Gateway for recognition as a ring signal. Default setting—256 ms |
| <Ring_Indication_Delay_3> | Choose from {0, 512, 768, 1024, 1280, 1536, 1792} (ms). Default setting—512ms |
| <Ring_Timeout_3> | Choose from {0, 128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280, 1408, 1536, 1664, 1792, 1920} (ms). Default setting—640 ms |
| <Ring_Threshold_3> | Choose from {13.5–16.5, 19.35–2.65, 40.5–49.5} (Vrms). Default setting—13.5-16.5 Vrms |
| <Line-In-Use_Voltage_3> | The voltage threshold at which the ATA assumes the PSTN is in use by another handset sharing the same line (and will declare
                                          PSTN gateway service not available to incoming VoIP callers). Default setting—30 |
| <Dial_Tone> | Prompts the user to enter a phone number. Reorder Tone is played automatically when Dial Tone or any of its alternatives times
                                          out. Default setting—350@-5,440@-5;10(*/0/1+2) |
| <Second_Dial_Tone> | Alternative to the Dial Tone when the user dials a three-way call. Default setting—420@-5,520@-5;10(*/0/1+2) |
| <Outside_Dial_Tone> | Alternative to the Dial Tone. It prompts the user to enter an external phone number, as opposed to an internal extension.
                                          It is triggered by a comma character encountered in the dial plan. Default setting—420@-4;10(*/0/1) |
| <Prompt_Tone> | Prompts the user to enter a call forwarding phone number. Default setting—520@-5,620@-5;10(*/0/1+2) |
| <Busy_Tone> | Played when a 486 RSC is received for an outbound call. Default setting—480@-5,620@-5;10(.5/.5/1+2) |
| <Reorder_Tone> | Played when an outbound call has failed, or after the far end hangs up during an established call. Reorder Tone is played
                                          automatically when Dial Tone or any of its alternatives times out. Default setting—480@-5,620@-5;10(.25/.25/1+2) |
| <Off_Hook_Warning_Tone> | Played when the caller has not properly placed the handset on the cradle. Off Hook Warning Tone is played when the Reorder
                                          Tone times out. Default setting—480@-3,620@3;10(.125/.125/1+2) |
| <Ring_Back_Tone> | Played during an outbound call when the far end is ringing. Default setting—440@-5,480@-5;*(2/4/1+2) |
| <Ring_Back_2_Tone> | Your ATA plays this ringback tone instead of Ring Back Tone if the called party replies with a SIP 182 response without SDP
                                          to its outbound INVITE request. Default setting—the same as Ring Back Tone, except the cadence is 1s on and 1s off. Default setting—440@-5,480@-5;*(1/1/1+2) |
| <Confirm_Tone> | Brief tone to notify the user that the last input value has been accepted. Default setting—600@-4;1(.25/.25/1) |
| <SIT1_Tone> through <SIT4_Tone> | Alternative to the Reorder Tone played when an error occurs as a caller makes an outbound call. The RSC to trigger this tone
                                          is configurable on the SIP screen. Default setting—985@-4,1428@-4,1777@-4;20(.380/0/1,.380/0/2,.380/0/3,0/4/0) |
| <MWI_Dial_Tone> | Played instead of the Dial Tone when there are unheard messages in the caller’s mailbox. Default setting—350@-5,440@-5;2(.1/.1/1+2);10(*/0/1+2) |
| <Cfwd_Dial_Tone> | Played when all calls are forwarded. Default setting—350@-5,440@-5;2(.2/.2/1+2);10(*/0/1+2) |
| <Holding_Tone> | Informs the local caller that the far end has placed the call on hold. Default setting—600@-5;*(.1/.1/1,.1/.1/1,.1/9.5/1) |
| <Conference_Tone> | Played to all parties when a three-way conference call is in progress. Default setting—350@-5;20(.1/.1/1,.1/9.7/1) |
| <Secure_Call_Indication_Tone> | Played when a call has been successfully switched to secure mode. It should be played only for a short while (less than 30
                                          seconds) and at a reduced level (less than -19 dBm) so it does not interfere with the conversation. Default setting—397@-5,507@-5;15(0/2/0,.2/.1/1,.1/2.1/2) |
| <VoIP_PIN_Tone> | This tone is played to prompt a VoIP caller to enter a PIN number. |
| <PSTN_PIN_Tone> | This tone is played to prompt a PSTN caller to enter a PIN number. |
| <Feature_Invocation_Tone> | Played when a feature is implemented. Default setting—350@-4;*(.1/.1/1) |

| <Ring1_Cadence> | Cadence script for distinctive ring 1. Default setting—60(2/4) |
|---|---|
| <Ring2_Cadence> | Cadence script for distinctive ring 2. Default setting—60(.8/.4,.8/4) |
| <Ring3_Cadence> | Cadence script for distinctive ring 3. Default setting—60(.4/.2,.4/.2,.8/4) |
| <Ring4_Cadence> | Cadence script for distinctive ring 4. Default setting—60(.3/.2,1/.2,.3/4) |
| <Ring5_Cadence> | Cadence script for distinctive ring 5. Default setting—1(.5/.5) |
| <Ring6_Cadence> | Cadence script for distinctive ring 6. Default setting—60(.2/.4,.2/.4,.2/4) |
| <Ring7_Cadence> | Cadence script for distinctive ring 7. Default setting—60(.4/.2,.4/.2,.4/4) |
| <Ring8_Cadence> | Cadence script for distinctive ring 8. Default setting—60(0.25/9.75) |

| <CWT1_Cadence> | Cadence script for distinctive CWT 1. Default setting—30(.3/9.7) |
|---|---|
| <CWT2_Cadence> | Cadence script for distinctive CWT 2. Default setting—30(.1/.1, .1/9.7) |
| <CWT3_Cadence> | Cadence script for distinctive CWT 3. Default setting—30(.1/.1, .1/.1, .1/9.7) |
| <CWT4_Cadence> | Cadence script for distinctive CWT 4. Default setting—30(.1/.1, .3/.1, .1/9.3) |
| <CWT5_Cadence> | Cadence script for distinctive CWT 5. Default setting—1(.5/.5) |
| <CWT6_Cadence> | Cadence script for distinctive CWT 6. Default setting—30(.3/.1,.3/.1,.1/9.1) |
| <CWT7_Cadence> | Cadence script for distinctive CWT 7. Default setting—30(.3/.1,.3/.1,.1/9.1) |
| <CWT8_Cadence> | Cadence script for distinctive CWT 8. Default setting—2.3(.3/2) |
| <Ring1_Name> | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 1 for the inbound call. Default setting—Bellcore-r1 |
| <Ring2_Name> | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 2 for the inbound call. Default setting—Bellcore-r2 |
| <Ring3_Name> | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 3 for the inbound call. Default setting—Bellcore-r3 |
| <Ring4_Name> | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 4 for the inbound call. Default setting—Bellcore-r4 |
| <Ring5_Name> | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 5 for the inbound call. Default setting—Bellcore-r5 |
| <Ring6_Name> | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 6 for the inbound call. Default setting—Bellcore-r6 |
| <Ring7_Name> | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 7 for the inbound call. Default setting—Bellcore-r7 |
| <Ring8_Name> | Name in an INVITE’s Alert-Info Header to pick distinctive ring/CWT 8 for the inbound call. Default setting—Bellcore-r8 |

| <Ring_Waveform> | Waveform for the ringing signal. Choices are Sinusoid or Trapezoid. Default setting—Sinusoid |
|---|---|
| <Ring_Frequency> | Frequency of the ringing signal. Valid values are 10–100 (Hz) Default setting—20 |
| <Ring_Voltage> | Ringing voltage. Choices are 60–90 (V) Default setting—85 |
| <CWT_Frequency> | Frequency script of the call waiting tone. All distinctive CWTs are based on this tone. Default setting—440@-10 |
| <Synchronized_Ring> | If this is set to yes, when the ATA is called, all lines ring at the same time (similar to a regular PSTN line) After one
                                          line answers, the others stop ringing. Default setting—no |

| <Hook_Flash_Timer_Min> | Minimum on-hook time before off-hook qualifies as hook flash. Less than this the onhook event is ignored. Range: 0.1–0.4 seconds. Default setting—0.1 |
|---|---|
| <Hook_Flash_Timer_Max> | Maximum on-hook time before off-hook qualifies as hook flash. More than this the onhook event is treated as on hook (no hookflash
                                          event) Range: 0.4–1.6 seconds. Default setting—0.9 |
| <Callee_On_<Hook_Delay> | Phone must be on-hook for at this time in sec. before the ATA will tear down the current inbound call. It does not apply to
                                          outbound calls. Range: 0–255 seconds. Default setting—0 |
| <Reorder_Delay> | Delay after far end hangs up before reorder tone is played. 0 =plays immediately, inf =never plays. Range: 0–255 seconds. Default setting—5. |
| <Call_Back_Expires> | Expiration time in seconds of a call back activation. Range: 0–65535 seconds. Default setting—1800 |
| <Call_Back_Retry_Intvl> | Call back retry interval in seconds. Range: 0–255 seconds. Default setting—30 |
| <Call_Back_Delay> | Delay after receiving the first SIP 18x response before declaring the remote end is ringing. If a busy response is received
                                          during this time, the ATA still considers the call as failed and keeps on retrying. Range: 0–65 seconds Default setting—0.5 |
| <VMWI_Refresh_Intvl> | Interval between VMWI refresh to the device. Range: 0–65535 seconds Default setting—0 |
| <Interdigit_Long_Timer> | Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit_Long_Timer
                                          is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Range: 0–64 seconds. Default setting—10 |
| <Interdigit_Short_Timer> | Short timeout between entering digits when dialing. The Interdigit_Short_Timer is used after any one digit, if at least one
                                          matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Range: 0–64
                                          seconds. Default setting—3 |
| <CPC_Delay> | Delay in seconds after caller hangs up when the ATA starts removing the tip-and-ring voltage to the attached equipment of
                                          the called party. The range is 0–255 seconds. This feature is generally used for answer supervision on the caller side to signal to the attached equipment when the call
                                          has been connected (remote end has answered) or disconnected (remote end has hung up) This feature should be disabled for
                                          the called party (in other words, by using the same polarity for connected and idle state) and the CPC feature should be used
                                          instead. Without CPC enabled, reorder tone will is played after a configurable delay. If CPC is enabled, dial tone will be
                                          played when tip-to-ring voltage is restored. Resolution is 1 second. Default setting—2 |
| <CPC_Duration> | Duration in seconds for which the tip-to-ring voltage is removed after the caller hangs up. After that, tip-to-ring voltage
                                          is restored and the dial tone applies if the attached equipment is still off-hook. CPC is disabled if this value is set to
                                          0. Range: 0 to 1.000 second. Resolution is 0.001 second. Default setting—0 (CPC disabled) |

| <Call_Return_Code> | Call Return Code This code calls the last caller. Default setting—*69 |
|---|---|
| <Call_Redial_Code> | Redials the last number called. Default setting—*07 |
| <Blind_Transfer_Code> | Begins a blind transfer of the current call to the extension specified after the activation code. Default setting—*98 |
| <Call_Back_Act_Code> | Starts a callback when the last outbound call is not busy. Default setting—*66 |
| <Call_Back_Deact_Code> | Cancels a callback. Default setting—*86 |
| <Call_Back_Busy_Act_Code> | Starts a callback when the last outbound call is busy. Default setting—*05 |
| <Cfwd_All_Act_Code> | Forwards all calls to the extension specified after the activation code. Default setting—*72 |
| <Cfwd_All_Deact_Code> | Cancels call forwarding of all calls. Default setting—*73 |
| <Cfwd_Busy_Act_Code> | Forwards busy calls to the extension specified after the activation code. Default setting—*90 |
| <Cfwd_Busy_Deact_Code> | Cancels call forwarding of busy calls. Default setting—*91 |
| <Cfwd_No_Ans_Act_Code> | Forwards no-answer calls to the extension specified after the activation code. Default setting—*92 |
| <Cfwd_No_Ans_Deact_Code> | Cancels call forwarding of no-answer calls. Default setting—*93 |
| <Cfwd_Last_Act_Code> | Forwards the last inbound or outbound call to the number that the user specifies after entering the activation code. Default setting—*63 |
| <Cfwd_Last_Deact_Code> | Cancels call forwarding of the last inbound or outbound call. Default setting—*83 |
| <Block_Last_Act_Code> | Blocks the last inbound call. Default setting—*60 |
| <Block_Last_Deact_Code> | Cancels blocking of the last inbound call. Default setting—*80 |
| <Accept_Last_Act_Code> | Accepts the last outbound call. It lets the call ring through when do not disturb or call forwarding of all calls are enabled. Default setting—*64 |
| <Accept_Last_Deact_Code> | Cancels the code to accept the last outbound call. Default setting—*84 |
| <CW_Act_Code> | Enables call waiting on all calls. Default setting—*56 |
| <CW_Deact_Code> |  |
|  | Enables call waiting on all calls. Default setting—*57 |
| <CW_Per_Call_Act_Code> | Enables call waiting for the next call. Default setting—*71 |
| <CW_Per_Call_Deact_Code> | Disables call waiting for the next call. Default setting—*70 |
| <Block_CID_Act_Code> | Blocks caller ID on all outbound calls. Default setting—*67 |
| <Block_CID_Deact_Code> | Removes caller ID blocking on all outbound calls. Default setting—*68 |
| <Block_CID_Per_Call_Act_Code> | Blocks caller ID on the next outbound call. Default setting—*81 |
| <Block_CID_Per_Call_Deact_Code> | Removes caller ID blocking on the next inbound call. Default setting—*82 |
| <Block_ANC_Act_Code> | Blocks all anonymous calls. Default setting—*77 |
| <Block_ANC_Deact_Code> | Removes blocking of all anonymous calls. Default setting—*87 |
| <DND_Act_Code> | Enables the do not disturb feature. Default setting—*78 |
| <DND_Deact_Code> | Disables the do not disturb feature. Default setting—*79 |
| <CID_Act_Code> | Enables caller ID generation. Default setting—*65 |
| <CID_Deact_Code> | Disables caller ID generation. Default setting—*85 |
| <CWCID_Act_Code> | Enables call waiting, caller ID generation. Default setting—*25 |
| <CWCID_Deact_Code> | Disables call waiting, caller ID generation. Default setting—*45 |
| <Dist_Ring_Act_Code> | Enables the distinctive ringing feature. Default setting—*26 |
| <Dist_Ring_Deact_Code> | Disables the distinctive ringing feature. Default setting—*46 |
| <Speed_Dial_Act_Code> | Assigns a speed dial number. Default setting—*74 |
| <Paging_Code> | Used for paging other clients in the group. Default setting—*96 |
| <Secure_All_Call_Act_Code> | Makes all outbound calls secure. Default setting—*16 |
| <Secure_No_Call_Act_Code> | Makes all outbound calls not secure. Default setting—*17 |
| <Secure_One_Call_Act_Code> | Makes the next outbound call secure. (It is redundant if all outbound calls are secure by default.) Default setting—*18 |
| <Secure_One_Call_Deact_Code> | Makes the next outbound call not secure. (It is redundant if all outbound calls are not secure by default.) Default setting—*19 |
| <Conference_Act_Code> | If this code is specified, the user must enter it before dialing the third party for a conference call. Enter the code for
                                          a conference call. Default setting—blank |
| <Attn-Xfer_Act_Code> | If the code is specified, the user must enter it before dialing the third party for a call transfer. Enter the code for a
                                          call transfer. Default setting—blank |
| <Modem_Line_Toggle_Code> | Toggles the line to a modem. Modem passthrough mode can be triggered only by pre-dialing this code. Default setting—*99 |
| <FAX_Line_Toggle_Code> | Toggles the line to a fax machine. Default setting—#99 |
| <Media_Loopback_Code> | Use for media loopback. Default setting—*03 |
| <Referral_Services_Codes> | These codes tell the ATA what to do when the user places the current call on hold and is listening to the second dial tone.
                                          One or more *codes can be configured into this parameter, such as *98, or *97\|*98\|*123, etc. The maximum length is 79 characters. This parameter applies when the user places the current call on hold by pressing the hook flash button. Each *code (and the
                                          following valid target number according to current dial plan) triggers the ATA to perform a blind transfer to a target number
                                          that is prepended by the service *code. For example, after the user dials *98, the ATA plays a special dial tone called the Prompt Tone while waiting for the user
                                          to enter a target number (which is checked according to dial plan as in normal dialing). When a complete number is entered,
                                          the ATA sends a blind REFER to the holding party with the Refer-To target equal to *98 target_number. This feature allows the ATA to hand off a call to an application server to perform further processing, such as call park. The *codes should not conflict with any of the other vertical service codes internally processed by the ATA. You can empty
                                          the corresponding *code that you do not want the ATA to process. Default setting—blank |
| <Feature_Dial_Services_Codes> | These codes tell the ATA what to do when the user is listening to the first or second dial tone. One or more *codes can be configured into this parameter, such as *72, or *72\|*74\|*67\|*82, etc. The maximum length is 79 characters.
                                          This parameter applies when the user has a dial tone (first or second dial tone.) After receiving dial tone, a user enters
                                          the *code and the target number according to current dial plan. For example, after user dials *72, the ATA plays a special tone called a Prompt tone while awaiting the user to enter a valid
                                          target number. When a complete number is entered, the ATA sends a INVITE to *72 target_number as in a normal call. This feature
                                          allows the proxy to process features like call forward (*72) or Block Caller ID (*67.) The *codes should not conflict with any of the other vertical service codes internally processed by the ATA. You can remove
                                          a corresponding *code that you do not want the ATA to process. You can add a parameter to indicate which tone plays after the *code is entered, such as *72‘c‘\|*67‘p‘. Below is a list of
                                          allowed tone parameters. (Note the use of open quotes surrounding the parameter, without spaces.) ‘c‘ = <Cfwd Dial Tone> ‘d‘ = <Dial Tone> ‘m‘ = <MWI Dial Tone> ‘o‘ = <Outside Dial Tone> ‘p‘ = <Prompt Dial Tone> ‘s‘ = <Second Dial Tone> ‘x‘ = No tones are place, x is any digit not used above If no tone parameter is specified, the ATA plays Prompt tone by default. If the *code is not to be followed by a phone number,
                                          such as *73 to cancel call forwarding, do not include this parameter. Instead, add the code in the dial plan and the ATA send
                                          INVITE *73@..... as usual when user dials *73. Default setting—blank |

| <Service_Annc_Base_Number> | Base number for service announcements. Default setting—blank |
|---|---|
| <Service_Annc_Extension_Codes> | Extension codes for service announcements. Default setting—blank |

| <Prefer_G711u_Code> | Dial prefix to make G.711u the preferred codec for the call. Default setting—*017110 |
|---|---|
| <Force_G711u_Code> | Dial prefix to make G.711u the only codec that can be used for the call. Default setting—*027110 |
| <Prefer_G711a_Code> | Dial prefix to make G.711a the preferred codec for the call. Default setting—*017111 |
| <Force_G711a_Code> | Dial prefix to make G.711a the only codec that can be used for the call. Default setting—*027111 |
| <Prefer_G726r32_Code> | Dial prefix to make G.726r32 the preferred codec for the call. Default setting—*0172632 |
| <Force_G726r32_Code> | Dial prefix to make G.726r32 the only codec that can be used for the call. Default setting—*0272632 |
| <Prefer_G729a_Code> | Dial prefix to make G.729a the preferred codec for the call. Default setting—*01729 |
| <Force_G729a_Code> | Dial prefix to make G.729a the only codec that can be used for the call. Default setting—*02729 |
| <Prefer_G722_Code> | Dial prefix to make G.722 the preferred codec for the call. Default setting—*01722 |
| <Force_G722_Code> | Dial prefix to make G.722 the only codec that can be used for the call. Default setting—*02722 |

| <FXS_Port_Impedance> | Sets the electrical impedance of the PHONE port. Choices are: 600, 900, 600+2.16uF, 900+2.16uF, 270+750\|\|150nF, 220+850\|\|120nF,
                                          220+820\|\|115nF, or 200+600\|\|100nF. Default setting—600 Note For New Zealand impedance (370+620\|\|310nF), use 270+750\|\|150nF. | Note | For New Zealand impedance (370+620\|\|310nF), use 270+750\|\|150nF. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note | For New Zealand impedance (370+620\|\|310nF), use 270+750\|\|150nF. |
| <FXS_Port_Input_Gain> | Input gain in dB, up to three decimal places. The range is 6.000 to -12.000. Default setting—-3 |
| <FXS_Port_Output_Gain> | Output gain in dB, up to three decimal places. The range is 6.000 to -12.000. The Call Progress Tones and DTMF playback level
                                          are not affected by the FXS Port Output Gain parameter. Default setting—-3 |
| <DTMF_Playback_Level> | Local DTMF playback level in dBm, up to one decimal place. Range: -30–0. Default setting—-16.0 |
| <DTMF_Playback_Length> | Local DTMF playback duration in milliseconds. Range: 0–65 seconds. Default setting—0.1 |
| <Detect_ABCD> | To enable local detection of DTMF ABCD, select yes. Otherwise, select no. Default setting—yes This setting has no effect if DTMF Tx Method is INFO; ABCD is always sent OOB regardless in this setting. |
| <Playback_ABCD> | To enable local playback of OOB DTMF ABCD, select yes. Otherwise, select no. Default setting—yes |
| <Caller_ID_Method> Default setting—Bellcore(N.Amer, China) | The choices are described below. Default setting—Bellcore (N.Amer, China) Bellcore(N.Amer,China): CID, CIDCW, and VMWI. FSK sent after first ring (same as ETSI FSK sent after first ring) (no polarity
                                                reversal or DTAS) DTMF(Finland, Sweden): CID only. DTMF sent after polarity reversal (and no DTAS) and before first ring. DTMF(Denmark): CID only. DTMF sent before first ring with no polarity reversal and no DTAS. ETSI DTMF: CID only. DTMF sent after DTAS (and no polarity reversal) and before first ring. ETSI DTMF With PR: CID only. DTMF sent after polarity reversal and DTAS and before first ring. ETSI DTMF After Ring: CID only. DTMF sent after first ring (no polarity reversal or DTAS) ETSI FSK: CID, CIDCW, and VMWI. FSK sent after DTAS (but no polarity reversal) and before first ring. Waits for ACK from a
                                                device after DTAS for CIDCW. ETSI FSK With PR (UK): CID, CIDCW, and VMWI. FSK is sent after polarity reversal and DTAS and before first ring. Waits for
                                                ACK from a device after DTAS for CIDCW. Polarity reversal is applied only if equipment is on hook. DTMF (Denmark) with PR: CID only. DTMF sent after polarity reversal (and no DTAS) and before first ring. Default setting—Bellcore(N.Amer, China) |
| <FXS_Port_Power_Limit> | The choices are from 1 to 8. Default setting—3 |
| <Caller_ID_FSK_Standard> | The ATA supports bell 202 and v.23 standards for caller ID generation. Default setting—bell 202 |
| <Feature_Invocation_Method> | Select the method you want to use, Default or Sweden default. Default setting—Default |
| <DECT_Enable> | To enable this handset for service, select yes. Otherwise, select no. Default setting—yes |
| <Call_Park_Enable> | Enables or disables Call Park. Default setting—No |
| <Call_Pickup_Enable> | Enables or disables Call Pickup. Default setting—No |
| <Call_Group_Pickup_Enable> | Enables or disables Group Pickup. Default setting—No |

| Note | For New Zealand impedance (370+620\|\|310nF), use 270+750\|\|150nF. |
|---|---|---|---|---|---|

| <Outgoing_Lines> | A comma-separated list of the index numbers (1~10) for the lines that are available from this handset for an outgoing call.
                                          These lines will be listed on the phone screen when the user displays the call options or holds down the green call button. Example : 1,2,8 In this example, a user can select DECT line 1, 2, or 8 for an outbound call. Default setting—1 Note You also can choose these lines from the DECT Handset Outgoing Line Selection section of the Quick Setup page. | Note | You also can choose these lines from the DECT Handset Outgoing Line Selection section of the Quick Setup page. |
|---|---|---|---|
| Note | You also can choose these lines from the DECT Handset Outgoing Line Selection section of the Quick Setup page. |
| <Failover> | When this feature is enabled and a call fails through the selected line, the ATA automatically attempts to place the call
                                          over another enabled DECT line. Select yes to enable this feature or select no to disable it. Default setting—no |
| <Deregister> | To deregister a handset, select yes. After you submit the settings and the voice module reboots, then the handset is deregistered.
                                          At that point, this parameter is reset to the default value. Default setting—no |
| <Bound_IPEI> | Enter the device’s IPEI number (a unique hardware identifier comparable to a MAC address) if you want to bind this device
                                          to the specified handset ID, such as Handset 3. The IPEI can be found in the Settings > Phone Info menu on the handset. Default setting—blank |

| Note | You also can choose these lines from the DECT Handset Outgoing Line Selection section of the Quick Setup page. |
|---|---|