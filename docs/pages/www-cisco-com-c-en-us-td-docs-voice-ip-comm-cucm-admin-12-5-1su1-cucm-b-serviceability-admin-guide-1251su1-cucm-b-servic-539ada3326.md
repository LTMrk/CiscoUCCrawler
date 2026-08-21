---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-serviceability-admin-guide-1251su1-cucm-b-servic-539ada3326
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_serviceability-admin-guide-1251su1/cucm_b_serviceability-admin-guide-1251su1_chapter_01.html
retrieved_at: 2026-08-21T01:13:37.923860+00:00
---

Cisco Unified Serviceability Administration Guide, Release 12.5(1)SU1

# Cisco Unified Serviceability Administration Guide, Release 12.5(1)SU1

Updated: June 19, 2019

Chapter: Seviceability Administrative Overview

## Chapter: Seviceability Administrative Overview

# Seviceability Administrative Overview

## Overview

Cisco Unified Serviceability is a web-based troubleshooting tool that provides the following functionality:

Saves alarms
                                    				and events for troubleshooting and provides alarm message definitions.

Saves trace
                                    				information to log files for troubleshooting.

Monitors real-time behavior of components through the Cisco Unified Real-Time Monitoring Tool (Unified RTMT).

Provides audit capability by logging configuration changes to the system by a user or due to result of the user action. This
                                    functionality supports the Information Assurance feature of Unified Communications Manager and Cisco Unity Connection .

Provides
                                    				feature services that you can activate, deactivate, and view through the Service Activation window.

Generates and
                                    				archives daily reports; for example, alert summary or server statistic reports.

Allows Unified Communications Manager , Instant Messaging and Presence and Cisco Unity Connection to work as a managed device for Simple Network Management Protocol (SNMP) remote management and troubleshooting.

Monitors the
                                    				disk usage of the log partition on a node (or all nodes in the cluster).

Monitors the
                                    				number of threads and processes in the system; uses cache to enhance the
                                    				performance.

Unified Communications Manager only : Generates Unified Communications Manager reports for Quality of Service, traffic, and billing information through Cisco Unified Communications Manager CDR Analysis and Reporting .

Instant Messaging and Presence Service uses a different Serviceability interface than the others and therefore is referred to separately when required.

Cisco RIS Data Collector provides Process and Thread statistic counters in the Cisco Unified Real-Time Monitoring Tool. To
                                          configure the maximum number of processes and threads that are allowed, so Cisco RIS Data Collector can provide these associated
                                          counters, access the Maximum Number of Threads and Process service parameter for the Cisco RIS Data Collector service in the
                                          administration interface for your configuration.

Unified Communications Manager : For information on configuring service parameters, refer to the Administration Guide for Cisco Unified Communications Manager .

Cisco Unity Connection : For information on configuring service parameters, refer to the System Administration Guide for Cisco Unity Connection .

Cisco Unity Connection only: For Cisco Unity Connection , you must perform serviceability-related tasks in both Cisco Unified Serviceability and Cisco Unity Connection Serviceability; for example, you may need to start and stop services, view alarms, and configure
                                          traces in both applications to troubleshoot a problem.

Cisco Unified Serviceability supports the functionality that is described in the Cisco Unified Serviceability Administration Guide ; for tasks that are specific to Cisco Unity Connection Serviceability, refer to the Cisco Unity Connection Serviceability Administration Guide .

## Reporting
                        	 Tools

Cisco Unified Serviceability provides the following
                              		  reporting tools:

Unified Communications Manager only:

Unified Communications Manager only: Cisco Unified Communications Manager CDR Analysis and Reporting - Generates Unified Communications Manager reports for Quality of Service, traffic, and billing information through Cisco Unified Communications Manager CDR Analysis and Reporting . For more information, see CDR Analysis and Reporting Administration Guide .

Unified Communications Manager only: Unified Communications Manager Dialed Number Analyzer - Allows you to test and diagnose a deployed Unified Communications Manager dial plan configuration, analyze the test results,
                                          and use the results to improve the dial plan. For more information on how to access and use Dialed Number Analyzer , see Cisco Unified Communications Manager Dialed Number Analyzer Guide .

Unified Communications Manager only: Cisco Unified Reporting Web Application - Allows you to inspect or troubleshoot data
                                          for a standalone server or a cluster. This application, which is separate from Cisco Unified Serviceability, combines data
                                          by category from all accessible Unified Communications Manager servers in a cluster into one output view. Some reports run
                                          health checks to identify conditions that could affect server or cluster operations. If you are an authorized user, you access
                                          Cisco Unified Reporting in the main navigation menu in Cisco Unified Communications Manager Administration or with the File > Cisco Unified Reporting link on the Unified RTMT menu. For more information, see Cisco Unified Reporting Administration Guide .

Serviceability Reports Archive - Archives reports that the Cisco
                                          					 Serviceability Reporter service generates.

Cisco Unified Real-Time Monitoring Tool (Unified RTMT)
                                    				- Monitors real-time behavior of components through Unified RTMT; creates daily
                                    				reports that you can access through the Serviceability Reports Archive. For
                                    				more information, see Cisco Unified Real-Time Monitoring Tool Administration
                                          					 Guide .

You can access
                                    				Cisco Unified IM and Presence Reporting in the main navigation menu in Cisco
                                    				Unified Communications IM and Presence Service.

## Remote
                        	 Serviceability Tools

The content in
                                          			 this section does not apply to Cisco Unity
                                             				Connection .

To supplement the management and administration of the Unified Communications Manager system, you can use remote serviceability
                              tools. Using these tools, you can gather system and debug information for diagnostic help or remote troubleshooting. The tools
                              can process and report on a collection of local or remote Unified Communications Manager configuration information. With customer
                              permission, technical support engineers log in to a Unified Communications Manager server and get a desktop or shell that
                              allows them to perform any function that could be done from a local login session.

Unified Communications Manager supports the following capabilities for remote serviceability:

Simple Network Management Protocol (SNMP) - Provides remote management for managed devices such as Unified Communications
                                    Manager.

Show Command Line Interface - Displays Unified Communications Manager system data.

## Customized Login
                        	 Message

You can upload a
                              		  text file that contains a customized login message that appears on the initial
                              		  Serviceability window.

For
                              		  more information and the procedure for uploading your customized login message,
                              		  refer to the Administration Guide for Cisco Unified Communications Manager .

| Note | Instant Messaging and Presence Service uses a different Serviceability interface than the others and therefore is referred to separately when required. |
|---|---|

| Tip | Cisco RIS Data Collector provides Process and Thread statistic counters in the Cisco Unified Real-Time Monitoring Tool. To
                                          configure the maximum number of processes and threads that are allowed, so Cisco RIS Data Collector can provide these associated
                                          counters, access the Maximum Number of Threads and Process service parameter for the Cisco RIS Data Collector service in the
                                          administration interface for your configuration. Unified Communications Manager : For information on configuring service parameters, refer to the Administration Guide for Cisco Unified Communications Manager . Cisco Unity Connection : For information on configuring service parameters, refer to the System Administration Guide for Cisco Unity Connection . |
|---|---|

| Tip | Cisco Unity Connection only: For Cisco Unity Connection , you must perform serviceability-related tasks in both Cisco Unified Serviceability and Cisco Unity Connection Serviceability; for example, you may need to start and stop services, view alarms, and configure
                                          traces in both applications to troubleshoot a problem. Cisco Unified Serviceability supports the functionality that is described in the Cisco Unified Serviceability Administration Guide ; for tasks that are specific to Cisco Unity Connection Serviceability, refer to the Cisco Unity Connection Serviceability Administration Guide . |
|---|---|

| Note | The content in
                                          			 this section does not apply to Cisco Unity
                                             				Connection . |
|---|---|