---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-10-0-english-admin-guide-p691-bk-af85a164-00-admin-guide-69-d5baeea1ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/10_0/english/admin_guide/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0_chapter_01000.html
retrieved_at: 2026-08-21T14:04:37.423694+00:00
---

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

# Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

Updated: May 9, 2025

Chapter: Troubleshooting and Maintenance

## Chapter: Troubleshooting and Maintenance

# Troubleshooting and Maintenance

## Troubleshooting and Maintenance Overview

This chapter provides information that can assist you in
                           		troubleshooting problems with your Cisco Unified IP Phone or with your IP
                           		telephony network. It also explains how to clean and maintain your phone.

If you need additional assistance to resolve an issue, see the Documentation, Support, and Security Guidelines .

## Troubleshooting

Use the following sections to troubleshoot problems with the
                           		phones.

### Startup Problems

After installing a CiscoUnified IP Phone into your network and
                              		adding it to Cisco Unified Communications Manager, the phone should start up as
                              		described in the Phone Startup Verification .

If the phone does not start up properly, see the following
                              		sections for troubleshooting information.

#### Cisco Unified IP Phone Does Not Go Through Normal Startup Process

##### Problem

When you connect a CiscoUnifiedIPPhone into the network port, the phone should go through the  normal startup process as described
                                    in Phone Startup Verification .

##### Cause

If the phone does not go through the startup process, the cause may include faulty cables, bad connections, network outages,
                                    and  lack of power. Or, the phone may be faulty.

##### Solution

To determine whether the phone is faulty, follow these suggestions to systematically eliminate other potential problems:

Verify that the network port is functional:

Exchange the Ethernet cables with cables that you know are functional.

Connect a operational phone to this network port to verify that the port is active.

Replace an operational phone with the nonoperational phone.

Connect the nonoperational phone directly to the port on the switch, eliminating the patch panel connection in the office.

Verify that the phone is receiving power:

If you are using external power, verify that the electrical outlet has power.

If you are using in-line power, plug the phone into an electrical outlet using the external power supply.

If you are using the external power supply, switch the power supply with a unit that you know works.

If the phone still does not start up properly, perform a factory reset of the phone. For instructions, see the Perform Factory Reset .

If after attempting these solutions, the phone still does not function, contact a Cisco technical support representative for
                                    additional assistance.

#### Cisco Unified IP Phone Does Not Register with Cisco Unified Communications Manager

Use this section if the phone proceeds past the first stage of the startup
                                 		process (all LED buttons on) but the phone is not starting up properly. The
                                 		phone cannot successfully start up unless it is connected to the Ethernet
                                 		network and it has registered with a CiscoUnifiedCommunications Manager
                                 		server.

In addition, problems with security may prevent the phone from
                                 		starting up properly. For more information, see General Troubleshooting Information .

##### Phone Displays Error Messages

###### Problem

Status messages display errors during startup.

###### Solution

As the phone cycles through the startup process, you can access status messages that might provide you with information about
                                       the cause of a problem. For instructions about accessing status messages and suggested actions to resolve the errors, see
                                       the Device Logs Area .

##### Phone Cannot Connect to TFTP Server or to Cisco Unified Communications Manager

###### Problem

If the network is down between the phone and either the TFTP server or Cisco Unified Communications Manager, the phone cannot
                                       start up properly.

###### Solution

Ensure that the network is currently running.

##### TFTP Server Settings

###### Problem

The TFTP server settings may not be correct.

###### Solution

Check the TFTP settings. See Check TFTP Settings .

##### IP Addressing and Routing

###### Problem

The IP addressing and routing fields may not be correctly
                                       		  configured.

###### Solution

You should verify the IP addressing and routing settings on
                                       		  the phone. If you are using DHCP, the DHCP server should provide these values.
                                       		  If you have assigned a static IP address to the phone, you must enter these
                                       		  values manually.

On the CiscoUnifiedIPPhone, press the * , # , and 0 buttons simultaneously, enter the password, and then follow
                                       		  the voice prompts to review the IP Address, Subnet Mask, Default Router.

If you have assigned a static IPaddress to the phone, you must
                                             				manually enter settings for these options. See the Cisco Unified IP Phone Network Settings Setup for instructions.

If you are using DHCP, check the IP addresses distributed by your
                                             				DHCP server. Refer to the Understanding and Troubleshooting DHCP in Catalyst Switch or
                                                				  Enterprise Networks document, available at this URL:

http://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml

##### Cisco CallManager and TFTP Services Are Not Running

###### Problem

If the Cisco CallManager or TFTP services are not running, phones may not be able to start up properly. In such a situation,
                                       it is likely that you are experiencing a systemwide failure, and other phones and devices are unable to start up properly.

###### Solution

If the Cisco CallManager service is not running, all devices on the network that rely on it to make phone calls are affected.
                                       If the TFTP service is not running, many devices cannot start up successfully. For more information, see Start Service .

##### Configuration File Corruption

###### Problem

If you continue to have problems with a particular phone that other suggestions in this chapter do not resolve, the configuration
                                       file may be corrupted.

###### Solution

Create a new phone configuration file. See Create New Configuration File .

##### Cisco Unified Communications Manager Phone Registration

###### Problem

The phone is not registered with the Cisco Unified
                                       		  Communications Manager.

###### Solution

A CiscoUnified IP Phone can register with a
                                       		  CiscoUnifiedCommunications Manager server only if the phone has been added to
                                       		  the server or (if autoregistration is enabled) there is a sufficient number of
                                       		  unit licenses. Review the information and procedures in Cisco Unified Communications Manager Phone Addition Methods to ensure that the phone has been added to the CiscoUnifiedCommunications
                                       		  Manager database.

To verify that the phone is in the
                                       		  CiscoUnifiedCommunications Manager database, choose Device > Phone > Find from CiscoUnifiedCommunications Manager Administration to search for the
                                       		  phone based on the  MAC Address. For information about determining a MAC
                                       		  address, see the Cisco Unified IP Phones and Different Protocols .

If the phone is already in the CiscoUnifiedCommunications
                                       		  Manager database, the phone   configuration file may be damaged. For assistance, see Create New Configuration File .

For more information about licensing, see the "Licences for phones" section of the Cisco Unified Communications Manager System Guide .

#### Cisco Unified IP Phone Cannot Obtain IP Address

##### Problem

If a phone cannot  obtain an IP address when it starts up, the phone may not be on the same network or VLAN as the DHCP server,
                                    or the switch port to which the phone connects may be disabled.

##### Solution

Ensure that the network or VLAN to which the phone  connects has access to the DHCP server, and ensure that the switch port
                                    is enabled.

#### Cisco Unified IP Phone Displays Flashing Red Light

##### Problem

The phone fails to boot, and the message indicator flashes a red light.

##### Cause

When a Cisco Unified IP Phone boots, it performs an internal Power On Self Test (POST). POST checks for existing encryption
                                    functionality. If POST detects that encryption functionality is missing, the phone fails to boot, and the phone displays a
                                    flashing red light.

##### Solution

To correct the problem, perform the following steps:

Reset the phone manually.

If the phone does not start up properly, power up the phone with the handset off-hook. When the phone is powered up in this
                                          way, it attempts to launch a backup software image.

If the phone still does not start up properly, perform a factory reset of the phone. For instructions, see Perform Factory Reset .

### Cisco Unified IP Phone Resets Unexpectedly

If users report that their phones are resetting during calls or
                              		while idle on their desk, you should investigate the cause. If the network
                              		connection and CiscoUnifiedCommunications Manager connection are stable, a
                              		CiscoUnified IP Phone should not reset on its own.

Typically, a phone resets if it has problems connecting to the
                              		Ethernet network or to Cisco Unified Communications Manager.

#### Physical Connection Problems

##### Problem

The physical connection to the LAN may be broken.

##### Solution

Verify that the Ethernet connection to which the Cisco Unified IP Phone connects is up. For example, check whether the particular
                                    port or switch to which the phone connects is down and that the switch is not rebooting. Also ensure that no cable breaks
                                    exist.

#### Intermittent Network Outages

##### Problem

Your network may be experiencing intermittent outages.

##### Solution

Intermittent network outages affect data and voice traffic differently. Your network might be experiencing intermittent outages
                                    without detection. If so, data traffic can resend lost packets and verify that packets are received and transmitted. However,
                                    voice traffic cannot recapture lost packets. Rather than retransmitting a lost network connection, the phone resets and attempts
                                    to reconnect to the network. Contact the system administrator for information on known problems in the voice network.

#### DHCP Settings Errors

##### Problem

The DHCP settings may be incorrect.

##### Solution

Verify that you have properly configured the phone to use DHCP. For more information see, Cisco Unified IP Phone Network Settings Setup . Verify that the DHCP server is set up properly. Verify the DHCP lease duration. Cisco recommends that you set the lease
                                    duration to 8 days.

#### Static IP Address Settings Errors

##### Problem

The static IP address assigned to the phone may be incorrect.

##### Solution

If the phone has been assigned a static IP address, verify that you have entered the correct settings. For more information,
                                    see Cisco Unified IP Phone Network Settings Setup .

#### Voice VLAN Setup Errors

##### Problem

If the CiscoUnified IP Phone appears to reset during heavy network usage (for example, following extensive web surfing on
                                    a computer connected to the same switch as the phone), it is likely that you do not have a voice VLAN configured.

##### Solution

Isolating the phones on a separate auxiliary VLAN increases the quality of the voice traffic. For more information, see Cisco Unified IP Phone 6911 and VLAN Interaction .

#### Phones Have Not Been Intentionally Reset

##### Problem

If you are not the only administrator with access to Cisco
                                    		  Unified Communications Manager, you should verify that no one else has
                                    		  intentionally reset the phones.

##### Solution

You can check if a Cisco Unified IP Phone received a
                                    		  command from Cisco Unified Communications Manager to reset by pressing Applications on the phone and choosing Administrator
                                          				Settings > Status > Network
                                          				Statistics .

If the Restart Cause field displays Reset-Reset , the phone received a Reset/Reset from Cisco Unified Communications Manager
                                          				Administration.

If the Restart Cause field displays Reset-Restart , the phone
                                          				reset because it received a Reset/Restart from Cisco Unified Communications Manager
                                          				Administration.

#### DNS or Other Connectivity Errors

##### Problem

The phone reset continues and you suspect DNS or other connectivity issues.

##### Solution

If the phone continues to reset, eliminate DNS or other connectivity errors with Determine DNS or Connectivity Issues .

#### Power Connection Problems

##### Problem

The phone does not appear to be powered up.

##### Solution

In most cases, a phone restarts if it powers up by using external power but loses that connection and switches to PoE. Similarly,
                                    a phone may restart if it powers up by using PoE and then connects to an external power supply.

### Audio Problems

The following sections describe how to resolve audio problems.

#### Poor Audio Quality with Calls That Route Outside  Cisco Unified Communications Manager

##### Problem

Poor quality occurs with tandem audio encoding. Tandem encoding can occur when calls are made between an IP Phone and a digital
                                    cellular phone, when  a conference bridge is used, or in situations where IP-to-IP calls are partially routed across the PSTN.

##### Cause

In these cases, use of voice codecs such as G.729 and iLBC may result in poor voice quality.

##### Solution

Use the G.729 and iLBC codecs only when absolutely necessary.

#### Choppy Speech

##### Problem

A user complains of choppy speech on a call.

##### Cause

There may be a mismatch in the jitter configuration.

##### Solution

Check the AvgJtr and the MaxJtr statistics. A large variance between these statistics
                                    might indicate a problem with jitter on the network or periodic high rates of
                                    network activity.

#### No Speech Path

##### Problem

One or more people on a call do not hear any audio.

##### Solution

When at least one person in a call does not receive audio, IP connectivity between phones is not established. Check the configuration
                                    of routers and switches to ensure that IP connectivity is properly configured.

### General Telephone Call Problems

The following sections help troubleshoot general telephone call problems.

#### Phone Call Cannot Be Established

##### Problem

A user complains about not being able to make a call.

##### Cause

The phone does not have a DHCP IP address, is unable to
                                    		  register to Cisco Unified Communications Manager. Phones with an LCD display show the message Configuring IP or Registering . Phones without an LCD display play the reorder tone (instead of dial tone) in the handset when the user attempts to make
                                    a call.

##### Solution

Verify the following:

- The Ethernet cable is
                                             				  attached.

- The Cisco CallManager
                                             				  service is running on the Cisco Unified Communications Manager server.

- Both phones are
                                             				  registered to the same Cisco Unified Communications Manager.

Audio server debug and capture logs are enabled for both phones.
                                          				If needed, enable Java debug.

#### Phone Does Not Recognize DTMF Digits or Digits Are Delayed

##### Problem

The user complains that numbers are missed or delayed when the keypad is used.

##### Cause

Pressing the keys too quickly can result in missed or delayed digits.

##### Solution

Keys should not be pressed rapidly.

### Troubleshooting Procedures

These procedures can be used to identify and correct problems.

#### Check TFTP Settings

Step 1

Determine the IP address of the TFTP server used by the
                                             			 phone by pressing the * , # , and 0 buttons simultaneously, entering the password, and then
                                             			 following the voice prompts to review the network setting.

Step 2

If you have assigned a static IP address to the phone, check the  setting for the TFTP Server 1 option. See the Cisco Unified IP Phone Network Settings Setup .

Step 3

If you are using DHCP, the phone obtains the address for the TFTP
                                             			 server from the DHCP server. Check the IP address configured in Option 150 or
                                             			 Option 66.

Step 4

Enable the phone to use an alternate TFTP server.
                                             			 Such a setting is particularly useful if the phone was recently moved from one
                                             			 location to another. See the Cisco Unified IP Phone Network Settings Setup for instructions.

#### Create New Configuration File

If you continue to have problems with a particular phone
                                    		  that other suggestions in this chapter do not resolve, the configuration file
                                    		  may be corrupted.

- When you remove a phone
                                                   				from the CiscoUnified Communications Manager database, the Cisco Unified Communications Manager deletes the configuration
                                                   file from the TFTP server. The
                                                   				assigned directory numbers for the phone remain in the CiscoUnified Communications
                                                   				Manager database. They are called unassigned DNs and can be assigned to other devices. If
                                                   				unassigned DNs are not used by other devices, delete them from the
                                                   				CiscoUnifiedCommunications Manager database. You can use the Route Plan
                                                   				Report to view and delete unassigned reference numbers. Refer toFor more information, see Cisco
                                                      				  UnifiedCommunications Manager Administration Guide .

- Changing the buttons on
                                                   				a phone button template, or assigning a different phone button template to a
                                                   				phone, may result in directory numbers that are no longer accessible from the
                                                   				phone. The directory numbers are still assigned to the phone in the
                                                   				CiscoUnified Communications Manager database, but there is no button on the
                                                   				phone for the line, meaning that no calls to the number can be answered. These directory numbers should be
                                                   				removed from the phone and deleted if necessary.

To create a new configuration file, follow these steps:

Step 1

From CiscoUnifiedCommunications Manager, choose Device > Phone > Find to locate the phone experiencing problems.

Step 2

Choose Delete to remove the phone from the
                                             			 CiscoUnifiedCommunications Manager database.

Step 3

Add the phone back to the CiscoUnifiedCommunications Manager
                                             			 database. See the Cisco Unified Communications Manager Phone Addition Methods for details.

Step 4

Power cycle the phone.

#### Determine DNS or Connectivity Issues

If the phone continues to reset, follow these steps to
                                    		  eliminate DNS or other connectivity errors:

Step 1

Use the Reset Settings menu to reset phone settings to their
                                             			 default values. For more information, see Cisco Unified IP Phone Reset or Restore .

Step 2

Modify DHCP and IP settings:

Disable DHCP. For instructions, see Cisco Unified IP Phone Network Settings Setup .

Assign static IP values to the phone. For instructions, see Cisco Unified IP Phone Network Settings Setup . Use the same default router setting used for other
                                                   				  functioning CiscoUnified IP Phones.

Assign a TFTP server. For instructions, see Cisco Unified IP Phone Network Settings Setup . Use the same TFTP server used for other functioning
                                                   				  CiscoUnified IP Phones.

Step 3

On the CiscoUnifiedCommunications Manager server, verify that
                                             			 the local host files have the correct CiscoUnifiedCommunications Manager
                                             			 server name mapped to the correct IP address.

Step 4

From CiscoUnifiedCommunications Manager, choose System > Server and verify that the server is referred to by the  IP address and not by the  DNS
                                             			 name.

Step 5

From CiscoUnifiedCommunications Manager, choose Device > Phone > Find and verify that you have assigned the correct MAC address to this CiscoUnified
                                             			 IP Phone. For information about determining a MAC address, see the Cisco Unified IP Phones and Different Protocols .

Step 6

Power cycle the phone.

#### Start Service

A service must be activated before it can be started or stopped. To
                                                			 activate a service, choose Tools > Service
                                                      				  Activation .

To start a service, follow these steps:

Step 1

From Cisco Unified Communications Manager Administration, choose Cisco Unified Serviceability from the
                                             			 Navigation drop-down list and click Go .

Step 2

Choose Tools > Control
                                                   				  Center - Feature Services .

Step 3

Choose the primary Cisco Unified Communications Manager server
                                             			 from the Server drop-down list.

The window displays the service names for the server that you
                                                				chose, the status of the services, and a service control panel to start or stop
                                                				a service.

Step 4

If a service has stopped, click the corresponding radio button and then click Start .

The Service Status symbol changes from a square to an arrow.

### General Troubleshooting Information

The following table provides general troubleshooting
                                 		  information for the CiscoUnified IP Phone.

Summary

Explanation

Connecting a Cisco Unified IP Phone to another Cisco Unified
                                             					 IP Phone through the PC port.

Cisco does not support connecting an IP Phone to another IP
                                             					 Phone through the PC port. Each IP Phone should directly connect to a switch
                                             					 port. If phones are connected together in a line (by using the PC port), the
                                             					 phones will not work.

Prolonged broadcast storms cause IPphones to reset, or be
                                             					 unable to make or answer a call.

A prolonged Layer 2 broadcast storm (lasting several minutes)
                                             					 on the voice VLAN may cause IP phones to reset, lose an active call, or be
                                             					 unable to initiate or answer a call. Phones may not regain connectivity  until a broadcast
                                             					 storm ends.

Moving a network connection from the phone to a workstation.

If you power your phone through the network connection,
                                             					 you must be careful if you decide to unplug the network connection of the phone and
                                             					 plug the cable into a desktop computer.

Caution

The computer network card cannot receive power through the
                                                         						network connection; if power comes through the connection, the network card can
                                                         						be destroyed. To protect a network card, wait 10 seconds or longer after
                                                         						unplugging the cable from the phone before plugging it into a computer. This
                                                         						delay gives the switch enough time to recognize that there is no longer a phone
                                                         						on the line and to stop providing power to the cable.

Changing the telephone configuration.

By default, the network configuration options are locked to
                                             					 prevent users from making changes that could impact their network connectivity.
                                             					 You must unlock the network configuration options before you can configure
                                             					 them. See the Access Phone Configuration Settings for details.

Phone resetting.

The phone resets when it loses contact with the Cisco
                                             					 UnifiedCommunications Manager software. This lost connection can be due to any
                                             					 network connectivity disruption, including cable breaks, switch outages, and
                                             					 switch reboots.

Codec mismatch between the phone and another device.

The RxType and the TxType statistics show the codec that is
                                             					 being used for a conversation between this Cisco UnifiedIPphone and the other
                                             					 device. The values of these statistics should match. If they do not match,
                                             					 verify that the other device can handle the codec conversation or that a
                                             					 transcoder is in place to handle the service.

Sound sample mismatch between the phone and another device.

The RxSize and the TxSize statistics show the size of the
                                             					 voice packets that are being used in a conversation between this Cisco
                                             					 UnifiedIPphone and the other device. The values of these statistics should
                                             					 match.

Loopback condition.

A loopback condition can occur when the following conditions
                                             					 are met:

- The SW Port
                                                						Configuration option in the Network Configuration menu on the phone is set to 10 Half (10-BaseT / half duplex)

- The phone receives
                                                						power from an external power supply

- The phone is
                                                						powered down (the power supply is disconnected)

In this case, the switch port on the phone can become disabled
                                             					 and the following message will appear in the switch console log:

HALF_DUX_COLLISION_EXCEED_THRESHOLD

To resolve this problem, reenable the port from the switch.

### Additional Troubleshooting Information

If you have additional questions about troubleshooting the CiscoUnified IP Phones, several Cisco.com web sites can provide
                              you with more tips. Choose from the sites available for your access level.

CiscoUnified IP Phone Troubleshooting Resources:

http://www.cisco.com/en/US/products/hw/phones/ps379/tsd_products_support_troubleshoot_and_alerts.html

Cisco Products and Services (Technical Support and Documentation):

http://www.cisco.com/en/US/products/ps10326/tsd_products_support_series_home.html

## Maintenance

The following sections describe voice and phone maintenance.

### Cisco Unified IP Phone Reset or Restore

The following sections detail two general methods for resetting or restoring the CiscoUnified IP Phone.

#### Perform Basic Reset

Performing a basic reset of a CiscoUnified IP Phone provides a methods to recover if the phone experiences an error and provides
                                    a methods to reset or restore various configuration and security settings.

The following table describes the methods to perform a basic reset. You can reset a phone with any of these operations after
                                    the phone has started up. Choose the operation that is appropriate for your situation.

Operation

Performing

Explanation

Restart phone

Unplug the power cable and plug it back in.

Resets any user and network configuration changes that you have made, but that the phone has not written to flash memory,
                                                to previously saved settings, then restarts the phone.

Reset Settings

Reset the phone to the  factory settings.

Resets user and network configuration settings to their default values, and restarts the phone.

#### Perform Factory Reset

When you perform a factory reset of the CiscoUnified IP
                                    		  Phone, the following information is erased or reset to the  default value:

- User configuration
                                       			 settings: Reset to default values

- Network configuration
                                       			 settings: Reset to default values

- Call histories: Erased

- Locale information: Reset
                                       			 to default values

- Phone application: Erased
                                       			 (phone recovers by using the image in the inactive partition of flash memory to
                                       			 boot up).

Before you perform a factory reset, ensure that the
                                    		  following conditions are met:

- The phone must be on a
                                       			 DHCP-enabled network.

- A valid TFTP server must
                                       			 be set in DHCP option 150 or option 66 on the DHCP server.

To perform a factory reset of a phone, you can use the IVR
                                    		  to reset the network settings to factory default or you can perform the
                                    		  following steps:

Step 1

Unplug the power cable from the phone and then plug it back in.

The phone begins its power-up cycle.

Step 2

While the phone is powering up, press and hold # button until the
                                             			 Line LED turns green.

Step 3

Release the # button and press 123456789*0# .

The line button LED turns red. The phone reboots when it is
                                                				finished.

### Voice Quality Monitoring

To measure the voice quality of calls that are sent and
                              		received within the network, Cisco Unified IP Phones use statistical metrics
                              		that are based on concealment events. The Digital Signal Processor (DSP) plays concealment frames to mask
                              		frame loss in the voice packet stream.

Concealment Ratio metrics: Shows the ratio of concealment frames
                                    			 over total speech frames. An interval conceal ratio is calculated every 3
                                    			 seconds.

Concealed Second metrics: Shows the number of seconds in which the
                                    			 DSP plays concealment frames due to lost frames. A severely "concealed second" is a second in which the DSP plays more than
                                    			 five percent concealment frames.

Mean Opinion Score (MOS) for Listening Quality (LQK) Voice Metrics:
                                    			 Uses a numeric score to estimate the relative voice-listening quality. The
                                    			 Cisco Unified IP Phones calculate the MOSLQK based audible-concealment events
                                    			 due to a frame loss in the preceding 8 seconds and includes weighting factors
                                    			 such as codec type and frame size.

MOS LQK scores are produced by a Cisco-proprietary algorithm, the
                                    			 Cisco Voice Transmission Quality (CVTQ) index. Depending on the MOS LQK version
                                    			 number, these scores may comply with the International Telecommunications Union
                                    			 (ITU) standard P.564. This standard defines evaluation methods and performance
                                    			 accuracy targets that predict listening quality scores based on observation of
                                    			 actual network impairment.

Concealment ratio and concealment seconds are primary measurements
                                          		  based on frame loss. A Conceal Ratio of zero indicates that the IP network is
                                          		  delivering frames and packets on time with no loss.

You can access voice quality metrics remotely by using
                              		Streaming Statistics (see Remote Monitoring ).

### Voice Quality Metrics

When using the metrics for monitoring voice quality, note the typical scores under normal conditions of zero packet loss and
                              use the metrics as a baseline for comparison.

It is also important to distinguish significant changes from random changes in metrics. Significant changes are scores that
                              change about 0.2 MOS or more and persist in calls that last longer than 30seconds. Conceal ratio changes indicate a frame
                              loss greater than 3percent.

The MOS LQK scores can vary based on the codec that the Cisco Unified IP Phone uses. The following codecs provide these corresponding
                              maximum MOS LQK scores under normal conditions with zero frame loss for Cisco Unified Phones 6901 and 6911:

G.711: 4.5 MOS LQK

G.722: 4.5 MOS LQK

G.728/iLBC: 3.9 MOS LQK

G729A/AB: 3.7 MOS LQK

Cisco Voice Transmission Quality (CVTQ) does not support wideband (7 kHz) speech codecs, because ITU has not defined the extension
                              of the technique to wideband. Therefore, MOS LQK scores that correspond to G.711 performance are reported for G.722 calls
                              to allow basic quality monitoring, rather than not reporting an MOS score.

Reporting G.711-scale MOS scores for wideband calls through the use of CVTQ allows basic-quality classifications to be indicated
                                    as good/normal or bad/abnormal. Calls with high scores (approximately 4.5) indicate high quality or a low packet loss, and
                                    lower scores (approximately 3.5) indicate low quality or a high packet loss.

Unlike MOS, the conceal ratio and concealed seconds metrics remain valid and useful for both wideband and narrowband calls.

A conceal ratio of zero indicates that the IP network is delivering frames and packets on time with noloss.

#### Voice Quality Troubleshooting Tips

When you observe significant and persistent changes to metrics, use the following table for general troubleshooting information.

Metric change

Condition

Conceal Ratio and Conceal Seconds increase significantly

Network impairment from packet loss or high jitter.

Conceal Ratio is near or at zero, but the voice quality is poor.

- Noise or distortion in the audio channel such as echo or audio levels.

- Tandem calls that undergo multiple encode/decode such as calls to a cellular network or calling card network.

- Acoustic problems coming from a speakerphone, handsfree cellular phone or wireless headset.

Check packet transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice packets are flowing.

MOS LQK scores decrease significantly

Network impairment from packet loss or high jitter levels:

- Average MOS LQK decreases may indicate widespread and uniform impairment.

- Individual MOS LQK decreases may indicate bursty impairment.

Cross-check the conceal ratio and conceal seconds for evidence of packet loss and jitter.

MOS LQK scores increase significantly

- Check to see if the phone is using a different codec than expected (RxType and TxType).

- Check to see if the MOS LQK version changed after a firmware upgrade.

Voice quality metrics do not account for noise or distortion, only frame loss.

### Cisco Unified IP Phone Cleaning

To clean your CiscoUnified IP Phone, use only a dry soft cloth to gently wipe the phone. Do not apply liquids or powders directly
                              on the phone. As with all non-weatherproof electronics, liquids and powders can damage the components and cause failures.

| Step 1 | Determine the IP address of the TFTP server used by the
                                             			 phone by pressing the * , # , and 0 buttons simultaneously, entering the password, and then
                                             			 following the voice prompts to review the network setting. |
|---|---|
| Step 2 | If you have assigned a static IP address to the phone, check the  setting for the TFTP Server 1 option. See the Cisco Unified IP Phone Network Settings Setup . |
| Step 3 | If you are using DHCP, the phone obtains the address for the TFTP
                                             			 server from the DHCP server. Check the IP address configured in Option 150 or
                                             			 Option 66. |
| Step 4 | Enable the phone to use an alternate TFTP server.
                                             			 Such a setting is particularly useful if the phone was recently moved from one
                                             			 location to another. See the Cisco Unified IP Phone Network Settings Setup for instructions. |

| Note | When you remove a phone
                                                   				from the CiscoUnified Communications Manager database, the Cisco Unified Communications Manager deletes the configuration
                                                   file from the TFTP server. The
                                                   				assigned directory numbers for the phone remain in the CiscoUnified Communications
                                                   				Manager database. They are called unassigned DNs and can be assigned to other devices. If
                                                   				unassigned DNs are not used by other devices, delete them from the
                                                   				CiscoUnifiedCommunications Manager database. You can use the Route Plan
                                                   				Report to view and delete unassigned reference numbers. Refer toFor more information, see Cisco
                                                      				  UnifiedCommunications Manager Administration Guide . Changing the buttons on
                                                   				a phone button template, or assigning a different phone button template to a
                                                   				phone, may result in directory numbers that are no longer accessible from the
                                                   				phone. The directory numbers are still assigned to the phone in the
                                                   				CiscoUnified Communications Manager database, but there is no button on the
                                                   				phone for the line, meaning that no calls to the number can be answered. These directory numbers should be
                                                   				removed from the phone and deleted if necessary. |
|---|---|

| Step 1 | From CiscoUnifiedCommunications Manager, choose Device > Phone > Find to locate the phone experiencing problems. |
|---|---|
| Step 2 | Choose Delete to remove the phone from the
                                             			 CiscoUnifiedCommunications Manager database. |
| Step 3 | Add the phone back to the CiscoUnifiedCommunications Manager
                                             			 database. See the Cisco Unified Communications Manager Phone Addition Methods for details. |
| Step 4 | Power cycle the phone. |

| Step 1 | Use the Reset Settings menu to reset phone settings to their
                                             			 default values. For more information, see Cisco Unified IP Phone Reset or Restore . |
|---|---|
| Step 2 | Modify DHCP and IP settings: Disable DHCP. For instructions, see Cisco Unified IP Phone Network Settings Setup . Assign static IP values to the phone. For instructions, see Cisco Unified IP Phone Network Settings Setup . Use the same default router setting used for other
                                                   				  functioning CiscoUnified IP Phones. Assign a TFTP server. For instructions, see Cisco Unified IP Phone Network Settings Setup . Use the same TFTP server used for other functioning
                                                   				  CiscoUnified IP Phones. |
| Step 3 | On the CiscoUnifiedCommunications Manager server, verify that
                                             			 the local host files have the correct CiscoUnifiedCommunications Manager
                                             			 server name mapped to the correct IP address. |
| Step 4 | From CiscoUnifiedCommunications Manager, choose System > Server and verify that the server is referred to by the  IP address and not by the  DNS
                                             			 name. |
| Step 5 | From CiscoUnifiedCommunications Manager, choose Device > Phone > Find and verify that you have assigned the correct MAC address to this CiscoUnified
                                             			 IP Phone. For information about determining a MAC address, see the Cisco Unified IP Phones and Different Protocols . |
| Step 6 | Power cycle the phone. |

| Note | A service must be activated before it can be started or stopped. To
                                                			 activate a service, choose Tools > Service
                                                      				  Activation . |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration, choose Cisco Unified Serviceability from the
                                             			 Navigation drop-down list and click Go . |
|---|---|
| Step 2 | Choose Tools > Control
                                                   				  Center - Feature Services . |
| Step 3 | Choose the primary Cisco Unified Communications Manager server
                                             			 from the Server drop-down list. The window displays the service names for the server that you
                                                				chose, the status of the services, and a service control panel to start or stop
                                                				a service. |
| Step 4 | If a service has stopped, click the corresponding radio button and then click Start . The Service Status symbol changes from a square to an arrow. |

| Summary | Explanation |
|---|---|
| Connecting a Cisco Unified IP Phone to another Cisco Unified
                                             					 IP Phone through the PC port. | Cisco does not support connecting an IP Phone to another IP
                                             					 Phone through the PC port. Each IP Phone should directly connect to a switch
                                             					 port. If phones are connected together in a line (by using the PC port), the
                                             					 phones will not work. |
| Prolonged broadcast storms cause IPphones to reset, or be
                                             					 unable to make or answer a call. | A prolonged Layer 2 broadcast storm (lasting several minutes)
                                             					 on the voice VLAN may cause IP phones to reset, lose an active call, or be
                                             					 unable to initiate or answer a call. Phones may not regain connectivity  until a broadcast
                                             					 storm ends. |
| Moving a network connection from the phone to a workstation. | If you power your phone through the network connection,
                                             					 you must be careful if you decide to unplug the network connection of the phone and
                                             					 plug the cable into a desktop computer. Caution The computer network card cannot receive power through the
                                                         						network connection; if power comes through the connection, the network card can
                                                         						be destroyed. To protect a network card, wait 10 seconds or longer after
                                                         						unplugging the cable from the phone before plugging it into a computer. This
                                                         						delay gives the switch enough time to recognize that there is no longer a phone
                                                         						on the line and to stop providing power to the cable. | Caution | The computer network card cannot receive power through the
                                                         						network connection; if power comes through the connection, the network card can
                                                         						be destroyed. To protect a network card, wait 10 seconds or longer after
                                                         						unplugging the cable from the phone before plugging it into a computer. This
                                                         						delay gives the switch enough time to recognize that there is no longer a phone
                                                         						on the line and to stop providing power to the cable. |
| Caution | The computer network card cannot receive power through the
                                                         						network connection; if power comes through the connection, the network card can
                                                         						be destroyed. To protect a network card, wait 10 seconds or longer after
                                                         						unplugging the cable from the phone before plugging it into a computer. This
                                                         						delay gives the switch enough time to recognize that there is no longer a phone
                                                         						on the line and to stop providing power to the cable. |
| Changing the telephone configuration. | By default, the network configuration options are locked to
                                             					 prevent users from making changes that could impact their network connectivity.
                                             					 You must unlock the network configuration options before you can configure
                                             					 them. See the Access Phone Configuration Settings for details. |
| Phone resetting. | The phone resets when it loses contact with the Cisco
                                             					 UnifiedCommunications Manager software. This lost connection can be due to any
                                             					 network connectivity disruption, including cable breaks, switch outages, and
                                             					 switch reboots. |
| Codec mismatch between the phone and another device. | The RxType and the TxType statistics show the codec that is
                                             					 being used for a conversation between this Cisco UnifiedIPphone and the other
                                             					 device. The values of these statistics should match. If they do not match,
                                             					 verify that the other device can handle the codec conversation or that a
                                             					 transcoder is in place to handle the service. |
| Sound sample mismatch between the phone and another device. | The RxSize and the TxSize statistics show the size of the
                                             					 voice packets that are being used in a conversation between this Cisco
                                             					 UnifiedIPphone and the other device. The values of these statistics should
                                             					 match. |
| Loopback condition. | A loopback condition can occur when the following conditions
                                             					 are met: The SW Port
                                                						Configuration option in the Network Configuration menu on the phone is set to 10 Half (10-BaseT / half duplex) The phone receives
                                                						power from an external power supply The phone is
                                                						powered down (the power supply is disconnected) In this case, the switch port on the phone can become disabled
                                             					 and the following message will appear in the switch console log: HALF_DUX_COLLISION_EXCEED_THRESHOLD To resolve this problem, reenable the port from the switch. |

| Caution | The computer network card cannot receive power through the
                                                         						network connection; if power comes through the connection, the network card can
                                                         						be destroyed. To protect a network card, wait 10 seconds or longer after
                                                         						unplugging the cable from the phone before plugging it into a computer. This
                                                         						delay gives the switch enough time to recognize that there is no longer a phone
                                                         						on the line and to stop providing power to the cable. |
|---|---|

| Operation | Performing | Explanation |
|---|---|---|
| Restart phone | Unplug the power cable and plug it back in. | Resets any user and network configuration changes that you have made, but that the phone has not written to flash memory,
                                                to previously saved settings, then restarts the phone. |
| Reset Settings | Reset the phone to the  factory settings. | Resets user and network configuration settings to their default values, and restarts the phone. |

| Step 1 | Unplug the power cable from the phone and then plug it back in. The phone begins its power-up cycle. |
|---|---|
| Step 2 | While the phone is powering up, press and hold # button until the
                                             			 Line LED turns green. |
| Step 3 | Release the # button and press 123456789*0# . The line button LED turns red. The phone reboots when it is
                                                				finished. |

| Note | Concealment ratio and concealment seconds are primary measurements
                                          		  based on frame loss. A Conceal Ratio of zero indicates that the IP network is
                                          		  delivering frames and packets on time with no loss. |
|---|---|

| Metric change | Condition |
|---|---|
| Conceal Ratio and Conceal Seconds increase significantly | Network impairment from packet loss or high jitter. |
| Conceal Ratio is near or at zero, but the voice quality is poor. | Noise or distortion in the audio channel such as echo or audio levels. Tandem calls that undergo multiple encode/decode such as calls to a cellular network or calling card network. Acoustic problems coming from a speakerphone, handsfree cellular phone or wireless headset. Check packet transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice packets are flowing. |
| MOS LQK scores decrease significantly | Network impairment from packet loss or high jitter levels: Average MOS LQK decreases may indicate widespread and uniform impairment. Individual MOS LQK decreases may indicate bursty impairment. Cross-check the conceal ratio and conceal seconds for evidence of packet loss and jitter. |
| MOS LQK scores increase significantly | Check to see if the phone is using a different codec than expected (RxType and TxType). Check to see if the MOS LQK version changed after a firmware upgrade. |

| Note | Voice quality metrics do not account for noise or distortion, only frame loss. |
|---|---|