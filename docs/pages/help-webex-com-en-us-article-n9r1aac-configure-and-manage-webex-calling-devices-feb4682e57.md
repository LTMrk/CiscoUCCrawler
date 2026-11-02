---
doc_id: help-webex-com-en-us-article-n9r1aac-configure-and-manage-webex-calling-devices-feb4682e57
source_url: https://help.webex.com/en-us/article/n9r1aac/Configure-and-manage-Webex-Calling-devices
retrieved_at: 2026-11-02T13:01:50.141386+00:00
---

## Reassigning an existing phone to another user or device

To reuse a phone that is assigned to one Webex Calling user/workspace to another Webex Calling user/workspace, follow these steps:

Sign in to Control Hub .

Go to the User/Workspace where the device is currently assigned.

You can reassign the device in these scenarios:

If you wish to delete the User / Workspace, select Delete User/Workspace to delete both the user/workspace and the associated devices.

If you wish to delete a device, select Devices and choose the device to delete.

On the phone, go to the settings menu and complete these steps to reassign the
                    phone.

Select Device administration , then Factory Reset .

If the device was not factory reset already, only then you must factory reset the device. The device automatically resets, if it was online and active during deletion.

The phone reboots. On completing the reboot, the phone displays the
                            Activation Code screen.

The phone is now ready for reassignment.

Follow instructions in the Add and assign phone to user or Add a phone to a new workspace to
                    assign or add a phone to a user/workspace.

On adding the device in the Control Hub, complete these actions on the phone:

For activation code:

Enter the activation code. The phone reboots and is on-boarded to the
                                new user/workspace.

For MAC address:

Enter #000 on the Activation Code screen, the phone is reonboarded
                                with Webex Calling and provisions to the new user/workspace.

## Add a board, desk, or room device to a user

Assigning a Board, Desk, or Room device as a personal device to someone allows them to get their Webex calls and meetings directly to their device. For more details, see Assign a personal Board, Desk, or Room device to a user .

## Add a board, desk, or room device to a new workspace

When people are at work, they get together in lots of workspaces like lunch rooms, lobbies, and conference rooms. You can set up shared Cisco Webex devices in these Workspaces, add services, and then watch the collaboration happen.

The key principle of a Workspaces device is that it’s not assigned to a specific user, but rather a physical location, allowing for shared usage.

The devices listed here support Webex Calling.

Sign in to Control Hub .

Go to Management > Devices > Add device .

You can also add a device to a new workspace from the Workspaces section by
                    navigation to Management > Workspaces > Add workspace .

Choose Shared usage and click Next .

Choose New workspace and click Next .

Enter a name for the workspace (such as the name of the physical room), select the room type, add the room capacity, and choose the location for the workspace. Then click Next .

Choose Cisco Room and Desk device .

Choose one of the following services and click Next .

- Call on Webex (1:1 call, non-PSTN) —Users can only make Webex App or Webex Session Initiation Protocol (SIP) calls using a SIP address (for example, username@example.calls.webex.com).

- Cisco Webex Calling —In addition to being able to
                        make and receive Webex App and SIP calls, people in this Workspace can use the device to make and
                        receive phone calls from within the Webex Calling numbering plan. For example, you can call your coworker by dialing the
                        phone number 555-555-5555, extension 5555, or SIP address
                        username@example.webex.com but you can also call your local
                        pizzeria.

If you've chosen a Cisco Webex Calling service, then
                    choose the subscription and the license type that you want to assign to the
                    workspace.

Professional workspace

Common area workspace

To find out more about the features that are available with the licenses,
                            see Features available by license type for Webex
                                Calling .

Assign a Location , Phone Number (determined by the location that you choose), an Extension , and then click Save .

Activate the device by using the code provided. You can copy, email, or print the activation code.

## Add and assign devices in bulk

To assign several devices to users and workspaces, you can populate a CSV file with the required information and activate those devices in just a couple of easy steps.

- You can add up to 5 Cisco Desk Phones, Cisco MPP phones, ATAs, or 3rd party devices to a workspace with Professional workspace license.

- You can add only one device to a workspace with a common area workspace
                            license.

The devices listed here support Webex Calling. You can register all devices using a MAC address; however, register the following subset of devices using an activation code:

Cisco IP Phone 6800 Series Multiplatform Phones (Audio phones—6821, 6841, 6851)

Cisco IP Phone 7800 Series Multiplatform Phones (Audio phones—7811, 7821, 7841, 7861)

Cisco IP Phone 8800 Series Multiplatform Phones (Audio phones—8811, 8841, 8851, 8861)

Cisco IP Phone 8800 Series Multiplatform Phones (Video phones—8845, 8865)

Cisco IP Conference Phone 7832 and 8832

Cisco Desk Phone 9800 Series, Cisco Wireless Phone 9821 and Cisco Video Phone 8875

Sign in to Control Hub .

Go to Management > Devices > Add device > Multiple Cisco IP phones .

Choose one of the following options and click Download .

- Users in my organization —You can get a list of all users in your organization and their associated attributes so you don't have to manually look up each user.

If a workspace has multiple devices, only the first device appears in the downloaded CSV. However, you can assign multiple devices to a professional workspace through CSV by adding the details in separate rows.

If you want to see which devices belong to a workspace, you can export the device CSV by navigating to Management > Devices . Then, select one or more devices and click Export to CSV .

- Add device sample template —You can use the available template to enter information such as usernames, type (indicate whether it's a user or a workspace), MAC addresses, and device models.

You can use the following table to prepare your CSV file.

The following fields are mandatory when assigning a device to Webex Calling users and workspaces:

- For Users: Username, Type, Device Type, and Model if the device
                                    type is IP.

- For Workspace: Username, Type, Phone number or Extension, Webex Calling Workspace [subscription name], Device Type, and Model if the
                                    device type is IP.

Username

To assign a device to a user, enter the user's email address.

Don't enter the user ID or their name.

You must add the existing user that belongs to
                                                  the organization.

To assign a device to a workspace, enter the workspace name.

If you enter a workspace that doesn't exist, the
                                                  new workspace is automatically created, but only
                                                  if you specify a Device Type. A new workspace
                                                  can't be created without a device.

Example user email: test@example.com

Example workspace name: Break Room

Type

Enter the appropriate type as user or workspace.

USER

WORKSPACE

Extension

If you've chosen the type as:

USER—The extension must be blank. Don’t enter any value.

WORKSPACE—Enter the extension that’s
                                                  available and valid for the specified
                                                  location.

Example: 00-999999

Phone Number

If you've chosen the type as:

USER—The phone number must be blank. Don’t enter any value.

WORKSPACE—The phone number is mandatory.

Example: +12815550100

Device Type

Enter the type of the device.

To use any Multiplatform Phones, ATA or DECT devices
                                                with Webex Calling, enter IP.

To create new workspaces to have RoomOS devices, enter WEBEX or WEBEX_CALLING, depending on the desired Calling option

Model

Enter the device model if the device type is IP.

Example device model: Cisco 7841, Cisco 8851, and so on

MAC Address

Enter the MAC address of the device.

If you leave the MAC address field blank, an activation code is generated.

Use activation codes for the RoomOS devices.

Example MAC address: 001A2B3C4D5E

Location

Enter the name of the user or workspace location.

Example: San Jose

Calling Plan

Enter TRUE to enable Cisco Calling Plan for the newly added workspace.

The location should be Cisco PSTN.

If the Type is Workspace and the Location is
                                                  a Cisco PSTN location and Calling Plan is set to
                                                  True, then this new Workspace uses Unlimited
                                                  Outbound Calling Plan and is allowed to make
                                                  outbound calls.

By default, the Calling Plan field is set to
                                                  False.

This feature doesn’t work for users, existing workspaces, and workspaces with unsupported location.

TRUE

FALSE

Workspace Subscription Update Only

Enter TRUE if you want to update only the
                                                subscription. This value skips the device onboarding
                                                even if the device related details are filled.

Enter FALSE if you want to update the subscription
                                                and onboard a new device.

By default, the value is set to FALSE.

This column isn’t applicable for Type USER. If
                                                  you've chosen the Type as USER, and entered this
                                                  column value as TRUE, you get an error.

This column isn’t applicable and will be
                                                  ignored when creating a new workspace.

TRUE

FALSE

Webex Calling Workspace [subscription ID]

Specify the subscription to be used for creating
                                                common-area or professional calling workspaces.

Each subscription possessing workspace license has a
                                                corresponding column. You can assign either a common
                                                area workspace license or a professional workspace
                                                license. To assign a license, enter TRUE in any one
                                                of the license type columns of the respective
                                                subscription.

You must assign only one subscription for a workspace.

You can also transfer workspaces from one subscription to another. To transfer, enter FALSE in the source subscription column and TRUE in the target subscription column.

Subscriptions that are suspended have “suspended”
                                                mentioned in their title. You receive an error if
                                                you assign a suspended subscription to a workspace.
                                                To update the workspace from suspended to active
                                                subscription, enter FALSE in the suspended
                                                subscription column, and TRUE in the active
                                                subscription column.

We recommend using a recently generated template to prepare the CSV import file, as it will contain accurate information regarding the active subscriptions for workspace licenses.

TRUE

FALSE

Webex Calling Professional Workspace [subscription ID]

These Phone Number and Extension fields were previously titled Directory Number and Direct Line ; these column names continue to support for a short time.

We recommend that you limit the number of devices to 1000 per CSV file. If you want to add more than 1000 devices, use a second CSV file.

Fill out the spreadsheet.

Upload the CSV file by dragging and dropping or clicking Choose a file .

If the MAC address is blank, you get the options to choose where the activation code gets sent.

- Provide a link —The activation code gets added to a CSV file. After import, you’ll get a link to download the activation code file on the Import Status screen.

- Email activation code —If the device is for a workspace, the activation code gets sent to you, as the administrator. If the device is for a user, the activation code is emailed to the user.

You or the user need to enter the activation code on the device for activating it.

Click Submit .

Multiplatform devices must be running a firmware load of 11.3.1 SR2 or later for users to enter the activation code on their device. For information about upgrading phone firmware, see this article.

## Export a device list

If you want to view the list of devices assigned to users and workspaces, you can export the CSV file.

Sign in to Control Hub and go to Devices .

Select multiple devices from the device list and select the Export option. You can choose the fields to include in the CSV file, and export the content to a local folder.

The fields displayed on the CSV file depend on the connection of the device to the platform. Therefore, some fields aren’t available in the output file.

## Manage a device for a user

You can add, remove, reboot, check activation, or create a new activation code for
                the devices that are assigned to users within your organization. This can be helpful
                to view and manage devices in the users screen, when needed.

Sign in to Control Hub .

Go to Management > Users .

Select a user and click Devices .

To add a device to this user, click Add Device .

If the user is already assigned a device and you want to add another device, click Action > Add device .

For more information on adding the device to a user, see Add phones to a user section.

To modify an existing device, select the device name.

This takes you to the Devices page. Here you can view and edit device settings, delete the device, reboot the device, or create a new activation code for the device, if applicable. For more information about configuring phone settings, see Configure and Update Phone Settings .

If the device added to the user is Webex Aware, then the Webex Aware option is
                    displayed under the devices as shown in the diagram. Webex Aware indicates that
                    the device has onboarded to the Webex platform and has access to Webex Features
                    supported by the phone.

Click Actions to manage the device. Actions enables you to apply configuration changes, reboot the device, Report a problem and collect device logs, or delete the device.

The Actions tab has these options for a Webex Aware-enabled device:

- Apply Changes—Issues request to the phone to download and apply changes to the configuration.

- Reboot—Issues request to force reboot the device and download the current configuration.

- Report Problem—Issues request to the device to generate and upload a PRT to the cloud.

## Manage a device for a workspace

You can add and manage devices directly from a workspace profile. Workspace devices
                can include ATA devices, like fax machines. You can also set up a workspace device
                as a Hoteling Host. For more information about hoteling, see Hoteling in Control Hub .

Sign in to Control Hub .

Go to Management > Workspaces .

Select the workspace to modify.

To add a device, click Add Device in the Devices tile.

For more information on adding devices to workspace, see Add a phone to a new workspace section.

To modify an existing device, select the device name.

This takes you to the Devices page. Here you can view and edit device settings, delete the device, reboot the device, and enable the device to be used as a Hoteling Host. For more information about configuring phone settings, see Configure and Update Phone Settings .

If the device added to the workspace is Webex Aware, then the Webex Aware
                    option is displayed under the devices as shown in the diagram. Webex Aware
                    indicates that the device has onboarded to the Webex platform and has access to
                    Webex features that are supported by the phone.

Click Actions to manage the device. Actions help to
                    apply configuration changes or update firmware for the MPP devices.

The Actions tab has these options for a Webex Aware-enabled device:

- Apply Changes—Issues request to the phone to download and apply changes to the configuration.

- Reboot—Issues request to force reboot the device and download the current configuration.

- Report Problem—Issues request to the device to generate and upload a PRT to the cloud.

## Configure lines - Add and reorder lines

The Configure Lines feature for assigning primary, shared, and virtual lines to phones allows multiple appearances of a shared line on the same device. The Configure Ports experience for ATAs in not changed.

Here are the updates for the Configure Lines feature for MPP and PhoneOS devices:

Primary Lines

Assign the owner of the device and ensure it occupies the first
                                    line position on the device.

Increase the Appearances on that row to add additional
                                    appearances.

Shared Lines / Virtual Lines

Assign shared lines from any Calling-enabled user or workspace
                                    within the organization with available Shared Call Appearances
                                    (SCAs).

Increase the Appearances on the shared line row to add additional
                                        appearances.

The SCA limits available for the user or workspace may
                                            limit the assignable appearances.

Assign a Line Index to each shared line. You can rearrange the
                                    shared lines through drag-and-drop.

You can't separate the individual appearances of a
                                            line.

Use the user’s Configure Layouts > Custom Layout mode to arrange the position of shared line indexes on
                                    a device.

Appearances

Configure multiple appearances of the same primary, shared, or
                                    virtual Line as individual weighted line sets.

Weighted lines are suffixed with a -1, -2, and so on (Cisco
                                    phones only).

Calls ring into the first available weighted line appearance.

New summary information (at the bottom of the page)

Unique SIP Registering Lines – Shows the number of unique SIP
                                    registering accounts that the phone can support. The maximum
                                    number of accounts currently supported is 16.

Total Lines Appearances – Shows the total number of assignable
                                    line appearances supported by the device. If the phone model
                                    supports KEMs, the maximum number of appearances includes the
                                    expanded capacity.

Bulk Line Assignment and Public APIs

- The Bulk CSV and Public API methods for assigning lines include the
                                “Appearances” functionality.

For more information on shared line across locations, see Configuration of shared lines and virtual lines across locations .

When a speed dial is added to a phone using a long press on the desired line key, the speed dial is not visible in Control Hub. A Speed dial can be overwritten by configuring a shared line on that line key.

Sign in to Control Hub .

Go to Users or Workspaces (depending on where the device to modify is assigned).

Select a user or workspace.

Go to Devices and click a device for which you want to
                    add or modify the shared lines.

This takes you to the Devices page.

Under Device Management , click Configure
                        Lines .

To add a shared line appearance, click the icon, search by name or phone number, and choose a
                    line.

You can assign the same shared line or virtual line to multiple individual
                        line keys on a phone. In the Appearances column of
                        the respective line, click the icon to set the number of appearances of the
                        line you want to display on the phone.

You can add the lines in the order in which you want them to appear. To
                        reorder the line appearance, delete and add to the list in the order you
                        want them to appear.

If a user has numbers from other users/groups configured on their devices,
                        you can add a Line label for the shared line. This
                        line label helps to identify one shared line appearance from the other.

To remove a line, click the icon. You can't remove the primary user on line
                        1.

Click Save .

For large organizations, the administrator must select a location before
                        configuring additional calling lines.

click the icon, and you can see the location filter
                        appears. The administrator then can select the desire location and select a
                            line.

For a regular organization, the location filter is not available, and the
                        administrator can select a line.

## Configure an ATA device for a user

You can configure the ports on an Analog Telephone Adapter (ATA) device assigned to a
                user in Control Hub. Currently, the two configurations for ATA devices available are for devices with
                two ports and devices with 24 ports.

Sign in to Control Hub .

Go to Management > Users .

Select a user to modify and scroll to Devices .

Select a device where you want to add or modify.

Under Users on this Device , click Configure Ports .

To add a shared port configuration, click the icon.

Enter the name or phone number and select from the options that appear and then click Save .

Only workspaces without devices appear in the lookup.

If the device requires T.38 fax compression, check the box in the T.38 column or override the user-level compression options, and then click Save .

A workspace can have an ATA. This is useful for fax machines.

## Add numbers to your location

You can add phone numbers to desk and room devices in your customer organization at any time, whether you're in the middle of a trial or have been converted to a paid subscription.

We've increased the number of telephone numbers that you can add in Control Hub from 250 to 1000.

Sign in to Control Hub .

Go to Services > Calling > Numbers , and then click Add Numbers .

Specify the Location and Number Type . If you're porting numbers over, enter both your current and new billing numbers.

Specify the Location , State , Area Code , Prefix (optional), and then click Search .

Available numbers are displayed.

Select the numbers that you want to add to the location.

The numbers you choose move over to the Selected Numbers field.

Click Save .

## Check the status of ordered PSTN numbers

You can see a list of PSTN numbers that your organization has ordered. With this
        information, you can see the unused numbers that are available, and the numbers that have
        been ordered that will soon become available.

Sign in to Control Hub .

Go to Services > Calling > PSTN Orders .

## Multiplatform Phone (MPP) connected accessories—Headsets and Key Expansion Modules (KEMs)

When you connect accessories (Headsets/KEMs) to an MPP device, they appear as an inventory item under the Devices tab in the Control Hub. From the Control Hub Devices inventory you can find out the accessory model, the status, and to whom the accessory belongs. When you select an accessory, additional information can be obtained, such as the accessory serial number and current software version. The accessory status field is reported as "online" as long as the accessory is connected to MPP. An MPP-connected headset will automatically upgrade its software with the latest version available from Device Management.

Phone Model

Cisco Headset 520 Series

Cisco Headset 530 Series

Cisco Headset 560 Series

Cisco Headset 730 Series

Cisco IP Phone 8811/8841/8845

—

—

RJ9 & RJ11

—

Cisco IP Phone 8851/8861/8865

USB

USB

USB

RJ9 & RJ11

—

Cisco IP Phone 7811/7821/7841/7861

—

—

—

—

Cisco IP Phone 6821/6841/6851/6861

—

—

—

—

Cisco IP Phone 6871

USB

USB

USB

—

Cisco IP Conference Phone 7832/8832

—

—

—

—

Phone Model

KEM

Cisco IP Phone 8811/8841/8845

—

Cisco IP Phone 8851/8861/8865

BEKEM

CP-8800-A-KEM

CP-8800-V-KEM

Cisco IP Phone 7811/7821/7841/7861

—

Cisco IP Phone 6821/6841/6861/6871

—

Cisco IP Phone 6851

CP-68KEM-3PCC

Cisco IP Conference Phone 7832/8832

—

To troubleshoot the issues faced with Key Expansion Module (key expansion module) on phones registered to Webex Calling, see Troubleshoot Key Expansion Modules Issues in Webex Calling for details.

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to the User/Workspace where the device is currently assigned. You can reassign the device in these scenarios: If you wish to delete the User / Workspace, select Delete User/Workspace to delete both the user/workspace and the associated devices. If you wish to delete a device, select Devices and choose the device to delete. |
| 3 | On the phone, go to the settings menu and complete these steps to reassign the
                    phone. Select Device administration , then Factory Reset . If the device was not factory reset already, only then you must factory reset the device. The device automatically resets, if it was online and active during deletion. The phone reboots. On completing the reboot, the phone displays the
                            Activation Code screen. The phone is now ready for reassignment. |
| 4 | Follow instructions in the Add and assign phone to user or Add a phone to a new workspace to
                    assign or add a phone to a user/workspace. |
| 5 | On adding the device in the Control Hub, complete these actions on the phone: For activation code: Enter the activation code. The phone reboots and is on-boarded to the
                                new user/workspace. For MAC address: Enter #000 on the Activation Code screen, the phone is reonboarded
                                with Webex Calling and provisions to the new user/workspace. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Management > Devices > Add device . You can also add a device to a new workspace from the Workspaces section by
                    navigation to Management > Workspaces > Add workspace . |
| 3 | Choose Shared usage and click Next . |
| 4 | Choose New workspace and click Next . |
| 5 | Enter a name for the workspace (such as the name of the physical room), select the room type, add the room capacity, and choose the location for the workspace. Then click Next . |
| 6 | Choose Cisco Room and Desk device . |
| 7 | Choose one of the following services and click Next . Call on Webex (1:1 call, non-PSTN) —Users can only make Webex App or Webex Session Initiation Protocol (SIP) calls using a SIP address (for example, username@example.calls.webex.com). Cisco Webex Calling —In addition to being able to
                        make and receive Webex App and SIP calls, people in this Workspace can use the device to make and
                        receive phone calls from within the Webex Calling numbering plan. For example, you can call your coworker by dialing the
                        phone number 555-555-5555, extension 5555, or SIP address
                        username@example.webex.com but you can also call your local
                        pizzeria. |
| 8 | If you've chosen a Cisco Webex Calling service, then
                    choose the subscription and the license type that you want to assign to the
                    workspace. Professional workspace Common area workspace To find out more about the features that are available with the licenses,
                            see Features available by license type for Webex
                                Calling . |
| 9 | Assign a Location , Phone Number (determined by the location that you choose), an Extension , and then click Save . |
| 10 | Activate the device by using the code provided. You can copy, email, or print the activation code. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Management > Devices > Add device > Multiple Cisco IP phones . |
| 3 | Choose one of the following options and click Download . Users in my organization —You can get a list of all users in your organization and their associated attributes so you don't have to manually look up each user. Workspaces in my organization —You can get a list of all workspaces in your organization and their associated attributes so you don't have to manually look up each workspace. If a workspace has multiple devices, only the first device appears in the downloaded CSV. However, you can assign multiple devices to a professional workspace through CSV by adding the details in separate rows. If you want to see which devices belong to a workspace, you can export the device CSV by navigating to Management > Devices . Then, select one or more devices and click Export to CSV . Add device sample template —You can use the available template to enter information such as usernames, type (indicate whether it's a user or a workspace), MAC addresses, and device models. You can use the following table to prepare your CSV file. The following fields are mandatory when assigning a device to Webex Calling users and workspaces: For Users: Username, Type, Device Type, and Model if the device
                                    type is IP. For Workspace: Username, Type, Phone number or Extension, Webex Calling Workspace [subscription name], Device Type, and Model if the
                                    device type is IP. Column Name Description Supported Value Username To assign a device to a user, enter the user's email address. Don't enter the user ID or their name. You must add the existing user that belongs to
                                                  the organization. To assign a device to a workspace, enter the workspace name. If you enter a workspace that doesn't exist, the
                                                  new workspace is automatically created, but only
                                                  if you specify a Device Type. A new workspace
                                                  can't be created without a device. Example user email: test@example.com Example workspace name: Break Room Type Enter the appropriate type as user or workspace. USER WORKSPACE Extension If you've chosen the type as: USER—The extension must be blank. Don’t enter any value. WORKSPACE—Enter the extension that’s
                                                  available and valid for the specified
                                                  location. Example: 00-999999 Phone Number If you've chosen the type as: USER—The phone number must be blank. Don’t enter any value. WORKSPACE—The phone number is mandatory. Example: +12815550100 Device Type Enter the type of the device. To use any Multiplatform Phones, ATA or DECT devices
                                                with Webex Calling, enter IP. To create new workspaces to have RoomOS devices, enter WEBEX or WEBEX_CALLING, depending on the desired Calling option Model Enter the device model if the device type is IP. Example device model: Cisco 7841, Cisco 8851, and so on MAC Address Enter the MAC address of the device. If you leave the MAC address field blank, an activation code is generated. Use activation codes for the RoomOS devices. Example MAC address: 001A2B3C4D5E Location Enter the name of the user or workspace location. Example: San Jose Calling Plan Enter TRUE to enable Cisco Calling Plan for the newly added workspace. The location should be Cisco PSTN. If the Type is Workspace and the Location is
                                                  a Cisco PSTN location and Calling Plan is set to
                                                  True, then this new Workspace uses Unlimited
                                                  Outbound Calling Plan and is allowed to make
                                                  outbound calls. By default, the Calling Plan field is set to
                                                  False. This feature doesn’t work for users, existing workspaces, and workspaces with unsupported location. TRUE FALSE Workspace Subscription Update Only Enter TRUE if you want to update only the
                                                subscription. This value skips the device onboarding
                                                even if the device related details are filled. Enter FALSE if you want to update the subscription
                                                and onboard a new device. By default, the value is set to FALSE. This column isn’t applicable for Type USER. If
                                                  you've chosen the Type as USER, and entered this
                                                  column value as TRUE, you get an error. This column isn’t applicable and will be
                                                  ignored when creating a new workspace. TRUE FALSE Webex Calling Workspace [subscription ID] Specify the subscription to be used for creating
                                                common-area or professional calling workspaces. Each subscription possessing workspace license has a
                                                corresponding column. You can assign either a common
                                                area workspace license or a professional workspace
                                                license. To assign a license, enter TRUE in any one
                                                of the license type columns of the respective
                                                subscription. You must assign only one subscription for a workspace. You can also transfer workspaces from one subscription to another. To transfer, enter FALSE in the source subscription column and TRUE in the target subscription column. Subscriptions that are suspended have “suspended”
                                                mentioned in their title. You receive an error if
                                                you assign a suspended subscription to a workspace.
                                                To update the workspace from suspended to active
                                                subscription, enter FALSE in the suspended
                                                subscription column, and TRUE in the active
                                                subscription column. We recommend using a recently generated template to prepare the CSV import file, as it will contain accurate information regarding the active subscriptions for workspace licenses. TRUE FALSE Webex Calling Professional Workspace [subscription ID] These Phone Number and Extension fields were previously titled Directory Number and Direct Line ; these column names continue to support for a short time. We recommend that you limit the number of devices to 1000 per CSV file. If you want to add more than 1000 devices, use a second CSV file. | Column Name | Description | Supported Value | Username | To assign a device to a user, enter the user's email address. Don't enter the user ID or their name. You must add the existing user that belongs to
                                                  the organization. To assign a device to a workspace, enter the workspace name. If you enter a workspace that doesn't exist, the
                                                  new workspace is automatically created, but only
                                                  if you specify a Device Type. A new workspace
                                                  can't be created without a device. | Example user email: test@example.com Example workspace name: Break Room | Type | Enter the appropriate type as user or workspace. | USER WORKSPACE | Extension | If you've chosen the type as: USER—The extension must be blank. Don’t enter any value. WORKSPACE—Enter the extension that’s
                                                  available and valid for the specified
                                                  location. | Example: 00-999999 | Phone Number | If you've chosen the type as: USER—The phone number must be blank. Don’t enter any value. WORKSPACE—The phone number is mandatory. | Example: +12815550100 | Device Type | Enter the type of the device. | To use any Multiplatform Phones, ATA or DECT devices
                                                with Webex Calling, enter IP. To create new workspaces to have RoomOS devices, enter WEBEX or WEBEX_CALLING, depending on the desired Calling option | Model | Enter the device model if the device type is IP. | Example device model: Cisco 7841, Cisco 8851, and so on | MAC Address | Enter the MAC address of the device. If you leave the MAC address field blank, an activation code is generated. Use activation codes for the RoomOS devices. | Example MAC address: 001A2B3C4D5E | Location | Enter the name of the user or workspace location. | Example: San Jose | Calling Plan | Enter TRUE to enable Cisco Calling Plan for the newly added workspace. The location should be Cisco PSTN. If the Type is Workspace and the Location is
                                                  a Cisco PSTN location and Calling Plan is set to
                                                  True, then this new Workspace uses Unlimited
                                                  Outbound Calling Plan and is allowed to make
                                                  outbound calls. By default, the Calling Plan field is set to
                                                  False. This feature doesn’t work for users, existing workspaces, and workspaces with unsupported location. | TRUE FALSE | Workspace Subscription Update Only | Enter TRUE if you want to update only the
                                                subscription. This value skips the device onboarding
                                                even if the device related details are filled. Enter FALSE if you want to update the subscription
                                                and onboard a new device. By default, the value is set to FALSE. This column isn’t applicable for Type USER. If
                                                  you've chosen the Type as USER, and entered this
                                                  column value as TRUE, you get an error. This column isn’t applicable and will be
                                                  ignored when creating a new workspace. | TRUE FALSE | Webex Calling Workspace [subscription ID] | Specify the subscription to be used for creating
                                                common-area or professional calling workspaces. Each subscription possessing workspace license has a
                                                corresponding column. You can assign either a common
                                                area workspace license or a professional workspace
                                                license. To assign a license, enter TRUE in any one
                                                of the license type columns of the respective
                                                subscription. You must assign only one subscription for a workspace. You can also transfer workspaces from one subscription to another. To transfer, enter FALSE in the source subscription column and TRUE in the target subscription column. Subscriptions that are suspended have “suspended”
                                                mentioned in their title. You receive an error if
                                                you assign a suspended subscription to a workspace.
                                                To update the workspace from suspended to active
                                                subscription, enter FALSE in the suspended
                                                subscription column, and TRUE in the active
                                                subscription column. We recommend using a recently generated template to prepare the CSV import file, as it will contain accurate information regarding the active subscriptions for workspace licenses. | TRUE FALSE | Webex Calling Professional Workspace [subscription ID] |
| Column Name | Description | Supported Value |
| Username | To assign a device to a user, enter the user's email address. Don't enter the user ID or their name. You must add the existing user that belongs to
                                                  the organization. To assign a device to a workspace, enter the workspace name. If you enter a workspace that doesn't exist, the
                                                  new workspace is automatically created, but only
                                                  if you specify a Device Type. A new workspace
                                                  can't be created without a device. | Example user email: test@example.com Example workspace name: Break Room |
| Type | Enter the appropriate type as user or workspace. | USER WORKSPACE |
| Extension | If you've chosen the type as: USER—The extension must be blank. Don’t enter any value. WORKSPACE—Enter the extension that’s
                                                  available and valid for the specified
                                                  location. | Example: 00-999999 |
| Phone Number | If you've chosen the type as: USER—The phone number must be blank. Don’t enter any value. WORKSPACE—The phone number is mandatory. | Example: +12815550100 |
| Device Type | Enter the type of the device. | To use any Multiplatform Phones, ATA or DECT devices
                                                with Webex Calling, enter IP. To create new workspaces to have RoomOS devices, enter WEBEX or WEBEX_CALLING, depending on the desired Calling option |
| Model | Enter the device model if the device type is IP. | Example device model: Cisco 7841, Cisco 8851, and so on |
| MAC Address | Enter the MAC address of the device. If you leave the MAC address field blank, an activation code is generated. Use activation codes for the RoomOS devices. | Example MAC address: 001A2B3C4D5E |
| Location | Enter the name of the user or workspace location. | Example: San Jose |
| Calling Plan | Enter TRUE to enable Cisco Calling Plan for the newly added workspace. The location should be Cisco PSTN. If the Type is Workspace and the Location is
                                                  a Cisco PSTN location and Calling Plan is set to
                                                  True, then this new Workspace uses Unlimited
                                                  Outbound Calling Plan and is allowed to make
                                                  outbound calls. By default, the Calling Plan field is set to
                                                  False. This feature doesn’t work for users, existing workspaces, and workspaces with unsupported location. | TRUE FALSE |
| Workspace Subscription Update Only | Enter TRUE if you want to update only the
                                                subscription. This value skips the device onboarding
                                                even if the device related details are filled. Enter FALSE if you want to update the subscription
                                                and onboard a new device. By default, the value is set to FALSE. This column isn’t applicable for Type USER. If
                                                  you've chosen the Type as USER, and entered this
                                                  column value as TRUE, you get an error. This column isn’t applicable and will be
                                                  ignored when creating a new workspace. | TRUE FALSE |
| Webex Calling Workspace [subscription ID] | Specify the subscription to be used for creating
                                                common-area or professional calling workspaces. Each subscription possessing workspace license has a
                                                corresponding column. You can assign either a common
                                                area workspace license or a professional workspace
                                                license. To assign a license, enter TRUE in any one
                                                of the license type columns of the respective
                                                subscription. You must assign only one subscription for a workspace. You can also transfer workspaces from one subscription to another. To transfer, enter FALSE in the source subscription column and TRUE in the target subscription column. Subscriptions that are suspended have “suspended”
                                                mentioned in their title. You receive an error if
                                                you assign a suspended subscription to a workspace.
                                                To update the workspace from suspended to active
                                                subscription, enter FALSE in the suspended
                                                subscription column, and TRUE in the active
                                                subscription column. We recommend using a recently generated template to prepare the CSV import file, as it will contain accurate information regarding the active subscriptions for workspace licenses. | TRUE FALSE |
| Webex Calling Professional Workspace [subscription ID] |
| 4 | Fill out the spreadsheet. |
| 5 | Upload the CSV file by dragging and dropping or clicking Choose a file . |
| 6 | If the MAC address is blank, you get the options to choose where the activation code gets sent. Provide a link —The activation code gets added to a CSV file. After import, you’ll get a link to download the activation code file on the Import Status screen. Email activation code —If the device is for a workspace, the activation code gets sent to you, as the administrator. If the device is for a user, the activation code is emailed to the user. You or the user need to enter the activation code on the device for activating it. |
| 7 | Click Submit . Displays the updated status when the devices become active. Multiplatform devices must be running a firmware load of 11.3.1 SR2 or later for users to enter the activation code on their device. For information about upgrading phone firmware, see this article. |

| Column Name | Description | Supported Value |
|---|---|---|
| Username | To assign a device to a user, enter the user's email address. Don't enter the user ID or their name. You must add the existing user that belongs to
                                                  the organization. To assign a device to a workspace, enter the workspace name. If you enter a workspace that doesn't exist, the
                                                  new workspace is automatically created, but only
                                                  if you specify a Device Type. A new workspace
                                                  can't be created without a device. | Example user email: test@example.com Example workspace name: Break Room |
| Type | Enter the appropriate type as user or workspace. | USER WORKSPACE |
| Extension | If you've chosen the type as: USER—The extension must be blank. Don’t enter any value. WORKSPACE—Enter the extension that’s
                                                  available and valid for the specified
                                                  location. | Example: 00-999999 |
| Phone Number | If you've chosen the type as: USER—The phone number must be blank. Don’t enter any value. WORKSPACE—The phone number is mandatory. | Example: +12815550100 |
| Device Type | Enter the type of the device. | To use any Multiplatform Phones, ATA or DECT devices
                                                with Webex Calling, enter IP. To create new workspaces to have RoomOS devices, enter WEBEX or WEBEX_CALLING, depending on the desired Calling option |
| Model | Enter the device model if the device type is IP. | Example device model: Cisco 7841, Cisco 8851, and so on |
| MAC Address | Enter the MAC address of the device. If you leave the MAC address field blank, an activation code is generated. Use activation codes for the RoomOS devices. | Example MAC address: 001A2B3C4D5E |
| Location | Enter the name of the user or workspace location. | Example: San Jose |
| Calling Plan | Enter TRUE to enable Cisco Calling Plan for the newly added workspace. The location should be Cisco PSTN. If the Type is Workspace and the Location is
                                                  a Cisco PSTN location and Calling Plan is set to
                                                  True, then this new Workspace uses Unlimited
                                                  Outbound Calling Plan and is allowed to make
                                                  outbound calls. By default, the Calling Plan field is set to
                                                  False. This feature doesn’t work for users, existing workspaces, and workspaces with unsupported location. | TRUE FALSE |
| Workspace Subscription Update Only | Enter TRUE if you want to update only the
                                                subscription. This value skips the device onboarding
                                                even if the device related details are filled. Enter FALSE if you want to update the subscription
                                                and onboard a new device. By default, the value is set to FALSE. This column isn’t applicable for Type USER. If
                                                  you've chosen the Type as USER, and entered this
                                                  column value as TRUE, you get an error. This column isn’t applicable and will be
                                                  ignored when creating a new workspace. | TRUE FALSE |
| Webex Calling Workspace [subscription ID] | Specify the subscription to be used for creating
                                                common-area or professional calling workspaces. Each subscription possessing workspace license has a
                                                corresponding column. You can assign either a common
                                                area workspace license or a professional workspace
                                                license. To assign a license, enter TRUE in any one
                                                of the license type columns of the respective
                                                subscription. You must assign only one subscription for a workspace. You can also transfer workspaces from one subscription to another. To transfer, enter FALSE in the source subscription column and TRUE in the target subscription column. Subscriptions that are suspended have “suspended”
                                                mentioned in their title. You receive an error if
                                                you assign a suspended subscription to a workspace.
                                                To update the workspace from suspended to active
                                                subscription, enter FALSE in the suspended
                                                subscription column, and TRUE in the active
                                                subscription column. We recommend using a recently generated template to prepare the CSV import file, as it will contain accurate information regarding the active subscriptions for workspace licenses. | TRUE FALSE |
| Webex Calling Professional Workspace [subscription ID] |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Management > Users . |
| 3 | Select a user and click Devices . |
| 4 | To add a device to this user, click Add Device . If the user is already assigned a device and you want to add another device, click Action > Add device . For more information on adding the device to a user, see Add phones to a user section. |
| 5 | To modify an existing device, select the device name. This takes you to the Devices page. Here you can view and edit device settings, delete the device, reboot the device, or create a new activation code for the device, if applicable. For more information about configuring phone settings, see Configure and Update Phone Settings . |
| 6 | If the device added to the user is Webex Aware, then the Webex Aware option is
                    displayed under the devices as shown in the diagram. Webex Aware indicates that
                    the device has onboarded to the Webex platform and has access to Webex Features
                    supported by the phone. |
| 7 | Click Actions to manage the device. Actions enables you to apply configuration changes, reboot the device, Report a problem and collect device logs, or delete the device. The Actions tab has these options for a Webex Aware-enabled device: Apply Changes—Issues request to the phone to download and apply changes to the configuration. Reboot—Issues request to force reboot the device and download the current configuration. Report Problem—Issues request to the device to generate and upload a PRT to the cloud. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Management > Workspaces . |
| 3 | Select the workspace to modify. |
| 4 | To add a device, click Add Device in the Devices tile. For more information on adding devices to workspace, see Add a phone to a new workspace section. |
| 5 | To modify an existing device, select the device name. This takes you to the Devices page. Here you can view and edit device settings, delete the device, reboot the device, and enable the device to be used as a Hoteling Host. For more information about configuring phone settings, see Configure and Update Phone Settings . |
| 6 | If the device added to the workspace is Webex Aware, then the Webex Aware
                    option is displayed under the devices as shown in the diagram. Webex Aware
                    indicates that the device has onboarded to the Webex platform and has access to
                    Webex features that are supported by the phone. |
| 7 | Click Actions to manage the device. Actions help to
                    apply configuration changes or update firmware for the MPP devices. The Actions tab has these options for a Webex Aware-enabled device: Apply Changes—Issues request to the phone to download and apply changes to the configuration. Reboot—Issues request to force reboot the device and download the current configuration. Report Problem—Issues request to the device to generate and upload a PRT to the cloud. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Users or Workspaces (depending on where the device to modify is assigned). |
| 3 | Select a user or workspace. |
| 4 | Go to Devices and click a device for which you want to
                    add or modify the shared lines. This takes you to the Devices page. |
| 5 | Under Device Management , click Configure
                        Lines . |
| 6 | To add a shared line appearance, click the icon, search by name or phone number, and choose a
                    line. You can assign the same shared line or virtual line to multiple individual
                        line keys on a phone. In the Appearances column of
                        the respective line, click the icon to set the number of appearances of the
                        line you want to display on the phone. You can add the lines in the order in which you want them to appear. To
                        reorder the line appearance, delete and add to the list in the order you
                        want them to appear. If a user has numbers from other users/groups configured on their devices,
                        you can add a Line label for the shared line. This
                        line label helps to identify one shared line appearance from the other. To remove a line, click the icon. You can't remove the primary user on line
                        1. |
| 7 | Click Save . For large organizations, the administrator must select a location before
                        configuring additional calling lines. click the icon, and you can see the location filter
                        appears. The administrator then can select the desire location and select a
                            line. For a regular organization, the location filter is not available, and the
                        administrator can select a line. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Management > Users . |
| 3 | Select a user to modify and scroll to Devices . |
| 4 | Select a device where you want to add or modify. |
| 5 | Under Users on this Device , click Configure Ports . |
| 6 | To add a shared port configuration, click the icon. |
| 7 | Enter the name or phone number and select from the options that appear and then click Save . Only workspaces without devices appear in the lookup. |
| 8 | If the device requires T.38 fax compression, check the box in the T.38 column or override the user-level compression options, and then click Save . A workspace can have an ATA. This is useful for fax machines. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Services > Calling > Numbers , and then click Add Numbers . |
| 3 | Specify the Location and Number Type . If you're porting numbers over, enter both your current and new billing numbers. |
| 4 | Specify the Location , State , Area Code , Prefix (optional), and then click Search . Available numbers are displayed. |
| 5 | Select the numbers that you want to add to the location. The numbers you choose move over to the Selected Numbers field. |
| 6 | Click Save . |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Services > Calling > PSTN Orders . |

| Phone Model | Cisco Headset 520 Series | Cisco Headset 530 Series | Cisco Headset 560 Series | Cisco Headset 730 Series |
|---|---|---|---|---|
| Cisco IP Phone 8811/8841/8845 | — | — | RJ9 & RJ11 | — |
| Cisco IP Phone 8851/8861/8865 | USB | USB | USB RJ9 & RJ11 | — |
| Cisco IP Phone 7811/7821/7841/7861 | — | — | — | — |
| Cisco IP Phone 6821/6841/6851/6861 | — | — | — | — |
| Cisco IP Phone 6871 | USB | USB | USB | — |
| Cisco IP Conference Phone 7832/8832 | — | — | — | — |

| Phone Model | KEM |
|---|---|
| Cisco IP Phone 8811/8841/8845 | — |
| Cisco IP Phone 8851/8861/8865 | BEKEM CP-8800-A-KEM CP-8800-V-KEM |
| Cisco IP Phone 7811/7821/7841/7861 | — |
| Cisco IP Phone 6821/6841/6861/6871 | — |
| Cisco IP Phone 6851 | CP-68KEM-3PCC |
| Cisco IP Conference Phone 7832/8832 | — |

## Figuras

![Device information page showing device status and SIP registration status](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/465001-466000/465877.png)

![Plus or Add icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/410001-420000/417001-418000/417379.jpg)

![Configure line page where admin can add shared lines and its appearances](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488057.jpg)

![Delete button represented by a trash bin icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/446001-447000/446495.jpg)

![Location filter for large orgs](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/494001-495000/494671.png)

![Add icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/451001-452000/451513.jpg)