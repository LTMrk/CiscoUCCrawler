---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-upgrade-15-cucm-b-upgrade-and-migration-guide-15-cucm-m-frequently-aske-366c9a77c9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/15/cucm_b_upgrade-and-migration-guide_15/cucm_m_frequently-asked-questions.html
retrieved_at: 2026-08-16T23:33:14.527433+00:00
---

Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 and SUs

# Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 and SUs

Updated: August 14, 2026

Chapter: Frequently Asked Questions

## Chapter: Frequently Asked Questions

- Frequently Asked Questions

- Frequently Asked Questions

# Frequently Asked Questions

## Frequently Asked Questions

### I am upgrading from a release of Unified Communications Manager or IM and Presence Service that has different requirements for the virtual environment than the new release. What do I need to do?

Verify the requirements for the new release using the information given in the table. After you have verified the requirements
                              for the new release, see Virtual Machine Configuration Tasks for instructions.

Item

Description

OVA templates

OVA files provide a set of predefined templates for virtual machine configuration. They cover items such as supported capacity
                                          levels and any required OS/VM/SAN alignment. You must use a VM configuration from the OVA file provided for the Unified Communications Manager and IM and Presence Service applications.

The correct VM configuration to use from the OVA file is based on the size of the deployment. For information about OVA files,
                                          search for the topic "Unified Communications Virtualization Sizing Guidelines" at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html .

VMware vSphere ESXi

You must install a version of vSphere ESXi hypervisor that meets the compatibility and support requirements for the release.

If you use Cisco Prime Collaboration Deployment (PCD) to perform an upgrade or migration, you must also ensure that you install
                                          vSphere ESXi with the correct license type. PCD is not compatible with all the license types of vSphere ESXi because some
                                          of these licenses do not enable required VMware APIs.

VMware vCenter

VMware vCenter is optional when you deploy Unified Communications Manager or IM and Presence Service on Business Edition 6000/7000 appliances, or on UC on UCS tested reference configuration hardware.

VMware vCenter is mandatory when you deploy on UC on UCS specs-based and third-party server specs-based hardware.

VM configuration virtual hardware specifications

Verify whether you need to change the vRAM on your VM to upgrade to a new release of Unified Communications Manager or IM and Presence Service .

Your Unified Communications Manager or IM and Presence Service Release 15 version may require more vRAM than you are currently running. Direct upgrade to IM and Presence Service Release 15 will fail if the older release versions do not have enough vRAM size.

The Unified Communications Manager or IM and Presence Service Release 15 versions may require more GB and different partitions than you are currently running. Direct upgrade to Unified Communications Manager and IM and Presence Service Release 15 will fail for all single 80GB vDisk deployments, even if you manually resized the HDD size to 110 GB.

To check vRAM and vDisk specifications before upgrade, either refer to the Readme of the base OVA for Release 15 or use the
                                          QuoteCollab tool.

For more references, see:

Virtual Machine Configuration Tasks to update your VMware.

To update the vDisk, either backup or restore your Release 12.5 or 14 and SU versions to a new VMware with vDisk installed
                                                as 110GB where Direst upgrade will be successful. Or use either PCD Migration or Fresh Install with Data Import Task migrations
                                                to move to a new node deployed with the Unified CM Release 15 OVA template.

You can find detailed information about the requirements for the virtualized environment by going to ../www.cisco.com/go/virtualized-collaboration , where you can:

follow the links for the Unified Communications Manager and IM and Presence Service applications to find the requirements for the release and download OVA files.

search for the topic "Unified Communications VMware Requirements" to find information about feature support and best practices.

### I want to move to a different VM size as part of the upgrade. Can I edit the VM configuration specifications?

Before you edit the VM configuration specifications, review the OVA ReadMe file to find the specific requirements for the
                              release that you are upgrading to. OVA files provide a set of predefined templates for virtual machine configuration. They
                              cover items such as supported capacity levels and any required OS/VM/SAN alignment. The correct VM configuration to use from
                              the OVA file is based on the size of the deployment.

For information about OVA files, search for the topic "Unified Communications Virtualization Sizing Guidelines" at ../www.cisco.com/go/virtualized-collaboration .

To obtain an OVA file, see Download and Install OVA Templates .

### I have applications that use an administrative XML (AXL) interface to access and modify Unified Communications Manager information. Will my application continue to work after I upgrade to Unified Communications Manager ?

For information about upgrading your AXL applications, see https://developer.cisco.com/site/axl/learn/how-to/upgrade-to-a-new-axl-schema.gsp . To see a list of the AXL operations supported for your release, refer to https://developer.cisco.com/site/axl/documents/operations-by-release/ .

| Item | Description |
|---|---|
| OVA templates | OVA files provide a set of predefined templates for virtual machine configuration. They cover items such as supported capacity
                                          levels and any required OS/VM/SAN alignment. You must use a VM configuration from the OVA file provided for the Unified Communications Manager and IM and Presence Service applications. The correct VM configuration to use from the OVA file is based on the size of the deployment. For information about OVA files,
                                          search for the topic "Unified Communications Virtualization Sizing Guidelines" at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html . |
| VMware vSphere ESXi | You must install a version of vSphere ESXi hypervisor that meets the compatibility and support requirements for the release. If you use Cisco Prime Collaboration Deployment (PCD) to perform an upgrade or migration, you must also ensure that you install
                                          vSphere ESXi with the correct license type. PCD is not compatible with all the license types of vSphere ESXi because some
                                          of these licenses do not enable required VMware APIs. |
| VMware vCenter | VMware vCenter is optional when you deploy Unified Communications Manager or IM and Presence Service on Business Edition 6000/7000 appliances, or on UC on UCS tested reference configuration hardware. VMware vCenter is mandatory when you deploy on UC on UCS specs-based and third-party server specs-based hardware. |
| VM configuration virtual hardware specifications | Verify whether you need to change the vRAM on your VM to upgrade to a new release of Unified Communications Manager or IM and Presence Service . Your Unified Communications Manager or IM and Presence Service Release 15 version may require more vRAM than you are currently running. Direct upgrade to IM and Presence Service Release 15 will fail if the older release versions do not have enough vRAM size. The Unified Communications Manager or IM and Presence Service Release 15 versions may require more GB and different partitions than you are currently running. Direct upgrade to Unified Communications Manager and IM and Presence Service Release 15 will fail for all single 80GB vDisk deployments, even if you manually resized the HDD size to 110 GB. To check vRAM and vDisk specifications before upgrade, either refer to the Readme of the base OVA for Release 15 or use the
                                          QuoteCollab tool. For more references, see: Virtual Machine Configuration Tasks to update your VMware. To update the vDisk, either backup or restore your Release 12.5 or 14 and SU versions to a new VMware with vDisk installed
                                                as 110GB where Direst upgrade will be successful. Or use either PCD Migration or Fresh Install with Data Import Task migrations
                                                to move to a new node deployed with the Unified CM Release 15 OVA template. |