---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-7db043b7ff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_0110.html
retrieved_at: 2026-08-22T01:04:27.785269+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: Troubleshoot and Maintenance

## Chapter: Troubleshoot and Maintenance

# Troubleshoot and Maintenance

## Configure Syslog Reports

Log Server / IPv6 Log Server: Syslog server in IPv4 and IPv6 format

Remote Log: Enabled or Disabled. Log messages are not sent to server if set to Disabled.

Log Profiles: Debug flag settings of log modules.

Log Module: To configure debug flags; these parameters are overwritten by the Unified Communications Manager Log Profile unless
                                       Preset is selected.

Log Setting: To configure log server, port and size. Server settings are overwritten after provisioning.

Log Viewer: To view, clear or download debug messages being logged.

Because debugging captures detailed information, the communication traffic can slow down the phone, making it less responsive.
                              After you capture the logs, turn off debugging.

0 - Emergency

1 - Alert

2 - Critical

3 - Error

4 - Warn

5 - Notification

6 - Information

7 - Debug

Only high severity messages are logged unless its debug flag is turned on.

If you are experiencing phone problems that you cannot resolve, Cisco TAC can assist you. You will need to turn on debugging
                              for the phone, reproduce the problem, turn debugging off, and send the logs to TAC for analysis.

The following table summarizes the Log Profile and Log Module Settings available to you.

Parameter

Configured from Cisco Unified Communications Manager Log Profile

Configured from Phone Adapter Configuration Utility Log Module

Description

Default

X

Not Available

Resets the debug level to default (All debug off).

Preset

X

Not Available

Use log module settings on Phone Adapter Configuration Utility for debug flags.

Telephony

X

X

Turn on debug flag for provisioning (including auto upgrade) and call features.

SIP

X

X

Turn on debug flag for SIP messages.

UI

X

X

Turn on debug flag for key events, such as DTMF, PRT, and reset button.

Network

X

X

Turn on debug flag for network events such as DHCP, VLAN, or link status change.

Media

X

X

Turn on debug flag for RTP, Fax, Tone, and SLIC -related issues.

System

X

X

Turn on debug flag for system events, such as reboot, or factory reset.

Web

X

X

Turn on debug flag for web operation and event logs.

NTP

X

X

Turn on debug flag for NTP related logs.

CDPLLDP

X

X

Turn on debug flag for CDP and LLDP logs.

Security

X

X

Turn on debug flag for security-related logs.

### Practice

This section provides practice exercises for getting your voice syslog information.

#### Turn On Debug flag for Media or SIP

Step 1

Sign into Cisco Unified Communications Manager Administration as an administrator.

Step 2

Select Device > Phone

Step 3

Locate the phone associated with the user.

Step 4

Navigate to the Product Specific Configuration Layout pane and set the fields.

Step 5

Navigate to the Product Specific Configuration Layout pane.

Step 6

In the Log Server field, enter an IP address and port of a remote system where log messages are to be sent.

Step 7

In the Remote Log field, select Enabled .

Step 8

In the Log Profile field, select Media .

Select SIP if you are configuring the SIP module to debug.

Step 9

Click Save .

Step 10

Click Apply Config .

## Resolve Startup Problems

After installing an ATA 191 into your network and adding it to Cisco Unified Communications Manager, the phone starts up.
                           If the phone does not start up properly, see the following sections for troubleshooting information:

The ATA 191 Does Not Go Through Its Normal Startup Process

The ATA 191 Does Not Register with Cisco Unified Communications Manager

ATA 191 Unable to Obtain IP Address

### The ATA 191 Does Not Register with Cisco Unified Communications Manager

If the ATA proceeds past the first stage of the startup process, with LED indicators flashing, but continues to cycle through
                              the messages, the ATA is not starting up properly. The ATA cannot successfully start up unless it is connected to the Ethernet
                              network and it has registered with a Cisco Unified Communications Manager server.

These sections can assist you in determining the reason the phone is unable to start up properly:

#### Check Network Connectivity

If the network is down between the ATA and the TFTP server or Cisco Unified Communications Manager, the ATA cannot start up
                                    properly.

Ensure that the network is currently running.

#### Verify TFTP Server Settings

You can determine the IP address of the TFTP server used by the ATA 191 by entering http:// x.x.x.x where x.x.x.x is the IP address of the ATA 191.

Step 1

If you have assigned a static IP address to the phone, manually enter a setting for the TFTP Server 1 option.

Step 2

If you are using DHCP, the phone obtains the address for the TFTP server from the DHCP server. Check the IP address that is
                                             configured in Option 150 or Option 66.

Step 3

You can also enable the phone to use an alternate TFTP server. Such a setting is very useful if the phone was recently moved
                                             from one location to another.

#### Verify DNS Settings

Step 1

If you are using DNS to refer to the TFTP server or to Cisco Unified Communications Manager, ensure that you have specified
                                             a DNS server. Verify this setting by entering http://x.x.x.x where x.x.x.x is the IP address of the ATA 191.

Step 2

Verify that there is an A entry in the DNS server for the TFTP server and for the Cisco Unified Communications Manager system.

Step 3

Ensure that DNS is configured to do reverse look-ups.

#### Verify Cisco Unified Communications Manager Settings

Enter http://x.x.x.x where x.x.x.x is the IP address of the ATA 191 to find the active Cisco Unified Communications Manager
                                             settings.

#### Cisco Unified Communications Manager and TFTP Services Are Not Running

If the Cisco Unified Communications Manager or TFTP services are not running, phones may not be able to start up properly.
                                    In such a situation, it is likely that you are experiencing a system-wide failure, and that other phones and devices are unable
                                    to start up properly.

If the Cisco Unified Communications Manager service is not running, all devices on the network that rely on it to make phone
                                    calls are affected. If the TFTP service is not running, many devices cannot start up successfully.

##### Before you begin

A service must be activated before it can be started or stopped. To activate a service, choose Tools > Service Activation .

Step 1

From Cisco Unified Communications Manager Administration, choose Cisco Unified Serviceability from the Navigation drop-down list.

Step 2

Choose Tools > Control Center - Network Services .

Step 3

Choose the primary Cisco Unified Communications Manager server from the Server drop-down list.

The window displays the service names for the server that you chose, the status of the services, and a service control panel
                                                to stop or start a service.

Step 4

If a service has stopped, click its radio button and then click the Start button.

The Service Status symbol changes from a square to an arrow.

#### Create a New Configuration File

If you continue to have problems with a particular phone that other suggestions in this chapter do not resolve, the configuration
                                    file may be corrupted.

##### Before you begin

When you remove a phone from the Cisco Unified Communications Manager database, its configuration file is deleted from the
                                    Cisco Unified Communications Manager TFTP server. The phone’s directory number or numbers remain in the Cisco Unified Communications
                                    Manager database. They are called “unassigned DNs” and can be used for other devices.

If unassigned DNs are not used by other devices, delete them from the Cisco Unified Communications Manager database. You can
                                    use the Route Plan Report to view and delete unassigned reference numbers. See the Administration Guide for Cisco Unified Communications Manager for more information.

Changing the buttons on a phone button template, or assigning a different phone button template to a phone, may result in
                                    directory numbers that are no longer accessible from the phone. The directory numbers are still assigned to the phone in the
                                    Cisco Unified Communications Manager database, but there is no button on the phone with which calls can be answered. These
                                    directory numbers should be removed from the phone and deleted if necessary.

Step 1

From Cisco Unified Communications Manager, choose Device > Phone > Find to locate the phone experiencing problems.

Step 2

Choose Delete to remove the phone from the Cisco Unified Communications Manager database.

Step 3

Add the phone back to the Cisco Unified Communications Manager database.

Step 4

Power cycle the phone.

#### Search for the ATA in Cisco Unified Communications Manager

An ATA can register with a Cisco Unified Communications Manager server only if it has been added to the server or if autoregistration
                                    is enabled.

##### Before you begin

Ensure that the ATA has been added to the Cisco Unified Communications Manager database.

Step 1

To search for a device, sign-in to the Cisco Unified Communications Manager Administration.

Step 2

Device

Step 3

Choose Phone > Find

##### What to do next

If the phone is already in the Cisco Unified Communications Manager database, its configuration file may be damaged.

### ATA 191 Unable to Obtain IP Address

If a phone is unable to obtain an IP address during startup, the phone may not be on the same network or VLAN as the DHCP
                                 server. Or, the switch port to which the phone is connected may be disabled.

Step 1

Ensure that the network or VLAN to which the phone is connected has access to the DHCP server.

Step 2

Ensure that the switch port is enabled.

## ATA 191 Resets Unexpectedly

If users report that their phones are resetting during calls or while idle on their desk, investigate the cause. If the network
                           connection and Cisco Unified Communications Manager connection are stable, an ATA 191 should not reset on its own.

Typically, a phone resets if it has problems connecting to the Ethernet network or to Cisco Unified Communications Manager.
                           These sections can help you identify the cause of a phone resetting in your network:

### Verify the Physical Connection

Verify that the ATA's Ethernet connection is up.

For example, check whether the particular port or switch to which the phone is connected is down and that the switch is not
                                             rebooting.

Make sure that there are no cable breaks.

### Identify Intermittent Network Outages

Intermittent network outages affect data and voice traffic differently. Your network might have been experiencing intermittent
                                 outages without detection. If so, data traffic can resend lost packets and verify that packets are received and transmitted.
                                 However, voice traffic cannot recapture lost packets. Rather than retransmitting a lost network connection, the phone resets
                                 and attempts to reconnect its network connection.

If you are experiencing problems with the voice network, investigate whether an existing problem is simply being exposed.

### Verify DHCP Settings

Follow this process to help determine if the phone has been properly configured to use DHCP:

Step 1

Verify that you have properly configured the phone to use DHCP.

Step 2

Verify that the DHCP server has been set up properly.

Step 3

Verify the DHCP lease duration. Cisco recommends that you set it to 8 days.

The ATA sends the DHCP request message to update the IP Address at half of the lease time. If no response is received from
                                             the server, the ATA starts the DHCP Discover process to get the new IP address.

### Check Static IP Address Settings

If the phone has been assigned a static IP address, verify that you have entered the correct settings.

### Verify Voice VLAN Configuration

If the ATA appears to reset during heavy network usage, it is likely that you do not have a voice VLAN configured. An example
                                 of heavy network usage can be extensive web surfing on a computer connected to the same switch as the phone.

Isolate the phones on a separate auxiliary VLAN.

This increases the quality of the voice traffic.

### Eliminate DNS or Other Connectivity Errors

If the phone continues to reset, follow these steps to eliminate DNS or other connectivity errors:

Step 1

Use the IVR to reset phone settings to their default values.

Step 2

Modify the DHCP and IP settings:

Disable DHCP.

Assign static IP values to the phone. Use the same default router setting used for other functioning ATA units.

Assign the TFTP server. Use the same TFTP server used for other functioning ATA units.

Step 3

On the Cisco Unified Communications Manager server, verify that the local host files have the correct Cisco Unified Communications
                                          Manager server name mapped to the correct IP address.

Step 4

From Cisco Unified Communications Manager, choose System > Server and verify that the server is referred to by its IP address and not by its DNS name.

Step 5

From Cisco Unified Communications Manager, choose Device > Phone and verify that you have assigned the correct MAC address to this ATA.

Step 6

Power cycle the phone.

## Troubleshoot ATA 191 Security

The following table provides troubleshooting information for the security features on the ATA 191. For information relating
                              to solutions for any of these issues, and for more troubleshooting information about security, see the Security Guide for Cisco Unified Communications Manager .

Problem

Possible Cause

CTL File Problems

Device authentication error.

CTL file does not have a Cisco Unified Communications Manager certificate or has an incorrect certificate.

ATA cannot authenticate the CTL file.

The security token that signed the updated CTL file does not exist in the CTL file on the phone.

ATA cannot authenticate any of the configuration files other than CTL file.

The configuration file may not be signed by the corresponding certificate in the phone’s Trust List.

ATA does not register with Cisco Unified Communications Manager.

The CTL file does not contain the correct information for the Cisco Unified Communications Manager server.

ATA does not request signed configuration files.

The CTL file does not contain any TFTP entries with certificates.

ATA cannot update the CTL file.

When the CTL file is updated on Cisco Unified Communications Manager, a factory reset of the ATA is required to update the
                                          CTL file.

## General Troubleshooting Tips

The following table provides general troubleshooting information for the ATA 191.

Summary

Explanation

Poor quality when calling mobile phones using the G.729 protocol

In Cisco Unified Communications Manager, you can configure the network to use the G.729 protocol (the default is G.711). When
                                       using G.729, calls between a phone and a mobile phone have poor voice quality. Use G.729 only when absolutely necessary.

Prolonged broadcast storms cause phones to reset, or be unable to make or answer a call.

A prolonged Layer 2 broadcast storm (lasting several minutes) on the voice VLAN may cause phones to reset, lose an active
                                       call, or be unable to initiate or answer a call. Phones may not come up until a broadcast storm ends.

Dual-Tone Multi-Frequency (DTMF) delay

When you are on a call that requires keypad input, if you press the keys too quickly, some of them may not be recognized.

Codec mismatch between the phone and another device

The RxType and the TxType statistics show the codec that is being used for a conversation between this ATA and the other device.
                                       These values should match. If they do not, verify that the other device can handle the codec conversation or that a transcoder
                                       is in place to handle the service.

Sound sample mismatch between the phone and another device

The RxSize and the TxSize statistics show the voice packet sizes that are being used in a conversation between this ATA and
                                       the other device. The values of these statistics should match.

Gaps in voice calls

Check the AvgJtr and the MaxJtr statistics. A large variance between these statistics may indicate a problem with jitter on
                                       the network or periodic high rates of network activity.

One-way audio

When at least one person in a call does not receive audio, IP connectivity between phones is not established. Check the configurations
                                       in routers and switches to ensure that IP connectivity is properly configures.

Phone call cannot be established.

The phone does not have a DHCP IP address and is unable to register with Cisco Unified Communications Manager.

Verify the following:

The Ethernet cable is attached.

The Cisco Unified Communications Manager service is running on the Cisco Unified Communications Manager server.

Both phones are registered to the same Cisco Unified Communications Manager.

## Problem Report Tool

To issue a problem report, press the PRT button on the ATA.

The Problem Report Tool logs are required by Cisco TAC when troubleshooting problems. The logs are cleared if you restart
                              the phone. Collect the logs before you restart the phones.

You must add a server address to the Customer Support Upload URL field on Cisco Unified Communications Manager.

### Configure a Customer Support Upload URL

You must use a server with an upload script to receive PRT files. The PRT uses an HTTP POST mechanism, with the following
                                 parameters included in the upload (utilizing multipart MIME encoding):

devicename (example: "SEP001122334455" )

serialno (example: "FCH12345ABC" )

username (the username configured in Cisco Unified Communications Manager, the device owner)

prt_file (example: "probrep-20141021-162840.tar.gz" )

A sample script is
                                 		  shown below. This script is provided for reference only. Cisco does not provide
                                 		  support for the upload script installed on a customer's server.

```
<?php

// NOTE: you may need to edit your php.ini file to allow larger
// size file uploads to work.
// Modify the setting for upload_max_filesize
// I used:  upload_max_filesize = 20M

// Retrieve the name of the uploaded file 
$filename = basename($_FILES['prt_file']['name']);

// Get rid of quotes around the device name, serial number and username if they exist
$devicename = $_POST['devicename'];
$devicename = trim($devicename, "'\"");

$serialno = $_POST['serialno'];
$serialno = trim($serialno, "'\"");

$username = $_POST['username'];
$username = trim($username, "'\"");

// where to put the file
$fullfilename = "/var/prtuploads/".$filename;

// If the file upload is unsuccessful, return a 500 error and
// inform the user to try again

if(!move_uploaded_file($_FILES['prt_file']['tmp_name'], $fullfilename)) {
        header("HTTP/1.0 500 Internal Server Error");
        die("Error: You must select a file to upload.");
}

?>
```

Step 1

Set up a server that can run your PRT upload script.

Step 2

Write a script that can handle the parameters listed above, or edit the provided sample script to suit your needs.

Step 3

Upload your script to your server.

Step 4

In Cisco Unified Communications Manager, go to the Product Specific
                                          			 Configuration Layout area of the individual device configuration window, Common
                                          			 Phone Profile window, or Enterprise Phone Configuration window.

Step 5

Check Customer support upload URL and
                                          			 enter your upload server URL.

#### Example:

Step 6

Save your changes.

### Generate a Problem Report

You can generate a problem report using one of the following methods:

The problem report is generated and sent to the system administrator. The LED turns green if the report is sent successfully,
                                                or turns red if the report failed. Press the PRT button again to retry.

- On the web interface for the device, go to Administration > PRT Viewer .  Click Generate PRT to start the PRT process and generate a problem report.

## Clean the ATA 191

To clean your ATA, use a soft, dry cloth to wipe the surface. Do not apply liquids or powders directly on the device. As with
                           all non-weather-proof electronics, liquids and powders can damage the components and cause failures.

| Parameter | Configured from Cisco Unified Communications Manager Log Profile | Configured from Phone Adapter Configuration Utility Log Module | Description |
|---|---|---|---|
| Default | X | Not Available | Resets the debug level to default (All debug off). |
| Preset | X | Not Available | Use log module settings on Phone Adapter Configuration Utility for debug flags. |
| Telephony | X | X | Turn on debug flag for provisioning (including auto upgrade) and call features. |
| SIP | X | X | Turn on debug flag for SIP messages. |
| UI | X | X | Turn on debug flag for key events, such as DTMF, PRT, and reset button. |
| Network | X | X | Turn on debug flag for network events such as DHCP, VLAN, or link status change. |
| Media | X | X | Turn on debug flag for RTP, Fax, Tone, and SLIC -related issues. |
| System | X | X | Turn on debug flag for system events, such as reboot, or factory reset. |
| Web | X | X | Turn on debug flag for web operation and event logs. |
| NTP | X | X | Turn on debug flag for NTP related logs. |
| CDPLLDP | X | X | Turn on debug flag for CDP and LLDP logs. |
| Security | X | X | Turn on debug flag for security-related logs. |

| Step 1 | Sign into Cisco Unified Communications Manager Administration as an administrator. |
|---|---|
| Step 2 | Select Device > Phone |
| Step 3 | Locate the phone associated with the user. |
| Step 4 | Navigate to the Product Specific Configuration Layout pane and set the fields. |
| Step 5 | Navigate to the Product Specific Configuration Layout pane. |
| Step 6 | In the Log Server field, enter an IP address and port of a remote system where log messages are to be sent. |
| Step 7 | In the Remote Log field, select Enabled . |
| Step 8 | In the Log Profile field, select Media . Select SIP if you are configuring the SIP module to debug. |
| Step 9 | Click Save . |
| Step 10 | Click Apply Config . |

| Ensure that the network is currently running. |
|---|

| Step 1 | If you have assigned a static IP address to the phone, manually enter a setting for the TFTP Server 1 option. |
|---|---|
| Step 2 | If you are using DHCP, the phone obtains the address for the TFTP server from the DHCP server. Check the IP address that is
                                             configured in Option 150 or Option 66. |
| Step 3 | You can also enable the phone to use an alternate TFTP server. Such a setting is very useful if the phone was recently moved
                                             from one location to another. |

| Step 1 | If you are using DNS to refer to the TFTP server or to Cisco Unified Communications Manager, ensure that you have specified
                                             a DNS server. Verify this setting by entering http://x.x.x.x where x.x.x.x is the IP address of the ATA 191. |
|---|---|
| Step 2 | Verify that there is an A entry in the DNS server for the TFTP server and for the Cisco Unified Communications Manager system. |
| Step 3 | Ensure that DNS is configured to do reverse look-ups. |

| Enter http://x.x.x.x where x.x.x.x is the IP address of the ATA 191 to find the active Cisco Unified Communications Manager
                                             settings. |
|---|

| Step 1 | From Cisco Unified Communications Manager Administration, choose Cisco Unified Serviceability from the Navigation drop-down list. |
|---|---|
| Step 2 | Choose Tools > Control Center - Network Services . |
| Step 3 | Choose the primary Cisco Unified Communications Manager server from the Server drop-down list. The window displays the service names for the server that you chose, the status of the services, and a service control panel
                                                to stop or start a service. |
| Step 4 | If a service has stopped, click its radio button and then click the Start button. The Service Status symbol changes from a square to an arrow. |

| Step 1 | From Cisco Unified Communications Manager, choose Device > Phone > Find to locate the phone experiencing problems. |
|---|---|
| Step 2 | Choose Delete to remove the phone from the Cisco Unified Communications Manager database. |
| Step 3 | Add the phone back to the Cisco Unified Communications Manager database. |
| Step 4 | Power cycle the phone. |

| Step 1 | To search for a device, sign-in to the Cisco Unified Communications Manager Administration. |
|---|---|
| Step 2 | Device |
| Step 3 | Choose Phone > Find |

| Step 1 | Ensure that the network or VLAN to which the phone is connected has access to the DHCP server. |
|---|---|
| Step 2 | Ensure that the switch port is enabled. |

| Verify that the ATA's Ethernet connection is up. For example, check whether the particular port or switch to which the phone is connected is down and that the switch is not
                                             rebooting. Make sure that there are no cable breaks. |
|---|

| If you are experiencing problems with the voice network, investigate whether an existing problem is simply being exposed. |
|---|

| Step 1 | Verify that you have properly configured the phone to use DHCP. |
|---|---|
| Step 2 | Verify that the DHCP server has been set up properly. |
| Step 3 | Verify the DHCP lease duration. Cisco recommends that you set it to 8 days. The ATA sends the DHCP request message to update the IP Address at half of the lease time. If no response is received from
                                             the server, the ATA starts the DHCP Discover process to get the new IP address. |

| If the phone has been assigned a static IP address, verify that you have entered the correct settings. |
|---|

| Isolate the phones on a separate auxiliary VLAN. This increases the quality of the voice traffic. |
|---|

| Step 1 | Use the IVR to reset phone settings to their default values. |
|---|---|
| Step 2 | Modify the DHCP and IP settings: Disable DHCP. Assign static IP values to the phone. Use the same default router setting used for other functioning ATA units. Assign the TFTP server. Use the same TFTP server used for other functioning ATA units. |
| Step 3 | On the Cisco Unified Communications Manager server, verify that the local host files have the correct Cisco Unified Communications
                                          Manager server name mapped to the correct IP address. |
| Step 4 | From Cisco Unified Communications Manager, choose System > Server and verify that the server is referred to by its IP address and not by its DNS name. |
| Step 5 | From Cisco Unified Communications Manager, choose Device > Phone and verify that you have assigned the correct MAC address to this ATA. |
| Step 6 | Power cycle the phone. |

| Problem | Possible Cause |
|---|---|
| CTL File Problems |
| Device authentication error. | CTL file does not have a Cisco Unified Communications Manager certificate or has an incorrect certificate. |
| ATA cannot authenticate the CTL file. | The security token that signed the updated CTL file does not exist in the CTL file on the phone. |
| ATA cannot authenticate any of the configuration files other than CTL file. | The configuration file may not be signed by the corresponding certificate in the phone’s Trust List. |
| ATA does not register with Cisco Unified Communications Manager. | The CTL file does not contain the correct information for the Cisco Unified Communications Manager server. |
| ATA does not request signed configuration files. | The CTL file does not contain any TFTP entries with certificates. |
| ATA cannot update the CTL file. | When the CTL file is updated on Cisco Unified Communications Manager, a factory reset of the ATA is required to update the
                                          CTL file. |

| Summary | Explanation |
|---|---|
| Poor quality when calling mobile phones using the G.729 protocol | In Cisco Unified Communications Manager, you can configure the network to use the G.729 protocol (the default is G.711). When
                                       using G.729, calls between a phone and a mobile phone have poor voice quality. Use G.729 only when absolutely necessary. |
| Prolonged broadcast storms cause phones to reset, or be unable to make or answer a call. | A prolonged Layer 2 broadcast storm (lasting several minutes) on the voice VLAN may cause phones to reset, lose an active
                                       call, or be unable to initiate or answer a call. Phones may not come up until a broadcast storm ends. |
| Dual-Tone Multi-Frequency (DTMF) delay | When you are on a call that requires keypad input, if you press the keys too quickly, some of them may not be recognized. |
| Codec mismatch between the phone and another device | The RxType and the TxType statistics show the codec that is being used for a conversation between this ATA and the other device.
                                       These values should match. If they do not, verify that the other device can handle the codec conversation or that a transcoder
                                       is in place to handle the service. |
| Sound sample mismatch between the phone and another device | The RxSize and the TxSize statistics show the voice packet sizes that are being used in a conversation between this ATA and
                                       the other device. The values of these statistics should match. |
| Gaps in voice calls | Check the AvgJtr and the MaxJtr statistics. A large variance between these statistics may indicate a problem with jitter on
                                       the network or periodic high rates of network activity. |
| One-way audio | When at least one person in a call does not receive audio, IP connectivity between phones is not established. Check the configurations
                                       in routers and switches to ensure that IP connectivity is properly configures. |
| Phone call cannot be established. | The phone does not have a DHCP IP address and is unable to register with Cisco Unified Communications Manager. Verify the following: The Ethernet cable is attached. The Cisco Unified Communications Manager service is running on the Cisco Unified Communications Manager server. Both phones are registered to the same Cisco Unified Communications Manager. |

| Step 1 | Set up a server that can run your PRT upload script. |
|---|---|
| Step 2 | Write a script that can handle the parameters listed above, or edit the provided sample script to suit your needs. |
| Step 3 | Upload your script to your server. |
| Step 4 | In Cisco Unified Communications Manager, go to the Product Specific
                                          			 Configuration Layout area of the individual device configuration window, Common
                                          			 Phone Profile window, or Enterprise Phone Configuration window. |
| Step 5 | Check Customer support upload URL and
                                          			 enter your upload server URL. Example: http://example.com/prtscript.php |
| Step 6 | Save your changes. |

| You can generate a problem report using one of the following methods: Press the PRT button on the top panel of the ATA 191. The problem report is generated and sent to the system administrator. The LED turns green if the report is sent successfully,
                                                or turns red if the report failed. Press the PRT button again to retry. On the web interface for the device, go to Administration > PRT Viewer .  Click Generate PRT to start the PRT process and generate a problem report. |
|---|