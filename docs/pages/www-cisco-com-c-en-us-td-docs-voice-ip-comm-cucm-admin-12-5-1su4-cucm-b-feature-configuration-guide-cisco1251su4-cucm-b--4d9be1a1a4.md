---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-feature-configuration-guide-cisco1251su4-cucm-b--4d9be1a1a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_feature-configuration-guide-cisco1251su4/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_01011.html
retrieved_at: 2026-08-16T16:57:53.453325+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: July 31, 2025

Chapter: Recording

## Chapter: Recording

# Recording

## Recording Overview

Call recording is a Unified Communications Manager feature that enables a recording server to archive agent conversations. Call recording is one of the essential features in
                              call centers, financial institutions and other enterprises. The call recording feature sends copies of the agent and the end-user
                              media streams to the recording server over a SIP trunk. Each media stream is sent separately in an effort to best support
                              a wide range of voice analytic applications.

Unified Communications Manager offers IP phone-based or network-based recording.

In IP phone based recording, recording media is sourced from the phone. The phone forks two media streams to the recording
                                    server.

In network-based recording, recording media can be sourced from either the phone or the gateway. When you implement network-based
                                    recording, the gateway in your network must connect to Unified Communications Manager over a SIP trunk.

Unified Communications Manager supports call recording in both single cluster and multi-cluster environments and offers three different recording modes:

Automatic Silent Recording —Automatic silent recording records all calls on a line appearance automatically. Unified Communications Manager invokes the recording session automatically with no visual indication on the phone that an active recording session is established.

Selective Silent Recording —A supervisor can start or stop the recording session via CTI-enabled desktop. Alternatively, a recording server can invoke
                                    the session based on predefined business rules and events. There is no visual indication on the phone that an active recording
                                    session is established.

Selective User Call Recording —An agent can choose which calls to record. The agent invokes the recording session through CTI-enabled desktop, or by a softkey
                                    or programmable line key. When selective user call recording is used, the Cisco IP phone displays recording session status
                                    messages.

Unified Communications Manager supports recording to a single recording server and can be deployed with CUBE as media proxy to record to more than one recording
                              server.

In multi-fork recording, Unified Communications Manager is connected to CUBE Media Proxy server through SIP trunk. The CUBE Media Proxy server receives two media streams from phone
                                    or gateway and it forks the media streams to one or more recording servers simultaneously.

In recording to single recording servers, Unified Communications Manager is directly connected to recording server through SIP trunk. The phone or the gateway forks two media streams to the recording
                                    server.

### Multi-Fork Recording

The multi-forking feature provides the following benefits:

Adds redundancy and failover to your recording deployment.

Provides additional media streams for speech analysis and monitoring.

Helps organization, such as financial industry, to be compliant to MiFID requirements, that mandate recording of customer
                                       calls to multiple recording servers for redundancy.

When you implement multi-fork recording, you must configure the CUBE Media Proxy server in your network which connects to Unified Communications Manager over a SIP trunk.

For more information on CUBE Media Proxy , see Cisco Unified Border Element Configuration Guide .

Connection from Unified Communications Manager to CUBE Media Proxy server over a SIP trunk must be configured with Early Offer.

The following example illustrates the phone-based recording of multi-fork recording through CUBE Media Proxy.

The following example illustrates the network-based recording of multi-fork recording through CUBE Media Proxy.

For more information on method summary, see  " Cisco Device-Specific Extensions " section of Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1).

#### Supported Platforms

Multi-fork recording through CUBE Media Proxy server is supported on the following Cisco Router Platforms running on Cisco
                                 IOS XE Gibraltar Release 16.10.1:

Cisco 4000 Series-Integrated Services Routers (ISR G3 - ISR4331, ISR4351, ISR4431, ISR4451).

Cisco Aggregated Services Routers (ASR - ASR1001-X, ASR1002-X, ASR1004 with RP2, ASR1006 with RP2).

Cisco Cloud Services Routers (CSR1000V series).

#### Restrictions for Multi-fork recording through CUBE Media Proxy

Multi-fork recording through CUBE Media Proxy server does not support the following:

Video recording.

Secure media (SRTP) forking of non secure calls.

SRTP fall back.

Midcall block.

### Recording Media Source Selection

When you configure network-based recording, you must configure either the phone or the gateway as your preferred source of
                                 recording media for the agent phone line. However, depending on your deployment, Unified Communications Manager may not select your preferred choice as the recording media source. The following table displays the logic Unified Communications Manager uses to select the recording media source.

Preferred Media Source

Media Type

Gateway in call path?

Selected Media Source

Gateway

Unsecure (RTP)

Yes

Gateway

No

Phone

Secure (sRTP)

Yes

Phone

No

Phone

Phone

Unsecure (RTP)

Yes

Phone

No

Phone

Secure (sRTP)

Yes

Phone

No

Phone

#### Alternate Recording Media Source if  the First Choice is Unavailable

If the recording media source that Unified Communications Manager selects is unavailable, Unified Communications Manager attempts to use an alternate source. The following table shows the logic Unified Communications Manager uses to select an alternate source for recording media.

Selected Media Source

Gateway Preferred

Phone Preferred

First attempt

First gateway in call path

Phone

Second attempt

Last gateway in call path

First gateway in call path

Third attempt

Phone

Last gateway in call path

## Recording Prerequisites

Cisco Unified IP Phone support—To view a list of the Cisco Unified IP Phone that support recording, log in to Cisco Unified Reporting and run the Unified CM Phone Feature List report, selecting Record as the feature. For a detailed procedure, see Generate a Phone Feature List .

Gateway support—For details on which gateways support recording, see https://developer.cisco.com/web/sip/wiki/-/wiki/Main/Unified+CM+Recording+Gateway+Requirements .

If you are configuring multiple-stream recording, deploy and configure a CUBE Media Proxy. For details, see the section CUBE Media Proxy in the Cisco Unified Border Element Configuration Guide .

## Recording Configuration Task Flow

### Before you begin

Step 1

Create a Recording Profile

Step 2

Configure SIP Profile for Recording

Optional . Configure the SIP Profile if you want to deliver the Conference Bridge Identifier to the recorder.

Step 3

Configure SIP Trunks for Recording

Step 4

Configure Route Pattern for Recording

Step 5

Configure Agent Phone Line for Recording

Step 6

Enable the built in bridge for your agent phones. Perform one of the following tasks to enable the built-in-bridge for recording:

- Enable Built in Bridge for Cluster

- Enable Built in Bridge for a Phone

The Built in Bridge setting on individual phones overrides the clusterwide defaults.

Step 7

Enable Gateway for Recording

Configure
                                          				Unified Communications services on the gateway.

Step 8

Configure Recording Notification Tones

Step 9

Perform one of
                                       			 the following procedures, depending on whether your phone uses feature buttons
                                       			 or softkeys:

- Configure a Record Feature Button

- Configure a Record Softkey

Configure a
                                          				Record feature button or softkey for your phone.

### Create a Recording Profile

Use this procedure to create a recording profile.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Recording Profile .

Step 2

Click Add New .

Step 3

In the Name field, enter a name for your recording profile.

Step 4

In the Recording Calling Search Space field, select the calling search space that contains the partition with the route pattern that is configured for the recording
                                          server.

Step 5

In the Recording Destination Address field, enter the directory number or the URL of the recording server or the URL of the CUBE Media Proxy server.

Step 6

Click Save .

### Configure SIP Profile for Recording

Use this procedure to deliver the conference bridge identifier to the recorder and configure the SIP Profile.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Step 2

Select the SIP profile that you want to use for your network.

Step 3

Set a value for the Early Offer Support for Voice and Video calls field. SIP trunk from Unified Communications Manager to CUBE Media Proxy server must be enabled for an Early Offer
                                          support and configuration options are Best Effort (no MTP inserted) and Mandatory (insert MTP if needed) .

We recommend that you enable SIP trunk for Mandatory (insert MTP if needed).

Step 4

Check the Deliver Conference Bridge Identifier check box.

Step 5

Click Save .

### Configure SIP Trunks for Recording

Use this procedure to assign the recording server information in the SIP Trunk Configuration window.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Click Add New .

Step 3

From the Trunk Type drop-down list, choose SIP Trunk .

Device Protocol is auto-populated to SIP , which is the only available option.

Step 4

From the Trunk Service Type drop-down list, choose the service type that you want to use in your network. The default value is None .

Step 5

Click Next .

Step 6

In the Destination Address field of the SIP Information pane, enter an IP address, fully qualified domain name, or DNS SRV of the recording server or CUBE Media proxy.

Step 7

From the SIP Profile drop-down list in the SIP Information pane, choose the SIP profile that you want to use in your network.

Step 8

From the Recording Information pane, select one of the following options:

- None—This trunk is not used for recording.

- This trunk connects to a recording-enabled gateway.

- This trunk connects to other clusters with recording-enabled gateways.

Step 9

Click Save .

SIP trunk from Unified Communications Manager to Media Proxy must be enabled for Early Offer support in the SIP Profile that
                                                         is used for this trunk. The configuration options are Mandatory (insert MTP if needed) and Best Effort (no MTP inserted).

### Configure Route Pattern for Recording

Use this procedure to describe the route pattern configurations that are specific to recorders. You must configure a route
                                 pattern that routes to the recording server or CUBE Media Proxy server.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Pattern .

Step 2

Click Add New to create a new route pattern.

Step 3

Complete the fields in the Route Pattern Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 4

For call recording, complete the following fields:

- Pattern —Enter a pattern that matches the recording destination address from the recording profile.

- Gateway/Route List —Choose the SIP trunk or route list  that points to the recording server.

Step 5

Click Save .

### Configure Agent Phone Line for Recording

Use this procedure to configure the agent phone line for recording.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find .

Step 3

Select the agent's phone.

Step 4

In the left Association pane, click the phone line for the agent to view the settings.

Step 5

From the Recording Option drop-down list, choose one of the following options:

- Call Recording Disabled —Calls on this phone line are not recorded.

- Automatic Call Recording Enabled —All calls on this phone line are recorded.

- Selective Call Recording Enabled —Only selected calls on this phone line are recorded.

Step 6

From the Recording Profile drop-down list, choose the recording profile that is configured for the agent.

Step 7

From the Recording Media Source drop-down list, choose whether you want to use the gateway or the phone as the preferred source of recording media.

Step 8

Set the Busy Trigger field to a minimum of 3 if you also have Multilevel Precedence and Preemption (MLPP) configured.

Step 9

Click Save .

### Enable Built in
                           	 Bridge for Cluster

Use this procedure to enable the phone's built in bridge for recording to use the agent phone as the recording media source.

When you set the Built-in-Bridge clusterwide service parameter to enable, the Built-in-Bridge default setting for all phones
                                 in the cluster is changed to enabled. However, the Built-in-Bridge setting in the Phone Configuration window for an individual phone overrides the clusterwide service parameter setting if the default option is not selected
                                 for that phone.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server on which the CallManager service is running.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

Set the Builtin Bridge Enable service parameter to On .

Step 5

Click Save .

### Enable Built in Bridge for a Phone

Use this procedure to enable the Built in Bridge for an individual phone. If the default option is not selected, the Built
                                 in Bridge setting in the Phone Configuration window overrides the clusterwide service parameter.

Optionally, use a service parameter to set the Built in Bridge defaults across the cluster. For more information, see Enable Built in Bridge for Cluster .

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to select the agent phone.

Step 3

From the Built in Bridge drop-down list, choose one of the following options:

- On —The Built in Bridge is enabled.

- Off —The Built in Bridge is disabled.

- Default —The setting of the clusterwide Builtin Bridge Enable service parameter is used.

The recording can fail if the Built-in-Bridge is ON and if you check the Media Termination Point Required check box.

Step 4

Click Save .

### Enable Gateway for Recording

Use this procedure to configure the gateway for recording. You must enable Unified Communications Gateway Services. The following
                                 task flow contains the high-level process to enable Unified Communications Gateway Services.

Step 1

Configure Unified Communications Manager IOS Services on the Device.

Step 2

Configure the XMF Provider.

Step 3

Verify Unified Communications Gateway Services.

For more information, see ASR routers Cisco Unified Border Element (Enterprise) Protocol-Independent Features and Setup Configuration Guide. Cisco IOS XE Release
                                          35 .

For  more information, see ISR routers Cisco Unified Border Element Protocol-Independent Features and Setup Configuration Guide, Cisco IOS Release 15M&T .

### Configure Recording Notification Tones

Use this procedure to configure notification tone to play when calls are recorded. For legal compliance, an explicit notification
                                 in the form of a periodic tone can be made audible to the agent, the caller, or both, to indicate that a recording session
                                 is in progress. This tone can also be disabled.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters.

Step 2

From the Server drop-down list, choose the server on which the Cisco CallManager service is running.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

If you want a notification tone to be played to the agent, set the Play Recording Notification Tone to Observed Target (agent) service parameter to True .

Step 5

If you want a notification tone to be played to the customer, set the value of the Play Recording Notification Tone To Observed Connected Parties (customer) service parameter to True .

Step 6

Click Save .

### Configure a Record Feature Button

Use this procedure to assign the Record feature button to your phone if your phone uses feature buttons.

Step 1

Configure a Phone Button Template for Recording

Configure a phone button template that includes the Record button.

Step 2

Associate a Phone Button Template with a Phone

Associate the phone button template that you set up for recording to the phone.

#### Configure a Phone Button Template for Recording

Use this procedure to create a phone button template that includes the Record feature button.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template .

Step 2

Click Find to display list of supported phone templates.

Step 3

Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step.

Select a default template for the model of phone and click Copy .

In the Phone Button Template Information field, enter a new name for the template.

Click Save .

Step 4

Perform the following steps if you want to add phone buttons to an existing template.

Click Find and enter the search criteria.

Choose an existing template.

Step 5

From the Line drop-down list, choose 
                                             			 feature that you want  to add to the template.

Step 6

Click Save .

Step 7

Perform one
                                             			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them.

#### Associate a Phone Button Template with a Phone

Use this procedure to associate the phone button template that you created for the Record button of the phone.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to display the list of configured phones.

Step 3

Choose the
                                             			 phone to which you want to add the phone button template.

Step 4

In the Phone
                                                				Button Template drop-down list, choose the phone button template
                                             			 that contains the new feature button.

Step 5

Click Save .

### Configure a Record Softkey

Use this procedure to add a Record softkey to the phone, if your phone uses softkeys. The Record softkey is only available
                                 in the Connected call state for the Cisco Chaperone Phone with Feature Hardkeys template.

Step 1

Configure a Softkey Template for Recording

Configure a softkey template that includes the Record softkey.

Step 2

Perform one of the following procedure:

- Associate a Softkey Template with a Phone

- Associate a Softkey Template with a Common Device Configuration

Associate the softkey template to a phone directly, or to a Common Device Configuration. You can then associate the Common
                                             Device Configuration to a group of phones.

#### Configure a Softkey Template for Recording

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template .

Step 2

Perform the following steps to create a new softkey template; otherwise, proceed to the next step.

Click Add New .

Select a default template and click Copy .

Enter a new name for the template in the Softkey Template Name field.

Click Save .

Step 3

Perform the following steps to add softkeys to an existing template.

Click Find and enter the search criteria.

Select the required existing template.

Step 4

Check the Default Softkey Template check box to designate this softkey template as the default softkey template.

If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation.

Step 5

Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                             			 corner and click Go .

Step 6

From the Select
                                                				a Call State to Configure drop-down list, choose the call state for
                                             			 which you want the softkey to display.

Step 7

From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                             			 to change the position of the new softkey.

Step 8

Repeat the previous step to display the softkey in additional call states.

Step 9

Click Save .

Step 10

Perform one
                                             			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                                see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections.

#### Associate a Softkey Template with a Phone

Use this procedure to assign the Record softkey to the phone by associating the softkey template that includes the Record
                                    softkey directly to a phone.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to select the phone to add the softkey template.

Step 3

From the Softkey Template drop-down list, choose the template that contains the new softkey.

Step 4

Click Save .

Step 5

Press Reset to update the phone settings.

#### Associate a Softkey Template with a Common Device Configuration

Use this procedure to add a Record softkey to the phone by associating the softkey template to a Common Device Configuration.

Step 1

Add a Softkey Template to the Common Device Configuration

Step 2

Add Common Device Configuration to Phone

##### Add a Softkey Template to the Common Device Configuration

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration .

Step 2

Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                                proceed to the next step.

Click Add New .

Enter a name for the Common Device Configuration in the Name field.

Click Save .

Step 3

Perform the following steps to add the softkey template to an existing Common Device Configuration.

Click Find and enter the search criteria.

Click an existing Common Device Configuration.

Step 4

In the Softkey Template drop-down list, choose the softkey
                                                			 template that contains the softkey that you want to make available.

Step 5

Click Save .

Step 6

Perform one
                                                			 of the following tasks:

- If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices.

- If you created a new Common Device Configuration, associate the configuration with devices and then restart them.

##### Add Common Device Configuration to Phone

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the phone device to add the softkey template.

Step 3

From the Common Device Configuration drop-down list, choose
                                                				  the common device configuration that contains the new softkey template.

Step 4

Click Save .

Step 5

Click Reset to update the phone settings.

## Recording Call Flow Examples

For call flow examples for both network-based call recording and IP phone-based call recording use cases, refer to Call Recording Examples for Network-Based and Phone-Based Recording at the following URL:

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/configExamples/cucm_b_recording-use-cases.html

## Recording Interactions and Restrictions

Feature

Interactions and Restrictions

Monitoring Tones

Recording Tones take precedence over Monitoring Tones for calls that are both recorded and monitored. If you configure both,
                                          and a call is both recorded and monitored, only the recording tone plays.

Multilevel Precedence and Preemption

If you also have Multilevel Precedence and Preemption (MLPP) configured, you must set the Busy Trigger setting on the agent phone line to a minimum of 3.

Secure Tones

If you configure Secure Tones, the secure tone plays to both call participants at the outset of a secure call, irrespective
                                          of whether Recording Tones are configured.

If you configure both Secure Tones and Recording Tones and the call is secure, the secure tone plays once at the outset of
                                          the call followed by the recording tone.

If you configure Secure Tones, Recording Tones, and Monitoring Tones, and the call is secured, recorded, and monitored, the
                                          secure tone plays once followed by the recording tone. The monitoring tone does not play.

Customer Voice Portal

Agent - customer calls that are routed through the Customer Voice Portal may be recorded using the agent phone as the recording
                                          source.

SIP Proxy Servers

If you are using the gateway as your recording source, you cannot place SIP proxy servers between Unified Communications Manager and the gateway.

Busy Hour Call Completion Rate

Each recording session adds two calls to the Busy Hour Call Completion (BHCC) rate with a minimal impact on CTI resources.

Selective Recording with Media Sense

When you configure Selective Recording, the Media Sense server does not record the consult call during a transfer. For example,
                                          if a call between an agent and a customer is being recorded and the agent initiates a transfer to a second agent, the consult
                                          call that takes place between the two agents, before the call being transferred, is not recorded.

Recording on authenticated phones

To record a call for authenticated phones on the Cisco Unified CM Service Parameter page, set the Authenticated Phone Recording field to Allow Recording . The default value is Do Not Allow Recording . Unified Communications Manager allows call recording for authenticated phones while using a non secure recorder. In case of secure recorder, recording is
                                          allowed only if the recorder supports a Secure Real-Time Transport protocol (SRTP) fallback.

When recording is enabled, the endpoint advertises a single codec and payload, and a select and join conference takes place
                                          in the Unified Communications Manager .

### Recording Calls Do Not Survive Agent Hold

Recording calls get torn down when the agent puts the call on hold, and they get reestablished when the agent resumes the
                              call.

| Note | Connection from Unified Communications Manager to CUBE Media Proxy server over a SIP trunk must be configured with Early Offer. |
|---|---|

| Preferred Media Source | Media Type | Gateway in call path? | Selected Media Source |
|---|---|---|---|
| Gateway | Unsecure (RTP) | Yes | Gateway |
| No | Phone |
| Secure (sRTP) | Yes | Phone |
| No | Phone |
| Phone | Unsecure (RTP) | Yes | Phone |
| No | Phone |
| Secure (sRTP) | Yes | Phone |
| No | Phone |

| Selected Media Source | Gateway Preferred | Phone Preferred |
|---|---|---|
| First attempt | First gateway in call path | Phone |
| Second attempt | Last gateway in call path | First gateway in call path |
| Third attempt | Phone | Last gateway in call path |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create a Recording Profile | Create a
                                       			 recording profile. |
| Step 2 | Configure SIP Profile for Recording | Optional . Configure the SIP Profile if you want to deliver the Conference Bridge Identifier to the recorder. |
| Step 3 | Configure SIP Trunks for Recording | Configure the recorder server or CUBE Media Proxy as a SIP trunk device. |
| Step 4 | Configure Route Pattern for Recording | Create a route pattern that routes to the recorder server or CUBE Media Proxy . |
| Step 5 | Configure Agent Phone Line for Recording | Configure the
                                       			 agent phone line for recording. |
| Step 6 | Enable the built in bridge for your agent phones. Perform one of the following tasks to enable the built-in-bridge for recording: Enable Built in Bridge for Cluster Enable Built in Bridge for a Phone | To use the agent phone as the recording media source you must enable the phone's built in bridge for recording. You can use
                                       a service parameter to set the built in bridge defaults across the cluster, or enable the built in bridge on an individual
                                       phone. Note The Built in Bridge setting on individual phones overrides the clusterwide defaults. | Note | The Built in Bridge setting on individual phones overrides the clusterwide defaults. |
| Note | The Built in Bridge setting on individual phones overrides the clusterwide defaults. |
| Step 7 | Enable Gateway for Recording | Configure
                                          				Unified Communications services on the gateway. |
| Step 8 | Configure Recording Notification Tones | Configure
                                       			 whether you want a notification tone to play when calls are recorded. |
| Step 9 | Perform one of
                                       			 the following procedures, depending on whether your phone uses feature buttons
                                       			 or softkeys: Configure a Record Feature Button Configure a Record Softkey | Configure a
                                          				Record feature button or softkey for your phone. |

| Note | The Built in Bridge setting on individual phones overrides the clusterwide defaults. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Recording Profile . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Name field, enter a name for your recording profile. |
| Step 4 | In the Recording Calling Search Space field, select the calling search space that contains the partition with the route pattern that is configured for the recording
                                          server. |
| Step 5 | In the Recording Destination Address field, enter the directory number or the URL of the recording server or the URL of the CUBE Media Proxy server. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Select the SIP profile that you want to use for your network. |
| Step 3 | Set a value for the Early Offer Support for Voice and Video calls field. SIP trunk from Unified Communications Manager to CUBE Media Proxy server must be enabled for an Early Offer
                                          support and configuration options are Best Effort (no MTP inserted) and Mandatory (insert MTP if needed) . Note We recommend that you enable SIP trunk for Mandatory (insert MTP if needed). | Note | We recommend that you enable SIP trunk for Mandatory (insert MTP if needed). |
| Note | We recommend that you enable SIP trunk for Mandatory (insert MTP if needed). |
| Step 4 | Check the Deliver Conference Bridge Identifier check box. |
| Step 5 | Click Save . |

| Note | We recommend that you enable SIP trunk for Mandatory (insert MTP if needed). |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Trunk Type drop-down list, choose SIP Trunk . Device Protocol is auto-populated to SIP , which is the only available option. |
| Step 4 | From the Trunk Service Type drop-down list, choose the service type that you want to use in your network. The default value is None . |
| Step 5 | Click Next . |
| Step 6 | In the Destination Address field of the SIP Information pane, enter an IP address, fully qualified domain name, or DNS SRV of the recording server or CUBE Media proxy. |
| Step 7 | From the SIP Profile drop-down list in the SIP Information pane, choose the SIP profile that you want to use in your network. |
| Step 8 | From the Recording Information pane, select one of the following options: None—This trunk is not used for recording. This trunk connects to a recording-enabled gateway. This trunk connects to other clusters with recording-enabled gateways. |
| Step 9 | Click Save . Note SIP trunk from Unified Communications Manager to Media Proxy must be enabled for Early Offer support in the SIP Profile that
                                                         is used for this trunk. The configuration options are Mandatory (insert MTP if needed) and Best Effort (no MTP inserted). | Note | SIP trunk from Unified Communications Manager to Media Proxy must be enabled for Early Offer support in the SIP Profile that
                                                         is used for this trunk. The configuration options are Mandatory (insert MTP if needed) and Best Effort (no MTP inserted). |
| Note | SIP trunk from Unified Communications Manager to Media Proxy must be enabled for Early Offer support in the SIP Profile that
                                                         is used for this trunk. The configuration options are Mandatory (insert MTP if needed) and Best Effort (no MTP inserted). |

| Note | SIP trunk from Unified Communications Manager to Media Proxy must be enabled for Early Offer support in the SIP Profile that
                                                         is used for this trunk. The configuration options are Mandatory (insert MTP if needed) and Best Effort (no MTP inserted). |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Pattern . |
|---|---|
| Step 2 | Click Add New to create a new route pattern. |
| Step 3 | Complete the fields in the Route Pattern Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | For call recording, complete the following fields: Pattern —Enter a pattern that matches the recording destination address from the recording profile. Gateway/Route List —Choose the SIP trunk or route list  that points to the recording server. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Select the agent's phone. |
| Step 4 | In the left Association pane, click the phone line for the agent to view the settings. |
| Step 5 | From the Recording Option drop-down list, choose one of the following options: Call Recording Disabled —Calls on this phone line are not recorded. Automatic Call Recording Enabled —All calls on this phone line are recorded. Selective Call Recording Enabled —Only selected calls on this phone line are recorded. |
| Step 6 | From the Recording Profile drop-down list, choose the recording profile that is configured for the agent. |
| Step 7 | From the Recording Media Source drop-down list, choose whether you want to use the gateway or the phone as the preferred source of recording media. |
| Step 8 | Set the Busy Trigger field to a minimum of 3 if you also have Multilevel Precedence and Preemption (MLPP) configured. |
| Step 9 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which the CallManager service is running. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | Set the Builtin Bridge Enable service parameter to On . |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to select the agent phone. |
| Step 3 | From the Built in Bridge drop-down list, choose one of the following options: On —The Built in Bridge is enabled. Off —The Built in Bridge is disabled. Default —The setting of the clusterwide Builtin Bridge Enable service parameter is used. Note The recording can fail if the Built-in-Bridge is ON and if you check the Media Termination Point Required check box. | Note | The recording can fail if the Built-in-Bridge is ON and if you check the Media Termination Point Required check box. |
| Note | The recording can fail if the Built-in-Bridge is ON and if you check the Media Termination Point Required check box. |
| Step 4 | Click Save . |

| Note | The recording can fail if the Built-in-Bridge is ON and if you check the Media Termination Point Required check box. |
|---|---|

| Step 1 | Configure Unified Communications Manager IOS Services on the Device. |
|---|---|
| Step 2 | Configure the XMF Provider. |
| Step 3 | Verify Unified Communications Gateway Services. |

| Note | Recording tone settings override monitoring tone settings when both are enabled for the same call. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters. |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which the Cisco CallManager service is running. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | If you want a notification tone to be played to the agent, set the Play Recording Notification Tone to Observed Target (agent) service parameter to True . |
| Step 5 | If you want a notification tone to be played to the customer, set the value of the Play Recording Notification Tone To Observed Connected Parties (customer) service parameter to True . |
| Step 6 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Phone Button Template for Recording | Configure a phone button template that includes the Record button. |
| Step 2 | Associate a Phone Button Template with a Phone | Associate the phone button template that you set up for recording to the phone. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template . |
|---|---|
| Step 2 | Click Find to display list of supported phone templates. |
| Step 3 | Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step. Select a default template for the model of phone and click Copy . In the Phone Button Template Information field, enter a new name for the template. Click Save . |
| Step 4 | Perform the following steps if you want to add phone buttons to an existing template. Click Find and enter the search criteria. Choose an existing template. |
| Step 5 | From the Line drop-down list, choose 
                                             			 feature that you want  to add to the template. |
| Step 6 | Click Save . |
| Step 7 | Perform one
                                             			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to display the list of configured phones. |
| Step 3 | Choose the
                                             			 phone to which you want to add the phone button template. |
| Step 4 | In the Phone
                                                				Button Template drop-down list, choose the phone button template
                                             			 that contains the new feature button. |
| Step 5 | Click Save . A
                                             			 dialog box is displayed with a message to press Reset to update the phone settings. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Softkey Template for Recording | Configure a softkey template that includes the Record softkey. |
| Step 2 | Perform one of the following procedure: Associate a Softkey Template with a Phone Associate a Softkey Template with a Common Device Configuration | Associate the softkey template to a phone directly, or to a Common Device Configuration. You can then associate the Common
                                             Device Configuration to a group of phones. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template . |
|---|---|
| Step 2 | Perform the following steps to create a new softkey template; otherwise, proceed to the next step. Click Add New . Select a default template and click Copy . Enter a new name for the template in the Softkey Template Name field. Click Save . |
| Step 3 | Perform the following steps to add softkeys to an existing template. Click Find and enter the search criteria. Select the required existing template. |
| Step 4 | Check the Default Softkey Template check box to designate this softkey template as the default softkey template. Note If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation. | Note | If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation. |
| Note | If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation. |
| Step 5 | Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                             			 corner and click Go . |
| Step 6 | From the Select
                                                				a Call State to Configure drop-down list, choose the call state for
                                             			 which you want the softkey to display. |
| Step 7 | From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                             			 to change the position of the new softkey. |
| Step 8 | Repeat the previous step to display the softkey in additional call states. |
| Step 9 | Click Save . |
| Step 10 | Perform one
                                             			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                                see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections. |

| Note | If you
                                                            				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                            designation. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to select the phone to add the softkey template. |
| Step 3 | From the Softkey Template drop-down list, choose the template that contains the new softkey. |
| Step 4 | Click Save . |
| Step 5 | Press Reset to update the phone settings. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add a Softkey Template to the Common Device Configuration |  |
| Step 2 | Add Common Device Configuration to Phone |  |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                                proceed to the next step. Click Add New . Enter a name for the Common Device Configuration in the Name field. Click Save . |
| Step 3 | Perform the following steps to add the softkey template to an existing Common Device Configuration. Click Find and enter the search criteria. Click an existing Common Device Configuration. |
| Step 4 | In the Softkey Template drop-down list, choose the softkey
                                                			 template that contains the softkey that you want to make available. |
| Step 5 | Click Save . |
| Step 6 | Perform one
                                                			 of the following tasks: If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices. If you created a new Common Device Configuration, associate the configuration with devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the phone device to add the softkey template. |
| Step 3 | From the Common Device Configuration drop-down list, choose
                                                				  the common device configuration that contains the new softkey template. |
| Step 4 | Click Save . |
| Step 5 | Click Reset to update the phone settings. |

| Feature | Interactions and Restrictions |
|---|---|
| Monitoring Tones | Recording Tones take precedence over Monitoring Tones for calls that are both recorded and monitored. If you configure both,
                                          and a call is both recorded and monitored, only the recording tone plays. |
| Multilevel Precedence and Preemption | If you also have Multilevel Precedence and Preemption (MLPP) configured, you must set the Busy Trigger setting on the agent phone line to a minimum of 3. |
| Secure Tones | If you configure Secure Tones, the secure tone plays to both call participants at the outset of a secure call, irrespective
                                          of whether Recording Tones are configured. If you configure both Secure Tones and Recording Tones and the call is secure, the secure tone plays once at the outset of
                                          the call followed by the recording tone. If you configure Secure Tones, Recording Tones, and Monitoring Tones, and the call is secured, recorded, and monitored, the
                                          secure tone plays once followed by the recording tone. The monitoring tone does not play. |
| Customer Voice Portal | Agent - customer calls that are routed through the Customer Voice Portal may be recorded using the agent phone as the recording
                                          source. |
| SIP Proxy Servers | If you are using the gateway as your recording source, you cannot place SIP proxy servers between Unified Communications Manager and the gateway. |
| Busy Hour Call Completion Rate | Each recording session adds two calls to the Busy Hour Call Completion (BHCC) rate with a minimal impact on CTI resources. |
| Selective Recording with Media Sense | When you configure Selective Recording, the Media Sense server does not record the consult call during a transfer. For example,
                                          if a call between an agent and a customer is being recorded and the agent initiates a transfer to a second agent, the consult
                                          call that takes place between the two agents, before the call being transferred, is not recorded. To ensure that the consult call is recorded, the agent must press the ‘Record’ softkey when the consult call starts. |
| Recording on authenticated phones | To record a call for authenticated phones on the Cisco Unified CM Service Parameter page, set the Authenticated Phone Recording field to Allow Recording . The default value is Do Not Allow Recording . Unified Communications Manager allows call recording for authenticated phones while using a non secure recorder. In case of secure recorder, recording is
                                          allowed only if the recorder supports a Secure Real-Time Transport protocol (SRTP) fallback. |
| Codec locking for auto recording calls in select and join conference | When recording is enabled, the endpoint advertises a single codec and payload, and a select and join conference takes place
                                          in the Unified Communications Manager . |