---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-10-0-english-admin-guide-ip05-bk-a6e3f5ab-00-adminguide-3905-10--e9794a9600
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/10_0/english/admin_guide/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0_chapter_01010.html
retrieved_at: 2026-08-21T14:35:29.615079+00:00
---

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

# Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

Updated: May 9, 2025

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Troubleshooting Overview

This chapter provides information that can assist you in
                           		troubleshooting problems with your Cisco Unified IP Phone or with your IP
                           		telephony network. It also explains how to maintain your voice network and
                           		clean your phone.

If you need additional assistance to resolve an issue, see Documentation, Support, and Security Guidelines .

This chapter includes these topics:

## Startup
                        	 Problems

After you install a phone into your network and add it to Cisco Unified Communications Manager, the phone should start up
                           as described in the related topic below.

If the
                           		phone does not start up properly, see the following sections for
                           		troubleshooting information.

### Cisco IP Phone
                           	 Does Not Go Through the Normal Startup Process

#### Problem

When you
                                 		  connect a Cisco IP Phone to the network port, the phone does not go through the
                                 		  normal startup process as described in the related topic and the phone screen
                                 		  does not display information.

#### Cause

If the
                                 		  phone does not go through the startup process, the cause may be faulty cables,
                                 		  bad connections, network outages, lack of power, or the phone may not be
                                 		  functional.

#### Solution

To
                                 		  determine whether the phone is functional, use the following suggestions to
                                 		  eliminate other potential problems.

Verify that
                                       				the network port is functional:

Exchange
                                             					 the Ethernet cables with cables that you know are functional.

Disconnect
                                             					 a functioning Cisco IP Phone from another port and connect it to this network
                                             					 port to verify that the port is active.

Connect
                                             					 the Cisco IP Phone that does not start up to a different network port that is
                                             					 known to be good.

Connect
                                             					 the Cisco IP Phone that does not start up directly to the port on the switch,
                                             					 eliminating the patch panel connection in the office.

Verify that
                                       				the phone is receiving power:

If you are
                                             					 using external power, verify that the electrical outlet is functional.

If you are
                                             					 using in-line power, use the external power supply instead.

If you are
                                             					 using the external power supply, switch with a unit that you know to be
                                             					 functional.

If the phone still does not start up properly, power up the phone from the backup software image.

If the phone
                                       				still does not start up properly, perform a factory reset of the phone.

After you
                                       				attempt these solutions, if the phone screen on the Cisco IP Phone does not
                                       				display any characters after at least five minutes, contact a Cisco technical
                                       				support representative for additional assistance.

### Cisco IP Phone Does Not Register with Cisco Unified Communications Manager

If the phone proceeds past the first stage of the startup process (LED buttons flashing on and off) but continues to cycle
                                 through the messages that displays on the phone screen, the phone is not starting up properly. The phone cannot successfully
                                 start up unless it  connects to the Ethernet network and it registers with a Cisco Unified Communications Manager server.

In addition, problems with security may prevent the phone from starting up properly. See Troubleshooting Procedures for more information.

### Phone Displays
                           	 Error Messages

#### Problem

Status
                                 		  messages display errors during startup.

#### Solution

While the
                                 		  phone cycles through the startup process, you can access status messages that
                                 		  might provide you with information about the cause of a problem. See the "Display
                                    		  Status Messages Window" section for instructions about accessing status messages
                                 		  and for a list of potential errors, their explanations, and their solutions.

#### Phone Cannot Connect to TFTP Server or to Cisco Unified Communications Manager

##### Problem

If the network is down between the phone and either the TFTP server or Cisco Unified Communications Manager, the phone cannot
                                    start up properly.

##### Solution

Ensure that the network is currently running.

#### Phone Cannot
                              	 Connect to TFTP Server

##### Problem

The TFTP
                                    		  server settings may not be correct.

##### Solution

Check the
                                    		  TFTP settings.

#### Phone Cannot
                              	 Connect to Server

##### Problem

The IP
                                    		  addressing and routing fields may not be configured correctly.

##### Solution

You
                                    		  should verify the IP addressing and routing settings on the phone. If you are
                                    		  using DHCP, the DHCP server should provide these values. If you have assigned a
                                    		  static IP address to the phone, you must enter these values manually.

### Cisco Unified Communications Manager and TFTP Services Are Not Running

#### Problem

If the Cisco Unified Communications Manager or TFTP services are not running, phones may not be able to start up properly.
                                 In such a situation, it is likely that you are experiencing a systemwide failure, and other phones and devices are unable
                                 to start up properly.

#### Solution

If the Cisco Unified Communications Manager service is not running, all devices on the network that rely on it to make phone
                                 calls are affected. If the TFTP service is not running, many devices cannot start up successfully. For more information, see Start Service .

### Configuration File Corruption

#### Problem

If you continue to have problems with a particular phone that
                                 		  other suggestions in this chapter do not resolve, the configuration file may be
                                 		  corrupted.

#### Solution

Create a new phone configuration file.

### Cisco Unified Communications Manager Phone Registration

#### Problem

The phone is not registered with the Cisco Unified
                                 		  Communications Manager

#### Solution

A Cisco IP Phone can register with a Cisco Unified
                                 		  Communications Manager server only if the phone is added to the server or if
                                 		  autoregistration is enabled. Review the information and procedures in Phone Addition Methods to ensure that the phone is added to the Cisco Unified Communications Manager
                                 		  database.

To verify that the phone is in the Cisco Unified
                                 		  Communications Manager database, choose Device > Phone from Cisco Unified Communications Manager Administration. Click Find to search for the
                                 		  phone based on the MAC Address. For information about determining a MAC
                                 		  address, see Determine the Phone MAC Address .

If the phone is already in the Cisco Unified Communications
                                 		  Manager database, the configuration file may be damaged. See Configuration File Corruption for assistance.

### Cisco IP Phone Cannot Obtain IP Address

#### Problem

If a phone cannot  obtain an IP address when it starts up, the phone may not be on the same network or VLAN as the DHCP server,
                                 or the switch port to which the phone connects may be disabled.

#### Solution

Ensure that the network or VLAN to which the phone  connects has access to the DHCP server, and ensure that the switch port
                                 is enabled.

## Phone Reset Problems

If users report that their phones are resetting during calls or while the phones are idle, you should investigate the cause.
                           If the network connection and Cisco Unified Communications Manager connection are stable, a phone should not reset.

Typically, a phone resets if it has problems in connecting to the network or to Cisco Unified Communications Manager.

### Phone Cannot Connect to LAN

#### Problem

The physical connection to the LAN may be broken.

#### Solution

Verify that the Ethernet connection to which the Cisco IP Phone connects is up. For example, check whether the particular
                                 port or switch to which the phone connects is down and that the switch is not rebooting. Also ensure that no cable breaks
                                 exist.

### Phone Resets Due to Intermittent Network Outages

#### Problem

Your network may be experiencing intermittent outages.

#### Solution

Intermittent network outages affect data and voice traffic differently. Your network might be experiencing intermittent outages
                                 without detection. If so, data traffic can resend lost packets and verify that packets are received and transmitted. However,
                                 voice traffic cannot recapture lost packets. Rather than retransmitting a lost network connection, the phone resets and attempts
                                 to reconnect to the network. Contact the system administrator for information on known problems in the voice network.

### Phone Resets Due to DHCP Setting Errors

#### Problem

The DHCP settings may be incorrect.

#### Solution

Verify that you have properly configured the phone to use DHCP. Verify that the DHCP server is set up properly. Verify the
                                 DHCP lease duration. We recommend that you set the lease duration to 8 days.

### Phone Resets Due to Incorrect Static IP Address

#### Problem

The static IP address assigned to the phone may be incorrect.

#### Solution

If the phone is assigned a static IP address, verify that you have entered the correct settings.

### Phone Resets During Heavy Network Usage

#### Problem

If the phone appears to reset during heavy network usage, it is likely that you do not have a voice VLAN configured.

#### Solution

Isolating the phones on a separate auxiliary VLAN increases the quality of the voice traffic.

### Phone Resets Due to Intentional Reset

#### Problem

If you are not the only administrator with access to Cisco
                                 		  Unified Communications Manager, you should verify that no one else has
                                 		  intentionally reset the phones.

#### Solution

You can check if a Cisco IP Phone received a command from Cisco Unified Communications Manager to reset by pressing Applications on the phone and choosing Admin Settings > Status > Network Statistics .

If the Restart Cause field displays Reset-Reset , the phone receives a Reset/Reset from Cisco Unified Communications Manager
                                       				Administration.

If the Restart Cause field displays Reset-Restart , the phone
                                       				closed because it received a Reset/Restart from Cisco Unified Communications Manager
                                       				Administration.

### Phone Resets Due to DNS or Other Connectivity Issues

#### Problem

The phone reset continues and you suspect DNS or other
                                 		  connectivity issues.

#### Solution

If the phone continues to reset, eliminate DNS or other
                                 		  connectivity errors by following the procedure in Determine DNS or Connectivity Issues .

### Phone Does Not Power Up

#### Problem

The phone does not appear to be powered up.

#### Solution

In most cases, a phone restarts if it powers up by using external power but loses that connection and switches to PoE. Similarly,
                                 a phone may restart if it powers up by using PoE and then connects to an external power supply.

## Cisco IP Phone Security Problems

### 802.1X Authentication Problems

801.1X authentication problems can be broken into the
                              		  categories that are described in the following table.

Phone cannot
                                                						obtain a DHCP-assigned IP address.

Phone does not
                                                						register with Cisco Unified Communications Manager.

Phone status
                                                						displays Configuring IP or Registering .

802.1X
                                                						Authentication Status displays Held .

Status menu 802.1X
                                                						status displays Failed .

802.1X Enabled on Phone but Phone Does Not Authenticate

Phone cannot
                                                						obtain a DHCP-assigned IP address.

Phone does not
                                                						register with Cisco Unified Communications Manager.

Phone status
                                                						displays Configuring IP or Registering .

802.1X
                                                						Authentication Status displays Disabled .

Status menu
                                                						displays that the DHCP status has timed out.

802.1X Not Enabled

Phone cannot
                                                						obtain a DHCP-assigned IP address.

Phone does not
                                                						register with Cisco Unified Communications Manager.

Phone status
                                                						display as Configuring IP or Registering .

You are unable to
                                                						access phone menus to verify 802.1X status.

Factory Reset of Phone Has Deleted 802.1X Shared Secret

### 802.1X Enabled on Phone but Phone Does Not Authenticate

#### Problem

The phone cannot authenticate.

#### Cause

These errors typically indicate that 802.1X authentication is enabled on the phone, but the phone is unable to authenticate.

#### Solution

To resolve this problem,  check the 802.1X and shared secret configuration. See Identify 802.1X Authentication Problems .

### 802.1X Not
                           	 Enabled

#### Problem

The
                                 		  phone does not have 802.1X configured.

#### Cause

These
                                 		  errors typically indicate that 802.1X authentication is not enabled on the
                                 		  phone.

#### Solution

If
                                 		  802.1X is not enabled on the phone, see 802.1X Authentication section.

### Factory Reset of
                           	 Phone Has Deleted 802.1X Shared Secret

#### Problem

After a
                                 		  reset, the phone does not authenticate.

#### Cause

These
                                 		  errors typically indicate that the phone has completed a factory reset while
                                 		  802.1X was enabled. A factory reset deletes the shared secret, which is
                                 		  required for 802.1X authentication and network access.

#### Solution

To
                                 		  resolve this situation, temporarily move the phone to a network environment
                                 		  that is not using 802.1X authentication. After the phone starts up normally,
                                 		  access the 802.1X configuration menus to enable device authentication and to
                                 		  reenter the shared secret. See 802.1X Authentication section for details.

## Audio  and Video Problems

The following sections describe how to resolve audio and video problems.

### No Speech Path

#### Problem

One or more people on a call do not hear any audio.

#### Solution

When at least one person in a call does not receive audio, IP connectivity between phones is not established. Check the configuration
                                 of routers and switches to ensure that IP connectivity is properly configured.

### Choppy Speech

#### Problem

A user complains of choppy speech on a call.

#### Cause

There may be a mismatch in the jitter configuration.

#### Solution

Check the AvgJtr and the MaxJtr statistics. A large variance between these statistics
                                 might indicate a problem with jitter on the network or periodic high rates of
                                 network activity.

### Poor Audio Quality with Calls that Route Outside Cisco Unified Communications Manager

#### Problem

Poor quality occurs with tandem audio encoding. Tandem encoding can occur when calls are made between an IP Phone and a digital
                                 cellular phone, when a conference bridge is used, or in situations where IP-to-IP calls are partially routed across the PSTN.

#### Cause

In these cases, use of voice codecs such as G.729 and iLBC may result in poor voice quality.

#### Solution

Use the G.729 and iLBC codecs only when absolutely necessary.

### Phone Display Is Wavy

#### Problem

The display appears to have rolling lines or a wavy pattern.

#### Cause

The phone might be interacting with certain types of older fluorescent lights in the building.

#### Solution

Move the phone away from the lights or replace the lights to resolve the problem.

## General Telephone Call Problems

The following sections help troubleshoot general telephone call problems.

### Phone Call Cannot Be Established

#### Problem

A user complains about not being able to make a call.

#### Cause

The phone does not have a DHCP IP address, is unable to register to Cisco Unified Communications Manager. Phones with an LCD
                                 display show the message Configuring IP or Registering . Phones without an LCD display play the reorder tone (instead of dial tone) in the handset when the user attempts to make
                                 a call.

#### Solution

Verify the following:

- The Ethernet cable is
                                          				  attached.

- The Cisco CallManager service is running on the Cisco Unified Communications Manager server.

- Both phones are
                                          				  registered to the same Cisco Unified Communications Manager.

Audio server debug and capture logs are enabled for both phones.
                                       				If needed, enable Java debug.

### Phone Does Not Recognize DTMF Digits or Digits Are Delayed

#### Problem

The user complains that numbers are missed or delayed when the keypad is used.

#### Cause

Pressing the keys too quickly can result in missed or delayed digits.

#### Solution

Keys should not be pressed rapidly.

### Phone Bandwidth Restrictions

#### Problem

Users report frequent Not  enough bandwidth messages on their phones.

#### Cause

The Cisco Unified Communications Manager  does not have adequate bandwidth to place the call or there are policy restrictions.

#### Solution

For information on changing the Cisco Unified Communications Manager  bandwidth, see the documentation for your particular
                                 version of Cisco Unified Communications Manager.

## Troubleshooting Procedures

These procedures can be used to identify and correct problems.

### Check TFTP Settings

Step 1

Check the TFTP Server 1 field.

If you have assigned a static IP address to the phone, you must
                                             			 manually enter a setting for the TFTP Server 1 option.

If you are using DHCP, the phone obtains the address for the TFTP
                                             			 server from the DHCP server. Check that the IP address is configured in Option
                                             			 150.

Step 2

You can also enable the phone to use an alternate TFTP server.
                                          			 Such a setting is particularly useful if the phone recently moved from one
                                          			 location to another.

Step 3

If the local DHCP does not offer the correct TFTP address, enable the phone to use an alternate TFTP server.

This is often necessary in VPN scenarios.

### Check DHCP
                           	 Settings

Step 1

Check the DHCP server field.

Step 2

Check the IP
                                          					 Address, Subnet Mask, and Default Router fields.

If you assign a static IP address
                                             					 to the phone, you must manually enter settings for these options.

Step 3

If you are
                                          			 using DHCP, check the IP addresses that your DHCP server distributes.

See the Understanding and Troubleshooting DHCP in Catalyst Switch or
                                                				  Enterprise Networks document, available at this URL:

https://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml

### Start Service

A service must be activated before it can be started or stopped.

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

### Create a New Phone Configuration File

When you remove a phone from the Cisco Unified Communications Manager database, the configuration file is deleted from the
                                 Cisco Unified Communications Manager TFTP server. The phone directory number or numbers remain in the Cisco Unified Communications
                                 Manager database. They are called unassigned DNs and can be used for other devices. If unassigned DNs are not used by other
                                 devices, delete these DNs from the Cisco Unified Communications Manager database. You can use the Route Plan Report to view
                                 and delete unassigned reference numbers. For more information, see the documentation for your particular Cisco Unified Communications
                                 Manager release.

Changing the buttons on a phone button template, or assigning a different phone button template to a phone, may result in
                                 directory numbers that are no longer accessible from the phone. The directory numbers are still assigned to the phone in the
                                 Cisco Unified Communications Manager database, but the phone has no button on the phone with which calls can be answered.
                                 These directory numbers should be removed from the phone and deleted if necessary.

Step 1

From Cisco Unified Communications Manager,
                                          			 choose Device > Phone and click Find to locate the phone that is experiencing problems.

Step 2

Choose Delete to remove the phone from the Cisco
                                          			 Unified Communications Manager database.

When you remove a phone from the Cisco Unified Communications
                                                         				  Manager database, the configuration file is deleted from the Cisco Unified
                                                         				  Communications Manager TFTP server. The phone directory number or numbers
                                                         				  remain in the Cisco Unified Communications Manager database. They are called 
                                                         				  unassigned DNs and can be used for other devices. If
                                                         				  unassigned DNs are not used by other devices, delete these DNs from the Cisco
                                                         				  Unified Communications Manager database. You can use the Route Plan Report to
                                                         				  view and delete unassigned reference numbers.

Step 3

Add the phone back to the Cisco Unified Communications Manager
                                          			 database.

Step 4

Power cycle the phone.

### Determine DNS or Connectivity Issues

Step 1

Use the Reset Settings menu to reset phone settings to their
                                          			 default values.

Step 2

Modify DHCP and IP settings:

Disable DHCP.

Assign static IP values to the phone. Use the same default router setting that other functioning
                                                				  phones use.

Assign a TFTP server. Use the same TFTP server that other functioning phones use.

Step 3

On the Cisco Unified Communications Manager server, verify that
                                          			 the local host files have the correct Cisco Unified Communications Manager
                                          			 server name mapped to the correct IP address.

Step 4

From Cisco Unified Communications Manager, choose System > Server and verify
                                          			 that reference to the server is made by the IP address and not by the DNS name.

Step 5

From Cisco Unified Communications Manager, choose Device > Phone . Click Find to search for this phone. Verify that you have assigned the correct MAC address to this Cisco IP Phone.

Step 6

Power cycle the phone.

### Identify 802.1X
                           	 Authentication Problems

Step 1

Verify that
                                          			 you have properly configured the required components.

Step 2

Confirm that
                                          			 the shared secret is configured on the phone.

If the
                                                   					 shared secret is configured, verify that you have the same shared secret on the
                                                   					 authentication server.

If the
                                                   					 shared secret is not configured on the phone, enter it, and ensure that it
                                                   					 matches the shared secret on the authentication server.

### Verify DNS Settings

Check that the DNS Server 1 field is set correctly.

## Additional Troubleshooting Information

If you have additional questions about troubleshooting your phone, go to the following Cisco website and  navigate to the
                           desired phone model:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html#Troubleshooting

| If all the following conditions apply, | See |
|---|---|
| Phone cannot
                                                						obtain a DHCP-assigned IP address. Phone does not
                                                						register with Cisco Unified Communications Manager. Phone status
                                                						displays Configuring IP or Registering . 802.1X
                                                						Authentication Status displays Held . Status menu 802.1X
                                                						status displays Failed . | 802.1X Enabled on Phone but Phone Does Not Authenticate |
| Phone cannot
                                                						obtain a DHCP-assigned IP address. Phone does not
                                                						register with Cisco Unified Communications Manager. Phone status
                                                						displays Configuring IP or Registering . 802.1X
                                                						Authentication Status displays Disabled . Status menu
                                                						displays that the DHCP status has timed out. | 802.1X Not Enabled |
| Phone cannot
                                                						obtain a DHCP-assigned IP address. Phone does not
                                                						register with Cisco Unified Communications Manager. Phone status
                                                						display as Configuring IP or Registering . You are unable to
                                                						access phone menus to verify 802.1X status. | Factory Reset of Phone Has Deleted 802.1X Shared Secret |

| Step 1 | Check the TFTP Server 1 field. If you have assigned a static IP address to the phone, you must
                                             			 manually enter a setting for the TFTP Server 1 option. If you are using DHCP, the phone obtains the address for the TFTP
                                             			 server from the DHCP server. Check that the IP address is configured in Option
                                             			 150. |
|---|---|
| Step 2 | You can also enable the phone to use an alternate TFTP server.
                                          			 Such a setting is particularly useful if the phone recently moved from one
                                          			 location to another. |
| Step 3 | If the local DHCP does not offer the correct TFTP address, enable the phone to use an alternate TFTP server. This is often necessary in VPN scenarios. |

| Step 1 | Check the DHCP server field. |
|---|---|
| Step 2 | Check the IP
                                          					 Address, Subnet Mask, and Default Router fields. If you assign a static IP address
                                             					 to the phone, you must manually enter settings for these options. |
| Step 3 | If you are
                                          			 using DHCP, check the IP addresses that your DHCP server distributes. See the Understanding and Troubleshooting DHCP in Catalyst Switch or
                                                				  Enterprise Networks document, available at this URL: https://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml |

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

| Step 1 | From Cisco Unified Communications Manager,
                                          			 choose Device > Phone and click Find to locate the phone that is experiencing problems. |
|---|---|
| Step 2 | Choose Delete to remove the phone from the Cisco
                                          			 Unified Communications Manager database. Note When you remove a phone from the Cisco Unified Communications
                                                         				  Manager database, the configuration file is deleted from the Cisco Unified
                                                         				  Communications Manager TFTP server. The phone directory number or numbers
                                                         				  remain in the Cisco Unified Communications Manager database. They are called 
                                                         				  unassigned DNs and can be used for other devices. If
                                                         				  unassigned DNs are not used by other devices, delete these DNs from the Cisco
                                                         				  Unified Communications Manager database. You can use the Route Plan Report to
                                                         				  view and delete unassigned reference numbers. | Note | When you remove a phone from the Cisco Unified Communications
                                                         				  Manager database, the configuration file is deleted from the Cisco Unified
                                                         				  Communications Manager TFTP server. The phone directory number or numbers
                                                         				  remain in the Cisco Unified Communications Manager database. They are called 
                                                         				  unassigned DNs and can be used for other devices. If
                                                         				  unassigned DNs are not used by other devices, delete these DNs from the Cisco
                                                         				  Unified Communications Manager database. You can use the Route Plan Report to
                                                         				  view and delete unassigned reference numbers. |
| Note | When you remove a phone from the Cisco Unified Communications
                                                         				  Manager database, the configuration file is deleted from the Cisco Unified
                                                         				  Communications Manager TFTP server. The phone directory number or numbers
                                                         				  remain in the Cisco Unified Communications Manager database. They are called 
                                                         				  unassigned DNs and can be used for other devices. If
                                                         				  unassigned DNs are not used by other devices, delete these DNs from the Cisco
                                                         				  Unified Communications Manager database. You can use the Route Plan Report to
                                                         				  view and delete unassigned reference numbers. |
| Step 3 | Add the phone back to the Cisco Unified Communications Manager
                                          			 database. |
| Step 4 | Power cycle the phone. |

| Note | When you remove a phone from the Cisco Unified Communications
                                                         				  Manager database, the configuration file is deleted from the Cisco Unified
                                                         				  Communications Manager TFTP server. The phone directory number or numbers
                                                         				  remain in the Cisco Unified Communications Manager database. They are called 
                                                         				  unassigned DNs and can be used for other devices. If
                                                         				  unassigned DNs are not used by other devices, delete these DNs from the Cisco
                                                         				  Unified Communications Manager database. You can use the Route Plan Report to
                                                         				  view and delete unassigned reference numbers. |
|---|---|

| Step 1 | Use the Reset Settings menu to reset phone settings to their
                                          			 default values. |
|---|---|
| Step 2 | Modify DHCP and IP settings: Disable DHCP. Assign static IP values to the phone. Use the same default router setting that other functioning
                                                				  phones use. Assign a TFTP server. Use the same TFTP server that other functioning phones use. |
| Step 3 | On the Cisco Unified Communications Manager server, verify that
                                          			 the local host files have the correct Cisco Unified Communications Manager
                                          			 server name mapped to the correct IP address. |
| Step 4 | From Cisco Unified Communications Manager, choose System > Server and verify
                                          			 that reference to the server is made by the IP address and not by the DNS name. |
| Step 5 | From Cisco Unified Communications Manager, choose Device > Phone . Click Find to search for this phone. Verify that you have assigned the correct MAC address to this Cisco IP Phone. |
| Step 6 | Power cycle the phone. |

| Step 1 | Verify that
                                          			 you have properly configured the required components. |
|---|---|
| Step 2 | Confirm that
                                          			 the shared secret is configured on the phone. If the
                                                   					 shared secret is configured, verify that you have the same shared secret on the
                                                   					 authentication server. If the
                                                   					 shared secret is not configured on the phone, enter it, and ensure that it
                                                   					 matches the shared secret on the authentication server. |

| Check that the DNS Server 1 field is set correctly. |
|---|