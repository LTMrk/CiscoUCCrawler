---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-srsv-guide-b-14cucsrsvx-b-14cucsrsvx-chapter-01-html-38bffbc7dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/srsv/guide/b_14cucsrsvx/b_14cucsrsvx_chapter_01.html
retrieved_at: 2026-08-16T18:35:19.816295+00:00
---

Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

# Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

Updated: March 31, 2021

Chapter: Installing and Configuring Cisco Unity Connection SRSV

## Chapter: Installing and Configuring Cisco Unity Connection SRSV

# Installing and Configuring Cisco Unity Connection SRSV

## Introduction

Cisco Unity Connection Survivable Remote Site Voicemail
                           		(Cisco Unity Connection SRSV) can either be installed on a Cisco Services Ready
                           		Engine (SRE) blade (mounted on Cisco Unified SRST router) or on a virtual
                           		machine.

For installing Unity Connection SRSV on a SRST blade, user needs to virtualize a SRE blade and install the Unity Connection
                                       server on it.  SRE virtualization is supported with VMware ESXi v5.1. 5.5, 6.0, 6.5, 6.5 U2 and 6.7. For more information,
                                       see the “ Cisco Services Ready Engine Virtualization Overview ” chapter of the Installation and Configuration Guide for Cisco Services Ready Engine Virtualization 1.0, available at http://www.cisco.com/c/en/us/td/docs/interfaces_modules/services_modules/sre_v/1-0/user/guide/sre_v.html .

After installing Unity Connection on the virtual machine or the
                           		SRE blade router, follow the tasks in the Task List for Installing Unity Connection SRSV section to install Unity Connection SRSV.

## Prerequisites for
                        	 Installing Unity Connection SRSV

Consider the following points before installing the Unity
                           		Connection SRSV server:

Unity Connection SRSV must be installed on a supported hardware
                                 			 platform. For more information, see the following sections:

“ Specification for Hardware Platforms and Cisco IOS Software Releases Supported by Unity Connection SRSV ” section of the Cisco Unity Connection 14 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html .

“ Specifications for Virtual Platform Overlays Supported by Unity Connection SRSV ” section of the Cisco Unity Connection 14 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html .

The Unity Connection SRSV administrator workstation must be configured as per the software requirements. For more information,
                                       see the “ Software Requirements-Administrator Workstations(Unity Connection and Unity connection SRSV) ” section of the System Requirements for Cisco Unity Connection, Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/requirements/b_14cucsysreqs.html .

## Task List for
                        	 Installing Unity Connection SRSV

Do the following tasks to install and configure a Unity
                           		Connection SRSV server:

Install Unity Connection either on a SRE-900/SRE-910 series blade or on a virtual machine. For information on the process
                                 of installing Unity Connection, see the “ Installing Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 14, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/install_upgrade/guide/b_14cuciumg.html .

After installation, Unity Connection starts in the Demo license
                                 			 mode.

Run the CLI command utils cuc activate CUSRSV to transform the
                                 			 Unity Connection server to a Unity Connection SRSV server.

Install the Unity Connection SRSV specific license on the Prime License Manager (PLM) server of the central Unity Connection
                                 server. For more information on installing licenses, see the “ Managing Licenses ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 14, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/install_upgrade/guide/b_14cuciumg.html .

The CUC_EnhancedMessaging tag on the License page of Cisco Unity
                                 			 Connection Administration reflects the number of licenses installed for both
                                 			 voicemail users and the SRSV feature in Unity Connection.

Following are the scenarios of license status on the central
                                 			 Unity Connection server:

When the central Unity Connection server license status is
                                       				  “Compliance” or “Violation”, all the functionalities, such as user provisioning
                                       				  and voicemail upload related to Unity Connection SRSV work as expected in a
                                       				  normal scenario.

When the central Unity Connection server license status is
                                       				  “Expire”, the synchronization of users from the central Unity Connection to the
                                       				  branch (Unity Connection SRSV) server stops working. However, the voicemail and
                                       				  auto-attendant functionalities continue to work at the branch server.

If you want Cisco Unity Connection SRSV Administration to be
                                    				localized for any other locale (other than Engligh U.S.): Download and
                                 			 install the Cisco Unified Communications Manager <language> locale. See
                                 			 the “Locale Installation” section in the “Software Upgrades” chapter of the applicable Cisco Unified Communications Operating System Administration
                                    				Guide at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cucos/10_0_1/CUCM_BK_C2F2626C_00_cucm-os-admin-guide-100.html. .

The Unity Connection SRSV system can have only one locale
                                             				installed.

If you have installed additional languages and want the
                                    				Cisco Personal Communications Assistant to be localized: Download and
                                 			 install the corresponding Cisco Unified Communications Manager locale. See the “Locale
                                    				Installation” Locale Installation section of "Software Upgrades" chapter
                                 			 of the applicable Cisco Unified
                                    				Communications Operating System Administrator Guide http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cucos/10_0_1/CUCM_BK_C2F2626C_00_cucm-os-admin-guide-100.html. .

Secure the communication between the central Unity Connection
                                    				server and the branch Unity Connection SRSV server after completing the
                                    				installation. This can be done either by uploading signed certificates to the
                                    				central server or allowing the central server to use self-signed certificates.
                                    				For more information, see the Securing
                                       				  Communication between Unity Connection and Unity Connection SRSV section.

Configure the following components displayed in Cisco Unity
                                 			 Connection SRSV Administration:

Users (Administrators and Subscribers).

Call Handler Templates.

System Distribution Lists.

System Call Handlers and Directory Handlers.

Networking.

System Settings (Schedules, Conversations, Enterprise
                                       				  Parameters, and Plugins).

Telephony Integrations (Phone System, Port Group, Port, and
                                       				  Security).

Custom Keypad Mapping.

## Post-Installation
                        	 Tasks

Do the following tasks after completing the installation of a
                           		Unity Connection SRSV server:

Configure the central Unity Connection server from the Branch
                                 			 Management page in Cisco Unity Connection Administration. For more information,
                                 			 see the Configuring Unity connection SRSV Settings section.

Download and install the Real-Time Monitoring Tool software on
                                 			 administrator workstations. See the “ Getting Started ”
                                 			 chapter of the Cisco Unified Real-Time Monitoring Tool Administration Guide,
                                 			 Release 10.0(1), available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/10_0_1/rtmt/CUCM_BK_CA30A928_00_cisco-unified-rtmt-administration-100.html .

### Configuring Unity Connection SRSVSettings

This section gives information on
                              		configuring Unity Connection SRSV to communicate with the central Unity
                              		Connection server.

#### Provisioning and Voicemail Upload

Unity Connection supports the following methods for provisioning and voicemail upload between the central Unity Connection
                                 server and the branch (Unity Connection SRSV) server:

##### Manual Synchronization

You can manually provision the users on the branch server and upload voicemails from the branch server to the central Unity
                                    Connection server.

###### Manually Synchronizing Unity Connection with the Branch Server

In Cisco Unity Connection Administration,
                                                   			 expand Networking> Branch Management and select Branches.

On the Branch Listing page, select Add New
                                                   			 to add a new branch.

On the New Branch page, enter the values of
                                                   			 the required fields and select Save. (For more information on each field, see
                                                   			 Help> This Page).

On the Edit Branch page, select Sync
                                                   			 Provisioning or Voicemail Upload.

To see the branch synchronization results:

In Cisco Unity Connection
                                                         				  Administration, expand Networking> Branch Management and select Branch Sync
                                                         				  Results.

You can filter the synchronization
                                                         				  results by selecting Voicemail or Provisioning in the Value field.(For more
                                                         				  information on each field, see Help> This Page).

##### Automatic Synchronization

You can enable the automatic provisioning of the users and voicemail upload from the branch to the central Unity Connection
                                    server by scheduling the voicemail upload process.

###### Enabling Automatic Provisioning and Voicemail Upload

In Cisco Unity Connection Administration,
                                                   			 expand Tools and select Task Management.

On the Task Management page, schedule either
                                                   			 Branch Provisioning Synchronization Task or Voicemail Upload. (For information
                                                   			 on each field, see Help> This Page).

Select Save.

### Task List for
                           	 Configuring a Unity Connection SRSV User

You can either create a new user or update an existing user to
                              		provide access to the Unity Connection SRSV feature.

Make sure that all the required services, such as Connection REST Service and Connection Branch Sync Service are started on
                                          the central Unity Connection server and on the branch system. For more information on services required for the Unity Connection
                                          SRSV feature, see the Administration Guide for Cisco Unity Connection Serviceability Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/serv_administration/guide/b_14cucservag.html .

Do the following steps to configure a Unity Connection SRSV
                              		user:

Create a partition on the Unity Connection server. For more information on creating a partition, see the “ Configuring Partitions ” section of the “Call Management” chapter of the System Administration Guide for Cisco Unity Connection, Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

Create a branch on the Unity Connection server with the details
                                    			 of Unity Connection SRSV that corresponds to the partition you created:

In Cisco Unity Connection Administration, expand Networking>
                                    			 Branch Management and select Branches.

On the Branch Listing page, select Add New to add a new branch.

On the New Branch page, enter the values of the required fields
                                    			 and select Save. (For more information on each field, see Help> This Page).

Assign the partition to an existing user or a new user for providing access to the Unity Connection SRSV feature. For more
                                    information on creating a new user, see the “ Creating User Accounts Manually ” section of the “Users” chapter of the System Administration Guide for Cisco Unity Connection, Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

| Note | For installing Unity Connection SRSV on a SRST blade, user needs to virtualize a SRE blade and install the Unity Connection
                                       server on it.  SRE virtualization is supported with VMware ESXi v5.1. 5.5, 6.0, 6.5, 6.5 U2 and 6.7. For more information,
                                       see the “ Cisco Services Ready Engine Virtualization Overview ” chapter of the Installation and Configuration Guide for Cisco Services Ready Engine Virtualization 1.0, available at http://www.cisco.com/c/en/us/td/docs/interfaces_modules/services_modules/sre_v/1-0/user/guide/sre_v.html . |
|---|---|

| Note | The Unity Connection SRSV system can have only one locale
                                             				installed. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                                   			 expand Networking> Branch Management and select Branches. |
|---|---|
| Step 2 | On the Branch Listing page, select Add New
                                                   			 to add a new branch. |
| Step 3 | On the New Branch page, enter the values of
                                                   			 the required fields and select Save. (For more information on each field, see
                                                   			 Help> This Page). |
| Step 4 | On the Edit Branch page, select Sync
                                                   			 Provisioning or Voicemail Upload. |
| Step 5 | To see the branch synchronization results: In Cisco Unity Connection
                                                         				  Administration, expand Networking> Branch Management and select Branch Sync
                                                         				  Results. You can filter the synchronization
                                                         				  results by selecting Voicemail or Provisioning in the Value field.(For more
                                                         				  information on each field, see Help> This Page). |

| Step 1 | In Cisco Unity Connection Administration,
                                                   			 expand Tools and select Task Management. |
|---|---|
| Step 2 | On the Task Management page, schedule either
                                                   			 Branch Provisioning Synchronization Task or Voicemail Upload. (For information
                                                   			 on each field, see Help> This Page). |
| Step 3 | Select Save. |

| Note | Make sure that all the required services, such as Connection REST Service and Connection Branch Sync Service are started on
                                          the central Unity Connection server and on the branch system. For more information on services required for the Unity Connection
                                          SRSV feature, see the Administration Guide for Cisco Unity Connection Serviceability Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/serv_administration/guide/b_14cucservag.html . |
|---|---|