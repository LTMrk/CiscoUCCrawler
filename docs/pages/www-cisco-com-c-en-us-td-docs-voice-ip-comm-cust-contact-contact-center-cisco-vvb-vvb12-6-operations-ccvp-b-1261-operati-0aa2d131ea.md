---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb12-6-operations-ccvp-b-1261-operati-0aa2d131ea
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb12_6/operations/ccvp_b_1261-operations-guide-for-cisco-virtualized-voice-browser/ccvp_b_1252-operations-guide-for-cisco-virtualized-voice-browser_chapter_01.html
retrieved_at: 2026-08-21T16:31:01.818129+00:00
---

Operations Guide for Cisco Virtualized Voice Browser, Release 12.6(1)

# Operations Guide for Cisco Virtualized Voice Browser, Release 12.6(1)

Find Matches in This Book

## Results

Updated: May 12, 2021

Chapter: Serviceability

## Chapter: Serviceability

# Serviceability

Cisco VVB Serviceability provides configuration details for the following functionality:

Configuring alarms for local and remote Syslogs.

Configuration trace settings for VVB components. After these settings are enabled, you can collect and view trace information
                                 using the Real-Time Monitoring Tool (RTMT).

Configuring and managing log profiles for different VVB components.

Setting Java Virtual Machine (JVM) parameters for different VVB services to collect thread and memory traces.

Cisco VVB does not support clustering. Therefore, you may ignore any message on the Cisco VVB Admin UI/CLI that refers to cluster , publisher , subscriber , etc.

For more information, see Cisco Virtualized Voice Browser Serviceability Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html

## Alarms

You can view alarm information by using the SysLog Viewer in Cisco Unified Real-Time Monitoring Tool (RTMT).

For more information, see Cisco Virtualized Voice Browser Serviceability Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html

## Traces

A trace
                              		  file is a log file that records activity from the Cisco VVB components.
                              		  Trace files provide detailed information about specific errors and help you
                              		  troubleshoot the errors.

The Cisco VVB system also generates information about all threads that are running in the system. This information is stored in the thread
                              dump file and is useful for troubleshooting.

For more information, see Cisco Virtualized Voice Browser Serviceability Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html

## Serviceability
                        	 Tools

### Network
                           	 Services

Network
                                 		  services include services that the system requires to function and are
                                 		  activated by default.

After
                                 		  you install your application, network services start automatically.

For more information, see Cisco Virtualized Voice Browser Serviceability Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html

| Note | Cisco VVB does not support clustering. Therefore, you may ignore any message on the Cisco VVB Admin UI/CLI that refers to cluster , publisher , subscriber , etc. |
|---|---|

| Note | For more information, see Cisco Virtualized Voice Browser Serviceability Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html |
|---|---|