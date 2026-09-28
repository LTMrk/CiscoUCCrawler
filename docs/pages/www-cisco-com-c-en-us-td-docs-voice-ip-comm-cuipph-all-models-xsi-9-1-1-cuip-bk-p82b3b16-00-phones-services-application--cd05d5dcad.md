---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-all-models-xsi-9-1-1-cuip-bk-p82b3b16-00-phones-services-application--cd05d5dcad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes1_chapter_0111.html
retrieved_at: 2026-08-16T18:01:57.090443+00:00
---

Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

# Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

Updated: August 6, 2026

Chapter: Troubleshooting Cisco Unified IP Phone Service Applications

## Chapter: Troubleshooting Cisco Unified IP Phone Service Applications

# Troubleshooting Cisco Unified IP Phone Service Applications

## Troubleshooting Tips

The following tips apply to troubleshooting Cisco Unified IP Phone service applications:

Microsoft Internet Explorer 5 or higher can display the XML source with its default style sheet.

Understand that standard IP troubleshooting techniques are important for HTTP errors.

Externally verify name resolution (Phone has DNS set).

If DNS is suspected, use IP addresses in URLs.

Browse the URL in question with Microsoft Internet Explorer or download and verify with another web browser.

Use a logged telnet session to verify that the desired HTTP headers are returned (telnet to the server on port 80, and then
                                    enter: get /path/page).

## XML Parsing Errors

The following tips apply to troubleshooting XML parsing errors in Cisco Unified IP Phone services applications:

Verify the object tags (the object tags are case sensitive).

Verify that "&" and the other four special characters are used according to the restrictions while inside the XML objects.

Validate XML applications developed prior to Cisco Unified IP Phone Firmware Release 8.3(2) against the more recent XML parser.
                                    Some of examples of the types of errors you might encounter include:

CiscoIPPhoneMenu Object: If the field <Name> is missing for a <MenuItem> , the original parser would stop rendering from that <MenuItem> onwards. The new parser will display a blank line in the menu list and continue to render any subsequent <MenuItem> definitions.

CiscoIPPhoneDirectory Object: If the field <Name> is not present, the old original parser would not display the directory entry, the new parser will display the directory
                                          entry, but there will be no <Name> associated with it.

CiscoIPPhoneInput Object: The URL and QueryStringParam fields are mandatory. The original parser would not report an error on the missing URL and on submit request would display
                                          a "Host not Found" message. If the QueryStringParam field is missing, the updated parser will report an error.

SoftKeyItem: The Position field is mandatory. If the Position field is not present, the updated XML parser will report an error.

## Error Messages

The following error messages may appear on the prompt line of the Cisco Unified IP Phone display:

XML Error[4] = XML Parser error (Invalid Object)

XML Error[5] = Unsupported XML Object (not supported by this phone model)

HTTP Error[8] = Unknown HTTP Error

HTTP Error[10] = HTTP Connection Failed

The Cisco Unified IP Phone 6900 Series supports the following error messages:

Services Unavailable

cfg file directoryURL or servicesURL is empty

Host Not Found

DNS query fails

Server Busy!

Server response 503

Connection failed

Socket cannot be created or the connection fails

XML Error [4]: Parse Error

Does not match XML schema

Data too large!

Downloaded content is over 196608 bytes

No services configured

HTTP message body is empty

Filename too long!

file name length is over 127 characters.

File Not Found

Server response 404

HTTP connection failed

Server response 500

Unknown Error

Other errors

| Text | Description |
|---|---|
| Services Unavailable | cfg file directoryURL or servicesURL is empty |
| Host Not Found | DNS query fails |
| Server Busy! | Server response 503 |
| Connection failed | Socket cannot be created or the connection fails |
| XML Error [4]: Parse Error | Does not match XML schema |
| Data too large! | Downloaded content is over 196608 bytes |
| No services configured | HTTP message body is empty |
| Filename too long! | file name length is over 127 characters. |
| File Not Found | Server response 404 |
| HTTP connection failed | Server response 500 |
| Unknown Error | Other errors |