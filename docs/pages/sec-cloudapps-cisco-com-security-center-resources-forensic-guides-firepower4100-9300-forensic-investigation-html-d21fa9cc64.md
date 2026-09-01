---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-firepower4100-9300-forensic-investigation-html-d21fa9cc64
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/firepower4100_9300_forensic_investigation.html
retrieved_at: 2026-09-01T14:10:28.823775+00:00
---

Home / Cisco Security

Cisco Firepower 4100 Series and 9300 Series Appliances Forensic Data Collection Procedures

# Cisco Firepower 4100 Series and 9300 Series Appliances Forensic Data Collection Procedures

Introduction

Prerequisites

Step One - Create Firepower Device Problem Description

Step Two - Document Firepower Runtime Environment

Step Three - Verify Integrity of FTD System Files

Step Four - Verify FXOS Digitally Signed Image Authenticity

Step Five - Enumerate Mezzanine Adapter Processes

Step Six - Verify FTD Memory .text Segment Integrity

Step Seven - Obtain  Firepower Crashinfo File and Core File

Step Eight - Check Firepower ROM Monitor Settings

Acknowledgments

Related Documentation

Firepower 4100 and 9300 Series Appliances Forensic Response Checklist

Appendix A - Firepower 4100/9300 Series Platforms Running ASA Software Modules

Revision History

## Introduction

This document provides steps to collect forensic information from Cisco Firepower 4100 Series and 9300 Series appliances that are running Cisco FXOS Software when compromise or tampering is suspected. It outlines commands that can be run to gather evidence for an investigation along with the respective output that should be collected after running these commands. This document also provides information about how to perform integrity checks on FXOS system images and on Cisco Firepower Threat Defense (FTD) application images, and it includes a procedure for collecting a memory dump, crashinfo file, and core file from a Firepower device.

Caution: DO NOT REBOOT THE DEVICE. Rebooting a  device during the initial stage of an assessment will irrecoverably lose all  volatile information that the device contains, such as RAM contents, ARP and routing  tables, NAT translations, and ACL hit and drop counts.

Caution: It is highly recommended that a device  suspected of tampering or compromise be isolated from the network before conducting  an initial forensic examination. This action may prevent remote unloading of  any implants or malware installed on the device and will prevent an adversary  from monitoring commands entered on the device that is under investigation.

If you require assistance or have questions regarding the following procedures, contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains eight main sections:

- Create  Firepower Device Problem Description: Describes why the platform is a candidate for forensic examination

- Document  Firepower Runtime Environment: Collects platform configuration and runtime state

- Verify Integrity of FTD System Files: Examines system file image hashes for inconsistencies

- Verify FXOS Digitally Signed Image Authenticity: Examines the FXOS operating system for proper signing characteristics

- Enumerate Mezzanine Adapter Processes: Lists the processes running on the mezzanine adapter

- Verify FTD Memory . text Segment Integrity: Retrieves and calculates a hash of the FTD .text segment

- Obtain Firepower Crashinfo File and Core File: Obtains crashinfo and core files from the running FTD application

- Check Firepower ROM Monitor Settings: Examines ROM monitor settings for remote system image loading

## Prerequisites

The procedures outlined in this document assume the reader has a basic understanding of Cisco FXOS Software, Cisco FTD Software, and Linux command syntax.

A  valid cisco.com account is required to view individual Cisco FXOS, ASA, and FTD software file hashes for software file integrity checking. Customers who do not  have a cisco.com account can download a publicly available comprehensive list  of file hashes (Bulk Hash file) from https://www.cisco.com/c/en/us/about/trust-center/downloads.html .

A Cisco Technical Assistance Center (TAC) service request (SR) for the device in question is required because these procedures assume that the information gathered in each step will be uploaded to a TAC SR.

Note: The examples used in this document are based on Cisco FXOS Software Release 2.16.2 and Cisco FTD Software Release 7.6.4 command syntax. The output that is produced by a command may vary depending on the software release that is deployed and/or the features that are supported or configured on the device. Not all commands that are used in these procedures may be supported on earlier releases of the software.

## Step One – Create  Firepower Device Problem Description

Describe in as much detail as possible why the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior that cannot be attributed to a misconfiguration or a software or hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific releases of Cisco Adaptive Security Appliance (ASA) Software, FTD Software, FXOS Software, IOS Software, IOS XE Software, NX-OS Software, NX-OS Software in ACI Mode, and Secure Firewall Management Center (FMC) Software.

Record any results that are returned by the tool that may explain the anomalous behavior that is being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA Software, FMC Software, FTD Software, and FXOS Software, the tool contains only vulnerability information for Cisco Security Advisories first published from January 2022 onward and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Submit the problem description and any relevant results that were obtained from the Cisco Software Checker to the relevant TAC SR and proceed to the next section of this document.

## Step Two - Document Firepower Runtime Environment

The initial stage of forensic information gathering is completed by using show tech-support commands in the Cisco FXOS and Firepower CLIs, and some of the output may vary depending on the Cisco FTD Software release and/or features that are supported or configured on the device.

Execute the following comands from the Cisco FXOS CLI prompt:

```
connect local-mgmt
show tech-support chassis 1 detail
copy workspace:/techsupport/<file_name> <destination>
```

Note: The copy command supports the FTP, HTTP, HTTPS, SCP, SFTP, and TFTP protocols.

Next, connect to the Cisco Firepower module CLI and collect the output of the show tech-support detail and dir /recursive all-filesystems commands.

Note: The slot ID is always 1 for Firepower 4100 Series appliances, and it can be 1 , 2 , or 3 for the  Firepower 9300 Series. It is highly recommended that each step in this document  be executed on each security service application instance. A list of  application instances and slot IDs can be obtained by executing the show  app-instance command at the FXOS CLI while in the ssa scope.

Execute the following command at the FXOS CLI  prompt:

```
connect module slot_id console
```

Execute the following command at the FTD CLI prompt:

```
system support diagnostic-cli
```

Execute each of the following commands at the diagnostic CLI and record the output:

```
enable
terminal pager 0
show tech-support detail
dir /recursive all-filesystems
```

Note: The output of the show tech-support detail command may be redirected to a file on the local filesystem, which can be copied off the platform at a later time. An example of this command follows:

```
show tech-support detail | redirect disk0:/tech-support-detail.txt
```

Submit all command output collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Three - Verify Integrity of FTD System Files

Connect to the FTD CLI. This can be accomplished  at the FXOS CLI by using the connect module slot_id console command.

At the FTD CLI, use the following commands to assume root privileges, run the  system file integrity checks, and collect the necessary files for forensic assessment:

Access expert mode and use the sudo command  to access the root account:

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

The verify_file_integ.sh script will return either “Successfully verified file integrity” or “Error: Failed to verify file integrity against the signed database,” which may indicate that system files have been tampered with.

Note: Older versions of Cisco FTD Software do not support the use of the force (-f) parameter on the verify file integrity script and require setting the FIPS environment variable first instead. If verify_file_integ.sh -f returns an error, execute export FIPS_MODE=1 and then verify_file_integ.sh (without the -f parameter).

Note: The Linux which command can be used to quickly locate the shell scripts in the next step. See the example below for more details.

Locate and retrieve copies of the following files:

```
verify_file_integ.sh
verify_signed_db.sh
db_manage.sh
/ngfw/etc/certs/*.crt
/ngfw/var/log/sf/verify_file_integ.log
/ngfw/var/tmp/merged-db/master.db
```

Create an archive of the files in the preceding list and copy the archive off the platform:

```
tar -cvf SR- sr_number .tar
sha512sum SR- sr_numbet .tar
ftp or scp
```

An example of this procedure follows:

```
FPR4150-1# connect module 1 console Telnet escape character is '~'.
Trying 127.5.1.1...
Connected to 127.5.1.1.
Escape character is '~'.
CISCO Serial Over LAN:
Close Network Connection to Exit

> expert *************************************************************
NOTICE - Shell access will be deprecated in future releases
         and will be replaced with a separate expert mode CLI.
**************************************************************
admin@firepower:/opt/cisco/csp/applications $ sudo su - Password: 

root@firepower:~# find /ngfw/var/sf/.icdb/* -name *.icdb.RELEASE.tar | xargs sha512sum b5800901d4ccb1df48b648edcda9b40b6766f86eee77ac700bd9e2921ebdd7e645bb8912592627
ffd6a54b7d8c82a55876724602a7c77764bb38367cf4adf2f4
/ngfw/var/sf/.icdb/0000/base-intel-6.4.0-102.icdb.RELEASE.tar
63c99b2b92895188f921bfbde6f000d670b65ac07642375b9d9ed8aedb63761441241006a86afb
047f7e27d02c10b4df4df8c860b8fba601f91b3a36bebf2cd8
/ngfw/var/sf/.icdb/0000/base-6.4.0-102.icdb.RELEASE.tar

#
# Note: the file names, number of files, and hash values may vary depending on 
# the version of software running on the appliance and whether any software   
# updates have been applied. It is extremely important that the output        
# (including file names and hashes) generated by the command above be         
# submitted to the TAC SR.
#

root@firepower:~# tail -n +1 /proc/*/smaps > /tmp/all-process-smaps.txt root@firepower:~# verify_file_integ.sh -f Running file integrity checks... Successfully verified file integrity # Identify the location of the system integrity scripts with the "which"      
# command:
root@firepower:~# which verify_file_integ.sh /ngfw/usr/local/sf/bin/verify_file_integ.sh
root@firepower:~# which verify_signed_db.sh /ngfw/usr/local/sf/bin/verify_signed_db.sh
root@firepower:~# which db_manage.sh /ngfw/usr/local/sf/bin/db_manage.sh

# Archive a copy of these scripts, along with all certificates found in
# /ngfw/etc/certs/, and the files /ngfw/var/log/sf/verify_file_integ.log and
# /ngfw/var/tmp/merged-db/master.db

root@firepower:~# tar -cvf SR-1234567890.tar 
/ngfw/usr/local/sf/bin/verify_file_integ.sh 
/ngfw/usr/local/sf/bin/verify_signed_db.sh /ngfw/usr/local/sf/bin/db_manage.sh 
/ngfw/etc/certs/*.crt /ngfw/var/log/sf/verify_file_integ.log 
/ngfw/var/tmp/merged-db/master.db /tmp/all-process-smaps.txt tar: Removing leading `/' from member names
/ngfw/usr/local/sf/bin/verify_file_integ.sh
/ngfw/usr/local/sf/bin/verify_signed_db.sh
/ngfw/usr/local/sf/bin/db_manage.sh
/ngfw/etc/certs/SRU_rel.crt
/ngfw/etc/certs/rel.crt
/ngfw/var/log/sf/verify_file_integ.log
/ngfw/var/tmp/merged-db/master.db
/tmp/all-process-smaps.txt

# Create a hash of the tar file:
root@firepower:~# sha512sum SR-1234567890.tar ec42b9928ba4cc3cfd8b10f67babcfb5bb4699d5d96504cb35addc46b47d9b8225cc4b91489023
3a605ff41d24e002eb11c682d76ff3c16561b4cfd3cc7df838  SR-1234567890.tar

# Copy the tar file off the platform using SCP:
root@firepower:~# scp SR-1234567890.tar anonymous@10.10.10.1: anonymous@10.10.10.1's password:
SR-1234567890.tar                             100%   15MB  43.5MB/s   00:00
          
root@firepower:~# exit logout
admin@firepower:/opt/cisco/csp/applications$ exit logout
> exit Disconnected from ftd(FTD-A) console!
Firepower-module1>~
telnet> quit Connection closed.
FPR4150-1#
```

Submit all command output and the files gathered in this step to the relevant TAC SR, and proceed to the next section of this document.

## Step Four - Verify FXOS Digitally Signed Image Authenticity

Cisco FXOS Software implements digitally signed system images on most platforms. Digitally signed Cisco FXOS Software uses asymmetric (public-key) cryptography, which increases the security posture of Cisco Firepower devices by ensuring that the system image has not been altered.

Certain  platforms that are running Cisco FXOS Software, such as Cisco Firepower Series platforms,  also support Cisco Secure Boot technologies. Cisco Secure Boot is a secure  startup process that a Cisco device performs each time it boots. Beginning with  the initial power-on, a special-purpose hardware device, known as the Trust  Anchor module, verifies the integrity of the ROM monitor code and the FXOS  image by using digital signatures as each is loaded. If any failures are  detected, the user is notified of the error, and the device will wait for the  operator to correct the error. This prevents the network device from executing  tainted network software.

For  additional information, see the Cisco Trustworthy Technologies Data Sheet .

Note: The show software authenticity commands  are supported only on Firepower platforms that incorporate Cisco Secure Boot  technologies.

Verify  the authenticity and integrity of a system image file by using the following  commands:

```
connect local-mgmt
show software authenticity running
show software authenticity file path/filename
```

An example of this procedure follows:

```
FPR4150-1# connect local-mgmt FPR4150-1(local-mgmt)# show software authenticity running MANAGER IMAGE
=============
File Name                     : /bootflash/nuova-sim-mgmt-nsg.0.1.0.001.bin
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : FXOS Organization Name     : CiscoSystems Certificate Serial Number : 5D795456 Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier name         : SYSTEM
        Verifier version      : 5.0(3)N2(4.71) [build 5.0(3)N2(4.71.83)]
SYSTEM IMAGE
============
File Name                     : /bootflash/installables/switch/fxos-k9-
system.5.0.3.N2.4.71.83.SPA
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : FXOS Organization Name     : CiscoSystems Certificate Serial Number : 5D795240 Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier name         : KICKSTART
        Verifier version      : 5.0(3)N2(4.71) [build 5.0(3)N2(4.71.83)]
KICKSTART IMAGE
===============
File Name                     : /bootflash/installables/switch/fxos-k9-
kickstart.5.0.3.N2.4.71.83.SPA
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : FXOS Organization Name     : CiscoSystems Certificate Serial Number : 5D794760 Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
        
    Verifier Information
        Verifier name         : ROMMON
        Verifier version      : 1.0.14

FPR4150-1(local-mgmt)# show software authenticity file bootflash:/nuova-sim-
mgmt-nsg.0.1.0.001.bin File Name                  : /bootflash/nuova-sim-mgmt-nsg.0.1.0.001.bin
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : FXOS Organization Name     : CiscoSystems Certificate Serial Number : 5D795456 Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

FPR4150-1(local-mgmt)# show software authenticity file 
bootflash:/installables/switch/fxos-k9-system.5.0.3.N2.4.71.83.SPA File Name                  : /bootflash/installables/switch/fxos-k9-
system.5.0.3.N2.4.71.83.SPA
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : FXOS Organization Name     : CiscoSystems Certificate Serial Number : 5D795240 Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

FPR4150-1(local-mgmt)# show software authenticity file 
bootflash:/installables/switch/fxos-k9-kickstart.5.0.3.N2.4.71.83.SPA File Name                  : /bootflash/installables/switch/fxos-k9-
kickstart.5.0.3.N2.4.71.83.SPA
Image type                    : Release
    Signer Information
        Common Name           : abraxas
        Organization Unit     : FXOS Organization Name     : CiscoSystems Certificate Serial Number : 5D794760 Hash Algorithm            : SHA2 512
    Signature Algorithm       : 2048-bit RSA
	Key Version               : A
```

The Organization Unit, Organization Name, and Certificate Serial Number values are visible  in the preceding output example. Review these values to verify that a system  image signature is valid, and confirm that the same certificate serial number is  returned from both the show software authenticity running and the show software authenticity file command for each file. In the examples above, each  authenticity check of the following images produces a value of 5D795240:

- System running image

- FXOS system image on bootflash

Next, use the following command to calculate a hash for the FXOS Manager, System, and  Kickstart images and verify the digital signatures:

```
verify signature path/filename
```

An example of this procedure follows:

```
FPR4150-1(local-mgmt)# verify signature bootflash:/nuova-sim-mgmt-
nsg.0.1.0.001.bin Verifying file integrity of /bootflash/nuova-sim-mgmt-nsg.0.1.0.001.bin
Computed Hash   SHA2: b0717cbd473ec69cd3d55b3e518d39b45f0ba99247257477a0b93c1ee98a061c7faafe76df82e5
7bff1f1
56b4c008209cf4aa248321d67d60a3fe35f8de4c39f
Embedded Hash   SHA2: b0717cbd473ec69cd3d55b3e518d39b45f0ba99247257477a0b93c1ee98a061c7faafe76df82e5
7bff1f1
56b4c008209cf4aa248321d67d60a3fe35f8de4c39f Digital signature successfully validated. FPR4150-1(local-mgmt)# verify signature bootflash:/installables/switch/fxos-k9-
system.5.0.3.N2.4.71.83.SPA Verifying file integrity of /bootflash/installables/switch/fxos-k9-system.
5.0.3.N2.4.71.83.SPA
Computed Hash   SHA2: 732f37aea8a8102bcbd33d657ea6a0ebea7870eb48ef92b51fbbc6c6c84b47880856dc820e019d
04743b1
f13c6c8e8ed9f531f1e2ea495a474852e925b3eac0d
Embedded Hash   SHA2: 732f37aea8a8102bcbd33d657ea6a0ebea7870eb48ef92b51fbbc6c6c84b47880856dc820e019d
04743b1
f13c6c8e8ed9f531f1e2ea495a474852e925b3eac0d Digital signature successfully validated. FPR4150-1(local-mgmt)# verify signature bootflash:/installables/switch/fxos-k9-
kickstart.5.0.3.N2.4.71.83.SPA Verifying file integrity of /bootflash/installables/switch/fxos-k9-kickstart.
5.0.3.N2.4.71.83.SPA
Computed Hash   SHA2: bd5645b6a70164079d634b91747ce30aa861d6acac844c9a90b2f4b36643c2f25b0f125bf02471
ba44f3c85
a518137c29be055e36604659c01dfb074fcb27af3
Embedded Hash   SHA2: bd5645b6a70164079d634b91747ce30aa861d6acac844c9a90b2f4b36643c2f25b0f125bf02471
ba44f3c85
a518137c29be055e36604659c01dfb074fcb27af3 Digital signature successfully validated.
```

Last, obtain a copy of the public keys by using the following command:

```
show software authenticity keys
```

An example of this procedure follows:

```
FPR4150-1(local-mgmt)# show software authenticity keys Primary Public Keys :
Key 1 :
Key Type              : Release (PRIMARY KEY STORAGE)
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

Backup Public Keys :
Key 1 :
Key Type              : Release (BACKUP KEY STORAGE)
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

Feature Public Keys :
Key 1 :
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

Submit all command output and any system images collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Five - Enumerate Mezzanine Adapter Processes

Execute the following commands at the Cisco FXOS CLI prompt:

```
connect adapter chassis/server/id show-systemstatus
```

An example of this procedure follows:

```
FPR4150-1# connect adapter 1/1/1 adapter 1/1/1 # show-systemstatus fwvers=5.4(1.10)

last pid:   835;  load avg:  0.08,  0.09,  0.06;  up 17+09:47:14       09:42:49
50 processes: 1 running, 49 sleeping
CPU states:  0.0% user,  0.0% nice,  0.0% system,  100% idle,  0.0% iowait
Kernel: 113 ctxsw, 1002 intr
Memory: 43M used, 131M free, 16M cached

  PID USERNAME  THR PRI NICE  SIZE   RES   SHR STATE   TIME    CPU COMMAND
  122 root        1  20    0  475M   14M 2548K sleep  14:10  0.00% mcp
  127 root        1  20    0 5328K  964K  764K sleep   2:06  0.00% /bin/memmon
    3 root        1  20    0    0K    0K    0K sleep   0:07  0.00% ksoftirqd/0
  126 root        1  20    0 1336K  396K  340K sleep   0:00  0.00% /bin/sh /bin/uptimed
  112 root        3  20    0   18M  336K  220K sleep   0:00  0.00% memtun
   54 root        1  20    0 3276K  696K  576K sleep   0:00  0.00% mqlogd
  132 root        1  39   19  325M  768K  608K sleep   0:00  0.00% /bin/nfe
    1 root        1  20    0 1340K  384K  316K sleep   0:00  0.00% init
   56 root        1  20    0 3276K  492K  376K sleep   0:00  0.00% flashlogger
  120 root        1  20    0  176M  592K  472K sleep   0:00  0.00% launcher
   38 root        1  30   10    0K    0K    0K sleep   0:00  0.00% jffs2_gcd_mtd0
  834 root        1  20    0 1484K  508K  408K run     0:00  0.00% top -d 1 -c
  829 root        1  20    0  475M   11M  372K sleep   0:00  0.00% mcp
  124 root        1  20    0  178M 1052K  648K sleep   0:00  0.00% /bin/fls
  121 root        1  20    0  177M  688K  548K sleep   0:00  0.00% /bin/paloerrd
  125 root        1  20    0  177M  688K  552K sleep   0:00  0.00% /bin/ecpumgr
  123 root        1  20    0  176M  676K  544K sleep   0:00  0.00% /bin/ecom
  130 root        1  20    0  176M  656K  532K sleep   0:00  0.00% /bin/bootoptd
  830 root        1  20    0 1332K  336K  284K sleep   0:00  0.00% /bin/sh 
-c getsystemstatus > /tmp/gssOuUC4h
   28 root        1  20    0    0K    0K    0K sleep   0:00  0.00% kworker/0:1
    6 root        1 -99    0    0K    0K    0K sleep   0:00  0.00% watchdog/0
   40 root        1  30   10    0K    0K    0K sleep   0:00  0.00% jffs2_gcd_mtd1
  101 root        1  20    0 1432K  520K  424K sleep   0:00  0.00% xinetd
  831 root        1  20    0 1332K  364K  312K sleep   0:00  0.00% /bin/
sh /bin/getsystemstatus
   58 root        1  20    0 1324K  260K  208K sleep   0:00  0.00% /sbin/klogd
  835 root        1  20    0 1324K  240K  196K sleep   0:00  0.00% uniq
 4031 root        1  20    0 1324K  236K  196K sleep   0:00  0.00% sleep 3600
  116 root        1  20    0  952K  184K  124K sleep   0:00  0.00% l2tun
   29 root        1  20    0    0K    0K    0K sleep   0:00  0.00% kworker/u:1
    4 root        1  20    0    0K    0K    0K sleep   0:00  0.00% kworker/0:0
   22 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock4
   23 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock5
   20 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock2
   25 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock7
   26 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock8
    9 root        1  20    0    0K    0K    0K sleep   0:00  0.00% bdi-default
   11 root        1  20    0    0K    0K    0K sleep   0:00  0.00% kswapd0
    2 root        1  20    0    0K    0K    0K sleep   0:00  0.00% kthreadd
   21 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock3
   18 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock0
   19 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock1
   24 root        1  20    0    0K    0K    0K sleep   0:00  0.00% mtdblock6
  742 root        1  20    0    0K    0K    0K sleep   0:00  0.00% flush-mtd-unmap
    5 root        1  20    0    0K    0K    0K sleep   0:00  0.00% kworker/u:0
    8 root        1  20    0    0K    0K    0K sleep   0:00  0.00% sync_supers
   17 root        1   0  -20    0K    0K    0K sleep   0:00  0.00% iscsi_eh
   12 root        1   0  -20    0K    0K    0K sleep   0:00  0.00% crypto
    7 root        1   0  -20    0K    0K    0K sleep   0:00  0.00% khelper
   27 root        1   0  -20    0K    0K    0K sleep   0:00  0.00% deferwq
   10 root        1   0  -20    0K    0K    0K sleep   0:00  0.00% kblockd

Filesystem                Size      Used Available Use% Mounted on
mtd0                     14.0M      1.5M     12.5M  10% /obfl
mtd1                     14.0M    740.0K     13.3M   5% /config
adapter 1/1/1 # exit FPR4150-1#
```

Submit all command output collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Six - Verify FTD Memory . text Segment Integrity

Execute the following commands at the Cisco FTD CLI prompt:

```
system support diagnostic-cli
enable
```

Then calculate a hash value for the . text memory segment and retrieve a copy of it by executing the following commands:

```
verify /sha-512 system:memory/text
copy system:memory/text ftp
```

An example of this procedure follows:

```
> system support diagnostic-cli Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable Password: 
firepower# verify /sha-512 system:memory/text !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!! [output truncated]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Done! verify /SHA-512 (system:memory/text) = a03a15444f0995f578e9aa6cbc8feed2a3f2dd8ac8cca919b7b2b54836
ba3d4b763372f58029e66fa64aafa8eea2b79d5f0c7ea65cde0d813aef17e436e49b85 firepower# copy system:memory/text ftp Source filename [memory/text]? 
Address or name of remote host []? 10.10.10.1
Destination filename [text]? system.memory.text.bin
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
INFO: No digital signature found
71921664 bytes copied in 2.60 secs (35960832 bytes/sec)
```

To ensure that no errors were introduced during the file transfer process, the following steps are highly recommended:

- Note the hash value for the copied memory  segment file (as described in the preceding example).

- Calculate a hash value for the memory segment  file on the recipient platform.

- Compare the hash values.

The following example utilizes the sha512sum utility, which is included with most Linux distributions:

```
root@ftp-server:~# sha512sum system.memory.text.bin
a03a15444f0995f578e9aa6cbc8feed2a3f2dd8ac8cca919b7b2b54836ba3d4b763372f5802
9e66fa64aafa8eea2b79d5f0c7ea65cde0d813aef17e436e49b85 system.memory.text.bin root@ftp-server:~#
```

Both the FTD verify command and the sha512sum utility produce the  following SHA-512 hash value for the system.memory.text.bin file in the preceding examples:

```
a03a15444f0995f578e9aa6cbc8feed2a3f2dd8ac8cca919b7b2b54836ba3d4b763372f5802
9e66fa64aafa8eea2b79d5f0c7ea65cde0d813aef17e436e49b85
```

Submit all command output (including all computed hash values) and any system images collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Seven - Obtain Firepower Crashinfo File and Core File

Caution: Executing the tasks in this section will trigger a reload of the FXOS platform.

Cisco recommends performing this task during a maintenance window. Cisco does not  recommend performing this task if additional forensic information needs to be collected because a reload of the device may cause the loss of information that is vital to a forensic investigation. Ensure that you have a copy of the  original device configuration and the appropriate authorization to initiate a reload of the platform in question prior to proceeding with this procedure.

This procedure outlines how to obtain a crashinfo file and a core dump from a Cisco FXOS device.

The  storage space required to accommodate the crashinfo file and core dump file may vary from several hundred megabytes to several gigabytes, depending on the  device model. Ensure that there is enough space on the destination flash or  disk device to accommodate both files. The crashinfo file is saved in the root  of the Cisco FXOS file system by default, and the system may place the core  dump in the underlying FTD file system or the coredumpfsys file system. The location depends on the version of software that is running on the system.

To initiate  the crashinfo dump process, execute the following commands:

```
system support diagnostic-cli
enable
crashinfo force page-fault
```

An  example of this procedure follows:

```
> system support diagnostic-cli Attaching to Diagnostic CLI ... Press 'Ctrl+a then d' to detach.
Type help or '?' for a list of available commands.
firepower> enable Password: 
firepower# crashinfo force page-fault WARNING: This command will force a crash and cause a
         reboot. Do you wish to proceed? [confirm]: 

Register dump: Thread DATAPATH-0-17007 in thread group
other: Unknown
        r8 0x000000000000100c
        r9 0x0000000000000002
       r10 0x00002acb49389340
       r11 0x0000000000000001
       r12 0x0000000000000000
       r13 0x0000000000000000
       r14 0xffffffffffffdf40
       r15 0x00002acb4939b740
       rdi 0x00002acb48564570
       rsi 0x0000000000000001
       rbp 0x00002ac95e7fd6f0
       rbx 0x00002acb483ce080
       rdx 0x0000000000000001
       rax 0x00002ac95e801000
       rcx 0x00002acb4979ae14
       rsp 0x00002ac95e7fd610
       rip 0x000055d4ad284073
    eflags 0x0000000000003246
    csgsfs 0x0000000000000033
error code n/a
    vector 0x0000000000000000
  old mask 0xffffffde3e3bd805
       cr2 0x0000000000000000
[output truncated]

Begin to dump crashinfo to flash....

End of console dump.
Do 'show crashinfo' after reboot to retrieve other crash information
Process shutdown finished
REBOOT: ASA not terminated, enforce reboot...
Rebooting... (status 0x8b)
```

Caution: When the crashinfo process is complete, the Firepower  platform will reboot.

After the platform has rebooted, perform the following  steps:

- Connect to the FTD CLI.

- Enter expert mode and assume root privileges.

- Locate the crashinfo and core files.

- Calculate hash values for both files.

- Copy both files to a secure location.

Use the following commands for the preceding steps:

```
sudo su -
sha512sum filename scp filename user@host:remote_path/filename
```

An example of this procedure follows:

```
> expert admin@firepower:~$ sudo su - Password: 

#
# Crashinfo files are typically located in /mnt/disk0 but the location
# could vary dependent on hardware platform or software release. The Linux
# “find” command can be used to locate all crashinfo files on the 
# filesystem: find / -name "crashinfo*"
#

root@firepower:~# cd /mnt/disk0 root@firepower:disk0# ls -l total 3360
-rwxr-xr-x 1 root root 530074 Aug 27 09:23 aclout.txt
-rwxr-xr-x 1 root root 531174 Aug 27 09:27 aclout2.txt
-rwxr-xr-x 1 root root 531174 Aug 27 09:38 aclout3.txt
-rw-r--r-- 1 root root   1461 Sep 10 13:32 asa-cmd-server.log
-rw-r--r-- 1 root root      5 Aug 27 15:37 asa_vnic_assigned
d--------- 2 root root     23 Aug 26 11:02 boot
lrwxrwxrwx 1 root root     15 Aug 26 11:01 coredumpfsys -> /var/data/cores
-rw-r--r-- 1 root root      0 Aug 26 11:01 coredumpfsysimage.bin
drw------- 2 root root     26 Aug 26 11:01 coredumpinfo
-rwxr-xr-x 1 root root 969632 Sep 10 13:25 crashinfo_20240910_132529_UTC drw------- 2 root root      6 Aug 26 11:01 crypto_archive
d--------- 4 root root     30 Aug 26 11:01 csco_config
-rw-r--r-- 1 root root 852703 Sep 10 13:11 debug_output.2024.09.10-13.11.07
-rw-r--r-- 1 root root      0 Aug 27 15:46 hitcnt_del_ruleid_list
drwxr-xr-x 3 root root   4096 Sep 10 13:40 log
drwxr-xr-x 2 root root      6 Aug 26 11:01 packet-tracer
-rw-r--r-- 1 root root     41 Sep 10 13:33 snortpacketinfo.conf

root@firepower:disk0# sha512sum crashinfo_20240910_132529_UTC 2430950c5597b54e7fbdbc404fdc2f107e434750176a682ebc25dcd29035d0d6b187ceda07a998b
7124e5dd021f7227f1c7c6a047aa4dc206ff322935d2af0d9 crashinfo_20240910_132529_UTC

root@firepower:disk0# scp /mnt/disk0/crashinfo_20240910_132529_UTC
labuser@10.10.10.1:/labuser/. labuser@10.10.10.1's password: 
crashinfo_20240910_132529_UTC        100%  958KB  47.4MB/s   00:00   

#
# This procedure is then repeated for the core file which is typically found
# in /mnt/disk0/coredumpfsys, but may be in /ngfw/var/common in older
# versions of the software. 
#
root@firepower:common# cd /mnt/disk0/coredumpfsys root@firepower:coredumpfsys# ls -l total 678628
-rw-r--r-- 1 root root 694212690 Sep 10 13:25 core.lina.11.15294.1725974707.gz
drwx------ 2 root root     16384 Aug 23 11:48 lost+found

root@firepower:coredumpfsys# sha512sum core.lina.11.15294.1725974707.gz de4134c1841b42668a19d20d7b09d72339a975425e28919c5cdf2d5f7ae99143ea7d3d6055eb0ee
aebc2f133eed79d5c62e5e1d1faa2a2a2f99fb7b2091be6af  core.lina.11.15294.1725974707.gz

root@firepower:coredumpfsys# scp 
/mnt/disk0/coredumpfsys/core.lina.11.15294.1725974707.gz 
labuser@10.10.10.1:/labuser/. labuser@10.10.10.1's password: 
core_file.tar.gz                     100%   694MB 125.5MB/s   00:00    
root@firepower:common# exit logout
admin@firepower:~$ exit logout
>
```

Submit  all command output, hash values, and the crashinfo and core files collected in  this section to the relevant TAC SR, and proceed to the next section of this  document.

## Step Eight – Check Firepower ROM Monitor Settings

The ROM monitor firmware of the Firepower platform is executed when the appliance is powered on or reset. The firmware initializes the platform hardware and boots the FXOS operating system software.

Because the ROM monitor settings persist if they have been synced to NVRAM, the values of the ROM monitor variables could indicate that there has been an attempt to influence the FXOS boot sequence. Use the set command at the ROM monitor prompt to see the value of the ROM monitor variables.

Access ROM monitor mode by rebooting the Firepower appliance and pressing the BREAK or ESC key during the reload process when prompted, as shown in the following example:

```
FPR4150-1# connect local-mgmt FPR4150-1(local-mgmt)# reboot Warning: This command causes an ungraceful reboot and causes 
service interruption and potential loss of configuration in database!
Before rebooting, please make a configuration backup.
Alternatively, perform a graceful reboot in scope chassis.
Do you still want to reboot? (yes/no): yes nohup: ignoring input and appending output to 'nohup.out'

Broadcast message from root@firepower (Mon Aug  3 20:05:02 2020):

All shells being terminated due to system /sbin/reboot
[590328.959462]  writing reset reason 9, 

Cisco FPR Series Security Appliance
INIT: Sending processes the TERM signal
Aug  3 14:35:13 %TTYD-2-TTYD_ERROR TTYD Error ttyd bad select

Sending all processes the TERM signal...
ipsec_starter[8993]: charon stopped after 200 ms

ipsec_starter[8993]: ipsec starter stopped

Sending all processes the KILL signal...
Copying /bootflash/logs/plog to /mnt/plog
Unmounting filesystems...
/bootflash/sysdebug/tftpd_logs: successfully unmounted
/spare                   : successfully unmounted
/cgroup                  : successfully unmounted
/workspace               : successfully unmounted
/opt/db/nvram            : successfully unmounted
/opt                     : successfully unmounted
/bootflash               : successfully unmounted
/mnt/pss                 : successfully unmounted
/dev/pts                 : ignored
/var/sysmgr/startup-cfg  : successfully unmounted
/mnt/cfg/1               : successfully unmounted
/mnt/cfg/0               : successfully unmounted
/mnt/plog                : successfully unmounted
/debugfs                 : successfully unmounted
/dev/mqueue              : successfully unmounted
/debug                   : successfully unmounted
/volatile                : successfully unmounted
/dev/shm                 : successfully unmounted
/callhome                : successfully unmounted
/var/sysmgr/ftp          : successfully unmounted
/var/sysmgr              : successfully unmounted
/var/tmp                 : successfully unmounted
/isan                    : successfully unmounted
/sys                     : ignored
/proc                    : ignored
[590348.764371] Disconnected SATA Storage device(sda) from PCI bus
[590424.958240] reboot: Restarting system

!!  Rommon image verified successfully  !!
Cisco System ROMMON, Version 1.0.15, RELEASE SOFTWARE
Copyright (c) 1994-2019  by Cisco Systems, Inc.
Compiled Wed 04/10/2019 15:48:43.00 by builder
Current image running: Boot ROM0
Last reset cause: ResetRequest
DIMM Slot 0 : Present
DIMM Slot 1 : Present
No USB drive !! 
BIOS has been locked !!

Platform FPR-4150-SUP with 8192 Mbytes of main memory
MAC Address: 38:90:a5:f1:aa:10

find the string ! boot bootflash:/installables/switch/fxos-k9-kickstart.5.0.3.N2.4.61.155.SPA
bootflash:/installables/switch/fxos-k9-system.5.0.3.N2.4.61.155.SPA Use BREAK, ESC or CTRL+L to interrupt boot. Use SPACE to begin boot immediately. Boot interrupted. rommon 1 >
```

The following example shows the output of the ROM monitor set command on a Cisco Firepower platform:

```
rommon 1 > set ADDRESS=
    NETMASK=
    GATEWAY=
    SERVER=
    IMAGE=
    CONFIG=
    PS1="rommon ! > "
```

The preceding example depicts a platform on which the ROM monitor values are at their default values and have not been altered.

To return the Firepower platform to normal operation, use the boot command at the ROM monitor prompt as shown in the following example:

```
rommon 2 > boot Try autoboot...
find the string ! boot bootflash:/installables/switch/fxos-k9-kickstart.5.0.3.N2.4.61.155.SPA
bootflash:/installables/switch/fxos-k9-system.5.0.3.N2.4.61.155.SPA 
!!   Kickstart Image verified successfully   !!
Linux version: 3.14.39ltsi (security@cisco.com) #1 SMP Tue Apr 9 20:36:27 PDT 2019
[4.197347] physmap-flash physmap-flash.0: Could not reserve memory region
linuxrc.ext Mon Aug  3 14:37:42 UTC 2020
1+0 records in
1+0 records out
64 bytes (64 B) copied, 0.103605 s, 0.6 kB/s
Usage: init {-e VAR[=VAL] | [-t SECONDS] {0|1|2|3|4|5|6|S|s|Q|q|A|a|B|b|C|c|U|u}}
INIT: version 2.88 booting
```

Submit all command output obtained in this section to the relevant TAC SR.

## Acknowledgments

The authors would like to thank all members of the Customer Experience Security Programs (CXSP) and Advanced Security Initiatives Group (ASIG) who provided their expertise for this document.

## Related Documentation

Additional information about Cisco Software Integrity Assurance, as well as forensic investigation procedures for other platforms, is available in Cisco Security Tactical Resources: https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## Firepower 4100 and 9300 Series Appliances Forensic Response Checklist

Step One - Create Firepower Device Problem Description

Device problem description uploaded to SR

Step Two - Document Firepower Runtime Environment

Output of show tech-support detail uploaded to SR

Output of dir all-filesystems uploaded to SR

Step Three - Verify Integrity of FTD System Files

Output of find /ngfw/var/sf/.icdb/* and hashes uploaded to SR

Output of the which command that was executed on shell scripts uploaded to SR

Shell scripts, certificates, log file, and hash database added to .tar file

.tar file and its associated hash value uploaded to SR

Step Four - Verify FXOS Digitally Signed Image Authenticity

Output of show software authenticity running uploaded to SR

Output of show software authenticity file uploaded to SR

Output of verify signature path/filename uploaded to SR

Output of show software authenticity keys uploaded to SR

Step Five - Enumerate Mezzanine Adapter Processes

Output of show-systemstatus uploaded to SR

Step Six - Verify FTD Memory . text Segment Integrity

Output of verify on memory text segment uploaded to SR

Copy of memory text segment uploaded to SR

Step Seven - Obtain Firepower Crashinfo File and Core File

Output of crashinfo uploaded to SR

Crashinfo file uploaded to SR

Core file uploaded to SR

Hash values of crashinfo and core files uploaded to SR

Step Eight - Check Firepower ROM Monitor Settings

Output of set command uploaded to SR

## Appendix A - Firepower 4100/9300 Series Platforms Running ASA Software Modules

Note: Only execute the commands in Appendix A if Cisco ASA Software is running as a module on a Cisco Firepower 4100/9300 Series appliance.

Execute the following commands from the Cisco ASA CLI prompt:

enable show tech-support detail dir /recursive all-filesystems verify /sha-512 system:/text copy system:/text ftp:

The output of show tech-support detail may also be redirected to a file server using either the FTP, SCP, SMB, or TFTP protocol. The following example depicts the required syntax if the FTP protocol is used:

```
show tech-support detail | redirect ftp://anonymous@10.10.10.1/tech-support-details.txt
```

An example of this entire procedure follows:

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
verify /SHA-512 (system:/text) = efc7164423606abce9a67ca5d4202ffd2c14342c4639596acee526d37c2b4a7d2aa
4061629534557c122dbfb528935fdd79fabd9e855c8d6d58e936f6563f8c2

ciscoasa# copy system:/text ftp:                            
Source filename [text]? 
Address or name of remote host []? 10.10.10.1
Destination filename [text]? system.memory.text.bin
73990144 bytes copied in 2.850 secs (36995072 bytes/sec)
ciscoasa#
```

Cisco highly recommends calculating a hash value on the copied memory segment file and comparing it to the hash value that was obtained on the recipient platform to ensure no errors were introduced during the file transfer process.

The following example utilizes the sha512sum utility, which is included with most Linux distributions:

root@ftp-server:~# sha512sum system.memory.text.bin efc7164423606abce9a67ca5d4202ffd2c14342c4639596acee526d37c2b4a7d2aa406162953 4557c122dbfb528935fdd79fabd9e855c8d6d58e936f6563f8c2 system.memory.text.bin root@ftp-server:~#

Note that the Cisco ASA verify command and the sha512sum utility both produce a SHA-512 hash value of efc7164423606abce9a67ca5d4202ffd2c14342c4639596acee526d37c2b4a7d2aa4061629534557 c122dbfb528935fdd79fabd9e855c8d6d58e936f6563f8c2 for the system.memory.text.bin file.

Submit all command output (including all computed hash values) and a copy of the system:/text memory segment that was collected in this section to the relevant TAC SR.

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Step One - Create Firepower Device Problem Description |  |
|---|---|
| Device problem description uploaded to SR |  |
| Step Two - Document Firepower Runtime Environment |  |
| Output of show tech-support detail uploaded to SR |  |
| Output of dir all-filesystems uploaded to SR |  |
| Step Three - Verify Integrity of FTD System Files |  |
| Output of find /ngfw/var/sf/.icdb/* and hashes uploaded to SR |  |
| Output of the which command that was executed on shell scripts uploaded to SR |  |
| Shell scripts, certificates, log file, and hash database added to .tar file |  |
| .tar file and its associated hash value uploaded to SR |  |
| Step Four - Verify FXOS Digitally Signed Image Authenticity |  |
| Output of show software authenticity running uploaded to SR |  |
| Output of show software authenticity file uploaded to SR |  |
| Output of verify signature path/filename uploaded to SR |  |
| Output of show software authenticity keys uploaded to SR |  |
| Step Five - Enumerate Mezzanine Adapter Processes |  |
| Output of show-systemstatus uploaded to SR |  |
| Step Six - Verify FTD Memory . text Segment Integrity |  |
| Output of verify on memory text segment uploaded to SR |  |
| Copy of memory text segment uploaded to SR |  |
| Step Seven - Obtain Firepower Crashinfo File and Core File |  |
| Output of crashinfo uploaded to SR |  |
| Crashinfo file uploaded to SR |  |
| Core file uploaded to SR |  |
| Hash values of crashinfo and core files uploaded to SR |  |
| Step Eight - Check Firepower ROM Monitor Settings |  |
| Output of set command uploaded to SR |  |

| Version | Date | Authors | Comments |
|---|---|---|---|
| 1.0 | 2021-04-19 | Dan Maunz and Jason Barnes | Initial public release. |
| 1.1 | 2022-08-26 | Dan Maunz | Validated procedures on FXOS Release 2.11 and FTD Release 7.0.1 |
| 1.2 | 2024-09-12 | Dan Maunz | Validated procedures on FXOS Release 2.13 and FTD Release 7.3.1 |
| 1.3 | 2026-07-01 | Dan Maunz | Validated procedures on FXOS Release 2.16.2 and FTD Release 7.6.4 |