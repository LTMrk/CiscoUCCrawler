---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-administration-guide-b-15cucsag-b-15cucsag-chapter-00-html-8b06e7e43f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag/b_15cucsag_chapter_00.html
retrieved_at: 2026-08-17T02:19:00.909339+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 12, 2025

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Introduction

Cisco Unity Connection provides a set of tools for
                           		administering, monitoring, and troubleshooting the system. The tools that
                           		enable the system administrators to provision the Unity Connection server and
                           		provide feature rich services, such as integrated voice messaging and audio
                           		text application for enterprise level businesses.

## Administrative
                        	 Tools

Following are the administrative tools supported with
                           		Unity Connection:

Cisco Unity Connection Administration : A tool used in most
                                 			 of the administrative tasks such as, customizing user settings and implementing
                                 			 a call management plan. Unity Connection Administration also provides access to
                                 			 several other tools including the Bulk Administration Tool (BAT), Custom Keypad
                                 			 Mapping, Task Management, and Migration Utilities. See Cisco Unity Connection Administration User Interface section.

Cisco Unified Serviceability: A monitoring and troubleshooting
                                 			 tool for serviceability that is shared between Unity Connection and Cisco
                                 			 Unified Communications Manager. This tool allows you to generate reports,
                                 			 enable alarms, set trace information, activate or deactivate services that are
                                 			 generic to the platform.

Cisco Unity Connection Serviceability : A monitoring and troubleshooting tool for serviceability that is used only by Unity Connection.This tool allows you to generate
                                 reports, enable alarms, set trace information, manage a Unity Connection cluster, and activate or deactivate services that
                                 are specific to Unity Connection. For more information, see the Administration Guide for Cisco Unity Connection Serviceability
                                 Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag.html .

Cisco Unified Operating System Administration : A tool used to change operating system settings (for example, IP address or NTP servers), view hardware and software configuration
                                 information (for example, the amount of memory or the Cisco Unified Communications Operating System version), manage SSL certificates,
                                 upgrade Unity Connection and the operating system (they are upgraded together), and enable remote access to the Unity Connection
                                 server. For more information, see the Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection
                                 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html .

Disaster Recovery System : A tool that allows you to perform full data back up and restore capabilities when required. For more information, see the
                                 " Backing Up and Restoring Cisco Unity Connection Components " chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

Real-Time Monitoring Tool (RTMT) : A tool that runs as a client side application to monitor system performance, view system alarms and alerts and collect trace
                                 information for detailed debugging. For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide
                                 Release 12.5 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/rtmt/cucm_b_cisco-unified-rtmt-administration-1251.html .

## Using Single
                        	 Sign-On

Unity Connection support Windows based single sign on feature that allows end users to log in once and gain access to the
                           following Unity Connection web applications without signing on again:

Cisco Personal Communications Assistant

Web Inbox

Cisco Unity Connection Administration

Cisco Unity Connection Serviceability

Single Sign-On feature can be implemented using SAML SSO. This functionality allows you to implement SSO using SAML open industry
                           standard protocol for providing single sign-on access to client applications. For more information on SAML SSO, see the Quick
                           Start Guide for SAML SSO in Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/quick_start/guide/b_15cucqssamlsso.html .

## Configuring
                        	 Browsers on a Unity Connection Administrator Workstation

To access all the administrative tools and web applications, you need to install the supported web browsers, such as Microsoft
                           Internet Explorer or Mozilla Firefox on the administrator workstation depending on the operating system you are using. Confirm
                           that the software required for correct browser configuration is installed. For information on supported web browsers for each
                           operating system, see the “Software Requirements—Administrator Workstations” section of System Requirements for Cisco Unity
                           Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

Make sure to run the Trusted Sites and Add Exceptions when
                                       		  logging in to Cisco Unity Connection Administration or related web pages after
                                       		  a successful installation of Unity Connection.

Table 1-1 specifies the configuration steps that you need to
                                       		  perform on each browser before accessing the web applications.

Browser

Configuration

Mozilla Firefox

Enable Java.

Enable Java Script > Enable Change Images in Java Script
                                             						Advanced.

Allow sites to set cookies. (For security purposes, you should
                                             						set this to Allow Sites to Set Cookies for the Originating Web Site Only.)

Microsoft Internet Explorer

Enable Active scripting.

Download and run ActiveX controls.

Enable Java scripting.

Accept all cookies.

Automatically check for newer versions of temporary Internet
                                             						files.

Enable Medium-High privacy.

Chrome

Accept all cookies and select the Allow local data to be set
                                             						option.

Enable Java Script and select the Allow all sites to run
                                             						JavaScript option.

Enable images and select the Show all images option.

### Accessing and
                           	 Exiting Cisco Unity Connection Administration

The first time when you sign in to Unity
                              		Connection Administration, use the default username and password of the
                              		administrator account specified during installation. Later, you can use the
                              		username and password for any additional administrator account that you create
                              		in Unity Connection Administration page.

### To Login to Unity
                           	 Connection Administration

Step 1

On an
                                          			 administrator workstation, open a browser session.

Step 2

Go to
                                          			 https://<Unity Connection server hostname>/cuadmin.

Step 3

Enter the
                                          			 applicable username and password. Select Login.

### To Exit Cisco
                           	 Unity Connection Administration

Step 1

In the Cisco
                                          			 Unity Connection Administration title pane, select Sign Out .

Step 2

Exit the web
                                          			 browser.

## Cisco Unity
                        	 Connection Administration User Interface

The Unity
                              		  Connection Administration interface is divided into four areas as mentioned in
                              		  the followinf table.

Navigation pane

Located along the left side of the interface, contains links to
                                          						the Unity Connection Administration pages. Select the name of the page to
                                          						display it.

Title Pane

Located across top of the interface, contains an About link and
                                          						the Sign Out link.

The title pane also offers a Navigation menu that you can use to
                                          						browse to other Unity Connection applications. Select the name of the
                                          						application from the Navigation list, and then select Go. Depending on the
                                          						application, you may be required to sign in again.

Title Bar

Displays the name of the page and, if applicable, the name of
                                          						the record displayed on the page. For example, on the Edit User Basics page for
                                          						a user with the alias John, the title bar reads “Edit User Basics (John).” The
                                          						right side of the title bar also shows the navigation path of the page, as it
                                          						relates to other pages in the category. You can select a page in the navigation
                                          						path to go that page.

Page Frame

Area in which the Unity Connection data is entered and
                                          						displayed, page name appears in the title bar at the top of the page. For
                                          						example, while adding new user template, the title bar reads “New User
                                          						Template”.

1

Navigation Pane

2

Title Pane

3

Title Bar

4

Page Frame

Unity Connection provides a means to access Unity
                                          				Connection Administration and other web applications using accessibility
                                          				shortcut keys. For more information, see the Accessibility chapter.

## Cisco Unity
                        	 Connection Configuration Scenarios

Following table lists some of the scenarios that can be used by
                              		  the System Administrator for configuring various tasks in Unity Connection
                              		  depending on the organizational needs.

Scenarios

Description

Configuring voice messaging for each user

The first group of information to be gathered is users
                                          					 requirements that includes total number of users in the company, location of
                                          					 the users, current voice messaging solution adopted by the users, and the
                                          					 expectation from Unity Connection as a unified messaging product.This enables
                                          					 the administrators to configure users as per the messaging needs. For more
                                          					 information, see the Configuring Voice Messaging for Each User section.

Configuring telephony in Unity Connection

A successful deployment requires you to make careful analysis of
                                          					 your existing telephony infrastructure and perform the correct planning steps
                                          					 to deploy and manage voicemail in a unified messaging environment. For more
                                          					 information, see the Configuring Telephony in Unity Connection section.

Connecting various locations in a network

Depending on the messaging needs of the organization, more than
                                          					 one Unity Connection servers located in different locations can be networked
                                          					 together. Being a highly scalable solution, the user configuration can be
                                          					 extended up to 10, 0000 users per server. For more information, see the Connecting Various Locations in a Network section.

Configuring mailbox storage and an email account for each user

Users voice messages are stored, retrieved, and synchronized
                                          					 from the voice mailboxes that are created during the server installation. The
                                          					 administrators can integrate Unity Connection to synchronize voice messages in
                                          					 user voice mailbox with the user exchange mailbox configured on Microsoft
                                          					 Business Productivity Online Suite (BPOS-Dedicated) environments or other third
                                          					 party hosted Exchange environments. For more information, see the Configuring Mailbox Storage and Email Account for Each User section.

Advanced configuration

Unity Connection provides the system administrators to configure
                                          					 the additional parameters for enhanced messaging experience. For more
                                          					 information, see the Advanced Configuration section.

Follow the tasks specified in the table to provide the
                              		  organizations with an enriched voicemail solution.

### Configuring Voice
                           	 Messaging for Each User

In Unity Connection, two users, Application Administrator and
                              		Platform Administrator are created at the time of installation. Both the user
                              		accounts enable the administration of different web pages in Unity Connection.

Application Administrator is a user without a mailbox that
                                    			 provides access to Cisco Unity Connection Administration, Cisco Unified
                                    			 Serviceability, and Cisco Unity Connection Serviceability web pages.

Platform
                                       				Administrator provides access to Command Line Interface (CLI), Cisco
                                    			 Unified Operating System Administration, and Disaster Recovery System (DRS).

Do the following steps to configure voice messaging in an
                              		organization:

Customizing the user templates for personalized user accounts.

Importing users through LDAP and Cisco Unified CM.

Synchronizing the Cisco Unified CM imported end users.

Defining the class of service for users with or without
                                    			 mailboxes.

Enabling HTML Notification for users

See the following sections to understand the importance of voice
                              		messaging components:

User Templates and User Accounts: A user template is a way to
                                    			 apply configurations to a new user. The user template consists of the
                                    			 authentication rules, class of services, schedules, and a number of other
                                    			 configuration options and settings. If you change the template in any way, the
                                    			 users already created based on this template are not affected. However, new
                                    			 users that are created based on this template adopt all new changes that were
                                    			 made to the template. By default, you have two user templates, Administrator
                                    			 Template and Voicemail User Template. You can also create your own customized
                                    			 user templates.

With Unity Connection, the administrator can configure the users
                              		with mailboxes and without mailboxes. The default application administrator
                              		user that cannot send, receive, or forward voice message is an example of user
                              		without mailbox, and is created using the administrator template. While the
                              		users with mailbox that can send, receive, and forward messages to other users
                              		using phones or web clients are based on voicemail user template. Users can
                              		also send video greetings to other voicemail users. For more information on
                              		user templates and settings, see the Call Management chapter.

Creating Users: You can either manually add users or import them
                                    			 from the LDAP directory or Cisco Unified CM configured AXL server on the
                                    			 Cisco Unity Connection Administration page.You can also use Bulk Administration
                                    			 Tool (BAT) to create users with and without mailbox. For more information on
                                    			 creating users, see the Users chapter.

Class of Service and Membership status: Class of service (COS)
                                    			 is a parameter that defines the limits and permissions for using
                                    			 Unity Connection. COS can be configured for users with mailbox and controls the
                                    			 user access to various features and applications such as, message length and
                                    			 using IMAP capability. You can customize the way COS handles the various
                                    			 options by editing or creating a new COS depending on your business needs. For
                                    			 more information on class of service, see the Class of Service section.

You can modify class of service membership status for individual
                              		user accounts to restrict access for various features using default COS defined
                              		during installation. For more information on class of service and class of
                              		service membership, see the User Attributes chapter.

Distribution List: A distribution list is a systematic way to
                                    			 group multiple users in Unity Connection that allows to send and receive voice
                                    			 messages to users that need the same type of information. For more information
                                    			 on distribution lists, see the System Distribution List chapter.

Contacts: Contacts are the users that frequently communicate
                                    			 with Unity Connection users. The contacts are part of voice messaging system
                                    			 with voice mailbox account other than the Unity Connection server. Contacts can
                                    			 be configured as part of VPIM messaging and are accessible using directory
                                    			 access, name dialing access and Personal Call Transfer Rules. For more
                                    			 information on contacts, see the Contacts chapter.

Notification Templates: The notification feature allows alerting
                                    			 the user outside the context of a web page of an occurrence, such as the
                                    			 delivery of email or voice message. User accounts in Unity Connection can be
                                    			 configured for HTML notification on desired email addresses. The default
                                    			 notification templates or the ones customized by administrators provides an
                                    			 easy access to subscriber messages by enabling the HTML notification device.
                                    			 For example, the administrators can configure the HTML templates to include
                                    			 header, footer, logos, images, MWI status, and hyperlink to the Mini Web Inbox.
                                    			 For more information on notification templates, see the Notifications chapter.

### Configuring
                           	 Telephony in Unity Connection

Unity Connection integrations are built using a phone system
                              		configuration that includes one or more port groups. Each port group contain
                              		one or more ports that you can use to support connectivity between the phone
                              		system and Unity Connection.

You can follow the below procedure to configure telephony
                              		integration in your organization.

Identifying the call agent for integrating Unity Connection.

Determining the integration type (SCCP/SIP/PIMG/TIMG/Secure
                                    			 SIP).

Configuring the phone system and adding ports as per the
                                    			 supported OVA and hardware requirements.

Defining the search space and partitions.

Mapping the routing rules with the call handlers as per your
                                    			 requirements.

Telephony Integration: It allows you to manage and integrate
                                    			 phone system in Unity Connection with a call agent for call processing
                                    			 functions, such as sending and receiving telephone calls. For more information
                                    			 on telephony integration, see the Telephony Integration chapter.

Phone System: A phone system in Unity Connection describes a
                                    			 single integration with a PBX or Cisco Unified CM system for call processing
                                    			 redundancy. The phone system contains global configurations that apply to the
                                    			 integrations, such as SIP and SCCP affecting all the port groups. For more
                                    			 information on phone system, see the Telephony Integration chapter.

Ports: Ports are endpoints in Unity Connection that answer calls
                                    			 (inbound) to record, retrieve messages, and handle call transfers.They can also
                                    			 initiate calls (outbound), as in the case of MWI and message notification. For
                                    			 example, if users use the clients (Cisco ViewMail for Microsoft Outlook) to
                                    			 retrieve voicemails, ports are not used for this operation, as long as they
                                    			 download the messages and listen using the workstation speakers. However, if
                                    			 users select IP phones to send or retrieve messages, a port is used. This
                                    			 operation requires a port to be configured for telephony record and playback
                                    			 (TRAP). Ports are associated to only one port group. For more information on
                                    			 ports, see the Telephony Integration chapter.

Port Groups: Port groups include one or more ports. Port groups
                                    			 contain most of the configuration settings for the integration, including the
                                    			 Message Waiting Indicator (MWI), IP address or hostname of the phone system,
                                    			 port numbers, advertised codecs, and other settings that apply to the ports
                                    			 within the port group. Multiple port groups can be configured depending on the
                                    			 type of integration method used for communication, such as SCCP or PIMG/TIMG.
                                    			 The multiple port groups are added under one phone system. For more information
                                    			 on port groups, see the Telephony Integration chapter.

Dial Plan: The dial plan in Unity Connection provides
                                    			 flexibility and access to resources, users, and features through the use of
                                    			 partitions and calling search spaces. Partitions enable an organization to
                                    			 segment resources in Unity Connection for the purpose of dialing, transfers,
                                    			 messaging, addressing, or multi-tenant functionality. The dial plan is an
                                    			 addressing method defined by the network administrator. Partitions are logical
                                    			 groupings of devices with similar reachability and a Search Space is an ordered
                                    			 list of partitions. Extensions must be unique within a partition, but not
                                    			 necessary in case of search spaces. For more information on dial plan, see the Call Management chapter.

Call Routing: Call routing provides a method to route calls from
                                    			 a call agent to Unity Connection. Routing rules influence the call routing as
                                    			 an incoming call is presented to Unity Connection on a voicemail port. The
                                    			 direct routing rule and forwarded routing rules are the two routing rules that
                                    			 can be applied on the calls placed directly to a voicemail number or the calls
                                    			 forwarded when a user is busy. User experience varies depending on the type of
                                    			 caller (internal or outside caller). For more information on call routing, see
                                    			 the Call Management chapter.

Call Management Handlers: Unity Connection offers various
                                    			 handlers as part of call management plan that includes System Call Handlers,
                                    			 Directory Handlers, and Interview Handlers.

A System Call Handler can serve multiple functions in
                                    			 Unity Connection, such as answering calls and playing a recorded announcement
                                    			 to other users or other call handlers. The call handlers are based on
                                    			 pre-defined call handler templates and the functions vary depending on the
                                    			 current call routing rule. The Directory Handlers provide an easy access method
                                    			 to reach the subscribers with recorded names. Interview Handlers offers a way
                                    			 to gather information from callers by playing a series of questions and
                                    			 recording the answers. You can customize the handlers over the phone to offer
                                    			 better user experience. For more information on call management handlers, see
                                    			 the Call Management chapter.

### Connecting Various
                           	 Locations in a Network

Networking in Unity Connection clusters enables the system
                              		administrators to inter-network with other voice messaging systems to achieve
                              		inter-interoperability and high scalability. Depending on the messaging needs
                              		of the organization, multiple Unity Connection directories (Unity Connection
                              		servers or clusters) can be combined to form a site (and to interlink multiple
                              		Unity Connection sites to form a voicemail organization.

Unity Connection allows you to meet your expanding business
                              		needs by providing various networking options:

VPIM: Unity Connection as a unified messaging system provides
                                    			 VPIM gateways with on ramps (gateways that connects from another voicemail
                                    			 networking protocol to VPIM) and off ramp (gateways that connect from VPIM to
                                    			 another voicemail networking protocol) to allow integration of similar and
                                    			 dissimilar messaging systems, such as Avaya Solutions and Unity Connection.

Voice Profile for Internet Mail (VPIM) protocol is an industry
                              		standard that allows different voice messaging systems to exchange voice and
                              		text messages over the Internet or any TCP/IP network. It is based on the
                              		Simple Mail Transfer Protocol (SMTP) and the Multi-Purpose Internet Mail
                              		Extension (MIME) protocol. For more information on VPIM, see the Networking chapter.

Unity Connection supports up to 10 VPIM locations and 100,000
                                          		  VPIM contacts in the Unity Connection directory.

Legacy Networking: Unity Connection supports intrasite and
                                    			 intersite networking between various Unity Connection clusters.

Intrasite Networking: If your organization has users that are
                                          				  more than what a single Unity Connection server or cluster pair can support,
                                          				  you can join two or more Unity Connection servers or clusters (up to a maximum
                                          				  of ten) to form a well-connected network, referred to as a Unity Connection
                                          				  site. The servers that are joined to the site are referred to as Locations.
                                          				  (When a Unity Connection cluster is configured, the cluster counts as one
                                          				  location in the site.) Each location is said to be linked to every other
                                          				  location in the site via an intrasite link. The Unity Connection site concept
                                          				  was known as a digital network in Unity Connection 7.x. You can join
                                          				  Unity Connection 7.x locations, 8.x locations, 9.x locations, 10.x locations,
                                          				  11.x, and 12.x locations in the same Unity Connection site, as long as you do
                                          				  not link the site to any other site. Users, system distribution lists,
                                          				  partitions, search spaces, and Unity Connection locations are replicated
                                          				  between sites.

Intersite Networking: An intersite link can be used to connect
                                          				  either one Unity Connection site to another Unity Connection site or to
                                          				  inter-network Unity Connection with the Unity servers. Intersite link can be
                                          				  configured for 20 locations. For more information on legacy networking, see the Networking chapter.

To support inter-networking between Cisco Unity and
                                                      					 Unity Connection sites, all servers in the site must be running
                                                      					 Unity Connection version 10.x or later.

HTTPS: With Unity Connection 10.0(1), a new concept of
                                          				  networking, HTTPS networking, has been introduced to connect different
                                          				  Unity Connection servers and clusters in a network. You should deploy a new
                                          				  network as an HTTPS network. You can connect maximum 25 Unity Connection
                                          				  locations in an HTTPS network. Within a network, each location uses HTTP or
                                          				  HTTPS to exchange directory information and SMTP to exchange voice messages
                                          				  with each other. For more information on HTTPS, see the Networking chapter.

SRSV: Cisco Unity Connection Survivable Remote Site Voicemail (Unity Connection SRSV) is a backup voicemail solution that
                                          works in conjunction with Cisco Unified Survivable Remote Site Telephony (SRST) for providing voicemail service to central
                                          and all remote locations during WAN outages. For more information on SRSV, see Complete Reference Guide for Cisco Unity Connection
                                          Survivable Remote Site Voicemail (SRSV) for Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/srsv/guide/b_15cucsrsvx.html .

SRSV deployment is supported with Unity Connection 9.1.2 and
                                                      					 later.

### Configuring
                           	 Mailbox Storage and Email Account for Each User

Unity Connection has an installed mailbox store.
                              		Unity Connection handles user properties, such as user mailbox accounts and
                              		voice messages by creating a directory configuration database. You need to
                              		configure your mailbox store as per your messaging needs.

Mailbox Store: Mailbox store is a repository that is used to
                                    			 store messages and Unity Connection directory information. A single mailbox
                                    			 store is created at the time of installation and is named as UnityMbxDb1. You
                                    			 can add additional message storage for better performance.For more information
                                    			 on message storage, see the Message Storage chapter.

Mailbox Quotas: Mailbox Quotas allows you to define the size
                                    			 limits of user voice mailboxes in Unity Connection. Unity Connection is
                                    			 configured with system-wide mailbox size quotas that can be customized to set
                                    			 restrictions on the send or receive of user voice messages. For more
                                    			 information on mailbox quotas, see the Message Storage chapter.

Message Aging Policy: When a mailbox store is created, maximum
                                    			 amount of disk space is created for the user voice messages. To maintain the
                                    			 allocated disk space within the specified mailbox quota, Unity Connection
                                    			 provides message aging policies. The rules apply on users mailbox and ensure
                                    			 that disk space for where voice messages are stored do not fill up. The state
                                    			 of the messages is changed when the aging policy is active. For example, new
                                    			 message moves to saved state and saved to deleted in the specified period of
                                    			 time. For more information on message aging policy, see the Message Storage chapter.

Unified Messaging Service: Unity Connection supports Unified
                                    			 Messaging Service (UMS) that integrates voice messaging with your email
                                    			 account, allowing you to store voice messages in your mailbox along with your
                                    			 email. With UMS, you can access your voice messages using an email client or a
                                    			 Telephone User Interface (TUI).

To enable communication between Unity Connection and Exchange,
                              		unified messaging service can be configured depending on the Exchange type,
                              		Exchange 2010, Exchange 2013 or Exchange 20016, Office365. UMS provides
                              		features that enables you to hear your exchange emails using TTS
                              		(text-to-speech) functionality in Unity Connection, enables access to exchange
                              		calendars and contacts, synchronize voice messages in Unity Connection and
                              		Exchange mailboxes for single inbox.

Single inbox: Single inbox is one of the unified messaging
                                    			 features in Unity Connection that synchronizes voice messages in
                                    			 Unity Connection and Exchange mailboxes.When a user is enabled for single
                                    			 inbox, all Unity Connection voice messages that are sent to the user, including
                                    			 the messages sent from Cisco Unity Connection ViewMail for Microsoft Outlook
                                    			 (VMO), are first stored in Unity Connection and are immediately replicated to
                                    			 the user mailbox in Exchange.ViewMail for Outlook is an add-in that allows
                                    			 voice messages to be heard and composed from within Microsoft Outlook 2010, or
                                    			 2016.

### Advanced
                           	 Configuration

Unity Connection provides many tools and options that can be
                              		enabled for enhanced user experience and system performance.Deploying and
                              		configuring a voice messaging system in your organization can also be further
                              		customized with some of the additional settings as described in the below
                              		section:

Tools: Various tools and utilities can be used for administering
                                    			 Unity Connection such as, Task Management and SMTP Address Search.

Some of the Unity Connection tools are:

Bulk Administration Tool (BAT) tool allows you to add, delete,
                                    			 edit object properties, such as users and distribution lists by exporting and
                                    			 importing the default templates.

Custom Keypad Mapping allows you to customize phone menu key
                                    			 press for users. User can change the DTMF keys for Cisco IP phones for sending
                                    			 and receiving voice messages through Telephone User Interface (TUI).

Task Management lists the Unity Connection services that run on
                                    			 a scheduled basis and can be used for various troubleshooting and system
                                    			 maintenance tasks.

Real-Time Monitoring Tool is an application plugin used as
                                    			 extension of Unity Connection for monitoring the system performance and port
                                    			 usage.

For more information on tools in Unity Connection, see the Tools chapter.

System Settings: Unity Connection allows the System
                                    			 Administrator to specify the system wide parameters for various object
                                    			 properties including cluster settings at the time of subscriber server
                                    			 installation, authentication rules to define the web password and voicemail PIN
                                    			 for user voice mailbox, licenses to view the license state of Unity Connection
                                    			 registered with Cisco Smart Software Manager (CSSM) or Cisco Smart Software
                                    			 Manager satellite, changing roles, setting the restriction table for phone
                                    			 extensions with larger digits, smart host settings, and many others. For more
                                    			 information on system settings, see the System Settings chapter.

Advanced Settings: It provides enabling and disabling check
                                    			 boxes for various functionalities including conversations for call transfer
                                    			 settings, messaging for user mailboxes, disk capacity to determine disk size,
                                    			 cluster configuration for change in cluster status, unified messaging service
                                    			 settings related to calendaring in UMS and more. For more information on
                                    			 advanced settings, see the Advanced System Settings chapter.

| Note | Make sure to run the Trusted Sites and Add Exceptions when
                                       		  logging in to Cisco Unity Connection Administration or related web pages after
                                       		  a successful installation of Unity Connection. Table 1-1 specifies the configuration steps that you need to
                                       		  perform on each browser before accessing the web applications. |
|---|---|

| Browser | Configuration |
|---|---|
| Mozilla Firefox | Enable Java. Enable Java Script > Enable Change Images in Java Script
                                             						Advanced. Allow sites to set cookies. (For security purposes, you should
                                             						set this to Allow Sites to Set Cookies for the Originating Web Site Only.) |
| Microsoft Internet Explorer | Enable Active scripting. Download and run ActiveX controls. Enable Java scripting. Accept all cookies. Automatically check for newer versions of temporary Internet
                                             						files. Enable Medium-High privacy. |
| Chrome | Accept all cookies and select the Allow local data to be set
                                             						option. Enable Java Script and select the Allow all sites to run
                                             						JavaScript option. Enable images and select the Show all images option. |

| Step 1 | On an
                                          			 administrator workstation, open a browser session. |
|---|---|
| Step 2 | Go to
                                          			 https://<Unity Connection server hostname>/cuadmin. |
| Step 3 | Enter the
                                          			 applicable username and password. Select Login. By default,
                                          			 a Unity Connection Administration session is set to time out after twenty
                                          			 minutes. You can change the Administration Session Timeout settings on the
                                          			 System Settings > Advanced > Connection Administration page. |

| Step 1 | In the Cisco
                                          			 Unity Connection Administration title pane, select Sign Out . |
|---|---|
| Step 2 | Exit the web
                                          			 browser. Note Unity
                                                      				Connection Administration supports both the IPv4 and IPv6 addresses. However,
                                                      				the IPv6 address works only when Unity Connection platform is configured in
                                                      				Dual (IPv4/IPv6) mode. | Note | Unity
                                                      				Connection Administration supports both the IPv4 and IPv6 addresses. However,
                                                      				the IPv6 address works only when Unity Connection platform is configured in
                                                      				Dual (IPv4/IPv6) mode. |
| Note | Unity
                                                      				Connection Administration supports both the IPv4 and IPv6 addresses. However,
                                                      				the IPv6 address works only when Unity Connection platform is configured in
                                                      				Dual (IPv4/IPv6) mode. |

| Note | Unity
                                                      				Connection Administration supports both the IPv4 and IPv6 addresses. However,
                                                      				the IPv6 address works only when Unity Connection platform is configured in
                                                      				Dual (IPv4/IPv6) mode. |
|---|---|

| Navigation pane | Located along the left side of the interface, contains links to
                                          						the Unity Connection Administration pages. Select the name of the page to
                                          						display it. |
|---|---|
| Title Pane | Located across top of the interface, contains an About link and
                                          						the Sign Out link. The title pane also offers a Navigation menu that you can use to
                                          						browse to other Unity Connection applications. Select the name of the
                                          						application from the Navigation list, and then select Go. Depending on the
                                          						application, you may be required to sign in again. |
| Title Bar | Displays the name of the page and, if applicable, the name of
                                          						the record displayed on the page. For example, on the Edit User Basics page for
                                          						a user with the alias John, the title bar reads “Edit User Basics (John).” The
                                          						right side of the title bar also shows the navigation path of the page, as it
                                          						relates to other pages in the category. You can select a page in the navigation
                                          						path to go that page. |
| Page Frame | Area in which the Unity Connection data is entered and
                                          						displayed, page name appears in the title bar at the top of the page. For
                                          						example, while adding new user template, the title bar reads “New User
                                          						Template”. |

| 1 | Navigation Pane |
|---|---|
| 2 | Title Pane |
| 3 | Title Bar |
| 4 | Page Frame |

| Note | Unity Connection provides a means to access Unity
                                          				Connection Administration and other web applications using accessibility
                                          				shortcut keys. For more information, see the Accessibility chapter. |
|---|---|

| Scenarios | Description |
|---|---|
| Configuring voice messaging for each user | The first group of information to be gathered is users
                                          					 requirements that includes total number of users in the company, location of
                                          					 the users, current voice messaging solution adopted by the users, and the
                                          					 expectation from Unity Connection as a unified messaging product.This enables
                                          					 the administrators to configure users as per the messaging needs. For more
                                          					 information, see the Configuring Voice Messaging for Each User section. |
| Configuring telephony in Unity Connection | A successful deployment requires you to make careful analysis of
                                          					 your existing telephony infrastructure and perform the correct planning steps
                                          					 to deploy and manage voicemail in a unified messaging environment. For more
                                          					 information, see the Configuring Telephony in Unity Connection section. |
| Connecting various locations in a network | Depending on the messaging needs of the organization, more than
                                          					 one Unity Connection servers located in different locations can be networked
                                          					 together. Being a highly scalable solution, the user configuration can be
                                          					 extended up to 10, 0000 users per server. For more information, see the Connecting Various Locations in a Network section. |
| Configuring mailbox storage and an email account for each user | Users voice messages are stored, retrieved, and synchronized
                                          					 from the voice mailboxes that are created during the server installation. The
                                          					 administrators can integrate Unity Connection to synchronize voice messages in
                                          					 user voice mailbox with the user exchange mailbox configured on Microsoft
                                          					 Business Productivity Online Suite (BPOS-Dedicated) environments or other third
                                          					 party hosted Exchange environments. For more information, see the Configuring Mailbox Storage and Email Account for Each User section. |
| Advanced configuration | Unity Connection provides the system administrators to configure
                                          					 the additional parameters for enhanced messaging experience. For more
                                          					 information, see the Advanced Configuration section. |

| Note | Unity Connection supports up to 10 VPIM locations and 100,000
                                          		  VPIM contacts in the Unity Connection directory. |
|---|---|

| Note | To support inter-networking between Cisco Unity and
                                                      					 Unity Connection sites, all servers in the site must be running
                                                      					 Unity Connection version 10.x or later. |
|---|---|

| Note | SRSV deployment is supported with Unity Connection 9.1.2 and
                                                      					 later. |
|---|---|