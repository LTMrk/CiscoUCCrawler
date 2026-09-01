---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-ios-forensic-investigation-html-35d4d9c64b
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/ios_forensic_investigation.html
retrieved_at: 2026-09-01T14:10:41.397429+00:00
---

Home / Cisco Security

Cisco IOS Software Forensic Data Collection Procedures

# Cisco IOS Software Forensic Data Collection Procedures

Introduction

Prerequisites

Step One - IOS Device Problem Description

Step Two - IOS Runtime Environment

Step Three - IOS Image File Verification

Step Four - Verify Digitally Signed Image Authenticity

Step Five - Text Memory Region Analysis

Step Six - Core File/Memory Dump

Step Seven -  ROMMON Upgrade Check

Related Documentation

IOS Device Forensic Report Checklist

Revision History

## Introduction

This document provides guidance for collecting forensic evidence from devices running Cisco IOS Software that are suspected of having been compromised or tampered with. The document outlines a number of commands that can be run to gather evidence for an investigation, along with the respective output that should be collected upon running these commands. This document also provides information on how to perform integrity checks on a device’s IOS Software images, how to collect a core file/memory dump from a device running Cisco IOS Software, and how to check to see if a ROMMON upgrade has been applied.

IMPORTANT: It is extrememly important when triaging a network device for compromise or tampering that it is not rebooted. Rebooting a device during an initial assessment will irrecoverably lose all volatile information contained within the device (e.g., RAM contents, arp and routing tables, NAT translations, ACL hit and drop counts, etc.).

Note: It is highly recommended that a device suspected of tampering or compromise be isolated from the network prior to conducting an initial forensic examination. This may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device under investigation.

Note: The  examples used in this document are based on Cisco IOS Software Release 15.9(3)M12 command syntax. The output produced by a command may vary depending on the  software version deployed and/or the features supported or configured on the  device. Not all commands used in these procedures may be supported on earlier  versions of the software.

If you require assistance or have questions regarding the following procedures, contact the Cisco Product Security Incident Response Team (PSIRT) .

The main section of this document contains the following sections:

1. IOS Device Problem Description – describes why the platform is a candidate for forensic examination

2. IOS Runtime Environment – collects platform configuration and runtime state

3. IOS Image File Verification – examines system image hashes for inconsistencies

4. Verify Digitally Signed Image Authenticity – examines system and running images for proper signing characteristics

5. Text Memory Region Analysis – provides an alternate method of analysis if a core dump cannot be performed

6. Core File/Memory Dump – obtains a core dump of the running IOS image and contents of memory

7. ROMMON Upgrade Check – examines the ROM monitor region for an upgraded image

## Prerequisites

The procedures described in this document assume the reader has a basic understanding of Cisco IOS Software command syntax.

A valid cisco.com account is required to view individual IOS Software and ROMMON firmware file hashes for software file integrity checking. For customers without a cisco.com account, a publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded from: https://www.cisco.com/c/en/us/about/trust-center/downloads.html

A Cisco Technical Assistance Center (TAC) service request (SR) is required for the device in question as the procedures outlined in this document assume that the information gathered in each step will be uploaded to a TAC SR.

## Step One – IOS Device Problem Description

Describe in as much detail as possible WHY the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior that cannot be attributed to a misconfiguration or a software or hardware defect? Are there any typical device administration commands that  are now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific software releases of the following products: Cisco ASA, FMC, FTD, FXOS, IOS, IOS XE, NX-OS, and NX-OS in ACI Mode.

https://sec.cloudapps.cisco.com/security/center/softwarechecker.x

Record any results returned by the tool that may explain the anomalous behavior being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA, FMC, FTD, and FXOS Software, the tool only contains vulnerability information for Cisco Security Advisories first published from January 2022 onward, and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Submit the problem description collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Two – Document the IOS Runtime Environment

The initial stage of evidence gathering is completed by issuing a show tech-support command and a dir all-filesystems command. These commands must be executed in enable mode (i.e., privileged EXEC mode), and some of the output produced may vary dependent on the particular IOS Software version and/or configured features.

Execute each of the following commands in enable mode and record the output:

```
enable
show platform versions
show tech-support
dir /recursive all-filesystems
```

Note: The output from the previous commands may also be redirected to the local file system or a server running any of the following protocols: FTP, HTTP/S, or TFTP with the following command syntax:

```
show tech-support | redirect <destination>
dir /recursive all-filesystems | redirect <destination>
```

Protocols supported by the redirect directive are FTP, HTTP/S, and TFTP.

An example of this command using the FTP protocol follows:

```
Router1#show tech-support | redirect ftp://admin:mypassword@10.10.10.1/show-tech.txt
Writing show-tech.txt..
Router1#
```

Submit all command output that is collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Three – IOS Image File Hash Verification

Access the command line of the Cisco IOS device and issue the following command in enable mode:

```
show version | inc image
```

Note the location and filename of the system image file and then execute the following command:

```
verify location:filename
```

Note: Comparing the embedded image hash with a calculated hash is only supported on digitally signed Cisco software, which can be identified by a three-character extension in the image name, typically “SPA”. A hashing algorithm parameter (either /md5 or /sha512) must be specified with the verify command for non-digitally signed Cisco software.

An example of this procedure follows:

```
Router1#show version | include image                      
System image file is "flash:c800-universalk9-mz.SPA.159-3.M12.bin"

Router1#verify flash:c800-universalk9-mz.SPA.159-3.M12.bin
Starting image verification
Hash Computation:    100% Done!
Computed Hash   SHA2: CAD6B6BDA9D63BF1C24BC4699B1B21EB
                      E0D67D28EF8BF793817D3C0D4E40FA95
                      22E47C1337F74FC0E0C579439CC0EC3F
                      DEE084566D11222EA36B889EBC966000
                      
Embedded Hash   SHA2: CAD6B6BDA9D63BF1C24BC4699B1B21EB
                      E0D67D28EF8BF793817D3C0D4E40FA95
                      22E47C1337F74FC0E0C579439CC0EC3F
                      DEE084566D11222EA36B889EBC966000
                      
CCO Hash        MD5 : BDA8EEF0652B129E84AD138E98549937
Digital signature successfully verified in file flash:c800-universalk9-mz.SPA.159-3.M12.bin
```

Note that the embedded hash and computed hash should return the same SHA2 value, and the CCO hash should match the MD5 value listed on CCO or in the Bulk Hash File for that particular image file.

Alternatively, to calculate an MD5 or SHA512 CCO hash directly, or to calculate a hash value for a non-digitally signed image, use the following command:

```
Router1#verify /md5 flash:c800-universalk9-mz.SPA.159-3.M12.bin
[output omitted]
MD5 of flash:c800-universalk9-mz.SPA.159-3.M12.bin Done!

verify /md5 (flash:c800-universalk9-mz.SPA.159-3.M12.bin) = bda8eef0652b129e84ad138e98549937
```

Repeat the above procedure for any other system image file located on the file systems. A comprehensive list of all files can be viewed by executing the following command:

```
dir /recursive all-filesystems
```

If any of the image file hashes show inconsistencies, copy the image file in question to a secure location if possible.

```
copy <location>:<system_image_filename.bin> ftp: 
Address or name of remote host []? <destination_ip>
Destination filename []? <destination_filename.bin>
```

It is highly recommended that a hash value be calculated on the copied system image file and compared to the hash value obtained on the platform to ensure no errors were introduced during the file transfer process.

Submit all command output and any system images collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Four – Verify Digitally Signed Image Authenticity

Some Cisco IOS platforms implement digitally signed system images. Digitally signed Cisco software uses asymmetric (public-key) cryptography that increases the security posture of Cisco IOS XE devices by ensuring that the software that is running on the system has not been altered and that the software originates from a trusted source.

Note: Older IOS platforms may not support the show software authenticity set of commands and will simply return an %Unrecognized command error.

The authenticity and integrity of a system image file can be verified by using the following command:

```
show software authenticity file location:filename
```

An example of this procedure follows:

```
Router1#show software authenticity file flash:c800-universalk9-mz.SPA.159-3.M12.bin   
File Name                     : flash:c800-universalk9-mz.SPA.159-3.M12.bin
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : C8xx
        Organization Name     : CiscoSystems
    Certificate Serial Number : 68CD837A
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The Organization Unit , Organization Name , and the Certificate Serial Number values can be viewed to verify that the system image signature is valid.

It is also important to verify the authenticity and integrity of the running system image, and this can be accomplished with the following command:

```
show software authenticity running
```

An example of this procedure follows:

```
Router1#show software authenticity running
SYSTEM IMAGE
------------
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : C8xx
        Organization Name     : CiscoSystems
    Certificate Serial Number : 68CD837A
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : ROMMON 1
        Verifier Version      : System Bootstrap, Version 15.5(1r)T, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
```

The Organization Unit , Organization Name , and the Certificate Serial Number values can be viewed to verify that the system image signature is valid, and the Certificate Serial Number should be the same as the value that is obtained from the show software authenticity file command. In the previous examples, the authenticity check of the IOS Software image on the boot flash and the authenticity check of the running image both produce a certificate serial number value of 68CD837A .

Lastly, obtain a copy of the public signing keys by executing the following command:

```
show software authenticity keys
```

An example of this procedure follows:

```
Router1#show software authenticity keys    
Public Key #1 Information
-------------------------
Key Type             : Production  (Primary)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        C8:AE:59:5E:E2:52:8C:64:55:6C:C6:AB:89:FA:56:53:
        06:2B:72:6D:18:A5:24:8A:37:35:BC:88:24:97:47:5D:
        93:76:D0:09:AF:16:EB:86:68:3B:66:CC:80:53:A8:ED:
        17:00:D1:F9:2D:15:0A:F2:29:BC:7E:9C:FF:85:31:C6:
        B1:5D:C7:44:A3:01:0E:D8:85:C9:12:77:61:AE:07:B3:
        E4:CA:84:AD:FC:C0:4E:E9:87:A2:4F:61:D4:93:C8:0F:
        37:D0:11:7F:B7:FB:92:EE:EB:91:56:F3:13:FA:E7:27:
        0E:57:4C:EE:F2:78:5A:62:6D:A9:C3:49:AC:96:A0:B8:
        E8:06:02:14:E0:2F:17:E3:6A:96:34:17:5A:B5:46:1C:
        AA:D1:F4:F6:3B:4D:4B:6E:1E:1A:09:45:95:44:B4:7C:
        85:AD:CB:C7:CE:0A:7D:4A:5D:F3:6B:1B:31:01:A8:78:
        BE:2D:A0:3E:33:1A:80:D3:29:4F:53:D8:66:CE:7D:AB:
        DF:AE:1A:D3:1D:61:D1:73:1F:01:FB:7D:02:3E:71:6C:
        1A:1E:4B:2D:D0:C3:E9:05:EB:57:D4:D0:A3:89:36:91:
        80:85:09:5A:0D:1A:71:31:D0:95:A9:2F:E6:2F:D2:E9:
        BA:A0:47:96:B0:D9:32:66:F5:34:35:51:36:E3:17:4D
Exponent (4 bytes)   : 10001
Key Version          : A
          
Public Key #2 Information
-------------------------
Key Type             : Special  (Primary)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        CE:BE:7A:25:8C:E4:45:79:5C:77:B8:1D:9E:94:78:61:
        B6:3D:64:4E:3C:36:25:11:9C:26:FF:D9:42:10:4C:86:
        F5:1C:AD:F1:49:A5:87:D3:4C:69:BF:08:E5:55:1C:59:
        CD:DA:62:9D:65:33:0D:B6:F1:F1:D1:AC:98:99:6B:CB:
        0B:3F:DA:E9:94:06:71:B3:78:B5:AA:85:C8:BE:64:CA:
        43:72:F2:B5:4B:C5:4D:FA:D9:CF:51:78:AD:45:9F:E8:
        CD:41:5A:A6:DE:B7:2E:75:85:EB:8C:7D:68:F2:D4:A1:
        5D:DD:B2:26:63:BB:7C:EB:79:80:33:80:05:B9:59:34:
        27:89:AA:92:04:61:0C:7D:E5:A5:DE:A0:40:60:73:64:
        5A:A7:06:C0:8A:04:CD:3A:1C:99:8D:B7:5C:C8:FE:97:
        70:9C:54:DF:AB:A7:8F:04:80:11:08:51:FF:7B:F5:73:
        C2:A1:C3:E3:A3:45:04:70:90:2D:EA:1E:AD:2C:75:5E:
        FF:55:EE:0D:75:D3:19:00:59:5C:F6:4C:E2:B7:5F:7A:
        8F:3E:9B:21:AC:59:6F:7C:63:B0:62:B5:AA:B4:D8:04:
        65:07:8B:56:94:18:14:E3:12:AC:A5:3F:B0:BA:97:D4:
        83:22:2E:EC:38:2F:D5:01:39:BA:60:A5:A8:5F:85:87
Exponent (4 bytes)   : 10001
Key Version          : A
[output truncated]
```

Submit all command output collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Five – Text Memory Region Analysis

Obtaining a core dump as outlined in step five below is the preferred method of gathering information for analysis in IOS device forensics. However, there may be times when retrieving a core dump is not possible and this section provides an alternative method for validating and obtaining a copy of the runtime image from the memory of an IOS device using the show , verify , and copy commands.

Note: It is highly recommended that a copy of the text region be obtained manually in case unforeseen issues arise during the core dump procedure.

Access the CLI of the IOS device and issue the following commands in enable mode:

```
show region
verify /md5 system:memory/text
copy system:memory/text ftp:
```

Note: This example uses the FTP protocol to transfer the text memory region from the platform, but HTTP/S, SCP, and TFTP can also be used.

An example of this procedure follows:

```
Router1#show region
Region Manager:
      Start         End     Size(b)  Class  Media  Name
 0x00000000  0x3C51313F  1011953984  Local  R/W    main
 0x01000000  0x03FFFFFF    50331648  Local  R/W    main:heap
 0x040001B0  0x0AF9415F   116998064  IText  R/O    main:text
 0x0AF95000  0x0FBFA21F    80106016  IData  R/W    main:data
 0x0FBFA220  0x106A7243    11194404  IBss   R/W    main:bss
 0x106A7244  0x3C51313F   736542460  Local  R/W    main:heap
 0x3C513140  0x3FFFFFFF    61787840  Iomem  R/W    iomem

Free Region Manager:
      Start         End     Size(b)  Class  Media  Name

Router1#verify /md5 system:memory/text
..............................................................................
..............................................................................
[output truncated]
.......................................................................................................................................................................................................... MD5 of system:memory/text Done!
verify /md5 (system:memory/text) = 87f97ac0b0703019056444a06070dbb2

Router1#copy system:memory/text ftp: 
Address or name of remote host []? 10.10.10.1
Destination filename [text]? system.memory.text
Writing system.memory.text
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[output truncated]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
116998064 bytes copied in 18.740 secs (6243226 bytes/sec)
```

Submit all command output and both of the core files collected in this section to relevant TAC SR and proceed to the next section of this document.

## Step Six - IOS Core File/Memory Dump

CAUTION: This section contains commands that alter device configuration. Please ensure that you have the appropriate authorization to make changes to the platform in question prior to proceeding with the following steps.

This procedure outlines how to configure an IOS device in order to obtain a dump of platform memory.

To configure the appropriate dump parameters, enter the following commands in enable mode:

```
conf t
service timestamps debug datetime msec localtime 
service timestamps log datetime msec localtime 
service internal 
exception core-file <filename.bin> compress
exception region-size 65536
exception dump <destination_ip_address>
exception protocol ftp
ip ftp username <username>
ip ftp password <passwword>
end
```

CAUTION: Initiating a core dump on an IOS device can be CPU intensive and may adversely affect traffic transitting the platform.

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
no ip ftp username <username>
no ip ftp password <password>
end
```

It is highly recommended that hash values be calculated on the core files obtained in this section so that any errors introduced by subsequent copying or transmission can be reliably detected.

An example of this procedure follows:

```
Router1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router1(config)#service timestamps debug datetime msec localtime 
Router1(config)#service timestamps log datetime msec localtime 
Router1(config)#service internal 
Router1(config)#exception core-file router1-core.bin compress
Router1(config)#exception region-size 65536
Router1(config)#exception dump 10.10.10.1
Router1(config)#exception protocol ftp
Router1(config)#ip ftp username anonymous
Router1(config)#ip ftp password mypasswd
Router1(config)#end
*Jan 22 08:29:51.477: %SYS-5-CONFIG_I: Configured from console by admin on console

Router1#write core
Remote host [10.10.10.1]? 
Base name of core files to write [router1-core.bin]?
writing compressed ftp://10.10.10.1/router1-core.bin.Z
Writing router1-core.bin.Z
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[output omitted]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
EOF-inputbuf 3C513140 [OK] [OK]
1011953984 bytes copied in 162.328 secs (6234008 bytes/sec)

Writing compressed ftp://10.10.10.1/router1-core.biniomem.Z
Writing router1-core.biniomem.Z
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[output omitted]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
EOF-inputbuf 40000000 [OK] [OK]
61787840 bytes copied in 21.208 secs (2913421 bytes/sec)

Router1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router1(config)#no service internal 
Router1(config)#no exception core-file router1-core.bin compress
Router1(config)#no exception region-size 65536
Router1(config)#no exception dump 10.10.10.1
Router1(config)#no exception protocol ftp
Router1(config)#no ip ftp username anonymous
Router1(config)#no ip ftp password mypasswd
Router1(config)#end
*Jan 22 08:36:27.779: %SYS-5-CONFIG_I: Configured from console by admin on console
```

Submit all command output and both of the cores files collected in this section to relevant TAC SR, and proceed to the next section of this document.

## Step Seven – ROMMON Upgrade Check

This procedure simply checks whether the ROM Monitor firmware of the device has been upgraded or not. Cisco is aware of a small number of incidents where a modified firmware image has been introduced in order to change device behavior or to circumnavigate certain platform or IOS license checks.

Execute the following command in enable mode:

```
show rom-monitor
```

Example 1 depicts a platform where the ROM Monitor has not been upgraded.

Example 2 depicts a platform where the ROM Monitor has been upgraded.

Submit all command output collected in this section to the relevant TAC SR.

## Related Documentation

Additional information about the procedures contained in this document, as well as forensic data collection procedures for other platforms, can be found at the following link:

Cisco Tactical Resources

https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## IOS Device Forensic Response Checklist

Step 1 – Create the IOS Device Problem Description

Device Problem Description uploaded to SR

Step 2 – Document IOS Runtime Environment

Output of show tech-support uploaded to SR

Output of dir all-filesystems uploaded to SR

Step 3 – IOS Image File Hash Verification

Output of verify on system image files uploaded to SR

Image files with hash inconsistencies uploaded to SR

Step 4 – Verify Digitally Signed Image Authenticity

Output of show software authenticity file uploaded to SR

Output of show software authenticity running uploaded to SR

Output of show software authenticity keys uploaded to SR

Step 5 – Text Memory Region Analysis (Alternate/Optional)

Output of show region uploaded to SR

Output of verify /md5 system:memory uploaded to SR

Copy of the text memory region uploaded to SR

Step 6 – IOS Core File Memory Dump

Output of write core uploaded to SR

Core dump file uploaded to SR

Binary iomemory file uploaded to SR

Core dump parameters unconfigured

Step 7 – ROMMON Upgrade Check

Output of show rom-monitor uploaded to SR

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
| 1.0 | 8/19/2019 | Dan Maunz | Initial public release |
| 1.1 | 2/16/2022 | Dan Maunz | Validated  procedures on Release 15.x. |
| 1.2 | 02/23/2023 | Dan Maunz | Validated procedures on Release 15.9.3. |
| 1.3 | 05/03/2023 | Dan Maunz | Reordered collection steps. |
| 1.4 | 02/02/2024 | Dan Maunz | Added image signing checks. |
| 1.5 | 02/28/2025 | Dan Maunz | Minor content adjustments. |
| 1.6 | 02/02/2026 | Dan Maunz | Validated procedures on Release 15.9(3)M12. |