---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-integration-pimg-b-14cucintpimg-b-14cucintpimg-chapter-01011-h-5af9e8badd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/pimg/b_14cucintpimg/b_14cucintpimg_chapter_01011.html
retrieved_at: 2026-08-16T18:37:27.669120+00:00
---

PIMG Integration Guide for Cisco Unity Connection Release 14

# PIMG Integration Guide for Cisco Unity Connection Release 14

Updated: March 25, 2021

Chapter: Setting Up a
	 Serial (SMDI, MCI, or MD-110) PIMG Integration with Cisco Unity Connection

## Chapter: Setting Up a
	 Serial (SMDI, MCI, or MD-110) PIMG Integration with Cisco Unity Connection

# Setting Up a
                     	 Serial (SMDI, MCI, or MD-110) PIMG Integration with Cisco Unity Connection

### Setting Up a Serial (SMDI, MCI, or MD-110) PIMG Integration

## Task List for
                        	 Serial (SMDI, MCI, or MD-110) PIMG Integration

Before doing the following tasks to integrate Unity Connection with the Serial phone system using PIMG units (media gateways),
                           confirm that the Unity Connection server is ready for the integration after completing the server installation, following
                           the tasks in the “ Installing Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

Review the system and equipment requirements to confirm that all
                                 			 phone system and Unity Connection server requirements have been met. See the Requirements section.

Plan how the voice messaging ports are used by Unity Connection.
                                 			 See the Planning the Usage of Voice Messaging Ports chapter.

Program the phone system and extensions. See the “Programming
                                    				Phone System for a Serial Integration” section.

Set up the PIMG units. See the “Setting
                                    				Up Analog PIMG Units for a Serial Integration” section.

Create the integration. See the Configuring Unity Connection for Integration with the Phone System section.

Test the integration. See the Testing the Integration chapter.

If this integration is a second or subsequent integration, add
                                 			 the applicable new user templates for the new phone system. See the Adding New User Templates for Multiple Integrations chapter.

## Requirements

This integration supports configurations of the following
                           		components:

### Phone
                           	 System

A phone system that supports the SMDI, MCI, or MD-110 serial
                                    			 protocols.

For a Centrex phone system only:

A Centrex service SMDI package, with one SMDI 4-wire private
                                          				  data link connected to the external modem.

A type 202T or 212A external modem, set to 1200 baud.

One or more of the applicable PIMG units. For details, see the
                                    			 " Introduction ”
                                    			 chapter.

The serial data port on the phone system connected to the serial
                                    			 port on the master PIMG unit through an RS-232 serial cable (which is available
                                    			 from Cisco).

Specifications for the serial cable are in Connecting PBX-IP Media Gateway (PIMG) to the Serial Port of a
                                 		  PBX at http://www.dialogic.com/support/helpweb/mg/tn117.htm .

We recommend that the serial cable have the following
                              		construction:

A maximum of 50 feet (15.24 m) in length

24 AWG stranded conductors

Low capacitance—for example, no more than 12 pF/ft (39.4 pF/m)
                                    			 between conductors

At least 65 percent braided shield over aluminized polymer
                                    			 sleeve around conductors

UL-recognized overall cable jacket insulation with low
                                    			 dielectric constant

Braided shield fully terminated to and enclosed by a metal
                                    			 connector backshell

Gold-plated connector contacts

The voice messaging ports in the phone system connected by
                                    			 analog lines to the ports on the PIMG units.

We recommend that you connect the voice messaging ports on the
                              		phone system to the ports on the PIMG units in a planned manner to simplify
                              		troubleshooting. For example, the first phone system voice messaging port
                              		connects to the first port on the first PIMG unit, the second phone system
                              		voice messaging port connects to the second port on the first PIMG unit, and so
                              		on.

The PIMG units connected to the same LAN or WAN that Unity
                                    			 Connection is connected to.

If the PIMG units connect to a WAN, the requirements for the WAN
                                    			 network connections are:

For G.729a codec formatting, a minimum of 32.76 Kbps guaranteed
                                          				  bandwidth for each voice messaging port.

For G.711 codec formatting, a minimum of 91.56 Kbps guaranteed
                                          				  bandwidth for each voice messaging port.

No network devices that implement network address translation
                                          				  (NAT).

A maximum 200 ms one-way network latency.

### Unity Connection
                           	 Server

Unity Connection installed following the tasks in the “ Installing Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

A license that enables the applicable number of voice messaging
                                    			 ports.

## Programming Phone System for a Serial Integration

If you use programming options other than those
                              		  supplied in the following procedure, the performance of the integration may be
                              		  affected.

Caution

In programming the phone system, do not send
                                          			 calls to voice messaging ports in Unity Connection that cannot answer calls
                                          			 (voice messaging ports that are not set to Answer Calls). For example, if a
                                          			 voice messaging port is set only to Perform Message Notification, do not send
                                          			 calls to it.

Do the following steps to program the phone
                              		  system for a serial integration with Unity Connection

Step 1

Program the analog lines connecting to the
                                       			 voice messaging ports on the PIMG units as a multiline hunt group.

Make sure that the phone system sends calls
                                          				only to Unity Connection voice ports that are set to Answer Calls. Calls sent
                                          				to a voice port not set to Answer Calls cannot be answered by Unity Connection
                                          				and may cause other problems.

Step 2

Enable hookflash transfer capability on each
                                       			 analog line that connects to the voice messaging ports on the PIMG units.

Step 3

Enable caller ID (via SMDI, MCI, or MD-110)
                                       			 on each subscriber extension.

Step 4

For each subscriber extension, set the call
                                       			 forwarding options to the following:

Unrestricted source

Forward when the extension is not
                                                					 answered

Forward when the extension is busy

## Setting Up Analog PIMG Units for a Serial Integration

Do the following procedures to set up the analog PIMG units that are connected to the phone system for a serial integration
                           using the SMDI, MCI, or MD-110 protocol.

These procedures require that the following tasks have already been completed:

The phone system is connected to the PIMG units using analog lines and the applicable RS-232 serial cable.

The PIMG units are ready to be connected to the LAN or WAN.

The PIMG units are connected to a power source.

Fields that are not mentioned in the following procedures must keep their default values. For the default values of all fields,
                           see the manufacturer documentation for the PIMG units.

### Downloading PIMG Firmware Update Files for Analog PIMG Units

Step 1

On a Windows workstation with a high-speed
                                          			 Internet connection that have access to the PIMG units, go to the Voice and
                                          			 Unified Communications Downloads page at http://software.cisco.com/download/navigator.html?mdfid=280082558&i=rm .

To access the software download page, you
                                                         				  must be signed in to Cisco.com as a registered user.

This procedure describes the steps when using
                                                         				  Internet Explorer as your web browser. If you are using a different web
                                                         				  browser, the steps may differ.

Step 2

In the tree control on the Downloads Home
                                          			 page, expand Unified Communications> Unified Communications
                                                				  Applications > Messaging > Cisco Unity and select Cisco Unity Telephony
                                             				Integration .

Step 3

On the Log In page, enter your username and
                                          			 password, then select Log In .

Step 4

On the Select a Release page, under Latest
                                          			 Releases, select the most recent release.

Step 5

In the right column, select the version of
                                          			 the firmware for analog PIMG units.

Step 6

On the Download Image page, select Download .

Step 7

On the Supporting Document(s) page, select Agree .

Step 8

In the File Download dialog box, select Save .

Step 9

In the Save As dialog box, browse to the
                                          			 Windows workstation that have access the PIMG units, browse to a directory
                                          			 where you want to save the file, and select Save .

Step 10

In the Download Complete dialog box, select Open . The window for
                                          			 extracting the PIMG firmware update files appears.

Step 11

Select Extract .

Step 12

In the Extract dialog box, browse to the
                                          			 directory where you want the extracted files, and select Extract .

Step 13

Close the window for the extracting
                                          			 application.

### Setting Up Analog PIMG Units (Firmware Version 6.x)

Step 1

On the Windows workstation, add a temporary
                                          			 route to enable access to the PIMG units.

On the Windows Start menu, select Run .

Enter cmd , and press Enter . The Command Prompt window
                                                				  appears.

At the command prompt, enter route add 10.12.13.74 <IP Address of
                                                   					 Workstation> , and press Enter .

For example, if the IP address of the
                                                   					 workstation is 198.1.3.25, enter “route add 10.12.13.74<space>198.1.3.25”
                                                   					 in the Command Prompt window.

Close the Command Prompt window.

Step 2

Connect a PIMG unit to the network.

Step 3

In the web browser, go to http://10.12.13.74 .

Step 4

To sign in, enter the following
                                          			 case-sensitive settings.

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

On the Upgrade page, select Browse .

Step 8

In the Choose File dialog box, browse to the
                                          			 directory on the Windows workstation that has the extracted PIMG firmware
                                          			 update files.

Step 9

Select Ls_<xx > .app (where <xx> is multiple digits), and select Open .

Step 10

On the Upgrade page, select Install File .

Step 11

After the file is installed, a message
                                          			 prompting you to restart the PIMG unit appears. Select Cancel .

Do not restart the PIMG unit until you are
                                             				instructed to do so later in this procedure, even if the file installation
                                             				fails. Restarting the PIMG unit at this step may prevent the PIMG unit from
                                             				functioning correctly.

Step 12

Repeat Step 6 through Step 11 for the file Run_<xx > .dsp .

Step 13

On the System menu, select Upgrade .

Step 14

On the Upgrade page, under Import, select Browse .

Step 15

In the Choose File dialog box, browse to the
                                          			 file Ls_<xx > .fsh .

Step 16

Select Ls_<xx > .fsh , and select Open .

Step 17

On the Upgrade page, select Install File .

Step 18

After the file is installed, a message
                                          			 prompting you to restart the PIMG unit appears. Select OK .

Step 19

In the web browser, go to http://10.12.13.74 .

Step 20

To sign in, enter the following
                                          			 case-sensitive settings.

Field

Setting

Username

Enter admin .

Password

Enter IpodAdmin .

Step 21

Select OK .

Step 22

If your Unity Connection system must have an
                                          			 RTP port range of 16384 to 32767, do the following substeps. Otherwise,
                                          			 continue to Step 23 .

You must set the RTP port range for the PIMG
                                             				units if your system uses an RTP port range of 16384 to 32767. Otherwise, Unity
                                             				Connection cannot answer calls and callers hear ringing or silence.

The default RTP port range for PIMG units
                                                         				  is 49000 to 50000. Some Unity Connection configurations require a different RTP
                                                         				  port range.

On the Configuration menu, select Import/Export .

On the Import/Export page, under Export
                                                				  Files, select Export All Settings .

In the File Download dialog box, select Save .

In the Save As dialog box, browse to the
                                                				  Windows workstation that has access to the PIMG units, browse to a directory
                                                				  where you want to save the file, and select Save .

In the Download Complete dialog box,
                                                				  select Open . Notepad opens the file
                                                				  Config.ini that you saved.

Locate the line with the following
                                                				  parameter:

```
gwRTPStartPort
```

Change the value of the parameter to 16384 so that the line reads as
                                                				  follows:

```
gwRTPStartPort = 16384
```

Locate the line with the following
                                                				  parameter:

```
gwRTPEndPort
```

Change the value of the parameter to 32767 so that the line reads as
                                                				  follows:

```
gwRTPEndPort = 32767
```

Save the file, and exit Notepad.

On the Configuration menu of the PIMG
                                                				  unit, select Import/Export .

On the Import/Export page, under Browse
                                                				  for Import File, select Browse .

In the Choose File dialog box, browse to
                                                				  the file Config.ini that you saved.

Select Config.ini , and select Open .

On the Import/Export page, select Import File .

When prompted to restart the PIMG unit,
                                                				  select OK .

When the PIMG unit has restarted, in the
                                                				  web browser, go to http://10.12.13.74 .

To sign in, enter the following
                                                				  case-sensitive settings.

Field

Setting

Username

Enter admin .

Password

Enter IpodAdmin .

Select OK .

Step 23

On the System menu, select Password .

Step 24

On the Change Password page, enter the
                                          			 following settings.

Field

Setting

Old Password

Enter IpodAdmin . (This setting is
                                                         						  case sensitive.)

New Password

Enter your new password. (This
                                                         						  setting is case sensitive.)

Confirm Password

Enter your new password. (This
                                                         						  setting is case sensitive.)

Step 25

Select Change .

Step 26

On the Configuration menu, select Mgmt Protocols .

Step 27

On the Management Protocols page, enter the
                                          			 following settings.

Field

Settings

E-mail Alarms Enabled

Select No .

SNMP Traps Enabled

Select No .

Step 28

Select Submit .

Step 29

On the Configuration menu, select Routing Table .

Step 30

On the Routing Table page, under Router
                                          			 Configuration, select VoIP Host Groups .

Step 31

Under VoIP Host Groups, enter the following
                                          			 settings for the first VoIP Host Group.

Field

Settings

Name

Accept the default or enter another
                                                         						  descriptive name of the VoIP host group.

Load-Balanced

(Unity
                                                            							 Connection without a cluster) Select False .

(Unity
                                                            							 Connection with a cluster configured) Select False .

Fault-Tolerant

(Unity
                                                            							 Connection without a cluster) Select False .

(Unity
                                                            							 Connection with a cluster configured) Select True .

Step 32

For Unity Connection without a cluster,
                                          			 under Host List, enter the host name or IP address of the Unity Connection
                                          			 server and the server port in the format <host name or IP address>:5060.

For Cisco Unity Connection with a cluster
                                             				configured, under Host List, enter the host name or IP address of the
                                             				subscriber server (the second Unity Connection server that you installed) and
                                             				the server port in the format <host name or IP address>:5060.

Step 33

For Unity Connection without a cluster,
                                          			 continue to Step 35 . For Unity Connection
                                          			 with a cluster configured, select Add Host .

Step 34

In the second field, enter the host name or
                                          			 IP address of the publisher server (the first Unity Connection server that you
                                          			 installed) and the server port in the format <host name or IP
                                          			 address>:5060.

Do not add a third host under Host List or a
                                             				second host group under VoIP Host Groups. Otherwise, the Unity Connection
                                             				cluster may not function correctly.

Step 35

Select Submit .

Step 36

Under Router Configuration, select TDM Trunk Groups .

Step 37

Under TDM Trunk Groups, select Add Trunk Group .

Step 38

Under TDM Trunk Groups, enter the following
                                          			 settings for the first TDM trunk group.

Field

Settings

Name

Enter All_Calls or another unique
                                                         						  name.

This TDM trunk group handles all
                                                         						  calls to and from the phone system.

Selection Direction

Select Ascending .

Selection Mode

Select Linear .

Port/Channel Content

Enter the numbers of the PIMG ports
                                                         						  that handle all calls. For example, enter “*” for all PIMG ports, or enter
                                                         						  “1-6” for the first six PIMG ports.

Step 39

Select Submit .

Step 40

Under Router Configuration, select Inbound VoIP Rules .

Step 41

Under Inbound VoIP Rules, uncheck the Enabled check box for
                                          			 the default rule.

Step 42

Select Add Rule .

Step 43

Under Inbound VoIP Rules, enter the
                                          			 following settings for the first new inbound VoIP rule.

Field

Settings

Enable

Check this check box.

Rule Label

Do one of the following:

If you use CPID manipulation,
                                                               								enter All_UC_Calls or another
                                                               								name.

This inbound VoIP rule handles all
                                                         						  outbound calls from Unity Connection.

If you cannot use CPID
                                                               								manipulation, enter UC_Calls_and_Messages or
                                                               								another name.

This inbound VoIP rule handles all
                                                         						  outbound calls and MWI calls from Unity Connection.

Request Type

Do one of the following:

If you use CPID manipulation,
                                                               								select Call .

If you cannot use CPID
                                                               								manipulation, select Any .

Originating VoIP Host Address

Enter * .

Step 44

Under Inbound VoIP Request Matching, enter
                                          			 the following settings.

The rule that you created in Step 43 must be selected.
                                             				Otherwise, any changes you make apply to another rule.

Field

Settings

Calling Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Calling Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Called Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Called Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Redirect Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Redirect Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Step 45

Under Outbound Routes, enter the following
                                          			 settings.

The rule that you created in Step 43 must be selected.
                                             				Otherwise, any changes you make apply to another rule.

Field

Settings

Device
                                                            							 Selection

Outbound Destination

Select TDM .

Trunk Group

Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.”

CPID
                                                            							 Manipulation

Calling Number

Enter S .

Calling Name

Enter S .

Called Number

Enter D .

Called Name

Enter D .

Redirect Number

Enter R .

Redirect Name

Enter R .

Select
                                                            							 Primary/Alternate Route

Primary

Select Primary .

Step 46

If you cannot use CPID manipulation, skip to Step 50 . Otherwise, under
                                          			 Inbound VoIP Rules, select Add Rule .

Step 47

Under Inbound VoIP Rules, enter the
                                          			 following settings for the second new inbound VoIP rule.

Field

Settings

Enable

Check this check box.

Rule Label

Enter UC_MWIs or another name.

This inbound VoIP rule handles all
                                                         						  MWIs from Unity Connection.

Request Type

Select Message .

Originating VoIP Host Address

Enter * .

Step 48

Under Inbound VoIP Request Matching, enter
                                          			 the following settings.

The rule that you created in Step 47 must be selected.
                                             				Otherwise, any changes you make apply to another rule.

Field

Settings

Calling Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Calling Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Called Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Called Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Redirect Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Redirect Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Step 49

Under Outbound Routes, enter the following
                                          			 settings.

The rule that you created in Step 47 must be selected.
                                             				Otherwise, any changes you make apply to another rule.

Field

Settings

Device
                                                            							 Selection

Outbound Destination

Select TDM .

Trunk Group

Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.”

CPID
                                                            							 Manipulation

Calling Number

Enter S .

Calling Name

Enter S .

Called Number

Enter D .

Called Name

Enter D .

Redirect Number

Enter R .

Redirect Name

Enter R .

Select
                                                            							 Primary/Alternate Route

Primary

Select Primary .

Step 50

Select Submit .

Step 51

Under Router Configuration, select Inbound TDM Rules .

Step 52

Under Inbound TDM Rules, enter the following
                                          			 settings for the first inbound TDM rule.

Field

Settings

Enable

Check this check box.

Rule Label

Enter Inbound_Rule_1 or another
                                                         						  name.

This inbound TDM rule handles all
                                                         						  incoming calls from the phone system.

Request Type

Select Call .

Trunk Group

Select the name of the TDM trunk
                                                         						  group that you created for incoming calls from the phone system in Step 38 . For example, select
                                                         						  “All_Calls.”

Step 53

Under Inbound TDM Request Matching, enter
                                          			 the following settings.

The rule that you created in Step 52 must be selected.
                                             				Otherwise, any changes you make apply to another rule.

Field

Settings

Calling Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Calling Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Called Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Called Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Redirect Number

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Redirect Name

Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all.

Step 54

Under Outbound Routes, enter the following
                                          			 settings.

The rule that you created in Step 52 must be selected.
                                             				Otherwise, any changes you make apply to another rule.

Field

Settings

Device
                                                            							 Selection

Outbound Destination

Select VoIP .

Host Group

Select the name of the VoIP host
                                                         						  group that you created for Unity Connection in Step 31 .

CPID
                                                            							 Manipulation

Calling Number

Enter S .

Calling Name

Enter S .

Called Number

Enter D .

Called Name

Enter D .

Redirect Number

Enter R .

Redirect Name

Enter R .

Select
                                                            							 Primary/Alternate Route

Primary

Select Primary .

Step 55

If you want to create more Inbound TDM
                                          			 rules, under Inbound TDM Rules, select Add Rule . Otherwise,
                                          			 continue to Step 57 .

Note that additional Inbound TDM rules are
                                             				not necessary if you cannot use CPID manipulation.

Step 56

Repeat Step 52 through Step 55 for all remaining
                                          			 inbound TDM rules that you want to create.

Step 57

Select Submit .

Step 58

Step 59

Step 60

Step 61

On the Configuration menu, select TDM > General .

Step 62

On the TDM General Settings page, enter the
                                          			 following settings.

Field

Settings

PCM Coding

Select uLaw .

Minimum Call Party Delay (ms)

Enter 500 .

Maximum Call Party Delay (ms)

Enter 2000 .

Dial Digit on Time (ms)

Enter 100 .

Dial Inter-Digit Time (ms)

Enter 100 .

Dial Pause Time (ms)

Enter 2000 .

Turn MWI On FAC

Leave this field blank.

Turn MWI Off FAC

Leave this field blank.

Outbound Call Connect Timeout (ms)

Enter 10000 .

Wait for Ringback/Connect on Blind
                                                         						  Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number of the Unity
                                                         						  Connection voice messaging ports.

Step 63

Select Submit .

Step 64

On the Configuration menu, select TDM > Port Enable .

Step 65

On the TDM Port Enabling page, select No for the ports that
                                          			 you want to disable on the PIMG unit.

Step 66

Confirm that Yes is selected for all
                                          			 other ports on the PIMG unit.

Step 67

Select Submit .

Step 68

On the Configuration menu, select VoIP > General .

Step 69

On the VoIP General Settings page, enter the
                                          			 following settings.

Field

Setting

User-Agent

Host and Domain Name

Enter the host and domain name of
                                                         						  the PIMG unit.

Transport Type

Select UDP .

Call as Domain Name

Select No .

Invite Expiration (sec)

Enter 120 .

Server

DNS Server Address

Enter the IP Address of the Domain
                                                         						  Name Server that the PIMG unit uses.

Registration Server Address

Leave this field blank.

Registration Server Port

Enter 5060 .

Registration Expiration (sec)

Enter 3600 .

TCP/UDP

UDP/TCP Transports Enabled

Select Yes .

TCP/UDP Server Port

Enter 5060 .

Proxy

Primary Proxy Server Address

Leave this field blank.

Primary Proxy Server Port

Not applicable. Leave the default
                                                         						  setting.

Backup Proxy Server Address

Not applicable. Leave the default
                                                         						  setting.

Backup Proxy Server Port

Not applicable. Leave the default
                                                         						  setting.

Proxy Query Interval

Enter 10 .

Timing

T1 Time (ms)

Enter 400 .

T2 Time (ms)

Enter 3000 .

Monitoring

Monitor Call Connections

Select No .

Step 70

Select Submit .

Step 71

On the Configuration menu, select VoIP > Media .

Step 72

On the VoIP Media Settings page, enter the
                                          			 following settings.

Field

Settings

Audio

Audio Compression

Select the preferred codec for audio
                                                         						  compression.

RTP Digit Relay Mode

Select RFC2833 .

Signaling Digit Relay Mode

Select Off .

Voice Activity Detection

Select Off .

Frame Size

Select the applicable setting:

G.711— 20

G.729AB— 10

Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence.

Frames Per Packet

Select the applicable setting:

G.711— 1

G.729AB— 2

Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence.

Step 73

Select Submit .

Step 74

On the Configuration menu, select VoIP > QOS .

Step 75

On the VoIP QOS Configuration page, enter
                                          			 the following settings.

Field

Settings

Call Control QOS Byte

Enter 104 .

RTP QOS Byte

Enter 184 .

Step 76

Select Submit .

Step 77

On the Configuration menu, select IP .

Step 78

On the IP Settings page, enter the following
                                          			 settings.

Field

Settings

Client IP Address

Enter the new IP address you want to
                                                         						  use for the PIMG unit.

(This is the IP address that you
                                                         						  enter in Cisco Unity Connection Administration when you create the
                                                         						  integration.)

Client Subnet Mask

Enter the new subnet mask, if the
                                                         						  subnet mask is different from the default IP address.

Default Network Gateway Address

Enter the IP address of the default
                                                         						  network gateway router that the PIMG units use.

BOOTP Enabled

Select No .

Step 79

Select Submit .

Step 80

On the Configuration menu, select Serial > General .

Step 81

On the Serial Port, COM 1 page, enter the
                                          			 following settings.

Field

Settings

Serial Port Baud Rate

Select the setting that is
                                                         						  configured on the phone system.

The default setting is 9600.

Serial Port Parity

Select the setting that is
                                                         						  configured on the phone system.

The default setting is None.

Serial Port Data Bits

Select the setting that is
                                                         						  configured on the phone system.

The default setting is 8.

Serial Port Stop Bits

Select the setting that is
                                                         						  configured on the phone system.

The default setting is 1.

Step 82

Select Submit .

Step 83

On the Configuration menu, select Serial > Switch Protocol .

Step 84

On the Switch Protocol page, enter the
                                          			 following settings.

Field

Settings

Serial
                                                            							 Port, COM 1

Serial Mode

Select the applicable setting:

Master —Select this setting when this PIMG unit is
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								only one master PIMG unit in a phone system integration.

Slave —Select this setting when this PIMG unit is not
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								multiple slave PIMG units in a phone system integration.

Serial Interface Protocol

Select the serial protocol that your
                                                         						  phone system uses:

SMDI

MCI

MD-110

Cpid Len

Select the applicable setting.
                                                         						  Typically, the settings are 7 or 10.

Cpid Padding String

Enter the applicable string or leave
                                                         						  this field blank. Typically, the setting is one of the following:

A string of zeros, where the
                                                               								number of zeros matches the setting of the Cpid Len field.

A prefix that is provided by the
                                                               								Centrex service.

Voice Mail Port Len

If the setting of the Serial
                                                         						  Interface Protocol field is MD-110, enter 2 . Otherwise, accept the
                                                         						  default of 7 .

System Number

Enter the applicable setting.
                                                         						  Typically, the setting is 1.

MWI Response Timeout

Enter 2000 .

IP Address of Serial Server

If the PIMG unit is the master, this
                                                         						  field is for display only.

If the PIMG unit is a slave, enter
                                                         						  the IP address of the master PIMG unit (the PIMG unit that is connected to the
                                                         						  data link serial cable from the phone system).

Serial Cpid Expiration

Enter 2000 .

Logical
                                                            							 Extension Number

1

If the setting of the Serial
                                                         						  Interface Protocol field is MCI or MD-110, enter the extension number for each
                                                         						  port on the PIMG unit.

If the setting of the Serial
                                                         						  Interface Protocol field is SMDI, enter the logical port number. Typically, the
                                                         						  setting is 1 for port 1, 2 for port 2, and so on beginning with the master PIMG
                                                         						  unit and continuing through each of the slave PIMG units.

2

3

4

5

6

7

8

Step 85

Select Submit .

Step 86

On the Configure menu, select Tone Detection .

Step 87

On the Tone Detection page, under Call
                                          			 Progress Tone - Learn, in the Learn Tone Event field, select Busy and do the
                                          			 following substeps to verify that the tone is correct.

From a available phone, call a second
                                                				  phone.

Answer the second phone when it rings,
                                                				  and leave both handsets off so that both phones are busy.

From a third phone, dial one of the busy
                                                				  phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the
                                                				  handsets for the other two phones off.

Step 88

Under Call Progress Tone - Learn, in the
                                          			 Dial String field, enter the extension that you dialed in Step 87 c. from
                                          			 the third phone.

Step 89

Select Learn .

Step 90

On the Tone Detection page, under Call
                                          			 Progress Tone - Learn, in the Learn field, select Error and do the
                                          			 following substeps to verify that the tone is correct.

From an available phone, dial an
                                                				  extension that does not exist.

Confirm that you hear the reorder or
                                                				  error tone.

Hang up the phone.

Step 91

Under Call Progress Tone - Learn, in the
                                          			 Dial String field, enter the extension that you dialed in Step 90 a.

Step 92

Select Learn .

Step 93

On the Tone Detection page, under Call
                                          			 Progress Tone - Learn, in the Learn field, select Ringback and do the
                                          			 following substeps to verify that the tone is correct.

From an available phone, dial an
                                                				  extension that does exist.

Confirm that you hear the ringback tone.

Hang up the phone.

Step 94

Under Call Progress Tone - Learn, in the
                                          			 Dial String field, enter the extension that you dialed in Step 93 a.

Step 95

Select Learn .

Step 96

Select Submit .

Step 97

Hang up the phones that you used in Step 87 .

Step 98

On the System menu, select Restart .

Step 99

On the Restart page, select Restart Unit Now .

Step 100

Repeat Step 2 through Step 99 on all remaining PIMG
                                          			 units.

## Configuring Unity
                        	 Connection for Integration with the Phone System

After ensuring that the phone
                           		system, the PIMG units, and Unity Connection are ready for the integration, do
                           		the following procedure to set up the integration and to enter the port
                           		settings.

### Creating an
                           	 Integration

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

Under Message Waiting Indicator Settings, select Use Same Port
                                             				for Enabling and Disabling MWIs .

Step 6

Select Save .

Step 7

On the Phone System Basics page, in the Related Links drop-down
                                          			 box, select Add Port Group and select Go .

Step 8

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

IP Address or Host Name

Enter the IP address of the PIMG unit that you are integrating
                                                         						  with Unity Connection.

Port

Enter the SIP port of the PIMG unit that Unity Connection
                                                         						  connects to. We recommend that you use the default setting.

This name must match the setting in the TCP/UDP Server Port
                                                         						  field on the Configuration > VoIP > General page of the PIMG unit.
                                                         						  Otherwise, the integration cannot function correctly.

Step 9

On the Port Group Basics page, under Message Waiting Indicator
                                          			 Settings, uncheck the Enable Message Waiting Indicators check box and select Save .

Step 10

In the Related Links drop-down box, select Add Ports and select Go .

Step 11

On the New Port page, enter the following settings and select Save .

Field

Considerations

Enabled

Check this check box.

Number of Ports

Enter 8 .

(If you want to use fewer than eight voice messaging ports,
                                                         						  enter the number of voice messaging ports that you want to use on this PIMG
                                                         						  unit.)

For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports.

Phone System

Select the name of the
                                                         						  phone system that you entered in Step 3 .

Port Group

Select the name of the
                                                         						  port group that you added in Step 8 .

Step 12

On the Search Ports page, select the display name of the first
                                          			 voice messaging port that you created for this phone system integration.

By default, the display names for the voice messaging ports are
                                                         				  composed of the port group display name followed by incrementing numbers.

Step 13

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

(Serial integrations only) Uncheck this check box.
                                                         						  Otherwise, the integration may not function correctly.

(Digital and analog integrations only) Check this check
                                                         						  box to designate the port for turning MWIs on and off. Assign Send MWI Requests
                                                         						  to the least busy ports

Allow TRAP Connections

Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports.

Outgoing Hunt Order

Enter the priority order
                                                         						  in which Unity Connection uses the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection uses
                                                         						  the port that has been idle the longest.

Step 14

Select Save .

Step 15

Select Next .

Step 16

Repeat Step 13 through Step 15 for all
                                          			 remaining voice messaging ports for the phone system.

Step 17

In Cisco Unity Connection Administration, expand Telephony
                                             				Integrations , then select Phone System .

Step 18

On the Search Phone Systems page, under Display Name, select the
                                          			 name of the phone system that you entered in Step 3 .

Step 19

Repeat Step 7 through Step 18 for each
                                          			 remaining PIMG unit integrated with Unity Connection.

Each PIMG unit is connected to one port group with the
                                                         				  applicable voice messaging ports. For example, a system that uses five PIMG
                                                         				  units requires five port groups, one port group for each PIMG unit.

Step 20

To create a port group for MWIs, do the following substeps.

In Cisco Unity Connection Administration expand Telephony Integration then select Port Group .

On the Search Port Groups page, select Add New .

On the New Port Group page, enter the applicable settings and
                                                				  select Save .

Field

Setting

Phone System

Create From

Display Name

SIP Security Profile

SIP Transport Protocol

IPv4 Address or Host Name

IPv6 Address or Host Name

IP Address or Host Name

Port

Caution

On the Port Group Basics page, on the Edit menu, select Advanced Settings .

On the Edit Advanced Settings page, under SIP MWI Requests,
                                                				  select Not Port Specific then select Save .

On the Edit menu, select Port Group Basics .

Under Port Group, select Reset .

Under Message Waiting Indicator Settings, confirm that the Enable Message Waiting Indicator check box is checked and
                                                				  select Save .

Step 21

If another phone system integration exists, in Cisco Unity
                                          			 Connection Administration, expand Telephony
                                             				Integrations , then select Trunk .
                                          			 Otherwise, skip to Step 25 .

Step 22

On the Search Phone System Trunks page, on the Phone System
                                          			 Trunk menu, select New Phone System
                                             				Trunk .

Step 23

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

Step 24

Repeat Step 22 and Step 23 for all
                                          			 remaining phone system trunks that you want to create.

Step 25

In the Related Links drop-down list, select Check Telephony
                                             				Configuration and select Go to confirm
                                          			 the phone system integration settings.

If the test is not successful, the Task Execution Results
                                             				displays one or more messages with troubleshooting steps. After correcting the
                                             				problems, test the connection again.

Step 26

In the Task Execution Results window, select Close .

| Caution | In programming the phone system, do not send
                                          			 calls to voice messaging ports in Unity Connection that cannot answer calls
                                          			 (voice messaging ports that are not set to Answer Calls). For example, if a
                                          			 voice messaging port is set only to Perform Message Notification, do not send
                                          			 calls to it. |
|---|---|

| Step 1 | Program the analog lines connecting to the
                                       			 voice messaging ports on the PIMG units as a multiline hunt group. Make sure that the phone system sends calls
                                          				only to Unity Connection voice ports that are set to Answer Calls. Calls sent
                                          				to a voice port not set to Answer Calls cannot be answered by Unity Connection
                                          				and may cause other problems. |
|---|---|
| Step 2 | Enable hookflash transfer capability on each
                                       			 analog line that connects to the voice messaging ports on the PIMG units. |
| Step 3 | Enable caller ID (via SMDI, MCI, or MD-110)
                                       			 on each subscriber extension. |
| Step 4 | For each subscriber extension, set the call
                                       			 forwarding options to the following: Unrestricted source Forward when the extension is not
                                                					 answered Forward when the extension is busy |

| Step 1 | On a Windows workstation with a high-speed
                                          			 Internet connection that have access to the PIMG units, go to the Voice and
                                          			 Unified Communications Downloads page at http://software.cisco.com/download/navigator.html?mdfid=280082558&i=rm . Note To access the software download page, you
                                                         				  must be signed in to Cisco.com as a registered user. This procedure describes the steps when using
                                                         				  Internet Explorer as your web browser. If you are using a different web
                                                         				  browser, the steps may differ. | Note | To access the software download page, you
                                                         				  must be signed in to Cisco.com as a registered user. This procedure describes the steps when using
                                                         				  Internet Explorer as your web browser. If you are using a different web
                                                         				  browser, the steps may differ. |
|---|---|---|---|
| Note | To access the software download page, you
                                                         				  must be signed in to Cisco.com as a registered user. This procedure describes the steps when using
                                                         				  Internet Explorer as your web browser. If you are using a different web
                                                         				  browser, the steps may differ. |
| Step 2 | In the tree control on the Downloads Home
                                          			 page, expand Unified Communications> Unified Communications
                                                				  Applications > Messaging > Cisco Unity and select Cisco Unity Telephony
                                             				Integration . |
| Step 3 | On the Log In page, enter your username and
                                          			 password, then select Log In . |
| Step 4 | On the Select a Release page, under Latest
                                          			 Releases, select the most recent release. |
| Step 5 | In the right column, select the version of
                                          			 the firmware for analog PIMG units. |
| Step 6 | On the Download Image page, select Download . |
| Step 7 | On the Supporting Document(s) page, select Agree . |
| Step 8 | In the File Download dialog box, select Save . |
| Step 9 | In the Save As dialog box, browse to the
                                          			 Windows workstation that have access the PIMG units, browse to a directory
                                          			 where you want to save the file, and select Save . |
| Step 10 | In the Download Complete dialog box, select Open . The window for
                                          			 extracting the PIMG firmware update files appears. |
| Step 11 | Select Extract . |
| Step 12 | In the Extract dialog box, browse to the
                                          			 directory where you want the extracted files, and select Extract . |
| Step 13 | Close the window for the extracting
                                          			 application. |

| Note | To access the software download page, you
                                                         				  must be signed in to Cisco.com as a registered user. This procedure describes the steps when using
                                                         				  Internet Explorer as your web browser. If you are using a different web
                                                         				  browser, the steps may differ. |
|---|---|

| Step 1 | On the Windows workstation, add a temporary
                                          			 route to enable access to the PIMG units. On the Windows Start menu, select Run . Enter cmd , and press Enter . The Command Prompt window
                                                				  appears. At the command prompt, enter route add 10.12.13.74 <IP Address of
                                                   					 Workstation> , and press Enter . For example, if the IP address of the
                                                   					 workstation is 198.1.3.25, enter “route add 10.12.13.74<space>198.1.3.25”
                                                   					 in the Command Prompt window. Close the Command Prompt window. |
|---|---|
| Step 2 | Connect a PIMG unit to the network. |
| Step 3 | In the web browser, go to http://10.12.13.74 . |
| Step 4 | To sign in, enter the following
                                          			 case-sensitive settings. Table 1. Sign-in Settings Field Setting Username Enter admin . Password Enter IpodAdmin . | Field | Setting | Username | Enter admin . | Password | Enter IpodAdmin . |
| Field | Setting |
| Username | Enter admin . |
| Password | Enter IpodAdmin . |
| Step 5 | Select OK . |
| Step 6 | On the System menu, select Upgrade . |
| Step 7 | On the Upgrade page, select Browse . |
| Step 8 | In the Choose File dialog box, browse to the
                                          			 directory on the Windows workstation that has the extracted PIMG firmware
                                          			 update files. |
| Step 9 | Select Ls_<xx > .app (where <xx> is multiple digits), and select Open . |
| Step 10 | On the Upgrade page, select Install File . |
| Step 11 | After the file is installed, a message
                                          			 prompting you to restart the PIMG unit appears. Select Cancel . Do not restart the PIMG unit until you are
                                             				instructed to do so later in this procedure, even if the file installation
                                             				fails. Restarting the PIMG unit at this step may prevent the PIMG unit from
                                             				functioning correctly. |
| Step 12 | Repeat Step 6 through Step 11 for the file Run_<xx > .dsp . |
| Step 13 | On the System menu, select Upgrade . |
| Step 14 | On the Upgrade page, under Import, select Browse . |
| Step 15 | In the Choose File dialog box, browse to the
                                          			 file Ls_<xx > .fsh . |
| Step 16 | Select Ls_<xx > .fsh , and select Open . |
| Step 17 | On the Upgrade page, select Install File . |
| Step 18 | After the file is installed, a message
                                          			 prompting you to restart the PIMG unit appears. Select OK . |
| Step 19 | In the web browser, go to http://10.12.13.74 . |
| Step 20 | To sign in, enter the following
                                          			 case-sensitive settings. Table 2. Sign-in Settings Field Setting Username Enter admin . Password Enter IpodAdmin . | Field | Setting | Username | Enter admin . | Password | Enter IpodAdmin . |
| Field | Setting |
| Username | Enter admin . |
| Password | Enter IpodAdmin . |
| Step 21 | Select OK . |
| Step 22 | If your Unity Connection system must have an
                                          			 RTP port range of 16384 to 32767, do the following substeps. Otherwise,
                                          			 continue to Step 23 . You must set the RTP port range for the PIMG
                                             				units if your system uses an RTP port range of 16384 to 32767. Otherwise, Unity
                                             				Connection cannot answer calls and callers hear ringing or silence. Note The default RTP port range for PIMG units
                                                         				  is 49000 to 50000. Some Unity Connection configurations require a different RTP
                                                         				  port range. On the Configuration menu, select Import/Export . On the Import/Export page, under Export
                                                				  Files, select Export All Settings . In the File Download dialog box, select Save . In the Save As dialog box, browse to the
                                                				  Windows workstation that has access to the PIMG units, browse to a directory
                                                				  where you want to save the file, and select Save . In the Download Complete dialog box,
                                                				  select Open . Notepad opens the file
                                                				  Config.ini that you saved. Locate the line with the following
                                                				  parameter: gwRTPStartPort Change the value of the parameter to 16384 so that the line reads as
                                                				  follows: gwRTPStartPort = 16384 Locate the line with the following
                                                				  parameter: gwRTPEndPort Change the value of the parameter to 32767 so that the line reads as
                                                				  follows: gwRTPEndPort = 32767 Save the file, and exit Notepad. On the Configuration menu of the PIMG
                                                				  unit, select Import/Export . On the Import/Export page, under Browse
                                                				  for Import File, select Browse . In the Choose File dialog box, browse to
                                                				  the file Config.ini that you saved. Select Config.ini , and select Open . On the Import/Export page, select Import File . When prompted to restart the PIMG unit,
                                                				  select OK . When the PIMG unit has restarted, in the
                                                				  web browser, go to http://10.12.13.74 . To sign in, enter the following
                                                				  case-sensitive settings. Table 3. Sign-in Settings Field Setting Username Enter admin . Password Enter IpodAdmin . Select OK . | Note | The default RTP port range for PIMG units
                                                         				  is 49000 to 50000. Some Unity Connection configurations require a different RTP
                                                         				  port range. | Field | Setting | Username | Enter admin . | Password | Enter IpodAdmin . |
| Note | The default RTP port range for PIMG units
                                                         				  is 49000 to 50000. Some Unity Connection configurations require a different RTP
                                                         				  port range. |
| Field | Setting |
| Username | Enter admin . |
| Password | Enter IpodAdmin . |
| Step 23 | On the System menu, select Password . |
| Step 24 | On the Change Password page, enter the
                                          			 following settings. Table 4. Change Password Page Settings Field Setting Old Password Enter IpodAdmin . (This setting is
                                                         						  case sensitive.) New Password Enter your new password. (This
                                                         						  setting is case sensitive.) Confirm Password Enter your new password. (This
                                                         						  setting is case sensitive.) | Field | Setting | Old Password | Enter IpodAdmin . (This setting is
                                                         						  case sensitive.) | New Password | Enter your new password. (This
                                                         						  setting is case sensitive.) | Confirm Password | Enter your new password. (This
                                                         						  setting is case sensitive.) |
| Field | Setting |
| Old Password | Enter IpodAdmin . (This setting is
                                                         						  case sensitive.) |
| New Password | Enter your new password. (This
                                                         						  setting is case sensitive.) |
| Confirm Password | Enter your new password. (This
                                                         						  setting is case sensitive.) |
| Step 25 | Select Change . |
| Step 26 | On the Configuration menu, select Mgmt Protocols . |
| Step 27 | On the Management Protocols page, enter the
                                          			 following settings. Table 5. Management Protocols Page
                                                   				Settings Field Settings E-mail Alarms Enabled Select No . SNMP Traps Enabled Select No . | Field | Settings | E-mail Alarms Enabled | Select No . | SNMP Traps Enabled | Select No . |
| Field | Settings |
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |
| Step 28 | Select Submit . |
| Step 29 | On the Configuration menu, select Routing Table . |
| Step 30 | On the Routing Table page, under Router
                                          			 Configuration, select VoIP Host Groups . |
| Step 31 | Under VoIP Host Groups, enter the following
                                          			 settings for the first VoIP Host Group. Table 6. First VoIP Host Group Settings Field Settings Name Accept the default or enter another
                                                         						  descriptive name of the VoIP host group. Load-Balanced (Unity
                                                            							 Connection without a cluster) Select False . (Unity
                                                            							 Connection with a cluster configured) Select False . Fault-Tolerant (Unity
                                                            							 Connection without a cluster) Select False . (Unity
                                                            							 Connection with a cluster configured) Select True . | Field | Settings | Name | Accept the default or enter another
                                                         						  descriptive name of the VoIP host group. | Load-Balanced | (Unity
                                                            							 Connection without a cluster) Select False . (Unity
                                                            							 Connection with a cluster configured) Select False . | Fault-Tolerant | (Unity
                                                            							 Connection without a cluster) Select False . (Unity
                                                            							 Connection with a cluster configured) Select True . |
| Field | Settings |
| Name | Accept the default or enter another
                                                         						  descriptive name of the VoIP host group. |
| Load-Balanced | (Unity
                                                            							 Connection without a cluster) Select False . (Unity
                                                            							 Connection with a cluster configured) Select False . |
| Fault-Tolerant | (Unity
                                                            							 Connection without a cluster) Select False . (Unity
                                                            							 Connection with a cluster configured) Select True . |
| Step 32 | For Unity Connection without a cluster,
                                          			 under Host List, enter the host name or IP address of the Unity Connection
                                          			 server and the server port in the format <host name or IP address>:5060. For Cisco Unity Connection with a cluster
                                             				configured, under Host List, enter the host name or IP address of the
                                             				subscriber server (the second Unity Connection server that you installed) and
                                             				the server port in the format <host name or IP address>:5060. |
| Step 33 | For Unity Connection without a cluster,
                                          			 continue to Step 35 . For Unity Connection
                                          			 with a cluster configured, select Add Host . |
| Step 34 | In the second field, enter the host name or
                                          			 IP address of the publisher server (the first Unity Connection server that you
                                          			 installed) and the server port in the format <host name or IP
                                          			 address>:5060. Do not add a third host under Host List or a
                                             				second host group under VoIP Host Groups. Otherwise, the Unity Connection
                                             				cluster may not function correctly. |
| Step 35 | Select Submit . |
| Step 36 | Under Router Configuration, select TDM Trunk Groups . |
| Step 37 | Under TDM Trunk Groups, select Add Trunk Group . |
| Step 38 | Under TDM Trunk Groups, enter the following
                                          			 settings for the first TDM trunk group. Table 7. First TDM Trunk Group Settings (All
                                                   				Calls) Field Settings Name Enter All_Calls or another unique
                                                         						  name. This TDM trunk group handles all
                                                         						  calls to and from the phone system. Selection Direction Select Ascending . Selection Mode Select Linear . Port/Channel Content Enter the numbers of the PIMG ports
                                                         						  that handle all calls. For example, enter “*” for all PIMG ports, or enter
                                                         						  “1-6” for the first six PIMG ports. | Field | Settings | Name | Enter All_Calls or another unique
                                                         						  name. This TDM trunk group handles all
                                                         						  calls to and from the phone system. | Selection Direction | Select Ascending . | Selection Mode | Select Linear . | Port/Channel Content | Enter the numbers of the PIMG ports
                                                         						  that handle all calls. For example, enter “*” for all PIMG ports, or enter
                                                         						  “1-6” for the first six PIMG ports. |
| Field | Settings |
| Name | Enter All_Calls or another unique
                                                         						  name. This TDM trunk group handles all
                                                         						  calls to and from the phone system. |
| Selection Direction | Select Ascending . |
| Selection Mode | Select Linear . |
| Port/Channel Content | Enter the numbers of the PIMG ports
                                                         						  that handle all calls. For example, enter “*” for all PIMG ports, or enter
                                                         						  “1-6” for the first six PIMG ports. |
| Step 39 | Select Submit . |
| Step 40 | Under Router Configuration, select Inbound VoIP Rules . |
| Step 41 | Under Inbound VoIP Rules, uncheck the Enabled check box for
                                          			 the default rule. |
| Step 42 | Select Add Rule . |
| Step 43 | Under Inbound VoIP Rules, enter the
                                          			 following settings for the first new inbound VoIP rule. Table 8. First New Inbound VoIP Rule Settings
                                                   				(All Calls) Field Settings Enable Check this check box. Rule Label Do one of the following: If you use CPID manipulation,
                                                               								enter All_UC_Calls or another
                                                               								name. This inbound VoIP rule handles all
                                                         						  outbound calls from Unity Connection. If you cannot use CPID
                                                               								manipulation, enter UC_Calls_and_Messages or
                                                               								another name. This inbound VoIP rule handles all
                                                         						  outbound calls and MWI calls from Unity Connection. Request Type Do one of the following: If you use CPID manipulation,
                                                               								select Call . If you cannot use CPID
                                                               								manipulation, select Any . Originating VoIP Host Address Enter * . | Field | Settings | Enable | Check this check box. | Rule Label | Do one of the following: If you use CPID manipulation,
                                                               								enter All_UC_Calls or another
                                                               								name. This inbound VoIP rule handles all
                                                         						  outbound calls from Unity Connection. If you cannot use CPID
                                                               								manipulation, enter UC_Calls_and_Messages or
                                                               								another name. This inbound VoIP rule handles all
                                                         						  outbound calls and MWI calls from Unity Connection. | Request Type | Do one of the following: If you use CPID manipulation,
                                                               								select Call . If you cannot use CPID
                                                               								manipulation, select Any . | Originating VoIP Host Address | Enter * . |
| Field | Settings |
| Enable | Check this check box. |
| Rule Label | Do one of the following: If you use CPID manipulation,
                                                               								enter All_UC_Calls or another
                                                               								name. This inbound VoIP rule handles all
                                                         						  outbound calls from Unity Connection. If you cannot use CPID
                                                               								manipulation, enter UC_Calls_and_Messages or
                                                               								another name. This inbound VoIP rule handles all
                                                         						  outbound calls and MWI calls from Unity Connection. |
| Request Type | Do one of the following: If you use CPID manipulation,
                                                               								select Call . If you cannot use CPID
                                                               								manipulation, select Any . |
| Originating VoIP Host Address | Enter * . |
| Step 44 | Under Inbound VoIP Request Matching, enter
                                          			 the following settings. The rule that you created in Step 43 must be selected.
                                             				Otherwise, any changes you make apply to another rule. Table 9. Inbound VoIP Request Matching
                                                   				Settings Field Settings Calling Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Calling Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Called Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Called Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Redirect Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Redirect Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Field | Settings | Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Field | Settings |
| Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Step 45 | Under Outbound Routes, enter the following
                                          			 settings. The rule that you created in Step 43 must be selected.
                                             				Otherwise, any changes you make apply to another rule. Table 10. Outbound Routes Settings Field Settings Device
                                                            							 Selection Outbound Destination Select TDM . Trunk Group Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.” CPID
                                                            							 Manipulation Calling Number Enter S . Calling Name Enter S . Called Number Enter D . Called Name Enter D . Redirect Number Enter R . Redirect Name Enter R . Select
                                                            							 Primary/Alternate Route Primary Select Primary . | Field | Settings | Device
                                                            							 Selection | Outbound Destination | Select TDM . | Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.” | CPID
                                                            							 Manipulation | Calling Number | Enter S . | Calling Name | Enter S . | Called Number | Enter D . | Called Name | Enter D . | Redirect Number | Enter R . | Redirect Name | Enter R . | Select
                                                            							 Primary/Alternate Route | Primary | Select Primary . |
| Field | Settings |
| Device
                                                            							 Selection |
| Outbound Destination | Select TDM . |
| Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.” |
| CPID
                                                            							 Manipulation |
| Calling Number | Enter S . |
| Calling Name | Enter S . |
| Called Number | Enter D . |
| Called Name | Enter D . |
| Redirect Number | Enter R . |
| Redirect Name | Enter R . |
| Select
                                                            							 Primary/Alternate Route |
| Primary | Select Primary . |
| Step 46 | If you cannot use CPID manipulation, skip to Step 50 . Otherwise, under
                                          			 Inbound VoIP Rules, select Add Rule . |
| Step 47 | Under Inbound VoIP Rules, enter the
                                          			 following settings for the second new inbound VoIP rule. Table 11. Second New Inbound VoIP Rule Settings
                                                   				(MWIs) Field Settings Enable Check this check box. Rule Label Enter UC_MWIs or another name. This inbound VoIP rule handles all
                                                         						  MWIs from Unity Connection. Request Type Select Message . Originating VoIP Host Address Enter * . | Field | Settings | Enable | Check this check box. | Rule Label | Enter UC_MWIs or another name. This inbound VoIP rule handles all
                                                         						  MWIs from Unity Connection. | Request Type | Select Message . | Originating VoIP Host Address | Enter * . |
| Field | Settings |
| Enable | Check this check box. |
| Rule Label | Enter UC_MWIs or another name. This inbound VoIP rule handles all
                                                         						  MWIs from Unity Connection. |
| Request Type | Select Message . |
| Originating VoIP Host Address | Enter * . |
| Step 48 | Under Inbound VoIP Request Matching, enter
                                          			 the following settings. The rule that you created in Step 47 must be selected.
                                             				Otherwise, any changes you make apply to another rule. Table 12. Inbound VoIP Request Matching
                                                   				Settings Field Settings Calling Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Calling Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Called Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Called Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Redirect Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Redirect Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Field | Settings | Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Field | Settings |
| Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Step 49 | Under Outbound Routes, enter the following
                                          			 settings. The rule that you created in Step 47 must be selected.
                                             				Otherwise, any changes you make apply to another rule. Table 13. Outbound Routes Settings Field Settings Device
                                                            							 Selection Outbound Destination Select TDM . Trunk Group Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.” CPID
                                                            							 Manipulation Calling Number Enter S . Calling Name Enter S . Called Number Enter D . Called Name Enter D . Redirect Number Enter R . Redirect Name Enter R . Select
                                                            							 Primary/Alternate Route Primary Select Primary . | Field | Settings | Device
                                                            							 Selection | Outbound Destination | Select TDM . | Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.” | CPID
                                                            							 Manipulation | Calling Number | Enter S . | Calling Name | Enter S . | Called Number | Enter D . | Called Name | Enter D . | Redirect Number | Enter R . | Redirect Name | Enter R . | Select
                                                            							 Primary/Alternate Route | Primary | Select Primary . |
| Field | Settings |
| Device
                                                            							 Selection |
| Outbound Destination | Select TDM . |
| Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.” |
| CPID
                                                            							 Manipulation |
| Calling Number | Enter S . |
| Calling Name | Enter S . |
| Called Number | Enter D . |
| Called Name | Enter D . |
| Redirect Number | Enter R . |
| Redirect Name | Enter R . |
| Select
                                                            							 Primary/Alternate Route |
| Primary | Select Primary . |
| Step 50 | Select Submit . |
| Step 51 | Under Router Configuration, select Inbound TDM Rules . |
| Step 52 | Under Inbound TDM Rules, enter the following
                                          			 settings for the first inbound TDM rule. Table 14. First Inbound TDM Rule Settings Field Settings Enable Check this check box. Rule Label Enter Inbound_Rule_1 or another
                                                         						  name. This inbound TDM rule handles all
                                                         						  incoming calls from the phone system. Request Type Select Call . Trunk Group Select the name of the TDM trunk
                                                         						  group that you created for incoming calls from the phone system in Step 38 . For example, select
                                                         						  “All_Calls.” | Field | Settings | Enable | Check this check box. | Rule Label | Enter Inbound_Rule_1 or another
                                                         						  name. This inbound TDM rule handles all
                                                         						  incoming calls from the phone system. | Request Type | Select Call . | Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for incoming calls from the phone system in Step 38 . For example, select
                                                         						  “All_Calls.” |
| Field | Settings |
| Enable | Check this check box. |
| Rule Label | Enter Inbound_Rule_1 or another
                                                         						  name. This inbound TDM rule handles all
                                                         						  incoming calls from the phone system. |
| Request Type | Select Call . |
| Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for incoming calls from the phone system in Step 38 . For example, select
                                                         						  “All_Calls.” |
| Step 53 | Under Inbound TDM Request Matching, enter
                                          			 the following settings. The rule that you created in Step 52 must be selected.
                                             				Otherwise, any changes you make apply to another rule. Table 15. Inbound TDM Request Matching
                                                   				Settings Field Settings Calling Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Calling Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Called Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Called Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Redirect Number Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. Redirect Name Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Field | Settings | Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. | Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Field | Settings |
| Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Step 54 | Under Outbound Routes, enter the following
                                          			 settings. The rule that you created in Step 52 must be selected.
                                             				Otherwise, any changes you make apply to another rule. Table 16. Outbound Routes Settings Field Settings Device
                                                            							 Selection Outbound Destination Select VoIP . Host Group Select the name of the VoIP host
                                                         						  group that you created for Unity Connection in Step 31 . CPID
                                                            							 Manipulation Calling Number Enter S . Calling Name Enter S . Called Number Enter D . Called Name Enter D . Redirect Number Enter R . Redirect Name Enter R . Select
                                                            							 Primary/Alternate Route Primary Select Primary . | Field | Settings | Device
                                                            							 Selection | Outbound Destination | Select VoIP . | Host Group | Select the name of the VoIP host
                                                         						  group that you created for Unity Connection in Step 31 . | CPID
                                                            							 Manipulation | Calling Number | Enter S . | Calling Name | Enter S . | Called Number | Enter D . | Called Name | Enter D . | Redirect Number | Enter R . | Redirect Name | Enter R . | Select
                                                            							 Primary/Alternate Route | Primary | Select Primary . |
| Field | Settings |
| Device
                                                            							 Selection |
| Outbound Destination | Select VoIP . |
| Host Group | Select the name of the VoIP host
                                                         						  group that you created for Unity Connection in Step 31 . |
| CPID
                                                            							 Manipulation |
| Calling Number | Enter S . |
| Calling Name | Enter S . |
| Called Number | Enter D . |
| Called Name | Enter D . |
| Redirect Number | Enter R . |
| Redirect Name | Enter R . |
| Select
                                                            							 Primary/Alternate Route |
| Primary | Select Primary . |
| Step 55 | If you want to create more Inbound TDM
                                          			 rules, under Inbound TDM Rules, select Add Rule . Otherwise,
                                          			 continue to Step 57 . Note that additional Inbound TDM rules are
                                             				not necessary if you cannot use CPID manipulation. |
| Step 56 | Repeat Step 52 through Step 55 for all remaining
                                          			 inbound TDM rules that you want to create. |
| Step 57 | Select Submit . |
| Step 58 |  |
| Step 59 |  |
| Step 60 |  |
| Step 61 | On the Configuration menu, select TDM > General . |
| Step 62 | On the TDM General Settings page, enter the
                                          			 following settings. Table 17. TDM General Settings Page
                                                   				Settings Field Settings PCM Coding Select uLaw . Minimum Call Party Delay (ms) Enter 500 . Maximum Call Party Delay (ms) Enter 2000 . Dial Digit on Time (ms) Enter 100 . Dial Inter-Digit Time (ms) Enter 100 . Dial Pause Time (ms) Enter 2000 . Turn MWI On FAC Leave this field blank. Turn MWI Off FAC Leave this field blank. Outbound Call Connect Timeout (ms) Enter 10000 . Wait for Ringback/Connect on Blind
                                                         						  Transfer Select Yes . Hunt Group Extension Enter the pilot number of the Unity
                                                         						  Connection voice messaging ports. | Field | Settings | PCM Coding | Select uLaw . | Minimum Call Party Delay (ms) | Enter 500 . | Maximum Call Party Delay (ms) | Enter 2000 . | Dial Digit on Time (ms) | Enter 100 . | Dial Inter-Digit Time (ms) | Enter 100 . | Dial Pause Time (ms) | Enter 2000 . | Turn MWI On FAC | Leave this field blank. | Turn MWI Off FAC | Leave this field blank. | Outbound Call Connect Timeout (ms) | Enter 10000 . | Wait for Ringback/Connect on Blind
                                                         						  Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number of the Unity
                                                         						  Connection voice messaging ports. |
| Field | Settings |
| PCM Coding | Select uLaw . |
| Minimum Call Party Delay (ms) | Enter 500 . |
| Maximum Call Party Delay (ms) | Enter 2000 . |
| Dial Digit on Time (ms) | Enter 100 . |
| Dial Inter-Digit Time (ms) | Enter 100 . |
| Dial Pause Time (ms) | Enter 2000 . |
| Turn MWI On FAC | Leave this field blank. |
| Turn MWI Off FAC | Leave this field blank. |
| Outbound Call Connect Timeout (ms) | Enter 10000 . |
| Wait for Ringback/Connect on Blind
                                                         						  Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity
                                                         						  Connection voice messaging ports. |
| Step 63 | Select Submit . |
| Step 64 | On the Configuration menu, select TDM > Port Enable . |
| Step 65 | On the TDM Port Enabling page, select No for the ports that
                                          			 you want to disable on the PIMG unit. |
| Step 66 | Confirm that Yes is selected for all
                                          			 other ports on the PIMG unit. |
| Step 67 | Select Submit . |
| Step 68 | On the Configuration menu, select VoIP > General . |
| Step 69 | On the VoIP General Settings page, enter the
                                          			 following settings. Table 18. VoIP General Settings Page
                                                   				Settings Field Setting User-Agent Host and Domain Name Enter the host and domain name of
                                                         						  the PIMG unit. Transport Type Select UDP . Call as Domain Name Select No . Invite Expiration (sec) Enter 120 . Server DNS Server Address Enter the IP Address of the Domain
                                                         						  Name Server that the PIMG unit uses. Registration Server Address Leave this field blank. Registration Server Port Enter 5060 . Registration Expiration (sec) Enter 3600 . TCP/UDP UDP/TCP Transports Enabled Select Yes . TCP/UDP Server Port Enter 5060 . Proxy Primary Proxy Server Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the default
                                                         						  setting. Backup Proxy Server Address Not applicable. Leave the default
                                                         						  setting. Backup Proxy Server Port Not applicable. Leave the default
                                                         						  setting. Proxy Query Interval Enter 10 . Timing T1 Time (ms) Enter 400 . T2 Time (ms) Enter 3000 . Monitoring Monitor Call Connections Select No . | Field | Setting | User-Agent | Host and Domain Name | Enter the host and domain name of
                                                         						  the PIMG unit. | Transport Type | Select UDP . | Call as Domain Name | Select No . | Invite Expiration (sec) | Enter 120 . | Server | DNS Server Address | Enter the IP Address of the Domain
                                                         						  Name Server that the PIMG unit uses. | Registration Server Address | Leave this field blank. | Registration Server Port | Enter 5060 . | Registration Expiration (sec) | Enter 3600 . | TCP/UDP | UDP/TCP Transports Enabled | Select Yes . | TCP/UDP Server Port | Enter 5060 . | Proxy | Primary Proxy Server Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the default
                                                         						  setting. | Backup Proxy Server Address | Not applicable. Leave the default
                                                         						  setting. | Backup Proxy Server Port | Not applicable. Leave the default
                                                         						  setting. | Proxy Query Interval | Enter 10 . | Timing | T1 Time (ms) | Enter 400 . | T2 Time (ms) | Enter 3000 . | Monitoring | Monitor Call Connections | Select No . |
| Field | Setting |
| User-Agent |
| Host and Domain Name | Enter the host and domain name of
                                                         						  the PIMG unit. |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| Invite Expiration (sec) | Enter 120 . |
| Server |
| DNS Server Address | Enter the IP Address of the Domain
                                                         						  Name Server that the PIMG unit uses. |
| Registration Server Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration (sec) | Enter 3600 . |
| TCP/UDP |
| UDP/TCP Transports Enabled | Select Yes . |
| TCP/UDP Server Port | Enter 5060 . |
| Proxy |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default
                                                         						  setting. |
| Backup Proxy Server Address | Not applicable. Leave the default
                                                         						  setting. |
| Backup Proxy Server Port | Not applicable. Leave the default
                                                         						  setting. |
| Proxy Query Interval | Enter 10 . |
| Timing |
| T1 Time (ms) | Enter 400 . |
| T2 Time (ms) | Enter 3000 . |
| Monitoring |
| Monitor Call Connections | Select No . |
| Step 70 | Select Submit . |
| Step 71 | On the Configuration menu, select VoIP > Media . |
| Step 72 | On the VoIP Media Settings page, enter the
                                          			 following settings. Table 19. VoIP Media Settings Page
                                                   				Settings Field Settings Audio Audio Compression Select the preferred codec for audio
                                                         						  compression. RTP Digit Relay Mode Select RFC2833 . Signaling Digit Relay Mode Select Off . Voice Activity Detection Select Off . Frame Size Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence. | Field | Settings | Audio | Audio Compression | Select the preferred codec for audio
                                                         						  compression. | RTP Digit Relay Mode | Select RFC2833 . | Signaling Digit Relay Mode | Select Off . | Voice Activity Detection | Select Off . | Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence. |
| Field | Settings |
| Audio |
| Audio Compression | Select the preferred codec for audio
                                                         						  compression. |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence. |
| Step 73 | Select Submit . |
| Step 74 | On the Configuration menu, select VoIP > QOS . |
| Step 75 | On the VoIP QOS Configuration page, enter
                                          			 the following settings. Table 20. VoIP QOS Configurative Page
                                                   				Settings Field Settings Call Control QOS Byte Enter 104 . RTP QOS Byte Enter 184 . | Field | Settings | Call Control QOS Byte | Enter 104 . | RTP QOS Byte | Enter 184 . |
| Field | Settings |
| Call Control QOS Byte | Enter 104 . |
| RTP QOS Byte | Enter 184 . |
| Step 76 | Select Submit . |
| Step 77 | On the Configuration menu, select IP . |
| Step 78 | On the IP Settings page, enter the following
                                          			 settings. Table 21. IP Settings Page Settings Field Settings Client IP Address Enter the new IP address you want to
                                                         						  use for the PIMG unit. (This is the IP address that you
                                                         						  enter in Cisco Unity Connection Administration when you create the
                                                         						  integration.) Client Subnet Mask Enter the new subnet mask, if the
                                                         						  subnet mask is different from the default IP address. Default Network Gateway Address Enter the IP address of the default
                                                         						  network gateway router that the PIMG units use. BOOTP Enabled Select No . | Field | Settings | Client IP Address | Enter the new IP address you want to
                                                         						  use for the PIMG unit. (This is the IP address that you
                                                         						  enter in Cisco Unity Connection Administration when you create the
                                                         						  integration.) | Client Subnet Mask | Enter the new subnet mask, if the
                                                         						  subnet mask is different from the default IP address. | Default Network Gateway Address | Enter the IP address of the default
                                                         						  network gateway router that the PIMG units use. | BOOTP Enabled | Select No . |
| Field | Settings |
| Client IP Address | Enter the new IP address you want to
                                                         						  use for the PIMG unit. (This is the IP address that you
                                                         						  enter in Cisco Unity Connection Administration when you create the
                                                         						  integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the
                                                         						  subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default
                                                         						  network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |
| Step 79 | Select Submit . |
| Step 80 | On the Configuration menu, select Serial > General . |
| Step 81 | On the Serial Port, COM 1 page, enter the
                                          			 following settings. Table 22. Serial Port, COM 1 Page Settings Field Settings Serial Port Baud Rate Select the setting that is
                                                         						  configured on the phone system. The default setting is 9600. Serial Port Parity Select the setting that is
                                                         						  configured on the phone system. The default setting is None. Serial Port Data Bits Select the setting that is
                                                         						  configured on the phone system. The default setting is 8. Serial Port Stop Bits Select the setting that is
                                                         						  configured on the phone system. The default setting is 1. | Field | Settings | Serial Port Baud Rate | Select the setting that is
                                                         						  configured on the phone system. The default setting is 9600. | Serial Port Parity | Select the setting that is
                                                         						  configured on the phone system. The default setting is None. | Serial Port Data Bits | Select the setting that is
                                                         						  configured on the phone system. The default setting is 8. | Serial Port Stop Bits | Select the setting that is
                                                         						  configured on the phone system. The default setting is 1. |
| Field | Settings |
| Serial Port Baud Rate | Select the setting that is
                                                         						  configured on the phone system. The default setting is 9600. |
| Serial Port Parity | Select the setting that is
                                                         						  configured on the phone system. The default setting is None. |
| Serial Port Data Bits | Select the setting that is
                                                         						  configured on the phone system. The default setting is 8. |
| Serial Port Stop Bits | Select the setting that is
                                                         						  configured on the phone system. The default setting is 1. |
| Step 82 | Select Submit . |
| Step 83 | On the Configuration menu, select Serial > Switch Protocol . |
| Step 84 | On the Switch Protocol page, enter the
                                          			 following settings. Table 23. Switch Protocol Page Settings Field Settings Serial
                                                            							 Port, COM 1 Serial Mode Select the applicable setting: Master —Select this setting when this PIMG unit is
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								only one master PIMG unit in a phone system integration. Slave —Select this setting when this PIMG unit is not
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								multiple slave PIMG units in a phone system integration. Serial Interface Protocol Select the serial protocol that your
                                                         						  phone system uses: SMDI MCI MD-110 Cpid Len Select the applicable setting.
                                                         						  Typically, the settings are 7 or 10. Cpid Padding String Enter the applicable string or leave
                                                         						  this field blank. Typically, the setting is one of the following: A string of zeros, where the
                                                               								number of zeros matches the setting of the Cpid Len field. A prefix that is provided by the
                                                               								Centrex service. Voice Mail Port Len If the setting of the Serial
                                                         						  Interface Protocol field is MD-110, enter 2 . Otherwise, accept the
                                                         						  default of 7 . System Number Enter the applicable setting.
                                                         						  Typically, the setting is 1. MWI Response Timeout Enter 2000 . IP Address of Serial Server If the PIMG unit is the master, this
                                                         						  field is for display only. If the PIMG unit is a slave, enter
                                                         						  the IP address of the master PIMG unit (the PIMG unit that is connected to the
                                                         						  data link serial cable from the phone system). Serial Cpid Expiration Enter 2000 . Logical
                                                            							 Extension Number 1 If the setting of the Serial
                                                         						  Interface Protocol field is MCI or MD-110, enter the extension number for each
                                                         						  port on the PIMG unit. If the setting of the Serial
                                                         						  Interface Protocol field is SMDI, enter the logical port number. Typically, the
                                                         						  setting is 1 for port 1, 2 for port 2, and so on beginning with the master PIMG
                                                         						  unit and continuing through each of the slave PIMG units. 2 3 4 5 6 7 8 | Field | Settings | Serial
                                                            							 Port, COM 1 | Serial Mode | Select the applicable setting: Master —Select this setting when this PIMG unit is
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								only one master PIMG unit in a phone system integration. Slave —Select this setting when this PIMG unit is not
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								multiple slave PIMG units in a phone system integration. | Serial Interface Protocol | Select the serial protocol that your
                                                         						  phone system uses: SMDI MCI MD-110 | Cpid Len | Select the applicable setting.
                                                         						  Typically, the settings are 7 or 10. | Cpid Padding String | Enter the applicable string or leave
                                                         						  this field blank. Typically, the setting is one of the following: A string of zeros, where the
                                                               								number of zeros matches the setting of the Cpid Len field. A prefix that is provided by the
                                                               								Centrex service. | Voice Mail Port Len | If the setting of the Serial
                                                         						  Interface Protocol field is MD-110, enter 2 . Otherwise, accept the
                                                         						  default of 7 . | System Number | Enter the applicable setting.
                                                         						  Typically, the setting is 1. | MWI Response Timeout | Enter 2000 . | IP Address of Serial Server | If the PIMG unit is the master, this
                                                         						  field is for display only. If the PIMG unit is a slave, enter
                                                         						  the IP address of the master PIMG unit (the PIMG unit that is connected to the
                                                         						  data link serial cable from the phone system). | Serial Cpid Expiration | Enter 2000 . | Logical
                                                            							 Extension Number | 1 | If the setting of the Serial
                                                         						  Interface Protocol field is MCI or MD-110, enter the extension number for each
                                                         						  port on the PIMG unit. If the setting of the Serial
                                                         						  Interface Protocol field is SMDI, enter the logical port number. Typically, the
                                                         						  setting is 1 for port 1, 2 for port 2, and so on beginning with the master PIMG
                                                         						  unit and continuing through each of the slave PIMG units. | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| Field | Settings |
| Serial
                                                            							 Port, COM 1 |
| Serial Mode | Select the applicable setting: Master —Select this setting when this PIMG unit is
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								only one master PIMG unit in a phone system integration. Slave —Select this setting when this PIMG unit is not
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								multiple slave PIMG units in a phone system integration. |
| Serial Interface Protocol | Select the serial protocol that your
                                                         						  phone system uses: SMDI MCI MD-110 |
| Cpid Len | Select the applicable setting.
                                                         						  Typically, the settings are 7 or 10. |
| Cpid Padding String | Enter the applicable string or leave
                                                         						  this field blank. Typically, the setting is one of the following: A string of zeros, where the
                                                               								number of zeros matches the setting of the Cpid Len field. A prefix that is provided by the
                                                               								Centrex service. |
| Voice Mail Port Len | If the setting of the Serial
                                                         						  Interface Protocol field is MD-110, enter 2 . Otherwise, accept the
                                                         						  default of 7 . |
| System Number | Enter the applicable setting.
                                                         						  Typically, the setting is 1. |
| MWI Response Timeout | Enter 2000 . |
| IP Address of Serial Server | If the PIMG unit is the master, this
                                                         						  field is for display only. If the PIMG unit is a slave, enter
                                                         						  the IP address of the master PIMG unit (the PIMG unit that is connected to the
                                                         						  data link serial cable from the phone system). |
| Serial Cpid Expiration | Enter 2000 . |
| Logical
                                                            							 Extension Number |
| 1 | If the setting of the Serial
                                                         						  Interface Protocol field is MCI or MD-110, enter the extension number for each
                                                         						  port on the PIMG unit. If the setting of the Serial
                                                         						  Interface Protocol field is SMDI, enter the logical port number. Typically, the
                                                         						  setting is 1 for port 1, 2 for port 2, and so on beginning with the master PIMG
                                                         						  unit and continuing through each of the slave PIMG units. |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |
| Step 85 | Select Submit . |
| Step 86 | On the Configure menu, select Tone Detection . |
| Step 87 | On the Tone Detection page, under Call
                                          			 Progress Tone - Learn, in the Learn Tone Event field, select Busy and do the
                                          			 following substeps to verify that the tone is correct. From a available phone, call a second
                                                				  phone. Answer the second phone when it rings,
                                                				  and leave both handsets off so that both phones are busy. From a third phone, dial one of the busy
                                                				  phones. Confirm that you hear a busy tone. Hang up the third phone but leave the
                                                				  handsets for the other two phones off. |
| Step 88 | Under Call Progress Tone - Learn, in the
                                          			 Dial String field, enter the extension that you dialed in Step 87 c. from
                                          			 the third phone. |
| Step 89 | Select Learn . |
| Step 90 | On the Tone Detection page, under Call
                                          			 Progress Tone - Learn, in the Learn field, select Error and do the
                                          			 following substeps to verify that the tone is correct. From an available phone, dial an
                                                				  extension that does not exist. Confirm that you hear the reorder or
                                                				  error tone. Hang up the phone. |
| Step 91 | Under Call Progress Tone - Learn, in the
                                          			 Dial String field, enter the extension that you dialed in Step 90 a. |
| Step 92 | Select Learn . |
| Step 93 | On the Tone Detection page, under Call
                                          			 Progress Tone - Learn, in the Learn field, select Ringback and do the
                                          			 following substeps to verify that the tone is correct. From an available phone, dial an
                                                				  extension that does exist. Confirm that you hear the ringback tone. Hang up the phone. |
| Step 94 | Under Call Progress Tone - Learn, in the
                                          			 Dial String field, enter the extension that you dialed in Step 93 a. |
| Step 95 | Select Learn . |
| Step 96 | Select Submit . |
| Step 97 | Hang up the phones that you used in Step 87 . |
| Step 98 | On the System menu, select Restart . |
| Step 99 | On the Restart page, select Restart Unit Now . |
| Step 100 | Repeat Step 2 through Step 99 on all remaining PIMG
                                          			 units. |

| Field | Setting |
|---|---|
| Username | Enter admin . |
| Password | Enter IpodAdmin . |

| Field | Setting |
|---|---|
| Username | Enter admin . |
| Password | Enter IpodAdmin . |

| Note | The default RTP port range for PIMG units
                                                         				  is 49000 to 50000. Some Unity Connection configurations require a different RTP
                                                         				  port range. |
|---|---|

| Field | Setting |
|---|---|
| Username | Enter admin . |
| Password | Enter IpodAdmin . |

| Field | Setting |
|---|---|
| Old Password | Enter IpodAdmin . (This setting is
                                                         						  case sensitive.) |
| New Password | Enter your new password. (This
                                                         						  setting is case sensitive.) |
| Confirm Password | Enter your new password. (This
                                                         						  setting is case sensitive.) |

| Field | Settings |
|---|---|
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |

| Field | Settings |
|---|---|
| Name | Accept the default or enter another
                                                         						  descriptive name of the VoIP host group. |
| Load-Balanced | (Unity
                                                            							 Connection without a cluster) Select False . (Unity
                                                            							 Connection with a cluster configured) Select False . |
| Fault-Tolerant | (Unity
                                                            							 Connection without a cluster) Select False . (Unity
                                                            							 Connection with a cluster configured) Select True . |

| Field | Settings |
|---|---|
| Name | Enter All_Calls or another unique
                                                         						  name. This TDM trunk group handles all
                                                         						  calls to and from the phone system. |
| Selection Direction | Select Ascending . |
| Selection Mode | Select Linear . |
| Port/Channel Content | Enter the numbers of the PIMG ports
                                                         						  that handle all calls. For example, enter “*” for all PIMG ports, or enter
                                                         						  “1-6” for the first six PIMG ports. |

| Field | Settings |
|---|---|
| Enable | Check this check box. |
| Rule Label | Do one of the following: If you use CPID manipulation,
                                                               								enter All_UC_Calls or another
                                                               								name. This inbound VoIP rule handles all
                                                         						  outbound calls from Unity Connection. If you cannot use CPID
                                                               								manipulation, enter UC_Calls_and_Messages or
                                                               								another name. This inbound VoIP rule handles all
                                                         						  outbound calls and MWI calls from Unity Connection. |
| Request Type | Do one of the following: If you use CPID manipulation,
                                                               								select Call . If you cannot use CPID
                                                               								manipulation, select Any . |
| Originating VoIP Host Address | Enter * . |

| Field | Settings |
|---|---|
| Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |

| Field | Settings |
|---|---|
| Device
                                                            							 Selection |
| Outbound Destination | Select TDM . |
| Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.” |
| CPID
                                                            							 Manipulation |
| Calling Number | Enter S . |
| Calling Name | Enter S . |
| Called Number | Enter D . |
| Called Name | Enter D . |
| Redirect Number | Enter R . |
| Redirect Name | Enter R . |
| Select
                                                            							 Primary/Alternate Route |
| Primary | Select Primary . |

| Field | Settings |
|---|---|
| Enable | Check this check box. |
| Rule Label | Enter UC_MWIs or another name. This inbound VoIP rule handles all
                                                         						  MWIs from Unity Connection. |
| Request Type | Select Message . |
| Originating VoIP Host Address | Enter * . |

| Field | Settings |
|---|---|
| Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |

| Field | Settings |
|---|---|
| Device
                                                            							 Selection |
| Outbound Destination | Select TDM . |
| Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for outbound calls in Step 38 . For example, select
                                                         						  “All_Calls.” |
| CPID
                                                            							 Manipulation |
| Calling Number | Enter S . |
| Calling Name | Enter S . |
| Called Number | Enter D . |
| Called Name | Enter D . |
| Redirect Number | Enter R . |
| Redirect Name | Enter R . |
| Select
                                                            							 Primary/Alternate Route |
| Primary | Select Primary . |

| Field | Settings |
|---|---|
| Enable | Check this check box. |
| Rule Label | Enter Inbound_Rule_1 or another
                                                         						  name. This inbound TDM rule handles all
                                                         						  incoming calls from the phone system. |
| Request Type | Select Call . |
| Trunk Group | Select the name of the TDM trunk
                                                         						  group that you created for incoming calls from the phone system in Step 38 . For example, select
                                                         						  “All_Calls.” |

| Field | Settings |
|---|---|
| Calling Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Calling Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Called Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Number | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |
| Redirect Name | Enter the applicable matching rule
                                                         						  used. For example, enter “*” for all. |

| Field | Settings |
|---|---|
| Device
                                                            							 Selection |
| Outbound Destination | Select VoIP . |
| Host Group | Select the name of the VoIP host
                                                         						  group that you created for Unity Connection in Step 31 . |
| CPID
                                                            							 Manipulation |
| Calling Number | Enter S . |
| Calling Name | Enter S . |
| Called Number | Enter D . |
| Called Name | Enter D . |
| Redirect Number | Enter R . |
| Redirect Name | Enter R . |
| Select
                                                            							 Primary/Alternate Route |
| Primary | Select Primary . |

| Field | Settings |
|---|---|
| PCM Coding | Select uLaw . |
| Minimum Call Party Delay (ms) | Enter 500 . |
| Maximum Call Party Delay (ms) | Enter 2000 . |
| Dial Digit on Time (ms) | Enter 100 . |
| Dial Inter-Digit Time (ms) | Enter 100 . |
| Dial Pause Time (ms) | Enter 2000 . |
| Turn MWI On FAC | Leave this field blank. |
| Turn MWI Off FAC | Leave this field blank. |
| Outbound Call Connect Timeout (ms) | Enter 10000 . |
| Wait for Ringback/Connect on Blind
                                                         						  Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity
                                                         						  Connection voice messaging ports. |

| Field | Setting |
|---|---|
| User-Agent |
| Host and Domain Name | Enter the host and domain name of
                                                         						  the PIMG unit. |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| Invite Expiration (sec) | Enter 120 . |
| Server |
| DNS Server Address | Enter the IP Address of the Domain
                                                         						  Name Server that the PIMG unit uses. |
| Registration Server Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration (sec) | Enter 3600 . |
| TCP/UDP |
| UDP/TCP Transports Enabled | Select Yes . |
| TCP/UDP Server Port | Enter 5060 . |
| Proxy |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default
                                                         						  setting. |
| Backup Proxy Server Address | Not applicable. Leave the default
                                                         						  setting. |
| Backup Proxy Server Port | Not applicable. Leave the default
                                                         						  setting. |
| Proxy Query Interval | Enter 10 . |
| Timing |
| T1 Time (ms) | Enter 400 . |
| T2 Time (ms) | Enter 3000 . |
| Monitoring |
| Monitor Call Connections | Select No . |

| Field | Settings |
|---|---|
| Audio |
| Audio Compression | Select the preferred codec for audio
                                                         						  compression. |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct
                                                               								setting results in recorded messages containing nothing but silence. |

| Field | Settings |
|---|---|
| Call Control QOS Byte | Enter 104 . |
| RTP QOS Byte | Enter 184 . |

| Field | Settings |
|---|---|
| Client IP Address | Enter the new IP address you want to
                                                         						  use for the PIMG unit. (This is the IP address that you
                                                         						  enter in Cisco Unity Connection Administration when you create the
                                                         						  integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the
                                                         						  subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default
                                                         						  network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |

| Field | Settings |
|---|---|
| Serial Port Baud Rate | Select the setting that is
                                                         						  configured on the phone system. The default setting is 9600. |
| Serial Port Parity | Select the setting that is
                                                         						  configured on the phone system. The default setting is None. |
| Serial Port Data Bits | Select the setting that is
                                                         						  configured on the phone system. The default setting is 8. |
| Serial Port Stop Bits | Select the setting that is
                                                         						  configured on the phone system. The default setting is 1. |

| Field | Settings |
|---|---|
| Serial
                                                            							 Port, COM 1 |
| Serial Mode | Select the applicable setting: Master —Select this setting when this PIMG unit is
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								only one master PIMG unit in a phone system integration. Slave —Select this setting when this PIMG unit is not
                                                               								connected to the data link serial cable from the phone system. There can be
                                                               								multiple slave PIMG units in a phone system integration. |
| Serial Interface Protocol | Select the serial protocol that your
                                                         						  phone system uses: SMDI MCI MD-110 |
| Cpid Len | Select the applicable setting.
                                                         						  Typically, the settings are 7 or 10. |
| Cpid Padding String | Enter the applicable string or leave
                                                         						  this field blank. Typically, the setting is one of the following: A string of zeros, where the
                                                               								number of zeros matches the setting of the Cpid Len field. A prefix that is provided by the
                                                               								Centrex service. |
| Voice Mail Port Len | If the setting of the Serial
                                                         						  Interface Protocol field is MD-110, enter 2 . Otherwise, accept the
                                                         						  default of 7 . |
| System Number | Enter the applicable setting.
                                                         						  Typically, the setting is 1. |
| MWI Response Timeout | Enter 2000 . |
| IP Address of Serial Server | If the PIMG unit is the master, this
                                                         						  field is for display only. If the PIMG unit is a slave, enter
                                                         						  the IP address of the master PIMG unit (the PIMG unit that is connected to the
                                                         						  data link serial cable from the phone system). |
| Serial Cpid Expiration | Enter 2000 . |
| Logical
                                                            							 Extension Number |
| 1 | If the setting of the Serial
                                                         						  Interface Protocol field is MCI or MD-110, enter the extension number for each
                                                         						  port on the PIMG unit. If the setting of the Serial
                                                         						  Interface Protocol field is SMDI, enter the logical port number. Typically, the
                                                         						  setting is 1 for port 1, 2 for port 2, and so on beginning with the master PIMG
                                                         						  unit and continuing through each of the slave PIMG units. |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |

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
| Step 5 | Under Message Waiting Indicator Settings, select Use Same Port
                                             				for Enabling and Disabling MWIs . |
| Step 6 | Select Save . |
| Step 7 | On the Phone System Basics page, in the Related Links drop-down
                                          			 box, select Add Port Group and select Go . |
| Step 8 | On the New Port Group page, enter the applicable settings and
                                          			 select Save . Table 24. Settings for the New Port Group Page Field Setting Phone System Select the name of the phone system that you entered in Step 3 . Create From Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box. Display Name Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. SIP Security Profile Select 5060 . SIP Transport Protocol Select the SIP transport protocol that Unity Connection uses. IP Address or Host Name Enter the IP address of the PIMG unit that you are integrating
                                                         						  with Unity Connection. Port Enter the SIP port of the PIMG unit that Unity Connection
                                                         						  connects to. We recommend that you use the default setting. This name must match the setting in the TCP/UDP Server Port
                                                         						  field on the Configuration > VoIP > General page of the PIMG unit.
                                                         						  Otherwise, the integration cannot function correctly. | Field | Setting | Phone System | Select the name of the phone system that you entered in Step 3 . | Create From | Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box. | Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. | SIP Security Profile | Select 5060 . | SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. | IP Address or Host Name | Enter the IP address of the PIMG unit that you are integrating
                                                         						  with Unity Connection. | Port | Enter the SIP port of the PIMG unit that Unity Connection
                                                         						  connects to. We recommend that you use the default setting. This name must match the setting in the TCP/UDP Server Port
                                                         						  field on the Configuration > VoIP > General page of the PIMG unit.
                                                         						  Otherwise, the integration cannot function correctly. |
| Field | Setting |
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. |
| IP Address or Host Name | Enter the IP address of the PIMG unit that you are integrating
                                                         						  with Unity Connection. |
| Port | Enter the SIP port of the PIMG unit that Unity Connection
                                                         						  connects to. We recommend that you use the default setting. This name must match the setting in the TCP/UDP Server Port
                                                         						  field on the Configuration > VoIP > General page of the PIMG unit.
                                                         						  Otherwise, the integration cannot function correctly. |
| Step 9 | On the Port Group Basics page, under Message Waiting Indicator
                                          			 Settings, uncheck the Enable Message Waiting Indicators check box and select Save . |
| Step 10 | In the Related Links drop-down box, select Add Ports and select Go . |
| Step 11 | On the New Port page, enter the following settings and select Save . Table 25. Settings for the New Port Page Field Considerations Enabled Check this check box. Number of Ports Enter 8 . (If you want to use fewer than eight voice messaging ports,
                                                         						  enter the number of voice messaging ports that you want to use on this PIMG
                                                         						  unit.) Note For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. Phone System Select the name of the
                                                         						  phone system that you entered in Step 3 . Port Group Select the name of the
                                                         						  port group that you added in Step 8 . | Field | Considerations | Enabled | Check this check box. | Number of Ports | Enter 8 . (If you want to use fewer than eight voice messaging ports,
                                                         						  enter the number of voice messaging ports that you want to use on this PIMG
                                                         						  unit.) Note For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. | Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. | Phone System | Select the name of the
                                                         						  phone system that you entered in Step 3 . | Port Group | Select the name of the
                                                         						  port group that you added in Step 8 . |
| Field | Considerations |
| Enabled | Check this check box. |
| Number of Ports | Enter 8 . (If you want to use fewer than eight voice messaging ports,
                                                         						  enter the number of voice messaging ports that you want to use on this PIMG
                                                         						  unit.) Note For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. | Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
| Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
| Phone System | Select the name of the
                                                         						  phone system that you entered in Step 3 . |
| Port Group | Select the name of the
                                                         						  port group that you added in Step 8 . |
| Step 12 | On the Search Ports page, select the display name of the first
                                          			 voice messaging port that you created for this phone system integration. Note By default, the display names for the voice messaging ports are
                                                         				  composed of the port group display name followed by incrementing numbers. | Note | By default, the display names for the voice messaging ports are
                                                         				  composed of the port group display name followed by incrementing numbers. |
| Note | By default, the display names for the voice messaging ports are
                                                         				  composed of the port group display name followed by incrementing numbers. |
| Step 13 | On the Port Basics page, set the voice messaging port settings
                                          			 as applicable. The fields in the following table are the ones that you can
                                          			 change. Table 26. Settings for the Voice Messaging Ports Field Considerations Enabled Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. Extension Enter the extension for
                                                         						  the port as assigned on the phone system. Answer Calls Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. Perform Message
                                                         						  Notification Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. Send MWI Requests (Serial integrations only) Uncheck this check box.
                                                         						  Otherwise, the integration may not function correctly. (Digital and analog integrations only) Check this check
                                                         						  box to designate the port for turning MWIs on and off. Assign Send MWI Requests
                                                         						  to the least busy ports Allow TRAP Connections Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. Outgoing Hunt Order Enter the priority order
                                                         						  in which Unity Connection uses the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection uses
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
                                                         						  Notification to the least busy ports. | Send MWI Requests | (Serial integrations only) Uncheck this check box.
                                                         						  Otherwise, the integration may not function correctly. (Digital and analog integrations only) Check this check
                                                         						  box to designate the port for turning MWIs on and off. Assign Send MWI Requests
                                                         						  to the least busy ports | Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. | Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection uses the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection uses
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
| Send MWI Requests | (Serial integrations only) Uncheck this check box.
                                                         						  Otherwise, the integration may not function correctly. (Digital and analog integrations only) Check this check
                                                         						  box to designate the port for turning MWIs on and off. Assign Send MWI Requests
                                                         						  to the least busy ports |
| Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. |
| Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection uses the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection uses
                                                         						  the port that has been idle the longest. |
| Step 14 | Select Save . |
| Step 15 | Select Next . |
| Step 16 | Repeat Step 13 through Step 15 for all
                                          			 remaining voice messaging ports for the phone system. |
| Step 17 | In Cisco Unity Connection Administration, expand Telephony
                                             				Integrations , then select Phone System . |
| Step 18 | On the Search Phone Systems page, under Display Name, select the
                                          			 name of the phone system that you entered in Step 3 . |
| Step 19 | Repeat Step 7 through Step 18 for each
                                          			 remaining PIMG unit integrated with Unity Connection. Note Each PIMG unit is connected to one port group with the
                                                         				  applicable voice messaging ports. For example, a system that uses five PIMG
                                                         				  units requires five port groups, one port group for each PIMG unit. | Note | Each PIMG unit is connected to one port group with the
                                                         				  applicable voice messaging ports. For example, a system that uses five PIMG
                                                         				  units requires five port groups, one port group for each PIMG unit. |
| Note | Each PIMG unit is connected to one port group with the
                                                         				  applicable voice messaging ports. For example, a system that uses five PIMG
                                                         				  units requires five port groups, one port group for each PIMG unit. |
| Step 20 | To create a port group for MWIs, do the following substeps. Note All MWI requests are handled by the master PIMG unit and sent
                                                      				to the phone system over the RS-232 serial cable (without using voice messaging
                                                      				ports). So the following substeps create a separate port group without voice
                                                      				messaging ports and enable the port group for MWIs that are "not port specific"
                                                      				(they do not use ports). In Cisco Unity Connection Administration expand Telephony Integration then select Port Group . On the Search Port Groups page, select Add New . On the New Port Group page, enter the applicable settings and
                                                				  select Save . Table 27. Settings for the New Port Group Page (MWIs) Field Setting Phone System Select the name of the phone system
                                                            							 that you entered in Step 3. Create From Select Port Group Template and select SIP to DMG/PIMG/TIMG SIP to in the drop-down box. Display Name Enter a MWI Port Group or another descriptive name for the
                                                            							 port group. SIP Security Profile Select 5060 . SIP Transport Protocol Select the SIP transport protocol that
                                                            							 Unity Connection uses. IPv4 Address or Host Name Enter the IP address of the master PIMG
                                                            							 unit. IPv6 Address or Host Name Do not enter a value in this field.
                                                            							 IPv6 is not supported for PIMG integrations. IP Address or Host Name Enter the IP address of the master PIMG
                                                            							 unit. Port Enter the SIP port of the master PIMG
                                                            							 unit. Caution This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. On the Port Group Basics page, on the Edit menu, select Advanced Settings . On the Edit Advanced Settings page, under SIP MWI Requests,
                                                				  select Not Port Specific then select Save . On the Edit menu, select Port Group Basics . Under Port Group, select Reset . Under Message Waiting Indicator Settings, confirm that the Enable Message Waiting Indicator check box is checked and
                                                				  select Save . | Note | All MWI requests are handled by the master PIMG unit and sent
                                                      				to the phone system over the RS-232 serial cable (without using voice messaging
                                                      				ports). So the following substeps create a separate port group without voice
                                                      				messaging ports and enable the port group for MWIs that are "not port specific"
                                                      				(they do not use ports). | Field | Setting | Phone System | Select the name of the phone system
                                                            							 that you entered in Step 3. | Create From | Select Port Group Template and select SIP to DMG/PIMG/TIMG SIP to in the drop-down box. | Display Name | Enter a MWI Port Group or another descriptive name for the
                                                            							 port group. | SIP Security Profile | Select 5060 . | SIP Transport Protocol | Select the SIP transport protocol that
                                                            							 Unity Connection uses. | IPv4 Address or Host Name | Enter the IP address of the master PIMG
                                                            							 unit. | IPv6 Address or Host Name | Do not enter a value in this field.
                                                            							 IPv6 is not supported for PIMG integrations. | IP Address or Host Name | Enter the IP address of the master PIMG
                                                            							 unit. | Port | Enter the SIP port of the master PIMG
                                                            							 unit. Caution This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. | Caution | This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. |
| Note | All MWI requests are handled by the master PIMG unit and sent
                                                      				to the phone system over the RS-232 serial cable (without using voice messaging
                                                      				ports). So the following substeps create a separate port group without voice
                                                      				messaging ports and enable the port group for MWIs that are "not port specific"
                                                      				(they do not use ports). |
| Field | Setting |
| Phone System | Select the name of the phone system
                                                            							 that you entered in Step 3. |
| Create From | Select Port Group Template and select SIP to DMG/PIMG/TIMG SIP to in the drop-down box. |
| Display Name | Enter a MWI Port Group or another descriptive name for the
                                                            							 port group. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that
                                                            							 Unity Connection uses. |
| IPv4 Address or Host Name | Enter the IP address of the master PIMG
                                                            							 unit. |
| IPv6 Address or Host Name | Do not enter a value in this field.
                                                            							 IPv6 is not supported for PIMG integrations. |
| IP Address or Host Name | Enter the IP address of the master PIMG
                                                            							 unit. |
| Port | Enter the SIP port of the master PIMG
                                                            							 unit. Caution This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. | Caution | This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. |
| Caution | This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. |
| Step 21 | If another phone system integration exists, in Cisco Unity
                                          			 Connection Administration, expand Telephony
                                             				Integrations , then select Trunk .
                                          			 Otherwise, skip to Step 25 . |
| Step 22 | On the Search Phone System Trunks page, on the Phone System
                                          			 Trunk menu, select New Phone System
                                             				Trunk . |
| Step 23 | On the New Phone System Trunk page, enter the following settings
                                          			 for the phone system trunk and select Save . Table 28. Settings for the Phone System Trunk Field Setting From Phone System Enter the display name of
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
| Step 24 | Repeat Step 22 and Step 23 for all
                                          			 remaining phone system trunks that you want to create. |
| Step 25 | In the Related Links drop-down list, select Check Telephony
                                             				Configuration and select Go to confirm
                                          			 the phone system integration settings. If the test is not successful, the Task Execution Results
                                             				displays one or more messages with troubleshooting steps. After correcting the
                                             				problems, test the connection again. |
| Step 26 | In the Task Execution Results window, select Close . |

| Field | Setting |
|---|---|
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                                         						  select SIP to DMG/PIMG/TIMG in the drop-down box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. |
| IP Address or Host Name | Enter the IP address of the PIMG unit that you are integrating
                                                         						  with Unity Connection. |
| Port | Enter the SIP port of the PIMG unit that Unity Connection
                                                         						  connects to. We recommend that you use the default setting. This name must match the setting in the TCP/UDP Server Port
                                                         						  field on the Configuration > VoIP > General page of the PIMG unit.
                                                         						  Otherwise, the integration cannot function correctly. |

| Field | Considerations |
|---|---|
| Enabled | Check this check box. |
| Number of Ports | Enter 8 . (If you want to use fewer than eight voice messaging ports,
                                                         						  enter the number of voice messaging ports that you want to use on this PIMG
                                                         						  unit.) Note For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. | Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
| Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
                                                                     							 all voice messaging traffic for the cluster if one of the servers stops
                                                                     							 functioning. For example, if the phone system is set up with 16 voice messaging
                                                                     							 ports, this server must have 16 voice messaging ports. |
| Phone System | Select the name of the
                                                         						  phone system that you entered in Step 3 . |
| Port Group | Select the name of the
                                                         						  port group that you added in Step 8 . |

| Note | For a Unity Connection
                                                                     							 cluster, the server must have the number of voice messaging ports that are set
                                                                     							 up on the phone system for the PIMG integration so that this server can handle
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
| Send MWI Requests | (Serial integrations only) Uncheck this check box.
                                                         						  Otherwise, the integration may not function correctly. (Digital and analog integrations only) Check this check
                                                         						  box to designate the port for turning MWIs on and off. Assign Send MWI Requests
                                                         						  to the least busy ports |
| Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. |
| Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection uses the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection uses
                                                         						  the port that has been idle the longest. |

| Note | Each PIMG unit is connected to one port group with the
                                                         				  applicable voice messaging ports. For example, a system that uses five PIMG
                                                         				  units requires five port groups, one port group for each PIMG unit. |
|---|---|

| Note | All MWI requests are handled by the master PIMG unit and sent
                                                      				to the phone system over the RS-232 serial cable (without using voice messaging
                                                      				ports). So the following substeps create a separate port group without voice
                                                      				messaging ports and enable the port group for MWIs that are "not port specific"
                                                      				(they do not use ports). |
|---|---|

| Field | Setting |
|---|---|
| Phone System | Select the name of the phone system
                                                            							 that you entered in Step 3. |
| Create From | Select Port Group Template and select SIP to DMG/PIMG/TIMG SIP to in the drop-down box. |
| Display Name | Enter a MWI Port Group or another descriptive name for the
                                                            							 port group. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that
                                                            							 Unity Connection uses. |
| IPv4 Address or Host Name | Enter the IP address of the master PIMG
                                                            							 unit. |
| IPv6 Address or Host Name | Do not enter a value in this field.
                                                            							 IPv6 is not supported for PIMG integrations. |
| IP Address or Host Name | Enter the IP address of the master PIMG
                                                            							 unit. |
| Port | Enter the SIP port of the master PIMG
                                                            							 unit. Caution This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. | Caution | This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. |
| Caution | This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. |

| Caution | This name must match the setting in
                                                                        								the TCP/UDP Server Port field on the Configuration > VoIP > General page
                                                                        								of the PIMG unit. Otherwise, the integration cannot function correctly. |
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