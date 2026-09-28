---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-ucce-b-1501-f415940025
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/ucce_b_1501_features-guide/rcct_m_1501_post-call-survey.html
retrieved_at: 2026-08-16T20:09:29.900299+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Post Call Survey

## Chapter: Post Call Survey

# Post Call Survey

## Post Call Survey

A Post Call Survey takes place after normal call treatment. Typically, you use the survey to determine whether a customer
                           was satisfied with the call experience. You configure a call flow that sends the call to a DNIS for the Post Call Survey after
                           the agent disconnects from the caller.

Your VRU asks callers whether they want to participate in a Post Call Survey. If they choose to do so, they are automatically
                           transferred to the Post Call Survey after the normal call flow completes.

### Use Case

The caller typically receives a prompt asking if they want to participate in a survey after the call. Your solution can determine
                                 based on dialed numbers to invoke the post call survey at the end of a call. When the customer completes the conversation
                                 with an agent, the customer is automatically redirected to a survey. The hang-up event from the last agent in the call triggers
                                 the post call survey.

A customer can use the keypad on a touch tone phone and voice with ASR/TTS to respond to questions asked during the survey.
                                 For the solution, the post call survey call is just like another regular call. The post call survey retrieves the call context
                                 information from the original customer call.

### Design

Observe the following conditions when designing a Post Call Survey:

A Post Call Survey triggers when the outbound call gets disconnected with the called party. When the agent hangs up, the call
                                       routing script launches a survey script.

The mapping of a dialed number pattern to a Post Call Survey number enables the Post Call Survey feature for the call.

The value of the expanded call variable user.microapp.isPostCallSurvey controls whether the call transfers to the Post Call Survey number.

If user.microapp.isPostCallSurvey is set to y (the implied default), the call transfers to the mapped post call survey number.

If user.microapp.isPostCallSurvey is set to n , the call ends.

To route all calls in the dialed number pattern to the survey, your script does not have to set the user.microapp.isPostCallSurvey variable. The variable is set to y by default.

You cannot have a REFER call flow with Post Call Survey. REFER call flows remove Unified CVP from the call. But, Post Call
                                       Survey needs Unified CVP because the agent has already disconnected.

For Unified CCE reporting purposes, the Post Call Survey call inherits the call context for the initial call. When a survey starts, the call
                                       context of the customer call that was transferred to the agent replicates into the call context of the Post Call Survey call.

The expanded call variable isPostCallSurvey will be cached only when the Unified CCE router generates a label for CVP.

## Configure Post Call Survey in CVP

Step 1

Log in to the Unified CVP Operations Console and choose System > Dialed Number Pattern .

Step 2

Enter the following configuration settings to associate incoming dialed numbers with survey numbers:

Dialed Number Pattern —Enter the appropriate dialed number.

The incoming Dialed Number for calls being directed to a Post Call Survey Dialed. This is the Dialed Number you want to redirect
                                                to the survey.

Enable Post Call Survey for Incoming Calls —Select to enable post call survey for incoming calls.

Survey Dialed Number Pattern —Enter the dialed number of the Post Call Survey. This is the dialed number to which the calls should be transferred to after
                                                the normal call flow completes.

Click Save to save the Dialed Number Pattern.

Step 3

Click Deploy to deploy the configuration to all Unified CVP Call Server devices.

### Configure Unified CCE

## Configure the ECC Variable

You need not configure Unified CCE to use Post Call Survey, however, you can turn the feature off (and then on again) within an ICM script by using the ECC
                              variable user.microapp.isPostCallSurvey and a value of n or y (value is case insensitive) to disable and re-enable the feature.

Configure the ECC variable to a value of n or y before the label node or before the Queue to Skillgroup node. This sends the correct value to Unified CVP before the agent
                              transfer. This ECC variable is not needed to initiate a Post Call Survey call, but you can use it to control the feature when
                              the Post Call Survey is configured using the Operations Console.

When the DN is mapped in the Operations Console for Post Call Survey, the call automatically transfers to the configured Post
                              Call Survey DN.

Complete the following procedure to enable or disable the Post Call Survey:

Step 1

On the Unified CCE Administration Workstation, using configuration manager, select the Expanded Call Variable List tool .

Step 2

Create a new ECC Variable with Name:user.microapp.isPostCallSurvey .

Step 3

Set Maximum Length to 1.

Step 4

Select the Enabled check box then click Save .

| Step 1 | Log in to the Unified CVP Operations Console and choose System > Dialed Number Pattern . |
|---|---|
| Step 2 | Enter the following configuration settings to associate incoming dialed numbers with survey numbers: Dialed Number Pattern —Enter the appropriate dialed number. The incoming Dialed Number for calls being directed to a Post Call Survey Dialed. This is the Dialed Number you want to redirect
                                                to the survey. Enable Post Call Survey for Incoming Calls —Select to enable post call survey for incoming calls. Survey Dialed Number Pattern —Enter the dialed number of the Post Call Survey. This is the dialed number to which the calls should be transferred to after
                                                the normal call flow completes. Click Save to save the Dialed Number Pattern. |
| Step 3 | Click Deploy to deploy the configuration to all Unified CVP Call Server devices. |

| Step 1 | On the Unified CCE Administration Workstation, using configuration manager, select the Expanded Call Variable List tool . |
|---|---|
| Step 2 | Create a new ECC Variable with Name:user.microapp.isPostCallSurvey . |
| Step 3 | Set Maximum Length to 1. |
| Step 4 | Select the Enabled check box then click Save . |