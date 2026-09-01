---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-fmc-forensic-investigation-html-2700c5d246
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/fmc_forensic_investigation.html
retrieved_at: 2026-09-01T14:10:11.942381+00:00
---

Home / Cisco Security

Assessing the Integrity of Cisco Firepower Management Center Software

# Assessing the Integrity of Cisco Firepower Management Center Software

Introduction

Prerequisites

Verifying the Integrity of System Files

Related Documentation

Revision History

## Introduction

This document provides steps to assess the software integrity of a Cisco Firepower Management Center appliance when compromise or tampering is suspected. It outlines a number of commands that can be run to assess important operating system files along with the respective output that should be collected upon running these commands.

Note: DO NOT REBOOT THE DEVICE. Rebooting or turning off the power to a device during the initial stage of an integrity assessment will result in the permanent loss of all volatile information that is contained within the device.

Note: It is highly recommended that a device that is suspected of being tampered with or compromised be isolated from the network prior to the initial examination, if possible. This may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device under investigation.

For further assistance or for more information about this procedure, contact the Cisco Product Security Incident Response Team (PSIRT) .

## Prerequisites

The procedures outlined in this document require the reader to have a basic understanding of Cisco Firepower Management Center operations and Linux command syntax.

Use the Cisco Software Checker to search for Cisco Security Advisories that apply to specific software releases of the following products: Cisco ASA, FMC, FTD, FXOS, IOS, IOS XE, NX-OS, and NX-OS in ACI Mode.

Record any results returned by the tool that may explain any anomalous behavior being observed. It is considered a best practice to keep software up to date to take advantage of the latest security fixes and enhancements.

Note: This tool does not provide information about Cisco IOS XR Software or interim software builds. Also note that for Cisco ASA, FMC, FTD, and FXOS Software, the tool contains only vulnerability information for Cisco Security Advisories that were first published from January 2022 onward, and for NX-OS Software and NX-OS Software in ACI Mode from July 2019 onward.

Note: The examples that are used in this document are based on Firepower Management Center Software Release 7.4.2. Command syntax and the output that is produced by a command may vary depending on the software release that is deployed.

## Verifying the Integrity of System Files

Connect to the FMC CLI and enter expert mode:

```
expert
```

From expert mode, issue the following commands to assume root permissions and run the system file integrity checks:

```
sudo su -
verify_file_integ.sh -f
```

An example of this procedure follows:

```
> expert
admin@firepower:~$ sudo su -
Password:
root@firepower:~# verify_file_integ.sh -f
Running file integrity checks...
Successfully verified file integrity
```

Note: Firepower Management Center Software releases prior to 7.4.0 may require setting the FIPS_MODE environment variable to run the verify_file_integ.sh script. Set the FIPS_MODE environment variable to true if running the script with the -f parameter returns the error illegal option – f .

In this case, issue the following commands to assume root permissions, set the appropriate environment variable, and run the system file integrity checks:

```
sudo su -
export FIPS_MODE=1
verify_file_integ.sh
unset FIPS_MODE
```

An example of this procedure for previous releases follows:

```
> expert
admin@firepower:~$ sudo su -
Password: 
root@firepower:~# export FIPS_MODE=1

# Check to see if the environment variable is set correctly
root@firepower:~# set | grep FIPS_MODE
FIPS_MODE=1
_=FIPS_MODE

root@firepower:~# verify_file_integ.sh
Running file integrity checks...
Successfully verified file integrity

# Once the file integrity verification script has completed, unset the        
# FIPS_MODE environment variable:
root@firepower:~# unset FIPS_MODE
```

Note: If any file checked by the file integrity process has been modified, the following error will be returned:

```
verify_file_integ.sh: Error: Failed to verify file integrity against the signed database
```

If the file integrity script successfully completes but it is suspected that the platform has been tampered with or the integrity script returns an error, execute the following steps:

Connect to the FMC CLI, enter expert mode, and assume root privileges:

```
expert
sudo su -
```

Execute the following commands and record the output that is produced:

```
find /var/sf/.icdb/* -name *.icdb.RELEASE.tar | xargs sha512sum
cat /proc/*/smaps > /tmp/all-process-smaps.txt
which verify_file_integ.sh
which verify_signed_db.sh
which db_manage.sh
```

This output will be used to create an archive file, which may be useful in further assessing the integrity of the platform. The following files should also be added to the archive:

```
/etc/certs/*.crt
/var/log/sf/verify_file_integ.log
/var/tmp/merged-db/master.db
```

Create an archive of the files listed above, generate a hash value for the archive, and copy the archive off the platform:

```
tar -czvf SR-<sr_number>.tar.gz
sha512sum SR-<sr_number>.tar.gz
sftp or scp
```

An example of this procedure follows:

```
> expert
admin@firepower:~$ sudo su -
Password: 
root@firepower:~# find /var/sf/.icdb/* -name *.icdb.RELEASE.tar | xargs sha512sum
9e073b4c98681aca3bcc147d538c3e528327ad2c8b8cc284c272b2325c926f52059b76c6d35ac67fb2a914906aec85181ffc47
ef00304410184f8a33f829df97  /var/sf/.icdb/0000/base-lilo-7.0.1-84.icdb.RELEASE.tar
65a9f5a841ecaae9e27c6ef2d224e1cbc3624feb3af37fa3a764b2700174ba682a0557cf94000d1d2e88736ca9d32fb702fe5a
d22fb11175dad38446375857af  /var/sf/.icdb/0000/base-ciscossl-7.0.1-84.icdb.RELEASE.tar
d5fa7dcd544caa7cf98fef09068733eb5930de6102c0aa32865b2809888412b83ddce6534e0db977fb6a4d78b7434ee0de825f
329730d77007c0fb05d8e4df05  /var/sf/.icdb/0000/base-7.0.1-84.icdb.RELEASE.tar

#
# Note: the file names, number of files, and hash values may vary dependent on 
# the version of software running on the appliance and whether any software   
# updates have been applied. It is extremely important that the output        
# (including file names and hashes) generated by the command above be         
# recorded and saved if further analysis is warranted.
#

root@firepower:~# cat /proc/*/smaps > /tmp/all-process-smaps.txt

# Identify the location of the system integrity scripts with the “which”      
# command:
root@firepower:~# which verify_file_integ.sh
/usr/local/sf/bin/verify_file_integ.sh
root@firepower:~# which verify_signed_db.sh
/usr/local/sf/bin/verify_signed_db.sh
root@firepower:~# which db_manage.sh
/usr/local/sf/bin/db_manage.sh

# Archive a copy of these scripts, along with all certificates found in       
# /etc/certs/, and the files /var/log/sf/verify_file_integ.log and
# /var/tmp/merged-db/master.db

root@firepower:~# tar -czvf SR-1234567890.tar.gz /usr/local/sf/bin/verify_file_integ.sh /usr/local/sf/
bin/verify_signed_db.sh /usr/local/sf/bin/db_manage.sh /etc/certs/*.crt /var/log/sf/
verify_file_integ.log /var/tmp/merged-db/master.db /tmp/all-process-smaps.txt
tar: Removing leading `/' from member names
/usr/local/sf/bin/verify_file_integ.sh
tar: Removing leading `/' from hard link targets
/usr/local/sf/bin/verify_signed_db.sh
/usr/local/sf/bin/db_manage.sh
/etc/certs/SRU_rel.crt
/etc/certs/rel.crt
/var/log/sf/verify_file_integ.log
/var/tmp/merged-db/master.db
/tmp/all-process-smaps.txt

# Create a hash of the tar file:
root@firepower:~# sha512sum SR-1234567890.tar.gz
48b85382e6e1b0ee0f145fa572019b1b297f4e320f4cd29b2af4b727aad092c7ca6bc70f716f7b71d2183e36d18a4b53c6309b
99d3f5c9708af50f4c963a4061  SR-1234567890.tar.gz
root@firepower:~#

# Copy the tar file off the platform using SFTP or SCP:
root@firepower:~# scp SR-1234567890.tar.gz labuser@10.10.10.1:/labuser/.
labuser@10.10.10.1's password: 
SR-1234567890.tar.gz                  100% 2692KB 104.1MB/s   00:01    
root@firepower:~# exit
logout
admin@firepower:~$ exit
logout
>
```

If further assistance is required to analyze the files collected in this procedure, contact the Cisco Technical Assistance Center (TAC) and open a service request.

## Related Documentation

Additional information about Cisco Software Integrity Assurance, as well as forensic data collection procedures for other platforms, can be found at the following link:

Cisco Security Tactical Resources

https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
| 1.0 | 02/01/2021 | D. Maunz | Initial public release. |
| 1.1 | 03/21/2022 | D. Maunz | Validated procedures on Release 7.0.1. |
| 1.2 | 03/17/2023 | D. Maunz | Validated procedures on Release 7.3.0. |
| 1.3 | 03/04/2024 | D. Maunz | Validated procedures on Release 7.4.1. |
| 1.4 | 02/28/2025 | D. Maunz | Validated procedures on Release 7.4.2. |
| 1.5 | 03/02/2026 | D. Maunz | Validated procedures on Release 7.6.5. |