---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-asa-forensic-investigation-html-f899116426
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/asa_forensic_investigation.html
retrieved_at: 2026-09-01T14:10:20.754858+00:00
---

Home / Cisco Security

Cisco ASA Forensic Data Collection Procedures

# Cisco ASA Forensic Data Collection Procedures

Introduction

Prerequisites

Step One - ASA Device Problem Description

Step Two - Document the ASA Runtime Environment

Step Three - ASA Image File Hash Verification

Step Four - Verify Digitally Signed Image Authenticity

Step Five - ASA Memory Dump and Core File Generation

Step Six - ROMMON Settings Check

Step Seven - SSL VPN Configuration Integrity Check

Acknowledgments

Related Documentation

ASA Device Forensic Checklist

Revision History

## Introduction

This document provides guidance for collecting forensic evidence from Cisco ASA 5500-X Series and ASAv Firewalls that are suspected of compromise or tampering. It outlines a number of commands that can be run to gather evidence for an investigation along with the respective output that should be collected upon running these commands. This document also provides information on how to perform integrity checks on an ASA’s system images, and includes a procedure for collecting a core file/memory dump from an ASA device.

Note : This document applies only to Cisco ASA Software and to no other Cisco operating systems. This document does not apply to any of the service modules that may be installed or running within a Cisco ASA device, such as an IPS or FirePOWER module.

Important : It is extremely important when triaging a network device for compromise or tampering that it is not rebooted. Rebooting a device during an initial assessment will irrecoverably lose all volatile information contained within the device (e.g., RAM contents, arp and routing tables, NAT translations, ACL hit and drop counts, etc.).

Note : It is highly recommended that a device suspected of tampering or compromise be isolated from the network prior to conducting an initial forensic examination. This may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device under investigation.

If you require assistance, or have questions regarding the procedures below, contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains seven sections:

- ASA Device Problem Description – Describes why the platform is a candidate for forensic examination

- ASA Runtime Environment – Collects platform configuration and runtime state

- ASA Image File Verification – Examines system image hashes for inconsistencies

- Digitally Signed Image Verification – Examines system and running images for proper signing characteristics

- Memory Dump and Core File Generation – Obtains a copy of the text memory segment and a core file

- ROM Monitor Variables – Examines ROM monitor settings for remote system image loading

- SSL VPN Integrity Checks – Examines the webvpn configuration (if enabled) for tampering

## Prerequisites

The procedures outlined in this document assume the reader has a basic understanding of Cisco ASA Software command syntax.

A valid cisco.com account is required to view individual ASA Software and ASA firmware file hashes for software file integrity checking. For customers without a cisco.com account, a publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded at https://www.cisco.com/c/en/us/about/trust-center/downloads.html

A Cisco Technical Assistance Center (TAC) service request (SR) for the device in question is required because these procedures assume that the information gathered in each step will be uploaded to a TAC SR.

Note: The examples that are used in this document are based on Cisco ASA Software Release 9.16(4)85 command syntax. The output that is produced by a command may vary depending on the software release that is deployed and/or the features that are supported or configured on the device. Not all commands that are used in these procedures may be supported on earlier releases of the software.

Important: If the ASA platform is in multiple context mode, the procedures and commands contained in this document must be executed from the system context.

## Step One – ASA Device Problem Description

Describe in as much detail as possible WHY the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior than cannot be attributed to a misconfiguration or a software/hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific software releases of the following products: Cisco ASA Software, FMC Software, FTD Software, FXOS Software, IOS Software, IOS XE Software, NX-OS Software, and NX-OS Software in ACI Mode.

Record any results that are returned by the tool that may explain the anomalous behavior being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA, FMC, FTD, and FXOS Software, the tool contains only vulnerability information for Cisco Security Advisories first published from January 2022 onward, and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Submit the problem description and any relevant results that are obtained from the Cisco Software Checker and collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Two – Document the ASA Runtime Environment

The initial stage of evidence gathering is completed by issuing a show tech-support command and two dir commands. These commands must be executed in enable mode (i.e., privileged EXEC mode), and some of the output produced may vary depending on the particular ASA Software version and/or features supported or configured on the device.

Execute each of the following commands in enable mode and record the output:

```
terminal pager 0
show tech-support detail
dir /recursive all-filesystems
dir /recursive cache:
```

Note : The output of the show tech-support detail command may be redirected to a file on the local filesystem that can be copied off the platform at a later time, or to a remote server using  the FTP, SCP, SMB, or TFTP protocols. An example of this command follows:

```
show tech-support detail | redirect disk0:/tech-support.txt
```

The following list of commands may also be executed to gather additional information relevant to the current operating state of the device. Although the output of these commands is not required to perform a forensic analysis of an ASA platform, it may provide additional information regarding any unauthorized changes made to the device if compromise is suspected. Note that if the ASA platform is in multiple context mode some of the optional commands below can only be executed in the system context, and other commands can only be executed in the admin or user-defined contexts.

Execution of the following commands in this section of Step 2 is optional.

```
terminal pager 0
show history
show clock detail
show startup-config
show reload
show processes
show kernel process detail
show kernel ifconfig
show kernel module
show logging
show route
show eigrp neighbor
show ospf neighbor
show bgp summary
show arp
show ip address
show interface ip brief
show nat detail
show snmp-server user
show snmp-server group
show ipv6 interface brief
show ipv6 route
show conn all
show xlate
show aaa login-history
```

Submit all command output collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Three – ASA Image File Hash Verification

Access the command line of the Cisco ASA device and issue the following command in enable mode:

```
show version | inc image
```

Note the location and filename of the ASA system image file and then execute the following command:

```
verify /sha-512 location:filename
```

Alternatively, an MD5 hash value can be calculated with the following command:

```
verify /md5 location:filename
```

An example of this procedure follows:

```
ciscoasa# show version | include image
System image file is "disk0:/asa9-16-4-85-lfbff-k8.SPA"

ciscoasa# verify /sha-512 disk0:/asa9-16-4-85-lfbff-k8.SPA
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[output omitted]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Done!
verify /SHA-512 (disk0:/asa9-16-4-85-lfbff-k8.SPA) = 30877b7bc94359a8b88b47611f31e232420f4f9257156027cd4f88c0b896f57881a2e9f1e4eddb86c38ecd78693495786918
28cffc5479fbbd18100711f53aaf
```

The computed hash calculated by the verify command should match the SHA-512 value listed on CCO or in the Bulk Hash File for that particular image file.

Repeat the above procedure for any other system image file located on the file systems. A comprehensive list of all files can be viewed by executing the following command:

```
dir all-filesystems
```

If any of the image file hashes show inconsistencies, copy the image file in question to a secure location if possible.

```
copy <location>:<system_image_filename.bin> ftp: 
Address or name of remote host []? <destination_ip> Destination filename []? <destination_filename.bin>
```

It is highly recommended that a hash value be calculated on the copied system image file and compared to the hash value obtained on the platform to ensure no errors were introduced during the file transfer process.

The example below utilizes the sha512sum utility, which is included with most Linux distributions.

```
root@ftp-server:~# sha512sum asa9-16-4-85-lfbff-k8.SPA
30877b7bc94359a8b88b47611f31e232420f4f9257156027cd4f88c0b896f57881a2e9f1e4edd
b86c38ecd7869349578691828cffc5479fbbd18100711f53aaf asa9-16-4-85-lfbff-k8.SPA
root@ftp-server:~#
```

Note that the ASA verify command and the sha512sum utility both produce a SHA-512 hash value of 30877b7bc94359a8b88b47611f31e232420f4f9257156027cd4f88c0b896f57881a2e9f1e4eddb86c38ecd7869349578691828cffc5479fbbd18100711f53aaf for the asa9-16-4-85-lfbff-k8.SPA.

Submit all command output (including all computed hash values) and any system images collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Four – Verify Digitally Signed Image Authenticity

Cisco ASA Software implements digitally signed system images on most platforms. Digitally signed Cisco ASA Software uses asymmetric (public-key) cryptography, which increases the security posture of Cisco ASA devices by ensuring that the software running on the system has not been altered and that the software originates from a trusted source.

Note : Digitally signed Cisco ASA Software images can be identified by the .SPA label in the image name.

Some ASA platforms, such as the Cisco ASA 5500-X Series, also support Secure Boot technologies. Cisco Secure Boot is a secure startup process that a Cisco device performs each time it boots up. Beginning with the initial power-on, a special purpose hardware device, known as the Trust Anchor module, verifies the integrity of the ROMMON code and the ASA image via digital signatures as they each are loaded. If any failures are detected, the user is notified of the error and the device will wait for the operator to correct the error. This prevents the network device from executing tainted network software.

For additional information, see Trust Anchor Technology .

Note : The show software authenticity set of commands were introduced in Cisco ASA Software version 9.3(2) and are supported only on ASA hardware platforms that incorporate Cisco Secure Boot technologies. These commands may not produce output on older platforms or virtual machine editions of ASA Software.

The authenticity and integrity of a system image file can be verified by using the following command:

```
show software authenticity file location:filename
```

An example of this procedure follows:

```
ciscoasa# show software authenticity file disk0:/asa9-16-4-85-lfbff-k8.SPA
File Name                     : disk0:/asa9-16-4-85-lfbff-k8.SPA
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : NCS_Kenton_ASA
        Organization Name     : CiscoSystems
    Certificate Serial Number : 68AFDEF8
    Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The Organization Name and Organization Unit values can be viewed to verify that the system image signature is valid.

It is also important to verify the authenticity and integrity of the running system image, and this can be accomplished with the following command:

```
show software authenticity running
```

An example of this procedure follows:

```
ciscoasa# show software authenticity running
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : NCS_Kenton_ASA
        Organization Name     : CiscoSystems
    Certificate Serial Number : 68AFDEF8
    Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : ROMMON
        Verifier Version      : Cisco ROMMON,1.1.18
```

The Organization Name and Organization Unit values can be viewed to verify that the system image signature is valid, and the certificate serial number should be the same as the value obtained from the show software authenticity file command. In the examples above, the authenticity check of the ASA software image on disk0 and the authenticity check of the running image both produce a value of 68AFDEF8.

Last, obtain a copy of the public keys by using the following command:

```
show software authenticity keys
```

An example of this procedure follows:

```
ciscoasa# show software authenticity keys

Public Key #1 Information
--------------------------
Key Type              : Release (Primary)
Public Key Algorithm  : 2048-bit RSA
Modulus :
        96:A2:E6:E4:51:4D:4A:B0:F0:EF:DB:41:82:A6:AC:D0:
        FC:11:40:C2:F0:76:10:19:CE:D0:16:7D:26:73:B1:55:
        FE:42:FE:5D:5F:4D:A5:D5:29:7F:91:EC:91:4D:9B:33:
        54:4B:B8:4D:85:E9:11:2D:79:19:AA:C5:E7:2C:22:5E:
        F6:66:27:98:1C:5A:84:5E:25:E7:B9:09:80:C7:CD:F4:
        13:FB:32:6B:25:B5:22:DE:CD:DC:BE:65:D5:6A:99:02:
        95:89:78:8D:1A:39:A3:14:C9:32:EE:02:4C:AB:25:D0:
        38:AD:E4:C9:C6:6B:28:FE:93:C3:0A:FE:90:D4:22:CC:
        FF:99:62:25:57:FB:A7:C6:E4:A5:B2:22:C7:35:91:F8:
        BB:2A:19:42:85:8F:5E:2E:BF:A0:9D:57:94:DF:29:45:
        AA:31:56:6B:7C:C4:5B:54:FE:DE:30:31:B4:FC:4E:0C:
        9D:D8:16:DB:1D:3D:8A:98:6A:BB:C2:34:8B:B4:AA:D1:
        53:66:FF:89:FB:C2:13:12:7D:5B:60:16:CA:D8:17:54:
        7B:41:1D:31:EF:54:DB:49:40:1F:99:FB:18:38:03:EE:
        2D:E8:E1:9F:E6:B2:C3:1C:55:70:F4:F3:B2:E7:4A:5A:
        F5:AA:1D:03:BD:A1:C3:9F:97:80:E6:63:05:27:F2:1F
Exponent              : 65537
Key Version           : A

Public Key #2 Information
--------------------------
Key Type              : Release (Backup)
Public Key Algorithm  : 2048-bit RSA
Modulus :
        96:A2:E6:E4:51:4D:4A:B0:F0:EF:DB:41:82:A6:AC:D0:
        FC:11:40:C2:F0:76:10:19:CE:D0:16:7D:26:73:B1:55:
        FE:42:FE:5D:5F:4D:A5:D5:29:7F:91:EC:91:4D:9B:33:
        54:4B:B8:4D:85:E9:11:2D:79:19:AA:C5:E7:2C:22:5E:
        F6:66:27:98:1C:5A:84:5E:25:E7:B9:09:80:C7:CD:F4:
        13:FB:32:6B:25:B5:22:DE:CD:DC:BE:65:D5:6A:99:02:
        95:89:78:8D:1A:39:A3:14:C9:32:EE:02:4C:AB:25:D0:
        38:AD:E4:C9:C6:6B:28:FE:93:C3:0A:FE:90:D4:22:CC:
        FF:99:62:25:57:FB:A7:C6:E4:A5:B2:22:C7:35:91:F8:
        BB:2A:19:42:85:8F:5E:2E:BF:A0:9D:57:94:DF:29:45:
        AA:31:56:6B:7C:C4:5B:54:FE:DE:30:31:B4:FC:4E:0C:
        9D:D8:16:DB:1D:3D:8A:98:6A:BB:C2:34:8B:B4:AA:D1:
        53:66:FF:89:FB:C2:13:12:7D:5B:60:16:CA:D8:17:54:
        7B:41:1D:31:EF:54:DB:49:40:1F:99:FB:18:38:03:EE:
        2D:E8:E1:9F:E6:B2:C3:1C:55:70:F4:F3:B2:E7:4A:5A:
        F5:AA:1D:03:BD:A1:C3:9F:97:80:E6:63:05:27:F2:1F
Exponent              : 65537
Key Version           : A
```

Submit all command output and any system images collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Five – ASA Memory Dump and Core File Generation

### Text Segment Memory Dump

Obtaining a core dump as outlined below is the preferred method for retrieving a complete copy of device memory contents. However, it is considered a best practice to retrieve a copy of the text memory segment first in case there are issues encountered during the core dump procedure, or in cases where a device cannot be rebooted.

Note: The ASA platform must be running software version 9.6.2 or higher in order to successfully execute this procedure.

Execute the following commands to retrieve software and firmware version information, calculate a hash value for the text segment, and copy the text segment off the platform:

```
show version | include Version
verify /sha-512 system:/text
copy system:/text ftp:
```

An example of this procedure follows:

```
ciscoasa# show version | include Version
Cisco Adaptive Security Appliance Software Version 9.16(4)85 
SSP Operating System Version 2.10(1.3000)
Device Manager Version 7.23(1)
FPGA UPGRADE Version      : 3.0
FPGA GOLDEN Version       : 3.0
ROMMON Version            : 1.1.18
Key Version               : A

ciscoasa# verify /sha-512 system:/text
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[output omitted]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Done!
verify /SHA-512 (system:/text) = 79e797186f8ac438427cc07cc8ec944f5d9117554aa74387caf
1eed6785d753afa6c1366f05768df9aadb716f04cbfdd9403728dff1052a56b59060e45d7bb02

ciscoasa# copy system:/text ftp:
Source filename [text]? 
Address or name of remote host []? 10.10.10.1
Destination filename [text]? system.text.bin
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
INFO: No digital signature found
64647168 bytes copied in 1.600 secs (64647168 bytes/sec)
```

It is highly recommended that a hash value be calculated on the copied memory segment file and compared to the hash value obtained on the platform to ensure no errors were introduced during the file transfer process.

The example below utilizes the sha512sum utility which is included with most Linux distributions.

```
root@ftp-server:~# sha512sum system.text.bin
79e797186f8ac438427cc07cc8ec944f5d9117554aa74387caf1eed6785d753afa6c1366
f05768df9aadb716f04cbfdd9403728dff1052a56b59060e45d7bb02 system.text.bin
root@ftp-server:~#
```

Note that the ASA verify command and the sha512sum utility both produce a SHA-512 hash value of 79e797186f8ac438427cc07cc8ec944f5d9117554aa74387caf1eed6785d753afa6c1366f05768df9aadb716f04cbfdd9403728dff1052a56b59060e45d7bb02 for the system.text.bin file.

Submit all command output (including all computed hash values) and any system images collected in this section to the relevant TAC SR, and proceed to the next section of this document.

### ASA Core File Generation

CAUTION: This section contains commands that alter the ASA device configuration. Please ensure you have a copy of the original device configuration and the appropriate authorization to make changes to the platform in question prior to proceeding with this procedure.

WARNING: Executing the tasks in this section will trigger an immediate reload of the ASA platform. Cisco recommends performing this task during a maintenance window. Cisco does not recommend performing this task if additional forensic evidence needs to be collected, as a reload of the device may cause the loss of information vital to a forensic investigation.

This procedure outlines how to configure a Cisco ASA device in order to obtain a dump of platform memory. The core dump is saved on the Cisco ASA file system in the /coredumpfsys directory and the storage space required may vary from several hundred megabytes to several gigabytes in size dependent on device model. Please ensure that there is enough space on the destination ASA flash or disk file system to accommodate the coredump.

To configure the system to generate a coredump, use the coredump enable command in configuration mode:

```
conf t
coredump enable filesystem filesystem
```

An example of this procedure follows:

```
ciscoasa# conf t
ciscoasa(config)# coredump enable filesystem disk0: 

WARNING: Enabling coredump on an ASA5516 platform will delay
the reload of the system in the event of software forced reload.
The exact time depends on the size of the coredump generated.

Proceed with coredump filesystem allocation of 300 MB
on 'disk0:' (Note this may take a while) ? [confirm]
filesys_image created ok: disk0:coredumpfsysimage.bin

Making coredump file system image !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Coredump file system image created & mounted successfully
/dev/loop0 on /mnt/disk0/coredumpfsys type vfat (rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro)
```

To initiate the core dump process, execute the following command in enable mode:

```
crashinfo force page-fault
```

The core dump may take some time to complete, depending on the amount of physical memory (RAM) installed on the device.

```
ciscoasa# crashinfo force page-fault 

WARNING: This command will force a crash and cause a
         reboot. Do you wish to proceed? [confirm]: 

Register dump: Thread DATAPATH-0-1594 in thread group
other: Unknown
        r8 0x00007ff18a4428c0
        r9 0x0000000000000001
       r10 0x0000000000000000
       r11 0x0000000000000000
       r12 0x00007ff179b4d680

[output truncated]

Begin to dump crashinfo to flash....

End of console dump.
Do 'show crashinfo' after reboot to retrieve other crash information
Process shutdown finished
[18679665.877738] 
[18679665.877738] Writing coredump file to flash. Please do not reload.
[18679665.877738] 
[18679665.877738] Coredump starting....
[18679666.076200]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Coredump completed
INIT: Sending processes the TERM signal
Rebooting... (status 0x8b)
```

When the core dump process is complete, the ASA will reboot.

The core dump is written to a compressed file located on the /coredumpfs file system. The name of the file can be displayed using the following command:

```
dir disk0:/coredumpfsys

ciscoasa# dir disk0:/coredumpfsys
Directory of disk0:/coredumpfsys/
102 -rwx  87316449 13:50:20 Feb 04 2026 core_smp.2026Feb04_134922.1605.11.gz
1 file(s) total size: 87316449 bytes
7365468160 bytes total (6451314688 bytes free/87% free)
```

It is highly recommended that hash values be calculated on the core files obtained in this section so that any errors introduced by subsequent copying or transmission can be reliably detected.

Submit all command output and core files collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Six – ROMMON Settings Check

The ROM monitor firmware of the ASA platform is executed when the ASA is powered up or reset. The firmware initializes the platform hardware and boots the ASA operating system software. Because the ROM monitor settings are persistent if they have been synced to NVRAM, information about the ROM monitor variable values could indicate an attempt to influence the Cisco ASA boot sequence. The set command can be used while in the ROM monitor prompt to see the value of the ROM monitor variables.

ROM monitor mode is accessed by rebooting the ASA device and pressing the BREAK or ESC key during the reload process when prompted as depicted in the example below.

```
ciscoasa# reload
Proceed with reload? [confirm] 
ciscoasa# 
***
*** --- START GRACEFUL SHUTDOWN ---
Shutting down isakmp
Shutting down webvpn
Shutting down sw-module
Shutting down License Controller
Shutting down File system
***
*** --- SHUTDOWN NOW ---
Process shutdown finished
Rebooting... (status 0x9)

[output truncated]

Cisco Systems ROMMON, Version 1.1.18, RELEASE SOFTWARE
Copyright (c) 1994-2020  by Cisco Systems, Inc.
Compiled Tue 09/15/2020 20:35:13.52 by wchen64

Current image running: Boot ROM0
Last reset cause: PowerCycleRequest
DIMM Slot 0 : Present
DIMM Slot 1 : Present

Platform ASA5516 with 8192 Mbytes of main memory
MAC Address: 6c:8b:d3:22:78:95

Use BREAK or ESC to interrupt boot.
Use SPACE to begin boot immediately.
Boot interrupted.  
rommon 1 >
```

The following example shows the output of the ROM monitor set command on a Cisco ASA platform:

```
rommon 1 > set
    ADDRESS=
    NETMASK=
    GATEWAY=
    SERVER=
    IMAGE=
    CONFIG=
    PS1="rommon ! > "
```

The example above depicts a platform where the ROM monitor values are at their default values and have not been altered.

To return the ASA platform to normal operation, simply issue the boot command at the ROM monitor prompt as depicted in the example below:

```
rommon 2> boot
Located '.boot_string' @ cluster 1139973.
#
Located 'asa9-16-4-85-lfbff-k8.SPA' @ cluster 105477.
##############################################################################
##############################################################################
LFBFF signature verified.
INIT: version 2.88 booting

[output truncated]
```

Submit all command output obtained in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Seven – SSL VPN Configuration Integrity Check

The Cisco ASA platform supports the termination of clientless SSL VPN connections, and when this feature is configured, the Cisco ASA will enable an internal web server that listens for remote connections to the SSL VPN portal.

The SSL VPN portal configuration is stored in XML files and additional functionality can be added through the importation of client plug-ins. These ActiveX or Java plug-ins enable features for SSL VPN sessions such as Remote Desktop Protocol (RDP), Secure Shell (SSH) and Telnet, and Virtual Network Computing (VNC) to name a few.

The XML configuration files and imported client plug-ins can both be sources of web-based exploit code, such as java code injection and malicious iframes for example, and should be examined if these features are enabled and the ASA platform is suspected of being compromised and/or tampered with.

Verifying that SSL VPN portal is enabled and retrieving the XML configuration code can be accomplished with the following commands:

```
show run | begin webvpn
export webvpn customization dfltCustomization filesystem:/filename
```

An example of this procedure follows:

```
ciscoasa# show run | begin webvpn
webvpn
 enable outside
 http-headers
  hsts-server
   enable
   max-age 31536000
   include-sub-domains
   no preload
  hsts-client
   enable
  x-content-type-options
  x-xss-protection
  content-security-policy
 anyconnect image disk0:/anyc/anyconnect-linux64-4.9.06037-webdeploy-k9.pkg 1
 anyconnect image disk0:/anyc/anyconnect-macos-4.9.06037-webdeploy-k9.pkg 2
 anyconnect image disk0:/anyc/anyconnect-win-4.9.06037-webdeploy-k9.pkg 3
 anyconnect enable
[output truncated]

ciscoasa# export webvpn customization dfltCustomization disk0:/webvpn.txt
%INFO: Customization object 'DfltCustomization' was exported to disk0:/webvpn.txt
```

Note : The presence of webvpn in the configuration does not by itself indicate that SSL VPN is enabled, it must also be accompanied by an enable <interface_name> statement.

In the example above, a SSL VPN portal is configured on the outside interface (as indicated by the “enable outside” statement), and the DfltCustomization configuration file is copied to webvpn.txt on disk0, which may now be copied off the ASA platform via FTP for analysis.

### Checking the Integrity of SSL VPN Plugins

Any imported SSL VPN plug-ins can be enumerated and copies of the plug-ins extracted from the ASA using the following commands:

```
show import webvpn plug-in detail
export webvpn plug-in protocol protocol url/filename
```

Note : If no plug-ins have been imported, the show import webvpn plug-in detail command will not produce any output.

An example of this procedure follows:

```
ciscoasa# show import webvpn plug-in detail
ssh,telnet   pHjJoOO34pptovI2yD594rvZKc4= Sun, 22 Dec 2013 02:07:29 GMT

ciscoasa# export webvpn plug-in protocol ssh,telnet ftp://10.10.10.1/ ssh.12.21.2013.jar
```

The first command enumerates all of the SSL VPN plug-ins that have been imported into the ASA platform, and the second command exports specific plug-ins to a FTP server where hash values can be calculated and compared with values listed on CCO or in the Bulk Hash File for that particular plug-in file.

Note : The string pHjJoOO34pptovI2yD594rvZKc4= in the example above is a base-64 encoded SHA-1 hash of the ssh,telnet plug-in file. It is recommended that plug-ins be copied off the device and a SHA-512 or MD5 hash calculated as only SHA-512 and MD5 hash values are listed on the CCO website.

The example below utilizes the sha512sum utility, which is included with most Linux distributions.

```
root@ftp-server:~# sha512sum ssh.12.21.2013.jar
9d38ef2071cd18eadd875648323bb8ee5b9e0b5d12a2191400d6ab7168a58e325a860de787bfca 487a1abaf4ed58e8efc38ef45de9ef5e5534adcddfde9eb95f  ssh.12.21.2013.jar
root@ftp-server:~#
```

The example below utilizes the md5sum utility which is included with most Linux distributions.

```
root@ftp-server:~# md5sum ssh.12.21.2013.jar      
a3d64b3d0291bb992e43ab43235dd9cc  ssh.12.21.2013.jar
root@ftp-server:~#
```

Submit all command output obtained in this section to the relevant TAC SR.

## Acknowledgments

The author would like to thank all members of the Customer Experience Security Programs (CXSP) and Advanced Security Initiatives Group (ASIG) who provided their expertise and support during the writing of this document.

## Related Documentation

Additional information about Cisco Software Integrity Assurance, as well as forensic data collection procedures for other platforms, is available in Cisco Security Tactical Resources: https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## ASA Device Forensic Response Checklist

Step 1 - Create the ASA Device Problem Description

Device Problem Description uploaded to SR

Step 2 - Document ASA Runtime Environment

Output of show tech-support uploaded to SR

Output of dir all-filesystems uploaded to SR

Step 3 - ASA Image File Hash Verification

Output of verify on system image files uploaded to SR

Image files with hash inconsistencies uploaded to SR

Step 4 - ASA Digitally Signed Image Authenticity Verification

Output of show software authenticity file uploaded to SR

Output of show software authenticity running uploaded to SR

Output of show software authenticity keys uploaded to SR

Step 5 - ASA  Memory Dump/Core File Generation

Output of verify on memory text segment uploaded to SR

Copy of the memory text segment uploaded to SR

Output of crashinfo uploaded to SR

Core file uploaded to SR

Step 6 - ASA ROM Monitor Variable Check

Output of set command uploaded to SR

Step 7 - SSL VPN Configuration Integrity Check (If applicable)

Output of export webvpn command uploaded to SR

Output of show import webvpn command uploaded to SR

Plug-in files with hash inconsistencies uploaded to SR

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
| 1.0 | 8/19/2019 | Dan Maunz | Initial public release. |
| 1.1 | 03/02/2022 | Dan Maunz | Added cert check and made various updates. |
| 1.2 | 04/11/2023 | Dan Maunz | Validated procedures on Release 9.16.4. |
| 1.3 | 01/25/2024 | Dan Maunz | Reordered the procedures in Step 5. |
| 1.4 | 02/18/2025 | Dan Maunz | Minor content adjustments. |
| 1.5 | 02/24/2026 | Dan Maunz | Validated procedures on Release 9.16(4).85. |
| 1.6 | 06/04/2026 | Dan Maunz | Minor content adjustments. |