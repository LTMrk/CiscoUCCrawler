---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--24fd246fbe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting_user_guide-1251/ucce_b_cisco-unified-contact-center-enterprise-125_chapter_010000.html
retrieved_at: 2026-08-22T00:02:01.614190+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release12.5(1)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release12.5(1)

Updated: February 4, 2020

Chapter: License Consumption Report

## Chapter: License Consumption Report

# License Consumption Report

## License
                        	 Consumption Report

The License
                              		  Consumption report displays the following for a specific interval:

The total of the maximum agents logged in.

The maximum number of the Enterprise agents logged in.

The maximum number of the Unified CCE agents logged in.

The maximum numbers of the Dialer ports and VRU ports consumed.

You can use the License Consumption report to view this data in a quarterhourly, halfhourly, daily, hourly, monthly, quarterly,
                              and weekly format.

Query: This report data
                              		  is built from a Store Procedure.

Views : This report has a grid view and a line chart view. The line chart view displays license usage for all the licensable items
                              over time against a common scale.

The License Consumption report provides the Suppress Spike feature that enables you to suppress the steep spikes in the report.
                                          This report uses the standard 95 percentile algorithm to ensure that the unusually high spikes, which are beyond the 95 percentile
                                          range, are excluded. The report generated using the Suppress Spike feature is indicative only and should not be considered
                                          for determining the peak license consumption, for agent licensing purposes.

Grouping: There is no
                              		  grouping supported for this report. It is sorted by date and time.

Value List: Frequency

Database Schema Tables from
                                 			 which Data is Retrieved: System_Capacity_Interval

While importing the License Consumption report, do the following:

In the Data Source for ReportDefinition field, select UCCE Historical .

In the Datasource for ValueList field, select CUIC .

### Current Fields in
                           	 License Consumption Grid View

The Current fields are the fields that appear by default in the grid view for this report.

The current fields
                                 		  are listed in the following table in the order (left to right) in which they
                                 		  appear by default in the report.

Column (Field)

Description

System Date Time

The date and time of the record of the selected row in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format.

Max Agents Logged In

Total Agents

The total of maximum Enterprise and Unified CCE agents logged in at the specified interval.

Derived from: System_Capacity_Interval.MaxagentsLoggedin

Enterprise Agents

The maximum number of the Enterprise agents logged in at the specified interval.

Derived from the formula:

(System_Capacity_Interval.MaxagentsLoggedin) - (System_Capacity_Interval.MaxICMAgents)

Unified CCE Agents

The maximum number of the Unified CCE agents logged in at the specified interval.

Derived from: System_Capacity_Interval.MaxICMAgents

Column (Field)

Description

Max VRU Ports Consumed

The maximum number of the VRU ports used at the specified interval.

Derived from: System_Capacity_Interval.maxvruports

Max Dialer Ports Consumed

The maximum number of the Dialer ports used at the specified interval.

Derived from: System_Capacity_Interval.FutureUseInt2

Report Summary: The summary line displays the maximum value in the corresponding
                                 		  column for each licensable item.

### License Consumption Graph View

The License Consumption Graph view displays license usage for all the licensable items over time against a common scale.

The Current fields are the fields that appear by default in the line chart view for this report.

The current fields are listed in the following table:

Columns (Fields)

Description

Licensable Items

Licensable items on the Y axis. The graph shows the maximum number of agents, such as ICM Agents, Enterprise Agents, or Total
                                             Agents logged in, and Maximum Dialer Ports Consumed and Maximum VRU Ports Consumed.

System Date and Time

The system date and time on the X axis.

### Flex License Consumption View

The Flex License Consumption view shows Flex Premium and Flex Standard license usage. The view can be filtered in the intervals
                                 of QuarterHourly, HalfHourly, Hourly, Daily, Weekly, Monthly, and Quarterly.

#### Fields in the Flex License Consumption View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order in which they appear in the stock template.

Columns (Fields)

Description

System Date Time

The system date and time.

Flex Premium Agents

The maximum number of Premium Agents logged in.

Flex Std Agents

The maximum number of Standard Agents logged in.

Max VRU Ports Consumed

The maximum number of VRU ports consumed.

### Perpetual License Consumption View

The Perpetual License Consumption view shows the Perpetual license usage. The view can be filtered in the intervals of QuarterHourly,
                                 HalfHourly, Hourly, Daily, Weekly, Monthly, and Quarterly.

#### Fields in the Perpetual License Consumption View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order in which they appear in the stock template.

Columns (Fields)

Description

System Date Time

The system date and time.

Perpetual Premium Agents

The maximum number of Perpetual Premium Agents logged in.

Max Dialer Ports Consumed

The maximum number of Dialer ports consumed.

Max VRU Ports Consumed

The maximum number of VRU ports consumed.

### Current Fields in
                           	 License Consumption Grid View

The Current fields are the fields that appear by default in the grid view for this report.

The current fields
                                 		  are listed in the following table in the order (left to right) in which they
                                 		  appear by default in the report.

Column (Field)

Description

System Date Time

The date and time of the record of the selected row in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format.

Max Agents Logged In

Total Agents

The total of maximum Enterprise and Unified CCE agents logged in at the specified interval.

Derived from: System_Capacity_Interval.MaxagentsLoggedin

Enterprise Agents

The maximum number of the Enterprise agents logged in at the specified interval.

Derived from the formula:

(System_Capacity_Interval.MaxagentsLoggedin) - (System_Capacity_Interval.MaxICMAgents)

Unified CCE Agents

The maximum number of the Unified CCE agents logged in at the specified interval.

Derived from: System_Capacity_Interval.MaxICMAgents

Column (Field)

Description

Max VRU Ports Consumed

The maximum number of the VRU ports used at the specified interval.

Derived from: System_Capacity_Interval.maxvruports

Max Dialer Ports Consumed

The maximum number of the Dialer ports used at the specified interval.

Derived from: System_Capacity_Interval.FutureUseInt2

Report Summary: The summary line displays the maximum value in the corresponding
                                 		  column for each licensable item.

### License Consumption Graph View

The License Consumption Graph view displays license usage for all the licensable items over time against a common scale.

The Current fields are the fields that appear by default in the line chart view for this report.

The current fields are listed in the following table:

Columns (Fields)

Description

Licensable Items

Licensable items on the Y axis. The graph shows the maximum number of agents, such as ICM Agents, Enterprise Agents, or Total
                                             Agents logged in, and Maximum Dialer Ports Consumed and Maximum VRU Ports Consumed.

System Date and Time

The system date and time on the X axis.

### Flex License Consumption View

The Flex License Consumption view shows Flex Premium and Flex Standard license usage. The view can be filtered in the intervals
                                 of QuarterHourly, HalfHourly, Hourly, Daily, Weekly, Monthly, and Quarterly.

#### Fields in the Flex License Consumption View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order in which they appear in the stock template.

Columns (Fields)

Description

System Date Time

The system date and time.

Flex Premium Agents

The maximum number of Premium Agents logged in.

Flex Std Agents

The maximum number of Standard Agents logged in.

Max VRU Ports Consumed

The maximum number of VRU ports consumed.

### Perpetual License Consumption View

The Perpetual License Consumption view shows the Perpetual license usage. The view can be filtered in the intervals of QuarterHourly,
                                 HalfHourly, Hourly, Daily, Weekly, Monthly, and Quarterly.

#### Fields in the Perpetual License Consumption View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order in which they appear in the stock template.

Columns (Fields)

Description

System Date Time

The system date and time.

Perpetual Premium Agents

The maximum number of Perpetual Premium Agents logged in.

Max Dialer Ports Consumed

The maximum number of Dialer ports consumed.

Max VRU Ports Consumed

The maximum number of VRU ports consumed.

| Note | The License Consumption report provides the Suppress Spike feature that enables you to suppress the steep spikes in the report.
                                          This report uses the standard 95 percentile algorithm to ensure that the unusually high spikes, which are beyond the 95 percentile
                                          range, are excluded. The report generated using the Suppress Spike feature is indicative only and should not be considered
                                          for determining the peak license consumption, for agent licensing purposes. |
|---|---|

| Note | While importing the License Consumption report, do the following: In the Data Source for ReportDefinition field, select UCCE Historical . In the Datasource for ValueList field, select CUIC . |
|---|---|

| Column (Field) | Description |
|---|---|
| System Date Time | The date and time of the record of the selected row in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format. |
| Max Agents Logged In |
| Total Agents | The total of maximum Enterprise and Unified CCE agents logged in at the specified interval. Derived from: System_Capacity_Interval.MaxagentsLoggedin |
| Enterprise Agents | The maximum number of the Enterprise agents logged in at the specified interval. Derived from the formula: (System_Capacity_Interval.MaxagentsLoggedin) - (System_Capacity_Interval.MaxICMAgents) |
| Unified CCE Agents | The maximum number of the Unified CCE agents logged in at the specified interval. Derived from: System_Capacity_Interval.MaxICMAgents |
| Column (Field) | Description |
| Max VRU Ports Consumed | The maximum number of the VRU ports used at the specified interval. Derived from: System_Capacity_Interval.maxvruports |
| Max Dialer Ports Consumed | The maximum number of the Dialer ports used at the specified interval. Derived from: System_Capacity_Interval.FutureUseInt2 |

| Columns (Fields) | Description |
|---|---|
| Licensable Items | Licensable items on the Y axis. The graph shows the maximum number of agents, such as ICM Agents, Enterprise Agents, or Total
                                             Agents logged in, and Maximum Dialer Ports Consumed and Maximum VRU Ports Consumed. |
| System Date and Time | The system date and time on the X axis. |

| Columns (Fields) | Description |
|---|---|
| System Date Time | The system date and time. |
| Flex Premium Agents | The maximum number of Premium Agents logged in. |
| Flex Std Agents | The maximum number of Standard Agents logged in. |
| Max VRU Ports Consumed | The maximum number of VRU ports consumed. |

| Columns (Fields) | Description |
|---|---|
| System Date Time | The system date and time. |
| Perpetual Premium Agents | The maximum number of Perpetual Premium Agents logged in. |
| Max Dialer Ports Consumed | The maximum number of Dialer ports consumed. |
| Max VRU Ports Consumed | The maximum number of VRU ports consumed. |

| Column (Field) | Description |
|---|---|
| System Date Time | The date and time of the record of the selected row in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format. |
| Max Agents Logged In |
| Total Agents | The total of maximum Enterprise and Unified CCE agents logged in at the specified interval. Derived from: System_Capacity_Interval.MaxagentsLoggedin |
| Enterprise Agents | The maximum number of the Enterprise agents logged in at the specified interval. Derived from the formula: (System_Capacity_Interval.MaxagentsLoggedin) - (System_Capacity_Interval.MaxICMAgents) |
| Unified CCE Agents | The maximum number of the Unified CCE agents logged in at the specified interval. Derived from: System_Capacity_Interval.MaxICMAgents |
| Column (Field) | Description |
| Max VRU Ports Consumed | The maximum number of the VRU ports used at the specified interval. Derived from: System_Capacity_Interval.maxvruports |
| Max Dialer Ports Consumed | The maximum number of the Dialer ports used at the specified interval. Derived from: System_Capacity_Interval.FutureUseInt2 |

| Columns (Fields) | Description |
|---|---|
| Licensable Items | Licensable items on the Y axis. The graph shows the maximum number of agents, such as ICM Agents, Enterprise Agents, or Total
                                             Agents logged in, and Maximum Dialer Ports Consumed and Maximum VRU Ports Consumed. |
| System Date and Time | The system date and time on the X axis. |

| Columns (Fields) | Description |
|---|---|
| System Date Time | The system date and time. |
| Flex Premium Agents | The maximum number of Premium Agents logged in. |
| Flex Std Agents | The maximum number of Standard Agents logged in. |
| Max VRU Ports Consumed | The maximum number of VRU ports consumed. |

| Columns (Fields) | Description |
|---|---|
| System Date Time | The system date and time. |
| Perpetual Premium Agents | The maximum number of Perpetual Premium Agents logged in. |
| Max Dialer Ports Consumed | The maximum number of Dialer ports consumed. |
| Max VRU Ports Consumed | The maximum number of VRU ports consumed. |