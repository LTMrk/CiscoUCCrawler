---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-tapi-dev-15-cucm-b-tapi-dev-guide-15-cucm-b-tapi-dev-guide-1251-appendi-cc194b25fe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/tapi_dev/15/cucm_b_tapi-dev-guide-15/cucm_b_tapi-dev-guide-1251_appendix_01010.html
retrieved_at: 2026-08-16T18:05:57.230389+00:00
---

Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: August 11, 2026

Chapter: Troubleshooting Cisco Unified TAPI

## Chapter: Troubleshooting Cisco Unified TAPI

# Troubleshooting Cisco Unified TAPI

This appendix contains information about troubleshooting Cisco Unified Communication manager. It contains the following sections:

## TSP Trace of Internal Messages

Step 1

Choose Start > Settings > Control Panel and select Phone and Modem Options .

Step 2

Click Advanced tab and select the CiscoTSP 0xx and click Configure button.

Step 3

Click Trace tab. Select Trace On check box and select 1 . TSP Trace to trace the TSP internal messages. Select Error to just log errors in the TSP Select Detailed to log internal messages for debugging purposes. Select 2. CTI Trace to trace the messages sent between CTI and TSP. Select 3. TSPI Trace to trace the requests and events that are sent between TSP and TAPI.

Step 4

Set up a Directory that is the path for the trace log. For example, c:\Temp No. of Files: Setting this to a value greater
                                       than or equal to 1 enables rolling log files. For example, a value of 10 will cause up to 10 log files to be used in a cyclic
                                       fashion. Max lines/file: specifies the maximum number of trace statements that will be written to each log file. For example,
                                       a value of 1000 will cause up to 1000 trace statements to be written to each log file.

## TSP Operation Verification

To verify the TSP operation on the machine where the TSP is installed, use the Microsoft Windows Phone Dialer Application.
                           Find this application in the C:\Program Files\Windows NT directory under the name dialer.exe. When the program is run, a dialog
                           box displays that asks which line and address the user wants to use to connect. If there are no lines in the Line drop down
                           list, then a problem may exist between the TSP and the Cisco Unified Communications Manager . If lines are available, choose one of the lines, keep the Address set to zero (0) and click OK . Enter a Number to dial, and a call should be placed to that number. If call is successful, you know that the TSP is operational
                           on the machine where the TSP is installed. If problems are encountered with installation and setup of Remote TSP, this test
                           represents a good way to verify whether the TSP is operating properly and that the problem is with the configuration and setup
                           of Remote TSP.

## Version Compatibility

Cisco recommends that the TSP client should always use the plug-in that is downloaded from corresponding Cisco Unified Communications Manager server.

## Cisco TSP Readme

The Cisco Unified Communications Manager TSP readme file is copied to the client PC when TSP plug-in is installed.

## Unsupported CTI
                        	 Events for SIP Phones

The following CTI events are not generated for SIP phones. Third party
                              		  applications that expect these call events should use SCCP phones:

CallOpenLogicalChannelEvent

CallRingEvent

DeviceLampModeChangedEvent

DeviceModeChangedEvent

DeviceDisplayChangedEvent

DeviceFeatureButtonPressedEvent

DeviceKeyPressedEvent

DeviceLampModeChangedEvent

DeviceRingModeChangedEvent

| Step 1 | Choose Start > Settings > Control Panel and select Phone and Modem Options . |
|---|---|
| Step 2 | Click Advanced tab and select the CiscoTSP 0xx and click Configure button. |
| Step 3 | Click Trace tab. Select Trace On check box and select 1 . TSP Trace to trace the TSP internal messages. Select Error to just log errors in the TSP Select Detailed to log internal messages for debugging purposes. Select 2. CTI Trace to trace the messages sent between CTI and TSP. Select 3. TSPI Trace to trace the requests and events that are sent between TSP and TAPI. |
| Step 4 | Set up a Directory that is the path for the trace log. For example, c:\Temp No. of Files: Setting this to a value greater
                                       than or equal to 1 enables rolling log files. For example, a value of 10 will cause up to 10 log files to be used in a cyclic
                                       fashion. Max lines/file: specifies the maximum number of trace statements that will be written to each log file. For example,
                                       a value of 1000 will cause up to 1000 trace statements to be written to each log file. |