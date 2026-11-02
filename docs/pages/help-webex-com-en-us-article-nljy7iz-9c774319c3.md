---
doc_id: help-webex-com-en-us-article-nljy7iz-9c774319c3
source_url: https://help.webex.com/en-us/article/nljy7iz
retrieved_at: 2026-11-02T13:07:22.478997+00:00
---

## Set up the calendar service

After you enable the calendar service and choose a cloud service on Unified CM, the softkey Calendar will display on the phone screen. With the softkey, users can scan a QR code to sign in to the calendar service. After the sign-in is successful, the users can directly join various types of meetings on the phone.

After the calendar service configuration is finished, the phone will try to retrieve the calendar items and relevant meeting links (SIP URLs). Only when the SIP URIs for the supported meeting types are identified, the phone can recognize the meeting types. As a result, the softkey Join will display on the calendar item. Then user can select the softkey to join a meeting from the calendar list.

- Currently, this feature supports the English language only.

- If you choose Microsoft as the cloud service for the calendar meeting, the
            calendar service only supports the Microsoft Office 365 Calendar. The Microsoft Exchange
            Calendar is not supported. In addition, the user must have a Microsoft account to sign
            in to the calendar service.

- If you choose Webex as the cloud service for the calendar meeting, the user
            must have a Webex account to sign in to the calendar service.

Before you begin

Cisco Video Integration for Microsoft Teams (VIMT) license is required for each device that
        joins the meeting. If users join the meeting via third party, the Microsoft Teams CVI
        license might be required.

Do one of the following actions from Cisco Unified CM Administration:

To set up the feature for a specific phone:

Choose Device > Phone and locate the phone that you want to set up.

To set up the feature for a group of phones:

Choose Device > Device Settings > Common Phone Profile and locate the profile that you want to set up.

To set up the feature for all phones:

Choose System > Enterprise Phone Configuration .

Ensure that CUCM can dial external SIP URI calls with SIP and expressway setup.

Set the following fields:

Calendar Service : Determines whether to enable or disable the calendar service. Once enabled, the users can find the softkey Calendar on the phone screen.

Default: Disabled.

Cloud Service : Specifies which cloud service is used for the calendar service.

Options:

- Microsoft—The cloud service is Microsoft Office 365 Calendar

- Webex—The cloud service is Webex Hybrid Calendar Service

Default: Microsoft

Calendar Login Timeout (days) : Specifies the number of days for the login duration. The user will automatically log out from the calendar service after the configured days. The maximum duration is 30 days.

Default: Empty

If the value is empty, the users remain logged in until they manually log out from the phone.

Click Save .

After the configuration, you can see the Calendar softkey or soft button on the phone screen, depending on your phone model.

If you choose Webex as the cloud service in Step 3, make sure the phone can access the following services via the HTTPS protocol (port 443):

- https://webexapis.com

- https://xxxx.webex.com

- https://xxxx.wbx2.com

If you choose Microsoft as the cloud service in Step 3, perform the following actions:

Check Microsoft services access.

Make sure that the phone can access the following services via the HTTPS protocol (port 443):

HTTP URLs to get user code, request token:

https://login.microsoftonline.com/organizations/oauth2/v2.0/devicecode

https://login.microsoftonline.com/organizations/oauth2/v2.0/token

HTTP URLs to retrieve calendar:

https://graph.microsoft.com/v1.0/me/calendar/calendarView?$orderby=start/dateTime&startDateTime=%s&endDateTime=%s&$select=subject,organizer,attendees,start,end,onlinemeeting,body,isCancelled&$top=%d

HTTP URLs to logout:

https://login.microsoftonline.com/common/oauth2/v2.0/logout

Authorize the OBTP application in Entra ID

## Authorize the OBTP application in Entra ID

To authorize the Cisco Phone OBTP application in Microsoft Entra ID, you can use one of the methods according to the Microsoft Entra role:

- The role has admin permissions in Entra ID.

- The role doesn't have admin permissions in Entra ID.

### Enable the OBTP application by using a role that has admin permissions in Entra ID

You can provide the user with an account that has the admin permissions in Entra ID. The admin role can manage applications in the Enterprise Applications Catalog of Entra ID.

By using the account with the admin privileges, the user can directly sign in to the OBTP application on the phone. For example:

Use the provided account to sign in to the OBTP application:

When the users sign in to the OBTP application at the first time, typically they will be prompted to accept the permissions request for the application integration on the phone. For example:

If you want to avoid the permissions request for the users, ensure that the Entra ID is configured to provide the requested permissions on behalf of your organization. For example:

The configuration in Microsoft Entra is out of scope of this article. For more information, see Quickstart: Add an enterprise application .

As the administrator of the Entra ID, you can find the application (for example, "Cisco Phone OBTP") in Entra ID Enterprise applications catalog. The navigation path is: Identity > Applications > Enterprise applications > All applications .

### Enable the OBTP service by using a role that doesn't have admin permissions in Entra ID

If you don't have the admin permissions in Entra ID, you need to provide the following URL to the Microsoft Entra administrators for support, so they can authorize the calendar service integration on behalf of the users. The Entra administrators will also create the application (for example, "Cisco Phone OBTP") in Entra ID applications catalog.

URL: https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=ac3f3f1a-96b5-4d6a-8449-cba134140123&scope=https%3A%2F%2Fgraph.microsoft.com%2FCalendars.Read%20https%3A%2F%2Fgraph.microsoft.com%2Foffline_access

The Entra ID administrators only need the admin permission in Entra ID. They doesn’t need
          to exist in Webex or any other application in Enterprise catalog applications.

After the Entra ID administrators approve the OBTP service for the associated Microsoft Tenant, the users can sign in to the Calendar service on the phone.

| 1 | Do one of the following actions from Cisco Unified CM Administration: To set up the feature for a specific phone: Choose Device > Phone and locate the phone that you want to set up. To set up the feature for a group of phones: Choose Device > Device Settings > Common Phone Profile and locate the profile that you want to set up. To set up the feature for all phones: Choose System > Enterprise Phone Configuration . |
|---|---|
| 2 | Ensure that CUCM can dial external SIP URI calls with SIP and expressway setup. |
| 3 | Set the following fields: Calendar Service : Determines whether to enable or disable the calendar service. Once enabled, the users can find the softkey Calendar on the phone screen. Default: Disabled. Cloud Service : Specifies which cloud service is used for the calendar service. Options: Microsoft—The cloud service is Microsoft Office 365 Calendar Webex—The cloud service is Webex Hybrid Calendar Service Default: Microsoft Calendar Login Timeout (days) : Specifies the number of days for the login duration. The user will automatically log out from the calendar service after the configured days. The maximum duration is 30 days. Default: Empty If the value is empty, the users remain logged in until they manually log out from the phone. |
| 4 | Click Save . After the configuration, you can see the Calendar softkey or soft button on the phone screen, depending on your phone model. |
| 5 | If you choose Webex as the cloud service in Step 3, make sure the phone can access the following services via the HTTPS protocol (port 443): https://webexapis.com https://xxxx.webex.com https://xxxx.wbx2.com |
| 6 | If you choose Microsoft as the cloud service in Step 3, perform the following actions: Check Microsoft services access. Make sure that the phone can access the following services via the HTTPS protocol (port 443): HTTP URLs to get user code, request token: https://login.microsoftonline.com/organizations/oauth2/v2.0/devicecode https://login.microsoftonline.com/organizations/oauth2/v2.0/token HTTP URLs to retrieve calendar: https://graph.microsoft.com/v1.0/me/calendar/calendarView?$orderby=start/dateTime&startDateTime=%s&endDateTime=%s&$select=subject,organizer,attendees,start,end,onlinemeeting,body,isCancelled&$top=%d HTTP URLs to logout: https://login.microsoftonline.com/common/oauth2/v2.0/logout Authorize the OBTP application in Entra ID |