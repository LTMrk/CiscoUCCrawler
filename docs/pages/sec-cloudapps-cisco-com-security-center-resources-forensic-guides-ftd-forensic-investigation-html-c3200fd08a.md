---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-ftd-forensic-investigation-html-c3200fd08a
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/ftd_forensic_investigation.html
retrieved_at: 2026-09-01T14:10:33.213006+00:00
---

Home / Cisco Security

Cisco Firepower Threat Defense Forensic Data Collection Procedures

# Cisco Firepower Threat Defense Forensic Data Collection Procedures

Retirement Notice

Introduction

Prerequisites

Step One - FTD Device Problem Description

Step Two - Document the FTD Runtime Environment

Step Three - FTD Image File Hash Verification

Step Four - Verify Digitally Signed Image Authenticity

Step Five - Verify Memory .text Segment Integrity

Step Six - FTD Crashinfo File/Core File

Step Seven - ROMMON Settings Check

Acknowledgments

Related Documentation

FTD Device Forensic Report Checklist

Revision History

## Retirement Notice

Note: The hardware platforms and software releases that are referenced in this document are approaching end of life. Therefore, no further updates will be made to this document.

## Introduction

This document provides steps to collect forensic information from Cisco ASA 5500-X series firewalls running Firepower Threat Defense (FTD) Software when compromise or tampering is suspected. It outlines a number of commands that can be run to gather evidence for an investigation, along with the respective output that should be collected after running these commands. This document also provides information on how to perform integrity checks on FTD system images and includes procedures for collecting a memory dump, crashinfo file, and a core dump from an FTD device.

IMPORTANT : DO NOT REBOOT THE DEVICE. Rebooting a device during initial assessment will irrevocably lose all volatile information contained within the device. (e.g. RAM contents, arp and routing tables, NAT translations, ACL hit and drop counts, etc.)

Note: It is highly recommended that a device suspected of tampering or compromise be isolated from the network prior to conducting an initial forensic examination. This may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device under investigation.

If you require assistance or have questions regarding the following procedures, contact the Cisco Product Security Incident Response Team (PSIRT) .

The main section of this document contains seven sections:

1.      FTD Device Problem Description – Describe why the platform is a candidate for forensic examination.

2.      FTD Runtime Environment – Collect platform configuration and runtime state.

3.      FTD Image File Verification – Examine system image hashes for inconsistencies.

4.      Digitally Signed Image Verification – Examine FTD system and running images for proper signing characteristics.

5.      Verify Memory .text Segment – Retrieve and calculate a hash of the .text segment.

6.      Crashinfo / Core File – Obtain a crashinfo dump and core file from the running FTD image.

7.      ROM Monitor Variables – Examine ROM monitor settings for remote system image loading.

## Prerequisites

The procedures described in this document assume the reader has a basic understanding of Cisco FTD Software command syntax.

A valid cisco.com account is required to view individual FTD Software and FTD firmware file hashes for software file integrity checking. For customers without a cisco.com account, a publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded from: https://www.cisco.com/c/en/us/about/trust-center/downloads.html

Note: The examples used in this document are based on Cisco Firepower Threat Defense (FTD) Software Release 7.0.8 command syntax. The output that is produced by a command may vary depending on the software release that is deployed and/or the features that are supported or configured on the device. Not all commands that are used in these procedures may be supported on earlier releases of the software.

## Step One – FTD Device Problem Description

Describe in as much detail as possible WHY the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior that cannot be attributed to a misconfiguration or a software or hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific software releases of the following products: Cisco ASA, FMC, FTD, FXOS, IOS, IOS XE, NX-OS, and NX-OS in ACI Mode.

https://sec.cloudapps.cisco.com/security/center/softwarechecker.x

Record any results that are returned by the tool that may explain the anomalous behavior being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA, FMC, FTD, and FXOS Software, the tool contains only vulnerability information for Cisco Security Advisories first published from January 2022 onward, and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Submit the problem description and any relevant results that are obtained from the Cisco Software Checker and collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Two – Document the FTD Runtime Environment

Complete the initial stage of forensic information gathering by issuing a show tech-support command and two dir commands. Execute these commands from the privileged EXEC mode of the FTD diagnostic CLI. Some of the output may vary depending on the particular FTD Software version and/or features supported/configured on the device.

Execute the following command from the FTD CLI prompt:

```
system support diagnostic-cli
```

Execute each of the following commands in the diagnostic CLI and record the output:

```
enable
terminal pager 0
show tech-support detail
dir /recursive all-filesystems
dir /recursive cache:
```

Note: The output of the show tech-support detail command may be redirected to a file on the local filesystem, which can be copied off the platform at a later time. An example of this command follows:

```
show tech-support detail | redirect disk0:/tech-support-detail.txt
```

Submit all command output collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Three – FTD Image File Hash Verification

Execute the following commands from the Cisco FTD CLI prompt:

```
system support diagnostic-cli
enable
show version
```

Note the location and filename of the FTD system image file and then execute the following command:

```
verify /sha-512 location:filename
```

Alternatively, an MD5 hash value can be calculated with the following command:

```
verify /md5 location:filename
```

After calculating the desired hash value(s), validate the digital signature of the file by issuing the following command:

```
verify location:filename
```

The following example illustrates this procedure:

```
> system support diagnostic-cli
Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.

firepower> enable
Password:
firepower# show version 
-------------------[ firepower ]--------------------
Model                     : Cisco ASA5516-X Threat Defense (75) Version 7.0.8 (Build 174)
UUID                      : 204173a0-82ca-11f0-84a9-f2dbe0d05857
LSP version               : lsp-rel-20210503-2107
VDB version               : 338
----------------------------------------------------
Cisco Adaptive Security Appliance Software Version 9.16(4)125 
SSP Operating System Version 2.10(1.4003)
Compiled on Mon 23-Jun-25 22:00 GMT by builders
System image file is "disk0:/os.img"
Config file at boot was "startup-config"

[output omitted]

firepower# verify /sha-512 disk0:/os.img
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
[output omitted]

Done!
verify /SHA-512 (disk0:/os.img) = 9c0d1575d8565e2b84aeb76e33c126abeef4e474f5eee322f6890039d9dab8738a951e450d744e8bc091cc0a909687a54df508de421b15ab8d5182697cf08f20

firepower# verify disk0:/os.img
Verifying file integrity of disk0:/os.img
Verifying file integrity of disk0:/os.img
Computed Hash   SHA2: 0ea0bf5c026e34ee9b7ba9925543f3f7
                      73e25c356c4e8717f9e9d2c0d9ed77f5
                      dfe67bcb5f58f4e5d1b950ec09f3d0be
                      7f0fa1e5bd98aaf1c2018fcb2e76fcd4
                      
Embedded Hash   SHA2: 0ea0bf5c026e34ee9b7ba9925543f3f7
                      73e25c356c4e8717f9e9d2c0d9ed77f5
                      dfe67bcb5f58f4e5d1b950ec09f3d0be
                      7f0fa1e5bd98aaf1c2018fcb2e76fcd4                     
Digital signature successfully validated
```

Note: Cisco is aware that the CLI verify command may not return output when executed on some releases of 6.7.0 and 7.0.0 software, and this issue will be corrected in a future release. See Cisco bug ID CSCwb58643 for more information.

Repeat the procedure for any other system image file located on the file systems. A comprehensive list of all files can be viewed by executing the following command:

```
dir all-filesystems
```

If directed to do so, obtain a copy of the system image file and transfer it to a secure location if possible.

```
copy <location>:<system_image_filename.img> ftp: 
Address or name of remote host []? <destination_ip>
Destination filename []? </destination_ip></system_image_filename.img></location>
```

It is highly recommended that a hash value be calculated on the copied system image file and compared to the hash value obtained on the platform to ensure that no errors were introduced during the file transfer process.

The following example uses the sha512sum utility, which is included with most Linux distributions:

```
root@ftp-server:~# sha512sum os.img
9c0d1575d8565e2b84aeb76e33c126abeef4e474f5eee322f6890039d9dab8738a951e450d744e8bc091cc0a909687a54df508de421b15ab8d5182697cf08f20 e5f1603c6ce0898555514d72  os.img
root@ftp-server:~#
```

Note that the FTD verify command and the sha512sum utility both produce an SHA-512 hash value of 9c0d1575d8565e2b84aeb76e33c126abeef4e474f5eee322f6890039d9dab8738a951e450d744e8bc091cc0a909687a54df508de421b15ab8d5182697cf08f20 for the os.img file in the previous output.

Submit all command output (including all computed hash values) and any system images collected in this section to the relevant TAC SRand proceed to the next section of this document.

## Step Four – Verify Digitally Signed Image Authenticity

Cisco FTD Software implements digitally signed system images on most platforms. Digitally signed Cisco FTD Software uses asymmetric (public-key) cryptography, which increases the security posture of Cisco FTD devices by ensuring that the system image has not been altered.

Certain ASA platforms running FTD Software, such as the newer Cisco 5500-X series, also support Secure Boot technologies. Cisco Secure Boot is a secure startup process that a Cisco device performs each time it boots up. Beginning with the initial power-on, a special purpose hardware device, known as the Trust Anchor module, verifies the integrity of the ROMMON code and the FTD image via digital signatures as they each are loaded. If any failures are detected, the user is notified of the error and the device will wait for the operator to correct the error. This prevents the network device from executing tainted network software.

For additional information see Trust Anchor Technology .

Note: The show software authenticity set of commands is supported only on FTD platforms that incorporate Cisco Secure Boot technologies, and these commands may not produce output on older platforms or virtual machine editions of Cisco FTD Software.

The authenticity and integrity of a system image file can be verified by using the following commands:

```
system support diagnostic-cli
enable
show software authenticity file location:filename
```

The following example illustrates this procedure using the location and filename identified in Step 3:

```
> system support diagnostic-cli
Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable
Password: 
firepower# show software authenticity file disk0:/os.img
File Name                     : disk0:/os.img
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : NCS_Kenton_ASA
        Organization Name     : CiscoSystems
    Certificate Serial Number : 5AB844ED
    Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The Organization Unit, Organization Name, and Certificate Serial Number values (highlighted in the previous output) can be viewed to verify that the system image signature is valid. It is also important to verify the authenticity and integrity of the running system image. This can be accomplished by using the following command:

```
show software authenticity running
```

The following example illustrates this procedure:

```
firepower# show software authenticity running           
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : NCS_Kenton_ASA
        Organization Name     : CiscoSystems
    Certificate Serial Number : 5AB844ED
    Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : ROMMON
        Verifier Version      : Cisco Systems ROMMON,1.1.18
```

The Organization Unit and Organization Name values (highlighted in the previous output) can be viewed to verify that the system image signature is valid. The certificate serial number should be the same as the value obtained from the show software authenticity file command. In the previous examples, the authenticity check of the FTD Software image on disk0 and the authenticity check of the running image both produce a value of 5AB844ED.

Lastly, obtain a copy of the public keys by using the following command:

```
show software authenticity keys

firepower# show software authenticity keys           
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

Submit all command output and any system images collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Five - Verify Memory .text Segment Integrity

Execute the following commands from the Cisco FTD CLI prompt:

```
system support diagnostic-cli
enable
```

Then calculate a hash value for the .text memory segment and retrieve a copy of it by executing the following commands:

```
verify /sha-512 system:memory/text
copy system:memory/text ftp:
```

The following example illustrates this procedure:

```
> system support diagnostic-cli
Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable
Password: 
firepower# verify /sha-512 system:memory/text !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
[output truncated]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!Done!
verify /SHA-512 (system:memory/text) = 
a03a15444f0995f578e9aa6cbc8feed2a3f2dd8ac8cca919b7b2b54836ba3d4b763372f58029e66fa64aafa8eea 2b79d5f0c7ea65cde0d813aef17e436e49b85

firepower# copy system:memory/text ftp:
Source filename [memory/text]? 
Address or name of remote host []? 10.10.10.1
Destination filename [text]? system.memory.text.bin
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
INFO: No digital signature found
71921664 bytes copied in 2.60 secs (35960832 bytes/sec)
```

It is highly recommended that a hash value be calculated on the copied memory segment file and compared to the hash value obtained on the platform to ensure that no errors were introduced during the file transfer process.

The following example uses the sha512sum utility, which is included with most Linux distributions:

```
root@ftp-server:~# sha512sum system.memory.text.bin
a03a15444f0995f578e9aa6cbc8feed2a3f2dd8ac8cca919b7b2b54836ba3d4b763372f58029e66fa64aafa8eea 2b79d5f0c7ea65cde0d813aef17e436e49b85 system.memory.text.bin
root@ftp-server:~#
```

Note that the FTD verify command and the sha512sum utility both produce an SHA-512 hash value of a03a15444f0995f578e9aa6cbc8feed2a3f2dd8ac8cca919b7b2b54836ba3d4b763372f58029e66fa 64aafa8eea2b79d5f0c7ea65cde0d813aef17e436e49b85 for the system.memory.text.bin file.

Submit all command output (including all computed hash values) and any system images collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Six – FTD Crashinfo File/Core File

WARNING : Executing the tasks in this section will trigger a reload of the FTD platform.

Cisco recommends performing this task during a maintenance window. Cisco does not recommend performing this task if additional forensic information needs to be collected because a reload of the device may cause the loss of information vital to a forensic investigation. Please ensure that you have a copy of the original device configuration and the appropriate authorization to initiate a reload of the platform in question prior to proceeding with this step.

This step describes how to obtain a crashinfo file from a Cisco FTD device. The crashinfo dump is saved in the root of the Cisco FTD file system by default and the storage space required may vary from several hundred megabytes to several gigabytes in size depending on device model. Be sure that there is enough space on the destination FTD flash or disk file system to accommodate the crashinfo dump file.

To initiate the crashinfo dump process, execute the following commands:

```
system support diagnostic-cli
enable
crashinfo force page-fault
```

The following example illustrates this procedure:

```
> system support diagnostic-cli
Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable
Password: 
firepower# crashinfo force page-fault 
WARNING: This command will force a crash and cause a
         reboot. Do you wish to proceed? [confirm]: 

Register dump: Thread DATAPATH-1-4679 in thread group
other: Unknown
        r8 0x0000000000000001
        r9 0x0000000000000000
       r10 0x00002afa53d2f488
       r11 0x0000000000000000
       r12 0x00002afa53d2f540
       r13 0x0000000000000000
       r14 0x00000000000000c8

[output truncated]

Begin to dump crashinfo to flash....

End of console dump.
Do 'show crashinfo' after reboot to retrieve other crash information
Process shutdown finished
Rebooting... (status 0x8b)
```

When the crashinfo dump process is complete, the FTD platform will reboot.

The crashinfo dump is written to a file located on the FTD file system with the following format: crashinfo_<date>_<time>_<timezone>. The name of the file can be displayed using the following command:

```
dir

> system support diagnostic-cli
Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable
Password: 
firepower# dir
Directory of disk0:/

81   -rwx  163256992    23:15:08 Aug 26 2025  os.img
83   -rwx  6872         22:12:02 Aug 26 2025  install.log
12   -rwx  345          15:34:01 Aug 27 2025  asa-cmd-server.log
13   drwx  4096         22:25:32 Aug 26 2025  log
15   -rwx  39           15:34:04 Aug 27 2025  snortpacketinfo.conf
22   drwx  4096         22:26:24 Aug 26 2025  crypto_archive
24   drwx  4096         22:26:26 Aug 26 2025  coredumpinfo
84   -rwx  796          15:29:00 Aug 27 2025  troubleshoot_file
85   -rwx  5184         22:56:28 Aug 26 2025  backup-config.cfg
86   -rwx  4482         22:56:28 Aug 26 2025  modified-config.cfg
11   -rwx  0            15:33:42 Aug 27 2025  hitcnt_del_ruleid_list
87   -rwx  577574       15:29:00 Aug 27 2025  crashinfo_20250827_152850_UTC

9 file(s) total size: 163852284 bytes
7366516736 bytes total (7202217984 bytes free/97% free)
```

It is highly recommended that hash values be calculated on the crashinfo files obtained in this section so that any errors introduced by subsequent copying or transmission can be reliably detected.

```
firepower# verify /sha-512 disk0:/crashinfo_20250827_152850_UTC
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Done!
```

```
verify /SHA-512 (disk0:/crashinfo_20250827_152850_UTC) = b500c16c6bd027bdc26d2b4a13b16929ebcc9e57c8b29cadb4f86fc81662a9c78992bab0f73076b4238bf413a1c993bdce31756a51823eea64cb2e63433e89aa
```

After calculating the hash value of the crashinfo file on the FTD platform, copy the crashinfo file to a secure location and calculate the hash value again.

The following example uses the sha512sum utility, which is included with most Linux distributions:

```
root@ftp-server:~# sha512sum crashinfo_20250827_152850_UTC
b500c16c6bd027bdc26d2b4a13b16929ebcc9e57c8b29cadb4f86fc81662a9c78992bab0f73076b4238bf413a1c993bdce31756a51823eea64cb2e63433e89aa crashinfo_20250827_152850_UTC
root@ftp-server:~#
```

Note that the FTD verify command and the sha512sum utility both produce an SHA-512 hash value of b500c16c6bd027bdc26d2b4a13b16929ebcc9e57c8b29cadb4f86fc81662a9c78992bab0f73076b4238bf413a1c993bdce31756a51823eea64cb2e63433e89aa for the crashinfo_20250827_152850_UTC file.

Next, enter FTD expert mode (you may need to enter the exit command twice if still in the system support diagnostic-cli) and copy the core file to disk0 so that it can be copied off the platform by executing the following command:

```
expert
```

Note: the sudo su - command must be executed after entering expert mode to ensure that the correct privileges are obtained to copy the core file from one disk partition to another.

The following example illustrates this procedure:

```
> expert
admin@firepower:~$ sudo su -

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

Password: 
root@firepower:~# cd /ngfw/var/common/
root@firepower:common# ls -l
total 98752
-rw------- 1 root root 97716325 Aug 27 15:29 core_1756308546_firepower_lina_11.3692.gz
-rw-r--r-- 1 root root  3401252 Aug 26 22:55 results-08-26-2025--225248.tar.gz
-rw------- 1 root root        0 Aug 27 15:34 sftls_clear_lmdb_counters.cmd
root@firepower:common# cp core_1756308546_firepower_lina_11.3692.gz /mnt/disk0/
root@firepower:common# exit
logout
admin@firepower:~$ exit
logout
>
```

After the core file has been copied to disk0, copy the core file to a secure location. The following example transfers the file using the secure copy command:

```
> file secure-copy 10.10.1.1 root /tmp  core_1756308546_firepower_lina_11.3692.gz
root@10.10.1.1's password: 
copy successful.
```

It is highly recommended that hash values be calculated on the core files obtained in this section so that any errors introduced by subsequent copying or transmission can be reliably detected.

Submit all command output, hash values, crashinfo and core files collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Seven – ROMMON Settings Check

The ROM monitor firmware of the FTD platform is executed when the FTD is powered up or reset. The firmware initializes the platform hardware and boots the FTD operating system software. Because the ROM monitor settings are persistent if they have been synced to NVRAM, information about the ROM monitor variable values could indicate an attempt to influence the Cisco FTD boot sequence. The set command can be used while in the ROM monitor prompt to see the value of the ROM monitor variables.

ROM monitor mode is accessed by rebooting the FTD device and pressing the BREAK or ESC key during the reload process when prompted as depicted in the following example:

```
> reboot
This command will reboot the system.  Continue?
Please enter 'YES' or 'NO': yes

Broadcast messagStopping Cisco ASA5516-X Threat Defense...
Shutting down sfifd...                                                [  OK  ]
Clearing static routes
Unconfiguring default route                                           [  OK  ]
Unconfiguring address on br1                                          [  OK  ]
Unconfiguring IPv6                                                    [  OK  ]
Downing interface                                                     [  OK  ]
Stopping xinetd: 

[output truncated]

Rebooting...
Rom image verified correctly
Cisco Systems ROMMON, Version 1.1.18, RELEASE SOFTWARE
Copyright (c) 1994-2020  by Cisco Systems, Inc.
Compiled Tue 09/15/2020 20:35:13.52 by wchen64

Current image running: Boot ROM0
Last reset cause: PowerCycleRequest
DIMM Slot 0 : Present
DIMM Slot 1 : Present

Platform ASA5516 with 8192 Mbytes of main memory
MAC Address: 70:b3:17:ce:ba:7d

Use BREAK or ESC to interrupt boot.
Use SPACE to begin boot immediately.
Boot interrupted.  
rommon 1 >
```

The following example shows the output of the ROM monitor set command on a Cisco FTD platform:

```
rommon 1 > set
    ADDRESS=
    NETMASK=
    GATEWAY=
    SERVER=
    IMAGE=
    CONFIG=
    PS1="rommon ! >
```

The previous example depicts a platform where the ROM monitor values are at their default values and have not been altered.

To return the FTD platform to normal operation, simply issue the boot command at the ROM monitor prompt as depicted in the following example:

```
rommon 2 > boot
Located '.boot_string' @ cluster 283386.
#
Located 'os.img' @ cluster 257862.
#############################################################################
#############################################################################
LFBFF signature verified.
INIT: version 2.88 booting

[output truncated]
```

Submit all command output obtained in this section to the relevant TAC SR.

## Acknowledgments

The author would like to thank all members of the Customer Experience Security Programs (CXSP) and Advanced Security Initiatives Group (ASIG) who provided their expertise for this document. A special note of thanks to Jason Barnes of ASIG whose contributions greatly enhanced the efficacy of the forensic procedures contained in this publication.

## Related Documentation

Additional information about Cisco Software Integrity Assurance, as well as forensic investigation procedures for other platforms, can be found at the following link:

Cisco Security Tactical Resources

https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## FTD Device Forensic Response Checklist

Step 1 – Create the FTD Device Problem Description

Device Problem Description uploaded to SR

Step 2 – Document FTD Runtime Environment

Output of show tech-support uploaded to SR

Output of dir all-filesystems uploaded to SR

Step 3 – FTD Image File Hash Verification

Output of verify on system image files uploaded to SR

Image files uploaded to SR (If requested)

Step 4 – FTD Digitally Signed Image Authenticity Verification

Output of show software authenticity file uploaded to SR

Output of show software authenticity running uploaded to SR

Output of show software authenticity keys uploaded to SR

Step 5 – Verify Memory .text Segment Integrity

Output of verify on memory text segment uploaded to SR

Copy of memory text segment uploaded to SR

Step 6 – FTD Crashinfo File / Core File

Output of crashinfo uploaded to SR

Crashinfo file uploaded to SR

Core file uploaded to SR

Step 7 – FTD ROM Monitor Variable Check

Output of set command uploaded to SR

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
| 1.4 | 8/28/2025 | Dan Maunz | Final release. |
| 1.3 | 7/22/2024 | Dan Maunz | Simplified procedures in step 2. |
| 1.2 | 6/2/2023 | Dan Maunz | Validated procedures on Release 7.0.5 |
| 1.1 | 6/23/2022 | Dan Maunz | Validated procedures on v6.7.0 |
| 1.0 | 8/19/2019 | Dan Maunz | Initial public release. |
|  |  |  |  |