---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--7a2d1f5c5d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_010010.html
retrieved_at: 2026-08-21T01:34:37.156751+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR Device Reports

## Chapter: CAR Device Reports

# CAR Device Reports

CAR provides reporting capabilities for three levels of users:
                        		administrators, managers, and individual users. Only administrators generate
                        		device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, gateways, and trunks.

## Device Reports Summary Descriptions

Device reports help CAR administrators track the load and performance of Unified Communications Manager -related devices, such as conference bridges, voice-messaging server, gateways, and trunks. This section describes the device
                              reports:

Gateway

Detail - Available for CAR administrators. Use the Gateway
                                          					 Detail report to track issues with specific gateways. The report provides a
                                          					 list of calls that used the specified gateways. Use this report to review
                                          					 detailed information about chosen gateways. You can specify gateways by type,
                                          					 such as all or some of the VG200 gateways in your system, or by only those
                                          					 gateways that use a particular route pattern. You can also specify search
                                          					 criteria based on call types and QoS values.

Summary - Available for CAR administrators. The Gateway
                                          					 Summary report provides a summary of all the calls that went through the
                                          					 gateways. It also provides the total number of calls and duration for each of
                                          					 the categories, namely Incoming, Tandem, and Outgoing (Long Distance, Local,
                                          					 International, Others, OnNet), and, also, the total calls for each QoS value
                                          					 for each gateway in the system. Use this report to track the functionality of
                                          					 the system on a daily basis. If you discover issues that need to be studied
                                          					 further, use the gateway detail report.

Utilization - Available for CAR administrators. The Gateway
                                          					 Utilization report provides an estimate of the utilization percentage of the
                                          					 gateway(s). You can examine the usage on the basis of each hour of a day or by
                                          					 a specified number of days of the week or month. Reports generate for each
                                          					 gateway that is chosen. Use this report for load balancing or capacity planning
                                          					 (to evaluate the need for adding or removing gateways, depending on their
                                          					 utilization). You can specify gateways by type, such as all or some of the
                                          					 VG200 gateways in your system, or by only those gateways that use a particular
                                          					 route pattern.

Route Patterns/Hunt Pilots

Route and Line Group Utilization - Only CAR administrators can
                                          					 generate the Route and Line Group Utilization report. This report provides an
                                          					 estimated utilization percentage of the chosen route and line group(s). You can
                                          					 examine the usage on the basis of each hour of a day or by a specified number
                                          					 of days of the week or month. Reports generate for each chosen route and line
                                          					 group. Use the report to analyze whether the route and line group capacity is
                                          					 sufficient to meet the usage requirements. Based on the results, you can decide
                                          					 whether additions are required. If you are load balancing gateways by using
                                          					 different route and line groups or route patterns and hunt lists that are
                                          					 assigned to the gateways, you can use this report to see the load for the whole
                                          					 grouping. This report also provides a convenient way of generating utilization
                                          					 information for a grouping of gateways by a particular route and line group;
                                          					 the group will also include any H.323 fallback gateways that are using the
                                          					 specified route and line group.

Route/Hunt List Utilization - Available for CAR
                                          					 administrators. The Route/Hunt List Utilization report provides an estimated
                                          					 utilization percentage of the chosen route/hunt list(s). You can examine the
                                          					 usage on the basis of each hour of a day or by a specified number of days of
                                          					 the week or month. Reports generate for each chosen route/hunt list. Use the
                                          					 report to analyze whether the route and line group capacity is sufficient to
                                          					 meet the usage requirements. Based on the results, you can decide whether
                                          					 additions are required. If you are load balancing gateways by using different
                                          					 route/hunt lists that are assigned to the gateways, you can use this report to
                                          					 see the load for the whole grouping. This report also provides a convenient way
                                          					 of generating utilization information for a grouping of gateways by a
                                          					 particular route/hunt list; the group will also include any H.323 fallback
                                          					 gateways that are using the chosen route/hunt list.

Route Pattern/Hunt Pilot Utilization - Available for CAR
                                          					 administrators. The Route Pattern/Hunt Pilot Utilization report provides an
                                          					 estimated utilization percentage of the chosen route pattern(s)/hunt pilot(s).
                                          					 You can examine the usage on the basis of each hour of a day or by a specified
                                          					 number of days of the week or month. Reports generate for each chosen route
                                          					 pattern/hunt pilot. Use the report to analyze system usage on the chosen route
                                          					 pattern/hunt pilot.

Hunt Pilot Summary - Only CAR administrators generate the Hunt
                                          					 Pilot Summary Report.The CDR Hunt Pilot Call Summary report displays the call
                                          					 details for the specified hunt pilot. This report displays an only an overview
                                          					 of the calls for the hunt pilots and hunt member information is not included.
                                          					 The CAR administrator can generate report for a maximum of five hunt pilot DNs.

Hunt Pilot Detail - Only CAR administrators generate the Hunt
                                          					 Pilot Detailed Call Report. This report displays call details for a hunt pilot
                                          					 number or a hunt member dn.

Conference Call Details - Available for CAR administrators. The
                                    				Conference Call Details report allows you to generate and view details about
                                    				conference calls and conference bridges. The Summary Report displays the
                                    				summary information of conference calls within a chosen date/time range but
                                    				does not contain information about each individual conference participant call
                                    				leg. The Detailed Report displays the detailed information about the conference
                                    				calls within a chosen date/time range and includes information about each
                                    				individual conference participant call leg.

Conference Bridge Utilization - Available for CAR administrators.
                                    				The Conference Bridge Utilization report provides an estimate of the
                                    				utilization percentage of the conference bridge(s). You can examine the usage
                                    				on the basis of each hour of a day or by a specified number of days of the week
                                    				or month. Generate reports for all the conference bridges in the system. Use
                                    				this report to determine the activity on the conference bridge(s) and whether
                                    				you need to add additional resources. This report helps you identify usage
                                    				patterns, so you can plan capacity when you discover recurring peaks in the
                                    				usage pattern.

Voice Messaging Utilization - Available for CAR administrators.
                                    				The Voice Messaging Utilization report provides an estimate of the utilization
                                    				percentage of the voice-messaging device(s). You can examine the usage on the
                                    				basis of each hour of a day or by a specified number of days of the week or
                                    				month. Reports generate for each voice-messaging device. Use this report to
                                    				determine the activity on the voice messaging device(s) and whether you need to
                                    				add additional resources. This report helps you to identify usage patterns, so
                                    				you can plan capacity when you discover recurring peaks in the usage pattern.

Trunk Utilization - Available for CAR administrators. Only CAR
                                    				administrators generate the Trunk Utilization report. This report calculates
                                    				the utilization reports for devices based on the duration of calls that passed
                                    				through the devices. You can generate this report on an hourly, daily, or
                                    				monthly basis. Reports generate for each trunk that is chosen. You can use this
                                    				report for capacity assessment. You can also generate utilization reports for
                                    				route groups, route lists and route patterns that are connected through trunks.

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide