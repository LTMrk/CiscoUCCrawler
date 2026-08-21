---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-705d39b14e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/callback_add.html
retrieved_at: 2026-08-21T17:09:44.634553+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Callback_Add

## Chapter: Callback_Add

# Callback_Add

The Callback_Add element is used to add a callback object to the database after all the callback information has been collected from the caller.
                                    In addition, it can be optionally configured to automatically delete old recorded files at specified intervals. These recorded
                                    files are the files produced by the Record element when the user records their name if they want a call back in the CallbackEntry
                                    application.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Callback Number

string

Yes

true

true

None

The
                                          phone number the callers specifies to call back.

Recorded Name File

string

Yes

true

true

None

The
                                          URL to the recorded file for playback when the caller is called
                                          back.

Recorded Name
                                          Path

string

No

true

true

None

Path
                                          to the recorded file. If specified, files starting with audio in this folder are deleted automatically based on
                                          the file retention time and interval specified in Recorded File
                                             Retention and Recorded File Deletion
                                             Interval settings.

If this setting is
                                          left blank, recorded files are not deleted automatically.

The
                                          value of this setting may be either the path to a folder or a path to a file.
                                          If a path to a file is specified, then the folder in which the file resides is
                                          the folder to be managed. The path to the folder must be accessible to the
                                          VXMLServer.

Recorded
                                          File Retention

Int

No

true

true

240

Number of minutes to
                                          retain recorded files before they are eligible for automatic deletion. This
                                          setting only takes effect if Recorded name Path is
                                          specified.

Recorded File
                                          Deletion Interval

Int

No

true

true

30

Number of interval minutes
                                          for checking when recorded files can be deleted. This setting only takes effect
                                          if Recorded name Path is specified

## Element Data

Name

Type

Notes

Result

string

Result of request to add callback
                                          object to the database. Valid string values are valid , no_validation and invalid_time .

valid – signifies that the request was successful.

no_validation – occurs when a callback object cannot be created because Callback_Validate element was not run in the script.

invalid_time – means that the time selected for the
                                                scheduled callback is
                                                invalid.

## Exit States

Name

Notes

done

The element is successfully run to retrieve the value.

error

The element failed to
                                          retrieve the
                                          value.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Cisco > Callback

com.cisco.cvp.vxml.custelem.callback.AddCallback

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| The Callback_Add element is used to add a callback object to the database after all the callback information has been collected from the caller.
                                    In addition, it can be optionally configured to automatically delete old recorded files at specified intervals. These recorded
                                    files are the files produced by the Record element when the user records their name if they want a call back in the CallbackEntry
                                    application. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Callback Number | string | Yes | true | true | None | The
                                          phone number the callers specifies to call back. |
| Recorded Name File | string | Yes | true | true | None | The
                                          URL to the recorded file for playback when the caller is called
                                          back. |
| Recorded Name
                                          Path | string | No | true | true | None | Path
                                          to the recorded file. If specified, files starting with audio in this folder are deleted automatically based on
                                          the file retention time and interval specified in Recorded File
                                             Retention and Recorded File Deletion
                                             Interval settings. Note All files created by the Record
                                                   element start with audio . If this setting is
                                          left blank, recorded files are not deleted automatically. The
                                          value of this setting may be either the path to a folder or a path to a file.
                                          If a path to a file is specified, then the folder in which the file resides is
                                          the folder to be managed. The path to the folder must be accessible to the
                                          VXMLServer. | Note | All files created by the Record
                                                   element start with audio . |
| Note | All files created by the Record
                                                   element start with audio . |
| Recorded
                                          File Retention | Int | No | true | true | 240 | Number of minutes to
                                          retain recorded files before they are eligible for automatic deletion. This
                                          setting only takes effect if Recorded name Path is
                                          specified. |
| Recorded File
                                          Deletion Interval | Int | No | true | true | 30 | Number of interval minutes
                                          for checking when recorded files can be deleted. This setting only takes effect
                                          if Recorded name Path is specified |

| Note | All files created by the Record
                                                   element start with audio . |
|---|---|

| Name | Type | Notes |
|---|---|---|
| Result | string | Result of request to add callback
                                          object to the database. Valid string values are valid , no_validation and invalid_time . valid – signifies that the request was successful. no_validation – occurs when a callback object cannot be created because Callback_Validate element was not run in the script. invalid_time – means that the time selected for the
                                                scheduled callback is
                                                invalid. |

| Name | Notes |
|---|---|
| done | The element is successfully run to retrieve the value. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.AddCallback |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |