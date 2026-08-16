---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-19f2bac8ff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_01000.html
retrieved_at: 2026-08-16T20:27:54.889532+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: Business Hours

## Chapter: Business Hours

# Business Hours

## Business Hours API

Use this API to list the currently defined business hours, define new business hours, and view, edit, and delete the existing
                           business hours.

### URL

### Operations

create : Creates one business hour.

get : Returns one business hour using the URL https://<server>/unifiedconfig/config/businesshour/<id>

get (template): Returns a sample CSV template for Special Hours and Holidays, which is provided by the API, using the URL https://<server>/unifiedconfig/config/businesshour/specialdayschedule/template . The response contains the CSV template as a file attachment.

list : Retrieves a list of business hours.

update : Updates one business hour.

delete : Permanently deletes one business hour.

### Parameters

changeStamp: See Shared Parameters .

refURL: The refURL of the business hour. See Shared Parameters .

name: The name of the business hour. See Shared Parameters .

description: See Shared Parameters .

type: Required. The type of the business hour.

0: 24x7

1: Custom

configuredStatus: The configured status of the business hour.

status: Required.

0: Calendar Schedule

1: Force Close

2: Force Open

statusReason: Required if the status is Force Open or Force Close.

runTimeStatus: The run time status of the business hour. Available only in Get. It cannot be set or updated.

timezone: Required. The time zone of the business hour.

weekDaySchedules: The list of schedules on weekdays of business. Required only when business hour type is Custom.

dayOfweek: Required.

0: Sunday

1: Monday

2: Tuesday

3: Wednesday

4: Thursday

5: Friday

6: Saturday

startTime: Required. Format HH:MM

endTime: Required. Format HH:MM

specialDaySchedules: The list of schedules on special days of business.

date: Required. Format: DD-MM-YYYY

startTime: Required, if the status is Open. Format: HH:MM

endTime: Required, if the status is Open. Format: HH:MM

description: Optional. Maximum of 255 characters.

status: Required.

0: Closed

1: Open

statusReason: Required. The refURL to existing status reason.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

name

description

name

runTimeStatus

runTimeStatusReason

type

timezone.dispName

See Search and Sort .

### Example Get Response

```
<businessHour>
    <refURL>/unifiedconfig/config/businesshour/1000</refURL>
    <changeStamp>0</changeStamp>
    <runTimeStatus>2</runTimeStatus>
    <runTimeStatusReason>closed</runTimeStatusReason>
    <name>credit_card</name>
    <type>1</type>
    <description>Business Line of Credit</description>
    <timezone>
    <refURL>/unifiedconfig/config/timezone/3001</refURL>
    <displayName>(UTC-05:00) Eastern Time (US & Canada)</displayName>
    </timezone>
    <configuredStatus>
        <status>1</status>
        <statusReason>
            <refURL>/unifiedconfig/config/businesshourstatusreason/5000</refURL>
            <reasonText>Emergency</reasonText>
        </statusReason>
    </configuredStatus>
    <specialDaySchedules>
        <specialDaySchedule>
            <refURL>/unifiedconfig/config/businesshour/1000/specialdayschedule/2001</refURL>
            <changeStamp>0</changeStamp>
            <date>04-02-2019</date>
            <startTime>03:26</startTime>
            <endTime>04:16</endTime>
            <description>Thanksgiving Day</description>
            <status>1</status>
            <statusReason>
                <refURL>/unifiedconfig/config/businesshourstatusreason/5000</refURL>
                <reasonText>Emergency</reasonText>
            </statusReason>
        </specialDaySchedule>
    </specialDaySchedules>
    <weekDaySchedules>
        <weekDaySchedule>
            <refURL>/unifiedconfig/config/businesshour/1000/weekdayschedule/1001</refURL>
            <changeStamp>0</changeStamp>
            <dayOfWeek>1</dayOfWeek>
            <startTime>06:20</startTime>
            <endTime>07:22</endTime>
        </weekDaySchedule>
    </weekDaySchedules>
</businessHour>
```

## Business Hour Status Reason API

Use this API to list the currently defined business hour status reasons, define new status reasons, and view, edit, and delete
                           the existing status reasons.

### URL

### Operations

create : Creates one business hour status reason.

get : Returns one business hour status reason using the URL https://<server>/unifiedconfig/config/businesshourstatusreason/<id>

list : Retrieves a list of business hour status reasons.

update : Updates one business hour status reason.

delete : Permanently deletes one business hour status reason.

### Parameters

category: Optional. The category of the reason codes: User-defined or System-defined.

reasonCode: Required. The unique status reason code for business hour. Range is 1001 to 65535.

Codes 1 to 1000 are reserved as system defined reason codes. The System-defined reason codes cannot be deleted.

reasonText: Optional. The reason for the business schedule. Maximum of 255 characters.

### Example Create Request

```
<businessHourStatusReason>
 <category>User-defined</category>
<reasonCode>1234</reasonCode>
<reasonText>Emergency</reasonText>
</businessHourStatusReason>
```

### Example Get Response

```
<businessHourStatusReason>
 <refURL>/unifiedconfig/config/businesshourstatusreason/5000</refURL>
 <changeStamp>0</changeStamp>
 <category>User-defined</category>
 <reasonCode>2550</reasonCode>
 <reasonText>Open</reasonText>
 </businessHourStatusReason>
```

## Time Zone API

Use the Time Zone API to list all available time zones and to get time zone information for a specified zone. Time zone information
                           is stored in the registry of the Windows operating system.

Microsoft periodically releases cumulative time zone updates. These updates include worldwide changes to time zone names,
                                       bias (the amount of time in minutes that a time zone is offset from Coordinated Universal Time (UTC)), and observance of daylight
                                       saving time. These patches update the information in the Windows registry. When these updates are available, apply them to
                                       all virtual machines in the deployment that are running a Microsoft Windows operating system.

Use this API with the Business Hours API to set the default time zone for a business hour.

This API is read-only.

### URL

https://<server>/unifiedconfig/config/timezone/v2

### Operations

list : Retrieves a list of available time zones. The list is sorted by UTC offset from the International Date Line from west to
                                    east.

get : Returns information for a specific time zone using the URL https://<server>/unifiedconfig/config/timezone/v2/<id> .

### Response Parameters

name: The name of the time zone.

displayName: Specific bias and location information about the time zone, such as the offset from UTC and one or more places
                                    located within the time zone.

Example: "(UTC-05:00) Eastern Time (US & Canada)"

changeStamp: See Shared Parameters .

### Example Get Response

```
<timezone>
    <refURL>/unifiedconfig/config/timezone/v2/5000</refURL>
    <changeStamp>0</changeStamp>
    <displayName>(UTC-05:00) Eastern Time (US & Canada)</displayName>
    <name>UTC</name>
</timezone>
```

| Search parameters | Sort parameters |
|---|---|
| name description | name runTimeStatus runTimeStatusReason type timezone.dispName |

| Note | Codes 1 to 1000 are reserved as system defined reason codes. The System-defined reason codes cannot be deleted. |
|---|---|

| Important | Microsoft periodically releases cumulative time zone updates. These updates include worldwide changes to time zone names,
                                       bias (the amount of time in minutes that a time zone is offset from Coordinated Universal Time (UTC)), and observance of daylight
                                       saving time. These patches update the information in the Windows registry. When these updates are available, apply them to
                                       all virtual machines in the deployment that are running a Microsoft Windows operating system. |
|---|---|