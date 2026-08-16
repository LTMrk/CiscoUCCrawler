---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-12-5-1-cup0-b-rcc-lync-server-integration--9e34fdfc38
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/12_5_1/cup0_b_rcc-lync-server-integration-1251/cup0_b_rcc-lync-server-integration-1251_chapter_00.html
retrieved_at: 2026-08-16T17:28:34.513477+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

Updated: January 23, 2019

Chapter: Introduction

## Chapter: Introduction

# Introduction

This chapter
                        		describes the configuration steps to integrate the IM and Presence Service with Microsoft Lync
                        		Server for Remote Call Control.

## About Microsoft Lync
                        	 Server

Microsoft Lync Server is designed for use in small and medium organization
                              		  deployments. The server acts as both a SIP registrar and SIP proxy in a single
                              		  system. The server functionality provides voice capabilities for Remote Call
                              		  Control to gateways such as the IM and Presence
                                 			 Service and Cisco Unified Communications
                                 			 Manager platforms.

Microsoft Lync Server 2010 Standard Edition installs the Microsoft SQL Server 2008
                                 			 Express database on the same server to provide data storage for users
                              		  and configuration system data. Microsoft Lync Server 2010 Enterprise Edition installs the Microsoft SQL Server 2008
                                 			 Express database on a different server. Commands that are entered
                              		  from the Lync Server Management Shell are loaded into the SQL database.

IM and Presence
                                             			 Service supports integration with Microsoft Lync Server Standard Edition or Enterprise Edition 2010 and 2013.

### Get More
                           	 Information

#### IM and
                                    			 Presence Service

For
                                 		  additional IM and Presence
                                    			 Service documentation, see the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

#### Cisco
                                    			 Unified Communications Manager

For Cisco Unified Communications
                                    			 Manager documentation, see the following URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

#### Microsoft
                                 		  Lync

For Microsoft Lync documentation, see the following URLs:

http://technet.microsoft.com/en-us/library/gg558664.aspx

http://office.microsoft.com/en-us/lync/

#### Microsoft Active
                                 		  Directory

For
                                 		  information about Microsoft Windows Server Active Directory, seethe following
                                 		  URL: http://technet2.microsoft.com/windowsserver/en/technologies/featured/ad/default.mspx

## About Remote Call
                        	 Control

Microsoft
                              		  Remote Call Control (RCC) allows enterprise users to control their Cisco Unified IP
                                 			 Phone or Cisco IP
                                 			 Communicator Phone through Microsoft Lync, a third-party desktop
                              		  instant-messaging (IM) application. When a user signs in to the Microsoft Lync
                              		  client, the Lync server sends instructions, through the IM and Presence
                                 			 Service node, to the Cisco Unified Communications
                                 			 Manager to set up, tear down and maintain calling features based on a
                              		  user's action at the Lync client.

SIP federation and Remote Call Control (RCC) do not work together on
                                          			 the same IM and Presence Service cluster. This is because for SIP federation a
                                          			 user cannot be licensed for both Cisco IM and Presence Service and Microsoft
                                          			 Lync/OCS, but for RCC a user must be licensed for Cisco IM and Presence Service
                                          			 and Microsoft Lync/OCS at the same time.

An IM and Presence Service cluster that is used for RCC does not support Jabber or other IM and Presence Service functionality.

## Integration
                        	 Overview

IM and Presence
                                 			 Service allows enterprise users to control their Cisco Unified IP
                                 			 Phone or Cisco IP Communicator Phone through Microsoft Lync , a
                              		  third-party desktop IM application.

Microsoft Lync sends session-initiating requests to the Computer Telephony Interface (CTI)
                              		  Gateway on IM and Presence
                                 			 Service to control Cisco Unified IP
                                 			 Phone s or Cisco IP Communicator Phones that are registered in Cisco Unified Communications
                                 			 Manager , as illustrated in the following figure. The CTI Gateway
                              		  forwards the requests to the CTI Manager on Cisco Unified Communications
                                 			 Manager . The Cisco Unified Communications
                                 			 Manager returns the events to the Microsoft Lync application using the same path in the opposite direction.

### Microsoft Lync sends requests to IM and Presence
                                 			 Service

Microsoft Lync sends session-initiating requests to IM and Presence
                                 			 Service . These requests are routed to the CTI connection addresses
                              		  that are configured on IM and Presence
                                 			 Service .

IM and
                                             				Presence Service supports CTI connections with up to eight Cisco Unified Communications
                                             				Manager nodes.

The
                              		  requests are distributed to the CTI connection addresses in a round-robin
                              		  sequence, for example the first request is routed to first CTI node, second
                              		  request to next CTI node, and so on. In a dual-node IM and Presence
                                 			 Service cluster, a load balancer can be used to distribute (in a
                              		  round-robin manner) the session-initiating requests that are sent from Microsoft Lync clients to the publisher and subscriber IM and Presence
                                 			 Service nodes.

### CTI Gateway
                              		  Monitors CTI Connection Addresses for Microsoft Lync User Sign-In

When the
                              		  CTI Gateway on IM and Presence
                                 			 Service starts, it connects to all CTI connection addresses in the
                              		  configured list, and monitors these connections by sending periodic heartbeat
                              		  messages. When a Microsoft Lync user
                              		  signs in, Microsoft Lync server sends a SIP INVITE request with a CSTA body to the CTI Gateway to
                              		  monitor the Cisco Unified IP
                                 			 Phone or Cisco IP Communicator Phone for the user. The CTI Gateway
                              		  creates a session for that Microsoft Lync user, and uses the load-balancing mechanism to send session-initiating requests
                              		  from that user to any of the CTI connection addresses.

### CSTA Application
                              		  Session Is Established

After the
                              		  CSTA application session is established, Microsoft Lync and
                              		  CTI Gateway exchange a sequence of SIP INFO messages for activities such as
                              		  monitoring devices, making calls, transferring calls, or changing the status of
                              		  controlling devices. This message exchange is sent over the same CTI connection
                              		  address with which the initial session was established.

If
                              		  connection to any of the CTI Managers fails, outbound call requests from Microsoft Lync are
                              		  returned until the connection comes back into service. If a Cisco Unified Communications
                                 			 Manager node is down, the CTI Gateway will make periodic attempts to
                              		  reestablish a connection to it. When the Cisco Unified Communications
                                 			 Manager node comes back in service, the CTI Gateway will reconnect to
                              		  it and monitor the connection. In this case, when Microsoft Lync sends an (in-session) SIP INFO request, the CTI Gateway will have a different
                              		  CTI Manager connection ID because of a new connection. Microsoft Lync sends a new SIP INVITE message, but the Microsoft Lync user
                              		  is not required to sign in again.

## Line
                        	 Appearances

When a user
                              		  selects a phone to use with the remote call control feature, on IM and Presence
                                 			 Service the user is selecting a line appearance to control through
                              		  the Microsoft Lync client. A line appearance is the association of a line with a device. On Cisco Unified Communications
                                 			 Manager , the administrator can associate a device with multiple
                              		  lines, and a line with multiple devices. Typically it is the role of the Cisco Unified Communications
                                 			 Manager administrator to configure line appearances by specifying the
                              		  lines and devices that are associated with each other.

See the Microsoft Office Communicator Call Control with
                                 			 Microsoft OCS for IM and Presence Service on Cisco Unified
                                 			 Communications Manager for information on the configuration steps to
                              		  integrate IM and Presence
                                 			 Service with Microsoft OCS for Microsoft Office Communicator Call
                              		  Control.

| Note | IM and Presence
                                             			 Service supports integration with Microsoft Lync Server Standard Edition or Enterprise Edition 2010 and 2013. |
|---|---|

| Note | SIP federation and Remote Call Control (RCC) do not work together on
                                          			 the same IM and Presence Service cluster. This is because for SIP federation a
                                          			 user cannot be licensed for both Cisco IM and Presence Service and Microsoft
                                          			 Lync/OCS, but for RCC a user must be licensed for Cisco IM and Presence Service
                                          			 and Microsoft Lync/OCS at the same time. |
|---|---|

| Note | An IM and Presence Service cluster that is used for RCC does not support Jabber or other IM and Presence Service functionality. |
|---|---|

| Note | IM and
                                             				Presence Service supports CTI connections with up to eight Cisco Unified Communications
                                             				Manager nodes. |
|---|---|