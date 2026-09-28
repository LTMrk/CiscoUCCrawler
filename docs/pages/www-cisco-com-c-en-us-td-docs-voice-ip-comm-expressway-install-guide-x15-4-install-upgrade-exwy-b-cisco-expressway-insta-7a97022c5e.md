---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-4-install-upgrade-exwy-b-cisco-expressway-insta-7a97022c5e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-4/install-upgrade/exwy_b_cisco-expressway-install-and-upgrade-guide-x154/exwy_m_requirements-and-limitations.html
retrieved_at: 2026-08-16T22:06:55.327621+00:00
---

Cisco Expressway Install and Upgrade Guide (X15.4)

# Cisco Expressway Install and Upgrade Guide (X15.4)

Updated: April 3, 2026

Chapter: Requirements and Limitations

## Chapter: Requirements and Limitations

- Requirements and Limitations

- Virtualization Requirements

- ESXi Requirements

# Requirements and Limitations

## Virtualization Requirements

### Application/Hypervisor Compatibility

See the following table for compatibility of Unified Communications Manager and the IM and Presence Service with hypervisor
                              releases.

Only the listed major/minor releases are supported, with a minimum required maintenance or patch release.

Unlisted major/minor release trains are not supported.

For support of subsequent maintenance or patch releases, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

Compatible Hypervisor Major/Minor Releases with Minimum Maintenance

VMware vSphere ESXi

Cisco NFVIS-for-UC

Nutanix AHV

Cisco Expressway Series

Release X15.4

8.0 U1

7.0 U3

4.18.2a

AHV 10.0 + AOS /PC 7.0

Release X15.0 through X15.4 and later releases

8.0 U1

7.0 U3

Not supported

Not supported

### Virtual Machine Configurations and CPU Minimum Base Frequencies

This section details the minimum specifications required for virtual machine configurations.

Applications are supported only with specific virtual machine (VM) configurations.

You must deploy these VMs using the latest Cisco-provided OVA file  (VMware or Nutanix) or NFVIS TAR.GZ file (see the Readme
                              file for important notes.)

For Expressway, the files are available here: Cisco Software Central - Software Downloads .

One base OVA is used for both VMware vSphere ESXi and Cisco NFVIS for UC, while a set of base OVAs is used for Nutanix AHV.

See the following table for the required and supported virtual machine configurations.

Each VM represents a particular application capacity point and has a minimum required CPU base frequency.

For more information on how these are used, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications . The guide is available at the following locations:

Cisco Collaboration Systems Release 15

Cisco Unified Communications Manager (CallManager)-Install and Upgrade Guides

Component and Capacity Point

vCPU

Physical CPU Required Minimum Base Frequency

vRAM

vDisk

vNIC

ESXi

NFVIS-for-UC

Nutanix AHV

Small

2

3600 MHz (2 x 1.8 GHz)

4 GB

132 GB

140 GB

140 GB

1 GB

Medium

2

4800 MHz (2 x 2.4 GHz)

6 GB

132 GB

140 GB

140 GB

1 GB

Large (extra performance and scalability capabilities)

8

25600 MHz (8 x 3.2 GHz)

8 GB

132 GB

140 GB

140 GB

1 GB

For more information on how these are used, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications . The guide is available at the following locations:

Two Large Expressway VMs can co-reside on a UCS server with two eightcore 3.2 GHz processors all dedicated to Expressway,
                              when hyperthreading is enabled. To allow for hypervisor overhead, the CPU reservation is set to 16000 MHz, but the full allocation
                              of 8x 3.2 GHz CPU cores must be made available to each Large Expressway VM. The reservation does not limit maximum Expressway
                              CPU speed, as the Expressway can use the headroom provided by the higher specification host.

For all deployment sizes, you need the following:

Hypervisor host operational and running a supported version of the Hypervisor (see ESXi Requirements ).

From X15.0.2, Expressway no longer supports ESXi 6.7 or earlier versions.

Reserved RAM, CPU, and NIC as per table above.

Subject to bandwidth constraints, Large VMs can run with 1 Gbps NIC.

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
                                    the Expressway Install and Upgrade Guides page.

Instructions about how to upgrade a single (non-clustered) Expressway VM are also in the Cisco Expressway on Virtual Machine
                                    Installation Guide.

Instructions about upgrading a clustered Expressway VM system are in the Cisco Expressway Cluster Creation and Maintenance
                                    Deployment Guide on the Cisco Expressway Series Configuration Guides page.

For information about VMware supported versions, see Product Lifecycle Matrix .

If using the vSphere client, configure the network properties through the console.

### Limitation

This issue applies to Expressways running as virtualized systems with certain ESXi versions using VMware vCenter 7.0.x (Prior to X15.0.2 for which this is not a valid configuration) . It was found during testing using VMware vCenter 7.0.1 with ESXi 6.7.0 to deploy an Expressway OVA. The Ready to complete final page of the Deploy OVF Template wizard displays template values instead of the actual values entered on the earlier wizard pages. The issue is cosmetic,
                                    and when you click "FINISH" the OVA will deploy as expected using the entered values. Bug ID CSCvw64883 refers.

Video calling capacity may be restricted if the ESXi Side-Channel-Aware Scheduler is enabled, and CPU load exceeds 70%.

With physical  appliances, the Advanced Networking feature allows the speed and duplex mode to be set for each configured Ethernet port. You cannot set port speeds for virtual
                                    machine-based  systems.

Also, virtual machine-based systems always show the connection speed between Expressway and Ethernet networks as 10000 Mb/s,
                                    regardless of the actual physical NIC speed. This is due to a limitation in virtual machines, which cannot retrieve the actual
                                    speed from the physical NIC(s).

|  | Compatible Hypervisor Major/Minor Releases with Minimum Maintenance |
|---|---|
|  | VMware vSphere ESXi | Cisco NFVIS-for-UC | Nutanix AHV |
| Cisco Expressway Series |  |  |  |
| Release X15.4 | 8.0 U1 7.0 U3 | 4.18.2a | AHV 10.0 + AOS /PC 7.0 |
| Release X15.0 through X15.4 and later releases | 8.0 U1 7.0 U3 | Not supported | Not supported |

| Component and Capacity Point | vCPU | Physical CPU Required Minimum Base Frequency | vRAM | vDisk | vNIC |
|---|---|---|---|---|---|
| ESXi | NFVIS-for-UC | Nutanix AHV |
| Small | 2 | 3600 MHz (2 x 1.8 GHz) | 4 GB | 132 GB | 140 GB | 140 GB | 1 GB |
| Medium | 2 | 4800 MHz (2 x 2.4 GHz) | 6 GB | 132 GB | 140 GB | 140 GB | 1 GB |
| Large (extra performance and scalability capabilities) | 8 | 25600 MHz (8 x 3.2 GHz) | 8 GB | 132 GB | 140 GB | 140 GB | 1 GB |

| Note | The minimum versions specified here are subject to VMware support. The versions are correct when this documentation is published,
                                       but if VMware subsequently withdraws support for any stated version, you may need to use newer ESXi versions. |
|---|---|

| Note | If you migrate an existing VM to a different host, you must shut down the VM before you move it. |
|---|---|