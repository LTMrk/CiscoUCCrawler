---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-tapi-dev-15-cucm-b-tapi-dev-guide-15-cucm-b-tapi-dev-guide-1251-appendi-e25ed70f17
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/tapi_dev/15/cucm_b_tapi-dev-guide-15/cucm_b_tapi-dev-guide-1251_appendix_01001.html
retrieved_at: 2026-08-16T18:05:53.246118+00:00
---

Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: August 11, 2026

Chapter: Cisco Unified TAPI Interfaces

## Chapter: Cisco Unified TAPI Interfaces

- Cisco Unified TAPI Interfaces

- Cisco Unified TAPI Version 2.1 Interfaces

# Cisco Unified TAPI Interfaces

This appendix contains a listing of APIs that are supported and not supported.

## Cisco Unified TAPI Version 2.1 Interfaces

### Core Package

The following table lists each TAPI interface

API/Message/Structure

Cisco TAPI support

Comments

TAPI Line Functions

lineAccept

Yes

lineAddProvider

Yes

lineAddToConference

Yes

lineAnswer

Yes

lineBlindTransfer

Yes

lineCallbackFunc

Yes

lineClose

Yes

lineCompleteCall

No

lineCompleteTransfer

Yes

lineConfigDialog

No

lineConfigDialogEdit

No

lineConfigProvider

Yes

lineDeallocateCall

Yes

lineDevSpecific

Yes

lineDevSpecificFeature

Yes

lineDial

Yes

lineDrop

Yes

lineForward

Yes

lineGatherDigits

No

lineGenerateDigits

Yes

lineGenerateTone

Yes

lineGetAddressCaps

Yes

lineGetAddressID

Yes

lineGetAddressStatus

Yes

lineGetAppPriority

No

lineGetCallInfo

Yes

lineGetCallStatus

Yes

lineGetConfRelatedCalls

Yes

lineGetCountry

No

lineGetDevCaps

Yes

lineGetDevConfig

No

lineGetIcon

No

lineGetID

Yes

lineGetLineDevStatus

Yes

lineGetMessage

Yes

lineGetNewCalls

Yes

lineGetNumRings

Yes

lineGetProviderList

Yes

lineGetRequest

Yes

lineGetStatusMessages

Yes

lineGetTranslateCaps

Yes

lineHandoff

Yes

lineHold

Yes

lineInitialize

Yes

lineInitializeEx

Yes

lineMakeCall

Yes

lineMonitorDigits

Yes

lineMonitorMedia

No

lineMonitorTones

Yes

lineNegotiateAPIVersion

Yes

lineNegotiateExtVersion

Yes

lineOpen

Yes

linePark

Yes

linePickup

No

linePrepareAddToConference

Yes

lineRedirect

Yes

lineRegisterRequestRecipient

Yes

lineReleaseUserUserInfo

No

lineRemoveFromConference

No

lineRemoveProvider

Yes

lineSecureCall

No

lineSendUserUserInfo

No

lineSetAppPriority

Yes

lineSetAppSpecific

No

lineSetCallData

No

lineSetCallParams

No

lineSetCallPrivilege

Yes

lineSetCallQualityOfService

No

lineSetCallTreatment

No

lineSetCurrentLocation

No

lineSetDevConfig

No

lineSetLineDevStatus

No

lineSetMediaControl

No

lineSetMediaMode

No

lineSetNumRings

Yes

lineSetStatusMessages

Yes

lineSetTerminal

No

lineSetTollList

Yes

lineSetupConference

Yes

lineSetupTransfer

Yes

lineShutdown

Yes

lineSwapHold

No

lineTranslateAddress

Yes

lineTranslateDialog

Yes

lineUncompleteCall

No

lineUnhold

Yes

lineUnpark

Yes

TAPI Line Messages

LINE_ADDRESSSTATE

Yes

LINE_APPNEWCALL

Yes

LINE_CALLINFO

Yes

LINE_CALLSTATE

Yes

LINE_CLOSE

Yes

LINE_CREATE

Yes

LINE_DEVSPECIFIC

Yes

LINE_DEVSPECIFICFEATURE

Yes

LINE_GATHERDIGITS

Yes

LINE_GENERATE

Yes

LINE_LINEDEVSTATE

Yes

LINE_MONITORDIGITS

Yes

LINE_MONITORMEDIA

No

LINE_MONITORTONE

Yes

LINE_REMOVE

Yes

LINE_REPLY

Yes

LINE_REQUEST

Yes

TAPI Line Structures

LINEADDRESSCAPS

Yes

LINEADDRESSSTATUS

Yes

LINEAPPINFO

Yes

LINECALLINFO

Yes

LINECALLLIST

Yes

LINECALLPARAMS

Yes

LINECALLSTATUS

Yes

LINECALLTREATMENTENTRY

No

LINECARDENTRY

Yes

LINECOUNTRYENTRY

Yes

LINECOUNTRYLIST

Yes

LINEDEVCAPS

Yes

LINEDEVSTATUS

Yes

LINEDIALPARAMS

No

LINEEXTENSIONID

Yes

LINEFORWARD

Yes

LINEFORWARDLIST

Yes

LINEGENERATETONE

Yes

LINEINITIALIZEEXPARAMS

Yes

LINELOCATIONENTRY

Yes

LINEMEDIACONTROLCALLSTATE

No

LINEMEDIACONTROLDIGIT

No

LINEMEDIACONTROLMEDIA

No

LINEMEDIACONTROLTONE

No

LINEMESSAGE

Yes

LINEMONITORTONE

Yes

LINEPROVIDERENTRY

Yes

LINEPROVIDERLIST

Yes

LINEREQMEDIACALL

No

LINEREQMAKECALL

Yes

LINETERMCAPS

No

LINETRANSLATECAPS

Yes

LINETRANSLATEOUTPUT

Yes

TAPI Phone Functions

phoneCallbackFunc

Yes

phoneClose

Yes

phoneConfigDialog

No

phoneDevSpecific

Yes

phoneGetButtonInfo

No

phoneGetData

No

phoneGetDevCaps

Yes

phoneGetDisplay

Yes

phoneGetGain

No

phoneGetHookSwitch

No

phoneGetIcon

No

phoneGetID

No

phoneGetLamp

No

phoneGetMessage

Yes

phoneGetRing

Yes

phoneGetStatus

No

phoneGetStatusMessages

Yes

phoneGetVolume

No

phoneInitialize

Yes

phoneInitializeEx

Yes

phoneNegotiateAPIVersion

Yes

phoneNegotiateExtVersion

No

phoneOpen

Yes

phoneSetButtonInfo

No

phoneSetData

No

phoneSetDisplay

Yes

phoneSetGain

No

phoneSetHookSwitch

No

phoneSetLamp

No

phoneSetRing

No

phoneSetStatusMessages

Yes

phoneSetVolume

No

phoneShutdown

Yes

TAPI Phone Messages

PHONE_BUTTON

Yes

PHONE_CLOSE

Yes

PHONE_CREATE

Yes

PHONE_DEVSPECIFIC

No

PHONE_REMOVE

Yes

PHONE_REPLY

Yes

PHONE_STATE

Yes

TAPI Phone Structures

PHONEBUTTONINFO

No

PHONECAPS

Yes

PHONEEXTENSIONID

No

PHONEINITIALIZEEXPARAMS

Yes

PHONEMESSAGE

Yes

PHONESTATUS

No

VARSTRING

Yes

TAPI Assisted Telephony Functions

tapiRequestDrop

No

tapiRequestMediaCall

No

TAPI Call Center Functions

lineAgentSpecific

No

lineGetAgentActivityList

No

lineGetAgentCaps

No

lineGetAgentGroupList

No

lineGetAgentStatus

No

lineProxyMessage

No

lineProxyResponse

No

lineSetAgentActivity

No

lineSetAgentGroup

No

lineSetAgentState

No

TAPI Call Center Messages

LINE_AGENTSPECIFIC

No

LINE_AGENTSTATUS

No

LINE_PROXYREQUEST

No

TAPI Call Center Structures

LINEAGENTACTIVITYENTRY

No

LINEAGENTACTIVITYLIST

No

LINEAGENTCAPS

No

LINEAGENTGROUPENTRY

No

LINEAGENTGROUPLIST

No

LINEAGENTSTATUS

No

LINEPROXYREQUEST

No

Wave Functions

waveInAddBuffer

Yes

waveInClose

Yes

waveInGetDevCaps

No

waveInGetErrorText

No

waveInGetID

Yes

waveInGetNumDevs

No

waveInGetPosition

Yes

waveInMessage

No

waveInOpen

Yes

waveInPrepareHeader

Yes

waveInProc

No

waveInReset

Yes

waveInStart

Yes

waveInStop

No

waveInUnprepareHeader

Yes

waveOutBreakLoop

No

waveOutClose

Yes

waveOutGetDevCaps

Yes

waveOutGetErrorText

No

waveOutGetID

Yes

waveOutGetNumDevs

No

waveOutGetPitch

No

waveOutGetPlaybackRate

No

waveOutGetPosition

No

waveOutGetVolume

No

waveOutMessage

No

waveOutOpen

Yes

waveOutPause

No

waveOutPrepareHeader

Yes

waveOutProc

No

waveOutReset

Yes

waveOutRestart

No

waveOutSetPitch

No

waveOutSetPlaybackRate

No

waveOutSetVolume

No

waveOutUnprepareHeader

Yes

waveOutWrite

Yes

| API/Message/Structure | Cisco TAPI support | Comments |
|---|---|---|
| TAPI Line Functions |
| lineAccept | Yes |  |
| lineAddProvider | Yes |  |
| lineAddToConference | Yes |  |
| lineAnswer | Yes |  |
| lineBlindTransfer | Yes |  |
| lineCallbackFunc | Yes |  |
| lineClose | Yes |  |
| lineCompleteCall | No |  |
| lineCompleteTransfer | Yes |  |
| lineConfigDialog | No |  |
| lineConfigDialogEdit | No |  |
| lineConfigProvider | Yes |  |
| lineDeallocateCall | Yes |  |
| lineDevSpecific | Yes |  |
| lineDevSpecificFeature | Yes |  |
| lineDial | Yes |  |
| lineDrop | Yes |  |
| lineForward | Yes |  |
| lineGatherDigits | No |  |
| lineGenerateDigits | Yes |  |
| lineGenerateTone | Yes |  |
| lineGetAddressCaps | Yes |  |
| lineGetAddressID | Yes |  |
| lineGetAddressStatus | Yes |  |
| lineGetAppPriority | No |  |
| lineGetCallInfo | Yes |  |
| lineGetCallStatus | Yes |  |
| lineGetConfRelatedCalls | Yes |  |
| lineGetCountry | No |  |
| lineGetDevCaps | Yes |  |
| lineGetDevConfig | No |  |
| lineGetIcon | No |  |
| lineGetID | Yes |  |
| lineGetLineDevStatus | Yes |  |
| lineGetMessage | Yes |  |
| lineGetNewCalls | Yes |  |
| lineGetNumRings | Yes |  |
| lineGetProviderList | Yes |  |
| lineGetRequest | Yes |  |
| lineGetStatusMessages | Yes |  |
| lineGetTranslateCaps | Yes |  |
| lineHandoff | Yes |  |
| lineHold | Yes |  |
| lineInitialize | Yes |  |
| lineInitializeEx | Yes |  |
| lineMakeCall | Yes |  |
| lineMonitorDigits | Yes |  |
| lineMonitorMedia | No |  |
| lineMonitorTones | Yes |  |
| lineNegotiateAPIVersion | Yes |  |
| lineNegotiateExtVersion | Yes |  |
| lineOpen | Yes |  |
| linePark | Yes |  |
| linePickup | No |  |
| linePrepareAddToConference | Yes |  |
| lineRedirect | Yes |  |
| lineRegisterRequestRecipient | Yes |  |
| lineReleaseUserUserInfo | No |  |
| lineRemoveFromConference | No |  |
| lineRemoveProvider | Yes |  |
| lineSecureCall | No |  |
| lineSendUserUserInfo | No |  |
| lineSetAppPriority | Yes |  |
| lineSetAppSpecific | No |  |
| lineSetCallData | No |  |
| lineSetCallParams | No |  |
| lineSetCallPrivilege | Yes |  |
| lineSetCallQualityOfService | No |  |
| lineSetCallTreatment | No |  |
| lineSetCurrentLocation | No |  |
| lineSetDevConfig | No |  |
| lineSetLineDevStatus | No |  |
| lineSetMediaControl | No |  |
| lineSetMediaMode | No |  |
| lineSetNumRings | Yes |  |
| lineSetStatusMessages | Yes |  |
| lineSetTerminal | No |  |
| lineSetTollList | Yes |  |
| lineSetupConference | Yes |  |
| lineSetupTransfer | Yes |  |
| lineShutdown | Yes |  |
| lineSwapHold | No |  |
| lineTranslateAddress | Yes |  |
| lineTranslateDialog | Yes |  |
| lineUncompleteCall | No |  |
| lineUnhold | Yes |  |
| lineUnpark | Yes |  |
| TAPI Line Messages |
| LINE_ADDRESSSTATE | Yes |  |
| LINE_APPNEWCALL | Yes |  |
| LINE_CALLINFO | Yes |  |
| LINE_CALLSTATE | Yes |  |
| LINE_CLOSE | Yes |  |
| LINE_CREATE | Yes |  |
| LINE_DEVSPECIFIC | Yes |  |
| LINE_DEVSPECIFICFEATURE | Yes |  |
| LINE_GATHERDIGITS | Yes |  |
| LINE_GENERATE | Yes |  |
| LINE_LINEDEVSTATE | Yes |  |
| LINE_MONITORDIGITS | Yes |  |
| LINE_MONITORMEDIA | No |  |
| LINE_MONITORTONE | Yes |  |
| LINE_REMOVE | Yes |  |
| LINE_REPLY | Yes |  |
| LINE_REQUEST | Yes |  |
| TAPI Line Structures |
| LINEADDRESSCAPS | Yes |  |
| LINEADDRESSSTATUS | Yes |  |
| LINEAPPINFO | Yes |  |
| LINECALLINFO | Yes |  |
| LINECALLLIST | Yes |  |
| LINECALLPARAMS | Yes |  |
| LINECALLSTATUS | Yes |  |
| LINECALLTREATMENTENTRY | No |  |
| LINECARDENTRY | Yes |  |
| LINECOUNTRYENTRY | Yes |  |
| LINECOUNTRYLIST | Yes |  |
| LINEDEVCAPS | Yes |  |
| LINEDEVSTATUS | Yes |  |
| LINEDIALPARAMS | No |  |
| LINEEXTENSIONID | Yes |  |
| LINEFORWARD | Yes |  |
| LINEFORWARDLIST | Yes |  |
| LINEGENERATETONE | Yes |  |
| LINEINITIALIZEEXPARAMS | Yes |  |
| LINELOCATIONENTRY | Yes |  |
| LINEMEDIACONTROLCALLSTATE | No |  |
| LINEMEDIACONTROLDIGIT | No |  |
| LINEMEDIACONTROLMEDIA | No |  |
| LINEMEDIACONTROLTONE | No |  |
| LINEMESSAGE | Yes |  |
| LINEMONITORTONE | Yes |  |
| LINEPROVIDERENTRY | Yes |  |
| LINEPROVIDERLIST | Yes |  |
| LINEREQMEDIACALL | No |  |
| LINEREQMAKECALL | Yes |  |
| LINETERMCAPS | No |  |
| LINETRANSLATECAPS | Yes |  |
| LINETRANSLATEOUTPUT | Yes |  |
| TAPI Phone Functions |
| phoneCallbackFunc | Yes |  |
| phoneClose | Yes |  |
| phoneConfigDialog | No |  |
| phoneDevSpecific | Yes |  |
| phoneGetButtonInfo | No |  |
| phoneGetData | No |  |
| phoneGetDevCaps | Yes |  |
| phoneGetDisplay | Yes |  |
| phoneGetGain | No |  |
| phoneGetHookSwitch | No |  |
| phoneGetIcon | No |  |
| phoneGetID | No |  |
| phoneGetLamp | No |  |
| phoneGetMessage | Yes |  |
| phoneGetRing | Yes |  |
| phoneGetStatus | No |  |
| phoneGetStatusMessages | Yes |  |
| phoneGetVolume | No |  |
| phoneInitialize | Yes |  |
| phoneInitializeEx | Yes |  |
| phoneNegotiateAPIVersion | Yes |  |
| phoneNegotiateExtVersion | No |  |
| phoneOpen | Yes |  |
| phoneSetButtonInfo | No |  |
| phoneSetData | No |  |
| phoneSetDisplay | Yes |  |
| phoneSetGain | No |  |
| phoneSetHookSwitch | No |  |
| phoneSetLamp | No |  |
| phoneSetRing | No |  |
| phoneSetStatusMessages | Yes |  |
| phoneSetVolume | No |  |
| phoneShutdown | Yes |  |
| TAPI Phone Messages |
| PHONE_BUTTON | Yes |  |
| PHONE_CLOSE | Yes |  |
| PHONE_CREATE | Yes |  |
| PHONE_DEVSPECIFIC | No |  |
| PHONE_REMOVE | Yes |  |
| PHONE_REPLY | Yes |  |
| PHONE_STATE | Yes |  |
| TAPI Phone Structures |
| PHONEBUTTONINFO | No |  |
| PHONECAPS | Yes |  |
| PHONEEXTENSIONID | No |  |
| PHONEINITIALIZEEXPARAMS | Yes |  |
| PHONEMESSAGE | Yes |  |
| PHONESTATUS | No |  |
| VARSTRING | Yes |  |
| TAPI Assisted Telephony Functions |
| tapiRequestDrop | No |  |
| tapiRequestMediaCall | No |  |
| TAPI Call Center Functions |
| lineAgentSpecific | No |  |
| lineGetAgentActivityList | No |  |
| lineGetAgentCaps | No |  |
| lineGetAgentGroupList | No |  |
| lineGetAgentStatus | No |  |
| lineProxyMessage | No |  |
| lineProxyResponse | No |  |
| lineSetAgentActivity | No |  |
| lineSetAgentGroup | No |  |
| lineSetAgentState | No |  |
| TAPI Call Center Messages |
| LINE_AGENTSPECIFIC | No |  |
| LINE_AGENTSTATUS | No |  |
| LINE_PROXYREQUEST | No |  |
| TAPI Call Center Structures |
| LINEAGENTACTIVITYENTRY | No |  |
| LINEAGENTACTIVITYLIST | No |  |
| LINEAGENTCAPS | No |  |
| LINEAGENTGROUPENTRY | No |  |
| LINEAGENTGROUPLIST | No |  |
| LINEAGENTSTATUS | No |  |
| LINEPROXYREQUEST | No |  |
| Wave Functions |
| waveInAddBuffer | Yes |  |
| waveInClose | Yes |  |
| waveInGetDevCaps | No |  |
| waveInGetErrorText | No |  |
| waveInGetID | Yes |  |
| waveInGetNumDevs | No |  |
| waveInGetPosition | Yes |  |
| waveInMessage | No |  |
| waveInOpen | Yes |  |
| waveInPrepareHeader | Yes |  |
| waveInProc | No |  |
| waveInReset | Yes |  |
| waveInStart | Yes |  |
| waveInStop | No |  |
| waveInUnprepareHeader | Yes |  |
| waveOutBreakLoop | No |  |
| waveOutClose | Yes |  |
| waveOutGetDevCaps | Yes |  |
| waveOutGetErrorText | No |  |
| waveOutGetID | Yes |  |
| waveOutGetNumDevs | No |  |
| waveOutGetPitch | No |  |
| waveOutGetPlaybackRate | No |  |
| waveOutGetPosition | No |  |
| waveOutGetVolume | No |  |
| waveOutMessage | No |  |
| waveOutOpen | Yes |  |
| waveOutPause | No |  |
| waveOutPrepareHeader | Yes |  |
| waveOutProc | No |  |
| waveOutReset | Yes |  |
| waveOutRestart | No |  |
| waveOutSetPitch | No |  |
| waveOutSetPlaybackRate | No |  |
| waveOutSetVolume | No |  |
| waveOutUnprepareHeader | Yes |  |
| waveOutWrite | Yes |  |