---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-operations-guide-ccvp-b-1251--5e9ccf5dbf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/operations/guide/ccvp_b_1251-ccvb-operations-guide-for-cisco-vvb/ccvp_b_1251-ccvb-operations-guide-for-cisco-vvb_chapter_01.html
retrieved_at: 2026-08-21T16:35:02.513355+00:00
---

Operations Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

# Operations Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

Find Matches in This Book

## Results

Updated: February 2, 2020

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