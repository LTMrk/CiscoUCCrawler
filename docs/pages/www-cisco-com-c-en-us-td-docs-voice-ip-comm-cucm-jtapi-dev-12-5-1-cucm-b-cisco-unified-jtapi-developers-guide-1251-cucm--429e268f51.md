---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-jtapi-dev-12-5-1-cucm-b-cisco-unified-jtapi-developers-guide-1251-cucm--429e268f51
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/jtapi_dev/12_5_1/cucm_b_cisco-unified-jtapi-developers-guide-1251/cucm_b_cisco-unified-jtapi-developers-guide-1251_appendix_01001.html
retrieved_at: 2026-08-16T18:13:09.257111+00:00
---

Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1)

# Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1)

Updated: June 11, 2025

Chapter: Cisco Unified JTAPI Classes and Interfaces

## Chapter: Cisco Unified JTAPI Classes and Interfaces

# Cisco Unified JTAPI Classes and Interfaces

This
                        		appendix contains a listing of all classes and interfaces that are available in
                        		the Cisco Unified JTAPI implementation:

Cisco Unified JTAPI Version 1.2 Classes and Interfaces ,  which lists all the JTAPI v 1.2
                              			 classes and methods. The supported classes and methods have a check mark in the
                              			 Cisco Unified JTAPI Support column.

Cisco Unified JTAPI Extension Classes and Interfaces ,  which lists the Cisco Unified
                              			 JTAPI extension classes and methods.

Cisco Trace Logging Classes and Interfaces ,  which lists the error tracing
                              			 classes and methods.

## Cisco Unified JTAPI Version 1.2 Classes and Interfaces

### Core Package

The following table lists each JTAPI interface in the JTAPI
                                 		  Core Package followed by the associated method (s) and whether the classes are
                                 		  supported by the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnified JTAPI support

Comments

Address

addCallObserver

Yes

addressObserver

Yes

getAddressCapabilities

Yes

getCallObservers

Yes

getCapabilities

Yes

getConnections

Yes

getName

Yes

getObservers

Yes

getProvider

Yes

getTerminals

Yes

removeCallObserver

Yes

removeObserver

Yes

AddressObserver

addressChangedEvent

Yes

Call

addObserver

Yes

connect

Yes

A CallObserver must exist for the Terminal or Address
                                             						originating the call.

The FeaturePriority parameter is not supported.

getCallCapabilities

Yes

getCapabilities

Yes

getConnections

Yes

getObservers

Yes

getProvider

Yes

getState

Yes

removeObserver

Yes

CallObserver

callChangedEvent

Yes

Connection

disconnect

Yes

getAddress

Yes

getCall

Yes

getCapabilities

Yes

getConnectionCapabilities

Yes

getState

Yes

getTerminalConnections

Yes

JtapiPeer

getName

Yes

getProvider

Yes

getServices

Yes

JtapiPeerFactory

getJtapiPeer

Yes

Provider

addObserver

Yes

createCall

Yes

getAddress

Yes

getAddressCapabilities ()

Yes

getAddressCapabilities (Terminal)

Yes

getAddresses

Yes

getCallCapabilities ()

Yes

getCallCapabilities (Terminal, Address)

Yes

getCalls

Yes

This method returns calls only when there are CallObservers
                                             						attached to Addresses or Terminals, when a RouteAddress is registered for
                                             						routing, or when a CiscoMediaTerminal is registered.

getCapabilities

Yes

getConnectionCapabilities ()

Yes

getConnectionCapabilities (Terminal, Address)

Yes

getName

Yes

getObservers

Yes

getProviderCapabilities ()

Yes

getProviderCapabilities (Terminal)

Yes

getState

Yes

getTerminal

Yes

getTerminalCapabilities ()

Yes

getTerminalCapabilities (Terminal)

Yes

getTerminalConnectionCapabilities ()

Yes

getTerminalConnectionCapab ilities (Terminal)

Yes

getTerminals

Yes

removeObserver

Yes

shutdown

Yes

ProviderObserver

providerChangedEvent

Yes

Terminal

addCallObserver

Yes

addObserver

Yes

getAddresses

Yes

getCallObservers

Yes

getCapabilities

Yes

getName

Yes

getObservers

Yes

getProvider

Yes

getTerminalCapabilities

Yes

getTerminalConnections

Yes

removeCallObserver

Yes

removeObserver

Yes

TerminalConnection

answer

Yes

getCapabilities

Yes

getConnection

Yes

getState

Yes

getTerminal

Yes

getTerminalConnectionCapabilities

Yes

TerminalObserver

terminalChangedEvent

Yes

### Call Center Package

The following table lists each JTAPI interface in the JTAPI
                                 		  Call Center Package followed by the associated method(s) and whether the
                                 		  classes are supported by the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

ACDAddress

getACDManagerAddress

getLoggedOnAgents

getNumberQueued

getOldestCallQueued

getQueueWaitTime

getRelativeQueueLoad

ACDAddressObserver

ACDConnection

getACDManagerConnection

ACDManagerAddress

getACDAddresses

ACDManagerConnection

getACDConnections

Agent

getACDAddress

getAgentAddress

getAgentID

getAgentTerminal

getState

setState

AgentTerminal

addAgent

getAgents

removeAgents

setAgents

AgentTerminalObserver

CallCenterAddress

addCallObserver

CallCenterCall

connectPredictive

getApplicationData

getTrunks

setApplicationData

CallCenterCallObserver

CallCenterProvider

getACDAddresses

getACDManagerAddresses

getRouteableAddresses

CallCenterTrunk

getCall

getName

getState

getType

RouteAddress

cancelRouteCallback

Yes

getActiveRouteSessions

Yes

getRouteCallback

Yes

registerRouteCallback

Yes

RouteCallback

reRouteEvent

Yes

routeCallbackEndedEvent

Yes

routeEndEvent

Yes

routeEvent

Yes

routeUsedEvent

Yes

RouteSession

endRoute

Yes

getCause

Yes

getRouteAddress

Yes

getState

Yes

selectRoute

Yes

### Call Center Capabilities Package

The following table lists each JTAPI interface in the JTAPI
                                 		  Call Center Capabilities Package followed by the associated method(s), and
                                 		  whether the classes are supported by the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

ACDAddressCapabilities

canGetACDManagerAddress

canGetLoggedOnAgents

canGetNumberQueued

canGetOldestCallQueued

canGetQueueWaitTime

canGetRelativeQueueLoad

ACDConnectionCapabilities

canGetACDManagerConnection

ACDManagerAddressCapabilities

canGetACDAddresses

ACDManagerConnectionCapabilities

canGetACDConnections

AgentTerminalCapabilities

canHandleAgents

CallCenterAddressCapabilities

canAddCallObserver

CallCenterCallCapabilities

canConnectPredictive

canGetTrunks

canHandleApplicationData

CallCenterProviderCapabilities

canGetACDAddresses

Yes

canGetACDManagerAddresses

Yes

canGetRouteableAddresses

Yes

RouteAddressCapabilities

canRouteCalls

Yes

### Call Center Events Package

The following table lists each JTAPI interface in the JTAPI
                                 		  Call Center Events Package followed by the associated method(s), and whether
                                 		  the classes are supported by the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

ACDAddrBusyEv

ACDAddrEv

getAgent

getAgentAddress

getAgentTerminal

getState

getTrunks

ACDAddrLoggedOffEv

ACDAddrLoggedOnEv

ACDAddrNotReadyEv

ACDAddrReadyEv

ACDAddrUnknownEv

ACDAddrWorkNotReadyEv

ACDAddrWorkReadyEv

AgentTermBusyEv

AgentTermEv

getACDAddress

getAgent

getAgentAddress

getAgentID

getState

AgentTermLoggedOffEv

AgentTermLoggedOnEv

AgentTermNotReadyEv

AgentTermReadyEv

AgentTermUnknownEv

AgentTermWorkNotReadyEv

AgentTermWorkReadyEv

CallCentCallAppDataEv

getApplicationData

CallCentCallEv

getCalledAddress

getCallingAddress

getCallingTerminal

getLastRedirectedAddress

getTrunks

CallCentConnEv

CallCentConnInProgressEv

CallCentEv

getCallCenterCause

CallCentTrunkEv

getTrunk

CallCentTrunkInvalidEv

CallCentTrunkValidEv

ReRouteEvent

Yes

RouteCallbackEndedEvent

getRouteAddress

Yes

RouteEndEvent

Yes

RouteEvent

getCallingAddress

Yes

getCallingTerminal

Yes

getCurrentRouteAddress

Yes

getRouteSelectAlgorithm

Yes

getSetupInformation

Yes

RouteSessionEvent

getRouteSession

Yes

RouteUsedEvent

getCallingAddress

Yes

getCallingTerminal

Yes

getDomain

Yes

getRouteUsed

Yes

### Call Control Package

The following table lists each JTAPI interface in the JTAPI
                                 		  Call Control Package followed by the associated method(s) and whether the
                                 		  classes are supported by the Cisco Unified JTAPI Implementation.

Class names

Method names

CiscoUnifiedJTAPI support

Comments

CallControlAddress

cancelForwarding

Yes

Only for Call Forward All

getDoNotDisturb

getForwarding

Yes

Only for Call Forward All

getMessageWaiting

setDoNotDisturb

setForwarding

Yes

Only for Call Forward All

setMessageWaiting

CallControlCall

addParty

conference

Yes

In a consult conference scenario, only
                                             						OriginalCall.conference (ConsultCall ) is supported. ConsultCall.conference
                                             						(OriginalCall) is not supported.

consult(TerminalConnection)

Yes

consult(TerminalConnection, String)

Yes

drop

Yes

getCalledAddress

Yes

getCallingAddress

Yes

getCallingTerminal

Yes

getConferenceController

Yes

getConferenceEnable

Yes

getLastRedirectedAddress

Yes

getTransferController

Yes

getTransferEnable

Yes

offHook

Yes

setConferenceController

Yes

setConferenceEnable

Yes

setTransferController

Yes

setTransferEnable

Yes

transfer(Call)

Yes

In a consult transfer scenario, only OriginalCall.transfer
                                             						(ConsultCall) is supported. ConsultCall.transfer (OriginalCall) is not
                                             						supported.

transfer(String)

Yes

CallControlCallObserver

Yes

CallControlConnection

accept

Yes

addToAddress

Yes

getCallControlState

Yes

park

Yes

redirect

Yes

Redirect allows a connection in the CallControlConnection.
                                             						ESTABLISHED state to be redirected.

reject

Yes

CallControlForwarding

getDestinationAddress

getFilter

getSpecificCaller

getType

CallControlTerminal

getDoNotDisturb

pickup (Address, Address)

pickup (Connection, Address)

pickup (TerminalConnection, Address)

pickupFromGroup(Address)

pickupFromGroup(String, Address)

setDoNotDisturb

CallControlTerminalConnection

getCallControlState

Yes

hold

Yes

join

Yes

Only implemented for CiscoIntercomAddresses

leave

unhold

Yes

CallControlTerminalObserver

### Call Control Capabilities Package

The following table lists each JTAPI interface in the JTAPI
                                 		  Call Control Capabilities Package followed by the associated method(s) and
                                 		  whether the classes are supported by the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

CallControlAddressCapabilities

canCancelForwarding

Yes

canGetDoNotDisturb

Yes

canGetForwarding

Yes

canGetMessageWaiting

Yes

canSetDoNotDisturb

Yes

canSetForwarding

Yes

canSetMessageWaiting

Yes

CallControlCallCapabilities

canAddParty

Yes

canConference

Yes

canConsult

Yes

canConsult(TerminalConnection)

Yes

canConsult(TerminalConnection, String)

Yes

canDrop

Yes

canOffHook

Yes

canSetConferenceController

Yes

canSetConferenceEnable

Yes

canSetTransferController

Yes

canSetTransferEnable

Yes

canTransfer

Yes

canTransfer(Call)

Yes

canTransfer(String)

Yes

CallControlConnectionCapabilities

canAccept

Yes

canAddToAddress

Yes

canPark

Yes

canRedirect

Yes

canReject

Yes

CallControlTerminalCapabilities

canGetDoNotDisturb

Yes

canPickup

Yes

canPickup(Address, Address)

Yes

canPickup(Connection, Address)

Yes

canPickup(TerminalConnection, Address)

Yes

canPickupFromGroup

Yes

canPickupFromGroup(Address)

Yes

canPickupFromGroup(String, Address)

Yes

canSetDoNotDisturb

Yes

CallControlTerminalConnectionCapabilities

canHold

Yes

canJoin

Yes

canLeave

Yes

canUnhold

Yes

### Call Control
                           	 Events Package

The
                                 		  following table lists each JTAPI interface in the JTAPI Call Control Events
                                 		  Package followed by the associated method(s) and whether the classes are
                                 		  supported by the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

Comments

CallCtlAddrDoNotDisturbEv

getDoNotDisturbState

CallCtlAddrEv

CallCtlAddrForwardEv

getForwarding

Yes

CallCtlAddrMessageWaitingEv

getMessageWaitingState

CallCtlCallEv

getCalledState

Yes

getCallingAddress

Yes

getCallingTerminal

Yes

getLastRedirectedAddress

Yes

CallCtlConnAlertingEv

Yes

CallCtlConnDialingEv

getDigits

Yes

CallCtlConnDisconnectedEv

Yes

CallCtlConnEstablishedEv

Yes

CallCtlConnEv

Yes

CallCtlConnFailedEv

Yes

CallCtlConnInitiatedEv

Yes

CallCtlConnNetworkAlertingEv

Yes

CallCtlConnNetworkReachedEv

Yes

CallCtlConnOfferedEv

Yes

CallCtlConnQueuedEv

getNumberInQueue

Yes

CallCtlConnUnknownEv

Yes

CallCtlEv

getCallControlCause

Yes

CallCtlTermConnBridgedEv

CallCtlTermConnDroppedEv

Yes

CallCtlTermConnEv

Yes

CallCtlTermConnHeldEv

Yes

CallCtlTermConnInUseEv

CallCtlTermConnRingingEv

Yes

CallCtlTermConnTalkingEv

Yes

CallCtlTermConnUnknownEv

Yes

CallCtlTermDoNotDisturbEv

CallCtlTermEv

### Capabilities
                           	 Package

The
                                 		  following table lists each JTAPI interface in the JTAPI Capabilities Package
                                 		  followed by the associated method(s) and whether the classes are supported by
                                 		  the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

Comments

AddressCapabilities

isObservable

Yes

CallCapabilities

canConnect

Yes

isObservable

Yes

ConnectionCapabilities

canDisconnect

Yes

ProviderCapabilities

isObservable

Yes

TerminalCapabilities

isObservable

Yes

TerminalConnectionCapabilities

canAnswer

Yes

### Events Package

The following table lists each JTAPI interface in the JTAPI
                                 		  Events Package followed by the associated method(s) and whether the classes are
                                 		  supported by the Cisco Unified JTAPI Implementation.

Class names

Method names

CiscoUnifiedJTAPI support

AddrEv

getAddress

Yes

AddrObservationEndedEv

Yes

CallActiveEv

Yes

CallEv

getCall

Yes

CallInvalidEv

Yes

CallObservationEndedEv

getEndedObject

Yes

ConnAlertingEv

Yes

ConnConnectedEv

Yes

ConnCreatedEv

Yes

ConnDisconnectedEv

Yes

ConnEv

getConnection

Yes

ConnFailedEv

Yes

ConnInProgressEv

Yes

ConnUnknownEv

Yes

Ev

getCause

Yes

getID

Yes

getMetaCode

Yes

getObserved

Yes

isNewMetaEvent

Yes

ProvEv

getProvider

Yes

ProvInServiceEv

Yes

ProvObservationEndedEv

Yes

ProvOutOfServiceEv

Yes

ProvShutdownEv

Yes

TermConnActiveEv

Yes

TermConnCreatedEv

Yes

TermConnDroppedEv

Yes

TermConnEvgetTerminalConnection

Yes

TermConnPassiveEv

TermConnRingingEv

Yes

TermConnUnknownEv

Yes

TermEv

getTerminal

Yes

TermObservationEndedEv

Yes

### Media
                           	 Package

The
                                 		  following table lists each JTAPI interface from the JTAPI Media Package
                                 		  followed by the associated method(s) and whether the classes are supported by
                                 		  the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

Comments

MediaCallObserver

Yes

MediaTerminalConnection

generateDtmf

Yes

getMediaAvailability

getMediaState

setDtmfDetection

Yes

startPlaying

startRecording

stopPlaying

stopRecording

useDefaultMicrophone

useDefaultSpeaker

usePlayURL

useRecordURL

### Media Capabilities
                           	 Package

The
                                 		  following table lists each JTAPI interface in the JTAPI Media Capabilities
                                 		  Package followed by the associated method(s) and whether the classes are
                                 		  supported by the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

Comments

MediaTerminalConnection Capabilities

canDetectDtmf

Yes

canGenerateDtmf

Yes

canStartPlaying

Yes

canStartRecording

Yes

canStopPlaying

Yes

canStopRecording

Yes

canUseDefaultMicrophone

Yes

canUseDefaultSpeaker

Yes

canUsePlayURL

Yes

canUseRecordURL

Yes

### Media Events
                           	 Package

The
                                 		  following table lists each JTAPI interface in the JTAPI Media Events Package
                                 		  followed by the associated method(s) and whether the classes are supported by
                                 		  the Cisco Unified JTAPI implementation.

Class names

Method names

CiscoUnifiedJTAPI support

Comments

MediaEv

getMediaCause

Yes

MediaTermConnAvailableEv

MediaTermConnDtmfEv

getDtmfDigit

Yes

MediaTermConnEv

Yes

MediaTermConnStateEv

getMediaState

MediaTermConnUnavailableEv

### Unsupported
                           	 Packages

The
                                 		  following table shows the JTAPI packages that are not supported by the Cisco
                                 		  Unified JTAPI implementation.

Unsupported JTAPI packages

JTAPI Phone Package

JTAPI Phone Capabilities Package

JTAPI Phone Events Package

JTAPI Private Data Package

JTAPI Private Data Capabilities Package

JTAPI Private Data Events Package

## Cisco Unified JTAPI Extension Classes and Interfaces

### Cisco Unified
                           	 JTAPI Extension Classes

Cisco extension classes

Method names

CiscoMediaCapability

getMaxFramesPerPacket()

getPayloadType()

toString()

CiscoG711MediaCapability

CiscoG723MediaCapability

getBitRate()

toString()

CiscoGSMMediaCapability

RegistrationException

UnregistrationException

### Cisco Unified
                           	 JTAPI Extension Interfaces

Cisco extension interfaces

Method names

CiscoAddrCreatedEv

getAddress()

CiscoAddress

getType()

CiscoAddressObserver

CiscoAddrEv

CiscoAddrInService

CiscoAddrOutOfService

CiscoCall

getCallID()

CiscoCallEv

CiscoCallID

getCall()

intValue()

CiscoConferenceEndEv

getConferenceCall()

getFinalCall()

getHeldConferenceController()

getTalkingConferenceController()

CiscoConferenceStartEv

getConferenceCall()

getFinalCall()

getHeldConferenceController()

getTalkingConferenceController()

CiscoConnection

getConnectionID()

getReason()

redirect(String destinationAddress,  int mode,  int
                                             					 callingSearchSpace,  int calledAddressOption,

String preferredOriginalCalledParty,  String facCode,  String
                                             					 cmcCode,  int featurePriority,  byte[] applicationXMLData)

CiscoConnectionID

getConnection()

intValue()

CiscoConsultCall

getConsultingTerminalConnection()

CiscoConsultCallActiveEv

getHeldTerminalConnection()

CiscoEv

CiscoJtapiPeer

CiscoMediaTerminal

getRTPInputProperties()

getRTPOutputProperties()

register(InetAddress,  int)

unregister()

CiscoProvEv

CiscoProvider

getCallbackGuardEnabled()

getMediaTerminal()

getMediaTerminals()

setCallbackGuardEnabled()

getRemoteTerminals()

getRemoteTerminal(String name)

CiscoProvConnToLeastPriorCtiServerEv

CiscoProvFallbackToPrimNwCompltdEv

CiscoProvPrimNwReachableEv

getReachableCtiServers()

CiscoProviderObserver

CiscoProvTerminalRemoteDestinationChangedEv

getTerminal()

getRemoteDestinations()

isMyAppLastToSetActiveRD()

getIPAddressingMode()

getIPV4Address()

getIPV6Address()

CiscoRecorderInfo

getRecordingType()

CiscoRemoteDestinationInfo

getRemoteDestinationName()

getRemoteDestinationNumber()

getIsActiveRD()

CiscoRemoteTerminal

getAllRemoteDestinations()

getActiveRemoteDestinations()

setActiveRemoteDestination(String remoteDestinationNumber, 
                                             					 boolean isActiveRD)

addRemoteDestination(String remoteDestinationName,  String
                                             					 remoteDestinationNumber,  boolean isActiveRD)

removeRemoteDestination(String remoteDestinationNumber)

removeAllRemoteDestinations()

updateRemoteDestinationName(String remoteDestinationNumber, 
                                             					 String remoteDestinationName)

updateRemoteDestinationNumber(String remoteDestinationNumber, 
                                             					 StringnewRemoteDestinationNumber)

updateRemoteDestination(String remoteDestinationNumber,  String
                                             					 remoteDestinationName,  String newRemoteDestinationNumber,  boolean isActiveRD)

isRegisteredByThisApp() Cisco Extend & Connect (CTI Remote
                                             					 Device)

getRegistrationType()

isMyAppLastToSetActiveRD()

CiscoRouteSession

getCall()

selectRoute(String[] routeSelected,  int callingSearchSpace, 
                                             					 String[] modifyingCallingNumber,

String[] preferedOriginalCalledNumber,  int[]
                                             					 preferedOriginalCalledOption,  String[] facCode,

String[] cmcCode,  int featurePriority,  byte[][]
                                             					 applicationXMLData)

CiscoRTPInputProperties

getBitRate()

getEchoCancellation()

getLocalAddress()

getLocalPort()

getPacketSize()

getPayloadType()

CiscoRTPInputStartedEv

getRTPInputProperties()

CiscoRTPInputStoppedEv

CiscoRTPOutputProperties

getBitRate()

getMaxFramesPerPacket()

getPacketSize()

getPayloadType()

getPrecedenceValue()

getRemoteAddress()

getRemotePort()

CiscoRTPOutputStartedEv

getRTPOutputProperties()

CiscoRTPOutputStoppedEv

CiscoSynronousObserver

CiscoTermCreatedEv

getTerminal()

CiscoTermEv

CiscoTerminal

getRegistrationState()

register()

unregister()

getType()

getTypeName()

CiscoTerminalConnection

startRecording(int playToneDirection,  int invocationType)

stopRecording(int invocationType)

CiscoTerminalObserver

CiscoTermInServiceEv

CiscoTermOutOfServiceEv

CiscoTransferEndEv

getFinalCall()

getTransferController()

getTransferredCall()

CiscoTransferStartEv

getFinalCall()

getTransferController()

getTransferredCall()

ObjectContainer

getObject()

setObject()

RTPBitRate

RTPPayload

## Cisco Trace Logging Classes and Interfaces

### Cisco Trace
                           	 Logging Classes

Cisco Trace Logging class

Method names

LogFileOutputStream

close()

flush()

getCurrentFile()

getFileExtension()

getFileNameBase()

getMaxFiles()

getMaxFileSize()

write(byte[],  int,  int)

write(int)

NullTraceWriter

close()

flush()

getEnabled()

print(String)

println(String)

OutputStreamTraceWriter

close()

flush()

getEnabled()

print(String)

println(String)

setOutputStream(OUputStream

TraceManagerFactory

getModules()

registerModule(String)

registerModule(TraceModule)

registerModule(TraceModule,  OutputStream)

### Cisco Trace
                           	 Logging Interfaces

Cisco Trace Logging interfaces

Method names

ConditionalTrace

disable()

enable()

Trace

append(Object)

append(String)

getName()

isEnabled()

print(Object)

print(String)

print(String,  Object)

print(String,  String)

println(Object)

println(String)

println(String,  Object)

println(String,  String)

setDefaultMnemonic(String)

TraceManager

disableAll()

disableTimeStamp()

enableAll()

enableTimeStamp()

getConditionalTrace(String)

getConditionalTrace(String,  String)

getName()

getOutputStream()

getSubFacilities()

getTraces()

getTraceWriter()

getUnconditionalTrace(String)

getUnconditionalTrace(String,  String)

removeTrace(String)

removeTrace(Trace)

setOutputStream(OutputStream)

setSubFacilities()

setTraceWriter()

TraceModule

getTraceManager()

getTraceModuleName()

TRACETYPE

TraceWriter

close()

flush()

getEnabled()

print(String)

println(String)

UnconditionalTrace

| Class names | Method names | CiscoUnified JTAPI support | Comments |
|---|---|---|---|
| Address | addCallObserver | Yes |  |
|  | addressObserver | Yes |  |
|  | getAddressCapabilities | Yes |  |
|  | getCallObservers | Yes |  |
|  | getCapabilities | Yes |  |
|  | getConnections | Yes |  |
|  | getName | Yes |  |
|  | getObservers | Yes |  |
|  | getProvider | Yes |  |
|  | getTerminals | Yes |  |
|  | removeCallObserver | Yes |  |
|  | removeObserver | Yes |  |
| AddressObserver | addressChangedEvent | Yes |  |
| Call | addObserver | Yes |  |
|  | connect | Yes | A CallObserver must exist for the Terminal or Address
                                             						originating the call. The FeaturePriority parameter is not supported. |
|  | getCallCapabilities | Yes |  |
|  | getCapabilities | Yes |  |
|  | getConnections | Yes |  |
|  | getObservers | Yes |  |
|  | getProvider | Yes |  |
|  | getState | Yes |  |
|  | removeObserver | Yes |  |
| CallObserver | callChangedEvent | Yes |  |
| Connection | disconnect | Yes |  |
|  | getAddress | Yes |  |
|  | getCall | Yes |  |
|  | getCapabilities | Yes |  |
|  | getConnectionCapabilities | Yes |  |
|  | getState | Yes |  |
|  | getTerminalConnections | Yes |  |
| JtapiPeer | getName | Yes |  |
|  | getProvider | Yes |  |
|  | getServices | Yes |  |
| JtapiPeerFactory | getJtapiPeer | Yes |  |
| Provider | addObserver | Yes |  |
|  | createCall | Yes |  |
|  | getAddress | Yes |  |
|  | getAddressCapabilities () | Yes |  |
|  | getAddressCapabilities (Terminal) | Yes |  |
|  | getAddresses | Yes |  |
|  | getCallCapabilities () | Yes |  |
|  | getCallCapabilities (Terminal, Address) | Yes |  |
|  | getCalls | Yes | This method returns calls only when there are CallObservers
                                             						attached to Addresses or Terminals, when a RouteAddress is registered for
                                             						routing, or when a CiscoMediaTerminal is registered. |
|  | getCapabilities | Yes |  |
|  | getConnectionCapabilities () | Yes |  |
|  | getConnectionCapabilities (Terminal, Address) | Yes |  |
|  | getName | Yes |  |
|  | getObservers | Yes |  |
|  | getProviderCapabilities () | Yes |  |
|  | getProviderCapabilities (Terminal) | Yes |  |
|  | getState | Yes |  |
|  | getTerminal | Yes |  |
|  | getTerminalCapabilities () | Yes |  |
|  | getTerminalCapabilities (Terminal) | Yes |  |
|  | getTerminalConnectionCapabilities () | Yes |  |
|  | getTerminalConnectionCapab ilities (Terminal) | Yes |  |
|  | getTerminals | Yes |  |
|  | removeObserver | Yes |  |
|  | shutdown | Yes |  |
| ProviderObserver | providerChangedEvent | Yes |  |
| Terminal | addCallObserver | Yes |  |
|  | addObserver | Yes |  |
|  | getAddresses | Yes |  |
|  | getCallObservers | Yes |  |
|  | getCapabilities | Yes |  |
|  | getName | Yes |  |
|  | getObservers | Yes |  |
|  | getProvider | Yes |  |
|  | getTerminalCapabilities | Yes |  |
|  | getTerminalConnections | Yes |  |
|  | removeCallObserver | Yes |  |
|  | removeObserver | Yes |  |
| TerminalConnection | answer | Yes |  |
|  | getCapabilities | Yes |  |
|  | getConnection | Yes |  |
|  | getState | Yes |  |
|  | getTerminal | Yes |  |
|  | getTerminalConnectionCapabilities | Yes |  |
| TerminalObserver | terminalChangedEvent | Yes |  |

| Class names | Method names | CiscoUnifiedJTAPI support |
|---|---|---|
| ACDAddress | getACDManagerAddress |  |
|  | getLoggedOnAgents |  |
|  | getNumberQueued |  |
|  | getOldestCallQueued |  |
|  | getQueueWaitTime |  |
|  | getRelativeQueueLoad |  |
| ACDAddressObserver |  |  |
| ACDConnection | getACDManagerConnection |  |
| ACDManagerAddress | getACDAddresses |  |
| ACDManagerConnection | getACDConnections |  |
| Agent | getACDAddress |  |
|  | getAgentAddress |  |
|  | getAgentID |  |
|  | getAgentTerminal |  |
|  | getState |  |
|  | setState |  |
| AgentTerminal | addAgent |  |
|  | getAgents |  |
|  | removeAgents |  |
|  | setAgents |  |
| AgentTerminalObserver |  |  |
| CallCenterAddress | addCallObserver |  |
| CallCenterCall | connectPredictive |  |
|  | getApplicationData |  |
|  | getTrunks |  |
|  | setApplicationData |  |
| CallCenterCallObserver |  |  |
| CallCenterProvider | getACDAddresses |  |
|  | getACDManagerAddresses |  |
|  | getRouteableAddresses |  |
| CallCenterTrunk | getCall |  |
|  | getName |  |
|  | getState |  |
|  | getType |  |
| RouteAddress | cancelRouteCallback | Yes |
|  | getActiveRouteSessions | Yes |
|  | getRouteCallback | Yes |
|  | registerRouteCallback | Yes |
| RouteCallback | reRouteEvent | Yes |
|  | routeCallbackEndedEvent | Yes |
|  | routeEndEvent | Yes |
|  | routeEvent | Yes |
|  | routeUsedEvent | Yes |
| RouteSession | endRoute | Yes |
|  | getCause | Yes |
|  | getRouteAddress | Yes |
|  | getState | Yes |
|  | selectRoute | Yes |

| Class names | Method names | CiscoUnifiedJTAPI support |
|---|---|---|
| ACDAddressCapabilities | canGetACDManagerAddress |  |
|  | canGetLoggedOnAgents |  |
|  | canGetNumberQueued |  |
|  | canGetOldestCallQueued |  |
|  | canGetQueueWaitTime |  |
|  | canGetRelativeQueueLoad |  |
| ACDConnectionCapabilities | canGetACDManagerConnection |  |
| ACDManagerAddressCapabilities | canGetACDAddresses |  |
| ACDManagerConnectionCapabilities | canGetACDConnections |  |
| AgentTerminalCapabilities | canHandleAgents |  |
| CallCenterAddressCapabilities | canAddCallObserver |  |
| CallCenterCallCapabilities | canConnectPredictive |  |
|  | canGetTrunks |  |
|  | canHandleApplicationData |  |
| CallCenterProviderCapabilities | canGetACDAddresses | Yes |
|  | canGetACDManagerAddresses | Yes |
|  | canGetRouteableAddresses | Yes |
| RouteAddressCapabilities | canRouteCalls | Yes |

| Class names | Method names | CiscoUnifiedJTAPI support |
|---|---|---|
| ACDAddrBusyEv |  |  |
| ACDAddrEv | getAgent |  |
|  | getAgentAddress |  |
|  | getAgentTerminal |  |
|  | getState |  |
|  | getTrunks |  |
| ACDAddrLoggedOffEv |  |  |
| ACDAddrLoggedOnEv |  |  |
| ACDAddrNotReadyEv |  |  |
| ACDAddrReadyEv |  |  |
| ACDAddrUnknownEv |  |  |
| ACDAddrWorkNotReadyEv |  |  |
| ACDAddrWorkReadyEv |  |  |
| AgentTermBusyEv |  |  |
| AgentTermEv | getACDAddress |  |
|  | getAgent |  |
|  | getAgentAddress |  |
|  | getAgentID |  |
|  | getState |  |
| AgentTermLoggedOffEv |  |  |
| AgentTermLoggedOnEv |  |  |
| AgentTermNotReadyEv |  |  |
| AgentTermReadyEv |  |  |
| AgentTermUnknownEv |  |  |
| AgentTermWorkNotReadyEv |  |  |
| AgentTermWorkReadyEv |  |  |
| CallCentCallAppDataEv | getApplicationData |  |
| CallCentCallEv | getCalledAddress |  |
|  | getCallingAddress |  |
|  | getCallingTerminal |  |
|  | getLastRedirectedAddress |  |
|  | getTrunks |  |
| CallCentConnEv |  |  |
| CallCentConnInProgressEv |  |  |
| CallCentEv | getCallCenterCause |  |
| CallCentTrunkEv | getTrunk |  |
| CallCentTrunkInvalidEv |  |  |
| CallCentTrunkValidEv |  |  |
| ReRouteEvent |  | Yes |
| RouteCallbackEndedEvent | getRouteAddress | Yes |
| RouteEndEvent |  | Yes |
| RouteEvent | getCallingAddress | Yes |
|  | getCallingTerminal | Yes |
|  | getCurrentRouteAddress | Yes |
|  | getRouteSelectAlgorithm | Yes |
|  | getSetupInformation | Yes |
| RouteSessionEvent | getRouteSession | Yes |
| RouteUsedEvent | getCallingAddress | Yes |
|  | getCallingTerminal | Yes |
|  | getDomain | Yes |
|  | getRouteUsed | Yes |

| Class names | Method names | CiscoUnifiedJTAPI support | Comments |
|---|---|---|---|
| CallControlAddress | cancelForwarding | Yes | Only for Call Forward All |
|  | getDoNotDisturb |  |  |
|  | getForwarding | Yes | Only for Call Forward All |
|  | getMessageWaiting |  |  |
|  | setDoNotDisturb |  |  |
|  | setForwarding | Yes | Only for Call Forward All |
|  | setMessageWaiting |  |  |
| CallControlCall | addParty |  |  |
|  | conference | Yes | In a consult conference scenario, only
                                             						OriginalCall.conference (ConsultCall ) is supported. ConsultCall.conference
                                             						(OriginalCall) is not supported. |
|  | consult(TerminalConnection) | Yes |  |
|  | consult(TerminalConnection, String) | Yes |  |
|  | drop | Yes |  |
|  | getCalledAddress | Yes |  |
|  | getCallingAddress | Yes |  |
|  | getCallingTerminal | Yes |  |
|  | getConferenceController | Yes |  |
|  | getConferenceEnable | Yes |  |
|  | getLastRedirectedAddress | Yes |  |
|  | getTransferController | Yes |  |
|  | getTransferEnable | Yes |  |
|  | offHook | Yes |  |
|  | setConferenceController | Yes |  |
|  | setConferenceEnable | Yes |  |
|  | setTransferController | Yes |  |
|  | setTransferEnable | Yes |  |
|  | transfer(Call) | Yes | In a consult transfer scenario, only OriginalCall.transfer
                                             						(ConsultCall) is supported. ConsultCall.transfer (OriginalCall) is not
                                             						supported. |
|  | transfer(String) | Yes |  |
| CallControlCallObserver |  | Yes |  |
| CallControlConnection | accept | Yes |  |
|  | addToAddress | Yes |  |
|  | getCallControlState | Yes |  |
|  | park | Yes |  |
|  | redirect | Yes | Redirect allows a connection in the CallControlConnection.
                                             						ESTABLISHED state to be redirected. |
|  | reject | Yes |  |
| CallControlForwarding | getDestinationAddress |  |  |
|  | getFilter |  |  |
|  | getSpecificCaller |  |  |
|  | getType |  |  |
| CallControlTerminal | getDoNotDisturb |  |  |
|  | pickup (Address, Address) |  |  |
|  | pickup (Connection, Address) |  |  |
|  | pickup (TerminalConnection, Address) |  |  |
|  | pickupFromGroup(Address) |  |  |
|  | pickupFromGroup(String, Address) |  |  |
|  | setDoNotDisturb |  |  |
| CallControlTerminalConnection | getCallControlState | Yes |  |
|  | hold | Yes |  |
|  | join | Yes | Only implemented for CiscoIntercomAddresses |
|  | leave |  |  |
|  | unhold | Yes |  |
| CallControlTerminalObserver |  |  |  |

| Class names | Method names | CiscoUnifiedJTAPI support |
|---|---|---|
| CallControlAddressCapabilities | canCancelForwarding | Yes |
|  | canGetDoNotDisturb | Yes |
|  | canGetForwarding | Yes |
|  | canGetMessageWaiting | Yes |
|  | canSetDoNotDisturb | Yes |
|  | canSetForwarding | Yes |
|  | canSetMessageWaiting | Yes |
| CallControlCallCapabilities | canAddParty | Yes |
|  | canConference | Yes |
|  | canConsult | Yes |
|  | canConsult(TerminalConnection) | Yes |
|  | canConsult(TerminalConnection, String) | Yes |
|  | canDrop | Yes |
|  | canOffHook | Yes |
|  | canSetConferenceController | Yes |
|  | canSetConferenceEnable | Yes |
|  | canSetTransferController | Yes |
|  | canSetTransferEnable | Yes |
|  | canTransfer | Yes |
|  | canTransfer(Call) | Yes |
|  | canTransfer(String) | Yes |
| CallControlConnectionCapabilities | canAccept | Yes |
|  | canAddToAddress | Yes |
|  | canPark | Yes |
|  | canRedirect | Yes |
|  | canReject | Yes |
| CallControlTerminalCapabilities | canGetDoNotDisturb | Yes |
|  | canPickup | Yes |
|  | canPickup(Address, Address) | Yes |
|  | canPickup(Connection, Address) | Yes |
|  | canPickup(TerminalConnection, Address) | Yes |
|  | canPickupFromGroup | Yes |
|  | canPickupFromGroup(Address) | Yes |
|  | canPickupFromGroup(String, Address) | Yes |
|  | canSetDoNotDisturb | Yes |
| CallControlTerminalConnectionCapabilities | canHold | Yes |
|  | canJoin | Yes |
|  | canLeave | Yes |
|  | canUnhold | Yes |

| Class names | Method names | CiscoUnifiedJTAPI support | Comments |
|---|---|---|---|
| CallCtlAddrDoNotDisturbEv | getDoNotDisturbState |  |  |
| CallCtlAddrEv |  |  |  |
| CallCtlAddrForwardEv | getForwarding | Yes |  |
| CallCtlAddrMessageWaitingEv | getMessageWaitingState |  |  |
| CallCtlCallEv | getCalledState | Yes |  |
|  | getCallingAddress | Yes |  |
|  | getCallingTerminal | Yes |  |
|  | getLastRedirectedAddress | Yes |  |
| CallCtlConnAlertingEv |  | Yes |  |
| CallCtlConnDialingEv | getDigits | Yes |  |
| CallCtlConnDisconnectedEv |  | Yes |  |
| CallCtlConnEstablishedEv |  | Yes |  |
| CallCtlConnEv |  | Yes |  |
| CallCtlConnFailedEv |  | Yes |  |
| CallCtlConnInitiatedEv |  | Yes |  |
| CallCtlConnNetworkAlertingEv |  | Yes |  |
| CallCtlConnNetworkReachedEv |  | Yes |  |
| CallCtlConnOfferedEv |  | Yes |  |
| CallCtlConnQueuedEv | getNumberInQueue | Yes |  |
| CallCtlConnUnknownEv |  | Yes |  |
| CallCtlEv | getCallControlCause | Yes |  |
| CallCtlTermConnBridgedEv |  |  |  |
| CallCtlTermConnDroppedEv |  | Yes |  |
| CallCtlTermConnEv |  | Yes |  |
| CallCtlTermConnHeldEv |  | Yes |  |
| CallCtlTermConnInUseEv |  |  |  |
| CallCtlTermConnRingingEv |  | Yes |  |
| CallCtlTermConnTalkingEv |  | Yes |  |
| CallCtlTermConnUnknownEv |  | Yes |  |
| CallCtlTermDoNotDisturbEv |  |  |  |
| CallCtlTermEv |  |  |  |

| Class names | Method names | CiscoUnifiedJTAPI support | Comments |
|---|---|---|---|
| AddressCapabilities | isObservable | Yes |  |
| CallCapabilities | canConnect | Yes |  |
|  | isObservable | Yes |  |
| ConnectionCapabilities | canDisconnect | Yes |  |
| ProviderCapabilities | isObservable | Yes |  |
| TerminalCapabilities | isObservable | Yes |  |
| TerminalConnectionCapabilities | canAnswer | Yes |  |

| Class names | Method names | CiscoUnifiedJTAPI support |
|---|---|---|
| AddrEv | getAddress | Yes |
| AddrObservationEndedEv |  | Yes |
| CallActiveEv |  | Yes |
| CallEv | getCall | Yes |
| CallInvalidEv |  | Yes |
| CallObservationEndedEv | getEndedObject | Yes |
| ConnAlertingEv |  | Yes |
| ConnConnectedEv |  | Yes |
| ConnCreatedEv |  | Yes |
| ConnDisconnectedEv |  | Yes |
| ConnEv | getConnection | Yes |
| ConnFailedEv |  | Yes |
| ConnInProgressEv |  | Yes |
| ConnUnknownEv |  | Yes |
| Ev | getCause | Yes |
|  | getID | Yes |
|  | getMetaCode | Yes |
|  | getObserved | Yes |
|  | isNewMetaEvent | Yes |
| ProvEv | getProvider | Yes |
| ProvInServiceEv |  | Yes |
| ProvObservationEndedEv |  | Yes |
| ProvOutOfServiceEv |  | Yes |
| ProvShutdownEv |  | Yes |
| TermConnActiveEv |  | Yes |
| TermConnCreatedEv |  | Yes |
| TermConnDroppedEv |  | Yes |
| TermConnEvgetTerminalConnection |  | Yes |
| TermConnPassiveEv |  |  |
| TermConnRingingEv |  | Yes |
| TermConnUnknownEv |  | Yes |
| TermEv | getTerminal | Yes |
| TermObservationEndedEv |  | Yes |

| Class names | Method names | CiscoUnifiedJTAPI support | Comments |
|---|---|---|---|
| MediaCallObserver |  | Yes |  |
| MediaTerminalConnection | generateDtmf | Yes |  |
|  | getMediaAvailability |  |  |
|  | getMediaState |  |  |
|  | setDtmfDetection | Yes |  |
|  | startPlaying |  |  |
|  | startRecording |  |  |
|  | stopPlaying |  |  |
|  | stopRecording |  |  |
|  | useDefaultMicrophone |  |  |
|  | useDefaultSpeaker |  |  |
|  | usePlayURL |  |  |
|  | useRecordURL |  |  |

| Class names | Method names | CiscoUnifiedJTAPI support | Comments |
|---|---|---|---|
|  |  |  |  |
| MediaTerminalConnection Capabilities | canDetectDtmf | Yes |  |
|  | canGenerateDtmf | Yes |  |
|  | canStartPlaying | Yes |  |
|  | canStartRecording | Yes |  |
|  | canStopPlaying | Yes |  |
|  | canStopRecording | Yes |  |
|  | canUseDefaultMicrophone | Yes |  |
|  | canUseDefaultSpeaker | Yes |  |
|  | canUsePlayURL | Yes |  |
|  | canUseRecordURL | Yes |  |

| Class names | Method names | CiscoUnifiedJTAPI support | Comments |
|---|---|---|---|
| MediaEv | getMediaCause | Yes |  |
| MediaTermConnAvailableEv |  |  |  |
| MediaTermConnDtmfEv | getDtmfDigit | Yes |  |
| MediaTermConnEv |  | Yes |  |
| MediaTermConnStateEv | getMediaState |  |  |
| MediaTermConnUnavailableEv |  |  |  |

| Unsupported JTAPI packages |
|---|
| JTAPI Phone Package |
| JTAPI Phone Capabilities Package |
| JTAPI Phone Events Package |
| JTAPI Private Data Package |
| JTAPI Private Data Capabilities Package |
| JTAPI Private Data Events Package |

| Cisco extension classes | Method names |
|---|---|
| CiscoMediaCapability | getMaxFramesPerPacket() getPayloadType() toString() |
| CiscoG711MediaCapability |  |
| CiscoG723MediaCapability | getBitRate() toString() |
| CiscoGSMMediaCapability |  |
| RegistrationException |  |
| UnregistrationException |  |

| Cisco extension interfaces | Method names |
|---|---|
| CiscoAddrCreatedEv | getAddress() |
| CiscoAddress | getType() |
| CiscoAddressObserver |  |
| CiscoAddrEv |  |
| CiscoAddrInService |  |
| CiscoAddrOutOfService |  |
| CiscoCall | getCallID() |
| CiscoCallEv |  |
| CiscoCallID | getCall() intValue() |
| CiscoConferenceEndEv | getConferenceCall() getFinalCall() getHeldConferenceController() getTalkingConferenceController() |
| CiscoConferenceStartEv | getConferenceCall() getFinalCall() getHeldConferenceController() getTalkingConferenceController() |
| CiscoConnection | getConnectionID() getReason() redirect(String destinationAddress,  int mode,  int
                                             					 callingSearchSpace,  int calledAddressOption, String preferredOriginalCalledParty,  String facCode,  String
                                             					 cmcCode,  int featurePriority,  byte[] applicationXMLData) |
| CiscoConnectionID | getConnection() intValue() |
| CiscoConsultCall | getConsultingTerminalConnection() |
| CiscoConsultCallActiveEv | getHeldTerminalConnection() |
| CiscoEv |  |
| CiscoJtapiPeer |  |
| CiscoMediaTerminal | getRTPInputProperties() getRTPOutputProperties() register(InetAddress,  int) unregister() |
| CiscoProvEv |  |
| CiscoProvider | getCallbackGuardEnabled() getMediaTerminal() getMediaTerminals() setCallbackGuardEnabled() getRemoteTerminals() getRemoteTerminal(String name) |
| CiscoProvConnToLeastPriorCtiServerEv |  |
| CiscoProvFallbackToPrimNwCompltdEv |  |
| CiscoProvPrimNwReachableEv | getReachableCtiServers() |
| CiscoProviderObserver |  |
| CiscoProvTerminalRemoteDestinationChangedEv | getTerminal() getRemoteDestinations() isMyAppLastToSetActiveRD() getIPAddressingMode() getIPV4Address() getIPV6Address() |
| CiscoRecorderInfo | getRecordingType() |
| CiscoRemoteDestinationInfo | getRemoteDestinationName() getRemoteDestinationNumber() getIsActiveRD() |
| CiscoRemoteTerminal | getAllRemoteDestinations() getActiveRemoteDestinations() setActiveRemoteDestination(String remoteDestinationNumber, 
                                             					 boolean isActiveRD) addRemoteDestination(String remoteDestinationName,  String
                                             					 remoteDestinationNumber,  boolean isActiveRD) removeRemoteDestination(String remoteDestinationNumber) removeAllRemoteDestinations() updateRemoteDestinationName(String remoteDestinationNumber, 
                                             					 String remoteDestinationName) updateRemoteDestinationNumber(String remoteDestinationNumber, 
                                             					 StringnewRemoteDestinationNumber) updateRemoteDestination(String remoteDestinationNumber,  String
                                             					 remoteDestinationName,  String newRemoteDestinationNumber,  boolean isActiveRD) isRegisteredByThisApp() Cisco Extend & Connect (CTI Remote
                                             					 Device) getRegistrationType() isMyAppLastToSetActiveRD() |
| CiscoRouteSession | getCall() selectRoute(String[] routeSelected,  int callingSearchSpace, 
                                             					 String[] modifyingCallingNumber, String[] preferedOriginalCalledNumber,  int[]
                                             					 preferedOriginalCalledOption,  String[] facCode, String[] cmcCode,  int featurePriority,  byte[][]
                                             					 applicationXMLData) |
| CiscoRTPInputProperties | getBitRate() getEchoCancellation() getLocalAddress() getLocalPort() getPacketSize() getPayloadType() |
| CiscoRTPInputStartedEv | getRTPInputProperties() |
| CiscoRTPInputStoppedEv |  |
| CiscoRTPOutputProperties | getBitRate() getMaxFramesPerPacket() getPacketSize() getPayloadType() getPrecedenceValue() getRemoteAddress() getRemotePort() |
| CiscoRTPOutputStartedEv | getRTPOutputProperties() |
| CiscoRTPOutputStoppedEv |  |
| CiscoSynronousObserver |  |
| CiscoTermCreatedEv | getTerminal() |
| CiscoTermEv |  |
| CiscoTerminal | getRegistrationState() register() unregister() getType() getTypeName() |
| CiscoTerminalConnection | startRecording(int playToneDirection,  int invocationType) stopRecording(int invocationType) |
| CiscoTerminalObserver |  |
| CiscoTermInServiceEv |  |
| CiscoTermOutOfServiceEv |  |
| CiscoTransferEndEv | getFinalCall() getTransferController() getTransferredCall() |
| CiscoTransferStartEv | getFinalCall() getTransferController() getTransferredCall() |
| ObjectContainer | getObject() setObject() |
| RTPBitRate |  |
| RTPPayload |  |

| Cisco Trace Logging class | Method names |
|---|---|
| LogFileOutputStream | close() flush() getCurrentFile() getFileExtension() getFileNameBase() getMaxFiles() getMaxFileSize() write(byte[],  int,  int) write(int) |
| NullTraceWriter | close() flush() getEnabled() print(String) println(String) |
| OutputStreamTraceWriter | close() flush() getEnabled() print(String) println(String) setOutputStream(OUputStream |
| TraceManagerFactory | getModules() registerModule(String) registerModule(TraceModule) registerModule(TraceModule,  OutputStream) |

| Cisco Trace Logging interfaces | Method names |
|---|---|
| ConditionalTrace | disable() enable() |
| Trace | append(Object) append(String) getName() isEnabled() print(Object) print(String) print(String,  Object) print(String,  String) println(Object) println(String) println(String,  Object) println(String,  String) setDefaultMnemonic(String) |
| TraceManager | disableAll() disableTimeStamp() enableAll() enableTimeStamp() getConditionalTrace(String) getConditionalTrace(String,  String) getName() getOutputStream() getSubFacilities() getTraces() getTraceWriter() getUnconditionalTrace(String) getUnconditionalTrace(String,  String) removeTrace(String) removeTrace(Trace) setOutputStream(OutputStream) setSubFacilities() setTraceWriter() |
| TraceModule | getTraceManager() getTraceModuleName() |
| TRACETYPE |  |
| TraceWriter | close() flush() getEnabled() print(String) println(String) |
| UnconditionalTrace |  |