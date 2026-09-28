---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-1-cjab-b-cloud-and-hybrid-deployments-121-cjab-b-cloud-and-hybrid--8afe30edcc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_1/cjab_b_cloud-and-hybrid-deployments_121/cjab_b_cloud-and-hybrid-deployments_121_chapter_0111.html
retrieved_at: 2026-08-21T21:14:16.614823+00:00
---

Cloud and Hybrid Deployments for Cisco Jabber 12.1

# Cloud and Hybrid Deployments for Cisco Jabber 12.1

Updated: July 17, 2018

Chapter: Configure Deskphone Control

## Chapter: Configure Deskphone Control

# Configure Deskphone Control

## Prerequisites

The Cisco CTIManager service must be running in the Cisco Unified Communications Manager cluster.

## Configure Deskphone Control Taskflow

Enable Device for CTI

Allows Cisco Jabber desktop clients to control the desk phone of the user.

Configure Desk Phone Video .

Let users receive video transmitted to their desk phone devices on their computers through the client.

Enable Video Rate Adaptation

The client uses video rate adaptation to negotiate optimum video quality.

Configure User Associations

Associate users with devices and assign users to access control groups.

Reset Devices

You must reset devices after you configure user associations.

## Enable Device for CTI

If you want Cisco Jabber desktop clients to be able to control the desk phone of the user, you must select the Allow Control of Device from CTI option when you create the device for the user.

In Cisco Unified CM Administration, click Device > Phone and search for the phone.

In the Device Information section, check Allow Control of Device from CTI .

Click Save .

## Configure Desk Phone Video

Desk phone video capabilities let users receive video transmitted to their desk phone devices on their computers through the
                              client. Users must physically connect the computer to the desk phone device through the computer port so that the client can
                              establish a connection to the device. Users cannot use desk phone video capabilities with wireless connections to desk phone
                              devices.

If users have both wireless and wired connections available, they should configure Microsoft Windows so that wireless connections
                                          do not take priority over wired connections. See the following Microsoft documentation for more information: An explanation of the Automatic Metric feature for Internet Protocol routes .

Discover the desk phone device.

Establish and maintain a connection to the desk phone device using the CAST protocol.

Desk Phone Video Considerations

You cannot use
                                       				desk phone video capabilities on devices if video cameras are attached to the
                                       				devices, such as a Cisco Unified IP Phone 9971. You can use desk phone video
                                       				capabilities if you remove video cameras from the devices.

You cannot use
                                       				desk phone video capabilities with devices that do not support CTI.

Video desktop
                                       				sharing, using the BFCP protocol, is not supported with desk phone video.

It is not
                                       				possible for endpoints that use SCCP to receive video only. SCCP endpoints must
                                       				send and receive video. Instances where SCCP endpoints do not send video result
                                       				in audio only calls.

7900 series
                                       				phones must use SCCP for desk phone video capabilities. 7900 series phones
                                       				cannot use SIP for desk phone video capabilities.

If a user
                                       				initiates a call from the keypad on a desk phone device, the call starts as an
                                       				audio call on the desk phone device. The client then escalates the call to
                                       				video. For this reason, you cannot make video calls to devices that do not
                                       				support escalation, such as H.323 endpoints. To use desk phone video
                                       				capabilities with devices that do not support escalation, users should initiate
                                       				calls from the client.

A
                                       				compatibility issue exists with Cisco Unified IP Phones that use firmware
                                       				version SCCP45.9-2-1S. You must upgrade your firmware to version SCCP45.9-3-1
                                       				to use desk phone video capabilities.

Some antivirus
                                       				or firewall applications, such as Symantec EndPoint Protection, block inbound
                                       				CDP packets, which disables desk phone video capabilities. You should configure
                                       				your antivirus or firewall application to allow inbound CDP packets.

See the
                                       				following Symantec technical document for additional details about this issue: Cisco
                                          				  IP Phone version 7970 and Cisco Unified Video Advantage is Blocked by Network
                                          				  Threat Protection .

You must not
                                       				select the Media Termination Point Required checkbox on the SIP
                                       				trunk configuration for Cisco Unified Communications Manager. Desk phone video
                                       				capabilities are not available if you select this checkbox.

Physically connect the computer to the computer port on the desk phone device.

Enable the desk phone device for video in Cisco Unified Communications Manager.

Install Jabber Desk Phone Video Services Interface on the computer.

### Troubleshooting Desk Phone Video

Ensure you
                                          				enable the desk phone device for video in Cisco Unified Communications Manager.

Reset the
                                          				physical desk phone.

Exit the
                                          				client.

Run
                                          				services.msc on the computer where you installed the client.

Restart Jabber Desk Phone Video  Services Interface from the Services tab of the Windows Task Manager.

Restart the
                                          				client.

## Enable Video Rate
                        	 Adaptation

The client uses
                              		  video rate adaptation to negotiate optimum video quality. Video rate adaptation
                              		  dynamically increases or decreases video quality based on network conditions.

RTCP is enabled
                                             				on software phone devices by default. However, you must enable RTCP on desk
                                             				phone devices.

### Enable RTCP on Common Phone Profiles

You can enable RTCP on a common phone profile to enable video rate adaptation on all devices that use the profile.

RTCP is an integral component of Jabber Telephony services. Jabber will continue to send RTCP packets even when disabled.

Open the Cisco Unified CM Administration interface.

Select Device > Device Settings > Common Phone Profile .

The Find and List Common Phone Profiles window opens.

Specify the appropriate filters in the Find Common Phone Profile where field and then select Find to retrieve a list of profiles.

Select the appropriate profile from the list.

The Common Phone Profile Configuration window opens.

Locate the Product Specific Configuration Layout section.

Select Enabled from the RTCP drop-down list.

Select Save .

### Enable RTCP on Device Configurations

You can enable RTCP on specific device configurations instead of a common phone profile. The specific device configuration
                                 overrides any settings you specify on the common phone profile.

Open the Cisco Unified CM Administration interface.

Select Device > Phone .

The Find and List Phones window opens.

Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of phones.

Select the appropriate phone from the list.

The Phone Configuration window opens.

Locate the Product Specific Configuration Layout section.

Select Enabled from the RTCP drop-down list.

Select Save .

## Configure User
                        	 Associations

When you associate a
                              		  user with a device, you provision that device to the user.

Open the Cisco
                                          				Unified CM Administration interface.

Select User
                                             				  Management > End User .

The Find
                                             				  and List Users window opens.

Specify the
                                       			 appropriate filters in the Find
                                          				User where field and then select Find to retrieve a list of users.

Select the
                                       			 appropriate user from the list.

The End
                                             				  User Configuration window opens.

Locate the Service
                                          				Settings section.

Select Home Cluster .

Select the
                                       			 appropriate service profile for the user from the UC
                                          				Service Profile drop-down list.

Locate the Device
                                          				Information section.

Select Device
                                          				Association .

The User
                                             				  Device Association window opens.

Select the devices to which you want to associate the user. Jabber only supports a single softphone association per device
                                       type. For example, only one TCT, BOT, CSF, and TAB device can be associated with a user.

Select Save
                                          				Selected/Changes .

Select User
                                             				  Management > End User and return to the Find and
                                          				List Users window.

Find and select
                                       			 the same user from the list.

The End
                                             				  User Configuration window opens.

Locate the Permissions Information section.

Select Add to
                                          				Access Control Group .

The Find
                                             				  and List Access Control Groups dialog box opens.

Select the
                                       			 access control groups to which you want to assign the user.

Standard CCM End
                                                      						Users

Standard CTI
                                                      						Enabled

If you are
                                                         					 provisioning users with secure phone capabilities, do not assign the users to
                                                         					 the Standard CTI Secure Connection group.

Cisco
                                                   					 Unified IP Phone 9900, 8900, or 8800 series or DX series, select Standard CTI Allow Control of Phones supporting Connected Xfer
                                                      						and conf .

Cisco
                                                   					 Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover
                                                      						Mode .

Select Add
                                          				Selected .

The Find
                                             				  and List Access Control Groups window closes.

Select Save on the End User
                                          				Configuration window.

## Reset Devices

After you create and associate users with devices, you should reset those devices.

Open the Cisco Unified CM Administration interface.

Select Device > Phone .

The Find and List Phones window opens.

Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices.

Select the appropriate device from the list.

The Phone Configuration window opens.

Locate the Association Information section.

Select the appropriate directory number configuration.

The Directory Number Configuration window opens.

Select Reset .

The Device Reset dialog box opens.

Select Reset .

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

| Note | If users have both wireless and wired connections available, they should configure Microsoft Windows so that wireless connections
                                          do not take priority over wired connections. See the following Microsoft documentation for more information: An explanation of the Automatic Metric feature for Internet Protocol routes . |
|---|---|

| Step 1 | Physically connect the computer to the computer port on the desk phone device. |
|---|---|
| Step 2 | Enable the desk phone device for video in Cisco Unified Communications Manager. |
| Step 3 | Install Jabber Desk Phone Video Services Interface on the computer. |

| Note | RTCP is enabled
                                             				on software phone devices by default. However, you must enable RTCP on desk
                                             				phone devices. |
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
| Step 5 | Locate the Service
                                          				Settings section. |
| Step 6 | Select Home Cluster . |
| Step 7 | Select the
                                       			 appropriate service profile for the user from the UC
                                          				Service Profile drop-down list. |
| Step 8 | Locate the Device
                                          				Information section. |
| Step 9 | Select Device
                                          				Association . The User
                                             				  Device Association window opens. |
| Step 10 | Select the devices to which you want to associate the user. Jabber only supports a single softphone association per device
                                       type. For example, only one TCT, BOT, CSF, and TAB device can be associated with a user. |
| Step 11 | Select Save
                                          				Selected/Changes . |
| Step 12 | Select User
                                             				  Management > End User and return to the Find and
                                          				List Users window. |
| Step 13 | Find and select
                                       			 the same user from the list. The End
                                             				  User Configuration window opens. |
| Step 14 | Locate the Permissions Information section. |
| Step 15 | Select Add to
                                          				Access Control Group . The Find
                                             				  and List Access Control Groups dialog box opens. |
| Step 16 | Select the
                                       			 access control groups to which you want to assign the user. At a minimum you
                                          				should assign the user to the following access control groups: Standard CCM End
                                                      						Users Standard CTI
                                                      						Enabled Remember If you are
                                                         					 provisioning users with secure phone capabilities, do not assign the users to
                                                         					 the Standard CTI Secure Connection group. Certain phone
                                          				models require additional control groups, as follows: Cisco
                                                   					 Unified IP Phone 9900, 8900, or 8800 series or DX series, select Standard CTI Allow Control of Phones supporting Connected Xfer
                                                      						and conf . Cisco
                                                   					 Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover
                                                      						Mode . | Remember | If you are
                                                         					 provisioning users with secure phone capabilities, do not assign the users to
                                                         					 the Standard CTI Secure Connection group. |
| Remember | If you are
                                                         					 provisioning users with secure phone capabilities, do not assign the users to
                                                         					 the Standard CTI Secure Connection group. |
| Step 17 | Select Add
                                          				Selected . The Find
                                             				  and List Access Control Groups window closes. |
| Step 18 | Select Save on the End User
                                          				Configuration window. |

| Remember | If you are
                                                         					 provisioning users with secure phone capabilities, do not assign the users to
                                                         					 the Standard CTI Secure Connection group. |
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