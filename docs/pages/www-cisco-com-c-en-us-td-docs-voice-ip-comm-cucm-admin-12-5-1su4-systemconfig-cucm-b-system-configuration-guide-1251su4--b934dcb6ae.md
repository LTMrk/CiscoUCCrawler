---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-systemconfig-cucm-b-system-configuration-guide-1251su4--b934dcb6ae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/systemConfig/cucm_b_system-configuration-guide-1251su4/cucm_mp_cdc129f1_00_configure-self-provisioning12-0.html
retrieved_at: 2026-08-16T17:40:28.377525+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: July 31, 2025

Chapter: Configure Self-Provisioning

## Chapter: Configure Self-Provisioning

# Configure Self-Provisioning

## Self-Provisioning
                        	 Overview

The Self-Provisioning feature helps you provision phones for your network by giving end users the ability to provision their
                           own phones without contacting an administrator. If the system is configured for self-provisioning, and an individual end user
                           is enabled for self-provisioning, then end user can provision a new phone by plugging the phone into the network and follow
                           the specified few prompts. Cisco Unified Communications Manager configures the phone and the phone line by applying pre-configured
                           templates.

Self-provisioning
                           		can be used either by administrators to provision phones on behalf of their end
                           		users, or end users can use self-provisioning to provision their own phones.

Self-provisioning is supported whether the cluster security setting is nonsecure or mixed mode.

### Security
                              		  Modes

You can configure
                              		  self-provisioning in one of two modes:

Secure mode—In
                                    				secure mode, users or administrators must be authenticated in order to access
                                    				self-provisioning. End users can be authenticated against their password or
                                    				PIN. Administrators can enter a pre-configured authentication code.

Non-secure
                                    				mode—In non-secure mode, users or administrators can enter their user ID, or a
                                    				self-provisioning ID, in order to associate the phone to a user account.
                                    				Non-secure mode is not recommended for day-to-day use.

### Configuration
                              		  through Universal Line and Device Templates

Self-provisioning
                              		  uses the universal line template and universal device template configurations
                              		  to configure provisioned phones and phone lines for an end user. When a user
                              		  provisions their own phone, the system references the user profile for that
                              		  user and applies the associated universal line template to the provisioned
                              		  phone line and the universal device template to the provisioned phone.

### Self-Provisioning Phones

When the feature is configured, you can provision a phone by doing the following:

Plug the phone into the network.

Dial the self-provisioning IVR extension.

Follow the prompts to configure the phone, and associate the phone to an end user. Depending on how you have configured self-provisioning,
                                    the end user may to enter the user password, PIN, or an administrative authentication code.

Tip

### Self Provisioning Analog FXS Ports

You can enable self-provisioning on analog FXS ports so that the users can call the self-provisioning IVR and assign their
                              associated DN to that analog port. In addition, for the provisioned phones, the user can unassign the DN associated with the
                              analog voice gateway port and assign it to another user.

Plugin the analog phone in the gateway’s FXS voice port. Since the port is auto-registered or pre configured (manually), the
                                    phone will automatically get DN from the auto-registered pool or assigned DN.

Call Self-Provision IVR from the auto-registered analog device.

Enter Self-Service ID and PIN.

Upon confirmation, the analog device is provisioned using the End User Primary Extension. The auto-registered DN is released
                                          to the pool.

## Self-Provisioning
                        	 Prerequisites

Before your end users can use self-provisioning, your end users be configured with the following items:

Your end users
                                 			 must have a primary extension.

Your end users must be associated to a user profile or feature group template that includes a universal line template, universal
                                 device template. The user profile must be enabled for self-provisioning.

## Self-Provisioning Configuration Task Flow

Step 1

Activate Services for Self-Provisioning

In Cisco Unified Serviceability, activate the Self-Provisioning IVR and CTI Manager services.

Step 2

Enable Autoregistration for Self-Provisioning

Enable autoregistration parameter for self-provisioning

Step 3

Configure CTI Route Point

Configure a CTI route point to handle the self-provisioning IVR service.

Step 4

Assign a Directory Number to the CTI Route Point

Configure the extension that users will dial in order to access the self-provisioning IVR and associate that extension to
                                          the CTI route point.

Step 5

Configure Application User for Self-Provisioning

Configure an application user for the self-provisioning IVR. Associate the CTI route point to the application user.

Step 6

Configure the System for Self-Provisioning

Configure self-provisioning settings for your system, including associating the application user and CTI route point to the
                                          self-provisioning IVR.

Step 7

Enable Self-Provisioning in a User Profile

Enables the users to Self-Provision phones in the user profile to which they are assigned.

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

| Tip | If you are provisioning a large number of phones on behalf of your end users, configure a speed dial on the universal device
                                       template that forwards to the self-provisioning IVR extension. |
|---|---|

| Note | Upon confirmation, the analog device is provisioned using the End User Primary Extension. The auto-registered DN is released
                                          to the pool. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate Services for Self-Provisioning | In Cisco Unified Serviceability, activate the Self-Provisioning IVR and CTI Manager services. |
| Step 2 | Enable Autoregistration for Self-Provisioning | Enable autoregistration parameter for self-provisioning |
| Step 3 | Configure CTI Route Point | Configure a CTI route point to handle the self-provisioning IVR service. |
| Step 4 | Assign a Directory Number to the CTI Route Point | Configure the extension that users will dial in order to access the self-provisioning IVR and associate that extension to
                                          the CTI route point. |
| Step 5 | Configure Application User for Self-Provisioning | Configure an application user for the self-provisioning IVR. Associate the CTI route point to the application user. |
| Step 6 | Configure the System for Self-Provisioning | Configure self-provisioning settings for your system, including associating the application user and CTI route point to the
                                          self-provisioning IVR. |
| Step 7 | Enable Self-Provisioning in a User Profile | Enables the users to Self-Provision phones in the user profile to which they are assigned. |

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