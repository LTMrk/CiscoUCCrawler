---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-nx-os-forensic-investigation-html-c1675dae2c
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/nx-os_forensic_investigation.html
retrieved_at: 2026-09-01T14:10:58.220467+00:00
---

Home / Cisco Security

Cisco NX-OS Software Forensic Data Collection Procedures

# Cisco NX-OS Software Forensic Data Collection Procedures

Introduction

Prerequisites

Step One - Create the NX-OS Device Problem Description

Step Two - Collect an NX-OS show tech-support File

Step Three - Verify NX-OS Digitally Signed Image Authenticity

Step Four - Gather Critical Process Core Files

Step Five - Collect Non-Volatile System Information and Artifacts

Related Documentation

Nexus Platform Forensic Response Checklist

Appendix A - Forensic Data Collection for NX-OS Platforms in ACI Boot Mode

Revision History

## Introduction

This document provides steps to collect forensic information from appliances that are running Cisco NX-OS Software when compromise or tampering is suspected. It outlines commands that can be run to gather evidence for an investigation along with the respective output that should be collected after running these commands. This document also provides information about how to perform integrity checks on an NX-OS system, and it includes procedures for collecting core files from critical system processes.

Caution: Do not reboot the device. Rebooting a device during the initial stage of an assessment will irrecoverably lose all volatile information that the device contains, such as RAM contents, ARP and routing tables, NAT translations, and ACL hit and drop counts.

Note: If it is suspected that a device has been tampered with or compromised, Cisco strongly recommends isolating the device from the network before conducting an initial forensic examination. This action may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device that is under investigation.

If you require assistance or have questions regarding the following procedures, contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains five main sections:

- Create the NX-OS Device Problem Description : Describes why the platform is a candidate for forensic examination

- Collect an NX-OS show tech-support File : Collects platform configuration and runtime state

- Verify NX-OS Digitally Signed Image Authenticity : Examines the NX-OS operating system for proper signing characteristics

- Obtain Core Files : Obtains core files for critical system processes

- Collect Non-Volatile System Information and Artifacts : Retrieves Docker configuration settings, enumerates deployed containers, and important system information

## Prerequisites

The procedures outlined in this document assume that the reader has a basic understanding of Cisco NX-OS Software and Linux command syntax.

A valid cisco.com account is required to view individual NX-OS Software file hashes for software file integrity checking. For customers without a cisco.com account, a publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded from: https://www.cisco.com/c/en/us/about/trust-center/downloads.html

A Cisco Technical Assistance Center (TAC) service request (SR) for the device in question is required because these procedures assume that the information gathered in each step will be uploaded to a TAC SR.

Cisco highly recommends using the Cisco NX-OS Software Forensic Data Collection shell script , which can be downloaded from https://sec.cloudapps.cisco.com/security/center/resources/nx-os_forensic_script.html . This script automates Steps Two through Five of the collection procedure and will print out the appropriate instructions for creating core dumps of any suspicious critical processes that are detected.

Note: The examples that are used in this document are based on Cisco NX-OS Software Release 10.5.3 command syntax and the output produced by a command may vary dependent on the software release deployed and/or features supported or configured on the device. Not all commands used in these procedures may be supported on earlier releases of the software.

## Step One – Create the NX-OS Device Problem Description

Describe in as much detail as possible why the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior that cannot be attributed to a misconfiguration or a software or hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific software releases of the following products: Cisco ASA, FMC, FTD, FXOS, IOS, IOS XE, NX-OS, and NX-OS in ACI Mode.

https://sec.cloudapps.cisco.com/security/center/softwarechecker.x

Record any results that are returned by the tool that may explain the anomalous behavior being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA, FMC, FTD, and FXOS Software, the tool contains only vulnerability information for Cisco Security Advisories first published from January 2022 onward and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

If you are executing a manual collection, submit the problem description to the relevant TAC SR, along with any relevant results that are obtained from the Cisco Software Checker and collected in this section. Then proceed to the next section of this document. If using the Cisco NX-OS Software Forensic Data Collection shell script, simply upload the device_hostname -forensics.tar.gz file that the script will create to the relevant TAC SR.

## Step Two – Collect an NX-OS show tech-support File

Note: The procedures in the remainder of this document are applicable to platforms in NX-OS boot mode and will not work on platforms in Application Centric Infrastructure (ACI) boot mode. To determine the boot mode, issue the show version command and examine the filename of the boot image, as depicted in the following example:

```
nxosv# show version | inc NXOS
  NXOS: version 10.5(3) [Feature Release]
  NXOS image file is: bootflash:///nxos64-cs.10.5.3.F.bin
  NXOS compile time:  4/15/2025 31:00:00 [04/19/2025 05:20:48]
nxosv#
```

Cisco NX-OS filenames begin with nxos [beginning with Cisco NX-OS Release 7.0(3)I2(1)] or n9000, while ACI filenames begin with aci-n9000.

If the platform is running in ACI boot mode, skip the remaining steps in this document and go to Appendix A.

To complete the initial stage of forensic information gathering, use the show tech-support details command. The output of this command may be redirected to a secure location from the CLI. Adjust the file system path, username, destination, and VRF as appropriate for your environment.

Execute the following command at the diagnostic CLI and record the output:

```
show tech-support details > file_system_path / file_name vrf vrf_name
```

An example of this procedure follows:

```
nxosv# show tech-support details > ftp://anonymous@10.10.1.21/show-tech.log vrf management
Show tech detail can take more than 5 minutes to complete. Please Wait ...
eth2: error fetching interface information: Device not found
eth3: error fetching interface information: Device not found
cat: /proc/net/eth0_stats: No such file or directory
Password:

***** Transfer of file Completed Successfully *****
```

Submit all command output collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Three – Verify NX-OS Digitally Signed Image Authenticity

Cisco NX-OS Software implements digitally signed system images on most platforms. Digitally signed Cisco NX-OS Software uses asymmetric (public-key) cryptography, which increases the security posture of Cisco Nexus devices by ensuring that the system image has not been altered.

Certain platforms that are running Cisco NX-OS Software also support Cisco Secure Boot technologies. Cisco Secure Boot is a secure startup process that a Cisco device performs each time it boots. Beginning with the initial power-on, a special-purpose hardware device known as the Trust Anchor module verifies the integrity of the ROM monitor code and the NX-OS image by using digital signatures as each is loaded. If any failures are detected, the user is notified of the error, and the device will wait for the operator to correct the error. This prevents the network device from executing tainted network software.

For additional information, see the Cisco Trustworthy Technologies Data Sheet.

Verify the authenticity and integrity of a system image file by using the following commands:

```
show software authenticity running
show software authenticity file path/filename
show software authenticity keys
```

An example of this procedure follows:

```
nxosv# show software authenticity running 

NXOS IMAGE
------------------------
Image type                    : Release
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : Nexus9k
        Organization Name     : CiscoSystems
    Certificate Serial Number : 66A30516
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : BIOS
        Verifier Version      :

nxosv# show software authenticity file bootflash:///nxos64-cs.10.5.1.F.bin
/bootflash/nxos64-cs.10.5.1.F.bin
Image type                    : Release
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : Nexus9k
        Organization Name     : CiscoSystems
    Certificate Serial Number : 66A30516
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```

The Organization Unit, Organization Name, and Certificate Serial Number values are visible in the preceding output example. Review these values to verify that a system image signature is valid, and confirm that the same certificate serial number is returned from both the show software authenticity running command and the show software authenticity file command for each file. In the preceding examples, each authenticity check of the following images produces a value of 609DE09C:

•   System running image

•   NX-OS system image on bootflash

Last, obtain a copy of the public keys by using the following command:

```
show software authenticity keys
```

An example of this procedure follows:

```
nxosv# show software authenticity keys 

Public Key #1 Information
-------------------------
Key Type             : Release  (PRIMARY KEY STORAGE)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        c6:64:53:69:18:a5:9d:1b:94:9b:fb:b3:6e:f0:c4:9f:
        ca:bc:60:2b:52:c5:f8:97:bb:dc:e0:af:82:df:a0:76:
        6a:bb:04:27:07:a8:47:81:25:34:8b:b6:3c:15:be:1d:
        a1:24:71:03:f1:26:8d:c4:14:80:eb:e0:b3:60:3d:cb:
        5c:f6:c2:18:08:8f:3a:a8:64:f2:08:8a:04:b2:e7:35:
        46:88:f1:24:ea:c0:d3:65:e6:3e:81:cd:65:62:41:dd:
        d7:e0:76:6c:a5:69:33:4d:05:af:ab:30:75:8b:09:b0:
        73:40:df:dc:22:b7:d9:e0:68:50:55:4f:91:15:7f:01:
        84:d8:d0:e7:53:1f:7e:a2:30:dd:6b:29:13:7c:ca:cb:
        ef:dc:76:ce:fa:22:87:cc:af:a1:ff:c6:f3:a9:6b:71:
        9f:d7:2e:e3:bc:85:13:24:10:d7:ae:5f:db:1b:7a:24:
        05:77:69:96:e3:38:cd:d8:1d:de:4a:b2:37:1a:30:23:
        7f:a1:51:7d:95:13:7c:cd:fb:6f:9f:1b:c2:79:8a:75:
        b2:39:79:e3:68:b0:f2:c0:13:c0:f2:b5:94:49:69:30:
        78:7d:6b:76:85:a5:94:8b:1b:94:62:a8:4e:2a:b2:7a:
        42:ae:a4:64:af:86:60:9e:b1:38:c3:72:71:6a:01:87
Exponent (4 bytes)   : 10001
Key Version          : A
Product Name         : Nexus9k

Public Key #2 Information
-------------------------
Key Type             : Development  (PRIMARY KEY STORAGE)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        b2:40:fe:ef:07:b0:c8:bb:ae:49:95:be:fe:37:c4:0e:
        e5:fb:fe:56:16:a6:66:80:2e:4c:cd:93:b9:11:2c:6a:
        01:3b:06:cf:74:ad:d4:59:68:be:e6:38:63:ec:25:0c:
        56:8d:85:fa:7e:36:c2:cc:13:3b:01:df:6f:9f:cc:a0:
        e7:8d:59:6a:2e:20:b1:48:d4:a9:79:63:1e:07:d2:a5:
        09:c9:67:f2:4c:76:e4:42:25:a9:1b:2d:e8:37:68:4e:
        a5:ea:36:1f:8d:d7:20:23:da:44:0d:19:1f:61:13:d3:
        c2:e9:38:d9:14:b0:2a:f7:4e:69:e0:25:46:a7:79:ad:
        d8:0d:e3:e6:d0:cf:6f:2c:6f:b3:ae:61:25:cc:ce:17:
        c1:ad:37:79:8a:d6:f5:1d:97:d4:0a:a9:6f:d2:7b:3c:
        15:9c:bd:a1:9d:9d:ad:7b:72:45:26:3d:d9:a7:4e:46:
        6f:4c:3a:7c:e2:f8:fc:8c:59:75:0f:8f:eb:9c:20:bf:
        7a:e3:d9:53:20:86:9c:c9:70:62:84:3f:0c:6b:1c:ee:
        90:97:57:8a:e2:d1:5c:08:f3:26:a1:f2:a7:b4:35:ae:
        7c:ab:f1:c0:81:4a:be:f7:ca:bd:6e:a5:7d:0c:e1:ad:
        c9:f8:25:40:79:90:c6:cd:2c:01:c3:f8:93:ed:51:1b
Exponent (4 bytes)   : 10001
Key Version          : A
Product Name         : Nexus9k

Public Key #3 Information
-------------------------
Key Type             : Release  (ROLLOVER KEY STORAGE)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        c6:64:53:69:18:a5:9d:1b:94:9b:fb:b3:6e:f0:c4:9f:
        ca:bc:60:2b:52:c5:f8:97:bb:dc:e0:af:82:df:a0:76:
        6a:bb:04:27:07:a8:47:81:25:34:8b:b6:3c:15:be:1d:
        a1:24:71:03:f1:26:8d:c4:14:80:eb:e0:b3:60:3d:cb:
        5c:f6:c2:18:08:8f:3a:a8:64:f2:08:8a:04:b2:e7:35:
        46:88:f1:24:ea:c0:d3:65:e6:3e:81:cd:65:62:41:dd:
        d7:e0:76:6c:a5:69:33:4d:05:af:ab:30:75:8b:09:b0:
        73:40:df:dc:22:b7:d9:e0:68:50:55:4f:91:15:7f:01:
        84:d8:d0:e7:53:1f:7e:a2:30:dd:6b:29:13:7c:ca:cb:
        ef:dc:76:ce:fa:22:87:cc:af:a1:ff:c6:f3:a9:6b:71:
        9f:d7:2e:e3:bc:85:13:24:10:d7:ae:5f:db:1b:7a:24:
        05:77:69:96:e3:38:cd:d8:1d:de:4a:b2:37:1a:30:23:
        7f:a1:51:7d:95:13:7c:cd:fb:6f:9f:1b:c2:79:8a:75:
        b2:39:79:e3:68:b0:f2:c0:13:c0:f2:b5:94:49:69:30:
        78:7d:6b:76:85:a5:94:8b:1b:94:62:a8:4e:2a:b2:7a:
        42:ae:a4:64:af:86:60:9e:b1:38:c3:72:71:6a:01:87
Exponent (4 bytes)   : 10001
Key Version          : A
Product Name         : Nexus9k

Public Key #4 Information
-------------------------
Key Type             : Development  (ROLLOVER KEY STORAGE)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        b2:40:fe:ef:07:b0:c8:bb:ae:49:95:be:fe:37:c4:0e:
        e5:fb:fe:56:16:a6:66:80:2e:4c:cd:93:b9:11:2c:6a:
        01:3b:06:cf:74:ad:d4:59:68:be:e6:38:63:ec:25:0c:
        56:8d:85:fa:7e:36:c2:cc:13:3b:01:df:6f:9f:cc:a0:
        e7:8d:59:6a:2e:20:b1:48:d4:a9:79:63:1e:07:d2:a5:
        09:c9:67:f2:4c:76:e4:42:25:a9:1b:2d:e8:37:68:4e:
        a5:ea:36:1f:8d:d7:20:23:da:44:0d:19:1f:61:13:d3:
        c2:e9:38:d9:14:b0:2a:f7:4e:69:e0:25:46:a7:79:ad:
        d8:0d:e3:e6:d0:cf:6f:2c:6f:b3:ae:61:25:cc:ce:17:
        c1:ad:37:79:8a:d6:f5:1d:97:d4:0a:a9:6f:d2:7b:3c:
        15:9c:bd:a1:9d:9d:ad:7b:72:45:26:3d:d9:a7:4e:46:
        6f:4c:3a:7c:e2:f8:fc:8c:59:75:0f:8f:eb:9c:20:bf:
        7a:e3:d9:53:20:86:9c:c9:70:62:84:3f:0c:6b:1c:ee:
        90:97:57:8a:e2:d1:5c:08:f3:26:a1:f2:a7:b4:35:ae:
        7c:ab:f1:c0:81:4a:be:f7:ca:bd:6e:a5:7d:0c:e1:ad:
        c9:f8:25:40:79:90:c6:cd:2c:01:c3:f8:93:ed:51:1b
Exponent (4 bytes)   : 10001
Key Version          : A
Product Name         : Nexus9k

Public Key #5 Information
-------------------------
Key Type             : Release  (BACKUP KEY STORAGE)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        c6:64:53:69:18:a5:9d:1b:94:9b:fb:b3:6e:f0:c4:9f:
        ca:bc:60:2b:52:c5:f8:97:bb:dc:e0:af:82:df:a0:76:
        6a:bb:04:27:07:a8:47:81:25:34:8b:b6:3c:15:be:1d:
        a1:24:71:03:f1:26:8d:c4:14:80:eb:e0:b3:60:3d:cb:
        5c:f6:c2:18:08:8f:3a:a8:64:f2:08:8a:04:b2:e7:35:
        46:88:f1:24:ea:c0:d3:65:e6:3e:81:cd:65:62:41:dd:
        d7:e0:76:6c:a5:69:33:4d:05:af:ab:30:75:8b:09:b0:
        73:40:df:dc:22:b7:d9:e0:68:50:55:4f:91:15:7f:01:
        84:d8:d0:e7:53:1f:7e:a2:30:dd:6b:29:13:7c:ca:cb:
        ef:dc:76:ce:fa:22:87:cc:af:a1:ff:c6:f3:a9:6b:71:
        9f:d7:2e:e3:bc:85:13:24:10:d7:ae:5f:db:1b:7a:24:
        05:77:69:96:e3:38:cd:d8:1d:de:4a:b2:37:1a:30:23:
        7f:a1:51:7d:95:13:7c:cd:fb:6f:9f:1b:c2:79:8a:75:
        b2:39:79:e3:68:b0:f2:c0:13:c0:f2:b5:94:49:69:30:
        78:7d:6b:76:85:a5:94:8b:1b:94:62:a8:4e:2a:b2:7a:
        42:ae:a4:64:af:86:60:9e:b1:38:c3:72:71:6a:01:87
Exponent (4 bytes)   : 10001
Key Version          : A
Product Name         : Nexus9k

Public Key #6 Information
-------------------------
Key Type             : Development  (BACKUP KEY STORAGE)
Public Key Algorithm : RSA
Modulus (256 bytes)   :
        b2:40:fe:ef:07:b0:c8:bb:ae:49:95:be:fe:37:c4:0e:
        e5:fb:fe:56:16:a6:66:80:2e:4c:cd:93:b9:11:2c:6a:
        01:3b:06:cf:74:ad:d4:59:68:be:e6:38:63:ec:25:0c:
        56:8d:85:fa:7e:36:c2:cc:13:3b:01:df:6f:9f:cc:a0:
        e7:8d:59:6a:2e:20:b1:48:d4:a9:79:63:1e:07:d2:a5:
        09:c9:67:f2:4c:76:e4:42:25:a9:1b:2d:e8:37:68:4e:
        a5:ea:36:1f:8d:d7:20:23:da:44:0d:19:1f:61:13:d3:
        c2:e9:38:d9:14:b0:2a:f7:4e:69:e0:25:46:a7:79:ad:
        d8:0d:e3:e6:d0:cf:6f:2c:6f:b3:ae:61:25:cc:ce:17:
        c1:ad:37:79:8a:d6:f5:1d:97:d4:0a:a9:6f:d2:7b:3c:
        15:9c:bd:a1:9d:9d:ad:7b:72:45:26:3d:d9:a7:4e:46:
        6f:4c:3a:7c:e2:f8:fc:8c:59:75:0f:8f:eb:9c:20:bf:
        7a:e3:d9:53:20:86:9c:c9:70:62:84:3f:0c:6b:1c:ee:
        90:97:57:8a:e2:d1:5c:08:f3:26:a1:f2:a7:b4:35:ae:
        7c:ab:f1:c0:81:4a:be:f7:ca:bd:6e:a5:7d:0c:e1:ad:
        c9:f8:25:40:79:90:c6:cd:2c:01:c3:f8:93:ed:51:1b
Exponent (4 bytes)   : 10001
Key Version          : A
Product Name         : Nexus9k
nxosv#
```

Submit all command output and any system images collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Four – Gather Critical Process Core Files

Note: The following procedure requires the bash shell feature to be enabled. Use the following command at the Cisco NX-OS CLI prompt to determine the status of the bash shell feature:

```
show feature | inc bash
```

If this command returns a value of disabled, enter configuration mode and execute the following command to enable the bash shell feature:

```
feature bash-shell
```

Next, execute the following commands to run the bash shell, obtain root privileges, and check that account rights have been elevated:

```
run bash
sudo su –
id
```

An example of this procedure follows:

```
nxosv# show feature | inc bash
bash-shell     1      enabled

nxosv#run bash
bash-4.4$ sudo su -

root@nxosv#id
uid=0(root) gid=0(root) groups=0(root)
```

In the next step, use the Linux pidof command to find the process IDs (PIDs) for the following NX-OS system processes:

```
licmgr – license manager
mts_mgr – message transaction system manager
netstack – IP stack
netstack_dummy – Configured IP stack features (e.g. IPv6, etc.)
sysmgr – system and high availability manager
```

An example of this procedure follows:

```
root@nxosv#pidof licmgr
32246

root@nxosv#pidof mts_mgr
32318

root@nxosv#pidof netstack
32686

root@nxosv#pidof netstack_dummy
32750 32752 32757

root@nxosv#pidof sysmgr
19892
```

The list of critical processes along with their PID values now looks like the following:

```
licmgr         32246
mts_mgr        32318
netstack       32686
netstack_dummy 32750
netstack_dummy 32752
netstack_dummy 32757
sysmgr         19892
```

Note: The number of netstack_dummy processes is dependent on the IP features that are configured on a particular platform. It is important to obtain a core file for each netstack_dummy process that is executing on the platform.

Next, use the Linux echo and cat commands to set the core dump filters to a value of 0x7f for each process and check that the value is correctly set:

```
echo 0x7f > /proc/<PID>/coredump_filter
cat /proc/<PID>/coredump_filter
```

An example of this procedure follows:

```
root@nxosv#echo 0x7f > /proc/32246/coredump_filter
root@nxosv#cat /proc/32246/coredump_filter
0000007f

root@nxosv#echo 0x7f > /proc/32318/coredump_filter
root@nxosv#cat /proc/32318/coredump_filter        
0000007f

root@nxosv#echo 0x7f > /proc/32686/coredump_filter
root@nxosv#cat /proc/32686/coredump_filter        
0000007f

root@nxosv#echo 0x7f > /proc/32750/coredump_filter
root@nxosv#cat /proc/32750/coredump_filter        
0000007f

root@nxosv#echo 0x7f > /proc/32752/coredump_filter
root@nxosv#cat /proc/32752/coredump_filter        
0000007f

root@nxosv#echo 0x7f > /proc/32757/coredump_filter
root@nxosv#cat /proc/32757/coredump_filter        
0000007f

root@nxosv#echo 0x7f > /proc/19892/coredump_filter
root@nxosv#cat /proc/19892/coredump_filter
0000007f
```

Note: Recent versions of Cisco NX-OS Software incorporate additional operating system security controls. To use the gencore_script utility successfully in the next step, gdb safe path loading must be temporarily disabled with the following command:

```
echo add-auto-load-safe-path / > /root/.gdbinit
```

This file may be deleted after process core dumps are completed with the following command:

```
rm /root/.gdbinit
```

The gencore_script utility may also produce numerous messages as depicted below, and these can be safely ignored:

```
unsupported GNU_PROPERTY_TYPE (5) type: 0xc0010001
```

Note: It is highly recommended that process core dumping is performed on the console as creating core files for processes such as netstack may temporarily impact traffic destined to or transiting the platform.

Next, use the gencore_script utility to collect a core file from each of the critical processes:

```
/isan/bin/gencore_script <pid> <file>
```

Note: If the gencore_script terminates prematurely with a timeout error and a core file is not created, rerun the script with output redirected to /dev/null as depicted in the following example:

```
/isan/bin/gencore_script <pid> <file> > /dev/null
```

An example of this procedure follows:

```
root@nxosv#/isan/bin/gencore_script 32246 licmgr
[output truncated]
0xf7fb5c89 in __kernel_vsyscall ()
(gdb) generate-core-file
Saved corefile core.32246
(gdb) q
A debugging session is active.

        Inferior 1 [process 32246] will be detached.

Quit anyway? (y or n) y
Detaching from program: /isan/bin/licmgr, process 32246
[Inferior 1 (process 32246) detached]
root@nxosv#

root@nxosv#/isan/bin/gencore_script 32318 mts_mgr
[output truncated]
0xf7fb9c89 in __kernel_vsyscall ()
(gdb) generate-core-file
Saved corefile core.32318
(gdb) q
A debugging session is active.

        Inferior 1 [process 32318] will be detached.

Quit anyway? (y or n) y
Detaching from program: /isan/bin/mts_mgr, process 32318
[Inferior 1 (process 32318) detached]
root@nxosv#

#
# Note that the routing-sw sub-directoy must be prepended to the file         
# parameter to successfully generate a core file for the netstack and         
# netstack_dummy processes!
#
root@nxosv#/isan/bin/gencore_script 32686 routing-sw/netstack
[output truncated]
0xf7fafc89 in __kernel_vsyscall ()
(gdb) generate-core-file
warning: target file /proc/32686/cmdline contained unexpected null characters
Saved corefile core.32686
(gdb) q
A debugging session is active.

        Inferior 1 [process 32686] will be detached.

Quit anyway? (y or n) y
Detaching from program: /isan/bin/routing-sw/netstack, process 32686
[Inferior 1 (process 32686) detached]
root@nxosv#

root@nxosv#/isan/bin/gencore_script 32750 routing-sw/netstack_dummy
[output truncated]
0xf7fa1c89 in __kernel_vsyscall ()
(gdb) generate-core-file
warning: target file /proc/32750/cmdline contained unexpected null characters
Saved corefile core.32750
(gdb) q
A debugging session is active.

        Inferior 1 [process 32750] will be detached.

Quit anyway? (y or n) y
Detaching from program: /isan/bin/routing-sw/netstack_dummy, process 32750
[Inferior 1 (process 32750) detached]

root@nxosv#/isan/bin/gencore_script 32752 routing-sw/netstack_dummy
[output truncated]
0xf7eebc89 in __kernel_vsyscall ()
(gdb) generate-core-file
warning: target file /proc/32752/cmdline contained unexpected null characters
Saved corefile core. 32752
(gdb) q
A debugging session is active.

        Inferior 1 [process 32752] will be detached.

Quit anyway? (y or n) y
Detaching from program: /isan/bin/routing-sw/netstack_dummy, process 32752
[Inferior 1 (process 32752) detached]

root@nxosv#/isan/bin/gencore_script 32757 routing-sw/netstack_dummy
[output truncated]
0xf7f4cc89 in __kernel_vsyscall ()
(gdb) generate-core-file
warning: target file /proc/32757/cmdline contained unexpected null characters
Saved corefile core. 32757
(gdb) q
A debugging session is active.

        Inferior 1 [process 32757] will be detached.

Quit anyway? (y or n) y
Detaching from program: /isan/bin/routing-sw/netstack_dummy, process 32757
[Inferior 1 (process 32757) detached]

#
# Note that the ../sbin directory must be prepended to the file parameter to
# successfully generate a core file for the sysmgr process!
#
root@nxosv#/isan/bin/gencore_script 19892 ../sbin/sysmgr
[output truncated]
0xf7f1bc89 in __kernel_vsyscall ()
(gdb) generate-core-file
warning: target file /proc/19892/cmdline contained unexpected null characters
Saved corefile core.19892
(gdb) q
A debugging session is active.

        Inferior 1 [process 19892] will be detached.

Quit anyway? (y or n) y
Detaching from program: /isan/sbin/sysmgr, process 19892
[Inferior 1 (process 19892) detached]
root@nxosv#
```

Core files are stored in the /var/sysmgr/logs directory by the gencore_script. Cisco strongly recommends appending the process names to the current file name and calculating the hash values  for each core file before copying the files from the Nexus platform. To do so, use the following commands:

```
mv file_name file_name	
find /var/sysmgr/logs -name core.* | xargs sha512sum
```

After process names have been assigned to each core file and hash values have been calculated, each file should be compressed and moved to the bootflash partition where files can be easily copied from the Nexus platform using the following commands:

```
gzip filename
mv source destination
```

An example of this procedure follows:

```
root@nxosv#ls -la /var/sysmgr/logs              
total 3121252
drwxrwxrwx  2 root root        120 Jun 22 09:54 .
drwxrwxrwx 17 root root        400 Jun 22 07:21 ..
-rw-r--r--  1 root root  453313880 Jun 22 09:54 core.19892
-rw-r--r--  1 root root  447109248 Jun 22 09:26 core.32246
-rw-r--r--  1 root root  436145916 Jun 22 09:33 core.32318
-rw-r--r--  1 root root 1051243060 Jun 22 09:40 core.32686
-rw-r--r--  1 root root  269443508 Jun 22 09:42 core.32750
-rw-r--r--  1 root root  269443508 Jun 22 09:45 core.32752
-rw-r--r--  1 root root  269443508 Jun 22 09:48 core.32757

root@nxosv#mv /var/sysmgr/logs/core.19892 /var/sysmgr/logs/core.19892_sysmgr
root@nxosv#mv /var/sysmgr/logs/core.32246 /var/sysmgr/logs/core.32246_licmgr
root@nxosv#mv /var/sysmgr/logs/core.32318 /var/sysmgr/logs/core.32318_mts_mgr
root@nxosv#mv /var/sysmgr/logs/core.32686 /var/sysmgr/logs/core.32686_netstack
root@nxosv#mv /var/sysmgr/logs/core.32750 /var/sysmgr/logs/core.32750_netstack_dummy_267
root@nxosv#mv /var/sysmgr/logs/core.32752 /var/sysmgr/logs/core.32752_netstack_dummy_269
root@nxosv#mv /var/sysmgr/logs/core.32757 /var/sysmgr/logs/core.32757_netstack_dummy_271

root@nxosv#ls -la /var/sysmgr/logs                             
total 3121252
drwxrwxrwx  2 root root        120 Jun 22 10:15 .
drwxrwxrwx 17 root root        400 Jun 22 07:21 ..
-rw-r--r--  1 root root  453313880 Jun 22 09:54 core.19892_sysmgr
-rw-r--r--  1 root root  447109248 Jun 22 09:26 core.32246_licmgr
-rw-r--r--  1 root root  436145916 Jun 22 09:33 core.32318_mts_mgr
-rw-r--r--  1 root root 1051243060 Jun 22 09:40 core.32686_netstack
-rw-r--r--  1 root root  269443508 Jun 22 09:42 core.32750_netstack_dummy_267
-rw-r--r--  1 root root  269443508 Jun 22 09:45 core.32752_netstack_dummy_269
-rw-r--r--  1 root root  269443508 Jun 22 09:48 core.32757_netstack_dummy_271

root@nxosv#find /var/sysmgr/logs -name core.* | xargs sha512sum
7bc51c659ad890c000a8d0eb39e7b9a92afacf2e089c7c20a24b6f155f46c926c64c7145c1118775314cd627b5076403f8673224a01d83ca36811a95b5e17174
/var/sysmgr/logs/core.32686_netstack
b63e03a83b82efb93178e693da8bfc146bd46ebf992e68baf8d427de18e2e9b24de12c659f7f05ee6def87a95d49b14e098036b85bdfa80afc5293fdcd234fdb
/var/sysmgr/logs/core.32318_mts_mgr
42dd552c9424917e41ad2b58598c1c863653f7c983d7cc70a3f796a8cf05c3d4be409c84da10bfcbbb00997e96c9817fe485a07282bd72e520d578a0f8d8ffcb
/var/sysmgr/logs/core.32246_licmgr
a840285565934d155e66a2cdc4e4546e13c8da27ce7f7411f512eda4ae40f7344b0cff189fa6a1e12b641ce7491b12983e31a4ea1eae2ffe26f75cbc6768ae99
/var/sysmgr/logs/core.19892_sysmgr
fd64a5c6fe9f8334c01267e471c651bbd534f18e131224d20c8282296f9c03462505bccfc88686db5e637f1b696c36b0b6f9329ca16b33e936d28038c735c104
/var/sysmgr/logs/core.32757_netstack_dummy_271
d5bcf956ec0c2d5dfc5b69930abe4ef17f5a869f8c050580eed258de6d2f519474b3569a9df1343d750c291459a653e18c9d0362905bc2c5cb6020b12f66e5a1
/var/sysmgr/logs/core.32752_netstack_dummy_269
c3e4e094c34c4a43224aaac0efdaddc71ad120b101800c25c616e0a51f23c5273e49806204bb4b4620b9e040de7c7daa5c808fd941b4548741afc52b5673e69e
/var/sysmgr/logs/core.32750_netstack_dummy_267

root@nxosv#
root@nxosv#gzip /var/sysmgr/logs/core.*
root@nxosv#mv /var/sysmgr/logs/core.* /bootflash/.
root@nxosv#exit
logout
bash-4.4$ exit
exit

nxosv# copy bootflash:core.19892_sysmgr.gz ftp://anonymous@10.10.1.21/ vrf management
Password:                                         
***** Transfer of file Completed Successfully *****
Copy complete, now saving to disk (please wait)...
Copy complete.
nxosv# copy bootflash:core.32246_licmgr.gz ftp://anonymous@10.10.1.21/ vrf management
Password:                                                  
***** Transfer of file Completed Successfully *****
Copy complete, now saving to disk (please wait)...
Copy complete.
nxosv# copy bootflash:core.32318_mts_mgr.gz ftp://anonymous@10.10.1.21/ vrf management
Password:                                                  
***** Transfer of file Completed Successfully *****
Copy complete, now saving to disk (please wait)...
Copy complete.
nxosv# copy bootflash:core.32686_netstack.gz ftp://anonymous@10.10.1.21/ vrf management
Password:                                             
***** Transfer of file Completed Successfully *****
Copy complete, now saving to disk (please wait)...
Copy complete.
nxosv# copy bootflash:core.32750_netstack_dummy_267.gz ftp://anonymous@10.10.1.21/ vrf management
Password:                                             
***** Transfer of file Completed Successfully *****
Copy complete, now saving to disk (please wait)...
Copy complete.
nxosv# copy bootflash:core.32752_netstack_dummy_269.gz ftp://anonymous@10.10.1.21/ vrf management
Password:                                             
***** Transfer of file Completed Successfully *****
Copy complete, now saving to disk (please wait)...
Copy complete.
nxosv# copy bootflash:core.32757_netstack_dummy_271.gz ftp://anonymous@10.10.1.21/ vrf management
Password:                                             
***** Transfer of file Completed Successfully *****
Copy complete, now saving to disk (please wait)...
Copy complete.
nxosv#
```

Submit all command output, calculated hash values, and core files collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Five – Collect Non-Volatile System Information and Artifacts

This procedure outlines how to collect additional system information and artifacts that might be germane in a forensic assessment of a Nexus platform. The following categories of information are collected in this step:

- Hash value of system image file

- Hash value of kickstart image file (applicable for modular platforms only)

- Process Tree

- Process memory maps (smaps)

- DNF (Dandified YUM) information

- Container and image information

- Open socket connections

Note: The show boot command will return two variables when executed on modular platforms: a kickstart variable and a system variable. Calculate hash values on both files. An example of the typical output from show boot on a modular platform follows:

```
switch# show boot
Current Boot Variables:
sup-1
kickstart variable = bootflash:/n7000-s2-kickstart.8.1.1.bin
system variable = bootflash:/n7000-s2-dk9.8.1.1.bin
Boot POAP Disabled
No module boot variable set
[output truncated]
```

Note: Cisco NX-OS Software releases earlier than Release 10.1.2 may not support the dnf command.

An example of this entire procedure follows:

```
nxosv# show boot
Current Boot Variables:
sup-1
NXOS variable = bootflash:/nxos64-cs.10.5.3.F.bin
Boot POAP Disabled

Boot Variables on next reload:
sup-1
NXOS variable = bootflash:/nxos64-cs.10.5.3.F.bin
Boot POAP Disabled

nxosv# run bash
bash-5.1$ sha512sum /bootflash/nxos64-cs.10.5.3.F.bin
fae1736419293422b8bedd443e399eed4b3c6aaa58c5438a0e4bdef94a81740ce911fe7cb5518dcb0c072805e94617326580a564fa9b497e81d1bc6a06e9a7dc
/bootflash/nxos64-cs.10.5.3.F.bin

#
# Additionally, calculate a hash value for the kickstart image file when
# assessing a modular platform:
#
# Linux# sha512sum /bootflash/n7000-s2-kickstart.8.1.1.bin
# 6e09b4048301e98584b5b181c4731face1174167c42310a3ef5cdfdbb83ff266f7f0a4be892 
# fd1ff325367f2c6e95625543b30b8dcb6652d68c7f7ef4728c7bd
# /bootflash/n7000-s2-kickstart.8.1.1.bin
#

root@nxosv#pstree
init─┬─bootflash_sync.───inotifywait
     ├─crond
     ├─dockerd─┬─containerd───16*[{containerd}]
     │         └─16*[{dockerd}]
     ├─incrond
     ├─klogd
     ├─libvirt_lxc───systemd─┬─5*[agetty]
     │                       ├─crond
     │                       ├─dbus-daemon
     │                       ├─rsyslogd───2*[{rsyslogd}]
     │                       ├─sshd
     │                       ├─systemd-journal
     │                       └─systemd-logind
     ├─libvirtd_mon.sh───inotifywait
     ├─login───vsh.bin─┬─vsh.bin───bash───sudo───su───bash
     │                 └─{vsh.bin}
     ├─rpc.mountd
     ├─rpc.statd
     ├─rpcbind
     ├─sh───libvirtd───15*[{libvirtd}]
     ├─sshd
     └─sysmgr─┬─aaad
              ├─acllog
              ├─aclmgr
              ├─aclqos
              ├─adbm───{adbm}
              ├─am───17*[{am}]
              ├─arp───9*[{arp}]
              ├─ascii_cfg_serve
              ├─bios_daemon
              ├─bloggerd───3*[{bloggerd}]
              ├─bootvar
[output truncated]

root@nxosv#cat /proc/*/smaps | gzip > /bootflash/all-process-smaps.gz

root@nxosv#dnf history
ID     | Command line             | Date and time    | Action(s) | Altered 
--------------------------------------------------------------------------
     1 | --installroot=/data/jack | 2021-05-13 22:22 | Install   |  931 EE

root@nxosv#dnf repolist
Last metadata expiration check: 0:02:04 ago on Tue 22 Jun 2021 12:13:36 PM EST.
repo id                        repo name                               status
groups-repo                    Groups-RPM Database                        43
localdb                        Local RPM Database                          0
patching                       Patch-RPM Database                          0
thirdparty                     Thirdparty RPM Database                     0
wrl-repo                       Groups-RPM Database                         6

root@nxosv#dnf history userinstalled
Packages installed by user
bash-4.4.18-r0.corei7_64
bridge-utils-1.6-r0.corei7_64
dnsmasq-2.84-r0.corei7_64
expect-5.45.4-r0.corei7_64
glibc-binary-localedata-en-us-2.28-r0.corei7_64
inetutils-ftpd-1.9.4-r0.corei7_64
initramfs-boot-1.0-r2.corei7_64
initscripts-functions-1.0-r155.corei7_64
less-530-r0.corei7_64
[output truncated]

root@nxosv#dnf list --installed 
Installed Packages
attr.corei7_64                  2.4.47-r0                   @corei7_64
augeas.corei7_64                1.10.1-r0                   @corei7_64
augeas-lenses.corei7_64         1.10.1-r0                   @corei7_64
base-files.n9k_sup              3.0.14-r89                  @n9k_sup  
base-passwd.corei7_64           3.5.29-r0                   @corei7_64
bash.corei7_64                  4.4.18-r0                   @corei7_64
bfd.lib32_n9000                 2.0.0.0-10.1.2              @System   
bgp.lib32_n9000                 2.0.0.0-10.1.2              @System   
bind-libs.corei7_64             9.11.28-r0                  @corei7_64
binutils.corei7_64              2.31.1-r0                   @corei7_64
[output truncated]

root@nxosv#exit
logout
bash-4.4$ exit
exit
nxosv# show sockets connection

Total number of netstack tcp sockets: 5
Active connections (including servers)
        Protocol State/       Recv-Q/   Local Address(port)/
                 Context      Send-Q    Remote Address(port)
[host]: tcp(4/6) LISTEN       0         *(22)
                 Wildcard     0         *(*) 
[host]: tcp      LISTEN       0         *(161)
                 Wildcard     0         *(*) 
[host]: tcp(4/6) LISTEN       0         *(161)
                 Wildcard     0         *(*) 
[host]: tcp      ESTABLISHED  0         10.10.1.112(22)
                 management   96        10.10.1.21(59879) 
[host]: tcp      LISTEN       0         127.0.0.1(9876)
                 management   0         *(*) 

Total number of netstack udp sockets: 9
Active connections (including servers)
        Protocol State/       Recv-Q/   Local Address(port)/
                 Context      Send-Q    Remote Address(port)
[host]: udp6                  0         *(123)
                 Wildcard     0         *(*) 
[host]: udp                   0         *(123)
                 Wildcard     0         *(*) 
[host]: udp                   0         *(161)
                 Wildcard     0         *(*) 
[host]: udp6                  0         *(161)
                 Wildcard     0         *(*) 
[host]: udp                   0         127.0.0.1(130)
                 Wildcard     0         *(*) 

Total number of netstack raw sockets: 0
[output truncated]
```

Cisco Nexus switches support a guest shell feature that provides a Bash interface into a Linux execution space on the host system that is isolated from the Cisco NX-OS host operating system. This allows users to add software packages or update shared libraries without impacting the platform operating system.

Cisco Nexus switches also support access to the underlying Linux shell and support the use of Docker containers. Docker containers can be used to install custom software in a minimal environment, which can be used to enhance the capabilities of the platform.

Both the guest shell and Docker container environments should be examined when determining the integrity of the NX-OS operating system.

Guest shell commands:

```
show virtual-service list
show guestshell detail
guestshell
sudo su –
dnf history
dnf repolist
dnf history userinstalled
dnf list --installed
exit
exit
run bash
sudo su -
virsh list --all
```

An example of this procedure follows:

```
nxosv# show virtual-service list
Virtual Service List:
Name                    Status             Package Name
-----------------------------------------------------------------------
guestshell+             Activated          guestshell.ova

nxosv# show guestshell detail
Virtual service guestshell+ detail
  State                 : Activated
  Package information
    Name                : guestshell.ova
    Path                : /isanboot/bin/guestshell.ova
    Application
      Name              : GuestShell
      Installed version : 3.0(0.1)
      Description       : Cisco Systems Guest Shell
    Signing
      Key type          : Cisco release key
      Method            : SHA-1
    Licensing
      Name              : None
      Version           : None
  Resource reservation
    Disk                : 400 MB
    Memory              : 256 MB
    CPU                 : 1% system CPU

  Attached devices
    Type              Name        Alias
    ---------------------------------------------
    Disk              _rootfs                    
    Disk              /cisco/core                 
    Serial/shell                                 
    Serial/aux                                   
    Serial/Syslog                 serial2        
    Serial/Trace                  serial3
```

Note: If the installed version of guest shell returned by the show guestshell detail command is less than 3.0, the DNF utility may not be installed and the YUM command may be substituted in the next step as follows:

- dnf history → yum history

- dnf repolist → yum repolist

- dnf history userinstalled → N/A

- dnf list –installed → yum list installed

```
nxosv# guestshell 
[admin@guestshell ~]$ sudo su -
[root@guestshell ~]# dnf history
ID     | Command line           | Date and time    | Action(s)      | Altered
-----------------------------------------------------------------------------

[root@guestshell ~]# dnf repolist
repo id                         repo name
appstream                       CentOS Linux 8 - AppStream
baseos                          CentOS Linux 8 - BaseOS
extras                          CentOS Linux 8 - Extras

[root@guestshell ~]# dnf history userinstalled
Packages installed by user
acl-2.2.53-1.el8.x86_64
attr-2.4.48-3.el8.x86_64
audit-libs-3.0-0.17.20191104git1c2f876.el8.x86_64
basesystem-11-5.el8.noarch
bash-4.4.19-12.el8.x86_64
bc-1.07.1-5.el8.x86_64
brotli-1.0.6-2.el8.x86_64
bzip2-libs-1.0.6-26.el8.x86_64
ca-certificates-2020.2.41-80.0.el8_2.noarch
[output truncated]

[root@guestshell ~]# dnf list --installed
Installed Packages
acl.x86_64                      2.2.53-1.el8                         @System
attr.x86_64                     2.4.48-3.el8                         @System
audit-libs.x86_64               3.0-0.17.20191104git1c2f876.el8      @System
basesystem.noarch               11-5.el8                             @System
bash.x86_64                     4.4.19-12.el8                        @System
bc.x86_64                       1.07.1-5.el8                         @System
brotli.x86_64                   1.0.6-2.el8                          @System
bzip2-libs.x86_64               1.0.6-26.el8                         @System
ca-certificates.noarch          2020.2.41-80.0.el8_2                 @System
[output truncated]

[root@guestshell ~]# exit
logout
[admin@guestshell ~]$ exit
logout

nxosv# run bash
bash-4.4$ sudo su -

root@nxosv#virsh list --all
 Id     Name                State    
-------------------------------------
 6222   vdc_1_guestshell+   running
```

Docker containers are managed with the docker command line utility. The first step is to determine whether the Docker daemon is running or ever has run in the past.  Examine the daemon status and the filesystem for a Docker reserved area on the disk subsystem. It is important to employ the following logic when attempting to enumerate Docker containers:

- If the Docker daemon is not running and the dockerpart file does not exist, do not start Docker and skip all of the remaining steps in this section.

- If the Docker daemon is not running and the dockerpart file exists, start Docker and complete the steps in this section.

- If the Docker daemon is running, complete the steps in this section.

Docker commands:

```
run bash
sudo su -
service docker status
ls -la /bootflash | grep docker
service docker start
docker system info
docker images
docker container ls
docker network ls
```

An example of this procedure follows:

```
nxosv# run bash
bash-4.4$ sudo su -

root@nxosv#service docker status
dockerd is stopped

root@nxosv#ls -la /bootflash | grep docker
-rw-rw-r--  1 root  root           300000000 Jul  9 14:37 dockerpart
#
# In this example the docker daemon is not running but the dockerpart file
# exists on the filesystem, so we must start the service:
#

root@nxosv#service docker start
losetup: /bootflash/dockerpart: Warning: file does not fit into a 512-byte sector; the end of the file will be ignored.
Updating certificates in /etc/ssl/certs...
0 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
Starting dockerd with args '--storage-driver=overlay':  .

root@nxosv#docker system info
Containers: 1
 Running: 1
 Paused: 0
 Stopped: 0
Images: 4
Server Version: 18.09.0-ce
Storage Driver: overlay
 Backing Filesystem: extfs
 Supports d_type: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: bridge host macvlan null overlay
 Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: cfd04396dc68220d1cecbe686a6cc3aa5ce3667c.m (expected: 468a545b9edcd5932818eb9de8e72413e616e86e)
runc version: 6a2c15596845f6ff5182e2022f38a65e5dfa88eb (expected: 69663f0bd4b60df09991c08812a60108003fa340)
init version: N/A (expected: )
Kernel Version: 4.19.179
Operating System: Nexus 10.1(2)I9 (containerized)
OSType: linux
Architecture: x86_64
CPUs: 4
Total Memory: 7.781GiB
Name: nxosv
ID: DOJW:FYYP:5LJ2:EAP4:L5NC:DLFG:HQRV:L62R:RXAO:EY6N:MTWS:LHXE
Docker Root Dir: /var/lib/docker
Debug Mode (client): false
Debug Mode (server): false
Registry: https://index.docker.io/v1/
Labels:
Experimental: false
Insecure Registries:
 127.0.0.0/8
Live Restore Enabled: false

WARNING: bridge-nf-call-iptables is disabled
WARNING: bridge-nf-call-ip6tables is disabled

root@nxosv#docker images
REPOSITORY          TAG          IMAGE ID           CREATED            SIZE
nginx               latest       4cdc5dd7eaad       7 days ago         133MB
alpine              latest       d4ff818577bc       4 weeks ago        5.59MB
busybox             latest       69593048aa3a       5 weeks ago        1.24MB
networkboot/dhcpd   latest       b57b32205814       8 months ago       79.3MB

root@nxosv#docker container ls
CONTAINER ID    IMAGE    COMMAND     CREATED     STATUS        PORTS   NAMES
59f6237b5f18    alpine   "/bin/sh"   5 days ago  Up 2 minutes          alpine1

root@nxosv#docker network ls 
NETWORK ID          NAME                DRIVER              SCOPE
cb9b31e37201        bridge              bridge              local
edebff19ced2        host                host                local
64c7f5d2e8d8        none                null                local

root@nxosv#docker volume ls
DRIVER              VOLUME NAME
root@nxosv#
```

Note: Docker containers may be defined in virtual device contexts (VDCs) other than the default NX-OS vdc_1. It is highly recommended that all VDCs defined on the platform be examined for Docker container instances. The show vdc command can be used to display all defined VDCs.

Submit all command output, including any calculated hash values, collected in this section to the relevant TAC SR.

## Related Documentation

Additional information about Cisco Software Integrity Assurance, as well as forensic investigation procedures for other platforms, is available in Cisco Security Tactical Resources: https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## Nexus Platform Forensic Response Checklist

Step 1 – Create the NX-OS Device Problem Description

Device problem description uploaded to SR

Step 2 – Collect an NX-OS show tech-support File

Output of show tech-support uploaded to SR

Step 3 – Verify NX-OS Digitally Signed Image Authenticity

Output of show software authenticity running uploaded to SR

Output of show software authenticity file uploaded to SR

Output of show software authenticity keys uploaded to SR

Step 4 – Gather Critical Process Core Files

licmgr core file uploaded to SR

mts_mgr core file uploaded to SR

netstack core file uploaded to SR

netstack_dummy core files uploaded to SR

sysmgr core file uploaded to SR

Hash values of all core files uploaded to SR

Step 5 – Collect Non-Volatile System Information and Artifacts

Hash value of system image file uploaded to SR

Hash value of kickstart image uploaded to SR (if applicable)

Process tree uploaded to SR

Process memory maps uploaded to SR

DNF information uploaded to SR

Open socket connections uploaded to SR

Container and image information uploaded to SR

## Appendix A – Forensic Data Collection for NXOS Platforms in ACI Boot Mode

This appendix provides the steps to collect forensic information from NX-OS appliances in ACI boot mode. Run the following commands on each switch suspected of compromise or tampering and save all output to a log file.

Step One – Document basic system information:

```
leaf-101# show hostname
leaf-101# show version
leaf-101# show cores
```

Step Two – Collect environment, process, and file information:

```
leaf-101# uname -a
leaf-101# echo $PATH
leaf-101# ps auxwww
leaf-101# lsof
leaf-101# lsmod
leaf-101# netstat -anlp
leaf-101# find /bin /controller/*bin /isan /isanboot /lc /lib /sbin /usr -type f -exec sha256sum {} \;
```

Step Three – Check for cronjobs and Bash history files:

```
leaf-101# find /etc/cron* -follow -type f | xargs more | cat
leaf-101# cat {/root,~}/.bash_history
```

Step Four – Copy core dump files off the platform

Collect any core files listed in Step One from the platform. Core files are typically found in the /logflash/core/ directory on the ACI appliance or can be retrieved from the APIC controller by navigating to Admin > Export Policies > Core > default > Operational.

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
| 1.0 | October 1, 2021 | D.Maunz/J. Barnes | Initial Public Release |
| 1.1 | September 7, 2022 | D. Maunz | Validated procedure on v10.2.3 |
| 1.2 | December 20, 2023 | D. Maunz | Validated procedures on v10.4.1 |
| 1.3 | November 1, 2024 | D. Maunz | Validated procedures on v10.5.1 |
| 1.4 | June 26, 2025 | D. Maunz | Validated procedures on v10.5.3 |