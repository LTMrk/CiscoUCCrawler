---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-iosaccesspoint-forensic-investigation-6865886a92
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/iosaccesspoint_forensic_investigation
retrieved_at: 2026-09-01T14:10:37.205105+00:00
---

Home / Cisco Security

Cisco IOS Access Point Software Forensic Data Collection Procedures

# Cisco IOS Access Point Software Forensic Data Collection Procedures

End of Life (EOL) Notice

Introduction

Prerequisites

Step One - Create Cisco IOS Device Problem Description

Step Two - Cisco IOS Runtime Environment

Step Three - Cisco IOS Image File Hash Verification

Step Four - Cisco IOS Core File and Memory Dump

Step Five - Analysis with the verify Command

Step Six - ROMMON Settings Check

Related Documentation

Cisco IOS Device Forensic Report Checklist

Revision History

## End of Life (EOL) Notice

Note: The hardware platforms and software releases that are referenced in this document have reached end of life. Therefore, no further updates will be made to this document.

## Introduction

This document provides guidance for collecting evidence from Cisco IOS access points when compromise or tampering are suspected. It outlines commands that can be run to gather evidence for an investigation, along with the respective output that should be collected upon running these commands. This document also provides procedures for performing integrity checks on a device’s Cisco IOS images, collecting a core file and memory dump from an access point, and checking ROMMON settings.

Note: It is extremely important when triaging a network device for compromise or tampering that the device is not rebooted. Rebooting a device during an initial assessment will irrecoverably delete all volatile information contained within the device (e.g., RAM contents, Address Resolution Protocol (ARP) and routing tables, Network Address Translations, access control list (ACL) hit and drop counts, etc.).

Note: It is highly recommended that a device suspected of tampering or compromise be isolated from the network prior to conducting an initial forensic examination. This may prevent remote unloading of any implant or malware that was installed on the device and will prevent an attacker from monitoring commands that are entered on the device under investigation.

If you require assistance or have questions regarding the following procedures, contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains six main sections:

- Cisco IOS Device Problem Description: Describes why the platform is a candidate for forensic examination

- Cisco IOS Runtime Environment: Collects platform configuration and runtime state

- Cisco IOS Image File Verification: Examines system image hashes for inconsistencies

- Core File and Memory Dump: Obtains a core dump of the running Cisco IOS image and contents of memory

- Analysis with verify : Provides an alternate method of collecting system memory if a core dump cannot be performed

- ROMMON Settings Check: Examines the ROM monitor (ROMMON) for version information and configuration settings

## Prerequisites

The procedures described in this document assume the reader has a basic understanding of Cisco IOS Software command syntax.

A valid cisco.com account is required to view individual Cisco IOS file hashes for software file integrity checking. Alternatively, a publicly available comprehensive list of file hashes (Bulk Hash file) can be downloaded from https://www.cisco.com/c/en/us/about/trust-center/downloads.html .

### Procedure Execution

The procedures contained in this document may be executed either from the access point console or through a network connection that uses SSH. If you are executing these procedures from the console, ensure that the terminal emulator is configured as follows:

- 9600 baud rate

- 8 data bits

- No parity

- 1 stop bit

- No flow control

Note: Make sure flow control is set to None. Console connections to routers and switches allow for Ready to Send/Clear to Send (RTS/CTS) flow control, however, wireless access points require flow control to be turned off.

SSH can be enabled on an access point (or all access points) by configuring the appropriate parameters on the Wireless LAN Controller (WLC) CLI:

```
config ap mgmtuser add username < username > password < password > secret <enable_password> <access_point_name | all>
```

SSH can also be configured from the WLC GUI by navigating to Wireless > Global Configuration > Global Telnet SSH , entering the appropriate parameters in the Login Credentials section, and enabling SSH in the Global Telnet SSH section.

Ensure that any changes made through the WLC CLI or GUI are saved; otherwise, they will not take effect.

### Operating System

The procedures contained in this document are intended for access points running Cisco IOS Software and will not work on access points running Cisco Cheetah operating system (COS) software.

Use the show version | inc BOOTLDR command to determine which operating system the access point is running, as shown in the following example:

```
AIR-AP1852i-1#show version | inc BOOTLDR
BOOTLDR: U-Boot boot loader Version 31
```

A boot loader value of U-Boot indicates the access point is running Cisco COS.

```
AIR-AP1602i-1#show version | inc BOOTLDR
BOOTLDR: C1600 Boot Loader (AP1G2-BOOT-M) LoaderVersion 15.2(2)JAX
```

A boot loader value containing the access point series (C1600 in the example above) indicates the access point is running Cisco IOS Software.

Note: The examples that are used in this document are based on Cisco IOS Software Release 15.3.3 command syntax. The output that is produced by a command may vary depending on the software release that is deployed and/or the features that are supported or configured on the device. Not all commands that are used in these procedures may be supported on earlier releases of the software.

## Step One – Create Cisco IOS Device Problem Description

Describe in as much detail as possible why the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior that cannot be attributed to a misconfiguration or a software or hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific software releases of the following products: Cisco ASA, FMC, FTD, FXOS, IOS, IOS XE, NX-OS, and NX-OS in ACI Mode.

https://sec.cloudapps.cisco.com/security/center/softwarechecker.x

Record any results that are returned by the tool that may explain the anomalous behavior that is being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA, FMC, FTD and FXOS Software, the tool contains only vulnerability information for Cisco Security Advisories first published from January 2022 onward, and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Submit the problem description and any relevant results obtained from the Cisco Software Checker that were collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Two – Cisco IOS Runtime Environment

The initial stage of evidence gathering is completed by issuing a show tech-support command and a dir all-filesystems command. These commands must be executed in enable mode (i.e., privileged EXEC mode), and some of the output produced may vary depending on the particular Cisco IOS version, the configured features, or both.

Execute each of the following commands in enable mode and record the output:

```
show tech-support
dir /all /recursive
```

Optional: The following list of commands may also be executed to gather additional information relevant to the current operating state of the device. Although the output of these commands is not required to perform a forensic analysis of a Cisco IOS platform, they may provide additional information about any unauthorized changes that have been made to the device.

```
terminal length 0
show history all
show clock detail
show startup-config
show reload
show ip route
show cdp nei detail
show ip arp
show ip interface
show ip interface brief
show tcp brief all
show udp detail
show sockets
show ip nat translations verbose
show ip cache flow
show snmp user
show snmp group
show snmp community
show ipv6 interface brief
show ipv6 route
show logging
show processes
```

Submit all command or script output collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Three – Cisco IOS Image File Hash Verification

To enable CLI debugging commands, access the command line of the Cisco IOS wireless access point and use the following command in enable mode:

```
debug capwap console cli
```

Next, examine the boot parameters and calculate a hash value for the system boot images by executing the following commands:

```
show boot
verify /md5 location:filename
show version | inc System image
verify /md5 location:filename
```

The following is an example of this procedure:

```
AIR-CAP1602i-2# debug capwap console cli This command is meant only for debugging/troubleshooting 
Any configuration change may result in different
behavior from centralized configuration. 

CAPWAP console CLI allow/disallow debugging is on

AIR-CAP1602i-2# show boot BOOT path-list:      flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-mx.153-3.JF14
Config file:         flash:/config.txt
Private Config file: flash:/private-config
Enable Break:        yes
Manual Boot:         no
Enable IOS Break:    no
HELPER path-list:    
NVRAM/Config file
      buffer size:   32768
      Mode Button:    on
Radio Core TFTP:

AIR-CAP1602i-2# verify /md5 flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-mx.153-3.JF14 ....................................................................................
MD5 of flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-mx.153-3.JF14 Done!
verify /md5 (flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-mx.153-3.JF14) = 74c465a11702dd3208117ae20e87b7f0 AIR-CAP1602i-2# show version | inc System image System image file is "flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-xx.153-3.JF14" 

AIR-CAP1602i-2# verify /md5 flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-xx.153-3.JF14 ....................................................................................
....................................................................................
....................................................................................
[output truncated]
....................................................................................
....................................................................................
....................................................................................
MD5 of flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-xx.153-3.JF14 Done!
verify /md5 (flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-xx.153-3.JF14) = 03ad60dcbadb99ed5f57611811178b95
```

Note that the embedded hash and computed hash should return the same message digest algorithm 5 (MD5) value, and the cisco.com hash should match the MD5 value listed in the Cisco Software Download Center or in the Bulk Hash File for that particular image file.

Note: Lightweight and Autonomous AP IOS Software packages can be downloaded from cisco.com, and then the hash values from the boot helper and IOS image can be compared to the hash values obtained with the verify command to validate the integrity of the software running on the access point.

If further analysis is required, the boot helper and system image may be copied from the access point using the copy command:

```
copy < location >:< system_image_filename.bin > ftp: 
Address or name of remote host []? < destination_ip >
Destination filename []? < destination_filename.bin >
```

It is highly recommended that a hash value be calculated on the copied system image file and compared to the hash value obtained on the platform to ensure no errors were introduced during the file transfer process.

Repeat the preceding procedure for any other system image file located on the file systems. A comprehensive list of all files can be viewed by executing the following command:

```
dir /all /recursive
```

Submit all command output and any system images collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Four – Cisco IOS Core File and Memory Dump

Caution: This section contains commands that alter device configuration. Please ensure you have the appropriate authorization to make changes to the platform in question prior to proceeding with this procedure.

Note: An access point in lightweight mode receives its configuration from the WLC each time it boots or is reset. If the access point is in autonomous mode (no WLC present) it is highly recommended that the current configuration is backed up in case the configuration needs to be reverted to its original state.

This procedure outlines how to configure a Cisco IOS-based access point in order to obtain a dump of platform memory.

To configure the appropriate dump parameters, enter the following commands in enable mode:

```
debug capwap console cli
conf t
service timestamps debug datetime msec localtime 
service timestamps log datetime msec localtime 
service internal 
exception core-file < filename.bin > compress
exception region-size 65536
exception dump < destination_ip_address >
exception protocol ftp
ip ftp username < username >
ip ftp password < password >
end
```

Caution: Initiating a core dump on a Cisco IOS device can be CPU intensive and may adversely affect any traffic transiting the platform. It is recommended that this procedure be executed at a time when potential disruption to client devices can be minimized.

To initiate the core dump process, execute the following command in enable mode:

```
write core
```

The core dump may take some time to complete, depending on the amount of physical memory (RAM) installed on the device.

When the core dump process is complete, remove the core dump parameters as follows:

```
conf t
no service internal 
no exception core-file
no exception region-size
no exception dump
no exception protocol ftp
no ip ftp username < username >
no ip ftp password < password >
end
```

The following is an example of this procedure:

```
AIR-CAP1602i-2 con0 is now available
Press RETURN to get started.
User Access Verification

Username: admin
Password: 

AIR-CAP1602i-2>en
Password: 

AIR-CAP1602i-2# debug capwap console cli This command is meant only for debugging/troubleshooting 
Any configuration change may result in different
behavior from centralized configuration. 
CAPWAP console CLI allow/disallow debugging is on

AIR-CAP1602i-2# conf t Enter configuration commands, one per line.  End with CNTL/Z.
AIR-CAP1602i-2(config)# service timestamps debug datetime msec localtime AIR-CAP1602i-2(config)# service timestamps log datetime msec localtime AIR-CAP1602i-2(config)# service internal AIR-CAP1602i-2(config)# exception core-file 1602i-core.bin compress AIR-CAP1602i-2(config)# exception region-size 65536 AIR-CAP1602i-2(config)# exception dump 10.10.10.100 AIR-CAP1602i-2(config)# exception protocol ftp AIR-CAP1602i-2(config)# ip ftp username anonymous AIR-CAP1602i-2(config)# ip ftp password qwerty123 AIR-CAP1602i-2(config)#end
*Mar 24 12:43:13.375: %SYS-5-CONFIG_I: Configured from console by admin on console       

AIR-CAP1602i-2# write core Remote host [10.10.10.100]? 
Base name of core files to write [1602i-core.bin]? 
EOF-inputbuf 1000
writing compressed ftp://10.10.10.100/1602i-core.binrambase.Z
! [OK]
4096 bytes copied in 1.120 secs (3657 bytes/sec)
writing compressed ftp://10.10.10.100/1602i-core.biniomem2.Z

*Mar 24 12:43:30.499: Writing 1602i-core.binrambase.Z 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
EOF-inputbuf 100000 [OK] [OK]
966656 bytes copied in 0.672 secs (1438476 bytes/sec)
writing compressed ftp://10.10.10.100/1602i-core.bin.Z
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
*Mar 24 12:43:31.619: Writing 1602i-core.biniomem2.Z 
*Mar 24 12:43:32.287: Writing 1602i-core.bin.Z 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#
# When the core dump has completed, remove the associated configuration:
#

AIR-CAP1602i-2# conf t Enter configuration commands, one per line.  End with CNTL/Z.
AIR-CAP1602i-2(config)# no service internal AIR-CAP1602i-2(config)# no exception core-file AIR-CAP1602i-2(config)# no exception region-size AIR-CAP1602i-2(config)# no exception dump AIR-CAP1602i-2(config)# no exception protocol ftp AIR-CAP1602i-2(config)# no ip ftp username AIR-CAP1602i-2(config)# no ip ftp password AIR-CAP1602i-2(config)# end AIR-CAP1602i-2#
*Mar 24 12:53:11.391: %SYS-5-CONFIG_I: Configured from console by admin on console
```

It is highly recommended that hash values be calculated on the core files obtained in this section so that any errors introduced by subsequent copying or transmission can be reliably detected.

Submit all command or script output collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Five - Analysis with the verify Command

Obtaining a core dump, as outlined in Step Four, is the preferred method of gathering information for analysis in Cisco IOS device forensics. However, there may be times when retrieving a core dump is not possible. This section provides an alternative method for obtaining a copy of the runtime image from the memory of a Cisco IOS device by using the verify /md5 system:memory/text command.

Access the CLI of the Cisco IOS device and use the following commands in enable mode:

```
debug capwap console cli
verify /md5 system:memory/text
copy system:memory/text ftp
```

The following is an example of this procedure:

```
AIR-CAP1602i-2# debug capwap console cli This command is meant only for debugging/troubleshooting 
Any configuration change may result in different
behavior from centralized configuration. 
CAPWAP console CLI allow/disallow debugging is on

AIR-CAP1602i-2# verify /md5 system:memory/text ..............................................................................
..............................................................................
[output truncated]
..............................................................................
...............................................MD5 of system:memory/text Done!
verify /md5 (system:memory/text) = 8fce245cdbc9019f80ed870a71f86364 AIR-CAP1602i-2# copy system:memory/text ftp Address or name of remote host []? 10.10.10.100 Destination filename [text]? 
!!!!!!!!!!!!!!!!!
*Mar 24 12:56:22.519: Writing text 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
30362336 bytes copied in 7.324 secs (4145595 bytes/sec)
```

Submit all command or script output collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Six – ROMMON Settings Check

This procedure simply checks the version of the ROMMON firmware installed on the access point and its current configuration.

Note: This procedure requires the access point to be rebooted and must be executed from the console. Please ensure that all the previous steps in this guide have been completed prior to reloading the device.

Execute the following command in enable mode:

```
reload
```

When the access point begins to boot (e.g., when the “Boot from flash” string is displayed on the console), hit the Esc or break key to interrupt the boot sequence and enter ROMMON mode, then enter the following commands at the ap shell prompt:

```
version
set
```

To return the access point to operation, simply enter the boot command:

```
boot
```

An example of this procedure follows:

```
Boot from flash
IOS Bootloader - Starting system.
 FLASH CHIP: Spansion S25FL256 
Xmodem file system is available.
flashfs[0]: 69 files, 9 directories
flashfs[0]: 0 orphaned files, 0 orphaned directories
flashfs[0]: Total bytes: 31936000
flashfs[0]: Bytes used: 21310464
flashfs[0]: Bytes available: 10625536
flashfs[0]: flashfs fsck took 10 seconds.
Reading cookie from SEEPROM
Base Ethernet MAC address: 00:12:34:56:78:90

The system boot has been aborted.  The following
commands will finish loading the operating system 
software:

    ether_init
    tftp_init
    boot

ap: version C1600 Boot Loader (AP1G2-BOOT-M) LoaderVersion 15.2(2)JAX, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Compiled Fri 30-Nov-12 15:48 by aselvara

ap: set 0=0
AP_IMAGE_RCV=flash:/ap1g2-rcvk9w8-mx/ap1g2-rcvk9w8-mx
AP_MD5_LAST_SUCCESSFUL_TIME=01:32:24 UTC Mar 8 2021
BOOT=flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-mx.153-3.JF14
DEFAULT_ROUTER=10.0.0.1
ENABLE_BREAK=yes
IOS_STATIC_DEFAULT_GATEWAY=10.10.10.1
IOS_STATIC_IP_ADDR=10.10.10.90
IOS_STATIC_NETMASK=255.255.255.0
IP_ADDR=10.0.0.1
MANUAL_BOOT=no
NETMASK=255.255.255.224
NEW_IMAGE=yes
RELOAD_REASON=23
TERMLINES=0

ap: boot Loading "flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-mx.153-3.JF14"...##############
File "flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-mx.153-3.JF14" uncompressed and installed, entry point: 0x2004000
executing...
File "flash:/ap1g2-k9w8-mx.153-3.JF14/ap1g2-k9w8-mx.153-3.JF14" uncompressed and installed, entry point: 0x2004000
executing...

Secondary Bootloader - Starting system.
[output truncated]
```

Submit all command output and the system:memory/text binary file collected in this section to the relevant TAC SR.

## Related Documentation

Additional information about Cisco software integrity assurance, as well as forensic investigation procedures for other platforms, is available in Cisco Security Tactical Resources: https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## Cisco IOS Device Forensic Response Checklist

Step One – Create Cisco IOS Device Problem Description

Device problem description uploaded to SR

Step Two – Cisco IOS Runtime Environment

Output of show tech-support uploaded to SR

Output of dir /all /recursive uploaded to SR

Output of other show commands uploaded to SR (Optional)

Step Three – Cisco IOS Image File Hash Verification

Output of verify on system image files uploaded to SR

Output of verify on system image files uploaded to SR

Step Four – Cisco IOS Core File and Memory Dump

Output of write core uploaded to SR

Core file uploaded to SR

Core dump parameters unconfigured

Step Five – Analysis with the verify Command

Output of verify /md5 system:memory/text uploaded to SR

Copy of system:memory/text uploaded to SR

Step Six – ROMMON Settings Check

Output of version and set uploaded to SR

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Step One – Create Cisco IOS Device Problem Description |  |
|---|---|
| Device problem description uploaded to SR |  |
| Step Two – Cisco IOS Runtime Environment |  |
| Output of show tech-support uploaded to SR |  |
| Output of dir /all /recursive uploaded to SR |  |
| Output of other show commands uploaded to SR (Optional) |  |
| Step Three – Cisco IOS Image File Hash Verification |  |
| Output of verify on system image files uploaded to SR |  |
| Output of verify on system image files uploaded to SR |  |
| Step Four – Cisco IOS Core File and Memory Dump |  |
| Output of write core uploaded to SR |  |
| Core file uploaded to SR |  |
| Core dump parameters unconfigured |  |
| Step Five – Analysis with the verify Command |  |
| Output of verify /md5 system:memory/text uploaded to SR |  |
| Copy of system:memory/text uploaded to SR |  |
| Step Six – ROMMON Settings Check |  |
| Output of version and set uploaded to SR |  |

| Version | Date | Author(s) | Comments |
|---|---|---|---|
| 1.0 | May 3, 2021 | Dan Maunz | Initial public release. |
| 1.1 | July 22, 2024 | Dan Maunz | Final release. |