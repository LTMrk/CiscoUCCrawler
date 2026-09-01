---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-staros-forensic-investigation-html-7f5aa07428
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/staros_forensic_investigation.html
retrieved_at: 2026-09-01T14:11:02.452186+00:00
---

Home / Cisco Security

Cisco StarOS Software Forensic Data Collection Procedures

# Cisco StarOS Software Forensic Data Collection Procedures

Introduction

Prerequisites

Step One – Create the StarOS Device Problem Description

Step Two – Collect a StarOS show support details File

Step Three – Obtain StarOS System Image Hash Value

Step Four – Gather Critical Process Core Files

Step Five – Collect Nonvolatile System Information and Artifacts

Step Six – Enumerate Line Card Processes

Related Documentation

Cisco StarOS Platform Forensic Response Checklist

Revision History

## Introduction

This document provides steps to collect forensic information from appliances that are running Cisco StarOS Software when compromise or tampering is suspected. It outlines commands that can be run to gather evidence for an investigation along with the respective output that should be collected after running these commands. This document also provides information about how to perform integrity checks on a StarOS system, and it includes procedures for collecting core files from critical system processes.

Caution: DO NOT REBOOT THE DEVICE. Rebooting a device during the initial stage of an assessment will irrecoverably lose all volatile information that the device contains, such as RAM contents, ARP and routing tables, NAT translations, and ACL hit and drop counts.

Caution: It is highly recommended that a device suspected of tampering or compromise be isolated from the network before conducting an initial forensic examination. This action may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device that is under investigation.

If you require assistance or have questions regarding the following procedures, contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains six main sections:

1.     Create the StarOS Device Problem Description – Describes why the platform is a candidate for forensic examination

2.     Collect a StarOS show support details File – Collects platform configuration and runtime state

3.     Obtain StarOS System Image Hash Value – Calculates an MD5 hash value for the system image file

4.     Gather Critical Process Core Files – Obtains core files for critical system processes

5.     Collect Nonvolatile System Information and Artifacts – Retrieves a list of processes and their associated memory maps, installed modules, IP tables, and startup scripts

6.     Enumerate Line Card Processes – Obtains a list of running processes from line cards installed in the chassis

## Prerequisites

The procedures outlined in this document assume the reader has a basic understanding of Cisco StarOS Software and Linux command syntax.

A valid cisco.com account is required to view individual Cisco StarOS Software file hashes for software file integrity checking. For customers without a cisco.com account, a publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded from: https://www.cisco.com/c/en/us/about/trust-center/downloads.html

A Cisco Technical Assistance Center (TAC) service request (SR) is required for the device in question as the procedures outlined in this document assume that the information gathered in each step will be uploaded to a TAC SR.

Note: The examples that are used in this document are based on Cisco StarOS Software Release  2026.01.gh3/h1 (image version 21.28.mh37) command syntax. The output that is produced by a command may vary depending on the software release that is deployed and/or the features that are supported or configured on the device. Not all commands that are used in these procedures may be supported on earlier releases of the software.

## Step One – Create the StarOS Device Problem Description

Describe in as much detail as possible WHY the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior that cannot be attributed to a misconfiguration or a software or hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Submit the problem description collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Two – Collect a StarOS show support details File

The initial stage of forensic information gathering is completed by using the show support details command, and the output of this command may be redirected to a secure location from the CLI. Adjust the file system path, username, and destination as appropriate for your environment.

Execute the following commands at the CLI and record the output:

```
context local
show support details to file <file_system_path/file_name>
```

An example of this procedure follows:

```
[local]qvpc-si# context local
[local]qvpc-si# show support details to file ftp://anonymous:anonymous@172.16.0.50/pub/support_details   
Are you sure? [Yes|No]: y
Warning: Changed output URL to file: ftp://anonymous:anonymous@172.16.0.50/pub/support_details.tar
******************************************************************************
Transferred 2682368 bytes in 0.022 seconds (119068.2 KB/sec)
```

Note: The show support details command supports  the TFTP, FTP, and SFTP protocols.

Note: Recipient file servers may need to be configured to allow file overwrites to transfer the support details file successfully or you may see errors such as the following: +ERR 2 File unavailable (e.g., file not found, no access) .

Submit all command output collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Three – Obtain StarOS System Image Hash Value

Note: The following procedure requires enabling the debug shell feature, and these commands must be issued by a user with administrator privileges.

Use the following commands at the Cisco StarOS CLI prompt to enable the debug shell:

```
configure
cli hidden
tech-support test-commands password <password>
cli test-commands password <password>
end
```

Obtain an MD5 hash value of the system image file by using the following commands:

```
show boot
cli test-commands
debug shell
md5sum <file_system_path /filename>
```

An example of this procedure follows:

```
[local]qvpc-si# show boot

boot system priority 10 \
    image /flash/staros.bin \
    config /flash/system.cfg

[local]qvpc-si# cli test-commands
Password:
Warning: Test commands enables internal testing and debugging commands
         USE OF THIS MODE MAY CAUSE SIGNIFICANT SERVICE INTERRUPTION

[local]qvpc-si# debug shell
Last login: Wed Apr 16 08:41:31 -0500 2025 on pts/3 from 192.168.1.2.

qvpc-si:ssi# md5sum /flash/staros.bin
713515126efe959515d8b7607e8dd88c  /flash/staros.bin
```

Submit all command output and any hash values calculated in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Four – Gather Critical Process Core Files

Note: The following procedure requires the debug shell feature to be enabled and a crash enable URL to be defined. Use the following commands at the Cisco StarOS CLI prompt to enable the debug shell if it was not enabled in the preceding step, and define a destination for the core files:

```
configure
cli hidden
tech-support test-commands password <password>
cli test-commands password <password>
crash enable url <destination_parameters>
```

Note: The crash enable url configuration command supports the TFTP, FTP, and SFTP protocols.

Note: The procedures in the examples that follow were executed on a minimally configured platform and are for illustration of the concepts only. Platforms in a production environment are more likely to have all the processes running and multiple instantiations of each process.

Enter the debug shell environment and ensure that root privileges have been obtained:

```
[local]qvpc-si# cli test-commands
Password:
Warning: Test commands enables internal testing and debugging commands
         USE OF THIS MODE MAY CAUSE SIGNIFICANT SERVICE INTERRUPTION

[local]qvpc-si# debug shell
Last login: Wed Apr 16 08:52:20 -0500 2025 on pts/3 from 192.168.1.2.

qvpc-si:ssi# id
uid=0(root) gid=0(root) groups=0(root)
```

In the next step, cut and paste the following script into the current debug shell session. The script will automate finding the process IDs for all critical processes and set the core dump filters appropriately.

```
processes=("vpnctrl" "vpnmgr" "sessctrl" "sessmgr" "aaamgr" "diamproxy" "gtpcmgr" "imsimgr" "sgtpmgr" "egtpinmgr" "gtpumgr" "npumgr" "cli")

for proc in "${processes[@]}"; do
    for pid in $(pidof $proc); do
        echo "Found pid $pid for process $proc"
        echo 0x7f > /proc/$pid/coredump_filter
        echo "Coredump_filter for $pid to $(cat /proc/$pid/coredump_filter)"
    done
done
```

An example of this procedure follows:

```
qvpc-si:ssi# processes=("vpnctrl" "vpnmgr" "sessctrl" "sessmgr" "aaamgr" "diamproxy" "gtpcmgr" "imsimgr" "sgtpmgr" "egtpinmgr" "gtpumgr" "npumgr" "cli")
qvpc-si:ssi# 
qvpc-si:ssi# for proc in "${processes[@]}"; do
>     for pid in $(pidof $proc); do
>         echo "Found pid $pid for process $proc"
>         echo 0x7f > /proc/$pid/coredump_filter
>         echo "Coredump_filter for $pid to $(cat /proc/$pid/coredump_filter)"
>     done
> done 
Found pid 6181 for process vpnctrl
Coredump_filter for 6181 to 0000007f
Found pid 11484 for process vpnmgr
Coredump_filter for 11484 to 0000007f
Found pid 6196 for process vpnmgr
Coredump_filter for 6196 to 0000007f
Found pid 6193 for process sessctrl
Coredump_filter for 6193 to 0000007f
Found pid 6200 for process aaamgr
Coredump_filter for 6200 to 0000007f
Found pid 6156 for process npumgr
Coredump_filter for 6156 to 0000007f
Found pid 21755 for process cli
Coredump_filter for 21755 to 0000007f
Found pid 14821 for process cli
Coredump_filter for 14821 to 0000007f
Found pid 6301 for process cli
Coredump_filter for 6301 to 0000007f
Found pid 6270 for process cli
Coredump_filter for 6270 to 0000007f
```

Next, exit from the debug shell, enable CLI test commands, and use the task core command to generate a core file from each active process identified above.

An example of this procedure follows:

```
qvpc-si:ssi# exit
logout
Connection to localhost closed.
[local]qvpc-si# cli test-commands 
Password:
Warning: Test commands enables internal testing and debugging commands
         USE OF THIS MODE MAY CAUSE SIGNIFICANT SERVICE INTERRUPTION
[local]qvpc-si# task core facility vpnctrl all
[local]qvpc-si# task core facility vpnmgr all
[local]qvpc-si# task core facility sessctrl all
[local]qvpc-si# task core facility aaamgr all
[local]qvpc-si# task core facility npumgr all
[local]qvpc-si# task core facility cli all
```

Note: Obtaining a core dump of the CLI processes will generate a stack trace on all active remote sessions and the console. Simply hit the Enter key to resume the session.

When the core files have completed transfer to the file server specified with the crash enable url command, it is highly recommended that a hash value be calculated for each file prior to uploading them to the SR.

An example of this procedure on a Linux server follows:

```
[admin@centos pub]# ls -la
total 533808
drwxrwxrwx   2 root   root         240 Feb  2 11:27 .
drwxr-xr-x. 35 root   root        4096 Aug  5 17:36 ..
-rw-r--r--   1 nobody nobody 106942594 Feb  2 10:28 crash-01-00-07661-61faa279-core
-rw-r--r--   1 nobody nobody 108202484 Feb  2 10:31 crash-01-00-10737-61faa31a-core
-rw-r--r--   1 nobody nobody 107580767 Feb  2 10:32 crash-01-00-12289-61faa36a-core
-rw-r--r--   1 nobody nobody 107534975 Feb  2 10:33 crash-01-00-13635-61faa3b1-core
-rw-r--r--   1 nobody nobody 108455732 Feb  2 10:34 crash-01-00-14646-61faa3e6-core
-rw-r--r--   1 nobody nobody   7886257 Feb  2 10:35 crash-01-00-16099-61faa42e-core

[admin@centos pub]# ls | xargs sha512sum
fbaa2215fc76d82faa1a3d391b3152745b4e3a6b018120f07f421f29184fc05c2bb45d9616147c2cdc9cc10eceb06c3fdb01af04c51e11d2ed9bd1721e71f853  crash-01-00-07661-61faa279-core
872cfb1e2fae57498c701fc43e013956f417e3db45ec54de25c08a17175478b377343b5a68773ae8f466d43e8c74eff125bf0929d95175d9e3f52700f47f27ea  crash-01-00-10737-61faa31a-core
d4b3143c958eef0db7bd2dc01cb9fffcad0443ad0a349113b904ce9da20122e5b7312f92cc31059c771f390125f433d153bbabe146cd2bcd3cdc39530b75ffcc  crash-01-00-12289-61faa36a-core
ed3f1fa01d66045cf3b973cefac79c9f592c82c0a54e830ab64b284f1326b55f880a1a4edf5b431261707e9b71866c99d56441509117d79ad9103c923d08bedc  crash-01-00-13635-61faa3b1-core
946aa8c6ed89a027014e32fc5136714908956c91fb99c59c31a2aac6af5725fb621791414c832e88bfc16430f334f0284062618b434d83534cd0c0a4e9fc2d1f  crash-01-00-14646-61faa3e6-core
7faf89d978dbca2182226cbe7e6526655553d0ca2b58660b518ee3909fe3f576906d714cf5fe6eee5de7041a2947244c13cf33edb95176cc749f937743c64734  crash-01-00-16099-61faa42e-core
```

Submit all command output, calculated hash values, and core files collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Five - Collect Nonvolatile System Information and Artifacts

This procedure outlines how to collect additional system information and artifacts that might be germane in a forensic assessment of a StarOS platform. The following categories of information are collected in this step:

- Process list

- Process memory maps (smaps)

- Installed modules

- IP tables

- System startup script

- Copy of the /etc/passwd file

Note: The artifacts collected in this section may be gathered by the following methods, or a combination of the following methods:

- Copying native files off the platform

- Piping command output to a file and then copying the file off

- Displaying the contents of file and capturing the output displayed on the screen

In all cases, it is recommended to have screen capture enabled on the terminal emulator being used to connect to the platform under analysis.

An example of this procedure follows:

```
[local]qvpc-si# debug shell
Last login: Wed Apr 16 09:14:11 -0500 2025 on pts/3 from 192.168.1.2.

qvpc-si:ssi# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2056   644 ?        Ss    2021   0:26 init [5]  
root         2  0.0  0.0      0     0 ?        S     2021   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S     2021   0:00 [ksoftirqd/0]
root         6  0.0  0.0      0     0 ?        S     2021   0:00 [migration/0]
root         7  0.0  0.0      0     0 ?        S     2021   0:03 [watchdog/0]
root         8  0.0  0.0      0     0 ?        S     2021   0:00 [migration/1]
root         9  0.0  0.0      0     0 ?        S     2021   0:00 [kworker/1:0]
root        10  0.0  0.0      0     0 ?        S     2021   0:01 [ksoftirqd/1]
root        11  0.0  0.0      0     0 ?        S     2021   1:58 [kworker/0:1]
root        12  0.0  0.0      0     0 ?        S     2021   0:03 [watchdog/1]
root        13  0.0  0.0      0     0 ?        S     2021   0:00 [migration/2]
root        15  0.0  0.0      0     0 ?        S     2021   0:00 [ksoftirqd/2]
root        16  0.0  0.0      0     0 ?        S     2021   0:00 [watchdog/2]
root        17  0.0  0.0      0     0 ?        S     2021   0:00 [migration/3]
root        18  0.0  0.0      0     0 ?        S     2021   0:00 [kworker/3:0]
root        19  0.0  0.0      0     0 ?        S     2021   0:00 [ksoftirqd/3]
root        20  0.0  0.0      0     0 ?        S     2021   0:00 [watchdog/3]
root        21  0.0  0.0      0     0 ?        S     2021   0:00 [migration/4]
root        22  0.0  0.0      0     0 ?        S     2021   0:00 [kworker/4:0]
root        23  0.0  0.0      0     0 ?        S     2021   0:00 [ksoftirqd/4]
root        40  0.0  0.0      0     0 ?        S     2021   0:03 [watchdog/8]
root        41  0.0  0.0      0     0 ?        S     2021   0:00 [migration/9]
root        42  0.0  0.0      0     0 ?        S     2021   0:00 [kworker/9:0]
root        43  0.0  0.0      0     0 ?        S     2021   0:00 [ksoftirqd/9]
root        44  0.0  0.0      0     0 ?        S     2021   0:03 [watchdog/9]
[output truncated]

qvpc-si:ssi# tail -n +1 /proc/*/smaps 2>/dev/null | gzip > /flash/all-process-smaps.gz

qvpc-si:ssi# lsmod
rte_kni 285701 1 - Live 0xffffffffa03f4000
igb_uio 12698 4 - Live 0xffffffffa03af000
ucad_shim_fifo 29388 2 - Live 0xffffffffa0344000
be2net 115864 0 - Live 0xffffffffa03d5000
i40evf 99938 0 - Live 0xffffffffa03ba000
i40e 223528 0 - Live 0xffffffffa0376000
ixgbevf 63497 0 - Live 0xffffffffa0364000
enic 65157 0 - Live 0xffffffffa0352000
ixgbe 198032 0 - Live 0xffffffffa0311000
mdio 12616 0 - Live 0xffffffffa020c000
mlx5_core 725534 0 - Live 0xffffffffa025d000
mlxfw 17196 1 mlx5_core, Live 0xffffffffa0238000
rdma_ucm 26278 0 - Live 0xffffffffa0254000
rdma_cm 48931 1 rdma_ucm, Live 0xffffffffa023e000
iw_cm 35373 1 rdma_cm, Live 0xffffffffa022d000
ib_ucm 17965 0 - Live 0xffffffffa00e8000
ib_uverbs 105653 2 rdma_ucm,ib_ucm, Live 0xffffffffa0211000
ib_umad 21448 0 - Live 0xffffffffa01c7000
ib_cm 47547 2 rdma_cm,ib_ucm, Live 0xffffffffa01b9000
ib_core 228522 7 rdma_ucm,rdma_cm,iw_cm,ib_ucm,ib_uverbs,ib_umad,ib_cm, Live 0xffffffffa01d2000
mlx_compat 37946 9 mlx5_core,rdma_ucm,rdma_cm,iw_cm,ib_ucm,ib_uverbs,ib_umad,ib_cm,ib_core, Live 0xffffffffa017f000
e1000e 180648 0 - Live 0xffffffffa018a000
e1000 134635 0 - Live 0xffffffffa015c000
vmxnet3 48126 0 - Live 0xffffffffa014e000
vhost_net 30934 0 - Live 0xffffffffa0144000
virtio_net 26516 0 - Live 0xffffffffa0074000
knpusim 328185 0 - Live 0xffffffffa00f1000 (P)
knpushm 430936 11 knpusim, Live 0xffffffffa007c000 (P)
virtio_scsi 13093 0 - Live 0xffffffffa0027000
virtio_blk 12655 0 - Live 0xffffffffa0050000
vmw_pvscsi 21352 0 - Live 0xffffffffa006c000
ata_piix 29415 0 - Live 0xffffffffa0062000
mptsas 43753 0 - Live 0xffffffffa0055000
mptspi 21935 2 - Live 0xffffffffa003f000
mptscsih 26768 2 mptsas,mptspi, Live 0xffffffffa0047000
mptbase 68795 3 mptsas,mptspi,mptscsih, Live 0xffffffffa002c000
ub 22054 0 - Live 0xffffffffa0015000
uhci_hcd 30584 0 - Live 0xffffffffa001d000
ehci_hcd 75018 0 - Live 0xffffffffa0000000

qvpc-si:ssi# iptables --list
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination   

qvpc-si:ssi# cp /etc/rc /flash/rc
qvpc-si:ssi# cp /etc/passwd /flash/passwd
qvpc-si:ssi# exit
logout
Connection to localhost closed.

[local]qvpc-si# copy /flash/all-process-smaps.gz tftp://172.16.0.50/all-process-smaps.gz
******************************************************************************
Transferred 109008 bytes in 0.008 seconds (13306.6 KB/sec)

[local]qvpc-si# copy /flash/rc tftp://172.16.0.50/rc
******************************************************************************
Transferred 199228 bytes in 0.030 seconds (6485.3 KB/sec)

[local]qvpc-si# copy /flash/passwd tftp://172.16.0.50/passwd   
******************************************************************************
Transferred 114 bytes in 0.001 seconds (111.3 KB/sec)
```

Submit all command output, calculated hash values, and core files collected in this section to the relevant TAC SR and proceed to the next section of this document.

## Step Six - Enumerate Line Card Processes

This step outlines how to collect a list of processes running on any line cards that might be installed in a hardware chassis that is running Cisco StarOS Software. Only line cards of type Univ Data Processing Card should be enumerated.

Use the following commands to display line cards installed on the platform, connect to specific line cards, and display the processes running on that line card:

```
show card table

	debug shell card cpu ps -aef
```

An example of this procedure follows:

```
[local]ASR5500# show card table
Tuesday March 05 17:13:14 EST 2024
Slot       Card Type                              Oper State   SPOF  Attach
---------  -------------------------------------  -----------  ----  ------
 1: DPC    None                                   -              -
 2: DPC    Univ Data Processing Card              Active         No
 3: DPC    Univ Data Processing Card              Standby        -
 4: DPC    None                                   -              -
 5: MMIO   Univ Management & 20x10Gb I/O Card     Active         Yes
 6: MMIO   Unsupported/Unknown                    Offline        -
 7: DPC    None                                   -              -
 8: DPC    Univ Data Processing Card              Active         No
 9: DPC    Univ Data Processing Card              Active         No
10: DPC    None                                   -              -
11: SSC    System Status Card                     Active         No
12: SSC    System Status Card                     Active         No
13: FSC    Fabric & 2x200GB Storage Card          Active         No
14: FSC    Fabric & 2x200GB Storage Card          Active         No
15: FSC    Fabric & 2x200GB Storage Card          Active         No
16: FSC    Fabric & 2x200GB Storage Card          Active         No
17: FSC    None                                   -              -
18: FSC    None                                   -              -

[local]ASR5500# debug shell card 2 cpu 1
Tuesday March 05 17:13:32 EST 2024
Last login: Fri Feb 23 11:20:26 -0500 2024 on pts/1 from 172.16.4.1.

asr5500:card2-cpu1# ps -aef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Feb21 ?        00:00:12 init [2]
root         2     0  0 Feb21 ?        00:00:00 [kthreadd]
[output truncated]
```

Submit all command output, calculated hash values, and core files collected in this section to the relevant TAC SR.

## Related Documentation

Additional information about Cisco Software Integrity Assurance, as well as forensic investigation procedures for other platforms, is available in Cisco Security Tactical Resources:

https://sec.cloudapps.cisco.com/security/center/tacticalresources.x

## StarOS Platform Forensic Response Checklist

Step 1 – Create the StarOS Device Problem Description

Device problem description uploaded to SR

Step 2 – Collect a StarOS show support details File

Output of show support details uploaded to SR

Step 3 – Obtain StarOS System Image Hash Value

Output of md5sum uploaded to SR

Step 4 – Gather Critical Process Core Files

vpnctrl core file uploaded to SR

vpnmgr core file uploaded to SR

sessctrl core file uploaded to SR

sessmgr core files uploaded to SR

aaamgr core file uploaded to SR

diamproxy core file uploaded to SR

gtpcmgr core file uploaded to SR

imsimgr core file uploaded to SR

sgtpmgr core file uploaded to SR

egtpinmgr core file uploaded to SR

gtpumgr core file uploaded to SR

npumgr core file uploaded to SR

cli core file uploaded to SR

Hash values of all core files uploaded to SR

Step 5 – Collect Nonvolatile System Information and Artifacts

Process list uploaded to SR

Process memory maps uploaded to SR

Installed modules list uploaded to SR

IP tables rules uploaded to SR

Copy of the rc startup script uploaded to SR

Copy of the /etc/passwd file uploaded to SR

Step 6 - Enumerate Line Card Processes

Process lists for all Univ Data Processing Cards uploaded to SR

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
| 1.0 | March 23, 2022 | D.  Maunz/J. Barnes | Initial  public release. |
| 1.1 | March 17, 2023 | Dan Maunz | Validated procedures on Release 21.28.m4. |
| 1.2 | March 28, 2024 | Dan Maunz | Simplified Step 4, tested procedures on Release 21.28.m18, and added Step 6. |
| 1.3 | April 16, 2025 | Dan Maunz | Validated procedures on v21.28.m33. |
| 1.4 | May 11, 2026 | Dan Maunz | Validated procedures on v21.28.mh37. |