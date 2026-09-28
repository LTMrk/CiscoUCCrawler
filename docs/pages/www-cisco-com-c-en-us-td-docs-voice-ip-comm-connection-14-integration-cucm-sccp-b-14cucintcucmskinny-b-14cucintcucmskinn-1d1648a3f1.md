---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-integration-cucm-sccp-b-14cucintcucmskinny-b-14cucintcucmskinn-1d1648a3f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/cucm_sccp/b_14cucintcucmskinny/b_14cucintcucmskinny_chapter_0111.html
retrieved_at: 2026-08-16T18:36:26.518440+00:00
---

Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 14

# Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 14

Updated: November 25, 2020

Chapter: Adding Cisco Unified Communications Manager Express to a Cisco Unified
	 Communications Manager Integration

## Chapter: Adding Cisco Unified Communications Manager Express to a Cisco Unified
	 Communications Manager Integration

# Adding Cisco Unified Communications Manager Express to a Cisco Unified
                     	 Communications Manager Integration

## Adding Cisco Unified Communications Manager Express to a Cisco Unified
                        	 Communications Manager Integration

### Overview

Cisco Unity Connection can integrate a Cisco Unified CM phone
                              		system having port group of Cisco Unified CM Express server and Cisco
                              		Unified CM servers. This configuration is typically used to ensure call
                              		processing functionality at a branch office when the WAN link is down.

There are the following considerations:

The version of Cisco Unified CM Express and the version of the
                                    			 Unity Connection must be a supported combination in the Compatibility Matrix
                                    			 for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html .

The Cisco Unified CM phone system integration is created before
                                    			 adding the Cisco Unified CM Express server.

#### Adding Cisco Unified CM Express Server to Cisco Unified CM Phone
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
                                             			 Unified Communications Manager, click Add .

Step 5

In the new row, enter the following settings

Settings for the Cisco Unified CM Express
                                                				Server

Field

Setting

Order

Enter a number that is higher than
                                                            							 the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                            							 server, the higher numbers are the secondary servers.

IPv4 Address or Host Name

Enter the IP address (or host
                                                            							 name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                            							 Unified CM port group.

IPv6 Address or Host Name

Do not enter any value in this
                                                            							 filed as IPv6 is not supported for Cisco Unified CM Express phone system
                                                            							 integrations.

Port

Enter the TCP port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting.

TLS Port

Enter the TLS port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting.

Server Type

Select Cisco Unified Communications
                                                               								Manager Express .

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

On the Port Group Basics page, in the
                                             			 Related Links drop-down list, select Test Port Group and
                                             			 select Go to confirm the Cisco
                                             			 Unified CM Express port group settings.

Step 11

When prompted that the test terminate call
                                             			 in progress, select OK .

If the test is not successful, the Task
                                                				Execution Results displays one or more messages with troubleshooting steps.
                                                				After correcting the problems, test the Unity Connection again.

Step 12

In the Task Execution Results window, select Close and sign out of
                                             			 Cisco Unity Connection Administration.

#### Use of Cisco Unified Survivable Remote Site Telephony (SRST) Router

When a Cisco Unified Survivable Remote Site Telephony (SRST) router is a part of the network and the Cisco Unified SRST router
                                 takes over call processing functions from Cisco Unified CM (for example, because the WAN link is down), phones at a branch
                                 office can continue to function. In this situation, however, the integration features have the following limitations:

Call forward to busy greeting —When the Cisco Unified SRST router uses FXO/FXS connections to the PSTN and a call is forwarded from a branch office to Cisco Unity
                                       Connection, the busy greeting cannot play.

Call forward to internal greeting —When the Cisco Unified SRST router uses FXO/FXS connections to the PSTN and a call is forwarded from a branch office to Cisco Unity
                                       Connection, the internal greeting cannot play. Because the PSTN provides the calling number of the FXO line, the caller is
                                       not identified as a user.

Call transfers —Because an access code is needed to reach the PSTN, call transfers from Unity Connection to a branch office fails.

Identified user messaging —When the Cisco Unified SRST router uses FXO/FXS connections to the PSTN and a user at a branch office leaves a message or
                                       forwards a call, the user is not identified. The caller appears as an unidentified caller.

Message waiting indication —MWIs are not updated on branch office phones, so MWIs do not correctly reflect when new messages arrive or when all messages
                                       have been listened to. We recommend resynchronizing MWIs after the WAN link is reestablished.

Routing rules —When the Cisco Unified SRST router uses FXO/FXS connections to the PSTN and a call arrives from a branch office to Cisco Unity
                                       Connection (either a direct or forwarded call), routing rules fail.

When the Cisco Unified SRST router uses PRI/BRI connections, the caller ID for calls from a branch office to Unity Connection
                                 may be the full number (exchange plus extension) provided by the PSTN and therefore may not match the extension of the Unity
                                 Connection user. If this is the case, you can let Unity Connection recognize the caller ID with alternate extensions.

Redirected Dialed Number Information Service (RDNIS) needs to be supported when using SRST.

For information on setting up Cisco Unified SRST routers, see the “Integrating Voice Mail with Cisco Unified SRST” chapter
                                 of the applicable Cisco Unified SRST System Administrator Guide at http://www.cisco.com/en/US/products/sw/voicesw/ps2169/products_installation_and_configuration_guides_list.html .

#### Impact of Non-Delivery of RDNIS on Voice Mail Calls Routed via AAR

RDNIS needs to be supported when using Automated Alternate Routing (AAR).

AAR can route calls over the PSTN when the WAN is oversubscribed. However, when calls are rerouted over the PSTN, RDNIS can
                                 be affected. Incorrect RDNIS information can affect voice mail calls that are rerouted over the PSTN by AAR when Cisco Unity
                                 Connection is remote from its messaging clients. If the RDNIS information is not correct, the call do not reach the voice
                                 mail box of the dialed user, instead receive the automated attendant prompt, and the caller might be asked to reenter the
                                 extension number of the party they wish to reach. This behavior is primarily an issue when the telephone carrier is unable
                                 to ensure RDNIS across the network. There are numerous reasons why the carrier might not be able to ensure that RDNIS is properly
                                 sent. Check with your carrier to determine whether it provides guaranteed RDNIS delivery end-to-end for your circuits. The
                                 alternative to using AAR for oversubscribed WANs is simply to let callers hear reorder tone in an oversubscribed condition.

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Telephony Integrations ,
                                             			 then select Port Group . |
|---|---|
| Step 2 | On the Search Port Groups page, select the
                                             			 name of the port group for the Cisco Unified CM servers. |
| Step 3 | On the Port Group Basics page, on the Edit
                                             			 menu, select Servers . |
| Step 4 | On the Edit Servers page, under Cisco
                                             			 Unified Communications Manager, click Add . |
| Step 5 | In the new row, enter the following settings Settings for the Cisco Unified CM Express
                                                				Server Field Setting Order Enter a number that is higher than
                                                            							 the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                            							 server, the higher numbers are the secondary servers. IPv4 Address or Host Name Enter the IP address (or host
                                                            							 name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                            							 Unified CM port group. IPv6 Address or Host Name Do not enter any value in this
                                                            							 filed as IPv6 is not supported for Cisco Unified CM Express phone system
                                                            							 integrations. Port Enter the TCP port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting. TLS Port Enter the TLS port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting. Server Type Select Cisco Unified Communications
                                                               								Manager Express . | Field | Setting | Order | Enter a number that is higher than
                                                            							 the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                            							 server, the higher numbers are the secondary servers. | IPv4 Address or Host Name | Enter the IP address (or host
                                                            							 name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                            							 Unified CM port group. | IPv6 Address or Host Name | Do not enter any value in this
                                                            							 filed as IPv6 is not supported for Cisco Unified CM Express phone system
                                                            							 integrations. | Port | Enter the TCP port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting. | TLS Port | Enter the TLS port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting. | Server Type | Select Cisco Unified Communications
                                                               								Manager Express . |
| Field | Setting |
| Order | Enter a number that is higher than
                                                            							 the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                            							 server, the higher numbers are the secondary servers. |
| IPv4 Address or Host Name | Enter the IP address (or host
                                                            							 name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                            							 Unified CM port group. |
| IPv6 Address or Host Name | Do not enter any value in this
                                                            							 filed as IPv6 is not supported for Cisco Unified CM Express phone system
                                                            							 integrations. |
| Port | Enter the TCP port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting. |
| TLS Port | Enter the TLS port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting. |
| Server Type | Select Cisco Unified Communications
                                                               								Manager Express . |
| Step 6 | Select Save . |
| Step 7 | On the Edit menu, select Advanced Settings . |
| Step 8 | On the Edit Advanced Settings page, in the
                                             			 Delay After Answer field, enter 1000 and select Save . |
| Step 9 | On the Edit menu, select Port Group Basics . |
| Step 10 | On the Port Group Basics page, in the
                                             			 Related Links drop-down list, select Test Port Group and
                                             			 select Go to confirm the Cisco
                                             			 Unified CM Express port group settings. |
| Step 11 | When prompted that the test terminate call
                                             			 in progress, select OK . If the test is not successful, the Task
                                                				Execution Results displays one or more messages with troubleshooting steps.
                                                				After correcting the problems, test the Unity Connection again. |
| Step 12 | In the Task Execution Results window, select Close and sign out of
                                             			 Cisco Unity Connection Administration. |

| Field | Setting |
|---|---|
| Order | Enter a number that is higher than
                                                            							 the Cisco Unified CM servers. The lowest number is the primary Cisco Unified CM
                                                            							 server, the higher numbers are the secondary servers. |
| IPv4 Address or Host Name | Enter the IP address (or host
                                                            							 name) of the Cisco Unified CM Express server that you are adding to the Cisco
                                                            							 Unified CM port group. |
| IPv6 Address or Host Name | Do not enter any value in this
                                                            							 filed as IPv6 is not supported for Cisco Unified CM Express phone system
                                                            							 integrations. |
| Port | Enter the TCP port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting. |
| TLS Port | Enter the TLS port of the Cisco
                                                            							 Unified CM Express server that you are adding to the Cisco Unified CM port
                                                            							 group. We recommend that you use the default setting. |
| Server Type | Select Cisco Unified Communications
                                                               								Manager Express . |