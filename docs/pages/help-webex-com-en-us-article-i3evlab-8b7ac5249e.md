---
doc_id: help-webex-com-en-us-article-i3evlab-8b7ac5249e
source_url: https://help.webex.com/en-us/article/i3evlab
retrieved_at: 2026-11-02T13:13:54.247155+00:00
---

ThousandEyes Agent integration for phones supports the following models:

Supported features

On ThousandEyes portal, you can view the following information related to phones:

- Scheduled tests

- Dynamic tests for meetings on Webex, Microsoft Teams,  and Zoom via Office 365 calendar

- Dynamic tests for SIP calls

- Local networks

The Webex, Microsoft Teams, or Zoom meetings that you join through the phone are using Session Initiation Protocol (SIP). When setting up tests for your phones on the ThousandEyes application, make sure that you use the Webex template, instead of other meeting app templates.

Limitations

- Phone Wi-Fi statistics aren't available on the ThousandEyes portal.

- The Run Once option for instant tests isn't supported in PhoneOS.

- Real user tests are not supported for phones.

Before you begin

Get ThousandEyes Endpoint Agent licenses (either
            essential or advantage). You need one endpoint license per device.

Get the connection string from the ThousandEyes application.

Install the device package for your Unified Communications Manager version to make the ThousandEyes related parameters available. Download the device package at the CallManager Support page .

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To enable ThousandEyes Agent for all deployed phones, go to System > Enterprise Phone Configuration .

- To enable ThousandEyes Agent for phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To enable ThousandEyes Agent for an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

Set ThousandEyes Enable to True .

Copy the connection string from the ThousandEyes application and paste it into the Connection String field.

Select Save .

Select Apply Config .

| Phone model | Firmware version |
|---|---|
| Cisco Video Phone 8875 | 5.0.1 and later |
| Cisco Desk Phone 9861 | 3.2.1 and later |
| Cisco Desk Phone 9871 | 3.2.1 and later |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To enable ThousandEyes Agent for all deployed phones, go to System > Enterprise Phone Configuration . To enable ThousandEyes Agent for phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To enable ThousandEyes Agent for an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. |
| 3 | Set ThousandEyes Enable to True . |
| 4 | Copy the connection string from the ThousandEyes application and paste it into the Connection String field. |
| 5 | Select Save . |
| 6 | Select Apply Config . |