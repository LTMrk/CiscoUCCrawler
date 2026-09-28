---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--6dddd6f1e5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/ucce_b_scripting-and-media-routing-guide_12_6/ucce_b_scripting-and-media-routing-guide_chapter_010.html
retrieved_at: 2026-08-21T11:54:20.973474+00:00
---

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

# Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

Updated: June 11, 2020

Chapter: Call Types Contact Data Scripting

## Chapter: Call Types Contact Data Scripting

# Call Types Contact Data Scripting

## Call Types

When writing scripts
                              		  to route contacts, you must understand call types and contact data.

A call type is the
                              		  first-level category of a contact and is determined by data associated with the
                              		  contact. You associate a script with a call type. When a contact of a certain
                              		  call type is received, the associated script runs on that contact.

You create call types during Unified ICM configuration, through the Configuration Manager. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html and the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

## Default Call
                        	 Types

A default call type
                              		  is the call type used when a contact does not map to a defined call type.

You define a default call type for each routing client through the Configuration Manager in the PG Explorer tool. The general
                              default call type is set through the Configuration Manager in the System Information tool. You can also define a general default
                              call type that is not specific to a routing client. See the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

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
                                 client and a period. For example, " NICClient.18005551212 " might be a dialed number.

The Calling line ID and Caller-entered digits are used to further categorize the call and determine the call type.

Typically, a dialed number is associated with one or more call types.

The dialed number is referred to as the Script Selector for media other than voice.

### Calling Line ID (CLID)

The Calling Line ID (CLID) is a string that represents the telephone
                                 number from where the call originated. The CLID is sometimes referred to
                                 as the ANI (Automatic Number Identification).

Typically, you would not use a CLID to define a Call Type. Rather, you
                                 would use a CLID prefix or CLID region.

For web requests, the CLID corresponds to the ApplicationString1
                                 parameter.

E-mail requests do not use the CLID.

### Use of CLID Prefixes

To define a Call Type based on the area code from where
                                 the call originated, you can use a CLID prefix.

For example, if you want to define a Call Type for all calls from the
                                 508 area code, you specify 508 as the CLID prefix. You can further
                                 refine the Call Type to calls from a certain exchange within the area
                                 code. For example, you can specify 508486 as the CLID prefix. A routing
                                 script can then process the call based on the area code or local
                                 exchange of the caller.

### Use of CLID Regions

You can define a Call Type that encompasses multiple CLID
                                 prefixes. For example, a useful Call Type could be defined as all calls
                                 from New York, which includes several area codes. To accomplish this,
                                 first define geographical regions through Unified ICM
                                 Configuration Manager. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

A routing script can then process the call based on the region of the
                                 caller.

### Caller-Entered Digits (CED)

Caller-Entered Digits (CED) are numbers entered by the caller in
                                 response to prompts. For example, a caller might enter a number to
                                 indicate the type of service needed.

The caller can enter digits through the carrier network or the call
                                 center system. The Caller-Entered Digits can be used in defining the
                                 call's Call Type. A routing script can then process the call based on
                                 data entered by the caller.

E-mail requests do not use the CED.

## Data for Enterprise Chat and
                              						Email Web Requests

The Enterprise Chat and
                                    						Email sends the following data to Unified ICM when requesting for routing a chat contact. These variables are mapped in the in.map.properties
                              file to variables in the call form. For more information about setting up ECE to send route requests to Unified ICM, see the administration documentation at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-email-interaction-manager/products-maintenance-guides-list.html .

dialednumber —A string that determines which script to run on Unified ICM. The value of the script selector variable maps to the value
                                    of the Script Selector (which maps to the Dialed Number for voice contacts) in the Call Type created through Unified ICM Configuration
                                    Manager. Therefore, you must ensure that a Script Selector with the value that the ECE uses is set up in Unified ICM.

applicationstring1 —A optional string that you can use to select a Unified ICM routing script. The value of the ApplicationString1 variable corresponds
                                    to the Calling Line ID created through Unified ICM Configuration Manager. that determines which script to run on Unified ICM.
                                    The value of the script selector variable maps to the value of the Script Selector (which maps to the Dialed Number for voice
                                    contacts) in the Call Type created through Unified ICM Configuration Manager.

applicationstring2 —A optional string that you can use to select a Unified ICM routing script. The value of the ApplicationString2 variable corresponds
                                    to the Caller-Entered Digits created through Unified ICM Configuration Manager.

callvar1-10 —Unified ICM call variables, up to 10. These are optional fields that you can use to pass any application-specific information
                                    to Unified ICM.

eccvar1-2 —Expanded call context variables, used to pass additional information to the Unified ICM. You must set up ECC variables on
                                    the Unified ICM before the ECE can use them. For more information about creating ECC variables, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Data for Enterprise Chat and
                              						Email E-mail Requests

The Enterprise Chat and
                                    						Email sends the following data to Unified ICM when requesting that an e-mail message be routed:

Instance and skill group name - A string that determines which script to run on Unified ICM. The value is the name of the ECE instance and the Unified ICM Routing skill group the message was assigned to, separated by a period; for example, "SupportInstance.techSupport".
                                    The string maps to the Script Selector value. Therefore, you must ensure that you set up the Script Selectors with the value
                                    of the ECE instance name and each Unified ICM Routing skill group in Unified ICM.

cisco.ece.Priority - The priority of the message. The value of the Priority variable, which is "0" through "3"

"0" for Normal

"1" for High

"2" for Very High

"3" for Urgent

cisco.ece.Category - The categories of the message. The categories variable is an array containing up to 10 category values. The ECE administrator sets up the category values. You can use the value of the variable to categorize the contact in a script.

cisco.ece.MessageKey - The unique identifier of the message that ECE is requesting Unified ICM to route. While you would not typically use the Message Key to categorize a contact in a script,
                                    it may be useful when Unified ICM is integrated with a CRM application; you could record the Message Key in the CRM database
                                    for future reference to e-mail correspondence with a customer.

These Expanded Call Context (ECC) variables are optional. Before you use these ECC variables, configure them for Unified CCE
                                          in the Configuration Manager's Expanded Call Variable List Tool and also in ECE .

For more information about Expanded Call Variables, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

For more information about setting up ECE to send route requests to Unified ICM, see at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

## Association of Contacts with Call Types

Following is the general process of how   the system attempts to associate a contact with a
                              call type:

If the dialed number, calling line ID, and caller-entered digits of the contact map to a defined call type, the system uses
                                    that call type:

If no call type matches the contact, the system uses the default call type for the routing client .

If no default call type is defined for the routing client, the system uses the general default call type.

If no general default call type is defined, the system uses the default label defined for the dialed number.

If no default label is defined for the dialed number, the system returns an error to the routing client.

## Determination of Call Type for Voice Contact

The following example demonstrates how  the system determines the call type for a voice
                              contact and runs the appropriate script:

When configuring Unified ICM , you create a call type called
                                    "MASSACHUSETTS_SALES". This call type is defined as:

Having a dialed number of " NICClient1.8005551234 ".

Being from Massachusetts. This is determined by using a
                                          Calling Line ID Region, which consists of CLID Prefixes for
                                          all area codes in Massachusetts: 617, 508, 978, and 413.

Being a Sales call. This is determined by a caller-entered
                                          digits value of "1", which is the number in the voice menu
                                          to indicate that the caller needs sales help.

You create a script called "MASSACHUSETTS_SALES_SCRIPT," which
                                    finds the longest available agent in the "NORTHEAST_SALES" skill
                                    group.

You schedule the script to run for the "MASSACHUSETTS_SALES" call
                                    type.

A caller dials 1-800-555-1234, from the phone number 508-663-4958.

When prompted by a menu, the caller enters 1 to request sales
                                    help.

A route request is sent to Unified ICM .

Unified ICM examines the dialed number, which
                                    equals "18005551234".

Unified ICM evaluates the CLID value and
                                    determines that the CLID prefix is "508", which is an area code in
                                    Massachusetts.

Unified ICM examines the CED value, which is
                                    "1", which indicates that it is a Sales call.

Unified ICM determines that the call type is "MASSACHUSETTS_SALES" and runs the "MASSACHUSETTS_SALES_SCRIPT" script.

Unified ICM assigns the task to a particular
                                    agent.

## Determination of Call Type for ECE Web Request

The following basic example demonstrates how the system determines the call type for a Enterprise Chat and
                                    						Email chat web request:

When configuring the Unified ICM , you create a call type called "SSC_CT". This call type is defined as having a Script Selector (Dialed Number) of "SSC_DN".

When configuring ECE , you set the value of the script selector variable in the call form to "SSC_DN".

When configuring ECE , you set the dialednumber variable in the input map to equal the script selector variable in the call form.

You create a script called "SSC_SCRIPT," which finds the longest available agent in the "COLLABORATION_SALES" skill group.

You schedule the script to run for the "SSC_CT" call type.

A web user requests a chat session.

A route request is sent to Unified ICM .

Unified ICM determines that the Call Type is "SSC_CT" and runs the "SSC_SCRIPT" script.

Unified ICM instructs ECE to assign the task to a particular agent.

## Determination of Call Type for ECE E-mail Contact

The following example demonstrates how Unified ICM determines
                              the Call Type for a Enterprise Chat and
                                    						Email e-mail contact:

When configuring Unified ICM, you create a Call Type called
                                    "EMAIL_CT". This Call Type is defined as having a Script Selector
                                    (Dialed Number).

When configuring ECE , you set the workflow rules to assign some messages to Unified ICM Routing queue "SalesQueue", which is mapped to an e-mail
                                    MRD.

You create a script called "EMAIL_SCRIPT". The e-mails are
                                    queued to skill group called Sales in the script.

You schedule the script to run for the "EMAIL_CT" Call Type.

A "Sales" message is assigned to the "SalesQueue" queue.

ECE sends a route request to Unified ICM.

Unified ICM determines that the Call Type is "EMAIL_CT" and runs the "EMAIL_SCRIPT" script.

Unified ICM instructs ECE to assign the task to a particular agent who is logged in to the Sales Skill group.

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

| Note | The dialed number is referred to as the Script Selector for media other than voice. |
|---|---|

| Note | You can differentiate between the case where the caller is not
                                          prompted for digits ("None Required") and the case where the caller is
                                          prompted but does not respond ("None Entered"). You can also choose
                                          "None" as the Caller-Entered Digits. |
|---|---|

| Note | The priority if set through the ECE rules. You can use the value of the variable to categorize the contact in a script. |
|---|---|

| Note | These Expanded Call Context (ECC) variables are optional. Before you use these ECC variables, configure them for Unified CCE
                                          in the Configuration Manager's Expanded Call Variable List Tool and also in ECE . |
|---|---|