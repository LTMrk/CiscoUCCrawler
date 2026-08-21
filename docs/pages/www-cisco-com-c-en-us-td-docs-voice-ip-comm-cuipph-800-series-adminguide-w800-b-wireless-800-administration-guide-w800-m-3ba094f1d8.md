---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-800-series-adminguide-w800-b-wireless-800-administration-guide-w800-m-3ba094f1d8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/800-series/adminguide/w800_b_wireless-800-administration-guide/w800_m_troubleshooting.html
retrieved_at: 2026-08-21T23:27:32.995668+00:00
---

Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

# Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

Updated: August 13, 2026

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## General troubleshooting information

### General issues

The following table provides general troubleshooting information.

Problem

Solution

You’re not in a call and the phone goes black and displays the message: Close proximity detected .

Your phone has a proximity sensor at the top right. When this sensor is blocked, the phone screen is black. The sensor is
                                          normally blocked by the face when the earpiece is used to listen to a caller.

If you’re not in a call and you see the message: Close proximity detected . The sensor may be covered with a finger or paper or something else that blocks light. If there’s no apparent blockage, clean
                                          the area of the sensor.

While using a standard headset, you experience a scratchy or intermittent signal.

The headset connector may be dirty. If available, blow canned air into the connector to clear debris. Always point canned
                                          air orientation at glancing angles away from your face and eyes and always wear safety goggles or glasses when performing
                                          this procedure.

Do not use air compressors on the connectors, since they apply too much force.

Third Party Application Conflicts

Third party application interference can be eliminated by factory reset and reregistration of a problematic phone. For more
                                          details about the factory reset, see Restoring Factory Defaults in the Cisco Wireless Phone 840 and 860 Deployment Guide .

### Visual voicemail issues

The following table provides general troubleshooting information that is related to issues with Visual Voicemail.

Problem

Solution

Unauthorized message appears in the Enter Unity Web Credentials dialog box after the user enters their credentials and selects the Login
                                          option.

Validate that the:

User enters the same Username as the Alias field (including case) on the User’s Mailbox in the Cisco Unity Connection voice messaging system.

User uses the Web Application password, not the Voicemail pin.

Password Settings for the User’s Web Application Password don't have the User Must Change Password at Next Sign-In check box
                                                selected.

When the user navigates to the Voicemail tab of the Cisco Phone app, a brief toast notification appears, which states Voicemail connection error. Unable to connect along with an error message Voicemail Authentication failed! Unable to connect to voicemail. Please contact your administrator . Also, you know that visual voicemail is not working on other devices at the same site.

Validate that the Cisco Unity Connection server’s tomcat-trust certificate has been imported into the Cisco Unified
                                             				Communications Manager ’s trust store and the Tomcat service has been restarted since the import occurred.

Voicemail connection error. Unable to connect. toast notification appears on the screen when the user navigates to the Voicemail tab of the Cisco Phone app.

Visual voicemail is unable to connect to the Cisco Unity Connection server. Investigate potential connectivity issues between the user’s phone and the server.

This feature has been disabled by your administrator appears when the user navigates to the Voicemail tab of the Cisco Phone app.

Enable visual voicemail from the Phone Configuration page in Cisco Unified
                                             				Communications Manager . This error appears only if visual voicemail was enabled previously, and then disabled.

## Details available on the phone

You can see some status and details about the phone in the Cisco apps.

This information helps you troubleshoot problems when you are in the same location as your user.

### View phone information

The About phone setting displays information such as the Device name , Model & hardware , Android version , Wi-Fi MAC address , Bluetooth address , and Build number .

To access the Settings app from any screen, swipe down on the status bar at the top of the screen and tap the Settings gear icon.

You can also access the Settings app in the launcher screen. Swipe up to open the launcher.

Step 1

Access the Settings app.

Step 2

Tap About phone .

### Access phone status and device information

The Cisco phone status and Device information menus provide information about the device and the connections between the phone and the call control system.

Step 1

Access the Cisco Phone app.

Step 2

Choose one of the following based on your phone's software version:

- For release 1.2(0), tap the Overflow menu.

- For release 1.3(0) or later, tap the Drawer menu.

Step 3

Tap Cisco phone status .

Step 4

Tap Device information .

### Access the About option for a Cisco app

The About menu option provides information about the app itself, including the version number. You might need to provide this information
                                 to the administrator from time to time.

Step 1

Tap the desired app.

Step 2

Choose one of the following based on your phone's software version:

- For release 1.2(0), tap the Overflow menu.

- For release 1.3(0) or later, tap the Drawer menu.

Step 3

Tap About .

### Exit and reenter the Smart Launcher on the phone

When troubleshooting issues on a phone with a Cisco Wireless Phone Configuration Management tool Smart Launcher, you can exit the Smart Launcher to access settings and apps outside of the Smart Launcher.

#### Before you begin

Get the updated Local Phone Unlock Password . The default password to exit the Smart Launcher is **#. Make sure to change this password so you can't exit the Smart Launcher
                                 and access more settings or apps.

Step 1

To exit the launcher, tap the Overflow menu, then tap Exit Launcher , and enter the Local Phone Unlock Password .

Step 2

To reenter the launcher, swipe up to access more apps, and tap the Smart Launcher app.

Note: You can also restart the phone to automatically open the Smart Launcher.

### Capture a screenshot on the phone

When troubleshooting, it may be helpful to have a screenshot of the phone.

You cannot capture a screenshot while the Smart Launcher is activated.

Do one of the following:

Press the Power and Volume down buttons at the same time.

(On Android 13) Swipe up to access the task manager and tap Screenshot .

(On Android 10) Press and hold the Power button, and then tap Screenshot . A notification briefly pops to the foreground and then appears in the notification drawer.

Tap the notification to Share , Edit , or Delete the screenshot.

Unless you delete a screenshot, you can also locate it in the Files app, if available.

## Problem report log bundles

If a user experiences a problem with their phone, they may generate a problem report on the phone and send you the log bundle,
                           or you may need to generate a problem report or retrieve the log bundle yourself.

### Generate a problem report and log bundle

You generate a problem report and log bundle in the phone.

It may take several minutes to generate the problem report and log bundle. When you tap Report Problem , a notification pops to the foreground and then appears in the notification drawer. You know that the report is complete
                                 when the phone vibrates twice and the notification disappears.

For release 1.9(0) or later, when you tap Report Problem , a screen appears and allows you to report a specific issue type before a notification pops up.

For release 1.9(0) or later, the log bundle that is generated also includes a configuration .zip file which contains the configuration
                                             for each application in .txt file format.

Step 1

Access the Cisco Phone app.

Step 2

Choose one of the following based on your phone's software version:

- For release 1.2(0), tap the Overflow menu.

- For release 1.3(0) or later, tap the Drawer menu.

Step 3

Choose one of the following based on your phone's software version:

For release 1.2(0), select Settings > Phone information > Report problem .

For release 1.3(0), tap Report problem .

For release 1.9(0), tap Report problem .

Step 4

For release 1.9(0), perform the following actions:

Select one of the following issue types:

Telephony call (dropper, other)

Audio quality

Battery

Other

Enter the user comment. (Optional)

Select the date and time of the issue ocurred.

Tap Submit .

### Retrieve problem report log bundles

Log bundles include the phone's MAC address, a timestamp, and the string LogBundle in the filename.

#### Before you begin

Get a detailed description and approximate time of the issue from the phone user.

To retrieve log bundles from the phone, you must first enable Web Access through the Cisco Unified
                                    				Communications Manager Vendor Specific Option.

To retrieve log bundles from a problem report upload URL server, you must first define the problem report upload URL in the
                                 phone's Cisco Unified
                                    				Communications Manager Vendor Specific Configuration Layout fields.

The problem report upload URL server must support file uploads using php.

Choose one of these options:

The log bundles appear at the bottom of the page.

To locate the file, it may help to search by MAC address or the string LogBundle .

| Problem | Solution |
|---|---|
| You’re not in a call and the phone goes black and displays the message: Close proximity detected . | Your phone has a proximity sensor at the top right. When this sensor is blocked, the phone screen is black. The sensor is
                                          normally blocked by the face when the earpiece is used to listen to a caller. If you’re not in a call and you see the message: Close proximity detected . The sensor may be covered with a finger or paper or something else that blocks light. If there’s no apparent blockage, clean
                                          the area of the sensor. |
| While using a standard headset, you experience a scratchy or intermittent signal. | The headset connector may be dirty. If available, blow canned air into the connector to clear debris. Always point canned
                                          air orientation at glancing angles away from your face and eyes and always wear safety goggles or glasses when performing
                                          this procedure. Do not use air compressors on the connectors, since they apply too much force. |
| Third Party Application Conflicts | Third party application interference can be eliminated by factory reset and reregistration of a problematic phone. For more
                                          details about the factory reset, see Restoring Factory Defaults in the Cisco Wireless Phone 840 and 860 Deployment Guide . |

| Problem | Solution |
|---|---|
| Unauthorized message appears in the Enter Unity Web Credentials dialog box after the user enters their credentials and selects the Login
                                          option. | Validate that the: User enters the same Username as the Alias field (including case) on the User’s Mailbox in the Cisco Unity Connection voice messaging system. User uses the Web Application password, not the Voicemail pin. Password Settings for the User’s Web Application Password don't have the User Must Change Password at Next Sign-In check box
                                                selected. |
| When the user navigates to the Voicemail tab of the Cisco Phone app, a brief toast notification appears, which states Voicemail connection error. Unable to connect along with an error message Voicemail Authentication failed! Unable to connect to voicemail. Please contact your administrator . Also, you know that visual voicemail is not working on other devices at the same site. | Validate that the Cisco Unity Connection server’s tomcat-trust certificate has been imported into the Cisco Unified
                                             				Communications Manager ’s trust store and the Tomcat service has been restarted since the import occurred. |
| Voicemail connection error. Unable to connect. toast notification appears on the screen when the user navigates to the Voicemail tab of the Cisco Phone app. | Visual voicemail is unable to connect to the Cisco Unity Connection server. Investigate potential connectivity issues between the user’s phone and the server. |
| This feature has been disabled by your administrator appears when the user navigates to the Voicemail tab of the Cisco Phone app. | Enable visual voicemail from the Phone Configuration page in Cisco Unified
                                             				Communications Manager . This error appears only if visual voicemail was enabled previously, and then disabled. |

| Note | To access the Settings app from any screen, swipe down on the status bar at the top of the screen and tap the Settings gear icon. |
|---|---|

| Note | You can also access the Settings app in the launcher screen. Swipe up to open the launcher. |
|---|---|

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Tap About phone . |

| Step 1 | Access the Cisco Phone app. |
|---|---|
| Step 2 | Choose one of the following based on your phone's software version: For release 1.2(0), tap the Overflow menu. For release 1.3(0) or later, tap the Drawer menu. |
| Step 3 | Tap Cisco phone status . |
| Step 4 | Tap Device information . |

| Step 1 | Tap the desired app. |
|---|---|
| Step 2 | Choose one of the following based on your phone's software version: For release 1.2(0), tap the Overflow menu. For release 1.3(0) or later, tap the Drawer menu. |
| Step 3 | Tap About . |

| Step 1 | To exit the launcher, tap the Overflow menu, then tap Exit Launcher , and enter the Local Phone Unlock Password . |
|---|---|
| Step 2 | To reenter the launcher, swipe up to access more apps, and tap the Smart Launcher app. Note: You can also restart the phone to automatically open the Smart Launcher. |

| Note | You cannot capture a screenshot while the Smart Launcher is activated. |
|---|---|

| Do one of the following: Press the Power and Volume down buttons at the same time. (On Android 13) Swipe up to access the task manager and tap Screenshot . (On Android 10) Press and hold the Power button, and then tap Screenshot . A notification briefly pops to the foreground and then appears in the notification drawer. Tap the notification to Share , Edit , or Delete the screenshot. Note Unless you delete a screenshot, you can also locate it in the Files app, if available. | Note | Unless you delete a screenshot, you can also locate it in the Files app, if available. |
|---|---|---|
| Note | Unless you delete a screenshot, you can also locate it in the Files app, if available. |

| Note | Unless you delete a screenshot, you can also locate it in the Files app, if available. |
|---|---|

| Note | For release 1.9(0) or later, the log bundle that is generated also includes a configuration .zip file which contains the configuration
                                             for each application in .txt file format. |
|---|---|

| Step 1 | Access the Cisco Phone app. |
|---|---|
| Step 2 | Choose one of the following based on your phone's software version: For release 1.2(0), tap the Overflow menu. For release 1.3(0) or later, tap the Drawer menu. |
| Step 3 | Choose one of the following based on your phone's software version: For release 1.2(0), select Settings > Phone information > Report problem . For release 1.3(0), tap Report problem . For release 1.9(0), tap Report problem . |
| Step 4 | For release 1.9(0), perform the following actions: Select one of the following issue types: Telephony call (dropper, other) Audio quality Battery Other Enter the user comment. (Optional) Select the date and time of the issue ocurred. Tap Submit . |

| Note | The problem report upload URL server must support file uploads using php. |
|---|---|

| Choose one of these options: Download, or ask the user to download the log bundle from the phone web browser Device Logs tab. Note The log bundles appear at the bottom of the page. Locate the log bundle on the problem report upload URL server. Note To locate the file, it may help to search by MAC address or the string LogBundle . | Note | The log bundles appear at the bottom of the page. | Note | To locate the file, it may help to search by MAC address or the string LogBundle . |
|---|---|---|---|---|
| Note | The log bundles appear at the bottom of the page. |
| Note | To locate the file, it may help to search by MAC address or the string LogBundle . |

| Note | The log bundles appear at the bottom of the page. |
|---|---|

| Note | To locate the file, it may help to search by MAC address or the string LogBundle . |
|---|---|