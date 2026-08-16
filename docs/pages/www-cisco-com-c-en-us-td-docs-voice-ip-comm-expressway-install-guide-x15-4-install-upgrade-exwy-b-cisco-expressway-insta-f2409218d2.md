---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-4-install-upgrade-exwy-b-cisco-expressway-insta-f2409218d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-4/install-upgrade/exwy_b_cisco-expressway-install-and-upgrade-guide-x154/exwy_m_system-requirements.html
retrieved_at: 2026-08-16T22:06:59.417228+00:00
---

Cisco Expressway Install and Upgrade Guide (X15.4)

# Cisco Expressway Install and Upgrade Guide (X15.4)

Updated: April 3, 2026

Chapter: System Requirements

## Chapter: System Requirements

# System Requirements

## Supported Platforms

The following is a list of  software X15.4.0 supported platforms:

VMware vSphere ESXi on Cisco or 3rd party Hardware.

Cisco NFVIS-for-UC hypervisor on BE6K, BE7K, CE1400V appliances only

Nutanix AHV/AOS on Cisco Compute Hyperconverged with Nutanix hardware only (no appliances, no 3rdparty).

AHV version 10.0 with AOS version 7.0.

PrismCentral version 2024.3

For more information, see " Chapter 2: Hypervisors Used "

For more information, see " Cisco Virtualization Guide for Cisco On-premises Calling Applications ".

### Supported Hardware

Cisco Expressway validates virtual CPU and memory reservations at boot time. If the documented reservations are not configured
                              in the hypervisor, Expressway will display a hardware compliance warning even if the underlying host CPU exceeds the required
                              performance. This behavior is expected.

Warning

Your current hardware does not meet supported VM configuration requirements.

Cisco HCI Infrastructure, which supports Nutanix.

CE1400V is not supported as a hypervisor with Nutanix.

See Virtualization for Cisco Expressway for the current list of supported UCS Tested Reference Configurations and specs-based supported platforms.

## Virtual Machine Requirements

We strongly recommend you not to use any power management features.

Important

Make sure that the following requirements are in place:

VT is enabled in the BIOS before you install the hypervisor.

This is specific to ESXi only. The VM host “ Virtual Machine Startup/Shutdown ” setting is configured to “ Allow Virtual machines to start and stop automatically with the system ”, and the VM Expressway has been moved to the Automatic startup section.

### Do not change the MAC address of the VM

The serial number of a virtual Expressway is based on the virtual machine's MAC address. The serial number is used to validate
                              Expressway licenses and to identify Expressways that are registered to the Cisco Webex cloud. Do not change the MAC address
                              of the Expressway virtual machine when using VMware tools or similar.

### Use the VM .ova/tar.gz file for initial VM installation only

The VM Expressway is licensed using information that is generated at the time of virtual machine deployment. If the .ova or
                              NFVIS tar.gz is used to install additional instances they would be unique, new licensing information would be created, and
                              to use the new VM, new release and license keys would need to be purchased. To upgrade a VM Expressway, follow the procedure
                              under Upgrading or Downgrading an Expressway VM , using the VM.ova or tar.gz version of the Expressway software.

### Take a backup after completion

After the VM installation is complete, we recommend that you take a backup of the configuration.

Caution

Do not take VMware snapshots of Cisco Expressway systems. The process interferes with database timing and negatively impacts
                                          performance.

## How to Modify Expressway VM Capacity

Increasing the capacity of a VM-based Expressway from a smaller deployment size to a larger deployment (Small -> Medium ->
                              Large) or decreasing the capacity from a larger deployment to a smaller one (Large -> Medium -> Small) cannot be done by simply increasing or decreasing the underlying vCPUs and memory hardware resources of the VM . The correct method to upgrade or downgrade is to deploy a new VM of the required deployment size and then restore the existing
                              configuration (smaller VM for upgrade and larger VM for downgrade) onto the new one.

## Co-residency Support

For more information, see Cisco Virtualization Guide for Cisco On-premises Calling Applications .

| Note | For more information, see " Chapter 2: Hypervisors Used " For more information, see " Cisco Virtualization Guide for Cisco On-premises Calling Applications ". |
|---|---|

| Warning | Your current hardware does not meet supported VM configuration requirements. |
|---|---|

| Note | CE1400V is not supported as a hypervisor with Nutanix. |
|---|---|

| Note | We strongly recommend you not to use any power management features. |
|---|---|

| Important | Make sure that the following requirements are in place: VT is enabled in the BIOS before you install the hypervisor. This is specific to ESXi only. The VM host “ Virtual Machine Startup/Shutdown ” setting is configured to “ Allow Virtual machines to start and stop automatically with the system ”, and the VM Expressway has been moved to the Automatic startup section. |
|---|---|

| Caution | Do not take VMware snapshots of Cisco Expressway systems. The process interferes with database timing and negatively impacts
                                          performance. |
|---|---|