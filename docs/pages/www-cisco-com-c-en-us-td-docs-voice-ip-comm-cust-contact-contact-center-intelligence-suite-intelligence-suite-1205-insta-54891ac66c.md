---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1205-insta-54891ac66c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1205/install/guide/cuic_b_installation-and-upgrade-guide-1205/cuic_b_installation-and-upgrade-guide-1205_chapter_0111.html
retrieved_at: 2026-08-21T04:36:39.814450+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.5(1)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.5(1)

Updated: January 31, 2020

Chapter: Member Configuration

## Chapter: Member Configuration

- Member Configuration

- Installation and                              	 Configuration for Member Node

- Complete                              	 Configuration for Member Node

# Member Configuration

## Installation and
                        	 Configuration for Member Node

To add a member node in a Live Data only deployment, see Live Data Standalone Installation , in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

To add a member node in a IdS only deployment, see Install Cisco Identity Service Standalone Deployment , in the Cisco Unified Contact Center Enterprise Features Guide https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

## Complete
                        	 Configuration for Member Node

Step 1

Install the
                                       			 member node following the steps in Preparation
                                          				for Unified Intelligence Center Installation on a Virtual Machine , under
                                       			 sections:

Deploy Unified
                                                   						Intelligence Center Open Virtualization Format/Open Virtual Appliance
                                                   						(OVF/OVA)Template

Specify Location of
                                                   						Unified Intelligence Center Installable, on page 9

Install Cisco Unified
                                                   						Intelligence Center on Virtual Machine, on page 10

Step 2

At the First
                                          				Node Configuration Screen , select No.

The First Node
                                          				Configuration Warning screen opens. This screen advises you that you must
                                          				configure the server on the first node before you can proceed. You completed
                                          				this configuration in Chapter
                                             				  4 .

Step 3

Select OK at the screen.

Step 4

In the Network Connectivity Test Configuration screen, you
                                       			 can verify the connection of this node to the first node (the Controller).

Step 5

In the First
                                          				Node Access Configuration screen, enter connection values for the
                                          				first node (the Controller) :

Host Name of
                                                					 the Controller

IP Address of
                                                					 the Controller

Security
                                             				  Password (enter and confirm)

Select OK to open the SMTP Host Configuration screen.

Step 6

In the SMTP
                                          				Host Configuration screen, select whether you want to configure an
                                       			 SMTP host to receive platform-level emails; for example, emails about
                                       			 certificate expiration. This field is optional. You configure email for report
                                       			 scheduling in the Administration console.

If

Then

You
                                                      							 want to configure an SMTP Host.

Select Yes to open the second SMTP screen.

Proceed to Step 7.

You
                                                      							 do not want to configure an SMTP Host.

Select No to open the Platform Configuration Confirmation
                                                      							 screen.

Proceed to Step 8.

Step 7

In the second SMTP
                                          				Host Configuration screen:

Enter the
                                             				  hostname or IP address for the SMTP server.

Select OK to open the Platform Configuration Confirmation screen.

Step 8

In
                                       			 the Platform
                                          				Configuration Confirmation screen:

If

Then

You
                                                      							 want to proceed.

Select OK .

The installation begins.

You want to revisit screens to modify the configuration.

Select Back .

| Note | All configured
                                       		  nodes in a cluster must be up and running before you install a new Member node. |
|---|---|

| Note | To add a member node in a Live Data only deployment, see Live Data Standalone Installation , in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
|---|---|

| Note | To add a member node in a IdS only deployment, see Install Cisco Identity Service Standalone Deployment , in the Cisco Unified Contact Center Enterprise Features Guide https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html . |
|---|---|

| Step 1 | Install the
                                       			 member node following the steps in Preparation
                                          				for Unified Intelligence Center Installation on a Virtual Machine , under
                                       			 sections: Deploy Unified
                                                   						Intelligence Center Open Virtualization Format/Open Virtual Appliance
                                                   						(OVF/OVA)Template Specify Location of
                                                   						Unified Intelligence Center Installable, on page 9 Install Cisco Unified
                                                   						Intelligence Center on Virtual Machine, on page 10 |
|---|---|
| Step 2 | At the First
                                          				Node Configuration Screen , select No. The First Node
                                          				Configuration Warning screen opens. This screen advises you that you must
                                          				configure the server on the first node before you can proceed. You completed
                                          				this configuration in Chapter
                                             				  4 . |
| Step 3 | Select OK at the screen. |
| Step 4 | In the Network Connectivity Test Configuration screen, you
                                       			 can verify the connection of this node to the first node (the Controller). Note The Network Connectivity Test Configuration screen
                                                   				refers to the first node as the publisher , in reference to its role in database replication.
                                                   				The first node publishes or replicates, the databases to the Member
                                                   				nodes, which are referred to as subscribers of the database replication. Select No to open the First Node Access Configuration
                                                   				screen. | Note | The Network Connectivity Test Configuration screen
                                                   				refers to the first node as the publisher , in reference to its role in database replication.
                                                   				The first node publishes or replicates, the databases to the Member
                                                   				nodes, which are referred to as subscribers of the database replication. Select No to open the First Node Access Configuration
                                                   				screen. |
| Note | The Network Connectivity Test Configuration screen
                                                   				refers to the first node as the publisher , in reference to its role in database replication.
                                                   				The first node publishes or replicates, the databases to the Member
                                                   				nodes, which are referred to as subscribers of the database replication. Select No to open the First Node Access Configuration
                                                   				screen. |
| Step 5 | In the First
                                          				Node Access Configuration screen, enter connection values for the
                                          				first node (the Controller) : Host Name of
                                                					 the Controller IP Address of
                                                					 the Controller Security
                                             				  Password (enter and confirm) Select OK to open the SMTP Host Configuration screen. |
| Step 6 | In the SMTP
                                          				Host Configuration screen, select whether you want to configure an
                                       			 SMTP host to receive platform-level emails; for example, emails about
                                       			 certificate expiration. This field is optional. You configure email for report
                                       			 scheduling in the Administration console. If Then You
                                                      							 want to configure an SMTP Host. Select Yes to open the second SMTP screen. Proceed to Step 7. You
                                                      							 do not want to configure an SMTP Host. Select No to open the Platform Configuration Confirmation
                                                      							 screen. Proceed to Step 8. | If | Then | You
                                                      							 want to configure an SMTP Host. | Select Yes to open the second SMTP screen. Proceed to Step 7. | You
                                                      							 do not want to configure an SMTP Host. | Select No to open the Platform Configuration Confirmation
                                                      							 screen. Proceed to Step 8. |
| If | Then |
| You
                                                      							 want to configure an SMTP Host. | Select Yes to open the second SMTP screen. Proceed to Step 7. |
| You
                                                      							 do not want to configure an SMTP Host. | Select No to open the Platform Configuration Confirmation
                                                      							 screen. Proceed to Step 8. |
| Step 7 | In the second SMTP
                                          				Host Configuration screen: Enter the
                                             				  hostname or IP address for the SMTP server. Select OK to open the Platform Configuration Confirmation screen. |
| Step 8 | In
                                       			 the Platform
                                          				Configuration Confirmation screen: If Then You
                                                      							 want to proceed. Select OK . The installation begins. You want to revisit screens to modify the configuration. Select Back . | If | Then | You
                                                      							 want to proceed. | Select OK . The installation begins. | You want to revisit screens to modify the configuration. | Select Back . |
| If | Then |
| You
                                                      							 want to proceed. | Select OK . The installation begins. |
| You want to revisit screens to modify the configuration. | Select Back . |

| Note | The Network Connectivity Test Configuration screen
                                                   				refers to the first node as the publisher , in reference to its role in database replication.
                                                   				The first node publishes or replicates, the databases to the Member
                                                   				nodes, which are referred to as subscribers of the database replication. Select No to open the First Node Access Configuration
                                                   				screen. |
|---|---|

| If | Then |
|---|---|
| You
                                                      							 want to configure an SMTP Host. | Select Yes to open the second SMTP screen. Proceed to Step 7. |
| You
                                                      							 do not want to configure an SMTP Host. | Select No to open the Platform Configuration Confirmation
                                                      							 screen. Proceed to Step 8. |

| If | Then |
|---|---|
| You
                                                      							 want to proceed. | Select OK . The installation begins. |
| You want to revisit screens to modify the configuration. | Select Back . |