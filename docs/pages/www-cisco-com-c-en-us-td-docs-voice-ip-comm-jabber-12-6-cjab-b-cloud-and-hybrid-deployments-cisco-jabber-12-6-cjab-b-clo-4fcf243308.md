---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-6-cjab-b-cloud-and-hybrid-deployments-cisco-jabber-12-6-cjab-b-clo-4fcf243308
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_6/cjab_b_cloud-and-hybrid-deployments-cisco-jabber-12-6/cjab_b_cloud-and-hybrid-deployments-cisco-jabber-12-6_chapter_0111.html
retrieved_at: 2026-08-21T19:09:19.914789+00:00
---

Cloud and Hybrid Deployments for Cisco Jabber 12.6

# Cloud and Hybrid Deployments for Cisco Jabber 12.6

Updated: April 2, 2024

Chapter: Configure Deskphone Control

## Chapter: Configure Deskphone Control

# Configure Deskphone Control

## Prerequisites

The Cisco CTIManager service must be running in the Cisco Unified Communications Manager cluster.

## Configure Deskphone Control Taskflow

Step 1

Enable Device for CTI

Allows Cisco Jabber desktop clients to control the desk phone of the user.

Step 2

Configure Desk Phone Video .

Let users receive video transmitted to their desk phone devices on their computers through the client.

Step 3

Enable Video Rate Adaptation

The client uses video rate adaptation to negotiate optimum video quality.

Step 4

Configure User Associations

Associate users with devices and assign users to access control groups.

Step 5

Reset Devices

You must reset devices after you configure user associations.

## Enable Device for CTI

If you want Cisco Jabber desktop clients to be able to control the desk phone of the user, you must select the Allow Control of Device from CTI option when you create the device for the user.

Step 1

In Cisco Unified CM Administration, click Device > Phone and search for the phone.

Step 2

In the Device Information section, check Allow Control of Device from CTI .

Step 3

Click Save .

## Configure Desk Phone Video

Desk phone video capabilities let you receive
                              				the video signal on your laptop and the audio signal on your desk phone. Physically
                              				connect your computer to the desk phone through the computer port for the client to
                              				establish a connection to the Jabber client. You cannot use this feature with a
                              				wireless connection to your desk phone.

If you have both wireless and wired
                                          					connections available, configure Microsoft Windows to not prioritize wireless
                                          					connections over wired connections. See Microsoft's An explanation of the
                                             						Automatic Metric feature for Internet Protocol routes for more
                                          					information.

First, download and install Jabber Desk Phone
                              				Video Services Interface from Cisco.com. Jabber Desk Phone Video Services Interface
                              				provides the Cisco Discover Protocol (CDP) driver. CDP enables the client to:

Discover the desk
                                    						phone.

Establish and maintain a
                                    						connection to the desk phone using the Cisco Audio Session Tunnel (CAST)
                                    						protocol.

Desk Phone Video Considerations

Review the following considerations and
                              				limitations before you set up the desk phone video feature:

You cannot have more than one video device connected with CAST. You cannot
                                    						use a desk phone with a built-in camera with this feature. If your desk
                                    						phone has a local USB camera, remove it before using this feature.

You cannot use this
                                    						feature with devices that do not support CTI.

You cannot use both video
                                    						screen sharing, using the BFCP protocol, and desk phone video.

It is not possible for
                                    						endpoints that use SCCP to receive video only. SCCP endpoints must send and
                                    						receive video. Instances where SCCP endpoints do not send a video signal
                                    						result in audio only calls.

7900 series phones must
                                    						use SCCP for desk phone video capabilities. 7900 series phones cannot use
                                    						SIP for desk phone video capabilities.

If you start a call from
                                    						a desk phone's keypad, the call starts as an audio call on the desk phone.
                                    						Jabber then escalates the call to video. For this reason, you cannot make
                                    						video calls to devices that do not support the escalation, such as H.323
                                    						endpoints. To use this feature with devices that do not support escalation,
                                    						begin calls from the Jabber client.

A compatibility issue
                                    						exists with Cisco Unified IP Phones that use firmware version SCCP45.9-2-1S.
                                    						Upgrade your firmware to version SCCP45.9-3-1 to use this feature.

Some antivirus or
                                    						firewall applications, such as Symantec EndPoint Protection, block inbound
                                    						CDP packets. This blockage disables desk phone video. Configure your
                                    						antivirus or firewall application to allow inbound CDP packets.

See the following
                                    						Symantec technical document for more details about this issue: Cisco IP Phone
                                       							version 7970 and Cisco Unified Video Advantage is Blocked by Network
                                       							Threat Protection .

Do not select the Media
                                       							Termination Point Required check box on the SIP trunk
                                    						configuration for Cisco Unified Communications Manager (Unified CM). That
                                    						setting disables desk phone video.

Step 1

Physically connect your
                                       					computer to the computer port on your desk phone.

Step 2

Enable the desk phone for
                                       					video in Unified CM.

Step 3

Install Jabber Desk Phone
                                       					Video Services Interface on your computer.

### Troubleshooting Desk Phone Video

If you encounter an error that indicates desk phone video capabilities are unavailable or the desk phone device is unknown,
                                 do the following:

Ensure you enable the desk phone device for video in Cisco Unified Communications Manager.

Reset the physical desk phone.

Exit the client.

Run services.msc on the computer where you installed the client.

Restart Jabber Desk Phone Video Services Interface from the Services tab of the Windows Task Manager.

Restart the client.

## Enable Video Rate
                        	 Adaptation

The client uses
                              		  video rate adaptation to negotiate optimum video quality. Video rate adaptation
                              		  dynamically increases or decreases video quality based on network conditions.

To use video rate adaptation, you must enable Real-Time Transport Control Protocol (RTCP) on Cisco Unified Communications
                              Manager.

RTCP is enabled on software phone devices by default. However, you must enable RTCP on desk phone devices.

### Enable RTCP on Common Phone Profiles

You can enable RTCP on a common phone profile to enable video rate adaptation on all devices that use the profile.

RTCP is an integral component of Jabber Telephony services. Jabber will continue to send RTCP packets even when disabled.

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select Device > Device Settings > Common Phone Profile .

The Find and List Common Phone Profiles window opens.

Step 3

Specify the appropriate filters in the Find Common Phone Profile where field and then select Find to retrieve a list of profiles.

Step 4

Select the appropriate profile from the list.

The Common Phone Profile Configuration window opens.

Step 5

Locate the Product Specific Configuration Layout section.

Step 6

Select Enabled from the RTCP drop-down list.

Step 7

Select Save .

### Enable RTCP on Device Configurations

You can enable RTCP on specific device configurations instead of a common phone profile. The specific device configuration
                                 overrides any settings you specify on the common phone profile.

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select Device > Phone .

The Find and List Phones window opens.

Step 3

Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of phones.

Step 4

Select the appropriate phone from the list.

The Phone Configuration window opens.

Step 5

Locate the Product Specific Configuration Layout section.

Step 6

Select Enabled from the RTCP drop-down list.

Step 7

Select Save .

## Configure User
                        	 Associations

When you associate a
                              		  user with a device, you provision that device to the user.

### Before you begin

Create and
                              		  configure Cisco Jabber devices.

Step 1

Open the Cisco
                                          				Unified CM Administration interface.

Step 2

Select User
                                             				  Management > End User .

The Find
                                             				  and List Users window opens.

Step 3

Specify the
                                       			 appropriate filters in the Find
                                          				User where field and then select Find to retrieve a list of users.

Step 4

Select the
                                       			 appropriate user from the list.

The End
                                             				  User Configuration window opens.

Step 5

Locate the Service Settings section.

Step 6

Select the appropriate service profile for the user from the UC Service Profile drop-down list.

Step 7

Locate the Device
                                          				Information section.

Step 8

Select Device
                                          				Association .

The User
                                             				  Device Association window opens.

Step 9

Select the devices to which you want to associate the user. Jabber only supports a single softphone association per device
                                       type. For example, only one TCT, BOT, CSF, and TAB device can be associated with a user.

Step 10

Select Save
                                          				Selected/Changes .

Step 11

Select User
                                             				  Management > End User and return to the Find and
                                          				List Users window.

Step 12

Find and select
                                       			 the same user from the list.

The End
                                             				  User Configuration window opens.

Step 13

Locate the Permissions Information section.

Step 14

Select Add to
                                          				Access Control Group .

The Find
                                             				  and List Access Control Groups dialog box opens.

Step 15

Select the
                                       			 access control groups to which you want to assign the user.

At a minimum you should assign the user to the following access control groups:

Standard CCM End Users

Standard CTI Enabled

Remember

If you are provisioning users with secure phone capabilities, do not assign the users to the Standard CTI Secure Connection group.

Certain phone models require additional control groups, as follows:

Cisco Unified IP Phone 9900, 8900, or 8800 series or DX series, select Standard CTI Allow Control of Phones supporting Connected Xfer and conf .

Cisco Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover Mode .

Step 16

Select Add
                                          				Selected .

The Find
                                             				  and List Access Control Groups window closes.

Step 17

Select Save on the End User
                                          				Configuration window.

## Reset Devices

After you create and associate users with devices, you should reset those devices.

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select Device > Phone .

The Find and List Phones window opens.

Step 3

Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices.

Step 4

Select the appropriate device from the list.

The Phone Configuration window opens.

Step 5

Locate the Association Information section.

Step 6

Select the appropriate directory number configuration.

The Directory Number Configuration window opens.

Step 7

Select Reset .

The Device Reset dialog box opens.

Step 8

Select Reset .

Step 9

Select Close to close the Device Reset dialog box.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Device for CTI | Allows Cisco Jabber desktop clients to control the desk phone of the user. |
| Step 2 | Configure Desk Phone Video . | Let users receive video transmitted to their desk phone devices on their computers through the client. |
| Step 3 | Enable Video Rate Adaptation | The client uses video rate adaptation to negotiate optimum video quality. |
| Step 4 | Configure User Associations | Associate users with devices and assign users to access control groups. |
| Step 5 | Reset Devices | You must reset devices after you configure user associations. |

| Step 1 | In Cisco Unified CM Administration, click Device > Phone and search for the phone. |
|---|---|
| Step 2 | In the Device Information section, check Allow Control of Device from CTI . |
| Step 3 | Click Save . |

| Note | If you have both wireless and wired
                                          					connections available, configure Microsoft Windows to not prioritize wireless
                                          					connections over wired connections. See Microsoft's An explanation of the
                                             						Automatic Metric feature for Internet Protocol routes for more
                                          					information. |
|---|---|

| Step 1 | Physically connect your
                                       					computer to the computer port on your desk phone. |
|---|---|
| Step 2 | Enable the desk phone for
                                       					video in Unified CM. |
| Step 3 | Install Jabber Desk Phone
                                       					Video Services Interface on your computer. |

| Note | RTCP is enabled on software phone devices by default. However, you must enable RTCP on desk phone devices. |
|---|---|

| Note | RTCP is an integral component of Jabber Telephony services. Jabber will continue to send RTCP packets even when disabled. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Device Settings > Common Phone Profile . The Find and List Common Phone Profiles window opens. |
| Step 3 | Specify the appropriate filters in the Find Common Phone Profile where field and then select Find to retrieve a list of profiles. |
| Step 4 | Select the appropriate profile from the list. The Common Phone Profile Configuration window opens. |
| Step 5 | Locate the Product Specific Configuration Layout section. |
| Step 6 | Select Enabled from the RTCP drop-down list. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of phones. |
| Step 4 | Select the appropriate phone from the list. The Phone Configuration window opens. |
| Step 5 | Locate the Product Specific Configuration Layout section. |
| Step 6 | Select Enabled from the RTCP drop-down list. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco
                                          				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
                                             				  Management > End User . The Find
                                             				  and List Users window opens. |
| Step 3 | Specify the
                                       			 appropriate filters in the Find
                                          				User where field and then select Find to retrieve a list of users. |
| Step 4 | Select the
                                       			 appropriate user from the list. The End
                                             				  User Configuration window opens. |
| Step 5 | Locate the Service Settings section. |
| Step 6 | Select the appropriate service profile for the user from the UC Service Profile drop-down list. |
| Step 7 | Locate the Device
                                          				Information section. |
| Step 8 | Select Device
                                          				Association . The User
                                             				  Device Association window opens. |
| Step 9 | Select the devices to which you want to associate the user. Jabber only supports a single softphone association per device
                                       type. For example, only one TCT, BOT, CSF, and TAB device can be associated with a user. |
| Step 10 | Select Save
                                          				Selected/Changes . |
| Step 11 | Select User
                                             				  Management > End User and return to the Find and
                                          				List Users window. |
| Step 12 | Find and select
                                       			 the same user from the list. The End
                                             				  User Configuration window opens. |
| Step 13 | Locate the Permissions Information section. |
| Step 14 | Select Add to
                                          				Access Control Group . The Find
                                             				  and List Access Control Groups dialog box opens. |
| Step 15 | Select the
                                       			 access control groups to which you want to assign the user. At a minimum you should assign the user to the following access control groups: Standard CCM End Users Standard CTI Enabled Remember If you are provisioning users with secure phone capabilities, do not assign the users to the Standard CTI Secure Connection group. Certain phone models require additional control groups, as follows: Cisco Unified IP Phone 9900, 8900, or 8800 series or DX series, select Standard CTI Allow Control of Phones supporting Connected Xfer and conf . Cisco Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover Mode . | Remember | If you are provisioning users with secure phone capabilities, do not assign the users to the Standard CTI Secure Connection group. |
| Remember | If you are provisioning users with secure phone capabilities, do not assign the users to the Standard CTI Secure Connection group. |
| Step 16 | Select Add
                                          				Selected . The Find
                                             				  and List Access Control Groups window closes. |
| Step 17 | Select Save on the End User
                                          				Configuration window. |

| Remember | If you are provisioning users with secure phone capabilities, do not assign the users to the Standard CTI Secure Connection group. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices. |
| Step 4 | Select the appropriate device from the list. The Phone Configuration window opens. |
| Step 5 | Locate the Association Information section. |
| Step 6 | Select the appropriate directory number configuration. The Directory Number Configuration window opens. |
| Step 7 | Select Reset . The Device Reset dialog box opens. |
| Step 8 | Select Reset . |
| Step 9 | Select Close to close the Device Reset dialog box. |