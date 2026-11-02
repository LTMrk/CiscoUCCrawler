---
doc_id: help-webex-com-en-us-article-mykour-96a7848e83
source_url: https://help.webex.com/en-us/article/mykour
retrieved_at: 2026-11-02T13:06:24.637071+00:00
---

Notifications in Control Hub is a central place to manage alerts for your Webex deployment.
        Administrators can configure alerts to be delivered through email, webhooks, PagerDuty, or
        in a Webex App space. Regardless of the delivery channel configured, all alerts will always
        appear in Control Hub.

Each administrator has their own set of alerts and rules that
        they can create and view in My alerts and My
          rules tabs, and they can view all alerts and rules from other administrators
        in the organization in the All alerts and All
          rules tabs.

Alerts for the last 14 days will appear in the Alerts section. You can export historical alerts for the last 30
        days in a CSV format by clicking on the export button.

Alerts that occur on the same
        day and have the same severity, type, and target are grouped together in a collapsible
        drop-down menu to make them easier to view and navigate. You can hover over the expand
        button to see how the alerts were combined.

There are two categories of alerts: Threshold-based and Service-generated.

## Threshold-based alerts

Administrators can create a rule to monitor for specific events by specifying specific
        thresholds, such as participants who reach more than 300ms of latency or a packet loss of
        more than 8%. These alerts are only triggered if the administrators configure them by
        creating a rule.

Administrators can further configure how these alerts are delivered by choosing the
        delivery channel for them:

- Email —You can add up to 30 email addresses as recipients to
          receive the alerts.

If an existing space gets renamed, the alert will still be delivered to the same
              space.

- Webhook —The alerts will be delivered to the webhook URL
          configured in Control Hub.

- PagerDuty —You can input a service key to deliver the alerts to a
          related service using PagerDuty.

## Service-generated alerts

These alerts are created automatically by Webex services. Most of these alerts are critical
        in nature that the administrator should pay attention to. Administrators can manage how
        these alerts are delivered by choosing the delivery channel for them similar to
        threshold-based alerts. The delivery channels include email, Webex App, webhook, and
        PagerDuty.

## View alerts and rules

Sign in to Control Hub and go to Notifications.

Select one of the following:

- In the All alerts tab, when you select a filter for a single service, an additional drop-down box appears so you can further refine your search.

- In the All rules tab, when you select a filter for a single service, an additional drop-down box appears so you can further refine your search.

- In the All rules tab, when you select a filter for Device Name or Email, a search bar appears so you can search for all rules related to a specific user or device.

## Find alerts by target

Use the Target column to see which device, workspace, user, trunk,
        or other target an alert affects. Search by target name to find related alerts.

A target appears only when target information is available for the alert.

Sign in to Control
            Hub and go to Notifications > Alerts .

Select All alerts or My alerts .

Check the Target column for the affected target.

Enter a target name in the search field to find matching alerts.

## Understand an alert type

Read an explanation of an alert type in its side panel to learn what the alert means.

Descriptions aren't available for every alert type.

Sign in to Control
            Hub and go to Notifications > Alerts .

Select All alerts or My alerts , then open
          an alert.

If an information icon appears beside Type , use it to read the
          explanation.

For Webex Meetings, you can create rules to get alerts for:

- Live meeting monitoring —Use this alert to find out when
            participants are experiencing media quality issues during meetings that are in progress.
            You can create up to 10 of these alerts.

- Device live meeting monitoring —Use this alert to find out when
            devices are experiencing media quality issues during meetings that are in progress. You
            can create up to 25 of these alerts.

- Historical meeting quality trend —Use this alert to find out
            when a percentage of participants in specific Webex sites and locations reach the media
            quality thresholds that are set automatically based on the past performance of meetings
            within the last seven days. You can create up to 10 of these alerts.

- Historical meeting quality monitoring —Similar to the history
            meeting quality trend alert, you can use this alert to set your own thresholds on when
            to receive an alert when a percentage of participants in specific Webex sites and
            locations reach any of the media quality thresholds. You can create up to 10 of these
            alerts.

Meeting alerts only trigger for participants who attend meetings through Webex Meetings
            and Webex App. The minimum app versions that participants must use for alerts to trigger
            are:

Webex Meetings desktop app version 39.6.5 or higher

Webex Meetings mobile app for Android and iOS version 39.11 or higher

Webex App desktop version 3.0.12427.0 or higher

Webex App mobile Android version 4.1.6 or higher

Webex App mobile iOS version 4.3 or higher

Alerts don't trigger for audio-only meetings, Webex Events, and Webex Training
            sessions.

Add a live meeting monitoring alert

You can enable up to 10 live meeting monitoring alerts per organization. Each alert can monitor up to either 30 user email addresses or 30 devices.

If the Monitor all participants check box is checked, then the alert only triggers for meetings with fewer than 50 participants.

Sign in to Control Hub and go to Notifications > My rules .

Click Create rule .

Select Live meeting monitoring next to Type , and enter the name for the alert next to Title .

Toggle the Status switch to on to receive notifications for the alert.

Select User email(s) or Device name(s) and enter up to 30 user email addresses or devices.

Check the Monitor all participants check box to receive alerts for all of the participants that are in the same meetings as the users or devices in the list.

In the Rules section, set the following thresholds:

- Latency —Enter between 400ms to 2000ms.

- Jitter —Enter between 400ms to 2000ms.

- Packet Loss —Enter between 5% to 100%.

- CPU —Enter between 90% to 100%.

Set the Accumulated and Consecutive duration for the alert to trigger.

In the Delivery channel section, check the Email check box and enter the email addresses of who will receive the alerts.

Check the Webex space check box and enter the name of the space if you want to receive messages in that space whenever a threshold is reached.

Click Save .

Add a device live meeting monitoring alert

You can enable up to 25 device live meeting monitoring alerts per organization.

Sign in to Control Hub and go to Notifications > My rules .

Click Create rule .

Select Device live meeting monitoring next to Type , and enter the name for the alert next to Title .

Toggle the Enabled switch to on to receive notifications for the
          alert.

Choose to monitor:

- All devices —Monitor all active devices in your
            organization.

- Device name(s) —Monitor up to 30 devices.

- Select device(s) by tag(s) —Monitor up to 30 device tags.
            The alert monitors any devices set with those tags.

In the Rules section, set the following audio and video
          thresholds:

- Packet Loss —Enter between 5% to 50%.

- Latency —Enter between 400ms to 2000ms.

- Jitter —Enter between 400ms to 2000ms.

Set the Accumulated and Consecutive duration for the alert to trigger.

In the Delivery channel section, you can:

- Check the Email check box and enter the email addresses of
            who receives the alerts.

- Check the Webex space check box and enter the name of the
            space if you want to receive messages in that space whenever a threshold is
            reached.

Click Save .

Add a historical meeting quality trend alert

You can add up to 10 historical meeting quality trend alerts per organization.

The maximum report size for the file when you download alerts is
        100MB.

Sign in to Control Hub and go to Notifications > My rules .

Click Create rule .

Select Historical meeting quality trend next to Type , and enter the name for the alert next to Title .

Toggle the Status switch to on to receive notifications for the alert.

Select which Webex site and participant locations to receive alerts for.

In the Delivery channel section, check the Email check box and enter the email addresses of who will receive the alerts.

Check the Webex space check box and enter the name of the space if you want to receive messages in that space whenever a threshold is reached.

Click Save .

Add a historical meeting quality monitoring alert

You can enable up to 10 historical meeting quality monitoring alerts per organization.

The maximum report size for the file when you download alerts is
        100MB.

Sign in to Control Hub and go to Notifications > My rules .

Click Create rule .

Select Historical meeting quality monitoring next to Type , and enter the name for the alert next to Title .

Toggle the Status switch to on to receive notifications for the alert.

Select which Webex site and participant locations to receive alerts for.

In the Rules section, set the following thresholds:

- Latency —Enter between 400ms to 2000ms.

- Jitter —Enter between 400ms to 2000ms.

- Packet Loss —Enter between 5% to 100%.

- CPU —Enter between 90% to 100%.

In the Trigger section, select a duration to monitor and enter the percentage of participants that must reach one of the thresholds to trigger the alert.

In the Delivery channel section, check the Email check box and enter the email addresses of who will receive the alerts.

Check the Webex space check box and enter the name of the space if you want to receive messages in that space whenever a threshold is reached.

Click Save .

Calling alerts

For Webex Calling, you can configure the following alerts:

### Add a call quality drop alert

Use this alert to find out when the call quality at specific locations or a user's media session drops to poor quality.

Call quality is calculated as:

- Good —Both video and audio stream had jitter below 150ms, latency below 400ms, and
          packet loss below 5%.

- Poor —Both video and audio stream had jitter above 150ms, latency above 400ms, and
          packet loss above 5%.

Alerts are sent out when a call ends. When you receive the alert, you can click Troubleshoot Call to take you straight to the call in Troubleshooting if the
        alert is monitoring specific users. If the alert is monitoring locations, you can click View Analytics to take you to the Media Quality tab in Calling
        Analytics.

You can create up to 10 Call Quality Drop alerts per organization.

Alerts are not triggered on Dedicated Instance (DI) based trunks.

Sign in to Control Hub .

Go to Notifications > My rules .

Click Create rule .

From the Service drop-down list, select Calling .

From the Type drop-down list, select Call Quality
            Drop .

From the Severity drop-down list.

This field shows how severe or important an alert is. You can choose severity level as
          High, Medium, or Low.

Enter a Title .

Toggle on Enabled to receive notifications for the alert.

In Target section, select User email(s) or Location name(s) .

You can enter up to 30 user email addresses or locations to monitor.

In the Delivery channel section, choose how to receive the alerts:

- Email —Enter the email addresses of who'll receive the alerts.

Your organization must have Messaging enabled for Webex App to use a space as a
                delivery channel.

- Webhook —Check this check box if you want to use the alert with third-party applications .

Click Save .

### Add a trunk status change alert

An alert is sent out when the status of the monitored trunk changes. The available trunk
        statuses are online, offline, and impaired. You can configure which status change should
        trigger an alert.

The following are the different trunk status:

Online —Successful registration of Local Gateway to Webex
            Calling.

Offline —Unsuccessful registration of Local Gateway to Webex
            Calling.

Impaired —Unsuccessful connection between at least one Webex
            Calling Edge proxy and Local Gateway.

Unknown —In the process of establishing a connection between
            Webex Calling and the Local Gateway that is recently added.

To know more about various status error changes, refer to help center article Local Gateway Troubleshooting section.

Sign in to Control Hub .

Go to Notifications > My rules .

Click Create rule .

From the Service drop-down list, select Calling .

From the Type drop-down list, select Trunk
            status .

From the Severity drop-down list.

This field shows how severe or important an alert is. You can choose severity level as
          High, Medium, or Low.

Enter a Title .

Toggle on Enabled to receive notifications for the alert

In Target section, select Trunk
          name(s) .

Alerts are not triggered on Dedicated Instance (DI) based trunks.

In the Rule definition section, you can define the rule for when
          alert needs to be triggered. You can select all or choose from the following status
          changes:

- Online to Offline

- Online to Impaired

- Impaired to Offline

- Impaired to Online

- Offline to Impaired

- Offline to Online

In the Delivery channel section, choose how to receive the
          alerts:

- Email —Enter the email addresses of who'll receive the
            alerts.

Your organization must have Messaging enabled for Webex App to use a space as a
                delivery channel.

```
"data": {
"summary": "LGW Trunk Status Changed from online to offline",
"severity": "HIGH",
"emailIds": null,
"notificationAttributes": null,
"overrideExistingSubscriptionRecipients": false,
"actionUrl": "https://admin.webex.com//calling/call-routing/trunks",
"type": "Calling",
"orgId": "zzzzzzzz-yyyy-zzzz-xxxx-yyyyyyyyyyyy",
"audit": false,
"callbackUrl": null,
"notificationId": "7ada8db8-8c2b-40b8-953d-5dca3f125443",
"subType": "Trunk status",
"ruleId": "8e2a0ae7-8bd0-4e40-87e5-78f06b93e11e",
"category": "CUSTOM"
}
}
```

- PagerDuty —Check this checkbox and enter a PagerDuty service
            key in the text box.

Click Save .

### Add a trunk concurrent call limit alert

An alert is sent out when threshold limit of concurrent calls on trunk is reached. This
        alert helps to identify the busy hour or day when trunk capacity is reached to handle
        concurrent calls.

Consecutive alerts are triggered at the selected time interval, if the configured threshold
        continues to breach.

Sign in to Control Hub .

Go to Notifications > My rules .

Click Create rule .

From the Service drop-down list, select Calling .

From the Type drop-down list, select Trunk concurrent
            call limit .

From the Severity drop-down list.

This field shows how severe or important an alert is. You can choose severity level as
          High, Medium, or Low.

Enter a Title .

Toggle on Enabled to receive notifications for the alert.

In the Target section, select Trunk
            name(s) .

Alerts are not triggered on Dedicated Instance (DI) based trunks.

In the Rule definitions section, you can define the rule for
          when alert needs to be triggered. Enter the following values for Concurrent
            call limit threshold condition:

In the Value field, enter the maximum percentage of
              concurrent calls, considered as threshold for sending alert.

For example, if you want to send an alert when 70% of the calls are concurrent
              calls, then enter 70 in this field.

In Sample every field, select a time range from 5, 15, 30,
              45 minutes or 1 hour.

Webex Calling checks the percentage of concurrent calls at this selected time interval.

In the Delivery channel section, choose how to receive the
          alerts:

- Email —Enter the email addresses of who'll receive the
            alerts.

Your organization must have Messaging enabled for Webex App to use a space as a
                delivery channel.

- Webhook —Check this check box if you want to show up the alert
            with third-party applications. See Enable Webhooks section in this article for more
            details.

- PagerDuty —Check this check box and enter a PagerDuty
            service key in the text box.

Click Save .

### Trunk certificate expiry alert

An alert is sent out when the certificate of a certificate-based trunk is about to expire or
      has expired. This is a system-generated alert, enabled by default for organizations with
      certificate-based trunks.

Before the certificate expires, automatic alerts are sent out on predefined days, such as on
        60 th day, 30 th day, 15 th day, and 7 th day before
      expiry. After the certificate expires, an alert is sent out immediately and only once. No
      consecutive alerts are sent.

Alerts are not triggered on Dedicated Instance (DI) based trunks.

### Route List calls blocked alert

When the number of concurrent calls exceeds the Route List Calls license limit, up to 20%
        additional capacity (bursting) is allowed. When the off-net (PSTN) call volume exceeds 20%
        bursting limits, they are blocked. An alert is sent to the user about Route List calls are
        blocked.

Before you begin

Sign in to Control Hub .

Go to Notifications > All rules .

List of all rules is displayed.

Select Route List Calls Blocked alert.

Route List Calls Blocked alert is a system-generated alert. Therefore you can only
              edit few of its details as mentioned in next steps.

In the Delivery channel section, choose how to receive the
          alerts:

- Email —Enter the email addresses of who'll receive the
            alerts.

Your organization must have Messaging enabled for Webex App to use a space as a
                delivery channel.

```
{
        "summary": "A PSTN call that was started on 2025-10-17T14:43:15.500Z (UTC) was blocked because the number of simultaneous calls exceeded the licensed limit for all Route List numbers. Please review your organization's Route List Calls licenses and consider making adjustments to prevent future disruptions.",
        "severity": "HIGH",
        "emailIds": null,
        "notificationAttributes": null,
        "overrideExistingSubscriptionRecipients": false,
        "actionUrl": null,
        "type": "Calling",
        "orgId": "e18ef5dd-08f1-4351-841b-8c0e8c449385",
        "audit": false,
        "callbackUrl": null,
        "notificationId": "48196554-d747-49ea-a30e-36b6dd4b0b2f",
        "subType": "Route List Calls Blocked",
        "ruleId": "25df20fd-9e59-40d5-bede-2875bbecca19",
        "category": "GENERATED"
}
```

- PagerDuty —Check this checkbox and enter a PagerDuty service
            key in the text box.

Click Save .

Dedicated Instance alerts

There are two categories of service alerts for Dedicated Instance: Maintenance alerts and Proactive alerts.

### Maintenance alerts

The system enables maintenance alerts by default. Partner or customer administrators should
        verify or configure the delivery channel to receive notifications via email and/or Webex
        space. Maintenance alerts are used to send notifications about maintenance, outages, and
        incident communication.

To add delivery channel information to receive maintenance alerts:

- Sign in to Control Hub and go to Notifications > All rules .

- Click Calling-Maintenance and Outage Alerts and scroll down to Delivery Channel .

You can add upto 30 email IDs.

To receive notifications in a Webex space, you must have a Messaging license. If bot
              access is enabled in Apps/Bots and you're allowed to be a member of the organization
              room, you’ll get the notifications. Otherwise, contact your organization administrator
              to resolve the issue.

You can select Webhooks if you have Webhooks enabled at the organizational level. For more information, see Enable webhooks for alerts in Control Hub .

- Enter the Email and Webex space information and click Save to save the changes.

Whenever maintenance occurs, Control Hub automatically displays
          a banner with the cluster details, region, and the scheduled date and time.

### Proactive alerts

Partner or customer administrators can subscribe to day two or day three proactive alerts
        and event notifications, and choose to have them delivered via email, Webex App spaces, or
        both by selecting the Delivery Channel when creating the alert.

For example : Unified CM Video Conf Bridge Out of Resource Count High, Unified CM MTP
        Out of Resource Count High.

### To create a proactive alert rule

Only partner or customer admin with full admin rights can create rules.

- Sign in to Control Hub and go to Notifications > My rules .

- Select Create rule .

- Select Calling from the Service drop-down list.

- Select Alerts for Dedicated Instance from the Type drop-down list.

We recommend creating rules for proactive alerts with medium or low
                      severity.

You receive alerts that match or exceed the severity level you selected when
                      setting up the rule.

- Add Title for the new rule.

- All the check boxes in the Rules section are selected by default. Uncheck the ones based on your preferences.

You can select Webhooks if you have Webhooks enabled at the organizational level. For more information, see Enable webhooks for alerts in Control Hub .

Once the rules are created, it takes a maximum of 6 hours to start receiving the notifications.

### Alert status and their legends

Control Hub consolidates the statuses of multiple UC application services, agent statuses,
        and the maintenance status of each node.

Services status for each node is refreshed every 30 seconds.

Critical alerts

Cisco CallManager

Cisco Tftp

Cisco CTIManager

Cisco Tomcat

Cisco CDR Agent

Cisco CDR Repository Manager

Cisco Extension Mobility

Cisco Extension Mobility Application

Cisco Smart License Manager

Connection Smart License Manager Server

Connection SMTP Server

License synchronization

Non-critical alerts

All other UC services which is not listed above are considered as non-critical
                  services.

Alert legends

### Certificate expiry alert

Control Hub sends certificate expiry alerts to customers 67 days before the expiration date
        and then every 12 days, until the certificate is renewed.

- Customer owned and managed certificates - A proactive alert is sent from Control
          Hub, and you’re responsible for renewing and managing the certificate.

- Cisco owned and managed certificates - A proactive alert is sent from Control
          Hub, and we’re responsible for renewing and managing the certificate.

Set up a proactive alert to receive a notification when a certificate expires.

### Control Hub application status alarm definitions

For a list of available alarm definitions for Dedicated Instance, see Control Hub
          application status alarm definitions .

For devices, you can create rules to get alerts for:

- Offline and online events —An event is registered after a device has been offline for 5 minutes or has come back online 5 minutes ago. You can create up to 100 of these alerts.

- Issues that are detected or resolved events —You can select if
            you want to receive all alerts or mute the ones that you don't wish to receive. You can
            create up to 100 of these alerts.

- Software version expiry —An alert is sent out 14 days and 3 days
            before the software version expires for the device. You can create up to 10 of these
            alerts

See RoomOS device alerts in Control Hub article for more details on available alerts and how to set them up for Board, Desk, and Room Series devices in your organization.

## Alerts of PhoneOS Phones on Control Hub

As the administrator, you can check the status of phones that are registered to Webex Calling. If any issue occurs on the phone, you can see the details in the Issues & Information section under the Devices for diagnostics and troubleshooting.

Also, you can view all alerts that are reported by the phone in Notifications . For more information about Notifications, see Notifications in Control Hub .

### Call protocol

The message can also display on the phone screen.

### Network

### Action button

### Security

### Configuration

Use Agent Central notifications in Control Hub to review Agentic Apps server and capability changes that may affect access for your organization. Agent Central notifications appear when an enabled public or private Agentic Apps server changes in a way that requires administrator awareness or review.

You must be a Control Hub administrator with access to Notifications to view Agent Central alerts for Agentic Apps and manage the delivery rule for generated alerts.

In Control Hub, Agentic Apps alerts and generated rules appear with the Agent Central name. Search for Agent Central when you filter alerts or rules.

All Agent Central alerts for Agentic Apps appear in Control Hub. High severity blocked alerts can also be delivered by email or to a Webex App space when you configure delivery for the generated rule. Low severity warning alerts appear in Notifications only.

Repeated detection of the same unresolved change doesn't generate duplicate alerts. If the issue is cleared and the server changes again later, Control Hub creates a new alert for the new change.

## View Agent Central alerts for Agentic Apps

You must be a Control Hub administrator with access to Notifications .

Sign in to Control Hub .

Go to Notifications > Alerts .

Select All alerts to view alerts for your organization, or My alerts to view alerts delivered to you.

Use search or filters to find Agent Central alerts.

Select the alert row to view alert details, or select Review server to open the affected Agentic Apps server.

## Agent Central alert types

Agent Central alerts for Agentic Apps tell you whether access can continue with a warning or is blocked until an administrator reviews the change.

If the same refresh detects both warning and blocked capability changes, Control Hub shows one high severity blocked alert with both states listed in the alert details. For example, a blocked alert can include two tools with status Blocked and one prompt with status Warning .

Registered servers don't generate Agent Central alerts until they're approved and enabled for your organization. New tools, prompts, resources, or skills that haven't been enabled for your organization don't trigger Agent Central alerts.

## Review and resolve Agent Central alerts

Use Review server from an alert to inspect the affected Agentic Apps server or capability.

Sign in to Control Hub.

Go to Notifications > Alerts .

Search for Agent Central .

Open the alert that you want to review.

Select Review server .

Review the affected server metadata, tool, prompt, resource, or skill.

Choose one of these actions:

- Re-approve the server metadata after confirming the change.

- Re-approve the affected tool, prompt, resource, or skill after confirming the change.

- Follow the server page remediation guidance if the metadata blocked alert is caused by a badge issue.

- Disable the server or affected capability if you don't want to allow the changed item.

Control Hub clears the active alert after the issue is corrected, disabled, or re-approved. Manually marking an Alert Center row as resolved doesn't approve metadata, restore a badge, or unblock an affected capability. If the underlying issue is still present, Control Hub may create a new alert when it detects the unresolved change again.

## View Agent Central alert rules

Agent Central alert rules for Agentic Apps are automatically generated by Webex and appear under the General service. These generated rules are read-only for rule name, severity, service, and trigger conditions. For high severity blocked rules, you can configure delivery channels and recipients.

Sign in to Control Hub.

Go to Notifications > Alerts .

Select All rules .

Search for Agent Central .

## Configure delivery for high severity Agent Central alerts

High severity blocked alerts can be delivered by email or to a Webex App space. Control Hub always receives the alert, even if you don't add an email or Webex App recipient.

Sign in to Control Hub.

Go to Notifications > Alerts .

Select All rules .

Search for Agent Central .

Open one of the high severity blocked rules: Agent Central metadata communication blocked or Agent Central capability communication blocked .

In Delivery channel , select Email and add the email recipients.

To deliver alerts in a Webex App space, select Webex space and choose the space delivery option.

Save the rule.

## Notes and limitations for Agent Central notifications

Keep these notes and limitations in mind when you use Agent Central notifications for Agentic Apps.

- Agentic Apps alerts appear with the Agent Central name in Control Hub.

- Low severity warning alerts are Alert Center only.

- High severity blocked alerts can be delivered by email or Webex App space if delivery is configured on the generated rule.

- Registered but not enabled servers don't generate Agent Central alerts.

- New upstream capabilities that haven't been enabled for your organization don't trigger Agent Central alerts.

- Repeated detection of the same unresolved change doesn't create duplicate alerts.

- Public server alerts are scoped to each affected enabled organization.

- Private server alerts are scoped to the owning organization after the server is approved and enabled.

- When a server-level metadata issue blocks access, Control Hub may show the metadata blocked alert instead of separate capability alerts until the server-level issue is resolved.

You can set up a webhook callback URL so that alerts show up in third-party applications.
        The admin can specify a webhook callback URL in Control Hub. After providing a callback URL,
        you can select the webhook option as an additional delivery channel in the rules for new or
        existing alerts. See below for steps on how to configure webhooks.

Here's an example of what the JSON element for an alert webhook looks like:

```
{
"orgId": "1ab23cde-4567-890f-1234-gh56ijk07l891",
"title": "title",
"summary" : "notification for a test alert",
"actionUrl" : "www.actionURL.com",
"severity" : "HIGH",
"eventType" : "created",
"resourceType": "ControlHubAlerts",
"type": "Meeting",
"subtype": "Live Meeting Monitoring",
}
```

## Set up a webhook callback URL

You must first add a webhook callback URL before you can enable rules to use webhooks.

Sign in to Control
            Hub and go to Organization Settings .

Scroll to the Webhook configuration section.

Toggle the Configure the webhook URL switch to on. A pop-up
          window appears.

Enter the webhook URL that you want to use.

You can also choose to add a secret token for the webhook. View this blog to learn more about secret tokens.

Select Validate . If validation fails, check to make sure the
          webhook URL and secret token are correct. Click Try again once
          you've finished checking.

Select Save .

## Enable webhook in a rule

After setting up a webhook URL, you can set up rules to use webhooks as a delivery channel.

Sign in to Control Hub and go to Notifications > My rules .

In the All rules tab, select a rule.

In the Delivery Method section, check the Webhook checkbox. Based on the type of alert you're creating, a
          payload example is shown so that you can know what to expect.

Click Save .

## Cisco devices webhook field reference

For information on webhook field references for Cisco devices, see this article .

You can set up a PagerDuty integration key so that alerts show up in third-party
        applications.

## Enable PagerDuty in a rule

Before you begin

You must first get an integration key in PagerDuty before you can enable the
        PagerDuty setting for alerts in Control Hub. To get an integration key, create a new service
        in PagerDuty and select Events API V2 as the integration. Once you create an Events API V2
        service, you can find the integration key in the Integrations tab of the PagerDuty
        dashboard.

Sign in to Control Hub and go to Notifications > My rules .

In the Delivery channel section, check the PagerDuty checkbox.

Enter the integration key that you created in the PagerDuty dashboard.

Click Save .

| 1 | Sign in to Control Hub and go to Notifications. |
|---|---|
| 2 | Select one of the following: To view alerts, select My alerts or All alerts . In the All alerts tab, when you select a filter for a single service, an additional drop-down box appears so you can further refine your search. To view rules, select My rules or All rules . In the All rules tab, when you select a filter for a single service, an additional drop-down box appears so you can further refine your search. In the All rules tab, when you select a filter for Device Name or Email, a search bar appears so you can search for all rules related to a specific user or device. |

| 1 | Sign in to Control
            Hub and go to Notifications > Alerts . |
|---|---|
| 2 | Select All alerts or My alerts . |
| 3 | Check the Target column for the affected target. |
| 4 | Enter a target name in the search field to find matching alerts. |

| 1 | Sign in to Control
            Hub and go to Notifications > Alerts . |
|---|---|
| 2 | Select All alerts or My alerts , then open
          an alert. |
| 3 | If an information icon appears beside Type , use it to read the
          explanation. |

| 1 | Sign in to Control Hub and go to Notifications > My rules . |
|---|---|
| 2 | Click Create rule . |
| 3 | Select Live meeting monitoring next to Type , and enter the name for the alert next to Title . |
| 4 | Toggle the Status switch to on to receive notifications for the alert. |
| 5 | Select User email(s) or Device name(s) and enter up to 30 user email addresses or devices. |
| 6 | Check the Monitor all participants check box to receive alerts for all of the participants that are in the same meetings as the users or devices in the list. |
| 7 | In the Rules section, set the following thresholds: Latency —Enter between 400ms to 2000ms. Jitter —Enter between 400ms to 2000ms. Packet Loss —Enter between 5% to 100%. CPU —Enter between 90% to 100%. |
| 8 | Set the Accumulated and Consecutive duration for the alert to trigger. |
| 9 | In the Delivery channel section, check the Email check box and enter the email addresses of who will receive the alerts. |
| 10 | Check the Webex space check box and enter the name of the space if you want to receive messages in that space whenever a threshold is reached. |
| 11 | Click Save . |

| 1 | Sign in to Control Hub and go to Notifications > My rules . |
|---|---|
| 2 | Click Create rule . |
| 3 | Select Device live meeting monitoring next to Type , and enter the name for the alert next to Title . |
| 4 | Toggle the Enabled switch to on to receive notifications for the
          alert. |
| 5 | Choose to monitor: All devices —Monitor all active devices in your
            organization. Device name(s) —Monitor up to 30 devices. Select device(s) by tag(s) —Monitor up to 30 device tags.
            The alert monitors any devices set with those tags. |
| 6 | In the Rules section, set the following audio and video
          thresholds: Packet Loss —Enter between 5% to 50%. Latency —Enter between 400ms to 2000ms. Jitter —Enter between 400ms to 2000ms. |
| 7 | Set the Accumulated and Consecutive duration for the alert to trigger. |
| 8 | In the Delivery channel section, you can: Check the Email check box and enter the email addresses of
            who receives the alerts. Check the Webex space check box and enter the name of the
            space if you want to receive messages in that space whenever a threshold is
            reached. |
| 9 | Click Save . |

| 1 | Sign in to Control Hub and go to Notifications > My rules . |
|---|---|
| 2 | Click Create rule . |
| 3 | Select Historical meeting quality trend next to Type , and enter the name for the alert next to Title . |
| 4 | Toggle the Status switch to on to receive notifications for the alert. |
| 5 | Select which Webex site and participant locations to receive alerts for. |
| 6 | In the Delivery channel section, check the Email check box and enter the email addresses of who will receive the alerts. |
| 7 | Check the Webex space check box and enter the name of the space if you want to receive messages in that space whenever a threshold is reached. |
| 8 | Click Save . |

| 1 | Sign in to Control Hub and go to Notifications > My rules . |
|---|---|
| 2 | Click Create rule . |
| 3 | Select Historical meeting quality monitoring next to Type , and enter the name for the alert next to Title . |
| 4 | Toggle the Status switch to on to receive notifications for the alert. |
| 5 | Select which Webex site and participant locations to receive alerts for. |
| 6 | In the Rules section, set the following thresholds: Latency —Enter between 400ms to 2000ms. Jitter —Enter between 400ms to 2000ms. Packet Loss —Enter between 5% to 100%. CPU —Enter between 90% to 100%. |
| 7 | In the Trigger section, select a duration to monitor and enter the percentage of participants that must reach one of the thresholds to trigger the alert. |
| 8 | In the Delivery channel section, check the Email check box and enter the email addresses of who will receive the alerts. |
| 9 | Check the Webex space check box and enter the name of the space if you want to receive messages in that space whenever a threshold is reached. |
| 10 | Click Save . |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Notifications > My rules . |
| 3 | Click Create rule . |
| 4 | From the Service drop-down list, select Calling . |
| 5 | From the Type drop-down list, select Call Quality
            Drop . |
| 6 | From the Severity drop-down list. This field shows how severe or important an alert is. You can choose severity level as
          High, Medium, or Low. |
| 7 | Enter a Title . |
| 8 | Toggle on Enabled to receive notifications for the alert. |
| 9 | In Target section, select User email(s) or Location name(s) . You can enter up to 30 user email addresses or locations to monitor. |
| 10 | In the Delivery channel section, choose how to receive the alerts: Email —Enter the email addresses of who'll receive the alerts. Webex space —Enter the name of the space to receive the alert as
            messages in a space. The bot only messages recipients that are added in the email
            delivery channel. Your organization must have Messaging enabled for Webex App to use a space as a
                delivery channel. Webhook —Check this check box if you want to use the alert with third-party applications . |
| 11 | Click Save . |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Notifications > My rules . |
| 3 | Click Create rule . |
| 4 | From the Service drop-down list, select Calling . |
| 5 | From the Type drop-down list, select Trunk
            status . |
| 6 | From the Severity drop-down list. This field shows how severe or important an alert is. You can choose severity level as
          High, Medium, or Low. |
| 7 | Enter a Title . |
| 8 | Toggle on Enabled to receive notifications for the alert |
| 9 | In Target section, select Trunk
          name(s) . You can enter up to 30 trunks to monitor. Alerts are not triggered on Dedicated Instance (DI) based trunks. |
| 10 | In the Rule definition section, you can define the rule for when
          alert needs to be triggered. You can select all or choose from the following status
          changes: Online to Offline Online to Impaired Impaired to Offline Impaired to Online Offline to Impaired Offline to Online |
| 11 | In the Delivery channel section, choose how to receive the
          alerts: Email —Enter the email addresses of who'll receive the
            alerts. Webex space —Enter the name of the space to receive the alert as
            messages in a space. The bot only messages recipients that are added in the email
            delivery channel. Your organization must have Messaging enabled for Webex App to use a space as a
                delivery channel. Webhook —Check this checkbox if you want to show up the alert in
            third-party applications. You can edit the webhook callback URL in organization setting.
            For example, set a webhook callback URL for trunk status alert as
            follow: "data": {
"summary": "LGW Trunk Status Changed from online to offline",
"severity": "HIGH",
"emailIds": null,
"notificationAttributes": null,
"overrideExistingSubscriptionRecipients": false,
"actionUrl": "https://admin.webex.com//calling/call-routing/trunks",
"type": "Calling",
"orgId": "zzzzzzzz-yyyy-zzzz-xxxx-yyyyyyyyyyyy",
"audit": false,
"callbackUrl": null,
"notificationId": "7ada8db8-8c2b-40b8-953d-5dca3f125443",
"subType": "Trunk status",
"ruleId": "8e2a0ae7-8bd0-4e40-87e5-78f06b93e11e",
"category": "CUSTOM"
}
} See Enable Webhooks section in this article for more
            details. PagerDuty —Check this checkbox and enter a PagerDuty service
            key in the text box. |
| 12 | Click Save . |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Notifications > My rules . |
| 3 | Click Create rule . |
| 4 | From the Service drop-down list, select Calling . |
| 5 | From the Type drop-down list, select Trunk concurrent
            call limit . |
| 6 | From the Severity drop-down list. This field shows how severe or important an alert is. You can choose severity level as
          High, Medium, or Low. |
| 7 | Enter a Title . |
| 8 | Toggle on Enabled to receive notifications for the alert. |
| 9 | In the Target section, select Trunk
            name(s) . You can enter up to 30 trunks to monitor. Alerts are not triggered on Dedicated Instance (DI) based trunks. |
| 10 | In the Rule definitions section, you can define the rule for
          when alert needs to be triggered. Enter the following values for Concurrent
            call limit threshold condition: In the Value field, enter the maximum percentage of
              concurrent calls, considered as threshold for sending alert. For example, if you want to send an alert when 70% of the calls are concurrent
              calls, then enter 70 in this field. In Sample every field, select a time range from 5, 15, 30,
              45 minutes or 1 hour. Webex Calling checks the percentage of concurrent calls at this selected time interval. |
| 11 | In the Delivery channel section, choose how to receive the
          alerts: Email —Enter the email addresses of who'll receive the
            alerts. Webex space —Enter the name of the space to receive the alert as
            messages in a space. The bot only messages recipients that are added in the email
            delivery channel. Your organization must have Messaging enabled for Webex App to use a space as a
                delivery channel. Webhook —Check this check box if you want to show up the alert
            with third-party applications. See Enable Webhooks section in this article for more
            details. PagerDuty —Check this check box and enter a PagerDuty
            service key in the text box. |
| 12 | Click Save . |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Notifications > All rules . List of all rules is displayed. |
| 3 | Select Route List Calls Blocked alert. Route List Calls Blocked alert is a system-generated alert. Therefore you can only
              edit few of its details as mentioned in next steps. |
| 4 | In the Delivery channel section, choose how to receive the
          alerts: Email —Enter the email addresses of who'll receive the
            alerts. Webex space —Enter the name of the space to receive the alert as
            messages in a space. The bot only messages recipients that are added in the email
            delivery channel. Your organization must have Messaging enabled for Webex App to use a space as a
                delivery channel. Webhook —Check this checkbox if you want to show up the alert in
            third-party applications. You can edit the webhook callback URL in organization setting.
            The following example shows the alert sent to webhook callback
            URL: {
        "summary": "A PSTN call that was started on 2025-10-17T14:43:15.500Z (UTC) was blocked because the number of simultaneous calls exceeded the licensed limit for all Route List numbers. Please review your organization's Route List Calls licenses and consider making adjustments to prevent future disruptions.",
        "severity": "HIGH",
        "emailIds": null,
        "notificationAttributes": null,
        "overrideExistingSubscriptionRecipients": false,
        "actionUrl": null,
        "type": "Calling",
        "orgId": "e18ef5dd-08f1-4351-841b-8c0e8c449385",
        "audit": false,
        "callbackUrl": null,
        "notificationId": "48196554-d747-49ea-a30e-36b6dd4b0b2f",
        "subType": "Route List Calls Blocked",
        "ruleId": "25df20fd-9e59-40d5-bede-2875bbecca19",
        "category": "GENERATED"
} See Enable Webhooks section in this article for more
            details. PagerDuty —Check this checkbox and enter a PagerDuty service
            key in the text box. |
| 5 | Click Save . |

| Critical alerts |  |  | Cisco CallManager Cisco Tftp Cisco CTIManager Cisco Tomcat Cisco CDR Agent Cisco CDR Repository Manager Cisco Extension Mobility Cisco Extension Mobility Application Cisco Smart License Manager Connection Smart License Manager Server Connection SMTP Server License synchronization |
|---|---|---|---|
| Non-critical alerts |  |  | All other UC services which is not listed above are considered as non-critical
                  services. |

| Status | Color | Description |
|---|---|---|
| Online | Green | Indicates the node is functioning normally without any issues |
| Maintenance | Orange | Indicates the node is undergoing a maintenance |
| Services Down | Red | Indicates one or more critical services are down on the node |
| Services Down | Orange | Indicates one or more non-critical services are down on the node, or the agent
                is offline |

| DisplayName | Code | Type | Message | Level |
|---|---|---|---|---|
| Limited service | wxclimitedservice | Limited service | SRST mode - this phone has limited service. The message can also display on the phone screen. | Warning |
| Sip profile registration | SIPProfileRegistration | SIP registration failed | SIP registration failed | Error |

| DisplayName | Code | Type | Message | Level |
|---|---|---|---|---|
| Packet loss detected | networkquality | Packet loss detected | During the last call we detected a level of packet loss that may have impacted the call quality. Packet loss is typically caused by network congestion. | Warning |

| DisplayName | Code | Type | Message | Level |
|---|---|---|---|---|
| Action button not configured | actionbuttonnotconfig | Action button not configured | The Action button is not configured. Configure it in All Configurations > Phone >Action Button. | Warning |
| Action button emergency service unavailable | emergencyunavailable | Action button emergency service unavailable | It's impossible to access the emergency service since no line is registered. Will fail to use the Action button or dial numbers to access the service. | Warning |

| DisplayName | Code | Type | Message | Level |
|---|---|---|---|---|
| SCEP certificate enrollment failed | scepcertenrollmentfailed | SCEP certificate enrollment failed | SCEP certificate enrollment failed | Error |

| DisplayName | Code | Type | Message | Level |
|---|---|---|---|---|
| Failed to apply configuration changes | wxcresyncfailed | Failed to apply configuration changes | The phone failed to apply configuration changes. The configurations may be out of date. | Error |
| Upgrade failed | wxcupgradefailed | Upgrade failed | The phone failed to update the firmware. Check that the device has a working network connection, that DNS is configured and it is not blocked by firewalls or proxies. | Error |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Notifications > Alerts . |
| 3 | Select All alerts to view alerts for your organization, or My alerts to view alerts delivered to you. |
| 4 | Use search or filters to find Agent Central alerts. |
| 5 | Select the alert row to view alert details, or select Review server to open the affected Agentic Apps server. |

| Alert type | Severity | What it means | What to do |
|---|---|---|---|
| Metadata communication warning | Low | The server name, description, or same-domain URL changed, and access can continue until review. | Review the server and re-approve the metadata, or disable the server if you don't trust the change. |
| Metadata communication blocked | High | A server-level change blocks access. This can include a new URL domain, a blocked metadata change, Agent Card security or interface changes, or an invalid server badge. | Review and re-approve the server, follow the server page guidance for badge issues, or disable the server. |
| Capability communication warning | Low | An enabled tool, prompt, resource, or skill changed, and your organization allows access to continue until review. | Review and re-approve the affected capability, or disable it. |
| Capability communication blocked | High | An enabled tool, prompt, resource, or skill changed and your organization doesn't allow access to continue, or an enabled item was removed or renamed. Access to the affected item is blocked. | Review and re-approve the affected capabilities, or disable the affected items. |

| 1 | Sign in to Control Hub. |
|---|---|
| 2 | Go to Notifications > Alerts . |
| 3 | Search for Agent Central . |
| 4 | Open the alert that you want to review. |
| 5 | Select Review server . |
| 6 | Review the affected server metadata, tool, prompt, resource, or skill. |
| 7 | Choose one of these actions: Re-approve the server metadata after confirming the change. Re-approve the affected tool, prompt, resource, or skill after confirming the change. Follow the server page remediation guidance if the metadata blocked alert is caused by a badge issue. Disable the server or affected capability if you don't want to allow the changed item. |

| 1 | Sign in to Control Hub. |
|---|---|
| 2 | Go to Notifications > Alerts . |
| 3 | Select All rules . |
| 4 | Search for Agent Central . |

| 1 | Sign in to Control Hub. |
|---|---|
| 2 | Go to Notifications > Alerts . |
| 3 | Select All rules . |
| 4 | Search for Agent Central . |
| 5 | Open one of the high severity blocked rules: Agent Central metadata communication blocked or Agent Central capability communication blocked . |
| 6 | In Delivery channel , select Email and add the email recipients. |
| 7 | To deliver alerts in a Webex App space, select Webex space and choose the space delivery option. |
| 8 | Save the rule. |

| 1 | Sign in to Control
            Hub and go to Organization Settings . |
|---|---|
| 2 | Scroll to the Webhook configuration section. |
| 3 | Toggle the Configure the webhook URL switch to on. A pop-up
          window appears. |
| 4 | Enter the webhook URL that you want to use. You can also choose to add a secret token for the webhook. View this blog to learn more about secret tokens. |
| 5 | Select Validate . If validation fails, check to make sure the
          webhook URL and secret token are correct. Click Try again once
          you've finished checking. |
| 6 | Select Save . |

| 1 | Sign in to Control Hub and go to Notifications > My rules . |
|---|---|
| 2 | In the All rules tab, select a rule. |
| 3 | In the Delivery Method section, check the Webhook checkbox. Based on the type of alert you're creating, a
          payload example is shown so that you can know what to expect. |
| 4 | Click Save . |

| 1 | Sign in to Control Hub and go to Notifications > My rules . |
|---|---|
| 2 | In the Delivery channel section, check the PagerDuty checkbox. |
| 3 | Enter the integration key that you created in the PagerDuty dashboard. |
| 4 | Click Save . |

## Figuras

![A screenshot of a web-based dashboard titled 'My alert' showing a list of system notifications. The interface features a search bar, filters for alert severity (High, Medium, Low), and a 'Download' button. The alert table includes columns for Severity, Alerts, Action, and Date. A pop-up tooltip for 'Grouped alerts' is visible, explaining that alerts are combined by target and type within the last 24 hours. Listed alerts include a 'VIP Group Alert' for a specific user, 'Video viewpoint events', 'Audio Packet loss', and a 'Medium' severity 'Video Packet loss' alert.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/494001-495000/494919.jpg)

![Call quality drop alert creation](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-491000/490647.jpg)

![Configuring Delivery channel while creating an alert](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-491000/490649.jpg)

![Trunk status alert](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-491000/490650.jpg)

![Trunks concurrent call limit alert creation](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-491000/490648.jpg)

![Route list call block alert](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/492001-493000/492427.png)

![Maintenance alert delivery](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/485001-486000/485912.jpg)

![Alert center CH](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483001.jpg)

![Proactive alerts](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/485001-486000/485913.jpg)

![Critical ToolTip](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/490582.jpg)

![Critical ToolTip side panel](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/490583.jpg)

![NonCritical_ToolTip](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/490580.jpg)

![NonCritical_ToolTip side panel](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/490581.jpg)

![An alert optionfor webhook call back URLs](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/463001-464000/463002.jpg)

![Enable webhook setting when making an alert in Control Hub](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/463001-464000/463004.jpg)