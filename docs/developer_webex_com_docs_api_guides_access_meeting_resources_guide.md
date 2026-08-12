[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/meeting/docs/api/guides/access-meeting-resources-guide)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/meeting/docs/api/guides/access-meeting-resources-guide)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/meeting/docs/api/guides/access-meeting-resources-guide)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Meeting Resource Guide
Webex Meetings
  * [Overview](https://developer.webex.com/meeting/docs/meetings)
  * Guides
    * [Access the API](https://developer.webex.com/meeting/docs/getting-started)
    * [Meeting Resource Guide](https://developer.webex.com/meeting/docs/api/guides/access-meeting-resources-guide)
    * [Integrations & Authorization](https://developer.webex.com/meeting/docs/integrations)
    * [Using Webex Service Apps](https://developer.webex.com/meeting/docs/service-apps)
    * [Webinar Guide](https://developer.webex.com/meeting/docs/api/guides/webinar-guide)
    * [Webhooks](https://developer.webex.com/meeting/docs/api/guides/webhooks)
    * [Meetings MCP Server](https://developer.webex.com/meeting/docs/meetings-mcp-server)
  * [Guest to Guest Meetings](https://developer.webex.com/meeting/docs/guest-to-guest-meetings)
  * [API Behavior Changes](https://developer.webex.com/meeting/docs/app-programming-interface-behavior-changes)
  * [REST API Basics](https://developer.webex.com/meeting/docs/basics)
  * API REFERENCE
  * All APIs
  * [Changelog](https://developer.webex.com/meeting/docs/api/changelog/webex-meetings)
  * SDK
  * [AI Assistant for Developers](https://developer.webex.com/meeting/docs/webex-aI-assistant-for-developers)
  * [Troubleshoot the API](https://developer.webex.com/meeting/docs/api/guides/troubleshooting)
  * [Widgets](https://developer.webex.com/meeting/docs/widgets)
  * [Tutorials](https://developer.webex.com/meeting/docs/tutorials)
  * [Suite Sandbox](https://developer.webex.com/meeting/docs/developer-sandbox-guide)
  * [Beta Program Overview](https://developer.webex.com/meeting/docs/webex-developer-beta-program)
  * [Webex Status API](https://developer.webex.com/meeting/docs/webex-status-api)
  * [XML API Deprecation](https://developer.webex.com/meeting/docs/webex-xml-api-deprecation-announcement)


## Webex Meetings
### Meeting Resource Guide
Use this guide to learn how to code to access the meeting resources from Webex.
####  anchorAccess Meeting Resources Guide
anchor
Sales enablement needs to know what meetings are occurring, who the participants in each individual meeting, when these meetings start and end and how to access the content from these meetings. Web developers have asked for improved availability of connecting to the resources that allow applications to be meeting aware and get access to post meeting resources.
###### Getting Started
To leverage assets from a meeting, you must first ensure the following settings are enabled in Webex when the meeting starts:
  * Recording: To record the meeting, you must enable the recordings option. This can be done by the users during a meeting or programmatically via API for a scheduled meeting.
  * Transcripts: To create a transcript, you must turn on Webex Assistant. This cannot be done programmatically and must be turned on by the meeting host/participant or set as default behavior in the control hub. NOTE: Webex Assistant requires a license.


###### Accessing Meeting Resources
When a meeting ends, Webex triggers a notice that unlock any meeting assets and you may retrieve them.
To achieve this via APIs, you must create a webhook for the meeting termination. 
The documentation for the Webhook APIs can be found at <https://developer.webex.com/docs/api/v1/webhooks/create-a-webhook>
Creation is a post request to /v1/webhooks event = ended and resource = meetings
The post might look like below:

```
{
  "name": "Meeting Ended Webhook",
  "targetUrl": "https://example.com/mywebhook",
  "resource": "meetings",
  "event": "ended",
}

```

Then the response might be something like:

```
{
    "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1dFQkhPT0svNDk5ZjkxZjItY2QxMi00NTk2LWEzYjctNDY4NTA1OGQ2NTlm",
    "name": "Meeting Ended Webhook",
    "targetUrl": "https://webhook.site/c231a24c-8a04-42b6-a7ed-85ff1a51b60b",
    "resource": "meetings",
    "event": "ended",
    "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi81NWM1YWUzZi04ZDdmLTQyN2ItYTRmOS01ZTNjYjNkZGRmN2I",
    "createdBy": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYzAxZjUzMi1kMDIyLTRmOGUtYTQ5NC1mMGE0ZDc5ZTUyMjc",
    "appId": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0NmMzkyNWU5NDFmMzhhYTc0M2Y0MmFiNzcwZmZhZjFhNTIyMjcxZDI5OTQ4NDhjNjk2YWMwYTEwN2Q2YTg5MjI3",
    "ownedBy": "creator",
    "status": "active",
    "created": "2021-05-14T20:20:01.024Z"
}

```

If you want to synchronize your app with all meetings, there are webhooks for the following categories: created, updated, and deleted. 
The webhook you receive for a meeting end might look something like:

```
{
  "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1dFQkhPT0svNDk5ZjkxZjItY2QxMi00NTk2LWEzYjctNDY4NTA1OGQ2NTlm",
  "name": "Meeting Ended Webhook",
  "targetUrl": "https://webhook.site/c231a24c-8a04-42b6-a7ed-85ff1a51b60b",
  "resource": "meetings",
  "event": "ended",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi81NWM1YWUzZi04ZDdmLTQyN2ItYTRmOS01ZTNjYjNkZGRmN2I",
  "createdBy": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYzAxZjUzMi1kMDIyLTRmOGUtYTQ5NC1mMGE0ZDc5ZTUyMjc",
  "appId": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0NmMzkyNWU5NDFmMzhhYTc0M2Y0MmFiNzcwZmZhZjFhNTIyMjcxZDI5OTQ4NDhjNjk2YWMwYTEwN2Q2YTg5MjI3",
  "ownedBy": "creator",
  "status": "active",
  "created": "2021-05-14T20:20:01.024Z",
  "data": {
    "id": "501e995485e2460bb129410116757b13_I_194316955237236650",
    "meetingType": "meeting",
    "timezone": "UTC",
    "start": "2021-05-14T20:25:19Z",
    "end": "2021-05-14T20:26:54Z",
    "hostUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYzAxZjUzMi1kMDIyLTRmOGUtYTQ5NC1mMGE0ZDc5ZTUyMjc",
    "state": "ended",
    "hostEmail": "spouliottes@gmail.com",
    "siteUrl": "spouliottes-test.webex.com",
    "orgId": "55c5ae3f-8d7f-427b-a4f9-5e3cb3dddf7b"
  }
}

```

It is important to remember that you need to store the ID in the data. Webex supports listing meetings but they only return future and in progress meetings. You cannot recover this IS historically and need to store in your app. 
Developer Note: When a meeting is created, the ID will look different than post meeting ID in webhook. Webex appends an additional ID that is demarcated with “ _I_ ”. For example, in the above case the ID on end event was: '501e995485e2460bb129410116757b13_I_194316955237236650'
In the pre-meeting creation, the ID for the event would have been: '501e995485e2460bb129410116757b13'
###### Find Recording Assets
After a meeting has finished, Webex will process and store post meeting assets and make them available through the endpoint: - /v1/recordings
You can query for all available recordings by leaving the query parameters blank or you can set specific data such as meetingId as in the example below: <https://webexapis.com/v1/recordings?meetingId=501e995485e2460bb129410116757b13_I_194316955237236650>
The response will look something like this:

```
{
  "items": [
    {
      "id": "724a81a697201039a976005056819cde",
      "meetingId": "501e995485e2460bb129410116757b13_I_194316955237236650",
      "scheduledMeetingId": "501e995485e2460bb129410116757b13_20210514T203000Z",
      "meetingSeriesId": "501e995485e2460bb129410116757b13",
      "topic": "Test meeting-20210514 2025-1",
      "createTime": "2021-05-14T20:28:53Z",
      "siteUrl": "spouliottes-test.webex.com",
      "downloadUrl": "https://spouliottes-test.webex.com/spouliottes-test/lsr.php?RCID=77ab059a6b6512550d6a3ddafeea57aa",
      "playbackUrl": "https://spouliottes-test.webex.com/spouliottes-test/ldr.php?RCID=6197666928e747419d239f3cfdee3e49",
      "password": "tA3hwXUm",
      "format": "MP4",
      "durationSeconds": 85,
      "sizeBytes": 4982263,
      "shareToMe": false
    }
  ]
}

```

The download and playback URLs are accessible via browser and require the password associated in the response. 
If you want a direct download link, you can retrieve that from - /v1/getRecordings/
As found in the above example with id": "724a81a697201039a976005056819cde 
This will return a response like the following:

```
{
  "id": "724a81a697201039a976005056819cde",
  "meetingId": "501e995485e2460bb129410116757b13_I_194316955237236650",
  "scheduledMeetingId": "501e995485e2460bb129410116757b13_20210514T203000Z",
  "meetingSeriesId": "501e995485e2460bb129410116757b13",
  "topic": "Test meeting-20210514 2025-1",
  "createTime": "2021-05-14T20:28:53Z",
  "siteUrl": "spouliottes-test.webex.com",
  "downloadUrl": "https://spouliottes-test.webex.com/spouliottes-test/lsr.php?RCID=77ab059a6b6512550d6a3ddafeea57aa",
  "playbackUrl": "https://spouliottes-test.webex.com/spouliottes-test/ldr.php?RCID=6197666928e747419d239f3cfdee3e49",
  "password": "tA3hwXUm",
  "temporaryDirectDownloadLinks": {
    "recordingDownloadLink": "https://nsj1wss.webex.com/nbr/MultiThreadDownloadServlet?siteid=13867087&recordid=220437037&confid=194316955237236650&from=MBS&trackingID=WEBEX-DEV-PORTAL_3bdadf4c-40a7-4ab5-967c-957c77a12a10_50&language=en_US&userid=600686172&serviceRecordID=220441022&ticket=SDJTSwAAAARjJiLHI3wKUisba87xO+urLcu84afdWTP4vg3ucK5ZhA==&timestamp=1621283371277&islogin=yes&isprevent=no&ispwd=yes",
    "audioDownloadLink": "https://nsj1wss.webex.com/nbr/MultiThreadDownloadServlet/audio.mp3?siteid=13867087&recordid=220437037&confid=194316955237236650&from=MBS&trackingID=WEBEX-DEV-PORTAL_3bdadf4c-40a7-4ab5-967c-957c77a12a10_50&language=en_US&userid=600686172&serviceRecordID=220441022&ticket=SDJTSwAAAAS/F5Mw2d32msyLuoeJKubqgkKvTlrlXdzjrQdvVmQQ0Q==&timestamp=1621283371276&islogin=yes&isprevent=no&ispwd=yes",
    "expiration": "2021-05-17T23:29:31Z"
  },
  "format": "MP4",
  "durationSeconds": 85,
  "sizeBytes": 4982263,
  "shareToMe": false
}

```

###### Get the Transcripts – VTT and TXT format
You can now query for the transcripts using endpoint:- /v1/meetingTranscripts/
A query might look like: <https://webexapis.com/v1/meetingTranscripts?meetingId=501e995485e2460bb129410116757b13_I_194316955237236650>
This will return to something like this:

```
{
    "items": [
        {
            "id": "a5038f0b-320a-456f-a51f-7541eeb0eae5_M_501e995485e2460bb129410116757b13",
            "meetingId": "501e995485e2460bb129410116757b13_I_194316955237236650",
            "startTime": "2021-05-14T20:25:22Z",
            "vttDownloadLink": "https://webexapis.com/v1/meetingTranscripts/a5038f0b-320a-456f-a51f-7541eeb0eae5_M_501e995485e2460bb129410116757b13/download?meetingId=501e995485e2460bb129410116757b13_I_194316955237236650&format=vtt",
            "txtDownloadLink": "https://webexapis.com/v1/meetingTranscripts/a5038f0b-320a-456f-a51f-7541eeb0eae5_M_501e995485e2460bb129410116757b13/download?meetingId=501e995485e2460bb129410116757b13_I_194316955237236650&format=txt"
        }
    ]
}

```

###### Get Assets in JSON format with speaker name
If you are designing an application that needs to programmatically use the transcript content, including speaker name in a machine readable format, you use the snippets API
  * meetingTranscripts//snippets Note: Meeting host listing/getting/updating meeting transcript snippets function is behind on a feature toggle. Only EFT user can use this function. Please contact [Webex Support Team](https://developer.webex.com/support) to turn on the toggle.


The response body might be like the following:

```
+ Response 200 (application/json;charset=UTF-8)
    + Attributes
        + items (array[SnippetObject], fixed-type) - Transcript snippet array
    + Body
            {
                "items": [
                    {
                        "id": "195d64646ad14be2924ea50f541fd91d_00001",
                        "text": "Hello everyone",
                        "personName": "John Andersen",
                        "personEmail": "john.andersen@example.com",
                        "offset": 1000,
                        "duration": 1500
                    }
                ]
            }

```

The offset field is the meeting start time in seconds. The ID field is a unique ID for the speaker slot. 
###### Set recording to on During a Meeting
The host of a meeting can toggle on recording, you can also ensure that all meetings have their recording enabled programmatically. When you receive a meeting creation notification, use the meeting ID to find the details of a meeting
The documentation for using the APIs can be found at <https://developer.webex.com/docs/api/v1/meetings/list-meetings-of-a-meeting-series>
The endpoint for meetings is: /v1/meetings
To retrieve a meetings details, perform a Get to /vi/meetings with the meeting ID set in the request URI along with any optional parameters you choose. This would look like: [https://webexapis.com/v1/meetings?meetingSeriesId=25bbf831-5be9-4c25-b4b0-9b592c8a086b&max=100&from=2019-03-18T09:30:00+08:00&to=2019-03-25T09:30:00+08:00&meetingType=[object](https://webexapis.com/v1/meetings?meetingSeriesId=25bbf831-5be9-4c25-b4b0-9b592c8a086b&max=100&from=2019-03-18T09:30:00+08:00&to=2019-03-25T09:30:00+08:00&meetingType=\[object) Object],[object Object]&state=[object Object],[object Object],[object Object],[object Object],[object Object],[object Object]&isModified=false&hostEmail=john.andersen@example.com

```
{
    "items": [
        {
            "id": "870f51ff287b41be84648412901e0402_20191101T120000Z",
            "meetingSeriesId": "870f51ff287b41be84648412901e0402",
            "meetingNumber": "123456789",
            "title": "Example Daily Meeting",
            "agenda": "Example Agenda",
            "password": "BgJep@43",
            "phoneAndVideoSystemPassword": "12345678",
            "meetingType": "scheduledMeeting",
            "state": "ready",
            "isModified": false,
            "timezone": "UTC",
            "start": "2019-11-01T12:00:00Z",
            "end": "2019-11-01T13:00:00Z",
            "hostUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jN2ZkNzNmMi05ZjFlLTQ3ZjctYWEwNS05ZWI5OGJiNjljYzY",
            "hostDisplayName": "John Andersen",
            "hostEmail": "john.andersen@example.com",
            "hostKey": "123456",
            "siteUrl": "site4-example.webex.com",
            "webLink": "https://site4-example.webex.com/site4/j.php?MTID=md41817da6a55b0925530cb88b3577b1e",
            "sipAddress": "123456789@site4-example.webex.com",
            "dialInIpAddress": "192.168.100.100",
            "enabledAutoRecordMeeting": false,
            "allowAnyUserToBeCoHost": false,
            "enabledJoinBeforeHost": false,
            "enableConnectAudioBeforeHost": false,
            "joinBeforeHostMinutes": 0,
            "allowFirstUserToBeCoHost": false,
            "allowAuthenticatedDevices": false,
            "telephony": {
                "accessCode": "1234567890",
                "callInNumbers": [
                    {
                        "label": "US Toll",
                        "callInNumber": "123456789",
                        "tollType": "toll"
                    }
                ],
                "links": [
                    {
                        "rel": "globalCallinNumbers",
                        "href": "/api/v1/meetings/870f51ff287b41be84648412901e0402/globalCallinNumbers",
                        "method": "GET"
                    }
                ]
            }
        },

```

###### Viewing the Log of the Participants
The meeting invite list can tell you who was invited, but it does not reveal who actually attended. Once a meeting is in progress or ended, you can query for a list of participants using: - /v1/meetingParticipants
With meetingID as a query parameter, you can request this information as follows: <https://webexapis.com/v1/meetingParticipants?meetingId=501e995485e2460bb129410116757b13_I_194316955237236650>
This will return a response something like:

```
{
    "items": [
        {
            "id": "870f51ff287b41be84648412901e0402_20191101T120000Z",
            "meetingSeriesId": "870f51ff287b41be84648412901e0402",
            "meetingNumber": "123456789",
            "title": "Example Daily Meeting",
            "agenda": "Example Agenda",
            "password": "BgJep@43",
            "phoneAndVideoSystemPassword": "12345678",
            "meetingType": "scheduledMeeting",
            "state": "ready",
            "isModified": false,
            "timezone": "UTC",
            "start": "2019-11-01T12:00:00Z",
            "end": "2019-11-01T13:00:00Z",
            "hostUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jN2ZkNzNmMi05ZjFlLTQ3ZjctYWEwNS05ZWI5OGJiNjljYzY",
            "hostDisplayName": "John Andersen",
            "hostEmail": "john.andersen@example.com",
            "hostKey": "123456",
            "siteUrl": "site4-example.webex.com",
            "webLink": "https://site4-example.webex.com/site4/j.php?MTID=md41817da6a55b0925530cb88b3577b1e",
            "sipAddress": "123456789@site4-example.webex.com",
            "dialInIpAddress": "192.168.100.100",
            "enabledAutoRecordMeeting": false,
            "allowAnyUserToBeCoHost": false,
            "enabledJoinBeforeHost": false,
            "enableConnectAudioBeforeHost": false,
            "joinBeforeHostMinutes": 0,
            "allowFirstUserToBeCoHost": false,
            "allowAuthenticatedDevices": false,
            "telephony": {
                "accessCode": "1234567890",
                "callInNumbers": [
                    {
                        "label": "US Toll",
                        "callInNumber": "123456789",
                        "tollType": "toll"
                    }
                ],
                "links": [
                    {
                        "rel": "globalCallinNumbers",
                        "href": "/api/v1/meetings/870f51ff287b41be84648412901e0402/globalCallinNumbers",
                        "method": "GET"
                    }
                ]
            }
        },

```

##### In This Article
  * [Access Meeting Resources Guide](https://developer.webex.com/meeting/docs/api/guides/access-meeting-resources-guide#access-meeting-resources-guide)


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
