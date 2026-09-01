---
doc_id: sec-cloudapps-cisco-com-security-center-resources-asa-integrity-assurance-html-dd528866a5
source_url: https://sec.cloudapps.cisco.com/security/center/resources/asa_integrity_assurance.html
retrieved_at: 2026-09-01T14:11:15.118408+00:00
---

Home / Cisco Security

ASA Integrity Assurance

# ASA Integrity Assurance

### Contents

Introduction Potential Attack Methods Manipulating Cisco ASA Software Images Vulnerabilities Identification Techniques Cisco ASA Image File Verification Using the Hash File Validation Feature Using Offline Image File Hashes Using Information from Cisco.com Secure Software Publishing - Bulk Hash File Download Center Verifying Authenticity for Digitally Signed Images Cisco ASA Runtime Memory Integrity Verification Core Dump Creating a Known-Good Text Region Additional Indicators Checking External Accounting Logs Checking External Syslog Logs Checking Booting Information Checking the ROM Monitor Information Checking Failover Events Checking the SSL VPN Portal Code Checking the Integrity of SSL VPN Plugins Checking the Configuration Checksum Verify the Integrity of Other Software Loaded on the Cisco ASA Device Security Best Practices Maintain Cisco ASA Image File Integrity Implement Change Control Harden the Software Distribution Server Keep Cisco ASA Software Updated Deploy Digitally Signed Cisco ASA Images Cisco Secure Boot Cisco Supply Chain Security Leverage the Latest Cisco ASA Security Protection Features Use Authentication, Authorization, and Accounting Use TACACS+ Authorization to Restrict Commands Implement Credential Management Securing Interactive Management Sessions Gain Traffic Visibility with NetFlow Use Centralized and Comprehensive Logging Conclusion Acknowledgments References Revision History

# Introduction

This document describes ways to verify that the software on a Cisco firewall running Cisco Adaptive Security Appliance (ASA) Software, both in device storage and in running memory, has not been modified. Additionally, the document presents common best practices that can aid in protecting against attempts to inject malicious software (also referred to as malware) in a device running Cisco ASA Software. This document applies only to Cisco ASA Software and to no other Cisco operating systems. This document does not apply to any of the service modules running within the Cisco ASA device.

In the past, attackers were primarily targeting infrastructure devices to create a denial of service (DoS) situation. While these types of attacks still represent the majority of attacks on network devices, attackers are now looking for ways to subvert the normal behavior of infrastructure devices due to the devices' privileged position within the IT infrastructure.

In fact, by compromising an infrastructure device such as a firewall, the attacker may gain a privileged position and the ability to access data flows or cryptographic materials, change security access policies, or perform additional attacks against the rest of the infrastructure.

Malicious software is software created to modify the behavior of a device for the benefit of a malicious third-party (attacker). One of the characteristics of effective malicious software is that it can run on a device undetected in privileged mode. Malicious software is usually designed to monitor and exfiltrate information from the operating system on which it is running, without being detected. Potentially, sophisticated malicious software running on Cisco ASA Software could attempt to hide its presence by modifying Cisco ASA command output that would normally reveal information about the presence of the malicious software.

An additional property of malicious software is the capability to send and receive information from a command-and-control (C&C) server. Methods to identify possibly compromised infrastructure devices using telemetry data are discussed in the Telemetry-Based Infrastructure Device Integrity Monitoring white paper.

In general, malicious software can be installed using various methods, typically by exploiting vulnerabilities on the system or by manipulating an authorized user via a number of social engineering attacks.

On Cisco devices running Cisco ASA Software, a limited number of infection methods are available to malicious software. Malicious software may be introduced into Cisco ASA Software in the following ways:

- Altering the ASA software image stored on the onboard device file system

- Tampering with Cisco ASA memory during runtime

- Obtaining access to the Cisco ASA Linux Operating System and installing a rootkit

- Modifying the BIOS firmware

- Using a combination of some or all the preceding mechanisms

# Potential Attack Methods

Attackers will try to use one of the methods described in this section to install malicious software in Cisco ASA Software.

Some models of Cisco ASA firewalls implement several techniques, including the use of safe coding practices, digital signing, and secure boot, to help protect against memory and code manipulation and provide assurances of authenticity.

Administrators should verify their hardware and software supports these features to ensure protection of the integrity of the device.

However, these technologies will not protect Cisco ASA Software from unauthorized access due to compromised credentials. It is therefore important that administrators protect the credentials of privileged accounts (for example, privilege 15) with appropriate controls and by implementing credentials management policies.

Note that an attacker with administrative, remote, or local access to a device, be it a Cisco device or one from any other vendor, can perform activities that may be dangerous or disruptive. Given the state of the current Cisco ASA integrity protection technology, attacks will often exploit inadequacies in secure configuration and network design, likely by trying to obtain administrative access.

## Manipulating Cisco ASA Software Images

It is possible that an attacker could modify a valid Cisco ASA Software image by adding malicious code and loading it onto a Cisco device that supports the modified image. This attack scenario applies to any computing device that loads its operating system from a writable device. There are image verification techniques that could prevent the firewall from loading such an image, as discussed in the Cisco ASA Software Image File Verification section of this document.

## Vulnerabilities

In Cisco ASA Software, as with any operating system, there is a possibility that a vulnerability could allow the execution of malicious code. In such a scenario, an attacker who exploited the vulnerability would install or run malicious code on Cisco ASA Software, which could then be used to take malicious action, such as modifying device behaviors or exfiltrating information. The Cisco Product Security Incident Response Team (PSIRT) manages and discloses all vulnerabilities and fixes for Cisco products. Any vulnerability that Cisco is made aware of is investigated and disclosed in accordance with the Cisco vulnerability disclosure policy .

# Identification Techniques

This section describes methods that can identify the modification of Cisco ASA Software image files and runtime memory. The absence of any indicators of compromise, when using these methods, may not guarantee that the Cisco ASA Software device is free from compromise. Readers should note that when facing potential exploitation, the chain of custody becomes important. Administrators need to be aware of the chain of custody through all forensic activities, including those presented below, because an exploit could alter specific forensic outputs that would further affect the forensic analysis.

Note: The examples in this document, unless otherwise noted, are taken from a Cisco ASA 5515-X running Cisco ASA Software 9.1(5). The output on your device may differ based on device model, operating system release, and feature set. In addition, the commands in this document may use a different syntax, or they may not be present at all. The Cisco recommendation is to follow up with your support organization if you need details about implementing these recommendations for a specific combination of device model, Cisco ASA Software release, and feature set.

## Cisco ASA Image File Verification

Network administrators can use one of several security features to verify the authenticity and integrity of Cisco ASA Software images in use on their ASA network devices. It is also possible to use a process that does not rely on features in Cisco ASA Software. Verifying the hash of Cisco ASA images by using the more thorough offline process described below is an important option, as it does not rely on the output of a potentially compromised device.

The following sections contain information about Cisco ASA Software features and administrative processes that can be used to verify the authenticity and integrity of a Cisco ASA Software image.

### Using the Hash File Validation Feature

The Hash File Validation feature allows network administrators to calculate the MD5 or the SHA-512 hash of a Cisco ASA Software image file that is loaded on a device's storage medium. The resulting hash is then compared against the hash provided by Cisco to verify the integrity of the image file. The comparison can be done by the Hash File Validation feature on the device, or the administrator can compare the two hashes, to ensure they match.

The trusted software hash values can be obtained from the Cisco Software download section of Cisco.com.

Note: The Hash File Validation feature can be used only to check the integrity of a Cisco ASA Software image that is stored on a Cisco ASA device. It cannot be used to check the integrity of an image running in memory.

The hash calculation and verification using the Hash File Validation feature can be accomplished using the verify command followed by the hashing algorithm to use. Currently Cisco ASA Software supports MD5 and SHA-512. The following example shows the syntax of the command:

```
verify [/md5|/sha-512] filesystem:filename [md5-hash|sha-512-hash]
```

Network administrators can use the verify /md5 or /sha-512 privileged EXEC command to verify the integrity of image files that are stored on the Cisco ASA file system of a device. The following example shows how to use the verify /sha-512 command on a Cisco ASA device:

```
ciscoasa# verify /sha-512 asa915-smp-k8.bin .....<output truncated>.....Done! verify /SHA-512 (disk0:/asa915-smp-k8.bin) = 4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19
```

Network administrators can also provide an MD5 or SHA-512 hash to the verify command. If the hash is provided, the verify command will compare the calculated and provided SHA-512 hashes as illustrated in the following example:

```
ciscoasa# verify /sha-512 asa915-smp-k8.bin 4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19 .....<output truncated>.....Done! Verified (disk0:/asa915-smp-k8.bin) = 4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19
```

If the network administrator provides a SHA-512 hash that does not match the hash calculated by the Hash File Validation feature, an error message will be displayed. This message is shown in the following example:

```
ciscoasa# verify /sha-512 asa915-smp-k8.bin 4deb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19 .....<output truncated>.....Done! %Error verifying disk0:/asa915-smp-k8.bin

Computed signature = 4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19

Submitted signature = 4deb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19
```

For additional information about how to use this feature, refer to the Cisco ASA command reference document.

### Using Offline Image File Hashes

A network administrator can verify the hash of a Cisco ASA Software image file stored on an administrative workstation by using any hashing utility. Administrators can use any available hash utility to calculate the hash value of a Cisco ASA Software image. The following example shows how to compute the hash by using the openssl utility.

```
linux:~$ openssl dgst  -sha512 asa915-smp-k8.bin

4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489
d4fe442ad3ab8c93e871b6e7214287208e947380498ae19 asa915-smp-k8.bin
```

### Using Information from Cisco.com

When the MD5 or SHA-512 hash and file size for a Cisco ASA Software image have been collected, network administrators can verify authenticity of the image by using information provided in the Support and Downloads area on the Cisco.com website. This provides details about each publicly available Cisco ASA image and may require a valid Cisco.com account.

Network administrators must identify their Cisco ASA Software release (this can be done by using information obtained from output provided by the show version command) and navigate through the Downloads area to locate the image in use on the Cisco ASA device. Network administrators should verify that one of the following hashes matches the MD5 hash that is provided on Cisco.com:

- MD5 hash calculated by the verify /md5 or verify /sha-512 command

- MD5 or SHA-512 hash calculated by a third-party utility

If the hash value for the entire Cisco ASA image file does not match the hash provided by Cisco, network administrators should download the Cisco ASA image file from the Support and Downloads area on the Cisco.com website and use the file verification methods described in this document to verify integrity of the Cisco ASA image file.

The following is an example of the information provided on Cisco.com during one of the steps required for downloading Cisco ASA Software Release 9.1(5).

Figure 1. Download Software

### Secure Software Publishing - Bulk Hash File Download Center

Cisco continues to strengthen the security in and around its products, solutions, and services. Cisco provides a Secure Hash Algorithm (SHA) 512 bits (SHA512) checksum to validate images that are downloaded from www.cisco.com.

The SHA512 hash value is generated on all software images, creating a unique output that is more secure than the MD5 algorithm. Cisco is providing both the MD5 and SHA512 hashes for all the images made available to customers in a . csv file. The compressed file is digitally signed with a Cisco private key.

Additional information can be found at https://www.cisco.com/c/en/us/support/web/tools/bulk-hash/index.html .

### Verifying Authenticity for Digitally Signed Images

Cisco ASA software supports digitally signed images on some platforms. Digitally signed Cisco software is signed using secure asymmetric (public-key) cryptography.

Digitally signed Cisco software increases the security posture of Cisco ASA devices by ensuring that the software running on the system has not been altered and originates from a trusted source.

Administrators can verify the authenticity and integrity of the binary file by using the show software authenticity file command. In the following example, taken from a Cisco ASA 5516-X Series, the command is used to verify the authenticity of the asa941-lfbff-k8.SPA image on the system:

```
ciscoasa#  show software authenticity file asa941-lfbff-k8.SPA
File  Name                    : disk0:/asa941-lfbff-k8.SPA
Image  type                   : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : NCS_Kenton_ASA Organization Name     : CiscoSystems Certificate Serial Number : 550DBBB9
    Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The organization name and unit values can be used to verify that the signature has been validated.

In addition, administrators can use the show software authenticity running command to verify the authenticity of the image that is currently running and in use on the device. Administrators should verify that the Certificate Serial Number value matches the value obtained by using the show software authenticity file command on the binary file. The following example shows the output of the show software authenticity running command on a Cisco ASA 5516-X Series running the asa941-lfbff-k8.SPA image.

```
ciscoasa#  show software authenticity running 
Image  type                   : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : NCS_Kenton_ASA
        Organization Name     : CiscoSystems
    Certificate Serial Number : 550DBBB9
    Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : ROMMON
        Verifier Version      : Cisco Systems ROMMON,1.1.3
```

Note that signed Cisco ASA images can be identified by the .SPA label in the image name.

## Cisco ASA Runtime Memory Integrity Verification

Cisco ASA Software is a Linux-based operating system (OS) running on various Cisco ASA platforms and virtual firewalls. It features a layered architecture providing control plane and data plane separation. The most important process is called lina, which controls all Cisco ASA Software operations.

Administrators can verify the integrity of the runtime memory of the lina process inside Cisco ASA. This is not a trivial task and there is not currently a solution that would allow the network administrator to analyze all parts of memory manually. However, the best way to verify the integrity of runtime memory for lina is to analyze the region of memory called text .

The text section contains the actual executable code for Cisco ASA Software after it is loaded in memory. As such, verifying its integrity is particularly relevant for detecting in-memory tampering. This region of memory should not change during normal Cisco ASA Software operation, and should be the same across reloads.

Verifying that the text section extracted by a running Cisco ASA device contains no modifications is a way to determine whether a Cisco ASA device has been compromised.

Currently, the only way to obtain the text section from a running Cisco ASA device is by having the device generate a core dump. Unlike Cisco IOS, there is no command to generate a core dump while the Cisco ASA continues running. This means that in order to collect a core dump, an administrator may need to force a crash of the Cisco ASA.

### Core Dump

Caution : The task in this section will trigger an immediate reload of the system. Cisco recommends performing this task during a maintenance window. Cisco does not recommend performing this task if additional forensic evidence needs to be collected as a reload of the device may delete some of the forensic evidence.

Cisco ASA Software does not support any command that would allow collecting the core dump without reloading the Cisco ASA device.

Starting with Cisco ASA Software version 8.2, an administrator can configure the Cisco ASA device to generate a core dump. Once the core dump feature is configured, it will automatically generate a core dump whenever a system crash occurs.

This method, however, implies trust in the memory dump process, which may be compromised and displaying output specified by an attacker.

The core dump is saved on the Cisco ASA file system in the coredumpfsys directory.

Caution: Some older versions of Cisco ASA Software do not include the text section due to a bug in the coredump feature. This has been resolved with the fix of Cisco ASA bugID CSCub38407.

Note: Administrators should ensure that there is enough space on the flash or disk to contain the coredump. The coredump operation will delay the reload of the system.

To configure the system to generate a coredump, use the coredump enable command. The following example shows how to enable a coredump on a Cisco ASA:

```
ciscoasa(config)#  coredump enable

WARNING: Enabling coredump on an ASA5515 platform will delay the reload of
the system by up to 30 minutes in the event of software forced reload.
The exact time depends on the size of the coredump generated.

Proceed  with coredump filesystem allocation of 1000 MB
on  'flash:' (Note this may take a while) ? [confirm]

Making  coredump file system  
image!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Coredump  file system image created & mounted successfully

/dev/loop0  on /mnt/disk0/coredumpfsys type vfat  
(rw,fmask=0022,dmask=0022,codepage=cp437,iocharset=iso8859-1)
```

Once the Cisco ASA is configured for a core dump, administrators can force the Cisco ASA to crash by using the crashinfo force command. The following example shows the command executed on a Cisco ASA:

```
ciscoasa#  crashinfo force page-fault 
WARNING:  This command will force a crash and cause a
          reboot. Do you wish to proceed? [confirm]: 
          
Thread  Name: ci/console
Page  fault: Address not mapped
         r8 0x0000000000333957
[...]
          
Begin to  dump crashinfo to flash....

End of  console dump.
Do 'show  crashinfo' after reboot to retrieve other crash information
Process  shutdown finished
[  3198.628066]
[  3198.628067] Writing coredump file to flash. Please do not reload.
[  3198.628067]
[  3198.628068] Coredump starting....
[  3198.800970]  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[  3228.087298] Writing coredump file to flash.   Please do not reload. 
(elapsed time: 0 Min 30 Secs)
[  3229.493109] !!!!!!!!!!!!!!!!!!!!
[  3258.076139] Writing coredump file to flash.   Please do not reload. 
(elapsed time: 1 Min 0 Secs)
[  3259.388954] !!!!!!!!!!!!!!!!!!!!
[  3288.020683] Writing coredump file to flash.   Please do not reload. 
(elapsed time: 1 Min 30 Secs)
[  3289.241283] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[  3302.582585] Coredump completed
Rebooting.....
[  3313.890603] sd 0:0:0:0: [sda] Synchronizing SCSI cache
[  3313.954768] Restarting system.
[...]
```

After reload, a core dump will be available in the coredumpfsys directory:

```
ciscoasa#  dir coredumpfsys

Directory of disk0:/coredumpfsys/

703    -rwx   46738141     14:53:48 Feb 23  2015   core_smp.2015Feb23_145203.1214.11.gz
```

An administrator can export this file for further processing. The copy command can be used to export the core dump to an external location.

Once the file has been exported, the text section can be extracted. First, uncompress the . gz file. The following example uses gunzip:

```
$ gunzip  core_smp.2015Feb23_145203.1214.11.gz
$ ls  core_smp.2015Feb23_145203.1214.11
core_smp.2015Feb23_145203.1214.11
```

The Cisco ASA core dump is in Executable and Linkable Format (ELF). To determine the boundaries of the text section within the core dump, use the readelf utility. The text section can be identified as the section with the largest size. This can be found by looking at the FileSiz column. Starting with Cisco ASA release 9.5(1) the show memory region command can be used to determine the virtual address where the text section starts.

The following example shows a snippet from the readelf utility on a coredump taken from a Cisco ASA 5515-X running Cisco ASA Software 9.1(5). The information about the text section appears in bold:

```
$ readelf  -lW core_smp.2015Oct13_134142.1188.11

Elf file type is CORE (Core file)
Entry point 0x0
There are 209 program headers, starting at offset 64

Program  Headers:
Type   Offset    VirtAddr           PhysAddr           FileSiz   MemSiz    Flg  Align
NOTE   0x002df8  0x0000000000000000 0x0000000000000000 0x00d728  0x000000       0 LOAD   0x011000  0x0000000000400000 0x0000000000000000 0x39af000 0x39af000 R E  0x1000 LOAD   0x39c0000 0x0000000003faf000 0x0000000000000000 0x003000  0x003000  R E  0x1000
[...]
```

Note: The text section flags (the Flg column) should be Read (R) and Execute (E) only. The text section should not be writable.

The example shows the text section starting with an offset of 69632 bytes (0x011000) and file size of 60485632 bytes (0x39af000). These values can be used to extract the text section from the core dump. This can be performed, for example, using the utility dd :

```
$ dd  if=core_smp.2015Feb23_145203.1214.11 of=core_smp_text.bin bs=1 skip=69632  count=60485632

65572864+0  records in
65572864+0  records out
65572864  bytes (66 MB) copied, 108.547 s, 604 kB/s
```

The output file core_smp_text.bin will be the text region.

After the text region is isolated, compute the checksum of the file. In this example, the Linux utility openssl is used to calculate the SHA-512 checksum of the file:

```
$  openssl dgst -sha512 core_smp_text.bin

SHA512(core_smp_text.bin)=  
ab9801074c53a4db0866b447ef6462761ce5619e28be85ee8f8e449f8efcc54d1d0947a7e8cfed
cee627f7c6deb6e19246d373c2e1ffd3becdf3b699f26b6656
```

This value should be compared to the hash value obtained by hashing the text section taken from a Cisco ASA device that it is known not to be compromised, also referred to as a known-good text region. The following section proposes a procedure to create a known-good text region.

### Creating a Known-Good Text Region

Known-good text is text that it is known not to be compromised. This text can be kept in a file and used as a reference point during the forensic operation. This section proposes a procedure that can be used to create a known-good text region.

- Download the Cisco ASA image from the Cisco Support and Downloads website and note the SHA-512 value of the binary.

- Use the method described in the Using Offline Image File Hashes section of the Cisco IOS Software Integrity Assurance document to verify that the SHA-512 hash of the downloaded image matches the one on the Cisco Support and Downloads website. This file will be called the "known-good image."

- Load the known-good image on a Cisco ASA device.

- Reload the device.

- After reload, use the method described in the Using the Hash File Validation Feature section of this document to verify the integrity of the image that is running. This will be called the "known-good device." The text memory region of this device will be called the "known-good text region."

- Use the method described in the Core Dump section of this document to calculate the hash value of the text region. This is called the "hash of a known-good text region."

## Additional Indicators

### Checking External Accounting Logs

Cisco ASA Software can be configured to send accounting information for EXEC and configuration commands to an external server via the TACACS+.

### Checking External Syslog Logs

Cisco ASA Software can be configured to send syslog information to an external syslog server. Network administrators should check the logs for unusual connections or connection attempts to the Cisco ASA devices via SSH, console, or other available methods.

Additionally, Cisco ASA would generate a syslog when a configuration change is performed with the related command issues. Administrators should review these syslogs and make sure the configuration changes are legitimate.

### Checking Booting Information

Information about the last time the Cisco ASA device was reloaded and the reason may provide additional insight about a possible compromise. For example, an unscheduled reload should raise attention and be investigated further.

Network administrators can use the show version command to see information about uptime, and which file was used to boot the Cisco ASA. The following is an example of show version output.

Important information in order of appearance in the output is:

- System image file: This field provides information about which file was used to boot the ASA. Administrators are advised to ensure that the filename matches the ASA image they intended to boot.

- Uptime: This information indicates how long the ASA has been up since last boot. This information can be correlated with change management logs to see whether a reload was authorized and expected.

- Configuration register: This value is used to indicate how the router should boot. The default value is 0x1 and should not be modified under normal circumstances. Modification of this value may indicate an attempt to change the correct boot sequence.

- Modification to Configuration: This field will give information on which user last modified the configuration together with timestamp.

```
ciscoasa#  show version
Cisco  Adaptive Security Appliance Software Version 9.1(5) 
Device  Manager Version 6.6(1)
Compiled  on Wed 08-Oct-14 16:51 PDT by builders System image file is "disk0:/asa915-smp-k8.bin" Config  file at boot was "startup-config" ciscoasa up 5 hours 18 mins Hardware:   ASA5515, 8192 MB RAM, CPU Clarkdale 3059  MHz, 1 CPU (4 cores)
ASA: 4096 MB RAM, 1 CPU (1 core)
Internal  ATA Compact Flash, 8192MB
BIOS  Flash MX25L6445E @ 0xffbb0000, 8192KB
[...] Configuration register is 0x1
Configuration last modified by enable_15 at 16:49:41.489 UTC Mon Mar 2 2015
```

### Checking the ROM Monitor Information

The ROM monitor is a bootstrap program that initializes the hardware and boots the Cisco ASA Software. Because the ROM monitor settings are persistent, information about the ROM monitor variable values could indicate an attempt to influence the Cisco ASA boot sequence. Administrators can use the set command while in the ROM monitor prompt to see the value of the ROM monitor variables.

The output of the set command may differ depending on the platform and Cisco ASA release.

The following example shows the output of the set command on a Cisco ASA 5515 running 9.1(5):

```
rommon  #0> set
ROMMON  Variable Settings:
ADDRESS=x.x.x.x
SERVER=z.z.z.z
GATEWAY=y.y.yy
PORT=Ethernet0/0
VLAN=untagged
IMAGE=
CONFIG=
LINKTIMEOUT=20
PKTTIMEOUT=4
RETRY=20
```

### Checking Failover Events

Failover history can indicate if a failover event has recently occurred. Failover events should be investigated as a possible indicator of compromise because an attacker could operate on the failover unit to hide the attack and then make that unit active, or use the failover mechanism to reduce the likelihood that a reload or configuration change is detected.

There are two ways administrators should check for recent failover events.

Administrators can use the show failover history command to view recent failover state changes. The following example shows the failover event log from the secondary unit that was on standby, but switched to the active role when an administrator used the command failover active on the ASA:

```
ciscoasa/act#  show failover history 
==========================================================================
From State                 To State                   Reason
==========================================================================
12:34:21 UTC Jun 12 2015
Standby Ready              Just Active                Set by the config command

12:34:21 UTC Jun 12 2015
Just Active                Active Drain               Set by the config command

12:34:21 UTC Jun 12 2015
Active Drain               Active Applying Config     Set by the config command

12:34:21 UTC Jun 12 2015
Active Applying Config     Active Config Applied      Set by the config command

12:34:21 UTC Jun 12 2015
Active Config Applied      Active                     Set by the config command 
==========================================================================
```

The show failover history command is run on the standby primary ASA and shows it moving to the standby role due to the command executed on the mate:

```
ciscoasa/stby#  show failover history
==========================================================================
From  State                 To State                   Reason
==========================================================================
12:28:56  UTC Jun 12 2015
Active  Applying Config     Active Config  Applied  HELLO not heard from mate
            
12:28:56  UTC Jun 12 2015
Active  Config Applied      Active                  HELLO not heard from mate
            
12:34:21  UTC Jun 12 2015
Active                      Standby Ready           Other unit wants me Standby
```

In addition to checking the failover events via the Cisco ASA CLI, the administrator should make sure logging is configured and that logs for failover activities are regularly reviewed.

The following example shows syslogs generated when the secondary ASA takes the active role, and the primary ASA moves to standby:

```
%ASA-1-104001:  (Secondary) Switching to ACTIVE - Set by the config command.
%ASA-1-104002:  (Primary) Switching to STANDBY - Other unit wants me Standby. 
Secondary unit  switch reason: Set by the config command.
```

### Checking the SSL VPN Portal Code

Cisco ASA Software supports a feature called clientless SSL VPN, and when configured, the Cisco ASA will enable a web server allowing remote users to access the SSL VPN portal via a web browser.

Attackers could be interested in compromising the SSL VPN portal page with the intent of injecting malicious code that executes malicious actions on the client machine.

Administrators should make sure they regularly check the XML source code of the SSL VPN portal in the default template and in all customization objects they have configured.

To access the XML code of the SSL VPN portal and customization objects, the administrator can use the export webvpn customization command to copy the content of the SSL VPN portal or of a customization object to a file. The administrator should review the file contents, looking for the presence of a web-based exploit (e.g. javascript code injection, iframe, etc.).

## Checking the Integrity of SSL VPN Plugins

Cisco ASA Software, when configured for clientless SSL VPN, supports the use of external plugins that can be used for different functions. Examples of such plugins are remote desktop protocol | Route Discovery Protocol (RDP), Secure Shell (SSH), Virtual Network Computing (VNC), etc. These plugins are ActiveX or Oracle JRE based, and they can be exploited to compromise clients' machines.

Administrators should regularly check the integrity of the SSL VPN plugins and make sure they have not been compromised.

Administrators should use the show import webvpn plug-in detailed command to visualize the list of plugins loaded on the Cisco ASA device and the base64 encoding of the SHA1 hash and timestamp of when the plugin was created. The following example shows the information about a Cisco ASA device with the RDP rdp02.24.2014.jar plugin installed:

```
ciscoasa/act#  show import webvpn plug-in detailed 

rdp          1IDx/GUOgQFnwGhtz/5+KunT+wU= Mon, 24  Feb 2014 17:47:53 GMT
```

The hash included in the output of this command can be verified by calculating the base64 encoding of a binary file generated by the command openssl sha1 binary rdp02.24.2014.jar.

## Checking the Configuration Checksum

Cisco ASA Software stores the checksum of the running configuration. Administrators could use the show checksum command to retrieve the checksum value. This value should be monitored to make sure that it only changes after an authorized configuration change occurs.

## Verify the Integrity of Other Software Loaded on the Cisco ASA Device

Besides verifying the integrity of the Cisco ASA Software image, administrators should also verify the integrity of other images that are typically used with the Cisco ASA. The verification steps are similar to the ones already discussed in the Cisco ASA Image File Verification section of this document.

In particular, the following images should be verified:

- Cisco AnyConnect Mobile Client

- Cisco Adaptive Security Device Manager

- Cisco Secure Desktop

- Cisco SSL VPN plugins

# Security Best Practices

## Maintain Cisco ASA Image File Integrity

To minimize the risk associated with malicious code, it is important that network administrators develop, and consistently apply, a secure methodology for Cisco ASA Software image management. This secure process must be used from the time a Cisco ASA Software image is downloaded from Cisco.com until a Cisco ASA device begins using it.

Although processes may vary based on the network and its security and change management requirements, the following procedure represents an example of best practices that may help minimize the possibility of malicious code installation.

- When downloading a Cisco ASA Software image from www.cisco.com, record the SHA-512 hash as presented by the Cisco Support and Downloads area of the cisco.com website.

- After the image has been downloaded to an administrative workstation, the SHA-512 hash of the local file should be verified against the hash presented by the Cisco ASA Upgrade Planner.

- After the Cisco ASA Software image file has been verified as authentic and unaltered, copy it to write-once media or media that can be rendered as read-only after the image has been written.

- Verify the ASA hash of the file written to the read-only media to detect corruption during the copy process.

- Remove the local file on the administrative workstation.

- Relocate the read-only media to the file server that is used for Cisco ASA Software image distribution to Cisco ASA devices.

- Transfer the Cisco ASA Software image from the file server to the Cisco ASA device using a secure protocol that provides both authentication and encryption.

- Verify the SHA-512 hash of the Cisco ASA Software image on the Cisco ASA device using any of the procedures detailed in the Cisco ASA Image File Verification section of this document.

- Modify the configuration of the Cisco ASA device to load the new Cisco ASA Software image upon startup.

- Reload the Cisco ASA device to place the new software into service.

## Implement Change Control

Change control is a mechanism through which network device changes are requested, approved, implemented, and audited. Change control is a great help in determining which changes have been authorized and which are unauthorized. Change control is important to help ensure that only authorized and unaltered Cisco ASA Software is used on Cisco ASA devices in the network.

## Harden the Software Distribution Server

The server that is used to distribute software to Cisco ASA devices in the network is a critical component of network security. Several best practices should be implemented to help ensure the authenticity and integrity of software that is distributed from this server. These best practices include the following:

- Application of well-established operating system hardening procedures that are specific to the operating system in use.

- Configuration of all appropriate logging and auditing capabilities, including logging to write-once media.

- Placement of the software distribution server on a secure network with restricted connectivity from all but the most trusted networks.

- The use of restrictive security controls to limit interactive access (as an example, SSH) to only a subset of trusted network administrators.

## Keep Cisco ASA Software Updated

Cisco ASA Software used in the network should be kept up to date so that new security functionality can be used and exposure to known vulnerabilities disclosed through Cisco Security Advisories is minimal.

Cisco is continually evolving the security of Cisco ASA Software images through the implementation of new security functionality and the resolution of bugs. For these reasons, it is imperative that network administrators maintain their networks in a manner that includes using up-to-date software. Failure to do so could expose vulnerabilities that may be used to gain unauthorized access to a Cisco ASA device.

Cisco transparently communicates vulnerabilities found in all Cisco products according to the Cisco Security Vulnerability Policy .

## Deploy Digitally Signed Cisco ASA Images

Digitally signed Cisco software is signed using secure asymmetrical (public-key) cryptography.

The purpose of digitally signed Cisco software is to increase the security posture of Cisco ASA devices by ensuring that the software running on the system has not been tampered with and originated from a trusted source as claimed.

## Cisco Secure Boot

Cisco Secure Boot is a secure startup process that the Cisco device performs each time it boots up. Beginning with the initial power-on, a special purpose hardware device verifies the integrity of the ROMMON code and the Cisco ASA image via digital signatures as they are loaded. If any failures are detected, the user is notified of the error and the device will wait for the operator to correct the error. This prevents the network device from executing compromised software.

For a list of Cisco ASA hardware that supports Secure Boot and digitally signed images, see the Cisco Secure Boot Product List .

## Cisco Supply Chain Security

Cisco's Supply Chain Security program focuses on counterfeit products, tainted products, and misuse of intellectual property. As important as physical security, maintaining a chain of custody from manufacturing through installation and provisioning is vital to a trustworthy network. There are many avenues to introduce malicious software or fraudulent hardware into network devices, and the Cisco Supply Chain Security program ensures that devices delivered with the Cisco Systems name are authentic and unmodified.

While this program will help ensure the authenticity of the Cisco hardware, administrators should make sure they have tight control on the delivery of new or refurbished equipment once it has arrived to the premise.

For additional information, see Cisco Supply Chain Security .

## Leverage the latest Cisco ASA Security Protection Features

Cisco is continuously working on increasing the security protection present in Cisco devices. Whenever possible, Cisco leverage the current hardware and provides software updates that will include such features. However in some case, new hardware capabilities are needed to provide best protection.

Administrators should review their hardware and software and make sure that features such as Cisco Digitally Signed Images, ASLR, and Cisco Secure Boot are present on devices running in critical segments of their network infrastructure.

## Use Authentication, Authorization, and Accounting

The comprehensive implementation of authentication, authorization, and accounting (AAA) is critical to ensuring the security of interactive access to network devices. Furthermore, AAA (specifically the authorization and accounting functions) should be used to limit the actions that authenticated users can perform and provide an audit trail of individual user actions.

The following example shows the necessary configuration to send accounting information to an external AAA server. Note that Cisco also recommends configuration of authentication and authorization together with accounting.

```
aaa accounting SSH console <serv-name>
aaa-server <serv-name> protocol tacacs+ 
aaa-server <serv-name> (<interface-name>) host <ip-address-of-tacacs-server> key <key>
```

Refer to Configure AAA for System Administrators for more information regarding the configuration of AAA command accounting.

## Use TACACS+ Authorization to Restrict Commands

Command authorization via the TACACS+ protocol should be enforced to keep tight control over commands that network administrators should not use without specific reasons. This can be accomplished by configuring authentication and command authorization via TACACS+.

When authorization is in place, the following commands should be restricted or prohibited by configuring the external AAA server. The following commands are particularly relevant to ensure that the Cisco ASA Software runtime memory and boot sequence are not modified:

- gdb *

- test *

- service internal

- config-register*

- boot*

- reload *

- debug menu*

- upgrade *

The following commands may be used to show a particular state of the system. They are important because they can be used during a reconnaissance attack to study the system and prepare an attack using other commands:

- show process *

- show memory *

## Implement Credential Management

Passwords control access to resources and devices when they are required for request authentication. When a request for access to a resource or device is received, the request is challenged for verification of the password and identity. Access can be granted, denied, or limited based on the result. As a security best practice, passwords must be managed with a TACACS+ or RADIUS authentication server. However, note that a locally configured password for privileged access will still be needed in the event of TACACS+ or RADIUS services failure. A device may also have other password information present in its configuration. Examples include an NTP key, SNMP community string, and failover or routing protocol keys.

The enable password command is used to set the password that grants privileged administrative access to the Cisco firewall system. This command uses Message Digest 5 (MD5) for password hashing. This algorithm has had considerable public review and is not known to be reversible. However, the algorithm is subject to dictionary attacks, in which an attacker attempts various dictionary words in addition to other lists of candidate passwords to search for a match. For resilience against dictionary attacks, a salt value is added to the password before it is hashed and stored. As a general precaution, configuration files must be securely stored and shared only with trusted individuals.

User passwords are also hashed using the MD5 algorithm after they have been concatenated with a salt value that provides resilience against dictionary attacks. Other Cisco firewall passwords (such as Open Shortest Path First (OSPF) keys and virtual private network (VPN) keys) are not encrypted on the firewall device by default, but the configured passwords will not be shown in the show running-configuration command output. Any Cisco firewall configuration file that contains passwords must be treated with care.

Beginning with Cisco ASA version 8.3, the firewall can store plaintext passwords in an encrypted format. The encryption algorithm is the Advanced Encryption Standard (AES). The feature requires the definition of an encryption passphrase that is used to encrypt and decrypt the keys/passwords. Keys that can be encrypted include keys for routing protocol authentication, VPN, failover, AAA servers, logging, shared licenses, and more. Refer to the Configure the Master Passphrase section of the Cisco ASA Series General Operations CLI Configuration Guide for further information on the feature.

## Securing Interactive Management Sessions

Management sessions destined to devices allow one to view and collect information about a device and its operations. If this information is disclosed to a malicious user, the device can become the target of an attack, compromised, and used to perform additional attacks. Anyone with privileged access to a device has the capability for full administrative control of that device. Securing management sessions is imperative to preventing information disclosure and unauthorized access.

Additional information on how to secure interactive management sessions can be found in the Securing Interactive Management Session section of the Cisco Firewall Best Practices Guide .

## Gain Traffic Visibility with NetFlow

Cisco ASA supports NetFlow version 9 services. In particular, the Cisco ASA implementation of NetFlow Secure Event Logging (NSEL) is stateful, IP flow tracking method that exports only records that indicate significant events in a flow. In stateful flow tracking, tracked flows go through a series of state changes. NSEL events are used to export data about flow status and are triggered by the event that caused the state change.

The significant events that are tracked include flow-create , flow-teardown , and flow-denied (excluding flows that are denied by EtherType access control lists (ACLs). Each NSEL record has an event ID and an extended event ID field, which describes the flow event.

For details regarding NSEL on Cisco firewalls, refer to the Cisco ASA NetFlow Implementation Guide . More information about this feature and how to use NetFlow to identify a possibly compromised device or network are in the Traffic Identification and Traceback section of the Cisco Guide to Harden Cisco IOS Devices document and in the Telemetry-Based Infrastructure Device Integrity Monitoring document.

## Use Centralized and Comprehensive Logging

For network administrators to understand the events that are taking place on a network, a comprehensive logging structure using centralized log collection and correlation must be implemented. Additionally, a standardized logging and time configuration must be deployed on all network devices to facilitate accurate logging. Furthermore, logging from the AAA functions in the network should be included in the centralized logging implementation.

After comprehensive logging is in place on a network, the collected data must be used to monitor network activity for events that may indicate unauthorized access to a network device or unauthorized actions by legitimate users. These types of events could represent the first step in undermining the security on a Cisco ASA device. Because the following items may represent unauthorized access or unauthorized actions, they should be monitored closely:

- The transmission of Cisco ASA Software images to a Cisco ASA device using the copy command or local SCP, TFTP, or FTP server functionality.

- The attempted execution of certain high-risk EXEC commands. The copy , gdb , more , configure, and test commands are some examples of commands that should be monitored. This list is not exhaustive.

- Modification of the boot environment in use on the network devices. This specifically includes the boot and config-register global configuration commands.

- Modification of the security configuration for a Cisco ASA device.

- Logging related to the insertion or removal of storage media, such as flash devices.

- SNMP-related logging of attempts to modify the Cisco ASA device configuration or perform file management tasks.

- The planned and unplanned reload of Cisco ASA Software due to a software crash or the use of the reload command.

For more information, see the Centralize Log Collection and Monitoring and Logging Best Practices sections of Cisco Firewall Best Practices Guide .

# Conclusion

In conclusion, as interest in Cisco ASA Software integrity assurance is growing, this document presents various methods for an administrator to assess the integrity of the software running on his or her Cisco ASA device. These include image and memory verification, command checks, boot history checks, and more. Most miscreants targeting Cisco ASA Software would, in theory, attempt to achieve it by compromising images, or exploiting vulnerabilities. These techniques can usually be prevented by implementing common recommendations and best practices that are published by Cisco and summarized in this document. Command authorization and accounting, logging, credential management, image signing, vulnerability control, and device hardening are some of the most important practices that will not only prevent Cisco ASA Software modification in nearly all cases, but will also ensure good security policy.

# Acknowledgments

Author: Stefano De Crescenzo (sdecresc[at]cisco[dot]com) is a member of the PSIRT team in the Cisco Security organization.

# References

Cisco Firewall Best Practice Guide http://www.cisco.com/web/about/security/intelligence/firewall-best-practices.html

Cisco Security Vulnerability Policy http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html

Creating Core Dumps https://supportforums.cisco.com/document/59021/enabling-coredump-asa

Telemetry-Based Infrastructure Device Integrity Monitoring http://www.cisco.com/web/about/security/intelligence/network-integrity-monitoring.html

Cisco IOS Software Integrity Assurance http://www.cisco.com/web/about/security/intelligence/integrity-assurance.html

Cisco IOS XE Software Integrity Assurance http://www.cisco.com/web/about/security/intelligence/ios-xe-integrity-assurance.html

Cisco Supply Chain Security https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/supplychainsecurity.pdf

Cisco Trust Anchor Technologies: Secure Boot Product List https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/cisco-secure-boot-product-list.pdf

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Date | Description |
|---|---|
| March 9, 2022 | Reviewed document and updated URLs. |
| September 7, 2018 | Moved content to a new URL. |
| September 28, 2016 | Added information about ASA support for Secure Boot. |
| April 11, 2016 | Initial public release. |