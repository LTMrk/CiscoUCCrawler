---
doc_id: help-webex-com-en-us-article-212ytk-5330352d05
source_url: https://help.webex.com/en-us/article/212ytk
retrieved_at: 2026-11-02T13:07:18.348614+00:00
---

## Check your calendar list on the phone

You can access the calendar list on the phone to check calendar items for the rest of the day.

The calendar list contains different types of meetings or events, such as, Webex Meeting,
        Microsoft Teams Meeting, Zoom Meeting, and Personal Event. Typically, the calendar list can
        display a maximum of 20 calendar items.

Only the Cisco Video Phone 8875 that uses Microsoft cloud calendar service can support the Zoom Meeting.

To access the calendar list, your phone must be connected to Internet. In addition, you must sign in to a cloud calendar service with a valid account. According to your administrator's configuration on the call control system, you might be prompted to sign in to the cloud calendar service with a Microsoft or Webex account.

After the sign-in is successful, your account will be logged out automatically after certain days. If your administrator doesn't enable the auto log-out, your account will remain log-in until you manually sign out from the phone.

When the phone restarts, your account doesn't log out automatically from the cloud calendar service. In addition, even though you log out of extension mobility, your account can still remain in the cloud calendar service.

- 9841 / 9851 / 9861

- 9871 / 8875

Before you begin

- Your phone has registered to Cisco Unified Communications Manager (Unified CM) or Cisco Webex Dedicated Instance (Webex DI).

- Your administrator has enabled and configured the calendar feature on your phone.

- A Microsoft account is required if the calendar service works with the Microsoft cloud calendar service.

- A Webex account is required if the calendar service works with Webex hybrid calendar service.

Locate and press Calendar to open the calendar list that contains your scheduled meetings or events, or both.

For Cisco Desk Phone 9851 and 9861, you can also tap Calendar to open the calendar list. The LED of the button turns on when your administrator enables the calendar feature.

Sign in to a cloud calendar service in one of the following ways:

If this is the first time you use the calendar feature, you're prompted to sign in
              with your Microsoft or Webex account. After a successful sign-in, the meetings that
              are associated with your account will be shared on the phone.

Use the camera on your mobile phone to scan the QR code displayed on the phone
                    screen. The phone might take seconds to generate a one-time user code for you.
                    The code will expire after 10 minutes.

Example:

On your mobile phone that shows the Microsoft sign-in page, enter the generated
                    user code and proceed.

You can also access the web page to enter the generated user code: https://login.microsoftonline.com/common/oauth2/deviceauth

Enter your user credentials to sign in to your Microsoft account.

If the phone prompts you for the permission to read the calendar data of your
                    account, grant the permissions. The phone loads your calendar.

For the first time, you may be prompted to ask for admin approval. After you
                      input your reason for use, the request will be pending on the approval from
                      the Microsoft admin. Once the admin approves your request, you can sign in to
                      the calendar service.

Use the camera on your mobile phone to scan the QR code displayed on the phone
                    screen.

Example:

On your mobile phone that shows the Webex sign-in page, enter your email
                    address.

Proceed by following the on-screen guide on your mobile device.

If prompted to accept the permissions requested by the Webex Web App, accept
                    the permissions.

On the Calendar screen, use the Navigation Cluster button to go through your scheduled calendar items that are fetched from the calendar service. Typically, each calendar item shows the following information:

- Starting in <n> minutes : Describes how soon the meeting will start, where the value range of <n> is 1–5.

- In progress <duration_time> : Shows that the meeting has started for the displayed duration and your phone still isn't in the meeting.

- Meeting title

- Meeting organizer

- : Webex Meeting

- : Microsoft Teams Meeting

- : Personal Event (without meeting URI)

- Meeting start time and end time

If you sign in the calendar service with a Microsoft account, you can press Refresh to manually refresh the calendar list to check the latest status of the calendar items or to find the newly scheduled calendar items for the rest of the day.

By default, the calendar list refreshes automatically around 9:00 AM and 12:00 PM. After the refresh, the finished and canceled calendar items will be removed from the list.

If you sign in with a Webex account, the Refresh softkey
              doesn't appear. This is because the refresh operation can always be triggered
              automatically on the phone.

To check details of a calendar item (meeting or event), navigate to the item and press Info .

If you sign in to the calendar service with a Microsoft account, you can further press Details to view more information about the meeting or event.

To join a meeting, navigate to it and press Join .

For the meeting with an invalid SIP URI address or unrecognized meeting type, the Join softkey doesn't appear. In addition, you can't join a
              personal event since it doesn't contain the SIP URI address.

To sign out your account from the phone, press Sign out on the calendar list screen, and then confirm it.

The information of your meetings and events will be cleared from the phone.

Before you begin

- Your phone has registered to Cisco Unified Communications Manager (Unified CM) or Cisco Webex Dedicated Instance (Webex DI).

- Your administrator has enabled and configured the calendar feature on your phone.

- A Microsoft account is required if the calendar service works with the Microsoft cloud calendar service.

- A Webex account is required if the calendar service works with Webex hybrid calendar service.

Tap Calendar to open the calendar list that contains your scheduled meetings or events, or both.

The digit number on the icon shows the count of the calendar items (including meetings and events) for the rest of the day.

Sign in to a cloud calendar service in one of the following ways:

If this is the first time you use the calendar feature, you're prompted to sign in
              with your Microsoft or Webex account. After a successful sign-in, the meetings that
              are associated with your account will be shared on the phone.

Use the camera on your mobile phone to scan the QR code displayed on the phone
                    screen. The phone might take seconds to generate a one-time user code for you.
                    The code will expire after 10 minutes.

Example:

On your mobile phone that shows the Microsoft sign-in page, enter the generated
                    user code and proceed.

You can also access the web page to enter the generated user code: https://login.microsoftonline.com/common/oauth2/deviceauth

Enter your user credentials to sign in to your Microsoft account.

If the phone prompts you for the permission to read the calendar data of your
                    account, grant the permissions. The phone loads your calendar.

For the first time, you may be prompted to ask for admin approval. After you
                      input your reason for use, the request will be pending on the approval from
                      the Microsoft admin. Once the admin approves your request, you can sign in to
                      the calendar service.

Use the camera on your mobile phone to scan the QR code displayed on the phone
                    screen.

Example:

On your mobile phone that shows the Webex sign-in page, enter your email
                    address.

Proceed by following the on-screen guide on your mobile device.

If prompted to accept the permissions requested by the Webex Web App, accept
                    the permissions.

On the Calendar screen, scroll through the calendar list to view your scheduled calendar items that are fetched from the cloud calendar service. Typically, each calendar item shows the following information:

- Starting in <n> minutes : Describes how soon the meeting will start, where the value range of <n> is 1–5.

- In progress <duration_time> : Shows that the meeting has started for the displayed duration and your phone still isn't in the meeting.

- Meeting title

- Meeting organizer

- : Webex Meeting

- : Microsoft Teams Meeting

The Zoom meeting is supported only on Cisco Video Phone 8875.

- : Personal event (without meeting URI)

- Meeting start time and end time

If you sign in the calendar service with a Microsoft account, you can tap Refresh to manually refresh the calendar list to check the latest status of the calendar items or to find the newly scheduled calendar items for the rest of the day.

By default, the calendar list refreshes automatically around 9:00 AM and 12:00 PM. After the refresh, the finished and canceled calendar items will be removed from the list.

If you sign in with a Webex account, the Refresh soft button
              doesn't appear. This is because the refresh operation can always be triggered
              automatically on the phone.

If you sign in the calendar service with a Microsoft account, you can tap the calendar item to show more information about the meeting or event.

To join a meeting, tap Join .

For the meeting with an invalid SIP URI address or unrecognized meeting type, the Join soft button doesn't display. In addition, you can't join
              a personal event since it doesn't contain the SIP URI address.

To sign out your account from the phone, tap Sign-out on the calendar list, and then confirm it.

The information of your meetings and events will be cleared from the phone.

## Join a meeting on your phone

You're prompted to join a meeting 5 minutes before it starts. If you choose to snooze the reminder, you will be prompted again 5 minutes later. If you ignore the notification, you will not be prompted again, but you can still find and join the meeting from the calendar list, which shows you the calendar items for the rest of the day.

If your phone can recognize and support the meeting link contained in the calendar item, the calendar item can display the Join softkey or soft button (depending on your phone model). When you press the softkey or tap the soft button, the phone makes a SIP call to the SIP URI address of the meeting.

The phone supports the following meeting types:

The SIP URI address is " <example> @webex.com".

The SIP URI address is " <example> @m.webex.com".

Cisco Video Integration for Microsoft Teams (VIMT) license is required for each device that joins the meeting.

The SIP URI address is " <example> @zoomcrc.com".

The type requires the meeting organizer to have a Zoom CRC license.

The Zoom meeting is supported only on Cisco Video Phone 8875.

Depending on the meeting configuration by the host, you may be prompted for the PIN code when joining a meeting. Usually, the PIN code is included in the meeting details.

Before using your phone for meetings, keep the following points in mind:

- You can join multiple meetings at a time. However, only one meeting that you join can be active, the others will be put to on-hold status.

- You can't be in a meeting and on a call simultaneously.

- If you check your voicemail during a meeting, the meeting will be put to on-hold status automatically.

- 9841 / 9851 / 9861

- 9871 / 8875

Before you begin

- Your administrator has enabled and configured the calendar feature on your phone.

- You have signed in to the cloud calendar service previously.

When prompted, press Join from the meeting notification to join a meeting.

Based on the meeting type, user license, and admin configuration, you may join a PSTN
              audio meeting. For example, only PSTN audio meeting is supported for the Zoom
              meeting.

When you are prompted with multiple meetings at the same time, all the relevant meeting notifications display on the phone screen. A digit at the title shows the count of the upcoming meetings. You can choose one to join.

If prompted, enter the meeting password.

You can either obtain the password from the meeting details or from the meeting host.

To leave the meeting, press End call .

To rejoin the meeting you left, locate and press Calendar on the phone home screen,  navigate to your desired meeting, and then press Join .

If you go back to the phone home screen during a meeting, the meeting is still ongoing.

Press the line key to view the meeting status, and perform the action as needed with the available softkeys.

Before you begin

- Your administrator has enabled and configured the calendar feature on your phone.

- You have signed in to the calendar list previously.

When prompted, tap Join from the meeting notification to join a meeting.

Based on the meeting type, user license, and admin configuration, you may join a PSTN
              audio meeting. For example, only PSTN audio meeting is supported for the Zoom
              meeting.

When you are prompted with multiple meetings at the same time, all the relevant meeting notifications display on the phone screen. A digit at the title shows the count of the upcoming meetings. You can choose one to join. Also, you can choose to snooze or ignore all the meeting notifications.

If prompted, enter the meeting password.

You can either obtain the password from the meeting details or from the meeting host.

To leave the meeting, tap End call .

To rejoin the meeting you left, tap Calendar on the phone home screen, and then tap Join for your desired meeting.

If you go back to the phone home screen during a meeting, the meeting is still ongoing. You can return to the meeting screen through the calls bar displayed at the bottom of the screen. Perform the action as needed with the available soft buttons.

| 1 | Locate and press Calendar to open the calendar list that contains your scheduled meetings or events, or both. For Cisco Desk Phone 9851 and 9861, you can also tap Calendar to open the calendar list. The LED of the button turns on when your administrator enables the calendar feature. |
|---|---|
| 2 | Sign in to a cloud calendar service in one of the following ways: If this is the first time you use the calendar feature, you're prompted to sign in
              with your Microsoft or Webex account. After a successful sign-in, the meetings that
              are associated with your account will be shared on the phone. Sign in with your Microsoft account Use the camera on your mobile phone to scan the QR code displayed on the phone
                    screen. The phone might take seconds to generate a one-time user code for you.
                    The code will expire after 10 minutes. Example: On your mobile phone that shows the Microsoft sign-in page, enter the generated
                    user code and proceed. You can also access the web page to enter the generated user code: https://login.microsoftonline.com/common/oauth2/deviceauth Enter your user credentials to sign in to your Microsoft account. If the phone prompts you for the permission to read the calendar data of your
                    account, grant the permissions. The phone loads your calendar. For the first time, you may be prompted to ask for admin approval. After you
                      input your reason for use, the request will be pending on the approval from
                      the Microsoft admin. Once the admin approves your request, you can sign in to
                      the calendar service. Sign in with your Webex account Use the camera on your mobile phone to scan the QR code displayed on the phone
                    screen. Example: On your mobile phone that shows the Webex sign-in page, enter your email
                    address. Proceed by following the on-screen guide on your mobile device. If prompted to accept the permissions requested by the Webex Web App, accept
                    the permissions. |
| 3 | On the Calendar screen, use the Navigation Cluster button to go through your scheduled calendar items that are fetched from the calendar service. Typically, each calendar item shows the following information: Meeting status: Starting in <n> minutes : Describes how soon the meeting will start, where the value range of <n> is 1–5. In progress <duration_time> : Shows that the meeting has started for the displayed duration and your phone still isn't in the meeting. Meeting title Meeting organizer Meeting type: : Webex Meeting : Microsoft Teams Meeting : Personal Event (without meeting URI) Meeting start time and end time |
| 4 | If you sign in the calendar service with a Microsoft account, you can press Refresh to manually refresh the calendar list to check the latest status of the calendar items or to find the newly scheduled calendar items for the rest of the day. By default, the calendar list refreshes automatically around 9:00 AM and 12:00 PM. After the refresh, the finished and canceled calendar items will be removed from the list. If you sign in with a Webex account, the Refresh softkey
              doesn't appear. This is because the refresh operation can always be triggered
              automatically on the phone. |
| 5 | To check details of a calendar item (meeting or event), navigate to the item and press Info . If you sign in to the calendar service with a Microsoft account, you can further press Details to view more information about the meeting or event. |
| 6 | To join a meeting, navigate to it and press Join . For the meeting with an invalid SIP URI address or unrecognized meeting type, the Join softkey doesn't appear. In addition, you can't join a
              personal event since it doesn't contain the SIP URI address. |
| 7 | To sign out your account from the phone, press Sign out on the calendar list screen, and then confirm it. The information of your meetings and events will be cleared from the phone. |

| 1 | Tap Calendar to open the calendar list that contains your scheduled meetings or events, or both. The digit number on the icon shows the count of the calendar items (including meetings and events) for the rest of the day. |
|---|---|
| 2 | Sign in to a cloud calendar service in one of the following ways: If this is the first time you use the calendar feature, you're prompted to sign in
              with your Microsoft or Webex account. After a successful sign-in, the meetings that
              are associated with your account will be shared on the phone. Sign in with your Microsoft account Use the camera on your mobile phone to scan the QR code displayed on the phone
                    screen. The phone might take seconds to generate a one-time user code for you.
                    The code will expire after 10 minutes. Example: On your mobile phone that shows the Microsoft sign-in page, enter the generated
                    user code and proceed. You can also access the web page to enter the generated user code: https://login.microsoftonline.com/common/oauth2/deviceauth Enter your user credentials to sign in to your Microsoft account. If the phone prompts you for the permission to read the calendar data of your
                    account, grant the permissions. The phone loads your calendar. For the first time, you may be prompted to ask for admin approval. After you
                      input your reason for use, the request will be pending on the approval from
                      the Microsoft admin. Once the admin approves your request, you can sign in to
                      the calendar service. Sign in with your Webex account Use the camera on your mobile phone to scan the QR code displayed on the phone
                    screen. Example: On your mobile phone that shows the Webex sign-in page, enter your email
                    address. Proceed by following the on-screen guide on your mobile device. If prompted to accept the permissions requested by the Webex Web App, accept
                    the permissions. |
| 3 | On the Calendar screen, scroll through the calendar list to view your scheduled calendar items that are fetched from the cloud calendar service. Typically, each calendar item shows the following information: Meeting status: Starting in <n> minutes : Describes how soon the meeting will start, where the value range of <n> is 1–5. In progress <duration_time> : Shows that the meeting has started for the displayed duration and your phone still isn't in the meeting. Meeting title Meeting organizer Meeting type: : Webex Meeting : Microsoft Teams Meeting : Zoom Meeting The Zoom meeting is supported only on Cisco Video Phone 8875. : Personal event (without meeting URI) Meeting start time and end time |
| 4 | If you sign in the calendar service with a Microsoft account, you can tap Refresh to manually refresh the calendar list to check the latest status of the calendar items or to find the newly scheduled calendar items for the rest of the day. By default, the calendar list refreshes automatically around 9:00 AM and 12:00 PM. After the refresh, the finished and canceled calendar items will be removed from the list. If you sign in with a Webex account, the Refresh soft button
              doesn't appear. This is because the refresh operation can always be triggered
              automatically on the phone. |
| 5 | If you sign in the calendar service with a Microsoft account, you can tap the calendar item to show more information about the meeting or event. |
| 6 | To join a meeting, tap Join . For the meeting with an invalid SIP URI address or unrecognized meeting type, the Join soft button doesn't display. In addition, you can't join
              a personal event since it doesn't contain the SIP URI address. |
| 7 | To sign out your account from the phone, tap Sign-out on the calendar list, and then confirm it. The information of your meetings and events will be cleared from the phone. |

| 1 | When prompted, press Join from the meeting notification to join a meeting. Based on the meeting type, user license, and admin configuration, you may join a PSTN
              audio meeting. For example, only PSTN audio meeting is supported for the Zoom
              meeting. When you are prompted with multiple meetings at the same time, all the relevant meeting notifications display on the phone screen. A digit at the title shows the count of the upcoming meetings. You can choose one to join. |
|---|---|
| 2 | If prompted, enter the meeting password. You can either obtain the password from the meeting details or from the meeting host. |
| 3 | To leave the meeting, press End call . |
| 4 | To rejoin the meeting you left, locate and press Calendar on the phone home screen,  navigate to your desired meeting, and then press Join . |
| 5 | If you go back to the phone home screen during a meeting, the meeting is still ongoing. Press the line key to view the meeting status, and perform the action as needed with the available softkeys. |

| 1 | When prompted, tap Join from the meeting notification to join a meeting. Based on the meeting type, user license, and admin configuration, you may join a PSTN
              audio meeting. For example, only PSTN audio meeting is supported for the Zoom
              meeting. When you are prompted with multiple meetings at the same time, all the relevant meeting notifications display on the phone screen. A digit at the title shows the count of the upcoming meetings. You can choose one to join. Also, you can choose to snooze or ignore all the meeting notifications. |
|---|---|
| 2 | If prompted, enter the meeting password. You can either obtain the password from the meeting details or from the meeting host. |
| 3 | To leave the meeting, tap End call . |
| 4 | To rejoin the meeting you left, tap Calendar on the phone home screen, and then tap Join for your desired meeting. |
| 5 | If you go back to the phone home screen during a meeting, the meeting is still ongoing. You can return to the meeting screen through the calls bar displayed at the bottom of the screen. Perform the action as needed with the available soft buttons. |

## Figuras

![Calendar hardkey](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/481001-482000/481011.png)

![Microsoft login for calendar meeting on 9861](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489766.png)

![Webex login for calendar meeting on 9861](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489764.png)

![Webex meeting icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/481001-482000/481013.jpg)

![Microsoft Teams Meeting icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/481001-482000/481014.jpg)

![General meeting (without URI) icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/481001-482000/481016.jpg)

![The "Meeting" icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/481001-482000/481012.jpg)

![Microsoft account login for calendar meeting on 9871 or 8875](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489767.png)

![Webex login for calendar meeting on 9871 or 8875](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489765.png)

![Zoom Meeting icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/481001-482000/481015.jpg)

![the Refresh soft button](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/481001-482000/481017.jpg)

![Log-out meetings list icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/481001-482000/481018.jpg)