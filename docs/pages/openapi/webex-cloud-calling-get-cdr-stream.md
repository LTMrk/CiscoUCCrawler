---
doc_id: webex-cloud-calling-get-cdr-stream
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /cdr_stream
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.636439+00:00
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
- `startTime` [query] (string) **(requerido)**: The start date-time of the first record you wish to collect in UTC time. It would be the earliest time at which the data was inserted into the Webex Calling cloud for the records you wish to collect. Format must be as `YYYY-MM-DDTHH:MM:SS.mmmZ`. `startTime` can't be older than 12 hours from your current UTC time. The window period between `startTime` and `endTime` must not exceed 2 hours in a single API request.
- `endTime` [query] (string) **(requerido)**: The end date-time of the last record you wish to collect in UTC time. It would be the latest time at which the data was inserted into the Webex Calling cloud for the records you wish to collect. Format must be as `YYYY-MM-DDTHH:MM:SS.mmmZ`. `endTime` must be 1 minute ago from your current UTC time and can’t be older than 12 hours. `endTime` must be greater than `startTime`. The window period between `startTime` and `endTime` must not exceed 2 hours in a single API request.
- `locations` [query] (string): Name of the location (as shown in Control Hub). Up to 10 comma-separated locations can be provided. Allows you to query reports by location.
- `max` [query] (number): Limit the maximum number of reports per page of the response. The range is 500 to 5000. Values below 500 are automatically adjusted up to 500, and values above 5000 are automatically adjusted down to 5000. When the API has more reports to return than the max value, the API response will be paginated. Follow the next link contained in the “Link” header within a response to request the next page of results. If there is no next link, all reports for the selected time range have been collected.  For instance, let's say the initial API request is  https://analytics-calling.webexapis.com/v1/cdr_stream?endTime=2025-08-15T10:00:00.000Z&startTime=2025-08-15T08:00:00.000Z&max=5000  The link header in the response would look something like  <<https://analytics-calling.webexapis.com/v1/cdr_stream?endTime=2025-08-15T10:00:00.000Z&startTime=2025-08-15T08:00:00.000Z&startTimeForNextFetch=2025-08-15T09:30:00.000Z&totalCount=20000&max=5000&orgId=zzzzzzzz-yyyy-zzzz-xxxx-yyyyyyyyyyyy>;rel="next">

## Respuestas
- **200**: OK
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
