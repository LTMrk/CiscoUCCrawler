---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--04b2731698
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_01000.html
retrieved_at: 2026-08-21T01:33:55.750799+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Review User Reports Results

## Chapter: Review User Reports Results

# Review User Reports Results

This chapter describes report output information for each CAR
                        		user report.

## Bill Summary Report Results

The report combines information in groups by the user name in
                              		  ascending order. The summary report includes the following fields (see the
                              		  following table).

Field

Description

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

Long-distance calls that originate in the Unified Communications Manager network that go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Others

All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911.

QOS

The number of calls for each Quality of Service
                                          					 category. Parameters that the CAR administrator sets provide the basis for the
                                          					 following QoS categories:

- Good - QoS for
                                             						these calls designates the highest possible quality.

- Acceptable - QoS
                                             						for these calls shows them slightly degraded but still within an acceptable
                                             						range.

- Fair - QoS for
                                             						these calls, that although degraded, still fall within a usable range.

- Poor - QoS for
                                             						these calls get categorized as unsatisfactory.

- NA - These calls
                                             						do not match any criteria for the established QoS categories.

See the Define QoS Values and the Generate QoS by Gateway Reports .

Calls

Indicates the number of calls for each call
                                          					 classification.

Charge

Indicates the charge that is associated with each
                                          					 call. Call charge information that the CAR administrator provides for the CAR
                                          					 rating engine provides basis for charges. See CAR Rating Engine .

The following figures display sample output from the
                              		  Individual Bill and Department Bill Summary reports.

## Bill Detail Report Results

The report places information in groups by the user name in
                              		  ascending order. The detail report includes the following fields (see the
                              		  following table).

Field

Description

Date

The date that the call originated.

Orig. Time

The time that the call originated.

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

Long-distance calls that originate in the Unified Communications Manager network that go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Others

All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911.

QOS

The number of calls for each Quality of Service
                                          					 category. Parameters that the CAR administrator sets provide the basis for the
                                          					 following QoS categories:

- Good - QoS for
                                             						these calls designates the highest possible quality.

- Acceptable - QoS
                                             						for these calls shows them slightly degraded but still within an acceptable
                                             						range.

- Fair - QoS for
                                             						these calls, that although degraded, still fall within a usable range.

- Poor - QoS for
                                             						these calls get categorized as unsatisfactory.

- NA - These calls
                                             						do not match any criteria for the established QoS categories.

See the Define QoS Values and the Generate QoS by Gateway Reports .

Duration(s)

The time, in seconds, that the call remains
                                          					 connected.

Charge

The charge that is associated with each call. Call
                                          					 charge information that the CAR administrator provided for the CAR rating
                                          					 engine provides the basis for charges. See the Define QoS Values .

The following figures display sample output from the
                              		  Individual Bill and Department Bill Detail reports.

## Top N by Charge or Duration Report Results

The fields for the Top N by Charge and the Top N by Duration
                              		  vary depending on the report type. The reports show only outgoing calls. See
                              		  the table.

Field

Description

By Individual Users

User

User names.

Calls

Total number of calls.

Duration(s)

The time, in seconds, that the call was connected.

Charge

The charge that is associated with each call. Call
                                          					 charge information that the CAR administrator provided for the CAR rating
                                          					 engine provides basis for charges. See the Define QoS Values .

By Destinations

Dest

The destination of the calls.

Call Classification

The total number of calls for each call
                                          					 classification.

Calls

Total number of calls.

Duration

The time, in seconds, that the call was connected.

Charge

The charge that is associated with each call. Call
                                          					 charge information that the CAR administrator provided for the CAR rating
                                          					 engine provides basis for charges. See CAR Rating Engine .

By Number of Calls

User

User names.

Date

Date that the call occurred.

Orig Time

Time that the call originated.

Orig

Origin of the call.

Dest

Destination of the call.

Call Classification

The total number of calls for each call
                                          					 classification.

Duration

The time, in seconds, that the call was connected.

Charge

The charge that is associated with each call. Call
                                          					 charge information that the CAR administrator provided for the CAR rating
                                          					 engine provides basis for charges. See CAR Rating Engine .

Figure 1 and Figure 2 display sample reports.

## Top N by Number of Calls Report Results

The fields for the Top N by Number of Calls report vary
                              		  depending on the report type. The report shows both incoming and outgoing
                              		  calls. See the table.

Field

Description

By Individual Users

Users

User names.

Charge

The total amount of billing charges for all calls to
                                          					 that user. Call charge information that the CAR administrator provided for the
                                          					 CAR rating engine provides basis for charges. See CAR Rating Engine .

Duration(s)

The time, in seconds, that the call connected.

Calls Made

The total number of calls that the user placed.

Calls Received

The total number of calls that the user received.

Total Calls

The total number of incoming and outgoing calls.

By Extensions

Extension No

The extension that originated/placed and received
                                          					 the call.

Charge

The total amount of billing charges for all calls to
                                          					 that user. Call charge information that the CAR administrator provided for the
                                          					 CAR rating engine provides basis for charges. See CAR Rating Engine .

Duration

The time, in seconds, that the call was connected.

Calls Made

The total number of calls that the user placed.

Calls Received

The total number of calls that the user received.

Total Calls

The total number of incoming and outgoing calls.

Figure 1 displays sample report output of Top N by Number of Calls by Individual Users
                              		  in PDF format.

## Call Usage for Assistant Detail Report Results

The report, which supports Cisco Unified Communications Manager Assistant , shows the number of calls that assistants handled for themselves, that the assistant handled for each manager, and the total
                              number of calls that the assistant handled. The report places information in groups about calls that the assistant handled
                              and calls that the assistant handled for the manager. The detail report includes the following fields (see the following table).

Field

Description

Date

The date that the call originated.

Orig. Time

The time that the call originated.

Orig.

The originating number from which the call was
                                          					 placed.

Dest.

The destination number to which the call was
                                          					 directed.

Call Classification

The type of call (internal, incoming, and so on.)

Duration (sec)

The time, in seconds, that the call connected.

Figure 1 displays sample output from a Call Usage for Assistant Detail report in PDF
                              		  format.

## Call Usage for Assistant Summary Report Results

The report, which supports Cisco Unified Communications Manager Assistant , shows information about calls that the assistant handled for themselves and that the assistant handled for the manager.
                              The reports place call information by groups by attendant name. The summary report includes the following fields (see the
                              following table).

Field

Description

Assistant-Extn/Manager

Shows the assistant name and directory number. If
                                          					 the assistant handles a call for a manager, the manager name displays.

Call Classification - Call categories specify
                                          					 classes.

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network that go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan .

Others

All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911.

Calls

The number of calls that the assistant handled or
                                          					 that the assistant handled for the manager.

Duration (sec)

The total duration for all the calls for the
                                          					 particular call classification.

The following figure displays sample output of the Call
                              		  Usage for Assistant Summary report in PDF format.

## Call Usage for Manager Detail Report Results

The report, which supports Cisco Unified Communications Manager Assistant , provides information about calls that managers handle for themselves and that assistants handle for managers. The report
                              places information in groups by the assistant name and shows the total number of calls that the manager handles and that the
                              assistant handles for the manager. The detail report includes the following fields (see the table).

Field

Description

Date

The date that the call originates.

Orig. Time

The time that the call originates.

Orig.

The originating number from which the call is
                                          					 placed.

Dest.

The destination number to which the call is
                                          					 directed.

Call Classification

The type of call (internal, incoming, and so on.)

Duration (sec)

The time, in seconds, that the call connects.

Figure 1 displays sample output from the Call Usage for Manager Detail report.

## Call Usage for Manager Summary Report Results

The report, which supports Cisco Unified Communications Manager Assistant , shows information about calls that the managers handle for themselves and that the assistants handle for the managers. The
                              report places information in groups by the manager name and shows the total number of calls that are handled for each manager.
                              The report includes the following fields (see the following table).

Field

Description

Manager-Extn/Assistant

Shows the manager name and directory number. If the
                                          					 assistant handles a call for a manager, the assistant name displays.

Call Classification - Call categories specify
                                          					 classes.

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network that go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan .

Others

All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911.

Calls

The number of calls that the assistant or the
                                          					 manager handles.

Duration

The total duration for all the calls for the
                                          					 particular call classification.

The following figure displays sample output of the Call
                              		  Usage for Manager Summary report in PDF format.

## IP Phone Services Report Results

The Cisco IP Phone Services report includes the following
                              		  fields (see the table).

Field

Description

Cisco IP Phone Services

The name of the selected service.

Number of Subscribers

The total number of subscribers for a given service.

% Subscription

The percentage of users who are subscribed to a
                                          					 given service, out of the total number of subscriptions for all services.

Figure 1 displays sample output from the Cisco IP Phone Services Report in PDF format.

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
| Call Classification - Call categories specify
                                          					 classes. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Others | All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911. |
| QOS | The number of calls for each Quality of Service
                                          					 category. Parameters that the CAR administrator sets provide the basis for the
                                          					 following QoS categories: Good - QoS for
                                             						these calls designates the highest possible quality. Acceptable - QoS
                                             						for these calls shows them slightly degraded but still within an acceptable
                                             						range. Fair - QoS for
                                             						these calls, that although degraded, still fall within a usable range. Poor - QoS for
                                             						these calls get categorized as unsatisfactory. NA - These calls
                                             						do not match any criteria for the established QoS categories. See the Define QoS Values and the Generate QoS by Gateway Reports . |
| Calls | Indicates the number of calls for each call
                                          					 classification. |
| Charge | Indicates the charge that is associated with each
                                          					 call. Call charge information that the CAR administrator provides for the CAR
                                          					 rating engine provides basis for charges. See CAR Rating Engine . |

| Field | Description |
|---|---|
| Date | The date that the call originated. |
| Orig. Time | The time that the call originated. |
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
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Others | All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911. |
| QOS | The number of calls for each Quality of Service
                                          					 category. Parameters that the CAR administrator sets provide the basis for the
                                          					 following QoS categories: Good - QoS for
                                             						these calls designates the highest possible quality. Acceptable - QoS
                                             						for these calls shows them slightly degraded but still within an acceptable
                                             						range. Fair - QoS for
                                             						these calls, that although degraded, still fall within a usable range. Poor - QoS for
                                             						these calls get categorized as unsatisfactory. NA - These calls
                                             						do not match any criteria for the established QoS categories. See the Define QoS Values and the Generate QoS by Gateway Reports . |
| Duration(s) | The time, in seconds, that the call remains
                                          					 connected. |
| Charge | The charge that is associated with each call. Call
                                          					 charge information that the CAR administrator provided for the CAR rating
                                          					 engine provides the basis for charges. See the Define QoS Values . |

| Field | Description |
|---|---|
| By Individual Users |
| User | User names. |
| Calls | Total number of calls. |
| Duration(s) | The time, in seconds, that the call was connected. |
| Charge | The charge that is associated with each call. Call
                                          					 charge information that the CAR administrator provided for the CAR rating
                                          					 engine provides basis for charges. See the Define QoS Values . |
| By Destinations |
| Dest | The destination of the calls. |
| Call Classification | The total number of calls for each call
                                          					 classification. |
| Calls | Total number of calls. |
| Duration | The time, in seconds, that the call was connected. |
| Charge | The charge that is associated with each call. Call
                                          					 charge information that the CAR administrator provided for the CAR rating
                                          					 engine provides basis for charges. See CAR Rating Engine . |
| By Number of Calls |
| User | User names. |
| Date | Date that the call occurred. |
| Orig Time | Time that the call originated. |
| Orig | Origin of the call. |
| Dest | Destination of the call. |
| Call Classification | The total number of calls for each call
                                          					 classification. |
| Duration | The time, in seconds, that the call was connected. |
| Charge | The charge that is associated with each call. Call
                                          					 charge information that the CAR administrator provided for the CAR rating
                                          					 engine provides basis for charges. See CAR Rating Engine . |

| Field | Description |
|---|---|
| By Individual Users |
| Users | User names. |
| Charge | The total amount of billing charges for all calls to
                                          					 that user. Call charge information that the CAR administrator provided for the
                                          					 CAR rating engine provides basis for charges. See CAR Rating Engine . |
| Duration(s) | The time, in seconds, that the call connected. |
| Calls Made | The total number of calls that the user placed. |
| Calls Received | The total number of calls that the user received. |
| Total Calls | The total number of incoming and outgoing calls. |
| By Extensions |
| Extension No | The extension that originated/placed and received
                                          					 the call. |
| Charge | The total amount of billing charges for all calls to
                                          					 that user. Call charge information that the CAR administrator provided for the
                                          					 CAR rating engine provides basis for charges. See CAR Rating Engine . |
| Duration | The time, in seconds, that the call was connected. |
| Calls Made | The total number of calls that the user placed. |
| Calls Received | The total number of calls that the user received. |
| Total Calls | The total number of incoming and outgoing calls. |

| Field | Description |
|---|---|
| Date | The date that the call originated. |
| Orig. Time | The time that the call originated. |
| Orig. | The originating number from which the call was
                                          					 placed. |
| Dest. | The destination number to which the call was
                                          					 directed. |
| Call Classification | The type of call (internal, incoming, and so on.) |
| Duration (sec) | The time, in seconds, that the call connected. |

| Field | Description |
|---|---|
| Assistant-Extn/Manager | Shows the assistant name and directory number. If
                                          					 the assistant handles a call for a manager, the manager name displays. |
| Call Classification - Call categories specify
                                          					 classes. |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Others | All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911. |
| Calls | The number of calls that the assistant handled or
                                          					 that the assistant handled for the manager. |
| Duration (sec) | The total duration for all the calls for the
                                          					 particular call classification. |

| Field | Description |
|---|---|
| Date | The date that the call originates. |
| Orig. Time | The time that the call originates. |
| Orig. | The originating number from which the call is
                                          					 placed. |
| Dest. | The destination number to which the call is
                                          					 directed. |
| Call Classification | The type of call (internal, incoming, and so on.) |
| Duration (sec) | The time, in seconds, that the call connects. |

| Field | Description |
|---|---|
| Manager-Extn/Assistant | Shows the manager name and directory number. If the
                                          					 assistant handles a call for a manager, the assistant name displays. |
| Call Classification - Call categories specify
                                          					 classes. |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                          					 switched telephone network (PSTN) to numbers without an area code or that
                                          					 include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                          in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Others | All other outgoing calls, such as toll-free numbers
                                          					 or emergency calls such as 911. |
| Calls | The number of calls that the assistant or the
                                          					 manager handles. |
| Duration | The total duration for all the calls for the
                                          					 particular call classification. |

| Field | Description |
|---|---|
| Cisco IP Phone Services | The name of the selected service. |
| Number of Subscribers | The total number of subscribers for a given service. |
| % Subscription | The percentage of users who are subscribed to a
                                          					 given service, out of the total number of subscriptions for all services. |