---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-configuration-guide-pcce-b-admi-a506a7b0e7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/configuration/guide/pcce_b_admin_configuration_guide_12_6_1/pcce_b_admin_configuration_guide_12_6_1_chapter_010110.html
retrieved_at: 2026-08-21T16:53:00.372722+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(1)

Updated: August 21, 2023

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

For more information refer to the topic Call Type and Survey Association in Unified CCE Admin in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

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

| Note | You can use POD.ID to send cc_CustomerID , and this cc_CustomerID can be used to filter the data in finesse gadget. POD.ID is an optional field in Experience Management voice survey and the supported POD. ID format will be xxx, where xxx is the Customer_id. |
|---|---|

| Step 1 | In Script Editor, create the routing script as shown in the example. |
|---|---|
| Step 2 | Do the following to ensure the routing script is mapped to the call type you created for Experience Management . Navigate to Script > Call Type Manager . On the Schedules tab, from the Call Type drop-down list, select the call type that you created for Experience Management . For more information refer to the topic Call Type and Survey Association in Unified CCE Admin in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html For more information refer to the topic Call Type and Survey Association in Unified CCE Admin in Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html Click Add . Click OK . For more information on optimizing the threshold values for SMS and Email batch processing, refer to the topic Configure SMS/Email Thresholds in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html |

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