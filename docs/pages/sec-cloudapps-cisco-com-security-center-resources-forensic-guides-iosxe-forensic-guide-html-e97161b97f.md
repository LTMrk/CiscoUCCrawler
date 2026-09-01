---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-iosxe-forensic-guide-html-e97161b97f
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/iosxe_forensic_guide.html
retrieved_at: 2026-09-01T14:10:45.829693+00:00
---

Home / Cisco Security

Cisco IOS XE Software Forensic Data Collection Procedures

# Cisco IOS XE Software Forensic Data Collection Procedures

Introduction

Prerequisites

Step One – Cisco IOS XE Device Problem Description

Step Two – Document the Cisco IOS XE Runtime Environment

Step Three – Cisco IOS XE Image File Hash Verification

Image File Hash Verification (.bin file)

Image File Hash Verification (.conf file)

Step Four – Verify Digitally Signed Image Authenticity

Step Five – Text Memory Section Export

Step Six – Core File Generation

Acknowledgments

Related Documentation

Cisco IOS XE Device Forensic Response Checklist

Revision History

## Introduction

This document provides guidance for collecting evidence from Cisco IOS XE devices that are suspected of compromise or tampering. It outlines a number of commands that can be run to gather evidence for an investigation along with the respective output that should be collected upon running these commands. This document also provides information on how to perform integrity checks on a device’s Cisco IOS XE images and includes a procedure for collecting the text memory segment so that the run-time integrity of the IOSd process can be ascertained.

Note: It is extremely important when triaging a network device for compromise or tampering that it is not rebooted. Rebooting a device during an initial assessment will irrecoverably lose all volatile information contained within the device (for example, RAM contents, arp and routing tables, NAT translations, ACL hit and drop counts, etc.).

Note: It is highly recommended that a device suspected of tampering or compromise be isolated from the network prior to conducting an initial forensic examination. This may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device under investigation.

If you require assistance or have questions regarding the procedures described in this document, contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains six main sections:

- Cisco IOS XE Device Problem Description – Describes why the platform is a candidate for forensic examination

- Cisco IOS XE Runtime Environment – Collects platform configuration and runtime state

- Cisco IOS XE Image File Verification – Examines system image hashes for inconsistencies

- Digitally Signed Image Verification – Examines system and running images for proper signing characteristics

- Text Memory Section Export – Collects the information necessary to verify the runtime integrity of the IOSd process

- Core File Generation – Obtains a complete copy of platform memory

## Prerequisites

The procedures outlined in this document assume that the reader has a basic understanding of Cisco IOS XE Software command syntax.

A valid cisco.com account is required to view individual Cisco IOS XE file hashes for software file integrity checking. A publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded from: https://www.cisco.com/c/en/us/about/trust-center/downloads.html

A Cisco Technical Assistance Center (TAC) service request (SR) for the device in question is required because these procedures assume that the information gathered in each step will be uploaded to a TAC SR.

Note: The examples used in this document are based on Cisco IOS XE Software Release 17.18.01 command syntax. The output produced by a command may vary depending on the software version deployed and/or the features supported or configured on the device. Not all commands used in these procedures may be supported on earlier versions of the software.

## Step One – Cisco IOS XE Device Problem Description

Describe in as much detail as possible why the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior than cannot be attributed to a misconfiguration or a software/hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific software releases of the following products: Cisco ASA, FMC, FTD, FXOS, IOS, IOS XE, NX-OS, and NX-OS in ACI Mode.

https://sec.cloudapps.cisco.com/security/center/softwarechecker.x

Record any results returned by the tool that may explain the anomalous behavior being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA, FMC, FTD and FXOS Software, the tool only contains vulnerability information for Cisco Security Advisories first published from January 2022 onward, and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Submit the problem description and any relevant results obtained from the Cisco Software Checker collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Two – Document the Cisco IOS XE Runtime Environment

Note: Several of the commands in this section and in the steps that follow require service internal to be configured. Issue the following commands to enable service internal :

```
configure terminal
service internal
end
```

Complete the initial stage of evidence gathering by issuing a number of show and dir commands. These commands must be executed in enable mode (privileged EXEC mode), and some of the output produced may vary depending on the particular Cisco IOS XE hardware platform, software version, and/or configured features.

Execute each of the following commands in enable mode and record the output:

```
show tech-support
```

Note: The output from the show tech-support command may be redirected to the local file system or a server running any of the following protocols: FTP, HTTP/S, or TFTP.  The following example depicts the use of the FTP protocol:

```
Router#show tech-support | redirect ftp://anonymous@192.168.1.1/show-tech.txt
```

```
!! Execute the following commands on all routing and switching platforms:
!! Enumerate app hosting environment
show iox
show app-hosting list 
!! Display system boot sequence integrity and hardware authenticity:
show platform integrity sign nonce 12345 
show platform hardware authentication status 
!! system logs – Note: core files and tracelogs may exist on the flash:, bootflash:, harddisk:, or crashinfo: partitions 
dir harddisk:/tracelogs

!! Execute the following two commands only on routing platforms:
show platform software process memory rp active name linux_iosd-imag maps 
show platform software process memory rp active name iosd smaps 
!! For more information about the command above, see footnote [1] at the end of this section

!! Execute the following two commands only on switching platforms:
!! Some switches require a target of r0.
!! Replace rp with r0 in the following two commands if a syntax error occurs.
show platform software process memory switch active rp name linux_iosd-imag maps 
show platform software process memory switch active rp active name iosd smaps 
!! For more information about the command above, see footnote [1] at the end of this section
```

Obtain a copy of any files found under the /tracelogs directory where the filename begins with “system_shell” as these will need to be uploaded to the SR. The following is an example of a shell log file that should be preserved:

```
3686402  -rw-   2132  Jul 26 2018 06:16:22 +00:00  system_shell_R0.log.20180726055205
```

Submit all command output and any system shell logs collected in this section to the relevant TAC SR and proceed to the next section of this document.

[1] Note: This procedure checks the active route processor (RP) for non-zero values in the “Private Dirty” entry for each segment with the executable flag set (i.e., r-xp or rwxp).

Routing platforms:

```
show platform software process memory rp active name iosd smaps
```

Switching platforms:

```
show platform software process memory switch active rp active name iosd smaps
```

The commands above display the memory map for the iosd process running on the active route processor. Executable segments of a program typically have the r-xp (read, execute, protected) attributes set, while an executable segment with the w (write) attribute set may indicate the software has been tampered with.

Example 1:

```
#
# This segment is flagged rw-p (read, write, protected) so a private
# dirty value greater than zero is expected and not of concern. 
#
Router#show platform software process memory rp active name iosd smaps

smaps for process 7438:
address          perms offset   dev   inode      pathname
7fff6000-7fff7000 rw-p 00000000 00:00 0 
Size:                128 kB
KernelPageSize:        4 kB
MMUPageSize:           4 kB
Rss:                  32 kB
Pss:                  32 kB
Shared_Clean:          0 kB
Shared_Dirty:          0 kB
Private_Clean:         0 kB
Private_Dirty:        64 kB
Referenced:           64 kB
Anonymous:            64 kB
LazyFree:              0 kB
AnonHugePages:         0 kB
ShmemPmdMapped:        0 kB
Shared_Hugetlb:        0 kB
Private_Hugetlb:       0 kB
Swap:                  0 kB
SwapPss:               0 kB
Locked:                0 kB
THPeligible:    0
VmFlags: rd wr mr mw ac
[output truncated]
```

Example 2:

```
#
# This segment is flagged rwxp (read, write, execute, protected) and
# private dirty has a value greater than zero which may indicate the
# software has been tampered with. 
#
Router#show platform software process memory rp active name iosd smaps

smaps for process 16320:
10a0000000-10a04c1000 rwxp 00000000 00:00 0 
Size:                128 kB
KernelPageSize:        4 kB
MMUPageSize:           4 kB
Rss:                 128 kB
Pss:                 128 kB
Shared_Clean:          0 kB
Shared_Dirty:          0 kB
Private_Clean:         0 kB
Private_Dirty:       128 kB
Referenced:          128 kB
Anonymous:           128 kB
LazyFree:              0 kB
AnonHugePages:         0 kB
ShmemPmdMapped:        0 kB
Shared_Hugetlb:        0 kB
Private_Hugetlb:       0 kB
Swap:                  0 kB
SwapPss:               0 kB
Locked:                0 kB
THPeligible:    0
VmFlags: rd wr ex mr mw me ac 
[output truncated]
```

## Step Three – Cisco IOS XE Image File Hash Verification

Access the command line of the Cisco IOS XE device and issue the following command in enable mode:

```
show version | include System image
```

If the system image file has a .bin file extension as shown in the following example, execute the steps in the Image File Hash Verification (.bin file) section of this document and omit the steps in the Image File Hash Verification (.conf file) section.

```
System image file is "bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin"
```

If the system image file has a .conf file extension as shown in the following example, skip the Image File Hash Verification (.bin file) section of this document and execute the steps in the Image File Hash Verification (.conf file) section.

```
System image file is "bootflash:packages.conf"
```

### Image File Hash Verification (.bin file)

Note the location and filename of the system image file obtained in the beginning of this section and execute the following command:

```
verify location:filename
```

An example of this procedure is as follows:

```
Router1#show version | include System image
System image file is "bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin"

Router1#verify bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin
Verifying file integrity of bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin
...........................................................................
...........................................................................
Embedded Hash   SHA1 : 7E9EA496349FC44B223C09F6DCC89FA1F5FBA7A8
Computed Hash   SHA1 : 7E9EA496349FC44B223C09F6DCC89FA1F5FBA7A8
Starting image verification
Hash Computation:    100%Done!
Computed Hash   SHA2: 35ea9ab4825f32810def7c10aa23acb4
                      80da7bb0e4903d3e28d3ebec2bd1cd5a
                      9c5cdb6c2faf429c945efe48b78a7920
                      3ceb36bae21324d88963df3ddd6aedda
                      
Embedded Hash   SHA2: 35ea9ab4825f32810def7c10aa23acb4
                      80da7bb0e4903d3e28d3ebec2bd1cd5a
                      9c5cdb6c2faf429c945efe48b78a7920
                      3ceb36bae21324d88963df3ddd6aedda
                      
Digital signature successfully verified in file bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin
Embedded hash verification successful.
```

Note that the embedded hash and computed hash should retun the same SHA1 (160 bit) and SHA2 (256 bit) values.

An SHA-512 hash can be calculated by adding the /sha512 parameter to the verify command as follows:

```
verify /sha512 location:filename
```

An MD5 hash can also be calculated by adding the /md5 parameter to the verify command as follows:

```
verify /md5 location:filename
```

The SHA-512 or MD5 hashes should match the values listed on CCO or in the Bulk Hash File for that particular image file.

Note : CCO contains only MD5 and SHA-512 hash values for software images.

Repeat the previous procedure for any other system image file located on the file systems. A comprehensive list of all files can be viewed by executing the following command:

```
dir all-filesystems
```

If any of the image file hashes show inconsistencies, copy the image file in question to a secure location if possible.

```
copy < location>:<system_image_filename.bin > ftp:
Address or name of remote host []? < destination_ip >
Destination filename []? <destination_filename.bin >
```

It is highly recommended that a hash value be calculated on the copied system image file and compared to the hash value obtained on the platform to ensure that no errors were introduced during the file transfer process.

Submit all command output (including calculated hash values), the running system image, and any other system images tested in this section to the relevant TAC SR and proceed to Step Four.

### Image File Hash Verification (.conf file)

Note the location and filename of the system image file obtained in the beginning of this section and execute the following command:

```
more location:filename
```

Next, issue the following command for the packages.conf image file and each unique entry listed in the contents of the packages.conf image file:

```
verify location:filename
```

An example of this procedure is as follows:

```
CSR1000v#show version | include System image
System image file is "bootflash:packages.conf"

CSR1000v#more bootflash:packages.conf | include .SPA.pkg
boot  rp 0 0   rp_boot       csr1000v-rpboot.16.06.04.SPA.pkg
iso   rp 0 0   rp_base       csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 1   rp_base       csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 0   rp_daemons    csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 1   rp_daemons    csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 0   rp_iosd       csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 1   rp_iosd       csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 0   rp_security   csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 1   rp_security   csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   fp 0 0   fp            csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   fp 0 1   fp            csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 0   rp_webui      csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 0 1   rp_webui      csr1000v-mono-universalk9.16.06.04.SPA.pkg
boot  rp 1 0   rp_boot       csr1000v-rpboot.16.06.04.SPA.pkg
iso   rp 1 0   rp_base       csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 1   rp_base       csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 0   rp_daemons    csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 1   rp_daemons    csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 0   rp_iosd       csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 1   rp_iosd       csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 0   rp_security   csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 1   rp_security   csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   fp 1 0   fp            csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   fp 1 1   fp            csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 0   rp_webui      csr1000v-mono-universalk9.16.06.04.SPA.pkg
iso   rp 1 1   rp_webui      csr1000v-mono-universalk9.16.06.04.SPA.pkg

CSR1000v#verify bootflash:packages.conf
bootflash:packages.conf is detected as a provisioning file
Verifying file integrity of bootflash:packages.conf.
Embedded Hash   SHA1 : 7EBF483217E3E7071ED796F2A17258FB60B6B2B0
Computed Hash   SHA1 : 7EBF483217E3E7071ED796F2A17258FB60B6B2B0
```

Note: In this example, packages.conf contains only two unique file entries:

```
csr1000v-rpboot.16.06.04.SPA.pkg
csr1000v-mono-universalk9.16.06.04.SPA.pkg
```

Therefore, the verification command need only be run twice, once on each of these two files.

```
CSR1000v# verify bootflash:csr1000v-rpboot.16.06.04.SPA.pkg
Verifying file integrity of bootflash:csr1000v-rpboot.16.06.04.SPA.pkg
...........................................................................
...........................................................................
Embedded Hash   SHA1 : 3AEDB29325BB17D02B39D295F15627286A1E2BEA
Computed Hash   SHA1 : 3AEDB29325BB17D02B39D295F15627286A1E2BEA
Starting image verification
Hash Computation:    100%Done!
Computed Hash   SHA2: f2682757e0106b9c3907962d96028608
                      89eb9325e0cb78276b0097219192143a
                      0d35fd011c0610279f0a97c55fe2ea6c
                      2aac24889967ce07344253f79267dcf2
                      
Embedded Hash   SHA2: f2682757e0106b9c3907962d96028608
                      89eb9325e0cb78276b0097219192143a
                      0d35fd011c0610279f0a97c55fe2ea6c
                      2aac24889967ce07344253f79267dcf2
                      
Digital signature successfully verified in file bootflash:csr1000v-rpboot.16.06.04.SPA.pkg

CSR1000v# verify bootflash:csr1000v-mono-universalk9.16.06.04.SPA.pkg
Verifying file integrity of bootflash:csr1000v-mono-universalk9.16.06.04.SPA.pkg
...........................................................................
...........................................................................
Embedded Hash   SHA1 : C5843C05740F1828197F3093DA294F11BA1DE37B
Computed Hash   SHA1 : C5843C05740F1828197F3093DA294F11BA1DE37B
Starting image verification
Hash Computation:    100%Done!
Computed Hash   SHA2: 14354cda30bb20d38e572275c6e1cc2a
                      0cc647459a1a34dd4267282eeaddf799
                      bda3f2048aca419ea49a417fe28fa43b
                      4e1501acb9f54fb521fe5b00e7f8337e
                      
Embedded Hash   SHA2: 14354cda30bb20d38e572275c6e1cc2a
                      0cc647459a1a34dd4267282eeaddf799
                      bda3f2048aca419ea49a417fe28fa43b
                      4e1501acb9f54fb521fe5b00e7f8337e
                      
Digital signature successfully verified in file bootflash:csr1000v-mono-universalPA.pkg
```

Note that the embedded hash and computed hash should retun the same SHA1 (160 bit) and SHA2 (256 bit) values.

An SHA-512 hash can be calculated by adding the /sha512 parameter to the verify command as follows:

```
verify /sha512 location:filename
```

An MD5 hash can also be calculated by adding the /md5 parameter to the verify command as follows:

```
verify /md5 location:filename
```

The SHA-512 or MD5 hashes should match the values listed on CCO or in the Bulk Hash File for that particular image file.

Note : CCO contains only MD5 and SHA-512 hash values for software images.

Repeat the above procedure for any other system image file located on the file systems. A comprehensive list of all files can be viewed by executing the following command:

```
dir /recursive all-filesystems
```

If any of the image file hashes show inconsistencies, copy the image file in question to a secure location if possible.

```
copy < location>:<system_image_filename.bin > ftp:
Address or name of remote host []? < destination_ip >
Destination filename []? <destination_filename.bin >
```

It is highly recommended that a hash value be calculated on the copied system image file and compared to the hash value obtained on the platform to ensure that no errors were introduced during the file transfer process.

Submit all command output (including calculated hash values), the running system image, and any other system images tested in this section to the relevant TAC SR, and proceed to Step Four of this document.

## Step Four – Verify Digitally Signed Image Authenticity

Cisco IOS XE Software implements digitally signed system images on most platforms. Digitally signed Cisco software uses asymmetric (public-key) cryptography that increases the security posture of Cisco IOS XE devices by ensuring that the software running on the system has not been altered and that the software originates from a trusted source.

Note: If the system image file was reported as packages.conf in Step Three, run the command more packages.conf to identify the individual software packages that comprise the boot image, and use those filenames as input to the show software authenticity file command. Software packages may be loaded multiple times by packages.conf, but the file verification procedure need only be run once per unique filename.

The authenticity and integrity of a system image file can be verified by using the following command:

```
show software authenticity file location:filename
```

An example of this procedure follows:

```
Router1#:show software authenticity file bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin  
File Name                     : bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : IOS-XE
        Organization Name     : CiscoSystems
    Certificate Serial Number : 5A94807E
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The Organization Unit, Organization Name, and the Certificate Serial Number values can be viewed to verify that the system image signature is valid.

It is also important to verify the authenticity and integrity of the running system image, and this can be accomplished with the following command:

```
show software authenticity running
```

Note: This procedure may not produce command ouput when executed on Cisco IOS XE virtual devices such as the CSR1000V.

An example of this procedure follows:

```
Router1# show software authenticity running 
SYSTEM IMAGE
------------
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : IOS-XE
        Organization Name     : CiscoSystems
    Certificate Serial Number : 5A94807E
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : ROMMON
        Verifier Version      : System Bootstrap, Version 16.3(2r
Microloader
-----------
Image type                    : Release
    Signer Information
        Common Name           : CiscoSystems
        Organization Name     : CiscoSystems
    Certificate Serial Number : 4143616e6e65642d5348413235362d48
    Hash Algorithm            : HMAC-SHA256
    Verifier Information
        Verifier Name         : Hardware Anchor
        Verifier Version      : ACannedHwAnchorVersionApril2012
```

The Organization Unit, Organization Name, and the Certificate Serial Number values can be viewed to verify that the system image signature is valid, and the Certificate Serial Number should be the same as the value obtained from the show software authenticity file command. In the examples above, the authenticity check of the IOS XE Software image on the boot flash and the authenticity check of the running image both produce a value of 5A94807E.

It is also recommended that digital signatures are verified for all other .bin and .pkg files resident on the device’s file systems. This can be accomplished with the following command:

```
show platform software authenticity verify location:filename
```

An example follows:

```
Router1#:show platform software authenticity verify bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin

Digital signature successfully verified in file bootflash:asr1000rp2-advipservicesk9.03.13.09.S.154-3.S9-ext.bin
```

Note : Some Cisco IOS XE platforms may require that service internal be configured prior to issuing the show platform software authenticity verify command.

Submit all command output collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Five – Text Memory Section Export

This section outlines the procedure to collect the system:memory/text region to verify the run-time integrity of the IOSd process from a device running Cisco IOS XE Software.

Note: This procedure requires a minimum Cisco IOS XE Software release of 15.5.1 or later. The text region in earlier versions of Cisco IOS XE Software may point to the text section of a library instead of the executable code of the IOSd process.

Access the command line interface of the Cisco IOS XE device and issue the following command in enable mode to view the system:memory/text entry:

```
dir system:memory
```

Copy the system:memory/text region to a file server using ftp or scp.

```
copy system:memory/text ftp:
```

An example of this procedure is depicted below:

```
Router1#dir system:memory
Directory of system:/memory/
    8  -r--         26460576                    <no date>  bss
    7  -r--            59584                    <no date>  data
    5  -r--  -      24686336                    <no date>  heap
    4  -r--          6295128                    <no date>  lsmpi_mem
    9  -r--           196608                    <no date>  stack
    6  -r--           303844                    <no date>  text
No space information available

Router1#copy system:memory/text ftp:
Address or name of remote host []? 192.168.1.1
Destination filename [text]? asr1004_main_text
Writing asr1004_main_text !!!!!!
303844 bytes copied in 4.641 secs (65470 bytes/sec)
```

It is highly recommended that hash values be calculated for the device’s system:memory/text region and for the file that was copied to the file server to ensure no errors were introduced during the file transfer process.

To calculate a hash value for the system:memory/text region, execute the following command:

```
verify /md5 system:memory/text
```

An example of this procedure is depicted below:

```
Router1#verify /md5 system:memory/text
.....Done!
verify /md5 (system:memory/text) = 53271c3c2baae5f6f9666db3031d478f
```

Next, calculate a hash value for the file transferred to the file server. An MD5 hash value can be calculated with the md5sum utility, which is included with most Linux distributions.

```
root@ftp-server:~# md5sum asr1004_main_text
53271c3c2baae5f6f9666db3031d478f asr1004_main_text
root@ftp-server:~#
```

Note that the Cisco IOS XE verify command and the md5sum utility both produce a MD5 hash value of 53271c3c2baae5f6f9666db3031d478f.

Submit all command output (including calculated hash values) and the file that contains the system:memory/text output to the relevant TAC SR and proceed to the next section of this document.

## Step Six – Core File Generation

This procedure outlines how to configure a Cisco IOS XE device to obtain a core dump of platform memory. A crash information file is created in the root of the bootflash filesystem, and the core file is created in the bootflash:/core subdirectory.

CAUTION: This section contains commands that may cause the platform to reboot. It is of critical importance that all the preceding information gathering steps have been completed successfully or important evidence may be permanently lost . Creating core dumps may also cause spikes in memory consumption and momentary disruptions to traffic transiting the device if a standby route processor is not present in the platform.

Note: Creating a core file may take several minutes. While the IOSd process space is being collected and written to disk, the file will have a .TEMP_IN_PROGRESS extension. Before copying the core file off the platform, make sure this temporary extension is no longer present.

Example of a core file in progress:

```
Router1_RP_0_x86_64_crb_linux_iosd-universalk9-ms_14778_20230201-141137-EST.core.gz.TEMP_IN_PROGRESS
```

Example of a completed core file:

```
Router1_RP_0_x86_64_crb_linux_iosd-universalk9-ms_14778_20230201-141137-EST.core.gz
```

The steps to acquire a core dump of the iosd process are as follows:

```
# use the following commands on routing platforms:
show platform software process environment ios rp active
request platform software process core ios rp active

# use the following commands on switching platforms:
# Note: switches with a single route processor may produce an error using
# rp as the target in the commands below. If so, use r0 as a target instead.
show platform software process environment ios switch active rp
request platform software process core ios switch active rp active
```

Note: Some platforms may use the test command instead of the request command. The syntax for the test command is as follows:

```
test platform software process core <process> <slot>
```

An example of the procedure to acquire a crash info file and core dump file follows:

```
Router1#show platform software process environment ios rp active
Name                            Value                                           
------------------------------------------------------------------------------
TRACEKEY                        1#84f2d2cb5aa33b87358ca5a1b96d199e              
BINOS_FRU_BASE_PKG              rp_base                                         
BINOS_BAY_LOCAL                 0                                               
PROC_CONF_RESTART               norestart                                       
RELOADFAST_FILE                 /tmp/chassis/local/stack_mgr/fast_reload        
BINOS_CONF_DIR                  /usr/binos/conf                                 
PROCESS_FRU                     rp                                              
SLOT                            0                                               
BINOS_BTRACE_FILE_PATH          /tmp/rp/trace                                   
TERM                            linux                                           
BINOS_LOCAL_CHASSIS_PATH        /tmp/chassis/local                              
LD_LIBRARY_PATH_COPY            /tmp/sw/rp/0/0/rp_iosd/mount/lib64:/tmp/sw/rp/  
ROMMON_BOOT                     bootflash:/asr1002x-universalk9.17.03.05.SPA.b  
BOARD_TYPE                      RP                                              
PROC_CONF_FAILURE_ACTION        critical                                        
BINOS_SLOT                      0                                               
TAN_FILE_ROTATE_INTERVAL_IN_SE                                                  
BINOS_FRU                       rp                                              
BINOS_BOOT_MODE                 non-NFS                                         
CHASSIS_SERIAL_NUM              FOX2107P0WA                                     
BINOS_BASE_DIR                  /tmp/rp                                         
[output truncated]

Router1#request platform software process core ios rp active
SUCCESS: Core file generated.
Router1#

Exception to IOS Thread:
Frame pointer 0x7FFE138F3498, PC = 0x7FE8F81E1305

UNIX-EXT-SIGNAL: Aborted(6), Process = Sched
-Traceback= 1#84f2d2cb5aa33b87358ca5a1b96d199e  c:7FE8F81CC000+15305 c:7FE8F81CC000+56C binos:7FE96CD98000+AC8E 

[output omitted]

Writing crashinfo to bootflash:Router1_crashinf_20230201-141134-EST
IOSD RP: 1172 messages not written to btrace log file

Router1#dir
Directory of bootflash:/

64769   drwx             4096   Feb 1 2023 14:11:58 -05:00  core
21      -rw-           220651   Feb 1 2023 14:11:37 -05:00  Router1_crashinf_20230201-141134-EST
696257  drwx             4096   Feb 1 2023 14:11:37 -05:00  .prst_sync
129537  drwx            28672   Feb 1 2023 14:11:03 -05:00  tracelogs
15      -rw-                1  Sep 27 2022 11:36:52 -04:00  cs_verify_rc.txt
97153   drwx             4096  Feb 18 2022 10:39:19 -05:00  .installer
291457  drwx             4096  Feb 18 2022 10:38:16 -05:00  license_evlog
14      -rw-               30  Feb 18 2022 10:38:14 -05:00  throughput_monitor_params
18      -rw-           134458  Feb 18 2022 10:37:37 -05:00  memleak.tcl
242881  drwx             4096  Feb 18 2022 10:37:28 -05:00  .inv
17      -rw-              454  Feb 18 2022 10:37:07 -05:00  mode_event_log
744833  drwx             4096  Feb 18 2022 02:32:53 -05:00  .dbpersist
259073  drwx             4096  Feb 18 2022 02:29:56 -05:00  onep
20      -rw-             1923  Feb 18 2022 02:29:04 -05:00  trustidrootx3_ca_092024.ca
19      -rw-            20109  Feb 18 2022 02:29:04 -05:00  ios_core.p7b
307649  drwx             4096  Feb 18 2022 02:28:50 -05:00  gs_script
194305  drwx             4096  Feb 18 2022 02:28:43 -05:00  bootlog_history
16      -rw-        860923521  Feb 18 2022 02:11:41 -05:00  asr1002x-universalk9.17.03.05.SPA.bin
178113  drwx             4096  Apr 27 2017 13:43:14 -04:00  virtual-instance
13      -rw-                0  Apr 27 2017 13:43:11 -04:00  tracelogs.629
80961   drwx             4096  Apr 27 2017 13:43:05 -04:00  .rollback_timer
12      -rw-        454254232  Apr 27 2017 13:35:32 -04:00  asr1002x-universal.03.16.02b.S.155-3.S2b-ext.SPA.bin
11      drwx            16384  Apr 27 2017 13:33:50 -04:00  lost+found

6646632448 bytes total (4938723328 bytes free)

Router1#verify /sha512 bootflash:/Router1_crashinf_20230201-141134-EST   
....Done!

verify /sha512 (bootflash:/Router1_crashinf_20230201-141134-EST) = def67296d50606d28d4f80b79826ff3898e0f7f07d01f59aefd658309632eb7f308b950d47
1b7c024a0c72097069d8cbb602365b7ddb32c4de99775806e86d62

Router1#dir bootflash:/core
Directory of bootflash:/core/

161922  -rw-         38893484   Feb 1 2023 14:11:58 -05:00  Router1_RP_0_x86_64_crb_linux_iosd-universalk9-ms_14778_20230201-
141137-EST.core.gz
64770   -rw-                1   Feb 1 2023 14:10:16 -05:00  .callhome
161921  drwx             4096  Feb 18 2022 02:28:48 -05:00  modules

6646632448 bytes total (4938723328 bytes free)

Router1#verify /sha512 bootflash:/core/Router1_RP_0_x86_64_crb_linux_iosd-universalk9-ms_14778_20230201-141137-EST.core.gz
...............................................................................................................................
...............................................................................................................................
...............................................................................................................................
...............................................................................................................................
......................................................................................Done!

verify /sha512 (bootflash:/core/Router1_RP_0_x86_64_crb_linux_iosd-universalk9-ms_14778_20230201-141137-EST.core.gz) = 7da52742d367a959351944
d7ed020472ca30462cda214457fec3e860528e18a2c43bf0e69d557a5d172d9a8d66356526c3f1b72af5ee857f6b95c9718e67c8f0

Router1#copy bootflash:/Router1_ crashinf_20230201-141134-EST ftp:
     
Address or name of remote host []? 192.168.1.1
Destination filename [Router1_crashinf_20230201-141134-EST]? 
Writing Router1_crashinf_20230201-141134-EST !
220651 bytes copied in 4.675 secs (47198 bytes/sec)

Router1#copy bootflash:/core/Router1_RP_0_x86_64_crb_linux_iosd-universalk9-ms_14778_20230201-141137-EST.core.gz ftp:
  
Address or name of remote host []? 192.168.1.1
Destination filename [Router1_RP_0_x86_64_crb_linux_iosd-universalk9-ms_14778_20230201-141137-EST.core.gz]? 
Writing Router1_RP_0_x86_64_crb_linux_iosd-universalk9-ms_14778_20230201-141137-EST.core.gz !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
38893484 bytes copied in 5.830 secs (6671267 bytes/sec)
Router1#
```

The final step in this section is to unconfigure service internal :

```
configure terminal
no service internal
end
```

Submit all command output collected in this section to the relevant TAC SR.

## Acknowledgments

The author would like to thank all members of the Customer Experience Security Programs (CXSP) and Advanced Security Initiatives Group (ASIG) who provided their expertise for this document. A special note of thanks to Xavier Brouckaert of ASIG whose contributions greatly enhanced the efficacy of the forensic procedures contained in this publication.

## Related Documentation

Additional information about the procedures contained in this document, as well as forensic data collection procedures for other platforms, can be found at the following link:

https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## Cisco IOS XE Device Forensic Response Checklist

Step 1 – Create the Cisco IOS XE Device Problem Description

Device Problem Description uploaded to SR

Step 2 – Document the Cisco IOS XE Runtime Environment

Output of show tech-support uploaded to SR

Output of process & integrity show commands uploaded to SR

All system shell log files uploaded to SR

Step 3 – Cisco IOS XE Image File Hash Verification

Output of verify on system image files uploaded to SR

Copy of the running system image file uploaded to SR

Image files with hash inconsistencies uploaded to SR

Step 4 – Verify Digitally Signed Image Authenticity

Output of show software authenticity file uploaded to SR

Output of show software authenticity running uploaded to SR

Step 5 – Text Memory Section Export

Output of verify /md5 system:memory/text uploaded to SR

Output of copy system:memory/text uploaded to SR

Step 6 – Core File Generation

Output  of verify /sha512 on core file uploaded to SR

Core  file uploaded to SR

Output  of verify /sha512 on crashinfo file uploaded to SR

Crashinfo  file uploaded to SR

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
| 1.0 | 8/19/2019 | Dan Maunz | Initial public release. |
| 1.1 | 11/22/2021 | Dan Maunz | Added container enumeration. |
| 1.2 | 10/21/2022 | Dan Maunz | Validated procedure on Release 17.03.05. |
| 1.3 | 02/02/2023 | Dan Maunz | Added core file procedure. |
| 1.4 | 02/27/2024 | Dan Maunz | Simplified procedures and validated on Release 17.03.08. |
| 1.5 | 12/09/2024 | Dan Maunz | Moved core procedure to new Step Six. |
| 1.6 | 03/21/2025 | Dan Maunz | Validated procedures on Release 17.12.04. |
| 1.7 | 04/14/2026 | Dan Maunz | Refined several procedures. |