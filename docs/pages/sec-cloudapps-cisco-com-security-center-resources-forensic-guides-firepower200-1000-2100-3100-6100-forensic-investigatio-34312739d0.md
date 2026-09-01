---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-firepower200-1000-2100-3100-6100-forensic-investigatio-34312739d0
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/firepower200_1000_2100_3100_6100_forensic_investigation.html
retrieved_at: 2026-09-01T14:10:24.681579+00:00
---

Home / Cisco Security

Cisco Firepower 200, 1000, 2100, 3100, and 6100 Series Forensic Data Collection Procedures

# Cisco Firepower 200, 1000, 2100, 3100, and 6100 Series Forensic Data Collection Procedures

Introduction

Prerequisites

Step 1 - Create the Firepower Device Problem Description

Step 2 - Document the Firepower Runtime Environment

Step 3 - Verify the Integrity of FTD System Files

Step 4 - Verify Digitally Signed Image Authenticity

Step 5 - Verify FTD Memory .text Segment Integrity

Step 6 -  Obtain Firepower crashinfo / core File

Step 7 - Check ROM Monitor Settings

Related Documentation

Firepower 200, 1000, 2100, 3100, and 6100 Series Forensic Data Collection Checklist

Appendix A - Firepower 200, 1000, 2100, 3100, and 6100 Series Platform That Is Running ASA Software

Revision History

## Introduction

This document provides steps to collect forensic information from Cisco Firepower 200, 1000, 2100, 3100, and 6100 Series appliances that are running Cisco Firepower eXtensible Operating System (FXOS) Software when compromise or tampering is suspected. It outlines a number of commands that can be run to gather evidence for an investigation along with the respective output that should be collected upon running these commands. This document also provides information on how to perform integrity checks on Cisco FXOS system and Cisco Firepower Threat Defense (FTD) application images and includes a procedure for collecting a memory dump, a crashinfo file, and a core file from a Cisco Firepower device.

Note: DO NOT REBOOT THE DEVICE. Rebooting a device during the initial stage of an assessment will irrecoverably lose all volatile information that is contained within the device (e.g., RAM contents, Address Resolution Protocol [ARP] and routing tables, Network Address Translations [NATs], access control list [ACL] hit and drop counts).

Note: Cisco highly recommends isolating a device that is suspected of tampering or compromise from the network before conducting an initial forensic examination. This may prevent remote unloading of any implants or malware that are installed on the device and will prevent an attacker from monitoring commands that are entered on the device under investigation.

Important: The steps in this guide are intended for platforms that are running Cisco FXOS Software with FTD security modules. If your platform is running Cisco FXOS Software with an ASA security module, omit steps 1 through 7 and proceed directly to Appendix A - Firepower 200, 1000, 2100, 3100, and 6100 Series Platform That Is Running ASA Software .

If you require assistance or have questions regarding the following procedures, contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains seven sections:

1.      Create the Firepower Device Problem Description - Describe why the platform is a candidate for forensic examination.

2.      Document the Firepower Runtime Environment - Collect platform configuration and runtime state.

3.      Verify the Integrity of FTD System Files - Examine system file image hashes for inconsistencies.

4.      Verify Digitally Signed Image Authenticity - Examine the Cisco FXOS operating system for proper signing characteristics.

5.      Verify FTD .text Memory Segment Integrity - Retrieve and calculate a hash of the Cisco FTD .text segment.

6.      Firepower crashinfo / core File - Obtain crashinfo and core files from the running Cisco FTD application.

7.      Check ROM Monitor Settings - Examine ROM monitor settings for remote system image loading.

## Prerequisites

The procedures that are outlined in this document assume that the reader has a basic understanding of Cisco FXOS Software, Cisco FTD Software, and Linux command syntax.

A valid cisco.com account is required to view individual Cisco FXOS Software and FTD Software file hashes for software file integrity checking. For customers without a cisco.com account, a publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded from https://www.cisco.com/c/en/us/about/trust-center/downloads.html .

A Cisco Technical Assistance Center (TAC) service request (SR) for the device in question is required because these procedures assume that the information gathered in each step will be uploaded to a TAC SR.

Note: The examples that are used in this document are based on Cisco FXOS Software Release 2.16.1 and Cisco FTD Software Release 7.6.4 command syntax. The output that is produced by a command may vary depending on the software release that is deployed and/or the features that are supported or configured on the device. Not all commands that are used in these procedures may be supported on earlier releases of the software.

Note: Collection steps 2 through 7 contain examples of the commands that should be executed along with the expected output toward the end of each step.

## Step 1 – Create the Firepower Device Problem Description

Describe in as much detail as possible why the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior that cannot be attributed to a misconfiguration or a software/hardware defect? Are any typical device administration commands now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific releases of Cisco Adaptive Security Appliance (ASA) Software, Firepower Management Center (FMC) Software, FTD Software, FXOS Software, IOS Software, IOS XE Software, NX-OS Software, and NX-OS Software in ACI Mode.

Record any results that are returned by the tool that may explain the anomalous behavior that is being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA Software, FMC Software, FTD Software, and FXOS Software, the tool contains only vulnerability information for Cisco Security Advisories first published from January 2022 onward, and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Submit the problem description and any relevant results that were obtained from the Cisco Software Checker to the relevant TAC SR and proceed to the next section of this document.

Note: If the platform is running a Cisco Adaptive Security Appliance (ASA) Software image, skip steps 2 through 7 and run the commands outlined in Appendix A. If the platform is running a Firepower Threat Defense (FTD) image, proceed with the commands in step 2.

## Step 2 – Document the Firepower Runtime Environment

The initial stage of forensic information gathering is completed by using show tech-support commands in the Cisco FXOS and Firepower CLIs, and some of the output may vary depending on the Cisco FTD Software release and/or features that are supported or configured on the device.

Note: For Cisco Firepower 200, 1000, 2100, 3100, and 6100 Series appliances, the default command shell will vary depending on the method that is used to access the platform. If SSH is used, the user will be placed into the Cisco FTD CLI. If a console connection is used, the user will be placed into the Cisco FXOS CLI. Use the connect ftd command to access the Cisco FTD CLI from the FXOS CLI and the connect fxos command to access the Cisco FXOS CLI from the FTD CLI.

Execute the following commands from the Cisco FXOS CLI prompt:

```
connect local-mgmt
show tech-support fprm detail
copy workspace:/techsupport/<file_name> <destination>
```

Note: The copy command supports the FTP, HTTP, HTTPS, SCP, SFTP, and TFTP protocols.

Next, connect to the Cisco Firepower module CLI and collect the output of show tech-support detail by using the following series of commands:

```
connect ftd
system support diagnostic-cli
enable
terminal pager 0
show tech-support detail
exit
exit
```

The output of show tech-support detail may also be redirected to a file server using the FTP, SCP, SMB, or TFTP protocols. The following example depicts the required syntax using the FTP protocol:

```
show tech-support file ftp://10.10.10.1/tech-support-details.txt detail
```

An example of this entire procedure follows:

```
firepower# connect local-mgmt 
firepower(local-mgmt)# show tech-support fprm detail
 firepower_FPRM
The showtechsupport file will be located at workspace:/techsupport/ 20240118150424_firepower_FPRM.tar.gz
Initiating tech-support information task on FABRIC A ...
WARNING: *** /mnt/disk0/smart-log/ is missing ***
WARNING: *** /tmp/sed_env_info.xml is missing ***
WARNING: *** /tmp/softraid_env.xml is missing ***
WARNING: *** /tmp/nvme_build.log is missing ***
WARNING: *** /tmp/sed_build.log is missing ***
WARNING: *** /tmp/sr_build.log is missing ***
WARNING: *** /tmp/vpath-cfg-cache is missing ***
Completed initiating tech-support subsystem tasks (Total: 0)

firepower(local-mgmt)#

firepower(local-mgmt)# copy workspace:/techsupport/20240118150424_firepower_FPRM.tar.gz ftp://anonymous@10.10.10.1/
Connected to 10.10.10.1.
220 Microsoft FTP Service
331 User name ok, need password
Password: 
230 User logged in
Remote system type is UNIX.
Using binary mode to transfer files.
200 Type set to I.
local: /opt/cisco/csp/workspace/techsupport/20240118150424_firepower_FPRM.tar.gz remote: /20240118150424_firepower_FPRM.tar.gz
227 Entering passive mode (10,10,10,1,222,195)
125 Using existing data connection
100% |***********************************| 6649 KiB  60.66 MiB/s   00:00 ETA
226 Closing data connection; File transfer successful.
6808707 bytes sent in 00:00 (43.99 MiB/s)
221 Service closing control connection

firepower(local-mgmt)# connect ftd
> system support diagnostic-cli
Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable
Password: 
firepower# terminal pager 0
firepower# show tech-support file ftp://10.10.10.1/tech-support-details.txt detail
!!!
firepower# exit
Logoff
User enable_1 logged in to firepower
Logins over the last 1 days: 2.  Last login: 13:10:25 UTC Feb 16 2024 from console
Failed logins since the last login: 0.  
Type help or '?' for a list of available commands.
firepower> exit
Console connection detached.
>
```

Submit all command output that was collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step 3 – Verify the Integrity of FTD System Files

Connect to the Cisco FTD CLI. This can be accomplished from the Cisco FXOS CLI by using the connect ftd command.

From the Cisco FTD CLI, use the following commands to assume root permissions, run the system file integrity checks, and collect the necessary files for forensic assessment.

Access expert mode and sudo to the root account:

```
expert
sudo su -
```

Run the integrity checks:

```
find /ngfw/var/sf/.icdb/* -name *.icdb.RELEASE.tar | xargs sha512sum
tail -n +1 /proc/*/smaps > /tmp/all-process-smaps.txt
verify_file_integ.sh -f
```

Note: The Linux which command can be used to quickly locate the shell scripts in the next step. See the following example for more details.

Locate and retrieve copies of the following files:

```
verify_file_integ.sh
verify_signed_db.sh
db_manage.sh
/ngfw/etc/certs/*.crt
/ngfw/var/log/sf/verify_file_integ.log
/ngfw/var/tmp/merged-db/master.db
```

Create an archive of the preceding list of files and copy the archive off the platform.

```
tar -cvf SR-<sr_number>.tar
sha512sum SR-<sr_number>.tar
ftp or scp
```

An example of this procedure follows:

```
firepower# connect ftd
> expert
admin@firepower:~$ sudo su -
We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:
    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.
Password:
root@firepower:~# find /ngfw/var/sf/.icdb/* -name *.icdb.RELEASE.tar | xargs sha512sum
480fd0602e527c156880543b7f0e8f87428f54c0692d217829633846316fc07a11d8ea1a90c6eeb9b80176c0a26223fee0390d02b72bc4d74aa360e8ba976077 /ngfw/var/sf/.icdb/lsp/lsp.icdb.RELEASE.tar
a4e48d6505e724d73b4037632988d5b24172afec1eeba2e37c986d496017563ff1ab012a787c65b61b17b9e50d569124469e6b61fa55078f2abb23673bf0e491 /ngfw/var/sf/.icdb/vdb/vdb.icdb.RELEASE.tar
ec1b5a2ac31a05a85c57880ec8fe781b2f449020454ccfe2eaada99aff4a4f5e5fde0ec9f43ea92be98425be13f034175ee77ddca3a712daa121994455411088 /ngfw/var/sf/.icdb/vdb/vdb.navl.icdb.RELEASE.tar
#
# Note: the file names, number of files, and hash values may vary dependent on # the version of software running on the appliance and whether any software # updates have been applied. It is important that the output (including file # names and hashes) generated by the command above be submitted to the TAC SR.
#
root@firepower:~# tail -n +1 /proc/*/smaps > /tmp/all-process-smaps.txt

root@firepower:~# verify_file_integ.sh -f
Running file integrity checks...
Successfully verified file integrity
#
# Identify the location of the system integrity scripts with the "which" # command:
#
root@firepower:~# which verify_file_integ.sh
/ngfw/usr/local/sf/bin/verify_file_integ.sh
root@firepower:~# which verify_signed_db.sh
/ngfw/usr/local/sf/bin/verify_signed_db.sh
root@firepower:~# which db_manage.sh
/ngfw/usr/local/sf/bin/db_manage.sh
#
# Archive a copy of these scripts, along with all certificates found in # /ngfw/etc/certs/, and the files /ngfw/var/log/sf/verify_file_integ.log and
# /ngfw/var/tmp/merged-db/master.db
#
root@firepower:~# tar -cvf SR-1234567890.tar /ngfw/usr/local/sf/bin/verify_file_integ.sh /ngfw/usr/local/sf/bin/verify_signed_db.sh
/ngfw/usr/local/sf/bin/db_manage.sh
/ngfw/etc/certs/*.crt /ngfw/var/log/sf/verify_file_integ.log /ngfw/var/tmp/merged-db/master.db
/tmp/all-process-smaps.txt
tar: Removing leading `/' from member names
/ngfw/usr/local/sf/bin/verify_file_integ.sh
/ngfw/usr/local/sf/bin/verify_signed_db.sh
/ngfw/usr/local/sf/bin/db_manage.sh
/ngfw/etc/certs/SRU_rel.crt
/ngfw/etc/certs/rel.crt
/ngfw/var/log/sf/verify_file_integ.log
/ngfw/var/tmp/merged-db/master.db
/ngfw/etc/certs/rewhich db_manage.sh
/tmp/all-process-smaps.txt 
#
# Create a hash of the tar file:
#
root@firepower:~# sha512sum SR-1234567890.tar
8833409f7affbae6ab19cdd8ca11153252f1176e147b3d4c373a7195e261da5ca72a3260a5aa1a5f991b12c1f6ac070d4ece31765e413f0e5e4afd6c95cf6ea5 SR-1234567890.tar
root@firepower:~#
#
# Copy the tar file off the platform using FTP or SCP:
#
root@firepower:~# ftp 10.10.10.1 
Connected to 10.10.10.1.
220 Microsoft FTP Service
Name (10.10.10.1:admin): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> bin
200 Type set to I.
ftp> put SR-1234567890.tar
local: SR-1234567890.tar remote: SR-1234567890.tar
229 Entering Extended Passive Mode (|||59418|)
125 Data connection already open; Transfer starting.
100% |***********************************|  1990 KiB  104.76 MiB/s    00:00 ETA
226 Transfer complete.
2037760 bytes sent in 00:00 (100.48 MiB/s)
ftp> quit
221 Goodbye.
root@firepower:~# exit
logout
admin@firepower:/opt/cisco/platform$ exit
logout
> exit
firepower(local-mgmt)#
```

Submit all command output and the files that were gathered in this step to the relevant TAC SR and proceed to the next section of this document.

## Step 4 – Verify Digitally Signed Image Authenticity

Cisco FXOS Software implements digitally signed system images on most platforms. Digitally signed Cisco FXOS Software uses asymmetric (public key) cryptography, which increases the security posture of Cisco Firepower devices by ensuring that the system image has not been altered.

Certain platforms that are running FXOS software, such as Cisco Firepower 1000 Series platforms, also support Cisco Secure Boot technologies. Cisco Secure Boot is a secure startup process that a Cisco device performs each time it boots up. Beginning with the initial power-on, a special-purpose hardware device known as the Trust Anchor module verifies the integrity of the ROM monitor code and the Cisco FXOS image using digital signatures as they are each loaded. If any failures are detected, the user is notified of the error, and the device will wait for the operator to correct the error. This prevents the network device from executing tainted network software.

For additional information, see Trust Anchor Technology .

Note: The show software authenticity set of commands are only supported on Cisco Firepower platforms that incorporate Cisco Secure Boot technologies.

The authenticity and integrity of a system image file can be verified by using the following commands from the Cisco FXOS CLI:

```
connect local-mgmt
cd bootflash:/
show file .boot_string
show software authenticity file <path/filename>
verify signature <path/filename>
show software authenticity running
show software authenticity keys
```

An example of this procedure follows:

```
firepower# connect local-mgmt
firepower(local-mgmt)# cd bootflash:/
firepower(local-mgmt)# show file .boot_string
disk0:installables/switch/fxos-k8-fp1k-lfbff.2.12.0.530.SPA
firepower(local-mgmt)# show software authenticity file /installables/switch/fxos-k8-fp1k-lfbff.2.12.0.530.SPA
: File /mnt/boot//installables/switch/fxos-k8-fp1k-lfbff.2.12.0.530.SPA size 199156688
File Name                     : <local>/fxos-k8-fp1k-lfbff.2.12.0.530.SPA
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : FXOS
        Organization Name     : CiscoSystems
    Certificate Serial Number : 65313942
    Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The Organization Unit , Organization Name , and Certificate Serial Number values (highlighted in the preceding output) can be viewed to verify that the system image signature is valid.

Next, calculate a hash for the Cisco FXOS system image and verify the digital signature by using the following command:

```
verify signature <path/filename>
```

An example of this procedure follows:

```
firepower(local-mgmt)# verify signature /installables/switch/fxos-k8-fp1k-lfbff.2.12.0.530.SPA
: File /mnt/boot//installables/switch/fxos-k8-fp1k-lfbff.2.12.0.530.SPA size 199156688
Done!
Computed Hash   SHA2: e94ca6457ed9c0411a42cfa1a747d438
                      033c79ca4309aa8a556aa7efb5e98801
                      8f4be4bffdcbcdc9dfbd184eb6bbb5ac
                      af0e6f76bc534c709233e8cb0e757fc3
                      
Embedded Hash   SHA2: e94ca6457ed9c0411a42cfa1a747d438
                      033c79ca4309aa8a556aa7efb5e98801
                      8f4be4bffdcbcdc9dfbd184eb6bbb5ac
                      af0e6f76bc534c709233e8cb0e757fc3         
The digital signature of the file: fxos-k8-fp1k-lfbff.2.12.0.530.SPA verified successfully
```

It is also important to verify the authenticity and integrity of the running system image, and this can be accomplished with the following command:

```
show software authenticity running
```

An example of this procedure follows:

```
firepower(local-mgmt)# show software authenticity running
File Name                     : <local>/fxos-k8-fp1k-lfbff.2.12.0.530.SPA
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : FXOS
        Organization Name     : CiscoSystems
    Certificate Serial Number : 65313942
    Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The Organization Unit , Organization Name , and Certificate Serial Number values (highlighted in the preceding output) can be viewed to verify that the system image signature is valid, and the certificate serial number should be the same as the value obtained from the show software authenticity file command. In the preceding examples, the authenticity checks of the Cisco FXOS Software image on bootflash: and the authenticity check of the running image both produce a value of 65313942.

Lastly, obtain a copy of the public keys with the following command:

```
show software authenticity keys
```

An example of this procedure follows:

```
firepower(local-mgmt)# show software authenticity keys
Public Key #1 Information
--------------------------
Key Type              : Release (Primary)
Public Key Algorithm  : 2048-bit RSA
Modulus :
        B6:B9:BC:D3:C8:A1:BE:3A:B5:04:0F:21:6C:AA:AB:D6:
        CC:FE:7A:AD:CF:97:1B:57:FC:9A:1D:4B:5A:6D:D4:B0:
        7D:DB:77:FB:3F:A4:57:1A:08:4F:C1:6E:3F:CB:BF:E0:
        3C:99:9C:EE:F5:DD:3C:FC:C6:8D:98:49:29:00:B9:9B:
        DF:22:7E:73:83:FB:B5:78:68:4E:48:1A:5B:EE:83:81:
        B6:3B:2E:35:5B:C2:D0:B8:46:D6:45:13:23:21:44:DA:
        36:55:F9:09:5B:B1:88:8B:9A:28:0B:DA:44:DE:D2:F8:
        8B:17:CF:99:64:BE:2F:80:EF:13:6B:BC:A4:3E:DE:99:
        33:EF:E8:30:56:4C:DA:D5:D3:89:55:CC:BF:A2:22:1A:
        B7:64:FD:14:3A:7D:4F:00:DC:86:B5:35:18:C3:F3:FC:
        93:D4:BF:5E:FD:85:8C:28:4B:96:0F:B1:6D:1E:96:E7:
        05:1C:39:B7:1F:C7:F9:52:47:60:9C:96:FB:00:E2:2D:
        D9:08:2E:3A:87:0C:4F:3E:39:77:C7:FE:AC:D7:2D:23:
        AA:63:EB:2A:4D:13:98:C7:6A:B4:06:F9:1E:2D:B6:F8:
        10:80:EA:F4:E3:BF:C4:49:63:D0:5D:93:9F:96:54:76:
        BF:4D:83:7B:9D:CD:72:61:CC:EC:47:EA:91:EF:34:0B
Exponent              : 65537
Key Version           : A
Product Name          : FXOS
Public Key #2 Information
--------------------------
Key Type              : Release (Backup)
Public Key Algorithm  : 2048-bit RSA
Modulus :
        B6:B9:BC:D3:C8:A1:BE:3A:B5:04:0F:21:6C:AA:AB:D6:
        CC:FE:7A:AD:CF:97:1B:57:FC:9A:1D:4B:5A:6D:D4:B0:
        7D:DB:77:FB:3F:A4:57:1A:08:4F:C1:6E:3F:CB:BF:E0:
        3C:99:9C:EE:F5:DD:3C:FC:C6:8D:98:49:29:00:B9:9B:
        DF:22:7E:73:83:FB:B5:78:68:4E:48:1A:5B:EE:83:81:
        B6:3B:2E:35:5B:C2:D0:B8:46:D6:45:13:23:21:44:DA:
        36:55:F9:09:5B:B1:88:8B:9A:28:0B:DA:44:DE:D2:F8:
        8B:17:CF:99:64:BE:2F:80:EF:13:6B:BC:A4:3E:DE:99:
        33:EF:E8:30:56:4C:DA:D5:D3:89:55:CC:BF:A2:22:1A:
        B7:64:FD:14:3A:7D:4F:00:DC:86:B5:35:18:C3:F3:FC:
        93:D4:BF:5E:FD:85:8C:28:4B:96:0F:B1:6D:1E:96:E7:
        05:1C:39:B7:1F:C7:F9:52:47:60:9C:96:FB:00:E2:2D:
        D9:08:2E:3A:87:0C:4F:3E:39:77:C7:FE:AC:D7:2D:23:
        AA:63:EB:2A:4D:13:98:C7:6A:B4:06:F9:1E:2D:B6:F8:
        10:80:EA:F4:E3:BF:C4:49:63:D0:5D:93:9F:96:54:76:
        BF:4D:83:7B:9D:CD:72:61:CC:EC:47:EA:91:EF:34:0B
Exponent              : 65537
Key Version           : A
Product Name          : FXOS
Public Key #3 Information
--------------------------
Key Type              : Release (FEATURE KEY STORAGE)
Public Key Algorithm  : 2048-bit RSA
Modulus :
        C3:9E:B2:42:93:F2:F5:8A:E7:BA:8A:20:13:23:4A:24:
        39:93:C1:9E:83:32:D5:C7:87:38:54:14:1F:BC:66:8A:
        1A:F5:BA:B5:44:6A:5A:D0:B8:22:B2:3D:66:3D:34:A4:
        13:DF:3C:EB:02:34:97:D3:59:37:BE:86:D1:5C:40:F8:
        4B:F8:C0:7C:C8:92:0E:8F:C0:9B:49:88:8E:EE:31:B4:
        86:4A:3B:D6:D9:34:9F:CB:16:5F:1C:84:47:5A:9C:07:
        9A:12:F3:33:A2:EE:EB:76:8D:B3:C5:29:D2:D3:C4:ED:
        47:7C:70:E0:D3:80:00:36:C5:C1:BC:B0:45:EF:78:D5:
        62:02:5C:B4:35:0F:E9:D9:AD:5F:FF:F9:92:69:0C:01:
        5C:19:7F:E2:FE:0F:6B:8F:58:71:DB:E1:D7:F8:43:2F:
        AF:C1:80:F9:84:D0:AD:CA:A3:EC:C8:C4:C7:BE:48:53:
        EA:D5:31:44:63:B2:F8:3D:F4:C4:66:93:76:83:20:C0:
        1C:F4:B9:9A:3B:8A:FB:8A:D6:EC:9E:D8:35:B1:E1:F0:
        48:16:4C:49:16:65:05:60:8E:77:B4:AA:7A:E9:3F:E7:
        11:89:3E:98:4A:97:82:6E:09:18:4C:7C:8F:5B:45:89:
        78:16:C2:37:8F:3E:40:AE:35:09:D2:91:E6:7F:3C:FB
Exponent              : 65537
Key Version           : A
Product Name          : FXOS-CID
```

Submit all command output and any system images that were collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step 5 – Verify FTD Memory .text Segment Integrity

Execute the following commands from the Cisco FTD CLI prompt:

```
system support diagnostic-cli
enable
```

Then calculate a hash value for the .text memory segment and retrieve a copy of it by executing the following commands:

```
verify /sha-512 system:/text
copy system:/text ftp
```

An example of this procedure follows:

```
> system support diagnostic-cli
Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable
Password: 
firepower# verify /sha-512 system:/text !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !! [output truncated]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!Done!
verify /SHA-512 (system:/text) = 2289796c12ee7d909ccac135e1b2075bc54d5c7a38300265dda95d5eb66 5a51b3f45b4fcdc8c17b69c7baa735972aac1a62d2a79530daad67d2aac3dec043b37

firepower# copy system:/text ftp
Source filename [/text]? 
Address or name of remote host []? 10.10.10.1
Destination filename [text]? system.text.bin
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
INFO: No digital signature found
74031104 bytes copied in 1.990 secs (74031104 bytes/sec)
```

Cisco highly recommends calculating a hash value on the copied memory segment file and comparing it to the hash value that was obtained on the recipient platform to ensure no errors were introduced during the file transfer process.

The following example utilizes the sha512sum utility, which is included with most Linux distributions:

```
root@ftp-server:~# sha512sum system.text.bin
2289796c12ee7d909ccac135e1b2075bc54d5c7a38300265dda95d5eb665a51b3f45b4fcdc8c17b69c7baa735972aac1a62d2a79530daad 67d2aac3dec043b37 system.text.bin
root@ftp-server:~#
```

Note that the Cisco FTD verify command and the sha512sum utility both produce a SHA-512 hash value of 2289796c12ee7d909ccac135e1b2075bc54d5c7a38300265dda95d5eb665a51b3f45b4fcdc8c17 b69c7baa735972aac1a62d2a79530daad67d2aac3dec043b37 for the system.text.bin file.

Submit all command output (including all computed hash values) and any system images that were collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step 6 – Obtain Firepower crashinfo / core File

WARNING: Executing the tasks in this section will trigger a reload of the FXOS platform. It is of critical importance that all of the preceding information gathering steps have been completed successfully or important evidence may be permanently lost.

Cisco recommends performing this task during a maintenance window. Customers should ensure that they have a copy of the original device configuration and the appropriate authorization to initiate a reload of the platform in question before proceeding with this procedure.

This procedure outlines how to obtain a crashinfo file and a core dump from a Cisco FXOS device.

The crashinfo file is saved in the root of the Cisco FXOS file system by default, and the core dump may be placed in the underlying FTD file system or the coredumpfsys filesystem depending on the software release that is running on the system. The storage space that is required may vary from several hundred megabytes to several gigabytes, depending on the device model. Please ensure that there is enough space on the destination flash or disk file system to accommodate the crashinfo file and core dump file.

To initiate the crashinfo dump process, execute the following commands from the Cisco FTD CLI:

```
system support diagnostic-cli
enable
crashinfo force page-fault
```

An example of this procedure follows:

```
> system support diagnostic-cli
Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable
Password: 
firepower# crashinfo force page-fault
WARNING: This command will force a crash and cause a
         reboot. Do you wish to proceed? [confirm]: 
!! !! First Crash in tid: 22879 type: Page fault error: Address not mapped

Writing live core file to flash. Please do not reload.
Coredump starting....
Corehelper: /opt/cisco/csp/cores/core.lina.11.22781.1745506311
Waiting for Corehelper to finish....
Livecore: generating coredump of 22781
[output omitted]

Saved corefile /opt/cisco/csp/cores/core.lina.11.22781.1745506311
[Inferior 1 (process 22781) detached]
!!! !!! Corehelper [22876] Exit Code: 0
Coredumping took 0 min and 4 secs
[output omitted]
```

When the crashinfo process is complete, the Cisco Firepower platform will reboot.

Once the platform has rebooted, connect to the Cisco FTD CLI, enter expert mode, calculate a hash value for the core and crashinfo files, and copy the files off the platform by executing the following commands:

```
expert
sudo su – 
cd /var/data/cores
sha512sum
cd /mnt/disk0
sha512sum
ftp or scp
exit
```

An example of this procedure follows:

```
> expert
admin@firepower:/mnt/boot$ sudo su -
Password: 
root@firepower:~# cd /var/data/cores
root@firepower:cores# ls -l | grep -i core
-rw-r--r-- 1 root root 110295949 Apr 24 14:51 core.lina.11.22781.1745506311.gz
root@firepower:cores# sha512sum core.lina.11.22781.1745506311.gz
d654eb3e6a2852d43fb927daaddabea5297e0eaad4abe797e7692bcdcfe825d2ed73931427cb85bae4ffdf685387e916b82313de51a3559b72bde1a987a382c6 core.lina.11.22781.1745506311.gz
root@firepower:cores# ftp 10.10.10.1
Connected to 10.10.10.1.
220 Microsoft FTP Service
Name (10.10.10.1:admin): anonymous
331 User name ok, need password
Password: 
230 User logged in
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> bin
200 Type set to I.
ftp> put core.lina.11.22781.1745506311.gz
local: core.lina.11.22781.1745506311.gz remote: core.lina.11.22781.1745506311.gz
227 Entering passive mode (10,10,1,21,231,84)
125 Using existing data connection
100% 
|***********************************************************************************************************|
105 MiB   52.09 MiB/s    00:00 ETA
226 Closing data connection; File transfer successful.
110295949 bytes sent in 00:02 (50.02 MiB/s)
ftp> quit
221 Service closing control connection
root@firepower:cores# cd /mnt/disk0
root@firepower:disk0# ls -l | grep -i crash
-rwxr-xr-x 1 root root 688157 Apr 24 14:52 crashinfo_20250424_145151_UTC
root@firepower:disk0# sha512sum crashinfo_20250424_145151_UTC
8121205d4ee87a77a5fcc1df400eb47fd7aba310d88e3907d3bd200f609024316a26b01d583ac4a94c27f5d5bbc696dd5e6550c76fdf692eb076fe44bb824f25  crashinfo_20250424_145151_UTC
root@firepower:disk0# ftp 10.10.10.1
Connected to 10.10.10.1.
220 Microsoft FTP Service
Name (10.10.10.1:admin): anonymous
331 User name ok, need password
Password: 
230 User logged in
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> bin
200 Type set to I.
ftp> put crashinfo_20250424_145151_UTC
local: crashinfo_20250424_145151_UTC remote: crashinfo_20250424_145151_UTC
227 Entering passive mode (10,10,1,21,231,92)
125 Using existing data connection
100% 
|***********************************************************************************************************|
672 KiB  100.93 MiB/s    00:00 ETA
226 Closing data connection; File transfer successful.
688157 bytes sent in 00:00 (14.37 MiB/s)
ftp> quit
221 Service closing control connection
root@firepower:disk0# exit
logout
admin@firepower:/mnt/boot$ exit
logout
> exit
firepower(local-mgmt)#
```

Submit all command output, hash values, and crashinfo and core files that were collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step 7 – Check ROM Monitor Settings

The ROM monitor firmware of the Cisco Firepower platform is executed when the appliance is powered up or reset. The firmware initializes the platform hardware and boots the Cisco FXOS operating system software. Because the ROM monitor settings are persistent if they have been synced to NVRAM, information about the ROM monitor variable values could indicate an attempt to influence the FXOS boot sequence. The set command can be used while in the ROM monitor prompt to see the value of the ROM monitor variables.

Note: This procedure must be executed from the appliance console.

Access ROM monitor mode by rebooting the Cisco Firepower appliance and pressing the Break or Esc key during the reload process when prompted, as shown in the following example:

```
firepower# connect local-mgmt 
firepower(local-mgmt)# reboot
Before rebooting, please take a configuration backup.
Do you still want to reboot? (yes/no):yes
Broadcast message from admin@firepower (Thu Jan 18 21:12:11 2024):

All shells being terminated due to system /sbin/reboot
Broadcast message from admin@firepower (Thu Jan 18 21:12:12 2024):
 Reboot requested by the user.
<13>Jan 18 21:12:13 admin: FXOS shutdown log started: pid = 29785 cmdline = /bin/sh/sbin/fxos_log_shutdown ####
[output truncated]

Rebooting... [ 5382.871024] reboot: Restarting system
******************************************************************************
Cisco System ROMMON, Version 1.0.18, RELEASE SOFTWARE
Copyright (c) 1994-2023  by Cisco Systems, Inc.
Compiled Thu 03/23/2023 16:16:11.64 by builder
******************************************************************************
Current image running: Boot ROM1
Last reset cause: ResetRequest (0x00001000)
DIMM0 : Present

Platform FPR-1120 with 16384 MBytes of main memory
Detected Nic devid(0) 15398086
bus: 3 dev: 0 func: 0
BIOS has been successfully locked !!
MAC Address: 6c:03:b5:27:e8:00

Use BREAK or ESC to interrupt boot.
Use SPACE to begin boot immediately.
Boot interrupted.  
rommon 1 >
```

The following example shows the output of the ROM monitor set command on a Cisco Firepower platform:

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

The preceding example depicts a platform where the ROM monitor values are at their default values and have not been altered.

To return the Cisco Firepower platform to normal operation, use the boot command at the ROM monitor prompt, as shown in the following example:

```
rommon 2 > boot
Located .boot_string 
Image size 60 inode num 15, bks cnt 1 blk size 8*512

Located installables/switch/fxos-k8-fp1k-lfbff.2.12.0.530.SPA 
Image size 199156688 inode num 65163, bks cnt 48623 blk size 8*512
############################################################################################################## ##############################################
[output truncated]
```

Submit all command output that was obtained in this section to the relevant TAC SR.

## Related Documentation

For additional information about Cisco Software Integrity Assurance, as well as forensic investigation procedures for other platforms, see the following link:

Cisco Security Tactical Resources

https://tools.cisco.com/security/center/tacticalresources.x

## Firepower 200, 1000, 2100, 3100, and 6100 Series Forensic Data Collection Checklist

Step 1 – Create the Firepower Device Problem Description

Device problem description uploaded to SR

Step 2 – Document FTD Runtime Environment

Output of Cisco FXOS show tech-support uploaded to SR

Output of Cisco Firepower module show tech-support uploaded to SR

Step 3 – Verify FTD System File Integrity

Output of find /ngfw/var/sf/.icdb/* and hashes uploaded to SR

Output of which executed on shell scripts uploaded to SR

Shell scripts, certificates, log file, and hash database added to .tar file

.tar file and its associated hash value uploaded to SR

Step 4 – Verify Digitally Signed Image Authenticity

Output of show software authenticity file uploaded to SR

Output of show software authenticity running uploaded to SR

Output of show software authenticity keys uploaded to SR

Step 5 – Verify FTD .text Memory Segment Integrity

Output of verify on memory text segment uploaded to SR

Copy of memory text segment uploaded to SR

Step 6 – Obtain Firepower crashinfo / core File

Output of crashinfo uploaded to SR

crashinfo file uploaded to SR

core file uploaded to SR

Hash values of crashinfo and core files uploaded to SR

Step 7 – Check ROM Monitor Settings

Output of set command uploaded to SR

## Appendix A – Firepower 200, 1000, 2100, 3100, and 6100 Series Platform That Is Running ASA Software

Note: Only execute the commands in Appendix A if Cisco ASA Software is running on a Cisco Firepower 200, 1000, 2100, 3100, and 6100 Series appliance.

Execute the following commands from the Cisco ASA CLI prompt:

```
enable
connect fxos admin
connect local-mgmt
show tech-support fprm detail
exit
exit
copy disk0:/fxos/<filename> ftp: | scp: | tftp:
```

An example of this procedure follows.

```
ciscoasa> enable
Password: *********
ciscoasa# 
ciscoasa# connect fxos admin
Configuring session..
Connecting to FXOS....
Connected to FXOS. Escape character sequence is 'CTRL-^X'.

NOTICE: You have connected to the FXOS CLI with admin privileges.
Config commands and commit-buffer are not supported in appliance mode.
[output omitted]

firepower# connect local-mgmt
Warning: network service is not available when entering 'connect local-mgmt'
firepower(local-mgmt)# show tech-support fprm detail
The showtechsupport file will be located at workspace:/techsupport/20260812152922_firepower_FPRM.tar.gz

Initiating tech-support information task on FABRIC A ...

firepower(local-mgmt)# exit
firepower# exit
Connection with FXOS terminated.
Type help or '?' for a list of available commands.

ciscoasa# dir fxos
Directory of disk0:/fxos/
340382  -rw-  7565355      15:30:08 Aug 12 2026  20260812152922_firepower_FPRM.tar.gz
1 file(s) total size: 7565355 bytes
16106127360 bytes total (15740329984 bytes free/97% free)

ciscoasa# copy disk0:/fxos/20260812152922_firepower_FPRM.tar.gz ftp:
Source filename [/fxos/20260812152922_firepower_FPRM.tar.gz]? 
Address or name of remote host []? 10.10.10.1
Destination filename [20260812152922_firepower_FPRM.tar.gz]? 
!!!!!!!
7565355 bytes copied in 0.420 secs
ciscoasa#
```

Next, execute the following commands from the Cisco ASA CLI prompt:

```
enable
show tech-support detail
dir /recursive all-filesystems
verify /sha-512 system:/text
copy system:/text ftp:
```

The output of show tech-support detail may also be redirected to a file server using either the FTP, SCP, SMB, or TFTP protocols. The following example depicts the required syntax if the FTP protocol is used:

```
show tech-support detail | redirect ftp://anonymous@10.10.10.1/tech-support-details.txt
```

An example of this procedure follows:

```
ciscoasa# show tech-support detail | redirect ftp://anonymous@10.10.10.1/show-tech-support.txt

ciscoasa# dir /recursive all-filesystems
Directory of disk0:/*
274941988  -rw-  116406136    19:20:38 Sep 12 2023  asdm.bin
268440446  -rw-  0            13:08:21 Mar 17 2024  coredumpfsysimage.bin
268439875  -rw-  1109         13:36:35 Mar 17 2024  asa-cmd-server.log
271838408  -rw-  39           13:36:34 Mar 17 2024  snortpacketinfo.conf
147407  -rw-  1901         13:08:20 Mar 17 2024  cspCfg.xml
Directory of disk0:/log
805367049  -rw-  2141         13:36:38 Mar 17 2024  lina_monitor.log
805367054  -rw-  0            13:36:33 Mar 17 2024  stdout_offload_app.log
805367055  -rwx  372361       17:17:23 Mar 17 2024  asa-miovif.log
805367058  -rw-  749          13:36:34 Mar 17 2024  lcore.log
805367060  -rwx  119861       13:39:57 Mar 17 2024  asa-appagent.log
805367061  -r--  3572         13:36:35 Mar 17 2024  asa_snmp.log
805367063  -rwx  108556       17:24:21 Mar 17 2024  asa-ssp_ntp.log
805367064  -rwx  0            13:09:15 Mar 17 2024  asa-fxos_xml.log
[output truncated]

ciscoasa# verify /sha-512 system:/text
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[output truncated]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Done!
verify /SHA-512 (system:/text) = efc7164423606abce9a67ca5d4202ffd2c14342c4639596acee526d37c2b4a7d2aa 4061629534557c122dbfb528935fdd79fabd9e855c8d6d58e936f6563f8c2

ciscoasa# copy system:/text ftp:                            
Source filename [text]? 
Address or name of remote host []? 10.10.10.1

Destination filename [text]? system.text.bin
73990144 bytes copied in 2.850 secs (36995072 bytes/sec)
ciscoasa#
```

Cisco highly recommends calculating a hash value on the copied memory segment file and comparing it to the hash value that was obtained on the recipient platform to ensure no errors were introduced during the file transfer process.

The following example utilizes the sha512sum utility, which is included with most Linux distributions:

```
root@ftp-server:~# sha512sum system.text.bin
efc7164423606abce9a67ca5d4202ffd2c14342c4639596acee526d37c2b4a7d2aa406162953 4557c122dbfb528935fdd79fabd9e855c8d6d58e936f6563f8c2 system.text.bin
root@ftp-server:~#
```

Note that the Cisco ASA verify command and the sha512sum utility both produce a SHA-512 hash value of efc7164423606abce9a67ca5d4202ffd2c14342c4639596acee526d37c2b4a7d2aa4061629534557 c122dbfb528935fdd79fabd9e855c8d6d58e936f6563f8c2 for the system.text.bin file.

ASA Module Core File Generation

Caution: This step contains commands that may cause the platform to reboot. It is of critical importance that all the preceding information-gathering steps have been completed successfully or important evidence may be permanently lost.

To initiate the core dump process, execute the following command in enable mode:

```
crashinfo force page-fault
```

The core dump may take some time to complete, depending on the amount of physical memory (RAM) installed on the device.

When the core dump process is complete, the ASA module will reboot.

```
ciscoasa# crashinfo force page-fault 
WARNING: This command will force a crash and cause a
         reboot. Do you wish to proceed? [confirm]: 
!! !! First Crash in tid: 24955 type: Page fault error: Address not mapped

Writing live core file to flash. Please do not reload.

Coredump starting....
Corehelper: /opt/cisco/csp/cores/core.lina.11.24829.1746100776
Waiting for Corehelper to finish....
Livecore: generating coredump of 24829
[New LWP 24941]
[New LWP 24942]
[New LWP 24943]
[New LWP 24944]
[New LWP 24945]
[New LWP 24947]
[New LWP 24948]
[New LWP 24955]
[New LWP 24957]
[New LWP 24958]
[New LWP 24959]
[New LWP 24960]
[New LWP 24961]
[New LWP 24962]
[New LWP 24963]
[New LWP 24964]
[New LWP 24965]
[New LWP 24966]
[New LWP 24993]
[New LWP 24994]
[New LWP 24995]
[New LWP 24996]
[New LWP 27356]
0x00007f3f71f4f2cd in ?? () from /lib64/libpthread.so.0
warning: target file /proc/24829/cmdline contained unexpected null characters
Saved corefile /opt/cisco/csp/cores/core.lina.11.24829.1746100776
[Inferior 1 (process 24829) detached]
!!! !!! Corehelper [24946] Exit Code: 0
Coredumping took 0 min and 6 secs
[output truncated]
```

The core dump is written to a compressed file located on the /coredumpfs file system. The name of the file can be displayed using the dir command:

```
ciscoasa# dir disk0:/coredumpfsys

Directory of disk0:/coredumpfsys/
11	drwx	16384	   07:50:37 Aug 03 2024  lost+found
1406273	drwx	4096       07:52:31 Aug 03 2024  sysdebug
24529	-rw-	125217750  11:59:42 May 01 2025 core.lina.11.24829.1746100776.gz

1 file(s) total size: 125217750 bytes
16106127360 bytes total (15739285504 bytes free/97% free)
```

It is highly recommended that a hash value be calculated on the core file obtained in this section so that any errors introduced by subsequent copying or transmission can be reliably detected.

```
ciscoasa# verify /sha-512 disk0:/coredumpfsys/core.lina.11.24829.1746100776.gz
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[output omitted]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Done!
verify /SHA-512 (disk0:/coredumpfsys/core.lina.11.24829.1746100776.gz) = 2e62ff2919a1c5ccc27b8cc5156633cb429f1a2c43037a6094ab9b4946f947a69536ca78e239bcc07f8d901862b9ce441cd15cf43bd4d1d5b273e8e336620bf6
ciscoasa#
```

Lastly, copy the core file off the platform using FTP, SCP, or TFTP.

```
ciscoasa# copy disk0:/coredumpfsys/core.lina.11.24829.1746100776.gz ftp:
Source filename [/coredumpfsys/core.lina.11.24829.1746100776.gz]? 
Address or name of remote host []? 10.10.10.1
Destination filename [core.lina.11.24829.1746100776.gz]? 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
125217750 bytes copied in 5.830 secs (25043550 bytes/sec)
```

Submit all command output (including all computed hash values), a copy of the system:/text memory segment, and the core file collected in this section to the relevant TAC SR.

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
|  |  |  |  |
| 1.0 | 4/5/2024 | Dan Maunz | Initial public release. |
| 1.1 | 8/27/2024 | Dan Maunz | Integrated 2100 Series. |
| 1.2 | 5/1/2025 | Dan Maunz | Validated procedures on 7.4.2. |
| 1.3 | 6/25/2026 | Dan Maunz | Validated procedures on 7.6.4. |
| 1.4 | 6/30/2026 | Dan Maunz | Added 3100 and 6100 platforms. |
| 1.5 | 8/18/2026 | Dan Maunz | Added FXOS show tech-support to Appendix A. |