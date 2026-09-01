---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-225637-troubleshoot-cloud-devices-failed-to-html-bcee34f8b8
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/225637-troubleshoot-cloud-devices-failed-to.html
retrieved_at: 2026-09-01T14:56:54.075272+00:00
---

Troubleshoot "Cloud Devices failed to join a Webex Meeting"

# Troubleshoot "Cloud Devices failed to join a Webex Meeting"

### Download Options

Updated: March 24, 2026

Document ID: 225637

Contents

## Contents

## Introduction

This document describes how to troubleshoot "Cloud Devices failed to join a Webex Meeting" when using the Join button.

## Problem

When attempting to join a Webex meeting by using the Join button, the message appears:

"Unable to join the meeting. The meeting number is not valid. Please check the number or the link and try again."

## Troubleshooting

### Locate failure attempt in Device logs

Locate callhistory.txt inside the log bundle.

```
*r CallHistoryGetResult Entry 1 CorrelationId: "45549518-9d36-482c-99bf-39e19085608c"
*r CallHistoryGetResult Entry 1 RemoteNumber: "<removed for privacy #00000008>"
*r CallHistoryGetResult Entry 1 CallbackNumber: "<removed for privacy #00000008>"
*r CallHistoryGetResult Entry 1 DisplayName: "<removed for privacy #00000009>"
*r CallHistoryGetResult Entry 1 Direction: Outgoing
*r CallHistoryGetResult Entry 1 Protocol: Spark
*r CallHistoryGetResult Entry 1 CallRate: 20000
*r CallHistoryGetResult Entry 1 CallType: Video
*r CallHistoryGetResult Entry 1 VideoUsed: False
*r CallHistoryGetResult Entry 1 EncryptionType: "None"
*r CallHistoryGetResult Entry 1 BookingId: "webex-1"
*r CallHistoryGetResult Entry 1 Duration: 0
*r CallHistoryGetResult Entry 1 StartTime: "2026-03-16T18:10:55"
*r CallHistoryGetResult Entry 1 StartTimeUTC: "2026-03-16T17:10:55Z"
*r CallHistoryGetResult Entry 1 EndTime: "2026-03-16T18:10:55"
*r CallHistoryGetResult Entry 1 EndTimeUTC: "2026-03-16T17:10:55Z"
*r CallHistoryGetResult Entry 1 DaysAgo: 2
*r CallHistoryGetResult Entry 1 DisconnectCause: "CallError (startOutgoingForWebexMeeting, unexpected, MeetingNotFound, response 404/404006)"
```

Use CorrelationID number on all.log file.

```
*r CallHistoryGetResult Entry 1 CorrelationId: "45549518-9d36-482c-99bf-39e19085608c"
```

```
2026-03-16T18:10:55.824+01:00 main[2441]: Wx2[3]: CallServiceImpl: Removing Call with correlationId='45549518-9d36-482c-99bf-39e19085608c'
2026-03-16T18:10:55.825+01:00 main[2441]: Wx2 I: MeetingContainerServiceImpl::on_call_set_updated: Call updated. Call count: 0, has convergedCall: no, session joined: false
2026-03-16T18:10:55.825+01:00 main[2441]: Wx2 I: MeetingContainerServiceImpl::on_call_set_updated: No active joined call found
2026-03-16T18:10:55.834+01:00 main[2441]: MainEvents I: CallDisconnected(p=7) remoteURI='<removed for privacy>' causeToLocal=[error('CallError (startOutgoingForWebexMeeting, unexpected, MeetingNotFound, response 404/404006)') 'OtherRemote'] causeToRemote=[normal('') 'LocalDisconnect']
```

Notice the MeetingNotFound reason:

```
2026-03-16T18:10:55.834+01:00 main[2441]: MainEvents I: CallDisconnected(p=7) remoteURI='<removed for privacy>' causeToLocal=[error('CallError (startOutgoingForWebexMeeting, unexpected, MeetingNotFound , response 404/404006)') 'OtherRemote'] causeToRemote=[normal('') 'LocalDisconnect']
```

Use MeetingNotFound and the timestamp corrected previously in the file application.log :

```
2026-03-16T18:10:55.810+01:00 main[2441]: Wx2Http[1]: HTTP(243) <= 404
2026-03-16T18:10:55.810+01:00 main[2441]: Wx2[1]: Response: {"code":404006,"message":"Cannot find the data"}
2026-03-16T18:10:55.810+01:00 main[2441]: Wx2 ERROR: CallImpl::verror: 'startOutgoingForWebexMeeting, unexpected, MeetingNotFound, response 404/404006'
2026-03-16T18:10:55.810+01:00 main[2441]: Wx2[3]: CallServiceImpl::onCallError: locusId='', lastActive=''
2026-03-16T18:10:55.815+01:00 main[2441]: MainEvents I: CallDisconnectIndicated(p=7) remoteURI='<removed for privacy>' cause=[error('CallError (startOutgoingForWebexMeeting, unexpected, MeetingNotFound, response 404/404006)') 'OtherRemote']
2026-03-16T18:10:55.815+01:00 main[2441]: MainEvents I: ParticipantLeftConference(c=6,p=7)
```

## Root Cause

The root cause of the Join meeting issue is that the meeting series was deleted or canceled by the host. The booking information was successfully parsed and displayed on the device, but the backend returned a 404 error when the Join button was used.

## Solution

Reschedule a new meeting and ensure that the mailbox assigned to the device accepts and properly updates the new meeting details.

### Revision History

1.0

24-Mar-2026

Initial Release

### Contributed by Cisco Engineers

Josue Jonathan Vizcaino Huape

Technical Consulting Engineer

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 24-Mar-2026 | Initial Release |