---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-user-guide-ccvp-b-1-b9a62d2dfd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/user/guide/ccvp_b_1262-user-guide-for-cisco-unified-cvp-vxml-server-and-call-studio/ccvp_b_1251-user-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio-release-1251_appendix_01001.html
retrieved_at: 2026-08-21T17:41:20.477171+00:00
---

User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio Release 12.6(2)

# User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio Release 12.6(2)

Updated: April 28, 2023

Chapter: Substitution Tag
	 Reference

## Chapter: Substitution Tag
	 Reference

- Substitution Tag                              	 Reference

# Substitution Tag
                     	 Reference

The following table
                        		lists the contents of tags used for setting value substitution. To represent
                        		each of the data values, the tag is rendered with braces containing the tag
                        		content listed and is case sensitive. The fragments rendered bold represent
                        		values replaced by the application designer. Optional information is enclosed
                        		in brackets ([]).

Tag Content

Description

CallData.ANI

The ANI of the
                                    				current call or NA if not sent.

CallData.DNIS

The DNIS of the
                                    				current call or NA if not sent.

CallData.UUI

The UUI of the
                                    				current call or NA if not sent.

CallData.IIDIGITS

The IIDIGITS of
                                    				the current call or NA if not sent.

CallData.SOURCE

The name of the
                                    				application that transferred to this one.

CallData.APP_NAME

The name of the
                                    				current application.

CallData.DURATION

The duration, in
                                    				seconds, of the call up to this point.

CallData.LANGUAGE

The language for
                                    				the application, up to this point in the call.

CallData.ENCODING

The VoiceXML
                                    				encoding for the application, up to this point in the call.

Data.Session. VAR

The value of
                                    				Session Data where VAR represents the name of the session variable. The object
                                    				stored there will be represented as a string.

Data.Element. ELEMENT.VAR

The value of
                                    				Element Data where ELEMENT represents the name of the element and VAR
                                    				represents the name of the element variable.

Data.Session.lastException.type

The type of
                                    				the last exception occurred.

Data.Session.lastException.code

This is the
                                    				exception code for the last exception occurred.

Data.Session.lastException.message

The message of
                                    				the last exception.

Data.Session.lastException.custom_field1, custom_field2, and
                                    				custom_field3

This is the
                                    				user-defined fields of the last exception.

CallerActivity.NthElement. N

The name of a
                                    				certain element visited in the call where N represents the number for the nth
                                    				element.

CallerActivity.NthExitState. N

The name of a
                                    				certain element’s exit state visited in the call where N represents the number
                                    				for the nth element.

CallerActivity.TimesElementVisited. ELEMENT

The number of
                                    				times an element was visited in the call where ELEMENT represents the name of
                                    				the element.

CallerActivity.imesElementVisitedExitState. ELEMENT.EXIT_STATE

The number of
                                    				times an element was visited in the call with a particular exit state where
                                    				ELEMENT is the name of the element and EXIT_STATE is the exit state.

GeneralDateTime.HourOfDay.CURRENT

The current
                                    				hour.

GeneralDateTime.HourOfDay.CALL_START

The hour the
                                    				call started.

GeneralDateTime.Minute.CURRENT

The current
                                    				minute.

GeneralDateTime.Minute.CALL_START

The minute the
                                    				call started.

GeneralDateTime.DayOfMonth.CURRENT

The current day
                                    				of the month.

GeneralDateTime.DayOfMonth.CALL_START

The day of the
                                    				month the call started.

GeneralDateTime.Month.CURRENT

The current
                                    				month.

GeneralDateTime.Month.CALL_START

The month the
                                    				call started.

GeneralDateTime.DayOfWeek.CURRENT

The current day
                                    				of the week.

GeneralDateTime.DayOfWeek.CALL_START

The day of the
                                    				week the call started.

GeneralDateTime.Year.CURRENT

The current
                                    				year.

GeneralDateTime.Year.CALL_START

The year the
                                    				call started.

The following tags
                        		will cause an error if the User Management System is inactive. Additionally,
                        		these tags relate to the current user and will cause an error unless the call
                        		is linked to a UID.

Tag

Description

UserInfo.Demographic.NAME

The name of
                                    				the current user.

UserInfo.Demographic.ZIP_CODE

The zip code
                                    				of the current user.

UserInfo.Demographic.BIRTHDAY

The birthday
                                    				of the current user.

UserInfo.Demographic.GENDER

The gender of
                                    				the current user.

UserInfo.Demographic.SSN

The social
                                    				security number of the current user.

UserInfo.Demographic.COUNTRY

The country of
                                    				the current user.

UserInfo.Demographic.LANGUAGE

The language
                                    				of the current user.

UserInfo.Demographic.CUSTOM1

The contents
                                    				of the first custom column of the current user.

UserInfo.Demographic.CUSTOM2

The contents
                                    				of the second custom column of the current user.

UserInfo.Demographic.CUSTOM3

The contents
                                    				of the third custom column of the current user.

UserInfo.Demographic.CUSTOM4

The contents
                                    				of the fourth custom column of the current user.

UserInfo.AniInfo.FIRST

The first
                                    				phone number associated with the current user’s account.

UserInfo.AniInfo.NUM_DIFF

The total
                                    				number of different phone numbers associated with the current user’s account.

UserInfo.UserDateTime.HourOfDay. LAST_MODIFIED

The hour of
                                    				the last time the current user’s account was modified.

UserInfo.UserDateTime.HourOfDay. CREATION

The hour of
                                    				the last time the current user’s account was created.

UserInfo.UserDateTime.HourOfDay. LAST_CALL

The hour of
                                    				the last time the current user called.

UserInfo.UserDateTime.Minute. LAST_MODIFIED

The minute of
                                    				the last time the current user’s account was modified.

UserInfo.UserDateTime.Minute.CREATION

The minute of
                                    				the last time the current user’s account was created.

UserInfo.UserDateTime.Minute. LAST_CALL

The minute of
                                    				the last time the current user called.

UserInfo.UserDateTime.DayOfMonth. LAST_MODIFIED

The day of the
                                    				month of the last time the current user’s account was modified.

UserInfo.UserDateTime.DayOfMonth. CREATION

The day of the
                                    				month of the last time the current user’s account was created.

UserInfo.UserDateTime.DayOfMonth. LAST_CALL

The day of the
                                    				month of the last time the current user called.

UserInfo.UserDateTime.Month. LAST_MODIFIED

The month of
                                    				the last time the current user’s account was modified.

UserInfo.UserDateTime.Month.CREATION

The month of
                                    				the last time the current user’s account was created.

UserInfo.UserDateTime.Month.LAST_CALL

The month of
                                    				the last time the current user called.

UserInfo.UserDateTime.DayOfWeek. LAST_MODIFIED

The day of the
                                    				week of the last time the current user’s account was modified.

UserInfo.UserDateTime.DayOfWeek. CREATION

The day of the
                                    				week of the last time the current user’s account was created.

UserInfo.UserDateTime.DayOfWeek. LAST_CALL

The day of the
                                    				week of the last time the current user called.

UserInfo.UserDateTime.Year. LAST_MODIFIED

The year of
                                    				the last time the current user’s account was modified.

UserInfo.UserDateTime.Year.CREATION

The year of
                                    				the last time the current user’s account was created.

UserInfo.UserDateTime.Year.LAST_CALL

The year of
                                    				the last time the current user called.

UserInfo.CalledFromAni

Is true if
                                    				the current user has made calls from the current phone or false if
                                    				not.

UserInfo.AccountInfo.PIN

The PIN number
                                    				of the current user’s account.

UserInfo.AccountInfo.ACCOUNT_NUMBER

The account
                                    				number of the current user’s account.

UserInfo.AccountInfo.EXTERNAL_UID

The external
                                    				UID of the current user’s account.

These tags relate to
                        		historical data. While still requiring the User Management System to be active,
                        		these do not require a user to be associated with the call. The fragments
                        		rendered bold represent
                        		values replaced by the application designer. Optional information is
                        		encapsulated in brackets ([]).

Tag Content

Description

GeneralAniInfo.AniDateTime.HourOfDay. LAST_CALL[. ANI ]

The hour of
                                    				the last time a call was received from the current phone number. Use ANI to get
                                    				the last time a call was received from another number where ANI is the number.

GeneralAniInfo.AniDateTime.Minute. LAST_CALL[. ANI ]

The minute of
                                    				the last time a call was received from the current phone number or ANI if
                                    				specified.

GeneralAniInfo.AniDateTime.DayOfMonth. LAST_CALL[. ANI ]

The day of the
                                    				month of the last time a call was received from the current phone number or ANI
                                    				if specified.

GeneralAniInfo.AniDateTime.Month. LAST_CALL[. ANI ]

The month of
                                    				the last time a call was received from the current phone number or ANI if
                                    				specified.

GeneralAniInfo.AniDateTime.DayOfWeek. LAST_CALL[. ANI ]

The day of the
                                    				week of the last time a call was received from the current phone number or ANI
                                    				if specified.

GeneralAniInfo.AniDateTime.Year. LAST_CALL[. ANI ]

The year of
                                    				the last time a call was received from the current phone number or ANI if
                                    				specified.

GeneralAniInfo.AniNumCalls[. ANI ]

The number of
                                    				calls received from the current phone number or ANI if specified.

Each Date / Time
                              			 tag evaluates to 0–23 when referring to the hour, 0-59 when referring to the
                              			 minute, 1–12 when referring to the month, 1–31 when referring to the day of the
                              			 month, 1–7 when referring to the day of the week (where 1 is Sunday), and the
                              			 year is represented as a four-digit number.

If any data
                              			 represented by the tag ends up as null, substitution renders it as an empty
                              			 string. For example, if a setting contained source{CallData.SOURCE} and there was no application that
                              			 transferred to the current application, the setting would be evaluated as source . In
                              			 this case, a warning appears in the Error Log for the application noting that a
                              			 substitution value was null and was replaced with an empty string.

| Tag Content | Description |
|---|---|
| CallData.ANI | The ANI of the
                                    				current call or NA if not sent. |
| CallData.DNIS | The DNIS of the
                                    				current call or NA if not sent. |
| CallData.UUI | The UUI of the
                                    				current call or NA if not sent. |
| CallData.IIDIGITS | The IIDIGITS of
                                    				the current call or NA if not sent. |
| CallData.SOURCE | The name of the
                                    				application that transferred to this one. |
| CallData.APP_NAME | The name of the
                                    				current application. |
| CallData.DURATION | The duration, in
                                    				seconds, of the call up to this point. |
| CallData.LANGUAGE | The language for
                                    				the application, up to this point in the call. |
| CallData.ENCODING | The VoiceXML
                                    				encoding for the application, up to this point in the call. |
| Data.Session. VAR | The value of
                                    				Session Data where VAR represents the name of the session variable. The object
                                    				stored there will be represented as a string. |
| Data.Element. ELEMENT.VAR | The value of
                                    				Element Data where ELEMENT represents the name of the element and VAR
                                    				represents the name of the element variable. |
| Data.Session.lastException.type | The type of
                                    				the last exception occurred. |
| Data.Session.lastException.code | This is the
                                    				exception code for the last exception occurred. |
| Data.Session.lastException.message | The message of
                                    				the last exception. |
| Data.Session.lastException.custom_field1, custom_field2, and
                                    				custom_field3 | This is the
                                    				user-defined fields of the last exception. |
| CallerActivity.NthElement. N | The name of a
                                    				certain element visited in the call where N represents the number for the nth
                                    				element. |
| CallerActivity.NthExitState. N | The name of a
                                    				certain element’s exit state visited in the call where N represents the number
                                    				for the nth element. |
| CallerActivity.TimesElementVisited. ELEMENT | The number of
                                    				times an element was visited in the call where ELEMENT represents the name of
                                    				the element. |
| CallerActivity.imesElementVisitedExitState. ELEMENT.EXIT_STATE | The number of
                                    				times an element was visited in the call with a particular exit state where
                                    				ELEMENT is the name of the element and EXIT_STATE is the exit state. |
| GeneralDateTime.HourOfDay.CURRENT | The current
                                    				hour. |
| GeneralDateTime.HourOfDay.CALL_START | The hour the
                                    				call started. |
| GeneralDateTime.Minute.CURRENT | The current
                                    				minute. |
| GeneralDateTime.Minute.CALL_START | The minute the
                                    				call started. |
| GeneralDateTime.DayOfMonth.CURRENT | The current day
                                    				of the month. |
| GeneralDateTime.DayOfMonth.CALL_START | The day of the
                                    				month the call started. |
| GeneralDateTime.Month.CURRENT | The current
                                    				month. |
| GeneralDateTime.Month.CALL_START | The month the
                                    				call started. |
| GeneralDateTime.DayOfWeek.CURRENT | The current day
                                    				of the week. |
| GeneralDateTime.DayOfWeek.CALL_START | The day of the
                                    				week the call started. |
| GeneralDateTime.Year.CURRENT | The current
                                    				year. |
| GeneralDateTime.Year.CALL_START | The year the
                                    				call started. |

| Tag | Description |
|---|---|
| UserInfo.Demographic.NAME | The name of
                                    				the current user. |
| UserInfo.Demographic.ZIP_CODE | The zip code
                                    				of the current user. |
| UserInfo.Demographic.BIRTHDAY | The birthday
                                    				of the current user. |
| UserInfo.Demographic.GENDER | The gender of
                                    				the current user. |
| UserInfo.Demographic.SSN | The social
                                    				security number of the current user. |
| UserInfo.Demographic.COUNTRY | The country of
                                    				the current user. |
| UserInfo.Demographic.LANGUAGE | The language
                                    				of the current user. |
| UserInfo.Demographic.CUSTOM1 | The contents
                                    				of the first custom column of the current user. |
| UserInfo.Demographic.CUSTOM2 | The contents
                                    				of the second custom column of the current user. |
| UserInfo.Demographic.CUSTOM3 | The contents
                                    				of the third custom column of the current user. |
| UserInfo.Demographic.CUSTOM4 | The contents
                                    				of the fourth custom column of the current user. |
| UserInfo.AniInfo.FIRST | The first
                                    				phone number associated with the current user’s account. |
| UserInfo.AniInfo.NUM_DIFF | The total
                                    				number of different phone numbers associated with the current user’s account. |
| UserInfo.UserDateTime.HourOfDay. LAST_MODIFIED | The hour of
                                    				the last time the current user’s account was modified. |
| UserInfo.UserDateTime.HourOfDay. CREATION | The hour of
                                    				the last time the current user’s account was created. |
| UserInfo.UserDateTime.HourOfDay. LAST_CALL | The hour of
                                    				the last time the current user called. |
| UserInfo.UserDateTime.Minute. LAST_MODIFIED | The minute of
                                    				the last time the current user’s account was modified. |
| UserInfo.UserDateTime.Minute.CREATION | The minute of
                                    				the last time the current user’s account was created. |
| UserInfo.UserDateTime.Minute. LAST_CALL | The minute of
                                    				the last time the current user called. |
| UserInfo.UserDateTime.DayOfMonth. LAST_MODIFIED | The day of the
                                    				month of the last time the current user’s account was modified. |
| UserInfo.UserDateTime.DayOfMonth. CREATION | The day of the
                                    				month of the last time the current user’s account was created. |
| UserInfo.UserDateTime.DayOfMonth. LAST_CALL | The day of the
                                    				month of the last time the current user called. |
| UserInfo.UserDateTime.Month. LAST_MODIFIED | The month of
                                    				the last time the current user’s account was modified. |
| UserInfo.UserDateTime.Month.CREATION | The month of
                                    				the last time the current user’s account was created. |
| UserInfo.UserDateTime.Month.LAST_CALL | The month of
                                    				the last time the current user called. |
| UserInfo.UserDateTime.DayOfWeek. LAST_MODIFIED | The day of the
                                    				week of the last time the current user’s account was modified. |
| UserInfo.UserDateTime.DayOfWeek. CREATION | The day of the
                                    				week of the last time the current user’s account was created. |
| UserInfo.UserDateTime.DayOfWeek. LAST_CALL | The day of the
                                    				week of the last time the current user called. |
| UserInfo.UserDateTime.Year. LAST_MODIFIED | The year of
                                    				the last time the current user’s account was modified. |
| UserInfo.UserDateTime.Year.CREATION | The year of
                                    				the last time the current user’s account was created. |
| UserInfo.UserDateTime.Year.LAST_CALL | The year of
                                    				the last time the current user called. |
| UserInfo.CalledFromAni | Is true if
                                    				the current user has made calls from the current phone or false if
                                    				not. |
| UserInfo.AccountInfo.PIN | The PIN number
                                    				of the current user’s account. |
| UserInfo.AccountInfo.ACCOUNT_NUMBER | The account
                                    				number of the current user’s account. |
| UserInfo.AccountInfo.EXTERNAL_UID | The external
                                    				UID of the current user’s account. |

| Tag Content | Description |
|---|---|
| GeneralAniInfo.AniDateTime.HourOfDay. LAST_CALL[. ANI ] | The hour of
                                    				the last time a call was received from the current phone number. Use ANI to get
                                    				the last time a call was received from another number where ANI is the number. |
| GeneralAniInfo.AniDateTime.Minute. LAST_CALL[. ANI ] | The minute of
                                    				the last time a call was received from the current phone number or ANI if
                                    				specified. |
| GeneralAniInfo.AniDateTime.DayOfMonth. LAST_CALL[. ANI ] | The day of the
                                    				month of the last time a call was received from the current phone number or ANI
                                    				if specified. |
| GeneralAniInfo.AniDateTime.Month. LAST_CALL[. ANI ] | The month of
                                    				the last time a call was received from the current phone number or ANI if
                                    				specified. |
| GeneralAniInfo.AniDateTime.DayOfWeek. LAST_CALL[. ANI ] | The day of the
                                    				week of the last time a call was received from the current phone number or ANI
                                    				if specified. |
| GeneralAniInfo.AniDateTime.Year. LAST_CALL[. ANI ] | The year of
                                    				the last time a call was received from the current phone number or ANI if
                                    				specified. |
| GeneralAniInfo.AniNumCalls[. ANI ] | The number of
                                    				calls received from the current phone number or ANI if specified. |