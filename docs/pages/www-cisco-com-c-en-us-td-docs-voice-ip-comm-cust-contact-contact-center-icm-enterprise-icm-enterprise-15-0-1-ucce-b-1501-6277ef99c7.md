---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-ucce-b-1501-6277ef99c7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/ucce_b_1501_features-guide/rcct_m_1501_call-transcription.html
retrieved_at: 2026-08-25T00:15:48.032359+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Call Transcription

## Chapter: Call Transcription

# Call Transcription

## Introduction

Unified CCE leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to provide services that assist agents. These
                              services are available for the agents in the Cisco Finesse desktop gadgets.

In the Transcript gadget, you can view in real-time, the voice conversation that was dynamically converted to text.

## Prerequisites

The prerequisites for configuring Call Transcription are:

IOS version 17.18.2 or later supports the Call Transcription feature with SIPREC enhancements on vCUBE Catalyst 8200/8300
                                    platforms, or on ISR 4431, 4451-X, and 4461 CUBE platforms.

The following components must be on release 15.0(1) ES202603 or later: ICM, Unified CVP, Cisco VVB, Finesse, and Cloud Connect.

Ensure that you have selected Media Gateway (MGW) as the mode in the Cisco VVB User Interface. For more information, see the
                                    section Post Installation in the Cisco VVB Installation chapter of the Installation and Upgrade Guide for Cisco Virtualized Voice Browser .

There are no additional license requirements for either the Cisco VVB or the Media Gateway service.

The default setting for SIP.EnableSIPREC in the sip.properties file is false . Change this setting to true to enable SIP Recording (SIPREC).

## Contact Center AI Features Task Flow

Follow this procedure to enable the Contact Center AI (CCAI) Services that equips your Contact Center for Call Transcription
                              Services.

Step 1

Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com .

Step 2

Ensure that the Cloud Connect publisher and subscriber are installed.

For more information, see the Install Cloud Connect section of the Installation chapter in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 3

Import the Cloud Connect certificate to the CVP Server.

For more information, see the section Import the Cloud Connect Certificate section of the Unified CVP Security chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 4

Configure Cloud Connect in the CVP Operations Console (OAMP).

For more information, see the Configure CVP Devices for Cloud Connect section of the Cisco Unified Customer Voice Portal chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Once the Cloud Connect is onboarded, the call server will establish a connection with the cache service hosted on the Cloud
                                          Connect.

Step 5

Register Cloud Connect in the Unified CCE Administration console and configure the proxy details.

For more information, see the Cloud Connect Integration section of the Web Based CCE Administration chapter in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

Step 6

In the Unified CCE Administration console, do the following with the CCAI configuration (created in step 1):

To view and sync the Contact Center AI configuration which is associated with all call types as a global configuration, see Associate Contact Center AI Configuration with All Call Types .

To view, update, or delete the Contact Center AI configuration associated with a specific call type, see Associate Contact Center AI Configuration with a Call Type .

Step 7

By default, the locale is set to English. To use languages other than English, in ICM Script Editor, set the user.microapp.locale variable to the language specified for your conversation profile. For example, set the value of the variable to "es-ES" for
                                       Spanish.

Step 8

Provision Cloud Connect on Cisco Finesse.

For more information, see the Cloud Connect Server Settings section of the Manage System Settings chapter in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Step 9

To add the Call Transcript gadget to the Cisco Finesse desktop layout:

Enable the Call Transcript gadget in Cisco Finesse Administration.

For more information, see the Add Transcript Gadget section of the Manage Desktop Layout chapter in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Enable the Call Transcription service in Unified CCE Administration for an agent or multiple agents together.

For more information, see Contact Center AI Features for Agents .

Once enabled, the Call Transcript gadget appears on the Home tab. For more information on how to use the gadget, see the Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise .

Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                            in Cisco Finesse. For more information, see Configure Multi-Tab Gadget Layout section of the Manage Desktop Layout chapter in the Cisco Finesse Administration Guide .

Step 10

Perform the following steps to configure Media Gateway service on the Cisco VVB:

After you install Cisco VVB, select the mode as Media Gateway (MGW) or Cisco Virtualized Voice Browser (VVB) and Media Gateway
                                             (MGW).

For more information, see the Post Installation section of the Cisco VVB Installation chapter in the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html .

Configure Cloud Connect with VVBs in the Operations Console (NOAMP).

For more information, see the Configure CVP or VVB Devices for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

View the dial number, proxy parameters, and cloud connect parameters for the Media Gateway service.

For more information, see the View Media Gateway Configuration section of the Cisco VVB Configuration chapter in the Cisco Virtualized Voice Browser Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-and-configuration-guides-list.html .

Set the proxy and non-proxy hosts for the Media Gateway service.

For more information, see the CLI Commands chapter of the Operation Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html .

Step 11

Perform the following steps on CVP Operations Console to enable the Media Gateway service:

Set the port for the Media Gateway to 5062 when configuring SIPREC-based forking for the SIP server group.

For more information, see the Edit SIP Server Group section of the Cisco Unified Customer Voice Portal chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configure the dialed number on the CVP and media gateway for media forking.

For more information, see the SIP Service Settings section of the Call Server Configuration chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configure the dial number pattern to enable media forking for incoming calls.

For more information, see the Add and Deploy Dialed Number Pattern section of the Cisco Unified Customer Voice Portal chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configure the dial number pattern to associate the Media Gateway service with media forking.

For more information, see Configure Media Gateway section of the Cisco Unified Customer Voice Portal chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configure the dial number on Unified CVP and the Media Gateway service when you configure the SIP service for the call server.

For more information, see SIP Service Settings section of the Managing Devices chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 12

Follow the steps below to fork media streams using SIPREC in conjunction with the Media Gateway service for call recording
                                       or integration with other services:

Configure the SIP profile to enable SIP recording (SIPREC).

For more information, see Configure SIP Forking to Enable SIP Recording (SIP-REC) .

Configure call routing at the Dial-Peer level in the Session Border Controller (SBC).

For more information, see Configure Call Routing at the Dial-Peer Level in SBC .

For more information, see the SIP Forking and Third-Party GUID Capture chapters in the Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.18.2 at https://www.cisco.com/c/en/us/support/unified-communications/unified-border-element/products-installation-and-configuration-guides-list.html .

Step 13

To enable regionalized media support, refer to the Regional Media Data Center Region Mapping .

## Contact Center AI Configuration

In the Unified CCE Administration console, the Contact Center AI feature tab allows administrators to view the Default Configuration (created or configured in the Cisco Webex Control Hub at https://admin.webex.com/ ) with all the call types (default configuration). Upon associating a configuration with a specific call type, the default
                              configuration (if any) gets overridden for the specific call type.

To access this feature, add Cloud Connect to the inventory in the Unified CCE Administration console and register.

### Associate Contact Center AI Configuration with All Call Types

You can view and sync the Contact Center AI configuration which is associated with all call types.

#### View Contact Center AI Configuration

In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI . The Contact Center AI Configuration displays the Default Configuration .

The default CCAI configuration for AI services as configured in the Control Hub is displayed. It also displays whether the
                                    configuration is in sync or out of sync as per the changes in Control Hub.

#### Sync Contact Center AI Global Configuration

This procedure explains how to sync the Contact Center AI configuration. Upon sync, the latest configuration is fetched from the Control Hub.

Step 1

In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI .

Step 2

In the Contact Center AI Configuration , the Sync button is located on the right side of the screen. Click the Sync button to view the sync status.

This sync button displays the latest AI configuration and updates the last synced time.

### Associate Contact Center AI Configuration with a Call Type

You can view, update, or delete the Contact Center AI configuration associated with a specific call type.

#### View Contact Center AI Configuration

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Type . The Contact Center AI Configuration search box displays the name of the Contact Center AI configuration that was previously associated with the call type.

#### Update Contact Center AI Configuration

You can create a Call Type using the Configuration Manager tool . Use Unified CCE Administration to associate a Contact Center AI configuration with a call type. This procedure explains how to update the Contact Center AI configuration associated with a call type.

Only one configuration can be associated with a call type.

Step 1

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings .

Step 2

Click the Call Type tab and select the call type for which Contact Center AI configuration has to be associated.

Step 3

Click the Contact Center AI tab.

Step 4

In the Contact Center AI Configuration search box, click the search icon. A pop-up window displays a list of Contact Center AI configurations. To use the Cisco native AI feature, select the system defined configuration 'Cisco AI Assistant'.

Step 5

Select the required configuration and click Save .

#### Reset Contact Center AI Configuration

This procedure explains how to reset the Contact Center AI configuration. Upon reset, the previously associated configuration with the call type is cleared from the search box and
                                    the call type is associated to the default configuration.

Step 1

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings .

Step 2

Click the Call Type tab.

Step 3

In the Contact Center AI Configuration search box, next to the configuration name, click the x icon.

Step 4

Click Save .

### Contact Center AI Features for Agents

Contact Center AI features  can be configured for each agent. Administrators and supervisors can enable or disable the features
                                 for an agent or multiple agents together.

#### Enable or Disable Contact Center AI Features for an Agent

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Click on the agent row whose services are to be modified.

Step 3

Click the Contact Center AI tab.

Step 4

To enable or disable the required Contact Center AI Features , check or uncheck the check boxes corresponding to the services.

Step 5

Click Save .

#### Enable or Disable Contact Center AI Features for Multiple Agents

Administrators and supervisors can enable or disable Contact Center AI Features for multiple agents.

All agents must belong to the same site and the same department, or all agents must be global agents. The Edit button is disabled if:

Agents from different sites , departments, or peripheral sets are selected.

A mix of global and departmental agents are selected.

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Check the check box corresponding to each agent whose services you want to edit.

Step 3

Click Edit > Contact Center AI .

If the service is enabled for all the agents selected for editing, the check box is checked.

If the service is disabled for all the agents selected for editing, the check box is unchecked.

If the service is enabled for some agents and disabled for the others, the check box has a dash (—).

Step 4

To enable or disable the Contact Center AI Features , check or uncheck the corresponding check boxes for the services.

Step 5

Click Save , and then click Yes to confirm the changes.

#### Enable or Disable Contact Center AI Features for Agents Using Bulk Job

Administrators can enable or disable Contact Center AI Features for multiple agents using bulk job.

Step 1

Navigate to Unified CCE Administration > Overview > Bulk Import .

Step 2

Click Templates .

The Download Templates popup window opens.

Step 3

Click the Download icon for the Contact Center AI template you want to use.

Step 4

Click OK to close the Download Templates popup window.

Step 5

Open the .csv template in Microsoft Excel.

Step 6

Populate the file as described in the Bulk Contact Center AI Features Content File .

Step 7

Save the populated file to the local machine.

Step 8

Navigate to Unified CCE Administration > Overview > Bulk Import .

Step 9

Click New .

Step 10

In the optional Description field, enter up to 255 characters to describe the bulk job.

Step 11

In the Content file field, choose the file to upload, and then click Save .

##### Bulk Contact Center AI Features Content File

The content file for Contact Center AI bulk job contains the fields given in the following table. Enter the values appropriately in the given fields to enable or
                                       disable Contact Center AI Features for the agents.

Field

Required?

Description

agentId

Agent ID or Username

Existing agentId for which you want to enable or disable the Contact Center AI Features .

You must provide either an agentId or the userName. If both are provided, agentId takes precedence over the userName. If the
                                                   agentId value is left blank, the userName will reference an existing agent.

userName

Username of the agent for which you want to enable or disable the Contact Center AI Features .

If no agent is found with the given username, the Contact Center AI Features association fails.

agentServices

Yes (to enable Contact Center AI Features )

The type of Contact Center AI Features to be associated with the agent. Supported values are AgentAnswers, VAV Transcript, and Transcript. To associate more than
                                                   one services, seperate the values using semicolon (;).

If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                                   with the agent.

## Regional Media Data Center Region Mapping

Contact Center Enterprise (CCE) now extends support for regional media across all supported data center locations. This feature
                              allows both customer and agent media (including audio and SIP signaling) to remain local to a specific geographic region.

To utilize regional media from a country or location that differs from your customer’s organization, it is necessary to configure
                              the appropriate variables in the SIP profile. This configuration must be done within the Cisco Unified Border Element (CUBE)
                              for the Call Transcript feature.

To enable regional media, follow these steps:

Step 1

Access the CUBE console and modify the existing SIP profile configuration, which was used during the setup of Call Transcript.
                                       For more information, see the Create a SIP Profile at the Dial-Peer Level in CUBE section in this guide.

You must execute the configuration command on the third party Session Border Controller (SBCs).

Step 2

Run the following command to add the X-Cisco-Clusterid variable as shown below. This variable is included as a custom SIP header in the outgoing SIP INVITE request from the SBC.

```
request SIP INVITE sip-header Call-Info add "X-Cisco-Clusterid : rtmsClusterId = <Regional Media Variable> ; wxccClusterId = <Cisco CCAI Services Variable>"
```

The x-Cisco-Clusterid variable requires the following key values:

rtmsClusterId : The value of the variable used for Regional Media data center.

wxccClusterId : The value of the variable used for CCAI cloud services data center.

```
request SIP INVITE sip-header Call-Info add "X-Cisco-Clusterid : rtmsClusterId = US1 ; wxccClusterId = US1"
```

The following tables list the variables associated with regional media data centers located in different countries. If your
                                          region is not listed below, ensure that you select the nearest data center location applicable to your region.

Important

Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment.

S. No

Country of Operation

Regional Media Data Center

Regional Media Variable

Cisco CCAI Services Variable

1

Australia

Australia

AS1

ANZ1

2

Indonesia

Singapore

SN1

ANZ1

3

Jordan

United Kingdom

UK1

EU1

4

Malaysia

Singapore

SN1

ANZ1

5

New Zealand

Australia

ANZ1

ANZ1

6

Philippines

Singapore

SN1

ANZ1

7

Singapore

Singapore

SN1

ANZ1

8

South Korea

Japan

JA1

JP1

9

Thailand

Singapore

SN1

ANZ1

10

Vietnam

Singapore

SN1

ANZ1

11

Japan

Japan

JA1

JP1

12

India

India

IN1

IN1

S. No

Country of Operation

Regional Media Data Center

Regional Media Variable

Cisco CCAI Services Variable

1

Austria

Germany

GM1

EU2

2

Belgium

Germany

GM1

EU2

3

Bulgaria

Germany

GM1

EU2

4

Croatia

Germany

GM1

EU2

5

Cyprus

Germany

GM1

EU2

6

Czech Republic

Germany

GM1

EU2

7

Denmark

Germany

GM1

EU2

8

Estonia

Germany

GM1

EU2

9

Finland

Germany

GM1

EU2

10

France

Germany

GM1

EU2

11

Georgia

Germany

GM1

EU2

12

Germany

Germany

GM1

EU2

13

Greece

Germany

GM1

EU2

14

Hungary

Germany

GM1

EU2

15

Ireland

Germany

GM1

EU2

16

Italy

Germany

GM1

EU2

17

Latvia

Germany

GM1

EU2

18

Lithuania

Germany

GM1

EU2

19

Luxembourg

Germany

GM1

EU2

20

Malta

Germany

GM1

EU2

21

Netherlands

Germany

GM1

EU2

22

Norway

Germany

GM1

EU2

23

Poland

Germany

GM1

EU2

24

Portugal

Germany

GM1

EU2

25

Romania

Germany

GM1

EU2

26

Slovakia

Germany

GM1

EU2

27

Slovenia

Germany

GM1

EU2

28

Spain

Germany

GM1

EU2

29

Sweden

Germany

GM1

EU2

30

Switzerland

Germany

GM1

EU2

31

Ukraine

Germany

GM1

EU2

32

United Arab Emirates

Germany

GM1

EU2

Saudi Arabia

United Kingdom

UK1

EU1

34

South Africa

United Kingdom

UK1

EU1

35

South Sudan

United Kingdom

UK1

EU1

36

United Kingdom

United Kingdom

UK1

EU1

S. No

Country of Operation

Regional Media Data Center

Regional Media Variable

Cisco CCAI Services Variable

1

Argentina

United States

US1

US1

2

Aruba

United States

US1

US1

3

Bahamas

United States

US1

US1

4

Belize

United States

US1

US1

5

Bermuda

United States

US1

US1

6

Brazil

United States

US1

US1

7

Caymen Islands

United States

US1

US1

8

Chile

United States

US1

US1

9

Colombia

United States

US1

US1

10

Costa Rica

United States

US1

US1

11

Curacao

United States

US1

US1

12

Dominican Republic

United States

US1

US1

13

Ecuador

United States

US1

US1

14

El Salvador

United States

US1

US1

15

Guatemala

United States

US1

US1

16

Honduras

United States

US1

US1

18

Jamaica

United States

US1

US1

19

Mexico

United States

US1

US1

20

Nicaragua

United States

US1

US1

21

Panama

United States

US1

US1

22

Peru

United States

US1

US1

23

Puerto Rico

United States

US1

US1

24

Trinidad and Tobago

United States

US1

US1

25

United States

United States

US1

US1

26

Canada

Canada

CA1

CA1

Step 3

Enable the POD.ID Extended Call Context (ECC) variable in Unified CCE Configuration Manager > List Tools > Expanded Call Variables List to ensure connectivity with the Cisco Finesse gadget.

After you enable the POD.ID , you must restart the VRU PG during non-production time or a scheduled maintenance window for the changes to take full effect.

## Configure SIP Forking to Enable SIP Recording (SIP-REC)

Run the following CLI Commands on the CUBE terminal to configure the SIP profiles to enable SIP recording:

```
voice class sip-profiles 103
request INVITE sip-header Call-Info add "X-Cisco-Forking: supported" 
!
voice class sip-profiles 999
request INVITE peer-header sip Cisco-Gucid copy "(.*)" u03 
request REINVITE peer-header sip Cisco-Gucid copy "(.*)" u01 
request INVITE sip-header Unsupported add "Unsupported: INVITE Dummy Header" 
request INVITE sip-header Unsupported modify ".*" "Cisco-Gucid:\u03" 
request REINVITE sip-header Unsupported add "Unsupported: Dummy Header" 
request REINVITE sip-header Unsupported modify ".*" "Cisco-Gucid:\u01" 
!
!
!
voice class sip-copylist 100
sip-header Cisco-Gucid

media profile recorder 105
media-type audio
media-recording 939393
!
!
media class 105
recorder profile 105 siprec
```

## Configure Call Routing at the Dial-Peer Level in SBC

Run the following CLI commands on the SBC terminal to receive and match incoming calls at the dial-peer level:

This configuration represents the default Contact Center call flow behavior, and the values shown below are for illustration
                                       purposes only.

```
dial-peer voice 800555 voip
 description GW ingress dial-peer
 session protocol sipv2
 session target sip-server
 incoming called-number 8005551199T
 voice-class sip copy-list 100
 media-class 105
 dtmf-relay rtp-nte h245-signal h245-alphanumeric
 codec g711ulaw
```

Run the following CLI Commands on the SBC terminal to forward calls to the required destination:

This configuration represents the default Contact Center call flow behavior, and the values shown below are for illustration
                                       purposes only.

```
dial-peer voice 80055 voip
 description CVP egress dial-peer
 destination-pattern 8005551199T
 session protocol sipv2
 session target ipv4: <CVP_IP_Address> session transport tcp
 voice-class sip profiles 103
 voice-class sip copy-list 100
 dtmf-relay rtp-nte h245-signal h245-alphanumeric
 codec g711ulaw
 no vad
```

Run the following CLI commands on the CUBE terminal to fork media or signaling usig the SIPREC protocol.

The values for the incoming called-number and destination-pattern shown in the following example are for illustration purposes
                                       only. Ensure you configure these parameters with the appropriate values that correspond to your specific environment and setup.

```
dial-peer voice 939393 voip
 description SIPREC Destination Recorder
 destination-pattern 9393939393
 session protocol sipv2
 session target ipv4: <CVP_IP_Address> session transport tcp
 voice-class sip profiles 999
 codec g711ulaw
```

## Enable or Disable Contact Center AI Features for Agents

Contact Center AI Features can be configured for each agent. Administrators and supervisors can enable or disable the features for an agent or for multiple
                              agents together.

### Enable or Disable Contact Center AI Features for an Agent

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Click on the agent row whose services are to be modified.

Step 3

Click the Contact Center AI tab.

Step 4

To enable or disable the required Contact Center AI Features , check or uncheck the check boxes corresponding to the services.

Step 5

Click Save .

### Enable or Disable Contact Center AI Features for Multiple Agents

Administrators and supervisors can enable or disable Contact Center AI Features for multiple agents.

All agents must belong to the same site and the same department, or all agents must be global agents. The Edit button is disabled if:

Agents from different sites , departments, or peripheral sets are selected.

A mix of global and departmental agents are selected.

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Check the check box corresponding to each agent whose services you want to edit.

Step 3

Click Edit > Contact Center AI .

If the service is enabled for all the agents selected for editing, the check box is checked.

If the service is disabled for all the agents selected for editing, the check box is unchecked.

If the service is enabled for some agents and disabled for the others, the check box has a dash (—).

Step 4

To enable or disable the Contact Center AI Features , check or uncheck the corresponding check boxes for the services.

Step 5

Click Save , and then click Yes to confirm the changes.

### Enable or Disable Contact Center AI Features for Agents using Bulk Job

Step 1

Navigate to Unified CCE Administration > Overview > Bulk Import .

Step 2

Click Templates .

The Download Templates popup window opens.

Step 3

Click the Download icon for the Contact Center AI template you want to use.

Step 4

Click OK to close the Download Templates popup window.

Step 5

Open the .csv template in Microsoft Excel.

Step 6

Populate the file as described in the Bulk Contact Center AI Features Content File .

Step 7

Save the populated file to the local machine.

Step 8

Navigate to Unified CCE Administration > Overview > Bulk Import .

Step 9

Click New .

Step 10

In the optional Description field, enter up to 255 characters to describe the bulk job.

Step 11

In the Content file field, choose the file to upload, and then click Save .

#### Bulk Contact Center AI Services Content File

The content file for Contact Center AI bulk job contains the fields given in the following table. Enter the values appropriately in the given fields to enable or
                                    disable Contact Center AI Features for the agents.

Field

Required?

Description

agentId

Agent ID or Username

Existing agentId for which you want to enable or disable the Contact Center AI Features .

You must provide either an agentId or the userName. If both are provided, agentId takes precedence over the userName. If the
                                                agentId value is left blank, the userName will reference an existing agent.

userName

Username of the agent for which you want to enable or disable the Contact Center AI Features .

If no agent is found with the given username, the Contact Center AI Features association fails.

agentServices

Yes (to enable Contact Center AI Features )

The type of Contact Center AI Features to be associated with the agent. Supported values are AgentAnswers, VAV Transcript, and Transcript. To associate more than
                                                one services, seperate the values using semicolon (;).

If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                                with the agent.

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Note | There are no additional license requirements for either the Cisco VVB or the Media Gateway service. |
|---|---|

| Step 1 | Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services. For more information, see the Create a Contact Center AI configuration article. |
|---|---|
| Step 2 | Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section of the Installation chapter in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 3 | Import the Cloud Connect certificate to the CVP Server. For more information, see the section Import the Cloud Connect Certificate section of the Unified CVP Security chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 4 | Configure Cloud Connect in the CVP Operations Console (OAMP). For more information, see the Configure CVP Devices for Cloud Connect section of the Cisco Unified Customer Voice Portal chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . Once the Cloud Connect is onboarded, the call server will establish a connection with the cache service hosted on the Cloud
                                          Connect. |
| Step 5 | Register Cloud Connect in the Unified CCE Administration console and configure the proxy details. For more information, see the Cloud Connect Integration section of the Web Based CCE Administration chapter in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
| Step 6 | In the Unified CCE Administration console, do the following with the CCAI configuration (created in step 1): To view and sync the Contact Center AI configuration which is associated with all call types as a global configuration, see Associate Contact Center AI Configuration with All Call Types . To view, update, or delete the Contact Center AI configuration associated with a specific call type, see Associate Contact Center AI Configuration with a Call Type . |
| Step 7 | By default, the locale is set to English. To use languages other than English, in ICM Script Editor, set the user.microapp.locale variable to the language specified for your conversation profile. For example, set the value of the variable to "es-ES" for
                                       Spanish. |
| Step 8 | Provision Cloud Connect on Cisco Finesse. For more information, see the Cloud Connect Server Settings section of the Manage System Settings chapter in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
| Step 9 | To add the Call Transcript gadget to the Cisco Finesse desktop layout: Enable the Call Transcript gadget in Cisco Finesse Administration. For more information, see the Add Transcript Gadget section of the Manage Desktop Layout chapter in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . Enable the Call Transcription service in Unified CCE Administration for an agent or multiple agents together. For more information, see Contact Center AI Features for Agents . Once enabled, the Call Transcript gadget appears on the Home tab. For more information on how to use the gadget, see the Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise . Note Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                            in Cisco Finesse. For more information, see Configure Multi-Tab Gadget Layout section of the Manage Desktop Layout chapter in the Cisco Finesse Administration Guide . | Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                            in Cisco Finesse. For more information, see Configure Multi-Tab Gadget Layout section of the Manage Desktop Layout chapter in the Cisco Finesse Administration Guide . |
| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                            in Cisco Finesse. For more information, see Configure Multi-Tab Gadget Layout section of the Manage Desktop Layout chapter in the Cisco Finesse Administration Guide . |
| Step 10 | Perform the following steps to configure Media Gateway service on the Cisco VVB: After you install Cisco VVB, select the mode as Media Gateway (MGW) or Cisco Virtualized Voice Browser (VVB) and Media Gateway
                                             (MGW). For more information, see the Post Installation section of the Cisco VVB Installation chapter in the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html . Configure Cloud Connect with VVBs in the Operations Console (NOAMP). For more information, see the Configure CVP or VVB Devices for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . View the dial number, proxy parameters, and cloud connect parameters for the Media Gateway service. For more information, see the View Media Gateway Configuration section of the Cisco VVB Configuration chapter in the Cisco Virtualized Voice Browser Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-and-configuration-guides-list.html . Set the proxy and non-proxy hosts for the Media Gateway service. For more information, see the CLI Commands chapter of the Operation Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html . |
| Step 11 | Perform the following steps on CVP Operations Console to enable the Media Gateway service: Set the port for the Media Gateway to 5062 when configuring SIPREC-based forking for the SIP server group. For more information, see the Edit SIP Server Group section of the Cisco Unified Customer Voice Portal chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . Configure the dialed number on the CVP and media gateway for media forking. For more information, see the SIP Service Settings section of the Call Server Configuration chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . Configure the dial number pattern to enable media forking for incoming calls. For more information, see the Add and Deploy Dialed Number Pattern section of the Cisco Unified Customer Voice Portal chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . Configure the dial number pattern to associate the Media Gateway service with media forking. For more information, see Configure Media Gateway section of the Cisco Unified Customer Voice Portal chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . Configure the dial number on Unified CVP and the Media Gateway service when you configure the SIP service for the call server. For more information, see SIP Service Settings section of the Managing Devices chapter in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 12 | Follow the steps below to fork media streams using SIPREC in conjunction with the Media Gateway service for call recording
                                       or integration with other services: Configure the SIP profile to enable SIP recording (SIPREC). For more information, see Configure SIP Forking to Enable SIP Recording (SIP-REC) . Configure call routing at the Dial-Peer level in the Session Border Controller (SBC). For more information, see Configure Call Routing at the Dial-Peer Level in SBC . For more information, see the SIP Forking and Third-Party GUID Capture chapters in the Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.18.2 at https://www.cisco.com/c/en/us/support/unified-communications/unified-border-element/products-installation-and-configuration-guides-list.html . |
| Step 13 | To enable regionalized media support, refer to the Regional Media Data Center Region Mapping . |

| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                            in Cisco Finesse. For more information, see Configure Multi-Tab Gadget Layout section of the Manage Desktop Layout chapter in the Cisco Finesse Administration Guide . |
|---|---|

| Note | To access this feature, add Cloud Connect to the inventory in the Unified CCE Administration console and register. |
|---|---|

| Step 1 | In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI . |
|---|---|
| Step 2 | In the Contact Center AI Configuration , the Sync button is located on the right side of the screen. Click the Sync button to view the sync status. This sync button displays the latest AI configuration and updates the last synced time. |

| Note | Only one configuration can be associated with a call type. |
|---|---|

| Step 1 | In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings . |
|---|---|
| Step 2 | Click the Call Type tab and select the call type for which Contact Center AI configuration has to be associated. |
| Step 3 | Click the Contact Center AI tab. |
| Step 4 | In the Contact Center AI Configuration search box, click the search icon. A pop-up window displays a list of Contact Center AI configurations. To use the Cisco native AI feature, select the system defined configuration 'Cisco AI Assistant'. |
| Step 5 | Select the required configuration and click Save . |

| Step 1 | In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings . |
|---|---|
| Step 2 | Click the Call Type tab. |
| Step 3 | In the Contact Center AI Configuration search box, next to the configuration name, click the x icon. |
| Step 4 | Click Save . |

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Click on the agent row whose services are to be modified. |
| Step 3 | Click the Contact Center AI tab. Displays a list of services enabled or disabled for the agent. |
| Step 4 | To enable or disable the required Contact Center AI Features , check or uncheck the check boxes corresponding to the services. |
| Step 5 | Click Save . |

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Check the check box corresponding to each agent whose services you want to edit. |
| Step 3 | Click Edit > Contact Center AI . The Edit Services dialog displays the list of services and status (enabled or disabled). If the service is enabled for all the agents selected for editing, the check box is checked. If the service is disabled for all the agents selected for editing, the check box is unchecked. If the service is enabled for some agents and disabled for the others, the check box has a dash (—). |
| Step 4 | To enable or disable the Contact Center AI Features , check or uncheck the corresponding check boxes for the services. |
| Step 5 | Click Save , and then click Yes to confirm the changes. |

| Step 1 | Navigate to Unified CCE Administration > Overview > Bulk Import . |
|---|---|
| Step 2 | Click Templates . The Download Templates popup window opens. |
| Step 3 | Click the Download icon for the Contact Center AI template you want to use. |
| Step 4 | Click OK to close the Download Templates popup window. |
| Step 5 | Open the .csv template in Microsoft Excel. |
| Step 6 | Populate the file as described in the Bulk Contact Center AI Features Content File . |
| Step 7 | Save the populated file to the local machine. |
| Step 8 | Navigate to Unified CCE Administration > Overview > Bulk Import . |
| Step 9 | Click New . |
| Step 10 | In the optional Description field, enter up to 255 characters to describe the bulk job. |
| Step 11 | In the Content file field, choose the file to upload, and then click Save . |

| Note | Bulk job is available for administrators only when Cloud Connect is added in the inventory and registered on the Control Hub. |
|---|---|

| Field | Required? | Description |
|---|---|---|
| agentId | Agent ID or Username | Existing agentId for which you want to enable or disable the Contact Center AI Features . You must provide either an agentId or the userName. If both are provided, agentId takes precedence over the userName. If the
                                                   agentId value is left blank, the userName will reference an existing agent. |
| userName | Username or Agent ID | Username of the agent for which you want to enable or disable the Contact Center AI Features . If no agent is found with the given username, the Contact Center AI Features association fails. |
| agentServices | Yes (to enable Contact Center AI Features ) | The type of Contact Center AI Features to be associated with the agent. Supported values are AgentAnswers, VAV Transcript, and Transcript. To associate more than
                                                   one services, seperate the values using semicolon (;). If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                                   with the agent. |

| Step 1 | Access the CUBE console and modify the existing SIP profile configuration, which was used during the setup of Call Transcript.
                                       For more information, see the Create a SIP Profile at the Dial-Peer Level in CUBE section in this guide. Note You must execute the configuration command on the third party Session Border Controller (SBCs). | Note | You must execute the configuration command on the third party Session Border Controller (SBCs). |
|---|---|---|---|
| Note | You must execute the configuration command on the third party Session Border Controller (SBCs). |
| Step 2 | Run the following command to add the X-Cisco-Clusterid variable as shown below. This variable is included as a custom SIP header in the outgoing SIP INVITE request from the SBC. Syntax : request SIP INVITE sip-header Call-Info add "X-Cisco-Clusterid : rtmsClusterId = <Regional Media Variable> ; wxccClusterId = <Cisco CCAI Services Variable>" The x-Cisco-Clusterid variable requires the following key values: rtmsClusterId : The value of the variable used for Regional Media data center. wxccClusterId : The value of the variable used for CCAI cloud services data center. Example : request SIP INVITE sip-header Call-Info add "X-Cisco-Clusterid : rtmsClusterId = US1 ; wxccClusterId = US1" The following tables list the variables associated with regional media data centers located in different countries. If your
                                          region is not listed below, ensure that you select the nearest data center location applicable to your region. Important Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment. Table 1. Data Center Location - APAC S. No Country of Operation Regional Media Data Center Regional Media Variable Cisco CCAI Services Variable 1 Australia Australia AS1 ANZ1 2 Indonesia Singapore SN1 ANZ1 3 Jordan United Kingdom UK1 EU1 4 Malaysia Singapore SN1 ANZ1 5 New Zealand Australia ANZ1 ANZ1 6 Philippines Singapore SN1 ANZ1 7 Singapore Singapore SN1 ANZ1 8 South Korea Japan JA1 JP1 9 Thailand Singapore SN1 ANZ1 10 Vietnam Singapore SN1 ANZ1 11 Japan Japan JA1 JP1 12 India India IN1 IN1 Table 2. Data Center Location - EMEA S. No Country of Operation Regional Media Data Center Regional Media Variable Cisco CCAI Services Variable 1 Austria Germany GM1 EU2 2 Belgium Germany GM1 EU2 3 Bulgaria Germany GM1 EU2 4 Croatia Germany GM1 EU2 5 Cyprus Germany GM1 EU2 6 Czech Republic Germany GM1 EU2 7 Denmark Germany GM1 EU2 8 Estonia Germany GM1 EU2 9 Finland Germany GM1 EU2 10 France Germany GM1 EU2 11 Georgia Germany GM1 EU2 12 Germany Germany GM1 EU2 13 Greece Germany GM1 EU2 14 Hungary Germany GM1 EU2 15 Ireland Germany GM1 EU2 16 Italy Germany GM1 EU2 17 Latvia Germany GM1 EU2 18 Lithuania Germany GM1 EU2 19 Luxembourg Germany GM1 EU2 20 Malta Germany GM1 EU2 21 Netherlands Germany GM1 EU2 22 Norway Germany GM1 EU2 23 Poland Germany GM1 EU2 24 Portugal Germany GM1 EU2 25 Romania Germany GM1 EU2 26 Slovakia Germany GM1 EU2 27 Slovenia Germany GM1 EU2 28 Spain Germany GM1 EU2 29 Sweden Germany GM1 EU2 30 Switzerland Germany GM1 EU2 31 Ukraine Germany GM1 EU2 32 United Arab Emirates Germany GM1 EU2 33 Saudi Arabia United Kingdom UK1 EU1 34 South Africa United Kingdom UK1 EU1 35 South Sudan United Kingdom UK1 EU1 36 United Kingdom United Kingdom UK1 EU1 Table 3. Data Center Location - AMER S. No Country of Operation Regional Media Data Center Regional Media Variable Cisco CCAI Services Variable 1 Argentina United States US1 US1 2 Aruba United States US1 US1 3 Bahamas United States US1 US1 4 Belize United States US1 US1 5 Bermuda United States US1 US1 6 Brazil United States US1 US1 7 Caymen Islands United States US1 US1 8 Chile United States US1 US1 9 Colombia United States US1 US1 10 Costa Rica United States US1 US1 11 Curacao United States US1 US1 12 Dominican Republic United States US1 US1 13 Ecuador United States US1 US1 14 El Salvador United States US1 US1 15 Guatemala United States US1 US1 16 Honduras United States US1 US1 18 Jamaica United States US1 US1 19 Mexico United States US1 US1 20 Nicaragua United States US1 US1 21 Panama United States US1 US1 22 Peru United States US1 US1 23 Puerto Rico United States US1 US1 24 Trinidad and Tobago United States US1 US1 25 United States United States US1 US1 26 Canada Canada CA1 CA1 | Important | Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment. | S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | 1 | Australia | Australia | AS1 | ANZ1 | 2 | Indonesia | Singapore | SN1 | ANZ1 | 3 | Jordan | United Kingdom | UK1 | EU1 | 4 | Malaysia | Singapore | SN1 | ANZ1 | 5 | New Zealand | Australia | ANZ1 | ANZ1 | 6 | Philippines | Singapore | SN1 | ANZ1 | 7 | Singapore | Singapore | SN1 | ANZ1 | 8 | South Korea | Japan | JA1 | JP1 | 9 | Thailand | Singapore | SN1 | ANZ1 | 10 | Vietnam | Singapore | SN1 | ANZ1 | 11 | Japan | Japan | JA1 | JP1 | 12 | India | India | IN1 | IN1 | S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | 1 | Austria | Germany | GM1 | EU2 | 2 | Belgium | Germany | GM1 | EU2 | 3 | Bulgaria | Germany | GM1 | EU2 | 4 | Croatia | Germany | GM1 | EU2 | 5 | Cyprus | Germany | GM1 | EU2 | 6 | Czech Republic | Germany | GM1 | EU2 | 7 | Denmark | Germany | GM1 | EU2 | 8 | Estonia | Germany | GM1 | EU2 | 9 | Finland | Germany | GM1 | EU2 | 10 | France | Germany | GM1 | EU2 | 11 | Georgia | Germany | GM1 | EU2 | 12 | Germany | Germany | GM1 | EU2 | 13 | Greece | Germany | GM1 | EU2 | 14 | Hungary | Germany | GM1 | EU2 | 15 | Ireland | Germany | GM1 | EU2 | 16 | Italy | Germany | GM1 | EU2 | 17 | Latvia | Germany | GM1 | EU2 | 18 | Lithuania | Germany | GM1 | EU2 | 19 | Luxembourg | Germany | GM1 | EU2 | 20 | Malta | Germany | GM1 | EU2 | 21 | Netherlands | Germany | GM1 | EU2 | 22 | Norway | Germany | GM1 | EU2 | 23 | Poland | Germany | GM1 | EU2 | 24 | Portugal | Germany | GM1 | EU2 | 25 | Romania | Germany | GM1 | EU2 | 26 | Slovakia | Germany | GM1 | EU2 | 27 | Slovenia | Germany | GM1 | EU2 | 28 | Spain | Germany | GM1 | EU2 | 29 | Sweden | Germany | GM1 | EU2 | 30 | Switzerland | Germany | GM1 | EU2 | 31 | Ukraine | Germany | GM1 | EU2 | 32 | United Arab Emirates | Germany | GM1 | EU2 | 33 | Saudi Arabia | United Kingdom | UK1 | EU1 | 34 | South Africa | United Kingdom | UK1 | EU1 | 35 | South Sudan | United Kingdom | UK1 | EU1 | 36 | United Kingdom | United Kingdom | UK1 | EU1 | S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | 1 | Argentina | United States | US1 | US1 | 2 | Aruba | United States | US1 | US1 | 3 | Bahamas | United States | US1 | US1 | 4 | Belize | United States | US1 | US1 | 5 | Bermuda | United States | US1 | US1 | 6 | Brazil | United States | US1 | US1 | 7 | Caymen Islands | United States | US1 | US1 | 8 | Chile | United States | US1 | US1 | 9 | Colombia | United States | US1 | US1 | 10 | Costa Rica | United States | US1 | US1 | 11 | Curacao | United States | US1 | US1 | 12 | Dominican Republic | United States | US1 | US1 | 13 | Ecuador | United States | US1 | US1 | 14 | El Salvador | United States | US1 | US1 | 15 | Guatemala | United States | US1 | US1 | 16 | Honduras | United States | US1 | US1 | 18 | Jamaica | United States | US1 | US1 | 19 | Mexico | United States | US1 | US1 | 20 | Nicaragua | United States | US1 | US1 | 21 | Panama | United States | US1 | US1 | 22 | Peru | United States | US1 | US1 | 23 | Puerto Rico | United States | US1 | US1 | 24 | Trinidad and Tobago | United States | US1 | US1 | 25 | United States | United States | US1 | US1 | 26 | Canada | Canada | CA1 | CA1 |
| Important | Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment. |
| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable |
| 1 | Australia | Australia | AS1 | ANZ1 |
| 2 | Indonesia | Singapore | SN1 | ANZ1 |
| 3 | Jordan | United Kingdom | UK1 | EU1 |
| 4 | Malaysia | Singapore | SN1 | ANZ1 |
| 5 | New Zealand | Australia | ANZ1 | ANZ1 |
| 6 | Philippines | Singapore | SN1 | ANZ1 |
| 7 | Singapore | Singapore | SN1 | ANZ1 |
| 8 | South Korea | Japan | JA1 | JP1 |
| 9 | Thailand | Singapore | SN1 | ANZ1 |
| 10 | Vietnam | Singapore | SN1 | ANZ1 |
| 11 | Japan | Japan | JA1 | JP1 |
| 12 | India | India | IN1 | IN1 |
| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable |
| 1 | Austria | Germany | GM1 | EU2 |
| 2 | Belgium | Germany | GM1 | EU2 |
| 3 | Bulgaria | Germany | GM1 | EU2 |
| 4 | Croatia | Germany | GM1 | EU2 |
| 5 | Cyprus | Germany | GM1 | EU2 |
| 6 | Czech Republic | Germany | GM1 | EU2 |
| 7 | Denmark | Germany | GM1 | EU2 |
| 8 | Estonia | Germany | GM1 | EU2 |
| 9 | Finland | Germany | GM1 | EU2 |
| 10 | France | Germany | GM1 | EU2 |
| 11 | Georgia | Germany | GM1 | EU2 |
| 12 | Germany | Germany | GM1 | EU2 |
| 13 | Greece | Germany | GM1 | EU2 |
| 14 | Hungary | Germany | GM1 | EU2 |
| 15 | Ireland | Germany | GM1 | EU2 |
| 16 | Italy | Germany | GM1 | EU2 |
| 17 | Latvia | Germany | GM1 | EU2 |
| 18 | Lithuania | Germany | GM1 | EU2 |
| 19 | Luxembourg | Germany | GM1 | EU2 |
| 20 | Malta | Germany | GM1 | EU2 |
| 21 | Netherlands | Germany | GM1 | EU2 |
| 22 | Norway | Germany | GM1 | EU2 |
| 23 | Poland | Germany | GM1 | EU2 |
| 24 | Portugal | Germany | GM1 | EU2 |
| 25 | Romania | Germany | GM1 | EU2 |
| 26 | Slovakia | Germany | GM1 | EU2 |
| 27 | Slovenia | Germany | GM1 | EU2 |
| 28 | Spain | Germany | GM1 | EU2 |
| 29 | Sweden | Germany | GM1 | EU2 |
| 30 | Switzerland | Germany | GM1 | EU2 |
| 31 | Ukraine | Germany | GM1 | EU2 |
| 32 | United Arab Emirates | Germany | GM1 | EU2 |
| 33 | Saudi Arabia | United Kingdom | UK1 | EU1 |
| 34 | South Africa | United Kingdom | UK1 | EU1 |
| 35 | South Sudan | United Kingdom | UK1 | EU1 |
| 36 | United Kingdom | United Kingdom | UK1 | EU1 |
| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable |
| 1 | Argentina | United States | US1 | US1 |
| 2 | Aruba | United States | US1 | US1 |
| 3 | Bahamas | United States | US1 | US1 |
| 4 | Belize | United States | US1 | US1 |
| 5 | Bermuda | United States | US1 | US1 |
| 6 | Brazil | United States | US1 | US1 |
| 7 | Caymen Islands | United States | US1 | US1 |
| 8 | Chile | United States | US1 | US1 |
| 9 | Colombia | United States | US1 | US1 |
| 10 | Costa Rica | United States | US1 | US1 |
| 11 | Curacao | United States | US1 | US1 |
| 12 | Dominican Republic | United States | US1 | US1 |
| 13 | Ecuador | United States | US1 | US1 |
| 14 | El Salvador | United States | US1 | US1 |
| 15 | Guatemala | United States | US1 | US1 |
| 16 | Honduras | United States | US1 | US1 |
| 18 | Jamaica | United States | US1 | US1 |
| 19 | Mexico | United States | US1 | US1 |
| 20 | Nicaragua | United States | US1 | US1 |
| 21 | Panama | United States | US1 | US1 |
| 22 | Peru | United States | US1 | US1 |
| 23 | Puerto Rico | United States | US1 | US1 |
| 24 | Trinidad and Tobago | United States | US1 | US1 |
| 25 | United States | United States | US1 | US1 |
| 26 | Canada | Canada | CA1 | CA1 |
| Step 3 | Enable the POD.ID Extended Call Context (ECC) variable in Unified CCE Configuration Manager > List Tools > Expanded Call Variables List to ensure connectivity with the Cisco Finesse gadget. Note After you enable the POD.ID , you must restart the VRU PG during non-production time or a scheduled maintenance window for the changes to take full effect. | Note | After you enable the POD.ID , you must restart the VRU PG during non-production time or a scheduled maintenance window for the changes to take full effect. |
| Note | After you enable the POD.ID , you must restart the VRU PG during non-production time or a scheduled maintenance window for the changes to take full effect. |

| Note | You must execute the configuration command on the third party Session Border Controller (SBCs). |
|---|---|

| Important | Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment. |
|---|---|

| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable |
|---|---|---|---|---|
| 1 | Australia | Australia | AS1 | ANZ1 |
| 2 | Indonesia | Singapore | SN1 | ANZ1 |
| 3 | Jordan | United Kingdom | UK1 | EU1 |
| 4 | Malaysia | Singapore | SN1 | ANZ1 |
| 5 | New Zealand | Australia | ANZ1 | ANZ1 |
| 6 | Philippines | Singapore | SN1 | ANZ1 |
| 7 | Singapore | Singapore | SN1 | ANZ1 |
| 8 | South Korea | Japan | JA1 | JP1 |
| 9 | Thailand | Singapore | SN1 | ANZ1 |
| 10 | Vietnam | Singapore | SN1 | ANZ1 |
| 11 | Japan | Japan | JA1 | JP1 |
| 12 | India | India | IN1 | IN1 |

| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable |
|---|---|---|---|---|
| 1 | Austria | Germany | GM1 | EU2 |
| 2 | Belgium | Germany | GM1 | EU2 |
| 3 | Bulgaria | Germany | GM1 | EU2 |
| 4 | Croatia | Germany | GM1 | EU2 |
| 5 | Cyprus | Germany | GM1 | EU2 |
| 6 | Czech Republic | Germany | GM1 | EU2 |
| 7 | Denmark | Germany | GM1 | EU2 |
| 8 | Estonia | Germany | GM1 | EU2 |
| 9 | Finland | Germany | GM1 | EU2 |
| 10 | France | Germany | GM1 | EU2 |
| 11 | Georgia | Germany | GM1 | EU2 |
| 12 | Germany | Germany | GM1 | EU2 |
| 13 | Greece | Germany | GM1 | EU2 |
| 14 | Hungary | Germany | GM1 | EU2 |
| 15 | Ireland | Germany | GM1 | EU2 |
| 16 | Italy | Germany | GM1 | EU2 |
| 17 | Latvia | Germany | GM1 | EU2 |
| 18 | Lithuania | Germany | GM1 | EU2 |
| 19 | Luxembourg | Germany | GM1 | EU2 |
| 20 | Malta | Germany | GM1 | EU2 |
| 21 | Netherlands | Germany | GM1 | EU2 |
| 22 | Norway | Germany | GM1 | EU2 |
| 23 | Poland | Germany | GM1 | EU2 |
| 24 | Portugal | Germany | GM1 | EU2 |
| 25 | Romania | Germany | GM1 | EU2 |
| 26 | Slovakia | Germany | GM1 | EU2 |
| 27 | Slovenia | Germany | GM1 | EU2 |
| 28 | Spain | Germany | GM1 | EU2 |
| 29 | Sweden | Germany | GM1 | EU2 |
| 30 | Switzerland | Germany | GM1 | EU2 |
| 31 | Ukraine | Germany | GM1 | EU2 |
| 32 | United Arab Emirates | Germany | GM1 | EU2 |
| 33 | Saudi Arabia | United Kingdom | UK1 | EU1 |
| 34 | South Africa | United Kingdom | UK1 | EU1 |
| 35 | South Sudan | United Kingdom | UK1 | EU1 |
| 36 | United Kingdom | United Kingdom | UK1 | EU1 |

| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable |
|---|---|---|---|---|
| 1 | Argentina | United States | US1 | US1 |
| 2 | Aruba | United States | US1 | US1 |
| 3 | Bahamas | United States | US1 | US1 |
| 4 | Belize | United States | US1 | US1 |
| 5 | Bermuda | United States | US1 | US1 |
| 6 | Brazil | United States | US1 | US1 |
| 7 | Caymen Islands | United States | US1 | US1 |
| 8 | Chile | United States | US1 | US1 |
| 9 | Colombia | United States | US1 | US1 |
| 10 | Costa Rica | United States | US1 | US1 |
| 11 | Curacao | United States | US1 | US1 |
| 12 | Dominican Republic | United States | US1 | US1 |
| 13 | Ecuador | United States | US1 | US1 |
| 14 | El Salvador | United States | US1 | US1 |
| 15 | Guatemala | United States | US1 | US1 |
| 16 | Honduras | United States | US1 | US1 |
| 18 | Jamaica | United States | US1 | US1 |
| 19 | Mexico | United States | US1 | US1 |
| 20 | Nicaragua | United States | US1 | US1 |
| 21 | Panama | United States | US1 | US1 |
| 22 | Peru | United States | US1 | US1 |
| 23 | Puerto Rico | United States | US1 | US1 |
| 24 | Trinidad and Tobago | United States | US1 | US1 |
| 25 | United States | United States | US1 | US1 |
| 26 | Canada | Canada | CA1 | CA1 |

| Note | After you enable the POD.ID , you must restart the VRU PG during non-production time or a scheduled maintenance window for the changes to take full effect. |
|---|---|

| Note | This configuration represents the default Contact Center call flow behavior, and the values shown below are for illustration
                                       purposes only. |
|---|---|

| Note | This configuration represents the default Contact Center call flow behavior, and the values shown below are for illustration
                                       purposes only. |
|---|---|

| Note | The values for the incoming called-number and destination-pattern shown in the following example are for illustration purposes
                                       only. Ensure you configure these parameters with the appropriate values that correspond to your specific environment and setup. |
|---|---|

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Click on the agent row whose services are to be modified. |
| Step 3 | Click the Contact Center AI tab. Displays a list of services enabled or disabled for the agent. |
| Step 4 | To enable or disable the required Contact Center AI Features , check or uncheck the check boxes corresponding to the services. |
| Step 5 | Click Save . |

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Check the check box corresponding to each agent whose services you want to edit. |
| Step 3 | Click Edit > Contact Center AI . The Edit Services dialog displays the list of services and status (enabled or disabled). If the service is enabled for all the agents selected for editing, the check box is checked. If the service is disabled for all the agents selected for editing, the check box is unchecked. If the service is enabled for some agents and disabled for the others, the check box has a dash (—). |
| Step 4 | To enable or disable the Contact Center AI Features , check or uncheck the corresponding check boxes for the services. |
| Step 5 | Click Save , and then click Yes to confirm the changes. |

| Step 1 | Navigate to Unified CCE Administration > Overview > Bulk Import . |
|---|---|
| Step 2 | Click Templates . The Download Templates popup window opens. |
| Step 3 | Click the Download icon for the Contact Center AI template you want to use. |
| Step 4 | Click OK to close the Download Templates popup window. |
| Step 5 | Open the .csv template in Microsoft Excel. |
| Step 6 | Populate the file as described in the Bulk Contact Center AI Features Content File . |
| Step 7 | Save the populated file to the local machine. |
| Step 8 | Navigate to Unified CCE Administration > Overview > Bulk Import . |
| Step 9 | Click New . |
| Step 10 | In the optional Description field, enter up to 255 characters to describe the bulk job. |
| Step 11 | In the Content file field, choose the file to upload, and then click Save . |

| Note | Bulk job is available for administrators only when Cloud Connect is added in the inventory and registered on the Control Hub. |
|---|---|

| Field | Required? | Description |
|---|---|---|
| agentId | Agent ID or Username | Existing agentId for which you want to enable or disable the Contact Center AI Features . You must provide either an agentId or the userName. If both are provided, agentId takes precedence over the userName. If the
                                                agentId value is left blank, the userName will reference an existing agent. |
| userName | Username or Agent ID | Username of the agent for which you want to enable or disable the Contact Center AI Features . If no agent is found with the given username, the Contact Center AI Features association fails. |
| agentServices | Yes (to enable Contact Center AI Features ) | The type of Contact Center AI Features to be associated with the agent. Supported values are AgentAnswers, VAV Transcript, and Transcript. To associate more than
                                                one services, seperate the values using semicolon (;). If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                                with the agent. |