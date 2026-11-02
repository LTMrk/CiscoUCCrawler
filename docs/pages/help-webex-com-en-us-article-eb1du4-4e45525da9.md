---
doc_id: help-webex-com-en-us-article-eb1du4-4e45525da9
source_url: https://help.webex.com/en-us/article/eb1du4
retrieved_at: 2026-11-02T13:07:13.635377+00:00
---

## Hot Desking overview

Hot Desking allows your organization to make the best use of office space. People using
      shared workspaces can sign in and book a shared phone for their workday.

As an administrator, you must configure the Hot Desking feature for both devices and users to
      enable access from the phone. Before setting it up in Control Hub, we recommend reading the
      following information to understand how it works for users.

Phones with the Hot Desking feature
        enabled show a QR code and sign-in options on the screen. If a workspace phone is set up as
        a hot-desk-only device, it displays the workspace name without a directory number, allowing
        only emergency calls before sign-in. If the phone displays the workspace name with a
        directory number, users can make and receive calls without signing in but can't view their
        directory, calendar, or call history.

Depending on configurations, users can choose one of the
        following ways to sign in to a shared phone and access its full features.

Signing in with Webex account

The user scans the QR code on the phone screen with their mobile device and follows the
            prompts to sign in via either Webex App or a web browser on the mobile device.

Signing in with voice portal (Only supported on 9800 Series and 8875)

The user will be prompted to enter their voice mailbox ID and passcode for
            authentication. Depending on the user's and the device's locations, these mailbox
            numbers can be used for Hot Desking sign-in:

- Extension number

- Enterprise Significant Number (ESN)

- E.164 format telephone number (without the + prefix)

- National format telephone number

- Enterprise Significant Number (ESN)

- E.164 format telephone number (without the + prefix)

- Extension number — works only if the "Allow extension dialing between
                    locations" policy for the organization is enabled and the extension is unique
                    across all locations.

- National format telephone number — works if both locations use the same
                    country code.

Depending on the phone model, the user can begin the sign-in process in the following
            ways:

Press the Sign in softkey or dial *30 on the phone.

Tap Sign in via voice portal or dial *30 .

After the user signs in and books the device, the phone is reprovisioned with their
        own directory number. If configured, the user's Webex calendar and call history also load
        onto the phone.

When the booking duration ends, the
        user is automatically signed out and the phone is provisioned back to the workspace device
        for others to book. However, the user can also end the booking earlier by manually signing
        out via the phone or through the mobile or desktop version of Webex App. After sign-out, all
        user information will be removed from the phone.

If there's an active call on the
        phone when the booking duration expires, the auto sign-out won't happen until the call ends.
        Remind your users to end all calls before they leave. They can't sign out via Webex App when
        the phone is on a call.

## Enable Hot Desking for a workspace phone

If your phone is added as a hot-desk-only device , the Hot Desking feature is
        enabled by default. You can't disable it unless the workspace's calling service is changed
        from hot desk only.

Follow these steps to enable the Hot Desking feature on a workspace phone:

Before you begin

Your phone has registered to Webex Calling as a shared device in a workspace. See Add a phone to a new workspace for the instructions.

From the customer view in Control Hub , go to Management > Workspaces .

Locate your phone and click it to open its settings.

On the Scheduling tab, choose Hot desking as the scheduling option.

Click Save .

## Enable Hot Desking sign-in via voice portal

To enable sign-in to Hot Desking devices using the voice portal, this feature must be
        enabled for both the device’s location and the user. The location setting ensures that
        phones in that location support sign-in via voice portal, while the user setting allows
        administrators to restrict access for specific users. By default, the feature is enabled in
        both the location-level and user-level configurations.

Keep the following notes in mind while configuring the Hot Desking feature:

- The voice portal in the device's location must have a phone number or extension
            configured.

- If the organization has a default voicemail passcode set, voice portal sign-in will be
            blocked.

- Hot Desking voice portal sign-in supports logging in with a Hot Desk user's voice
            mailbox. Logging in using mailboxes for groups, workspaces, or virtual lines isn't
            supported.

- Before signing in to the phone using the voice portal, users must change their
            voicemail PIN from the default.

- If a user enters the wrong PIN three times when signing in to the voice portal, the
            mailbox will be locked. To unlock it, reset the voicemail PIN .

Follow these steps to enable the voice portal sign-in option:

- In Control
                  Hub , go to Locations and find your location.

- In the location settings, go to Calling > Calling features settings > Hot Desking and toggle on Hot desk sign in using voice
                  portal .

- In Control
                  Hub , go to Users and find the user.

- In the user settings, go to Calling > Between-user permissions > Hot Desking and toggle on Hot desk sign in using voice
                  portal .

Click Save .

## Configure phone lines for a Hot Desking user

By default, the user's primary line is used for Hot Desking. You can add more lines for the user to use on a shared phone.

From the customer view in Control Hub , go to Management > Users , and then select the user.

In the Between-user permissions section on the Calling tab, select Hot Desking .

Click Configure lines .

Click on Line 2 and choose the desired directory number to add.

By default, the user's primary line takes Line 1. If you need to set both Line 1 and Line 2 as primary lines, click on Line 1.

Repeat Step 4 to add more lines.

Click Save .

For large organizations, the administrator must select a location before configuring
            additional calling lines.

Click icon, and you can see the location filter appears. The
            administrator then can select a line.

For a regular organization, the location filter is not available, and the administrator
            can select a line.

## Manage user bookings

If a workspace phone has been booked, you can change or end the booking in Control Hub.

From the customer view in Control Hub , go to Management > Workspaces , and then select your workspace.

In the Real-Time Utilization Metrics section, edit the booking range or end the session as needed.

- To change the booking, click the More button next to the booking time and click Modify booking end time . Then, edit the end time and save the change.

- To end the booking, click End hot desking session and confirm the action in the prompt window.

| 1 | From the customer view in Control Hub , go to Management > Workspaces . |
|---|---|
| 2 | Locate your phone and click it to open its settings. |
| 3 | On the Scheduling tab, choose Hot desking as the scheduling option. |
| 4 | Click Save . |

| 1 | Follow these steps to enable the voice portal sign-in option: Enable the feature for a location In Control
                  Hub , go to Locations and find your location. In the location settings, go to Calling > Calling features settings > Hot Desking and toggle on Hot desk sign in using voice
                  portal . Enable the feature for a user In Control
                  Hub , go to Users and find the user. In the user settings, go to Calling > Between-user permissions > Hot Desking and toggle on Hot desk sign in using voice
                  portal . |
|---|---|
| 2 | Click Save . |

| 1 | From the customer view in Control Hub , go to Management > Users , and then select the user. |
|---|---|
| 2 | In the Between-user permissions section on the Calling tab, select Hot Desking . |
| 3 | Click Configure lines . |
| 4 | Click on Line 2 and choose the desired directory number to add. By default, the user's primary line takes Line 1. If you need to set both Line 1 and Line 2 as primary lines, click on Line 1. |
| 5 | Repeat Step 4 to add more lines. |
| 6 | Click Save . For large organizations, the administrator must select a location before configuring
            additional calling lines. Click icon, and you can see the location filter appears. The
            administrator then can select a line. For a regular organization, the location filter is not available, and the administrator
            can select a line. |

| 1 | From the customer view in Control Hub , go to Management > Workspaces , and then select your workspace. |
|---|---|
| 2 | In the Real-Time Utilization Metrics section, edit the booking range or end the session as needed. To change the booking, click the More button next to the booking time and click Modify booking end time . Then, edit the end time and save the change. To end the booking, click End hot desking session and confirm the action in the prompt window. |

## Figuras

![For 9841, 9851, and 9861 phones](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483151.png)

![Icon for 9871 and 8875 for common topics](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/485001-486000/485950.png)

![the plus icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473335.png)

![Location filter for large orgs](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/494001-495000/494672.png)

![Icon for More button](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/486001-487000/486265.png)