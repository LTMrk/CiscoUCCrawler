---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-5-dig-onprem-cjab-b-on-premises-deployment-cisco-jabber-125-cjab-b-2855b45b44
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_5/DIG_OnPrem/cjab_b_on-premises-deployment-cisco-jabber_125/cjab_b_on-premises-deployment-cisco-jabber_125_chapter_010.html
retrieved_at: 2026-08-21T21:09:01.810250+00:00
---

On-Premises Deployment for Cisco Jabber 12.5

# On-Premises Deployment for Cisco Jabber 12.5

Updated: November 27, 2018

Chapter: Configuration and Installation Workflows

## Chapter: Configuration and Installation Workflows

# Configuration and Installation Workflows

## Purpose of
                        	 Configuration Workflows

Configuration and installation workflows outline the processes to
                           		configure and install on-premises deployment. Before you deploy and install
                           		Cisco Jabber, see the Cisco Jabber Planning Guide at Install and Upgrade Guides to determine
                           		the deployment options that best suit your business needs.

## Prerequisites

Installation
                                    				servers must be started and active

Activate and Start Essential Services

Install Cisco Options Package File for Devices

### Activate and Start
                           	 Essential Services

Essential services
                                 		  enable communication between servers and provide capabilities to the client.

Open the Cisco
                                             				Unified IM and Presence Serviceability interface.

Select Tools > Control Center - Feature
                                                				  Services .

Select the
                                          			 appropriate server from the Server drop-down list.

Ensure the
                                          			 following services are started and activated:

- Cisco SIP Proxy

- Cisco Sync Agent

- Cisco XCP Authentication
                                                      					 Service

- Cisco XCP Connection
                                                      					 Manager

- Cisco XCP Text Conference
                                                      					 Manager

- Cisco Presence
                                                      					 Engine

Select Tools > Control Center - Network
                                                				  Services .

Select the
                                          			 appropriate server from the Server drop-down list.

Ensure Cisco
                                             				XCP Router Service is running.

### Install Cisco
                           	 Options Package File for Devices

To make 
                                 		  Cisco Jabber
                                 		  available as a device in 
                                 		  Cisco Unified Communications Manager,
                                 		  you must install a device-specific Cisco Options Package (COP) file on all your
                                 		  
                                 		  Cisco Unified Communications Manager
                                 		  nodes.

Perform this
                                 		  procedure at a time of low usage; it can interrupt service.

General
                                 		  information about installing COP files is available in the “Software Upgrades”
                                 		  chapter in the Cisco Unified
                                    			 Communications Operating System Administration Guide for your release.

Download the
                                          			 device COP file.

Locate the
                                                				  device COP file.

Go to
                                                         						  the software downloads
                                                            							 site .

Locate
                                                         						  the device COP file for your release.

Click Download Now .

Note the
                                                				  MD5 checksum.

You will
                                                   					 need this information later.

Click Proceed with Download and follow the instructions.

Place the COP
                                          			 file on an FTP or SFTP server that is accessible from your 
                                          			 Cisco Unified Communications Manager
                                          			 nodes.

Install this
                                          			 COP file on the Publisher node in your 
                                          			 Cisco Unified Communications Manager
                                          			 cluster:

Open the Cisco Unified OS Administration interface.

Select Software
                                                      						Upgrades > Install/Upgrade .

Specify
                                                				  the location of the COP file and provide the required information.

For more
                                                   					 information, see the online help.

Select Next .

Select the
                                                				  device COP file.

Select Next .

Follow the
                                                				  instructions on the screen.

Select Next .

Wait for
                                                   					 the process to complete. This process can take some time.

Reboot 
                                                				  Cisco Unified Communications Manager
                                                				  at a time of low usage.

Let the
                                                				  system fully return to service.

To avoid
                                                               						interruptions in service, make sure each node returns to active service before
                                                               						you perform this procedure on another server.

Install the COP file on each Subscriber node in the cluster.

Use the same process you used for the Publisher, including rebooting the node.

## Deployment and Installation Workflows

### Full UC Deployment

Read the Cisco
                                          			 Jabber Planning Guide located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Choose
                                                   					 your deployment scenario.

Review
                                                   					 requirements to confirm that you meet them.

Review
                                                   					 contact sources to determine which contact source you will use.

Create Default Service Profile

Create a default service profile to add services.

Contact Source

Configure a contact source for your users.

Configure Instant Messaging and Presence Service

Set up the Cisco Unified Communications IM & Presence service.

Configure Voicemail

Set up voicemail for your users.

Configure Webex Conferencing

Set up conferencing with Cisco Webex Meetings Server.

Configure CTI Service

Set up a CTI service and provide Jabber with devices that are associated with users.

Users

Set up users for Jabber.

Configure Softphone

Set up softphone devices for users.

Configure Deskphone Control

Create deskphone devices and enable features.

Configure Extend and Connect

Set up options for users to extend calls to remote devices.

Configure Service Discovery

Choose a service discovery option for your users.

Configure Certificate Validation

Set up the required certificates for each server.

Configure the Clients

Choose what features to include in the client configuration files.

Deploy Cisco Jabber Applications and Jabber Softphone for VDI

Choose how to install the clients for your users.

### Jabber IM Only Deployment

Read the Cisco
                                          			 Jabber Planning Guide located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Choose
                                                   					 your deployment scenario.

Review
                                                   					 requirements to confirm that you meet them.

Review
                                                   					 contact sources to determine which contact source you will use.

Create Default Service Profile

Create a default service profile to add services.

Contact Source

Configure a contact source for your users.

Configure Instant Messaging and Presence Service

Set up the Cisco Unified Communications IM & Presence service.

Configure Webex Conferencing

Set up conferencing with Cisco Webex Meetings Server.

Users

Set up users for Jabber.

Configure Service Discovery

Choose a service discovery option for your users.

Configure Certificate Validation

Set up the required certificates for each server.

Configure the Clients

Choose what features to include in the client configuration files.

Deploy Cisco Jabber Applications and Jabber Softphone for VDI

Choose how to install the clients for your users.

### Phone Only Mode Deployment

Read the Cisco
                                          			 Jabber Planning Guide located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Choose
                                                   					 your deployment scenario.

Review
                                                   					 requirements to confirm that you meet them.

Review
                                                   					 contact sources to determine which contact source you will use.

Create Default Service Profile

Create a default service profile to add services.

Configure Voicemail

Set up voicemail for your users.

Configure Webex Conferencing

Set up conferencing with Cisco Webex Meetings Server.

Configure CTI Service

Set up a CTI service and provide Jabber with devices that are associated with users.

Users

Set up users for Jabber.

Configure Softphone

Set up softphone devices for users.

Configure Service Discovery

Choose a service discovery option for your users.

Configure Certificate Validation

Certificates
                                             				are required for each service to which the Jabber clients connect.

Configure the Clients

Choose what features to include in the client configuration files.

Deploy Cisco Jabber Applications and Jabber Softphone for VDI

Choose how to install the clients for your users.

### Phone Mode with Contacts Deployment

Read the Cisco Jabber Planning Guide located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Confirm that you meet the requirements.

Determine which contact sources you will use.

Create Default Service Profile

Create a default service profile to add services.

Contact Source

Configure a contact source for your users.

Manage Presence Settings

Choose if your users have presence in the client.

Disable Instant Message Settings

Remove instant messaging for this phone mode with contacts deployment.

Configure Voicemail

Set up voicemail for your users.

Configure Webex Conferencing

Set up conferencing with Cisco Webex Meetings Server.

Configure CTI Service

Set up a CTI service and provide Jabber with devices that are associated with users.

Users

Set up users for Jabber.

Configure Softphone

Set up softphone devices for users.

Configure Deskphone Control

Create deskphone devices and enable features.

Configure Extend and Connect

Set up options for users to extend calls to remote devices.

Configure Service Discovery

Choose a service discovery option for your users.

Configure Certificate Validation

Set up the required certificates for each server.

Configure the Clients

Choose what features to include in the client configuration files.

Deploy Cisco Jabber Applications and Jabber Softphone for VDI

Choose how to install the clients for your users.

| Step 1 | Open the Cisco
                                             				Unified IM and Presence Serviceability interface. |
|---|---|
| Step 2 | Select Tools > Control Center - Feature
                                                				  Services . |
| Step 3 | Select the
                                          			 appropriate server from the Server drop-down list. |
| Step 4 | Ensure the
                                          			 following services are started and activated: Cisco SIP Proxy Cisco Sync Agent Cisco XCP Authentication
                                                      					 Service Cisco XCP Connection
                                                      					 Manager Cisco XCP Text Conference
                                                      					 Manager Cisco Presence
                                                      					 Engine |
| Step 5 | Select Tools > Control Center - Network
                                                				  Services . |
| Step 6 | Select the
                                          			 appropriate server from the Server drop-down list. |
| Step 7 | Ensure Cisco
                                             				XCP Router Service is running. |

| Step 1 | Download the
                                          			 device COP file. Locate the
                                                				  device COP file. Go to
                                                         						  the software downloads
                                                            							 site . Locate
                                                         						  the device COP file for your release. Click Download Now . Note the
                                                				  MD5 checksum. You will
                                                   					 need this information later. Click Proceed with Download and follow the instructions. |
|---|---|
| Step 2 | Place the COP
                                          			 file on an FTP or SFTP server that is accessible from your 
                                          			 Cisco Unified Communications Manager
                                          			 nodes. |
| Step 3 | Install this
                                          			 COP file on the Publisher node in your 
                                          			 Cisco Unified Communications Manager
                                          			 cluster: Open the Cisco Unified OS Administration interface. Select Software
                                                      						Upgrades > Install/Upgrade . Specify
                                                				  the location of the COP file and provide the required information. For more
                                                   					 information, see the online help. Select Next . Select the
                                                				  device COP file. Select Next . Follow the
                                                				  instructions on the screen. Select Next . Wait for
                                                   					 the process to complete. This process can take some time. Reboot 
                                                				  Cisco Unified Communications Manager
                                                				  at a time of low usage. Let the
                                                				  system fully return to service. Note To avoid
                                                               						interruptions in service, make sure each node returns to active service before
                                                               						you perform this procedure on another server. | Note | To avoid
                                                               						interruptions in service, make sure each node returns to active service before
                                                               						you perform this procedure on another server. |
| Note | To avoid
                                                               						interruptions in service, make sure each node returns to active service before
                                                               						you perform this procedure on another server. |
| Step 4 | Install the COP file on each Subscriber node in the cluster. Use the same process you used for the Publisher, including rebooting the node. |

| Note | To avoid
                                                               						interruptions in service, make sure each node returns to active service before
                                                               						you perform this procedure on another server. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Read the Cisco
                                          			 Jabber Planning Guide located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Choose
                                                   					 your deployment scenario. Review
                                                   					 requirements to confirm that you meet them. Review
                                                   					 contact sources to determine which contact source you will use. |
| Step 2 | Create Default Service Profile | Create a default service profile to add services. |
| Step 3 | Contact Source | Configure a contact source for your users. |
| Step 4 | Configure Instant Messaging and Presence Service | Set up the Cisco Unified Communications IM & Presence service. |
| Step 5 | Configure Voicemail | Set up voicemail for your users. |
| Step 6 | Configure Webex Conferencing | Set up conferencing with Cisco Webex Meetings Server. |
| Step 7 | Configure CTI Service | Set up a CTI service and provide Jabber with devices that are associated with users. |
| Step 8 | Users | Set up users for Jabber. |
| Step 9 | Configure Softphone | Set up softphone devices for users. |
| Step 10 | Configure Deskphone Control | Create deskphone devices and enable features. |
| Step 11 | Configure Extend and Connect | Set up options for users to extend calls to remote devices. |
| Step 12 | Configure Service Discovery | Choose a service discovery option for your users. |
| Step 13 | Configure Certificate Validation | Set up the required certificates for each server. |
| Step 14 | Configure the Clients | Choose what features to include in the client configuration files. |
| Step 15 | Deploy Cisco Jabber Applications and Jabber Softphone for VDI | Choose how to install the clients for your users. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Read the Cisco
                                          			 Jabber Planning Guide located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Choose
                                                   					 your deployment scenario. Review
                                                   					 requirements to confirm that you meet them. Review
                                                   					 contact sources to determine which contact source you will use. |
| Step 2 | Create Default Service Profile | Create a default service profile to add services. |
| Step 3 | Contact Source | Configure a contact source for your users. |
| Step 4 | Configure Instant Messaging and Presence Service | Set up the Cisco Unified Communications IM & Presence service. |
| Step 5 | Configure Webex Conferencing | Set up conferencing with Cisco Webex Meetings Server. |
| Step 6 | Users | Set up users for Jabber. |
| Step 7 | Configure Service Discovery | Choose a service discovery option for your users. |
| Step 8 | Configure Certificate Validation | Set up the required certificates for each server. |
| Step 9 | Configure the Clients | Choose what features to include in the client configuration files. |
| Step 10 | Deploy Cisco Jabber Applications and Jabber Softphone for VDI | Choose how to install the clients for your users. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Read the Cisco
                                          			 Jabber Planning Guide located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Choose
                                                   					 your deployment scenario. Review
                                                   					 requirements to confirm that you meet them. Review
                                                   					 contact sources to determine which contact source you will use. |
| Step 2 | Create Default Service Profile | Create a default service profile to add services. |
| Step 3 | Configure Voicemail | Set up voicemail for your users. |
| Step 4 | Configure Webex Conferencing | Set up conferencing with Cisco Webex Meetings Server. |
| Step 5 | Configure CTI Service | Set up a CTI service and provide Jabber with devices that are associated with users. |
| Step 6 | Users | Set up users for Jabber. |
| Step 7 | Configure Softphone | Set up softphone devices for users. |
| Step 8 | Configure Service Discovery | Choose a service discovery option for your users. |
| Step 9 | Configure Certificate Validation | Certificates
                                             				are required for each service to which the Jabber clients connect. |
| Step 10 | Configure the Clients | Choose what features to include in the client configuration files. |
| Step 11 | Deploy Cisco Jabber Applications and Jabber Softphone for VDI | Choose how to install the clients for your users. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Read the Cisco Jabber Planning Guide located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Confirm that you meet the requirements. Determine which contact sources you will use. |
| Step 2 | Create Default Service Profile | Create a default service profile to add services. |
| Step 3 | Contact Source | Configure a contact source for your users. |
| Step 4 | Manage Presence Settings | Choose if your users have presence in the client. |
| Step 5 | Disable Instant Message Settings | Remove instant messaging for this phone mode with contacts deployment. |
| Step 6 | Configure Voicemail | Set up voicemail for your users. |
| Step 7 | Configure Webex Conferencing | Set up conferencing with Cisco Webex Meetings Server. |
| Step 8 | Configure CTI Service | Set up a CTI service and provide Jabber with devices that are associated with users. |
| Step 9 | Users | Set up users for Jabber. |
| Step 10 | Configure Softphone | Set up softphone devices for users. |
| Step 11 | Configure Deskphone Control | Create deskphone devices and enable features. |
| Step 12 | Configure Extend and Connect | Set up options for users to extend calls to remote devices. |
| Step 13 | Configure Service Discovery | Choose a service discovery option for your users. |
| Step 14 | Configure Certificate Validation | Set up the required certificates for each server. |
| Step 15 | Configure the Clients | Choose what features to include in the client configuration files. |
| Step 16 | Deploy Cisco Jabber Applications and Jabber Softphone for VDI | Choose how to install the clients for your users. |