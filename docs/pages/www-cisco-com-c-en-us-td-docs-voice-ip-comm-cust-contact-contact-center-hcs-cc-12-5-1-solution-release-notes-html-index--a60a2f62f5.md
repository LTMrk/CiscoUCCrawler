---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-solution-release-notes-html-index--a60a2f62f5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Solution_Release_Notes/html/index/Cisco-Enterprise-Chat-and-Email-for-HCS-for-Contact-Center-for-Release-12-5-1.html
retrieved_at: 2026-08-21T23:56:37.022601+00:00
---

Release Notes for Cisco Hosted Collaboration Solution for Contact Center Solution, Release 12.5(1)

# Release Notes for Cisco Hosted Collaboration Solution for Contact Center Solution, Release 12.5(1)

Updated: January 23, 2024

Chapter: Cisco Enterprise Chat and Email

## Chapter: Cisco Enterprise Chat and Email

## New Features

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge v79 and later) for Agent Desktops. For more information, see Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Ability to Block Chat Customers

Agents can now block chat customers that appear to be spam bots, or visitors who are trolling the company or the agent. The administrator can enable this feature and configure option to block chat visitors based on Browser Cookie or Visitor IP Address. When the feature is enabled by administrators, agents get the option to block customers per chat. The customer is then blocked from creating chats from that browser instance/IP Address for the number of days set by the administrator. Supervisors have access to the list of customers who are blocked and can unblock them if needed.

For details about configuring this feature, see the at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

### Finesse Shortcuts

Finesse Shortcuts for availability controls are now available for Agents.

For details about all these features, see the Enterprise Chat and Email Agent’s Guide, For Unified Contact Center Enterprise and Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-user-guide-list.html

### Messaging Hub

Messaging is increasingly becoming the most popular way customers are choosing to engage with businesses. With so many messaging platforms and channels, it is important for a business to be able to provide an experience to customers and a consistent experience for their agents. eGain Messaging Hub provides a consistent messaging experience for their customers and agents across all messaging channels (synchronous and asynchronous).

eGain Messaging Hub add-on enables ECE to connect to the messaging platform Facebook Messenger and Twitter Direct Messaging seamlessly. It can also interface with eGain Virtual Assistant for automatic handling of the queries before escalating to an agent assistance.

### Calltrack

eGain Calltrack is a case management solution that helps companies provide quick, high-quality, and cost-efficient resolution of customer issues.

eGain Calltrack add-on for ECE makes agents more efficient and productive as it provides them complete customer context across all channels including email, chat and voice, which helps them resolve the cases promptly and correctly. Additionally, agents can categorize and add notes to the Calltrack activity.

### APIs

These new APIs were introduced/enhanced in ECE 12.5:

Login and Logout APIs

Interaction APIs

Messaging APIs

- Login and Logout APIs

- Interaction APIs

- Messaging APIs

#### Login and Logout APIs

New APIs are provided to achieve the following functionality:

SAML assertion with bearer token can be used to log a user into the application using Single Sign-On.

Existing APIs have been enhanced to provide the following functionality:

Authenticate client application enhancements.

The client application session will now expire after a fixed duration, even if it is not inactive.

A maximum of 10 concurrent sessions can be created for each client application.

Supports a query parameter to force a login even if there are 10 concurrent sessions by terminating the earliest session.

Customer Single Sign-On supports external ID.

For more information about the APIs, see the Enterprise Chat and Email's Interaction API Developer Guide at https://developer.cisco.com/docs/enterprise-chat-and-email/#!interaction-api-developer-guide

#### Interaction APIs

New APIs are provided to achieve the following functionality:

Users can get the information about the product version and installed licenses using the Get application details API.

For more information about the APIs, see the Enterprise Chat and Email's Interaction API Developer Guide at https://developer.cisco.com/docs/enterprise-chat-and-email/#!interaction-api-developer-guide

#### Messaging APIs

New APIs are provided to achieve the following functionality:

Client applications can invoke an API to activate the webhook callback URL.

Existing APIs have been enhanced to provide the following functionality:

A new conversation can be initiated for the following social contact types: Facebook, Twitter.

Get conversation API response will now have message type as text/plain or text/html instead of text.

The message type text is not supported anymore as part of Send Message API. Instead, the clients can now use text/plain or text/html. This API also supports error type of message.

The message type text is not supported anymore as part of posting messages on the Webhook Callback URLs. Instead, the application will either use text/plain or text/html.

For more information about the APIs, see the Enterprise Chat and Email's Interaction API Developer Guide at https://developer.cisco.com/docs/enterprise-chat-and-email/#!interaction-api-developer-guide

## Updated Features

### Headers, Footers, Greetings, Signatures, and Auto-Acknowledgements Limitation

The Headers, Footers, Greetings, Signatures, and Auto-Acknowledgements templates text should not exceed beyond 600 characters. Post ECE 12.5, the product will enforce these limits and will not allow users to add more than 600 characters to these templates.

### Popover Configuration Improvements

Administrators can now add call variables information in the Finesse popovers displayed to agents from the Administration Console.

For details about configuring this feature, see the at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

Administrators can now configure the counter value and counter type for popover notifications.

For details about configuring this feature, see the at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

### Agent Efficiency Improvements

Agents can now click the Attachments icon to access and download attachments from all the places in the Agent Console where the activity information is available. In addition to administrators, supervisors can now pick activities from the default exception queue.

For details see the Enterprise Chat and Email Agent’s Guide for Unified Contact Center Enterprise and Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-user-guide-list.html

### Chat Monitors

While monitoring chats, supervisors can now view the name of the agent in the Inbox tile view. The agent information provides the supervisor context on the agent handling the chat and helps them in deciding to monitor chats for specific agents.

For details about using this feature, see the Enterprise Chat and Email Supervisor’s Guide for Unified Contact Center Enterprise and Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-user-guide-list.html

## Deprecated Features

In this release, Internet Explorer version 11 is deprecated. Edge Chromium (Microsoft Edge v79 and later) is the replacement.

- Kiwi Chat Template

### Kiwi Chat Template

The Kiwi template for chat is deprecated with ECE 12.5.

## Third-party Software Impacts

None.