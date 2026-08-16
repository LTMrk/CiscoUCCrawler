---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-all-models-xsi-9-1-1-cuip-bk-p82b3b16-00-phones-services-application--92e78d7a32
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes_chapter_01.html
retrieved_at: 2026-08-16T18:01:29.309494+00:00
---

Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

# Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

Updated: August 6, 2026

Chapter: Custom Client Services Overview

## Chapter: Custom Client Services Overview

# Custom Client Services Overview

## Services and Directories

You can use Cisco Unified IP Phones to deploy customized client services that users can interact with using the phone keypad
                              and display. Services deploy using HTTP from standard web servers.

Users access client services using the menu options (availability varies by phone model). When a user opens the Services menu
                              item, a menu of configured services displays. The user then chooses a service from the list, and the phone displays the service.

The following list gives typical services that might be supplied to a phone:

Weather

Stock information

Contact information

Company news

To-do lists

Daily schedule

The following figures shows a sample icon menu and a Directory list.

Phone users can navigate a text menu using the Navigation button followed by the Select softkey, or by using the numeric keypad
                              to enter a selection directly.

When a menu selection is made, the Cisco IP Phone acts on it by using the HTTP client to load a specific URL. The return type
                              from this URL can be plain text or one of the CiscoIPPhone XML objects. The object loads and the user interacts with the object.

Cisco Unified Communications Manager limits Cisco IP Phone service activity to a specific Services pane in the Cisco Unified
                              IP Phone display. A service cannot modify the top line of the phone display, which contains the time, date, and primary extension.
                              A service cannot overwrite the bottom line of the display, which contains softkey definitions.

HTML Disclaimer : Phone service developers must take into consideration that the phone is not a web browser and cannot parse HTML. Although
                                          content is delivered to the phone through HTTP messages using a web server, keep in mind that the content is not HTML. All
                                          content comes to the phone either as plain text or packaged in proprietary XML wrappers.

## Restrictions and Limitations

### Custom Application Delays

When users interact with custom phone applications, they may experience unusually long phone response delays  under the following
                                 conditions:

Heavy data usage when there are concurrent phone calls or other HTTP services (for example, Extension Mobility or Extension
                                       Mobility Cross Cluster).

Repeated pushing of large files to the phones (for example, pushing large image files every second).

The response time also varies between different phone models due to internal processing limitations.

Administrators should configure the external services for the best application performance. For more information, see IP Phone Service Administration and Subscription .

### Wireless Phone Application Differences

If you created applications for the Cisco Unified Wireless IP Phone 792x Series, you may want to use them on the Cisco Wireless
                                 IP Phone 882x Series. However, the applications for the older wireless phones are not completely compatible with the newer
                                 phones.

Object

Cisco Unified Wireless IP Phone 792x Series

Cisco Wireless IP Phone 882x Series

SoftkeyItem

Supported <SoftKeyItems> and </SoftKeyItems> tags to group SoftKeyItem definitions.

SoftKeyItems is not supported. Remove these tags from the application.

WindowMode

Does not support WindowMode.

### Cisco IP DECT 6800 Series Doesn't Support XSI

The Cisco IP DECT 6800 Series doesn't support Cisco Unified IP Phone Services Applications.

| Note | HTML Disclaimer : Phone service developers must take into consideration that the phone is not a web browser and cannot parse HTML. Although
                                          content is delivered to the phone through HTTP messages using a web server, keep in mind that the content is not HTML. All
                                          content comes to the phone either as plain text or packaged in proprietary XML wrappers. |
|---|---|

| Note | The response time also varies between different phone models due to internal processing limitations. |
|---|---|

| Object | Cisco Unified Wireless IP Phone 792x Series | Cisco Wireless IP Phone 882x Series |
|---|---|---|
| SoftkeyItem | Supported <SoftKeyItems> and </SoftKeyItems> tags to group SoftKeyItem definitions. | SoftKeyItems is not supported. Remove these tags from the application. |
| WindowMode |  | Does not support WindowMode. |