---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-serviceability-administration-guide-1-0-1-sacdrm-html-e3f1c32399
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/serviceability/administration/guide/1_0_1/sacdrm.html
retrieved_at: 2026-08-21T16:08:05.377143+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: CDR Repository Manager Configuration

## Chapter: CDR Repository Manager Configuration

## CDR Repository Manager Configuration

Note Cisco Unified Presence Server Release 1.0(1) does not support CDR management.

Use the CDR Management Configuration window to set the amount of disk space to allocate to call detail record (CDR) and call management record (CMR) files, configure the number of days to preserve files before deletion, and configure up to three billing application server destinations for CDRs. The CDR repository manager service repeatedly attempts to deliver CDR and CMR files to the billing servers that you configure on the CDR Management Configuration window until it delivers the files successfully, until you change or delete the billing application server on the CDR Management Configuration window, or until the files fall outside the preservation window and are deleted.

By default, the system generates the CDRFileDeliveryFailed alert if the Cisco CDR Repository Manager service fails to deliver files to any billing application server. You can configure the alert to send you an e-mail or to page you. For information on configuring alerts, see the "Setting Alert Properties" section . The system generates the CDRFileDeliveryFailureContinues syslog alarm upon subsequent failures to deliver the files to the billing application servers.

When you enable the file deletion based on high water mark parameter, the CDR repository manager service monitors the amount of disk space that CDR and CMR files use. If disk usage exceeds the high water mark that you configure, the system purges the CDR and CMR files that have been successfully delivered to all destinations and loaded into the CAR database (if CAR is activated) until the disk space reaches the low water mark or the system deletes all successfully delivered files. If disk usage still exceeds the high water mark after it deletes all successfully delivered files, the system does not delete any more files, unless the disk usage still exceeds the disk allocation that you configure. If the disk usage still exceeds the disk allocation that you configure, the system purges files beginning with the oldest, regardless of whether the files fall within the preservation window or have been successfully delivered, until the disk usage falls below the high watermark.

Note Regardless of whether you enable the deletion of files based on the high-water mark parameter, if disk usage exceeds the disk allocation that you configure, the CDR repository manager service deletes CDR and CMR files, beginning with the oldest files, until disk utilization falls below the high water mark.

The log partition monitoring service monitors the disk usage of CDR and CMR flat files that have not been delivered to the CDR repository manager. If the disk usage of the log partition on a server exceeds the configured limit and the service has deleted all other log and trace files, the log partition monitor service deletes CDR/CMR files on the subsequent nodes that have not been delivered to the CDR repository manager. For more information on the log partition monitoring services, refer to the "Log Partition Monitoring" section in the Cisco Unified CallManager Serviceability System Guide .

This chapter contains the following topics:

• Configuring the CDR Repository Manager General Parameters

• Configuring Application Billing Servers

• Application Billing Server Parameter Settings

• Deleting Application Billing Servers

• Related Topics

## Configuring the CDR Repository Manager General Parameters

Use the following procedure to set disk utilization and file preservation parameters for CDRs.

Step 1 Choose Tools > CDR Management .

The CDR Management Configuration window displays.

Step 2 Click the CDR Manager general parameter value that you want to change.

Step 3 Enter the appropriate parameters as described in Table 14-1 .

Step 4 Click Update .

Tip At any time, you can click Set Default to specify the default values. After you set the defaults, click Update to save the default values.

Additional Information

See the "Related Topics" section .

## CDR Repository Manager General Parameter Settings

Table 14-1 describes the available settings in the General Parameters section of the CDR Management Configuration window. For related procedures, see the "Related Topics" section .

Table 14-1 CDR Repository Manager General Parameter Settings

Disk Allocation (MB)

Choose the number of megabytes that you want to allocate to CDR and CMR flat file storage. The range and default values vary depending on the size of the repository node hard drive.

The default disk allocation and range varies depending on the size of the server hard drive.

Note If disk usage exceeds the allocated maximum disk space for CDR files, the system generates the CDRMaximumDiskSpaceExceeded alert and deletes all successfully processed files (those delivered to billing servers and loaded to CAR). If disk usage still exceeds the allocated disk space, the system deletes undelivered files and files within the preservation duration, starting with the oldest until disk utilization falls below the high water mark.

Note If you have a large system and do not allocate enough disk space, the system may delete the CDR and CMR files before the CAR Scheduler loads the files into the CAR database. For example, if you configure the CAR Scheduler to run once a day and you set the disk allocation to a value that is not large enough to hold the CDR and CMR files that are generated in a day, the system will delete the files before they are loaded into the CAR database.

High Water Mark (%)

This field specifies the maximum percentage of the allocated disk space for CDR and CMR files. For example, if you choose 2000 megabytes from the Disk Allocation field and 80% from the High Water Mark (%) field, the high water mark equals 1600 megabytes.

When the disk usage exceeds the percentage that you specify and the Disable CDR/CMR Files Deletion Based on HWM check box is unchecked, the system automatically purges all successfully processed CDR and CMR files (those delivered to billing servers and loaded to CAR) beginning with the oldest files to reduce disk usage to the amount that you specify in the Low Water Mark (%) drop-down list box.

If the disk usage still exceeds the low water mark or high water mark, the system does not delete any undelivered or unloaded files, unless the disk usage exceeds the disk allocation.

If you check the Disable CDR/CMR Files Deletion Based on HWM check box, the system does not delete CDRs and CMRs based on the percentage that you specify in this field.

Note If CDR disk space exceeds the high water mark, the system generates the CDRHWMExceeded alert.

Low Water Mark (%)

This field specifies the percentage of disk space that is allocated to CDR and CMR files that is always available for use. For example, if you choose 2000 megabytes from the Disk Allocation field and 40% from the Low Water Mark (%) field, the low water mark equals 800 megabytes.

CDR / CMR Files Preservation Duration (Days)

Choose the number of days that you want to retain CDR and CMR files. The CDR Repository Manager deletes files that fall outside the preservation window.

Disable CDR/CMR Files Deletion Based on HWM

If you do not want to delete CDRs and CMRs even if disk usage exceeds the percentage that you specify in the High Water Mark (%) field, check this check box. By default, this check box remains unchecked, so the system deletes CDRs and CMRs if disk usage exceeds the high water mark.

Note Regardless of whether you enable the deletion of files based on the high-water mark parameter, if disk usage exceeds the disk allocation that you configure, the CDR repository manager service deletes CDR and CMR files, beginning with the oldest files, until disk utilization falls below the high water mark.

CDR Repository Manager Host Name

Lists the host name of the CDR repository manager server.

CDR Repository Manager Host Address

Lists the IP address of the CDR repository manager server.

## Configuring Application Billing Servers

Note Cisco Unified Presence Server Release 1.0(1) does not support CDR management.

Use the following procedure to configure application billing servers to which you want to send CDRs. You can configure up to three billing servers.

Step 1 Choose Tools > CDR Management Configuration .

The CDR Management Configuration window displays.

Step 2 Do one of the following tasks:

• To add a new application billing server, click the Add New button.

• To update an existing application billing server, click the server host name/IP address.

Step 3 Enter the appropriate settings as described in Table 14-2 .

Step 4 Click Add or Update .

Additional Information

See the "Related Topics" section .

## Application Billing Server Parameter Settings

Table 14-2 describes the available settings in the Billing Application Server Parameters section of the CDR Management Configuration window. For related procedures, see the "Related Topics" section .

Table 14-2 Application Billing Server Parameter Settings

Host Name/IP Address

Enter the host name or IP address of the application billing server to which you want to send CDRs.

If you change the value in this field, a prompt asks whether you want to send the undelivered files to the new destination.

Perform one of the following tasks:

• To deliver the files to the new server, click Yes .

• To change the server host name/IP address without sending undelivered files, click No .

The CDR Management service marks the CDR and CMR files as successfully delivered.

User Name

Enter the user name of the application billing server.

Password

Enter the FTP password for the application billing server.

Protocol

Choose the protocol, either FTP or SFTP, that you want to use to send the CDR files to the configured billing servers.

Directory Path

Enter the directory path on the application billing server to which you want to send the CDRs. You should end the path that you specify with a "/" or "\", depending on the operating system that is running on the application billing server.

Note Make sure the FTP user has write permission to the directory.

## Deleting Application Billing Servers

Use the following procedure to delete an application billing server.

Step 1 Choose Tools > CDR Management .

The CDR Management Configuration window displays.

Step 2 Check the check box next to the application billing server that you want to delete and click Delete Selected .

A message displays that indicates that if you delete this server, any CDR or CMR files that have not been sent to this server will not be delivered to this server and will be treated as successfully delivered files.

Tip When you delete a server, the system does not generate the CDRFileDeliveryFailed alert for the files that are not sent to that server.

Step 3 To complete the deletion, click OK .

Additional Information

See the "Related Topics" section .

## Related Topics

• Configuring the CDR Repository Manager General Parameters

• CDR Repository Manager General Parameter Settings

• Configuring Application Billing Servers

• Application Billing Server Parameter Settings

• Deleting Application Billing Servers

Alerts

• Alert Configuration in RTMT

• Alerts, Cisco Unified Presence Server Serviceability Administration Guide

CDRs

• Cisco Unified CallManager CDR Analysis and Reporting Administration Guide

• Cisco Unified CallManager Call Detail Records Definition

| Field | Description |
|---|---|
| Disk Allocation (MB) | Choose the number of megabytes that you want to allocate to CDR and CMR flat file storage. The range and default values vary depending on the size of the repository node hard drive. The default disk allocation and range varies depending on the size of the server hard drive. Note If disk usage exceeds the allocated maximum disk space for CDR files, the system generates the CDRMaximumDiskSpaceExceeded alert and deletes all successfully processed files (those delivered to billing servers and loaded to CAR). If disk usage still exceeds the allocated disk space, the system deletes undelivered files and files within the preservation duration, starting with the oldest until disk utilization falls below the high water mark. Note If you have a large system and do not allocate enough disk space, the system may delete the CDR and CMR files before the CAR Scheduler loads the files into the CAR database. For example, if you configure the CAR Scheduler to run once a day and you set the disk allocation to a value that is not large enough to hold the CDR and CMR files that are generated in a day, the system will delete the files before they are loaded into the CAR database. |
| High Water Mark (%) | This field specifies the maximum percentage of the allocated disk space for CDR and CMR files. For example, if you choose 2000 megabytes from the Disk Allocation field and 80% from the High Water Mark (%) field, the high water mark equals 1600 megabytes. When the disk usage exceeds the percentage that you specify and the Disable CDR/CMR Files Deletion Based on HWM check box is unchecked, the system automatically purges all successfully processed CDR and CMR files (those delivered to billing servers and loaded to CAR) beginning with the oldest files to reduce disk usage to the amount that you specify in the Low Water Mark (%) drop-down list box. If the disk usage still exceeds the low water mark or high water mark, the system does not delete any undelivered or unloaded files, unless the disk usage exceeds the disk allocation. If you check the Disable CDR/CMR Files Deletion Based on HWM check box, the system does not delete CDRs and CMRs based on the percentage that you specify in this field. Note If CDR disk space exceeds the high water mark, the system generates the CDRHWMExceeded alert. |
| Low Water Mark (%) | This field specifies the percentage of disk space that is allocated to CDR and CMR files that is always available for use. For example, if you choose 2000 megabytes from the Disk Allocation field and 40% from the Low Water Mark (%) field, the low water mark equals 800 megabytes. |
| CDR / CMR Files Preservation Duration (Days) | Choose the number of days that you want to retain CDR and CMR files. The CDR Repository Manager deletes files that fall outside the preservation window. |
| Disable CDR/CMR Files Deletion Based on HWM | If you do not want to delete CDRs and CMRs even if disk usage exceeds the percentage that you specify in the High Water Mark (%) field, check this check box. By default, this check box remains unchecked, so the system deletes CDRs and CMRs if disk usage exceeds the high water mark. Note Regardless of whether you enable the deletion of files based on the high-water mark parameter, if disk usage exceeds the disk allocation that you configure, the CDR repository manager service deletes CDR and CMR files, beginning with the oldest files, until disk utilization falls below the high water mark. |
| CDR Repository Manager Host Name | Lists the host name of the CDR repository manager server. |
| CDR Repository Manager Host Address | Lists the IP address of the CDR repository manager server. |

| Field | Description |
|---|---|
| Host Name/IP Address | Enter the host name or IP address of the application billing server to which you want to send CDRs. If you change the value in this field, a prompt asks whether you want to send the undelivered files to the new destination. Perform one of the following tasks: • To deliver the files to the new server, click Yes . • To change the server host name/IP address without sending undelivered files, click No . The CDR Management service marks the CDR and CMR files as successfully delivered. |
| User Name | Enter the user name of the application billing server. |
| Password | Enter the FTP password for the application billing server. |
| Protocol | Choose the protocol, either FTP or SFTP, that you want to use to send the CDR files to the configured billing servers. |
| Directory Path | Enter the directory path on the application billing server to which you want to send the CDRs. You should end the path that you specify with a "/" or "\", depending on the operating system that is running on the application billing server. Note Make sure the FTP user has write permission to the directory. |