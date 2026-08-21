---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-configuration-guide-pcce-b-admi-288bac2e0b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/configuration/guide/pcce_b_admin_configuration_guide_12_6_1/pcce_b_admin_configuration_guide_12_5_2_chapter_0111.html
retrieved_at: 2026-08-21T16:52:16.361521+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(1)

Updated: August 21, 2023

Chapter: Call Types, Contact Data, and Scripting

## Chapter: Call Types, Contact Data, and Scripting

# Call Types, Contact Data, and Scripting

## Call Types

When writing scripts
                              		  to route contacts, you must understand call types and contact data.

A call type is the
                              		  first-level category of a contact and is determined by data associated with the
                              		  contact. You associate a script with a call type. When a contact of a certain
                              		  call type is received, the associated script runs on that contact.

You create call types through the Call Type tool in Unified CCE Administration. See the section on call types for more information.

You create call types during Unified ICM configuration, through the Configuration Manager. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html and the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

## Default Call
                        	 Types

A default call type
                              		  is the call type used when a contact does not map to a defined call type.

You define a default call type for each routing client through the Configuration Manager in the PG Explorer tool. The general
                              default call type is set through the Configuration Manager in the System Information tool. You can also define a general default
                              call type that is not specific to a routing client. See the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

You specify the system default call type in the Settings tool of Unified CCE Administration. For more information, see the
                              section on system settings for call reporting.

## Relation Between Call Types and Scripts

Scripts are scheduled by call type . In other words, when the system receives a request to route a contact, it
                              determines the call type of that contact, then runs the associated script.

Call types provide the first level of categorization of contacts , enabling you to write scripts to route contacts differently depending on their call type. While other types of categorization
                              take place within a script, call types enable you to provide contacts with different treatment by running different scripts
                              to begin with. Call types enable categorization before a script begins to run.

## Call Type Qualifiers

The following data determine the call type. This data is referred to as the call type qualifier.

The call type qualifiers described in this section apply to
                              contacts from all media. The terminology used is applicable to voice
                              contacts; where the terminology differs for other media, the differences
                              are explained in this section.

The differences between call type qualifiers for voice and other media are also explained in the following sections in this
                              topic:

Contact Data for Cisco Enterprise Chat and Email

You can also use the call type qualifiers for categorization within a script.

### Dialed Number (DN)

A Dialed number (DN) is a string that represents the telephone number dialed by the caller, preceded by the name of the routing
                                 client and a period. For example, " NICClient.18005551212 ucm.18005551212 " might be a dialed number.

Wildcard pattern is supported in dialed number configuration.

Only the last two characters of the dialed number can be configured as wildcards. The supported wildcard character is X.

You cannot assign a valid number in the wildcard defined range, when the last two digits of dialed number are defined as wildcards.
                                                   For example, you cannot configure the valid dialed number 18000001101 under the wildcard entry 180000011XX.

During DNlookup in the script editor, the dialed number is evaluated based on the wildcard-configured dialed number.

The Calling line ID and Caller-entered digits are used to further categorize the call and determine the call type.

Typically, a dialed number is associated with one or more call types.

The dialed number is referred to as the Script Selector for media other than voice.

## Association of Contacts with Call Types

Following is the general process of how   the system attempts to associate a contact with a
                              call type:

If the dialed number, calling line ID, and caller-entered digits of the contact map to a defined call type, the system uses
                                    that call type:

If the dialed number of the contact maps to a defined call type, the system uses that call type.

If no call type matches the contact, the system uses the default call type for the routing client .

If no default call type is defined for the routing client, the system uses the general default call type.

If no general default call type is defined, the system uses the default label defined for the dialed number.

If no default label is defined for the dialed number, the system returns an error to the routing client.

If no default call type is defined, the system returns an error to the routing client.

## Determination of Call Type for Voice Contact

The following example demonstrates how  the system determines the call type for a voice
                              contact and runs the appropriate script:

When configuring Packaged CCE , you create a call type called
                                    "MASSACHUSETTS_SALES". This call type is defined as:

Having a dialed number of " ucm.8005551234 ".

You create a script called "MASSACHUSETTS_SALES_SCRIPT," which
                                    finds the longest available agent in the "NORTHEAST_SALES" skill
                                    group.

You schedule the script to run for the "MASSACHUSETTS_SALES" call
                                    type.

Packaged CCE determines that the call type is "MASSACHUSETTS_SALES" and runs the "MASSACHUSETTS_SALES_SCRIPT" script.

Packaged CCE assigns the task to a particular
                                    agent.

## Determination of Call Type for ECE Web Request

The following basic example demonstrates how the system determines the call type for a Enterprise Chat and
                                    						Email chat web request:

When configuring the Unified ICM Packaged CCE , you create a call type called "SSC_CT". This call type is defined as having a Script Selector (Dialed Number) of "SSC_DN".

When configuring ECE , you set the value of the script selector variable in the call form to "SSC_DN".

When configuring ECE , set the value of the Script Selector for Media Routing Domain to "SSC_DN".

When configuring ECE , you set the dialednumber variable in the input map to equal the script selector variable in the call form.

You create a script called "SSC_SCRIPT," which finds the longest available agent in the "COLLABORATION_SALES" skill group.

You schedule the script to run for the "SSC_CT" call type.

A n e-mail is sent or a web user requests a chat session.

A route request is sent to Unified ICM Packaged CCE .

Unified ICM Packaged CCE determines that the Call Type is "SSC_CT" and runs the "SSC_SCRIPT" script.

Unified ICM Packaged CCE instructs ECE to assign the task to a particular agent.

## Determination of Call Type for a Task
                              					Routing Task

This example is for a multichannel task from a third-party multichannel application that uses the Task
                                    					Routing APIs.  It demonstrates how  the system determines the call type for the task and runs the appropriate script.  In this example,
                              the task is a chat task.

When configuring CCE, you create a multichannel MRD called "Chat_Task_MRD".  You create a  call type called "Chat".  You create
                                    a dialed number/script selector "Chat_DN", and associate it with "Chat_Task_MRD" and the "Chat" call type.

You create a Customer Collaboration Platform Chat application from which a user can request to chat with an agent. You set the value of the script selector in the chat
                                    form to the "Chat_DN" dialed number.

You create a script called "Universal_Queue_script" that finds the longest available agent in the "Sales" skill group in the
                                    "Chat" MRD.

You schedule the script to run for the "Chat" call type.

A user requests a chat session from the Customer Collaboration Platform Chat application, using the Customer Collaboration Platform Task API.

Customer Collaboration Platform submits the task request to CCE, including the dialed number/script selector.

CCE uses the script selector to determine the call type, and runs the "Universal_Queue_script".

CCE assigns the task to an agent who is logged into the "Sales" skill group in the "Chat" MRD.

| Note | You can also use the call type qualifiers for categorization within a script. |
|---|---|

| Note | Wildcard pattern is supported in dialed number configuration. Only the last two characters of the dialed number can be configured as wildcards. The supported wildcard character is X. You cannot assign a valid number in the wildcard defined range, when the last two digits of dialed number are defined as wildcards.
                                                   For example, you cannot configure the valid dialed number 18000001101 under the wildcard entry 180000011XX. During DNlookup in the script editor, the dialed number is evaluated based on the wildcard-configured dialed number. |
|---|---|

| Note | The dialed number is referred to as the Script Selector for media other than voice. |
|---|---|