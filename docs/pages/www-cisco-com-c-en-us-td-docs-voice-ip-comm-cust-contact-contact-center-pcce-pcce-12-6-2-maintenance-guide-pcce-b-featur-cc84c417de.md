---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-maintenance-guide-pcce-b-featur-cc84c417de
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/maintenance/guide/pcce_b_features-guide-1262/ucce_b_features-guide-1261_chapter_01000.html
retrieved_at: 2026-08-21T12:29:26.282283+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: November 15, 2024

Chapter: Virtual Agent–Voice Call Transcription

## Chapter: Virtual Agent–Voice Call Transcription

# Virtual Agent–Voice Call Transcription

## VAV Transcript Overview

Cisco Contact Center Enterprise leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to provide
                           transcription services that assist agents. These services are available for the agents in the Cisco Finesse desktop gadgets.

If a customer has interacted with a virtual agent at the beginning of the call and then the call gets routed to an agent,
                           the Transcript gadget displays the transcript of the voice conversation between the customer and the virtual agent along with the live transcript.
                           It helps in gathering context from the earlier interaction with the virtual agent and capturing high level summary points
                           for wrapping up the call. In addition, the gadget displays the Highlights panel where you can view the following information:

Intents and intent parameters (appear only if offered by the CCAI cloud provider). The intents and intent parameters are based
                                 on the customers' queries. For example, a customer's query is to book a flight ticket. The intent for this query is Flight
                                 Booking and the parameters for this intent are Source, Destination, and Date of departure depending on the customer’s interaction
                                 with the virtual agent.

A confidence score of high, medium, or low for each intent.

A customer sentiment indicator – happy, neutral, or sad, for each intent (appears only if offered by the CCAI cloud provider).

You can also view the overall sentiment indicator of the customer for the entire call.

The Transcript gadget shows the transcript of the voice conversation along with their timestamp in the local time zone of the agent desktop.

On the gadget interface, you can do the following:

Filter the transcripts based on Customer, Virtual Agent, and Agent.

Search the transcripts using keywords.

The Search box is disabled when the call is not active.

If redaction or advance security settings are not enabled, PII and PCI information is also reflected in the gadget.

## Prerequisites

To configure VAV Call Transcription:

Ensure that the Packaged CCE AW, VVB, Cloud Connect, and Agent Desktop components have access to Webex services to use VAV
                                          Call Transcription.

Complete the prerequisites for configuring VAV via Cloud-based connector. For more details, see Prerequisites .

For this feature to work, you must deploy VAV via Cloud-based connector.

The following components must be on release 12.6(1) or higher:

Cisco Unified CCE components (Router, Logger, AW, and PG)

Cisco Finesse

Cisco Unified CVP

Cloud Connect

For further assistance, you can contact the Cisco TAC team. For more details, see https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html .

## Configuration Task Flow

Follow this procedure to enable the Cisco Contact Center AI (CCAI) Services that equip your Cisco Contact Center for VAV Call
                              Transcription service.

Step 1

Configure VAV via Cloud-based connector. See VAV via Cloud-Based Connector .

Step 2

Add the Transcript gadget and the VAV Transcription service to the Cisco Finesse desktop layout:

Enable the Transcript gadget in Cisco Finesse Administration.

For details, see the Manage Desktop Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Enable the VAV Transcript service in Unified CCE Administration for an agent or multiple agents together.

For details, see Enable or Disable Contact Center AI Features for Agents .

Once enabled, the Transcript gadget appears on the Home tab. For details on how to use the gadget, see the Cisco Contact Center AI Gadgets guide at https://ccaigadgets.produs1.ciscoccservice.com/doc/en_us/index.html .

Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

## Enable or Disable Contact Center AI Features for Agents

Contact Center AI Features can be configured for each agent. Administrators and supervisors can enable or disable the services for an agent or multiple
                           agents together.

### Configure Contact Center AI Features for an Agent

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Click New to open the New Agent page.

Step 3

Click the Contact Center AI tab.

Step 4

To enable or disable the required Contact Center AI Features , check or uncheck the check boxes corresponding to the services.

Step 5

Click Save .

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

To enable or disable the Contact Center AI Features , check or uncheck the check boxes corresponding to the services.

Step 5

Click Save , and then click Yes to confirm the changes.

### Enable or Disable Answers Contact Center AI Services for Agents using Bulk Job

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

#### Bulk Contact Center AI Features Content File

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

The type of Contact Center AI Features to be associated with the agent. Supported values are AgentAnswers , VAV Transcript, and Transcript. To associate more than one services, seperate the values using semicolon (;).

If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                             with the agent.

| Note | The Search box is disabled when the call is not active. If redaction or advance security settings are not enabled, PII and PCI information is also reflected in the gadget. |
|---|---|

| Note | Ensure that the Packaged CCE AW, VVB, Cloud Connect, and Agent Desktop components have access to Webex services to use VAV
                                          Call Transcription. |
|---|---|

| Command or Action | Purpose |
|---|---|
| Complete the prerequisites for configuring VAV via Cloud-based connector. For more details, see Prerequisites . | Note For this feature to work, you must deploy VAV via Cloud-based connector. The following components must be on release 12.6(1) or higher: Cisco Unified CCE components (Router, Logger, AW, and PG) Cisco Finesse Cisco Unified CVP Cloud Connect For further assistance, you can contact the Cisco TAC team. For more details, see https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html . | Note | For this feature to work, you must deploy VAV via Cloud-based connector. |
| Note | For this feature to work, you must deploy VAV via Cloud-based connector. |

| Note | For this feature to work, you must deploy VAV via Cloud-based connector. |
|---|---|

| Step 1 | Configure VAV via Cloud-based connector. See VAV via Cloud-Based Connector . |
|---|---|
| Step 2 | Add the Transcript gadget and the VAV Transcription service to the Cisco Finesse desktop layout: Enable the Transcript gadget in Cisco Finesse Administration. For details, see the Manage Desktop Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . Enable the VAV Transcript service in Unified CCE Administration for an agent or multiple agents together. For details, see Enable or Disable Contact Center AI Features for Agents . Once enabled, the Transcript gadget appears on the Home tab. For details on how to use the gadget, see the Cisco Contact Center AI Gadgets guide at https://ccaigadgets.produs1.ciscoccservice.com/doc/en_us/index.html . Note Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . | Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |

| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Click New to open the New Agent page. This page has: General , Attributes , Skill Groups , Supervised Teams , Enable Email & Chat , and Contact Center AI tabs.You cannot save the agent until you have entered all required fields on the General tab. You can complete other tabs as needed and in any order. For more information, see Add and Maintain Agents section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| Step 3 | Click the Contact Center AI tab. Displays a list of services for the agent. |
| Step 4 | To enable or disable the required Contact Center AI Features , check or uncheck the check boxes corresponding to the services. |
| Step 5 | Click Save . |

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Click on the agent row whose services are to be modified. |
| Step 3 | Click the Contact Center AI tab. Displays a list of services enabled or disabled for the agent. |
| Step 4 | To enable or disable the required Contact Center AI Features , check or uncheck the check boxes corresponding to the services. |
| Step 5 | Click Save . |

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Check the check box corresponding to each agent whose services you want to edit. |
| Step 3 | Click Edit > Contact Center AI . The Edit Services dialog displays a list of services that are the service that is enabled or disabled. If the service is enabled for all the agents selected for editing, the check box is checked. If the service is disabled for all the agents selected for editing, the check box is unchecked. If the service is enabled for some agents and disabled for the others, the check box has a dash (—). |
| Step 4 | To enable or disable the Contact Center AI Features , check or uncheck the check boxes corresponding to the services. |
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
| agentServices | Yes (to enable Contact Center AI Features ) | The type of Contact Center AI Features to be associated with the agent. Supported values are AgentAnswers , VAV Transcript, and Transcript. To associate more than one services, seperate the values using semicolon (;). If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                             with the agent. |