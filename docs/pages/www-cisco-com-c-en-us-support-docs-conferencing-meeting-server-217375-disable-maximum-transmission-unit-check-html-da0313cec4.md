---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-217375-disable-maximum-transmission-unit-check-html-da0313cec4
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/217375-disable-maximum-transmission-unit-check.html
retrieved_at: 2026-08-16T14:22:02.284133+00:00
---

Disable Maximum Transmission Unit Check Enforcement in ESXi

# Disable Maximum Transmission Unit Check Enforcement in ESXi

Log in to Save Content

### Download Options

Updated: September 20, 2021

Document ID: 217375

Contents

## Contents

# Introduction

This document describes the Maximum Transmission Unit (MTU) check on the virtual vmxnet3 Network Interface Cards (vNICs) enforced on ESXi 6.7 update 2 and later.

# Prerequisites

## Requirements

Cisco recommends that you have knowledge of these topics:

- VMWare Virtual Machine network configurations in ESXi

- Cisco Meeting Server (CMS) Command line interface (CLI)

## Components Used

The information in this document is based on CMS that runs as a virtual machine.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

In particular, this document refers to the CMS but affects any virtual machine that meets the floowing requirements:

- ESXi version 6.7 update 2 or later

- vmxnet3 adapter in use

- Changes of MTU at the vNIC level of the virtual machine

# Background Information

In ESXi version 6.7 update 2 and later, the default behavior of the platform is enforced to perform a MTU check on the receiving path and will not allow packets that are larger than the vNIC's MTU size.

Prior to this version, this check was not enforced and this can increase the likelihood of packet drops when the MTU size is changed on the virtual machine (VM) that's using the vmxnet3 vNICs.

For example, if the vSwitch is set to receive an MTU of 1500 bytes but the vNIC MTU of the VM is lowered to 1300 bytes, and a packet greater than 1300 bytes is received, then this packet gets dropped or discarded.

# Problem: Potential packet loss when the MTU size is lowered

Environments that runs Cisco Meeting Server (or other applications that modify MTU at vNIC level and use vmxnet3 adapter) VM on ESXi version 6.7 update 2 and later, can experience issues of packet loss when the MTU is lowered due to this default behavior change.

The MTU is lowered with the command iface <interface> mtu <value> on the CMS Mainboard Management Processor ( MMP) configuration which then sets the value at the vNIC in order to lower latency of packets in the network.

More details about these changes can be found at this VMware article .

# Solution

Below are options that can help to resolve this issue.

Note : Options 1 and 2 require that the ESXi environment have installed the patch release of ESXi670-201912001 so that the option is available for modification of the vmxnet3 configuration for the MTU check. More information on this can be found in the release notes for the patch release. Which the text below refers.

" PR 2409342: You cannot select to disable the Maximum Transmission Unit (MTU) check in the vmxnet3 backend for packet length to not exceed the vNIC MTU

With ESXi670-201912001, you can select to disable the Maximum Transmission Unit (MTU) check in the vmxnet3 backend for packet length to not exceed the vNIC MTU. The default behavior is to perform the MTU check. However, if you use vmxnet3, as a result of this check, you might see an increase of dropped packets. For more information, see VMware knowledge base article 75213 .

This issue is resolved in this release. "

## Option 1: Host wide configuration

As stated prior, this option requires the patch release ( ESXi670-201912001 ) to be installed. The below details are taken directly from the resolution section of the VMware document 75213.

esxcli system settings advanced set -o "/Net/vmxnet3NonTsoPacketGtMtuAllowed" -i 1

Note : This configuration is applicable over all vmxnet3 vNIcs (host-wide). This setting is then applied to each VM that's powered on after making this change.

## Option 2: vNIC specific configuration

As stated prior, this option requires the patch release ( ESXi670-201912001 ) to be installed. The below details are taken directly from the resolution section of the VMware document 75213.

" Use ethernet0.rxAllowPktGtMtu = "1" in the vmx file:

Where "ethernet0" should be replaced by the specific vNic on which the configuration is to be applied.

Please use VMware KB article to follow steps on How to:

Modifying advanced virtual machine settings using vSphere client (1016098) KB ."

## Option 3:  Workaround

For the workaround option, you have the option to revert the MTU configuration on the application/VM so that it is set to receive what is accepted in the network.

For example, if the vSwitch is set to to receive MTU size of 1500 and thus the Virtual machine vNIC must be set to match this. If the environment runs CMS, then you must set the interface MTU to what is expected.

For example: iface a mtu 1500 configured on CMS MMP .

The other option would be to ensure the network is configured so that packets that arrive to the vNIC do not exceed the set MTU value for the vNIC. This would need to be done throughout the network to ensure that fragmentation is set correctly.

# Related Information

- Technical Support & Documentation - Cisco Systems

### Revision History

2.0

20-Sep-2021

Corrected inconsistent font sizes.

1.0

19-Sep-2021

Initial Release

### Contributed by Cisco Engineers

Brent Huff

Cisco TAC Engineer

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

### This Document Applies to These Products

- Meeting Server

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 20-Sep-2021 | Corrected inconsistent font sizes. |
| 1.0 | 19-Sep-2021 | Initial Release |