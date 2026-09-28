---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-cucm-b-feature-configuration-guide-for-cisco1251su3-cuc-bc3e247318
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/cucm_b_feature-configuration-guide-for-cisco1251su3/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_01101.html
retrieved_at: 2026-08-16T17:05:21.108858+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Auto-Attendant

## Chapter: Auto-Attendant

# Auto-Attendant

## Auto-Attendant
                        	 Overview

Auto-Attendant
                              		  allows callers to locate people in your organization without talking to a
                              		  receptionist. You can customize the prompts that are played for the caller.

Auto-Attendant works with Unified Communications Manager to receive calls on specific telephone extensions. The software interacts with the caller and allows the caller to search
                              for and select the extension of the party (in your organization) that the caller is trying to reach.

Auto-Attendant
                              		  provides the following functions:

Answers a call

Plays a
                                    				user-configurable welcome prompt

Plays a main
                                    				menu prompt that asks the caller to perform one of three actions:

Press 0
                                          					 for the operator

Press 1 to
                                          					 enter an extension number

Press 2 to
                                          					 spell by name

If the caller chooses to spell by name (by pressing 2), the system compares the letters that are entered with the names that
                                          are configured to the available extensions. One of the following results can occur:

If a match exists, the system announces a transfer to the matched user and waits for up to 2 seconds for the caller to press
                                                any Dual Tone Multifrequency (DTMF) key to stop the transfer. If the caller does not stop the transfer, the system performs
                                                an explicit confirmation: it prompts the user for confirmation of the name and transfers the call to the primary extension
                                                of that user.

If more than one match occurs, the system prompts the caller to choose the correct extension.

If too many matches occur, the system prompts the caller to enter more characters.

If no match occurs, that is, if the user presses wrong options, the system prompts that the user pressed the wrong options
                                                and prompts the user to press the correct options.

When the
                                    				caller specifies the destination, the system transfers the call.

If the line is
                                    				busy or not in service, the system informs the caller accordingly and replays
                                    				the main menu prompt.

Auto-Attendant solution can be deployed in three different ways as
                              		  follows using different Cisco products that can provide interactive voice
                              		  response functionality.

Auto-Attendant using Cisco Unity Connection (CUC); the most widely used Auto-Attendant solution configuration by customers

Auto-Attendant using Cisco Unified Contact Center Express (Unified CCX)

Auto-Attendant using Cisco Unity Express (CUE)

## Cisco Unity Connection Configuration

The Cisco Unity Connection server provides Automated-Attendant functionality for both external and internal callers. An Auto-Attendant allows callers
                              to be automatically transferred to an extension without the intervention of an operator or receptionist.

Auto-Attendants offer a menu system; it may also allow a caller to reach a live operator by dialing a number, usually "0" . Multiple Auto-Attendants may be implemented to support individual site locations. Within Cisco Unity Connection , an Auto-Attendant is a customized application tree structure that is built by creating and linking multiple Call Handlers
                              together. The Auto-Attendant is defined by entry and exit points, and intermediate routing decisions based on the callers
                              DTMF input choices.

For more information about Auto-Attendant default behavior and examples, see System Administration Guide for Cisco Unity Connection .

### Cisco Unity
                           	 Connection Configuration Task Flow

You can use this task flow to configure auto-attendant using Cisco Unity Connection :

Step 1

Configure CTI Route Point

Step 2

Configure Auto-Attendant System Call Handler

Step 3

Configure Caller Input Option

Step 4

Configure Extension for Operator Call Handler

Step 5

Modify Standard Call Transfer Rule for Operator

Step 6

Update Default System Transfer Restriction Table

#### Configure CTI Route
                              	 Point

Step 1

From Cisco Unified CM Administration, choose Device > CTI Route Point .

Step 2

Click Add
                                                				New .

Step 3

In the Device
                                                				Name field, enter a device name for the route point.

Step 4

From the Device
                                                				Pool drop-down list, choose Default .

Step 5

Click Save .

Step 6

From the Association area, click Line
                                                				[1] - Add a new DN .

Step 7

In the Directory Number field, enter the directory number
                                             			 that matches with the DID of the company.

Step 8

From the Route
                                                				Partition drop-down list, choose the required route partition.

Step 9

From the Call
                                                			 Forward and Call Pickup Settings area, for Forward All , choose the appropriate calling search
                                             			 space and check the Voice
                                                				Mail check box.

Step 10

Click Save .

#### Configure
                              	 Auto-Attendant System Call Handler

Step 1

From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to Call Management and choose System
                                                				Call Handlers .

Step 2

Click Add
                                                				New .

Step 3

In the Display Name field, enter AutoAttendant .

Step 4

In the Extension field, enter the same extension that you
                                             			 provided for the CTI Route Point.

Step 5

Click Save .

Step 6

Edit the
                                             			 required fields and click Save .

#### Configure Caller
                              	 Input Option

Step 1

From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to Call Management and choose System
                                                				Call Handlers .

Step 2

Click AutoAttendant .

Step 3

Choose Edit > Caller
                                                   				  Inputs .

Step 4

In the Key column, click 0 .

Step 5

Click the Call
                                                				Handler radio button, choose Operator from the drop-down list, and click the Attempt Transfer radio button.

Step 6

Click Save .

Step 7

Choose Edit > Caller
                                                   				  Inputs .

Step 8

In the Key column, click 1 .

Step 9

In the Conversation radio button, choose Caller
                                                				System Transfer from the drop-down list.

Step 10

Click Save .

#### Configure
                              	 Extension for Operator Call Handler

Step 1

From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to Call Management and choose System
                                                				Call Handlers .

Step 2

Click Operator .

Step 3

Enter the
                                             			 extension of the operator in the Extension field and click Save .

#### Modify Standard
                              	 Call Transfer Rule for Operator

Step 1

From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to Call Management and choose System
                                                				Call Handlers .

Step 2

Click Operator .

Step 3

From the Edit menu, choose Transfer Rules .

Step 4

Click Standard .

Step 5

In the Transfer Calls to option, click the Extension radio button and enter the configured operator
                                             			 extension number.

Step 6

Click Save .

#### Update Default
                              	 System Transfer Restriction Table

Step 1

From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to System Settings and choose Restriction Tables .

Step 2

Click Default System Transfer .

Step 3

Uncheck the
                                             			 check box in the Blocked column for 6 in the Order column.

Step 4

Click Save .

### Cisco Unity Connection Auto-Attendant Troubleshooting

## Cisco Unified CCX Configuration

Auto-Attendant
                              		  comes standard with the five-seat bundle of Cisco Unified Contact Center
                              		  Express (Unified
                              			 CCX).

For information about the supported versions of Cisco Unified CCX with Unified Communications Manager , see Cisco Collaboration Systems Release Summary Matrix for IP Telephony .

For information about getting started with scripts, see the Cisco Unified Contact Center Express Getting Started with Scripts .

### Cisco Unified CCX
                           	 Prerequisites

Install and
                                       				configure Cisco Unified CCX before you can use Auto-Attendant. Cisco Unified
                                       				CCX controls the software and its connection to the telephony system.

Configure users on Unified Communications Manager .

### Cisco Unified CCX
                           	 Auto-Attendant Task Flow

Auto-Attendant configuration tasks are completed in Cisco Unified Contact Center Express (Unified CCX). To view detailed steps
                                 for the following tasks, see Cisco Unified CCX Administration Guide and the Cisco Unified Contact Center Express Getting Started with Scripts respectively.

#### Before you begin

Learn more about the Auto-Attendant feature by reviewing Auto-Attendant Overview .

Learn more about Cisco UCCX with Auto-Attendant functionality by
                                       				reviewing Cisco Unified CCX Configuration

Review Cisco Unified CCX Prerequisites .

Step 1

Configure
                                          			 Unified CM Telephony call control groups.

The Unified
                                             				CCX system uses Unified CM Telephony call control groups to pool together a
                                             				series of CTI ports, which the system uses to serve calls as they arrive or
                                             				depart from the Unified CCX server.

Step 2

Add a Cisco
                                          			 Media Termination (CMT) dialog control group.

The Cisco
                                             				Media subsystem is a subsystem of the Unified CCX Engine. The Cisco Media
                                             				subsystem manages the CMT media resource. CMT channels are required for Unified
                                             				CCX to be able to play or record media.

The Cisco
                                             				Media subsystem uses dialog groups to organize and share resources among
                                             				applications. A dialog group is a pool of dialog channels in which each channel
                                             				is used to perform dialog interactions with a caller, during which the caller
                                             				responds to automated prompts by pressing buttons on a touch-tone phone.

Caution

All media
                                                         				  termination strings begin with "auto" and contain the same ID as the call control group—not the CMT dialog group.
                                                         				  Perform this procedure if the default media termination is configured and the
                                                         				  ID differs.

Step 3

Configure a
                                          			 Cisco script application.

Step 4

Provision a
                                          			 Unified CM Telephony trigger.

A Unified CM
                                             				Telephony trigger responds to calls that arrive on a specific route point by
                                             				selecting telephony and media resources to serve the call and invoking an
                                             				application script to handle the call.

Step 5

Customize
                                          			 Auto-Attendant.

- Modify an existing
                                             				Auto-Attendant instance

- Configure the
                                             				Auto-Attendant prompts

The Cisco
                                             				Unified CCX Administration page allows you to modify any existing
                                             				Auto-Attendant instance as necessary.

Cisco
                                             				Unified CCX allows you to customize the Auto-Attendant prompts from the Cisco
                                             				Unified CCX Administration Media Configuration window. It allows you to record
                                             				the welcome prompt, configure the welcome prompt, and upload a spoken name.

## Cisco Unity Express Configuration

For information about Auto-Attendant Configuration using Cisco Unity Express, see the "Configuring Auto Attendants" chapter in Cisco Unity Express VoiceMail and Auto Attendant CLI Administrator Guide for 3.0 and Later Versions .

For information about deploying a sample Auto-Attendant script, see "Deployment of sample script aa.aef" chapter in the Getting Started with Cisco Unified IP IVR .

For information about an Auto-Attendant example, see "Auto Attendant Script Example" chapter in the Cisco Unity Express Guide to Writing and Editing Scripts for 7.0 and Later Versions .

### Cisco Unity Express Auto-Attendant Troubleshooting

For information about Auto-Attendant troubleshooting using Cisco Unity Connection , see the "Troubleshooting Cisco Unity Express Automated Attendant" in Excerpts from Cisco IP Communications Express: CallManager Express with Cisco Unity Express .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure CTI Route Point | Perform this
                                          			 task on the Cisco Unified CM Administration. Create a CTI Route Point which
                                          			 maps to the Direct-Inward Dial (DID) number of the company (board number). |
| Step 2 | Configure Auto-Attendant System Call Handler | Call handlers answer calls, greet callers with recorded prompts, provide callers with information and options, route calls,
                                          and take messages. Note You can customize the greeting for the AutoAttendant Call Handler by choosing Edit > Greetings . For more information about customizing greetings, see System Administration Guide for Cisco Unity Connection . | Note | You can customize the greeting for the AutoAttendant Call Handler by choosing Edit > Greetings . For more information about customizing greetings, see System Administration Guide for Cisco Unity Connection . |
| Note | You can customize the greeting for the AutoAttendant Call Handler by choosing Edit > Greetings . For more information about customizing greetings, see System Administration Guide for Cisco Unity Connection . |
| Step 3 | Configure Caller Input Option | Caller input option enables you to designate a single digit to represent a user extension, alternate contact number, call
                                          handler, interview handler, or directory handler. The caller presses a single key during a call handler greeting instead of
                                          entering the full extension, and Cisco Unity Connection responds accordingly. Several different keys configured as caller input options offers the callers a menu of choices in the
                                          call handler greeting. |
| Step 4 | Configure Extension for Operator Call Handler | Configure an
                                          			 extension for the operator to allow callers to speak to an operator during a
                                          			 call handler greeting. |
| Step 5 | Modify Standard Call Transfer Rule for Operator | Modify the
                                          			 Standard Call Transfer Rule to enable the call to be transferred to the
                                          			 operator when the caller presses 0 to speak to an operator. |
| Step 6 | Update Default System Transfer Restriction Table | Update the
                                          			 Default System Transfer restriction table. The Default System Transfer
                                          			 restriction table restricts numbers that can be used for Caller system
                                          			 transfers, which allow unidentified callers to transfer to a number that they
                                          			 specify. |

| Note | You can customize the greeting for the AutoAttendant Call Handler by choosing Edit > Greetings . For more information about customizing greetings, see System Administration Guide for Cisco Unity Connection . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > CTI Route Point . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | In the Device
                                                				Name field, enter a device name for the route point. |
| Step 4 | From the Device
                                                				Pool drop-down list, choose Default . |
| Step 5 | Click Save . The Add
                                                				successful message is displayed. |
| Step 6 | From the Association area, click Line
                                                				[1] - Add a new DN . The Directory Number Configuration window is displayed. |
| Step 7 | In the Directory Number field, enter the directory number
                                             			 that matches with the DID of the company. |
| Step 8 | From the Route
                                                				Partition drop-down list, choose the required route partition. |
| Step 9 | From the Call
                                                			 Forward and Call Pickup Settings area, for Forward All , choose the appropriate calling search
                                             			 space and check the Voice
                                                				Mail check box. |
| Step 10 | Click Save . |

| Step 1 | From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to Call Management and choose System
                                                				Call Handlers . |
|---|---|
| Step 2 | Click Add
                                                				New . The New
                                                				Call Handler window is displayed. |
| Step 3 | In the Display Name field, enter AutoAttendant . |
| Step 4 | In the Extension field, enter the same extension that you
                                             			 provided for the CTI Route Point. |
| Step 5 | Click Save . The Edit
                                                				Call Handler Basics (AutoAttendant) window is displayed. |
| Step 6 | Edit the
                                             			 required fields and click Save . |

| Step 1 | From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to Call Management and choose System
                                                				Call Handlers . |
|---|---|
| Step 2 | Click AutoAttendant . The Edit
                                                				Call Handler Basics (AutoAttendant) window is displayed. |
| Step 3 | Choose Edit > Caller
                                                   				  Inputs . The Caller
                                                				Input window is displayed. |
| Step 4 | In the Key column, click 0 . The Edit
                                                				Caller Input (0) window is displayed. |
| Step 5 | Click the Call
                                                				Handler radio button, choose Operator from the drop-down list, and click the Attempt Transfer radio button. |
| Step 6 | Click Save . The Updated Caller Input status message is displayed. |
| Step 7 | Choose Edit > Caller
                                                   				  Inputs . The Caller
                                                				Input window is displayed. |
| Step 8 | In the Key column, click 1 . The Edit
                                                				Caller Input (0) window is displayed. |
| Step 9 | In the Conversation radio button, choose Caller
                                                				System Transfer from the drop-down list. |
| Step 10 | Click Save . The Updated Caller Input status message is displayed. |

| Step 1 | From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to Call Management and choose System
                                                				Call Handlers . |
|---|---|
| Step 2 | Click Operator . The Edit
                                                				Call Handler Basics (Operator) window is displayed. |
| Step 3 | Enter the
                                             			 extension of the operator in the Extension field and click Save . The Updated Caller Input status message is displayed. |

| Step 1 | From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to Call Management and choose System
                                                				Call Handlers . |
|---|---|
| Step 2 | Click Operator . The Edit
                                                				Call Handler Basics (Operator) window is displayed. |
| Step 3 | From the Edit menu, choose Transfer Rules . The Transfer Rules window is displayed. |
| Step 4 | Click Standard . The Edit
                                                				Transfer Rule (Standard) window is displayed. |
| Step 5 | In the Transfer Calls to option, click the Extension radio button and enter the configured operator
                                             			 extension number. |
| Step 6 | Click Save . |

| Step 1 | From Cisco
                                             			 Unity Connection Administration, from the Cisco Unity Connection tree on the
                                             			 left, navigate to System Settings and choose Restriction Tables . |
|---|---|
| Step 2 | Click Default System Transfer . The Edit
                                                				Restriction Table Basics (Default System Transfer) window is
                                             			 displayed. |
| Step 3 | Uncheck the
                                             			 check box in the Blocked column for 6 in the Order column. |
| Step 4 | Click Save . |

| Note | For information about the supported versions of Cisco Unified CCX with Unified Communications Manager , see Cisco Collaboration Systems Release Summary Matrix for IP Telephony . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure
                                          			 Unified CM Telephony call control groups. | The Unified
                                             				CCX system uses Unified CM Telephony call control groups to pool together a
                                             				series of CTI ports, which the system uses to serve calls as they arrive or
                                             				depart from the Unified CCX server. |
| Step 2 | Add a Cisco
                                          			 Media Termination (CMT) dialog control group. | The Cisco
                                             				Media subsystem is a subsystem of the Unified CCX Engine. The Cisco Media
                                             				subsystem manages the CMT media resource. CMT channels are required for Unified
                                             				CCX to be able to play or record media. The Cisco
                                             				Media subsystem uses dialog groups to organize and share resources among
                                             				applications. A dialog group is a pool of dialog channels in which each channel
                                             				is used to perform dialog interactions with a caller, during which the caller
                                             				responds to automated prompts by pressing buttons on a touch-tone phone. Caution All media
                                                         				  termination strings begin with "auto" and contain the same ID as the call control group—not the CMT dialog group.
                                                         				  Perform this procedure if the default media termination is configured and the
                                                         				  ID differs. | Caution | All media
                                                         				  termination strings begin with "auto" and contain the same ID as the call control group—not the CMT dialog group.
                                                         				  Perform this procedure if the default media termination is configured and the
                                                         				  ID differs. |
| Caution | All media
                                                         				  termination strings begin with "auto" and contain the same ID as the call control group—not the CMT dialog group.
                                                         				  Perform this procedure if the default media termination is configured and the
                                                         				  ID differs. |
| Step 3 | Configure a
                                          			 Cisco script application. | The Unified
                                          			 CCX script applications are applications that are based on scripts created in
                                          			 the Unified CCX Editor. These applications come with every Unified CCX system
                                          			 and executes scripts that are created in the Unified CCX Editor. |
| Step 4 | Provision a
                                          			 Unified CM Telephony trigger. | A Unified CM
                                             				Telephony trigger responds to calls that arrive on a specific route point by
                                             				selecting telephony and media resources to serve the call and invoking an
                                             				application script to handle the call. |
| Step 5 | Customize
                                          			 Auto-Attendant. Modify an existing
                                             				Auto-Attendant instance Configure the
                                             				Auto-Attendant prompts | The Cisco
                                             				Unified CCX Administration page allows you to modify any existing
                                             				Auto-Attendant instance as necessary. Cisco
                                             				Unified CCX allows you to customize the Auto-Attendant prompts from the Cisco
                                             				Unified CCX Administration Media Configuration window. It allows you to record
                                             				the welcome prompt, configure the welcome prompt, and upload a spoken name. |

| Caution | All media
                                                         				  termination strings begin with "auto" and contain the same ID as the call control group—not the CMT dialog group.
                                                         				  Perform this procedure if the default media termination is configured and the
                                                         				  ID differs. |
|---|---|