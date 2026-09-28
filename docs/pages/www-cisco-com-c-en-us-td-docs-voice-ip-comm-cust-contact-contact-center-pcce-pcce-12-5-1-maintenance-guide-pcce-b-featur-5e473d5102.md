---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-featur-5e473d5102
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_features_guide_12_5/pcce_b_pcce_features_guide_12_5_chapter_010101.html
retrieved_at: 2026-08-21T04:48:12.113468+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1)

Updated: July 29, 2021

Chapter: Webex Experience Management

## Chapter: Webex Experience Management

# Webex Experience Management

## Experience Management Overview

To enable this feature in Packaged CCE , install the following patches:

ICM 12.5(1)_ES7

CVP 12.5(1)_ES6

Cloud Connect 12.5(1)ES1

Finesse 12.5(1)ES2

Cisco Webex Experience Management is a Customer Experience Management (CEM) platform that allows
                           you to see your business from your customers' perspective. To know more about Webex
                           Expereince Management, see https://xm.webex.com/docs/ccoverview/ .

With Webex Experience Management, Packaged CCE supports:

Customer experience surveys - Set up and send surveys to customers, after an interaction, to collect feedback about their
                                 interaction.

Customer Experience Journey (CEJ) gadget - Displays all the past survey responses from a customer in a chronological list. The agent and supervisor use this
                                 gadget to gain context about the customers past experiences with the business and engage with them appropriately.

Customer Experience Analytics (CEA) gadget - Displays the overall experience of the customer interaction with agents using industry-standard metrics such as
                                 NPS, CSAT, and CES or other KPIs tracked within Experience Management. This gadget is available for agents and supervisors.

## Experience Management  Survey

Experience Management post-call survey is used to determine whether the customers are satisfied with their voice call experiences.
                           You can configure Experience Management to initiate this survey when an agent disconnects from the caller. The survey can
                           be done in three modes—voice, SMS, or email.

The CCE script enables or disables voice call survey for each call by testing for conditions and setting an expanded call
                           variable that controls Experience Management. For example, the script can invoke a prompt that asks callers whether they want
                           to participate in a survey. Based on the caller's response, the script sets the expanded call variable that controls whether
                           the call gets transferred to the voice call survey Dialed Number.

You can send post call survey links through email or SMS also. After every call, the customer is provided with a choice to
                           participate in the survey and answer few questions over email or their phone. For more information on how to configure or
                           to associate the survey, refer to the section Configure Packaged CCE for Experience Management Voice, SMS and Email Survey .

Experience Management supports G.711 u-law and G.711 a-law codecs.

### Experience Management Task Flow

To enable Experience Management Post Call Survey in Cisco Packaged CCE , follow this task flow:

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

Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Create VM for Cloud Connect Publisher and Create VM for Cloud Connect Subscriber sections in Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

Step 6

Provision Experience Management service using CLI on Cloud Connect. For more information, see Provision Experience Management Service on Cloud Connect .

Step 7

Configure Cloud Connect in Unified CCE Admininstration. For details on how to do this, see Configure Cloud Connect section in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Step 8

Configure Packaged CCE for Post Call Survey. For more information, see Configure Packaged CCE for Post Call Survey .

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

Configure Packaged CCE Experience Management . For more information, see the topic Configure Packaged CCE for Experience Management Voice, SMS and Email Survey .

Step 12

Configure Dialed Number and Call Type for Incoming Call and Experience
                                          Management post call survey routing script. For more information, see Configure Dialed Number and Call Type .

Step 13

Modify CCE scripts. For more information, see Experience Management Scripting in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Associate the CCE script with the Call Type created in the previous step.

Step 14

Add Experience Management gadgets into Finesse desktop layout. For more information, see Cisco Webex Experience Management Gadgets .

## Provision Experience Management Service on Cloud Connect

Provision Experience Management service using the following CLI on Cloud Connect.

```
set cloudconnect cherrypoint config
```

Configure Cloud Connect in Packaged CCE Admininstration. For details on how to do this, see Configure Cloud Connect topic at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

The partner hosted module which is a part of Experience Management Invitations solution is required to send surveys to customers
                           over emails and SMS.

For information about Partner Hosted Module Architecture refer to https://xm.webex.com/docs/cxsetup/guides/partnerarchitecture/

For information about how to provision the infrastructure required to deploy the partner hosted
                           components of the Experience Management Invitations module, see https://xm.webex.com/docs/cxsetup/guides/partnerinfra/ .

For information about how to deploy the partner hosted components on the Experience Management
                           Invitations module once the infrastructure is provisioned, see https://xm.webex.com/docs/cxsetup/guides/partnerdeployment/ .

## Configure Packaged CCE for Post Call Survey

You can enable and disable Post Call Survey within a CCE routing script by using the ECC variable variableuser.microapp.isPostCallSurvey . A value of n or y disables and enables the feature. (The value is case-insensitive.)

Configure the ECC variable to a value of n or y before either the label node or the Queue to Skillgroup node. This configuration
                              sends the correct value to Unified CVP before the agent transfer. This ECC variable is not needed to initiate a Post Call
                              Survey call, but you can use it to control the feature once Post Call Survey is configured in the Unified CCE Administration.
                              Dialed Number is mapped to the Post Call Survey Dialed Number patter to automatically transfer the call.

The Post Call Survey DN is called if the Unified CVP has received at least one CONNECT message from CCE (either from the VRU
                                                leg or from the Agent leg). Use the END node in your CCE routing script if the Post Call Survey is not required for the calls
                                                disconnected from the IVR.

If Router Requery is configured incorrectly and the Ring-No-Answer timeout expires, the caller is still transferred to the
                                                Post Call Survey DN. This can occur if a Queue node is used and Enable target requery is not checked.

Step 1

In Unified CCE Administration, navigate to Overview > Call Settings > Route Settings > Expanded Call Variables .

Step 2

Click New to open the New Expanded Call Variable window.

Step 3

Create a new ECC variable with Name: user.microapp.isPostCallSurvey .

Step 4

Set Max Length: to 1.

Step 5

Check the Enabled checkbox. Then click Save .

In your CCE routing scripts, remember that, at script start, the default behavior of Post Call Survey equals enabled , even if user.microapp.isPostCallSurvey has not yet been set in the script. You can turn off Post Call Survey in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y .

Step 6

Navigate to Overview > Call Settings > Route Settings > Call Types .

Step 7

Add the call type for Post Call Survey, and click Save .

Step 8

Navigate to Overview > Call Settings > Route Settings > Dialed Numbers .

Step 9

Click New and complete the following fields:

Dialed Number String

yes

The value used to route the call, which is the Post Call Survey Dialed Number. Enter a string value that is unique for the
                                                      routing type, maximum of 25 characters.

The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site.

Description

no

Enter a maximum of 255 characters to describe the dialed number string.

Department

yes (for departmental administrators)

A departmental administrator must select one department from the popup list to associate with this dialed number. The list
                                                      shows all this administrator's departments.

When a departmental administrator selects a department for the dialed number, the popup list for call type includes global
                                                      call types and call types in the same department as the dialed number.

A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number.

When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department.

Routing Type

yes

From the drop-down menu, select Post Call Survey: .

Post Call Survey: Select this option for Post Call Survey dialed number strings that apply to voice calls coming from Cisco Unified Customer
                                                      Voice Portal (CVP). This option is similar to External Voice where the calls comes from outside of the enterprise through
                                                      a gateway. However, Unified CVP directs the calls internally to Post Call Survey after agent ends the call. This option allows
                                                      you to enter the Post Call Survey Dialed Number and associate the Dialed Number Patterns to the Post Call Survey Dialed Number.

For remote sites, the Post Call Survey option is available if the site is configured to VRU PG.

Media Routing Domain

no

The Media Routing Domain associated with the dialed number. Media Routing Domains (MRDs) organize how requests for media are
                                                      routed. The system routes calls to agents who are associated with a particular communication medium; for example, voice or
                                                      email. The selection of Routing Type determines what appears in this field.

If the Routing Type is External Voice, Internal Voice, or Outbound Voice, the Media Routing Domain is Cisco_Voice and you
                                                            cannot change it.

If the Routing Type is Multichannel, click the magnifying glass icon to display the Select Media Routing Domain popup window.

Call Type

no

Use the drop-down menu to select the call type that you created for Post Call Survey.

PCS Enabled Dialed Number Patterns

no

The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey .

Enter one or more dialed number patterns that allow calls to transfer to the Post Call Survey dialed number entered in the Dialed Number String field.

The field allows maximum of 512 characters that can have the comma separated list without any spaces. Both alphanumeric and
                                                      special characters are supported.

Ringtone Media File

no

The Ringtone Media File field appears if the Routing Type is External Voice .

Enter filename of the custom ringtone - maximum of 256 characters without any spaces.

Step 10

Click Save .

Step 11

Restart the active generic PG (side A or B) to register the new ECC variable.

The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. Therefore, if you do not
                                                      want the survey to run, without first reaching an agent (such as 'after hours of treatment'), you must set the isPostCallSurvey
                                                      to n before the initial 'Run script request'.

## Configure Packaged CCE for Experience Management Voice, SMS and Email Survey

## Configure Expanded Call Variables

Step 1

In Unified CCE Administration, navigate to Overview > Call Settings > Route Settings > Expanded Call Variables .

Step 2

From the list of ECC variables, click on the user.microapp.isPostCallSurvey variable to open it.

Set Max Length: to 1.

Check the Enabled checkbox.

Click Save .

In your CCE routing scripts, remember that, at script start, the default behavior of Post Call Survey equals enabled , even if user.microapp.isPostCallSurvey has not yet been set in the script. You can turn off Post Call Survey in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y .

Step 3

Create a new ECC variable with Name: user.CxSurveyInfo .

Set Max Length to 120.

Check the Enabled check box.

Step 4

Click Save .

The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice.

Step 5

Populate the POD. ID variable.

Step 6

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

For more information on Expanded Call Context Variables , see the chapter Expanded Call Variables in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

You can also configure POD.ID from CVP Call Studio. For more information, refer to the topic Configure Call Studio App Data Format in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

## Upload Audio Files for Questions in Experience Management

Experience Management allows you to upload the audio files for post call survey.

To run post-call voice survey, you must either configure Text-To-Speech(TTS) in the voice browser or upload audio prompts in Experience Management.

Create and configure the questionnaires in Experience Management for sending IVR surveys to the customer. For more information on Experience Management , refer to https://xm.webex.com/docs/ccoverview/

For more information on how to create and modify the questionnaires, refer to https://xm.webex.com/docs/cxsetup/questionnaires/ .

## Configure Dialed Number and Call Type

Step 1

In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Types .

Step 2

Click New to open the Call Type window.

Step 3

Enter the Name of the Call Type for Experience Management survey.

Step 4

Click Save You will be re-directed to the List window and the confirmation message is displayed.

Step 5

Navigate to Overview > Call Settings > Route Settings > Dialed Numbers .

Step 6

Click New and complete the following fields:

Dialed Number String

Yes

This value is used to route the call.

Description

No

Enter a maximum of 255 characters to describe the dialed number string.

Department

No

(Yes for departmental administrators)

A departmental administrator must select one department from the pop-up list to associate with this dialed number. The list
                                                      shows all this administrator's departments.

When a departmental administrator selects a department for the dialed number, the pop-up list for call type includes global
                                                      call types and call types in the same department as the dialed number.

A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number.

When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department.

Site

Yes

The Site field displays Main by default for Packaged CCE 2000 Agents deployment .

For Packaged CCE 4000 Agents and 12000 Agents deployments, Site is a mandatory field and has no default value.

To add a site :

Click the magnifying glass icon to display the list of sites .

Select the site .

Peripheral Set

Yes

This field is available only in Packaged CCE 4000 Agents and 12000 Agents deployments.

To add a peripheral set:

Click the magnifying glass icon to display the list of peripheral sets configured for the selected Site .

Select the peripheral set.

Routing Type

Yes

From the drop-down menu, select External Voice.

These calls are referred to as external because they typically come from outside of the enterprise through a gateway. External
                                                      Voice is the selection for calls that come in from customers and must be answered by agents or sent to the VRU.

Media Routing Domain

Yes

The Media Routing Domain associated with the dialed number.

The selection of Routing Type determines what appears in this field. Because the Routing Type is External Voice , the Media Routing Domain is always Cisco_Voice .

Call Type

Yes

Click on the magnifying glass icon. From the Select Call Type pop-up window, enter or select the call type you created in step 3.

Associating a dialed number with a call type ensures appropriate routing and affects reporting.

Ringtone Media File

No

This field appears when the Routing Type is External Voice .

Enter file name of the custom ringtone for the user-defined Dialed Numbers, a maximum of 256 characters without any spaces.

Step 7

Click Save . You will be re-directed to the List window and the confirmation message is displayed.

Step 8

To create the PCS dialed number refer topic, Configure Packaged CCE for Post Call Survey .

### Associate Survey to Call Type in Unified CCE Admin

You can associate the Call Type to the survey only if you have added Cloud Connect in the Inventory page and configured the survey in Webex Experience Management portal.

Only one survey can be associated to a Call Type.

Step 1

In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Types .

The list of all the Call Types are displayed.

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

| Note | To enable this feature in Packaged CCE , install the following patches: ICM 12.5(1)_ES7 CVP 12.5(1)_ES6 Cloud Connect 12.5(1)ES1 Finesse 12.5(1)ES2 |
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
| Step 5 | Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Create VM for Cloud Connect Publisher and Create VM for Cloud Connect Subscriber sections in Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html |
| Step 6 | Provision Experience Management service using CLI on Cloud Connect. For more information, see Provision Experience Management Service on Cloud Connect . |
| Step 7 | Configure Cloud Connect in Unified CCE Admininstration. For details on how to do this, see Configure Cloud Connect section in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| Step 8 | Configure Packaged CCE for Post Call Survey. For more information, see Configure Packaged CCE for Post Call Survey . |
| Step 9 | Import the following certificates to the CVP Server: Cloud Connect certificate Experience Management certificate For details, see the sections Import Cloud Connect Certificate to
                                                Unified CVP Keystore and Import Experience Management
                                                Certificate to Unified CVP Call Server in Configuration
                                                Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 10 | Ensure that the threshold properties (in ivr.properties and sip.properties files) and proxy settings are configured in CVP for Experience Management. For details, see the section Webex Experience Management Configuration in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 11 | Configure Packaged CCE Experience Management . For more information, see the topic Configure Packaged CCE for Experience Management Voice, SMS and Email Survey . |
| Step 12 | Configure Dialed Number and Call Type for Incoming Call and Experience
                                          Management post call survey routing script. For more information, see Configure Dialed Number and Call Type . |
| Step 13 | Modify CCE scripts. For more information, see Experience Management Scripting in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . Associate the CCE script with the Call Type created in the previous step. |
| Step 14 | Add Experience Management gadgets into Finesse desktop layout. For more information, see Cisco Webex Experience Management Gadgets . |

| Note | The Post Call Survey DN is called if the Unified CVP has received at least one CONNECT message from CCE (either from the VRU
                                                leg or from the Agent leg). Use the END node in your CCE routing script if the Post Call Survey is not required for the calls
                                                disconnected from the IVR. If Router Requery is configured incorrectly and the Ring-No-Answer timeout expires, the caller is still transferred to the
                                                Post Call Survey DN. This can occur if a Queue node is used and Enable target requery is not checked. |
|---|---|

| Step 1 | In Unified CCE Administration, navigate to Overview > Call Settings > Route Settings > Expanded Call Variables . |
|---|---|
| Step 2 | Click New to open the New Expanded Call Variable window. |
| Step 3 | Create a new ECC variable with Name: user.microapp.isPostCallSurvey . |
| Step 4 | Set Max Length: to 1. |
| Step 5 | Check the Enabled checkbox. Then click Save . In your CCE routing scripts, remember that, at script start, the default behavior of Post Call Survey equals enabled , even if user.microapp.isPostCallSurvey has not yet been set in the script. You can turn off Post Call Survey in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y . |
| Step 6 | Navigate to Overview > Call Settings > Route Settings > Call Types . |
| Step 7 | Add the call type for Post Call Survey, and click Save . |
| Step 8 | Navigate to Overview > Call Settings > Route Settings > Dialed Numbers . |
| Step 9 | Click New and complete the following fields: Field Required? Description Dialed Number String yes The value used to route the call, which is the Post Call Survey Dialed Number. Enter a string value that is unique for the
                                                      routing type, maximum of 25 characters. Note The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. Description no Enter a maximum of 255 characters to describe the dialed number string. Department yes (for departmental administrators) A departmental administrator must select one department from the popup list to associate with this dialed number. The list
                                                      shows all this administrator's departments. When a departmental administrator selects a department for the dialed number, the popup list for call type includes global
                                                      call types and call types in the same department as the dialed number. A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number. When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department. Routing Type yes From the drop-down menu, select Post Call Survey: . Post Call Survey: Select this option for Post Call Survey dialed number strings that apply to voice calls coming from Cisco Unified Customer
                                                      Voice Portal (CVP). This option is similar to External Voice where the calls comes from outside of the enterprise through
                                                      a gateway. However, Unified CVP directs the calls internally to Post Call Survey after agent ends the call. This option allows
                                                      you to enter the Post Call Survey Dialed Number and associate the Dialed Number Patterns to the Post Call Survey Dialed Number. For remote sites, the Post Call Survey option is available if the site is configured to VRU PG. Media Routing Domain no The Media Routing Domain associated with the dialed number. Media Routing Domains (MRDs) organize how requests for media are
                                                      routed. The system routes calls to agents who are associated with a particular communication medium; for example, voice or
                                                      email. The selection of Routing Type determines what appears in this field. If the Routing Type is External Voice, Internal Voice, or Outbound Voice, the Media Routing Domain is Cisco_Voice and you
                                                            cannot change it. If the Routing Type is Multichannel, click the magnifying glass icon to display the Select Media Routing Domain popup window. Call Type no Use the drop-down menu to select the call type that you created for Post Call Survey. PCS Enabled Dialed Number Patterns no Note The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . Enter one or more dialed number patterns that allow calls to transfer to the Post Call Survey dialed number entered in the Dialed Number String field. The field allows maximum of 512 characters that can have the comma separated list without any spaces. Both alphanumeric and
                                                      special characters are supported. Ringtone Media File no Note The Ringtone Media File field appears if the Routing Type is External Voice . Enter filename of the custom ringtone - maximum of 256 characters without any spaces. | Field | Required? | Description | Dialed Number String | yes | The value used to route the call, which is the Post Call Survey Dialed Number. Enter a string value that is unique for the
                                                      routing type, maximum of 25 characters. Note The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. | Note | The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. | Description | no | Enter a maximum of 255 characters to describe the dialed number string. | Department | yes (for departmental administrators) | A departmental administrator must select one department from the popup list to associate with this dialed number. The list
                                                      shows all this administrator's departments. When a departmental administrator selects a department for the dialed number, the popup list for call type includes global
                                                      call types and call types in the same department as the dialed number. A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number. When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department. | Routing Type | yes | From the drop-down menu, select Post Call Survey: . Post Call Survey: Select this option for Post Call Survey dialed number strings that apply to voice calls coming from Cisco Unified Customer
                                                      Voice Portal (CVP). This option is similar to External Voice where the calls comes from outside of the enterprise through
                                                      a gateway. However, Unified CVP directs the calls internally to Post Call Survey after agent ends the call. This option allows
                                                      you to enter the Post Call Survey Dialed Number and associate the Dialed Number Patterns to the Post Call Survey Dialed Number. For remote sites, the Post Call Survey option is available if the site is configured to VRU PG. | Media Routing Domain | no | The Media Routing Domain associated with the dialed number. Media Routing Domains (MRDs) organize how requests for media are
                                                      routed. The system routes calls to agents who are associated with a particular communication medium; for example, voice or
                                                      email. The selection of Routing Type determines what appears in this field. If the Routing Type is External Voice, Internal Voice, or Outbound Voice, the Media Routing Domain is Cisco_Voice and you
                                                            cannot change it. If the Routing Type is Multichannel, click the magnifying glass icon to display the Select Media Routing Domain popup window. | Call Type | no | Use the drop-down menu to select the call type that you created for Post Call Survey. | PCS Enabled Dialed Number Patterns | no | Note The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . Enter one or more dialed number patterns that allow calls to transfer to the Post Call Survey dialed number entered in the Dialed Number String field. The field allows maximum of 512 characters that can have the comma separated list without any spaces. Both alphanumeric and
                                                      special characters are supported. | Note | The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . | Ringtone Media File | no | Note The Ringtone Media File field appears if the Routing Type is External Voice . Enter filename of the custom ringtone - maximum of 256 characters without any spaces. | Note | The Ringtone Media File field appears if the Routing Type is External Voice . |
| Field | Required? | Description |
| Dialed Number String | yes | The value used to route the call, which is the Post Call Survey Dialed Number. Enter a string value that is unique for the
                                                      routing type, maximum of 25 characters. Note The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. | Note | The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. |
| Note | The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. |
| Description | no | Enter a maximum of 255 characters to describe the dialed number string. |
| Department | yes (for departmental administrators) | A departmental administrator must select one department from the popup list to associate with this dialed number. The list
                                                      shows all this administrator's departments. When a departmental administrator selects a department for the dialed number, the popup list for call type includes global
                                                      call types and call types in the same department as the dialed number. A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number. When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department. |
| Routing Type | yes | From the drop-down menu, select Post Call Survey: . Post Call Survey: Select this option for Post Call Survey dialed number strings that apply to voice calls coming from Cisco Unified Customer
                                                      Voice Portal (CVP). This option is similar to External Voice where the calls comes from outside of the enterprise through
                                                      a gateway. However, Unified CVP directs the calls internally to Post Call Survey after agent ends the call. This option allows
                                                      you to enter the Post Call Survey Dialed Number and associate the Dialed Number Patterns to the Post Call Survey Dialed Number. For remote sites, the Post Call Survey option is available if the site is configured to VRU PG. |
| Media Routing Domain | no | The Media Routing Domain associated with the dialed number. Media Routing Domains (MRDs) organize how requests for media are
                                                      routed. The system routes calls to agents who are associated with a particular communication medium; for example, voice or
                                                      email. The selection of Routing Type determines what appears in this field. If the Routing Type is External Voice, Internal Voice, or Outbound Voice, the Media Routing Domain is Cisco_Voice and you
                                                            cannot change it. If the Routing Type is Multichannel, click the magnifying glass icon to display the Select Media Routing Domain popup window. |
| Call Type | no | Use the drop-down menu to select the call type that you created for Post Call Survey. |
| PCS Enabled Dialed Number Patterns | no | Note The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . Enter one or more dialed number patterns that allow calls to transfer to the Post Call Survey dialed number entered in the Dialed Number String field. The field allows maximum of 512 characters that can have the comma separated list without any spaces. Both alphanumeric and
                                                      special characters are supported. | Note | The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . |
| Note | The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . |
| Ringtone Media File | no | Note The Ringtone Media File field appears if the Routing Type is External Voice . Enter filename of the custom ringtone - maximum of 256 characters without any spaces. | Note | The Ringtone Media File field appears if the Routing Type is External Voice . |
| Note | The Ringtone Media File field appears if the Routing Type is External Voice . |
| Step 10 | Click Save . |
| Step 11 | Restart the active generic PG (side A or B) to register the new ECC variable. If the ECC variable already existed, you can skip this step. Note The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. Therefore, if you do not
                                                      want the survey to run, without first reaching an agent (such as 'after hours of treatment'), you must set the isPostCallSurvey
                                                      to n before the initial 'Run script request'. | Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. Therefore, if you do not
                                                      want the survey to run, without first reaching an agent (such as 'after hours of treatment'), you must set the isPostCallSurvey
                                                      to n before the initial 'Run script request'. |
| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. Therefore, if you do not
                                                      want the survey to run, without first reaching an agent (such as 'after hours of treatment'), you must set the isPostCallSurvey
                                                      to n before the initial 'Run script request'. |

| Field | Required? | Description |
|---|---|---|
| Dialed Number String | yes | The value used to route the call, which is the Post Call Survey Dialed Number. Enter a string value that is unique for the
                                                      routing type, maximum of 25 characters. Note The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. | Note | The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. |
| Note | The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. |
| Description | no | Enter a maximum of 255 characters to describe the dialed number string. |
| Department | yes (for departmental administrators) | A departmental administrator must select one department from the popup list to associate with this dialed number. The list
                                                      shows all this administrator's departments. When a departmental administrator selects a department for the dialed number, the popup list for call type includes global
                                                      call types and call types in the same department as the dialed number. A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number. When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department. |
| Routing Type | yes | From the drop-down menu, select Post Call Survey: . Post Call Survey: Select this option for Post Call Survey dialed number strings that apply to voice calls coming from Cisco Unified Customer
                                                      Voice Portal (CVP). This option is similar to External Voice where the calls comes from outside of the enterprise through
                                                      a gateway. However, Unified CVP directs the calls internally to Post Call Survey after agent ends the call. This option allows
                                                      you to enter the Post Call Survey Dialed Number and associate the Dialed Number Patterns to the Post Call Survey Dialed Number. For remote sites, the Post Call Survey option is available if the site is configured to VRU PG. |
| Media Routing Domain | no | The Media Routing Domain associated with the dialed number. Media Routing Domains (MRDs) organize how requests for media are
                                                      routed. The system routes calls to agents who are associated with a particular communication medium; for example, voice or
                                                      email. The selection of Routing Type determines what appears in this field. If the Routing Type is External Voice, Internal Voice, or Outbound Voice, the Media Routing Domain is Cisco_Voice and you
                                                            cannot change it. If the Routing Type is Multichannel, click the magnifying glass icon to display the Select Media Routing Domain popup window. |
| Call Type | no | Use the drop-down menu to select the call type that you created for Post Call Survey. |
| PCS Enabled Dialed Number Patterns | no | Note The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . Enter one or more dialed number patterns that allow calls to transfer to the Post Call Survey dialed number entered in the Dialed Number String field. The field allows maximum of 512 characters that can have the comma separated list without any spaces. Both alphanumeric and
                                                      special characters are supported. | Note | The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . |
| Note | The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . |
| Ringtone Media File | no | Note The Ringtone Media File field appears if the Routing Type is External Voice . Enter filename of the custom ringtone - maximum of 256 characters without any spaces. | Note | The Ringtone Media File field appears if the Routing Type is External Voice . |
| Note | The Ringtone Media File field appears if the Routing Type is External Voice . |

| Note | The External Voice and Post Call Survey routing types must not have the same dialed number strings for the same site. |
|---|---|

| Note | The PCS Enabled Dialed Number Patterns field appears if the Routing Type is Post Call Survey . |
|---|---|

| Note | The Ringtone Media File field appears if the Routing Type is External Voice . |
|---|---|

| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. Therefore, if you do not
                                                      want the survey to run, without first reaching an agent (such as 'after hours of treatment'), you must set the isPostCallSurvey
                                                      to n before the initial 'Run script request'. |
|---|---|

| Step 1 | In Unified CCE Administration, navigate to Overview > Call Settings > Route Settings > Expanded Call Variables . |
|---|---|
| Step 2 | From the list of ECC variables, click on the user.microapp.isPostCallSurvey variable to open it. Set Max Length: to 1. Check the Enabled checkbox. Click Save . In your CCE routing scripts, remember that, at script start, the default behavior of Post Call Survey equals enabled , even if user.microapp.isPostCallSurvey has not yet been set in the script. You can turn off Post Call Survey in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y . |
| Step 3 | Create a new ECC variable with Name: user.CxSurveyInfo . Set Max Length to 120. Check the Enabled check box. |
| Step 4 | Click Save . Note The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. | Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
| Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                      payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
| Step 5 | Populate the POD. ID variable. For more information on populating this variable, refer to the topic Configure POD.ID . |
| Step 6 | Restart the active VRU PG (side A or B) to register the new ECC variable. If the ECC variable already exists, you can skip this step. Note The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. | Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |
| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                      of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |

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

| Step 1 | In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Types . |
|---|---|
| Step 2 | Click New to open the Call Type window. |
| Step 3 | Enter the Name of the Call Type for Experience Management survey. |
| Step 4 | Click Save You will be re-directed to the List window and the confirmation message is displayed. |
| Step 5 | Navigate to Overview > Call Settings > Route Settings > Dialed Numbers . |
| Step 6 | Click New and complete the following fields: Field Required? Description Dialed Number String Yes This value is used to route the call. Description No Enter a maximum of 255 characters to describe the dialed number string. Department No (Yes for departmental administrators) A departmental administrator must select one department from the pop-up list to associate with this dialed number. The list
                                                      shows all this administrator's departments. When a departmental administrator selects a department for the dialed number, the pop-up list for call type includes global
                                                      call types and call types in the same department as the dialed number. A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number. When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department. Site Yes The Site field displays Main by default for Packaged CCE 2000 Agents deployment . For Packaged CCE 4000 Agents and 12000 Agents deployments, Site is a mandatory field and has no default value. To add a site : Click the magnifying glass icon to display the list of sites . Select the site . Peripheral Set Yes This field is available only in Packaged CCE 4000 Agents and 12000 Agents deployments. To add a peripheral set: Click the magnifying glass icon to display the list of peripheral sets configured for the selected Site . Select the peripheral set. Routing Type Yes From the drop-down menu, select External Voice. These calls are referred to as external because they typically come from outside of the enterprise through a gateway. External
                                                      Voice is the selection for calls that come in from customers and must be answered by agents or sent to the VRU. Media Routing Domain Yes The Media Routing Domain associated with the dialed number. The selection of Routing Type determines what appears in this field. Because the Routing Type is External Voice , the Media Routing Domain is always Cisco_Voice . Call Type Yes Click on the magnifying glass icon. From the Select Call Type pop-up window, enter or select the call type you created in step 3. Associating a dialed number with a call type ensures appropriate routing and affects reporting. Ringtone Media File No This field appears when the Routing Type is External Voice . Enter file name of the custom ringtone for the user-defined Dialed Numbers, a maximum of 256 characters without any spaces. | Field | Required? | Description | Dialed Number String | Yes | This value is used to route the call. | Description | No | Enter a maximum of 255 characters to describe the dialed number string. | Department | No (Yes for departmental administrators) | A departmental administrator must select one department from the pop-up list to associate with this dialed number. The list
                                                      shows all this administrator's departments. When a departmental administrator selects a department for the dialed number, the pop-up list for call type includes global
                                                      call types and call types in the same department as the dialed number. A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number. When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department. | Site | Yes | The Site field displays Main by default for Packaged CCE 2000 Agents deployment . For Packaged CCE 4000 Agents and 12000 Agents deployments, Site is a mandatory field and has no default value. To add a site : Click the magnifying glass icon to display the list of sites . Select the site . | Peripheral Set | Yes | This field is available only in Packaged CCE 4000 Agents and 12000 Agents deployments. To add a peripheral set: Click the magnifying glass icon to display the list of peripheral sets configured for the selected Site . Select the peripheral set. | Routing Type | Yes | From the drop-down menu, select External Voice. These calls are referred to as external because they typically come from outside of the enterprise through a gateway. External
                                                      Voice is the selection for calls that come in from customers and must be answered by agents or sent to the VRU. | Media Routing Domain | Yes | The Media Routing Domain associated with the dialed number. The selection of Routing Type determines what appears in this field. Because the Routing Type is External Voice , the Media Routing Domain is always Cisco_Voice . | Call Type | Yes | Click on the magnifying glass icon. From the Select Call Type pop-up window, enter or select the call type you created in step 3. Associating a dialed number with a call type ensures appropriate routing and affects reporting. | Ringtone Media File | No | This field appears when the Routing Type is External Voice . Enter file name of the custom ringtone for the user-defined Dialed Numbers, a maximum of 256 characters without any spaces. |
| Field | Required? | Description |
| Dialed Number String | Yes | This value is used to route the call. |
| Description | No | Enter a maximum of 255 characters to describe the dialed number string. |
| Department | No (Yes for departmental administrators) | A departmental administrator must select one department from the pop-up list to associate with this dialed number. The list
                                                      shows all this administrator's departments. When a departmental administrator selects a department for the dialed number, the pop-up list for call type includes global
                                                      call types and call types in the same department as the dialed number. A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number. When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department. |
| Site | Yes | The Site field displays Main by default for Packaged CCE 2000 Agents deployment . For Packaged CCE 4000 Agents and 12000 Agents deployments, Site is a mandatory field and has no default value. To add a site : Click the magnifying glass icon to display the list of sites . Select the site . |
| Peripheral Set | Yes | This field is available only in Packaged CCE 4000 Agents and 12000 Agents deployments. To add a peripheral set: Click the magnifying glass icon to display the list of peripheral sets configured for the selected Site . Select the peripheral set. |
| Routing Type | Yes | From the drop-down menu, select External Voice. These calls are referred to as external because they typically come from outside of the enterprise through a gateway. External
                                                      Voice is the selection for calls that come in from customers and must be answered by agents or sent to the VRU. |
| Media Routing Domain | Yes | The Media Routing Domain associated with the dialed number. The selection of Routing Type determines what appears in this field. Because the Routing Type is External Voice , the Media Routing Domain is always Cisco_Voice . |
| Call Type | Yes | Click on the magnifying glass icon. From the Select Call Type pop-up window, enter or select the call type you created in step 3. Associating a dialed number with a call type ensures appropriate routing and affects reporting. |
| Ringtone Media File | No | This field appears when the Routing Type is External Voice . Enter file name of the custom ringtone for the user-defined Dialed Numbers, a maximum of 256 characters without any spaces. |
| Step 7 | Click Save . You will be re-directed to the List window and the confirmation message is displayed. |
| Step 8 | To create the PCS dialed number refer topic, Configure Packaged CCE for Post Call Survey . |

| Field | Required? | Description |
|---|---|---|
| Dialed Number String | Yes | This value is used to route the call. |
| Description | No | Enter a maximum of 255 characters to describe the dialed number string. |
| Department | No (Yes for departmental administrators) | A departmental administrator must select one department from the pop-up list to associate with this dialed number. The list
                                                      shows all this administrator's departments. When a departmental administrator selects a department for the dialed number, the pop-up list for call type includes global
                                                      call types and call types in the same department as the dialed number. A global administrator can leave this field as Global (the default), which sets the dialed number as global (belonging to
                                                      no departments). A global administrator can also select a department for this Dialed Number. When an administrator changes the department, selections for call type are cleared if the selections do not belong to the
                                                      new department or the global department. |
| Site | Yes | The Site field displays Main by default for Packaged CCE 2000 Agents deployment . For Packaged CCE 4000 Agents and 12000 Agents deployments, Site is a mandatory field and has no default value. To add a site : Click the magnifying glass icon to display the list of sites . Select the site . |
| Peripheral Set | Yes | This field is available only in Packaged CCE 4000 Agents and 12000 Agents deployments. To add a peripheral set: Click the magnifying glass icon to display the list of peripheral sets configured for the selected Site . Select the peripheral set. |
| Routing Type | Yes | From the drop-down menu, select External Voice. These calls are referred to as external because they typically come from outside of the enterprise through a gateway. External
                                                      Voice is the selection for calls that come in from customers and must be answered by agents or sent to the VRU. |
| Media Routing Domain | Yes | The Media Routing Domain associated with the dialed number. The selection of Routing Type determines what appears in this field. Because the Routing Type is External Voice , the Media Routing Domain is always Cisco_Voice . |
| Call Type | Yes | Click on the magnifying glass icon. From the Select Call Type pop-up window, enter or select the call type you created in step 3. Associating a dialed number with a call type ensures appropriate routing and affects reporting. |
| Ringtone Media File | No | This field appears when the Routing Type is External Voice . Enter file name of the custom ringtone for the user-defined Dialed Numbers, a maximum of 256 characters without any spaces. |

| Note | Only one survey can be associated to a Call Type. |
|---|---|

| Step 1 | In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Types . The list of all the Call Types are displayed. |
|---|---|
| Step 2 | Click on the Call Type which you want to associate to the Survey. Associate the survey with the last call type before the call is first connected
                                          to an agent. |
| Step 3 | Select the Enable Experience Management check box to associate the Webex Experience Management survey. The Experience Management tab is enabled with the following options: Inline Survey (post-call voice survey) Deferred Survey (post-call Email and SMS survey) |
| Step 4 | Click on the magnifying glass icon, and the configured surveys will be populated in the pop-up window. |
| Step 5 | Select the survey from the pop-up window and click Save . |