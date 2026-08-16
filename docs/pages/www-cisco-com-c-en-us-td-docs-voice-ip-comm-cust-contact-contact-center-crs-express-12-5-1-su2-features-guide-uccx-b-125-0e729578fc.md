---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-features-guide-uccx-b-125-0e729578fc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/features/guide/uccx_b_1251su2_features-guide/uccx_m_1251su2_cisco-webex-experience-management-survey.html
retrieved_at: 2026-08-16T21:17:53.431041+00:00
---

Cisco Unified Contact Center Express Features Guide, Release 12.5(1) SU2

# Cisco Unified Contact Center Express Features Guide, Release 12.5(1) SU2

Updated: April 10, 2022

Chapter: Cisco Webex Experience Management

## Chapter: Cisco Webex Experience Management

# Cisco Webex Experience Management

## Overview

Cisco Webex Experience Management is a Customer Experience Management (CEM) platform, enabling you to see your business from your customers' perspective and
                           their experience with the brand. Experience Management powers customer journey mapping, text analytics, and predictive modeling using the feedback collected from customers via
                           different channels such as email, SMS, and IVR.

Experience Management also allows handling of Personally Identifiable Information (PII) about a customer in a sensitive manner by avoiding storing
                           PII data on the platform.

With Experience Management integrated with Unified CCX:

Administrators can configure IVR, SMS, or email post-call surveys to collect feedback directly from customers. Configure the
                                 IVR survey when an inline survey has to be played to the customer at the end of a call. Configure the SMS/Email survey when
                                 a survey link has to be sent to the customer allowing them to provide feedback after a call at their convenience.

Administrators can configure and add gadgets that can be viewed on the Finesse desktop. The gadgets can display Customer Experience
                                 Journey of the customer calling in or aggregated feedback data about agent or supervisor performance.

Agents and supervisors can view the pulse of the customers using industry standard metrics such as NPS, CSAT, and CES or any
                                 other custom KPIs.

Currently, you can have surveys only for inbound ICD calls.

For an overview about Experience Management , see Experience Management Overview .

For more information on the voice survey, see Experience Management Voice Survey .

For more information on the SMS or email survey, see Experience Management SMS or Email Survey .

For more information on PII data handling, see Experience Management PII .

## Task Flow for Experience Management Post-Call Survey

Unified CCX is integrated with Experience Management to collect customer feedback through the various channels such as voice, SMS, or email post-call surveys.

The following table lists the tasks that are required to be performed to enable cross channel integration between Unified
                           CCX and Experience Management :

Task

Description

Experience Management account setup

Onboarding and configuring Unified CCX to enable cross channel integration

Configure voice (IVR) survey

Configure SMS or email survey

## Task Flow for Account Setup

The task flow to setup an account to enable Experience Management Post-Call Survey in Cisco Unified CCX solution is as follows:

Sequence

Task

1

Contact your Cisco representative to purchase Experience Management licenses. After the purchase, you need to provide relevant information about your organization to the Experience Management Activation Team. To know more about the information that will be collected, see Prerequisites .

2

Experience Management Activation Team creates:

Accounts and provisions the same.

Default spaces and metric groups for your accounts. To know more about creating spaces, see Space Creation .

Standard questionnaires for Experience Management Post Call Survey and publishes the same. To know more about creating questionnaires, see Questionnaires .

3

After successful account creation and provisioning, you will receive handover emails from the Experience Management Activation Team. The email contains credentials and other essential information for your account. To know more about provisioning
                                          details, see Handover .

4

Initially Spaces and Widgets are created by the Experience Management provisioning team. To know more about the different default Widgets, how to export and derive meaningful insights from them,
                                          see Experience Management Widgets .

To know how to configure additional Widgets in Experience Management , see Configure Experience Management Widgets .

## Task flow to Integrate Experience Management and Unified CCX

To onboard and configure Experience Management post-call survey in Cisco Unified CCX solution, the task flow is as follows:

Sequence

Task

1

Use the details provided in the Handover emails and provision Experience Management in Unified CCX by using the set cloudconnect cherrypoint config command. For more information, see Cloud Connect topic in Command Line Interface chapter of Cisco Unified Contact Center Express Admin and Operations Guide .

2

Configure server settings in Cloud Connect Server Settings gadget of Finesse Administration, with hostname of Unified CCX nodes. Use the application user credentials. For more information,
                                          see Cloud Connect Server Settings topic in Cisco Unified Contact Center Express Admin and Operations Guide .

3

Add Gadgets to Finesse desktop

The following Experience Management Widgets can be added as gadgets in Finesse desktop:

Customer Experience Journey

Customer Experience Analytics

For example, you can add Customer Experience Journey in the Home page and Customer Experience Analytics in My Statistics page for agents and Manage Team page for supervisors.

To know more about adding Gadgets to your Finesse desktop, see Experience Management Gadgets .

## Task Flow to Configure IVR Experience Management Post-Call Survey

The task flow to enable IVR Experience Management post-call survey in Unified CCX solution is as follows:

Sequence

Task

1

Create and configure the questionnaires in Experience Management for sending IVR surveys to the customer. For more information about creating questionnaires, see Questionnaires .

2

In CUCM, configure Domain Routing based SIP Route Pattern, which is associated with SIP Trunk, so that the calls can be forwarded
                                          to the Survey URI (URI of the domain that has been provisioned, which is shared as part of the Handover ). For more information, see Cisco Unified Call Manager Admin Guide .

3

Configure the Unified CCX Administration to provide an inline IVR survey to the customer.

Select the required questionnaire for IVR survey from Enable Cisco Webex Experience Management post-call survey available in the Cisco Script Application page of Unified CCX Administration. For more information, see Cisco Unified Contact Center Express Admin and Operations Guide .

If you associate an application with both IVR Experience Management post-call survey and Unified CCX Post-Call Treatment, when an agent ends a call from Finesse desktop, the Unified CCX Post-Call
                                          Treatment takes precedence and the call is not transferred to Experience Management post-call survey.

### Configure Scripts for IVR Survey

The following script variables can be configured for IVR survey:

Script Variable

Type

Description

ECC

In IVR script, populate the POD.ID ECC variable with customer ID because Customer Experience Journey gadget uses this variable to fetch and display all responses that are provided by the calling customer, across all channels.
                                          If the variable is not populated, it uses the calling number to fetch the relevant responses.

session

Enabling and Disabling a Survey for a Customer

When an application is associated with a Post-Call Survey , by default the survey is presented to all customers, when agents end the calls from the Finesse desktop. If the ccx_survey_opt_in session variable in IVR script is set as false (for a customer, in a particular session), the survey is not presented to that customer after the agent ends the call from
                                          the Finesse desktop. The ccx_survey_opt_in session variable holds a Boolean value.

The survey that is played to the customer, is the one that is associated with the first application that is triggered for
                                                      the customer. However, the survey data is associated with the agent who ends the call on Finesse desktop.

session

Customers' Language Preference

When an Unified CCX application is associated with a survey, the script may use the ccx_survey_language session variable in IVR script to add the language preference of the customers. The format of the variable is LanguageCode-CountryCode . For example, en-US . If the ccx_survey_language session variable is not populated in IVR script, by default, the language associated with trigger will be used. To configure
                                          the survey to be played in multiple languages, see Questionnaires . To know the languages that are supported by Experience Management , see Languages .

When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                      in Experience Management , the language selection option is played to the customer.

For a sample template script, see /wfavvid/Scripts/Templates/WXM/wxm_survey.aef which gets installed automatically when Unified CCX editor web launcher is launched.

## Task Flow to Configure SMS/Email Experience Management Post-Call Survey

The task flow to enable SMS/Email Experience Management post-call survey in Unified CCX solution is as follows:

Sequence

Task

1

The partner hosted module in the Experience Management Invitations solution is mandatory for the SMS/Email surveys to work.

For information about partner hosted module, see https://xm.webex.com/docs/cxsetup/guides/partnerarchitecture/

For information about how to provision the infrastructure required to deploy the partner hosted components of the Experience Management Invitations module, see https://xm.webex.com/docs/cxsetup/guides/partnerinfra/ .

For information about how to provision the infrastructure required to deploy the partner hosted components, see https://xm.webex.com/docs/cxsetup/guides/partnerdeployment/

2

Configure the Experience Management Invitation module for sending SMS/Email surveys to the customer. Create dispatch templates on Experience Management . For information about setting up dispatch in Experience Management , see https://xm.webex.com/docs/cxsetup/guides/

3

Configure the Unified CCX Administration to provide an offline SMS/Email survey to the customer.

Select the required dispatch template for SMS/Email survey from Enable Cisco Webex Experience Management post-call survey available in the Cisco Script Application page of Unified CCX Administration. For more information, see Cisco Unified Contact Center Express Admin and Operations Guide .

You can associate an application with both SMS/Email Experience Management post-call survey and Unified CCX Post-Call Treatment. Legacy Unified CCX post-call survey is triggered only if agent ends
                                          the call from Finesse desktop. SMS/Email survey is triggered irrespective of who ends the call. When both SMS/Email Experience Management post-call survey and Unified CCX Post-Call Treatment are enabled, Unified CCX Post-Call Treatment is triggered and the Experience Management post-call survey is sent.

### Configure Scripts for SMS/Email Survey

The following script variables can be configured for SMS/Email survey:

Script Variable

Type

Description

ECC

In IVR script, populate the POD.ID ECC variable with customer ID because Customer Experience Journey gadget uses this variable to fetch and display all responses that are provided by the calling customer, across all channels.
                                             If the variable is not populated the SMS/Email survey may not work as expected.

session

Enabling and Disabling a Survey for a Customer

When an application is associated with a Post-Call Survey , by default the survey is presented to all customers after the call ends. If the ccx_survey_opt_in session variable in IVR script is set as false (for a customer, in a particular session), the survey is not presented to that customer. The ccx_survey_opt_in session variable holds a Boolean value.

The survey that is sent to the customer, is the one that is associated with the first application that is triggered for the
                                                         customer after the call ends.

session

Customers' Language Preference

When an Unified CCX application is associated with a survey, the script may use the ccx_survey_language session variable in IVR script to add the language preference of the customers. The format of the variable is LanguageCode-CountryCode . For example, en-US . If the ccx_survey_language session variable is not populated in IVR script, by default, the language associated with trigger will be used. To configure
                                             the survey to be played in multiple languages, see Questionnaires . To know the languages that are supported by Experience Management , see Languages .

When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                         in Experience Management , the customer is asked to choose from the language selection options before accessing the survey.

session

Customer's Phone Number

If the ccx_customer_ani session variable is configured with the phone number of the customer in the IVR script then an SMS is sent to this number
                                             when one of the channel associated is SMS. If the phone number is not configured then the phone number of the caller is obtained
                                             from JTAPI.

ccx_customer_email_id

session

Customer's Email ID

When an Unified CCX application is associated with a survey, the script can use the ccx_customer_email_id session variable in IVR script to add the email address of the customer. This is a mandatory variable for the SMS/Email survey
                                             to work when one of the channel associated is email.

For a sample template script, see /wfavvid/Scripts/Templates/WXM/wxm_survey.aef directory which gets installed automatically when Unified CCX editor web launcher is launched.

| Note | Currently, you can have surveys only for inbound ICD calls. |
|---|---|

| Task | Description |
|---|---|
| Experience Management account setup | Task Flow for Account Setup |
| Onboarding and configuring Unified CCX to enable cross channel integration | Task flow to Integrate Experience Management and Unified CCX |
| Configure voice (IVR) survey | Task Flow to Configure IVR Experience Management Post-Call Survey |
| Configure SMS or email survey | Task Flow to Configure SMS/Email Experience Management Post-Call Survey |

| Sequence | Task |
|---|---|
| 1 | Contact your Cisco representative to purchase Experience Management licenses. After the purchase, you need to provide relevant information about your organization to the Experience Management Activation Team. To know more about the information that will be collected, see Prerequisites . |
| 2 | Experience Management Activation Team creates: Accounts and provisions the same. Default spaces and metric groups for your accounts. To know more about creating spaces, see Space Creation . Standard questionnaires for Experience Management Post Call Survey and publishes the same. To know more about creating questionnaires, see Questionnaires . |
| 3 | After successful account creation and provisioning, you will receive handover emails from the Experience Management Activation Team. The email contains credentials and other essential information for your account. To know more about provisioning
                                          details, see Handover . |
| 4 | Initially Spaces and Widgets are created by the Experience Management provisioning team. To know more about the different default Widgets, how to export and derive meaningful insights from them,
                                          see Experience Management Widgets . To know how to configure additional Widgets in Experience Management , see Configure Experience Management Widgets . |

| Sequence | Task |
|---|---|
| 1 | Use the details provided in the Handover emails and provision Experience Management in Unified CCX by using the set cloudconnect cherrypoint config command. For more information, see Cloud Connect topic in Command Line Interface chapter of Cisco Unified Contact Center Express Admin and Operations Guide . |
| 2 | Configure server settings in Cloud Connect Server Settings gadget of Finesse Administration, with hostname of Unified CCX nodes. Use the application user credentials. For more information,
                                          see Cloud Connect Server Settings topic in Cisco Unified Contact Center Express Admin and Operations Guide . |
| 3 | Add Gadgets to Finesse desktop The following Experience Management Widgets can be added as gadgets in Finesse desktop: Customer Experience Journey Customer Experience Analytics For example, you can add Customer Experience Journey in the Home page and Customer Experience Analytics in My Statistics page for agents and Manage Team page for supervisors. To know more about adding Gadgets to your Finesse desktop, see Experience Management Gadgets . |

| Sequence | Task |
|---|---|
| 1 | Create and configure the questionnaires in Experience Management for sending IVR surveys to the customer. For more information about creating questionnaires, see Questionnaires . |
| 2 | In CUCM, configure Domain Routing based SIP Route Pattern, which is associated with SIP Trunk, so that the calls can be forwarded
                                          to the Survey URI (URI of the domain that has been provisioned, which is shared as part of the Handover ). For more information, see Cisco Unified Call Manager Admin Guide . |
| 3 | Configure the Unified CCX Administration to provide an inline IVR survey to the customer. Select the required questionnaire for IVR survey from Enable Cisco Webex Experience Management post-call survey available in the Cisco Script Application page of Unified CCX Administration. For more information, see Cisco Unified Contact Center Express Admin and Operations Guide . |

| Note | If you associate an application with both IVR Experience Management post-call survey and Unified CCX Post-Call Treatment, when an agent ends a call from Finesse desktop, the Unified CCX Post-Call
                                          Treatment takes precedence and the call is not transferred to Experience Management post-call survey. |
|---|---|

| Script Variable | Type | Description |
|---|---|---|
| POD.ID | ECC | In IVR script, populate the POD.ID ECC variable with customer ID because Customer Experience Journey gadget uses this variable to fetch and display all responses that are provided by the calling customer, across all channels.
                                          If the variable is not populated, it uses the calling number to fetch the relevant responses. |
| ccx_survey_opt_in | session | Enabling and Disabling a Survey for a Customer When an application is associated with a Post-Call Survey , by default the survey is presented to all customers, when agents end the calls from the Finesse desktop. If the ccx_survey_opt_in session variable in IVR script is set as false (for a customer, in a particular session), the survey is not presented to that customer after the agent ends the call from
                                          the Finesse desktop. The ccx_survey_opt_in session variable holds a Boolean value. Note The survey that is played to the customer, is the one that is associated with the first application that is triggered for
                                                      the customer. However, the survey data is associated with the agent who ends the call on Finesse desktop. | Note | The survey that is played to the customer, is the one that is associated with the first application that is triggered for
                                                      the customer. However, the survey data is associated with the agent who ends the call on Finesse desktop. |
| Note | The survey that is played to the customer, is the one that is associated with the first application that is triggered for
                                                      the customer. However, the survey data is associated with the agent who ends the call on Finesse desktop. |
| ccx_survey_language | session | Customers' Language Preference When an Unified CCX application is associated with a survey, the script may use the ccx_survey_language session variable in IVR script to add the language preference of the customers. The format of the variable is LanguageCode-CountryCode . For example, en-US . If the ccx_survey_language session variable is not populated in IVR script, by default, the language associated with trigger will be used. To configure
                                          the survey to be played in multiple languages, see Questionnaires . To know the languages that are supported by Experience Management , see Languages . Note When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                      in Experience Management , the language selection option is played to the customer. | Note | When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                      in Experience Management , the language selection option is played to the customer. |
| Note | When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                      in Experience Management , the language selection option is played to the customer. |

| Note | The survey that is played to the customer, is the one that is associated with the first application that is triggered for
                                                      the customer. However, the survey data is associated with the agent who ends the call on Finesse desktop. |
|---|---|

| Note | When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                      in Experience Management , the language selection option is played to the customer. |
|---|---|

| Note | For a sample template script, see /wfavvid/Scripts/Templates/WXM/wxm_survey.aef which gets installed automatically when Unified CCX editor web launcher is launched. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | The partner hosted module in the Experience Management Invitations solution is mandatory for the SMS/Email surveys to work. For information about partner hosted module, see https://xm.webex.com/docs/cxsetup/guides/partnerarchitecture/ For information about how to provision the infrastructure required to deploy the partner hosted components of the Experience Management Invitations module, see https://xm.webex.com/docs/cxsetup/guides/partnerinfra/ . For information about how to provision the infrastructure required to deploy the partner hosted components, see https://xm.webex.com/docs/cxsetup/guides/partnerdeployment/ |
| 2 | Configure the Experience Management Invitation module for sending SMS/Email surveys to the customer. Create dispatch templates on Experience Management . For information about setting up dispatch in Experience Management , see https://xm.webex.com/docs/cxsetup/guides/ |
| 3 | Configure the Unified CCX Administration to provide an offline SMS/Email survey to the customer. Select the required dispatch template for SMS/Email survey from Enable Cisco Webex Experience Management post-call survey available in the Cisco Script Application page of Unified CCX Administration. For more information, see Cisco Unified Contact Center Express Admin and Operations Guide . |

| Note | You can associate an application with both SMS/Email Experience Management post-call survey and Unified CCX Post-Call Treatment. Legacy Unified CCX post-call survey is triggered only if agent ends
                                          the call from Finesse desktop. SMS/Email survey is triggered irrespective of who ends the call. When both SMS/Email Experience Management post-call survey and Unified CCX Post-Call Treatment are enabled, Unified CCX Post-Call Treatment is triggered and the Experience Management post-call survey is sent. |
|---|---|

| Script Variable | Type | Description |
|---|---|---|
| POD.ID | ECC | In IVR script, populate the POD.ID ECC variable with customer ID because Customer Experience Journey gadget uses this variable to fetch and display all responses that are provided by the calling customer, across all channels.
                                             If the variable is not populated the SMS/Email survey may not work as expected. |
| ccx_survey_opt_in | session | Enabling and Disabling a Survey for a Customer When an application is associated with a Post-Call Survey , by default the survey is presented to all customers after the call ends. If the ccx_survey_opt_in session variable in IVR script is set as false (for a customer, in a particular session), the survey is not presented to that customer. The ccx_survey_opt_in session variable holds a Boolean value. Note The survey that is sent to the customer, is the one that is associated with the first application that is triggered for the
                                                         customer after the call ends. | Note | The survey that is sent to the customer, is the one that is associated with the first application that is triggered for the
                                                         customer after the call ends. |
| Note | The survey that is sent to the customer, is the one that is associated with the first application that is triggered for the
                                                         customer after the call ends. |
| ccx_survey_language | session | Customers' Language Preference When an Unified CCX application is associated with a survey, the script may use the ccx_survey_language session variable in IVR script to add the language preference of the customers. The format of the variable is LanguageCode-CountryCode . For example, en-US . If the ccx_survey_language session variable is not populated in IVR script, by default, the language associated with trigger will be used. To configure
                                             the survey to be played in multiple languages, see Questionnaires . To know the languages that are supported by Experience Management , see Languages . Note When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                         in Experience Management , the customer is asked to choose from the language selection options before accessing the survey. | Note | When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                         in Experience Management , the customer is asked to choose from the language selection options before accessing the survey. |
| Note | When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                         in Experience Management , the customer is asked to choose from the language selection options before accessing the survey. |
| ccx_customer_ani | session | Customer's Phone Number If the ccx_customer_ani session variable is configured with the phone number of the customer in the IVR script then an SMS is sent to this number
                                             when one of the channel associated is SMS. If the phone number is not configured then the phone number of the caller is obtained
                                             from JTAPI. |
| ccx_customer_email_id | session | Customer's Email ID When an Unified CCX application is associated with a survey, the script can use the ccx_customer_email_id session variable in IVR script to add the email address of the customer. This is a mandatory variable for the SMS/Email survey
                                             to work when one of the channel associated is email. |

| Note | The survey that is sent to the customer, is the one that is associated with the first application that is triggered for the
                                                         customer after the call ends. |
|---|---|

| Note | When a customer selects a language through Unified CCX application and if the same language is not configured for that survey
                                                         in Experience Management , the customer is asked to choose from the language selection options before accessing the survey. |
|---|---|

| Note | For a sample template script, see /wfavvid/Scripts/Templates/WXM/wxm_survey.aef directory which gets installed automatically when Unified CCX editor web launcher is launched. |
|---|---|