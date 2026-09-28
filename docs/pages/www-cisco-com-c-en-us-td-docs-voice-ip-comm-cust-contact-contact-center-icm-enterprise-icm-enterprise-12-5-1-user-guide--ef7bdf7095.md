---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--ef7bdf7095
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_125-outbound-option-guide/ucce_b_125-outbound-option-guide-for_appendix_01011.html
retrieved_at: 2026-08-16T20:40:58.189991+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.5(1)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.5(1)

Updated: August 22, 2023

Chapter: Personal Callback List Table

## Chapter: Personal Callback List Table

- Personal Callback List Table

- Personal_Callback_List Table

# Personal Callback List Table

## Personal_Callback_List Table

The following table
                              		  documents all the columns in the personal callback table.

If Outbound Option High Availability is enabled, you must use the Personal_Callback API to insert data into the Personal_Calback_List
                                          table.

Column Name

Type

Description

PersonalCallbackListID

IDENTITY

Unique identifier for each record in this table. The identity
                                          					 seed value on side A is (1,1) and on side B is (-2147483648, 1)

DialingListID

INT

Cross-references a record that has been moved from the
                                          					 contact_list to this table.

CampaignID

INT

Campaign ID
                                          					 (if the record was originally dialed as part of a campaign).

PeripheralID

INT

Peripheral
                                          					 ID for the peripheral where the agent would be available.

AgentID

INT

Agent to
                                          					 which the call has to be connected.

CampaignDN

VARCHAR

Dialed number (DN) to use (if the original agent is unavailable).
                                          									Length is 12.

GMTZone

SMALLINT

GMT of the
                                          					 customer number (if NULL, the local GMT zone is assumed). If this value is
                                          					 provided, it must always be a positive value from 0 to 23. Convert all negative
                                          					 GMT values using the following formula: 24 + (negative GMT value). For example,
                                          					 the US eastern time zone is –5, so the value stored in this column is 24 + (-5)
                                          					 = 19.

This column is not currently
                                          					 being used. It is reserved for future use.

Phone

VARCHAR

Phone number to call back. Length is 20.

AccountNumber

VARCHAR

Customer account number. Length is 32.

MaxAttempts

INT

Maximum
                                          					 number of times a call is attempted (decrements at each attempt). An "attempt" is defined as the Outbound Option Dialer’s attempt
                                          					 to reserve the agent and make the customer call. Since the Outbound Option
                                          					 Dialer places multiple customer call attempts (busy, no answer), the actual
                                          					 individual call attempts are not tracked here; only the result at the end of
                                          					 the callback time range.

CallbackDateTime

DATETIME

Time to
                                          					 attempt customer callback is normalized to the logger GMT zone; for example, if
                                          					 the Campaign Manager is in Boston and the customer is in California and wished
                                          					 to be contacted at 3:00 PM, the time in this column would be 6:00 PM.

NULL columns will be allowed for the single agent campaigns

CallStatus

CHAR

Current
                                          					 status of the callback record, such as 'P' for pending or 'C' for closed.

CallResult

SMALLINT

Telephony
                                          					 call result (busy, no answer, and so on) or agent reservation attempt result
                                          					 (Agent Rejected Call, Unable to reserve, and so on).

LastName

CHAR

Last name of the customer. Length is 50.

FirstName

CHAR

First name of the customer. Length is 50.

InsertedIntoDBDateTime

DATETIME

The date and
                                          					 time that the personal callback record was inserted into the database.

SentToDialerDateTime

DATETIME

The date and
                                          					 time that the personal callback record was sent to the dialer and inserted into
                                          					 the dialer cache for processing.

| Note | If Outbound Option High Availability is enabled, you must use the Personal_Callback API to insert data into the Personal_Calback_List
                                          table. |
|---|---|

| Column Name | Type | Description |
|---|---|---|
| PersonalCallbackListID | IDENTITY | Unique identifier for each record in this table. The identity
                                          					 seed value on side A is (1,1) and on side B is (-2147483648, 1) |
| DialingListID | INT | Cross-references a record that has been moved from the
                                          					 contact_list to this table. |
| CampaignID | INT | Campaign ID
                                          					 (if the record was originally dialed as part of a campaign). |
| PeripheralID | INT | Peripheral
                                          					 ID for the peripheral where the agent would be available. |
| AgentID | INT | Agent to
                                          					 which the call has to be connected. |
| CampaignDN | VARCHAR | Dialed number (DN) to use (if the original agent is unavailable).
                                          									Length is 12. |
| GMTZone | SMALLINT | GMT of the
                                          					 customer number (if NULL, the local GMT zone is assumed). If this value is
                                          					 provided, it must always be a positive value from 0 to 23. Convert all negative
                                          					 GMT values using the following formula: 24 + (negative GMT value). For example,
                                          					 the US eastern time zone is –5, so the value stored in this column is 24 + (-5)
                                          					 = 19. This column is not currently
                                          					 being used. It is reserved for future use. |
| Phone | VARCHAR | Phone number to call back. Length is 20. |
| AccountNumber | VARCHAR | Customer account number. Length is 32. |
| MaxAttempts | INT | Maximum
                                          					 number of times a call is attempted (decrements at each attempt). An "attempt" is defined as the Outbound Option Dialer’s attempt
                                          					 to reserve the agent and make the customer call. Since the Outbound Option
                                          					 Dialer places multiple customer call attempts (busy, no answer), the actual
                                          					 individual call attempts are not tracked here; only the result at the end of
                                          					 the callback time range. Note Once this
                                                   					 column is set to 0, no more attempts are made. | Note | Once this
                                                   					 column is set to 0, no more attempts are made. |
| Note | Once this
                                                   					 column is set to 0, no more attempts are made. |
| CallbackDateTime | DATETIME | Time to
                                          					 attempt customer callback is normalized to the logger GMT zone; for example, if
                                          					 the Campaign Manager is in Boston and the customer is in California and wished
                                          					 to be contacted at 3:00 PM, the time in this column would be 6:00 PM. NULL columns will be allowed for the single agent campaigns |
| CallStatus | CHAR | Current
                                          					 status of the callback record, such as 'P' for pending or 'C' for closed. Note New
                                                   					 records must be set to 'P.' | Note | New
                                                   					 records must be set to 'P.' |
| Note | New
                                                   					 records must be set to 'P.' |
| CallResult | SMALLINT | Telephony
                                          					 call result (busy, no answer, and so on) or agent reservation attempt result
                                          					 (Agent Rejected Call, Unable to reserve, and so on). |
| LastName | CHAR | Last name of the customer. Length is 50. |
| FirstName | CHAR | First name of the customer. Length is 50. |
| InsertedIntoDBDateTime | DATETIME | The date and
                                          					 time that the personal callback record was inserted into the database. Note The
                                                   					 Campaign Manager sets this value when an agent schedules a personal callback.
                                                   					 Customers, partners, or 3rd-party applications that insert new records into
                                                   					 this table must populate the InsertedIntoDBDateTime column with the current
                                                   					 date and time. | Note | The
                                                   					 Campaign Manager sets this value when an agent schedules a personal callback.
                                                   					 Customers, partners, or 3rd-party applications that insert new records into
                                                   					 this table must populate the InsertedIntoDBDateTime column with the current
                                                   					 date and time. |
| Note | The
                                                   					 Campaign Manager sets this value when an agent schedules a personal callback.
                                                   					 Customers, partners, or 3rd-party applications that insert new records into
                                                   					 this table must populate the InsertedIntoDBDateTime column with the current
                                                   					 date and time. |
| SentToDialerDateTime | DATETIME | The date and
                                          					 time that the personal callback record was sent to the dialer and inserted into
                                          					 the dialer cache for processing. Note This date
                                                   					 and time is set by the Campaign Manager. Do not modify this value. | Note | This date
                                                   					 and time is set by the Campaign Manager. Do not modify this value. |
| Note | This date
                                                   					 and time is set by the Campaign Manager. Do not modify this value. |

| Note | Once this
                                                   					 column is set to 0, no more attempts are made. |
|---|---|

| Note | New
                                                   					 records must be set to 'P.' |
|---|---|

| Note | The
                                                   					 Campaign Manager sets this value when an agent schedules a personal callback.
                                                   					 Customers, partners, or 3rd-party applications that insert new records into
                                                   					 this table must populate the InsertedIntoDBDateTime column with the current
                                                   					 date and time. |
|---|---|

| Note | This date
                                                   					 and time is set by the Campaign Manager. Do not modify this value. |
|---|---|