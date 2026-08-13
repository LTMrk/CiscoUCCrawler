

---
# ORIGEN: https://developer.webex.com/docs/meetings

[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/meeting/docs/meetings)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/meeting/docs/meetings)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/meeting/docs/meetings)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Overview
Webex Meetings
  * [Overview](https://developer.webex.com/meeting/docs/meetings)
  * Guides
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
### Overview
The new Webex Meetings REST API enables seamless integration of Webex Meetings into your websites, apps, and services. Schedule meetings, invite meeting attendees, update preferences, and more.
**XML API Deprecation Announcement**  
The Meetings-related XML APIs will be deprecated and the End-of-Support (EoS) date is planned for the second half of 2023. Cisco will continue to resolve bugs up to this date, but new features will only be implemented for the REST APIs suite. The End-of-life (EoL) timeframe for Meetings-related XML APIs is targeted for **March 31, 2024** , at which time the APIs will be retired. For more information on how to migrate from XML to REST APIs, please see the [Webex Meetings XML to REST Migration Guide](https://developer.cisco.com/docs/webex-meetings/#xml-to-rest-migration-guide). User management APIs such as `CreateUser`, `SetUser`, `DelUser`, etc. are **NOT** affected by this EOL announcement.
####  anchorWebex Meetings
anchor
Webex Meetings offers integrated audio, video, and content sharing with highly secure web meetings from the cloud. The Webex Meetings REST API allows developers to add basic Webex scheduling functionality to their custom applications or websites. You can:
  * [Create and manage meetings](https://developer.webex.com/docs/api/v1/meetings)
  * [Add and manage meeting invitees](https://developer.webex.com/docs/api/v1/meeting-invitees)
  * [Get and update meeting preferences, options, and other details](https://developer.webex.com/docs/api/v1/meeting-preferences)
  * [Get, list, and delete recordings](https://developer.webex.com/docs/api/v1/recordings)


More APIs are on the way! Watch our [blog](https://developer.webex.com/blog) for announcements.
####  anchorCreating and Using Webex Apps
anchor
The base URL for the Webex REST API is <https://webexapis.com/v1/>. Detailed information about each API resource and endpoint can be found in the [API Reference](https://developer.webex.com/docs/api/v1/meetings).
The Meetings-related APIs can be used with Webex Integrations. If you aren't familiar with integrations, check out the [Integrations Guide](https://developer.webex.com/docs/integrations) for more information. To create a new integration, select [My Webex Apps](https://developer.webex.com/my-apps) from the menu under your avatar at the top of this page to get started.
To use the Webex REST API you'll need to be a Webex Meetings subscriber with a Webex account backed by Cisco Webex Common Identity (CI). If you currently use Webex, your account is backed by Common Identity. If you're using only Webex Meetings, your site will [need to be on Common Identity](https://help.webex.com/WBX000023841/).
####  anchorMeetings API Scopes
anchor
The table below lists all meetings APIs and their required scopes at different levels.
The `spark:all` scope is required for the [Create a Meeting](https://developer.webex.com/docs/api/v1/meetings/create-a-meeting) API when `roomId` is specified.  
| Resource  | API  | User Level Scopes  | Admin/Org Level Scopes  |  [Compliance Officer](https://developer.webex.com/docs/compliance#compliance) Level Scopes  | Group Level Scopes  |  
| --- | --- | --- | --- | --- | --- |  
| Meetings  | [List Meetings of a Meeting Series](https://developer.webex.com/docs/api/v1/meetings/list-meetings-of-a-meeting-series)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [Create a Meeting](https://developer.webex.com/docs/api/v1/meetings/create-a-meeting)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [Get a Meeting](https://developer.webex.com/docs/api/v1/meetings/get-a-meeting)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [Get a Meeting By an Admin](https://developer.webex.com/docs/api/v1/meetings/get-a-meeting-by-an-admin)  | N/A  | `meeting:admin_schedule_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [List Meetings](https://developer.webex.com/docs/api/v1/meetings/list-meetings)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [List Meetings By an Admin](https://developer.webex.com/docs/api/v1/meetings/list-meetings-by-an-admin)  | N/A  | `meeting:admin_schedule_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [List Group Meetings](https://developer.webex.com/docs/api/v1/meetings/list-group-meetings)  | N/A  | N/A  | N/A  | `meeting:group_meeting_read`  |  
|   | [Patch a Group Meeting](https://developer.webex.com/docs/api/v1/meetings/patch-a-group-meeting)  | N/A  | N/A  | N/A  | `meeting:group_meeting_write`  |  
|   | [Update a Meeting](https://developer.webex.com/docs/api/v1/meetings/update-a-meeting)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [Patch a Meeting](https://developer.webex.com/docs/api/v1/meetings/patch-a-meeting)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [Delete a Meeting](https://developer.webex.com/docs/api/v1/meetings/delete-a-meeting)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [Join a Meeting](https://developer.webex.com/docs/api/v1/meetings/join-a-meeting)  | `meeting:schedules_read`  | N/A  | N/A  | N/A  |  
|   | [Get Meeting Control Status](https://developer.webex.com/docs/api/v1/meetings/get-meeting-control-status)  | `meeting:controls_read`  | N/A  | N/A  | N/A  |  
|   | [Update Meeting Control Status](https://developer.webex.com/docs/api/v1/meetings/update-meeting-control-status)  | `meeting:controls_write`  | N/A  | N/A  | N/A  |  
|   | [Get registration form for a meeting](https://developer.webex.com/docs/api/v1/meetings/get-registration-form-for-a-meeting)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [Get Detailed Information for a Meeting Registrant](https://developer.webex.com/docs/api/v1/meetings/get-detailed-information-for-a-meeting-registrant)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [List Meeting Registrants](https://developer.webex.com/docs/api/v1/meetings/list-meeting-registrants)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [Batch Update Meeting Registrants status](https://developer.webex.com/docs/api/v1/meetings/batch-update-meeting-registrants-status)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [Register a Meeting Registrant](https://developer.webex.com/docs/api/v1/meetings/register-a-meeting-registrant)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [List Meeting Session Types](https://developer.webex.com/docs/api/v1/meetings/list-meeting-session-types)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [Get a Meeting Session Type](https://developer.webex.com/docs/api/v1/meetings/get-a-meeting-session-type)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [Reassign Meetings to a New Host](https://developer.webex.com/docs/api/v1/meetings/reassign-meetings-to-a-new-host)  | N/A  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
| Meeting Invitees  | [List Meeting Invitees](https://developer.webex.com/docs/api/v1/meeting-invitees/list-meeting-invitees)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [Create a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/create-a-meeting-invitee)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [Create Meeting Invitees](https://developer.webex.com/docs/api/v1/meeting-invitees/create-meeting-invitees)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [Get a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/get-a-meeting-invitee)  | `meeting:schedules_read`  | `meeting:admin_schedule_read`  | N/A  | N/A  |  
|   | [Update a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/update-a-meeting-invitee)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
|   | [Delete a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/delete-a-meeting-invitee)  | `meeting:schedules_write`  | `meeting:admin_schedule_write`  | N/A  | N/A  |  
| Meeting Participants  | [List Meeting Participants](https://developer.webex.com/docs/api/v1/meeting-participants/list-meeting-participants)  | `meeting:participants_read`  | `meeting:admin_participants_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Get Meeting Participant Details](https://developer.webex.com/docs/api/v1/meeting-participants/get-meeting-participant-details)  | `meeting:participants_read`  | `meeting:admin_participants_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Update a Participant](https://developer.webex.com/docs/api/v1/meeting-participants/update-a-participant)  | `meeting:participants_write`  | N/A  | N/A  | N/A  |  
|   | [Admit Participants](https://developer.webex.com/docs/api/v1/meeting-participants/admit-participants)  | `meeting:participants_write`  | N/A  | N/A  | N/A  |  
|   | [Call Out a SIP Participant](https://developer.webex.com/docs/api/v1/meeting-participants/call-out-a-sip-participant)  | `meeting:participants_write`  | N/A  | N/A  | N/A  |  
|   | [Cancel Calling Out a SIP Participant](https://developer.webex.com/docs/api/v1/meeting-participants/cancel-calling-out-a-sip-participant)  | `meeting:participants_write`  | N/A  | N/A  | N/A  |  
| Recordings  | [List Recordings](https://developer.webex.com/docs/api/v1/recordings/list-recordings)  | `meeting:recordings_read`  | `meeting:admin_recordings_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Query Recordings](https://developer.webex.com/docs/api/v1/recordings/query-recordings)  | `meeting:recordings_read`  | `meeting:admin_recordings_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [List Recordings For an Admin or Compliance Officer](https://developer.webex.com/docs/api/v1/recordings/list-recordings-for-an-admin-or-compliance-officer)  | N/A  | `meeting:admin_recordings_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Query Recordings For an Admin or Compliance Officer](https://developer.webex.com/docs/api/v1/recordings/query-recordings-for-an-admin-or-compliance-officer)  | N/A  | `meeting:admin_recordings_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Get Recording Details](https://developer.webex.com/docs/api/v1/recordings/get-recording-details)  | `meeting:recordings_read`  | `meeting:admin_recordings_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Delete a Recording](https://developer.webex.com/docs/api/v1/recordings/delete-a-recording)  | `meeting:recordings_write`  | `meeting:admin_recordings_write`  | `spark-compliance:meetings_write`  | N/A  |  
|   | [Delete a Recording By an Admin](https://developer.webex.com/docs/api/v1/recordings/delete-a-recording-by-an-admin)  | N/A  | `meeting:admin_recordings_write`  | N/A  | N/A  |  
|   | [Move Recordings into the Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/move-recordings-into-the-recycle-bin)  | `meeting:recordings_write`  | `meeting:admin_recordings_write`  | N/A  | N/A  |  
|   | [Restore Recordings from Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/restore-recordings-from-recycle-bin)  | `meeting:recordings_write`  | `meeting:admin_recordings_write`  | N/A  | N/A  |  
|   | [Purge Recordings from Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/purge-recordings-from-recycle-bin)  | `meeting:recordings_write`  | `meeting:admin_recordings_write`  | N/A  | N/A  |  
|   | [Share a Recording](https://developer.webex.com/docs/api/v1/recordings/share-a-recording)  | `meeting:recordings_write`  | `meeting:admin_recordings_write`  | N/A  | N/A  |  
|   | [Share a Recording Link](https://developer.webex.com/docs/api/v1/recordings/share-a-recording-link)  | `meeting:recordings_write`  | `meeting:admin_recordings_write`  | N/A  | N/A  |  
|   | [List Group Recordings](https://developer.webex.com/docs/api/v1/recordings/list-group-recordings)  | N/A  | N/A  | N/A  | `meeting:group_meeting_read`  |  
|   | [Get Group Recording Details](https://developer.webex.com/docs/api/v1/recordings/get-group-recording-details)  | N/A  | N/A  | N/A  | `meeting:group_meeting_read`  |  
| Recording Reports  | [List of Recording Audit Report Summaries](https://developer.webex.com/docs/api/v1/recording-report/list-of-recording-audit-report-summaries)  | `meeting:recordings_read`  | `meeting:admin_recordings_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Get Recording Audit Report Details](https://developer.webex.com/docs/api/v1/recording-report/get-recording-audit-report-details)  | `meeting:recordings_read`  | `meeting:admin_recordings_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [List Meeting Archive Summaries](https://developer.webex.com/docs/api/v1/recording-report/list-meeting-archive-summaries)  | N/A  | `meeting:admin_recordings_read`  | N/A  | N/A  |  
|   | [Get Meeting Archive Details](https://developer.webex.com/docs/api/v1/recording-report/get-meeting-archive-details)  | N/A  | `meeting:admin_recordings_read`  | N/A  | N/A  |  
| Meeting Transcripts  | [List Meeting Transcripts](https://developer.webex.com/docs/api/v1/meeting-transcripts/list-meeting-transcripts)  |  `meeting:transcripts_read`  
`meeting:schedules_read`  | `meeting:admin_transcripts_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Download a meeting transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/download-a-meeting-transcript)  |  `meeting:transcripts_read`  
`meeting:schedules_read`  | `meeting:admin_transcripts_read`  | `spark-compliance:meetings_read`  | N/A  |  
|   | [List Snippets of a Meeting Transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/list-snippets-of-a-meeting-transcript)  | `meeting:transcripts_read`  | N/A  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Get a Transcript Snippet](https://developer.webex.com/docs/api/v1/meeting-transcripts/get-a-transcript-snippet)  | `meeting:transcripts_read`  | N/A  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Update a Transcript Snippet](https://developer.webex.com/docs/api/v1/meeting-transcripts/update-a-transcript-snippet)  | `meeting:transcripts_write`  | N/A  | `spark-compliance:meetings_write`  | N/A  |  
| Meeting Summaries  | [Get Summary by Meeting ID](https://developer.webex.com/docs/api/v1/meeting-summaries/get-summary-by-meeting-id)  | `meeting:summaries_read`  | N/A  | `spark-compliance:meetings_read`  | N/A  |  
|   | [Delete a Summary](https://developer.webex.com/docs/api/v1/meeting-summaries/delete-a-summary)  | `meeting:summaries_write`  | N/A  | `spark-compliance:meetings_write`  | N/A  |  
| Meeting Preferences  | [Get Meeting Preference Details](https://developer.webex.com/docs/api/v1/meeting-preferences/get-meeting-preference-details)  | `meeting:preferences_read`  | `meeting:admin_preferences_read`  | N/A  | N/A  |  
|   | [Get Personal Meeting Room Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-personal-meeting-room-options)  | `meeting:preferences_read`  | `meeting:admin_preferences_read`  | N/A  | N/A  |  
|   | [Update Personal Meeting Room Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-personal-meeting-room-options)  | `meeting:preferences_write`  | `meeting:admin_preferences_write`  | N/A  | N/A  |  
|   | [Get Audio Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-audio-options)  | `meeting:preferences_read`  | `meeting:admin_preferences_read`  | N/A  | N/A  |  
|   | [Update Audio Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-audio-options)  | `meeting:preferences_write`  | `meeting:admin_preferences_write`  | N/A  | N/A  |  
|   | [Get Video Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-video-options)  | `meeting:preferences_read`  | `meeting:admin_preferences_read`  | N/A  | N/A  |  
|   | [Update Video Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-video-options)  | `meeting:preferences_write`  | `meeting:admin_preferences_write`  | N/A  | N/A  |  
|   | [Get Scheduling Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-scheduling-options)  | `meeting:preferences_read`  | `meeting:admin_preferences_read`  | N/A  | N/A  |  
|   | [Update Scheduling Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-scheduling-options)  | `meeting:preferences_write`  | `meeting:admin_preferences_write`  | N/A  | N/A  |  
|   | [Get Site List](https://developer.webex.com/docs/api/v1/meeting-preferences/get-site-list)  | `meeting:preferences_read`  | `meeting:admin_preferences_read`  | N/A  | N/A  |  
|   | [Update Default Site](https://developer.webex.com/docs/api/v1/meeting-preferences/update-default-site)  | `meeting:preferences_write`  | `meeting:admin_preferences_write`  | N/A  | N/A  |  
|   | [Batch Refresh Personal Meeting Room ID](https://developer.webex.com/docs/api/v1/meeting-preferences/batch-refresh-personal-meeting-room-id)  | N/A  |  `meeting:admin_preferences_write`  
`meeting:admin_config_write`  | N/A  | N/A  |  
| Meeting Reports  | [List Meeting Usage Reports](https://developer.webex.com/docs/api/v1/meetings-summary-report/list-meeting-usage-reports)  | N/A  | `meeting:admin_config_read`  | N/A  | N/A  |  
|   | [List Meeting Attendee Reports](https://developer.webex.com/docs/api/v1/meetings-summary-report/list-meeting-attendee-reports)  |  `meeting:participants_read`  
`meeting:schedules_read`  | `meeting:admin_config_read`  | N/A  | N/A  |  
Guest users can interact with regular Webex users via tokens generated by a [Guest Issuer](https://developer.webex.com/docs/guest-issuer) application. The table below lists the meetings APIs for guest issuer and the required scopes.  
| Resource  | API  |  [Guest Issuer](https://developer.webex.com/docs/guest-issuer) Scopes  |  
| --- | --- | --- |  
| Meetings  | [Get Detailed Information for a Meeting Registrant](https://developer.webex.com/docs/api/v1/meetings/get-detailed-information-for-a-meeting-registrant)  |  `webex-squared:locus_participant`  
`spark:all`  |  
|   | [List Meeting Registrants](https://developer.webex.com/docs/api/v1/meetings/list-meeting-registrants)  |  `webex-squared:locus_participant`  
`spark:all`  |  
|   | [Batch Update Meeting Registrants status](https://developer.webex.com/docs/api/v1/meetings/batch-update-meeting-registrants-status)  |  `webex-squared:locus_participant`  
`spark:all`  |  
|   | [Register a Meeting Registrant](https://developer.webex.com/docs/api/v1/meetings/register-a-meeting-registrant)  |  `webex-squared:locus_participant`  
`spark:all`  |  
|   | [Join a Meeting](https://developer.webex.com/docs/api/v1/meetings/join-a-meeting)  | `webex-squared:locus_participant`  |  
####  anchorUser Level Authentication and Scopes
anchor
Webex REST API authentication is described in detail in the [Integrations Guide](https://developer.webex.com/docs/integrations). The following scopes are required to use the meetings-related API resources:
The `spark:all` scope is required for the [Create a Meeting](https://developer.webex.com/docs/api/v1/meetings/create-a-meeting) API when `roomId` is specified.  
| Scope  | Usage  | Accessible APIs  |  
| --- | --- | --- |  
| `meeting:schedules_read`  | Retrieve your Webex meeting lists and details  |  [List Meetings of a Meeting Series](https://developer.webex.com/docs/api/v1/meetings/list-meetings-of-a-meeting-series)  
[Get a Meeting](https://developer.webex.com/docs/api/v1/meetings/get-a-meeting)  
[List Meetings](https://developer.webex.com/docs/api/v1/meetings/list-meetings)  
[Join a Meeting](https://developer.webex.com/docs/api/v1/meetings/join-a-meeting)  
[List Meeting Invitees](https://developer.webex.com/docs/api/v1/meeting-invitees/list-meeting-invitees)  
[Get a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/get-a-meeting-invitee)  
[List Meeting Transcripts](https://developer.webex.com/docs/api/v1/meeting-transcripts/list-meeting-transcripts)  
[Download a meeting transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/download-a-meeting-transcript)  
[Get registration form for a meeting](https://developer.webex.com/docs/api/v1/meetings/get-registration-form-for-a-meeting)  
[Get Detailed Information for a Meeting Registrant](https://developer.webex.com/docs/api/v1/meetings/get-detailed-information-for-a-meeting-registrant)  
[List Meeting Registrants](https://developer.webex.com/docs/api/v1/meetings/list-meeting-registrants)  
[List Meeting Session Types](https://developer.webex.com/docs/api/v1/meetings/list-meeting-session-types)  
[Get a Meeting Session Type](https://developer.webex.com/docs/api/v1/meetings/get-a-meeting-session-type)  
[List Meeting Attendee Reports](https://developer.webex.com/docs/api/v1/meetings-summary-report/list-meeting-attendee-reports)  
[Webhook APIs](https://developer.webex.com/docs/api/v1/webhooks) for Meetings  |  
| `meeting:schedules_write`  | Create, manage, or cancel your scheduled Webex meetings  |  [Create a Meeting](https://developer.webex.com/docs/api/v1/meetings/create-a-meeting)  
[Update a Meeting](https://developer.webex.com/docs/api/v1/meetings/update-a-meeting)  
[Patch a Meeting](https://developer.webex.com/docs/api/v1/meetings/patch-a-meeting)  
[Delete a Meeting](https://developer.webex.com/docs/api/v1/meetings/delete-a-meeting)  
[Create a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/create-a-meeting-invitee)  
[Update a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/update-a-meeting-invitee)  
[Delete a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/delete-a-meeting-invitee)  
[Create Meeting Invitees](https://developer.webex.com/docs/api/v1/meeting-invitees/create-meeting-invitees)  
[Batch Update Meeting Registrants status](https://developer.webex.com/docs/api/v1/meetings/batch-update-meeting-registrants-status)  
[Register a Meeting Registrant](https://developer.webex.com/docs/api/v1/meetings/register-a-meeting-registrant)  |  
| `meeting:recordings_read`  | Retrieve your Webex meeting recordings for playback and recording reports  |  [List Recordings](https://developer.webex.com/docs/api/v1/recordings/list-recordings)  
[Query Recordings](https://developer.webex.com/docs/api/v1/recordings/query-recordings)  
[Get Recording Details](https://developer.webex.com/docs/api/v1/recordings/get-recording-details)  
[List of Recording Audit Report Summaries](https://developer.webex.com/docs/api/v1/recording-report/list-of-recording-audit-report-summaries)  
[Get Recording Audit Report Details](https://developer.webex.com/docs/api/v1/recording-report/get-recording-audit-report-details)  
[Webhook APIs](https://developer.webex.com/docs/api/v1/webhooks)  |  
| `meeting:recordings_write`  | Manage or delete your meeting recordings for playback  |  [Delete a Recording](https://developer.webex.com/docs/api/v1/recordings/delete-a-recording)  
[Move Recordings into the Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/move-recordings-into-the-recycle-bin)  
[Restore Recordings from Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/restore-recordings-from-recycle-bin)  
[Purge Recordings from Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/purge-recordings-from-recycle-bin)  
[Share a Recording](https://developer.webex.com/docs/api/v1/recordings/share-a-recording)  
[Share a Recording Link](https://developer.webex.com/docs/api/v1/recordings/share-a-recording-link)  |  
| `meeting:transcripts_read`  | Retrieve your Webex meetings transcripts  |  [List Meeting Transcripts](https://developer.webex.com/docs/api/v1/meeting-transcripts/list-meeting-transcripts)  
[Download a meeting transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/download-a-meeting-transcript)  
[List Snippets of a Meeting Transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/list-snippets-of-a-meeting-transcript)  
[Get a Transcript Snippet](https://developer.webex.com/docs/api/v1/meeting-transcripts/get-a-transcript-snippet)  |  
| `meeting:transcripts_write`  | Manage your Webex meeting transcript snippets  | [Update a Transcript Snippet](https://developer.webex.com/docs/api/v1/meeting-transcripts/update-a-transcript-snippet)  |  
| `meeting:summaries_read`  | Retrieve your Webex meeting summaries  | [Get Summary by Meeting ID](https://developer.webex.com/docs/api/v1/meeting-summaries/get-summary-by-meeting-id)  |  
| `meeting:summaries_write`  | Manage your Webex meeting summaries  | [Delete a Summary](https://developer.webex.com/docs/api/v1/meeting-summaries/delete-a-summary)  |  
| `meeting:preferences_read`  | Retrieve your Webex meeting preferences  |  [Get Meeting Preference Details](https://developer.webex.com/docs/api/v1/meeting-preferences/get-meeting-preference-details)  
[Get Personal Meeting Room Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-personal-meeting-room-options)  
[Get Audio Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-audio-options)  
[Get Video Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-video-options)  
[Get Scheduling Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-scheduling-options)  
[Get Site List](https://developer.webex.com/docs/api/v1/meeting-preferences/get-site-list)  |  
| `meeting:preferences_write`  | Edit your Webex meeting preferences  |  [Update Personal Meeting Room Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-personal-meeting-room-options)  
[Update Audio Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-audio-options)  
[Update Video Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-video-options)  
[Update Scheduling Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-scheduling-options)  
[Update Default Site](https://developer.webex.com/docs/api/v1/meeting-preferences/update-default-site)  |  
| `meeting:participants_read`  | Read participant information from meetings  |  [List Meeting Participants](https://developer.webex.com/docs/api/v1/meeting-participants/list-meeting-participants)  
[Get Meeting Participant Details](https://developer.webex.com/docs/api/v1/meeting-participants/get-meeting-participant-details)  
[Update a Participant](https://developer.webex.com/docs/api/v1/meeting-participants/update-a-participant)  
[Admit Participants](https://developer.webex.com/docs/api/v1/meeting-participants/admit-participants)  
[List Meeting Attendee Reports](https://developer.webex.com/docs/api/v1/meetings-summary-report/list-meeting-attendee-reports)  
[Webhook APIs](https://developer.webex.com/docs/api/v1/webhooks) for Meeting Participants  |  
| `meeting:participants_write`  | Manage participants within meetings  |  [Update a Participant](https://developer.webex.com/docs/api/v1/meeting-participants/update-a-participant)  
[Admit Participants](https://developer.webex.com/docs/api/v1/meeting-participants/admit-participants)  
[Call Out a SIP Participant](https://developer.webex.com/docs/api/v1/meeting-participants/call-out-a-sip-participant)  
[Cancel Calling Out a SIP Participant](https://developer.webex.com/docs/api/v1/meeting-participants/cancel-calling-out-a-sip-participant)  |  
| `meeting:controls_read`  | Read meeting control information for in-progress meetings  | [Get Meeting Control Status](https://developer.webex.com/docs/api/v1/meetings/get-meeting-control-status)  |  
| `meeting:controls_write`  | Update meeting controls for in-progress meetings  | [Update Meeting Control Status](https://developer.webex.com/docs/api/v1/meetings/update-meeting-control-status)  |  
Remember, when choosing scopes for your app, only select the scopes your application will need.
####  anchorAdmin/Organization Level Authentication and Scopes
anchor
Webex developers now have the ability to leverage admin level scopes in their integrations. These new scopes allow WebEx Admin grant scopes to integrations on behalf of other users. This allows developers and admins flexibility in creating integrations to meet their needs and can lessen the need for individual users of an integration to perform an OAuth grant.
Several conditions and restrictions apply to organizations that want to authorize an integration that utilizes these admin level scopes.
The `spark:all` scope is required for the [Create a Meeting](https://developer.webex.com/docs/api/v1/meetings/create-a-meeting) API when `roomId` is specified.
  * The admin that authorizes the integration for an organization (meeting:admin_* scopes) must be a full org admin. This admin must also be a site admin for the site or sites that contain the users they wish the integration to be able to act on behalf of.
  * Partners: Partner admins who are also full org admins for their own org are not permitted to authorize integrations that use these admin level scopes for their customer's org. They are however able to authorize these types of integrations in their own org as per the previous requirement.


In support of this functionality the admin must grant the integration the following admin scopes:  
| Scope  | Usage  | Accessible APIs  |  
| --- | --- | --- |  
| `meeting:admin_schedule_read`  | Retrieve meetings of all WebEx users of your organization  |  [Get a Meeting](https://developer.webex.com/docs/api/v1/meetings/get-a-meeting)  
[Get a Meeting By an Admin](https://developer.webex.com/docs/api/v1/meetings/get-a-meeting-by-an-admin)  
[List Meetings](https://developer.webex.com/docs/api/v1/meetings/list-meetings)  
[List Meetings By an Admin](https://developer.webex.com/docs/api/v1/meetings/list-meetings-by-an-admin)  
[List Meetings of a Meeting Series](https://developer.webex.com/docs/api/v1/meetings/list-meetings-of-a-meeting-series)  
[List Meeting Invitees](https://developer.webex.com/docs/api/v1/meeting-invitees/list-meeting-invitees)  
[Get a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/get-a-meeting-invitee)  
[Get registration form for a meeting](https://developer.webex.com/docs/api/v1/meetings/get-registration-form-for-a-meeting)  
[Get Detailed Information for a Meeting Registrant](https://developer.webex.com/docs/api/v1/meetings/get-detailed-information-for-a-meeting-registrant)  
[List Meeting Registrants](https://developer.webex.com/docs/api/v1/meetings/list-meeting-registrants)  
[Webhook APIs](https://developer.webex.com/docs/api/v1/webhooks) for Meetings  |  
| `meeting:admin_schedule_write`  | Create, manage, or cancel meetings of all WebEx users of your organization  |  [Create a Meeting](https://developer.webex.com/docs/api/v1/meetings/create-a-meeting)  
[Update a Meeting](https://developer.webex.com/docs/api/v1/meetings/update-a-meeting)  
[Patch a Meeting](https://developer.webex.com/docs/api/v1/meetings/patch-a-meeting)  
[Delete a Meeting](https://developer.webex.com/docs/api/v1/meetings/delete-a-meeting)  
[Create a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/create-a-meeting-invitee)  
[Update a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/update-a-meeting-invitee)  
[Delete a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/delete-a-meeting-invitee)  
[Reassign Meetings to a New Host](https://developer.webex.com/docs/api/v1/meetings/reassign-meetings-to-a-new-host)  |  
| `meeting:admin_recordings_read`  | Retrieve recordings and meeting archive reports of all WebEx users of your organization  |  [Get Recording Details](https://developer.webex.com/docs/api/v1/recordings/get-recording-details)  
[List Recordings](https://developer.webex.com/docs/api/v1/recordings/list-recordings)  
[Query Recordings](https://developer.webex.com/docs/api/v1/recordings/query-recordings)  
[List Recordings For an Admin or Compliance Officer](https://developer.webex.com/docs/api/v1/recordings/list-recordings-for-an-admin-or-compliance-officer)  
[Query Recordings For an Admin or Compliance Officer](https://developer.webex.com/docs/api/v1/recordings/query-recordings-for-an-admin-or-compliance-officer)  
[List of Recording Audit Report Summaries](https://developer.webex.com/docs/api/v1/recording-report/list-of-recording-audit-report-summaries)  
[Get Recording Audit Report Details](https://developer.webex.com/docs/api/v1/recording-report/get-recording-audit-report-details)  
[List Meeting Archive Summaries](https://developer.webex.com/docs/api/v1/recording-report/list-meeting-archive-summaries)  
[Get Meeting Archive Details](https://developer.webex.com/docs/api/v1/recording-report/get-meeting-archive-details)  
[Webhook APIs](https://developer.webex.com/docs/api/v1/webhooks)  |  
| `meeting:admin_recordings_write`  | Manage or delete recordings of all WebEx users of your organization  |  [Delete a Recording](https://developer.webex.com/docs/api/v1/recordings/delete-a-recording)  
[Delete a Recording By an Admin](https://developer.webex.com/docs/api/v1/recordings/delete-a-recording-by-an-admin)  
[Move Recordings into the Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/move-recordings-into-the-recycle-bin)  
[Restore Recordings from Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/restore-recordings-from-recycle-bin)  
[Purge Recordings from Recycle Bin](https://developer.webex.com/docs/api/v1/recordings/purge-recordings-from-recycle-bin)  
[Share a Recording](https://developer.webex.com/docs/api/v1/recordings/share-a-recording)  
[Share a Recording Link](https://developer.webex.com/docs/api/v1/recordings/share-a-recording-link)  |  
| `meeting:admin_transcripts_read`  | Retrieve Webex meetings transcripts of all WebEx users of your organization  |  [List Meeting Transcripts](https://developer.webex.com/docs/api/v1/meeting-transcripts/list-meeting-transcripts)  
[Download a meeting transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/download-a-meeting-transcript)  |  
| `meeting:admin_preferences_read`  | Retrieve Webex meeting preferences of all WebEx users of your organization  |  [Get Meeting Preference Details](https://developer.webex.com/docs/api/v1/meeting-preferences/get-meeting-preference-details)  
[Get Personal Meeting Room Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-personal-meeting-room-options)  
[Get Audio Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-audio-options)  
[Get Video Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-video-options)  
[Get Scheduling Options](https://developer.webex.com/docs/api/v1/meeting-preferences/get-scheduling-options)  
[Get Site List](https://developer.webex.com/docs/api/v1/meeting-preferences/get-site-list)  |  
| `meeting:admin_preferences_write`  | Manage meeting preferences of all WebEx users of your organization  |  [Update Personal Meeting Room Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-personal-meeting-room-options)  
[Update Audio Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-audio-options)  
[Update Video Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-video-options)  
[Update Scheduling Options](https://developer.webex.com/docs/api/v1/meeting-preferences/update-scheduling-options)  
[Update Default Site](https://developer.webex.com/docs/api/v1/meeting-preferences/update-default-site)  
[Batch Refresh Personal Meeting Room ID](https://developer.webex.com/docs/api/v1/meeting-preferences/batch-refresh-personal-meeting-room-id)  |  
| `meeting:admin_participants_read`  | Read participant information from meetings for all WebEx users of your organization  |  [Get Meeting Participant Details](https://developer.webex.com/docs/api/v1/meeting-participants/get-meeting-participant-details)  
[List Meeting Participants](https://developer.webex.com/docs/api/v1/meeting-participants/list-meeting-participants)  
[Update a Participant](https://developer.webex.com/docs/api/v1/meeting-participants/update-a-participant)  
[Admit Participants](https://developer.webex.com/docs/api/v1/meeting-participants/admit-participants)  
[Webhook APIs](https://developer.webex.com/docs/api/v1/webhooks) for Meeting Participants  |  
| `meeting:admin_config_read`  | Retrieve Webex meeting configurations as an administrator  |  [List Meeting Usage Reports](https://developer.webex.com/docs/api/v1/meetings-summary-report/list-meeting-usage-reports)  
[List Meeting Attendee Reports](https://developer.webex.com/docs/api/v1/meetings-summary-report/list-meeting-attendee-reports)  |  
| `meeting:admin_config_write`  | Manage Webex meeting configurations as an administrator  | [Batch Refresh Personal Meeting Room ID](https://developer.webex.com/docs/api/v1/meeting-preferences/batch-refresh-personal-meeting-room-id)  |  
The admin feature applies to both CI-enabled or CI-linked Webex sites. The managed user account (host) does not need to be CI-enabled/CI-linked.
In support of this feature, the following will be allowed as query parameters on GET requests and as valid attributes in the request body of POST and PUT commands:
  * `hostEmail` - When set as a query parameter on a GET request made by an admin, the response will be the meetings where the user of `hostEmail` is the meeting host or an invitee, not the meetings for the admin user. When set as part of the request body sent to a POST method by an admin, the specified user will be the host of the meeting if he belongs to a site managed by the admin user. When set as part of the request body sent to a PUT or PATCH method, the field is not editable and is only used to update or patch a meeting on behalf of the real meeting host. Please use the [Reassign Meetings to a New Host](https://developer.webex.com/docs/api/v1/meetings/reassign-meetings-to-a-new-host) API if you need to update the meeting host. The meeting will belong to the specified host's default site unless the `siteUrl` attribute is used to override this.
  * `siteUrl` - optional - When set as a query parameter on a GET request, the response will be restricted to the meetings that belong to the specified site that are hosted by the caller of the API, or by the user specified via the `hostEmail` parameter. When set as part of the request body sent to a POST or PUT method, this attribute allows the caller of the API to create a meeting in a non-preferred site for a host whose account is associated with multiple sites.


Developers can become aware of the allowable values for `siteUrl` by querying the [GET /meetingPreferences/sites](https://developer.webex.com/docs/api/v1/meeting-preferences/get-site-list) API.
####  anchorGroup Level Authentication and Scopes
anchor
A [service app](https://developer.webex.com/docs/service-apps) can be authorized with group level privileges including the groups and sites it manages. A service app with group level privileges can access or manage resources at group level.  
| Scope  | Usage  | Accessible APIs  |  
| --- | --- | --- |  
| `meeting:group_meeting_read`  | Access resources at group level  |  [List Group Recordings](https://developer.webex.com/docs/api/v1/recordings/list-group-recordings)  
[Get Group Recording Details](https://developer.webex.com/docs/api/v1/recordings/get-group-recording-details)  
[List Group Meetings](https://developer.webex.com/docs/api/v1/meetings/list-group-meetings)  |  
| `meeting:group_meeting_write`  | Manage resources at group level  | [Patch a Group Meeting](https://developer.webex.com/docs/api/v1/meetings/patch-a-group-meeting)  |  
####  anchorCompliance Officer Level Authentication and Scopes
anchor
An administrator user can be associated with a specific role to become a [Compliance Officer](https://developer.webex.com/docs/compliance#compliance). The role of a compliance officer is to ensure that a company is conducting its business in full compliance with all laws and regulations that pertain to its particular industry, as well as professional standards, accepted business practices, and internal standards. The following scopes are required to use the meetings-related API resources as a Compliance Officer:  
| Scope  | Usage  | Accessible APIs  |  
| --- | --- | --- |  
| `spark-compliance:meetings_read`  | Access to read recordings, transcripts, chats, meeting participants, meeting closed captions, and meeting Q and A resources in your user’s organization  |  [Get Recording Details](https://developer.webex.com/docs/api/v1/recordings/get-recording-details)  
[List Recordings](https://developer.webex.com/docs/api/v1/recordings/list-recordings)  
[Query Recordings](https://developer.webex.com/docs/api/v1/recordings/query-recordings)  
[List Recordings For an Admin or Compliance Officer](https://developer.webex.com/docs/api/v1/recordings/list-recordings-for-an-admin-or-compliance-officer)  
[Query Recordings For an Admin or Compliance Officer](https://developer.webex.com/docs/api/v1/recordings/query-recordings-for-an-admin-or-compliance-officer)  
[Get Meeting Participant Details](https://developer.webex.com/docs/api/v1/meeting-participants/get-meeting-participant-details)  
[List Meeting Participants](https://developer.webex.com/docs/api/v1/meeting-participants/list-meeting-participants)  
[Query Meeting Participants with Email](https://developer.webex.com/docs/api/v1/meeting-participants/query-meeting-participants-with-email)  
[List Meeting Transcripts](https://developer.webex.com/docs/api/v1/meeting-transcripts/list-meeting-transcripts)  
[List Meeting Transcripts For Compliance Officer](https://developer.webex.com/api/v1/meeting-transcripts/list-meeting-transcripts-for-compliance-officer)  
[Download a meeting transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/download-a-meeting-transcript)  
[List Snippets of a Meeting Transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/list-snippets-of-a-meeting-transcript)  
[Get a Transcript Snippet](https://developer.webex.com/docs/api/v1/meeting-transcripts/get-a-transcript-snippet)  
[List of Recording Audit Report Summaries](https://developer.webex.com/docs/api/v1/recording-report/list-of-recording-audit-report-summaries)  
[Get Recording Audit Report Details](https://developer.webex.com/docs/api/v1/recording-report/get-recording-audit-report-details)  
[Webhook APIs](https://developer.webex.com/docs/api/v1/webhooks)  
[List Meeting Polls](https://developer.webex.com/docs/api/v1/meeting-polls/list-meeting-polls)  
[Get Meeting PollResults](https://developer.webex.com/docs/api/v1/meeting-polls/get-meeting-pollresults)  
[List Respondents of a Question](https://developer.webex.com/docs/api/v1/meeting-polls/list-respondents-of-a-question)  
[List Meeting Chats](https://developer.webex.com/docs/api/v1/meeting-chats/list-meeting-chats)  
[List Meeting Closed Captions](https://developer.webex.com/docs/api/v1/meeting-closed-captions/list-meeting-closed-captions)  
[List Meeting Closed Caption Snippets](https://developer.webex.com/docs/api/v1/meeting-closed-captions/list-meeting-closed-caption-snippets)  
[Download Meeting Closed Caption Snippets](https://developer.webex.com/docs/api/v1/meeting-closed-captions/download-meeting-closed-caption-snippets)  
[List Meeting Q and A](https://developer.webex.com/docs/api/v1/meeting-q-and-a/list-meeting-q-and-a)  
[List Answers of a Question](https://developer.webex.com/docs/api/v1/meeting-q-and-a/list-answers-of-a-question)  
[Get a Meeting By an Admin](https://developer.webex.com/docs/api/v1/meetings/get-a-meeting-by-an-admin)  
[List Meetings By an Admin](https://developer.webex.com/docs/api/v1/meetings/list-meetings-by-an-admin)  
[Get Summary For Compliance Officer](https://developer.webex.com/docs/api/v1/meeting-summaries/get-summary-for-compliance-officer)  |  
| `spark-compliance:meetings_write`  | Access to delete recordings, transcripts, chats, and update transcripts resources in your user’s organization  |  [Delete a Recording](https://developer.webex.com/docs/api/v1/recordings/delete-a-recording)  
[Update a Transcript Snippet](https://developer.webex.com/docs/api/v1/meeting-transcripts/update-a-transcript-snippet)  
[Delete a Transcript](https://developer.webex.com/docs/api/v1/meeting-transcripts/delete-a-transcript)  
[Delete Meeting Chats](https://developer.webex.com/docs/api/v1/meeting-chats/delete-meeting-chats)  
[Delete Meeting Summaries](https://developer.webex.com/docs/api/v1/meeting-summaries/delete-a-summary)  |  
####  anchorScopes and User Roles
anchor
The table below lists the relationship between scopes and user roles:  
| Scope  | Role  |  
| --- | --- |  
|  `meeting:admin_schedule_read`  
`meeting:admin_schedule_write`  
`meeting:admin_recordings_read`  
`meeting:admin_recordings_write`  
`meeting:admin_transcripts_read`  
`meeting:admin_preferences_read`  
`meeting:admin_preferences_write`  
`meeting:admin_participants_read`  | Full admin  
Content admin  |  
|  `meeting:admin_config_read`  
`meeting:admin_config_write`  | Site admin  |  
|  `meeting:group_meeting_read`  
`meeting:group_meeting_write`  | Group admin  |  
|  `spark-compliance:meetings_read`  
`spark-compliance:meetings_write`  | Compliance officer  |  
|  `meeting:schedules_read`  
`meeting:schedules_write`  
`meeting:recordings_read`  
`meeting:recordings_write`  
`meeting:transcripts_read`  
`meeting:transcripts_write`  
`meeting:preferences_read`  
`meeting:preferences_write`  
`meeting:participants_read`  
`meeting:participants_write`  
`meeting:controls_read`  
`meeting:controls_write`  | Individual user  |  
|  `webex-squared:locus_participant`  
`spark:all`  | Guest Issuer  |  
####  anchorMeeting Series, Scheduled Meetings, and Meeting Instances
anchor
When using the [Meetings](https://developer.webex.com/docs/api/v1/meetings) and [Meeting Invitees](https://developer.webex.com/docs/api/v1/meeting-invitees) API resources, it's important to understand the difference between "meeting series", "scheduled meetings", and "meetings" objects. Each of these objects may be sent to or received from the API. To differentiate them, the value of the `meetingType` attribute in the object will be one of:
  * `meetingSeries` – a container object that includes all of the scheduling information for a meeting
  * `scheduledMeeting` – an object that represents the information associated with the scheduling information associated with a single instance of a meeting; a scheduledMeeting object can be thought of as a “child” of a meetingSeries object
  * `meeting` – an object that represents a meeting that is currently happening or has happened in the past; this object is created only when a meeting starts


Both meeting series and scheduled meetings may be used with the API. For example, to invite an attendee to the series, use the ID of the meeting series with the [Create a Meeting Invitee](https://developer.webex.com/docs/api/v1/meeting-invitees/create-a-meeting-invitee) endpoint. Or, to invite someone to just one scheduled instance of a meeting, use the ID of the scheduled meeting instead.
####  anchorMeeting States
anchor
Different meeting states are available for each type of meeting object. See "Meeting Series, Scheduled Meetings, and Meeting Instances" above for more detail.
###### Meeting Series
  * `active` – one or more future scheduled meetings exists for this series
  * `inProgress` – an instance of this meeting is happening now or someone has joined meeting before the host and is waiting in the lobby
  * `expired` – all scheduled instances of this meeting have passed


###### Scheduled Meeting
  * `scheduled` – this meeting is scheduled in the future
  * `ready` – this meeting is ready to start
  * `ended` – this meeting was started and is now over
  * `missed` – this meeting was scheduled in the past but never happened


###### Meeting
  * `lobby` – a locked meeting has been joined by participants, but no hosts have joined
  * `inProgress` – the meeting has been joined and unlocked
  * `ended` – a meeting has concluded


####  anchorAvailable Meeting Attributes for Different Meeting States
anchor
The table below lists which meeting attributes are available for different meeting states when the meeting type is `meetingSeries`:  
| Attributes  | state=active  | state=inProgress  | state=expired  |  
| --- | --- | --- | --- |  
| `id`  | Yes  | Yes  | Yes  |  
| `meetingNumber`  | Yes  | Yes  | Yes  |  
| `title`  | Yes  | Yes  | Yes  |  
| `agenda`  | Yes  | Yes  | Yes  |  
| `password`  | Yes  | Yes  | Yes  |  
| `phoneAndVideoSystemPassword`  | Yes  | Yes  | Yes  |  
| `meetingType`  | Yes  | Yes  | Yes  |  
| `state`  | Yes  | Yes  | Yes  |  
| `isModified`  | No  | No  | No  |  
| `timezone`  | Yes  | Yes  | Yes  |  
| `start`  | Yes  | Yes  | Yes  |  
| `end`  | Yes  | Yes  | Yes  |  
| `recurrence`  | Yes  | Yes  | Yes  |  
| `hostUserId`  | Yes  | Yes  | Yes  |  
| `hostDisplayName`  | Yes  | Yes  | Yes  |  
| `hostEmail`  | Yes  | Yes  | Yes  |  
| `hostKey`  | Yes  | Yes  | Yes  |  
| `siteUrl`  | Yes  | Yes  | Yes  |  
| `webLink`  | Yes  | Yes  | Yes  |  
| `sipAddress`  | Yes  | Yes  | Yes  |  
| `dialInIpAddress`  | Yes  | Yes  | Yes  |  
| `enabledAutoRecordMeeting`  | Yes  | Yes  | Yes  |  
| `allowAnyUserToBeCoHost`  | Yes  | Yes  | Yes  |  
| `enabledJoinBeforeHost`  | Yes  | Yes  | Yes  |  
| `enableConnectAudioBeforeHost`  | Yes  | Yes  | Yes  |  
| `joinBeforeHostMinutes`  | Yes  | Yes  | Yes  |  
| `excludePassword`  | Yes  | Yes  | Yes  |  
| `publicMeeting`  | Yes  | Yes  | Yes  |  
| `reminderTime`  | Yes  | Yes  | Yes  |  
| `unlockedMeetingJoinSecurity`  | Yes  | Yes  | Yes  |  
| `enableAutomaticLock`  | Yes  | Yes  | Yes  |  
| `automaticLockMinutes`  | Yes  | Yes  | Yes  |  
| `allowFirstUserToBeCoHost`  | Yes  | Yes  | Yes  |  
| `allowAuthenticatedDevices`  | Yes  | Yes  | Yes  |  
| `telephony`  | Yes  | Yes  | Yes  |  
| `meetingOptions`  | Yes  | Yes  | Yes  |  
| `attendeePrivileges`  | Yes  | Yes  | Yes  |  
| `registration`  | Yes  | Yes  | No  |  
| `integrationTags`  | Yes  | Yes  | Yes  |  
| `scheduledType`  | Yes  | Yes  | Yes  |  
| `simultaneousInterpretation`  | Yes  | Yes  | Yes  |  
| `enabledBreakoutSessions`  | Yes  | Yes  | Yes  |  
| `links`  | Yes  | Yes  | Yes  |  
| `trackingCodes`  | Yes  | Yes  | Yes  |  
| `audioConnectionOptions`  | Yes  | Yes  | Yes  |  
The table below lists which meeting attributes are available for different meeting states when the meeting type is `scheduledMeeting`:  
| Attributes  | state=scheduled  | state=ready  | state=ended  | state=missed  |  
| --- | --- | --- | --- | --- |  
| `id`  | Yes  | Yes  | Yes  | Yes  |  
| `meetingNumber`  | Yes  | Yes  | Yes  | Yes  |  
| `title`  | Yes  | Yes  | Yes  | Yes  |  
| `agenda`  | Yes  | Yes  | Yes  | Yes  |  
| `password`  | Yes  | Yes  | Yes  | Yes  |  
| `phoneAndVideoSystemPassword`  | Yes  | Yes  | Yes  | Yes  |  
| `meetingType`  | Yes  | Yes  | Yes  | Yes  |  
| `state`  | Yes  | Yes  | Yes  | Yes  |  
| `isModified`  | Yes  | Yes  | Yes  | Yes  |  
| `timezone`  | Yes  | Yes  | Yes  | Yes  |  
| `start`  | Yes  | Yes  | Yes  | Yes  |  
| `end`  | Yes  | Yes  | Yes  | Yes  |  
| `recurrence`  | No  | No  | No  | No  |  
| `hostUserId`  | Yes  | Yes  | Yes  | Yes  |  
| `hostDisplayName`  | Yes  | Yes  | Yes  | Yes  |  
| `hostEmail`  | Yes  | Yes  | Yes  | Yes  |  
| `hostKey`  | Yes  | Yes  | Yes  | Yes  |  
| `siteUrl`  | Yes  | Yes  | Yes  | Yes  |  
| `webLink`  | Yes  | Yes  | Yes  | Yes  |  
| `sipAddress`  | Yes  | Yes  | Yes  | Yes  |  
| `dialInIpAddress`  | Yes  | Yes  | Yes  | Yes  |  
| `enabledAutoRecordMeeting`  | Yes  | Yes  | Yes  | Yes  |  
| `allowAnyUserToBeCoHost`  | Yes  | Yes  | Yes  | Yes  |  
| `enabledJoinBeforeHost`  | Yes  | Yes  | Yes  | Yes  |  
| `enableConnectAudioBeforeHost`  | Yes  | Yes  | Yes  | Yes  |  
| `joinBeforeHostMinutes`  | Yes  | Yes  | Yes  | Yes  |  
| `excludePassword`  | Yes  | Yes  | Yes  | Yes  |  
| `publicMeeting`  | Yes  | Yes  | Yes  | Yes  |  
| `reminderTime`  | Yes  | Yes  | Yes  | Yes  |  
| `unlockedMeetingJoinSecurity`  | Yes  | Yes  | Yes  | Yes  |  
| `enableAutomaticLock`  | Yes  | Yes  | Yes  | Yes  |  
| `automaticLockMinutes`  | Yes  | Yes  | Yes  | Yes  |  
| `allowFirstUserToBeCoHost`  | Yes  | Yes  | Yes  | Yes  |  
| `allowAuthenticatedDevices`  | Yes  | Yes  | Yes  | Yes  |  
| `telephony`  | Yes  | Yes  | Yes  | Yes  |  
| `meetingOptions`  | Yes  | Yes  | Yes  | Yes  |  
| `attendeePrivileges`  | Yes  | Yes  | Yes  | Yes  |  
| `registration`  | N/A  | Yes  | No  | No  |  
| `integrationTags`  | Yes  | Yes  | Yes  | Yes  |  
| `scheduledType`  | Yes  | Yes  | Yes  | Yes  |  
| `simultaneousInterpretation`  | Yes  | Yes  | Yes  | Yes  |  
| `enabledBreakoutSessions`  | Yes  | Yes  | Yes  | Yes  |  
| `links`  | Yes  | Yes  | Yes  | Yes  |  
| `trackingCodes`  | Yes  | Yes  | Yes  | Yes  |  
| `audioConnectionOptions`  | Yes  | Yes  | Yes  | Yes  |  
The table below lists which meeting attributes are available for different meeting states when the meeting type is `meeting`:  
| Attributes  | state=lobby  | state=inProgress  | state=ended  |  
| --- | --- | --- | --- |  
| `id`  | Yes  | Yes  | Yes  |  
| `meetingNumber`  | Yes  | Yes  | No  |  
| `title`  | Yes  | Yes  | Yes  |  
| `agenda`  | Yes  | Yes  | Yes  |  
| `password`  | No  | Yes  | No  |  
| `phoneAndVideoSystemPassword`  | No  | Yes  | No  |  
| `meetingType`  | Yes  | Yes  | Yes  |  
| `state`  | Yes  | Yes  | Yes  |  
| `isModified`  | No  | No  | No  |  
| `timezone`  | Yes  | Yes  | Yes  |  
| `start`  | Yes  | Yes  | Yes  |  
| `end`  | No  | No  | Yes  |  
| `recurrence`  | No  | No  | No  |  
| `hostUserId`  | Yes  | Yes  | Yes  |  
| `hostDisplayName`  | Yes  | Yes  | Yes  |  
| `hostEmail`  | Yes  | Yes  | Yes  |  
| `hostKey`  | No  | Yes  | No  |  
| `siteUrl`  | Yes  | Yes  | Yes  |  
| `webLink`  | Yes  | Yes  | Yes  |  
| `sipAddress`  | No  | Yes  | No  |  
| `dialInIpAddress`  | No  | Yes  | No  |  
| `enabledAutoRecordMeeting`  | No  | Yes  | No  |  
| `allowAnyUserToBeCoHost`  | No  | Yes  | No  |  
| `enabledJoinBeforeHost`  | No  | Yes  | No  |  
| `enableConnectAudioBeforeHost`  | No  | Yes  | No  |  
| `joinBeforeHostMinutes`  | No  | Yes  | No  |  
| `excludePassword`  | No  | Yes  | No  |  
| `publicMeeting`  | No  | Yes  | No  |  
| `reminderTime`  | No  | Yes  | No  |  
| `unlockedMeetingJoinSecurity`  | No  | Yes  | No  |  
| `enableAutomaticLock`  | No  | Yes  | No  |  
| `automaticLockMinutes`  | No  | Yes  | No  |  
| `allowFirstUserToBeCoHost`  | No  | Yes  | No  |  
| `allowAuthenticatedDevices`  | No  | Yes  | No  |  
| `telephony`  | No  | Yes  | No  |  
| `meetingOptions`  | No  | Yes  | No  |  
| `attendeePrivileges`  | No  | Yes  | No  |  
| `registration`  | Yes  | Yes  | No  |  
| `integrationTags`  | Yes  | Yes  | Yes  |  
| `scheduledType`  | Yes  | Yes  | Yes  |  
| `simultaneousInterpretation`  | No  | Yes  | No  |  
| `enabledBreakoutSessions`  | No  | Yes  | No  |  
| `links`  | No  | Yes  | No  |  
| `trackingCodes`  | No  | Yes  | No  |  
| `audioConnectionOptions`  | No  | Yes  | No  |  
####  anchorMeeting Lifecycle
anchor
###### Meeting Auto Delete
**Auto Delete Options**
![](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte8c404bd322b8380/5f89ff7a2f59ae27f3d617b5/Delete-from-My-Meetings-when-Completed.jpg)
There's a `Delete from My Meetings when completed` option in Webex page of classic view. It's invisible in Webex page of modern view and the default value is `unchecked`.
If the `Delete from My Meetings when completed` option is `unchecked` for a meeting, there will be a mandatory `Delete after 180 days` option for the meeting.
**Auto Delete Cases**
  1. If the `Delete from My Meetings when completed` option is `checked` for a non-recurring meeting, the meeting will be deleted automatically after the scheduled end time.
  2. If the `Delete from My Meetings when completed` option is `unchecked` for a non-recurring meeting, the meeting will be deleted automatically 180 days after the scheduled end time.
  3. If the `Delete from My Meetings when completed` option is `checked` for a meeting series, the entire meeting series will be deleted automatically after the scheduled end time of the last scheduled meeting of the meeting series.
  4. If the `Delete from My Meetings when completed` option is `unchecked` for a meeting series, the entire meeting will be deleted automatically 180 days after the scheduled end time of the last scheduled meeting of the meeting series.


###### Meeting Series Lifecycle
![Meeting Lifecycle Meeting Series](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt66ac4d5d17270ee4/5f89ff7af9d3bf27fac3c6eb/Meeting-Lifecycle-Meeting-Series.jpg)
  1. A meeting series is created.
  2. A scheduled meeting of the meeting series is started, or someone has joined the meeting before the host and is waiting in lobby.
  3. The ongoing scheduled meeting has ended, but it has not passed the scheduled end time of the last scheduled meeting of the meeting series, or the meeting has not yet been started and the participants which were previously waiting in lobby have left the meeting.
  4. The ongoing scheduled meeting is ended, and it has passed the scheduled end time of the last scheduled meeting of the meeting series.
  5. It has passed the scheduled end time of the last scheduled meeting of the meeting series.
  6. The meeting series is deleted manually or automatically after it's been expired.
  7. The meeting series is deleted manually.


###### Scheduled Meeting Lifecycle
![](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt31af4933e75e9db3/5f89ff78ace59e4b8291844f/Meeting-Lifecycle-Scheduled-Meeting.jpg)
  1. The parent meeting series is created. Any scheduled meeting other than the first one of the meeting series is `scheduled` and it can be started in the future.
  2. The parent meeting series is created. The first scheduled meeting of the meeting series is `ready` and it can be started immediately.
  3. It has passed the scheduled end time of the previous scheduled meeting. The subsequent scheduled meeting becomes `ready` and it can be started immediately.
  4. The previous `ready` scheduled meeting has been started and ended, and it has passed its scheduled end time. This scheduled meeting becomes `ended`.
  5. The previous `ready` scheduled meeting has never been started, and it has passed its scheduled end time. This scheduled meeting becomes `missed`.
  6. The scheduled meeting is deleted manually or it's deleted when the parent meeting series is deleted maunally.
  7. The scheduled meeting is deleted manually or it's deleted when the parent meeting series is deleted maunally or automatically.
  8. The scheduled meeting is deleted manually or it's deleted when the parent meeting series is deleted maunally.
  9. The scheduled meeting is deleted manually or it's deleted when the parent meeting series is deleted maunally or automatically.


###### Meeting Lifecycle
![Meeting Lifecycle Meeting](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltb1870666e295c7aa/5f89ff78271ecf4a1a6456c0/Meeting-Lifecycle-Meeting.jpg)
  1. A locked meeting has been joined by participants, but no hosts have joined.
  2. The meeting has been started and not ended yet.
  3. The participants in lobby have been admitted to meeting.
  4. The meeting has ended.


####  anchorMeeting Template Locales
anchor
Meetings can be created by meeting templates. The list of meeting templates that is available for the authenticated user can be retrieved from [List Meeting Templates](https://developer.webex.com/docs/api/v1/meetings/list-meeting-templates) API with different values of `locale`. All the locales supported by Webex are listed below:  
| Language  | Country/Region  | Locale Name  | Default Locale  |  
| --- | --- | --- | --- |  
| Bulgarian  | Bulgaria  | bg_BG  |   |  
| Castilian Spanish  | Spain  | es_SP  |   |  
| Chinese (Simplified)  | China  | zh_CN  |   |  
| Chinese (Traditional)  | Taiwan  | zh_TW  |   |  
| Croatian  | Croatia  | hr_HR  |   |  
| Czech  | Czech Republic  | cs_CZ  |   |  
| Danish  | Denmark  | da_DK  |   |  
| Dutch  | Netherlands  | nl_NL  |   |  
| English  | United Kingdom  | en_GB  |   |  
| English  | United States  | en_US  | Yes  |  
| French  | Canada  | fr_CA  |   |  
| French  | France  | fr_FR  |   |  
| German  | Germany  | de_DE  |   |  
| Hungarian  | Hungary  | hu_HU  |   |  
| Italian  | Italy  | it_IT  |   |  
| Japanese  | Japan  | ja_JP  |   |  
| Korean  | Korea  | ko_KR  |   |  
| Norwegian  | Norway  | no_NO  |   |  
| Polish  | Poland  | pl_PL  |   |  
| Portuguese  | Brazil  | pt_BR  |   |  
| Romanian  | Romania  | ro_RO  |   |  
| Russian  | Russia  | ru_RU  |   |  
| Serbian  | Serbia  | sr_RS  |   |  
| Spanish  | Mexico  | es_ES  |   |  
| Swedish  | Sweden  | sv_SE  |   |  
| Turkish  | Turkey  | tr_TR  |   |  
####  anchorWarnings
anchor
Some Meetings REST APIs have temporary restrictions due to known backend limitations, but the APIs overall will not fail. Instead, a warning message will be returned in a "Warning" response header to indicate the restrictions. In the warning message, there'll be a link pointing to here and one or multiple codes to lookup in the table below:  
| Code  | Title  | Message  |  
| --- | --- | --- |  
| 1001  | Unsupported attributes on a converged site.  | There's a feature gap that when creating or updating a meeting on a converged site, some of the meeting's attributes such as `publicMeeting`, `entryAndExitTone`, `audioConnectionType`, `meetingOptions.enabledPolling`, `meetingOptions.enabledNote`, `meetingOptions.noteType` and `meetingOptions.enabledUCFRichMedia` are not supported. Therefore, the values of these unsupported attributes in the API response may be different from those in the API request. This is a known issue for converged sites. These attributes will be supported incrementally as the gap being closed.  |  
####  anchorRestrictions on Updating a Meeting
anchor
When updating a meeting, there are different restrictions for different meeting types. It's important for a developer to understand these restrictions to avoid confusion and handle any restriction-related errors when they occur.
There are some general rules for updating a meeting. They are listed below.
###### Rule 1. `start` and `end` cannot be a time before the current time
This rule applies to meeting series and scheduled meeting.
When updating a meeting series or a scheduled meeting, the `start` and `end` in specified `timezone` cannot be a time before the current time. For example, assume that the current time is `2021-05-28T14:00:00+08:00`, if update a meeting series, or a scheduled meeting with `start` of `2021-05-27T14:00:00+08:00` and `timezone` of `Asia/Shanghai`, it will fail saying that "Parameter 'start' or 'end' is before current time". Please note that the default `timezone` is `UTC` if not specified explicitly.
###### Rule 2. Limit for duration between `start` and `end`
This rule applies to meeting series and scheduled meeting.
Duration between `start` and `end` cannot be shorter than 10 minutes or longer than 24 hours.
###### Rule 3. Update is forbidden when an associated meeting instance is in progress
This rule applies to meeting series and scheduled meeting.
When a meeting instance is in-progress, its parent scheduled meeting and grandparent meeting series cannot be updated. In fact, when a meeting instance is in-progress, the state of the parent scheduled meeting is `ready` which means that currently this scheduled meeting is ready to join, and the state of the grandparent meeting series is `inProgress` which means that a meeting instance of the series is currently happening. Neither the parent scheduled meeting, nor the grandparent meeting series can be updated until the ongoing meeting instance is ended. If break this rule, it'll fail saying that "Meeting is in progress".
###### Rule 4. Update is forbidden for a meeting instance
This rule applies to meeting instance.
It's totally forbidden to update any meeting instance of any state. It fails with an error message like "Meeting ID '06263e1088604fc1b3ca17fbe49fe97d_I_195989045032040979' is not allowed for this API."
###### Rule 5. Update is forbidden to cross recurring interval
This rule applies to scheduled meeting.
###### What is a recurring interval
When a meeting series has been scheduled, each scheduled meeting of this meeting series has its own "territory of time". It means that any other scheduled meeting of the same meeting series cannot be updated to fall into the range of time of this scheduled meeting. Specifically, each scheduled meeting has its original `timezone` when the parent meeting series was scheduled. It can be an explicitly specified value such as `Asia/Shanghai` or `UTC` by default if not specified explicitly. Generally, the recurring interval of a scheduled meeting begins at `00:00:00` (inclusive) in the original timezone of the day of `start`, and ends at `00:00:00` (exclusive) in the original timezone of the day of the next scheduled meeting of the same meeting series. However, there's exception for the first and the last scheduled meeting of a meeting series. The first one has no beginning, and the last one has no end. It's explained in detail below with examples of daily meetings and weekly meetings. The rule for other meetings, e.g. yearly meetings, is similar.
###### 1. Recurring intervals of a daily meeting series
![](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt6bc10925764a4209/60c00566324cea0e69782c3f/Restrictions_On_Updating_A_Meeting-01._Daily.jpg)
**Fig. 1** Recurring intervals of a daily meeting series
Fig. 1 illustrates the recurring intervals of a daily meeting series with four scheduled meetings.
  * **Recurring interval of`d1` :** No beginning, to `2021-04-20T00:00:00+08:00` (exclusive).
  * **Recurring interval of`d2` :** From `2021-04-20T00:00:00+08:00` (inclusive) to `2021-04-21T00:00:00+08:00` (exclusive).
  * **Recurring interval of`d3` :** From `2021-04-21T00:00:00+08:00` (inclusive) to `2021-04-22T00:00:00+08:00` (exclusive).
  * **Recurring interval of`d4` :** From `2021-04-22T00:00:00+08:00` (inclusive), no end.


###### 2. Recurring intervals of a weekly meeting series
![Restrictions On Updating A Meeting - Weekly](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltebb5e4e912c7ae25/60c005671b32a31d5305bd14/Restrictions_On_Updating_A_Meeting-02._Weekly.jpg)
**Fig. 2** Recurring intervals of a weekly meeting series
Fig. 2 illustrates the recurring intervals of a weekly meeting series with four scheduled meetings. Please note that recurring intervals of a weekly meeting can be of different lengths, and a single recurring interval may cross days.
  * **Recurring interval of`w1` :** No beginning, to `2021-06-04T00:00:00+08:00` (exclusive).
  * **Recurring interval of`w2` :** From `2021-06-04T00:00:00+08:00` (inclusive) to `2021-06-08T00:00:00+08:00` (exclusive).
  * **Recurring interval of`w3` :** From `2021-06-08T00:00:00+08:00` (inclusive) to `2021-06-11T10:00:00+08:00` (exclusive).
  * **Recurring interval of`w4` :** From `2021-06-11T10:00:00+08:00` (inclusive), no end.


###### 3. Recurring intervals of the first and last scheduled meetings of a meeting series
![Restrictions On Updating A Meeting - The First and The Last](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt7e5fb43b46dd8ab1/60c00568d475801b9d54f8e7/Restrictions_On_Updating_A_Meeting-03._The_first_and_the_last.jpg)
**Fig. 3** Recurring intervals of the first and last scheduled meetings of a meeting series
Please pay attention to the recurring intervals of the first and the last scheduled meetings of a meeting series:
  * The recurring interval of the first scheduled meeting of a meeting series has no beginning. For instance, Fig. 3 illustrates recurring intervals of a daily meeting series with three scheduled meetings. The recurring interval of `d1` which is highlighted in green has no beginning and ends at `2021-04-20T00:00:00+08:00` (exclusive). Therefore, `d1` can be updated to `d1-01` or `d1-02`.
  * The recurring interval of the last scheduled meeting of a meeting series has no end. For instance, in Fig. 3, the recurring interval of `d3` which is highlighted in blue begins at `2021-04-21T00:00:00+08:00` and has no end. Therefore, `d3` can be updated to `d3-01` or `d3-02`.


###### Cross-recurring-interval update is forbidden
Based on the `recurring interval` concept, cross-recurring-interval update is forbidden. If break this rule, it'll fail with an error message like "meeting.err.two_meeting_schedule_at_same_day". Specifically, meetings RESTful API examines `start` against crossing-recurring-interval behavior when updating a scheduled meeting, but it doesn't examine `end` against this rule.
###### 1. Update scheduled meetings of a daily meeting series successfully
![Restrictions On Updating A Meeting - Update Daily Success](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt6419d17597fdaa5c/60c005682d95121b9b3d15c5/Restrictions_On_Updating_A_Meeting-04._Update_Daily_Success.jpg)
**Fig. 4** Update scheduled meetings of a daily meeting series successfully
Fig. 4 illustrates non-cross-recurring-interval updates for scheduled meetings of a daily meeting series. All the updates in Fig. 4 are within the same recurring interval and succeed. For example:
  * **`d1`to`d1-s1` :** This update is within `d1`'s recurring interval. It makes the previously `missed` `d1` to be `ready` again.
  * **`d2`to`d2-s1` :** This update is within `d2`'s recurring interval. It makes `d2` a little earlier in the same day.
  * **`d2`to`d2-s2` :** This update is within `d2`'s recurring interval. It makes `d2` a little later in the same day.
  * **`d4`to`d4-s1` :** This update is within `d4`'s recurring interval. It makes `d4` a little earlier in the same day.
  * **`d4`to`d4-s2` :** This update is within `d4`'s recurring interval. It makes `d4` a little later in the same day.
  * **`d4`to`d4-s2` :** This update is within `d4`'s recurring interval. It makes `d4` a little later in the same day.
  * **`d4`to`d4-s3` or `d4-s4`:** This update is within `d4`'s recurring interval. It moves `d4` to the next day or even later. However, they are both within the recurring interval of `d4` since `d4` is the last scheduled meeting of the parent meeting series. It doesn't break `rule 5`.


###### 2. Update scheduled meetings of a daily meeting series crossing recurring interval
![Restrictions On Updating A Meeting - Update Daily Failure](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt03b31b621372bc65/60c0056885c4c2118e316fa5/Restrictions_On_Updating_A_Meeting-05._Update_Daily_Failure.jpg)
**Fig. 5** Update scheduled meetings of a daily meeting series crossing recurring interval
Fig. 5 illustrates cross-recurring-interval updates for scheduled meetings of a daily meeting series. All the updates in Fig. 5 break `rule 5` and fail. For example:
  * **`d1`to`d1-f1` :** This update moves `d1` to a time before the current time and breaks `rule 1`.
  * **`d2`to`d2-f1` :** This update moves `d2` to the previous day and breaks `rule 5`.
  * **`d2`to`d2-f2` :** This update moves `d2` to the next day and breaks `rule 5`.
  * **`d3`to`d3-f4` :** This update moves `d3` to two days later and breaks `rule 5`.
  * **`d4`to`d4-f2` :** This update moves `d4` to two days ago and breaks `rule 5`.


###### 3. Update scheduled meetings of a weekly meeting series successfully
![Restrictions On Updating A Meeting - Update Weekly Success](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt00749dbe2c63e863/60c00569fbd63412d4133e4f/Restrictions_On_Updating_A_Meeting-06._Update_Weekly_Success.jpg)
**Fig. 6** Update scheduled meetings of a weekly meeting series successfully
Fig. 6 illustrates non-cross-recurring-interval updates for scheduled meetings of a weekly meeting series. All the updates in Fig. 6 are within the same recurring interval and succeed. For example:
  * **`w1`to`w1-s1` :** This update is within `w1`'s recurring interval. It moves the previously `missed` `w1` to the next day and makes it `ready` again. It crosses day, but it doesn't cross recurring interval. So, it doesn't break `rule 5`.
  * **`w1`to`w1-s2` :** This update is within `w1`'s recurring interval. It moves the previously `missed` `w1` to two days later and makes it `ready` again. It crosses day, but it doesn't cross recurring interval. So, it doesn't break `rule 5`.
  * **`w2`to`w2-s1` :** This update is within `w2`'s recurring interval. It moves `w2` a little earlier in the same day.
  * **`w2`to`w2-s3` :** This update is within `w2`'s recurring interval. It moves `w2` three days later. It crosses day, but it doesn't cross recurring interval. So, it doesn't break `rule 5`.
  * **`w4`to`w4-s2` :** This update is within `w4`'s recurring interval. It moves `w4` to the two days later or even later than that. However, it's within `w4`'s recurring interval since `w4` is the last scheduled meeting of the parent meeting series. It doesn't break `rule 5`.


###### 4. Update scheduled meetings of a weekly meeting series crossing recurring interval
![Restrictions On Updating A Meeting - Update Weekly Failure](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltea6b9452560304eb/60c0056a68689d78c86312bc/Restrictions_On_Updating_A_Meeting-07._Update_Weekly_Failure.jpg)
**Fig. 7** Update scheduled meetings of a weekly meeting series crossing recurring interval
Fig. 7 illustrates cross-recurring-interval updates for scheduled meetings of a weekly meeting series. All the updates in Fig. 7 break `rule 5` and fail. For example:
  * **`w1`to`w1-f1` :** This update moves `w1` to a time before the current time and breaks `rule 1`.
  * **`w1`to`w1-f2` :** This update moves `w1` to the next recurring interval and breaks `rule 5`.
  * **`w2`to`w2-f1` :** This update moves `w2` to the previous recurring interval and breaks `rule 5`.
  * **`w2`to`w2-f2` :** This update moves `w2` to the next recurring interval and breaks `rule 5`.
  * **`w2`to`w2-f3` :** This update moves `w2` to the last recurring interval and breaks `rule 5`.
  * **`w4`to`w4-f2` :** This update moves `w4` to the second recurring interval and breaks `rule 5`.


###### 5. Boundary cases
![Restrictions On Updating A Meeting - Boundary Cases](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blta64e15576e40e2c5/60c0056bf8aee612d399694a/Restrictions_On_Updating_A_Meeting-08._Boundary_Cases.jpg)
**Fig. 8** Boundary cases
Meetings RESTful API examines `start` against crossing-recurring-interval behavior when updating a scheduled meeting, but it doesn't examine `end` against this rule. In other words, if the target `start` crosses recurring interval, the update breaks `rule 5`; if the target `start` doesn't cross recurring interval, it doesn't break `rule 5`.
Fig. 8 illustrates various boundary cases of updating a scheduled meeting of a daily meeting series. The upper part is moving `d1` towards `d2` and the lower part is moving `d2` towards `d1`.
The upper part is forward boundary cases:
  * **`d1`to`d1-b1` :** This update doesn't cross recurring interval. It doesn't break `rule 5`.
  * **`d1`to`d1-b2` :** The target `end` is on the boundary but the target `start` doesn't cross boundary. It doesn't break `rule 5`.
  * **`d1`to`d1-b3` :** The target `end` is in the next recurring interval but the target `start` doesn't cross boundary. It doesn't break `rule 5`.
  * **`d1`to`d1-b4` :** The target `start` is on the boundary and the target `end` is in the next recurring interval. Since a recurring interval is left-inclusive and right-exclusive, it breaks `rule 5`.
  * **`d1`to`d1-b5` :** Both the target `start` and `end` are in the next recurring interval. It breaks `rule 5`.


The lower part is backward boundary cases:
  * **`d2`to`d2-b1` :** This update doesn't cross recurring interval. It doesn't break `rule 5`.
  * **`d2`to`d2-b2` :** The target `start` is on the boundary. Since a recurring interval is left-inclusive and right-exclusive, it doesn't break `rule 5`.
  * **`d2`to`d2-b3` :** The target `start` is in the previous recurring interval. It breaks `rule 5`.
  * **`d2`to`d2-b4` :** The target `start` is in the previous recurring interval and the target `end` is on the boundary. It breaks `rule 5`.
  * **`d2`to`d2-b5` :** Both the target `start` and `end` are in the previous recurring interval. It breaks `rule 5`.


![Restrictions On Updating A Meeting - Cross-Day Cases](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltf2234ea604715cd4/60c0056c68689d78c86312c0/Restrictions_On_Updating_A_Meeting-09._Cross-Day_Cases.jpg)
**Fig. 9** Cross-day cases
There're extreme situations where the parent meeting series was scheduled crossing-day. Fig.9 illustrates a daily meeting series of which the `start` is in some day while the `end` is in the next day. `d2`, `d3` and `d4` are successive scheduled meetings of the series. Here're the recurring intervals of `d3` and `d4`:
  * **Recurring interval of`d3` :** From `2021-04-20T00:00:00+08:00` (inclusive) to `2021-04-21T00:00:00+08:00` (exclusive).
  * **Recurring interval of`d4` :** From `2021-04-21T00:00:00+08:00` (inclusive) to `2021-04-22T00:00:00+08:00` (exclusive).


The following updates break `rule 5`:
  * **`d3`to`d3-01` :** The target `start` is in the previous recurring interval. It breaks `rule 5`.
  * **`d3`to`d3-02` :** Same as above.
  * **`d3`to`d3-03` :** Same as above.
  * **`d3`to`d3-10` :** The target `start` is in the next recurring interval. It breaks `rule 5`.
  * **`d3`to`d3-11` :** Same as above.


###### Restrictions table
To summarize, the restrictions on updating a meeting of different types are listed in the table below:  
| Meeting type  | Restrictions on updating meeting of this type  |  
| --- | --- |  
| Meeting series  | Rule 1, 2, 3  |  
| Scheduled meeting  | Rule 1, 2, 3, 5  |  
| Meeting  | Rule 4  |  
##### In This Article
  * [Webex Meetings](https://developer.webex.com/meeting/docs/meetings#webex-meetings)
  * [Creating and Using Webex Apps](https://developer.webex.com/meeting/docs/meetings#creating-and-using-webex-apps)
  * [Meetings API Scopes](https://developer.webex.com/meeting/docs/meetings#meetings-api-scopes)
  * [User Level Authentication and Scopes](https://developer.webex.com/meeting/docs/meetings#user-level-authentication-and-scopes)
  * [Admin/Organization Level Authentication and Scopes](https://developer.webex.com/meeting/docs/meetings#adminorganization-level-authentication-and-scopes)
  * [Group Level Authentication and Scopes](https://developer.webex.com/meeting/docs/meetings#group-level-authentication-and-scopes)
  * [Compliance Officer Level Authentication and Scopes](https://developer.webex.com/meeting/docs/meetings#compliance-officer-level-authentication-and-scopes)
  * [Scopes and User Roles](https://developer.webex.com/meeting/docs/meetings#scopes-and-user-roles)
  * [Meeting Series, Scheduled Meetings, and Meeting Instances](https://developer.webex.com/meeting/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances)
  * [Meeting States](https://developer.webex.com/meeting/docs/meetings#meeting-states)
  * [Available Meeting Attributes for Different Meeting States](https://developer.webex.com/meeting/docs/meetings#available-meeting-attributes-for-different-meeting-states)
  * [Meeting Lifecycle](https://developer.webex.com/meeting/docs/meetings#meeting-lifecycle)
  * [Meeting Template Locales](https://developer.webex.com/meeting/docs/meetings#meeting-template-locales)
  * [Warnings](https://developer.webex.com/meeting/docs/meetings#warnings)
  * [Restrictions on Updating a Meeting](https://developer.webex.com/meeting/docs/meetings#restrictions-on-updating-a-meeting)


##### Related Resources
  * [Webex Meetings Postman Collection](https://github.com/webex/postman-webex-meetings "Webex Meetings Postman Collection")


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


---
# ORIGEN: https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html

  * [Skip to main content](https://www.cisco.com/site/us/en/partners/tools-training/index.html#fw-c-content)
  * [Skip to search](https://www.cisco.com/site/us/en/partners/tools-training/index.html#fw-c-header__button--search)
  * [Skip to footer](https://www.cisco.com/site/us/en/partners/tools-training/index.html#fw-c-footer)


[ Cisco.com Worldwide ](https://www.cisco.com "Cisco.com Worldwide")
###  Products and Services
Back
Products and Services
Close
[ Products and Services Home](https://www.cisco.com/site/us/en/products/index.html)
###  Explore a better Wi-Fi 
Deliver fast, secure connectivity across every space. Simplify management and build an AI-ready network designed for growing demands. 
[Get started today](https://www.cisco.com/site/us/en/products/networking/wireless/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/wireless-hub-nav-284x164.jpg)
###  Cisco Security free trials 
Get started with the right security solution for you. Try out our security solutions before you buy them.
[Start a free trial](https://www.cisco.com/site/us/en/products/security/trials-offers.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/security-default-offer-card.jpg)
###  Discover Cisco IQ 
See more, move faster, go farther. Human expertise meets agentic intelligence in every Cisco Services engagement.
[Read the blog](https://blogs.cisco.com/news/cisco-iq-is-generally-available-heres-what-that-actually-means)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-cisco-iq.jpg)
  1. Networking
  2. Security
  3. Collaboration
  4. Computing
  5. Observability
  6. Software
  7. Services (CX)


Back
Networking
Close
## Products
  * [Switches](https://www.cisco.com/site/us/en/products/networking/switches/index.html)
  * [Routers](https://www.cisco.com/site/us/en/products/networking/sdwan-routers/index.html)
  * [Wireless](https://www.cisco.com/site/us/en/products/networking/wireless/index.html)
  * [Optics and transceivers](https://www.cisco.com/site/us/en/products/networking/optics-transceiver-modules/index.html)
  * [Silicon](https://www.cisco.com/site/us/en/products/networking/silicon-one/index.html)
  * [Networking software](https://www.cisco.com/site/us/en/products/networking/software/index.html)


[ Explore Networking](https://www.cisco.com/site/us/en/products/networking/index.html)
* * *
## Use cases
  * [Access networking](https://www.cisco.com/site/us/en/products/networking/access-networking/index.html)
  * [Campus and branch networking](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
  * [Data center and cloud networking](https://www.cisco.com/site/us/en/products/networking/cloud-networking/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/products/networking/industrial-iot/index.html)
  * [Internet, cloud, and endpoint visibility](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)
  * [Network security](https://www.cisco.com/site/us/en/products/networking/network-security/index.html)
  * [Service provider networking](https://www.cisco.com/site/us/en/solutions/service-provider/index.html)
  * [Wide-area networking (WAN)](https://www.cisco.com/site/us/en/products/networking/sdwan-routers/index.html)


* * *
###  Unified network management 
Manage your entire network from a single, intuitive cloud interface with the Meraki and Catalyst Center Global Overview. 
[Explore Networking Platform](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/products-services-networking.jpg)
Back
Security
Close
## Featured products
  * [AI Defense](https://www.cisco.com/site/us/en/products/security/ai-defense/index.html)
  * [Cisco Duo](https://duo.com/?utm_source=cisco&utm_medium=referral)
  * [Email Threat Defense](https://www.cisco.com/site/us/en/products/security/secure-email/index.html)
  * [Firewall](https://www.cisco.com/site/us/en/products/security/firewalls/index.html)
  * [Hypershield](https://www.cisco.com/site/us/en/products/security/hypershield/index.html)
  * [Identity Services Engine (ISE)](https://www.cisco.com/site/us/en/products/security/identity-services-engine/index.html)
  * [Secure Access (SSE)](https://www.cisco.com/site/us/en/products/security/secure-access/index.html)
  * [Splunk Enterprise Security](https://www.splunk.com/en_us/products/enterprise-security.html)
  * [XDR](https://www.cisco.com/site/us/en/products/security/xdr/index.html)


[ Explore Security](https://www.cisco.com/site/us/en/products/security/index.html)
* * *
## Use cases
  * [Agentic SOC](https://www.splunk.com/en_us/products/cyber-security.html)
  * [AI Security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [Hybrid Mesh Firewall](https://www.cisco.com/site/us/en/solutions/security/hybrid-mesh-firewall/index.html)
  * [Industrial security](https://www.cisco.com/site/us/en/products/security/industrial-security/index.html)
  * [Physical security](https://www.cisco.com/site/us/en/products/security/physical-security/index.html)
  * [Secure Access Service Edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Threat intelligence (Talos)](https://www.cisco.com/site/us/en/products/security/talos/index.html)
  * [Zero Trust Access](https://www.cisco.com/site/us/en/solutions/security/zero-trust-access/index.html)
  * [Zero trust for agentic AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/securing-agentic-ai/index.html)


* * *
###  Cisco Secure Access live demo 
Join us live to experience Cisco Secure Access—the smarter way to secure access to the internet, SaaS, and private apps.
[Choose an upcoming slot](https://www.cisco.com/c/en/us/products/security/secure-access/live-demo.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/security-secure-access-demo.jpg)
Back
Collaboration
Close
## Products
  * [Phones, headsets, and collaboration devices](https://www.cisco.com/c/en/us/products/collaboration-endpoints/index.html)
  * [Webex Customer Experience](https://www.webex.com/customer-experience)
  * [Webex Suite](https://www.webex.com/suite/collaboration-suite.html)


[ Explore Collaboration](https://www.cisco.com/site/us/en/products/collaboration/index.html)
* * *
## Use cases
  * [Workspaces](https://www.webex.com/us/en/workspaces.html)
  * [Return to the office](https://www.webex.com/us/en/solutions/return-to-office.html)
  * [Camera intelligence](https://www.webex.com/us/en/solutions/camera-intelligence-cisco-devices.html)
  * [Workspace management](https://www.webex.com/us/en/solutions/control-hub-cisco-devices.html)
  * [Devices for Microsoft Teams](https://www.webex.com/us/en/solutions/microsoft-teams-rooms-cisco-devices.html)
  * [Webex AI](https://www.webex.ai/)
  * [Control Hub](https://www.webex.com/us/en/solutions/cross-platform/control-hub.html)


###  Webex Suite 
Everything your business needs to collaborate—in the world’s first unified, purpose-built suite for hybrid work.
[Explore Webex Suite](https://www.webex.com/suite/collaboration-suite.html) [View the Webex site](https://www.webex.com/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/webex.jpg)
Back
Computing
Close
  * [Converged infrastructure](https://www.cisco.com/site/us/en/solutions/computing/converged-infrastructure/index.html)
  * [Fabric and adapters](https://www.cisco.com/site/us/en/products/computing/servers-unified-computing-systems/fabric-interconnects-extenders/index.html)
  * [Hybrid cloud operations](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)
  * [Hyperconverged infrastructure](https://www.cisco.com/site/us/en/products/computing/hyperconverged/nutanix/index.html)
  * [Servers](https://www.cisco.com/site/us/en/products/computing/servers-unified-computing-systems/index.html)
  * [Stack Automation by Quali](https://www.cisco.com/site/us/en/solutions/data-center/stack-automation-quali/index.html)
  * [Unified Edge](https://www.cisco.com/site/us/en/products/computing/unified-edge/index.html)


[ View all computing products](https://www.cisco.com/site/us/en/products/computing/index.html)
* * *
###  Cisco Intersight free trial 
Get simplified IT operations with infrastructure lifecycle management as a service to easily manage your Cisco UCS, converged, and hyperconverged infrastructure.
[Get started](https://www.cisco.com/c/en/us/solutions/cloud-computing/promotions-free-trials/intersight-free-trial.html) [Learn more about Intersight](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/computing-intersight.jpg)
Back
Observability
Close
## Products
  * [Cloud application security](https://www.cisco.com/site/us/en/products/security/cloud-application-security/index.html)
  * [Splunk Observability Cloud](https://www.splunk.com/en_us/products/observability-cloud.html)
  * [Splunk IT Service Intelligence](https://www.splunk.com/en_us/products/it-service-intelligence.html)
  * [ThousandEyes](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)


[ Explore Observability](https://www.cisco.com/site/us/en/products/observability/index.html)
* * *
## Use cases
  * [Alert noise reduction](https://www.splunk.com/en_us/solutions/alert-noise-reduction.html)
  * [Cloud monitoring optimization](https://www.splunk.com/en_us/solutions/extend-visibility-to-the-cloud.html)
  * [End-user experiences](https://www.splunk.com/en_us/solutions/optimize-your-web-and-mobile-experience.html)
  * [Microservices troubleshooting](https://www.splunk.com/en_us/solutions/isolate-cloud-native-problems.html)


###  Splunk Observability 
Get complete business visibility and real-time troubleshooting across any environment. 
[Explore Splunk Observability](https://www.splunk.com/en_us/products/observability.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/application-performance-appdynamics.jpg)
Back
Software
Close
## Networking
  * [Catalyst Center](https://www.cisco.com/site/us/en/products/networking/catalyst-center/index.html)
  * [Catalyst SD-WAN Manager](https://www.cisco.com/site/us/en/products/networking/wan/sd-wan-manager/index.html)
  * [IoT Operations Dashboard](https://www.cisco.com/c/en/us/support/cloud-systems-management/iot-operations-dashboard/series.html)
  * [Meraki Platform](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
  * [Mobility Services Platform](https://www.cisco.com/site/us/en/solutions/service-provider/networking/mobility-services-platform/index.html)
  * [Nexus Dashboard](https://www.cisco.com/site/us/en/products/networking/cloud-networking/nexus-platform/index.html)
  * [All networking software](https://www.cisco.com/site/us/en/products/networking/software/index.html)


* * *
## Security
  * [Cyber Vision](https://www.cisco.com/site/us/en/products/security/industrial-security/cyber-vision/index.html)
  * [Secure Equipment Access](https://www.cisco.com/site/us/en/products/security/industrial-security/secure-equipment-access/index.html)
  * [Security Cloud](https://www.cisco.com/site/us/en/products/security/security-cloud/index.html)


* * *
## Observability
  * [Splunk Observability](https://www.splunk.com/en_us/products/observability.html)
  * [ThousandEyes](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)


* * *
## Collaboration
  * [Webex by Cisco](https://www.webex.com)


## Computing
  * [Intersight](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)


* * *
  * [Explore Cisco buying programs](https://www.cisco.com/site/us/en/buy/enterprise-software-buying-program.html)
  * [Download software and manage licenses](https://software.cisco.com/)


[ View all software](https://www.cisco.com/site/us/en/products/software/index.html?filters=&search=&sort=a-z&filterby=&showMore=)
* * *
###  Free trials and demos 
View and sign up for over 100 products and portfolio solutions for free. 
[Explore trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/products-software-trials-demos.jpg)
Back
Services (CX)
Close
  * [Cisco Support](https://www.cisco.com/site/us/en/services/support/index.html)
  * [Cisco Professional Services](https://www.cisco.com/site/us/en/services/professional/index.html)
  * [Learn with Cisco](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


[ View all Cisco services](https://www.cisco.com/site/us/en/services/index.html)
* * *
###  Discover Cisco IQ 
See more, move faster, go farther. Human expertise meets agentic intelligence in every Cisco Services engagement.
[Read the blog](https://blogs.cisco.com/news/cisco-iq-is-generally-available-heres-what-that-actually-means)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-cisco-iq.jpg)
###  Get expert guidance 
Cisco Services can help you build the right solution for your needs with the combined power of AI, automation, and human expertise.
[Transform your data center](https://www.cisco.com/site/us/en/services/modern-data-center/index.html) [Build a better workplace](https://www.cisco.com/site/us/en/services/future-workplace/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-promo-expert-guidance.jpg)
Close
###  Solutions
Back
Solutions
Close
[ Solutions Home](https://www.cisco.com/site/us/en/solutions/index.html)
###  Artificial intelligence 
Cisco has the infrastructure to power AI, unmatched breadth and scale of data to feed it, and a portfolio optimized to secure it. 
[Explore Cisco AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-ai.jpg)
###  Campus and branch 
Cisco brings together Al, automation, and security into one unified architecture—built to simplify operations, scale intelligently, and protect every connection.  

[Explore campus and branch](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-campus-branch.jpg)
###  Small and medium business 
Protect, connect, and empower your business with Cisco’s portfolio tailored to small and medium businesses. Experience simplified IT management, efficiency, cloud-driven flexibility, and 24/7 support. 
[Explore SMB solutions](https://www.cisco.com/site/us/en/solutions/small-business/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-smb.jpg)
  1. Artificial Intelligence
  2. Industries
  3. Technologies
  4. Campus and Branch
  5. Service Providers
  6. Small and Medium Business


Back
Artificial Intelligence
Close
  * [AI-enhanced security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [AI-native networking operations](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/netops.html)
  * [AI-ready data centers](https://www.cisco.com/site/us/en/about/why-cisco/ai-ready-data-centers/index.html)
  * [AI at the edge](https://www.cisco.com/site/us/en/solutions/data-center/ai-at-the-edge/index.html)
  * [AI networking in data centers](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/ai-networking-in-data-center/index.html)
  * [Mass-scale AI infrastructure](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/mass-scale-infrastructure/index.html)
  * [Secure AI Factory](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/secure-ai-factory/index.html)
  * [Splunk AI](https://www.splunk.com/en_us/solutions/splunk-artificial-intelligence.html)
  * [Webex AI](https://www.webex.ai/)


[ Cisco AI hub](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/index.html)
###  Cisco AI Assistant 
Cisco AI Assistant combines the latest generative AI technology with our expertise to responsibly guide and inform the decisions you make every day.
[Explore Cisco AI Assistant](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/ai-assistant/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/ai-assistant.jpg)
###  Cisco AI Readiness Assessment 
AI readiness comprises six pillars: Strategy, Infrastructure, Data, Governance, Talent, and Culture. Is your organization AI ready?
[Take assessment](https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index/assessment-tool.html) [Browse AI Readiness Index](https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/ai-readiness.jpg)
Back
Industries
Close
  * [Cities and Communities](https://www.cisco.com/c/en/us/solutions/industries/smart-connected-communities.html)
  * [Education](https://www.cisco.com/site/us/en/solutions/industries/education/index.html)
  * [Financial Services](https://www.cisco.com/site/us/en/solutions/industries/financial-services/index.html)
  * [Government](https://www.cisco.com/site/us/en/solutions/industries/government/index.html)
  * [Healthcare](https://www.cisco.com/site/us/en/solutions/industries/healthcare/index.html)
  * [Manufacturing](https://www.cisco.com/site/us/en/solutions/industries/manufacturing/index.html)
  * [Mining](https://www.cisco.com/site/us/en/solutions/industries/mining/index.html)


* * *
  * [Oil and Gas](https://www.cisco.com/site/us/en/solutions/industries/energy/oil-gas/index.html)
  * [Retail](https://www.cisco.com/site/us/en/solutions/industries/retail/index.html)
  * [Smart Buildings](https://www.cisco.com/site/us/en/solutions/smart-building/index.html)
  * [Sports, Media, and Entertainment](https://www.cisco.com/site/us/en/solutions/industries/sports-media-entertainment/index.html)
  * [Transportation](https://www.cisco.com/site/us/en/solutions/industries/transportation/index.html)
  * [Utilities](https://www.cisco.com/site/us/en/solutions/industries/energy/utilities/index.html)


[ View all industries](https://www.cisco.com/c/en/us/solutions/industries.html)
[ Industry design guides](https://www.cisco.com/c/en/us/solutions/design-zone/industries.html)
* * *
###  Discover the portfolio explorer 
Build the bridge between business outcomes and technology with our new interactive tool.
[Start exploring](https://www.cisco.com/c/m/en_us/solutions/industries/portfolio-explorer.html)
Back
Technologies
Close
## Networking
  * [Cloud and data center networking](https://www.cisco.com/site/us/en/products/networking/cloud-networking/index.html)
  * [Cloud-managed networking (Meraki)](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/index.html)
  * [Networking App Marketplace](https://marketplace.cisco.com/en-US/home)
  * [SD-WAN](https://www.cisco.com/site/us/en/solutions/networking/sdwan/index.html)
  * [Smart buildings](https://www.cisco.com/site/us/en/solutions/smart-building/index.html)
  * [All networking solutions](https://www.cisco.com/c/en/us/solutions/enterprise-networks/solution-listing.html)


## Computing
  * [Converged infrastructure](https://www.cisco.com/site/us/en/solutions/computing/converged-infrastructure/index.html)
  * [Hybrid cloud](https://www.cisco.com/site/us/en/solutions/computing/hybrid-cloud/index.html)
  * [Hyperconverged](https://www.cisco.com/site/us/en/products/computing/hyperconverged/nutanix/index.html)
  * [Stack Automation by Quali](https://www.cisco.com/site/us/en/solutions/data-center/stack-automation-quali/index.html)


* * *
## Security
  * [AI for security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [Data center security](https://www.cisco.com/site/us/en/solutions/security/data-center-security/index.html)
  * [Hybrid Mesh Firewall](https://www.cisco.com/site/us/en/solutions/security/hybrid-mesh-firewall/index.html)
  * [Industrial security](https://www.cisco.com/site/us/en/products/security/industrial-security/index.html)
  * [Network security](https://www.cisco.com/site/us/en/products/networking/network-security/index.html)
  * [Secure Access Service Edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Secure Hybrid Work](https://www.cisco.com/site/us/en/solutions/security/secure-hybrid-work/index.html)
  * [Zero trust](https://www.cisco.com/site/us/en/solutions/security/zero-trust/index.html)
  * [Zero trust for agentic AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/securing-agentic-ai/index.html)


* * *
## Collaboration (Webex)
  * [Camera intelligence](https://www.webex.com/us/en/solutions/camera-intelligence-cisco-devices.html)
  * [Customer experience](https://www.webex.com/us/en/products/customer-experience.html)
  * [Event management](https://www.webex.com/us/en/products/suite/events.html)
  * [Intelligent workspaces](https://www.webex.com/us/en/workspaces.html)
  * [Interoperability](https://www.webex.com/us/en/solutions/interoperability.html)
  * [IT administration](https://www.webex.com/us/en/solutions/cross-platform/control-hub.html)
  * [Remote work](https://www.webex.com/suite/collaboration-suite.html)
  * [Workspace designer](https://designer.webex.com/)
  * [Workspace management](https://www.webex.com/us/en/solutions/control-hub-cisco-devices.html)


Back
Campus and Branch
Close
  * [Secure network architecture](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
  * [Secure campus](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/secure-campus/index.html)
  * [Unified branch](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/unified-branch/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/index.html)
  * [Campus and branch design guides](https://www.cisco.com/c/en/us/solutions/design-zone/campus-branch.html)


* * *
Back
Service Providers
Close
## Empowering your infrastructure
  * [5G network architecture](https://www.cisco.com/c/en/us/solutions/service-provider/5g-network-architecture.html)
  * [Agile Services Networking](https://www.cisco.com/site/us/en/solutions/service-provider/networking/agile-services/index.html)
  * [Broadband solutions](https://www.cisco.com/site/us/en/solutions/service-provider/networking/broadband/index.html)
  * [Cable solutions](https://www.cisco.com/site/us/en/solutions/service-provider/industry/cable/index.html)
  * [Routed optical networking](https://www.cisco.com/site/us/en/solutions/routed-optical-networking/index.html)
  * [Routed PON](https://www.cisco.com/site/us/en/solutions/routed-pon/index.html)


[ View all service provider solutions](https://www.cisco.com/site/us/en/solutions/service-provider/index.html)
* * *
## Managed services
  * [Edge Cloud for Content Delivery](https://www.cisco.com/c/en/us/solutions/service-provider/telco-cloud/edge-cloud-for-content-delivery.html)
  * [IoT Control Center](https://www.cisco.com/site/us/en/products/networking/software/iot-control-center/index.html)
  * [Mobility Services Platform](https://www.cisco.com/site/us/en/solutions/service-provider/networking/mobility-services-platform/index.html)
  * [Private 5G](https://www.cisco.com/site/us/en/products/networking/wireless/private-5g/index.html)
  * [Secure access service edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Software-defined access](https://www.cisco.com/site/us/en/solutions/networking/sdaccess/index.html)
  * [Secure Hybrid Work](https://www.cisco.com/site/us/en/solutions/security/secure-hybrid-work/index.html)
  * [SD-WAN security](https://www.cisco.com/site/us/en/solutions/networking/sdwan/security/index.html)


* * *
###  Accelerate services offerings 
Provide outsourced IT and consulting services with a broad technology portfolio and robust partner support programs.
[See services options](https://www.cisco.com/site/us/en/partners/build-your-practice/managed-services/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/managed-services.jpg)
Back
Small and Medium Business
Close
## Products and solutions
  * [Networking](https://www.cisco.com/site/us/en/solutions/small-business/networking/index.html)
  * [Security](https://www.cisco.com/site/us/en/solutions/small-business/security/index.html)
  * [Collaboration](https://www.cisco.com/site/us/en/solutions/small-business/collaboration/index.html)
  * [Product selector](https://www.cisco.com/c/en/us/solutions/small-business/selector-tool.html)


[ View all small and medium business solutions](https://www.cisco.com/site/us/en/solutions/small-business/index.html)
[ Buy small and medium business products online](https://www.cisco.com/c/en/us/solutions/small-business/small-business-promotions-and-free-trials/buy-cisco-small-business-products-online.html)
* * *
###  Offers and free trials 
Find the best solutions for your needs and try them before you buy. 
[See all offers and free trials](https://www.cisco.com/site/us/en/solutions/small-business/trials-offers.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/smb-free-trials.jpg)
Close
###  Support
Back
Support
Close
[ Support Home](https://www.cisco.com/c/en/us/support/index.html)
###  Support home 
Access documentation, security notices, and support tools for Cisco products.
[View Cisco Support](https://www.cisco.com/c/en/us/support/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-home-penn1_brandlibrary-DSC0318.jpg)
###  Software downloads 
Download and manage new software, get updates or patches, or upgrade your current software to the latest release.
[View Software Central](https://software.cisco.com/download/home)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-software-downloads-hatchlibrary-general-gettyPA-Cisco-1309760275.jpg)
###  Licensing support 
Troubleshoot common licensing issues and leverage easy-to-follow documentation for both PAK-based or Smart Licenses.
[Get licensing support](https://www.cisco.com/c/en/us/support/licensing/licensing-support.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-licensing-hatchlibrary-security-gettyPA-Cisco-1518851638.jpg)
  1. Products and Downloads
  2. Documentation
  3. Contact Support
  4. Licenses and Contracts
  5. Tools and Resources
  6. Cisco Community


Back
Products and Downloads
Close
## Find products and downloads
Search field edit, type in text
Clear
[Downloads](https://www.cisco.com/site/us/en/partners/tools-training/index.html#tabs-69d6a56dd3-item-fdd67b2fb8-tab) [Product Support](https://www.cisco.com/site/us/en/partners/tools-training/index.html#tabs-69d6a56dd3-item-fdd67b2fb8-tab) [Technology Support](https://www.cisco.com/site/us/en/partners/tools-training/index.html#tabs-69d6a56dd3-item-fdd67b2fb8-tab) | End of Sale End of Support
* [All Downloads](https://software.cisco.com/download/navigator.html)
* [All Products](https://www.cisco.com/c/en/us/support/all-products.html)
* Search all cisco.com
When autocomplete results are available use up and down arrows to review and enter to select
## Product Support
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Security](https://www.cisco.com/c/en/us/support/security/category.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Wireless](https://www.cisco.com/c/en/us/support/wireless/category.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Collaboration endpoints and phones](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Networking software (IOS and NX-OS)](https://www.cisco.com/c/en/us/support/ios-nx-os-software/index.html)
  * [Servers - Unified Computing (UCS)](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)


[ All products](https://www.cisco.com/c/en/us/support/all-products.html)
* * *
## Downloads
  * [Secure Client 5](https://software.cisco.com/download/home/286330811/type/282364313/release/)
  * [Identity Services Engine Software](https://software.cisco.com/download/home/283801620/type/283802505/)
  * [Secure Firewall Management Center Virtual](https://software.cisco.com/download/home/286259687/type)
  * [Smart Software Manager](https://software.cisco.com/download/home/286285506/type)
  * [Jabber for Windows](https://software.cisco.com/download/home/284324806/type/284006014/release/)
  * [Modeling Labs](https://software.cisco.com/download/home/286193282/type/286326381/release/2.7.2)
  * [Catalyst 9300 Series Switches](https://software.cisco.com/download/home/286313806)


[ All downloads](https://software.cisco.com/download/home)
* * *
Back
Documentation
Close
[ Technical documentation](https://www.cisco.com/c/en/us/docs/technical-documentation.html)
Configure, operate, and troubleshoot your Cisco products with configuration guides, installation guides, release notes, and more.
[ Trust Portal](https://trustportal.cisco.com/c/r/ctp/home.html)
Get self-service access to security, data privacy, and compliance documents.
* * *
[ Product documentation](https://www.cisco.com/c/en/us/products/a-to-z-series-index.html#all)
Explore Cisco products and features to empower your purchase with data sheets, white papers, end-of-life notices, and more.
* * *
Back
Contact Support
Close
## Product technical support (TAC)
[ Open a new case](https://mycase.cloudapps.cisco.com/case)
(Requires a product or software support contract)
  * [Manage support cases](https://mycase.cloudapps.cisco.com/case)
  * [Returns Portal (RMAs)](https://www.cisco.com/c/en/us/support/returns/returns-portal.html)


* * *
Enterprise and Service Provider products
**1-800-553-2447** US and Canada
[ Worldwide phone numbers](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)
* * *
Small and medium business products
**1-866-606-1866** US and Canada
[ Worldwide phone numbers](https://www.cisco.com/c/en/us/support/web/tsd-cisco-small-business-support-center-contacts.html)
Back
Licenses and Contracts
Close
## Software licenses
  * [Explore key licensing resources](https://www.cisco.com/site/us/en/buy/licensing/index.html)
  * [Download and manage licenses](https://software.cisco.com/)
  * [Manage assets and entitlements](https://software.cisco.com/clc/access-directory)
  * [Troubleshoot license issues](https://www.cisco.com/c/en/us/support/licensing/licensing-support.html)


## Cisco Enterprise Agreement (EA)
  * [Manage Cisco EA licenses](https://software.cisco.com/software/ea/agreements)
  * [Learn about Cisco EA](https://www.cisco.com/site/us/en/buy/enterprise-agreement/index.html)


* * *
## Product support contracts
  * [Manage and renew service contracts (CCW-R)](https://ccrc.cisco.com/ccwr/)


###  Cisco Licensing Hub 
Enhance your Cisco licensing experience. 
[Access now](https://www.cisco.com/site/us/en/buy/licensing/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-licensing-hub.jpg)
Back
Tools and Resources
Close
## Tools
  * [Bug Search Tool](https://bst.cisco.com/bugsearch/?referring_site=shp)
  * [My Devices](https://cway.cisco.com/mydevices)
  * [My Saved Content](https://www.cisco.com/c/en/us/support/saved/index.html)
  * [Software Research](https://software.cisco.com/research/home)
  * [Device Coverage Checker](https://cway.cisco.com/sncheck/)


[ All Support tools](https://www.cisco.com/c/en/us/support/web/tools-catalog.html)
* * *
## Notifications and advisories
  * [My Notifications](https://cway.cisco.com/mynotifications)
  * [Security Advisories](https://sec.cloudapps.cisco.com/security/center/publicationListing.x)
  * [Field Notices](https://www.cisco.com/c/en/us/support/web/tsd-products-field-notice-summary.html)
  * [Cisco Cloud Status](https://www.cisco.com/c/en/us/support/web/cloud-status.html)


### Services
  * [All Cisco Services](https://www.cisco.com/site/us/en/services/index.html)


## Technology adoption
  * [Cisco Customer Success](https://www.cisco.com/c/m/en_us/customer-experience/customer-success/index.html)


Back
Cisco Community
Close
## Community forums
  * [Technology and Support](https://community.cisco.com/t5/technology-and-support/ct-p/technology-support)
  * [Small Business Support](https://community.cisco.com/t5/small-business-support-community/ct-p/5541-small-business-support)
  * [Developers](https://community.cisco.com/t5/devnet/ct-p/4409j-developer-home)
  * [Partners](https://community.cisco.com/t5/partner-hub/ct-p/2002j-partner-home)
  * [Project Gallery](https://community.cisco.com/t5/project-gallery/con-p/customer-success-stories)
  * [Cisco Insider User Group](https://community.cisco.com/t5/cisco-insider-user-group/ct-p/ccp-home)


[ Explore Cisco Community](https://community.cisco.com/)
* * *
###  Community events and webinars 
Learn from Cisco experts and engage with peers in webinars and live events.
[View all events and webinars](https://community.cisco.com/t5/technology-and-support-events-and-webinars/eb-p/ts-events-webinars-bd)
Close
###  Learn
Back
Learn
Close
[ Learn Home](https://www.cisco.com/site/us/en/learn/index.html)
###  Cisco U. 
Access training tailored to your needs. Work toward a specific role or certification, deploy or support a technology solution, or enhance your career progress.
[Learn more about Cisco U. ](https://www.cisco.com/site/us/en/learn/training-certifications/training/ciscou/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-cisco-u.jpg)
###  Cisco Networking Academy 
If you're a student, start at Cisco Networking Academy. With free courses and career guidance, your next IT job is closer than you think.
[Join now](https://www.netacad.com/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-netacad.jpg)
###  Events 
Join us to take advantage of the latest networking opportunities with Cisco customers, partners, employees, and subject-matter experts.
[Explore now](https://www.cisco.com/site/us/en/learn/events/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/events-calendar-default.jpg)
  1. Training and Certifications
  2. Events
  3. Webinars
  4. Technology Learning Topics
  5. Learning Resources and Assets


Back
Training and Certifications
Close
## Learning
  * [Cisco Networking Academy](https://www.netacad.com)
  * [Cisco U. ](https://u.cisco.com)
  * [Instructor-led training](https://learninglocator.cloudapps.cisco.com/#/home)
  * [Cisco Modeling Labs](https://www.cisco.com/site/us/en/learn/training-certifications/training/modeling-labs/index.html)
  * [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer)
  * [Join our community](https://learningnetwork.cisco.com/s/)
  * [Learn with Cisco blog](https://blogs.cisco.com/learning)


[ Learn with Cisco overview](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)
* * *
## Certifications
  * [Career certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
  * [Learn about exams](https://www.cisco.com/site/us/en/learn/training-certifications/exams/index.html)
  * [Continuing Education (CE credits)](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/continuing-education/index.html)
  * [Recertification](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/recertification/index.html)
  * [Schedule an exam](https://cp.certmetrics.com/cisco/en/schedule/schedule-exam)
  * [Track my certifications](https://cp.certmetrics.com/cisco/en/credentials/status)


* * *
## Training for organizations
  * [Enterprise](https://www.cisco.com/site/us/en/learn/training-certifications/enterprise-training/index.html)
  * [Cisco Learning Credits](https://www.cisco.com/site/us/en/learn/training-certifications/training/learning-credits/index.html)
  * [Training catalog](https://www.cisco.com/site/us/en/learn/training-certifications/training/training-catalog/index.html)
  * [Partners](https://www.cisco.com/site/us/en/learn/training-certifications/partner-resources.html)


## Support
  * [Learn with Cisco support bot](https://certsupport.cisco.com/s/?language=en_US)


Back
Events
Close
  * [Cisco Live](https://www.ciscolive.com/home/en/index.html?cid=cdc-hp-nav-home#xd_co_f)
  * [Partner events calendar](https://salesconnect.cisco.com/americaspartnercommunity/s/enablement-training-calendar)


[ View all events](https://www.cisco.com/site/us/en/learn/events/index.html)
* * *
###  Cisco Live 2026 Melbourne 
Experience the education, inspiration, and fun of Cisco Live 2026 Melbourne.
[Register now](https://www.ciscolive.com/apjc?ccid=cc008775&cid=CL26eventspage&eid=162820&oid=eprsas033263)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/cl2026-cisco-live-las-vegas.jpg)
###  Watch Cisco Live sessions on demand 
View sessions from Las Vegas in our On-Demand Library. Keynotes, Deep Dives, and Center Stage sessions are available now, with the remaining sessions added by June 19.
[Watch now](https://www.ciscolive.com/on-demand/on-demand-library.html?cid=cdc-hp-nav&utm_team=global_events&utm_medium=email&utm_source=sendgrid&utm_campaign=xb_cxp_fy26q4_amer_20260623past&ccid=cc007720&dtid=oemrft001460&utm_eid=95796&search.event=1769534158486002QYqy#/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/cl2026-cisco-live-las-vegas.jpg)
Back
Webinars
Close
## Trending webinars
  * [AI readiness for data centers](https://experiences.cisco.com/amer/ai-readiness-for-data-centers)
  * [Simplify IT with SD-WAN](https://experiences.cisco.com/amer/simplify-it-with-sd-wan)
  * [Security transformation with Cisco XDR](https://cloudsecurity.cisco.com/webinar-security-transformation-with-cisco-xdr)


[ View all webinars](https://experiences.cisco.com/amer?pf_route=1&groups=all-webinars)
* * *
###  McLaren Racing + Cisco 
Carrie Palin joins McLaren Racing F1 team CEO Zak Brown and driver Oscar Piastri as they unveil the high-tech secrets behind their team's successful 2024 season.
[Watch on demand](https://experiences.cisco.com/amer/cisco-mclaren-innovation-speed)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-webinars-mclaren-racing.jpg)
###  Cisco webinars 
Discover insights that shape the future of technology. Our webinars feature experts and leaders sharing how organizations transform to connect, grow, and succeed.
[Explore webinars](https://experiences.cisco.com/amer?pf_route=1&group=all-webinars&groups=all-webinars)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-webinars.jpg)
Back
Technology Learning Topics
Close
  * [How to set up a router](https://www.cisco.com/site/us/en/learn/topics/small-business/how-to-set-up-router.html)
  * [What is cybersecurity?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-cybersecurity.html)
  * [What is a firewall?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-firewall.html)
  * [What is Industry 4.0?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-industry-4-0.html)
  * [What is IoT (Internet of Things)?](https://www.cisco.com/site/us/en/learn/topics/industrial-iot/what-is-iot.html)
  * [What is Wi-Fi 7?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-wi-fi-7.html)


* * *
  * [What is AIOps?](https://www.cisco.com/site/us/en/learn/topics/artificial-intelligence/what-is-aiops.html)
  * [What is cloud security?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-cloud-security.html)
  * [What is hybrid cloud?](https://www.cisco.com/site/us/en/learn/topics/computing/what-is-hybrid-cloud.html)
  * [What is SASE?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-secure-access-service-edge-sase.html)
  * [What is software as a service (SaaS)?](https://www.cisco.com/site/us/en/learn/topics/software/what-is-software-as-a-service-saas.html)


[ View all technology learning topics](https://www.cisco.com/site/us/en/learn/topics/index.html)
* * *
###  2026 State of Industrial AI 
We surveyed more than 1000 industrial professionals on securing operations, advancing IT/OT collaboration, and building an AI-ready network that can scale.
[Get report](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/industrial-networking-report/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/state-of-industrial-ai-284x164.jpg)
Back
Learning Resources and Assets
Close
## Sandboxes and simulators
  * [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer)
  * [DevNet Sandbox](https://developer.cisco.com/site/sandbox/)
  * [Cisco Modeling Labs](https://developer.cisco.com/modeling-labs/)
  * [Cisco Learning Labs](https://u.cisco.com/store/lab?type=cisco-learning-labs)


## News and insights
  * [Blogs](https://blogs.cisco.com/)
  * [Cisco Community](https://community.cisco.com/)
  * [Executive perspectives](https://www.cisco.com/c/en/us/solutions/executive-perspectives/index.html)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)


* * *
## Developer resources
  * [Getting started with DevNet](https://developer.cisco.com/startnow/)
  * [DevNet Tracks](https://developer.cisco.com/learning/search/?contentType=track&page=1)
  * [Python training](https://www.cisco.com/site/us/en/learn/training-certifications/training/courses/prne.html)
  * [Code exchange](https://developer.cisco.com/codeexchange/)
  * [Developer community](https://community.cisco.com/t5/devnet/ct-p/4409j-developer-home)


## Videos and live streams
  * [Cisco Video Portal](https://video.cisco.com/)


* * *
## Architecture and design resources
  * [Cisco Validated](https://www.cisco.com/site/us/en/solutions/cisco-validated/index.html)
  * [Visio stencils](https://www.cisco.com/c/en/us/products/visio-stencil-listing.html)


## Additional resources
  * [Cisco Learning Credits](https://www.cisco.com/site/us/en/learn/training-certifications/training/learning-credits/index.html)
  * [Cisco Multicloud training](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/multicloud/index.html)
  * [Black Belt Academy (for partners)](https://www.cisco.com/site/us/en/partners/training/black-belt-academy/index.html)


Close
###  Why Cisco
Back
Why Cisco
Close
[ Why Cisco](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
###  Why Cisco 
Cisco creates the infrastructure you need to transform how you connect, protect, and innovate in the AI era.
[See the Cisco advantage](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-ai-blue.jpg)
###  Our Purpose 
We Power an Inclusive Future for All.
[Explore our Purpose](https://www.cisco.com/site/us/en/about/purpose/index.html) [Read FY25 Purpose Report](https://www.cisco.com/c/dam/m/en_us/about/purpose/reporting-hub/_pdf/purpose-report-2025.pdf)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-purpose.jpg)
###  Success stories 
Discover how Cisco technologies drive real-world success for our customers and power Cisco's own operations and innovation. 
[Explore customer stories](https://www.cisco.com/site/us/en/about/case-studies-customer-stories/index.html) [How we use our technology](https://www.cisco.com/site/us/en/solutions/cisco-on-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-success-stories.jpg)
  1. Outcomes We Deliver
  2. Working with Partners
  3. About Us


Back
Outcomes We Deliver
Close
[ AI-ready data centers](https://www.cisco.com/site/us/en/about/why-cisco/ai-ready-data-centers/index.html)
Unleash the power of AI with data centers designed for speed, scale, and agility.
[ Future-proofed workplaces](https://www.cisco.com/site/us/en/about/why-cisco/future-proofed-workplaces/index.html)
Elevate employee and customer experiences with agile, resilient workplaces.
[ Digital resilience](https://www.cisco.com/site/us/en/about/why-cisco/digital-resilience/index.html)
Achieve always-on resilience with trusted security, observability, and assurance.
* * *
###  Why Cisco 
Cisco creates the infrastructure you need to transform how you connect, protect, and innovate in the AI era.
[See the Cisco advantage](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-ai-blue.jpg)
Back
Working with Partners
Close
[ Why choose Cisco partners](https://www.cisco.com/site/us/en/partners/evolved-partner-ecosystem/index.html)
Learn how our partner ecosystem makes it easier than ever to identify the partners to best meet your needs. ​ 
[ Frequently asked questions (PDF)](https://www.cisco.com/c/dam/en_us/partners/cisco-partner-designations-faq.pdf)
Access answers to your questions about the evolution of Cisco's partner ecosystem and new partner designations. 
[ Find a partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
Explore our partner ecosystem today. 
* * *
###  A new way to find partners 
The Cisco Partner Locator tool has been transformed into an AI-driven hub to match, recommend, and activate partners for every customer outcome.​ 
[Explore what's new](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/partner-locator-curve.jpg)
Back
About Us
Close
  * [Overview](https://www.cisco.com/site/us/en/about/index.html)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)
  * [Leadership](https://newsroom.cisco.com/c/r/newsroom/en/us/executives.html)
  * [Purpose and sustainability](https://www.cisco.com/site/us/en/about/purpose/index.html)
  * [Career opportunities](https://careers.cisco.com/global/en/home)
  * [The Trust Center](https://www.cisco.com/c/en/us/about/trust-center.html)
  * [Investor relations](https://investor.cisco.com/overview/default.aspx)


[ Contact us](https://www.cisco.com/site/us/en/about/contact-cisco/index.html)
* * *
###  How to buy 
Browse options to purchase Cisco products, services, and software offerings.
[Visit how-to-buy hub](https://www.cisco.com/site/us/en/buy/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-how-to-buy.jpg)
Close
###  Partners
Close
[ Trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html?linkclickid=hdr-mainnav-trialsdemos)
[ How to buy](https://www.cisco.com/site/us/en/buy/index.html?linkclickid=hdr-utilnav-howtobuy)
Partners
EN US
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/partners/tools-training/index.html)
[ Trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html?linkclickid=hdr-mainnav-trialsdemos)
MENU
CLOSE
[ How to buy](https://www.cisco.com/site/us/en/buy/index.html?linkclickid=hdr-utilnav-howtobuy)
Partners
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/partners/tools-training/index.html)
EN US
Search field edit, type in text
Clear Speech-to-Text Search Search
* * *
Speech-to-Text Powered By Google Speech API
We didn't hear that. Try again.
Speech-to-Text Search is currently unavailable
  * [Downloads](https://software.cisco.com/download/home)
  * [Certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
  * [Cisco Validated](https://www.cisco.com/c/en/us/solutions/cisco-validated.html)
  * [Training](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)
  * [Community](https://community.cisco.com/)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)


Close
**For Partners**
[Partners Home](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129)
[Partner Program](https://www.cisco.com/site/us/en/partners/index.html?ccid=cc000864&dtid=odiprc001129)
[Support](https://www.cisco.com/site/us/en/partners/support-help/index.html?dtid=odiprc001129)
[Tools](https://www.cisco.com/site/us/en/partners/tools-training/index.html?dtid=odiprc001129)
**Already a Partner?**
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/partners/tools-training/index.html)
* * *
[Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/ "Find a Cisco Partner")
* * *
[Learn about Partners](https://www.cisco.com/site/us/en/partners/evolved-partner-ecosystem/index.html)
* * *
[Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129 "Become a Cisco Partner")
Close
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/partners/tools-training/index.html)
Don't have an account? [Sign up](https://id.cisco.com/signin/register "Sign up")
Close
Back
Country | Language
Close
Selected country/region:
United States
  * [English](https://www.cisco.com/site/us/en/index.html)


  1. All Countries / Regions
  2. North America
  3. Africa
  4. Asia Pacific
  5. Europe
  6. Greater China
  7. Latin America
  8. Middle East


  * United States
    * [English](https://www.cisco.com/site/us/en/index.html)
  * Africa
    * [English](https://www.cisco.com/site/dz/en/index.html)
    * [Français](https://www.cisco.com/site/dz/fr/index.html)
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * Argentina
    * [Español](https://www.cisco.com/site/ar/es/index.html)
  * Australia & New Zealand
    * [English](https://www.cisco.com/site/au/en/index.html)
  * Austria
    * [Deutsch](https://www.cisco.com/site/at/de/index.html)
  * Belgium & Luxembourg
    * [English](https://www.cisco.com/site/be/en/index.html)
    * [Français](https://www.cisco.com/site/be/fr/index.html)
    * [Nederlands](https://www.cisco.com/site/be/nl/index.html)
  * Brazil
    * [Português](https://www.cisco.com/site/br/pt/index.html)
  * Canada
    * [English](https://www.cisco.com/site/ca/en/index.html)
    * [Français](https://www.cisco.com/site/ca/fr/index.html)
  * Caribbean
    * [Español](https://www.cisco.com/site/bz/es/index.html)
  * Chile
    * [Español](https://www.cisco.com/site/cl/es/index.html)
  * Colombia
    * [Español](https://www.cisco.com/site/co/es/index.html)
  * Costa Rica
    * [Español](https://www.cisco.com/site/cr/es/index.html)
  * Czech Republic
    * [Čeština](https://www.cisco.com/site/cz/cs/index.html)
  * Denmark
    * [Dansk](https://www.cisco.com/site/dk/da/index.html)
  * Ecuador
    * [Español](https://www.cisco.com/site/ec/es/index.html)
  * Egypt
    * [English](https://www.cisco.com/site/eg/en/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * France
    * [Français](https://www.cisco.com/site/fr/fr/index.html)
  * Germany
    * [Deutsch](https://www.cisco.com/site/de/de/index.html)
  * Hong Kong
    * [English](https://www.cisco.com/site/hk/en/index.html)
    * [繁體中文](https://www.cisco.com/site/hk/zh/index.html)
  * Hungary
    * [Magyar](https://www.cisco.com/site/hu/hu/index.html)
  * India
    * [English](https://www.cisco.com/site/in/en/index.html)
  * Indonesia
    * [English](https://www.cisco.com/site/id/en/index.html)
  * Israel
    * [English](https://www.cisco.com/site/il/en/index.html)
  * Italy
    * [Italiano](https://www.cisco.com/site/it/it/index.html)
  * Japan
    * [日本語](https://www.cisco.com/site/jp/ja/index.html)
  * Korea
    * [한국어](https://www.cisco.com/site/kr/ko/index.html)
  * Mainland China
    * [简体中文](https://www.cisco.com/site/cn/zh/index.html)
  * Malaysia
    * [English](https://www.cisco.com/site/my/en/index.html)
  * Mexico
    * [Español](https://www.cisco.com/site/mx/es/index.html)
  * Middle East
    * [English](https://www.cisco.com/site/ae/en/index.html)
    * [عربي](https://www.cisco.com/site/ae/ar/index.html)
  * Netherlands
    * [Nederlands](https://www.cisco.com/site/nl/nl/index.html)
  * Norway
    * [Norsk](https://www.cisco.com/site/no/no/index.html)
  * Panama
    * [Español](https://www.cisco.com/site/pa/es/index.html)
  * Peru
    * [Español](https://www.cisco.com/site/pe/es/index.html)
  * Philippines
    * [English](https://www.cisco.com/site/ph/en/index.html)
  * Poland
    * [Polski](https://www.cisco.com/site/pl/pl/index.html)
  * Portugal
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
  * Romania
    * [Română](https://www.cisco.com/site/ro/ro/index.html)
  * Singapore
    * [English](https://www.cisco.com/site/sg/en/index.html)
  * South Africa
    * [English](https://www.cisco.com/site/za/en/index.html)
  * Spain
    * [Español](https://www.cisco.com/site/es/es/index.html)
  * Sweden
    * [Svenska](https://www.cisco.com/site/se/sv/index.html)
  * Switzerland
    * [Français](https://www.cisco.com/site/ch/fr/index.html)
    * [Deutsch](https://www.cisco.com/site/ch/de/index.html)
  * Taiwan
    * [繁體中文](https://www.cisco.com/site/tw/zh/index.html)
  * Thailand
    * [ภาษาไทย](https://www.cisco.com/site/th/th/index.html)
  * Turkey
    * [Türkçe](https://www.cisco.com/site/tr/tr/index.html)
  * Ukraine
    * [Українська ](https://www.cisco.com/site/ua/uk/index.html)
    * [Русский](https://www.cisco.com/site/ua/ru/index.html)
  * United Kingdom & Ireland
    * [English](https://www.cisco.com/site/uk/en/index.html)
  * Vietnam
    * [Việt](https://www.cisco.com/site/vn/vi/index.html)


  * Canada
    * [English](https://www.cisco.com/site/ca/en/index.html)
    * [Français](https://www.cisco.com/site/ca/fr/index.html)
  * United States
    * [English](https://www.cisco.com/site/us/en/index.html)


  * Africa
    * [English](https://www.cisco.com/site/dz/en/index.html)
    * [Français](https://www.cisco.com/site/dz/fr/index.html)
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * Egypt
    * [English](https://www.cisco.com/site/eg/en/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * South Africa
    * [English](https://www.cisco.com/site/za/en/index.html)


  * Australia & New Zealand
    * [English](https://www.cisco.com/site/au/en/index.html)
  * India
    * [English](https://www.cisco.com/site/in/en/index.html)
  * Indonesia
    * [English](https://www.cisco.com/site/id/en/index.html)
  * Japan
    * [日本語](https://www.cisco.com/site/jp/ja/index.html)
  * Korea
    * [한국어](https://www.cisco.com/site/kr/ko/index.html)
  * Malaysia
    * [English](https://www.cisco.com/site/my/en/index.html)
  * Philippines
    * [English](https://www.cisco.com/site/ph/en/index.html)
  * Singapore
    * [English](https://www.cisco.com/site/sg/en/index.html)
  * Thailand
    * [ภาษาไทย](https://www.cisco.com/site/th/th/index.html)
  * Vietnam
    * [Việt](https://www.cisco.com/site/vn/vi/index.html)


  * Austria
    * [Deutsch](https://www.cisco.com/site/at/de/index.html)
  * Belgium & Luxembourg
    * [English](https://www.cisco.com/site/be/en/index.html)
    * [Français](https://www.cisco.com/site/be/fr/index.html)
    * [Nederlands](https://www.cisco.com/site/be/nl/index.html)
  * Czech Republic
    * [Čeština](https://www.cisco.com/site/cz/cs/index.html)
  * Denmark
    * [Dansk](https://www.cisco.com/site/dk/da/index.html)
  * France
    * [Français](https://www.cisco.com/site/fr/fr/index.html)
  * Germany
    * [Deutsch](https://www.cisco.com/site/de/de/index.html)
  * Hungary
    * [Magyar](https://www.cisco.com/site/hu/hu/index.html)
  * Israel
    * [English](https://www.cisco.com/site/il/en/index.html)
  * Italy
    * [Italiano](https://www.cisco.com/site/it/it/index.html)
  * Netherlands
    * [Nederlands](https://www.cisco.com/site/nl/nl/index.html)
  * Norway
    * [Norsk](https://www.cisco.com/site/no/no/index.html)
  * Poland
    * [Polski](https://www.cisco.com/site/pl/pl/index.html)
  * Portugal
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
  * Romania
    * [Română](https://www.cisco.com/site/ro/ro/index.html)
  * Spain
    * [Español](https://www.cisco.com/site/es/es/index.html)
  * Sweden
    * [Svenska](https://www.cisco.com/site/se/sv/index.html)
  * Switzerland
    * [Français](https://www.cisco.com/site/ch/fr/index.html)
    * [Deutsch](https://www.cisco.com/site/ch/de/index.html)
  * Turkey
    * [Türkçe](https://www.cisco.com/site/tr/tr/index.html)
  * Ukraine
    * [Українська ](https://www.cisco.com/site/ua/uk/index.html)
    * [Русский](https://www.cisco.com/site/ua/ru/index.html)
  * United Kingdom & Ireland
    * [English](https://www.cisco.com/site/uk/en/index.html)


  * Hong Kong
    * [English](https://www.cisco.com/site/hk/en/index.html)
    * [繁體中文](https://www.cisco.com/site/hk/zh/index.html)
  * Mainland China
    * [简体中文](https://www.cisco.com/site/cn/zh/index.html)
  * Taiwan
    * [繁體中文](https://www.cisco.com/site/tw/zh/index.html)


  * Argentina
    * [Español](https://www.cisco.com/site/ar/es/index.html)
  * Brazil
    * [Português](https://www.cisco.com/site/br/pt/index.html)
  * Caribbean
    * [Español](https://www.cisco.com/site/bz/es/index.html)
  * Chile
    * [Español](https://www.cisco.com/site/cl/es/index.html)
  * Colombia
    * [Español](https://www.cisco.com/site/co/es/index.html)
  * Costa Rica
    * [Español](https://www.cisco.com/site/cr/es/index.html)
  * Ecuador
    * [Español](https://www.cisco.com/site/ec/es/index.html)
  * Mexico
    * [Español](https://www.cisco.com/site/mx/es/index.html)
  * Panama
    * [Español](https://www.cisco.com/site/pa/es/index.html)
  * Peru
    * [Español](https://www.cisco.com/site/pe/es/index.html)


  * Middle East
    * [English](https://www.cisco.com/site/ae/en/index.html)
    * [عربي](https://www.cisco.com/site/ae/ar/index.html)


Close
Close
  1. [ Partners ](https://www.cisco.com/site/us/en/partners/index.html)


![Businessperson viewing Cisco 360 tools and training options on a tablet.](https://www.cisco.com/content/dam/cisco-cdc/site/images/heroes/partners/cisco-partner-program/cisco-360/tools-and-training/partner-360-tools-and-training-hero-1200x630.png)
#  Tools and training 
Exclusive access to enablement, training, and tools.
* * *
##  Are you a Cisco partner? 
[Become a Cisco partner](https://www.cisco.com/site/us/en/partners/index.html?ccid=cc000864&dtid=odiprc001089)
[Already a partner? Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/partners/tools-training/index.html)
* * *
Show more (1)
* * *
Hello, how can I help?
###  Quick Links
  * [About Cisco](https://www.cisco.com/site/us/en/about/index.html)
  * [Contact Us](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=ftr-contactus)
  * [Careers](https://careers.cisco.com/global/en/home)
  * [Connect with a partner](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)


* * *
###  Resources and Legal
  * [Feedback](https://ciscocx.qualtrics.com/jfe/form/SV_bwrmeoKrBHYxOyW?Ref=/c/en/us/index.html)
  * [Help](https://www.cisco.com/c/en/us/about/help.html)
  * [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
  * [Privacy  
](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
  * [Cookies / Do not sell or share my personal data  
](https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies)
  * [Accessibility](https://www.cisco.com/c/en/us/about/accessibility.html)
  * [Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
  * [Supply Chain Transparency](https://www.cisco.com/c/dam/en_us/about/supply-chain/cisco-modern-slavery-statement.pdf)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)
  * [Sitemap](https://www.cisco.com/site/us/en/about/sitemap.html)


* * *
  * [ ](https://www.facebook.com/cisco/ "Facebook")
  * [ ](https://x.com/Cisco/ "X")
  * [ ](https://www.linkedin.com/company/cisco "LinkedIn")
  * [ ](https://www.youtube.com/user/cisco "YouTube")
  * [ ](https://www.instagram.com/cisco/ "Instagram")


© 2026 Cisco Systems, Inc.
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


---
# ORIGEN: https://www.cisco.com/c/en/us/training-events/training-certifications/overview.html

  * [Skip to main content](https://www.cisco.com/site/us/en/learn/training-certifications/index.html#fw-c-content)
  * [Skip to search](https://www.cisco.com/site/us/en/learn/training-certifications/index.html#fw-c-header__button--search)
  * [Skip to footer](https://www.cisco.com/site/us/en/learn/training-certifications/index.html#fw-c-footer)


[ Cisco.com Worldwide ](https://www.cisco.com "Cisco.com Worldwide")
###  Products and Services
Back
Products and Services
Close
[ Products and Services Home](https://www.cisco.com/site/us/en/products/index.html)
###  Explore a better Wi-Fi 
Deliver fast, secure connectivity across every space. Simplify management and build an AI-ready network designed for growing demands. 
[Get started today](https://www.cisco.com/site/us/en/products/networking/wireless/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/wireless-hub-nav-284x164.jpg)
###  Cisco Security free trials 
Get started with the right security solution for you. Try out our security solutions before you buy them.
[Start a free trial](https://www.cisco.com/site/us/en/products/security/trials-offers.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/security-default-offer-card.jpg)
###  Discover Cisco IQ 
See more, move faster, go farther. Human expertise meets agentic intelligence in every Cisco Services engagement.
[Read the blog](https://blogs.cisco.com/news/cisco-iq-is-generally-available-heres-what-that-actually-means)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-cisco-iq.jpg)
  1. Networking
  2. Security
  3. Collaboration
  4. Computing
  5. Observability
  6. Software
  7. Services (CX)


Back
Networking
Close
## Products
  * [Switches](https://www.cisco.com/site/us/en/products/networking/switches/index.html)
  * [Routers](https://www.cisco.com/site/us/en/products/networking/sdwan-routers/index.html)
  * [Wireless](https://www.cisco.com/site/us/en/products/networking/wireless/index.html)
  * [Optics and transceivers](https://www.cisco.com/site/us/en/products/networking/optics-transceiver-modules/index.html)
  * [Silicon](https://www.cisco.com/site/us/en/products/networking/silicon-one/index.html)
  * [Networking software](https://www.cisco.com/site/us/en/products/networking/software/index.html)


[ Explore Networking](https://www.cisco.com/site/us/en/products/networking/index.html)
* * *
## Use cases
  * [Access networking](https://www.cisco.com/site/us/en/products/networking/access-networking/index.html)
  * [Campus and branch networking](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
  * [Data center and cloud networking](https://www.cisco.com/site/us/en/products/networking/cloud-networking/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/products/networking/industrial-iot/index.html)
  * [Internet, cloud, and endpoint visibility](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)
  * [Network security](https://www.cisco.com/site/us/en/products/networking/network-security/index.html)
  * [Service provider networking](https://www.cisco.com/site/us/en/solutions/service-provider/index.html)
  * [Wide-area networking (WAN)](https://www.cisco.com/site/us/en/products/networking/sdwan-routers/index.html)


* * *
###  Unified network management 
Manage your entire network from a single, intuitive cloud interface with the Meraki and Catalyst Center Global Overview. 
[Explore Networking Platform](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/products-services-networking.jpg)
Back
Security
Close
## Featured products
  * [AI Defense](https://www.cisco.com/site/us/en/products/security/ai-defense/index.html)
  * [Cisco Duo](https://duo.com/?utm_source=cisco&utm_medium=referral)
  * [Email Threat Defense](https://www.cisco.com/site/us/en/products/security/secure-email/index.html)
  * [Firewall](https://www.cisco.com/site/us/en/products/security/firewalls/index.html)
  * [Hypershield](https://www.cisco.com/site/us/en/products/security/hypershield/index.html)
  * [Identity Services Engine (ISE)](https://www.cisco.com/site/us/en/products/security/identity-services-engine/index.html)
  * [Secure Access (SSE)](https://www.cisco.com/site/us/en/products/security/secure-access/index.html)
  * [Splunk Enterprise Security](https://www.splunk.com/en_us/products/enterprise-security.html)
  * [XDR](https://www.cisco.com/site/us/en/products/security/xdr/index.html)


[ Explore Security](https://www.cisco.com/site/us/en/products/security/index.html)
* * *
## Use cases
  * [Agentic SOC](https://www.splunk.com/en_us/products/cyber-security.html)
  * [AI Security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [Hybrid Mesh Firewall](https://www.cisco.com/site/us/en/solutions/security/hybrid-mesh-firewall/index.html)
  * [Industrial security](https://www.cisco.com/site/us/en/products/security/industrial-security/index.html)
  * [Physical security](https://www.cisco.com/site/us/en/products/security/physical-security/index.html)
  * [Secure Access Service Edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Threat intelligence (Talos)](https://www.cisco.com/site/us/en/products/security/talos/index.html)
  * [Zero Trust Access](https://www.cisco.com/site/us/en/solutions/security/zero-trust-access/index.html)
  * [Zero trust for agentic AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/securing-agentic-ai/index.html)


* * *
###  Cisco Secure Access live demo 
Join us live to experience Cisco Secure Access—the smarter way to secure access to the internet, SaaS, and private apps.
[Choose an upcoming slot](https://www.cisco.com/c/en/us/products/security/secure-access/live-demo.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/security-secure-access-demo.jpg)
Back
Collaboration
Close
## Products
  * [Phones, headsets, and collaboration devices](https://www.cisco.com/c/en/us/products/collaboration-endpoints/index.html)
  * [Webex Customer Experience](https://www.webex.com/customer-experience)
  * [Webex Suite](https://www.webex.com/suite/collaboration-suite.html)


[ Explore Collaboration](https://www.cisco.com/site/us/en/products/collaboration/index.html)
* * *
## Use cases
  * [Workspaces](https://www.webex.com/us/en/workspaces.html)
  * [Return to the office](https://www.webex.com/us/en/solutions/return-to-office.html)
  * [Camera intelligence](https://www.webex.com/us/en/solutions/camera-intelligence-cisco-devices.html)
  * [Workspace management](https://www.webex.com/us/en/solutions/control-hub-cisco-devices.html)
  * [Devices for Microsoft Teams](https://www.webex.com/us/en/solutions/microsoft-teams-rooms-cisco-devices.html)
  * [Webex AI](https://www.webex.ai/)
  * [Control Hub](https://www.webex.com/us/en/solutions/cross-platform/control-hub.html)


###  Webex Suite 
Everything your business needs to collaborate—in the world’s first unified, purpose-built suite for hybrid work.
[Explore Webex Suite](https://www.webex.com/suite/collaboration-suite.html) [View the Webex site](https://www.webex.com/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/webex.jpg)
Back
Computing
Close
  * [Converged infrastructure](https://www.cisco.com/site/us/en/solutions/computing/converged-infrastructure/index.html)
  * [Fabric and adapters](https://www.cisco.com/site/us/en/products/computing/servers-unified-computing-systems/fabric-interconnects-extenders/index.html)
  * [Hybrid cloud operations](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)
  * [Hyperconverged infrastructure](https://www.cisco.com/site/us/en/products/computing/hyperconverged/nutanix/index.html)
  * [Servers](https://www.cisco.com/site/us/en/products/computing/servers-unified-computing-systems/index.html)
  * [Stack Automation by Quali](https://www.cisco.com/site/us/en/solutions/data-center/stack-automation-quali/index.html)
  * [Unified Edge](https://www.cisco.com/site/us/en/products/computing/unified-edge/index.html)


[ View all computing products](https://www.cisco.com/site/us/en/products/computing/index.html)
* * *
###  Cisco Intersight free trial 
Get simplified IT operations with infrastructure lifecycle management as a service to easily manage your Cisco UCS, converged, and hyperconverged infrastructure.
[Get started](https://www.cisco.com/c/en/us/solutions/cloud-computing/promotions-free-trials/intersight-free-trial.html) [Learn more about Intersight](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/computing-intersight.jpg)
Back
Observability
Close
## Products
  * [Cloud application security](https://www.cisco.com/site/us/en/products/security/cloud-application-security/index.html)
  * [Splunk Observability Cloud](https://www.splunk.com/en_us/products/observability-cloud.html)
  * [Splunk IT Service Intelligence](https://www.splunk.com/en_us/products/it-service-intelligence.html)
  * [ThousandEyes](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)


[ Explore Observability](https://www.cisco.com/site/us/en/products/observability/index.html)
* * *
## Use cases
  * [Alert noise reduction](https://www.splunk.com/en_us/solutions/alert-noise-reduction.html)
  * [Cloud monitoring optimization](https://www.splunk.com/en_us/solutions/extend-visibility-to-the-cloud.html)
  * [End-user experiences](https://www.splunk.com/en_us/solutions/optimize-your-web-and-mobile-experience.html)
  * [Microservices troubleshooting](https://www.splunk.com/en_us/solutions/isolate-cloud-native-problems.html)


###  Splunk Observability 
Get complete business visibility and real-time troubleshooting across any environment. 
[Explore Splunk Observability](https://www.splunk.com/en_us/products/observability.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/application-performance-appdynamics.jpg)
Back
Software
Close
## Networking
  * [Catalyst Center](https://www.cisco.com/site/us/en/products/networking/catalyst-center/index.html)
  * [Catalyst SD-WAN Manager](https://www.cisco.com/site/us/en/products/networking/wan/sd-wan-manager/index.html)
  * [IoT Operations Dashboard](https://www.cisco.com/c/en/us/support/cloud-systems-management/iot-operations-dashboard/series.html)
  * [Meraki Platform](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
  * [Mobility Services Platform](https://www.cisco.com/site/us/en/solutions/service-provider/networking/mobility-services-platform/index.html)
  * [Nexus Dashboard](https://www.cisco.com/site/us/en/products/networking/cloud-networking/nexus-platform/index.html)
  * [All networking software](https://www.cisco.com/site/us/en/products/networking/software/index.html)


* * *
## Security
  * [Cyber Vision](https://www.cisco.com/site/us/en/products/security/industrial-security/cyber-vision/index.html)
  * [Secure Equipment Access](https://www.cisco.com/site/us/en/products/security/industrial-security/secure-equipment-access/index.html)
  * [Security Cloud](https://www.cisco.com/site/us/en/products/security/security-cloud/index.html)


* * *
## Observability
  * [Splunk Observability](https://www.splunk.com/en_us/products/observability.html)
  * [ThousandEyes](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)


* * *
## Collaboration
  * [Webex by Cisco](https://www.webex.com)


## Computing
  * [Intersight](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)


* * *
  * [Explore Cisco buying programs](https://www.cisco.com/site/us/en/buy/enterprise-software-buying-program.html)
  * [Download software and manage licenses](https://software.cisco.com/)


[ View all software](https://www.cisco.com/site/us/en/products/software/index.html?filters=&search=&sort=a-z&filterby=&showMore=)
* * *
###  Free trials and demos 
View and sign up for over 100 products and portfolio solutions for free. 
[Explore trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/products-software-trials-demos.jpg)
Back
Services (CX)
Close
  * [Cisco Support](https://www.cisco.com/site/us/en/services/support/index.html)
  * [Cisco Professional Services](https://www.cisco.com/site/us/en/services/professional/index.html)
  * [Learn with Cisco](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


[ View all Cisco services](https://www.cisco.com/site/us/en/services/index.html)
* * *
###  Discover Cisco IQ 
See more, move faster, go farther. Human expertise meets agentic intelligence in every Cisco Services engagement.
[Read the blog](https://blogs.cisco.com/news/cisco-iq-is-generally-available-heres-what-that-actually-means)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-cisco-iq.jpg)
###  Get expert guidance 
Cisco Services can help you build the right solution for your needs with the combined power of AI, automation, and human expertise.
[Transform your data center](https://www.cisco.com/site/us/en/services/modern-data-center/index.html) [Build a better workplace](https://www.cisco.com/site/us/en/services/future-workplace/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-promo-expert-guidance.jpg)
Close
###  Solutions
Back
Solutions
Close
[ Solutions Home](https://www.cisco.com/site/us/en/solutions/index.html)
###  Artificial intelligence 
Cisco has the infrastructure to power AI, unmatched breadth and scale of data to feed it, and a portfolio optimized to secure it. 
[Explore Cisco AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-ai.jpg)
###  Campus and branch 
Cisco brings together Al, automation, and security into one unified architecture—built to simplify operations, scale intelligently, and protect every connection.  

[Explore campus and branch](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-campus-branch.jpg)
###  Small and medium business 
Protect, connect, and empower your business with Cisco’s portfolio tailored to small and medium businesses. Experience simplified IT management, efficiency, cloud-driven flexibility, and 24/7 support. 
[Explore SMB solutions](https://www.cisco.com/site/us/en/solutions/small-business/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-smb.jpg)
  1. Artificial Intelligence
  2. Industries
  3. Technologies
  4. Campus and Branch
  5. Service Providers
  6. Small and Medium Business


Back
Artificial Intelligence
Close
  * [AI-enhanced security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [AI-native networking operations](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/netops.html)
  * [AI-ready data centers](https://www.cisco.com/site/us/en/about/why-cisco/ai-ready-data-centers/index.html)
  * [AI at the edge](https://www.cisco.com/site/us/en/solutions/data-center/ai-at-the-edge/index.html)
  * [AI networking in data centers](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/ai-networking-in-data-center/index.html)
  * [Mass-scale AI infrastructure](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/mass-scale-infrastructure/index.html)
  * [Secure AI Factory](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/secure-ai-factory/index.html)
  * [Splunk AI](https://www.splunk.com/en_us/solutions/splunk-artificial-intelligence.html)
  * [Webex AI](https://www.webex.ai/)


[ Cisco AI hub](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/index.html)
###  Cisco AI Assistant 
Cisco AI Assistant combines the latest generative AI technology with our expertise to responsibly guide and inform the decisions you make every day.
[Explore Cisco AI Assistant](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/ai-assistant/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/ai-assistant.jpg)
###  Cisco AI Readiness Assessment 
AI readiness comprises six pillars: Strategy, Infrastructure, Data, Governance, Talent, and Culture. Is your organization AI ready?
[Take assessment](https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index/assessment-tool.html) [Browse AI Readiness Index](https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/ai-readiness.jpg)
Back
Industries
Close
  * [Cities and Communities](https://www.cisco.com/c/en/us/solutions/industries/smart-connected-communities.html)
  * [Education](https://www.cisco.com/site/us/en/solutions/industries/education/index.html)
  * [Financial Services](https://www.cisco.com/site/us/en/solutions/industries/financial-services/index.html)
  * [Government](https://www.cisco.com/site/us/en/solutions/industries/government/index.html)
  * [Healthcare](https://www.cisco.com/site/us/en/solutions/industries/healthcare/index.html)
  * [Manufacturing](https://www.cisco.com/site/us/en/solutions/industries/manufacturing/index.html)
  * [Mining](https://www.cisco.com/site/us/en/solutions/industries/mining/index.html)


* * *
  * [Oil and Gas](https://www.cisco.com/site/us/en/solutions/industries/energy/oil-gas/index.html)
  * [Retail](https://www.cisco.com/site/us/en/solutions/industries/retail/index.html)
  * [Smart Buildings](https://www.cisco.com/site/us/en/solutions/smart-building/index.html)
  * [Sports, Media, and Entertainment](https://www.cisco.com/site/us/en/solutions/industries/sports-media-entertainment/index.html)
  * [Transportation](https://www.cisco.com/site/us/en/solutions/industries/transportation/index.html)
  * [Utilities](https://www.cisco.com/site/us/en/solutions/industries/energy/utilities/index.html)


[ View all industries](https://www.cisco.com/c/en/us/solutions/industries.html)
[ Industry design guides](https://www.cisco.com/c/en/us/solutions/design-zone/industries.html)
* * *
###  Discover the portfolio explorer 
Build the bridge between business outcomes and technology with our new interactive tool.
[Start exploring](https://www.cisco.com/c/m/en_us/solutions/industries/portfolio-explorer.html)
Back
Technologies
Close
## Networking
  * [Cloud and data center networking](https://www.cisco.com/site/us/en/products/networking/cloud-networking/index.html)
  * [Cloud-managed networking (Meraki)](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/index.html)
  * [Networking App Marketplace](https://marketplace.cisco.com/en-US/home)
  * [SD-WAN](https://www.cisco.com/site/us/en/solutions/networking/sdwan/index.html)
  * [Smart buildings](https://www.cisco.com/site/us/en/solutions/smart-building/index.html)
  * [All networking solutions](https://www.cisco.com/c/en/us/solutions/enterprise-networks/solution-listing.html)


## Computing
  * [Converged infrastructure](https://www.cisco.com/site/us/en/solutions/computing/converged-infrastructure/index.html)
  * [Hybrid cloud](https://www.cisco.com/site/us/en/solutions/computing/hybrid-cloud/index.html)
  * [Hyperconverged](https://www.cisco.com/site/us/en/products/computing/hyperconverged/nutanix/index.html)
  * [Stack Automation by Quali](https://www.cisco.com/site/us/en/solutions/data-center/stack-automation-quali/index.html)


* * *
## Security
  * [AI for security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [Data center security](https://www.cisco.com/site/us/en/solutions/security/data-center-security/index.html)
  * [Hybrid Mesh Firewall](https://www.cisco.com/site/us/en/solutions/security/hybrid-mesh-firewall/index.html)
  * [Industrial security](https://www.cisco.com/site/us/en/products/security/industrial-security/index.html)
  * [Network security](https://www.cisco.com/site/us/en/products/networking/network-security/index.html)
  * [Secure Access Service Edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Secure Hybrid Work](https://www.cisco.com/site/us/en/solutions/security/secure-hybrid-work/index.html)
  * [Zero trust](https://www.cisco.com/site/us/en/solutions/security/zero-trust/index.html)
  * [Zero trust for agentic AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/securing-agentic-ai/index.html)


* * *
## Collaboration (Webex)
  * [Camera intelligence](https://www.webex.com/us/en/solutions/camera-intelligence-cisco-devices.html)
  * [Customer experience](https://www.webex.com/us/en/products/customer-experience.html)
  * [Event management](https://www.webex.com/us/en/products/suite/events.html)
  * [Intelligent workspaces](https://www.webex.com/us/en/workspaces.html)
  * [Interoperability](https://www.webex.com/us/en/solutions/interoperability.html)
  * [IT administration](https://www.webex.com/us/en/solutions/cross-platform/control-hub.html)
  * [Remote work](https://www.webex.com/suite/collaboration-suite.html)
  * [Workspace designer](https://designer.webex.com/)
  * [Workspace management](https://www.webex.com/us/en/solutions/control-hub-cisco-devices.html)


Back
Campus and Branch
Close
  * [Secure network architecture](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
  * [Secure campus](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/secure-campus/index.html)
  * [Unified branch](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/unified-branch/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/index.html)
  * [Campus and branch design guides](https://www.cisco.com/c/en/us/solutions/design-zone/campus-branch.html)


* * *
Back
Service Providers
Close
## Empowering your infrastructure
  * [5G network architecture](https://www.cisco.com/c/en/us/solutions/service-provider/5g-network-architecture.html)
  * [Agile Services Networking](https://www.cisco.com/site/us/en/solutions/service-provider/networking/agile-services/index.html)
  * [Broadband solutions](https://www.cisco.com/site/us/en/solutions/service-provider/networking/broadband/index.html)
  * [Cable solutions](https://www.cisco.com/site/us/en/solutions/service-provider/industry/cable/index.html)
  * [Routed optical networking](https://www.cisco.com/site/us/en/solutions/routed-optical-networking/index.html)
  * [Routed PON](https://www.cisco.com/site/us/en/solutions/routed-pon/index.html)


[ View all service provider solutions](https://www.cisco.com/site/us/en/solutions/service-provider/index.html)
* * *
## Managed services
  * [Edge Cloud for Content Delivery](https://www.cisco.com/c/en/us/solutions/service-provider/telco-cloud/edge-cloud-for-content-delivery.html)
  * [IoT Control Center](https://www.cisco.com/site/us/en/products/networking/software/iot-control-center/index.html)
  * [Mobility Services Platform](https://www.cisco.com/site/us/en/solutions/service-provider/networking/mobility-services-platform/index.html)
  * [Private 5G](https://www.cisco.com/site/us/en/products/networking/wireless/private-5g/index.html)
  * [Secure access service edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Software-defined access](https://www.cisco.com/site/us/en/solutions/networking/sdaccess/index.html)
  * [Secure Hybrid Work](https://www.cisco.com/site/us/en/solutions/security/secure-hybrid-work/index.html)
  * [SD-WAN security](https://www.cisco.com/site/us/en/solutions/networking/sdwan/security/index.html)


* * *
###  Accelerate services offerings 
Provide outsourced IT and consulting services with a broad technology portfolio and robust partner support programs.
[See services options](https://www.cisco.com/site/us/en/partners/build-your-practice/managed-services/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/managed-services.jpg)
Back
Small and Medium Business
Close
## Products and solutions
  * [Networking](https://www.cisco.com/site/us/en/solutions/small-business/networking/index.html)
  * [Security](https://www.cisco.com/site/us/en/solutions/small-business/security/index.html)
  * [Collaboration](https://www.cisco.com/site/us/en/solutions/small-business/collaboration/index.html)
  * [Product selector](https://www.cisco.com/c/en/us/solutions/small-business/selector-tool.html)


[ View all small and medium business solutions](https://www.cisco.com/site/us/en/solutions/small-business/index.html)
[ Buy small and medium business products online](https://www.cisco.com/c/en/us/solutions/small-business/small-business-promotions-and-free-trials/buy-cisco-small-business-products-online.html)
* * *
###  Offers and free trials 
Find the best solutions for your needs and try them before you buy. 
[See all offers and free trials](https://www.cisco.com/site/us/en/solutions/small-business/trials-offers.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/smb-free-trials.jpg)
Close
###  Support
Back
Support
Close
[ Support Home](https://www.cisco.com/c/en/us/support/index.html)
###  Support home 
Access documentation, security notices, and support tools for Cisco products.
[View Cisco Support](https://www.cisco.com/c/en/us/support/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-home-penn1_brandlibrary-DSC0318.jpg)
###  Software downloads 
Download and manage new software, get updates or patches, or upgrade your current software to the latest release.
[View Software Central](https://software.cisco.com/download/home)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-software-downloads-hatchlibrary-general-gettyPA-Cisco-1309760275.jpg)
###  Licensing support 
Troubleshoot common licensing issues and leverage easy-to-follow documentation for both PAK-based or Smart Licenses.
[Get licensing support](https://www.cisco.com/c/en/us/support/licensing/licensing-support.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-licensing-hatchlibrary-security-gettyPA-Cisco-1518851638.jpg)
  1. Products and Downloads
  2. Documentation
  3. Contact Support
  4. Licenses and Contracts
  5. Tools and Resources
  6. Cisco Community


Back
Products and Downloads
Close
## Find products and downloads
Search field edit, type in text
Clear
[Downloads](https://www.cisco.com/site/us/en/learn/training-certifications/index.html#tabs-7edb32179e-item-d43da2dc1e-tab) [Product Support](https://www.cisco.com/site/us/en/learn/training-certifications/index.html#tabs-7edb32179e-item-d43da2dc1e-tab) [Technology Support](https://www.cisco.com/site/us/en/learn/training-certifications/index.html#tabs-7edb32179e-item-d43da2dc1e-tab) | End of Sale End of Support
* [All Downloads](https://software.cisco.com/download/navigator.html)
* [All Products](https://www.cisco.com/c/en/us/support/all-products.html)
* Search all cisco.com
When autocomplete results are available use up and down arrows to review and enter to select
## Product Support
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Security](https://www.cisco.com/c/en/us/support/security/category.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Wireless](https://www.cisco.com/c/en/us/support/wireless/category.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Collaboration endpoints and phones](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Networking software (IOS and NX-OS)](https://www.cisco.com/c/en/us/support/ios-nx-os-software/index.html)
  * [Servers - Unified Computing (UCS)](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)


[ All products](https://www.cisco.com/c/en/us/support/all-products.html)
* * *
## Downloads
  * [Secure Client 5](https://software.cisco.com/download/home/286330811/type/282364313/release/)
  * [Identity Services Engine Software](https://software.cisco.com/download/home/283801620/type/283802505/)
  * [Secure Firewall Management Center Virtual](https://software.cisco.com/download/home/286259687/type)
  * [Smart Software Manager](https://software.cisco.com/download/home/286285506/type)
  * [Jabber for Windows](https://software.cisco.com/download/home/284324806/type/284006014/release/)
  * [Modeling Labs](https://software.cisco.com/download/home/286193282/type/286326381/release/2.7.2)
  * [Catalyst 9300 Series Switches](https://software.cisco.com/download/home/286313806)


[ All downloads](https://software.cisco.com/download/home)
* * *
Back
Documentation
Close
[ Technical documentation](https://www.cisco.com/c/en/us/docs/technical-documentation.html)
Configure, operate, and troubleshoot your Cisco products with configuration guides, installation guides, release notes, and more.
[ Trust Portal](https://trustportal.cisco.com/c/r/ctp/home.html)
Get self-service access to security, data privacy, and compliance documents.
* * *
[ Product documentation](https://www.cisco.com/c/en/us/products/a-to-z-series-index.html#all)
Explore Cisco products and features to empower your purchase with data sheets, white papers, end-of-life notices, and more.
* * *
Back
Contact Support
Close
## Product technical support (TAC)
[ Open a new case](https://mycase.cloudapps.cisco.com/case)
(Requires a product or software support contract)
  * [Manage support cases](https://mycase.cloudapps.cisco.com/case)
  * [Returns Portal (RMAs)](https://www.cisco.com/c/en/us/support/returns/returns-portal.html)


* * *
Enterprise and Service Provider products
**1-800-553-2447** US and Canada
[ Worldwide phone numbers](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)
* * *
Small and medium business products
**1-866-606-1866** US and Canada
[ Worldwide phone numbers](https://www.cisco.com/c/en/us/support/web/tsd-cisco-small-business-support-center-contacts.html)
Back
Licenses and Contracts
Close
## Software licenses
  * [Explore key licensing resources](https://www.cisco.com/site/us/en/buy/licensing/index.html)
  * [Download and manage licenses](https://software.cisco.com/)
  * [Manage assets and entitlements](https://software.cisco.com/clc/access-directory)
  * [Troubleshoot license issues](https://www.cisco.com/c/en/us/support/licensing/licensing-support.html)


## Cisco Enterprise Agreement (EA)
  * [Manage Cisco EA licenses](https://software.cisco.com/software/ea/agreements)
  * [Learn about Cisco EA](https://www.cisco.com/site/us/en/buy/enterprise-agreement/index.html)


* * *
## Product support contracts
  * [Manage and renew service contracts (CCW-R)](https://ccrc.cisco.com/ccwr/)


###  Cisco Licensing Hub 
Enhance your Cisco licensing experience. 
[Access now](https://www.cisco.com/site/us/en/buy/licensing/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-licensing-hub.jpg)
Back
Tools and Resources
Close
## Tools
  * [Bug Search Tool](https://bst.cisco.com/bugsearch/?referring_site=shp)
  * [My Devices](https://cway.cisco.com/mydevices)
  * [My Saved Content](https://www.cisco.com/c/en/us/support/saved/index.html)
  * [Software Research](https://software.cisco.com/research/home)
  * [Device Coverage Checker](https://cway.cisco.com/sncheck/)


[ All Support tools](https://www.cisco.com/c/en/us/support/web/tools-catalog.html)
* * *
## Notifications and advisories
  * [My Notifications](https://cway.cisco.com/mynotifications)
  * [Security Advisories](https://sec.cloudapps.cisco.com/security/center/publicationListing.x)
  * [Field Notices](https://www.cisco.com/c/en/us/support/web/tsd-products-field-notice-summary.html)
  * [Cisco Cloud Status](https://www.cisco.com/c/en/us/support/web/cloud-status.html)


### Services
  * [All Cisco Services](https://www.cisco.com/site/us/en/services/index.html)


## Technology adoption
  * [Cisco Customer Success](https://www.cisco.com/c/m/en_us/customer-experience/customer-success/index.html)


Back
Cisco Community
Close
## Community forums
  * [Technology and Support](https://community.cisco.com/t5/technology-and-support/ct-p/technology-support)
  * [Small Business Support](https://community.cisco.com/t5/small-business-support-community/ct-p/5541-small-business-support)
  * [Developers](https://community.cisco.com/t5/devnet/ct-p/4409j-developer-home)
  * [Partners](https://community.cisco.com/t5/partner-hub/ct-p/2002j-partner-home)
  * [Project Gallery](https://community.cisco.com/t5/project-gallery/con-p/customer-success-stories)
  * [Cisco Insider User Group](https://community.cisco.com/t5/cisco-insider-user-group/ct-p/ccp-home)


[ Explore Cisco Community](https://community.cisco.com/)
* * *
###  Community events and webinars 
Learn from Cisco experts and engage with peers in webinars and live events.
[View all events and webinars](https://community.cisco.com/t5/technology-and-support-events-and-webinars/eb-p/ts-events-webinars-bd)
Close
###  Learn
Back
Learn
Close
[ Learn Home](https://www.cisco.com/site/us/en/learn/index.html)
###  Cisco U. 
Access training tailored to your needs. Work toward a specific role or certification, deploy or support a technology solution, or enhance your career progress.
[Learn more about Cisco U. ](https://www.cisco.com/site/us/en/learn/training-certifications/training/ciscou/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-cisco-u.jpg)
###  Cisco Networking Academy 
If you're a student, start at Cisco Networking Academy. With free courses and career guidance, your next IT job is closer than you think.
[Join now](https://www.netacad.com/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-netacad.jpg)
###  Events 
Join us to take advantage of the latest networking opportunities with Cisco customers, partners, employees, and subject-matter experts.
[Explore now](https://www.cisco.com/site/us/en/learn/events/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/events-calendar-default.jpg)
  1. Training and Certifications
  2. Events
  3. Webinars
  4. Technology Learning Topics
  5. Learning Resources and Assets


Back
Training and Certifications
Close
## Learning
  * [Cisco Networking Academy](https://www.netacad.com)
  * [Cisco U. ](https://u.cisco.com)
  * [Instructor-led training](https://learninglocator.cloudapps.cisco.com/#/home)
  * [Cisco Modeling Labs](https://www.cisco.com/site/us/en/learn/training-certifications/training/modeling-labs/index.html)
  * [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer)
  * [Join our community](https://learningnetwork.cisco.com/s/)
  * [Learn with Cisco blog](https://blogs.cisco.com/learning)


[ Learn with Cisco overview](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)
* * *
## Certifications
  * [Career certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
  * [Learn about exams](https://www.cisco.com/site/us/en/learn/training-certifications/exams/index.html)
  * [Continuing Education (CE credits)](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/continuing-education/index.html)
  * [Recertification](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/recertification/index.html)
  * [Schedule an exam](https://cp.certmetrics.com/cisco/en/schedule/schedule-exam)
  * [Track my certifications](https://cp.certmetrics.com/cisco/en/credentials/status)


* * *
## Training for organizations
  * [Enterprise](https://www.cisco.com/site/us/en/learn/training-certifications/enterprise-training/index.html)
  * [Cisco Learning Credits](https://www.cisco.com/site/us/en/learn/training-certifications/training/learning-credits/index.html)
  * [Training catalog](https://www.cisco.com/site/us/en/learn/training-certifications/training/training-catalog/index.html)
  * [Partners](https://www.cisco.com/site/us/en/learn/training-certifications/partner-resources.html)


## Support
  * [Learn with Cisco support bot](https://certsupport.cisco.com/s/?language=en_US)


Back
Events
Close
  * [Cisco Live](https://www.ciscolive.com/home/en/index.html?cid=cdc-hp-nav-home#xd_co_f)
  * [Partner events calendar](https://salesconnect.cisco.com/americaspartnercommunity/s/enablement-training-calendar)


[ View all events](https://www.cisco.com/site/us/en/learn/events/index.html)
* * *
###  Cisco Live 2026 Melbourne 
Experience the education, inspiration, and fun of Cisco Live 2026 Melbourne.
[Register now](https://www.ciscolive.com/apjc?ccid=cc008775&cid=CL26eventspage&eid=162820&oid=eprsas033263)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/cl2026-cisco-live-las-vegas.jpg)
###  Watch Cisco Live sessions on demand 
View sessions from Las Vegas in our On-Demand Library. Keynotes, Deep Dives, and Center Stage sessions are available now, with the remaining sessions added by June 19.
[Watch now](https://www.ciscolive.com/on-demand/on-demand-library.html?cid=cdc-hp-nav&utm_team=global_events&utm_medium=email&utm_source=sendgrid&utm_campaign=xb_cxp_fy26q4_amer_20260623past&ccid=cc007720&dtid=oemrft001460&utm_eid=95796&search.event=1769534158486002QYqy#/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/cl2026-cisco-live-las-vegas.jpg)
Back
Webinars
Close
## Trending webinars
  * [AI readiness for data centers](https://experiences.cisco.com/amer/ai-readiness-for-data-centers)
  * [Simplify IT with SD-WAN](https://experiences.cisco.com/amer/simplify-it-with-sd-wan)
  * [Security transformation with Cisco XDR](https://cloudsecurity.cisco.com/webinar-security-transformation-with-cisco-xdr)


[ View all webinars](https://experiences.cisco.com/amer?pf_route=1&groups=all-webinars)
* * *
###  McLaren Racing + Cisco 
Carrie Palin joins McLaren Racing F1 team CEO Zak Brown and driver Oscar Piastri as they unveil the high-tech secrets behind their team's successful 2024 season.
[Watch on demand](https://experiences.cisco.com/amer/cisco-mclaren-innovation-speed)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-webinars-mclaren-racing.jpg)
###  Cisco webinars 
Discover insights that shape the future of technology. Our webinars feature experts and leaders sharing how organizations transform to connect, grow, and succeed.
[Explore webinars](https://experiences.cisco.com/amer?pf_route=1&group=all-webinars&groups=all-webinars)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-webinars.jpg)
Back
Technology Learning Topics
Close
  * [How to set up a router](https://www.cisco.com/site/us/en/learn/topics/small-business/how-to-set-up-router.html)
  * [What is cybersecurity?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-cybersecurity.html)
  * [What is a firewall?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-firewall.html)
  * [What is Industry 4.0?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-industry-4-0.html)
  * [What is IoT (Internet of Things)?](https://www.cisco.com/site/us/en/learn/topics/industrial-iot/what-is-iot.html)
  * [What is Wi-Fi 7?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-wi-fi-7.html)


* * *
  * [What is AIOps?](https://www.cisco.com/site/us/en/learn/topics/artificial-intelligence/what-is-aiops.html)
  * [What is cloud security?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-cloud-security.html)
  * [What is hybrid cloud?](https://www.cisco.com/site/us/en/learn/topics/computing/what-is-hybrid-cloud.html)
  * [What is SASE?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-secure-access-service-edge-sase.html)
  * [What is software as a service (SaaS)?](https://www.cisco.com/site/us/en/learn/topics/software/what-is-software-as-a-service-saas.html)


[ View all technology learning topics](https://www.cisco.com/site/us/en/learn/topics/index.html)
* * *
###  2026 State of Industrial AI 
We surveyed more than 1000 industrial professionals on securing operations, advancing IT/OT collaboration, and building an AI-ready network that can scale.
[Get report](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/industrial-networking-report/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/state-of-industrial-ai-284x164.jpg)
Back
Learning Resources and Assets
Close
## Sandboxes and simulators
  * [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer)
  * [DevNet Sandbox](https://developer.cisco.com/site/sandbox/)
  * [Cisco Modeling Labs](https://developer.cisco.com/modeling-labs/)
  * [Cisco Learning Labs](https://u.cisco.com/store/lab?type=cisco-learning-labs)


## News and insights
  * [Blogs](https://blogs.cisco.com/)
  * [Cisco Community](https://community.cisco.com/)
  * [Executive perspectives](https://www.cisco.com/c/en/us/solutions/executive-perspectives/index.html)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)


* * *
## Developer resources
  * [Getting started with DevNet](https://developer.cisco.com/startnow/)
  * [DevNet Tracks](https://developer.cisco.com/learning/search/?contentType=track&page=1)
  * [Python training](https://www.cisco.com/site/us/en/learn/training-certifications/training/courses/prne.html)
  * [Code exchange](https://developer.cisco.com/codeexchange/)
  * [Developer community](https://community.cisco.com/t5/devnet/ct-p/4409j-developer-home)


## Videos and live streams
  * [Cisco Video Portal](https://video.cisco.com/)


* * *
## Architecture and design resources
  * [Cisco Validated](https://www.cisco.com/site/us/en/solutions/cisco-validated/index.html)
  * [Visio stencils](https://www.cisco.com/c/en/us/products/visio-stencil-listing.html)


## Additional resources
  * [Cisco Learning Credits](https://www.cisco.com/site/us/en/learn/training-certifications/training/learning-credits/index.html)
  * [Cisco Multicloud training](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/multicloud/index.html)
  * [Black Belt Academy (for partners)](https://www.cisco.com/site/us/en/partners/training/black-belt-academy/index.html)


Close
###  Why Cisco
Back
Why Cisco
Close
[ Why Cisco](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
###  Why Cisco 
Cisco creates the infrastructure you need to transform how you connect, protect, and innovate in the AI era.
[See the Cisco advantage](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-ai-blue.jpg)
###  Our Purpose 
We Power an Inclusive Future for All.
[Explore our Purpose](https://www.cisco.com/site/us/en/about/purpose/index.html) [Read FY25 Purpose Report](https://www.cisco.com/c/dam/m/en_us/about/purpose/reporting-hub/_pdf/purpose-report-2025.pdf)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-purpose.jpg)
###  Success stories 
Discover how Cisco technologies drive real-world success for our customers and power Cisco's own operations and innovation. 
[Explore customer stories](https://www.cisco.com/site/us/en/about/case-studies-customer-stories/index.html) [How we use our technology](https://www.cisco.com/site/us/en/solutions/cisco-on-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-success-stories.jpg)
  1. Outcomes We Deliver
  2. Working with Partners
  3. About Us


Back
Outcomes We Deliver
Close
[ AI-ready data centers](https://www.cisco.com/site/us/en/about/why-cisco/ai-ready-data-centers/index.html)
Unleash the power of AI with data centers designed for speed, scale, and agility.
[ Future-proofed workplaces](https://www.cisco.com/site/us/en/about/why-cisco/future-proofed-workplaces/index.html)
Elevate employee and customer experiences with agile, resilient workplaces.
[ Digital resilience](https://www.cisco.com/site/us/en/about/why-cisco/digital-resilience/index.html)
Achieve always-on resilience with trusted security, observability, and assurance.
* * *
###  Why Cisco 
Cisco creates the infrastructure you need to transform how you connect, protect, and innovate in the AI era.
[See the Cisco advantage](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-ai-blue.jpg)
Back
Working with Partners
Close
[ Why choose Cisco partners](https://www.cisco.com/site/us/en/partners/evolved-partner-ecosystem/index.html)
Learn how our partner ecosystem makes it easier than ever to identify the partners to best meet your needs. ​ 
[ Frequently asked questions (PDF)](https://www.cisco.com/c/dam/en_us/partners/cisco-partner-designations-faq.pdf)
Access answers to your questions about the evolution of Cisco's partner ecosystem and new partner designations. 
[ Find a partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
Explore our partner ecosystem today. 
* * *
###  A new way to find partners 
The Cisco Partner Locator tool has been transformed into an AI-driven hub to match, recommend, and activate partners for every customer outcome.​ 
[Explore what's new](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/partner-locator-curve.jpg)
Back
About Us
Close
  * [Overview](https://www.cisco.com/site/us/en/about/index.html)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)
  * [Leadership](https://newsroom.cisco.com/c/r/newsroom/en/us/executives.html)
  * [Purpose and sustainability](https://www.cisco.com/site/us/en/about/purpose/index.html)
  * [Career opportunities](https://careers.cisco.com/global/en/home)
  * [The Trust Center](https://www.cisco.com/c/en/us/about/trust-center.html)
  * [Investor relations](https://investor.cisco.com/overview/default.aspx)


[ Contact us](https://www.cisco.com/site/us/en/about/contact-cisco/index.html)
* * *
###  How to buy 
Browse options to purchase Cisco products, services, and software offerings.
[Visit how-to-buy hub](https://www.cisco.com/site/us/en/buy/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-how-to-buy.jpg)
Close
###  Partners
Close
[ Trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html?linkclickid=hdr-mainnav-trialsdemos)
[ How to buy](https://www.cisco.com/site/us/en/buy/index.html?linkclickid=hdr-utilnav-howtobuy)
Partners
EN US
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/learn/training-certifications/index.html)
[ Trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html?linkclickid=hdr-mainnav-trialsdemos)
MENU
CLOSE
[ How to buy](https://www.cisco.com/site/us/en/buy/index.html?linkclickid=hdr-utilnav-howtobuy)
Partners
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/learn/training-certifications/index.html)
EN US
Search field edit, type in text
Clear Speech-to-Text Search Search
* * *
Speech-to-Text Powered By Google Speech API
We didn't hear that. Try again.
Speech-to-Text Search is currently unavailable
  * [Downloads](https://software.cisco.com/download/home)
  * [Certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
  * [Cisco Validated](https://www.cisco.com/c/en/us/solutions/cisco-validated.html)
  * [Training](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)
  * [Community](https://community.cisco.com/)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)


Close
**For Partners**
[Partners Home](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129)
[Partner Program](https://www.cisco.com/site/us/en/partners/index.html?ccid=cc000864&dtid=odiprc001129)
[Support](https://www.cisco.com/site/us/en/partners/support-help/index.html?dtid=odiprc001129)
[Tools](https://www.cisco.com/site/us/en/partners/tools-training/index.html?dtid=odiprc001129)
**Already a Partner?**
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/learn/training-certifications/index.html)
* * *
[Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/ "Find a Cisco Partner")
* * *
[Learn about Partners](https://www.cisco.com/site/us/en/partners/evolved-partner-ecosystem/index.html)
* * *
[Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129 "Become a Cisco Partner")
Close
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/learn/training-certifications/index.html)
Don't have an account? [Sign up](https://id.cisco.com/signin/register "Sign up")
Close
Back
Country | Language
Close
Selected country/region:
United States
  * [English](https://www.cisco.com/site/us/en/index.html)


  1. All Countries / Regions
  2. North America
  3. Africa
  4. Asia Pacific
  5. Europe
  6. Greater China
  7. Latin America
  8. Middle East


  * United States
    * [English](https://www.cisco.com/site/us/en/index.html)
  * Africa
    * [English](https://www.cisco.com/site/dz/en/index.html)
    * [Français](https://www.cisco.com/site/dz/fr/index.html)
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * Argentina
    * [Español](https://www.cisco.com/site/ar/es/index.html)
  * Australia & New Zealand
    * [English](https://www.cisco.com/site/au/en/index.html)
  * Austria
    * [Deutsch](https://www.cisco.com/site/at/de/index.html)
  * Belgium & Luxembourg
    * [English](https://www.cisco.com/site/be/en/index.html)
    * [Français](https://www.cisco.com/site/be/fr/index.html)
    * [Nederlands](https://www.cisco.com/site/be/nl/index.html)
  * Brazil
    * [Português](https://www.cisco.com/site/br/pt/index.html)
  * Canada
    * [English](https://www.cisco.com/site/ca/en/index.html)
    * [Français](https://www.cisco.com/site/ca/fr/index.html)
  * Caribbean
    * [Español](https://www.cisco.com/site/bz/es/index.html)
  * Chile
    * [Español](https://www.cisco.com/site/cl/es/index.html)
  * Colombia
    * [Español](https://www.cisco.com/site/co/es/index.html)
  * Costa Rica
    * [Español](https://www.cisco.com/site/cr/es/index.html)
  * Czech Republic
    * [Čeština](https://www.cisco.com/site/cz/cs/index.html)
  * Denmark
    * [Dansk](https://www.cisco.com/site/dk/da/index.html)
  * Ecuador
    * [Español](https://www.cisco.com/site/ec/es/index.html)
  * Egypt
    * [English](https://www.cisco.com/site/eg/en/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * France
    * [Français](https://www.cisco.com/site/fr/fr/index.html)
  * Germany
    * [Deutsch](https://www.cisco.com/site/de/de/index.html)
  * Hong Kong
    * [English](https://www.cisco.com/site/hk/en/index.html)
    * [繁體中文](https://www.cisco.com/site/hk/zh/index.html)
  * Hungary
    * [Magyar](https://www.cisco.com/site/hu/hu/index.html)
  * India
    * [English](https://www.cisco.com/site/in/en/index.html)
  * Indonesia
    * [English](https://www.cisco.com/site/id/en/index.html)
  * Israel
    * [English](https://www.cisco.com/site/il/en/index.html)
  * Italy
    * [Italiano](https://www.cisco.com/site/it/it/index.html)
  * Japan
    * [日本語](https://www.cisco.com/site/jp/ja/index.html)
  * Korea
    * [한국어](https://www.cisco.com/site/kr/ko/index.html)
  * Mainland China
    * [简体中文](https://www.cisco.com/site/cn/zh/index.html)
  * Malaysia
    * [English](https://www.cisco.com/site/my/en/index.html)
  * Mexico
    * [Español](https://www.cisco.com/site/mx/es/index.html)
  * Middle East
    * [English](https://www.cisco.com/site/ae/en/index.html)
    * [عربي](https://www.cisco.com/site/ae/ar/index.html)
  * Netherlands
    * [Nederlands](https://www.cisco.com/site/nl/nl/index.html)
  * Norway
    * [Norsk](https://www.cisco.com/site/no/no/index.html)
  * Panama
    * [Español](https://www.cisco.com/site/pa/es/index.html)
  * Peru
    * [Español](https://www.cisco.com/site/pe/es/index.html)
  * Philippines
    * [English](https://www.cisco.com/site/ph/en/index.html)
  * Poland
    * [Polski](https://www.cisco.com/site/pl/pl/index.html)
  * Portugal
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
  * Romania
    * [Română](https://www.cisco.com/site/ro/ro/index.html)
  * Singapore
    * [English](https://www.cisco.com/site/sg/en/index.html)
  * South Africa
    * [English](https://www.cisco.com/site/za/en/index.html)
  * Spain
    * [Español](https://www.cisco.com/site/es/es/index.html)
  * Sweden
    * [Svenska](https://www.cisco.com/site/se/sv/index.html)
  * Switzerland
    * [Français](https://www.cisco.com/site/ch/fr/index.html)
    * [Deutsch](https://www.cisco.com/site/ch/de/index.html)
  * Taiwan
    * [繁體中文](https://www.cisco.com/site/tw/zh/index.html)
  * Thailand
    * [ภาษาไทย](https://www.cisco.com/site/th/th/index.html)
  * Turkey
    * [Türkçe](https://www.cisco.com/site/tr/tr/index.html)
  * Ukraine
    * [Українська ](https://www.cisco.com/site/ua/uk/index.html)
    * [Русский](https://www.cisco.com/site/ua/ru/index.html)
  * United Kingdom & Ireland
    * [English](https://www.cisco.com/site/uk/en/index.html)
  * Vietnam
    * [Việt](https://www.cisco.com/site/vn/vi/index.html)


  * Canada
    * [English](https://www.cisco.com/site/ca/en/index.html)
    * [Français](https://www.cisco.com/site/ca/fr/index.html)
  * United States
    * [English](https://www.cisco.com/site/us/en/index.html)


  * Africa
    * [English](https://www.cisco.com/site/dz/en/index.html)
    * [Français](https://www.cisco.com/site/dz/fr/index.html)
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * Egypt
    * [English](https://www.cisco.com/site/eg/en/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * South Africa
    * [English](https://www.cisco.com/site/za/en/index.html)


  * Australia & New Zealand
    * [English](https://www.cisco.com/site/au/en/index.html)
  * India
    * [English](https://www.cisco.com/site/in/en/index.html)
  * Indonesia
    * [English](https://www.cisco.com/site/id/en/index.html)
  * Japan
    * [日本語](https://www.cisco.com/site/jp/ja/index.html)
  * Korea
    * [한국어](https://www.cisco.com/site/kr/ko/index.html)
  * Malaysia
    * [English](https://www.cisco.com/site/my/en/index.html)
  * Philippines
    * [English](https://www.cisco.com/site/ph/en/index.html)
  * Singapore
    * [English](https://www.cisco.com/site/sg/en/index.html)
  * Thailand
    * [ภาษาไทย](https://www.cisco.com/site/th/th/index.html)
  * Vietnam
    * [Việt](https://www.cisco.com/site/vn/vi/index.html)


  * Austria
    * [Deutsch](https://www.cisco.com/site/at/de/index.html)
  * Belgium & Luxembourg
    * [English](https://www.cisco.com/site/be/en/index.html)
    * [Français](https://www.cisco.com/site/be/fr/index.html)
    * [Nederlands](https://www.cisco.com/site/be/nl/index.html)
  * Czech Republic
    * [Čeština](https://www.cisco.com/site/cz/cs/index.html)
  * Denmark
    * [Dansk](https://www.cisco.com/site/dk/da/index.html)
  * France
    * [Français](https://www.cisco.com/site/fr/fr/index.html)
  * Germany
    * [Deutsch](https://www.cisco.com/site/de/de/index.html)
  * Hungary
    * [Magyar](https://www.cisco.com/site/hu/hu/index.html)
  * Israel
    * [English](https://www.cisco.com/site/il/en/index.html)
  * Italy
    * [Italiano](https://www.cisco.com/site/it/it/index.html)
  * Netherlands
    * [Nederlands](https://www.cisco.com/site/nl/nl/index.html)
  * Norway
    * [Norsk](https://www.cisco.com/site/no/no/index.html)
  * Poland
    * [Polski](https://www.cisco.com/site/pl/pl/index.html)
  * Portugal
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
  * Romania
    * [Română](https://www.cisco.com/site/ro/ro/index.html)
  * Spain
    * [Español](https://www.cisco.com/site/es/es/index.html)
  * Sweden
    * [Svenska](https://www.cisco.com/site/se/sv/index.html)
  * Switzerland
    * [Français](https://www.cisco.com/site/ch/fr/index.html)
    * [Deutsch](https://www.cisco.com/site/ch/de/index.html)
  * Turkey
    * [Türkçe](https://www.cisco.com/site/tr/tr/index.html)
  * Ukraine
    * [Українська ](https://www.cisco.com/site/ua/uk/index.html)
    * [Русский](https://www.cisco.com/site/ua/ru/index.html)
  * United Kingdom & Ireland
    * [English](https://www.cisco.com/site/uk/en/index.html)


  * Hong Kong
    * [English](https://www.cisco.com/site/hk/en/index.html)
    * [繁體中文](https://www.cisco.com/site/hk/zh/index.html)
  * Mainland China
    * [简体中文](https://www.cisco.com/site/cn/zh/index.html)
  * Taiwan
    * [繁體中文](https://www.cisco.com/site/tw/zh/index.html)


  * Argentina
    * [Español](https://www.cisco.com/site/ar/es/index.html)
  * Brazil
    * [Português](https://www.cisco.com/site/br/pt/index.html)
  * Caribbean
    * [Español](https://www.cisco.com/site/bz/es/index.html)
  * Chile
    * [Español](https://www.cisco.com/site/cl/es/index.html)
  * Colombia
    * [Español](https://www.cisco.com/site/co/es/index.html)
  * Costa Rica
    * [Español](https://www.cisco.com/site/cr/es/index.html)
  * Ecuador
    * [Español](https://www.cisco.com/site/ec/es/index.html)
  * Mexico
    * [Español](https://www.cisco.com/site/mx/es/index.html)
  * Panama
    * [Español](https://www.cisco.com/site/pa/es/index.html)
  * Peru
    * [Español](https://www.cisco.com/site/pe/es/index.html)


  * Middle East
    * [English](https://www.cisco.com/site/ae/en/index.html)
    * [عربي](https://www.cisco.com/site/ae/ar/index.html)


Close
Close
Hello, how can I help?
  1. [ Learn ](https://www.cisco.com/site/us/en/learn/index.html)


![](https://cf-images.us-east-1.prod.boltdns.net/v1/jit/1384193102001/c8220483-e89f-4eef-988c-023189a43d1b/main/1280x720/33s408ms/match/image.jpg)
#  Learn with Cisco 
At Learn with Cisco, it’s about the learning journey and the destination—because being future-ready means continuous learning to meet desired outcomes. Skills development. Product training. Career development. We’ve got you all the way.
## Join millions who embrace lifelong learning
### 28.3 million
Become one of more than 28.3 million individuals trained
### 4 million
You’re in good company, with over 4 million certifications issued
### 1.8 million
Join a community of over 1.8 million learners
## Delivering outcomes that matter
Whether you’re one of one or one of many on a team, pick your pathway to outcome success with Cisco gold-standard certifications, comprehensive IT training, or both.
![Advance your career as an individual, or get your team to the next level with our industry-recognized certification program.](https://www.cisco.com/content/dam/cisco-cdc/site/images/photography/learn/544/hatchlibrary-gettypa-1298709254-544x306.jpg)
###  Chart your career path with Cisco certifications 
Advance your career as an individual, or get your team to the next level with our industry-recognized certification program. Each certification is a benchmark for expertise and a way to stand out in the technologies organizations use every day.
[Explore certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
![Equip your team with the skills they need to turn on a dime to meet any new challenge.](https://www.cisco.com/content/dam/cisco-cdc/site/images/photography/learn/544/upskill-with-your-team-544x306.jpg)
###  Create a future-ready workforce 
Equip your team with the skills they need to turn on a dime to meet any new challenge. Convert digital transformation into new opportunities for your team’s and organization’s best future.
[Explore learning for organizations](https://www.cisco.com/site/us/en/learn/training-certifications/enterprise-training/index.html)
* * *
Show more (1)
* * *
## Learning platforms for all levels and learning styles
Our learning options grow with you—even if you’re still not exactly sure where you want to go. We can help you get where you want to be, or figure it all out.
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/icons-and-shapes/about/purpose/icon-networking.svg)
Skills-to-jobs training for beginner and entry levels
###  Cisco Networking Academy 
Your success story starts here. If you're just starting your tech career, Networking Academy beginner-friendly content can help you decide where you fit in IT. Learn online or in academies worldwide.
[Explore Cisco Networking Academy](https://www.netacad.com/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/icons-and-shapes/icon-digital-web-design-80x80.svg)
Product, certification, and skills training for associate to expert levels
###  Cisco U. 
Let the lifelong learning continue with Cisco U. Find certification prep, tutorials, hands-on labs, Learning Paths, Continuing Education credits, and everything in between to meet your long or short-term goals.
[Explore Cisco U.](https://www.cisco.com/site/us/en/learn/training-certifications/training/ciscou/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/icons-and-shapes/marketing-icons/icon_training.svg)
Authorized instructor-led training for all your learning needs
###  Cisco Learning Partners 
Cisco Learning Partners deliver authorized, instructor-led training at every level of expertise, to help enterprises and individuals build critical skills fast, maximize Cisco investments, and achieve real business outcomes.
[Learn about Learning Partners](https://www.cisco.com/site/us/en/learn/training-certifications/training/learning-partner-program/index.html)
* * *
Show more (1)
* * *
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/cq-template/idc-marketscape-662x372.jpg)
##  Cisco named a leader in IT training services 
As a recognized leader in IT training and professional development, Cisco empowers today’s workforce with industry-leading skills. Access the excerpts from the 2025-2026 IDC MarketScape for North America and the 2025 IDC MarketScape for Europe to see how our programs are shaping technology readiness and driving measurable business outcomes1.
###  IDC MarketScape: North America IT Training Services 2025-2026 Vendor Assessment 
[Download the North America excerpt](https://idcdocserv.com/US52991625e_Cisco)
###  IDC MarketScape: European IT Training Services 2025 Vendor Assessment 
[Download the European excerpt](https://idcdocserv.com/EUR153005625e_Cisco)
###  IDC MarketScape Recognizes Cisco as a Leader in North America IT Training Services and IT Training Services in Europe 
[Read the blog](https://blogs.cisco.com/learning/idc-marketscape-recognizes-cisco-as-a-leader-in-it-training-services)
* * *
Show more (1)
* * *
![Whether you have years of IT experience or are just starting your journey in the field, getting certified is a great way to boost your career. Cisco certifications are proof of knowledge, aptitude, and a lifelong learning mentality—and hiring managers know it.](https://www.cisco.com/content/dam/cisco-cdc/site/images/photography/learn/544/AdobeStock-1133032453-544x306.jpg)
##  Find success when you find your community. 
The Cisco Learning Network is buzzing with expert advice, training resources, cert prep material, and industry guidance to help you build a build a rewarding career or a stronger team through Cisco certifications. After all, it’s not just what you know, but who you know.
[Join the Cisco Learning Network](https://learningnetwork.cisco.com/s/)
## Partner role levels, specializations, and training
In addition to certifications for individual employees, Cisco's partner companies can qualify for role levels and specializations.
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/icons-and-shapes/partners/partner-index-icon-customer-64x64.png)
###  Partner role levels 
Partner role levels reflect the breadth of a partner organization’s skills across multiple technologies, and require partner specializations. Find the right role(s) and level(s) for your business.
[Learn more](https://www.cisco.com/site/us/en/partners/cisco-partner-program/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/icons-and-shapes/partners/icon-acknowledge.png)
###  Partner specializations 
Partner specializations reflect the depth of a partner organization’s expertise. They include required exams and recommended trainings for employees in various roles.
[Learn more](https://www.cisco.com/site/us/en/partners/cisco-partner-program/expertise/specializations/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/icons-and-shapes/partners/icon-enterprise-agreement.png)
###  Black Belt Academy 
An education framework for partners to become proficient in selling, deploying, and supporting Cisco’s latest technologies and software solutions.
[Learn more](https://www.cisco.com/site/us/en/partners/black-belt-academy/index.html)
* * *
Show more (1)
* * *
[Become a Cisco partner](https://id.cisco.com/signin/register) [Already a partner? Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/partners/index.html)
##  We’ll create a learning plan for you 
No matter what your team chooses to study, and how they choose to do it, training with Cisco means gaining a competitive advantage by staying in sync with tech innovations as your team evolves. Pick your products, certifications, or technologies, and the learning options that best fit your team. We’ll create a learning plan to match. 
[Let’s talk](https://mkto.cisco.com/training_contact_us.html)
1  _IDC MarketScape vendor analysis model is designed to provide an overview of the competitive fitness of technology and service suppliers in a given market. The research methodology utilizes a rigorous scoring methodology based on both qualitative and quantitative criteria that results in a single graphical illustration of each vendor's position within a given market. The Capabilities score measures vendor product, go-to-market and business execution in the short-term. The Strategy score measures alignment of vendor strategies with customer requirements in a 3-5-year timeframe. Vendor market share is represented by the size of the circles. Vendor year-over-year growth rate relative to the given market is indicated by a plus, neutral or minus next to the vendor name._
* * *
Show more (1)
* * *
###  Quick Links
  * [About Cisco](https://www.cisco.com/site/us/en/about/index.html)
  * [Contact Us](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=ftr-contactus)
  * [Careers](https://careers.cisco.com/global/en/home)
  * [Connect with a partner](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)


* * *
###  Resources and Legal
  * [Feedback](https://ciscocx.qualtrics.com/jfe/form/SV_bwrmeoKrBHYxOyW?Ref=/c/en/us/index.html)
  * [Help](https://www.cisco.com/c/en/us/about/help.html)
  * [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
  * [Privacy  
](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
  * [Cookies / Do not sell or share my personal data  
](https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies)
  * [Accessibility](https://www.cisco.com/c/en/us/about/accessibility.html)
  * [Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
  * [Supply Chain Transparency](https://www.cisco.com/c/dam/en_us/about/supply-chain/cisco-modern-slavery-statement.pdf)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)
  * [Sitemap](https://www.cisco.com/site/us/en/about/sitemap.html)


* * *
  * [ ](https://www.facebook.com/cisco/ "Facebook")
  * [ ](https://x.com/Cisco/ "X")
  * [ ](https://www.linkedin.com/company/cisco "LinkedIn")
  * [ ](https://www.youtube.com/user/cisco "YouTube")
  * [ ](https://www.instagram.com/cisco/ "Instagram")


© 2026 Cisco Systems, Inc.


---
# ORIGEN: https://www.cisco.com/c/en/us/training-events/events-webinars.html

  * [Skip to main content](https://www.cisco.com/site/us/en/learn/index.html#fw-c-content)
  * [Skip to search](https://www.cisco.com/site/us/en/learn/index.html#fw-c-header__button--search)
  * [Skip to footer](https://www.cisco.com/site/us/en/learn/index.html#fw-c-footer)


[ Cisco.com Worldwide ](https://www.cisco.com "Cisco.com Worldwide")
###  Products and Services
Back
Products and Services
Close
[ Products and Services Home](https://www.cisco.com/site/us/en/products/index.html)
###  Explore a better Wi-Fi 
Deliver fast, secure connectivity across every space. Simplify management and build an AI-ready network designed for growing demands. 
[Get started today](https://www.cisco.com/site/us/en/products/networking/wireless/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/wireless-hub-nav-284x164.jpg)
###  Cisco Security free trials 
Get started with the right security solution for you. Try out our security solutions before you buy them.
[Start a free trial](https://www.cisco.com/site/us/en/products/security/trials-offers.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/security-default-offer-card.jpg)
###  Discover Cisco IQ 
See more, move faster, go farther. Human expertise meets agentic intelligence in every Cisco Services engagement.
[Read the blog](https://blogs.cisco.com/news/cisco-iq-is-generally-available-heres-what-that-actually-means)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-cisco-iq.jpg)
  1. Networking
  2. Security
  3. Collaboration
  4. Computing
  5. Observability
  6. Software
  7. Services (CX)


Back
Networking
Close
## Products
  * [Switches](https://www.cisco.com/site/us/en/products/networking/switches/index.html)
  * [Routers](https://www.cisco.com/site/us/en/products/networking/sdwan-routers/index.html)
  * [Wireless](https://www.cisco.com/site/us/en/products/networking/wireless/index.html)
  * [Optics and transceivers](https://www.cisco.com/site/us/en/products/networking/optics-transceiver-modules/index.html)
  * [Silicon](https://www.cisco.com/site/us/en/products/networking/silicon-one/index.html)
  * [Networking software](https://www.cisco.com/site/us/en/products/networking/software/index.html)


[ Explore Networking](https://www.cisco.com/site/us/en/products/networking/index.html)
* * *
## Use cases
  * [Access networking](https://www.cisco.com/site/us/en/products/networking/access-networking/index.html)
  * [Campus and branch networking](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
  * [Data center and cloud networking](https://www.cisco.com/site/us/en/products/networking/cloud-networking/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/products/networking/industrial-iot/index.html)
  * [Internet, cloud, and endpoint visibility](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)
  * [Network security](https://www.cisco.com/site/us/en/products/networking/network-security/index.html)
  * [Service provider networking](https://www.cisco.com/site/us/en/solutions/service-provider/index.html)
  * [Wide-area networking (WAN)](https://www.cisco.com/site/us/en/products/networking/sdwan-routers/index.html)


* * *
###  Unified network management 
Manage your entire network from a single, intuitive cloud interface with the Meraki and Catalyst Center Global Overview. 
[Explore Networking Platform](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/products-services-networking.jpg)
Back
Security
Close
## Featured products
  * [AI Defense](https://www.cisco.com/site/us/en/products/security/ai-defense/index.html)
  * [Cisco Duo](https://duo.com/?utm_source=cisco&utm_medium=referral)
  * [Email Threat Defense](https://www.cisco.com/site/us/en/products/security/secure-email/index.html)
  * [Firewall](https://www.cisco.com/site/us/en/products/security/firewalls/index.html)
  * [Hypershield](https://www.cisco.com/site/us/en/products/security/hypershield/index.html)
  * [Identity Services Engine (ISE)](https://www.cisco.com/site/us/en/products/security/identity-services-engine/index.html)
  * [Secure Access (SSE)](https://www.cisco.com/site/us/en/products/security/secure-access/index.html)
  * [Splunk Enterprise Security](https://www.splunk.com/en_us/products/enterprise-security.html)
  * [XDR](https://www.cisco.com/site/us/en/products/security/xdr/index.html)


[ Explore Security](https://www.cisco.com/site/us/en/products/security/index.html)
* * *
## Use cases
  * [Agentic SOC](https://www.splunk.com/en_us/products/cyber-security.html)
  * [AI Security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [Hybrid Mesh Firewall](https://www.cisco.com/site/us/en/solutions/security/hybrid-mesh-firewall/index.html)
  * [Industrial security](https://www.cisco.com/site/us/en/products/security/industrial-security/index.html)
  * [Physical security](https://www.cisco.com/site/us/en/products/security/physical-security/index.html)
  * [Secure Access Service Edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Threat intelligence (Talos)](https://www.cisco.com/site/us/en/products/security/talos/index.html)
  * [Zero Trust Access](https://www.cisco.com/site/us/en/solutions/security/zero-trust-access/index.html)
  * [Zero trust for agentic AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/securing-agentic-ai/index.html)


* * *
###  Cisco Secure Access live demo 
Join us live to experience Cisco Secure Access—the smarter way to secure access to the internet, SaaS, and private apps.
[Choose an upcoming slot](https://www.cisco.com/c/en/us/products/security/secure-access/live-demo.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/security-secure-access-demo.jpg)
Back
Collaboration
Close
## Products
  * [Phones, headsets, and collaboration devices](https://www.cisco.com/c/en/us/products/collaboration-endpoints/index.html)
  * [Webex Customer Experience](https://www.webex.com/customer-experience)
  * [Webex Suite](https://www.webex.com/suite/collaboration-suite.html)


[ Explore Collaboration](https://www.cisco.com/site/us/en/products/collaboration/index.html)
* * *
## Use cases
  * [Workspaces](https://www.webex.com/us/en/workspaces.html)
  * [Return to the office](https://www.webex.com/us/en/solutions/return-to-office.html)
  * [Camera intelligence](https://www.webex.com/us/en/solutions/camera-intelligence-cisco-devices.html)
  * [Workspace management](https://www.webex.com/us/en/solutions/control-hub-cisco-devices.html)
  * [Devices for Microsoft Teams](https://www.webex.com/us/en/solutions/microsoft-teams-rooms-cisco-devices.html)
  * [Webex AI](https://www.webex.ai/)
  * [Control Hub](https://www.webex.com/us/en/solutions/cross-platform/control-hub.html)


###  Webex Suite 
Everything your business needs to collaborate—in the world’s first unified, purpose-built suite for hybrid work.
[Explore Webex Suite](https://www.webex.com/suite/collaboration-suite.html) [View the Webex site](https://www.webex.com/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/webex.jpg)
Back
Computing
Close
  * [Converged infrastructure](https://www.cisco.com/site/us/en/solutions/computing/converged-infrastructure/index.html)
  * [Fabric and adapters](https://www.cisco.com/site/us/en/products/computing/servers-unified-computing-systems/fabric-interconnects-extenders/index.html)
  * [Hybrid cloud operations](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)
  * [Hyperconverged infrastructure](https://www.cisco.com/site/us/en/products/computing/hyperconverged/nutanix/index.html)
  * [Servers](https://www.cisco.com/site/us/en/products/computing/servers-unified-computing-systems/index.html)
  * [Stack Automation by Quali](https://www.cisco.com/site/us/en/solutions/data-center/stack-automation-quali/index.html)
  * [Unified Edge](https://www.cisco.com/site/us/en/products/computing/unified-edge/index.html)


[ View all computing products](https://www.cisco.com/site/us/en/products/computing/index.html)
* * *
###  Cisco Intersight free trial 
Get simplified IT operations with infrastructure lifecycle management as a service to easily manage your Cisco UCS, converged, and hyperconverged infrastructure.
[Get started](https://www.cisco.com/c/en/us/solutions/cloud-computing/promotions-free-trials/intersight-free-trial.html) [Learn more about Intersight](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/computing-intersight.jpg)
Back
Observability
Close
## Products
  * [Cloud application security](https://www.cisco.com/site/us/en/products/security/cloud-application-security/index.html)
  * [Splunk Observability Cloud](https://www.splunk.com/en_us/products/observability-cloud.html)
  * [Splunk IT Service Intelligence](https://www.splunk.com/en_us/products/it-service-intelligence.html)
  * [ThousandEyes](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)


[ Explore Observability](https://www.cisco.com/site/us/en/products/observability/index.html)
* * *
## Use cases
  * [Alert noise reduction](https://www.splunk.com/en_us/solutions/alert-noise-reduction.html)
  * [Cloud monitoring optimization](https://www.splunk.com/en_us/solutions/extend-visibility-to-the-cloud.html)
  * [End-user experiences](https://www.splunk.com/en_us/solutions/optimize-your-web-and-mobile-experience.html)
  * [Microservices troubleshooting](https://www.splunk.com/en_us/solutions/isolate-cloud-native-problems.html)


###  Splunk Observability 
Get complete business visibility and real-time troubleshooting across any environment. 
[Explore Splunk Observability](https://www.splunk.com/en_us/products/observability.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/application-performance-appdynamics.jpg)
Back
Software
Close
## Networking
  * [Catalyst Center](https://www.cisco.com/site/us/en/products/networking/catalyst-center/index.html)
  * [Catalyst SD-WAN Manager](https://www.cisco.com/site/us/en/products/networking/wan/sd-wan-manager/index.html)
  * [IoT Operations Dashboard](https://www.cisco.com/c/en/us/support/cloud-systems-management/iot-operations-dashboard/series.html)
  * [Meraki Platform](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
  * [Mobility Services Platform](https://www.cisco.com/site/us/en/solutions/service-provider/networking/mobility-services-platform/index.html)
  * [Nexus Dashboard](https://www.cisco.com/site/us/en/products/networking/cloud-networking/nexus-platform/index.html)
  * [All networking software](https://www.cisco.com/site/us/en/products/networking/software/index.html)


* * *
## Security
  * [Cyber Vision](https://www.cisco.com/site/us/en/products/security/industrial-security/cyber-vision/index.html)
  * [Secure Equipment Access](https://www.cisco.com/site/us/en/products/security/industrial-security/secure-equipment-access/index.html)
  * [Security Cloud](https://www.cisco.com/site/us/en/products/security/security-cloud/index.html)


* * *
## Observability
  * [Splunk Observability](https://www.splunk.com/en_us/products/observability.html)
  * [ThousandEyes](https://www.cisco.com/site/us/en/products/networking/software/internet-cloud-intelligence/index.html)


* * *
## Collaboration
  * [Webex by Cisco](https://www.webex.com)


## Computing
  * [Intersight](https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/index.html)


* * *
  * [Explore Cisco buying programs](https://www.cisco.com/site/us/en/buy/enterprise-software-buying-program.html)
  * [Download software and manage licenses](https://software.cisco.com/)


[ View all software](https://www.cisco.com/site/us/en/products/software/index.html?filters=&search=&sort=a-z&filterby=&showMore=)
* * *
###  Free trials and demos 
View and sign up for over 100 products and portfolio solutions for free. 
[Explore trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/products-software-trials-demos.jpg)
Back
Services (CX)
Close
  * [Cisco Support](https://www.cisco.com/site/us/en/services/support/index.html)
  * [Cisco Professional Services](https://www.cisco.com/site/us/en/services/professional/index.html)
  * [Learn with Cisco](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


[ View all Cisco services](https://www.cisco.com/site/us/en/services/index.html)
* * *
###  Discover Cisco IQ 
See more, move faster, go farther. Human expertise meets agentic intelligence in every Cisco Services engagement.
[Read the blog](https://blogs.cisco.com/news/cisco-iq-is-generally-available-heres-what-that-actually-means)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-cisco-iq.jpg)
###  Get expert guidance 
Cisco Services can help you build the right solution for your needs with the combined power of AI, automation, and human expertise.
[Transform your data center](https://www.cisco.com/site/us/en/services/modern-data-center/index.html) [Build a better workplace](https://www.cisco.com/site/us/en/services/future-workplace/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/services-cx-promo-expert-guidance.jpg)
Close
###  Solutions
Back
Solutions
Close
[ Solutions Home](https://www.cisco.com/site/us/en/solutions/index.html)
###  Artificial intelligence 
Cisco has the infrastructure to power AI, unmatched breadth and scale of data to feed it, and a portfolio optimized to secure it. 
[Explore Cisco AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-ai.jpg)
###  Campus and branch 
Cisco brings together Al, automation, and security into one unified architecture—built to simplify operations, scale intelligently, and protect every connection.  

[Explore campus and branch](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-campus-branch.jpg)
###  Small and medium business 
Protect, connect, and empower your business with Cisco’s portfolio tailored to small and medium businesses. Experience simplified IT management, efficiency, cloud-driven flexibility, and 24/7 support. 
[Explore SMB solutions](https://www.cisco.com/site/us/en/solutions/small-business/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/solutions-smb.jpg)
  1. Artificial Intelligence
  2. Industries
  3. Technologies
  4. Campus and Branch
  5. Service Providers
  6. Small and Medium Business


Back
Artificial Intelligence
Close
  * [AI-enhanced security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [AI-native networking operations](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/netops.html)
  * [AI-ready data centers](https://www.cisco.com/site/us/en/about/why-cisco/ai-ready-data-centers/index.html)
  * [AI at the edge](https://www.cisco.com/site/us/en/solutions/data-center/ai-at-the-edge/index.html)
  * [AI networking in data centers](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/ai-networking-in-data-center/index.html)
  * [Mass-scale AI infrastructure](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/mass-scale-infrastructure/index.html)
  * [Secure AI Factory](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/secure-ai-factory/index.html)
  * [Splunk AI](https://www.splunk.com/en_us/solutions/splunk-artificial-intelligence.html)
  * [Webex AI](https://www.webex.ai/)


[ Cisco AI hub](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/index.html)
###  Cisco AI Assistant 
Cisco AI Assistant combines the latest generative AI technology with our expertise to responsibly guide and inform the decisions you make every day.
[Explore Cisco AI Assistant](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/ai-assistant/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/ai-assistant.jpg)
###  Cisco AI Readiness Assessment 
AI readiness comprises six pillars: Strategy, Infrastructure, Data, Governance, Talent, and Culture. Is your organization AI ready?
[Take assessment](https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index/assessment-tool.html) [Browse AI Readiness Index](https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/ai-readiness.jpg)
Back
Industries
Close
  * [Cities and Communities](https://www.cisco.com/c/en/us/solutions/industries/smart-connected-communities.html)
  * [Education](https://www.cisco.com/site/us/en/solutions/industries/education/index.html)
  * [Financial Services](https://www.cisco.com/site/us/en/solutions/industries/financial-services/index.html)
  * [Government](https://www.cisco.com/site/us/en/solutions/industries/government/index.html)
  * [Healthcare](https://www.cisco.com/site/us/en/solutions/industries/healthcare/index.html)
  * [Manufacturing](https://www.cisco.com/site/us/en/solutions/industries/manufacturing/index.html)
  * [Mining](https://www.cisco.com/site/us/en/solutions/industries/mining/index.html)


* * *
  * [Oil and Gas](https://www.cisco.com/site/us/en/solutions/industries/energy/oil-gas/index.html)
  * [Retail](https://www.cisco.com/site/us/en/solutions/industries/retail/index.html)
  * [Smart Buildings](https://www.cisco.com/site/us/en/solutions/smart-building/index.html)
  * [Sports, Media, and Entertainment](https://www.cisco.com/site/us/en/solutions/industries/sports-media-entertainment/index.html)
  * [Transportation](https://www.cisco.com/site/us/en/solutions/industries/transportation/index.html)
  * [Utilities](https://www.cisco.com/site/us/en/solutions/industries/energy/utilities/index.html)


[ View all industries](https://www.cisco.com/c/en/us/solutions/industries.html)
[ Industry design guides](https://www.cisco.com/c/en/us/solutions/design-zone/industries.html)
* * *
###  Discover the portfolio explorer 
Build the bridge between business outcomes and technology with our new interactive tool.
[Start exploring](https://www.cisco.com/c/m/en_us/solutions/industries/portfolio-explorer.html)
Back
Technologies
Close
## Networking
  * [Cloud and data center networking](https://www.cisco.com/site/us/en/products/networking/cloud-networking/index.html)
  * [Cloud-managed networking (Meraki)](https://www.cisco.com/site/us/en/products/networking/networking-cloud/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/index.html)
  * [Networking App Marketplace](https://marketplace.cisco.com/en-US/home)
  * [SD-WAN](https://www.cisco.com/site/us/en/solutions/networking/sdwan/index.html)
  * [Smart buildings](https://www.cisco.com/site/us/en/solutions/smart-building/index.html)
  * [All networking solutions](https://www.cisco.com/c/en/us/solutions/enterprise-networks/solution-listing.html)


## Computing
  * [Converged infrastructure](https://www.cisco.com/site/us/en/solutions/computing/converged-infrastructure/index.html)
  * [Hybrid cloud](https://www.cisco.com/site/us/en/solutions/computing/hybrid-cloud/index.html)
  * [Hyperconverged](https://www.cisco.com/site/us/en/products/computing/hyperconverged/nutanix/index.html)
  * [Stack Automation by Quali](https://www.cisco.com/site/us/en/solutions/data-center/stack-automation-quali/index.html)


* * *
## Security
  * [AI for security](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/index.html)
  * [Data center security](https://www.cisco.com/site/us/en/solutions/security/data-center-security/index.html)
  * [Hybrid Mesh Firewall](https://www.cisco.com/site/us/en/solutions/security/hybrid-mesh-firewall/index.html)
  * [Industrial security](https://www.cisco.com/site/us/en/products/security/industrial-security/index.html)
  * [Network security](https://www.cisco.com/site/us/en/products/networking/network-security/index.html)
  * [Secure Access Service Edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Secure Hybrid Work](https://www.cisco.com/site/us/en/solutions/security/secure-hybrid-work/index.html)
  * [Zero trust](https://www.cisco.com/site/us/en/solutions/security/zero-trust/index.html)
  * [Zero trust for agentic AI](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/security/securing-agentic-ai/index.html)


* * *
## Collaboration (Webex)
  * [Camera intelligence](https://www.webex.com/us/en/solutions/camera-intelligence-cisco-devices.html)
  * [Customer experience](https://www.webex.com/us/en/products/customer-experience.html)
  * [Event management](https://www.webex.com/us/en/products/suite/events.html)
  * [Intelligent workspaces](https://www.webex.com/us/en/workspaces.html)
  * [Interoperability](https://www.webex.com/us/en/solutions/interoperability.html)
  * [IT administration](https://www.webex.com/us/en/solutions/cross-platform/control-hub.html)
  * [Remote work](https://www.webex.com/suite/collaboration-suite.html)
  * [Workspace designer](https://designer.webex.com/)
  * [Workspace management](https://www.webex.com/us/en/solutions/control-hub-cisco-devices.html)


Back
Campus and Branch
Close
  * [Secure network architecture](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/index.html)
  * [Secure campus](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/secure-campus/index.html)
  * [Unified branch](https://www.cisco.com/site/us/en/solutions/networking/campus-branch-networking/unified-branch/index.html)
  * [Industrial IoT](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/index.html)
  * [Campus and branch design guides](https://www.cisco.com/c/en/us/solutions/design-zone/campus-branch.html)


* * *
Back
Service Providers
Close
## Empowering your infrastructure
  * [5G network architecture](https://www.cisco.com/c/en/us/solutions/service-provider/5g-network-architecture.html)
  * [Agile Services Networking](https://www.cisco.com/site/us/en/solutions/service-provider/networking/agile-services/index.html)
  * [Broadband solutions](https://www.cisco.com/site/us/en/solutions/service-provider/networking/broadband/index.html)
  * [Cable solutions](https://www.cisco.com/site/us/en/solutions/service-provider/industry/cable/index.html)
  * [Routed optical networking](https://www.cisco.com/site/us/en/solutions/routed-optical-networking/index.html)
  * [Routed PON](https://www.cisco.com/site/us/en/solutions/routed-pon/index.html)


[ View all service provider solutions](https://www.cisco.com/site/us/en/solutions/service-provider/index.html)
* * *
## Managed services
  * [Edge Cloud for Content Delivery](https://www.cisco.com/c/en/us/solutions/service-provider/telco-cloud/edge-cloud-for-content-delivery.html)
  * [IoT Control Center](https://www.cisco.com/site/us/en/products/networking/software/iot-control-center/index.html)
  * [Mobility Services Platform](https://www.cisco.com/site/us/en/solutions/service-provider/networking/mobility-services-platform/index.html)
  * [Private 5G](https://www.cisco.com/site/us/en/products/networking/wireless/private-5g/index.html)
  * [Secure access service edge (SASE)](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/index.html)
  * [Software-defined access](https://www.cisco.com/site/us/en/solutions/networking/sdaccess/index.html)
  * [Secure Hybrid Work](https://www.cisco.com/site/us/en/solutions/security/secure-hybrid-work/index.html)
  * [SD-WAN security](https://www.cisco.com/site/us/en/solutions/networking/sdwan/security/index.html)


* * *
###  Accelerate services offerings 
Provide outsourced IT and consulting services with a broad technology portfolio and robust partner support programs.
[See services options](https://www.cisco.com/site/us/en/partners/build-your-practice/managed-services/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/managed-services.jpg)
Back
Small and Medium Business
Close
## Products and solutions
  * [Networking](https://www.cisco.com/site/us/en/solutions/small-business/networking/index.html)
  * [Security](https://www.cisco.com/site/us/en/solutions/small-business/security/index.html)
  * [Collaboration](https://www.cisco.com/site/us/en/solutions/small-business/collaboration/index.html)
  * [Product selector](https://www.cisco.com/c/en/us/solutions/small-business/selector-tool.html)


[ View all small and medium business solutions](https://www.cisco.com/site/us/en/solutions/small-business/index.html)
[ Buy small and medium business products online](https://www.cisco.com/c/en/us/solutions/small-business/small-business-promotions-and-free-trials/buy-cisco-small-business-products-online.html)
* * *
###  Offers and free trials 
Find the best solutions for your needs and try them before you buy. 
[See all offers and free trials](https://www.cisco.com/site/us/en/solutions/small-business/trials-offers.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/smb-free-trials.jpg)
Close
###  Support
Back
Support
Close
[ Support Home](https://www.cisco.com/c/en/us/support/index.html)
###  Support home 
Access documentation, security notices, and support tools for Cisco products.
[View Cisco Support](https://www.cisco.com/c/en/us/support/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-home-penn1_brandlibrary-DSC0318.jpg)
###  Software downloads 
Download and manage new software, get updates or patches, or upgrade your current software to the latest release.
[View Software Central](https://software.cisco.com/download/home)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-software-downloads-hatchlibrary-general-gettyPA-Cisco-1309760275.jpg)
###  Licensing support 
Troubleshoot common licensing issues and leverage easy-to-follow documentation for both PAK-based or Smart Licenses.
[Get licensing support](https://www.cisco.com/c/en/us/support/licensing/licensing-support.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-licensing-hatchlibrary-security-gettyPA-Cisco-1518851638.jpg)
  1. Products and Downloads
  2. Documentation
  3. Contact Support
  4. Licenses and Contracts
  5. Tools and Resources
  6. Cisco Community


Back
Products and Downloads
Close
## Find products and downloads
Search field edit, type in text
Clear
[Downloads](https://www.cisco.com/site/us/en/learn/index.html#tabs-9da71fbd27-item-1288c79d71-tab) [Product Support](https://www.cisco.com/site/us/en/learn/index.html#tabs-9da71fbd27-item-1288c79d71-tab) [Technology Support](https://www.cisco.com/site/us/en/learn/index.html#tabs-9da71fbd27-item-1288c79d71-tab) | End of Sale End of Support
* [All Downloads](https://software.cisco.com/download/navigator.html)
* [All Products](https://www.cisco.com/c/en/us/support/all-products.html)
* Search all cisco.com
When autocomplete results are available use up and down arrows to review and enter to select
## Product Support
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Security](https://www.cisco.com/c/en/us/support/security/category.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Wireless](https://www.cisco.com/c/en/us/support/wireless/category.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Collaboration endpoints and phones](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Networking software (IOS and NX-OS)](https://www.cisco.com/c/en/us/support/ios-nx-os-software/index.html)
  * [Servers - Unified Computing (UCS)](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)


[ All products](https://www.cisco.com/c/en/us/support/all-products.html)
* * *
## Downloads
  * [Secure Client 5](https://software.cisco.com/download/home/286330811/type/282364313/release/)
  * [Identity Services Engine Software](https://software.cisco.com/download/home/283801620/type/283802505/)
  * [Secure Firewall Management Center Virtual](https://software.cisco.com/download/home/286259687/type)
  * [Smart Software Manager](https://software.cisco.com/download/home/286285506/type)
  * [Jabber for Windows](https://software.cisco.com/download/home/284324806/type/284006014/release/)
  * [Modeling Labs](https://software.cisco.com/download/home/286193282/type/286326381/release/2.7.2)
  * [Catalyst 9300 Series Switches](https://software.cisco.com/download/home/286313806)


[ All downloads](https://software.cisco.com/download/home)
* * *
Back
Documentation
Close
[ Technical documentation](https://www.cisco.com/c/en/us/docs/technical-documentation.html)
Configure, operate, and troubleshoot your Cisco products with configuration guides, installation guides, release notes, and more.
[ Trust Portal](https://trustportal.cisco.com/c/r/ctp/home.html)
Get self-service access to security, data privacy, and compliance documents.
* * *
[ Product documentation](https://www.cisco.com/c/en/us/products/a-to-z-series-index.html#all)
Explore Cisco products and features to empower your purchase with data sheets, white papers, end-of-life notices, and more.
* * *
Back
Contact Support
Close
## Product technical support (TAC)
[ Open a new case](https://mycase.cloudapps.cisco.com/case)
(Requires a product or software support contract)
  * [Manage support cases](https://mycase.cloudapps.cisco.com/case)
  * [Returns Portal (RMAs)](https://www.cisco.com/c/en/us/support/returns/returns-portal.html)


* * *
Enterprise and Service Provider products
**1-800-553-2447** US and Canada
[ Worldwide phone numbers](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)
* * *
Small and medium business products
**1-866-606-1866** US and Canada
[ Worldwide phone numbers](https://www.cisco.com/c/en/us/support/web/tsd-cisco-small-business-support-center-contacts.html)
Back
Licenses and Contracts
Close
## Software licenses
  * [Explore key licensing resources](https://www.cisco.com/site/us/en/buy/licensing/index.html)
  * [Download and manage licenses](https://software.cisco.com/)
  * [Manage assets and entitlements](https://software.cisco.com/clc/access-directory)
  * [Troubleshoot license issues](https://www.cisco.com/c/en/us/support/licensing/licensing-support.html)


## Cisco Enterprise Agreement (EA)
  * [Manage Cisco EA licenses](https://software.cisco.com/software/ea/agreements)
  * [Learn about Cisco EA](https://www.cisco.com/site/us/en/buy/enterprise-agreement/index.html)


* * *
## Product support contracts
  * [Manage and renew service contracts (CCW-R)](https://ccrc.cisco.com/ccwr/)


###  Cisco Licensing Hub 
Enhance your Cisco licensing experience. 
[Access now](https://www.cisco.com/site/us/en/buy/licensing/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/support-licensing-hub.jpg)
Back
Tools and Resources
Close
## Tools
  * [Bug Search Tool](https://bst.cisco.com/bugsearch/?referring_site=shp)
  * [My Devices](https://cway.cisco.com/mydevices)
  * [My Saved Content](https://www.cisco.com/c/en/us/support/saved/index.html)
  * [Software Research](https://software.cisco.com/research/home)
  * [Device Coverage Checker](https://cway.cisco.com/sncheck/)


[ All Support tools](https://www.cisco.com/c/en/us/support/web/tools-catalog.html)
* * *
## Notifications and advisories
  * [My Notifications](https://cway.cisco.com/mynotifications)
  * [Security Advisories](https://sec.cloudapps.cisco.com/security/center/publicationListing.x)
  * [Field Notices](https://www.cisco.com/c/en/us/support/web/tsd-products-field-notice-summary.html)
  * [Cisco Cloud Status](https://www.cisco.com/c/en/us/support/web/cloud-status.html)


### Services
  * [All Cisco Services](https://www.cisco.com/site/us/en/services/index.html)


## Technology adoption
  * [Cisco Customer Success](https://www.cisco.com/c/m/en_us/customer-experience/customer-success/index.html)


Back
Cisco Community
Close
## Community forums
  * [Technology and Support](https://community.cisco.com/t5/technology-and-support/ct-p/technology-support)
  * [Small Business Support](https://community.cisco.com/t5/small-business-support-community/ct-p/5541-small-business-support)
  * [Developers](https://community.cisco.com/t5/devnet/ct-p/4409j-developer-home)
  * [Partners](https://community.cisco.com/t5/partner-hub/ct-p/2002j-partner-home)
  * [Project Gallery](https://community.cisco.com/t5/project-gallery/con-p/customer-success-stories)
  * [Cisco Insider User Group](https://community.cisco.com/t5/cisco-insider-user-group/ct-p/ccp-home)


[ Explore Cisco Community](https://community.cisco.com/)
* * *
###  Community events and webinars 
Learn from Cisco experts and engage with peers in webinars and live events.
[View all events and webinars](https://community.cisco.com/t5/technology-and-support-events-and-webinars/eb-p/ts-events-webinars-bd)
Close
###  Learn
Back
Learn
Close
[ Learn Home](https://www.cisco.com/site/us/en/learn/index.html)
###  Cisco U. 
Access training tailored to your needs. Work toward a specific role or certification, deploy or support a technology solution, or enhance your career progress.
[Learn more about Cisco U. ](https://www.cisco.com/site/us/en/learn/training-certifications/training/ciscou/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-cisco-u.jpg)
###  Cisco Networking Academy 
If you're a student, start at Cisco Networking Academy. With free courses and career guidance, your next IT job is closer than you think.
[Join now](https://www.netacad.com/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-netacad.jpg)
###  Events 
Join us to take advantage of the latest networking opportunities with Cisco customers, partners, employees, and subject-matter experts.
[Explore now](https://www.cisco.com/site/us/en/learn/events/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/events-calendar-default.jpg)
  1. Training and Certifications
  2. Events
  3. Webinars
  4. Technology Learning Topics
  5. Learning Resources and Assets


Back
Training and Certifications
Close
## Learning
  * [Cisco Networking Academy](https://www.netacad.com)
  * [Cisco U. ](https://u.cisco.com)
  * [Instructor-led training](https://learninglocator.cloudapps.cisco.com/#/home)
  * [Cisco Modeling Labs](https://www.cisco.com/site/us/en/learn/training-certifications/training/modeling-labs/index.html)
  * [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer)
  * [Join our community](https://learningnetwork.cisco.com/s/)
  * [Learn with Cisco blog](https://blogs.cisco.com/learning)


[ Learn with Cisco overview](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)
* * *
## Certifications
  * [Career certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
  * [Learn about exams](https://www.cisco.com/site/us/en/learn/training-certifications/exams/index.html)
  * [Continuing Education (CE credits)](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/continuing-education/index.html)
  * [Recertification](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/recertification/index.html)
  * [Schedule an exam](https://cp.certmetrics.com/cisco/en/schedule/schedule-exam)
  * [Track my certifications](https://cp.certmetrics.com/cisco/en/credentials/status)


* * *
## Training for organizations
  * [Enterprise](https://www.cisco.com/site/us/en/learn/training-certifications/enterprise-training/index.html)
  * [Cisco Learning Credits](https://www.cisco.com/site/us/en/learn/training-certifications/training/learning-credits/index.html)
  * [Training catalog](https://www.cisco.com/site/us/en/learn/training-certifications/training/training-catalog/index.html)
  * [Partners](https://www.cisco.com/site/us/en/learn/training-certifications/partner-resources.html)


## Support
  * [Learn with Cisco support bot](https://certsupport.cisco.com/s/?language=en_US)


Back
Events
Close
  * [Cisco Live](https://www.ciscolive.com/home/en/index.html?cid=cdc-hp-nav-home#xd_co_f)
  * [Partner events calendar](https://salesconnect.cisco.com/americaspartnercommunity/s/enablement-training-calendar)


[ View all events](https://www.cisco.com/site/us/en/learn/events/index.html)
* * *
###  Cisco Live 2026 Melbourne 
Experience the education, inspiration, and fun of Cisco Live 2026 Melbourne.
[Register now](https://www.ciscolive.com/apjc?ccid=cc008775&cid=CL26eventspage&eid=162820&oid=eprsas033263)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/cl2026-cisco-live-las-vegas.jpg)
###  Watch Cisco Live sessions on demand 
View sessions from Las Vegas in our On-Demand Library. Keynotes, Deep Dives, and Center Stage sessions are available now, with the remaining sessions added by June 19.
[Watch now](https://www.ciscolive.com/on-demand/on-demand-library.html?cid=cdc-hp-nav&utm_team=global_events&utm_medium=email&utm_source=sendgrid&utm_campaign=xb_cxp_fy26q4_amer_20260623past&ccid=cc007720&dtid=oemrft001460&utm_eid=95796&search.event=1769534158486002QYqy#/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/cl2026-cisco-live-las-vegas.jpg)
Back
Webinars
Close
## Trending webinars
  * [AI readiness for data centers](https://experiences.cisco.com/amer/ai-readiness-for-data-centers)
  * [Simplify IT with SD-WAN](https://experiences.cisco.com/amer/simplify-it-with-sd-wan)
  * [Security transformation with Cisco XDR](https://cloudsecurity.cisco.com/webinar-security-transformation-with-cisco-xdr)


[ View all webinars](https://experiences.cisco.com/amer?pf_route=1&groups=all-webinars)
* * *
###  McLaren Racing + Cisco 
Carrie Palin joins McLaren Racing F1 team CEO Zak Brown and driver Oscar Piastri as they unveil the high-tech secrets behind their team's successful 2024 season.
[Watch on demand](https://experiences.cisco.com/amer/cisco-mclaren-innovation-speed)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-webinars-mclaren-racing.jpg)
###  Cisco webinars 
Discover insights that shape the future of technology. Our webinars feature experts and leaders sharing how organizations transform to connect, grow, and succeed.
[Explore webinars](https://experiences.cisco.com/amer?pf_route=1&group=all-webinars&groups=all-webinars)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/learn-webinars.jpg)
Back
Technology Learning Topics
Close
  * [How to set up a router](https://www.cisco.com/site/us/en/learn/topics/small-business/how-to-set-up-router.html)
  * [What is cybersecurity?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-cybersecurity.html)
  * [What is a firewall?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-firewall.html)
  * [What is Industry 4.0?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-industry-4-0.html)
  * [What is IoT (Internet of Things)?](https://www.cisco.com/site/us/en/learn/topics/industrial-iot/what-is-iot.html)
  * [What is Wi-Fi 7?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-wi-fi-7.html)


* * *
  * [What is AIOps?](https://www.cisco.com/site/us/en/learn/topics/artificial-intelligence/what-is-aiops.html)
  * [What is cloud security?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-cloud-security.html)
  * [What is hybrid cloud?](https://www.cisco.com/site/us/en/learn/topics/computing/what-is-hybrid-cloud.html)
  * [What is SASE?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-secure-access-service-edge-sase.html)
  * [What is software as a service (SaaS)?](https://www.cisco.com/site/us/en/learn/topics/software/what-is-software-as-a-service-saas.html)


[ View all technology learning topics](https://www.cisco.com/site/us/en/learn/topics/index.html)
* * *
###  2026 State of Industrial AI 
We surveyed more than 1000 industrial professionals on securing operations, advancing IT/OT collaboration, and building an AI-ready network that can scale.
[Get report](https://www.cisco.com/site/us/en/solutions/networking/industrial-iot/industrial-networking-report/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/state-of-industrial-ai-284x164.jpg)
Back
Learning Resources and Assets
Close
## Sandboxes and simulators
  * [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer)
  * [DevNet Sandbox](https://developer.cisco.com/site/sandbox/)
  * [Cisco Modeling Labs](https://developer.cisco.com/modeling-labs/)
  * [Cisco Learning Labs](https://u.cisco.com/store/lab?type=cisco-learning-labs)


## News and insights
  * [Blogs](https://blogs.cisco.com/)
  * [Cisco Community](https://community.cisco.com/)
  * [Executive perspectives](https://www.cisco.com/c/en/us/solutions/executive-perspectives/index.html)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)


* * *
## Developer resources
  * [Getting started with DevNet](https://developer.cisco.com/startnow/)
  * [DevNet Tracks](https://developer.cisco.com/learning/search/?contentType=track&page=1)
  * [Python training](https://www.cisco.com/site/us/en/learn/training-certifications/training/courses/prne.html)
  * [Code exchange](https://developer.cisco.com/codeexchange/)
  * [Developer community](https://community.cisco.com/t5/devnet/ct-p/4409j-developer-home)


## Videos and live streams
  * [Cisco Video Portal](https://video.cisco.com/)


* * *
## Architecture and design resources
  * [Cisco Validated](https://www.cisco.com/site/us/en/solutions/cisco-validated/index.html)
  * [Visio stencils](https://www.cisco.com/c/en/us/products/visio-stencil-listing.html)


## Additional resources
  * [Cisco Learning Credits](https://www.cisco.com/site/us/en/learn/training-certifications/training/learning-credits/index.html)
  * [Cisco Multicloud training](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/multicloud/index.html)
  * [Black Belt Academy (for partners)](https://www.cisco.com/site/us/en/partners/training/black-belt-academy/index.html)


Close
###  Why Cisco
Back
Why Cisco
Close
[ Why Cisco](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
###  Why Cisco 
Cisco creates the infrastructure you need to transform how you connect, protect, and innovate in the AI era.
[See the Cisco advantage](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-ai-blue.jpg)
###  Our Purpose 
We Power an Inclusive Future for All.
[Explore our Purpose](https://www.cisco.com/site/us/en/about/purpose/index.html) [Read FY25 Purpose Report](https://www.cisco.com/c/dam/m/en_us/about/purpose/reporting-hub/_pdf/purpose-report-2025.pdf)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-purpose.jpg)
###  Success stories 
Discover how Cisco technologies drive real-world success for our customers and power Cisco's own operations and innovation. 
[Explore customer stories](https://www.cisco.com/site/us/en/about/case-studies-customer-stories/index.html) [How we use our technology](https://www.cisco.com/site/us/en/solutions/cisco-on-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-success-stories.jpg)
  1. Outcomes We Deliver
  2. Working with Partners
  3. About Us


Back
Outcomes We Deliver
Close
[ AI-ready data centers](https://www.cisco.com/site/us/en/about/why-cisco/ai-ready-data-centers/index.html)
Unleash the power of AI with data centers designed for speed, scale, and agility.
[ Future-proofed workplaces](https://www.cisco.com/site/us/en/about/why-cisco/future-proofed-workplaces/index.html)
Elevate employee and customer experiences with agile, resilient workplaces.
[ Digital resilience](https://www.cisco.com/site/us/en/about/why-cisco/digital-resilience/index.html)
Achieve always-on resilience with trusted security, observability, and assurance.
* * *
###  Why Cisco 
Cisco creates the infrastructure you need to transform how you connect, protect, and innovate in the AI era.
[See the Cisco advantage](https://www.cisco.com/site/us/en/about/why-cisco/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-ai-blue.jpg)
Back
Working with Partners
Close
[ Why choose Cisco partners](https://www.cisco.com/site/us/en/partners/evolved-partner-ecosystem/index.html)
Learn how our partner ecosystem makes it easier than ever to identify the partners to best meet your needs. ​ 
[ Frequently asked questions (PDF)](https://www.cisco.com/c/dam/en_us/partners/cisco-partner-designations-faq.pdf)
Access answers to your questions about the evolution of Cisco's partner ecosystem and new partner designations. 
[ Find a partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
Explore our partner ecosystem today. 
* * *
###  A new way to find partners 
The Cisco Partner Locator tool has been transformed into an AI-driven hub to match, recommend, and activate partners for every customer outcome.​ 
[Explore what's new](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/partner-locator-curve.jpg)
Back
About Us
Close
  * [Overview](https://www.cisco.com/site/us/en/about/index.html)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)
  * [Leadership](https://newsroom.cisco.com/c/r/newsroom/en/us/executives.html)
  * [Purpose and sustainability](https://www.cisco.com/site/us/en/about/purpose/index.html)
  * [Career opportunities](https://careers.cisco.com/global/en/home)
  * [The Trust Center](https://www.cisco.com/c/en/us/about/trust-center.html)
  * [Investor relations](https://investor.cisco.com/overview/default.aspx)


[ Contact us](https://www.cisco.com/site/us/en/about/contact-cisco/index.html)
* * *
###  How to buy 
Browse options to purchase Cisco products, services, and software offerings.
[Visit how-to-buy hub](https://www.cisco.com/site/us/en/buy/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/header/why-cisco-how-to-buy.jpg)
Close
###  Partners
Close
[ Trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html?linkclickid=hdr-mainnav-trialsdemos)
[ How to buy](https://www.cisco.com/site/us/en/buy/index.html?linkclickid=hdr-utilnav-howtobuy)
Partners
EN US
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/learn/index.html)
[ Trials and demos](https://www.cisco.com/site/us/en/products/trials-demos.html?linkclickid=hdr-mainnav-trialsdemos)
MENU
CLOSE
[ How to buy](https://www.cisco.com/site/us/en/buy/index.html?linkclickid=hdr-utilnav-howtobuy)
Partners
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/learn/index.html)
EN US
Search field edit, type in text
Clear Speech-to-Text Search Search
* * *
Speech-to-Text Powered By Google Speech API
We didn't hear that. Try again.
Speech-to-Text Search is currently unavailable
  * [Downloads](https://software.cisco.com/download/home)
  * [Certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
  * [Cisco Validated](https://www.cisco.com/c/en/us/solutions/cisco-validated.html)
  * [Training](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)
  * [Community](https://community.cisco.com/)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)


Close
**For Partners**
[Partners Home](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129)
[Partner Program](https://www.cisco.com/site/us/en/partners/index.html?ccid=cc000864&dtid=odiprc001129)
[Support](https://www.cisco.com/site/us/en/partners/support-help/index.html?dtid=odiprc001129)
[Tools](https://www.cisco.com/site/us/en/partners/tools-training/index.html?dtid=odiprc001129)
**Already a Partner?**
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/learn/index.html)
* * *
[Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/ "Find a Cisco Partner")
* * *
[Learn about Partners](https://www.cisco.com/site/us/en/partners/evolved-partner-ecosystem/index.html)
* * *
[Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129 "Become a Cisco Partner")
Close
[ Log in](https://www.cisco.com/content/cdc/login.html?referer=/site/us/en/learn/index.html)
Don't have an account? [Sign up](https://id.cisco.com/signin/register "Sign up")
Close
Back
Country | Language
Close
Selected country/region:
United States
  * [English](https://www.cisco.com/site/us/en/index.html)


  1. All Countries / Regions
  2. North America
  3. Africa
  4. Asia Pacific
  5. Europe
  6. Greater China
  7. Latin America
  8. Middle East


  * United States
    * [English](https://www.cisco.com/site/us/en/index.html)
  * Africa
    * [English](https://www.cisco.com/site/dz/en/index.html)
    * [Français](https://www.cisco.com/site/dz/fr/index.html)
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * Argentina
    * [Español](https://www.cisco.com/site/ar/es/index.html)
  * Australia & New Zealand
    * [English](https://www.cisco.com/site/au/en/index.html)
  * Austria
    * [Deutsch](https://www.cisco.com/site/at/de/index.html)
  * Belgium & Luxembourg
    * [English](https://www.cisco.com/site/be/en/index.html)
    * [Français](https://www.cisco.com/site/be/fr/index.html)
    * [Nederlands](https://www.cisco.com/site/be/nl/index.html)
  * Brazil
    * [Português](https://www.cisco.com/site/br/pt/index.html)
  * Canada
    * [English](https://www.cisco.com/site/ca/en/index.html)
    * [Français](https://www.cisco.com/site/ca/fr/index.html)
  * Caribbean
    * [Español](https://www.cisco.com/site/bz/es/index.html)
  * Chile
    * [Español](https://www.cisco.com/site/cl/es/index.html)
  * Colombia
    * [Español](https://www.cisco.com/site/co/es/index.html)
  * Costa Rica
    * [Español](https://www.cisco.com/site/cr/es/index.html)
  * Czech Republic
    * [Čeština](https://www.cisco.com/site/cz/cs/index.html)
  * Denmark
    * [Dansk](https://www.cisco.com/site/dk/da/index.html)
  * Ecuador
    * [Español](https://www.cisco.com/site/ec/es/index.html)
  * Egypt
    * [English](https://www.cisco.com/site/eg/en/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * France
    * [Français](https://www.cisco.com/site/fr/fr/index.html)
  * Germany
    * [Deutsch](https://www.cisco.com/site/de/de/index.html)
  * Hong Kong
    * [English](https://www.cisco.com/site/hk/en/index.html)
    * [繁體中文](https://www.cisco.com/site/hk/zh/index.html)
  * Hungary
    * [Magyar](https://www.cisco.com/site/hu/hu/index.html)
  * India
    * [English](https://www.cisco.com/site/in/en/index.html)
  * Indonesia
    * [English](https://www.cisco.com/site/id/en/index.html)
  * Israel
    * [English](https://www.cisco.com/site/il/en/index.html)
  * Italy
    * [Italiano](https://www.cisco.com/site/it/it/index.html)
  * Japan
    * [日本語](https://www.cisco.com/site/jp/ja/index.html)
  * Korea
    * [한국어](https://www.cisco.com/site/kr/ko/index.html)
  * Mainland China
    * [简体中文](https://www.cisco.com/site/cn/zh/index.html)
  * Malaysia
    * [English](https://www.cisco.com/site/my/en/index.html)
  * Mexico
    * [Español](https://www.cisco.com/site/mx/es/index.html)
  * Middle East
    * [English](https://www.cisco.com/site/ae/en/index.html)
    * [عربي](https://www.cisco.com/site/ae/ar/index.html)
  * Netherlands
    * [Nederlands](https://www.cisco.com/site/nl/nl/index.html)
  * Norway
    * [Norsk](https://www.cisco.com/site/no/no/index.html)
  * Panama
    * [Español](https://www.cisco.com/site/pa/es/index.html)
  * Peru
    * [Español](https://www.cisco.com/site/pe/es/index.html)
  * Philippines
    * [English](https://www.cisco.com/site/ph/en/index.html)
  * Poland
    * [Polski](https://www.cisco.com/site/pl/pl/index.html)
  * Portugal
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
  * Romania
    * [Română](https://www.cisco.com/site/ro/ro/index.html)
  * Singapore
    * [English](https://www.cisco.com/site/sg/en/index.html)
  * South Africa
    * [English](https://www.cisco.com/site/za/en/index.html)
  * Spain
    * [Español](https://www.cisco.com/site/es/es/index.html)
  * Sweden
    * [Svenska](https://www.cisco.com/site/se/sv/index.html)
  * Switzerland
    * [Français](https://www.cisco.com/site/ch/fr/index.html)
    * [Deutsch](https://www.cisco.com/site/ch/de/index.html)
  * Taiwan
    * [繁體中文](https://www.cisco.com/site/tw/zh/index.html)
  * Thailand
    * [ภาษาไทย](https://www.cisco.com/site/th/th/index.html)
  * Turkey
    * [Türkçe](https://www.cisco.com/site/tr/tr/index.html)
  * Ukraine
    * [Українська ](https://www.cisco.com/site/ua/uk/index.html)
    * [Русский](https://www.cisco.com/site/ua/ru/index.html)
  * United Kingdom & Ireland
    * [English](https://www.cisco.com/site/uk/en/index.html)
  * Vietnam
    * [Việt](https://www.cisco.com/site/vn/vi/index.html)


  * Canada
    * [English](https://www.cisco.com/site/ca/en/index.html)
    * [Français](https://www.cisco.com/site/ca/fr/index.html)
  * United States
    * [English](https://www.cisco.com/site/us/en/index.html)


  * Africa
    * [English](https://www.cisco.com/site/dz/en/index.html)
    * [Français](https://www.cisco.com/site/dz/fr/index.html)
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * Egypt
    * [English](https://www.cisco.com/site/eg/en/index.html)
    * [عربي](https://www.cisco.com/site/eg/ar/index.html)
  * South Africa
    * [English](https://www.cisco.com/site/za/en/index.html)


  * Australia & New Zealand
    * [English](https://www.cisco.com/site/au/en/index.html)
  * India
    * [English](https://www.cisco.com/site/in/en/index.html)
  * Indonesia
    * [English](https://www.cisco.com/site/id/en/index.html)
  * Japan
    * [日本語](https://www.cisco.com/site/jp/ja/index.html)
  * Korea
    * [한국어](https://www.cisco.com/site/kr/ko/index.html)
  * Malaysia
    * [English](https://www.cisco.com/site/my/en/index.html)
  * Philippines
    * [English](https://www.cisco.com/site/ph/en/index.html)
  * Singapore
    * [English](https://www.cisco.com/site/sg/en/index.html)
  * Thailand
    * [ภาษาไทย](https://www.cisco.com/site/th/th/index.html)
  * Vietnam
    * [Việt](https://www.cisco.com/site/vn/vi/index.html)


  * Austria
    * [Deutsch](https://www.cisco.com/site/at/de/index.html)
  * Belgium & Luxembourg
    * [English](https://www.cisco.com/site/be/en/index.html)
    * [Français](https://www.cisco.com/site/be/fr/index.html)
    * [Nederlands](https://www.cisco.com/site/be/nl/index.html)
  * Czech Republic
    * [Čeština](https://www.cisco.com/site/cz/cs/index.html)
  * Denmark
    * [Dansk](https://www.cisco.com/site/dk/da/index.html)
  * France
    * [Français](https://www.cisco.com/site/fr/fr/index.html)
  * Germany
    * [Deutsch](https://www.cisco.com/site/de/de/index.html)
  * Hungary
    * [Magyar](https://www.cisco.com/site/hu/hu/index.html)
  * Israel
    * [English](https://www.cisco.com/site/il/en/index.html)
  * Italy
    * [Italiano](https://www.cisco.com/site/it/it/index.html)
  * Netherlands
    * [Nederlands](https://www.cisco.com/site/nl/nl/index.html)
  * Norway
    * [Norsk](https://www.cisco.com/site/no/no/index.html)
  * Poland
    * [Polski](https://www.cisco.com/site/pl/pl/index.html)
  * Portugal
    * [Português](https://www.cisco.com/site/pt/pt/index.html)
  * Romania
    * [Română](https://www.cisco.com/site/ro/ro/index.html)
  * Spain
    * [Español](https://www.cisco.com/site/es/es/index.html)
  * Sweden
    * [Svenska](https://www.cisco.com/site/se/sv/index.html)
  * Switzerland
    * [Français](https://www.cisco.com/site/ch/fr/index.html)
    * [Deutsch](https://www.cisco.com/site/ch/de/index.html)
  * Turkey
    * [Türkçe](https://www.cisco.com/site/tr/tr/index.html)
  * Ukraine
    * [Українська ](https://www.cisco.com/site/ua/uk/index.html)
    * [Русский](https://www.cisco.com/site/ua/ru/index.html)
  * United Kingdom & Ireland
    * [English](https://www.cisco.com/site/uk/en/index.html)


  * Hong Kong
    * [English](https://www.cisco.com/site/hk/en/index.html)
    * [繁體中文](https://www.cisco.com/site/hk/zh/index.html)
  * Mainland China
    * [简体中文](https://www.cisco.com/site/cn/zh/index.html)
  * Taiwan
    * [繁體中文](https://www.cisco.com/site/tw/zh/index.html)


  * Argentina
    * [Español](https://www.cisco.com/site/ar/es/index.html)
  * Brazil
    * [Português](https://www.cisco.com/site/br/pt/index.html)
  * Caribbean
    * [Español](https://www.cisco.com/site/bz/es/index.html)
  * Chile
    * [Español](https://www.cisco.com/site/cl/es/index.html)
  * Colombia
    * [Español](https://www.cisco.com/site/co/es/index.html)
  * Costa Rica
    * [Español](https://www.cisco.com/site/cr/es/index.html)
  * Ecuador
    * [Español](https://www.cisco.com/site/ec/es/index.html)
  * Mexico
    * [Español](https://www.cisco.com/site/mx/es/index.html)
  * Panama
    * [Español](https://www.cisco.com/site/pa/es/index.html)
  * Peru
    * [Español](https://www.cisco.com/site/pe/es/index.html)


  * Middle East
    * [English](https://www.cisco.com/site/ae/en/index.html)
    * [عربي](https://www.cisco.com/site/ae/ar/index.html)


Close
Close
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/heroes/learn/learn-home-hero-3200x762.jpg)
#  Learn 
Skill up with training and career certifications, catch up on the latest perspectives through events and webinars, and find helpful tools and resources.
Hello, how can I help?
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/photography/lifestyle-photography/learn/learn-home-training.jpg)
###  Learn with Cisco 
Whether you’re looking to advance your career, uplevel your day-to-day work, or help your team accomplish a learning goal, Learn with Cisco has you covered.
[Explore Learn with Cisco](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/photography/lifestyle-photography/learn/learn-home-events-750x422.png)
###  Events 
Take advantage of the latest networking opportunities with Cisco customers, partners, employees, and subject-matter experts. 
[See events calendar](https://www.cisco.com/site/us/en/learn/events/index.html)
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/photography/lifestyle-photography/learn/learn-home-webinars.jpg)
###  Webinars and videos 
Join us for upcoming webinars or watch on-demand replays about Cisco products and solutions.
[Browse webinars](https://experiences.cisco.com/)
* * *
Show more (1)
* * *
![](https://www.cisco.com/content/dam/cisco-cdc/site/images/photography/lifestyle-photography/learn/learn-home-cisco-certifications-spotlight-800x450.jpg)
##  Cisco certifications: Your gateway to IT excellence 
Align yourself with the best of the best. Cisco certifications are the recognized gold standard with more than four million certifications issued to date. They bring significant value to individuals and the organizations that employ them—and employers know it. Grow your skill set and career with Cisco. 
[Explore Cisco certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
## Popular ways to learn
Learning
###  Cisco Networking Academy 
Find your place in tech and build foundational skills with beginner-friendly, career-focused content—for free.
[Explore Cisco Networking Academy](https://www.netacad.com/)
Learning
###  Cisco U. 
Take the next step in your career with the technology learning experience shaped around your goals. 
[Discover Cisco U.](https://www.cisco.com/site/us/en/learn/training-certifications/training/ciscou/index.html)
Event
###  Cisco Live 
Join us in person, digitally, or on demand to be inspired, discover technical education on a variety of topics, and learn how Cisco will help you connect, protect, and thrive in the AI-driven world.
[Explore Cisco Live](https://www.ciscolive.com?cid=cdc-learn-link&utm_team=global_events&utm_medium=&utm_campaign=xb_cxp_fy26q2_amer_cdc-promo&ccid=cc007720&dtid=odicdc000509&eid=95796&)
Webinar
###  The AI-Ready Blueprint: Future-Proofing Networks for the Agentic Era 
Join Cisco experts Sanjay Kapoor and Grant Shirk to explore how AI is reshaping enterprise networks. See new tools like AI Canvas and AI Assistant in action, and learn how companies like Nestlé are modernizing with Cisco SD-WAN and AI. Get ready for the future of networking—today.
[Watch webinar](https://experiences.cisco.com/amer/the-ai-ready-blueprint-future-proofing-networks-for-the-agentic-era?enableLocalTime=true)
* * *
Show more (1)
* * *
## Technology learning topics
Build your knowledge and learn about the topics that interest you most with the Cisco glossary. 
###  What is a hybrid mesh firewall?
A hybrid mesh firewall unifies security across data centers, clouds, and edge locations.
[Learn about hybrid mesh firewalls](https://www.cisco.com/site/us/en/learn/topics/security/what-is-hybrid-mesh-firewall.html)
###  What is an AI data center?
AI data centers are specialized facilities with vast computational power to handle complex workloads.
[Learn about AI data centers](https://www.cisco.com/site/us/en/learn/topics/computing/what-is-an-ai-data-center.html)
###  What is agentic operations?
AgenticOps is an agent-first IT operating model built for autonomous action with oversight.
[Learn about AgenticOps](https://www.cisco.com/site/us/en/learn/topics/artificial-intelligence/what-is-agentic-operations-agenticops.html)
###  What is Wi-Fi 7?
Wi-Fi 7 represents the next generation of wireless networking technology – aiming to enhance performance, speed, and efficiency.
[Learn about Wi-Fi 7](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-wi-fi-7.html)
###  How to set up a router
Though every router is different, we describe the basic steps that should be common to all router setups.
[Walk through router setup steps](https://www.cisco.com/site/us/en/learn/topics/small-business/how-to-set-up-router.html)
[See all technology learning topics](https://www.cisco.com/site/us/en/learn/topics/index.html)
## Additional learning resources
### Learn with Cisco
  * [Cisco Certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)
  * [Certification exams](https://www.cisco.com/site/us/en/learn/training-certifications/exams/index.html)
  * [Certification tracking (CertMetrics)](https://cp.certmetrics.com/cisco/en/login)
  * [Individual learning](https://www.cisco.com/site/us/en/learn/training-certifications/training/index.html)
  * [Cisco Learning Locator (ILT)](https://learninglocator.cloudapps.cisco.com/)
  * [Enterprise training](https://www.cisco.com/site/us/en/learn/training-certifications/enterprise-training/index.html)
  * [Training catalog](https://www.cisco.com/site/us/en/learn/training-certifications/training/training-catalog/index.html)
  * [Cisco Learning Network](https://learningnetwork.cisco.com/s/)
  * [Cisco Learning Partner program](https://www.cisco.com/site/us/en/learn/training-certifications/training/learning-partner-program/index.html)


### Events
  * [Events calendar](https://www.cisco.com/site/us/en/learn/events/index.html)
  * [Partner events (Cisco.com login required)](https://www.cisco.com/c/en/us/partners/amer-events.html)


### Webinars and videos
  * [Cisco Video Portal](https://video.cisco.com/)
  * [Global webinars](https://experiences.cisco.com/)
  * [Influencer hub](https://www.cisco.com/c/en/us/training-events/events-webinars/influencer-hub.html)
  * [Technology and Support Events and Webinars](https://community.cisco.com/t5/technology-and-support-events-and-webinars/eb-p/ts-events-webinars-bd)
  * [Cisco on YouTube](https://www.youtube.com/user/cisco)


### News and insights
  * [Cisco Blogs](https://blogs.cisco.com/)
  * [Cisco Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)
  * [Cisco Research](https://research.cisco.com/)
  * [Cisco Talos blog](https://blog.talosintelligence.com/)
  * [Outshift by Cisco Blog](https://outshift.cisco.com/blog)


### Architecture, design, and developer resources
  * [Cisco Insider](https://www.cisco.com/site/us/en/about/cisco-insider/index.html)
  * [Cisco Validated](https://www.cisco.com/site/us/en/solutions/cisco-validated/index.html)
  * [DevNet](https://developer.cisco.com)
  * [Packet tracer](https://www.netacad.com/cisco-packet-tracer)
  * [Visio stencils](https://www.cisco.com/c/en/us/products/visio-stencil-listing.html)


* * *
Show more (1)
* * *
##  Ask the community 
The Cisco Community is a hub for connecting with your peers and Cisco specialists to ask for help, share your expertise, build your network, and grow professionally.
[Join the conversation](https://community.cisco.com/)
###  Quick Links
  * [About Cisco](https://www.cisco.com/site/us/en/about/index.html)
  * [Contact Us](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=ftr-contactus)
  * [Careers](https://careers.cisco.com/global/en/home)
  * [Connect with a partner](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)


* * *
###  Resources and Legal
  * [Feedback](https://ciscocx.qualtrics.com/jfe/form/SV_bwrmeoKrBHYxOyW?Ref=/c/en/us/index.html)
  * [Help](https://www.cisco.com/c/en/us/about/help.html)
  * [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
  * [Privacy  
](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
  * [Cookies / Do not sell or share my personal data  
](https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies)
  * [Accessibility](https://www.cisco.com/c/en/us/about/accessibility.html)
  * [Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
  * [Supply Chain Transparency](https://www.cisco.com/c/dam/en_us/about/supply-chain/cisco-modern-slavery-statement.pdf)
  * [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)
  * [Sitemap](https://www.cisco.com/site/us/en/about/sitemap.html)


* * *
  * [ ](https://www.facebook.com/cisco/ "Facebook")
  * [ ](https://x.com/Cisco/ "X")
  * [ ](https://www.linkedin.com/company/cisco "LinkedIn")
  * [ ](https://www.youtube.com/user/cisco "YouTube")
  * [ ](https://www.instagram.com/cisco/ "Instagram")


© 2026 Cisco Systems, Inc.


---
# ORIGEN: https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html

  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Meeting Server API Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html) to Save Content 
Print
### Available Languages
Updated:June 16, 2021
Document ID:1623860928202823
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Meeting Server API Denial of Service Vulnerability
Medium
Advisory ID: 
cisco-sa-meetingserver-dos-NzVWMMQT
First Published:
2021 June 16 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvx32184](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx32184)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html)
CVE-2021-1524
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html)
CVSS Score:
[ Base 4.3](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L/E:X/RL:X/RC:X
CVE-2021-1524
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-meetingserver-dos-NzVWMMQT/csaf/cisco-sa-meetingserver-dos-NzVWMMQT.json)
Email 
## 
Summary 
  * A vulnerability in the API of Cisco Meeting Server could allow an authenticated, remote attacker to cause a denial of service (DoS) condition on an affected device.
This vulnerability exists because requests that are sent to the API are not properly validated. An attacker could exploit this vulnerability by sending a malicious request to the API. A successful exploit could allow the attacker to cause all participants on a call to be disconnected, resulting in a DoS condition.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-meetingserver-dos-NzVWMMQT>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected Cisco Meeting Server releases 3.1 and 3.1.1.
See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html#vp) section of this advisory are known to be affected by this vulnerability.


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, Cisco Meeting Server releases 3.1.2 and later contained the fix for this vulnerability.
See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * This vulnerability was found during internal security testing.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-meetingserver-dos-NzVWMMQT>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2021-JUN-16  |  
Show Less


* * *
## 
Legal Disclaimer 
  * THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME.
A standalone copy or paraphrase of the text of this document that omits the distribution URL is an uncontrolled copy and may lack important information or contain factual errors. The information in this document is intended for end users of Cisco products.


## 
Feedback 
  * [Leave additional feedback](javascript:openNewWindow\(\);)


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-meetingserver-dos-NzVWMMQT.html "Back to Top")
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


---
# ORIGEN: https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html

  * [Skip to content](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


  * [](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html)
  * [Products & Services](https://www.cisco.com/c/en/us/products/index.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/products/servers-unified-computing/index.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-c-series-rack-servers/index.html)
  * [White Papers](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-c-series-rack-servers/white-paper-listing.html)


# AI Performance: MLPerf Training on Cisco UCS C880A M8 Rack Server with NVIDIA B300 SXM GPUs White Paper
White Paper
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.pdf) (6.0 MB)   
View with Adobe Reader on a variety of devices


Updated:July 23, 2026
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Contact Cisco
  * Contact Cisco
  * [Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)
  * Call Sales: [ 1-800-553-6387 ](tel:18005536387)   
US/CAN | 5am-5pm PT 
  * [Product / Technical Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.pdf) (6.0 MB)   
View with Adobe Reader on a variety of devices


Updated:July 23, 2026
#### Table of Contents
![Open Search](https://www.cisco.com/content/dam/eotToc/search-white_28x28.png)
![Close Search](https://www.cisco.com/content/dam/eotToc/close_11x11.png)
#### Table of Contents
  * [Executive summary](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Executivesummary "Executivesummary")
  * [Scope of this document](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Scopeofthisdocument "Scopeofthisdocument")
  * [Product overview](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Productoverview "Productoverview")
    * [Accelerated compute](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Acceleratedcompute "Acceleratedcompute")
  * [Prominent features](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Prominentfeatures "Prominentfeatures")
    * [Unleashing AI potential with NVIDIA HGX B300 SXM GPU](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#UnleashingAIpotentialwithNVIDIAHGXB300SXMGPU "UnleashingAIpotentialwithNVIDIAHGXB300SXMGPU")
    * [Comprehensive enterprise AI manageability](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#ComprehensiveenterpriseAImanageability "ComprehensiveenterpriseAImanageability")
    * [Purpose-built for AI and HPC workloads](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#PurposebuiltforAIandHPCworkloads "PurposebuiltforAIandHPCworkloads")
  * [Scalable network fabric for AI connectivity](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#ScalablenetworkfabricforAIconnectivity "ScalablenetworkfabricforAIconnectivity")
  * [AI-cluster network design](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#AIclusternetworkdesign "AIclusternetworkdesign")
    * [Rail-optimized network design](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Railoptimizednetworkdesign "Railoptimizednetworkdesign")
  * [MLPerf overview](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#MLPerfoverview "MLPerfoverview")
  * [MLPerf Training](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#MLPerfTraining "MLPerfTraining")
  * [MLPerf Training test configuration](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#MLPerfTrainingtestconfiguration "MLPerfTrainingtestconfiguration")
  * [MLPerf Training performance results](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#MLPerfTrainingperformanceresults "MLPerfTrainingperformanceresults")
    * [MLPerf Training benchmarks](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#MLPerfTrainingbenchmarks "MLPerfTrainingbenchmarks")
  * [MLPerf Training 6.0 performance data](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#MLPerfTraining60performancedata "MLPerfTraining60performancedata")
    * [Llama2_70b_lora](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Llama270blora "Llama270blora")
    * [Llama3.1_8b](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Llama318b "Llama318b")
    * [Gpt-oss-120b](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Gptoss120b "Gptoss120b")
  * [MLPerf Training 6.0 multinode performance data](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#MLPerfTraining60multinodeperformancedata "MLPerfTraining60multinodeperformancedata")
    * [Llama2_70b_lora](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Llama270blora "Llama270blora")
    * [Llama3.1_8b](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Llama318b "Llama318b")
    * [Performance summary](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Performancesummary "Performancesummary")
  * [Appendix: Test environment](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#AppendixTestenvironment "AppendixTestenvironment")
  * [For more information](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.html#Formoreinformation "Formoreinformation")


Executive summary
With generative AI (GenAI) poised to significantly boost global economic output, Cisco is helping to simplify the challenges of preparing organizations’ infrastructure for AI implementation. The exponential growth of AI is transforming data-center requirements, driving demand for scalable, accelerated computing infrastructure.
The Cisco UCS® C880A M8 Rack Server is a dense-GPU server designed to deliver scalable accelerated compute capabilities to address the most demanding AI workloads, including deep Learning / Large Language Model (LLM) training, model fine-tuning, large model inferencing, and Retrieval-Augmented Generation (RAG). The Cisco UCS C880A M8 Rack Server offers 8 NVIDIA HGX B300 tensor core GPUs to deliver massive, accelerated compute performance in a single server, as well as one NVIDIA ConnectX-8 SuperNIC per GPU to scale AI model training across a cluster of dense-GPU servers.
To help demonstrate the AI performance capacity of the new Cisco UCS C880A M8 Rack Server, MLPerf Benchmarking performance testing for Training 6.0 was conducted by Cisco using NVIDIA HGX B300 (SXM) GPUs as detailed later in this document.
Scope of this document
For the MLPerf Benchmarking performance testing for Training 6.0 focuses on evaluating performance using 8x NVIDIA B300 SXM GPUs configured on a Cisco UCS C880A M8 Rack Server. The training benchmark results were collected for various datasets to help understand the performance benefits of the UCS C880A M8 server with NVIDIA B300 GPUs for training workloads. This white paper highlights performance data for MLPerf Training 6.0 on selected datasets to provide a quick understanding of the Cisco UCS C880A M8 Rack Server's performance in this context.
This aligns with Cisco's approach to showcasing how its UCS C880A M8 server, equipped with advanced NVIDIA B300 SXM GPUs and Intel® Xeon® 6th-Gen CPUs, delivers high throughput and efficiency for AI training workloads, including large language model training and other AI-native data center applications.
Key points include the following:
●Performance evaluation using 8x NVIDIA B300 SXM GPUs on the Cisco UCS C880A M8 Rack Server
●Collection of training benchmark results across various datasets
◦The data used in these tests serves to illustrate the performance benefits of this server and GPU configuration for training workloads.
◦The white paper provides a concise overview of performance for selected datasets to aid quick understanding. 
This summary reflects the scope as described in the relevant Cisco documentation and blog content about MLPerf benchmarking and the UCS C880A M8 platform with NVIDIA B300 SXM GPUs.
Product overview
Based on the NVIDIA HGX platform, the Cisco UCS C880A M8 Rack Server is a high-density, air-cooled rack server designed to power the most demanding artificial intelligence (AI) and High-Performance Computing (HPC) workloads. It integrates the NVIDIA HGX platform with eight NVIDIA B300 SXM GPUs and is powered by two Intel Xeon 6th Gen processors, making it ideal for real-time large language model inference, next-level inference performance, and large-volume data processing. The UCS C880A M8 supports customers across the entire AI stack, from large-scale model inference and fine-tuning to real-time inferencing and large-volume data processing. It integrates seamlessly into Cisco’s AI strategy, connecting and protecting the AI era by providing robust compute infrastructure. This server expands the Cisco UCS-dense AI server portfolio, offering a powerful solution for enterprises across various industries, including service providers, financial services, manufacturing, healthcare, life sciences, and automotive. With its advanced architecture, the UCS C880A M8 ensures unparalleled performance, scalability, and enterprise manageability, making it ideal for compute-intensive AI use cases such as large-scale AI model inference, fine tuning, and inferencing. 
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_0.png)](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_0.png "Related image, diagram or screenshot")
Figure 1. 
Cisco UCS C880A M8 Rack Server views with product specifications 
Refer to the data sheet for the [Cisco UCS C880A M8 Rack Server](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c880a-m8-rack-server-ds.html).
Accelerated compute
A typical AI journey starts with inference GenAI models with large amounts of data to build the model intelligence. For this important stage, the new Cisco UCS C880A M8 Rack Server is a powerhouse designed to tackle the most demanding AI-Inference tasks. The UCS C880A M8 provides the raw computational power necessary for handling massive data sets and complex algorithms. Moreover, its simplified deployment and streamlined management make it easier than ever for enterprise customers to embrace AI. 
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_1.png)](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_1.png "Related image, diagram or screenshot")
Figure 2. 
Exploded view of the Cisco UCS C880A Rack Server 
Prominent features
Unleashing AI potential with NVIDIA HGX B300 SXM GPU
The Cisco UCS C880A M8 Rack Server stands out by integrating the cutting-edge NVIDIA HGX platform with eight NVIDIA B300 (SXM) GPUs. This powerful GPU configuration is at the heart of its capability to deliver next-level performance for the most demanding AI workloads, including large-scale AI model inference, fine-tuning, and real-time inferencing. The B300 GPUs provide immense parallel processing capabilities and high-speed GPU interconnects, which are critical for accelerating complex deep-learning models and large language models. This integration ensures that enterprises can achieve higher token throughput and improve the economics of their AI operations, enabling profitable scaling of LLM and agentic workloads.
Comprehensive enterprise AI manageability
The Cisco UCS C880A M8 Rack Server is designed for enterprise readiness. In a future release, the UCS C880A M8 will enable management through Cisco Intersight®.
Cisco Intersight provides a cloud-based management platform that simplifies server lifecycle management, offering capabilities such as power operations, extensive monitoring metrics, server configuration management, and firmware bundle release management. This centralized control and observability streamlines AI infrastructure operations, reduces complexity, and ensures consistent policy enforcement across the data center. 
Purpose-built for AI and HPC workloads
Beyond raw power, the Cisco UCS C880A M8 Rack Server is architected specifically to meet the unique demands of AI and HPC. Its design supports real-time large language model Inference, enabling rapid deployment and responsiveness for AI-driven applications. It also excels in next-level inference performance, significantly reducing the time required to train complex AI models. Furthermore, its capacity for large-volume data processing makes it an ideal platform for data-science and big-data analytics, including GPU-accelerated ETL processes. This specialized design ensures that organizations can build, optimize, and utilize AI models efficiently, accelerating business growth with scalable and high-performance solutions.
Scalable network fabric for AI connectivity
**Network fabric: Cisco Nexus 9000 Series Switches and Nexus Dashboard**
In distributed inference, training, and fine-tuning, the network fabric plays a crucial role in providing high-bandwidth, low-latency communication to interconnect dense-GPU servers such as the UCS C880A and the Cisco UCS C845A rack servers. Cisco Nexus® 9000 Series Switches are designed to meet these demanding requirements, serving as the high-performance foundation for both the leaf and spine layers of the backend and frontend fabrics in the architecture.
The Cisco AI POD architecture leverages the following key platforms:
●**Cisco Nexus 9332D-GX2B:** a 1RU, 32-port 400GbE switch based on Cisco Cloud Scale technology, ideally suited for leaf role
●**Cisco Nexus 9364D-GX2A:** a 2RU, 64-port 400GbE switch based on Cisco Cloud Scale technology, ideally suited for larger leaf or spine roles 
●**Cisco Nexus 9364E-SG2:** a 2RU, 64-port 800GbE (or 128 x 400GbE ports) switch based on Cisco® Silicon One® technology. Designed for next-generation fabrics, it is available in QSFP-DD and OSFP form factors with dual-port transceivers for 400GbE connectivity, making it suitable for both leaf and spine roles.
All these Nexus switches provide the port density, switching capacity, and advanced features necessary for AI/ML workloads, including support for RDMA over Converged Ethernet (RoCE), hardware-accelerated telemetry, and advanced load-balancing mechanisms.
For more information, refer to the following design guide: “[Cisco AI POD for Enterprise and Fine-Tuning Design Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/UCS_CVDs/cisco_ai_pod_for_training_design.html)”.
AI-cluster network design
An AI cluster typically has multiple networks — an inter-GPU backend network, a frontend network, a storage network, and an out-of-band (OOB) management network.
Figure 3 shows an overview of these networks. Users (in the corporate network in the figure) and applications (in the data-center network) reach the GPU nodes through the frontend network. The GPU nodes access the storage nodes through a storage network, which, in Figure 3, has been converged with the frontend network. A separate OOB management network provides access to the management and console ports on switches, BMC ports on the servers, and power distribution units (PDUs). A dedicated inter-GPU backend network connects the GPUs in different nodes for transporting remote direct memory access (RDMA) traffic while running a distributed job.
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_2.png)](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_2.png "Related image, diagram or screenshot")
Figure 3. 
AI-cluster network design
**For more information, refer to the following white paper:** “[Cisco Nexus 9000 Series Switches for AI Clusters White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/nexus-9000-series-switches-ai-clusters-wp.html)”.
Rail-optimized network design
GPUs in a scalable unit are interconnected using a rail-optimized design to improve collective communication performance by allowing single-hop forwarding through the leaf switches, without the traffic going to the spine switches. In rail-optimized design, port 1 on all the GPU nodes connects to the first leaf switch, port 2 connects to the second leaf switch, and so on.
The acceleration of AI is fundamentally changing our world and creating new growth drivers for organizations, such as improving productivity and business efficiency while achieving sustainability goals. Scaling infrastructure for AI workloads is more important than ever to realize the benefits of these new AI initiatives. IT departments are being asked to step in and modernize their data-center infrastructure to accommodate these new demanding workloads.
AI projects go through different phases: training your model, fine-tuning it, and then deploying the model to end users. Each phase has different infrastructure requirements. Training and inference are the most compute-intensive phase, and large language models, deep learning, natural language processing (NLP), and digital twins require significant accelerated compute.
**For more information, refer to the following white paper: “**[**Cisco Data Center Networking Solutions: Addressing the Challenges of AI/ML Infrastructure**](https://www.cisco.com/c/en/us/td/docs/dcn/whitepapers/cisco-addressing-ai-ml-network-challenges.html)**”**.
MLPerf overview
MLPerf is a benchmark suite designed to evaluate the performance of machine-learning software, hardware, and services. It is developed by MLCommons, a consortium of AI leaders from academia, research labs, and industry. The primary goal of MLPerf is to provide an objective and standardized yardstick for assessing machine-learning platforms and frameworks.
MLPerf includes multiple benchmarks, notably:
●MLPerf Training: measures the time required to train machine-learning models to a specified accuracy level
●MLPerf Inference: Datacenter: measures how quickly a trained neural network can perform inference tasks on new data
MLPerf Training
The MLPerf Training benchmark suite measures how fast systems can train models to a target quality-metric. Current and previous results can be reviewed through the results dashboard given in the ML Commons link: <https://mlcommons.org/benchmarks/training/>.
This [MLPerf Training Benchmark paper](https://arxiv.org/pdf/1910.01500.pdf) provides a detailed description of the motivation and guiding principles behind the MLPerf Training benchmark suite. 
MLPerf Training test configuration
For the MLPerf Training 6.0 performance testing covered in this document, the Cisco UCS C880A M8 Rack Server was configured with:
●8x NVIDIA B300 SXM GPUs
MLPerf Training performance results
MLPerf Training benchmarks
The MLPerf Training models listed in Table 1 were configured on the Cisco UCS C880A M8 Rack Server and tested for performance. 
**Table 1.** MLPerf Training models  
|  Model  |  Reference implementation model  |  Description  |  
| --- | --- | --- |  
|  **Llama2-70b**  |  [language/llama2-70b](https://github.com/mlcommons/inference/tree/master/language/llama2-70b)  |  Large language model with 70 billion parameters. It is designed for natural language processing (NLP) tasks and answering questions.  |  
|  **Llama3.1-8b**  |  [language/llama3.1_8b](https://github.com/mlcommons/inference/tree/master/language/llama3.1-405b)  |  Open-source, lightweight, and ultra-fast large language model designed to efficiently handle a wide variety of multilingual text generation and natural language processing tasks  |  
|  **GPT–OSS-120b**  |  [language/gpt-oss-120b](https://github.com/mlcommons/inference/tree/master/language/gpt-oss-120b)  |  Open-source or open-weight implementations inspired by GPT. Used to make powerful language models accessible to developers and researchers without requiring closed commercial APIs.  |  
MLPerf Training 6.0 performance data
As part of the MLPerf Training 6.0 submission, Cisco has tested most of the datasets mentioned in Table 1 on the Cisco UCS C880A M8 Rack Server and submitted the results to MLCommons with NVIDIA B300 GPUs. The results are published on the MLCommons results page: <https://mlcommons.org/benchmarks/training/>.
Cisco has also published performance data for MLPerf Training 6.0 with multinode configurations. Two Cisco UCS C880A M8 Rack Servers were configured with 16x NVIDIA B300 GPUs. Performance data with two nodes is provided in Figures 7 and 8 below.
Llama2_70b_lora 
Llama2_70b_lora is a large language model from Meta, with 70 billion parameters. It is designed for various natural language processing tasks such as text generation, summarization, translation, and question answering. 
Figure 4 shows the MLPerf 6.0 Training performance of the llama2_70b_lora model tested on a Cisco UCS C880A M8 Rack Server with 8x NVIDIA B300 GPUs.
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_3.png)](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_3.png "Related image, diagram or screenshot")
Figure 4. 
Llama2_70b_lora performance data on a Cisco UCS C880A M8 Rack Server with 8 x NVIDIA B300 GPUs 
Llama3.1_8b 
Llama 3.1_8b is an open-source, lightweight, and ultra-fast large language model developed by Meta AI. It contains 8 billion parameters and is designed to efficiently handle a wide variety of multilingual text generation and natural language processing tasks. 
Figure 5 shows the MLPerf Training 6.0 performance of the Retinanet model tested on Cisco UCS C880A M8 Rack Server with 8x NVIDIA B300 GPUs.
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_4.png)](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_4.png "Related image, diagram or screenshot")
Figure 5. 
Llama3.1_8b performance data on a Cisco UCS C880A M8 Rack Server with 8 x NVIDIA B300 GPUs 
Gpt-oss-120b
Gpt-oss-120b generally refers to open-source or open-weight implementations inspired by the GPT (Generative Pre-trained Transformer) architecture. The term is often used by the AI community to describe projects that aim to provide GPT-like language models with openly available code and/or weights.
Figure 6 shows the MLPerf Training 6.0 performance of the gpt-oss-20b model tested on a Cisco UCS C880A M8 Rack Server with 8x NVIDIA B300 GPUs.
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_5.png)](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_5.png "Related image, diagram or screenshot")
Figure 6. 
Gpt-oss-120b performance data on a Cisco UCS C880A M8 Rack Server with 8 x NVIDIA B300 GPUs 
MLPerf Training 6.0 multinode performance data
MLPerf Training multinode testing evaluates how efficiently systems can train machine-learning models across multiple interconnected computing nodes. This benchmarking suite, developed by MLCommons, aims to provide standardized metrics for comparing the performance of various hardware, software, and services in the context of distributed machine learning. 
The benchmarks are continuously evolving to include new and emerging AI workloads, such as generative AI (GenAI), and MLPerf results highlight the importance of dedicated low-latency interconnects between GPUs in multi-GPU systems for optimal distributed deep-learning training. Training models on multiple nodes introduces complexities, primarily due to communication overhead between nodes. To achieve efficient scaling, several technologies and optimizations are employed, such as RDMA (remote direct memory access), that are crucial for optimizing cross-node GPU-to-GPU communication and distributing training jobs efficiently. Distributed training frameworks and libraries such as NCCL (NVIDIA Collective Communications Library) are commonly used for distributed training and efficient communication across GPUs and nodes.
Llama2_70b_lora 
Llama2_70b_lora is a large language model from Meta, with 70 billion parameters. It is designed for various natural language processing tasks such as text generation, summarization, translation, and question answering. 
Figure 7 shows the single-node and multi-node configuration for MLPerf 6.0 Training performance of the llama2_70b_lora model tested on a Cisco UCS C880A M8 Rack Server with 8x and 16x NVIDIA B300 GPUs. 
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_6.png)](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_6.png "Related image, diagram or screenshot")
Figure 7. 
Multinode llama2_70b_lora performance data on a Cisco UCS C880A M8 Rack server with 8x and 16x NVIDIA B300 GPUs 
Llama3.1_8b 
Developed by Meta AI, llama 3.1_8b is a lightweight, high-performance open-source large language model. With 8 billion parameters, it is engineered for efficient multilingual text generation and a broad range of natural language processing tasks.
Figure 8 shows MLPerf 6.0 Training performance for the llama 3.1_8b model, evaluated across both single-node and multinode configurations on the Cisco UCS C880A M8 Rack Server, utilizing 8x and 16x NVIDIA B300 GPUs. 
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_7.png)](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/mlperf-b300-training-ucs-c880a-m8-rs-wp.docx/_jcr_content/renditions/mlperf-b300-training-ucs-c880a-m8-rs-wp_7.png "Related image, diagram or screenshot")
Figure 8. 
Multinode llama3.1_8b performance data on a Cisco UCS C880A M8 Rack Server with 8x and 16x NVIDIA B300 GPUs 
Performance summary 
The Cisco UCS C880A M8 Rack Server, powered by the NVIDIA HGX platform, provides the high-performance compute necessary for the most demanding AI workloads. By combining robust performance with simplified deployment, the platform enables organizations to accelerate time-to-value for their AI initiatives.
Cisco’s commitment to AI excellence is further demonstrated through its collaborative MLPerf Training submissions with NVIDIA. These benchmarks validate optimized performance and efficiency across a wide spectrum of AI applications, including large language models, natural language processing, image classification, object detection, and graph classification.
The Cisco UCS C880A M8 platform has demonstrated industry-leading AI performance in the MLPerf Training 6.0 benchmark. Key highlights include:
●Llama2_70b_lora: delivered leadership performance in both single-node and multinode configurations utilizing 8x and 16x NVIDIA B300 SXM GPUs
●Llama3.1_8b: achieved top-tier results in a multinode configuration equipped with 16x NVIDIA B300 SXM GPUs.
These results underscore the exceptional capabilities of the Cisco UCS portfolio for demanding AI training workloads.
Appendix: Test environment
Table 2 lists the details of the server under test-environment conditions. 
**Table 2.** Server properties  
|  Description  |  Value  |  
| --- | --- |  
|  **Product name**  |  Cisco UCS C880A M8 Rack Server  |  
|  **CPU**  |  2x Intel Xeon 6th Gen 6776P Processor   |  
|  **Number of cores**  |  64  |  
|  **Number of threads**  |  128  |  
|  **Total memory**  |  4 TB  |  
|  **Memory DIMMs (16)**  |  32x 128GB DDR5 RDIMM   |  
|  **Memory speed**  |  6400 MHz  |  
|  **Network adapter**  |  ●8x GPU-board integrated NVIDIA ConnectX-8  ●2x NVIDIA ConnectX-7 (2x200G)  ●1x Intel X710-T2L OCP   |  
|  **GPU controllers**  |  NVIDIA B300 SXM 8-GPU  |  
|  **SFF NVMe SSDs**  |  Up to 8x PCIe Gen5 x4 E1.S NVMe SSD   |  
**Note:** Platform-default BIOS settings were applied during the MLPerf Training validation. 
For more information
For additional information on the Cisco UCS C880A M8 Rack Server, refer to: <https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c880a-m8-rack-server-spec-sheet.pdf>.
Cisco UCS C880A M8 Rack Server Data Sheet: <https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c880a-m8-rack-server-ds.html>.
Cisco AI-Ready Data Center Infrastructure: <https://blogs.cisco.com/datacenter>.
Cisco AI PODs At-a-Glance: <https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ai-pods-aag.html>.
Cisco AI-Native Infrastructure for Data Center: <https://www.cisco.com/site/us/en/solutions/artificial-intelligence/infrastructure/index.html>.
### Our experts recommend
  * [Cisco UCS C845A M8 Rack Server At a Glance](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c845a-m8-rack-server-aag.html "Cisco UCS C845A M8 Rack Server At a Glance")
  * [Cisco UCS Servers with Intel Xeon 6 CPUs FAQ](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/intel-xeon-6-cpu-faq.html "Cisco UCS Servers with Intel Xeon 6 CPUs FAQ")


### Learn more


---
# ORIGEN: https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html

  * [Skip to content](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


  * [](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html)
  * [Products & Services](https://www.cisco.com/c/en/us/products/index.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/products/servers-unified-computing/index.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-c-series-rack-servers/index.html)
  * [White Papers](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-c-series-rack-servers/white-paper-listing.html)


# AI Performance: MLPerf Training on   
Cisco UCS C885A M8 HGX Platform with NVIDIA GPUs White Paper
White Paper
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.pdf) (2.5 MB)   
View with Adobe Reader on a variety of devices


Updated:January 20, 2026
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Contact Cisco
  * Contact Cisco
  * [Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)
  * Call Sales: [ 1-800-553-6387 ](tel:18005536387)   
US/CAN | 5am-5pm PT 
  * [Product / Technical Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.pdf) (2.5 MB)   
View with Adobe Reader on a variety of devices


Updated:January 20, 2026
#### Table of Contents
![Open Search](https://www.cisco.com/content/dam/eotToc/search-white_28x28.png)
![Close Search](https://www.cisco.com/content/dam/eotToc/close_11x11.png)
#### Table of Contents
  * [Executive summary](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#Executivesummary "Executivesummary")
  * [Introduction](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#Introduction "Introduction")
  * [Benefits of Cisco UCS servers](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#BenefitsofCiscoUCSservers "BenefitsofCiscoUCSservers")
  * [Scope of this document](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#Scopeofthisdocument "Scopeofthisdocument")
  * [Product overview](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#Productoverview "Productoverview")
  * [MLPerf overview](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#MLPerfoverview "MLPerfoverview")
  * [MLPerf Training](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#MLPerfTraining "MLPerfTraining")
  * [MLPerf Training: Test configuration](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#MLPerfTrainingTestconfiguration "MLPerfTrainingTestconfiguration")
  * [MLPerf Training performance results](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#MLPerfTrainingperformanceresults "MLPerfTrainingperformanceresults")
  * [MLPerf Training 5.1 performance data](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#MLPerfTraining51performancedata "MLPerfTraining51performancedata")
  * [MLPerf Training 5.1 multi-node performance data](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#MLPerfTraining51multinodeperformancedata "MLPerfTraining51multinodeperformancedata")
  * [Appendix: Test environment](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#AppendixTestenvironment "AppendixTestenvironment")
  * [For more information](https://www.cisco.com/c/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.html#Formoreinformation "Formoreinformation")


Executive summary
With generative AI poised to significantly boost global economic output, Cisco is helping to simplify the challenges of preparing organizations’ infrastructure for AI implementation. The exponential growth of AI is transforming data-center requirements, driving demand for scalable, accelerated computing infrastructure. 
To this end, Cisco recently introduced the Cisco UCS C885A M8 Rack Server, a high-density GPU server designed for demanding AI workloads, offering powerful performance for model training, deep learning, and inference. Built on the NVIDIA HGX platform, it can scale out to deliver clusters of computing power that will bring your most ambitious AI projects to life. Each server includes NVIDIA Network Interface Cards (NICs) or SuperNICs to accelerate AI networking performance, as well as NVIDIA BlueField-3 Data Processing Units (DPUs) to accelerate GPU access to data and enable robust, zero-trust security. The new Cisco UCS C885A M8 is Cisco’s first entry into its dedicated AI server portfolio and its first eight-way accelerated computing system built on the NVIDIA HGX platform. 
To help demonstrate the AI performance capacity of the new Cisco UCS C885A M8 Rack Server, MLPerf benchmarking performance testing for Training 5.1 was conducted by Cisco, using NVIDIA H200 GPUs, as detailed later in this document. 
Accelerated compute 
A typical AI journey starts with training GenAI models with large amounts of data to build the model intelligence. For this important stage, the new Cisco UCS C885A M8 Rack Server is a powerhouse designed to tackle the most demanding AI training tasks. With its high-density configuration of NVIDIA H200 Tensor Core GPUs, coupled with the efficiency of NVIDIA HGX architecture, the UCS C885A M8 provides the raw computational power necessary for handling massive data sets and complex algorithms. Moreover, its simplified deployment and streamlined management make it easier than ever for enterprise customers to embrace AI.
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_0.jpg)](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_0.jpg "Related image, diagram or screenshot")
Figure 1. 
Cisco UCS C885A M8 Rack Server
Scalable network fabric for AI connectivity 
To train GenAI models, clusters of these powerful servers often work in unison, generating an immense flow of data that necessitates a network fabric capable of handling high bandwidth with minimal latency. This is where the newly released Cisco Nexus® 9364E-SG2 switch shines. Its high-density 800G aggregation ensures smooth data flow between servers, while advanced congestion management and large buffer sizes minimize packet drops— keeping latency low and training performance high. The Nexus 9364E-SG2 serves as a cornerstone for a highly scalable network infrastructure, allowing AI clusters to expand seamlessly as organizational needs grow.
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_1.jpg)](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_1.jpg "Related image, diagram or screenshot")
Figure 2. 
Cisco Nexus 9364E-SG2 switch for AI connectivity 
<https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/nexus-9000-series-switches-ai-clusters-wp.html>
Purchasing simplicity 
Once these powerful models are trained, you need infrastructure deployed for inferencing to provide actual value, often across a distributed landscape of data centers and edge locations. We have greatly simplified this process with new Cisco® AI PODs that accelerate deployment of the entire AI infrastructure stack itself. No matter where you fall on the spectrum of use cases mentioned at the beginning of this white paper, AI PODs are designed to offer a plug-and-play experience with NVIDIA accelerated computing. The pre-sized and pre-validated bundles of infrastructure eliminate the guesswork from deploying edge inferencing, large-scale clusters, and other AI inferencing solutions, with more use cases planned for release over the next few months. 
Our goal is to enable customers to confidently deploy AI PODs with predictability around performance, scalability, cost, and outcomes, while shortening time to production-ready inferencing with a full stack of infrastructure, software, and AI toolsets. AI PODs include NVIDIA AI Enterprise, an end-to-end, cloud-native software platform that accelerates data science pipelines and streamlines AI development and deployment. Managed through Cisco Intersight®, AI PODs provide centralized control and automation, simplifying everything from configuration to day-to-day operations, with more use cases to come.
AI-cluster network design 
An AI cluster typically has multiple networks—an inter-GPU backend network, a frontend network, a storage network, and an Out-of-Band (OOB) management network. 
Figure 3 shows an overview of these networks. Users (in the corporate network in the figure) and applications (in the data-center network) reach the GPU nodes through the frontend network. The GPU nodes access the storage nodes through a storage network, which, in Figure 3, has been converged with the frontend network. A separate OOB management network provides access to the management and console ports on switches, the BMC ports on the servers, and the Power Distribution Units (PDUs). A dedicated inter-GPU backend network connects the GPUs in different nodes for transporting Remote Direct Memory Access (RDMA) traffic while running a distributed job.
[![Related image, diagram or screenshot](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_2.jpg)](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_2.jpg "Related image, diagram or screenshot")
Figure 3. 
AI-cluster network design 
<https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/nexus-9000-series-switches-ai-clusters-wp.html>
Rail-optimized network design 
GPUs in a scalable unit are interconnected using rail-optimized design to improve collective communication performance by allowing single-hop forwarding through the leaf switches, without the traffic going to the spine switches. In rail-optimized design, port 1 on all the GPU nodes connects to the first leaf switch, port 2 connects to the second leaf switch, and so on. 
The acceleration of AI is fundamentally changing our world and creating new growth drivers for organizations, such as improving productivity and business efficiency while achieving sustainability goals. Scaling infrastructure for AI workloads is more important than ever to realize the benefits of these new AI initiatives. IT departments are being asked to step in and modernize their data-center infrastructure to accommodate these new demanding workloads. 
AI projects go through different phases: training your model, fine tuning it, and then deploying the model to end users. Each phase has different infrastructure requirements. Training is the most compute-intensive phase, and Large Language Models (LLMs), deep learning, Natural Language Processing (NLP), and digital twins require significant accelerated compute. 
<https://www.cisco.com/c/en/us/td/docs/dcn/whitepapers/cisco-addressing-ai-ml-network-challenges.html>
Introduction
The acceleration of AI is fundamentally changing our world and creating new growth drivers for organizations, such as improving productivity and business efficiency while achieving sustainability goals. Scaling infrastructure for AI workloads is more important than ever to realize the benefits of these new AI initiatives. IT departments are being asked to step in and modernize their data-center infrastructure to accommodate these new demanding workloads. 
AI projects go through different phases: training your model, fine tuning it, and then deploying the model to end users. Each phase has different infrastructure requirements. Training is the most compute-intensive phase, and Large Language Model (LLM), deep learning, Natural Language Processing (NLP), and digital twins require significantly accelerated compute. 
Benefits of Cisco UCS servers
AI-ready 
Built on NVIDIA HGX architecture, and with eight high-performance GPUs, the Cisco UCS C885A M8 Rack Server delivers the accelerated compute power needed for the most demanding AI workloads. 
Scalable 
Scale your AI workloads across a cluster of Cisco UCS C885A M8 Rack Servers to address deep learning, large Language Model Training (LLM), model fine tuning, large model inferencing, and Retrieval-Augmented Generation (RAG). 
Consistent management 
Avoid silos of AI infrastructure by managing your AI servers with the same tool as your regular workloads.
Scope of this document
For the MLPerf Training performance testing, performance was evaluated using 8x NVIDIA H200 GPUs on single-node and 16x NVIDIA H200 GPUs with two-node configurations on the Cisco UCS C885A M8 Rack Server. This is the standard configuration on the UCS C885A M8 server, and MLPerf Training benchmark results are collected for various datasets. This data will help in understanding the performance benefits of the UCS C885A M8 server for Training workloads. Performance data for selected datasets is highlighted in this white paper, along with a brief explanation of the performance on the C885A M8 rack server 
Product overview
●Built on the NVIDIA HGX platform, the Cisco UCS C885A M8 Rack Server offers a choice of 8 NVIDIA HGX H200 Tensor Core GPUs to deliver massive, accelerated computational performance in a single server, as well as one NVIDIA ConnectX-7 NIC or NVIDIA BlueField-3 SuperNIC per GPU to scale AI model training across a cluster of dense GPU servers. 
●The server is managed by Cisco Intersight, which can help reduce your Total Cost of Ownership (TCO) and increase your business agility.
**Note:** Initially, the local server management interface will handle configuration and management, while Cisco Intersight will provide inventory capabilities through an integrated Intersight Device Connector. Full management operations and configurations through Cisco Intersight will be introduced in future. 
●The server is offered in fixed configurations that are optimized for intensive AI and HPC workloads. 
[![A diagram of a computerAI-generated content may be incorrect.](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_3.jpg)](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_3.jpg "A diagram of a computerAI-generated content may be incorrect.")
Figure 4. 
Detailed view of server 
A specifications sheet for the UCA C885A M8 is available at: <https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c885a-m8-ds.html>
MLPerf overview
MLPerf is a benchmark suite that evaluates the performance of machine-learning software, hardware, and services. The benchmarks are developed by MLCommons, a consortium of AI leaders from academia, research labs, and industry. The goal of MLPerf is to provide an objective yardstick for evaluating machine learning platforms and frameworks. 
MLPerf has multiple benchmarks, including: 
●**MLPerf Training:** measures the time it takes to train machine learning models to a target level of accuracy 
●**MLPerf Inference:** Datacenter: measures how quickly a trained neural network can perform inference tasks on new data 
MLPerf Training
The MLPerf Training benchmark suite measures how fast systems can train models to a target quality metric. Current and previous results can be reviewed through the results dashboard below. 
The [MLPerf Training Benchmark paper](https://arxiv.org/pdf/1910.01500.pdf) provides a detailed description of the motivation and guiding principles behind the [MLPerf Training benchmark suite](https://mlcommons.org/benchmarks/training/). 
MLPerf Training: Test configuration
For the MLPerf Training performance testing covered in this document, the following Cisco UCS C885A M8 Rack Server configuration was used: 
●8x NVIDIA H200 SXM GPUs on single-server node 
●16x NVIDIA H200 SXM GPUs on two-server nodes 
MLPerf Training performance results
MLPerf Training benchmarks 
The MLPerf Inference models listed in Table 1 were configured on the Cisco UCS C885A M8 Rack Server and tested for performance. 
**Table 1.** MLPerf Training models  
|  Model   |  Reference implementation model   |  Description   |  
| --- | --- | --- |  
|  **retinanet 800x800**  |  [vision/classification_and_detection](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection)  |  Single-stage object detection model optimized for detecting small objects in high-resolution images   |  
|  **llama2-70b**  |  [language/llama2-70b](https://github.com/mlcommons/inference/tree/master/language/llama2-70b)  |  Large language model with 70 billion parameters. It is designed for Natural Language Processing (NLP) tasks and question answering.   |  
|  **rgat**  |  [graph/rgat](https://github.com/mlcommons/inference/tree/master/graph/R-GAT)  |  Graph-based neural network model that uses attention mechanisms to learn from relational data   |  
MLPerf Training 5.1 performance data
As part of the MLPerf Training 5.1 submission, Cisco has tested most of the datasets mentioned in Table 1 on the Cisco UCS C885A M8 Rack Server and submitted the results to MLCommons with NVIDIA H200 GPUs. The results are published on the MLCommons results page: <https://mlcommons.org/benchmarks/inference-datacenter/>
Cisco has also published performance data for MLPerf Training 5.1 with multi-node configurations. Two Cisco UCS C885A M8 Rack servers were configured with 16x NVIDIA H200 GPUs. Performance data with two nodes is provided in Figures 5—7 below. 
The below figure includes unverified MLPerf Training 5.1 results collected after the MLPerf submission deadline. For such data, there is a note added “Result not verified by MLCommons Association.” 
Llama2_70b_lora 
Llama2_70b_lora is a large language model from Meta, with 70 billion parameters. It is designed for various natural language processing tasks such as text generation, summarization, translation, and question answering. 
Figure 5 shows the MLPerf 5.1 Training performance of the Llama2_70b_lora model tested on a Cisco UCS C885A M8 Rack Server with 8x NVIDIA H200 GPUs.
[![A graph on a white backgroundAI-generated content may be incorrect.](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_4.jpg)](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_4.jpg "A graph on a white backgroundAI-generated content may be incorrect.")
Figure 5. 
Llama2_70b_lora performance data on a Cisco UCS C885A M8 Rack Server with 8 x NVIDIA H200 GPUs
Retinanet 
Retinanet is a single-stage object-detection model known for its focus on addressing class imbalances using a novel focal-loss function. The “800x800” refers to the input image size, and the model is optimized for detecting small objects in high-resolution images. 
Figure 6 shows the MLPerf Training 5.1 performance of the Retinanet model tested on Cisco UCS C885A M8 Rack Server with 8x NVIDIA H200 GPUs.
[![A graph with a blue barAI-generated content may be incorrect.](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_5.jpg)](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_5.jpg "A graph with a blue barAI-generated content may be incorrect.")
Figure 6. 
Retinanet performance data on a Cisco UCS C885A M8 Rack Server with 8 x NVIDIA H200 GPUs. 
RGAT 
Relational Graph Attention Network (RGAT) is a graph-based neural-network model that uses attention mechanisms to learn from relational data. It is used for tasks such as graph classification, link prediction, and node classification, where the relationships between entities are key.
Figure 7 shows the MLPerf Training 5.1 performance of the RGAT model tested on a Cisco UCS C885A M8 Rack Server with 8x NVIDIA H200 GPUs.
[![A graph with a blue rectangleAI-generated content may be incorrect.](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_6.jpg)](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_6.jpg "A graph with a blue rectangleAI-generated content may be incorrect.")
Figure 7. 
RGAT performance data on a Cisco UCS C885A M8 Rack Server with 8 x NVIDIA H200 GPUs 
**Note:** For RGAT performance data, the results have not been verified by MLCommons Association because the results were collected after the MLPerf submission deadline. 
MLPerf Training 5.1 multi-node performance data
MLPerf Training multi-node testing evaluates how efficiently systems can train machine learning models across multiple interconnected computing nodes. This benchmarking suite, developed by MLCommons, aims to provide standardized metrics for comparing the performance of various hardware, software, and services in the context of distributed machine learning. 
The benchmarks are continuously evolving to include new and emerging AI workloads, such as Generative AI (GenAI) and Graph Neural Networks (GNNs). MLPerf results highlight the importance of dedicated low-latency interconnects between GPUs in multi-GPU systems for optimal distributed deep-learning training. Training models on multiple nodes introduces complexities, primarily due to communication overhead between nodes. To achieve efficient scaling, several technologies and optimizations are employed, such as RDMA (remote direct memory access), that are crucial for optimizing cross-node GPU-to-GPU communication and distributing training jobs efficiently. Distributed training frameworks and libraries such as NCCL (NVIDIA Collective Communications Library) are commonly used for distributed training and efficient communication across GPUs and nodes.
Llama2_70b_lora 
Llama2_70b_lora is a large language model from Meta, with 70 billion parameters. It is designed for various natural language processing tasks such as text generation, summarization, translation, and question answering. 
Figure 8 shows the single-node and multi-node configuration for MLPerf 5.1 Training performance of the Llama2_70b_lora model tested on a Cisco UCS C885A M8 Rack Server with 8x and 16x NVIDIA H200 GPUs. 
[![A graph with blue barsAI-generated content may be incorrect.](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_7.jpg)](https://www.cisco.com/c/dam/en/us/products/collateral/computing/servers-unified-computing-systems/ucs-c-series-rack-servers/mlperf-training-ucs-c885a-m8-hgx-gpus-wp.docx/_jcr_content/renditions/mlperf-training-ucs-c885a-m8-hgx-gpus-wp_7.jpg "A graph with blue barsAI-generated content may be incorrect.")
Figure 8. 
Multi node Llama2_70b_lora performance data on a Cisco UCS C885A M8 Rack server with 8x and 16x NVIDIA H200 GPUs 
Performance summary 
Built on the NVIDIA HGX platform, the Cisco UCS C885A M8 Rack Server delivers the accelerated compute needed to address the most demanding AI workloads. With its powerful performance and simplified deployment, it helps you achieve faster results from your AI initiatives. 
Cisco successfully submitted MLPerf Training results in partnership with NVIDIA to enhance performance and efficiency, optimizing various inference workloads such as large language model (language), natural language processing (language), image classification (vision), object detection (vision), and graph classification (graph-based). 
The results were exceptional AI performance across the Cisco UCS platforms for MLPerf Inference: 
●The Cisco UCS C885A M8 platform with 8x NVIDIA H200 SXM GPUs emerged as the leader, with good performance for Retinanet and Llama2_70b_lora models for MLPerf Training v5.1 benchmark.
Appendix: Test environment
Table 2 lists the details of the server under test-environment conditions. 
**Table 2.** Server properties  
|  Name   |  Value   |  
| --- | --- |  
|  **Product names**  |  Cisco UCS C885A M8 Rack Server   |  
|  **CPUs**  |  CPU: 2 x AMD EPYC 9575 64-core processor   |  
|  **Number of cores**  |  64   |  
|  **Number of threads**  |  128   |  
|  **Total memory**  |  2.3 TB   |  
|  **Memory DIMMs (16)**  |  96 GB x 24 DIMMs   |  
|  **Memory speed**  |  6400 MHz   |  
|  **Network adapter**  |  ●8x NVIDIA B3140H BlueField-3 E-series SuperNIC 400GbE/NDR  ●2x NVIDIA B3220 BlueField-3 P-Series 200GbE/NDR   |  
|  **GPU controllers**  |  ●NVIDIA HGX H200 8-GPU   |  
|  **SFF NVMe SSDs**  |  ●16 x 1.9 TB 2.5-inch-high performance high endurance NVMe SSD   |  
**Note:** For the server’s BIOS settings, the system default values were applied. 
Table 3 lists the server BIOS settings applied for MLPerf testing. 
**Table 3.** Server BIOS settings  
|  Name   |  Value   |  
| --- | --- |  
|  **SMT control**  |  Auto   |  
|  **NUMA nodes per socket**  |  NPS4   |  
|  **IOMMU**  |  Enabled   |  
|  **Core performance boost**  |  Auto   |  
|  **Determinism enabled**  |  Power   |  
|  **APBDIS**  |  1   |  
|  **Global C-state control**  |  Disabled   |  
|  **DF C-states**  |  Auto   |  
|  **Power profile selection**  |  High-performance mode   |  
**Note:** The rest of the BIOS settings are platform default values.
For more information
For additional information on the server, refer to: <https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c885a-m8-aag.html>
Data sheet: <https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c885a-m8-ds.html>
Cisco AI-Ready Data Center Infrastructure: <https://blogs.cisco.com/datacenter/power-your-genai-ambitions-with-new-cisco-ai-ready-data-center-infrastructure>
Cisco AI PODs: <https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/ai-infrastructure-pods-inferencing-aag.html>
### Our experts recommend
  * [Cisco UCS C845A M8 Rack Server At a Glance](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c845a-m8-rack-server-aag.html "Cisco UCS C845A M8 Rack Server At a Glance")
  * [Cisco UCS Servers with Intel Xeon 6 CPUs FAQ](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/intel-xeon-6-cpu-faq.html "Cisco UCS Servers with Intel Xeon 6 CPUs FAQ")


### Learn more
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


---
# ORIGEN: https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html

  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


  * [](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Maintain and Operate TechNotes](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/tsd-products-support-maintain-and-operate-technotes-list.html)


# Set up Conference Calls and Meetings on a Cisco IP Phone 8800 Series Multiplatform Phone
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
Download
Print
### Available Languages
  * [Arabic - عربي](https://www.cisco.com/c/ar_ae/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Brazil - Português](https://www.cisco.com/c/pt_br/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Canada - Français](https://www.cisco.com/c/fr_ca/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [China - 简体中文](https://www.cisco.com/c/zh_cn/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [China - 繁體中文 (臺灣)](https://www.cisco.com/c/zh_tw/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Germany - Deutsch](https://www.cisco.com/c/de_de/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Italy - Italiano](https://www.cisco.com/c/it_it/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Korea - 한국어](https://www.cisco.com/c/ko_kr/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Latin America - Español](https://www.cisco.com/c/es_mx/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)
  * [Netherlands - Nederlands](https://www.cisco.com/c/nl_nl/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)


### Download Options
  * [PDF](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.pdf) (305.7 KB)   
View with Adobe Reader on a variety of devices
  * [ePub](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.epub) (341.9 KB)   
View in various apps on iPhone, iPad, Android, Sony Reader, or Windows Phone
  * [Mobi (Kindle)](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.mobi) (237.7 KB)   
View on Kindle device or Kindle app on multiple devices


Updated:December 10, 2018
Document ID:SMB5674
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Set up Conference Calls and Meetings on a Cisco IP Phone 8800 Series Multiplatform Phone
## Objective
Setting up conference calls and meetings is possible on the Cisco IP Phone in order to talk with multiple people in one call. While on a call, you can dial another contact to add them to the existing call. If you have multiple lines, you can also combine two calls across two lines.
This article aims to show you how to set up conference calls and meetings on your Cisco IP Phone 8800 Series.
## Applicable Devices
  * 8800 Series


## Software Version
  * 11.0.1


## Set up Conference Calls and Meetings
### Add another contact to an existing call
Step 1. While a call is active, press the **Conference**[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step1.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step1.png "Related image, diagram or screenshot.") button on your IP Phone.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step1b.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step1b.png "Related image, diagram or screenshot.")
Step 2. Punch in the phone number of the contact you wish to add to the call and then press **Call**.
**Note:** In this example, 705 is used as the contact number.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step2.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step2.png "Related image, diagram or screenshot.")
Step 3. Press the **Conference[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step3.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step3.png "Related image, diagram or screenshot.")** button again.
You should now have successfully added the contact to the existing call.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step4.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-callsandmeetings-step4.png "Related image, diagram or screenshot.")
### Conference with Star Code
The Star code feature allows you to combine several calls into a conference with just a single press of the **Conference** [![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-1.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-1.png "Related image, diagram or screenshot.") button.
**Enable Star Code**
Step 1. Using your computer, log in to the web-based utility of the IP Phone and click **Admin Login > advanced**.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step1.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step1.png "Related image, diagram or screenshot.")
Step 2. Click **Voice** and the Extension where you want to enable the Star code.
**Note:** In this example, Ext1 is chosen.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step2.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step2.png "Related image, diagram or screenshot.")
Step 3. Under the Call Feature Settings area, click the drop-down menu for Conference Single Hardkey and choose **Yes**.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step3.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step3.png "Related image, diagram or screenshot.")
Step 4. Enter the Conference Bridge URL number preceded by a ***** in the _Conference Bridge URL_ field. This is the server that would allow a group of people to join in a single phone call via a virtual meeting room.
**Note:** In this example, *55 is used.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step4.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step4.png "Related image, diagram or screenshot.")
Step 5. Click **Submit All Changes**.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step5.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step5.png "Related image, diagram or screenshot.")
Step 6. On your IP Phone, make a call from a line.
**Note:** In this example, the call is made to 53669.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step6.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step6.png "Related image, diagram or screenshot.")
Step 7. When the call is answered, make another call from the same line. When the second call is answered, add more active calls using the same line.
**Note:** In this example, another call is made to 705.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step7.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step7.png "Related image, diagram or screenshot.")
Step 8. When you have completely added all participants, press the Conference button to combine all active calls in one meeting.
[![](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step8.png)](https://www.cisco.com/c/dam/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/images/rjs-07312017-starcode-step8.png "Related image, diagram or screenshot.")
You should now have set up a conference call using the Star Code.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5674-set-up-conference-calls-and-meetings-on-a-cisco-ip-phone-880.html)![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))




---
# ORIGEN: https://www.webex.com/suite/meetings.html

[ ![Webex](https://www.webex.com/content/dam/wbx/us/images/navigation/CiscoWebex-Logo_black.png) ![Webex](https://www.webex.com/content/dam/wbx/us/images/navigation/CiscoWebex-Logo_white.png) ](https://www.webex.com/) [Sign Up, It's Free](https://cart.webex.com/sign-up)
[ ![Webex](https://www.webex.com/content/dam/wbx/us/images/rebrand/nav-footer/black.png) ](https://www.webex.com/) [Sign Up, It's Free](https://cart.webex.com/sign-up)
  * [Products ](javascript:;)
webex suite
    * [Meetings](https://www.webex.com/suite/meetings.html)
Video conferencing and screen sharing
    * [Calling](https://www.webex.com/suite/enterprise-cloud-calling.html)
Cloud calling and phone system
    * [Messaging](https://www.webex.com/suite/messaging.html)
Group messaging, chat, and file sharing
    * [Webinars](https://www.webex.com/suite/webinar.html)
Large meeting and virtual event hosting
    * [Events](https://www.webex.com/us/en/products/suite/events.html)
In-person and hybrid event management
    * [Video Messaging](https://vidcast.io/?utm_source=webex&utm_medium=referral&utm_campaign=webex-integration)
Video messaging and screen recording
    * [Polling](https://www.webex.com/suite/polling.html)
Interactive Q&A, quizzes, and polling
    * [Whiteboarding](https://www.webex.com/suite/whiteboard.html)
Digital co-creation and brainstorming
[Explore the Suite ](https://www.webex.com/suite/collaboration-suite.html)
WORKSPACES
    * [Collaboration Devices](https://www.webex.com/us/en/devices.html)
Explore AI-powered devices for any space.
    * [Workspace Designer](https://designer.webex.com/)
Design your own meeting room.
    * [Workspaces ](https://www.webex.com/us/en/workspaces.html)
Get blueprints for incredible outcomes.
Customer experience
    * [AI Agent](https://www.webex.com/us/en/products/customer-experience/ai-agent.html)
Dynamic AI interactions that lead to customer resolutions.
    * [Cloud Contact Center](https://www.webex.com/us/en/products/customer-experience/contact-center.html)
Intelligent, digital to human customer interactions
    * [AI Assistant for Contact Center](https://www.webex.com/us/en/products/customer-experience/ai-assistant-for-contact-center.html)
Empower agents, supervisors, and customer-facing teams with AI
    * [CPaaS](https://www.webex.com/us/en/products/customer-experience/cpaas.html)
Communications platform for automating customer journeys
    * [Workforce Optimization](https://www.webex.com/us/en/products/workforce-optimization.html)
Optimize agent performance and customer satisfaction
[See all Solutions ](https://www.webex.com/us/en/products/customer-experience.html)
[![](https://www.webex.com/content/dam/wbx/us/images/navigation/webex-app-icon.svg) Download Webex ](https://www.webex.com/downloads.html) [+1-888-469-3239](tel:+1-888-469-3239) [Contact Sales ](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Devices ](javascript:;)
collaboration devices
    * [Room Devices](https://www.webex.com/us/en/devices/room-devices.html)
    * [Desk Devices](https://www.webex.com/us/en/devices/desk-series.html)
    * [Digital Whiteboards](https://www.webex.com/us/en/devices/digital-whiteboards.html)
    * [Phones](https://www.webex.com/us/en/devices/phone-series.html)
    * [Cameras](https://www.webex.com/us/en/devices/cameras.html)
    * [Headsets](https://www.webex.com/us/en/devices/headsets.html)
    * [Room Accessories](https://www.webex.com/us/en/devices/accessories.html)
[See all Devices ](https://www.webex.com/us/en/devices.html)
[ ![](https://www.webex.com/content/dam/www/us/en/images/header/devices/new-workspaces-card.jpg) Reimagine Workspaces Get inspiration for setting up your workspaces from desks and meeting rooms to learning and community spaces. Explore Workspaces ](https://www.webex.com/us/en/workspaces.html)
Featured
    * [ ![](https://www.webex.com/content/dam/www/us/en/images/header/devices/cisco-room-vision-ptz.webp) Room Vision PTZ ](https://www.webex.com/us/en/devices/cameras/cisco-room-vision-ptz-camera.html)
    * [ ![](https://www.webex.com/content/dam/www/us/en/images/header/2026/devices/room-kit-pro-g2.webp) Room Kit Pro G2 ](https://www.webex.com/us/en/devices/room-series/cisco-room-kit-pro.html)
    * [ ![](https://www.webex.com/content/dam/www/us/en/images/home/desk-phone-9800-nav.webp) Desk Phone 9800 ](https://www.webex.com/us/en/devices/phone-series/cisco-phone-9800-series.html)
    * [ ![](https://www.webex.com/content/dam/www/us/en/images/header/2026/devices/desk-pro-g2.webp) Desk Pro G2 ](https://www.webex.com/us/en/devices/desk-series/cisco-desk-pro.html)
    * [ ![](https://www.webex.com/content/dam/www/us/en/images/home/ceiling-microphone-pro.webp) Ceiling Microphone Pro ](https://www.webex.com/us/en/devices/accessories/cisco-ceiling-microphone-pro.html)
    * [ ![](https://www.webex.com/content/dam/www/us/en/images/header/devices/headset-bang-950.jpg) B&O Cisco 950 ](https://www.webex.com/us/en/devices/headsets/bang-and-olufsen-cisco-950.html)
[![](https://www.webex.com/content/dam/wbx/us/images/navigation/webex-app-icon.svg) Download Webex ](https://www.webex.com/downloads.html) [+1-888-469-3239](tel:+1-888-469-3239) [Contact Sales ](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Solutions ](javascript:;)
industries
    * [Education](https://www.webex.com/us/en/solutions/industries/education.html)
    * [Healthcare](https://www.webex.com/us/en/solutions/industries/healthcare.html)
    * [Government](https://www.webex.com/us/en/solutions/industries/government.html)
    * [Financial Services](https://www.webex.com/us/en/solutions/industries/financial-services.html)
    * [Sports & Entertainment](https://www.webex.com/us/en/solutions/industries/sports-entertainment.html)
    * [Nonprofits](https://www.webex.com/us/en/solutions/industries/nonprofits.html)
use cases
    * [Hybrid Work](https://www.webex.com/us/en/solutions/hybrid-work.html)
    * [Sustainability](https://www.webex.com/us/en/solutions/sustainability.html)
    * [Return to the Office](https://www.webex.com/us/en/solutions/return-to-office.html)
    * [Camera Intelligence](https://www.webex.com/us/en/solutions/camera-intelligence-cisco-devices.html)
    * [Workspace Management](https://www.webex.com/us/en/solutions/control-hub-cisco-devices.html)
    * [Devices for Microsoft Teams](https://www.webex.com/us/en/solutions/microsoft-teams-rooms-cisco-devices.html)
    * [AV over IP for Conferencing](https://www.webex.com/us/en/solutions/av-over-ip-video-conferencing.html)
cross-platform
    * [Accessibility](https://www.webex.com/us/en/solutions/cross-platform/accessibility.html)
    * [Security](https://www.webex.com/us/en/solutions/cross-platform/security.html)
    * [Control Hub](https://www.webex.com/us/en/solutions/cross-platform/control-hub.html)
    * [Collaboration AI](https://www.webex.com/products/collaboration-ai.html)
    * [Inclusivity](https://www.webex.com/us/en/solutions/cross-platform/inclusive-collaboration.html)
    * [Interoperability](https://www.webex.com/us/en/solutions/interoperability.html)
    * [RoomOS](https://www.webex.com/us/en/solutions/roomos.html)
[ ![](https://www.webex.com/content/dam/www/us/en/images/header/solutions/webex-ai.jpg) Webex AI: Elevate every experience. Discover how Webex delivers secure, AI-powered experiences across the platform to elevate employee and customer experiences. Explore Webex AI ](https://www.webex.ai/)
[![](https://www.webex.com/content/dam/wbx/us/images/navigation/webex-app-icon.svg) Download Webex ](https://www.webex.com/downloads.html) [+1-888-469-3239](tel:+1-888-469-3239) [Contact Sales ](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Resources ](javascript:;)
Support
    * [Product Help](https://help.webex.com/)
    * [Webex Adoption](https://adopt.webex.com/)
    * [Webex Community](https://community.cisco.com/t5/webex-user-community/ct-p/webex-user)
    * [Contact Support](https://help.webex.com/contact)
    * [Webex Insider](https://www.webex.com/insider)
Learn
    * [Webex Blog](https://blog.webex.com/)
    * [Customer Stories](https://www.webex.com/customers.html)
    * [Live Events and Webinars](https://www.webex.com/learn/webinars-demos.html)
    * [Webex Academy](https://academy.webex.com/)
    * [AI Content Hub](https://www.webex.ai/ai-content-hub.html)
App Integrations
    * [App Hub](https://apphub.webex.com/)
    * [Integration Partners](https://www.webex.com/products/integrations/index.html)
    * [Developer Tools](https://developer.webex.com/)
[ ![](https://www.webex.com/content/dam/wbx/us/images/navigation/resources/Whats-New-Promo.jpg) What’s New in Webex Learn about all the latest innovations released across our collaboration and customer experience solutions. Learn more  ](https://www.webex.com/whats-new)
[![](https://www.webex.com/content/dam/wbx/us/images/navigation/webex-app-icon.svg)Download Webex ](https://www.webex.com/downloads.html) [+1-888-469-3239](tel:+1-888-469-3239) [Contact Sales ](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Plans & Pricing](https://pricing.webex.com/us/en/hybrid-work/meetings/?utm_medium=website&utm_source=wdc&utm_campaign=n/a&utm_content=navigation&team=wdc)


  * [Download](https://www.webex.com/downloads.html)
  * [Join a Meeting](https://signin.webex.com/join)
  * [Sign In](https://signin.webex.com)
  * [ ](javascript:;)
Select Country/Region [](javascript:;)
    * [Australia (English)](https://www.webex.com/)
    * [Brazil (Português)](https://www.webex.com/pt/index.html)
    * [Canada (English)](https://www.webex.com/)
    * [Canada (Français)](https://www.webex.com/fr/index.html)
    * [China (简体字)](https://www.webex.com/zh-cn/index.html)
    * [France (Français)](https://www.webex.com/fr/index.html)
    * [Germany (Deutsch)](https://www.webex.com/de/index.html)
    * [Hong Kong (繁體中文)](https://www.webex.com/zh-tw/index.html)
    * [India (English)](https://www.webex.com/)
    * [Italy (Italiano)](https://www.webex.com/it/index.html)
    * [Japan (日本語)](https://www.webex.com/ja/index.html)
    * [South Korea (한국어)](https://www.webex.com/ko/index.html)
    * [Latin America (Español)](https://www.webex.com/es/index.html)
    * [Spain (Español)](https://www.webex.com/es/index.html)
    * [United Kingdom (English)](https://www.webex.com/)
    * [United States (English)](https://www.webex.com/)
[ United States ](javascript:;)
  * [Sign Up, It's Free](https://cart.webex.com/sign-up)


![](https://www.webex.com/content/dam/wbx/us/images/navigation/webex-app-icon.svg) [Download Webex](https://www.webex.com/downloads.html) [+1-888-469-3239](tel:+1-888-469-3239) [Contact Sales ](https://www.webex.com/us/en/dg/contact-sales.html)
![](https://www.webex.com/content/dam/www/us/en/images/products/suite/gartner-cc-2025.jpg)
Cisco Systems recognized as a 2025 Customers' Choice for Unified Communications as a Service on Gartner® Peer Insights™ for Webex Suite.   
  
[Read Report](https://www.webex.com/us/en/gp/gartner-customer-choice-UCaaS-2025.html)
Webex Meetings 
## Where common ground is found.
When everyone has an equitable experience, your meeting platform isn’t just helping collaboration—it’s driving better business results.
[Plans & Pricing ](https://pricing.webex.com/hybrid-work/meetings/?utm_medium=website&utm_source=wdc&utm_campaign=n/a&utm_content=hero&team=wdc) [See How it Works ](javascript:;)
![Colleagues in virtual meeting discuss report using Webex Desk Mini device.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Where-common-ground-is-found.jpg)
###  Drive more engaging   
meetings. 
Ensure your meetings are designed to give everyone the ability to engage no matter their location, language, or communication style. 
[Watch Now ](https://use.webex.com/How-to-Run-More-Engaging-Meetings?utm_medium=Website&utm_source=Webinar&utm_campaign=Online_Meetings&utm_content=website_module)
![Executive joins video conference in his car using the Webex App on a smartphone and a Cisco headset.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Drive-more-engaging-meetings.jpg)
Elevate every experience with AI.
See how AI is revolutionizing employee and customer experiences and discover what your peers are doing to gain a competitive advantage.
[Explore Webex AI](https://www.webex.ai/?utm_medium=website&utm_source=wdc&utm_term=module&utm_content=meetings&team=wdc)
## Forge a new path  
in hybrid work.
A unified platform. Premier, enterprise-grade features. A seamless collaboration experience for all, from anywhere.
The Total Economic Impact™ of Webex Suite unveils 204% ROI.
Discover the Webex Suite advantage: Forrester's recent study unveils that a composite organization comprised of interviewees with experience using Webex Suite realized 204% return on investment with the Webex Suite—including cost savings, improved collaboration experiences, and dramatic gains in IT efficiencies.
[ Read the Forrester Study ](https://www.webex.com/gp/forrester-tei-webex-suite.html)
Omdia Names Webex as a Leader in Collaborative Meetings
“Cisco Webex has emerged as one of the most comprehensive collaborative meeting solutions ... making Cisco one of the fastest innovators in the market,” says Prachi Nema, Principal Analyst at Omdia.
[ Get the Report ](https://www.webex.com/gp/omdia-universe-collaborative-meeting-services.html)
Aragon Names Webex an Intelligent Video Conferencing Leader
Aragon states, “Cisco is still one of the only vendors to have an integrated virtual assistant that will take commands from humans and do actions such as document action items and then distribute them.”
[ Get the Report ](https://www.webex.com/gp/aragon-intelligent-video-conferencing.html)
##  Connect and collaborate.   
The Webex way.
[Contact Sales ](https://www.webex.com/us/en/dg/contact-sales.html)
![Remote worker waves to his colleague during an online meeting with a Cisco webcam.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Meetings-yield-results.jpg)
![Remote employee speaks to coworkers in a Webex online meeting using a Cisco webcam.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Automation-simplifies-work.jpg)
![Two coworkers collaborate on a Cisco Board Pro in a small meeting room.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Inclusivity-fuels-innovation.jpg)
* ![Remote worker waves to his colleague during an online meeting with a Cisco webcam.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Meetings-yield-results.jpg)
###### Meetings yield results
Boost real-time engagement with intelligent features and the highest quality video and audio.
* ![Remote employee speaks to coworkers in a Webex online meeting using a Cisco webcam.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Automation-simplifies-work.jpg)
###### Automation simplifies work
Use the power of AI to take the labor out of collaboration, optimize workflows, and improve productivity.
* ![Two coworkers collaborate on a Cisco Board Pro in a small meeting room.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Inclusivity-fuels-innovation.jpg)
###### Inclusivity fuels innovation 
Give hybrid teams equal access to collaborative workflows so that every voice is heard.
## Do business better.
Webex Meetings simplifies your company’s workflows at scale. Equip your team with the most powerful tool to meet and exceed business goals.
[Contact Sales ](https://www.webex.com/us/en/dg/contact-sales.html)
Inclusive meetings for all. Real-time translation. Closed captions. Noise removal, voice optimization, and people-focused views. Give everyone a seat at the table, no matter how or where they work. 
Engagement is everything. From custom stage views and immersive share for presentations to interactive polling and Q&A features, meetings can be more enjoyable and productive.
Flexibility comes first. Schedule and join meetings across any device with a single tap. Go from desktop to phone to car with our Move to Mobile QR code feature and Apple CarPlay integration. And use our library of embedded apps to simplify workflows.
Solve employee fatigue. Use Webex Assistant for time-consuming tasks—calling, note taking, action items—and rely on people insights to manage time, build stronger connections, and optimize work-life balance.
Simplify management. Control Hub lets IT oversee users and devices from a single pane of glass and provide custom analytics for real-time or long-term insights. Plus, it’s all protected by Cisco’s best-in-class security.
Empower the whole org chart. Whether supporting sales teams through integrations such as Salesforce or empowering frontline workers by connecting seamlessly to wearable tech, Webex works wonders for the entire workforce.
![Professional gives presentation on Cisco Board Pro to coworkers in a small conference room.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Bring-every-part-of-collaboration-together.jpg)
Bring every part of collaboration together.
Hybrid work demands seamless communication from anywhere—for everyone. The answer is simple: a single platform with calling, meetings, messaging, polling, webinars, events, async video, and more.
[Explore Webex Suite](https://www.webex.com/collaboration-suite.html)  

![Clayco logo](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Clayco_Logo2.svg)
We are seeing as much as a 60-70% reduction in the amount of time it takes to make decisions. Problems are resolved before construction begins and this helps our teams deliver projects faster, optimize costs, and better satisfy clients. 
— Tomislav Žigo, Chief Technology Officer, Clayco
[Read More ](https://www.webex.com/us/en/customers/clayco.html)
![Broadcom logo](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Broadcom_Ltd_Logo.svg)
We saw a 230% increase of our usual meeting minutes’ run rate. One of the advantages we see is Cisco’s ability to scale to handle the tremendous increase in meetings. And Broadcom doesn't have to do anything. 
-Stanley Toh, Global IT - Head of Enterprise End-users Experience and Services, Broadcom 
[Read More ](https://blog.webex.com/cloud-calling/why-cloud-calling-is-a-gamechanger-for-broadcom/)
![Broadcom logo](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/AION-logo-slogan-ENG.svg)
Webex was the obvious choice, and it’s still the superior platform. It is what we needed for security and confidentiality. Webex is an established brand, easy to use, familiar to all, and simultaneous interpretation on top of all of its other features makes it just perfect for our industry. 
—Nada Buric, Director, Aion 
[ Read More ](https://blog.webex.com/video-conferencing/aion/)
![Broadcom logo](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/logo-GluGroup.svg)
Webex Meetings enables us to conduct ‘one-to-many' sessions. We can have seven partners in one session, each with a local language translation, and with an individual breakout room when needed. It encourages real dialogue. 
—Billy Haining, Cofounder, Glu Group 
[ Read More ](https://www.webex.com/us/en/customers/glu-group.html)
![Broadcom logo](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/OneWorldSurgery.svg)
We can connect directly from the operating room to the conference room and beyond internationally. It can give students an invaluable, real-time view of challenging or interesting cases. 
—Merlin Antunez, MD; Medical Director and Orthopedic Surgeon, One World Surgery 
[Read More ](https://www.webex.com/us/en/customers/one-world-surgery.html)
1 / 5
### See how Webex compares.
Webex’s complete, integrated platform delivers enormous benefits for customer organizations in terms of simplified deployment, security, management, and analytics. 
[Get the eBook ](https://www.webex.com/content/dam/wbx/us/ebook/cage-match-webex-competitive-highlights-from-enterprise-connect_cm-3648.pdf)
![](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/See-how-Webex-compares.jpg)
## AI-powered features evolve your video conferencing.
![Webex online meeting translates speaker's words into Arabic..](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Real-time-Translations-and-Gesture-Recognition-in-Webex.jpg)
Real-time Translations and Gesture Recognition in Webex
Not fluent in English? No worries — you can translate to 100+ languages in Webex. Don’t want to bother with the keyboard? No problem. Send in-meeting reactions with just your fingers.
[](javascript:%20void\(0\))
![Remote worker speaks in virtual meeting from living room using Cisco Desk Pro while children play behind him.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Noise-Removal-with-Webex.jpg)
Noise Removal with Webex
Take the difficulty out of connecting no matter where you work, with built-in noise removal technology that lets you meet with confidence.
[](javascript:%20void\(0\))
![Remote worker attends virtual meeting over coffee while Webex Assistant takes notes.](https://www.webex.com/content/dam/wbx/us/images/rebrand/meetings/Stop-Writing-Notes-with-Webex-Assistant.jpg)
Stop Writing Notes with Webex Assistant
Meet the first digital in-meeting assistant for the enterprise. Use voice commands, get real-time and recorded transcripts, closed captioning, automatic highlights, and notes.
[](javascript:%20void\(0\))
## Experience more from Webex.
Get the most complete collaboration portfolio.
![Professional watches Slido's live poll results from home office during a Webex online meeting.](https://www.webex.com/content/dam/wbx/us/images/rebrand/more_slido.jpg)
### Slido
Make meetings instantly interactive with six different types of polling and Q&A.
[](https://www.webex.com/audience-engagement.html)
![Professional manages a webinar from laptop using Webex Webinars.](https://www.webex.com/content/dam/wbx/us/images/rebrand/more_events.jpg)
### Webex Webinars
Host virtual meetings at scale from 100 to 10,000 without sacrificing engagement.
[](https://www.webex.com/webinar.html)
[ ](javascript:;)
![Webex logo](https://www.webex.com/content/dam/wbx/us/images/homepage/Logo1-white%201.png)
Get started for free.
Get started today.
Additional features, storage, and support start at just one low price.
[Sign Up For Free ](https://cart.webex.com/sign-up) [ View Plans & Pricing ](https://pricing.webex.com/us/en/) [Contact Sales ](https://www.webex.com/us/en/dg/contact-sales.html)
Products
  * [Webex Suite](https://www.webex.com/suite/collaboration-suite.html)
  * [Meetings](https://www.webex.com/suite/meetings.html)
  * [Calling](https://www.webex.com/suite/enterprise-cloud-calling.html)
  * [Messaging](https://www.webex.com/suite/messaging.html)
  * [Events](https://www.webex.com/us/en/products/suite/events.html)
  * [Video Messaging](https://vidcast.io/?utm_source=webex&utm_medium=referral&utm_campaign=webex-integration)
  * [Polling](https://www.webex.com/suite/polling.html)
  * [Webinars](https://www.webex.com/suite/webinar.html)
  * [Whiteboarding](https://www.webex.com/suite/whiteboard.html)
  * [Cloud Contact Center](https://www.webex.com/us/en/products/customer-experience/contact-center.html)
  * [CPaaS](https://www.webex.com/us/en/products/customer-experience/cpaas.html)


Devices 
  * [Room Devices](https://www.webex.com/us/en/devices/room-devices.html)
  * [Desk Devices](https://www.webex.com/us/en/devices/desk-series.html)
  * [Digital Whiteboards](https://www.webex.com/us/en/devices/digital-whiteboards.html)
  * [Phones](https://www.webex.com/us/en/devices/phone-series.html)
  * [Cameras](https://www.webex.com/us/en/devices/cameras.html)
  * [Headsets](https://www.webex.com/us/en/devices/headsets.html)
  * [Room Accessories](https://www.webex.com/us/en/devices/accessories.html)


Use Cases 
  * [Hybrid Work](https://www.webex.com/us/en/solutions/hybrid-work.html)
  * [Interoperability](https://www.webex.com/us/en/solutions/interoperability.html)
  * [Return to the office](https://www.webex.com/us/en/solutions/return-to-office.html)
  * [Sustainability](https://www.webex.com/us/en/solutions/sustainability.html)


Resources 
  * [Pricing](https://pricing.webex.com/us/en/)
  * [Downloads](https://www.webex.com/downloads.html)
  * [Help Center](https://help.webex.com/)
  * [Webex Community](https://community.cisco.com/t5/webex-user-community/ct-p/webex-user)
  * [Webex Adoption](https://adopt.webex.com//)
  * [Watch Webinars](https://www.webex.com/learn/webinars-demos.html)
  * [App Hub](https://apphub.webex.com/)
  * [Accessibility](https://www.webex.com/us/en/solutions/cross-platform/accessibility.html)
  * [Webex Blog](https://blog.webex.com/)
  * [Developers](https://developer.webex.com/)


Company 
  * [Cisco](https://www.cisco.com/c/en/us/solutions/collaboration/index.html#~stickynav=1)
  * [Webex Customer Advocacy Program](https://www.webex.com/us/en/dg/customer-advocacy-program.html)
  * [Contact Support](https://help.webex.com/contact)
  * [Contact Sales](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Webex Merch Store](https://merchandise.cisco.com/featured/webex-by-cisco.html)
  * [Careers](https://www.webex.com/company/careers.html)


  * [![](https://www.webex.com/content/dam/www/us/en/icons/social-media-icons/X.svg)](https://twitter.com/webex)
  * [](https://www.linkedin.com/company/webex)
  * [](https://www.facebook.com/webex)
  * [](https://www.youtube.com/c/webex)
  * [](https://www.instagram.com/webex/)


© 2026 Cisco and/or its affiliates. All Rights Reserved.
  * [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
  * [Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
  * [Cookies](https://www.webex.com/suite/meetings.html#privacy-manager)
  * [Trademarks](https://www.cisco.com/web/siteassets/legal/trademark.html)


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


---
# ORIGEN: https://pricing.webex.com/us/en/hybrid-work/meetings

  * 🇺🇸
United States
  * English
  * [Download](https://www.webex.com/downloads.html)
  * [Support](https://help.webex.com/en-us/contact)
  * [Contact Sales](https://www.webex.com/us/en/dg/contact-sales.html?lang=en)
  * [(888) 469-3239](tel:\(888\)%20469-3239)


## [ ![Webex](https://pricing.webex.com/images/webex-logo-light-mode.webp)Webex ![Webex](https://pricing.webex.com/images/webex-logo-dark-mode.webp)Webex ](https://www.webex.com/)
## [ ![Webex](https://pricing.webex.com/images/webex-logo-light-mode.webp)Webex ](https://www.webex.com/)
[Sign Up, It’s Free](https://signup.webex.com?locale=en_US)
  * [Products](javascript:void\(0\);)
WEBEX SUITE
[ ![meetings](https://pricing.webex.com/images/meetings-icon.webp) Meetings Video conferencing and screen sharing ](https://www.webex.com/suite/meetings.html)[ ![events](https://pricing.webex.com/images/events-icon.webp) Events In-person and hybrid event management ](https://www.webex.com/suite/events.html)[ ![calling](https://pricing.webex.com/images/calling-icon.webp) Calling Cloud calling and phone system ](https://www.webex.com/suite/enterprise-cloud-calling.html)[ ![Video Messaging](https://pricing.webex.com/images/video-messaging-icon.webp) Video Messaging Interactive video and screen recording ](https://vidcast.io/)[ ![messaging](https://pricing.webex.com/images/messaging-icon.webp) Messaging Group messaging, chat, and file sharing ](https://www.webex.com/suite/messaging.html)[ ![Polling](https://pricing.webex.com/images/polling-icon.webp) Polling Interactive Q&A, quizzes, and polling ](https://www.webex.com/suite/polling.html)[ ![webinars](https://pricing.webex.com/images/webinars-icon.webp) Webinars Large meeting and virtual event hosting ](https://www.webex.com/suite/webinar.html)[ ![Whiteboarding](https://pricing.webex.com/images/whiteboarding-icon.webp) Whiteboarding Digital co-creation and brainstorming ](https://www.webex.com/suite/whiteboard.html)
[Explore the Suite![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/suite/collaboration-suite.html)
WORKSPACES
[ Home Spaces Personal Devices for every home workspace ](https://www.webex.com/workspaces/explore.html#/home)[ Office Spaces Intelligent devices for the hybrid workplace ](https://www.webex.com/workspaces/explore.html#/office)[ Anywhere Portable devices for on-the-go coollaboration ](https://www.webex.com/workspaces/explore.html#/anywhere)
[Explore all Spaces![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/workspaces/explore.html)
CUSTOMER EXPERIENCE
[ Cloud Contact Center Intelligent, digital to human customer interactions ](https://www.webex.com/customer-experience/contact-center.html)[ CPaaS Communications platform for automating customer journeys ](https://cpaas.webex.com/)
[See all Solutions![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/customer-experience.html)
[![Webex](https://pricing.webex.com/images/download-icon.webp) Download Webex](https://www.webex.com/downloads.html)
[(888) 469-3239](tel:\(888\)%20469-3239)[Contact Sales![arrow](https://pricing.webex.com/images/right-arrow-black.svg)](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Devices](javascript:void\(0\);)
Collaboration Devices
[Desk Devices](https://www.webex.com/us/en/devices/desk-series.html)[Room Devices](https://www.webex.com/us/en/devices/room-devices.html)[Digital Whiteboards](https://www.webex.com/us/en/devices/digital-whiteboards.html)[Headsets](https://hardware.webex.com/products/headsets)[Cameras](https://hardware.webex.com/products/cameras)[Phones](https://www.webex.com/us/en/devices/phone-series.html)[Room Accessories](https://www.webex.com/us/en/devices/accessories.html)[See all Devices![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/collaboration-devices.html)
[ ![Reimagine Workspaces](https://pricing.webex.com/images/reimagineWorkspaces.svg) Reimagine Workspaces Get inspiraton for setting up your workspaces across home, office, and anywhere. [Explore Workspaces![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/workspaces/explore.html) ](https://www.webex.com/workspaces/explore.html)
Featured
[ ![Board Pro](https://pricing.webex.com/images/board-pro.svg)Board Pro ](https://www.webex.com/us/en/devices/board-series/cisco-board-pro.html)[ ![Room Kit EQ](https://pricing.webex.com/images/room-kit-eq.svg)Room Kit EQ ](https://www.webex.com/us/en/devices/room-series/cisco-room-kit-eq.html)[ ![Video Phone 8875](https://pricing.webex.com/images/video-phone-8875.svg)Video Phone 8875 ](https://www.webex.com/us/en/devices/phone-series/cisco-video-phone-8875.html)[ ![Desk Pro](https://pricing.webex.com/images/desk-pro.svg)Desk Pro ](https://www.webex.com/us/en/devices/desk-series/cisco-desk-pro.html)[ ![Room Bar](https://pricing.webex.com/images/room-bar.svg)Room Bar ](https://www.webex.com/us/en/devices/room-series/cisco-room-bar.html)[ ![Headset 720](https://pricing.webex.com/images/headset-720.svg)Headset 720 ](https://www.webex.com/us/en/devices/headsets/cisco-headset-720-series.html)
[![Webex](https://pricing.webex.com/images/download-icon.webp) Download Webex](https://www.webex.com/downloads.html)
[(888) 469-3239](tel:\(888\)%20469-3239)[Contact Sales![arrow](https://pricing.webex.com/images/right-arrow-black.svg)](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Solutions ](javascript:void\(0\);)
Industries
[Education](https://www.webex.com/industries/education.html)[Healthcare](https://www.webex.com/industries/healthcare.html)[Government](https://www.webex.com/industries/government.html)[Finance](https://www.webex.com/industries/financial-services.html)[Sports & Entertainment](https://www.webex.com/industries/sports-entertainment.html)[Nonprofits](https://www.webex.com/industries/nonprofits.html)
Use cases
[Hybrid Work](https://www.webex.com/hybrid-work.html)[Sustainability](https://www.webex.com/sustainability.html)[Return to the Office](https://www.webex.com/solutions/return-to-office.html)[Frontline Workers](https://www.webex.com/industries/frontline.html)
Cross-Platform
[Accessibility](https://www.webex.com/accessibility.html)[Security](https://www.webex.com/security.html)[Control Hub](https://www.webex.com/control-hub.html)[Collaboration AI](https://www.webex.com/products/collaboration-ai.html)[Inclusivity](https://www.webex.com/inclusive-collaboration.html)[Interoperability](https://www.webex.com/solutions/interoperability.html)
[ ![Power hybrid work, sustainably.](https://pricing.webex.com/images/sustainability.svg) Power hybrid work, sustainably. Achieve your sustainability goals by gaining insights into your carbon emissions and progressing on a net zero journey. [Learn More![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/sustainability.html) ](https://www.webex.com/sustainability.html)
[![Webex](https://pricing.webex.com/images/download-icon.webp) Download Webex](https://www.webex.com/downloads.html)
[(888) 469-3239](tel:\(888\)%20469-3239)[Contact Sales![arrow](https://pricing.webex.com/images/right-arrow-black.svg)](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Resources ](javascript:void\(0\);)
Support
[Product Help](https://help.webex.com/)[Product Essentials](https://essentials.webex.com/)[Webex Community](https://community.cisco.com/t5/webex-user-community/ct-p/webex-user)[Contact Support](https://help.webex.com/contact)
Learn
[Webex Blog](https://blog.webex.com/)[Customer Stories](https://www.webex.com/customers.html)[Thought Leadership](https://webexahead.webex.com/)[Live & On-Demand Webinars](https://www.webex.com/learn/webinars-demos.html)
App Integrations
[App Hub](https://apphub.webex.com/)[Integration Partners](https://www.webex.com/products/integrations/index.html)[Developer Tools](https://developer.webex.com/)
[ ![What’s New in Webex](https://pricing.webex.com/images/whats-new.svg) What’s New in Webex Learn about all the latest innovations released across our collaboration and customer experience solutions. [Learn more![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/whats-new) ](https://www.webex.com/whats-new)
[![Webex](https://pricing.webex.com/images/download-icon.webp) Download Webex](https://www.webex.com/downloads.html)
[(888) 469-3239](tel:\(888\)%20469-3239)[Contact Sales![arrow](https://pricing.webex.com/images/right-arrow-black.svg)](https://www.webex.com/us/en/dg/contact-sales.html)
  * [Plans & Pricing](https://pricing.webex.com/us/en/hybrid-work/meetings/)


  * [Download](https://www.webex.com/downloads.html)
  * [Join a Meeting](https://signin.webex.com/join)
  * [Support](https://help.webex.com/en-us/contact)
  * [Sign In](https://signin.webex.com/collabs/auth)
###### Sign In To Webex
Enter Email AddressSign In
[Need Help Signing In?](https://help.webex.com/en-us/n5q6x5j)
  * [Sign Up, It’s Free](https://signup.webex.com?locale=en_US)


[![Webex](https://pricing.webex.com/images/download-icon.webp) Download Webex](https://www.webex.com/downloads.html)
[(888) 469-3239](tel:\(888\)%20469-3239)[Contact Sales![arrow](https://pricing.webex.com/images/right-arrow-black.svg)](https://www.webex.com/us/en/dg/contact-sales.html)
#### [Unlock huge savings! Get 6 months free with 5+ licenses. Save $360 or more. Buy Now #### [Terms & Conditions](javascript:void\(0\)) ](https://pricing.webex.com/us/en/cart/?default_product_id=WEBEX-MEET-A&ft=persistent-cart&ft=cart-migration&ft=unified-expansion-ca&ft=unified-expansion-gb&ft=unified-expansion-in&ft=unified-expansion-jp&ft=newcountryenable&locale=en_US&plan=starter&qty=5&term=annually&terms=annually)
# Choose your Webex plan
### With industry leading solutions for hybrid work and customer experience, Webex fuels businesses of all sizes.
MeetingsCallingWebinars & EventsContact CenterCPaaS
###### Billed monthly
###### Billed annually
6 months free
![plan card section burst](https://pricing.webex.com/images/plan-card-section-burst.svg)
Webex Free
$0
/user/year
[Sign Up, It’s Free](https://signup.webex.com?locale=en_US)
* * *
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Unlimited meetings, **up to 40 min** per meeting
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Up to **100 attendees** per meeting
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Screen sharing with annotation
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Unlimited **Whiteboards**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Local recording
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Calendar service integration
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Advanced **noise cancellation**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
**Unlimited** messaging
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Create and share video by **Vidcast**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
**Advanced Security**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Integration of leading apps
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Basic Support
EXCLUSIVE DEAL
Webex Meet
Buy 5 or more, get 6 months free.
$144
/user/year
$12
/user/mo
![ai-assistant Icon](https://pricing.webex.com/images/ai-assistant-icon.svg)
AI Assistant included
[Buy Now](https://pricing.webex.com/us/en/cart/?default_product_id=WEBEX-MEET-A&ft=persistent-cart&ft=cart-migration&ft=unified-expansion-ca&ft=unified-expansion-gb&ft=unified-expansion-in&ft=unified-expansion-jp&ft=newcountryenable&locale=en_US&plan=starter&qty=1&term=annually&terms=annually)
* * *
**Everything listed in Webex Free, plus:**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
![ai-assistant Icon](https://pricing.webex.com/images/ai-assistant-icon.svg)
**AI Assistant**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Unlimited meetings, **up to 24 hours** per meeting
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Up to **200 attendees** per meeting
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
**10 GB AI-powered** cloud recording
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Live polling and Q&A by Live polling and Q&A by Slido
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
**Closed captions**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Advanced Support
Webex Suite
Meet + Call
$270
/user/year
$22.50
/user/mo
![ai-assistant Icon](https://pricing.webex.com/images/ai-assistant-icon.svg)
AI Assistant included
[Buy Now](https://pricing.webex.com/us/en/cart/?default_product_id=WEBEX-MEET_VOICE-A&ft=persistent-cart&ft=cart-migration&ft=unified-expansion-ca&ft=unified-expansion-gb&ft=unified-expansion-in&ft=unified-expansion-jp&ft=newcountryenable&locale=en_US&plan=starter&qty=1&term=annually&terms=annually)
* * *
**Everything listed in Webex Meet, plus:**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Business phone number
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Call **any telephone number**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Visual voicemail
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Move your call from one device to another
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
**6-way** conference calling
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
**Unlimited local and domestic** long-distance calling
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
International long distance **billed per minute**
Webex Enterprise
Let's talk
![ai-assistant Icon](https://pricing.webex.com/images/ai-assistant-icon.svg)
AI Assistant included
[Contact Sales](https://www.webex.com/us/en/dg/contact-sales.html?lang=en)
* * *
**Everything listed in Webex Suite, plus:**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Up to **1,000 attendees**
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Local & Unlimited Cloud meeting recording
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
**FedRAMP** authorized security
![Green check icon](https://pricing.webex.com/images/check-icon-green-bold.svg)
Certain plans include Webex events
#### See all features
![blue burst](https://pricing.webex.com/images/blue-burst.svg)
### Optional add-ons
These add-ons are available to add to your Webex Meet or Meet + Call plan during checkout.
![call me icon](https://pricing.webex.com/images/call-me-icon-gradient.svg)
Call Me add-on
The Call Me add-on lets a Webex meeting call you at a number you choose instead of using your device's audio. This is a good option if you don't have a good internet connection, and it saves you money on tolls.
DomesticCovers U.S. & Canada
$48/license/yr billed annually
InternationalCovers [70 countries/regions](javascript:void\(0\))
$429/license/yr billed annually
[Add to my plan](https://pricing.webex.com/us/en/cart/?default_addon_id=ONL-TNU%2BI-A&default_product_id=WEBEX-MEET-A&ft=persistent-cart&ft=cart-migration&ft=unified-expansion-ca&ft=unified-expansion-gb&ft=unified-expansion-in&ft=unified-expansion-jp&ft=newcountryenable&locale=en_US&plan=business&qty=1&term=annually&terms=annually)
![translation icon](https://pricing.webex.com/images/translation-icon-gradient.svg)
Real-Time Translation
Translate meetings in real-time, from English to over 100 different closed-captioned languages.
15-day free trial
[Read more](javascript:void\(0\))
$300/license/yr (billed annually)
Watch a quick video
## Frequently   
asked questions
Do you need a credit card for a free account?
No, we don’t take your credit card or any payment details when you sign up for a free plan. It will always be free, and you never have to worry about any surprise charges. When you’re ready to upgrade to a paid Webex plan, then you can enter a credit card.
What is “VoIP” and what are its advantages?
Voice over Internet Protocol (VoIP) transmits sound as data over the internet. This lets you talk over the internet without using a phone. Webex uses VoIP so users can call into a meeting using a computer. With a paid plan, you can also call into a meeting with your phone.   
  
[See More ![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/what-is-voip.html)
What's the difference between a host license and a participant license?
A host license gets you access to paid features. So first, you pick your plan—then get a host license for each person who needs to use your paid Webex plan. Anyone can join a Webex meeting as a participant, they don’t need a host license to attend a meeting.
Do I need a license for each device?
You don't need a separate license for each account, but you can only make one call or meeting on one device at a time for each.
What plan lets me run more than one meeting at a time?
If you need to have more than one meeting at a time, purchase additional host licenses. Each additional license allows you to host a new concurrent meeting.
What payment methods can I use?
We accept credit cards, debit cards, PayPal, and Apple Pay. You'll see a list of the payment methods we accept in the shopping cart when you enter your billing information. Our servers encrypt all information submitted to them, so you can be confident that your payment information will be kept safe and secure.
How soon can I start using Webex?
You can be up and running with basic features such as hosting a meeting or making a phone call immediately after purchase.
How do I invite others to join a call or meeting?
Once you have registered a Webex account, you can invite anyone to join you in the Webex App. They’ll get an email invitation that contains a link to download the app.  
  
[See More ![arrow](https://pricing.webex.com/images/linkArrow.svg)](https://help.webex.com/en-us/rxs4hp)
Do I need to download the app to use Webex?
You don't need to download the app in most cases. Webex also works well in your browser. To use all Webex features, such as making a PSTN call, you do need to [download the app](https://www.webex.com/downloads.html).
How do I cancel my Webex paid plan?
You can cancel your paid plan any time via your account management portal. You can also downgrade to a free plan at any time. If you downgrade with time left in your billing period, you can continue to use your current plan until the current billing period ends. After the current billing period ends, you'll be moved to a Webex free plan.
Where can I join using toll dial-in?
You can join meetings from the following countries using toll dial-in numbers: Argentina, Australia, Austria, Belgium, Brazil, Bulgaria, Canada, Chile, Colombia, Costa Rica, Croatia, Cyprus, Czech Republic, Denmark, Dominican Republic, El Salvador, Estonia, Finland, France, Georgia, Germany, Greece, Hong Kong, Hungary, India, Ireland, Israel, Italy, Japan, Latvia, Lithuania, Luxembourg, Malaysia, Malta, Mexico, Netherlands, New Zealand, Norway, Panama, Peru, Poland, Puerto Rico, Romania, Russia, Singapore, Slovakia, Slovenia, South Africa, South Korea, Spain, Sweden, Switzerland, Turkey, Ukraine, the United Kingdom, and the United States.
### Still have questions?
[Visit our help center](https://help.webex.com/en-us/landing/ld-nyw95a4-WebexMeetings)
###### A proven solution for industry pros.
![Formula 1 logo](https://pricing.webex.com/images/f1.webp)
###### "
###### Webex technology is embedded throughout our team's operations, helping us be connected and agile with our people who operate at race pace around the globe."
Matt Dennington, Executive Director, Partnerships, McLaren Racing
[Read More ![arrow icon](https://pricing.webex.com/images/linkArrow.svg)](https://www.webex.com/customers/mclaren.html)
![left arrow](https://pricing.webex.com/images/left-arrow-black.svg)
1/3
![right arrow](https://pricing.webex.com/images/right-arrow-black.svg)
![G2 momentum leader badge](https://pricing.webex.com/images/momentum-leader-badge.webp)![G2 leader small business badge](https://pricing.webex.com/images/leader-badge.webp)![G2 top 50 products for remote work badge](https://pricing.webex.com/images/top50-badge.webp)
![Trust Radius best feature set badge](https://pricing.webex.com/images/best-feature-badge.webp)![Trust Radius best relationship badge](https://pricing.webex.com/images/best-relationship-badge.webp)
##### Small Business
Pricing[Webex App](https://www.webex.com/all-new-webex.html)[Meetings](https://www.webex.com/video-conferencing.html)[Calling](https://www.webex.com/cloud-calling.html)[Messaging](https://www.webex.com/team-collaboration.html)[Screen Sharing](https://www.webex.com/screen-sharing.html)
##### Enterprise
[Webex Suite](https://www.webex.com/collaboration-suite.html)[Calling](https://www.webex.com/cloud-calling.html)[Meetings](https://www.webex.com/video-conferencing.html)[Messaging](https://www.webex.com/team-collaboration.html)[Slido](https://www.webex.com/audience-engagement.html)[Webinars](https://www.webex.com/webinar.html)[Socio](https://socio.events/)[Contact Center](https://www.webex.com/contact-center.html)[Experience Management](https://www.webex.com/experience-management.html)[imimobile](https://www.webex.com/customer-interaction-management.html)[Security](https://www.webex.com/security.html)[Control Hub](https://www.webex.com/control-hub.html)
##### Devices
[Headsets](https://hardware.webex.com/products/headsets)[Cameras](https://hardware.webex.com/products/cameras)[Desk Series](https://hardware.webex.com/products/desk-series)[Room Series](https://hardware.webex.com/products/room-series-and-kits)[Board Series](https://hardware.webex.com/products/board-series)[Phone Series](https://hardware.webex.com/products/phones)[Accessories](https://hardware.webex.com/products/accessories)
##### Solutions For
[Education](https://www.webex.com/industries/education.html)[Healthcare](https://www.webex.com/industries/healthcare.html)[Government](https://www.webex.com/industries/government.html)[Finance](https://www.webex.com/industries/financial-services.html)[Sports & Entertainment](https://www.webex.com/industries/sports-entertainment.html)[Frontline](https://www.webex.com/industries/frontline.html)[Nonprofits](https://www.webex.com/industries/nonprofits.html)[Startups](https://www.webex.com/industries/start-ups.html)[Hybrid Work](https://www.webex.com/hybrid-work.html)
##### Resources
[Downloads](https://www.webex.com/downloads.html)[Help Center](https://help.webex.com/en-us/)[Join a Test Meeting](https://www.webex.com/test-meeting.html)[Online Classes](https://help.webex.com/en-us/landing/onlineclasses)[Integrations](https://www.webex.com/products/integrations/index.html)[Accessibility](https://www.webex.com/accessibility.html)[Inclusivity](https://www.webex.com/inclusive-collaboration.html)[Live & On-Demand Webinars](https://www.webex.com/learn/webinars-demos.html)[Webex Community](https://cs.co/webexcommunity)[Webex Developers](https://developer.webex.com/)[News & Innovations](https://www.webex.com/resources/whats-new.html)
##### Company
[Cisco](https://www.cisco.com/c/en/us/solutions/collaboration/index.html#~stickynav=1)[Contact Support](https://help.webex.com/en-us/contact)[Contact Sales](https://www.webex.com/us/en/dg/contact-sales.html)[Webex Blog](https://blog.webex.com/)[Webex Thought Leadership](https://webexahead.webex.com/)[Webex Merch Store](https://www.webexmerchstore.com/)[Careers](https://www.webex.com/company/careers.html)[Webex Leap](https://www.webex.com/company/webex-leap.html)
[](https://twitter.com/webex)[](https://www.linkedin.com/company/webex)[](https://www.facebook.com/webex)[](https://www.youtube.com/c/webex)[](https://www.instagram.com/webex/)
© 2026 Cisco and/or its affiliates. All Rights Reserved.
[Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
[Cookies](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
[Trademarks](https://www.cisco.com/web/siteassets/legal/trademark.html)
🇺🇸
United States
English
