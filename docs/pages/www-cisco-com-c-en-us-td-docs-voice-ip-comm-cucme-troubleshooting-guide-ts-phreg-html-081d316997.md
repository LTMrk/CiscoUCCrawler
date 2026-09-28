---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-troubleshooting-guide-ts-phreg-html-081d316997
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/troubleshooting/guide/ts_phreg.html
retrieved_at: 2026-08-21T09:48:01.161234+00:00
---

Troubleshooting Phone Registration in Cisco Unified CME

# Troubleshooting Phone Registration in Cisco Unified CME

### Download Options

Updated: April 4, 2010

## Table Of Contents

Troubleshooting IP Phone Registration in Cisco Unified CME

Contents

Prerequisites

Begin Here

All IP phones in a Cisco Unified CME system failed to successfully register

All IP phones of a single phone type failed to successfully register

One or more IP phones failed to successfully register

Additional References

Related Documents

Technical Assistance

Obtaining Documentation, Obtaining Support, and Security Guidelines

## Troubleshooting IP Phone Registration in Cisco Unified CME

Last Updated: April 5, 2010 First Published: March 26, 2008

During the phone bootup sequence, the IP phone requests and receives network configuration information and the configuration file, including the IP address of the Cisco Unified CME router, from the TFTP server.

At this point, the IP phone has enough information to request registration from the Cisco Unified CME router to which it is connected. The router verifies the phone's configuration against the router's running configuration. If it is correct, the phone successfully registers with Cisco Unified CME and downloads its phone specific information including phone identification, telephone and extension numbers, phone firmware upgrade - if required, and features. If the phone firmware is required, the phone downloads the appropriate firmware files from the TFTP server and begins the phone bootup sequence again.

An IP phone can register in Cisco Unified CME and not successfully download its configuration information. When this happens, soft keys can appear on the phone display but the extension, name, or label do not appear on the phone display.

The following symptoms can indicate that an IP phone is not successfully registered with the Cisco Unified CME system to which it is connected or that an IP phone is registered with Cisco Unified CME but is not provisioned.

Symptoms

No extension number, name, or label or an incorrect extension number, name, or label appears on the phone display.

## Contents

• Prerequisites

• Begin Here

• All IP phones in a Cisco Unified CME system failed to successfully register

• All IP phones of a single phone type failed to successfully register

• One or more IP phones failed to successfully register

• Additional References

• Obtaining Documentation, Obtaining Support, and Security Guidelines

## Prerequisites

• You have access to a TFTP server for downloading files.

• The hardware and software to establish a physical console connection to the Cisco router using a terminal or PC running terminal emulation is available and operational.

• Cisco router is configured for Cisco Unified CME.

• Phones, phone cables, and ports are operational.

## Begin Here

Note For information about individual commands, see the Cisco Unified CME Command Reference .

To modify or correct the configuration file on the Cisco Unified CME router, see the Cisco Unified CME System Administrator Guide .

Step 1 show ephone registered show voice register statistics

For SCCP phones: Use the show ephone registered command to display the status of registered SCCP phones.

For SIP phones: Use the show voice register statistics command to display statistics associated with the registration event.

Step 2 Are one or more phones registered in the Cisco Unified CME?

• Yes—Go to next step.

• No—See "All IP phones in a Cisco Unified CME system failed to successfully register" section .

Step 3 show ephone show voice register all

For SCCP phones: Use the show ephone command to display the status of SCCP phones that are not registered or are trying to register.

For SIP phones: Use the show voice register all command to display configuration and registration information for SIP phones in Cisco Unified CME.

Step 4 Are all phones that failed to successfully register using the SIP protocol?

• Yes—See "All IP phones in a Cisco Unified CME system failed to successfully register" section .

• No or don't know—Go to Step 5 .

Step 5 Are all of the phones that fail to successfully register of the same type, such as all Cisco Unified IP Phone 7940s or all Cisco Unified IP Phone 7905s?

• Yes—See "All IP phones of a single phone type failed to successfully register" section .

• No or don't know—See "One or more IP phones failed to successfully register" section .

## All IP phones in a Cisco Unified CME system failed to successfully register

If this is a newly installed and configured Cisco Unified CME and all of the phones fail to register, the configuration is incorrect or unavailable. If all IP phones have lost their registration, the network interface is the most likely source of the failure.

Step 1 Is this a brand new installation or configuration and all phones have failed to register?

• Yes—Go to next step.

• No—If you have an external LAN switch, verify that the LAN switch has not been disabled or disconnected from the LAN, or has not failed, then go to the next step. If you have an internal EtherSwitch module, go to the next step.

Step 2 show running-config

Use the show running-config command to display the contents of the currently running configuration file on your Cisco Unified CME router. The following is a partial sample output from the show command including the configuration for an internal DHCP server and Ethernet switch network interface.

```
Router# show running-config
```

```
.
```

```
.
```

```
.
```

```
voice service voip
```

```
allow-connections h323 to sip
```

```
allow-connections sip to h323
```

```
allow-connections sip to sip
```

```
sip
```

```
registrar server expires max 600 min 60  !--- <==== required for SIP phones in 
Cisco Unified CME
```

```
.
```

```
.
```

```
.
```

```
ip dhcp excluded-address 192.0.2.12 192.0.2.12  !--- <==== prevents IP address of Cisco 
router from being assigned to IP phones
```

```
!
```

```
ip dhcp pool voice  !--- <==== configuration for internal DHCP
```

```
network 190.0.2.0 255.255.255.0
```

```
option 150 ip 190.0.2.12  !--- <==== IP address of the TFTP server
```

```
default-router 190.0.2.12  !--- <==== Cisco router to which the IP phones are 
connected
```

```
.
```

```
.
```

```
.
```

```
!
```

```
interface Ethernet0/0  !---< ==== Connects router to network
```

```
ip address 190.0.2.12 255.255.255.0  !---< ==== IP address of internal network 
interface
```

```
half-duplex
```

```
!
```

```
interface Ethernet1/0
```

```
no ip address
```

Note The configuration for the DHCP server will not be included if you are using an external DHCP server. If you have an external DHCP server, Verify that the DHCP server is enabled or enable the DHCP server.

Step 3 Are all phones that failed to successfully register using the SIP protocol?

• Yes—Go to next step.

• No—Go to Step 5 .

Step 4 Does the running configuration include the registrar server command?

• Yes—Go to next step.

• No—Correct the configuration.

Step 5 An incorrect DHCP configuration can prevent IP communications between phones and other devices on the LAN. Does the subnet mask in the DHCP configuration match the one in the network interface?

• Yes—Go to next step.

• No—Correct the configuration file.

Step 6 Is the IP address for the TFTP server, option 150 under the dhcp configuration, correctly configured?

Tip If the Cisco Unified CME router is also the TFTP server and there is an internal Ethernet switch installed in the same router, the IP addresses for the TFTP server, the default-router, and network interface are identical.

• Yes—Go to next step

• No—Correct the configuration file.

Step 7 If the problem persists, contact technical support at http://www.cisco.com/techsupport.

## All IP phones of a single phone type failed to successfully register

All Cisco Unified IP phones of a particular type can fail to register for one of the following reasons:

• The wrong or incorrect Cisco phone firmware filename is specified for a particular phone type.

• The phones cannot download the correct Cisco phone firmware file from the TFTP server.

• Auto assign for a specified phone type is enabled and there are more phones of that type than there are available telephone or extension numbers.

Tip To identify phone firmware filenames associated to specific Cisco Unified  IP phone types and compatible with the Cisco IOS release on the Cisco Unified CME router, see the appropriate Cisco Unified CME Supported Firmware, Platforms, Memory, and Voice Products .

Step 1 show running-config

Use the show running-config command to display the contents of the running configuration file on this Cisco Unified CME router.

```
Router# show running-configuration
```

```
.
```

```
.
```

```
.
```

```
voice service voip
```

```
allow-connections h323 to sip
```

```
allow-connections sip to h323
```

```
allow-connections sip to sip
```

```
sip
```

```
registrar server expires max 600 min 60  !--- <==== required for SIP phones in 
Cisco Unified CME
```

```
.
```

```
.
```

```
.
```

```
!
```

```
telephony-service
```

```
Load 7960-7940 P00308000300  !--- <==== configuration for load command
```

```
Load 7941 SCCP41.8-3-1-21S
```

```
Load 7961 SCCP41.8-3-1-21S
```

```
Load 7971 SCCP70.8-3-1-21S
```

```
Load 7970 SCCP70.8-3-1-21S
```

```
max-ephones 10
```

```
max-dn 10
```

```
ip source-address 200.200.200.1 port 2000
```

```
auto-assign 1 to 10 type 7941  !---< ==== auto-assign configuration
```

```
.
```

```
.
```

```
.
```

```
ip dhcp excluded-address 192.0.2.12 192.0.2.12  !--- <==== prevents IP address of Cisco 
router from being assigned to IP phones
```

```
!
```

```
ip dhcp pool voice
```

```
network 190.0.2.0 255.255.255.0
```

```
option 150 ip 190.0.2.12  !--- <==== IP address of the TFTP server
```

```
default-router 190.0.2.12
```

```
.
```

```
.
```

```
.
```

```
!
```

```
voice register global
```

```
mode cme
```

```
ip source-address 190.0.2.12 port 2000  !--- <==== IP address of the TFTP server
```

```
max-dn
```

```
max-pool
```

```
Load 7960-7940 P0S3-08-02-00  !--- <==== configuration for load command
```

```
...
```

Step 2 Does your running configuration include the auto-assign command?

• Yes—Go to next step

• No—Go to Step 6 .

Step 3 Examine the output for the auto-assign command. Is a phone type specified in the auto-assign configuration?

• Yes—Go to next step

• No—Go to Step 5 .

Step 4 Does the phone type specified in the auto-assign configuration match the phone type of the phone to be registered?

• Yes—Go to next step

• No—Correct the configuration.

Step 5 Does the number specified in the auto-assign configuration match or exceed the number of phones to be registered?

• Yes—Go to next step

• No—Correct the configuration.

Step 6 Examine the output for the load command. Is the phone type in the command correctly identified? Is the appropriate phone firmware filename, including version and protocol, specified for this phone type?

Note The firmware filename must not include the .sbin or .loads suffix for all phones except Cisco ATA and Cisco Unified IP Phone 7905 and 7912.

• Yes—Go to next step

• No—Correct the configuration file.

Step 7 Is the IP address for the TFTP server, option 150 under the dhcp configuration, correctly configured?

Tip If the Cisco Unified CME router is also the TFTP server and there is an internal Ethernet switch installed in the same router, the IP addresses for the TFTP server, the default-router, and network interface are identical.

• Yes—Go to next step

• No—Correct the configuration file.

Step 8 If your Cisco Unified CME router also the TFTP server?

• Yes—Go to next step.

• No—Go to Step 12 .

Step 9 show flash

Use the show flash command to display a list of files in flash memory. The following partial sample output shows SCCP and SIP phone firmware filenames in the list of files

```
Router# show flash
```

```
System flash Directory
```

```
.
```

```
.
```

```
.
```

```
24    333822    P00403020214.bin
```

```
25    398244    P00305000300.sbin
```

```
26    59222     P0S3-07-04-00.bin
```

```
27    461       P0S3-07-04-00.loads
```

Step 10 Are the Cisco phone firmware files required for each phone type installed in flash memory?

• Yes—Go to next step.

• No—See "Installing and Upgrading Cisco Unified CME Software" in the Cisco Unified CME Administrator Guide .

Step 11 Use the reset command to reboot the IP phones. The phone should upgrade its firmware to the new firmware mentioned in the configuration. Does the "File not Found" or "Error verifying configuration" error message appear on the IP phone display?

• Yes—The phone is unable to download the firmware file from the TFTP server. Use the tftp-server flash command to configure your Cisco Unified  CME router or a Flash memory device on your router as a TFTP server, then generate the configuration file. Use the reset command to reboot this IP phone.

• No—If the problem persists, contact technical support at http://www.cisco.com/techsupport.

Step 12 Verify that the tftp-path command is correctly configure for the external TFTP server.

Step 13 Verify that the external TFTP server is reachable. Ping the external TFTP server.

Step 14 Telnet into the external TFTP server and display a list files. Verify or install the appropriate Cisco phone firmware files on the external TFTP server.

Step 15 Use the reset command to reboot the IP phones. The phone should upgrade its firmware to the new firmware mentioned in the configuration. Does the "File not Found" or "Error verifying configuration" error message appear on the IP phone display?

• Yes—The phone is unable to download the firmware file from the TFTP server. Use the tftp-server flash command to configure your Cisco Unified  CME router or a Flash memory device on your router as a TFTP server, then generate the configuration file. Use the reset command to reboot this IP phone.

• No—If the problem persists, contact technical support at http://www.cisco.com/techsupport.

## One or more IP phones failed to successfully register

Typically, an individual Cisco Unified IP phone fails to successfully complete registration for any of the following reasons:

• The configuration file for this IP phone is incorrect or empty.

• The IP phone cannot download its configuration file.

• Auto register is disabled and an individual phone is not explicitly configured.

• Auto assign is enabled and there are more IP phones than there are available telephone or extension numbers.

• The appropriate Cisco phone firmware is not or cannot be installed on this IP phone.

Step 1 show running-config

Use the show running-config command to display the contents of the running configuration file on this Cisco Unified CME router.

```
Router# show running-configuration
```

```
.
```

```
.
```

```
.
```

```
voice service voip
```

```
allow-connections h323 to sip
```

```
allow-connections sip to h323
```

```
allow-connections sip to sip
```

```
sip
```

```
registrar server expires max 600 min 60  !--- <==== required for SIP phones in 
Cisco Unified CME
```

```
.
```

```
.
```

```
.
```

```
!
```

```
telephony-service
```

```
Load 7960-7940 P00308000300  !--- <==== configuration for load command
```

```
Load 7941 SCCP41.8-3-1-21S
```

```
Load 7961 SCCP41.8-3-1-21S
```

```
Load 7971 SCCP70.8-3-1-21S
```

```
Load 7970 SCCP70.8-3-1-21S
```

```
max-ephones 10
```

```
max-dn 10
```

```
ip source-address 200.200.200.1 port 2000
```

```
auto-assign 1 to 10 type 7941  !---< ==== auto-assign configuration
```

```
.
```

```
.
```

```
.
```

```
!
```

Step 2 Is the phone that failed to successfully register using the SIP protocol?

• Yes—Go to next step.

• No—Go to Step 4 .

Step 3 Does the running configuration include the registrar server command?

• Yes—Go to next step.

• No—Correct the configuration.

Step 4 Has this IP phone successfully registered in Cisco Unified CME before today?

• Yes—Go to next step.

• No—Go to Step 10 .

Step 5 Does your running configuration include the auto-assign command?

• Yes—Go to next step

• No—Go to Step 9 .

Step 6 Examine the output for the auto-assign command. Is a phone type specified in the auto-assign configuration?

• Yes—Go to next step

• No—Go to Step 8 .

Step 7 Does the phone type specified in the auto-assign configuration match the phone type of the phone to be registered?

• Yes—Go to next step

• No—Correct the configuration.

Step 8 Does the number specified in the auto-assign configuration match or exceeds the number of phones to be registered?

• Yes—Go to next step

• No—Correct the configuration.

Step 9 Prior to this registration attempt, was this IP phone loaded with the same version of Cisco phone firmware as it is today; i.e., same protocol (SIP or SCCP) or the same release version firmware?

• Yes—Go to next step.

• No—See the "All IP phones of a single phone type failed to successfully register" section

Step 10 Identify the MAC address for this IP phone. The MAC address is located on a label on the rear of the phone.

Step 11 show telephony-service tftp-bindings show voice register tftp-bin

For SCCP phones: Use the show telephony-service tftp-bindings command to display a list of files that were generated during configuration. The following is a partial sample output from the show command.

```
Router(config)# show telephony-service tftp-bindings
```

```
tftp-server system:/its/SEPDEFAULT.cnf
```

```
tftp-server system:/its/SEPDEFAULT.cnf alias SEPDefault.cnf
```

```
tftp-server system:/its/XMLDefault.cnf.xml alias XMLDefault.cnf.xml
```

```
tftp-server system:/its/ATADefault.cnf.xml
```

```
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP00036B54BB15.cnf.xml
```

```
tftp-server system:/its/germany/7960-font.xml alias German_Germany/7960-font.xml
```

```
tftp-server system:/its/germany/7960-dictionary.xml alias 
 German_Germany/7960-dictionary.xml
```

```
tftp-server system:/its/germany/7960-kate.xml alias German_Germany/7960-kate.xml
```

```
tftp-server system:/its/germany/SCCP-dictionary.xml alias 
 German_Germany/SCCP-dictionary.xml
```

```
tftp-server system:/its/germany/7960-tones.xml alias Germany/7960-tones.xml
```

```
.
```

```
.
```

```
.
```

For SIP phones: Use the s how voice register tftp-bind command to display a list of files that were generated during configuration. The following is a partial sample output from the show command.

```
Router(config)# show voice register tftp-bind
```

```
tftp-server SIPDefault.cnf url system:/cme/sipphone/SIPDefault.cnf
```

```
tftp-server syncinfo.xml url system:/cme/sipphone/syncinfo.xml
```

```
tftp-server SIP0009B7F7532E.cnf url system:/cme/sipphone/SIP0009B7F7532E.cnf
```

```
tftp-server SIP000ED7DF7932.cnf url system:/cme/sipphone/SIP000ED7DF7932.cnf
```

```
tftp-server SIP0012D9EDE0AA.cnf url system:/cme/sipphone/SIP0012D9EDE0AA.cnf
```

```
tftp-server gk123456789012 url system:/cme/sipphone/gk123456789012
```

```
tftp-server gk123456789012.txt url system:/cme/sipphone/gk123456789012.txt
```

```
.
```

```
.
```

```
.
```

Step 12 Filenames of configuration files include the designated MAC address for the individual IP phone. Does the file list include a configuration file for the MAC address of this phone?

• Yes—Go to next step.

• No—The create-cnf or create profile (voice register global) command was not issued. Use the appropriate command to generate configuration files for this phone, then use the reset command to reboot this phone. If the problem persists, go to Step 15 .

Step 13 more system: url

Use the more system command to display the contents of the configuration profile for a particular Cisco Unified IP phone. The following is sample output from this command displaying information in three different configuration files; SIP0009B7F7532E.cnf contains no information.

```
Router# more system:/cme/sipphone/XMLDefault.cnf.xml
```

```
<device>
```

```
<devicePool>
```

```
.
```

```
.
```

```
.
```

```
Router# more system:/cme/sipphone/SIP0012D9EDE0AA.cnf
```

```
image_version: "P0S3-07-4-00";
```

```
user_info: "phone";
```

```
line1_name: "1051";
```

```
line1_displayname: "";
```

```
line1_shortname: "";
```

```
line1_authname: "1051";
```

```
.
```

```
.
```

```
.
```

```
Router# more system:/cme/sipphone/SIP0009B7F7532E.cnf
```

```
Router#
```

Step 14 Does the configuration file contain information required for this phone to register?

• Yes—Go to next step.

• No—The create-cnf file or create profile (voice register global) command was not issued. Use the appropriate command to generate configuration files for this phone, then use the reset command to reboot this phone.

Step 15 show ephone show voice register all

For SCCP phones: Use the show ephone command to display information about the state of SCCP phones and locate the configuration information for this phone. The following partial sample output shows registration information for the three IP phones.

```
Router# show ephone
```

```
ephone-2 Mac:000A.8A5C.5961 TCP socket:[1] activeLine:0 REGISTERED
```

```
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
```

```
IP:192.168.0.50 50349 Telecaster 7940  keepalive 23738 max_line 2
```

```
button 1: dn 2  number 91450 CH1 IDLE      CH2 IDLE
```

```
ephone-5 Mac:123E.A432.987B TCP socket:[-1] activeLine:0 UNREGISTERED
```

```
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
```

```
IP:192.168.0.51 52243 Unknown 0 keepalive 0 max_line 0
```

```
ephone-5 Mac:1234.A432.987B TCP socket:[-1] activeLine:0 REGISTERED
```

```
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
```

```
IP:192.168.0.52 50988 Telecaster 7940 keepalive 23 max_line 2
```

For SIP phones: Use the show voice register all command to display information about SIP phones and locate the configuration information for this phone. The following is a partial sample output showing voice register dn and voice register pool information for a phone with the MAC address 123A.8A5C.5961.

```
Router# show voice register all
```

```
.
```

```
.
```

```
.
```

```
VOICE REGISTER DN =================
```

```
Dn Tag 1
```

```
Config:
```

```
Number is 7001
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Name christoper robert
```

```
Auto answer is disabled
```

```
Label is jennifer nicole
```

```
Dn Tag 2 Config:
```

```
Number is 7002
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Name Jenny
```

```
Auto answer is disabled
```

```
.
```

```
.
```

```
.
```

```
VOICE REGISTER POOL ===================
```

```
Pool Tag 1
```

```
Config:
```

```
Mac address is 123A.8A5C.5961
```

```
Type is 7960
```

```
Number list 1 : DN 1
```

```
Proxy Ip address is 0.0.0.0
```

```
Default preference is 1
```

```
DTMF Relay is disabled
```

```
Call Waiting is disabled
```

```
DnD is disabled
```

```
keep-conference is enabled
```

```
template is 1
```

```
Dialpeers created:
```

Step 16 Locate the MAC address for this phone in the command output. Is the correct MAC address configured for this phone?

• Yes—Go to next step.

• No—Correct the configuration file.

Step 17 Is the appropriate telephone or extension number associated with the (ephone) dn or pool tag for this phone?

• Yes—Use the restart command to reboot this phone. If the problem persists, go the next step.

• No—Correct the configuration.

Step 18 Copy and paste the valid configuration information, then use the reset command to reboot this phone. If the problem persists:

a. Unplug this phone.

b. Delete the configuration for this individual phone.

c. Create a simple, one-extension to one-button, ephone or voice register pool configuration for this phone and then generate the configuration file.

d. Plug in this phone.

Step 19 Did this phone successfully register with Cisco Unified CME?

• Yes—Modify the configuration for this phone to add desired features and buttons.

• No—Contact technical support at http://www.cisco.com/techsupport.

## Additional References

The following sections provide references related to Cisco Unified CallManger Express.

### Related Documents

Related Topic

Document Title

Cisco Unified Communications Express

• Cisco Unified CME System Administrator Guide

• Cisco Unified CME Command Reference

• Cisco Unified CME Documentation

Cisco IOS commands

• Cisco IOS Voice Command Reference

• Cisco IOS Software Releases 12.4T Command References

• Cisco IOS Debug Command Reference

Cisco IOS configuration

• Cisco IOS Voice Configuration Library

• Cisco IOS Software Releases 12.4T Configuration Guides

### Technical Assistance

Description

Link

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.

http://www.cisco.com/techsupport

## Obtaining Documentation, Obtaining Support, and Security Guidelines

For information on obtaining documentation, obtaining support, providing documentation feedback, security guidelines, and also recommended aliases and general Cisco documents, see the monthly What's New in Cisco Product Documentation, which also lists all new and revised Cisco technical documentation, at: http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html .

### CCDE, CCENT, CCSI, Cisco Eos, Cisco Explorer, Cisco HealthPresence, Cisco IronPort, the Cisco logo, Cisco Nurse Connect, Cisco Pulse, Cisco SensorBase, Cisco StackPower, Cisco StadiumVision, Cisco TelePresence, Cisco TrustSec, Cisco Unified Computing System, Cisco WebEx, DCE, Flip Channels, Flip for Good, Flip Mino, Flipshare (Design), Flip Ultra, Flip Video, Flip Video (Design), Instant Broadband, and Welcome to the Human Network are trademarks; Changing the Way We Work, Live, Play, and Learn, Cisco Capital, Cisco Capital (Design), Cisco:Financed (Stylized), Cisco Store, Flip Gift Card, and One Million Acts of Green are service marks; and Access Registrar, Aironet, AllTouch, AsyncOS, Bringing the Meeting To You, Catalyst, CCDA, CCDP, CCIE, CCIP, CCNA, CCNP, CCSP, CCVP, Cisco, the Cisco Certified Internetwork Expert logo, Cisco IOS, Cisco Lumin, Cisco Nexus, Cisco Press, Cisco Systems, Cisco Systems Capital, the Cisco Systems logo, Cisco Unity, Collaboration Without Limitation, Continuum, EtherFast, EtherSwitch, Event Center, Explorer, Follow Me Browsing, GainMaker, iLYNX, IOS, iPhone, IronPort, the IronPort logo, Laser Link, LightStream, Linksys, MeetingPlace, MeetingPlace Chime Sound, MGX, Networkers, Networking Academy, PCNow, PIX, PowerKEY, PowerPanels, PowerTV, PowerTV (Design), PowerVu, Prisma, ProConnect, ROSA, SenderBase, SMARTnet, Spectrum Expert, StackWise, WebEx, and the WebEx logo are registered trademarks of Cisco and/or its affiliates in the United States and certain other countries.

### All other trademarks mentioned in this document or website are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1002R)

### Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental. ©2008-2010 Cisco Systems, Inc. All rights reserved.

| Related Topic | Document Title |
|---|---|
| Cisco Unified Communications Express | • Cisco Unified CME System Administrator Guide • Cisco Unified CME Command Reference • Cisco Unified CME Documentation |
| Cisco IOS commands | • Cisco IOS Voice Command Reference • Cisco IOS Software Releases 12.4T Command References • Cisco IOS Debug Command Reference |
| Cisco IOS configuration | • Cisco IOS Voice Configuration Library • Cisco IOS Software Releases 12.4T Configuration Guides |

| Description | Link |
|---|---|
| The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies. To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds. Access to most tools on the Cisco Support website requires a Cisco.com user ID and password. | http://www.cisco.com/techsupport |