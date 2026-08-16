---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14su2-cucm-b-feature-configuration-guide-for-cisco14su2-cucm-m-he-177ebc24fa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14SU2/cucm_b_feature-configuration-guide-for-cisco14su2/cucm_m_headset-services.html
retrieved_at: 2026-08-16T16:25:49.090311+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: May 7, 2026

Chapter: Headset Services

## Chapter: Headset Services

# Headset Services

## Headset Services Overview

Headset Services allow you to connect the Cisco Headset into its supported Devices to provide simple and integrated user experiences
                           such as Headset-based Extension Mobility and many more in the future.

Headset-based Extension Mobility is the first feature introduced under the Headset Services. When you connect your Cisco headset
                           to Extension Mobility enabled devices, it provides a seamless login experience for extension mobility log in and log out.

Headset Services allow the administrator and end user to associate headset(s) from any devices such as a self-owned device,
                           shared space, and common area device. This association helps in authentications and creating a customized experience for its
                           users. This feature supports both wired and wireless headsets.

Headset association assigns the user’s identity to the headset. You can log in to the services that need user identity.

The Unified Communications Manager interface allows the administrator to:

Associate and disassociate headset to end users along with serial numbers.

Enable Headset-based Extension Mobility.

Import and export bulk users to headsets association.

Headset-based Extension Mobility login is not supported for Extension Mobility Cross Cluster (EMCC).

Headset-based Extension Mobility login works for devices supporting Mobile and Remote Access (MRA). The compatible Phone Firmware
                                       version is 14.1(1).

Headset-based Extension Mobility login does not work if the same user ID is controlling both the Headset and the Phone.

## Headset Services Prerequisites

Make sure that end users are already created in the Unified Communications Manager .

For Extension Mobility login using the headset, ensure that Extension Mobility is enabled in the user device. And also, Allow headset for Extension Mobility sign in and sign out option is enabled so that the user can perform Extension Mobility log in or log out using Cisco headset.

Headset-based Extension Mobility feature supports only the latest firmware of 88XX and 78XX series Cisco IP Phones.

## Headset Services Administrator Configuration Task Flow

The administrator can use the following task to associate headset to users and enable Headset-based Extension Mobility.

Step 1

Headset Association to a User

Specifies how to associate and dissociate the serial number with a user.

Step 2

Manage End User Headset Association

Optional : Allows the end users to create a headset association for the devices.

Step 3

Enable Headset-based Extension Mobility

Enables Extension Mobility for headsets from the Unified Communications Manager .

Step 4

Enable Pinless Extension Mobility Login

Enables pinless Extension Mobility login.

Step 5

Configure Extension Mobility Headset Logout Timer

Configures automatic logout timeout settings for headsets.

### Headset Association to a User

Use this procedure to associate the headset with a user.

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Click Find and choose an existing user to whom you want to associate the headset.

Step 3

In the Associated Headsets section, enter the serial number of the headset that you want to assign.

Step 4

Click Save .

Step 5

Click (+) if you want to associate more headsets to the selected user.

You can associate a maximum of only 15 headsets to a specific user. The headset serial number is unique for every individual
                                                         headset. The same headset can’t be associated with two users. To move the headset association to a different user, you must
                                                         first disassociate the headset from the first user.

For information on how to locate the Serial Number for a specific headset, refer to the Headset Administration Guide for that headset model.

Step 6

(Optional) Click (-) to dissociate the headset serial number for the selected user.

Step 7

Click View Details link to view the inventory details of a headset. For more information, see the Headset Inventory Settings section in the
                                          'Headset and Accessories Management' chapter to view the headset details.

### Manage End User Headset Association

Optional : Use this procedure to configure settings in the Unified Communication Manager to enable end users to associate headset using the Headset Association menu option on the device screen.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

In the Enterprise Parameters Configuration section, choose one of the following to associate the end user headset to the device:

- Choose Prompt user to initiate Headset Association from all devices to display the Headset Association screen when the headset is connected to the device for the first time. By default, this parameter value is selected.

- Choose Prompt user to initiate Headset association only from Extension Mobility-enabled devices for the Headset Association screen to only appear in the Extension Mobility enabled devices.

- Choose Do not prompt user to initiate Headset association from all devices to disable Headset Association screen on all devices. This setting doesn’t prevent the user from initiating headset association manually from the device
                                             menu.

Any changes in the settings is not applicable to the headsets that are already associated with the end user.

Step 3

Click Save and Apply Config for the configuration changes to take effect.

Tip

Click the parameter name or the question mark (?) icon in the Enterprise Parameter Configuration window for detailed descriptions.

### Enable Headset-based Extension Mobility

Use this procedure to allow users to log in to Extension mobility from associated headsets.

#### Before you begin

Ensure that you configure Cisco IP Phones and device profiles to the extension mobility service that headset users can log
                                 in, use, and log out of Extension Mobility using a headset. For more information, see Subscribe to Extension Mobility .

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server field, choose the node running the Cisco Extension Mobility service.

Step 3

From the Service field, choose Cisco Extension Mobility .

Step 4

In the Headset-based Extension Mobility field, choose one of the following to use an associated headset for extension mobility login:

- Choose Allow headset for Extension Mobility sign in and sign out to allow the headset user to sign in with extension mobility. By default, this parameter value is selected.

- Choose Do not Allow headset for Extension Mobility sign in and sign out to restrict the headset user to sign in with Extension Mobility. If you choose this option, end users don't see the Extension
                                             Mobility login or logout screen when they connect their headsets.

Step 5

Click Save .

### Enable Pinless Extension Mobility Login

Use this procedure for pinless Extension Mobility login using a headset associated with a user.

This feature is supported from release 12.5(1)SU3 onwards.

#### Before you begin

The specified maximum duration takes effect only when PIN entry for headset-based sign in field is set to Not Required .

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server field, choose the node running the Cisco Extension Mobility service.

Step 3

From the Service field, choose Cisco Extension Mobility .

Step 4

In the PIN entry for headset-based sign in field, choose one of the following to enable or disable pinless Extension Mobility login:

- Choose Required to prompt the user to enter a PIN for Extension Mobility login. By default, this parameter value is selected.

Important

When the user automatically signs out within the set time or manually logged out using wired or wireless headset, we recommend
                                                            the user to click Cancel to avoid automatic sign-in within the specified duration.

Step 5

Click Save .

### Configure Extension Mobility Headset Logout Timer

Use this procedure to configure the auto-logout timeout settings.

If the Headset-based Extension Mobility service parameter in Service Parameter Configuration window is set to Do not Allow headset for Extension Mobility sign in and sign out , then configuring auto-logout timer value has no effect.

Step 1

From Cisco Unified CM Administration, choose Service > Service Parameters .

Step 2

From the Server field, choose the node running the Cisco Extension Mobility service.

Step 3

From the Service field, choose Cisco Extension Mobility .

Step 4

In the Auto logout timer after headset disconnect field, enter the maximum duration value that the system can wait for user input when the headset is disconnected from the
                                          device before automatically logging out the user.

By default, the value is set for 5 minutes. You can set the maximum value to 15 minutes.

Step 5

Click Save .

## Headset Services End User Association Task Flow

The end user can use the following task to associate the headset and use the associated identity to login using Extension
                              Mobility.

Step 1

Associate a User Headset

Creates a headset association to the end user.

Step 2

Skip Headset Association

Allows skipping the headset association for the particular end user.

Step 3

Extension Mobility Login Using Headset

Enables customized experience to use an associated headset for Extension Mobility login.

Step 4

Logout User from Extension Mobility Using Headset

Helps to logout the headset from Extension Mobility within the default set time.

### Associate a User Headset

Use this procedure to assign the headset to a user.

Step 1

Connect the headset to the Cisco IP Phone.

The Associate headset to user popup screen appears on the IP Phone screen.

The Username is automatically populated if the device is in a shared space or common area or user is associated with the device.
                                             If the device is anonymous, the User ID field is blank and any end user can associate the headset providing the user credentials.

Step 2

Enter or modify User ID and PIN . Contact the administrator if you don’t know the credentials.

Step 3

Click Submit .

Successful associating of headset message is displayed along with the Username.

If you enter invalid credentials ( User ID or PIN ) more than three times, the Cisco IP Phone displays an error message.

If the headset association fails, you can disconnect and connect in the headset to provide valid credentials or contact the
                                             administrator.

Step 4

(Optional) To associate headset manually through Cisco IP Phone, choose Settings > Accessories > Cisco Headset Setup > Associate User .

The Associate User option is greyed out if the headset is disconnected. To enable, connect in the headset to the device.

### Skip Headset Association

Use this procedure to skip associating the headset to a user.

Step 1

Connect the headset to the Cisco IP Phone.

Step 2

Click Exit before associating the headset to a user.

Step 3

Click Yes if you don't want to associate the headset.

### Extension Mobility Login Using Headset

Use this procedure to log in with Extension Mobility using a headset that has a user associated.

Step 1

Connect the headset to the Cisco IP Phone.

Step 2

If the headset isn’t associated, perform the following:

Enter the User ID and PIN to associate the headset with the user.

Click Submit .

The login screen displays a success message with the associated User ID and allows the user to sign in with Extension Mobility.

Click Sign In to complete the Extension Mobility login.

Step 3

If the headset is already associated with the user, perform the following:

Enter the PIN to login with Extension Mobility.

Select the required user profile.

Click Submit .

Step 4

If a user is already logged in to Extension Mobility on the device and another user plugs in a previously associated headset,
                                          the logout screen appears and allows the user to sign out previously logged in user.

Step 5

Click Yes to log out of the earlier profile.

Step 6

Enter the PIN to login with Extension Mobility.

Step 7

Click Submit .

The phone resets each time the device profile changes, and the user profile is changed to the original profile.

### Logout User from Extension Mobility Using Headset

Use this procedure to sign out the headset from the Extension Mobility enabled device.

Step 1

Disconnect the headset from the Cisco IP Phone.

Step 2

Click Sign Out .

The phone resets and the device profile is changed to the original device profile.

If you disconnect the headset during an ongoing call (one to one call or conference call), the call is not terminated, and
                                                         the Extension Mobility sign out occurs only when the call ends.

You are automatically signed out within the set time if you haven’t manually logged out or go out of range for a wireless
                                                         headset. By default, the set time is 5 minutes. For more information, see the Configure Extension Mobility Headset Logout Timer section.

Step 3

Click Cancel if you want to retain the current Extension Mobility session. Reconnect within the default set time to retain the user profile
                                          and avoid a reset.

| Note | Headset-based Extension Mobility login is not supported for Extension Mobility Cross Cluster (EMCC). Headset-based Extension Mobility login works for devices supporting Mobile and Remote Access (MRA). The compatible Phone Firmware
                                       version is 14.1(1). Headset-based Extension Mobility login does not work if the same user ID is controlling both the Headset and the Phone. |
|---|---|

| Note | Headset-based Extension Mobility feature supports only the latest firmware of 88XX and 78XX series Cisco IP Phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Headset Association to a User | Specifies how to associate and dissociate the serial number with a user. |
| Step 2 | Manage End User Headset Association | Optional : Allows the end users to create a headset association for the devices. |
| Step 3 | Enable Headset-based Extension Mobility | Enables Extension Mobility for headsets from the Unified Communications Manager . |
| Step 4 | Enable Pinless Extension Mobility Login | Enables pinless Extension Mobility login. |
| Step 5 | Configure Extension Mobility Headset Logout Timer | Configures automatic logout timeout settings for headsets. |

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Click Find and choose an existing user to whom you want to associate the headset. |
| Step 3 | In the Associated Headsets section, enter the serial number of the headset that you want to assign. |
| Step 4 | Click Save . |
| Step 5 | Click (+) if you want to associate more headsets to the selected user. Note You can associate a maximum of only 15 headsets to a specific user. The headset serial number is unique for every individual
                                                         headset. The same headset can’t be associated with two users. To move the headset association to a different user, you must
                                                         first disassociate the headset from the first user. For information on how to locate the Serial Number for a specific headset, refer to the Headset Administration Guide for that headset model. | Note | You can associate a maximum of only 15 headsets to a specific user. The headset serial number is unique for every individual
                                                         headset. The same headset can’t be associated with two users. To move the headset association to a different user, you must
                                                         first disassociate the headset from the first user. For information on how to locate the Serial Number for a specific headset, refer to the Headset Administration Guide for that headset model. |
| Note | You can associate a maximum of only 15 headsets to a specific user. The headset serial number is unique for every individual
                                                         headset. The same headset can’t be associated with two users. To move the headset association to a different user, you must
                                                         first disassociate the headset from the first user. For information on how to locate the Serial Number for a specific headset, refer to the Headset Administration Guide for that headset model. |
| Step 6 | (Optional) Click (-) to dissociate the headset serial number for the selected user. |
| Step 7 | Click View Details link to view the inventory details of a headset. For more information, see the Headset Inventory Settings section in the
                                          'Headset and Accessories Management' chapter to view the headset details. |

| Note | You can associate a maximum of only 15 headsets to a specific user. The headset serial number is unique for every individual
                                                         headset. The same headset can’t be associated with two users. To move the headset association to a different user, you must
                                                         first disassociate the headset from the first user. For information on how to locate the Serial Number for a specific headset, refer to the Headset Administration Guide for that headset model. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | In the Enterprise Parameters Configuration section, choose one of the following to associate the end user headset to the device: Choose Prompt user to initiate Headset Association from all devices to display the Headset Association screen when the headset is connected to the device for the first time. By default, this parameter value is selected. Choose Prompt user to initiate Headset association only from Extension Mobility-enabled devices for the Headset Association screen to only appear in the Extension Mobility enabled devices. Choose Do not prompt user to initiate Headset association from all devices to disable Headset Association screen on all devices. This setting doesn’t prevent the user from initiating headset association manually from the device
                                             menu. Note Any changes in the settings is not applicable to the headsets that are already associated with the end user. | Note | Any changes in the settings is not applicable to the headsets that are already associated with the end user. |
| Note | Any changes in the settings is not applicable to the headsets that are already associated with the end user. |
| Step 3 | Click Save and Apply Config for the configuration changes to take effect. Tip Click the parameter name or the question mark (?) icon in the Enterprise Parameter Configuration window for detailed descriptions. | Tip | Click the parameter name or the question mark (?) icon in the Enterprise Parameter Configuration window for detailed descriptions. |
| Tip | Click the parameter name or the question mark (?) icon in the Enterprise Parameter Configuration window for detailed descriptions. |

| Note | Any changes in the settings is not applicable to the headsets that are already associated with the end user. |
|---|---|

| Tip | Click the parameter name or the question mark (?) icon in the Enterprise Parameter Configuration window for detailed descriptions. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server field, choose the node running the Cisco Extension Mobility service. |
| Step 3 | From the Service field, choose Cisco Extension Mobility . |
| Step 4 | In the Headset-based Extension Mobility field, choose one of the following to use an associated headset for extension mobility login: Choose Allow headset for Extension Mobility sign in and sign out to allow the headset user to sign in with extension mobility. By default, this parameter value is selected. Choose Do not Allow headset for Extension Mobility sign in and sign out to restrict the headset user to sign in with Extension Mobility. If you choose this option, end users don't see the Extension
                                             Mobility login or logout screen when they connect their headsets. |
| Step 5 | Click Save . |

| Note | This feature is supported from release 12.5(1)SU3 onwards. |
|---|---|

| Note | The specified maximum duration takes effect only when PIN entry for headset-based sign in field is set to Not Required . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server field, choose the node running the Cisco Extension Mobility service. |
| Step 3 | From the Service field, choose Cisco Extension Mobility . |
| Step 4 | In the PIN entry for headset-based sign in field, choose one of the following to enable or disable pinless Extension Mobility login: Choose Required to prompt the user to enter a PIN for Extension Mobility login. By default, this parameter value is selected. Choose Not Required to automatically sign in the user within a minute to Extension Mobility. The user isn’t prompted to enter PIN details on
                                             the Phone UI. Important When the user automatically signs out within the set time or manually logged out using wired or wireless headset, we recommend
                                                            the user to click Cancel to avoid automatic sign-in within the specified duration. | Important | When the user automatically signs out within the set time or manually logged out using wired or wireless headset, we recommend
                                                            the user to click Cancel to avoid automatic sign-in within the specified duration. |
| Important | When the user automatically signs out within the set time or manually logged out using wired or wireless headset, we recommend
                                                            the user to click Cancel to avoid automatic sign-in within the specified duration. |
| Step 5 | Click Save . |

| Important | When the user automatically signs out within the set time or manually logged out using wired or wireless headset, we recommend
                                                            the user to click Cancel to avoid automatic sign-in within the specified duration. |
|---|---|

| Note | If the Headset-based Extension Mobility service parameter in Service Parameter Configuration window is set to Do not Allow headset for Extension Mobility sign in and sign out , then configuring auto-logout timer value has no effect. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Service > Service Parameters . |
|---|---|
| Step 2 | From the Server field, choose the node running the Cisco Extension Mobility service. |
| Step 3 | From the Service field, choose Cisco Extension Mobility . |
| Step 4 | In the Auto logout timer after headset disconnect field, enter the maximum duration value that the system can wait for user input when the headset is disconnected from the
                                          device before automatically logging out the user. Note By default, the value is set for 5 minutes. You can set the maximum value to 15 minutes. | Note | By default, the value is set for 5 minutes. You can set the maximum value to 15 minutes. |
| Note | By default, the value is set for 5 minutes. You can set the maximum value to 15 minutes. |
| Step 5 | Click Save . |

| Note | By default, the value is set for 5 minutes. You can set the maximum value to 15 minutes. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Associate a User Headset | Creates a headset association to the end user. |
| Step 2 | Skip Headset Association | Allows skipping the headset association for the particular end user. |
| Step 3 | Extension Mobility Login Using Headset | Enables customized experience to use an associated headset for Extension Mobility login. |
| Step 4 | Logout User from Extension Mobility Using Headset | Helps to logout the headset from Extension Mobility within the default set time. |

| Step 1 | Connect the headset to the Cisco IP Phone. The Associate headset to user popup screen appears on the IP Phone screen. The Username is automatically populated if the device is in a shared space or common area or user is associated with the device.
                                             If the device is anonymous, the User ID field is blank and any end user can associate the headset providing the user credentials. |
|---|---|
| Step 2 | Enter or modify User ID and PIN . Contact the administrator if you don’t know the credentials. |
| Step 3 | Click Submit . Successful associating of headset message is displayed along with the Username. If you enter invalid credentials ( User ID or PIN ) more than three times, the Cisco IP Phone displays an error message. If the headset association fails, you can disconnect and connect in the headset to provide valid credentials or contact the
                                             administrator. |
| Step 4 | (Optional) To associate headset manually through Cisco IP Phone, choose Settings > Accessories > Cisco Headset Setup > Associate User . Note The Associate User option is greyed out if the headset is disconnected. To enable, connect in the headset to the device. | Note | The Associate User option is greyed out if the headset is disconnected. To enable, connect in the headset to the device. |
| Note | The Associate User option is greyed out if the headset is disconnected. To enable, connect in the headset to the device. |

| Note | The Associate User option is greyed out if the headset is disconnected. To enable, connect in the headset to the device. |
|---|---|

| Step 1 | Connect the headset to the Cisco IP Phone. |
|---|---|
| Step 2 | Click Exit before associating the headset to a user. |
| Step 3 | Click Yes if you don't want to associate the headset. The headset association screen isn’t prompted on any further connections to the device. If the same headset is connected to
                                          another device, the Associate Headset to User popup screen appears on the Cisco IP Phone screen and navigates you through the association process. |

| Step 1 | Connect the headset to the Cisco IP Phone. |
|---|---|
| Step 2 | If the headset isn’t associated, perform the following: Enter the User ID and PIN to associate the headset with the user. Click Submit . The login screen displays a success message with the associated User ID and allows the user to sign in with Extension Mobility. Click Sign In to complete the Extension Mobility login. |
| Step 3 | If the headset is already associated with the user, perform the following: Enter the PIN to login with Extension Mobility. Select the required user profile. Click Submit . |
| Step 4 | If a user is already logged in to Extension Mobility on the device and another user plugs in a previously associated headset,
                                          the logout screen appears and allows the user to sign out previously logged in user. |
| Step 5 | Click Yes to log out of the earlier profile. |
| Step 6 | Enter the PIN to login with Extension Mobility. |
| Step 7 | Click Submit . Note The phone resets each time the device profile changes, and the user profile is changed to the original profile. | Note | The phone resets each time the device profile changes, and the user profile is changed to the original profile. |
| Note | The phone resets each time the device profile changes, and the user profile is changed to the original profile. |

| Note | The phone resets each time the device profile changes, and the user profile is changed to the original profile. |
|---|---|

| Step 1 | Disconnect the headset from the Cisco IP Phone. |
|---|---|
| Step 2 | Click Sign Out . Note The phone resets and the device profile is changed to the original device profile. If you disconnect the headset during an ongoing call (one to one call or conference call), the call is not terminated, and
                                                         the Extension Mobility sign out occurs only when the call ends. You are automatically signed out within the set time if you haven’t manually logged out or go out of range for a wireless
                                                         headset. By default, the set time is 5 minutes. For more information, see the Configure Extension Mobility Headset Logout Timer section. | Note | The phone resets and the device profile is changed to the original device profile. If you disconnect the headset during an ongoing call (one to one call or conference call), the call is not terminated, and
                                                         the Extension Mobility sign out occurs only when the call ends. You are automatically signed out within the set time if you haven’t manually logged out or go out of range for a wireless
                                                         headset. By default, the set time is 5 minutes. For more information, see the Configure Extension Mobility Headset Logout Timer section. |
| Note | The phone resets and the device profile is changed to the original device profile. If you disconnect the headset during an ongoing call (one to one call or conference call), the call is not terminated, and
                                                         the Extension Mobility sign out occurs only when the call ends. You are automatically signed out within the set time if you haven’t manually logged out or go out of range for a wireless
                                                         headset. By default, the set time is 5 minutes. For more information, see the Configure Extension Mobility Headset Logout Timer section. |
| Step 3 | Click Cancel if you want to retain the current Extension Mobility session. Reconnect within the default set time to retain the user profile
                                          and avoid a reset. |

| Note | The phone resets and the device profile is changed to the original device profile. If you disconnect the headset during an ongoing call (one to one call or conference call), the call is not terminated, and
                                                         the Extension Mobility sign out occurs only when the call ends. You are automatically signed out within the set time if you haven’t manually logged out or go out of range for a wireless
                                                         headset. By default, the set time is 5 minutes. For more information, see the Configure Extension Mobility Headset Logout Timer section. |
|---|---|