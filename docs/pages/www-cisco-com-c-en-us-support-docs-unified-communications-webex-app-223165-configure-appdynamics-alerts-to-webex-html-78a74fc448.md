---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-app-223165-configure-appdynamics-alerts-to-webex-html-78a74fc448
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-app/223165-configure-appdynamics-alerts-to-webex.html
retrieved_at: 2026-08-16T22:03:17.928632+00:00
---

Configure AppDynamics Alerts to Webex for Live Incident Response

# Configure AppDynamics Alerts to Webex for Live Incident Response

### Download Options

Updated: June 27, 2025

Document ID: 223165

Contents

## Contents

## Introduction

This document describes how to configure AppDynamics Controller to send alert notifications directly to Webex spaces.

## Prerequisites

- Administrative access to AppDynamics Controller (SaaS or on-premises)

- Webex account with permission to create Webhook

- Familiarity with AppDynamics alerting and HTTP request templates

- Basic understanding of REST APIs

### Requirements

- AppDynamics Controller version 21.x or later

- Webex App account and access to the Webex AppHub

- Network connectivity between AppDynamics Controller and Webex cloud endpoints

- Configured notification policies in AppDynamics

### Components Used

- AppDynamics Controller

- Webex App

- HTTP Request Template

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

In the fast-paced environments of today, minimizing Mean Time to Detect (MTTD) and Mean Time to Resolve (MTTR) is critical. This guide walks you through the steps to integrate the AppDynamics Controller with Webex in order to automatically push alert notifications to your team collaborative spaces — enabling real-time visibility and accelerating incident response.

## Configure

### Why Integrate AppDynamics with Webex?

- Instant Collaboration: Receive AppDynamics alerts in Webex spaces for immediate team awareness and action.

- Enhanced Incident Response: Enable IT and DevOps teams to triage and resolve issues collaboratively in real time.

- Unified Workflows: Manage incidents and discussions in a single platform, reducing context switching.

### Configurations

#### Step 1: Create a Webex Webhook

- Create Webex Space:

- Login to Webex AppHub and Navigate to Incoming Webhooks and select Connect:

- Provide Webhook Name and select Webex Space to send alerts:

- Click Add and copy webhook URL to your notepad:

#### Step 2: Set Up the HTTP Request Template in AppDynamics

- In AppDynamics Controller, navigate to Alert & Respond > HTTP Request Templates and click New:

- Give name to this HTTP Request Template and choose the POST method:

- Enter copied Webex Webhook endpoint for messages from step 1:

- Enter your payload. A sample payload is provided. Update based on your business needs:

```
{
  "markdown": "AppDynamics Alert: ${latestEvent.displayName}\nSeverity: ${latestEvent.severity}\nTime: ${latestEvent.eventTime}\nApp: ${latestEvent.application.name}\nNode: ${latestEvent.node.name}\nTier: ${latestEvent.tier.name}\nMessage: ${latestEvent.eventMessage}\nLink: ${latestEvent.deepLink}"
}
```

#### Step 3: Link the HTTP Request Template to a Policy

- Go to Alert & Respond > Policies in AppDynamics:

- Create or edit a policy that triggers on your desired health rules or custom events:

The HTTP Request Template name populates automatically, as created in Step 2:

- Save and enable the policy:

## Verify

- Trigger a test alert in AppDynamics:

- Check the designated Webex space for the alert message:

- Confirm that the alert includes all relevant details and links back to AppDynamics for further investigation.

## Troubleshoot

## Conclusion

By integrating AppDynamics with Webex, you empower your IT and DevOps teams to respond to alerts more quickly, reduce time to resolution, and increase service reliability. This low-code integration streamlines incident collaboration right where your teams already work.

## Need Further Assistance?

If you have a question or are experiencing issues, please reach out to AppDynamics Support and include details such as error messages, configuration information, or relevant logs to help expedite troubleshooting.

## Related Information

- AppDynamics Documentation

- HTTP Request Template

### Revision History

1.0

27-Jun-2025

Initial Release

### Contributed by Cisco Engineers

Sunil Agarwal

Software Consulting Engineering Technical Leader

### This Document Applies to These Products

- Webex App

| Issue | Troubleshooting Steps |
|---|---|
| No Message in Webex | - Verify the bot token and permissions - Check AppDynamics HTTP request logs for errors - Ensure the space ID and API endpoint are correct |
| Authentication Errors | - Confirm the Webhook URL is correct |
| Message Formatting Issues | - Validate your JSON payload - Confirm AppDynamics variable names are correct |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-Jun-2025 | Initial Release |