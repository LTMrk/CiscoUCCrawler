---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-0-virtual-machine-exwy-b-cisco-expressway-on-vi-86ad3a3791
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-0/virtual-machine/exwy_b_cisco-expressway-on-virtual-machine-installation-guide-x14-0/exwy_b_vm-install-guide_chapter_010.html
retrieved_at: 2026-08-16T22:17:25.122850+00:00
---

Cisco Expressway on Virtual Machine Installation Guide (X14.0)

# Cisco Expressway on Virtual Machine Installation Guide (X14.0)

Updated: April 14, 2021

Chapter: System Requirements

## Chapter: System Requirements

# System Requirements

## Recommended Platform

See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-expressway.html for the current list of supported UCS Tested Reference Configurations and specs-based supported platforms.

## Virtual Machine Requirements

Make sure that the following requirements are in place:

VT is enabled in the BIOS before you install VMware ESXi.

The VM host “ Virtual Machine Startup/Shutdown ” setting is configured to “ Allow Virtual machines to start and stop automatically with the system ”, and the VM Expressway has been moved to the Automatic startup section.

Do not change the MAC address of the VM

The serial number of a virtual Expressway is based on the virtual machine's MAC address. The serial number is used to validate
                              Expressway licenses and to identify Expressways that are registered to the Cisco Webex cloud. Do not change the MAC address
                              of the Expressway virtual machine when using VMware tools, or you risk losing service.

Use the VM .ova file for initial VM installation only

The VM Expressway is licensed using information that is generated at the time of the .ova file installation. If the .ova was
                              installed a second time, new licensing information would be created, and to use the new VM, new release and licence keys would
                              need to be purchased. To upgrade a VM Expressway, follow the procedure under Upgrading or Downgrading an Expressway VM , using the .tar.gz version of the Expressway software.

Take a backup after completion

After the VM installation is complete, we recommend that you take a backup of the configuration (described in Creating a Backup of your System and Deleting Existing Snapshots ).

Do not take VMware snapshots of Cisco Expressway systems. The process interferes with database timing and negatively impacts
                                          performance.

## Specifications-Based System – Minimum Specification

If you use a UCS Tested Reference Configuration or specifications-based system, the minimum requirements are:

Deployment size

vCPU

Reserved CPU resource

Reserved RAM

Disk space

NIC

Small

2 core

3600 MHz (2 x 1.8 GHz)

4 GB

132 GB

1 Gb

Medium

2 core

4800 MHz (2 x 2.4 GHz)

6 GB

132 GB

1 Gb

Large (extra performance and scalability capabilities)

8 core

25600 MHz (8 x 3.2 GHz)

8 GB

132 GB

1 Gb

Two Large Expressway VMs can co-reside on a UCS server with two eightcore 3.2 GHz
                              processors all dedicated to Expressway, when hyperthreading is enabled. To allow for
                              hypervisor overhead, the CPU reservation is set to 16000 MHz, but the full
                              allocation of 8x 3.2 GHz CPU cores must be made available to each Large Expressway
                              VM. The reservation does not limit maximum Expressway CPU speed, as the Expressway
                              can use the headroom provided by the higher specification host.

For all deployment sizes, you need the following:

VM host operational and running a supported ESXi version (see ESXi Requirements ).

From X12.5, the Expressway no longer supports ESXi 5.5 or earlier versions.

VMware vCenter or vSphere client operational. Depending on the client software version, you may need to use the Flash-based
                                    version (not HTML5) due to customized template requirements.

The desktop vSphere Client is not available from vSphere 6.5 and later.

Reserved RAM, CPU, and NIC as per table above.

Subject to bandwidth constraints, Large VMs can run with a 1 Gbps NIC.

## How to Modify Expressway VM Capacity

Increasing the capacity of a VM-based Expressway from a smaller deployment size to a larger
                           			deployment (Small -> Medium -> Large) or decreasing the capacity from a larger
                           			deployment to a smaller one (Large -> Medium -> Small) cannot be done by
                              				simply increasing or decreasing the underlying vCPUs and memory hardware resources
                              				of the VM . The correct method to upgrade or downgrade is to deploy a new VM of
                           			the required deployment size, and then restore the existing configuration (smaller VM
                           			for upgrade and larger VM for downgrade) onto the new one. The process to do this is
                           			outlined later in this guide in Upgrading or Downgrading an Expressway VM .

## ESXi Requirements

The minimum virtual hardware required to host virtual Expressway deployments is VMware ESXi 6.5. Cisco does not support Expressway
                              VMs hosted on ESXi 6.0 or earlier (these versions are no longer supported by VMware).

New installations of Expressway OVAs will not run on any host version before ESXi 6.5.

The following are the ESXi supported versions for X12.7. For new Expressway VM deployments, the Expressway OVAs must be installed
                              on any of the following versions. If you have existing VM deployments running on an ESXi 6.0 or earlier versions, upgrade the host to any of the following versions before you install the new Expressway software.

ESXi 6.5 Update 2

ESXi 6.7 Update 1 from X12.5.2, and Update 2 - for Large VMs only - from
                                    X12.5.4

ESXi 6.7 Update 3 from X12.6.1 for Large and Medium VMs

ESXi 6.7 Update 3 from X12.6.3 for Small VMs

ESXi 7.0

For upgrade instructions, see your VMware documentation.

If you migrate an existing VM to a different host, you must shut down the VM before you move it.

More information

Instructions about installing new Cisco Expressway VMs are in the Cisco Expressway on Virtual Machine Installation Guide on
                                    the Expressway Install and Upgrade Guides page

Instructions about how to upgrade a single (non-clustered) Expressway VM are also in the Cisco Expressway on Virtual Machine
                                    Installation Guide

Instructions about upgrading a clustered Expressway VM system are in the Cisco Expressway Cluster Creation and Maintenance
                                    Deployment Guide on the Cisco Expressway Series configuration guides page

For information about VMware supported versions, see https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/support/product-lifecyclematrix.pdf

If using the vSphere client, configure the network properties through the console.

## Co-residency Support

The Expressway can co-reside with applications (any other VMs occupying same host) subject to the following conditions:

No oversubscription of CPU. You need one-to-one allocation of vCPU to physical cores.

No oversubscription of RAM. You need one-to-one allocation of vRAM to physical memory

No oversubscription of NIC. The Expressway handles large volumes of data, much of which is for real-time communications, and
                                    it needs dedicated access to all the bandwidth specified for its interfaces.

For example, you should not assume that four co-resident small Expressway VMs can handle the expected load if there is only
                                    a 1 Gbps physical interface on the host. In this case none of the VMs meet the required minimum specification.

Sharing disk storage subsystem is supported, subject to correct performance (latency, bandwidth) characteristics.

| Warning | The Expressway ova virtual appliances are designed to meet the minimum deployment requirements. Do not change the ova configuration
                                       after installation, as Cisco may no longer be able to support your deployment. |
|---|---|

| Caution | Do not take VMware snapshots of Cisco Expressway systems. The process interferes with database timing and negatively impacts
                                          performance. |
|---|---|

| Deployment size | vCPU | Reserved CPU resource | Reserved RAM | Disk space | NIC |
|---|---|---|---|---|---|
| Small | 2 core | 3600 MHz (2 x 1.8 GHz) | 4 GB | 132 GB | 1 Gb |
| Medium | 2 core | 4800 MHz (2 x 2.4 GHz) | 6 GB | 132 GB | 1 Gb |
| Large (extra performance and scalability capabilities) | 8 core | 25600 MHz (8 x 3.2 GHz) | 8 GB | 132 GB | 1 Gb |

| Note | The minimum versions specified here are subject to VMware support. The versions
                                       are correct when this documentation is published, but if VMware subsequently
                                       withdraws support for any stated version, you may need to use newer ESXi
                                       versions. |
|---|---|

| Note | If you migrate an existing VM to a different host, you must shut down the VM before you move it. |
|---|---|