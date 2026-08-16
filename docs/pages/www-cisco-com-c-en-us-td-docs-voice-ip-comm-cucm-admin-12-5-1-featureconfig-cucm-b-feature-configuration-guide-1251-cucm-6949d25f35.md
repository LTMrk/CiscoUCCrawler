---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-featureconfig-cucm-b-feature-configuration-guide-1251-cucm-6949d25f35
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/featureConfig/cucm_b_feature-configuration-guide-1251/cucm_b_feature-configuration-guide-1251_chapter_0100011.html
retrieved_at: 2026-08-16T16:55:40.490133+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 13, 2025

Chapter: External Call Transfer Restrictions

## Chapter: External Call Transfer Restrictions

# External Call Transfer Restrictions

## External Call
                        	 Transfer Restrictions Overview

External
                              		  Call Transfer Restrictions is a feature that you can use to configure gateways,
                              		  trunks, and route patterns as OnNet (internal) or OffNet (external) devices at
                              		  the system level. By setting the devices as OffNet, you can restrict the
                              		  transferring of an external call to an external device and thus help prevent
                              		  toll fraud.

If you try to transfer a call on an OffNet gateway or trunk when the
                              		  service parameter Block OffNet to OffNet Transfer is set to True, a message
                              		  displays on the user phone to indicate that the call cannot be transferred.

This chapter uses
                              		  the following terms:

OnNet
                                          						Device

A device
                                          						that is configured as OnNet and considered to be internal to the network.

OffNet
                                          						Device

A device
                                          						that is considered as OffNet and, when routed, is considered to be external to
                                          						the network.

Network
                                          						Location

The
                                          						location of the device, which is considered as OnNet or OffNet, with respect to
                                          						the network.

Originating End

The
                                          						device that gets transferred. The system considers this device as OnNet or
                                          						OffNet.

Terminating End

The
                                          						device that receives the transferred call. The system considers this device as
                                          						OnNet or OffNet.

Incoming
                                          						Call

A call
                                          						for which only gateways and trunks call classification settings get used to
                                          						classify it as OnNet or OffNet. Route Pattern call classification settings do
                                          						not apply.

Outgoing
                                          						Call

A call
                                          						for which the call classification setting of the trunk, gateway, and route
                                          						pattern gets considered. The Allow Device Override setting on the route pattern
                                          						determines whether the trunk or gateway call classification setting gets used
                                          						instead of the route pattern call classification setting.

## Configure External
                        	 Call Transfer Restrictions Task Flow

Step 1

Configure the Service Parameter for Call Transfer Restrictions

Step 2

To configure
                                       			 incoming calls perform the following procedures:

- Configure the Clusterwide Service Parameter

- Configure Gateways for Call Transfer Restrictions

- Configure Trunks for Call Transfer Restrictions

Step 3

Configure Outgoing Calls

### Configure the
                           	 Service Parameter for Call Transfer Restrictions

To block external
                                 		  calls from being transferred to another external device or number:

Step 1

From the Cisco
                                          			 Unified CM Administration user interface choose System > Service
                                                				  Parameters .

Step 2

On the Service Parameter Configuration window choose the Cisco Unified CM server you want to configure from the Server drop-down
                                          list.

Step 3

Choose Cisco CallManager (Active) from the Service drop-down list.

Step 4

Choose True from the Block OffNet to OffNet Transfer drop-down list. The default value specifies False.

Step 5

Click Save .

### Configure Incoming
                           	 Calls Task Flow

Step 1

(Optional) Configure the Clusterwide Service Parameter

Configure all
                                             				gateways or trunks in the Cisco Unified Communications Manager cluster to be
                                             				OffNet (external) or OnNet (internal).

Step 2

Configure Gateways for Call Transfer Restrictions

Configure
                                             				gateways as OnNet (internal) or OffNet (external) by using Gateway
                                             				Configuration. When the feature is used in conjunction with the clusterwide
                                             				service parameter Block OffNet to OffNet Transfer, the configuration determines
                                             				whether calls can transfer over a gateway.

You can
                                             				configure the following devices as internal and external to Cisco Unified
                                             				Communications Manager:

H.323
                                                   					 gateway

MGCP FXO
                                                   					 trunk

MGCP T1/E1
                                                   					 trunk

Step 3

Configure Trunks for Call Transfer Restrictions

Configure
                                             				trunks as OnNet (internal) or OffNet (external) by using Trunk Configuration.
                                             				When the feature is used in conjunction with the clusterwide service parameter
                                             				Block OffNet to OffNet Transfer, the configuration determines whether calls can
                                             				transfer over a trunk.

You can
                                             				configure the following devices as internal and external to Cisco Unified
                                             				Communications Manager:

Intercluster trunk

SIP trunk

#### Configure the
                              	 Clusterwide Service Parameter

To
                                    		  configure all gateways or trunks in the Cisco Unified
                                       			 Communications Manager cluster to be OffNet (external) or OnNet
                                    		  (internal), perform the following steps:

##### Before you begin

Step 1

From the Cisco
                                             			 Unified CM Administration user interface choose System > Service
                                                   				  Parameters .

Step 2

On the Service Parameter Configuration window choose the Cisco Unified CM server you want to configure from the Server drop-down
                                             list.

Step 3

Choose Cisco CallManager (Active) from the Service drop-down list.

Step 4

Choose either OffNet or OnNet (the default specifies OffNet) from the Call Classification drop-down list.

#### Configure Gateways
                              	 for Call Transfer Restrictions

To
                                    		  configure the gateway as OffNet, OnNet, or Use System Default, perform the
                                    		  following procedure. The system considers calls that come to the network
                                    		  through that gateway as OffNet or OnNet, respectively.

##### Before you begin

Step 1

From Cisco Unified CM Administration, choose Device > Gateway .

The Find and List Gateways window displays.

Step 2

To list the
                                             			 configured gateways, click Find .

The gateways that are configured in Unified Communications Manager display.

Step 3

Choose the
                                             			 gateway that you want to configure as OffNet or OnNet.

Step 4

In the Call
                                             			 Classification field choose OffNet or OnNet. If you have enabled clusterwide
                                             			 restrictions an all gateways, configure each gateway to Use System Default
                                             			 (this reads the setting in the Call Classification service parameter and uses
                                             			 that setting for the gateway).

Step 5

Click Save .

#### Configure Trunks
                              	 for Call Transfer Restrictions

To
                                    		  configure the trunk as OffNet, OnNet, or Use System Default, perform the
                                    		  following procedure. The system considers calls that come to the network
                                    		  through that trunk as OffNet or OnNet, respectively.

##### Before you begin

Step 1

From Cisco Unified CM Administration, choose Device > Trunk.

The Find and List Trunk window displays.

Step 2

To list the
                                             			 configured trunks, click Find.

The trunks that are configured in Unified Communications Manager display.

Step 3

Choose the
                                             			 trunk that you want to configure as OffNet or OnNet.

Step 4

From the Call
                                             			 Classification drop-down list, choose one of the following fields:

OffNet - When you choose this field, this identifies the
                                                   				  gateway as an external gateway. When a call comes in from a gateway that is
                                                   				  configured as OffNet, the system sends the outside ring to the destination
                                                   				  device.

OnNet - When you choose this field, this identifies the
                                                   				  gateway as an internal gateway. When a call comes in from a gateway that is
                                                   				  configured as OnNet, the system sends the inside ring to the destination
                                                   				  device.

Use System Default - When you choose this field, this uses the Unified Communications Manager clusterwide service parameter Call Classification.

If you have
                                                            				  enabled clusterwide restrictions an all trunks, configure each trunk to Use
                                                            				  System Default (this reads the setting in the Call Classification service
                                                            				  parameter and uses that setting for the trunk)

Step 5

Click Save.

### Configure Outgoing
                           	 Calls

To
                                 		  classify a call as OnNet or OffNet, administrators can set the Call
                                    			 Classification field to OnNet or OffNet, respectively, on the Route
                                    			 Pattern Configuration window. Administrators can override the route
                                 		  pattern setting and use the trunk or gateway setting by checking the Allow
                                    			 Device Override check box on the Route
                                    			 Pattern Configuration window.

#### Before you begin

Step 1

From Cisco
                                          			 Unified CM Administration, choose Call Routing > Route/Hunt > Route
                                                				  Pattern and click Find to list all route patterns.

Step 2

Choose the
                                          			 route pattern you want to configure, or click Add
                                             				New .

Step 3

In the Route
                                             				Pattern Configuration window, use the following fields to configure
                                          			 transfer capabilities with route pattern configuration:

Call
                                                   					 Classification —Use this drop-down list to classify the call that
                                                				  uses this route Pattern as OffNet or OnNet.

Provide Outside Dial
                                                   					 Tone —If Call Classification is set to OffNet, this check box gets
                                                				  checked.

Allow Device
                                                   					 Override —When this check box is checked, the system uses the Call
                                                				  Classification setting of the trunk or gateway that is associated with the
                                                				  route pattern instead of the Call Classification setting on the Route Pattern
                                                				  Configuration window.

Step 4

Click Save .

## External Call
                        	 Transfer Restrictions Interactions

Feature

Interaction

Drop
                                          						Conference

The Drop
                                          						Conference feature determines whether an existing ad hoc conference should be
                                          						dropped by checking whether the conference parties are configured as OffNet or
                                          						OnNet. You use the service parameter Drop Ad Hoc Conference and choose the
                                          						option When No OnNet Parties Remain in the Conference to configure the feature.
                                          						You determine OnNet status for each party by checking the device or route
                                          						pattern that the party is using. For more information, see topics related to Ad
                                          						Hoc Conference linking in the “Ad Hoc Conferencing” chapter.

Bulk
                                          						Administration

Bulk
                                          						Administration inserts gateway configuration (OffNet or OnNet) on the Gateway
                                          						Template. For more information, see the Cisco Unified Communications Manager Bulk Administration
                                                							 Guide .

Dialed Number Analyzer (DNA)

When
                                          						used to perform digit analysis on a gateway, DNA displays the Call
                                          						Classification that is configured for the gateway and the route pattern. For
                                          						more information, see the Cisco Unified
                                                							 Communications Manager Dialed Number Analyzer Guide .

## External Call Transfer Restrictions Restrictions

Restriction

Description

FXS Gateways

FXS gateways such as Cisco Catalyst 6000 24 Port do not have
                                          						a Call Classification field on the Gateway Configuration window; therefore, the
                                          						system always considers them as OnNet.

Cisco VG248 Gateway

The system does not support the Cisco VG248 Gateway which does not have a Call Classification field.

FXS Ports

Cisco Unified
                                             						  Communications Manager considers all Cisco Unified IP
                                             						  Phone s and FXS ports as OnNet (internal) that cannot be configured as
                                          						OffNet (external).

| Term | Description |
|---|---|
| OnNet
                                          						Device | A device
                                          						that is configured as OnNet and considered to be internal to the network. |
| OffNet
                                          						Device | A device
                                          						that is considered as OffNet and, when routed, is considered to be external to
                                          						the network. |
| Network
                                          						Location | The
                                          						location of the device, which is considered as OnNet or OffNet, with respect to
                                          						the network. |
| Originating End | The
                                          						device that gets transferred. The system considers this device as OnNet or
                                          						OffNet. |
| Terminating End | The
                                          						device that receives the transferred call. The system considers this device as
                                          						OnNet or OffNet. |
| Incoming
                                          						Call | A call
                                          						for which only gateways and trunks call classification settings get used to
                                          						classify it as OnNet or OffNet. Route Pattern call classification settings do
                                          						not apply. |
| Outgoing
                                          						Call | A call
                                          						for which the call classification setting of the trunk, gateway, and route
                                          						pattern gets considered. The Allow Device Override setting on the route pattern
                                          						determines whether the trunk or gateway call classification setting gets used
                                          						instead of the route pattern call classification setting. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure the Service Parameter for Call Transfer Restrictions | Block
                                       			 external calls from being transferred to another external device or number. |
| Step 2 | To configure
                                       			 incoming calls perform the following procedures: Configure the Clusterwide Service Parameter Configure Gateways for Call Transfer Restrictions Configure Trunks for Call Transfer Restrictions | Configure
                                       			 gateways and trunks as OnNet (internal) or OffNet (external) by using Gateway
                                       			 Configuration or Trunk Configuration or by setting a clusterwide service
                                       			 parameter. |
| Step 3 | Configure Outgoing Calls | Configure
                                       			 transfer capabilities with route pattern configuration. |

| Step 1 | From the Cisco
                                          			 Unified CM Administration user interface choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | On the Service Parameter Configuration window choose the Cisco Unified CM server you want to configure from the Server drop-down
                                          list. |
| Step 3 | Choose Cisco CallManager (Active) from the Service drop-down list. |
| Step 4 | Choose True from the Block OffNet to OffNet Transfer drop-down list. The default value specifies False. |
| Step 5 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | (Optional) Configure the Clusterwide Service Parameter | Configure all
                                             				gateways or trunks in the Cisco Unified Communications Manager cluster to be
                                             				OffNet (external) or OnNet (internal). |
| Step 2 | Configure Gateways for Call Transfer Restrictions | Configure
                                             				gateways as OnNet (internal) or OffNet (external) by using Gateway
                                             				Configuration. When the feature is used in conjunction with the clusterwide
                                             				service parameter Block OffNet to OffNet Transfer, the configuration determines
                                             				whether calls can transfer over a gateway. You can
                                             				configure the following devices as internal and external to Cisco Unified
                                             				Communications Manager: H.323
                                                   					 gateway MGCP FXO
                                                   					 trunk MGCP T1/E1
                                                   					 trunk |
| Step 3 | Configure Trunks for Call Transfer Restrictions | Configure
                                             				trunks as OnNet (internal) or OffNet (external) by using Trunk Configuration.
                                             				When the feature is used in conjunction with the clusterwide service parameter
                                             				Block OffNet to OffNet Transfer, the configuration determines whether calls can
                                             				transfer over a trunk. You can
                                             				configure the following devices as internal and external to Cisco Unified
                                             				Communications Manager: Intercluster trunk SIP trunk |

| Step 1 | From the Cisco
                                             			 Unified CM Administration user interface choose System > Service
                                                   				  Parameters . |
|---|---|
| Step 2 | On the Service Parameter Configuration window choose the Cisco Unified CM server you want to configure from the Server drop-down
                                             list. |
| Step 3 | Choose Cisco CallManager (Active) from the Service drop-down list. |
| Step 4 | Choose either OffNet or OnNet (the default specifies OffNet) from the Call Classification drop-down list. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Gateway . The Find and List Gateways window displays. |
|---|---|
| Step 2 | To list the
                                             			 configured gateways, click Find . The gateways that are configured in Unified Communications Manager display. |
| Step 3 | Choose the
                                             			 gateway that you want to configure as OffNet or OnNet. |
| Step 4 | In the Call
                                             			 Classification field choose OffNet or OnNet. If you have enabled clusterwide
                                             			 restrictions an all gateways, configure each gateway to Use System Default
                                             			 (this reads the setting in the Call Classification service parameter and uses
                                             			 that setting for the gateway). |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk. The Find and List Trunk window displays. |
|---|---|
| Step 2 | To list the
                                             			 configured trunks, click Find. The trunks that are configured in Unified Communications Manager display. |
| Step 3 | Choose the
                                             			 trunk that you want to configure as OffNet or OnNet. |
| Step 4 | From the Call
                                             			 Classification drop-down list, choose one of the following fields: OffNet - When you choose this field, this identifies the
                                                   				  gateway as an external gateway. When a call comes in from a gateway that is
                                                   				  configured as OffNet, the system sends the outside ring to the destination
                                                   				  device. OnNet - When you choose this field, this identifies the
                                                   				  gateway as an internal gateway. When a call comes in from a gateway that is
                                                   				  configured as OnNet, the system sends the inside ring to the destination
                                                   				  device. Use System Default - When you choose this field, this uses the Unified Communications Manager clusterwide service parameter Call Classification. Note If you have
                                                            				  enabled clusterwide restrictions an all trunks, configure each trunk to Use
                                                            				  System Default (this reads the setting in the Call Classification service
                                                            				  parameter and uses that setting for the trunk) | Note | If you have
                                                            				  enabled clusterwide restrictions an all trunks, configure each trunk to Use
                                                            				  System Default (this reads the setting in the Call Classification service
                                                            				  parameter and uses that setting for the trunk) |
| Note | If you have
                                                            				  enabled clusterwide restrictions an all trunks, configure each trunk to Use
                                                            				  System Default (this reads the setting in the Call Classification service
                                                            				  parameter and uses that setting for the trunk) |
| Step 5 | Click Save. |

| Note | If you have
                                                            				  enabled clusterwide restrictions an all trunks, configure each trunk to Use
                                                            				  System Default (this reads the setting in the Call Classification service
                                                            				  parameter and uses that setting for the trunk) |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Call Routing > Route/Hunt > Route
                                                				  Pattern and click Find to list all route patterns. |
|---|---|
| Step 2 | Choose the
                                          			 route pattern you want to configure, or click Add
                                             				New . |
| Step 3 | In the Route
                                             				Pattern Configuration window, use the following fields to configure
                                          			 transfer capabilities with route pattern configuration: Call
                                                   					 Classification —Use this drop-down list to classify the call that
                                                				  uses this route Pattern as OffNet or OnNet. Provide Outside Dial
                                                   					 Tone —If Call Classification is set to OffNet, this check box gets
                                                				  checked. Allow Device
                                                   					 Override —When this check box is checked, the system uses the Call
                                                				  Classification setting of the trunk or gateway that is associated with the
                                                				  route pattern instead of the Call Classification setting on the Route Pattern
                                                				  Configuration window. |
| Step 4 | Click Save . |

| Feature | Interaction |
|---|---|
| Drop
                                          						Conference | The Drop
                                          						Conference feature determines whether an existing ad hoc conference should be
                                          						dropped by checking whether the conference parties are configured as OffNet or
                                          						OnNet. You use the service parameter Drop Ad Hoc Conference and choose the
                                          						option When No OnNet Parties Remain in the Conference to configure the feature.
                                          						You determine OnNet status for each party by checking the device or route
                                          						pattern that the party is using. For more information, see topics related to Ad
                                          						Hoc Conference linking in the “Ad Hoc Conferencing” chapter. |
| Bulk
                                          						Administration | Bulk
                                          						Administration inserts gateway configuration (OffNet or OnNet) on the Gateway
                                          						Template. For more information, see the Cisco Unified Communications Manager Bulk Administration
                                                							 Guide . |
| Dialed Number Analyzer (DNA) | When
                                          						used to perform digit analysis on a gateway, DNA displays the Call
                                          						Classification that is configured for the gateway and the route pattern. For
                                          						more information, see the Cisco Unified
                                                							 Communications Manager Dialed Number Analyzer Guide . |

| Restriction | Description |
|---|---|
| FXS Gateways | FXS gateways such as Cisco Catalyst 6000 24 Port do not have
                                          						a Call Classification field on the Gateway Configuration window; therefore, the
                                          						system always considers them as OnNet. |
| Cisco VG248 Gateway | The system does not support the Cisco VG248 Gateway which does not have a Call Classification field. |
| FXS Ports | Cisco Unified
                                             						  Communications Manager considers all Cisco Unified IP
                                             						  Phone s and FXS ports as OnNet (internal) that cannot be configured as
                                          						OffNet (external). |