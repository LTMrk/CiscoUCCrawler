---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-cup0-b-config-and-admin-guide-1251--a69ba22b49
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1/cup0_b_config-and-admin-guide-1251/cup0_b_config-and-admin-guide-1251_chapter_00.html
retrieved_at: 2026-08-16T16:40:13.238031+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)

Updated: November 27, 2024

Chapter: Plan the System

## Chapter: Plan the System

# Plan the System

## IM and Presence Service Overview

IM and Presence Service Administration is a web-based application that allows you to make individual, manual configuration
                           changes to the IM and Presence Service nodes. The procedures in this guide describe how to configure features using this application.

IM and Presence Service offers a choice of either rich-featured Cisco Jabber Unified Communications clients or any third-party
                           XMPP-compliant IM and presence client. IM and Presence Service also provides instant messaging, file transfer, and has the
                           ability to host and configure persistent Group Chat Rooms.

In an on-premises deployment with IM and Presence Service and Cisco Unified Communications Manager, the following services
                           are available:

Presence

Instant messaging

File Transfers

Audio Calls

Video

Voicemail

Conferencing

See Cisco Unified Communications Manager documentation for more.

### IM and Presence Service Components

The following figure provides an overview of an IM and Presence Service deployment, including the main components and interfaces
                                 between Cisco Unified Communications Manager and IM and Presence Service.

#### SIP Interface

You must configure the following to enable the SIP interface:

In Cisco Unified Communications Manager, you must configure a SIP trunk that points to the IM and Presence Service for the
                                       presence information exchange.

On the IM and Presence Service, configure Cisco Unified Communications Manager as a Presence Gateway so that IM and Presence
                                       Service can send SIP subscribe messages to Cisco Unified Communications Manager over the SIP trunk.

#### AXL/SOAP Interface

The AXL/SOAP interface handles the database synchronization from Cisco Unified Communications Manager and populates the IM
                                 and Presence Service database. To activate the database synchronization, the Cisco Sync Agent network service must be running..

By default, the Sync Agent load balances all users equally across all nodes within the IM and Presence Service cluster. However,
                                 you also have the option to manually assign users to a particular node in the cluster.

For guidelines on the recommended synchronization intervals when executing a database synchronization with Cisco Unified Communications
                                 Manager, for single and dual-node IM and Presence Service, see the IM and Presence Service SRND document.

The AXL interface is not supported for application developer interactions.

#### LDAP Interface

Cisco Unified Communications Manager obtains all user information via manual configuration or synchronization directly over
                                 LDAP. The IM and Presence Service then synchronizes all this user information from Cisco Unified Communications Manager (using
                                 the AXL/SOAP interface).

IM and Presence Service provides LDAP authentication for users of the Cisco Jabber client and IM and Presence Service user
                                 interface. If a Cisco Jabber user logs into IM and Presence Service, and LDAP authentication is enabled on Cisco Unified Communications
                                 Manager, IM and Presence Service goes directly to the LDAP directory for user authentication. When the user is authenticated,
                                 IM and Presence Service forwards this information to Cisco Jabber to continue the user login.

#### XMPP Interface

An XMPP connection handles the presence information exchange and instant messaging operations for XMPP-based clients. The
                                 IM and Presence Service supports ad hoc and persistent chat rooms for XMPP-based clients. An IM Gateway supports the IM interoperability
                                 between SIP-based and XMPP-based clients in an IM and Presence Service deployment.

#### CTI Interface

The CTI (Computer Telephony Integration) interface handles all the CTI communication for users on the IM and Presence node
                                 to control phones on Cisco Unified Communications Manager. The CTI functionality allows users of the Cisco Jabber client to
                                 run the application in desk phone control mode.

The CTI functionality is also used for the IM and Presence Service integration with Microsoft Lync for Remote Call Control
                                 (RCC). For information, see the Remote Call Control with Microsoft Lync Server for the IM and Presence Service .

To configure CTI functionality for IM and Presence Service users on Cisco Unified Communications Manager, users must be associated
                                 with a CTI-enabled group, and the primary extension assigned to that user must be enabled for CTI.

To configure Cisco Jabber desk phone control, you must configure a CTI server and profile, and assign any users that wish
                                 to use the application in desk phone mode to that profile. However, note that all CTI communication occurs directly between
                                 Cisco Unified Communications Manager and Cisco Jabber, and not through the IM and Presence Service node.

#### Cisco IM and Presence Data Monitor Service

The Cisco IM and Presence Data Monitor monitors the IDS replication state on the IM and Presence Service. Other IM and Presence
                                 services are dependent on the Cisco IM and Presence Data Monitor so that they can delay startup until  IDS replication is
                                 in a stable state.

The Cisco IM and Presence Data Monitor also checks the status of the Cisco Sync Agent sync from Cisco Unified Communications
                                 Manager. Dependent services are only allowed to start after IDS replication has set up and the Sync Agent on the IM and Presence
                                 database publisher node has completed its sync from Cisco Unified Communications Manager. After the timeout has been reached,
                                 the Cisco IM and Presence Data Monitor on the Publisher node will allow dependent services to start even if IDS replication
                                 and the Sync Agent have not completed.

On the subscriber nodes, the Cisco IM and Presence Data Monitor delays the startup of feature services until IDS replication
                                 is successfully established. The Cisco IM and Presence Data Monitor only delays the startup of feature services on the problem
                                 subscriber node in a cluster, it will not delay the startup of feature services on all subscriber nodes due to one problem
                                 node. For example, if IDS replication is successfully established on node1 and node2, but not on node3, the Cisco IM and Presence
                                 Data Monitor allows feature services to start on node1 and node2, but delays feature service startup on node3.

The Cisco IM and Presence Data Monitor behaves differently on the IM and Presence database publisher node. It only delays
                                 the startup of feature services until a timeout expires. When the timeout expires, it allows all feature services to start
                                 on the publisher node even if IDS replication is not successfully established.

The Cisco IM and Presence Data Monitor generates an alarm when it delays feature service startup on a node. It then generates
                                 a notification when IDS replication is successfully established on that node.

The Cisco IM and Presence Data Monitor impacts both a fresh multinode installation, and a software upgrade procedure. Both
                                 will only complete when the publisher node and subscriber nodes are running the same IM and Presence release, and IDS replication
                                 is successfully established on the subscriber nodes.

To check the status of the IDS replication on a node either:

Use this CLI command: utils dbreplication runtimestate

Use the Cisco Unified IM and Presence Reporting Tool. The “IM and Presence Database Status” report displays a detailed status
                                       of the cluster.

To check the status of the Cisco Sync Agent, navigate to the Cisco Unified CM IM and Presence Administration interface and
                                 select Diagnostics > System Dashboard. You will find the Cisco Unified Communications Manager publisher node IP address as
                                 well as the sync status.

## Planning Overview

Before you configure your system, make sure that you plan how you want to deploy your system. The IM and Presence Service
                              offers different deployment options that are designed to meet the needs of different companies.

For detailed information on how to design a Cisco Collaboration system that includes an IM and Presence Service deployment
                              that meets your needs, refer to the Cisco Collaboration System Solution Reference Network Design at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-implementation-design-guides-list.html .

## Plan Your Deployment

Before you configure your system, make sure that you plan your cluster topology and how you want to deploy your system.

Step 1

Size your Collaboration deployment

For information, refer to the "Collaboration Solution Sizing Guidance" chapter of the Cisco Collaboration System Solution
                                          Reference Network Design at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-implementation-design-guides-list.html .

Step 2

Determine which features you want to deploy.

For details, see Feature Deployment Options .

Step 3

Determine if you will install the standard deployment or an IM and Presence  central cluster deployment

Decide whether you want to deploy the IM and Presence Service on the same cluster as your telephony, or whether you want to
                                          deploy a centralized cluster for IM and Presence. For details, see Standard Deployment vs Centralized Cluster .

Step 4

Plan how many cluster nodes you want to deploy.

The IM and Presence multinode scalability features allow you to size your deployment to meet your needs. For details, see Multinode Scalability Requirements .

Step 5

Plan how you are going to add redundancy.

Scalability Options for Deployment

Step 6

Plan your geographic sites

You can install at a single site in order to maintain your hardware from a single location. However, you can also deploy your
                                          clusters over the WAN to add geographic redundancy with deploying multiple sites. For details, see:

Intracluster Deployments Over WAN

Intercluster Deployments Over WAN

Step 7

Plan the schema for Jabber identifiers (JIDs) for IM and Presence users.

For the allowed characters in the Jabber identifier (JID), please refer RFC 3920 (3. Addressing Scheme) and XEP-0106. Cisco
                                          Jabber and other 3 rd party XMPP clients may impose further restrictions for which the client-side documentation should be referred.

Step 8

Decide if you want to configure SAML Single-Sign On.

For details, see SAML Single Sign-On Deployments .

Step 9

Determine if you want to integrate with a third-party application.

This includes Microsoft Outlook calendar integration as well as federation with a third-party system. For details, see Third Party Integrations .

### IM and Presence Service Deployment Sizing

For information on how to size your Collaboration deployment, refer to the "Collaboration Solution Sizing Guidance" chapter
                                 of the Cisco Collaboration System Solution Reference Network Design at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-implementation-design-guides-list.html .

## Feature Deployment Options

Basic IM, availability, and ad hoc group chat are among the core features that are available after you install IM and Presence
                              Service and configure your users in a basic deployment.

You can add optional features to enhance a basic deployment. The following figure shows the IM and Presence Service feature
                              deployment options.

The following table lists the feature deployment options for IM and Presence Service.

Core IM and Availability Features

Advanced IM Features (optional)

Rich Unified Communications Availability features (optional)

Remote Desk Phone Control (optional)

View user availability

Securely send and receive rich text IMs

File transfers

Ad hoc group chat

Manage contacts

User history

Cisco Jabber support

Multiple client device support: Microsoft windows, MAC, Mobile, tablet, IOS, Android, BB

Microsoft Office integration

LDAP directory integration

Personal directory and buddy lists

Open APIs

System troubleshooting

Persistent chat

Managed File Transfer

Message Archiver

Calendaring Third-party XMPP client support

High availability

Scalability: multinode support and clustering over WAN

Intercluster peering

Enterprise federation:

IM and Presence Service integration

Cisco WebEx Messenger integration

Microsoft Lync/Skype for Business/Office365 server integration

IBM SameTime integration

Cisco Jabber XCP

Public federation:

Google Talk, AOL integration

XMMP services or BOTs

Third-party Exchange Service integration

IM Compliance

SAML Single Sign On

Custom login banner

Cisco telephony availability

Microsoft Outlook calendar integration (on-premise Exchange or hosted Office 365 deployments)

Remote Cisco IP Phone control

Remote Softphone Control

Microsoft Remote Call Control integration

## Standard Deployment vs Centralized Cluster

Before you even install your system, you must decide whether you want to deploy a standard deployment of the IM and Presence
                           Service or whether you want an IM and Presence Service central cluster as this will affect your topology and installation:

IM and Presence Service on Cisco Unified Communications Manager (Standard deployment)—In standard deployments, the IM and
                                 Presence Service cluster is installed on the same servers as the Cisco Unified Communications Manager telephonynodes. The
                                 IM and Presence cluster shares a platform and many of the same services as the telephony cluster. This option requires a 1x1
                                 mapping of telephony clusters to IM and Presence clusters.

Centralized IM and Presence cluster—In this deployment, the IM and Presence Service cluster is installed separately from your
                                 telephony cluster. Depending on how you plan your topology, the IM and Presence central cluster may be located on completely
                                 different hardware servers from your telephony cluster. This deployment option removes the 1x1 mapping requirement of telephony
                                 clusters and IM and Presence clusters, which allows you to better scale each deployment type to its own needs.

The IM and Presence central cluster still has an instance of Cisco Unified Communications Manager. However, this instance
                                       is for user provisioning and database and does not handle telephony. For telephony integration, the IM and Presence central
                                       cluster must connect to a separate Cisco Unified Communictions Manager telephony cluster.

The procedures in this document can be used for both standard deployments and central cluster deployments. However, for central
                           cluster deployments, you must also complete the tasks in the Configure Centralized Deployment , chapter to properly align your telephony cluster and IM and Presence cluster.

## Multinode Scalability Feature

### Multinode Scalability Requirements

IM and Presence Service supports multinode scalability:

Six nodes per cluster

75,000 users per cluster with a maximum of 25,000 users per node in a full Unified Communication (UC) mode deployment

25,000 users in a presence redundancy group, and 75,000 users per cluster in a deployment with High Availability.

Administrable customer-defined limit on the maximum contacts per user (default unlimited)

The IM and Presence Service continues to support intercluster deployments with the multinode feature.

### OVA Requirements

The following OVA requirements apply:

For intercluster deployments, you must deploy a minimum OVA of 15,000 users. It is possible to have different clusters running
                                       different OVA sizes so long as all clusters are running at least the 15,000 user OVA.

For Persistent Chat deployments, we recommend that you deploy a minimum OVA of 15,000 users.

For Centralized Deployments, we recommend the 25,000 user IM and Presence OVA with a minimum OVA of 15,000 users. The 15,000
                                       user OVA can grow to 25,000 users. With a 25K OVA template, and a six-node cluster with High Availability enabled, the IM
                                       and Presence Service central deployment supports up to 75,000 clients. To support 75K users with 25K OVA, default trace level
                                       for XCP router needs to be changed from Info to Error . For the Unified Communications Manager publisher node in the central cluster, the following requirements apply:

A 25,000 IM and Presence OVA (maximum 75,000 users) can be deployed with a 10,000 user OVA installed on the central cluster's
                                             Unified Communications Manager publisher node

A 15,000 IM and Presence OVA (maximum 45,000 users) can be deployed with a 7,500 user OVA installed on the central cluster's
                                             Unified Communications Manager publisher node

Scalability depends on the number of clusters in your deployment. For detailed VM configuration requirements and OVA templates,
                                 see Virtualization for Unified CM IM and Presence at the following url: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-ucm-im-presence.html .

### Scalability Options for Deployment

IM and Presence Service clusters can support up to six nodes. If you originally installed less than six nodes, then you can
                                 install additional nodes at any time. If you want to scale your IM and Presence Service deployment to support more users,
                                 you must consider the multinode deployment model you have configured. The following table describes the scalability options
                                 for each multinode deployment model.

Deployment Mode

Scalability Option

Add a New Node to an Existing Presence Redundancy Group

Add a New Node to a New Presence

Redundancy Group

Balanced Non-Redundant High Availability Deployment

If you add a new node to an existing presence redundancy group, the new node can support the same number of users as the existing
                                             node; the presence redundancy group can now support twice the number of users. It also provides balanced High Availability
                                             for the users on the existing node and the new node in that presence redundancy group.

If you add a new node to a new presence redundancy group, you can support more users in your deployment.

This does not provide balanced High Availability for the users in the presence redundancy group. To provide balanced High
                                             Availability, you must add a second node to the presence redundancy group.

Balanced Redundant High Availability Deployment

If you add a new node to an existing presence redundancy group, the new node can support the same users as the existing node.
                                             For example, if the existing node supports 5000 users, the new node supports the same 5000 users. It also provides balanced
                                             redundant High Availability for the users on the existing node and the new node in that presence redundancy group.

You may have to reassign your users within the presence redundancy group, depending how many users were on the existing node.

If you add a new node to a new presence redundancy group, you can support more users in your deployment.

This does not provide balanced High Availability for the users in the presence redundancy group. To provide balanced High
                                             Availability, you must add a second node to the presence redundancy group.

Active/Standby Redundant High Availability Deployment

If you add a new node to an existing presence redundancy group, you provide High Availability for the users in the existing
                                             node in the presence redundancy group. This provides a High Availability enhancement only; it does not increase the number
                                             of users you can support in your deployment.

If you add a new node in a new presence redundancy group, you can support more users in your deployment.

This does not provide High Availability for the users in the presence redundancy group. To provide High Availability, you
                                             must add a second node to the presence redundancy group.

## WAN Deployments

IM and Presence Service supports Clustering over WAN for both intracluster and intercluster deployments. This option allows
                           you to add geographic redundancy to your deployment.

### Intracluster Deployments Over WAN

IM and Presence Service supports intracluster deployments over WAN, using the bandwidth recommendations provided in this module.
                              IM and Presence Service supports a single presence redundancy group geographically split over WAN, where one node in the presence
                              redundancy group is in one geographic site and the second node in the presence redundancy group is in another geographic location.

This model can provide geographical redundancy and remote failover, for example failover to a backup IM and Presence Service
                              node on a remote site. With this model, the IM and Presence Service node does not need to be co-located with the Cisco Unified
                              Communications Manager database publisher node. The Cisco Jabber client can be either local or remote to the IM and Presence
                              Service node.

This model also supports High Availability for the clients, where the clients fail over to the remote peer IM and Presence
                              Service node if the services or hardware fails on the home IM and Presence Service node. When the failed node comes online
                              again, the clients automatically reconnect to the home IM and Presence Service node.

When you deploy IM and Presence Service over WAN with remote failover, note the following restriction:

This model only supports High Availability at the system level. Certain IM and Presence Service components may still have
                                    a single point of failure. These components are the Cisco Sync Agent, Cisco Intercluster Sync Agent, and Cisco Unified CM
                                    IM and Presence Administration interface.

IM and Presence Service also supports multiple presence redundancy groups in a Clustering over WAN deployment. For information
                              about scale for a Clustering over WAN deployment, see the IM and Presence Service SRND.

For additional information, see the IM and Presence Service Solution Reference Network Design (SRND).

#### Multinode Configuration for Deployment Over WAN

When you configure the IM and Presence Service multinode feature for an intracluster deployment over WAN, configure the IM
                                 and Presence Service presence redundancy group, nodes and user assignment as described in the multinode section, but note
                                 the following recommendations:

For optimum performance, Cisco recommends that you assign the majority of your users to the home IM and Presence Service node.
                                       This deployment model decreases the volume of messages sent to the remote IM and Presence Service node over WAN, however the
                                       failover time to the secondary node depends on the number of users failing over.

If you wish to configure a High Availability deployment model over WAN, you can configure a presence redundancy group-wide
                                       DNS SRV address. In this case, IM and Presence Service sends the initial PUBLISH request message to the node specified by
                                       DNS SRV and the response message indicates the host node for the user. IM and Presence Service then sends all subsequent PUBLISH
                                       messages for that user to the host node. Before configuring this High Availability deployment model, you must consider if
                                       you have sufficient bandwidth for the potential volume of messages that may be sent over the WAN.

### Intercluster Deployments Over WAN

IM and Presence Service supports intercluster deployments over WAN, using the bandwidth recommendations provided in this module.
                              The considerations apply when deploying intercluster deployments:

Intercluster Peers—You can configure peer relationships that interconnect standalone IM and Presence Service clusters, known
                                    as intercluster peers. This intercluster peer functionality allows users in one IM and Presence Service cluster to communicate
                                    and subscribe to the availability information of users in a remote IM and Presence Service cluster within the same domain.
                                    For details on how to set up intercluster peers, see Configure Intercluster Peers .

Node Names—The node name that you define for any IM and Presence Service node must be resolvable by every other IM and Presence
                                    Service node on every cluster. Therefore, each IM and Presence Service node name must be the FQDN of the node. If DNS is not
                                    deployed in your network, each node name must be an IP address.

IM Address Scheme—For intercluster deployments, all nodes in each of the clusters must use the same IM address scheme. If
                                    any node in a cluster is running a version of IM and Presence Service that is earlier than Release 10, all nodes must be set
                                    to use the UserID@Default_Domain IM address scheme for backward compatibility.

Router-to-Router Communications—By default, IM and Presence Service assigns all nodes in a cluster as intercluster router-to-router
                                    connectors. When IM and Presence Service establishes an intercluster peer connection between the clusters over the AXL interface,
                                    it synchronizes the information from all intercluster router-to-router connector nodes in the home and remote clusters.

You can also configure secure router-to-router communications that use TLS to secure the connection between each router-to-router
                                    connector node in the local cluster, and each router connector node in the remote cluster.

## SAML Single Sign-On Deployments

The Security Assertion Markup Language (SAML)
                              Single Sign-On feature allows administrative users to access a
                              number of Cisco Collaboration applications, including the IM and
                              Presence Service, after signing into only one of those
                              applications. This feature simplifies the administrator's
                              job in the following ways:

A single login is required to access a number of Cisco Collaboration
                                    applications after a single sign-in.

Only one password is required–there's no longer any need to
                                    remember different passwords for each application.

Administrators can manage all passwords and
                                    authentication from a single Identity Provider (IdP).

For details on how to setup and configure SAML
                              Single Sign-On, see the SAML SSO Deployment Guide for Cisco Unified
                                 Communications Solutions at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Third Party Integrations

The IM and Presence Service integrates with a variety of third-party systems. The following table outlines the integrations
                           and provides a link to the document that describes how to configure it.

Guide Title

This Guide Contains ...

Microsoft Outlook Calendar Integration for the IM and Presence Service

Configure the IM and Presence Service to connect with an on-premise Microsoft Exchange server or a hosted Office 365 server
                                       in order to use calendar information from Microsoft Outlook in an IM and Presence user's Presence status.

Interdomain Federation for the IM and Presence Service

Configure the IM and Presence Service for interdomain federation with the following systems. This allows IM and Presence users
                                       to exchange IM and Presence with users on the other system.

Microsoft Lync

Microsoft Skype for Business

Microsoft Office 365

GoogleTalk

AOL

IBM SameTime

Cisco WebEx Messenger

another IM and Presence Service enterprise

Partitioned Intradomain Federation for the IM and Presence Service

Configuring the IM and Presence Service for Partitioned Intradomain Federation with Microsoft Lync or Skype for Business.
                                       You can use this integration to maintain communications within your network while you are in the process of migrating users
                                       to the IM and Presence Service.

Remote Call Control with Microsoft Lync Server for the IM and Presence Service

Configure Cisco Unified Communications Manager and IM and Presence Service for integration with Microsoft Lync for Microsoft
                                       Remote Call Control (RCC). This integration allows enterprise users to control their Cisco Unified IP Phone or Cisco IP Communicator
                                       Phone through Microsoft Lync, a third-party desktop instant-messaging (IM) application.

## Third Party Client Integration

This section outlines some of the requirements for third-party client integrations.

### Supported Third-Party XMPP Clients

IM and Presence Service supports standards-based XMPP to enable third-party XMPP client applications to integrate with IM
                              and Presence Service for availability and instant messaging (IM) services. Third-party XMPP clients must comply with the XMPP
                              standard as outlined in the Cisco Software Development Kit (SDK).

This module describes the configuration requirements for integrating XMPP clients with IM and Presence Service. If you are
                              integrating XMPP-based API (web) client applications with IM and Presence Service, also see developer documentation for IM
                              and Presence Service APIs on the Cisco Developer Portal:

http://developer.cisco.com/

### License Requirements

You must assign IM and Presence Service capabilities for each user of an XMPP client application. IM and Presence capabilities
                              are included within both User Connect Licensing (UCL) and Cisco Unified Workspace Licensing (CUWL).

For additional information on licensing, see the "Smart Software   Licensing" chapter of the System Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

### XMPP Client Integration on Cisco Unified Communications Manager

Before you integrate an XMPP client, perform the following tasks on Cisco Unified Communications Manager:

Configure the licensing requirements.

Configure the users and devices. Associate a device with each user, and associate each user with a line appearance.

### LDAP Integration for XMPP Contact Search

To allow users of the XMPP client applications to search and add contacts from an LDAP directory, configure the Third-Party
                              LDAP settings for XMPP clients on IM and Presence Service.

### DNS Configuration for XMPP Clients

You must enable DNS SRV in your deployment when you integrate XMPP clients with IM and Presence Service. The XMPP client performs
                              a DNS SRV query to find an XMPP node (IM and Presence Service) to communicate with, and then performs a record lookup of the
                              XMPP node to get the IP address.

| Note | The AXL interface is not supported for application developer interactions. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Size your Collaboration deployment | For information, refer to the "Collaboration Solution Sizing Guidance" chapter of the Cisco Collaboration System Solution
                                          Reference Network Design at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-implementation-design-guides-list.html . |
| Step 2 | Determine which features you want to deploy. | For details, see Feature Deployment Options . |
| Step 3 | Determine if you will install the standard deployment or an IM and Presence  central cluster deployment | Decide whether you want to deploy the IM and Presence Service on the same cluster as your telephony, or whether you want to
                                          deploy a centralized cluster for IM and Presence. For details, see Standard Deployment vs Centralized Cluster . |
| Step 4 | Plan how many cluster nodes you want to deploy. | The IM and Presence multinode scalability features allow you to size your deployment to meet your needs. For details, see Multinode Scalability Requirements . |
| Step 5 | Plan how you are going to add redundancy. | Scalability Options for Deployment |
| Step 6 | Plan your geographic sites | You can install at a single site in order to maintain your hardware from a single location. However, you can also deploy your
                                          clusters over the WAN to add geographic redundancy with deploying multiple sites. For details, see: Intracluster Deployments Over WAN Intercluster Deployments Over WAN |
| Step 7 | Plan the schema for Jabber identifiers (JIDs) for IM and Presence users. | For the allowed characters in the Jabber identifier (JID), please refer RFC 3920 (3. Addressing Scheme) and XEP-0106. Cisco
                                          Jabber and other 3 rd party XMPP clients may impose further restrictions for which the client-side documentation should be referred. |
| Step 8 | Decide if you want to configure SAML Single-Sign On. | For details, see SAML Single Sign-On Deployments . |
| Step 9 | Determine if you want to integrate with a third-party application. | This includes Microsoft Outlook calendar integration as well as federation with a third-party system. For details, see Third Party Integrations . |

| Core IM and Availability Features | Advanced IM Features (optional) | Rich Unified Communications Availability features (optional) | Remote Desk Phone Control (optional) |
|---|---|---|---|
| View user availability Securely send and receive rich text IMs File transfers Ad hoc group chat Manage contacts User history Cisco Jabber support Multiple client device support: Microsoft windows, MAC, Mobile, tablet, IOS, Android, BB Microsoft Office integration LDAP directory integration Personal directory and buddy lists Open APIs System troubleshooting | Persistent chat Managed File Transfer Message Archiver Calendaring Third-party XMPP client support High availability Scalability: multinode support and clustering over WAN Intercluster peering Enterprise federation: IM and Presence Service integration Cisco WebEx Messenger integration Microsoft Lync/Skype for Business/Office365 server integration IBM SameTime integration Cisco Jabber XCP Public federation: Google Talk, AOL integration XMMP services or BOTs Third-party Exchange Service integration IM Compliance SAML Single Sign On Custom login banner | Cisco telephony availability Microsoft Outlook calendar integration (on-premise Exchange or hosted Office 365 deployments) | Remote Cisco IP Phone control Remote Softphone Control Microsoft Remote Call Control integration |

| Note | The IM and Presence central cluster still has an instance of Cisco Unified Communications Manager. However, this instance
                                       is for user provisioning and database and does not handle telephony. For telephony integration, the IM and Presence central
                                       cluster must connect to a separate Cisco Unified Communictions Manager telephony cluster. |
|---|---|

| Note | If you plan to enable Multiple Device Messaging, measure deployments by the number of clients instead of the number of users
                                          as each user may have multiple Jabber clients. For example, if you have 25,000 users, and each user has two Jabber clients,
                                          your deployment requires the capacity of 50,000 users. |
|---|---|

| Deployment Mode | Scalability Option |
|---|---|
| Add a New Node to an Existing Presence Redundancy Group | Add a New Node to a New Presence Redundancy Group |
| Balanced Non-Redundant High Availability Deployment | If you add a new node to an existing presence redundancy group, the new node can support the same number of users as the existing
                                             node; the presence redundancy group can now support twice the number of users. It also provides balanced High Availability
                                             for the users on the existing node and the new node in that presence redundancy group. | If you add a new node to a new presence redundancy group, you can support more users in your deployment. This does not provide balanced High Availability for the users in the presence redundancy group. To provide balanced High
                                             Availability, you must add a second node to the presence redundancy group. |
| Balanced Redundant High Availability Deployment | If you add a new node to an existing presence redundancy group, the new node can support the same users as the existing node.
                                             For example, if the existing node supports 5000 users, the new node supports the same 5000 users. It also provides balanced
                                             redundant High Availability for the users on the existing node and the new node in that presence redundancy group. Note You may have to reassign your users within the presence redundancy group, depending how many users were on the existing node. | Note | You may have to reassign your users within the presence redundancy group, depending how many users were on the existing node. | If you add a new node to a new presence redundancy group, you can support more users in your deployment. This does not provide balanced High Availability for the users in the presence redundancy group. To provide balanced High
                                             Availability, you must add a second node to the presence redundancy group. |
| Note | You may have to reassign your users within the presence redundancy group, depending how many users were on the existing node. |
| Active/Standby Redundant High Availability Deployment | If you add a new node to an existing presence redundancy group, you provide High Availability for the users in the existing
                                             node in the presence redundancy group. This provides a High Availability enhancement only; it does not increase the number
                                             of users you can support in your deployment. | If you add a new node in a new presence redundancy group, you can support more users in your deployment. This does not provide High Availability for the users in the presence redundancy group. To provide High Availability, you
                                             must add a second node to the presence redundancy group. |

| Note | You may have to reassign your users within the presence redundancy group, depending how many users were on the existing node. |
|---|---|

| Guide Title | This Guide Contains ... |
|---|---|
| Microsoft Outlook Calendar Integration for the IM and Presence Service | Configure the IM and Presence Service to connect with an on-premise Microsoft Exchange server or a hosted Office 365 server
                                       in order to use calendar information from Microsoft Outlook in an IM and Presence user's Presence status. |
| Interdomain Federation for the IM and Presence Service | Configure the IM and Presence Service for interdomain federation with the following systems. This allows IM and Presence users
                                       to exchange IM and Presence with users on the other system. Microsoft Lync Microsoft Skype for Business Microsoft Office 365 GoogleTalk AOL IBM SameTime Cisco WebEx Messenger another IM and Presence Service enterprise |
| Partitioned Intradomain Federation for the IM and Presence Service | Configuring the IM and Presence Service for Partitioned Intradomain Federation with Microsoft Lync or Skype for Business.
                                       You can use this integration to maintain communications within your network while you are in the process of migrating users
                                       to the IM and Presence Service. |
| Remote Call Control with Microsoft Lync Server for the IM and Presence Service | Configure Cisco Unified Communications Manager and IM and Presence Service for integration with Microsoft Lync for Microsoft
                                       Remote Call Control (RCC). This integration allows enterprise users to control their Cisco Unified IP Phone or Cisco IP Communicator
                                       Phone through Microsoft Lync, a third-party desktop instant-messaging (IM) application. |

| Note | If you have multiple IM domains configured in your IM and Presence Service deployment, a DNS SRV record is required for each
                                       domain. All SRV records can resolve to the same result set. |
|---|---|