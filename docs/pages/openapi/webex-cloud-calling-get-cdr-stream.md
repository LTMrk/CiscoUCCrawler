---
doc_id: webex-cloud-calling-get-cdr-stream
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /cdr_stream
operation_id: getLiveStreamDetailedCallHistory
tags: Reports: Detailed Call History
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.321339+00:00
---

# GET /cdr_stream

**API:** Webex Cloud Calling
**Área:** Reports: Detailed Call History
**operationId:** `getLiveStreamDetailedCallHistory`

## Resumen
Get Live Stream Detailed Call History

## Descripción
Provides Webex Calling Detailed Call History data for your organization.

Results can be filtered with the `startTime`, `endTime` and `locations` request parameters. The `startTime` and `endTime` parameters specify the time window during which Detailed Call History data was inserted into the Webex Calling cloud. The API will return all reports whose insertion time into the Webex Calling cloud falls between `startTime` and `endTime`.

<br/><br/>
Response entries may be added as more information is made available for the reports.
Values in response items may be extended as more capabilities are added to Webex Calling.

## Parámetros
- `startTime` [query] (string) (**requerido**): The start date-time of the first record you wish to collect in UTC time. It would be the earliest time at which the data was inserted into the Webex Calling cloud for the records you wish to collect. Format must be as `YYYY-MM-DDTHH:MM:SS.mmmZ`. `startTime` can't be older than 12 hours from your current UTC time. The window period between `startTime` and `endTime` must not exceed 2 hours in a single API request.
- `endTime` [query] (string) (**requerido**): The end date-time of the last record you wish to collect in UTC time. It would be the latest time at which the data was inserted into the Webex Calling cloud for the records you wish to collect. Format must be as `YYYY-MM-DDTHH:MM:SS.mmmZ`. `endTime` must be 1 minute ago from your current UTC time and can’t be older than 12 hours. `endTime` must be greater than `startTime`. The window period between `startTime` and `endTime` must not exceed 2 hours in a single API request.
- `locations` [query] (string): Name of the location (as shown in Control Hub). Up to 10 comma-separated locations can be provided. Allows you to query reports by location.
- `max` [query] (number): Limit the maximum number of reports per page of the response. The range is 500 to 5000. Values below 500 are automatically adjusted up to 500, and values above 5000 are automatically adjusted down to 5000. When the API has more reports to return than the max value, the API response will be paginated. Follow the next link contained in the “Link” header within a response to request the next page of results. If there is no next link, all reports for the selected time range have been collected.  For instance, let's say the initial API request is  https://analytics-calling.webexapis.com/v1/cdr_stream?endTime=2025-08-15T10:00:00.000Z&startTime=2025-08-15T08:00:00.000Z&max=5000  The link header in the response would look something like  <<https://analytics-calling.webexapis.com/v1/cdr_stream?endTime=2025-08-15T10:00:00.000Z&startTime=2025-08-15T08:00:00.000Z&startTimeForNextFetch=2025-08-15T09:30:00.000Z&totalCount=20000&max=5000&orgId=zzzzzzzz-yyyy-zzzz-xxxx-yyyyyyyyyyyy>;rel="next"> Por defecto: 5000.

## Ejemplo de invocación
```bash
curl -X GET '/cdr_stream?startTime=<startTime>&endTime=<endTime>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Array of detailed call history records
  - `Answer indicator` (string): Whether the call leg was answered after a redirection. Possible values:   - Yes  - No  - Yes-PostRedirection
  - `Answer time` (string): The time the call was answered. Time is in UTC.
  - `Answered` (string): Whether the call leg was answered. For example, in a hunt group case, some legs will be unanswered, and one will be answered.
  - `Authorization code` (string): The authorization code admin created for a location or site for users to use. Collected by the Account/Authorization Codes or Enhanced Outgoing Calling Plan services.
  - `Call ID` (string): SIP Call ID used to identify the call. You can share the Call ID with Cisco TAC to help them pinpoint a call if necessary.
  - `Caller ID number` (string): Displays the calling party’s presentation number based on the caller ID setting from Control Hub. Can be a line/extension, location number, or a custom organization option.  - The Caller ID number is not restricted to E.164 format and can vary based on system configuration.  - For redirected calls, represents only the redirecting party's caller ID number.
  - `Call outcome` (string): Identifies whether the call was set up or disconnected normally. Possible values:  - Success: Call is routed and disconnected successfully. Includes Normal, UserBusy, and NoAnswer scenarios.  - Failure: Call failed with an internal or external error.  - Refusal: Call is rejected because of call block or timeout. You can find more information in the Call outcome reason field.
  - `Call outcome reason` (string): Additional information about the Call outcome returned. Possible reasons are:  - Success   - Normal: Call is completed successfully.   - UserBusy: Call is a success, but the user is busy.   - NoAnswer: Call is a success, but the user didn't answer.  - Refusal   - CallRejected: Call attempt rejected at the recipient's end.   - UnassignedNumber: The dialed number isn't assigned to any user or service.   - SIP408: Request timed out because couldn’t find the user in time.   - InternalRequestTimeout: Request timed out as the service couldn’t fulfill the request due to an unexpected condition.   - Q850102ServerTimeout: Recovery on timer expiry/server timed out   - NoUserResponse: No response from any end-user device/client   - NoAnswerFromUser: No answer from the user.   - SIP480: Callee or called party is currently unavailable.   - SIP487: Request is terminated by bye or cancel.   - TemporarilyUnavailable: User is temporarily unavailable.   - AdminCallBlock: Call attempt is rejected due to the organization's call block list.   - UserCallBlock: The call to user is rejected because the number is on the user's block list.   - Unreachable: Unable to route the call to the desired destination.   - LocalGatewayLoop: Loop detected between the local gateway and Webex Calling.   - UserAbsent: User is temporarily unreachable or unavailable.  - Failure   - DestinationOutOfOrder: Service request failed as the destination can’t be reached or the interface to the destination isn’t functioning correctly.   - SIP501: Invalid method and can’t identify the request method.   - SIP503: Service is temporarily unavailable so can’t process the request.   - ProtocolError: Unknown or unimplemented release code.   - SIP606: Some aspect of the session description wasn't acceptable.   - NoRouteToDestination: No route available to the destination   - Internal: Failed because of internal Webex Calling reasons.   - MaxConcurrentTerminatingAlertingRequestsExceeded: The number of simultaneous unanswered calls to a local gateway, for the same calling and called number, exceeded the limit.  - RouteListCalls: When off-net route list call is blocked due to exceeding the Route List Calls license overage limit for the organization.
  - `Call Recording Platform Name` (string): `Call recording Platform Name` and the recording platform can be "DubberRecorder", "Webex" or "Unknown" if the `Call Recording Platform Name` could not be fetched. Other supported vendors include "Eleveo", "ASCTech", "MiaRec", and "Imagicle".
  - `Call Recording Result` (string): Status of the recorded media: "successful", "failed", or "successful but not kept."
  - `Call Recording Trigger` (string): User's recording mode for the call. The values for this field are "always", always-pause-resume", "on-demand", or "on-demand-user-start."
  - `Call transfer Time` (string): Indicates the time at which the call transfer service was invoked during the call. The invocation time is shown using the UTC/GMT time zone format.
  - `Call type` (string): Type of call. For example:  - SIP_MEETING  - SIP_INTERNATIONAL  - SIP_SHORTCODE  - SIP_INBOUND  - UNKNOWN  - SIP_EMERGENCY  - SIP_PREMIUM  - SIP_ENTERPRISE  - SIP_TOLLFREE  - SIP_NATIONAL  - SIP_MOBILE
  - `Called line ID` (string): For incoming calls, the calling line ID of the user. For outgoing calls, it's the calling line ID of the called party.
  - `Called number` (string): For incoming calls, the telephone number of the user. For outgoing calls, it's the telephone number of the called party.
  - `Calling line ID` (string): For incoming calls, the calling line ID of the calling party. For outgoing calls, it's the calling line ID of the user.
  - `Calling number` (string): For incoming calls, the telephone number of the calling party. For outgoing calls, it's the telephone number of the user.
  - `Client type` (string): The type of client that the user (creating this record) is using to make or receive the call. For example:  - SIP  - WXC_CLIENT  - WXC_THIRD_PARTY  - TEAMS_WXC_CLIENT  - WXC_DEVICE  - WXC_SIP_GW
  - `Client version` (string): The version of the client that the user (creating this record) is using to make or receive the call.
  - `Correlation ID` (string): Correlation ID to tie together multiple call legs of the same call session.
  - `Department ID` (string): A unique identifier for the user's department name.
  - `Device MAC` (string): The MAC address of the device, if known.
  - `Device owner UUID` (string): When calls are made using multi-line or shared line options, this field represents the unique identifier of the device owner. It holds the UUID from the Cisco Common Identity associated with the user. For example, if Alice has a device assigned and makes or receives a call from Bob's line, the CDR will show Alice's UUID as the device owner.      - Only set when the device owner is different than the owner of the device who made/received the call.
  - `Dialed digits` (string): The keypad digits as dialed by the user, before pre-translations.  This field reports multiple call dial possibilities:  - Feature access codes (FAC) used for invoking features such as Last Number Redial or a Call Return.  - An extension that got dialed and a mis-dialed keypad digit from a device/app.  - When a user must dial an outside access code (for example, 9+) before dialing a number, this access code is also reported, as well as the digits dialed thereafter.  Note that when pre-translations have no effect, the dialed digits field contains the same data as the called number field.  This field is only used for originating (outgoing) Calls and is not available for terminating (incoming) Calls.
  - `Direction` (string): Whether the call was inbound or outbound. The possible values are:  - ORIGINATING  - TERMINATING
  - `Duration` (number): The length of the call in seconds.
  - `External caller ID number` (string): Set only when the control hub External Caller ID phone number is a location number or another number from the organization. Not set when "Direct line/Ext" options are selected.   - Only included in originating CDRs (not present in terminating CDRs).  - Not set for calls that are redirected
  - `Final local SessionID` (string): Each call consists of four UUIDs known as Local Session ID, Final Local Session ID, Remote Session ID and Final Remote Session ID.  - The Session ID comprises a Universally Unique Identifier (UUID) for each user-agent participating in a call.  - It can be used for end-to-end tracking of a SIP session in IP-based multimedia communication systems in compliance with RFC 7206 and draft-ietf-insipid-session-id-15.  - The Local SessionID is generated from the Originating user agent.  - The Remote SessionID is generated from the Terminating user agent.  - The Final Local Session ID has the value of the Local Session ID at the end of the call.  - The Final Remote Session ID has the value of the Remote Session ID at the end of the call.
  - `Final remote SessionID` (string): Each call consists of four UUIDs known as Local Session ID, Final Local Session ID, Remote Session ID and Final Remote Session ID.  - The Session ID comprises a Universally Unique Identifier (UUID) for each user-agent participating in a call.  - It can be used for end-to-end tracking of a SIP session in IP-based multimedia communication systems in compliance with RFC 7206 and draft-ietf-insipid-session-id-15.  - The Local SessionID is generated from the Originating user agent.  - The Remote SessionID is generated from the Terminating user agent.  - The Final Local Session ID has the value of the Local Session ID at the end of the call.  - The Final Remote Session ID has the value of the Remote Session ID at the end of the call.
  - `Inbound trunk` (string): Inbound trunk may be presented in Originating and Terminating records.
  - `International country` (string): The country code of the dialed number. This is only populated for international calls.
  - `Local call ID` (string): A unique identifier that is used to correlate CDRs and call legs with each other. This ID is used in conjunction with:  - Remote call ID: To identify the remote CDR of a call leg.  - Transfer related call ID: To identify the call transferred leg.
  - `Local SessionID` (string): Each call consists of four UUIDs known as Local Session ID, Final Local Session ID, Remote Session ID and Final Remote Session ID.  - The Session ID comprises a Universally Unique Identifier (UUID) for each user-agent participating in a call.  - It can be used for end-to-end tracking of a SIP session in IP-based multimedia communication systems in compliance with RFC 7206 and draft-ietf-insipid-session-id-15.  - The Local SessionID is generated from the Originating user agent.  - The Remote SessionID is generated from the Terminating user agent.  - The Final Local Session ID has the value of the Local Session ID at the end of the call.  - The Final Remote Session ID has the value of the Remote Session ID at the end of the call.
  - `Location` (string): Location of the report.
  - `Model` (string): The device model type the user is using to make or receive the call.
  - `Network call ID` (string): A unique identifier that shows if other CDRs are in the same call leg. Two CDRs belong in the same call leg if they have the same Network call ID.
  - `Org UUID` (string): A unique identifier for the organization that made the call. This is a unique identifier across Cisco.
  - `Original reason` (string): Call redirection reason for the original called number. For example:  - Unconditional: Call Forward Always (CFA) service, Group night forwarding.  - NoAnswer: The party was not available to take the call. CF/busy or Voicemail/busy.  - Deflection: Indication that a call was redirected. Possible causes could be Blind transfer, Auto attendant transfer, Transfer out of a Call center etc.  - TimeOfDay: Automated redirection based on the time of the call. Call Forwarding Selective, Call Forwarding mode-based, or Group Night.  - UserBusy: DND enabled or the user willingly declined the call. CF/busy or voicemail/busy.  - FollowMe: Automated redirection to a personal redirecting service which could be Simultaneous Ringing, Sequential Ringing, Office Anywhere, or Remote Office.  - CallQueue: A call center call to an agent or a user (a member of the call queue).  - HuntGroup: A hunt-group-based call to an agent or a user (denotes a member of the hunt group).  - Unavailable: To voicemail, when the user has no app or device.  - Unrecognized: Unable to determine the reason.  - Unknown: Call forward by phone with no reason.  - ExplicitIdxxx: Enterprise voice portal redirection to the user’s home voice portal. The “xxx” portion is the digits collected from the caller, identifying the target mailbox (Extension or DN).  - ImplicitId: Indicates an enterprise voice portal redirection to the user’s home voice portal.
  - `OS type` (string): The operating system that the app was running on, if available.
  - `Outbound trunk` (string): Outbound trunk may be presented in Originating and Terminating records.
  - `Public Called IP Address` (string): Public IP address of the terminating device or application that is assigned with an Internet Telephony Number.
  - `Public Calling IP Address` (string): Public IP address of the device or application making a call that is assigned with an Internet Telephony Number.
  - `Release time` (string): The time the call was finished, in UTC.
  - `Ring duration` (number): The length of ringing before the call was answered or timed out, in seconds.
  - `Redirecting party UUID` (string): When a call is redirected one or more times, indicates the unique identifier of the last redirecting party user or service accountable for the CDR. Holds the value of the UUID contained in the Cisco Common Identity associated with a user or service.
  - `Redirect reason` (string): Call Redirection Reason for the redirecting number. For example:  - Unconditional: Call Forward Always (CFA) service.  - NoAnswer: The party was not available to take the call. CF/busy or Voicemail/busy.  - Deflection: Indication that a call was redirected. Possible causes could be Blind transfer, Auto attendant transfer, Transfer out of a Call center etc.  - TimeOfDay: Automated redirection based on the time of the call. Call Forwarding Selective, Call Forwarding Mode-Based, or Group Night  - UserBusy: DND enabled or user willingly declined the call. CF/busy or Voicemail/busy.  - FollowMe: Automated redirection to a personal redirecting service which could be Simultaneous Ringing, Sequential Ringing, Office Anywhere, or Remote Office.  - CallQueue: A call center call to an agent or a user (denotes a member of the call queue).  - HuntGroup: A hunt-group-based call to an agent or a user (denotes a member of the hunt group).  - Unavailable: To voicemail, when the user has no app or device.  - Unrecognized: Unable to determine the reason.  - Unknown: Call forward by phone with no reason.  - ExplicitIdxxx: Enterprise voice portal redirection to the user’s home voice portal. The “xxx” portion is the digits collected from the caller, identifying the target mailbox (Extension or DN).  - ImplicitId: Indicates an enterprise voice portal redirection to the user’s home voice portal.
  - `Redirecting number` (string): When the call has been redirected one or more times, this field reports the last redirecting number. Identifies who last redirected the call. Only applies to call scenarios such as transfer, call forwarded calls, simultaneous rings, etc.
  - `Related call ID` (string): Call identifier of a different call that was created by this call because of a service activation. The value is the same as the Local call ID field of the related call. You can use this field to correlate multiple call legs connected through other services.
  - `Related reason` (string): Indicates a trigger that led to a change in the call presence. The trigger could be for this particular call or redirected via a different call. For example:  - ConsultativeTransfer: While on a call, the call was transferred to another user by announcing it first. meaning the person was given a heads up or asked if they're interested in taking the call and then transferred.  - CallForwardModeBased: Calls are forwarded using the mode-based management feature option.  - CallForwardSelective: Call Forward as per the defined schedule. Might be based on factors like a specific time, specific callers or to a VM. It always takes precedence over Call Forwarding.  - CallForwardAlways: Calls are unconditionally forwarded to a defined phone number or to VM.  - CallForwardNoAnswer: The party was not available to take the call.  - CallQueue: A call center call to an agent or a user (denotes a member of the call queue).  - HuntGroup: A hunt group based call to an agent or a user (denotes a member of the hunt group).  - CallPickup: The user part of a pickup group or pickup attempted by this user against a ringing call for a different user or extension.  - CalllPark: An ongoing call was parked, assigned with a parked number (not the user’s phone number).  - CallParkRetrieve: Call park retrieval attempt by the user, either for a different extension or against the user’s own extension.  - Deflection: Indication that a call was redirected. Possible causes could be Blind transfer, Auto-attendant transfer, Transfer out of a Call center, etc.  - FaxDeposit: Indicates a FAX was transmitted to the FAX service.  - PushNotificationRetrieval: Push notification feature usage indication. Means that a push notification was sent to wake up the client and get ready to receive a call.  - BargeIn: Indicates the user barged-in to someone else’s call.  - VoiceXMLScriptTermination: Route Point feature usage indication.  - AnywhereLocation: Indicates call origination towards the single number reach location.  - AnywherePortal: Indicates call origination towards the “user” identified by the single number reach portal.  - Unrecognized: Unable to determine the reason.  - CallForwardBusy: The user willingly declined the call, or DND was enabled that then redirected the call to a defined phone number or voice mail.  - CallForwardNotReachable: Hunt group redirection for an agent who is not reachable.  - CallRetrieve: The user triggered the call retrieve option to pick up a call that was parked.  - CallRecording: The user initiated the call recording service that triggered Start/Pause/Resume/Stop recording options.  - DirectedCallPickup: Indicates this user belonged to a call pickup group who answered the call or answered when another member of the call pickup group in a location was busy.  - Executive: The user has been configured using the Executive/Executive assistant service who is allowed to handle calls on someone else's behalf. Also known as Boss-admin.  - ExecutiveAssistantInitiateCall: The user has been configured as an Executive assistant who placed or initiated the call on someone else’s (Boss admin's) behalf.  - ExecutiveAssistantDivert: The user has been configured as an Executive assistant who had call forwarding enabled to a defined phone number.  - ExecutiveForward: The Executive (Boss-admin) had a call forward setting enabled to a defined number. Generally triggered when an ExecutiveAssistant did not pick a call.  - ExecutiveAssistantCallPush: The user has been configured as an Executive assistant who received a call and pushed that call out (using #63) to the Executive’s (Boss-admin's) number.  - Remote Office: Indicates the call was made to reach the remote location of the user.  - RoutePoint: Indicates an incoming and queued call to an agent (for incoming calls to the route point).  - SequentialRing: Indicates this user is in the list of phone numbers, which are alerted sequentially upon receiving an incoming call that matches a set of criteria.  - SimultaneousRingPersonal: Indicates this user was in the list of multiple destinations that are to ring simultaneously when any calls are received on their phone number (the first destination answered is connected).  - CCMonitoringBI: The indication that a Call Queue supervisor invoked silent monitoring.
  - `Releasing party` (string): Indicates which party released the call first. The possible values are:  - Local: Used when the local user has released the call first.  - Remote: Used when the far-end party releases the call first.  - Unknown: Used when the call has partial information or is unable to gather enough information about the party who released the call. It could be because of situations like force lock or because of a session audit failure.
  - `Remote call ID` (string): A unique identifier that is used to correlate CDRs and call legs with each other. This ID is used in conjunction with Local call ID to identity the local CDR of a call leg.
  - `Remote SessionID` (string): Each call consists of four UUIDs known as Local Session ID, Final Local Session ID, Remote Session ID and Final Remote Session ID.  - The Session ID comprises a Universally Unique Identifier (UUID) for each user-agent participating in a call.  - It can be used for end-to-end tracking of a SIP session in IP-based multimedia communication systems in compliance with RFC 7206 and draft-ietf-insipid-session-id-15.  - The Local SessionID is generated from the Originating user agent.  - The Remote SessionID is generated from the Terminating user agent.  - The Final Local Session ID has the value of the Local Session ID at the end of the call.  - The Final Remote Session ID has the value of the Remote Session ID at the end of the call.
  - `Report ID` (string): A unique ID for this particular record. This can be used when processing records to aid in deduplication.
  - `Report time` (string): The time this report was created. Time is in UTC.
  - `Route group` (string): If present, this field's only reported in Originating records. Route group identifies the route group used for outbound calls routed via a route group to Premises-based PSTN or an on-prem deployment integrated with Webex Calling (dial plan or unknown extension).
  - `Route list calls overage` (string): This field is reported whenever an off-net route list call is made or received that exceeds the Route List Calls license volume for the organization. The value indicates the number of bursting calls (calls over the licensed volume) at the time the call was made or received.
  - `Site main number` (string): The main number for the user's site where the call was made or received.
  - `Site timezone` (string): Site timezone is the offset in minutes from UTC time of the user's timezone.
  - `Site UUID` (string): A unique identifier for the site associated with the call. Unique across Cisco products.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "Answer indicator": "Yes",
      "Answer time": "2020-05-14T11:01:17.551Z",
      "Answered": "true",
      "Authorization code": "107",
      "Call ID": "SSE1101163211405201218829100@10.177.4.29",
      "Caller ID number": "2003",
      "Call outcome": "Success",
      "Call outcome reason": "Normal",
      "Call Recording Platform Name": "Webex",
      "Call Recording Result": "successful",
      "Call Recording Trigger": "always",
      "Call transfer Time": "2023-06-05T18:21:29.707Z",
      "Call type": "SIP_ENTERPRISE",
      "Called line ID": "CALLEDCLIDGOESHERE",
      "Called number": "2002",
      "Calling line ID": "YOURCLIDGOESHERE",
      "Calling number": "2001",
      "Client type": "SIP_TOLLFREE",
      "Client version": "1.0.2.3",
      "Correlation ID": "8e8e1dc7-4f25-4595-b9c7-26237f824535",
      "Department ID": "4370c763-81ec-403b-aba3-626a7b1cf264",
      "Device MAC": "6C710D8ABC10",
      "Device owner UUID": "1e9e14c7-4f25-4595-b9c7-26237f824536",
      "Dialed digits": "1246",
      "Direction": "ORIGINATING",
      "Duration": 36,
      "External caller ID number": "2004",
      "Final local SessionID": "82bb753300105000a0000242be131609",
      "Final remote SessionID": "cfe67b8a00105000a0000242be131609",
      "Inbound trunk": "InTrunk",
      "International country": "US",
      "Local call ID": "113104021:0",
      "Local SessionID": "82bb753300105000a0000242be131609",
      "Location": "Richardson",
      "Model": "885
  ... (truncado)
```
- Cabecera `Link`: 

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs