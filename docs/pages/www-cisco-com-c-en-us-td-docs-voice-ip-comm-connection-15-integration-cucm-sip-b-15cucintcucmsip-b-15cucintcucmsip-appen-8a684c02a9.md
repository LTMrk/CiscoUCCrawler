---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-integration-cucm-sip-b-15cucintcucmsip-b-15cucintcucmsip-appen-8a684c02a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/cucm_sip/b_15cucintcucmsip/b_15cucintcucmsip_appendix_0100.html
retrieved_at: 2026-08-17T03:34:23.715237+00:00
---

Cisco Unified Communications Manager SIP Integration Guide for Cisco Unity Connection Release 15

# Cisco Unified Communications Manager SIP Integration Guide for Cisco Unity Connection Release 15

Updated: October 1, 2024

Chapter: Adding Cisco
	 Unified Communications Manager Express to a Cisco Unified Communications
	 Manager Integration

## Chapter: Adding Cisco
	 Unified Communications Manager Express to a Cisco Unified Communications
	 Manager Integration

# Adding Cisco
                     	 Unified Communications Manager Express to a Cisco Unified Communications
                     	 Manager Integration

Cisco Unity Connection can integrate a Cisco Unified
                        		Communications Manager phone system integration that has a port group of Cisco
                        		Unified CM servers and a Cisco Unified Communications Manager Express server.
                        		This configuration is typically used to ensure call processing functionality at
                        		a branch office when the WAN link is down.

There are, however, the following considerations:

The version of Cisco Unified CM Express and the version of the
                              			 Cisco Unity Connection must be a supported combination in the Compatibility
                              			 Matrix for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html .

The Cisco Unified CM phone system integration is typically
                              			 already created before adding the Cisco Unified CM Express server.

## Adding Cisco
                        	 Unified Communications Manager Express to a Cisco Unified Communications
                        	 Manager Integration

Cisco Unity Connection can integrate a Cisco Unified
                           		Communications Manager phone system integration that has a port group of Cisco
                           		Unified CM servers and a Cisco Unified Communications Manager Express server.
                           		This configuration is typically used to ensure call processing functionality at
                           		a branch office when the WAN link is down.

There are, however, the following considerations:

The version of Cisco Unified CM Express and the version of the
                                 			 Cisco Unity Connection must be a supported combination in the Compatibility
                                 			 Matrix for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html .

The Cisco Unified CM phone system integration is typically
                                 			 already created before adding the Cisco Unified CM Express server.

### Adding a Cisco Unified CM Express Server to a Cisco Unified CM Phone
                           	 System Integration

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations ,
                                          			 then select Port Group .

Step 2

On the Search Port Groups page, select the
                                          			 name of the port group for the Cisco Unified CM servers.

Step 3

On the Port Group Basics page, on the Edit
                                          			 menu, select Servers .

Step 4

On the Edit Servers page, under Cisco
                                          			 Unified Communications Manager, select Add .

Step 5

In the new row, enter the following
                                          			 settings.

Field

Setting

Order

Enter a number that is higher than
                                                         						  the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                         						  server, the higher numbers are the secondary servers.

IPv4 Address or Host Name )

Enter the IPv4 address (or host
                                                         						  name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group.

IPv6 Address or Host Name )

Do not use this field for Cisco
                                                         						  Unified CM Express integrations. IPv6 is not supported between Cisco Unity
                                                         						  Connection and Cisco Unified CM Express.

IP Address or Host Name)

Enter the IP address (or host name)
                                                         						  of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group.

Port

Enter the TCP port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting.

TLS Port

Enter the TLS port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting.

Step 6

Select Save .

Step 7

On the Edit menu, select Advanced Settings .

Step 8

On the Edit Advanced Settings page, in the
                                          			 Delay After Answer field, enter 1000 and select Save .

Step 9

On the Edit menu, select Port Group Basics .

Step 10

On the Port Group Basics page, select Reset .

Step 11

When prompted that resetting terminates all
                                          			 call traffic, select OK .

Step 12

In the Related Links drop-down list, select Test Port Group and
                                          			 select Go to confirm the Cisco
                                          			 Unified CM Express port group settings.

Step 13

When prompted that the test terminates call
                                          			 in progress, select OK .

If the test is not successful, the Task
                                             				Execution Results displays one or more messages with troubleshooting steps.
                                             				After correcting the problems, test the connection again.

Step 14

In the Task Execution Results window, select Close .

Step 15

Sign out of Cisco Unity Connection
                                          			 Administration.

### Use of Cisco
                           	 Unified Survivable Remote Site Telephony (SRST) Router

When a Cisco Unified Survivable Remote Site Telephony (SRST)
                              		router is part of the network and the Cisco Unified SRST router takes over call
                              		processing functions from Cisco Unified CM (for example, because the WAN link
                              		is down), phones at a branch office can continue to function. In this
                              		situation, however, the integration features have the following limitations:

Call forward to busy greeting —When the Cisco Unified SRST
                                    			 router uses FXO/FXS connections to the PSTN and a call is forwarded from a
                                    			 branch office to Cisco Unity Connection, the busy greeting cannot play.

Call forward to internal greeting —When the Cisco Unified
                                    			 SRST router uses FXO/FXS connections to the PSTN and a call is forwarded from a
                                    			 branch office to Cisco Unity Connection, the internal greeting cannot play.
                                    			 Because the PSTN provides the calling number of the FXO line, the caller is not
                                    			 identified as a user.

Call transfers —Because an access code is needed to reach the
                                    			 PSTN, call transfers from Unity Connection to a branch office fails.

Identified user messaging —When the Cisco Unified SRST router
                                    			 uses FXO/FXS connections to the PSTN and a user at a branch office leaves a
                                    			 message or forwards a call, the user is not identified. The caller appears as
                                    			 an unidentified caller.

Message waiting indication —MWIs are not updated on branch
                                    			 office phones, so MWIs do not correctly reflect when new messages arrive or
                                    			 when all messages have been listened to. We recommend resynchronizing MWIs
                                    			 after the WAN link is reestablished.

Routing rules —When the Cisco Unified SRST router uses
                                    			 FXO/FXS connections to the PSTN and a call arrives from a branch office to
                                    			 Unity Connection (either a direct or forwarded call), routing rules fail.

When the Cisco Unified SRST router uses PRI/BRI connections, the
                              		caller ID for calls from a branch office to Unity Connection may be the full
                              		number (exchange plus extension) provided by the PSTN and therefore may not
                              		match the extension of the Unity Connection user. If this is the case, you can
                              		let Unity Connection recognize the caller ID using alternate extensions.

Redirected Dialed Number Information Service (RDNIS) needs to be
                              		supported when using SRST.

For information on setting up Cisco Unified SRST routers, see
                              		the “Integrating Voice Mail with Cisco Unified SRST” chapter of the applicable Cisco Unified SRST System Administrator Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-survivable-remote-site-telephony/products-installation-and-configuration-guides-list.html .

### Impact of Non-Delivery of RDNIS on Voice Mail Calls Routed via AAR

RDNIS needs to be supported when using Automated Alternate Routing (AAR).

AAR can route calls over the PSTN when the WAN is oversubscribed. However, when calls are rerouted over the PSTN, RDNIS can
                                    be affected. Incorrect RDNIS information can affect voicemail calls that are rerouted over the PSTN by AAR when Cisco Unity
                                    Connection is remote from its messaging clients. If the RDNIS information is not correct, the call does not reach the voicemail
                                    box of the dialed user but instead receives the automated attendant prompt, and the caller might be asked to reenter the extension
                                    number of the party they wish to reach. This behavior is primarily an issue when the telephone carrier is unable to ensure
                                    RDNIS across the network. There are numerous reasons why the carrier might not be able to ensure that RDNIS is properly sent.
                                    Check with your carrier to determine whether it provides guaranteed RDNIS delivery end-to-end for your circuits. The alternative
                                    to using AAR for oversubscribed WANs is simply to let callers hear reorder tone in an oversubscribed condition.

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations ,
                                          			 then select Port Group . |
|---|---|
| Step 2 | On the Search Port Groups page, select the
                                          			 name of the port group for the Cisco Unified CM servers. |
| Step 3 | On the Port Group Basics page, on the Edit
                                          			 menu, select Servers . |
| Step 4 | On the Edit Servers page, under Cisco
                                          			 Unified Communications Manager, select Add . |
| Step 5 | In the new row, enter the following
                                          			 settings. Table 1. Settings for the Cisco Unified CM
                                                   				Express Server Field Setting Order Enter a number that is higher than
                                                         						  the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                         						  server, the higher numbers are the secondary servers. IPv4 Address or Host Name ) Enter the IPv4 address (or host
                                                         						  name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group. IPv6 Address or Host Name ) Do not use this field for Cisco
                                                         						  Unified CM Express integrations. IPv6 is not supported between Cisco Unity
                                                         						  Connection and Cisco Unified CM Express. IP Address or Host Name) Enter the IP address (or host name)
                                                         						  of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group. Port Enter the TCP port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting. TLS Port Enter the TLS port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting. | Field | Setting | Order | Enter a number that is higher than
                                                         						  the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                         						  server, the higher numbers are the secondary servers. | IPv4 Address or Host Name ) | Enter the IPv4 address (or host
                                                         						  name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group. | IPv6 Address or Host Name ) | Do not use this field for Cisco
                                                         						  Unified CM Express integrations. IPv6 is not supported between Cisco Unity
                                                         						  Connection and Cisco Unified CM Express. | IP Address or Host Name) | Enter the IP address (or host name)
                                                         						  of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group. | Port | Enter the TCP port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting. | TLS Port | Enter the TLS port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting. |
| Field | Setting |
| Order | Enter a number that is higher than
                                                         						  the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                         						  server, the higher numbers are the secondary servers. |
| IPv4 Address or Host Name ) | Enter the IPv4 address (or host
                                                         						  name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group. |
| IPv6 Address or Host Name ) | Do not use this field for Cisco
                                                         						  Unified CM Express integrations. IPv6 is not supported between Cisco Unity
                                                         						  Connection and Cisco Unified CM Express. |
| IP Address or Host Name) | Enter the IP address (or host name)
                                                         						  of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group. |
| Port | Enter the TCP port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting. |
| TLS Port | Enter the TLS port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting. |
| Step 6 | Select Save . |
| Step 7 | On the Edit menu, select Advanced Settings . |
| Step 8 | On the Edit Advanced Settings page, in the
                                          			 Delay After Answer field, enter 1000 and select Save . |
| Step 9 | On the Edit menu, select Port Group Basics . |
| Step 10 | On the Port Group Basics page, select Reset . |
| Step 11 | When prompted that resetting terminates all
                                          			 call traffic, select OK . |
| Step 12 | In the Related Links drop-down list, select Test Port Group and
                                          			 select Go to confirm the Cisco
                                          			 Unified CM Express port group settings. |
| Step 13 | When prompted that the test terminates call
                                          			 in progress, select OK . If the test is not successful, the Task
                                             				Execution Results displays one or more messages with troubleshooting steps.
                                             				After correcting the problems, test the connection again. |
| Step 14 | In the Task Execution Results window, select Close . |
| Step 15 | Sign out of Cisco Unity Connection
                                          			 Administration. |

| Field | Setting |
|---|---|
| Order | Enter a number that is higher than
                                                         						  the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                         						  server, the higher numbers are the secondary servers. |
| IPv4 Address or Host Name ) | Enter the IPv4 address (or host
                                                         						  name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group. |
| IPv6 Address or Host Name ) | Do not use this field for Cisco
                                                         						  Unified CM Express integrations. IPv6 is not supported between Cisco Unity
                                                         						  Connection and Cisco Unified CM Express. |
| IP Address or Host Name) | Enter the IP address (or host name)
                                                         						  of the Cisco Unified CM Express server that you are adding to the Cisco
                                                         						  Unified CM port group. |
| Port | Enter the TCP port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting. |
| TLS Port | Enter the TLS port of the Cisco
                                                         						  Unified CM Express server that you are adding to the Cisco Unified CM port
                                                         						  group. We recommend that you use the default setting. |