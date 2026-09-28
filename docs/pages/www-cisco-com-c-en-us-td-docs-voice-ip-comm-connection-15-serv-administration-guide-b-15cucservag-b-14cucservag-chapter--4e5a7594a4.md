---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-serv-administration-guide-b-15cucservag-b-14cucservag-chapter--4e5a7594a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag/b_14cucservag_chapter_0101.html
retrieved_at: 2026-08-21T00:59:48.816628+00:00
---

Administration Guide for Cisco Unity Connection Serviceability Release 15

# Administration Guide for Cisco Unity Connection Serviceability Release 15

Updated: December 18, 2023

Chapter: Using Reports

## Chapter: Using Reports

# Using Reports

## Understanding
                        	 Reports

Cisco Unity Connection
                              		  Serviceability lets you gather information about system configuration and call
                              		  handlers into reports.

Table 6-1 describes the
                              		  reports that you can generate in Cisco Unity Connection Serviceability.

Report Name

Description of Output

Phone Interface Failed Logon

Includes the following information for every failed attempt to
                                          					 sign in to Unity Connection by phone:

Name of user, alias, caller ID, and extension of user who failed
                                                						  to sign in.

Date and time the failed logon occurred.

Whether the maximum number of failed sign-ins has been reached
                                                						  for the user.

Users

Includes the following information for each user:

Last name, first name, and alias.

Information that identifies the Unity Connection or Cisco
                                                						  Business Edition server associated with the user.

Billing ID, class of service, and extension.

Whether the account is locked.

Whether the user has enabled personal call transfer rules.

Message Traffic

Includes totals for the following traffic categories:

Voice.

Fax.

Email.

Non-delivery receipt (NDR).

Delivery receipt.

Read receipt.

Hourly totals.

Daily totals.

Port Activity

Includes the following information for voice messaging ports:

Name.

Number of inbound calls handled.

Number of outbound MWI calls handled.

Number of outbound AMIS calls handled.

Number of outbound notification calls handled.

Number of outbound TRaP calls handled.

Total number of calls handled.

Mailbox Store

Includes the following information about the specified mailbox
                                          					 stores:

Mail database name.

Display name.

Server name.

Whether access is enabled.

Mailbox store size.

Last error.

Status.

Whether the mail database can be deleted.

Dial Plan

Includes a list of the search spaces configured on the Unity
                                          					 Connection or Cisco Business Edition server, with an ordered list of partitions
                                          					 assigned to each search space.

If the server is part of a Digital Network, also lists the
                                          					 search spaces and associated partition membership on every other Unity
                                          					 Connection location on the network.

Dial Search Scope

Includes a list of all users and their extensions in the
                                          					 specified partition that is configured in the Unity Connection directory. If a
                                          					 partition is not specified, lists all users and their extensions for all
                                          					 partitions that are configured in the directory.

User Phone Login and MWI

Includes the following information about phone logins, MWI
                                          					 activity, and message notifications to phone devices per user:

Name, extension, and class of service.

Date and time for each activity.

The source of each activity.

Action completed (for example, Login, MWI On or Off, and Phone
                                                						  Dialout).

Dial out number and results (applicable only for message
                                                						  notifications to phone devices).

The number of new messages for a user at time of login.

User Message Activity

Includes the following information about messages sent and
                                          					 received, per user:

Name, extension, and class of service.

Date and time for each message.

Type of message.

Action completed (for example, new message, message saved, and
                                                						  so on).

Information on the message sender.

Distribution Lists

Includes the following information:

Name and display name of
                                                						  the list.

Date and time the list
                                                						  was created. (Date and time are given in Greenwich Mean Time.)

A count of the number of
                                                						  users included in the list.

If the Include List
                                                						  Members check box is checked, a listing of the alias of each user who is a
                                                						  member of the list.

User Lockout

Includes user alias, the number of failed logon attempts for the
                                          					 user, credential type (a result of “4” indicates a logon attempt from the Unity
                                          					 Connection conversation; a result of “3” indicates a logon attempt from a web
                                          					 application), and the date and time that the account was locked.

(Date and time are given in Greenwich Mean Time.)

Unused Voicemail  Accounts

Includes user alias and display name, and the date and time that
                                          					 the user account was created.

(Date and time are given in Greenwich Mean Time.)

Transfer Call Billing

Includes the following information for each call:

Name, extension, and
                                                						  billing ID of the user.

Date and time that the
                                                						  call occurred.

The phone number dialed.

The result of the
                                                						  transfer (connected, ring-no-answer (RNA), busy, or unknown).

Outcall Billing Detail

Includes the following information, arranged by day and by the
                                          					 extension of the user who placed the call:

Name, extension, and
                                                						  billing ID.

Date and time the call
                                                						  was placed.

The phone number called.

The result of the call
                                                						  (connected, ring-no-answer (RNA), busy, or unknown).

The duration of the call
                                                						  in seconds.

Outcall Billing Summary

Arranged by date and according to the name, extension, and
                                          					 billing ID of the user who placed the call, and is a listing of the 24 hours of
                                          					 the day, with a dialout time in seconds specified for each hour span.

Call Handler  Traffic

Includes the following information for each call handler, in
                                          					 rows for each hour of a day:

Total number of calls.

Number of times each key
                                                						  on the phone keypad was pressed.

Extension.

Invalid extension.

Number of times the after
                                                						  greeting action occurred.

Number of times the
                                                						  caller hung up.

System Configuration

Includes detailed information about all aspects of the
                                          					 configuration of the Unity Connection system.

SpeechView Activity Report By User

Includes the total number of transcribed messages, failed
                                          					 transcriptions, and truncated transcriptions for a given user during a given
                                          					 time period. If the report is run for all users, then the output is broken out
                                          					 by user.

SpeechView Activity Summary Report

Includes the total number of transcribed messages, failed
                                          					 transcriptions, and truncated transcriptions for the entire system during a
                                          					 given time period. When messages are sent to multiple recipients, the message
                                          					 is transcribed only once, so the transcription activity is counted only once.

HTTPS Networking Sync Error Report

(Applicable only for HTTPS Networking) Includes the following
                                          					 information associated with the directory objects that does not synchronize
                                          					 during directory synchronization:

Creation Date

Failed ObjectId

USN

Object Type

Location Display Name

HTTP(S) Link

Error Message

## Setting Report Configuration Parameters

Cisco Unity Connection is automatically set to gather and store data from which you can generate reports. The parameters listed
                           in this section can be adjusted, depending on the report output that you want to generate. All report parameter settings are
                           found on the System Settings > Advanced > Reports page in Cisco Unity Connection Administration.

Reports data is gradually written over, depending on the parameters you set for retention of data. We recommend that if you
                           want to keep reports for historical purposes, you develop a schedule for regularly generating reports, and save them in a
                           location separate from the Unity Connection or Cisco Business Edition server.

Milliseconds Between Data Collection Cycles —Set by default to 30 minutes (1,800,000 milliseconds). This setting controls the amount of time Unity Connection waits between
                                 cycles of gathering report data.

Days to Keep Data in Reports Database —Set by default to 180 days. Note that even if you specify more than this number of days in the time range for the report
                                 you are generating, the number of days of data is limited by what you set here.

Maximum Records in Report Output —Set by default to 25,000 records. The maximum value allowed for this field is 30,000 records. If the report you want to generate
                                 exceeds the maximum number of records allowed, you can generate the report in pieces (for example by reducing the date range
                                 or number of user accounts included in each iteration).

The Maximum Records in Report Output setting for the User Message Activity Report has been restricted to 15,000 records—rather
                                             than the default of 25,000 records—because of the size of the report.

Minimum Records Needed to Display Progress Indicator —Set by default to 2,500 records. The maximum value allowed for this field is 10,000 records. The purpose of the progress
                                 indicator is to warn you if the report you request is large and likely to take a long time to complete. In Unity Connection,
                                 reports are generated from within a browser, and the browser session must be kept open while the report is being generated.
                                 Depending on the size of the database, and the type of report being generated, a report can take a long time to generate;
                                 meanwhile, you are unable to use the browser, and must keep the Connection Administration session open.

## Generating and
                        	 Viewing Reports

When you generate a report, you can specify some
                           		or all of the following:

The objects (for example, user accounts or call handlers) to
                                 			 include in the report.

The date and time range to include.

The sort order for the data in the report.

You can select one of the following file formats for the report:

Web page

HTML file. Report output appears in your web browser.

Select this format to quickly view a small report.

For archiving purposes, we recommend that you generate PDF
                                       					 reports.

Comma-delimited file

Text file (also known as a comma-separated, or CSV, file).
                                       					 Report output appears as a string of data, separated by commas.

Select this format if you want to view or print the information
                                       					 in another application, for example, a spreadsheet application.

PDF file

Report output appears as a PDF that can be printed and saved.

We recommend that you select this format if you plan to archive
                                       					 reports.

The best time to generate reports is when the system is not
                           		busy: after regular business hours when Unity Connection is not processing many
                           		calls, or when there are no other processes running (for example, before or
                           		after a full backup). Requests to generate reports are queued. If multiple
                           		reports are generated at one time (from separate browsers), the reports wait in
                           		line and only one is processed at a time.

Caution

Generating large reports when the system is busy uses system
                                       		  resources and could potentially result in slower response time for system
                                       		  users.

Note that reports cannot be scheduled in advance. If you shut
                           		down the Unity Connection or Cisco Business Edition server, or close the
                           		Connection Administration browser session while reports are being generated,
                           		the report generation is canceled.

### Generating and View a Report

Step 1

In Cisco Unity Connection Serviceability,
                                          			 select Tools > Reports .

Step 2

On the Serviceability Reports page, select
                                          			 the name of the report that you want to generate.

Step 3

Select the applicable file format for the
                                          			 report output.

Step 4

If the fields are available, set a date
                                          			 range by selecting the beginning and ending month, day, year, and time.

Step 5

Set other parameters, as applicable.

Step 6

Select Generate Report .

Step 7

View the report output, depending on the
                                          			 file format you select in Step 3 :

Web Page

Output appears in your browser
                                                         							 window.

Comma-delimited File

File download dialog box opens,
                                                         							 asking if you want to open or save the file.

PDF File

File download dialog box opens,
                                                         							 asking if you want to open or save the file.

| Report Name | Description of Output |
|---|---|
| Phone Interface Failed Logon | Includes the following information for every failed attempt to
                                          					 sign in to Unity Connection by phone: Name of user, alias, caller ID, and extension of user who failed
                                                						  to sign in. Date and time the failed logon occurred. Whether the maximum number of failed sign-ins has been reached
                                                						  for the user. |
| Users | Includes the following information for each user: Last name, first name, and alias. Information that identifies the Unity Connection or Cisco
                                                						  Business Edition server associated with the user. Billing ID, class of service, and extension. Whether the account is locked. Whether the user has enabled personal call transfer rules. |
| Message Traffic | Includes totals for the following traffic categories: Voice. Fax. Email. Non-delivery receipt (NDR). Delivery receipt. Read receipt. Hourly totals. Daily totals. |
| Port Activity | Includes the following information for voice messaging ports: Name. Number of inbound calls handled. Number of outbound MWI calls handled. Number of outbound AMIS calls handled. Number of outbound notification calls handled. Number of outbound TRaP calls handled. Total number of calls handled. |
| Mailbox Store | Includes the following information about the specified mailbox
                                          					 stores: Mail database name. Display name. Server name. Whether access is enabled. Mailbox store size. Last error. Status. Whether the mail database can be deleted. |
| Dial Plan | Includes a list of the search spaces configured on the Unity
                                          					 Connection or Cisco Business Edition server, with an ordered list of partitions
                                          					 assigned to each search space. If the server is part of a Digital Network, also lists the
                                          					 search spaces and associated partition membership on every other Unity
                                          					 Connection location on the network. |
| Dial Search Scope | Includes a list of all users and their extensions in the
                                          					 specified partition that is configured in the Unity Connection directory. If a
                                          					 partition is not specified, lists all users and their extensions for all
                                          					 partitions that are configured in the directory. |
| User Phone Login and MWI | Includes the following information about phone logins, MWI
                                          					 activity, and message notifications to phone devices per user: Name, extension, and class of service. Date and time for each activity. The source of each activity. Action completed (for example, Login, MWI On or Off, and Phone
                                                						  Dialout). Dial out number and results (applicable only for message
                                                						  notifications to phone devices). The number of new messages for a user at time of login. |
| User Message Activity | Includes the following information about messages sent and
                                          					 received, per user: Name, extension, and class of service. Date and time for each message. Type of message. Action completed (for example, new message, message saved, and
                                                						  so on). Information on the message sender. |
| Distribution Lists | Includes the following information: Name and display name of
                                                						  the list. Date and time the list
                                                						  was created. (Date and time are given in Greenwich Mean Time.) A count of the number of
                                                						  users included in the list. If the Include List
                                                						  Members check box is checked, a listing of the alias of each user who is a
                                                						  member of the list. |
| User Lockout | Includes user alias, the number of failed logon attempts for the
                                          					 user, credential type (a result of “4” indicates a logon attempt from the Unity
                                          					 Connection conversation; a result of “3” indicates a logon attempt from a web
                                          					 application), and the date and time that the account was locked. (Date and time are given in Greenwich Mean Time.) |
| Unused Voicemail  Accounts | Includes user alias and display name, and the date and time that
                                          					 the user account was created. (Date and time are given in Greenwich Mean Time.) |
| Transfer Call Billing | Includes the following information for each call: Name, extension, and
                                                						  billing ID of the user. Date and time that the
                                                						  call occurred. The phone number dialed. The result of the
                                                						  transfer (connected, ring-no-answer (RNA), busy, or unknown). |
| Outcall Billing Detail | Includes the following information, arranged by day and by the
                                          					 extension of the user who placed the call: Name, extension, and
                                                						  billing ID. Date and time the call
                                                						  was placed. The phone number called. The result of the call
                                                						  (connected, ring-no-answer (RNA), busy, or unknown). The duration of the call
                                                						  in seconds. |
| Outcall Billing Summary | Arranged by date and according to the name, extension, and
                                          					 billing ID of the user who placed the call, and is a listing of the 24 hours of
                                          					 the day, with a dialout time in seconds specified for each hour span. |
| Call Handler  Traffic | Includes the following information for each call handler, in
                                          					 rows for each hour of a day: Total number of calls. Number of times each key
                                                						  on the phone keypad was pressed. Extension. Invalid extension. Number of times the after
                                                						  greeting action occurred. Number of times the
                                                						  caller hung up. |
| System Configuration | Includes detailed information about all aspects of the
                                          					 configuration of the Unity Connection system. |
| SpeechView Activity Report By User | Includes the total number of transcribed messages, failed
                                          					 transcriptions, and truncated transcriptions for a given user during a given
                                          					 time period. If the report is run for all users, then the output is broken out
                                          					 by user. |
| SpeechView Activity Summary Report | Includes the total number of transcribed messages, failed
                                          					 transcriptions, and truncated transcriptions for the entire system during a
                                          					 given time period. When messages are sent to multiple recipients, the message
                                          					 is transcribed only once, so the transcription activity is counted only once. |
| HTTPS Networking Sync Error Report | (Applicable only for HTTPS Networking) Includes the following
                                          					 information associated with the directory objects that does not synchronize
                                          					 during directory synchronization: Creation Date Failed ObjectId USN Object Type Location Display Name HTTP(S) Link Error Message |

| Note | The Maximum Records in Report Output setting for the User Message Activity Report has been restricted to 15,000 records—rather
                                             than the default of 25,000 records—because of the size of the report. |
|---|---|

| Web page | HTML file. Report output appears in your web browser. Select this format to quickly view a small report. For archiving purposes, we recommend that you generate PDF
                                       					 reports. |
|---|---|
| Comma-delimited file | Text file (also known as a comma-separated, or CSV, file).
                                       					 Report output appears as a string of data, separated by commas. Select this format if you want to view or print the information
                                       					 in another application, for example, a spreadsheet application. |
| PDF file | Report output appears as a PDF that can be printed and saved. We recommend that you select this format if you plan to archive
                                       					 reports. |

| Note | A " Checksum (SHA512) for Generated PDF or CSV Report " link
                                       		  appears at the end of the page. After clicking the link, the SHA-512 checksum
                                       		  value is displayed for the report to check the integrity of the file. |
|---|---|

| Caution | Generating large reports when the system is busy uses system
                                       		  resources and could potentially result in slower response time for system
                                       		  users. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability,
                                          			 select Tools > Reports . |
|---|---|
| Step 2 | On the Serviceability Reports page, select
                                          			 the name of the report that you want to generate. |
| Step 3 | Select the applicable file format for the
                                          			 report output. |
| Step 4 | If the fields are available, set a date
                                          			 range by selecting the beginning and ending month, day, year, and time. |
| Step 5 | Set other parameters, as applicable. |
| Step 6 | Select Generate Report . |
| Step 7 | View the report output, depending on the
                                          			 file format you select in Step 3 : Web Page Output appears in your browser
                                                         							 window. Comma-delimited File File download dialog box opens,
                                                         							 asking if you want to open or save the file. PDF File File download dialog box opens,
                                                         							 asking if you want to open or save the file. | Web Page | Output appears in your browser
                                                         							 window. | Comma-delimited File | File download dialog box opens,
                                                         							 asking if you want to open or save the file. | PDF File | File download dialog box opens,
                                                         							 asking if you want to open or save the file. |
| Web Page | Output appears in your browser
                                                         							 window. |
| Comma-delimited File | File download dialog box opens,
                                                         							 asking if you want to open or save the file. |
| PDF File | File download dialog box opens,
                                                         							 asking if you want to open or save the file. |

| Web Page | Output appears in your browser
                                                         							 window. |
|---|---|
| Comma-delimited File | File download dialog box opens,
                                                         							 asking if you want to open or save the file. |
| PDF File | File download dialog box opens,
                                                         							 asking if you want to open or save the file. |