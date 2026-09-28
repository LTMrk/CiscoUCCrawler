---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-callreportingbillingadmin-15-cucm-b-reporting-billing-administration-gu-35f71200f3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/callReportingBillingAdmin/15/cucm_b_reporting-billing-administration-guide-15/cucm_b_reporting-and-billing-administration-guide_chapter_01010.html
retrieved_at: 2026-08-17T00:25:33.978787+00:00
---

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: April 9, 2026

Chapter: CDR Field Descriptions

## Chapter: CDR Field Descriptions

# CDR Field Descriptions

This chapter provides field descriptions for the Call Detail Records (CDRs) in the order in which they appear in the CDR file.

## CDR Field Descriptions

The following table describes all fields in the current CDRs in the order in which they appear.

Field Name

Range of Values

Description

cdrRecordType

0, 1, 2

Defines the type of record. The following valid values apply:

0—Start call detail record (not used)

1—End call detail record (CDR)

2—CMR record

Default - For CDRs, this field always remains1.

globalCallID_callManagerId

Positive Integer

Designates a unique Unified Communications Manager identity.

The Global Call ID comprises two fields: globalCallID_callId globalCallID_callManagerId.

All records that are associated with a standard call have the same Global Call ID in them.

Default - Ensure that this field is populated.

globalCallID_callId

Positive Integer

Designates a unique call identity value that is assigned to each call. The system allocates this identifier independently
                                          on each call server. Values get chosen sequentially when a call begins. A value gets assigned for each call, successful or
                                          unsuccessful. When Unified Communications Manager restarts, it checks the file for the current globalCallID_callId number and assigns the next 1000th number to the next GlobalCallID_callId.

The Global Call ID consists of two fields: globalCallID_callId globalCallID_callManagerId.

All records that are associated with a standard call have the same Global Call ID in them.

For Unified Communications Manager Release 5.x and later releases, the value in the GlobalCallId CDR field survives over Unified Communications Manager restarts. In Release 4.x and earlier releases, although the GlobalCallId field is time-based, the field gets reused under
                                                      conditions of heavy traffic. Because of this behavior, problems can occur with customer billing applications and the ability
                                                      of CAR to correlate CMRs with CDRs and to correlate conference call CDRs. For Release 5.x and later releases, GlobalCallId
                                                      redesign ensures that the field retains a unique value, at least for a certain number of days. Now, the last used globalCallId_callId
                                                      value gets written to disk periodically (for every x number of calls). The value gets retrieved after a Unified Communications Manager restart, and the new globalCallId_callId value begins with this number plus x.

Default - Ensure that this field is populated.

origLegCallIdentifier

Positive Integer

Identifies the originating leg of a call. Be aware that this value is unique within a cluster. If the leg of a call persists
                                          across several subcalls and CDRs (as during a call transfer), this value remains constant.

Default - Ensure that this field is populated.

dateTimeOrigination

Integer

Identifies the date and time when the user goes off the hook or the date and time that the H.323 SETUP message is received
                                          for an incoming call. The time gets stored as UTC.

Default - Ensure that this field is populated.

origNodeId

Positive Integer

Identifies the server, or node within a cluster, to which the originator of the call is registered at the time that the call
                                          is made.

Default - Ensure that this field is populated.

origSpan

0, Positive Integer

For calls that originate at a gateway, this field indicates the B-channel number of the T1, PRI, or BRI trunk where the call
                                          originates, or a zero value for FXS or FXO trunks.

For H.323 gateways, the span number remains unknown, and this field contains the call leg ID of the originator.

For calls that did not originate at a gateway, the value specifies zero.

Default - This field gets populated based on these rules.

origIpAddr

Integer

Identifies the v4 IP address of the device that originates the call signaling.

For Cisco Unified IP Phones , this field specifies the v4 address of the phone.

For PSTN calls, this field specifies the v4address of the H.323 gateway.

For intercluster calls, this field specifies the v4address of the remote Unified Communications Manager .

Default - 0. If the v4 address does not exist for the originating device, this field equals 0. This field gets populated based
                                          on these rules.

callingPartyNumber

Text String

Specifies a numeric string of up to 25 characters that indicates the calling party number if the calling party is identified
                                          with a directory number.

If the calling party uses a blended address in the identity headers, this field contains the directory number portion of the
                                          blended address.

For calls that originate at a Cisco Unified IP Phone , this field shows the extension number of the line that is used.

For incoming H.323 calls, this field specifies the value that is received in the Calling Party Number field in the Setup message.
                                          This field reflects any translations that are applied to the Calling Party Number before it arrives at the Unified Communications Manager (such as translations at the gateway).

For the server calls, where Unified Communications Manager originates a half call without a calling party, this field may remain empty.

CallingPartyNumber could contain a SIP URI.

Default - This field gets populated based on these rules.

callingPartyUnicodeLoginUserID

Unicode – UTF_8

Specifies the calling party login user ID. The format of this field specifies UTF_8.

Default - Empty string "" . If the user ID does not exist, this field stays empty.

origCause_location

0 to 15

For a list of cause code values see Call Termination Cause Codes

Specifies the Location field that is indicated in the ISDN release message for clearing causes that are received over ISDN
                                          signaling links. See topics that are related to call termination cause codes for a list of the valid values per Q.850.

For clearing causes that are created internally by the Unified Communications Manager , this value specifies zero.

Default - 0

origCause_value

0 to 129

For a list of cause code values see Call Termination Cause Codes

Reflects the reason for clearance for the calls that are cleared by the originating party.

Unified Communications Manager currently uses the Q.850 codes and some Unified Communications Manager defined codes. See topics that are related to call termination cause codes for a listing.

For calls that are cleared by the terminating party, this field specifies zero.

In addition to the standard values that are described in Q.850, when a call is split by a feature (transfer or conference),
                                          the CDR terminates, and this field gets set to 393216. This represents a proprietary value for this field.

Default - 0

origPrecedenceLevel

0 to 4

Represents the precedence level of the original leg. For MLPP, each call leg includes a precedence level.

Precedence 0 = FLASH OVERRIDE/ EXECUTIVE OVERRIDE

Precedence 1 = FLASH

Precedence 2 = IMMEDIATE

Precedence 3 = PRIORITY

Precedence 4 = ROUTINE

Default - 4

origMediaTransportAddress_IP

0, Integer

Identifies the v4 IP address of the device that originates the media for the call.

For Cisco Unified IP Phones , this field specifies the v4 address of the phone.

For PSTN calls, this field specifies the v4address of the H.323 gateway.

For intercluster calls, this field specifies the v4address of the remote phone.

Default - 0. If media is not established or the address is not v4, this field equals 0.

origMediaTransportAddress_Port

0, Positive Integer

Identifies the IP port number that is associated with the OrigMediaTransportAddress_IP field.

Default - 0. If media is not established, this field stays 0.

origMediaCap_payloadCapability

0, Positive Integer

For a full list of codecs, see Codec Types

Identifies the codec type that the originator uses to transmit media.

Unified Communications Manager currently uses the following payload capability values: 0, 1-16, 18-20, 25, 32, 33, 81-86. See topics related to codec types
                                          for a listing of the valid values.

Default - 0. If media is not established, this field stays 0.

origMediaCap_maxFramesPerPacket

0, Positive Integer

Identifies the number of milliseconds of data per packet that the originating party sends. This field normally gets set to
                                          10, 20, or 30 for G.729 or G.711 codecs, but the field can store any nonzero value.

Default - 0. If media is not established, this field stays 0.

origMediaCap_g723BitRate

0

This field is not used in the current release of Unified Communications Manager .

Default - This field will remain 0.

origVideoCap_Codec

0,

100 = H.261,

101 = H.263,

103 = H.264

Identifies the codec type that the originator uses to transmit video (H.261, H.263, or H.264.)

Default - 0. If media is not established, this field stays 0.

origVideoCap_Bandwidth

0, Positive Integer

Identifies the bandwidth that is measured in units of kbps.

Default - 0. If media is not established, this field stays 0.

origVideoCap_Resolution

0,

1 = SQCIF,

2 = QCIF,

3 = CIF,

4 = CIF4,

5 = CIF16

6 = H263 custom resolution

7 = W360P

8 = VGA

9 = W448P

10 = HD720P

11 = HD1080P

12 = CIF2

Indicates the transmitting resolution. In the case of H.264 codec or SIP device, this field refers to the max transmitting
                                          resolution the device can transmit for this call.

Default - 0. If media is not established, this field stays 0.

origVideoTransportAddress_IP

0, Integer

Identifies the v4 IP address of the device that originates the call.

Default - 0. If media is not established or the address is not v4, this field stays 0.

origVideoTransportAddress_Port

0, Positive Integer

Identifies the video RTP port that is associated with the origVideoTransportAddress_IP field.

Default - 0. If media is not established, this field stays 0.

origRSVPAudioStat

0 to 5

Provides the status of the RSVP audio reservation from originator to terminator.

0 – No reservation.

1 – RSVP Reservation Failure condition at call setup or feature invocation.

2 – RSVP Reservation Success condition at the call setup or feature invocation.

3 – RSVP Reservation No Response (RSVP Agent) condition at the call setup or feature invocation.

4 – RSVP Mid Call Failure Preempted condition (preempted after the call setup).

5 – RSVP Mid Call Failure Lost Bandwidth condition (includes all mid-call failures except MLPP preemption).

Default – 0

origRSVPVideoStat

0 to 5

Provides the status of the RSVP video reservation from originator to terminator.

0 – No reservation.

1 – RSVP Reservation Failure condition at call setup or feature invocation.

2 – RSVP Reservation Success condition at call setup or feature invocation.

3 – RSVP Reservation No Response (RSVP Agent) condition at call setup or feature invocation.

4 – RSVP MID Call Failure Preempted condition (preempted after call setup).

5 – RSVP MID Call Failure Lost Bandwidth condition (includes all mid-call failures except MLPP preemption).

Default – 0

destLegIdentifier

0, Positive Integer

Identifies the terminating leg of a call. This value remains unique within a cluster. If the leg of a call persists across
                                          several sub-calls and, consequently, several CDRs (as during a call transfer), this value remains constant.

Default - 0. If the destination cannot be reached, this field stays 0.

destNodeId

0, Positive Integer

Identifies the location, or node within a cluster, to which the terminating party of the call is registered at the time that
                                          the call is made.

Default - 0. If the destination cannot be reached, this field stays 0.

destSpan

0, Positive integer

For calls that are received at a gateway, this field indicates the B channel number of the T1, PRI, or BRI trunk where the
                                          call is received, or a zero value for FXS or FXO trunks.

For H.323 gateways, the span number remains unknown, and this field contains the call leg ID of the destination.

For calls not terminating at a gateway, the value specifies zero.

Default - 0. If the destination cannot be reached, this field stays 0.

destIpAddr

0, Integer

Identifies the v4 IP address of the device that terminates the call signaling.

For Cisco Unified IP Phones , this field specifies the v4 address of the phone.

For PSTN calls, this field specifies the v4address of the H.323 gateway.

For intercluster calls, this field specifies the v4address of the remote Unified Communications Manager .

Default - 0. If the destination cannot be reached, this field stays 0. If the v4 address does not exist for this device, the
                                          field equals 0.

originalCalledPartyNumber

Text String

Specifies the number to which the original call was presented, prior to any call forwarding. If translation rules are configured,
                                          this number reflects the called number after the translations have been applied.

If a blended address is used for the called party, this field specifies the directory number portion of the blended address.

This field represents a numeric string of up to 48 characters that can be either digits or a SIP URL.

Default - Empty string "" . If destination cannot be reached, or if the called party number is a directory URI, this field stays empty.

finalCalledPartyNumber

Text String

Specifies the phone number to which the call finally gets presented, until it is answered or rings out. If no forwarding occurs,
                                          this number shows the same number as the originalCalledPartyNumber.

If the call finally gets presented to a directory URI, the field remains empty.

If a blended address is used, this field specifies the directory number portion of the blended address.

For calls to a conference bridge, this field contains the actual identifier of the conference bridge, which is an alphanumeric
                                          string (for example, b0019901001).

This field represents an alphanumeric string that can be either digits or a SIP URL.

Default - Empty string "" . If destination cannot be reached, this field stays empty.

finalCalledPartyUnicodeLoginUserID

Unicode – UTF_8

Specifies the login user ID. The format of this field specifies UTF_8.

Default - Empty string "" . If the user ID does not exist, this field stays empty.

destCause_location

0 to 15

For a list of cause code values see Call Termination Cause Codes

For clearing causes that are received over ISDN signaling links, the ISDN release message indicates this location field. See
                                          topics that are related to call termination cause codes for a listing of the valid values per Q.850.

For clearing causes that Unified Communications Manager creates internally, this value equals zero.

Default - 0. If the destination cannot be reached, this field stays 0.

destCause_value

0 to 129

For a list of cause code values see Call Termination Cause Codes

Reflects the reason for the calss that the destination party cleared. See topics that are related to call termination cause
                                          codes for a listing of the valid values per Q.850.

For calls that the originating party clears, this field stays zero.

In addition to the standard values that are described in Q.850, when a call gets split by a feature (transfer or conference),
                                          the CDR terminates, and this field gets set to 393216. This represents a proprietary value for this field.

Default - 0. If the destination cannot be reached, this field stays 0.

destPrecedenceLevel

0 to 4

Represents the destination legs precedence level. For MLPP, each call leg has a precedence level.

Precedence 0 = FLASH OVERRIDE

Precedence 1 = FLASH

Precedence 2 = IMMEDIATE

Precedence 3 = PRIORITY

Precedence 4 = ROUTINE

Default - 4

destMediaTransportAddress_IP

0, Integer

Identifies the v4 IP address of the device that terminates the media for the call.

For Cisco Unified IP Phones , this field designates the v4 address of the phone.

For PSTN calls, this field designates the v4address of the H.323 gateway.

For intercluster calls, this field shows the v4address of the remote phone.

Default - 0. If the destination cannot be reached or the IP address of the destination is not v4, this field stays 0.

destMediaTransportAddress_Port

0, Positive Integer

Identifies the IP port number that is associated with the DestMediaTransportAddress_IP field.

Default - 0. If the destination cannot be reached, this field stays 0.

destMediaCap_payloadCapability

0, Positive Integer

For a full list of codecs, see Codec Types

Identifies the codec type that the terminating party uses to transmit media.

Unified Communications Manager currently uses the following payload capability values: 0, 1-16, 18-20, 25, 32, 33, 81-86. See topics related to codec types
                                          for a listing of the valid values.

Default - 0. If the destination cannot be reached, this field stays 0.

destMediaCap_maxFramesPerPacket

0, Positive Integer

Identifies the number of milliseconds of data per packet that the terminating party of the call sends. This field normally
                                          gets set to 10, 20, or 30 for G.729 or G.711 codecs but can store any nonzero value.

This field can specify zero if the media is never established.

Default - 0. If the destination cannot be reached, this field stays 0.

destMediaCap_g723BitRate

0

This field is not used in the current release of Unified Communications Manager .

Default - This field stays 0.

destVideoCap_Codec

0,

100 = H.261,

101 = H.263,

103 = H.264

Identifies the codec type that the terminating party uses to transmit video (H.261, H.263, or H.264).

Default - 0. If the destination cannot be reached, this field stays 0.

destVideoCap_Bandwidth

0, Positive Integer

Identifies the bandwidth, and is measured in units of kbps.

Default - 0. If the destination cannot be reached, this field stays 0.

destVideoCap_Resolution

0,

1 = SQCIF,

2 = QCIF,

3 = CIF,

4 = CIF4,

5 = CIF16

6 = H263 custom resolution

7 = W360P

8 = VGA

9 = W448P

10 = HD720P

11 = HD1080P

12 = CIF2

Indicates the transmitting resolution. In the case of H.264 codec or SIP device, this field refers to the max transmitting
                                          resolution the device can transmit for this call.

Default - 0. If media is not established, this field stays 0.

destVideoTransportAddress _IP

0, Integer

Identifies the v4 IP address of the device that receives the call.

Default - 0. If the destination cannot be reached or the IP address of the destination is not v4, this field stays 0.

destVideoTransportAddress_Port

0, Positive Integer

Identifies the video RTP port that is associated with the destVideoTransportAddress_IP field.

Default - 0. If the destination cannot be reached, this field stays 0.

destRSVPAudioStat

0 - 5

Designates the status of the RSVP audio reservation from terminator to originator.

0 – No reservation.

1 – RSVP Reservation Failure condition at the call setup or feature invocation.

2 – RSVP Reservation Success condition at call setup or feature invocation.

3 – RSVP Reservation No Response (RSVP Agent) condition at call setup or feature invocation.

4 – RSVP Mid Call Failure Preempted condition (preempted after call setup).

5 – RSVP Mid Call Failure Lost Bandwidth condition (includes all mid call failures except MLPP preemption).

Default – 0

destRSVPVideoStat

0 - 5

Designates the status of the RSVP video reservation from terminator to originator.

0 – No reservation.

1 – RSVP Reservation Failure condition at call setup or feature invocation.

2 – RSVP Reservation Success condition at call setup or feature invocation.

3 – RSVP Reservation No Response (RSVP Agent) condition at call setup or feature invocation.

4 – RSVP Mid Call Failure Preempted condition (preempted after call setup).

5 – RSVP Mid Call Failure Lost Bandwidth condition (includes all mid call failures except MLPP preemption).

Default – 0

dateTimeConnect

0, Integer

Identifies the date and time that the call connects. The time gets stored as UTC. If the call is never answered, this value
                                          shows zero.

Default - 0. If the call is never connected, this field stays 0.

dateTimeDisconnect

Integer

Identifies the date and time when the call is cleared. This field gets set even if the call never connects. The time gets
                                          stored as UTC.

Default - Ensure that this field is populated.

lastRedirectDn

Text String

Specifies a numeric string of up to 25 characters. The numeric string can contain digits or a SIP URL.

For forwarded calls, this field specifies the phone number of the next to last hop before the call reaches its final destination.
                                          If only one hop occurs, this number matches the OriginalCalledPartyNumber.

If a blended address is used for call addressing, this field contains only the directory number portion of the blended address.

For calls that are not forwarded, this field matches the OriginalCalledPartyNumber and the FinalCalledPartyNumber.

For calls to a conference bridge, this field contains the actual identifier of the conference bridge, which is an alphanumeric
                                          string (for example, b0019901001).

Default - Empty string "" . If the call is never redirected, or if the next to last hop address is a directory URI, this field remains empty.

pkid

Text String

Identifies a text string that the database uses internally to uniquely identify each row. This text string provides no meaning
                                          to the call itself.

Default - A unique ID should always populate this field.

originalCalledPartyNumberPartition

Text String

Identifies unique partition name that is associated with the OriginalCalledPartyNumber field because Unified Communications Manager supports multiple Cisco Unified IP Phones with the same extension number in different partitions.

For calls that egress through an H.323 gateway, this field uniquely specifies the partition name that is associated with the
                                          route pattern that points to the gateway.

Default - Empty string "" . If the original called party does not have a partition, this field remains empty.

callingPartyNumberPartition

Text String

Identifies unique partition name that is associated with the CallingPartyNumber field because Unified Communications Manager supports multiple Cisco Unified IP Phones with the same extension number in different partitions.

For calls that ingress through an H.323 gateway, this field remains blank.

Default - Empty string "" . If the original called party does not have a partition, this field remains empty.

finalCalledPartyNumberPartition

Text String

Identifies unique partition name that is associated with the FinalCalledPartyNumber field because Unified Communications Manager supports multiple Cisco Unified IP Phones with the same extension number in different partitions.

For calls that egress through an H.323 gateway, this field uniquely specifies the partition name that is associated with the
                                          route pattern that points to the gateway.

Default - Empty string "" . If the final called party does not have a partition, this field remains empty.

lastRedirectDnPartition

Text String

Identifies unique partition name that is associated with the LastRedirectDn field because Unified Communications Manager supports multiple Cisco Unified IP Phones with the same extension number in different partitions.

For calls that egress through an H.323 gateway, this field specifies the partition name that is associated with the route
                                          pattern that points to the gateway.

Default - Empty string "" . If the last redirecting Party does not have a partition or the call was never redirected, this field stays empty.

duration

0, Positive integer

Identifies the difference between the Connect Time and Disconnect Time. This field specifies the time that the call remains
                                          connected, in seconds. This field remains zero if the call never connects or if it connects for less than 1 second.

Default - 0

origDeviceName

Text String

Specifies the text string that identifies the name of the originating device.

Default - Ensure that this field is populated.

destDeviceName

Text String

Specifies the text string that identifies the name of the destination device.

Default - Empty string "" . If the original device does not have a name, this field stays empty.

origCallTerminationOnBehalfOf

0, Positive Integer

For a complete list of OnBehalfOf fields, see OnBehalfof Codes

Specifies code that identifies why the originator was terminated.

For example, if the originator of the call hangs up the phone, the OnBehalfOf code shows "12" for Device. If the call terminates because of a transfer, the OnBehalfOf code shows "10" for Transfer.

See topics related to CDR field descriptions for a list of the codes. This release added new OnBehalfOf codes.

Default - 0

destCallTerminationOnBehalfOf

0, Positive Integer

For a complete list of OnBehalfOf fields, see OnBehalfof Codes

Specifies code that identifies why the destination was terminated.

For example, if the destination of the call hangs up the phone, the OnBehalfOf code shows "12" for Device. If the call terminates because of a transfer, the OnBehalfOf code shows "10" for Transfer.

See topics related to CDR field descriptions for a list of the codes. This release added new OnBehalfOf codes.

Default - 0

origCalledPartyRedirectOnBehalfOf

0, Positive Integer

For a complete list of OnBehalfOf fields, see OnBehalfof Codes

Specifies code that identifies the reason for redirection of the original called party.

For example, if the original called party was redirected because of a conference, the OnBehalfOf code specifies "4."

See topics related to CDR field descriptions for a list of the codes. This release added new OnBehalfOf codes.

Default - 0

lastRedirectRedirectOnBehalfOf

0, Integer

For a complete list of OnBehalfOf fields, see OnBehalfof Codes

Specifies code that identifies the reason for redirection of the last redirected party.

For example, if the last redirected party was redirected on behalf of a conference, the OnBehalfOf code specifies "4."

See topics related to CDR field descriptions for a list of the codes. This release added new OnBehalfOf codes.

Default - 0

origCalledPartyRedirectReason

0, Integer

For a complete list of OnBehalfOf fields, see Redirect Reason Codes

Identifies the reason for a redirect of the original called party.

See topics related to redirect reason codes for a complete list of the codes.

Default - 0

lastRedirectRedirectReason

0, Integer

For a complete list of OnBehalfOf fields, see Redirect Reason Codes

Identifies the last redirect reason for redirection.

See topics related to redirect reason codes for a complete list of the codes.

Default - 0

destConversationID

0, Integer

Specifies a unique identifier that is used to identify the parties of a conference call.

For conference chaining scenarios, the origConversationID and destConversationID fields identify which conferences are chained
                                          together.

Default - 0

globalCallId_ClusterId

Text String

Specifies a unique ID that identifies a cluster of Unified Communications Manager s.

The field is generated at installation and is not used by Unified Communications Manager . The fields globalCallId_ClusterId + globalCallId_CMId + globalCallId_CallId make up this unique key.

Default - This field should always be populated.

joinOnBehalfOf

0, Integer

For a complete list of OnBehalfOf fields, see OnBehalfof Codes

Specifies code that identifies the reason for a join.

For example, if the join takes place on behalf of a transfer, the OnBehalfOf code specifies "10."

See topics related to CDR field descriptions for a list of the codes.

Default - 0

comment

Text String

Allows features to add text to the CDRs. This text can describe details about the call.

For example, the following field flags malicious calls:

Tag—CallFlag

Value—MALICIOUS

Default - Empty string "" .

authCodeDescription

Text String

Provides a description of the FAC.

Default - Empty string "" or null.

authorizationLevel

0, Integer

Displays the level of the FAC.

Default - 0

clientMatterCode

Text String

Displays the client matter code. Before the system extends a call, the user enters a client matter code that can be used for
                                          assigning account or billing codes to calls.

Default - Empty string "" or null.

origDTMFMethod

0, Positive Integer

Displays the DTMF method that the originator uses.

0 - No DTMF - Use ANY matched DTMF.

1 - OOB - Use OOB if endpoints behind SIPTrunk support it.

2 - 2833 - Use RFC2833 if endpoints behind SIPTrunk support it.

3 - OOB and 2833 - Use both KPML and RFC2833 if endpoints behind SIPTrunk can support both.

4 - Unknown

Default - 0 (No preference)

destDTMFMethod

0, Positive Integer

Displays the DTMF method that the destination uses.

0 - No DTMF - Use ANY matched DTMF.1 - OOB - Use OOB if endpoints behind SIPTrunk support it.2 - 2833 - Use RFC2833 if endpoints
                                          behind SIPTrunk support it.3 - OOB and 2833 - Use both KPML and RFC2833 if endpoints behind SIPTrunk can support both.4 -
                                          Unknown.

Default - 0 (No preference)

callSecuredStatus

0, Positive Integer

Displays the highest security status that is reached during a call. For example, if the call is originally unsecured, and
                                          later the call changes to secured, the CDR contains 1 for "Secured" even though different portions of the call have different status values.

0 - Non-secured

1 - Authenticated (not encrypted)

2 - Secured (encrypted)

Default - 0 (Non-secured)

origConversationID

Integer

Identifies the conference ID that is associated with the originating leg of the call. In most cases, this field equals 0.

For conference chaining scenarios, the origConversationID and destConversationID fields identify which conferences are chained
                                          together.

Default - 0

origMediaCap_Bandwidth

0, Positive Integer

Displays the media bandwidth that is used at the origination of the call.

Default - 0

destMediaCap_Bandwidth

0, Positive Integer

Displays the media bandwidth that is used at the destination of the call.

Default - 0

authorizationCodeValue

Text String

Displays the Forced Authorization Code (FAC) that is associated with the call.

Default - Empty string "" or null.

outpulsedCallingPartyNumber

Text String

Comprises an alphanumeric string of up to 50 characters.

The calling party number gets outpulsed from the device. This field gets populated only when normalization or localization
                                          takes place at the device.

Default - Empty string "" or null.

outpulsedCalledPartyNumber

Text String

Comprises an alphanumeric string of up to 50 characters.

The called party number gets outpulsed from the device. This field gets populated only when normalization or localization
                                          takes place at the device.

Default - Empty string "" or null.

origIpv4v6Addr

Text string

Comprises an alphanumeric string of up to 64 characters.

This field identifies the IP address of the device that originates the call signalling. The field can be either IPv4 or IPv6
                                          format depending on the type of IP address that gets used for the call.

For Cisco Unified IP Phones , this field is the address of the Cisco Unified IP Phone . For PSTN calls, this field is the address of the gateway. For intercluster calls, this field is the address of the remote Unified Communications Manager .

The IP addressis either in dotted decimal format or in colon separated hexadecimal format.

Default - TheIP address of the originating device as reported by the device or used for the call after media negotiation.

destIpv4v6Addr

Text string

Comprises an alphanumeric string of up to 64 characters.

This field identifies the IP address of the device that terminates the call signalling. The field can be either in IPv4 or
                                          IPv6 format depending upon the type of IP address that gets used for the call.

For Cisco Unified IP Phones , this field is the address of the Cisco Unified IP Phone . For PSTN calls, this field is the address of the gateway. For intercluster calls, this field is the address of the remote Unified Communications Manager .

The IP addressis either in dotted decimal format or in colon separated hexadecimal format.

Default - Empty String "" or null. If the destination does not get reached, this field stays empty.

origVideoCap_Codec_Channel2

0,

100 = H.261,

101 = H.263,

103 = H.264,

Identifies the codec type that the originator uses to transmit video (H.261, H.263, or H.264) for the second video channel.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0.

origVideoCap_Bandwidth_Channel2

0, Positive integer

Identifies the bandwidth measured in units of kbps for the second video channel.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0.

origVideoCap_Resolution_Channel2

0,

1 = SQCIF,

2 = QCIF,

3 = CIF,

4 = CIF4,

5 = CIF16

6 = H263 custom resolution

7 = W360P

8 = VGA

9 = W448P

10 = HD720P

11 = HD1080P

12 = CIF2

Indicates the transmitting resolution for the second video channel. In the case of H.264 codec or SIP device, this field refers
                                          to the maximum transmitting resolution the device can transmit for this call.

Default - 0. If media is not established, this field stays 0. Also, if H.239 and BFCP are not supported for this call, this
                                          field displays 0.

origVideoTransportAddress_IP_Channel2

0, Integer

Identifies the v4 IP address of the device that originates the call for the second video channel.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0.

origVideoTransportAddress_Port_Channel2

0, Positive integer

Identifies the video RTP port associated with the origH239VideoTransportAddress_IP field for the second video channel.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0.

origVideoChannel_Role_Channel2

0 = Presentation role,

1 = Live role,

Positive integer

Identifies the H.239 video channel role of the device that originates.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 is not supported, this field displays
                                          0.

destVideoCap_Codec_Channel2

0,

100 = H.261,

101 = H.263,

103 = H.264

Identifies the codec type that the terminating party uses to transmit video (H.261, H.263, or H.264) for the second video
                                          channel.

Default - 0. If the destination cannot be reached, this field stays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0.

destVideoCap_Bandwidth_Channel2

0, Positive integer

Identifies the bandwidth measured in units of kbps for the second video channel.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0.

destVideoCap_Resolution_Channel2

0,

1 = SQCIF,

2 = QCIF,

3 = CIF,

4 = CIF4,

5 = CIF16

6 = H263 custom resolution

7 = W360P

8 = VGA

9 = W448P

10 = HD720P

11 = HD1080P

12 = CIF2

Indicates the transmitting resolution for the second video channel. In the case of H.264 codec or SIP device, this field refers
                                          to the maximum transmitting resolution the device can transmit for this call.

Default - 0. If media is not established, this field stays 0. Also, if H.239 and BFCP are not supported for this call, this
                                          field displays 0.

destVideoTransportAddress_IP_Channel2

0, Integer

Identifies the v4 IP address of the device that receives the call.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0.

destVideoTransportAddress_Port_Channel2

0, Positive integer

Identifies the video RTP port associated with the destH239VideoTransportAddress_IP field.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0.

destVideoChannel_Role_Channel2

0 = Presentation role,

1 = Live role,

Positive integer

Identifies the H.239 video channel role of the device that receives the call.

Default - 0. If media does not get established, this field displays 0. Also, if H.239 is not supported, this field displays
                                          0.

incomingProtocolID

0 = Unknown,

1 = SIP,

2 = H323,

3 = CTI/JTAPI,

4 = Q931,

Integer

Identifies the protocol (SIP, H.323, CTI/JTAPI, or Q.931) used between Cisco Unified CM and the upstream voice product in
                                          the call path.

incomingProtocolCallRef

Varchar(32)

Identifies the globally unique call reference identification for the protocol. The value is received from the upstream voice
                                          product. The value is alpha–numeric and truncated to 32 characters.

outgoingProtocolID

0 = Unknown,

1 = SIP,

2 = H323,

3 = CTI/JTAPI,

4 = Q931,

Integer

Identifies the protocol (SIP, H.323, CTI/JTAPI, or Q.931) used between Cisco Unified CM and the downstream voice product in
                                          the call path.

outgoingProtocolCallRef

Varchar(32)

Identifies the globally unique call reference identification for the protocol. The value is passed to the next downstream
                                          voiced product. The value is alpha–numeric and truncated to 32 characters.

currentRoutingReason

Positive Integer

For field values see Routing Reason Values for External Call Control

Displays the reason why the call was intercepted for the active call. This field is used with the external call control feature.
                                          See topics related to routing reason values for external call control for a list of reasons.

Default value is 0.

origRoutingReason

Positive Integer

For a complete list of OnBehalfOf fields, see OnBehalfof Codes

Displays the reason why the call was intercepted for the first time. This field is used with the external call control feature,
                                          See topics related to routing reason values for external call control for a list of reasons.

Default value is 0.

lastRedirectingRoutingReason

Positive Integer

For a complete list of OnBehalfOf fields, see OnBehalfof Codes

Displays why the call was intercepted for the last time. This field is used with the external call control feature. See topics
                                          related to routing reason values for external call control for a list of reasons.

Default - Empty string.

huntPilotPartition

Text String

Indicates the partition for the hunt pilot DN.

Default - Empty string.

huntPilotDN

Text String

Indicates the hunt pilot DN through which the call is routed.

Default - Empty string.

calledPartyPatternUsage

Positive Integer

Indicates the pattern of the called party.

Default value specifies 5 (PATTERN_ROUTE).

If the huntPilotDN is populated, use the huntPilotDN field value as the hunt pilot.

If the huntPilotDN is not available, check the pattern usage (7 =PATTERN_HUNT_PILOT) in the CDR table to identify the call
                                                type. If this call is a hunt list call, use the finalCalledPartyNumber as the huntPilotDN.

Possible value for the fields:

0 CallPark PATTERN_CALL_PARK

1 Conference PATTERN_CONF

2 Device PATTERN_DEVICE

3 Translation PATTERN_TRANSLATION

4 Call Pick Up Group PATTERN_CALL_PICK_UP_GROUP

5 Route PATTERN_ROUTE

6 Message Waiting PATTERN_MESSAGE_WAITING

7 Hunt Pilot PATTERN_HUNT_PILOT

8 Voice Mail Port PATTERN_VOICE_MAIL_PORT

9 Domain Routing PATTERN_ROUTE_DOMAIN

10 IPAddress Routing PATTERN_ROUTE_IPNET

11 Device template PATTERN_DEVICE_TEMPLATE

12 Directed Call Park PATTERN_DIRECTED_CALL_PARK

13 Device Intercom PATTERN_DEVICE_INTERCOM

14 Translation Intercom PATTERN_TRANSLATION_INTERCOM

15 Translation Calling Party Number PATTERN_TRANSLATION_CALLING_PARTY_NUMBER

16 Mobility Handoff PATTERN_MOBILITY_HANDOFF

17 Mobility DTMF PATTERN_MOBILITY_DTMF

18 Mobility IVR PATTERN_MOBILITY_IVR

19 Device Intercom Template PATTERN_DEVICE_INTERCOM_TEMPLATE

incomingICID

Text String

Specifies alphanumeric string up to 50 characters.

This field is populated with the IMS Identifier(ICID) from the P-Charging Vector at the incoming call leg of the call.

This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled.

Default = Empty String " "

incomingOrigIOI

Text String

Specifies alphanumeric string up to 50 characters.

This field is populated with the originating Interoperator Identifier(IOI) from the P-Charging Vector at the incoming call
                                          leg of the call.

This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled.

Default = Empty String " "

incomingTermIOI

Text String

Specifies alphanumeric string up to 50 characters.

This field is populated with the terminating Interoperator Identifier(IOI) from the P-Charging Vector at the incoming call
                                          leg of the call.

This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled.

Default = Empty String " "

outgoingICID

Text String

Specifies alphanumeric string up to 50 characters.

This field is populated with the IMS Identifier(ICID) from the P-Charging Vector at the outgoing call leg of the call.

This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled.

Default = Empty String " "

outgoingOrigIOI

Text String

Specifies alphanumeric string up to 50 characters.

This field is populated with the originating Interoperator Identifier(IOI) from the P-Charging Vector at the outgoing call
                                          leg of the call.

This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled.

Default = Empty String " "

outgoingTermIOI

Text String

Specifies alphanumeric string up to 50 characters.

This field is populated with the terminating Interoperator Identifier(IOI) from the P-Charging Vector at the outgoing call
                                          leg of the call.

This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled.

Default = Empty String " "

outpulsedOriginalCalledPartyNumber

Text String

Specifies alphanumeric string up to 50 characters.

The Original called party number outpulsed from the device. Refer to section on Redirecting Number Transformation for details.

Default = Empty String " "

outpulsedLastRedirectingNumber

Text String

Specifies alphanumeric string up to 50 characters.

The Last Redirecting number outpulsed from the device. Refer to section on Redirecting Number Transformation for details.

Default = Empty String " "

wasCallQueued

Positive Integer

Specifies whether the call has been put into a queue or not. A value of 0 means that the call is not put into any queue; 1
                                          means the call has been put into a queue.

totalWaitTimeInQueue

Positive Integer

Specifies how long a caller has been put into a queue. The value is specified in second. The value is 0 if the call is never
                                          put into any queue.

callingPartyNumber_uri

Text String

Specifies an alphanumeric string of up to 254 characters that identifies the calling party if the calling party uses a directory
                                          URI for call addressing.

If the calling party uses a blended address in the identity headers, this field contains the directory URI portion of the
                                          blended address.

Default - Empty string "" . If the calling party does not use a directory URI, the field stays empty.

originalCalledPartyNumber_uri

Text String

Specifies a string of up to 254 alphanumeric characters that specifies the directory URI to which the original call was addressed,
                                          prior to any call forwarding, provided the call was addressed to a directory URI.

If a blended address is used for the called party, this field specifies the directory URI portion of the blended address.

Default - Empty string "" . If destination cannot be reached, or if the called party is a directory number, this field stays empty.

finalCalledPartyNumber_uri

Text String

Specifies an alphanumeric string of up to 254 characters that indicate the directory URI address to which the call finally
                                          gets presented, if the final address is a directory URI. If no forwarding occurs, this field shows the same directory URI
                                          as the originalCalledPartyNumber_uri field.

If a blended address is used for the called number, this field specifies the directory URI portion of the blended address.

For calls to a conference bridge, this field contains the actual identifier of the conference bridge, which is an alphanumeric
                                          string (for example, b0019901001).

Default - Empty string "" . If destination cannot be reached, or if a directory number is used for called addressing, this field stays empty.

lastRedirectDn_uri

Text String

Specifies an alphanumeric string of up to 254 characters.

For forwarded calls that use a directory URI for addressing, this field specifies the directory URI of the next to last hop
                                          before the call reaches its final destination. If only one hop occurs, this number matches the originalCalledPartyNumber_uri.

If a blended address is used, this field contains only the directory URI portion of the blended address.

For calls that are not forwarded, this field matches the originalCalledPartyNumber_uri and the finalCalledPartyNumber_uri.

For calls to a conference bridge, this field contains the actual identifier of the conference bridge, which is an alphanumeric
                                          string (for example, b0019901001).

Default - Empty string "" . If the call is never redirected, or if the address is a directory number, this field remains empty.

mobileCallingPartyNumber

Text string

Specifies the mobile cellular number if the original calling device is a mobile device.

If the original calling device is not a mobile device, this field remains empty.

Default - Empty string

finalMobileCalledPartyNumber

Text string

Specifies the mobile called party if the final called device is a mobile device.

If the final called device is not a mobile device, this field remains empty.

Default - Empty string

origMobileDeviceName

Text string

Specifies the device name of the calling party if the call is placed from a mobile device.

If the mobile call uses a remote destination profile, the device name is the mobile number and remote destination profile
                                          name. For example, mobileNumber: RDP-name.

If the mobile device uses a mobile identity, the device name is the mobile identity name.

If the original device is not a mobile device, this field remains empty.

Default - Empty string

destMobileDeviceName

Text string

If the mobile device uses a remote destination profile the device name is the mobile number and remote destination profile
                                          name. For example, mobileNumber: RDP-name.

If the mobile device uses a mobile identity, the device name is the mobile identity name.

If the destination device is not a mobile device, this field remains empty.

Default - Empty string

origMobileCallDuration

Positive integer

Specifies the call duration in the mobile network of the originating device if the calling party is a mobile device.

If the calling party is not a mobile device, this field remains empty.

Default - 0

destMobileCallDuration

Positive integer

Specifies the call duration in the mobile network for the destination device if the destination device is a mobile device.

If the destination device is not a mobile device, this field remains empty.

Default - 0

mobileCallType

Positive integer

Specifies the mobility feature that is invoked for this mobile call.

Default - 0

originalCalledPartyPattern

Text String

Specifies numeric string (with special characters) up to 50 characters.

This is the pattern to which the original call was placed before any configured translation is applied.

Calls to Translation Pattern will always populate the pattern after applying the configured transformation on the translation
                                          pattern.

Default—empty string "" .

finalCalledPartyPattern

Text String

Specifies numeric string (with special characters) string up to 50 characters.

The pattern of the final called party to which the call is presented until that call is answered or ringing has ended. If
                                          no forwarding occurred, this pattern is the same as originalCalledPartyPattern. This field indicates the pattern before any
                                          configured translation rules are applied.

This value is the same as the finalCalledPartyNumber if the number is a direct match without any translation

Default—empty string "" .

lastRedirectingPartyPattern

Text String

Specifies numeric string (with special characters) string up to 50 characters.

The pattern of the last party which redirected the call to the current called party. If there is no redirection, the field
                                          has the same value as the originalCalledPartyPattern.

Default—empty string "" .

huntPilotPattern

Text String

Specifies numeric string (with special characters) string up to 50 characters.

The huntPilot pattern as configured in the database. This field is populated only when the HuntPilot member answers the call
                                          which is placed either directly or due to redirection to the huntPilot.

Default - empty string "". If no huntPilot member answers, this field is empty.

origDeviceType

Text String

Indicates whether the device that initiated the call was a Spark client that is anchored to Cisco Unified Communications Manager
                                          over the Spark Remote Device:

If yes, this field indicates "CiscoSparkRemoteDevice"

If no, this field is empty.

destDeviceType

Text String

Indicates whether the device that was called was a Spark client that is anchored to Cisco Unified Communications Manager over
                                          the Spark Remote Device:

If yes, this field indicates "CiscoSparkRemoteDevice"

If no, this field is empty.

If the Spark client "rings" and the CDR Log Calls with Zero Duration Flag service parameter is True, this field gets populated
                                                      as 'CiscoSparkRemoteDevice' even if an enterprise number was dialed with "Ring all shared lines" configured.

origDeviceSessionID

Text String

Indicates the call Session ID of the originating device.

When the session terminates, the system generates a CDR record and the field is populated with the originating device Session
                                          ID for the particular call.

If the CDR service parameter 'CDR Log Calls with Zero Duration Flag' is set to 'True', this field is populated even though
                                                      the call is not answered.

The maximum length of this field is restricted to 127 characters. For example, origDeviceSessionID = ab30317fla784dc48fl824d0d3715d86

Default—empty string "" .

destDeviceSessionID

Text String

Indicates the call Session ID of the destination device.

When the session terminates, the system generates a CDR record and the field is populated with the destination device Session
                                          ID for the particular call.

The maximum length of this field is restricted to 127 characters. For example, destDeviceSessionID = 47755a9de7794ba387653f2099600ef2

Default—empty string "" .

## Routing Reason Values for External Call Control

Unified Communications Manager supports the external call control feature, which enables an adjunct route server to make call-routing decisions for Unified Communications Manager by using the Cisco Unified Routing Rules Interface. When you configure external call control, Unified Communications Manager issues a route request that contains the calling party and called party information to the adjunct route server. The adjunct
                              route server receives the request, applies appropriate business logic, and returns a route response that instructs Unified Communications Manager on how the call should get routed, along with any additional call treatment that should get applied.

The adjunct route server can instruct Unified Communications Manager to allow, divert, or deny the call, modify calling and called party information, play announcements to callers, reset call
                              history so adjunct voicemail and IVR servers can properly interpret calling/called party information, and log reason codes
                              that indicate why calls were diverted or denied.

The following table includes the reasons that can display for the currentRoutingReason, origRoutingReason, or lastRedirectingRoutingReason
                              fields.

Field Value

Reason

Description

0

PDPDecision_NONE

This value indicates that the route server did not return a routing directive to the Unified Communications Manager .

1

PDPDecision_Allow_Fulfilled

This value indicates that Unified Communications Manager allowed a call.

2

PDPDecision_Allow_Unfulfilled

This value indicates that Unified Communications Manager disallowed a call.

3

PDPDecision_Divert_Fulfilled

This value indicates that Unified Communications Manager diverted the call.

4

PDPDecision_Divert_Unfulfilled

This value indicates that Unified Communications Manager was not able to divert the call.

5

PDPDecision_Forward_Fulfilled

This value indicates that Unified Communications Manager forwarded the call.

6

PDPDecision_Forward_Unfulfilled

This value indicates that Unified Communications Manager was unable to forward the call.

7

PDPDecision_Reject_Fulfilled

This value indicates that Unified Communications Manager rejected the call.

8

PDPDecision_Reject_Unfulfilled

This value indicates that Unified Communications Manager was not able to reject the call.

## Cisco Call Detail Records Codes

This chapter section information about the codec types and codes that are used in the Call Detail Record fields.

### Codec Types

The following table contains the compression and payload types that may appear in the codec fields.

Value

Description

1

NonStandard

2

G711Alaw 64k

3

G711Alaw 56k

4

G711mu-law 64k

5

G711mu-law 56k

6

G722 64k

7

G722 56k

8

G722 48k

9

G7231

10

G728

11

G729

12

G729AnnexA

13

Is11172AudioCap

14

Is13818AudioCap

15

G.729AnnexB

16

G.729 Annex AwAnnexB

18

GSM Full Rate

19

GSM Half Rate

20

GSM Enhanced Full Rate

25

Wideband 256K

32

Data 64k

33

Data 56k

40

G7221 32K

41

G7221 24K

42

AAC

43

MP4ALATM_128

44

MP4ALATM_64

45

MP4ALATM_56

46

MP4ALATM_48

47

MP4ALATM_32

48

MP4ALATM_24

49

MP4ALATM_NA

80-

GSM

81

ActiveVoice

82

G726 32K

83

G726 24K

84

G726 16K

86

iLBC

89

iSAC

90

OPUS

100

H261

101

H263

102

Vieo

103

H264

104

H264_SVC

105

T120

106

H224

107

T38Fax

108

TOTE

109

H265

110

H264_UC

111

XV150_MR_711U

112

NSE_VBD_711U

113

XV150_MR_729A

114

NSE_VBD_729A

115

H264_FEC

120

Clear_Chan

222

Universal_Xcoder

257

RFC2833_DynPayload

258

PassThrough

259

Dynamic_Payload_PassThru

260

DTMF_OOB

261

Inband_DTMF_RFC2833

299

NoAudio

300

v150_LC_ModemRelay

301

v150_LC_SPRT

302

v150_LC_SSE

303

T38 fax

### Call Termination Cause Codes

The following tables contain call termination cause codes that may appear in the Cause fields in CDRs.

Cause Code is defined in call control as Natural number. It is a 32 bit unsigned (long) positive integer with values ranging
                                             from 0 to +4,294,967,295.

Code

Description

0

No error

1

Unallocated (unassigned) number

2

No route to specified transit network (national use)

3

No route to destination

4

Send special information tone

5

Misdialed trunk prefix (national use)

6

Channel unacceptable

7

Call awarded and being delivered in an established channel

8

Preemption

9

Preemption—circuit reserved for reuse

16

Normal call clearing

17

User busy

18

No user responding

19

No answer from user (If "No Answer Ring duration" value is greater than the T301 Timer value and after T301 Timer expiry,
                                             Call Forwarding No Answer(CFNA) Feature would be invoked).

20

Subscriber absent

21

Call rejected

22

Number changed

25

Natural Exchange Routing Error

26

Non-selected user clearing

27

Destination out of order

28

Invalid number format (address incomplete)

29

Facility rejected

30

Response to STATUS ENQUIRY

31

Normal, unspecified

34

No circuit/channel available

38

Network out of order

39

Permanent frame mode connection out of service

40

Permanent frame mode connection operational

41

Temporary failure

42

Switching equipment congestion

43

Access information discarded

44

Requested circuit/channel not available

46

Precedence call blocked

47

Resource unavailable, unspecified

49

Quality of Service not available

50

Requested facility not subscribed

53

Service operation violated

54

Incoming calls barred

55

Incoming calls barred within Closed User Group (CUG)

57

Bearer capability not authorized

58

Bearer capability not presently available

62

Inconsistency in designated outgoing access information and subscriber class

63

Service or option not available, unspecified

65

Bearer capability not implemented

66

Channel type not implemented

69

Requested facility not implemented

70

Only restricted digital information bearer capability is available (national use)

79

Service or option that is not implemented, unspecified

81

Invalid call reference value

82

Identified channel does not exist

83

A suspended call exists, but this call identity does not

84

Call identity in use

85

No call suspended

86

Call having the requested call identity has been cleared

87

User not member of CUG (Closed User Group)

88

Incompatible destination

90

Destination number missing and DC not subscribed

91

Invalid transit network selection (national use)

95

Invalid message, unspecified

96

Mandatory information element is missing

97

Message type nonexistent or not implemented

98

Message is not compatible with the call state, or the message type is nonexistent or not implemented

99

An information element or parameter does not exist or is not implemented

100

Invalid information element contents

101

The message is not compatible with the call state

102

Call terminated when timer expired; a recovery routine that is executed to recover from the error

103

Parameter nonexistent or not implemented - passed on (national use)

110

Message with unrecognized parameter discarded

111

Protocol error, unspecified

122

Precedence Level Exceeded

123

Device not Preemptable

125

Out of bandwidth (Cisco specific)

126

Call split (Cisco specific)

127

Interworking, unspecified

129

Precedence out of bandwidth

130

Natural Isolated Code

131

Call Control Discovery PSTN Failover (Cisco specific)

132

IME QOS Fallback (Cisco specific)

133

PSTN Fallback locate Call Error (Cisco specific)

134

PSTN Fallback wait for DTMF Timeout (Cisco specific)

135

IME Failed Connection Timed out (Cisco specific)

136

IME Failed not enrolled (Cisco specific)

137

IME Failed socket error (Cisco specific)

138

IME Failed domain blocked (Cisco specific)

139

IME Failed prefix blocked (Cisco specific)

140

IME Failed expired ticket (Cisco specific)

141

IME Failed remote no matching route (Cisco specific)

142

IME Failed remote unregistered (Cisco specific)

143

IME Failed remote IME disabled (Cisco specific)

144

IME Failed remote invalid IME trunk URI (Cisco specific)

145

IME Failed remote URI not E164 (Cisco specific)

146

IME Failed remote called number not available (Cisco specific)

147

IME Failed Invalid Ticket (Cisco specific)

148

IME Failed unknown (Cisco specific)

155

DCC Allowed Percentage Exceeded

Decimal Value Code

Hex Value Code

Description

262144

0x40000

Conference Full (was 124)

393216

0x60000

Call split (was 126) This code applies when a call terminates during a transfer operation because it was split off and terminated
                                             (was not part of the final transferred call). This code can help you to determine which calls terminated as part of a feature
                                             operation.

458752

0x70000

Conference drop any party/Conference drop last party (was 128)

16777257

0x1000029

CCM_SIP_400_BAD_REQUEST

33554453

0x2000015

CCM_SIP_401_UNAUTHORIZED

50331669

0x3000015

CCM_SIP_402_PAYMENT_REQUIRED

67108885

0x4000015

CCM_SIP_403_FORBIDDEN

83886081

0x5000001

CCM_SIP_404_NOT_FOUND

100663359

0x600003F

CCM_SIP_405_METHOD_NOT_ALLOWED

117440591

0x700004F

CCM_SIP_406_NOT_ACCEPTABLE

134217749

0x8000015

CCM_SIP_407_PROXY_AUTHENTICATION_REQUIRED

150995046

0x9000066

CCM_SIP_408_REQUEST_TIMEOUT

184549398

0xB000016

CCM_SIP__410_GONE

201326719

0xC00007F

CCM_SIP_411_LENGTH_REQUIRED

234881151

0xE00007F

CCM_SIP_413_REQUEST_ENTITY_TOO_LONG

251658367

0xF00007F

CCM_SIP_414_REQUEST_URI_TOO_LONG

268435535

0x1000004F

CCM_SIP_415_UNSUPPORTED_MEDIA_TYPE

285212799

0x1100007F

CCM_SIP_416_UNSUPPORTED_URI_SCHEME

83886207

0x1500007F

CCM_SIP_420_BAD_EXTENSION

369098879

0x1600007F

CCM_SIP_421_EXTENSION_REQUIRED

402653311

0x1800007F

CCM_SIP_423_INTERVAL_TOO_BRIEF

419430421

0x19000015

CCM_SIP_424_BAD_LOCATION_INFO

503316501

0x1E000015

CCM_SIP_429_PROVIDE_REFER_IDENTITY

1073741842

0x40000012

CCM_SIP_480_TEMPORARILY_UNAVAILABLE

1090519081

0x41000029

CCM_SIP_481_CALL_LEG_DOES_NOT_EXIST

1107296281

0x42000019

CCM_SIP_482_LOOP_DETECTED = 0x42000000 + EXCHANGE_ROUTING_ERROR

1124073497

0x43000019

CCM_SIP_483_TOO_MANY_HOOPS

1140850716

0x4400001C

CCM_SIP_484_ADDRESS_INCOMPLETE

1157627905

0x45000001

CCM_SIP_485_AMBIGUOUS

1174405137

0x46000011

CCM_SIP_486_BUSY_HERE

1191182367

0x4700001F

CCM_SIP_487_REQUEST_TERMINATED

1207959583

0x4800001F

CCM_SIP_488_NOT_ACCEPTABLE_HERE

1258291217

0x4B000011

CCM_SIP_491_REQUEST_PENDING

1291845649

0x4D000011

CCM_SIP_493_UNDECIPHERABLE

1409286185

0x54000029

CCM_SIP_500_SERVER_INTERNAL_ERROR

1442840614

0x56000026

CCM_SIP_502_BAD_GATEWAY

1459617833

0x57000029

CCM_SIP_503_SERVICE_UNAVAILABLE

2801795135

0xA700003F

CCM_SIP_503_SERVICE_UNAVAILABLE_SER_OPTION_NOAV

1476395110

0x58000066

CCM_SIP__504_SERVER_TIME_OUT

1493172351

0x5900007F

CCM_SIP_505_SIP_VERSION_NOT_SUPPORTED

1509949567

0x5A00007F

CCM_SIP_513_MESSAGE_TOO_LARGE

2701131793

0xA1000011

CCM_SIP_600_BUSY_EVERYWHERE

2717909013

0xA2000015

CCM_SIP_603_DECLINE

2734686209

0xA3000001

CCM_SIP_604_DOES_NOT_EXIST_ANYWHERE

2751463455

0xA400001F

CCM_SIP_606_NOT_ACCEPTABLE

655360

0xA0000

CTI_REQUEST_INVALID_PRIMARY_CALL_STATE

851976

0xD0008

PREEMPTION_NON_IP

917512

0xE0008

PREEMPTION_NETWORK

301989951

0x1200003F

CCM_SIP_417_ERR_RESOURCE_PRIORITY_ROUTINE

570425365

0x22000015

CCM_SIP_433_ANONYMITY_DISALLOWED

### Redirect Reason Codes

The following table contains the available Redirect Reason Codes that may appear in a record.

Q.931 Standard Redirect Reason Codes

Value

Description

0

Unknown

1

Call Forward Busy

2

Call Forward No Answer

4

Call Transfer

5

Call Pickup

7

Call Park

8

Call Park Pickup

9

CPE Out of Order

10

Call Forward

11

Call Park Reversion

15

Call Forward all

Nonstandard Redirect Reason Codes

18

Call Deflection

34

Blind Transfer

50

Call Immediate Divert

66

Call Forward Alternate Party

82

Call Forward On Failure

98

Conference

114

Barge

129

Aar

130

Refer

146

Replaces

162

Redirection (3xx)

177

SIP-forward busy greeting

178

Call Forward Unregistered

207

Follow Me (SIP-forward all greeting)

209

Out of Service (SIP-forward busy greeting)

239

Time of Day (SIP-forward all greeting)

242

Do Not Disturb (SIP-forward no answer greeting)

257

Unavailable (SIP-forward busy greeting)

274

Away (SIP-forward no answer greeting)

303

Mobility HandIn

319

Mobility HandOut

335

Mobility Follow Me

351

Mobility Redial

354

Recording

370

Monitoring

399

Mobility IVR

401

Mobility DVOR

402

Mobility EFA

403

Mobility Session Handoff

415

Mobility Cell Pickup

418

Click to Conference

434

Forward No Retrieve

450

Forward No Retrieve Send Back to Parker

464

Call Control Discovery (indicates that the call is redirected to a PSTN failover number)

480

Intercompany Media Engine (IME)

496

IME Connection Timed Out

512

IME Not Enrolled

528

IME Socket Error

544

IME Domain Blacklisted

560

IME Prefix Blacklisted

576

IME Expired Ticket

592

IME Remote No Matching Route

608

IME Remote Unregistered

624

IME Remote IME Disabled

640

IME Remote Invalid IME Trunk URI

656

IME Remote URI not E164

672

IME Remote Called Number Not Available

688

IME Invalid Ticket

704

IME Unknown

720

IME PSTN Fallback

738

Presence Enabled Routing

752

Agent Greeting

783

NuRD

786

Native Call Queuing, queue a call

802

Native Call Queuing, de-queue a call

818

Native Call Queuing, redirect to the second destination when no agent is logged in

834

Native Call Queuing, redirect to the second destination when the queue is full

850

Native Call Queuing, redirect to the second destination when the maximum wait time in queue is reached

### OnBehalfof Codes

The following table contains the available OnBehalfof Codes that may appear in a CDR record.

Value

Description

0

Unknown

1

CctiLine

2

Unicast Shared Resource Provider

3

Call Park

4

Conference

5

Call Forward

6

Meet-Me Conference

7

Meet-Me Conference Intercepts

8

Message Waiting

9

Multicast Shared Resource Provider

10

Transfer

11

SSAPI Manager

12

Device

13

Call Control

14

Immediate Divert

15

Barge

16

Pickup

17

Refer

18

Replaces

19

Redirection

20

Callback

21

Path Replacement

22

FacCmc Manager

23

Malicious Call

24

Mobility

25

Aar

26

Directed Call Park

27

Recording

28

Monitoring

29

CCDRequestingService

30

Intercompany Media Engine

31

FallBack Manager

32

Presence Enabled Routing

33

AgentGreeting

34

NativeCallQueuing

35

MobileCallType

| Field Name | Range of Values | Description |
|---|---|---|
| cdrRecordType | 0, 1, 2 | Defines the type of record. The following valid values apply: 0—Start call detail record (not used) 1—End call detail record (CDR) 2—CMR record Default - For CDRs, this field always remains1. |
| globalCallID_callManagerId | Positive Integer | Designates a unique Unified Communications Manager identity. The Global Call ID comprises two fields: globalCallID_callId globalCallID_callManagerId. All records that are associated with a standard call have the same Global Call ID in them. Default - Ensure that this field is populated. |
| globalCallID_callId | Positive Integer | Designates a unique call identity value that is assigned to each call. The system allocates this identifier independently
                                          on each call server. Values get chosen sequentially when a call begins. A value gets assigned for each call, successful or
                                          unsuccessful. When Unified Communications Manager restarts, it checks the file for the current globalCallID_callId number and assigns the next 1000th number to the next GlobalCallID_callId. The Global Call ID consists of two fields: globalCallID_callId globalCallID_callManagerId. All records that are associated with a standard call have the same Global Call ID in them. Note For Unified Communications Manager Release 5.x and later releases, the value in the GlobalCallId CDR field survives over Unified Communications Manager restarts. In Release 4.x and earlier releases, although the GlobalCallId field is time-based, the field gets reused under
                                                      conditions of heavy traffic. Because of this behavior, problems can occur with customer billing applications and the ability
                                                      of CAR to correlate CMRs with CDRs and to correlate conference call CDRs. For Release 5.x and later releases, GlobalCallId
                                                      redesign ensures that the field retains a unique value, at least for a certain number of days. Now, the last used globalCallId_callId
                                                      value gets written to disk periodically (for every x number of calls). The value gets retrieved after a Unified Communications Manager restart, and the new globalCallId_callId value begins with this number plus x. Default - Ensure that this field is populated. | Note | For Unified Communications Manager Release 5.x and later releases, the value in the GlobalCallId CDR field survives over Unified Communications Manager restarts. In Release 4.x and earlier releases, although the GlobalCallId field is time-based, the field gets reused under
                                                      conditions of heavy traffic. Because of this behavior, problems can occur with customer billing applications and the ability
                                                      of CAR to correlate CMRs with CDRs and to correlate conference call CDRs. For Release 5.x and later releases, GlobalCallId
                                                      redesign ensures that the field retains a unique value, at least for a certain number of days. Now, the last used globalCallId_callId
                                                      value gets written to disk periodically (for every x number of calls). The value gets retrieved after a Unified Communications Manager restart, and the new globalCallId_callId value begins with this number plus x. |
| Note | For Unified Communications Manager Release 5.x and later releases, the value in the GlobalCallId CDR field survives over Unified Communications Manager restarts. In Release 4.x and earlier releases, although the GlobalCallId field is time-based, the field gets reused under
                                                      conditions of heavy traffic. Because of this behavior, problems can occur with customer billing applications and the ability
                                                      of CAR to correlate CMRs with CDRs and to correlate conference call CDRs. For Release 5.x and later releases, GlobalCallId
                                                      redesign ensures that the field retains a unique value, at least for a certain number of days. Now, the last used globalCallId_callId
                                                      value gets written to disk periodically (for every x number of calls). The value gets retrieved after a Unified Communications Manager restart, and the new globalCallId_callId value begins with this number plus x. |
| origLegCallIdentifier | Positive Integer | Identifies the originating leg of a call. Be aware that this value is unique within a cluster. If the leg of a call persists
                                          across several subcalls and CDRs (as during a call transfer), this value remains constant. Default - Ensure that this field is populated. |
| dateTimeOrigination | Integer | Identifies the date and time when the user goes off the hook or the date and time that the H.323 SETUP message is received
                                          for an incoming call. The time gets stored as UTC. Default - Ensure that this field is populated. |
| origNodeId | Positive Integer | Identifies the server, or node within a cluster, to which the originator of the call is registered at the time that the call
                                          is made. Default - Ensure that this field is populated. |
| origSpan | 0, Positive Integer | For calls that originate at a gateway, this field indicates the B-channel number of the T1, PRI, or BRI trunk where the call
                                          originates, or a zero value for FXS or FXO trunks. For H.323 gateways, the span number remains unknown, and this field contains the call leg ID of the originator. For calls that did not originate at a gateway, the value specifies zero. Default - This field gets populated based on these rules. |
| origIpAddr | Integer | Identifies the v4 IP address of the device that originates the call signaling. For Cisco Unified IP Phones , this field specifies the v4 address of the phone. For PSTN calls, this field specifies the v4address of the H.323 gateway. For intercluster calls, this field specifies the v4address of the remote Unified Communications Manager . Default - 0. If the v4 address does not exist for the originating device, this field equals 0. This field gets populated based
                                          on these rules. |
| callingPartyNumber | Text String | Specifies a numeric string of up to 25 characters that indicates the calling party number if the calling party is identified
                                          with a directory number. If the calling party uses a blended address in the identity headers, this field contains the directory number portion of the
                                          blended address. For calls that originate at a Cisco Unified IP Phone , this field shows the extension number of the line that is used. For incoming H.323 calls, this field specifies the value that is received in the Calling Party Number field in the Setup message.
                                          This field reflects any translations that are applied to the Calling Party Number before it arrives at the Unified Communications Manager (such as translations at the gateway). For the server calls, where Unified Communications Manager originates a half call without a calling party, this field may remain empty. CallingPartyNumber could contain a SIP URI. Default - This field gets populated based on these rules. |
| callingPartyUnicodeLoginUserID | Unicode – UTF_8 | Specifies the calling party login user ID. The format of this field specifies UTF_8. Default - Empty string "" . If the user ID does not exist, this field stays empty. |
| origCause_location | 0 to 15 For a list of cause code values see Call Termination Cause Codes | Specifies the Location field that is indicated in the ISDN release message for clearing causes that are received over ISDN
                                          signaling links. See topics that are related to call termination cause codes for a list of the valid values per Q.850. For clearing causes that are created internally by the Unified Communications Manager , this value specifies zero. Default - 0 |
| origCause_value | 0 to 129 For a list of cause code values see Call Termination Cause Codes | Reflects the reason for clearance for the calls that are cleared by the originating party. Unified Communications Manager currently uses the Q.850 codes and some Unified Communications Manager defined codes. See topics that are related to call termination cause codes for a listing. For calls that are cleared by the terminating party, this field specifies zero. In addition to the standard values that are described in Q.850, when a call is split by a feature (transfer or conference),
                                          the CDR terminates, and this field gets set to 393216. This represents a proprietary value for this field. Default - 0 |
| origPrecedenceLevel | 0 to 4 | Represents the precedence level of the original leg. For MLPP, each call leg includes a precedence level. Precedence 0 = FLASH OVERRIDE/ EXECUTIVE OVERRIDE Precedence 1 = FLASH Precedence 2 = IMMEDIATE Precedence 3 = PRIORITY Precedence 4 = ROUTINE Default - 4 |
| origMediaTransportAddress_IP | 0, Integer | Identifies the v4 IP address of the device that originates the media for the call. For Cisco Unified IP Phones , this field specifies the v4 address of the phone. For PSTN calls, this field specifies the v4address of the H.323 gateway. For intercluster calls, this field specifies the v4address of the remote phone. Default - 0. If media is not established or the address is not v4, this field equals 0. |
| origMediaTransportAddress_Port | 0, Positive Integer | Identifies the IP port number that is associated with the OrigMediaTransportAddress_IP field. Default - 0. If media is not established, this field stays 0. |
| origMediaCap_payloadCapability | 0, Positive Integer For a full list of codecs, see Codec Types | Identifies the codec type that the originator uses to transmit media. Unified Communications Manager currently uses the following payload capability values: 0, 1-16, 18-20, 25, 32, 33, 81-86. See topics related to codec types
                                          for a listing of the valid values. Default - 0. If media is not established, this field stays 0. |
| origMediaCap_maxFramesPerPacket | 0, Positive Integer | Identifies the number of milliseconds of data per packet that the originating party sends. This field normally gets set to
                                          10, 20, or 30 for G.729 or G.711 codecs, but the field can store any nonzero value. Default - 0. If media is not established, this field stays 0. |
| origMediaCap_g723BitRate | 0 | This field is not used in the current release of Unified Communications Manager . Default - This field will remain 0. |
| origVideoCap_Codec | 0, 100 = H.261, 101 = H.263, 103 = H.264 | Identifies the codec type that the originator uses to transmit video (H.261, H.263, or H.264.) Default - 0. If media is not established, this field stays 0. |
| origVideoCap_Bandwidth | 0, Positive Integer | Identifies the bandwidth that is measured in units of kbps. Default - 0. If media is not established, this field stays 0. |
| origVideoCap_Resolution | 0, 1 = SQCIF, 2 = QCIF, 3 = CIF, 4 = CIF4, 5 = CIF16 6 = H263 custom resolution 7 = W360P 8 = VGA 9 = W448P 10 = HD720P 11 = HD1080P 12 = CIF2 | Indicates the transmitting resolution. In the case of H.264 codec or SIP device, this field refers to the max transmitting
                                          resolution the device can transmit for this call. Default - 0. If media is not established, this field stays 0. |
| origVideoTransportAddress_IP | 0, Integer | Identifies the v4 IP address of the device that originates the call. Default - 0. If media is not established or the address is not v4, this field stays 0. |
| origVideoTransportAddress_Port | 0, Positive Integer | Identifies the video RTP port that is associated with the origVideoTransportAddress_IP field. Default - 0. If media is not established, this field stays 0. |
| origRSVPAudioStat | 0 to 5 | Provides the status of the RSVP audio reservation from originator to terminator. 0 – No reservation. 1 – RSVP Reservation Failure condition at call setup or feature invocation. 2 – RSVP Reservation Success condition at the call setup or feature invocation. 3 – RSVP Reservation No Response (RSVP Agent) condition at the call setup or feature invocation. 4 – RSVP Mid Call Failure Preempted condition (preempted after the call setup). 5 – RSVP Mid Call Failure Lost Bandwidth condition (includes all mid-call failures except MLPP preemption). Default – 0 |
| origRSVPVideoStat | 0 to 5 | Provides the status of the RSVP video reservation from originator to terminator. 0 – No reservation. 1 – RSVP Reservation Failure condition at call setup or feature invocation. 2 – RSVP Reservation Success condition at call setup or feature invocation. 3 – RSVP Reservation No Response (RSVP Agent) condition at call setup or feature invocation. 4 – RSVP MID Call Failure Preempted condition (preempted after call setup). 5 – RSVP MID Call Failure Lost Bandwidth condition (includes all mid-call failures except MLPP preemption). Default – 0 |
| destLegIdentifier | 0, Positive Integer | Identifies the terminating leg of a call. This value remains unique within a cluster. If the leg of a call persists across
                                          several sub-calls and, consequently, several CDRs (as during a call transfer), this value remains constant. Default - 0. If the destination cannot be reached, this field stays 0. |
| destNodeId | 0, Positive Integer | Identifies the location, or node within a cluster, to which the terminating party of the call is registered at the time that
                                          the call is made. Default - 0. If the destination cannot be reached, this field stays 0. |
| destSpan | 0, Positive integer | For calls that are received at a gateway, this field indicates the B channel number of the T1, PRI, or BRI trunk where the
                                          call is received, or a zero value for FXS or FXO trunks. For H.323 gateways, the span number remains unknown, and this field contains the call leg ID of the destination. For calls not terminating at a gateway, the value specifies zero. Default - 0. If the destination cannot be reached, this field stays 0. |
| destIpAddr | 0, Integer | Identifies the v4 IP address of the device that terminates the call signaling. For Cisco Unified IP Phones , this field specifies the v4 address of the phone. For PSTN calls, this field specifies the v4address of the H.323 gateway. For intercluster calls, this field specifies the v4address of the remote Unified Communications Manager . Default - 0. If the destination cannot be reached, this field stays 0. If the v4 address does not exist for this device, the
                                          field equals 0. |
| originalCalledPartyNumber | Text String | Specifies the number to which the original call was presented, prior to any call forwarding. If translation rules are configured,
                                          this number reflects the called number after the translations have been applied. If a blended address is used for the called party, this field specifies the directory number portion of the blended address. This field represents a numeric string of up to 48 characters that can be either digits or a SIP URL. Default - Empty string "" . If destination cannot be reached, or if the called party number is a directory URI, this field stays empty. |
| finalCalledPartyNumber | Text String | Specifies the phone number to which the call finally gets presented, until it is answered or rings out. If no forwarding occurs,
                                          this number shows the same number as the originalCalledPartyNumber. If the call finally gets presented to a directory URI, the field remains empty. If a blended address is used, this field specifies the directory number portion of the blended address. For calls to a conference bridge, this field contains the actual identifier of the conference bridge, which is an alphanumeric
                                          string (for example, b0019901001). This field represents an alphanumeric string that can be either digits or a SIP URL. Default - Empty string "" . If destination cannot be reached, this field stays empty. |
| finalCalledPartyUnicodeLoginUserID | Unicode – UTF_8 | Specifies the login user ID. The format of this field specifies UTF_8. Default - Empty string "" . If the user ID does not exist, this field stays empty. |
| destCause_location | 0 to 15 For a list of cause code values see Call Termination Cause Codes | For clearing causes that are received over ISDN signaling links, the ISDN release message indicates this location field. See
                                          topics that are related to call termination cause codes for a listing of the valid values per Q.850. For clearing causes that Unified Communications Manager creates internally, this value equals zero. Default - 0. If the destination cannot be reached, this field stays 0. |
| destCause_value | 0 to 129 For a list of cause code values see Call Termination Cause Codes | Reflects the reason for the calss that the destination party cleared. See topics that are related to call termination cause
                                          codes for a listing of the valid values per Q.850. For calls that the originating party clears, this field stays zero. In addition to the standard values that are described in Q.850, when a call gets split by a feature (transfer or conference),
                                          the CDR terminates, and this field gets set to 393216. This represents a proprietary value for this field. Default - 0. If the destination cannot be reached, this field stays 0. |
| destPrecedenceLevel | 0 to 4 | Represents the destination legs precedence level. For MLPP, each call leg has a precedence level. Precedence 0 = FLASH OVERRIDE Precedence 1 = FLASH Precedence 2 = IMMEDIATE Precedence 3 = PRIORITY Precedence 4 = ROUTINE Default - 4 |
| destMediaTransportAddress_IP | 0, Integer | Identifies the v4 IP address of the device that terminates the media for the call. For Cisco Unified IP Phones , this field designates the v4 address of the phone. For PSTN calls, this field designates the v4address of the H.323 gateway. For intercluster calls, this field shows the v4address of the remote phone. Default - 0. If the destination cannot be reached or the IP address of the destination is not v4, this field stays 0. |
| destMediaTransportAddress_Port | 0, Positive Integer | Identifies the IP port number that is associated with the DestMediaTransportAddress_IP field. Default - 0. If the destination cannot be reached, this field stays 0. |
| destMediaCap_payloadCapability | 0, Positive Integer For a full list of codecs, see Codec Types | Identifies the codec type that the terminating party uses to transmit media. Unified Communications Manager currently uses the following payload capability values: 0, 1-16, 18-20, 25, 32, 33, 81-86. See topics related to codec types
                                          for a listing of the valid values. Default - 0. If the destination cannot be reached, this field stays 0. |
| destMediaCap_maxFramesPerPacket | 0, Positive Integer | Identifies the number of milliseconds of data per packet that the terminating party of the call sends. This field normally
                                          gets set to 10, 20, or 30 for G.729 or G.711 codecs but can store any nonzero value. This field can specify zero if the media is never established. Default - 0. If the destination cannot be reached, this field stays 0. |
| destMediaCap_g723BitRate | 0 | This field is not used in the current release of Unified Communications Manager . Default - This field stays 0. |
| destVideoCap_Codec | 0, 100 = H.261, 101 = H.263, 103 = H.264 | Identifies the codec type that the terminating party uses to transmit video (H.261, H.263, or H.264). Default - 0. If the destination cannot be reached, this field stays 0. |
| destVideoCap_Bandwidth | 0, Positive Integer | Identifies the bandwidth, and is measured in units of kbps. Default - 0. If the destination cannot be reached, this field stays 0. |
| destVideoCap_Resolution | 0, 1 = SQCIF, 2 = QCIF, 3 = CIF, 4 = CIF4, 5 = CIF16 6 = H263 custom resolution 7 = W360P 8 = VGA 9 = W448P 10 = HD720P 11 = HD1080P 12 = CIF2 | Indicates the transmitting resolution. In the case of H.264 codec or SIP device, this field refers to the max transmitting
                                          resolution the device can transmit for this call. Default - 0. If media is not established, this field stays 0. |
| destVideoTransportAddress _IP | 0, Integer | Identifies the v4 IP address of the device that receives the call. Default - 0. If the destination cannot be reached or the IP address of the destination is not v4, this field stays 0. |
| destVideoTransportAddress_Port | 0, Positive Integer | Identifies the video RTP port that is associated with the destVideoTransportAddress_IP field. Default - 0. If the destination cannot be reached, this field stays 0. |
| destRSVPAudioStat | 0 - 5 | Designates the status of the RSVP audio reservation from terminator to originator. 0 – No reservation. 1 – RSVP Reservation Failure condition at the call setup or feature invocation. 2 – RSVP Reservation Success condition at call setup or feature invocation. 3 – RSVP Reservation No Response (RSVP Agent) condition at call setup or feature invocation. 4 – RSVP Mid Call Failure Preempted condition (preempted after call setup). 5 – RSVP Mid Call Failure Lost Bandwidth condition (includes all mid call failures except MLPP preemption). Default – 0 |
| destRSVPVideoStat | 0 - 5 | Designates the status of the RSVP video reservation from terminator to originator. 0 – No reservation. 1 – RSVP Reservation Failure condition at call setup or feature invocation. 2 – RSVP Reservation Success condition at call setup or feature invocation. 3 – RSVP Reservation No Response (RSVP Agent) condition at call setup or feature invocation. 4 – RSVP Mid Call Failure Preempted condition (preempted after call setup). 5 – RSVP Mid Call Failure Lost Bandwidth condition (includes all mid call failures except MLPP preemption). Default – 0 |
| dateTimeConnect | 0, Integer | Identifies the date and time that the call connects. The time gets stored as UTC. If the call is never answered, this value
                                          shows zero. Default - 0. If the call is never connected, this field stays 0. |
| dateTimeDisconnect | Integer | Identifies the date and time when the call is cleared. This field gets set even if the call never connects. The time gets
                                          stored as UTC. Default - Ensure that this field is populated. |
| lastRedirectDn | Text String | Specifies a numeric string of up to 25 characters. The numeric string can contain digits or a SIP URL. For forwarded calls, this field specifies the phone number of the next to last hop before the call reaches its final destination.
                                          If only one hop occurs, this number matches the OriginalCalledPartyNumber. If a blended address is used for call addressing, this field contains only the directory number portion of the blended address. For calls that are not forwarded, this field matches the OriginalCalledPartyNumber and the FinalCalledPartyNumber. For calls to a conference bridge, this field contains the actual identifier of the conference bridge, which is an alphanumeric
                                          string (for example, b0019901001). Default - Empty string "" . If the call is never redirected, or if the next to last hop address is a directory URI, this field remains empty. |
| pkid | Text String | Identifies a text string that the database uses internally to uniquely identify each row. This text string provides no meaning
                                          to the call itself. Default - A unique ID should always populate this field. |
| originalCalledPartyNumberPartition | Text String | Identifies unique partition name that is associated with the OriginalCalledPartyNumber field because Unified Communications Manager supports multiple Cisco Unified IP Phones with the same extension number in different partitions. For calls that egress through an H.323 gateway, this field uniquely specifies the partition name that is associated with the
                                          route pattern that points to the gateway. Default - Empty string "" . If the original called party does not have a partition, this field remains empty. |
| callingPartyNumberPartition | Text String | Identifies unique partition name that is associated with the CallingPartyNumber field because Unified Communications Manager supports multiple Cisco Unified IP Phones with the same extension number in different partitions. For calls that ingress through an H.323 gateway, this field remains blank. Default - Empty string "" . If the original called party does not have a partition, this field remains empty. |
| finalCalledPartyNumberPartition | Text String | Identifies unique partition name that is associated with the FinalCalledPartyNumber field because Unified Communications Manager supports multiple Cisco Unified IP Phones with the same extension number in different partitions. For calls that egress through an H.323 gateway, this field uniquely specifies the partition name that is associated with the
                                          route pattern that points to the gateway. Default - Empty string "" . If the final called party does not have a partition, this field remains empty. |
| lastRedirectDnPartition | Text String | Identifies unique partition name that is associated with the LastRedirectDn field because Unified Communications Manager supports multiple Cisco Unified IP Phones with the same extension number in different partitions. For calls that egress through an H.323 gateway, this field specifies the partition name that is associated with the route
                                          pattern that points to the gateway. Default - Empty string "" . If the last redirecting Party does not have a partition or the call was never redirected, this field stays empty. |
| duration | 0, Positive integer | Identifies the difference between the Connect Time and Disconnect Time. This field specifies the time that the call remains
                                          connected, in seconds. This field remains zero if the call never connects or if it connects for less than 1 second. Default - 0 |
| origDeviceName | Text String | Specifies the text string that identifies the name of the originating device. Default - Ensure that this field is populated. |
| destDeviceName | Text String | Specifies the text string that identifies the name of the destination device. Default - Empty string "" . If the original device does not have a name, this field stays empty. |
| origCallTerminationOnBehalfOf | 0, Positive Integer For a complete list of OnBehalfOf fields, see OnBehalfof Codes | Specifies code that identifies why the originator was terminated. For example, if the originator of the call hangs up the phone, the OnBehalfOf code shows "12" for Device. If the call terminates because of a transfer, the OnBehalfOf code shows "10" for Transfer. See topics related to CDR field descriptions for a list of the codes. This release added new OnBehalfOf codes. Default - 0 |
| destCallTerminationOnBehalfOf | 0, Positive Integer For a complete list of OnBehalfOf fields, see OnBehalfof Codes | Specifies code that identifies why the destination was terminated. For example, if the destination of the call hangs up the phone, the OnBehalfOf code shows "12" for Device. If the call terminates because of a transfer, the OnBehalfOf code shows "10" for Transfer. See topics related to CDR field descriptions for a list of the codes. This release added new OnBehalfOf codes. Default - 0 |
| origCalledPartyRedirectOnBehalfOf | 0, Positive Integer For a complete list of OnBehalfOf fields, see OnBehalfof Codes | Specifies code that identifies the reason for redirection of the original called party. For example, if the original called party was redirected because of a conference, the OnBehalfOf code specifies "4." See topics related to CDR field descriptions for a list of the codes. This release added new OnBehalfOf codes. Default - 0 |
| lastRedirectRedirectOnBehalfOf | 0, Integer For a complete list of OnBehalfOf fields, see OnBehalfof Codes | Specifies code that identifies the reason for redirection of the last redirected party. For example, if the last redirected party was redirected on behalf of a conference, the OnBehalfOf code specifies "4." See topics related to CDR field descriptions for a list of the codes. This release added new OnBehalfOf codes. Default - 0 |
| origCalledPartyRedirectReason | 0, Integer For a complete list of OnBehalfOf fields, see Redirect Reason Codes | Identifies the reason for a redirect of the original called party. See topics related to redirect reason codes for a complete list of the codes. Default - 0 |
| lastRedirectRedirectReason | 0, Integer For a complete list of OnBehalfOf fields, see Redirect Reason Codes | Identifies the last redirect reason for redirection. See topics related to redirect reason codes for a complete list of the codes. Default - 0 |
| destConversationID | 0, Integer | Specifies a unique identifier that is used to identify the parties of a conference call. For conference chaining scenarios, the origConversationID and destConversationID fields identify which conferences are chained
                                          together. Default - 0 |
| globalCallId_ClusterId | Text String | Specifies a unique ID that identifies a cluster of Unified Communications Manager s. The field is generated at installation and is not used by Unified Communications Manager . The fields globalCallId_ClusterId + globalCallId_CMId + globalCallId_CallId make up this unique key. Default - This field should always be populated. |
| joinOnBehalfOf | 0, Integer For a complete list of OnBehalfOf fields, see OnBehalfof Codes | Specifies code that identifies the reason for a join. For example, if the join takes place on behalf of a transfer, the OnBehalfOf code specifies "10." See topics related to CDR field descriptions for a list of the codes. Default - 0 |
| comment | Text String | Allows features to add text to the CDRs. This text can describe details about the call. For example, the following field flags malicious calls: Tag—CallFlag Value—MALICIOUS Default - Empty string "" . |
| authCodeDescription | Text String | Provides a description of the FAC. Default - Empty string "" or null. |
| authorizationLevel | 0, Integer | Displays the level of the FAC. Default - 0 |
| clientMatterCode | Text String | Displays the client matter code. Before the system extends a call, the user enters a client matter code that can be used for
                                          assigning account or billing codes to calls. Default - Empty string "" or null. |
| origDTMFMethod | 0, Positive Integer | Displays the DTMF method that the originator uses. 0 - No DTMF - Use ANY matched DTMF. 1 - OOB - Use OOB if endpoints behind SIPTrunk support it. 2 - 2833 - Use RFC2833 if endpoints behind SIPTrunk support it. 3 - OOB and 2833 - Use both KPML and RFC2833 if endpoints behind SIPTrunk can support both. 4 - Unknown Default - 0 (No preference) |
| destDTMFMethod | 0, Positive Integer | Displays the DTMF method that the destination uses. 0 - No DTMF - Use ANY matched DTMF.1 - OOB - Use OOB if endpoints behind SIPTrunk support it.2 - 2833 - Use RFC2833 if endpoints
                                          behind SIPTrunk support it.3 - OOB and 2833 - Use both KPML and RFC2833 if endpoints behind SIPTrunk can support both.4 -
                                          Unknown. Default - 0 (No preference) |
| callSecuredStatus | 0, Positive Integer | Displays the highest security status that is reached during a call. For example, if the call is originally unsecured, and
                                          later the call changes to secured, the CDR contains 1 for "Secured" even though different portions of the call have different status values. 0 - Non-secured 1 - Authenticated (not encrypted) 2 - Secured (encrypted) Default - 0 (Non-secured) |
| origConversationID | Integer | Identifies the conference ID that is associated with the originating leg of the call. In most cases, this field equals 0. For conference chaining scenarios, the origConversationID and destConversationID fields identify which conferences are chained
                                          together. Default - 0 |
| origMediaCap_Bandwidth | 0, Positive Integer | Displays the media bandwidth that is used at the origination of the call. Default - 0 |
| destMediaCap_Bandwidth | 0, Positive Integer | Displays the media bandwidth that is used at the destination of the call. Default - 0 |
| authorizationCodeValue | Text String | Displays the Forced Authorization Code (FAC) that is associated with the call. Default - Empty string "" or null. |
| outpulsedCallingPartyNumber | Text String | Comprises an alphanumeric string of up to 50 characters. The calling party number gets outpulsed from the device. This field gets populated only when normalization or localization
                                          takes place at the device. Default - Empty string "" or null. |
| outpulsedCalledPartyNumber | Text String | Comprises an alphanumeric string of up to 50 characters. The called party number gets outpulsed from the device. This field gets populated only when normalization or localization
                                          takes place at the device. Default - Empty string "" or null. |
| origIpv4v6Addr | Text string | Comprises an alphanumeric string of up to 64 characters. This field identifies the IP address of the device that originates the call signalling. The field can be either IPv4 or IPv6
                                          format depending on the type of IP address that gets used for the call. For Cisco Unified IP Phones , this field is the address of the Cisco Unified IP Phone . For PSTN calls, this field is the address of the gateway. For intercluster calls, this field is the address of the remote Unified Communications Manager . The IP addressis either in dotted decimal format or in colon separated hexadecimal format. Default - TheIP address of the originating device as reported by the device or used for the call after media negotiation. |
| destIpv4v6Addr | Text string | Comprises an alphanumeric string of up to 64 characters. This field identifies the IP address of the device that terminates the call signalling. The field can be either in IPv4 or
                                          IPv6 format depending upon the type of IP address that gets used for the call. For Cisco Unified IP Phones , this field is the address of the Cisco Unified IP Phone . For PSTN calls, this field is the address of the gateway. For intercluster calls, this field is the address of the remote Unified Communications Manager . The IP addressis either in dotted decimal format or in colon separated hexadecimal format. Default - Empty String "" or null. If the destination does not get reached, this field stays empty. |
| origVideoCap_Codec_Channel2 | 0, 100 = H.261, 101 = H.263, 103 = H.264, | Identifies the codec type that the originator uses to transmit video (H.261, H.263, or H.264) for the second video channel. Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0. |
| origVideoCap_Bandwidth_Channel2 | 0, Positive integer | Identifies the bandwidth measured in units of kbps for the second video channel. Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0. |
| origVideoCap_Resolution_Channel2 | 0, 1 = SQCIF, 2 = QCIF, 3 = CIF, 4 = CIF4, 5 = CIF16 6 = H263 custom resolution 7 = W360P 8 = VGA 9 = W448P 10 = HD720P 11 = HD1080P 12 = CIF2 | Indicates the transmitting resolution for the second video channel. In the case of H.264 codec or SIP device, this field refers
                                          to the maximum transmitting resolution the device can transmit for this call. Default - 0. If media is not established, this field stays 0. Also, if H.239 and BFCP are not supported for this call, this
                                          field displays 0. |
| origVideoTransportAddress_IP_Channel2 | 0, Integer | Identifies the v4 IP address of the device that originates the call for the second video channel. Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0. |
| origVideoTransportAddress_Port_Channel2 | 0, Positive integer | Identifies the video RTP port associated with the origH239VideoTransportAddress_IP field for the second video channel. Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0. |
| origVideoChannel_Role_Channel2 | 0 = Presentation role, 1 = Live role, Positive integer | Identifies the H.239 video channel role of the device that originates. Default - 0. If media does not get established, this field displays 0. Also, if H.239 is not supported, this field displays
                                          0. |
| destVideoCap_Codec_Channel2 | 0, 100 = H.261, 101 = H.263, 103 = H.264 | Identifies the codec type that the terminating party uses to transmit video (H.261, H.263, or H.264) for the second video
                                          channel. Default - 0. If the destination cannot be reached, this field stays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0. |
| destVideoCap_Bandwidth_Channel2 | 0, Positive integer | Identifies the bandwidth measured in units of kbps for the second video channel. Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0. |
| destVideoCap_Resolution_Channel2 | 0, 1 = SQCIF, 2 = QCIF, 3 = CIF, 4 = CIF4, 5 = CIF16 6 = H263 custom resolution 7 = W360P 8 = VGA 9 = W448P 10 = HD720P 11 = HD1080P 12 = CIF2 | Indicates the transmitting resolution for the second video channel. In the case of H.264 codec or SIP device, this field refers
                                          to the maximum transmitting resolution the device can transmit for this call. Default - 0. If media is not established, this field stays 0. Also, if H.239 and BFCP are not supported for this call, this
                                          field displays 0. |
| destVideoTransportAddress_IP_Channel2 | 0, Integer | Identifies the v4 IP address of the device that receives the call. Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0. |
| destVideoTransportAddress_Port_Channel2 | 0, Positive integer | Identifies the video RTP port associated with the destH239VideoTransportAddress_IP field. Default - 0. If media does not get established, this field displays 0. Also, if H.239 and BFCP are not supported for this
                                          call, this field displays 0. |
| destVideoChannel_Role_Channel2 | 0 = Presentation role, 1 = Live role, Positive integer | Identifies the H.239 video channel role of the device that receives the call. Default - 0. If media does not get established, this field displays 0. Also, if H.239 is not supported, this field displays
                                          0. |
| incomingProtocolID | 0 = Unknown, 1 = SIP, 2 = H323, 3 = CTI/JTAPI, 4 = Q931, Integer | Identifies the protocol (SIP, H.323, CTI/JTAPI, or Q.931) used between Cisco Unified CM and the upstream voice product in
                                          the call path. |
| incomingProtocolCallRef | Varchar(32) | Identifies the globally unique call reference identification for the protocol. The value is received from the upstream voice
                                          product. The value is alpha–numeric and truncated to 32 characters. |
| outgoingProtocolID | 0 = Unknown, 1 = SIP, 2 = H323, 3 = CTI/JTAPI, 4 = Q931, Integer | Identifies the protocol (SIP, H.323, CTI/JTAPI, or Q.931) used between Cisco Unified CM and the downstream voice product in
                                          the call path. |
| outgoingProtocolCallRef | Varchar(32) | Identifies the globally unique call reference identification for the protocol. The value is passed to the next downstream
                                          voiced product. The value is alpha–numeric and truncated to 32 characters. |
| currentRoutingReason | Positive Integer For field values see Routing Reason Values for External Call Control | Displays the reason why the call was intercepted for the active call. This field is used with the external call control feature.
                                          See topics related to routing reason values for external call control for a list of reasons. Default value is 0. |
| origRoutingReason | Positive Integer For a complete list of OnBehalfOf fields, see OnBehalfof Codes | Displays the reason why the call was intercepted for the first time. This field is used with the external call control feature,
                                          See topics related to routing reason values for external call control for a list of reasons. Default value is 0. |
| lastRedirectingRoutingReason | Positive Integer For a complete list of OnBehalfOf fields, see OnBehalfof Codes | Displays why the call was intercepted for the last time. This field is used with the external call control feature. See topics
                                          related to routing reason values for external call control for a list of reasons. Default - Empty string. |
| huntPilotPartition | Text String | Indicates the partition for the hunt pilot DN. Default - Empty string. |
| huntPilotDN | Text String | Indicates the hunt pilot DN through which the call is routed. Default - Empty string. |
| calledPartyPatternUsage | Positive Integer | Indicates the pattern of the called party. Default value specifies 5 (PATTERN_ROUTE). If the huntPilotDN is populated, use the huntPilotDN field value as the hunt pilot. If the huntPilotDN is not available, check the pattern usage (7 =PATTERN_HUNT_PILOT) in the CDR table to identify the call
                                                type. If this call is a hunt list call, use the finalCalledPartyNumber as the huntPilotDN. Possible value for the fields: 0 CallPark PATTERN_CALL_PARK 1 Conference PATTERN_CONF 2 Device PATTERN_DEVICE 3 Translation PATTERN_TRANSLATION 4 Call Pick Up Group PATTERN_CALL_PICK_UP_GROUP 5 Route PATTERN_ROUTE 6 Message Waiting PATTERN_MESSAGE_WAITING 7 Hunt Pilot PATTERN_HUNT_PILOT 8 Voice Mail Port PATTERN_VOICE_MAIL_PORT 9 Domain Routing PATTERN_ROUTE_DOMAIN 10 IPAddress Routing PATTERN_ROUTE_IPNET 11 Device template PATTERN_DEVICE_TEMPLATE 12 Directed Call Park PATTERN_DIRECTED_CALL_PARK 13 Device Intercom PATTERN_DEVICE_INTERCOM 14 Translation Intercom PATTERN_TRANSLATION_INTERCOM 15 Translation Calling Party Number PATTERN_TRANSLATION_CALLING_PARTY_NUMBER 16 Mobility Handoff PATTERN_MOBILITY_HANDOFF 17 Mobility DTMF PATTERN_MOBILITY_DTMF 18 Mobility IVR PATTERN_MOBILITY_IVR 19 Device Intercom Template PATTERN_DEVICE_INTERCOM_TEMPLATE |
| incomingICID | Text String | Specifies alphanumeric string up to 50 characters. This field is populated with the IMS Identifier(ICID) from the P-Charging Vector at the incoming call leg of the call. This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled. Default = Empty String " " |
| incomingOrigIOI | Text String | Specifies alphanumeric string up to 50 characters. This field is populated with the originating Interoperator Identifier(IOI) from the P-Charging Vector at the incoming call
                                          leg of the call. This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled. Default = Empty String " " |
| incomingTermIOI | Text String | Specifies alphanumeric string up to 50 characters. This field is populated with the terminating Interoperator Identifier(IOI) from the P-Charging Vector at the incoming call
                                          leg of the call. This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled. Default = Empty String " " |
| outgoingICID | Text String | Specifies alphanumeric string up to 50 characters. This field is populated with the IMS Identifier(ICID) from the P-Charging Vector at the outgoing call leg of the call. This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled. Default = Empty String " " |
| outgoingOrigIOI | Text String | Specifies alphanumeric string up to 50 characters. This field is populated with the originating Interoperator Identifier(IOI) from the P-Charging Vector at the outgoing call
                                          leg of the call. This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled. Default = Empty String " " |
| outgoingTermIOI | Text String | Specifies alphanumeric string up to 50 characters. This field is populated with the terminating Interoperator Identifier(IOI) from the P-Charging Vector at the outgoing call
                                          leg of the call. This field will be empty when the call leg has no IMS or SIP trunk with P-Charging-Vector enabled. Default = Empty String " " |
| outpulsedOriginalCalledPartyNumber | Text String | Specifies alphanumeric string up to 50 characters. The Original called party number outpulsed from the device. Refer to section on Redirecting Number Transformation for details. Default = Empty String " " |
| outpulsedLastRedirectingNumber | Text String | Specifies alphanumeric string up to 50 characters. The Last Redirecting number outpulsed from the device. Refer to section on Redirecting Number Transformation for details. Default = Empty String " " |
| wasCallQueued | Positive Integer | Specifies whether the call has been put into a queue or not. A value of 0 means that the call is not put into any queue; 1
                                          means the call has been put into a queue. |
| totalWaitTimeInQueue | Positive Integer | Specifies how long a caller has been put into a queue. The value is specified in second. The value is 0 if the call is never
                                          put into any queue. |
| callingPartyNumber_uri | Text String | Specifies an alphanumeric string of up to 254 characters that identifies the calling party if the calling party uses a directory
                                          URI for call addressing. If the calling party uses a blended address in the identity headers, this field contains the directory URI portion of the
                                          blended address. Default - Empty string "" . If the calling party does not use a directory URI, the field stays empty. |
| originalCalledPartyNumber_uri | Text String | Specifies a string of up to 254 alphanumeric characters that specifies the directory URI to which the original call was addressed,
                                          prior to any call forwarding, provided the call was addressed to a directory URI. If a blended address is used for the called party, this field specifies the directory URI portion of the blended address. Default - Empty string "" . If destination cannot be reached, or if the called party is a directory number, this field stays empty. |
| finalCalledPartyNumber_uri | Text String | Specifies an alphanumeric string of up to 254 characters that indicate the directory URI address to which the call finally
                                          gets presented, if the final address is a directory URI. If no forwarding occurs, this field shows the same directory URI
                                          as the originalCalledPartyNumber_uri field. If a blended address is used for the called number, this field specifies the directory URI portion of the blended address. For calls to a conference bridge, this field contains the actual identifier of the conference bridge, which is an alphanumeric
                                          string (for example, b0019901001). Default - Empty string "" . If destination cannot be reached, or if a directory number is used for called addressing, this field stays empty. |
| lastRedirectDn_uri | Text String | Specifies an alphanumeric string of up to 254 characters. For forwarded calls that use a directory URI for addressing, this field specifies the directory URI of the next to last hop
                                          before the call reaches its final destination. If only one hop occurs, this number matches the originalCalledPartyNumber_uri. If a blended address is used, this field contains only the directory URI portion of the blended address. For calls that are not forwarded, this field matches the originalCalledPartyNumber_uri and the finalCalledPartyNumber_uri. For calls to a conference bridge, this field contains the actual identifier of the conference bridge, which is an alphanumeric
                                          string (for example, b0019901001). Default - Empty string "" . If the call is never redirected, or if the address is a directory number, this field remains empty. |
| mobileCallingPartyNumber | Text string | Specifies the mobile cellular number if the original calling device is a mobile device. If the original calling device is not a mobile device, this field remains empty. Default - Empty string |
| finalMobileCalledPartyNumber | Text string | Specifies the mobile called party if the final called device is a mobile device. If the final called device is not a mobile device, this field remains empty. Default - Empty string |
| origMobileDeviceName | Text string | Specifies the device name of the calling party if the call is placed from a mobile device. If the mobile call uses a remote destination profile, the device name is the mobile number and remote destination profile
                                          name. For example, mobileNumber: RDP-name. If the mobile device uses a mobile identity, the device name is the mobile identity name. If the original device is not a mobile device, this field remains empty. Default - Empty string |
| destMobileDeviceName | Text string | Specifies the name of the destination mobile device. If the mobile device uses a remote destination profile the device name is the mobile number and remote destination profile
                                          name. For example, mobileNumber: RDP-name. If the mobile device uses a mobile identity, the device name is the mobile identity name. If the destination device is not a mobile device, this field remains empty. Default - Empty string |
| origMobileCallDuration | Positive integer | Specifies the call duration in the mobile network of the originating device if the calling party is a mobile device. If the calling party is not a mobile device, this field remains empty. Default - 0 |
| destMobileCallDuration | Positive integer | Specifies the call duration in the mobile network for the destination device if the destination device is a mobile device. If the destination device is not a mobile device, this field remains empty. Default - 0 |
| mobileCallType | Positive integer | Specifies the mobility feature that is invoked for this mobile call. Default - 0 |
| originalCalledPartyPattern | Text String | Specifies numeric string (with special characters) up to 50 characters. This is the pattern to which the original call was placed before any configured translation is applied. Calls to Translation Pattern will always populate the pattern after applying the configured transformation on the translation
                                          pattern. Default—empty string "" . |
| finalCalledPartyPattern | Text String | Specifies numeric string (with special characters) string up to 50 characters. The pattern of the final called party to which the call is presented until that call is answered or ringing has ended. If
                                          no forwarding occurred, this pattern is the same as originalCalledPartyPattern. This field indicates the pattern before any
                                          configured translation rules are applied. This value is the same as the finalCalledPartyNumber if the number is a direct match without any translation Default—empty string "" . |
| lastRedirectingPartyPattern | Text String | Specifies numeric string (with special characters) string up to 50 characters. The pattern of the last party which redirected the call to the current called party. If there is no redirection, the field
                                          has the same value as the originalCalledPartyPattern. Default—empty string "" . |
| huntPilotPattern | Text String | Specifies numeric string (with special characters) string up to 50 characters. The huntPilot pattern as configured in the database. This field is populated only when the HuntPilot member answers the call
                                          which is placed either directly or due to redirection to the huntPilot. Default - empty string "". If no huntPilot member answers, this field is empty. |
| origDeviceType | Text String | Indicates whether the device that initiated the call was a Spark client that is anchored to Cisco Unified Communications Manager
                                          over the Spark Remote Device: If yes, this field indicates "CiscoSparkRemoteDevice" If no, this field is empty. |
| destDeviceType | Text String | Indicates whether the device that was called was a Spark client that is anchored to Cisco Unified Communications Manager over
                                          the Spark Remote Device: If yes, this field indicates "CiscoSparkRemoteDevice" If no, this field is empty. Note If the Spark client "rings" and the CDR Log Calls with Zero Duration Flag service parameter is True, this field gets populated
                                                      as 'CiscoSparkRemoteDevice' even if an enterprise number was dialed with "Ring all shared lines" configured. | Note | If the Spark client "rings" and the CDR Log Calls with Zero Duration Flag service parameter is True, this field gets populated
                                                      as 'CiscoSparkRemoteDevice' even if an enterprise number was dialed with "Ring all shared lines" configured. |
| Note | If the Spark client "rings" and the CDR Log Calls with Zero Duration Flag service parameter is True, this field gets populated
                                                      as 'CiscoSparkRemoteDevice' even if an enterprise number was dialed with "Ring all shared lines" configured. |
| origDeviceSessionID | Text String | Indicates the call Session ID of the originating device. When the session terminates, the system generates a CDR record and the field is populated with the originating device Session
                                          ID for the particular call. Note If the CDR service parameter 'CDR Log Calls with Zero Duration Flag' is set to 'True', this field is populated even though
                                                      the call is not answered. The maximum length of this field is restricted to 127 characters. For example, origDeviceSessionID = ab30317fla784dc48fl824d0d3715d86 Default—empty string "" . | Note | If the CDR service parameter 'CDR Log Calls with Zero Duration Flag' is set to 'True', this field is populated even though
                                                      the call is not answered. |
| Note | If the CDR service parameter 'CDR Log Calls with Zero Duration Flag' is set to 'True', this field is populated even though
                                                      the call is not answered. |
| destDeviceSessionID | Text String | Indicates the call Session ID of the destination device. When the session terminates, the system generates a CDR record and the field is populated with the destination device Session
                                          ID for the particular call. The maximum length of this field is restricted to 127 characters. For example, destDeviceSessionID = 47755a9de7794ba387653f2099600ef2 Default—empty string "" . |

| Note | For Unified Communications Manager Release 5.x and later releases, the value in the GlobalCallId CDR field survives over Unified Communications Manager restarts. In Release 4.x and earlier releases, although the GlobalCallId field is time-based, the field gets reused under
                                                      conditions of heavy traffic. Because of this behavior, problems can occur with customer billing applications and the ability
                                                      of CAR to correlate CMRs with CDRs and to correlate conference call CDRs. For Release 5.x and later releases, GlobalCallId
                                                      redesign ensures that the field retains a unique value, at least for a certain number of days. Now, the last used globalCallId_callId
                                                      value gets written to disk periodically (for every x number of calls). The value gets retrieved after a Unified Communications Manager restart, and the new globalCallId_callId value begins with this number plus x. |
|---|---|

| Note | If the Spark client "rings" and the CDR Log Calls with Zero Duration Flag service parameter is True, this field gets populated
                                                      as 'CiscoSparkRemoteDevice' even if an enterprise number was dialed with "Ring all shared lines" configured. |
|---|---|

| Note | If the CDR service parameter 'CDR Log Calls with Zero Duration Flag' is set to 'True', this field is populated even though
                                                      the call is not answered. |
|---|---|

| Field Value | Reason | Description |
|---|---|---|
| 0 | PDPDecision_NONE | This value indicates that the route server did not return a routing directive to the Unified Communications Manager . |
| 1 | PDPDecision_Allow_Fulfilled | This value indicates that Unified Communications Manager allowed a call. |
| 2 | PDPDecision_Allow_Unfulfilled | This value indicates that Unified Communications Manager disallowed a call. |
| 3 | PDPDecision_Divert_Fulfilled | This value indicates that Unified Communications Manager diverted the call. |
| 4 | PDPDecision_Divert_Unfulfilled | This value indicates that Unified Communications Manager was not able to divert the call. |
| 5 | PDPDecision_Forward_Fulfilled | This value indicates that Unified Communications Manager forwarded the call. |
| 6 | PDPDecision_Forward_Unfulfilled | This value indicates that Unified Communications Manager was unable to forward the call. |
| 7 | PDPDecision_Reject_Fulfilled | This value indicates that Unified Communications Manager rejected the call. |
| 8 | PDPDecision_Reject_Unfulfilled | This value indicates that Unified Communications Manager was not able to reject the call. |

| Value | Description |
|---|---|
| 1 | NonStandard |
| 2 | G711Alaw 64k |
| 3 | G711Alaw 56k |
| 4 | G711mu-law 64k |
| 5 | G711mu-law 56k |
| 6 | G722 64k |
| 7 | G722 56k |
| 8 | G722 48k |
| 9 | G7231 |
| 10 | G728 |
| 11 | G729 |
| 12 | G729AnnexA |
| 13 | Is11172AudioCap |
| 14 | Is13818AudioCap |
| 15 | G.729AnnexB |
| 16 | G.729 Annex AwAnnexB |
| 18 | GSM Full Rate |
| 19 | GSM Half Rate |
| 20 | GSM Enhanced Full Rate |
| 25 | Wideband 256K |
| 32 | Data 64k |
| 33 | Data 56k |
| 40 | G7221 32K |
| 41 | G7221 24K |
| 42 | AAC |
| 43 | MP4ALATM_128 |
| 44 | MP4ALATM_64 |
| 45 | MP4ALATM_56 |
| 46 | MP4ALATM_48 |
| 47 | MP4ALATM_32 |
| 48 | MP4ALATM_24 |
| 49 | MP4ALATM_NA |
| 80- | GSM |
| 81 | ActiveVoice |
| 82 | G726 32K |
| 83 | G726 24K |
| 84 | G726 16K |
| 86 | iLBC |
| 89 | iSAC |
| 90 | OPUS |
| 100 | H261 |
| 101 | H263 |
| 102 | Vieo |
| 103 | H264 |
| 104 | H264_SVC |
| 105 | T120 |
| 106 | H224 |
| 107 | T38Fax |
| 108 | TOTE |
| 109 | H265 |
| 110 | H264_UC |
| 111 | XV150_MR_711U |
| 112 | NSE_VBD_711U |
| 113 | XV150_MR_729A |
| 114 | NSE_VBD_729A |
| 115 | H264_FEC |
| 120 | Clear_Chan |
| 222 | Universal_Xcoder |
| 257 | RFC2833_DynPayload |
| 258 | PassThrough |
| 259 | Dynamic_Payload_PassThru |
| 260 | DTMF_OOB |
| 261 | Inband_DTMF_RFC2833 |
| 299 | NoAudio |
| 300 | v150_LC_ModemRelay |
| 301 | v150_LC_SPRT |
| 302 | v150_LC_SSE |
| 303 | T38 fax |

| Note | Cause Code is defined in call control as Natural number. It is a 32 bit unsigned (long) positive integer with values ranging
                                             from 0 to +4,294,967,295. |
|---|---|

| Code | Description |
|---|---|
| 0 | No error |
| 1 | Unallocated (unassigned) number |
| 2 | No route to specified transit network (national use) |
| 3 | No route to destination |
| 4 | Send special information tone |
| 5 | Misdialed trunk prefix (national use) |
| 6 | Channel unacceptable |
| 7 | Call awarded and being delivered in an established channel |
| 8 | Preemption |
| 9 | Preemption—circuit reserved for reuse |
| 16 | Normal call clearing |
| 17 | User busy |
| 18 | No user responding |
| 19 | No answer from user (If "No Answer Ring duration" value is greater than the T301 Timer value and after T301 Timer expiry,
                                             Call Forwarding No Answer(CFNA) Feature would be invoked). |
| 20 | Subscriber absent |
| 21 | Call rejected |
| 22 | Number changed |
| 25 | Natural Exchange Routing Error |
| 26 | Non-selected user clearing |
| 27 | Destination out of order |
| 28 | Invalid number format (address incomplete) |
| 29 | Facility rejected |
| 30 | Response to STATUS ENQUIRY |
| 31 | Normal, unspecified |
| 34 | No circuit/channel available |
| 38 | Network out of order |
| 39 | Permanent frame mode connection out of service |
| 40 | Permanent frame mode connection operational |
| 41 | Temporary failure |
| 42 | Switching equipment congestion |
| 43 | Access information discarded |
| 44 | Requested circuit/channel not available |
| 46 | Precedence call blocked |
| 47 | Resource unavailable, unspecified |
| 49 | Quality of Service not available |
| 50 | Requested facility not subscribed |
| 53 | Service operation violated |
| 54 | Incoming calls barred |
| 55 | Incoming calls barred within Closed User Group (CUG) |
| 57 | Bearer capability not authorized |
| 58 | Bearer capability not presently available |
| 62 | Inconsistency in designated outgoing access information and subscriber class |
| 63 | Service or option not available, unspecified |
| 65 | Bearer capability not implemented |
| 66 | Channel type not implemented |
| 69 | Requested facility not implemented |
| 70 | Only restricted digital information bearer capability is available (national use) |
| 79 | Service or option that is not implemented, unspecified |
| 81 | Invalid call reference value |
| 82 | Identified channel does not exist |
| 83 | A suspended call exists, but this call identity does not |
| 84 | Call identity in use |
| 85 | No call suspended |
| 86 | Call having the requested call identity has been cleared |
| 87 | User not member of CUG (Closed User Group) |
| 88 | Incompatible destination |
| 90 | Destination number missing and DC not subscribed |
| 91 | Invalid transit network selection (national use) |
| 95 | Invalid message, unspecified |
| 96 | Mandatory information element is missing |
| 97 | Message type nonexistent or not implemented |
| 98 | Message is not compatible with the call state, or the message type is nonexistent or not implemented |
| 99 | An information element or parameter does not exist or is not implemented |
| 100 | Invalid information element contents |
| 101 | The message is not compatible with the call state |
| 102 | Call terminated when timer expired; a recovery routine that is executed to recover from the error |
| 103 | Parameter nonexistent or not implemented - passed on (national use) |
| 110 | Message with unrecognized parameter discarded |
| 111 | Protocol error, unspecified |
| 122 | Precedence Level Exceeded |
| 123 | Device not Preemptable |
| 125 | Out of bandwidth (Cisco specific) |
| 126 | Call split (Cisco specific) |
| 127 | Interworking, unspecified |
| 129 | Precedence out of bandwidth |
| 130 | Natural Isolated Code |
| 131 | Call Control Discovery PSTN Failover (Cisco specific) |
| 132 | IME QOS Fallback (Cisco specific) |
| 133 | PSTN Fallback locate Call Error (Cisco specific) |
| 134 | PSTN Fallback wait for DTMF Timeout (Cisco specific) |
| 135 | IME Failed Connection Timed out (Cisco specific) |
| 136 | IME Failed not enrolled (Cisco specific) |
| 137 | IME Failed socket error (Cisco specific) |
| 138 | IME Failed domain blocked (Cisco specific) |
| 139 | IME Failed prefix blocked (Cisco specific) |
| 140 | IME Failed expired ticket (Cisco specific) |
| 141 | IME Failed remote no matching route (Cisco specific) |
| 142 | IME Failed remote unregistered (Cisco specific) |
| 143 | IME Failed remote IME disabled (Cisco specific) |
| 144 | IME Failed remote invalid IME trunk URI (Cisco specific) |
| 145 | IME Failed remote URI not E164 (Cisco specific) |
| 146 | IME Failed remote called number not available (Cisco specific) |
| 147 | IME Failed Invalid Ticket (Cisco specific) |
| 148 | IME Failed unknown (Cisco specific) |
| 155 | DCC Allowed Percentage Exceeded |

| Decimal Value Code | Hex Value Code | Description |
|---|---|---|
| 262144 | 0x40000 | Conference Full (was 124) |
| 393216 | 0x60000 | Call split (was 126) This code applies when a call terminates during a transfer operation because it was split off and terminated
                                             (was not part of the final transferred call). This code can help you to determine which calls terminated as part of a feature
                                             operation. |
| 458752 | 0x70000 | Conference drop any party/Conference drop last party (was 128) |
| 16777257 | 0x1000029 | CCM_SIP_400_BAD_REQUEST |
| 33554453 | 0x2000015 | CCM_SIP_401_UNAUTHORIZED |
| 50331669 | 0x3000015 | CCM_SIP_402_PAYMENT_REQUIRED |
| 67108885 | 0x4000015 | CCM_SIP_403_FORBIDDEN |
| 83886081 | 0x5000001 | CCM_SIP_404_NOT_FOUND |
| 100663359 | 0x600003F | CCM_SIP_405_METHOD_NOT_ALLOWED |
| 117440591 | 0x700004F | CCM_SIP_406_NOT_ACCEPTABLE |
| 134217749 | 0x8000015 | CCM_SIP_407_PROXY_AUTHENTICATION_REQUIRED |
| 150995046 | 0x9000066 | CCM_SIP_408_REQUEST_TIMEOUT |
| 184549398 | 0xB000016 | CCM_SIP__410_GONE |
| 201326719 | 0xC00007F | CCM_SIP_411_LENGTH_REQUIRED |
| 234881151 | 0xE00007F | CCM_SIP_413_REQUEST_ENTITY_TOO_LONG |
| 251658367 | 0xF00007F | CCM_SIP_414_REQUEST_URI_TOO_LONG |
| 268435535 | 0x1000004F | CCM_SIP_415_UNSUPPORTED_MEDIA_TYPE |
| 285212799 | 0x1100007F | CCM_SIP_416_UNSUPPORTED_URI_SCHEME |
| 83886207 | 0x1500007F | CCM_SIP_420_BAD_EXTENSION |
| 369098879 | 0x1600007F | CCM_SIP_421_EXTENSION_REQUIRED |
| 402653311 | 0x1800007F | CCM_SIP_423_INTERVAL_TOO_BRIEF |
| 419430421 | 0x19000015 | CCM_SIP_424_BAD_LOCATION_INFO |
| 503316501 | 0x1E000015 | CCM_SIP_429_PROVIDE_REFER_IDENTITY |
| 1073741842 | 0x40000012 | CCM_SIP_480_TEMPORARILY_UNAVAILABLE |
| 1090519081 | 0x41000029 | CCM_SIP_481_CALL_LEG_DOES_NOT_EXIST |
| 1107296281 | 0x42000019 | CCM_SIP_482_LOOP_DETECTED = 0x42000000 + EXCHANGE_ROUTING_ERROR |
| 1124073497 | 0x43000019 | CCM_SIP_483_TOO_MANY_HOOPS |
| 1140850716 | 0x4400001C | CCM_SIP_484_ADDRESS_INCOMPLETE |
| 1157627905 | 0x45000001 | CCM_SIP_485_AMBIGUOUS |
| 1174405137 | 0x46000011 | CCM_SIP_486_BUSY_HERE |
| 1191182367 | 0x4700001F | CCM_SIP_487_REQUEST_TERMINATED |
| 1207959583 | 0x4800001F | CCM_SIP_488_NOT_ACCEPTABLE_HERE |
| 1258291217 | 0x4B000011 | CCM_SIP_491_REQUEST_PENDING |
| 1291845649 | 0x4D000011 | CCM_SIP_493_UNDECIPHERABLE |
| 1409286185 | 0x54000029 | CCM_SIP_500_SERVER_INTERNAL_ERROR |
| 1442840614 | 0x56000026 | CCM_SIP_502_BAD_GATEWAY |
| 1459617833 | 0x57000029 | CCM_SIP_503_SERVICE_UNAVAILABLE |
| 2801795135 | 0xA700003F | CCM_SIP_503_SERVICE_UNAVAILABLE_SER_OPTION_NOAV |
| 1476395110 | 0x58000066 | CCM_SIP__504_SERVER_TIME_OUT |
| 1493172351 | 0x5900007F | CCM_SIP_505_SIP_VERSION_NOT_SUPPORTED |
| 1509949567 | 0x5A00007F | CCM_SIP_513_MESSAGE_TOO_LARGE |
| 2701131793 | 0xA1000011 | CCM_SIP_600_BUSY_EVERYWHERE |
| 2717909013 | 0xA2000015 | CCM_SIP_603_DECLINE |
| 2734686209 | 0xA3000001 | CCM_SIP_604_DOES_NOT_EXIST_ANYWHERE |
| 2751463455 | 0xA400001F | CCM_SIP_606_NOT_ACCEPTABLE |
| 655360 | 0xA0000 | CTI_REQUEST_INVALID_PRIMARY_CALL_STATE |
| 851976 | 0xD0008 | PREEMPTION_NON_IP |
| 917512 | 0xE0008 | PREEMPTION_NETWORK |
| 301989951 | 0x1200003F | CCM_SIP_417_ERR_RESOURCE_PRIORITY_ROUTINE |
| 570425365 | 0x22000015 | CCM_SIP_433_ANONYMITY_DISALLOWED |

| Q.931 Standard Redirect Reason Codes |
|---|
| Value | Description |
| 0 | Unknown |
| 1 | Call Forward Busy |
| 2 | Call Forward No Answer |
| 4 | Call Transfer |
| 5 | Call Pickup |
| 7 | Call Park |
| 8 | Call Park Pickup |
| 9 | CPE Out of Order |
| 10 | Call Forward |
| 11 | Call Park Reversion |
| 15 | Call Forward all |
| Nonstandard Redirect Reason Codes |
| 18 | Call Deflection |
| 34 | Blind Transfer |
| 50 | Call Immediate Divert |
| 66 | Call Forward Alternate Party |
| 82 | Call Forward On Failure |
| 98 | Conference |
| 114 | Barge |
| 129 | Aar |
| 130 | Refer |
| 146 | Replaces |
| 162 | Redirection (3xx) |
| 177 | SIP-forward busy greeting |
| 178 | Call Forward Unregistered |
| 207 | Follow Me (SIP-forward all greeting) |
| 209 | Out of Service (SIP-forward busy greeting) |
| 239 | Time of Day (SIP-forward all greeting) |
| 242 | Do Not Disturb (SIP-forward no answer greeting) |
| 257 | Unavailable (SIP-forward busy greeting) |
| 274 | Away (SIP-forward no answer greeting) |
| 303 | Mobility HandIn |
| 319 | Mobility HandOut |
| 335 | Mobility Follow Me |
| 351 | Mobility Redial |
| 354 | Recording |
| 370 | Monitoring |
| 399 | Mobility IVR |
| 401 | Mobility DVOR |
| 402 | Mobility EFA |
| 403 | Mobility Session Handoff |
| 415 | Mobility Cell Pickup |
| 418 | Click to Conference |
| 434 | Forward No Retrieve |
| 450 | Forward No Retrieve Send Back to Parker |
| 464 | Call Control Discovery (indicates that the call is redirected to a PSTN failover number) |
| 480 | Intercompany Media Engine (IME) |
| 496 | IME Connection Timed Out |
| 512 | IME Not Enrolled |
| 528 | IME Socket Error |
| 544 | IME Domain Blacklisted |
| 560 | IME Prefix Blacklisted |
| 576 | IME Expired Ticket |
| 592 | IME Remote No Matching Route |
| 608 | IME Remote Unregistered |
| 624 | IME Remote IME Disabled |
| 640 | IME Remote Invalid IME Trunk URI |
| 656 | IME Remote URI not E164 |
| 672 | IME Remote Called Number Not Available |
| 688 | IME Invalid Ticket |
| 704 | IME Unknown |
| 720 | IME PSTN Fallback |
| 738 | Presence Enabled Routing |
| 752 | Agent Greeting |
| 783 | NuRD |
| 786 | Native Call Queuing, queue a call |
| 802 | Native Call Queuing, de-queue a call |
| 818 | Native Call Queuing, redirect to the second destination when no agent is logged in |
| 834 | Native Call Queuing, redirect to the second destination when the queue is full |
| 850 | Native Call Queuing, redirect to the second destination when the maximum wait time in queue is reached |

| Value | Description |
|---|---|
| 0 | Unknown |
| 1 | CctiLine |
| 2 | Unicast Shared Resource Provider |
| 3 | Call Park |
| 4 | Conference |
| 5 | Call Forward |
| 6 | Meet-Me Conference |
| 7 | Meet-Me Conference Intercepts |
| 8 | Message Waiting |
| 9 | Multicast Shared Resource Provider |
| 10 | Transfer |
| 11 | SSAPI Manager |
| 12 | Device |
| 13 | Call Control |
| 14 | Immediate Divert |
| 15 | Barge |
| 16 | Pickup |
| 17 | Refer |
| 18 | Replaces |
| 19 | Redirection |
| 20 | Callback |
| 21 | Path Replacement |
| 22 | FacCmc Manager |
| 23 | Malicious Call |
| 24 | Mobility |
| 25 | Aar |
| 26 | Directed Call Park |
| 27 | Recording |
| 28 | Monitoring |
| 29 | CCDRequestingService |
| 30 | Intercompany Media Engine |
| 31 | FallBack Manager |
| 32 | Presence Enabled Routing |
| 33 | AgentGreeting |
| 34 | NativeCallQueuing |
| 35 | MobileCallType |