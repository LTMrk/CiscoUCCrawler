---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-serviceability-administration-guide-1-0-1-sartmtal-html-229a059fad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/serviceability/administration/guide/1_0_1/sartmtal.html
retrieved_at: 2026-08-21T16:07:40.000583+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Alert Configuration in RTMT

## Chapter: Alert Configuration in RTMT

## Alert Configuration in RTMT

RTMT comprises two kinds of alerts: preconfigured and user defined. You can configure both kinds of alerts, but you cannot delete preconfigured alerts. You can disable both preconfigured and user-defined alerts in RTMT.

For information on preconfigured alerts, alert customization, and alert action fields in which you can configure alerts, refer to "Alerts" in the Cisco Unified CallManager Serviceability System Guide .

When an activated service goes from up to down, RTMT generates an alert. You use Alert Central to view the status and history of the alerts that RTMT generates.

This chapter provides information on the following topics:

• Working with Alerts

• Setting Alert Properties

• Suspending Alerts on Cisco Unified Presence Server Nodes or the Cluster

• Configuring E-mails for Alert Notification

• Configuring Alert Actions

## Working with Alerts

By using the following procedure, you can perform tasks, such as access Alert Central, sort alert information, enable, disable, or remove an alert, clear an alert, or view alert details.

Step 1 Perform one of the following tasks:

• In the Quick Launch Channel, click the Tools tab and then the Alert tab; click the Alert Central icon.

• Choose Tools > Alert > Alert Central .

The Alert Central monitoring window displays and shows the alert status and alert history of the alerts that RTMT generated for the Cisco Unified Presence Server cluster.

Step 2 Perform one of the following tasks:

• To set alert properties, see the "Setting Alert Properties" section .

• To suspend alerts on Cisco Unified Presence Server nodes, see the "Suspending Alerts on Cisco Unified Presence Server Nodes or the Cluster" section .

• To configure e-mails for alert notification, see the "Configuring E-mails for Alert Notification" section .

• To configure alert actions, see the "Configuring Alert Actions" section .

• To sort alert information in the Alert Status pane, click the up/down arrow that displays in the column heading. For example, click the up/down arrow that displays in the Enabled or InSafeRange column.

You can sort alert history information by clicking the up/down arrow in the columns in the Alert History pane. To see alert history that is out of view in the pane, use the scroll bar on the right side of the Alert History pane.

• To enable, disable, or remove an alert, perform one of the following tasks:

– From the Alert Status window, right-click the alert and choose Disable/Enable Alert (option toggles) or Remove Alert , depending on what you want to accomplish.

– Highlight the alert in the Alert Status window and choose Tools > Alert > Disable/Enable (or Remove ) Alert .

Tip You can only remove user-defined alerts from RTMT. The Remove Alert option appears grayed out when you choose a preconfigured alert.

• To clear either individual or collective alerts after they get resolved, perform one of the following tasks:

– After the Alert Status window displays, right-click the alert and choose Clear Alert (or Clear All Alerts ).

– Highlight the alert in the Alert Status window and choose Tools > Alert > Clear Alert (or Clear All Alerts) .

After you clear an alert, it changes from red to black.

• To view alert details, perform one of the following tasks:

– After the Alert Status window displays, right-click the alert and choose Alert Details .

– Highlight the alert in the Alert Status window and choose Tools > Alert > Alert Details .

Tip After you have finished viewing the alert details, click OK .

Additional Information

See the Related Topics .

## Setting Alert Properties

The following procedure describes how to set alert properties.

Step 1 Display Alert Central, as described in the "Working with Alerts" section .

Step 2 From the Alert Status window, click the alert for which you want to set alert properties.

Step 3 Perform one of the following tasks:

• Right-click the alert and choose Set Alert/Properties .

• Choose Tools > Alert > Set Alert/Properties .

Note For Cisco Unified Presence Server clusterwide alerts, the Enable/Disable this alert on following server(s): box does not show up in the alert properties window. Clusterwide alerts include number of registered phones, gateways, media devices, route list exhausted, media list exhausted, MGCP D-channel out of service, malicious call trace, and excessive quality reports.

Step 4 To enable the alert, check the Enable Alert check box.

Step 5 From the Severity drop-down list box, choose the severity of the alert.

Step 6 From the Enable/Disable this alert on following server(s) pane, check the Enable check box of the servers on which you want this alert to be enabled.

For preconfigured alerts, the Description information pane displays a description of the alert.

Step 7 Click Next .

Step 8 In the Threshold pane, enter the conditions in which the system triggers the alert.

Step 9 In the Duration pane, click one of the following radio buttons:

• Trigger alert only when below or over.... radio button—If you want the alert to be triggered only when the value is constantly below or over the threshold for a specific number of seconds; then, enter the seconds.

• Trigger alert immediately—If you want the system to trigger an alert immediately.

Step 10 Click Next .

Step 11 In the Frequency pane, click one of the following radio buttons:

• trigger alert on every poll — If you want the alert to be triggered on every poll.

• trigger up to <numbers> of alerts within <number> of minutes—If you want a specific number of alerts to be triggered within a specific number of minutes. Enter the number of alerts and number of minutes.

Step 12 In the Schedule pane, click one of the following radio buttons:

• 24-hours daily—If you want the alert to be triggered 24 hours a day.

• Start time/Stop time—If you want the alert to be triggered within a specific start and stop time. Enter the start and stop times.

Step 13 Click Next .

Step 14 If you want to enable e-mail for this alert, check the Enable Email check box.

Step 15 To trigger an alert action with this alert, choose the alert action that you want to send from the drop-down list box.

Step 16 To configure a new alert action, or edit an existing one, click Configure .

Step 17 To add a new alert action, perform the following procedure:

a. Click Add .

b. In the Name field, enter a name for the alert action.

c. In the Description field, enter a description of the alert action.

d. To add an e-mail recipient, click Add .

e. In the Enter email/epage address field, enter an e-mail or e-page address of the recipient that you want to receive the alert action.

f. Click OK .

The Action Configuration window shows the recipient(s) that you added, and the Enable check box appears checked.

Tip To delete an e-mail recipient, highlight the recipient and click Delete . The recipient that you chose disappears from the recipient list.

g. When you finish adding all the recipients, click OK .

Step 18 To edit an existing alert action, perform the following procedure:

a. Highlight the alert action and click Edit .

The Action Configuration window of the alert action that you chose displays.

b. Update the configuration and click OK .

Step 19 After you finish alert action configuration, click Close .

Step 20 For alerts that do not allow trace download, click Activate in the Alert Properties: Email Notification window.

For alerts, such as CriticalServiceDown and CodeYellow, that allow trace download, perform the following procedure:

a. Click Next.

b. In the Alert Properties: TCT Download window, check the Enable TCT Download check box.

c. The SFTP Parameters Dialog window displays. Enter the IP address, a user name, password, port and download directory path where the trace will be saved. To ensure that you have connectivity with the SFTP server, click Test Connection . If the connection test fails, your settings will not be saved.

d. To save your configuration, click OK.

e. In the TCT Download Parameters window, enter the number and frequency of downloads. Setting the number and frequency of download will help you to limit the number of trace files that will be downloaded. The setting for polling provides the basis for the default setting for the frequency.

Note To delete an alert action, highlight the action, click Delete , and click Close .

Additional Information

See the Related Topics .

## Suspending Alerts on Cisco Unified Presence Server Nodes or the Cluster

You may want to temporarily suspend some or all alerts, either on a particular Cisco Unified Presence Server node or the entire cluster. For example, if you are upgrading the Cisco Unified Presence Server to a newer release, you would probably want to suspend all alerts until the upgrade completes, so you do not receive e-mails and/or e-pages during the upgrade. The following procedure describes how to suspend alerts in Alert Central.

Step 1 Choose Tools > Alert > Suspend cluster/node Alerts .

Note Per server suspend states do not apply to Cisco Unified Presence Server clusterwide alerts.

Step 2 To suspend all alerts in the cluster, choose the Cluster Wide radio button and check the suspend all alerts check box.

Step 3 To suspend alerts per server, choose the Per Server radio button and check the Suspend check box of each server on which you want alerts to be suspended.

Step 4 Click OK .

Note To resume alerts, choose Alert > Suspend cluster/node Alerts again and uncheck the suspend check boxes.

Additional Information

See the Related Topics .

## Configuring E-mails for Alert Notification

Perform the following procedure to configure e-mail information for alert notification.

Step 1 Choose Tools > Alert > Config Email Server .

The Mail Server Configuration window displays.

Step 2 In the Mail Server field, enter the e-mail recipient information.

Step 3 In the Port field, enter the port number of the mail server.

Step 4 Click OK .

Additional Information

See the Related Topics .

## Configuring Alert Actions

The following procedure describes how to configure new alert actions.

Step 1 Display Alert Central, as described in the "Working with Alerts" section .

Step 2 Choose Alert > Config Alert Action .

Step 3 Perform Step 17 through Step 20 in the "Setting Alert Properties" section to add, edit, or delete alert actions.

Additional Information

See the Related Topics .

## Related Topics

• Working with Alerts

• Setting Alert Properties

• Suspending Alerts on Cisco Unified Presence Server Nodes or the Cluster

• Configuring E-mails for Alert Notification

• Configuring Alert Actions