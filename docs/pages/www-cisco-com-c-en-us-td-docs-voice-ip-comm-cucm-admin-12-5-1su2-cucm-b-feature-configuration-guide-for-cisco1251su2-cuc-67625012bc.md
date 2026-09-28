---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-cucm-b-feature-configuration-guide-for-cisco1251su2-cuc-67625012bc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2/cucm_m_native-phone-migration-using-ivr.html
retrieved_at: 2026-08-16T17:15:33.175970+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Native Phone Migration Using IVR

## Chapter: Native Phone Migration Using IVR

# Native Phone Migration Using IVR

## Phone Replacement or Migration Using Self-Provisioning Overview

Use the Self-provisioning IVR service in Unified Communications Manager to directly migrate or replace a faulty desk phone
                           or old phones for which support has ended without the need to contact the administrator. This feature makes it simple to replace
                           phones while minimizing costs at the same time.

Migration using self-provisioning in Unified Communications Manager minimizes the initial configuration requirement while
                           migrating the existing phone settings to the new phone. You can choose to delete or retain the old phones in Unified Communications
                           Manager when provisioning a phone for migration or replacement.

Using Self-provisioning IVR, you can migrate or replace the phone under the primary extension of the authenticated user.

Phone users authenticate to the IVR using their user PIN. Administrators can authenticate using a specified authentication
                                       code.

You can also migrate phones using the Cisco Unified Communications Manager Administrative Interface. See Migrate Phones using Cisco Unified CM Administration Interface .

## Phone Migration Prerequisites

Before your end users can use self-provisioning for migration or replacement purpose, the following should be configured:

Enable Auto-registration.

End users must have a primary extension. Ensure that the primary DN is always Line1 on the phone or device.

End users must be associated to a user profile or feature group template that includes a universal line template, universal
                                 device template and which has Self-Provisioning enabled.

Ensure that the right “CTI Route Point” and “Application User” configurations are selected.

Enable Self-Provisioning IVR service.

For more information on self-provisioning, see the ‘Configure Self-Provisioning’ section in the System Configuration Guide for Cisco Unified Communications Manager .

## Phone Migration Task Flow Using Self-Provisioning IVR

After you complete this workflow, you can configure Self-Provisioning IVR service, migrate old or faulty Cisco IP Phones,
                              and track the migrated phones list.

Step 1

Activate Services for Self-Provisioning

Activate the Self-Provisioning IVR and CTI Manager services in Cisco Unified Serviceability.

Step 2

Enable Autoregistration for Self-Provisioning

Enable autoregistration parameter for self-provisioning.

Step 3

Configure CTI Route Point

Configure a CTI route point to handle the self-provisioning IVR service.

Step 4

Assign a Directory Number to the CTI Route Point

Configure the extension that users dial in order to access the self-provisioning IVR and associate that extension to the CTI
                                          route point.

Step 5

Configure Application User for Self-Provisioning

Configure an application user for the self-provisioning IVR. Associate the CTI route point to the application user.

Step 6

Configure the System for Self-Provisioning

Configure Self-Provisioning system settings.

Step 7

Enable Self-Provisioning in a User Profile

Enables the users to Self-Provision phones in the user profile to which they are assigned.

Step 8

Migrate phones using any of these procedures:

- Migrate Phones Using Self-Provisioning IVR (Administrator)

- Migrate Phones Using Self-Provisioning IVR (Phone Users)

Choose the migration procedure that applies for you. The Self-Provisioning IVR can be used by either administrators or phone
                                          users to migrate phones.

Step 9

View Phone Migration Report

Following the migration, view a report that shows Cisco IP Phones that are migrated.

### Activate Services for Self-Provisioning

Use this procedure to activate the services that support the Self-Provisioning feature. Ensure that both the Self-Provisioning
                                 IVR and Cisco CTI Manager services are running.

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

From the Server drop-down list, select the publisher node and click Go .

Step 3

Under CM Services , check Cisco CTI Manager .

Step 4

Under CTI Services , check Self Provisioning IVR .

Step 5

Click Save .

### Enable Autoregistration for Self-Provisioning

Use this procedure for self-provisioning, you must configure the auto-registration parameters on the publisher.

Step 1

In Cisco Unified CM Administration, choose System > Cisco Unified CM .

Step 2

Click on the publisher node.

Step 3

Select the Universal Device Template that you want to be applied to provisioned phones.

Step 4

Select the Universal Line Template that you want to be applied to the phone lines for provisioned phones.

Step 5

Use the Starting Directory Number and Ending Directory Number fields to enter a range of directory numbers to apply to provisioned phones.

Step 6

Uncheck the Auto-registration Disabled on the Cisco Unified Communications Manager check box.

Step 7

Confirm the ports that will be used for SIP registrations. In most cases, there is no need to change the ports from their
                                          default settings.

Step 8

Click Save .

### Configure CTI Route Point

Us this procedure to configure a CTI Route Point for the Self-Provisioning IVR.

Step 1

From Cisco Unified CM Administration, choose, Device > CTI Route Points .

Step 2

Complete either of the following steps:

Click Find and select an existing CTI route point.

Click Add New to create a new CTI route point.

Step 3

In the Device Name field, enter a unique name to identify the route point.

Step 4

From the Device Pool drop-down list, select the device pool that specifies the properties for this device.

Step 5

From the Location drop-down list, select the appropriate location for this CTI route point.

Step 6

From the Use Trusted Relay Point drop-down list, enable or disable whether Unified Communications Manager inserts a trusted relay point (TRP) device with
                                          this media endpoint. The default setting is to use the Common Device Configuration setting that is associated to this device.

Step 7

Complete the remaining fields in the CTI Route Point Configuration window. For more information on the fields and their settings, see the online help.

Step 8

Click Save .

### Assign a Directory Number to the CTI Route Point

Use this procedure to set up the extension that users will dial in to access the self-provisioning IVR. You must associate
                                 this extension to the CTI route point that you want to use for self-provisioning.

Step 1

From Cisco Unified CM Administration, choose Device > CTI Route Point .

Step 2

Click Find and select the CTI route point that you set up for self-provisioning.

Step 3

Under Association click Line [1] - Add a new DN .

Step 4

In the Directory Number field, enter the extension that you want users to dial to access the Self-Provisioning IVR service.

Step 5

Click Save .

Step 6

Complete the remaining fields in the Directory Number Configuration window. For more information with the fields and their settings, see the online help.

Step 7

Click Save .

### Configure Application User for Self-Provisioning

You must set up an application user for the self-provisioning IVR and associate the CTI route point that you created to the
                                 application user.

Step 1

From Cisco Unified CM Administration, choose User > Application User .

Step 2

Perform either of the following steps:

To select an existing application user, click Find and select the application user.

To create a new application user, click Add New .

Step 3

In the User ID text box, enter a unique ID for the application user.

Step 4

Select a BLF Presence Group for the application user.

Step 5

Associate the CTI route point that you created to the application user by performing the following steps:

If the CTI route point that you created  does not appear in the Available Devices list box, click Find More Route Points .

In the Available Devices list, select the CTI route point that you created for self-provisioning and click the down arrow.

Step 6

Complete the remaining fields in the Application User Configuration window. For help with the fields and their settings, see the online help.

Step 7

Click Save .

### Configure the
                           	 System for Self-Provisioning

Use this procedure to configure your system for self-provisioning. Self-provisioning provides users in your network with the
                                 ability to add their own desk phone through an IVR system, without contacting an administrator.

Step 1

From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Self-Provisioning .

Step 2

Configure
                                          			 whether you want the self-provisioning IVR to authenticate end users by
                                          			 clicking one of the following radio buttons:

- Require
                                                				  Authentication —In order to use the self-provisioning IVR, end users
                                             				must enter their password, PIN, or a system authentication code.

- No Authentication
                                                				  Required —End users can access the self-provisioning IVR without
                                             				authenticating.

Step 3

If the
                                          			 self-provisioning IVR is configured to require authentication, click one of the
                                          			 following radio buttons to configure the method whereby the IVR authenticates
                                          			 end users:

- Allow authentication for end users only —End users must enter their password or PIN.

- Allow authentication for
                                                				  users (via Password/PIN) and Administrators (via Authentication
                                                				  Code) —End Users must enter an authentication code. If you choose
                                             				this option, configure the authentication code by entering an integer between 0
                                             				and 20 digits in the Authentication Code text box.

Step 4

In the IVR
                                             				Settings list boxes, use the arrows to select the Language that you
                                          			 prefer to use for IVR prompts. The list of available languages depends on the
                                          			 language packs that you have installed on your system. Refer to the Downloads
                                          			 section of cisco.com if you want to download additional language packs.

Step 5

From the CTI Route Points drop-down list, choose the CTI route point that you have configured for your self-provisioning IVR.

Step 6

From the Application User drop-down list, choose the application user that you have configured for self-provisioning.

Step 7

Click Save .

### Enable Self-Provisioning in a User Profile

In order for users to be able to Self-Provision phones, the feature must be enabled in the user profile to which they are
                                 assigned.

If you don’t know which user profile your users are using, you can open a user’s settings in the End User Configuration window
                                             and view the User Profile field to get the correct profile.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > User Profile .

Step 2

Click Find and select the user profile to which the user is assigned.

Step 3

Assign Universal Line Templates and Universal Device Templates to the user profile.

Step 4

Configure user settings for Self-Provisioning:

- Check the Allow End User to Provision their own phones check box.

- Enter a limit for the number of phones a user can provision. The default is 10.

- If you want users to be able to use self-provisioning to reassign a previously assigned phone, check the Allow Provisioning of a phone that is already assigned to a different End User setting in the user profile page associated with the end user of old device. Users can reassign a previously assigned phone
                                             only if this check box is enabled in the User Profile that is associated to the old device.

Step 5

Click Save .

## Phone Migration Tasks

After self-provisioning Authentication is setup, use any of the following procedures to migrate phones.

### Migrate Phones Using Self-Provisioning IVR (Phone Users)

Phone users can use this procedure to migrate to a new Cisco IP Phone.

#### Before you begin

Make sure that the old phone is in the "Unregistered" state before you proceed with migration. You can plug the new phone
                                 into the network, wait until the phone registers and then perform the migration tasks. Once the migration is successful, the
                                 device will re-register with the users phone configuration data.

Step 1

Dial the extension that is assigned to the Self-Provisioning IVR from a new Cisco IP Phone.

Step 2

Press 2 to replace an existing phone.

Step 3

Enter the primary extension number of your phone followed by the pound key ( # ).

Step 4

Enter your PIN followed by the pound key ( # ).

Migration starts after a successful authentication. After successful migration, the phone restarts with the configuration
                                             settings migrated from your old phone.

If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option.

### Migrate Phones Using Self-Provisioning IVR (Administrator)

Administrators can use this procedure to migrate Cisco IP Phones on behalf of an end user, or to migrate common phones (for
                                 example, a lobby phone).

#### Before you begin

Make sure that the old phone is in the "Unregistered" state before you proceed with migration. You can plug the new phone
                                 into the network, wait until the phone registers and then perform the migration tasks. Once the migration is successful, the
                                 device will re-register with the users phone configuration data.

Step 1

Dial the extension that is assigned to the Self-Provisioning IVR from a new phone.

Step 2

Press 2 to replace an existing phone.

Step 3

Enter the primary extension number of an end user phone or common phone followed by the pound key ( # ).

Step 4

Enter the Authentication Code followed by the pound key ( # ).

Migration starts after a successful authentication. Following the migration, the phone restarts with configuration settings
                                             migrated from end user’s old phone.

### Phone Migration Service COP File

If you are running any version of the Unified Communications Manager starting from 11.5(1) until 11.5(1)SU7, install Phone
                              Migration Service COP file (ciscocm-migration-service-11-5-1.zip) to get the Native Phone Migration feature support.

As part of the COP file installation, ‘Tftp restart’ service is done automatically for Unified Communications Manager.

### View Phone Migration Report

Use this procedure to view the list of all the Cisco IP Phones that are migrated.

Step 1

In Cisco Unified CM Administration, select Device> Phone .

Step 2

From the Find and List Phones page, choose Migrate (old phone) from the Find Phone where drop-down list.

Step 3

Click Find .

You can view the list of all the old devices that got migrated. This list is populated only if the Retain Existing Phone option is configured in the Enterprise Parameters page.

## Migrate Phones using Cisco Unified CM Administration Interface

Use this procedure to migrate phones using either the Phone Template or Phone Type (and Protocol) options in the Cisco Unified CM Administration interface.

Step 1

In the Find and List Phones window ( Device > Phone ), find the Cisco IP Phone that you want to migrate.

Step 2

In the Phone Configuration window for the Cisco IP Phone that you want to migrate, choose Migrate Phone from the Related Links drop-down list.

Step 3

To migrate phones, you can use one of the following options:

Phone Template —Choose the phone template for the phone model to which you want to migrate the phone configuration.

Phone Type (and Protocol) —Choose the Cisco IP Phone model for which you want to migrate the phone configuration.

Step 4

Enter the MAC address for the new Cisco Unified IP Phone to which you are migrating the configuration.

Step 5

(Optional) Enter a description for the new phone. For more information on the migration considerations and configuration settings, see
                                       the Cisco Unified CM Administration Online Help pages.

Step 6

Click Save .

If a warning message displays that the new phone may lose feature functionality, click OK . After migration, the new device will inherit setting of the old phone.

## Phones Using Shared Lines

Consider a scenario where an old phone has the primary DN shared line with multiple devices. These devices may be owned by
                           the same user or among multiple users. When you try to migrate the old phone with a new Cisco IP Phone using Self-Provisioning
                           IVR or Phone Migration Service methods using a shared line, migration is possible only for users who own the device with the
                           DN as Line 1. Here, the shared lines feature settings are carried over after phone migration.

If the old phone does not support the Shared Line feature, the old phones lines are removed after phone migration. The new
                           phone retains the old phones lines after phone migration.

| Note | Using Self-provisioning IVR, you can migrate or replace the phone under the primary extension of the authenticated user. Phone users authenticate to the IVR using their user PIN. Administrators can authenticate using a specified authentication
                                       code. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate Services for Self-Provisioning | Activate the Self-Provisioning IVR and CTI Manager services in Cisco Unified Serviceability. |
| Step 2 | Enable Autoregistration for Self-Provisioning | Enable autoregistration parameter for self-provisioning. |
| Step 3 | Configure CTI Route Point | Configure a CTI route point to handle the self-provisioning IVR service. |
| Step 4 | Assign a Directory Number to the CTI Route Point | Configure the extension that users dial in order to access the self-provisioning IVR and associate that extension to the CTI
                                          route point. |
| Step 5 | Configure Application User for Self-Provisioning | Configure an application user for the self-provisioning IVR. Associate the CTI route point to the application user. |
| Step 6 | Configure the System for Self-Provisioning | Configure Self-Provisioning system settings. |
| Step 7 | Enable Self-Provisioning in a User Profile | Enables the users to Self-Provision phones in the user profile to which they are assigned. |
| Step 8 | Migrate phones using any of these procedures: Migrate Phones Using Self-Provisioning IVR (Administrator) Migrate Phones Using Self-Provisioning IVR (Phone Users) | Choose the migration procedure that applies for you. The Self-Provisioning IVR can be used by either administrators or phone
                                          users to migrate phones. |
| Step 9 | View Phone Migration Report | Following the migration, view a report that shows Cisco IP Phones that are migrated. |

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down list, select the publisher node and click Go . |
| Step 3 | Under CM Services , check Cisco CTI Manager . |
| Step 4 | Under CTI Services , check Self Provisioning IVR . |
| Step 5 | Click Save . |

| Step 1 | In Cisco Unified CM Administration, choose System > Cisco Unified CM . |
|---|---|
| Step 2 | Click on the publisher node. |
| Step 3 | Select the Universal Device Template that you want to be applied to provisioned phones. |
| Step 4 | Select the Universal Line Template that you want to be applied to the phone lines for provisioned phones. |
| Step 5 | Use the Starting Directory Number and Ending Directory Number fields to enter a range of directory numbers to apply to provisioned phones. |
| Step 6 | Uncheck the Auto-registration Disabled on the Cisco Unified Communications Manager check box. |
| Step 7 | Confirm the ports that will be used for SIP registrations. In most cases, there is no need to change the ports from their
                                          default settings. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose, Device > CTI Route Points . |
|---|---|
| Step 2 | Complete either of the following steps: Click Find and select an existing CTI route point. Click Add New to create a new CTI route point. |
| Step 3 | In the Device Name field, enter a unique name to identify the route point. |
| Step 4 | From the Device Pool drop-down list, select the device pool that specifies the properties for this device. |
| Step 5 | From the Location drop-down list, select the appropriate location for this CTI route point. |
| Step 6 | From the Use Trusted Relay Point drop-down list, enable or disable whether Unified Communications Manager inserts a trusted relay point (TRP) device with
                                          this media endpoint. The default setting is to use the Common Device Configuration setting that is associated to this device. |
| Step 7 | Complete the remaining fields in the CTI Route Point Configuration window. For more information on the fields and their settings, see the online help. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > CTI Route Point . |
|---|---|
| Step 2 | Click Find and select the CTI route point that you set up for self-provisioning. |
| Step 3 | Under Association click Line [1] - Add a new DN . The Directory Number Configuration window displays. |
| Step 4 | In the Directory Number field, enter the extension that you want users to dial to access the Self-Provisioning IVR service. |
| Step 5 | Click Save . |
| Step 6 | Complete the remaining fields in the Directory Number Configuration window. For more information with the fields and their settings, see the online help. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User > Application User . |
|---|---|
| Step 2 | Perform either of the following steps: To select an existing application user, click Find and select the application user. To create a new application user, click Add New . |
| Step 3 | In the User ID text box, enter a unique ID for the application user. |
| Step 4 | Select a BLF Presence Group for the application user. |
| Step 5 | Associate the CTI route point that you created to the application user by performing the following steps: If the CTI route point that you created  does not appear in the Available Devices list box, click Find More Route Points . The CTI route point that you created displays as an available device. In the Available Devices list, select the CTI route point that you created for self-provisioning and click the down arrow. The CTI route point displays in the Controlled Devices list. |
| Step 6 | Complete the remaining fields in the Application User Configuration window. For help with the fields and their settings, see the online help. |
| Step 7 | Click Save . |

| Note | In order to use
                                          		  the self-provisioning feature, your end users must also have the feature
                                          		  enabled in their user profiles. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Self-Provisioning . |
|---|---|
| Step 2 | Configure
                                          			 whether you want the self-provisioning IVR to authenticate end users by
                                          			 clicking one of the following radio buttons: Require
                                                				  Authentication —In order to use the self-provisioning IVR, end users
                                             				must enter their password, PIN, or a system authentication code. No Authentication
                                                				  Required —End users can access the self-provisioning IVR without
                                             				authenticating. |
| Step 3 | If the
                                          			 self-provisioning IVR is configured to require authentication, click one of the
                                          			 following radio buttons to configure the method whereby the IVR authenticates
                                          			 end users: Allow authentication for end users only —End users must enter their password or PIN. Allow authentication for
                                                				  users (via Password/PIN) and Administrators (via Authentication
                                                				  Code) —End Users must enter an authentication code. If you choose
                                             				this option, configure the authentication code by entering an integer between 0
                                             				and 20 digits in the Authentication Code text box. |
| Step 4 | In the IVR
                                             				Settings list boxes, use the arrows to select the Language that you
                                          			 prefer to use for IVR prompts. The list of available languages depends on the
                                          			 language packs that you have installed on your system. Refer to the Downloads
                                          			 section of cisco.com if you want to download additional language packs. |
| Step 5 | From the CTI Route Points drop-down list, choose the CTI route point that you have configured for your self-provisioning IVR. |
| Step 6 | From the Application User drop-down list, choose the application user that you have configured for self-provisioning. |
| Step 7 | Click Save . |

| Note | If you don’t know which user profile your users are using, you can open a user’s settings in the End User Configuration window
                                             and view the User Profile field to get the correct profile. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > User Profile . |
|---|---|
| Step 2 | Click Find and select the user profile to which the user is assigned. |
| Step 3 | Assign Universal Line Templates and Universal Device Templates to the user profile. |
| Step 4 | Configure user settings for Self-Provisioning: Check the Allow End User to Provision their own phones check box. Enter a limit for the number of phones a user can provision. The default is 10. If you want users to be able to use self-provisioning to reassign a previously assigned phone, check the Allow Provisioning of a phone that is already assigned to a different End User setting in the user profile page associated with the end user of old device. Users can reassign a previously assigned phone
                                             only if this check box is enabled in the User Profile that is associated to the old device. |
| Step 5 | Click Save . |

| Step 1 | Dial the extension that is assigned to the Self-Provisioning IVR from a new Cisco IP Phone. |
|---|---|
| Step 2 | Press 2 to replace an existing phone. |
| Step 3 | Enter the primary extension number of your phone followed by the pound key ( # ). |
| Step 4 | Enter your PIN followed by the pound key ( # ). Migration starts after a successful authentication. After successful migration, the phone restarts with the configuration
                                             settings migrated from your old phone. Note If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option. | Note | If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option. |
| Note | If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option. |

| Note | If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option. |
|---|---|

| Step 1 | Dial the extension that is assigned to the Self-Provisioning IVR from a new phone. |
|---|---|
| Step 2 | Press 2 to replace an existing phone. |
| Step 3 | Enter the primary extension number of an end user phone or common phone followed by the pound key ( # ). |
| Step 4 | Enter the Authentication Code followed by the pound key ( # ). Migration starts after a successful authentication. Following the migration, the phone restarts with configuration settings
                                             migrated from end user’s old phone. |

| Note | If you plan to upgrade the Unified CM after Phone Migration Service COP file installation, ensure that you upgrade your Unified
                                       CM server to a release version that has native support for the Native Phone Migration feature. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, select Device> Phone . |
|---|---|
| Step 2 | From the Find and List Phones page, choose Migrate (old phone) from the Find Phone where drop-down list. |
| Step 3 | Click Find . You can view the list of all the old devices that got migrated. This list is populated only if the Retain Existing Phone option is configured in the Enterprise Parameters page. |

| Step 1 | In the Find and List Phones window ( Device > Phone ), find the Cisco IP Phone that you want to migrate. |
|---|---|
| Step 2 | In the Phone Configuration window for the Cisco IP Phone that you want to migrate, choose Migrate Phone from the Related Links drop-down list. |
| Step 3 | To migrate phones, you can use one of the following options: Phone Template —Choose the phone template for the phone model to which you want to migrate the phone configuration. Phone Type (and Protocol) —Choose the Cisco IP Phone model for which you want to migrate the phone configuration. |
| Step 4 | Enter the MAC address for the new Cisco Unified IP Phone to which you are migrating the configuration. |
| Step 5 | (Optional) Enter a description for the new phone. For more information on the migration considerations and configuration settings, see
                                       the Cisco Unified CM Administration Online Help pages. |
| Step 6 | Click Save . If a warning message displays that the new phone may lose feature functionality, click OK . After migration, the new device will inherit setting of the old phone. |