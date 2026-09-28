---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-installation-guide-cfin-b-1-74b755c986
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/installation/guide/cfin_b_1501_cisco-installation-and-upgrade-guide-15_0/cfin_m_1501_cisco-finesse-virtualization.html
retrieved_at: 2026-08-21T15:53:08.997960+00:00
---

Cisco Finesse Installation and Upgrade Guide, Release 15.0(1)

# Cisco Finesse Installation and Upgrade Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Cisco Finesse Virtualization

## Chapter: Cisco Finesse Virtualization

# Cisco Finesse Virtualization

## Virtualization
                        	 Hardware

Before you install the Finesse software on any server, you must address the following requirement:

If you are performing a fresh install of Finesse in any deployment, be sure to verify that the virtual machine is also fresh
                                    (no previously-installed OS is present in the VM).

If you use SATA 7200 RPM disks in your server, you must configure the datastore as RAID 10.

## Virtualization
                        	 Software

All Finesse servers run on VMs using the Unified Communications Operating System (Unified OS or UCOS). See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html .

Finesse ISO or DVD

You must install Finesse by configuring a DataStore ISO file on the virtual CD or DVD drive of the target VM.

ESXi must be
                                    				installed prior to the installation of Cisco Finesse.

## Deploying Virtual
                        	 Machines for Cisco Finesse

Perform the following steps in vSphere client to deploy the Virtual
                              		  machines:

### Before you begin

See Unified Communications VMWare Requirements .

The following software requirements apply specifically to Finesse:

For other third-party software requirements and for a list of approved UCS servers, see the server requirements and version
                                    compatibility with Unified CM sections in the C isco Unified Contact Center Enterprise Design Guide available at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/products_implementation_design_guides_list.html .

Step 1

Highlight the host or cluster
                                       			 to which you wish the VM to be deployed.

Step 2

Select File > Deploy OVF
                                             				  Template .

Step 3

Click the Deploy from File radio button and specify the
                                       			 name and location of the file you downloaded in the previous section OR click
                                       			 the Deploy from URL radio button and specify the
                                       			 complete URL in the field, then click Next .

Step 4

Enter the name of the VM machine that you are creating and the
                                       			 location where it will be created.

Step 5

Choose the type of deployment (Production or Lab).

Step 6

Choose the datastore on which you would like the VM to reside
                                       			 (ensure there is sufficient free space to accommodate the new VM), then click Next .

Step 7

Verify the deployment settings, then click Finish .

Step 8

Update boot order as per instructions as specified in the topic Changing the Boot Order of the Virtual Machine .

Step 9

Insert the Finesse disk and follow the instructions specified in
                                       			 the topic Cisco Finesse Server Installation .

## Changing the Boot
                        	 Order of the Virtual Machine

You must change the boot order of the Virtual Machine so that the
                              		  system boots off the CD/DVD drive for the install. Perform the following steps
                              		  to change the boot order of the Virtual Machine:

Step 1

In VMware vSphere Client,
                                       			 power off the virtual machine onto which you deployed the OVA .

Step 2

In the left pane of vSphere Client, right-click the name of the
                                       			 virtual machine, and select Edit Settings .

Step 3

In the Virtual Machine Properties dialog box, select
                                       			 the Options tab.

Step 4

In the Settings column, under Advanced, select Boot Options .

Step 5

Under Force BIOS Setup, check The Next Time the Virtual Machine Boots, Force Entry into
                                          				the BIOS Setup Screen check box.

Step 6

Click OK to close the Virtual Machine Properties
                                       			 dialog box.

Step 7

Power on the virtual machine (the virtual machine boots into the
                                       			 BIOS menu).

Step 8

Navigate to the Boot menu and change the boot device order so the
                                       			 CD-ROM device is listed first and the Hard Drive device is listed second.

Step 9

Save the change and exit BIOS setup.

| Note | You must install Finesse by configuring a DataStore ISO file on the virtual CD or DVD drive of the target VM. |
|---|---|

| Step 1 | Highlight the host or cluster
                                       			 to which you wish the VM to be deployed. |
|---|---|
| Step 2 | Select File > Deploy OVF
                                             				  Template . |
| Step 3 | Click the Deploy from File radio button and specify the
                                       			 name and location of the file you downloaded in the previous section OR click
                                       			 the Deploy from URL radio button and specify the
                                       			 complete URL in the field, then click Next . |
| Step 4 | Enter the name of the VM machine that you are creating and the
                                       			 location where it will be created. |
| Step 5 | Choose the type of deployment (Production or Lab). |
| Step 6 | Choose the datastore on which you would like the VM to reside
                                       			 (ensure there is sufficient free space to accommodate the new VM), then click Next . |
| Step 7 | Verify the deployment settings, then click Finish . |
| Step 8 | Update boot order as per instructions as specified in the topic Changing the Boot Order of the Virtual Machine . |
| Step 9 | Insert the Finesse disk and follow the instructions specified in
                                       			 the topic Cisco Finesse Server Installation . |

| Step 1 | In VMware vSphere Client,
                                       			 power off the virtual machine onto which you deployed the OVA . |
|---|---|
| Step 2 | In the left pane of vSphere Client, right-click the name of the
                                       			 virtual machine, and select Edit Settings . |
| Step 3 | In the Virtual Machine Properties dialog box, select
                                       			 the Options tab. |
| Step 4 | In the Settings column, under Advanced, select Boot Options . |
| Step 5 | Under Force BIOS Setup, check The Next Time the Virtual Machine Boots, Force Entry into
                                          				the BIOS Setup Screen check box. |
| Step 6 | Click OK to close the Virtual Machine Properties
                                       			 dialog box. |
| Step 7 | Power on the virtual machine (the virtual machine boots into the
                                       			 BIOS menu). |
| Step 8 | Navigate to the Boot menu and change the boot device order so the
                                       			 CD-ROM device is listed first and the Hard Drive device is listed second. |
| Step 9 | Save the change and exit BIOS setup. Note After finishing the installation, consider changing the boot order back so that the Hard Drive device is again listed before
                                                   the CD-ROM device. | Note | After finishing the installation, consider changing the boot order back so that the Hard Drive device is again listed before
                                                   the CD-ROM device. |
| Note | After finishing the installation, consider changing the boot order back so that the Hard Drive device is again listed before
                                                   the CD-ROM device. |

| Note | After finishing the installation, consider changing the boot order back so that the Hard Drive device is again listed before
                                                   the CD-ROM device. |
|---|---|