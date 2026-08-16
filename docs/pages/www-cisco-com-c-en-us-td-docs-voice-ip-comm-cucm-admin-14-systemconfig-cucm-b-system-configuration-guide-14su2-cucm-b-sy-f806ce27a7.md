---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14-systemconfig-cucm-b-system-configuration-guide-14su2-cucm-b-sy-f806ce27a7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14/systemConfig/cucm_b_system-configuration-guide-14su2/cucm_b_system-configuration-guide-14_chapter_011101.html
retrieved_at: 2026-08-16T16:33:41.231297+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: August 7, 2026

Chapter: Configure Endpoints

## Chapter: Configure Endpoints

# Configure Endpoints

## Endpoint Provisioning Defaults

Use the information in this part to configure endpoint devices, and how to associate users with endpoints.

Unified Communications Manager contains a set of device defaults that you can provision prior to adding endpoints. If you
                           set these device default settings beforehand, when you provision new users and devices will be configured automatically based
                           on the settings that are applied.

Following are the two default configurations for endpoints provisioning:

Configure Device Defaults

Configure Enterprise Phone Settings

## Endpoint Provisioning Default Prerequisites

Confirm the ports that are configured for endpoint registrations.  From Cisco Unified CM Administration, go to System > Cisco Unified CM , select the server and confirm the configured port settings.

## Endpoint Provisioning Defaults Task Flow

Complete the following task flows to configure devices for your system.

Step 1

Configure Device Defaults

You can change the default settings that are applied to devices that auto-register with a Unified Communications Manager node.
                                          Each type of device has a specific set of defaults.

Step 2

Configure Device Profile

Optional . You can configure a device profile comprises the set of attributes that associate with a particular device for a user.

Step 3

Configure Default Device Profiles

You can configure a default device profile that a phone takes whenever a user logs into a phone for which that user does not
                                          have a user device profile.

Step 4

Configure a Softkey Template on the Default Device Profile

Optional . You can add the default device profile to a softkey template.

Step 5

Configure Enterprise Phone

You can configure the basic enterprise phone settings that apply to all phones in the same cluster.

## Configure Device Defaults

### Update Device Default Settings

#### Before you begin

Before updating the device default settings, perform any of the following tasks that apply to your system.

Add new firmware files for the devices to the TFTP server.

If you use device defaults to assign a firmware load that does not exist in the directory, those devices will fail to load
                                       the assigned firmware.

Configure new device pools. If the device is a phone, configure new phone templates.

Step 1

In Cisco Unified CM Administration, select Device > Device Settings > Device Defaults .

Step 2

In the Device Defaults Configuration window, modify the applicable settings for the type of device that you want to update, then click Save . For field descriptions, see the online help.

Load Information

Device Pool

Phone Template

Step 3

Click the Reset icon that appears to the left of the device name to reset all the devices of that type and load the new defaults to all devices
                                          of that type on all nodes in the cluster.

If you do not reset all devices, then only new devices that auto-register on the node are configured with  the updated default
                                             values.

### Configure Default Device Profiles

The phone takes on
                                 		  the default device profile whenever a user logs into a phone for which that
                                 		  user does not have a user device profile.

A default device
                                 		  profile includes device type (phone), user locale, phone button template,
                                 		  softkey template, and multilevel precedence and preemption (MLPP) information.

Step 1

From the Cisco
                                             				Unified CM Administration window, choose Device > Device
                                                				  Settings > Default Device Profile .

Step 2

In the Default Device Profile Configuration window,
                                          			 from the Device
                                             				Profile Type drop-down list, choose the appropriate Cisco Unified
                                          			 IP Phone.

Step 3

Click Next .

Step 4

From the Device
                                             				Protocol drop-down list, choose the appropriate protocol.

Step 5

Click Next .

Step 6

Configure the
                                          			 fields in the Default Device Profile Configuration window. See the online help for
                                          			 more information about the fields and their configuration options.

Step 7

Click Save .

### Configure a
                           	 Softkey Template on the Default Device Profile

Cisco Unified
                                    			 Communications Manager includes standard softkey templates for call
                                 		  processing and applications. When creating custom softkey templates, copy the
                                 		  standard templates and make modifications as required.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template .

Step 2

Perform the following steps to create a new softkey template; otherwise, proceed to the next step.

Click Add New .

Select a default template and click Copy .

Enter a new name for the template in the Softkey Template Name field.

Click Save .

Step 3

Perform the following steps to add softkeys to an existing template.

Click Find and enter the search criteria.

Select the required existing template.

Step 4

Check the Default Softkey Template check box to designate this softkey template as the default softkey template.

If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation.

Step 5

Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                          			 corner and click Go .

Step 6

From the Select
                                             				a Call State to Configure drop-down list, choose the call state for
                                          			 which you want the softkey to display.

Step 7

From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                          			 to change the position of the new softkey.

Step 8

Repeat the previous step to display the softkey in additional call states.

Step 9

Click Save .

Step 10

Perform one
                                          			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                             see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections.

#### What to do next

You can apply a customized softkey template to a device by selecting the template from the Softkey Template drop-down in one
                                 of the following configuration windows:

Phone Configuration

Universal Device Template

BAT Template

Common Device Configuration

Device Profile

Default Device Profile

UDP Profile

### Configure Device
                           	 Profile

A device profile comprises the set of attributes that associate with a particular device. You can associate the device profile
                                 that you create to an end user in order to use the Cisco Extension Mobility feature.

Step 1

From the Cisco
                                             				Unified CM Administration window, choose Device > Device
                                                				  Settings > Device Profile .

Step 2

In the Device Profile Configuration window, from the Device
                                             				Profile Type drop-down list, choose the appropriate Cisco Unified
                                          			 IP Phone.

Step 3

Click Next .

Step 4

From the Device
                                             				Protocol drop-down list, choose the appropriate protocol.

Step 5

Click Next .

Step 6

From the Phone Button Template drop-down list, choose a template.

Step 7

(Optional) From the Softkey Template drop-down list, select a softkey template.

Step 8

Configure the
                                          			 fields in the Device
                                             				Profile Configuration window. See the online help for more
                                          			 information about the fields and their configuration options.

Step 9

Click Save .

For details on using Device Profiles to setup Cisco Extension Mobility, see the Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1 .

## Configure Enterprise Phone

### Configure Enterprise Phone Settings

Parameters that you set in this window may also appear in the Common Phone Profile Configuration window and in the Phone Configuration
                                 window for various devices. If you set these same parameters in these other windows too, the following order determines the
                                 setting that takes precedence: 1) Phone Configuration window settings, 2) Common Phone Profile window settings, 3) Enterprise
                                 Phone Configuration window settings.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Phone Configuration .

Step 2

Enter the required fields in the Product Specific Configuration Layout section.

To view the descriptions of all enterprise phone parameters, click the ? button in the Enterprise Phone Parameters Configuration
                                             window.

Step 3

Complete the remaining fields in the Enterprise Phone Configuration window. For help with the fields and their settings, see
                                          the online help.

### Configure a Phone

Perform these steps to manually add the phone to the Unified Communications Manager database. You do not have to perform these
                                 steps if you are using autoregistration. If you opt for autoregistration, Unified Communications Manager automatically adds
                                 the phone and assigns the directory number.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Add New .

Step 3

From the Phone Type drop-down list, select the appropriate Cisco IP Phone model.

Step 4

Click Next .

Step 5

From the Select the device protocol drop-down list, choose one of the following:

- SCCP

- SIP

Step 6

Click Next .

Step 7

Configure the fields in the Phone Configuration window. See the online help for more information about the fields and their configuration options.

The CAPF settings that are configured in the security profile relate to the Certificate Authority Proxy Function settings
                                                         that display in the Phone Configuration window. You must configure CAPF settings for certificate operations that involve manufacturer-installed
                                                         certificates (MICs) or locally significant certificates (LSC). See the Cisco Unified Communications Manager Security Guide
                                                         for more information about how CAPF settings that you update in the phone configuration window affect security profile CAPF
                                                         settings.

Step 8

Click Save .

Step 9

In the Association area, click Line [1] - Add a new DN .

Step 10

In the Directory Number field, enter the directory number that you want to associate with the phone.

Step 11

Click Save .

### Configure Cisco IP Phone Services

#### Before you begin

Configure a Phone

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Services .

Step 2

Click Add New .

Step 3

Configure the fields in the IP Phone Services Configuration window. See the online help for more information about the fields and their configuration options.

Step 4

Click Save .

#### What to do next

Add services to the phones in the database if they are not classified as enterprise subscriptions. You can add services to
                                       the phones using Bulk Administration Tool (BAT) or Cisco Unified Communications Self Care Portal. For more information, see Cisco Unified Communications Manager Bulk Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html and Cisco Unified Communications Self Care Portal User Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-user-guide-list.html .

You can assign the services to the phone buttons, if the phone model supports these buttons. For more information about assigning
                                       services, see the Cisco IP Phone User Guide for your phone model.

Configure VPN Client (optional).

## Self Care Portal

The Self Care Portal can be used as part of the deployment process for provisioning and configuring new phones:

End users can use the portal to customize features and settings for their phones.

With Device Activation Code Onboarding, users have the option to use the portal to activate their phones.

Users can also use the portal to self-provision their own Single Number Reach remote destinations.

End users need to be set up with access before they can use the portal. For details on how to set up the portal, go to the
                              “Self Care Portal’ chapter of the Feature Configuration Guide for Cisco Unified Communications Manager .

| Note | In most cases, there is no need to change the ports from their default settings. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Device Defaults | You can change the default settings that are applied to devices that auto-register with a Unified Communications Manager node.
                                          Each type of device has a specific set of defaults. |
| Step 2 | Configure Device Profile | Optional . You can configure a device profile comprises the set of attributes that associate with a particular device for a user. |
| Step 3 | Configure Default Device Profiles | You can configure a default device profile that a phone takes whenever a user logs into a phone for which that user does not
                                          have a user device profile. |
| Step 4 | Configure a Softkey Template on the Default Device Profile | Optional . You can add the default device profile to a softkey template. |
| Step 5 | Configure Enterprise Phone | You can configure the basic enterprise phone settings that apply to all phones in the same cluster. |

| Step 1 | In Cisco Unified CM Administration, select Device > Device Settings > Device Defaults . |
|---|---|
| Step 2 | In the Device Defaults Configuration window, modify the applicable settings for the type of device that you want to update, then click Save . For field descriptions, see the online help. Load Information Device Pool Phone Template |
| Step 3 | Click the Reset icon that appears to the left of the device name to reset all the devices of that type and load the new defaults to all devices
                                          of that type on all nodes in the cluster. If you do not reset all devices, then only new devices that auto-register on the node are configured with  the updated default
                                             values. |

| Step 1 | From the Cisco
                                             				Unified CM Administration window, choose Device > Device
                                                				  Settings > Default Device Profile . |
|---|---|
| Step 2 | In the Default Device Profile Configuration window,
                                          			 from the Device
                                             				Profile Type drop-down list, choose the appropriate Cisco Unified
                                          			 IP Phone. |
| Step 3 | Click Next . |
| Step 4 | From the Device
                                             				Protocol drop-down list, choose the appropriate protocol. |
| Step 5 | Click Next . |
| Step 6 | Configure the
                                          			 fields in the Default Device Profile Configuration window. See the online help for
                                          			 more information about the fields and their configuration options. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template . |
|---|---|
| Step 2 | Perform the following steps to create a new softkey template; otherwise, proceed to the next step. Click Add New . Select a default template and click Copy . Enter a new name for the template in the Softkey Template Name field. Click Save . |
| Step 3 | Perform the following steps to add softkeys to an existing template. Click Find and enter the search criteria. Select the required existing template. |
| Step 4 | Check the Default Softkey Template check box to designate this softkey template as the default softkey template. Note If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. | Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
| Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
| Step 5 | Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                          			 corner and click Go . |
| Step 6 | From the Select
                                             				a Call State to Configure drop-down list, choose the call state for
                                          			 which you want the softkey to display. |
| Step 7 | From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                          			 to change the position of the new softkey. |
| Step 8 | Repeat the previous step to display the softkey in additional call states. |
| Step 9 | Click Save . |
| Step 10 | Perform one
                                          			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                             see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections. |

| Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
|---|---|

| Step 1 | From the Cisco
                                             				Unified CM Administration window, choose Device > Device
                                                				  Settings > Device Profile . |
|---|---|
| Step 2 | In the Device Profile Configuration window, from the Device
                                             				Profile Type drop-down list, choose the appropriate Cisco Unified
                                          			 IP Phone. |
| Step 3 | Click Next . |
| Step 4 | From the Device
                                             				Protocol drop-down list, choose the appropriate protocol. |
| Step 5 | Click Next . |
| Step 6 | From the Phone Button Template drop-down list, choose a template. |
| Step 7 | (Optional) From the Softkey Template drop-down list, select a softkey template. |
| Step 8 | Configure the
                                          			 fields in the Device
                                             				Profile Configuration window. See the online help for more
                                          			 information about the fields and their configuration options. |
| Step 9 | Click Save . Note For details on using Device Profiles to setup Cisco Extension Mobility, see the Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1 . | Note | For details on using Device Profiles to setup Cisco Extension Mobility, see the Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1 . |
| Note | For details on using Device Profiles to setup Cisco Extension Mobility, see the Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1 . |

| Note | For details on using Device Profiles to setup Cisco Extension Mobility, see the Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1 . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Phone Configuration . |
|---|---|
| Step 2 | Enter the required fields in the Product Specific Configuration Layout section. To view the descriptions of all enterprise phone parameters, click the ? button in the Enterprise Phone Parameters Configuration
                                             window. |
| Step 3 | Complete the remaining fields in the Enterprise Phone Configuration window. For help with the fields and their settings, see
                                          the online help. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Phone Type drop-down list, select the appropriate Cisco IP Phone model. |
| Step 4 | Click Next . |
| Step 5 | From the Select the device protocol drop-down list, choose one of the following: SCCP SIP |
| Step 6 | Click Next . |
| Step 7 | Configure the fields in the Phone Configuration window. See the online help for more information about the fields and their configuration options. Note The CAPF settings that are configured in the security profile relate to the Certificate Authority Proxy Function settings
                                                         that display in the Phone Configuration window. You must configure CAPF settings for certificate operations that involve manufacturer-installed
                                                         certificates (MICs) or locally significant certificates (LSC). See the Cisco Unified Communications Manager Security Guide
                                                         for more information about how CAPF settings that you update in the phone configuration window affect security profile CAPF
                                                         settings. | Note | The CAPF settings that are configured in the security profile relate to the Certificate Authority Proxy Function settings
                                                         that display in the Phone Configuration window. You must configure CAPF settings for certificate operations that involve manufacturer-installed
                                                         certificates (MICs) or locally significant certificates (LSC). See the Cisco Unified Communications Manager Security Guide
                                                         for more information about how CAPF settings that you update in the phone configuration window affect security profile CAPF
                                                         settings. |
| Note | The CAPF settings that are configured in the security profile relate to the Certificate Authority Proxy Function settings
                                                         that display in the Phone Configuration window. You must configure CAPF settings for certificate operations that involve manufacturer-installed
                                                         certificates (MICs) or locally significant certificates (LSC). See the Cisco Unified Communications Manager Security Guide
                                                         for more information about how CAPF settings that you update in the phone configuration window affect security profile CAPF
                                                         settings. |
| Step 8 | Click Save . |
| Step 9 | In the Association area, click Line [1] - Add a new DN . |
| Step 10 | In the Directory Number field, enter the directory number that you want to associate with the phone. |
| Step 11 | Click Save . |

| Note | The CAPF settings that are configured in the security profile relate to the Certificate Authority Proxy Function settings
                                                         that display in the Phone Configuration window. You must configure CAPF settings for certificate operations that involve manufacturer-installed
                                                         certificates (MICs) or locally significant certificates (LSC). See the Cisco Unified Communications Manager Security Guide
                                                         for more information about how CAPF settings that you update in the phone configuration window affect security profile CAPF
                                                         settings. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Services . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Configure the fields in the IP Phone Services Configuration window. See the online help for more information about the fields and their configuration options. |
| Step 4 | Click Save . |