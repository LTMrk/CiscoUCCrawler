---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-configuration-guide-pcce-b-admi-7125de14f8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/configuration/guide/pcce_b_admin-and-config-guide_12_5/pcce_b_admin-and-config-guide_12_5_chapter_010101.html
retrieved_at: 2026-08-21T04:45:15.530449+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

Updated: June 11, 2024

Chapter: Experience Management Scripting

## Chapter: Experience Management Scripting

# Experience Management Scripting

## Modify CCE Scripts for Experience Management Voice, SMS, and Email Surveys

In Script Editor, modify your CCE call routing scripts for incoming calls as follows:

Add nodes to invoke the call studio survey script, if needed. The following example explains when you might need to explicitly
                           add nodes to call the survey script.

A script is called that asks callers if they want to participate in a survey. The script then sets the user.microapp.isPostCallSurvey variable according to the caller's response.

You can use POD.ID to send cc_CustomerID , and this cc_CustomerID can be used to filter the data in finesse gadget.

POD.ID is an optional field in Experience Management voice survey and the supported POD. ID format will be xxx, where xxx is the Customer_id.

### Create Experience Management Routing Script for Voice

Create the following routing script for the Experience Management Call Type to play your survey script or application to the caller.

Step 1

In Script Editor, create the routing script as shown in the example.

Step 2

Do the following to ensure the routing script is mapped to the call type you created for Experience Management .

Navigate to Script > Call Type Manager .

On the Schedules tab, from the Call Type drop-down list, select the call type that you created for Experience Management .

For more information refer to the topic Call Type and Survey Association in Unified CCE Admin in Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

Click Add .

Click OK .

For more information on optimizing the threshold values for SMS and Email batch processing, refer to the topic Configure SMS/Email Thresholds in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html

### Create Experience Management Routing Script for SMS and Email

Experience Management Deferred (SMS/Email) survey is used for getting feedback on the overall customer journey experience.
                              For invoking this survey, the caller's mobile number, email address, and other details have to be collected from Call Studio
                              and passed to ICM. To configure this, refer to the following sections:

#### Configure Call Studio App Data Format

Create Call Studio application with the use of CVP SubDialogReurn element and fill the customer data as external VXML variables.

Example: External VXML 0 = Email=abcd@cisco.com;cc_CustomerId=xyz;cc_language=en-US;Optin=yes;Mobile=911234567890;

Each key-value pair is separated by a semi colon.

The variable names are case sensitive.

Refer to the following table for the variables and their descriptions.

Variable Name

Description

cc_CustomerId

Unique ID for a customer across multiple channels.

Required

Email

Customer email ID

Either email or phone number is required

Mobile

Customer mobile number with country code.

Example: 919911223344

Either email or phone number is required

cc_language

Survey language

Example: en-US

Optional

Optin

Option to check if customer wants to opt for the survey:

Values: yes/no

Default value is yes when the value is not captured from Call Studio.

Optional

#### Configure ICM Script

Step 1

Create the ICM script as shown in the following screen shot:

Step 2

Fill the ECC variable POD.ID values from user.microapp.FromExtVXML array and pass it to ICM.

Example: POD.ID=cc_CustomerId=xyz;Email=abcd@cisco.com;cc_language=en-US;Optin=yes;Mobile=911234567890;

Step 3

Save the script.

## Modify CCE Script for Experience Management Digital Channel Surveys

In Script Editor, set up new call routing scripts or modify your CCE call routing scripts for a new email/chat task request.
                           You can enable a survey for an Email and Chat activity by configuring it in the associated call type, and enabling the user.microapp.isPostCallSurvey and user.CxSurveyInfo ECC variables. You must also configure POD.ID to define prefill data that ties the generated survey to the end customer after receiving a response from them. The same
                           prefill data is also used for showcasing the customer's previous interaction/feedback to the agent using the Customer Experience
                           Journey (CEJ) gadget on the Finesse desktop.

The variable user.CxSurveyInfo is populated automatically by the Call Router if the survey is enabled through the routing script and for a particular Call
                           Type used for routing the task. The script then sets the user.microapp.isPostCallSurvey variable according to the caller's response.

You can use POD.ID to set cc_CustomerID to uniquely identify a survey response for the end customer.

### Create Experience Management Routing Script for Digital Channel Surveys

Step 1

Modify the ICM script as shown to enable Digital Channel Surveys:

Ensure that these ECC variables are setup using the set variable nodes before the script queues the request to the skill group.

Step 2

Add set variable node and set the user.microapp.isPostCallSurvey variable to Y .

Step 3

Add the set variable for POD.ID and follow the example below to pass the values to ICM. You can use custom or system defined variables in POD.ID in key-value pairs.

Example: POD.ID=cc_CustomerId=xxx;Email=xx;Mobile=xxx;

In this example, the POD.ID variable is initialized with ECC variables that contain the customer's name, email ID, and phone
                                                         number received from ECE.

Alternatively, the Script Administrator can also perform a database lookup to retrieve these values and assign it to the POD.ID
                                                         variable.

Step 4

Save the script.

| Note | You can use POD.ID to send cc_CustomerID , and this cc_CustomerID can be used to filter the data in finesse gadget. POD.ID is an optional field in Experience Management voice survey and the supported POD. ID format will be xxx, where xxx is the Customer_id. |
|---|---|

| Step 1 | In Script Editor, create the routing script as shown in the example. |
|---|---|
| Step 2 | Do the following to ensure the routing script is mapped to the call type you created for Experience Management . Navigate to Script > Call Type Manager . On the Schedules tab, from the Call Type drop-down list, select the call type that you created for Experience Management . For more information refer to the topic Call Type and Survey Association in Unified CCE Admin in Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html Click Add . Click OK . For more information on optimizing the threshold values for SMS and Email batch processing, refer to the topic Configure SMS/Email Thresholds in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html |

| Create Call Studio application with the use of CVP SubDialogReurn element and fill the customer data as external VXML variables. Example: External VXML 0 = Email=abcd@cisco.com;cc_CustomerId=xyz;cc_language=en-US;Optin=yes;Mobile=911234567890; Note Each key-value pair is separated by a semi colon. Note The variable names are case sensitive. Figure 1. Example Refer to the following table for the variables and their descriptions. Table 1. Variables and their descriptions Variable Name Description Required/Optional cc_CustomerId Unique ID for a customer across multiple channels. Required Email Customer email ID Either email or phone number is required Mobile Customer mobile number with country code. Example: 919911223344 Either email or phone number is required cc_language Survey language Example: en-US Optional Optin Option to check if customer wants to opt for the survey: Values: yes/no Default value is yes when the value is not captured from Call Studio. Optional | Note | Each key-value pair is separated by a semi colon. | Note | The variable names are case sensitive. | Variable Name | Description | Required/Optional | cc_CustomerId | Unique ID for a customer across multiple channels. | Required | Email | Customer email ID | Either email or phone number is required | Mobile | Customer mobile number with country code. Example: 919911223344 | Either email or phone number is required | cc_language | Survey language Example: en-US | Optional | Optin | Option to check if customer wants to opt for the survey: Values: yes/no Default value is yes when the value is not captured from Call Studio. | Optional |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note | Each key-value pair is separated by a semi colon. |
| Note | The variable names are case sensitive. |
| Variable Name | Description | Required/Optional |
| cc_CustomerId | Unique ID for a customer across multiple channels. | Required |
| Email | Customer email ID | Either email or phone number is required |
| Mobile | Customer mobile number with country code. Example: 919911223344 | Either email or phone number is required |
| cc_language | Survey language Example: en-US | Optional |
| Optin | Option to check if customer wants to opt for the survey: Values: yes/no Default value is yes when the value is not captured from Call Studio. | Optional |

| Note | Each key-value pair is separated by a semi colon. |
|---|---|

| Note | The variable names are case sensitive. |
|---|---|

| Variable Name | Description | Required/Optional |
|---|---|---|
| cc_CustomerId | Unique ID for a customer across multiple channels. | Required |
| Email | Customer email ID | Either email or phone number is required |
| Mobile | Customer mobile number with country code. Example: 919911223344 | Either email or phone number is required |
| cc_language | Survey language Example: en-US | Optional |
| Optin | Option to check if customer wants to opt for the survey: Values: yes/no Default value is yes when the value is not captured from Call Studio. | Optional |

| Step 1 | Create the ICM script as shown in the following screen shot: |
|---|---|
| Step 2 | Fill the ECC variable POD.ID values from user.microapp.FromExtVXML array and pass it to ICM. Example: POD.ID=cc_CustomerId=xyz;Email=abcd@cisco.com;cc_language=en-US;Optin=yes;Mobile=911234567890; |
| Step 3 | Save the script. |

| Note | You can use POD.ID to set cc_CustomerID to uniquely identify a survey response for the end customer. |
|---|---|

| Step 1 | Modify the ICM script as shown to enable Digital Channel Surveys: Note Ensure that these ECC variables are setup using the set variable nodes before the script queues the request to the skill group. | Note | Ensure that these ECC variables are setup using the set variable nodes before the script queues the request to the skill group. |
|---|---|---|---|
| Note | Ensure that these ECC variables are setup using the set variable nodes before the script queues the request to the skill group. |
| Step 2 | Add set variable node and set the user.microapp.isPostCallSurvey variable to Y . |
| Step 3 | Add the set variable for POD.ID and follow the example below to pass the values to ICM. You can use custom or system defined variables in POD.ID in key-value pairs. Example: POD.ID=cc_CustomerId=xxx;Email=xx;Mobile=xxx; Note In this example, the POD.ID variable is initialized with ECC variables that contain the customer's name, email ID, and phone
                                                         number received from ECE. Alternatively, the Script Administrator can also perform a database lookup to retrieve these values and assign it to the POD.ID
                                                         variable. | Note | In this example, the POD.ID variable is initialized with ECC variables that contain the customer's name, email ID, and phone
                                                         number received from ECE. Alternatively, the Script Administrator can also perform a database lookup to retrieve these values and assign it to the POD.ID
                                                         variable. |
| Note | In this example, the POD.ID variable is initialized with ECC variables that contain the customer's name, email ID, and phone
                                                         number received from ECE. Alternatively, the Script Administrator can also perform a database lookup to retrieve these values and assign it to the POD.ID
                                                         variable. |
| Step 4 | Save the script. |

| Note | Ensure that these ECC variables are setup using the set variable nodes before the script queues the request to the skill group. |
|---|---|

| Note | In this example, the POD.ID variable is initialized with ECC variables that contain the customer's name, email ID, and phone
                                                         number received from ECE. Alternatively, the Script Administrator can also perform a database lookup to retrieve these values and assign it to the POD.ID
                                                         variable. |
|---|---|