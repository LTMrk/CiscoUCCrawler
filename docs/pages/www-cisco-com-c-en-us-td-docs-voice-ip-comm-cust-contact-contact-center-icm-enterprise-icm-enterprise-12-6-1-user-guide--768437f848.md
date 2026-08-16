---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--768437f848
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/ucce_b_ucce_b_outbound-option-guide-for-unified_1261/ucce_b_ucce_b_outbound-option-guide-for-unified_1261_appendix_01000.html
retrieved_at: 2026-08-16T20:39:54.570358+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(1)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(1)

Updated: August 22, 2023

Chapter: Long Distance Digit Prefix Logic

## Chapter: Long Distance Digit Prefix Logic

- Long Distance Digit Prefix Logic

- Transformation of Imported Numbers

- Dialer Configuration Fields and Registry Settings

# Long Distance Digit Prefix Logic

## Transformation of Imported Numbers

The following example displays an Outbound Option call route that provides information about how imported numbers are transformed
                              for the Outbound Option call.

Call Item

Outbound Option Configuration Field

Description

ImportedNumber <= TestNumberMaxDigits Registry
                                             						  setting

Final dialing number transferred to either the ACD or Unified CM (used for debugging/lab purposes only)

Area Code match beginning of ImportedNumber

Local area code

Area/city code used at your location, which is configured in
                                          						the Dialer Configuration Component

Include Area Code When Dialing

Local area code

Includes the area code for a long distance call or removes
                                          						the area code for a local call

PrePend "LongDistancePrefix"

Long distance prefix

Includes the pre-pended value for a long distance call,
                                          						which is configured in the Dialer Configuration Component

PrePend "Dial Prefix" Digits

Dial prefix

Include the dialing prefix required by your location or by
                                          						your campaign, which is configured in the Dialer Configuration Component

## Dialer Configuration Fields and Registry Settings

The following example displays the Dialer configuration fields and Registry settings from
                              the Dumpconf Procmon command that are used in an outbound call.

```
C:\>procmon ipccd dialer badialer >>>>dumpconf Dialer Config
     ------------- DialerID : [5006] PeripheralID : [5000] ActiveDialers : [1] LocalAreaCode : [978]
     <--- area code DialToneDetectEnabled : [0] HangupTime : [1] TenDigitDialEnabled : [0]
     <--- Include area code when dialing PrefixDigits : [] <--- Dial prefix digits
     LongDistancePrefix : [1] <---- "Long distance prefix" Callback config has not been received
     yet ----------------------------------------- Configured Skill Groups -----------------------
     --------- SkillGroupID : [11988] VDN : [11988] PeripheralNumber : [890] SkillGroupEnableStatus:
     [0] CampaignName : [DialAgents] ModeName : [N] TypeName : [I] Customer Count : [0] Customer
     Count (idle) : [0] RecordsToCache : [20] PredictiveExt : [890] PreviewExt : [890]
     *PortsPerAgent : [1.500000] AgentPercentage : [100] AgentsLoggedIn : [0] AgentsAvailable : [0]
     AgentsTalking : [0] *PortsAllocated : [0] AgentsReadyIn8Secs : [0] TalkTimeAverage : [60]
     *AgentsToReserveDelta : [0] *PortsUsedToDialDelta : [0] OverflowAgents : [0]
     AutoAnswerReservation : [0] AbandonRate : [2] MaximumLinesPerAgent : [2.000000]
     NoAnswerRingLimit : [4] MinimumCallDuration : [1] PreReservedRecordCount: [0] IVRPortCount :
     [0] TransferToIVREnabled : [N] TransferAnsMachine : [Y] IVRExt : [] --------- SkillGroupID :
     [-1] VDN : [-1] PeripheralNumber : [0] SkillGroupEnableStatus: [0] CampaignName : [Callback]
     ModeName : [A] TypeName : [O] Customer Count : [0] Customer Count (idle) : [0] RecordsToCache :
     [0] PredictiveExt : [] PreviewExt : [] *PortsPerAgent : [1.500000] AgentPercentage : [100]
     AgentsLoggedIn : [0] AgentsAvailable : [0] AgentsTalking : [0] *PortsAllocated : [0]
     AgentsReadyIn8Secs : [0] TalkTimeAverage : [0] *AgentsToReserveDelta : [0]
     *PortsUsedToDialDelta : [0] OverflowAgents : [0] AutoAnswerReservation : [1] AbandonRate : [1]
     MaximumLinesPerAgent : [3.000000] NoAnswerRingLimit : [3] MinimumCallDuration : [0]
     PreReservedRecordCount: [0] IVRPortCount : [0] TransferToIVREnabled : [N] TransferAnsMachine :
     [N] IVRExt : [] --------- SkillGroupID : [11965] VDN : [11965] PeripheralNumber : [889]
     SkillGroupEnableStatus: [0] CampaignName : [TT_ISN] ModeName : [R] TypeName : [O] Customer
     Count : [0] Customer Count (idle) : [0] RecordsToCache : [20] PredictiveExt : [12345]
     PreviewExt : [12345] *PortsPerAgent : [1.500000] AgentPercentage : [100] AgentsLoggedIn : [60]
     AgentsAvailable : [60] AgentsTalking : [0] *PortsAllocated : [0] AgentsReadyIn8Secs : [0]
     TalkTimeAverage : [60] *AgentsToReserveDelta : [0] *PortsUsedToDialDelta : [0] OverflowAgents :
     [0] AutoAnswerReservation : [0] AbandonRate : [3] MaximumLinesPerAgent : [2.500000]
     NoAnswerRingLimit : [4] MinimumCallDuration : [1] PreReservedRecordCount: [0] IVRPortCount :
     [60] TransferToIVREnabled : [Y] TransferAnsMachine : [Y] IVRExt : [90001] Port Map Config
     --------------- Port: [000], Station: [30100] Port: [015], Station: [30115] Port: [081],
     Station: [30181] Port: [082], Station: [30182] Port: [083], Station: [30183] Port: [016],
     Station: [30116] Port: [031], Station: [30131] Port: [087], Station: [30187] Port: [023],
     Station: [30123] Port: [071], Station: [30171] Port: [095], Station: [30195] Port: [063],
     Station: [30163] Port: [055], Station: [30155] Port: [047], Station: [30147] Port: [039],
     Station: [30139] Port: [008], Station: [30108] Port: [032], Station: [30132] Port: [024],
     Station: [30124] Port: [088], Station: [30188] Port: [072], Station: [30172] Port: [064],
     Station: [30164] Port: [048], Station: [30148] Port: [040], Station: [30140] Port: [001],
     Station: [30101] Port: [009], Station: [30109] Port: [033], Station: [30133] Port: [017],
     Station: [30117] Port: [025], Station: [30125] Port: [089], Station: [30189] Port: [065],
     Station: [30165] Port: [073], Station: [30173] Port: [049], Station: [30149] Port: [041],
     Station: [30141] Port: [002], Station: [30102] Port: [018], Station: [30118] Port: [026],
     Station: [30126] Port: [090], Station: [30190] Port: [066], Station: [30166] Port: [074],
     Station: [30174] Port: [050], Station: [30150] Port: [042], Station: [30142] Port: [003],
     Station: [30103] Port: [027], Station: [30127] Port: [019], Station: [30119] Port: [091],
     Station: [30191] Port: [075], Station: [30175] Port: [067], Station: [30167] Port: [059],
     Station: [30159] Port: [051], Station: [30151] Port: [043], Station: [30143] Port: [004],
     Station: [30104] Port: [020], Station: [30120] Port: [028], Station: [30128] Port: [092],
     Station: [30192] Port: [084], Station: [30184] Port: [076], Station: [30176] Port: [060],
     Station: [30160] Port: [068], Station: [30168] Port: [052], Station: [30152] Port: [036],
     Station: [30136] Port: [021], Station: [30121] Port: [044], Station: [30144] Port: [093],
     Station: [30193] Port: [005], Station: [30105] Port: [029], Station: [30129] Port: [085],
     Station: [30185] Port: [069], Station: [30169] Port: [077], Station: [30177] Port: [061],
     Station: [30161] Port: [053], Station: [30153] Port: [037], Station: [30137] Port: [045],
     Station: [30145] Port: [014], Station: [30114] Port: [038], Station: [30138] Port: [079],
     Station: [30179] Port: [010], Station: [30110] Port: [056], Station: [30156] Port: [034],
     Station: [30134] Port: [080], Station: [30180] Port: [057], Station: [30157] Port: [058],
     Station: [30158] Port: [022], Station: [30122] Port: [006], Station: [30106] Port: [030],
     Station: [30130] Port: [011], Station: [30111] Port: [035], Station: [30135] Port: [012],
     Station: [30112] Port: [013], Station: [30113] Port: [086], Station: [30186] Port: [070],
     Station: [30170] Port: [094], Station: [30194] Port: [078], Station: [30178] Port: [062],
     Station: [30162] Port: [046], Station: [30146] Port: [054], Station: [30154] Port: [007],
     Station: [30107] Registry Config Values ---------------------- TimeToCTIBeginCall : [7]
     TimeToRingCustomer : [8] TimeToHoldCustomer : [1] TimeToReserve : [10] TimeToTransfer : [7]
     TimeToFreeStuckPort : [7200] TimeToFreeStuckCall : [7200] SwitchPrefix : []
     TimeToRetryCustomerRequest : [30] TimeToWaitForRecord : [5] TimeToWaitForCTIResp : [3]
     TalkTimeAvg : [60] CustRecReadyRequestToServer: [30] TestNumberMaxDigits : [5] <----- "Test
     Number Max digits" ca_cnosig : [20] PortThrottleTime : [2] PortThrottleCount : [20]
     OptimizeAgentAvailability : [0] RTPortFeedDisable : [1] SkillGroupQueryDelay : [1]
     ReclassifyTransferFailures : [0] SetAgentsReadyOnResvDrop : [1] DirectAgentDial : [0]
     OverrideNetworkTones : [0] AnswrTrnsfrUsingAgentPhone : [1] </end>>>>>
```

| Call Item | Outbound Option Configuration Field | Description |
|---|---|---|
| ImportedNumber <= TestNumberMaxDigits Registry
                                             						  setting |  | Final dialing number transferred to either the ACD or Unified CM (used for debugging/lab purposes only) |
| Area Code match beginning of ImportedNumber | Local area code | Area/city code used at your location, which is configured in
                                          						the Dialer Configuration Component |
| Include Area Code When Dialing | Local area code | Includes the area code for a long distance call or removes
                                          						the area code for a local call |
| PrePend "LongDistancePrefix" | Long distance prefix | Includes the pre-pended value for a long distance call,
                                          						which is configured in the Dialer Configuration Component |
| PrePend "Dial Prefix" Digits | Dial prefix | Include the dialing prefix required by your location or by
                                          						your campaign, which is configured in the Dialer Configuration Component |