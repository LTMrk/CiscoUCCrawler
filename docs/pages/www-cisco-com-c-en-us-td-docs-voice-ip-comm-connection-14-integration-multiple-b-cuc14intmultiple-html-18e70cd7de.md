---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-integration-multiple-b-cuc14intmultiple-html-18e70cd7de
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/multiple/b_cuc14intmultiple.html
retrieved_at: 2026-08-16T18:28:29.355887+00:00
---

Multiple Phone System Integration Guide for Cisco Unity Connection Release 14

# Multiple Phone System Integration Guide for Cisco Unity Connection Release 14

### Download Options

Updated: March 24, 2021

# Multiple Phone System Integration Guide for Cisco Unity Connection Release 14

## Introduction

This document provides instructions for
                  		integrating multiple phone systems with Cisco Unity Connection, deleting one of
                  		the phone systems that are integrated with Unity Connection, and replacing one
                  		phone system with another phone system in a Unity Connection integration.

## Integration
               	 Tasks

Before doing the following tasks to integrate Cisco Unity Connection with multiple phone systems, confirm that Cisco Unity
                  Connection is ready for the additional integration by completing the applicable tasks in the “ Installing Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/install_upgrade/guide/b_14cuciumg.html .

The following task lists describe the processes for creating,
                  		deleting, and replacing the integration.

### Task List to Create the Multiple Phone System Integrations

Use the following task list to integrate multiple
                     		phone systems with Cisco Unity Connection.

Review the system and equipment requirements
                           			 to confirm that all phone system and Cisco Unity Connection server requirements
                           			 have been met. See the “Requirements”
                              				section on page 3 .

Confirm that the combination of phone systems
                           			 is supported in a multiple phone system integration with Cisco Unity
                           			 Connection. See the “Combination
                              				Limitations for Multiple Phone System Integrations” section on page 3 .

Create the integration. See the “Creating Multiple
                              				Phone System Integrations” section on page 3 .

An additional Cisco Unified CM cluster can be added
                                    			 in Cisco Unity Connection Administration by creating a new phone system, a new
                                    			 port group for the phone system, and new ports for the port group. Each Cisco
                                    			 Unified CM cluster is a separate phone system integration.

Repeat Task 1. through Task 3. for each remaining phone
                           			 system.

While integrating the Cisco Unity Connection with
                                    			 Cisco Unified Call Manager through a Multiple Phone System uncheck the
                                    			 Synchronize guest time to host option for Unified Communications product line
                                    			 in Virtualized environment. This enables the Unified Communications to
                                    			 synchronize with their clock to external NTP servers.

### Task List to
                  	 Delete an Existing Phone System Integration

Use the following task list to delete one of the phone systems
                     		that is integrated with Cisco Unity Connection (for example, to change from two
                     		phone system integrations to a single phone system integration).

Reassign the users who are homed on the phone system that you want to delete to another phone system. Alternatively, delete
                           these users. See the “ Deleting User Accounts ” section of the “Users” chapter of the System Administration Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html

If you reassign users to a new phone system, we recommend that
                                    			 you change the user extensions to the extensions that will be used by the new
                                    			 phone system before deleting the old phone system. Otherwise, users will not be
                                    			 able to access their voice messages.

Delete the phone system integration. See the “Deleting
                              				an Existing Phone System Integration” section on page 4 .Task List to
                           			 Replace an Existing Phone System with a New Phone System

## Requirements

Cisco Unity Connection has the following requirements for
                  		multiple phone system integrations:

All phone system and Unity Connection server requirements have been met. See the applicable Cisco Unity Connection integration
                        guides at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html .

There must be an adequate number of voice messaging ports on the
                        			 Cisco Unity Connection server to connect to connect to the phone systems. This
                        			 number of ports must not exceed the number ports that are enabled by the
                        			 Cisco Unity Connection license files.

All extensions
                        			 must be unique. The dial plans for the phone systems must not overlap.

If overlapping dial plans cannot be avoided, you must install a Unity Connection server for each phone system that has overlapping
                        dial plans, digitally network the servers, and set up dialing domains to accommodate the overlapping dial plans. See the Networking in Cisco Unity Connection Guide Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/networking/guide/b_14cucnetx.html

Unity Connection is installed on a separate server from Cisco
                        			 Unified CM.

Multiple integrations are not supported when Unity Connection is
                        			 installed as Cisco Business Edition—on the same server with Cisco Unified CM.

## Combination Limitations for Multiple Phone System Integrations

Unity Connection has no combination limitations.It supports multiple simultaneous phone system integrations that are limited
                  only by the number of licensed voice messaging ports.

For example, Cisco Unity Connection can be integrated with the following phone systems at one time (a total of 28 phone system
                  integrations):

Seven circuit-switched phone systems through PIMG/TIMG units

Seven Cisco Unified CM phone systems through Skinny Call Control Protocol (SCCP)

Seven QSIG-enabled phone systems through Cisco ISR voice gateways

Seven Cisco Unified CM phone systems through SIP trunk

## Creating Multiple
               	 Phone System Integrations

After ensuring that the Unity Connection server and the phone
                     		  systems are ready for the integration, do the following procedure.

### SUMMARY STEPS

- Integrate one phone system with Cisco Unity Connection. See the applicable Cisco Unity Connection integration guide at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html .

- Repeat Step 1 for the
                     			 remaining phone systems.

- Add applicable new user templates that are assigned to the new
                     			 phone system so that new users can be assigned to the phone system that you
                     			 want.

### DETAILED STEPS

Integrate one phone system with Cisco Unity Connection. See the applicable Cisco Unity Connection integration guide at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html .

You can integrate the phone systems with Unity Connection in any order.

Repeat Step 1 for the
                              			 remaining phone systems.

Add applicable new user templates that are assigned to the new
                              			 phone system so that new users can be assigned to the phone system that you
                              			 want.

For details on adding new user templates, or on selecting a user template when adding a new user, see the “ User Templates ” section of the “User Attributes” chapter of the System Administration Guide for Cisco Unity Connection Release 14 . The guide is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html

## Deleting an
               	 Existing Phone System Integration

If you want to delete an existing phone system integration (for
                     		  example, you have replaced the phone system with which Cisco Unity Connection
                     		  originally integrated), confirm that the following items are deleted or
                     		  associated to another phone system:

Users (including MWI devices and notification devices) who are
                           				associated with the phone system that you want to delete.

To see a list of users associated with the phone system, in
                     		  Cisco Unity Connection Administration, expand Telephony Integrations > Phone System ; select the name of
                     		  the phone system; on the Phone System Basics page, on the Edit menu, select Phone System Associations .

User templates that are associated with the phone system that
                           				you want to delete.

System call handlers that are associated with the phone system
                           				that you want to delete.

Call handler templates that are associated with the phone system
                           				that you want to delete.

If users, user templates, call handlers, MWI devices, or
                     		  notification devices are associated with this phone system, Cisco Unity
                     		  Connection cannot delete the phone system.

When you attempt to delete a phone system that still has these
                     		  items associated with it, a status warning will appear with a link to the
                     		  Delete Phone System Wizard. This wizard will guide you to associate all items
                     		  from the phone system that you want to delete to another phone system.

All users, user templates, call handlers, MWI devices and
                     		  notification devices that are associated with a phone system must be reassigned
                     		  before the phone system can be deleted.

You
                              		  can see a list of users who are associated with a phone system on the Phone
                              		  System Associations page for the phone system. To view Phone System
                              		  Associations page, on the Phone System Basics page, select Phone System Associations on the Edit menu.

It is not necessary to delete the port groups or ports that
                     		  belong to a phone system before deleting the phone system integration. The
                     		  member port groups and ports will be automatically deleted with the phone
                     		  system.

Port groups and ports that do not belong to the phone system
                              		  will not be affected when the phone system integration is deleted.

Do the following steps to Delete an Existing Phone System
                     		  Integration

### SUMMARY STEPS

- Sign in to Cisco Unity Connection Administration.

- In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System .

- On the Search Phone Systems page, check the check box to the
                     			 left of the phone system that you want to delete.

- Select Delete Selected .

- When prompted to confirm that you want to delete the phone
                     			 system, select OK .

- Sign out of Cisco Unity Connection Administration.

### DETAILED STEPS

Sign in to Cisco Unity Connection Administration.

In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System .

On the Search Phone Systems page, check the check box to the
                              			 left of the phone system that you want to delete.

Select Delete Selected .

When prompted to confirm that you want to delete the phone
                              			 system, select OK .

Sign out of Cisco Unity Connection Administration.

Cisco and the Cisco logo are trademarks or registered
                                    				  trademarks of Cisco and/or its affiliates in the U.S. and other countries. To
                                    				  view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks .
                                    				  Third-party trademarks mentioned are the property of their respective owners.
                                    				  The use of the word partner does not imply a partnership relationship between
                                    				  Cisco and any other company. (1110R)

Any Internet Protocol (IP)
                                    				  addresses used in this document are not intended to be actual addresses. Any
                                    				  examples, command display output, and figures included in the document are
                                    				  shown for illustrative purposes only. Any use of actual IP addresses in
                                    				  illustrative content is unintentional and coincidental.

© 2015 Cisco Systems, Inc.
                                    				  All rights reserved.

### This Document Applies to These Products

- Unity Connection Version 14

| Note | An additional Cisco Unified CM cluster can be added
                                    			 in Cisco Unity Connection Administration by creating a new phone system, a new
                                    			 port group for the phone system, and new ports for the port group. Each Cisco
                                    			 Unified CM cluster is a separate phone system integration. |
|---|---|

| Note | While integrating the Cisco Unity Connection with
                                    			 Cisco Unified Call Manager through a Multiple Phone System uncheck the
                                    			 Synchronize guest time to host option for Unified Communications product line
                                    			 in Virtualized environment. This enables the Unified Communications to
                                    			 synchronize with their clock to external NTP servers. |
|---|---|

| Caution | If you reassign users to a new phone system, we recommend that
                                    			 you change the user extensions to the extensions that will be used by the new
                                    			 phone system before deleting the old phone system. Otherwise, users will not be
                                    			 able to access their voice messages. |
|---|---|

| Step 1 | Integrate one phone system with Cisco Unity Connection. See the applicable Cisco Unity Connection integration guide at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html . You can integrate the phone systems with Unity Connection in any order. |
|---|---|
| Step 2 | Repeat Step 1 for the
                              			 remaining phone systems. |
| Step 3 | Add applicable new user templates that are assigned to the new
                              			 phone system so that new users can be assigned to the phone system that you
                              			 want. For details on adding new user templates, or on selecting a user template when adding a new user, see the “ User Templates ” section of the “User Attributes” chapter of the System Administration Guide for Cisco Unity Connection Release 14 . The guide is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html |

| Note | You
                              		  can see a list of users who are associated with a phone system on the Phone
                              		  System Associations page for the phone system. To view Phone System
                              		  Associations page, on the Phone System Basics page, select Phone System Associations on the Edit menu. |
|---|---|

| Note | Port groups and ports that do not belong to the phone system
                              		  will not be affected when the phone system integration is deleted. |
|---|---|

| Step 1 | Sign in to Cisco Unity Connection Administration. |
|---|---|
| Step 2 | In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System . |
| Step 3 | On the Search Phone Systems page, check the check box to the
                              			 left of the phone system that you want to delete. |
| Step 4 | Select Delete Selected . |
| Step 5 | When prompted to confirm that you want to delete the phone
                              			 system, select OK . |
| Step 6 | Sign out of Cisco Unity Connection Administration. Cisco and the Cisco logo are trademarks or registered
                                    				  trademarks of Cisco and/or its affiliates in the U.S. and other countries. To
                                    				  view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks .
                                    				  Third-party trademarks mentioned are the property of their respective owners.
                                    				  The use of the word partner does not imply a partnership relationship between
                                    				  Cisco and any other company. (1110R) Any Internet Protocol (IP)
                                    				  addresses used in this document are not intended to be actual addresses. Any
                                    				  examples, command display output, and figures included in the document are
                                    				  shown for illustrative purposes only. Any use of actual IP addresses in
                                    				  illustrative content is unintentional and coincidental. © 2015 Cisco Systems, Inc.
                                    				  All rights reserved. |