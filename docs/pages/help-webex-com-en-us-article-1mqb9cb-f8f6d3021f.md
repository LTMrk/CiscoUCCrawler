---
doc_id: help-webex-com-en-us-article-1mqb9cb-f8f6d3021f
source_url: https://help.webex.com/en-us/article/1mqb9cb
retrieved_at: 2026-09-01T21:38:43.179420+00:00
---

## Add a phone to a new workspace

When people are at work, they gather in places such as lunch rooms, lobbies, and conference rooms. You can set up shared Webex devices in these Workspaces, add services, and then watch the collaboration happen.

A workspaces device isn’t assigned to a specific user but to a physical location thus allowing for shared usage.

The devices listed support Webex Calling. You can register most of these devices using a MAC address, and register only the following subset using an activation code:

Cisco IP Phone 6800 Series Multiplatform Phones (Audio phones—6821, 6841, 6851)

Cisco IP Phone 7800 Series Multiplatform Phones (Audio phones—7811, 7821, 7841, 7861)

Cisco IP Phone 8800 Series Multiplatform Phones (Audio phones—8811, 8841, 8851, 8861)

Cisco IP Phone 8800 Series Multiplatform Phones (Video phones—8845, 8865)

Cisco IP Conference Phone 7832 and 8832

Cisco Desk Phone 9800 Series

Before you begin

- You can add up to five Cisco desk phones, Cisco MPP phones, wireless, ATAs, Phone OS, or third-party devices to a Workspace with a professional Workspace license.

- You can add multiple devices to a professional workspace only from the new
                    workspace page. Turn on Try new Workspaces from the upper
                    right corner of the workspace page to use the new workspace page.

- You can add only one device to a Workspace with a common area Workspace license.

Sign in to Control Hub .

Go to Management > Devices > Add device .

You can also add a device to a new Workspace by going to Management > Workspaces > Add workspace .

Choose Shared usage , then click Next .

Choose New workspace , then click Next .

Enter a name for the workspace (such as the name of the physical room), select the room type, add the room capacity, and choose the location of the workspace. Click Next .

A workspace name can't be longer than 128 characters, and can't have %, #, <, >, /, \, and " characters.

Choose the kind of device you want to set up for the workspace:

- Cisco Desk Phone

- Cisco MPP, Wireless, ATA, or third-party
                        device —If you choose this option, choose Cisco
                            Managed Devices from the Select
                            device drop-down menu.

Click the Calling service, and choose the subscription and license type that you want to assign to the workspace.

Professional workspace

Common area workspace

To find out more about the features that are available with the licenses, see Features available by license type for Webex Calling .

Assign a Location and Phone Number (determined by the location that you choose), and then click Save . You also have the option of assigning an extension.

The location is updated during the nightly resync.

A notification appears if you've already added the maximum number of devices to the workspace and you can't proceed further.

The Add Device option is disabled if you've already added the maximum number of devices to the workspace.

To modify or manage the devices assigned to the workspace, see Manage a device for a workspace section.

## Create a workspace and add services for Board, Desk, and Room Series devices

Sign in to Control Hub , then go to Management > Workspaces , and then click Add workspace .

Enter a name for the workspace (such as the name of the physical room), then select the room type and add the capacity. Click Next .

Click Cisco Room and Desk device , then click Next .

You can only have one type of device in a single space. The exception is Companion Mode, where you can have one Board and one Room Series device in a Workspace. It is also possible to add a Room Navigator in standalone mode to a workspace with other devices.

Select the Calling service you want for the workspace.

- None — No calling service. Select this for a standalone Room Navigator, Room USB, or Microsoft Teams Rooms.

- Call on Webex (1:1 call, non-PSTN) (default) — For Webex App and SIP address calling.

For more information about the PSTN options, see PSTN Connectivity in the data sheet .

- Premises calling — Add an on-premises registered device to link it with Webex Edge for Devices .

If you chose Hybrid Calling, enter the Unified CM mail ID for the account that you created earlier. Then download the Device Connector to synchronize the Unified CM configurations to the cloud. Then click Next .

For more information, see the Deployment Guide for Hybrid Calling for Cisco Devices .

(Optional) Go to Scheduling and click Choose
            scheduling Click Save .

Enter or paste the email address of the room device. This is the email address that will be used to schedule meetings:

For devices that will be scheduled in Google Calendar, enter the Google resource email address from G Suites (Calendar > Resources). See About calendar resources (rooms, etc) for more information.

For devices that will be scheduled in Microsoft Exchange or Office 365, enter the email address of the room mailbox. See Create and Manage Room Mailboxes for more information.

This option requires the Hybrid Calendar. To configure the service, see the Deployment Guide for Cisco Webex Hybrid Calendar Service .

- Hot desking — Enable hot desking to allow users to sign in and book any shared Board or Desk Series device with their Webex identity.

This configuration controls whether a user may walk-up sign-in at device

Turn on device-hosted meetings so that people can host Webex meetings on devices , then select the Webex site to use.

Click Next , then activate the device with the code provided.

## Create a workspace and add services for a Webex Share

Before you can use your Webex Share, you associate the device to a physical location.

Sign in to Control Hub , then go to Management > Workspaces and click Add Workspace .

Enter a name for the workspace (such as the name of the physical room), select the room type, and add capacity. Click Next .

Choose Cisco Room and Desk device , then click Next .

You can only have one type of device in a single space. For example, you can add up to 10 desk phones to a lobby or a single Webex Room Device, but not a combination of the two.

Choose Call on Webex (1:1 call, non-PSTN) (default) .
                    Although a call service doesn't apply to Webex Share, select the default to move to the next step.

(Optional) In the Scheduling section, select Calendar to allow people to use One Button to Push (OBTP) on this device, then click Next .

If you selected Calendar , enter or paste the email address of the calendar mailbox for the room device. This is the email address that is used to schedule meetings.

For devices that will be scheduled in Google Calendar, enter the Google resource email address from G Suites (Calendar > Resources). For more information, see What is a Calendar resource? .

For devices that will be scheduled in Microsoft Exchange or Office 365, enter the email address of the room mailbox. For more information, see Create and manage room mailboxes .

Click Next , then activate the device with the code provided.

If you use certificates, deploy the certificate to your Webex Share before activating it.

## Delete a workspace

Sign in to Control Hub , then go to Management > Workspaces .

Check the workspace you want to delete, then select and click Delete .

Confirm the action in the pop-up window.

If you're deleting a workspace assigned an MPP phone, when the workspace is deleted,
              the phone is also deleted and a factory reset is performed on the phone to clear any
              existing configuration. This only applies if the phone is online. If the phone is
              offline or can't be contacted, you should manually factory reset it before reusing it.
              For more information, see Factory reset a Webex Calling phone . After the
              factory reset, the phone returns to its Activation Code screen.

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Management > Devices > Add device . You can also add a device to a new Workspace by going to Management > Workspaces > Add workspace . |
| 3 | Choose Shared usage , then click Next . |
| 4 | Choose New workspace , then click Next . |
| 5 | Enter a name for the workspace (such as the name of the physical room), select the room type, add the room capacity, and choose the location of the workspace. Click Next . A workspace name can't be longer than 128 characters, and can't have %, #, <, >, /, \, and " characters. |
| 6 | Choose the kind of device you want to set up for the workspace: Cisco Desk Phone Cisco MPP, Wireless, ATA, or third-party
                        device —If you choose this option, choose Cisco
                            Managed Devices from the Select
                            device drop-down menu. |
| 7 | Click the Calling service, and choose the subscription and license type that you want to assign to the workspace. Professional workspace Common area workspace To find out more about the features that are available with the licenses, see Features available by license type for Webex Calling . |
| 8 | Assign a Location and Phone Number (determined by the location that you choose), and then click Save . You also have the option of assigning an extension. The location is updated during the nightly resync. If you want to add additional devices to a professional workspace, you can do it in any one of the following ways: Go to Management > Devices > Add device > Shared usage > Existing workspace . From the drop-down, search and select the workspace. A notification appears if you've already added the maximum number of devices to the workspace and you can't proceed further. Go to Management > Workspaces . Then, click under the Actions column of the respective workspace and click Add Device . The Add Device option is disabled if you've already added the maximum number of devices to the workspace. To modify or manage the devices assigned to the workspace, see Manage a device for a workspace section. |

| 1 | Sign in to Control Hub , then go to Management > Workspaces , and then click Add workspace . |
|---|---|
| 2 | Enter a name for the workspace (such as the name of the physical room), then select the room type and add the capacity. Click Next . |
| 3 | Click Cisco Room and Desk device , then click Next . You can only have one type of device in a single space. The exception is Companion Mode, where you can have one Board and one Room Series device in a Workspace. It is also possible to add a Room Navigator in standalone mode to a workspace with other devices. |
| 4 | Select the Calling service you want for the workspace. None — No calling service. Select this for a standalone Room Navigator, Room USB, or Microsoft Teams Rooms. Call on Webex (1:1 call, non-PSTN) (default) — For Webex App and SIP address calling. Cisco Webex Calling — Add PSTN service to the device in the Workspace through the Webex Calling service—depending on your deployment, the PSTN service may come from a local gateway on the premises, through the PSTN the Service Provider bundled, or through a cloud connected PSTN (CCP) provider. Assign a phone number and extension to the device, and then click Next . For more information about the PSTN options, see PSTN Connectivity in the data sheet . Premises calling — Add an on-premises registered device to link it with Webex Edge for Devices . Hybrid Calling (legacy) — To use call service (PSTN access or internal extension access) through your on-premises call control. Unified CM provides the phone number or extension for the devices in the place. If you chose Hybrid Calling, enter the Unified CM mail ID for the account that you created earlier. Then download the Device Connector to synchronize the Unified CM configurations to the cloud. Then click Next . For more information, see the Deployment Guide for Hybrid Calling for Cisco Devices . |
| 5 | (Optional) Go to Scheduling and click Choose
            scheduling Click Save . Calendar — Choose Calendar so that people can use One Button to Push (OBTP) from their devices. Then select calendar service from the drop-down menu and select Resource Group and add Email Address . Enter or paste the email address of the room device. This is the email address that will be used to schedule meetings: For devices that will be scheduled in Google Calendar, enter the Google resource email address from G Suites (Calendar > Resources). See About calendar resources (rooms, etc) for more information. For devices that will be scheduled in Microsoft Exchange or Office 365, enter the email address of the room mailbox. See Create and Manage Room Mailboxes for more information. This option requires the Hybrid Calendar. To configure the service, see the Deployment Guide for Cisco Webex Hybrid Calendar Service . Hot desking — Enable hot desking to allow users to sign in and book any shared Board or Desk Series device with their Webex identity. Ad-hoc booking — Allow users to book the workspace and extend the booking time from the device or enabled peripheral in the workspace. For more information, see Enable room booking for shared mode devices . This configuration controls whether a user may walk-up sign-in at device |
| 6 | Turn on device-hosted meetings so that people can host Webex meetings on devices , then select the Webex site to use. |
| 7 | Click Next , then activate the device with the code provided. |

| 1 | Sign in to Control Hub , then go to Management > Workspaces and click Add Workspace . |
|---|---|
| 2 | Enter a name for the workspace (such as the name of the physical room), select the room type, and add capacity. Click Next . |
| 3 | Choose Cisco Room and Desk device , then click Next . You can only have one type of device in a single space. For example, you can add up to 10 desk phones to a lobby or a single Webex Room Device, but not a combination of the two. |
| 4 | Choose Call on Webex (1:1 call, non-PSTN) (default) .
                    Although a call service doesn't apply to Webex Share, select the default to move to the next step. |
| 5 | (Optional) In the Scheduling section, select Calendar to allow people to use One Button to Push (OBTP) on this device, then click Next . |
| 6 | If you selected Calendar , enter or paste the email address of the calendar mailbox for the room device. This is the email address that is used to schedule meetings. For devices that will be scheduled in Google Calendar, enter the Google resource email address from G Suites (Calendar > Resources). For more information, see What is a Calendar resource? . For devices that will be scheduled in Microsoft Exchange or Office 365, enter the email address of the room mailbox. For more information, see Create and manage room mailboxes . |
| 7 | Click Next , then activate the device with the code provided. If you use certificates, deploy the certificate to your Webex Share before activating it. |

| 1 | Sign in to Control Hub , then go to Management > Workspaces . |
|---|---|
| 2 | Check the workspace you want to delete, then select and click Delete . |
| 3 | Confirm the action in the pop-up window. If you're deleting a workspace assigned an MPP phone, when the workspace is deleted,
              the phone is also deleted and a factory reset is performed on the phone to clear any
              existing configuration. This only applies if the phone is online. If the phone is
              offline or can't be contacted, you should manually factory reset it before reusing it.
              For more information, see Factory reset a Webex Calling phone . After the
              factory reset, the phone returns to its Activation Code screen. |