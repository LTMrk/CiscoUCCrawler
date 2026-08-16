---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-2feabf8f22
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_0110.html
retrieved_at: 2026-08-16T21:15:25.789086+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: Deployment of Sample Script aa.aef

## Chapter: Deployment of Sample Script aa.aef

# Deployment of Sample Script aa.aef

## Cisco Unified CM AutoAttendant Overview

The Cisco Unified CM AutoAttendant works with Unified CM to receive calls on specific telephone extensions. The software interacts
                              with the caller and allows the caller to search for and select the extension of the party (in your organization) that the
                              caller is trying to reach.

The Cisco Unified CM AutoAttendant does the following:

Answers a call.

Plays a user-configurable welcome prompt.

Plays a main menu prompt that asks the caller to perform one of three actions:

Press 0 for the operator.

Press 1 to enter an extension number.

Press 2 to spell by name.

If the caller chooses to spell by name (option 2), the system compares the letters that are entered with the names that are
                                    configured to the available extensions.

If a match exists, the system announces a transfer to the matched user and waits for up to two seconds for the caller to press
                                    any DTMF key to stop the transfer. If the caller does not stop the transfer, the system performs an explicit confirmation:
                                    it prompts the user for confirmation of the name and transfers the call to that user's primary extension.

If more than one match occurs, the system prompts the caller to choose the correct extension.

If too many matches occur, the system prompts the caller to enter more characters.

When the caller has specified the destination, the system transfers the call.

If the line is busy or not in service, the system informs the caller accordingly and replays the main menu prompt.

## Configure the Cisco
                        	 Unified CM AutoAttendant Application (aa.aef)

Follow the
                              		  instructions for configuring a Unified IP IVR application in Unified IP IVR Installation and Configuration ,
                              		  and for the application, choose the Cisco Unified CM AutoAttendant. Configure
                              		  both a telephone number that can be dialed and a name that can be dialed.

For
                              		  further information on how to configure and how to customize the Cisco Unified
                              		  CM AutoAttendant, see the chapter on the AutoAttendant in the .

Example
                              		  configuration data:

AutoAttendant
                                    				Number: 5000

Telephones: 7001
                                    				and 7002

Agent: tjones
                                    				(Tom Jones)

Tom Jones phone:
                                    				7002

## Test Your System and the Cisco Unified CM AutoAttendant Application

Verify that your system and the Cisco Unified CM AutoAttendant application work.

Select one of the phone numbers you have configured in the Unified CM and dial that phone number to see if you get the correct
                                       phone. If you get the correct phone, Unified CM is working.

On one of your IP phones, phone the AutoAttendant number you have created (for example: 5000).

You should get the welcome prompt. If you do, then the AutoAttendant is working.

If you have associated a person with a phone (in the example case, Tom Jones), dial the AutoAttendant number and then at the
                                       prompt, type in the person's name (in our example, tjones).

The phone (for example, 7002) you associated with the name (for example, Tom Jones) should ring.

| Step 1 | Select one of the phone numbers you have configured in the Unified CM and dial that phone number to see if you get the correct
                                       phone. If you get the correct phone, Unified CM is working. |
|---|---|
| Step 2 | On one of your IP phones, phone the AutoAttendant number you have created (for example: 5000). You should get the welcome prompt. If you do, then the AutoAttendant is working. |
| Step 3 | If you have associated a person with a phone (in the example case, Tom Jones), dial the AutoAttendant number and then at the
                                       prompt, type in the person's name (in our example, tjones). The phone (for example, 7002) you associated with the name (for example, Tom Jones) should ring. |