---
doc_id: developer-cisco-com-docs-finesse-notification-popover-service-9167575cdb
source_url: https://developer.cisco.com/docs/finesse/notification-popover-service/
retrieved_at: 2026-08-25T18:47:56.257523+00:00
---

# Notification Popover Service

Class finesse.containerservices.NotificationPopoverService

The NotificationPopoverService publishes notifications on the desktop using the newly created topic finext.notification.popover . This API causes the received notifications to appear in the Notification Center.

Methods

init()

finesse.containerservices.NotificationPopoverService.init(finesse.containerservices.ContainerServices)

Initializes the NotificationPopoverService for use in gadgets. The initialization sets the logger and creates the topic for sending the notifications.

showNotification()

finesse.containerservices.NotificationPopoverService.showNotification(messageFrom,message, isDismissable, timeout, icon, type, pristine, showAlways, customLink, onClickCustomLink)

Sends the notification to the Finesse desktop with the details passed to the showNotification() method.

Example

finesse.containerservices.NotificationPopoverService.showNotification("Michael Littlefoot", "Hello, how are you doing ?", true, 500000, {'name': 'circle', size: 14, color: 'red'}, 'error' )

Name

Type

Description

Required

messageFrom

String

The name of the customer from whom the message is coming.

No

message

String

The message sent by the customer.

Yes

isDismissable

Boolean

Whether the notification message popover is dismissable or not by the agent. (Whether to show the close icon).

Default value: true

No

timeout

String

Determines the time (in milliseconds) after which the popup notification gets closed if not canceled explicitly.

Default value: 8000 milliseconds.

When the timeout for a message is set to 0, the desktop does not display the notification pop-up immediately upon its arrival. Instead, the desktop accumulates all the messages with a timeout value of 0 and displays a generic notification pop-up after the configured wait time. The notification remains visible for the pre-configured pop-up duration before it disappears.

No

icon

Object

Object containing name, color, size, and svg of the icon.

The icon has to be from the list of icons supported by Finesse.

The details of svg to be rendered include:

Content – The content type for svg is string. It contains the graphical data.

Height – This controls the height of svg.

Width – This controls the width of svg.

The default width and height of svg is 24 px.

If both name and svg parameters are provided, the name parameter takes precedence.

Yes

type

String

Type of the message. If the value of type is error, the floating message notification is always visible irrespective of whether the navbar is pinned or not.

Otherwise, floating notification is shown only when navbar is unpinned, which is the default behavior.

No

pristine

Boolean

Flag to prefix "Messages From" text in the notification title.

Default value: false. Indicates to prefix the "Message From" text in the notification title.

No

showAlways

Boolean

Determines whether the popover remains visible at all times, regardless of the navigation being pinned or unpinned.

Default value: false.

No

customLink

String

Displays a custom text link (for example, "Click to open") within the toaster notification.

No

onClickCustomLink

Function

Callback function triggered when the customLink is clicked.

No

| Name | Type | Description | Required |
|---|---|---|---|
| messageFrom | String | The name of the customer from whom the message is coming. | No |
| message | String | The message sent by the customer. | Yes |
| isDismissable | Boolean | Whether the notification message popover is dismissable or not by the agent. (Whether to show the close icon). Default value: true | No |
| timeout | String | Determines the time (in milliseconds) after which the popup notification gets closed if not canceled explicitly. Default value: 8000 milliseconds. Note When the timeout for a message is set to 0, the desktop does not display the notification pop-up immediately upon its arrival. Instead, the desktop accumulates all the messages with a timeout value of 0 and displays a generic notification pop-up after the configured wait time. The notification remains visible for the pre-configured pop-up duration before it disappears. | Note | When the timeout for a message is set to 0, the desktop does not display the notification pop-up immediately upon its arrival. Instead, the desktop accumulates all the messages with a timeout value of 0 and displays a generic notification pop-up after the configured wait time. The notification remains visible for the pre-configured pop-up duration before it disappears. | No |
| Note | When the timeout for a message is set to 0, the desktop does not display the notification pop-up immediately upon its arrival. Instead, the desktop accumulates all the messages with a timeout value of 0 and displays a generic notification pop-up after the configured wait time. The notification remains visible for the pre-configured pop-up duration before it disappears. |
| icon | Object | Object containing name, color, size, and svg of the icon. The icon has to be from the list of icons supported by Finesse. The details of svg to be rendered include: Content – The content type for svg is string. It contains the graphical data. Height – This controls the height of svg. Width – This controls the width of svg. The default width and height of svg is 24 px. If both name and svg parameters are provided, the name parameter takes precedence. | Yes |
| type | String | Type of the message. If the value of type is error, the floating message notification is always visible irrespective of whether the navbar is pinned or not. Otherwise, floating notification is shown only when navbar is unpinned, which is the default behavior. | No |
| pristine | Boolean | Flag to prefix "Messages From" text in the notification title. Default value: false. Indicates to prefix the "Message From" text in the notification title. | No |
| showAlways | Boolean | Determines whether the popover remains visible at all times, regardless of the navigation being pinned or unpinned. Default value: false. | No |
| customLink | String | Displays a custom text link (for example, "Click to open") within the toaster notification. | No |
| onClickCustomLink | Function | Callback function triggered when the customLink is clicked. | No |

| Note | When the timeout for a message is set to 0, the desktop does not display the notification pop-up immediately upon its arrival. Instead, the desktop accumulates all the messages with a timeout value of 0 and displays a generic notification pop-up after the configured wait time. The notification remains visible for the pre-configured pop-up duration before it disappears. |
|---|---|