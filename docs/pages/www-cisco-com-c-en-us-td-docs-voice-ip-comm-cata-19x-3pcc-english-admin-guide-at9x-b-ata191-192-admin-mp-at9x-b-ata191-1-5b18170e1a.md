---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-admin-guide-at9x-b-ata191-192-admin-mp-at9x-b-ata191-1-5b18170e1a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/admin-guide/at9x_b_ata191-192-admin-mp/at9x_b_ata191-192-admin-mp_chapter_00.html
retrieved_at: 2026-08-22T01:01:28.671812+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Get Started

## Chapter: Get Started

# Get Started

## Your Analog Telephone Adapter

The ATA 191 and ATA 192 analog telephone adapters are telephony-device-to-Ethernet adapters that allow regular analog phones
                              to operate on IP-based telephony networks. Both models support two voice ports, each with an independent phone number. Both
                              have an RJ-45 10/100BASE-T data port while the ATA 192 has an additional Ethernet port.

The ATA connects to the Internet through a broadband (DSL or cable) modem or router. The ATA can be used with an on-site call-control
                              system or an Internet-based call-control system.

The ATA is an intelligent low-density Voice over IP (VoIP) gateway that enables carrier-class residential and business IP
                              Telephony services delivered over broadband or high-speed Internet connections. An ATA maintains the state of each call it
                              terminates and reacts appropriately to user input events (such as on/off hook or hook flash). The ATAs use the Session Initiation
                              Protocol (SIP) open standard so there is on/off hook or hook flash. The ATAs use the Session Initiation Protocol (SIP) open
                              standard so there is little or no involvement by a “middle-man” server or media gateway controller. SIP allows inter-operation
                              with all ITSPs that support SIP.

### ATA 191 and ATA 192 Top Panel

The following figure shows the different LEDs and buttons found on the top of your ATA.

Item

Description

Power LED

Steady green: System booted up successfully and is ready for use.

Slow flashing green: System is booting up.

Fast flashing green three times, then repeats: System failed to boot up.

Fast flashing green: The LED behaviour occurs in the following situations:

System detects a factory reset.

A factory reset is performed successfully.

Off: Power is off.

Network LED

Flashing green: Data transmission or reception is in progress through the WAN port.

Off: No link.

Phone 1 LED

Phone 2 LED

Steady green: On hook.

Slow flashing green: Off hook.

Fast flashing green three times, then repeats: The analog device failed to register.

Fast flashing green: A factory reset is performed successfully.

Off: The port is not configured.

Problem Report Tool (PRT) Button

Press this button to create a problem report using the Problem Report Tool.

This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator.

Problem Report Tool (PRT) LED

Flashing amber: The PRT is preparing the data for the problem report.

Fast Flashing amber: The PRT is sending the problem report log to the HTTP server.

Solid amber: The activation of the FIPS mode failed. Press the PRT button to turn off the PRT LED.

Solid green for five seconds, then off: The PRT report was sent successfully.

Fast flashing green: A factory reset is performed successfully.

Flashing red: The PRT report failed. Press the PRT button once to cancel the flashing, then press again to trigger a new PRT.

#### Problem Report Tool Button

The Problem Report Tool (PRT) button is on the ATA top panel. Press the PRT button, and a log file is prepared and uploaded
                                 to the server for troubleshooting your network.

You can instruct your analog phone users to press the PRT button on the ATA device to start the PRT log file process.

Set up the HTTP server to upload the PRT log file from the ATA.

Configure the customer support upload URL to best suit your needs, and apply it to the ATA.

### ATA 191 and ATA 192 Back Panel

The following figures shows the different ports and buttons found on the back of your ATA.

Item

Description

RESET

To restart the ATA, use a paper clip or similar object to press this button briefly.

To restore the factory default settings, press and hold for about 10 seconds.

The LED behaviour for the factory reset:

After you press and hold the button for about 10 seconds, the Power LED is fast flashing green.

After the factory reset is performed successfully, all LEDs are fast flashing green for about 5 seconds.

PHONE 1

Use an RJ-11 phone cable to connect an analog phone or fax machine.

PHONE 2

Use an RJ-11 phone cable to connect a second analog phone or fax machine.

ETHERNET (ATA 192 only)

Use an Ethernet cable to connect your ATA to a device on your network, such as a computer.

NETWORK

Use an Ethernet cable to connect to the network.

DC 5V POWER

Use the power adapter that was provided to connect to a power source.

## Install Your Cisco ATA

You can use either Category 3/5/5e/6 cabling for 10-Mbps connections, but you must use Category 5/5e/6 for 100-Mbps connections.

Step 1

Connect the power supply to the Cisco DC Adapter port.

Step 2

Connect a straight-through Ethernet cable from the network to the network port on the ATA. Each ATA ships with one Ethernet
                                       cable in the box.

## ATA Voice Quality

The ATA can be custom provisioned within a wide range of configuration parameters. The sections below describe the factors
                           that contribute to voice quality.

### Supported Codecs

The ATA supports the codecs listed below. You can use the default settings or configure the codec settings in the Audio Configuration section of the Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) page.

Codec

Description

G.711 (A-law and mu-law)

Very low complexity codecs that support uncompressed 64 kbps digitized voice transmissions at one through ten 5 ms voice frames
                                             per packet. These codecs provide the highest narrow-band voice quality and uses the most bandwidth of anyof the available
                                             codecs.

G.726-32

Very low complexity codecs that support uncompressed 64 kbps digitized voice transmissions at one through ten 5 ms voice frames
                                             per packet. These codecs provide the highest narrow-band voice quality and uses the most bandwidth of anyof the available
                                             codecs.

G.729a

ITU G.729 voice coding algorithm used to compress digitized speech. G.729a is a reduced complexity version of G.729 requiring
                                             about half the processing power of G.729. The G.729 and G.729a bit streams are compatible and interoperable, but not identical.

### SIP Proxy Redundancy

An average SIP Proxy Server can handle tens of thousands of subscribers. A backup server allows an active server to be temporarily
                                 switched out for maintenance. The ATA supports the use of backup servers to minimize or eliminate service disruption.

A simple way to support proxy redundancy is to specify a SIP Proxy Server. The ATA sends a DNS NAPTR or SRV query to the DNS
                                 server. If configured, the DNS server returns SRV records that contain a list of servers for the domain, with their hostnames,
                                 priority, listening ports, and so forth. The ATA tries to contact the servers in the order of the priority. The server with
                                 a lower number has a higher priority. Up to 6 NAPTR records and 12 SRV records are supported in a query. And an SRV record can associate with up to 10 A records.

When the ATA fails to communicate with the primary server, the ATA can failover to a lower-priority server. If configured,
                                 the ATA can restore the connection back to the primary. Failover and failback support switches between servers with different
                                 SIP transport protocols. The ATA doesn't perform failback to the primary server during an active call until the call ends
                                 and the failback conditions are met.

#### Example of Resource Records from the DNS Server

```
as1bsoft     3600    IN NAPTR 50   50  "s"  "SIPS+D2T"     ""  _sips._tcp.tlstest
             3600    IN NAPTR 90   50  "s"  "SIP+D2T"      ""  _sip._tcp.tcptest
             3600    IN NAPTR 100  50  "s"  "SIP+D2U"      ""  _sip._udp.udptest

_sips._tcp.tlstest  SRV 1 10 5061 srv1.sipurash.com.
                    SRV 2 10 5060 srv2.sipurash.com.
_sip._tcp.tcptest   SRV 1 10 5061 srv3.sipurash.com.
                    SRV 2 10 5060 srv4.sipurash.com.
_sip._udp.udptest   SRV 1 10 5061 srv5.sipurash.com.
                    SRV 2 10 5060 srv6.sipurash.com.

srv1     3600    IN    A   1.1.1.1
srv2     3600    IN    A   2.2.2.2
srv3     3600    IN    A   3.3.3.3
srv4     3600    IN    A   4.4.4.4
srv5     3600    IN    A   5.5.5.5
srv6     3600    IN    A   6.6.6.6
```

```
Priority       IP Address     SIP Protocol    Status
1st            1.1.1.1            TLS            UP
2nd            2.2.2.2            TLS            UP
3rd            3.3.3.3            TCP            UP
4th            4.4.4.4            TCP            UP
5th            5.5.5.5            UDP            UP
6th            6.6.6.6            UDP            UP
```

The ATA always sends SIP messages to the available address with the top priority and with the status UP in the list. In the
                                 example, the ATA sends all the SIP messages to the address 1.1.1.1. If the address 1.1.1.1 in the list is marked with the
                                 status DOWN, then the ATA communicates with 2.2.2.2 instead. The ATA can restore the connection back to 1.1.1.1 when the specified
                                 failback conditions are met. For more details about failover and failback, see SIP Proxy Failover and SIP Proxy Fallback .

#### SIP Proxy Failover

The ATA performs a failover in any of these cases:

The ATA sends SIP messages and doesn't get responses from the server.

The server responds with a code that matches the specified code in Try Backup RSC .

The ATA gets a TCP disconnection request.

We strongly recommend that you set the Auto Register When Failover to yes when SIP Transport is set to AUTO .

##### ATA Failover Behavior

When the ATA fails to communicate with the currently connected server, it refreshes the server list status. The unavailable
                                    server is marked with the status DOWN in the server list. The ATA tries to connect to the top-priority server with the status
                                    UP in the list.

In the following example, the addresses 1.1.1.1 and 2.2.2.2 aren’t available. The ATA sends SIP messages to 3.3.3.3, which
                                    has the top priority among the servers with the status UP.

```
Priority       IP Address     SIP Protocol    Status
1st            1.1.1.1            TLS          DOWN
2nd            2.2.2.2            TLS          DOWN
3rd            3.3.3.3            TCP          UP
4th            4.4.4.4            TCP          UP
5th            5.5.5.5            UDP          UP
6th            6.6.6.6            UDP          UP
```

In the following example, there are two SRV records from the DNS NAPTR response. For each SRV record, there are three A records
                                    (IP addresses).

```
Priority       IP Address     SIP Protocol    Server            Status
1st            1.1.1.1            UDP         SRV1              DOWN
2nd            1.1.1.2            UDP         SRV1              UP
3rd            1.1.1.3            UDP         SRV1              UP
4th            2.2.2.1            TLS         SRV2              UP
5th            2.2.2.2            TLS         SRV2              UP
6th            2.2.2.3            TLS         SRV2              UP
```

Let's assume that the ATA failed to connect to 1.1.1.1 and then registered to 1.1.1.2. When 1.1.1.2 goes down, ATA behavior
                                    depends on the setting of Proxy Fallback Intvl .

When Proxy Fallback Intvl is set to 0 , the ATA tries with the addresses in this order: 1.1.1.1, 1.1.1.3, 2.2.2.1, 2.2.2.2, 2.2.2.3.

When Proxy Fallback Intvl is set to a value other than zero, the ATA tries with the addresses in this order: 1.1.1.3, 2.2.2.1, 2.2.2.2, 2.2.2.3.

#### SIP Proxy Fallback

The proxy fallback requires a value other than zero specified in the Proxy Fallback Intvl field under the Proxy and Registration section in the ATA administration web page. If you set this field to 0 , the SIP proxy failback feature is disabled.

The time when the ATA triggers a failback depends on the ATA configuration and the SIP transport protocols in use.

To enable the ATA to perform failback between different SIP transport protocols, set SIP Transport to AUTO under the Proxy and Registration section from Voice > Line (n) of the ATA administration web page.

##### Failback from a UDP Connection

```
Priority       IP Address     SIP Protocol    Status      
1st            1.1.1.1            TLS          DOWN        T1 (Down time)
2nd            2.2.2.2            UDP          UP          
3rd            3.3.3.3            TCP          UP
```

The ATA has the following configuration:

```
<Proxy_Fallback_Intvl_ n _ ua="na">60</Proxy_Fallback_Intvl_ n _>
<Register_Expires_ n _ ua="na">3600</Register_Expires_ n _>
<SIP_Timer_F ua="na">16</SIP_Timer_F>
```

where n is the extension number.

The ATA refreshes the registration at time T2 (T2=(3600-16)*78%). The ATA checks the address list for the availability of
                                    the IP addresses and the down time. If T2-T1 > = 60 , the failed server 1.1.1.1 resumes back to UP and the list is updated to the following. The ATA sends SIP messages to 1.1.1.1.

```
Priority       IP Address     SIP Protocol    Status     
1st            1.1.1.1            TLS           UP        
2nd            2.2.2.2            UDP           UP
3rd            3.3.3.3            TCP           UP
```

##### Failback from a TCP or TLS Connection

```
Priority       IP Address     SIP Protocol    Status      
1st            1.1.1.1            UDP          DOWN        T1 (Down time)
2nd            2.2.2.2            TCP          UP          
3rd            3.3.3.3            TLS          UP
```

The ATA has the following configuration:

```
<Proxy_Fallback_Intvl_ n _ ua="na">60</Proxy_Fallback_Intvl_ n _>
<Register_Expires_ n _ ua="na">3600</Register_Expires_ n _>
<SIP_Timer_F ua="na">16</SIP_Timer_F>
```

where n is the extension number.

The proxy fallback interval (60 seconds) counts down from T1. The ATA triggers proxy failback at the time of T1+60. If you
                                    set the proxy fallback interval to 0 in this example, the ATA keeps the connection on 2.2.2.2.

### Other ATA Voice Quality Features

#### Silence Suppression and Comfort Noise Generation

Voice Activity Detection (VAD) with Silence Suppression reduces the bandwidth needed for a single call, making it possible
                                 for your network to support more calls overall. VAD distinguishes between speech and non-speech signals, and Silence Suppression
                                 removes the natural silences that occur in a conversation. The IP bandwidth is used only to transmit speech.

Comfort Noise Generation provides white noise when nobody is talking so you know that your call is still connected.

#### Modem and Fax Pass-Through

The following applies to modem and fax pass-through:

Modem pass-through mode can be triggered by predialing the Vertical Service Activation Code for the Modem Line Toggle Code.
                                       You can configure this setting in the Vertical Service Activation Codes section of the Regional page.

A CED/CNG tone or an NSE event triggers FAX pass-through mode.

Echo canceller is automatically disabled for Modem passthrough mode.

Echo canceller is disabled for FAX pass-through if FAX Disable ECAN (Line 1 or 2 tab) is set to “Yes” for that line. In this
                                       case, FAX pass-through is the same as Modem pass-through.

Call waiting and silence suppression are automatically disabled for both FAX and Modem pass-through. Out-of-band DTMF transmission
                                       is disabled during modem or fax passthrough.

#### Adaptive Jitter Buffer

The ATA can buffer incoming voice packets to minimize the impact of variable network delays. This process is known as jitter
                                 buffering. The size of the jitter buffer adjusts to changing network conditions. The ATA has a Network Jitter Level control
                                 setting for each line of service. The jitter level determines how aggressively the ATA tries to shrink the jitter buffer over
                                 time to achieve a lower overall delay. If the jitter level is higher, it shrinks more gradually. If jitter level is lower,
                                 it shrinks more quickly. You can use the default settings or configure this feature in the Network Settings section of the
                                 "Voice Settings Configuration" chapter.

#### Adjustable Audio Frames Per Packet

This feature allows you to set the number of audio frames contained in one RTP packet. Packets can be adjusted to contain
                                 from 1 to 10 audio frames. Increasing the number of packets decreases the bandwidth utilized, but it also increases delay
                                 and may affect voice quality. You can configure this setting in the RTP Parameters section of the SIP page.

#### DTMF Relay

The ATA may relay DTMF digits as out-of-band events to preserve the fidelity of the digits. This action enhances the reliability
                                 of DTMF transmission required by many IVR applications such as dial-up banking and airline information. You can configure
                                 this setting in the RTP Parameters section of the SIP page.

#### Call Progress Tones

The ATA has configurable call progress tones. Call progress tones are generated locally on the ATA and alert you to a call's
                                 status. Parameters for each type of tone, such as a dial tone, may include frequency and amplitude of each component, and
                                 cadence information. You can keep the default settings or configure these tones in the Call Progress Tones section of the
                                 Regional page.

#### Call Progress Tone Pass Through

This feature allows you to hear the call progress tones (such as ringing) that are generated from the far-end network.

#### Echo Cancellation

Impedance mismatch between the phone and the IP Telephony gateway phone port can lead to near-end echo. The ATA has a near-end
                                 echo canceller that compensates for impedance mismatch. The ATA also implements an echo suppressor with Comfort Noise Generator
                                 (CNG) so that any residual echo is not noticeable. This feature is enabled by default. You can configure this setting in the
                                 Audio Configuration of the Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) page.

#### Hook Flash Events

The ATA signals hook flash events to the proxy during a connected call. This feature can be used to provide advanced mid-call
                                 services with third-party-call control.

Depending on your service provider, you may need to disable Call Waiting Service, Three Way Conference Service, or Three Way
                                       Call Service. These three features could prevent the signaling of a hook flash event to the softswitch. You can configure
                                       these settings in the Supplementary Service Subscription section of the Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) page.

The Hook Flash setting determines the time period required for hook flash detection. It is in the Control Timer Values section
                                       of the SIP page.

#### Configurable Dial Plan with Interdigit Timers

The ATA has three configurable interdigit timers:

The initial timeout—signals that a phone is taken off hook.

A long timeout—signals the end of a dialed string.

A short timeout—signals that more digits are expected.

#### Polarity Control

The ATA allows the polarity to be set when a call is connected and when a call is disconnected. This feature is required to
                                 support some pay phone system and answering machines. You can configure these settings in the FXS Port Polarity Configuration
                                 section of the Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) page.

#### Calling Party Control

Calling Party Control (CPC) momentarily removes the voltage between the tip and the ring signals, signaling that the calling
                                 party has hung up. This feature is useful for auto-answer equipment. You can configure these settings in the Control Timer
                                 Values section of the Regional page.

#### Encryption of SIP Messages using SIP over TLS

You can enable SIP over Transport Layer Security (TLS) to encrypt the SIP messages between the service provider and your business.
                                 SIP over TLS relies on the TLS protocol to encrypt the signaling messages. You can configure the SIP Transport parameter in
                                 the SIP Settings section of the Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) page.

#### Secure Calling Using SRTP

Voice packets are encrypted by using Secure Real-Time Transport Protocol (SRTP). This function is implemented on a standards
                                 basis (RFC4568). Secure call service (Secure Call Serv) is enabled by default. It is located in the Supplementary Service
                                 Subscription section of the Line 1 and Line 2 Settings (PHONE 1 and PHONE 2) page. When this service is enabled, you can activate
                                 secure calling by pressing the star (*) key before dialing a phone number. You can also enable the Secure Call Setting to
                                 encrypt all calls from a phone.

#### DNS NAPTR Support

The Line 1 and Line 2 (PHONE 1 and PHONE2) can select the SIP transport protocol (TPC, UDP, or TLS) automatically based on
                                 the Name Authority Pointer (NAPTR) records on the DNS server. Typically, the line uses the protocol with the highest priority
                                 in the records.

| Item | Description |
|---|---|
| Power LED | Steady green: System booted up successfully and is ready for use. Slow flashing green: System is booting up. Fast flashing green three times, then repeats: System failed to boot up. Fast flashing green: The LED behaviour occurs in the following situations: System detects a factory reset. To perform a factory reset, press and hold the RESET button for about 10 seconds. A factory reset is performed successfully. Off: Power is off. |
| Network LED | Flashing green: Data transmission or reception is in progress through the WAN port. Off: No link. |
| Phone 1 LED Phone 2 LED | Steady green: On hook. Slow flashing green: Off hook. Fast flashing green three times, then repeats: The analog device failed to register. Fast flashing green: A factory reset is performed successfully. Off: The port is not configured. |
| Problem Report Tool (PRT) Button | Press this button to create a problem report using the Problem Report Tool. Note This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator. | Note | This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator. |
| Note | This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator. |
| Problem Report Tool (PRT) LED | Flashing amber: The PRT is preparing the data for the problem report. Fast Flashing amber: The PRT is sending the problem report log to the HTTP server. Solid amber: The activation of the FIPS mode failed. Press the PRT button to turn off the PRT LED. Solid green for five seconds, then off: The PRT report was sent successfully. Fast flashing green: A factory reset is performed successfully. Flashing red: The PRT report failed. Press the PRT button once to cancel the flashing, then press again to trigger a new PRT. |

| Note | This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator. |
|---|---|

| Item | Description |
|---|---|
| RESET | To restart the ATA, use a paper clip or similar object to press this button briefly. To restore the factory default settings, press and hold for about 10 seconds. The LED behaviour for the factory reset: After you press and hold the button for about 10 seconds, the Power LED is fast flashing green. After the factory reset is performed successfully, all LEDs are fast flashing green for about 5 seconds. |
| PHONE 1 | Use an RJ-11 phone cable to connect an analog phone or fax machine. |
| PHONE 2 | Use an RJ-11 phone cable to connect a second analog phone or fax machine. |
| ETHERNET (ATA 192 only) | Use an Ethernet cable to connect your ATA to a device on your network, such as a computer. |
| NETWORK | Use an Ethernet cable to connect to the network. |
| DC 5V POWER | Use the power adapter that was provided to connect to a power source. |

| Step 1 | Connect the power supply to the Cisco DC Adapter port. |
|---|---|
| Step 2 | Connect a straight-through Ethernet cable from the network to the network port on the ATA. Each ATA ships with one Ethernet
                                       cable in the box. |

| Codec | Description |
|---|---|
| G.711 (A-law and mu-law) | Very low complexity codecs that support uncompressed 64 kbps digitized voice transmissions at one through ten 5 ms voice frames
                                             per packet. These codecs provide the highest narrow-band voice quality and uses the most bandwidth of anyof the available
                                             codecs. |
| G.726-32 | Very low complexity codecs that support uncompressed 64 kbps digitized voice transmissions at one through ten 5 ms voice frames
                                             per packet. These codecs provide the highest narrow-band voice quality and uses the most bandwidth of anyof the available
                                             codecs. |
| G.729a | ITU G.729 voice coding algorithm used to compress digitized speech. G.729a is a reduced complexity version of G.729 requiring
                                             about half the processing power of G.729. The G.729 and G.729a bit streams are compatible and interoperable, but not identical. |