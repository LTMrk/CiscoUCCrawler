---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--1df0426f58
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_010001.html
retrieved_at: 2026-08-21T01:34:33.568561+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: System Reports Results

## Chapter: System Reports Results

# System Reports Results

This chapter describes report output information for each CAR
                        		system report.

## QoS Detail Report Results

The results of the QoS Detail report include the following
                              		  fields. See the following table.

Field

Description

Orig. Time

The time that the call was placed, in 24-hour,
                                          					 minute, and second format.

Term. Time

The time that the call disconnected, in 24-hour,
                                          					 minute, and second format.

Duration(s)

The time, in seconds, that the call was connected.

Orig.

The originating number from which the call was
                                          					 placed.

Dest.

The destination number to which the call was
                                          					 directed.

Call Classification - Call categories specify
                                          					 classes.

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan .

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network that go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911.

Orig. Codec

The codec that the originating device uses.

Dest. Codec

The codec that the destination device uses.

Orig. Device

The name of the device that placed the call.

Dest. Device

The name of the device that received the call.

Orig. QoS

The voice quality that the device that placed the
                                          					 call experienced.

Dest. QoS

The voice quality that the device that received the
                                          					 call experienced.

The following figure displays sample output of the QoS Detail
                              		  report in PDF format.

## QoS Summary Report Results

The QoS Summary report includes the following fields. See the
                              		  table. If you select PDF format for the report output, the report shows a pie
                              		  chart that displays the QoS of the total number of calls.

Field

Description

Quality of Service

The quality of service of the calls.

Call Legs

Number of call legs with the quality of service that
                                          					 the Quality of Service field specified.

Figure 1 displays sample output of the QoS Summary Report in PDF format.

## QoS by Gateways Report Results

The QoS by Gateways report provides the following
                              		  information. See the table.

Field

Description

Time/Day

Indicates the cumulative hours of the day(s), the
                                          					 days of the week, or the days of the month for the selected date range.

% of Call Legs

Displays the percentage of calls for each gateway
                                          					 for the hours of the day, the days of the week, or the days of the month for
                                          					 the selected date range.

Figure 1 displays sample output of the QoS by Gateways report in PDF format.

## QoS by Call Types Report Results

The QoS by Call Types report provides the following
                              		  information. See the table.

Field

Description

Time/Day

The cumulative hours of the day(s), the days of the
                                          					 week, or the days of the month for the selected date range.

% of Call Legs

The percentage of calls for each gateway for the
                                          					 hours of the day, the days of the week, or the days of the month for the
                                          					 selected date range.

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network that go out through the PSTN.

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan .

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911.

Figure 1 displays sample output of the QoS by Call Types report in PDF format.

## Traffic Summary Report Results

The Traffic Summary and Traffic Summary by Phone Number
                              		  reports contain the same information and include some or all the following
                              		  fields. See the table. A separate line displays under the report title for the
                              		  Busy Hour Call Completion (BHCC) number for that day.

Field

Description

Time/Day

The cumulative hours of the day(s), the days of the
                                          					 week, or the days of the month for the selected date range.

Average Number of Calls

The percentage of calls for each gateway for the
                                          					 hours of the day, the days of the week, or the days of the month for the
                                          					 selected date range.

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan .

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network that go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911.

Total

The total number of calls for each hour or day.

Figure 1 and Figure 2 display sample output of the Traffic Summary and the Traffic Summary by Phone
                              		  Number report results in PDF format.

## Authorization Code Name Call Details Report Results

This report shows the usage of specific authorization code
                              		  names. For security purposes, the authorization code name (description)
                              		  displays and not the authorization code. The Authorization Code Name Call
                              		  Details report includes the following fields (see the table).

Field

Description

Orig.

The originating number from which the call was
                                          					 placed.

Dest.

The destination number to which the call was
                                          					 directed.

Orig. Date Time

The date and time that the call originated.

Duration (sec)

The time, in seconds, that the call connected.

Call Classification

The type of call (internal, incoming, on so on.)

Authorization Level

The authorization level for calls for each chosen
                                          					 authorization code name.

Figure 1 displays sample output of the Authorization Code Name Call Details report in
                              		  PDF format.

## Authorization Level Call Details Report Results

This report shows the usage of specific authorization
                              		  levels. The Authorization Level Call Details report includes the following
                              		  fields (see the table).

Field

Description

Orig.

The originating number from which the call was
                                          					 placed.

Dest.

The destination number to which the call was
                                          					 directed.

Orig. Date Time

The date and time that the call originated.

Duration (sec)

The time, in seconds, that the call connected.

Call Classification

The type of call (internal, incoming, and so on.)

Authorization Code Name

The authorization code name for each authorization
                                          					 level that you chose.

Figure 1 displays sample output of the Authorization Level Call Details report in PDF
                              		  format.

## Client Matter Code Details Report Results

The report shows the usage of specific client matter codes.
                              		  The Client Matter Code Details report includes the following fields (see the
                              		  following table).

Field

Description

Orig.

The originating number from which the call was
                                          					 placed.

Dest.

The destination number to which the call was
                                          					 directed.

Orig. Date Time

The date and time that the call originated.

Duration (sec)

The time, in seconds, that the call connected.

Call Classification

The type of call (internal, incoming, and so on).

Figure 1 displays sample output of the Client Matter Code Details report in PDF format.

## Malicious Call Details Report Results

The Malicious Call Details report provides information about
                              		  malicious calls. The report provides the following fields. See the table.

Field

Description

Orig. Time

Time at which the malicious call originated.

Term. Time

Time at which the malicious call terminated.

Duration

Total time of malicious call in seconds.

Orig.

Originating DN.

Dest.

Destination DN.

Orig. Device

Name of the originating device.

Dest. Device

Name of the destination device.

Call Classification

Classification of the malicious call.

Figure 1 displays sample output of the Malicious Calls Detail report in PDF format.

## Precedence Call Summary Report Results

The Precedence Call Summary report provides information
                              		  about calls based on precedence levels. The report displays the call summary
                              		  for the precedence values in the form of a bar chart on an "Hour of Day," "Day of Week," or "Day of Month" basis for each precedence level that you choose. If
                              		  you choose to display the report in PDF format, two tables, one reflecting the
                              		  bar chart, and the other listing the "Number of Calls" and "Percentage" for each precedence level that was chosen, display in
                              		  the report. See the table.

Field

Description

Time/Day

Indicates the cumulative hours of the day(s), the
                                          					 days of the week, or the days of the month for the selected date range.

Call Legs

Number of calls for each precedence level by
                                          					 time/day.

Precedence Level

Precedence level value of the call.

No. of Call Legs

Number of call legs per each precedence level.

Percentage

Percentage of calls per each precedence level.

Figure 1 displays sample output of the Precedence Call Summary by Hour of Day report in
                              		  PDF format.

## System Report Results

The system overview provides information about all parts of the Unified Communications Manager network. The report provides the following sections. See the table.

Field

Description

Top 5 Users based on Charge

Details the five users who have incurred the highest
                                          					 charges for calls that occurred during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Destinations based on Charge

Details the five called numbers that have incurred
                                          					 the highest charges for calls during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Calls based on Charge

Details the five calls that have incurred the
                                          					 highest charges for calls during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Users based on Duration

Details the five users who have spent the most time
                                          					 on calls during the specified date range. See Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Destinations based on Duration

Details the five called numbers that have been
                                          					 engaged in calls for the longest time during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Calls based on Duration

Details the five longest calls for the specified
                                          					 date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Traffic Summary Report - Hour of Day

Shows the volume of calls during the specified date
                                          					 range based on each hour of the day. If the date range is within one day, the
                                          					 system identifies the hour with the highest traffic volume (the BHCC number).
                                          					 See the Traffic Summary Report Results for details about this section of the system overview report.

Traffic Summary Report - Day of Week

Shows the volume of calls during the specified date
                                          					 range based on each day of the week. See the Traffic Summary Report Results for details about this section of the system overview report.

Traffic Summary Report - Day of Month

Shows the volume of calls during the specified date
                                          					 range based on each day of the month. See the Traffic Summary Report Results for details about this section of the system overview report.

Quality of Service Report - Summary

Shows the number of calls that fell within each
                                          					 voice-quality category during the specified date range. See the QoS Summary Report Results for details about this section of the system overview report.

Gateway Summary Report

Shows the summary of the call classification for
                                          					 each gateway along with the QoS, the number of calls, and the duration for each
                                          					 classification for the gateway during the specified date range. See the QoS by Gateways Report Results for details about this section of the system overview report.

## CDR Error Report Results

The CDR Error report provides the following information. See
                              		  the following table.

Field

Description

Time

The hour of the specified day that the error
                                          					 occurred.

No of Error CDRs

The total number of CDR records that were not
                                          					 processed during the CAR load because of an error.

No of Valid CDRs

The total number of CDR records that were
                                          					 successfully loaded into CAR.

% of Error CDRs

The percentage of failed CDR data records out of all
                                          					 the CDR data records to be loaded.

The following figure displays sample output of the CDR Error
                              		  report in PDF format.

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Field | Description |
|---|---|
| Orig. Time | The time that the call was placed, in 24-hour,
                                          					 minute, and second format. |
| Term. Time | The time that the call disconnected, in 24-hour,
                                          					 minute, and second format. |
| Duration(s) | The time, in seconds, that the call was connected. |
| Orig. | The originating number from which the call was
                                          					 placed. |
| Dest. | The destination number to which the call was
                                          					 directed. |
| Call Classification - Call categories specify
                                          					 classes. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911. |
| Orig. Codec | The codec that the originating device uses. |
| Dest. Codec | The codec that the destination device uses. |
| Orig. Device | The name of the device that placed the call. |
| Dest. Device | The name of the device that received the call. |
| Orig. QoS | The voice quality that the device that placed the
                                          					 call experienced. |
| Dest. QoS | The voice quality that the device that received the
                                          					 call experienced. |

| Field | Description |
|---|---|
| Quality of Service | The quality of service of the calls. |
| Call Legs | Number of call legs with the quality of service that
                                          					 the Quality of Service field specified. |

| Field | Description |
|---|---|
| Time/Day | Indicates the cumulative hours of the day(s), the
                                          					 days of the week, or the days of the month for the selected date range. |
| % of Call Legs | Displays the percentage of calls for each gateway
                                          					 for the hours of the day, the days of the week, or the days of the month for
                                          					 the selected date range. |

| Field | Description |
|---|---|
| Time/Day | The cumulative hours of the day(s), the days of the
                                          					 week, or the days of the month for the selected date range. |
| % of Call Legs | The percentage of calls for each gateway for the
                                          					 hours of the day, the days of the week, or the days of the month for the
                                          					 selected date range. |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911. |

| Field | Description |
|---|---|
| Time/Day | The cumulative hours of the day(s), the days of the
                                          					 week, or the days of the month for the selected date range. |
| Average Number of Calls | The percentage of calls for each gateway for the
                                          					 hours of the day, the days of the week, or the days of the month for the
                                          					 selected date range. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911. |
| Total | The total number of calls for each hour or day. |

| Field | Description |
|---|---|
| Orig. | The originating number from which the call was
                                          					 placed. |
| Dest. | The destination number to which the call was
                                          					 directed. |
| Orig. Date Time | The date and time that the call originated. |
| Duration (sec) | The time, in seconds, that the call connected. |
| Call Classification | The type of call (internal, incoming, on so on.) |
| Authorization Level | The authorization level for calls for each chosen
                                          					 authorization code name. |

| Field | Description |
|---|---|
| Orig. | The originating number from which the call was
                                          					 placed. |
| Dest. | The destination number to which the call was
                                          					 directed. |
| Orig. Date Time | The date and time that the call originated. |
| Duration (sec) | The time, in seconds, that the call connected. |
| Call Classification | The type of call (internal, incoming, and so on.) |
| Authorization Code Name | The authorization code name for each authorization
                                          					 level that you chose. |

| Field | Description |
|---|---|
| Orig. | The originating number from which the call was
                                          					 placed. |
| Dest. | The destination number to which the call was
                                          					 directed. |
| Orig. Date Time | The date and time that the call originated. |
| Duration (sec) | The time, in seconds, that the call connected. |
| Call Classification | The type of call (internal, incoming, and so on). |

| Field | Description |
|---|---|
| Orig. Time | Time at which the malicious call originated. |
| Term. Time | Time at which the malicious call terminated. |
| Duration | Total time of malicious call in seconds. |
| Orig. | Originating DN. |
| Dest. | Destination DN. |
| Orig. Device | Name of the originating device. |
| Dest. Device | Name of the destination device. |
| Call Classification | Classification of the malicious call. |

| Field | Description |
|---|---|
| Time/Day | Indicates the cumulative hours of the day(s), the
                                          					 days of the week, or the days of the month for the selected date range. |
| Call Legs | Number of calls for each precedence level by
                                          					 time/day. |
| Precedence Level | Precedence level value of the call. |
| No. of Call Legs | Number of call legs per each precedence level. |
| Percentage | Percentage of calls per each precedence level. |

| Field | Description |
|---|---|
| Top 5 Users based on Charge | Details the five users who have incurred the highest
                                          					 charges for calls that occurred during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Destinations based on Charge | Details the five called numbers that have incurred
                                          					 the highest charges for calls during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Calls based on Charge | Details the five calls that have incurred the
                                          					 highest charges for calls during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Users based on Duration | Details the five users who have spent the most time
                                          					 on calls during the specified date range. See Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Destinations based on Duration | Details the five called numbers that have been
                                          					 engaged in calls for the longest time during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Calls based on Duration | Details the five longest calls for the specified
                                          					 date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Traffic Summary Report - Hour of Day | Shows the volume of calls during the specified date
                                          					 range based on each hour of the day. If the date range is within one day, the
                                          					 system identifies the hour with the highest traffic volume (the BHCC number).
                                          					 See the Traffic Summary Report Results for details about this section of the system overview report. |
| Traffic Summary Report - Day of Week | Shows the volume of calls during the specified date
                                          					 range based on each day of the week. See the Traffic Summary Report Results for details about this section of the system overview report. |
| Traffic Summary Report - Day of Month | Shows the volume of calls during the specified date
                                          					 range based on each day of the month. See the Traffic Summary Report Results for details about this section of the system overview report. |
| Quality of Service Report - Summary | Shows the number of calls that fell within each
                                          					 voice-quality category during the specified date range. See the QoS Summary Report Results for details about this section of the system overview report. |
| Gateway Summary Report | Shows the summary of the call classification for
                                          					 each gateway along with the QoS, the number of calls, and the duration for each
                                          					 classification for the gateway during the specified date range. See the QoS by Gateways Report Results for details about this section of the system overview report. |

| Field | Description |
|---|---|
| Time | The hour of the specified day that the error
                                          					 occurred. |
| No of Error CDRs | The total number of CDR records that were not
                                          					 processed during the CAR load because of an error. |
| No of Valid CDRs | The total number of CDR records that were
                                          					 successfully loaded into CAR. |
| % of Error CDRs | The percentage of failed CDR data records out of all
                                          					 the CDR data records to be loaded. |