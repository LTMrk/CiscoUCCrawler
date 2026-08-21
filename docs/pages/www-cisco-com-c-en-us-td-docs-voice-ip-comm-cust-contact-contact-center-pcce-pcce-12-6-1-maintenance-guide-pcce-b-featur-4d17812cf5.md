---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-featur-4d17812cf5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_features-guide-1261/pcce_b_features-guide-1261_chapter_01101.html
retrieved_at: 2026-08-21T16:41:37.447139+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Post Call Survey

## Chapter: Post Call Survey

# Post Call Survey

## Capabilities

A Post Call Survey takes place after usual call treatment. It is typically used to determine whether customers are satisfied
                           with their call center experiences. This feature lets you configure a call flow that, after the agent disconnects from the
                           caller, optionally sends the call to a Dialed Number configured for a Post Call Survey.

The Unified CCE script can
                           enable and disable Post Call Survey on a per-call basis by testing for conditions and setting an expanded call variable that
                           controls post call survey. For example, the script can invoke a prompt  that asks callers whether they want to participate
                           in a survey. Based on the caller's response, the script can set the expanded call variable that controls whether the call
                           gets transferred to the Post Call Survey dialed number.

The Post Call
                           Survey call works just like a regular call from the Unified CCE point of view. Scripts can be invoked and the customer can
                           use the
                           keypad on a touch tone phone and/or voice with ASR/TTS to respond to questions
                           asked during the survey. During Post Call Survey, the call context information
                           is retrieved from the original customer call.

### Design
                           	 Considerations

Observe the
                              		following conditions when designing the Post Call Survey feature:

A Post Call Survey is triggered when the outbound call gets disconnected with the called party . When the agent ends the call, the call routing script launches a survey script.

The mapping of a
                                    			 dialed number pattern to a Post Call Survey number enables the Post Call Survey
                                    			 feature for the call.

The value of the
                                    			 expanded call variable user.microapp.isPostCallSurvey controls whether the
                                    			 call is transferred to the Post Call Survey number.

If user.microapp.isPostCallSurvey is set to y (the implied default), the call is transferred to
                                          				  the mapped post call survey number.

If user.microapp.isPostCallSurvey is set to n , the call ends.

To route all
                                          				  calls in the dialed number pattern to the survey, your script does not have to
                                          				  set the user.microapp.isPostCallSurvey variable. The
                                          				  variable is set to y by default.

REFER call flows
                                    			 are not supported with Post Call Survey. The two features conflict: REFER call
                                    			 flows remove Unified CVP from the call and Post Call Survey needs Unified CVP
                                    			 because the agent has already disconnected.

For Unified CCE
                                    			 reporting purposes, when a survey is initiated, the call context of the
                                    			 customer call that was just transferred to the agent is replicated into the
                                    			 call context of the Post Call Survey call.

## Initial Setup

To set up the Post Call Survey feature:

Step 1

Create one or more survey scripts and add the files to the CVP media servers. See Create a Survey Script .

Step 2

Configure Unified CCE for Post Call Survey. This step adds a required expanded call context variable, adds a new call type
                                       for Post Call Survey, maps incoming dialed number to a survey dialed number pattern, and associates your survey dialed number
                                       patterns to the survey call type. See Configure Packaged CCE for Post Call Survey .

Step 3

Modify your Unified CCE call routing scripts to launch the survey scripts. See Modify CCE Scripts for Post Call Survey .

The scripts can optionally contain nodes that test for conditions and dynamically control whether a call is transferred to
                                          the survey.

### Create a Survey  Script

To create a survey script or application that queries the caller for information, use the CVP Call Studio tool. For more information
                                 on Unified CVP Call Studio, see User Guide for Cisco Unified CVP VXML Server and Unified Call Studio .

#### What to do next

Map  CVP  dialed number patterns to  the survey script numbers.

### Configure Packaged CCE for Post Call Survey

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

### Modify CCE Scripts for Post Call Survey

In Script Editor, modify your CCE call routing scripts for incoming calls as follows:

Add  nodes  to invoke the call studio survey script, if needed. The following notes explain when you might need to explicitly
                                    add nodes to call the survey script.

If a DN is mapped  for Post Call Survey, the call is automatically transferred to the configured Post Call Survey dialed number.

Optionally, you can add nodes in the script to test for conditions for which you want to turn the survey off.

To dynamically control whether the survey is offered to callers, you must explicitly set the user.microapp.isPostCallSurvey expanded call context variable to y and n .

To offer the survey to all callers, you do not need to set the variable in the script. It is set to y by default.

Configure the expanded call context variable to a value of n or y before the  Queue to Skillgroup node. This sends the correct value to Unified CVP before the agent transfer.

The following example calls a script that asks callers if they want to participate in a survey. The script then sets the user.microapp.isPostCallSurvey variable according to the caller's response.

Create a routing script for the Post Call Survey Call Type to play your survey script or application to the caller. The following
                              script is an example:

## Administration and Usage

### Get Survey
                           	 Results

To obtain survey
                                 		  results, you query or create a report that gathers survey data from the CVP
                                 		  database.

For more information
                                 		  on how to configure a Data Source, see the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

Step 1

In Cisco
                                          			 Unified Intelligence Center Reporting tool, connect to the CVP database.

Step 2

Create a query
                                          			 that identifies survey calls, gathers call information from those calls, and
                                          			 extracts data related to specific survey dialed numbers:

In the
                                                				  Call_Type table, test for Event_Type = Post_Call_Survey.

If true, use
                                                				  that entry's call information to query the VXML_Element table and get the VXML
                                                				  data for the call.

In the VXML
                                                				  data, you can identify the exact survey that a caller participated in from the
                                                				  dialed number used to place the Post Call Survey.

Step 3

To report on the
                                          			 results of a particular survey, collate the VXML data for all calls with that
                                          			 survey's dialed number.

Step 4

To identify
                                          			 answers to survey questions, in the CauseRef table, the CauseID is 20, and the
                                          			 Cause is Post Call Answer.

| Note | The call context for the post call
                                    survey includes all context up to the point where the call is transferred to
                                    the agent. Context that the agent creates after the transfer is not included in
                                    the post call survey context. |
|---|---|

| Step 1 | Create one or more survey scripts and add the files to the CVP media servers. See Create a Survey Script . |
|---|---|
| Step 2 | Configure Unified CCE for Post Call Survey. This step adds a required expanded call context variable, adds a new call type
                                       for Post Call Survey, maps incoming dialed number to a survey dialed number pattern, and associates your survey dialed number
                                       patterns to the survey call type. See Configure Packaged CCE for Post Call Survey . |
| Step 3 | Modify your Unified CCE call routing scripts to launch the survey scripts. See Modify CCE Scripts for Post Call Survey . The scripts can optionally contain nodes that test for conditions and dynamically control whether a call is transferred to
                                          the survey. |

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

| Note | The Post Call Survey dialed number is only called if the script ends with a call to
                                             an agent. If the script completes without
                                             going to an agent then the call is not directed to the Post Call
                                             Survey dialed number . In these cases, you can, for example, use a Send to
                                                Script node in your Unified CCE script to direct the call to the
                                             Post Call Survey script. |
|---|---|

| Step 1 | In Cisco
                                          			 Unified Intelligence Center Reporting tool, connect to the CVP database. |
|---|---|
| Step 2 | Create a query
                                          			 that identifies survey calls, gathers call information from those calls, and
                                          			 extracts data related to specific survey dialed numbers: In the
                                                				  Call_Type table, test for Event_Type = Post_Call_Survey. If true, use
                                                				  that entry's call information to query the VXML_Element table and get the VXML
                                                				  data for the call. In the VXML
                                                				  data, you can identify the exact survey that a caller participated in from the
                                                				  dialed number used to place the Post Call Survey. |
| Step 3 | To report on the
                                          			 results of a particular survey, collate the VXML data for all calls with that
                                          			 survey's dialed number. |
| Step 4 | To identify
                                          			 answers to survey questions, in the CauseRef table, the CauseID is 20, and the
                                          			 Cause is Post Call Answer. |