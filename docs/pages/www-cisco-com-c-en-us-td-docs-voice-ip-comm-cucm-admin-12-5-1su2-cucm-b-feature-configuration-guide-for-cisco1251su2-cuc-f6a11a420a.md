---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-cucm-b-feature-configuration-guide-for-cisco1251su2-cuc-f6a11a420a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_01.html
retrieved_at: 2026-08-16T17:09:35.314345+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Configuration Tools

## Chapter: Configuration Tools

# Configuration Tools

## About the Feature Configuration Guide

This guide provides information about the tasks that you need to complete in order to configure features on the Unified Communications Manager system. Use this guide after you have configured the call control system, which includes "day 1" configurations such as inbound
                              and outbound calling, dial plans, and network resources. For information about configuring the call control system, see System Configuration Guide for Cisco Unified Communications Manager .

## Configuration Tools Overview

The procedures in this guide require you to use the following two configuration tools:

Cisco Unified Communications Manager Administration

Cisco Unified Serviceability

This chapter provides a brief description of the tools and how to access them.

### Cisco Unified Communications Manager Administration

Cisco Unified Communications Manager Administration Administration is a web-based application that allows you to make individual, manual configuration changes to the Unified Communications Manager nodes. The procedures in this guide describe how to configure features using this application.

If you need to perform bulk configuration tasks and want to automate the configuration process, you can use the Unified Communications Manager Bulk Administration Tool (BAT) to make a large number of configuration changes at the same time. For more information, see Bulk Administration Guide for Cisco Unified Communications Manager .

#### Log In to Cisco Unified CM Administration

Use the following procedure to log in to Cisco Unified Communications Manager Administration . After you log in to Cisco Unified Communications Manager Administration , messages may display that indicate the current state of licenses for Unified Communications Manager in the main window. For example, Unified Communications Manager may identify the following situations:

Unified Communications Manager currently operates with starter (demo) licenses, so upload the appropriate license files.

Unified Communications Manager currently operates with an insufficient number of licenses, so upload additional license files.

Unified Communications Manager does not currently use the correct software feature license. In this case, the Cisco CallManager service stops and does not
                                          start until you upload the appropriate software version license and restart the Cisco CallManager service.

Use the following procedure to browse into the server and log in to Cisco Unified CM Administration .

Step 1

Start your preferred operating system browser.

Step 2

In the address bar of the web browser, enter the following case-sensitive URL:

https://<Unified CM-server-name>:{8443}/ccmadmin/showHome.do

where: <Unified CM-server-name> equals the name or IP address of the server

You can optionally specify a port number.

Step 3

A Security Alert dialog box displays. Click the appropriate button.

Step 4

At the main Cisco Unified CM Administration window, enter the username and password that you specified during Unified Communications Manager installation and click Login . (If you want to clear the content of both fields, click Reset .)

For security purposes, Cisco Unified Communications Manager Administration logs you out after 30 minutes of inactivity, and you must log back in.

### Cisco Unified Communications Manager Serviceability

Some procedures in this guide require you to use the Cisco Unified Serviceability application to start or restart services on the Unified Communications Manager nodes.

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

Allows Unified Communications Manager , IM and Presence Service and Cisco Unity Connection to work as a managed device for Simple Network Management Protocol (SNMP) remote management and troubleshooting.

Monitors the
                                       				disk usage of the log partition on a node (or all nodes in the cluster).

Monitors the
                                       				number of threads and processes in the system; uses cache to enhance the
                                       				performance.

Unified Communications Manager only : Generates Unified Communications Manager reports for Quality of Service, traffic, and billing information through Cisco Unified Communications Manager CDR Analysis and Reporting .

#### Log into Cisco Unified Communications Manager Serviceability

Use the following procedure to log in to Cisco Unified Serviceability .

Step 1

Start your preferred operating system browser.

Step 2

In the address bar of the web browser, enter the following case-sensitive URL:

https://<Unified CM-server-name>:{8443}/ccmadmin/showHome.do

where: <Unified CM-server-name> equals the name or IP address of the server

Step 3

A Security Alert dialog box displays. Click the appropriate button.

Step 4

From Cisco Unified CM Administration, choose Cisco Unified Serviceability from the Navigation menu drop-down list and click Go .

Step 5

Enter the username and password that you specified during Unified Communications Manager installation and click Login .

For security purposes, the system logs you out after 30 minutes of inactivity, and you must log back in.

## Generate a Phone Feature List

Generate a phone feature list report to determine which devices support the feature that you want to configure.

Step 1

From Cisco Unified Reporting, choose System Reports .

Step 2

From the list of reports, click Unified CM Phone Feature List .

Step 3

Perform one of the following steps:

- Choose Generate New Report (the bar chart icon)  to generate a new report.

- Choose Unified CM Phone Feature List if a report exists.

Step 4

From the Product drop-down list, choose All .

Step 5

Click the name of the feature that you want to configure.

Step 6

Click Submit , to generate the report.

| Step 1 | Start your preferred operating system browser. |
|---|---|
| Step 2 | In the address bar of the web browser, enter the following case-sensitive URL: https://<Unified CM-server-name>:{8443}/ccmadmin/showHome.do where: <Unified CM-server-name> equals the name or IP address of the server Note You can optionally specify a port number. | Note | You can optionally specify a port number. |
| Note | You can optionally specify a port number. |
| Step 3 | A Security Alert dialog box displays. Click the appropriate button. |
| Step 4 | At the main Cisco Unified CM Administration window, enter the username and password that you specified during Unified Communications Manager installation and click Login . (If you want to clear the content of both fields, click Reset .) Note For security purposes, Cisco Unified Communications Manager Administration logs you out after 30 minutes of inactivity, and you must log back in. | Note | For security purposes, Cisco Unified Communications Manager Administration logs you out after 30 minutes of inactivity, and you must log back in. |
| Note | For security purposes, Cisco Unified Communications Manager Administration logs you out after 30 minutes of inactivity, and you must log back in. |

| Note | You can optionally specify a port number. |
|---|---|

| Note | For security purposes, Cisco Unified Communications Manager Administration logs you out after 30 minutes of inactivity, and you must log back in. |
|---|---|

| Step 1 | Start your preferred operating system browser. |
|---|---|
| Step 2 | In the address bar of the web browser, enter the following case-sensitive URL: https://<Unified CM-server-name>:{8443}/ccmadmin/showHome.do where: <Unified CM-server-name> equals the name or IP address of the server |
| Step 3 | A Security Alert dialog box displays. Click the appropriate button. |
| Step 4 | From Cisco Unified CM Administration, choose Cisco Unified Serviceability from the Navigation menu drop-down list and click Go . |
| Step 5 | Enter the username and password that you specified during Unified Communications Manager installation and click Login . Note For security purposes, the system logs you out after 30 minutes of inactivity, and you must log back in. | Note | For security purposes, the system logs you out after 30 minutes of inactivity, and you must log back in. |
| Note | For security purposes, the system logs you out after 30 minutes of inactivity, and you must log back in. |

| Note | For security purposes, the system logs you out after 30 minutes of inactivity, and you must log back in. |
|---|---|

| Step 1 | From Cisco Unified Reporting, choose System Reports . |
|---|---|
| Step 2 | From the list of reports, click Unified CM Phone Feature List . |
| Step 3 | Perform one of the following steps: Choose Generate New Report (the bar chart icon)  to generate a new report. Choose Unified CM Phone Feature List if a report exists. |
| Step 4 | From the Product drop-down list, choose All . |
| Step 5 | Click the name of the feature that you want to configure. |
| Step 6 | Click Submit , to generate the report. |