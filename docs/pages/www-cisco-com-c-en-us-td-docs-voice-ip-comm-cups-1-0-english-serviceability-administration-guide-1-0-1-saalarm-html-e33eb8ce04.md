---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-serviceability-administration-guide-1-0-1-saalarm-html-e33eb8ce04
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/serviceability/administration/guide/1_0_1/saalarm.html
retrieved_at: 2026-08-21T16:07:18.965694+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Alarm Configuration

## Chapter: Alarm Configuration

## Alarm Configuration

Cisco Unified Presence Server Serviceability Alarms assist system administrators and support personnel in troubleshooting Cisco Unified Presence Server problems by enabling administrators to configure alarms and events and by providing alarm message definitions. An administrator configures alarms and trace parameters and provides the information to a Cisco TAC engineer.

Administrators use alarms to provide runtime status and state of the system and to take corrective action for problem resolution; for example, to determine whether phones are registered and working. Alarms contain information such as explanation and recommended action. Alarm information includes application name, machine name, and cluster name to help you perform troubleshooting for problems that are not on your local Cisco Unified Presence Server.

You can configure alarms for Cisco Unified Presence Server servers that are in a cluster and services for each server. You configure the alarm interface to send alarm information to multiple destinations, and each destination can have its own alarm event level (from debug to emergency). Then, you use the real-time monitoring tool to collect and view the alarms.

When a service issues an alarm, the alarm interface sends the alarm to the chosen monitors (for example, SDI trace, Cisco RIS Data Collector). The monitor forwards the alarm or writes it to its final destination (such as a log file).

This chapter contains the following topics:

• Configuring or Updating an Alarm for a Service

• Alarm Destination Settings

• Alarm Event Level Settings

## Configuring or Updating an Alarm for a Service

This section describes how to configure an alarm for any Cisco Unified Presence Server service.

Note Cisco recommends that you do not change SNMP Trap and Catalog configurations.

Refer to your online OS documentation for more information on how to use your standard registry editor.

Step 1 Choose Alarm > Configuration .

The Alarm Configuration window displays.

Step 2 From the Server drop-down box, choose the server for which you want to configure the alarm.

Step 3 From the Service drop-down box, choose the service for which you want to configure the alarm.

Note The drop-down list box displays all services (active and inactive).

In the Alarm Configuration window, a list of alarm monitors with the event levels displays for the chosen service displays.

Step 4 Check the check box or boxes for the desired alarm destination as described in Table 3-1 .

Step 5 In the Alarm Event Level selection box, click the Down arrow.

A list with event levels displays.

Step 6 Click the desired alarm event level as described in Table 3-2 .

Step 7 To apply the current settings for selected services to all nodes in a cluster, check the Apply to all Nodes check box.

Step 8 To save your configuration, click the Save button.

Note To set the default, click the Set Default button; then, click Save .

Additional Information

See the Related Topics .

## Alarm Destination Settings

Table 3-1 describes the alarm destination settings.

Table 3-1 Alarm Destinations

Enable Alarm for Local Syslogs

SysLog Viewer. The program logs Cisco Unified Presence Server errors in the Application Logs within SysLog Viewer and provides a description of the alarm and a recommended action. You can access the SysLog Viewer from the Serviceability Real-Time Monitoring Tool.

For information on viewing logs with the SysLog Viewer, see the "Using SysLog Viewer in RTMT" section on page 11-1 .

Enable Alarm for Remote Syslogs

Syslog file. Check this check box to enable the Syslog messages to be stored on a Syslog server and to specify the Syslog server name. If this destination is enabled and no server name is specified, Cisco Unified Presence Server does not send the Syslog messages.

Note If you want to send the alarms to CiscoWorks 2000, specify the CiscoWorks 2000 server name.

Enable Alarm for SDI Trace

The SDI trace library.

To log alarms in the SDI trace log file, check this check box, and check the Trace On check box in Trace Configuration window for the chosen service.

For more information on by using the Trace Configuration window, see the "Configuring Trace Parameters" section on page 5-1 .

Additional Information

See the Related Topics .

## Alarm Event Level Settings

Table 3-2 describes the alarm event level settings.

Table 3-2 Alarm Event Levels

Emergency

This level designates system as unusable.

Alert

This level indicates that immediate action is needed.

Critical

Cisco Unified Presence Server detects a critical condition.

Error

This level signifies an error condition exists.

Warning

This level indicates that a warning condition is detected.

Notice

This level designates a normal but significant condition.

Informational

This level designates information messages only.

Debug

This level designates detailed event information that Cisco TAC engineers use for debugging.

Additional Information

See the Related Topics .

## Related Topics

• Configuring or Updating an Alarm for a Service

• Alarm Destination Settings

• Alarm Event Level Settings

| Name | Destination description |
|---|---|
| Enable Alarm for Local Syslogs | SysLog Viewer. The program logs Cisco Unified Presence Server errors in the Application Logs within SysLog Viewer and provides a description of the alarm and a recommended action. You can access the SysLog Viewer from the Serviceability Real-Time Monitoring Tool. For information on viewing logs with the SysLog Viewer, see the "Using SysLog Viewer in RTMT" section on page 11-1 . |
| Enable Alarm for Remote Syslogs | Syslog file. Check this check box to enable the Syslog messages to be stored on a Syslog server and to specify the Syslog server name. If this destination is enabled and no server name is specified, Cisco Unified Presence Server does not send the Syslog messages. Note If you want to send the alarms to CiscoWorks 2000, specify the CiscoWorks 2000 server name. |
| Enable Alarm for SDI Trace | The SDI trace library. To log alarms in the SDI trace log file, check this check box, and check the Trace On check box in Trace Configuration window for the chosen service. For more information on by using the Trace Configuration window, see the "Configuring Trace Parameters" section on page 5-1 . |

| Name | Description |
|---|---|
| Emergency | This level designates system as unusable. |
| Alert | This level indicates that immediate action is needed. |
| Critical | Cisco Unified Presence Server detects a critical condition. |
| Error | This level signifies an error condition exists. |
| Warning | This level indicates that a warning condition is detected. |
| Notice | This level designates a normal but significant condition. |
| Informational | This level designates information messages only. |
| Debug | This level designates detailed event information that Cisco TAC engineers use for debugging. |