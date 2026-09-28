---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-admin-cucm-b-serviceability-admin-guide-1251-cucm-b-servic-8ea8e797f2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/admin/cucm_b_serviceability-admin-guide-1251/cucm_b_serviceability-admin-guide-1251_chapter_0110.html
retrieved_at: 2026-08-21T01:09:26.744130+00:00
---

Cisco Unified Serviceability Administration Guide, Release 12.5(1)

# Cisco Unified Serviceability Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Tools and Reports

## Chapter: Tools and Reports

# Tools and Reports

## Serviceability Reports Archive

The Cisco Serviceability Reporter service generates daily reports containing charts that display a summary of the  statistics
                           for that particular report.
                           		Reporter generates reports once a day on the basis of logged information.

Using the serviceability GUI, view reports from Tools > Serviceability
                                 			 Reports Archive . You must activate the Cisco
                           		Serviceability Reporter service before you can view reports. After you activate
                           		the service, report generation may take up to 24 hours.

The reports contain 24-hour data for the previous day. A suffix
                           		that is added to the report names shows the date for which Reporter generated
                           		them; for example, AlertRep_mm_dd_yyyy.pdf. The Serviceability Reports Archive
                           		window uses this date to display the reports for the relevant date only. The
                           		reports generate from the data that is present in the log files, with the
                           		timestamp for the previous day. The system considers log files for the current
                           		date and the previous two days for collecting data.

The time that is shown in the report reflects the server "System Time."

You can retrieve log files from the server while you are generating
                           		  reports.

The Cisco Unified Reporting web application provides snapshot views of
                                       		  data into one output and runs data checks. The application also allows you to archive generated reports. See the Cisco Unified Reporting Administration Guide for more
                                       		  information.

### Serviceability Report Archive Considerations for Cluster Configurations

This section applies to Unified Communications Manager and IM and Presence Service only.

Because the Cisco Serviceability Reporter is
                                    		  only active on the first server, at any time, Reporter generates reports only
                                    		  on the first server, not the other servers.

The time that is shown in the report reflects the
                                    		first server "System Time." If the first server and subsequent servers are in
                                    		different time zones, the first server "System Time" shows in the report.

The time zone
                                    		differences between the server locations in a cluster are taken into account when data is collected for the reports.

You can select log files from individual servers or from all servers in the cluster when you generate
                                    		  reports.

Cisco Unified Reporting web application output and data checks include cluster data from all accessible
                                    		  servers.

### Serviceability
                           	 Reporter Service Parameters

Cisco
                              		Serviceability Reporter uses the following service parameters:

RTMT Reporter
                                    			 Designated Node - Specifies the designated node on which RTMT Reporter runs.
                                    			 This default equals the IP address of the server on which the Cisco
                                    			 Serviceability Reporter service is first activated.

Unified Communications Manager only: Because the Serviceability Reporter service is CPU intensive, Cisco recommends that you
                                    specify a non-call-processing node.

Report Generation
                                    			 Time - Specifies the number of minutes after midnight. Reports are generated at
                                    			 this time for the most recent day. The minimum value equals 0 and the maximum
                                    			 value equals 1439.

Report Deletion
                                    			 Age - Specifies the number of days that the report must be kept on the disk.
                                    			 The system deletes reports that are older than the specified age. The minimum
                                    			 value equals 0, and the maximum value equals 30.

You can disable
                                          		  reports by setting the service parameter Report Deletion Age to a value of 0.

For more
                              		information about service parameter configuration, see the following guides:

Unified Communications Manager only: System Configuration Guide for Cisco Unified Communications Manager

Connection only: System Administration Guide for Cisco Unity
                                          				  Connection

Unified Communications Manager only: If a node is removed completely from the network and does not appear in the list of servers
                                          in Cisco Unified Communications Manager Administration , Reporter does not include that node when it generates reports, even if the log file contains the data for that node.

### Device Statistics Report

The Device Statistics Report does not apply to IM and Presence Service and Cisco Unity Connection .

The Device Statistics Report provides the following line charts:

Number of Registered Phones per Server

Number of H.323 Gateways in the Cluster

Number of Trunks in the Cluster

#### Number of Registered Phones Per Server

A line chart displays the number of registered phones for each Unified Communications Manager server (and cluster in a Unified
                                 Communications Manager cluster configuration). Each line in the chart represents the data for a server for which data is available,
                                 and one extra line displays the clusterwide data (Unified Communications Manager clusters only). Each data value in the chart
                                 represents the average number of phones that are registered for a 15-minute duration. If a server shows no data, Reporter
                                 does not generate the line that represents that server. If no data exists for the server (or for all servers in a Unified
                                 Communications Manager cluster configuration), for registered phones, Reporter does not generate the chart. The message "No data for Device Statistics report available" displays.

#### Number of MGCP Gateways Registered in the Cluster

A line chart displays the number of registered MGCP FXO, FXS, PRI, and T1CAS gateways. Each line represents data only for
                                 the Unified Communications Manager server (or cluster in a Unified Communications Manager cluster configuration); so, four
                                 lines show server (or clusterwide) details for each gateway type. Each data value in the chart represents the average number
                                 of MGCP gateways that are registered for a 15-minute duration. If no data exists for a gateway for the server (or all the
                                 servers in a cluster), Reporter does not generate the line that represents data for that particular gateway. If no data exists
                                 for all gateways for the server (or for all servers in a cluster), Reporter does not generate the chart.

#### Number of H.323 Gateways in the Cluster

A line chart displays the number of H.323 gateways. One line represents the details of the H.323 gateways (or the clusterwide
                                 details in a Unified Communications Manager cluster configuration). Each data value in the chart represents the average number
                                 of H.323 gateways for a 15-minute duration. If no data exists for H.323 gateways for the server (or for all servers in a cluster),
                                 Reporter does not generate the chart.

#### Number of Trunks in the Cluster

A line chart displays the number of H.323 and SIP trunks. Two lines represent the details of the H.323 trunks and SIP trunks
                                 (or the clusterwide details in a Unified Communications Manager cluster configuration). Each data value in the chart represents
                                 the average number of H.323 and SIP trunks for a 15-minute duration. If no data exists for H.323 trunks for the server (or
                                 for all servers in a cluster), Reporter does not generate the line that represents data for the H.323 trunks. If no data exists
                                 for SIP trunks for the server (or for all servers in the cluster), Reporter does not generate the line that represents data
                                 for SIP trunks. If no data exists for trunks at all, Reporter does not generate the chart.

The server (or each server in the cluster) contains log files that match the filename pattern DeviceLog_mm_dd_yyyy_hh_mm.csv.
                                 The following information exists in the log file:

Number of registered phones on the server (or on each server in a Unified Communications Manager cluster)

Number of registered MGCP FXO, FXS, PRI, and T1CAS gateways on the server (or on each server in a Unified Communications Manager
                                       cluster)

Number of registered H.323 gateways on the server (or on each server in a Unified Communications Manager cluster)

Number of SIP trunks and H.323 trunks

### Server Statistics Report

The Server Statistics Report provides the following line charts:

Percentage of CPU per Server

Percentage of Memory Usage per Server

Percentage of Hard Disk Usage of the Largest Partition per Server

Cluster-specific statistics are only supported by Unified Communications Manager and IM and Presence Service .

#### Percentage of CPU Per Server

A line chart displays the percentage of CPU usage for the server (or for each server in a  cluster). The line in the chart
                                 represents the data for the server (or one line for each server in a  cluster) for which data is available. Each data value
                                 in the chart represents the average CPU usage for a 15-minute duration. If no data exists for the server (or for any one server
                                 in a cluster), Reporter does not generate the line that represents that server. If there are no lines to generate, Reporter
                                 does not create the chart. The message "No data for Server Statistics report available" displays.

#### Percentage of Memory Usage Per Server

A line chart displays the percentage of Memory Usage for the Unified Communications Manager server (%MemoryInUse). In a Unified
                                 Communications Manager cluster configuration, there is one line per server in the cluster for which data is available. Each
                                 data value in the chart represents the average memory usage for a 15-minute duration. If no data exists, Reporter does not
                                 generate the chart. If no data exists for any server in a cluster configuration, Reporter does not generate the line that
                                 represents that server.

#### Percentage of Hard Disk Usage of the Largest Partition Per Server

A line chart displays the percentage of disk space usage for the largest partition on the server (%DiskSpaceInUse), or on
                                 each server in a cluster configuration. Each data value in the chart represents the average disk usage for a 15-minute duration.
                                 If no data exists, Reporter does not generate the chart. If no data exists for any one server in a cluster configuration,
                                 Reporter does not generate the line that represents that server.

The server (or each server in a cluster configuration) contains log files that match the filename pattern ServerLog_mm_dd_yyyy_hh_mm.csv.
                                 The following information exists in the log file:

Percentage of CPU usage on the server (or each server in a cluster)

Percentage of Memory usage (%MemoryInUse) on the server (or on each server in a cluster)

Percentage of Hard disk usage of the largest partition (%DiskSpaceInUse) on the server (or on each server in a cluster)

### Service Statistics Report

The Service Statistics Report does not support IM and Presence Service and Cisco Unity Connection .

The Service Statistics Report provides the following line charts:

Cisco CTI Manager: Number of Open Devices

Cisco CTI Manager: Number of Open Lines

Cisco TFTP: Number of Requests

Cisco TFTP: Number of Aborted Requests

#### Cisco CTI Manager: Number of Open Devices

A line chart displays the number of CTI Open Devices for the CTI Manager (or for each CTI Manager in a Unified Communications
                                 Manager cluster configuration). Each line chart represents the data for the server (or on each server in a Unified Communications
                                 Manager cluster) on which service is activated. Each data value in the chart represents the average number of CTI open devices
                                 for a 15-minute duration. If no data exists, Reporter does not generate the chart. If no data exists for any one server in
                                 a Unified Communications Manager cluster configuration, Reporter does not generate the line that represents that server. The
                                 message "No data for Service Statistics report available" displays.

#### Cisco CTI Manager: Number of Open Lines

A line chart displays the number of CTI open lines for the CTI Manager (or per CTI Manager in a Unified Communications Manager
                                 cluster configuration). A line in the chart represents the data for the server (or one line for each server in a Unified Communications
                                 Manager cluster configuration) where the Cisco CTI Manager service is activated. Each data value in the chart represents the
                                 average number of CTI open lines for a 15-minute duration. If no data exists, Reporter does not generate the chart. If no
                                 data exists for any one server in a Unified Communications Manager cluster configuration, Reporter does not generate the line
                                 that represents that server.

#### Cisco TFTP: Number of Requests

A line chart displays the number of Cisco TFTP requests for the TFTP server (or per TFTP server in a Unified Communications
                                 Manager cluster configuration). A line in the chart represents the data for the server (or one line for each server in a Unified
                                 Communications Manager cluster) where the Cisco TFTP service is activated. Each data value in the chart represents the average
                                 number of TFTP requests for a 15-minute duration. If no data exists, Reporter does not generate the chart. If no data exists
                                 for any one server in a Unified Communications Manager cluster configuration, Reporter does not generate the line that represents
                                 that server.

#### Cisco TFTP: Number of Aborted Requests

A line chart displays the number of Cisco TFTP requests that were aborted for the TFTP server (or per TFTP server in a Unified
                                 Communications Manager cluster configuration). A line in the chart represents the data for the server (or one line for each
                                 server in a Unified Communications Manager cluster) where the Cisco TFTP service is activated. Each data value in the chart
                                 represents the average of TFTP requests that were aborted for a 15-minute duration. If no data exists, Reporter does not generate
                                 the chart. If no data exists for any one server in a Unified Communications Manager cluster configuration, Reporter does not
                                 generate the line that represents that server.

The server (or each server in a Unified Communications Manager cluster) contains log files that match the filename pattern
                                 ServiceLog_mm_dd_yyyy_hh_mm.csv. The following information exists in the log file:

For each CTI Manager - Number of open devices

For each CTI Manager - Number of open lines

For each Cisco TFTP server - TotalTftpRequests

For each Cisco TFTP server - TotalTftpRequestsAborted

### Call Activities Report

The Call Activities Report does not support IM and Presence Service and Cisco Unity Connection .

The Call Activities Report provides the following line charts:

Unified Communications Manager Call Activity for a cluster

H.323 Gateways Call Activity for the Cluster

MGCP Gateways Call Activity for the Cluster

MGCP Gateways

Trunk Call Activity for the Cluster

#### Cisco Unified Communications Manager Call Activity for the Cluster

A line chart displays the number of Unified Communications Manager calls that were attempted and calls that were completed.
                                 In a Unified Communications Manager cluster configuration, the line chart displays the number of calls attempted and completed
                                 for the entire cluster. The chart comprises two lines, one for the number of calls that were attempted and another for the
                                 number of calls that were completed. For a Unified Communications Manager cluster configuration, each line represents the
                                 cluster value, which is the sum of the values for all the servers in the cluster (for which data is available). Each data
                                 value in the chart represents the total number of calls that were attempted or calls that were completed for a 15-minute duration.

If no data exists for Unified Communications Manager calls that were completed, Reporter does not generate the line that represents
                                 data for the calls that were completed. If no data exists for Unified Communications Manager calls that were attempted, Reporter
                                 does not generate the line that represents data for the calls that were attempted. In a Unified Communications Manager cluster
                                 configuration, if no data exists for a server in the cluster, Reporter does not generate the line that represents calls attempted
                                 or completed on that server. If no data exists for Unified Communications Manager call activities at all, Reporter does not
                                 generate the chart. The message "No data for Call Activities report available" displays.

#### H.323 Gateways Call Activity for the Cluster

A line chart displays the number of calls that were attempted and calls that were completed for H.323 gateways. In a Unified
                                 Communications Manager cluster configuration, the line chart displays the number of calls attempted and completed for the
                                 entire cluster. The chart comprises two lines, one for the number of calls that were attempted and another for the number
                                 of calls that were completed. For a Unified Communications Manager cluster configuration, each line represents the cluster
                                 value, which equals the sum of the values for all the servers in the cluster (for which data is available). Each data value
                                 in the chart represents the total number of calls that were attempted or calls that were completed for a 15-minute duration.
                                 If no data exists for H.323 gateways calls that were completed, Reporter does not generate the line that represents data for
                                 calls that were completed. If no data exists for H.323 gateways calls that were attempted, Reporter does not generate the
                                 line that represents data for calls that were attempted. In a Unified Communications Manager cluster configuration, if no
                                 data exists for a server in the cluster, Reporter does not generate the line that represents calls attempted or completed
                                 on that server. If no data exists for H.323 gateways call activities at all, Reporter does not generate the chart.

#### MGCP Gateways Call Activity for the Cluster

A line chart displays the number of calls that were completed in an hour for MGCP FXO, FXS, PRI, and T1CAS gateways. In a
                                 Unified Communications Manager cluster configuration, the chart displays the number of calls that were completed for the entire
                                 Unified Communications Manager cluster. The chart comprises four lines at the most, one for the number of calls that were
                                 completed for each of the gateway types (for which data is available). Each data value in the chart represents the total number
                                 of calls that were completed for a 15-minute duration. If no data exists for a gateway, Reporter does not generate the line
                                 that represents data for calls that were completed for a particular gateway. If no data exists for all gateways, Reporter
                                 does not generate the chart.

#### MGCP Gateways

A line chart displays the number of Ports In Service and Active Ports for MGCP FXO, FXS gateways and the number of Spans In
                                 Service or Channels Active for PRI, T1CAS gateways. For a Unified Communications Manager cluster configuration, the chart
                                 displays the data for the entire Unified Communications Manager cluster. The chart comprises eight lines, two lines each for
                                 the number of Ports In Service for MGCP FXO and FXS, and two lines each for the number of Active Ports for MGCP FXO and FXS.
                                 Four more lines for the number of Spans In Service and Channels Active for PRI and T1CAS gateways exist. For a Unified Communications
                                 Manager cluster configuration, each line represents the cluster value, which is the sum of the values for all servers in the
                                 cluster (for which data is available). Each data value in the chart represents the total Number of Ports In Service, Number
                                 of Active Ports, Spans In Service or Channels Active for a 15-minute duration. If no data exists for the number of Spans In
                                 Service or the Channels Active for a gateway (MGCP PRI, T1CAS) for all servers, Reporter does not generate the line that represents
                                 data for that particular gateway.

#### Trunk Call Activity for the Cluster

A line chart displays the number of calls that were completed and calls that were attempted in an hour for SIP trunk and H.323
                                 trunk. For a Unified Communications Manager cluster configuration, the chart displays the number of calls that were completed
                                 and calls that were attempted for the entire Unified Communications Manager cluster. The chart comprises four lines, two for
                                 the number of calls that were completed for each SIP and H.323 trunk (for which data is available) and two for the number
                                 of calls that were attempted. For a Unified Communications Manager cluster configuration, each line represents the cluster
                                 value, which is the sum of the values for all nodes in the cluster (for which data is available). Each data value in the chart
                                 represents the total number of calls that were completed or number of calls that were attempted for a 15-minute duration.
                                 If no data exists for a trunk, Reporter does not generate the line that represents data for the calls that were completed
                                 or the calls that were attempted for that particular trunk. If no data exists for both trunk types, Reporter does not generate
                                 the chart.

The server (or each server in a Unified Communications Manager cluster configuration) contains log files that match the filename
                                 pattern CallLog_mm_dd_yyyy_hh_mm.csv. The following information exists in the log file:

Calls that were attempted and calls that were completed for Unified Communications Manager (or for each server in a Unified
                                       Communications Manager cluster)

Calls that were attempted and calls that were completed for the H.323 gateways (or for the gateways in each server in a Unified
                                       Communications Manager cluster)

Calls that were completed for the MGCP FXO, FXS, PRI, and T1CAS gateways (or for the gateways in each server in a Unified
                                       Communications Manager cluster)

Ports in service, active ports for MGCP FXO and FXS gateways and spans in service, channels active for PRI, and T1CAS gateways
                                       (in each server in a Unified Communications Manager cluster)

Calls that were attempted and calls that were completed for H.323 trunks and SIP trunks

### Alert Summary Report

The Alert Summary Report provides the details of alerts that
                              		are generated for the day.

Cluster-specific statistics are supported only by Unified Communications Manager and IM and Presence Service .

#### Number of Alerts Per Server

A pie chart provides the number of alerts per
                                 		
                                 		node in a cluster. The chart displays the serverwide
                                 		details of the alerts that are generated. Each sector of the pie chart
                                 		represents the number of alerts generated for a particular server in the cluster. The chart includes as many number of
                                 		sectors as there are servers (for which Reporter generates alerts in the day)
                                 		in the cluster. If no data exists for a server, no sector in the chart
                                 		represents that server. If no data exists for all servers, Reporter does not
                                 		generate the chart. The message "No alerts were generated for the day" displays.

Cisco Unity Connection only: A pie chart provides the
                                 		number of alerts for the server. The chart displays the serverwide details of
                                 		the alerts that are generated. If no data exists for the server, Reporter does
                                 		not generate the chart. The message “No alerts were generated for the day”
                                 		displays.

The following chart shows a pie chart example that represents the number of alerts per server in a Unified Communications
                                 Manager cluster.

#### Number of Alerts Per Severity for the Cluster

A pie chart displays the number of alerts per alert severity.
                                 		The chart displays the severity details of the alerts that are generated. Each
                                 		sector of the pie chart represents the number of alerts that are generated of a
                                 		particular severity type. The chart provides as many number of sectors as there
                                 		are severities (for which Reporter generates alerts in the day). If no data
                                 		exists for a severity, no sector in the chart represents that severity. If no
                                 		data exists, Reporter does not generate the chart.

The following chart shows a pie chart example that represents the number of alerts per severity for a Unified Communications
                                 Manager cluster.

#### Top Ten Alerts in the Cluster

A bar chart displays the number of alerts of a particular
                                 		alert type. The chart displays the details of the alerts that are generated on
                                 		the basis of the alert type. Each bar represents the number of alerts for an
                                 		alert type. The chart displays details only for the first ten alerts based on
                                 		the highest number of alerts in descending order. If no data exists for a
                                 		particular alert type, no bar represents that alert. If no data exists for any
                                 		alert type, RTMT does not generate the chart.

The following chart shows a bar chart example that represents the top ten alerts in a Unified Communications Manager cluster.

The server (or each server in a 
                                 		cluster) contains log files that match the
                                 		filename pattern AlertLog_mm_dd_yyyy_hh_mm.csv. The following information
                                 		exists in the log file:

Time - Time at which the alert occurred

Alert Name - Descriptive name

Node Name - Server on which the alert occurred

Monitored object - The object that is monitored

Severity - Severity of this alert

### Performance Protection Report

The Performance Protection Report does not support IM and Presence Service and Cisco Unity Connection .

The Performance Protection Report provides a summary that comprises different charts that display the statistics for that
                              particular report. Reporter generates reports once a day on the basis of logged information.

The Performance Protection Report provides trend analysis information on default monitoring objects for the last seven that
                              allows you to track information about Cisco Intercompany Media Engine . The report includes the Cisco IME Client Call Activity chart that shows the total calls and fallback call ratio for the Cisco IME client.

The Performance Protection report comprises the following charts:

Cisco Unified Communications Manager Call Activity

Number of registered phones and MGCP gateways

System Resource Utilization

Device and Dial Plan Quantities

#### Cisco Unified Communications Manager Call Activity

A line chart displays the hourly rate of increase or decrease for number of calls that were attempted and calls that were
                                 completed as the number of active calls. For a Unified Communications Manager cluster configuration, the data is charted for
                                 each server in the cluster. The chart comprises three lines, one for the number of calls that were attempted, one for the
                                 calls that were completed, and one for the active calls. If no data exists for call activity, Reporter does not generate the
                                 chart.

#### Number of Registered Phones and MGCP Gateways

A line chart displays the number of registered phones and MGCP gateways. For a Unified Communications Manager cluster configuration,
                                 the chart displays the data for each server in the cluster.The chart comprises two lines, one for the number of registered
                                 phones and another for the number of MGCP gateways. If no data exists for phones or MGCP gateways, Reporter does not generate
                                 the chart.

#### System Resource Utilization

A line chart displays the CPU load percentage and the percentage of memory that is used (in bytes) for the server (or for
                                 the whole cluster in a Unified Communications Manager cluster configuration). The chart comprises two lines, one for the CPU
                                 load and one for the memory usage. In a Unified Communications Manager cluster, each line represents the cluster value, which
                                 is the average of the values for all the servers in the cluster (for which data is available). If no data exists for phones
                                 or MGCP gateways, Reporter does not generate the chart.

#### Device and Dial Plan Quantities

Two tables display information from the Unified Communications Manager database about the numbers of devices and number of
                                 dial plan components. The device table shows the number of IP phones, Cisco Unity Connection ports, H.323 clients, H.323 gateways, MGCP gateways, MOH resources, and MTP resources. The dial plan table shows the number
                                 of directory numbers and lines, route patterns, and translation patterns.

### Set Up Serviceability Reports Archive Overview

The following steps provide information for configuring the
                                 		  serviceability report archive feature.

Activate the Cisco Serviceability Reporter service.

Configure the Cisco Serviceability Reporter service parameters.

View the reports that the Cisco Serviceability Reporter service
                                          			 generates.

### Set Up
                           	 Serviceability Reports Archive

The Cisco
                                 		  Serviceability Reporter service generates daily reports in Cisco Unified
                                    			 Serviceability . Each report provides a summary that comprises
                                 		  different charts that display the statistics for that particular report.
                                 		  Reporter generates reports once a day on the basis of logged information.

This section
                                 		  describes how to use the Serviceability Reports Archive window.

#### Before you begin

Activate the
                                 		  Cisco Serviceability Reporter service, which is CPU intensive. After you
                                 		  activate the service, report generation may take up to 24 hours.

Unified Communications Manager only: Cisco recommends that you activate the service on a non-call-processing server.

Choose Tools > Serviceability Reports
                                                				  Archive .

The
                                             				Serviceability Reports Archive window displays the month and year for which the
                                             				reports are available.

From the
                                          			 Month-Year pane, choose the month and year for which you want to display
                                          			 reports.

A list of days
                                             				that correspond to the month displays.

To view reports,
                                          			 click the link that corresponds to the day for which reports were generated.

The report files
                                             				for the day that you chose display.

To view a
                                          			 particular PDF report, click the link of the report that you want to view.

If you browsed
                                                         				  into Cisco Unified
                                                            					 Serviceability by using the node name, you must log in to Cisco Unified
                                                            					 Serviceability before you can view the report.

If your
                                                         				  network uses Network Address Translation (NAT) and you are trying to access
                                                         				  serviceability reports inside the NAT, enter the IP address for the private
                                                         				  network that is associated with the NAT in the browser URL. If you are trying
                                                         				  to access the reports outside the NAT, enter the public IP address, and NAT
                                                         				  will accordingly translate/map to the private IP address.

To view PDF
                                                         				  reports, you must install Acrobat Reader on your machine. To download Acrobat
                                                         				  Reader, click the link at the bottom of the Serviceability Reports Archive
                                                         				  window.

A window opens
                                             				and displays the PDF file of the report that you chose.

### Access to Serviceability Reports Archive

#### Activate Serviceability Reports Archive

Select Tools > Service Activation .

Select the required server from the Server list box, and then select Go .

Navigate to the Performance and Monitoring services pane.

Check the Cisco Serviceability Reporter service checkbox, and then select Save .

Select Tools > Control Center - Feature Services .

Select the required server from the Server list box, and then select Go .

Navigate to the Performance and Monitoring services pane and locate the Cisco Serviceability Reporter.

Verify that the status of the Cisco Serviceability Reporter is Started and Activated. If the Cisco Serviceability Reporter
                                             is not running, select the Cisco Serviceability Reporter and select Start .

##### What to do next

If you opened Cisco Unified IM and Presence Serviceability by entering the server name in the browser, you must sign in to Cisco Unified IM and Presence Serviceability before you can view the report.

The Cisco Unified IM and Presence Serviceability service generates reports only on the first node, even if you turn on the service on other nodes.

#### Access Serviceability Reports Archive

##### Before you begin

Activate the Cisco Serviceability Reporter service. After you activate the service, report generation may take up to 24 hours.

Select Tools > Serviceability Reports Archive .

Select the month and year for which you want to display reports in the Month-Year section.

Select the link that corresponds to the day for which reports were generated to view the required report.

Select the link of the report that you want to view to view a particular PDF report.

The section in the Trace Filter Settings area that relates to devices is not relevant to IM and Presence .

If you opened Cisco Unified IM and Presence Serviceability by entering the server name in the browser, you must sign in to Cisco Unified IM and Presence Serviceability before you can view the report.

## CDR Repository Manager

This section does not apply to IM and Presence Service .

Use the CDR Management Configuration window to set the amount of
                           		disk space to allocate to call detail record (CDR) and call management record
                           		(CMR) files, configure the number of days to preserve files before deletion,
                           		and configure up to three billing application server destinations for CDRs. The
                           		CDR Repository Manager service repeatedly attempts to deliver CDR and CMR files
                           		to the billing servers that you configure in the CDR Management Configuration
                           		window until it delivers the files successfully, until you change or delete the
                           		billing application server on the CDR Management Configuration window, or until
                           		the files fall outside the preservation window and are deleted.

To access the Enterprise Parameters Configuration window, open Cisco Unified Communications Manager Administration and choose System > Enterprise
                                             				Parameters . The CDR File Time Interval parameter specifies the time interval for
                                       		  collecting CDR data. For example, if this value is set to 1, each file will
                                       		  contain 1 minute of CDR data (CDRs and CMRs, if enabled). The external billing
                                       		  server and CAR database will not receive the data in each file until the
                                       		  interval has expired, so consider how quickly you want access to the CDR data
                                       		  when you decide what interval to set for this parameter. For example, setting
                                       		  this parameter to 60 means that each file will contain 60 minutes worth of
                                       		  data, but that data will not be available until the 60-minute period has
                                       		  elapsed, and the records are written to the CAR database. and the CDR files are
                                       		  sent to the configured billing servers. The default value equals 1. The
                                       		  minimum value specifies 1, and the maximum value specifies 1440. The unit of
                                       		  measure for this required field represents a minute.

Both the CDR Agent and the CDR Repository Manager process files
                           		with an interval that is independent of the CDR File Time Interval. The CDR
                           		Repository Manager sends all existing CDR files to the billing application
                           		servers, sleeps for 6 seconds before checking the new files to send, and
                           		continues that 6-second interval. If the destination (the external billing
                           		application servers) does not respond, the system attempts the process again by
                           		using a doubled length of the sleep interval (12 seconds). Each delivery
                           		failure results in double the sleep time (6, 12, 24, 48,and so on, seconds)
                           		until 2 minutes occurs, then stays at 2-minute intervals until successful
                           		delivery occurs. After successful delivery, the 6-second interval automatically
                           		resumes.

Users cannot configure the 6-second processing time, with the
                           		sleep time interval doubling in case of failure. Users can configure only the CDR File Time Interval enterprise parameter. No alert gets sent
                           		after the first file delivery failure. By default, the system generates the
                           		CDRFileDeliveryFailed alert after the second delivery failure of the Cisco CDR
                           		Repository Manager service to deliver files to any billing application server.
                           		You can configure the alert to send you an e-mail or to page you. For
                           		information on configuring alerts, see the "Working with Alerts" chapter in the Cisco Unified Real-Time Monitoring Tool Administration Guide .

The system generates the CDRFileDeliveryFailureContinues syslog
                           		alarm upon subsequent failures to deliver the files to the billing application
                           		servers.

The CDR Agent behaves in almost the same manner. First, it
                           		sends all the existing CDR files to the publisher. If no additional files to
                           		send exist, the CDR Agent sleeps for 6 seconds before checking for new files.
                           		Each delivery failure results in the immediate change of the sleep interval to
                           		1 minute, then says at 1-minute intervals until successful delivery. After the
                           		first successful delivery of files, the 6-second interval resumes.

The system sends no alert after the first file delivery failure
                           		by the CDR Agent. By default, the system generates the CDRAgentSendFileFailed
                           		alert after the second delivery failure of the CDR Agent. You can configure the
                           		alert to send you an email or to page you. For information on configuring
                           		alerts, see the "Working with Alerts" chapter in the Cisco Unified Real-Time Monitoring Tool Administration Guide

The system generates the CDRAgentSendFileFailedContinues syslog
                           		alarm upon subsequent failures to deliver the files.

If you need to start or restart the file transfer timer, you can restart the Cisco CDR Repository Manager or CDR Agent process
                           		by going to the Cisco Unified Serviceability window and selecting Tools > Control
                                 			 Center > Network Services .

When you enable the file deletion based on high water mark
                           		parameter, the CDR repository manager service monitors the amount of disk space
                           		that CDR and CMR files use. If disk usage exceeds the high water mark that you
                           		configure, the system purges the CDR and CMR files that have been successfully
                           		delivered to all destinations and loaded into the CAR database (if CAR is
                           		activated) until the disk space reaches the low water mark or the system
                           		deletes all successfully delivered files. If disk usage still exceeds the high
                           		water mark after the system deletes all successfully delivered files, it does
                           		not delete any more files, unless the disk usage still exceeds the disk
                           		allocation that you configure. If the disk usage still exceeds the disk
                           		allocation that you configure, the system purges files beginning with the
                           		oldest, regardless of whether the files fall within the preservation window or
                           		have been successfully delivered, until the disk usage falls below the high
                           		water mark.

Regardless of whether you enable the deletion of files based on the
                                       		  high water mark parameter, if disk usage exceeds the disk allocation that you
                                       		  configure, the CDR repository manager service deletes CDR and CMR files,
                                       		  beginning with the oldest files, until disk utilization falls below the high
                                       		  water mark.

The Cisco Log Partition Monitoring Tool service monitors the
                           		disk usage of CDR and CMR flat files that have not been delivered to the CDR
                           		repository manager.

Unified Communications Manager only: If the disk usage of the log partition on a server exceeds the configured limit and the
                           service has deleted all other log and trace files, the log partition monitor service deletes CDR/CMR files on the subsequent
                           nodes that have not been delivered to the CDR repository manager.

For more information about log partition monitoring, see the Cisco Unified Real-Time Monitoring Tool Administration Guide .

### Set Up General Parameters

To set disk utilization and file preservation parameters for
                                 		  CDRs, perform the following procedure.

Choose Tools > CDR
                                                				  Management .

The CDR Management window displays.

Click the CDR Manager general parameter value that you want to
                                          			 change.

Enter the appropriate CDR Repository Manager general parameter settings.

Click Update .

At any time, you can click Set Default to specify the default values. After you set the
                                                         				  defaults, click Update to save the default values.

### General Parameter
                           	 Settings

The following
                              		table describes the available settings in the General Parameters section of the
                              		CDR Management Configuration window.

Disk
                                          				  Allocation (MB)

Choose the number of megabytes that you want to allocate to CDR
                                          				  and CMR flat file storage.

The
                                          				  default disk allocation and range vary depending on the size of the server hard
                                          				  drive.

The maximum disk allocation space equals 3328 MB for a Unified Communications Manager server.

If disk
                                                      					 usage exceeds the allocated maximum disk space for CDR files, the system
                                                      					 generates the CDRMaximumDiskSpaceExceeded alert and deletes all successfully
                                                      					 processed files (those delivered to billing servers and loaded to CAR). If disk
                                                      					 usage still exceeds the allocated disk space, the system deletes undelivered
                                                      					 files and files within the preservation duration, starting with the oldest,
                                                      					 until disk utilization falls below the high water mark.

If you have
                                                      					 a large system and do not allocate enough disk space, the system may delete the
                                                      					 CDR and CMR files before the CAR Scheduler loads the files into the CAR
                                                      					 database. For example, if you configure the CAR Scheduler to run once a day and
                                                      					 you set the disk allocation to a value that is not large enough to hold the CDR
                                                      					 and CMR files that are generated in a day, the system will delete the files
                                                      					 before they are loaded into the CAR database.

High
                                          				  Water Mark (%)

This field specifies the maximum percentage of the allocated disk space for CDR and CMR files. For example, if you choose
                                          2000 megabytes from the Disk Allocation field and 80% from the High Water Mark (%) field, the high water mark equals 1600
                                          megabytes. In addition to the high water mark percentage, the number of CDRs in the CAR database cannot exceed two million
                                          records for a Unified Communications Manager server.

When
                                          				  the disk usage exceeds the percentage that you specify, or the total number of
                                          				  CDRs is exceeded, and the Disable CDR/CMR Files Deletion Based on HWM check box
                                          				  is unchecked, the system automatically purges all successfully processed CDR
                                          				  and CMR files (those delivered to billing servers and loaded to CAR) beginning
                                          				  with the oldest files to reduce disk usage to the amount that you specify in
                                          				  the Low Water Mark (%) drop-down list box.

If
                                          				  the disk usage still exceeds the low water mark or high water mark, the system
                                          				  does not delete any undelivered or unloaded files, unless the disk usage
                                          				  exceeds the disk allocation.

If
                                          				  you check the Disable CDR/CMR Files Deletion Based on HWM check box, the system
                                          				  does not delete CDRs and CMRs based on the percentage that you specify in this
                                          				  field.

If CDR disk
                                                      					 space exceeds the high water mark, the system generates the CDRHWMExceeded
                                                      					 alert.

Low
                                          				  Water Mark (%)

This
                                          				  field specifies the percentage of disk space that is allocated to CDR and CMR
                                          				  files that is always available for use. For example, if you choose 2000
                                          				  megabytes from the Disk Allocation field and 40% from the Low Water Mark (%)
                                          				  field, the low water mark equals 800 megabytes.

CDR /
                                          				  CMR Files Preservation Duration (Days)

Choose the number of days that you want to retain CDR and CMR
                                          				  files. The CDR Repository Manager deletes files that fall outside the
                                          				  preservation window.

If you
                                                      					 continuously receive the CDRMaximumDiskSpaceExceeded alarm, you either must
                                                      					 increase the disk allocation or lower the number of preservation days.

Disable CDR/CMR Files Deletion Based on HWM

Regardless
                                                      					 of whether you enable the deletion of files based on the high-water mark
                                                      					 parameter, if disk usage exceeds the disk allocation that you configure, the
                                                      					 maximum database size, or the maximum number of records for your installation,
                                                      					 the CDR repository manager service deletes CDR and CMR files, beginning with
                                                      					 the oldest files, until disk utilization falls below the high water mark.

If
                                          				  you do not want to delete CDRs and CMRs even if disk usage exceeds the
                                          				  percentage that you specify in the High Water Mark (%) field, check this check
                                          				  box. By default, this check box remains unchecked, so the system deletes CDRs
                                          				  and CMRs if disk usage exceeds the high water mark.

CDR
                                          				  Repository Manager Host Name

This
                                          				  field lists the hostname of the CDR repository manager server.

CDR
                                          				  Repository Manager Host Address

This
                                          				  field lists the IP address of the CDR repository manager server.

### Set Up Application Billing Servers

Use the following procedure to configure application billing
                                 		  servers to which you want to send CDRs. You can configure up to three billing
                                 		  servers.

Cipher Support

For Unified Communications Manager 11.5 and earlier versions, Unified Communications Manager advertises the following CBC
                                 ciphers for SFTP connections:

aes128-cbc

3des-cbc

blowfish-cbc

Make sure that the backup SFTP Server supports one of these CBC ciphers to communicate with Unified Communications Manager.

From Unified Communications Manager 12.0 release onwards, CBC ciphers are not supported. Unified Communications Manager supports
                                 and advertises only the following CTR ciphers:

aes256-ctr

aes128-ctr

aes192-ctr

Make sure that the backup SFTP Server supports one of these CTR ciphers to communicate with Unified Communications Manager.

Choose Tools > CDR Management
                                                				  Configuration .

The CDR Management Configuration window displays.

Perform one of the following tasks:

To add a new application billing server, click the Add New button.

To update an existing application billing server, click the
                                                   				  server hostname/IP address.

Enter the application billing server parameter settings.

Click Add or Update .

### Application Billing Server Parameter Settings

The following table describes the available settings in the Billing Application Server Parameters section of the CDR Management
                              Configuration window.

Host Name/IP Address

Enter the hostname or IP address of the application billing server to which you want to send CDRs.

If you change the value in this field, a prompt asks whether you want to send the undelivered files to the new destination.

- To deliver the files to the new server, click Yes .

- To change the server hostname/IP address without sending undelivered files, click No . The CDR Management service marks the CDR and CMR files as delivered.

User Name

Enter the username of the application billing server.

Protocol

Choose the protocol, either FTP or SFTP, that you want to use to send the CDR files to the configured billing servers.

Directory Path

Enter the directory path on the application billing server to which you want to send the CDRs. You should end the path that
                                          you specify with a "/" or "\" , depending on the operating system that is running on the application billing server.

Make sure the FTP user has write permission to the directory.

Password

Enter the password that is used to access the application billing server.

Resend on Failure

When you check the Resend on Failure box, this option informs CDRM to send outdated CDR and CMR files to the billing server
                                          after the FTP or SFTP connection is restored. When the box is checked, the Resend on Failure flag is set to True. When the
                                          box is not checked, the Resend on Failure flag is set to False.

There are several different scenarios that can occur. When the billing server Resend on Failure flag is set to True, all CDR
                                          files get moved to the billing server. When the Resend On Failure flag is set to False, CDR files that get generated during
                                          shutdown of the billing server get moved to the processed folder, but do not get moved to the billing server. When the Resend
                                          on Failure flag gets set to True at the beginning, and then gets changed several times, the result is that the CDR files get
                                          moved to the billing server whenever the Resend on Failure box gets checked.

Generate New Key

Click on the Reset button to generate new keys and reset the connection to the SFTP server.

### Delete Application Billing Servers

Use the following procedure to delete an application billing
                                 		  server.

Choose Tools > CDR
                                                				  Management .

The CDR Management Configuration window displays.

Check the check box next to the application billing server that
                                          			 you want to delete and click Delete Selected .

A message displays that indicates that if you delete this server,
                                             				any CDR or CMR files that have not been sent to this server will not be
                                             				delivered to this server and will be treated as successfully delivered files.

When you delete a server, the system does not generate the
                                                         				  CDRFileDeliveryFailed alert for the files that are not sent to that server.

To complete the deletion, click OK .

### Billing Server Authentication Issue

If you have a billing server deployed with SFTP, and you are using a non-default cipher that you configured on both Unified
                                 Communications Manager and on the billing server, a connection issue may result if you restart a Unified Communications Manager
                                 server, or if you restart the Cisco CallManager service. If this occurs, the billing server will be unable to authenticate
                                 and the connection will be broken.

After the restart, Unified Communications Manager advertises only the default ciphers and will not advertise any new ciphers
                                 that you installed, which will result in an authentication issue if you are using a non-default cipher. If you run into this
                                 issue, generate a new key and reset the connection:

Choose Tools > CDR Management .

The CDR Management Configuration window displays.

Under Billing Application Server Parameters , locate your billing server.

Click Reset to generate a new key that corresponds to your billing server.

## Locations

This section does not apply to IM and Presence Service .

This section explains the Locations feature ( Tools > Locations ) in Cisco Unified Serviceability. This feature enables an administrator to view details of the configured locations in an
                           enterprise, understand the link and intralocation discrepancies, view effective path between the two locations, and identify
                           disconnected groups of locations.

### Locations Topology

Cisco Unified Serviceability Locations Topology provides details of configured locations in your enterprise. Location Topology
                                 refers to a modeled topology representing the flow of media in a network.

The following are some commonly used terms and their definitions:

Assertion

An assertion refers to the location and link bandwidth and weight values configured in a cluster. Asserted values may be replicated
                                 to another cluster.

Discrepancy

A discrepancy occurs if there is a difference
                                 in the location bandwidth values or link bandwidth and  weight values asserted across various
                                 clusters.

Effective Path

An Effective Path is a sequence of intermediate locations connecting two end locations, with weight assigned to each link
                                 between each adjacent pair of locations. The Effective Path, as determined by the least cumulative weight, is the only path
                                 used for bandwidth deductions between any two end locations.

#### View Locations Topology

This section describes how to search and view location topology in Cisco Unified Serviceability.

In Cisco Unified Serviceability, choose Tools > Locations > Topology .

The Locations Topology window appears.

From the Find Locations Where Location Name drop-down box, choose the filter criteria.

Enter the search string in the Find Locations Where Location Name field and then click Find .

The Find Locations Where Location Name field is not casesensitive.

The list of locations is displayed for the chosen filter criteria.

In the list, click to expand any location to view its intralocation details and link details.

The intralocation details include audio, video, and immersive bandwidth whereas the link details contain the details of the
                                                link connecting two locations such as its weight, audio, video and immersive bandwidth.

If the list of locations is long, it may run into multiple pages. To view another page, click the appropriate navigation button
                                                            at the bottom of the Locations Topology window or enter a page number in the Page field. To change the number of locations
                                                            that display in the window, choose a different value from the Rows Per Page drop-down box.

If a location is highlighted by a Caution symbol, this indicates a discrepancy. To view the details of this discrepancy, click View Assertion Details link.

To view the assertion details of any location, click View Assertion Details link at the bottom of the expanded details section.

The Assertion Details window appears.

To return to the Locations Topology window, click Close.

To download the locations topology data in XML format, click Download Topology at the bottom of the Locations Topology window or Download Topology icon in the toolbar at the top.

For more information about the topology data in XML format, see the Cisco Unified Communications Manager XML Developers Guide .

##### View Assertion Details

Intralocation configuration assertions—Includes the intralocation assertion details such as Asserted by Cluster, Audio, Video
                                                and Immersive bandwidth. Asserted by Cluster column lists the names of all the clusters that assert a particular location.

Link assertions—Includes the assertion details of the link that connects two locations, such as Asserted by Cluster, Weight,
                                                Audio, Video, and Immersive bandwidth.

Select Tools > Locations > Locations Topology .

Click the View Assertion Details link in the Locations Topology window.

### Locations Discrepancy

The Locations Discrepancy screen displays the conflicts in assertions for various locations configurations.

The following details are displayed:

Link Configuration Discrepancy—Includes the discrepancy details of the link that connects two locations, such as Weight, Audio,
                                       Video and Immersive bandwidth.

Intralocation Configuration Discrepancy—Includes intralocation discrepancy details such as Audio, Video, and Immersive bandwidth.

#### View Locations Discrepancy

In Cisco Unified Serviceability, choose Tools > Locations > Discrepancy .

The Location Discrepancy window appears.

The list of link configuration discrepancies and intralocation configuration discrepancies is displayed.

The Link Configuration Discrepancy section lists only those link names where discrepancy has been detected. Link names are
                                                            listed in the format <Location Name 1> <--> <Location Name 2> . The Intralocation Configuration Discrepancy section lists only those location names where such discrepancy has been detected.
                                                            The elements in the list are sorted in lexical order.

If no discrepancies are found, the following status message is displayed:

In the list, click on a link name or location name to expand and view its configuration details as asserted by different clusters,
                                             in a tabular view.

The bottom row displays the effective values considered for audio, video, and immersive bandwidth pools and weight (in the
                                                case of links). The values that do not match with the effective values are highlighted in red.

The Effective Value is the least of the values in a particular column. For example, the Effective Value of audio bandwidth
                                                            is the minimum value in the Audio Bandwidth column.

### Effective Path

The Cisco Unified Serviceability Effective Path screen provides details of the effective path that media takes for audio,
                                 video, or immersive calls made between two locations provided by the administrator. This screen displays the Available bandwidth
                                 and the Configured bandwidth across each link and intralocation in the effective path. An administrator can use this report
                                 to determine bandwidth availability across a link and intra-location when there are bandwidth issues in making calls. Cisco
                                 Unified Serviceability Effective Path can also be used to troubleshoot bandwidth issues in making calls and find out where
                                 the bandwidth availability is low.

The Cisco Unified Serviceability Effective Path screen displays the following details between two selected locations:

Quick Path Overview —Displays the cumulative weight and the least of the configured and available Audio, Video, and Immersive
                                       Bandwidth values across the effective path.

Detailed Path View—Displays the weight and bandwidth values (Available and Configured) for Audio, Video, and Immersive calls
                                       for locations and links constituting the effective path, in a tabular view ordered from source location at top to the destination
                                       location at bottom.

The Available bandwidth values displayed in the report are the value at the time of viewing the Effective Path. You can view
                                             the real-time values in the Cisco Unified Real-Time Monitoring Tool.

#### View Effective Path

In Cisco Unified Serviceability, choose Tools > Locations > Effective Path .

The Effective Path window appears.

From the Location drop-down boxes, select any two locations between which effective path is required and then click Find.

Alternatively, start typing the location name in the input box to shortlist the matching location names and then click Find.

The effective path details, which include the Quick Path Overview and Detailed Path View sections, are displayed. If there
                                                is no path between the two selected locations, the following status message is displayed:

No path exists between <From_Location> and <To_Location>.

### Disconnected
                           	 Groups

Cisco
                                 		  Unified Serviceability Disconnected Groups screen enables an administrator to
                                 		  view and analyze any disconnect between the locations that are part of the
                                 		  topology. It displays a list of disconnected groups of locations, which helps
                                 		  an administrator understand which locations need to be connected.

The disconnect in
                                 		  the topology can occur when a link between two locations is not configured or a
                                 		  shared location name is misspelled.

The Disconnected Groups screen displays and compares only
                                             			 disconnected groups of locations. For information on connecting locations, see
                                             			 topics related to location configuration in Administration Guide for Cisco Unified Communications
                                                				Manager .

#### View Disconnected Groups

This section describes how to view disconnected groups in Cisco Unified Serviceability.

In Cisco Unified Serviceability, choose Tools > Locations > Disconnected Groups .

The Disconnected Groups screen appears.

The following table describes the settings that are displayed on the Disconnected Groups screen.

List of Disconnected Groups

Select

Check this box to select a disconnected group to be compared with another disconnected group.

You can select only two groups for comparison.

Group ID

Auto-generated unique identification number of the selected group is displayed here.

Description

The names of the first and last location (as per the alphabetical order) in the group are displayed here.

If a disconnected group has only one node, only the name of that node is displayed here.

No of Locations

The number of locations in a group is displayed here.

Compare Selected Groups

Click this button to display and compare the selected groups. After you click this button, the details that pertain to the
                                                selected groups are displayed.

For every group you select, names of the locations that are part of that group and the corresponding clusters that assert
                                                a location are displayed. See Comparison view for the selected groups below.

Comparison view for the selected groups

Location Name

The names of all the locations that are part of a group are listed in this column.

Asserted by Cluster

The names of all the clusters that assert a particular location are listed  in this column.

If there are no disconnected groups of locations, the following status message is displayed:

No disconnected groups of locations found

The List of Disconnected Groups can be sorted by any column. By default, the groups are sorted by the No. of Locations column.

| Note | The Cisco Unified Reporting web application provides snapshot views of
                                       		  data into one output and runs data checks. The application also allows you to archive generated reports. See the Cisco Unified Reporting Administration Guide for more
                                       		  information. |
|---|---|

| Tip | You can disable
                                          		  reports by setting the service parameter Report Deletion Age to a value of 0. |
|---|---|

| Note | Unified Communications Manager only: If a node is removed completely from the network and does not appear in the list of servers
                                          in Cisco Unified Communications Manager Administration , Reporter does not include that node when it generates reports, even if the log file contains the data for that node. |
|---|---|

| Step 1 | Activate the Cisco Serviceability Reporter service. |
|---|---|
| Step 2 | Configure the Cisco Serviceability Reporter service parameters. |
| Step 3 | View the reports that the Cisco Serviceability Reporter service
                                          			 generates. |

| Step 1 | Choose Tools > Serviceability Reports
                                                				  Archive . The
                                             				Serviceability Reports Archive window displays the month and year for which the
                                             				reports are available. |
|---|---|
| Step 2 | From the
                                          			 Month-Year pane, choose the month and year for which you want to display
                                          			 reports. A list of days
                                             				that correspond to the month displays. |
| Step 3 | To view reports,
                                          			 click the link that corresponds to the day for which reports were generated. The report files
                                             				for the day that you chose display. |
| Step 4 | To view a
                                          			 particular PDF report, click the link of the report that you want to view. Tip If you browsed
                                                         				  into Cisco Unified
                                                            					 Serviceability by using the node name, you must log in to Cisco Unified
                                                            					 Serviceability before you can view the report. If your
                                                         				  network uses Network Address Translation (NAT) and you are trying to access
                                                         				  serviceability reports inside the NAT, enter the IP address for the private
                                                         				  network that is associated with the NAT in the browser URL. If you are trying
                                                         				  to access the reports outside the NAT, enter the public IP address, and NAT
                                                         				  will accordingly translate/map to the private IP address. To view PDF
                                                         				  reports, you must install Acrobat Reader on your machine. To download Acrobat
                                                         				  Reader, click the link at the bottom of the Serviceability Reports Archive
                                                         				  window. A window opens
                                             				and displays the PDF file of the report that you chose. | Tip | If you browsed
                                                         				  into Cisco Unified
                                                            					 Serviceability by using the node name, you must log in to Cisco Unified
                                                            					 Serviceability before you can view the report. If your
                                                         				  network uses Network Address Translation (NAT) and you are trying to access
                                                         				  serviceability reports inside the NAT, enter the IP address for the private
                                                         				  network that is associated with the NAT in the browser URL. If you are trying
                                                         				  to access the reports outside the NAT, enter the public IP address, and NAT
                                                         				  will accordingly translate/map to the private IP address. To view PDF
                                                         				  reports, you must install Acrobat Reader on your machine. To download Acrobat
                                                         				  Reader, click the link at the bottom of the Serviceability Reports Archive
                                                         				  window. |
| Tip | If you browsed
                                                         				  into Cisco Unified
                                                            					 Serviceability by using the node name, you must log in to Cisco Unified
                                                            					 Serviceability before you can view the report. If your
                                                         				  network uses Network Address Translation (NAT) and you are trying to access
                                                         				  serviceability reports inside the NAT, enter the IP address for the private
                                                         				  network that is associated with the NAT in the browser URL. If you are trying
                                                         				  to access the reports outside the NAT, enter the public IP address, and NAT
                                                         				  will accordingly translate/map to the private IP address. To view PDF
                                                         				  reports, you must install Acrobat Reader on your machine. To download Acrobat
                                                         				  Reader, click the link at the bottom of the Serviceability Reports Archive
                                                         				  window. |

| Tip | If you browsed
                                                         				  into Cisco Unified
                                                            					 Serviceability by using the node name, you must log in to Cisco Unified
                                                            					 Serviceability before you can view the report. If your
                                                         				  network uses Network Address Translation (NAT) and you are trying to access
                                                         				  serviceability reports inside the NAT, enter the IP address for the private
                                                         				  network that is associated with the NAT in the browser URL. If you are trying
                                                         				  to access the reports outside the NAT, enter the public IP address, and NAT
                                                         				  will accordingly translate/map to the private IP address. To view PDF
                                                         				  reports, you must install Acrobat Reader on your machine. To download Acrobat
                                                         				  Reader, click the link at the bottom of the Serviceability Reports Archive
                                                         				  window. |
|---|---|

| Step 1 | Select Tools > Service Activation . |
|---|---|
| Step 2 | Select the required server from the Server list box, and then select Go . |
| Step 3 | Navigate to the Performance and Monitoring services pane. |
| Step 4 | Check the Cisco Serviceability Reporter service checkbox, and then select Save . |
| Step 5 | Select Tools > Control Center - Feature Services . |
| Step 6 | Select the required server from the Server list box, and then select Go . |
| Step 7 | Navigate to the Performance and Monitoring services pane and locate the Cisco Serviceability Reporter. |
| Step 8 | Verify that the status of the Cisco Serviceability Reporter is Started and Activated. If the Cisco Serviceability Reporter
                                             is not running, select the Cisco Serviceability Reporter and select Start . |

| Step 1 | Select Tools > Serviceability Reports Archive . |
|---|---|
| Step 2 | Select the month and year for which you want to display reports in the Month-Year section. |
| Step 3 | Select the link that corresponds to the day for which reports were generated to view the required report. |
| Step 4 | Select the link of the report that you want to view to view a particular PDF report. The section in the Trace Filter Settings area that relates to devices is not relevant to IM and Presence . Tip If you opened Cisco Unified IM and Presence Serviceability by entering the server name in the browser, you must sign in to Cisco Unified IM and Presence Serviceability before you can view the report. | Tip | If you opened Cisco Unified IM and Presence Serviceability by entering the server name in the browser, you must sign in to Cisco Unified IM and Presence Serviceability before you can view the report. |
| Tip | If you opened Cisco Unified IM and Presence Serviceability by entering the server name in the browser, you must sign in to Cisco Unified IM and Presence Serviceability before you can view the report. |

| Tip | If you opened Cisco Unified IM and Presence Serviceability by entering the server name in the browser, you must sign in to Cisco Unified IM and Presence Serviceability before you can view the report. |
|---|---|

| Note | To access the Enterprise Parameters Configuration window, open Cisco Unified Communications Manager Administration and choose System > Enterprise
                                             				Parameters . The CDR File Time Interval parameter specifies the time interval for
                                       		  collecting CDR data. For example, if this value is set to 1, each file will
                                       		  contain 1 minute of CDR data (CDRs and CMRs, if enabled). The external billing
                                       		  server and CAR database will not receive the data in each file until the
                                       		  interval has expired, so consider how quickly you want access to the CDR data
                                       		  when you decide what interval to set for this parameter. For example, setting
                                       		  this parameter to 60 means that each file will contain 60 minutes worth of
                                       		  data, but that data will not be available until the 60-minute period has
                                       		  elapsed, and the records are written to the CAR database. and the CDR files are
                                       		  sent to the configured billing servers. The default value equals 1. The
                                       		  minimum value specifies 1, and the maximum value specifies 1440. The unit of
                                       		  measure for this required field represents a minute. |
|---|---|

| Note | Regardless of whether you enable the deletion of files based on the
                                       		  high water mark parameter, if disk usage exceeds the disk allocation that you
                                       		  configure, the CDR repository manager service deletes CDR and CMR files,
                                       		  beginning with the oldest files, until disk utilization falls below the high
                                       		  water mark. |
|---|---|

| Step 1 | Choose Tools > CDR
                                                				  Management . The CDR Management window displays. |
|---|---|
| Step 2 | Click the CDR Manager general parameter value that you want to
                                          			 change. |
| Step 3 | Enter the appropriate CDR Repository Manager general parameter settings. |
| Step 4 | Click Update . Tip At any time, you can click Set Default to specify the default values. After you set the
                                                         				  defaults, click Update to save the default values. | Tip | At any time, you can click Set Default to specify the default values. After you set the
                                                         				  defaults, click Update to save the default values. |
| Tip | At any time, you can click Set Default to specify the default values. After you set the
                                                         				  defaults, click Update to save the default values. |

| Tip | At any time, you can click Set Default to specify the default values. After you set the
                                                         				  defaults, click Update to save the default values. |
|---|---|

| Field | Description |
|---|---|
| Disk
                                          				  Allocation (MB) | Choose the number of megabytes that you want to allocate to CDR
                                          				  and CMR flat file storage. The
                                          				  default disk allocation and range vary depending on the size of the server hard
                                          				  drive. Note The maximum disk allocation space equals 3328 MB for a Unified Communications Manager server. If disk
                                                      					 usage exceeds the allocated maximum disk space for CDR files, the system
                                                      					 generates the CDRMaximumDiskSpaceExceeded alert and deletes all successfully
                                                      					 processed files (those delivered to billing servers and loaded to CAR). If disk
                                                      					 usage still exceeds the allocated disk space, the system deletes undelivered
                                                      					 files and files within the preservation duration, starting with the oldest,
                                                      					 until disk utilization falls below the high water mark. If you have
                                                      					 a large system and do not allocate enough disk space, the system may delete the
                                                      					 CDR and CMR files before the CAR Scheduler loads the files into the CAR
                                                      					 database. For example, if you configure the CAR Scheduler to run once a day and
                                                      					 you set the disk allocation to a value that is not large enough to hold the CDR
                                                      					 and CMR files that are generated in a day, the system will delete the files
                                                      					 before they are loaded into the CAR database. | Note | The maximum disk allocation space equals 3328 MB for a Unified Communications Manager server. If disk
                                                      					 usage exceeds the allocated maximum disk space for CDR files, the system
                                                      					 generates the CDRMaximumDiskSpaceExceeded alert and deletes all successfully
                                                      					 processed files (those delivered to billing servers and loaded to CAR). If disk
                                                      					 usage still exceeds the allocated disk space, the system deletes undelivered
                                                      					 files and files within the preservation duration, starting with the oldest,
                                                      					 until disk utilization falls below the high water mark. If you have
                                                      					 a large system and do not allocate enough disk space, the system may delete the
                                                      					 CDR and CMR files before the CAR Scheduler loads the files into the CAR
                                                      					 database. For example, if you configure the CAR Scheduler to run once a day and
                                                      					 you set the disk allocation to a value that is not large enough to hold the CDR
                                                      					 and CMR files that are generated in a day, the system will delete the files
                                                      					 before they are loaded into the CAR database. |
| Note | The maximum disk allocation space equals 3328 MB for a Unified Communications Manager server. If disk
                                                      					 usage exceeds the allocated maximum disk space for CDR files, the system
                                                      					 generates the CDRMaximumDiskSpaceExceeded alert and deletes all successfully
                                                      					 processed files (those delivered to billing servers and loaded to CAR). If disk
                                                      					 usage still exceeds the allocated disk space, the system deletes undelivered
                                                      					 files and files within the preservation duration, starting with the oldest,
                                                      					 until disk utilization falls below the high water mark. If you have
                                                      					 a large system and do not allocate enough disk space, the system may delete the
                                                      					 CDR and CMR files before the CAR Scheduler loads the files into the CAR
                                                      					 database. For example, if you configure the CAR Scheduler to run once a day and
                                                      					 you set the disk allocation to a value that is not large enough to hold the CDR
                                                      					 and CMR files that are generated in a day, the system will delete the files
                                                      					 before they are loaded into the CAR database. |
| High
                                          				  Water Mark (%) | This field specifies the maximum percentage of the allocated disk space for CDR and CMR files. For example, if you choose
                                          2000 megabytes from the Disk Allocation field and 80% from the High Water Mark (%) field, the high water mark equals 1600
                                          megabytes. In addition to the high water mark percentage, the number of CDRs in the CAR database cannot exceed two million
                                          records for a Unified Communications Manager server. When
                                          				  the disk usage exceeds the percentage that you specify, or the total number of
                                          				  CDRs is exceeded, and the Disable CDR/CMR Files Deletion Based on HWM check box
                                          				  is unchecked, the system automatically purges all successfully processed CDR
                                          				  and CMR files (those delivered to billing servers and loaded to CAR) beginning
                                          				  with the oldest files to reduce disk usage to the amount that you specify in
                                          				  the Low Water Mark (%) drop-down list box. If
                                          				  the disk usage still exceeds the low water mark or high water mark, the system
                                          				  does not delete any undelivered or unloaded files, unless the disk usage
                                          				  exceeds the disk allocation. If
                                          				  you check the Disable CDR/CMR Files Deletion Based on HWM check box, the system
                                          				  does not delete CDRs and CMRs based on the percentage that you specify in this
                                          				  field. Note If CDR disk
                                                      					 space exceeds the high water mark, the system generates the CDRHWMExceeded
                                                      					 alert. | Note | If CDR disk
                                                      					 space exceeds the high water mark, the system generates the CDRHWMExceeded
                                                      					 alert. |
| Note | If CDR disk
                                                      					 space exceeds the high water mark, the system generates the CDRHWMExceeded
                                                      					 alert. |
| Low
                                          				  Water Mark (%) | This
                                          				  field specifies the percentage of disk space that is allocated to CDR and CMR
                                          				  files that is always available for use. For example, if you choose 2000
                                          				  megabytes from the Disk Allocation field and 40% from the Low Water Mark (%)
                                          				  field, the low water mark equals 800 megabytes. |
| CDR /
                                          				  CMR Files Preservation Duration (Days) | Choose the number of days that you want to retain CDR and CMR
                                          				  files. The CDR Repository Manager deletes files that fall outside the
                                          				  preservation window. Note If you
                                                      					 continuously receive the CDRMaximumDiskSpaceExceeded alarm, you either must
                                                      					 increase the disk allocation or lower the number of preservation days. | Note | If you
                                                      					 continuously receive the CDRMaximumDiskSpaceExceeded alarm, you either must
                                                      					 increase the disk allocation or lower the number of preservation days. |
| Note | If you
                                                      					 continuously receive the CDRMaximumDiskSpaceExceeded alarm, you either must
                                                      					 increase the disk allocation or lower the number of preservation days. |
| Disable CDR/CMR Files Deletion Based on HWM | Note Regardless
                                                      					 of whether you enable the deletion of files based on the high-water mark
                                                      					 parameter, if disk usage exceeds the disk allocation that you configure, the
                                                      					 maximum database size, or the maximum number of records for your installation,
                                                      					 the CDR repository manager service deletes CDR and CMR files, beginning with
                                                      					 the oldest files, until disk utilization falls below the high water mark. If
                                          				  you do not want to delete CDRs and CMRs even if disk usage exceeds the
                                          				  percentage that you specify in the High Water Mark (%) field, check this check
                                          				  box. By default, this check box remains unchecked, so the system deletes CDRs
                                          				  and CMRs if disk usage exceeds the high water mark. | Note | Regardless
                                                      					 of whether you enable the deletion of files based on the high-water mark
                                                      					 parameter, if disk usage exceeds the disk allocation that you configure, the
                                                      					 maximum database size, or the maximum number of records for your installation,
                                                      					 the CDR repository manager service deletes CDR and CMR files, beginning with
                                                      					 the oldest files, until disk utilization falls below the high water mark. |
| Note | Regardless
                                                      					 of whether you enable the deletion of files based on the high-water mark
                                                      					 parameter, if disk usage exceeds the disk allocation that you configure, the
                                                      					 maximum database size, or the maximum number of records for your installation,
                                                      					 the CDR repository manager service deletes CDR and CMR files, beginning with
                                                      					 the oldest files, until disk utilization falls below the high water mark. |
| CDR
                                          				  Repository Manager Host Name | This
                                          				  field lists the hostname of the CDR repository manager server. |
| CDR
                                          				  Repository Manager Host Address | This
                                          				  field lists the IP address of the CDR repository manager server. |

| Note | The maximum disk allocation space equals 3328 MB for a Unified Communications Manager server. If disk
                                                      					 usage exceeds the allocated maximum disk space for CDR files, the system
                                                      					 generates the CDRMaximumDiskSpaceExceeded alert and deletes all successfully
                                                      					 processed files (those delivered to billing servers and loaded to CAR). If disk
                                                      					 usage still exceeds the allocated disk space, the system deletes undelivered
                                                      					 files and files within the preservation duration, starting with the oldest,
                                                      					 until disk utilization falls below the high water mark. If you have
                                                      					 a large system and do not allocate enough disk space, the system may delete the
                                                      					 CDR and CMR files before the CAR Scheduler loads the files into the CAR
                                                      					 database. For example, if you configure the CAR Scheduler to run once a day and
                                                      					 you set the disk allocation to a value that is not large enough to hold the CDR
                                                      					 and CMR files that are generated in a day, the system will delete the files
                                                      					 before they are loaded into the CAR database. |
|---|---|

| Note | If CDR disk
                                                      					 space exceeds the high water mark, the system generates the CDRHWMExceeded
                                                      					 alert. |
|---|---|

| Note | If you
                                                      					 continuously receive the CDRMaximumDiskSpaceExceeded alarm, you either must
                                                      					 increase the disk allocation or lower the number of preservation days. |
|---|---|

| Note | Regardless
                                                      					 of whether you enable the deletion of files based on the high-water mark
                                                      					 parameter, if disk usage exceeds the disk allocation that you configure, the
                                                      					 maximum database size, or the maximum number of records for your installation,
                                                      					 the CDR repository manager service deletes CDR and CMR files, beginning with
                                                      					 the oldest files, until disk utilization falls below the high water mark. |
|---|---|

| Note | Make sure that the backup SFTP Server supports one of these CBC ciphers to communicate with Unified Communications Manager. |
|---|---|

| Note | Make sure that the backup SFTP Server supports one of these CTR ciphers to communicate with Unified Communications Manager. |
|---|---|

| Step 1 | Choose Tools > CDR Management
                                                				  Configuration . The CDR Management Configuration window displays. |
|---|---|
| Step 2 | Perform one of the following tasks: To add a new application billing server, click the Add New button. To update an existing application billing server, click the
                                                   				  server hostname/IP address. |
| Step 3 | Enter the application billing server parameter settings. |
| Step 4 | Click Add or Update . |

| Field | Description |
|---|---|
| Host Name/IP Address | Enter the hostname or IP address of the application billing server to which you want to send CDRs. If you change the value in this field, a prompt asks whether you want to send the undelivered files to the new destination. Perform one of the following tasks: To deliver the files to the new server, click Yes . To change the server hostname/IP address without sending undelivered files, click No . The CDR Management service marks the CDR and CMR files as delivered. |
| User Name | Enter the username of the application billing server. |
| Protocol | Choose the protocol, either FTP or SFTP, that you want to use to send the CDR files to the configured billing servers. |
| Directory Path | Enter the directory path on the application billing server to which you want to send the CDRs. You should end the path that
                                          you specify with a "/" or "\" , depending on the operating system that is running on the application billing server. Note Make sure the FTP user has write permission to the directory. | Note | Make sure the FTP user has write permission to the directory. |
| Note | Make sure the FTP user has write permission to the directory. |
| Password | Enter the password that is used to access the application billing server. |
| Resend on Failure | When you check the Resend on Failure box, this option informs CDRM to send outdated CDR and CMR files to the billing server
                                          after the FTP or SFTP connection is restored. When the box is checked, the Resend on Failure flag is set to True. When the
                                          box is not checked, the Resend on Failure flag is set to False. There are several different scenarios that can occur. When the billing server Resend on Failure flag is set to True, all CDR
                                          files get moved to the billing server. When the Resend On Failure flag is set to False, CDR files that get generated during
                                          shutdown of the billing server get moved to the processed folder, but do not get moved to the billing server. When the Resend
                                          on Failure flag gets set to True at the beginning, and then gets changed several times, the result is that the CDR files get
                                          moved to the billing server whenever the Resend on Failure box gets checked. |
| Generate New Key | Click on the Reset button to generate new keys and reset the connection to the SFTP server. |

| Note | Make sure the FTP user has write permission to the directory. |
|---|---|

| Step 1 | Choose Tools > CDR
                                                				  Management . The CDR Management Configuration window displays. |
|---|---|
| Step 2 | Check the check box next to the application billing server that
                                          			 you want to delete and click Delete Selected . A message displays that indicates that if you delete this server,
                                             				any CDR or CMR files that have not been sent to this server will not be
                                             				delivered to this server and will be treated as successfully delivered files. Tip When you delete a server, the system does not generate the
                                                         				  CDRFileDeliveryFailed alert for the files that are not sent to that server. | Tip | When you delete a server, the system does not generate the
                                                         				  CDRFileDeliveryFailed alert for the files that are not sent to that server. |
| Tip | When you delete a server, the system does not generate the
                                                         				  CDRFileDeliveryFailed alert for the files that are not sent to that server. |
| Step 3 | To complete the deletion, click OK . |

| Tip | When you delete a server, the system does not generate the
                                                         				  CDRFileDeliveryFailed alert for the files that are not sent to that server. |
|---|---|

| Step 1 | Choose Tools > CDR Management . The CDR Management Configuration window displays. |
|---|---|
| Step 2 | Under Billing Application Server Parameters , locate your billing server. |
| Step 3 | Click Reset to generate a new key that corresponds to your billing server. |

| Step 1 | In Cisco Unified Serviceability, choose Tools > Locations > Topology . The Locations Topology window appears. |
|---|---|
| Step 2 | From the Find Locations Where Location Name drop-down box, choose the filter criteria. |
| Step 3 | Enter the search string in the Find Locations Where Location Name field and then click Find . Note The Find Locations Where Location Name field is not casesensitive. The list of locations is displayed for the chosen filter criteria. | Note | The Find Locations Where Location Name field is not casesensitive. |
| Note | The Find Locations Where Location Name field is not casesensitive. |
| Step 4 | In the list, click to expand any location to view its intralocation details and link details. The intralocation details include audio, video, and immersive bandwidth whereas the link details contain the details of the
                                                link connecting two locations such as its weight, audio, video and immersive bandwidth. Tip If the list of locations is long, it may run into multiple pages. To view another page, click the appropriate navigation button
                                                            at the bottom of the Locations Topology window or enter a page number in the Page field. To change the number of locations
                                                            that display in the window, choose a different value from the Rows Per Page drop-down box. Tip If a location is highlighted by a Caution symbol, this indicates a discrepancy. To view the details of this discrepancy, click View Assertion Details link. | Tip | If the list of locations is long, it may run into multiple pages. To view another page, click the appropriate navigation button
                                                            at the bottom of the Locations Topology window or enter a page number in the Page field. To change the number of locations
                                                            that display in the window, choose a different value from the Rows Per Page drop-down box. | Tip | If a location is highlighted by a Caution symbol, this indicates a discrepancy. To view the details of this discrepancy, click View Assertion Details link. |
| Tip | If the list of locations is long, it may run into multiple pages. To view another page, click the appropriate navigation button
                                                            at the bottom of the Locations Topology window or enter a page number in the Page field. To change the number of locations
                                                            that display in the window, choose a different value from the Rows Per Page drop-down box. |
| Tip | If a location is highlighted by a Caution symbol, this indicates a discrepancy. To view the details of this discrepancy, click View Assertion Details link. |
| Step 5 | To view the assertion details of any location, click View Assertion Details link at the bottom of the expanded details section. The Assertion Details window appears. |
| Step 6 | To return to the Locations Topology window, click Close. Note To download the locations topology data in XML format, click Download Topology at the bottom of the Locations Topology window or Download Topology icon in the toolbar at the top. For more information about the topology data in XML format, see the Cisco Unified Communications Manager XML Developers Guide . | Note | To download the locations topology data in XML format, click Download Topology at the bottom of the Locations Topology window or Download Topology icon in the toolbar at the top. |
| Note | To download the locations topology data in XML format, click Download Topology at the bottom of the Locations Topology window or Download Topology icon in the toolbar at the top. |

| Note | The Find Locations Where Location Name field is not casesensitive. |
|---|---|

| Tip | If the list of locations is long, it may run into multiple pages. To view another page, click the appropriate navigation button
                                                            at the bottom of the Locations Topology window or enter a page number in the Page field. To change the number of locations
                                                            that display in the window, choose a different value from the Rows Per Page drop-down box. |
|---|---|

| Tip | If a location is highlighted by a Caution symbol, this indicates a discrepancy. To view the details of this discrepancy, click View Assertion Details link. |
|---|---|

| Note | To download the locations topology data in XML format, click Download Topology at the bottom of the Locations Topology window or Download Topology icon in the toolbar at the top. |
|---|---|

| Step 1 | Select Tools > Locations > Locations Topology . |
|---|---|
| Step 2 | Click the View Assertion Details link in the Locations Topology window. |

| Step 1 | In Cisco Unified Serviceability, choose Tools > Locations > Discrepancy . The Location Discrepancy window appears. |
|---|---|
| Step 2 | The list of link configuration discrepancies and intralocation configuration discrepancies is displayed. Note The Link Configuration Discrepancy section lists only those link names where discrepancy has been detected. Link names are
                                                            listed in the format <Location Name 1> <--> <Location Name 2> . The Intralocation Configuration Discrepancy section lists only those location names where such discrepancy has been detected.
                                                            The elements in the list are sorted in lexical order. If no discrepancies are found, the following status message is displayed: No discrepancies found | Note | The Link Configuration Discrepancy section lists only those link names where discrepancy has been detected. Link names are
                                                            listed in the format <Location Name 1> <--> <Location Name 2> . The Intralocation Configuration Discrepancy section lists only those location names where such discrepancy has been detected.
                                                            The elements in the list are sorted in lexical order. |
| Note | The Link Configuration Discrepancy section lists only those link names where discrepancy has been detected. Link names are
                                                            listed in the format <Location Name 1> <--> <Location Name 2> . The Intralocation Configuration Discrepancy section lists only those location names where such discrepancy has been detected.
                                                            The elements in the list are sorted in lexical order. |
| Step 3 | In the list, click on a link name or location name to expand and view its configuration details as asserted by different clusters,
                                             in a tabular view. The bottom row displays the effective values considered for audio, video, and immersive bandwidth pools and weight (in the
                                                case of links). The values that do not match with the effective values are highlighted in red. Note The Effective Value is the least of the values in a particular column. For example, the Effective Value of audio bandwidth
                                                            is the minimum value in the Audio Bandwidth column. | Note | The Effective Value is the least of the values in a particular column. For example, the Effective Value of audio bandwidth
                                                            is the minimum value in the Audio Bandwidth column. |
| Note | The Effective Value is the least of the values in a particular column. For example, the Effective Value of audio bandwidth
                                                            is the minimum value in the Audio Bandwidth column. |

| Note | The Link Configuration Discrepancy section lists only those link names where discrepancy has been detected. Link names are
                                                            listed in the format <Location Name 1> <--> <Location Name 2> . The Intralocation Configuration Discrepancy section lists only those location names where such discrepancy has been detected.
                                                            The elements in the list are sorted in lexical order. |
|---|---|

| Note | The Effective Value is the least of the values in a particular column. For example, the Effective Value of audio bandwidth
                                                            is the minimum value in the Audio Bandwidth column. |
|---|---|

| Note | The Available bandwidth values displayed in the report are the value at the time of viewing the Effective Path. You can view
                                             the real-time values in the Cisco Unified Real-Time Monitoring Tool. |
|---|---|

| Step 1 | In Cisco Unified Serviceability, choose Tools > Locations > Effective Path . The Effective Path window appears. |
|---|---|
| Step 2 | From the Location drop-down boxes, select any two locations between which effective path is required and then click Find. Alternatively, start typing the location name in the input box to shortlist the matching location names and then click Find. The effective path details, which include the Quick Path Overview and Detailed Path View sections, are displayed. If there
                                                is no path between the two selected locations, the following status message is displayed: No path exists between <From_Location> and <To_Location>. |

| Note | The Disconnected Groups screen displays and compares only
                                             			 disconnected groups of locations. For information on connecting locations, see
                                             			 topics related to location configuration in Administration Guide for Cisco Unified Communications
                                                				Manager . |
|---|---|

| In Cisco Unified Serviceability, choose Tools > Locations > Disconnected Groups . The Disconnected Groups screen appears. |
|---|

| Setting | Description |
|---|---|
| List of Disconnected Groups |
| Select | Check this box to select a disconnected group to be compared with another disconnected group. Caution You can select only two groups for comparison. | Caution | You can select only two groups for comparison. |
| Caution | You can select only two groups for comparison. |
| Group ID | Auto-generated unique identification number of the selected group is displayed here. |
| Description | The names of the first and last location (as per the alphabetical order) in the group are displayed here. Note If a disconnected group has only one node, only the name of that node is displayed here. | Note | If a disconnected group has only one node, only the name of that node is displayed here. |
| Note | If a disconnected group has only one node, only the name of that node is displayed here. |
| No of Locations | The number of locations in a group is displayed here. |
| Compare Selected Groups | Click this button to display and compare the selected groups. After you click this button, the details that pertain to the
                                                selected groups are displayed. For every group you select, names of the locations that are part of that group and the corresponding clusters that assert
                                                a location are displayed. See Comparison view for the selected groups below. |
| Comparison view for the selected groups |
| Location Name | The names of all the locations that are part of a group are listed in this column. |
| Asserted by Cluster | The names of all the clusters that assert a particular location are listed  in this column. |

| Caution | You can select only two groups for comparison. |
|---|---|

| Note | If a disconnected group has only one node, only the name of that node is displayed here. |
|---|---|

| Note | The List of Disconnected Groups can be sorted by any column. By default, the groups are sorted by the No. of Locations column. |
|---|---|