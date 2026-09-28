---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-853fb8681c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-for-es/rcct-m-new-and-updated-features-15-01-es.html
retrieved_at: 2026-08-16T19:36:24.790043+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202508

# Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202508

Find Matches in This Book

## Results

Updated: August 29, 2025

Chapter: Features

## Chapter: Features

# Features

## Features Summary

GA refers to the stage in the product lifecycle when the software version and its documentation are officially released and
                                 publicly available to all customers.

Beta refers to the stage in the product lifecycle where select customers are invited to evaluate and provide feedback on features
                                 that have not yet reached GA.

Beta features are not enabled by default and are "out of the box". To join Beta testing or enable these features, email the
                                 Product Management team at cce-pm-team@cisco.com .

For CCE ES202508, the following components have made features available:

Solution/Component

Updated Features

Beta Features

Unified CCE/Packaged CCE

Disabling Personal Callback Reattempt

Graceful Shutdown for Router

Webex AI Agent for Voice and Digital Channels

## New Features

### Agent Typing Notification for ECE Chat Templates

Customers don’t have to wait and guess anymore as they can now see real time indicator when agent is typing a response to
                              their query. This feature is available across the templates and custom implementation using APIs.

### CTI Server State sync with ECE Agent state

ECE Agent state will be updated real time in case of any disconnects or logout event from the CTI server. This will help enhance
                              the agent experience while working on chat and email.

### Ability to search Department while importing MRDs and Users

Administrators can now search the Department, while importing UCCE MRDs and Users into ECE.

### Support for Entra ID

CCMP Portal now allows logins using Entra ID, in addition to Windows Authentication and ADFS.

## Updated Features

### Graceful Shutdown for Router

You can now initiate maintenance mode on Router or Rogger via orchestration.

For more information about maintenance mode in orchestration, see the Initiate maintenance mode for a specific node(s) section in CCE Orchestration chapter of the following guides:

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

### Disabling Personal Callback Reattempt

This outbound enhacement improves agent productivity and customer experience by preventing agents from being assigned to unanswered
                                 Personal Callback (PCB) calls and by restricting redialing. Rescheduling is disabled for unreachable personal callback records
                                 with call results 2, 4, 6, 8, 9, or 16. The list of unanswered calls for manual rescheduling can also be retrieved.

CCE now allows you to use the PersonalCallbackReattempt registry item on both the Campaign Manager and Dialer to control redial attempts for unanswered.

You can prevent retry of unanswered PCB calls by disabling the PersonalCallbackReattempt registry item on both the Dialer and Campaign Manager. This configuration stops the Dialer from redialing unanswered PCB
                                 calls and ensures that the Campaign Manager does not reschedule them, instead marking the records with a closed status (C).

For more information about enabling or disabling the PersonalCallbackReattempt registry, see the Registry Settings chapter in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

## Beta Features

### Webex AI Agent

The Webex AI Agent, an AI-powered virtual assistant, is now available for voice and digital channels. With the Webex AI Agent,
                              you can create AI-driven voice agents to automate customer service and support interactions before involving a human agent.
                              These agents facilitate voice interactions with intonation, language comprehension, and contextual awareness throughout conversations.

Customers will benefit from an experience similar to having a personal assistant, receiving help with inquiries, information
                              retrieval, and reduced wait times.

| Solution/Component | GA Features | Updated Features | Beta Features |
|---|---|---|---|
| Unified CCE/Packaged CCE |  | Disabling Personal Callback Reattempt Graceful Shutdown for Router | Webex AI Agent for Voice and Digital Channels |