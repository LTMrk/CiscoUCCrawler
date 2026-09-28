---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-jabber-for-everyone-12-5-1-cup0-b-jabber-for-everyone-solut-f655fe9d11
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/jabber_for_everyone/12_5_1/cup0_b_jabber-for-everyone-solution-guide.html
retrieved_at: 2026-08-20T15:39:26.204819+00:00
---

Jabber for Everyone Quick Start Guide

# Jabber for Everyone Quick Start Guide

### Download Options

Updated: December 9, 2019

First Published: December 9, 2019

# Purpose of this Document

This document provides a solution level overview of Cisco “Jabber for Everyone” as well as a quick start guide to deployment;
                  from core functionality to advanced features. This document also contains links to the appropriate supporting documentation
                  on www.cisco.com.

This document supports the IM and Presence Service, Release 11.5(1), 12.0(1), and 12.5(1).

## Jabber for Everyone Overview

"Jabber for everyone " makes Cisco Jabber presence and instant messaging (IM) available at a small end user cost for customers who have deployed Cisco Unified Communications Manager for all or part of their organization

"Jabber for Everyone" provides the complete flexibility of Jabber's Bring Your Own Device (BYOD) capabilities for presence and IM. The full range
                     of Cisco Jabber clients deployable on Windows, MAC, iPad, iPhone, and Android are supported. Customers can also build and deploy presence
                     and IM-enabled applications using the Jabber Web Software Development Kit (SDK).

Employees who are existing Cisco IP Telephony users can leverage Cisco Jabber clients to control their IP desk phone to initiate and manage calls. In addition, employees who are existing Cisco Unity Connection users can leverage Cisco Jabber clients for visual voicemail. Customers who are fully licensed for Cisco Collaboration can easily expand beyond the "Jabber for Everyone" IM and Presence Service to leverage Jabber's complete Unified Communications capabilities, including WebEx meetings, and standards-based voice and
                     HD video (using Cisco's Precision Video Engine PVE technology) across desktop and mobile devices.

### Jabber for Everyone Solution Supported Features

"Jabber for Everyone" enables a broad range of Cisco Jabber features as follows:

Core IM and Presence —This is the baseline offering. It provides standard IM features such as One-to-One and   Group Chat IM. It also provides
                              a range of presence states  ( "Available," "Away," "Offline," "Do Not Disturb," and custom status). Core IM and Presence also enables Multi-Device which allows a user to log in to multiple Cisco Jabber devices in parallel (such as Cisco Jabber for Windows and Cisco Jabber IM for iPhone), send and receive IMs to multiple devices simultaneously and set presence state from any
                              device. See Table 1 for details of supported features.

Advanced IM —If you want to add other  advanced IM features such as federation, compliance and high availability, you can incorporate
                              them into your deployment with additional configuration. See Table 1 for details.

Rich UC Presence —If you want to integrate additional sources of presence including the telephony state of Cisco IP phone-enabled users  ( "On a call" ) or meeting status from Microsoft Exchange ( "In a Meeting" ) with the presence features that are available with Core IM and Presence , you can do so with   additional configuration. See Table 1 for details.

Desk Phone Control —Along with IM and Presence capabilities, "Jabber for Everyone" allows users who are configured for Cisco IP Telephony to also use their Cisco Jabber client to control their Cisco IP phone to make and answer calls through Computer Telephony Integration (CTI).

Visual Voicemail —If you have Cisco Unity Connection deployed, you can add the ability to view, play, sort and delete voicemail messages from Cisco Jabber with additional configuration.

- Mobile and Remote Access —If you have Cisco Expressway deployed,  you can provide presence and instant messaging features to Cisco Jabber users whereby Cisco Jabber users do not have to connect to the corporate network over a VPN.

You must configure Core IM and Presence as  the first step to utilize basic features of IM and Presence and as a prerequisite to further enable Rich UC Presence , any of the Advanced IM , Desk Phone Control or Visual Voicemail features, if you wish to do so. You can  flexibly select which features of Rich UC Presence and Advanced IM you wish to enable. In general, these optional features do not have to be configured or enabled in any particular sequence.

The following matrix lists the features that "Jabber for Everyone" supports for each client.

( "Available," "Away," "Do not Disturb," "Offline" )

1 Interdomain federation enables IM and Presence Service client users in one enterprise domain to exchange presence information and IM with users in external domains.

2 Partitioned intradomain federation enables IM and Presence Service client users and Microsoft Skype for Business users within the same enterprise domain to exchange presence information and
                                    IM.

The following features are not included in "Jabber for Everyone" :

Audio

Video (softphone and softphone control)

Desktop sharing

Options for phone configuration

### Jabber for Everyone Architecture

"Jabber for Everyone" is an IM and Presence Service solution that consists of the following components:

Server software—Provides IM, presence, and directory services to the client application

Client application—Renders IM and presence functionality to users

#### Server Software

"Jabber for Everyone" comprises the following server components:

Cisco Unified Communications Manager —Provides user configuration, device configuration, licensing, and directory integration services.

IM and  Presence Service —Provides instant messaging and presence capabilities.

External directory source—Provides contact search and retrieval services. For directory requirements for specific clients,
                                 see the appropriate client documentation.

#### Client Software

"Jabber for Everyone" supports the following Cisco Jabber clients, as release available:

Cisco Jabber for Windows

Cisco Jabber for Mac

Cisco Jabber IM for Android

Cisco Jabber IM for iPhone

Cisco Jabber for iPad

Cisco Jabber Web SDK

### Related Documentation

You can find installation, configuration, and administration information for Cisco Unified Communications Manager , IM and  Presence Service , and Cisco Jabber clients at the following links:

## System Requirements

### Deployment Prerequisites

The only prerequisite to deploy "Jabber for Everyone" is that you must be both a Cisco Unified Communications Manager customer and an IM and Presence Service customer.

### Hardware and Software Requirements

This section describes the hardware and software requirements for "Jabber for Everyone" .

#### Hardware Requirements

"Jabber for Everyone" supports Cisco-provided, third party compatible, or virtual hardware solutions. For more information about hardware requirements,
                           see the appropriate compatibility information for IM and Presence Service and Cisco Unified Communications Manager .

##### Scale Requirements

For Cisco Unified Communications Manager nodes, adding users with "Jabber for Everyone" should not impact the scalability for the core voice and video users.

For IM and Presence Service , mixing full UC mode users and users added with "Jabber for Everyone" is supported on the same node, or cluster. The following formula shows how to determine how many users you can add to your
                           deployment with "Jabber for Everyone" :

Number of "Jabber for Everyone" users = (Number of full UC users/Maximum number of full UC users) x Maximum number of "Jabber for Everyone" users

For example, if you have 10,000 full UC users on a node that supports a maximum of 15,000 users, then you are operating at
                           2/3 of the scale for UC, which means that 1/3 is available for "Jabber for Everyone" users. The IM and Presence Service supports 15,000 users for IM-only mode, therefore, you can add 5,000 users (15,000 x 1/3) through "Jabber for Everyone" . This amounts to a total of 15,000 users.

For more information about sizing an IM and Presence Service cluster, refer to the Cisco Collaboration Sizing Tool.

#### Software Requirements

" Jabber for Everyone" is supported with Cisco Unified Communications Manager and IM and Presence Service Releases 11.5, 12.0 and 12.5.

For Cisco Jabber , refer to your Jabber product documentation.

### License Requirements

With "Jabber for Everyone" , Jabber IM client applications and IM and Presence Service licenses are available to Cisco Unified Communications Manager customers at no additional license cost.

Ordering options are available for existing User Connect Licensing (UCL) and Cisco Unified Workspace Licensing (CUWL) customers
                        as follows:

Cisco Unified Communications Manager UCL customers can order "Jabber for Everyone" to provide IM support to users that are not Cisco Unified Communications Manager users.

CUWL customers can order "Jabber for Everyone" to provide IM support to users that are not Cisco Unified Communications Manager users.

IM and Presence Service is an integrated service, therefore all Cisco Unified Communications Manager users have access to IM as part of the core user licensing.

The following table describes the available SKUs.

New or upgraded customer of IM and Presence Service , Release 11.5(1), 12.0(1) or 12.5(1).

Order new JABBER-IM-ADDON under the Presence on-premise CUWL options, where clients are selected to request IM for the number of non- Cisco Unified Communications Manager users.

Existing customer of IM and Presence Service Release 11.5(1), 12.0(1) or 12.5(1).

Order new JABBER-IM-ADDON standalone SKU   to request IM for the number of non- Cisco Unified Communications Manager users.

For e-delivery, use R-JABBER-ADDON-K9 .

For physical delivery, use JABBER-ADDON-K9 .

New or upgraded customer of IM and Presence Service , Release 11.5(1), 12.0(1) and 12.5(1).

Order new JABBER-IM-ADDON within the UCL configuration (CUCM-USR-LIC) to request IM for the number of non- Cisco Unified Communications Manager users
                                    .

Existing customer of IM and Presence Service Release 11.5(1), 12.0(1) and 12.5(1).

Order new JABBER-IM-ADDON standalone SKU  to request IM for the number of non- Cisco Unified Communications Manager users.

For e-delivery, use R-JABBER-ADDON-K9 .

For physical delivery, use JABBER-ADDON-K9 .

## Jabber for Everyone Deployment Workflow

Core IM and Presence represents the baseline offering for the "Jabber for Everyone" solution.  You can extend your deployment by incorporating any of the following additional, optional feature sets:

Advanced IM

Rich UC Presence

Desk Phone Control

Visual Voicemail

Each deployment scenario assumes that Unified Communications Manager is installed.

The following figure shows the Core IM and Presence feature set and the optional features that can be deployed with additional configuration for Advanced IM , Rich UC Presence , Desk Phone Control and Visual Voicemail .

### Core IM and Presence Service Deployment

The following are the high-level tasks that you must complete to enable core IM and Presence Service features in your network:

Set up users on Cisco Unified Communications Manager .

Install the IM and  Presence Service .

Verify essential services on Cisco Unified Communications Manager and IM and  Presence Service .

Specify capabilities assignments for end users on Cisco Unified Communications Manager .

Create an LDAP profile on the IM and Presence Service .

Install Cisco Jabber .

You can deploy "Jabber for Everyone" in a mixed cluster where you provision some users with only instant messaging and availability and other users with instant
                                    messaging and availability  along with audio capabilities.

You should create separate service profiles for users that have only instant messaging and availability capabilities. If the
                                    service profile contains a CTI or Cisco CallManager Cisco IP Phone (CCMCIP) profile, the client attempts to retrieve device
                                    lists for users from Cisco Unified Communications Manager . If no device lists exist for users, the client continually requests device lists from the node. As a result, the node consumes
                                    additional CPU resources.

Jabber for Everyone is also supported in Centralized Deployments of the IM and Presence Service. To use this option, you must
                                    be running a minimum IM and Presence Service release of 11.5(1)SU4.

#### Set Up Users on Cisco Unified Communications Manager

The Cisco Jabber clients retrieve user details from Cisco Unified Communications Manager . For this reason, you must add users to Cisco Unified Communications Manager , including users who are not Cisco IP phone users.

Add users to Cisco Unified Communications Manager using one of the following methods:

Provisioning Method

Details

Add users via LDAP Directory Sync

Add users to the database by syncing users from a company LDAP directory. Complete the following high-level tasks:

Configure UC Services such as IM and Presence Service, Voicemail, Drectory  and Jabber config file (for optional Jabber feature
                                                         customization).

Add your UC services to a Service Profile and add the Service Profile to a Feature Group Template.

Add the Service Profile to a Feature Group Template.

Configure an LDAP Directory sync that includes the Feature Group Template that you configured, and which also assigns users
                                                         to the Standard CCM End Users access control group.

Complete an LDAP sync.

For configuration details, refer to configuring and provisioning end users sections in the System Configuration Guide for Cisco Unified Communications Manager .

Add users via Bulk Administration

Add multiple users from a csv file with the Bulk Administration Tool.

In Unified CM, configure UC services such as voicemail, directory access, IM and Presence Servie, and Jabber config files
                                                         (for Jabber features).

In Unified CM, add UC Services to a Service Profile.

Download the BAT.xlt spreadsheet and use it to create a csv file with your end users. For the Service Profile , make sure to assign the IM and Presence-enabled profile that you set up.

Use Bulk Administration to import the end users into the database.

For details on how to configure Service Profiles, see System Configuration Guide for Cisco Unified Communications Manager .

For details on how to use the BAT spreadsheet to import users into the database, see the “User Additions” chapter in the Bulk Administration Guide for Cisco Unified Communications Manager .

Add users manually

Add individual users manually. See the “Manage End Users” chapter of the Administration Guide for Cisco Unified Communications Manager for instructions on manually adding individual users.

If you haven't already assigned users to the Standard CCM End Users access control group, do so now.

See the “Assign Users to Access Control Groups” section in the Cisco Unified Communications Manager Administration Guide for instructions on assigning users to a user group.

#### Install the IM and Presence Service

"Jabber for Everyone" requires integration with the IM and Presence Service . If your environment does not already include IM and Presence Service , you must install the IM and Presence Service software that is included in your Unified Communications software delivery.

For installation details, refer to the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service . You have the option to install your system using either touchless installation or the basic installation.

Cisco recommends that you use the touchless installation method to install your system using an answer file. This method lets
                                    you define configuration values before initializing the installation process, which provides an automated installation and
                                    helps ensure a successful installation.

#### Verify Essential Services on Cisco Unified Communications Manager  and the IM and Presence Service

A number of essential services must be activated and in a started state on Cisco Unified Communications Manager and IM and Presence Service to ensure that data synchronizes between the two nodes and that the Cisco Jabber clients can access IM and Presence Service feature services.

Most services automatically activate and start when you install the node. However, you should verify that the services that
                                       are listed in the following procedure are in a started state before you proceed with any other deployment tasks.

Verify that the Cisco AXL Web Service feature service is activated and in a started state on Cisco Unified Communications Manager :

For procedures on how to activate feature services, see the “Services” chapter in the Cisco Unified Serviceability Administration Guide .

Verify that the following feature services are activated and  started on the IM and Presence Service :

- Cisco Presence Engine

- Cisco Sync Agent

- Cisco XCP Connection Manager

- Cisco XCP Authentication Service

- Cisco XCP Text Conference Manager

Verify that all network services on IM and Presence Service are activated and started.

#### Specify End-user Capabilities on Cisco Unified Communications Manager

You must assign IM and Presence Service capabilities to users in Cisco Unified Communications Manager .

Log in to the Cisco Unified Communications Manager Administration interface.

Choose User Management > End User .

Use the filters to the find the user that you want to enable for the IM and Presence Service .

The user configuration displays in the End User Configuration window.

Configure the following options in the End User Configuration window.

- Enable User for Unified CM IM and Presence —Check this check box to turn the IM and Presence Service on for this user.

- Include meeting information in presence —Check this optional check box if you want to enable calendar integration with Microsoft Outlook for this user.

- Service Profile —Make sure that the service profile that you configured for the IM and Presence Service is selected.

Click Save .

If you have a large group of existing users for whom you want to enable IM and Presence, you can use the Update Users feature
                                       of Bulk Administration to check the check box in the above procedure for all of those users. See the "User Updates" chapter
                                       of the Bulk Administration Guide for Cisco Unified Communications Manager .

#### LDAP Configuration on the IM and Presence Service

IM and Presence Service Lightweight Directory Access Protocol (LDAP) integration provides contact search capabilities for Jabber clients. LDAP integration
                           for the IM and Presence Service is configured on Cisco Unified Communications Manager via the Service Profile. Refer to the
                           end user configuration sections of the System Configuration Guide for Cisco Unified Communications Manager for information on configuring directory access in Cisco Unified Communications Manager.

In addition, see the appropriate Cisco Jabber client documentation for additional  information that is specific to your Jabber deployment.

##### Third-Party Clients

If you are deploying additional third-party XMPP clients, configure the IM and Presence Service to allow contact searches
                           from the third-party XMPP clients. For details, refer to the "LDAP Directory Integration for Contact Searches on XMPP Clients"
                           configuration section of the Configuration and Administration Guide for the IM and Presence Service .

#### Cisco Jabber Installation

After you complete the procedures to set up Cisco Unified Communications Manager IM and Presence Service , you must configure and install the appropriate Cisco Jabber clients. However, it is beyond the scope of this document to provide detailed instructions on installing all of the Cisco Jabber clients. This document provides a high-level overview of the steps you must complete to install an IM and Presence Service deployment of Cisco Jabber . Refer to the appropriate client documentation for detailed instructions.

##### Install Cisco Jabber

Before you begin

###### Before you begin

Review configuration parameters for Cisco Jabber.

In most environments, Cisco Jabber for Windows does not require any configuration and can connect automatically to the IM and Presence Service and Microsoft Active Directory . Before you create a configuration file, review the default configuration parameters to determine if your deployment requires
                                                   any configuration.

For a detailed list of parameters that are available with Jabber configuration files, refer to Parameters Reference Guide for Cisco Jabber .

(Optional) Complete the following steps if your deployment requires configuration:

Create the configuration files.

Host the configuration files on your TFTP server.

Restart the TFTP service on Cisco Unified Communications Manager .

You must restart the TFTP service on each node where you host a configuration file.

Refer to the "Create and Host the Client Configuration Files" task flow in the "Configure the Clients" chapter of On-Premises Deployment for Cisco Jabber :

Install Cisco Jabber . See the “Deploy Cisco Jabber Applications” chapter of On-Premises Deployment for Cisco Jabber for installation instructions.

For additional information on Jabber feature configuration, refer to Feature Configuration for Cisco Jabber .

##### Develop with Cisco Jabber Web SDK

The Cisco Jabber Web SDK enables you to integrate Cisco Unified Communications capabilities in web applications. To integrate IM capabilities in a web application, you use the Cisco AJAX XMPP Library
                              (CAXL). CAXL is a client-side JavaScript library that runs in a web browser and sends and receives XMPP messages as HTTP POSTs.

Set up a web server.

Download the CAXL library from the Cisco Developer Network.

Extract the contents of the CAXL library to the working directory of your website.

Implement the required HTML with JavaScript objects to send and receive XMPP messages.

### Advanced IM and Presence Service Deployment

"Jabber for Everyone" supports optional advanced IM and Presence Service features that extend your baseline deployment.

#### Supported Federation

"Jabber for Everyone" supports interdomain federation and partitioned intradomain federation.

##### Interdomain Federation

Microsoft Lync

Microsoft Skype for Business (Minimum IM and Presence Service release is 11.5(1)SU2)

Another IM and Presence Service system

Any other XMPP-compliant system

For more information about deploying interdomain federation on the IM and Presence Service , see the Interdomain Federation Guide for IM and Presence Service .

See the appropriate Cisco Jabber client documentation to review support for interdomain federation and any required configuration.

##### Partitioned Intradomain Federation

- Microsoft Lync Server

Microsoft Skype for Business (Minimum IM and Presence Service release is 11.5(1)SU2)

For more information about deploying partitioned intradomain federation, see the Partitioned Intradomain Federation for IM and Presence Service on Cisco Unified Communications Manager .

See  the appropriate Cisco Jabber client documentation to review support for partitioned  intradomain federation and any required configuration.

#### IM Compliance

Point-to-point messages

Group chats, including temporary and permanent chat messages

For more information about configuring IM compliance, see Instant Messaging Compliance for IM and Presence Service .

#### Intercluster Peering

You can deploy multiple clusters of IM and Presence services for large-scale deployments. If you deploy multiple clusters,
                           you must define peer relationships for each IM and Presence Service cluster within the same domain.

For more information about multiple cluster deployments, see Cisco Collaboraton Preferred Architectures documentation.

For more information about configuring an intercluster deployment, see Configuration and Administration of IM and Presence Service .

#### High Availability

The IM and Presence Service supports high availability with clustered nodes. If a node in a subcluster fails, the IM and Presence services from that
                           node fail over to the second node in the subcluster. As a result, there is no loss of IM and Presence services for users.

For information about configuring high availability deployments, see Configuration and Administration of IM and Presence Service .

### Rich UC Presence Deployment

You can optionally expand your Cisco Jabber for Everyone deployment to include Telephone Presence ( "On a call" )  for Cisco IP phone users and Meeting Status ( "In a Meeting" ) through integration with Microsoft Exchange.

#### Telephony Presence Integration

The following are the high-level tasks that you must complete if you want to deploy rich presence for Cisco IP phone users
                           in your network:

Configure the SIP Publish trunk.

Configure a Presence Gateway for Cisco Unified Communications Manager .

Associate line appearances to IM and Presence Service enabled users.

##### Set Up SIP Publish Trunk

Cisco Unified Communications Manager communicates with the IM and Presence Service through a SIP trunk.

Configure the SIP trunk on Cisco Unified Communications Manager .

For instructions, see the "SIP Trunk Configuration on Cisco Unified Communications Manager " section in Configuration and Administration of the IM and Presence Service .

Choose the SIP publish trunk on IM and Presence.

Log in to the Cisco Unified Communications Manager IM and Presence Administration interface.

Choose Presence > Settings .

From the CUCM SIP Publish Trunk drop-down list, choose the SIP publish trunk.

Click Save .

##### Set Up Presence Gateway for Cisco Unified Communications Manager

You must configure Cisco Unified Communications Manager as a Presence Gateway on the IM and Presence Service . The Presence Gateway enables Cisco Unified Communications Manager and the IM and Presence Service to share availability status for users.

Log in to the Cisco Unified Communications Manager IM and Presence Administration interface.

Choose Presence > Gateways .

Click Add New .

From the Presence Gateway Type drop-down list, choose CUCM .

In the Description field, enter a description.

In the Presence Gateway field, specify one of the following values:

IP address of the Cisco Unified Communications Manager publisher node.

Fully qualified domain name (FQDN) of the Cisco Unified Communications Manager publisher node.

DNS SRV FQDN that resolves to the Cisco Unified Communications Manager subscriber nodes.

Click Save .

For more information about configuring a Presence Gateway, see Configuration and Administration of IM and Presence Service .

##### Associate Line Appearances with Users

To enable telephony presence, you must associate each IM and Presence Service enabled user with a line appearance in Cisco Unified Communications Manager .

Log in to  the Cisco Unified Communications Manager Administration interface.

Choose Device > Phone .

Do one of the following to retrieve a list of phones:

- In the Find Capabilities Assignment where field, specify appropriate criteria  and click Find .

- To retrieve a list of all available users, click Find .

Choose the appropriate device name from the list.

The Phone Configuration window opens.

In the Association Information area, click the link for the appropriate line.

The Directory Number Configuration window opens.

In the Users Associated with Line area, choose Associate End Users .

The Find and List Users window opens.

Do one of the following to retrieve a list of users:

- In the Find Capabilities Assignment where field, specify the appropriate criteria and click Find .

- To retrieve a list of all available users, click Find .

Check the checkboxes for  the appropriate users from the list.

Click Add Selected .

In the Directory Number Configuration window, click Save .

#### Calendar Integration with Microsoft Outlook

The IM and Presence Service integrates with a Microsoft Exchange or Microsoft Office 365 deployment so that events in a user’s Microsoft Outlook calendar change the user’s availability status in the client application.

The IM and Presence Service supports calendar integration with either a Microsoft Exchange 2007, 2010, 2013, 2016 server, or a Microsoft Office 365 deployment.

For calendar integration with Office 365, you must be running a minimum IM and Presence Service Release of  11.5(1)SU3.

For configuration details, see Microsoft Outlook Calendar Integration for IM and Presence Service .

### Desk Phone Control Deployment

Computer Telephony Integration (CTI), or desk phone control,  allows users to control
                        		  their Cisco IP Phone through Cisco Jabber . To enable desk phone control, you  must set up a CTI UC service and assign it to a  service profile.

For configuration information, refer to the following configuration chapters in On-Premises Deployment for Cisco Jabber :

Configure CTI Service

Configure Deskphone Control

### Visual Voicemail Deployment

Cisco Unity Connection provides Cisco Jabber users with the ability to view, play, sort, and delete voicemail messages from the Cisco Jabber interface.

For details on how to configure voicemail, refer to the "Configure Voicemail" chapter of One-Premises Deployments for Cisco Jabber .

| Feature | Jabber for Windows | Jabber for Mac | Jabber IM for Android | Jabber IM for iPhone | Jabber for iPad | Jabber Web SDK |
|---|---|---|---|---|---|---|
| Core IM and Presence Features |
| Presence ( "Available," "Away," "Do not Disturb," "Offline" ) | X | X | X | X | X | X |
| Instant messaging | X | X | X | X | X | X |
| Multi-device (support for simultaneous login to multiple Cisco Jabber devices) | X | X | X | X | X | X |
| Group chat | X | X | X | X | X | X |
| File transfer | X | X | X | X | X |  |
| Emoticons | X | X | X | X | X | X |
| Contact search and retrieval including predictive search | X | X | X | X | X |  |
| Remote Call Control with Lync Server 2010, 2013 | X |  |  |  |  |  |
| Offline messages | X | X | X | X | X | X |
| Client history | X | X | X | X | X | X |
| Localization | X | X | X | X | X | X |
| Advanced IM Features |
| Interdomain federation 1 with Microsoft Skype for Business | X | X | X | X | X | X |
| Interdomain federation with XMPP-enabled Enterprises (Cisco, WebEx, multiple third parties) | X | X | X | X | X | X |
| Partitioned intradomain federation 2 with Microsoft Skype For Business | X | X | X | X | X | X |
| Start/join WebEx meetings | X |  | X | X | X | X |
| Visual Voicemail (Cisco Unity Connection customers) | X | X |  |  |  |  |
| Rich UC Presence Features |
| Cisco Telephony Presence Integration ( "On a call" ) | X | X | X | X | X | X |
| "In a meeting" Microsoft Outlook calendar integration (on-premise Exchange or hosted Office 365) | X | X | X | X | X | X |
| Desk Phone Control (for Cisco Phones) |
| Desktop Phone Control | X | X |  |  |  |  |
| Visual Voicemail |
| Visual Voicemail (Cisco Unity Connection customers) | X | X |  |  |  |  |
| Mobile and Remote Access |
| Presence and instant messaging through Cisco Expressway | X | X | X | X | X | X |
| 1 Interdomain federation enables IM and Presence Service client users in one enterprise domain to exchange presence information and IM with users in external domains. 2 Partitioned intradomain federation enables IM and Presence Service client users and Microsoft Skype for Business users within the same enterprise domain to exchange presence information and
                                    IM. |

| Note | IM and Presence Service is an integrated service, therefore all Cisco Unified Communications Manager users have access to IM as part of the core user licensing. |
|---|---|

| Customer | SKU |
|---|---|
| CUWL Customer |
| New or upgraded customer of IM and Presence Service , Release 11.5(1), 12.0(1) or 12.5(1). | Order new JABBER-IM-ADDON under the Presence on-premise CUWL options, where clients are selected to request IM for the number of non- Cisco Unified Communications Manager users. |
| Existing customer of IM and Presence Service Release 11.5(1), 12.0(1) or 12.5(1). | Order new JABBER-IM-ADDON standalone SKU   to request IM for the number of non- Cisco Unified Communications Manager users. For e-delivery, use R-JABBER-ADDON-K9 . For physical delivery, use JABBER-ADDON-K9 . |
| Cisco Unified Communications Manager UCL Customer |
| New or upgraded customer of IM and Presence Service , Release 11.5(1), 12.0(1) and 12.5(1). | Order new JABBER-IM-ADDON within the UCL configuration (CUCM-USR-LIC) to request IM for the number of non- Cisco Unified Communications Manager users
                                    . |
| Existing customer of IM and Presence Service Release 11.5(1), 12.0(1) and 12.5(1). | Order new JABBER-IM-ADDON standalone SKU  to request IM for the number of non- Cisco Unified Communications Manager users. For e-delivery, use R-JABBER-ADDON-K9 . For physical delivery, use JABBER-ADDON-K9 . |

| Note | You can deploy "Jabber for Everyone" in a mixed cluster where you provision some users with only instant messaging and availability and other users with instant
                                    messaging and availability  along with audio capabilities. You should create separate service profiles for users that have only instant messaging and availability capabilities. If the
                                    service profile contains a CTI or Cisco CallManager Cisco IP Phone (CCMCIP) profile, the client attempts to retrieve device
                                    lists for users from Cisco Unified Communications Manager . If no device lists exist for users, the client continually requests device lists from the node. As a result, the node consumes
                                    additional CPU resources. |
|---|---|

| Note | Jabber for Everyone is also supported in Centralized Deployments of the IM and Presence Service. To use this option, you must
                                    be running a minimum IM and Presence Service release of 11.5(1)SU4. |
|---|---|

| Step 1 | Add users to Cisco Unified Communications Manager using one of the following methods: Table 3. Provisioning Methods to Add IM and Presence Users Provisioning Method Details Add users via LDAP Directory Sync Add users to the database by syncing users from a company LDAP directory. Complete the following high-level tasks: Configure UC Services such as IM and Presence Service, Voicemail, Drectory  and Jabber config file (for optional Jabber feature
                                                         customization). Add your UC services to a Service Profile and add the Service Profile to a Feature Group Template. Add the Service Profile to a Feature Group Template. Configure an LDAP Directory sync that includes the Feature Group Template that you configured, and which also assigns users
                                                         to the Standard CCM End Users access control group. Complete an LDAP sync. For configuration details, refer to configuring and provisioning end users sections in the System Configuration Guide for Cisco Unified Communications Manager . Add users via Bulk Administration Add multiple users from a csv file with the Bulk Administration Tool. In Unified CM, configure UC services such as voicemail, directory access, IM and Presence Servie, and Jabber config files
                                                         (for Jabber features). In Unified CM, add UC Services to a Service Profile. Download the BAT.xlt spreadsheet and use it to create a csv file with your end users. For the Service Profile , make sure to assign the IM and Presence-enabled profile that you set up. Use Bulk Administration to import the end users into the database. For details on how to configure Service Profiles, see System Configuration Guide for Cisco Unified Communications Manager . For details on how to use the BAT spreadsheet to import users into the database, see the “User Additions” chapter in the Bulk Administration Guide for Cisco Unified Communications Manager . Add users manually Add individual users manually. See the “Manage End Users” chapter of the Administration Guide for Cisco Unified Communications Manager for instructions on manually adding individual users. | Provisioning Method | Details | Add users via LDAP Directory Sync | Add users to the database by syncing users from a company LDAP directory. Complete the following high-level tasks: Configure UC Services such as IM and Presence Service, Voicemail, Drectory  and Jabber config file (for optional Jabber feature
                                                         customization). Add your UC services to a Service Profile and add the Service Profile to a Feature Group Template. Add the Service Profile to a Feature Group Template. Configure an LDAP Directory sync that includes the Feature Group Template that you configured, and which also assigns users
                                                         to the Standard CCM End Users access control group. Complete an LDAP sync. For configuration details, refer to configuring and provisioning end users sections in the System Configuration Guide for Cisco Unified Communications Manager . | Add users via Bulk Administration | Add multiple users from a csv file with the Bulk Administration Tool. In Unified CM, configure UC services such as voicemail, directory access, IM and Presence Servie, and Jabber config files
                                                         (for Jabber features). In Unified CM, add UC Services to a Service Profile. Download the BAT.xlt spreadsheet and use it to create a csv file with your end users. For the Service Profile , make sure to assign the IM and Presence-enabled profile that you set up. Use Bulk Administration to import the end users into the database. For details on how to configure Service Profiles, see System Configuration Guide for Cisco Unified Communications Manager . For details on how to use the BAT spreadsheet to import users into the database, see the “User Additions” chapter in the Bulk Administration Guide for Cisco Unified Communications Manager . | Add users manually | Add individual users manually. See the “Manage End Users” chapter of the Administration Guide for Cisco Unified Communications Manager for instructions on manually adding individual users. |
|---|---|---|---|---|---|---|---|---|---|
| Provisioning Method | Details |
| Add users via LDAP Directory Sync | Add users to the database by syncing users from a company LDAP directory. Complete the following high-level tasks: Configure UC Services such as IM and Presence Service, Voicemail, Drectory  and Jabber config file (for optional Jabber feature
                                                         customization). Add your UC services to a Service Profile and add the Service Profile to a Feature Group Template. Add the Service Profile to a Feature Group Template. Configure an LDAP Directory sync that includes the Feature Group Template that you configured, and which also assigns users
                                                         to the Standard CCM End Users access control group. Complete an LDAP sync. For configuration details, refer to configuring and provisioning end users sections in the System Configuration Guide for Cisco Unified Communications Manager . |
| Add users via Bulk Administration | Add multiple users from a csv file with the Bulk Administration Tool. In Unified CM, configure UC services such as voicemail, directory access, IM and Presence Servie, and Jabber config files
                                                         (for Jabber features). In Unified CM, add UC Services to a Service Profile. Download the BAT.xlt spreadsheet and use it to create a csv file with your end users. For the Service Profile , make sure to assign the IM and Presence-enabled profile that you set up. Use Bulk Administration to import the end users into the database. For details on how to configure Service Profiles, see System Configuration Guide for Cisco Unified Communications Manager . For details on how to use the BAT spreadsheet to import users into the database, see the “User Additions” chapter in the Bulk Administration Guide for Cisco Unified Communications Manager . |
| Add users manually | Add individual users manually. See the “Manage End Users” chapter of the Administration Guide for Cisco Unified Communications Manager for instructions on manually adding individual users. |
| Step 2 | If you haven't already assigned users to the Standard CCM End Users access control group, do so now. See the “Assign Users to Access Control Groups” section in the Cisco Unified Communications Manager Administration Guide for instructions on assigning users to a user group. |

| Provisioning Method | Details |
|---|---|
| Add users via LDAP Directory Sync | Add users to the database by syncing users from a company LDAP directory. Complete the following high-level tasks: Configure UC Services such as IM and Presence Service, Voicemail, Drectory  and Jabber config file (for optional Jabber feature
                                                         customization). Add your UC services to a Service Profile and add the Service Profile to a Feature Group Template. Add the Service Profile to a Feature Group Template. Configure an LDAP Directory sync that includes the Feature Group Template that you configured, and which also assigns users
                                                         to the Standard CCM End Users access control group. Complete an LDAP sync. For configuration details, refer to configuring and provisioning end users sections in the System Configuration Guide for Cisco Unified Communications Manager . |
| Add users via Bulk Administration | Add multiple users from a csv file with the Bulk Administration Tool. In Unified CM, configure UC services such as voicemail, directory access, IM and Presence Servie, and Jabber config files
                                                         (for Jabber features). In Unified CM, add UC Services to a Service Profile. Download the BAT.xlt spreadsheet and use it to create a csv file with your end users. For the Service Profile , make sure to assign the IM and Presence-enabled profile that you set up. Use Bulk Administration to import the end users into the database. For details on how to configure Service Profiles, see System Configuration Guide for Cisco Unified Communications Manager . For details on how to use the BAT spreadsheet to import users into the database, see the “User Additions” chapter in the Bulk Administration Guide for Cisco Unified Communications Manager . |
| Add users manually | Add individual users manually. See the “Manage End Users” chapter of the Administration Guide for Cisco Unified Communications Manager for instructions on manually adding individual users. |

| Note | Cisco recommends that you use the touchless installation method to install your system using an answer file. This method lets
                                    you define configuration values before initializing the installation process, which provides an automated installation and
                                    helps ensure a successful installation. |
|---|---|

| Note | Most services automatically activate and start when you install the node. However, you should verify that the services that
                                       are listed in the following procedure are in a started state before you proceed with any other deployment tasks. |
|---|---|

| Step 1 | Verify that the Cisco AXL Web Service feature service is activated and in a started state on Cisco Unified Communications Manager : Note For procedures on how to activate feature services, see the “Services” chapter in the Cisco Unified Serviceability Administration Guide . | Note | For procedures on how to activate feature services, see the “Services” chapter in the Cisco Unified Serviceability Administration Guide . |
|---|---|---|---|
| Note | For procedures on how to activate feature services, see the “Services” chapter in the Cisco Unified Serviceability Administration Guide . |
| Step 2 | Verify that the following feature services are activated and  started on the IM and Presence Service : Cisco Presence Engine Cisco Sync Agent Cisco XCP Connection Manager Cisco XCP Authentication Service Cisco XCP Text Conference Manager |
| Step 3 | Verify that all network services on IM and Presence Service are activated and started. |

| Note | For procedures on how to activate feature services, see the “Services” chapter in the Cisco Unified Serviceability Administration Guide . |
|---|---|

| Step 1 | Log in to the Cisco Unified Communications Manager Administration interface. |
|---|---|
| Step 2 | Choose User Management > End User . |
| Step 3 | Use the filters to the find the user that you want to enable for the IM and Presence Service . The user configuration displays in the End User Configuration window. |
| Step 4 | Configure the following options in the End User Configuration window. Enable User for Unified CM IM and Presence —Check this check box to turn the IM and Presence Service on for this user. Include meeting information in presence —Check this optional check box if you want to enable calendar integration with Microsoft Outlook for this user. Service Profile —Make sure that the service profile that you configured for the IM and Presence Service is selected. |
| Step 5 | Click Save . |

| Note | If you have a large group of existing users for whom you want to enable IM and Presence, you can use the Update Users feature
                                       of Bulk Administration to check the check box in the above procedure for all of those users. See the "User Updates" chapter
                                       of the Bulk Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | Review configuration parameters for Cisco Jabber. Note In most environments, Cisco Jabber for Windows does not require any configuration and can connect automatically to the IM and Presence Service and Microsoft Active Directory . Before you create a configuration file, review the default configuration parameters to determine if your deployment requires
                                                   any configuration. For a detailed list of parameters that are available with Jabber configuration files, refer to Parameters Reference Guide for Cisco Jabber . | Note | In most environments, Cisco Jabber for Windows does not require any configuration and can connect automatically to the IM and Presence Service and Microsoft Active Directory . Before you create a configuration file, review the default configuration parameters to determine if your deployment requires
                                                   any configuration. |
|---|---|---|---|
| Note | In most environments, Cisco Jabber for Windows does not require any configuration and can connect automatically to the IM and Presence Service and Microsoft Active Directory . Before you create a configuration file, review the default configuration parameters to determine if your deployment requires
                                                   any configuration. |
| Step 2 | (Optional) Complete the following steps if your deployment requires configuration: Create the configuration files. Host the configuration files on your TFTP server. Restart the TFTP service on Cisco Unified Communications Manager . You must restart the TFTP service on each node where you host a configuration file. Refer to the "Create and Host the Client Configuration Files" task flow in the "Configure the Clients" chapter of On-Premises Deployment for Cisco Jabber : |
| Step 3 | Install Cisco Jabber . See the “Deploy Cisco Jabber Applications” chapter of On-Premises Deployment for Cisco Jabber for installation instructions. |

| Note | In most environments, Cisco Jabber for Windows does not require any configuration and can connect automatically to the IM and Presence Service and Microsoft Active Directory . Before you create a configuration file, review the default configuration parameters to determine if your deployment requires
                                                   any configuration. |
|---|---|

| Note | For additional information on Jabber feature configuration, refer to Feature Configuration for Cisco Jabber . |
|---|---|

| Step 1 | Set up a web server. |
|---|---|
| Step 2 | Download the CAXL library from the Cisco Developer Network. |
| Step 3 | Extract the contents of the CAXL library to the working directory of your website. |
| Step 4 | Implement the required HTML with JavaScript objects to send and receive XMPP messages. |

| Step 1 | Configure the SIP trunk on Cisco Unified Communications Manager . For instructions, see the "SIP Trunk Configuration on Cisco Unified Communications Manager " section in Configuration and Administration of the IM and Presence Service . |
|---|---|
| Step 2 | Choose the SIP publish trunk on IM and Presence. Log in to the Cisco Unified Communications Manager IM and Presence Administration interface. Choose Presence > Settings . From the CUCM SIP Publish Trunk drop-down list, choose the SIP publish trunk. Click Save . |

| Step 1 | Log in to the Cisco Unified Communications Manager IM and Presence Administration interface. |
|---|---|
| Step 2 | Choose Presence > Gateways . |
| Step 3 | Click Add New . |
| Step 4 | From the Presence Gateway Type drop-down list, choose CUCM . |
| Step 5 | In the Description field, enter a description. |
| Step 6 | In the Presence Gateway field, specify one of the following values: IP address of the Cisco Unified Communications Manager publisher node. Fully qualified domain name (FQDN) of the Cisco Unified Communications Manager publisher node. DNS SRV FQDN that resolves to the Cisco Unified Communications Manager subscriber nodes. |
| Step 7 | Click Save . For more information about configuring a Presence Gateway, see Configuration and Administration of IM and Presence Service . |

| Step 1 | Log in to  the Cisco Unified Communications Manager Administration interface. |
|---|---|
| Step 2 | Choose Device > Phone . |
| Step 3 | Do one of the following to retrieve a list of phones: In the Find Capabilities Assignment where field, specify appropriate criteria  and click Find . To retrieve a list of all available users, click Find . |
| Step 4 | Choose the appropriate device name from the list. The Phone Configuration window opens. |
| Step 5 | In the Association Information area, click the link for the appropriate line. The Directory Number Configuration window opens. |
| Step 6 | In the Users Associated with Line area, choose Associate End Users . The Find and List Users window opens. |
| Step 7 | Do one of the following to retrieve a list of users: In the Find Capabilities Assignment where field, specify the appropriate criteria and click Find . To retrieve a list of all available users, click Find . |
| Step 8 | Check the checkboxes for  the appropriate users from the list. |
| Step 9 | Click Add Selected . |
| Step 10 | In the Directory Number Configuration window, click Save . |

| Note | The IM and Presence Service supports calendar integration with either a Microsoft Exchange 2007, 2010, 2013, 2016 server, or a Microsoft Office 365 deployment. For calendar integration with Office 365, you must be running a minimum IM and Presence Service Release of  11.5(1)SU3. |
|---|---|