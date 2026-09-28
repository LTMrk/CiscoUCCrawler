---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-upgrade-12-5-1-cucm-b-upgrade-migration-guide-1251su6-cucm-b-upgrade-mi-731968012b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-1251su6/cucm_b_upgrade-migration-guide-1251su2_chapter_01000.html
retrieved_at: 2026-08-17T00:08:54.297728+00:00
---

Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU6

# Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU6

Updated: July 13, 2023

Chapter: Change the Virtualization Software

## Chapter: Change the Virtualization Software

# Change the Virtualization Software

Complete the procedures in this appendix only if your upgrade requires you to update your VMware.

## Virtual Machine Configuration Tasks

Use the procedures in this chapter if you need to change your virtual machine configuration to meet the requirements of the
                              software version that you are upgrading to.

### Before you begin

Verify whether you need to upgrade your virtual machine to meet the requirements of the new release. You can find the requirements
                              by going to Cisco Collaboration Virtualization and following the links for the Unified Communications Manager and IM and Presence Service applications.

Step 1

Install and Configure VMware vCenter

VMware vCenter is required only when you are migrating from Cisco Business Edition  or Tested Reference Configuration (TRC)
                                          hardware to UC on UCS specs-based or third-party
                                          server specs-based hardware. If you require VMware vCenter, install and configure it first.

Using VMware vCenter is optional when you deploy Unified Communications Manager or IM and Presence Service on UC on UCS tested reference configuration hardware.

Step 2

Upgrade vSphere ESXi

You must install a version of vSphere ESXi hypervisor that meets the requirements of the release.

We recommend that you upgrade the ESXi hypervisor before you begin an upgrade of Unified Communications Manager or IM and Presence Service ; however, if your currently installed version of these applications is not compatible with the ESXi version required for
                                          the new release, you can upgrade the ESXi version after you upgrade the Cisco applications.

Step 3

Download and Install OVA Templates

OVA files provide a set of predefined templates for virtual machine configuration. They cover items such as supported capacity
                                          levels and any required OS/VM/SAN alignment.

This procedure is optional. If you are already running Unified Communications Manager or IM and Presence Service on a virtual machine, and your deployment size has not changed, you do not need to download and install a new OVA template.
                                          If you are changing the size of your system, download and install an OVA template for the new release that is sized for your
                                          deployment.

Step 4

Change Virtual Machine Configuration Specifications

Use this procedure when you need to change the vCPU, vRAM, vDisk size, or vNIC type on your virtual machine (VM) in order
                                          to upgrade to a new release of Unified Communications Manager or IM and Presence Service .

Do this step for only for direct upgrades, which use either the Unified CM OS Admin interface or the PCD Upgrade task to perform
                                          the upgrade.

Step 5

Migrate From Single to Multi-vDisk Virtual Machine

Use this
                                          		  procedure if you are
                                          		  migrating to a larger virtual machine (VM) deployment that requires multiple
                                          		  vDisks.

### Install and Configure VMware vCenter

Using VMware vCenter is optional when you deploy Unified Communications Manager or IM and Presence Service on UC on UCS tested reference configuration hardware. VMware vCenter is mandatory when you deploy on UC on UCS specs-based
                                 and third-party server specs-based hardware.

Step 1

Install VMware vCenter.

Step 2

Set the level of detail tracked by the performance statistics. The statistics levels range from 1 to 4, with level 4 containing
                                          the most data. On a  UCS specs-based or HP/IBM specs-based deployment,
                                          you must set the statistics level to 4.

Step 3

View the data size estimates to ensure there is enough space to keep all statistics.

### Upgrade vSphere ESXi

Use the following procedure when you need to update your vSphere ESXi hypervisor in order to upgrade to a new release of Unified Communications Manager .

Step 1

Move the virtual machine that is running Unified Communications Manager off the host server using one of the following methods:

- If you have a hot standby host, use vMotion to migrate the virtual machine from one physical server to another.

- If you do not have a hot standby host, power down the virtual machine and copy it to a different location.

Step 2

Upgrade the vSphere
                                          ESXi using the upgrade procedures provided by VMware.

Step 3

Verify that the vSphere ESXi upgraded successfully.

Step 4

Move the virtual machine that is running Unified Communications Manager back to the host server using one of the following methods:

- If you have a hot standby host, use vMotion to migrate the virtual machine from one physical server to another.

- If you do not have a hot standby host, power down the virtual machine and copy it the host server.

### Download and Install OVA Templates

OVA files provide a set of predefined templates for virtual machine configuration. They cover items such as supported capacity
                                 levels and any required OS/VM/SAN alignment. For information about OVA files, search for the topic "Unified Communications
                                 Virtualization Sizing Guidelines" at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

This procedure is optional. If you are already running Unified Communications Manager or IM and Presence Service on a virtual machine, and your deployment size has not changed, you do not need to download and install a new OVA template.
                                 If you are changing the size of your system, download and install an OVA template that is sized for your deployment.

Step 1

Locate the OVA template for your release:

- For Unified Communications Manager , go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html and search for the topic "Virtualization for Cisco Unified Communications Manager."

- For IM and Presence Service , go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html and search for the topic "Virtualization for Unified CM IM and Presence."

Step 2

To download a single OVA file, click the Download File button next to that file. To download multiple OVA files, click the Add to Cart button next to each file that you want to
                                          download, then click on the Download Cart link.

Step 3

Click the Proceed with Download button on the Download Cart page.

Step 4

Read the information on the Software License Agreement page and click the Agree button.

Step 5

Click on one of the following links:

- Download Manager (requires Java)

- Non Java Download Option

Step 6

Save the file:

- If you selected Download Manager , a Select Location dialog box
                                             appears. Specify the location where you want to save the file, and
                                             click Open to save the file to your local machine.

- If you selected Non Java Download Option , click the Download link on the new browser window. Specify the location and save the
                                             file to your local machine

### Change Virtual Machine Configuration Specifications

Use the following procedure when you need to change the vCPU, vRAM, vDisk, or vNIC on your virtual machine (VM) in order
                                 to upgrade to a new release of Unified Communications Manager or IM and Presence Service .

For information about VM requirements, see the Readme
                                 		  file with the OVA template that supports your release. For details about OVA
                                 		  templates and requirements, go to www.cisco.com/go/virtualized-collaboration and search on the topic  "Implementing Virtualization Deployments."

#### Before you begin

If you need to increase the vDisk storage space, you must remove your Virtual Machine (VM) snapshots before you being. Otherwise,
                                 the increase disk size option is greyed out. See VMware Snapshots .

Step 1

Perform a
                                          			 Disaster Recovery System (DRS) backup.

Step 2

(Optional) For an upgrade
                                          			 from 9.x or earlier, if you need to increase the vDisk space to meet the space
                                          			 requirements of a refresh upgrade, install the following COP file:

ciscocm.vmware-disk-size-reallocation-<latest_version>.cop.sgn

Step 3

Shut down the
                                          			 virtual machine.

Step 4

Change the
                                          			 configuration of the virtual machine as needed:

Change the
                                                				  Guest OS version to match the requirements of the new release.

To change
                                                				  the vCPU, make the change in vSphere Client. Ensure that you change the
                                                				  reservation value to match the specifications of the new release.

To change
                                                				  the vRAM, make the change in vSphere Client. Ensure that you change the
                                                				  reservation value to match the specifications of the new release.

To
                                                				  increase the vDisk space, edit the storage  size using vSphere Client. If the virtual
                                                				  machine has two disks, expand the second one.

The new
                                                   					 space is automatically added to the common partition when you restart the
                                                   					 virtual machine.

You need
                                                               						to change the disk size changes only if you need additional space to complete
                                                               						the upgrade. The disk space requirements are specified in the Readme file for
                                                               						the OVA template.

Expanding the disk size to
                                                               						add space to the common partition will not increase the user capacity of your
                                                               						system. If you need to extend the user capacity of your system, you must
                                                               						migrate from a single-disk to a multi-disk virtual machine.

If you need to shrink the vDisk or change the vDisk quantity, you must re-install the vDisk or install a new vDisk.

In vSphere Client, verify that the
                                                			 Network Adapter is configured to use the VMXNET 3 Adapter type. If the Network Adapter is set to a different type, modify
                                                it.

For more information about making configuration changes using vSphere Client, see the user manual for the product.

Step 5

Proceed with the upgrade and then power on the
                                          			 virtual machine.

### Migrate From
                           	 Single to Multi-vDisk Virtual Machine

If you are
                                 		  migrating to a larger virtual machine (VM) deployment that requires multiple
                                 		  vDisks, perform the following procedure. After you complete this procedure, you
                                 		  must Change Virtual Machine Configuration Specifications to ensure that the specifications
                                 		  match the requirements of the release.

Step 1

Use the Disaster Recovery System (DRS) to perform a
                                          			 backup of the existing virtual machine (VM).

Step 2

Power off the
                                          			 existing VM and remove it from the network.

Step 3

Deploy a new
                                          			 VM at the correct user count using the appropriate OVA template.

Step 4

Perform a fresh installation of the same software release of IM and Presence Service or Unified Communications Manager on the new VM using the same hostname and IP address.

Step 5

Perform a DRS
                                          			 restore on the new VM.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Install and Configure VMware vCenter | VMware vCenter is required only when you are migrating from Cisco Business Edition  or Tested Reference Configuration (TRC)
                                          hardware to UC on UCS specs-based or third-party
                                          server specs-based hardware. If you require VMware vCenter, install and configure it first. Using VMware vCenter is optional when you deploy Unified Communications Manager or IM and Presence Service on UC on UCS tested reference configuration hardware. |
| Step 2 | Upgrade vSphere ESXi | You must install a version of vSphere ESXi hypervisor that meets the requirements of the release. We recommend that you upgrade the ESXi hypervisor before you begin an upgrade of Unified Communications Manager or IM and Presence Service ; however, if your currently installed version of these applications is not compatible with the ESXi version required for
                                          the new release, you can upgrade the ESXi version after you upgrade the Cisco applications. |
| Step 3 | Download and Install OVA Templates | OVA files provide a set of predefined templates for virtual machine configuration. They cover items such as supported capacity
                                          levels and any required OS/VM/SAN alignment. This procedure is optional. If you are already running Unified Communications Manager or IM and Presence Service on a virtual machine, and your deployment size has not changed, you do not need to download and install a new OVA template.
                                          If you are changing the size of your system, download and install an OVA template for the new release that is sized for your
                                          deployment. |
| Step 4 | Change Virtual Machine Configuration Specifications | Use this procedure when you need to change the vCPU, vRAM, vDisk size, or vNIC type on your virtual machine (VM) in order
                                          to upgrade to a new release of Unified Communications Manager or IM and Presence Service . Do this step for only for direct upgrades, which use either the Unified CM OS Admin interface or the PCD Upgrade task to perform
                                          the upgrade. |
| Step 5 | Migrate From Single to Multi-vDisk Virtual Machine | Use this
                                          		  procedure if you are
                                          		  migrating to a larger virtual machine (VM) deployment that requires multiple
                                          		  vDisks. |

| Step 1 | Install VMware vCenter. |
|---|---|
| Step 2 | Set the level of detail tracked by the performance statistics. The statistics levels range from 1 to 4, with level 4 containing
                                          the most data. On a  UCS specs-based or HP/IBM specs-based deployment,
                                          you must set the statistics level to 4. |
| Step 3 | View the data size estimates to ensure there is enough space to keep all statistics. |

| Step 1 | Move the virtual machine that is running Unified Communications Manager off the host server using one of the following methods: If you have a hot standby host, use vMotion to migrate the virtual machine from one physical server to another. If you do not have a hot standby host, power down the virtual machine and copy it to a different location. |
|---|---|
| Step 2 | Upgrade the vSphere
                                          ESXi using the upgrade procedures provided by VMware. |
| Step 3 | Verify that the vSphere ESXi upgraded successfully. |
| Step 4 | Move the virtual machine that is running Unified Communications Manager back to the host server using one of the following methods: If you have a hot standby host, use vMotion to migrate the virtual machine from one physical server to another. If you do not have a hot standby host, power down the virtual machine and copy it the host server. |

| Step 1 | Locate the OVA template for your release: For Unified Communications Manager , go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html and search for the topic "Virtualization for Cisco Unified Communications Manager." For IM and Presence Service , go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html and search for the topic "Virtualization for Unified CM IM and Presence." |
|---|---|
| Step 2 | To download a single OVA file, click the Download File button next to that file. To download multiple OVA files, click the Add to Cart button next to each file that you want to
                                          download, then click on the Download Cart link. |
| Step 3 | Click the Proceed with Download button on the Download Cart page. |
| Step 4 | Read the information on the Software License Agreement page and click the Agree button. |
| Step 5 | Click on one of the following links: Download Manager (requires Java) Non Java Download Option A new browser window appears. |
| Step 6 | Save the file: If you selected Download Manager , a Select Location dialog box
                                             appears. Specify the location where you want to save the file, and
                                             click Open to save the file to your local machine. If you selected Non Java Download Option , click the Download link on the new browser window. Specify the location and save the
                                             file to your local machine |

| Step 1 | Perform a
                                          			 Disaster Recovery System (DRS) backup. |
|---|---|
| Step 2 | (Optional) For an upgrade
                                          			 from 9.x or earlier, if you need to increase the vDisk space to meet the space
                                          			 requirements of a refresh upgrade, install the following COP file: ciscocm.vmware-disk-size-reallocation-<latest_version>.cop.sgn |
| Step 3 | Shut down the
                                          			 virtual machine. |
| Step 4 | Change the
                                          			 configuration of the virtual machine as needed: Change the
                                                				  Guest OS version to match the requirements of the new release. To change
                                                				  the vCPU, make the change in vSphere Client. Ensure that you change the
                                                				  reservation value to match the specifications of the new release. To change
                                                				  the vRAM, make the change in vSphere Client. Ensure that you change the
                                                				  reservation value to match the specifications of the new release. To
                                                				  increase the vDisk space, edit the storage  size using vSphere Client. If the virtual
                                                				  machine has two disks, expand the second one. The new
                                                   					 space is automatically added to the common partition when you restart the
                                                   					 virtual machine. Note You need
                                                               						to change the disk size changes only if you need additional space to complete
                                                               						the upgrade. The disk space requirements are specified in the Readme file for
                                                               						the OVA template. Expanding the disk size to
                                                               						add space to the common partition will not increase the user capacity of your
                                                               						system. If you need to extend the user capacity of your system, you must
                                                               						migrate from a single-disk to a multi-disk virtual machine. If you need to shrink the vDisk or change the vDisk quantity, you must re-install the vDisk or install a new vDisk. In vSphere Client, verify that the
                                                			 Network Adapter is configured to use the VMXNET 3 Adapter type. If the Network Adapter is set to a different type, modify
                                                it. For more information about making configuration changes using vSphere Client, see the user manual for the product. | Note | You need
                                                               						to change the disk size changes only if you need additional space to complete
                                                               						the upgrade. The disk space requirements are specified in the Readme file for
                                                               						the OVA template. Expanding the disk size to
                                                               						add space to the common partition will not increase the user capacity of your
                                                               						system. If you need to extend the user capacity of your system, you must
                                                               						migrate from a single-disk to a multi-disk virtual machine. If you need to shrink the vDisk or change the vDisk quantity, you must re-install the vDisk or install a new vDisk. |
| Note | You need
                                                               						to change the disk size changes only if you need additional space to complete
                                                               						the upgrade. The disk space requirements are specified in the Readme file for
                                                               						the OVA template. Expanding the disk size to
                                                               						add space to the common partition will not increase the user capacity of your
                                                               						system. If you need to extend the user capacity of your system, you must
                                                               						migrate from a single-disk to a multi-disk virtual machine. If you need to shrink the vDisk or change the vDisk quantity, you must re-install the vDisk or install a new vDisk. |
| Step 5 | Proceed with the upgrade and then power on the
                                          			 virtual machine. |

| Note | You need
                                                               						to change the disk size changes only if you need additional space to complete
                                                               						the upgrade. The disk space requirements are specified in the Readme file for
                                                               						the OVA template. Expanding the disk size to
                                                               						add space to the common partition will not increase the user capacity of your
                                                               						system. If you need to extend the user capacity of your system, you must
                                                               						migrate from a single-disk to a multi-disk virtual machine. If you need to shrink the vDisk or change the vDisk quantity, you must re-install the vDisk or install a new vDisk. |
|---|---|

| Step 1 | Use the Disaster Recovery System (DRS) to perform a
                                          			 backup of the existing virtual machine (VM). |
|---|---|
| Step 2 | Power off the
                                          			 existing VM and remove it from the network. |
| Step 3 | Deploy a new
                                          			 VM at the correct user count using the appropriate OVA template. |
| Step 4 | Perform a fresh installation of the same software release of IM and Presence Service or Unified Communications Manager on the new VM using the same hostname and IP address. |
| Step 5 | Perform a DRS
                                          			 restore on the new VM. |