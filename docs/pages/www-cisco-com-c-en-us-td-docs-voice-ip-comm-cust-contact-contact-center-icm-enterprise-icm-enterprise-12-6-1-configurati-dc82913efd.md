---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-dc82913efd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/ucce_b_features-guide-1261/ucce_m_wxm_digital_channel_survey_mgt-1251.html
retrieved_at: 2026-08-16T20:13:12.199220+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Webex Experience Management Digital Channel Survey

## Chapter: Webex Experience Management Digital Channel Survey

# Webex Experience Management Digital Channel Survey

## Overview

Digital Channel Survey is initiated when the agent responds to an email/chat from a customer
                           using the Enterprise Chat and Email gadget. Cisco Webex Experience Management is a
                           Customer Experience Management (CEM) platform that allows you to see the business from
                           your customers perspective. It provides customer journey experience using the CEJ
                           omni-channel gadget. To learn more about Webex Experience Management, see https://xm.webex.com/docs/ccoverview/ .

With Webex Experience Management, Unified CCE supports:

Customer experience surveys - Set up and send surveys to customers, after an interaction, to collect feedback about their
                                 interaction.

Customer Experience Journey (CEJ) gadget - Displays all the past survey responses from a customer in a chronological list. The agent and supervisor use this
                                 gadget to gain context about the customers past experiences with the business and engage with them appropriately.

Customer Experience Analytics (CEA) gadget - Displays the overall experience of the customer interaction with agents using industry-standard metrics such as
                                 NPS, CSAT, and CES or other KPIs tracked within Experience Management. This gadget is available for agents and supervisors.

## Digital Channel Survey

Email and chat inline surveys are used to determine whether customers are satisfied with their interaction with the agent
                           in resolving their query over an email or chat. The feedback collected through the survey is used by the agents to gain context
                           about the customer in their subsequent interactions and to also improve their own performance. You can configure Enterprise
                           Chat and Email to initiate this survey when the agent sends an email or terminates a chat conversation with a customer. The
                           survey is sent inline in the agents email response to customers who contact them via email, and within the chat window for
                           customers who contact them via chat.

### Digital Channel Survey Task Flow (Email/Chat)

To enable Experience Management inline surveys with Enterprise Email and Chat in Cisco Unified CCE , perform the following procedure:

Step 1

Contact your Cisco representative to purchase Experience Management license. Provide relevant information about your organization to Experience Management Activation Team. To know more about the information that will be collected,
                                          see Prerequisites .

Step 2

Experience Management Activation Team performs the following actions:

Creates account and provisions the same.

Creates default spaces and metric groups for your accounts. To know
                                                more about creating spaces, see Space
                                                   Creation .

Creates default questionnaires in Expereince Management suited for
                                                inline email and chat survey. To know more about creating your own
                                                questionnaires or editing the default ones, see Questionnaires .

Step 3

After creating and provisioning the account, you will receive handover emails
                                          from the Experience Management Activation Team. The email contains credentials and other essential
                                          information for your account. To know more about provisioning details, see Handover .

Step 4

Initially, Spaces and Widgets are created by the Experience Management provisioning team. To know more about the different default Widgets and how
                                          to export and derive meaningful insights from them, see Cisco Webex Experience Management Gadgets .

To know how to configure other Widgets in Experience Management, see Basic Widget and Composite
                                                Widgets .

Step 5

Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Step 6

Provision Experience Management service using CLI on Cloud Connect. For more information, see Provision Cloud Connect for Digital Channel Survey .

Step 7

Ensure that the Enterprise Chat and Email (ECE) is installed and configured, see the Webex Experience Manager Integration in Enterprise Chat and Email Administrator’s Guide to Administration Console at https://www.cisco.com/c/en/us/support/contact-center/enterprise-chat-email-12-5-1/model.html .

Step 8

Configure Unified CCE Experience Management integration. For more information, see Configure Unified CCE for Digital Channel Survey .

Step 9

Configure Call Type and Dialed Number. For more information, see Configure Call Type, Dialed Number, and Survey Association .

Step 10

Modify CCE Scripts. For more information, see Modify CCE Scripts for Experience Management Digital Channel Surveys in Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

Associate the CCE script with the Call Type created in the previous step.

Step 11

Provision Cloud Connect on Cisco Finesse. For more information, see the Cloud Connect Server Settings topic at the Cisco Finesse Administration Guide .

Step 12

Add Experience Management gadgets into Finesse desktop layout. For more information, see Cisco Webex Experience Management Gadgets .

## Provision Cloud Connect for Digital Channel Survey

Before provisioning Cloud Connect for Experience Management service, ensure to setup and enable Cloud Connect. For more information, see the Cloud Connect Administration section in Administration Guide for Cisco Unified Contact Center Enterprise

Ensure that you have installed the self-signed certificates for Cloud Connect. For more information, see the Self-Signed Certificates section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

Provision Experience Management service using the following CLI on Cloud Connect.

```
set cloudconnect cherrypoint config
```

For more commands related to Experience Management service, see the Cloud Connect CLI section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

## Configure Unified CCE for Digital Channel Survey

Refer to the following procedures to enable the Experience Management email and chat survey:

Configure Expanded Call Variables

Configure Call Type, Dialed Number, and Survey Association

Associate Survey to Call Type in Unified CCE Admin

## Configure Expanded Call Variables

Step 1

In the Configuration Manager menu, select Tools > List Tools > Expanded Call Variable List .

Step 2

Click Retrieve to view the list of existing ECC variables.

Step 3

Check if the user.microapp.isPostCallSurvey variable exists. If the variable does not exist, do the following to create a new variable:

Click Add .

In the Attributes tab that appears, enter user.microapp.isPostCallSurvey in the Name field.

Set Max Length to 1.

Check the Enabled check box.

Click Save .

When your CCE routing scripts starts, you can turn off Post Call Survey field in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y .

In the script, set the user.microapp.isPostCallSurvey before routing it to the agent.

Step 4

Check if the user.CxSurveyInfo variable exists. If the variable does not exist, do the following to create a new variable:

Click Add .

In the Attributes tab that appears, enter user.CxSurveyInfo in the Name field.

Set Max Length to 80.

Check the Enabled check box.

Step 5

Click Save .

The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice.

You can use several ECC payloads in the same call flow, but only one ECC payload has scope at a given moment. For more information,
                                                      see ECC Payloads sections in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Step 6

Populate the POD. ID variable.

Step 7

Restart the active VRU PG (side A or B) to register the new ECC variable.

The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you don’t want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'.

### Configure POD.ID

Cisco provided variables are predefined, but for POD.ID, the maximum length should be set to 120. Enable the POD.ID variable
                              to edit its length.

You can modify the variables only if you have the edit access.

Populate the value in the script with multiple attributes in a key-value pair format. Each key-value pair is seperated with
                              a semi-colon. These attributes are sent to the Webex Experience Management as prefills when ECE initiates the survey. The
                              following table displays the supported attributes:

Attribute

Description

Applicable

cc_CustomerId

Unique ID for a customer across multiple channels

Chat and Email surveys for Digital Channels

Email

Email ID of the customer for Email survey across multiple channels

Chat and Email surveys for Digital Channels

Mobile

Phone number for Chat surveys

Chat and Email surveys for Digital Channels

Example: cc_CustomerId=xxx;Email=xx;Mobile=xxx;

For more information on setting the ECC variables used in the example, see Modify CCE Scripts for Experience Management Digital Channel Surveys in Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

For more information on Expanded Call Context Variables , see the chapter Configuring Variables in the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Configure Call Type, Dialed Number, and Survey Association

Step 1

In ICM Configuration Manager, navigate to Tools > List Tools > Call Type List to create a Call Type.

Step 2

Associate the survey with the last call type before the email/chat is handled by the agent.

For more information, refer to the topic Associate Survey to Call Type in Unified CCE Admin .

Step 3

Create a Dial Number in ICM Configuration Manager and associate it with Call type (created in Step 1) for email and chat.

### Associate Survey to Call Type in Unified CCE Admin

You can associate the survey to the Call Type only if you have added Cloud Connect to the Inventory page in CCE Admin and configured the survey in Webex Experience Management portal.

Only inline surveys can be associated to a Call Type associated with digital channels.

Call Types are created and managed in Configuration Manager tool and the survey is associated using the CCE Admin tool.

Step 1

In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Type .

The list of all the Call Type are displayed.

For more information on Call Types, refer to the Help in Configuration Manager > Tools > List Tool > Call Type List .

Step 2

Click on the Call Type which you want to associate to the Survey.

Step 3

Select the Enable Experience Management check box to associate the Webex Experience Management survey.

The Experience Management tab is enabled with the following options:

Inline Survey

Deferred Survey

Step 4

Select Inline Survey for email and chat.

Click on the magnifying glass icon, and the configured surveys will be populated in the pop-up window.

Step 5

Select the survey from the pop-up window and click Save .

| Step 1 | Contact your Cisco representative to purchase Experience Management license. Provide relevant information about your organization to Experience Management Activation Team. To know more about the information that will be collected,
                                          see Prerequisites . |
|---|---|
| Step 2 | Experience Management Activation Team performs the following actions: Creates account and provisions the same. Creates default spaces and metric groups for your accounts. To know
                                                more about creating spaces, see Space
                                                   Creation . Creates default questionnaires in Expereince Management suited for
                                                inline email and chat survey. To know more about creating your own
                                                questionnaires or editing the default ones, see Questionnaires . |
| Step 3 | After creating and provisioning the account, you will receive handover emails
                                          from the Experience Management Activation Team. The email contains credentials and other essential
                                          information for your account. To know more about provisioning details, see Handover . |
| Step 4 | Initially, Spaces and Widgets are created by the Experience Management provisioning team. To know more about the different default Widgets and how
                                          to export and derive meaningful insights from them, see Cisco Webex Experience Management Gadgets . To know how to configure other Widgets in Experience Management, see Basic Widget and Composite
                                                Widgets . |
| Step 5 | Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| Step 6 | Provision Experience Management service using CLI on Cloud Connect. For more information, see Provision Cloud Connect for Digital Channel Survey . |
| Step 7 | Ensure that the Enterprise Chat and Email (ECE) is installed and configured, see the Webex Experience Manager Integration in Enterprise Chat and Email Administrator’s Guide to Administration Console at https://www.cisco.com/c/en/us/support/contact-center/enterprise-chat-email-12-5-1/model.html . |
| Step 8 | Configure Unified CCE Experience Management integration. For more information, see Configure Unified CCE for Digital Channel Survey . |
| Step 9 | Configure Call Type and Dialed Number. For more information, see Configure Call Type, Dialed Number, and Survey Association . |
| Step 10 | Modify CCE Scripts. For more information, see Modify CCE Scripts for Experience Management Digital Channel Surveys in Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html . Associate the CCE script with the Call Type created in the previous step. |
| Step 11 | Provision Cloud Connect on Cisco Finesse. For more information, see the Cloud Connect Server Settings topic at the Cisco Finesse Administration Guide . |
| Step 12 | Add Experience Management gadgets into Finesse desktop layout. For more information, see Cisco Webex Experience Management Gadgets . |

| Note | Ensure that you have installed the self-signed certificates for Cloud Connect. For more information, see the Self-Signed Certificates section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide . |
|---|---|

| Step 1 | In the Configuration Manager menu, select Tools > List Tools > Expanded Call Variable List . The Expanded Call Variable List window appears. |
|---|---|
| Step 2 | Click Retrieve to view the list of existing ECC variables. |
| Step 3 | Check if the user.microapp.isPostCallSurvey variable exists. If the variable does not exist, do the following to create a new variable: Click Add . In the Attributes tab that appears, enter user.microapp.isPostCallSurvey in the Name field. Set Max Length to 1. Check the Enabled check box. Click Save . When your CCE routing scripts starts, you can turn off Post Call Survey field in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y . Note In the script, set the user.microapp.isPostCallSurvey before routing it to the agent. Note To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . | Note | In the script, set the user.microapp.isPostCallSurvey before routing it to the agent. | Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
| Note | In the script, set the user.microapp.isPostCallSurvey before routing it to the agent. |
| Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
| Step 4 | Check if the user.CxSurveyInfo variable exists. If the variable does not exist, do the following to create a new variable: Click Add . In the Attributes tab that appears, enter user.CxSurveyInfo in the Name field. Set Max Length to 80. Check the Enabled check box. |
| Step 5 | Click Save . Note The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. Note You can use several ECC payloads in the same call flow, but only one ECC payload has scope at a given moment. For more information,
                                                      see ECC Payloads sections in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html | Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. | Note | You can use several ECC payloads in the same call flow, but only one ECC payload has scope at a given moment. For more information,
                                                      see ECC Payloads sections in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
| Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
| Note | You can use several ECC payloads in the same call flow, but only one ECC payload has scope at a given moment. For more information,
                                                      see ECC Payloads sections in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
| Step 6 | Populate the POD. ID variable. For more information on populating this variable, refer to the topic Configure POD.ID . |
| Step 7 | Restart the active VRU PG (side A or B) to register the new ECC variable. If the ECC variable exists, you can skip this step. Note The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you don’t want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. | Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you don’t want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |
| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you don’t want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |

| Note | In the script, set the user.microapp.isPostCallSurvey before routing it to the agent. |
|---|---|

| Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
|---|---|

| Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
|---|---|

| Note | You can use several ECC payloads in the same call flow, but only one ECC payload has scope at a given moment. For more information,
                                                      see ECC Payloads sections in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
|---|---|

| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you don’t want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |
|---|---|

| Attribute | Description | Applicable |
|---|---|---|
| cc_CustomerId | Unique ID for a customer across multiple channels | Chat and Email surveys for Digital Channels |
| Email | Email ID of the customer for Email survey across multiple channels | Chat and Email surveys for Digital Channels |
| Mobile | Phone number for Chat surveys | Chat and Email surveys for Digital Channels |

| Step 1 | In ICM Configuration Manager, navigate to Tools > List Tools > Call Type List to create a Call Type. |
|---|---|
| Step 2 | Associate the survey with the last call type before the email/chat is handled by the agent. For more information, refer to the topic Associate Survey to Call Type in Unified CCE Admin . |
| Step 3 | Create a Dial Number in ICM Configuration Manager and associate it with Call type (created in Step 1) for email and chat. |

| Note | Only inline surveys can be associated to a Call Type associated with digital channels. |
|---|---|

| Step 1 | In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Type . The list of all the Call Type are displayed. For more information on Call Types, refer to the Help in Configuration Manager > Tools > List Tool > Call Type List . |
|---|---|
| Step 2 | Click on the Call Type which you want to associate to the Survey. |
| Step 3 | Select the Enable Experience Management check box to associate the Webex Experience Management survey. The Experience Management tab is enabled with the following options: Inline Survey Deferred Survey |
| Step 4 | Select Inline Survey for email and chat. Click on the magnifying glass icon, and the configured surveys will be populated in the pop-up window. |
| Step 5 | Select the survey from the pop-up window and click Save . |