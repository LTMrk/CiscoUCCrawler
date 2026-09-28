---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-install-15-cucm-b-install-guide-cucm-imp-15-cucm-m-preinstallation-task-efa9db2e46
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/install/15/cucm_b_install-guide-cucm-imp-15/cucm_m_preinstallation-tasks_su4.html
retrieved_at: 2026-08-16T23:46:50.765936+00:00
---

Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 and SUs

# Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 and SUs

Updated: March 17, 2026

Chapter: Preinstallation Tasks

## Chapter: Preinstallation Tasks

# Preinstallation Tasks

## Preinstall Tasks for Unified Communications Manager on VMware vSphere ESXi

Step 1

Planning the Installation

Review the Planning chapter. Make sure to review the following:

Decide on your Unified CM and IM and Presence Service cluster Topology.

Decide on the Hypervisor version that you want and its supported hardware.

Pick an installation method supported by Hypervisor.

Step 2

Required Installation Information

Review the installation requirements and record the configuration settings for each server that you plan to install.

Step 3

Create virtual machines.

Get base OVA. An example OVA file name is: cucm_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova.

From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                            is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                            a new Virtual Machine, use the following steps:

Navigate to https://www.cisco.com/security/pki/codesign/ .

Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page.

Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 .

Step 4

Select a VM configuration from the Base OVA and deploy using the OVA.

For more information, refer to the technical documentation on Broadcom.com .

Step 5

Mount the installation ISO file.

Place the installation ISO file in a location where the virtual machine can access it and edit the virtual machine's DVD drive
                                          to map to the file. Select the option to mount the DVD drive when you power on the virtual machine.

When you power on the virtual machine, it mounts the ISO file and start the installation process. Do not begin the installation
                                          process until you have completed all the steps in this procedure.

For more information, refer to the technical documentation on Broadcom.com .

## Preinstall Tasks for Cisco Unified Communications Manager on Cisco NFVIS-for-UC

Step 1

Planning the Installation

Decide on your Unified CM and IM and Presence Service cluster Topology.

Decide on the Hypervisor version that you want and its supported hardware.

Pick an installation method supported by Hypervisor.

Step 2

Required Installation Information

Review the installation requirements and record the configuration settings for each server that you plan to install.

Step 3

Upload the ISO image and OVA.

An example OVA file name is: cucm_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova.

Upload the OVA as a profile and the ISO as an image together. This process creates a separate profile for each VM configuration
                                          and a single image for the bootable ISO. For more information, refer to the 'Image Registration for CUCM Applications' section
                                          in the Cisco Enterprise Network Function Virtualization Infrastructure Software Configuration Guide .

Step 4

Deploy a VM.

Ensure that an OVA and ISO image is already uploaded.

Navigate to Configuration > Deploy .

Select OTHER as the option when creating virtual machines for your application type.

Connect to the virtual network and assign the Image/Profile (depending on the deployment size that you prefer), and click Deploy .

Open the VM console via Configuration > Virtual Machine > Manage .

Use the console to complete the ISO installation process.

## Preinstall Tasks for Cisco Unified Communications Manager on Nutanix AHV

Step 1

Plan the installation

Decide on the Unified CM and IM and Presence Service cluster Topology.

Decide on the Hypervisor version that you want and its supported hardware and hyperconvergence software version.

Pick an installation method supported by Hypervisor.

Step 2

Required Installation Information

Review the installation requirements and record the configuration settings for each server that you plan to install.

Step 3

Create virtual machines in Nutanix AHV and select an OVA per each VM configuration from the Base OVA and deploy using the
                                       OVA.

An example OVA file name for a large size deployment is: cucm_15_large_ahv_v1.0.sha512.ova .

Download the Unified CM .ova files based on the required configuration from the Software Download page .

Upload the Unified CM .ova files (downloaded) onto the Nutanix cluster using Prism Central.

Download the desired Unified CM bootable .iso image version from the Software Download page and upload the image to the Nutanix
                                                cluster.

Creating Unified CM Publisher and Subscriber VMs using the .ova files.

Update Unified CM VMs to mount CD-ROM with the Unified CM image.

## Preinstall Tasks for IM and Presence Service on VMware vSphere ESXi

Step 1

Planning the Installation

Review the Planning chapter. Make sure to review the following:

Decide on your IM and Presence Service and Unified CM cluster Topology.

Decide on the Hypervisor that you want and its supported hardware.

Pick an installation method supported by Hypervisor.

Step 2

Supported Version

Make sure that the Unified Communications Manager and IM and Presence Service software versions are compatible.

Step 3

Required Installation Information

Gather all the information you need to complete the installation and configuration of the IM and Presence Service.

Step 4

Create your virtual machines.

For every node in your cluster, create virtual machines using the Virtual Server Template (OVA file) that is recommended for
                                          your release. An example OVA file name is: imp_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova .

From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                      is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                      a new Virtual Machine, use the following steps:

Navigate to https://www.cisco.com/security/pki/codesign/ .

Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page.

Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 .

Different OVA files are available; choose the correct OVA file based on the environment in which you are deploying Unified
                                          Communications Manager. See Virtualization Requirements .

Step 5

Verify network connectivity.

Make sure that each IM and Presence Service server has network access to the Unified Communications Manager publisher server.
                                          Ping the Unified Communications Manager publisher node from the other IM and Presence Service servers.

## Preinstall Tasks for IM and Presence Service on Cisco NFVIS-for-UC

Step 1

Planning the Installation

Decide on your IM and Presence Service and Unified CM cluster Topology.

Decide on the Hypervisor version that you want and its supported hardware.

Pick an installation method supported by Hypervisor.

Step 2

Required Installation Information

Review the installation requirements and record the configuration settings for each server that you plan to install.

Step 3

Upload the OVA and ISO image.

Upload the OVA (an example OVA file name is: imp_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova ) as a profile and the ISO as an image together. This process creates a separate profile for each VM configuration and a single
                                          image for the bootable ISO. For more information, refer to the Cisco Enterprise Network Function Virtualization Infrastructure Software Configuration Guide .

Step 4

Deploy a VM.

Ensure that an OVA and ISO image is already uploaded.

Navigate to Configuration > Deploy .

Select OTHER as the option when creating virtual machines for your application type.

Connect to the virtual network and assign the Image/Profile (depending on the deployment size that you prefer), and click Deploy .

Open the VM console via Configuration > Virtual Machine > Manage .

Use the console to complete the ISO installation process.

## Preinstall Tasks for IM and Presence Service on Nutanix AHV

Step 1

Plan the installation

Decide on the IM and Presence Service and Unified CM cluster Topology.

Decide on the Hypervisor version that you want and its supported hardware and hyperconvergence software version.

Pick an installation method supported by Hypervisor.

Step 2

Required Installation Information

Review the installation requirements and record the configuration settings for each server that you plan to install.

Step 3

Create virtual machines in Nutanix AHV and select an OVA per each VM configuration from the Base OVA and deploy using the
                                       OVA.

An example OVA file name for a medium sized deployment is: imp_15_medium_ahv_v1.0.sha512.ova .

Download the IMP.ova files based on the required configuration from the Software Download page.

Upload the IMP.ova files (downloaded) onto the Nutanix cluster using Prism Central.

Download the desired IMP bootable .iso image version from the Software Download page and upload the image to the Nutanix cluster.

Creating IM and Presence Service Publisher and Subscriber VMs using the .ova files.

UpdateIM and Presence Service VMs to mount CD-ROM with the IM and Presence Service image.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Planning the Installation | Review the Planning chapter. Make sure to review the following: Decide on your Unified CM and IM and Presence Service cluster Topology. Decide on the Hypervisor version that you want and its supported hardware. Pick an installation method supported by Hypervisor. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configuration settings for each server that you plan to install. |
| Step 3 | Create virtual machines. | Get base OVA. An example OVA file name is: cucm_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova. Note From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                            is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                            a new Virtual Machine, use the following steps: Navigate to https://www.cisco.com/security/pki/codesign/ . Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page. Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 . | Note | From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                            is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                            a new Virtual Machine, use the following steps: Navigate to https://www.cisco.com/security/pki/codesign/ . Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page. Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 . |
| Note | From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                            is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                            a new Virtual Machine, use the following steps: Navigate to https://www.cisco.com/security/pki/codesign/ . Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page. Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 . |
| Step 4 | Select a VM configuration from the Base OVA and deploy using the OVA. | For more information, refer to the technical documentation on Broadcom.com . |
| Step 5 | Mount the installation ISO file. | Place the installation ISO file in a location where the virtual machine can access it and edit the virtual machine's DVD drive
                                          to map to the file. Select the option to mount the DVD drive when you power on the virtual machine. When you power on the virtual machine, it mounts the ISO file and start the installation process. Do not begin the installation
                                          process until you have completed all the steps in this procedure. For more information, refer to the technical documentation on Broadcom.com . |

| Note | From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                            is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                            a new Virtual Machine, use the following steps: Navigate to https://www.cisco.com/security/pki/codesign/ . Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page. Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Planning the Installation | Decide on your Unified CM and IM and Presence Service cluster Topology. Decide on the Hypervisor version that you want and its supported hardware. Pick an installation method supported by Hypervisor. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configuration settings for each server that you plan to install. |
| Step 3 | Upload the ISO image and OVA. | An example OVA file name is: cucm_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova. Upload the OVA as a profile and the ISO as an image together. This process creates a separate profile for each VM configuration
                                          and a single image for the bootable ISO. For more information, refer to the 'Image Registration for CUCM Applications' section
                                          in the Cisco Enterprise Network Function Virtualization Infrastructure Software Configuration Guide . |
| Step 4 | Deploy a VM. | Ensure that an OVA and ISO image is already uploaded. Navigate to Configuration > Deploy . Select OTHER as the option when creating virtual machines for your application type. Connect to the virtual network and assign the Image/Profile (depending on the deployment size that you prefer), and click Deploy . Open the VM console via Configuration > Virtual Machine > Manage . Use the console to complete the ISO installation process. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Plan the installation | Decide on the Unified CM and IM and Presence Service cluster Topology. Decide on the Hypervisor version that you want and its supported hardware and hyperconvergence software version. Pick an installation method supported by Hypervisor. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configuration settings for each server that you plan to install. |
| Step 3 | Create virtual machines in Nutanix AHV and select an OVA per each VM configuration from the Base OVA and deploy using the
                                       OVA. | An example OVA file name for a large size deployment is: cucm_15_large_ahv_v1.0.sha512.ova . Download the Unified CM .ova files based on the required configuration from the Software Download page . Upload the Unified CM .ova files (downloaded) onto the Nutanix cluster using Prism Central. Download the desired Unified CM bootable .iso image version from the Software Download page and upload the image to the Nutanix
                                                cluster. Creating Unified CM Publisher and Subscriber VMs using the .ova files. Update Unified CM VMs to mount CD-ROM with the Unified CM image. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Planning the Installation | Review the Planning chapter. Make sure to review the following: Decide on your IM and Presence Service and Unified CM cluster Topology. Decide on the Hypervisor that you want and its supported hardware. Pick an installation method supported by Hypervisor. |
| Step 2 | Supported Version | Make sure that the Unified Communications Manager and IM and Presence Service software versions are compatible. |
| Step 3 | Required Installation Information | Gather all the information you need to complete the installation and configuration of the IM and Presence Service. |
| Step 4 | Create your virtual machines. | For every node in your cluster, create virtual machines using the Virtual Server Template (OVA file) that is recommended for
                                          your release. An example OVA file name is: imp_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova . Note From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                      is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                      a new Virtual Machine, use the following steps: Navigate to https://www.cisco.com/security/pki/codesign/ . Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page. Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 . Different OVA files are available; choose the correct OVA file based on the environment in which you are deploying Unified
                                          Communications Manager. See Virtualization Requirements . | Note | From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                      is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                      a new Virtual Machine, use the following steps: Navigate to https://www.cisco.com/security/pki/codesign/ . Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page. Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 . |
| Note | From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                      is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                      a new Virtual Machine, use the following steps: Navigate to https://www.cisco.com/security/pki/codesign/ . Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page. Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 . |
| Step 5 | Verify network connectivity. | Make sure that each IM and Presence Service server has network access to the Unified Communications Manager publisher server.
                                          Ping the Unified Communications Manager publisher node from the other IM and Presence Service servers. |

| Note | From Release 15 onwards, the OVA template is signed with sha512 using Cisco authenticated certificates to ensure that there
                                                      is no tampering of the OVA file. To avoid seeing the "The certificate is not trusted" warning when using the OVA to create
                                                      a new Virtual Machine, use the following steps: Navigate to https://www.cisco.com/security/pki/codesign/ . Download the Issuer Chain PKCS7 (PEM) file (right-click and choose Save link as ) for the selected certificate that is used to sign the OVA file. The signing certificate used is documented in the File Information of the downloaded OVA page. Add these certificates to vCenter by following the steps in the 'Resolution' section at: https://kb.vmware.com/s/article/84240 . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Planning the Installation | Decide on your IM and Presence Service and Unified CM cluster Topology. Decide on the Hypervisor version that you want and its supported hardware. Pick an installation method supported by Hypervisor. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configuration settings for each server that you plan to install. |
| Step 3 | Upload the OVA and ISO image. | Upload the OVA (an example OVA file name is: imp_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova ) as a profile and the ISO as an image together. This process creates a separate profile for each VM configuration and a single
                                          image for the bootable ISO. For more information, refer to the Cisco Enterprise Network Function Virtualization Infrastructure Software Configuration Guide . |
| Step 4 | Deploy a VM. | Ensure that an OVA and ISO image is already uploaded. Navigate to Configuration > Deploy . Select OTHER as the option when creating virtual machines for your application type. Connect to the virtual network and assign the Image/Profile (depending on the deployment size that you prefer), and click Deploy . Open the VM console via Configuration > Virtual Machine > Manage . Use the console to complete the ISO installation process. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Plan the installation | Decide on the IM and Presence Service and Unified CM cluster Topology. Decide on the Hypervisor version that you want and its supported hardware and hyperconvergence software version. Pick an installation method supported by Hypervisor. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configuration settings for each server that you plan to install. |
| Step 3 | Create virtual machines in Nutanix AHV and select an OVA per each VM configuration from the Base OVA and deploy using the
                                       OVA. | An example OVA file name for a medium sized deployment is: imp_15_medium_ahv_v1.0.sha512.ova . Download the IMP.ova files based on the required configuration from the Software Download page. Upload the IMP.ova files (downloaded) onto the Nutanix cluster using Prism Central. Download the desired IMP bootable .iso image version from the Software Download page and upload the image to the Nutanix cluster. Creating IM and Presence Service Publisher and Subscriber VMs using the .ova files. UpdateIM and Presence Service VMs to mount CD-ROM with the IM and Presence Service image. |