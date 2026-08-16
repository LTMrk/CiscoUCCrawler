---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-integration-timg-b-15cucinttimg-b-14cucinttimg-chapter-010-htm-9babe2935b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/timg/b_15cucinttimg/b_14cucinttimg_chapter_010.html
retrieved_at: 2026-08-16T18:47:31.290805+00:00
---

TIMG Integration Guide for Cisco Unity Connection Release 15

# TIMG Integration Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Setting Up an Avaya Definity G3 In-Band TIMG Integration with Cisco
	 Unity Connection

## Chapter: Setting Up an Avaya Definity G3 In-Band TIMG Integration with Cisco
	 Unity Connection

# Setting Up an Avaya Definity G3 In-Band TIMG Integration with Cisco
                     	 Unity Connection

For detailed instructions for setting up an Avaya Definity G3 in-band
                        		TIMG integration with Cisco Unity Connection, see the following sections in
                        		this chapter:

## Setting Up an Avaya Definity G3 In-Band TIMG Integration with Cisco
                        	 Unity Connection

For detailed instructions for setting up an Avaya Definity G3 in-band
                           		TIMG integration with Cisco Unity Connection, see the following sections in
                           		this chapter:

### Task List to
                           	 Create an Avaya Definity G3 In-Band TIMG Integration

Before doing the following tasks to integrate Unity Connection with the phone system using the T1 media gateway (TIMG), confirm
                              that the Unity Connection server is ready for the integration after completing the installation following the steps as mentioned
                              in the " Installing Cisco Unity Connection " chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html .

Review the system and equipment requirements to confirm that all
                                    			 phone system and Unity Connection server requirements have been met. See the Requirements section.

Plan how the voice messaging ports used by Unity Connection. See
                                    			 the Planning
                                       				the Usage of Voice Messaging Port in Cisco Unity Connection chapter.

Program the phone system and extensions. See the Programming
                                       				Phone System for In-Band TIMG Integration section.

Set up the TIMG units for an in-band integration. See the Setting
                                       				Up the TIMG Units section.

Create the integration. See the Creating
                                       				an Integration with the Phone System section.

Test the integration. See the Testing
                                       				the Integration chapter.

If this integration is a second or subsequent integration, add
                                    			 the applicable new user templates for the new phone system. See the Adding
                                       				New User Templates for Multiple Integrations chapter.

### Requirements

The Avaya Definity G3 in-band TIMG integration supports configurations
                              		of the following components:

#### Phone System

Avaya Definity G3 phone system.

T1 digital trunk interface card.

One or more TIMG units (media gateways).

The voice messaging ports in the phone system
                                       			 connected by T1 digital lines (DS1 or “dry T1” digital lines only) to the ports
                                       			 on the TIMG units.

Caution

The TIMG units connected to the same LAN or
                                       			 WAN that Unity Connection is connected to.

If the TIMG units connect to a WAN, the
                                       			 requirements for the WAN network connections are:

For G.729a codec formatting, a minimum of
                                             				  32.76 Kbps guaranteed bandwidth for each voice messaging port.

For G.711 codec formatting, a minimum of
                                             				  91.56 Kbps guaranteed bandwidth for each voice messaging port.

No network devices that implement network
                                             				  address translation (NAT).

A maximum 200 ms one-way one-way network
                                             				  latency.

The phone system ready for the integration, as
                                       			 described in the documentation for the phone system.

#### Unity Connection
                              	 Server

Unity Connection installed and ready for the integration after completing the installation following the steps as mentioned
                                       in the " Installing Cisco Unity Connection " chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

A license that enables the applicable number of voice messaging
                                       			 ports.

#### Centralized Voice Messaging

Unity Connection supports centralized voice
                                 		messaging through the phone system, which supports various inter-phone system
                                 		networking protocols including proprietary protocols such as Avaya DCS, Nortel
                                 		MCDN, or Siemens CorNet, and standards-based protocols such as QSIG or DPNSS.
                                 		Note that centralized voice messaging is a function of the phone system and its
                                 		inter-phone system networking, not voicemail. Unity Connection supports
                                 		centralized voice messaging as long as the phone system and its inter-phone
                                 		system networking are properly configured.

### Programming Phone
                           	 System for In-Band TIMG Integration

If you use programming options other than those supplied in the
                                 		  following procedure, the performance of the integration may be affected.

Caution

Step 1

Create a coverage path which contains the TIMG unit hunt group
                                          			 number as the coverage point.

Step 2

Assign the coverage path that you created in Step 1 to the user stations that must forward to the voice messaging ports on the TIMG
                                          			 units when calls are not answered or when the user station is busy, based on
                                          			 one of the call transfer types shown in Table 3-1 .

Transfer Type

Usage

Release transfer

(blind transfer)

Program the user station to forward calls to the pilot number
                                                         						  when:

The extension is busy.

The call is not answered.

Supervised transfer

Program the user station to forward calls to the pilot number
                                                         						  only when the call is not answered (on the phone system, the number of rings
                                                         						  before forwarding must be more than the number of rings to supervise the call).
                                                         						  Confirm that call forwarding is disabled when the extension is busy.

Step 3

Assign an extension number for each voice messaging port, which
                                          			 is a digital line that connects to the TIMG unit, and set the voice messaging
                                          			 port options as shown in Table 3-2 .

Option

Setting

Extension

Enter the extension number of the digital line.

Type

Enter the applicable setting:

VMI

VMIFD

Loss Group

Enter 4 .

Off Premises Station

Enter y .

R Balance Network

Enter n .

Survivable COR

Enter internal .

Survivable Trunk Dest

Enter y .

LWC Activation

Enter y .

LWC Log External Calls

Enter n .

CDR Privacy

Enter n .

Redirect Notification

Enter y .

Per Button Ring Control

Enter n .

Bridged Call Alerting

Enter n .

Switch hook Flash

Enter y .

Ignore Rotary Digits

Enter n .

H.320 Conversion

Enter n .

Service Link Mode

Enter as-needed .

Multimedia Mode

Enter basic .

Coverage Message
                                                         						  Retrieval

Enter y .

Auto Answer

Enter none .

Data Restriction

Enter n .

Distinctive Audible Alert

Enter y .

Adjunct Supervision

Enter y .

Audible Message Waiting

Enter n .

Coverage After Forwarding

Enter s .

Multimedia Early Answer

Enter n .

LWC Appearance

Enter call-appr .

Step 4

Set the DS1 Circuit Pack options as shown in Table 3-3 .

Option

Setting

Line Compensation

Enter 1 .

Signaling Mode

Enter robbed-bit .

Line Coding

Enter b8zs .

Framing Mode

Enter esf .

Interface Companding

Enter mulaw .

Idle Code

Enter 11111111 .

Slip Detection

Enter n .

Echo Cancellation

Enter n .

Near-end CSU Type

Enter other .

Step 5

Assign a the voice messaging ports to a hunt group by setting
                                          			 the options shown in Table 3-4 .

Option

Setting

LWC Reception

Enter none .

Message Center

Enter none .

Group Number

Enter the hunt group
                                                         						  number.

Group Extension

Enter the pilot number
                                                         						  for the hunt group.

Group Type

Enter ucd-mia .

Group Name

Enter the display name
                                                         						  for the hunt group.

Queue?

Enter n .

Step 6

Enter the group member assignments for the voice messaging ports
                                          			 that answer calls and press Enter .

#### Setting Up the
                              	 TIMG Units

Do the following procedures to set up the TIMG units (media
                                    		  gateways) that are connected to the phone system.

These procedures
                                    		  require that the following tasks have already been completed:

- The phone system is
                                       			 connected to the TIMG units using T1 digital lines.

- The TIMG units are
                                       			 connected to a power source.

- The TIMG units are ready to
                                       			 be connected to the LAN or WAN.

Caution

Fields that are
                                    		  not mentioned in the following procedures must keep their default values. For
                                    		  the default values of all fields, see the manufacturer documentation for the
                                    		  TIMG units.

Step 1

On a Windows workstation that have access to the TIMG units, go
                                             			 to the following link: http://software.cisco.com/download/navigator.html?mdfid=280082558&i=rm .

This
                                                            				  procedure describes the steps when using Internet Explorer as your web browser.
                                                            				  If you are using a different web browser, the steps may differ.

Step 2

In the tree control on the Downloads Home page, expand Unified
                                             			 Communications> Unified Communications Applications > Messaging >
                                             			 Cisco Unity and select Cisco Unity Telephony Integration.

Step 3

On the Log In page, enter your username and password, then
                                             			 select Log In .

Step 4

On the Select a Release page, under Latest Releases, select the
                                             			 most recent release.

Step 5

In the right column, select the version of the firmware for your
                                             			 TIMG units.

Step 6

On the Download Image page, select Download .

Step 7

On the Supporting Document(s) page, select Agree .

Step 8

In the File Download dialog box, select Save .

Step 9

In the Save As dialog box, browse to the Windows workstation
                                             			 that have access the TIMG units, browse to a directory where you want to save
                                             			 the file, and select Save .

Step 10

In the Download Complete dialog box, select Open . The window for extracting the TIMG firmware
                                             			 update files appears.

Step 11

Select Extract .

Step 12

In the Extract dialog box, browse to the directory where you
                                             			 want the extracted files, and select Extract .

Step 13

Close the window for the extracting application.

#### Setting Up the
                              	 TIMG Units (Firmware Version 6.x)

Step 1

On the Windows workstation, add a temporary route to enable
                                             			 access to the TIMG units.

On the Windows Start menu, select Run .

Enter cmd , and press Enter . The Command Prompt window appears.

At the command prompt, enter route add 10.12.13.74 <IP Address of Workstation> , and
                                                   				  press Enter .

For example, if the IP address of the workstation is 198.1.3.25,
                                                      					 enter “route add 10.12.13.74<space>198.1.3.25” in the Command Prompt
                                                      					 window.

Close the Command Prompt window.

Step 2

Connect a TIMG unit to the network.

Step 3

In the web browser, go to http://10.12.13.74 .

Step 4

To sign in, enter the following case-sensitive settings.

Field

Setting

Username

Enter admin .

Password

Enter IpodAdmin .

Step 5

Select OK .

Step 6

On the System menu, select Upgrade .

Step 7

On the Upgrade page, under Browse for Upgrade File, select Browse .

Step 8

In the Choose File dialog box, browse to the directory on the
                                             			 Windows workstation that has the extracted TIMG firmware update files.

Step 9

Select T1E1_<xx > .app (where <xx> is multiple
                                             			 digits), and select Open .

Step 10

On the Upgrade page, select Install File .

Step 11

After the file is installed, a message prompting you to restart
                                             			 the TIMG unit appears. Select Cancel .

Caution

Step 12

Repeat Step 6 through Step 11 for the following files:

T1E1_<xx>.fsh

T1E1_<xx>.msd

Step 13

On the Configuration menu, select Import/Export .

Step 14

On the Import/Export page, select Browse .

Step 15

In the Choose File dialog box, browse to the file
                                             			 T1_LS_Cfg_LucentG3.ini.

Step 16

Select T1_LS_Cfg_LucentG3.ini , and select Open .

Step 17

On the Import/Export page, select Import File .

Step 18

After the file is imported, a message prompting you to restart
                                             			 the TIMG unit appears. Select OK .

Step 19

In the web browser, go to http://10.12.13.74 .

Step 20

To sign in, enter the following case-sensitive settings.

Field

Setting

Username

Enter admin .

Password

Enter IpodAdmin .

Step 21

Select OK .

Step 22

On the System menu, select Password .

Step 23

On the Change Password page, enter the following settings.

Field

Setting

Old Password

Enter IpodAdmin . (This
                                                            						  setting is case sensitive.)

New Password

Enter your new password.
                                                            						  (This setting is case sensitive.)

Confirm Password

Enter your new password.
                                                            						  (This setting is case sensitive.)

Step 24

Select Change .

Step 25

On the Configuration menu, select Mgmt
                                                				Protocols .

Step 26

On the Management Protocols page, enter the following settings.

Field

Settings

E-mail Alarms Enabled

Select No .

SNMP Traps Enabled

Select No .

HTTP Server Enabled

Select Yes .

HTTPs Server Enabled

Select No .

Step 27

Select Submit .

Step 28

On the Configuration menu, select Routing
                                                				Table .

Step 29

On the Routing Table page, under Router Configuration, select VoIP Host
                                                				Groups .

Step 30

Under VoIP Host Groups, enter the following settings for the
                                             			 first VoIP Host Group.

Field

Settings

Name

Accept the default or
                                                            						  enter another descriptive name of the VoIP host group.

Load-Balanced

(Unity Connection without
                                                               							 a cluster) Select False .

(Unity Connection with a
                                                               							 cluster configured) Select False .

Fault-Tolerant

(Unity Connection without
                                                               							 a cluster) Select False .

(Unity Connection with a
                                                               							 cluster configured) Select True .

Step 31

For Unity Connection without a cluster, under Host List, enter
                                             			 the host name or IP address of the Unity Connection server and the server port
                                             			 in the format <host name or IP address>:5060.

For Unity Connection with a cluster configured, under Host List,
                                                				enter the host name or IP address of the subscriber server (the second Unity
                                                				Connection server that you installed) and the server port in the format
                                                				<host name or IP address>:5060.

Step 32

For Unity Connection without a cluster, continue to Step 34 .
                                             			 For Unity Connection with a cluster configured, select Add Host .

Step 33

In the second field, enter the host name or IP address of the
                                             			 publisher server (the first Unity Connection server that you installed) and the
                                             			 server port in the format <host name or IP address>:5060.

Step 34

Select Submit .

Step 35

On the Configuration menu, select TDM > T1/E1 .

Step 36

On the T1/E1 Configuration page, enter the following settings.

Field

Settings

Line Settings

Line Mode

Select T1 .

Signaling Mode

Select CAS .

Interface Mode

Select Terminal .

T1 Line

Line Encoding

Select B8ZS .

Framing

Select EFS .

Selects Transmit Pulse
                                                            						  Waveform

Select Short_Haul_110ft .

T1 CAS Protocol

T1 CAS Protocol

Select Loop_Start .

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

Failover Settings

Enable Failover

Select No .

Step 37

Select Submit .

Step 38

On the Configuration menu, select TDM > General .

Step 39

On the TDM General Settings page, enter the following settings.

Field

Settings

PCM Coding

Select uLaw .

Minimum Call Party Delay
                                                            						  (ms)

Enter 500 .

Maximum Call Party Delay
                                                            						  (ms)

Enter 2000 .

Dial Digit on Time (ms)

Enter 100 .

Dial Inter-Digit Time
                                                            						  (ms)

Enter 100 .

Dial Pause Time (ms)

Enter 2000 .

Turn MWI On FAC

Enter the code that the
                                                            						  phone system uses to turn MWIs on.

Turn MWI Off FAC

Enter the code that the
                                                            						  phone system uses to turn MWIs off.

Outbound Call Connect
                                                            						  Timeout (ms)

Enter 10000 .

Wait for Ringback/Connect
                                                            						  on Blind Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number of
                                                            						  the Unity Connection voice messaging ports.

Step 40

Select Submit .

Step 41

On the Configuration menu, select TDM > Port
                                                   				  Enable .

Step 42

On the TDM Port Enabling page, select No for the
                                             			 ports that you want to disable on the TIMG unit.

Step 43

Confirm that Yes is
                                             			 selected for all other ports on the TIMG unit.

Step 44

Select Submit .

Step 45

On the Configuration menu, select VoIP > General .

Step 46

On the VoIP General Settings page, enter the following settings.

Field

Setting

User-Agent

Host and Domain Name

Enter the domain name of
                                                            						  the TIMG unit.

Transport Type

Select UDP .

Call as Domain Name

Select No .

SIPS URI Scheme Enabled

Select No .

Invite Expiration (sec)

Enter 120 .

Server

DNS Server Address

Enter the IP Address of
                                                            						  the Domain Name Server that the TIMG unit uses.

Registration Server
                                                            						  Address

Leave this field blank.

Registration Server Port

Enter 5060 .

Registration Expiration
                                                            						  (sec)

Enter 3600 .

TCP/UDP

UDP/TCP Transports
                                                            						  Enabled

Select Yes .

TCP/UDP Server Port

Enter 5060 .

Proxy

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

Timing

T1 Time

Enter 500 .

T2 Time

Enter 4000 .

T4 Time

Enter 5000 .

Monitoring

Monitor Call Connections

Select No .

Step 47

Select Submit .

Step 48

On the Configuration menu, select VoIP > Media .

Step 49

On the VoIP Media Settings page, enter the following settings.

Field

Settings

Audio

Audio Compression

Select the preferred
                                                            						  codec for audio compression:

G.711u —The TIMG unit
                                                                  								uses only the G.711 mu-law codec.

G.729AB —The TIMG unit
                                                                  								prefers the G.729 codec but can also use the G.711 mu-law codec.

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

Caution

Frames Per Packet

Select the applicable
                                                            						  setting:

G.711— 1

G.729AB— 2

Caution

Step 50

Select Submit .

Step 51

On the Configuration menu, select VoIP > QOS .

Step 52

On the VoIP QOS Configuration page, enter the following
                                             			 settings.

Field

Settings

Call Control QOS Byte

Enter 104 (equivalent to
                                                            						  DSCP AF31).

RTP QOS Byte

Enter 184 (equivalent to
                                                            						  DSCP EF).

Step 53

Select Submit .

Step 54

On the Configuration menu, select IP .

Step 55

On the IP Settings, LAN1 page, enter the following settings.

Field

Settings

Client IP Address

Enter the new IP address
                                                            						  that you want to use for the TIMG unit.

(This is the IP address
                                                            						  that you enter in Cisco Unity Connection Administration when you create the
                                                            						  integration.)

Client Subnet Mask

Enter the new subnet
                                                            						  mask, if the subnet mask is different from the default IP address.

Default Network Gateway
                                                            						  Address

Enter the IP address of
                                                            						  the default network gateway router that the TIMG units use.

BOOTP Enabled

If you are using DHCP,
                                                            						  select Yes .

If you are not using
                                                            						  DHCP, select No .

Step 56

Select Submit .

Step 57

On the Configuration menu, select Tone
                                                				Detection .

Step 58

On the Tone Detection page, under Call Progress Tone - Learn, in
                                             			 the Learn Tone Event field, select Busy and do
                                             			 the following substeps to verify that the tone is correct.

From a available phone, call a second phone.

Answer the second phone when it rings, and leave both handsets
                                                   				  off so that both phones are busy.

From a third phone, dial one of the busy phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the handsets for the other two
                                                   				  phones off.

Step 59

Under Call Progress Tone - Learn, in the Dial String field,
                                             			 enter the extension that you dialed in Step 58c from the third phone.

Step 60

Select Learn .

Step 61

On the Tone Detection page, under Call Progress Tone - Learn, in
                                             			 the Learn field, select Error and do
                                             			 the following substeps to verify that the tone is correct.

From an available phone, dial an extension that does not exist.

Confirm that you hear the reorder or error tone.

Hang up the phone.

Step 62

Under Call Progress Tone - Learn, in the Dial String field,
                                             			 enter the extension that you dialed in Step 61a

Step 63

Select Learn .

Step 64

On the Tone Detection page, under Call Progress Tone - Learn, in
                                             			 the Learn field, select Ringback and
                                             			 do the following substeps to verify that the tone is correct.

From an available phone, dial an extension that does exist.

Confirm that you hear the ringback tone.

Hang up the phone.

Step 65

Under Call Progress Tone - Learn, in the Dial String field,
                                             			 enter the extension that you dialed in Step 64a

Step 66

Select Learn .

Step 67

Select Submit .

Step 68

Hang up the phones that you used in Step 58 .

Step 69

On the Configuration menu, select Import/Export .

Step 70

On the Import/Export page, under Export Files, select Export All
                                                				Settings .

Step 71

In the File Download dialog box, select Save .

Step 72

In the Save As dialog box, browse to the Windows workstation
                                             			 that has access to the TIMG units, browse to a directory where you want to save
                                             			 the file, and select Save .

Step 73

In the Download Complete dialog box, select Open . Notepad
                                             			 opens the file Config.ini that you saved.

Step 74

Locate the line with the following parameter:

```
telautoanswer
```

Step 75

Confirm that the value of the parameter is no so that
                                             			 the line reads as follows:

```
telautoanswer = no
```

Step 76

Locate the line with the following parameter:

```
telFacCDropProc
```

Step 77

Confirm that the value of the parameter is !! so that the line reads as follows:

```
telFacCDropProc = !!
```

Caution

Step 78

Save the file, and exit Notepad.

Step 79

On the Configuration menu of the TIMG unit, select Import/Export .

Step 80

On the Import/Export page, under Browse for Import File, select Browse .

Step 81

In the Choose File dialog box, browse to the file Config.ini
                                             			 that you saved.

Step 82

Select Config.ini ,
                                             			 and select Open .

Step 83

On the Import/Export page, select Import File .

Step 84

When prompted to restart the TIMG unit, select OK .

Step 85

Repeat Step 2 through Step 84 on all remaining TIMG units.

### Creating an
                           	 Integration with the Phone System

After ensuring that the phone system, the TIMG units and the
                                 		  Unity Connection server are ready for the integration, do the following
                                 		  procedures to set up the integration and to enter the port settings.

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System .

Step 2

On the Search Phone Systems page, under Display Name, select the
                                          			 name of the default phone system.

Step 3

On the Phone System Basics page, in the Phone System Name field,
                                          			 enter the descriptive name that you want for the phone system.

Step 4

If you want to use this phone system as the default for TRaP
                                          			 connections so that administrators and users without voicemail boxes can record
                                          			 and playback through the phone in Unity Connection web applications, check the Default TRAP Switch check box. If you want to use
                                          			 another phone system as the default for TRaP connections, uncheck this check
                                          			 box.

Step 5

Select Save .

Step 6

On the Phone System Basics page, in the Related Links drop-down
                                          			 box, select Add Port Group and select Go .

Step 7

On the New Port Group page, enter the applicable settings and
                                          			 select Save .

Field

Setting

Phone System

Select the name of the phone system that you entered in Step 3 .

Create From

Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box.

Display Name

Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want.

SIP Security Profile

Select 5060 .

SIP Transport Protocol

Select the SIP transport protocol that Unity Connection uses.

IPv4 Address or Host Name

Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection.

IPv6 Address or Host Name

Do not enter a value in this field. IPv6 is not supported for
                                                         						  TIMG integrations.

IP Address or Host Name

Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection.

Port

Enter the SIP port of the TIMG unit that Unity Connection
                                                         						  connects to. You should use the default setting.

Caution

Step 8

On the Port Group Basics page, in the Related Links drop-down
                                          			 box, select Add Ports and select Go .

Step 9

On the New Port page, enter the following settings and select Save .

Field

Considerations

Enabled

Check this check box.

Number of Ports

Enter the number of voice messaging ports that you want to
                                                         						  create in this port group.

For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports.

Phone System

Select the name of the
                                                         						  phone system that you entered in Step 3 .

Port Group

Select the name of the
                                                         						  port group that you added in Step 7 .

Step 10

On the Search Ports page, select the display name of the first
                                          			 voice messaging port that you created for this phone system integration.

Step 11

On the Port Basics page, set the voice messaging port settings
                                          			 as applicable. The fields in the following table are the ones that you can
                                          			 change.

Field

Considerations

Enabled

Check this check box to
                                                         						  enable the port. The port is enabled during normal operation.

Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing.

Extension

Enter the extension for
                                                         						  the port as assigned on the phone system.

Answer Calls

Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users.

Perform Message
                                                         						  Notification

Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports.

Send MWI Requests

Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports.

Allow TRAP Connections

Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports.

Outgoing Hunt Order

Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest.

Step 12

Select Save .

Step 13

Select Next .

Step 14

Repeat Step 11 through Step 13 for all
                                          			 remaining voice messaging ports for the phone system.

Step 15

In Cisco Unity Connection Administration, expand Telephony
                                             				Integrations , then select Phone System .

Step 16

On the Search Phone Systems page, under Display Name, select the
                                          			 name of the phone system that you entered in Step 3 .

Step 17

Repeat Step 6 through Step 16 for each
                                          			 remaining TIMG unit integrated with Unity Connection.

Step 18

If another phone system integration exists, in Cisco Unity
                                          			 Connection Administration, expand Telephony
                                             				Integrations , then select Trunk .
                                          			 Otherwise, skip to Step 22 .

Step 19

On the Search Phone System Trunks page, on the Phone System
                                          			 Trunk menu, select New Phone System
                                             				Trunk .

Step 20

On the New Phone System Trunk page, enter the following settings
                                          			 for the phone system trunk and select Save .

Field

Setting

From Phone System

Enter the display name of
                                                         						  the phone system that you are creating a trunk for.

To Phone System

Enter the display name of
                                                         						  the previously existing phone system that the trunk connects to.

Trunk Access Code

Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system.

Step 21

Repeat Step 19 and Step 20 for all
                                          			 remaining phone system trunks that you want to create.

Step 22

In Cisco Unity Connection Administration, expand Telephony
                                             				Integrations , then select Port Group .

Step 23

On the Search Port Groups page, select the display name of the
                                          			 port group that you added in Step 7 .

Step 24

On the Port Group Basics page, select Reset .

Step 25

When prompted that resetting terminates all call traffic, select OK .

Step 26

In the Related Links drop-down list, select Check Telephony
                                             				Configuration and select Go to confirm
                                          			 the phone system integration settings.

If the test is not successful, the Task Execution Results
                                             				displays one or more messages with troubleshooting steps. After correcting the
                                             				problems, test the connection again.

Step 27

In the Task Execution Results window, select Close .

| Caution | T1 (or “wet T1”) connections to the PSTN must be
                                                			 through an MTU, CSU, or other device that provides line isolation. Otherwise,
                                                			 the TIMG units may be damaged |
|---|---|

| Caution | In programming the phone system, do not send calls to voice
                                          		  messaging ports in Unity Connection that cannot answer calls (voice messaging
                                          		  ports that are not set to Answer Calls). For example, if a voice messaging port
                                          		  is set only to Perform Message Notification, do not send calls to it. |
|---|---|

| Step 1 | Create a coverage path which contains the TIMG unit hunt group
                                          			 number as the coverage point. |
|---|---|
| Step 2 | Assign the coverage path that you created in Step 1 to the user stations that must forward to the voice messaging ports on the TIMG
                                          			 units when calls are not answered or when the user station is busy, based on
                                          			 one of the call transfer types shown in Table 3-1 . Table 1. Call Transfer Types Transfer Type Usage Release transfer (blind transfer) Program the user station to forward calls to the pilot number
                                                         						  when: The extension is busy. The call is not answered. Supervised transfer Program the user station to forward calls to the pilot number
                                                         						  only when the call is not answered (on the phone system, the number of rings
                                                         						  before forwarding must be more than the number of rings to supervise the call).
                                                         						  Confirm that call forwarding is disabled when the extension is busy. | Transfer Type | Usage | Release transfer (blind transfer) | Program the user station to forward calls to the pilot number
                                                         						  when: The extension is busy. The call is not answered. | Supervised transfer | Program the user station to forward calls to the pilot number
                                                         						  only when the call is not answered (on the phone system, the number of rings
                                                         						  before forwarding must be more than the number of rings to supervise the call).
                                                         						  Confirm that call forwarding is disabled when the extension is busy. |
| Transfer Type | Usage |
| Release transfer (blind transfer) | Program the user station to forward calls to the pilot number
                                                         						  when: The extension is busy. The call is not answered. |
| Supervised transfer | Program the user station to forward calls to the pilot number
                                                         						  only when the call is not answered (on the phone system, the number of rings
                                                         						  before forwarding must be more than the number of rings to supervise the call).
                                                         						  Confirm that call forwarding is disabled when the extension is busy. |
| Step 3 | Assign an extension number for each voice messaging port, which
                                          			 is a digital line that connects to the TIMG unit, and set the voice messaging
                                          			 port options as shown in Table 3-2 . Note You should
                                                      				distribute the voice messaging ports among multiple phone system line cards so
                                                      				that call processing can continue even if a line card becomes inactive. Table 2. Voice Messaging Port Options for All Lines Option Setting Extension Enter the extension number of the digital line. Type Enter the applicable setting: VMI VMIFD Loss Group Enter 4 . Off Premises Station Enter y . R Balance Network Enter n . Survivable COR Enter internal . Survivable Trunk Dest Enter y . LWC Activation Enter y . LWC Log External Calls Enter n . CDR Privacy Enter n . Redirect Notification Enter y . Per Button Ring Control Enter n . Bridged Call Alerting Enter n . Switch hook Flash Enter y . Ignore Rotary Digits Enter n . H.320 Conversion Enter n . Service Link Mode Enter as-needed . Multimedia Mode Enter basic . Coverage Message
                                                         						  Retrieval Enter y . Auto Answer Enter none . Data Restriction Enter n . Distinctive Audible Alert Enter y . Adjunct Supervision Enter y . Audible Message Waiting Enter n . Coverage After Forwarding Enter s . Multimedia Early Answer Enter n . LWC Appearance Enter call-appr . | Note | You should
                                                      				distribute the voice messaging ports among multiple phone system line cards so
                                                      				that call processing can continue even if a line card becomes inactive. | Option | Setting | Extension | Enter the extension number of the digital line. | Type | Enter the applicable setting: VMI VMIFD | Loss Group | Enter 4 . | Off Premises Station | Enter y . | R Balance Network | Enter n . | Survivable COR | Enter internal . | Survivable Trunk Dest | Enter y . | LWC Activation | Enter y . | LWC Log External Calls | Enter n . | CDR Privacy | Enter n . | Redirect Notification | Enter y . | Per Button Ring Control | Enter n . | Bridged Call Alerting | Enter n . | Switch hook Flash | Enter y . | Ignore Rotary Digits | Enter n . | H.320 Conversion | Enter n . | Service Link Mode | Enter as-needed . | Multimedia Mode | Enter basic . | Coverage Message
                                                         						  Retrieval | Enter y . | Auto Answer | Enter none . | Data Restriction | Enter n . | Distinctive Audible Alert | Enter y . | Adjunct Supervision | Enter y . | Audible Message Waiting | Enter n . | Coverage After Forwarding | Enter s . | Multimedia Early Answer | Enter n . | LWC Appearance | Enter call-appr . |
| Note | You should
                                                      				distribute the voice messaging ports among multiple phone system line cards so
                                                      				that call processing can continue even if a line card becomes inactive. |
| Option | Setting |
| Extension | Enter the extension number of the digital line. |
| Type | Enter the applicable setting: VMI VMIFD |
| Loss Group | Enter 4 . |
| Off Premises Station | Enter y . |
| R Balance Network | Enter n . |
| Survivable COR | Enter internal . |
| Survivable Trunk Dest | Enter y . |
| LWC Activation | Enter y . |
| LWC Log External Calls | Enter n . |
| CDR Privacy | Enter n . |
| Redirect Notification | Enter y . |
| Per Button Ring Control | Enter n . |
| Bridged Call Alerting | Enter n . |
| Switch hook Flash | Enter y . |
| Ignore Rotary Digits | Enter n . |
| H.320 Conversion | Enter n . |
| Service Link Mode | Enter as-needed . |
| Multimedia Mode | Enter basic . |
| Coverage Message
                                                         						  Retrieval | Enter y . |
| Auto Answer | Enter none . |
| Data Restriction | Enter n . |
| Distinctive Audible Alert | Enter y . |
| Adjunct Supervision | Enter y . |
| Audible Message Waiting | Enter n . |
| Coverage After Forwarding | Enter s . |
| Multimedia Early Answer | Enter n . |
| LWC Appearance | Enter call-appr . |
| Step 4 | Set the DS1 Circuit Pack options as shown in Table 3-3 . Table 3. DS1 Circuit Pack Options Option Setting Line Compensation Enter 1 . Signaling Mode Enter robbed-bit . Line Coding Enter b8zs . Framing Mode Enter esf . Interface Companding Enter mulaw . Idle Code Enter 11111111 . Slip Detection Enter n . Echo Cancellation Enter n . Near-end CSU Type Enter other . | Option | Setting | Line Compensation | Enter 1 . | Signaling Mode | Enter robbed-bit . | Line Coding | Enter b8zs . | Framing Mode | Enter esf . | Interface Companding | Enter mulaw . | Idle Code | Enter 11111111 . | Slip Detection | Enter n . | Echo Cancellation | Enter n . | Near-end CSU Type | Enter other . |
| Option | Setting |
| Line Compensation | Enter 1 . |
| Signaling Mode | Enter robbed-bit . |
| Line Coding | Enter b8zs . |
| Framing Mode | Enter esf . |
| Interface Companding | Enter mulaw . |
| Idle Code | Enter 11111111 . |
| Slip Detection | Enter n . |
| Echo Cancellation | Enter n . |
| Near-end CSU Type | Enter other . |
| Step 5 | Assign a the voice messaging ports to a hunt group by setting
                                          			 the options shown in Table 3-4 . Table 4. Hunt Group Options Option Setting LWC Reception Enter none . Message Center Enter none . Group Number Enter the hunt group
                                                         						  number. Group Extension Enter the pilot number
                                                         						  for the hunt group. Group Type Enter ucd-mia . Group Name Enter the display name
                                                         						  for the hunt group. Queue? Enter n . | Option | Setting | LWC Reception | Enter none . | Message Center | Enter none . | Group Number | Enter the hunt group
                                                         						  number. | Group Extension | Enter the pilot number
                                                         						  for the hunt group. | Group Type | Enter ucd-mia . | Group Name | Enter the display name
                                                         						  for the hunt group. | Queue? | Enter n . |
| Option | Setting |
| LWC Reception | Enter none . |
| Message Center | Enter none . |
| Group Number | Enter the hunt group
                                                         						  number. |
| Group Extension | Enter the pilot number
                                                         						  for the hunt group. |
| Group Type | Enter ucd-mia . |
| Group Name | Enter the display name
                                                         						  for the hunt group. |
| Queue? | Enter n . |
| Step 6 | Enter the group member assignments for the voice messaging ports
                                          			 that answer calls and press Enter . If you
                                          			 plan to set the voice messaging ports to either answer calls or to dial out
                                          			 (for example, to set MWIs), make sure that you include in the hunt group only
                                          			 the voice messaging ports are set to answer calls. For
                                          			 smaller systems, include in the hunt group all voice messaging ports when the
                                          			 ports are set to both answer calls and dial out (for example, to set MWIs). |

| Transfer Type | Usage |
|---|---|
| Release transfer (blind transfer) | Program the user station to forward calls to the pilot number
                                                         						  when: The extension is busy. The call is not answered. |
| Supervised transfer | Program the user station to forward calls to the pilot number
                                                         						  only when the call is not answered (on the phone system, the number of rings
                                                         						  before forwarding must be more than the number of rings to supervise the call).
                                                         						  Confirm that call forwarding is disabled when the extension is busy. |

| Note | You should
                                                      				distribute the voice messaging ports among multiple phone system line cards so
                                                      				that call processing can continue even if a line card becomes inactive. |
|---|---|

| Option | Setting |
|---|---|
| Extension | Enter the extension number of the digital line. |
| Type | Enter the applicable setting: VMI VMIFD |
| Loss Group | Enter 4 . |
| Off Premises Station | Enter y . |
| R Balance Network | Enter n . |
| Survivable COR | Enter internal . |
| Survivable Trunk Dest | Enter y . |
| LWC Activation | Enter y . |
| LWC Log External Calls | Enter n . |
| CDR Privacy | Enter n . |
| Redirect Notification | Enter y . |
| Per Button Ring Control | Enter n . |
| Bridged Call Alerting | Enter n . |
| Switch hook Flash | Enter y . |
| Ignore Rotary Digits | Enter n . |
| H.320 Conversion | Enter n . |
| Service Link Mode | Enter as-needed . |
| Multimedia Mode | Enter basic . |
| Coverage Message
                                                         						  Retrieval | Enter y . |
| Auto Answer | Enter none . |
| Data Restriction | Enter n . |
| Distinctive Audible Alert | Enter y . |
| Adjunct Supervision | Enter y . |
| Audible Message Waiting | Enter n . |
| Coverage After Forwarding | Enter s . |
| Multimedia Early Answer | Enter n . |
| LWC Appearance | Enter call-appr . |

| Option | Setting |
|---|---|
| Line Compensation | Enter 1 . |
| Signaling Mode | Enter robbed-bit . |
| Line Coding | Enter b8zs . |
| Framing Mode | Enter esf . |
| Interface Companding | Enter mulaw . |
| Idle Code | Enter 11111111 . |
| Slip Detection | Enter n . |
| Echo Cancellation | Enter n . |
| Near-end CSU Type | Enter other . |

| Option | Setting |
|---|---|
| LWC Reception | Enter none . |
| Message Center | Enter none . |
| Group Number | Enter the hunt group
                                                         						  number. |
| Group Extension | Enter the pilot number
                                                         						  for the hunt group. |
| Group Type | Enter ucd-mia . |
| Group Name | Enter the display name
                                                         						  for the hunt group. |
| Queue? | Enter n . |

| Caution | Because TIMG units have the same default IP address, you must set them up one
                                             		  at a time. Otherwise, you can experience IP address conflicts. |
|---|---|

| Step 1 | On a Windows workstation that have access to the TIMG units, go
                                             			 to the following link: http://software.cisco.com/download/navigator.html?mdfid=280082558&i=rm . Note To access the software download page, you must be signed in to
                                                         				Cisco.com as a registered user. This
                                                            				  procedure describes the steps when using Internet Explorer as your web browser.
                                                            				  If you are using a different web browser, the steps may differ. | Note | To access the software download page, you must be signed in to
                                                         				Cisco.com as a registered user. This
                                                            				  procedure describes the steps when using Internet Explorer as your web browser.
                                                            				  If you are using a different web browser, the steps may differ. |
|---|---|---|---|
| Note | To access the software download page, you must be signed in to
                                                         				Cisco.com as a registered user. This
                                                            				  procedure describes the steps when using Internet Explorer as your web browser.
                                                            				  If you are using a different web browser, the steps may differ. |
| Step 2 | In the tree control on the Downloads Home page, expand Unified
                                             			 Communications> Unified Communications Applications > Messaging >
                                             			 Cisco Unity and select Cisco Unity Telephony Integration. |
| Step 3 | On the Log In page, enter your username and password, then
                                             			 select Log In . |
| Step 4 | On the Select a Release page, under Latest Releases, select the
                                             			 most recent release. |
| Step 5 | In the right column, select the version of the firmware for your
                                             			 TIMG units. |
| Step 6 | On the Download Image page, select Download . |
| Step 7 | On the Supporting Document(s) page, select Agree . |
| Step 8 | In the File Download dialog box, select Save . |
| Step 9 | In the Save As dialog box, browse to the Windows workstation
                                             			 that have access the TIMG units, browse to a directory where you want to save
                                             			 the file, and select Save . |
| Step 10 | In the Download Complete dialog box, select Open . The window for extracting the TIMG firmware
                                             			 update files appears. |
| Step 11 | Select Extract . |
| Step 12 | In the Extract dialog box, browse to the directory where you
                                             			 want the extracted files, and select Extract . |
| Step 13 | Close the window for the extracting application. |

| Note | To access the software download page, you must be signed in to
                                                         				Cisco.com as a registered user. This
                                                            				  procedure describes the steps when using Internet Explorer as your web browser.
                                                            				  If you are using a different web browser, the steps may differ. |
|---|---|

| Step 1 | On the Windows workstation, add a temporary route to enable
                                             			 access to the TIMG units. On the Windows Start menu, select Run . Enter cmd , and press Enter . The Command Prompt window appears. At the command prompt, enter route add 10.12.13.74 <IP Address of Workstation> , and
                                                   				  press Enter . For example, if the IP address of the workstation is 198.1.3.25,
                                                      					 enter “route add 10.12.13.74<space>198.1.3.25” in the Command Prompt
                                                      					 window. Close the Command Prompt window. |
|---|---|
| Step 2 | Connect a TIMG unit to the network. |
| Step 3 | In the web browser, go to http://10.12.13.74 . |
| Step 4 | To sign in, enter the following case-sensitive settings. Table 5. Sign-in Settings Field Setting Username Enter admin . Password Enter IpodAdmin . | Field | Setting | Username | Enter admin . | Password | Enter IpodAdmin . |
| Field | Setting |
| Username | Enter admin . |
| Password | Enter IpodAdmin . |
| Step 5 | Select OK . |
| Step 6 | On the System menu, select Upgrade . |
| Step 7 | On the Upgrade page, under Browse for Upgrade File, select Browse . |
| Step 8 | In the Choose File dialog box, browse to the directory on the
                                             			 Windows workstation that has the extracted TIMG firmware update files. |
| Step 9 | Select T1E1_<xx > .app (where <xx> is multiple
                                             			 digits), and select Open . |
| Step 10 | On the Upgrade page, select Install File . |
| Step 11 | After the file is installed, a message prompting you to restart
                                             			 the TIMG unit appears. Select Cancel . Caution Do not restart the TIMG unit until you are instructed to do so
                                                         				later in this procedure, even if the file installation fails. Restarting the
                                                         				TIMG unit at this step may prevent the TIMG unit from functioning correctly. | Caution | Do not restart the TIMG unit until you are instructed to do so
                                                         				later in this procedure, even if the file installation fails. Restarting the
                                                         				TIMG unit at this step may prevent the TIMG unit from functioning correctly. |
| Caution | Do not restart the TIMG unit until you are instructed to do so
                                                         				later in this procedure, even if the file installation fails. Restarting the
                                                         				TIMG unit at this step may prevent the TIMG unit from functioning correctly. |
| Step 12 | Repeat Step 6 through Step 11 for the following files: T1E1_<xx>.fsh T1E1_<xx>.msd |
| Step 13 | On the Configuration menu, select Import/Export . |
| Step 14 | On the Import/Export page, select Browse . |
| Step 15 | In the Choose File dialog box, browse to the file
                                             			 T1_LS_Cfg_LucentG3.ini. |
| Step 16 | Select T1_LS_Cfg_LucentG3.ini , and select Open . |
| Step 17 | On the Import/Export page, select Import File . |
| Step 18 | After the file is imported, a message prompting you to restart
                                             			 the TIMG unit appears. Select OK . |
| Step 19 | In the web browser, go to http://10.12.13.74 . |
| Step 20 | To sign in, enter the following case-sensitive settings. Table 6. Sign-in Settings Field Setting Username Enter admin . Password Enter IpodAdmin . | Field | Setting | Username | Enter admin . | Password | Enter IpodAdmin . |
| Field | Setting |
| Username | Enter admin . |
| Password | Enter IpodAdmin . |
| Step 21 | Select OK . |
| Step 22 | On the System menu, select Password . |
| Step 23 | On the Change Password page, enter the following settings. Table 7. Change Password Page Settings Field Setting Old Password Enter IpodAdmin . (This
                                                            						  setting is case sensitive.) New Password Enter your new password.
                                                            						  (This setting is case sensitive.) Confirm Password Enter your new password.
                                                            						  (This setting is case sensitive.) | Field | Setting | Old Password | Enter IpodAdmin . (This
                                                            						  setting is case sensitive.) | New Password | Enter your new password.
                                                            						  (This setting is case sensitive.) | Confirm Password | Enter your new password.
                                                            						  (This setting is case sensitive.) |
| Field | Setting |
| Old Password | Enter IpodAdmin . (This
                                                            						  setting is case sensitive.) |
| New Password | Enter your new password.
                                                            						  (This setting is case sensitive.) |
| Confirm Password | Enter your new password.
                                                            						  (This setting is case sensitive.) |
| Step 24 | Select Change . |
| Step 25 | On the Configuration menu, select Mgmt
                                                				Protocols . |
| Step 26 | On the Management Protocols page, enter the following settings. Table 8. Management Protocols Page Settings Field Settings E-mail Alarms Enabled Select No . SNMP Traps Enabled Select No . HTTP Server Enabled Select Yes . HTTPs Server Enabled Select No . | Field | Settings | E-mail Alarms Enabled | Select No . | SNMP Traps Enabled | Select No . | HTTP Server Enabled | Select Yes . | HTTPs Server Enabled | Select No . |
| Field | Settings |
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |
| HTTP Server Enabled | Select Yes . |
| HTTPs Server Enabled | Select No . |
| Step 27 | Select Submit . |
| Step 28 | On the Configuration menu, select Routing
                                                				Table . |
| Step 29 | On the Routing Table page, under Router Configuration, select VoIP Host
                                                				Groups . |
| Step 30 | Under VoIP Host Groups, enter the following settings for the
                                             			 first VoIP Host Group. Table 9. First VoIP Host Group Settings Field Settings Name Accept the default or
                                                            						  enter another descriptive name of the VoIP host group. Load-Balanced (Unity Connection without
                                                               							 a cluster) Select False . (Unity Connection with a
                                                               							 cluster configured) Select False . Fault-Tolerant (Unity Connection without
                                                               							 a cluster) Select False . (Unity Connection with a
                                                               							 cluster configured) Select True . | Field | Settings | Name | Accept the default or
                                                            						  enter another descriptive name of the VoIP host group. | Load-Balanced | (Unity Connection without
                                                               							 a cluster) Select False . (Unity Connection with a
                                                               							 cluster configured) Select False . | Fault-Tolerant | (Unity Connection without
                                                               							 a cluster) Select False . (Unity Connection with a
                                                               							 cluster configured) Select True . |
| Field | Settings |
| Name | Accept the default or
                                                            						  enter another descriptive name of the VoIP host group. |
| Load-Balanced | (Unity Connection without
                                                               							 a cluster) Select False . (Unity Connection with a
                                                               							 cluster configured) Select False . |
| Fault-Tolerant | (Unity Connection without
                                                               							 a cluster) Select False . (Unity Connection with a
                                                               							 cluster configured) Select True . |
| Step 31 | For Unity Connection without a cluster, under Host List, enter
                                             			 the host name or IP address of the Unity Connection server and the server port
                                             			 in the format <host name or IP address>:5060. For Unity Connection with a cluster configured, under Host List,
                                                				enter the host name or IP address of the subscriber server (the second Unity
                                                				Connection server that you installed) and the server port in the format
                                                				<host name or IP address>:5060. |
| Step 32 | For Unity Connection without a cluster, continue to Step 34 .
                                             			 For Unity Connection with a cluster configured, select Add Host . |
| Step 33 | In the second field, enter the host name or IP address of the
                                             			 publisher server (the first Unity Connection server that you installed) and the
                                             			 server port in the format <host name or IP address>:5060. Note Do not
                                                         				add a third host under Host List or a second host group under VoIP Host Groups.
                                                         				Otherwise, the Unity Connection cluster may not function correctly. | Note | Do not
                                                         				add a third host under Host List or a second host group under VoIP Host Groups.
                                                         				Otherwise, the Unity Connection cluster may not function correctly. |
| Note | Do not
                                                         				add a third host under Host List or a second host group under VoIP Host Groups.
                                                         				Otherwise, the Unity Connection cluster may not function correctly. |
| Step 34 | Select Submit . |
| Step 35 | On the Configuration menu, select TDM > T1/E1 . |
| Step 36 | On the T1/E1 Configuration page, enter the following settings. Table 10. T1/E1 Configuration Page Settings Field Settings Line Settings Line Mode Select T1 . Signaling Mode Select CAS . Interface Mode Select Terminal . T1 Line Line Encoding Select B8ZS . Framing Select EFS . Selects Transmit Pulse
                                                            						  Waveform Select Short_Haul_110ft . T1 CAS Protocol T1 CAS Protocol Select Loop_Start . Flash Hook Enter 550 . Consult Call Dialtone
                                                            						  Drop Code Enter !! . Consult Call Proceeding
                                                            						  Drop Code Enter !! . Consult Call Busy Drop
                                                            						  Code Enter ! . Consult Call Error Drop
                                                            						  Code Enter !! . Consult Call Connected
                                                            						  Drop Code Enter ,,,, . Consult Call Disconnected
                                                            						  Drop Code Enter ! . MWI confirmation Tone Select No . CPID Type Select TypeII_CPID . Initial Wait for Inband
                                                            						  CPID Enter 5000 . Inband CPID Complete
                                                            						  Timeout Enter 500 . Failover Settings Enable Failover Select No . | Field | Settings | Line Settings | Line Mode | Select T1 . | Signaling Mode | Select CAS . | Interface Mode | Select Terminal . | T1 Line | Line Encoding | Select B8ZS . | Framing | Select EFS . | Selects Transmit Pulse
                                                            						  Waveform | Select Short_Haul_110ft . | T1 CAS Protocol | T1 CAS Protocol | Select Loop_Start . | Flash Hook | Enter 550 . | Consult Call Dialtone
                                                            						  Drop Code | Enter !! . | Consult Call Proceeding
                                                            						  Drop Code | Enter !! . | Consult Call Busy Drop
                                                            						  Code | Enter ! . | Consult Call Error Drop
                                                            						  Code | Enter !! . | Consult Call Connected
                                                            						  Drop Code | Enter ,,,, . | Consult Call Disconnected
                                                            						  Drop Code | Enter ! . | MWI confirmation Tone | Select No . | CPID Type | Select TypeII_CPID . | Initial Wait for Inband
                                                            						  CPID | Enter 5000 . | Inband CPID Complete
                                                            						  Timeout | Enter 500 . | Failover Settings | Enable Failover | Select No . |
| Field | Settings |
| Line Settings |
| Line Mode | Select T1 . |
| Signaling Mode | Select CAS . |
| Interface Mode | Select Terminal . |
| T1 Line |
| Line Encoding | Select B8ZS . |
| Framing | Select EFS . |
| Selects Transmit Pulse
                                                            						  Waveform | Select Short_Haul_110ft . |
| T1 CAS Protocol |
| T1 CAS Protocol | Select Loop_Start . |
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
| Failover Settings |
| Enable Failover | Select No . |
| Step 37 | Select Submit . |
| Step 38 | On the Configuration menu, select TDM > General . |
| Step 39 | On the TDM General Settings page, enter the following settings. Table 11. TDM General Settings Page Settings Field Settings PCM Coding Select uLaw . Minimum Call Party Delay
                                                            						  (ms) Enter 500 . Maximum Call Party Delay
                                                            						  (ms) Enter 2000 . Dial Digit on Time (ms) Enter 100 . Dial Inter-Digit Time
                                                            						  (ms) Enter 100 . Dial Pause Time (ms) Enter 2000 . Turn MWI On FAC Enter the code that the
                                                            						  phone system uses to turn MWIs on. Turn MWI Off FAC Enter the code that the
                                                            						  phone system uses to turn MWIs off. Outbound Call Connect
                                                            						  Timeout (ms) Enter 10000 . Wait for Ringback/Connect
                                                            						  on Blind Transfer Select Yes . Hunt Group Extension Enter the pilot number of
                                                            						  the Unity Connection voice messaging ports. | Field | Settings | PCM Coding | Select uLaw . | Minimum Call Party Delay
                                                            						  (ms) | Enter 500 . | Maximum Call Party Delay
                                                            						  (ms) | Enter 2000 . | Dial Digit on Time (ms) | Enter 100 . | Dial Inter-Digit Time
                                                            						  (ms) | Enter 100 . | Dial Pause Time (ms) | Enter 2000 . | Turn MWI On FAC | Enter the code that the
                                                            						  phone system uses to turn MWIs on. | Turn MWI Off FAC | Enter the code that the
                                                            						  phone system uses to turn MWIs off. | Outbound Call Connect
                                                            						  Timeout (ms) | Enter 10000 . | Wait for Ringback/Connect
                                                            						  on Blind Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number of
                                                            						  the Unity Connection voice messaging ports. |
| Field | Settings |
| PCM Coding | Select uLaw . |
| Minimum Call Party Delay
                                                            						  (ms) | Enter 500 . |
| Maximum Call Party Delay
                                                            						  (ms) | Enter 2000 . |
| Dial Digit on Time (ms) | Enter 100 . |
| Dial Inter-Digit Time
                                                            						  (ms) | Enter 100 . |
| Dial Pause Time (ms) | Enter 2000 . |
| Turn MWI On FAC | Enter the code that the
                                                            						  phone system uses to turn MWIs on. |
| Turn MWI Off FAC | Enter the code that the
                                                            						  phone system uses to turn MWIs off. |
| Outbound Call Connect
                                                            						  Timeout (ms) | Enter 10000 . |
| Wait for Ringback/Connect
                                                            						  on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of
                                                            						  the Unity Connection voice messaging ports. |
| Step 40 | Select Submit . |
| Step 41 | On the Configuration menu, select TDM > Port
                                                   				  Enable . |
| Step 42 | On the TDM Port Enabling page, select No for the
                                             			 ports that you want to disable on the TIMG unit. |
| Step 43 | Confirm that Yes is
                                             			 selected for all other ports on the TIMG unit. |
| Step 44 | Select Submit . |
| Step 45 | On the Configuration menu, select VoIP > General . |
| Step 46 | On the VoIP General Settings page, enter the following settings. Table 12. VoIP General Settings Page Settings Field Setting User-Agent Host and Domain Name Enter the domain name of
                                                            						  the TIMG unit. Transport Type Select UDP . Call as Domain Name Select No . SIPS URI Scheme Enabled Select No . Invite Expiration (sec) Enter 120 . Server DNS Server Address Enter the IP Address of
                                                            						  the Domain Name Server that the TIMG unit uses. Registration Server
                                                            						  Address Leave this field blank. Registration Server Port Enter 5060 . Registration Expiration
                                                            						  (sec) Enter 3600 . TCP/UDP UDP/TCP Transports
                                                            						  Enabled Select Yes . TCP/UDP Server Port Enter 5060 . Proxy Primary Proxy Server
                                                            						  Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the
                                                            						  default setting. Backup Proxy Server
                                                            						  Address Not applicable. Leave the
                                                            						  default setting. Backup Proxy Server Port Not applicable. Leave the
                                                            						  default setting. Proxy Query Interval Enter 10 . Timing T1 Time Enter 500 . T2 Time Enter 4000 . T4 Time Enter 5000 . Monitoring Monitor Call Connections Select No . | Field | Setting | User-Agent | Host and Domain Name | Enter the domain name of
                                                            						  the TIMG unit. | Transport Type | Select UDP . | Call as Domain Name | Select No . | SIPS URI Scheme Enabled | Select No . | Invite Expiration (sec) | Enter 120 . | Server | DNS Server Address | Enter the IP Address of
                                                            						  the Domain Name Server that the TIMG unit uses. | Registration Server
                                                            						  Address | Leave this field blank. | Registration Server Port | Enter 5060 . | Registration Expiration
                                                            						  (sec) | Enter 3600 . | TCP/UDP | UDP/TCP Transports
                                                            						  Enabled | Select Yes . | TCP/UDP Server Port | Enter 5060 . | Proxy | Primary Proxy Server
                                                            						  Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the
                                                            						  default setting. | Backup Proxy Server
                                                            						  Address | Not applicable. Leave the
                                                            						  default setting. | Backup Proxy Server Port | Not applicable. Leave the
                                                            						  default setting. | Proxy Query Interval | Enter 10 . | Timing | T1 Time | Enter 500 . | T2 Time | Enter 4000 . | T4 Time | Enter 5000 . | Monitoring | Monitor Call Connections | Select No . |
| Field | Setting |
| User-Agent |
| Host and Domain Name | Enter the domain name of
                                                            						  the TIMG unit. |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| SIPS URI Scheme Enabled | Select No . |
| Invite Expiration (sec) | Enter 120 . |
| Server |
| DNS Server Address | Enter the IP Address of
                                                            						  the Domain Name Server that the TIMG unit uses. |
| Registration Server
                                                            						  Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration
                                                            						  (sec) | Enter 3600 . |
| TCP/UDP |
| UDP/TCP Transports
                                                            						  Enabled | Select Yes . |
| TCP/UDP Server Port | Enter 5060 . |
| Proxy |
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
| Timing |
| T1 Time | Enter 500 . |
| T2 Time | Enter 4000 . |
| T4 Time | Enter 5000 . |
| Monitoring |
| Monitor Call Connections | Select No . |
| Step 47 | Select Submit . |
| Step 48 | On the Configuration menu, select VoIP > Media . |
| Step 49 | On the VoIP Media Settings page, enter the following settings. Table 13. VoIP Media Settings Page Settings Field Settings Audio Audio Compression Select the preferred
                                                            						  codec for audio compression: G.711u —The TIMG unit
                                                                  								uses only the G.711 mu-law codec. G.729AB —The TIMG unit
                                                                  								prefers the G.729 codec but can also use the G.711 mu-law codec. RTP Digit Relay Mode Select RFC2833 . Signaling Digit Relay
                                                            						  Mode Select Off . Voice Activity Detection Select On . Frame Size Select the applicable
                                                            						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                           								correct setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable
                                                            						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                           								correct setting results in recorded messages containing nothing but silence. | Field | Settings | Audio | Audio Compression | Select the preferred
                                                            						  codec for audio compression: G.711u —The TIMG unit
                                                                  								uses only the G.711 mu-law codec. G.729AB —The TIMG unit
                                                                  								prefers the G.729 codec but can also use the G.711 mu-law codec. | RTP Digit Relay Mode | Select RFC2833 . | Signaling Digit Relay
                                                            						  Mode | Select Off . | Voice Activity Detection | Select On . | Frame Size | Select the applicable
                                                            						  setting: G.711— 20 G.729AB— 10 Caution Failure to use the
                                                                           								correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                           								correct setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable
                                                            						  setting: G.711— 1 G.729AB— 2 Caution Failure to use the
                                                                           								correct setting results in recorded messages containing nothing but silence. | Caution | Failure to use the
                                                                           								correct setting results in recorded messages containing nothing but silence. |
| Field | Settings |
| Audio |
| Audio Compression | Select the preferred
                                                            						  codec for audio compression: G.711u —The TIMG unit
                                                                  								uses only the G.711 mu-law codec. G.729AB —The TIMG unit
                                                                  								prefers the G.729 codec but can also use the G.711 mu-law codec. |
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
| Step 50 | Select Submit . |
| Step 51 | On the Configuration menu, select VoIP > QOS . |
| Step 52 | On the VoIP QOS Configuration page, enter the following
                                             			 settings. Table 14. VoIP QOS Configurative Page Settings Field Settings Call Control QOS Byte Enter 104 (equivalent to
                                                            						  DSCP AF31). RTP QOS Byte Enter 184 (equivalent to
                                                            						  DSCP EF). | Field | Settings | Call Control QOS Byte | Enter 104 (equivalent to
                                                            						  DSCP AF31). | RTP QOS Byte | Enter 184 (equivalent to
                                                            						  DSCP EF). |
| Field | Settings |
| Call Control QOS Byte | Enter 104 (equivalent to
                                                            						  DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to
                                                            						  DSCP EF). |
| Step 53 | Select Submit . |
| Step 54 | On the Configuration menu, select IP . |
| Step 55 | On the IP Settings, LAN1 page, enter the following settings. Table 15. IP Settings, LAN1 Page Settings Field Settings Client IP Address Enter the new IP address
                                                            						  that you want to use for the TIMG unit. (This is the IP address
                                                            						  that you enter in Cisco Unity Connection Administration when you create the
                                                            						  integration.) Client Subnet Mask Enter the new subnet
                                                            						  mask, if the subnet mask is different from the default IP address. Default Network Gateway
                                                            						  Address Enter the IP address of
                                                            						  the default network gateway router that the TIMG units use. BOOTP Enabled If you are using DHCP,
                                                            						  select Yes . If you are not using
                                                            						  DHCP, select No . | Field | Settings | Client IP Address | Enter the new IP address
                                                            						  that you want to use for the TIMG unit. (This is the IP address
                                                            						  that you enter in Cisco Unity Connection Administration when you create the
                                                            						  integration.) | Client Subnet Mask | Enter the new subnet
                                                            						  mask, if the subnet mask is different from the default IP address. | Default Network Gateway
                                                            						  Address | Enter the IP address of
                                                            						  the default network gateway router that the TIMG units use. | BOOTP Enabled | If you are using DHCP,
                                                            						  select Yes . If you are not using
                                                            						  DHCP, select No . |
| Field | Settings |
| Client IP Address | Enter the new IP address
                                                            						  that you want to use for the TIMG unit. (This is the IP address
                                                            						  that you enter in Cisco Unity Connection Administration when you create the
                                                            						  integration.) |
| Client Subnet Mask | Enter the new subnet
                                                            						  mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway
                                                            						  Address | Enter the IP address of
                                                            						  the default network gateway router that the TIMG units use. |
| BOOTP Enabled | If you are using DHCP,
                                                            						  select Yes . If you are not using
                                                            						  DHCP, select No . |
| Step 56 | Select Submit . |
| Step 57 | On the Configuration menu, select Tone
                                                				Detection . |
| Step 58 | On the Tone Detection page, under Call Progress Tone - Learn, in
                                             			 the Learn Tone Event field, select Busy and do
                                             			 the following substeps to verify that the tone is correct. From a available phone, call a second phone. Answer the second phone when it rings, and leave both handsets
                                                   				  off so that both phones are busy. From a third phone, dial one of the busy phones. Confirm that you hear a busy tone. Hang up the third phone but leave the handsets for the other two
                                                   				  phones off. |
| Step 59 | Under Call Progress Tone - Learn, in the Dial String field,
                                             			 enter the extension that you dialed in Step 58c from the third phone. |
| Step 60 | Select Learn . |
| Step 61 | On the Tone Detection page, under Call Progress Tone - Learn, in
                                             			 the Learn field, select Error and do
                                             			 the following substeps to verify that the tone is correct. From an available phone, dial an extension that does not exist. Confirm that you hear the reorder or error tone. Hang up the phone. |
| Step 62 | Under Call Progress Tone - Learn, in the Dial String field,
                                             			 enter the extension that you dialed in Step 61a |
| Step 63 | Select Learn . |
| Step 64 | On the Tone Detection page, under Call Progress Tone - Learn, in
                                             			 the Learn field, select Ringback and
                                             			 do the following substeps to verify that the tone is correct. From an available phone, dial an extension that does exist. Confirm that you hear the ringback tone. Hang up the phone. |
| Step 65 | Under Call Progress Tone - Learn, in the Dial String field,
                                             			 enter the extension that you dialed in Step 64a |
| Step 66 | Select Learn . |
| Step 67 | Select Submit . |
| Step 68 | Hang up the phones that you used in Step 58 . |
| Step 69 | On the Configuration menu, select Import/Export . |
| Step 70 | On the Import/Export page, under Export Files, select Export All
                                                				Settings . |
| Step 71 | In the File Download dialog box, select Save . |
| Step 72 | In the Save As dialog box, browse to the Windows workstation
                                             			 that has access to the TIMG units, browse to a directory where you want to save
                                             			 the file, and select Save . |
| Step 73 | In the Download Complete dialog box, select Open . Notepad
                                             			 opens the file Config.ini that you saved. |
| Step 74 | Locate the line with the following parameter: telautoanswer |
| Step 75 | Confirm that the value of the parameter is no so that
                                             			 the line reads as follows: telautoanswer = no |
| Step 76 | Locate the line with the following parameter: telFacCDropProc |
| Step 77 | Confirm that the value of the parameter is !! so that the line reads as follows: telFacCDropProc = !! Caution The telFacCDropProc parameter must be set to !!. If the
                                                         				telFacCDropProc parameter is set to 1, supervised transfers fail, and the
                                                         				caller hears the called party standard greeting two times. | Caution | The telFacCDropProc parameter must be set to !!. If the
                                                         				telFacCDropProc parameter is set to 1, supervised transfers fail, and the
                                                         				caller hears the called party standard greeting two times. |
| Caution | The telFacCDropProc parameter must be set to !!. If the
                                                         				telFacCDropProc parameter is set to 1, supervised transfers fail, and the
                                                         				caller hears the called party standard greeting two times. |
| Step 78 | Save the file, and exit Notepad. |
| Step 79 | On the Configuration menu of the TIMG unit, select Import/Export . |
| Step 80 | On the Import/Export page, under Browse for Import File, select Browse . |
| Step 81 | In the Choose File dialog box, browse to the file Config.ini
                                             			 that you saved. |
| Step 82 | Select Config.ini ,
                                             			 and select Open . |
| Step 83 | On the Import/Export page, select Import File . |
| Step 84 | When prompted to restart the TIMG unit, select OK . |
| Step 85 | Repeat Step 2 through Step 84 on all remaining TIMG units. |

| Field | Setting |
|---|---|
| Username | Enter admin . |
| Password | Enter IpodAdmin . |

| Caution | Do not restart the TIMG unit until you are instructed to do so
                                                         				later in this procedure, even if the file installation fails. Restarting the
                                                         				TIMG unit at this step may prevent the TIMG unit from functioning correctly. |
|---|---|

| Field | Setting |
|---|---|
| Username | Enter admin . |
| Password | Enter IpodAdmin . |

| Field | Setting |
|---|---|
| Old Password | Enter IpodAdmin . (This
                                                            						  setting is case sensitive.) |
| New Password | Enter your new password.
                                                            						  (This setting is case sensitive.) |
| Confirm Password | Enter your new password.
                                                            						  (This setting is case sensitive.) |

| Field | Settings |
|---|---|
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |
| HTTP Server Enabled | Select Yes . |
| HTTPs Server Enabled | Select No . |

| Field | Settings |
|---|---|
| Name | Accept the default or
                                                            						  enter another descriptive name of the VoIP host group. |
| Load-Balanced | (Unity Connection without
                                                               							 a cluster) Select False . (Unity Connection with a
                                                               							 cluster configured) Select False . |
| Fault-Tolerant | (Unity Connection without
                                                               							 a cluster) Select False . (Unity Connection with a
                                                               							 cluster configured) Select True . |

| Note | Do not
                                                         				add a third host under Host List or a second host group under VoIP Host Groups.
                                                         				Otherwise, the Unity Connection cluster may not function correctly. |
|---|---|

| Field | Settings |
|---|---|
| Line Settings |
| Line Mode | Select T1 . |
| Signaling Mode | Select CAS . |
| Interface Mode | Select Terminal . |
| T1 Line |
| Line Encoding | Select B8ZS . |
| Framing | Select EFS . |
| Selects Transmit Pulse
                                                            						  Waveform | Select Short_Haul_110ft . |
| T1 CAS Protocol |
| T1 CAS Protocol | Select Loop_Start . |
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
| Failover Settings |
| Enable Failover | Select No . |

| Field | Settings |
|---|---|
| PCM Coding | Select uLaw . |
| Minimum Call Party Delay
                                                            						  (ms) | Enter 500 . |
| Maximum Call Party Delay
                                                            						  (ms) | Enter 2000 . |
| Dial Digit on Time (ms) | Enter 100 . |
| Dial Inter-Digit Time
                                                            						  (ms) | Enter 100 . |
| Dial Pause Time (ms) | Enter 2000 . |
| Turn MWI On FAC | Enter the code that the
                                                            						  phone system uses to turn MWIs on. |
| Turn MWI Off FAC | Enter the code that the
                                                            						  phone system uses to turn MWIs off. |
| Outbound Call Connect
                                                            						  Timeout (ms) | Enter 10000 . |
| Wait for Ringback/Connect
                                                            						  on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of
                                                            						  the Unity Connection voice messaging ports. |

| Field | Setting |
|---|---|
| User-Agent |
| Host and Domain Name | Enter the domain name of
                                                            						  the TIMG unit. |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| SIPS URI Scheme Enabled | Select No . |
| Invite Expiration (sec) | Enter 120 . |
| Server |
| DNS Server Address | Enter the IP Address of
                                                            						  the Domain Name Server that the TIMG unit uses. |
| Registration Server
                                                            						  Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration
                                                            						  (sec) | Enter 3600 . |
| TCP/UDP |
| UDP/TCP Transports
                                                            						  Enabled | Select Yes . |
| TCP/UDP Server Port | Enter 5060 . |
| Proxy |
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
| Timing |
| T1 Time | Enter 500 . |
| T2 Time | Enter 4000 . |
| T4 Time | Enter 5000 . |
| Monitoring |
| Monitor Call Connections | Select No . |

| Field | Settings |
|---|---|
| Audio |
| Audio Compression | Select the preferred
                                                            						  codec for audio compression: G.711u —The TIMG unit
                                                                  								uses only the G.711 mu-law codec. G.729AB —The TIMG unit
                                                                  								prefers the G.729 codec but can also use the G.711 mu-law codec. |
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

| Caution | Failure to use the
                                                                           								correct setting results in recorded messages containing nothing but silence. |
|---|---|

| Caution | Failure to use the
                                                                           								correct setting results in recorded messages containing nothing but silence. |
|---|---|

| Field | Settings |
|---|---|
| Call Control QOS Byte | Enter 104 (equivalent to
                                                            						  DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to
                                                            						  DSCP EF). |

| Field | Settings |
|---|---|
| Client IP Address | Enter the new IP address
                                                            						  that you want to use for the TIMG unit. (This is the IP address
                                                            						  that you enter in Cisco Unity Connection Administration when you create the
                                                            						  integration.) |
| Client Subnet Mask | Enter the new subnet
                                                            						  mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway
                                                            						  Address | Enter the IP address of
                                                            						  the default network gateway router that the TIMG units use. |
| BOOTP Enabled | If you are using DHCP,
                                                            						  select Yes . If you are not using
                                                            						  DHCP, select No . |

| Caution | The telFacCDropProc parameter must be set to !!. If the
                                                         				telFacCDropProc parameter is set to 1, supervised transfers fail, and the
                                                         				caller hears the called party standard greeting two times. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System . |
|---|---|
| Step 2 | On the Search Phone Systems page, under Display Name, select the
                                          			 name of the default phone system. |
| Step 3 | On the Phone System Basics page, in the Phone System Name field,
                                          			 enter the descriptive name that you want for the phone system. |
| Step 4 | If you want to use this phone system as the default for TRaP
                                          			 connections so that administrators and users without voicemail boxes can record
                                          			 and playback through the phone in Unity Connection web applications, check the Default TRAP Switch check box. If you want to use
                                          			 another phone system as the default for TRaP connections, uncheck this check
                                          			 box. |
| Step 5 | Select Save . |
| Step 6 | On the Phone System Basics page, in the Related Links drop-down
                                          			 box, select Add Port Group and select Go . |
| Step 7 | On the New Port Group page, enter the applicable settings and
                                          			 select Save . Table 16. Settings for the New Port Group Page Field Setting Phone System Select the name of the phone system that you entered in Step 3 . Create From Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box. Display Name Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. SIP Security Profile Select 5060 . SIP Transport Protocol Select the SIP transport protocol that Unity Connection uses. IPv4 Address or Host Name Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection. IPv6 Address or Host Name Do not enter a value in this field. IPv6 is not supported for
                                                         						  TIMG integrations. IP Address or Host Name Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection. Port Enter the SIP port of the TIMG unit that Unity Connection
                                                         						  connects to. You should use the default setting. Caution This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. | Field | Setting | Phone System | Select the name of the phone system that you entered in Step 3 . | Create From | Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box. | Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. | SIP Security Profile | Select 5060 . | SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. | IPv4 Address or Host Name | Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection. | IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                                         						  TIMG integrations. | IP Address or Host Name | Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection. | Port | Enter the SIP port of the TIMG unit that Unity Connection
                                                         						  connects to. You should use the default setting. Caution This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. | Caution | This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. |
| Field | Setting |
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. |
| IPv4 Address or Host Name | Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection. |
| IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                                         						  TIMG integrations. |
| IP Address or Host Name | Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection. |
| Port | Enter the SIP port of the TIMG unit that Unity Connection
                                                         						  connects to. You should use the default setting. Caution This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. | Caution | This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. |
| Caution | This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. |
| Step 8 | On the Port Group Basics page, in the Related Links drop-down
                                          			 box, select Add Ports and select Go . |
| Step 9 | On the New Port page, enter the following settings and select Save . Table 17. Settings for the New Ports Page Field Considerations Enabled Check this check box. Number of Ports Enter the number of voice messaging ports that you want to
                                                         						  create in this port group. Note For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. Phone System Select the name of the
                                                         						  phone system that you entered in Step 3 . Port Group Select the name of the
                                                         						  port group that you added in Step 7 . | Field | Considerations | Enabled | Check this check box. | Number of Ports | Enter the number of voice messaging ports that you want to
                                                         						  create in this port group. Note For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. | Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. | Phone System | Select the name of the
                                                         						  phone system that you entered in Step 3 . | Port Group | Select the name of the
                                                         						  port group that you added in Step 7 . |
| Field | Considerations |
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice messaging ports that you want to
                                                         						  create in this port group. Note For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. | Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
| Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
| Phone System | Select the name of the
                                                         						  phone system that you entered in Step 3 . |
| Port Group | Select the name of the
                                                         						  port group that you added in Step 7 . |
| Step 10 | On the Search Ports page, select the display name of the first
                                          			 voice messaging port that you created for this phone system integration. Note By default, the display names for the voice messaging ports are
                                                      				composed of the port group display name followed by incrementing numbers. | Note | By default, the display names for the voice messaging ports are
                                                      				composed of the port group display name followed by incrementing numbers. |
| Note | By default, the display names for the voice messaging ports are
                                                      				composed of the port group display name followed by incrementing numbers. |
| Step 11 | On the Port Basics page, set the voice messaging port settings
                                          			 as applicable. The fields in the following table are the ones that you can
                                          			 change. Table 18. Settings for the Voice Messaging Ports Field Considerations Enabled Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. Extension Enter the extension for
                                                         						  the port as assigned on the phone system. Answer Calls Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. Perform Message
                                                         						  Notification Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. Send MWI Requests Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports. Allow TRAP Connections Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. Outgoing Hunt Order Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest. | Field | Considerations | Enabled | Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. | Extension | Enter the extension for
                                                         						  the port as assigned on the phone system. | Answer Calls | Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. | Perform Message
                                                         						  Notification | Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. | Send MWI Requests | Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports. | Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. | Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest. |
| Field | Considerations |
| Enabled | Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. |
| Extension | Enter the extension for
                                                         						  the port as assigned on the phone system. |
| Answer Calls | Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. |
| Perform Message
                                                         						  Notification | Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. |
| Send MWI Requests | Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports. |
| Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. |
| Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest. |
| Step 12 | Select Save . |
| Step 13 | Select Next . |
| Step 14 | Repeat Step 11 through Step 13 for all
                                          			 remaining voice messaging ports for the phone system. |
| Step 15 | In Cisco Unity Connection Administration, expand Telephony
                                             				Integrations , then select Phone System . |
| Step 16 | On the Search Phone Systems page, under Display Name, select the
                                          			 name of the phone system that you entered in Step 3 . |
| Step 17 | Repeat Step 6 through Step 16 for each
                                          			 remaining TIMG unit integrated with Unity Connection. Note Each TIMG unit is connected to one port group with the
                                                      				applicable voice messaging ports. For example, a system that uses two TIMG
                                                      				units requires two port groups, one port group for each TIMG unit. | Note | Each TIMG unit is connected to one port group with the
                                                      				applicable voice messaging ports. For example, a system that uses two TIMG
                                                      				units requires two port groups, one port group for each TIMG unit. |
| Note | Each TIMG unit is connected to one port group with the
                                                      				applicable voice messaging ports. For example, a system that uses two TIMG
                                                      				units requires two port groups, one port group for each TIMG unit. |
| Step 18 | If another phone system integration exists, in Cisco Unity
                                          			 Connection Administration, expand Telephony
                                             				Integrations , then select Trunk .
                                          			 Otherwise, skip to Step 22 . |
| Step 19 | On the Search Phone System Trunks page, on the Phone System
                                          			 Trunk menu, select New Phone System
                                             				Trunk . |
| Step 20 | On the New Phone System Trunk page, enter the following settings
                                          			 for the phone system trunk and select Save . Table 19. Settings for the Phone System Trunk Field Setting From Phone System Enter the display name of
                                                         						  the phone system that you are creating a trunk for. To Phone System Enter the display name of
                                                         						  the previously existing phone system that the trunk connects to. Trunk Access Code Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system. | Field | Setting | From Phone System | Enter the display name of
                                                         						  the phone system that you are creating a trunk for. | To Phone System | Enter the display name of
                                                         						  the previously existing phone system that the trunk connects to. | Trunk Access Code | Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system. |
| Field | Setting |
| From Phone System | Enter the display name of
                                                         						  the phone system that you are creating a trunk for. |
| To Phone System | Enter the display name of
                                                         						  the previously existing phone system that the trunk connects to. |
| Trunk Access Code | Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system. |
| Step 21 | Repeat Step 19 and Step 20 for all
                                          			 remaining phone system trunks that you want to create. |
| Step 22 | In Cisco Unity Connection Administration, expand Telephony
                                             				Integrations , then select Port Group . |
| Step 23 | On the Search Port Groups page, select the display name of the
                                          			 port group that you added in Step 7 . |
| Step 24 | On the Port Group Basics page, select Reset . |
| Step 25 | When prompted that resetting terminates all call traffic, select OK . |
| Step 26 | In the Related Links drop-down list, select Check Telephony
                                             				Configuration and select Go to confirm
                                          			 the phone system integration settings. If the test is not successful, the Task Execution Results
                                             				displays one or more messages with troubleshooting steps. After correcting the
                                             				problems, test the connection again. |
| Step 27 | In the Task Execution Results window, select Close . |

| Field | Setting |
|---|---|
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. |
| IPv4 Address or Host Name | Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection. |
| IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                                         						  TIMG integrations. |
| IP Address or Host Name | Enter the IP address of the TIMG unit that you are integrating
                                                         						  with Unity Connection. |
| Port | Enter the SIP port of the TIMG unit that Unity Connection
                                                         						  connects to. You should use the default setting. Caution This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. | Caution | This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. |
| Caution | This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. |

| Caution | This name must match the setting in the TCP/UDP Server Port
                                                                  						  field on the Configuration > VoIP > General page of the TIMG unit.
                                                                  						  Otherwise, the integration do not function correctly. |
|---|---|

| Field | Considerations |
|---|---|
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice messaging ports that you want to
                                                         						  create in this port group. Note For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. | Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
| Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
| Phone System | Select the name of the
                                                         						  phone system that you entered in Step 3 . |
| Port Group | Select the name of the
                                                         						  port group that you added in Step 7 . |

| Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the TIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
|---|---|

| Note | By default, the display names for the voice messaging ports are
                                                      				composed of the port group display name followed by incrementing numbers. |
|---|---|

| Field | Considerations |
|---|---|
| Enabled | Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. |
| Extension | Enter the extension for
                                                         						  the port as assigned on the phone system. |
| Answer Calls | Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. |
| Perform Message
                                                         						  Notification | Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. |
| Send MWI Requests | Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports. |
| Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. |
| Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest. |

| Note | Each TIMG unit is connected to one port group with the
                                                      				applicable voice messaging ports. For example, a system that uses two TIMG
                                                      				units requires two port groups, one port group for each TIMG unit. |
|---|---|

| Field | Setting |
|---|---|
| From Phone System | Enter the display name of
                                                         						  the phone system that you are creating a trunk for. |
| To Phone System | Enter the display name of
                                                         						  the previously existing phone system that the trunk connects to. |
| Trunk Access Code | Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system. |