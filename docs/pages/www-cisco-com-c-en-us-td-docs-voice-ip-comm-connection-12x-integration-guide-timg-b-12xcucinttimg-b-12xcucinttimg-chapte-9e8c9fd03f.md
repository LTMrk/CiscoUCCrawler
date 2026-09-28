---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-integration-guide-timg-b-12xcucinttimg-b-12xcucinttimg-chapte-9e8c9fd03f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/timg/b_12xcucinttimg/b_12xcucinttimg_chapter_01010.html
retrieved_at: 2026-08-16T18:46:18.724696+00:00
---

TIMG Integration Guide for Cisco Unity Connection Release 12.x

# TIMG Integration Guide for Cisco Unity Connection Release 12.x

Updated: October 30, 2018

Chapter: Settings for TIMG Firmware Version 5.x

## Chapter: Settings for TIMG Firmware Version 5.x

# Settings for TIMG Firmware Version 5.x

## Introduction

This chapter provide the information for TIMG settings when firmware version 5.x is installed on the TIMG units. You must
                           upgrade your TIMG units to the most recent version that is available at http://software.cisco.com/download/navigator.html?mdfid=280082558&i=rm . For instructions on downloading and installing the most recent TIMG firmware, see the chapter for your phone system integration
                           in this guide.

## TIMG Settings for
                        	 a Serial Integration (Firmware Version 5.x)

On a Windows workstation, sign in to a TIMG unit.

On the Configure menu, select IP .

On the IP page, enter the following settings for LAN1.

Field

Setting

Client IP Address

Enter the new IP address that you want to use for the TIMG unit.

(This is the IP address that you enter in UTIM when you create
                                                      						  the integration.)

Client Subnet Mask

Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address.

Default Network Gateway Address

Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use.

BOOTP Enabled

If you are using DHCP, select Yes .

If you are not using DHCP, select No .

Select Apply Changes .

On the Configure menu, select System .

On the System page, enter the following settings.

Field

Setting

Operating Mode

Select SIP .

PCM Coding

Select uLaw .

Determine which serial port on the TIMG unit you use to connect
                                       			 the data link serial cable from the phone system, then enter the following
                                       			 settings in the applicable group.

Field

Setting

Serial Port Baud Rate

Select the setting that is configured on the phone system.

The default setting is 9600.

Serial Port Parity

Select the setting that is configured on the phone system.

The default setting is None.

Serial Port Data Bits

Select the setting that is configured on the phone system.

The default setting is 8.

Serial Port Stop Bits

Select the setting that is configured on the phone system.

The default setting is 1.

Select Apply Changes .

On the Configure menu, select Gateway .

On the Gateway page, select the Gateway
                                          				Routing tab.

On the Gateway Routing tab, Unity Connection without a cluster,
                                       			 skip to Step 12 . If Unity
                                       			 Connection has a cluster configured, do the following substeps:

In the Fault Tolerance Enabled field, select Yes .

In the Load Balancing Enabled field, select No .

Under VoIP Endpoint ID, enter the following settings.

Field

Setting

VoIP Endpoint ID: 1

(Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a
                                                         							 cluster configured) Enter the server name of the subscriber server.

VoIP Endpoint ID: 2

(Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a
                                                         							 cluster configured) Enter the server name of the publisher server.

Select Apply
                                          				Changes .

On the Gateway page, select the Gateway
                                          				Advanced tab.

On the Gateway Advanced tab, enter the following settings.

Field

Settings

Advanced Call Routing

Call Connect Mode

Select OnAnswer .

Send DNIS to VoIP
                                                      						  Endpoint

Select No .

Destination for
                                                      						  Unroutable IP Calls

Leave this field blank.

Destination for
                                                      						  Unroutable PBX Calls

Leave this field blank.

Monitor Call Connections

Select No .

Telephony

Minimum Call Party Delay

Enter 500 .

Maximum Call Party Delay

Enter 2000 .

Dial Digit on Time

Enter 100 .

Dial Inter-Digit Time

Enter 100 .

Dial Pause Time

Enter 2000 .

Turn MWI On FAC

Leave this field blank.

Turn MWI Off FAC

Leave this field blank.

Dial Send Key

Select None .

Outbound Call Connect
                                                      						  Timeout

Enter 10000 .

Wait for Ringback/Connect
                                                      						  on Blind Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports.

Audio

Audio Compression

Select the preferred
                                                      						  codec for audio compression:

G.711

G.729AB

RTP Digit Relay Mode

Select RFC2833 .

Signaling Digit Relay
                                                      						  Mode

Select Off .

Voice Activity Detection

Select On .

Frame Size

Select the applicable
                                                      						  setting:

G.711— 20

G.729AB— 10

Frames Per Packet

Select the applicable
                                                      						  setting:

G.711— 1

G.729AB— 2

Quality of Service

Call Control QOS Byte

Enter 104 (equivalent to
                                                      						  DSCP AF31).

RTP QOS Byte

Enter 184 (equivalent to
                                                      						  DSCP EF).

Traps and Alarms

E-mail Alarms Enabled

Select No .

SNMP Traps Enabled

Select No .

HTTP Server Enabled

Select Yes .

HTTPs Server Enabled

Select No .

Select Apply
                                          				Changes .

On the Gateway page, select the Gateway
                                          				Capabilities tab.

Enter the following settings for all ports that are used by
                                       			 voice messaging ports on Unity Connection.

Field

Setting

Telephony Port Capability

Select Both .

Telephony Port Enabled

For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes .

For ports that are not
                                                      						  used, select No .

Select Apply
                                          				Changes .

On the Configure menu, select T1E1 .

On the T1E1 page, select the T1/E1 Mode tab.

On the T1/E1 Mode tab, enter the following settings.

Field

Setting

Line Mode

Select T1 .

Signaling Mode

Select CAS .

Interface Mode

Select Terminal .

Select Apply
                                          				Changes .

Select the T1-CAS
                                          				Protocol tab.

On the T1-CAS Protocol tab, enter the following settings.

Field

Setting

T1 CAS Protocol

Enter the setting that
                                                      						  matches the phone system programming.

Line Encoding

Enter the setting that
                                                      						  matches the phone system programming.

Framing

Enter the setting that
                                                      						  matches the phone system programming.

Selects Transmit Pulse
                                                      						  Waveform

Enter the setting that
                                                      						  matches the phone system programming.

Flash Hook

Enter the setting that
                                                      						  matches the phone system programming.

Consult Call Dialtone
                                                      						  Drop Code

Enter the setting that
                                                      						  matches the phone system programming.

Consult Call Proceeding
                                                      						  Drop Code

Enter the setting that
                                                      						  matches the phone system programming.

Consult Call Busy Drop
                                                      						  Code

Enter the setting that
                                                      						  matches the phone system programming.

Consult Call Error Drop
                                                      						  Code

Enter the setting that
                                                      						  matches the phone system programming.

Consult Call Connected
                                                      						  Drop Code

Enter the setting that
                                                      						  matches the phone system programming.

Consult Call Disconnected
                                                      						  Drop Code

Enter the setting that
                                                      						  matches the phone system programming.

MWI confirmation Tone

Select No .

CPID Type

Select TypeII_CPID .

Initial Wait for Inband
                                                      						  CPID

Enter 100 .

Inband CPID Complete
                                                      						  Timeout

Enter 300 .

Select Apply
                                          				Changes .

On the Configure menu, select Serial
                                          				Protocol .

On the Serial Protocol page, enter the following settings.

Field

Setting

Serial Mode
                                                      						  (Master/Slave)

Select the applicable
                                                      						  setting:

Master —Select this
                                                            								setting when this TIMG unit is connected to the data link serial cable from the
                                                            								phone system. There can be only one master TIMG unit in a phone system
                                                            								integration.

Slave —Select this
                                                            								setting when this TIMG unit is not connected to the data link serial cable from
                                                            								the phone system. There can be multiple slave TIMG units in a phone system
                                                            								integration.

Serial Interface Protocol

Select the serial
                                                      						  protocol that your phone system uses:

SMDI

MCI

MD-110

MWI Response Timeout

Enter 2000 .

IP Address of Serial
                                                      						  Server

If the TIMG unit is the
                                                      						  master, leave this field blank.

If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system).

Serial Cpid Expiration

Enter 5000 .

Logical Extension Number

If the TIMG unit is the
                                                      						  master, leave this field blank.

If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system).

Select Apply
                                          				Changes .

On the Configure menu, select SIP .

On the SIP page, enter the following settings.

Field

Setting

Host and Domain Name

Enter the domain name of
                                                      						  the TIMG unit.

Transport Type

Select UDP .

Call as Domain Name

Select No .

SIPS URI Scheme Enabled

Select No .

Invite Expiration

Enter 120 .

DNS Server Address

Enter the IP address of
                                                      						  the DNS server.

Registration Server
                                                      						  Address

Leave this field blank.

Registration Server Port

Enter 5060 .

Registration Expiration

Enter 3600 .

UDP/TCP Transports
                                                      						  Enabled

Select Yes .

TCP/UDP Server Port

Enter 5060 .

Primary Proxy Server
                                                      						  Address

Leave this field blank.

Primary Proxy Server Port

Not applicable. Leave the
                                                      						  default setting.

Backup Proxy Server
                                                      						  Address

Not applicable. Leave the
                                                      						  default setting.

Backup Proxy Server Port

Not applicable. Leave the
                                                      						  default setting.

Proxy Query Interval

Enter 10 .

T1 Time

Enter 500 .

T2 Time

Enter 4000 .

T4 Time

Enter 5000 .

Select Apply
                                          				Changes .

On the Configure menu, select Tones .

On the Tones page, select the Learn tab.

On the Tones page, for the Dialtone event, confirm that the
                                       			 Acquire Tone check box is checked and leave the Destination Address field
                                       			 blank.

On the Tones page, for the Busy Tone event, confirm that the
                                       			 Acquire Tone check box is checked and do the following substeps to verify that
                                       			 the tone is correct.

From a available phone, call a second phone.

Answer the second phone when it rings, and leave both handsets
                                             				  off so that both phones are busy.

From a third phone, dial one of the busy phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the handsets for the other two
                                             				  phones off.

On the Tones page, in the Destination Address field for Busy
                                       			 Tone, enter the extension that you dialed in Step 36 c. from the third
                                       			 phone.

On the Tones page, for the Error/Reorder Tone event, confirm
                                       			 that the Acquire Tone check box is checked and do the following substeps to
                                       			 verify that the tone is correct.

From an available phone, dial an extension that does not exist.

Confirm that you hear the reorder or error tone.

Hang up the phone.

On the Tones page, in the Destination Address field for
                                       			 Error/Reorder Tone, enter the extension that you dialed in Step 38 a.

On the Tones page, for the Ringback Tone event, confirm that the
                                       			 Acquire Tone check box is checked and do the following substeps to verify that
                                       			 the tone is correct.

From an available phone, dial an extension that does exist.

Confirm that you hear the ringback tone.

Hang up the phone.

On the Tones page, in the Destination Address field for Ringback
                                       			 Tone, enter the extension that you dialed in Step 40 a.

Select Learn .

When the process is complete, check the check box for each newly
                                       			 learned tone and select Apply .

Hang up the phones that you used in Step 36 .

If the TIMG unit is connected to a Nortel SL-100 phone system,
                                       			 do the following substeps to learn the stutter dial tone. Otherwise, continue
                                       			 to Step 46 .

On the Tones page, on the Learn tab, for the Dialtone event,
                                             				  confirm that the Acquire Tone check box is checked and enter ! in the Destination Address field.

Uncheck the Acquire Tone check boxes for all other tones.

Select Learn .

When the process is complete, check the check box for each newly
                                             				  learned tone and select Apply .

On the Configure menu, select Restart .

On the Restart page, select Restart Unit
                                          				Now .

When the TIMG unit has restarted, in the View menu, select Refresh .

Repeat Step 1 through Step 48 on all
                                       			 remaining TIMG units.

## TIMG Settings for
                        	 an In-Band Integration (Firmware Version 5.x)

On a Windows workstation, sign in to a TIMG unit.

On the Configure menu, select IP .

On the IP page, enter the following settings for LAN1.

Field

Setting

Client IP Address

Enter the new IP address that you want to use for the TIMG unit.

(This is the IP address that you enter in UTIM when you create
                                                      						  the integration.)

Client Subnet Mask

Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address.

Default Network Gateway Address

Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use.

BOOTP Enabled

If you are using DHCP, select Yes .

If you are not using DHCP, select No .

Select Apply Changes .

On the Configure menu, select System .

On the System page, enter the following settings.

Field

Setting

Operating Mode

Select SIP .

PCM Coding

Select uLaw .

Select Apply Changes .

On the Configure menu, select Gateway .

On the Gateway page, select the Gateway Routing tab.

On the Gateway Routing tab, Unity Connection without a cluster,
                                       			 skip to Step 11 . If Unity
                                       			 Connection has a cluster configured, do the following substeps:

In the Fault Tolerance Enabled field, select Yes .

In the Load Balancing Enabled field, select No .

Under VoIP Endpoint ID, enter the following settings.

Field

Setting

VoIP Endpoint ID: 1

(Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the
                                                      						  server name of the subscriber server.

VoIP Endpoint ID: 2

(Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the
                                                      						  server name of the publisher server.

Select Apply
                                          				Changes .

On the Gateway page, select the Gateway
                                          				Advanced tab.

On the Gateway Advanced tab, enter the following settings.

Field

Settings

Advanced Call Routing

Call Connect Mode

Select OnAnswer .

Send DNIS to VoIP
                                                      						  Endpoint

Select No .

Destination for
                                                      						  Unroutable IP Calls

Leave this field blank.

Destination for
                                                      						  Unroutable PBX Calls

Leave this field blank.

Monitor Call Connections

Select No .

Telephony

Minimum Call Party Delay

Enter 500 .

Maximum Call Party Delay

Enter 2000 .

Dial Digit on Time

Enter 100 .

Dial Inter-Digit Time

Enter 100 .

Dial Pause Time

Enter 2000 .

Turn MWI On FAC

Enter the code that the
                                                      						  phone system uses to turn MWIs on.

Turn MWI Off FAC

Enter the code that the
                                                      						  phone system uses to turn MWIs off.

Dial Send Key

Select None .

Outbound Call Connect
                                                      						  Timeout

Enter 10000 .

Wait for Ringback/Connect
                                                      						  on Blind Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports.

Audio

Audio Compression

Select the preferred
                                                      						  codec for audio compression:

G.711

G.729AB

RTP Digit Relay Mode

Select RFC2833 .

Signaling Digit Relay
                                                      						  Mode

Select Off .

Voice Activity Detection

Select On .

Frame Size

Select the applicable
                                                      						  setting:

G.711— 20

G.729AB— 10

Frames Per Packet

Select the applicable
                                                      						  setting:

G.711— 1

G.729AB— 2

Quality of Service

Call Control QOS Byte

Enter 104 (equivalent to
                                                      						  DSCP AF31).

RTP QOS Byte

Enter 184 (equivalent to
                                                      						  DSCP EF).

Traps and Alarms

E-mail Alarms Enabled

Select No .

SNMP Traps Enabled

Select No .

HTTP Server Enabled

Select Yes .

HTTPs Server Enabled

Select No .

Select Apply
                                          				Changes .

On the Gateway page, select the Gateway
                                          				Capabilities tab.

Enter the following settings for all ports that are used by
                                       			 voice messaging ports on Unity Connection.

Field

Setting

Telephony Port Capability

Select Both .

Telephony Port Enabled

For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes .

For ports that are not
                                                      						  used, select No .

Select Apply
                                          				Changes .

On the Configure menu, select T1E1 .

On the T1E1 page, select the T1/E1 Mode tab.

On the T1/E1 Mode tab, enter the following settings.

Field

Setting

Line Mode

Select T1 .

Signaling Mode

Select CAS .

Interface Mode

Select Terminal .

Select Apply
                                          				Changes .

Select the T1-CAS
                                          				Protocol tab.

On the T1-CAS Protocol tab, enter the following settings.

Field

Setting

T1 CAS Protocol

Select Loop_Start .

Line Encoding

Select B8ZS .

Framing

Select EFS .

Selects Transmit Pulse
                                                      						  Waveform

Select Short_Haul_110ft .

Flash Hook

Enter 550 .

Consult Call Dialtone
                                                      						  Drop Code

Enter !! .

Consult Call Proceeding
                                                      						  Drop Code

Enter !! .

Consult Call Busy Drop
                                                      						  Code

Enter ! .

Consult Call Error Drop
                                                      						  Code

Enter !! .

Consult Call Connected
                                                      						  Drop Code

Enter ,,,, .

Consult Call Disconnected
                                                      						  Drop Code

Enter ! .

MWI confirmation Tone

Select No .

CPID Type

Select TypeII_CPID .

Initial Wait for Inband
                                                      						  CPID

Enter 5000 .

Inband CPID Complete
                                                      						  Timeout

Enter 500 .

Select Apply
                                          				Changes .

On the Configure menu, select SIP .

On the SIP page, enter the following settings.

Field

Setting

Host and Domain Name

Enter the domain name of
                                                      						  the TIMG unit.

Transport Type

Select UDP .

Call as Domain Name

Select No .

SIPS URI Scheme Enabled

Select No .

Invite Expiration

Enter 120 .

DNS Server Address

Enter the IP address of
                                                      						  the DNS server.

Registration Server
                                                      						  Address

Leave this field blank.

Registration Server Port

Enter 5060 .

Registration Expiration

Enter 3600 .

UDP/TCP Transports
                                                      						  Enabled

Select Yes .

TCP/UDP Server Port

Enter 5060 .

Primary Proxy Server
                                                      						  Address

Leave this field blank.

Primary Proxy Server Port

Not applicable. Leave the
                                                      						  default setting.

Backup Proxy Server
                                                      						  Address

Not applicable. Leave the
                                                      						  default setting.

Backup Proxy Server Port

Not applicable. Leave the
                                                      						  default setting.

Proxy Query Interval

Enter 10 .

T1 Time

Enter 500 .

T2 Time

Enter 4000 .

T4 Time

Enter 5000 .

Select Apply
                                          				Changes .

On the Configure menu, select Tones .

On the Tones page, select the Learn tab.

On the Tones page, for the Dialtone event, confirm that the
                                       			 Acquire Tone check box is checked and leave the Destination Address field
                                       			 blank.

On the Tones page, for the Busy Tone event, confirm that the
                                       			 Acquire Tone check box is checked and do the following substeps to verify that
                                       			 the tone is correct.

From a available phone, call a second phone.

Answer the second phone when it rings, and leave both handsets
                                             				  off so that both phones are busy.

From a third phone, dial one of the busy phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the handsets for the other two
                                             				  phones off.

On the Tones page, in the Destination Address field for Busy
                                       			 Tone, enter the extension that you dialed in Step 32 c. from the third
                                       			 phone.

On the Tones page, for the Error/Reorder Tone event, confirm
                                       			 that the Acquire Tone check box is checked and do the following substeps to
                                       			 verify that the tone is correct.

From an available phone, dial an extension that does not exist.

Confirm that you hear the reorder or error tone.

Hang up the phone.

On the Tones page, in the Destination Address field for
                                       			 Error/Reorder Tone, enter the extension that you dialed in Step 34 a.

On the Tones page, for the Ringback Tone event, confirm that the
                                       			 Acquire Tone check box is checked and do the following substeps to verify that
                                       			 the tone is correct.

From an available phone, dial an extension that does exist.

Confirm that you hear the ringback tone.

Hang up the phone.

On the Tones page, in the Destination Address field for Ringback
                                       			 Tone, enter the extension that you dialed in Step 36 a.

Select Learn .

When the process is complete, check the check box for each newly
                                       			 learned tone and select Apply .

Hang up the phones that you used in Step 32 .

On the Configure menu, select Import/Export .

On the Import/Export page, under Export Settings, select Export
                                          				Settings .

In the File Download dialog box, select Save .

In the Save As dialog box, browse to the Windows workstation
                                       			 that has access to the TIMG units, browse to a directory where you want to save
                                       			 the file, and select Save .

In the Download Complete dialog box, select Open . Notepad
                                       			 opens the file Config.ini that you saved.

Locate the line with the following parameter:

```
telautoanswer
```

Confirm that the value of the parameter is no so that
                                       			 the line reads as follows:

```
telautoanswer = no
```

Locate the line with the following parameter:

```
telFacCDropProc
```

Confirm that the value of the parameter is !! so that the line reads as follows:

```
telFacCDropProc = !!
```

Save the file, and exit Notepad.

On the Configure menu of the TIMG unit, select Import/Export .

On the Import/Export page, under Import Settings, select Browse .

In the Choose File dialog box, browse to the file Config.ini
                                       			 that you saved.

Select Config.ini ,
                                       			 and select Open .

On the Import/Export page, select Import
                                          				Settings .

When prompted to restart the TIMG unit, select OK .

When the TIMG unit has restarted, in the View menu, select Refresh .

Repeat Step 1 through Step 57 on all
                                       			 remaining TIMG units.

| Step 1 | On a Windows workstation, sign in to a TIMG unit. |
|---|---|
| Step 2 | On the Configure menu, select IP . |
| Step 3 | On the IP page, enter the following settings for LAN1. Table 1. IP Page Settings for LAN1 Field Setting Client IP Address Enter the new IP address that you want to use for the TIMG unit. (This is the IP address that you enter in UTIM when you create
                                                      						  the integration.) Client Subnet Mask Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address. Default Network Gateway Address Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use. BOOTP Enabled If you are using DHCP, select Yes . If you are not using DHCP, select No . | Field | Setting | Client IP Address | Enter the new IP address that you want to use for the TIMG unit. (This is the IP address that you enter in UTIM when you create
                                                      						  the integration.) | Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address. | Default Network Gateway Address | Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use. | BOOTP Enabled | If you are using DHCP, select Yes . If you are not using DHCP, select No . |
| Field | Setting |
| Client IP Address | Enter the new IP address that you want to use for the TIMG unit. (This is the IP address that you enter in UTIM when you create
                                                      						  the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use. |
| BOOTP Enabled | If you are using DHCP, select Yes . If you are not using DHCP, select No . |
| Step 4 | Select Apply Changes . |
| Step 5 | On the Configure menu, select System . |
| Step 6 | On the System page, enter the following settings. Table 2. System Page Settings for the System and Telephony Groups Field Setting Operating Mode Select SIP . PCM Coding Select uLaw . | Field | Setting | Operating Mode | Select SIP . | PCM Coding | Select uLaw . |
| Field | Setting |
| Operating Mode | Select SIP . |
| PCM Coding | Select uLaw . |
| Step 7 | Determine which serial port on the TIMG unit you use to connect
                                       			 the data link serial cable from the phone system, then enter the following
                                       			 settings in the applicable group. Table 3. System Page Settings for Serial Port Groups Field Setting Serial Port Baud Rate Select the setting that is configured on the phone system. The default setting is 9600. Serial Port Parity Select the setting that is configured on the phone system. The default setting is None. Serial Port Data Bits Select the setting that is configured on the phone system. The default setting is 8. Serial Port Stop Bits Select the setting that is configured on the phone system. The default setting is 1. | Field | Setting | Serial Port Baud Rate | Select the setting that is configured on the phone system. The default setting is 9600. | Serial Port Parity | Select the setting that is configured on the phone system. The default setting is None. | Serial Port Data Bits | Select the setting that is configured on the phone system. The default setting is 8. | Serial Port Stop Bits | Select the setting that is configured on the phone system. The default setting is 1. |
| Field | Setting |
| Serial Port Baud Rate | Select the setting that is configured on the phone system. The default setting is 9600. |
| Serial Port Parity | Select the setting that is configured on the phone system. The default setting is None. |
| Serial Port Data Bits | Select the setting that is configured on the phone system. The default setting is 8. |
| Serial Port Stop Bits | Select the setting that is configured on the phone system. The default setting is 1. |
| Step 8 | Select Apply Changes . |
| Step 9 | On the Configure menu, select Gateway . |
| Step 10 | On the Gateway page, select the Gateway
                                          				Routing tab. |
| Step 11 | On the Gateway Routing tab, Unity Connection without a cluster,
                                       			 skip to Step 12 . If Unity
                                       			 Connection has a cluster configured, do the following substeps: In the Fault Tolerance Enabled field, select Yes . In the Load Balancing Enabled field, select No . |
| Step 12 | Under VoIP Endpoint ID, enter the following settings. Table 4. Gateway Routing Tab Settings Field Setting VoIP Endpoint ID: 1 (Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a
                                                         							 cluster configured) Enter the server name of the subscriber server. VoIP Endpoint ID: 2 (Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a
                                                         							 cluster configured) Enter the server name of the publisher server. | Field | Setting | VoIP Endpoint ID: 1 | (Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a
                                                         							 cluster configured) Enter the server name of the subscriber server. | VoIP Endpoint ID: 2 | (Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a
                                                         							 cluster configured) Enter the server name of the publisher server. |
| Field | Setting |
| VoIP Endpoint ID: 1 | (Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a
                                                         							 cluster configured) Enter the server name of the subscriber server. |
| VoIP Endpoint ID: 2 | (Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a
                                                         							 cluster configured) Enter the server name of the publisher server. |
| Step 13 | Select Apply
                                          				Changes . |
| Step 14 | On the Gateway page, select the Gateway
                                          				Advanced tab. |
| Step 15 | On the Gateway Advanced tab, enter the following settings. Table 5. Gateway Advanced Tab Settings Field Settings Advanced Call Routing Call Connect Mode Select OnAnswer . Send DNIS to VoIP
                                                      						  Endpoint Select No . Destination for
                                                      						  Unroutable IP Calls Leave this field blank. Destination for
                                                      						  Unroutable PBX Calls Leave this field blank. Monitor Call Connections Select No . Telephony Minimum Call Party Delay Enter 500 . Maximum Call Party Delay Enter 2000 . Dial Digit on Time Enter 100 . Dial Inter-Digit Time Enter 100 . Dial Pause Time Enter 2000 . Turn MWI On FAC Leave this field blank. Turn MWI Off FAC Leave this field blank. Dial Send Key Select None . Outbound Call Connect
                                                      						  Timeout Enter 10000 . Wait for Ringback/Connect
                                                      						  on Blind Transfer Select Yes . Hunt Group Extension Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports. Audio Audio Compression Select the preferred
                                                      						  codec for audio compression: G.711 G.729AB RTP Digit Relay Mode Select RFC2833 . Signaling Digit Relay
                                                      						  Mode Select Off . Voice Activity Detection Select On . Frame Size Select the applicable
                                                      						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable
                                                      						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. Quality of Service Call Control QOS Byte Enter 104 (equivalent to
                                                      						  DSCP AF31). RTP QOS Byte Enter 184 (equivalent to
                                                      						  DSCP EF). Traps and Alarms E-mail Alarms Enabled Select No . SNMP Traps Enabled Select No . HTTP Server Enabled Select Yes . HTTPs Server Enabled Select No . | Field | Settings | Advanced Call Routing | Call Connect Mode | Select OnAnswer . | Send DNIS to VoIP
                                                      						  Endpoint | Select No . | Destination for
                                                      						  Unroutable IP Calls | Leave this field blank. | Destination for
                                                      						  Unroutable PBX Calls | Leave this field blank. | Monitor Call Connections | Select No . | Telephony | Minimum Call Party Delay | Enter 500 . | Maximum Call Party Delay | Enter 2000 . | Dial Digit on Time | Enter 100 . | Dial Inter-Digit Time | Enter 100 . | Dial Pause Time | Enter 2000 . | Turn MWI On FAC | Leave this field blank. | Turn MWI Off FAC | Leave this field blank. | Dial Send Key | Select None . | Outbound Call Connect
                                                      						  Timeout | Enter 10000 . | Wait for Ringback/Connect
                                                      						  on Blind Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports. | Audio | Audio Compression | Select the preferred
                                                      						  codec for audio compression: G.711 G.729AB | RTP Digit Relay Mode | Select RFC2833 . | Signaling Digit Relay
                                                      						  Mode | Select Off . | Voice Activity Detection | Select On . | Frame Size | Select the applicable
                                                      						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable
                                                      						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Quality of Service | Call Control QOS Byte | Enter 104 (equivalent to
                                                      						  DSCP AF31). | RTP QOS Byte | Enter 184 (equivalent to
                                                      						  DSCP EF). | Traps and Alarms | E-mail Alarms Enabled | Select No . | SNMP Traps Enabled | Select No . | HTTP Server Enabled | Select Yes . | HTTPs Server Enabled | Select No . |
| Field | Settings |
| Advanced Call Routing |
| Call Connect Mode | Select OnAnswer . |
| Send DNIS to VoIP
                                                      						  Endpoint | Select No . |
| Destination for
                                                      						  Unroutable IP Calls | Leave this field blank. |
| Destination for
                                                      						  Unroutable PBX Calls | Leave this field blank. |
| Monitor Call Connections | Select No . |
| Telephony |
| Minimum Call Party Delay | Enter 500 . |
| Maximum Call Party Delay | Enter 2000 . |
| Dial Digit on Time | Enter 100 . |
| Dial Inter-Digit Time | Enter 100 . |
| Dial Pause Time | Enter 2000 . |
| Turn MWI On FAC | Leave this field blank. |
| Turn MWI Off FAC | Leave this field blank. |
| Dial Send Key | Select None . |
| Outbound Call Connect
                                                      						  Timeout | Enter 10000 . |
| Wait for Ringback/Connect
                                                      						  on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports. |
| Audio |
| Audio Compression | Select the preferred
                                                      						  codec for audio compression: G.711 G.729AB |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay
                                                      						  Mode | Select Off . |
| Voice Activity Detection | Select On . |
| Frame Size | Select the applicable
                                                      						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable
                                                      						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Quality of Service |
| Call Control QOS Byte | Enter 104 (equivalent to
                                                      						  DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to
                                                      						  DSCP EF). |
| Traps and Alarms |
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |
| HTTP Server Enabled | Select Yes . |
| HTTPs Server Enabled | Select No . |
| Step 16 | Select Apply
                                          				Changes . |
| Step 17 | On the Gateway page, select the Gateway
                                          				Capabilities tab. |
| Step 18 | Enter the following settings for all ports that are used by
                                       			 voice messaging ports on Unity Connection. Table 6. Gateway Capabilities Tab Settings Field Setting Telephony Port Capability Select Both . Telephony Port Enabled For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes . For ports that are not
                                                      						  used, select No . | Field | Setting | Telephony Port Capability | Select Both . | Telephony Port Enabled | For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes . For ports that are not
                                                      						  used, select No . |
| Field | Setting |
| Telephony Port Capability | Select Both . |
| Telephony Port Enabled | For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes . For ports that are not
                                                      						  used, select No . |
| Step 19 | Select Apply
                                          				Changes . |
| Step 20 | On the Configure menu, select T1E1 . |
| Step 21 | On the T1E1 page, select the T1/E1 Mode tab. |
| Step 22 | On the T1/E1 Mode tab, enter the following settings. Table 7. T1/E1 Mode Tab Settings Field Setting Line Mode Select T1 . Signaling Mode Select CAS . Interface Mode Select Terminal . | Field | Setting | Line Mode | Select T1 . | Signaling Mode | Select CAS . | Interface Mode | Select Terminal . |
| Field | Setting |
| Line Mode | Select T1 . |
| Signaling Mode | Select CAS . |
| Interface Mode | Select Terminal . |
| Step 23 | Select Apply
                                          				Changes . |
| Step 24 | Select the T1-CAS
                                          				Protocol tab. |
| Step 25 | On the T1-CAS Protocol tab, enter the following settings. Table 8. T1-CAS Protocol Tab Settings Field Setting T1 CAS Protocol Enter the setting that
                                                      						  matches the phone system programming. Line Encoding Enter the setting that
                                                      						  matches the phone system programming. Framing Enter the setting that
                                                      						  matches the phone system programming. Selects Transmit Pulse
                                                      						  Waveform Enter the setting that
                                                      						  matches the phone system programming. Flash Hook Enter the setting that
                                                      						  matches the phone system programming. Consult Call Dialtone
                                                      						  Drop Code Enter the setting that
                                                      						  matches the phone system programming. Consult Call Proceeding
                                                      						  Drop Code Enter the setting that
                                                      						  matches the phone system programming. Consult Call Busy Drop
                                                      						  Code Enter the setting that
                                                      						  matches the phone system programming. Consult Call Error Drop
                                                      						  Code Enter the setting that
                                                      						  matches the phone system programming. Consult Call Connected
                                                      						  Drop Code Enter the setting that
                                                      						  matches the phone system programming. Consult Call Disconnected
                                                      						  Drop Code Enter the setting that
                                                      						  matches the phone system programming. MWI confirmation Tone Select No . CPID Type Select TypeII_CPID . Initial Wait for Inband
                                                      						  CPID Enter 100 . Inband CPID Complete
                                                      						  Timeout Enter 300 . | Field | Setting | T1 CAS Protocol | Enter the setting that
                                                      						  matches the phone system programming. | Line Encoding | Enter the setting that
                                                      						  matches the phone system programming. | Framing | Enter the setting that
                                                      						  matches the phone system programming. | Selects Transmit Pulse
                                                      						  Waveform | Enter the setting that
                                                      						  matches the phone system programming. | Flash Hook | Enter the setting that
                                                      						  matches the phone system programming. | Consult Call Dialtone
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. | Consult Call Proceeding
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. | Consult Call Busy Drop
                                                      						  Code | Enter the setting that
                                                      						  matches the phone system programming. | Consult Call Error Drop
                                                      						  Code | Enter the setting that
                                                      						  matches the phone system programming. | Consult Call Connected
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. | Consult Call Disconnected
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. | MWI confirmation Tone | Select No . | CPID Type | Select TypeII_CPID . | Initial Wait for Inband
                                                      						  CPID | Enter 100 . | Inband CPID Complete
                                                      						  Timeout | Enter 300 . |
| Field | Setting |
| T1 CAS Protocol | Enter the setting that
                                                      						  matches the phone system programming. |
| Line Encoding | Enter the setting that
                                                      						  matches the phone system programming. |
| Framing | Enter the setting that
                                                      						  matches the phone system programming. |
| Selects Transmit Pulse
                                                      						  Waveform | Enter the setting that
                                                      						  matches the phone system programming. |
| Flash Hook | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Dialtone
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Proceeding
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Busy Drop
                                                      						  Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Error Drop
                                                      						  Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Connected
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Disconnected
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. |
| MWI confirmation Tone | Select No . |
| CPID Type | Select TypeII_CPID . |
| Initial Wait for Inband
                                                      						  CPID | Enter 100 . |
| Inband CPID Complete
                                                      						  Timeout | Enter 300 . |
| Step 26 | Select Apply
                                          				Changes . |
| Step 27 | On the Configure menu, select Serial
                                          				Protocol . |
| Step 28 | On the Serial Protocol page, enter the following settings. Table 9. Serial Protocol Page Settings Field Setting Serial Mode
                                                      						  (Master/Slave) Select the applicable
                                                      						  setting: Master —Select this
                                                            								setting when this TIMG unit is connected to the data link serial cable from the
                                                            								phone system. There can be only one master TIMG unit in a phone system
                                                            								integration. Slave —Select this
                                                            								setting when this TIMG unit is not connected to the data link serial cable from
                                                            								the phone system. There can be multiple slave TIMG units in a phone system
                                                            								integration. Serial Interface Protocol Select the serial
                                                      						  protocol that your phone system uses: SMDI MCI MD-110 MWI Response Timeout Enter 2000 . IP Address of Serial
                                                      						  Server If the TIMG unit is the
                                                      						  master, leave this field blank. If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system). Serial Cpid Expiration Enter 5000 . Logical Extension Number If the TIMG unit is the
                                                      						  master, leave this field blank. If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system). | Field | Setting | Serial Mode
                                                      						  (Master/Slave) | Select the applicable
                                                      						  setting: Master —Select this
                                                            								setting when this TIMG unit is connected to the data link serial cable from the
                                                            								phone system. There can be only one master TIMG unit in a phone system
                                                            								integration. Slave —Select this
                                                            								setting when this TIMG unit is not connected to the data link serial cable from
                                                            								the phone system. There can be multiple slave TIMG units in a phone system
                                                            								integration. | Serial Interface Protocol | Select the serial
                                                      						  protocol that your phone system uses: SMDI MCI MD-110 | MWI Response Timeout | Enter 2000 . | IP Address of Serial
                                                      						  Server | If the TIMG unit is the
                                                      						  master, leave this field blank. If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system). | Serial Cpid Expiration | Enter 5000 . | Logical Extension Number | If the TIMG unit is the
                                                      						  master, leave this field blank. If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system). |
| Field | Setting |
| Serial Mode
                                                      						  (Master/Slave) | Select the applicable
                                                      						  setting: Master —Select this
                                                            								setting when this TIMG unit is connected to the data link serial cable from the
                                                            								phone system. There can be only one master TIMG unit in a phone system
                                                            								integration. Slave —Select this
                                                            								setting when this TIMG unit is not connected to the data link serial cable from
                                                            								the phone system. There can be multiple slave TIMG units in a phone system
                                                            								integration. |
| Serial Interface Protocol | Select the serial
                                                      						  protocol that your phone system uses: SMDI MCI MD-110 |
| MWI Response Timeout | Enter 2000 . |
| IP Address of Serial
                                                      						  Server | If the TIMG unit is the
                                                      						  master, leave this field blank. If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system). |
| Serial Cpid Expiration | Enter 5000 . |
| Logical Extension Number | If the TIMG unit is the
                                                      						  master, leave this field blank. If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system). |
| Step 29 | Select Apply
                                          				Changes . |
| Step 30 | On the Configure menu, select SIP . |
| Step 31 | On the SIP page, enter the following settings. Table 10. SIP Page Settings Field Setting Host and Domain Name Enter the domain name of
                                                      						  the TIMG unit. Transport Type Select UDP . Call as Domain Name Select No . SIPS URI Scheme Enabled Select No . Invite Expiration Enter 120 . DNS Server Address Enter the IP address of
                                                      						  the DNS server. Registration Server
                                                      						  Address Leave this field blank. Registration Server Port Enter 5060 . Registration Expiration Enter 3600 . UDP/TCP Transports
                                                      						  Enabled Select Yes . TCP/UDP Server Port Enter 5060 . Primary Proxy Server
                                                      						  Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the
                                                      						  default setting. Backup Proxy Server
                                                      						  Address Not applicable. Leave the
                                                      						  default setting. Backup Proxy Server Port Not applicable. Leave the
                                                      						  default setting. Proxy Query Interval Enter 10 . T1 Time Enter 500 . T2 Time Enter 4000 . T4 Time Enter 5000 . | Field | Setting | Host and Domain Name | Enter the domain name of
                                                      						  the TIMG unit. | Transport Type | Select UDP . | Call as Domain Name | Select No . | SIPS URI Scheme Enabled | Select No . | Invite Expiration | Enter 120 . | DNS Server Address | Enter the IP address of
                                                      						  the DNS server. | Registration Server
                                                      						  Address | Leave this field blank. | Registration Server Port | Enter 5060 . | Registration Expiration | Enter 3600 . | UDP/TCP Transports
                                                      						  Enabled | Select Yes . | TCP/UDP Server Port | Enter 5060 . | Primary Proxy Server
                                                      						  Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. | Backup Proxy Server
                                                      						  Address | Not applicable. Leave the
                                                      						  default setting. | Backup Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. | Proxy Query Interval | Enter 10 . | T1 Time | Enter 500 . | T2 Time | Enter 4000 . | T4 Time | Enter 5000 . |
| Field | Setting |
| Host and Domain Name | Enter the domain name of
                                                      						  the TIMG unit. |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| SIPS URI Scheme Enabled | Select No . |
| Invite Expiration | Enter 120 . |
| DNS Server Address | Enter the IP address of
                                                      						  the DNS server. |
| Registration Server
                                                      						  Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration | Enter 3600 . |
| UDP/TCP Transports
                                                      						  Enabled | Select Yes . |
| TCP/UDP Server Port | Enter 5060 . |
| Primary Proxy Server
                                                      						  Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. |
| Backup Proxy Server
                                                      						  Address | Not applicable. Leave the
                                                      						  default setting. |
| Backup Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 500 . |
| T2 Time | Enter 4000 . |
| T4 Time | Enter 5000 . |
| Step 32 | Select Apply
                                          				Changes . |
| Step 33 | On the Configure menu, select Tones . |
| Step 34 | On the Tones page, select the Learn tab. Caution Destination addresses cannot be duplicated in the same session.
                                                      				  Otherwise, the process for learning tones do not succeed. If you do not have
                                                      				  enough available phones to learn all the tones at one time, you can run
                                                      				  multiple sessions to learn tones individually by checking or unchecking the
                                                      				  applicable Acquire Tone check boxes. | Caution | Destination addresses cannot be duplicated in the same session.
                                                      				  Otherwise, the process for learning tones do not succeed. If you do not have
                                                      				  enough available phones to learn all the tones at one time, you can run
                                                      				  multiple sessions to learn tones individually by checking or unchecking the
                                                      				  applicable Acquire Tone check boxes. |
| Caution | Destination addresses cannot be duplicated in the same session.
                                                      				  Otherwise, the process for learning tones do not succeed. If you do not have
                                                      				  enough available phones to learn all the tones at one time, you can run
                                                      				  multiple sessions to learn tones individually by checking or unchecking the
                                                      				  applicable Acquire Tone check boxes. |
| Step 35 | On the Tones page, for the Dialtone event, confirm that the
                                       			 Acquire Tone check box is checked and leave the Destination Address field
                                       			 blank. |
| Step 36 | On the Tones page, for the Busy Tone event, confirm that the
                                       			 Acquire Tone check box is checked and do the following substeps to verify that
                                       			 the tone is correct. From a available phone, call a second phone. Answer the second phone when it rings, and leave both handsets
                                             				  off so that both phones are busy. From a third phone, dial one of the busy phones. Confirm that you hear a busy tone. Hang up the third phone but leave the handsets for the other two
                                             				  phones off. |
| Step 37 | On the Tones page, in the Destination Address field for Busy
                                       			 Tone, enter the extension that you dialed in Step 36 c. from the third
                                       			 phone. |
| Step 38 | On the Tones page, for the Error/Reorder Tone event, confirm
                                       			 that the Acquire Tone check box is checked and do the following substeps to
                                       			 verify that the tone is correct. From an available phone, dial an extension that does not exist. Confirm that you hear the reorder or error tone. Hang up the phone. |
| Step 39 | On the Tones page, in the Destination Address field for
                                       			 Error/Reorder Tone, enter the extension that you dialed in Step 38 a. |
| Step 40 | On the Tones page, for the Ringback Tone event, confirm that the
                                       			 Acquire Tone check box is checked and do the following substeps to verify that
                                       			 the tone is correct. From an available phone, dial an extension that does exist. Confirm that you hear the ringback tone. Hang up the phone. |
| Step 41 | On the Tones page, in the Destination Address field for Ringback
                                       			 Tone, enter the extension that you dialed in Step 40 a. |
| Step 42 | Select Learn . |
| Step 43 | When the process is complete, check the check box for each newly
                                       			 learned tone and select Apply . |
| Step 44 | Hang up the phones that you used in Step 36 . |
| Step 45 | If the TIMG unit is connected to a Nortel SL-100 phone system,
                                       			 do the following substeps to learn the stutter dial tone. Otherwise, continue
                                       			 to Step 46 . On the Tones page, on the Learn tab, for the Dialtone event,
                                             				  confirm that the Acquire Tone check box is checked and enter ! in the Destination Address field. Uncheck the Acquire Tone check boxes for all other tones. Select Learn . When the process is complete, check the check box for each newly
                                             				  learned tone and select Apply . |
| Step 46 | On the Configure menu, select Restart . |
| Step 47 | On the Restart page, select Restart Unit
                                          				Now . |
| Step 48 | When the TIMG unit has restarted, in the View menu, select Refresh . |
| Step 49 | Repeat Step 1 through Step 48 on all
                                       			 remaining TIMG units. |

| Field | Setting |
|---|---|
| Client IP Address | Enter the new IP address that you want to use for the TIMG unit. (This is the IP address that you enter in UTIM when you create
                                                      						  the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use. |
| BOOTP Enabled | If you are using DHCP, select Yes . If you are not using DHCP, select No . |

| Field | Setting |
|---|---|
| Operating Mode | Select SIP . |
| PCM Coding | Select uLaw . |

| Field | Setting |
|---|---|
| Serial Port Baud Rate | Select the setting that is configured on the phone system. The default setting is 9600. |
| Serial Port Parity | Select the setting that is configured on the phone system. The default setting is None. |
| Serial Port Data Bits | Select the setting that is configured on the phone system. The default setting is 8. |
| Serial Port Stop Bits | Select the setting that is configured on the phone system. The default setting is 1. |

| Field | Setting |
|---|---|
| VoIP Endpoint ID: 1 | (Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a
                                                         							 cluster configured) Enter the server name of the subscriber server. |
| VoIP Endpoint ID: 2 | (Unity Connection without
                                                         							 a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a
                                                         							 cluster configured) Enter the server name of the publisher server. |

| Field | Settings |
|---|---|
| Advanced Call Routing |
| Call Connect Mode | Select OnAnswer . |
| Send DNIS to VoIP
                                                      						  Endpoint | Select No . |
| Destination for
                                                      						  Unroutable IP Calls | Leave this field blank. |
| Destination for
                                                      						  Unroutable PBX Calls | Leave this field blank. |
| Monitor Call Connections | Select No . |
| Telephony |
| Minimum Call Party Delay | Enter 500 . |
| Maximum Call Party Delay | Enter 2000 . |
| Dial Digit on Time | Enter 100 . |
| Dial Inter-Digit Time | Enter 100 . |
| Dial Pause Time | Enter 2000 . |
| Turn MWI On FAC | Leave this field blank. |
| Turn MWI Off FAC | Leave this field blank. |
| Dial Send Key | Select None . |
| Outbound Call Connect
                                                      						  Timeout | Enter 10000 . |
| Wait for Ringback/Connect
                                                      						  on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports. |
| Audio |
| Audio Compression | Select the preferred
                                                      						  codec for audio compression: G.711 G.729AB |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay
                                                      						  Mode | Select Off . |
| Voice Activity Detection | Select On . |
| Frame Size | Select the applicable
                                                      						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable
                                                      						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Quality of Service |
| Call Control QOS Byte | Enter 104 (equivalent to
                                                      						  DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to
                                                      						  DSCP EF). |
| Traps and Alarms |
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |
| HTTP Server Enabled | Select Yes . |
| HTTPs Server Enabled | Select No . |

| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
|---|---|

| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
|---|---|

| Field | Setting |
|---|---|
| Telephony Port Capability | Select Both . |
| Telephony Port Enabled | For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes . For ports that are not
                                                      						  used, select No . |

| Field | Setting |
|---|---|
| Line Mode | Select T1 . |
| Signaling Mode | Select CAS . |
| Interface Mode | Select Terminal . |

| Field | Setting |
|---|---|
| T1 CAS Protocol | Enter the setting that
                                                      						  matches the phone system programming. |
| Line Encoding | Enter the setting that
                                                      						  matches the phone system programming. |
| Framing | Enter the setting that
                                                      						  matches the phone system programming. |
| Selects Transmit Pulse
                                                      						  Waveform | Enter the setting that
                                                      						  matches the phone system programming. |
| Flash Hook | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Dialtone
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Proceeding
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Busy Drop
                                                      						  Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Error Drop
                                                      						  Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Connected
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. |
| Consult Call Disconnected
                                                      						  Drop Code | Enter the setting that
                                                      						  matches the phone system programming. |
| MWI confirmation Tone | Select No . |
| CPID Type | Select TypeII_CPID . |
| Initial Wait for Inband
                                                      						  CPID | Enter 100 . |
| Inband CPID Complete
                                                      						  Timeout | Enter 300 . |

| Field | Setting |
|---|---|
| Serial Mode
                                                      						  (Master/Slave) | Select the applicable
                                                      						  setting: Master —Select this
                                                            								setting when this TIMG unit is connected to the data link serial cable from the
                                                            								phone system. There can be only one master TIMG unit in a phone system
                                                            								integration. Slave —Select this
                                                            								setting when this TIMG unit is not connected to the data link serial cable from
                                                            								the phone system. There can be multiple slave TIMG units in a phone system
                                                            								integration. |
| Serial Interface Protocol | Select the serial
                                                      						  protocol that your phone system uses: SMDI MCI MD-110 |
| MWI Response Timeout | Enter 2000 . |
| IP Address of Serial
                                                      						  Server | If the TIMG unit is the
                                                      						  master, leave this field blank. If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system). |
| Serial Cpid Expiration | Enter 5000 . |
| Logical Extension Number | If the TIMG unit is the
                                                      						  master, leave this field blank. If the TIMG unit is a
                                                      						  slave, enter the IP address of the master TIMG unit (the TIMG unit that is
                                                      						  connected to the data link serial cable from the phone system). |

| Field | Setting |
|---|---|
| Host and Domain Name | Enter the domain name of
                                                      						  the TIMG unit. |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| SIPS URI Scheme Enabled | Select No . |
| Invite Expiration | Enter 120 . |
| DNS Server Address | Enter the IP address of
                                                      						  the DNS server. |
| Registration Server
                                                      						  Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration | Enter 3600 . |
| UDP/TCP Transports
                                                      						  Enabled | Select Yes . |
| TCP/UDP Server Port | Enter 5060 . |
| Primary Proxy Server
                                                      						  Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. |
| Backup Proxy Server
                                                      						  Address | Not applicable. Leave the
                                                      						  default setting. |
| Backup Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 500 . |
| T2 Time | Enter 4000 . |
| T4 Time | Enter 5000 . |

| Caution | Destination addresses cannot be duplicated in the same session.
                                                      				  Otherwise, the process for learning tones do not succeed. If you do not have
                                                      				  enough available phones to learn all the tones at one time, you can run
                                                      				  multiple sessions to learn tones individually by checking or unchecking the
                                                      				  applicable Acquire Tone check boxes. |
|---|---|

| Step 1 | On a Windows workstation, sign in to a TIMG unit. |
|---|---|
| Step 2 | On the Configure menu, select IP . |
| Step 3 | On the IP page, enter the following settings for LAN1. Table 11. IP Page Settings for LAN1 Field Setting Client IP Address Enter the new IP address that you want to use for the TIMG unit. (This is the IP address that you enter in UTIM when you create
                                                      						  the integration.) Client Subnet Mask Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address. Default Network Gateway Address Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use. BOOTP Enabled If you are using DHCP, select Yes . If you are not using DHCP, select No . | Field | Setting | Client IP Address | Enter the new IP address that you want to use for the TIMG unit. (This is the IP address that you enter in UTIM when you create
                                                      						  the integration.) | Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address. | Default Network Gateway Address | Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use. | BOOTP Enabled | If you are using DHCP, select Yes . If you are not using DHCP, select No . |
| Field | Setting |
| Client IP Address | Enter the new IP address that you want to use for the TIMG unit. (This is the IP address that you enter in UTIM when you create
                                                      						  the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use. |
| BOOTP Enabled | If you are using DHCP, select Yes . If you are not using DHCP, select No . |
| Step 4 | Select Apply Changes . |
| Step 5 | On the Configure menu, select System . |
| Step 6 | On the System page, enter the following settings. Table 12. System Page Settings for the System and Telephony Groups Field Setting Operating Mode Select SIP . PCM Coding Select uLaw . | Field | Setting | Operating Mode | Select SIP . | PCM Coding | Select uLaw . |
| Field | Setting |
| Operating Mode | Select SIP . |
| PCM Coding | Select uLaw . |
| Step 7 | Select Apply Changes . |
| Step 8 | On the Configure menu, select Gateway . |
| Step 9 | On the Gateway page, select the Gateway Routing tab. |
| Step 10 | On the Gateway Routing tab, Unity Connection without a cluster,
                                       			 skip to Step 11 . If Unity
                                       			 Connection has a cluster configured, do the following substeps: In the Fault Tolerance Enabled field, select Yes . In the Load Balancing Enabled field, select No . |
| Step 11 | Under VoIP Endpoint ID, enter the following settings. Table 13. Gateway Routing Tab Settings Field Setting VoIP Endpoint ID: 1 (Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server. (Unity Connection with a cluster configured) Enter the
                                                      						  server name of the subscriber server. VoIP Endpoint ID: 2 (Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server. (Unity Connection with a cluster configured) Enter the
                                                      						  server name of the publisher server. | Field | Setting | VoIP Endpoint ID: 1 | (Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server. (Unity Connection with a cluster configured) Enter the
                                                      						  server name of the subscriber server. | VoIP Endpoint ID: 2 | (Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server. (Unity Connection with a cluster configured) Enter the
                                                      						  server name of the publisher server. |
| Field | Setting |
| VoIP Endpoint ID: 1 | (Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server. (Unity Connection with a cluster configured) Enter the
                                                      						  server name of the subscriber server. |
| VoIP Endpoint ID: 2 | (Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server. (Unity Connection with a cluster configured) Enter the
                                                      						  server name of the publisher server. |
| Step 12 | Select Apply
                                          				Changes . |
| Step 13 | On the Gateway page, select the Gateway
                                          				Advanced tab. |
| Step 14 | On the Gateway Advanced tab, enter the following settings. Table 14. Gateway Advanced Tab Settings Field Settings Advanced Call Routing Call Connect Mode Select OnAnswer . Send DNIS to VoIP
                                                      						  Endpoint Select No . Destination for
                                                      						  Unroutable IP Calls Leave this field blank. Destination for
                                                      						  Unroutable PBX Calls Leave this field blank. Monitor Call Connections Select No . Telephony Minimum Call Party Delay Enter 500 . Maximum Call Party Delay Enter 2000 . Dial Digit on Time Enter 100 . Dial Inter-Digit Time Enter 100 . Dial Pause Time Enter 2000 . Turn MWI On FAC Enter the code that the
                                                      						  phone system uses to turn MWIs on. Turn MWI Off FAC Enter the code that the
                                                      						  phone system uses to turn MWIs off. Dial Send Key Select None . Outbound Call Connect
                                                      						  Timeout Enter 10000 . Wait for Ringback/Connect
                                                      						  on Blind Transfer Select Yes . Hunt Group Extension Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports. Audio Audio Compression Select the preferred
                                                      						  codec for audio compression: G.711 G.729AB RTP Digit Relay Mode Select RFC2833 . Signaling Digit Relay
                                                      						  Mode Select Off . Voice Activity Detection Select On . Frame Size Select the applicable
                                                      						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable
                                                      						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. Quality of Service Call Control QOS Byte Enter 104 (equivalent to
                                                      						  DSCP AF31). RTP QOS Byte Enter 184 (equivalent to
                                                      						  DSCP EF). Traps and Alarms E-mail Alarms Enabled Select No . SNMP Traps Enabled Select No . HTTP Server Enabled Select Yes . HTTPs Server Enabled Select No . | Field | Settings | Advanced Call Routing | Call Connect Mode | Select OnAnswer . | Send DNIS to VoIP
                                                      						  Endpoint | Select No . | Destination for
                                                      						  Unroutable IP Calls | Leave this field blank. | Destination for
                                                      						  Unroutable PBX Calls | Leave this field blank. | Monitor Call Connections | Select No . | Telephony | Minimum Call Party Delay | Enter 500 . | Maximum Call Party Delay | Enter 2000 . | Dial Digit on Time | Enter 100 . | Dial Inter-Digit Time | Enter 100 . | Dial Pause Time | Enter 2000 . | Turn MWI On FAC | Enter the code that the
                                                      						  phone system uses to turn MWIs on. | Turn MWI Off FAC | Enter the code that the
                                                      						  phone system uses to turn MWIs off. | Dial Send Key | Select None . | Outbound Call Connect
                                                      						  Timeout | Enter 10000 . | Wait for Ringback/Connect
                                                      						  on Blind Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports. | Audio | Audio Compression | Select the preferred
                                                      						  codec for audio compression: G.711 G.729AB | RTP Digit Relay Mode | Select RFC2833 . | Signaling Digit Relay
                                                      						  Mode | Select Off . | Voice Activity Detection | Select On . | Frame Size | Select the applicable
                                                      						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable
                                                      						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Quality of Service | Call Control QOS Byte | Enter 104 (equivalent to
                                                      						  DSCP AF31). | RTP QOS Byte | Enter 184 (equivalent to
                                                      						  DSCP EF). | Traps and Alarms | E-mail Alarms Enabled | Select No . | SNMP Traps Enabled | Select No . | HTTP Server Enabled | Select Yes . | HTTPs Server Enabled | Select No . |
| Field | Settings |
| Advanced Call Routing |
| Call Connect Mode | Select OnAnswer . |
| Send DNIS to VoIP
                                                      						  Endpoint | Select No . |
| Destination for
                                                      						  Unroutable IP Calls | Leave this field blank. |
| Destination for
                                                      						  Unroutable PBX Calls | Leave this field blank. |
| Monitor Call Connections | Select No . |
| Telephony |
| Minimum Call Party Delay | Enter 500 . |
| Maximum Call Party Delay | Enter 2000 . |
| Dial Digit on Time | Enter 100 . |
| Dial Inter-Digit Time | Enter 100 . |
| Dial Pause Time | Enter 2000 . |
| Turn MWI On FAC | Enter the code that the
                                                      						  phone system uses to turn MWIs on. |
| Turn MWI Off FAC | Enter the code that the
                                                      						  phone system uses to turn MWIs off. |
| Dial Send Key | Select None . |
| Outbound Call Connect
                                                      						  Timeout | Enter 10000 . |
| Wait for Ringback/Connect
                                                      						  on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports. |
| Audio |
| Audio Compression | Select the preferred
                                                      						  codec for audio compression: G.711 G.729AB |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay
                                                      						  Mode | Select Off . |
| Voice Activity Detection | Select On . |
| Frame Size | Select the applicable
                                                      						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable
                                                      						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Quality of Service |
| Call Control QOS Byte | Enter 104 (equivalent to
                                                      						  DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to
                                                      						  DSCP EF). |
| Traps and Alarms |
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |
| HTTP Server Enabled | Select Yes . |
| HTTPs Server Enabled | Select No . |
| Step 15 | Select Apply
                                          				Changes . |
| Step 16 | On the Gateway page, select the Gateway
                                          				Capabilities tab. |
| Step 17 | Enter the following settings for all ports that are used by
                                       			 voice messaging ports on Unity Connection. Table 15. Gateway Capabilities Tab Settings Field Setting Telephony Port Capability Select Both . Telephony Port Enabled For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes . For ports that are not
                                                      						  used, select No . | Field | Setting | Telephony Port Capability | Select Both . | Telephony Port Enabled | For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes . For ports that are not
                                                      						  used, select No . |
| Field | Setting |
| Telephony Port Capability | Select Both . |
| Telephony Port Enabled | For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes . For ports that are not
                                                      						  used, select No . |
| Step 18 | Select Apply
                                          				Changes . |
| Step 19 | On the Configure menu, select T1E1 . |
| Step 20 | On the T1E1 page, select the T1/E1 Mode tab. |
| Step 21 | On the T1/E1 Mode tab, enter the following settings. Table 16. T1/E1 Mode Tab Settings Field Setting Line Mode Select T1 . Signaling Mode Select CAS . Interface Mode Select Terminal . | Field | Setting | Line Mode | Select T1 . | Signaling Mode | Select CAS . | Interface Mode | Select Terminal . |
| Field | Setting |
| Line Mode | Select T1 . |
| Signaling Mode | Select CAS . |
| Interface Mode | Select Terminal . |
| Step 22 | Select Apply
                                          				Changes . |
| Step 23 | Select the T1-CAS
                                          				Protocol tab. |
| Step 24 | On the T1-CAS Protocol tab, enter the following settings. Table 17. T1-CAS Protocol Tab Settings Field Setting T1 CAS Protocol Select Loop_Start . Line Encoding Select B8ZS . Framing Select EFS . Selects Transmit Pulse
                                                      						  Waveform Select Short_Haul_110ft . Flash Hook Enter 550 . Consult Call Dialtone
                                                      						  Drop Code Enter !! . Consult Call Proceeding
                                                      						  Drop Code Enter !! . Consult Call Busy Drop
                                                      						  Code Enter ! . Consult Call Error Drop
                                                      						  Code Enter !! . Consult Call Connected
                                                      						  Drop Code Enter ,,,, . Consult Call Disconnected
                                                      						  Drop Code Enter ! . MWI confirmation Tone Select No . CPID Type Select TypeII_CPID . Initial Wait for Inband
                                                      						  CPID Enter 5000 . Inband CPID Complete
                                                      						  Timeout Enter 500 . | Field | Setting | T1 CAS Protocol | Select Loop_Start . | Line Encoding | Select B8ZS . | Framing | Select EFS . | Selects Transmit Pulse
                                                      						  Waveform | Select Short_Haul_110ft . | Flash Hook | Enter 550 . | Consult Call Dialtone
                                                      						  Drop Code | Enter !! . | Consult Call Proceeding
                                                      						  Drop Code | Enter !! . | Consult Call Busy Drop
                                                      						  Code | Enter ! . | Consult Call Error Drop
                                                      						  Code | Enter !! . | Consult Call Connected
                                                      						  Drop Code | Enter ,,,, . | Consult Call Disconnected
                                                      						  Drop Code | Enter ! . | MWI confirmation Tone | Select No . | CPID Type | Select TypeII_CPID . | Initial Wait for Inband
                                                      						  CPID | Enter 5000 . | Inband CPID Complete
                                                      						  Timeout | Enter 500 . |
| Field | Setting |
| T1 CAS Protocol | Select Loop_Start . |
| Line Encoding | Select B8ZS . |
| Framing | Select EFS . |
| Selects Transmit Pulse
                                                      						  Waveform | Select Short_Haul_110ft . |
| Flash Hook | Enter 550 . |
| Consult Call Dialtone
                                                      						  Drop Code | Enter !! . |
| Consult Call Proceeding
                                                      						  Drop Code | Enter !! . |
| Consult Call Busy Drop
                                                      						  Code | Enter ! . |
| Consult Call Error Drop
                                                      						  Code | Enter !! . |
| Consult Call Connected
                                                      						  Drop Code | Enter ,,,, . |
| Consult Call Disconnected
                                                      						  Drop Code | Enter ! . |
| MWI confirmation Tone | Select No . |
| CPID Type | Select TypeII_CPID . |
| Initial Wait for Inband
                                                      						  CPID | Enter 5000 . |
| Inband CPID Complete
                                                      						  Timeout | Enter 500 . |
| Step 25 | Select Apply
                                          				Changes . |
| Step 26 | On the Configure menu, select SIP . |
| Step 27 | On the SIP page, enter the following settings. Table 18. SIP Page Settings Field Setting Host and Domain Name Enter the domain name of
                                                      						  the TIMG unit. Transport Type Select UDP . Call as Domain Name Select No . SIPS URI Scheme Enabled Select No . Invite Expiration Enter 120 . DNS Server Address Enter the IP address of
                                                      						  the DNS server. Registration Server
                                                      						  Address Leave this field blank. Registration Server Port Enter 5060 . Registration Expiration Enter 3600 . UDP/TCP Transports
                                                      						  Enabled Select Yes . TCP/UDP Server Port Enter 5060 . Primary Proxy Server
                                                      						  Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the
                                                      						  default setting. Backup Proxy Server
                                                      						  Address Not applicable. Leave the
                                                      						  default setting. Backup Proxy Server Port Not applicable. Leave the
                                                      						  default setting. Proxy Query Interval Enter 10 . T1 Time Enter 500 . T2 Time Enter 4000 . T4 Time Enter 5000 . | Field | Setting | Host and Domain Name | Enter the domain name of
                                                      						  the TIMG unit. | Transport Type | Select UDP . | Call as Domain Name | Select No . | SIPS URI Scheme Enabled | Select No . | Invite Expiration | Enter 120 . | DNS Server Address | Enter the IP address of
                                                      						  the DNS server. | Registration Server
                                                      						  Address | Leave this field blank. | Registration Server Port | Enter 5060 . | Registration Expiration | Enter 3600 . | UDP/TCP Transports
                                                      						  Enabled | Select Yes . | TCP/UDP Server Port | Enter 5060 . | Primary Proxy Server
                                                      						  Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. | Backup Proxy Server
                                                      						  Address | Not applicable. Leave the
                                                      						  default setting. | Backup Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. | Proxy Query Interval | Enter 10 . | T1 Time | Enter 500 . | T2 Time | Enter 4000 . | T4 Time | Enter 5000 . |
| Field | Setting |
| Host and Domain Name | Enter the domain name of
                                                      						  the TIMG unit. |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| SIPS URI Scheme Enabled | Select No . |
| Invite Expiration | Enter 120 . |
| DNS Server Address | Enter the IP address of
                                                      						  the DNS server. |
| Registration Server
                                                      						  Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration | Enter 3600 . |
| UDP/TCP Transports
                                                      						  Enabled | Select Yes . |
| TCP/UDP Server Port | Enter 5060 . |
| Primary Proxy Server
                                                      						  Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. |
| Backup Proxy Server
                                                      						  Address | Not applicable. Leave the
                                                      						  default setting. |
| Backup Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 500 . |
| T2 Time | Enter 4000 . |
| T4 Time | Enter 5000 . |
| Step 28 | Select Apply
                                          				Changes . |
| Step 29 | On the Configure menu, select Tones . |
| Step 30 | On the Tones page, select the Learn tab. Caution Destination addresses cannot be duplicated in the same session.
                                                      				  Otherwise, the process for learning tones do not succeed. If you do not have
                                                      				  enough available phones to learn all the tones at one time, you can run
                                                      				  multiple sessions to learn tones individually by checking or unchecking the
                                                      				  applicable Acquire Tone check boxes. | Caution | Destination addresses cannot be duplicated in the same session.
                                                      				  Otherwise, the process for learning tones do not succeed. If you do not have
                                                      				  enough available phones to learn all the tones at one time, you can run
                                                      				  multiple sessions to learn tones individually by checking or unchecking the
                                                      				  applicable Acquire Tone check boxes. |
| Caution | Destination addresses cannot be duplicated in the same session.
                                                      				  Otherwise, the process for learning tones do not succeed. If you do not have
                                                      				  enough available phones to learn all the tones at one time, you can run
                                                      				  multiple sessions to learn tones individually by checking or unchecking the
                                                      				  applicable Acquire Tone check boxes. |
| Step 31 | On the Tones page, for the Dialtone event, confirm that the
                                       			 Acquire Tone check box is checked and leave the Destination Address field
                                       			 blank. |
| Step 32 | On the Tones page, for the Busy Tone event, confirm that the
                                       			 Acquire Tone check box is checked and do the following substeps to verify that
                                       			 the tone is correct. From a available phone, call a second phone. Answer the second phone when it rings, and leave both handsets
                                             				  off so that both phones are busy. From a third phone, dial one of the busy phones. Confirm that you hear a busy tone. Hang up the third phone but leave the handsets for the other two
                                             				  phones off. |
| Step 33 | On the Tones page, in the Destination Address field for Busy
                                       			 Tone, enter the extension that you dialed in Step 32 c. from the third
                                       			 phone. |
| Step 34 | On the Tones page, for the Error/Reorder Tone event, confirm
                                       			 that the Acquire Tone check box is checked and do the following substeps to
                                       			 verify that the tone is correct. From an available phone, dial an extension that does not exist. Confirm that you hear the reorder or error tone. Hang up the phone. |
| Step 35 | On the Tones page, in the Destination Address field for
                                       			 Error/Reorder Tone, enter the extension that you dialed in Step 34 a. |
| Step 36 | On the Tones page, for the Ringback Tone event, confirm that the
                                       			 Acquire Tone check box is checked and do the following substeps to verify that
                                       			 the tone is correct. From an available phone, dial an extension that does exist. Confirm that you hear the ringback tone. Hang up the phone. |
| Step 37 | On the Tones page, in the Destination Address field for Ringback
                                       			 Tone, enter the extension that you dialed in Step 36 a. |
| Step 38 | Select Learn . |
| Step 39 | When the process is complete, check the check box for each newly
                                       			 learned tone and select Apply . |
| Step 40 | Hang up the phones that you used in Step 32 . |
| Step 41 | On the Configure menu, select Import/Export . |
| Step 42 | On the Import/Export page, under Export Settings, select Export
                                          				Settings . |
| Step 43 | In the File Download dialog box, select Save . |
| Step 44 | In the Save As dialog box, browse to the Windows workstation
                                       			 that has access to the TIMG units, browse to a directory where you want to save
                                       			 the file, and select Save . |
| Step 45 | In the Download Complete dialog box, select Open . Notepad
                                       			 opens the file Config.ini that you saved. |
| Step 46 | Locate the line with the following parameter: telautoanswer |
| Step 47 | Confirm that the value of the parameter is no so that
                                       			 the line reads as follows: telautoanswer = no |
| Step 48 | Locate the line with the following parameter: telFacCDropProc |
| Step 49 | Confirm that the value of the parameter is !! so that the line reads as follows: telFacCDropProc = !! Caution The telFacCDropProc parameter must be set to !!. If the
                                                      				  telFacCDropProc parameter is set to 1, supervised transfers fail, and the
                                                      				  caller hear the called party standard greeting two times. | Caution | The telFacCDropProc parameter must be set to !!. If the
                                                      				  telFacCDropProc parameter is set to 1, supervised transfers fail, and the
                                                      				  caller hear the called party standard greeting two times. |
| Caution | The telFacCDropProc parameter must be set to !!. If the
                                                      				  telFacCDropProc parameter is set to 1, supervised transfers fail, and the
                                                      				  caller hear the called party standard greeting two times. |
| Step 50 | Save the file, and exit Notepad. |
| Step 51 | On the Configure menu of the TIMG unit, select Import/Export . |
| Step 52 | On the Import/Export page, under Import Settings, select Browse . |
| Step 53 | In the Choose File dialog box, browse to the file Config.ini
                                       			 that you saved. |
| Step 54 | Select Config.ini ,
                                       			 and select Open . |
| Step 55 | On the Import/Export page, select Import
                                          				Settings . |
| Step 56 | When prompted to restart the TIMG unit, select OK . |
| Step 57 | When the TIMG unit has restarted, in the View menu, select Refresh . |
| Step 58 | Repeat Step 1 through Step 57 on all
                                       			 remaining TIMG units. |

| Field | Setting |
|---|---|
| Client IP Address | Enter the new IP address that you want to use for the TIMG unit. (This is the IP address that you enter in UTIM when you create
                                                      						  the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from
                                                      						  the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that
                                                      						  the TIMG units use. |
| BOOTP Enabled | If you are using DHCP, select Yes . If you are not using DHCP, select No . |

| Field | Setting |
|---|---|
| Operating Mode | Select SIP . |
| PCM Coding | Select uLaw . |

| Field | Setting |
|---|---|
| VoIP Endpoint ID: 1 | (Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server. (Unity Connection with a cluster configured) Enter the
                                                      						  server name of the subscriber server. |
| VoIP Endpoint ID: 2 | (Unity Connection without a cluster) Enter the server name
                                                      						  of the Unity Connection server. (Unity Connection with a cluster configured) Enter the
                                                      						  server name of the publisher server. |

| Field | Settings |
|---|---|
| Advanced Call Routing |
| Call Connect Mode | Select OnAnswer . |
| Send DNIS to VoIP
                                                      						  Endpoint | Select No . |
| Destination for
                                                      						  Unroutable IP Calls | Leave this field blank. |
| Destination for
                                                      						  Unroutable PBX Calls | Leave this field blank. |
| Monitor Call Connections | Select No . |
| Telephony |
| Minimum Call Party Delay | Enter 500 . |
| Maximum Call Party Delay | Enter 2000 . |
| Dial Digit on Time | Enter 100 . |
| Dial Inter-Digit Time | Enter 100 . |
| Dial Pause Time | Enter 2000 . |
| Turn MWI On FAC | Enter the code that the
                                                      						  phone system uses to turn MWIs on. |
| Turn MWI Off FAC | Enter the code that the
                                                      						  phone system uses to turn MWIs off. |
| Dial Send Key | Select None . |
| Outbound Call Connect
                                                      						  Timeout | Enter 10000 . |
| Wait for Ringback/Connect
                                                      						  on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number
                                                      						  for the Unity Connection voice messaging ports. |
| Audio |
| Audio Compression | Select the preferred
                                                      						  codec for audio compression: G.711 G.729AB |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay
                                                      						  Mode | Select Off . |
| Voice Activity Detection | Select On . |
| Frame Size | Select the applicable
                                                      						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable
                                                      						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
| Quality of Service |
| Call Control QOS Byte | Enter 104 (equivalent to
                                                      						  DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to
                                                      						  DSCP EF). |
| Traps and Alarms |
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |
| HTTP Server Enabled | Select Yes . |
| HTTPs Server Enabled | Select No . |

| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
|---|---|

| Caution | Failure to use the
                                                                        								  correct setting results in recorded messages containing nothing but silence. |
|---|---|

| Field | Setting |
|---|---|
| Telephony Port Capability | Select Both . |
| Telephony Port Enabled | For ports that are used
                                                      						  by voice messaging ports on Unity Connection, select Yes . For ports that are not
                                                      						  used, select No . |

| Field | Setting |
|---|---|
| Line Mode | Select T1 . |
| Signaling Mode | Select CAS . |
| Interface Mode | Select Terminal . |

| Field | Setting |
|---|---|
| T1 CAS Protocol | Select Loop_Start . |
| Line Encoding | Select B8ZS . |
| Framing | Select EFS . |
| Selects Transmit Pulse
                                                      						  Waveform | Select Short_Haul_110ft . |
| Flash Hook | Enter 550 . |
| Consult Call Dialtone
                                                      						  Drop Code | Enter !! . |
| Consult Call Proceeding
                                                      						  Drop Code | Enter !! . |
| Consult Call Busy Drop
                                                      						  Code | Enter ! . |
| Consult Call Error Drop
                                                      						  Code | Enter !! . |
| Consult Call Connected
                                                      						  Drop Code | Enter ,,,, . |
| Consult Call Disconnected
                                                      						  Drop Code | Enter ! . |
| MWI confirmation Tone | Select No . |
| CPID Type | Select TypeII_CPID . |
| Initial Wait for Inband
                                                      						  CPID | Enter 5000 . |
| Inband CPID Complete
                                                      						  Timeout | Enter 500 . |

| Field | Setting |
|---|---|
| Host and Domain Name | Enter the domain name of
                                                      						  the TIMG unit. |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| SIPS URI Scheme Enabled | Select No . |
| Invite Expiration | Enter 120 . |
| DNS Server Address | Enter the IP address of
                                                      						  the DNS server. |
| Registration Server
                                                      						  Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration | Enter 3600 . |
| UDP/TCP Transports
                                                      						  Enabled | Select Yes . |
| TCP/UDP Server Port | Enter 5060 . |
| Primary Proxy Server
                                                      						  Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. |
| Backup Proxy Server
                                                      						  Address | Not applicable. Leave the
                                                      						  default setting. |
| Backup Proxy Server Port | Not applicable. Leave the
                                                      						  default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 500 . |
| T2 Time | Enter 4000 . |
| T4 Time | Enter 5000 . |

| Caution | Destination addresses cannot be duplicated in the same session.
                                                      				  Otherwise, the process for learning tones do not succeed. If you do not have
                                                      				  enough available phones to learn all the tones at one time, you can run
                                                      				  multiple sessions to learn tones individually by checking or unchecking the
                                                      				  applicable Acquire Tone check boxes. |
|---|---|

| Caution | The telFacCDropProc parameter must be set to !!. If the
                                                      				  telFacCDropProc parameter is set to 1, supervised transfers fail, and the
                                                      				  caller hear the called party standard greeting two times. |
|---|---|