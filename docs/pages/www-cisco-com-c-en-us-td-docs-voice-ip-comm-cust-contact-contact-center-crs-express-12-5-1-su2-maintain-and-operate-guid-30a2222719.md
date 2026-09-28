---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-maintain-and-operate-guid-30a2222719
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/maintain_and_operate/guide/uccx_b_1251su2_admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_appendix_011110.html
retrieved_at: 2026-08-16T21:37:51.182221+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

Updated: April 11, 2022

Chapter: Bubble Chat Experience

## Chapter: Bubble Chat Experience

- Bubble Chat Experience

- Bubble Chat Experience

# Bubble Chat Experience

## Bubble Chat Experience

Bubble chat can be launched on any device and the display adapts to the screen size of the device used. For example, if you
                              launch the bubble chat using a desktop, a small chat pop-over appears on the right-side bottom of the web page. If you use
                              a mobile device, the bubble chat launches in the full-screen mode.

To use Bubble chat, ensure that:

The browser cookies and third-party cookies are enabled.

The Tracking Protection option in the browser is disabled.

The Customer Collaboration Platform server and customer website are in the same domain so that the bubble chat works on various browsers.

For more information about cookies and Tracking Protection option, see your browser-specific documentation.

If you use a private certificate, your end customers must accept an untrusted certificate in their browser to initiate a chat.
                                                If you do not want your end customers to accept untrusted certificate, you must use CA-signed certificate.

The chat process is as follows:

The customer initiates the chat by clicking a text link, button, or icon.

The chat form attempts to collect the details of the customer, such as, name, email, phone number etc. The form also presents
                                    a list of problem statements - from which the customer has to mandatorily select one.

The customer provides details in the chat form and submits it.

The chat pop-over opens with a welcome message, such as 'Thanks for contacting. We will be with you shortly'. If all the agents
                                    are busy, an appropriate message appears.

When the agent joins the chat, the customer is notified by a message, and the pop-over divides into a conversation area (where
                                    messages appear) and a typing area (where the customer can type messages for the agent).

The customer and agent chat - more than one agent can join the chat to create a group chat. While chatting, the agent's messages
                                    are displayed on the left of the conversation area and the customer's messages are displayed on the right. All messages are
                                    displayed with the timestamp below the message (in the 24-hour format); the agent's message will additionally have the agent's
                                    name before the timestamp.

The chat pop-over can be minimized or maximized.

The following indicators appear on the chat pop-over at appropriate times:

Agent typing indicator: This indicator, represented by three squiggly dots, appears above the typing area whenever the agent
                                          types.

New messages indicator: The pop-over blinks in a minimized stated whenever a new event occurs during the chat, such as the
                                          receipt of a new message, joining of another agent, connection problems etc.

Agent left/joined indicator: The customer is informed when an agent leaves or joins the chat.

When the customer completes the chat and attempts to exit the chat, the following pop-ups are displayed in a sequence:

A chat closure confirmation box.

A chat transcript download box. The customer can choose to download the chat transcript.

A chat rating box, if rating is enabled for the chat. The customer can choose to rate or skip rating by closing this box.

Any connectivity or technical problems that are encountered during the chat session are notified as banner messages at the
                                          top of the conversation area.

| Note | For more information about cookies and Tracking Protection option, see your browser-specific documentation. If you use a private certificate, your end customers must accept an untrusted certificate in their browser to initiate a chat.
                                                If you do not want your end customers to accept untrusted certificate, you must use CA-signed certificate. |
|---|---|

| Note | Any connectivity or technical problems that are encountered during the chat session are notified as banner messages at the
                                          top of the conversation area. |
|---|---|