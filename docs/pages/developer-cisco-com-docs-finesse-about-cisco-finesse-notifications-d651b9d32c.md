---
doc_id: developer-cisco-com-docs-finesse-about-cisco-finesse-notifications-d651b9d32c
source_url: https://developer.cisco.com/docs/finesse/about-cisco-finesse-notifications/
retrieved_at: 2026-09-07T14:07:32.567043+00:00
---

# About Cisco
	 Finesse Notifications

The Cisco Finesse Web Service sends notifications to clients that
		  subscribe to that class of resource.

For example, a client that is subscribed to User notifications receives a notification when an agent signs
		  in or out of the Finesse desktop, information about an agent changes, or an
		  agent's state changes.

The preceding example illustrates some cases where notifications are
			 sent. It is not intended to be an exhaustive list.

Notification payloads are XML-encoded. If these payloads contain any
			 special XML characters, you must ensure that the client decodes this
			 information correctly before processing it further.

| Note | The preceding example illustrates some cases where notifications are
			 sent. It is not intended to be an exhaustive list. |
|---|---|

| Note | Notification payloads are XML-encoded. If these payloads contain any
			 special XML characters, you must ensure that the client decodes this
			 information correctly before processing it further. |
|---|---|