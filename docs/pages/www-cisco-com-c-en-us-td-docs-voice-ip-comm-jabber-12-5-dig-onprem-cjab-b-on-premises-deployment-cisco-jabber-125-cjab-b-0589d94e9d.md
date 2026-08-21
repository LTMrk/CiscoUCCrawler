---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-5-dig-onprem-cjab-b-on-premises-deployment-cisco-jabber-125-cjab-b-0589d94e9d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_5/DIG_OnPrem/cjab_b_on-premises-deployment-cisco-jabber_125/cjab_b_on-premises-deployment-cisco-jabber_125_chapter_01011.html
retrieved_at: 2026-08-21T21:09:40.148029+00:00
---

On-Premises Deployment for Cisco Jabber 12.5

# On-Premises Deployment for Cisco Jabber 12.5

Updated: November 27, 2018

Chapter: Configure Deskphone Control

## Chapter: Configure Deskphone Control

# Configure Deskphone Control

## Prerequisites

The Cisco CTIManager service must be running in the Cisco Unified Communications Manager cluster.

## Configure Desk Phone Control Workflow

Create Desk Phone Devices

Create a desk phone device.

Enable Device for CTI

Allows Cisco Jabber desktop clients to control the desk phone of the user.

Configure Desk Phone Video .

Let users receive video transmitted to their desk phone devices on their computers through the client.

Add Directory Number to the Device for Desktop Applications .

Assign a Directory number to the device.

Enable Video Rate Adaptation

The client uses video rate adaptation to negotiate optimum video quality.

## Create Desk Phone Devices

Users can control desk phones on their computers to place audio calls.

### Before you begin

Create software phone devices.

Open the Cisco Unified CM Administration interface.

Select Device > Phone .

The Find and List Phones window opens.

Select Add New .

Select the appropriate device from the Phone Type drop-down list and then select Next .

The Phone Configuration window opens.

Complete the following steps in the Device Information section:

Enter a meaningful description in the Description field.

The client displays device descriptions to users. If users have multiple devices of the same model, the descriptions help
                                                users tell the difference between multiple devices.

Select Allow Control of Device from CTI .

If you do not select Allow Control of Device from CTI , users cannot control the desk phone.

Set the Owner User ID field to the appropriate user.

On Cisco Unified
                                                            				  Communications Manager version 9.x, the client uses the Owner User ID field to get service profiles for users. For this reason, each user must have a device and the User Owner ID field must be associated with the user.

If you do not associate users with devices and set the Owner User ID field to the appropriate user, the client cannot retrieve the service profile that you apply to the user.

Complete the following steps to enable desk phone video capabilities:

Locate the Product Specific Configuration Layout section.

Select Enabled from the Video Capabilities drop-down list.

If possible, you should enable desk phone video capabilities on the device configuration. However, certain phone models do
                                                            not include the Video Capabilities drop-down list at the device configuration level. In this case, you should open the Common Phone Profile Configuration window and then select Enabled from the Video Calling drop-down list.

See Desk Phone Video Configuration for more information about desk phone video.

Specify all other configuration settings on the Phone Configuration window as appropriate.

See the Cisco Unified
                                             				  Communications Manager documentation for more information about the configuration settings on the Phone Configuration window.

Select Save .

An message displays to inform you if the device is added successfully. The Association Information section becomes available on the Phone Configuration window.

### What to do next

Add a directory number to the device and apply the configuration.

## Enable Device for CTI

If you want Cisco Jabber desktop clients to be able to control the desk phone of the user, you must select the Allow Control of Device from CTI option when you create the device for the user.

In Cisco Unified CM Administration, click Device > Phone and search for the phone.

In the Device Information section, check Allow Control of Device from CTI .

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

Physically connect your
                                       					computer to the computer port on your desk phone.

Enable the desk phone for
                                       					video in Unified CM.

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

## Add Directory Number
                        	 to the Device for Desktop Applications

You must add
                              		  directory numbers to devices in Cisco Unified
                                 				  Communications Manager . This topic provides instructions on
                              		  adding directory numbers using the Device > Phone menu option after you create
                              		  your device. Under this menu option, only the configuration settings that apply
                              		  to the phone model or CTI route point display. See the Cisco Unified
                                 				  Communications Manager documentation for more information
                              		  about different options to configure directory numbers.

Locate the 
                                       			 Association Information section on the Phone
                                          				Configuration window.

Select Add a
                                          				new DN .

Specify a
                                       			 directory number in the Directory Number field.

Specify all
                                       			 other required configuration settings as appropriate.

Associate end
                                       			 users with the directory number as follows:

Locate the Users Associated with Line section.

Select Associate End Users .

Specify the
                                             				  appropriate filters in the Find
                                                					 User where field and then select Find to retrieve a list of users.

Select the
                                             				  appropriate users from the list.

Select Add
                                                					 Selected .

The selected
                                                					 users are added to the voicemail profile.

Select Save .

Select Apply
                                          				Config .

Follow the
                                       			 prompts on the Apply
                                          				Configuration window to apply the configuration.

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

### Before you begin

Create and
                              		  configure Cisco Jabber devices.

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

Locate the Service Settings section.

Select the appropriate service profile for the user from the UC Service Profile drop-down list.

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

At a minimum you should assign the user to the following access control groups:

Standard CCM End Users

Standard CTI Enabled

If you are provisioning users with secure phone capabilities, do not assign the users to the Standard CTI Secure Connection group.

Certain phone models require additional control groups, as follows:

Cisco Unified IP Phone 9900, 8900, or 8800 series or DX series, select Standard CTI Allow Control of Phones supporting Connected Xfer and conf .

Cisco Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover Mode .

Select Add
                                          				Selected .

The Find
                                             				  and List Access Control Groups window closes.

Select Save on the End User
                                          				Configuration window.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create Desk Phone Devices | Create a desk phone device. |
| Step 2 | Enable Device for CTI | Allows Cisco Jabber desktop clients to control the desk phone of the user. |
| Step 3 | Configure Desk Phone Video . | Let users receive video transmitted to their desk phone devices on their computers through the client. |
| Step 4 | Add Directory Number to the Device for Desktop Applications . | Assign a Directory number to the device. |
| Step 5 | Enable Video Rate Adaptation | The client uses video rate adaptation to negotiate optimum video quality. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Select Add New . |
| Step 4 | Select the appropriate device from the Phone Type drop-down list and then select Next . The Phone Configuration window opens. |
| Step 5 | Complete the following steps in the Device Information section: Enter a meaningful description in the Description field. The client displays device descriptions to users. If users have multiple devices of the same model, the descriptions help
                                                users tell the difference between multiple devices. Select Allow Control of Device from CTI . If you do not select Allow Control of Device from CTI , users cannot control the desk phone. |
| Step 6 | Set the Owner User ID field to the appropriate user. Important On Cisco Unified
                                                            				  Communications Manager version 9.x, the client uses the Owner User ID field to get service profiles for users. For this reason, each user must have a device and the User Owner ID field must be associated with the user. If you do not associate users with devices and set the Owner User ID field to the appropriate user, the client cannot retrieve the service profile that you apply to the user. | Important | On Cisco Unified
                                                            				  Communications Manager version 9.x, the client uses the Owner User ID field to get service profiles for users. For this reason, each user must have a device and the User Owner ID field must be associated with the user. If you do not associate users with devices and set the Owner User ID field to the appropriate user, the client cannot retrieve the service profile that you apply to the user. |
| Important | On Cisco Unified
                                                            				  Communications Manager version 9.x, the client uses the Owner User ID field to get service profiles for users. For this reason, each user must have a device and the User Owner ID field must be associated with the user. If you do not associate users with devices and set the Owner User ID field to the appropriate user, the client cannot retrieve the service profile that you apply to the user. |
| Step 7 | Complete the following steps to enable desk phone video capabilities: Locate the Product Specific Configuration Layout section. Select Enabled from the Video Capabilities drop-down list. Note If possible, you should enable desk phone video capabilities on the device configuration. However, certain phone models do
                                                            not include the Video Capabilities drop-down list at the device configuration level. In this case, you should open the Common Phone Profile Configuration window and then select Enabled from the Video Calling drop-down list. See Desk Phone Video Configuration for more information about desk phone video. | Note | If possible, you should enable desk phone video capabilities on the device configuration. However, certain phone models do
                                                            not include the Video Capabilities drop-down list at the device configuration level. In this case, you should open the Common Phone Profile Configuration window and then select Enabled from the Video Calling drop-down list. |
| Note | If possible, you should enable desk phone video capabilities on the device configuration. However, certain phone models do
                                                            not include the Video Capabilities drop-down list at the device configuration level. In this case, you should open the Common Phone Profile Configuration window and then select Enabled from the Video Calling drop-down list. |
| Step 8 | Specify all other configuration settings on the Phone Configuration window as appropriate. See the Cisco Unified
                                             				  Communications Manager documentation for more information about the configuration settings on the Phone Configuration window. |
| Step 9 | Select Save . An message displays to inform you if the device is added successfully. The Association Information section becomes available on the Phone Configuration window. |

| Important | On Cisco Unified
                                                            				  Communications Manager version 9.x, the client uses the Owner User ID field to get service profiles for users. For this reason, each user must have a device and the User Owner ID field must be associated with the user. If you do not associate users with devices and set the Owner User ID field to the appropriate user, the client cannot retrieve the service profile that you apply to the user. |
|---|---|

| Note | If possible, you should enable desk phone video capabilities on the device configuration. However, certain phone models do
                                                            not include the Video Capabilities drop-down list at the device configuration level. In this case, you should open the Common Phone Profile Configuration window and then select Enabled from the Video Calling drop-down list. |
|---|---|

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

| Step 1 | Locate the 
                                       			 Association Information section on the Phone
                                          				Configuration window. |
|---|---|
| Step 2 | Select Add a
                                          				new DN . |
| Step 3 | Specify a
                                       			 directory number in the Directory Number field. |
| Step 4 | Specify all
                                       			 other required configuration settings as appropriate. |
| Step 5 | Associate end
                                       			 users with the directory number as follows: Locate the Users Associated with Line section. Select Associate End Users . Specify the
                                             				  appropriate filters in the Find
                                                					 User where field and then select Find to retrieve a list of users. Select the
                                             				  appropriate users from the list. Select Add
                                                					 Selected . The selected
                                                					 users are added to the voicemail profile. |
| Step 6 | Select Save . |
| Step 7 | Select Apply
                                          				Config . |
| Step 8 | Follow the
                                       			 prompts on the Apply
                                          				Configuration window to apply the configuration. |

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