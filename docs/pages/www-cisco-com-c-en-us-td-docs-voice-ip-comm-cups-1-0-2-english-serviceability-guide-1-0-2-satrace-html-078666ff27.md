---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-serviceability-guide-1-0-2-satrace-html-078666ff27
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/serviceability/guide/1_0_2/satrace.html
retrieved_at: 2026-08-21T16:06:06.461364+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Trace Configuration

## Chapter: Trace Configuration

## Trace Configuration

The Trace Configuration window allows you to specify the parameters that you want to trace for troubleshooting Cisco Unified Presence Server problems. You can configure the level of information that you want traced (debug level), what information you want to trace (trace fields), and information about the trace files (such as number of files per service, and size of file). You can configure trace for a single service or apply the trace settings for that service to all servers in the cluster. If the service is a call-processing application such as Cisco Presence Server or Cisco CTIManager, you can configure a trace on devices such as phones and gateways, or you can narrow the trace to enabled phones with a directory number beginning with 555.

After you have configured which information you want to include in the trace files for the various services, you can collect trace files by using the trace and log central option in the Real-Time Monitoring Tool (RTMT). For more information on collecting traces, see the "Trace Collection and Log Central in RTMT" section .

Note Enabling Trace decreases system performance; therefore, enable Trace only for troubleshooting purposes. For assistance in using Trace, contact Cisco TAC.

This chapter contains the following topics:

• Configuring Trace Parameters

• Debug Trace Level Settings

• Trace Output Settings Descriptions and Defaults

## Configuring Trace Parameters

This section describes how to configure trace parameters for Cisco Presence Server services.

Step 1 Choose Trace > Configuration .

The Trace Configuration window displays.

Step 2 From the Server drop-down list box, choose the server that is running the service for which you want to configure trace.

Step 3 From the Service drop-down list box, choose the service for which you want to configure trace.

Note The drop-down list box displays all services (active and inactive).

The trace parameters display for the service that you chose.

Note If you configured Troubleshooting Trace for this service, a message displays at the top of the window that indicates that Troubleshooting Traces have been set. The system disables all fields on the window except the Output Settings. To configure the Output Settings, go to Step 15 . To reset Troubleshooting trace, see the "Troubleshooting Trace Setting Configuration" section .

Step 4 If you want trace to apply to all Cisco Unified Presence Server servers in the cluster, check the Apply to All Nodes check box.

Step 5 From the Debug Trace Level drop-down list box, choose the level of information that you want traced as described in "Debug Trace Level Settings" section .

Step 6 Check the Trace Fields check box for the service that you chose; for example, Cisco Unified Presence Server Trace Fields.

Note If you are configuring trace for the Cisco Presence Server service or the Cisco CTIManager service and you only want trace information for specific Cisco Unified Presence Server devices, go to Step 7 .

Step 7 If the service that you chose has multiple trace fields, check the check boxes next the trace fields that you want to enable; otherwise, check the Enable All Trace check box. Perform one of the following steps:

• If you are configuring trace for the Cisco Presence Server service or the Cisco CTIManager service and you want trace information for specific Cisco Unified Presence Server devices, check the Device Name Based Trace Monitoring check box and continue with Step 8 . The Device Name Based Trace Monitoring option traces only the selected devices, thus narrowing the number of trace logs that are generated and reducing the impact on call processing.

• If you are configuring a service other than Cisco Presence Server service or the Cisco CTIManager service or you do not want to trace information for specific devices, continue with Step 15 .

Step 8 Click the Select Devices button.

The Device Selection for Tracing window displays.

Tip Using Cisco Unified Presence Server Administration System > Enterprise Parameters , configure the maximum number of devices that are available for tracing . Enter a value in the Max Number of Device Level Trace field. The default specifies 12. Refer to the Cisco Unified Presence Server Administration Guide for details.

Step 9 From the Find drop-down list box, choose the device for which you want a trace.

Step 10 Enter the appropriate search criteria for the device for which you want a trace and click the Find button.

The window with the search results displays.

If more pages of search results to view exist, click the First , Previous , Next , or Last button.

Step 11 Click the Trace check box for the device or devices for which you want device-name-based trace monitoring.

Step 12 Click the Save button.

Step 13 When the update finishes, click the browser close button to close the Device Selection for Tracing window and return to the Trace Configuration window.

Step 14 If you want trace to apply to non-devices in addition to devices, check the Include Non-device Traces check box. If check box is checked, set the appropriate debug trace level as described in "Debug Trace Level Settings" section .

Step 15 To limit the number and size of the trace files, specify the trace output setting. See Table 5-3 for descriptions and default values.

Step 16 To save your trace parameters configuration, click the Update button.

The changes to trace configuration take effect immediately for all services except Cisco Messaging Interface. The trace configuration changes for Cisco Messaging Interface take effect in 3 to 5 minutes.

Note To set the default, click the Set Default button.

Additional Information

See the Related Topics .

## Trace Fields

For a description of the individual trace fields, refer to the most current version of this document at the following URL:

http://www.cisco.com/univercd/cc/td/doc/product/voice/cups/1_0/index.htm

## Debug Trace Level Settings

Table 5-1 describes the debug trace level settings for services.

Table 5-1 Debug Trace Levels for Services

Error

Traces alarm conditions and events. Used for all traces that are generated in abnormal path. Uses minimum number of CPU cycles.

Special

Traces all Error conditions plus process and device initialization messages.

State Transition

Traces all Special conditions plus subsystem state transitions that occur during normal operation.

Significant

Traces all State Transition conditions plus media layer events that occur during normal operation.

Entry/Exit

Traces all Significant conditions plus entry and exit points of routines. Not all services use this trace level (for example, Cisco Presence Server does not).

Arbitrary

Traces all Entry/Exit conditions plus low-level debugging information.

Note Do not use this trace level with the Cisco UPS Presence Engine service or the Cisco IP Voice Media Streaming Application service during normal operation.

Detailed

Traces all Arbitrary conditions plus detailed debugging information.

Note Do not use this trace level with the Cisco UPS Presence Engine service or the Cisco IP Voice Media Streaming Application service during normal operation.

Table 5-2 describes the debug trace level settings for servlets.

Table 5-2 Debug Trace Levels for Servlets

Fatal

Traces very severe error events that may cause the application to abort.

Error

Traces alarm conditions and events. Used for all traces that are generated in abnormal path.

Warn

Traces potentially harmful situations.

Info

Traces the majority of servlet problems and has a minimal effect on system performance.

Debug

Traces all State Transition conditions plus media layer events that occur during normal operation.

Trace level that turns on all logging

Additional Information

See the Related Topics .

## Trace Output Settings Descriptions and Defaults

Table 5-3 contains the trace log file descriptions and defaults.

Table 5-3 Trace Output Settings

Maximum number of files

This field specifies the total number of trace files for a given service. Cisco Unified Presence Server automatically appends a sequence number to the file name to indicate which file it is; for example, ccm299.txt. When the last file in the sequence is full, the trace data begins writing over the first file. The default varies by service.

Maximum file size (MB)

This field specifies the maximum size of the trace file in megabytes. The default varies by service.

Additional Information

See the Related Topics .

## Related Topics

• Configuring Trace Parameters

• Trace Output Settings Descriptions and Defaults

• Debug Trace Level Settings

| Level | Description |
|---|---|
| Error | Traces alarm conditions and events. Used for all traces that are generated in abnormal path. Uses minimum number of CPU cycles. |
| Special | Traces all Error conditions plus process and device initialization messages. |
| State Transition | Traces all Special conditions plus subsystem state transitions that occur during normal operation. |
| Significant | Traces all State Transition conditions plus media layer events that occur during normal operation. |
| Entry/Exit | Traces all Significant conditions plus entry and exit points of routines. Not all services use this trace level (for example, Cisco Presence Server does not). |
| Arbitrary | Traces all Entry/Exit conditions plus low-level debugging information. Note Do not use this trace level with the Cisco UPS Presence Engine service or the Cisco IP Voice Media Streaming Application service during normal operation. |
| Detailed | Traces all Arbitrary conditions plus detailed debugging information. Note Do not use this trace level with the Cisco UPS Presence Engine service or the Cisco IP Voice Media Streaming Application service during normal operation. |

| Level | Description |
|---|---|
| Fatal | Traces very severe error events that may cause the application to abort. |
| Error | Traces alarm conditions and events. Used for all traces that are generated in abnormal path. |
| Warn | Traces potentially harmful situations. |
| Info | Traces the majority of servlet problems and has a minimal effect on system performance. |
| Debug | Traces all State Transition conditions plus media layer events that occur during normal operation. Trace level that turns on all logging |

| Field | Description |
|---|---|
| Maximum number of files | This field specifies the total number of trace files for a given service. Cisco Unified Presence Server automatically appends a sequence number to the file name to indicate which file it is; for example, ccm299.txt. When the last file in the sequence is full, the trace data begins writing over the first file. The default varies by service. |
| Maximum file size (MB) | This field specifies the maximum size of the trace file in megabytes. The default varies by service. |