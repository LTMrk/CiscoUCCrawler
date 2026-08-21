---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-english-9-3-4-admin-guide-8831-3pcc-ag-regional-html-7e6c759a3d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/english/9_3_4/admin-guide/8831-3pcc-ag/regional.html
retrieved_at: 2026-08-21T02:09:38.694851+00:00
---

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

# Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

Updated: October 22, 2014

Chapter: Configure Regional Parameters and Supplementary Services

## Chapter: Configure Regional Parameters and Supplementary Services

## Configure Regional Parameters and Supplementary Services

Use the Regional tab to configure regional and local settings, such as control timer parameters, dictionary server script, language Selection, and locale to change localization:

## Control Timer Values (sec)

The table describes Control Timer parameters.

Interdigit Long Timer

Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit Long Timer is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Ranges from 0 to 64 seconds.

Setting this value high can result in a longer post dialing delay (PDD), which is the time between the start of a call and the time the phone starts ringing. A value that is too low can result in dialed digits not being correctly recognized.

Defaults to 10.

Interdigit Short Timer

Short timeout between entering digits when dialing. The Interdigit Short Timer is used after any one digit, if at least one matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Ranges from 0 to 64 seconds.

Defaults to 3.

## Localize Your Conference Phone

The following table describes the localization parameters in the Voice > Regional tab under Time section.

Set Local Date (mm/dd)

Enter the local date ( mm represents the month and dd represents the day). The year is optional and uses two or four digits. For example,

May 1, 2014, can be entered as: 05/01 or 05/01/14 or 05/01/2014 .

Set Local Time (HH/mm)

Enter the local time ( HH represents hours and MM represents minutes). Seconds are optional.

Time Zone

Selects the number of hours to add to GMT to generate the local time for caller ID generation. Choices are GMT-12:00, GMT-11:00,…, GMT-1:00, GMT-0:00, GMT+01:00, GMT+02:00, …, GMT+13:00.

Defaults to GMT-08:00.

Time Offset (HH/mm)

Enter the offset from GMT to use for the local system time.

Ignore DHCP Time Offset

When used with some routers that have DHCP with time offset values configured, the conference phone uses the router settings and ignores the phone time zone and offset settings. To ignore the router DHCP time offset value, and use the local time zone and offset settings, choose Yes for this option. Choosing No causes the IP phone to use the router’s DHCP time offset value.

The default value is Yes.

Daylight Saving Time Rule

Enter the rule for calculating daylight saving time. See the “Configure Daylight Saving Time” section .

Daylight Saving Enable

Select Yes to enable or No to disable DST on the phone. This setting affects all lines (extensions) on the phone.

Dictionary Server Script

Defines the location of the dictionary server, the languages available, and the associated dictionary. See the “Create a Dictionary Server Script” section .

Language Selection

Specifies the default language. The value must match one of the languages supported by the dictionary server. The script (dx value) is:

Defaults to blank; the maximum number of characters is 512. For example:

Locale

Choose the locale that should be set in the HTTP Accept-Language header.

### Manage the Time and Date

The Cisco conference phone obtains the time settings in one of three ways:

- NTP Server—When the phone boots up, it tries to contact the first Network Time Protocol (NTP) server to get the time. The phone periodically synchronizes its time with the NTP server. The synchronization period is fixed at 1 hour. Between updates the phone tracks time with its internal clock.

- SIP Messages—Each SIP message (request or response) sent to the phone could contain a Date header with the current time information. If the header is present, the phone uses it to set its clock.

- Manual Setup—The time and date can be entered manually by using the phone web user interface. However, this value is overwritten by the NTP time or SIP Message Date whenever they are available to the phone. Manual setup requires that you enter the time in 24-hour format only.

The time served by the NTP Server and the SIP Date Header are expressed in GMT time. The local time is obtained by offsetting the GMT according to the time zone of the region.

The Time Zone parameter can be configured by using the phone web user interface or through provisioning. This time can be further offset by the Time Offset (HH/mm) parameter. This parameter must be entered in 24-hour format and can also be configured from the IP phone screen.

The Time Zone and Time Offset (HH/mm) offset values are not applied to manual time and date setup.

### Configure Daylight Saving Time

The phone supports auto adjustment for daylight saving time. You must set Daylight Saving Time Enable to Yes and enter the DST rule. This option affects the time stamp on the CallerID .

To enter the rule for calculating DST, include the start, end, and save values separated by semi-colons (;) as follows:

For example, the default DST rule is:

The start-time and end-time values specify the start and end dates and times of daylight saving time. The format is:

The month value equals any value in the range 1-12 (January-December).

The day value equals any + or - value in the range 1-31. If the day value is -1, the time changes on the last occurrence of a weekday in that month. If the day value is -2 to -31 (max day value for that month) then the time changes on the weekday in that month (or previous month) on or before that day of the month.

The weekday value equals any value in the range 1-7 (Monday-Sunday). It can also be 0. If the weekday value is 0, it means that the date to start or end daylight saving is the given date. In that case, the day value must not be negative. If the weekday value is positive (but not 0) then the daylight saving starts or ends on the weekday value on or after the given date. If the weekday value is negative (not -1), then the daylight saving starts or ends on the weekday value on or before the given date.

Optional time values: HH represents hours (0-23), mm represents minutes (0-59). and ss represents seconds (0-59). Optional values inside brackets [ ] are assumed to be 0 if not specified. Midnight is represented by 0:0:0.

The save-time value is the number of hours, minutes, and/or seconds to add to the current time during DST.

### Daylight Saving Time Examples

The following example configures daylight saving time for the U.S, adding one hour starting at midnight on the first Sunday in April and ending at midnight on the last Sunday of October; add 1 hour (USA, North America):

The following example configures daylight saving time for Egypt, starting at midnight on the last Sunday in April and ending at midnight on the last Sunday of September:

The following example configures daylight saving time for New Zealand (in version 7.5.1 and higher), starting at midnight on the first Sunday of October and ending at midnight on the third Sunday of March.

The following example reflects the new change starting in March. DST starts on the second Sunday in March and ends on the first Sunday in November:

The following example configures the daylight saving time starting on the last Monday (before April 8) and ending on the first Wednesday (after May 8.)

### Select a Display Language

This section describes how to localize the display language on the conference phone. You can define up to twelve languages, in addition to English, to be available and host the dictionaries for each of the languages on the HTTP or TFTP provisioning server. Language support follows Cisco dictionary principles.

Use the Language Selection parameter to select the phone default display language. The value must match one of the languages supported by the dictionary server. The script (dx value) is as follows:

- <Language_Selection ua="na">

- </Language_Selection>

Defaults to blank; the maximum number of characters is 512. For example:

During startup, the phone checks the selected language and downloads the dictionary from the TFTP/HTTP provisioning server indicated in the phone configuration. The dictionaries are available at the support website. See Appendix B, “Related Documentation,” for the website location.

The end user can change the language of the phone on the phone by following these steps:

Step 1 Press the Setup button.

Step 2 Select Language , then press the Select soft button.

Step 3 Select Option to change the language.

Step 4 With the desired language highlighted, press Save .

### Create a Dictionary Server Script

The Dictionary Server Script defines the location of the dictionary server, the languages available and the associated dictionary. Up to five language entries are recognized in the script. The syntax is:

Note TFTP, HTTP, and HTTPS are supported for the dictionary download.

Defaults to blank; the maximum number of characters is 512. The detailed format is as follows:

The following languages are supported on the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control:

– da-DK : Danish_Denmark

– nl-NL : Dutch_Netherlands

– fr-FR : French_France

– de-DE : German_Germany

– he-IL : Hebrew_Israel

– it-IT : Italian_Italy

– no-NO : Norwegian_Norway

– pt-PT : Portuguese_Portugal

– ru-RU : Russian_Russian_Federation

– es-MX : Spanish_Mexico

– es-ES : Spanish_Spain

– sv-SE : Swedish_Sweden

### Localization Configuration Example

Language Selection: French

(Entry dx must match one of the languages supported by the dictionary server.)

Locale: fr-FR

(Entry lx must be within the Locale option list.)

| Field | Description |
|---|---|
| Interdigit Long Timer | Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit Long Timer is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Ranges from 0 to 64 seconds. Setting this value high can result in a longer post dialing delay (PDD), which is the time between the start of a call and the time the phone starts ringing. A value that is too low can result in dialed digits not being correctly recognized. Defaults to 10. |
| Interdigit Short Timer | Short timeout between entering digits when dialing. The Interdigit Short Timer is used after any one digit, if at least one matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Ranges from 0 to 64 seconds. Defaults to 3. |

| Field | Description |
|---|---|
| Set Local Date (mm/dd) | Enter the local date ( mm represents the month and dd represents the day). The year is optional and uses two or four digits. For example, May 1, 2014, can be entered as: 05/01 or 05/01/14 or 05/01/2014 . |
| Set Local Time (HH/mm) | Enter the local time ( HH represents hours and MM represents minutes). Seconds are optional. |
| Time Zone | Selects the number of hours to add to GMT to generate the local time for caller ID generation. Choices are GMT-12:00, GMT-11:00,…, GMT-1:00, GMT-0:00, GMT+01:00, GMT+02:00, …, GMT+13:00. Defaults to GMT-08:00. |
| Time Offset (HH/mm) | Enter the offset from GMT to use for the local system time. |
| Ignore DHCP Time Offset | When used with some routers that have DHCP with time offset values configured, the conference phone uses the router settings and ignores the phone time zone and offset settings. To ignore the router DHCP time offset value, and use the local time zone and offset settings, choose Yes for this option. Choosing No causes the IP phone to use the router’s DHCP time offset value. The default value is Yes. |
| Daylight Saving Time Rule | Enter the rule for calculating daylight saving time. See the “Configure Daylight Saving Time” section . |
| Daylight Saving Enable | Select Yes to enable or No to disable DST on the phone. This setting affects all lines (extensions) on the phone. |
| Dictionary Server Script | Defines the location of the dictionary server, the languages available, and the associated dictionary. See the “Create a Dictionary Server Script” section . |
| Language Selection | Specifies the default language. The value must match one of the languages supported by the dictionary server. The script (dx value) is: <Language_Selection ua="na"> </Language_Selection> Defaults to blank; the maximum number of characters is 512. For example: <Language_Selection ua="na"> Spanish </Language_Selection> |
| Locale | Choose the locale that should be set in the HTTP Accept-Language header. |