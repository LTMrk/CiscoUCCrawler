[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/compliance/docs/compliance)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/compliance/docs/compliance)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/compliance/docs/compliance)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Compliance
Webex Compliance
  * [Compliance](https://developer.webex.com/compliance/docs/compliance)


## Webex Compliance
### Compliance
Webex is an end-to-end encrypted cloud collaboration platform. Organizations have exclusive control over the management of their encryption keys as well as the confidentiality of their data.
####  anchorOverview
anchor
Because we recognize that some data in Webex may involve access to sensitive information about users and accounts, Webex Control Hub supports multiple types of administrator roles with access to different subsets of information. Webex Control Hub provides a full-service management experience supporting trials, purchasing, account and user configuration, adoption reports, and customer support. For more information about Webex Control Hub, please see [this data sheet](https://www.cisco.com/c/dam/en/us/solutions/collaboration/spark-control-hub.pdf).
Within Webex Control Hub, you can associate administrative users with a specific role to ensure that the data within Webex remains in compliance with the legal standards in effect for an organization. This role is known as the Compliance Officer. Compliance officers can use the Webex REST API to access information within Webex to aid in compliance activities for their organization.
Additionally, the Webex REST API includes an Events API endpoint, which authorized third-party software can use to access, monitor, and archive the data created and shared by Webex users within an organization.
This guide will provide more detail about the Compliance Officer role, the Events API endpoint, and the types of permissions that can be used for data monitoring and management within Webex. It will also describe the monitoring controls that can be put into place to ensure that all activities within Webex are in full compliance with accepted business practices and internal standards.
####  anchorWebex Data
anchor
###### Permissions & Ownership
Data created within Webex belongs to the [organization](https://developer.webex.com/docs/api/v1/organizations) that owns the room (space). The owner of a group room is generally the organization for the person who created the room. For 1:1 rooms between users in different organizations, the organization that each person belongs to owns their participant’s content. Rooms created by bots are owned by the organization of the first non-bot participant.
Data access permissions within Webex vary depending on a few factors: the room creator, room membership, and organization membership. When a room is created, the organization associated with the creator is considered the **owning organization** for the room. If users from other organizations are added to the room, those organizations are **participating organizations** in the room. 
In general, the following types of users will be viewing, creating, and managing data within Webex:
  * Room participants—can send and view messages within the room.
  * Room moderator—users can be assigned as a moderator by a room owner and have exclusive control of the room including the room’s title and participant list.
  * Compliance officers for the owning organization—can monitor and manage all data within group rooms created by a member of the organization; can manage all content in 1:1 rooms, including those with external participants.
  * Compliance officers for the participating organization-can monitor and manage data created by their users in rooms owned by another organization; can manage all content in 1:1 rooms with external participants.


In a 1:1 room between users of different organizations, either organization’s compliance officers can monitor and manage data created by _both_ participants.
###### Security & Privacy
A key management server (KMS) is responsible for the creation and security of the encryption keys the Webex clients use to encrypt and decrypt data and communications. It is architecturally and operationally separated from the rest of the Webex Cloud and its data is not accessible by any other components. Whether the KMS is managed by Cisco or installed and managed on-premise, data within the Webex Cloud is encrypted from end-to-end and is not decrypted until it reaches the API endpoint.
For more information about data security and privacy in Webex, please see the [Webex Security White Paper](https://www.cisco.com/c/dam/en/us/solutions/collateral/collaboration/cloud-collaboration/cisco-spark-security-white-paper.pdf).
####  anchorCompliance
anchor
###### Compliance Officer
The role of a compliance officer is to ensure that a company is conducting its business in full compliance with all laws and regulations that pertain to its particular industry, as well as professional standards, accepted business practices, and internal standards.
The Webex REST API has compliance authorization scopes that support the compliance officer’s role. Using these `spark-compliance` scopes, compliance officers will have access to, and the ability to manage, all data created by their organization such as messages or content attachments. Compliance officers can monitor data and take action to mitigate compliance issues that could arise.
###### Authorization Scopes
The `spark-compliance` scopes and their descriptions are listed below:
Scope
Usage
`spark-compliance:events_read`
Access to read events in your user's organization
`spark-compliance:messages_write`
Delete messages in all spaces in your user's organization
`spark-compliance:messages_read`
Access to read messages in your user's organization
`spark-compliance:recordings_write`
Access to update/delete converged recording resources in your user’s organization
`spark-compliance:recordings_read`
Access to read converged recording resources in your user’s organization.
`spark-compliance:memberships_write`
Access to create/update/delete memberships in your user's organization
`spark-compliance:memberships_read`
Access to read memberships in your user's organization
`spark-compliance:rooms_write`
Access to modify rooms in your user's organization
`spark-compliance:rooms_read`
Access to read rooms in your user's organization
`spark-compliance:teams_read`
Access to read teams in your user's organization
`spark-compliance:team_memberships_write`
Access to update team memberships in your user's organization
`spark-compliance:team_memberships_read`
Access to read team memberships in your user's organization
For instructions on how to add these scopes to your app and for a full list of all available authorization scopes see the [Integrations/OAuth Guide](https://developer.webex.com/docs/integrations).
###### Using the Compliance Scopes
Normally, Webex REST API users only have access to information related to their account, such as messages in rooms where they are members. The `spark-compliance` scopes provide access to information across the organization. For instance, if granted the `spark-compliance:messages_read` scope, messages will be available for all rooms within the organization, not just those that the authenticated compliance officer is a member of.
Several scopes provide access to write data or take action within an organization. If an action should be taken against certain data within Webex for compliance reasons, the Webex REST API can be used with an authentication token authorized with one of the above scopes to carry out the action. For example, if a message needs to be deleted, the `spark-compliance:messages_write` scope will be required. To delete the message, use the [DELETE /messages endpoint](https://developer.webex.com/docs/api/v1/messages/delete-a-message). Similarly, if a member of a room, either a person or a bot, needs to be added or removed, the `spark-compliance:memberships_write` scope will be required and the membership can be deleted with the [DELETE /memberships endpoint](https://developer.webex.com/docs/api/v1/memberships/delete-a-membership).
When using the appropriate `spark-compliance:` scopes and API endpoints, the authenticated user _does not_ need to be a member of the room to take action. For example, a compliance officer who is not a member of a particular room can create, update, or delete the room's [memberships](https://developer.webex.com/docs/api/v1/memberships) with the `spark-compliance:memberships_write` scope.
####  anchorMeetings
anchor
Please refer to the [Meetings](https://developer.webex.com/docs/meetings) documentation for details.
###### Meeting Recordings
Compliance officers are able to retrieve user recordings for analysis and compliance. There is a separate API endpoint for admins and compliance officers [/admin/recordings](https://developer.webex.com/docs/api/v1/recordings/list-recordings-for-an-admin-or-compliance-officer), while regular users use [/recordings](https://developer.webex.com/docs/api/v1/recordings/list-recordings). As it relates to recording deletion, a recycle bin and associated recording `status` is available. A user typically moves a recording to the recycle bin via the GUI and then either restores the recording or purges the recording from the recycle bin. Once purged, the recording isn't accessible to regular users any longer, but it is still accessible to the Compliance Officer until it is removed through the retention process. Compliance officers who want to retrieve user-deleted recordings must query the [/events API](https://developer.webex.com/docs/api/v1/events) for deleted recording events, and use the returned recording ID to retrieve the recording from [/recordings/{id}](https://developer.webex.com/docs/api/v1/recordings/get-recording-details). Regular users will see a 404 error. 
####  anchorEvents
anchor
###### Introduction
The [Events API](https://developer.webex.com/docs/api/v1/events) endpoint gives developers access to events happening within their Webex organization. Events can be integrated with Data Loss Prevention (DLP) and CASB software to check for policy violations and to take action to resolve any issues. The events available for monitoring include activities such as posting messages, sending content such as files, and group space membership changes. The Events API endpoint can be integrated with your existing archiving software to archive an unlimited amount of Webex data. For access to events older than 90 days, the organization will need the [Pro Pack](https://www.cisco.com/go/pro-pack) for Webex Control Hub.
Use the Events API endpoint to access activities after they have occurred. Perhaps you need to replay every message sent to a room to comply with a legal audit process, or you need to know which rooms someone joined and left. The Events API endpoint will give you access to this information quickly and securely. In addition Webex provides a tool to uncover actions of a specific user in form of the eDiscovery report, available through the Webex Control Hub.
Known Limitations: Membership events generated as a result of a POST to [/team/memberships](https://developer.webex.com/docs/api/v1/team-memberships/create-a-team-membership) do not currently contain a "roomType" or "isHidden" parameter.
Most events apply to an API resource of the same name. For example when a user creates a message a message creation event will be available. Some events though are not quite as straightforward to correlate. These include
  * `Attachment Actions` events, which are part of Buttons&Cards and corresponding message creations.
  * `Space Classifications`, which are Room Classifications (the `rooms` resource). The only supported event is `updated`.
  * `File Downloads`, that get triggered whenever a user downloads a file.
  * `File Transcodings` events, which are created when a user sees a preview of a file in their Webex client (title page).
  * `Call Records(CDR)` events, which are created when a Webex Calling user makes or receives calls.
  * `Business Texts(SMS)` events, which are created when a Webex Calling users sends or receives SMS messages.

  
| Resource  | created  | updated  | deleted  | ended  | read  |  
| --- | --- | --- | --- | --- | --- |  
| [Attachment Actions](https://developer.webex.com/docs/api/v1/attachment-actions)  | X  |   |   |   |   |  
| [Messages](https://developer.webex.com/docs/api/v1/messages)  | X  | X  | X  |   |   |  
| [Memberships](https://developer.webex.com/docs/api/v1/memberships)  | X  | X  | X  |   |   |  
| [Space Classifications (rooms)](https://developer.webex.com/admin/docs/api/v1/classifications)  |   | X  |   |   |   |  
| [File Downloads](https://developer.webex.com/docs/api/v1/messages)  |   |   |   |   | X  |  
| [File Previews a.k.a. File Transcodings](https://developer.webex.com/docs/api/v1/messages)  |   |   |   |   | X  |  
| [Room Tabs](https://developer.webex.com/docs/api/v1/room-tabs)  | X  | X  | X  |   |   |  
| [Meetings](https://developer.webex.com/docs/api/v1/meetings)  |   |   |   | X  |   |  
| [Meeting transcripts](https://developer.webex.com/docs/api/v1/meeting-transcripts)  | X  |   |   |   |   |  
| [Meeting messages](https://developer.webex.com/docs/api/v1/meeting-messages)  | X  | X  | X  |   |   |  
| Call Records(CDR)  | X  |   |   |   |   |  
| Business Texts(SMS)  | X  |   |   |   |   |  
###### Authorization Scopes
One scope for Events is available. Note that in order to use a `spark-compliance` scope you will need to be a designated compliance officer for your organization in Webex Control Hub. For instructions on how to add these scopes to your app and for a full list of all available authorization scopes see the [Integrations/OAuth Guide](https://developer.webex.com/docs/integrations).
Scope
Usage
`spark-compliance:events_read`
Access to read events in your user's organization
###### Using Events
With the [Events API](https://developer.webex.com/docs/api/v1/events) endpoint you can retrieve information about user activities in Webex such as message activity in spaces, content or files shared, or user membership changes in spaces.
The `spark-compliance:events_read` scope can be used by compliance officers to retrieve events for the entire organization.
Each event contains a `data` object which mimics the Webex REST API resource (such as a message or membership) at the time the event took place. If properties are added to existing API resources, new events will include them; past events will not be updated to include the new properties.
When requesting a list of events from the API, the result may be split into pages. See the [Pagination](https://developer.webex.com/docs/api/basics#pagination) guide to learn how to navigate through paged API responses.
###### Example: Retrieve Created Messages
To retrieve all messages that have been created, use the [List Events](https://developer.webex.com/docs/api/v1/events/list-events) endpoint. Use URL query parameters to limit the response to include only events related to the _messages_ resource and only _created_ items by using: `resource=messages&type=created`.
GET `https://webexapis.com/v1/events?resource=messages&type=created`

```
{
  "items": [ {
    "id": "Y2lzY29zcGFyazovL3VzL0VWRU5UL2JiY2ViMWFkLTQzZjEtM2I1OC05MTQ3LWYxNGJiMGM0ZDE1NAo",
    "resource": "messages",
    "type": "created",
    "actorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
    "orgId": "OTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
    "appId": "null",
    "created": "2015-10-18T14:26:16+00:00",
    "data": {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "roomType": "group",
      "text": "PROJECT UPDATE - A new project plan has been published on Box: http://box.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "personEmail": "matt@example.com",
      "attachments": [
        {
          "contentType": "application/vnd.microsoft.card.adaptive",
          "content": {
            ... omitted ...
          }
        }
      ],
      "created": "2015-10-18T14:26:16+00:00"
    }
  } ]
}

```

In this example response, only one record is returned, but let’s take a look at it in detail.

```
{
  "items": [ {
    "id": "Y2lzY29zcGFyazovL3VzL0VWRU5UL2JiY2ViMWFkLTQzZjEtM2I1OC05MTQ3LWYxNGJiMGM0ZDE1NAo",
    "resource": "messages",
    "type": "created",
    "actorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
    "orgId": "OTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
    "appId": "null",
    "created": "2015-10-18T14:26:16+00:00",
    "data": {
      ... omitted ...
    }
  } ]
}

```

The event object returned contains several fields which describe the event. This includes:
  * `id`—a unique ID for the event
  * `resource`—which resource the event includes
  * `type`—the type of action which took place, such as created or deleted
  * `actorId`—the ID of the person which committed the activity for this event
  * `orgId`—the ID of the organization for the actor
  * `appId`—the ID of the integration or bot which committed the activity for this event
  * `created`—when the event took place
  * `data`—the data for the event


```
{
  "items": [ {
    ... omitted ...
    "data": {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "roomType": "group",
      "text": "PROJECT UPDATE - A new project plan has been published on Box: http://box.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "personEmail": "matt@example.com",
      "attachments": [
        {
          "contentType": "application/vnd.microsoft.card.adaptive",
          "content": {
            ... omitted ...
          }
        }
      ],
      "created": "2015-10-18T14:26:16+00:00"
    }
  } ]
}

```

Inside of the event object, the `data` object contains an object which represents the Webex REST API resource at the time the event took place. For instance, in this event, a message object represents a message at the time of its creation.
###### Example: Retrieve Deleted Messages and Files
To retrieve all messages that have been deleted, use the List Events endpoint. Use URL query parameters to limit the response to include only events related to the messages resource and only deleted items by using: resource=messages&type=deleted.
Deleted messages have a reference back to the original message. Here is an example response for a single message that was deleted.

```
 {
      "id": "Y2lzY29zcGFyazovL3VzL0VWRU5UL2MyZjhlMjYwLTgyYmUtMTFlYi1iYzdhLWNmZmIwNDA0Y2Y1YQ",
      "resource": "messages",
      "type": "deleted",
      "actorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82ZDg4MDc3MS05MTA4LTRiMzktYmJlOS02OWJiNjA2ODBmZTG”,
      "created": "2021-03-11T23:08:59.142Z",
      "data": {
        "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNDYyMDQ4NTAtODJiZS0xMWViLWJkYmUtM2IyYWMxNWZlNjg5",
        "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMGQ5MTg1ZDAtODJiZS0xMWViLWEyNGYtZDMxMWQ2NmMwNjBj",
        "roomType": "group",
        "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82ZDg4MDc3MS05MTA4LTRiMzktYmJlOS02OWJiNjA2ODBmZTG”,
        "personEmail": “example@gmail.com"
      }
 }

```

For a Compliance Officer, it is important to understand what has been deleted. The way to go about it, is to use the message ID and query the /messages resource with it. Both the text and in this case file attachment are returned.
GET `https://webexapis.com/v1/messages/Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNDYyMDQ4NTAtODJiZS0xMWViLWJkYmUtM2IyYWMxNWZlNjg5 `
The sample response looks like this

```
{
  "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNDYyMDQ4NTAtODJiZS0xMWViLWJkYmUtM2IyYWMxNWZlNjg5",
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMGQ5MTg1ZDAtODJiZS0xMWViLWEyNGYtZDMxMWQ2NmMwNjBj",
  "roomType": "group",
  "text": "check this",
  "files": [
    "https://integration.webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvNDYyMDQ4NTAtODJiZS0xMWViLWJkYmUtM2IyYWMxNWZlNjg5LzA"
  ],
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82ZDg4MDc3MS05MTA4LTRiMzktYmJlOS02OWJiNjA2ODBmZTG”,
  "personEmail": “example@gmail.com",
  "html": "<p>check this</p>",
  "created": "2021-03-11T23:05:29.685Z"
}

```

The deleted message had a file attachment. Any file attachment is always encapsulated into a message, even if the user did not supply any text. For the Compliance Officer to check the file that was deleted, they have to query the /contents URL. Only the Compliance Officer will have access to the file and only for the duration of the default retention period. Regular users and after the retention period the query will return a http `404`. If the Compliance Officer tries to delete the message again they will receive a `410` error status, which should be avoided.
For more information about how to use the Events API endpoint, please see the [Events API Reference](https://developer.webex.com/docs/api/v1/events).
##### In This Article
  * [Overview](https://developer.webex.com/compliance/docs/compliance#overview)
  * [Webex Data](https://developer.webex.com/compliance/docs/compliance#webex-data)
  * [Compliance](https://developer.webex.com/compliance/docs/compliance#compliance)
  * [Meetings](https://developer.webex.com/compliance/docs/compliance#meetings)
  * [Events](https://developer.webex.com/compliance/docs/compliance#events)


## Connect
[Support](https://developer.webex.com/support)
[Developer Community](https://community.cisco.com/t5/webex-for-developers/bd-p/disc-webex-developers)
[Developer Events](https://developer.webex.com/blog/categories/events)
[Contact Sales](https://www.webex.com/contact-sales.html?TrackID=1017639&hbxref=&goid=us_contact_sales)
## Handy Links
[Webex Ambassadors](https://www.essentials.webex.com/programs/ambassadors)
[Webex App Hub](https://www.essentials.webex.com/programs/ambassadors)
## Resources
[Open Source Bot Starter Kits](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[Download Webex](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[DevNet Learning Labs](https://www.webex.com)
[Terms of Service](https://developer.webex.com/terms-of-service)
[Privacy Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html)
[Cookie Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html#cookies)
[Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
© 2026 Cisco and/or its affiliates. All rights reserved.
[](https://github.com/webex)[](https://www.facebook.com/CiscoCollab/)[](https://twitter.com/webexdevs)[](https://www.youtube.com/playlist?list=PL2k86RlAekM_bIUrvVw4Haq_0xxTez9zU)[](https://www.linkedin.com/company/webex/)
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
