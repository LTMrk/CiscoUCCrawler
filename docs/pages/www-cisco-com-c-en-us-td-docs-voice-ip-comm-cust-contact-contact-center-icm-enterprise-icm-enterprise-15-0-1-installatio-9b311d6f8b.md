---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-9b311d6f8b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_stagingguide_release_15_0_1/ucce_m_1261_moving-the-cisco-root.html
retrieved_at: 2026-08-16T19:59:17.161360+00:00
---

Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1)

# Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1)

Updated: March 24, 2025

Chapter: Moving the Cisco Root OU

## Chapter: Moving the Cisco Root OU

# Moving the Cisco Root OU

## Introduction

This section
                              		  describes the instructions to move the Cisco Root OU safely from one OU to
                              		  another within the same domain. The procedure involves moving the OU in which
                              		  ICM is installed to another (created or existing) OU, and then moving the
                              		  Unified ICM into the destination OU.

Warning

Moving the Cisco Root OU is only supported if the OU is moved within the same domain. Transferring an OU from one domain to
                                          another is not supported.

### Definitions

This section defines the terms used in the movement of Cisco Root
                                 OU:

#### Cisco Root
                              	 OU

The OU contains all
                                 		Unified ICM created domain resources. The OU defines the permissions for all
                                 		Unified ICM instances. When you use this tool, you determine which uses a Cisco
                                 		Root OU named "Cisco_ICM" . Only
                                 		one Cisco Root OU exists in each domain.

#### Domain
                              	 Manager

A tool for creating
                                 		all Cisco OUs along with their associated groups and permissions. This tool
                                 		helps you to determine which users in your corporate domain have access rights
                                 		to perform Unified ICM-related tasks.

### Requirements and
                           	 Prerequisites

The instructions in
                                 		  this document are subject to the following requirements and prerequisites:

The OU might
                                       				only be transferred to a new location within the same domain.

Stop all Unified
                                       				ICM Services and applications before following these instructions. For duplexed
                                       				systems, stop both the primary and secondary systems.

Obtain and
                                       				record the Instance Number of each Unified ICM instance on the system.

### Preparatory
                           	 Steps

Before moving the
                                 		  OU:

Stop all Unified
                                       				ICM Services before removing the OU.

Reset the
                                       				permissions for the users using the User List Tool.

Run Web
                                             					 Setup to edit each component of each instance to reset the service account to
                                             					 the new OU.

Start all
                                             					 Unified ICM Services.

Run the Configuration Manager tool.

Run the User List tool and re-establish the permissions for
                                             					 individual users to ensure all the users in the User List Tools have the
                                             					 correct permissions.

### Transfer Cisco Root
                           	 OU to Another OU

As an example, see the following diagram which illustrates the domain SETUPLABS. Assume that the original Cisco Root OU was
                                 created under the OU MyCorp_Appl. The task is to move Cisco_Root OU from MyCorp_Appl into a new OU called MyCorp_Dev.

Step 1

On the Domain,
                                          			 find the OU in which the Cisco Root OU is contained.

Step 2

Stop all Unified ICM services and applications on the Unified ICM system.

Step 3

On the domain SETUPLABS.com , drag and drop Cisco_ICM from MyCorp_Appl to MyCorp_Dev .

The following
                                             				message is displayed.

Step 4

Click Yes to continue.

The following
                                             				diagram illustrates the current location of the Cisco Root OU.

Step 5

On all the CCE machines, run Web Setup. Open the Instance Management page.

Step 6

Select the existing instance being used.

Step 7

Click Edit .

Step 8

Edit the Facility or the Instance
                                             				Number fields.

Step 9

After making any
                                          			 desired changes, click Save . You return to the Instance List page.

Step 10

Start all Unified ICM/CCE services.

Step 11

Run the Configuration Manager tool.

Step 12

As the permissions for the users in the User List were lost, run the User List tool and re-establish the permissions for individual users. When you re-establish the permissions, ensure that all the users
                                          in the User List Tools have the correct permissions.

| Warning | Moving the Cisco Root OU is only supported if the OU is moved within the same domain. Transferring an OU from one domain to
                                          another is not supported. |
|---|---|

| Step 1 | On the Domain,
                                          			 find the OU in which the Cisco Root OU is contained. |
|---|---|
| Step 2 | Stop all Unified ICM services and applications on the Unified ICM system. |
| Step 3 | On the domain SETUPLABS.com , drag and drop Cisco_ICM from MyCorp_Appl to MyCorp_Dev . The following
                                             				message is displayed. Figure 2. AD Moving
                                                				  Objects Error Message |
| Step 4 | Click Yes to continue. The following
                                             				diagram illustrates the current location of the Cisco Root OU. Figure 3. Cisco Root
                                                				  OU Location |
| Step 5 | On all the CCE machines, run Web Setup. Open the Instance Management page. Figure 4. ICM Setup Dialog Box |
| Step 6 | Select the existing instance being used. |
| Step 7 | Click Edit . |
| Step 8 | Edit the Facility or the Instance
                                             				Number fields. You cannot edit the Domain field. |
| Step 9 | After making any
                                          			 desired changes, click Save . You return to the Instance List page. |
| Step 10 | Start all Unified ICM/CCE services. |
| Step 11 | Run the Configuration Manager tool. |
| Step 12 | As the permissions for the users in the User List were lost, run the User List tool and re-establish the permissions for individual users. When you re-establish the permissions, ensure that all the users
                                          in the User List Tools have the correct permissions. |