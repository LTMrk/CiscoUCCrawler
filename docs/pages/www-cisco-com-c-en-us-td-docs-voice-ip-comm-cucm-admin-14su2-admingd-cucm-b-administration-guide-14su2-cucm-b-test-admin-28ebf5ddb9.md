---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14su2-admingd-cucm-b-administration-guide-14su2-cucm-b-test-admin-28ebf5ddb9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14SU2/adminGd/cucm_b_administration-guide-14su2/cucm_b_test-adminguide_chapter_010111.html
retrieved_at: 2026-08-17T00:41:07.030077+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 8, 2025

Chapter: Services

## Chapter: Services

# Services

## Feature
                        	 Services

Use the Serviceability GUI to activate, start, and stop Cisco Unified Communications Manager and IM and Presence services.
                              Activation turns on and starts a service. You must manually activate the feature service for all features that you want to
                              use. For service-activation recommendations, see topics related to service activation.

If you try to access a Unified Communications Manager server from an IM and Presence node or vice versa, you may encounter
                                          the following error: "Connection to the Server cannot be established (unable to access Remote Node)" . If this error message
                                          appears, see the Administration Guide for Cisco Unified Communications Manager .

Devices using IM and Presence are configured to use a Postgres external database to support persistent chat, compliance, and
                                          file transfer. However, the connection between IM and Presence server and Postgres is not secured and the data passes without
                                          any check. For the services or devices that do not support TLS, there is another way to provide secure communication by configuring
                                          IP Sec, which is a standard protocol for secure communications by authenticating and encrypting each IP packet of a communication
                                          session.

After you activate a service in the Service Activation window, you do not need to start it in the Control Center - Feature Services window. If the service does not start for any reason, you must start it in the Control Center - Feature Services window.

After the system is installed, it does not automatically activate feature services, You need to activate the feature service
                              to use your configuration features, for example, the Serviceability Reports Archive feature.

Unified Communications Manager and Cisco Unified IM and Presence Service only: If you are upgrading Unified Communications Manager, those services that you activated on the system before the upgrade
                              automatically start after the upgrade.

Cisco Unified Communications Manager Administration

Cisco Unity Connection Administration

### Feature
                              		  Services Categories

In Cisco Unified
                                 			 Serviceability , the Service
                                 			 Activation window and the Control
                                 			 Center - Feature Services window categorize feature services into
                              		  the following groups:

Database and
                                    				administration services

Performance
                                    				and monitoring services

CM services

CTI services

CDR services

Security
                                    				services

Directory
                                    				services

Voice quality
                                    				reporter services

Database and
                                       				administration services

Performance
                                       				and monitoring services

IM and Presence Service services

### Database and Administration Services

#### Locations Bandwidth Manager

This service is not supported by IM and Presence Service .

The Locations Bandwidth Manager service assembles a network model from configured Location and Link data in one or more clusters,
                                    determines the Effective Paths between pairs of Locations, determines whether to admit calls between a pair of Locations based
                                    on the availability of bandwidth for each type of call, and deducts (reserves) bandwidth for the duration of each call that
                                    is admitted.

#### Cisco AXL Web Service

The Cisco AXL Web Service allows you to modify database entries and execute stored procedures from client-based applications
                                    that use AXL.

In an IM and Presence Service system, this service supports both Unified Communications Manager and Cisco Unity Connection .

#### Cisco UXL Web Service

This service is not supported by IM and Presence Service .

The TabSync client in Cisco IP Phone Address Book Synchronizer uses the Cisco UXL Web Service for queries to the Unified Communications
                                    Manager database, which ensures that Cisco IP Phone Address Book Synchronizer users have access only to end-user data that
                                    pertains to them. The Cisco UXL Web Service performs the following functions:

Conducts authentication checks by verifying the end-user username and password when an end user logs in to Cisco IP Phone
                                          Address Book Synchronizer.

Conducts a user authorization check by only allowing the user that is currently logged in to Cisco IP Phone Address Book Synchronizer
                                          to perform functions such as listing, retrieving, updating, removing, and adding contacts.

#### Cisco Bulk Provisioning Service

This service does not support Cisco Unity Connection .

If your configuration supports clusters (Unified Communications Manager only), you can activate the Cisco Bulk Provisioning
                                    Service only on the first server. If you use the Unified Communications Manager Bulk Administration Tool to administer phones and users, you must activate this service.

#### Cisco TAPS Service

This service does not support Cisco Unity Connection or IM and Presence Service.

The Cisco Tools for Auto-Registered Phones Support (TAPS) Service supports the Cisco Unified Communications Manager Auto-Register Phone Tool , which allows a user to upload a customized configuration on an auto registered phone after a user responds to Interactive
                                    Voice Response (IVR) prompts.

If your configuration supports clusters (Unified Communications Manager only), you activate this service on the first server.
                                    When you want to create dummy MAC addresses for the tool, ensure that the Cisco Bulk Provisioning Service is activated on the same server.

Tip

The Cisco Unified Communications Manager Auto-Register Phone Tool relies on Cisco Customer Response Solutions (CRS). Before the tool can work as designed, verify that the CRS server is configured
                                                and running, as described in the CRS documentation.

#### Platform Administrative Web Service

The Platform Administrative Web Service is a Simple Object Access Protocol (SOAP) API that can be activated on Unified Communications
                                    Manager, IM and Presence Service , and Cisco Unity Connection systems to allow the PAWS-M server to upgrade the system.

Important

Do not activate the Platform Administrative Web Service on the PAWS-M server.

### Performance and monitoring services

### Cisco Serviceability Reporter

The Cisco Serviceability Reporter service generates daily reports. For details, see topics that are related to the serviceability
                                 reports archive.

If your configuration supports clusters (Unified Communications Manager only), this service is installed on all the Unified
                                 Communications Manager servers in the cluster. Reporter generates reports once a day based on logged information. You can
                                 access the reports that Reporter generates in Cisco Unified Serviceability from the Tools menu. Each summary report comprises different charts that display the statistics for that particular report.
                                 After you activate the service, report generation may take up to 24 hours.

### Cisco CallManager SNMP Service

This service does not support IM and Presence Service and Cisco Unity Connection .

This service, which implements the CISCO-CCM-MIB, provides SNMP access to provisioning and statistics information that is
                                 available for Unified Communications Manager.

If your configuration supports clusters (Unified Communications Manager only), activate this service on all servers in the
                                 cluster.

### CM Services

This section describes the CM Services and does not apply to IM and Presence Service and Cisco Unity Connection .

#### Cisco
                              	 CallManager

The Cisco CallManager Service provides software-only call processing as well as signaling and call control functionality for
                                    Unified Communications Manager.

Tip

Unified Communications Manager clusters only: Before you activate this service, verify that the Unified Communications Manager
                                                server displays in the Find and List Cisco Unified Communications Manager's window in Cisco Unified Communications Manager
                                                Administration. If the server does not display, add the Unified Communications Manager server before you activate this service.
                                                For information on how to find and add the server, see the Administration Guide for Cisco Unified Communications Manager .

Unified Communications Manager clusters only: If you deactivate the Cisco CallManager or CTIManager services in Service Activation,
                                                the Unified Communications Manager server where you deactivated the service no longer exists in the database, which means
                                                that you cannot choose that Unified Communications Manager server for configuration operations in Cisco Unified Communications
                                                Manager Administration because it does not display in the graphical user interface (GUI). If you then reactivate the services
                                                on the same Unified Communications Manager server, the database creates an entry for Unified Communications Manager again
                                                and adds a "CM_" prefix to the server name or IP address; for example, if you reactivate the Cisco CallManager or CTIManager service on a
                                                server with an IP address of 172.19.140.180, then CM_172.19.140.180 displays in Cisco Unified Communications Manager Administration.
                                                You can now choose the server, with the new "CM_" prefix, in Cisco Unified Communications Manager Administration.

The
                                    		  following services rely on Cisco CallManager service activation:

CM
                                             				  Services

CDR
                                             				  Services

#### Cisco TFTP

Cisco Trivial File Transfer Protocol (TFTP) builds and serves files that are consistent with the trivial file transfer protocol,
                                    a simplified version of FTP. Cisco TFTP serves embedded component executable, ringer files, and device configuration files.

Unified Communications Manager only: A configuration file includes a list of Unified Communications Manager's to which devices
                                    (telephones and gateways) make connections. When a device boots, the component queries a Dynamic Host Configuration Protocol
                                    (DHCP) server for its network configuration information. The DHCP server responds with an IP address for the device, a subnet
                                    mask, a default gateway, a Domain Name System (DNS) server address, and a TFTP server name or address. The device requests
                                    a configuration file from the TFTP server. The configuration file contains a list of Unified Communications Manager's and
                                    the TCP port through which the device connects to those Unified Communications Manager's. The configuration file contains
                                    a list of Unified Communications Managers and the TCP port through which the device connects to those Unified Communications
                                    Manager's.

#### Cisco Unified Mobile Voice Access Service

Make calls from the cellular phone as if the call originated from the desk phone.

Turn Cisco Unified Mobility on.

Turn Cisco Unified Mobility off.

#### Cisco IP Voice Media Streaming App

The Cisco IP Voice Media Streaming Application service provides voice media streaming functionality for Unified Communications
                                    Manager for use with Media Termination Point (MTP), conferencing, music on hold (MOH), and annunciator. The Cisco IP Voice
                                    Media Streaming Application relays messages from Unified Communications Manager to the IP voice media streaming driver, which
                                    handles Real-Time Protocol (RTP) streaming.

The Cisco IP Voice Media Streaming Application service does not generate the Call Management Record (CMR) files for call legs
                                    that involve any IP Voice Media Streaming Application components like conference, MOH, annunciator, or MTP.

#### Cisco CTIManager

The Cisco CTI Manager contains the CTI components that interact with applications. This service allows applications to monitor
                                    or control phones and virtual devices to perform call control functionality.

Unified Communications Manager clusters only: With CTI Manager, applications can access resources and functionality of all
                                    Unified Communications Manager's in the cluster and have improved failover capability. Although one or more CTI Managers can
                                    be active in a cluster, only one CTI Manager can exist on an individual server. An application (JTAPI/TAPI) can have simultaneous
                                    connections to multiple CTI Managers; however, an application can use only one connection at a time to open a device with
                                    media termination.

#### Cisco Extension Mobility

This service, which supports the Cisco Extension Mobility feature, performs the login and automatic logout functionality for the feature.

#### Cisco Dialed Number Analyzer

The Cisco Dialed Number Analyzer service supports Unified Communications Manager Dialed Number Analyzer . When activated, this application consumes a lot of resources, so activate this service only during off-peak hours when minimal
                                    call-processing interruptions may occur.

Unified Communications Manager clusters only: Cisco does not recommend that you activate the service on all the servers in
                                    a cluster. Cisco recommends that you activate this service only on one of the servers of a cluster where call-processing activity
                                    is the least.

#### Cisco Dialed Number Analyzer Server

The Cisco Dialed Number Analyzer Server service along with the Cisco Dialed Number Analyzer service supports Cisco Unified
                                    Communications Manager Dialed Number Analyzer. This service needs to be activated only on the node that is dedicated specifically
                                    for the Cisco Dialed Number Analyzer service.

Unified Communications Manager clusters only: Cisco does not recommend that you activate the service on all the servers in
                                    a cluster. Cisco recommends that you activate this service only on one of the servers of a cluster where call-processing activity
                                    is the least.

#### Cisco DHCP Monitor Service

Cisco DHCP Monitor Service monitors IP address changes for IP phones in the database tables. When a change is detected, it
                                    modifies the /etc./dhcpd.conf file and restarts the DHCPD daemon.

#### Cisco Intercluster Lookup Service

The Intercluster Lookup Service (ILS) runs on a cluster-wide basis. ILS allows you to create networks of remote Unified Communications
                                    Manager clusters. The ILS cluster discovery feature allows Unified Communications Manager to connect to remote clusters without
                                    the need for an administrator having to manually configure connections between each cluster. The ILS Global Dial Plan Replication
                                    feature enables clusters in the ILS network with the ability to exchange global dial plan data with the other clusters in
                                    an ILS network.

ILS can be activated from the ILS Configuration window that can be accessed in Cisco Unified Communications Manager Administration
                                    by selecting Advanced Features > ILS Configuration .

#### Cisco UserSync Service

Cisco UserSync service synchronizes the data from Unified Communications Manager end-user table to the LDAP database.

#### Cisco UserLookup Web Service

Cisco UserLookup Web service routes the commercial calls (calls through external gateways) to an alternate internal number
                                    of the called party in order to avoid the commercial cost of calling an external number.

If a caller within a Unified Communications Manager network makes a call on an external number, Unified Communications Manager
                                    checks if an internal number exists for the called party in the LDAP database. If an internal number exists, the call is routed
                                    to that internal number. If the internal number is not found in the LDAP database, the call is routed to the original (external)
                                    number.

#### Cisco Headset Service

Cisco Headset Service enables you to manage inventory, configuration updates, and diagnostics data of your Cisco Headset if
                                    you use compatible Cisco IP Phones, Cisco Jabber, or other Cisco devices.

Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                                is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                                want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                                activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it.

### IM and Presence Services

IM and Presence services apply only to IM and Presence Service .

#### Cisco SIP Proxy

The Cisco SIP Proxy service is responsible for providing the SIP registrar and proxy functionality. This includes request
                                    routing, requestor identification, and transport interconnection.

#### Cisco Presence Engine

The Cisco Presence Engine collects, aggregates, and distributes user capabilities and attributes using the standards-based
                                    SIP and SIMPLE interface. It collects information about the availability status and communications capabilities of a user.

#### Cisco XCP Text Conference Manager

The Cisco XCP Text Conference Manager supports the chat feature. The chat feature allows users to communicate with each other
                                    in online chat rooms. It supports chat functionality using ad hoc (temporary) and permanent chat rooms, which remain on a
                                    Cisco-supported external database until they are deleted.

#### Cisco XCP Web Connection Manager

The Cisco XCP Web Connection Manager service enables browser-based clients to connect to IM and Presence Service .

#### Cisco XCP Connection Manager

The Cisco Unified Presence XCP Connection Manager enables XMPP clients to connect to the Cisco Unified Presence server.

#### Cisco XCP SIP Federation Connection Manager

The Cisco XCP SIP Federation Connection Manager supports interdomain federation with Microsoft OCS over the SIP protocol.
                                    You must also turn on this service when your deployment contains an intercluster connection between an IM and Presence Service Release 9.0 cluster, and a Cisco Unified Presence Release 8.6 cluster.

#### Cisco XCP XMPP Federation Connection Manager

The Cisco XCP XMPP Federation Connection Manager supports interdomain federation with third party enterprises such as IBM
                                    Lotus Sametime, Cisco Webex Meeting Center, and GoogleTalk over the XMPP protocol, as well as supports interdomain federation
                                    with another IM and Presence Service enterprise over the XMPP protocol.

#### Cisco XCP Message Archiver

The Cisco XCP Message Archiver service supports the IM Compliance feature. The IM Compliance feature logs all messages sent
                                    to and from the IM and Presence Service server, including point-to-point messages, and messages from ad hoc (temporary) and permanent chat rooms for the Chat feature.
                                    Messages are logged to an external Cisco-supported database.

#### Cisco XCP Directory Service

The Cisco XCP Directory Service supports the integration of XMPP clients with the LDAP directory to allow users to search
                                    and add contacts from the LDAP directory.

#### Cisco XCP Authentication Service

The Cisco XCP Authentication Service handles all authentication requests from XMPP clients that are connecting to IM and Presence Service .

### CTI Services

This section describes the CTI Services and does not apply to Cisco Unity Connection or IM  and Presence Service .

#### Cisco IP Manager Assistant

This service supports Cisco Unified Communications Manager Assistant . After service activation, Cisco Unified Communications Manager Assistant enables managers and their assistants to work together more effectively. Cisco Unified Communications Manager Assistant supports two modes of operation: proxy line support and shared line support.

The feature comprises a call-routing service, enhancements to phone capabilities for the manager, and desktop interfaces that
                                    are primarily used by the assistant.

The service intercepts calls that are made to managers and routes them to selected assistants, to managers, or to other targets
                                    on the basis of preconfigured call filters. The manager can change the call routing dynamically; for example, by pressing
                                    a softkey on the phone, the manager can instruct the service to route all calls to the assistant and can receive status on
                                    these calls.

Unified Communications Manager users comprise managers and assistants. The routing service intercepts manager calls and routes
                                    them appropriately. An assistant user handles calls on behalf of a manager.

#### Cisco WebDialer Web Service

##### Cisco WebDialer Web Service for Cisco Unified Communications Manager Systems

Cisco Web Dialer provides click-to-dial functionality. It allows users inside a Unified Communications Manager cluster to initiate a call
                                    to other users inside or outside the cluster by using a web page or a desktop application. Cisco Web Dialer provides a web page that enables users to call each other within a cluster. Cisco Web Dialer comprises two components: WebDialer servlet and Redirector servlet.

The Redirector servlet provides the ability for third-party applications to use Cisco Web Dialer . The Redirector servlet finds the appropriate Unified Communications Manager cluster for the Cisco Web Dialer user and redirects the request to the Cisco Web Dialer in that cluster. The Redirector functionality applies only for HTTP/HTML-based WebDialer client applications because it is
                                    not available for Simple Object Access Protocol (SOAP)-based WebDialer applications.

#### Self-Provisioning
                              	 IVR

With the introduction of Self-Provisioning IVR Service, the autoregistered IP phones on the Unified Communications Manager
                                    are assigned to users quickly with less effort. When you dial the CTI RP DN, that is configured on the Self-Provisioning page,
                                    from an extension of a user that uses the IVR service, the phone connects to the Self-Provisioning IVR application and prompts
                                    you to provide the Self-Service credentials. Based on the validation of the Self-Service credentials that you provide, the
                                    IVR service assigns the autoregistered IP phones to the users.

You can configure
                                    		  self-provisioning even if the service is deactivated, but the administrator
                                    		  cannot assign IP phones to users using the IVR service. By default, this
                                    		  service is deactivated.

To enable the
                                    		  Self-Provisioning IVR service, you must also enable the Cisco CTI Manager
                                    		  service.

For
                                    		  more information about how to configure self-provisioning, see the Administration Guide for Cisco Unified Communications Manager .

### CDR Services

This section describes the CDR Services and does not apply to IM and Presence Service and Cisco Unity Connection .

#### CAR Web Service

The Cisco CAR Web Service loads the user interface for CAR, a web-based reporting application that generates either CSV or
                                    PDF reports by using CDR data.

#### Cisco SOAP -
                              	 CDRonDemand Service

The
                                    		  Cisco SOAP - CDRonDemand Service, a SOAP/HTTPS-based service, runs on the CDR
                                    		  Repository server. It receives SOAP requests for CDR filename lists that are
                                    		  based on a user-specified time interval (up to a maximum of 1 hour) and returns
                                    		  a list of filenames that fit the time duration that is specified in the
                                    		  request. This service also receives requests for delivery of a specific CDR/CMR
                                    		  file with the filename and the transfer method (SFTP/FTP, server name, login
                                    		  info, directory) that is specified in the request.

If you
                                    		  are using a third-party billing application that accesses CDR data through an
                                    		  HTTPS/SOAP interface, activate this service.

For Unified Communications Manager Release 12.x and later releases, CDR onDemand Service is not enabled by default. If you
                                    want to enable the CDR onDemand service, the service should be activated manually. Execute the following command at the root
                                    level to activate the CDR onDemand service: /usr/local/cm/bin/soapservicecontrol2.shCDRonDemandServiceCDRonDemanddeploy8443 .

### Security Services

This section describes the Security Services and does not apply to IM and Presence Service and Cisco Unity Connection .

#### Cisco CTL Provider

Unified Communications Manager only: The Cisco Certificate Trust List (CTL) Provider service, which runs with local system
                                    account privileges, works with the Cisco CTL Provider Utility, a client-side plug-in, to change the security mode for the
                                    cluster from nonsecure to mixed mode. When you install the plug-in, the Cisco CTL Provider service retrieves a list of all
                                    Unified Communications Manager and Cisco TFTP servers in the cluster for the CTL file, which contains a list of security tokens
                                    and servers in the cluster.

You can install and configure the Cisco CTL Client or the CLI command set utils ctl , and then activate this service for the clusterwide security mode to change from nonsecure to secure.

After you activate the service, the Cisco CTL Provider service reverts to the default CTL port, which is2444. If you want
                                    to change the port, see the Cisco Unified Communications Manager Security Guide for more information.

#### Cisco Certificate Authority Proxy Function (CAPF)

Working in conjunction with the Cisco Certificate Authority Proxy Function (CAPF) application, the CAPF service can perform
                                    the following tasks, depending on your configuration:

Issue locally significant certificates to supported Cisco Unified IP Phone models.

Upgrade existing certificates on the phones.

Retrieve phone certificates for troubleshooting.

Delete locally significant certificates on the phone.

Unified Communications Manager only: When you view real-time information in the Real-Time Monitoring Tool (RTMT), the CAPF
                                                service displays only for the first server.

### Directory Services

This section describes the  Directory Services and does not apply to IM and Presence Service and Cisco Unity Connection .

#### Cisco DirSync

Users with duplicate email IDs are not synchronized and the administrator receives no notification about the list of users
                                                   which are not synced. These IDS are shown in the DirSync error logs from Unified RTMT.

Cisco Unity Connection : When Cisco Unity Connection is integrated with an LDAP directory, the Cisco DirSync service synchronizes a small subset of user data (first name, last
                                    name, alias, phone number, and so on) in the Unified Communications Manager database on the Cisco Unity Connection server with the corresponding data in the LDAP directory. Another service (CuCmDbEventListener) synchronizes data in the Cisco Unity Connection user database with data in the Unified Communications Manager database. When a Cisco Unity Connection cluster is configured, the Cisco DirSync service runs only on the publisher server.

### Location Based Tracking Services

This section describes Location Based Tracking Services.

#### Cisco Wireless
                              	 Controller Synchronization Service

This service
                                    		  supports the Location Awareness feature, which provides a status of your
                                    		  network's wireless access points and associated mobile devices.

This service must be running to synchronize Unified Communications Manager with a Cisco wireless access point controller.
                                    When the service is running, and synchronization is configured, Unified Communications Manager syncs its database with a Cisco
                                    wireless access point controller and saves status information for the wireless access points that the controller manages.
                                    You can schedule syncs to occur at regular intervals so that the information stays current.

Make sure that this service is running when adding a new Cisco
                                                			 wireless access point controller.

### Voice Quality Reporter Services

This section describes the Voice Quality Reporter Services and does not apply to IM and Presence Service and Cisco Unity Connection .

#### Cisco Extended
                              	 Functions

The Cisco Extended Functions service provides support for Unified Communications Manager voice-quality features, including
                                    Quality Report Tool (QRT). For more information about individual features, see the System Configuration Guide for Cisco Unified Communications Manager and the Cisco Unified IP Phone AdministrationGuide for Cisco Unified Communications Manager .

## Network Services

Installed automatically, network services include services
                           		that the system requires to function, for example, database and platform
                           		services. Because these services are required for basic functionality, you
                           		cannot activate them in the Service Activation window. If necessary, for
                           		example, for troubleshooting purposes, you may need to stop and start (or
                           		restart) a network service in the Control Center - Network Services window.

After the installation of your application, network services
                           		start automatically, as noted in the Control Center - Network Services window. The serviceability GUI categorizes services
                           into logical groups.

### Performance and Monitoring Services

#### Cisco CallManager Serviceability RTMT

The Cisco CallManager Serviceability RTMT servlet supports the IM and Presence Real-Time Monitoring Tool (RTMT), which allows you to collect and view traces, view performance monitoring objects, work
                                 with alerts, and monitor system performance and performance counters, and so on.

#### Cisco RTMT Reporter Servlet

The Cisco RTMT Reporter servlet allows you to publish reports for RTMT.

#### Cisco Log Partition Monitoring Tool

The Cisco Log Partition Monitoring Tool service supports the Log Partition Monitoring feature, which monitors the disk usage
                                 of the log partition on a node (or all nodes in the cluster) by using configured thresholds and a polling interval.

#### Cisco Tomcat Stats Servlet

The Cisco Tomcat Stats Servlet allows you to monitor the Tomcat perfmon counters by using RTMT or the CLI. Do not stop this
                                 service unless you suspect that this service is using too many resources, such as CPU time.

#### Cisco RIS Data Collector

The Real-Time Information Server (RIS) maintains real-time information such as device registration status, performance counter
                                 statistics, critical alarms generated, and so on. The Cisco RIS Data Collector service provides an interface for applications,
                                 such as the IM and Presence Real-Time Monitoring Tool (RTMT), SOAP applications, and so on, to retrieve the information that is stored in all RIS nodes
                                 in the cluster.

#### Cisco AMC Service

Used for the Real-Time Monitoring Tool (RTMT), this service, Alert Manager and Collector service, allows RTMT to retrieve
                                 real-time information that exists on the server (or on all servers in the cluster).

#### Cisco Audit Event Service

The Cisco Audit Event Service monitors and logs any administrative configuration change to the Unified Communications Manager
                                 or IM and Presence system by a user or as a result of the user action. The Cisco Audit Event Service also monitors and logs end user events
                                 such as login, logout, and IM chat room entry and exit.

### Backup and Restore Services

#### Cisco DRF Master

This does not apply to IM and Presence Service.

The CiscoDRF Master Agent service supports the DRF Master Agent, which works with the Disaster Recovery System GUI or CLI
                                 to schedule backups, perform restorations, view dependencies, check status of jobs, and cancel jobs, if necessary. The Cisco
                                 DRF Master Agent also provides the storage medium for the backup and restoration process.

#### Cisco DRF Local

The Cisco DRF Local service supports the Cisco DRF Local Agent, which acts as the workhorse for the DRF Master Agent. Components
                                 register with the Cisco DRF Local Agent to use the disaster recovery framework. The Cisco DRF Local Agent executes commands
                                 that it receives from the Cisco DRF Master Agent. Cisco DRF Local Agent sends the status, logs, and command results to the
                                 Cisco DRF Master Agent.

### System Services

#### Cisco CallManager Serviceability

The Cisco CallManager Serviceability service supports Cisco Unified Serviceability and the IM and Presence Service serviceability GUIs, which are web application/interfaces that you use to troubleshoot issues and manage services. This service,
                                 which is installed automatically, allows you access to the serviceability GUIs. If you stop this service on the server, you
                                 cannot access the serviceability GUI when you browse into that server.

#### Cisco CDP

Cisco  Discovery Protocol (CDP) advertises the voice application to other network management applications, so the network
                                 management application, for example, SNMP or Cisco Unified Operations Manager, can perform network management tasks for the
                                 voice application.

#### Cisco Trace Collection Servlet

The Cisco Trace Collection Servlet, along with the Cisco Trace Collection Service, supports trace collection and allows users
                                 to view traces by using RTMT. If you stop this service on a server, you cannot collect or view traces on that server.

For SysLog Viewer and Trace and Log Central to work in RTMT, the Cisco Trace Collection Servlet and the Cisco Trace Collection
                                 Service must run on the server.

#### Cisco Trace Collection Service

The Cisco Trace Collection Service, along with the Cisco Trace Collection Servlet, supports trace collection and allows users
                                 to view traces by using the RTMT client. If you stop this service on a server, you cannot collect or view traces on that server.

For SysLog Viewer and Trace and Log Central to work in RTMT, the Cisco Trace Collection Servlet and the Cisco Trace Collection
                                 Service must run on the server.

Tip

If necessary, Cisco recommends that, to reduce the initialization time, you restart the Cisco Trace Collection Service before
                                             you restart  Cisco Trace Collection Servlet.

### Platform
                           	 Services

#### A Cisco
                                 		  DB

A Cisco DB service supports the Progres database engine on Unified Communications Manager. On IM and Presence Service , A Cisco DB service supports the IDS database engine.

#### A Cisco DB
                                 		  Replicator

Unified Communications Manager and IM and Presence only: The A Cisco DB Replicator service ensures database configuration
                                 and data synchronization between the first and subsequent servers in the cluster.

#### Cisco
                                 		  Tomcat

The
                                 		  Cisco Tomcat service supports the web server.

#### SNMP Master
                                 		  Agent

This
                                 		  service, which acts as the agent protocol engine, provides authentication,
                                 		  authorization, access control, and privacy functions that relate to SNMP
                                 		  requests.

Tip

After you
                                             			 complete SNMP configuration in the serviceability GUI, you must restart the
                                             			 SNMP Master Agent service in the Control
                                                				Center—Network Features window.

#### MIB2
                                 		  Agent

This
                                 		  service provides SNMP access to variables, which are defined in RFC 1213, that
                                 		  read and write variables, for example, system, interfaces, and IP.

#### Host Resources
                                 		  Agent

This
                                 		  service provides SNMP access to host information, such as storage resources,
                                 		  process tables, device information, and installed software base. This service
                                 		  implements the HOST-RESOURCES-MIB.

#### Native Agent
                                 		  Adaptor

This
                                 		  service, which supports vendor Management Information Bases (MIBs), allows you
                                 		  to forward SNMP requests to another SNMP agent that runs on the system.

For IM and Presence Service and Unified Communications Manager, this service will not be present if installed on a Virtual Machine.

#### System
                                 		  Application Agent

This
                                 		  service provides SNMP access to the applications that are installed and
                                 		  executing on the system. This implements the SYSAPPL-MIB.

#### Cisco CDP
                                 		  Agent

This
                                 		  service uses the Cisco Discovery Protocol to provide SNMP access to network
                                 		  connectivity information on the node. This service implements the
                                 		  CISCO-CDP-MIB.

#### Cisco Syslog
                                 		  Agent

This service supports gathering of syslog messages that various Unified Communications Manager components generate. This service
                                 implements the CISCO-SYSLOG-MIB.

Caution

Stopping any
                                             			 SNMP service may result in loss of data because the network management system
                                             			 no longer monitors the network. Do not stop the services unless your technical
                                             			 support team tells you to do so.

#### Cisco
                                 		  Certificate Change Notification

This service keeps certificates of components like Tomcat, CallManager, and XMPP automatically synchronized across all nodes
                                 in the cluster. When the service is stopped and you regenerate certificates, then you have to manually upload them to Certificate
                                 Trust on the other nodes.

#### Platform
                                 		  Administrative Web Service

The Platform Administrative Web Service is a Simple Object Access Protocol (SOAP) API that can be activated on Unified Communications
                                 Manager, IM and Presence Service , and Cisco Unity Connection systems to allow the PAWS-M server to upgrade the system.

Important

Do not
                                             			 activate the Platform Administrative Web Service on the PAWS-M server.

#### Platform Communication Web Service

Platform Communication Web Service is a Representational State Transfer Protocol (REST) API which runs on Unified Communications
                                 Manager, IM and Presence Service , and Cisco Unity Connection systems.

You cannot start or stop the Platform Communication Web Service manually.

#### Cisco UDS Tomcat

This service avoids high resource usage on UDS which slows down other web applications or make GUI slow or inaccessible.

#### Cisco AXL Tomcat

This service avoids high resource usage on AXL which slows down other web applications or make GUI slow or inaccessible.

#### Cisco SSOSP Tomcat

This service avoids high resource usage on SSOSP which slows down other web applications or make GUI slow or inaccessible.

#### Cisco
                                 		  Certificate Expiry Monitor

This service periodically checks the expiration status of certificates that the system generates and sends notification when
                                 a certificate is close to its expiration date. For Unified Communications Manager, you manage the certificates that use this
                                 service in Cisco Unified Operating System Administration. For IM and Presence Service , you manage the certificates that use this service in Cisco Unified IM and Presence Operating System Administration.

#### Cisco Smart
                                 		  License Manager

Cisco Smart License Manager is a network service that runs only on the publisher. It manages all the Cisco Smart Licensing
                                 operations on the Unified Communications Manager publisher. Cisco Smart License Manager service reports the product's license
                                 or entitlement usage to Cisco Smart Software Manager or Cisco Smart Software Manager satellite and gets the authorization
                                 status from Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

### Security Services

#### Cisco Certificate Enrollment Service

This service creates an online connection between an online third-party CA and the Certificate Authority Proxy Function. This
                                 service must be activated in order to use an Online CA with the Certificate Authority Proxy Function for signing LSC certificates.

#### Cisco Trust Verification Service

This service is not supported by IM and Presence Service.

Cisco Trust Verification Service is a service running on a CallManager server or a dedicated server, that authenticates certificates
                                 on behalf of phones and other endpoints. It associates a list of roles for the owner of the certificate. A certificate or
                                 the owner can be associated with one or many roles.

The protocol between phones and Trust Verification Service allows phones to request for verification. Trust Verification Service
                                 validates the certificate and returns a list of roles associated with it. The protocol allows Trust Verification Service to
                                 authenticate a request and conversely, a phone to authenticate the response from Trust Verification Service. The protocol
                                 protects the integrity of the request and the response. Confidentiality of the request and the response is not required.

Multiples instances of Cisco Trust Verification Service run on different servers in the cluster to provide scalability. These
                                 servers may or may not be the same as the ones hosting the Cisco Unified CallManager. Phones obtain a list of Trust Verification
                                 Services in the network and connect to one of them using a selection algorithm (example: Round Robin). If the contacted Trust
                                 Verification Service does not respond, the phone switches to the next Trust Verification Service in the list.

### Database Services

#### Cisco Database Layer Monitor

The Cisco Database Layer Monitor service monitors aspects of the database layer. This service handles change notification
                                 and monitoring.

Unified Communications Manager uses Automatic Update Statistics, an intelligent statistics update feature that monitors the
                                             changes that are made in the database tables and updates only tables that need statistic updates. This feature saves considerable
                                             bandwidth, especially on VMware deployments of Unified Communications Manager. Automatic Update Statistics is the default
                                             indexing method.

### SOAP Services

#### Cisco SOAP-Real-Time Service APIs

IM and Presence Service only: The Cisco SOAP-Real-Time Service APIs support client login and third-party APIs for presence data.

Unified Communications Manager and Cisco Unity Connection only: The Cisco SOAP-Real-Time Service APIs allow you to collect real-time information for devices and CTI applications.
                                 This service also provides APIs for activating, starting, and stopping services.

#### Cisco SOAP-Performance-Monitoring APIs

The Cisco SOAP-Performance-Monitoring APIs service allows you to use performance monitoring counters for various applications
                                 through SOAP APIs; for example, you can monitor memory information per service, CPU usage, and performance monitoring counters.

#### Cisco SOAP-Log-Collection APIs

The Cisco SOAP-Log-Collection APIs service allows you to collect log files and to schedule collection of log files on a remote
                                 SFTP server. Examples of log files that you can collect include syslog, core dump files, and Cisco application trace files.

#### SOAP-Diagnostic Portal Database Service

The Cisco Unified Real-Time Monitoring Tool (RTMT) uses the SOAP-Diagnostic Portal Database Service to access the RTMT Analysis
                                 Manager hosting database. RTMT gathers call records based on operator-defined filter selections. If this service is stopped,
                                 RTMT cannot collect the call records from the database.

### CM Services

This section describes the Unified Communications Manager CM Services and does not apply to IM and Presence Service and Cisco Unity Connection .

#### Cisco Extension Mobility Application

The Cisco Extension Mobility Application service allows you to define login settings such as duration limits on phone configuration
                                 for the Cisco Extension Mobility feature.

Unified Communications Manager only: The Cisco Extension Mobility feature allows users within a Unified Communications Manager cluster to temporarily configure another phone in the cluster
                                 as their own phone by logging in to that other phone. After a user logs in, the phone adopts the personal phone numbers, speed
                                 dials, services links, and other user-specific properties of the user. After logout, the phone adopts the original user profile.

#### Cisco User Data Services

Cisco User Data Services provides Cisco Unified IP Phones with the ability to access user data from the Cisco Unified Communications
                                 Manager database. Cisco User Data Services provides support for Cisco Personal Directory.

#### Cisco Push Notification Service

The Cisco Push Notification Service provides functionality to send push notification for incoming calls to Apple iOS devices
                                 from Cisco Unified Communications Manager. This service relays push notification messages from the Cisco CallManager service
                                 to the Cisco Collaboration Cloud. This service also manages the access tokens used to send push notifications.

#### Cisco Headset Service

Cisco Headset Service enables you to manage inventory, configuration updates, and diagnostics data of your Cisco Headset if
                                 you use compatible Cisco IP Phones, Cisco Jabber, or other Cisco devices.

Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                             is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                             want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                             activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it.

### IM and Presence
                           	 Service Services

IM
                                    			 and Presence Service services apply only to IM and Presence Service.

#### Cisco Login
                                 		  Datastore

The Cisco Login
                                 		  Datastore is a real-time database for storing client sessions to the Cisco
                                 		  Client Profile Agent.

#### Cisco Route
                                 		  Datastore

The Cisco Route
                                 		  Datastore is a real-time database for storing a cache of route information and
                                 		  assigned users for the Cisco SIP Proxy and the Cisco Client Profile Agent.

#### Cisco Config
                                 		  Agent

The Cisco
                                 		  Configuration Agent is a change-notification service that notifies the Cisco
                                 		  SIP Proxy of configuration changes in the IM and Presence Service IDS database.

#### Cisco Sync
                                 		  Agent

The Cisco Sync Agent keeps IM and Presence data synchronized with Unified Communications Manager data. It sends SOAP requests to the Unified Communications Manager
                                 for data of interest to IM and Presence and subscribes to change notifications from Unified Communications Manager and updates the IM and Presence IDS database.

#### Cisco OAM
                                 		  Agent

The Cisco
                                 		  OAM Agent service monitors configuration parameters in the IM and Presence Service IDS database that are of
                                 		  interest to the Presence Engine. When a change is made in the database, the OAM
                                 		  Agent writes a configuration file and sends an RPC notification to the Presence
                                 		  Engine.

#### Cisco Client
                                 		  Profile Agent

The Cisco
                                 		  Client Profile Agent service provides a secure SOAP interface to or from
                                 		  external clients using HTTPS.

#### Cisco
                                 		  Intercluster Sync Agent

The Cisco Intercluster Sync Agent service provides the following: DND propagation to Unified Communications Manager and syncs
                                 end user information between IM and Presence Service clusters for intercluster SIP routing.

#### Cisco XCP
                                 		  Router

The XCP
                                 		  Router is the core communication functionality on the IM and Presence Service server. It provides XMPP-based
                                 		  routing functionality on IM and Presence Service ; it routes XMPP data to the
                                 		  other active XCP services on IM and Presence Service , and it accesses SDNS to allow
                                 		  the system to route XMPP data to IM and Presence Service users. The XCP router manages
                                 		  XMPP sessions for users, and routes XMPP messages to and from these sessions.

After IM and Presence Service installation, the system turns
                                 		  on Cisco XCP Router by default.

If you restart the
                                             			 Cisco XCP Router, IM and Presence Service automatically restarts all
                                             			 active XCP services. Note that you must select the Restart option to restart
                                             			 the Cisco XCP Router; this is not the same as turning off and turning on the
                                             			 Cisco XCP Router. If you turn off the Cisco XCP Router, rather than restart
                                             			 this service, IM and Presence Service stops all other XCP services.
                                             			 Subsequently when you turn on the XCP router, IM and Presence Service does not automatically turn on
                                             			 the other XCP services; you need to manually turn on the other XCP services.

#### Cisco XCP Config
                                 		  Manager

The Cisco
                                 		  XCP Config Manager service monitors the configuration and system topology
                                 		  changes made through the administration GUI (as well as topology changes that
                                 		  are synchronized from an InterCluster Peer) that affect other XCP components
                                 		  (for example, Router and Message Archiver), and updates these components as
                                 		  needed. The Cisco XCP Config Manager service creates notifications for the
                                 		  administrator indicating when an XCP component requires a restart (due to these
                                 		  changes), and it automatically clears the notifications after the restarts are
                                 		  complete.

#### Cisco Server
                                 		  Recovery Manager

The Cisco Server Recovery
                                 		  Manager (SRM) service manages the failover between nodes in a presence
                                 		  redundancy group. The SRM manages all state changes in a node; state changes
                                 		  are either automatic or initiated by the administrator (manual). Once you turn
                                 		  on high availability in a presence redundancy group, the SRM on each node
                                 		  establishes heartbeat connections with the peer node and begins to monitor the
                                 		  critical processes.

#### Cisco IM and Presence Data Monitor

The Cisco IM and Presence Data Monitor monitors IDS replication state
                                 		  on the IM and Presence Service. Other IM and Presence services are dependent on
                                 		  the Cisco IM and Presence Data Monitor. These dependent services use the Cisco
                                 		  service to delay startup until such time as IDS replication is in a stable
                                 		  state.

The Cisco IM and Presence Data Monitor also checks the status of the Cisco Sync Agent sync from Unified Communications Manager.
                                 Dependent services are only allowed to start after IDS replication has set up and the Sync Agent on the IM and Presence database
                                 publisher node has completed its sync from Unified Communications Manager. After the timeout has been reached, the Cisco IM
                                 and Presence Data Monitor on the Publisher node will allow dependent services to start even if IDS replication and the Sync
                                 Agent have not completed.

On the subscriber nodes, the Cisco IM and Presence Data Monitor delays
                                 		  the startup of feature services until IDS replication is successfully
                                 		  established. The Cisco IM and Presence Data Monitor only delays the startup of
                                 		  feature services on the problem subscriber node in a cluster, it will not delay
                                 		  the startup of feature services on all subscriber nodes due to one problem
                                 		  node. For example, if IDS replication is successfully established on node1 and
                                 		  node2, but not on node3, the Cisco IM and Presence Data Monitor allows feature
                                 		  services to start on node1 and node2, but delays feature service startup on
                                 		  node3.

#### Cisco Presence
                                 		  Datastore

The Cisco Presence
                                 		  Datastore is a real-time database for storing transient presence data and
                                 		  subscriptions.

#### Cisco SIP
                                 		  Registration Datastore

The Cisco Presence
                                 		  SIP Registration Datastore is a real-time database for storing SIP Registration
                                 		  data.

#### Cisco RCC Device Selection

The Cisco RCC Device Selection service is the Cisco IM and Presence user device selection service for Remote Call Control.

### CDR Services

This section describes the CDR Services and does not apply to IM and Presence Service and Cisco Unity Connection .

#### Cisco CDR Repository Manager

This service maintains and moves the generated Call Detail Records (CDRs) that are obtained from the Cisco CDR Agent service.
                                 In a system that supports clusters (Unified Communications Manager only), the service exists on the first server.

#### Cisco CDR Agent

Unified Communications Manager supports Cisco CDR Agent in Cisco Unified Communications Manager systems.

This service does not support IM and Presence Service and Cisco Unity Connection .

The Cisco CDR Agent service transfers CDR and CMR files that are generated by Unified Communications Manager from the local
                                 host to the CDR repository server, where the CDR Repository Manager service runs over a SFTP connection.

This service transfers CDR and CMR files generated from the local host to the CDR repository server in a cluster. The CDR
                                 Agent in the CDR Repository Node standalone server transfers the files that are generated by the standalone server to the
                                 Cisco CDR Repository Manager over a SFTP connection. The CDR Agent maintains and moves the files.

For this service to work, activate the Cisco CallManager service on the server and ensure that it is running. If your configuration
                                 supports clusters (Unified Communications Manager only), activate the Cisco CallManager service on the first server.

#### Cisco CAR Scheduler

The  Cisco CDR Analysis and Reporting (CAR) Scheduler service does not support IM and Presence Service and Cisco Unity Connection .

The Cisco CAR Scheduler service allows you to schedule CAR-related tasks; for example, you can schedule report generation
                                 or CDR file loading into the CAR database.

#### Cisco SOAP-CallRecord Service

The Cisco SOAP-CallRecord service runs by default on the publisher as a SOAP server, so that the client can connect to CAR
                                 database through the SOAP API. This connection happens through the use of the CAR connector (with a separate CAR IDS instance).

#### Cisco CAR DB

Cisco CAR DB manages the Informix instance for the CAR database, which allows Service Manager to start or stop this service
                                 and to bring up or shut down the CAR IDS instance respectively. This is similar to the Unified Communications Manager database
                                 that is used to maintain the CCM IDS instance.

The Cisco CAR DB service is activated on the publisher by default.  The CAR DB instances are installed and actively run on
                                 the publisher, to maintain the CAR database. This network service is used only on the publisher and is not available on the
                                 subscribers.

### Admin Services

This section describes the Admin Services and does not apply to Cisco Unity Connection .

#### Cisco CallManager Admin

The Cisco CallManager Admin service  is not supported by IM and Presence Service and Cisco Unity Connection .

The Cisco CallManager Admin service supports Cisco Unified Communications Manager Administration, the web application/interface
                                 that you use to configure Unified Communications Manager settings. After the Unified Communications Manager installation,
                                 this service starts automatically and allows you to access the graphical user interface (GUI). If you stop this service, you
                                 cannot access the Cisco Unified Communications Manager Administration graphical user interface when you browse into that server.

#### Cisco IM and Presence Admin

The Cisco IM and Presence Admin service is not supported by Unified Communications Manager and Cisco Unity Connection .

The Cisco IM and Presence Admin service supports Cisco Unified Communications Manager IM and Presence Administration, the
                                 web application/interface that you use to configure IM and Presence Service settings. After the IM and Presence Service installation, this service starts automatically and allows you to access the GUI. If you stop this service, you cannot access
                                 the Cisco Unified Communications Manager IM and Presence Administration GUI when you browse into that server.

### Services setup

## Control Center

From Control Center in 
                           		the serviceability GUI, you can view status and start and stop one service at
                           		a time. To start, stop,
                           		and restart network services, access the Control Center - Network Services
                           		window. To start, stop, and restart feature services, access the Control Center
                           		- Feature Services window.

Tip

Use the Related Links drop-down list box and the Go button to navigate
                                       		  to Control Center and Service Activation windows.

Unified Communications Manager and IM and Presence only: In a cluster configuration, you can view status and start and stop
                           services for one server in the cluster at a time.

Unified Communications Manager only: Starting and stopping a feature service causes all Cisco Unified IP Phone s and gateways that are currently registered to that service to fail over to their secondary service. Devices and phones need
                           to restart only if they cannot register with their secondary service. Starting and stopping a service may cause other installed
                           applications (such as a conference bridge or Cisco Messaging Interface) that are homed to that Unified Communications Manager
                           to start and stop as well.

Caution

Unified Communications Manager only: Stopping a service also stops call processing for all devices that the service controls.
                                       When a service is stopped, calls from an IP phone to another IP phone stay up; calls in progress from an IP phone to a Media
                                       Gateway Control Protocol (MGCP) gateway also stay up, but other types of calls drop.

## Set Up Services

You can perform the following tasks when working with services:

Step 1

Activate the feature services that you want to run.

Step 2

Configure the appropriate service parameters.

Step 3

If necessary, troubleshoot problems by using the 
                                       			 serviceability GUI  trace tools.

## Service
                        	 Activation

You can activate or deactivate multiple feature services or choose default services to activate from the Service Activation
                                       window in the serviceability GUI. You can view, start, and stop Unified Communications Manager services from an IM and Presence
                                       node and vice versa. You may encounter the following error: "Connection to the Server cannot be established (unable to access
                                       Remote Node)". If this error message appears, see the Administration Guide for Cisco Unified Communications Manager .

Starting with Unified Communications Manager Release 6.1.1, end users can no longer access Cisco Unified Serviceability to start and stop services.

Feature
                           		services are activated in automatic mode and the serviceability GUI checks for
                           		service dependencies based on a single-node configuration. When you choose to
                           		activate a feature service, you are prompted to select all the other services,
                           		if any, that depend on that service to run. When you click Set
                              		  Default , the serviceability GUI chooses those services that are
                           		required to run on the server.

Unified Communications Manager and IM and Presence Service only: Even in a configuration that supports clusters, this process is based on a single-server configuration.

Activating a
                           		service automatically starts the service. You start and stop services from
                           		Control Center.

## Cluster Service
                        	 Activation Recommendations for Cisco Unified Communications Manager

Before you activate services in a cluster, review the following table, which provides service recommendations for multiserver
                              Unified Communications Manager configurations.

Service/Servlet

Activation Recommendations

CM
                                          					 Services

Cisco CallManager

This service supports Unified Communications Manager.

In
                                          					 the Control Center - Network Services, ensure that the Cisco RIS Data Collector
                                          					 service and Database Layer Monitor service are running on the node.

Tip

Before you activate this service, verify that the Unified Communications Manager server displays in the Unified Communications
                                                      Manager Find/List window in Cisco Unified Communications Manager Administration . If the server does not display, add the Unified Communications Manager server before you activate this service.

For information on how to
                                                      						add a server, see the System Configuration Guide for Cisco Unified Communications
                                                         						  Manager .

Cisco Messaging Interface

Activate only if using an SMDI integration to a third-party Voicemail system
                                          					 using a server-attached USB-to-serial adapter.

Cisco Unified Mobile Voice Access Service

For
                                          					 mobile voice access to work, you must activate this service on the first node
                                          					 in the cluster after you configure the H.323 gateway to point to the first VXML
                                          					 page. In addition, make sure that the Cisco CallManager and the Cisco TFTP
                                          					 services run on one server in the cluster, not necessarily the same server
                                          					 where the Cisco Unified Mobile Voice Access Service runs.

Cisco IP Voice Media Streaming App

If
                                          					 you have more than one node in the cluster, activate on one or two servers per
                                          					 cluster. You may activate on a node that is dedicated specifically for music on
                                          					 hold. This service requires that you activate Cisco TFTP on one node in the
                                          					 cluster. Do not activate this service on the first node or on any nodes that
                                          					 run the Cisco CallManager service.

Cisco CTIManager

Activate on each node to which JTAPI/TAPI applications will
                                          					 connect. CTIManager activation requires the Cisco CallManager service also to
                                          					 be activated on the node. See topics related to CM services for more
                                          					 information on CTIManager and Cisco CallManager services interaction.

Cisco Extension Mobility

Activate on all nodes in the cluster.

Cisco Extended Functions

Activate this service, which supports the Quality Report Tool
                                          					 (QRT), on one or more servers that run the Cisco RIS Data Collector. Make sure
                                          					 that you activate the Cisco CTIManager service on a node in the cluster.

Cisco DHCP Monitor Service

When the DHCP Monitor service is enabled, it detects changes in
                                          					 the database that affect IP addresses for the IP phones, modifies the
                                          					 /etc/dhcpd.conf file, and stops and restarts the DHCPD daemon with the updated
                                          					 configuration file. Activate this service on the node that has DHCP enabled.

Cisco
                                          					 Location Bandwidth Manager

If you
                                          					 plan to use Cisco Location Call Admission Control functionality to manage
                                          					 bandwidth allocation for audio and video calls, you must activate this service.
                                          					 This service works in conjunction with the Cisco CallManager service. It is
                                          					 recommended to run the Cisco Location Bandwidth Manager on the same server that
                                          					 runs the Cisco CallManager service. If the Location Bandwidth Manager is not
                                          					 running on the same server as the CallManager service, ensure that you
                                          					 configure the Location Bandwidth Manager Group correctly.

Cisco
                                          					 Intercluster Lookup Service

If you plan to propagate the URI and numeric routing information between multiple Unified Communications Manager clusters,
                                          you must activate this service on the publisher of the cluster that participates in this exchange.

Cisco Dialed Number Analyzer Server

If
                                          					 you have more than one node in the cluster, activate this service on one node
                                          					 that is dedicated specifically for the Cisco Dialed Number Analyzer service.

Cisco Dialed Number Analyzer

If you are planning to use Unified Communications Manager Dialed Number Analyzer , activate this service. This service may consume a lot of resources, so only activate this service on the node with the least
                                          amount of call-processing activity or during off-peak hours.

Cisco TFTP

If
                                          					 you have more than one node in the cluster, activate this service on one node
                                          					 that is dedicated specifically for the Cisco TFTP service. Configure Option 150
                                          					 if you activate this service on more than one node in the cluster.

Cisco Headset Service

Activate this service if you plan to manage your Cisco headsets from Unified Communications Manager.

Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                                      is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                                      want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                                      activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it.

CTI
                                          					 Services

Cisco IP Manager Assistant

If
                                          					 you are planning to use Cisco Unified Communications
                                             						Manager Assistant , activate this service on any two servers (Primary
                                          					 and Backup) in the cluster. Ensure that Cisco CTI Manager service is activated
                                          					 in the cluster.

See the Feature Configuration Guide for Cisco Unified Communications
                                                						  Manager for more details on Cisco IP Manager
                                          					 Assistant.

Cisco WebDialer Web Service

Activate on one node per cluster.

Self-Provisioning IVR

To enable
                                          					 the Self-Provisioning IVR service, you must also enable the Cisco CTI Manager
                                          					 service.

You can
                                          					 configure self-provisioning even if the service is deactivated, but the
                                          					 administrator cannot assign IP phones to users using the IVR service. By
                                          					 default, this service is deactivated.

CDR Services

Cisco SOAP-CDRonDemand Service

You can activate the Cisco SOAP-CDROnDemand Service only on the
                                          					 first server, and it requires that the Cisco CDR Repository Manager and Cisco
                                          					 CDR Agent services are running on the same server.

For Unified Communications Manager Release 12.x and later releases, CDR onDemand Service is not enabled by default. If you
                                          want to enable the CDR onDemand service, the service should be activated manually. Execute the following command at the root
                                          level to activate the CDR onDemand service: /usr/local/cm/bin/soapservicecontrol2.shCDRonDemandServiceCDRonDemanddeploy8443 .

Cisco CAR Web Service

You can activate the Cisco CAR Web Service only on the first
                                          					 server, and it requires that the Cisco CAR Scheduler service is activated and
                                          					 running on the same server and that the CDR Repository Manager service also is
                                          					 running on the same server.

Database and Admin Services

Cisco AXL Web Service

Following installation,
                                          					 Cisco AXL Web Service is enabled by default on all cluster nodes. Cisco
                                          					 recommends that you always leave the service activated on the publisher node.
                                          					 This ensures that you are able to configure products that are dependent on AXL,
                                          					 such as Unified Provisioning Manager.

Based on your needs, you
                                          					 can activate or deactivate the service on specific subscriber nodes in Cisco
                                          					 Unified Serviceability under Feature Services.

Cisco Bulk Provisioning Service

You can activate the Cisco Bulk Provisioning Service only on the
                                          					 first node. If you use the Bulk Administration
                                             						Tool (BAT) to administer phones and users, you must activate this
                                          					 service.

Cisco UXL
                                          					 Web Service

This
                                          					 service performs authentication and user authorization checks. The TabSync
                                          					 client in Cisco IP Phone Address Book Synchronizer uses the Cisco UXL Web
                                          					 Service for queries to the Cisco Unified Communications Manager database.

If you
                                          					 plan to use the Cisco IP Phone Address Book Synchronizer, you must activate
                                          					 this service on one node, preferably publisher. If you are not using Cisco IP
                                          					 Phone Address Book Synchronizer, then Cisco recommends that you deactivate this
                                          					 service . By default, this service is deactivated.

Cisco
                                          					 Platform Administrative Web Service

You must
                                          					 activate this service if you plan to use a Cisco Prime Collaboration Deployment
                                          					 (PCD) server to manage upgrades, switch version, restart or readdress
                                          					 operations. Platform Administrative Web Service (PAWS) allows SOAP
                                          					 communication between the Call Manager and Prime Collaboration Deployment
                                          					 (PCD). If you have more than one node in the cluster, you must activate this
                                          					 service on each server in the cluster.

Cisco TAPS Service

Before you can use the Cisco Unified Communications Manager Auto-Register Phone Tool , you must activate this service on the first node. When you create dummy MAC addresses for the Cisco Unified Communications Manager Auto-Register Phone Tool , ensure that the Cisco Bulk Provisioning Service is activated on the same node.

Performance and Monitoring Services

Cisco Serviceability Reporter

Activate on only the first node.

The
                                                      						service only generates reports on the first node even if you activate the
                                                      						service on other nodes.

Cisco CallManager SNMP Service

If you use SNMP, activate this service on all servers in the
                                          					 cluster.

Security Services

Cisco CTL Provider

Activate on all servers in the cluster.

Cisco Certificate Authority Proxy Function (CAPF)

Activate on only the first node.

Directory Services

Cisco DirSync

Activate only on the first node.

## Cluster Service Activation Recommendations for IM and Presence Service

Caution

Before you turn on any services for a feature, you must complete all the required configuration on IM and Presence for that feature. See the relevant documentation for each IM and Presence feature.

Before you turn on services in a cluster, review the following table, which provides service recommendations for multinode IM and Presence configurations.

Service/Servlet

Recommendations

Database and Admin Services

Cisco AXL Web Service

Following installation, Cisco AXL Web Service is enabled by default on all cluster nodes. Cisco recommends that you always
                                          leave the service activated on the IM and Presence Service database publisher node. This ensures that you are able to configure products that are dependent on AXL. If intercluster
                                          communication is configured, this service must be enabled on both nodes  in the sub-cluster where remote peers are configured
                                          to sync from. If this service is not enabled on both nodes presence and IM capabilities will be lost  in failover scenarios.

Based on your needs, you can activate or deactivate the service on specific IM and Presence subscriber nodes in Cisco Unified Serviceability under Feature Services.

Cisco Bulk Provisioning Service

- You turn on the Cisco Bulk Provisioning Service only on the first node.

- If you use the Bulk Administration Tool (BAT) to administer users, you must turn on this service.

Performance and Monitoring Services

Cisco Serviceability Reporter

The service only generates reports on the publisher node even if you turn on the service on other nodes.

IM and Presence Services

Cisco SIP Proxy

Turn on this service on all nodes in the cluster.

Cisco Presence Engine

Turn on this service on all nodes in the cluster.

Cisco Sync Agent

Turn on this service on all nodes in the cluster.

Cisco XCP Text Conference Manager

- Turn on this service if you deploy the chat feature on IM and Presence .

- Turn on this service on each node that runs the chat feature.

The permanent chat feature requires an external database. If you enable the permanent chat feature, you must also configure
                                                      an external database before starting the Text Conference Manager service. The Text Conference Manager service will not start
                                                      if the permanent chat feature is enabled and an external database is not configured. See the Database Setup Guide for IM and Presence on Unified Communications Manager .

Cisco XCP Web Connection Manager

- Turn on this service if you integrate web clients with IM and Presence .

- Turn on this service on all nodes in the cluster.

Cisco XCP Connection Manager

- Turn on this service if you integrate XMPP clients with IM and Presence .

- Turn on this service on all nodes in the cluster.

Cisco XCP SIP Federation Connection Manager

Interdomain federation over the SIP protocol on IM and Presence . Turn on this service on each node that runs SIP federation.

Intercluster deployment between a IM and Presence Release 9.x cluster and a Cisco Unified Presence Release 8.6(x) cluster. Turn on this service on all nodes in the Release 9.x cluster.

Cisco XCP XMPP Federation Connection Manager

- Turn on this service only if you deploy interdomain federation over the XMPP protocol on IM and Presence .

- Turn on this service on each node that runs XMPP federation.

Before you turn on the XMPP Federation Connection Manager service on a node, you must turn on XMPP Federation in Cisco Unified
                                                      Communications Manager IM and Presence Administration on that node. See Interdomain Federation for IM and Presence on Unified Communications Manager .

Cisco XCP Message Archiver

- Turn on this service if you deploy the Compliance feature on IM and Presence .

- Turn on this service on any node that runs the IM Compliance feature.

If you turn on the Message Archiver before you configure an external database, the service will not start. Also, if the external
                                                      database is not reachable, the service will not start. See the Database Setup Guide for IM and Presence on Unified Communications Manager .

Cisco XCP Directory Service

- Turn on this service if you integrate XMPP clients on IM and Presence with an LDAP directory.

- Turn on this service on all nodes in the cluster.

If you turn on the Directory Service before you configure the LDAP contact search settings for third-party XMPP clients, the
                                                      service will start, and then stop again. See Configuration and Administration of IM and Presence Service on Unified Communications Manager .

Cisco XCP Authentication Service

- Turn on this service if you integrate XMPP clients with IM and Presence .

- Turn on this service on all nodes in the cluster.

## Activate Feature
                        	 Services

You activate
                              		  and deactivate feature services in the Service
                                 			 Activation window in the serviceability GUI. Services that display
                              		  in the Service
                                 			 Activation window do not start until you activate them.

You can
                              		  activate and deactivate only features services (not network services). You may
                              		  activate or deactivate as many services as you want at the same time. Some
                              		  feature services depend on other services, and the dependent services get
                              		  activated before the feature service activates.

Tip

Unified Communications Manager and IM and Presence Service only: Before you activate services in the Service Activation window, review topics related to cluster service activation
                                          recommendations.

Step 1

Choose Tools > Service
                                             				  Activation .

The Service
                                             				  Activation window displays.

Step 2

Select the
                                       			 server (node) from the Server drop-down list, and then click Go .

You can access Unified Communications Manager services from an IM and Presence Service node and vice versa. You may encounter the following error when trying to access a remote node: "Connection to the Server
                                          cannot be established (unable to connect to Remote Node)". If this error message appears, see the Administration Guide for Cisco Unified Communications Manager .

Step 3

Perform one of
                                       			 the following actions to turn on or turn off services:

To turn on
                                             				  the default services required to run on a single server, select Set
                                                					 to Default .

This
                                                            						option selects default services based on the configuration of a single server,
                                                            						and checks for service dependencies.

To turn on
                                             				  all services, check Check All Services .

To turn on a
                                             				  specific service, check the check box for the service that you want to turn on

To turn off
                                             				  a service, uncheck the check box for the services that you want to turn off.

Step 4

Unified Communications Manager and IM and Presence Service only: For a cluster configuration, review the cluster service activation recommendations, and then check the check boxes
                                       next to the services that you want to activate.

Step 5

After you check
                                       			 the check boxes for the services that you want to activate, click Save .

Tip

To deactivate
                                                      				  services that you activated, uncheck the check boxes next to the services that
                                                      				  you want to deactivate; then, click Save .

Tip

To obtain the
                                                      				  latest status of the services, click the Refresh button.

## Start, Stop, and Restart Services in Control Center or CLI

To perform these tasks, the serviceability GUI provides two Control Center windows. To start, stop, and restart network services,
                              access the Control Center—Network Services window. To start, stop, and restart feature services, access the Control Center—Feature Services window.

Tip

Use the Related Links list box and the Go button to navigate to Control Center and Service Activation windows.

### Start, Stop, and Restart Services in Control Center

- view status

- refresh status

- start, stop, and restart feature and network services on a particular server, or for a server in a cluster in a cluster configuration

When a service is
                                 		  stopping, you cannot start it until after the service is stopped.

Caution

Unified Communications Manager only: Stopping a service also stops call processing for all devices that the service controls.
                                             When a service is stopped, calls from an IP phone to another IP phone remain connected; calls in progress from an IP phone
                                             to a Media Gateway Control Protocol (MGCP) gateway also remain connected, but other types of calls get dropped.

Step 1

Depending on the service type that you want to
                                          			 start/stop/restart/refresh, perform one of the following tasks:

Choose Tools > Control
                                                         						Center - Feature Services .

Tip

Before you can start, stop, or restart a feature service, it must
                                                               						be activated.

Choose Tools > Control
                                                         						Center - Network Services .

Step 2

Choose the server from the Server drop-down list, and then click Go .

The window displays the following items:

The service names for the server that you chose.

The service group.

The service status, for example, Started, Running, Not
                                                   				  Running, and so on. (Status column).

The exact time that the service started running. (Start Time
                                                   				  column).

The amount of time that the service has been running. (Up Time
                                                   				  column).

Step 3

Perform one of the following tasks:

Click the radio button next to the service that you want to
                                                   				  start,  and then click Start .
                                                   				The Status changes to reflect the updated status.

Click the radio button next to the service that you want to
                                                   				  stop,  and then click Stop .
                                                   				 The Status changes to reflect the updated status.

Click the radio button next to the service that you want to
                                                   				  restart,  and then click Restart . A message indicates that restarting may take a while. Click OK .

Click Refresh to get the latest status of the services.

To go to the Service Activation window or to the other Control
                                                   				  Center window, choose an option from the Related Links drop-down list, and
                                                   				  then click Go .

### Start, Stop, and Restart Services Using Command Line Interface

You can start and stop some services through the CLI. For a list of services that you can start and stop through the CLI and
                              for information on how to perform these tasks, refer to the Command Line Interface Reference Guide for Cisco Unified Solutions .

Tip

You must start and stop most services from Control Center in the serviceability GUI.

| Note | If you try to access a Unified Communications Manager server from an IM and Presence node or vice versa, you may encounter
                                          the following error: "Connection to the Server cannot be established (unable to access Remote Node)" . If this error message
                                          appears, see the Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Note | Devices using IM and Presence are configured to use a Postgres external database to support persistent chat, compliance, and
                                          file transfer. However, the connection between IM and Presence server and Postgres is not secured and the data passes without
                                          any check. For the services or devices that do not support TLS, there is another way to provide secure communication by configuring
                                          IP Sec, which is a standard protocol for secure communications by authenticating and encrypting each IP packet of a communication
                                          session. |
|---|---|

| Tip | The Cisco Unified Communications Manager Auto-Register Phone Tool relies on Cisco Customer Response Solutions (CRS). Before the tool can work as designed, verify that the CRS server is configured
                                                and running, as described in the CRS documentation. |
|---|---|

| Important | Do not activate the Platform Administrative Web Service on the PAWS-M server. |
|---|---|

| Tip | Unified Communications Manager clusters only: Before you activate this service, verify that the Unified Communications Manager
                                                server displays in the Find and List Cisco Unified Communications Manager's window in Cisco Unified Communications Manager
                                                Administration. If the server does not display, add the Unified Communications Manager server before you activate this service.
                                                For information on how to find and add the server, see the Administration Guide for Cisco Unified Communications Manager . Unified Communications Manager clusters only: If you deactivate the Cisco CallManager or CTIManager services in Service Activation,
                                                the Unified Communications Manager server where you deactivated the service no longer exists in the database, which means
                                                that you cannot choose that Unified Communications Manager server for configuration operations in Cisco Unified Communications
                                                Manager Administration because it does not display in the graphical user interface (GUI). If you then reactivate the services
                                                on the same Unified Communications Manager server, the database creates an entry for Unified Communications Manager again
                                                and adds a "CM_" prefix to the server name or IP address; for example, if you reactivate the Cisco CallManager or CTIManager service on a
                                                server with an IP address of 172.19.140.180, then CM_172.19.140.180 displays in Cisco Unified Communications Manager Administration.
                                                You can now choose the server, with the new "CM_" prefix, in Cisco Unified Communications Manager Administration. |
|---|---|

| Note | Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                                is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                                want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                                activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it. |
|---|---|

| Note | Unified Communications Manager only: When you view real-time information in the Real-Time Monitoring Tool (RTMT), the CAPF
                                                service displays only for the first server. |
|---|---|

| Note | Users with duplicate email IDs are not synchronized and the administrator receives no notification about the list of users
                                                   which are not synced. These IDS are shown in the DirSync error logs from Unified RTMT. |
|---|---|

| Note | Make sure that this service is running when adding a new Cisco
                                                			 wireless access point controller. |
|---|---|

| Tip | If necessary, Cisco recommends that, to reduce the initialization time, you restart the Cisco Trace Collection Service before
                                             you restart  Cisco Trace Collection Servlet. |
|---|---|

| Tip | After you
                                             			 complete SNMP configuration in the serviceability GUI, you must restart the
                                             			 SNMP Master Agent service in the Control
                                                				Center—Network Features window. |
|---|---|

| Caution | Stopping any
                                             			 SNMP service may result in loss of data because the network management system
                                             			 no longer monitors the network. Do not stop the services unless your technical
                                             			 support team tells you to do so. |
|---|---|

| Important | Do not
                                             			 activate the Platform Administrative Web Service on the PAWS-M server. |
|---|---|

| Note | You cannot start or stop the Platform Communication Web Service manually. |
|---|---|

| Note | Unified Communications Manager uses Automatic Update Statistics, an intelligent statistics update feature that monitors the
                                             changes that are made in the database tables and updates only tables that need statistic updates. This feature saves considerable
                                             bandwidth, especially on VMware deployments of Unified Communications Manager. Automatic Update Statistics is the default
                                             indexing method. |
|---|---|

| Note | Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                             is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                             want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                             activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it. |
|---|---|

| Note | If you restart the
                                             			 Cisco XCP Router, IM and Presence Service automatically restarts all
                                             			 active XCP services. Note that you must select the Restart option to restart
                                             			 the Cisco XCP Router; this is not the same as turning off and turning on the
                                             			 Cisco XCP Router. If you turn off the Cisco XCP Router, rather than restart
                                             			 this service, IM and Presence Service stops all other XCP services.
                                             			 Subsequently when you turn on the XCP router, IM and Presence Service does not automatically turn on
                                             			 the other XCP services; you need to manually turn on the other XCP services. |
|---|---|

| Note | Unified Communications Manager supports Cisco CDR Agent in Cisco Unified Communications Manager systems. |
|---|---|

| Tip | Use the Related Links drop-down list box and the Go button to navigate
                                       		  to Control Center and Service Activation windows. |
|---|---|

| Caution | Unified Communications Manager only: Stopping a service also stops call processing for all devices that the service controls.
                                       When a service is stopped, calls from an IP phone to another IP phone stay up; calls in progress from an IP phone to a Media
                                       Gateway Control Protocol (MGCP) gateway also stay up, but other types of calls drop. |
|---|---|

| Step 1 | Activate the feature services that you want to run. |
|---|---|
| Step 2 | Configure the appropriate service parameters. |
| Step 3 | If necessary, troubleshoot problems by using the 
                                       			 serviceability GUI  trace tools. |

| Note | You can activate or deactivate multiple feature services or choose default services to activate from the Service Activation
                                       window in the serviceability GUI. You can view, start, and stop Unified Communications Manager services from an IM and Presence
                                       node and vice versa. You may encounter the following error: "Connection to the Server cannot be established (unable to access
                                       Remote Node)". If this error message appears, see the Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Note | Starting with Unified Communications Manager Release 6.1.1, end users can no longer access Cisco Unified Serviceability to start and stop services. |
|---|---|

| Service/Servlet | Activation Recommendations |
|---|---|
| CM
                                          					 Services |
| Cisco CallManager | This service supports Unified Communications Manager. In
                                          					 the Control Center - Network Services, ensure that the Cisco RIS Data Collector
                                          					 service and Database Layer Monitor service are running on the node. Tip Before you activate this service, verify that the Unified Communications Manager server displays in the Unified Communications
                                                      Manager Find/List window in Cisco Unified Communications Manager Administration . If the server does not display, add the Unified Communications Manager server before you activate this service. For information on how to
                                                      						add a server, see the System Configuration Guide for Cisco Unified Communications
                                                         						  Manager . | Tip | Before you activate this service, verify that the Unified Communications Manager server displays in the Unified Communications
                                                      Manager Find/List window in Cisco Unified Communications Manager Administration . If the server does not display, add the Unified Communications Manager server before you activate this service. For information on how to
                                                      						add a server, see the System Configuration Guide for Cisco Unified Communications
                                                         						  Manager . |
| Tip | Before you activate this service, verify that the Unified Communications Manager server displays in the Unified Communications
                                                      Manager Find/List window in Cisco Unified Communications Manager Administration . If the server does not display, add the Unified Communications Manager server before you activate this service. For information on how to
                                                      						add a server, see the System Configuration Guide for Cisco Unified Communications
                                                         						  Manager . |
| Cisco Messaging Interface | Activate only if using an SMDI integration to a third-party Voicemail system
                                          					 using a server-attached USB-to-serial adapter. |
| Cisco Unified Mobile Voice Access Service | For
                                          					 mobile voice access to work, you must activate this service on the first node
                                          					 in the cluster after you configure the H.323 gateway to point to the first VXML
                                          					 page. In addition, make sure that the Cisco CallManager and the Cisco TFTP
                                          					 services run on one server in the cluster, not necessarily the same server
                                          					 where the Cisco Unified Mobile Voice Access Service runs. |
| Cisco IP Voice Media Streaming App | If
                                          					 you have more than one node in the cluster, activate on one or two servers per
                                          					 cluster. You may activate on a node that is dedicated specifically for music on
                                          					 hold. This service requires that you activate Cisco TFTP on one node in the
                                          					 cluster. Do not activate this service on the first node or on any nodes that
                                          					 run the Cisco CallManager service. |
| Cisco CTIManager | Activate on each node to which JTAPI/TAPI applications will
                                          					 connect. CTIManager activation requires the Cisco CallManager service also to
                                          					 be activated on the node. See topics related to CM services for more
                                          					 information on CTIManager and Cisco CallManager services interaction. |
| Cisco Extension Mobility | Activate on all nodes in the cluster. |
| Cisco Extended Functions | Activate this service, which supports the Quality Report Tool
                                          					 (QRT), on one or more servers that run the Cisco RIS Data Collector. Make sure
                                          					 that you activate the Cisco CTIManager service on a node in the cluster. |
| Cisco DHCP Monitor Service | When the DHCP Monitor service is enabled, it detects changes in
                                          					 the database that affect IP addresses for the IP phones, modifies the
                                          					 /etc/dhcpd.conf file, and stops and restarts the DHCPD daemon with the updated
                                          					 configuration file. Activate this service on the node that has DHCP enabled. |
| Cisco
                                          					 Location Bandwidth Manager | If you
                                          					 plan to use Cisco Location Call Admission Control functionality to manage
                                          					 bandwidth allocation for audio and video calls, you must activate this service.
                                          					 This service works in conjunction with the Cisco CallManager service. It is
                                          					 recommended to run the Cisco Location Bandwidth Manager on the same server that
                                          					 runs the Cisco CallManager service. If the Location Bandwidth Manager is not
                                          					 running on the same server as the CallManager service, ensure that you
                                          					 configure the Location Bandwidth Manager Group correctly. |
| Cisco
                                          					 Intercluster Lookup Service | If you plan to propagate the URI and numeric routing information between multiple Unified Communications Manager clusters,
                                          you must activate this service on the publisher of the cluster that participates in this exchange. |
| Cisco Dialed Number Analyzer Server | If
                                          					 you have more than one node in the cluster, activate this service on one node
                                          					 that is dedicated specifically for the Cisco Dialed Number Analyzer service. |
| Cisco Dialed Number Analyzer | If you are planning to use Unified Communications Manager Dialed Number Analyzer , activate this service. This service may consume a lot of resources, so only activate this service on the node with the least
                                          amount of call-processing activity or during off-peak hours. |
| Cisco TFTP | If
                                          					 you have more than one node in the cluster, activate this service on one node
                                          					 that is dedicated specifically for the Cisco TFTP service. Configure Option 150
                                          					 if you activate this service on more than one node in the cluster. |
| Cisco Headset Service | Activate this service if you plan to manage your Cisco headsets from Unified Communications Manager. Note Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                                      is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                                      want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                                      activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it. | Note | Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                                      is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                                      want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                                      activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it. |
| Note | Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                                      is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                                      want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                                      activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it. |
| CTI
                                          					 Services |
| Cisco IP Manager Assistant | If
                                          					 you are planning to use Cisco Unified Communications
                                             						Manager Assistant , activate this service on any two servers (Primary
                                          					 and Backup) in the cluster. Ensure that Cisco CTI Manager service is activated
                                          					 in the cluster. See the Feature Configuration Guide for Cisco Unified Communications
                                                						  Manager for more details on Cisco IP Manager
                                          					 Assistant. |
| Cisco WebDialer Web Service | Activate on one node per cluster. |
| Self-Provisioning IVR | To enable
                                          					 the Self-Provisioning IVR service, you must also enable the Cisco CTI Manager
                                          					 service. You can
                                          					 configure self-provisioning even if the service is deactivated, but the
                                          					 administrator cannot assign IP phones to users using the IVR service. By
                                          					 default, this service is deactivated. |
| CDR Services |
| Cisco SOAP-CDRonDemand Service | You can activate the Cisco SOAP-CDROnDemand Service only on the
                                          					 first server, and it requires that the Cisco CDR Repository Manager and Cisco
                                          					 CDR Agent services are running on the same server. For Unified Communications Manager Release 12.x and later releases, CDR onDemand Service is not enabled by default. If you
                                          want to enable the CDR onDemand service, the service should be activated manually. Execute the following command at the root
                                          level to activate the CDR onDemand service: /usr/local/cm/bin/soapservicecontrol2.shCDRonDemandServiceCDRonDemanddeploy8443 . |
| Cisco CAR Web Service | You can activate the Cisco CAR Web Service only on the first
                                          					 server, and it requires that the Cisco CAR Scheduler service is activated and
                                          					 running on the same server and that the CDR Repository Manager service also is
                                          					 running on the same server. |
| Database and Admin Services |
| Cisco AXL Web Service | Following installation,
                                          					 Cisco AXL Web Service is enabled by default on all cluster nodes. Cisco
                                          					 recommends that you always leave the service activated on the publisher node.
                                          					 This ensures that you are able to configure products that are dependent on AXL,
                                          					 such as Unified Provisioning Manager. Based on your needs, you
                                          					 can activate or deactivate the service on specific subscriber nodes in Cisco
                                          					 Unified Serviceability under Feature Services. |
| Cisco Bulk Provisioning Service | You can activate the Cisco Bulk Provisioning Service only on the
                                          					 first node. If you use the Bulk Administration
                                             						Tool (BAT) to administer phones and users, you must activate this
                                          					 service. |
| Cisco UXL
                                          					 Web Service | This
                                          					 service performs authentication and user authorization checks. The TabSync
                                          					 client in Cisco IP Phone Address Book Synchronizer uses the Cisco UXL Web
                                          					 Service for queries to the Cisco Unified Communications Manager database. If you
                                          					 plan to use the Cisco IP Phone Address Book Synchronizer, you must activate
                                          					 this service on one node, preferably publisher. If you are not using Cisco IP
                                          					 Phone Address Book Synchronizer, then Cisco recommends that you deactivate this
                                          					 service . By default, this service is deactivated. |
| Cisco
                                          					 Platform Administrative Web Service | You must
                                          					 activate this service if you plan to use a Cisco Prime Collaboration Deployment
                                          					 (PCD) server to manage upgrades, switch version, restart or readdress
                                          					 operations. Platform Administrative Web Service (PAWS) allows SOAP
                                          					 communication between the Call Manager and Prime Collaboration Deployment
                                          					 (PCD). If you have more than one node in the cluster, you must activate this
                                          					 service on each server in the cluster. |
| Cisco TAPS Service | Before you can use the Cisco Unified Communications Manager Auto-Register Phone Tool , you must activate this service on the first node. When you create dummy MAC addresses for the Cisco Unified Communications Manager Auto-Register Phone Tool , ensure that the Cisco Bulk Provisioning Service is activated on the same node. |
| Performance and Monitoring Services |
| Cisco Serviceability Reporter | Activate on only the first node. Note The
                                                      						service only generates reports on the first node even if you activate the
                                                      						service on other nodes. | Note | The
                                                      						service only generates reports on the first node even if you activate the
                                                      						service on other nodes. |
| Note | The
                                                      						service only generates reports on the first node even if you activate the
                                                      						service on other nodes. |
| Cisco CallManager SNMP Service | If you use SNMP, activate this service on all servers in the
                                          					 cluster. |
| Security Services |
| Cisco CTL Provider | Activate on all servers in the cluster. |
| Cisco Certificate Authority Proxy Function (CAPF) | Activate on only the first node. |
| Directory Services |
| Cisco DirSync | Activate only on the first node. |

| Tip | Before you activate this service, verify that the Unified Communications Manager server displays in the Unified Communications
                                                      Manager Find/List window in Cisco Unified Communications Manager Administration . If the server does not display, add the Unified Communications Manager server before you activate this service. For information on how to
                                                      						add a server, see the System Configuration Guide for Cisco Unified Communications
                                                         						  Manager . |
|---|---|

| Note | Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                                      is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                                      want to administer headsets using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                                      activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it. |
|---|---|

| Note | The
                                                      						service only generates reports on the first node even if you activate the
                                                      						service on other nodes. |
|---|---|

| Caution | Before you turn on any services for a feature, you must complete all the required configuration on IM and Presence for that feature. See the relevant documentation for each IM and Presence feature. |
|---|---|

| Service/Servlet | Recommendations |
|---|---|
| Database and Admin Services |
| Cisco AXL Web Service | Following installation, Cisco AXL Web Service is enabled by default on all cluster nodes. Cisco recommends that you always
                                          leave the service activated on the IM and Presence Service database publisher node. This ensures that you are able to configure products that are dependent on AXL. If intercluster
                                          communication is configured, this service must be enabled on both nodes  in the sub-cluster where remote peers are configured
                                          to sync from. If this service is not enabled on both nodes presence and IM capabilities will be lost  in failover scenarios. Based on your needs, you can activate or deactivate the service on specific IM and Presence subscriber nodes in Cisco Unified Serviceability under Feature Services. |
| Cisco Bulk Provisioning Service | You turn on the Cisco Bulk Provisioning Service only on the first node. If you use the Bulk Administration Tool (BAT) to administer users, you must turn on this service. |
| Performance and Monitoring Services |
| Cisco Serviceability Reporter | Turn on this service on the publisher node only. Note The service only generates reports on the publisher node even if you turn on the service on other nodes. | Note | The service only generates reports on the publisher node even if you turn on the service on other nodes. |
| Note | The service only generates reports on the publisher node even if you turn on the service on other nodes. |
| IM and Presence Services |
| Cisco SIP Proxy | Turn on this service on all nodes in the cluster. |
| Cisco Presence Engine | Turn on this service on all nodes in the cluster. |
| Cisco Sync Agent | Turn on this service on all nodes in the cluster. |
| Cisco XCP Text Conference Manager | Turn on this service if you deploy the chat feature on IM and Presence . Turn on this service on each node that runs the chat feature. Note The permanent chat feature requires an external database. If you enable the permanent chat feature, you must also configure
                                                      an external database before starting the Text Conference Manager service. The Text Conference Manager service will not start
                                                      if the permanent chat feature is enabled and an external database is not configured. See the Database Setup Guide for IM and Presence on Unified Communications Manager . | Note | The permanent chat feature requires an external database. If you enable the permanent chat feature, you must also configure
                                                      an external database before starting the Text Conference Manager service. The Text Conference Manager service will not start
                                                      if the permanent chat feature is enabled and an external database is not configured. See the Database Setup Guide for IM and Presence on Unified Communications Manager . |
| Note | The permanent chat feature requires an external database. If you enable the permanent chat feature, you must also configure
                                                      an external database before starting the Text Conference Manager service. The Text Conference Manager service will not start
                                                      if the permanent chat feature is enabled and an external database is not configured. See the Database Setup Guide for IM and Presence on Unified Communications Manager . |
| Cisco XCP Web Connection Manager | Turn on this service if you integrate web clients with IM and Presence . Turn on this service on all nodes in the cluster. |
| Cisco XCP Connection Manager | Turn on this service if you integrate XMPP clients with IM and Presence . Turn on this service on all nodes in the cluster. |
| Cisco XCP SIP Federation Connection Manager | Turn on this service if you deploy any of the following configurations: Interdomain federation over the SIP protocol on IM and Presence . Turn on this service on each node that runs SIP federation. Intercluster deployment between a IM and Presence Release 9.x cluster and a Cisco Unified Presence Release 8.6(x) cluster. Turn on this service on all nodes in the Release 9.x cluster. |
| Cisco XCP XMPP Federation Connection Manager | Turn on this service only if you deploy interdomain federation over the XMPP protocol on IM and Presence . Turn on this service on each node that runs XMPP federation. Note Before you turn on the XMPP Federation Connection Manager service on a node, you must turn on XMPP Federation in Cisco Unified
                                                      Communications Manager IM and Presence Administration on that node. See Interdomain Federation for IM and Presence on Unified Communications Manager . | Note | Before you turn on the XMPP Federation Connection Manager service on a node, you must turn on XMPP Federation in Cisco Unified
                                                      Communications Manager IM and Presence Administration on that node. See Interdomain Federation for IM and Presence on Unified Communications Manager . |
| Note | Before you turn on the XMPP Federation Connection Manager service on a node, you must turn on XMPP Federation in Cisco Unified
                                                      Communications Manager IM and Presence Administration on that node. See Interdomain Federation for IM and Presence on Unified Communications Manager . |
| Cisco XCP Message Archiver | Turn on this service if you deploy the Compliance feature on IM and Presence . Turn on this service on any node that runs the IM Compliance feature. Note If you turn on the Message Archiver before you configure an external database, the service will not start. Also, if the external
                                                      database is not reachable, the service will not start. See the Database Setup Guide for IM and Presence on Unified Communications Manager . | Note | If you turn on the Message Archiver before you configure an external database, the service will not start. Also, if the external
                                                      database is not reachable, the service will not start. See the Database Setup Guide for IM and Presence on Unified Communications Manager . |
| Note | If you turn on the Message Archiver before you configure an external database, the service will not start. Also, if the external
                                                      database is not reachable, the service will not start. See the Database Setup Guide for IM and Presence on Unified Communications Manager . |
| Cisco XCP Directory Service | Turn on this service if you integrate XMPP clients on IM and Presence with an LDAP directory. Turn on this service on all nodes in the cluster. Note If you turn on the Directory Service before you configure the LDAP contact search settings for third-party XMPP clients, the
                                                      service will start, and then stop again. See Configuration and Administration of IM and Presence Service on Unified Communications Manager . | Note | If you turn on the Directory Service before you configure the LDAP contact search settings for third-party XMPP clients, the
                                                      service will start, and then stop again. See Configuration and Administration of IM and Presence Service on Unified Communications Manager . |
| Note | If you turn on the Directory Service before you configure the LDAP contact search settings for third-party XMPP clients, the
                                                      service will start, and then stop again. See Configuration and Administration of IM and Presence Service on Unified Communications Manager . |
| Cisco XCP Authentication Service | Turn on this service if you integrate XMPP clients with IM and Presence . Turn on this service on all nodes in the cluster. |

| Note | The service only generates reports on the publisher node even if you turn on the service on other nodes. |
|---|---|

| Note | The permanent chat feature requires an external database. If you enable the permanent chat feature, you must also configure
                                                      an external database before starting the Text Conference Manager service. The Text Conference Manager service will not start
                                                      if the permanent chat feature is enabled and an external database is not configured. See the Database Setup Guide for IM and Presence on Unified Communications Manager . |
|---|---|

| Note | Before you turn on the XMPP Federation Connection Manager service on a node, you must turn on XMPP Federation in Cisco Unified
                                                      Communications Manager IM and Presence Administration on that node. See Interdomain Federation for IM and Presence on Unified Communications Manager . |
|---|---|

| Note | If you turn on the Message Archiver before you configure an external database, the service will not start. Also, if the external
                                                      database is not reachable, the service will not start. See the Database Setup Guide for IM and Presence on Unified Communications Manager . |
|---|---|

| Note | If you turn on the Directory Service before you configure the LDAP contact search settings for third-party XMPP clients, the
                                                      service will start, and then stop again. See Configuration and Administration of IM and Presence Service on Unified Communications Manager . |
|---|---|

| Tip | Unified Communications Manager and IM and Presence Service only: Before you activate services in the Service Activation window, review topics related to cluster service activation
                                          recommendations. |
|---|---|

| Step 1 | Choose Tools > Service
                                             				  Activation . The Service
                                             				  Activation window displays. |
|---|---|
| Step 2 | Select the
                                       			 server (node) from the Server drop-down list, and then click Go . You can access Unified Communications Manager services from an IM and Presence Service node and vice versa. You may encounter the following error when trying to access a remote node: "Connection to the Server
                                          cannot be established (unable to connect to Remote Node)". If this error message appears, see the Administration Guide for Cisco Unified Communications Manager . |
| Step 3 | Perform one of
                                       			 the following actions to turn on or turn off services: To turn on
                                             				  the default services required to run on a single server, select Set
                                                					 to Default . Note This
                                                            						option selects default services based on the configuration of a single server,
                                                            						and checks for service dependencies. To turn on
                                             				  all services, check Check All Services . To turn on a
                                             				  specific service, check the check box for the service that you want to turn on To turn off
                                             				  a service, uncheck the check box for the services that you want to turn off. | Note | This
                                                            						option selects default services based on the configuration of a single server,
                                                            						and checks for service dependencies. |
| Note | This
                                                            						option selects default services based on the configuration of a single server,
                                                            						and checks for service dependencies. |
| Step 4 | Unified Communications Manager and IM and Presence Service only: For a cluster configuration, review the cluster service activation recommendations, and then check the check boxes
                                       next to the services that you want to activate. |
| Step 5 | After you check
                                       			 the check boxes for the services that you want to activate, click Save . Tip To deactivate
                                                      				  services that you activated, uncheck the check boxes next to the services that
                                                      				  you want to deactivate; then, click Save . Tip To obtain the
                                                      				  latest status of the services, click the Refresh button. | Tip | To deactivate
                                                      				  services that you activated, uncheck the check boxes next to the services that
                                                      				  you want to deactivate; then, click Save . | Tip | To obtain the
                                                      				  latest status of the services, click the Refresh button. |
| Tip | To deactivate
                                                      				  services that you activated, uncheck the check boxes next to the services that
                                                      				  you want to deactivate; then, click Save . |
| Tip | To obtain the
                                                      				  latest status of the services, click the Refresh button. |

| Note | This
                                                            						option selects default services based on the configuration of a single server,
                                                            						and checks for service dependencies. |
|---|---|

| Tip | To deactivate
                                                      				  services that you activated, uncheck the check boxes next to the services that
                                                      				  you want to deactivate; then, click Save . |
|---|---|

| Tip | To obtain the
                                                      				  latest status of the services, click the Refresh button. |
|---|---|

| Tip | Use the Related Links list box and the Go button to navigate to Control Center and Service Activation windows. |
|---|---|

| Caution | Unified Communications Manager only: Stopping a service also stops call processing for all devices that the service controls.
                                             When a service is stopped, calls from an IP phone to another IP phone remain connected; calls in progress from an IP phone
                                             to a Media Gateway Control Protocol (MGCP) gateway also remain connected, but other types of calls get dropped. |
|---|---|

| Step 1 | Depending on the service type that you want to
                                          			 start/stop/restart/refresh, perform one of the following tasks: Choose Tools > Control
                                                         						Center - Feature Services . Tip Before you can start, stop, or restart a feature service, it must
                                                               						be activated. Choose Tools > Control
                                                         						Center - Network Services . | Tip | Before you can start, stop, or restart a feature service, it must
                                                               						be activated. |
|---|---|---|---|
| Tip | Before you can start, stop, or restart a feature service, it must
                                                               						be activated. |
| Step 2 | Choose the server from the Server drop-down list, and then click Go . The window displays the following items: The service names for the server that you chose. The service group. The service status, for example, Started, Running, Not
                                                   				  Running, and so on. (Status column). The exact time that the service started running. (Start Time
                                                   				  column). The amount of time that the service has been running. (Up Time
                                                   				  column). |
| Step 3 | Perform one of the following tasks: Click the radio button next to the service that you want to
                                                   				  start,  and then click Start .
                                                   				The Status changes to reflect the updated status. Click the radio button next to the service that you want to
                                                   				  stop,  and then click Stop .
                                                   				 The Status changes to reflect the updated status. Click the radio button next to the service that you want to
                                                   				  restart,  and then click Restart . A message indicates that restarting may take a while. Click OK . Click Refresh to get the latest status of the services. To go to the Service Activation window or to the other Control
                                                   				  Center window, choose an option from the Related Links drop-down list, and
                                                   				  then click Go . |

| Tip | Before you can start, stop, or restart a feature service, it must
                                                               						be activated. |
|---|---|

| Tip | You must start and stop most services from Control Center in the serviceability GUI. |
|---|---|