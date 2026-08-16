---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-design-guide-html-index-cisco-w-ac0f0af537
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/design/guide/html/index/Cisco-Webex-Experience-Management-for-Unified-CCX-for-Release-12-5-1.html
retrieved_at: 2026-08-16T21:05:55.093365+00:00
---

Solution Design Guide for Cisco Unified Contact Center Express, Release 12.5(1)

# Solution Design Guide for Cisco Unified Contact Center Express, Release 12.5(1)

Updated: January 28, 2024

Chapter: Cisco Webex Experience Management

## Chapter: Cisco Webex Experience Management

- Overview

- Post-Call Voice Survey Call Flow

- SMS or Email Post-Call Survey Call Flow

## Overview

Cisco Webex Experience Management is a Customer Experience Management (CEM) platform, enabling you to see your business from your customers' perspective and their experience with the brand. Experience Management powers customer journey mapping, text analytics, and predictive modeling using the feedback collected from customers via different channels such as email, SMS and IVR.

Surveys are used to collect feedback from customers to determine the performance of the contact center and the services that are offered. With Experience Management , you can configure post-call surveys that can be initiated over IVR when agents end the calls from Finesse desktop or can be sent to the customer via Email or SMS after the call ends.

In case of survey over IVR, after an agent ends the call, Unified CCX transfers the call to Experience Management and the survey is played to the customer. Customer uses the keypad to answer the survey.

For survey via email or SMS, Unified CCX can be configured to send out an email or SMS containing a message along with a link to launch the survey and provide feedback.

The data that is collected through various surveys can be analyzed and presented to agents and supervisors as gadgets on the Finesse desktop.

A script (in conjunction with application) enables or disables Experience Management post-call survey on a per-call basis by testing for conditions and setting a session variable that controls triggering of the survey.

## Post-Call Voice Survey Call Flow

After integrating Experience Management with Unified CCX, the Post-Call Survey Call Flow is as follows:

Customer calls the Contact Center route point (Unified CCX application) on which, Experience Management post-call survey is enabled.

The call information flows through Voice Gateway, CUCM, and reaches Unified CCX.

Unified CCX identifies an agent and call is transferred to the agent.

If Experience Management gadgets are configured in Finesse desktop and prior survey data is collected, the earlier feedback from the calling customer is displayed in the Customer Experience Journey gadget.

When an agent ends the call from Finesse desktop, Unified CCX sends a secure REST API (https) request to Experience Management to construct a unique SIP URI for the call.

Unified CCX informs CUCM to transfer the call to the SIP URI that is constructed.

CUCM transfers the call to SIP URI through Voice Gateway and the survey is played to the customer.

## SMS or Email Post-Call Survey Call Flow

After integrating Experience Management with Unified CCX, the SMS/Email Post-Call Survey call flow is as follows:

Customer calls the Contact Center route point (Unified CCX application) on which, Experience Management post-call survey is enabled.

The call information flows through Voice Gateway, CUCM, and reaches Unified CCX.

Unified CCX identifies an agent and transfers the call to the agent.

Unified CCX adds call details into an in-memory cache.

Periodically Unified CCX dispatches all the records accumulated in a dispatch to the partner hosted module of the Experience Management Invitations solution. The Experience Management Invitations solution consists of the partner hosted module along with Experience Management module. For more information about Experience Management Invitations solution, see Experience Management Invitation Architecture

The Experience Management Invitations solution sends the SMS/Email survey to the customer based on the configurations set in Experience Management Invitations solution.

Note:

Experience Management also allows handling of Personally Identifiable Information (PII) about a customer in a sensitive manner by avoiding storing PII data on the platform. For more information about how to take advantage of PII, see Experience Management PII .

| Note | If Experience Management gadgets are configured in Finesse desktop and prior survey data is collected, the earlier feedback from the calling customer is displayed in the Customer Experience Journey gadget. |
|---|---|