---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1205-user--227a57c399
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1205/user/guide/cuic_b_report-customization-guide-1205/cuic_b_report-customization-guide-1205_chapter_0110.html
retrieved_at: 2026-08-21T04:38:19.271029+00:00
---

Cisco Unified Intelligence Center Report Customization Guide, Release 12.5(1)

# Cisco Unified Intelligence Center Report Customization Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Permalinks

## Chapter: Permalinks

# Permalinks

## Variable
                        	 Parameters in a Permalink

You can apply
                           		variable parameters on the fields or on the display name of a field, and on the
                           		parameters.

Permalinks with filters specified in the URL (also known as Variable Permalinks) are by default authenticated for reports.
                                       You can uncheck the Authenticate Permalink > Variable check box to unauthenticate the variable permalink. Variable Permalinks do not support Excel and XML formats.

You must not
                                       		  include both fields and parameters at the same time in a permalink.

You can explicitly
                           		specify the filtering criteria by using either fields or parameters in a
                           		permalink to display the changed report data.

Format of the Parameters
                              		  and Fields in a Permalink

You can include
                           		variable parameters to the default permalink using the following format:

<variable_param_name> or <field
                           		name>=<operator><space><value><space><value>

<variable_param_name> can be either the field name or
                           		parameter name as configured in the report definition of the report.

<value> is any
                           		valid value for the configured field.

To include multiple
                           		variable parameters in a permalink URL, use an & (ampersand) between two
                           		variable parameters.

The permalink with
                                       		  the variable parameter is one single URL. Do not break it into different lines.
                                       		  In this example, the URL is broken to explain the concept of variable
                                       		  parameters. You can have a space only between an operator and a value.

### Parameters

You can apply the
                              		  variable parameters only on the parameter name for anonymous-block-based and
                              		  stored-procedure-based reports.

Parameters are
                              		  created from a stored procedure or an anonymous block.

This example
                                    				shows how you can include @start_date, @end_date, and @agent_list parameters to
                                    				change the report data shown by a default permalink based of the values that
                                    				are passed to these parameters.

//localhost:8444/cuicui/permalink/?

viewId=5BC22D1C1000013C61E3571D0A4E5AF5&linkType=htmlType&viewType=Grid

&@start_date=ABSDATE
                                       				  11-01-2012 00:00:00

&@end_date=ABSDATE
                                       				  01-21-2013 23:59:59

&@agent_list=14527,14537

### Fields

You can apply the
                              		  variable parameters on a field name or its display name for a
                              		  database-query-based report.

Fields are created
                              		  from a database query.

This example
                                       				  shows how you can include variable parameters to a permalink URL based on the
                                       				  fields EventTime and User to change the report data shown by a default
                                       				  permalink based of the values that are passed to these fields.

//localhost:8444/cuicui/permalink/?

viewId=5BC22D1C1000013C61E3571D0A4E5AF5&linkType=htmlType&viewType=Grid

&EventTime=ABSDATE
                                          					 11-01-2012 01-21-2013 00:00:00-23:59:59 MON,WED

&User=VL CUIC %5C administrator

The EventTime
                              		  field retrieves the report data based on the absolute date value ABSDATE
                                 			 11-01-2012 01-21-2013 00:00:00-23:59:59 MON,WED .

The User field retrieves the report data based on the value &User=VL CUIC %5C administrator .

& is the separator that separates two variable parameters.

User is the second field.

VL is the second operator that works on the values CUIC %5C administrator.

CUIC %5C administrator is the value that is passed to the User field.

## Supported Operators for Fields

This section describes the supported operators for fields in a permalink:

For all data types, after an operator, specify the field ID as the value. For example, if the ID of IPCC_1.2000001 filter
                           field is 1000, specify this ID in the variable permalink as &SkillTargetID=LIKE 1000.

Do not specify the field name as the value.

DECIMAL

Equal to

Not equal to

Less than

Less than or equal to

Greater than

Greater than or equal to

Between

&agents_logged_on=LEQ 9.0

STRING

Equal to

Not equal to

Matches the pattern

&agent_team_name=LIKE%20%25IPCC_1%25

Ensure to URL encode the special characters in variable permalinks.

DATETIME

RELATIVE DATE

ABSOLUTE DATE

&EventTime=RELDATE THISMONTH 09:00:00-23:59:00 MON,TUE,WED,THU,FRI

&DateTime=ABSDATE 12-31-2008 12-06-2012 09:00:00-23:59:00 MON,TUE,WED,THU,FRI

The following other operators can take more than two parameters depending on what you want to configure:

Format:

<date_type_param_name>=

<date_op><space><value_1>

<space><value_2><space><value_3>

Relative date values: Today, Yesterday, This Week, Last Week, This Month, Last Month, Year to Date, and Last Year

Can be any one of these: TODAY, YESTERDAY, THISWEEK, LASTWEEK, THISMONTH, LASTMONTH, YEARTODATE, and LASTYEAR.

Timestamp in 24 hour format indicating both start time and end time separated by a hyphen (-) hh:mm:ss-hh:mm:ss

Comma separated values indicating days of a week based on which the report data is retrieved. For example, MON,TUE,WED, and
                                          so on.

For example:

EventTime=RELDATE LASTMONTH 00:00:00-23:59:59 TUE,THU,SAT

You can have <Weekdays> only when you have <from_timestamp>-<to_timestamp>. When you configure days, you must always configure
                                       the timestamp. Example: EventTime=RELDATE LASTMONTH 00:00:00-23:59:59 TUE,THU,SAT

In case of RELDATE and ABSDATE, if weekdays are not provided to the <weekdays> parameter then the default value is used, that
                                       is, MON, TUE, WED, THU, FRI, SAT, and SUN.

Absolute date requires the following parameters:

Date in the format: MM-DD-YYY

Date in the format: MM-DD-YYY

Timestamp in 24 hour format indicating both start time and end time separated by a hyphen (-) hh:mm:ss-hh:mm:ss

Comma separated values indicating days of a week based on which the report data is retrieved. For example, MON,TUE,WED, and
                                          so on.

For example:

EventTime=ABSDATE 12-21-2012 01-07-2013 00:00:00-23:59:59 MON,TUE,WED

<from_date> and <to_date> are mandatory.

<from_timestamp> and <to_timestamp> are optional.

For all parameters that take boolean values, TRUE and FALSE are the valid values.

## Supported Operators for Parameters

RELDATE

It is the Relative date.

<value_1>

<value_1> can be any of the following:

TODAY, YESTERDAY, THISWEEK, LASTWEEK, THISMONTH, LASTMONTH, YEARTODATE, LASTYEAR

Option 1

@param1=RELDATE THISMONTH&@param2=RELDATE THISMONTH

For example:

@startDate=RELDATE THISMONTH&@endDate=RELDATE THISMONTH

Option 2:

@param1=RELDATE THISMONTH

For example:

@startDate=RELDATE THISMONTH

Option 3:

@param2=RELDATE THISMONTH

For example:

@endDate=RELDATE THISMONTH

<value_2>

Timestamp in hh:mm:ss format

For example:

@startDate=RELDATE TODAY 00:00:00

ABSDATE

It is the Absolute date.

<value_1>

date in the format: MM-DD-YYYY

<value_2>

Timestamp in hh:mm:ss format.

For example:

@endDate=ABSDATE 12-21-2012 01-07-2013 00:00:00-23:59:59 MON,TUE,WED

## Collections as Variables in Report Permalinks

You can use collection names as a variable parameter in a permalink provided you have the right permissions to the collections.

Permalinks with variable parameters are always authenticated irrespective of the check box Enable Unauthenticated Access being checked or not.

If you do not provide specific collection names after the =CL keyword, the report will be filtered using all the collections that the user has permissions for. The user in this case is
                                       the person using the permalink.

### Format of the Permalink URL as collection variable for SQL based Report Definition

Permalink URL&<field name>=CL<white space>Collection 1,Collection 2.

Example

https://localhost:8444/cuic/permalink/PermalinkViewer.htmx?

viewId=65FB26481000013F000000250A8E79F3&linkType=htmlType&viewType=Grid

&EventTime=RELDATE%20TODAY%2009:00:00-23:59:00&User=CL TestColl_FF_15201,TestColl_FF_7066

In the above URL, &User is the name of the field and TestColl_FF_15201 and TestColl_FF_7066 are collection names separated by commas.

### Format of the Permalink URL as collection variable for Stored Procedure or Anonymous Block Report Definition

Permalink URL&<parameter name>=CL<whitespace>Collection 1,Collection 2.

Example

https://localhost:8444/cuic/permalink/PermalinkViewer.htmx?

viewId=25DE58941000012E63BCDF340A591C3A&linkType=htmlType&viewType=Grid

&refreshRate=3600&@start_date=ABSDATE 05-03-2010 00:00:00&@end_date=ABSDATE 01-03-2014 23:59:00&@team_list=CL TestColl_FF_15201,TestColl_FF_7066

In the above URL, &@team_list is the name of the parameter and TestColl_FF_15201 and TestColl_FF_7066 are collection names separated by commas.

| Note | Permalinks with filters specified in the URL (also known as Variable Permalinks) are by default authenticated for reports.
                                       You can uncheck the Authenticate Permalink > Variable check box to unauthenticate the variable permalink. Variable Permalinks do not support Excel and XML formats. |
|---|---|

| Note | You must not
                                       		  include both fields and parameters at the same time in a permalink. |
|---|---|

| Note | The permalink with
                                       		  the variable parameter is one single URL. Do not break it into different lines.
                                       		  In this example, the URL is broken to explain the concept of variable
                                       		  parameters. You can have a space only between an operator and a value. |
|---|---|

| Note | Do not specify the field name as the value. |
|---|---|

| Data Type | Supported Operators | Example |
|---|---|---|
| DECIMAL | EQ Equal to NEQ Not equal to LT Less than LEQ Less than or equal to GT Greater than GEQ Greater than or equal to BTWN Between | &agents_logged_on=LEQ 9.0 |
| STRING | EQ Equal to NEQ Not equal to % Matches the pattern | &agent_team_name=LIKE%20%25IPCC_1%25 Note Ensure to URL encode the special characters in variable permalinks. | Note | Ensure to URL encode the special characters in variable permalinks. |
| Note | Ensure to URL encode the special characters in variable permalinks. |
| DATETIME | RELATIVE DATE ABSOLUTE DATE | Relative Date &EventTime=RELDATE THISMONTH 09:00:00-23:59:00 MON,TUE,WED,THU,FRI Absolute Date &DateTime=ABSDATE 12-31-2008 12-06-2012 09:00:00-23:59:00 MON,TUE,WED,THU,FRI |

| Note | Ensure to URL encode the special characters in variable permalinks. |
|---|---|

| Note | You can have <Weekdays> only when you have <from_timestamp>-<to_timestamp>. When you configure days, you must always configure
                                       the timestamp. Example: EventTime=RELDATE LASTMONTH 00:00:00-23:59:59 TUE,THU,SAT In case of RELDATE and ABSDATE, if weekdays are not provided to the <weekdays> parameter then the default value is used, that
                                       is, MON, TUE, WED, THU, FRI, SAT, and SUN. |
|---|---|

| Note | <from_date> and <to_date> are mandatory. <from_timestamp> and <to_timestamp> are optional. |
|---|---|

| Note | For all parameters that take boolean values, TRUE and FALSE are the valid values. |
|---|---|

| Operators | Values | Description | Example |
|---|---|---|---|
| RELDATE | It is the Relative date. |
| <value_1> | <value_1> can be any of the following: TODAY, YESTERDAY, THISWEEK, LASTWEEK, THISMONTH, LASTMONTH, YEARTODATE, LASTYEAR | Option 1 @param1=RELDATE THISMONTH&@param2=RELDATE THISMONTH For example: @startDate=RELDATE THISMONTH&@endDate=RELDATE THISMONTH Option 2: @param1=RELDATE THISMONTH For example: @startDate=RELDATE THISMONTH Option 3: @param2=RELDATE THISMONTH For example: @endDate=RELDATE THISMONTH |
| <value_2> | Timestamp in hh:mm:ss format | For example: @startDate=RELDATE TODAY 00:00:00 |
| ABSDATE | It is the Absolute date. |
| <value_1> | date in the format: MM-DD-YYYY |  |
| <value_2> | Timestamp in hh:mm:ss format. | For example: @endDate=ABSDATE 12-21-2012 01-07-2013 00:00:00-23:59:59 MON,TUE,WED |

| Note | Permalinks with variable parameters are always authenticated irrespective of the check box Enable Unauthenticated Access being checked or not. |
|---|---|

| Note | If you do not provide specific collection names after the =CL keyword, the report will be filtered using all the collections that the user has permissions for. The user in this case is
                                       the person using the permalink. |
|---|---|