---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-adminguide-cs38-bk-ad57597a-00-adminguide-8831-cs-5dd5521ca7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/AdminGuide/CS38_BK_AD57597A_00_adminguide-8831/CS38_BK_AD57597A_00_adminguide-8831_chapter_011.html
retrieved_at: 2026-08-21T13:37:53.338481+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

# Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

Updated: November 17, 2014

Chapter: Cisco Unified IP
	 Conference Phone Installation

## Chapter: Cisco Unified IP
	 Conference Phone Installation

# Cisco Unified IP
                     	 Conference Phone Installation

## Cisco Unified IP
                        	 Conference Phone Installation Overview

This chapter helps you set up and install the Cisco Unified IP
                           		Conference Phone on an IP telephony network.

Before you install a conference phone, you must decide how to
                                       		  configure the conference phone in your network. After you have determined your
                                       		  configuration requirements, you can install the conference phone and verify its
                                       		  functionality. For more information, see Cisco Unified IP Phones and Telephony Networks

## Before You
                        	 Begin

Before you install
                           		the conference phone, review the requirements in the following sections.

### Network
                           	 Requirements

For the Cisco
                              		Unified IP Conference Station to successfully operate as an endpoint in your
                              		network, your network must meet these requirements:

VoIP network:

VoIP
                                             				  configured on your Cisco routers and gateways

Cisco
                                             				  Unified Communications Manager installed in your network and configured to
                                             				  handle call processing

IP network:

Support for
                                             				  Dynamic Host Configuration Protocol (DHCP) or manual assignment of IP address,
                                             				  gateway, and subnet mask

### Cisco Unified
                           	 Communications Manager Setup

The conference
                              		phone requires Cisco Unified Communications Manager to handle call
                              		processing. See the Cisco Unified
                                 		  Communications Manager Administration Guide or to context-sensitive help
                              		in the Cisco Unified Communications Manager application to ensure that Cisco
                              		Unified Communications Manager is correctly setup to manage the conference
                              		phone and to properly route and process calls.

If you plan to use
                              		autoregistration, verify that it is enabled and properly configured in Cisco
                              		Unified Communications Manager before connecting any conference station to the
                              		network. For information about enabling and configuring autoregistration, see Cisco Unified
                                 		  Communications Manager Administration Guide .

You must use Cisco
                              		Unified Communications Manager to configure and assign telephony features to
                              		the conference phones.

In Cisco Unified
                              		Communications Manager, you can add users to the database, add users to user
                              		groups, and associate users with specific conference phones. In this way,
                              		users gain access to Cisco Unified Communications Self Care Portal that allow
                              		them to configure items such as call forwarding and voice
                              		messaging system options.

### Wireless
                           	 Microphone Region Setting

The
                                 		  Wireless Microphone Frequency Lock feature provides a secure DECT frequency for
                                 		  wireless microphones by locking down the Wireless Region setting. The Cisco
                                 		  Unified IP Conference Phone 8831 is shipped from the manufacturer with the mask
                                 		  and the Wireless Region setting configured for your region.

The Cisco Unified IP Conference Phone 8831NR does not support wireless microphones.

For
                                 		  additional information, see Cisco Unified IP Conference Phone 8831 Release Notes for Firmware
                                    			 Release 10.3(1) .

### Safety

Review the following warnings before installing the conference station. To see translations of these warnings, see the Regulatory
                                 Compliance and Safety Information for Cisco Unified IP Conference Stations document that accompanied this device.

Read the installation instructions before you connect the system to its power source.

Only trained and qualified personnel should be allowed to install, replace, or service this equipment.

Ultimate disposal of this product should be handled according to all national laws and regulations.

Do not work on the system or connect or disconnect cables during periods of lightning activity.

To avoid electric shock, do not connect safety extra low voltage (SELV) circuits to teleconference station network voltage
                                             (TNV) circuits. LAN ports contain SELV circuits, and WAN ports contain TNV circuits. Some LAN and WAN ports both use RJ-45
                                             connectors. Use caution when connecting cables.

The following warnings apply when you use an external power supply.

This product relies on the building's installation for short-circuit (overcurrent) protection. Ensure that a fuse or circuit
                                             breaker no larger than 120 VAC, 15 A U.S. (240 VAC, 10 A international) is used on the phase conductors (all current-carrying
                                             conductors

The device is designed to work with TN power systems.

The plug-socket combination must be accessible at all times because it serves as the main disconnecting device.

## Cisco Unified IP
                        	 Conference Phone Components

The Cisco Unified IP
                           		Conference Phone includes these components on the conference phone or as
                           		accessories for the conference phone.

### Network
                           	 Ports

The underside of the
                              		conference phone sound base has a single network port. This port is labeled
                              		LAN.

Your conference
                              		phone has a 10/100 Base-T autosensing Ethernet port. This port supports Mbps
                              		half- or full-duplex connections to external devices. You can use either
                              		Category 3 or 5, or 5e cabling for 10-Mbps connections, but you must use
                              		Category 5 or 5e for 100 Mbps connections.

Use the ethernet
                              		network port to connect the conference phone to the network. You must use a
                              		straight-through cable on this port. The conference phone can also obtain
                              		inline power from a switch over this connection (PoE).

### Wired Extension
                           	 Microphone Kit

The optional wired
                              		extension microphone kit includes two wired omni-directional microphones.
                              		Connecting a microphone kit enhances the room coverage of the conference phone.
                              		The sound base has two wired microphone ports and you can connect one or both
                              		wired microphones.

If the conference
                              		phone is connected to another sound base in Linked Mode, the primary base
                              		station supports one or two wireless microphones, or it supports one wired
                              		microphone. The secondary unit supports only one wired microphone; a wireless
                              		microphone cannot be connected to a secondary Sound Base. You cannot mix
                              		microphone kits: if you plan to connect a microphone to both sound bases, they
                              		must both be wired microphones.

Wired and wireless
                                          		  microphones cannot be used at the same time, and the wireless microphones have
                                          		  a higher priority. Attempting to connect a wired microphone to a conference
                                          		  phone that has paired or connected channels results in a warning to the user
                                          		  that the wired microphone is disabled. To solve this problem, unpair any paired
                                          		  or connected wireless microphones before connecting a wired microphone.

1

Mute button.

### Wireless Extension
                           	 Microphone Kit

The optional
                              		wireless microphone extension kit enhances the room coverage of the conference
                              		phone. Two wireless microphones can be paired to the conference phone.

The Cisco Unified IP Conference Phone 8831NR does not support wireless microphones.

Wireless microphones
                              		support an 8-hour call before the battery requires charging. The charger is
                              		separate device, and is not connected to the conference phone.

LEDs on the wireless
                              		microphone base indicate the connection status of the microphone, and an icon
                              		will also be displayed on the conference phone screen. The LEDs and the display
                              		screen also indicate the mute status of the wireless microphone.

If your conference
                              		phone is to be configured to use wireless extension microphones, you can access
                              		the configuration menu from the conference phone by choosing Apps > Admin
                                    			 Settings > Wireless Microphones . From this menu,
                              		the user can choose which channel to set in pairing mode, initiate the pairing
                              		process, and set the wireless microphone range.

Low

Medium

High

If the conference phone is connected to another sound base in Linked Mode, the primary base station supports one or two wireless
                              microphones, or it supports one wired microphone. The secondary unit supports only one wired microphone; a wireless microphone
                              cannot be connected to a secondary Sound Base. You cannot mix microphone kits: if you plan to connect a microphone to both
                              sound bases, they must both be wired microphones.

Wired and wireless
                                          		  microphones cannot be used at the same time, and the wireless microphones have
                                          		  a higher priority. Attempting to connect a wired microphone to a conference
                                          		  phone that has paired or connected channels results in a warning to the user
                                          		  that the wired microphone is disabled. To solve this problem, unpair any paired
                                          		  or connected wireless microphones before connecting a wired microphone.

## Cisco Unified IP Conference Phone Setup

You must connect the
                           		
                           		Cisco Unified IP Conference Phone to the network and to a power source
                           		before using it.

Before connecting
                                       		  the ethernet cable to the device, you must first install a ferrite bead on the
                                       		  ethernet cable.

Before you install
                                       		  a conference phone or phone, even if it is new, upgrade the device to the
                                       		  current firmware image. Before using external devices, see the Readme file for
                                       		  safety and performance information.

See Buttons and Hardware for a diagram of the connections
                           		for the 
                           		Cisco Unified IP Conference Phone.

### Phone
                           	 Connections

The Sound Base
                                 		  contains the network and power connection for the phone. The base also contains
                                 		  the mini-USB connection for the DCS, the wired microphone ports, and the daisy
                                 		  chain port for the Linked Mode feature.

1

Network
                                             					 port

Network
                                             					 port (10/100 SW) connection. IEEE 802.3af power enabled.

2

Wall power

Local
                                             					 power connection.

3

Mini USB
                                             					 port

Connects
                                             					 the base station to the DCU.

When
                                                         						connecting the USB cable, firmly press down on the ferrite bead to ensure it
                                                         						seats correctly between the posts.

4

Wired
                                             					 microphone ports

Two RJ11
                                             					 microphone ports. An optional wired microphone can be connected to each port.

5

Linked
                                             					 Mode daisy chain port

Supports
                                             					 the connection of two base stations in Linked Mode.

#### Connect Mini-USB
                              	 Cable to DCU

Insert the
                                             			 mini-USB connector into the port on the base of the phone.

Seat the
                                             			 ferrite bead between the posts and press the bead down firmly.

Thread the
                                             			 cable in the cable channel. Make sure that you leave some slack in the cable.

#### Install Ferrite
                              	 Bead on Network Cable

Align the
                                             			 ferrite bead with the head of the network cable and move the ferrite bead along
                                             			 the cable until there is a gap of 1.0 mm +/- 0.3 mm between the bead and the
                                             			 connector.

Place the
                                             			 cable into the ferrite bead channel and loop the cable around the ferrite bead
                                             			 so that the cable exits the bottom of the bead.

Hold the cable
                                             			 in the ferrite bead channel and close the ferrite bead. Snap the latch closed.

### Install Cisco Unified IP Conference Phone

Before you install a conference phone, even if it is new, upgrade the conference phone  to
                                             			 the current firmware image. Before using external devices, see the Readme file  for safety
                                             			 and performance information.

Connect the power supply to the Cisco DC
                                          			 Adapter port. See the Power Guidelines for more information about powering your conference phone.

Connect a straight-through Ethernet cable from the switch to the
                                          			 network port on the 
                                          			 conference phone. Each Cisco Unified IP Conference Phone 8831 ships with one
                                          			 ethernet cable in the box.

You can use either Category 3, 5, or 5e cabling for 10-Mbps
                                             				connections, but you must use Category 5 or 5e for 100 Mbps connections.

See Network Ports for guidelines.

(Optional) Connect wired extension microphones.

### Performance
                           	 Guidelines

Follow these
                              		guidelines to ensure optimum performance with the conference phone and the
                              		wired or wireless extension microphones if they are connected.

Use the
                                    			 conference phone in closed offices and conference rooms up to 20 feet by 20
                                    			 feet (without external microphones) and 20 feet by 30 feet (with external
                                    			 microphones).

Place the
                                    			 conference phone base on a flat surface and make sure that it is clear from any
                                    			 reflective surfaces.

Maintain a
                                    			 minimum distance of four feet between each external microphone and the
                                    			 conference phone base and other objects.

Make sure that
                                    			 all microphones are acoustically unobstructed.

Position the
                                    			 external microphones toward the areas that need to be covered, and so that the
                                    			 main pickup direction is pointed away from the conference phone.

Seat all
                                    			 conference participants the same distance from the conference phone.

Speak at normal
                                    			 conversation levels and direct your voice toward the conference phone.

Do not move or
                                    			 handle the conference phone base or the external microphones while on a call,
                                    			 and do not shuffle papers near the equipment.

Minimize
                                    			 background noise from air conditioning units, fans, or other equipment in the
                                    			 office or conference room.

### Wireless
                           	 Microphone Menu

The Wireless
                                 		  Microphone menu provides options for setting the pairing and range options for
                                 		  the wireless expansion microphones. A maximum of two wireless microphones can
                                 		  be paired with the conference station at a time.

The Cisco Unified IP Conference Phone 8831NR does not support wireless microphones.

To access the
                                 		  Wireless Microphone menu, navigate to Apps > Admin
                                       				Settings > Wireless Microphones .

The following
                                 		  table describes the Wireless Microphone Options and, where applicable, explains
                                 		  how to change them.

Wireless
                                             					 Microphone 1

The
                                             					 channel that can be used to pair the first microphone.

See Pair Wireless Microphone or Unpair Wireless Microphone

Wireless
                                             					 Microphone 2

The
                                             					 channel that can be used to pair the second microphone.

See Pair Wireless Microphone or Unpair Wireless Microphone

Wireless
                                             					 Microphone Range

Sets the
                                             					 baseband power and effective RF range for the wireless microphones.

The RF
                                             					 range can be set to

Low

Medium

High

Select
                                             					 Low, Medium or High, and press Select . Or press Default to select the default setting and press Select .

#### Pair Wireless
                              	 Microphone

##### Before you begin

The microphone
                                    		  must be in the off state before you can pair it to the conference station. A
                                    		  microphone is off if the microphone's LED is off. To turn off the wireless
                                    		  microphone, hold down the microphone button until the microphone LED turns
                                    		  solid red, then release.

Choose Apps > Admin
                                                   				  Settings > Wireless Microphones .

Select either
                                             			 Wireless Microphone 1 or Wireless Microphone 2.

If the
                                                				selected channel is available, a Pair microphone 1? or Pair microphone 2? prompt displays, and the Pair softkey displays.

If a
                                                				microphone is already linked to a particular channel, pairing cannot be
                                                				initiated on the selected channel and the dialog shows that the microphone is
                                                				linked.

Press Pair .

If the channel
                                                				is ready to pair, the pairing process begins and a text message displays.

Put the
                                             			 microphone that corresponds to the selected channel in pairing mode by pressing
                                             			 the microphone's Mute button until the LED lights solid red.

If pairing
                                                				succeeds, the screen reverts to the Wireless Microphones Menu, and the message Mic X Paired Successfully! displays.

If pairing
                                                				times out or fails, the status is updated and you can cancel or retry.

Press Cancel to revert to the Wireless Microphones Menu.

Press Retry to start the pairing process again.

#### Unpair Wireless
                              	 Microphone

If you need to
                                    		  connect a wired microphone to the conference station, any wireless microphones
                                    		  must be unpaired first. You can also use this procedure to unpair a microphone
                                    		  that is no longer in use.

This option is
                                                			 not available if the microphone is connected. To enable the unpair command,
                                                			 place the wireless microphone in its charger or turn it off.

Choose Applications > Admin
                                                   				  Settings > Wireless Microphones .

Select either
                                             			 Wireless Microphone 1 or Wireless Microphone 2.

If the
                                                				selected channel is paired, the Unpair softkey displays.

Press Unpair .

A verification
                                                				prompt with the options to Cancel or Unpair displays.

Press Unpair to continue to unpair the microphone.

The
                                                				microphone channel's registration information in the base deletes. If you view
                                                				the microphone channel's status in phone info menu, the status value and RFID
                                                				are empty.

Press return
                                             			 to revert to the wireless microphones menu and stop the process.

## IP Phone Startup
                        	 Verification

After the
                           		conference phone has power connected to it, it begins the startup diagnostic
                           		process by cycling through the following steps.

The specified
                                 			 LED buttons flash on and off during the various stages of boot up as the
                                 			 conference phone checks its hardware. See the following table for a list of the
                                 			 hardware test and the LED diagnostic status.

Hardware Test

Sound Base
                                             				LEDs

DCU LEDs

Power is Ready

Green LEDs
                                             				flash

Red and Green
                                             				LEDs flash

Flash is
                                             				Accessible

Green LEDs
                                             				flash

Red and Green
                                             				LEDs flash

RAM Test
                                             				Successful

Green LEDs
                                             				flash

Red and Green
                                             				LEDs flash

Ethernet Test
                                             				Successful

—

—

The screen displays
                                 		the Cisco Systems, Inc., logo screen.

The screen displays
                                 		the Revolabs, Inc., splash screen

This message appears
                                 		as the conference phone starts up.

Phone is not
                                          				registered

The home screen
                                 		displays:

Current date and
                                       			 time

Primary
                                       			 directory number

Softkeys

If the
                           	 conference phone successfully passes through these stages, it has started up
                           	 properly. If the conference phone does not start up properly, see Startup Problems .

## Network
                        	 Settings

If you are not using
                           		DHCP in your network, you must configure these network settings on the
                           		conference phone after installing it on the network:

IP address

IP subnet
                                 			 information (subnet mask)

TFTP server IP
                                 			 address

You also may
                                 			 configure the domain name and the DNS server settings, if necessary.

Collect this
                           		information before you start to configure the conference phone.

## Cisco Unified IP
                        	 Phone Security

The
                           		security features protect against several threats, including threats to the
                           		identity of the conference phone and to data. These features establish and
                           		maintain secure communication streams between the conference phone and the Cisco Unified
                              				Communications Manager server, and digitally sign files
                           		before they are delivered.

For more
                           		information about the security features, see Cisco Unified IP Conference Phone Security Features and also consult the Cisco Unified
                                 				Communications Manager Security Guide .

### Set Up Locally
                           	 Significant Certificate

You can
                                 		  initiate the installation of a Locally Significant Certificate (LSC) from the
                                 		  Security Configuration menu on the conference phone. This menu also lets you
                                 		  update or remove an LSC.

To
                                 		  manually configure an LSC on the conference phone, perform these steps:

#### Before you begin

Ensure
                                 		  that the appropriate Cisco Unified Communications Manager and the Certificate
                                 		  Authority Proxy Function (CAPF) security configurations are complete:

- The CTL file should have a
                                    			 CAPF certificate.

- On Cisco Unified
                                    			 Communications Operating System Administration, verify that the CAPF
                                    			 certificate has been installed.

- The CAPF is running and
                                    			 configured.

For more
                                 		  information, see Cisco Unified
                                    			 Communications Manager Security Guide .

Obtain the
                                          			 CAPF authentication code that was set when the CAPF was configured.

From the
                                          			 phone, choose Apps > Admin
                                                				  Settings > Security Configuration .

You can
                                                         				  control access to the Administrator Settings Menu by using the Settings Access
                                                         				  field in the Cisco Unified Communications Manager Administration Device
                                                         				  Configuration window. For more information, see the Cisco
                                                            					 Unified Communications Manager Administration Guide .

Scroll to LSC
                                          			 and press Update .

The conference
                                             				phone prompts for an authentication string.

Enter the
                                          			 authentication code and press Submit .

The conference
                                             				phone begins to install, update, or remove the LSC, depending on how the CAPF
                                             				was configured. During the procedure, a notification message is displayed so
                                             				that you can monitor progress.

The LSC
                                             				install, update, or removal process can take a long time to complete. You can
                                             				stop the process at any time by pressing Exit .

You can verify
                                             				that an LSC is installed on the conference phone by choosing Apps > Admin
                                                   					 Settings > Security Setup and ensuring that the
                                             				LSC setting shows Installed .

| Note | Before you install a conference phone, you must decide how to
                                       		  configure the conference phone in your network. After you have determined your
                                       		  configuration requirements, you can install the conference phone and verify its
                                       		  functionality. For more information, see Cisco Unified IP Phones and Telephony Networks |
|---|---|

| Note | The conference
                                          		  phone displays the data and time from Cisco Unified Communications Manager. If
                                          		  the Cisco Unified Communications Manager server is located in a different time
                                          		  zone than the conference stations, the conference stations do no display the
                                          		  correct local time. |
|---|---|

| Attention | Read the installation instructions before you connect the system to its power source. |
|---|---|

| Attention | Only trained and qualified personnel should be allowed to install, replace, or service this equipment. |
|---|---|

| Attention | Ultimate disposal of this product should be handled according to all national laws and regulations. |
|---|---|

| Attention | Do not work on the system or connect or disconnect cables during periods of lightning activity. |
|---|---|

| Caution | To avoid electric shock, do not connect safety extra low voltage (SELV) circuits to teleconference station network voltage
                                             (TNV) circuits. LAN ports contain SELV circuits, and WAN ports contain TNV circuits. Some LAN and WAN ports both use RJ-45
                                             connectors. Use caution when connecting cables. |
|---|---|

| Attention | This product relies on the building's installation for short-circuit (overcurrent) protection. Ensure that a fuse or circuit
                                             breaker no larger than 120 VAC, 15 A U.S. (240 VAC, 10 A international) is used on the phase conductors (all current-carrying
                                             conductors |
|---|---|

| Attention | The device is designed to work with TN power systems. |
|---|---|

| Attention | The plug-socket combination must be accessible at all times because it serves as the main disconnecting device. |
|---|---|

| Note | Wired and wireless
                                          		  microphones cannot be used at the same time, and the wireless microphones have
                                          		  a higher priority. Attempting to connect a wired microphone to a conference
                                          		  phone that has paired or connected channels results in a warning to the user
                                          		  that the wired microphone is disabled. To solve this problem, unpair any paired
                                          		  or connected wireless microphones before connecting a wired microphone. |
|---|---|

| Item | Description |
|---|---|
| 1 | Mute button. |

| Note | Wired and wireless
                                          		  microphones cannot be used at the same time, and the wireless microphones have
                                          		  a higher priority. Attempting to connect a wired microphone to a conference
                                          		  phone that has paired or connected channels results in a warning to the user
                                          		  that the wired microphone is disabled. To solve this problem, unpair any paired
                                          		  or connected wireless microphones before connecting a wired microphone. |
|---|---|

| Note | Before connecting
                                       		  the ethernet cable to the device, you must first install a ferrite bead on the
                                       		  ethernet cable. |
|---|---|

| Note | Before you install
                                       		  a conference phone or phone, even if it is new, upgrade the device to the
                                       		  current firmware image. Before using external devices, see the Readme file for
                                       		  safety and performance information. |
|---|---|

|  | Item | Description |
|---|---|---|
| 1 | Network
                                             					 port | Network
                                             					 port (10/100 SW) connection. IEEE 802.3af power enabled. |
| 2 | Wall power | Local
                                             					 power connection. |
| 3 | Mini USB
                                             					 port | Connects
                                             					 the base station to the DCU. Attention When
                                                         						connecting the USB cable, firmly press down on the ferrite bead to ensure it
                                                         						seats correctly between the posts. | Attention | When
                                                         						connecting the USB cable, firmly press down on the ferrite bead to ensure it
                                                         						seats correctly between the posts. |
| Attention | When
                                                         						connecting the USB cable, firmly press down on the ferrite bead to ensure it
                                                         						seats correctly between the posts. |
| 4 | Wired
                                             					 microphone ports | Two RJ11
                                             					 microphone ports. An optional wired microphone can be connected to each port. |
| 5 | Linked
                                             					 Mode daisy chain port | Supports
                                             					 the connection of two base stations in Linked Mode. |

| Attention | When
                                                         						connecting the USB cable, firmly press down on the ferrite bead to ensure it
                                                         						seats correctly between the posts. |
|---|---|

| Step 1 | Insert the
                                             			 mini-USB connector into the port on the base of the phone. |
|---|---|
| Step 2 | Seat the
                                             			 ferrite bead between the posts and press the bead down firmly. |
| Step 3 | Thread the
                                             			 cable in the cable channel. Make sure that you leave some slack in the cable. |

| Step 1 | Align the
                                             			 ferrite bead with the head of the network cable and move the ferrite bead along
                                             			 the cable until there is a gap of 1.0 mm +/- 0.3 mm between the bead and the
                                             			 connector. |
|---|---|
| Step 2 | Place the
                                             			 cable into the ferrite bead channel and loop the cable around the ferrite bead
                                             			 so that the cable exits the bottom of the bead. |
| Step 3 | Hold the cable
                                             			 in the ferrite bead channel and close the ferrite bead. Snap the latch closed. |

| Note | Before you install a conference phone, even if it is new, upgrade the conference phone  to
                                             			 the current firmware image. Before using external devices, see the Readme file  for safety
                                             			 and performance information. |
|---|---|

| Step 1 | Connect the power supply to the Cisco DC
                                          			 Adapter port. See the Power Guidelines for more information about powering your conference phone. |
|---|---|
| Step 2 | Connect a straight-through Ethernet cable from the switch to the
                                          			 network port on the 
                                          			 conference phone. Each Cisco Unified IP Conference Phone 8831 ships with one
                                          			 ethernet cable in the box. You can use either Category 3, 5, or 5e cabling for 10-Mbps
                                             				connections, but you must use Category 5 or 5e for 100 Mbps connections. See Network Ports for guidelines. |
| Step 3 | (Optional) Connect wired extension microphones. |

| Option | Description | To Change |
|---|---|---|
| Wireless
                                             					 Microphone 1 | The
                                             					 channel that can be used to pair the first microphone. | See Pair Wireless Microphone or Unpair Wireless Microphone |
| Wireless
                                             					 Microphone 2 | The
                                             					 channel that can be used to pair the second microphone. | See Pair Wireless Microphone or Unpair Wireless Microphone |
| Wireless
                                             					 Microphone Range | Sets the
                                             					 baseband power and effective RF range for the wireless microphones. The RF
                                             					 range can be set to Low Medium High | Select
                                             					 Low, Medium or High, and press Select . Or press Default to select the default setting and press Select . |

| Step 1 | Choose Apps > Admin
                                                   				  Settings > Wireless Microphones . |
|---|---|
| Step 2 | Select either
                                             			 Wireless Microphone 1 or Wireless Microphone 2. If the
                                                				selected channel is available, a Pair microphone 1? or Pair microphone 2? prompt displays, and the Pair softkey displays. If a
                                                				microphone is already linked to a particular channel, pairing cannot be
                                                				initiated on the selected channel and the dialog shows that the microphone is
                                                				linked. |
| Step 3 | Press Pair . If the channel
                                                				is ready to pair, the pairing process begins and a text message displays. |
| Step 4 | Put the
                                             			 microphone that corresponds to the selected channel in pairing mode by pressing
                                             			 the microphone's Mute button until the LED lights solid red. If pairing
                                                				succeeds, the screen reverts to the Wireless Microphones Menu, and the message Mic X Paired Successfully! displays. If pairing
                                                				times out or fails, the status is updated and you can cancel or retry. |
| Step 5 | Press Cancel to revert to the Wireless Microphones Menu. |
| Step 6 | Press Retry to start the pairing process again. |

| Note | This option is
                                                			 not available if the microphone is connected. To enable the unpair command,
                                                			 place the wireless microphone in its charger or turn it off. |
|---|---|

| Step 1 | Choose Applications > Admin
                                                   				  Settings > Wireless Microphones . |
|---|---|
| Step 2 | Select either
                                             			 Wireless Microphone 1 or Wireless Microphone 2. If the
                                                				selected channel is paired, the Unpair softkey displays. |
| Step 3 | Press Unpair . A verification
                                                				prompt with the options to Cancel or Unpair displays. |
| Step 4 | Press Unpair to continue to unpair the microphone. The
                                                				microphone channel's registration information in the base deletes. If you view
                                                				the microphone channel's status in phone info menu, the status value and RFID
                                                				are empty. |
| Step 5 | Press return
                                             			 to revert to the wireless microphones menu and stop the process. |

| Hardware Test | Sound Base
                                             				LEDs | DCU LEDs |
|---|---|---|
| Power is Ready | Green LEDs
                                             				flash | Red and Green
                                             				LEDs flash |
| Flash is
                                             				Accessible | Green LEDs
                                             				flash | Red and Green
                                             				LEDs flash |
| RAM Test
                                             				Successful | Green LEDs
                                             				flash | Red and Green
                                             				LEDs flash |
| Ethernet Test
                                             				Successful | — | — |

| Step 1 | Obtain the
                                          			 CAPF authentication code that was set when the CAPF was configured. |
|---|---|
| Step 2 | From the
                                          			 phone, choose Apps > Admin
                                                				  Settings > Security Configuration . Note You can
                                                         				  control access to the Administrator Settings Menu by using the Settings Access
                                                         				  field in the Cisco Unified Communications Manager Administration Device
                                                         				  Configuration window. For more information, see the Cisco
                                                            					 Unified Communications Manager Administration Guide . | Note | You can
                                                         				  control access to the Administrator Settings Menu by using the Settings Access
                                                         				  field in the Cisco Unified Communications Manager Administration Device
                                                         				  Configuration window. For more information, see the Cisco
                                                            					 Unified Communications Manager Administration Guide . |
| Note | You can
                                                         				  control access to the Administrator Settings Menu by using the Settings Access
                                                         				  field in the Cisco Unified Communications Manager Administration Device
                                                         				  Configuration window. For more information, see the Cisco
                                                            					 Unified Communications Manager Administration Guide . |
| Step 3 | Scroll to LSC
                                          			 and press Update . The conference
                                             				phone prompts for an authentication string. |
| Step 4 | Enter the
                                          			 authentication code and press Submit . The conference
                                             				phone begins to install, update, or remove the LSC, depending on how the CAPF
                                             				was configured. During the procedure, a notification message is displayed so
                                             				that you can monitor progress. The LSC
                                             				install, update, or removal process can take a long time to complete. You can
                                             				stop the process at any time by pressing Exit . You can verify
                                             				that an LSC is installed on the conference phone by choosing Apps > Admin
                                                   					 Settings > Security Setup and ensuring that the
                                             				LSC setting shows Installed . |

| Note | You can
                                                         				  control access to the Administrator Settings Menu by using the Settings Access
                                                         				  field in the Cisco Unified Communications Manager Administration Device
                                                         				  Configuration window. For more information, see the Cisco
                                                            					 Unified Communications Manager Administration Guide . |
|---|---|