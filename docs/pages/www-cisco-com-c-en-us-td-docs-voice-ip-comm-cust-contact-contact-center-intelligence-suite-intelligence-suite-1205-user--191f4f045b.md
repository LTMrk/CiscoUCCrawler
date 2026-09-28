---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1205-user--191f4f045b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1205/user/guide/cuic_b_user-guide-1205/report-and-time-zones.html
retrieved_at: 2026-08-16T19:33:23.896556+00:00
---

Cisco Unified Intelligence Center User Guide, Release 12.5(1)

# Cisco Unified Intelligence Center User Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Reports and Time
	 Zones

## Chapter: Reports and Time
	 Zones

- Reports and Time                              	 Zones

# Reports and Time
                     	 Zones

You can configure
                           		  four time zones in Unified Intelligence Center: Server, Data Source, Report and
                           		  User.

## Server

The server time zone is defined during installation while running the installation wizard and it does not affect reports.
                           The server administrator can view and change the server time zone using these CLI commands: show timezone config and set timezone zone . For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html

## Data
                           		  Source

The data source
                           		  time zone is defined when the data source is configured. It is the time zone of
                           		  the database.

## Report

The report time
                           		  zone is defined in the report filter.

If your call center
                           		  spans several time zones and you intend to compare reports, run historical
                           		  reports using the absolute date range and a specific time period.

## User

The user's time
                           		  zone is set on the User Profile.

For example, when a user in New York is asked to review a report that was run by a colleague in the China office, the user
                           accesses the User Profile page to change the time zone to match the colleague's, and then runs the report using the same absolute
                           date range.

## Time Zone Considerations

The system treats the time-specific data that the user enters as local to the user's time zone and then converts this time
                           to the data source time zone when the filter query is formed.

The system treats
                           		  the time-specific data that it fetches from a data source as local to the data
                           		  source and then converts this time to the user time zone before displaying the
                           		  date and time in the report data.

If the user time zone or data source time zone is not configured, the system uses the time zone of the Unified Intelligence
                           Center server. The system performs these conversions only after the time zone normalization at data source level has occurred.

The schedule for Weekly and Monthly reports is based on the data source time zone, not the server time zone. That is, the
                                       week and month boundaries are midnight, in the time zone of the database, of the week or month beginning and end days.

Consider the
                           		  following example, in which the user enters the date and time value in the
                           		  filter. Depending on the time zone setting, the system converts the time zones
                           		  in the filter query as shown below:

filter value = 1/1/2010
                              			 12:00:00 AM

User Time Zone

User Time Zone

Data Source Time Zone

Data Source Time Zone

When set (+11 GMT)

When not set (Subtract
                                          						  Cisco Unified Intelligence Center server time zone)

When set (+2 GMT)

When not set (Add Cisco
                                          						  Unified Intelligence Center server time zone)

Thursday, December 31, 2009
                                          						  3:00:00 PM EET

Original Time – User time zone offset (+11 GMT) + Data source time zone (+2
                                       						GMT)

To
                                       						Original Time, -9 ( -11 +2) hours added

Thursday, December 31, 2009
                                          						  8:30:00 PM EET

Original Time – Cisco Unified Intelligence server time zone (+5.30 GMT) + Data
                                       						source time zone offset ( +2 GMT)

From
                                       						Original Time, 3.30 (– 5.30 +2) hours subtracted

Thursday, December 31, 2009
                                          						  3:00:00 PM EET

Original Time – User time zone offset (+11 GMT) + Data source time zone (+2
                                       						GMT)

To
                                       						Original Time, -9 ( -11 +2) hours added

Thursday, December 31, 2009
                                          						  6:30:00 PM IST

Original Time – User time zone offset (+11 GMT) + Cisco Unified Intelligence
                                       						server time zone (+5.30 GMT)

From
                                       						Original Time, 5.30 ( –11 +5.30) hours subtracted

Thursday, December 31, 2009
                                          						  6:30:00 PM IST

Original Time – User time zone offset (+11 GMT) + Cisco Unified Intelligence
                                       						server time zone (+5.30 GMT)

From
                                       						Original Time, 5.30 ( –11 +5.30) hours subtracted

Friday, January 1, 2010
                                          						  12:00:00 AM IST

To
                                       						Original Time, 0 (– 5.30 +5.30) hours added

Thursday, December 31, 2009
                                          						  8:30:00 PM EET

Original Time – Cisco Unified Intelligence server time zone (+5.30 GMT) + Data
                                       						source time zone offset ( +2 GMT)

From
                                       						Original Time, 3.30 (–5.30 +2) hours subtracted

Friday, January 1, 2010
                                          						  12:00:00 AM IST

To
                                       						Original Time, 0 (– 5.30 +5.30) hours added

The following
                           		  example shows a database with date and time values. Depending on your time zone
                           		  setting, the system converts and displays the time zones in the report data as
                           		  shown below:

Database value = 1/1/2010 12:00:00
                              			 AM

Data Source Time Zone

Data Source Time Zone

User Time Zone

User Time Zone

When set (+11 GMT)

When not set (Subtract
                                          						  Unified Intelligence Center server time zone)

When set (+2 GMT)

When not set (Add Unified
                                          						  Intelligence Center server time zone)

Thursday, December 31, 2009
                                          						  3:00:00 PM EET

Original Time – Data source time zone offset (+11 GMT) + User time zone (+2
                                       						GMT)

To
                                       						Original Time, -9 ( -11 +2) hours added

Thursday, December 31, 2009
                                          						  8:30:00 PM EET

Original Time – Unified Intelligence Center server time zone (+5.30 GMT) + User
                                       						time zone offset ( +2 GMT)

From
                                       						Original Time, 3.30 (– 5.30 +2) hours subtracted

Thursday, December 31, 2009
                                          						  3:00:00 PM EET

Original
                                       						Time – Data source time zone offset (+11 GMT) + User time zone (+2 GMT)

To
                                       						Original Time, -9 ( -11 +2) hours added

Thursday, December 31, 2009
                                          						  6:30:00 PM IST

Original
                                       						Time – Data source time zone offset (+11 GMT) + Unified Intelligence Center
                                       						server time zone (+5.30 GMT)

From
                                       						Original Time, 5.30 ( –11 +5.30) hours subtracted

Thursday, December 31, 2009
                                          						  6:30:00 PM IST

Original Time – Data source time zone offset (+11 GMT) + Unified Intelligence
                                       						Center server time zone (+5.30 GMT)

From
                                       						Original Time, 5.30 ( –11 +5.30) hours subtracted

Friday, January 1, 2010
                                          						  12:00:00 AM IST

To
                                       						Original Time, 0 (– 5.30 +5.30) hours added

Thursday, December 31, 2009
                                          						  8:30:00 PM EET

Original
                                       						Time – Unified Intelligence Center server time zone(+5.30 GMT) + User time zone
                                       						offset ( +2 GMT)

From
                                       						Original Time, 3.30 (–5.30 +2) hours subtracted

Friday, January 1, 2010
                                          						  12:00:00 AM IST

To
                                       						Original Time, 0 (– 5.30 +5.30) hours added

| Note | The schedule for Weekly and Monthly reports is based on the data source time zone, not the server time zone. That is, the
                                       week and month boundaries are midnight, in the time zone of the database, of the week or month beginning and end days. |
|---|---|

| User Time Zone | User Time Zone | Data Source Time Zone | Data Source Time Zone |
|---|---|---|---|
| When set (+11 GMT) | When not set (Subtract
                                          						  Cisco Unified Intelligence Center server time zone) | When set (+2 GMT) | When not set (Add Cisco
                                          						  Unified Intelligence Center server time zone) |
| Thursday, December 31, 2009
                                          						  3:00:00 PM EET Original Time – User time zone offset (+11 GMT) + Data source time zone (+2
                                       						GMT) To
                                       						Original Time, -9 ( -11 +2) hours added | Thursday, December 31, 2009
                                          						  8:30:00 PM EET Original Time – Cisco Unified Intelligence server time zone (+5.30 GMT) + Data
                                       						source time zone offset ( +2 GMT) From
                                       						Original Time, 3.30 (– 5.30 +2) hours subtracted | Thursday, December 31, 2009
                                          						  3:00:00 PM EET Original Time – User time zone offset (+11 GMT) + Data source time zone (+2
                                       						GMT) To
                                       						Original Time, -9 ( -11 +2) hours added | Thursday, December 31, 2009
                                          						  6:30:00 PM IST Original Time – User time zone offset (+11 GMT) + Cisco Unified Intelligence
                                       						server time zone (+5.30 GMT) From
                                       						Original Time, 5.30 ( –11 +5.30) hours subtracted |
| Thursday, December 31, 2009
                                          						  6:30:00 PM IST Original Time – User time zone offset (+11 GMT) + Cisco Unified Intelligence
                                       						server time zone (+5.30 GMT) From
                                       						Original Time, 5.30 ( –11 +5.30) hours subtracted | Friday, January 1, 2010
                                          						  12:00:00 AM IST To
                                       						Original Time, 0 (– 5.30 +5.30) hours added | Thursday, December 31, 2009
                                          						  8:30:00 PM EET Original Time – Cisco Unified Intelligence server time zone (+5.30 GMT) + Data
                                       						source time zone offset ( +2 GMT) From
                                       						Original Time, 3.30 (–5.30 +2) hours subtracted | Friday, January 1, 2010
                                          						  12:00:00 AM IST To
                                       						Original Time, 0 (– 5.30 +5.30) hours added |

| Data Source Time Zone | Data Source Time Zone | User Time Zone | User Time Zone |
|---|---|---|---|
| When set (+11 GMT) | When not set (Subtract
                                          						  Unified Intelligence Center server time zone) | When set (+2 GMT) | When not set (Add Unified
                                          						  Intelligence Center server time zone) |
| Thursday, December 31, 2009
                                          						  3:00:00 PM EET Original Time – Data source time zone offset (+11 GMT) + User time zone (+2
                                       						GMT) To
                                       						Original Time, -9 ( -11 +2) hours added | Thursday, December 31, 2009
                                          						  8:30:00 PM EET Original Time – Unified Intelligence Center server time zone (+5.30 GMT) + User
                                       						time zone offset ( +2 GMT) From
                                       						Original Time, 3.30 (– 5.30 +2) hours subtracted | Thursday, December 31, 2009
                                          						  3:00:00 PM EET Original
                                       						Time – Data source time zone offset (+11 GMT) + User time zone (+2 GMT) To
                                       						Original Time, -9 ( -11 +2) hours added | Thursday, December 31, 2009
                                          						  6:30:00 PM IST Original
                                       						Time – Data source time zone offset (+11 GMT) + Unified Intelligence Center
                                       						server time zone (+5.30 GMT) From
                                       						Original Time, 5.30 ( –11 +5.30) hours subtracted |
| Thursday, December 31, 2009
                                          						  6:30:00 PM IST Original Time – Data source time zone offset (+11 GMT) + Unified Intelligence
                                       						Center server time zone (+5.30 GMT) From
                                       						Original Time, 5.30 ( –11 +5.30) hours subtracted | Friday, January 1, 2010
                                          						  12:00:00 AM IST To
                                       						Original Time, 0 (– 5.30 +5.30) hours added | Thursday, December 31, 2009
                                          						  8:30:00 PM EET Original
                                       						Time – Unified Intelligence Center server time zone(+5.30 GMT) + User time zone
                                       						offset ( +2 GMT) From
                                       						Original Time, 3.30 (–5.30 +2) hours subtracted | Friday, January 1, 2010
                                          						  12:00:00 AM IST To
                                       						Original Time, 0 (– 5.30 +5.30) hours added |