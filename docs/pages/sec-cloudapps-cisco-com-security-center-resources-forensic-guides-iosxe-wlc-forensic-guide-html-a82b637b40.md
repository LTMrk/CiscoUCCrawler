---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-iosxe-wlc-forensic-guide-html-a82b637b40
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/iosxe_wlc_forensic_guide.html
retrieved_at: 2026-09-01T14:10:50.250780+00:00
---

Home / Cisco Security

Cisco IOS XE Software for Wireless Controllers Forensic Data Collection Procedures

# Cisco IOS XE Software for Wireless Controllers Forensic Data Collection Procedures

Introduction

Prerequisites

Step One – Cisco WLC Platform Problem Description

Step Two – Document the Cisco IOS XE Runtime Environment

Step Three – Cisco IOS XE Image File Hash Verification

Step Four – Verify Digitally Signed Image Authenticity

Step Five – Text Memory Section Export

Step Six – Core File Generation

Related Documentation

Cisco IOS XE Device Forensic Response Checklist

Revision History

## Introduction

This document provides guidance for collecting evidence from Cisco Wireless Lan Controller (WLC) platforms that are suspected of compromise or tampering. It outlines a number of commands that can be run to gather evidence for an investigation along with the respective output that should be collected upon running these commands. This document also provides information on how to perform integrity checks on device images and includes a procedure for collecting the text memory segment so that the run-time integrity of the IOSd process can be ascertained.

Important: Do not reboot a network device when triaging for compromise or tampering. Rebooting a device during an initial assessment will irrecoverably lose all volatile information that is contained within the device (for example, RAM contents, arp and routing tables, NAT translations, ACL hit and drop counts, etc.).

Note: It is highly recommended that a device suspected of tampering or compromise be isolated from the network prior to conducting an initial forensic examination. This may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device under investigation.

If you require assistance or have questions regarding the procedures described in this document, contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains six main sections:

- Cisco WLC Platform Problem Description – Describes why the platform is a candidate for forensic examination

- Cisco WLC Runtime Environment – Collects platform configuration and runtime state

- Cisco WLC Image File Verification – Examines system image hashes for inconsistencies

- Digitally Signed Image Verification – Examines system and running images for proper signing characteristics

- Text Memory Section Export – Collects the information necessary to verify the runtime integrity of the IOSd process

- Core File Generation – Obtains a complete copy of platform memory

## Prerequisites

The procedures outlined in this document assume that the reader has a basic understanding of Cisco IOS XE Software for Wireless Controllers command syntax.

A valid cisco.com account is required to view individual Cisco IOS XE file hashes for software file integrity checking. A publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded from: https://www.cisco.com/c/en/us/about/trust-center/downloads.html

A Cisco Technical Assistance Center (TAC) service request (SR) for the device in question is required because these procedures assume that the information gathered in each step will be uploaded to a TAC SR.

Note: The examples that are used in this document are based on Cisco IOS XE Software for Wireless Controllers Release 17.15.03 command syntax. The output produced by a command may vary depending on the software release that is deployed and/or the features that are supported or configured on the device. Not all commands used in these procedures may be supported on earlier versions of the software.

Important: The commands and procedures contained in this document are not supported on the older AireOS-based line of Cisco Wireless Lan Controller platforms and, therefore, cannot be executed.

## Step One – Cisco WLC Platform Problem Description

Describe in as much detail as possible why the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior than cannot be attributed to a misconfiguration or a software/hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific software releases of the following products: Cisco ASA, FMC, FTD, FXOS, IOS, IOS XE, NX-OS, and NX-OS in ACI Mode.

https://sec.cloudapps.cisco.com/security/center/softwarechecker.x

Record any results returned by the tool that may explain the anomalous behavior being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA, FMC, FTD, and FXOS Software, the tool contains only vulnerability information for Cisco Security Advisories first published from January 2022 onward, and for Cisco NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Submit the problem description and any relevant results obtained from the Cisco Software Checker collected in this section to the relevant Cisco Technical Assistance Center (TAC) Service Request (SR) and proceed to the next section of this document.

## Step Two – Document the Cisco IOS XE Runtime Environment

Complete the initial stage of evidence gathering by issuing a number of show and dir commands. These commands must be executed in enable mode (also called privileged EXEC mode), and some of the output may vary depending on the particular Cisco WLC hardware platform, software release, and/or configured features.

Execute each of the following commands in enable mode and record the output:

```
terminal length 0
show tech-support
show tech-support wireless
show tech-support diagnostic
dir /recursive all-filesystems
```

Note: The output from the show tech-support command may be redirected to the local file system or a server running any of the following protocols: FTP, HTTP, HTTPS, or TFTP.

The following example depicts the use of the FTP protocol:

```
WLC-9800#show tech-support | redirect ftp://anonymous@172.16.0.2/show-tech.txt
```

```
!! Enumerate app hosting environment
show iox
show app-hosting list
!! WLC process and integrity information
show platform software process memory chassis active r0 name linux_iosd-imag maps
!! The following command may take several minutes, or longer to complete
show platform software process memory chassis active r0 name iosd smaps [1] show platform integrity sign nonce 12345
!! Obtain a copy of all trace log files
request platform software trace archive
```

Submit all command output, the tech support files, and the trace log archive to the relevant TAC SR, and proceed to the next section of this document.

[1] This procedure checks the active chassis route processor (R0) for non-zero values in the Private Dirty entry for each segment with the executable flag set (in other words, r-xp or rwxp).

Executable segments of a program typically have the r-xp (read, execute, protected) attributes set, while an executable segment with the w (write) attribute set may indicate the software has been tampered with.

### Example 1

```
#
# This segment is flagged rw-p (read, write, protected) so a private
# dirty value greater than zero is expected and not of concern. 
#
WLC-9800# show platform software process memory chassis active r0 name iosd smaps smaps for process 7438:
address          perms offset   dev   inode      pathname
5d08b11a8000-5d08b518d000 rw-p 19ba5000 07:00 11704                      
Size:              65428 kB
KernelPageSize:        4 kB
MMUPageSize:           4 kB
Rss:               61928 kB
Pss:               61928 kB
Shared_Clean:          0 kB
Shared_Dirty:          0 kB
Private_Clean:      6044 kB Private_Dirty:     55884 kB Referenced:        61928 kB
Anonymous:         55884 kB
LazyFree:              0 kB
AnonHugePages:         0 kB
ShmemPmdMapped:        0 kB
FilePmdMapped:         0 kB
Shared_Hugetlb:        0 kB
Private_Hugetlb:       0 kB
Swap:                  0 kB
SwapPss:               0 kB
Locked:                0 kB
THPeligible:    0
VmFlags: rd wr mr mw me ac
[output truncated]
```

### Example 2

```
#
# This segment is flagged rwxp (read, write, execute, protected) and
# private dirty has a value greater than zero which may indicate the
# software has been tampered with. 
#
WLC-9800# show platform software process memory chassis active r0 name iosd smaps smaps for process 6412:
address          perms offset   dev   inode      pathname
70feac6ef000-70feac75d000 rwxp 007d5000 07:00 23264
Size:                440 kB
KernelPageSize:        4 kB
MMUPageSize:           4 kB
Rss:                 432 kB
Pss:                 432 kB
Shared_Clean:          0 kB
Shared_Dirty:          0 kB
Private_Clean:         0 kB Private_Dirty:       432 kB Referenced:          432 kB
Anonymous:           432 kB
LazyFree:              0 kB
AnonHugePages:         0 kB
ShmemPmdMapped:        0 kB
FilePmdMapped:         0 kB
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

Access the command line of the Cisco WLC device and issue the following command in enable mode:

```
show version | inc System image
```

Note the location and filename of the system image file obtained and execute the following command:

```
more location:filename
```

Next, issue the following command for the packages.conf image file, and each unique entry listed in the contents of the packages.conf image file:

```
verify location:filename
```

An example of this procedure follows:

```
WLC-9800# show version | inc System image System image file is "bootflash:packages.conf"

WLC-9800#more bootflash:packages.conf
#! /usr/binos/bin/packages_conf.sh
sha1sum: 1d206d5536d48eee6c79e11aa9a7f0f7b9fda874
# sha1sum above - used to verify that this file is not corrupted.
#
# package.conf: provisioned software file for build 2024-11-21_00.33
#
# NOTE: The text and comments contained in this file have been omitted for    
# brevity. 
#
boot  rp 0 0   rp_boot C9800-L-rpboot.V1712_4_ESW13.SPA.pkg iso   rp 0 0   rp_base C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg iso   rp 0 1   rp_base     C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 0   rp_daemons  C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 1   rp_daemons  C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 0   rp_iosd     C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 1   rp_iosd     C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 0   rp_security C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 1   rp_security C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 0   rp_webui    C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 1   rp_webui    C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 0   rp_wlc      C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   rp 0 1   rp_wlc      C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg       
iso   fp 0 0   fp          C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   cc 0 0   cc          C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   cc 0 0   cc_spa      C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   cc 0 1   cc_spa      C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   cc 0 2   cc_spa      C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
iso   cc 0 3   cc_spa      C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
[output truncated]

WLC-9800# verify bootflash:packages.conf bootflash:packages.conf is detected as a provisioning file
Verifying file integrity of bootflash:packages.conf.. Embedded Hash   SHA1 : 1D206D5536D48EEE6C79E11AA9A7F0F7B9FDA874 Computed Hash   SHA1 : 1D206D5536D48EEE6C79E11AA9A7F0F7B9FDA874 # Note: In this example, packages.conf contains only two unique file entries:
# C9800-L-rpboot.V1712_4_ESW13.SPA.pkg
# C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
# Therefore, the verification command need only be run twice, once on each of these two files.

WLC-9800# verify bootflash:C9800-L-rpboot.V1712_4_ESW13.SPA.pkg Verifying file integrity of bootflash:C9800-L-rpboot.V1712_4_ESW13.SPA.pkg 
...........................................................................
[output truncated]
...........................................................................
...........................................................................
Embedded Hash   SHA1 : 58399C2563376C5741790570E0C463C02F001B7D
Computed Hash   SHA1 : 58399C2563376C5741790570E0C463C02F001B7D
Starting image verification
Hash Computation:    100%Done!
Computed Hash   SHA2: 39251a15f8b81046f87085857672c70a
                      faecd5d70f1c32c86a38b1143a58e50b
                      b596158c08f7c65c37a006dd498c5e34
                      56f89398123786db481298e08538d212
                      
Embedded Hash   SHA2: 39251a15f8b81046f87085857672c70a
                      faecd5d70f1c32c86a38b1143a58e50b
                      b596158c08f7c65c37a006dd498c5e34
                      56f89398123786db481298e08538d212 Digital signature successfully verified in file bootflash:C9800-L-rpboot.V1712_4_ESW13.SPA.pkg WLC-9800# verify bootflash:C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg Verifying file integrity of bootflash:C9800-L-mono-universalk9_wlc.V1712_4 _ESW13.SPA.pkg 
...........................................................................
[output truncated]
...........................................................................
...........................................................................
Embedded Hash   SHA1 : A8D03E02C592C3BBC8E63F9BB34B9C9F85CEEE22
Computed Hash   SHA1 : A8D03E02C592C3BBC8E63F9BB34B9C9F85CEEE22
Starting image verification
Hash Computation:    100%Done!
Computed Hash   SHA2: 17f48d46e17e7e665df7d74419851258
                      93ad6976af5b9726b7d956a49ebc68ec
                      515e6af873e58599778ef2c7d9f1ef2e
                      463794c4c45028674ad99bfe8e7f445e
                      
Embedded Hash   SHA2: 17f48d46e17e7e665df7d74419851258
                      93ad6976af5b9726b7d956a49ebc68ec
                      515e6af873e58599778ef2c7d9f1ef2e
                      463794c4c45028674ad99bfe8e7f445e Digital signature successfully verified in file bootflash:C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
```

Note that the embedded hash and computed hash should return the same SHA1 (160 bit) and SHA2 (256 bit) values.

A SHA-512 hash can be calculated by adding the /sha512 parameter to the verify command as follows:

```
verify /sha512 location:filename
```

An MD5 hash can also be calculated by adding the /md5 parameter to the verify command as follows:

```
verify /md5 location:filename
```

The SHA-512 or MD5 hashes should match the values listed on CCO or in the Bulk Hash File for that particular image file.

Note: CCO contains only MD5 and SHA-512 hash values for software images.

If any of the image file hashes show inconsistencies, copy the image file in question to a secure location if possible.

```
copy < Location >:< system_image_filename.bin > ftp: 
Address or name of remote host []? < destination_ip >
Destination filename []? < destination_filename.bin >
```

It is highly recommended that a hash value be calculated on the copied system image file and compared to the hash value obtained on the platform to ensure no errors were introduced during the file transfer process.

Submit all command output (including calculated hash values), the running system image, and any other system images tested in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Four – Verify Digitally Signed Image Authenticity

Cisco IOS XE Software implements digitally signed system images on most platforms. Digitally signed Cisco software uses asymmetric (public-key) cryptography, which increases the security posture of devices that are running Cisco IOS XE Software by ensuring that the software running on the system has not been altered and that the software originates from a trusted source.

Run the command more packages.conf to identify the individual software packages that comprise the boot image, and use those filenames as input to the show software authenticity file command. Software packages may be loaded multiple times by packages.conf , but the file verification procedure need only be run once per unique filename.

The authenticity and integrity of a system image file can be verified by using the following command:

```
show software authenticity file Location:filename
```

An example of this procedure follows:

```
WLC-9800# show software authenticity file bootflash:C9800-L-rpboot.V1712_4_ESW13.SPA.pkg File Name                     : bootflash:C9800-L-rpboot.V1712_4_ESW13.SPA.pkg
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : EWLC Organization Name     : CiscoSystems Certificate Serial Number : 673F86FE
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

WLC-9800# show software authenticity file bootflash:C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg File Name                     : bootflash:C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : EWLC Organization Name     : CiscoSystems Certificate Serial Number : 673F86DB Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The Organization Unit, Organization Name, and the Certificate Serial Number values can be viewed to verify that the system image signature is valid.

It is also important to verify the authenticity and integrity of the running system image, and this can be accomplished with the following command:

```
show software authenticity running
```

An example of this procedure follows:

```
WLC-9800# show software authenticity running PACKAGE C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
------------------------------------------------------------
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : EWLC Organization Name     : CiscoSystems Certificate Serial Number : 673F86DB Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : mono
        Verifier Version      : V1712_4_ESW13

SYSTEM IMAGE
------------
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : EWLC Organization Name     : CiscoSystems Certificate Serial Number : 673F86FE Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : ROMMON
        Verifier Version      : System Bootstrap, Version 15.12(3r)

ROMMON
------
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : AIR-CT9510_LDWM
        Organization Name     : CiscoSystems
    Certificate Serial Number : 5da8372600000018
    Hash Algorithm            : SHA256
    Signature Algorithm       : LDWM
    Key Type                  : REL
    LDWM Algorithm            : SHA256_TRUNC_8
    LDWM Signature Type       : SIGNATURE_Y67
    LDWM W Parameter          : W_EIGHT
    LDWM MTS Parameter        : MTS_K4_H10
    LDWM APATH Parameter      : MTS_PATH_T30
    Verifier Information
        Verifier Name         : Microloader
        Verifier Version      : MA1011R06.1503172017
Microloader
-----------
Image type                    : Release
    Signer Information
        Common Name           : CiscoSystems
        Organization Name     : CiscoSystems
    Certificate Serial Number : 799aa79d17dce0264d94fe3d157383bb
    Hash Algorithm            : SHA256
    Signature Algorithm       : LDWM (m=20, w=4, k=4, h=10)
    Verifier Information
        Verifier Name         : Hardware Anchor
        Verifier Version      : R04.1173930452019-06-11
```

The Organization Unit, Organization Name, and the Certificate Serial Number values can be viewed to verify that the system image signature is valid, and the Certificate Serial Numbers should be the same as the values obtained from the show software authenticity file commands. In the previous examples, the authenticity check of the Cisco IOS XE Software image on the boot flash and the authenticity check of the running image both produce values of 673F86FE and 673F86DB.

Additional digital signature checks may also be accomplished with the following command:

```
show platform software authenticity verify Location:filename
```

Note: Some Cisco Wireless Controller platforms may require that service internal be configured prior to issuing the show platform software authenticity verify command.

An example follows:

```
WLC-9800# show platform software authenticity verify bootflash:C9800-L-rpboot. V1712_4 _ESW13.SPA.pkg Digital signature successfully verified in file bootflash:C9800-L-rpboot.V1712_4_ESW13.SPA.pkg WLC-9800# show platform software authenticity verify bootflash:C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg Digital signature successfully verified in file bootflash:C9800-L-mono-universalk9_wlc.V1712_4_ESW13.SPA.pkg
```

Lastly, obtain a copy of the public signing keys by executing the following command:

```
show software authenticity keys
```

An example of this procedure follows:

```
WLC-9800# show software authenticity keys Public Key #1 Information
-------------------------
Key Type                  : Production  (Primary)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        e2:9e:33:e2:68:f4:1a:fb:cc:4f:20:a6:c6:f1:ea:17:
        d4:7c:6c:5d:d1:02:f6:f8:8c:b5:4e:57:68:98:db:2b:
        de:ed:c5:dd:55:1f:ba:aa:98:ad:88:3d:e2:de:cf:08:
        a9:09:c3:55:75:c6:da:26:b6:7c:cf:47:bf:13:cb:f8:
        cd:c1:5f:e8:3c:b2:3c:ae:1c:3f:b5:34:57:f7:0a:cd:
        2a:b4:05:a3:d0:bb:2e:b7:15:7c:12:bf:57:61:0e:01:
        ad:a9:0b:bc:e4:14:6d:43:f9:ae:88:43:a6:a8:76:ca:
        08:28:39:4c:5f:58:3c:75:29:f0:18:2f:f8:4e:28:6b:
        b3:42:b8:82:2a:b5:04:a4:5b:5d:f0:a6:9e:01:db:73:
        dc:97:4f:b7:a9:e3:33:54:c8:08:15:c0:4e:39:4e:09:
        c5:51:6b:eb:81:98:f9:22:7f:f3:1d:d6:2a:63:51:f6:
        95:ed:d2:fb:5c:a6:d0:bd:c9:e9:52:4e:b6:e8:f0:f4:
        af:6c:25:8b:e6:92:f3:a5:23:35:82:48:55:f3:7c:3c:
        5d:5a:02:45:f5:58:eb:f3:90:d4:29:b0:b8:8c:ed:36:
        c8:cc:56:a6:ae:c8:84:56:bb:45:de:2f:1e:86:a8:33:
        aa:66:12:4c:4a:07:03:03:d6:ad:8d:2d:82:37:bd:b5
Exponent (3 bytes)   : 10001
Key Version          : A
Product Name         : EWLC
[output truncated]
```

Submit all command output collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Five – Text Memory Section Export

This section outlines the procedure to collect the system:memory/text region to verify the run-time integrity of the IOSd process from a device that is running Cisco IOS XE Software.

Note: This procedure requires a minimum of Cisco IOS XE Software Release 15.5.1 or later. The text region in earlier releases may point to the text section of a shared library instead of the executable code of the IOSd process.

Access the CLI of the Cisco Wireless Controller and issue the following command in enable mode to view the system:memory/text entry:

```
dir system:memory/text
```

Copy the system:memory/text region to a file server using ftp or scp.

```
copy system:memory/text ftp:
```

An example of this procedure follows:

```
WLC-9800# dir system:memory/text Directory of system:memory/text
5       -r--        285813101 <no date>  text No space information available

WLC-9800# copy system:memory/text ftp: Address or name of remote host []? 172.16.0.2
Destination filename [text]? wlc-9800-text.bin
Writing wlc-9800-text.bin !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[output omitted]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
285813101 bytes copied in 9.701 secs (29462231 bytes/sec)
```

It is highly recommended that hash values be calculated for the device system:memory/text region and for the file that was copied to the file server to ensure that no errors were introduced during the file transfer process.

To calculate a hash value for the system:memory/text region, execute the following command:

```
verify /md5 system:memory/text
```

An example of this procedure is depicted below:

```
WLC-9800# verify /md5 system:memory/text ............................................................................................................................................................
[output omitted]
.......................................................................................................................................................Done!
verify /md5 (system:memory/text) = ce1eec8ada35e22a130888517f7db019
```

Next, calculate a hash value for the file transferred to the file server.  A MD5 hash value can be calculated with the md5sum utility, which is included with most Linux distributions.

```
root@ftp-server:~# md5sum wlc-9800-text.bin
ce1eec8ada35e22a130888517f7db019 wlc-9800-text.bin root@ftp-server:~#
```

Note that the IOS XE verify command and the md5sum utility both produce an MD5 hash value of ce1eec8ada35e22a130888517f7db019.

Submit all command output (including calculated hash values) and the file containing the system:memory/text output to the relevant TAC SR and proceed to the next section of this document.

## Step Six – Core File Generation

This procedure outlines how to configure a Cisco Wireless Controller to obtain a core dump of platform memory. A crash information file is created in the root of the bootflash filesystem, and the core file is created in the bootflash:/core subdirectory.

Caution: This section contains commands that alter the configuration of the wireless controller, and that may cause the platform to reboot. It is of critical importance that all the preceding information-gathering steps have been completed successfully or important evidence may be permanently lost . Creating core dumps may also cause spikes in memory consumption and momentary disruptions to traffic that is transiting the device if a standby wireless controller has not been deployed in the environment.

The steps to acquire a core dump of the IOSd process are as follows:

```
conf t
service internal
show platform software process environment ios chassis active r0
request platform software process core ios chassis active r0
```

An example of the procedure to acquire a crash info file and core dump file follows:

```
WLC-9800# conf t Enter configuration commands, one per line.  End with CNTL/Z.
WLC-9800(config)# service internal WLC-9800(config)# end WLC-9800#
Apr 2 10:44:33.151: %SYS-5-CONFIG_I: Configured from console by console

WLC-9800# show platform software process environment ios chassis active r0 Name                            Value                                           
------------------------------------------------------------------------------
CPP_CONF_DIR                    /usr/cpp/conf                                   
SLOT                            0                                               
SHELL                           /bin/bash                                       
ROMMON_CHASSIS_HA_REMOTE_IP     0.0.0.0                                         
PROF_DIR                        /harddisk                                       
BOARD_SUBTYPE                   KATAR                                           
BINOS_CHASSIS_XML               /usr/binos/conf/chassis.xml                     
ROMMON_RET_2_RTS                10:18:06 Eastern Tue Apr 1 2025                 
BINOS_SLOT                      0                                               
ALL_BINARIES                    cpp_cp, wncd, wncmgrd, mobilityd, rrm, rogued,  
SW_FRU_BASE                     /tmp/sw/rp/0/0/rp_wlc/mount                     
PROCESS_SCOREBOARD_DIR          /tmp/rp/process/linux_iosd_image%rp_0_0%0       
BINOS_CMRP_IMAGE_ROOT           /tftp                                           
BINOS_ROOT                      /nobackup/mcpre/s2c-build-ws/binos              
ROMMON_CHASSIS_HA_LOCAL_MASK    0.0.0.0                                         
BINOS_CONF_DIR                  /usr/binos/conf                                 
SAI_ENABLED                     1                                               
WIRELESS_BINARIES               cpp_cp, wncd, wncmgrd, mobilityd, rrm, rogued,  
STORAGE_TARGET                  /bootflash                                      
BINOS_BTRACE_LEVEL              NOTICE                                          
BINOS_BASE_DIR                  /tmp/rp                                         
BINOS_NVRAM_DIR                 /config                                         
CHASSIS_CONTROLLER_TRIGGER      /tmp/chassis/local/controller_launch            
CC_COUNT                        1                                               
BOARD_TYPE                      RP                                              
BINOS_SLOT_LOCAL                0                                               
BINOS_FRU_BASE_PKG              rp_base                                         
PROC_SCOREBOARD_BKTRACE_FILE    /tmp/rp/process/linux_iosd_image%rp_0_0%0/linu
[output truncated]

WLC-9800# request platform software process core ios chassis active R0 SUCCESS: Core file generated.
WLC-9800#

Exception to IOS Thread:
Frame pointer 0x7FFE886F5308, PC = 0x70FEBEAC26D2

UNIX-EXT-SIGNAL: Aborted(6), Process = Sched
-Traceback= 1#db1ddb099741ed1ce69f6548bd2aa3a4 c:70FEBEA86000+3C6D2 c:70FEBEA86000+2656B uipeer:70FEEF676000+49D2E uipeer:70FEEF676000+667DC cdllib_pi:70FED6644000+324117 cdllib_pi:70FED6644000+8DD06 cdlcore:70FEEF61D000+21A46 cdlcore:70FEEF61D000+21834 cdlcore:70FEEF61D000+27D5D cdlcore:70FEEF61D000+27B0C uipeer:70FEEF676000+2BF41 evutil:70FED65AF000+789A evutil:70FED65AF000+76C4 evlib:70FED65C3000+8DE7 iosd_crb_qwlc_unix:70FEEF721000+82957 :5D0897602000+9C81F56 

RAX = 0000000000000000  RBX = 000070FEA491D500
RCX = 000070FEBEAC26D2  RDX = 0000000000000000
RSP = 00007FFE886F5308  RBP = 00007FFE886F5390
RSI = 00007FFE886F5290  RDI = 0000000000000002
R8  = 0000000000000000  R9  = 00007FFE886F5290
R10 = 0000000000000008  R11 = 0000000000000246
R12 = 0000000000000195  R13 = 000070FEA4919E70
R14 = 00005D08BB191018  R15 = 00005D08BB5BB198
RFL = 0000000000000246  RIP = 000070FEBEAC26D2
CS = 0033  FS = 0000  GS = 0000
ST0 = 0000 0000000000000000  ST1 = 0000 0000000000000000
ST2 = 0000 0000000000000000  ST3 = 0000 0000000000000000
ST4 = 0000 0000000000000000  ST5 = 3FE8 8000000000000000
ST6 = 0000 0000000000000000  ST7 = 0000 0000000000000000
X87CW = 037F  X87SW = 0000  X87TG = 0000  X87OP = 0000
X87IP = 000070FED649E156  X87DP = 000070FED64B3120
XMM0  = FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
XMM1  = 5345545F43494D414E59440065757274
XMM2  = FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
XMM3  = 505F434C00534547415353454D5F434C
XMM4  = 0000000000000000B879F3B1085D0080
XMM5  = 00000000000000000000000000000000
XMM6  = 303937355F31305F30305F31305F3130
XMM7  = 00000000000000000000000000000000
XMM8  = 42206E61556C43202C64656B726F6620
XMM9  = 00000000000000000000000000000000
XMM10 = 00000000000000000000000000000000
XMM11 = 00000000000000000000001C0000001C
XMM12 = 4538453A444041373C4043393B434339
XMM13 = 00310033003900303539003234000032
XMM14 = 000000000000005E000000000000005C
XMM15 = 00000000000000200000000000000020
MXCSR = 00001F80

Writing crashinfo to bootflash:WLC-9800_crashinfo_RP_00_00_20250402-104847-Eastern
Buffered messages: (last 4096 bytes only)

WLC-9800# verify /sha512 bootflash:WLC-9800_crashinfo_RP_00_00_20250402-104847-Eastern ....Done!
verify /sha512 (bootflash:WLC-9800_crashinfo_RP_00_00_20250402-104847-Eastern) = 9b8108e395477d8193b261e6fcde5bfb3de13fb7e15ebe2e2aeaa4a185713cf12b0a13b2a7e5 bcf40844ee913ffefb60b85434b49b6b45d079e52a34406a7b46

WLC-9800#dir bootflash:/core
Directory of bootflash:/core/

179875  -rw-   57994348 Apr 2 2025 10:49:19 +00:00  WLC-9800_1_RP_0_x86_64_crb _linux_iosd_qwlc-universalk9_wlc-ms_4971_20250402-104850-Eastern.core.gz
179874  -rw-   1        Apr 2 2025 10:48:42 +00:00  .callhome
188049  drwx   4096     Jan 8 2017 11:21:19 +00:00  modules

WLC-9800# verify /sha512 bootflash:/core/WLC-9800_1_RP_0_x86_64_crb_linux_iosd _qwlc-universalk9_wlc-ms_4971_20250402-104850-Eastern.core.gz ............................................................................................................................................................[output omitted] .......................................................................................................................................................Done!
verify /sha512 (bootflash:/core/WLC-9800_1_RP_0_x86_64_crb_linux_iosd_qwlc-universalk9_wlc-ms_4971_20250402-104850-Eastern.core.gz) = 6eaa5fdbc4a355bd2e1ac119df853e3eab852b6778de32531978836bf88c9a525405fbc670a22f44f1fe6c09157f15bde2bf0c8502b595c0b296eba5c0b33115

WLC-9800# copy bootflash:/WLC-9800_crashinfo_RP_00_00_20250402-104847-Eastern ftp: Address or name of remote host []? 172.16.0.2
Destination filename [WLC-9800_crashinfo_RP_00_00_20250402-104847-Eastern]? 
Writing WLC-9800_crashinfo_RP_00_00_20250402-104847-Eastern !
229755 bytes copied in 0.092 secs (2497337 bytes/sec)

WLC-9800# copy bootflash:/core/ WLC-9800_1_RP_0_x86_64_crb_linux_iosd_qwlc-universalk9_wlc-ms_4971_20250402-104850-Eastern.core.gz ftp: Address or name of remote host []? 172.16.0.2
Destination filename [WLC-9800_1_RP_0_x86_64_crb_linux_iosd_qwlc-universalk9_wlc-ms_4971_20250402-104850-Eastern.core.gz]? 
Writing WLC-9800_1_RP_0_x86_64_crb_linux_iosd_qwlc-universalk9_wlc-ms_4971_20250402-104850-Eastern.core.gz !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
57994348 bytes copied in 3.417 secs (15972300 bytes/sec)
```

Submit all command output (including calculated hash values) and the file that contains the system:memory/text output to the relevant TAC SR.

## Related Documentation

Additional information about the procedures contained in this document, as well as forensic data collection procedures for other platforms, can be found at the following link:

https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## Cisco WLC Software Forensic Response Checklist

Step 1 – Create the Cisco WLC Device Problem Description

Device Problem Description uploaded to SR

Step 2 – Document the Cisco WLC Runtime Environment

Output of show tech-support uploaded to SR

Output of show tech-support wireless uploaded to SR

Output of show tech-support diagnostic uploaded to SR

Output of process and integrity show commands uploaded to SR

Trace log archive file uploaded to SR

Step 3 – Cisco WLC Image File Hash Verification

Output of verify on system image files uploaded to SR

Step 4 – Verify Digitally Signed Image Authenticity

Output of show software authenticity file uploaded to SR

Output of show software authenticity running uploaded to SR

Output of show software authenticity keys uploaded to SR

Step 5 – Text Memory Section Export

Output of copy system:memory/text uploaded to SR

Output of verify /md5 system:memory/text uploaded to SR

Step 6 – Core File Generation

Output  of verify /sha512 on core file uploaded to SR

Core  file uploaded to SR

Output of verify /sha512 on crashinfo file uploaded to SR

Crashinfo file uploaded to SR

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

| Version | Date | Author | Comments |
|---|---|---|---|
| 1.0 | 4/25/2025 | Dan Maunz | Initial public release. |
| 1.1 | 10/22/2025 | Dan Maunz | Validated procedures on Release 17.15.03. |