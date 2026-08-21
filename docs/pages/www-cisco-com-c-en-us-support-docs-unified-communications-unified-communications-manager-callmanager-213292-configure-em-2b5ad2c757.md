---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213292-configure-em-2b5ad2c757
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213292-configure-email-notification-for-specifi.html
retrieved_at: 2026-08-21T13:57:14.540330+00:00
---

Configure Email Notification for Specific Node in the CUCM Cluster

# Configure Email Notification for Specific Node in the CUCM Cluster

### Download Options

Updated: April 16, 2024

Document ID: 213292

Contents

## Contents

## Introduction

This document describes the procedure to configure the email notification for a specific node in the cluster.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Simple Mail Transfer Protocol ( SMTP) Server IP/Host Name

- SMTP Server Reachability

- Cisco Unified Communications Manager (CUCM) Cluster IPs

### Components Used

The information in this document is based on these software and hardware versions:

- Microsoft Exchange SMTP server

- Call Manager version:14.0.1.12900-161

"The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Lab Cluster Information

```
CUCM 14SU2 cluster: 10.1.66.15 << Publisher 10.1.66.16 << Subscriber Windows Server 2016 (STMP server): 10.1.66.11
```

## Configure

Email notification for only Publisher node (10.1.66.15) in the cluster is required.

Step 1. Login into CUCM Publisher node and navigate to Cisco Unified OS Administration:

Step 2. Navigate to Settings > SMTP:

Step 3. Add the SMTP server IP/Hostname and click on Save .

Note : Once you save configuration, make sure status shows as "The SMTP server is available"

Step 4. Navigate to Cisco Unified CM Administration Page.

Step.5 Navigate to System > Service Parameters > Select publisher node and "Cisco AMC service" at service.

Check that the Primary Collector is a Publisher node IP/hostname.

Step 6. Configure "Certificate Monitoring" On CUCM publisher. On OS administration, go to Security > Certificate monitoring:

Step 7. Configure Notification time at your convenience, check "Enable E-mail Notification" and add email IDs (You can add more than one email address separated by semicolon).

Step 8. Click Save . After this, you receive email notifications at the time configured for certificate status. This is an example of an email notification:

Configure the custom alert/notification in RTMT:

Refer to this link for alert configuration:

https://supportforums.cisco.com/t5/collaboration-voice-and-video/how-to-configure-the-alerts-and-email-notification-in-rtmt/ta-p/3139725

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

In case the alert not working for the specific node, collect these logs:

- RIS Data Collector Logs

- AMC Service (change the log level to debug)

- AMC Service Alert Log

- Event Viewer Application and Syslog

- Packet capture from publisher

## Related Information

- Cisco Technical Support & Downloads

### Revision History

2.0

16-Apr-2024

The version was updated to CUCM 14 and new screenshots added as well as a new section.

1.0

27-Apr-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 16-Apr-2024 | The version was updated to CUCM 14 and new screenshots added as well as a new section. |
| 1.0 | 27-Apr-2018 | Initial Release |