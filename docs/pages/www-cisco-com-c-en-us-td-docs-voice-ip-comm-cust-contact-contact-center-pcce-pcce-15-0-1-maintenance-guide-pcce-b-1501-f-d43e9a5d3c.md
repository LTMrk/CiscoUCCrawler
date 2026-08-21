---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-maintenance-guide-pcce-b-1501-f-d43e9a5d3c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/maintenance/guide/pcce_b_1501_features-guide/rcct_m_1501_virtual-agent-voice-call-transcription.html
retrieved_at: 2026-08-21T12:11:18.239284+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

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

Ensure that the Unified CCE ADS, Unified CCE OAMP, VVB, Cloud Connect, and Agent Desktop components have access to Webex services
                                          to use the Call Transcription.

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

For this feature to work, you must deploy VAV via Cloud-based connector.

### Before you begin

The following components must be on release 12.6(1) or higher:

Cisco Unified CCE components (Router, Logger, AW, and PG)

Cisco Finesse

Cisco Unified CVP

Cloud Connect

For further assistance, you can contact the Cisco TAC team. For more details, see https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html .

Step 1

Configure VAV over Cloud-based connector.

See Overview .

Step 2

Add the Transcript gadget and the VAV Transcription service to the Cisco Finesse desktop layout:

Enable the Transcript gadget in Cisco Finesse Administration.

For details, see the Manage Desktop Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Enable the VAV Transcript service in Unified CCE Administration for an agent or multiple agents together.

For details, see:

Enable or Disable Contact Center AI Features for an Agent

Enable or Disable Contact Center AI Features for Multiple Agents

Enable or Disable Contact Center AI Features for Agents using Bulk Job

Once enabled, the Transcript gadget appears on the Home tab. For details on how to use the gadget, see the Cisco Contact Center AI Gadgets guide at https://ccaigadgets.produs1.ciscoccservice.com/doc/en_us/index.html .

Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

| Note | The Search box is disabled when the call is not active. If redaction or advance security settings are not enabled, PII and PCI information is also reflected in the gadget. |
|---|---|

| Note | Ensure that the Unified CCE ADS, Unified CCE OAMP, VVB, Cloud Connect, and Agent Desktop components have access to Webex services
                                          to use the Call Transcription. |
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

| Note | For this feature to work, you must deploy VAV via Cloud-based connector. |
|---|---|

| Step 1 | Configure VAV over Cloud-based connector. See Overview . |
|---|---|
| Step 2 | Add the Transcript gadget and the VAV Transcription service to the Cisco Finesse desktop layout: Enable the Transcript gadget in Cisco Finesse Administration. For details, see the Manage Desktop Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . Enable the VAV Transcript service in Unified CCE Administration for an agent or multiple agents together. For details, see: Enable or Disable Contact Center AI Features for an Agent Enable or Disable Contact Center AI Features for Multiple Agents Enable or Disable Contact Center AI Features for Agents using Bulk Job Once enabled, the Transcript gadget appears on the Home tab. For details on how to use the gadget, see the Cisco Contact Center AI Gadgets guide at https://ccaigadgets.produs1.ciscoccservice.com/doc/en_us/index.html . Note Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . | Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |

| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multitab gadget in
                                                      Cisco Finesse. For more details, see Call Transcript Gadget in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
|---|---|