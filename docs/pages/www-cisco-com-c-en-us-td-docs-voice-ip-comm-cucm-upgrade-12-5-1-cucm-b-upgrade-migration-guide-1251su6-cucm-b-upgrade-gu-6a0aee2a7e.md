---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-upgrade-12-5-1-cucm-b-upgrade-migration-guide-1251su6-cucm-b-upgrade-gu-6a0aee2a7e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-1251su6/cucm_b_upgrade-guide-1251su2_chapter_0110.html
retrieved_at: 2026-08-17T00:09:19.963446+00:00
---

Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU6

# Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU6

Updated: July 13, 2023

Chapter: Frequently Asked Questions

## Chapter: Frequently Asked Questions

- Frequently Asked Questions

- Frequently Asked Questions

# Frequently Asked Questions

## Frequently Asked Questions

### I am upgrading from a release of Unified Communications Manager or IM and Presence Service that has different requirements for the virtual environment than the new release. What do I need to do?

Verify the requirements for the new release using the information below. After you have verified the requirements for the
                              new release, see Virtual Machine Configuration Tasks for instructions.

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

VMware vCenter is mandatory when you deploy on
                                          UC on UCS specs-based and third-party
                                          server specs-based hardware.

VM configuration virtual hardware specifications

Verify whether you need to change the virtual hardware specifications on your VM in order to upgrade to a new release of Unified Communications Manager or IM and Presence Service . For example, verify the requirements for vCPU, vRAM, vNIC adaptor type, and vDisk size, as well as other specifications.

Any changes to a VM must align with the OVA configuration. VM changes that result in an unsupported OVA configuration are
                                          not allowed. For information about VM requirements, see  Readme file with the OVA template that supports your release.

If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                      expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                      110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                      only adds additional HDD space to common partition.

You can find detailed information about the requirements for the virtualized environment by going to ../www.cisco.com/go/virtualized-collaboration , where you can:

follow the links for the Unified Communications Manager and IM and Presence Service applications to find the requirements for the release and download OVA files.

search for the topic  "Unified Communications VMware Requirements" to find information about feature support and best practices.

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
| VMware vCenter | VMware vCenter is optional when you deploy Unified Communications Manager or IM and Presence Service on Business Edition 6000/7000 appliances, or on UC on UCS tested reference configuration hardware. VMware vCenter is mandatory when you deploy on
                                          UC on UCS specs-based and third-party
                                          server specs-based hardware. |
| VM configuration virtual hardware specifications | Verify whether you need to change the virtual hardware specifications on your VM in order to upgrade to a new release of Unified Communications Manager or IM and Presence Service . For example, verify the requirements for vCPU, vRAM, vNIC adaptor type, and vDisk size, as well as other specifications. Any changes to a VM must align with the OVA configuration. VM changes that result in an unsupported OVA configuration are
                                          not allowed. For information about VM requirements, see  Readme file with the OVA template that supports your release. Note If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                      expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                      110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                      only adds additional HDD space to common partition. | Note | If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                      expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                      110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                      only adds additional HDD space to common partition. |
| Note | If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                      expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                      110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                      only adds additional HDD space to common partition. |

| Note | If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                      expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                      110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                      only adds additional HDD space to common partition. |
|---|---|