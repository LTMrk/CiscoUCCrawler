---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-c7a866e562
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_150_install_upgrade_guide/migrate_from_co-resident_deployment_to_standalone_deployment.html
retrieved_at: 2026-08-16T19:57:27.170502+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Migrate from
	 Co-resident Deployment to Standalone Deployment

## Chapter: Migrate from
	 Co-resident Deployment to Standalone Deployment

# Migrate from
                     	 Co-resident Deployment to Standalone Deployment

## Migrate from Co-resident to Standalone Deployments

If your solution exceeds the configuration limits of 2000 Agent Reference Design, use a Reference Design with higher limits
                              and replace the co-resident deployment of CUIC with a standalone deployment of CUIC, Live Data, and IdS. A standalone deployment
                              allows higher capacity and increased reporting end users. You cannot convert the existing co-resident server to a standalone
                              server.

You can export the CUIC reports from the co-resident deployment and import them into the new standalone CUIC.

For a new standalone deployment, you must perform fresh install of the following servers, using the method outlined below:

Sequence

Task

1

2

Install Cisco Unified Intelligence Center Standalone (4000, 8000, 12000 Agent Deployment). See Installation and Upgrade Guide for Cisco Unified Intelligence Center at http://www.cisco.com/en/US/products/ps9755/prod_installation_guides_list.html .

3

Install Live Data. See Live Data Standalone Installation .

4

Install the Identity Service. See Install Cisco Identity Service Standalone Deployment .

### Set up the System
                           	 Inventory for Standalone Deployment

Step 1

In Unified CCE
                                          			 Administration, navigate to System > Deployment .

Step 2

Add the new
                                          			 machine to the System Inventory:

Select the coresident machine to remove. Click Delete .

Click New . The Add Machine popup window opens.

The Add Machine popup window opens.

From the Type drop-down menu, select the following machine
                                                				  type:

Unified
                                                   					 Intelligence Center Publisher.

In the Hostname field, enter the FQDN, hostname, or IP
                                                				  address of the machine.

The system
                                                   					 attempts to convert the value you enter to FQDN.

Enter the
                                                				  machine's Administration credentials.

Click Save .

The machine
                                             				and its related Subscriber or Secondary machine are added to the System
                                             				Inventory.

#### What to do next

If you remove a component from your deployment, delete it from your
                                 		  System Inventory. If you add the component again, or add more components, add
                                 		  those components to the System Inventory.

## Upgrading Live Data for 24k Deployment Type

Step 1

In the Virtual Machine:

Click the Edit virtual machine settings option in VM Hardware on the ESXi/ESX host.

Increase the CPU cores to 12 and CPU reservation to 24000MHz.

Increase the Memory is 36GB and Memory reservation to 36864MB.

For details about how to edit the VM Hardware settings, see the VMware hardware documentation.

Step 2

Upgrade live data.

The System Memory and CPU should be increased before upgrade. If the upgrade is applied before increasing the system memory,
                                                      use the CLI command in step 3 to set the memory profile parameters correctly.

Step 3

Run the set live-data memory profile CLI command to set the parameters correctly.

This CLI command updates the memory parameters only if the total RAM on the VM is at least 36 GB. If the RAM is lesser than
                                                      36 GB, the CLI resets the memory parameters to default values.

| Note | You can export the CUIC reports from the co-resident deployment and import them into the new standalone CUIC. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Set up the System Inventory for Standalone Deployment |
| 2 | Install Cisco Unified Intelligence Center Standalone (4000, 8000, 12000 Agent Deployment). See Installation and Upgrade Guide for Cisco Unified Intelligence Center at http://www.cisco.com/en/US/products/ps9755/prod_installation_guides_list.html . |
| 3 | Install Live Data. See Live Data Standalone Installation . |
| 4 | Install the Identity Service. See Install Cisco Identity Service Standalone Deployment . |

| Step 1 | In Unified CCE
                                          			 Administration, navigate to System > Deployment . |
|---|---|
| Step 2 | Add the new
                                          			 machine to the System Inventory: Select the coresident machine to remove. Click Delete . Click New . The Add Machine popup window opens. The Add Machine popup window opens. From the Type drop-down menu, select the following machine
                                                				  type: Unified
                                                   					 Intelligence Center Publisher. In the Hostname field, enter the FQDN, hostname, or IP
                                                				  address of the machine. The system
                                                   					 attempts to convert the value you enter to FQDN. Enter the
                                                				  machine's Administration credentials. Click Save . The machine
                                             				and its related Subscriber or Secondary machine are added to the System
                                             				Inventory. |

| Step 1 | In the Virtual Machine: Click the Edit virtual machine settings option in VM Hardware on the ESXi/ESX host. Increase the CPU cores to 12 and CPU reservation to 24000MHz. Increase the Memory is 36GB and Memory reservation to 36864MB. For details about how to edit the VM Hardware settings, see the VMware hardware documentation. |
|---|---|
| Step 2 | Upgrade live data. Note The System Memory and CPU should be increased before upgrade. If the upgrade is applied before increasing the system memory,
                                                      use the CLI command in step 3 to set the memory profile parameters correctly. | Note | The System Memory and CPU should be increased before upgrade. If the upgrade is applied before increasing the system memory,
                                                      use the CLI command in step 3 to set the memory profile parameters correctly. |
| Note | The System Memory and CPU should be increased before upgrade. If the upgrade is applied before increasing the system memory,
                                                      use the CLI command in step 3 to set the memory profile parameters correctly. |
| Step 3 | Run the set live-data memory profile CLI command to set the parameters correctly. Note This CLI command updates the memory parameters only if the total RAM on the VM is at least 36 GB. If the RAM is lesser than
                                                      36 GB, the CLI resets the memory parameters to default values. | Note | This CLI command updates the memory parameters only if the total RAM on the VM is at least 36 GB. If the RAM is lesser than
                                                      36 GB, the CLI resets the memory parameters to default values. |
| Note | This CLI command updates the memory parameters only if the total RAM on the VM is at least 36 GB. If the RAM is lesser than
                                                      36 GB, the CLI resets the memory parameters to default values. |

| Note | The System Memory and CPU should be increased before upgrade. If the upgrade is applied before increasing the system memory,
                                                      use the CLI command in step 3 to set the memory profile parameters correctly. |
|---|---|

| Note | This CLI command updates the memory parameters only if the total RAM on the VM is at least 36 GB. If the RAM is lesser than
                                                      36 GB, the CLI resets the memory parameters to default values. |
|---|---|