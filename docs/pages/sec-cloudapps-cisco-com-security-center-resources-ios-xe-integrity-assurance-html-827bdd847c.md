---
doc_id: sec-cloudapps-cisco-com-security-center-resources-ios-xe-integrity-assurance-html-827bdd847c
source_url: https://sec.cloudapps.cisco.com/security/center/resources/ios_xe_integrity_assurance.html
retrieved_at: 2026-09-01T14:11:10.977118+00:00
---

Home / Cisco Security

Cisco IOS XE Software Integrity Assurance

# Cisco IOS XE Software Integrity Assurance

### Contents

Introduction Architecture Notes and Differences with Cisco IOS Software Potential Attack Methods Commands Manipulating Cisco IOS XE Images Vulnerabilities Identification Techniques Cisco IOS XE Image File Verification Using the Message Digest 5 File Validation Feature Using the Image Verification Feature Using Offline Image File Hashes Using Information from Cisco.com Verifying Authenticity for Digitally Signed Images Cisco IOSd Run-Time Memory Integrity Verification Introduction, Limitation, and Caveats Text Memory Section Export Compute the MD5 Checksum of a Known-Good Text Section Verify MD5 Validation Feature for the Text Region Additional Indicators of Compromise Unusual and Suspicious Commands Checking That IOSd Call Stacks Are Within the Text Section Boundaries Checking the Command History Checking Platform Shell Access Logs and Syslog Checking External Accounting Logs Checking External Syslog Logs Checking Booting Information Checking the ROM Monitor Information Security Best Practices Maintain Cisco IOS XE Image File Integrity Implement Change Control Harden the Software Distribution Server Keep Cisco IOS XE Software Updated Deploy Digitally Signed Cisco IOS XE Images Cisco Secure Boot Cisco Value Chain Security Use Authentication, Authorization, and Accounting Use TACACS+ Authorization to Restrict Commands Implement Credentials Management Implement Configuration Controls Protect Interactive Access to Devices Gain Traffic Visibility with NetFlow Use Centralized and Comprehensive Logging Conclusion Acknowledgments References Revision History

# Introduction

This document analyzes injection of malicious software in Cisco IOS XE Software and describes ways to verify that the software on a Cisco router, both in device storage and in running memory, has not been modified. Additionally, the document presents common best practices that can aid in protecting against attempts to inject malicious software (also referred to as malware) in a Cisco IOS XE device. This document applies only to Cisco IOS XE Software and to no other Cisco operating systems. Customers running Cisco IOS Software can refer to Cisco IOS Software Integrity Assurance .

Malware is software created to modify a device's behavior for the benefit of a malicious third party (attacker). One of the characteristics of effective malware is that it can run on a device stealthily in privileged mode. Malware may be designed to monitor and exfiltrate information from the operating system on which it is running without being detected. Potentially, sophisticated Cisco IOS XE malware would attempt to hide its presence by modifying Cisco IOS XE command output that would reveal information about it.

An additional property of malware is the capability to be remotely programmable from a command-and-control (C&C) server. Methods for using telemetry data to identify possibly compromised infrastructure devices are discussed in the Telemetry-Based Infrastructure Device Integrity Monitoring white paper.

In general, malware can be installed by using various methods, including using stolen administrator credentials, leveraging insecure physical access to devices, exploiting vulnerabilities on the system, or by manipulating an authorized user via a number of social engineering attacks.

On Cisco devices running Cisco IOS XE Software, a limited number of infection methods are available to malware. Malicious software in Cisco IOS XE Software may be introduced in the following ways:

- By altering the software image stored on the onboard device file system. These types of malware would be persistent and would remain after a reboot.

- By tampering with Cisco IOS XE memory during run time. In this case, the malware is not persistent and a reload will remove the in-memory malware from the Cisco IOS XE device.

- By modifying the ROM monitor on systems with flash-based ROM monitor storage.

- By obtaining privileged access to the Cisco IOS XE platform shell and install a *unix-based rootkit.

- By a combination of some or all of the preceding mechanisms

# Architecture Notes and Differences with Cisco IOS Software

Cisco IOS XE is a Linux-based operating system (OS) running on various Cisco platforms. It features a layered architecture providing control plane and data plane separation. The control plane is managed by the IOS daemon (IOSd), which inherits most properties and features from the Cisco IOS operating system.

While Cisco IOS XE Software has a lot of similarity with Cisco IOS Software, there are some important architectural differences that are relevant when talking about attack vector and forensic analysis of a device running Cisco IOS XE Software.

The most notable difference is that Cisco IOS XE is based on the Linux kernel. This opens a series of new attack vectors because an attacker that has access to the operating system could potentially use any available root kit for Linux to manipulate the system. Therefore, it is imperative that an administrator protect access to the Linux OS

Because Cisco IOS XE features a layered architecture, different processes handle different functions. The most important process running on Cisco IOS XE device is the IOSd process, which provides control plane functionality. Attackers would most likely focus on this process as this could give an entry point to modify the integrity of the device towards accomplishing their goals. However there are additional important areas that could be of interest for an attacker such as the one providing data plane functionality (for a Cisco ASR 1000 Series Aggregation Services Router is the Quantum Flow Processor), or the software running on the interface cards.

Currently there is no method that can be used to verify the integrity of all the components of Cisco IOS XE architecture. This document focuses on providing methods to help verifying the integrity of the IOSd and gives security best practices to prevent and detect software-based device tampering.

# Potential Attack Methods

To install malware in Cisco IOS XE Software, attackers will try to use one of the methods described in this section. Cisco IOS XE Software implements several techniques, including the use of safe coding practices, Address Space Layout Randomization (ASLR), and digitally signed software to help protect against memory and code manipulation and provide assurances of authenticity. However, these technologies will not protect Cisco IOS XE Software from unauthorized access due to compromised credentials. Specifically, for Cisco IOS XE this is particularly dangerous as theft of administrative credential may lead to unauthorized access with root privileges to the Linux OS, augmenting the attack surface. Readers should note that a user with administrative access to a device, be it a Cisco device or one from any other vendor, will be able to perform activities that may be dangerous or disruptive, and that that user may also be able to hide these activities. Attacks will often exploit inadequacies in secure configuration and network design.

## Commands

Some Cisco IOS XE devices offer a limited set of commands that are intended to be used by Cisco Technical Assistance Center (TAC) engineers during the process of troubleshooting a technical problem. Such advanced troubleshooting and diagnostic commands require privileged EXEC level and require valid credentials to execute. Thus, these commands could be an area that attackers can focus on to identify ways to run malicious software in Cisco IOS XE.

It is important to note that not all Cisco IOS XE platforms offer advanced diagnostic commands. Of the platforms that do, only a very limited set of such commands is usually available. Additionally, to run these commands, a user needs administrative access to the device. Thus, following common authentication and command authorization security best practices will help prevent a malicious user from using these commands to attempt to install malicious software in Cisco IOS XE Software. Such best practices are discussed in the Security Best Practices section of this document.

## Manipulating Cisco IOS XE Images

It is possible that an attacker could insert malicious code into a Cisco IOS XE Software image and load it onto a Cisco device that supports the image. This attack scenario applies to any computing device that loads its operating system from a writable device. While this attack scenario is not likely, there are image verification techniques, discussed in the Cisco IOS XE Image File Verification section of this document, that could prevent the router from loading such an image. Administrators should, whenever possible, use products that support Cisco Secure Boot and image signing.

## Vulnerabilities

As with every operating system, there is a possibility that a vulnerability could exist in Cisco IOS XE Software that, under certain conditions, could allow malicious code execution. In such a scenario, an attacker who exploited the vulnerability would install or run malicious code in Cisco IOS XE Software, which could then be used to take malicious action, such as modifying device behaviors or exfiltrating information. The Cisco Product Security Incident Response Team (PSIRT) manages and discloses all vulnerabilities in and fixes for Cisco products. Any vulnerability that Cisco is made aware of is investigated and disclosed in accordance with the Cisco vulnerability disclosure policy .

The following table summarizes possible attack methods, the privileges required to perform each attack, and the recommended best practices that, if followed, can greatly reduce the chance of a successful attack:

Table 1. Possible Attack Methods

# Identification Techniques

This section describes methods that can identify the modification of Cisco IOS XE image files and run-time memory. The absence of indicators of compromise using these methods may not guarantee that the Cisco IOS XE device is free from compromise. Readers should note that when facing potential exploitation, the chain of custody becomes important. Administrators need to be aware of chain of custody through all forensic activities, including those presented below, because an exploit could alter specific forensic outputs that would further affect the forensic analysis.

Note: The examples in this document, unless otherwise noted, are taken from a Cisco ASR 1000 Series Aggregation Services Router running Cisco IOS XE Software version 03.08.02.S and IOSd version 15.3(1)S2 advanced enterprise. The output on your device may differ based on device model, operating system release, and feature set. In addition, the commands in this document may use a different syntax, or they may not be present at all. The Cisco recommendation is to follow up with your support organization if you need details about implementing these recommendations for a specific combination of device model, Cisco IOS XE release, and feature set.

## Cisco IOS XE Image File Verification

Network administrators can use one of several security features to verify the authenticity and integrity of Cisco IOS XE Software images in use on their network devices. It is also possible to use a process that does not rely on features in Cisco IOS XE Software. Verifying the MD5 hash of Cisco IOS XE images using the more thorough offline process described below is an important option as it does not rely on the output of a potentially compromised device.

The following sections contain information about Cisco IOS XE Software features and administrative processes that can be used to verify the authenticity and integrity of a Cisco IOS XE Software image.

### Using the Message Digest 5 File Validation Feature

The Message Digest 5 (MD5) File Validation feature allows network administrators to calculate the MD5 hash of a Cisco IOS XE Software image file that is loaded on a device. It also allows administrators to verify the calculated MD5 hash against that provided by the user. After the MD5 hash value of the installed Cisco IOS XE image is determined, it can also be compared with the MD5 hash provided by Cisco to verify the integrity of the image file.

Note: The MD5 File Validation feature can be used only to check the integrity of a Cisco IOS XE Software image that is stored on a Cisco IOS XE device. It cannot be used to check the integrity of an image running in memory.

MD5 hash calculation and verification using the MD5 File Validation feature can be accomplished using the following command:

```
verify /md5 filesystem:filename [md5-hash]
```

Network administrators can use the verify /md5 privileged EXEC command to verify the integrity of image files that are stored on the Cisco IOS XE file system of a device. The following example shows how to use the verify /md5 command on a Cisco IOS XE device:

```
router# verify /md5 bootflash:asr1001-universalk9.03.08.02.S.153-1.S2.bin .....<output truncated>.....Done! verify /md5 (bootflash:asr1001-universalk9.03.08.02.S.153-1.S2.bin) = 8307d56881931c08c3fed66d169823a4 router#
```

Network administrators can also provide an MD5 hash to the verify command. If the hash is provided, the verify command will compare the calculated and provided MD5 hashes as illustrated in the following example:

```
router# verify /md5 bootflash:asr1001-universalk9.03.08.02.S.153-1.S2.bin 8307d56881931c08c3fed66d169823a4 .....<output truncated>.....Done! Verified (bootflash:asr1001-universalk9.03.08.02.S.153-1.S2.bin) = 8307d56881931c08c3fed66d169823a4 router#
```

If the network administrator provides an MD5 hash that does not match the hash calculated by the MD5 File Validation feature, an error message will be displayed. This message is shown in the following example:

```
router# verify /md5 bootflash:asr1001-universalk9.03.08.02.S.153-1.S2.bin e383bf779e137367839593efa8f0f725 .....<output truncated>.....Done! %Error verifying bootflash:asr1001-universalk9.03.08.02.S.153-1.S2.bin
Computed signature = 8307d56881931c08c3fed66d169823a4 
Submitted signature = e383bf779e137367839593efa8f0f725 router#
```

For additional information about how to use this feature, see the MD5 File Validation document.

Since release 16.5.1, the SHA-512 algorithm is also supported in the verify command by using /sha512 instead of /md5 .

### Using the Image Verification Feature

The Image Verification feature builds on the MD5 File Validation functionality to allow network administrators to more easily verify the integrity of an image file that is loaded on the Cisco IOS XE file system of a device. The purpose of the Image Verification feature is to ensure that corruption of the Cisco IOS XE Software image file has not occurred. The corruption detected by this feature could have occurred at any time, such as during the download from Cisco.com or the installation process.

Note: The Image Verification feature does not check the integrity of the image running in memory.

Cisco IOS XE Software image file verification using this feature can be accomplished using the following commands:

- file verify auto

- copy [ /erase ] [ /verify | /noverify ] source-url destination-url

- reload [ warm ] [ /verify | /noverify ] [ text | in time [ text ] | at time [ text ] | cancel

Network administrators can use the file verify auto global configuration command to enable verification of all images that are either copied using the copy privileged EXEC command or loaded using the reload privileged EXEC command. These images are automatically verified for image file integrity.

The following example shows how to configure the file verify auto Cisco IOS XE feature:

```
router# configure terminal router(config)# file verify auto router(config)# exit router#
```

In addition to file verify auto , both the copy and reload commands have a /verify argument that enables the Image Verification feature to check the integrity of the Cisco IOS XE image file. This argument must be used each time an image is copied to or reloaded on a Cisco IOS XE device if the global configuration command file verify auto is not present.

For information about the copy /verify and reload /verify commands, see the Image Verification document

### Using Offline Image File Hashes

For a file stored on an administrative workstation, a network administrator can verify the MD5 hash for that Cisco IOS XE image file using an MD5 hashing utility. Such utilities include md5sum for the Linux operating system, md5 for the BSD operating system, and fsum , MD5summer , and WinMD5 for Microsoft Windows platforms. Additionally, the size of the Cisco IOS XE image file can be obtained using the ls command on Linux and BSD operating systems and the dir command on Microsoft Windows platforms.

The following example demonstrates the MD5 calculation and file size display for Linux-based systems:

```
$ 
$ md5sum asr1001-universalk9.03.08.02.S.153-1.S2.bin 8307d56881931c08c3fed66d169823a4 asr1001-universalk9.03.08.02.S.153-1.S2.bin
$
$ ls -l asr1001-universalk9.03.08.02.S.153-1.S2.bin -r--r--r--   1 user user 392877324 May 16 15:17   asr1001-universalk9.03.08.02.S.153-1.S2.bin 
$
```

The following example shows the use of the fsum utility on a Windows system:

```
C:\> fsum -md5 asr1001-universalk9.03.08.02.S.153-1.S2.bin 
SlavaSoft Optimizing Checksum Utility - fsum 2.52.00337 
Implemented using SlavaSoft QuickHash Library <www.slavasoft.com> 
Copyright (C) SlavaSoft Inc. 1999-2007. All rights reserved. 
       
; SlavaSoft Optimizing Checksum Utility - fsum 2.52.00337 <www.slavasoft.com> 
; 
; Generated on 06/15/14 at 00:01:13 ;
8307d56881931c08c3fed66d169823a4 *asr1001-universalk9.03.08.02.S.153-1.S2.bin
```

Note: The use of the fsum utility is for illustrative purposes only and should not be interpreted as an endorsement of the tool.

### Using Information from Cisco.com

When the MD5 hash and file size for a Cisco IOS XE Software image have been collected, network administrators can verify authenticity of the image using information provided in the Support and Downloads area on the Cisco.com website. This provides details about each publicly available IOS image and may require a valid Cisco.com account.

Network administrators must identify their Cisco IOS XE Software release (this can be done by using information obtained from output provided by the show version command) and navigate through the Downloads area to locate the image in use on the Cisco IOS XE device. Network administrators should verify that one of the following hashes matches the MD5 hash that is provided on Cisco.com:

- MD5 hash calculated by the verify /md5 command (part of the MD5 File Validation Cisco IOS XE feature)

- MD5 hash calculated by a third-party utility

If the MD5 hash value for the whole Cisco IOS XE image file does not match the MD5 hash provided by Cisco, network administrators should download the Cisco IOS XE image file from the Support and Downloads area on the Cisco.com website and use the file verification methods described in this document to verify integrity of the Cisco IOS XE image file.

The following is an example of the information provided on Cisco.com during one of the steps required for downloading Cisco IOS XE Software Release 03.08.02.S and IOSd 15.3(1)S2

Figure 1. Download Software

To facilitate automation of the verification task, Cisco has made available the checksum value of images published on cisco.com. The Bulk Hash file can be downloaded from the Trust Center Downloads page .

### Verifying Authenticity for Digitally Signed Images

Cisco IOS XE supports digitally signed images. Digitally signed Cisco software is digitally signed using secure asymmetric (public-key) cryptography.

The purpose of digitally signed Cisco software is to increase the security posture of Cisco IOS XE devices by ensuring that the software running in the system has not been tampered with and originated from a trusted source as claimed.

Administrators can display information about the authenticity of the binary file by using the show software authenticity file command. In the following example the command is used to verify the authenticity of the csr1000v-mono-universalk9.03.16.01a.S.155-3.S1a-ext.SPA.pkg on the system bootflash:

```
Router#show software authenticity file bootflash:csr1000v-mono-universalk9.03.16.01a.S.155-3.S1a-ext.SPA.pkg
File Name                     : bootflash:csr1000v-mono-universalk9.03.16.01a.S.155-3.S1a-ext.SPA.pkg
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : csr
        Organization Name     : CiscoSystems
    Certificate Serial Number : 563ACCAA
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

It is then possible to verify the signature using the verify command:

```
Router#verify csr1000v-mono-universalk9.03.16.01a.S.155-3.S1a-ext.SPA.pkg
Verifying file integrity of bootflash:csr1000v-mono-universalk9.03.16.01a.S.155-3.S1a-ext.SPA.pkg
..................................[…]………………………
Embedded Hash   SHA1 : 714554E0E6DEB3EE3B900B8616D4CD6094BE57E1
Computed Hash   SHA1 : 714554E0E6DEB3EE3B900B8616D4CD6094BE57E1
Starting image verification
Hash Computation:    100%Done!
Computed Hash   SHA2: e89c7108ea9fdac90ea6eb4a28ed4d87
                      d5d61a30cb29a4d1b33a2ec49a0e8f73
                      653e1c4add30e8f8659214c6befcede0
                      4339366eff3018baeb811971303d9fd9
                      
Embedded Hash   SHA2: e89c7108ea9fdac90ea6eb4a28ed4d87
                      d5d61a30cb29a4d1b33a2ec49a0e8f73
                      653e1c4add30e8f8659214c6befcede0
                      4339366eff3018baeb811971303d9fd9
                      
Digital signature successfully verified in file bootflash:csr1000v-mono-universalk9.03.16.01a.S.155-3.S1a-ext.SPA.pkg

Embedded hash verification successful.
```

Additional information is in Digitally Signed Cisco Software .

## Cisco IOSd Run-Time Memory Integrity Verification

### Introduction, Limitation, and Caveats

Network administrators can also verify the integrity of the run-time memory of IOSd inside Cisco IOS XE. This is not a trivial task and there is not currently a solution that would allow the network administrator to analyze all parts of memory manually. However, the best way to verify the integrity of run-time memory for IOSd is to analyze the region of memory called text .

The text section contains the actual executable code for IOSd after it is loaded in memory. As such, verifying its integrity is particularly relevant for detecting in-memory tampering. This region of memory should not change during normal Cisco IOS XE Software operation, and should be the same across reloads.

There is currently no method to verify the integrity of the other running processes, the Linux kernel, and the microcode running on the forwarding engine engine without accessing the platform shell. Administrators who need to perform forensics on another part of the system should contact their Cisco support representatives.

Cisco IOS XE releases starting from IOSd software version 15.3(2)S include multiple text sections, both for IOSd executable code and other libraries. Because of a change in the memory management implementation, it is possible that the text section that is referenced by system:memory/text may not point to the IOSd text section in memory but to a text section of a library. This means that the methods described in this section of the document cannot be applied to these releases. This issue has been resolved in Cisco IOS XE 15.5.1 and later.

Unlike Cisco IOS Software, Cisco IOS XE Software does not support a recommended method to retrieve a memory dump (also known as core dump). This means that it is not currently possible to analyze the run-time memory by extracting the text section from the core dump.

Note: The absence of indicators of compromise using the methods presented in this section may not guarantee that the Cisco IOS XE device was not compromised.

### Text Memory Section Export

One way to verify the integrity of the text section is by exporting the section using the copy command and then calculating the hash of the file.

Depending on the Cisco IOS XE release, the copy command can copy files stored in the Cisco IOS XE file system to an external server via several protocols, including FTP and Secure Copy Protocol (SCP). The following example shows how to copy the text memory section via FTP.

Configure the FTP username and password if it has not been done already:

```
ip  ftp username <user>
ip  ftp password <pass>
```

Use the dir command to locate the text region. This is usually in the system:/memory directory. The following example shows the output of dir system:/memory :

```
Router#dir system:memory      
Directory of system:/memory/
    7  -r--    29585392                    <no date>  bss
    6  -r--    74029984                    <no date>  data
    9  -r--  1168212400                    <no date>  heap
    8  -r--     6295128                    <no date>  lsmpi_mem
   10  -r--      172032                    <no date>  stack 5  -r--   130602790              	   <no date>  text No space information available
```

Export the text region by using the copy command:

```
router# copy system:memory/text ftp: Address or name of remote host []? <FTP server ip  address>
Destination filename [text]? asr1k_main_text
Writing router_main_text !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
<output suppressed>
```

After the file has been exported, use any utility to calculate the MD5 checksum, for example md5sum:

```
$ md5sum asr1k_main_text 
ffe7bea1a10f06da017f526167bbe7e1 asr1k_main_text
```

This method implies trust in the copy process, which may itself be compromised.

This value should be compared with the value obtained by the procedure described in the following section, "Compute the MD5 Checksum of a Known-Good Text Section."

Compute the MD5 Checksum of a Known-Good Text Section

A known-good text region is a file that contains the main:text that it is known not to be compromised and that can be used as a reference point during the forensic operation. This section proposes the procedure that can be used to create a known-good text region.

- Download the Cisco IOS XE image from the Cisco Support and Downloads website and note the MD5 value of the binary.

- Use the method described in the Using Offline Image File Hashes section of this document to verify that the MD5 hash of the image downloaded matches the one on the Cisco Support and Downloads website. We will call this the "known-good image."

- Load the known-good image on a Cisco IOS XE device.

- Reload the device.

- After reload, use the method described in the Using the Message Digest 5 File Validation Feature section of this document to verify the integrity of the image that has been booted. We will call this "known-good device." The main:text memory region of this device will be called the known-good text region.

- Use the method described in Verify MD5 Validation Feature for the Text Region to calculate the MD5 hash value of the main:text region. This is what we call the "MD5 hash of a known-good text region."

### Verify MD5 Validation Feature for the Text Region

Network administrators can use the verify /md5 command to compute the MD5 checksum of the text region without creating a memory dump. The text region is usually located in the system:/memory directory.

Use the dir command to locate the text region. This is usually in the system:/memory directory. The following example shows the output of dir system:/memory :

```
Router#dir system:memory      
Directory of system:/memory/
    7  -r--    29585392                    <no date>  bss
    6  -r--    74029984                    <no date>  data
    9  -r--  1168212400                    <no date>  heap
    8  -r--     6295128                    <no date>  lsmpi_mem
   10  -r--      172032                    <no date>  stack 5  -r--   130602790                    <no date>  text No space information available
```

Use the verify /md5 command to calculate the MD5 checksum of the text region:

```
router#verify /md5 system:memory/text .......................................................................
[...] 
.....................................Done!
verify /md5 (system:memory/text) = ffe7bea1a10f06da017f526167bbe7e1
```

This value should be compared with the value obtained by the procedure described in Compute the MD5 Checksum of a Known-Good Text Section .

This method implies trust in the onboard verify /md5 command, which may itself be compromised.

Since release 16.5.1, the SHA-512 algorithm is also supported in the verify command by using /sha512 instead of /md5 .

## Additional Indicators of Compromise

In addition to verifying the integrity of the run-time memory, network administrators can check external logs and logs stored on the Cisco IOS XE device itself for the presence of "unusual" commands.

### Unusual and Suspicious Commands

The presence of the following commands should trigger further investigation. The asterisk symbol * indicates any text that follows the command itself.

- test *

- tclsh *

- service internal

- config-register *

- boot *

- attach *

- hw-module *

- platform shell

- request *

- show region

- show memory *

- show platform *

- do-exec version of any of the above

Note: Cisco IOS XE allows command abbreviation. For example, typing se in instead of service internal will still configure service internal on a device. When checking the logs, abbreviation of commands such as tes , rem , and se in should also be considered.

### Checking That IOSd Call Stacks Are Within the Text Section Boundaries

During normal operation Cisco IOS XE processes should have the Program Counter (PC) and Return Address (RA) within the boundary of the text section.

If this is not the case, the events should be further investigated.

In order to verify that the PC and RA are within the text section boundaries, use the show stack <pid> command where the Process ID (PID) can be obtained for example using the show process command. The following example shows how to display the pid of the process running on the Cisco IOS XE device and how to use the show stack command:

```
Router#show process
CPU utilization for five seconds: 0%/0%; one minute: 0%; five minutes: 1%
 PID QTy       PC Runtime (ms)    Invoked   uSecs    Stacks TTY Process
   1 Cwe  39CDDEA            3         21     14222776/24000  0 Chunk Manager   
   2 Csp  6D00678           31        104     29811152/12000  0 Load Meter      
   3 Mwe  6CCDAAB            0          1       023432/24000  0 T3E3-SPA backgro
   4 Mwe  4E179E5            0         11       023408/24000  0 Retransmission o
   5 Mwe  4E15574            0          3       022232/24000  0 IPC ISSU Dispatc
   6 Mwe  3D1AC86            5         12     41620600/24000  0 RF Slave Main Th
   7 Mwe  6EC0E15            0          1       094496/96000  0 EDDRI_MAIN      
   8 Mwe  39726B5            0          1       023640/24000  0 RO Notify Timers [...]
```

Administrators should use the show stack command to display information about the PC or RA (depending on the software version and model, the output may include information about PC or RA), for each processes displayed with the show process command.

The following example shows the PC information by the use of show stack for PID 5, which identifies the IPC ISSU Dispatch process:

```
Router#show stack 5
Process 5:  IPC ISSU Dispatch Process
  Stack segment 0x7F8BDD7DC000 - 0x7F8BDD7E1DC0
	PC: 0x41FD621 , RSP: 0x7F8BDD7E1CD0
	PC: 0x3A02D79 , RSP: 0x7F8BDD7E1D00
	PC: 0x4E15574 , RSP: 0x7F8BDD7E1DB0
```

Once the information about PC or RA is available, administrator should verify that the memory addresses fall into the text region boundaries. The text section boundaries can be displayed by using the show region command:

```
Router# show region
Region Manager:
      Start         End     Size(b)  Class  Media  Name 0x00554C90  0x081E23B5   130602790  IText  R/W    text 0x0C990240  0x11029DDF    74029984  IData  R/W    data
 0x11029DE0  0x12C60DCF    29585392  IBss   R/W    bss
 0x7F8BDCA531A8  0x7F8BDD053FFF     6295128  Iomem  R/W    lsmpi_mem
 0x7F8BDD25C010  0x7F8C22C741BF  1168212400  Local  R/W    heap
 0x7FFF157A3000  0x7FFF157CCFFF      172032  Local  R/W    stack
Free Region Manager:
      Start         End     Size(b)  Class  Media  Name
```

In this case, all PC addresses 0x41FD621, 0x3A02D79, and 0x4E15574 are within the text section boundaries, that is between 0x00554C90 and 0x081E23B5.

### Checking the Command History

Network administrators can use the show history all command to access command history records. The following example shows how to search for the presence of the service internal command in the history buffer:

```
router#show history all | include se
CMD: 'service internal' 18:28:54 UTC Wed Jun 18 2014
CMD: 'show history all | i se' 18:36:09 UTC Wed Jun 18 2014
```

The command history can be used to check whether some of the suspicious commands, for example the ones listed in Unusual and Suspicious Commands , have been run on a router, which would be an indication of compromise.

### Checking Platform Shell Access Logs and Syslog

As explained in the previous sections, Cisco IOS XE provides to device administrator the possibility to access the Linux shell by using the platform shell , request platform software shell , or request system shell commands depending on the platform. Access to platform shell is there to facilitate troubleshooting activity from Cisco TAC or other Cisco personnel and normally should not be used by the device administrator.

It is very important that access to the Linux shell is tightly controlled. An unauthorized access to the Linux shell is an unwanted event and should be further investigated.

When the platform shell is accessed, syslogs are generated to log this event. The following example shows the syslog generated upon accessing the platform shell:

```
*Jun 18 19:06:34.630: %IOSXE-5-PLATFORM: SIP0: %SYSTEM-3-SYSTEM_SHELL_LOG: Shell ended: con 0
*Jun 18 19:06:34.670: %IOSXE-5-PLATFORM: SIP0: %SYSTEM-3-SYSTEM_SHELL_LOG: Log: harddisk:tracelogs/system_shell_R0.log.20140618190625
*Jun 18 19:06:34.678: %IOSXE-5-PLATFORM: SIP0: %SYSTEM-3-SYSTEM_SHELL_LOG: (fingerprint: 6346d70a3e4928fbb8375e85e8c8983c)
```

In addition to the syslog, a log file is created in the tracelogs directory in the filesystem. The log file usually starts with system_shell*. Administrators should review these logs as they may indicate a compromise of the system. The following example shows how to access these logs:

```
Router#cd tracelogs
Router#dir | include system_shell
843706  -rw-         529  Jun 18 2014 19:19:01 +00:00  system_shell_R0.log.20140618191728
843699  -rw-         161  Jun 18 2014 19:06:34 +00:00  system_shell_R0.log.20140618190625
```

### Checking External Accounting Logs

Cisco IOS XE can be configured to send accounting information for exec and configuration commands to an external server via the TACACS+ protocol as explained in the Security Best Practices section. Commands can be used to check whether some of the suspicious commands, for example the ones listed in the Unusual and Suspicious Commands section, have been run on a router, which would be an indication of compromise.

### Checking External Syslog Logs

Cisco IOS XE Software can be configured to send syslog information to an external syslog server. Currently Cisco IOS XE Software will not send commands executed via the console or vty to the syslog server. Network administrators should check the logs for unusual connections or connection attempts to the Cisco IOS XE devices via vty, console, or other available methods.

### Checking Booting Information

Information about the last time the Cisco IOS XE device was reloaded and the reason may provide additional insight about a possible compromise. For example, an unscheduled reload should raise attention and be investigated further.

Network administrators can use the show version command to see information about uptime, last reload cause, and which file was used to boot the Cisco IOS. The following is an example of show version output:

Important information in order of appearance in the output is:

- Router uptime: This information indicates how long the router has been up. This information can be correlated with change management logs to see whether a reload was authorized and expected.

- Image booted: This field provides information about which file was used to boot the Cisco IOS XE device. Administrators are advised to ensure that the filename matches the Cisco IOS XE image they intended to boot.

- Configuration register: This value is used to indicate how the router should boot. The default value is 0x2102 and should not be modified under normal circumstances. Modification of this value may indicate an attempt to change the correct boot sequence. Additional information is in Use of the Configuration Register on All Cisco Routers .

```
Router#show version
Cisco IOS Software, IOS-XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 15.3(1)S2, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Tue 30-Apr-13 22:28 by mcpre
IOS XE Version: 03.08.02.S
Cisco IOS-XE software, Copyright (c) 2005-2013 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.
ROM: IOS-XE ROMMON
Router uptime is 11 minutes Uptime for this control processor is 12 minutes System returned to ROM by reload
System image file is "bootflash:asr1001-universalk9.03.08.02.S.153-1.S2.bin" Last reload reason: Reload Command
This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.
A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html
If you require further assistance please contact us by sending email to
export@cisco.com.
License Level: adventerprise
License Type: RightToUse
Next reload license Level: adventerprise
cisco ASR1001 (1RU) processor with 1141000K/6147K bytes of memory.
Processor board ID SSI15240FEC
4 Gigabit Ethernet interfaces
32768K bytes of non-volatile configuration memory.
4194304K bytes of physical memory.
7782399K bytes of eUSB flash at bootflash:. Configuration register is 0x2102
```

### Checking the ROM Monitor Information

The ROM monitor is a bootstrap program that initializes the hardware and boots the Cisco IOS XE Software.

Because the ROM monitor settings are persistent, information about the ROM monitor variable values could indicate an attempt to influence the Cisco IOS XE boot sequence. Administrators can use the set command while in the ROM monitor prompt to see the value of the ROM monitor variables.

Note: Entering the ROM monitor prompt will require a reload of the Cisco IOS XE device.

The output of the set command may differ depending on the platform and Cisco IOS XE release; however, administrators should ensure that the following conditions are met:

- The BOOT variable is set, reflecting the image file that should be used to boot Cisco IOS XE Software

- REAL_MGMTE_DEV

- DEBUG_CONF

- ROMMON_DEBUG_CONF

- BOOT_PARAM

- SR_NVRAM_PATH

- SR_MGMT_VRF

- STBY_CONS_EN

The following example shows the output of the set command:

```
rommon 1 > set
PS1=rommon ! > 
MCP_STARTUP_TRACEFLAGS=00000000:00000000
IOSXE_DUAL_IOS=0
LICENSE_BOOT_LEVEL=adventerprise,all:asr1001;
EULA_ACCEPTED=TRUE
NITROX_FAIL=0
BOOT=bootflash:asr1001-universalk9.03.08.02.S.153-1.S2.bin,12;
RET_2_RTS=
?=1
BSI=0
RANDOM_NUM=1014685630
RET_2_RCALTS=1403618345
```

# Security Best Practices

## Maintain Cisco IOS XE Image File Integrity

To minimize the risk associated with malicious code, it is important that network administrators develop and consistently apply a secure methodology for Cisco IOS XE Software image management. This secure process must be used from the time a Cisco IOS XE Software image is downloaded from Cisco.com until a Cisco IOS XE device begins using it.

Although processes may vary based on the network and its security and change management requirements, the following procedure represents an example of best practices that may help minimize the possibility of malicious code installation.

- When downloading a Cisco IOS XE Software image from www.cisco.com, record the MD5 hash as presented by the Cisco IOS XE Upgrade Planner tool.

- After the image has been downloaded to an administrative workstation, the MD5 hash of the local file should be verified against the hash presented by the Cisco IOS XE Upgrade Planner.

- After the Cisco IOS XE Software image file has been verified as authentic and unaltered, copy it to write-once media or media that can be rendered as read-only after the image has been written.

- Verify the MD5 hash of the file written to the read-only media to detect corruption during the copy process.

- Remove the local file on the administrative workstation.

- Relocate the read-only media to the file server that is used for Cisco IOS XE Software image distribution to Cisco IOS XE devices.

- Transfer the Cisco IOS XE Software image from the file server to the Cisco IOS XE device using a secure protocol that provides both authentication and encryption.

- Verify the MD5 hash of the Cisco IOS XE Software image on the Cisco IOS XE device using any of the procedures detailed in the Cisco IOS XE Image File Verification section of this document.

- Modify the configuration of the Cisco IOS XE device to load the new Cisco IOS XE Software image upon startup.

- Reload the Cisco IOS XE device to place the new software into service.

## Implement Change Control

Change control is a mechanism through which network device changes are requested, approved, implemented, and audited. Change control is a great help in determining which changes have been authorized and which are unauthorized. Change control is important to help ensure that only authorized and unaltered Cisco IOS XE Software is used on Cisco IOS XE devices in the network.

## Harden the Software Distribution Server

The server that is used to distribute software to Cisco IOS XE devices in the network is a critical component of network security. Several best practices should be implemented to help ensure the authenticity and integrity of software that is distributed from this server. These best practices include the following:

- Application of well-established operating system hardening procedures that are specific to the operating system in use

- Configuration of all appropriate logging and auditing capabilities, including logging to write-once media

- Placement of the software distribution server on a secure network with restricted connectivity from all but the most trusted networks

- The use of restrictive security controls to limit interactive access (as an example, SSH) to only a subset of trusted network administrators

## Keep Cisco IOS XE Software Updated

Cisco IOS XE Software used in the network must be kept up to date so that new security functionality can be used and exposure to known vulnerabilities disclosed through Cisco Security Advisories is minimal.

Cisco is continually evolving the security of Cisco IOS XE Software images through the implementation of new security functionality and the resolution of bugs. For these reasons, it is imperative that network administrators maintain their networks in a manner that includes using up-to-date software. Failure to do so could expose vulnerabilities that may be used to gain unauthorized access to a Cisco IOS XE device.

Cisco transparently communicates vulnerabilities found in all Cisco products according to the Cisco Security Vulnerability Policy .

## Deploy Digitally Signed Cisco IOS XE Images

Digitally signed Cisco software is digitally signed using secure asymmetrical (public-key) cryptography.

The purpose of digitally signed Cisco software is to increase the security posture of Cisco IOS XE devices by ensuring that the software running in the system has not been tampered with and originated from a trusted source as claimed.

For additional information, see Digitally Signed Cisco Software .

## Cisco Secure Boot

Cisco Secure Boot is a secure startup process that your Cisco device performs each time it boots up. Beginning with the initial power-on, a special purpose hardware device, known as the Trust Anchor module, verifies the integrity of the ROMMON code and the IOS image via digital signatures as they each are loaded. If any failures are detected, the user is notified of the error and the device will wait for the operator to correct the error. This prevents your network device from executing tainted network software.

For additional information see Trust Anchor Technology .

## Cisco Value Chain Security

Cisco's Value Chain Security program focuses on counterfeit products, tainted products, and misuse of intellectual property. Just as important as physical security, maintaining a chain of custody from manufacturing through installation and provisioning is vital to a trustworthy network. There are many avenues to introduce malware or fraudulent hardware into network devices, and Cisco's Value Chain Security program ensures that devices delivered with the Cisco Systems name are authentic and unmodified.

While this program will help ensure the authenticity of the Cisco hardware, administrators should make sure they have tight control on the delivery of new or refurbished equipment after it has arrived on the premises.

For additional information, see Cisco Value Chain Security .

## Use Authentication, Authorization, and Accounting

The comprehensive implementation of Authentication, Authorization, and Accounting (AAA) is critical to ensuring the security of interactive access to network devices. Furthermore, AAA (specifically the authorization and accounting functions) should be used to limit the actions that authenticated users can perform and provide an audit trail of individual user actions.

The following example shows the necessary configuration to send accounting information to an external AAA server. Note that Cisco also recommends configuration of authentication and authorization together with accounting.

```
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 0 default start-stop group  tacacs+
aaa accounting commands 1 default start-stop group  tacacs+
aaa accounting commands 15 default start-stop group  tacacs+
```

For additional information about the implementation of AAA, see the Using Authentication, Authorization, and Accounting section of Cisco Guide to Harden Cisco IOS Devices .

## Use TACACS+ Authorization to Restrict Commands

Command authorization via TACACS+ should be enforced to keep tight control over commands that network administrators should not use without specific reasons. This can be accomplished by configuring authentication and command authorization via TACACS+.

The following example shows how to configure a Cisco IOS XE device for TACACS+ authentication, command authorization, and command accounting:

```
aaa new-model
aaa authentication login default group tacacs+ local  enable
aaa authentication enable default group tacacs+  enable
aaa authorization config-commands 
aaa authorization exec default group tacacs+ local  if-authenticated  
aaa authorization commands 1 default group tacacs+  local if-authenticated  
aaa authorization commands 15 default group tacacs+  local if-authenticated  
aaa accounting exec default start-stop group tacacs+ 
aaa accounting commands 0 default start-stop group  tacacs+ 
aaa accounting commands 1 default start-stop group  tacacs+ 
aaa accounting commands 15 default start-stop group  tacacs+ 
aaa session-id common
```

When authorization is in place, the following commands should be restricted or prohibited by configuring the external AAA server. The following commands are particularly relevant to help ensure that the Cisco IOS XE Software run-time memory and boot sequence are not modified:

- gdb *

- test *

- tclsh *

- service internal

- config-register *

- boot *

The following commands may be used to connect to line cards or switch processors on products that support them. They are particularly important because after the Cisco IOS XE device is connected to a line card or switch processor, the commands executed are not logged or authorized using the AAA server.

- attach *

- hw-module *

The following command can be used to connect to the Linux shell of the Cisco IOS XE. Controlling the access to platform shell is critical to avoid software modification and malware implants.

- platform shell

- request *

The following commands may be used to show a particular state of the system. They are important because they can be used during a reconnaissance attack to study the system and prepare an attack using other commands:

- show platform *

- show region

- show memory *

Cisco IOS XE Software allows the use of the do-exec <command> in configuration mode. It is important that policies for authentication, command authorization, and command accounting take this feature into account by restricting or prohibiting any of the commands detailed in this section even when they are preceded by the do-exec command (for example, do-exec test * ).

## Implement Credentials Management

Passwords control access to resources or devices. A password or secret is defined and used to authenticate requests. When a request is received for access to a resource or device, the request is challenged for verification of the password and identity, and access can be granted, denied, or limited based on the result.

As a security best practice, passwords should be managed with a TACACS+ or RADIUS authentication server. However, a locally configured password for privileged access is still needed in the event of a failure of the TACACS+ or RADIUS services. A device can also have other password information in its configuration, such as an NTP key, Simple Network Management Protocol (SNMP) community string, or routing protocol key.

The enable secret command is used to set the password that grants privileged administrative access to the Cisco IOS XE system. The enable secret command must be used, rather than the older enable password command. The enable password command uses a weak encryption algorithm.

If no enable secret is set and a password is configured for the console line, the console password can be used to receive privileged access, even from a remote vty session. This action is almost certainly unwanted and is another reason to ensure configuration of an enable secret.

The service password-encryption global configuration command directs Cisco IOS XE Software to encrypt the passwords, Challenge Handshake Authentication Protocol (CHAP) secrets, and similar data that are saved in its configuration file. Such encryption is useful to prevent casual observers from reading passwords, such as when they look at the screen over the shoulder of an administrator. However, the algorithm used by the service password-encryption command is a simple Vigenère cipher. The algorithm is not designed to protect configuration files against serious analysis by even slightly sophisticated attackers and must not be used for this purpose. Any Cisco IOS XE configuration file that contains encrypted passwords must be treated with the same care that is used for a cleartext list of those same passwords.

Although this weak encryption algorithm is not used by the enable secret command, it is used by the enable password global configuration command, as well as the password line configuration command. Passwords of this type must be eliminated and the enable secret command or the Enhanced Password Security feature needs to be used.

The enable secret command and the Enhanced Password Security feature use salted MD5 for password hashing. This algorithm has had considerable public review and is not known to be reversible. However, the algorithm is subject to dictionary attacks. In a dictionary attack, an attacker tries every word in a dictionary or other list of candidate passwords to find a match. Therefore, configuration files must be securely stored and only shared with trusted individuals.

Particular care should be taken in protecting network administrator credentials from theft because privileged access to the Cisco IOS XE device may be used to compromise the integrity of the memory, compromise the confidentiality of the data and configuration, and affect operations.

## Implement Configuration Controls

Configuration management is a process by which configuration changes are proposed, reviewed, approved, and deployed. In the context of a Cisco IOS XE device configuration, two additional aspects of configuration management are critical: configuration archives and security.

You can use configuration archives to roll back changes that are made to network devices. In a security context, configuration archives can also be used to determine which security changes were made and when these changes occurred. In conjunction with AAA log data, this information can assist in the security auditing of network devices.

The configuration of a Cisco IOS XE device contains many sensitive details. Usernames, passwords, and the contents of access control lists are examples of this type of information. The repository that you use to archive Cisco IOS XE device configurations needs to be secured. Insecure access to this information can undermine the security of the entire network.

Additional information is in the Cisco IOS Software Configuration Management section of Cisco Guide to Harden Cisco IOS Devices .

## Protect Interactive Access to Devices

After AAA has been implemented to control which users can log in to particular network devices, access control should be implemented to limit IP addresses from which users may perform management functions on a network device. This access control includes multiple security features and solutions to limit access to a device:

- VTY access classes

- Management Plane Protection (MPP)

- Control Plane Policing (CoPP)

- Control Plane Protection (CPPr)

- Infrastructure access control lists (iACL)

- SNMP access lists

For more information, see the following sections of Cisco Guide to Harden Cisco IOS Devices : Secure Interactive Management Sessions and Fortify the Simple Network Management Protocol .

Many protocols carry sensitive network management data. You must use secure protocols whenever possible. A secure protocol choice includes the use of SSH instead of Telnet so that both authentication data and management information are encrypted. In addition, you must use secure file transfer protocols when you copy configuration data. An example is the use of SCP in place of FTP or TFTP.

See the Secure Interactive Management Sessions section of Cisco Guide to Harden Cisco IOS Devices for more information about the secure management of Cisco IOS XE devices.

## Gain Traffic Visibility with NetFlow

NetFlow enables you to monitor traffic flows in the network. Originally intended to export traffic information to network management applications, NetFlow can also be used to show flow information on a router. This capability allows you to see what traffic traverses the network in real time. Regardless of whether flow information is exported to a remote collector, you are advised to configure network devices for NetFlow so that it can be used reactively if needed.

More information about this feature and how to use NetFlow to identify a possibly compromised device or network are in the Traffic Identification and Traceback section of Cisco Guide to Harden Cisco IOS Devices and in Telemetry-Based Infrastructure Device Integrity Monitoring .

## Use Centralized and Comprehensive Logging

For network administrators to understand events taking place on a network, a comprehensive logging structure using centralized log collection and correlation must be implemented. Additionally, a standardized logging and time configuration must be deployed on all network devices to facilitate accurate logging. Furthermore, logging from the AAA functions in the network should be included in the centralized logging implementation.

After comprehensive logging is in place on a network, the collected data must be used to monitor network activity for events that may indicate unauthorized access to a network device or unauthorized actions by legitimate users. These types of events could represent the first step in undermining the security on a Cisco IOS XE device. Because the following items may represent unauthorized access or unauthorized actions, they should be monitored closely:

- The transmission of Cisco IOS XE Software images to a Cisco IOS XE device using the copy command or local SCP, TFTP, or FTP server functionality.

- The attempted execution of certain high-risk EXEC commands. The copy , gdb , more , configure , tclsh, test, and request platform commands are some examples of commands that should be monitored. This list is not exhaustive.

- Modification of the boot environment in use on the network devices. This specifically includes the boot and config-register global configuration commands.

- Modification of the security configuration for a Cisco IOS XE device. This may include the removal of VTY access classes or the logging configuration or the addition of new administrative users.

- Logging related to the insertion or removal of storage media, such as flash devices.

- SNMP-related logging of attempts to modify the Cisco IOS XE device configuration or perform file management tasks.

- The planned and unplanned reload of the Cisco IOS XE Software due to a software crash or the use of the reload command.

For more information, see the Centralize Log Collection and Monitoring and Logging Best Practices sections of Cisco Guide to Harden Cisco IOS Devices .

# Conclusion

In conclusion, as interest in Cisco IOS XE Software integrity assurance is growing, this document presented various methods for an administrator to assess the integrity of the software running on the Cisco IOS XE device. These include image and IOSd memory verification, command checks, boot history checks, and more. Most attackers targeting Cisco IOS XE router software would, in theory, use stolen administrator credentials, use hidden commands, compromise images, or exploit vulnerabilities. These techniques can usually be prevented by implementing common recommendations and best practices that are published by Cisco and summarized in this document. Command authorization and accounting, logging, credential management, image signing, vulnerability control, and device hardening are some of the most important practices that will not only prevent Cisco IOS XE Software modification in nearly all cases, but will also ensure good security policy.

# Acknowledgments

Authors:

Stefano De Crescenzo (sdecresc[at]cisco[dot]com) is a member of the PSIRT team in the Security Intelligence Operations organization.

Xavier Brouckaert (xabrouck[at]cisco[dot]com) is a member of the PSIRT team in the Security Intelligence Operations organization.

# References

Cisco Guide to Harden Cisco IOS Devices //www.cisco.com/c/en/us/support/docs/ip/access-lists/13608-21.html

Cisco IOS Image Verification //www.cisco.com/web/about/security/intelligence/iosimage.html

Offline Analysis of IOS Image Integrity Blog http://blogs.cisco.com/security/offline-analysis-of-ios-image-integrity/

Securing Tool Command Language on Cisco IOS //www.cisco.com/web/about/security/intelligence/securetcl.html

Cisco Security Vulnerability Policy //www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html

Use of the Configuration Register on All Cisco Routers //www.cisco.com/c/en/us/support/docs/routers/10000-series-routers/50421-config-register-use.html

Digitally Signed Cisco Software //www.cisco.com/c/en/us/td/docs/ios-xml/ios/sys-image-mgmt/configuration/xe-3s/asr1000/sysimgmgmt-xe-3s-asr1000-book/sysimgmgmt-dgtly-sgnd-sw.html

Cisco IOS XE Configuration Guides //www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xe-3s/products-installation-and-configuration-guides-list.html

MD5 File Validation //www.cisco.com/c/en/us/td/docs/ios-xml/ios/sys-image-mgmt/configuration/15-mt/sysimgmgmt-15-mt-book/sysimgmgmt-md5.html

Image Verification //www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_cfg/configuration/xe-3s/sec-usr-cfg-xe-3s-book/sec-image-verifctn.html

Telemetry-Based Infrastructure Device Integrity Monitoring http://www.cisco.com/web/about/security/intelligence/network-integrity-monitoring.html

# Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Attack Vector | Privileges Required | Recommended Best Practices |
|---|---|---|
| Code injection in run time via IOS commands | Administrative privileges | Use Authentication, Authorization, and Accounting Use TACACS+ Authorization to Restrict Commands Implement Credentials Management Implement Configuration Controls |
| Modified binary image | Administrative privileges | Use Cisco Secure Boot Deploy Digitally Signed Cisco IOS Images Maintain Cisco IOS Image File Integrity Implement Change Control Harden the Software Distribution Server Implement Credentials Management Protect Interactive Access to Devices |
| Modified ROMMON image | Administrative privileges | Use Cisco Secure Boot Deploy Digitally Signed Cisco IOS Images Implement Change Control Harden the Software Distribution Server Implement Credentials Management Protect Interactive Access to Devices |
| Hardware modification | Physical access to the device | Cisco Value Chain Security |
| Vulnerabilities that could cause writing in memory | Varies according to the vulnerability | Keep Cisco IOS Software Updated |

| Date | Description |
|---|---|
| September 5, 2018 | Moved content to a new URL. |
| February 6, 2018 | Corrected information about ASLR and provided a general refresh. |
| November 6, 2014 | Removed RADIUS from "Checking External Accounting Logs." |
| July 17, 2014 | Added hw-module * to two command lists. Changed to show software authenticity file in text to match code. |
| July 7, 2014 | Initial public release. |