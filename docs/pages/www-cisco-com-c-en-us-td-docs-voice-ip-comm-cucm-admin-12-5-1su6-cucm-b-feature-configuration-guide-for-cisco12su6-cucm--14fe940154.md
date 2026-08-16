---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--14fe940154
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_011010.html
retrieved_at: 2026-08-16T16:36:53.029564+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Prime Line Support

## Chapter: Prime Line Support

# Prime Line Support

## Prime Line Support
                        	 Overview

You can configure
                           		the Prime Line Support in Cisco Unified CM Administration so that when the
                           		phone is off-hook and receives a call on any line, the system always chooses
                           		the primary line for the call.

## Prime Line Support
                        	 Prerequisites

The following devices are compatible with the Prime Line Support
                              		  feature:

Cisco Unified IP Phone 7900 Series, 8900 Series, and 9900 Series

For more information on the supported devices, see the latest version
                              		  of Cisco Unified IP Phone Guide and Cisco Unified IP Phone Administration Guide .

## Prime Line Support
                        	 Configuration Task Flow

To configure the Prime Line Support feature for either the Cisco CallManager service or devices and device profiles, perform
                              one of the following procedures.

### Before you begin

Review Prime Line Support Prerequisites .

Step 1

Configure Clusterwide Prime Line Support

(Optional) . Configure the Prime Line Support feature for the Cisco CallManager service, which applies to the entire cluster.

Step 2

Configure Prime Line Support for Devices

(Optional) . Configure the Prime Line Support feature for specific devices within the cluster, if you do not want to enable the feature
                                          clusterwide.

When you configure this parameter, going off-hook makes only the first line active on the phone, even when a call rings on
                                                      another line on the phone. So the call does not get answered on the other line.

### Configure
                           	 Clusterwide Prime Line Support

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server that is
                                          			 running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco
                                             				CallManager .

Step 4

From the Always
                                             				Use Prime Line clusterwide service parameter, choose one of the
                                          			 following options from the drop-down list:

True - When a phone goes off-hook, the primary line gets chosen and becomes the active line.

False - When a phone goes off-hook, the IP phone automatically chooses an available line as the active line.

The default
                                          				value for this service parameter is False .

Step 5

For this
                                          			 change to take effect on the SIP phones, click the ApplyConfig button in Cisco Unified CM
                                          			 Administration (for example, on the Device
                                             				Configuration window, the Device
                                             				Pool Configuration window, or any other window on which ApplyConfig
                                          			 is an option).

### Configure Prime
                           	 Line Support for Devices

Step 1

From Cisco Unified CM Administration, choose Device > Common Phone Profile .

Step 2

From the Find
                                             				and List window, choose the phone for which you want to change the
                                          			 Always Use Prime Line setting.

Step 3

From the Always Use Prime Line drop-down list, choose one of
                                          			 the following options:

- Off - When the
                                             				phone is idle and receives a call on any line, the phone user answers the call
                                             				from the line on which the call is received.

- On - When the
                                             				phone is idle (off hook) and receives a call on any line, the primary line is
                                             				chosen for the call. Calls on other lines continue to ring, and the phone user
                                             				must select those other lines to answer these calls.

- Default - Unified Communications Manager uses the configuration from the Always Use Prime Line service parameter, which supports the Cisco CallManager service.

Step 4

Click Save .

## Prime Line Support
                        	 Interactions

Always Use Prime Line

If you select On for the Always Use Prime Line parameter in the Device Profile or Default Device Profile Configuration window, a Cisco Extension Mobility user can use this feature after logging in
                                          						to the device that supports Cisco Extension Mobility.

Maximum Number of Calls and Busy Trigger Settings

When the phone already has a call on a line, Unified Communications Manager uses the configuration for the Maximum Number of Calls and Busy Trigger settings to determine how to route the call.

Auto Answer

If you choose the Auto Answer with Headset option or Auto
                                          						Answer with Speakerphone option from the Auto Answer drop-down list in Cisco
                                          						Unified CM Administration, the Auto Answer configuration overrides the
                                          						configuration for the Always Use Prime Line parameter.

## Prime Line Support Troubleshooting

### Prime Line Support
                           	 Does Not Work When Set To True

Problem When the cluster-wide
                                 		  service parameter Always
                                    			 use Prime Line is set to True and the IP phone goes off-hook, the primary
                                 		  line becomes the active line. Even if a call rings on the second line, when the
                                 		  user goes off-hook, it activates only the first line. The phone does not answer
                                 		  the call on the second line. However, when IP phones with multiple line
                                 		  appearances are used with the 7.1.2 phone load, the phone does not use the
                                 		  primary line when a second line rings. If the user picks up the handset, the
                                 		  phone answers the call on the second line.

Solution Press the line button for the primary line so that the
                                 		  secondary line is not engaged when a call is initiated.

### Unable To Answer
                           	 Inbound Calls

Problem The users are unable to
                                 		  automatically answer inbound calls after they go off-hook on IP phones, and
                                 		  must press the Answer softkey to answer the calls.

Solution To resolve the problem, perform the following procedure:

From Cisco Unified CM Administration, choose System > Service Parameters .

From the
                                       				Server drop-down list, choose the server that is running the Cisco CallManager
                                       				service.

From the
                                       				Service drop-down list, choose Cisco CallManager .

In Cluster
                                       				wide parameters (Device - phone), set Always Use Prime Line to False .

### Inbound Calls Are
                           	 Answered Automatically

Problem When an inbound call is
                                 		  received on a shared line of an IP phone, the call is answered immediately as
                                 		  the handset is lifted, without the option to either answer the call or make an
                                 		  outbound call. This behavior does not change even though Auto
                                    			 Line Select is set to disabled.

Solution To resolve the problem, perform the following procedure:

From Cisco Unified CM Administration, choose System > Service Parameters .

From the
                                       				Server drop-down list, choose the server that is running the Cisco CallManager
                                       				service.

From the
                                       				Service drop-down list, choose Cisco CallManager .

In Cluster
                                       				wide parameters (Device - phone), set Always Use Prime Line to False .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Clusterwide Prime Line Support | (Optional) . Configure the Prime Line Support feature for the Cisco CallManager service, which applies to the entire cluster. |
| Step 2 | Configure Prime Line Support for Devices | (Optional) . Configure the Prime Line Support feature for specific devices within the cluster, if you do not want to enable the feature
                                          clusterwide. Note When you configure this parameter, going off-hook makes only the first line active on the phone, even when a call rings on
                                                      another line on the phone. So the call does not get answered on the other line. | Note | When you configure this parameter, going off-hook makes only the first line active on the phone, even when a call rings on
                                                      another line on the phone. So the call does not get answered on the other line. |
| Note | When you configure this parameter, going off-hook makes only the first line active on the phone, even when a call rings on
                                                      another line on the phone. So the call does not get answered on the other line. |

| Note | When you configure this parameter, going off-hook makes only the first line active on the phone, even when a call rings on
                                                      another line on the phone. So the call does not get answered on the other line. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is
                                          			 running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco
                                             				CallManager . |
| Step 4 | From the Always
                                             				Use Prime Line clusterwide service parameter, choose one of the
                                          			 following options from the drop-down list: True - When a phone goes off-hook, the primary line gets chosen and becomes the active line. False - When a phone goes off-hook, the IP phone automatically chooses an available line as the active line. The default
                                          				value for this service parameter is False . |
| Step 5 | For this
                                          			 change to take effect on the SIP phones, click the ApplyConfig button in Cisco Unified CM
                                          			 Administration (for example, on the Device
                                             				Configuration window, the Device
                                             				Pool Configuration window, or any other window on which ApplyConfig
                                          			 is an option). Note If the new
                                                      				configuration is not applied on the SIP phones, the SIP Prime Line Support
                                                      				feature changes will not be implemented until the next reset of the Cisco
                                                      				CallManager service or reset of each affected device. | Note | If the new
                                                      				configuration is not applied on the SIP phones, the SIP Prime Line Support
                                                      				feature changes will not be implemented until the next reset of the Cisco
                                                      				CallManager service or reset of each affected device. |
| Note | If the new
                                                      				configuration is not applied on the SIP phones, the SIP Prime Line Support
                                                      				feature changes will not be implemented until the next reset of the Cisco
                                                      				CallManager service or reset of each affected device. |

| Note | If the new
                                                      				configuration is not applied on the SIP phones, the SIP Prime Line Support
                                                      				feature changes will not be implemented until the next reset of the Cisco
                                                      				CallManager service or reset of each affected device. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Common Phone Profile . |
|---|---|
| Step 2 | From the Find
                                             				and List window, choose the phone for which you want to change the
                                          			 Always Use Prime Line setting. The Phone
                                             				Configuration window appears. |
| Step 3 | From the Always Use Prime Line drop-down list, choose one of
                                          			 the following options: Off - When the
                                             				phone is idle and receives a call on any line, the phone user answers the call
                                             				from the line on which the call is received. On - When the
                                             				phone is idle (off hook) and receives a call on any line, the primary line is
                                             				chosen for the call. Calls on other lines continue to ring, and the phone user
                                             				must select those other lines to answer these calls. Default - Unified Communications Manager uses the configuration from the Always Use Prime Line service parameter, which supports the Cisco CallManager service. |
| Step 4 | Click Save . |

| Feature | Interaction |
|---|---|
| Always Use Prime Line | If you select On for the Always Use Prime Line parameter in the Device Profile or Default Device Profile Configuration window, a Cisco Extension Mobility user can use this feature after logging in
                                          						to the device that supports Cisco Extension Mobility. |
| Maximum Number of Calls and Busy Trigger Settings | When the phone already has a call on a line, Unified Communications Manager uses the configuration for the Maximum Number of Calls and Busy Trigger settings to determine how to route the call. |
| Auto Answer | If you choose the Auto Answer with Headset option or Auto
                                          						Answer with Speakerphone option from the Auto Answer drop-down list in Cisco
                                          						Unified CM Administration, the Auto Answer configuration overrides the
                                          						configuration for the Always Use Prime Line parameter. |