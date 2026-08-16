---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-feature-configuration-guide-cisco1251su4-cucm-m--fe41515538
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_feature-configuration-guide-cisco1251su4/cucm_m_phone-replacement-migration-ivr-phone.html
retrieved_at: 2026-08-16T17:01:24.336221+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: July 31, 2025

Chapter: Native Phone Migration using IVR and Phone Services

## Chapter: Native Phone Migration using IVR and Phone Services

# Native Phone Migration using IVR and Phone Services

## Native Phone Migration using IVR and Phone Services Overview

The Phone Migration feature is an easy and intuitive Cisco IP Phone migration solution native to Unified Communications Manager.
                           It minimizes the cost and complexity of replacing deprecated or faulty phones. Using the solution, an end user or an administrator
                           can easily migrate all the settings from an old phone to a new phone with a simple user interface. Solution supports following
                           methods for migrating the phones:

Using Self-provisioning IVR Service

Using Phone Migration Service

Using Cisco Unified CM Administration Interface

Following table provides a quick comparison of the various phone migration options:

Using Self-provisioning IVR Service

Using Phone Migration Service

Using Unified CM Administration Interface

End user or administrator driven phone migration

End user (Self-service)

End user (Self-service)

Administrator

Auto-registration required

Yes

No

No

Migration steps

Auto register a new phone

Dial self-provisioning IVR number

Follow the voice prompts

Plug-in new phone to the network

Key in primary extension and PIN (optional)

Sign in to Cisco Unified CM Administration interface

Choose “Migrate Phone” option in the Phone Configuration page of the old phone

Enter phone type (model & protocol) and MAC address of the new phone

Administrator involvement

Medium

Low

High

### Enterprise Parameters for Phone Migration

Migration depends on the following two parameters in the Enterprise Parameters Configuration page:

When Provisioning a Replacement Phone for an End User —You can choose either Retain Existing Phone(s) (default option) or Delete the Existing Phone for that End User . If the Retain Existing Phone(s) option is selected, then during migration the old phone is marked as migrated and can be filtered in the Find and List Phones
                                    page to generate migration report.

Security Profile for Migrated Phone —This option determines the type of security profile that is applied for a migrated phone (old phone was in secure mode) during
                                    phone migration. Choosing the Non-secure profile brings up your device in the non-secure mode.

Phone Migration User Identification Prompt —This parameter determines whether a user is able to proceed with phone migration using the Self-Service User ID or using
                                    the Primary Extension. If the Use Enduser Self-Service User ID option is selected, the end user is prompted to enter the unique Self-Service User ID before proceeding with phone migration.
                                    If the Use Enduser Primary Extension option is selected, you can migrate your phone after entering the primary extension number. In this mode, if the same DN
                                    exists in different route partitions, phone migration is not possible using IVR or Phone Migration service.

The default value is Use Enduser Primary Extension .

To facilitate secure phone migration, the following Standard Universal Phone Security Profiles templates have been added.
                              Based on the old phone security profile, the new phone chooses one of these new profiles.

Universal Device Template - Security Profile - Non-Secure

Universal Device Template - Security Profile – Authenticated

Universal Device Template - Security Profile – Encrypted

Universal Device Template - Security Profile - Encrypted - Device_TFTP

Universal Device Template - Security Profile - Encrypted EC preferred

The following table lists the new devices security profile mappings after phone migration:

Old Security Profile Settings

New Mapped Profile Name

Device Security Mode

TFTP Encrypted Configuration

Transport Type

Key Order

Non-Secure

No

TCP

RSA

Universal Device Template - Security Profile - Non-Secure

Authenticated

No

TLS

RSA

Universal Device Template - Security Profile – Authenticated

Encrypted

No

TLS

RSA

Universal Device Template - Security Profile – Encrypted

Encrypted

Yes

TLS

RSA

Universal Device Template - Security Profile - Encrypted - Device_TFTP

Encrypted

Yes

TLS

EC preferred, RSA backup

Universal Device Template - Security Profile - Encrypted - Device_TFTP

Encrypted

No

TLS

EC preferred, RSA backup

Universal Device Template - Security Profile - Encrypted EC preferred

## Phone Migration Prerequisites

### Using Self-provisioning IVR

Before your end users can use self-provisioning for migration, the following should be configured:

Enable Auto-registration.

End users must have a primary extension. Ensure that the primary DN is always Line 1 on the phone or device.

End users must be associated to a user profile or feature group template that includes a universal line template, universal
                                    device template and which has Self-Provisioning enabled.

Ensure that the right “CTI Route Point” and “Application User” configurations are selected.

Enable Self-Provisioning IVR service.

### Using Phone Migration Service

Before your end users can use Phone Migration Service for migration, the following should be configured:

Disable Auto-registration.

End users must have a primary extension. Ensure that the primary DN is always Line 1 on the phone or device.

Supported Phone Models: 88XX, 78XX, 8832, and 7832.

Minimum supported phone version is Release 12.8.1 and above.

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

### Phone Migration Tasks

After self-provisioning Authentication is setup, use any of the following procedures to migrate phones.

#### Migrate Phones Using Self-Provisioning IVR (Administrator)

Administrators can use this procedure to migrate Cisco IP Phones on behalf of an end user, or to migrate common phones (for
                                    example, a lobby phone).

##### Before you begin

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

#### Migrate Phones Using Self-Provisioning IVR (Phone Users)

Phone users can use this procedure to migrate to a new Cisco IP Phone.

##### Before you begin

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

## Phone Migration Task Flow Using Phone Migration Service

Use the following task flow to guide you through the phone migration procedure using Phone Migration Service.

After you complete this workflow, you can migrate old or faulty Cisco IP Phones, and track the migrated phones list.

Step 1

Disable Autoregistration

Disable the autoregistration parameter before phone migration.

Step 2

Set Up Default Phone Load

Configure the default phone load before the phone migration service.

Step 3

Configure Self-Provisioning Authentication

Configure the required Self-Provisioning authentication settings.

Step 4

Migrate phones using any of these procedures:

- Migrate Phones Using Phone Migration Service (Administrator)

- Migrate Phones Using Phone Migration Service (Phone Users)

Choose the migration procedure that applies for you. The Phone Migration Service can be used by either administrators or phone
                                          users to migrate phones.

Step 5

View Phone Migration Report

Following the migration, view a report that shows Cisco IP Phones that are migrated.

### Disable Autoregistration

To use the Phone Migration Service, autoregistration must be disabled.

Step 1

In Cisco Unified CM Administration, choose System > Cisco Unified CM .

Step 2

Click on the publisher node.

Step 3

Check the Auto-registration Disabled on the Cisco Unified Communications Manager check box.

Step 4

Confirm the ports that will be used for SIP registrations. In most cases, there is no need to change the ports from their
                                          default settings.

Step 5

Click Save .

### Set Up Default Phone Load

Use this procedure to set up the default phone load before the phone migration service.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Device Defaults .

Step 2

Select the required phone model for migration.

Step 3

Enter the phone load and click the Swap Loads button in the phone load to make it the default phone load.

Step 4

Click Save .

### Configure Self-Provisioning Authentication

Step 1

From Cisco Unified CM Administration, choose User Management > Self-Provisioning .

Step 2

Configure whether you want the self-provisioning to authenticate end users by clicking one of the following radio buttons:

- Require Authentication —In order to use self-provisioning, end users must enter their password, PIN, or a system authentication code.

- No Authentication Required —End users can access the self-provisioning options without authenticating.

Step 3

If the self-provisioning functionality is configured to require authentication, click one of the following radio buttons to
                                          configure the method whereby the self-provisioning options authenticates end users:

- Allow authentication for end users only —End users must enter their password or PIN.

- Allow authentication for users (via Password/PIN) and Administrators (via Authentication Code) —End Users must enter an authentication code. If you choose this option, configure the authentication code by entering an
                                             integer between 0 and 20 digits in the Authentication Code text box.

Step 4

Click Save .

### Phone Migration Tasks

After self-provisioning Authentication is setup, use any of the following procedures to migrate phones.

#### Migrate Phones Using Phone Migration Service (Administrator)

Administrators can use this procedure to migrate Cisco IP Phones on behalf of an end user, or to migrate common phones (for
                                    example, a lobby phone).

##### Before you begin

Make sure that the old phone is in the "Unregistered" state before you proceed with migration. You can plug the new phone
                                    into the network, wait until you get the phone migration or provisioning prompt and start the migration process. Once the
                                    migration is successful, the device re-registers with the users phone configuration data.

Step 1

Connect the new Cisco IP Phone to the network.

Step 2

Select option 2 to replace an existing phone.

Step 3

Enter the primary extension number of your phone.

Step 4

Enter the Authentication Code .

Migration starts after a successful authentication. After successful migration, the phone restarts with configuration settings
                                                migrated from your old phone.

#### Migrate Phones Using Phone Migration Service (Phone Users)

Phone users can use this procedure to migrate to a new Cisco IP Phone using a non-IVR method. After you plug in the phones
                                    to the network, the phone will attempt to boot and configure itself. From the default phone load, users get options to select
                                    either the 'Provision a new phone' or 'Replace an existing phone'.

##### Before you begin

Make sure that the old phone is in the "Unregistered" state before you proceed with migration. You can plug the new phone
                                    into the network, wait until you get the phone migration or provisioning prompt and start the migration process. Once the
                                    migration is successful, the device re-registers with the users phone configuration data.

Step 1

Connect the new Cisco IP Phone to the network.

Step 2

Select the option 2 to replace an existing phone.

Step 3

Enter the primary extension number of your phone.

Step 4

Enter your PIN .

Migration starts after a successful authentication. After successful migration, the phone restarts with configuration settings
                                                migrated from your old phone.

#### Phone Migration Service COP File

If you are running any version of the Unified Communications Manager starting from 11.5(1) until 11.5(1)SU7, install Phone
                                 Migration Service COP file (ciscocm-migration-service-11-5-1.zip) to get the Native Phone Migration feature support.

As part of the COP file installation, ‘Tftp restart’ service is done automatically for Unified Communications Manager.

## View Phone Migration Report

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

## Migration Scenarios

### Phones Using Shared Lines

Consider a scenario where an old phone has the primary DN shared line with multiple devices. These devices may be owned by
                              the same user or among multiple users. When you try to migrate the old phone with a new Cisco IP Phone using Self-Provisioning
                              IVR or Phone Migration Service methods using a shared line, migration is possible only for users who own the device with the
                              DN as Line 1. Here, the shared lines feature settings are carried over after phone migration.

If the old phone does not support the Shared Line feature, the old phones lines are removed after phone migration. The new
                              phone retains the old phones lines after phone migration.

### Phone Migration Service Running on Proxy TFTP

Native phone migration using Phone Migration Service support Cisco proxy TFTP server deployment models.

Phone Migration Service running on the proxy TFTP searches for the primary extension on all the remote clusters and redirect
                              the phone to its home or local Phone Migration Service for completing phone migration.

In a proxy setup environment, Unified Communications Manager server looks for devices with same DN in a remote cluster. If
                              there is more than one device in the registered or unregistered state with the same DN in any one of the off-cluster, those
                              devices from that particular off-cluster is not considered for phone migration. This is a known limitation for Release 11.5(1)SU8.

### Phone Migration Service—User Assigned with Multiple Devices

If there is more than one device for the user with the same primary extension for migration, user will be prompted to choose
                                 the device to be migrated.

The following table displays the various migration scenarios possible:

Device Status Before Phone Migration

Phone Display During Migration

Scenario 1

Device 1—Registered

Device 2—Unregistered

Phone Configuration settings of Device 2 will be migrated.

Scenario 2

Device 1—Registered

Device 2—Registered

Device 3—Unregistered

Phone Configuration settings of Device 3 will be migrated.

Scenario 3

Device 1—Registered

Device 2—Unregistered

Device 3—Unregistered

Displays the device list with the following: Description, Phone Model, and MAC Address. Users should choose the device from
                                             the list required for phone migration.

Scenario 4

Device 1—Unregistered

Device 2—Unregistered

Device 3—Unregistered

Displays the device list with the following: Description, Phone Model, and MAC Address. Users should choose the device from
                                             the list required for phone migration.

Scenario 5

Device 1—Registered

Device 2—Registered

Device 3—Registered

Displays the device list with the following: Description, Phone Model, and MAC Address. Users should choose the device from
                                             the list required for phone migration.

Scenario 6

More than 3 devices are in Registered or Unregistered states

Displays the device list with the following: Description, Phone Model, and MAC Address. Users should choose the device from
                                             the list required for phone migration.

### Device Display Based on Unified CM Parameter Settings

The following table lists the behavior of the migration screen on the new phone based on the release version of Cisco Unified
                                 Communications Manager and related configuration settings:

Phone or Device preconfigured by Administrator

Autoregistration Enabled at Enterprise Level

Onboarding Method at Device Defaults Level

Behavior without Phone Migration Service

Behavior with Phone Migration Service

No

Yes

—

Devices get auto registered to the network.

Devices get auto registered to the network.

No

No

—

Phone replacement screen prompts to enter the Primary Extension and PIN.

Yes

N/A

—

Device registers with the preconfigured settings.

Device registers with the preconfigured settings.

No

Yes

Device Type set to Activation Code

Welcome screen of the phone prompts the following: "Enter activation code".

Phone replacement screen prompts to select one of the following: “Provision a new phone” or “Replace an existing phone”.

No

No

Device Type set to Auto Registration

Device retries to register to the network and gives up.

Phone replacement screen prompts the following: “Replace an existing phone”.

No

No

Device Type set to Activation Code

Welcome screen of the phone prompts the following: "Enter activation code".

Phone replacement screen prompts to select one of the following: “Provision a new phone” or “Replace an existing phone”.

Yes

N/A

N/A

Device registers with the preconfigured settings.

### Phones Using Extension Mobility

In scenarios where the old phone supports Extension Mobility login, after migration the new device will also support the Extension
                              Mobility capability. If the old phone was logged-in before migration, then the logged-in Extension Mobility user is automatically
                              logged-out during the phone migration. The user must perform fresh Extension Mobility login on the new phone.

Native phone migration does not support end-users Extension Mobility Device profile migration.

### CTI Controlled Devices

If an old device is CTI Controlled before phone migration, then the new device is also CTI controlled. This is because the
                              device configuration settings are carried over after phone migration.

### Phones with Key Expansion Module

If the Key Expansion Module (KEM) attached to your old phone is not compatible with your new phone model, you will lose the
                              KEM 'Expansion Module Information' configuration settings on the new phone after phone migration.

The following table explains different scenarios:

Scenarios

Old Phone  (Model 79xx)

New Phone (Model 88xx)

Expected Behavior After Migration

KEM 1 attached to the old phone is compatible with the new phone.

User removes the KEM 1 from the old phone and attaches it with the new phone.

KEM 1

KEM 1

KEM 1 configuration settings are carried over.

KEM 1 attached to the old phone is incompatible with the new phone.

User attaches a compatible KEM 2 (brand new or used) to the new phone.

KEM 1

KEM 2

KEM 1 configuration settings are carried over to KEM 2.

KEM 1 attached to the old phone is deprecated.

User attaches a new KEM 3 to the new phone.

KEM 1

KEM 3

KEM 1 configuration settings are carried over to KEM 3.

### Product Specific Configuration Parameters

During phone migration, the product-specific parameters of the older phones are also migrated. The new phone considers only
                              the parameters that the phone understands. The remaining parameters are set to their default value.

If the ‘Line Mode’ parameter is already configured during phone migration, the ‘Line Mode’ configuration settings are carried
                              over. Else, this parameter is set as ‘Session Line Mode’ by default.

Also, during phone migration, if the "Show All Calls on Primary Line" parameter is configured in the old phone, then the new
                              phone will retain the "Show All Calls on Primary Line" parameter after phone migration. If this parameter is not configured
                              before phone migration, it is enabled by default after phone migration.

### Phone Button Templates

When a SCCP Phone model is migrated to a SIP Phone model, the SIP Phone considers only the parameters that it understands.
                              Else, it takes the default configuration values from the SIP Phone model (for example, Standard SIP Profile).

If the old phone had a unique Custom Phone Button Template, then the new phone will retain the Custom Phone Button Template
                              after phone migration. For the Standard Phone Button template, the new device uses the Standard Phone Button Template specific
                              to the phone model.

Old Device

Phone Button Template of the Old Device

New Device Selected for Phone Migration

Phone Button Template of the New Device After Phone Migration

Cisco Unified IP Phone 7965 SCCP

Standard 7965 SCCP

Cisco IP Phone 8861

Standard 8861 SIP

Cisco Unified IP Phone 7965 SCCP

Universal Device Template Button layout

Cisco IP Phone 8861

Universal Device Template Button layout

Cisco Unified IP Phone 7965 SCCP

Custom 7965 SCCP

Cisco IP Phone 8861

Custom 7965 SCCP

Cisco Unified IP Phone 8851 SIP

Standard 8851 SIP

Cisco IP Phone 8861

Standard 8861 SIP

### Collaboration Devices—Room Systems, Desk, and IP Phones

You can only migrate a video endpoints device to another video endpoints device.

Unified Communications Manager does not support phone migration to CSF (Jabber for Desktop), TCT (Jabber for iPhone), TAB
                                    (Jabber for iPad), or BOT (Jabber for Android) devices.

You cannot migrate video endpoints using Phone Migration Service.

If the old video endpoints device was in the locked state, note that the new video endpoints device will not retain the locked
                                    state after phone migration.

|  | Using Self-provisioning IVR Service | Using Phone Migration Service | Using Unified CM Administration Interface |
|---|---|---|---|
| End user or administrator driven phone migration | End user (Self-service) | End user (Self-service) | Administrator |
| Auto-registration required | Yes | No | No |
| Migration steps | Auto register a new phone Dial self-provisioning IVR number Follow the voice prompts | Plug-in new phone to the network Key in primary extension and PIN (optional) | Sign in to Cisco Unified CM Administration interface Choose “Migrate Phone” option in the Phone Configuration page of the old phone Enter phone type (model & protocol) and MAC address of the new phone |
| Administrator involvement | Medium | Low | High |

| Note | While phone migration using Self-provisioning IVR Service and Phone Migration Service facilitates the migration of the phone
                                    by an end user as a self-service; administrators, can use these methods to migrate the phone on-behalf of an end-user or common
                                    phones (for example, a lobby phone). |
|---|---|

| Note | During phone migration, if the end user does not remember the PIN, administrators should advise the end user to log in to
                                    the Self Care Portal to change the PIN, if required. |
|---|---|

| Note | If the administrator decides to choose the Retain Existing Phone(s) option for phone migration, a total of two licenses will be consumed, that is, one license each for the existing phone and
                                             the new phone picked up for migration. |
|---|---|

| Note | During phone migration, if the administrator decides to choose the Retain Existing Phone(s) option for phone migration, the intercom DN is not migrated to the new device. If the Delete the Existing Phone for that End User option is selected, the intercom DN information is also migrated. |
|---|---|

| Old Security Profile Settings | New Mapped Profile Name |
|---|---|
| Device Security Mode | TFTP Encrypted Configuration | Transport Type | Key Order |  |
| Non-Secure | No | TCP | RSA | Universal Device Template - Security Profile - Non-Secure |
| Authenticated | No | TLS | RSA | Universal Device Template - Security Profile – Authenticated |
| Encrypted | No | TLS | RSA | Universal Device Template - Security Profile – Encrypted |
| Encrypted | Yes | TLS | RSA | Universal Device Template - Security Profile - Encrypted - Device_TFTP |
| Encrypted | Yes | TLS | EC preferred, RSA backup | Universal Device Template - Security Profile - Encrypted - Device_TFTP |
| Encrypted | No | TLS | EC preferred, RSA backup | Universal Device Template - Security Profile - Encrypted EC preferred |

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

| Step 1 | Dial the extension that is assigned to the Self-Provisioning IVR from a new phone. |
|---|---|
| Step 2 | Press 2 to replace an existing phone. |
| Step 3 | Enter the primary extension number of an end user phone or common phone followed by the pound key ( # ). |
| Step 4 | Enter the Authentication Code followed by the pound key ( # ). Migration starts after a successful authentication. Following the migration, the phone restarts with configuration settings
                                                migrated from end user’s old phone. |

| Step 1 | Dial the extension that is assigned to the Self-Provisioning IVR from a new Cisco IP Phone. |
|---|---|
| Step 2 | Press 2 to replace an existing phone. |
| Step 3 | Enter the primary extension number of your phone followed by the pound key ( # ). |
| Step 4 | Enter your PIN followed by the pound key ( # ). Migration starts after a successful authentication. After successful migration, the phone restarts with the configuration
                                                settings migrated from your old phone. Note If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option. | Note | If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option. |
| Note | If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option. |

| Note | If the phone is assigned to another user, a phone user can re-provision the phone provided an administrator has enabled the Allow Provisioning of a phone already assigned to a different End User option in the user's User Profile window. Talk to your administrator about this option. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Disable Autoregistration | Disable the autoregistration parameter before phone migration. |
| Step 2 | Set Up Default Phone Load | Configure the default phone load before the phone migration service. |
| Step 3 | Configure Self-Provisioning Authentication | Configure the required Self-Provisioning authentication settings. |
| Step 4 | Migrate phones using any of these procedures: Migrate Phones Using Phone Migration Service (Administrator) Migrate Phones Using Phone Migration Service (Phone Users) | Choose the migration procedure that applies for you. The Phone Migration Service can be used by either administrators or phone
                                          users to migrate phones. |
| Step 5 | View Phone Migration Report | Following the migration, view a report that shows Cisco IP Phones that are migrated. |

| Step 1 | In Cisco Unified CM Administration, choose System > Cisco Unified CM . |
|---|---|
| Step 2 | Click on the publisher node. |
| Step 3 | Check the Auto-registration Disabled on the Cisco Unified Communications Manager check box. |
| Step 4 | Confirm the ports that will be used for SIP registrations. In most cases, there is no need to change the ports from their
                                          default settings. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Device Defaults . |
|---|---|
| Step 2 | Select the required phone model for migration. |
| Step 3 | Enter the phone load and click the Swap Loads button in the phone load to make it the default phone load. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > Self-Provisioning . |
|---|---|
| Step 2 | Configure whether you want the self-provisioning to authenticate end users by clicking one of the following radio buttons: Require Authentication —In order to use self-provisioning, end users must enter their password, PIN, or a system authentication code. No Authentication Required —End users can access the self-provisioning options without authenticating. |
| Step 3 | If the self-provisioning functionality is configured to require authentication, click one of the following radio buttons to
                                          configure the method whereby the self-provisioning options authenticates end users: Allow authentication for end users only —End users must enter their password or PIN. Allow authentication for users (via Password/PIN) and Administrators (via Authentication Code) —End Users must enter an authentication code. If you choose this option, configure the authentication code by entering an
                                             integer between 0 and 20 digits in the Authentication Code text box. |
| Step 4 | Click Save . |

| Step 1 | Connect the new Cisco IP Phone to the network. |
|---|---|
| Step 2 | Select option 2 to replace an existing phone. Note If Administrator has not configured Activation Code based device onboarding or phone migration is done on the 11.5(1)SU8 version
                                                         of Unified Communications Manager which does not support activation code, the phone displays the screen to enter the primary
                                                         extension. | Note | If Administrator has not configured Activation Code based device onboarding or phone migration is done on the 11.5(1)SU8 version
                                                         of Unified Communications Manager which does not support activation code, the phone displays the screen to enter the primary
                                                         extension. |
| Note | If Administrator has not configured Activation Code based device onboarding or phone migration is done on the 11.5(1)SU8 version
                                                         of Unified Communications Manager which does not support activation code, the phone displays the screen to enter the primary
                                                         extension. |
| Step 3 | Enter the primary extension number of your phone. |
| Step 4 | Enter the Authentication Code . Migration starts after a successful authentication. After successful migration, the phone restarts with configuration settings
                                                migrated from your old phone. Note Consider a scenario where the On-premise Onboarding Method option is selected as Auto registration in the Device Defaults Configuration page. While performing the phone migration, if you press either the EXIT or BACK button when an error message is displayed, it takes you directly to the initial phone migration screen after a possible expected
                                                         delay. This delay is due to the phones trying to re-register to the Unified CM as auto-registration is disabled in the Unified
                                                         Communications Manager server. Note If there are more than one device for the user with the same primary extension, user will be prompted to choose the device
                                                         to be migrated. For more information, see Phone Migration Service—User Assigned with Multiple Devices . | Note | Consider a scenario where the On-premise Onboarding Method option is selected as Auto registration in the Device Defaults Configuration page. While performing the phone migration, if you press either the EXIT or BACK button when an error message is displayed, it takes you directly to the initial phone migration screen after a possible expected
                                                         delay. This delay is due to the phones trying to re-register to the Unified CM as auto-registration is disabled in the Unified
                                                         Communications Manager server. | Note | If there are more than one device for the user with the same primary extension, user will be prompted to choose the device
                                                         to be migrated. For more information, see Phone Migration Service—User Assigned with Multiple Devices . |
| Note | Consider a scenario where the On-premise Onboarding Method option is selected as Auto registration in the Device Defaults Configuration page. While performing the phone migration, if you press either the EXIT or BACK button when an error message is displayed, it takes you directly to the initial phone migration screen after a possible expected
                                                         delay. This delay is due to the phones trying to re-register to the Unified CM as auto-registration is disabled in the Unified
                                                         Communications Manager server. |
| Note | If there are more than one device for the user with the same primary extension, user will be prompted to choose the device
                                                         to be migrated. For more information, see Phone Migration Service—User Assigned with Multiple Devices . |

| Note | If Administrator has not configured Activation Code based device onboarding or phone migration is done on the 11.5(1)SU8 version
                                                         of Unified Communications Manager which does not support activation code, the phone displays the screen to enter the primary
                                                         extension. |
|---|---|

| Note | Consider a scenario where the On-premise Onboarding Method option is selected as Auto registration in the Device Defaults Configuration page. While performing the phone migration, if you press either the EXIT or BACK button when an error message is displayed, it takes you directly to the initial phone migration screen after a possible expected
                                                         delay. This delay is due to the phones trying to re-register to the Unified CM as auto-registration is disabled in the Unified
                                                         Communications Manager server. |
|---|---|

| Note | If there are more than one device for the user with the same primary extension, user will be prompted to choose the device
                                                         to be migrated. For more information, see Phone Migration Service—User Assigned with Multiple Devices . |
|---|---|

| Note | An end user should perform migration only if they are the owner of the old device. |
|---|---|

| Note | If you decide to choose the Retain Existing Phone(s) ' option from the When Provisioning a Replacement Phone for an End User enterprise parameter and you migrate the phone using the Phone Template, the old migrated phone configurations details will
                                             not be listed in the Find List page. Only the successful new phone migration details are listed. This is because the Retain Existing Phone(s) option is applicable only for Phone Migrations based on Phone Types and not based on the Phone Template. |
|---|---|

| Step 1 | Connect the new Cisco IP Phone to the network. |
|---|---|
| Step 2 | Select the option 2 to replace an existing phone. Note If the Administrator hasn't configured Activation Code based device onboarding or phone migration is done on the 11.5(1)SU8
                                                         version of Unified Communications Manager which doesn't support activation code, the phone displays the screen to enter the
                                                         primary extension. | Note | If the Administrator hasn't configured Activation Code based device onboarding or phone migration is done on the 11.5(1)SU8
                                                         version of Unified Communications Manager which doesn't support activation code, the phone displays the screen to enter the
                                                         primary extension. |
| Note | If the Administrator hasn't configured Activation Code based device onboarding or phone migration is done on the 11.5(1)SU8
                                                         version of Unified Communications Manager which doesn't support activation code, the phone displays the screen to enter the
                                                         primary extension. |
| Step 3 | Enter the primary extension number of your phone. |
| Step 4 | Enter your PIN . Migration starts after a successful authentication. After successful migration, the phone restarts with configuration settings
                                                migrated from your old phone. Note Consider a scenario where the On-premise Onboarding Method option is selected as Auto registration in the Device Defaults Configuration page. While performing the phone migration, if you press either the EXIT or BACK button when an error message is displayed, it takes you directly to the initial phone migration screen after a possible expected
                                                         delay. This delay is due to the phones trying to re-register to the Unified CM as auto-registration is disabled in the Unified
                                                         Communications Manager server. Note If there are more than one device for the user with the same primary extension, the user will be prompted to choose the device
                                                         to be migrated. For more information, see Phone Migration Service—User Assigned with Multiple Devices . | Note | Consider a scenario where the On-premise Onboarding Method option is selected as Auto registration in the Device Defaults Configuration page. While performing the phone migration, if you press either the EXIT or BACK button when an error message is displayed, it takes you directly to the initial phone migration screen after a possible expected
                                                         delay. This delay is due to the phones trying to re-register to the Unified CM as auto-registration is disabled in the Unified
                                                         Communications Manager server. | Note | If there are more than one device for the user with the same primary extension, the user will be prompted to choose the device
                                                         to be migrated. For more information, see Phone Migration Service—User Assigned with Multiple Devices . |
| Note | Consider a scenario where the On-premise Onboarding Method option is selected as Auto registration in the Device Defaults Configuration page. While performing the phone migration, if you press either the EXIT or BACK button when an error message is displayed, it takes you directly to the initial phone migration screen after a possible expected
                                                         delay. This delay is due to the phones trying to re-register to the Unified CM as auto-registration is disabled in the Unified
                                                         Communications Manager server. |
| Note | If there are more than one device for the user with the same primary extension, the user will be prompted to choose the device
                                                         to be migrated. For more information, see Phone Migration Service—User Assigned with Multiple Devices . |

| Note | If the Administrator hasn't configured Activation Code based device onboarding or phone migration is done on the 11.5(1)SU8
                                                         version of Unified Communications Manager which doesn't support activation code, the phone displays the screen to enter the
                                                         primary extension. |
|---|---|

| Note | Consider a scenario where the On-premise Onboarding Method option is selected as Auto registration in the Device Defaults Configuration page. While performing the phone migration, if you press either the EXIT or BACK button when an error message is displayed, it takes you directly to the initial phone migration screen after a possible expected
                                                         delay. This delay is due to the phones trying to re-register to the Unified CM as auto-registration is disabled in the Unified
                                                         Communications Manager server. |
|---|---|

| Note | If there are more than one device for the user with the same primary extension, the user will be prompted to choose the device
                                                         to be migrated. For more information, see Phone Migration Service—User Assigned with Multiple Devices . |
|---|---|

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

| Note | In Proxy TFTP, after migration, the phone restarts with configuration settings migrated from your old phone. Note that the
                                       phone takes 2 reset cycles to restart after successful migration. |
|---|---|

|  | Device Status Before Phone Migration | Phone Display During Migration |
|---|---|---|
| Scenario 1 | Device 1—Registered Device 2—Unregistered | Phone Configuration settings of Device 2 will be migrated. |
| Scenario 2 | Device 1—Registered Device 2—Registered Device 3—Unregistered | Phone Configuration settings of Device 3 will be migrated. |
| Scenario 3 | Device 1—Registered Device 2—Unregistered Device 3—Unregistered | Displays the device list with the following: Description, Phone Model, and MAC Address. Users should choose the device from
                                             the list required for phone migration. |
| Scenario 4 | Device 1—Unregistered Device 2—Unregistered Device 3—Unregistered | Displays the device list with the following: Description, Phone Model, and MAC Address. Users should choose the device from
                                             the list required for phone migration. |
| Scenario 5 | Device 1—Registered Device 2—Registered Device 3—Registered | Displays the device list with the following: Description, Phone Model, and MAC Address. Users should choose the device from
                                             the list required for phone migration. |
| Scenario 6 | More than 3 devices are in Registered or Unregistered states | Displays the device list with the following: Description, Phone Model, and MAC Address. Users should choose the device from
                                             the list required for phone migration. |

| Phone or Device preconfigured by Administrator | Autoregistration Enabled at Enterprise Level | Onboarding Method at Device Defaults Level | Behavior without Phone Migration Service | Behavior with Phone Migration Service |
|---|---|---|---|---|
| No | Yes | — | Devices get auto registered to the network. | Devices get auto registered to the network. |
| No | No | — | Device retries to register to the network and keeps retrying based on the back-off timer set. | Phone replacement screen prompts to enter the Primary Extension and PIN. |
| Yes | N/A | — | Device registers with the preconfigured settings. | Device registers with the preconfigured settings. |
| No | Yes | Device Type set to Activation Code | Welcome screen of the phone prompts the following: "Enter activation code". | Phone replacement screen prompts to select one of the following: “Provision a new phone” or “Replace an existing phone”. |
| No | No | Device Type set to Auto Registration | Device retries to register to the network and gives up. | Phone replacement screen prompts the following: “Replace an existing phone”. |
| No | No | Device Type set to Activation Code | Welcome screen of the phone prompts the following: "Enter activation code". | Phone replacement screen prompts to select one of the following: “Provision a new phone” or “Replace an existing phone”. |
| Yes | N/A | N/A | Device retries to register to the network and keeps retrying based on the back-off timer set. | Device registers with the preconfigured settings. |

| Note | Native phone migration does not support end-users Extension Mobility Device profile migration. |
|---|---|

| Scenarios | Old Phone  (Model 79xx) | New Phone (Model 88xx) | Expected Behavior After Migration |
|---|---|---|---|
| KEM 1 attached to the old phone is compatible with the new phone. User removes the KEM 1 from the old phone and attaches it with the new phone. | KEM 1 | KEM 1 | KEM 1 configuration settings are carried over. |
| KEM 1 attached to the old phone is incompatible with the new phone. User attaches a compatible KEM 2 (brand new or used) to the new phone. | KEM 1 | KEM 2 | KEM 1 configuration settings are carried over to KEM 2. |
| KEM 1 attached to the old phone is deprecated. User attaches a new KEM 3 to the new phone. | KEM 1 | KEM 3 | KEM 1 configuration settings are carried over to KEM 3. |

| Old Device | Phone Button Template of the Old Device | New Device Selected for Phone Migration | Phone Button Template of the New Device After Phone Migration |
|---|---|---|---|
| Cisco Unified IP Phone 7965 SCCP | Standard 7965 SCCP | Cisco IP Phone 8861 | Standard 8861 SIP |
| Cisco Unified IP Phone 7965 SCCP | Universal Device Template Button layout | Cisco IP Phone 8861 | Universal Device Template Button layout |
| Cisco Unified IP Phone 7965 SCCP | Custom 7965 SCCP | Cisco IP Phone 8861 | Custom 7965 SCCP |
| Cisco Unified IP Phone 8851 SIP | Standard 8851 SIP | Cisco IP Phone 8861 | Standard 8861 SIP |