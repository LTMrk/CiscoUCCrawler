---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-adminguide-administration-pa2d-b-7800-mpp-ag-11-pa2d-fe357d4100
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/adminguide/administration/pa2d_b_7800-mpp-ag-11/pa2d_b_7800-mpp-ag-11_chapter_010000.html
retrieved_at: 2026-09-01T15:41:49.385667+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Updated: April 29, 2019

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## General Troubleshooting Information

The following table provides general troubleshooting information for the Cisco IP Phone.

Summary

Explanation

Connecting a Cisco IP Phone to another Cisco IP Phone

Cisco does not support connecting an IP phone to another IP Phone through the PC port. Each IP Phone should connect directly
                                       to a switch port. If phones are connected together in a line by using the PC port, the phones do not work.

Prolonged broadcast storms cause IP phones to reset, or be unable to make or answer a call

A prolonged Layer 2 broadcast storm (lasting several minutes) on the voice VLAN may cause IP phones to reset, lose an active
                                       call, or be unable to initiate or answer a call. Phones may not come up until a broadcast storm ends.

Moving a network connection from the phone to a workstation

If you power your phone through the network connection, you must be careful if you decide to unplug the network connection
                                       of the phone and plug the cable into a desktop computer.

The network card in the computer cannot receive power through the network connection; if power comes through the connection,
                                                   the network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the
                                                   phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a phone
                                                   on the line and to stop providing power to the cable.

Changing the telephone configuration

By default, the administrator password settings are locked to prevent users from making changes that could impact their network
                                       connectivity. You must unlock the administrator password settings before you can configure them.

Codec mismatch between the phone and another device

The RxType and the TxType statistics show the codec that is used for a conversation between this Cisco IP Phone and the other
                                       device. The values of these statistics should match. If they do not, verify that the other device can handle the codec conversation,
                                       or that a transcoder is in place to handle the service. See Display Call Statistics Window for details.

Sound sample mismatch between the phone and another device

The RxSize and the TxSize statistics show the size of the voice packets that are used in a conversation between this Cisco
                                       IP Phone and the other device. The values of these statistics should match. See Display Call Statistics Window for details.

Loopback condition

A loopback condition can occur when the following conditions are met:

- The SW Port Configuration option on the phone is set to 10 Half (10-BaseT/half duplex).

- The phone receives power from an external power supply.

- The phone is powered down (the power supply is disconnected).

In this case, the switch port on the phone can become disabled and the following message appears in the switch console log:

HALF_DUX_COLLISION_EXCEED_THRESHOLD

To resolve this problem, reenable the port from the switch.

## Startup Problems

After you install a phone into your network and you can access the phone web page (phone Configuration Utility), the phone
                              should start up as described in the related topic below.

If the phone does not start up properly, see the following sections for troubleshooting information.

### Cisco IP Phone Does Not Go Through the Normal Startup Process

#### Problem

When you connect a Cisco IP Phone to the network port, the phone does not go through the normal startup process as described
                                 in the related topic and the phone screen does not display information.

#### Cause

If the phone does not go through the startup process, the cause may be faulty cables, bad connections, network outages, lack
                                 of power, or the phone may not be functional.

#### Solution

To determine whether the phone is functional, use the following suggestions to eliminate other potential problems.

Verify that the network port is functional:

Exchange the Ethernet cables with cables that you know are functional.

Disconnect a functioning Cisco IP Phone from another port and connect it to this network port to verify that the port is active.

Connect the Cisco IP Phone that does not start up to a different network port that is known to be good.

Connect the Cisco IP Phone that does not start up directly to the port on the switch, eliminating the patch panel connection
                                             in the office.

Verify that the phone is receiving power:

If you are using external power, verify that the electrical outlet is functional.

If you are using in-line power, use the external power supply instead.

If you are using the external power supply, switch with a unit that you know to be functional.

If the phone still does not start up properly, power up the phone with the handset off-hook. When the phone is powered up
                                       in this way, it attempts to launch a backup software image.

If the phone still does not start up properly, perform a factory reset of the phone.

After you attempt these solutions, if the phone screen on the Cisco IP Phone does not display any characters after at least
                                       five minutes, contact a Cisco technical support representative for additional assistance.

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

#### Phone Cannot Connect Using DNS

##### Problem

The DNS settings may be incorrect.

##### Solution

If you use DNS to access the TFTP server or Third-Party Call Control Manager, you must ensure that you specify a DNS server.

### Configuration File Corruption

#### Problem

If you continue to have problems with a particular phone that other suggestions in this chapter do not resolve, the configuration
                                 file may be corrupted.

#### Solution

Get a new configuration file remotely from the provisioning server using resync .

### Cisco IP Phone Cannot Obtain IP Address

#### Problem

If a phone cannot  obtain an IP address when it starts up, the phone may not be on the same network or VLAN as the DHCP server,
                                 or the switch port to which the phone connects may be disabled.

#### Solution

Ensure that the network or VLAN to which the phone  connects has access to the DHCP server, and ensure that the switch port
                                 is enabled.

## Phone Reset Problems

If users report that their phones are resetting during calls or while the phones are idle on their desk, you should investigate
                           the cause. If the network connection and Third Party Call Control connection are stable, a Cisco IP Phone should not reset.

Typically, a phone resets if it has problems in connecting to the Ethernet network or to Third Party Call Control.

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

## General Telephone Call Problems

The following sections help troubleshoot general telephone call problems.

### Phone Call Cannot Be Established

#### Problem

A user complains about not being able to make a call.

#### Cause

The phone does not have a DHCP IP address. The phones display the message Configuring IP or Registering .

#### Solution

Verify the following:

- The Ethernet cable is attached.

- The Third-Party Call Control system is active.

Enable audio server debug and capture logs on both phones, then examine the logs.

### Phone Does Not Recognize DTMF Digits or Digits Are Delayed

#### Problem

The user complains that numbers are missed or delayed when the keypad is used.

#### Cause

Pressing the keys too quickly can result in missed or delayed digits.

#### Solution

Keys should not be pressed rapidly.

## Feature Troubleshooting

Here is troubleshooting information related to some of the phone features.

### ACD Call Information Missing

#### Problem

A call center phone does not see call information during a call.

#### Solution

Check the phone configuration to determine if Call Information Enable is set to yes.

Check the Broadsoft server configuration to determine if the user's Device Profile is configured with "Support Call Center MIME Type" .

### Phone Doesn't Show ACD Softkeys

#### Problem

The phone doesn't display the Agent Sign In or Agent Sign Out softkeys.

#### Solution

Check Broadsoft server configuration to determine if that user has been configured as a call center agent.

Enable the programmable softkeys (PSK) and add the ACD softkeys to the softkey list. For more information, see Configuring Programmable Softkeys .

Check the phone configuration to determine if BroadSoft ACD is set to yes.

### Call Doesn't Record

#### Problem

When a user tries to record a call, the recording doesn't takes place.

#### Cause

This is often due to configuration issues.

#### Solution

Set the phone to always record a call.

Make a call.

If the recording doesn't start, there are configuration problems. Check the configuration of the BroadWorks and third-party
                                 recorder.

If the recording does start:

Set the phone to record on demand.

Set up Wireshark to capture a trace of the network traffic between the phone and Broadworks when the problem occurs. When
                                       you have the trace, contact TAC for further assistance.

### An Emergency Call Doesn't Connect to Emergency Services

#### Problem

A user tries to place an emergency call, but the call doesn't connect to the emergency services (fire, police, or emergency
                                 services operator).

#### Solution

Check the emergency call configuration:

Company Identifier or location request URL setup is incorrect. See Configure a Phone to Make Emergency Calls .

An incorrect or blank emergency number exists in the Dial Plan setup. See Dial Plan

The location request servers (emergency call service provider) did not respond with a phone location, after multiple attempts.

### Presence Status Doesn't Work

#### Problem

The phone doesn't show presence information.

#### Solution

Use UC Communicator as a reference to verify that the account works.

### Phone Presence Message: Disconnected from Server

#### Problem

Instead of presence information, the user sees the message Disconnected from server .

#### Solution

Check the Broadsoft server configuration to determine if IM&P service is enabled and assigned to that user.

Check the phone configuration to determine if the phone can connect to the internet and get the XMPP messages.

Check the XMPP Incoming and Outgoing messages printed in the syslog to make sure it can login successfully.

### Phone Cannot Access BroadSoft Directory for XSI

#### Problem

The phone displays XSI directory access error.

#### Solution

Check Broadsoft server configuration for the user login and SIP credentials.

Check error messages in syslog.

Check information on the error on the phone screen.

If HTTPS connection fails, check the error message on the phone screen and in the syslog.

Install custom CA for HTTPS connection if the BroadSoft certificate is not signed from phone built-in root CA.

## Phone Display Problems

Your users may see unusual screen displays. Use the following sections to troubleshoot the problem.

### The Font is Too Small or Has Unusual Characters

#### Problem

The phone screen has smaller fonts than expected or there are unusual characters displayed. Examples of unusual characters
                                 are letters from a different alphabet from the characters that the locale uses.

#### Cause

Possible causes are:

TFTP server does not have the correct set of locale and font files

XML files or other files are specified as a font file

The font and locale files did not download successfully.

#### Solution

Font files and locale files must be in the same directory.

Do not add or change files in the locale and font folder structure.

On the phone web page, select Admin Login > Advanced > Info > Status and scroll to the Locale Download Package section to verify that the locale and font files downloaded successfully. If they did not, try the download again.

### Phone Screen Displays Boxes Instead of Asian Characters

#### Problem

The phone is set for an Asian language, but the phone shows square boxes instead of Asian characters.

#### Cause

Possible causes are:

TFTP server does not have the correct set of locale and font files.

The font and locale files did not download successfully.

#### Solution

Font files and locale files must be in the same directory.

On the phone web page, select Admin Login > Advanced > Info > Status and scroll to the Locale Download Package section to verify that the locale and font files downloaded successfully. If they did not, try the download again.

### Softkey Labels are Truncated

#### Problem

The softkey labels appear to be truncated.

#### Cause

The phone has the wrong version of files in the TFTP server.

#### Solution

Check that the file version is correct for the phone model. Each phone model has its own files.

### Phone Locale is Not Displayed

#### Problem

The phone is set to use a different language from the one that is displayed.

#### Cause

TFTP server does not have the correct set of locale and font files.

#### Solution

Font files and locale files must be in the same directory.

## Report All Phone
                        	 Issues from the Phone Web Page

If you are working
                              		  with Cisco TAC to troubleshoot a problem, they typically require the logs from
                              		  the Problem Reporting Tool to help resolve the issue. You can generate PRT logs
                              		  using the phone web page and upload them to a remote log server.

### Before you begin

Access the phone
                              		  administration web page. See Access the Phone Web Page .

Select Info > Debug
                                             				  Info .

In the Problem Reports section, click Generate PRT .

Enter the
                                       			 following information in the Report
                                          				Problem screen:

Enter the
                                             				  date that you experienced the problem in the Date field. The current date appears in this field
                                             				  by default.

Enter the
                                             				  time that you experienced the problem in the Time field. The current time appears in this field
                                             				  by default.

In the Select Problem drop-down list box, choose the
                                             				  description of the problem from the available options.

Click Submit in the Report
                                          				Problem screen.

The Submit
                                          				button is enabled only if you select a value in the Select Problem drop-down list box.

You get a
                                          				notification alert on the Phone Web page that indicates if the PRT upload was
                                          				successful or not.

## Report a Phone Problem Remotely

You can initiate a phone problem report remotely. The phone generates a problem report using the Cisco Problem Report Tool
                              (PRT), with the problem description "Remote PRT Trigger" . If you have configured an upload rule for problem reports, the phone uploads the problem report according to the upload
                              rule.

You can see the status of the problem report generation and upload on the phone administration web page. When a problem report
                              is successfully generated, you can download the problem report from the phone administration web page.

To initiate a phone problem report remotely, initiate a SIP-NOTIFY message from the server to the phone, with the Event specified as prt-gen .

## Troubleshooting Procedures

These procedures can be used to identify and correct problems.

### Check DHCP Settings

On the phone, press Applications .

Select Admin Settings > Network Setup > IPv4 Setup .

Check the DHCP server field.

Check the DHCP option for enabled or disabled.

Check the IP Address, Subnet Mask, and Default Router fields.

If you assign a static IP address to the phone, you must manually enter settings for these options.

If you are using DHCP, check the IP addresses that your DHCP server distributes.

See the Understanding and Troubleshooting DHCP in Catalyst Switch or Enterprise Networks document, available at this URL:

https://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml

### Verify DNS Settings

On the phone, press Applications .

Select Admin Settings > Network Setup > IPv4 Setup

Check that the DNS Server 1 field is set correctly.

You should also verify that a CNAME entry was made in the DNS server for the TFTP server and for the Third-Party Call Control.

You must also ensure that DNS is configured to do reverse lookups.

## Additional Troubleshooting Information

If you have additional questions about troubleshooting your phone, go to the following Cisco website and  navigate to the
                           desired phone model:

https://www.cisco.com/cisco/web/psa/troubleshoot.html

| Summary | Explanation |
|---|---|
| Connecting a Cisco IP Phone to another Cisco IP Phone | Cisco does not support connecting an IP phone to another IP Phone through the PC port. Each IP Phone should connect directly
                                       to a switch port. If phones are connected together in a line by using the PC port, the phones do not work. |
| Prolonged broadcast storms cause IP phones to reset, or be unable to make or answer a call | A prolonged Layer 2 broadcast storm (lasting several minutes) on the voice VLAN may cause IP phones to reset, lose an active
                                       call, or be unable to initiate or answer a call. Phones may not come up until a broadcast storm ends. |
| Moving a network connection from the phone to a workstation | If you power your phone through the network connection, you must be careful if you decide to unplug the network connection
                                       of the phone and plug the cable into a desktop computer. Caution The network card in the computer cannot receive power through the network connection; if power comes through the connection,
                                                   the network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the
                                                   phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a phone
                                                   on the line and to stop providing power to the cable. | Caution | The network card in the computer cannot receive power through the network connection; if power comes through the connection,
                                                   the network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the
                                                   phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a phone
                                                   on the line and to stop providing power to the cable. |
| Caution | The network card in the computer cannot receive power through the network connection; if power comes through the connection,
                                                   the network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the
                                                   phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a phone
                                                   on the line and to stop providing power to the cable. |
| Changing the telephone configuration | By default, the administrator password settings are locked to prevent users from making changes that could impact their network
                                       connectivity. You must unlock the administrator password settings before you can configure them. Note If the administrator password is not set in common phone profile, then user can modify the network settings. | Note | If the administrator password is not set in common phone profile, then user can modify the network settings. |
| Note | If the administrator password is not set in common phone profile, then user can modify the network settings. |
| Codec mismatch between the phone and another device | The RxType and the TxType statistics show the codec that is used for a conversation between this Cisco IP Phone and the other
                                       device. The values of these statistics should match. If they do not, verify that the other device can handle the codec conversation,
                                       or that a transcoder is in place to handle the service. See Display Call Statistics Window for details. |
| Sound sample mismatch between the phone and another device | The RxSize and the TxSize statistics show the size of the voice packets that are used in a conversation between this Cisco
                                       IP Phone and the other device. The values of these statistics should match. See Display Call Statistics Window for details. |
| Loopback condition | A loopback condition can occur when the following conditions are met: The SW Port Configuration option on the phone is set to 10 Half (10-BaseT/half duplex). The phone receives power from an external power supply. The phone is powered down (the power supply is disconnected). In this case, the switch port on the phone can become disabled and the following message appears in the switch console log: HALF_DUX_COLLISION_EXCEED_THRESHOLD To resolve this problem, reenable the port from the switch. |

| Caution | The network card in the computer cannot receive power through the network connection; if power comes through the connection,
                                                   the network card can be destroyed. To protect a network card, wait 10 seconds or longer after unplugging the cable from the
                                                   phone before plugging it into a computer. This delay gives the switch enough time to recognize that there is no longer a phone
                                                   on the line and to stop providing power to the cable. |
|---|---|

| Note | If the administrator password is not set in common phone profile, then user can modify the network settings. |
|---|---|

| Step 1 | Select Info > Debug
                                             				  Info . |
|---|---|
| Step 2 | In the Problem Reports section, click Generate PRT . |
| Step 3 | Enter the
                                       			 following information in the Report
                                          				Problem screen: Enter the
                                             				  date that you experienced the problem in the Date field. The current date appears in this field
                                             				  by default. Enter the
                                             				  time that you experienced the problem in the Time field. The current time appears in this field
                                             				  by default. In the Select Problem drop-down list box, choose the
                                             				  description of the problem from the available options. |
| Step 4 | Click Submit in the Report
                                          				Problem screen. The Submit
                                          				button is enabled only if you select a value in the Select Problem drop-down list box. You get a
                                          				notification alert on the Phone Web page that indicates if the PRT upload was
                                          				successful or not. |

| To initiate a phone problem report remotely, initiate a SIP-NOTIFY message from the server to the phone, with the Event specified as prt-gen . |
|---|

| Step 1 | On the phone, press Applications . |
|---|---|
| Step 2 | Select Admin Settings > Network Setup > IPv4 Setup . |
| Step 3 | Check the DHCP server field. Check the DHCP option for enabled or disabled. |
| Step 4 | Check the IP Address, Subnet Mask, and Default Router fields. If you assign a static IP address to the phone, you must manually enter settings for these options. |
| Step 5 | If you are using DHCP, check the IP addresses that your DHCP server distributes. See the Understanding and Troubleshooting DHCP in Catalyst Switch or Enterprise Networks document, available at this URL: https://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a00800f0804.shtml |

| Step 1 | On the phone, press Applications . |
|---|---|
| Step 2 | Select Admin Settings > Network Setup > IPv4 Setup |
| Step 3 | Check that the DNS Server 1 field is set correctly. |
| Step 4 | You should also verify that a CNAME entry was made in the DNS server for the TFTP server and for the Third-Party Call Control. You must also ensure that DNS is configured to do reverse lookups. |