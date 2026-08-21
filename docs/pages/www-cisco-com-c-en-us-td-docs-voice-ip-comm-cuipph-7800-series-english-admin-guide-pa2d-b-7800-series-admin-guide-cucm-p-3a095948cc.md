---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-english-admin-guide-pa2d-b-7800-series-admin-guide-cucm-p-3a095948cc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/english/admin-guide/pa2d_b_7800-series-admin-guide-cucm/pa2d_b_7800-series-admin-guide-cucm_chapter_01110.html
retrieved_at: 2026-08-21T13:26:45.991412+00:00
---

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Updated: May 29, 2025

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## General
                        	 Troubleshooting Information

The
                           		following table provides general troubleshooting information for the Cisco IP
                           		Phone.

Summary

Explanation

Connecting a
                                       				Cisco IP Phone to another Cisco IP Phone

The Cisco 7832 conference phone does not have a PC port.

Prolonged
                                       				broadcast storms cause IP phones to reset, or be unable to make or answer a
                                       				call

A prolonged
                                       				Layer 2 broadcast storm (lasting several minutes) on the voice VLAN may cause
                                       				IP phones to reset, lose an active call, or be unable to initiate or answer a
                                       				call. Phones may not come up until a broadcast storm ends.

Moving a
                                       				network connection from the phone to a workstation

If you power
                                       				your phone through the network connection, you must be careful if you decide to
                                       				unplug the network connection of the phone and plug the cable into a desktop
                                       				computer.

Caution

The network
                                                   				  card in the computer cannot receive power through the network connection; if
                                                   				  power comes through the connection, the network card can be destroyed. To
                                                   				  protect a network card, wait 10 seconds or longer after unplugging the cable
                                                   				  from the phone before plugging it into a computer. This delay gives the switch
                                                   				  enough time to recognize that there is no longer a phone on the line and to
                                                   				  stop providing power to the cable.

Changing the
                                       				telephone configuration

By default,
                                       				the administrator password settings are locked to prevent users from making
                                       				changes that could impact their network connectivity. You must unlock the
                                       				administrator password settings before you can configure them.

See Apply a Phone Password for details.

Codec mismatch
                                       				between the phone and another device

The RxType and
                                       				the TxType statistics show the codec that is used for a conversation between
                                       				this Cisco IP Phone and the other device. The values of these statistics should
                                       				match. If they do not, verify that the other device can handle the codec
                                       				conversation, or that a transcoder is in place to handle the service. See Display Call Statistics Window for details.

Sound sample
                                       				mismatch between the phone and another device

The RxSize and
                                       				the TxSize statistics show the size of the voice packets that are used in a
                                       				conversation between this Cisco IP Phone and the other device. The values of
                                       				these statistics should match. See Display Call Statistics Window for details.

Loopback
                                       				condition

A loopback
                                       				condition can occur when the following conditions are met:

- The SW Port Configuration
                                          				  option on the phone is set to 10 Half (10-BaseT/half duplex).

- The phone receives power
                                          				  from an external power supply.

- The phone is powered down
                                          				  (the power supply is disconnected).

In this case,
                                       				the switch port on the phone can become disabled and the following message
                                       				appears in the switch console log:

HALF_DUX_COLLISION_EXCEED_THRESHOLD

To resolve
                                       				this problem, reenable the port from the switch.

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

If the phone
                                       				still does not start up properly, power up the phone by pressing #*2.
                                       				When the phone is powered up in this way, it attempts to launch a backup
                                       				software image.

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

#### Phone Cannot
                              	 Connect Using DNS

##### Problem

The DNS settings may be incorrect.

##### Solution

If you use DNS to access the TFTP server or Cisco Unified Communications Manager, you must ensure that you specify a DNS server.

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

## Phone Cannot Connect to LAN

### Problem

The physical connection to the LAN may be broken.

### Solution

Verify that the Ethernet connection to which the Cisco IP Phone connects is up. For example, check whether the particular
                              port or switch to which the phone connects is down and that the switch is not rebooting. Also ensure that no cable breaks
                              exist.

## Cisco IP Phone Security Problems

The following sections provide troubleshooting information for the security features on the Cisco IP Phone. For information
                           about the solutions for any of these issues, and for additional troubleshooting information about security, see Cisco Unified Communications Manager Security Guide .

### CTL File Problems

The following sections describe troubleshooting problems with the CTL file.

#### Authentication Error, Phone Cannot Authenticate CTL File

##### Problem

A device authentication error occurs.

##### Cause

CTL file does not have a Cisco Unified Communications Manager certificate or has an incorrect certificate.

##### Solution

Install a correct certificate.

#### Phone Cannot Authenticate CTL File

##### Problem

Phone cannot authenticate the CTL file.

##### Cause

The security token that signed the updated CTL file does not exist in the CTL file on the phone.

##### Solution

Change the security token in the CTL file and install the new file on the phone.

#### CTL File Authenticates but Other Configuration Files Do Not Authenticate

##### Problem

Phone cannot authenticate any  configuration files
                                    		  other than the CTL file.

##### Cause

A bad TFTP record exists, or the configuration file may
                                    		  not be signed by the corresponding certificate in the phone Trust List.

##### Solution

Check the TFTP record and the certificate in the Trust List.

#### ITL File Authenticates but Other Configuration Files Do Not Authenticate

##### Problem

Phone cannot authenticate any  configuration files
                                    		  other than the ITL file.

##### Cause

The configuration file may not be signed by the
                                    		  corresponding certificate in the phone Trust List.

##### Solution

Re-sign the configuration file by using the correct certificate.

#### TFTP Authorization Fails

##### Problem

Phone reports TFTP authorization failure.

##### Cause

The TFTP address for the phone does not exist in the CTL file.

If you created a new CTL file with a new TFTP record, the existing CTL file on the phone may not contain a record for the
                                    new TFTP server.

##### Solution

Check the configuration of the TFTP address in the phone CTL file.

#### Phone Does Not Register

##### Problem

Phone does not register with Cisco Unified Communications Manager.

##### Cause

The CTL file does not contain the correct information for the Cisco Unified Communications Manager server.

##### Solution

Change the Cisco Unified Communications Manager server information in the CTL file.

#### Signed Configuration Files Are Not Requested

##### Problem

Phone does not request signed configuration files.

##### Cause

The CTL file does not contain any TFTP entries with certificates.

##### Solution

Configure TFTP entries with certificates in the CTL file.

## Audio Problems

The following sections describe how to resolve audio problems.

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

## Troubleshooting Procedures

These procedures can be used to identify and correct problems.

### Create a Phone Problem Report from Cisco Unified Communications Manager

You can generate a problem report for the phones from Cisco Unified Communications Manager. This action results in the same
                                 information that the Problem Report Tool (PRT) softkey generates on the phone.

The problem report contains information about the phone and the headsets.

Step 1

In Cisco Unified CM Administration, select Device > Phone .

Step 2

Click Find and select one or more Cisco IP Phones.

Step 3

Click Generate PRT for Selected to collect PRT logs for the headsets used on the selected Cisco IP Phones.

### Create a Console Log from Your Phone

You generate a console log when your phone will not connect to the network and you cannot access the Problem Report Tool (PRT).

#### Before you begin

Connect a console cable to the Auxiliary port on the back of your phone.

Step 1

On your phone, press Applications .

Step 2

Navigate Admin settings > Aux port .

Step 3

Select Collect console log to collect device logs.

### Check TFTP Settings

Step 1

On the phone, press Applications .

Step 2

Select Admin
                                                				  Settings > Network Setup > IPv4 Setup .

Step 3

Check the TFTP Server 1 field.

If you have assigned a static IP address to the phone, you must
                                             			 manually enter a setting for the TFTP Server 1 option.

If you are using DHCP, the phone obtains the address for the TFTP
                                             			 server from the DHCP server. Check that the IP address is configured in Option
                                             			 150.

Step 4

You can also enable the phone to use an alternate TFTP server.
                                          			 Such a setting is particularly useful if the phone recently moved from one
                                          			 location to another.

Step 5

If the local DHCP does not offer the correct TFTP address, enable the phone to use an alternate TFTP server.

This is often necessary in VPN scenarios.

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

### Check DHCP
                           	 Settings

Step 1

On the phone, press Applications .

Step 2

Select Admin
                                                				  Settings > Network Setup > IPv4 Setup .

Step 3

Check the DHCP server field.

If you have assigned a static IP address to the phone, you do not need
                                             					 to enter a value for the DHCP Server option. However, if you are using a DHCP
                                             					 server, this option must have a value. If no value is found, check your IP
                                             					 routing and VLAN configuration. See the Troubleshooting Switch Port and Interface Problems document, available at this URL:

https://www.cisco.com/en/US/customer/products/hw/switches/ps708/prod_tech_notes_list.html

Step 4

Check the IP
                                          					 Address, Subnet Mask, and Default Router fields.

If you assign a static IP address
                                             					 to the phone, you must manually enter settings for these options.

Step 5

If you are
                                          			 using DHCP, check the IP addresses that your DHCP server distributes.

See the Understanding and Troubleshooting DHCP in Catalyst Switch or
                                                				  Enterprise Networks document, available at this URL:

https://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml

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

### Verify DNS Settings

Step 1

On the phone, press Applications .

Step 2

Select Admin
                                                				  Settings > Network Setup > IPv4 Setup

Step 3

Check that the DNS Server 1 field is set correctly.

Step 4

You should also verify that a CNAME entry was made in the DNS
                                          			 server for the TFTP server and for the Cisco Unified Communications Manager
                                          			 system.

You must also ensure that DNS is configured to do reverse
                                             				lookups.

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

## Control Debug
                        	 Information from Cisco Unified Communications Manager

If you are
                              		  experiencing phone problems that you cannot resolve, Cisco TAC can assist you.
                              		  You will need to turn debugging on for the phone, reproduce the problem, turn
                              		  debugging off, and send the logs to TAC for analysis.

Because debugging
                              		  captures detailed information, the communication traffic can slow down the
                              		  phone, making it less responsive. After you capture the logs, you should turn
                              		  debugging off to ensure phone operation.

0 - Emergency

1 - Alert

2 - Critical

3 - Error

4 - Warn

5 -
                                       				Notification

6 -
                                       				Information

7 - Debugging

Contact Cisco TAC
                              		  for more information and assistance.

Step 1

In the Cisco
                                       			 Unified Communications Manager Administration, select one of the following
                                       			 windows:

Device > Device
                                                      						  settings > Common Phone Profile

System > Enterprise Phone
                                                      						  Configuration

Device > Phone

Step 2

Set the
                                       			 following parameters:

To implement multilevel and multi-section support of the parameters, check the Log Profile check box.

- Remote Log - values:
                                          				Disable (default), Enable

- IPv6 Log Server or Log Server - IP address (IPv4 or IPv6 address)

When the Log
                                                      				  Server cannot be reached, the phone stops sending debug messages.

The format
                                                					 for the IPv4 Log Server address is address:<port>@@base=<0-7>;pfs=<0-1>

The
                                                					 format for the IPv6 Log Server address is [address]:<port>@@base=<0-7>;pfs=<0-1>

Where:

the
                                                      						  IPv4 address is separated with dot (.)

the
                                                      						  IPv6 address is separated with colon (:)

## Additional Troubleshooting Information

If you have additional questions about troubleshooting your phone, go to the following Cisco website and  navigate to the
                           desired phone model:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html#Troubleshooting

| Summary | Explanation |
|---|---|
| Connecting a
                                       				Cisco IP Phone to another Cisco IP Phone | Cisco does not
                                       				support connecting an IP phone to another IP Phone through the PC port. Each IP
                                       				Phone should connect directly to a switch port. If phones are connected
                                       				together in a line by using the PC port, the phones do not work. Note The Cisco 7832 conference phone does not have a PC port. | Note | The Cisco 7832 conference phone does not have a PC port. |
| Note | The Cisco 7832 conference phone does not have a PC port. |
| Prolonged
                                       				broadcast storms cause IP phones to reset, or be unable to make or answer a
                                       				call | A prolonged
                                       				Layer 2 broadcast storm (lasting several minutes) on the voice VLAN may cause
                                       				IP phones to reset, lose an active call, or be unable to initiate or answer a
                                       				call. Phones may not come up until a broadcast storm ends. |
| Moving a
                                       				network connection from the phone to a workstation | If you power
                                       				your phone through the network connection, you must be careful if you decide to
                                       				unplug the network connection of the phone and plug the cable into a desktop
                                       				computer. Caution The network
                                                   				  card in the computer cannot receive power through the network connection; if
                                                   				  power comes through the connection, the network card can be destroyed. To
                                                   				  protect a network card, wait 10 seconds or longer after unplugging the cable
                                                   				  from the phone before plugging it into a computer. This delay gives the switch
                                                   				  enough time to recognize that there is no longer a phone on the line and to
                                                   				  stop providing power to the cable. | Caution | The network
                                                   				  card in the computer cannot receive power through the network connection; if
                                                   				  power comes through the connection, the network card can be destroyed. To
                                                   				  protect a network card, wait 10 seconds or longer after unplugging the cable
                                                   				  from the phone before plugging it into a computer. This delay gives the switch
                                                   				  enough time to recognize that there is no longer a phone on the line and to
                                                   				  stop providing power to the cable. |
| Caution | The network
                                                   				  card in the computer cannot receive power through the network connection; if
                                                   				  power comes through the connection, the network card can be destroyed. To
                                                   				  protect a network card, wait 10 seconds or longer after unplugging the cable
                                                   				  from the phone before plugging it into a computer. This delay gives the switch
                                                   				  enough time to recognize that there is no longer a phone on the line and to
                                                   				  stop providing power to the cable. |
| Changing the
                                       				telephone configuration | By default,
                                       				the administrator password settings are locked to prevent users from making
                                       				changes that could impact their network connectivity. You must unlock the
                                       				administrator password settings before you can configure them. See Apply a Phone Password for details. Note If the
                                                   				  administrator password is not set in common phone profile, then user can modify
                                                   				  the network settings. | Note | If the
                                                   				  administrator password is not set in common phone profile, then user can modify
                                                   				  the network settings. |
| Note | If the
                                                   				  administrator password is not set in common phone profile, then user can modify
                                                   				  the network settings. |
| Codec mismatch
                                       				between the phone and another device | The RxType and
                                       				the TxType statistics show the codec that is used for a conversation between
                                       				this Cisco IP Phone and the other device. The values of these statistics should
                                       				match. If they do not, verify that the other device can handle the codec
                                       				conversation, or that a transcoder is in place to handle the service. See Display Call Statistics Window for details. |
| Sound sample
                                       				mismatch between the phone and another device | The RxSize and
                                       				the TxSize statistics show the size of the voice packets that are used in a
                                       				conversation between this Cisco IP Phone and the other device. The values of
                                       				these statistics should match. See Display Call Statistics Window for details. |
| Loopback
                                       				condition | A loopback
                                       				condition can occur when the following conditions are met: The SW Port Configuration
                                          				  option on the phone is set to 10 Half (10-BaseT/half duplex). The phone receives power
                                          				  from an external power supply. The phone is powered down
                                          				  (the power supply is disconnected). In this case,
                                       				the switch port on the phone can become disabled and the following message
                                       				appears in the switch console log: HALF_DUX_COLLISION_EXCEED_THRESHOLD To resolve
                                       				this problem, reenable the port from the switch. |

| Note | The Cisco 7832 conference phone does not have a PC port. |
|---|---|

| Caution | The network
                                                   				  card in the computer cannot receive power through the network connection; if
                                                   				  power comes through the connection, the network card can be destroyed. To
                                                   				  protect a network card, wait 10 seconds or longer after unplugging the cable
                                                   				  from the phone before plugging it into a computer. This delay gives the switch
                                                   				  enough time to recognize that there is no longer a phone on the line and to
                                                   				  stop providing power to the cable. |
|---|---|

| Note | If the
                                                   				  administrator password is not set in common phone profile, then user can modify
                                                   				  the network settings. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, select Device > Phone . |
|---|---|
| Step 2 | Click Find and select one or more Cisco IP Phones. |
| Step 3 | Click Generate PRT for Selected to collect PRT logs for the headsets used on the selected Cisco IP Phones. |

| Step 1 | On your phone, press Applications . |
|---|---|
| Step 2 | Navigate Admin settings > Aux port . |
| Step 3 | Select Collect console log to collect device logs. |

| Step 1 | On the phone, press Applications . |
|---|---|
| Step 2 | Select Admin
                                                				  Settings > Network Setup > IPv4 Setup . |
| Step 3 | Check the TFTP Server 1 field. If you have assigned a static IP address to the phone, you must
                                             			 manually enter a setting for the TFTP Server 1 option. If you are using DHCP, the phone obtains the address for the TFTP
                                             			 server from the DHCP server. Check that the IP address is configured in Option
                                             			 150. |
| Step 4 | You can also enable the phone to use an alternate TFTP server.
                                          			 Such a setting is particularly useful if the phone recently moved from one
                                          			 location to another. |
| Step 5 | If the local DHCP does not offer the correct TFTP address, enable the phone to use an alternate TFTP server. This is often necessary in VPN scenarios. |

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

| Step 1 | On the phone, press Applications . |
|---|---|
| Step 2 | Select Admin
                                                				  Settings > Network Setup > IPv4 Setup . |
| Step 3 | Check the DHCP server field. If you have assigned a static IP address to the phone, you do not need
                                             					 to enter a value for the DHCP Server option. However, if you are using a DHCP
                                             					 server, this option must have a value. If no value is found, check your IP
                                             					 routing and VLAN configuration. See the Troubleshooting Switch Port and Interface Problems document, available at this URL: https://www.cisco.com/en/US/customer/products/hw/switches/ps708/prod_tech_notes_list.html |
| Step 4 | Check the IP
                                          					 Address, Subnet Mask, and Default Router fields. If you assign a static IP address
                                             					 to the phone, you must manually enter settings for these options. |
| Step 5 | If you are
                                          			 using DHCP, check the IP addresses that your DHCP server distributes. See the Understanding and Troubleshooting DHCP in Catalyst Switch or
                                                				  Enterprise Networks document, available at this URL: https://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml |

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

| Step 1 | On the phone, press Applications . |
|---|---|
| Step 2 | Select Admin
                                                				  Settings > Network Setup > IPv4 Setup |
| Step 3 | Check that the DNS Server 1 field is set correctly. |
| Step 4 | You should also verify that a CNAME entry was made in the DNS
                                          			 server for the TFTP server and for the Cisco Unified Communications Manager
                                          			 system. You must also ensure that DNS is configured to do reverse
                                             				lookups. |

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

| Step 1 | In the Cisco
                                       			 Unified Communications Manager Administration, select one of the following
                                       			 windows: Device > Device
                                                      						  settings > Common Phone Profile System > Enterprise Phone
                                                      						  Configuration Device > Phone |
|---|---|
| Step 2 | Set the
                                       			 following parameters: Log Profile - values: Preset (default), Default, Telephony, SIP, UI, Network, Media, Upgrade, Accessory, Security, Wi-Fi,
                                          VPN, Energywise, MobileRemoteAccess Note To implement multilevel and multi-section support of the parameters, check the Log Profile check box. Remote Log - values:
                                          				Disable (default), Enable IPv6 Log Server or Log Server - IP address (IPv4 or IPv6 address) Note When the Log
                                                      				  Server cannot be reached, the phone stops sending debug messages. The format
                                                					 for the IPv4 Log Server address is address:<port>@@base=<0-7>;pfs=<0-1> The
                                                					 format for the IPv6 Log Server address is [address]:<port>@@base=<0-7>;pfs=<0-1> Where: the
                                                      						  IPv4 address is separated with dot (.) the
                                                      						  IPv6 address is separated with colon (:) | Note | To implement multilevel and multi-section support of the parameters, check the Log Profile check box. | Note | When the Log
                                                      				  Server cannot be reached, the phone stops sending debug messages. |
| Note | To implement multilevel and multi-section support of the parameters, check the Log Profile check box. |
| Note | When the Log
                                                      				  Server cannot be reached, the phone stops sending debug messages. |

| Note | To implement multilevel and multi-section support of the parameters, check the Log Profile check box. |
|---|---|

| Note | When the Log
                                                      				  Server cannot be reached, the phone stops sending debug messages. |
|---|---|