---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200615-cisco-ip-pho-04f1620e39
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200615-Cisco-IP-Phone-Feature-Peer-Firmware-S.html
retrieved_at: 2026-08-21T13:56:57.446742+00:00
---

Cisco IP Phone Feature - Peer Firmware Sharing

# Cisco IP Phone Feature - Peer Firmware Sharing

Updated: May 23, 2018

Document ID: 200615

Contents

## Contents

## Introduction

This document describes the Peer Firmware Sharing (PFS) feature of the IP Phone that allows IP Phones located at remote sites in order to share firmware files amongst them, unlike the traditional method of IP Phone firmware upgrade that demands the Trivia File Tranfer Protocol (TFTP) server to send firmware files to each phone.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communication Manager (CUCM)

- IP Phone Firmware Upgrade Process

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM 10.5.2.10000-5.

- Cisco Unified IP Phone 7961 and 7961G.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

In the traditional firmware upgrade process, the TFTP server is supposed to communicate individually with each phone, and send the upgrade files to them simultaneously. However, consider a scenario wherein 1000 phones are located at a remote site and the TFTP server at the headquarters is approximately 15000 kms away. In this case, phones are connected to the server over the Wide Area Network (WAN), and in a huge quantity. So, the firmware upgrade for these phones takes a considerable amount of time.

PFS allows IP Phones located at remote sites to share the firmware files amongst them, which saves bandwidth when the upgrade process takes place. This feature uses Cisco Peer to Peer Distribution Protocol which is a Cisco proprietary protocol used to form a peer to peer hierarchy of devices. Cisco Peer to Peer Distribution Protocol is also used to copy firmware or other files from peer devices to the neighbouring devices.

PFS is included in the phone firmware versions 8.3(1) (and above) which ships as a part of the CUCM 6.0 release. It will be applicable to 3rd Gen Cisco IP Phones that includes:

- 7906

- 7911

- 7931

- 7941 7961 (Gig and non-Gig)

- 7970 7971

- Future 3rd Gen phone models will be supported as well.

Note : PFS is neither applicable to 2nd generation 7960 or 7940 phones nor to OEM phones like the Tandberg video phones.

Here are some of the key advantages of PFS over the traditional upgrade method:

- Limits congestion on the link between centralized TFTP server and the remote IP phones.

- Helps in the case of low bandwidth scenarios.

- The more the number of IP phones, the better it's performance compared to the traditional firmware upgrade method.

## Working

- The PFS field needs to be enabled in order for this to work.

- PFS works in a hierarchy, where one phone becomes the parent, and the other, its child phone. When the upgrade is initiated, the TFTP sends the firmware files (one by one) to the parent phone. The other phones wait till the download of the component is complete on the parent. Then, once one component is received completely by the parent, it passes it on to its child phones through a TCP connection. This works in the manner of a binary tree, where one phone can have maximum 2 child phones as shown in the image:

Figure 1. Peer Firmware Sharing Distribution Hierarchy

Figure 2. Hierarchical Difference between Traditional Upgrade Method and PFS

Figure 2 (a). Traditional Firmware Upgrade

Figure 2 (b). PFS

## Configure PFS

Only the PFS field needs to have the value enabled on either of these in decreasing order of precedence as shown in the image:

1. Phone Configuration page of every remote device.

2. Common Phone Profile.

3. Enterprise Phone Configuration.

This is an excerpt from the console logs taken from the root phone, in order to confirm that PFS works here:

```
"DBG 02:19:22.634167 DLoad: +++ fd=7 Listening on peer TCP port 4051"
```

Indicates the phone starts the process of peer to peer and is ready to listen to the handshake packets to setup a Peer to Peer structure before it shares the firmware:

```
NOT 02:19:22.634945 DLoad: ^.idl_child.c-openUDPPort
NOT 02:19:22.664131 DLoad: |parent=-1><fd[0]=-1 fd[1]=-1 FULL=0
```

```
"NOT 02:19:23.161938 DLoad: ^.idl_protocol.c-sendBroadcastOffer"
```

Phone sends a broadcast Offer message to all the peers, when it becomes the root:

```
"NF 02:19:23.162700 DLoad: XID080027F8 TxBdcst ClaimRoot(tent): map=ff9d7cb9
strength=31d4d43d "
```

Indicates the phone started to claim itself in the subnet that it is the root of peer to peer sharing:

```
"NOT 02:19:23.410198 DLoad: ^.idl_timeout.c-doTimeout
DBG 02:19:23.410963 DLoad: Timeout XID080027F8 hier=ClaimRoot(tent)
NOT 02:19:23.411644 DLoad: ^.idl_protocol.c-sendBroadcastOffer
INF 02:19:23.411925 DLoad: XID080027F8 TxBdcst Ad 1: ClaimRoot(tent)
NOT 02:19:23.660235 DLoad: ^.idl_timeout.c-doTimeout
DBG 02:19:23.661014 DLoad: Timeout XID080027F8 hier=ClaimRoot(tent)
NOT 02:19:23.661772 DLoad: ^.idl_protocol.c-sendBroadcastOffer
INF 02:19:23.662527 DLoad: XID080027F8 TxBdcst Ad 2: ClaimRoot(tent)
NOT 02:19:23.910338 DLoad: ^.idl_timeout.c-doTimeout
DBG 02:19:23.911135 DLoad: Timeout XID080027F8 hier=ClaimRoot(tent)
NOT 02:19:23.911966 DLoad: ^.idl_protocol.c-sendBroadcastOffer
INF 02:19:23.912719 DLoad: XID080027F8 TxBdcst Ad 3: ClaimRoot(tent)INF
02:19:34.410208 DLoad: XID080027F8 Root sending TFTP XfrCmd on ROOT_WAITING
TO
NOT 02:19:24.160548 DLoad: ^.idl_timeout.c-doTimeout
DBG 02:19:24.161318 DLoad: Timeout XID080027F8 hier=ClaimRoot(tent)
NOT 02:19:24.162076 DLoad: ^.idl_protocol.c-sendBroadcastOffer
INF 02:19:24.162828 DLoad: XID080027F8 TxBdcst Ad 4: ClaimRoot(tent)
NOT 02:19:24.410188 DLoad: ^.idl_timeout.c-doTimeout
DBG 02:19:24.411262 DLoad: Timeout XID080027F8 hier=ClaimRoot(tent)"
```

Indicates multiple timeouts when it does not get any responses:

```
"NOT 02:19:24.412095 DLoad: UT:Confirmed root bumping strength"
```

Phone becomes the root since it did not get any incoming packets of handshaking from the peers:

```
NOT 02:19:24.412806 DLoad: @@@HROOT:XID080027F8 H=36685558 m=CP-7961G
ROOT=10.106.117.68 /dnld/SCCP41.9-4-2SR2-2S.loads
```

Mark a difference between both:

When you enable PFS from the Phone Configuration page, there is no considerable difference between PFS and the traditional method of upgrade. However, while the upgrade is in process, a few differences can be marked from the phone screens.

Traditional Upgrade Method

PFS

All the phones show the same screen throughout the process. For example, if there is one component that is downloaded on one phone, others also show the same.

Some of the phones show a different behavior here. Basically, whoever is/are the parent(s) at one instant, might show the status of component x as 100%, whereas others still upgrade to component x, and, show the KBs that are downloaded for x.

The box is blank for a traditional upgrade as shown in the image.

You can see the PFS icon at the top right corner of the screen of the phones at the time of upgrade as seen in the image.

Phone 1:

Phone 1:

Phone 2:

Phone 2:

Phone 3:

Phone 3:

Phone 4:

Phone 4:

Points to Remember:

- PFS works on a file by file basis. One phone might become parent for one file or child for another, at the time of the same upgrade.

- PFS is phone-model specific; different phone types will form multiple hierarchies.

- PFS can only work with phones in the same subnet.

- The more the number of devices, the better is its performance.

- It gives better results when phones are reset in bulk.

- All UDP broadcast traffic and TCP child connections from phone to phone take place on port 4051.

- For Cisco Communications Manager 5.0 and later, enable Peer Firmware Settings in the Phone Template window of the Bulk Administration Tool.

- Navigate to http://www.cisco.com/cgi-bin/tablebuild.pl/ip-7900ser .

- Download ccmppid.exe and ccmppid readme .

- Install ccmppid.exe in accordance to the readme file instructions.

## Bugs

- CSCtg96408 - Third-gen phone (7911/41, etc) fails to boot after PFS upgrade.

- CSCso40251 - No "Peer Firmware Sharing" field for 7975/7965 in CUCM ES 5.1.2.3127-1.

- CSCsh98792 - CM 5.x/6.0 Bulk Admin Update Phones fails to set product specific params.

- CSCud66570 - 7931 Peer Firmware Sharing always disabled.

- CSCui49910 - [Pegatron]"No ""peer firmware sharing"" in network setup of web page".

- CSCus67416 - Enable "Peer Firmware Sharing", Phone B still go to servers download fw.

- CSCtb49726 - Peer File sharing Option is missing On Product specific conf on 7942/62.

- CSCsh20977 - Adding new Product Specific features Peer Firmware Sharin gn World Wide.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

| Traditional Upgrade Method | PFS |
|---|---|
| All the phones show the same screen throughout the process. For example, if there is one component that is downloaded on one phone, others also show the same. | Some of the phones show a different behavior here. Basically, whoever is/are the parent(s) at one instant, might show the status of component x as 100%, whereas others still upgrade to component x, and, show the KBs that are downloaded for x. |
| The box is blank for a traditional upgrade as shown in the image. | You can see the PFS icon at the top right corner of the screen of the phones at the time of upgrade as seen in the image. |
| Phone 1: | Phone 1: |
| Phone 2: | Phone 2: |
| Phone 3: | Phone 3: |
| Phone 4: | Phone 4: |