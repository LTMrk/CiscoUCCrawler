---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-english-userguide-p881-b-8800-3pcc-user-guide-p881-b-8800-3p-b7119fc676
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/english/userguide/p881_b_8800-3pcc-user-guide/p881_b_8800-3pcc-user-guide-110_chapter_01001.html
retrieved_at: 2026-08-21T02:35:40.603388+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

# Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Updated: November 19, 2025

Chapter: Recent Calls

## Chapter: Recent Calls

# Recent Calls

## Recent calls list

Use the Recents list to see the 180 most recent individual calls and call groups.

If your Recents list reaches the maximum size, the next new entry overwrites the oldest entry in the list.

If you have missed calls, the phone shows the number of missed calls for the line on the main screen (up to 99 missed calls).
                              To clear the number from the line, you view your Recents list.

The missed calls number that displays on the main screen may differ from the actual number of calls in the missed calls list.
                              Some missed calls may have been removed from the list by the phone because you have more than 180 entries in the Recents list.

When STIR/SHAKEN support is implemented on the server, the phone displays an extra icon next to the caller ID based on the
                              caller's STIR/SHAKEN verification result. Based on the verification result, the phone displays three types of icons. For more
                              information on the icons, see View your Recent Calls .

## View your Recent Calls

Check to see who's called you recently.

Each line has missed call badging. You can view the number of missed calls per line on the phone screen. The maximum missed
                                          call badge is 99. When you view either the All calls or Missed calls list on the phone screen for a particular line, the missed
                                          call badge for the selected line gets cleared.

The missed call badge and the actual number of missed calls may be different due to a display limit of 180 calls for the Recents
                                          list. This limit consists of outgoing calls, missed calls, and incoming calls. Also, there can be some old missed calls that
                                          get added to the count for the missed call badge. This can get overwritten in the Recents list.

Step 1

Press Applications .

Step 2

Do one of these actions:

- Desk phones: Select a line to view and press Applications .

- Conference phones: Press Settings .

Step 3

Select Recents to access the Recents screen.

You can also press Recents softkey on the phone home screen. You only see this softkey when your administrator configures it on the phone web interface.

When you press the Recents softkey, it directly goes to the All calls screen automatically.

Step 4

In the Recents screen, choose to view all recent calls, or to view a certain kind of recent calls from the following calls list.

- All calls

- Missed calls

- Received calls

- Placed calls

- Display recents from

To know more on how to view call logs using the Display recents from option, see View Calls Logs from Server .

Your administrator configures the Option , Call , Edit call , Filter , and Back softkeys in this screen for All, Placed, Received, and Missed calls list. When configured, you can see those softkeys when
                                          you access any of the menus in the above calls list. The softkeys can also appear as one of the Option menus of calls list based on the configuration.

Your administrator enables support to log Webex calls. In the All calls screen, if the call is represented by a phone number, you can see Call and Edit call softkeys. If the call is not represented by a phone number, the phone doesn't show both the softkeys.

Each menu in the above calls list contains Option softkey with the following menus.

Filter－Allows to access Recents screen, when pressed.

Availability of this menu depends on your adminsitrator's softkey configuration on the phone web interface.

Edit call－Enables to edit any call entry details, when pressed.

Availability of this menu depends on your adminsitrator's softkey configuration on the phone web interface.

Delete entry－Deletes any selected entry, when pressed.

Delete list－Deletes all the entries in the selected menu, when pressed.

Sort by name－Sort according to caller names when selected.

Add contact－Adds a new contact to the directory.

When your administrator enables support to log Webex calls, and in the All calls screen, if the call is represented by a phone number, you can see Add contact option. If the call is not represented by a phone number, the option menu doesn't contain the Add contact option.

An extra icon next to the caller id is displayed on the phone with a color screen indicating a validated caller.

When the icon appears in red color, it indicates a missed call.

Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons.

When you go to the call details of any call, you can view if the call is a missed call or an answered call.

An extra icon next to the caller id is displayed on the phone indicating an illegitimate caller.

When the icon appears in red color, it indicates a missed call.

An extra icon next to the caller id is displayed on the phone indicating an unverified call.

When the icon appears in red color, it indicates a missed call.

## View Webex Call Logs Duration

You can view duration of a received and placed Webex call.

### Before you begin

The phone is onboarded to the Webex cloud server.

Your administrator adds the Display recents from menu on your phone.

When your administrator enables support to show logs from Webex calls, the Webex option is available in the Display recents from menu.

Step 1

Press Applications .

Step 2

Select Recents to access the Recents screen.

You can also press Recents softkey on the phone home screen. You only see this softkey when your administrator configures it on the phone web interface.

When you press the Recents softkey, it directly goes to the All calls screen automatically.

Step 3

In the All calls screen, select a call log.

When you select a placed call or a received call, you can see the call duration in the Duration field. For a missed call, the call duration information is not available.

## Spam Indication for Webex Calls

If your phone is registered to Webex server, the phone displays the following icons as verification in call sessions, local
                              call logs, and Webex call logs.

An extra icon next to the caller id is displayed on the phone with a color screen indicating a validated caller.

When the icon appears in red color, it indicates a missed call.

When you go to the call details of any call, you can view if the call is a missed call or an answered call.

An extra icon next to the caller id is displayed on the phone indicating an illegitimate caller.

When the icon appears in red color, it indicates a missed call.

An extra icon next to the caller id is displayed on the phone indicating an unverified call.

When the icon appears in red color, it indicates a missed call.

## View Calls Logs from Server

You can view a separate list for the BroadWorks XSI server call logs, for the local call logs, and for the logs from Webex
                              cloud server depending on your selection.

The phone does a reverse name lookup against local personal directory when the user navigates the BroadWorks call log on the
                              phone.

### Before you begin

Your administrator adds the Display recents from menu on your phone.

When your administrator enables support to show logs from Webex calls, the Webex option is available in the Display recents from menu.

Step 1

Select a line to view.

Step 2

Press Applications .

Step 3

Select Recents .

Step 4

Select Display recents from and choose one of the options.

- XSI Server : Displays call logs stored on and transferred from the server.

- Phone : Displays call logs stored on the phone.

- Webex : Displays call logs stored in the Webex cloud server.

Step 5

Click Set .

You can view all calls, missed calls, received calls, and placed calls list.

## Return a recent call

Step 1

Do one of the following actions:

- Desk phones—Press Applications .

- Conference phones—Press Settings .

Step 2

Press Recents .

If there is a missed call on a line, you can use the Missed softkey on the phone's home screen to access the Missed calls list.

Step 3

Select the call record that you want to dial.

Step 4

(Optional) Press Edit call to edit the call record.

Step 5

Press the required line button or press Call to place the call.

## Clear the recent calls list

Step 1

Select a line to view.

Step 2

Press Applications .

Step 3

Do one of the following actions:

- Desk phones—Press Applications .

- Conference phones—Press Settings .

Step 4

Select Recents .

Step 5

Select a list that you want to delete.

- All Calls

- Missed Calls

- Received Calls

- Placed Calls

- Display recents from

Step 6

Press Option and select Delete all .

Step 7

Press OK .

## Create a Contact from a Recents Record

Step 1

Select a line to view.

Step 2

Press Applications .

Step 3

Select Recents .

Step 4

Select a list item.

- All Calls

- Missed Calls

- Received Calls

- Placed Calls

To view calls in the Display recents from option, see View Calls Logs from Server .

Step 5

Highlight the individual record that you want to add.

Step 6

Press Option .

Step 7

Press Add contact .

The menu label shows the target directory to which you want to add the contact:

If the menu Add personal address entry displays, you add the contact to the local personal address book.

If the menu Add BroadSoft personal contact displays, you add the contact to the BroadSoft Personal directory.

Step 8

Press Save to add the contact.

## Delete a call record

Step 1

Press Applications .

Step 2

Do one of the following actions:

- Desk phones—Press Applications .

- Conference phones—Press Settings .

Step 3

Select Recents .

Step 4

Choose to view all recent calls, or to view a certain kind of recent call.

- All Calls

- Missed Calls

- Received Calls

- Placed Calls

- Display recents from

Step 5

Highlight the individual record or call group that you want to delete.

Step 6

Press Option .

Step 7

Select Delete entry .

Step 8

Press OK .

For more information, refer to 6800 , 7800 , 8800 , 7832 , and 8832 Multiplatform Phones User Guides.

## Delete All Call Records

You can delete all call history records on your phone.

Step 1

Press Applications .

Step 2

Select Recents .

Step 3

Select All calls .

Step 4

Press Option and select Delete all .

Step 5

Press OK .

| Note | Each line has missed call badging. You can view the number of missed calls per line on the phone screen. The maximum missed
                                          call badge is 99. When you view either the All calls or Missed calls list on the phone screen for a particular line, the missed
                                          call badge for the selected line gets cleared. The missed call badge and the actual number of missed calls may be different due to a display limit of 180 calls for the Recents
                                          list. This limit consists of outgoing calls, missed calls, and incoming calls. Also, there can be some old missed calls that
                                          get added to the count for the missed call badge. This can get overwritten in the Recents list. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Do one of these actions: Desk phones: Select a line to view and press Applications . Conference phones: Press Settings . |
| Step 3 | Select Recents to access the Recents screen. You can also press Recents softkey on the phone home screen. You only see this softkey when your administrator configures it on the phone web interface. When you press the Recents softkey, it directly goes to the All calls screen automatically. |
| Step 4 | In the Recents screen, choose to view all recent calls, or to view a certain kind of recent calls from the following calls list. All calls Missed calls Received calls Placed calls Display recents from To know more on how to view call logs using the Display recents from option, see View Calls Logs from Server . Your administrator configures the Option , Call , Edit call , Filter , and Back softkeys in this screen for All, Placed, Received, and Missed calls list. When configured, you can see those softkeys when
                                          you access any of the menus in the above calls list. The softkeys can also appear as one of the Option menus of calls list based on the configuration. Your administrator enables support to log Webex calls. In the All calls screen, if the call is represented by a phone number, you can see Call and Edit call softkeys. If the call is not represented by a phone number, the phone doesn't show both the softkeys. Each menu in the above calls list contains Option softkey with the following menus. Filter－Allows to access Recents screen, when pressed. Availability of this menu depends on your adminsitrator's softkey configuration on the phone web interface. Edit call－Enables to edit any call entry details, when pressed. Availability of this menu depends on your adminsitrator's softkey configuration on the phone web interface. Delete entry－Deletes any selected entry, when pressed. Delete list－Deletes all the entries in the selected menu, when pressed. Sort by name－Sort according to caller names when selected. Add contact－Adds a new contact to the directory. When your administrator enables support to log Webex calls, and in the All calls screen, if the call is represented by a phone number, you can see Add contact option. If the call is not represented by a phone number, the option menu doesn't contain the Add contact option. Note An extra icon next to the caller id is displayed on the phone with a color screen indicating a validated caller. When the icon appears in red color, it indicates a missed call. Note Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. When you go to the call details of any call, you can view if the call is a missed call or an answered call. An extra icon next to the caller id is displayed on the phone indicating an illegitimate caller. When the icon appears in red color, it indicates a missed call. An extra icon next to the caller id is displayed on the phone indicating an unverified call. When the icon appears in red color, it indicates a missed call. | Note | An extra icon next to the caller id is displayed on the phone with a color screen indicating a validated caller. When the icon appears in red color, it indicates a missed call. Note Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. When you go to the call details of any call, you can view if the call is a missed call or an answered call. An extra icon next to the caller id is displayed on the phone indicating an illegitimate caller. When the icon appears in red color, it indicates a missed call. An extra icon next to the caller id is displayed on the phone indicating an unverified call. When the icon appears in red color, it indicates a missed call. | Note | Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. |
| Note | An extra icon next to the caller id is displayed on the phone with a color screen indicating a validated caller. When the icon appears in red color, it indicates a missed call. Note Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. When you go to the call details of any call, you can view if the call is a missed call or an answered call. An extra icon next to the caller id is displayed on the phone indicating an illegitimate caller. When the icon appears in red color, it indicates a missed call. An extra icon next to the caller id is displayed on the phone indicating an unverified call. When the icon appears in red color, it indicates a missed call. | Note | Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. |
| Note | Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. |

| Note | An extra icon next to the caller id is displayed on the phone with a color screen indicating a validated caller. When the icon appears in red color, it indicates a missed call. Note Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. When you go to the call details of any call, you can view if the call is a missed call or an answered call. An extra icon next to the caller id is displayed on the phone indicating an illegitimate caller. When the icon appears in red color, it indicates a missed call. An extra icon next to the caller id is displayed on the phone indicating an unverified call. When the icon appears in red color, it indicates a missed call. | Note | Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. |
|---|---|---|---|
| Note | Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. |

| Note | Cisco IP Phone 8811 has grayscale screen therefore doesn't support color icons. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Recents to access the Recents screen. You can also press Recents softkey on the phone home screen. You only see this softkey when your administrator configures it on the phone web interface. When you press the Recents softkey, it directly goes to the All calls screen automatically. |
| Step 3 | In the All calls screen, select a call log. When you select a placed call or a received call, you can see the call duration in the Duration field. For a missed call, the call duration information is not available. |

| Step 1 | Select a line to view. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select Recents . |
| Step 4 | Select Display recents from and choose one of the options. XSI Server : Displays call logs stored on and transferred from the server. Phone : Displays call logs stored on the phone. Webex : Displays call logs stored in the Webex cloud server. |
| Step 5 | Click Set . You can view all calls, missed calls, received calls, and placed calls list. |

| Step 1 | Do one of the following actions: Desk phones—Press Applications . Conference phones—Press Settings . |
|---|---|
| Step 2 | Press Recents . If there is a missed call on a line, you can use the Missed softkey on the phone's home screen to access the Missed calls list. |
| Step 3 | Select the call record that you want to dial. |
| Step 4 | (Optional) Press Edit call to edit the call record. |
| Step 5 | Press the required line button or press Call to place the call. |

| Step 1 | Select a line to view. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Do one of the following actions: Desk phones—Press Applications . Conference phones—Press Settings . |
| Step 4 | Select Recents . |
| Step 5 | Select a list that you want to delete. All Calls Missed Calls Received Calls Placed Calls Display recents from |
| Step 6 | Press Option and select Delete all . |
| Step 7 | Press OK . |

| Step 1 | Select a line to view. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select Recents . |
| Step 4 | Select a list item. All Calls Missed Calls Received Calls Placed Calls Display recents from To view calls in the Display recents from option, see View Calls Logs from Server . |
| Step 5 | Highlight the individual record that you want to add. |
| Step 6 | Press Option . |
| Step 7 | Press Add contact . The menu label shows the target directory to which you want to add the contact: If the menu Add personal address entry displays, you add the contact to the local personal address book. If the menu Add BroadSoft personal contact displays, you add the contact to the BroadSoft Personal directory. Your administrator can change the target directory. |
| Step 8 | Press Save to add the contact. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Do one of the following actions: Desk phones—Press Applications . Conference phones—Press Settings . |
| Step 3 | Select Recents . |
| Step 4 | Choose to view all recent calls, or to view a certain kind of recent call. All Calls Missed Calls Received Calls Placed Calls Display recents from |
| Step 5 | Highlight the individual record or call group that you want to delete. |
| Step 6 | Press Option . |
| Step 7 | Select Delete entry . |
| Step 8 | Press OK . Note For more information, refer to 6800 , 7800 , 8800 , 7832 , and 8832 Multiplatform Phones User Guides. | Note | For more information, refer to 6800 , 7800 , 8800 , 7832 , and 8832 Multiplatform Phones User Guides. |
| Note | For more information, refer to 6800 , 7800 , 8800 , 7832 , and 8832 Multiplatform Phones User Guides. |

| Note | For more information, refer to 6800 , 7800 , 8800 , 7832 , and 8832 Multiplatform Phones User Guides. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Recents . |
| Step 3 | Select All calls . |
| Step 4 | Press Option and select Delete all . |
| Step 5 | Press OK . |