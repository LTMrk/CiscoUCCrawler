---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-adminguide-cs38-bk-ad57597a-00-adminguide-8831-cs-42dd31e925
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/AdminGuide/CS38_BK_AD57597A_00_adminguide-8831/CS38_BK_AD57597A_00_adminguide-8831_chapter_01001.html
retrieved_at: 2026-08-21T13:38:22.698088+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

# Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

Updated: November 17, 2014

Chapter: Troubleshooting
	 and Maintenance

## Chapter: Troubleshooting
	 and Maintenance

# Troubleshooting
                     	 and Maintenance

## Call, Device, and Network Information

You can view call, device, and network information through the Applications menu, or remotely through each conference phone
                           web page. You can use this information to monitor the operation of a conference phone to assist with troubleshooting.

## Troubleshooting

Use the following sections to troubleshoot problems with the conference phone.

### Startup Problems

After installing a conference phone into your network and adding it to Cisco Unified Communications Manager, the conference
                              phone should start up as described in IP Phone Startup Verification . If the conference phone does not start up properly, see the following sections for troubleshooting information.

#### Cisco Unified IP Phone Does Not Go Through the Normal Startup Process

##### Problem

When you connect a conference phone into the network port, the conference phone should go through its normal startup process,
                                    and the LCD screen should display information.

##### Cause

If the conference phone does not go through the startup process, the cause may be faulty cables, bad connections, network
                                    outages, lack of power, and so on. Or, the conference phone may not be functional.

##### Solution

Verify that the network port is functional:

Exchange the Ethernet cables with cables that you know are functional.

Disconnect a functioning conference phone from another port and connect it to this network port to verify the port is active.

Connect the conference phone that will not start up to a different network port that is known to be good.

Connect the conference phone that will not start up directly to the port on the switch, eliminating the patch panel connection
                                                   in the office.

Verify that the conference phone is receiving power:

If you are using external power, verify that the electrical outlet is functional.

If you are using in-line power, use the external power supply instead.

If you are using the external power supply, switch with a unit that you know to be functional.

If the conference phone still does not start up properly, perform a factory reset of the conference phone.

If after attempting these solutions, the LCD screen on the conference phone does not display any characters after at least
                                    five minutes, contact a Cisco technical support representative for additional assistance.

#### Cisco Unified IP Phone Does Not Register with Cisco Unified Communications Manager

To start up properly, the conference phone must be connected to the Ethernet network and registered with a Cisco Unified Communications
                                 Manager. If the conference phone does not start up properly, review the following sections.

##### TFTP Server Settings

###### Problem

The TFTP server settings may not be correct.

###### Solution

Check the TFTP settings. See Check TFTP Settings .

##### IP Addressing and Routing

###### Problem

The IP addressing and routing fields may not be configured correctly.

###### Solution

You should verify the Internet Protocol (IP) addressing and routing settings on the conference phone. If you are using DHCP,
                                       the DHCP server should provide these values. If you have assigned a static IP address to the conference phone, you must enter
                                       these values manually. See Check DHCP Settings

##### DNS Settings

###### Problem

The DNS settings may be incorrect.

###### Solution

If you are using DNS to see the TFTP server or to Cisco Unified Communications Manager, you must ensure that you have specified
                                       a Domain Name System (DNS) server. See Verify DNS Settings

#### Cisco Unified Communications Manager and TFTP Servers Are Not Running

If the Cisco Unified Communications Manager or TFTP services are not running, conference phones may not be able to start up
                                 properly. However, in such a situation, it is likely that you are experiencing a system-wide failure and that other conference
                                 phones and devices are unable to start up properly.

If the Cisco Unified Communications Manager service is not running, all devices on the network that rely on it to make conference
                                 phone calls will be affected. If the TFTP service is not running, many devices will not be able to start up successfully For
                                 more information, see Start Service .

#### Configuration File Corruption

##### Problem

If you continue to have problems with a particular conference phone that other suggestions in this chapter do not resolve,
                                    the configuration file may be corrupted.

##### Solution

Create a new configuration file. See Create New Phone Configuration File .

#### Cisco Unified Communications Manager Phone Registration

##### Problem

The conference phone is not registered with the Cisco Unified Communications Manager.

##### Solution

A conference phone can register with a Cisco Unified Communications Manager server only if the conference phone has been added
                                    to the server or if autoregistration is enabled. Review the information and procedures in the Cisco Unified Communications Manager Administration Conference Station Addition section  to ensure that the conference phone has been added to Cisco Unified Communications Manager.

To verify that the conference phone is in the Cisco Unified Communications Manager database, choose Device > Phone from Cisco Unified Communications Manager Administration and search for the conference phone based on its MAC Address. For
                                    information about determining a MAC address, see the Conference Phone MAC Address Determination section.

If the conference phone is already in the Cisco Unified Communications Manager database, its configuration file may be damaged.
                                    See the Configuration File Corruption section  for assistance.

### Cisco Unified IP Conference Phone Cannot Obtain IP Address

#### Problem

If a phone cannot obtain an IP address when it starts up, the phone may not be on the same network or VLAN as the DHCP server,
                                 or the switch port to which the conference phone is connected may be disabled.

#### Solution

Ensure that the network or VLAN to which the phone connects has access to the DHCP server, and ensure that the switch port
                                 is enabled.

### Cisco Unified IP Conference Phone Resets Unexpectedly

If users report that their phones are resetting during calls or while idle on their desk, you should investigate the cause.
                              If the network connection and Cisco Unified
                                 				Communications Manager connection are stable, a phone should not reset on its own.

Typically, a phone resets if it has problems connecting to the Ethernet network or to Cisco Unified
                                 				Communications Manager . The following sections can help you identify the cause of a conference phone resetting in your network.

#### Physical Connection Problems

##### Problem

The physical connection to the LAN may be broken.

##### Solution

Verify that the Ethernet connection to which the phone is connected is up. For example, check if the particular port or switch
                                    to which the phone is connected is down and that the switch is not rebooting. Also make sure that there are no cable breaks.

#### Intermittent Network Outages

##### Problem

The conference phone resets because the network may be experiencing intermittent outages.

##### Solution

Intermittent network outages affect data and voice traffic differently. Your network might be experiencing intermittent outages
                                    without detection. If so, data traffic can resend lost packets and verify that packets are received and transmitted. However,
                                    voice traffic cannot recapture lost packets. Rather than retransmitting a lost network connection, the phone resets and attempts
                                    to reconnect to the network. Contact the network administrator for information on known problems in the voice network.

#### DHCP Setting Errors

##### Problem

The DHCP settings may be incorrect.

##### Solution

Verify that you have properly configured the conference phone to use DHCP. See the Network Setup Menu section  for more information.

Verify that the DHCP server has been set up properly.

Verify the DHCP lease duration. Cisco recommends that you set it to 8 days.

conference phones send messages with request type 151 to renew their DHCP address leases. If the DHCP server expects messages
                                             with request type 150, the lease will be denied, forcing the conference phone to restart and request a new IP address from
                                             the DHCP server.

#### Static IP Address Setting Errors

##### Problem

The status IP address assigned to the conference phone may be incorrect.

##### Solution

If the conference phone has been assigned a static IP address, verify that you have entered the correct settings. See the Network Setup Menu section more information.

#### Voice VLAN Setup
                              	 Errors

##### Problem

If the conference
                                    		  phone appears to reset during heavy network usage (for example, following
                                    		  extensive web surfing on a computer connected to the same switch as conference
                                    		  phone), it is likely that you do not have a voice VLAN configured.

##### Solution

Isolating the
                                    		  conference phones on a separate auxiliary VLAN increases the quality of the
                                    		  voice traffic. See the Cisco Unified IP Communications Product Interactions section for details.

#### DNS or Other Connectivity Errors

##### Problem

The phone reset continues and you suspect DNS or other connectivity issues.

##### Solution

If the conference phone continues to reset, follow the procedure in Determine DNS or Connectivity Issues .

### Power Connection Problems

#### Problem

The conference station does not appear to be powered up.

#### Solution

In most cases, a conference phone will restart if it powers up using external power but loses that connection and switches
                                 to Power over Ethernet (PoE). Similarly, a conference phone may restart if it powers up using PoE and then gets connected
                                 to an external power supply.

### Audio and Display Problems

The following sections describe how to resolve audio and display problems.

#### Display Is Wavy

##### Problem

The display appears to have rolling lines of a wavy pattern.

##### Cause

The conference phone might be interacting with certain types of older fluorescent lights in the building.

##### Solution

Move the conference phone away from the lights or replace the lights to resolve the problem.

#### Choppy Speech or Sound

##### Problem

A user complains of choppy speech or a metallic sound coming from or going to the far end.

##### Cause

There may be jitter in the network or too many dropped packets.

##### Solution

Check the AvgJtr and the MaxJtr statistics. A large variance between these statistics might indicate a problem with jitter
                                    on the network or periodic high rates of network activity. For more information about displaying statistics, see Call Statistics Screen .

#### Choppy Speech or Sound When Using Wireless Microphones

##### Problem

A user complains of choppy speech or metallic sound coming from the wireless microphones.

##### Cause

Too many dropped packets.

##### Solution

Check the RF environment

#### Echo on Far End

##### Problem

The far end hears echo.

##### Cause

The conference phone is not on a flat and stable surface.

The wired or wireless microphones are too close to the sound base.

The wired or wireless microphones are not on a flat and stable surface.

In Linked Mode, the primary and secondary sound base units are too close together.

##### Solution

Check the placement of the bases and microphones.

#### Audio Level Too  Low

##### Problem

A user complains that the audio level is too low.

##### Cause

The user is not facing the conference phone when speaking.

The user is too far from the conference phone when speaking.

The wireless microphones are being moved.

##### Solution

Consider using external microphones, or increasing the room coverage by using Linked Mode.

#### Audio Quality Poor

##### Problem

User complains about poor audio quality.

##### Cause

You are using a narrow band rather than a wide band codec.

##### Solution

Verify on the CUCM that the default codec is G.722 (wide band).

#### No Audio Between Units

##### Problem

There is no audio to or from the secondary unit in Linked Mode.

##### Cause

The daisy cable is not connected properly.

##### Solution

Verify that the daisy cable is properly seated and that it is routed inside the cable grooves.

Verify that the external microphone icon is present on the display if one is connected.

#### No Audio from External Wireless Microphones

##### Problem

There is no audio to or from the external wireless microphones.

##### Cause

The wireless microphones are not paired or are not linked with the device.

##### Solution

Verify that the wireless microphone is paired and that the wireless microphone icon is present on the display.

Verify that the LED on the wireless external microphone is flashing green.

Verify that the wireless microphone is charged.

### Conference Call Reception Problems

To ensure optimum performance with the conference phone and the external microphones, see Performance Guidelines .

### General Troubleshooting Information

This section provides troubleshooting information for some common issues that might occur on the conference phone.

The following table provides general troubleshooting information for the conference phone.

Summary

Explanation

Changing the conference phone configuration

By default, the network configuration options are locked to prevent users from making changes that could impact their network
                                          connectivity. You must unlock the network configuration options before you can configure them.

Codec mismatch between the conference phone and another device

The RxType and the TxType statistics show the codec that is being used for a conversation between this conference phone and
                                          the other device. The values of these statistics should match. If they do not, verify that the other device can handle the
                                          codec conversation or that a transcoder is in place to handle the service.

See Call Statistics Screen for information about displaying these statistics.

Dual-Tone Multi-Frequency (DTMF) delay

When you are on a call that requires keypad input, if you press the keys too quickly, some of them might not be recognized.

conference phone does not ring

Check that the ringer setting is not “Ringer Off.” Check the volume level.

Loopback condition

The conference phone receives power from an external power supply

The conference phone is powered down (the power supply is disconnected)

In this case, the switch port on the conference phone can become disabled and the following message will appear in the switch
                                          console log:

HALF_DUX_COLLISION_EXCEED_THRESHOLD

To resolve this problem, re-enable the port from the switch.

Moving a network connection from the conference phone to a workstation

The computer’s network card cannot receive power through the network connection; if power comes through the connection, the
                                                         network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the conference
                                                         phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a conference
                                                         phone on the line and to stop providing power to the cable.

No dial tone

Check that all connections are secure and in place. Make sure all connections are correct.

No LCD screen display

Check to make sure that the conference phone has power. Make sure that the power supply unit is plugged in.

One-way audio

When at least one person in a call does not receive audio, IP connectivity between conference phones is not established. Check
                                          the configurations in routers and switches to ensure that IP connectivity is properly configures.

Poor voice quality when calling digital cell conference phones using the G.729 codec (protocol)

Using a cell, mobile, or GSM conference phone, or two-way radio in close proximity to a Cisco Unified IP Conference Phone
                                                      8831 might cause interference. For more information, see the manufacturer's documentation of the interfering device.

In Cisco Unified Communications Manager, you can configure the network to use the G.729 protocol (the default is G.711). When
                                          using G.729, calls between a Cisco Unified IP Conference Phone and a digital cellular conference phone will have poor voice
                                          quality. Use G.729 only when absolutely necessary.

For more information, see the Cisco Unified Communications Manager application online help.

Prolonged broadcast storms cause conference phones to reset, or be unable to make or answer a call

A prolonged Layer 2 broadcast storm (lasting several minutes) on the voice VLAN may cause conference phones to reset, lose
                                          an active call, or be unable to initiate or answer a call. conference phones may not come up until a broadcast storm ends.

Sound sample mismatch between the conference phone and another device

The RxSize and the TxSize statistics show the size of the voice packets that are being used in a conversation between this
                                          conference phone and the other device. The values of these statistics should match.

See Call Statistics Screen for information about displaying these statistics.

### Troubleshooting Procedures

These procedures can be used to identify and correct problems.

#### Check TFTP Settings

You can determine the IP address of the TFTP server used by the conference phone by choosing Apps > Admin Settings > Network Setup > IPv4 Configuration > TFTP Server 1 .

If you have assigned a static IP address to the conference phone, you must manually enter a setting for the TFTP Server 1
                                             option.

If you are using Dynamic Host Configuration Protocol (DHCP), the conference phone obtains the address for the Trivial File
                                             Transfer Protocol (TFTP) server from the DHCP server. A valid TFTP server must be set in DHCP option 150 or option 66 on the
                                             DHCP server.

You can also enable the conference phone to use an alternate TFTP server. Such a setting is particularly useful if the conference
                                             phone was recently moved from one location to another.

#### Start Service

To start a service, follow these steps:

From Cisco Unified Communications Manager Administration, choose Cisco Unified Serviceability from the Navigation drop-down list that displays in the upper, right corner of the window, and then click Go .

Choose Tools > Control Center - Network Services .

Choose the primary Cisco Unified Communications Manager server from the Server drop-down list.

The page displays the service names for the server that you chose, the status of the services, and a service control panel
                                                to stop or start a service.

If a service has stopped, click its radio button, and then click Start .

#### Determine DNS or Connectivity Issues

Use these steps to eliminate DNS or other connectivity errors:

Navigate to Apps > Admin Settings > Network Setup > IPv4 Configuration > DHCP and choose the Reset All  option to reset conference phone settings to their default values.

Modify DHCP and IP settings:

Disable DHCP.

Assign static IP values to the conference phone. Use the same default router setting used for other functioning conference
                                                   phones.

Assign TFTP server. Use the same TFTP server used for other functioning conference phones.

On the Cisco Unified Communications Manager server, verify that the local host files have the correct Cisco Unified Communications
                                             Manager server name mapped to the correct IP address.

From Cisco Unified Communications Manager Administration, choose System > Server to locate the server, and then click the server name. Verify that the server is referred to by its IP address and not by
                                             its DNS name.

From Cisco Unified Communications Manager Administration, choose Device > Phone to locate the conference phone, and then click the conference phone name. Verify that you have assigned the correct MAC address
                                             to this conference phone.

Power cycle the conference phone.

#### Create New Phone Configuration File

When you remove a conference phone from the Cisco Unified Communications Manager database, its configuration file is deleted
                                                from the Cisco Unified Communications Manager TFTP server. The conference phone directory number remains in the Cisco Unified
                                                Communications Manager. It becomes an “unassigned DN” and can be used by another device. If unassigned DNs are not used by
                                                other devices, delete them from Cisco Unified Communications Manager. You can use the Route Plan Report to view and delete
                                                unassigned reference numbers. For more information, see Cisco Unified Communications Manager Administration Guide .

To create a new configuration file, follow these steps:

In Cisco Unified Communications Manager Administration, choose Device > Phone . Enter search criteria to locate the conference phone experiencing problems, and then click the device name.

In the Phone Configuration window, click Delete to remove the conference phone from Cisco Unified Communications Manager.

Add the conference phone to Cisco Unified Communications Manager.

Power cycle the conference phone.

#### Verify DNS Settings

To verify DNS settings, follow these steps:

Select Apps > Admin Settings > Network Setup > IPv4 Configuration > DNS Server 1 .

Verify that there is a CNAME entry in the DNS server for the TFTP server and one for Cisco Unified Communications Manager.

Ensure that DNS is configured to do reverse look-ups.

#### Check DHCP
                              	 Settings

DHCP can be
                                                			 enabled and disabled manually.

On the
                                             			 conference station, select Apps > Admin
                                                   				  Settings > Network Setup > IPv4
                                                   				  Configuration , and look at the following options:

DHCP: If
                                                      					 you have assigned a static IP address to the conference phone, you do not need
                                                      					 to enter a value for the DHCP Server option. However, if you are using a DHCP
                                                      					 server, this option must have a value. If it does not, check your IP routing
                                                      					 and VLAN configuration. See Troubleshooting Switch Port Problems , available at this
                                                      					 URL: http://www.cisco.com/en/US/customer/products/hw/switches/ps708/prod_tech_notes_list.html

IP
                                                      					 Address, Subnet Mask, Default Router: If you have assigned a static IP address
                                                      					 to the conference phone, you must manually enter settings for these options.

If you are
                                             			 using DHCP, check the IP addresses distributed by your DHCP server. See Understanding and Troubleshooting DHCP in Catalyst Switch or
                                                				Enterprise Networks , available at this URL: http://www.cisco.com/c/en/us/support/docs/ip/dynamic-address-allocation-resolution/27470-100.html

### Additional Troubleshooting Information

Conference Phone Troubleshooting Resources: http://www.cisco.com/en/US/products/hw/phones/ps379/tsd_products_support_series_home.html

Cisco Products and Services (Technical Support and Documentation): http://www.cisco.com/en/US/products/sw/voicesw/tsd_products_support_category_home.html

## Maintenance

The following sections describe phone maintenance.

### Cisco Unified IP Conference Phone Reset or Restore

The following sections describe the methods for resetting or restoring the conference phone.

#### Settings
                              	 Reset

All

Network

Security

You can reset a
                                 		conference phone at any time after the conference phone has started up.

All

Network

Security

### Quality Report Tool

The Quality Report Tool (QRT) is a voice quality and general problem-reporting tool for the conference phone. The QRT feature
                              is installed as part of Cisco Unified Communications Manager.

You can configure users’ conference phones with QRT. When you do so, users can report problems with conference phone calls
                              by pressing the QRT softkey. This softkey is available only when the conference phone is in the Connected, Connected Conference,
                              Connected Transfer, or OnHook states.

When a user presses the QRT softkey, a list of problem categories appears. The user selects the appropriate problem category
                              and this feedback is logged in an XML file. Actual information logged depends on the user selection and whether the destination
                              device is a conference phone.

For more information about using QRT, see the Cisco Unified Communications Manager Features and Services Guide .

### Voice Quality
                           	 Monitoring

Concealment
                                       			 Ratio metrics: Show the ratio of concealment frames over total speech frames.
                                       			 An interval conceal ratio is calculated every 3 seconds.

Concealed Second
                                       			 metrics: Show the number of seconds in which the DSP plays concealment frames
                                       			 due to lost frames. A severely “concealed second” is a second in which the DSP
                                       			 plays more than five percent concealment frames.

MOS-LQK metrics:
                                       			 Use a numeric score to estimate the relative voice listening quality. The
                                       			 conference phone calculates the mean opinion score (MOS) for listening quality
                                       			 (LQK) based audible concealment events due to frame loss in the preceding 8
                                       			 seconds, and includes perceptual weighting factors such as codec type and frame
                                       			 size.

MOS LQK scores are
                              		produced by a Cisco proprietary algorithm that is an implementation of P.VTQ,
                              		an ITU provisional standard.

Concealment ratio
                                          		  and concealment seconds are primary measurements based on frame loss while MOS
                                          		  LQK scores project a “human-weighted” version of the same information on a
                                          		  scale from 5 (excellent) to 1 (bad) for measuring listening quality.

Listening quality
                              		scores (MOS LQK) relate to the clarity or sound of the received voice signal.
                              		Conversational quality scores (MOS CQ such as G.107) include impairment
                              		factors, such as delay, that degrade the natural flow of conversation.

For information
                              		about configuring voice quality metrics for conference phones, see the Cisco Unified
                                 		  Communications Manager System Guide , “Cisco Unified IP Phones” chapter,
                              		“Phone Features” section.

You can access voice
                              		quality metrics from the conference phone by using the Call Statistics screen
                              		or remotely by using Streaming Statistics.

To use the metrics
                              		for monitoring voice quality, note the typical scores under normal conditions
                              		of zero packet loss, and use the metrics as a baseline for comparison.

It is important to
                              		distinguish significant changes from random changes in metrics. Significant
                              		changes are scores that change about 0.2 MOS or greater and persist in calls
                              		that last longer than 30 seconds. Conceal Ratio changes should indicate greater
                              		than 3 percent frame loss.

G.711 codec
                                       			 gives 4.5 score

G.719A/ AB gives
                                       			 3.7 score

A Conceal Ratio of
                              		zero indicates that the IP network is delivering frames and packets on time
                              		with no loss.

When you observe
                              		significant and persistent changes to metrics, use the following table for
                              		general troubleshooting information.

Metric Change

Condition

MOS LQK scores
                                          				decrease significantly

Average
                                                   					 MOS LQK decreases could indicate widespread and uniform impairment.

Individual
                                                   					 MOS LQK decreases indicate bursty impairment.

Cross-check
                                          				with Conceal Ratio and Conceal Seconds for evidence of packet loss and jitter.

MOS LQK scores
                                          				decrease significantly

- Check to see if the
                                             				  conference phone is using a different codec than expected (RxType and TxType).

Check to
                                                					 see if the MOS LQK version changed after a firmware upgrade.

Conceal Ratio
                                          				and Conceal Seconds increase significantly

Network
                                          				impairment from packet loss or high jitter.

Conceal Ratio
                                          				is near or at zero, but the voice quality is poor

Noise or
                                                					 distortion in the audio channel such as echo or audio levels.

Tandem
                                                					 calls that undergo multiple encode/decode such as calls to a cellular network
                                                					 or calling card network.

Check packet
                                          				transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice
                                          				packets are flowing.

### Cisco Unified IP Phone Cleaning

To clean your conference phone, use a soft, dry cloth to wipe the conference phone and the LCD screen. Do not apply liquids
                              or powders directly on the conference phone. As with all non-weather-proof electronics, liquids and powders can damage the
                              components and cause failures.

| Summary | Explanation |
|---|---|
| Changing the conference phone configuration | By default, the network configuration options are locked to prevent users from making changes that could impact their network
                                          connectivity. You must unlock the network configuration options before you can configure them. |
| Codec mismatch between the conference phone and another device | The RxType and the TxType statistics show the codec that is being used for a conversation between this conference phone and
                                          the other device. The values of these statistics should match. If they do not, verify that the other device can handle the
                                          codec conversation or that a transcoder is in place to handle the service. See Call Statistics Screen for information about displaying these statistics. |
| Dual-Tone Multi-Frequency (DTMF) delay | When you are on a call that requires keypad input, if you press the keys too quickly, some of them might not be recognized. |
| conference phone does not ring | Check that the ringer setting is not “Ringer Off.” Check the volume level. |
| Loopback condition | A loopback condition can occur when the following conditions are met: The conference phone receives power from an external power supply The conference phone is powered down (the power supply is disconnected) In this case, the switch port on the conference phone can become disabled and the following message will appear in the switch
                                          console log: HALF_DUX_COLLISION_EXCEED_THRESHOLD To resolve this problem, re-enable the port from the switch. |
| Moving a network connection from the conference phone to a workstation | If you are powering your conference phone through the network connection, you must be careful if you decide to unplug the
                                          conference phone network connection and plug the cable into a desktop computer. Caution The computer’s network card cannot receive power through the network connection; if power comes through the connection, the
                                                         network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the conference
                                                         phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a conference
                                                         phone on the line and to stop providing power to the cable. | Caution | The computer’s network card cannot receive power through the network connection; if power comes through the connection, the
                                                         network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the conference
                                                         phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a conference
                                                         phone on the line and to stop providing power to the cable. |
| Caution | The computer’s network card cannot receive power through the network connection; if power comes through the connection, the
                                                         network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the conference
                                                         phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a conference
                                                         phone on the line and to stop providing power to the cable. |
| No dial tone | Check that all connections are secure and in place. Make sure all connections are correct. |
| No LCD screen display | Check to make sure that the conference phone has power. Make sure that the power supply unit is plugged in. |
| One-way audio | When at least one person in a call does not receive audio, IP connectivity between conference phones is not established. Check
                                          the configurations in routers and switches to ensure that IP connectivity is properly configures. |
| Poor voice quality when calling digital cell conference phones using the G.729 codec (protocol) Caution Using a cell, mobile, or GSM conference phone, or two-way radio in close proximity to a Cisco Unified IP Conference Phone
                                                      8831 might cause interference. For more information, see the manufacturer's documentation of the interfering device. | Caution | Using a cell, mobile, or GSM conference phone, or two-way radio in close proximity to a Cisco Unified IP Conference Phone
                                                      8831 might cause interference. For more information, see the manufacturer's documentation of the interfering device. | In Cisco Unified Communications Manager, you can configure the network to use the G.729 protocol (the default is G.711). When
                                          using G.729, calls between a Cisco Unified IP Conference Phone and a digital cellular conference phone will have poor voice
                                          quality. Use G.729 only when absolutely necessary. For more information, see the Cisco Unified Communications Manager application online help. |
| Caution | Using a cell, mobile, or GSM conference phone, or two-way radio in close proximity to a Cisco Unified IP Conference Phone
                                                      8831 might cause interference. For more information, see the manufacturer's documentation of the interfering device. |
| Prolonged broadcast storms cause conference phones to reset, or be unable to make or answer a call | A prolonged Layer 2 broadcast storm (lasting several minutes) on the voice VLAN may cause conference phones to reset, lose
                                          an active call, or be unable to initiate or answer a call. conference phones may not come up until a broadcast storm ends. |
| Sound sample mismatch between the conference phone and another device | The RxSize and the TxSize statistics show the size of the voice packets that are being used in a conversation between this
                                          conference phone and the other device. The values of these statistics should match. See Call Statistics Screen for information about displaying these statistics. |

| Caution | The computer’s network card cannot receive power through the network connection; if power comes through the connection, the
                                                         network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the conference
                                                         phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a conference
                                                         phone on the line and to stop providing power to the cable. |
|---|---|

| Caution | Using a cell, mobile, or GSM conference phone, or two-way radio in close proximity to a Cisco Unified IP Conference Phone
                                                      8831 might cause interference. For more information, see the manufacturer's documentation of the interfering device. |
|---|---|

| Step 1 | You can determine the IP address of the TFTP server used by the conference phone by choosing Apps > Admin Settings > Network Setup > IPv4 Configuration > TFTP Server 1 . |
|---|---|
| Step 2 | If you have assigned a static IP address to the conference phone, you must manually enter a setting for the TFTP Server 1
                                             option. |
| Step 3 | If you are using Dynamic Host Configuration Protocol (DHCP), the conference phone obtains the address for the Trivial File
                                             Transfer Protocol (TFTP) server from the DHCP server. A valid TFTP server must be set in DHCP option 150 or option 66 on the
                                             DHCP server. |
| Step 4 | You can also enable the conference phone to use an alternate TFTP server. Such a setting is particularly useful if the conference
                                             phone was recently moved from one location to another. |

| Step 1 | From Cisco Unified Communications Manager Administration, choose Cisco Unified Serviceability from the Navigation drop-down list that displays in the upper, right corner of the window, and then click Go . |
|---|---|
| Step 2 | Choose Tools > Control Center - Network Services . |
| Step 3 | Choose the primary Cisco Unified Communications Manager server from the Server drop-down list. The page displays the service names for the server that you chose, the status of the services, and a service control panel
                                                to stop or start a service. |
| Step 4 | If a service has stopped, click its radio button, and then click Start . |

| Step 1 | Navigate to Apps > Admin Settings > Network Setup > IPv4 Configuration > DHCP and choose the Reset All  option to reset conference phone settings to their default values. |
|---|---|
| Step 2 | Modify DHCP and IP settings: Disable DHCP. Assign static IP values to the conference phone. Use the same default router setting used for other functioning conference
                                                   phones. Assign TFTP server. Use the same TFTP server used for other functioning conference phones. |
| Step 3 | On the Cisco Unified Communications Manager server, verify that the local host files have the correct Cisco Unified Communications
                                             Manager server name mapped to the correct IP address. |
| Step 4 | From Cisco Unified Communications Manager Administration, choose System > Server to locate the server, and then click the server name. Verify that the server is referred to by its IP address and not by
                                             its DNS name. |
| Step 5 | From Cisco Unified Communications Manager Administration, choose Device > Phone to locate the conference phone, and then click the conference phone name. Verify that you have assigned the correct MAC address
                                             to this conference phone. |
| Step 6 | Power cycle the conference phone. |

| Note | When you remove a conference phone from the Cisco Unified Communications Manager database, its configuration file is deleted
                                                from the Cisco Unified Communications Manager TFTP server. The conference phone directory number remains in the Cisco Unified
                                                Communications Manager. It becomes an “unassigned DN” and can be used by another device. If unassigned DNs are not used by
                                                other devices, delete them from Cisco Unified Communications Manager. You can use the Route Plan Report to view and delete
                                                unassigned reference numbers. For more information, see Cisco Unified Communications Manager Administration Guide . |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, choose Device > Phone . Enter search criteria to locate the conference phone experiencing problems, and then click the device name. |
|---|---|
| Step 2 | In the Phone Configuration window, click Delete to remove the conference phone from Cisco Unified Communications Manager. |
| Step 3 | Add the conference phone to Cisco Unified Communications Manager. |
| Step 4 | Power cycle the conference phone. |

| Step 1 | Select Apps > Admin Settings > Network Setup > IPv4 Configuration > DNS Server 1 . |
|---|---|
| Step 2 | Verify that there is a CNAME entry in the DNS server for the TFTP server and one for Cisco Unified Communications Manager. |
| Step 3 | Ensure that DNS is configured to do reverse look-ups. |

| Note | DHCP can be
                                                			 enabled and disabled manually. |
|---|---|

| Step 1 | On the
                                             			 conference station, select Apps > Admin
                                                   				  Settings > Network Setup > IPv4
                                                   				  Configuration , and look at the following options: DHCP: If
                                                      					 you have assigned a static IP address to the conference phone, you do not need
                                                      					 to enter a value for the DHCP Server option. However, if you are using a DHCP
                                                      					 server, this option must have a value. If it does not, check your IP routing
                                                      					 and VLAN configuration. See Troubleshooting Switch Port Problems , available at this
                                                      					 URL: http://www.cisco.com/en/US/customer/products/hw/switches/ps708/prod_tech_notes_list.html IP
                                                      					 Address, Subnet Mask, Default Router: If you have assigned a static IP address
                                                      					 to the conference phone, you must manually enter settings for these options. |
|---|---|
| Step 2 | If you are
                                             			 using DHCP, check the IP addresses distributed by your DHCP server. See Understanding and Troubleshooting DHCP in Catalyst Switch or
                                                				Enterprise Networks , available at this URL: http://www.cisco.com/c/en/us/support/docs/ip/dynamic-address-allocation-resolution/27470-100.html |

| Note | Concealment ratio
                                          		  and concealment seconds are primary measurements based on frame loss while MOS
                                          		  LQK scores project a “human-weighted” version of the same information on a
                                          		  scale from 5 (excellent) to 1 (bad) for measuring listening quality. |
|---|---|

| Metric Change | Condition |
|---|---|
| MOS LQK scores
                                          				decrease significantly | Network
                                          				impairment from packet loss or high jitter: Average
                                                   					 MOS LQK decreases could indicate widespread and uniform impairment. Individual
                                                   					 MOS LQK decreases indicate bursty impairment. Cross-check
                                          				with Conceal Ratio and Conceal Seconds for evidence of packet loss and jitter. |
| MOS LQK scores
                                          				decrease significantly | Check to see if the
                                             				  conference phone is using a different codec than expected (RxType and TxType). Check to
                                                					 see if the MOS LQK version changed after a firmware upgrade. |
| Conceal Ratio
                                          				and Conceal Seconds increase significantly | Network
                                          				impairment from packet loss or high jitter. |
| Conceal Ratio
                                          				is near or at zero, but the voice quality is poor | Noise or
                                                					 distortion in the audio channel such as echo or audio levels. Tandem
                                                					 calls that undergo multiple encode/decode such as calls to a cellular network
                                                					 or calling card network. Check packet
                                          				transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice
                                          				packets are flowing. |

| Note | Voice quality
                                       	 metrics do not account for noise or distortion, only frame loss. |
|---|---|