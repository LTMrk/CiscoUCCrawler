---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-cdrdef-cucm-b-cdr-admin-guide-1251-cucm-b-cdr-admin-guid-b268b6ee10
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/cdrdef/cucm_b_cdr-admin-guide-1251/cucm_b_cdr-admin-guide-1251_chapter_011.html
retrieved_at: 2026-08-21T01:38:10.271730+00:00
---

Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: Call Information Record Types

## Chapter: Call Information Record Types

# Call Information Record Types

This chapter describes the two types of call information records that Cisco Unified Communications Manager generates: Call Detail Records (CDRs) and Call Management Records (CMRs), also called call diagnostic records.

## Call Information Record Types

Unified Communications Manager generates two different types of call information records: Call Detail Records (CDRs) and Call Management Records (CMRs),
                              also called call diagnostic records. CDRs store information about the endpoints of the call and other call control/routing
                              aspects. CMRs contain diagnostic information about the quality of the streamed audio of the call. More than one CMR can exist
                              per CDR.

CMRs are supported by Cisco Unified IP Phone s, Cisco 7960 series phones, and Media Gateway Control Protocol (MGCP) gateways. If one of these endpoints is involved in
                              a call, it will generate a CMR record after the call terminates. Each endpoint in the call generates a separate CMR record.
                              If the call involves endpoints that do not support call diagnostics, no record gets generated for that endpoint. A call from
                              a Cisco7960 phone to an H.323 gateway generates one CMR record (from the Cisco 7960 phone).

CDRs relate to the CMRs via two globalCallID columns:

globalCallID_callManagerId

globalCallId_callId

When the Call Diagnostics service parameter is set to True, the system generates up to two CMRs for each call. Each type of
                              call, such as conference calls, call transfers, forwarded calls, and calls through gateways, produce a set of records that
                              gets written to ASCII files at the end of the call. Only completed calls and failed calls generate CDRs and CMRs. Unified Communications Manager does not perform any post processing on CDRs or CMRs.

## Global Call Identifier

The Unified Communications Manager allocates a global call identifier (GlobalCallID_callId) each time that a Cisco Unified IP Phone is taken off hook or a call is received from a gateway. The GlobalCallID_callId is allocated sequentially on a Unified Communications Manager server, independent of calls running on other call servers in the cluster. Unified Communications Manager writes the GlobalCallID_callId value to a disk file for every 1,000th call. When Unified Communications Manager restarts for any reason, it assigns the next 1000th number to the next GlobalCallID_callId.

For example, when a successful call gets made, the GlobalCallID_callId value in the CDR specifies 1001. For the next call,
                              the GlobalCallID_callId value specifies 1002, and so on. When Unified Communications Manager restarts, the value for the next call in the CDR gets assigned 2001. The numbers continue sequentially from there until Unified Communications Manager restarts again. For the next restart, the GlobalCallID_callId value specifies 3001.

The maximum value that gets assigned to the GlobalCallID_callId is limited to 24 bits. When this limitation occurs, the GlobalCallID_callId
                                          value gets reset to 1.

The GlobalCallID_callIds in the CDR file may not be in sequential order in the CDR flat file. If a call with GlobalCallID_callId
                              = 1 lasts longer than the call with GlobalCallID_callId = 2, then the CDR records for GlobalCallId_callId= 2 are written before
                              GlobalCallId_callId = 1. GlobalCallID_callIds may be completely missing from the CDR flat file. If the first CDR record has
                              GlobalCallID_callId = 1, and the second CDR has GlobalCallID_callId = 3, that does not mean that the CDR for GlobalCallID_callId
                              = 2 is missing. GlobalCallID_callId = 2 did not meet the criteria to generate a CDR. The failure to generate a CDR can occur
                              because while the first and third call were successful, the second call was never completed; or, GlobalCallID_callId = 2 could
                              be part of a conference call. Each call leg in a conference call is assigned a GlobalCallID_callId that is overwritten in
                              the conference GlobalCallID_callId. The original GlobalCallID_callId may not appear in the CDR flat file.

If the GlobalCallID_callId field is missing from the CDR record, CAR generates an error for that particular record. Additional
                              information on CDR errors is available in the "Configuring CDR Error Reports" chapter of the CDR Analysis and Reporting Administration Guide .

For Unified Communications Manager Release 5.x and later releases, the value in the GlobalCallId CDR field survives over Unified Communications Manager restarts. In Release 4.x and earlier releases, even though the GlobalCallId field is time-based, the field gets reused under
                                          conditions of heavy traffic. Because of this behavior, problems can occur with customer billing applications and the ability
                                          of CAR to correlate CMRs with CDRs and to correlate conference call CDRs. For Release 5.x and later releases, GlobalCallId
                                          redesign ensures the field retains a unique value, at least for a certain number of days. Now, the last used globalCallId_callId
                                          value gets written to disk periodically (for every x number of calls). The value gets retrieved after a Unified Communications Manager restart, and the new globalCallId_callId value begins with this number plus x.

## Number Translations

The Unified Communications Manager can perform translations on the digits that a user dials. The translated number, not the actual dialed digits, appears in
                              the CDR.

For example, many companies translate "911" calls to "9-911," so the caller does not need to dial an outside line in an emergency. In these cases, the CDR contains "9911" although the user dials "911."

Gateways can perform further modifications to the number before the digits are actually output through the gateway. The CDR
                                          does not reflect these modifications.

## Partitions and Numbers

Within a CDR, a combination of extension number and partitions identifies each phone that is referenced, if partitions are
                              defined. When partitions exist, fully identifying a phone requires both values because extension numbers may not be unique.

The Partition field stays empty when a call ingresses through a gateway. When a call egresses through a gateway, the Partition
                              field shows the partition to which the gateway belongs.

If the dial plan allows callers to use the # key for speed dialing, the # key goes into the database when it is used. For
                              example, the Called Party Number field may contain a value such as "902087569174#."

The Party Number fields may include SIP URIs instead of the traditional calling/called party number.

CDRs use the Partition/Extension Numbers that are shown in the following table:

Phone Number

Description

callingPartyNumber

This party placed the call. For transferred calls, the transferred party becomes the calling party.

originalCalledPartyNumber

This number designates the originally called party, after any digit translations have occurred.

finalCalledPartyNumber

For forwarded calls, this number designates the last party to receive the call.

For non-forwarded calls, this field shows the original called party.

lastRedirectDn

For forwarded calls, this field designates the last party to redirect the call.

For non-forwarded calls, this field shows the last party to redirect (such as transfer and conference) the call.

callingPartyNumberPartition

This number identifies the partition name that is associated with the CallingPartyNumber field. This field uniquely identifies
                                          this number because the Unified Communications Manager supports multiple Cisco Unified IP Phone s with the same extension number in different partitions.

For calls that ingress through a gateway, this field remains blank.

originalCalledPartyNumberPartition

This number identifies the partition name that is associated with the OriginalCalledPartyNumber field. This field uniquely
                                          identifies this number because the Unified Communications Manager supports multiple Cisco Unified IP Phone s with the same extension number in different partitions.

For calls that egress through a gateway, this field specifies the partition name that is associated with the route pattern
                                          that pointed to the gateway.

finalCalledPartyNumberPartition

This number identifies the partition name that is associated with the FinalCalledPartyNumber field. This field uniquely identifies
                                          this number because the Unified Communications Manager supports multiple Cisco Unified IP Phone s with the same extension number in different partitions.

For calls that egress through a gateway, this field specifies the partition name that is associated with the route pattern
                                          that pointed to the gateway.

lastRedirectDnPartition

This number identifies the partition name that is associated with the LastRedirectDn field. This field uniquely identifies
                                          this number because the Unified Communications Manager supports multiple Cisco Unified IP Phone s with the same extension number in different partitions.

For calls that egress through a gateway, this field specifies the partition name that is associated with the route pattern
                                          that pointed to the gateway.

outpulsedCallingPartyNumber

The calling party number outpulsed from the device.

outpulsedCalledPartyNumber

The called party number outpulsed from the device.

## Timestamps

Timestamps within a CDR appear in Universal Coordinated Time (UTC). This value remains independent of daylight saving time
                              changes.

Unsigned 32-bit integers represent all time values. This unsigned integer value displays from the database as a single integer.
                              The field specifies a time_t value that is obtained from the operating system.

The following table displays the UTC timestamps that get included in the CDR.

Field

Format

Description

dateTimeOrigination

UTC

For outgoing calls, this field designates the time that the device goes off hook.

For incoming calls, this field designates the time that the SETUP message is received.

This field always gets populated.

dateTimeConnect

UTC

This field designates the time that the devices connect.

Thisfield shows a zero if the call never connects.

dateTimeDisconnect

UTC

This field designates the time that the call disconnects. This field gets set even if the call never connects. The time gets
                                          stored as UTC.

This field always gets populated.

## Call Clearing Causes

The CDR includes two call clearing cause codes: OrigCause and DestCause. When the originating party releases the call, the
                              OrigCause gets populated. When the terminating party releases the call, or the call is rejected, the DestCause gets populated.
                              When unpopulated, the cause code value shows zero.

Table 1 lists the call clearing cause code values per ITU specification Q.850. For On Net call legs, the Unified Communications Manager determines the cause code value. For Off Net call legs, the far-end switch determines the cause code value.

## Convert Signed Decimal Value to IP Address

The system stores IP addresses as unsigned integers. The CDR file displays IP addresses as signed integers. Toconvert the
                              signed decimal value to an IP address, first convert the value to a hex number, taking into consideration that it is really
                              an unsigned number. The 32-bit hex value represents four bytes in reverse order (Intel standard). To determine the IP address,
                              reverse the order of the bytes and convert each byte to a decimal number. The resulting four bytes represent the four-byte
                              fields of the IP address in dotted decimal notation.

The file displays a negative number when the low byte of the IP address has the most significant bit set.

For example, the IP address 192.168.18.188 displays as -1139627840. To convert this IP address, perform the following procedure:

Convert the database display (-1139627840) to a hex value.

The hex value equals 0xBC12A8C0.

Reverse the order of the hex bytes, as shown below:

CO A8 12 BC

Convert the four bytes from hex to decimal, as shown below:

192 168 18 188

The IP address displays in the dotted decimal format:

192.168.18.188

### What to do next

When working with CDRs, you may want to read other tables in the CAR database to obtain information about the type of device
                              in each CDR because the correlation between devices in the device table and the IP address that is listed in the CDR is not
                              straightforward.

| Note | The maximum value that gets assigned to the GlobalCallID_callId is limited to 24 bits. When this limitation occurs, the GlobalCallID_callId
                                          value gets reset to 1. |
|---|---|

| Note | For Unified Communications Manager Release 5.x and later releases, the value in the GlobalCallId CDR field survives over Unified Communications Manager restarts. In Release 4.x and earlier releases, even though the GlobalCallId field is time-based, the field gets reused under
                                          conditions of heavy traffic. Because of this behavior, problems can occur with customer billing applications and the ability
                                          of CAR to correlate CMRs with CDRs and to correlate conference call CDRs. For Release 5.x and later releases, GlobalCallId
                                          redesign ensures the field retains a unique value, at least for a certain number of days. Now, the last used globalCallId_callId
                                          value gets written to disk periodically (for every x number of calls). The value gets retrieved after a Unified Communications Manager restart, and the new globalCallId_callId value begins with this number plus x. |
|---|---|

| Note | Gateways can perform further modifications to the number before the digits are actually output through the gateway. The CDR
                                          does not reflect these modifications. |
|---|---|

| Phone Number | Description |
|---|---|
| callingPartyNumber | This party placed the call. For transferred calls, the transferred party becomes the calling party. |
| originalCalledPartyNumber | This number designates the originally called party, after any digit translations have occurred. |
| finalCalledPartyNumber | For forwarded calls, this number designates the last party to receive the call. For non-forwarded calls, this field shows the original called party. |
| lastRedirectDn | For forwarded calls, this field designates the last party to redirect the call. For non-forwarded calls, this field shows the last party to redirect (such as transfer and conference) the call. |
| callingPartyNumberPartition | This number identifies the partition name that is associated with the CallingPartyNumber field. This field uniquely identifies
                                          this number because the Unified Communications Manager supports multiple Cisco Unified IP Phone s with the same extension number in different partitions. For calls that ingress through a gateway, this field remains blank. |
| originalCalledPartyNumberPartition | This number identifies the partition name that is associated with the OriginalCalledPartyNumber field. This field uniquely
                                          identifies this number because the Unified Communications Manager supports multiple Cisco Unified IP Phone s with the same extension number in different partitions. For calls that egress through a gateway, this field specifies the partition name that is associated with the route pattern
                                          that pointed to the gateway. |
| finalCalledPartyNumberPartition | This number identifies the partition name that is associated with the FinalCalledPartyNumber field. This field uniquely identifies
                                          this number because the Unified Communications Manager supports multiple Cisco Unified IP Phone s with the same extension number in different partitions. For calls that egress through a gateway, this field specifies the partition name that is associated with the route pattern
                                          that pointed to the gateway. |
| lastRedirectDnPartition | This number identifies the partition name that is associated with the LastRedirectDn field. This field uniquely identifies
                                          this number because the Unified Communications Manager supports multiple Cisco Unified IP Phone s with the same extension number in different partitions. For calls that egress through a gateway, this field specifies the partition name that is associated with the route pattern
                                          that pointed to the gateway. |
| outpulsedCallingPartyNumber | The calling party number outpulsed from the device. |
| outpulsedCalledPartyNumber | The called party number outpulsed from the device. |

| Field | Format | Description |
|---|---|---|
| dateTimeOrigination | UTC | For outgoing calls, this field designates the time that the device goes off hook. For incoming calls, this field designates the time that the SETUP message is received. This field always gets populated. |
| dateTimeConnect | UTC | This field designates the time that the devices connect. Thisfield shows a zero if the call never connects. |
| dateTimeDisconnect | UTC | This field designates the time that the call disconnects. This field gets set even if the call never connects. The time gets
                                          stored as UTC. This field always gets populated. |

| Note | The file displays a negative number when the low byte of the IP address has the most significant bit set. |
|---|---|

| Step 1 | Convert the database display (-1139627840) to a hex value. The hex value equals 0xBC12A8C0. |
|---|---|
| Step 2 | Reverse the order of the hex bytes, as shown below: CO A8 12 BC |
| Step 3 | Convert the four bytes from hex to decimal, as shown below: 192 168 18 188 |
| Step 4 | The IP address displays in the dotted decimal format: 192.168.18.188 |