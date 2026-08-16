---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-0-2-virtual-machine-exwy-b-cisco-expressway-on--7a7e2a962a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-0-2/virtual-machine/exwy_b_cisco-expressway-on-virtual-machine-installation-guide-x1502/exwy_m_system-requirements.html
retrieved_at: 2026-08-16T22:10:48.855367+00:00
---

Cisco Expressway on Virtual Machine Installation Guide (X15.0.2)

# Cisco Expressway on Virtual Machine Installation Guide (X15.0.2)

Updated: May 15, 2024

Chapter: System Requirements

## Chapter: System Requirements

# System Requirements

## Recommended Platform

See Virtualization for Cisco Expressway for the current list of supported UCS Tested Reference Configurations and specs-based supported platforms.

## Virtual Machine Requirements

Warning

We strongly recommend you not to use any power management features.

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

After the VM installation is complete, we recommend that you take a backup of the configuration (described in Creating a Backup of Your System and Deleting Existing Snapshots ).

Caution

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

3600 MHz (2 x 1.8 GHz) (i.e., 2 x a single speed of 1.8 GHz per single core)

4 GB

132 GB

1 Gb

Medium

2 core

4800 MHz (2 x 2.4 GHz) (i.e., 2 x a single speed of 2.4 GHz per single core)

6 GB

132 GB

1 Gb

Large (extra performance and scalability capabilities)

8 core

25600 MHz (8 x 3.2 GHz) (i.e., 8 x a single speed of 3.2 GHz per single core)

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

From X15.0.2, the Expressway no longer supports ESXi 6.7 or earlier versions.

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

The minimum VMware ESXi version required to host a new virtual Expressway X15.0.2 deployment is VMware ESXi 7.0. Cisco does
                              not support new Expressway VMs hosted on ESXi 6.7 or earlier (VMware no longer supports these versions).

New deployments of X15 are compatible only with VMware ESXi versions 7.0 U1 and 8.0 U1 and later. Expressway is supported
                              on any subsequent ESXi minor release version.

The VMware Virtual Machine Hardware Version embedded in the OVA may change on a per-release basis. If it is updated, it can
                              impact which versions of ESXi it can be deployed on. Current compatibility and historical reference information is available
                              at: Virtualization for Cisco Expressway Series .

For upgrade instructions, see your VMware documentation.

If you migrate an existing VM to a different host, you must shut down the VM before you move it.

More information

Instructions about installing new Cisco Expressway VMs are in the Cisco Expressway on Virtual Machine Installation Guide on
                                    the Expressway Install and Upgrade Guides page

Instructions about how to upgrade a single (non-clustered) Expressway VM are also in the Cisco Expressway on Virtual Machine
                                    Installation Guide

Instructions about upgrading a clustered Expressway VM system are in the Cisco Expressway Cluster Creation and Maintenance
                                    Deployment Guide on the Cisco Expressway Series configuration guides page

For information about VMware supported versions, see Product Lifecycle Matrix .

If using the vSphere client, configure the network properties through the console.

### Limitation

This issue applies to Expressways running as virtualized systems with certain ESXi versions using VMware vCenter 7.0.x (Prior to X15.0.2 for which this is not a valid configuration). . It was found during testing using VMware vCenter 7.0.1 with ESXi 6.7.0 to deploy an Expressway OVA. The Ready to complete final page of the Deploy OVF Template wizard displays template values instead of the actual values entered on the earlier wizard pages. The issue is cosmetic,
                                    and when you click "FINISH" the OVA will deploy as expected using the entered values. Bug ID CSCvw64883 refers.

Video calling capacity may be restricted if the ESXi Side-Channel-Aware Scheduler is enabled, and CPU load exceeds 70%.

With physical  appliances, the Advanced Networking feature allows the speed and duplex mode to be set for each configured Ethernet port. You cannot set port speeds for virtual
                                    machine-based  systems.

Also, virtual machine-based systems always show the connection speed between  and Ethernet networks as 10000 Mb/s, regardless
                                    of the actual physical NIC speed. This is due to a limitation in virtual machines, which cannot retrieve the actual speed
                                    from the physical NIC(s).

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

| Note | We strongly recommend you not to use any power management features. |
|---|---|

| Caution | Do not take VMware snapshots of Cisco Expressway systems. The process interferes with database timing and negatively impacts
                                          performance. |
|---|---|

| Deployment size | vCPU | Reserved CPU resource | Reserved RAM | Disk space | NIC |
|---|---|---|---|---|---|
| Small | 2 core | 3600 MHz (2 x 1.8 GHz) (i.e., 2 x a single speed of 1.8 GHz per single core) | 4 GB | 132 GB | 1 Gb |
| Medium | 2 core | 4800 MHz (2 x 2.4 GHz) (i.e., 2 x a single speed of 2.4 GHz per single core) | 6 GB | 132 GB | 1 Gb |
| Large (extra performance and scalability capabilities) | 8 core | 25600 MHz (8 x 3.2 GHz) (i.e., 8 x a single speed of 3.2 GHz per single core) | 8 GB | 132 GB | 1 Gb |

| Note | The minimum versions specified here are subject to VMware support. The versions are correct when this documentation is published,
                                       but if VMware subsequently withdraws support for any stated version, you may need to use newer ESXi versions. |
|---|---|

| Note | If you migrate an existing VM to a different host, you must shut down the VM before you move it. |
|---|---|