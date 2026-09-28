---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-guide--01245eb0ab
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/guide/rcct_b_contact-center-ai-gadgets/rcct_m_contact-center-ai-gadgets_new.html
retrieved_at: 2026-08-21T04:30:35.944825+00:00
---

Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise

# Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise

Book Contents

- Book Title Page

- Preface

- Contact Center AI Gadgets

Find Matches in This Book

## Results

Updated: April 27, 2023

Chapter: Contact Center AI Gadgets

## Chapter: Contact Center AI Gadgets

# Contact Center AI Gadgets

## Contact Center AI Gadgets

The Contact Center AI Gadgets appear on the Agent Desktop and help the agents to assist the customers in real time during
                           calls. For example, the Agent Answers gadget displays suggestions and recommendations based on the conversation with the customer. This improves the capabilities
                           of the agent to respond to the customer in real time, thereby improving the customer satisfaction. Administrators and supervisors
                           can enable the Contact Center AI Services for the agents.

### Agent Answers

The Agent Answers gadget displays suggestions or recommendations (also called as Answers) in real time during the conversation between an agent
                              and a customer. These answers are the excerpts from articles and/or matching Question and Answers (Q&As) from Frequently Asked
                              Questions (FAQs) documented in the knowledge base. Displaying answers on the gadget augments the efficiency and capabilities
                              of an agent to respond to the customer more effectively.

Behavior of Agent Answers feature in the following call scenario:

Consultation : When an agent is consulting with another agent, no new answers will appear for the first agent.

For example, when Agent 1 is consulting Agent 2, customer will be put on hold. No new answers will be shown for Agent 1 and
                                    no answers will be populated for Agent 2.

Transfer and conference call scenarios are not supported.

#### Gadget User Interface

The fields on the user interface are described in the following table:

Title

Articles have a title with hyperlink, a name closely related to the context next to the title, and a descriptive text related
                                             to the conversation.

You can click the link to view the article in a new browser tab.

FAQs have a title (question), a name closely related to the context, and an answer related to the conversation.

High Match

Suggestions with high confidence score are tagged as High Match.

Thumbs-up or Thumbs-down icon

Select thumbs-up or thumbs-down icon to provide feedback about the displayed suggestions.

Article excerpts and matching Question and Answers (Q&As) are presented as suggestions, based on the utterances made by the
                                 caller during a conversation.

A separator line differentiates the set of answers or FAQs based on the context.

#### Notifications and Errors

The following notifications and errors appear on the Agent Answers gadget. You must pay attention to these notifications to get regular information on the status of answers and gadget, and
                                 take necessary action.

Banner notifications are displayed in different scenarios. For example, in case of network issues, when new answers are not
                                       populated, gadget reconnects to the server, and so on.

Tab notification appears as a red dot when the tab is not active. This indicates that there are new suggestions. The dot disappears
                                       when the tab is active.

Errors are displayed in different scenarios. For example, when gadget loading fails or when answers are not populated for
                                       a given conversation, and so on.

Toaster notification appears at the bottom-right corner of your screen when there are new suggestions. The notification does
                                       not appear on the browser tab of the desktop.

Suggestions are displayed only during the call and they are cleared when the call ends.

If you do not see any suggestions, check if the Contact Center AI service is enabled. For information on how to enable the Contact Center AI Service , see the Contact Center AI Services section in the Administration Guide for Cisco Unified Contact Center Enterprise .

When a Contact Center AI service is disabled for an agent in Unified CCE Administration, the change takes effect in the Finesse
                                                   Desktop when the agent logs off and logs in to the desktop.

### Transcript

The Transcript gadget displays the voice conversation that was dynamically converted to text and presents the text to an agent for real-time
                              viewing and reference. Displaying the text in real time on the gadget increases the efficiency and capabilities of an agent
                              to respond to the customer more effectively.

Behavior of Call Transcription feature in the following call scenarios:

Virtual Agent : If a customer had interacted with a virtual agent at the beginning of the call and then the call gets routed to an agent,
                                    the gadget displays the transcript of the voice conversation between the customer and the virtual agent along with the live
                                    transcript. In addition, the gadget displays the Highlights panel where you can view the following information:

Intents and intent parameters appear only if offered by the CCAI cloud provider. The intents and intent parameters are based
                                          on the customers' queries. For example, a customer's query is to book a flight ticket. The intent for this query is Flight
                                          Booking and the parameters for this intent are Source, Destination, and Date of departure depending on the customer’s interaction
                                          with the virtual agent.

A confidence score of high, medium, or low for each intent.

A customer sentiment indicator – happy, neutral, or sad, for each intent.

You can also view the overall sentiment indicator of the customer for the entire call.

Consultation : When an agent is consulting with another agent for assistance to resolve customer queries, the customer is put on hold.
                                    Transcripts between the first agent and the customer appear on the gadget for both agents. Transcripts between the agents
                                    during the consult does not appear on the gadget.

The Transcript gadget appears as shown in the following screenshot (example).

The timestamp that appears on the gadget is in the local time zone of the agent desktop.

On the gadget interface, you can do the following:

Filter the transcripts based on Customer, Virtual Agent, and Agent.

Search the transcripts using keywords.

#### Notifications and Errors

The following notifications and errors appear on the Transcript gadget. Pay attention to these notifications to get regular information on the status of the transcript and take necessary
                                 action.

Tab notification appears as a red dot when the tab is not active. The red dot indicates that there are new suggestions. The
                                       dot disappears when the tab is active.

The Transcript gadget displays errors in different scenarios. For example, when gadget loading fails or when transcripts are not populated
                                       for a given conversation, and so on.

Transcripts are displayed only during the call and they are cleared when the call ends.

If you don't see the transcripts, check if the Contact Center AI Service is enabled. For information on how to enable the Contact Center AI Service , see the Contact Center AI Services section in the Administration Guide for Cisco Unified Contact Center Enterprise .

When a Contact Center AI Service is disabled for an agent in Unified CC Enterprise Administration, the change takes effect in the Cisco Finesse Desktop when
                                                   the agent logs off and logs in to the desktop.

| Fields | Description |
|---|---|
| Title | Articles have a title with hyperlink, a name closely related to the context next to the title, and a descriptive text related
                                             to the conversation. You can click the link to view the article in a new browser tab. FAQs have a title (question), a name closely related to the context, and an answer related to the conversation. |
| Keyword | Keywords or matched phrases are extracted from the conversations and displayed above the title. |
| High Match | Suggestions with high confidence score are tagged as High Match. |
| Thumbs-up or Thumbs-down icon | Select thumbs-up or thumbs-down icon to provide feedback about the displayed suggestions. |

| Note | Suggestions are displayed only during the call and they are cleared when the call ends. If you do not see any suggestions, check if the Contact Center AI service is enabled. For information on how to enable the Contact Center AI Service , see the Contact Center AI Services section in the Administration Guide for Cisco Unified Contact Center Enterprise . When a Contact Center AI service is disabled for an agent in Unified CCE Administration, the change takes effect in the Finesse
                                                   Desktop when the agent logs off and logs in to the desktop. |
|---|---|

| Note | The Search box is disabled when the call is not active. |
|---|---|

| Note | Transcripts are displayed only during the call and they are cleared when the call ends. If you don't see the transcripts, check if the Contact Center AI Service is enabled. For information on how to enable the Contact Center AI Service , see the Contact Center AI Services section in the Administration Guide for Cisco Unified Contact Center Enterprise . When a Contact Center AI Service is disabled for an agent in Unified CC Enterprise Administration, the change takes effect in the Cisco Finesse Desktop when
                                                   the agent logs off and logs in to the desktop. |
|---|---|