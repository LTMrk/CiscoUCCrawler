---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-150-user-g-1e872b9ea2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_150/user/guide/cuic_b_1501_user-guide/cuic_m_1501_report-and-time-zones.html
retrieved_at: 2026-08-21T04:42:37.812525+00:00
---

Cisco Unified Intelligence Center User Guide, Release 15.0(1)

# Cisco Unified Intelligence Center User Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Report and Time zones

## Chapter: Report and Time zones

- Report and Time zones

- Report and Time Zones

# Report and Time zones

## Report and Time Zones

You can configure three related time settings in Unified Intelligence Center: server, data source, and user. They work together
                           so that:

Dates and times you enter in a filter match your local intent.

Queries sent to a historical database match how that database stores time (often UTC).

Dates and times in the report grid appear in your time zone.

This section explains each setting, how they interact, and includes US Eastern Time (ET) and UTC examples typical of contact-center
                           deployments (UCCX, UCCE, and standalone CUIC).

### Server

The server time zone is the time zone of the Unified Intelligence Center application server. It is set during installation.
                              The server administrator can view or change it using these CLI commands:

show timezone config

set timezone zone

For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html

How the server time zone is used

If your user time zone is configured, normal report viewing and dashboards use your time zone for display and not the server
                              time zone.

### Data Source

The data source time zone is defined when the data source is configured in the Data Sources drawer. It is the time zone of
                              the remote database or warehouse and how that system stores or interprets date and time values.

It is not the time zone of the CUIC server and not the time zone of your PC.

Why data source time zone is often different from server time zone

Historical contact center databases, such as UCCE AW/HDS or UCCX Informix historical stores, record events in the operating
                              system time zone of the data source host. If the data source time zone is not set correctly, a filter such as "June 15, 9:00
                              a.m. to 5:00 p.m. Eastern" can query the wrong time interval in the database.

If it is wrong, historical reports can be off by several hours even when your user time zone is correct.

If data source time zone is not set, Unified Intelligence Center uses the server time zone when converting filters and reading
                              query results.

Example: Server Eastern, data source UTC (historical report)

Supervisor enters an absolute filter:

June 15, 2026, 9:00 AM – 5:00 PM (meaning Eastern Time)

You think in ET; the warehouse stores UTC; CUIC converts in both directions.

Live Data (real-time stream) and data source time zone

Live Data reports (real-time queue, agent, and stream dashboards) uses browser time zone for agents and for user time zone
                              for supervisors.

Example: Live Data vs. historical (same contact center)

If Live Data times look wrong, check user time zone first. If historical data is off by a fixed number of hours, check data
                              source time zone on the historical connection.

### Report

There is no time zone field on stock Reports in the Unified Intelligence Center UI. If you open bundled (stock) reports, you
                              will not see a time zone setting on the report itself. This is expected.

What Report Time Zone means in practice

When you run a report, dates and times in the grid or chart are shown in the running user’s time zone from the user profile.
                              If user time zone is not set, the server time zone is used.

The date and time values you enter in a report filter are not a separate Report Time Zone. They are interpreted in your user
                              time zone (or server time zone if yours is not set), then converted for the database as described under Time Zone Considerations
                              section.

Example: Two users, same stock report

The report object is identical; display follows each user’s profile.

If your contact center spans several time zones and you need to compare results, run historical reports with an absolute date
                              range and a specific time period. Align user time zones when you need to match another person’s clock times.

### User

The user time zone is set on the User Information page (user profile).

It is not only used when you run reports. It applies to any activity performed as that user:

If user time zone is not set, Unified Intelligence Center uses the server time zone for display and filter conversion.

Example: User time zone for reports, schedules, and Live Data

Example: Reviewing a colleague’s report (New York and another region)

A user in New York runs a historical report for January 1, 2026, 12:00 AM – 11:59 PM Eastern and shares the filter settings.

To see the same clock times on the grid as the New York colleague:

Set user time zone on the profile to America/New York.

Run the same report with the same absolute date range.

To work in your own local zone instead, keep your profile time zone (for example America/Los_Angeles ) and use an absolute range that matches the business day you intend—understanding that clock labels on the grid will differ
                              from New York.

### Time Zone Considerations

Unified Intelligence Center applies these rules for historical reports:

Filter input : Time you enter in a filter is local to your user time zone (or server time zone if user time zone is not set). Unified Intelligence
                                    Center converts this value toward the data source time zone when the query is formed.

Report display : Values from the database are read using the data source time zone (or server if data source time zone is not set), then
                                    shown in your user time zone (or server if user time zone is not set).

Fallback : If user time zone or data source time zone is not configured, the server time zone is used for the missing setting.

Live Data : Display and filter metadata use user time zone. Live Data does not use the same SQL date-filter conversion path as historical
                                    databases.

The adjustment for filter queries is based on (data source offset − user offset), with the server time zone substituted when
                              user or data source time zone is not set.

Example 1 - Filter value conversion (Eastern user, UTC database)

You enter a date and time in a historical report filter. Below shows how settings affect the value used toward the database.

Filter value you enter = June 15, 2026 12:00:00 AM (midnight Eastern)

Assume EDT (UTC−4) for Eastern in this example.

Example 2: Filter value conversion (business hours Eastern to UTC)

Filter value you enter = June 15, 2026 9:00:00 AM – 5:00:00 PM (Eastern, EDT = UTC−4)

Example 3: Database value conversion (what you see in the report)

The database stores a single timestamp. Below shows how settings affect what appears in the grid.

Database stored value = June 15, 2026 6:00:00 PM UTC

\*When data source time zone is not set to UTC, CUIC may not treat the stored value as UTC; always configure data source time
                              zone to match the warehouse.

Summary: The same database timestamp displays as different clock times for users in different time zones.

Example 4: Live Data supervisor (real-time user)

Example 5: Scheduled historical report

### Summary

| Use | Description |
|---|---|
| Fallback for reports | If your user time zone is not set on your profile, report dates and times are displayed in the server time zone. |
| Fallback for conversion | If user or data source time zone is not set, the server time zone is used in place of the missing value when converting filter
                                       values or reading database results. |
| Relative date filters | Filters such as Today, This Week, and Last Month are calculated starting from the server clock. If your user time zone is
                                       set, the calendar day is adjusted toward your local day when needed. |
| Permalinks | If you open a report permalink without signing in, display may use the server time zone. |

|  | Server time zone | Data source time zone |
|---|---|---|
| Represents | Where CUIC runs | Where historical data is stored |
| Typical US deployment | America/New_York (Eastern) - CUIC VM in US East | GMT or UTC — warehouse stores universal time |
| Configured in UI? | No (installation / CLI) | Yes - Data Sources |

| Setting | Value |
|---|---|
| Server time zone | America/New_York (Eastern, EDT = UTC−4 in summer) |
| Data source time zone | GMT (UTC) |
| User time zone | America/New_York (Eastern) |

| Step | Time zone logic | Result |
|---|---|---|
| 1. What you type | Treated as Eastern (user) | 9:00 AM – 5:00 PM ET |
| 2. Query sent to database | Converted to UTC (data source) | 1:00 PM – 9:00 PM UTC on June 15 |
| 3. Database returns a row stored as | 2:30 PM UTC on June 15 | (example call-completion time) |
| 4. What you see in the grid | Converted to Eastern (user) | 10:30 AM Eastern on June 15 |

| Report type | Data source time zone | What matters for display |
|---|---|---|
| Historical (database query, stored procedure) | Required for correct date filters | User time zone + data source time zone |
| Live Data / real-time stream | Not used for stream display | User time zone for timestamps in the grid and toolbar |

| Setting | Value |
|---|---|
| Server | America/New_York (Eastern) |
| User | America/New_York (Eastern) |
| Historical data source | GMT (UTC) |
| Live Data connection | (real-time stream; no date-range SQL filter) |

| Action | Data source TZ role | What supervisor sees |
|---|---|---|
| Open Live Data agent queue dashboard | Not used for SQL date conversion | Queue metrics and “last updated” in Eastern |
| Run historical report for “yesterday 9 AM–5 PM ET” | Used — filter converted ET → UTC | Grid times in Eastern ; query used UTC bounds |

| Note | For weekly and monthly historical reports, aggregation in the underlying warehouse (daily, weekly, monthly or yearly) often
                                       follows the data source or warehouse time zone for example, week boundaries at midnight UTC. When comparing reports across
                                       regions, use an absolute date range and the same time period in the filter. |
|---|---|

| User | User time zone | Same filter: June 15, 2026 9:00 AM – 5:00 PM |
|---|---|---|
| Supervisor A | America/New_York (Eastern) | Sees grid times in Eastern |
| Supervisor B | America/Los_Angeles (Pacific) | Sees grid times in Pacific |

| Activity | Uses user time zone? |
|---|---|
| Viewing historical or Live Data reports (grid, chart, export) | Yes |
| Entering date/time values in report filters | Yes - input treated as local to this zone |
| Scheduled reports you own | Yes - when the schedule runs and how emailed results are formatted |
| Dashboard gadgets while signed in | Yes |
| Permalinks while signed in | Yes |

| Setting | Value |
|---|---|
| User time zone | America/New_York (Eastern) |
| Server time zone | America/New_York (Eastern) |
| Schedule | Daily at 8:00 AM (owned by this user) |
| Historical data source | GMT (UTC) |

| Activity | Effect of user time zone |
|---|---|
| Run historical report | Filter times treated as Eastern ; grid shows Eastern |
| Live Data dashboard | Stream timestamps shown in Eastern |
| Scheduled email at 8:00 AM | Job runs at 8:00 AM Eastern , not UTC |
| User clears time zone on profile | All of the above fall back to server (Eastern) |

| User time zone | Data source time zone | Effective user zone | Effective data source zone | Value used toward database (UTC) | Explanation |
|---|---|---|---|---|---|
| Set - Eastern (UTC−4) | Set - UTC | Eastern | UTC | June 15, 2026 4:00:00 AM UTC | Midnight Eastern = 4:00 AM UTC |
| Not set | Set - UTC | Server Eastern (UTC−4) | UTC | June 15, 2026 4:00:00 AM UTC | Server substitutes for user |
| Set - Eastern (UTC−4) | Not set | Eastern | Server Eastern (UTC−4) | June 15, 2026 12:00:00 AM Eastern | No net offset when DS defaults to server |
| Not set | Not set | Server Eastern | Server Eastern | June 15, 2026 12:00:00 AM Eastern | Both default to server; no conversion |

| User time zone | Data source time zone | Query window sent to database (UTC) |
|---|---|---|
| Eastern | UTC | June 15, 2026 1:00 PM – 9:00 PM UTC |
| Eastern | (not set; server = Eastern) | June 15, 2026 9:00 AM – 5:00 PM Eastern (no DS offset) |
| (not set; server = Eastern) | UTC | June 15, 2026 1:00 PM – 9:00 PM UTC |

| Data source time zone | User time zone | Effective DS zone | Effective user zone | Displayed in report (Eastern, EDT) |
|---|---|---|---|---|
| Set - UTC | Set - Eastern | UTC | Eastern | June 15, 2026 2:00:00 PM Eastern |
| Not set (server = Eastern) | Set - Eastern | Server Eastern | Eastern | June 15, 2026 6:00:00 PM Eastern * |
| Set - UTC | Not set (server = Eastern) | UTC | Server Eastern | June 15, 2026 2:00:00 PM Eastern |
| Not set | Not set | Server Eastern | Server Eastern | June 15, 2026 6:00:00 PM Eastern * |

| Setting | Value |
|---|---|
| Server | America/New_York (Eastern) |
| User | America/New_York (Eastern) |
| Report | Live Data — CSQ statistics |
| Historical data source (not used for this view) | GMT (UTC) |

| Item | Time zone | Example |
|---|---|---|
| Last updated on dashboard | User (Eastern) | 3:45 PM Eastern |
| Underlying stream processing | Server clock internally | — |
| If user changes profile to America/Chicago and refreshes | User (Central) | 2:45 PM Central (same instant) |

| Setting | Value |
|---|---|
| Schedule owner user time zone | America/New_York (Eastern) |
| Schedule | Weekly, Monday 7:00 AM |
| Historical data source | GMT (UTC) |
| Filter in schedule | Previous week, absolute range |

| Item | Time zone used |
|---|---|
| Schedule fires | 7:00 AM Eastern (owner’s user time zone) |
| Email attachment datetimes | Eastern |
| Query for Previous Week | Filter intent Eastern converted to UTC for warehouse |

| Note | Week and month boundaries in warehouse-aggregated historical data often follow the data source (UTC) time zone. CUIC schedule
                                       run time follows the schedule owner’s user time zone. |
|---|---|

| Setting | Where configured | Primary uses | US deployment example |
|---|---|---|---|
| Server | Installation / CLI | Logging; fallback when user or DS unset; relative dates | America/New_York |
| Data source | Data Sources UI | Historical query filters; reading DB timestamps | GMT / UTC |
| Report | (not stored on stock reports) | Display = user time zone at run time | — |
| User | User Information profile | Reports, filters, schedules, dashboards, Live Data display | America/New_York |