---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-ucce-b-3d844e4195
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/ucce_b_150_outbound-option-guide-for-unified/dialing_list_table.html
retrieved_at: 2026-08-16T20:35:52.145754+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 15.0(1)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Dialing List Table

## Chapter: Dialing List Table

- Dialing List Table

- Dialing_List Table                              	 Columns

# Dialing List Table

## Dialing_List Table
                        	 Columns

The following table
                              		  displays the Dialing_List table column names and their description.

Column Name

Type

Description

Phone01
                                          					 through Phone10

VARCHAR20

PhoneExt01
                                          					 through PhoneExt10

VARCHAR8

The phone number extensions imported into PhoneExt01 through PhoneExt10 standard column.

Although the phone number extensions are imported into the table, they are currently not used for any dialing operations.

CallbackNumber

VARCHAR20

Phone number to be used for a regular callback it can be supplied by the agent.

CallResult

SMALLINT

The call
                                          					 result from the last call placed for this record (see Call Result definitions).

CallResult01
                                          					 through CallResult10

SMALLINT

The call result from the last time Phone01through Phone10 was called (see Call Result definitions). CallResult01 captures
                                          the results of all requested regular callback calls for Phone01 to Phone10.

DialingList ID

IDENTITY

Unique identifier for each record in this table. The identity seed value on Side A is (1,1) and on Side B is (-2147483648,
                                          1).

LastZoneDialed

SMALLINT

The last zone that was dialed (0 indicates zone1, 1 indicates zone2).

LastNumberDialedZone1

SMALLINT

The last
                                          					 number dialed in zone1 (1 for phone01, 2 for phone02, and so on)

LastNumberDialedZone2

SMALLINT

The last
                                          					 number dialed in zone2 (1 for phone01, 2 for phone02, and so on)

CallsMadeToZone1

SMALLINT

The number
                                          					 of calls made to numbers in zone 1

CallsMadeToZone2

SMALLINT

The number
                                          					 of calls made to numbers in zone 2

CallbackDateTimeZone1

DATETIME

The date or time when the next call to this zone will occur.

CallbackDateTimeZone2

DATETIME

The number of calls made to numbers in zone 2.

CallbackDateTime01 through CallbackDateTime010

DATETIME

The date or time when the next call to this phone number will occur.

GMTPhone01
                                          					 through GMTPhone10

SMALLINT

The time zone where this phone number is located.

DSTPhone01
                                          					 through DSTPhone10

SMALLINT

Is DST
                                          					 observed at this phone number (boolean).

CallStatusZone1 and CallStatusZone2

CHAR(1)

The call status (pending, retry, callback, and so forth) for this zone.

AccountNumber

VARCHAR30

The account number of the customer.

LastName

VARCHAR50

The last name of the customer.

FirstName

VARCHAR50

The first name of the customer.

ImportRuleDate

DATETIME

The date or time when the record was imported.

| Column Name | Type | Description |
|---|---|---|
| Phone01
                                          					 through Phone10 | VARCHAR20 | The phone number imported into Phone01 through Phone 10 standard column. |
| PhoneExt01
                                          					 through PhoneExt10 | VARCHAR8 | The phone number extensions imported into PhoneExt01 through PhoneExt10 standard column. Note Although the phone number extensions are imported into the table, they are currently not used for any dialing operations. | Note | Although the phone number extensions are imported into the table, they are currently not used for any dialing operations. |
| Note | Although the phone number extensions are imported into the table, they are currently not used for any dialing operations. |
| CallbackNumber | VARCHAR20 | Phone number to be used for a regular callback it can be supplied by the agent. |
| CallResult | SMALLINT | The call
                                          					 result from the last call placed for this record (see Call Result definitions). |
| CallResult01
                                          					 through CallResult10 | SMALLINT | The call result from the last time Phone01through Phone10 was called (see Call Result definitions). CallResult01 captures
                                          the results of all requested regular callback calls for Phone01 to Phone10. |
| DialingList ID | IDENTITY | Unique identifier for each record in this table. The identity seed value on Side A is (1,1) and on Side B is (-2147483648,
                                          1). |
| LastZoneDialed | SMALLINT | The last zone that was dialed (0 indicates zone1, 1 indicates zone2). |
| LastNumberDialedZone1 | SMALLINT | The last
                                          					 number dialed in zone1 (1 for phone01, 2 for phone02, and so on) |
| LastNumberDialedZone2 | SMALLINT | The last
                                          					 number dialed in zone2 (1 for phone01, 2 for phone02, and so on) |
| CallsMadeToZone1 | SMALLINT | The number
                                          					 of calls made to numbers in zone 1 Note For a call which an Outbound Option Agent has scheduled a callback, the CallResult resets to 0. | Note | For a call which an Outbound Option Agent has scheduled a callback, the CallResult resets to 0. |
| Note | For a call which an Outbound Option Agent has scheduled a callback, the CallResult resets to 0. |
| CallsMadeToZone2 | SMALLINT | The number
                                          					 of calls made to numbers in zone 2 Note For a call which an Outbound Option Agent has scheduled a callback, the CallResult resets to 0. | Note | For a call which an Outbound Option Agent has scheduled a callback, the CallResult resets to 0. |
| Note | For a call which an Outbound Option Agent has scheduled a callback, the CallResult resets to 0. |
| CallbackDateTimeZone1 | DATETIME | The date or time when the next call to this zone will occur. |
| CallbackDateTimeZone2 | DATETIME | The number of calls made to numbers in zone 2. |
| CallbackDateTime01 through CallbackDateTime010 | DATETIME | The date or time when the next call to this phone number will occur. |
| GMTPhone01
                                          					 through GMTPhone10 | SMALLINT | The time zone where this phone number is located. |
| DSTPhone01
                                          					 through DSTPhone10 | SMALLINT | Is DST
                                          					 observed at this phone number (boolean). |
| CallStatusZone1 and CallStatusZone2 | CHAR(1) | The call status (pending, retry, callback, and so forth) for this zone. |
| AccountNumber | VARCHAR30 | The account number of the customer. |
| LastName | VARCHAR50 | The last name of the customer. |
| FirstName | VARCHAR50 | The first name of the customer. |
| ImportRuleDate | DATETIME | The date or time when the record was imported. |

| Note | Although the phone number extensions are imported into the table, they are currently not used for any dialing operations. |
|---|---|

| Note | For a call which an Outbound Option Agent has scheduled a callback, the CallResult resets to 0. |
|---|---|

| Note | For a call which an Outbound Option Agent has scheduled a callback, the CallResult resets to 0. |
|---|---|