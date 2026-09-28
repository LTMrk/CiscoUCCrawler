---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-12-5-1-cup0-b-rcc-lync-server-integration--890617e4c1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/12_5_1/cup0_b_rcc-lync-server-integration-1251/cup0_b_rcc-lync-server-integration-1251_chapter_01.html
retrieved_at: 2026-08-16T17:28:38.700906+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

Updated: January 23, 2019

Chapter: Integration Requirements

## Chapter: Integration Requirements

# Integration Requirements

Call forward setting on IP phone: Call forward
                                       settings made on the Cisco IP phone, using the soft key button or
                                       the Cisco UCM phone configuration page are not reflected
                                       in the Microsoft Lync Client,  however call forward settings made on
                                       Micorsoft Lync are reflected on the Cisco IP phone.

The Microsoft Lync Client can override any call
                                       forward setting configured on the IP Phone.  The IP Phone can
                                       override any call forward setting configured on the Microsoft Lync
                                       Client.

## Software
                        	 Requirements

The
                              		  following software is required for integrating IM and Presence Service with Microsoft Lync Server :

IM and Presence Service , current release

IM and Presence Service Lync Remote Call
                                    				Control Plug-in

Cisco Unified Communications Manager , current release

Microsoft Lync Server 2010 or 2013 Release 4.x, Standard
                                    				Edition or Enterprise Edition

Lync Server
                                          					 Control Panel

Lync Server
                                          					 Deployment Wizard

Lync Server
                                          					 Logging Tool

Lync Server
                                          					 Management Shell

Lync Server
                                          					 Topology Builder

Microsoft 2010 Lync Client, or, Microsoft 2013
                                    				Lync Client

(Optional) Upgraded Skype for Business 2015 Client

The Skype for Business 2015 client must have been upgraded from a Lync 2013 client and must be registered to a  Lync 2013
                                                server.

(Optional) Cisco CSS 11500 Content
                                       				  Services Switch

Microsoft Domain
                                    				Controller

Microsoft Active
                                    				Directory

DNS

Certificate
                                    				Authority

## Preconfiguration
                        	 Checklist

An IM and Presence Service node that is set up
                                       				and configured as described in Configuration and Administration of IM and Presence Service on
                                          				  Cisco Unified Communications Manager . The IM and Presence Service node must be
                                       				correctly deployed with a Cisco Unified Communications Manager (Unified
                                       				Communications Manager) server as described in Configuration and Administration of IM and Presence Service on
                                          				  Cisco Unified Communications Manager .

A Microsoft Lync Server that is set up and configured according to the requirements
                                       				defined in the Microsoft documentation.

A Microsoft Lync Client or an upgraded Skype for Business 2015 Client that is set up according to the requirements defined
                                       				in the Microsoft documentation.

If you are using Skype for Business clients, the client must have been upgraded from a Lync 2013 client, and must be registered
                                                   to a  Lync 2013 server.

Verify that all
                                       				services are running on Microsoft Lync Server.

Verify that you
                                       				updated all SRV records in DNS in support of Microsoft Lync Server as instructed in the Microsoft Lync Server installation instructions.

Verify that the
                                       				computer on which the Microsoft Lync client is installed can resolve the FQDN of the Microsoft Lync server. You can do this by executing the NSLOOKUP command from the Microsoft Lync client computer.

Verify that the IM and Presence Service node, Cisco Unified Communications
                                          				  Manager node and Microsoft Lync server are added to DNS and that each of these servers is resolving to its
                                       				FQDN. You can do this by executing the NSLOOKUP command from another resource
                                       				in each of their domains.

If you are using
                                       				LDAP synchronization between AD and Cisco Unified Communications
                                          				  Manager server, verify that connections are synchronizing properly.

## Integration License
                        	 Requirements

### What To Do
                              		  Next

You must assign IM and Presence Service to each Microsoft
                              		  Lync Remote Call Control (RCC) user. IM and Presence Service capabilities are
                              		  included within both User Connect Licensing (UCL) and Cisco Unified Workspace
                              		  Licensing (CUWL). See the Cisco Unified
                                 			 Communications Manager Enterprise License Manager User Guide for more
                              		  information.

You can assign IM and Presence Service to a user in the End User
                                 			 Configuration window in Cisco Unified Communications Manager. See
                              		  the Cisco Unified
                                 			 Communications Manager Administration Guide for more information.

Cisco Unified Communications Manager Server Setup

| Note | Call forward setting on IP phone: Call forward
                                       settings made on the Cisco IP phone, using the soft key button or
                                       the Cisco UCM phone configuration page are not reflected
                                       in the Microsoft Lync Client,  however call forward settings made on
                                       Micorsoft Lync are reflected on the Cisco IP phone. The Microsoft Lync Client can override any call
                                       forward setting configured on the IP Phone.  The IP Phone can
                                       override any call forward setting configured on the Microsoft Lync
                                       Client. |
|---|---|

| Note | The Skype for Business 2015 client must have been upgraded from a Lync 2013 client and must be registered to a  Lync 2013
                                                server. |
|---|---|

| Note | If you are using Skype for Business clients, the client must have been upgraded from a Lync 2013 client, and must be registered
                                                   to a  Lync 2013 server. |
|---|---|