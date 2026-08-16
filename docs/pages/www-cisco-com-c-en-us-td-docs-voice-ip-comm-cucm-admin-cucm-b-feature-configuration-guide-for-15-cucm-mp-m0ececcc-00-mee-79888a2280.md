---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-mp-m0ececcc-00-mee-79888a2280
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_mp_m0ececcc_00_meet-me-conferencing-12-0.html
retrieved_at: 2026-08-16T16:03:38.103254+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Meet-Me Conferencing

## Chapter: Meet-Me Conferencing

# Meet-Me Conferencing

## Meet-Me Conferencing Overview

Users can use Meet-Me Conferencing to set up or join conferences. A user that sets up a conference is called the conference
                              controller. A user that joins a conference is called a participant.

## Meet-Me
                        	 Conferencing Task Flow

### Before you begin

Refer to the
                                    				configuration documentation which came with your router and check for any
                                    				settings which you may need to configure before proceeding with the Meet-Me
                                    				Conferencing Task Flow.

Step 1

Configure a Softkey Template for Meet-Me Conferencing

Add the
                                          				Meet-Me softkey to a softkey template.

Step 2

To Associate a Softkey Template with a Common Device Configuration ,
                                       			 complete the following subtasks:

- Add a Softkey Template to a Common Device Configuration

- Associate a Common Device Configuration with a Phone

Optional . To make the softkey template available to phones, you must complete either this step or the following step.

Step 3

Common Device
                                       			 Configuration Associate a Softkey Template with a Phone

Optional . Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                          in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                          if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                          softkey assignment.

Step 4

Configure a Meet-Me Conferencing Number

Enable
                                          				advanced conferencing, specify the maximum number of participants, and specify
                                          				when to drop a conference connection.

### Configure a Softkey Template for Meet-Me Conferencing

Use this procedure to make the Meet Me softkey available in the off hook call state.

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

### Associate a Softkey Template with a Common Device Configuration

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

To use the alternative method, see Associate a Softkey Template with a Phone .

#### Before you begin

Configure a Softkey Template for Meet-Me Conferencing

Step 1

Add a Softkey Template to a Common Device Configuration

Step 2

Associate a Common Device Configuration with a Phone

#### Add a Softkey Template to a Common Device Configuration

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

##### Before you begin

Add a Softkey Template to a Common Device Configuration

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

#### Before you begin

Configure a Softkey Template for Meet-Me Conferencing

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

### Configure a
                           	 Meet-Me Conferencing Number

The Cisco Unified
                                 		  Communications Manager administrator provides the Meet-Me conference directory
                                 		  number range to users, so that they can access the feature. The user chooses a
                                 		  directory number from the range that is specified for the Meet-Me Number or
                                 		  Pattern to establish a Meet-Me conference and becomes the conference
                                 		  controller.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Meet-Me Number/Pattern .

Step 2

Enter the
                                          			 appropriate search criteria and click Find .

Step 3

In the list of
                                          			 records, click the link for the record that you want to view.

Step 4

Perform one
                                          			 of the followings tasks:

- To copy a Meet-Me number or
                                             				pattern, click the Meet-Me number or pattern that you want to copy. The Meet-Me Number/Pattern Configuration window appears.
                                             				Click Copy .

To add a
                                                				  Meet-Me Number or Pattern, click the Add New button.

- To update an existing
                                             				Meet-Me Number or Pattern, click the Meet-Me Number or Pattern that you want to
                                             				update.

Step 5

Enter the
                                          			 appropriate settings.

See the
                                             				Related Topics section for information about the fields and their configuration
                                             				options.

Step 6

Click Save .

#### Meet-Me Number and Pattern Settings

Field

Description

Directory Number or Pattern

Enter a Meet-Me number or a range of numbers.

To configure a range, the dash must appear within brackets and
                                                					 follow a digit; for example, to configure the range 1000 to 1050, enter
                                                					 10[0-5]0.

Description

The description can include up to 50 characters in any
                                                					 language, but it cannot include double quotation marks ("), percentage sign (%),
                                                					 ampersand (&), or angle brackets (<>).

Partition

To use a partition to restrict access to the Meet-Me number
                                                					 or pattern, choose the desired partition from the drop-down list box.

If you do not want to restrict access to the Meet-Me
                                                					 number or pattern, choose <None> for the partition.

You can configure the number of partitions that are displayed in
                                                					 this drop-down list box by using the Max List Box Items enterprise parameter.
                                                					 If more partitions exist than the Max List Box Items enterprise parameter
                                                					 specifies, the Find button is displayed next to the drop-down list box. Click the Find button to display the Find and List Partitions window.

To set the maximum list box items, choose System > Enterprise
                                                                  							 Parameters and update the Max List Box Items field
                                                            						under CCMAdmin Parameters.

Make sure that the combination of Meet-Me number or pattern and partition is unique within the Unified Communications Manager cluster.

Minimum Security Level

Choose the minimum Meet-Me conference security level for this
                                                					 Meet-Me number or pattern from the drop-down list box.

Choose Authenticated to block participants with nonsecure phones from joining the conference.

Choose Encrypted to block participants with authenticated or nonsecure phones from joining the conference.

Choose Non Secure to allow all participants to join the conference.

To use this feature, ensure that you have a secure conference
                                                            						bridge that is configured and available.

## Meet-Me Conferencing Restrictions

Unified Communications Manager supports a maximum of 100 simultaneous Meet-Me conferences for each Unified Communications Manager server.

After the maximum number of participants that is specified for that conference is has been exceeded, no other callers can
                              join the conference.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Softkey Template for Meet-Me Conferencing | Add the
                                          				Meet-Me softkey to a softkey template. |
| Step 2 | To Associate a Softkey Template with a Common Device Configuration ,
                                       			 complete the following subtasks: Add a Softkey Template to a Common Device Configuration Associate a Common Device Configuration with a Phone | Optional . To make the softkey template available to phones, you must complete either this step or the following step. |
| Step 3 | Common Device
                                       			 Configuration Associate a Softkey Template with a Phone | Optional . Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                          in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                          if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                          softkey assignment. |
| Step 4 | Configure a Meet-Me Conferencing Number | Enable
                                          				advanced conferencing, specify the maximum number of participants, and specify
                                          				when to drop a conference connection. |

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

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add a Softkey Template to a Common Device Configuration |  |
| Step 2 | Associate a Common Device Configuration with a Phone |  |

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

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Meet-Me Number/Pattern . The Find and List Meet-Me Numbers window appears. |
|---|---|
| Step 2 | Enter the
                                          			 appropriate search criteria and click Find . All
                                          			 matching records are displayed. |
| Step 3 | In the list of
                                          			 records, click the link for the record that you want to view. |
| Step 4 | Perform one
                                          			 of the followings tasks: To copy a Meet-Me number or
                                             				pattern, click the Meet-Me number or pattern that you want to copy. The Meet-Me Number/Pattern Configuration window appears.
                                             				Click Copy . To add a
                                                				  Meet-Me Number or Pattern, click the Add New button. To update an existing
                                             				Meet-Me Number or Pattern, click the Meet-Me Number or Pattern that you want to
                                             				update. |
| Step 5 | Enter the
                                          			 appropriate settings. See the
                                             				Related Topics section for information about the fields and their configuration
                                             				options. |
| Step 6 | Click Save . |

| Field | Description |
|---|---|
| Directory Number or Pattern | Enter a Meet-Me number or a range of numbers. To configure a range, the dash must appear within brackets and
                                                					 follow a digit; for example, to configure the range 1000 to 1050, enter
                                                					 10[0-5]0. |
| Description | The description can include up to 50 characters in any
                                                					 language, but it cannot include double quotation marks ("), percentage sign (%),
                                                					 ampersand (&), or angle brackets (<>). |
| Partition | To use a partition to restrict access to the Meet-Me number
                                                					 or pattern, choose the desired partition from the drop-down list box. If you do not want to restrict access to the Meet-Me
                                                					 number or pattern, choose <None> for the partition. You can configure the number of partitions that are displayed in
                                                					 this drop-down list box by using the Max List Box Items enterprise parameter.
                                                					 If more partitions exist than the Max List Box Items enterprise parameter
                                                					 specifies, the Find button is displayed next to the drop-down list box. Click the Find button to display the Find and List Partitions window. Note To set the maximum list box items, choose System > Enterprise
                                                                  							 Parameters and update the Max List Box Items field
                                                            						under CCMAdmin Parameters. Note Make sure that the combination of Meet-Me number or pattern and partition is unique within the Unified Communications Manager cluster. | Note | To set the maximum list box items, choose System > Enterprise
                                                                  							 Parameters and update the Max List Box Items field
                                                            						under CCMAdmin Parameters. | Note | Make sure that the combination of Meet-Me number or pattern and partition is unique within the Unified Communications Manager cluster. |
| Note | To set the maximum list box items, choose System > Enterprise
                                                                  							 Parameters and update the Max List Box Items field
                                                            						under CCMAdmin Parameters. |
| Note | Make sure that the combination of Meet-Me number or pattern and partition is unique within the Unified Communications Manager cluster. |
| Minimum Security Level | Choose the minimum Meet-Me conference security level for this
                                                					 Meet-Me number or pattern from the drop-down list box. Choose Authenticated to block participants with nonsecure phones from joining the conference. Choose Encrypted to block participants with authenticated or nonsecure phones from joining the conference. Choose Non Secure to allow all participants to join the conference. Note To use this feature, ensure that you have a secure conference
                                                            						bridge that is configured and available. | Note | To use this feature, ensure that you have a secure conference
                                                            						bridge that is configured and available. |
| Note | To use this feature, ensure that you have a secure conference
                                                            						bridge that is configured and available. |

| Note | To set the maximum list box items, choose System > Enterprise
                                                                  							 Parameters and update the Max List Box Items field
                                                            						under CCMAdmin Parameters. |
|---|---|

| Note | Make sure that the combination of Meet-Me number or pattern and partition is unique within the Unified Communications Manager cluster. |
|---|---|

| Note | To use this feature, ensure that you have a secure conference
                                                            						bridge that is configured and available. |
|---|---|