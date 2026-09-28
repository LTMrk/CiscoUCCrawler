---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-10-5-cjab-bk-d6497e98-00-deployment-installation-guide-ciscojabber-cj-1886da8bae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/10_5/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber/CJAB_BK_D6497E98_00_deployment-and-installation-guide-for_chapter_00.html
retrieved_at: 2026-08-21T05:10:01.430346+00:00
---

Deployment and Installation Guide for Cisco Jabber, Release 10.5

# Deployment and Installation Guide for Cisco Jabber, Release 10.5

Updated: August 14, 2014

Chapter: Configuration and Installation Workflows

## Chapter: Configuration and Installation Workflows

# Configuration and Installation Workflows

## Server Configuration Workflows for Cloud-Based Deployments

### Cloud-Based
                           	 Deployment Using CUCM 9.x and Later

Configure IM and Presence Service for Cloud-Based Deployments .

Configure Voice and Video Communication for On-Premises Deployments .

Configure Voicemail for an On-Premises Deployment with Cisco Unified Communications Manager Release 9.x and Later .

Configure Conferencing for Cloud-Based Deployments .

Configure the Clients ..

Certificate Requirements for Cloud-Based Servers .

Ensure these
                                             				certificates are on your server.

Configure Service Discovery.

Install the Clients .

### Cloud-Based
                           	 Deployment Using CUCM 8.x

Configure IM and Presence Service for Cloud-Based Deployments .

Configure Voice and Video Communication for On-Premises Deployments .

Configure Voicemail for an On-Premises Deployment with Cisco Unified Communications Manager Release 8.6 .

Configure Conferencing for Cloud-Based Deployments .

Configure the Clients .

Certificate Requirements for Cloud-Based Servers .

Ensure these
                                             				certificates are on your server.

Configure Service Discovery.

Install the Clients .

## Server
                        	 Configuration Workflows for On-Premises Deployments

### Deployment and Installation Workflow for an On-Premises Deployment with CUCM 9.x and Later

Configure IM and Presence Service for On-Premises Deployments with Cisco Unified Communications Manager 9.x and Later .

Configure Voice and Video Communication for Cloud-Based Deployments .

Configure via
                                             				WebEx.

Configure Voicemail for Cloud-Based Deployments .

Configure via
                                             				WebEx.

Configure
                                          			 conferencing.

- To configure onsite, Configure On-Premises Conferencing using WebEx Meetings Server .

- To configure offsite, Configure Cloud-Based Conferencing Using WebEx Meeting Center .

Configure the Clients .

Get Certificates Signed by Certificate Authority .

If there is a
                                             				delay after you request CSRs, you may wish to request them before configuring
                                             				services, and then apply the certificates prior to installing the client.

Configure Service Discovery.

Install the Clients .

### Deployment and Installation Workflow for an On-Premises Deployment with CUCM 8.6 and
                           	 CUP

Configure IM and Presence Service for On-Premises Deployments with Cisco Unified Communications Manager 8.x and Cisco Unified
                                             Presence .

Configure Voice and Video Communication for Cloud-Based Deployments .

Configure via
                                             				WebEx.

Configure Voicemail for Cloud-Based Deployments

Configure via
                                             				WebEx.

Configure
                                          			 conferencing.

- To configure onsite
                                             				conferencing, Configure On-Premises Conferencing using WebEx Meetings Server .

- To configure offsite
                                             				conferencing, Configure Cloud-Based Conferencing Using WebEx Meeting Center .

Configure the Clients .

Get Certificates Signed by Certificate Authority .

If there is a
                                             				delay after you request CSRs, you may wish to request them before configuring
                                             				services, and then apply the certificates prior to installing the client.

Configure Service Discovery.

Install the Clients .

### Deployment and Installation Workflow for Phone Only Mode with CUCM 9.x and Later

Set Up Directory Synchronization and Authentication .

Configure
                                             				synchronization and authentication with your corporate directory server.

Configure Voice and Video Communication .

Configure
                                             				voice and video communication for your deployment.

Configure Voicemail .

Configure
                                             				voicemail for your deployment.

Configure Conferencing .

Configure
                                             				conferencing for your deployment.

Configure the Clients .

User
                                             				experience and client features are controlled using a configuration file.
                                             				Creation of a configuration file is integral part of application deployment.

Install the Clients .

Additional
                                             				client customization can be performed during the installation of Cisco Jabber for Windows and Cisco Jabber for Mac.

## Server
                        	 Configuration Workflows for User-Based Configuration

This section
                              		  describes how to configure an on-premises deployment of Cisco Jabber using Cisco Unified Communications Manager 9.x and later based on the central action of user
                              		  creation. This section is divided into three parts:

Pre-user
                                    				creation tasks

User creation
                                    				tasks

Post-user
                                    				creation tasks

### Pre-User Creation
                           	 Workflow

#### Before you begin

This workflow
                                 		  assumes you have already successfully installed and deployed Cisco Unified
                                    		  Communications Manager , Cisco Unity Connection , and any other supporting services. It is
                                 		  beyond the scope of this document to describe the installation and
                                 		  configuration of these services. Refer to the appropriate documentation suites
                                 		  for information on these tasks before continuing.

Planning Considerations .

Plan your
                                             				deployment by considering what types of technologies you'll need to use to
                                             				service your users.

Hardware Requirements .

Plan your
                                             				deployment by considering if your current hardware meets Cisco Jabber requirements.

Software Requirements .

Plan your
                                             				deployment by considering if you current software meets Cisco Jabber requirements.

Contact Sources .

Plan your
                                             				deployment by considering which contact source type you'll use with Cisco Jabber .

### User Creation
                           	 Workflow

#### Before you begin

This section
                                 		  covers individual tasks pertaining to user and device creation. See the Cisco Unified
                                    			 Communications Manager Bulk Administration Guide for your release of Cisco Unified Communications Manager for information about the bulk creation of
                                 		  users and device assignment.

Set Up Directory Synchronization and Authentication .

Configure
                                             				synchronization and authentication with your corporate directory server.

Configure IM and Presence Service .

Configure IM and Presence Service for your deployment.

Configure Voice and Video Communication .

Configure
                                             				voice and video communication for your deployment.

Configure Voicemail .

Configure
                                             				voicemail for your deployment.

Configure Conferencing .

Configure
                                             				conferencing for your deployment.

### Post-User Creation
                           	 Workflow

#### Before you begin

This section covers tasks that are performed after users and devices
                                 		  have been provisioned.

Configure the Clients .

User
                                             				experience and client features are controlled using a configuration file.
                                             				Creation of a configuration file is integral part of application deployment.

Install the Clients .

Additional
                                             				client customization can be performed during the installation of Cisco Jabber
                                                				for Windows and Cisco Jabber for Mac.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IM and Presence Service for Cloud-Based Deployments . |  |
| Step 2 | Configure Voice and Video Communication for On-Premises Deployments . |  |
| Step 3 | Configure Voicemail for an On-Premises Deployment with Cisco Unified Communications Manager Release 9.x and Later . |  |
| Step 4 | Configure Conferencing for Cloud-Based Deployments . |  |
| Step 5 | Configure the Clients .. |  |
| Step 6 | Certificate Requirements for Cloud-Based Servers . | Ensure these
                                             				certificates are on your server. |
| Step 7 | Configure Service Discovery. |  |
| Step 8 | Install the Clients . |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IM and Presence Service for Cloud-Based Deployments . |  |
| Step 2 | Configure Voice and Video Communication for On-Premises Deployments . |  |
| Step 3 | Configure Voicemail for an On-Premises Deployment with Cisco Unified Communications Manager Release 8.6 . |  |
| Step 4 | Configure Conferencing for Cloud-Based Deployments . |  |
| Step 5 | Configure the Clients . |  |
| Step 6 | Certificate Requirements for Cloud-Based Servers . | Ensure these
                                             				certificates are on your server. |
| Step 7 | Configure Service Discovery. |  |
| Step 8 | Install the Clients . |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IM and Presence Service for On-Premises Deployments with Cisco Unified Communications Manager 9.x and Later . |  |
| Step 2 | Configure Voice and Video Communication for Cloud-Based Deployments . | Configure via
                                             				WebEx. |
| Step 3 | Configure Voicemail for Cloud-Based Deployments . | Configure via
                                             				WebEx. |
| Step 4 | Configure
                                          			 conferencing. To configure onsite, Configure On-Premises Conferencing using WebEx Meetings Server . To configure offsite, Configure Cloud-Based Conferencing Using WebEx Meeting Center . |  |
| Step 5 | Configure the Clients . |  |
| Step 6 | Get Certificates Signed by Certificate Authority . | If there is a
                                             				delay after you request CSRs, you may wish to request them before configuring
                                             				services, and then apply the certificates prior to installing the client. |
| Step 7 | Configure Service Discovery. |  |
| Step 8 | Install the Clients . |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IM and Presence Service for On-Premises Deployments with Cisco Unified Communications Manager 8.x and Cisco Unified
                                             Presence . |  |
| Step 2 | Configure Voice and Video Communication for Cloud-Based Deployments . | Configure via
                                             				WebEx. |
| Step 3 | Configure Voicemail for Cloud-Based Deployments | Configure via
                                             				WebEx. |
| Step 4 | Configure
                                          			 conferencing. To configure onsite
                                             				conferencing, Configure On-Premises Conferencing using WebEx Meetings Server . To configure offsite
                                             				conferencing, Configure Cloud-Based Conferencing Using WebEx Meeting Center . |  |
| Step 5 | Configure the Clients . |  |
| Step 6 | Get Certificates Signed by Certificate Authority . | If there is a
                                             				delay after you request CSRs, you may wish to request them before configuring
                                             				services, and then apply the certificates prior to installing the client. |
| Step 7 | Configure Service Discovery. |  |
| Step 8 | Install the Clients . |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Set Up Directory Synchronization and Authentication . | Configure
                                             				synchronization and authentication with your corporate directory server. |
| Step 2 | Configure Voice and Video Communication . | Configure
                                             				voice and video communication for your deployment. |
| Step 3 | Configure Voicemail . | Configure
                                             				voicemail for your deployment. |
| Step 4 | Configure Conferencing . | Configure
                                             				conferencing for your deployment. |
| Step 5 | Configure the Clients . | User
                                             				experience and client features are controlled using a configuration file.
                                             				Creation of a configuration file is integral part of application deployment. |
| Step 6 | Install the Clients . | Additional
                                             				client customization can be performed during the installation of Cisco Jabber for Windows and Cisco Jabber for Mac. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Planning Considerations . | Plan your
                                             				deployment by considering what types of technologies you'll need to use to
                                             				service your users. |
| Step 2 | Hardware Requirements . | Plan your
                                             				deployment by considering if your current hardware meets Cisco Jabber requirements. |
| Step 3 | Software Requirements . | Plan your
                                             				deployment by considering if you current software meets Cisco Jabber requirements. |
| Step 4 | Contact Sources . | Plan your
                                             				deployment by considering which contact source type you'll use with Cisco Jabber . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Set Up Directory Synchronization and Authentication . | Configure
                                             				synchronization and authentication with your corporate directory server. |
| Step 2 | Configure IM and Presence Service . | Configure IM and Presence Service for your deployment. |
| Step 3 | Configure Voice and Video Communication . | Configure
                                             				voice and video communication for your deployment. |
| Step 4 | Configure Voicemail . | Configure
                                             				voicemail for your deployment. |
| Step 5 | Configure Conferencing . | Configure
                                             				conferencing for your deployment. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure the Clients . | User
                                             				experience and client features are controlled using a configuration file.
                                             				Creation of a configuration file is integral part of application deployment. |
| Step 2 | Install the Clients . | Additional
                                             				client customization can be performed during the installation of Cisco Jabber
                                                				for Windows and Cisco Jabber for Mac. |