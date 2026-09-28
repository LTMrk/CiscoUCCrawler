---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-collaboration-systems-release-217288-how-to-build-a-linux-serv-90b0aa3ec4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/collaboration-systems-release/217288-how-to-build-a-linux-server-and-untar-th.html
retrieved_at: 2026-08-16T18:27:59.445948+00:00
---

How to Build a Linux Server and Untar the CIMC and BIOS bin files from UCS HUU?

# How to Build a Linux Server and Untar the CIMC and BIOS bin files from UCS HUU?

### Download Options

Updated: August 5, 2021

Document ID: 217288

Contents

## Contents

## Introduction

The document describes the procedure to build the Linux server and unzip the cimc.bin and bios.bin file from HUU ISO.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- UCS

- Linux

### Components Used

The information in this document is based on these software and hardware versions:

- Any VM or Hardware with resources to install RHEL

- RHEL ISO download

- Squash RPM download

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## How to Build this Server?

### Step 1. Download the required Software.

#### Get Linux ISO

Download ISO from this global link:

https://archive.org/download/rhel-server-7.5-x86_64-dvd/rhel-server-7.5-x86_64-dvd.iso OR

Download from your lab or enterprise, if already available

#### Download Squash

http://mirror.centos.org/centos/7/os/x86_64/Packages/squashfs-tools-4.3-0.21.gitaae0aff4.el7.x86_64.rpm

### Step 2. Install Linux ISO and Install Squash.

#### Install Linux Server

Quick Installation Guide

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/installation_guide/chap-simple-install

#### Install squash

```
rpm -ivh squashfs-tools-4.3-0.21.gitaae0aff4.el7.x86_64.rpm
```

### Step 3. Configure Network on the Operating System.

#### 1. Check the Network.

```
[root@localhost ~]# ip address | grep mtu 1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 2: ens192 : <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000 Here interface to be used is ens192
```

#### 2. Assign IP and Gateway on the Interface.

In this example,

```
ens192 is the network interface 192.168.1.2 is the IP assigned to interface 192.168.1.1 is the Gateway 255.255.255.255 or /24 is the Subnet
```

3. Add the IP Address.

```
ip address add 192.168.1.2/24 dev ens192
```

4. Add the Default Gateway.

```
ip route add default via 192.168.1.1 dev ens192
```

5. Check the reachability.

Ping Gateway: ping 192.168.1.1

Now the server is ready.

## How to Upload and Untar ISO to bin Files?

### How to Upload ISO?

Upload the ISO( ex.ucs-c220m4-huu-4.1.2f.iso ) to the Linux server using SFTP Client(e.g. Filezilla)

Credentials for SFTP is root/password (this is set during OS installation) and port number is 22

Wait for the upload to complete...

### How to Untar the ISO to bin Files?

SSH to the Linux Server IP with root credentials

#### Step 1. Mount the ISO.

```
mount -t iso9660 /root/ucs-c220m4-huu-4.1.2f.iso /media/
```

#### Step 2. Copy the getfw from the CD Folder to Root Location.

```
cp /media/GETFW/getfw /root
```

#### Step 3. Run the Script.

```
./getfw -s /root/ucs-c220m4-huu-4.1.2f.iso -d /root/ Output : FW/s available at '/tmp/HUU/ucs-c220m4-huu-4.1.2f'
```

Files and location:

ucs-c220m4-huu-4.1.2f/bios / bios.bin

ucs-c220m4-huu-4.1.2f/cimc / cimc.bin

## Download the files

Download the cimc.bin or bios.bin using the SFTP client.

Unmount the media and delete the files.

```
umount /media/ rm -rf ucs-c220m4-huu-4.1.2f*
```

Note : The process is not for all HUU ISOs. Rest all HUU can be decompressed to find the bin files.

### Revision History

1.0

05-Aug-2021

Initial Release

### Contributed by Cisco Engineers

Manjunath H D

Cisco TAC Engineer

Kuhoo Tiwari

Cisco TAC Engineer

Tirtha Tripathy

Cisco TAC Engineer

### This Document Applies to These Products

- Collaboration Systems Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Aug-2021 | Initial Release |