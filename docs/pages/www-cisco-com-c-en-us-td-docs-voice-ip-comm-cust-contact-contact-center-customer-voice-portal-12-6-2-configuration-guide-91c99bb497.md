---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-configuration-guide-91c99bb497
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/configuration/guide/ccvp_b_1262-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-configuration-guide-for-cisco-unified-customer-voice-portal-release-1252_chapter_010101.html
retrieved_at: 2026-08-21T11:58:38.973795+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Network-based Recording Configuration

## Chapter: Network-based Recording Configuration

# Network-based Recording Configuration

## CUCM
                        	 Configuration

Network- based
                           		recording is configured using Cisco Unified Communications Manager
                           		Administration. Network-based recording is controlled by using a recording
                           		profile assigned to the line. The recording can be selective or full-time
                           		audio-only recording. You can either configure CUBE or phone as the forking
                           		device and you can change the forking device during a call.

## Create a Recording
                        	 Profile

Step 1

From Cisco Unified Communications Manager Administration , choose Device > Device Settings > Recording Profile .

Step 2

To add a new
                                       			 recording profile, click Add
                                          				New .

Step 3

In the Name field, enter a name to identify the recording
                                       			 profile.

Step 4

In the Recording Destination Address field, enter the
                                       			 directory number (DN) or the URL of the recorder that associates with this
                                       			 recording profile. This field allows any characters except the following
                                       			 characters: double quotation marks (“), back quote (‘), and space ( ).

Step 5

Click Save .

## Configure the SIP
                        	 Trunk from CUCM to Recording Server

Step 1

From Cisco Unified Communications Manager Administration , choose Device > Trunk .

Step 2

To add a new
                                       			 SIP trunk, click Add
                                          				New .

Step 3

In the Device Name field, enter a unique identifier for the trunk (which is the IP address of the Recording server).

For Call Transcript, the IP address should be that of the Call Server.

Step 4

In the Description field, enter a name for the trunk.

Step 5

From the SIP
                                          				Profile drop-down list, choose Standard SIP Profile for this SIP trunk.

Step 6

In the Recording Information section, click None .

Step 7

Click Save .

## Creating a
                        	 Recorder Route Group

Step 1

From Cisco Unified Communications Manager Administration , choose Call Routing > Route/Hunt > Route Group .

Step 2

In the Available Devices drop-down list, choose a device to add and click Add to Route Group to move it to the Selected Devices list box. Repeat this step for each device that you want to add to this route group.

If an SIP trunk is already configured for CVP, Route Group does not list that trunk.

Step 3

In the Selected Devices drop-down list, choose the order in
                                       			 which the new device or devices must be accessed in this route group. To change
                                       			 the order of devices, click a device and use the Up and Down arrows to the right of the list box.

Step 4

To add the new
                                       			 device or devices, and to update the device order for this route group, click Save .

## Add a Route Group
                        	 to a Route List

Step 1

From Cisco Unified Communications Manager Administration , select Call Routing > Route/Hunt > Route List .

Step 2

Select the route list to which you want to add the route group.

Step 3

Click Add Route Group .

Step 4

Select/enter values for the fields.

Step 5

Click Save .

Step 6

Click OK .

## Create a Route
                        	 Pattern Based on the DN for the Recorder

Step 1

From Cisco Unified Communications Manager Administration , choose Call Routing > Route/Hunt > Route Pattern .

Step 2

Select the route list for which you are adding a route pattern.

Step 3

Select/enter values for the fields.

Step 4

Click Save .

Step 5

Click OK .

## Configure the
                        	 Device Phone for Recording

Step 1

From Cisco Unified Communications Manager Administration , choose Device > Phone . Click Find to list the phones.

Step 2

Click Find .

Step 3

From the Association Information area, click the link
                                       			 associated with your phone.

Step 4

From the Recording Option drop-down list, choose one of the
                                       			 following options:

- Call Recording
                                             				  Disabled —The calls that the agent makes on this line appearance are
                                          				not recorded.

- Automatic Call Recording
                                             				  Enabled —The calls that the agent makes on this line appearance are
                                          				automatically recorded.

- Application Invoked Call
                                             				  Recording Enabled —The calls that the agent makes on this line
                                          				appearance are recorded if an application invokes calling recording.

- Device Invoked Call
                                             				  Recording Enabled —This option supports the external call control
                                          				feature. If the policies on the policy server dictate that a chaperone must
                                          				monitor and record calls, choose this option.

Step 5

From the Recording Profile drop-down list, choose an existing
                                       			 recording profile.

Step 6

Set the Recording Media Source preference (either Phone
                                       			 Preferred or Gateway Preferred) when enabling recording on the line appearance
                                       			 of the device.

Step 7

Click Save .

## Enable the Device
                        	 Phone for Recording

Step 1

To enable phone-based recording, choose Device > Phone from Cisco Unified Communications Manager Administration .

Step 2

From the Built
                                          				In Bridge drop-down list, choose On .

Step 3

If the
                                       			 recorder does not support codecs (for example, G.722, ILIBC), enable Cisco
                                       			 Unified CM to ignore the preference if audio codecs.

Choose System > Service
                                                   						Parameters .

From the Server drop-down list, choose the server.

From the Server drop-down list, choose the service that
                                             				  contains the Accept Audio Codec Preferences in Received Offer parameter.

From the Accept Audio Codec Preferences in Received Offer drop-down list, choose Off .

Click Save .

## Configure the
                        	 Ingress Gateway for Recording

Step 1

From Cisco Unified Communications Manager Administration , choose Device > Trunk .

Step 2

In the Device
                                          				Name field, enter the IP address of the Ingress Gateway.

Step 3

From the Device
                                          				Pool drop-down list, choose Default .

Step 4

From the Call Classification drop-down list, choose Use System Default .

Step 5

From the Location drop-down list, choose Hub_None .

The locations feature does not track the bandwidth that this
                                          				device consumes.

Step 6

From the AAR Group drop-down list, choose None .

Step 7

From the Tunneled Protocol drop-down list, choose None .

Step 8

From the QSIG Variant drop-down list, choose No Changes. .

Step 9

From the ASN.1 ROSE OID Encoding drop-down list, choose No Changes .

Step 10

From the Packet Capture Mode drop-down list, choose None .

Step 11

In the Recording Information area, click the This trunk connects to a recording-enabled
                                          				gateways radio button.

Step 12

Click Save .

## Configure the
                        	 Outgoing Trunk from CVP to CUCM

Step 1

To create a new SIP profile for recording, choose Device > Device Settings > SIP Profile from Cisco Unified Communications Manager Administration .

Step 2

To add a new
                                       			 SIP profile, click Add
                                          				New .

Step 3

In the Name field, enter a name to identify the SIP
                                       			 profile.

Step 4

In the Default MTP Telephony Event Payload Type field,
                                       			 enter the default value, 101.

Step 5

From the Early
                                          				Offer for G.Clear Calls drop-down list, choose Disabled to disable Early Offer for G.Clear Calls.

Step 6

From the User-Agent and Server header information drop-down
                                       			 list, choose Send
                                          				Unified CM Version Information as User-Agent Header .

Step 7

From the Version in User-Agent and Server Headers drop-down
                                       			 list, choose Major
                                          				and Minor .

Step 8

From the Dial
                                          				String Interpretation drop-down list, choose Phone
                                          				number .

Step 9

From the Confidential Access Level Headers drop-down list,
                                       			 choose Disabled .

Step 10

From the SDP
                                          				Session-level Bandwidth Modifier for Early Offer and Re-invites drop-down list, choose TIAS
                                          				and AS .

Step 11

From the Accept
                                          				Audio Codec Preferences in Received Offer drop-down list, choose Default .

Step 12

Click Save .

## Gateway Setup for Network-based Recording

```
uc wsapi
  message-exchange max-failures 100
  response-timeout 300
  source-address <IP address of gateway>
  probing interval negative 20
  probing interval keepalive 255

  provider xmf	
  remote-url 1 http://<IP address of CUCM>:8090/ucm_xml
```

When using ISR G2 for network-based recording, ensure that the VXML Voice Gateway functionality is not enabled on the same gateway.

In case of multiple subscribers, specify the URL for each subscriber and select the Run on All Active CM Nodes check box in CUCM SIP trunk.

For more information, please refer the section Network-Based Recording in Cisco Unified Border Element Configuration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-border-element/products-installation-and-configuration-guides-list.html .

| Step 1 | From Cisco Unified Communications Manager Administration , choose Device > Device Settings > Recording Profile . |
|---|---|
| Step 2 | To add a new
                                       			 recording profile, click Add
                                          				New . |
| Step 3 | In the Name field, enter a name to identify the recording
                                       			 profile. |
| Step 4 | In the Recording Destination Address field, enter the
                                       			 directory number (DN) or the URL of the recorder that associates with this
                                       			 recording profile. This field allows any characters except the following
                                       			 characters: double quotation marks (“), back quote (‘), and space ( ). |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Device > Trunk . |
|---|---|
| Step 2 | To add a new
                                       			 SIP trunk, click Add
                                          				New . |
| Step 3 | In the Device Name field, enter a unique identifier for the trunk (which is the IP address of the Recording server). Note For Call Transcript, the IP address should be that of the Call Server. | Note | For Call Transcript, the IP address should be that of the Call Server. |
| Note | For Call Transcript, the IP address should be that of the Call Server. |
| Step 4 | In the Description field, enter a name for the trunk. |
| Step 5 | From the SIP
                                          				Profile drop-down list, choose Standard SIP Profile for this SIP trunk. |
| Step 6 | In the Recording Information section, click None . |
| Step 7 | Click Save . |

| Note | For Call Transcript, the IP address should be that of the Call Server. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration , choose Call Routing > Route/Hunt > Route Group . |
|---|---|
| Step 2 | In the Available Devices drop-down list, choose a device to add and click Add to Route Group to move it to the Selected Devices list box. Repeat this step for each device that you want to add to this route group. Note If an SIP trunk is already configured for CVP, Route Group does not list that trunk. | Note | If an SIP trunk is already configured for CVP, Route Group does not list that trunk. |
| Note | If an SIP trunk is already configured for CVP, Route Group does not list that trunk. |
| Step 3 | In the Selected Devices drop-down list, choose the order in
                                       			 which the new device or devices must be accessed in this route group. To change
                                       			 the order of devices, click a device and use the Up and Down arrows to the right of the list box. |
| Step 4 | To add the new
                                       			 device or devices, and to update the device order for this route group, click Save . |

| Note | If an SIP trunk is already configured for CVP, Route Group does not list that trunk. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration , select Call Routing > Route/Hunt > Route List . |
|---|---|
| Step 2 | Select the route list to which you want to add the route group. The Route List Configuration page is displayed. |
| Step 3 | Click Add Route Group . The Route List Details Configuration page is displayed. |
| Step 4 | Select/enter values for the fields. |
| Step 5 | Click Save . A confirmation message is displayed. |
| Step 6 | Click OK . The route list configuration is saved and the route group is added. |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Call Routing > Route/Hunt > Route Pattern . The Find and List Route Patterns page is displayed. |
|---|---|
| Step 2 | Select the route list for which you are adding a route pattern. The Route Pattern Configuration page is displayed. |
| Step 3 | Select/enter values for the fields. |
| Step 4 | Click Save . A confirmation message is displayed. |
| Step 5 | Click OK . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Device > Phone . Click Find to list the phones. |
|---|---|
| Step 2 | Click Find . Choose the trunk profile that you want to view. |
| Step 3 | From the Association Information area, click the link
                                       			 associated with your phone. |
| Step 4 | From the Recording Option drop-down list, choose one of the
                                       			 following options: Call Recording
                                             				  Disabled —The calls that the agent makes on this line appearance are
                                          				not recorded. Automatic Call Recording
                                             				  Enabled —The calls that the agent makes on this line appearance are
                                          				automatically recorded. Application Invoked Call
                                             				  Recording Enabled —The calls that the agent makes on this line
                                          				appearance are recorded if an application invokes calling recording. Device Invoked Call
                                             				  Recording Enabled —This option supports the external call control
                                          				feature. If the policies on the policy server dictate that a chaperone must
                                          				monitor and record calls, choose this option. |
| Step 5 | From the Recording Profile drop-down list, choose an existing
                                       			 recording profile. |
| Step 6 | Set the Recording Media Source preference (either Phone
                                       			 Preferred or Gateway Preferred) when enabling recording on the line appearance
                                       			 of the device. |
| Step 7 | Click Save . |

| Step 1 | To enable phone-based recording, choose Device > Phone from Cisco Unified Communications Manager Administration . |
|---|---|
| Step 2 | From the Built
                                          				In Bridge drop-down list, choose On . |
| Step 3 | If the
                                       			 recorder does not support codecs (for example, G.722, ILIBC), enable Cisco
                                       			 Unified CM to ignore the preference if audio codecs. Choose System > Service
                                                   						Parameters . From the Server drop-down list, choose the server. From the Server drop-down list, choose the service that
                                             				  contains the Accept Audio Codec Preferences in Received Offer parameter. From the Accept Audio Codec Preferences in Received Offer drop-down list, choose Off . Click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Device > Trunk . |
|---|---|
| Step 2 | In the Device
                                          				Name field, enter the IP address of the Ingress Gateway. |
| Step 3 | From the Device
                                          				Pool drop-down list, choose Default . |
| Step 4 | From the Call Classification drop-down list, choose Use System Default . |
| Step 5 | From the Location drop-down list, choose Hub_None . The locations feature does not track the bandwidth that this
                                          				device consumes. |
| Step 6 | From the AAR Group drop-down list, choose None . |
| Step 7 | From the Tunneled Protocol drop-down list, choose None . |
| Step 8 | From the QSIG Variant drop-down list, choose No Changes. . |
| Step 9 | From the ASN.1 ROSE OID Encoding drop-down list, choose No Changes . |
| Step 10 | From the Packet Capture Mode drop-down list, choose None . |
| Step 11 | In the Recording Information area, click the This trunk connects to a recording-enabled
                                          				gateways radio button. |
| Step 12 | Click Save . |

| Step 1 | To create a new SIP profile for recording, choose Device > Device Settings > SIP Profile from Cisco Unified Communications Manager Administration . |
|---|---|
| Step 2 | To add a new
                                       			 SIP profile, click Add
                                          				New . |
| Step 3 | In the Name field, enter a name to identify the SIP
                                       			 profile. |
| Step 4 | In the Default MTP Telephony Event Payload Type field,
                                       			 enter the default value, 101. |
| Step 5 | From the Early
                                          				Offer for G.Clear Calls drop-down list, choose Disabled to disable Early Offer for G.Clear Calls. |
| Step 6 | From the User-Agent and Server header information drop-down
                                       			 list, choose Send
                                          				Unified CM Version Information as User-Agent Header . |
| Step 7 | From the Version in User-Agent and Server Headers drop-down
                                       			 list, choose Major
                                          				and Minor . |
| Step 8 | From the Dial
                                          				String Interpretation drop-down list, choose Phone
                                          				number . |
| Step 9 | From the Confidential Access Level Headers drop-down list,
                                       			 choose Disabled . |
| Step 10 | From the SDP
                                          				Session-level Bandwidth Modifier for Early Offer and Re-invites drop-down list, choose TIAS
                                          				and AS . |
| Step 11 | From the Accept
                                          				Audio Codec Preferences in Received Offer drop-down list, choose Default . |
| Step 12 | Click Save . |

| Note | When using ISR G2 for network-based recording, ensure that the VXML Voice Gateway functionality is not enabled on the same gateway. In case of multiple subscribers, specify the URL for each subscriber and select the Run on All Active CM Nodes check box in CUCM SIP trunk. For more information, please refer the section Network-Based Recording in Cisco Unified Border Element Configuration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-border-element/products-installation-and-configuration-guides-list.html . |
|---|---|