---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-cca637f946
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0101101.html
retrieved_at: 2026-08-16T17:32:40.762175+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Device Profiles and Templates

## Chapter: Device Profiles and Templates

# Device Profiles and Templates

## Device Profiles
                        	 and Templates Overview

This chapter explains how to configure device profiles and templates. For information about configuring specific features,
                              see the Feature Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

### Device
                           	 Profiles

A device profile
                                 		  defines the services, features, and directory numbers that associate with a
                                 		  particular device. You can configure a device profile and then you can assign
                                 		  the user device profile to a user, so that when the user logs in to a device,
                                 		  those features and services are available on that device.

### SIP Profiles for End Points

A SIP profile comprises the set of SIP attributes that are associated with SIP endpoints. SIP profiles include information
                                 such as name, description, timing, retry, call pickup URI, and so on. The profiles contain some standard entries that cannot
                                 be deleted or changed.

### Device Profiles and Templates

Cisco Unified Communications Manager also supports a default device profile. Cisco Unified Communications Manager uses the default device profile whenever a user logs on to a phone model for which no user device profile exists.

### Peer-to-Peer Image
                           	 Distribution

Limits
                                          				congestion on TFTP transfers to centralized TFTP servers.

Eliminates the
                                          				need to manually control firmware upgrades.

Reduces phone
                                          				downtime during upgrades when large numbers of devices are reset
                                          				simultaneously.

In most
                                 		  conditions, the peer firmware sharing feature optimizes firmware upgrades in
                                 		  branch deployment scenarios over bandwidth-limited WAN links.

When the feature
                                 		  is enabled, it allows the phone to discover similar phones on the subnet that
                                 		  are requesting the files that make up the firmware image and to automatically
                                 		  assemble transfer hierarchies on a per-file basis. The individual files that
                                 		  make up the firmware image get retrieved from the TFTP server by only the root
                                 		  phone in the hierarchy and are then rapidly transferred down the transfer
                                 		  hierarchy to the other phones on the subnet using TCP connections.

## Configure Device
                        	 Profiles and Templates Task Flow

Step 1

Configure a Softkey Template on the Default Device Profile

Add the
                                          				default device profile to a softkey template.

Step 2

Associate a Softkey Template with a Common Device Configuration

Optional. To make the softkey template available to phones, you must associate the template to a Common Device Configuration
                                          or directly to a phone. Follow this step if your system uses a common device configuration to apply configuration options
                                          to phones (this is the most commonly used method for making a softkey template available to phones).

For information on how to associate a common device configuration on multiple phones by using the Bulk Administration Tool,
                                                      see the Cisco Unified Communications Manager Bulk Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 3

Associate a Softkey Template with a Phone

Optional. Use
                                          				this procedure either as an alternative to associating the softkey template
                                          				with the common device configuration, or in conjunction with the common device
                                          				configuration. Use this procedure in conjunction with the common device
                                          				configuration if you need assign a softkey template that overrides the
                                          				assignment in the common device configuration or any other default softkey
                                          				assignment.

Step 4

Configure Feature Control Policy Task Flow

Optional. Use
                                          				this procedure as an alternative to configuring softkey templates. Configure
                                          				feature control policies to enable or disable a particular feature and thereby
                                          				control the appearance of softkeys that display on the phone. You can create a
                                          				feature control policy for a group of users that wants to use a common set of
                                          				features. For example, call park and call pickup features are typically used by
                                          				the employees from the sales group and not all the employees in a company. You
                                          				can create a feature control policy that enables only these two features and
                                          				assign that policy to the sales group. After you create a feature control
                                          				policy, you can associate that policy with an individual phone, a group of
                                          				phones, or with all phones in the system.

Step 5

Configure a Phone Button Template

- Associate a Button Template with a Phone

Use this procedure to include default templates for each Cisco IP Phone model. When you add phones, you can assign one of
                                          these templates to the phone or create a template of your own.

Step 6

Configure Device Profile

Configure the
                                          				device profile for any phone model that supports SIP or SCCP.

Step 7

Configure SIP Profiles for Endpoints

To configure
                                          				a new SIP profile for the phone.

Step 8

Configure Default Device Profiles

Configure the
                                          				default device profile for any phone model that supports SIP or SCCP.

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

### Associate a
                           	 Softkey Template with a Common Device Configuration

Optional . There are two ways to associate a softkey template with a phone:

Add the softkey template to the Phone Configuration .

Add the
                                       				softkey template to the Common Device Configuration .

The
                                 		  procedures in this section describe how to associate the softkey template with
                                 		  a Common
                                    			 Device Configuration . Follow these procedures if your system uses a Common
                                    			 Device Configuration to apply configuration options to phones. This
                                 		  is the most commonly used method for making a softkey template available to
                                 		  phones.

To use the alternative method, see the section Associate a Softkey Template with a Phone .

Step 1

Add a Softkey Template to a Common Device Configuration

Step 2

Associate a Common Device Configuration with a Phone

#### Add a Softkey
                              	 Template to a Common Device Configuration

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration .

Step 2

Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                             proceed to the next step.

Click Add New .

Enter a name for the Common Device Configuration in the Name field.

Click Save .

Step 3

Perform the following steps to add the softkey template to an existing Common Device Configuration.

Click Find and enter the search criteria.

Click an existing Common Device Configuration.

Step 4

In the Softkey Template drop-down list, choose the softkey
                                             			 template that contains the softkey that you want to make available.

Step 5

Click Save .

Step 6

Perform one
                                             			 of the following tasks:

- If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices.

- If you created a new Common Device Configuration, associate the configuration with devices and then restart them.

#### Associate a Common Device Configuration with a Phone

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the phone device to add the softkey template.

Step 3

From the Common Device Configuration drop-down list, choose
                                             				  the common device configuration that contains the new softkey template.

Step 4

Click Save .

Step 5

Click Reset to update the phone settings.

### Associate a Softkey Template with a Phone

Optional . Use this procedure as an alternative to associating the softkey template with the Common Device Configuration. This procedure
                                 also works in conjunction with the Common Device Configuration. You can use it when you need to assign a softkey template
                                 that overrides the assignment in the Common Device Configuration or any other default softkey assignment.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to select the phone to add the softkey template.

Step 3

From the Softkey Template drop-down list, choose the template that contains the new softkey.

Step 4

Click Save .

Step 5

Press Reset to update the phone settings.

### Configure Feature Control Policy Task Flow

Step 1

Generate a Phone Feature List

Login to Cisco Unified Reporting and run a phone feature list report to determine which phones support Feature Control Policy.

Step 2

Create a Feature Control Policy

Create a Feature Control Policy for Cisco IP Phones.

Step 3

Perform one of
                                          			 the following tasks:

- Apply Feature Control Policy to a Phone

- Apply Feature Control Policy to a Common Phone Profile

- Apply Feature Control Policy to All Phones

After you create a Feature Control Policy, you must associate that policy to an individual phone, a group of phones, or to
                                             all phones in the system. The Feature Control Policy for an individual phone overrides the clusterwide feature control policy.

For information on how to apply Feature Control Policy on multiple phones by using the Bulk Administration Tool, see the Cisco Unified Communications Manager Bulk Administration Guide .

#### Generate a Phone Feature List

Generate a phone feature list report to determine which devices support the feature that you want to configure.

Step 1

From Cisco Unified Reporting, choose System Reports .

Step 2

From the list of reports, click Unified CM Phone Feature List .

Step 3

Perform one of the following steps:

- Choose Generate New Report (the bar chart icon)  to generate a new report.

- Choose Unified CM Phone Feature List if a report exists.

Step 4

From the Product drop-down list, choose All .

Step 5

Click the name of the feature that you want to configure.

Step 6

Click Submit , to generate the report.

#### Create a  Feature Control Policy

Follow these steps to create a feature control policy. Use this policy to enable or disable a particular feature and hence
                                    control the appearance of softkeys that display on the phone.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Feature Control Policy .

Step 2

Perform one of the following tasks:

To modify the settings for an existing policy, enter search criteria, click Find and choose the policy from the resulting list.

- To add a new policy, click Add New .

Step 3

In the Name field, enter a name for the feature control policy.

Step 4

In the Description field, enter a brief description for the feature control policy.

Step 5

In the Feature Control Section , for each feature listed, choose whether you want to override the system default and enable or disable the setting:

If the feature is enabled by default and you want to disable the setting, check the check box under Override Default and uncheck the check box under Enable Setting .

If the feature is disabled by default and you want to enable the setting, check the check box under Override Default and check the check box under Enable Setting .

Step 6

Click Save .

#### Apply Feature
                              	 Control Policy to a Phone

##### Before you begin

Ensure that the phone model supports Feature Control Policy. For more information, see Generate a Phone Feature List .

Create a Feature Control Policy

Step 1

From Cisco
                                             			 Unified CM Administration, choose Device > Phone .

Step 2

Enter the
                                             			 search criteria and click Find .

Step 3

Choose a phone to which you want to apply a Feature Control Policy.

Step 4

From the Feature Control Policy drop-down list, choose the required Feature Control Policy.

Step 5

Click Save .

Step 6

Click Apply
                                                				Config .

Step 7

Click OK .

#### Apply Feature
                              	 Control Policy to a Common Phone Profile

Common Phone Profiles allow you to configure Feature Control Policy settings and then apply those settings to all the phones
                                    in your network that use that profile.

##### Before you begin

Create a Feature Control Policy

Step 1

From Cisco
                                             			 Unified CM Administration, choose Device > Device
                                                   				  Settings > Common Phone Profile .

Step 2

Enter the
                                             			 search criteria and click Find .

Step 3

Choose a common phone profile to which you want to apply a Feature Control Policy.

Step 4

From the Feature Control Policy drop-down list, choose the required Feature Control Policy.

Step 5

Click Save .

Step 6

Click Apply
                                                				Config .

Step 7

Click OK .

#### Apply Feature
                              	 Control Policy to All Phones

##### Before you begin

Create a Feature Control Policy

Step 1

From Cisco
                                             			 Unified CM Administration, choose System > Enterprise
                                                   				  Parameters .

Step 2

From the Feature Control Policy drop-down list, choose the required Feature Control Policy.

Step 3

Click Save .

Step 4

Click Apply
                                                				Config .

Step 5

Click OK .

### Configure a Phone Button Template

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template .

Step 2

Click Find to display list of supported phone templates.

Step 3

Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step.

Select a default template for the model of phone and click Copy .

In the Phone Button Template Information field, enter a new name for the template.

Click Save .

Step 4

Perform the following steps if you want to add phone buttons to an existing template.

Click Find and enter the search criteria.

Choose an existing template.

Step 5

From the Line drop-down list, choose 
                                          			 feature that you want  to add to the template.

Step 6

Click Save .

Step 7

Perform one
                                          			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them.

### Associate a Button Template with a Phone

#### Before you begin

Configure a Phone Button Template

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to display the list of configured phones.

Step 3

Choose the
                                          			 phone to which you want to add the phone button template.

Step 4

In the Phone
                                             				Button Template drop-down list, choose the phone button template
                                          			 that contains the new feature button.

Step 5

Click Save .

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

### Configure SIP Profiles for Endpoints

Cisco Unified Communications Manager uses SIP
                                 		  profiles to define SIP attributes that are associated with SIP trunks and Cisco
                                 		  Unified IP Phones.

Step 1

In the Cisco
                                             				Unified CM Administration window, choose Device > Device
                                                				  Settings > SIP Profiles .

Step 2

To add a new
                                          			 SIP Profile, click the Add
                                             				New button.

Step 3

Configure the
                                          			 fields in the SIP
                                             				Profile Configuration window. See the online help for more
                                          			 information about the fields and their configuration options.

Step 4

Click Apply
                                             				Config .

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

### Configure
                           	 Peer-to-Peer Image Distribution Feature for Phones

Step 1

In Cisco
                                          			 Unified Communications Manager Administration, choose Device > Phone .

Step 2

In the Find and List Phones window, to select a phone,
                                          			 specify the appropriate filters in the Find
                                             				Phone where field, click Find to retrieve a list of phones, and then select
                                          			 the phone from the list.

Step 3

In the Phone Configuration window, from the Peer
                                             				Firmware Sharing drop-down list in the Product Specific
                                          			 Configuration Layout pane, choose one the following options.

- Enabled (default)—Indicates that the phone supports Peer-to-Peer Image Distribution
                                             				(PPID).

- Disabled —Indicates that the phone does not support
                                             				Peer-to-Peer Image Distribution (PPID).

Step 4

Click Apply
                                             				Config .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Softkey Template on the Default Device Profile | Add the
                                          				default device profile to a softkey template. |
| Step 2 | Associate a Softkey Template with a Common Device Configuration | Optional. To make the softkey template available to phones, you must associate the template to a Common Device Configuration
                                          or directly to a phone. Follow this step if your system uses a common device configuration to apply configuration options
                                          to phones (this is the most commonly used method for making a softkey template available to phones). Note For information on how to associate a common device configuration on multiple phones by using the Bulk Administration Tool,
                                                      see the Cisco Unified Communications Manager Bulk Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Note | For information on how to associate a common device configuration on multiple phones by using the Bulk Administration Tool,
                                                      see the Cisco Unified Communications Manager Bulk Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Note | For information on how to associate a common device configuration on multiple phones by using the Bulk Administration Tool,
                                                      see the Cisco Unified Communications Manager Bulk Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 3 | Associate a Softkey Template with a Phone | Optional. Use
                                          				this procedure either as an alternative to associating the softkey template
                                          				with the common device configuration, or in conjunction with the common device
                                          				configuration. Use this procedure in conjunction with the common device
                                          				configuration if you need assign a softkey template that overrides the
                                          				assignment in the common device configuration or any other default softkey
                                          				assignment. |
| Step 4 | Configure Feature Control Policy Task Flow | Optional. Use
                                          				this procedure as an alternative to configuring softkey templates. Configure
                                          				feature control policies to enable or disable a particular feature and thereby
                                          				control the appearance of softkeys that display on the phone. You can create a
                                          				feature control policy for a group of users that wants to use a common set of
                                          				features. For example, call park and call pickup features are typically used by
                                          				the employees from the sales group and not all the employees in a company. You
                                          				can create a feature control policy that enables only these two features and
                                          				assign that policy to the sales group. After you create a feature control
                                          				policy, you can associate that policy with an individual phone, a group of
                                          				phones, or with all phones in the system. |
| Step 5 | Configure a Phone Button Template Associate a Button Template with a Phone | Use this procedure to include default templates for each Cisco IP Phone model. When you add phones, you can assign one of
                                          these templates to the phone or create a template of your own. |
| Step 6 | Configure Device Profile | Configure the
                                          				device profile for any phone model that supports SIP or SCCP. |
| Step 7 | Configure SIP Profiles for Endpoints | To configure
                                          				a new SIP profile for the phone. |
| Step 8 | Configure Default Device Profiles | Configure the
                                          				default device profile for any phone model that supports SIP or SCCP. |

| Note | For information on how to associate a common device configuration on multiple phones by using the Bulk Administration Tool,
                                                      see the Cisco Unified Communications Manager Bulk Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

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

| Step 1 | Add a Softkey Template to a Common Device Configuration |
|---|---|
| Step 2 | Associate a Common Device Configuration with a Phone |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                             proceed to the next step. Click Add New . Enter a name for the Common Device Configuration in the Name field. Click Save . |
| Step 3 | Perform the following steps to add the softkey template to an existing Common Device Configuration. Click Find and enter the search criteria. Click an existing Common Device Configuration. |
| Step 4 | In the Softkey Template drop-down list, choose the softkey
                                             			 template that contains the softkey that you want to make available. |
| Step 5 | Click Save . |
| Step 6 | Perform one
                                             			 of the following tasks: If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices. If you created a new Common Device Configuration, associate the configuration with devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the phone device to add the softkey template. |
| Step 3 | From the Common Device Configuration drop-down list, choose
                                             				  the common device configuration that contains the new softkey template. |
| Step 4 | Click Save . |
| Step 5 | Click Reset to update the phone settings. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to select the phone to add the softkey template. |
| Step 3 | From the Softkey Template drop-down list, choose the template that contains the new softkey. |
| Step 4 | Click Save . |
| Step 5 | Press Reset to update the phone settings. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Login to Cisco Unified Reporting and run a phone feature list report to determine which phones support Feature Control Policy. |
| Step 2 | Create a Feature Control Policy | Create a Feature Control Policy for Cisco IP Phones. |
| Step 3 | Perform one of
                                          			 the following tasks: Apply Feature Control Policy to a Phone Apply Feature Control Policy to a Common Phone Profile Apply Feature Control Policy to All Phones | After you create a Feature Control Policy, you must associate that policy to an individual phone, a group of phones, or to
                                             all phones in the system. The Feature Control Policy for an individual phone overrides the clusterwide feature control policy. Note For information on how to apply Feature Control Policy on multiple phones by using the Bulk Administration Tool, see the Cisco Unified Communications Manager Bulk Administration Guide . | Note | For information on how to apply Feature Control Policy on multiple phones by using the Bulk Administration Tool, see the Cisco Unified Communications Manager Bulk Administration Guide . |
| Note | For information on how to apply Feature Control Policy on multiple phones by using the Bulk Administration Tool, see the Cisco Unified Communications Manager Bulk Administration Guide . |

| Note | For information on how to apply Feature Control Policy on multiple phones by using the Bulk Administration Tool, see the Cisco Unified Communications Manager Bulk Administration Guide . |
|---|---|

| Step 1 | From Cisco Unified Reporting, choose System Reports . |
|---|---|
| Step 2 | From the list of reports, click Unified CM Phone Feature List . |
| Step 3 | Perform one of the following steps: Choose Generate New Report (the bar chart icon)  to generate a new report. Choose Unified CM Phone Feature List if a report exists. |
| Step 4 | From the Product drop-down list, choose All . |
| Step 5 | Click the name of the feature that you want to configure. |
| Step 6 | Click Submit , to generate the report. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Feature Control Policy . |
|---|---|
| Step 2 | Perform one of the following tasks: To modify the settings for an existing policy, enter search criteria, click Find and choose the policy from the resulting list. To add a new policy, click Add New . The Feature Control Policy Configuration window is displayed. |
| Step 3 | In the Name field, enter a name for the feature control policy. |
| Step 4 | In the Description field, enter a brief description for the feature control policy. |
| Step 5 | In the Feature Control Section , for each feature listed, choose whether you want to override the system default and enable or disable the setting: If the feature is enabled by default and you want to disable the setting, check the check box under Override Default and uncheck the check box under Enable Setting . If the feature is disabled by default and you want to enable the setting, check the check box under Override Default and check the check box under Enable Setting . |
| Step 6 | Click Save . |

| Step 1 | From Cisco
                                             			 Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Enter the
                                             			 search criteria and click Find . A list
                                             			 of phones that are configured on the Cisco
                                                				Unified Communications Manager is displayed. |
| Step 3 | Choose a phone to which you want to apply a Feature Control Policy. |
| Step 4 | From the Feature Control Policy drop-down list, choose the required Feature Control Policy. |
| Step 5 | Click Save . |
| Step 6 | Click Apply
                                                				Config . |
| Step 7 | Click OK . |

| Step 1 | From Cisco
                                             			 Unified CM Administration, choose Device > Device
                                                   				  Settings > Common Phone Profile . |
|---|---|
| Step 2 | Enter the
                                             			 search criteria and click Find . |
| Step 3 | Choose a common phone profile to which you want to apply a Feature Control Policy. |
| Step 4 | From the Feature Control Policy drop-down list, choose the required Feature Control Policy. |
| Step 5 | Click Save . |
| Step 6 | Click Apply
                                                				Config . |
| Step 7 | Click OK . |

| Step 1 | From Cisco
                                             			 Unified CM Administration, choose System > Enterprise
                                                   				  Parameters . |
|---|---|
| Step 2 | From the Feature Control Policy drop-down list, choose the required Feature Control Policy. |
| Step 3 | Click Save . |
| Step 4 | Click Apply
                                                				Config . |
| Step 5 | Click OK . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template . |
|---|---|
| Step 2 | Click Find to display list of supported phone templates. |
| Step 3 | Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step. Select a default template for the model of phone and click Copy . In the Phone Button Template Information field, enter a new name for the template. Click Save . |
| Step 4 | Perform the following steps if you want to add phone buttons to an existing template. Click Find and enter the search criteria. Choose an existing template. |
| Step 5 | From the Line drop-down list, choose 
                                          			 feature that you want  to add to the template. |
| Step 6 | Click Save . |
| Step 7 | Perform one
                                          			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to display the list of configured phones. |
| Step 3 | Choose the
                                          			 phone to which you want to add the phone button template. |
| Step 4 | In the Phone
                                             				Button Template drop-down list, choose the phone button template
                                          			 that contains the new feature button. |
| Step 5 | Click Save . A
                                          			 dialog box is displayed with a message to press Reset to update the phone settings. |

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

| Step 1 | In the Cisco
                                             				Unified CM Administration window, choose Device > Device
                                                				  Settings > SIP Profiles . |
|---|---|
| Step 2 | To add a new
                                          			 SIP Profile, click the Add
                                             				New button. |
| Step 3 | Configure the
                                          			 fields in the SIP
                                             				Profile Configuration window. See the online help for more
                                          			 information about the fields and their configuration options. |
| Step 4 | Click Apply
                                             				Config . |

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

| Step 1 | In Cisco
                                          			 Unified Communications Manager Administration, choose Device > Phone . |
|---|---|
| Step 2 | In the Find and List Phones window, to select a phone,
                                          			 specify the appropriate filters in the Find
                                             				Phone where field, click Find to retrieve a list of phones, and then select
                                          			 the phone from the list. |
| Step 3 | In the Phone Configuration window, from the Peer
                                             				Firmware Sharing drop-down list in the Product Specific
                                          			 Configuration Layout pane, choose one the following options. Enabled (default)—Indicates that the phone supports Peer-to-Peer Image Distribution
                                             				(PPID). Disabled —Indicates that the phone does not support
                                             				Peer-to-Peer Image Distribution (PPID). |
| Step 4 | Click Apply
                                             				Config . |