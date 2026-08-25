---
doc_id: developer-cisco-com-site-jtapi-cti-tapi-jtapi-supported-device-matrix-8c9e010f5b
source_url: https://developer.cisco.com/site/jtapi/cti-tapi-jtapi-supported-device-matrix/
retrieved_at: 2026-08-25T11:43:36.580781+00:00
---

# CTI (TAPI/JTAPI) Supported Device Matrix

Last update 2024/07/08

Device/Phone Model

Supported Protocols

Remarks

Softphone Mode:

Extend/Connect Mode:

Remote Desktop Control Mode:

Refer to the device model under remote control to determine CTI support.

Click-to-Answer requires device speakerphone support.

Remote Desktop Control Mode over MRA/Expressway:

Also referred to as Borderless CTI

Extend/Connect Mode over MRA/Expressway:

Also referred to as Borderless CTI

Compatibility of Cisco IP Phones & Clients

Phone models that are End of Software Maintenance will continue to be supported on the latest Unified
                Communications Manager releases. However, they will not take advantage of any new Unified Communications
                Manager or firmware features associated with that release.

For more information on End of Sale phone models, reference the model's End of Sale announcement for
                information on level of firmware and hardware support.

Note: Phones that are past the Last Date of Support continue to be supported on Cisco Unified
                Communications Manager (Unified CM) until they are deprecated. After a phone is deprecated, it will no
                longer register with the Unified CM. Phone deprecation started with Unified CM Release 11.5. See the
                release notes for Unified CM Release 11.5 or later for the list of deprecated phones.

Phones that do not have CTI support

The following phones cannot be controlled or monitored via CTI: Cisco 3905, Cisco 3911, Cisco E20, Cisco EX60, Cisco EX90, Cisco CTS 500, Cisco CTS 500-32, Cisco CTS (all other models), Cisco ATA 187, Cisco ATA 188, Cisco ATA 190, Cisco ATA 191, VG224, ISDN BRI Phone, IMS Client, Mobile Communicator, Nokia S60, Remote Destination Profile (Single Number Reach)

The following phones cannot be controlled when operating in softphone mode: Cisco Unified Communications Integration for Microsoft Office Communicator/Lync, Cisco Unified Communications for RTX, Cisco Web Communicator for Wx Social, Cisco Unified Communications Integration for WebEx Connect

| Device/Phone Model | Supported Protocols | Remarks |
|---|---|---|
| Analog Phone |  | See Cisco ATA devices |
| Cisco 12 S |  |  |
| Cisco 12 SP |  |  |
| Cisco 30 SP+ |  |  |
| Cisco 6901 |  |  |
| Cisco 6911 |  |  |
| Cisco 6921 |  |  |
| Cisco 6941 |  |  |
| Cisco 6945 |  |  |
| Cisco 6961 |  |  |
| Cisco 7811 |  |  |
| Cisco 7821 |  |  |
| Cisco 7841 |  |  |
| Cisco 7861 |  |  |
| Cisco 7902 |  |  |
| Cisco 7905 |  |  |
| Cisco 7906 |  |  |
| Cisco 7910 |  |  |
| Cisco 7911 |  |  |
| Cisco 7912 |  |  |
| Cisco 7914 Sidecar |  |  |
| Cisco 7915 Sidecar |  |  |
| Cisco 7916 Sidecar |  |  |
| Cisco CKEM Sidecar |  |  |
| Cisco 7920 |  |  |
| Cisco 7921 |  |  |
| Cisco 7925 & 7925-EX |  |  |
| Cisco 7926 |  |  |
| Cisco 7931 |  |  |
| Cisco 7935 |  |  |
| Cisco 7936 |  |  |
| Cisco 7937 |  |  |
| Cisco 7940 |  |  |
| Cisco 7941 |  |  |
| Cisco 7941G-GE |  |  |
| Cisco 7942 |  |  |
| Cisco 7945 |  |  |
| Cisco 7960 |  |  |
| Cisco 7961 |  |  |
| Cisco 7961G-GE |  |  |
| Cisco 7962 |  |  |
| Cisco 7965 |  |  |
| Cisco 7970 |  |  |
| Cisco 7971 |  |  |
| Cisco 7975 |  |  |
| Cisco 7985 |  |  |
| Cisco 8811 |  |  |
| Cisco 8821 |  |  |
| Cisco 8831 |  |  |
| Cisco 8832 |  |  |
| Cisco 8841 |  |  |
| Cisco 8845 |  |  |
| Cisco 8851 |  |  |
| Cisco 8861 |  |  |
| Cisco 8865 |  |  |
| Cisco 8875 |  |  |
| Cisco 8941 |  |  |
| Cisco 8945 |  |  |
| Cisco 8961 |  | phoneSetDisplay() interface is not supported |
| Cisco 9841 |  |  |
| Cisco 9851 |  |  |
| Cisco 9861 |  |  |
| Cisco 9871 |  |  |
| Cisco 9951 |  | phoneSetDisplay() interface is not supported |
| Cisco 9971 |  | phoneSetDisplay() interface is not supported |
| Cisco DX650 |  | phoneSetDisplay() interface is not supported |
| Cisco DX70 |  |  |
| Cisco DX80 |  |  |
| Cisco ATA 186 |  | Limited functionality, see the JTAPI Developer Guide |
| Cisco IP Communicator |  |  |
| Softphone Mode: Cisco Jabber for Windows Cisco Jabber for Mac Cisco Webex App for Windows Cisco Webex App for Mac Cisco Unified Personal Communicator |  | Requires Jabber 9.0 Requires CUCM 8.6(1) Requires CUPC 8.5(1) |
| Extend/Connect Mode: Cisco Jabber for Windows Cisco Jabber for Mac Cisco Webex App for Windows Cisco Webex App for Mac |  | Requires CUCM 9.1(1a) and Jabber 9.1(2) |
| Remote Desktop Control Mode: Cisco Jabber for Windows Cisco Jabber for Mac Cisco Webex App for Windows Cisco Webex App for Mac Cisco Unified Personal Communicator Cisco Unified Communications Integration for Microsoft Office Communicator/Lync Cisco Unified Communications for RTX (CUCRTX) Cisco Unified Communications Integration for WebEx Connect |  | Refer to the device model under remote control to determine CTI support. Click-to-Answer requires device speakerphone support. |
| Remote Desktop Control Mode over MRA/Expressway: Cisco Webex App for Windows Cisco Webex App for Mac |  | Also referred to as Borderless CTI Minimum CUCM version : 14.0 SU2 Minimum WxApp version - v42.7 Desk Phones: Cisco IP Phone 8800 Series, Cisco IP Phone 7800 Series, Cisco Webex Desk Series DX & DeskPro) |
| Extend/Connect Mode over MRA/Expressway: Cisco Webex App for Windows Cisco Webex App for Mac |  | Also referred to as Borderless CTI Minimum CUCM version : 14.0 SU2 Minimum WxApp version - v42.7 Desk Phones: Cisco IP Phone 8800 Series, Cisco IP Phone 7800 Series, Cisco Webex Desk Series DX & DeskPro) |
| Cisco Jabber for iPhone & iPad Cisco Webex App for iPhone & iPad |  | Support for CTI event monitoring added in CUCM 12.5 su1 for WiFi mode only. Does not support
                            invoking
                            call control/feature requests. See Release
                                Notes for details |
| Cisco Jabber for Android Cisco Webex App for Android |  | Support for CTI event monitoring added in CUCM 12.5 su1 for WiFi mode only. Does not support
                            invoking
                            call control/feature requests. See Release
                                Notes for details |
| Cisco VGC Phone |  |  |
| VG248 |  | Limited functionality, see the JTAPI Developer Guide |
| CTI Port |  |  |
| CTI Remote Device (Extend/Connect) |  |  |
| CTI Route Point |  |  |
| Cisco Spark Remote Device |  | This is a CTI device, but is not supported via Cisco TAPI/JTAPI |