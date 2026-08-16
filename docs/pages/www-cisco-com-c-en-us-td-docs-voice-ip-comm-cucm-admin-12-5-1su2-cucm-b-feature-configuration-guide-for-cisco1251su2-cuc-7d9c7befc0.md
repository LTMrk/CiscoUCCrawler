---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-cucm-b-feature-configuration-guide-for-cisco1251su2-cuc-7d9c7befc0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_0101010.html
retrieved_at: 2026-08-16T17:12:29.732532+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Privacy

## Chapter: Privacy

# Privacy

## Privacy
                        	 Overview

The Privacy feature
                           		allows you to enable or disable the capability of users with phones that share
                           		the same line (DN) to view call status and to barge into the call. You can
                           		enable or disable privacy for each phone or for all phones. By default, the
                           		system enables privacy for all phones in the cluster.

When the device that
                           		is configured for privacy registers with Cisco
                              		  Unified Communications Manager , the feature button on the phone that
                           		is configured with privacy gets labeled, and the status is indicated through an
                           		icon. If the button has a lamp, it comes on.

When the phone
                           		receives an incoming call, the user makes the call private (so the call
                           		information does not display on the shared line) by pressing the Privacy
                           		feature button. The Privacy feature button toggles between On and Off.

To verify if your
                           		Cisco Unified IP Phone supports Privacy, see the user documentation for your
                           		phone model.

### Privacy on
                           	 Hold

Privacy on Hold
                              		allows you to enable or disable the capability of users with phones that share
                              		the same line (DN) to view call status and retrieve calls on hold.

You can enable or
                              		disable Privacy on Hold for specific phones or all the phones. Privacy on Hold
                              		activates automatically on all private calls when Privacy on Hold is enabled.
                              		By default, the system disables Privacy on Hold for all phones in the cluster.

To activate Privacy
                              		on Hold, users press the Hold softkey or Hold button while on a private call. To return to
                              		the call, users press the Resume softkey. The phone that puts the call on hold
                              		displays the status indicator for a held call; shared lines display the status
                              		indicators for a private and held call.

## Privacy
                        	 Configuration Task Flow

Step 1

Generate a Phone Feature List

Generate a
                                          				report to identify devices that support the Privacy feature.

Step 2

Enable Privacy Cluster-wide

Step 3

Enable Privacy for a Device

Enable Privacy
                                          				for specific devices.

Step 4

Configure Privacy Phone Button Template

Step 5

Associate Privacy Phone Button Template with a Phone

Step 6

Configure Shared Line Appearance

Step 7

(Optional) Configure Privacy on Hold

### Enable
                           	 Privacy Cluster-wide

Perform these steps to enable Privacy by default for the entire cluster.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters .

Step 2

From the Server drop-down list, choose the server that is running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

From the Privacy Setting drop-down list, choose True .

Step 5

Click Save .

### Enable Privacy for  a Device

#### Before you begin

Ensure that the phone model supports Privacy. For more information, see Generate a Phone Feature List .

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Specify search criteria and click Find .

Step 3

Select the phone.

Step 4

From the Privacy drop-down list, select Default .

Step 5

Click Save .

### Configure Privacy
                           	 Phone Button Template

#### Before you begin

Enable Privacy for a Device

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

### Associate Privacy
                           	 Phone Button Template with a Phone

#### Before you begin

Configure Privacy Phone Button Template

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

### Configure Shared
                           	 Line Appearance

#### Before you begin

Associate Privacy Phone Button Template with a Phone

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

To locate a
                                          			 specific phone, enter search criteria and click Find .

Step 3

Choose the
                                          			 phone for which you want to configure shared line appearance.

Step 4

Click Add a
                                             				new DN link in the Association Information area on the left side of
                                          			 the Phone
                                             				Configuration window.

Step 5

Enter the Directory Number and choose the Route
                                             				Partition to which the directory number belongs.

Step 6

Configure the remaining fields in the Directory Number Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 7

Repeat Step 3 to Step 6 for all the phones for which you want to create a shared line appearance.

### Configure Privacy
                           	 on Hold

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters .

Step 2

From the Server drop-down list, choose the server that is running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

Set the Enforce Privacy Setting on Held Calls service parameter to True .

Step 5

Click Save .

## Privacy
                        	 Restrictions

Restriction

Description

CTI

CTI does not support
                                                			 Privacy through APIs that TAPI and JTAPI applications invoke. CTI generates events
                                                			 when Privacy is enabled or disabled from an IP phone by using the Privacy
                                                			 feature button.

CTI does not support
                                                			 Privacy on Hold through APIs that TAPI/JTAPI applications invoke. CTI generates
                                                			 events when a Privacy-enabled call is put on hold and when Privacy gets enabled
                                                			 or disabled on held calls from an IP phone by using the Privacy feature button.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Generate a
                                          				report to identify devices that support the Privacy feature. |
| Step 2 | Enable Privacy Cluster-wide | Enable
                                       			 Privacy by default for all the phones in the cluster. |
| Step 3 | Enable Privacy for a Device | Enable Privacy
                                          				for specific devices. |
| Step 4 | Configure Privacy Phone Button Template | Configure
                                       			 Privacy phone button template for a device. |
| Step 5 | Associate Privacy Phone Button Template with a Phone | Associate the
                                       			 phone button template with a user. |
| Step 6 | Configure Shared Line Appearance | Configure the
                                       			 shared line appearance. |
| Step 7 | (Optional) Configure Privacy on Hold | Configure
                                       			 Privacy on Hold. |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters . The Service
                                             				Parameter Configuration window appears. |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | From the Privacy Setting drop-down list, choose True . |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Specify search criteria and click Find . The phone search results appear. |
| Step 3 | Select the phone. |
| Step 4 | From the Privacy drop-down list, select Default . |
| Step 5 | Click Save . |

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

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . The Find and List Phones window appears. |
|---|---|
| Step 2 | To locate a
                                          			 specific phone, enter search criteria and click Find . A list
                                          			 of phones that match the search criteria is displayed. |
| Step 3 | Choose the
                                          			 phone for which you want to configure shared line appearance. The Phone
                                             				Configuration window is displayed. |
| Step 4 | Click Add a
                                             				new DN link in the Association Information area on the left side of
                                          			 the Phone
                                             				Configuration window. The Directory Number Configuration window appears. |
| Step 5 | Enter the Directory Number and choose the Route
                                             				Partition to which the directory number belongs. |
| Step 6 | Configure the remaining fields in the Directory Number Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 7 | Repeat Step 3 to Step 6 for all the phones for which you want to create a shared line appearance. Note Ensure that
                                                      				you assign the same directory number and route partition to all the phones that
                                                      				are part of the shared line appearance. | Note | Ensure that
                                                      				you assign the same directory number and route partition to all the phones that
                                                      				are part of the shared line appearance. |
| Note | Ensure that
                                                      				you assign the same directory number and route partition to all the phones that
                                                      				are part of the shared line appearance. |

| Note | Ensure that
                                                      				you assign the same directory number and route partition to all the phones that
                                                      				are part of the shared line appearance. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters . The Service
                                             				Parameter Configuration window appears. |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | Set the Enforce Privacy Setting on Held Calls service parameter to True . |
| Step 5 | Click Save . |

| Restriction | Description |
|---|---|
| CTI | CTI does not support
                                                			 Privacy through APIs that TAPI and JTAPI applications invoke. CTI generates events
                                                			 when Privacy is enabled or disabled from an IP phone by using the Privacy
                                                			 feature button. CTI does not support
                                                			 Privacy on Hold through APIs that TAPI/JTAPI applications invoke. CTI generates
                                                			 events when a Privacy-enabled call is put on hold and when Privacy gets enabled
                                                			 or disabled on held calls from an IP phone by using the Privacy feature button. |