

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
