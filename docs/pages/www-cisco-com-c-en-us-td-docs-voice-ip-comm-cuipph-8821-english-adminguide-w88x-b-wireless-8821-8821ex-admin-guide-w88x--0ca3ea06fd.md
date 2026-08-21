---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-english-adminguide-w88x-b-wireless-8821-8821ex-admin-guide-w88x--0ca3ea06fd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/english/adminguide/w88x_b_wireless-8821-8821ex-admin-guide/w88x_b_wireless-8821-8821ex-admin-guide_chapter_01001.html
retrieved_at: 2026-08-21T01:56:35.266476+00:00
---

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

# Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

Updated: June 28, 2016

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## General Troubleshooting Information

The following table provides general troubleshooting
                              		information for the 
                              		wireless IP phone.

Summary

Explanation

Phone is resetting

The phone resets when it loses contact with the
                                          				CiscoUnifiedCommunications Manager software. This lost connection can be due
                                          				to any network connectivity disruption, including access point problems, switch
                                          				outages, and switch reboots.

See Phone Reset Problems .

Time on the phone is incorrect

Sometimes the time or date on the phone is incorrect.
                                          				The 
                                          				phone gets its time and date when it
                                          				registers with Cisco Unified Communications Manager. Power cycle the phone to
                                          				reset the time or date.

The time shows in either 12 hour or 24 hour format.

Phone firmware downgrades

After applying a Cisco Unified Communications Manager
                                          				upgrade or patch, that is older than the current 
                                          				phone firmware, the phones could
                                          				automatically downgrade to the load contained in the patch. Check the 
                                          				phone default image in the TFTP
                                          				folder to fix this problem.

Battery life is shorter than specified

An unstable RF environment can cause the phone to remain
                                          				in active mode because it is constantly seeking an AP. This reduces the battery
                                          				life considerably. When leaving an area of coverage, shut down the phone.

Higher phone transmit power can affect battery life.

To maximize idle time on the phone and conserve battery
                                          				life, you need to optimize the registration time so the phone can go into power
                                          				save mode more often.

Phone call cannot be established

The phone does not have a DHCP IP address, is unable to
                                          				register to Cisco Unified Communications Manager, and shows a Configuring IP or Registering message.

Verify the following:

The Cisco Unified Communications Manager service is running on
                                                					 the Cisco Unified Communications Manager server.

Both phones are registered to the same Cisco Unified
                                                					 Communications Manager.

Audio server debug and capture logs are enabled for both
                                                					 phones. If needed, enable Java debug.

Call established with the iLBC protocol does not show
                                          				that the iLBC codec is being used

Call statistics display does not show iLBC as the
                                          				receiver/sender codec.

Check the following using the Cisco Unified Communications
                                                					 Manager administration pages:

Both phones are in the iLBC device pool.

The iLBC device pool is configured with the iLBC region.

The iLBC region is configured with the iLBC codec.

Capture a sniffer trace between the phone and Cisco Unified
                                                					 Communications Manager and verify that SCCP messages,OpenReceiveChannel, and
                                                					 StationMediaTransmit messages have media payload type value equal to 86. If so,
                                                					 the problem is with the phone; otherwise the problem is with the Cisco Unified
                                                					 Communications Manager configuration.

Enable audio server debug and capture logs from both phones.
                                                					 If needed, enable Java debug.

For additional troubleshooting information, see the Cisco Unified Communications Manager Troubleshooting Guide .

## Phone Does Not Go Through the Normal Startup Process

### Problem

The phone does not start up and information does not display on the phone.

### Cause

When a phone connects to the wireless network, the phone
                              		  should go through its normal startup process and the phone screen should
                              		  display information.

If the phone does not complete the startup process, the cause
                              		  might be due to low RF signal strength, network outages, a dead battery in the
                              		  phone, or the phone might not be functional.

### Solution

To determine whether the phone is functional, follow these
                              		  suggestions to systematically eliminate potential problems.

Verify that the wired network is accessible by placing calls to
                                    				and from other wired   IP Phones.

Verify that the wireless network is accessible:

Power on another previously functional 
                                          					 phone to verify that the access point is active.

Power on the 
                                          					 phone
                                          					 that will not start up and move to a different access point location that is
                                          					 known to be good.

Verify that the phone is receiving power:

If the message Low Battery is displayed on the phone screen, the battery might be
                                          					 dead.

Insert a new or fully charged battery in the 
                                          					 phone
                                          					 that will not start up.

If you are using the battery, try plugging in the external
                                          					 power supply instead.

Reset the phone to the default settings:

Select Applications > Admin settings > Reset settings > All settings .

At the confirmation screen, select Reset .

Restart the phone from the alternate image:

Turn off the phone by pressing the red, power button.

As you press and hold * , press the power button a second time.

Release * when the LED display changes color.

If, after you  attempt these solutions, the phone still does
                              		  not start up, contact a Cisco technical support representative for additional
                              		  assistance.

## Connection Problems

If the phones experience connection problems that are not related to roaming, the problems are often related to the Access
                              Point or to the way the phone connects to the Cisco Unified Communications Manager.

### No Association to Wireless Access Points

After power on, if a phone continues to
                                 		cycle through messages displaying on the phone screen, the phone is not
                                 		associating with the access point properly. The phone cannot successfully start
                                 		up unless it associates and authenticates with an access point.

The 
                                 		wireless phone must first authenticate and associate with an
                                 		access point before it can obtain an IP address. The phone follows this start
                                 		up process with the access point:

Scans for an access point

Associates with an access point

Authenticates using a preconfigured authentication method (using the configured security mode setting)

Obtains an IP address

#### Access Point Settings Mismatch

##### Problem

A configuration mismatch exists between the phone and the AP.

##### Solution

Check the SSID settings on the access point and on the phone to be sure the SSIDs match.

Check the authentication type settings on the access point and on the phone to be sure authentication and encryption settings
                                          match.

If the No Service - IP Config Failed message displays, DHCP failed because the encryption between the access point and phone do not match.

If using static WEP, check the WEP key on the phone to be sure it matches the WEP key on the access point. Reenter the WEP
                                          key on the phone to be sure it is correct.

If open authentication is set, the phone is able to associate to an access point even if the WEP keys are incorrect or mismatched.

#### Authentication Failed, No AP Found

##### Problem

Authentication returns the No AP found message.

##### Solution

Check whether the correct authentication method and related encryption settings are enabled on the access point.

Check that the correct SSID is entered on the phone.

Check that the correct username and password are configured when using EAP-FAST, EP-TLS, PEAP-GTC, or PEAP-MSCHAPV2 authentication.

If you are using a WPA Pre-shared key or WPA2 Pre-shared Key, check that you have the correct passphrase configured.

You might need to enter the username on the phone in the domain\username format when authenticating with a Windows domain.

#### EAP Authentication Failed Message

##### Problem

Authentication returns the EAP authentication failed message.

##### Solution

If you are using EAP, you might need to enter the EAP username on the phone in the domain\username format when authenticating
                                          with a Windows domain.

Check that the correct EAP username and password are entered on phone.

#### AP Error - Cannot Support All Requested Capabilities

##### Problem

Authentication returned the AP Error - Cannot support all requested capabilities message.

##### Solution

On the access point, check that CKIP/CMIC is not enabled for the voice VLAN SSID. The wireless phone does not support these
                                    features.

### Phone Does Not Register with Cisco Unified Communications Manager

If a phone proceeds past the first stage (authenticating with
                              		access point) and continues to cycle through the messages displaying on the
                              		phone screen, the phone is not starting up properly. The phone cannot
                              		successfully start up until it connects to the LAN and registers with a
                              		CiscoUnifiedCommunications Manager server.

The following sections can assist you in determining the reason that
                              		the phone is unable to start up properly.

#### Phone Cannot Connect to TFTP Server or to Cisco Unified Communications Manager

##### Problem

If the network is down between the phone and either the TFTP server or Cisco Unified Communications Manager, the phone cannot
                                    start up properly.

##### Solution

Ensure that the network is currently running.

#### Phone Cannot Connect to TFTP Server

##### Problem

The TFTP server setting on the phone is incorrect.

##### Cause

The 
                                    		  phone uses the TFTP server setting to identify the
                                    		  primary TFTP server to use. If the TFTP server does not respond to the request,
                                    		  then the Communications Manager1 (CM1) shows as TFTP_AS_CM if the phone has not
                                    		  registered with Cisco Unified Communications Manager before.

If the phone has previously registered with Cisco Unified
                                                			 Communications Manager, the Cisco Unified Communications Manager list
                                                			 information is cached in memory. If TFTP fails, you must power cycle the phone
                                                			 to connect to the TFTP server.

The phone tries to create a TCP connection to the TFTP IP
                                    		  address and then to the gateway. If Cisco Unified Communications Manager
                                    		  service is not running on the TFTP server, or if SRST is not running on the
                                    		  gateway, the 
                                    		  phone may
                                    		  continually cycle while attempting to contact the identified TFTP server.

The 
                                    		  phone does not cache the IP information passed from the
                                    		  DHCP server, so the TFTP request must be sent and responded to every time the
                                    		  phone power cycles.

##### Solution

If you have assigned a static IP address to the phone, you
                                    		  must manually enter the TFTP server address. See Manually Set Up the Phone Network from the Settings Menu .

If you are using DHCP, the phone obtains the address for the
                                    		  TFTP server from the DHCP server. Check the IP address configured in the DHCP
                                    		  server.

You can also enable the phone to use a static TFTP server.
                                    		  Such a setting is particularly useful if the phone was recently moved from one
                                    		  location to another.

#### Phone Cannot Connect to Server

##### Problem

The IP addressing and routing fields may not be correctly
                                    		  configured.

##### Solution

Verify the IP addressing for the 
                                    		  phone. If you are using DHCP, the DHCP server should
                                    		  provide these values. If you have assigned a static IP address to the phone,
                                    		  you must enter these values manually.

When the 
                                                			 wireless IP phone loses
                                                			 the RF signal (goes out of the coverage area), the phone will not release the
                                                			 DHCP server unless it reaches the timeout state.

Check for these problems:

DHCP Server: If you have assigned a static IP address to the phone, you do not need to enter a value for the DHCP Server option.
                                          If you are using a DHCP server, and the wireless IP phone gets a response from the DHCP server, the information is automatically
                                          configured. See Troubleshooting Switch Port Problems , available at this URL: https://www.cisco.com/en/US/products/hw/switches/ps708/products_tech_note09186a008015bfd6.shtml .

IP Address, Subnet Mask, Primary Gateway: If you have assigned a
                                          				static IP address to the phone, you must configure settings for these options.
                                          				See Manually Set Up the Phone Network from the Settings Menu .

If you are using DHCP, check the IP addresses distributed by your DHCP server. Be aware of DHCP conflicts and duplicate IP
                                    addresses. See Understanding and Troubleshooting DHCP in Catalyst Switch or Enterprise Networks , available at this URL: https://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml .

#### Phone Cannot Connect with DNS

##### Problem

The phone has incorrect DNS server information.

##### Solution

If you are using DNS to refer to
                                    		  Cisco Unified Communications Manager, you must ensure that you have specified a
                                    		  DNS server. You should also verify that there is a CNAME entry in the DNS
                                    		  server for the Cisco Unified Communications Manager system.

You must also ensure that DNS is configured to do reverse
                                    		  look-ups. The default setting on Windows 2000 is to perform forward-only
                                    		  look-ups.

For information about determining and changing DNS settings,
                                    		  see Manually Set Up the Phone Network from the Settings Menu .

#### Cisco Unified Communications Manager and TFTP Services Are Not Running

##### Problem

If the Cisco Unified Communications Manager or TFTP services are not running, phones may not be able to start up properly.
                                    In such a situation, it is likely that you are experiencing a systemwide failure, and other phones and devices are unable
                                    to start up properly.

##### Solution

If the Cisco Unified Communications Manager service is not running, all devices on the network that rely on it to make phone
                                    calls are affected. If the TFTP service is not running, many devices cannot start up successfully. For more information, see Start Service .

#### Phone is Not Configured in Cisco Unified Communications Manager

##### Problem

The phone is not registered with the Cisco Unified
                                    		  Communications Manager

##### Solution

A phone can register with a Cisco Unified
                                    		  Communications Manager server only if the phone is added to the server or if
                                    		  autoregistration is enabled.

To verify that the phone is in the Cisco Unified
                                    		  Communications Manager database, choose Device > Phone from Cisco Unified Communications Manager Administration. Click Find to search for the
                                    		  phone based on the MAC Address. For information about determining a MAC
                                    		  address, see Determine the MAC Address of the Phone .

If the phone is already in the Cisco Unified Communications
                                    		  Manager database, the configuration file may be damaged. See Configuration File Corruption for assistance.

### Configuration File Corruption

#### Problem

If you continue to have problems with a particular phone that
                                 		  other suggestions in this chapter do not resolve, the configuration file may be
                                 		  corrupted.

#### Solution

Create a new phone configuration file.

## Phone Reset Problems

If users report that their phones are resetting during calls or while the phones are idle, you should investigate the cause.
                           If the network connection and Cisco Unified Communications Manager connection are stable, a phone should not reset.

Typically, a phone resets if it has problems in connecting to the network or to Cisco Unified Communications Manager.

### Phone Resets Due to Access Point Setup

#### Problem

The AP may not be configured correctly.

#### Solution

Verify that the wireless configuration is correct. For
                                 		  example, check if the particular access point or switch to which the phone is
                                 		  connected is down.

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

### Phone Resets
                           	 Due to Intentional Reset

#### Problem

If you
                                 		  are not the only administrator with access to Cisco Unified Communications
                                 		  Manager, you should verify that no one else has intentionally reset the phones.

#### Solution

You can
                                 		  check if a wireless phone received a command from Cisco Unified Communications
                                 		  Manager to reset by accessing the Settings app on the phone and choosing Admin
                                       				settings > Status > WLAN
                                       				statistics .

If the Restart
                                       				Cause field displays Reset-Reset , the phone receives a Reset/Reset
                                       				from Cisco Unified Communications Manager Administration.

If the Restart
                                       				Cause field displays Reset-Restart , the phone closed because it
                                       				received a Reset/Restart from Cisco Unified Communications Manager
                                       				Administration.

### Phone Resets Due to DNS or Other Connectivity Issues

#### Problem

The phone reset continues and you suspect DNS or other
                                 		  connectivity issues.

#### Solution

If the phone continues to reset, eliminate DNS or other
                                 		  connectivity errors by following the procedure in Determine DNS or Connectivity Issues .

## Audio Problems

When users report that active phone calls have poor voice
                           		quality that includes choppy audio, static or gaps in audio, or no audio, use the information in this section to identify
                           the cause of the problem.

### One-Way Audio or No Speech Path

#### Problem

One or more people on a call do not hear any audio.

#### Solution

Use the following list to identify possible causes for the
                                 		  problem:

Check the access point to see if the transmit power setting
                                       				matches the transmit power setting on the phone. One-way audio is common when
                                       				the access point power setting is greater than that of the phone.

The phone firmware supports dynamic transmit power
                                       				control (DTPC). The phone uses the transmit power that the access point
                                       				advertises upon association.

With DTPC, if Client Transmit Power is set in the access point,
                                                   				  the phone automatically uses the same client power setting. If the access point
                                                   				  is set for the maximum setting (Max), the access point uses the Transmit Power
                                                   				  setting on the phone.

Check that the access point is enabled for ARP caching. When the 
                                       				phone  is in power save mode or scanning, the
                                       				access point can respond to the wireless IP phone only when ARP caching is
                                       				enabled.

Check your gateway and IP routing for voice problems.

Check if a firewall or NAT is in the path of the RTP packets. If
                                       				so, you can use Cisco IOS and PIXNAT to modify the connections so that two-way
                                       				audio is possible.

Check that the Data Rate setting for the phone and the access
                                       				point are the same. These settings should match or the phone should be set for
                                       				Auto.

Check the phone hardware to be sure the speaker is functioning
                                       				properly.

Check that the speaker is functioning properly. Adjust the speaker
                                       				volume setting and call the phone to check the speaker.

### Ring Volume is Too Low

#### Problem

User complains that the ringer on the phone is not loud
                                 		  enough.

#### Solution

Press the Volume button on the side of the
                                 		  phone, and increase the volume.

### Phone Does Not Ring

#### Problem

User complains that phone does not ring.

#### Solution

Check the phone settings:

In the Settings app,

Check where the ringer should ring. Choose Phone
                                                   					 settings > Sounds > Ringer output , and check that the correct location is
                                             				selected.

Check the ringtone. Choose Phone
                                                   					 settings > Sounds > Ringtone . If a ringtone  is not
                                             				set, select a ringtone for the phone.

To see if the speaker is functioning properly, adjust the ring
                                       				volume settings to the highest level. Enable keypad tones or call the phone to
                                       				check the speaker.

## Feature Issues

Your users may report problems with some features. If you get the exact message that the user sees on the phone, you can identify
                              and fix the cause of the problem.

### Users Report Problems with Call Park

#### Problem

Your users report  seeing these messages:

There is no free place to park this call.

Call park is not available.

#### Resolution

Message

Meaning

There is no free place to park this call.

You need to allocate more slots to park calls.

Call park is not available.

You have a configuration problem with Call park on your Cisco Unified Communications Manager.

For more information, see the Cisco Unified Communications Manager documentation.

## Roaming and Voice Quality or Lost Connection Problems

If users report that when they are engaged in an active phone call and
                           		walking from one location to another (roaming), the voice quality deteriorates
                           		or the connection is lost, use the information in this section to identify
                           		the cause of the problem.

### Voice Quality Deteriorates While Roaming

#### Problem

User complains that the voice quality deteriorates while roaming.

#### Solution

Check the RSSI on the destination access point to see if the signal strength is adequate. The next access point should have
                                       an RSSI value of -67 dBm or greater.

Check the site survey to determine if the channel overlap is adequate for the phone and the access point to hand off the call
                                       to the next access point before the signal is lost from the previous access point.

Check to see if noise or interference in the coverage area is too great.

Check that signal to noise ratio (SNR) levels are 25 dB or higher for acceptable voice quality.

### Voice Conversation Delays While Roaming

#### Problem

User complains of delays in the voice conversation while roaming.

#### Solution

Check the Neighbor List to see if there is another acceptable access point as a roaming option. The next access point should
                                       have an signal of -67 dBm to roam successfully.

Check the Cisco Catalyst 45xx switch. If Cisco Catalyst 45xx series switches are being used as the main Layer 3 switches in
                                       the network, ensure that the supervisor blades are a minimum SUP2+ or later version. The wireless phone (or any wireless client)
                                       experiences roaming delays when an earlier version (SUP 1 or SUP2) blade is used.

### Phone Loses Cisco Unified Communications Manager Connection While Roaming

#### Problem

User complains that the call gets dropped while roaming.

#### Solution

Check for the following configuration or connectivity issues
                                 		  between the phone and the access point:

The RF signal strength might be weak. Access the Neighbor list and check the RSSI value for the next access point.

The next access point might not have connectivity to Cisco Unified Communications Manager.

There might be an authentication type mismatch between the phone and the next access point.

The access point might be in a different subnet from the previous access point. The Cisco Unified Wireless IP Phone is capable
                                       of Layer 2 roaming only. Layer 3 roaming requires WLSM that uses GRE. For more information, see WLANs and Roaming .

If using EAP-FAST, EAP-TLS, PEAP-GTC, or PEAP-MSCHAPV2 authentication, the access point might be using filters to block TCP
                                       ports. The RADIUS server uses port 1812 for authentication and 1813 for accounting.

### Phone Does not Roam Back to Preferred Band

#### Problem

The phone does not roam back to the preferred wireless band.

#### Solution

For troubleshooting information, see the Cisco Wireless IP Phone 8821 Series Deployment Guide .

## Troubleshooting Procedures

These procedures can be used to identify and correct problems.

### Check TFTP
                           	 Settings

On the Cisco IP Phone, access the Settings app,  
                                          			 choose Wi-Fi , select a profile, then select Network configuration > IPv4
                                                				  setup > TFTP server 1 .

If you have
                                          			 assigned a static IP address to the phone, you must manually enter a setting
                                          			 for the TFTP Server 1 option.

If you are
                                          			 using DHCP, the phone obtains the address for the TFTP server from the DHCP
                                          			 server. Check that the IP address is configured in Option 150.

You can also
                                          			 enable the phone to use an alternate TFTP server. Such a setting is
                                          			 particularly useful if the phone recently moved from one location to another.

If the local
                                          			 DHCP does not offer the correct TFTP address, enable the phone to use an
                                          			 alternate TFTP server.

This is often
                                             				necessary in VPN scenario.

### Determine DNS or Connectivity Issues

Use the Reset Settings menu to reset phone settings to their
                                          			 default values.

Modify DHCP and IP settings:

Disable DHCP.

Assign static IP values to the phone. Use the same default router setting that other functioning
                                                				  phones use.

Assign a TFTP server. Use the same TFTP server that other functioning phones use.

On the Cisco Unified Communications Manager server, verify that
                                          			 the local host files have the correct Cisco Unified Communications Manager
                                          			 server name mapped to the correct IP address.

From Cisco Unified Communications Manager, choose System > Server and verify
                                          			 that reference to the server is made by the IP address and not by the DNS name.

From Cisco Unified Communications Manager, choose Device > Phone . Click Find to search for this phone. Verify that you have assigned the correct MAC address to this Cisco IP Phone.

Power cycle the phone.

### Check DHCP Settings

On the phone, access the Settings app.

Select Wi-Fi , select the active profile, then select Network configuration > IPv4 setup , and look at
                                          			 the DHCP field:

If DHCP is on, then the phone is assigned the settings from the DHCP server.

If DHCP is off, then you must configure a static IP Address, and set the Subnet Mask, Default Router, and DNS server 1  fields.

If you are using DHCP, check the IP addresses that your
                                          			 DHCP server distributes.

See the Understanding and Troubleshooting DHCP in Catalyst Switch
                                                			 or Enterprise Networks document, available at this URL:

http://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml

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

From Cisco Unified Communications Manager,
                                          			 choose Device > Phone and click Find to locate the phone that is experiencing problems.

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

Add the phone back to the Cisco Unified Communications Manager
                                          			 database.

Power cycle the phone.

### Start Service

A service must be activated before it can be started or stopped.

From Cisco Unified Communications Manager Administration, choose Cisco Unified Serviceability from the
                                          			 Navigation drop-down list and click Go .

Choose Tools > Control
                                                				  Center - Feature Services .

Choose the primary Cisco Unified Communications Manager server
                                          			 from the Server drop-down list.

The window displays the service names for the server that you
                                             				chose, the status of the services, and a service control panel to start or stop
                                             				a service.

If a service has stopped, click the corresponding radio button and then click Start .

The Service Status symbol changes from a square to an arrow.

### Capture Phone Logs

If your users have problems and you need to contact Cisco TAC for assistance, you need to capture the phone log files. The
                                 log files will help TAC resolve the problem.

Capture these logs as close to the problem event as possible. If the user can recreate the problem easily, get the user to
                                 record what they did to get the problem to occur.

#### Before you begin

Make sure that the web access is enabled for the phone.

If possible, ask your user for the time span that the problem occurred.

Obtain the IP
                                          			 address of the Cisco IP Phone by using one of these methods:

Search for
                                                				  the phone in Cisco Unified Communications Manager Administration by choosing Device > Phone . Phones that register with Cisco
                                                				  Unified Communications Manager display the IP address on the Find and List
                                                   				  Phones window and at the top of the Phone Configuration window.

On the
                                                				  Cisco IP Phone, access the Settings app,
                                                					 select Phone information > Device information > Network > IPv4 , and then scroll to the IP
                                                					 Address field.

Open a web browser and enter the following URL, where IP_address is the IP address of the Cisco IP Phone:

http:// <IP_address>

Click Console logs .

Open the listed log files and save the files that cover the time period that the user experienced the problem.

If the problem is not limited to a specific time, save all the log files.

### Make a Screen Capture

If your users have problems and you need to contact Cisco TAC for assistance, a capture of the phone screen may help TAC resolve
                                 the problem.

#### Before you begin

Make sure that the web access is enabled for the phone.

Obtain the IP
                                          			 address of the Cisco IP Phone by using one of these methods:

Search for
                                                				  the phone in Cisco Unified Communications Manager Administration by choosing Device > Phone . Phones that register with Cisco
                                                				  Unified Communications Manager display the IP address on the Find and List
                                                   				  Phones window and at the top of the Phone Configuration window.

On the
                                                				  Cisco IP Phone, access the Settings app,
                                                					 select Phone information > Device information > Network > IPv4 , and then scroll to the IP
                                                					 Address field.

Open a web
                                          			 browser and enter the following URL, where IP_address is the IP
                                          			 address of the Cisco IP Phone:

http:// IP_address /CGI/Screenshot

At the prompt, enter the username and password.

The phone creates an image of the phone screen.

Save the file to your computer.

### Access Phone Diagnostics

The Diagnostics menu on the phone enables you to troubleshoot some common phone problems.

Access the Settings app.

Select Admin settings > Diagnostics .

#### Perform Audio Diagnostics

The Audio entry in the Diagnostics menu on the phone enables you to troubleshoot problems with the audio on the phone.

Access the Settings app.

Select Admin settings > Diagnostics > Audio .

Listen to the tone on the handset speaker.

Press the Speaker button to turn on handsfree, and listen to the tone.

Plug in a wired headset and listen to the tone.

#### Perform WLAN Diagnostics

The WLAN entry in the Diagnostics menu on the phone enables you to troubleshoot WLAN problems from the phone.

Access the Settings app.

Select Admin settings > Diagnostics > WLAN .

At the prompt, select Continue .

Select the profile that is currently in use.

The screen displays the WLAN information.

### Find the List of Neighbor Access Points

The Neighbor list menu on the phone gives you the list of access points that the phone can connect to.

Access the Settings app.

Select Admin settings > Neighbor list .

### Create a Problem Report from the Phone

If your users have a problem with their phones, you can ask them to generate a problem report using the problem report tool
                                 (PRT). You can access the report from the phone administration web page.

On the phone that has the problem, access the Settings app.

Select Phone information > Report problem .

Press Submit .

Access the phone administration web page to download the report.

### Generate a Problem Report from the Admin Web Page

You can remotely generate a problem report for a phone with the admin web page.

#### Before you begin

Connect to the admin web page. For more information, see Access the Phone Administration Web Page .

Click Device logs > Console logs .

Click Report problem .

| Summary | Explanation |
|---|---|
| Phone is resetting | The phone resets when it loses contact with the
                                          				CiscoUnifiedCommunications Manager software. This lost connection can be due
                                          				to any network connectivity disruption, including access point problems, switch
                                          				outages, and switch reboots. See Phone Reset Problems . |
| Time on the phone is incorrect | Sometimes the time or date on the phone is incorrect.
                                          				The 
                                          				phone gets its time and date when it
                                          				registers with Cisco Unified Communications Manager. Power cycle the phone to
                                          				reset the time or date. The time shows in either 12 hour or 24 hour format. |
| Phone firmware downgrades | After applying a Cisco Unified Communications Manager
                                          				upgrade or patch, that is older than the current 
                                          				phone firmware, the phones could
                                          				automatically downgrade to the load contained in the patch. Check the 
                                          				phone default image in the TFTP
                                          				folder to fix this problem. |
| Battery life is shorter than specified | An unstable RF environment can cause the phone to remain
                                          				in active mode because it is constantly seeking an AP. This reduces the battery
                                          				life considerably. When leaving an area of coverage, shut down the phone. Higher phone transmit power can affect battery life. To maximize idle time on the phone and conserve battery
                                          				life, you need to optimize the registration time so the phone can go into power
                                          				save mode more often. |
| Phone call cannot be established | The phone does not have a DHCP IP address, is unable to
                                          				register to Cisco Unified Communications Manager, and shows a Configuring IP or Registering message. Verify the following: The Cisco Unified Communications Manager service is running on
                                                					 the Cisco Unified Communications Manager server. Both phones are registered to the same Cisco Unified
                                                					 Communications Manager. Audio server debug and capture logs are enabled for both
                                                					 phones. If needed, enable Java debug. |
| Call established with the iLBC protocol does not show
                                          				that the iLBC codec is being used | Call statistics display does not show iLBC as the
                                          				receiver/sender codec. Check the following using the Cisco Unified Communications
                                                					 Manager administration pages: Both phones are in the iLBC device pool. The iLBC device pool is configured with the iLBC region. The iLBC region is configured with the iLBC codec. Capture a sniffer trace between the phone and Cisco Unified
                                                					 Communications Manager and verify that SCCP messages,OpenReceiveChannel, and
                                                					 StationMediaTransmit messages have media payload type value equal to 86. If so,
                                                					 the problem is with the phone; otherwise the problem is with the Cisco Unified
                                                					 Communications Manager configuration. Enable audio server debug and capture logs from both phones.
                                                					 If needed, enable Java debug. |

| Note | If the No Service - IP Config Failed message displays, DHCP failed because the encryption between the access point and phone do not match. |
|---|---|

| Note | If open authentication is set, the phone is able to associate to an access point even if the WEP keys are incorrect or mismatched. |
|---|---|

| Note | If the phone has previously registered with Cisco Unified
                                                			 Communications Manager, the Cisco Unified Communications Manager list
                                                			 information is cached in memory. If TFTP fails, you must power cycle the phone
                                                			 to connect to the TFTP server. |
|---|---|

| Note | When the 
                                                			 wireless IP phone loses
                                                			 the RF signal (goes out of the coverage area), the phone will not release the
                                                			 DHCP server unless it reaches the timeout state. |
|---|---|

| Note | With DTPC, if Client Transmit Power is set in the access point,
                                                   				  the phone automatically uses the same client power setting. If the access point
                                                   				  is set for the maximum setting (Max), the access point uses the Transmit Power
                                                   				  setting on the phone. |
|---|---|

| Message | Meaning |
|---|---|
| There is no free place to park this call. | You need to allocate more slots to park calls. |
| Call park is not available. | You have a configuration problem with Call park on your Cisco Unified Communications Manager. |

| Step 1 | On the Cisco IP Phone, access the Settings app,  
                                          			 choose Wi-Fi , select a profile, then select Network configuration > IPv4
                                                				  setup > TFTP server 1 . |
|---|---|
| Step 2 | If you have
                                          			 assigned a static IP address to the phone, you must manually enter a setting
                                          			 for the TFTP Server 1 option. |
| Step 3 | If you are
                                          			 using DHCP, the phone obtains the address for the TFTP server from the DHCP
                                          			 server. Check that the IP address is configured in Option 150. |
| Step 4 | You can also
                                          			 enable the phone to use an alternate TFTP server. Such a setting is
                                          			 particularly useful if the phone recently moved from one location to another. |
| Step 5 | If the local
                                          			 DHCP does not offer the correct TFTP address, enable the phone to use an
                                          			 alternate TFTP server. This is often
                                             				necessary in VPN scenario. |

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

| Step 1 | On the phone, access the Settings app. |
|---|---|
| Step 2 | Select Wi-Fi , select the active profile, then select Network configuration > IPv4 setup , and look at
                                          			 the DHCP field: If DHCP is on, then the phone is assigned the settings from the DHCP server. If DHCP is off, then you must configure a static IP Address, and set the Subnet Mask, Default Router, and DNS server 1  fields. |
| Step 3 | If you are using DHCP, check the IP addresses that your
                                          			 DHCP server distributes. See the Understanding and Troubleshooting DHCP in Catalyst Switch
                                                			 or Enterprise Networks document, available at this URL: http://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml |

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

| Step 1 | Obtain the IP
                                          			 address of the Cisco IP Phone by using one of these methods: Search for
                                                				  the phone in Cisco Unified Communications Manager Administration by choosing Device > Phone . Phones that register with Cisco
                                                				  Unified Communications Manager display the IP address on the Find and List
                                                   				  Phones window and at the top of the Phone Configuration window. On the
                                                				  Cisco IP Phone, access the Settings app,
                                                					 select Phone information > Device information > Network > IPv4 , and then scroll to the IP
                                                					 Address field. |
|---|---|
| Step 2 | Open a web browser and enter the following URL, where IP_address is the IP address of the Cisco IP Phone: http:// <IP_address> |
| Step 3 | Click Console logs . |
| Step 4 | Open the listed log files and save the files that cover the time period that the user experienced the problem. If the problem is not limited to a specific time, save all the log files. |

| Step 1 | Obtain the IP
                                          			 address of the Cisco IP Phone by using one of these methods: Search for
                                                				  the phone in Cisco Unified Communications Manager Administration by choosing Device > Phone . Phones that register with Cisco
                                                				  Unified Communications Manager display the IP address on the Find and List
                                                   				  Phones window and at the top of the Phone Configuration window. On the
                                                				  Cisco IP Phone, access the Settings app,
                                                					 select Phone information > Device information > Network > IPv4 , and then scroll to the IP
                                                					 Address field. |
|---|---|
| Step 2 | Open a web
                                          			 browser and enter the following URL, where IP_address is the IP
                                          			 address of the Cisco IP Phone: http:// IP_address /CGI/Screenshot |
| Step 3 | At the prompt, enter the username and password. The phone creates an image of the phone screen. |
| Step 4 | Save the file to your computer. |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Diagnostics . |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Diagnostics > Audio . |
| Step 3 | Listen to the tone on the handset speaker. |
| Step 4 | Press the Speaker button to turn on handsfree, and listen to the tone. |
| Step 5 | Plug in a wired headset and listen to the tone. |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Diagnostics > WLAN . |
| Step 3 | At the prompt, select Continue . |
| Step 4 | Select the profile that is currently in use. The screen displays the WLAN information. |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Neighbor list . |

| Step 1 | On the phone that has the problem, access the Settings app. |
|---|---|
| Step 2 | Select Phone information > Report problem . |
| Step 3 | Press Submit . |
| Step 4 | Access the phone administration web page to download the report. |

| Step 1 | Click Device logs > Console logs . |
|---|---|
| Step 2 | Click Report problem . |