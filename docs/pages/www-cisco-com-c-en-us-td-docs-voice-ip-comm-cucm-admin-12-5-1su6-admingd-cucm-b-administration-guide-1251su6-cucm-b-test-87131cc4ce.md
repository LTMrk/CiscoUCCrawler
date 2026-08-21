---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-admingd-cucm-b-administration-guide-1251su6-cucm-b-test-87131cc4ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/adminGd/cucm_b_administration-guide-1251su6/cucm_b_test-adminguide_chapter_0100010.html
retrieved_at: 2026-08-21T08:38:19.918946+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6 and 12.5(1)SU7

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6 and 12.5(1)SU7

Updated: April 8, 2025

Chapter: Configure Call Diagnostics and Quality Reporting for Cisco  IP Phones

## Chapter: Configure Call Diagnostics and Quality Reporting for Cisco  IP Phones

# Configure Call Diagnostics and Quality Reporting for Cisco  IP Phones

## Diagnostics and Reporting Overview

Call Diagnostics—Call diagnostics includes generating  Call Management Records (CMR) and voice quality metrics.

Quality Report Tool QRT)—QRT is a voice-quality and general
                                       		  problem-reporting tool for 
                                       		  Cisco Unified IP Phones. This tool allows users to easily and accurately report audio and other
                                       		  general problems with their IP phone.

### Call Diagnostics Overview

You can configure Cisco IP Phones that are running SCCP and SIP to collect call diagnostics. Call diagnostics comprises Call
                                 Management Records (CMR), also called diagnostic records, and voice quality metrics.

Voice quality metrics are enabled by default and supported on most of the Cisco IP Phones. Cisco IP Phones calculate voice
                                 quality metrics based on MOS (Mean Opinion Square) value. Voice quality metrics do not account for noise or distortion, only
                                 frame loss.

The CMR records store information about the quality of the streamed audio of the call. You can configure the Unified Communications
                                 Manager to generate CMRs. This information is useful for post-processing activities such as generating billing records and
                                 network analysis.

### Quality Report
                           	 Tool Overview

The Quality Report Tool (QRT) is a voice-quality and general problem-reporting tool for Cisco IP Phones. This tool allows
                                 users to easily and accurately report audio and other general problems with their IP phone.

As a
                                 		  system administrator, you can enable QRT functionality by configuring and
                                 		  assigning a softkey template to display the QRT softkey on a user IP phone. You
                                 		  can choose from two different user modes, depending on the level of user
                                 		  interaction that you want with QRT. You then define how the feature works in
                                 		  your system by configuring system parameters and setting up Cisco Unified
                                 		  Serviceability tools. You can create, customize, and view phone problem reports
                                 		  by using the QRT Viewer application.

When users experience problems with their IP phones, they can report the type of problem and other relevant statistics by
                                 pressing the QRT softkey on the Cisco IP Phones during the On Hook or Connected call states. Users can then choose the reason code that best describes the problem that is
                                 being reported for the IP phone. A customized phone problem report provides you with the specific information.

QRT attempts to collect the streaming statistics after a user selects
                                 		  the type of problem by pressing the QRT softkey. A call should be active for a
                                 		  minimum of 5 seconds for QRT to collect the streaming statistics.

### Detailed Call Reporting and Billing

The Cisco CDR Analysis and Reporting (CAR) tool generates detailed reports for quality of service, traffic, user call volume,
                                 billing, and gateways. CAR uses data from Call Detail Records (CDRs), Call Management Records (CMRs), and the Unified Communications
                                 Manager database in order to generate reports. The CAR interface can be accessed under the Tools menu of Cisco Unified Serviceability.

CAR is not intended to replace call accounting and billing solutions that third-party companies provide. You can find the
                                 companies that provide these solutions and that are members of the Cisco Technology Developer Program by searching the home
                                 page of the Cisco Developer Community.

For details about how to configure reporting with CAR, refer to the Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager .

### Prerequisites

## Call Diagnostics
                        	 Prerequisites

Check if your
                              		  Cisco Unified IP Phone supports Call Diagnostics.

## Quality Report Tool Prerequisites

Any Cisco  IP Phone that
                              		  includes the following capabilities:

Support for softkey templates

Support for IP phone services

Controllable by CTI

Contains an internal HTTP server

For more information, see the guide for your phone model.

## Diagnostics and Reporting Configuration Task Flow

Step 1

Configure Call Diagnostics

Perform this task to configure Cisco Unified
                                          Communications Manager
                                          to generate CMRs. The CMR records store information about the quality of the streamed audio of the call. For more information
                                          about accessing CMRs, see the Cisco Unified Communications Manager Call Detail Records
                                             Administration Guide .

Voice Quality Metrics are automatically enabled on the Cisco IP Phones. For more information about accessing voice quality
                                          metrics, see the Cisco Unified IP Phone Administration Guide for your phone model.

Step 2

To Configure the Quality Report Tool , perform the following subtasks:

Configure the Quality Report Tool (QRT) so that users who experience problems with their IP phones can report the type of
                                          problem and other relevant statistics by pressing a QRT softkey.

### Configure Call Diagnostics

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server on which the Cisco CallManager service is running.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

In the Clusterwide Parameters (Device - General) area, configure the Call Diagnostics Enabled service parameter. The following options are available:

Disabled —CMRs are not generated.

Enabled Only When CDR Enabled Flag is True —CMRs are generated only when the Call Detail Records (CDR) Enabled Flag service parameter is
                                                   set to True.

Enabled Regardless of CDR Enabled Flag —CMRs are generated regardless of the CDR Enabled Flag
                                                   service parameter
                                                   value.

Generating CMRs without enabling the  CDR Enabled Flag service parameter can cause uncontrolled
                                                         disk space consumption. Cisco recommends that you enable CDRs when CMRs are enabled.

Step 5

Click Save .

### Configure the Quality Report Tool

Configure the Quality Report Tool (QRT) so that users who experience problems with their IP phones can report the type of
                                 problem and other relevant statistics by pressing a QRT softkey.

Step 1

Configure a Softkey Template with the QRT Softkey

Connected Conference

Connected Transfer

Step 2

(Optional) To Associate a QRT Softkey Template with a Common Device Configuration , perform the following subtasks:

- Add a QRT Softkey Template to a Common Device Configuration

- Associate a Common Device Configuration with a Phone

To make the softkey template available to phones, you must complete either this step or the following step. Follow this step
                                             if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly used method for making a softkey template available to
                                             phones.

Step 3

(Optional) Add the QRT Softkey Template to a Phone

Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                             in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                             if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                             softkey assignment.

Step 4

To Configure QRT in Cisco Unified Serviceability , perform the following subtasks:

- Activate the Cisco Extended Functions Service

- Configure Alarms

- Configure Traces

Step 5

(Optional) Configure the Service Parameters for the Quality Report Tool

#### Configure a Softkey Template with the QRT Softkey

Connected Conference

Connected Transfer

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

Perform one of the following steps:

Add a QRT Softkey Template to a Common Device Configuration

Add the QRT Softkey Template to a Phone

#### Associate a QRT Softkey Template with a Common Device Configuration

Optional. There are two ways to associate a softkey template with a phone:

Add the softkey template to the Phone Configuration.

Add the softkey template to the Common Device Configuration.

The procedures in this section describe how to associate the softkey template with a Common Device Configuration. Follow these
                                    procedures if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly
                                    used method for making a softkey template available to phones.

To use the alternative method, see Add the QRT Softkey Template to a Phone .

Step 1

Add a QRT Softkey Template to a Common Device Configuration

Step 2

Associate a Common Device Configuration with a Phone

##### Add a QRT Softkey Template to a Common Device Configuration

###### Before you begin

Configure a Softkey Template with the QRT Softkey

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

###### What to do next

Associate a Common Device Configuration with a Phone

##### Associate a Common Device Configuration with a Phone

###### Before you begin

Add a QRT Softkey Template to a Common Device Configuration

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

#### Add the QRT Softkey Template to a Phone

##### Before you begin

Configure a Softkey Template with the QRT Softkey

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

#### Configure QRT in Cisco Unified Serviceability

Step 1

Activate the Cisco Extended Functions Service

Activate the Cisco Extended Functions Service to provide support for voice-quality features such as the Quality Report Tool.

Step 2

Configure Alarms

Configure alarms for the QRT to log errors in the Application Logs within SysLog Viewer. This function logs alarms, provides
                                                a description of the alarms, and recommended actions. You can access the SysLog Viewer from the Cisco Unified Real-Time Monitoring
                                                Tool.

Step 3

Configure Traces

Configure traces for the QRT to log trace information for your voice application. After configure the information that you
                                                want to include in the trace files for the QRT, you can collect and view trace files by using the Trace and Log Central option
                                                in the Cisco Unified Real-Time Monitoring Tool.

##### Activate the Cisco Extended Functions Service

Activate the Cisco Extended Functions Service to provide support for voice-quality features such as the Quality Report Tool.

Step 1

From Cisco Unified Serviceability , choose Tools > Service
                                                      				  Activation .

Step 2

From the Server drop-down list, choose the 
                                                			 node on which you want to activate
                                                			 the Cisco Extended Functions service.

Step 3

Check the Cisco Extended Functions check box.

Step 4

Click Save .

###### What to do next

Configure Alarms

##### Configure Alarms

Configure alarms for the QRT to log errors in the Application Logs within SysLog Viewer. This function logs alarms, provides
                                       a description of the alarms, and recommended actions. You can access the SysLog Viewer from the Cisco Unified Real-Time Monitoring
                                       Tool.

###### Before you begin

Activate the Cisco Extended Functions Service

Step 1

From the Cisco Unified Serviceability , choose Alarm > Configuration .

Step 2

From the Server drop-down list, choose the 
                                                			 node on which you want to configure
                                                			 alarms.

Step 3

From the Service Group drop-down list, choose CM Services .

Step 4

From the Service drop-down list, choose Cisco Extended Functions .

Step 5

Check the Enable Alarm check box for both Local Syslogs and SDI
                                                			 Trace.

Step 6

From the drop-down list, configure the Alarm Event Level for
                                                			 both Local Syslogs and SDI Trace by choosing one of the following options:

- Emergency —Designates the system as unusable.

- Alert —Indicates that immediate action is needed.

- Critical —The system detects a critical condition.

- Error —Indicates that an error condition is detected.

- Warning —Indicates that a warning condition is detected.

- Notice —Indicates that a normal but significant condition is detected.

- Informational —Indicates only information messages.

- Debug — Indicates detailed event information that Cisco Technical Assistance Center (TAC) engineers use for debugging.

The default value is Error .

Step 7

Click Save .

###### What to do next

Configure Traces

##### Configure Traces

Configure traces for the QRT to log trace information for your voice application. After configure the information that you
                                       want to include in the trace files for the QRT, you can collect and view trace files by using the Trace and Log Central option
                                       in the Cisco Unified Real-Time Monitoring Tool.

###### Before you begin

Configure Alarms

Step 1

From Cisco Unified Serviceability , choose Trace > Configuration .

Step 2

From the Server drop-down list, choose the 
                                                			 node on which you want to configure
                                                			 traces.

Step 3

From the Service Group drop-down list, choose CM Services .

Step 4

From the Service drop-down list, choose Cisco Extended Functions .

Step 5

Check the Trace On check box.

Step 6

From the Debug Trace Level drop-down list, choose one of the following options:

- Error —Traces all error conditions, as well as process and device initialization messages.

- Special —Traces all special conditions and subsystem state transitions that occur during normal operation. Traces call-processing
                                                   events.

- State Transition —Traces all state transition conditions and media layer events that occur during normal operation.

- Significant —Traces all significant conditions, as well as entry and exit points of routines. Not all services use this trace level.

- Entry_exit —Traces all entry and exit conditions, plus low-level debugging information.

- Arbitrary —Traces all Arbitrary conditions plus detailed debugging information.

- Detailed — Traces alarm conditions and events. Used for all traces that are generated in abnormal path. Uses minimum number of CPU
                                                   cycles.

The default value is Error .

Tip

We recommend that you check all the check boxes in this
                                                               						section for troubleshooting purposes.

Step 7

Click Save .

###### What to do next

(Optional) Configure the Service Parameters for the Quality Report Tool

#### Configure the Service Parameters for the Quality Report Tool

Caution

We recommend that you use the default service parameters
                                                			 settings unless the Cisco Technical Assistance Center (TAC) instructs
                                                			 otherwise.

Step 1

From Cisco Unified Communications Manager Administration , choose System > Service
                                                   				  Parameters .

Step 2

Choose the 
                                             			 node where the QRT application
                                             			 resides.

Step 3

Choose the Cisco Extended
                                                			 Functions service.

Step 4

Configure the service parameters. See the Related Topics section for more information about the service parameters and their
                                             configuration options.

Step 5

Click Save .

##### Quality Report
                                 	 Tool Service Parameters

Set
                                                            						  this field to true to display extended menu choices (interview mode).

Set
                                                            						  this field to false to not display extended menu choices (silent mode).

The
                                                            						  recommended default value is false (silent mode).

Set
                                                            						  this field to -1 to poll until the call ends.

Set
                                                            						  this field to 0 to not poll at all.

Set it
                                                            						  to any positive value to poll for that many seconds. Polling stops when the
                                                            						  call ends.

The
                                                            						  recommended default value is -1 (poll until the call ends).

The value
                                                      					 ranges between 30 and 3600. The recommended default value is 30.

Valid
                                                      					 values are between 1 and 10000. The recommended default value is 250.

The
                                                            						  value ranges between 100 and 2000.

The
                                                            						  recommended default value specifies 2000.

Turn on
                                                                  						security by enabling the CTI Manager Connection Security Flag service
                                                                  						parameter. You must restart the Cisco Extended Functions service for the
                                                                  						changes to take effect.

The value
                                                      					 choices are True and False. You must choose True to enable a secure connection
                                                      					 to CTI.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Call Diagnostics | Perform this task to configure Cisco Unified
                                          Communications Manager
                                          to generate CMRs. The CMR records store information about the quality of the streamed audio of the call. For more information
                                          about accessing CMRs, see the Cisco Unified Communications Manager Call Detail Records
                                             Administration Guide . Voice Quality Metrics are automatically enabled on the Cisco IP Phones. For more information about accessing voice quality
                                          metrics, see the Cisco Unified IP Phone Administration Guide for your phone model. |
| Step 2 | To Configure the Quality Report Tool , perform the following subtasks: | Configure the Quality Report Tool (QRT) so that users who experience problems with their IP phones can report the type of
                                          problem and other relevant statistics by pressing a QRT softkey. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which the Cisco CallManager service is running. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . The Service Parameter Configuration window appears. |
| Step 4 | In the Clusterwide Parameters (Device - General) area, configure the Call Diagnostics Enabled service parameter. The following options are available: Disabled —CMRs are not generated. Enabled Only When CDR Enabled Flag is True —CMRs are generated only when the Call Detail Records (CDR) Enabled Flag service parameter is
                                                   set to True. Enabled Regardless of CDR Enabled Flag —CMRs are generated regardless of the CDR Enabled Flag
                                                   service parameter
                                                   value. Note Generating CMRs without enabling the  CDR Enabled Flag service parameter can cause uncontrolled
                                                         disk space consumption. Cisco recommends that you enable CDRs when CMRs are enabled. | Note | Generating CMRs without enabling the  CDR Enabled Flag service parameter can cause uncontrolled
                                                         disk space consumption. Cisco recommends that you enable CDRs when CMRs are enabled. |
| Note | Generating CMRs without enabling the  CDR Enabled Flag service parameter can cause uncontrolled
                                                         disk space consumption. Cisco recommends that you enable CDRs when CMRs are enabled. |
| Step 5 | Click Save . |

| Note | Generating CMRs without enabling the  CDR Enabled Flag service parameter can cause uncontrolled
                                                         disk space consumption. Cisco recommends that you enable CDRs when CMRs are enabled. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Softkey Template with the QRT Softkey | You must configure the On Hook and Connected call states for the QRT Softkey. The following call states are also available: Connected Conference Connected Transfer |
| Step 2 | (Optional) To Associate a QRT Softkey Template with a Common Device Configuration , perform the following subtasks: Add a QRT Softkey Template to a Common Device Configuration Associate a Common Device Configuration with a Phone | (Optional) To make the softkey template available to phones, you must complete either this step or the following step. Follow this step
                                             if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly used method for making a softkey template available to
                                             phones. |
| Step 3 | (Optional) Add the QRT Softkey Template to a Phone | (Optional) Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                             in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                             if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                             softkey assignment. |
| Step 4 | To Configure QRT in Cisco Unified Serviceability , perform the following subtasks: Activate the Cisco Extended Functions Service Configure Alarms Configure Traces |  |
| Step 5 | (Optional) Configure the Service Parameters for the Quality Report Tool | (Optional) |

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
| Step 1 | Add a QRT Softkey Template to a Common Device Configuration |  |
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
| Step 2 | Click Find to display the list of configured phones. |
| Step 3 | Choose the
                                             			 phone to which you want to add the phone button template. |
| Step 4 | In the Phone
                                                				Button Template drop-down list, choose the phone button template
                                             			 that contains the new feature button. |
| Step 5 | Click Save . A
                                             			 dialog box is displayed with a message to press Reset to update the phone settings. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate the Cisco Extended Functions Service | Activate the Cisco Extended Functions Service to provide support for voice-quality features such as the Quality Report Tool. |
| Step 2 | Configure Alarms | Configure alarms for the QRT to log errors in the Application Logs within SysLog Viewer. This function logs alarms, provides
                                                a description of the alarms, and recommended actions. You can access the SysLog Viewer from the Cisco Unified Real-Time Monitoring
                                                Tool. |
| Step 3 | Configure Traces | Configure traces for the QRT to log trace information for your voice application. After configure the information that you
                                                want to include in the trace files for the QRT, you can collect and view trace files by using the Trace and Log Central option
                                                in the Cisco Unified Real-Time Monitoring Tool. |

| Step 1 | From Cisco Unified Serviceability , choose Tools > Service
                                                      				  Activation . |
|---|---|
| Step 2 | From the Server drop-down list, choose the 
                                                			 node on which you want to activate
                                                			 the Cisco Extended Functions service. |
| Step 3 | Check the Cisco Extended Functions check box. |
| Step 4 | Click Save . |

| Step 1 | From the Cisco Unified Serviceability , choose Alarm > Configuration . |
|---|---|
| Step 2 | From the Server drop-down list, choose the 
                                                			 node on which you want to configure
                                                			 alarms. |
| Step 3 | From the Service Group drop-down list, choose CM Services . |
| Step 4 | From the Service drop-down list, choose Cisco Extended Functions . |
| Step 5 | Check the Enable Alarm check box for both Local Syslogs and SDI
                                                			 Trace. |
| Step 6 | From the drop-down list, configure the Alarm Event Level for
                                                			 both Local Syslogs and SDI Trace by choosing one of the following options: Emergency —Designates the system as unusable. Alert —Indicates that immediate action is needed. Critical —The system detects a critical condition. Error —Indicates that an error condition is detected. Warning —Indicates that a warning condition is detected. Notice —Indicates that a normal but significant condition is detected. Informational —Indicates only information messages. Debug — Indicates detailed event information that Cisco Technical Assistance Center (TAC) engineers use for debugging. The default value is Error . |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified Serviceability , choose Trace > Configuration . |
|---|---|
| Step 2 | From the Server drop-down list, choose the 
                                                			 node on which you want to configure
                                                			 traces. |
| Step 3 | From the Service Group drop-down list, choose CM Services . |
| Step 4 | From the Service drop-down list, choose Cisco Extended Functions . |
| Step 5 | Check the Trace On check box. |
| Step 6 | From the Debug Trace Level drop-down list, choose one of the following options: Error —Traces all error conditions, as well as process and device initialization messages. Special —Traces all special conditions and subsystem state transitions that occur during normal operation. Traces call-processing
                                                   events. State Transition —Traces all state transition conditions and media layer events that occur during normal operation. Significant —Traces all significant conditions, as well as entry and exit points of routines. Not all services use this trace level. Entry_exit —Traces all entry and exit conditions, plus low-level debugging information. Arbitrary —Traces all Arbitrary conditions plus detailed debugging information. Detailed — Traces alarm conditions and events. Used for all traces that are generated in abnormal path. Uses minimum number of CPU
                                                   cycles. The default value is Error . Tip We recommend that you check all the check boxes in this
                                                               						section for troubleshooting purposes. | Tip | We recommend that you check all the check boxes in this
                                                               						section for troubleshooting purposes. |
| Tip | We recommend that you check all the check boxes in this
                                                               						section for troubleshooting purposes. |
| Step 7 | Click Save . |

| Tip | We recommend that you check all the check boxes in this
                                                               						section for troubleshooting purposes. |
|---|---|

| Caution | We recommend that you use the default service parameters
                                                			 settings unless the Cisco Technical Assistance Center (TAC) instructs
                                                			 otherwise. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration , choose System > Service
                                                   				  Parameters . |
|---|---|
| Step 2 | Choose the 
                                             			 node where the QRT application
                                             			 resides. |
| Step 3 | Choose the Cisco Extended
                                                			 Functions service. |
| Step 4 | Configure the service parameters. See the Related Topics section for more information about the service parameters and their
                                             configuration options. |
| Step 5 | Click Save . |

| Parameter | Description |
|---|---|
| Display Extended QRT Menu
                                                   				  Choices | Determines whether extended
                                                   				  menu choices are presented to the user. You can choose one of the following
                                                   				  configuration options: Set
                                                            						  this field to true to display extended menu choices (interview mode). Set
                                                            						  this field to false to not display extended menu choices (silent mode). The
                                                            						  recommended default value is false (silent mode). |
| Streaming Statistics
                                                   				  Polling Duration | Determines the duration
                                                   				  that is to be used for polling streaming statistics. You can choose one of the
                                                   				  following configuration options: Set
                                                            						  this field to -1 to poll until the call ends. Set
                                                            						  this field to 0 to not poll at all. Set it
                                                            						  to any positive value to poll for that many seconds. Polling stops when the
                                                            						  call ends. The
                                                            						  recommended default value is -1 (poll until the call ends). |
| Streaming Statistics
                                                   				  Polling Frequency (seconds) | Enter the number of seconds
                                                   				  to wait between each poll. The value
                                                      					 ranges between 30 and 3600. The recommended default value is 30. |
| Maximum No. of Files | Enter the maximum number
                                                   				  of files before the file count restarts and overwrites the old files. Valid
                                                      					 values are between 1 and 10000. The recommended default value is 250. |
| Maximum No. of Lines per
                                                   				  File | Enter the maximum number of
                                                   				  lines in each file before starting the next file: The
                                                            						  value ranges between 100 and 2000. The
                                                            						  recommended default value specifies 2000. |
| CAPF Profile Instance Id
                                                   				  for Secure Connection to CTI Manager | Enter the Instance ID of
                                                   				  the Application CAPF Profile for application user CCMQRTSysUser that the Cisco
                                                   				  Extended Function service will use to open a secure connection to CTI Manager.
                                                   				  You must configure this parameter if CTI Manager Connection Security Flag is
                                                   				  enabled. Note Turn on
                                                                  						security by enabling the CTI Manager Connection Security Flag service
                                                                  						parameter. You must restart the Cisco Extended Functions service for the
                                                                  						changes to take effect. | Note | Turn on
                                                                  						security by enabling the CTI Manager Connection Security Flag service
                                                                  						parameter. You must restart the Cisco Extended Functions service for the
                                                                  						changes to take effect. |
| Note | Turn on
                                                                  						security by enabling the CTI Manager Connection Security Flag service
                                                                  						parameter. You must restart the Cisco Extended Functions service for the
                                                                  						changes to take effect. |
| CTI Manager Connection
                                                   				  Security Flag | Choose whether security for
                                                   				  Cisco Extended Functions service CTI Manager connection is enabled or disabled.
                                                   				  If enabled, Cisco Extended Functions will open a secure connection to CTI
                                                   				  Manager using the Application CAPF Profile configured for the Instance ID for
                                                   				  application user CCMQRTSysUser. The value
                                                      					 choices are True and False. You must choose True to enable a secure connection
                                                      					 to CTI. |

| Note | Turn on
                                                                  						security by enabling the CTI Manager Connection Security Flag service
                                                                  						parameter. You must restart the Cisco Extended Functions service for the
                                                                  						changes to take effect. |
|---|---|