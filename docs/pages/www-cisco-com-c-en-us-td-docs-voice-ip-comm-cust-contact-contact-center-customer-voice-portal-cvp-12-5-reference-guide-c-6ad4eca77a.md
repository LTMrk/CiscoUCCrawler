---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-reference-guide-c-6ad4eca77a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/reference/guide/ccvp_b_1251-element-specification-guide-cvp/ccvp_mp_vf6c33db_00_videoconnect-map.html
retrieved_at: 2026-08-21T17:34:36.460654+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

Updated: January 31, 2020

Chapter: VideoConnect

## Chapter: VideoConnect

# VideoConnect

The VideoConnect element plays a specific video file (identified using the dialed number)
                        from the video media server and collect digits during the video file
                        playback.

This chapter contains the following
                        topics:

## Settings

Setting

Value

Allowed

- If you enter the  DTMF that do not match the configured
                                          pattern. It results in an automatic retry for digit collection, so
                                          unmatched patterns does not cause the video element to
                                          exit.

- If the intent is to explicitly trap no-matches,
                                          then you can collect any single digit and return to the application.

## Element Data

Name

Type

Notes

## Exit States

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

## Others

Studio Element Folder

Video

| Name (Label) | Type | Required | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Video Media Server DN | String | Yes | True | True | None | Video Media Server Destination Number. Example:
                                       5000. Must be a valid dialed number on Cisco UBE and the Video
                                       Media Server. |
| Digit Match Pattern | String | No | True | True | None | Pattern to use for matching incoming digit
                                       collection. Leave blank for no digit collection. Example: 600. Must be a valid pattern for Cisco IOS gateway.
                                       The Pattern format is same as   the destination-pattern format used in IOS
                                       gateway dial-peers. |
| No-input Timeout | String | No | True | True | No timeout | Maximum time (seconds) to wait for caller input. Example: 15. |

| Note | If you enter the  DTMF that do not match the configured
                                          pattern. It results in an automatic retry for digit collection, so
                                          unmatched patterns does not cause the video element to
                                          exit. If the intent is to explicitly trap no-matches,
                                          then you can collect any single digit and return to the application. |
|---|---|

| Name | Type | Notes |
|---|---|---|
| callerdtmf | String | The digit string value captured. |
| result | String | Video call outcome. |

| State | Description |
|---|---|
| End_of_media | The Video played to completion and the video server gets disconnected. |
| Caller_input | The Caller entered a DTMF string that matched the specified digit collection pattern. |
| No_input | A digit collection pattern was specified, but no input was received before the input timeout occured. |
| Error | This exit state is used when an error occurs and for all other unexpected termination reasons. |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |

| Studio Element Folder | Video |
|---|---|
| Class Name | com.cisco.cvp.vxml.custelem.VideoConnect |