---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-1b0c9f3d0e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_features-guide-1262/rcct_m_webex-experience-management-integration1261.html
retrieved_at: 2026-08-21T11:55:57.948426+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: April 30, 2025

Chapter: Webex Experience Management Integration

## Chapter: Webex Experience Management Integration

# Webex Experience Management Integration

## Experience Management Overview

To enable this feature in Unified CCE , install the following patches:

ICM 12.5(1)_ES7

CVP 12.5(1)_ES6

Cloud Connect 12.5(1)ES1

Finesse 12.5(1)ES2

Cisco Webex Experience Management is a Customer Experience Management (CEM) platform that allows
                           you to see your business from your customers' perspective. To know more about Webex
                           Expereince Management, see https://xm.webex.com/docs/ccoverview/ .

With Webex Experience Management, Unified CCE supports:

Customer experience surveys - Set up and send surveys to customers, after an interaction, to collect feedback about their
                                 interaction.

Experience Management Post Call Survey

Customer Experience Journey (CEJ) gadget - Displays all the past survey responses from a customer in a chronological list. The agent and supervisor use this
                                 gadget to gain context about the customers past experiences with the business and engage with them appropriately.

Customer Experience Analytics (CEA) gadget - Displays the overall experience of the customer interaction with agents using industry-standard metrics such as
                                 NPS, CSAT, and CES or other KPIs tracked within Experience Management. This gadget is available for agents and supervisors.

## Experience Management Voice Survey

Experience Management post-call survey is used to determine whether the customers are satisfied with their voice call experiences.
                           You can configure Experience Management to initiate this survey when an agent disconnects from the caller. The survey can
                           be done in three modes—voice, SMS, or email.

The CCE script enables or disables voice call survey for each call by testing for conditions and setting an expanded call
                           variable that controls Experience Management. For example, the script can invoke a prompt that asks callers whether they want
                           to participate in a survey. Based on the caller's response, the script sets the expanded call variable that controls whether
                           the call gets transferred to the voice call survey Dialed Number.

You can send post call survey links through email or SMS also. After every call, the customer is provided with a choice to
                           participate in the survey and answer few questions over email or their phone. For more information on how to configure or
                           to associate the survey, refer to the section Configure Unified CCE for Experience Management Voice, SMS and Email Survey .

The Experience Management Post Call Survey call works just like a regular call from the Unified CCE point of view. Scripts are invoked, CVP refers the call to Experience Management , and the customer uses the keypad on a phone to respond to questions asked during the survey. During Experience Management Post Call Survey , the call context information is retrieved from the original customer call.

Experience Management supports G.711 u-law and G.711 a-law codecs.

### Experience Management Task Flow

To enable Experience Management Post Call Survey in Cisco Unified CCE , follow this task flow:

Step 1

Contact your Cisco representative to purchase Experience Management license. After the purchase, you need to provide relevant information about your organization to Experience Management Activation Team. To know more about the information that will be collected, see Prerequisites .

Step 2

Experience Management Activation Team performs the following actions:

Creates accounts and provisions the same.

Creates default spaces and metric groups for your accounts. To know more about creating spaces, see Space Creation .

Creates standard questionnaires for Experience Management Post Call Survey and publishes the same. To know more about creating questionnaires, see Questionnaires .

Step 3

After creating and provisioning the account, you will receive handover emails from the Experience Management Activation Team. The email contains credentials and other essential information for your account. To know more about provisioning
                                          details, see Handover .

Step 4

Initially, Spaces and Widgets are created by the Experience Management provisioning team. To know more about the different default Widgets, how to export and derive meaningful insights from them,
                                          see Experience Management Gadgets .

To know how to configure additional Widgets in Experience Management , see Experience Management Gadgets .

Step 5

Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 6

Provision Experience Management service using CLI on Cloud Connect. For more information, see Provision Experience Management Service on Cloud Connect .

Step 7

Configure Cloud Connect in Operations Console (NOAMP). For details see the section Configure CVP Devices for Cloud Connect in Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 8

Configure Post Call Survey in CVP. For more information, see Configure Post Call Survey in CVP .

Step 9

Import the following certificates to the CVP Server:

Cloud Connect certificate

Experience Management certificate

For details, see the sections Import Cloud Connect Certificate to
                                                Unified CVP Keystore and Import Experience Management
                                                Certificate to Unified CVP Call Server in Configuration
                                                Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 10

Ensure that the threshold properties (in ivr.properties and sip.properties files) and proxy settings are configured in CVP for Experience Management. For details, see the section Webex Experience Management Configuration in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 11

Configure Unified CCE Experience Management . For more information, see the topic Configure Unified CCE for Experience Management Voice, SMS and Email Survey .

Step 12

Configure Dialed Number and Call Type for Incoming Call and Experience
                                          Management post call survey routing script. For more information, see Configure Dialed Number and Call Type .

Step 13

Modify CCE scripts. For more information, see Modify CCE Scripts for Experience Management Voice, SMS and Email Surveys in Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

Associate the CCE script with the Call Type created in the previous step.

Step 14

Provision Cloud Connect on Cisco Finesse. For more information, see the Cloud Connect Server Settings topic at the Cisco Finesse Administration Guide .

Step 15

Add Experience Management gadgets into Finesse desktop layout. For more information, see Cisco Webex Experience Management Gadgets .

## Provision Experience Management Service on Cloud Connect

Before provisioning Experience Management service on Cloud Connect, ensure to setup and enable Cloud Connect. For more information, see the Cloud Connect Administration section in Administration Guide for Cisco Unified Contact Center Enterprise

Provision Experience Management service using the following CLI on Cloud Connect.

```
set cloudconnect cherrypoint config
```

For more commands related to Experience Management service, see the Cloud Connect CLI section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

The partner hosted module which is a part of Experience Management Invitations solution is required to send surveys to customers
                           over emails and SMS.

For information about Partner Hosted Module Architecture refer to https://xm.webex.com/docs/cxsetup/guides/partnerarchitecture/

For information about how to provision the infrastructure required to deploy the partner hosted
                           components of the Experience Management Invitations module, see https://xm.webex.com/docs/cxsetup/guides/partnerinfra/ .

For information about how to deploy the partner hosted components on the Experience Management
                           Invitations module once the infrastructure is provisioned, see https://xm.webex.com/docs/cxsetup/guides/partnerdeployment/ .

### Configuration Changes in Webex Experience Management

Any configuration changes done in the Webex Experience Management administration interface gets reflected in the on-premise Contact Center integrations after a maximum caching delay.

You observe the caching delay when:

Modify the questionnaires.

Adding or removing questions.

Adding new stock prefill question.

Updating the tags associated with stock prefill questions. The
                                             specific tags that Contact Center integrations use.

System configuration changes are made to the dispatch.

The maximum caching delay depends on the kind of configuration change. Because the
                                 on-premise systems cache, Webex Experience Management configuration, and
                                 the maximum delay depend on the cache invalidation period. In cache invalidation,
                                 the system invalidates or removes the data from the cache after a specific time
                                 interval.

#### Types of Caches and Cache Invalidation

The different types of caches that are used in the on-premise systems are:

Prefill Cache if any new tag is not in the cache it's updated.
                                       However, if any new questions get added with the tag it reflects only after
                                       a cache invalidation period of 24 hours. For example, tag -> List of
                                          Questions .

As the new questions are staff prefill questions, we do not expect it to
                                                   change often. Hence a delay of 24 hours is acceptable.

All other caches will be reflected after a cache invalidation period
                                       of 1 hour. For example, questionnaire -> hashScheme dispatchTemplate ->
                                          questionnaire DispatchSettings (As obtained from
                                          settings API)

The partner hosted module in the Experience Management Invitations solution maintains
                                 a cache with maximum delay of 1 hour for the Dispatches list, Settings, Delivery
                                 Policy, Active Questions, and Questionnaire APIs. For more information, see https://xm.webex.com/docs/cxsetup/guides/partnerarchitecture/#43-caching-mechanism .

## Configure Unified CCE for Experience Management Voice, SMS and Email Survey

## Configure Expanded Call Variables

Step 1

In the Configuration Manager menu, select Tools > List Tools > Expanded Call Variables List .

Step 2

Click Retrieve to view the list of existing ECC variables.

Step 3

Check if the user.microapp.isPostCallSurvey variable exists. If the variable does not exist, do the following to create a new variable:

Click Add .

In the Attributes tab that appears, enter user.microapp.isPostCallSurvey in the Name field.

Set Max Length to 1.

Check the Enabled check box.

Click Save .

When your CCE routing scripts starts, the Post Call Survey field is enabled by default even if user.microapp.isPostCallSurvey has not yet been set in the script. You can turn off Post Call Survey field in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y .

Step 4

Check if the user.CxSurveyInfo variable exists. If the variable does not exist, do the following to create a new variable:

Click Add .

In the Attributes tab that appears, enter user.CxSurveyInfo in the Name field.

Set the Max Length to 133 for Type 10 VRUs. For all other routing clients, set Max Length to 80.

Check the Enabled check box.

Step 5

Click Save .

The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice.

Step 6

Populate the POD. ID variable.

Step 7

Restart the active VRU PG (side A or B) to register the new ECC variable.

The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'.

### Configure POD.ID

Cisco provided variables are predefined, but for POD.ID, the maximum length should be set to 120.

You can modify the variables only if you have the edit access.

Populate the value in the script with multiple attributes in a key-value pair format. Each key-value pair is seperated with
                              a semi-colon. The following table displays the supported attributes:

Attribute

Description

Applicable

cc_CustomerId

Unique ID for a customer across multiple channels

Chat and Email surveys for Digital Channels

Email

Email ID of the caller for Email surveys

Email survey for voice channel

Mobile

Phone number for SMS surveys

SMS survey for voice channel

cc_language

Language of the survey

For the list of supported languages, refer to the Webex Experience Management documentation at https://xm.webex.com/docs/user/getting-help/#cloudcherry-language-support

Email, SMS, and Voice surveys for voice channel

Optin

Whether to opt in or opt out of the survey

Email, SMS, and Voice surveys for voice channel

Example: cc_CustomerId=xxx;Email=xx;Mobile=xxx;cc_langauge=xxx;Optin=yes/no

For more information on Expanded Call Context Variables , see the chapter Configure Variables in the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

You can also configure POD.ID from CVP Call Studio. For more information, refer to the topic Configure Call Studio App Data Format in the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

## Upload Audio Files for Questions in Experience Management

Experience Management allows you to upload the audio files for post call survey.

To run post-call voice survey, you must either configure Text-To-Speech(TTS) in the voice browser or upload audio prompts in Experience Management.

Create and configure the questionnaires in Experience Management for sending IVR surveys to the customer. For more information on Experience Management , refer to https://xm.webex.com/docs/ccoverview/

For more information on how to create and modify the questionnaires, refer to https://xm.webex.com/docs/cxsetup/questionnaires/ .

## Configure Dialed Number and Call Type

Step 1

In Configuration Manager , navigate to Tools > List Tools > DialedNumber/Script Selector List .

Step 2

In DialedNumber/Script Selector List create Incoming Dialed Number and Post Call Survey Dialed Number .

For more information on how to create a PCS Dialed Number, refere to the section Configure ICM for Post Call Survey in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 3

Click Save . You will be re-directed to the Configuration Manager window.

Step 4

In Configuration Manager , navigate to Tools > List Tools > Call Type List .

Step 5

In Call Type List create the Call Type . You should associate to the incoming call script and PCS script.

You should associate the incoming call type with the survey from CCEAdmin.

For more information, refer to the topic Associate Survey to Call Type in Unified CCE Admin .

## Associate Survey to Call Type in Unified CCE Admin

You can associate the Call Type to the survey only if you have added Cloud Connect in the Inventory page and configured the survey in Webex Experience Management portal.

Only one survey can be associated to a Call Type.

Call Types are created and managed in Configuration Manager tool and the survey is associated using the CCE Admin tool.

Step 1

In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Types .

The list of all the Call Types are displayed.

For more information on Call Types, refer to the Help in ConfigManager > List Tools > Call Types .

Step 2

Click on the Call Type which you want to associate to the Survey. Associate the survey with the last call type before the call is first connected
                                       to an agent.

Step 3

Select the Enable Experience Management check box to associate the Webex Experience Management survey.

The Experience Management tab is enabled with the following options:

Inline Survey (post-call voice survey)

Deferred Survey (post-call Email and SMS survey)

Step 4

Click on the magnifying glass icon, and the configured surveys will be populated in the pop-up window.

Step 5

Select the survey from the pop-up window and click Save .

| Note | To enable this feature in Unified CCE , install the following patches: ICM 12.5(1)_ES7 CVP 12.5(1)_ES6 Cloud Connect 12.5(1)ES1 Finesse 12.5(1)ES2 |
|---|---|

| Note | Experience Management supports G.711 u-law and G.711 a-law codecs. |
|---|---|

| Step 1 | Contact your Cisco representative to purchase Experience Management license. After the purchase, you need to provide relevant information about your organization to Experience Management Activation Team. To know more about the information that will be collected, see Prerequisites . |
|---|---|
| Step 2 | Experience Management Activation Team performs the following actions: Creates accounts and provisions the same. Creates default spaces and metric groups for your accounts. To know more about creating spaces, see Space Creation . Creates standard questionnaires for Experience Management Post Call Survey and publishes the same. To know more about creating questionnaires, see Questionnaires . |
| Step 3 | After creating and provisioning the account, you will receive handover emails from the Experience Management Activation Team. The email contains credentials and other essential information for your account. To know more about provisioning
                                          details, see Handover . |
| Step 4 | Initially, Spaces and Widgets are created by the Experience Management provisioning team. To know more about the different default Widgets, how to export and derive meaningful insights from them,
                                          see Experience Management Gadgets . To know how to configure additional Widgets in Experience Management , see Experience Management Gadgets . |
| Step 5 | Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 6 | Provision Experience Management service using CLI on Cloud Connect. For more information, see Provision Experience Management Service on Cloud Connect . |
| Step 7 | Configure Cloud Connect in Operations Console (NOAMP). For details see the section Configure CVP Devices for Cloud Connect in Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 8 | Configure Post Call Survey in CVP. For more information, see Configure Post Call Survey in CVP . |
| Step 9 | Import the following certificates to the CVP Server: Cloud Connect certificate Experience Management certificate For details, see the sections Import Cloud Connect Certificate to
                                                Unified CVP Keystore and Import Experience Management
                                                Certificate to Unified CVP Call Server in Configuration
                                                Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 10 | Ensure that the threshold properties (in ivr.properties and sip.properties files) and proxy settings are configured in CVP for Experience Management. For details, see the section Webex Experience Management Configuration in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 11 | Configure Unified CCE Experience Management . For more information, see the topic Configure Unified CCE for Experience Management Voice, SMS and Email Survey . |
| Step 12 | Configure Dialed Number and Call Type for Incoming Call and Experience
                                          Management post call survey routing script. For more information, see Configure Dialed Number and Call Type . |
| Step 13 | Modify CCE scripts. For more information, see Modify CCE Scripts for Experience Management Voice, SMS and Email Surveys in Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html . Associate the CCE script with the Call Type created in the previous step. |
| Step 14 | Provision Cloud Connect on Cisco Finesse. For more information, see the Cloud Connect Server Settings topic at the Cisco Finesse Administration Guide . |
| Step 15 | Add Experience Management gadgets into Finesse desktop layout. For more information, see Cisco Webex Experience Management Gadgets . |

| Note | As the new questions are staff prefill questions, we do not expect it to
                                                   change often. Hence a delay of 24 hours is acceptable. |
|---|---|

| Step 1 | In the Configuration Manager menu, select Tools > List Tools > Expanded Call Variables List . The Expanded Call Variables List window appears. |
|---|---|
| Step 2 | Click Retrieve to view the list of existing ECC variables. |
| Step 3 | Check if the user.microapp.isPostCallSurvey variable exists. If the variable does not exist, do the following to create a new variable: Click Add . In the Attributes tab that appears, enter user.microapp.isPostCallSurvey in the Name field. Set Max Length to 1. Check the Enabled check box. Click Save . When your CCE routing scripts starts, the Post Call Survey field is enabled by default even if user.microapp.isPostCallSurvey has not yet been set in the script. You can turn off Post Call Survey field in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y . Note To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . | Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
| Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
| Step 4 | Check if the user.CxSurveyInfo variable exists. If the variable does not exist, do the following to create a new variable: Click Add . In the Attributes tab that appears, enter user.CxSurveyInfo in the Name field. Set the Max Length to 133 for Type 10 VRUs. For all other routing clients, set Max Length to 80. Check the Enabled check box. |
| Step 5 | Click Save . Note The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. | Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
| Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
| Step 6 | Populate the POD. ID variable. For more information on populating this variable, refer to the topic Configure POD.ID . |
| Step 7 | Restart the active VRU PG (side A or B) to register the new ECC variable. If the ECC variable already exists, you can skip this step. Note The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. | Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |
| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |

| Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
|---|---|

| Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
|---|---|

| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |
|---|---|

| Attribute | Description | Applicable |
|---|---|---|
| cc_CustomerId | Unique ID for a customer across multiple channels | Chat and Email surveys for Digital Channels |
| Email | Email ID of the caller for Email surveys | Email survey for voice channel |
| Mobile | Phone number for SMS surveys | SMS survey for voice channel |
| cc_language | Language of the survey For the list of supported languages, refer to the Webex Experience Management documentation at https://xm.webex.com/docs/user/getting-help/#cloudcherry-language-support | Email, SMS, and Voice surveys for voice channel |
| Optin | Whether to opt in or opt out of the survey | Email, SMS, and Voice surveys for voice channel |

| Note | To run post-call voice survey, you must either configure Text-To-Speech(TTS) in the voice browser or upload audio prompts in Experience Management. |
|---|---|

| Step 1 | In Configuration Manager , navigate to Tools > List Tools > DialedNumber/Script Selector List . |
|---|---|
| Step 2 | In DialedNumber/Script Selector List create Incoming Dialed Number and Post Call Survey Dialed Number . For more information on how to create a PCS Dialed Number, refere to the section Configure ICM for Post Call Survey in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 3 | Click Save . You will be re-directed to the Configuration Manager window. |
| Step 4 | In Configuration Manager , navigate to Tools > List Tools > Call Type List . |
| Step 5 | In Call Type List create the Call Type . You should associate to the incoming call script and PCS script. You should associate the incoming call type with the survey from CCEAdmin. For more information, refer to the topic Associate Survey to Call Type in Unified CCE Admin . |

| Note | Only one survey can be associated to a Call Type. |
|---|---|

| Step 1 | In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Types . The list of all the Call Types are displayed. For more information on Call Types, refer to the Help in ConfigManager > List Tools > Call Types . |
|---|---|
| Step 2 | Click on the Call Type which you want to associate to the Survey. Associate the survey with the last call type before the call is first connected
                                       to an agent. |
| Step 3 | Select the Enable Experience Management check box to associate the Webex Experience Management survey. The Experience Management tab is enabled with the following options: Inline Survey (post-call voice survey) Deferred Survey (post-call Email and SMS survey) |
| Step 4 | Click on the magnifying glass icon, and the configured surveys will be populated in the pop-up window. |
| Step 5 | Select the survey from the pop-up window and click Save . |