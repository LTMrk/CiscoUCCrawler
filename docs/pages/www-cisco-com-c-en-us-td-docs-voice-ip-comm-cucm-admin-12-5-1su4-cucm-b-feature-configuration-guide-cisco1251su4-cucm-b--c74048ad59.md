---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-feature-configuration-guide-cisco1251su4-cucm-b--c74048ad59
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_feature-configuration-guide-cisco1251su4/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0100100.html
retrieved_at: 2026-08-16T17:00:07.616021+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: July 31, 2025

Chapter: Call Transfer

## Chapter: Call Transfer

# Call Transfer

## Call Transfer Overview

The transfer feature
                           		allows you to redirect a connected call from your phone to another number. After call
                           		transfer, your  call is disconnected and the transferred call is established as a new call connection.

Following are the
                           		different types of call transfers:

Consult
                                    				Transfer and Blind Transfer —In Consult Transfer, a transferring phone user
                                 			 can redirect the caller to a different target address, after consulting with
                                 			 the target phone user that answers the call. That is, the transferring phone
                                 			 user will stay on the call until the target phone user answers the call. In
                                 			 Blind Transfer, the transferring phone user connects the caller to a
                                 			 destination line before the target of the transfer answers the call.

Most phones use hard keys or softkeys for Transfer. Both Consult Transfer and Blind Transfer do not require separate configuration.
                                 The difference between the two types of transfer depends on when the transferring party presses the Transfer button a second time. For a consult transfer, the transferring party presses the Transfer button after the target answers, while for a Blind Transfer, the transferring party presses the Transfer button before the target answers.

For
                                 			 SCCP-initiated blind transfers, Cisco
                                    				Unified Communications Manager provides call progress indications in
                                 			 the form of ring-back to the transferred user.

Transfer On-Hook —In this type of call transfer, the user presses the Transfer softkey, dials the number to which the call will be transferred, and then presses the Transfer softkey again, or simply goes on-hook to complete the transfer operation. You must set the Transfer On-Hook service parameter to True . This service parameter determines whether a call transfer is completed as a result of the user going on-hook after initiating
                                 a transfer operation.

Both Consult
                                 			 Transfer and Blind Transfer use the Transfer On-Hook option.

Direct Transfer —This type of transfer allows a user to join two established calls (the two calls can either be on hold or in the connected
                                 state) into one call and then drop the initiator from the transfer. Direct Transfer does not initiate a consultation call
                                 and does not put the active call on hold. The user uses the DirTrfr softkey to join any two established calls and remove the initiator.

## Call Transfer
                        	 Configuration Task Flow

Step 1

Configure Consult and Blind Transfer

Transfer
                                          				allows you to redirect a single call to a new number with or without consulting
                                          				the transfer recipient. Perform this step to configure Trnsfer as a softkey
                                          				and/or button.

Step 2

Configure Transfer On-Hook

(Optional)
                                          				Transfer On-Hook is an option to complete call transfers. Press Trnsfer, dial
                                          				the number to which the call should be transferred to, and go on-hook to
                                          				complete the transfer. Perform this step to configure the service parameter.

Step 3

Configure Direct Transfer

(Optional)
                                          				Direct Transfer allows you to transfer two calls to each other (without you
                                          				remaining on the line). Perform this step to configure DirTrfr as a softkey
                                          				and/or button.

### Configure Consult and Blind Transfer

Complete one of the task flows depending on whether your phone supports softkey or buttons.

Step 1

Configure a Softkey Template for Transfer

Step 2

Configure Transfer Button

#### Configure a Softkey Template for Transfer

connected

on hold

Use this procedure to make the Trnsfer softkey available:

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

##### What to do next

Associate Transfer Softkey Template with a Common Device Configuration

Associate Transfer Softkey Template with a Phone

##### Associate Transfer
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

To use the
                                       		  alternative method, see Associate Transfer Softkey Template with a Phone .

###### Before you begin

Configure a Softkey Template for Transfer

Step 1

Add Transfer Softkey Template to the Common Device Configuration

Perform this
                                                   				step to add Trnsfer softkey template to the Common Device Configuration.

Step 2

Associate a Common Device Configuration with a Phone

Perform this
                                                   				step to link the Trnsfer softkey Common Device Configuration to a phone.

###### What to do next

Configure Transfer Button

###### Add Transfer
                                    	 Softkey Template to the Common Device Configuration

###### Before you begin

Configure a Softkey Template for Transfer

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

###### Associate a Common
                                    	 Device Configuration with a Phone

###### Before you begin

Add Transfer Softkey Template to the Common Device Configuration

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

##### Associate Transfer
                                 	 Softkey Template with a Phone

Optional . Use this procedure as an alternative to associating the softkey template with the Common Device Configuration. This procedure
                                       also works in conjunction with the Common Device Configuration. You can use it when you need to assign a softkey template
                                       that overrides the assignment in the Common Device Configuration or any other default softkey assignment.

###### Before you begin

Configure a Softkey Template for Transfer

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

#### Configure Transfer Button

The procedures in this section describe how to configure the Transfer button.

Step 1

Configure a Phone Button Template for Transfer

Perform this step to assign Transfer button features to line or speed dial keys.

Step 2

Associate Transfer Button Template with a Phone

Perform this step to configure the Transfer button for a phone.

##### Configure a Phone Button Template for Transfer

Optional . Follow this procedure when you want to assign features to line or speed dial keys.

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

##### Associate Transfer Button Template with a Phone

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

### Configure Transfer
                           	 On-Hook

#### Before you begin

Configure Consult and Blind Transfer

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server on which
                                          			 you want to configure the parameter.

Step 3

From the Service drop-down list, choose the Cisco
                                             				CallManager (Active) service.

Step 4

In the Clusterwide Parameters (Device - Phone) , choose True for the Transfer On-Hook Enabled service parameter.

Step 5

Click Save .

### Configure Direct
                           	 Transfer

Complete one of
                                 		  the task flows depending on whether your phone supports softkey or buttons.

Step 1

Configure a Softkey Template for Direct Transfer

Perform this
                                             				step to add Direct Transfer softkey to template and configure the softkey using
                                             				the Common Device Configuration or phone.

Step 2

Configure Direct Transfer Button

Perform this
                                             				step to add and configure the Direct Transfer button to a phone.

#### Configure a Softkey Template for Direct Transfer

Direct Transfer softkey has the following call states:

Connected

On hold

Use this procedure to make the Direct Transfer softkey available:

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

##### What to do next

Perform one the following procedures:

Associate Direct Transfer Softkey Template with a Common Device Configuration

Associate Direct Transfer Softkey Template with a Phone

##### Associate Direct
                                 	 Transfer Softkey Template with a Common Device Configuration

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

To use the
                                       		  alternative method, see Associate Direct Transfer Softkey Template with a Phone

###### Before you begin

Configure a Softkey Template for Direct Transfer

Step 1

Add Direct Transfer Softkey Template to the Common Device Configuration

Perform this
                                                   				step to add Direct Transfer softkey template to the Common Device
                                                   				Configuration.

Step 2

Associate a Common Device Configuration with a Phone

Perform this
                                                   				step to add Direct Transfer softkey template to the Common Device
                                                   				Configuration.

###### Add Direct Transfer Softkey Template to the Common Device Configuration

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

###### Associate a Common
                                    	 Device Configuration with a Phone

###### Before you begin

Add Direct Transfer Softkey Template to the Common Device Configuration

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

##### Associate Direct
                                 	 Transfer Softkey Template with a Phone

Optional . Use this procedure as an alternative to associating the softkey template with the Common Device Configuration. This procedure
                                       also works in conjunction with the Common Device Configuration. You can use it when you need to assign a softkey template
                                       that overrides the assignment in the Common Device Configuration or any other default softkey assignment.

###### Before you begin

Configure a Softkey Template for Direct Transfer

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

#### Configure Direct Transfer Button

The procedures in this section describe how to configure the Direct Transfer button.

Step 1

Configure Phone Button Template for Direct Transfer

Perform this step to assign Direct Transfer button features to line or speed dial keys.

Step 2

Associate Direct Transfer Button Template with a Phone

Perform this step to configure the Direct Transfer button for a phone.

##### Configure Phone Button Template for Direct Transfer

Optional . Follow this procedure when you want to assign features to line or speed dial keys.

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

##### Associate Direct
                                 	 Transfer Button Template with a Phone

###### Before you begin

Configure Phone Button Template for Direct Transfer

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

## Call Transfer Interactions

Feature

Interaction

Logical
                                          						Partitioning

The
                                          						logical partitioning policy check is performed between the geolocation
                                          						identifier of the device that is acting as a transferred party and the
                                          						geolocation identifier of the device that is acting as a transferred
                                          						destination.

Logical
                                          						partitioning handling takes place in the following circumstances:

When
                                                							 a phone user uses Transfer softkey to transfer the call, the second press of
                                                							 the softkey invokes and processes the Call Transfer feature.

When
                                                							 other transfer mechanisms, such as Direct Transfer, On-Hook Transfer, Hook
                                                							 Flash Transfer, and CTI-application-initiated Transfer results in invoking the
                                                							 Call Transfer feature.

When
                                                							 the transferred and the transferred destination specifies a PSTN participant.

When Cisco Unified Communications Manager uses the
                                                							 geolocation identifier information that associates with the transferred and
                                                							 transferred destination device to perform logical partitioning policy checking.

Before splitting of the primary and secondary calls, and before
                                                							 joining.

Logical
                                          						partitioning handles a denied call as follows:

Sends External Transfer Restricted message to the VoIP phone.

Normal Transfer—For a phone that is running SCCP, the primary
                                                							 call remains on hold, and the consultation call remains active. For a phone
                                                							 that is running SIP, both primary and consultation calls remain on hold and
                                                							 must be resumed manually after the failure.

On-Hook, Hook-Flash and Analog-Phone-Initiated Transfer—Both the
                                                							 primary and secondary calls are cleared by using the cause code=63 "Service or option not available" with a reorder tone from Cisco Unified Communications Manager .

The
                                                							 Number of Transfer Failures perfmon counter is incremented.

Multilevel Precedence and Preemption (MLPP)

When a
                                          						switch initiates a call transfer between two segments that have the same
                                          						precedence level, the segments maintain the precedence level upon transfer.
                                          						When a call transfer is made between call segments that are at different
                                          						precedence levels, the switch that initiates the transfer marks the connection
                                          						at the segment that has the higher precedence level.

Cisco Unified
                                             						  Communications Manager supports this requirement by upgrading the
                                          						precedence level of a call leg that is involved in a Call Transfer operation.
                                          						For example, party A calls party B with Priority precedence level. Party B then
                                          						initiates a transfer to party C and dials the Flash precedence digits when
                                          						dialing. When the transfer is complete, the precedence level of party A gets
                                          						upgraded from Priority to Flash.

The Call
                                          						Transfer feature is enabled automatically when MLPP is enabled, and the phones
                                          						support the Transfer softkey.

The
                                                      						  precedence level upgrade does not work over a trunk device such as an
                                                      						  intercluster trunk (ICT) or a PRI trunk.

## Call Transfer
                        	 Restrictions

Feature

Restriction

Logical
                                       					 Partitioning

Logical
                                       					 partitioning handling does not take place when both the transferred and the
                                       					 transferred destination devices are VoIP phones.

Logical
                                       					 partitioning handling does not take place when geolocation or a geolocation
                                       					 filter is not associated with any device.

External
                                       					 Call Transfer Restrictions

To
                                       					 restrict transfer for external call scenarios, see the “External Call Transfer
                                       					 Restrictions” chapter.

Hunt Pilot

If a call
                                       					 transfer to a hunt pilot is initiated when an announcement is in progress, the
                                       					 call is redirected only after the announcement is complete.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Consult and Blind Transfer | Transfer
                                          				allows you to redirect a single call to a new number with or without consulting
                                          				the transfer recipient. Perform this step to configure Trnsfer as a softkey
                                          				and/or button. |
| Step 2 | Configure Transfer On-Hook | (Optional)
                                          				Transfer On-Hook is an option to complete call transfers. Press Trnsfer, dial
                                          				the number to which the call should be transferred to, and go on-hook to
                                          				complete the transfer. Perform this step to configure the service parameter. |
| Step 3 | Configure Direct Transfer | (Optional)
                                          				Direct Transfer allows you to transfer two calls to each other (without you
                                          				remaining on the line). Perform this step to configure DirTrfr as a softkey
                                          				and/or button. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Softkey Template for Transfer |  |
| Step 2 | Configure Transfer Button |  |

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
| Step 1 | Add Transfer Softkey Template to the Common Device Configuration | Perform this
                                                   				step to add Trnsfer softkey template to the Common Device Configuration. |
| Step 2 | Associate a Common Device Configuration with a Phone | Perform this
                                                   				step to link the Trnsfer softkey Common Device Configuration to a phone. |

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
| Step 1 | Configure a Phone Button Template for Transfer | Perform this step to assign Transfer button features to line or speed dial keys. |
| Step 2 | Associate Transfer Button Template with a Phone | Perform this step to configure the Transfer button for a phone. |

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

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . The Service Parameter Configuration window is displayed. |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which
                                          			 you want to configure the parameter. |
| Step 3 | From the Service drop-down list, choose the Cisco
                                             				CallManager (Active) service. |
| Step 4 | In the Clusterwide Parameters (Device - Phone) , choose True for the Transfer On-Hook Enabled service parameter. |
| Step 5 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Softkey Template for Direct Transfer | Perform this
                                             				step to add Direct Transfer softkey to template and configure the softkey using
                                             				the Common Device Configuration or phone. |
| Step 2 | Configure Direct Transfer Button | Perform this
                                             				step to add and configure the Direct Transfer button to a phone. |

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
| Step 1 | Add Direct Transfer Softkey Template to the Common Device Configuration | Perform this
                                                   				step to add Direct Transfer softkey template to the Common Device
                                                   				Configuration. |
| Step 2 | Associate a Common Device Configuration with a Phone | Perform this
                                                   				step to add Direct Transfer softkey template to the Common Device
                                                   				Configuration. |

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
| Step 1 | Configure Phone Button Template for Direct Transfer | Perform this step to assign Direct Transfer button features to line or speed dial keys. |
| Step 2 | Associate Direct Transfer Button Template with a Phone | Perform this step to configure the Direct Transfer button for a phone. |

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

| Feature | Interaction |
|---|---|
| Logical
                                          						Partitioning | The
                                          						logical partitioning policy check is performed between the geolocation
                                          						identifier of the device that is acting as a transferred party and the
                                          						geolocation identifier of the device that is acting as a transferred
                                          						destination. Logical
                                          						partitioning handling takes place in the following circumstances: When
                                                							 a phone user uses Transfer softkey to transfer the call, the second press of
                                                							 the softkey invokes and processes the Call Transfer feature. When
                                                							 other transfer mechanisms, such as Direct Transfer, On-Hook Transfer, Hook
                                                							 Flash Transfer, and CTI-application-initiated Transfer results in invoking the
                                                							 Call Transfer feature. When
                                                							 the transferred and the transferred destination specifies a PSTN participant. When Cisco Unified Communications Manager uses the
                                                							 geolocation identifier information that associates with the transferred and
                                                							 transferred destination device to perform logical partitioning policy checking. Before splitting of the primary and secondary calls, and before
                                                							 joining. Logical
                                          						partitioning handles a denied call as follows: Sends External Transfer Restricted message to the VoIP phone. Normal Transfer—For a phone that is running SCCP, the primary
                                                							 call remains on hold, and the consultation call remains active. For a phone
                                                							 that is running SIP, both primary and consultation calls remain on hold and
                                                							 must be resumed manually after the failure. On-Hook, Hook-Flash and Analog-Phone-Initiated Transfer—Both the
                                                							 primary and secondary calls are cleared by using the cause code=63 "Service or option not available" with a reorder tone from Cisco Unified Communications Manager . The
                                                							 Number of Transfer Failures perfmon counter is incremented. |
| Multilevel Precedence and Preemption (MLPP) | When a
                                          						switch initiates a call transfer between two segments that have the same
                                          						precedence level, the segments maintain the precedence level upon transfer.
                                          						When a call transfer is made between call segments that are at different
                                          						precedence levels, the switch that initiates the transfer marks the connection
                                          						at the segment that has the higher precedence level. Cisco Unified
                                             						  Communications Manager supports this requirement by upgrading the
                                          						precedence level of a call leg that is involved in a Call Transfer operation.
                                          						For example, party A calls party B with Priority precedence level. Party B then
                                          						initiates a transfer to party C and dials the Flash precedence digits when
                                          						dialing. When the transfer is complete, the precedence level of party A gets
                                          						upgraded from Priority to Flash. The Call
                                          						Transfer feature is enabled automatically when MLPP is enabled, and the phones
                                          						support the Transfer softkey. Note The
                                                      						  precedence level upgrade does not work over a trunk device such as an
                                                      						  intercluster trunk (ICT) or a PRI trunk. | Note | The
                                                      						  precedence level upgrade does not work over a trunk device such as an
                                                      						  intercluster trunk (ICT) or a PRI trunk. |
| Note | The
                                                      						  precedence level upgrade does not work over a trunk device such as an
                                                      						  intercluster trunk (ICT) or a PRI trunk. |

| Note | The
                                                      						  precedence level upgrade does not work over a trunk device such as an
                                                      						  intercluster trunk (ICT) or a PRI trunk. |
|---|---|

| Feature | Restriction |
|---|---|
| Logical
                                       					 Partitioning | Logical
                                       					 partitioning handling does not take place when both the transferred and the
                                       					 transferred destination devices are VoIP phones. Logical
                                       					 partitioning handling does not take place when geolocation or a geolocation
                                       					 filter is not associated with any device. |
| External
                                       					 Call Transfer Restrictions | To
                                       					 restrict transfer for external call scenarios, see the “External Call Transfer
                                       					 Restrictions” chapter. |
| Hunt Pilot | If a call
                                       					 transfer to a hunt pilot is initiated when an announcement is in progress, the
                                       					 call is redirected only after the announcement is complete. |