---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-12-5-1-cup0-b-rcc-lync-server-integration--d91ddd9858
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/12_5_1/cup0_b_rcc-lync-server-integration-1251/cup0_b_rcc-lync-server-integration-1251_chapter_011.html
retrieved_at: 2026-08-16T17:28:47.264727+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

Updated: January 23, 2019

Chapter: IM and Presence Service Node Setup

## Chapter: IM and Presence Service Node Setup

# IM and Presence Service Node Setup

## Set Up Service
                        	 Parameters

The SIP
                              		  message routing from IM and Presence Service to Microsoft Lync is
                              		  based on the Record-Route header added by Microsoft Lync in
                              		  the initial request. IM and Presence Service resolves the hostname in the
                              		  Record-Route header to an IP address and routes the SIP messages to the Microsoft Lync client.

In
                              		  addition the transport type on IM and Presence Service should be the same as the
                              		  transport type configured on Microsoft Lync for
                              		  the IM and Presence Service route.

Select Cisco Unified CM IM and
                                             				  Presence Administration > System > Service
                                             				  Parameters .

Select the IM and
                                          				Presence server.

Select the
                                       			 service Cisco
                                          				SIP Proxy .

Verify that the
                                       			 following parameters are configured correctly:

The proxy
                                             				  domain must define the enterprise top-level domain (for example,
                                             				  "example.com"). This value can be entered in the CUCM Domain service parameter field.

This
                                                					 parameter specifies which URIs are treated as local and handled by this IM and Presence
                                                   						Service installation. Other SIP requests may be proxied.

Enable the Add
                                                					 Record-Route Header parameter.

Enable the Use
                                                					 Transport in Record-Route Header parameter.

The SIP
                                                					 Route Header Transport Type parameter value must be set to the same
                                             				  type as the transport parameter configured on Microsoft Lync for
                                             				  the Microsoft Lync to IM and Presence
                                                					 Service route.

Select Save .

### What to do next

Set Up Incoming and Outgoing Access Control Lists

## Set Up Incoming and Outgoing Access Control Lists

This procedure involves adding four access control list (ACL) entries:

- The FQDN of the Lync server for the incoming ACL

- The IP address of the Lync server for the incoming ACL

- The FQDN of the Lync server for the outgoing ACL

- The IP Address of the Lync server for the outgoing ACL

Select Cisco Unified CM IM and Presence Administration > System > Security > Incoming ACL > Add New .

Enter a description of the incoming ACL, for example, Lync Standard Server.

Enter the FQDN of the Lync server in the Address Pattern field and select Save .

To view the new Incoming ACL entry, select Go from the top right of the window. A list of all configured Incoming ACLs is displayed.

Select Add New .

Enter a description of the incoming ACL, for example, Lync Standard Server.

Enter the IP address of the Lync server in the Address Pattern field and select Save .

Select Cisco Unified CM IM and Presence Administration > System > Security > Outgoing ACL > Add New .

Enter a description of the outgoing ACL, for example, Lync Standard Server.

Enter the FQDN of the Lync server in the Address Pattern field and select Save .

To view the new Outgoing ACL entry, select Go from the top right of the window. A list of all configured Outgoing ACLs is displayed.

Select Add New .

Enter a description of the outgoing ACL, for example, Lync Standard Server.

Enter the IP address of the Lync server in the Address Pattern field and select Save .

### What to do next

Set Up Routing Settings

## Set Up Routing
                        	 Settings

Complete
                              		  the following procedure to configure the routing settings.

Select Cisco Unified CM IM and
                                             				  Presence Administration > Presence > Routing > Settings .

Select On for Method/Event Routing Status .

Select Default
                                          				Cisco SIP Proxy TCP Listener for the Preferred Proxy Server.

Select Save.

### What to do next

Remote Call Control Setup

## Remote Call Control Setup

### Set Up IM and
                           	 Presence Service CTI Connection

Complete
                                 		  the following procedure to configure the CTI connections on IM and Presence Service .

#### Before you begin

Obtain the
                                 		  username and password that you configured for the application user account on
                                 		  the associated Cisco Unified Communications
                                    			 Manager server for the CTI Gateway.

Select Cisco Unified CM IM and
                                                				  Presence Administration > Application > Microsoft
                                                				  RCC > Settings .

Select On from the Application Status menu.

Enter the CTI
                                          			 Gateway application username and password.

The username
                                                         				  and password are case-sensitive and must match what is configured on Cisco Unified Communications
                                                            					 Manager .

Enter a value
                                          			 (in seconds) for the heartbeat interval.

This is the
                                             				length of time between heartbeat messages sent from IM and Presence Service to the Cisco Unified Communications
                                                				  Manager nodes to monitor the CTI connections.

Enter a value
                                          			 (in seconds) for the session timer.

This is the
                                             				session timer for the Microsoft Lync sign-in session.

Select the type
                                          			 of Microsoft server you are using from the Microsoft Server Type menu.

For Microsoft Lync integration, you must select MOC
                                                            					 server OCS .

As required,
                                          			 enter the IP address of each Cisco Unified Communications
                                             				Manager node with which you want to establish a CTI connection.

You can
                                                         				  configure a CTI connection with up to eight Cisco Unified Communications
                                                            					 Manager nodes. These nodes must all belong to the same Cisco Unified Communications
                                                            					 Manager cluster.

Select Save .

If you select
                                                         				  MOC server OCS as the Microsoft Server Type, you must install the IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in on the Microsoft Lync client for any users who use more than one line appearance for remote call
                                                         				  control. The IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in adds a menu item to the Microsoft Lync client that enables the user to select a line appearance to control.

#### What to do next

Assign User Capabilities

### Assign User Capabilities

Complete the following procedure to assign Microsoft Remote Call Control (RCC) capabilities to users.

Select Cisco Unified CM IM and Presence Administration > Application > Microsoft RCC > User Assignment .

Select Find .

Check the users to whom you want to assign remote call control capabilities.

Select Assign Selected Users .

Check Enable Microsoft RCC in the Microsoft RCC Assignment window.

Select Save .

Make sure that you have assigned remote call control capabilities to each Microsoft Lync user.

#### What to do next

Run Microsoft RCC Troubleshooter

### Run Microsoft RCC
                           	 Troubleshooter

The
                                 		  Microsoft RCC Troubleshooter validates the configuration that supports the
                                 		  integration of the Microsoft Lync client with IM and Presence Service .

Select Cisco Unified CM IM and
                                                				  Presence Administration > Diagnostics > Microsoft RCC
                                                				  Troubleshooter .

Enter a valid
                                          			 user ID.

Select Search
                                                         				  to find the ID for a user.

Enter the Microsoft Lync server address.

Select Submit .

#### What to do next

Microsoft Component Integration Setup for IM and Presence Service

| Step 1 | Select Cisco Unified CM IM and
                                             				  Presence Administration > System > Service
                                             				  Parameters . |
|---|---|
| Step 2 | Select the IM and
                                          				Presence server. |
| Step 3 | Select the
                                       			 service Cisco
                                          				SIP Proxy . |
| Step 4 | Verify that the
                                       			 following parameters are configured correctly: The proxy
                                             				  domain must define the enterprise top-level domain (for example,
                                             				  "example.com"). This value can be entered in the CUCM Domain service parameter field. This
                                                					 parameter specifies which URIs are treated as local and handled by this IM and Presence
                                                   						Service installation. Other SIP requests may be proxied. Enable the Add
                                                					 Record-Route Header parameter. Enable the Use
                                                					 Transport in Record-Route Header parameter. The SIP
                                                					 Route Header Transport Type parameter value must be set to the same
                                             				  type as the transport parameter configured on Microsoft Lync for
                                             				  the Microsoft Lync to IM and Presence
                                                					 Service route. |
| Step 5 | Select Save . |

| Step 1 | Select Cisco Unified CM IM and Presence Administration > System > Security > Incoming ACL > Add New . |
|---|---|
| Step 2 | Enter a description of the incoming ACL, for example, Lync Standard Server. |
| Step 3 | Enter the FQDN of the Lync server in the Address Pattern field and select Save . Tip To view the new Incoming ACL entry, select Go from the top right of the window. A list of all configured Incoming ACLs is displayed. | Tip | To view the new Incoming ACL entry, select Go from the top right of the window. A list of all configured Incoming ACLs is displayed. |
| Tip | To view the new Incoming ACL entry, select Go from the top right of the window. A list of all configured Incoming ACLs is displayed. |
| Step 4 | Select Add New . |
| Step 5 | Enter a description of the incoming ACL, for example, Lync Standard Server. |
| Step 6 | Enter the IP address of the Lync server in the Address Pattern field and select Save . |
| Step 7 | Select Cisco Unified CM IM and Presence Administration > System > Security > Outgoing ACL > Add New . |
| Step 8 | Enter a description of the outgoing ACL, for example, Lync Standard Server. |
| Step 9 | Enter the FQDN of the Lync server in the Address Pattern field and select Save . Tip To view the new Outgoing ACL entry, select Go from the top right of the window. A list of all configured Outgoing ACLs is displayed. | Tip | To view the new Outgoing ACL entry, select Go from the top right of the window. A list of all configured Outgoing ACLs is displayed. |
| Tip | To view the new Outgoing ACL entry, select Go from the top right of the window. A list of all configured Outgoing ACLs is displayed. |
| Step 10 | Select Add New . |
| Step 11 | Enter a description of the outgoing ACL, for example, Lync Standard Server. |
| Step 12 | Enter the IP address of the Lync server in the Address Pattern field and select Save . |

| Tip | To view the new Incoming ACL entry, select Go from the top right of the window. A list of all configured Incoming ACLs is displayed. |
|---|---|

| Tip | To view the new Outgoing ACL entry, select Go from the top right of the window. A list of all configured Outgoing ACLs is displayed. |
|---|---|

| Step 1 | Select Cisco Unified CM IM and
                                             				  Presence Administration > Presence > Routing > Settings . |
|---|---|
| Step 2 | Select On for Method/Event Routing Status . |
| Step 3 | Select Default
                                          				Cisco SIP Proxy TCP Listener for the Preferred Proxy Server. |
| Step 4 | Select Save. |

| Step 1 | Select Cisco Unified CM IM and
                                                				  Presence Administration > Application > Microsoft
                                                				  RCC > Settings . |
|---|---|
| Step 2 | Select On from the Application Status menu. |
| Step 3 | Enter the CTI
                                          			 Gateway application username and password. Tip The username
                                                         				  and password are case-sensitive and must match what is configured on Cisco Unified Communications
                                                            					 Manager . | Tip | The username
                                                         				  and password are case-sensitive and must match what is configured on Cisco Unified Communications
                                                            					 Manager . |
| Tip | The username
                                                         				  and password are case-sensitive and must match what is configured on Cisco Unified Communications
                                                            					 Manager . |
| Step 4 | Enter a value
                                          			 (in seconds) for the heartbeat interval. This is the
                                             				length of time between heartbeat messages sent from IM and Presence Service to the Cisco Unified Communications
                                                				  Manager nodes to monitor the CTI connections. |
| Step 5 | Enter a value
                                          			 (in seconds) for the session timer. This is the
                                             				session timer for the Microsoft Lync sign-in session. |
| Step 6 | Select the type
                                          			 of Microsoft server you are using from the Microsoft Server Type menu. Note For Microsoft Lync integration, you must select MOC
                                                            					 server OCS . | Note | For Microsoft Lync integration, you must select MOC
                                                            					 server OCS . |
| Note | For Microsoft Lync integration, you must select MOC
                                                            					 server OCS . |
| Step 7 | As required,
                                          			 enter the IP address of each Cisco Unified Communications
                                             				Manager node with which you want to establish a CTI connection. Note You can
                                                         				  configure a CTI connection with up to eight Cisco Unified Communications
                                                            					 Manager nodes. These nodes must all belong to the same Cisco Unified Communications
                                                            					 Manager cluster. | Note | You can
                                                         				  configure a CTI connection with up to eight Cisco Unified Communications
                                                            					 Manager nodes. These nodes must all belong to the same Cisco Unified Communications
                                                            					 Manager cluster. |
| Note | You can
                                                         				  configure a CTI connection with up to eight Cisco Unified Communications
                                                            					 Manager nodes. These nodes must all belong to the same Cisco Unified Communications
                                                            					 Manager cluster. |
| Step 8 | Select Save . Important If you select
                                                         				  MOC server OCS as the Microsoft Server Type, you must install the IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in on the Microsoft Lync client for any users who use more than one line appearance for remote call
                                                         				  control. The IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in adds a menu item to the Microsoft Lync client that enables the user to select a line appearance to control. | Important | If you select
                                                         				  MOC server OCS as the Microsoft Server Type, you must install the IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in on the Microsoft Lync client for any users who use more than one line appearance for remote call
                                                         				  control. The IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in adds a menu item to the Microsoft Lync client that enables the user to select a line appearance to control. |
| Important | If you select
                                                         				  MOC server OCS as the Microsoft Server Type, you must install the IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in on the Microsoft Lync client for any users who use more than one line appearance for remote call
                                                         				  control. The IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in adds a menu item to the Microsoft Lync client that enables the user to select a line appearance to control. |

| Tip | The username
                                                         				  and password are case-sensitive and must match what is configured on Cisco Unified Communications
                                                            					 Manager . |
|---|---|

| Note | For Microsoft Lync integration, you must select MOC
                                                            					 server OCS . |
|---|---|

| Note | You can
                                                         				  configure a CTI connection with up to eight Cisco Unified Communications
                                                            					 Manager nodes. These nodes must all belong to the same Cisco Unified Communications
                                                            					 Manager cluster. |
|---|---|

| Important | If you select
                                                         				  MOC server OCS as the Microsoft Server Type, you must install the IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in on the Microsoft Lync client for any users who use more than one line appearance for remote call
                                                         				  control. The IM and Presence Service Lync
                                                         				  Remote Call Control Plug-in adds a menu item to the Microsoft Lync client that enables the user to select a line appearance to control. |
|---|---|

| Step 1 | Select Cisco Unified CM IM and Presence Administration > Application > Microsoft RCC > User Assignment . |
|---|---|
| Step 2 | Select Find . |
| Step 3 | Check the users to whom you want to assign remote call control capabilities. |
| Step 4 | Select Assign Selected Users . |
| Step 5 | Check Enable Microsoft RCC in the Microsoft RCC Assignment window. |
| Step 6 | Select Save . Important Make sure that you have assigned remote call control capabilities to each Microsoft Lync user. | Important | Make sure that you have assigned remote call control capabilities to each Microsoft Lync user. |
| Important | Make sure that you have assigned remote call control capabilities to each Microsoft Lync user. |

| Important | Make sure that you have assigned remote call control capabilities to each Microsoft Lync user. |
|---|---|

| Step 1 | Select Cisco Unified CM IM and
                                                				  Presence Administration > Diagnostics > Microsoft RCC
                                                				  Troubleshooter . |
|---|---|
| Step 2 | Enter a valid
                                          			 user ID. Tip Select Search
                                                         				  to find the ID for a user. | Tip | Select Search
                                                         				  to find the ID for a user. |
| Tip | Select Search
                                                         				  to find the ID for a user. |
| Step 3 | Enter the Microsoft Lync server address. |
| Step 4 | Select Submit . |

| Tip | Select Search
                                                         				  to find the ID for a user. |
|---|---|