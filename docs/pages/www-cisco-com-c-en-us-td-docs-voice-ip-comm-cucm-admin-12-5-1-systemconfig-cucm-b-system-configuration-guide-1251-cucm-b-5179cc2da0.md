---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-5179cc2da0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0111100.html
retrieved_at: 2026-08-16T17:33:45.210304+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Annunciator

## Chapter: Configure Annunciator

# Configure Annunciator

## Annunciator
                        	 Overview

An annunciator is an SCCP software devices that runs on Cisco Unified Communications Manager and which allows you to send
                              prerecorded messages and tones to Cisco IP Phones and gateways. The annunciator is activated on a cluster node by turning
                              on the Cisco IP Voice Media Streaming service on that node. Features such as MLPP, SIP trunks, IOS gateways, and software
                              conference bridges rely on the annunciator to send the predefined message to the phone or gateway via a one-way media stream.
                              In addition:

Both IPv4 and IPV6 are supported. The annunciator is configured automatically in dual mode when the system's platform is configured
                                    for IPv6 and the IPv6 enterprise parameter is enabled.

SRTP is supported

### Annunciator Scalability

By default, an annunciator supports 48 simultaneous media streams. You can add capacity by activating the annunciator on additional
                              nodes or by changing the default number of annunciator media streams via the Call Count service parameter. However, it's not recommended to increase this value on a node unless the Cisco CallManager service is deactivated on that node.

If the annunciator runs on a dedicated subscriber node where the Cisco CallManager service does not run, the annunciator can support up to 255 simultaneous announcement streams. If the dedicated subscriber
                              node meets the OVA virtual machine configuration for 10,000 users, the annunciator can support up to 400 simultaneous announcement
                              streams.

Caution

We recommend that you do not activate the annunciator on Unified Communications Manager nodes that have a high call-processing load.

### Annunciator with Conference Bridge

The Annunciator is available to a conference bridge under the following conditions:

If the media resource group list that contains the annunciator is assigned to the device pool where the conference bridge
                                    exists.

If the annunciator is configured as the default media resource.

The annunciator is not available to a conference bridge if the media resource group list is assigned directly to the device
                              that controls the conference.

Each conference supports only one announcement. If the system requests another announcement while the current announcement
                              is playing, the new announcement preempts the one that is playing.

### Default Annunciator Announcements and Tones

Announcement —
                                          				Played for devices that are configured for Cisco Multilevel Precedence and
                                          				Preemption.

Barge tone —
                                          				Heard before a participant joins an ad hoc conference.

Ring back tone
                                          				— When you transfer a call over the PSTN through an IOS gateway, the
                                          				annunciator plays the tone because the gateway cannot play the tone when the
                                          				call is active.

Ring back tone
                                          				— When you transfer calls over an H.323 intercluster trunk, a tone is played.

Ring back tone
                                          				— When you transfer calls to the SIP client from a phone that is running SCCP,
                                          				a tone is played.

You cannot change
                                 		  the default prerecorded annunciator announcements or add additional
                                 		  announcements. Localization of the announcement is supported if the Cisco Unified Communications Manager Locale Installer
                                 		  is installed and the locale settings are configured for the Cisco Unified IP
                                 		  Phone or device pool. For information about the Locale Installer and the files
                                 		  to install for user and (combined) network locales, see Installing
                                    			 Cisco Unified Communications Manager . To download the locale installer,
                                 		  see the support pages at www.cisco.com .

Condition

Announcement

An equal
                                             					 or higher precedence call is in progress.

Precedence
                                             					 access limitation has prevented the completion of your call. Please hang up and
                                             					 try again. This is a recording.

A
                                             					 precedence access limitation exists.

Precedence
                                             					 access limitation has prevented the completion of your call. Please hang up and
                                             					 try again. This is a recording.

Someone
                                             					 attempted an unauthorized precedence level.

The
                                             					 precedence used is not authorized for your line. Please use an authorized
                                             					 precedence or ask your operator for assistance. This is a recording.

The call
                                             					 appears busy, or the administrator did not configure the directory number for
                                             					 call waiting or preemption.

The number
                                             					 you have dialed is busy and not equipped for call waiting or preemption. Please
                                             					 hang up and try again. This is a recording.

The system
                                             					 cannot complete the call.

Your call
                                             					 cannot be completed as dialed. Please consult your directory and call again or
                                             					 ask your operator for assistance. This is a recording.

A service
                                             					 interruption occurred.

A service
                                             					 disruption has prevented the completion of your call. In case of emergency call
                                             					 your operator. This is a recording.

The following
                                 		  table lists the tones that the annunciator supports.

Type

Description

Busy
                                             					 tone

A busy
                                             					 tone is heard when the dialed number is busy.

Barge tone

A
                                             					 conference barge-in tone is heard before the participant joins an ad hoc
                                             					 conference.

Ring back
                                             					 tone

When
                                                      						  you transfer a call over the PSTN through an IOS gateway.

When
                                                      						  you transfer a call over an H.323 intercluster trunk.

When
                                                      						  you transfer a call to the SIP client from an SCCP phone.

### Annunciator Use With  Conference Bridges

The  Annunciator is available to a conference bridge under the following conditions:

If the media resource group list that contains the annunciator is assigned to the device pool where the conference bridge
                                       exists.

If the annunciator is configured as the default media resource.

The annunciator is not available  to a conference bridge if the media resource group list is
                                 assigned directly to the device that controls the conference.

Each conference supports only one announcement. If the system
                                 				requests another announcement while the current announcement is playing, the
                                 				new announcement preempts the one that is playing.

## Annunciator Configuration Task Flow

Step 1

Activate the Annunciator

Activate the  Cisco IP Voice Media Streaming
                                          				Application service on the node to activate the annunciator for that node. Activate only one Cisco IP Voice Media Streaming
                                          Application
                                          				service for each annunciator device in the cluster.

Step 2

Media Resource Group Task Flow

Add the annunciator to media resource groups and lists to manage your media resources using Cisco Unified Communications Manager Administration . You can see which media resource groups have annunciators from the Dependency Records Summary window.

Step 3

Configure Device Pools

Add the media resource group that includes the annunciator to a device pool using Cisco Unified Communications Manager Administration . Repeat this step for each annunciator. Each annunciator must belong to a device pool.

Step 4

(Optional) Change the Default Number of Media Streams

You can change the default number of media streams for an annunciator.

Step 5

(Optional) Override the Annunciator Security Mode

When Cisco Unified
                                             Communications Manager is configured in a secured deployment, the media streaming between the annunciator and security enabled devices is automatically
                                          encrypted using the Secure Real-Time Protocol (SRTP). You 
                                          can override the annunciator security settings so that media streamed from the secured annunciator is not encrypted.

Step 6

(Optional) View List of Media Resource Groups That Have Annunciators

You can see which media resource groups use the annunciator device.

Step 7

(Optional) Configure Annunciator for Conference Bridges

You can use the annunciator with conference bridges when the annunciator and conference bridge belong to the same device pool.

### Activate the Annunciator

Activate only one Cisco IP Voice Media Streaming Application
                                 				service for each annunciator device in the cluster.

Caution

We recommend that you do not activate the annunciator  on Cisco Unified Communications
                                                				  Manager nodes that have a high call-processing load.

Step 1

From the Serviceability GUI, choose Tools > Activation . The Service Activation window appears.

Step 2

Select the node in the Server field and click Go .

Step 3

Check Cisco IP Voice Media Streaming
                                             				Application , and then click Save .

#### What to do next

If you haven't yet set up your media resource group and assigned it to a device pool, Media Resources Configuration Task Flow .

Otherwise, Change the Default Number of Media Streams .

### Change the Default Number of Media Streams

An annunciator supports 48 simultaneous media streams by default. You can change the default number of media streams using
                                 the annunciator service parameter; however, we recommend that you do not exceed 48 annunciator streams on a node.

#### Before you begin

Activate the Annunciator

Step 1

From Cisco Unified Communications Manager Administration , choose System > Service Parameters .

Step 2

In the Service Parameters Configuration window, select the  server and then select the service called Cisco IP Voice Media Streaming App.

Step 3

In the Service Parameter Configuration window, enter the number of simultaneous media streams in the Call Count field of the Annunciator (ANN) Parameters section, and then click Save .

When you update the annunciator, the changes automatically occur when the annunciator is idle and no active announcements
                                             are playing.

#### What to do next

Override the Annunciator Security Mode

### Override the Annunciator Security Mode

When the enterprise parameter called Cluster Security Mode is set to 1 (mixed mode), annunciator devices are automatically
                                 enable for security. The annunciator registers as a secured SRTP device on Cisco Unified Communications Manager nodes that have Secure Real-Time Protocol (SRTP) enabled. A locked icon appears on SRTP capable devices. Announcements from
                                 a secured annunciator are encrypted if the receiving device is also SRTP capable; otherwise, unsecured announcements and tones
                                 are sent.

You can override the annunciator security mode using the service parameter called Make Annunciator Non-secure when Cluster
                                 Security is Mixed. When the annunciator security mode is overridden, an unencrypted announcement is played even if the receiving
                                 device is SRTP capable.

#### Before you begin

Change the Default Number of Media Streams

Step 1

From Cisco Unified Communications Manager Administration , choose System > Service Parameters .

Step 2

Select the node in the Server field.

Step 3

Select Cisco Unified IP Voice Media Streaming Application in the Service field.

Step 4

Set Make Annunciator Non-secure when Cluster Security is Mixed to True , and then click Save .

Tip

Click Advanced if you do not see the Make Annunciator Non-secure when Cluster Security is Mixed parameter.

#### What to do next

View List of Media Resource Groups That Have Annunciators

### View List of Media Resource Groups That Have Annunciators

View the Dependency Records Summary window to see which media resource groups use the annunciator device.

#### Before you begin

Override the Annunciator Security Mode

Step 1

From Cisco Unified CM Administration, choose Media Resources > Annunciator .

Step 2

Select the annunciator that is set up for your system.

Step 3

From the Related Links drop-down list box, choose Dependency Records and click Go .

#### What to do next

Configure Annunciator for Conference Bridges

### Configure Annunciator for Conference Bridges

You can use the annunciator with conference bridges.

#### Before you begin

View List of Media Resource Groups That Have Annunciators

Step 1

Add the annunciator to a media resource group list.

Step 2

Assign the media resource group list that contains the annunciator to the device pool of the conference bridge to make the
                                          annunciator available to all devices in the cluster.

| Caution | We recommend that you do not activate the annunciator on Unified Communications Manager nodes that have a high call-processing load. |
|---|---|

| Condition | Announcement |
|---|---|
| An equal
                                             					 or higher precedence call is in progress. | Precedence
                                             					 access limitation has prevented the completion of your call. Please hang up and
                                             					 try again. This is a recording. |
| A
                                             					 precedence access limitation exists. | Precedence
                                             					 access limitation has prevented the completion of your call. Please hang up and
                                             					 try again. This is a recording. |
| Someone
                                             					 attempted an unauthorized precedence level. | The
                                             					 precedence used is not authorized for your line. Please use an authorized
                                             					 precedence or ask your operator for assistance. This is a recording. |
| The call
                                             					 appears busy, or the administrator did not configure the directory number for
                                             					 call waiting or preemption. | The number
                                             					 you have dialed is busy and not equipped for call waiting or preemption. Please
                                             					 hang up and try again. This is a recording. |
| The system
                                             					 cannot complete the call. | Your call
                                             					 cannot be completed as dialed. Please consult your directory and call again or
                                             					 ask your operator for assistance. This is a recording. |
| A service
                                             					 interruption occurred. | A service
                                             					 disruption has prevented the completion of your call. In case of emergency call
                                             					 your operator. This is a recording. |

| Type | Description |
|---|---|
| Busy
                                             					 tone | A busy
                                             					 tone is heard when the dialed number is busy. |
| Barge tone | A
                                             					 conference barge-in tone is heard before the participant joins an ad hoc
                                             					 conference. |
| Ring back
                                             					 tone | An alert
                                             					 tone is heard for the following scenarios: When
                                                      						  you transfer a call over the PSTN through an IOS gateway. When
                                                      						  you transfer a call over an H.323 intercluster trunk. When
                                                      						  you transfer a call to the SIP client from an SCCP phone. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate the Annunciator | Activate the  Cisco IP Voice Media Streaming
                                          				Application service on the node to activate the annunciator for that node. Activate only one Cisco IP Voice Media Streaming
                                          Application
                                          				service for each annunciator device in the cluster. |
| Step 2 | Media Resource Group Task Flow | Add the annunciator to media resource groups and lists to manage your media resources using Cisco Unified Communications Manager Administration . You can see which media resource groups have annunciators from the Dependency Records Summary window. |
| Step 3 | Configure Device Pools | Add the media resource group that includes the annunciator to a device pool using Cisco Unified Communications Manager Administration . Repeat this step for each annunciator. Each annunciator must belong to a device pool. |
| Step 4 | (Optional) Change the Default Number of Media Streams | (Optional) You can change the default number of media streams for an annunciator. |
| Step 5 | (Optional) Override the Annunciator Security Mode | (Optional) When Cisco Unified
                                             Communications Manager is configured in a secured deployment, the media streaming between the annunciator and security enabled devices is automatically
                                          encrypted using the Secure Real-Time Protocol (SRTP). You 
                                          can override the annunciator security settings so that media streamed from the secured annunciator is not encrypted. |
| Step 6 | (Optional) View List of Media Resource Groups That Have Annunciators | (Optional) You can see which media resource groups use the annunciator device. |
| Step 7 | (Optional) Configure Annunciator for Conference Bridges | (Optional) You can use the annunciator with conference bridges when the annunciator and conference bridge belong to the same device pool. |

| Caution | We recommend that you do not activate the annunciator  on Cisco Unified Communications
                                                				  Manager nodes that have a high call-processing load. |
|---|---|

| Step 1 | From the Serviceability GUI, choose Tools > Activation . The Service Activation window appears. |
|---|---|
| Step 2 | Select the node in the Server field and click Go . |
| Step 3 | Check Cisco IP Voice Media Streaming
                                             				Application , and then click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose System > Service Parameters . |
|---|---|
| Step 2 | In the Service Parameters Configuration window, select the  server and then select the service called Cisco IP Voice Media Streaming App. |
| Step 3 | In the Service Parameter Configuration window, enter the number of simultaneous media streams in the Call Count field of the Annunciator (ANN) Parameters section, and then click Save . When you update the annunciator, the changes automatically occur when the annunciator is idle and no active announcements
                                             are playing. |

| Step 1 | From Cisco Unified Communications Manager Administration , choose System > Service Parameters . |
|---|---|
| Step 2 | Select the node in the Server field. |
| Step 3 | Select Cisco Unified IP Voice Media Streaming Application in the Service field. |
| Step 4 | Set Make Annunciator Non-secure when Cluster Security is Mixed to True , and then click Save . Tip Click Advanced if you do not see the Make Annunciator Non-secure when Cluster Security is Mixed parameter. | Tip | Click Advanced if you do not see the Make Annunciator Non-secure when Cluster Security is Mixed parameter. |
| Tip | Click Advanced if you do not see the Make Annunciator Non-secure when Cluster Security is Mixed parameter. |

| Tip | Click Advanced if you do not see the Make Annunciator Non-secure when Cluster Security is Mixed parameter. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Annunciator . |
|---|---|
| Step 2 | Select the annunciator that is set up for your system. |
| Step 3 | From the Related Links drop-down list box, choose Dependency Records and click Go . The Dependency Records Summary window displays the media resource groups that use the annunciator device. |

| Step 1 | Add the annunciator to a media resource group list. |
|---|---|
| Step 2 | Assign the media resource group list that contains the annunciator to the device pool of the conference bridge to make the
                                          annunciator available to all devices in the cluster. |