---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-cucis-api-cucis-api-guide-cucisa-api-html-27c2ef6f3b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/CUCIS_API/CUCIS_API_Guide/CUCISA_API.html
retrieved_at: 2026-08-16T15:55:10.209953+00:00
---

Cisco Unified Communications Gateway Services API Guide

# Cisco Unified Communications Gateway Services API Guide

Updated: July 27, 2017

Chapter: Provider and Field Descriptions

## Chapter: Provider and Field Descriptions

## Provider and Field Descriptions

## XCC

### XCC Provider Operations

The XCC (Extended Call Control) provider supports operations that allow a client application to perform call control and real-time call monitoring.

XccRegister

inOut

RequestXccRegister

ResponseXccRegister

fault: XMLParserError

fault: ServiceException

Allows application to register with XCC provider and specify the connection events filter

XccUnRegister

inOut

RequestXccUnRegister

ResponseXmfUnRegister

fault: XMLParserError

fault: ServiceException

Allows application to unregister with XCC provider

XccControlUpdate

inOut

RequestXccControlUpdate

ResponseXccControlUpdate

fault: XMLParserError

fault: ServiceException

Allows application to update parameters after registered

XccCallRelease

inOut

RequestXccCallRelease

ResponseXccCallRelease

fault: XMLParserError

fault: ServiceException

Allows application to release the call session

XccConnectionRelease

inOut

RequestXccConnectionRelease

ResponseXccConnectionRelease

fault: XMLParserError

fault: ServiceException

Allows application to release the connection from the call session

XccProviderUnregister

outIn

ResponseXccProviderUnRegister

SolicitXccProviderUnRegister

Allows XCC Provider to unregister with application

XccProviderStatus

OutOnly

NotifyXccProviderStatus

Updated application once XCC provider

XccCallMediaSetAttributes

inOut

RequestXccCallMediaSetAttributes

ResponseXccCallMediaSetAttributes

Allows application to specify the media attributes for a call session

XccCallMediaForking

inOut

RequestXccCallMediaForking

ResponseXccCallMediaForking

fault: XMLParserError

fault: ServiceException

Allows application to enable media forking a call session

XccCallData

outOnly

NotifyXccCallData

Notifies application that a call session on one of the following conditions:

- mode is changed

- a dtmf digit is detected

- media inactive or active is detected

XccConnectionAuthorize

outIn

ResponseXccConnectionAuthorize

SolicitXccConnectionAuthorize

Allows application to perform the connection authorization

XccConnectionAuthorizeDone

inOut

RequestXccConnectionAuthorizeDone

ResponseXccConnectionAuthorizeDone

fault: XMLParserError

fault: ServiceException

Allows application to handle the connection once the authorization is done

XccConnectionAddressAnalyze

outIn

ResponseXccConnectionAddressAnalyze

SolicitXccConnectionAddressAnalyze

Allows application to analyze the connection address

XccConnectionAddressAnalyzeDonr

inOut

RequestXccConnectionAddressAnalyzeDone

ResponseXccConnectionAddressAnalyzeDone

fault: XMLParserError

fault: ServiceException

Allows application to handle the connection once the analysis is done

XccConnectionMediaForking

inOut

RequestXccConnectionMediaForking

ResponseXccConnectionMediaForking

fault: XMLParserError

fault: ServiceException

Allows application to enable media forking for the call session

XccConnectionData

outOnly

NotifyXccConnectionData

Notifies application that a connection is in one of the following conditions:

- a new connection is created

- a connection is in call delivery state

- a connection is redirected to another destination

- a connection is in alerting state

- a conection is in connected state

- a connection is transferred to another target

- a connection is in disconnected state

- a connection is handoff and leave the call session

- a connection is handoff to the call session

XccProbing

outIn

ResponseXccProbing

SolicitXccProbing

Allows XCC provider to keep alive a registration session and probe its health

### XCC API Messages

### NotifyXccCallData

msgHeader

MsgHeader

M

Message header common for all the messages

callData

CallData

M

Call information

mediaEvent

cMediaEvent

M

Choice of media event

### NotifyXccConnectionData

msgHeader

MsgHeader

M

Message header common for all the messages

callData

CallData

M

Call information

connData

ConnData

M

Connection information

event

cConnectionData

M

Event choice

### NotifyXccProviderStatus

msgHeader

MsgHeader

M

Message header common for all the messages

applicationData

ApplicationData

M

Application URL configured in the router CLI

providerData

ProviderData

M

Provider data

providerStatus

eProviderStatus

M

Provider current status

### RequestXccCallMediaForking

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call Identification

action

cCallMediaForking

M

Provider data

### RequestXccCallMediaSetAttributes

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call identification

mediaEventsFilter

MediaEventsFilter

O

Enables media event types to be sent in an application. Turn off any media events if this element is not included in the request

mediaForking

MediaForkingData

O

Media Forking Data

### RequestXccCallRelease

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call identification

disCause

int

O

Q.850 disconnect cause range [1-188]

### RequestXccConnectionAddressAnalyzeDone

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call Identification

connID

string

M

Connection Identification

action

cConnectionAddressAnalyzeDone

M

Action choice

### RequestXccConnectionAuthorizeDone

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call Identification

connID

string

M

Connection Identification

action

cConnectionAuthorizeDone

M

Action choice

### RequestXccConnectionMediaForking

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call Identification

connID

string

M

Connection Identification

action

cCallMediaForking

M

Media forking action choice

### RequestXccConnectionRelease

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call Identification

connID

string

M

Connection Identification

discCause

int

M

Q.850 disconnect cause range [1 - 188]

### RequestXccControlUpdate

msgHeader

MsgHeader

M

Message header common for all the messages

connectionEventsFilter

ConnectionEventsFilter

O

List of events that shall be notified to application

mediaEventsFilter

MediaEventsFilter

O

List of media events that shall be notfied to application

blockingEventTimeoutSec

int

O

Some application responses may block. This timeout specifies how long XCC provider will wait for the response in seconds.

blockingTimeoutHandle

eBlockingTimeoutHandle

O

How XCC provider should handle the call when blocking event timeouts

### RequestXccRegister

msgHeader

MsgHeader

M

Message header common for all the messages

applicationData

ApplicationData

M

Application sends this request

providerData

ProviderData

M

XCC provider

connectionEventsFilter

ConnectionEventsFilter

O

List of events that shall be notified to application

mediaEventsFilter

MediaEventsFilter

O

List of media events that shall be notfied to application

blockingEventTimeoutSec

int

O

Some application responses may block. This timeout specifies how long XCC provider will wait for the response in seconds.

blockingTimeoutHandle

eBlockingTimeoutHandle

O

How XCC provider should handle the call when blocking event timeouts

### RequestXccUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccCallMediaForking

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccCallMediaSetAttributes

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccCallRelease

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccConnectionAddressAnalyze

msgHeader

MsgHeader

M

Message header common for all the messages

action

cConnectionAddressAnalyze

M

Action choice

### ResponseXccConnectionAddressAnalyzeDone

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccConnectionAuthorize

msgHeader

MsgHeader

M

Message header common for all the messages

action

cConnectionAuthorize

M

Action choice

### ResponseXccConnectionAuthorizeDone

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccConnectionMediaForking

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccConnectionRelease

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccControlUpdate

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccProbing

msgHeader

MsgHeader

M

Message header common for all the messages

sequence

int

M

Sequence number of the probing messages

### ResponseXccProviderUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXccRegister

msgHeader

MsgHeader

M

Message header common for all the messages

providerStatus

eProviderStatus

M

Current provider status

### ResponseXccUnRegister

msgHeader

MsgHeader

M

Message header the messages

### SolicitXccConnectionAddressAnalyze

msgHeader

MsgHeader

M

Message header common for all the messages

callData

CallData

M

Call information

connData

ConnData

M

Connection information

collectAddress

AddrData

O

Connection collect address data

### SolicitXccConnectionAuthorize

msgHeader

MsgHeader

M

Message header common for all the messages

callData

CallData

M

Call information

connDetailData

ConnDetailData

M

Connection detail information

### SolicitXccProbing

msgHeader

MsgHeader

M

Message header common for all the messages

sequence

int

M

Sequence number of the probing message

interval

duration

M

Interval between probing messages

failureCount

int

M

Counts on previous probing failures since last successful message exchange in this reigstration session

registered

boolean

M

Registration status

providerStatus

eProviderStatus

M

Provider current status

### SolicitXccProviderUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### Xcc Message Data Types

This section describes the data types and elements that are found in the Xcc Provider messages.

### Xcc Composite Data Type

The following section describes the composite data structures defined within the Xcc Provider.

### AddrData

Referenced by: CallRouteData , ConnDetailData , RedirectAddrData , SolicitXccConnectionAddressAnalyze

type

eAddrType

M

Address data type

addr

string

M

Address in string format

### Alerting

(This is an empty element)

### Block

blockingEventTimeoutSec

int

O

Some application responses may block. This timeout specifies how long XCC provider will wait for the response in seconds.

blockingTimeoutHandle

eBlockingTimeoutHandle

O

How XCC provider should handle the call when blocking event timeouts

### CallData

Referenced by: NotifyXccCallData , NotifyXccConnectionData , SolicitXccConnectionAddressAnalyze , SolicitXccConnectionAuthorize

callID

string

M

Call Identification

state

eCallState

M

call state

### CallDelivery

(This is an empty element)

### CallRouteData

routeAddrData

AddrData

M

terminating party address data

connectionEventsFilter

ConnectionEventsFilter

O

List of connection events shall be enabled for the new terminating connection

### cCallMediaForking

Referenced by: RequestXccCallMediaForking , RequestXccConnectionMediaForking

CallMediaForkingOpt

CallMediaForkingOpt - choice

M

CallMediaForkingOpt

### cConnectionAddressAnalyze

Referenced by: ResponseXccConnectionAddressAnalyze

ConnAddrAnalzOpt

ConnAddrAnalzOpt - choice

M

ConnAddrAnalzOpt

### cConnectionAddressAnalyzeDone

Referenced by: RequestXccConnectionAddressAnalyzeDone

ConnAddrAnalzDoneOpt

ConnAddrAnalzDoneOpt - choice

M

ConnAddrAnalzDoneOpt

### cConnectionAuthorize

Referenced by: ResponseXccConnectionAuthorize

ConnAuthOpt

ConnAuthOpt - choice

M

ConnAuthOpt

### cConnectionAuthorizeDone

Referenced by: RequestXccConnectionAuthorizeDone

ConnAuthDoneOpt

ConnAuthDoneOpt - choice

M

ConnAuthDoneOpt

### cConnectionData

Referenced by: NotifyXccConnectionData

ConnDataOpt

ConnDataOpt - choice

M

ConnDataOpt

### cMediaEvent

Referenced by: NotifyXccCallData

MediaEventOpt

MediaEventOpt - choice

M

MediaEventOpt

### ConnData

Referenced by: ConnDetailData , NotifyXccConnectionData , SolicitXccConnectionAddressAnalyze

connID

string

M

Connection Identification

state

eConnState

M

connection state

### ConnDetailData

Referenced by: Connected , Created , HandoffJoin , SolicitXccConnectionAuthorize

connData

ConnData

M

Connection information

guid

string

M

Connection guid data

guidAltFormat

string

O

Connection guid data represented in Alternate format

callingAddrData

AddrData

O

Calling party address data

origCallingAddrData

AddrData

O

orignal calling party address data

calledAddrData

AddrData

O

Called party address data

origCalledAddrData

AddrData

O

original called party address data

redirectAddrData

RedirectAddrData

O

Redirect party address data

connIntfType

eConnIntfType

O

Connection interface type

mediaData

MediaData

O

Connection media data

connIntf

string

O

Connection interface name string

connDirectionType

eConnDirectionType

M

Connection direction type

routeName

string

O

Connection interface route name string

routeDescription

string

O

Route description

### Connected

connDetailData

ConnDetailData

M

Connection detail information

### ConnectionEventsFilter

Referenced by: CallRouteData , RequestXccControlUpdate , RequestXccRegister

eConnectionEventsFilter

eMediaEventsFilter

O

### ContinueProcessing

(This is an empty element)

### Created

connDetailData

ConnDetailData

M

Connection detail information

### DisableMediaForking

(This is an empty element)

### Disconnected

mediaData

MediaData

M

Connection media data

discCause

int

M

Q.850 disconnect cause range [1 - 188]

statsData

StatsData

O

statistics data

jitterData

JitterData

O

media jitter data

### DTMF

digit

string

M

a dtmf digit

dateTime

string

M

Time when dtmf occurs

### HandoffJoin

connDetailData

ConnDetailData

M

Connection detail information

### HandoffLeave

(This is an empty element)

### JitterData

Referenced by: Disconnected

roundTripDelayMSec

int

M

Round trip delay (in ms)

onTimeRvPlayMSec

int

M

On time Rv Play (in ms)

gapFillWithPredictionMSec

int

M

Prediction count (in ms)

gapFillWithInterpolationMSec

int

M

Interpolation count (in ms)

gapFillWithRedundancyMSec

int

M

Redundancy count (in ms)

lostPacketsCount

int

M

Lost packets count

earlyPacketsCount

int

M

Early packets count

latePacketsCount

int

M

Late packets count

receiveDelayMSec

int

M

Receive delay (in ms)

loWaterPlayoutDelayMSec

int

M

Low water playout delay (in ms)

hiWaterPlayoutDelayMSec

int

M

Hi water playout delay (in ms)

### MediaActivity

old

eActivityState

M

old media activity state

new

eActivityState

M

new media activity state

### MediaAddrData

Referenced by: MediaForkingData

ipv4

string

M

Remote IP Address ver 4

port

int

M

Remote RTP port

recordTone

eCountryType

O

Country specific record tone

### MediaData

Referenced by: ConnDetailData , Disconnected

type

eMediaType

M

Media type

coderType

string

O

codec type

coderByte

int

O

codec byte

### MediaEventsFilter

Referenced by: RequestXccCallMediaSetAttributes , RequestXccControlUpdate , RequestXccControlUpdate

eMediaEventsFilter

MediaEventsFilter

O

### MediaForkingData

Referenced by: RequestXccCallMediaSetAttributes

nearEndAddr

MediaAddrData

M

Media address for near-end side

farEndAddr

MediaAddrData

M

Media address for far-end side

preserve

boolean

O

Media Forking Preservd after app unregister

### MediaForkingEvent

mediaForkingState

eMediaForkingState

M

Media forking status

### ModeChange

old

eMediaType

M

old media type

new

eMediaType

M

new media type

### RedirectAddrData

Referenced by: ConnDetailData , Redirected , Transferred

calledAddrData

AddrData

M

called address data

### Redirected

redirectAddrData

RedirectAddrData

M

Redirect party address data

### Release

discCause

int

M

Q.850 disconnect cause range [1 - 188]

### StatsData

Referenced by: Disconnected

callDuration

duration

M

call duration

TxPacketsCount

int

M

Total Tx Packets

TxBytesCount

int

M

Total Tx Bytes

TxDurationMSec

int

M

Tx Duration in milliseconds

TxVoiceDurationMSec

int

M

Tx Voice Duration in milliseconds

RxPacketsCount

int

M

Total Rx Packets

RxBytesCount

int

M

Total Rx Bytes

RxDurationMSec

int

M

Rx Duration in milliseconds

RxVoiceDurationMSec

int

M

Rx Voice Duration in milliseconds

### Tone

toneType

eToneType

M

Tone type

### Transferred

redirectAddrData

RedirectAddrData

O

Redirect party address data

### Xcc Choice Elements

Choice records - may contain only one field at a time

### CallMediaForkingOpt - choice

Referenced by: cCallMediaForking

Enable media forking Only one of the following elements:

enableMediaForking

MediaForkingData

Enable media forking

disableMediaForking

Empty element

Disable media forking

### ConnAddrAnalzDoneOpt - choice

Referenced by: cConnectionAddressAnalyzeDone

Release the connection Only one of the following elements:

release

Release

Release the connection

continueProcessing

Empty element

Continue the connection processing

callRoute

CallRouteData

Application specifies the call route

### ConnAddrAnalzOpt - choice

Referenced by: cConnectionAddressAnalyze

Temporary block the connection processing and wait for application for further request Only one of the following elements:

block

Block

Temporary block the connection processing and wait for application for further request

release

Release

Release the connection

continueProcessing

Empty element

Continue the connection processing

callRoute

CallRouteData

Application specifies the call route

### ConnAuthDoneOpt - choice

Referenced by: cConnectionAuthorizeDone

Release the connection Only one of the following elements:

release

Release

Release the connection

continueProcessing

Empty element

Continue the connection processing

### ConnAuthOpt - choice

Referenced by: cConnectionAuthorize

Temporary block the connection processing and wait for application for further request Only one of the following elements:

block

Block

Temporary block the connection processing and wait for application for further request

release

Release

Release the connection

continueProcessing

Empty element

Continue the connection processing

### ConnDataOpt - choice

Referenced by: cConnectionData

Enables connection created notify event Only one of the following elements:

created

Created

Enables connection created notify event

callDelivery

Empty element

Enables call delivery notify event

alerting

Empty element

Enables connection alerting notify event

redirected

Redirected

Enables connection redirected notify event

connected

Connected

Enables connection connected notify event

transferred

Transferred

Enables connection transferred notify event

disconnected

Disconnected

Enables connection disconnected notify event

handoffLeave

Empty element

Enables connection handoff leave notify event

handoffJoin

HandoffJoin

Enables connection handoff join notify event

mediaForking

MediaForkingEvent

Updates media forking status

### MediaEventOpt - choice

Referenced by: cMediaEvent

DTMF detected Only one of the following elements:

DTMF

DTMF

DTMF detected

mediaActivity

MediaActivity

Media activity state changed

modeChange

ModeChange

Mode of call changed

tone

Tone

Tone detected

mediaForking

MediaForkingEvent

Updates media forking status

### Xcc Enumerated Elements

This section describes the enumerated elements that are found in the Xcc provider data types and Xcc provider messages.

### eActivityState

Referenced by: MediaActivity

ACTIVE

Active state

INACTIVE

Inactive state

### eAddrType

Referenced by: AddrData

E164

Address is e164 number format

URI

Address is URI string format

OTHER

Address in other formats

### eBlockingTimeoutHandle

Referenced by: Block , RequestXccControlUpdate , RequestXccControlUpdate

###### Value

###### Description

RELEASE

Abort connection attempt

CONTINUE_PROCESSING

Proceed with connection attempt

### eCallState

Referenced by: CallData

IDLE

Initial state of a call. A call has zero connection

ACTIVE

A call has ongoing activity

INVALID

Final state of a call. A call in this state has one or more connections associated with

### eConnDirectionType

Referenced by: ConnDetailData

INCOMING

Incoming connection

OUTGOING

Outgoing connection

### eConnectionEventsFilter

Referenced by: ConnectionEventsFilter

CREATED

First event sent when a new connection is created

AUTHORIZE_CALL

Sent to request call authorization

ADDRESS_ANALYZE

Enables address analyze solicit event

REDIRECTED

Enables connection redirected notify event

ALERTING

Enables connection alerting notify event

CONNECTED

Enables connection connected notify event

TRANSFERRED

Enables connection transferred notify event

CALL_DELIVERY

Enables connection call delivery notify event

DISCONNECTED

Enables connection disconnected notify event

HANDOFFLEAVE

Enables connection handoff leave notify event

HANDOFFJOIN

Enables connection handoff join notify event

### eConnIntfType

Referenced by: ConnDetailData

CONN_UNKNOWN

Unknown connection interface type

CONN_ANALOG_EM

Analog E n M port

CONN_ANALOG_FXO

Analog FXO port

CONN_ANALOG_FXS

Analog FXS port

CONN_ANALOG_EFXS

Analog eFXS port

CONN_ANALOG_EFXO

Analog eFXO port

CONN_ISDN

ISDN PRI interface

CONN_CAS

CAS interfacee

CONN_BRI

ISDN BRI interface

CONN_R2

E1 R2 interface

CONN_H323

H.323 interface

CONN_SIP

SIP interface

CONN_TRUNKGROUP

Trunk group

### eConnState

Referenced by: ConnData

IDLE

Connection is idle state

AUTHORIZE_CALL_ATTEMPT

Connection is in authorize call attempt

ADDRESS_COLLECT

Connection is in collecting address state

ADDRESS_ANALYZE

Connection is pending for address analyze state

CALL_DELIVERY

Connection is in call delivery state

ALERTING

Connection is in alerting state

CONNECTED

Connection is in connected state

DISCONNECTED

Enables connection disconnected notify event

### eCountryType

Referenced by: MediaAddrData

COUNTRY_USA

United States

COUNTRY_AUSTRALIA

Australia

COUNTRY_GERMANY

Germany

COUNTRY_RUSSIA

Russia

COUNTRY_SPAIN

Spain

COUNTRY_SWITZERLAND

Switzerland

### eMediaEventsFilter

Referenced by: MediaEventsFilter MediaEventsFilter

DTMF

Enables inband dtmf detection

MEDIA_ACTIVITY

Enables media activity detection

MODE_CHANGE

Enables mode change notify when a mode of a call session has changed

TONE_BUSY

Enables busy tone detection

TONE_DIAL

Enables dialtone detection

TONE_OUT_OF_SERVICE

Enable out of service tone detection

TONE_RINGBACK

Enables ringback detection

TONE_SECOND_DIAL

Enables secondary dialtone detection

### eMediaForkingState

Referenced by: MediaForkingEvent

FORK_STARTED

Media forking setup success

FORK_FAILED

Media forking setup failure

FORK_DONE

Media forking completed

### eMediaType

Referenced by: MediaData , ModeChange

VOICE

Voice call

FAX

Fax call

MODEM

Modem call

VIDEO

Video call

DATA

Data call

### eToneType

Referenced by: Tone

TONE_BUSY

busy tone detected

TONE_DIAL

dialtone detected

TONE_RINGBACK

ringback detected

TONE_SECOND_DIAL

secondary dialtone detected

TONE_OUT_OF_SERVICE

out of service detected

## XSVC

### Xsvc Provider Operations

The XSVC provider monitors the trunk status, and provides real-time notification of link status and configuration change to application.

XsvcRegister

inOut

RequestXsvcRegister

ResponseXsvcRegister

fault:

XMLParserError

fault:

ServiceException

Allows application to register with XSVC provider and specify the connection events filter

XsvcUnRegister

inOut

RequestXsvcUnRegister

ResponseXsvcUnRegister

fault:

XMLParserError

fault:

ServiceException

Allows application to unregister with XSVC provider

XsvcProviderUnRegister

outIn

ResponseXsvcProviderUnRegister

SolicitXsvcProviderUnRegister

Allows XSVC provider to unregister with application.

XsvcProviderStatus

outOnly

NotifyXsvcProviderStatus

Updates application once the XSVC provider status has changed

XsvcRouteSetFilter

inOut

RequestXsvcRouteSetFilter

ResponseXsvcRouteSetFilter

fault:

XMLParserError

fault:

ServiceException

Allows the application to set the fitler so that XSVC provider will only report to the application the updates it is interested in

XsvcRouteSnapshot

inOut

RequestXsvcRouteSnapshot

ResponseXsvcRouteSnapshot

fault:

XMLParserError

fault:

ServiceException

Allows application to get the big picture of all the routes being monitored.

XsvcRouteStats

inOut

RequestXsvcRouteStats

ResponseXsvcRouteStats

fault:

XMLParserError

fault:

ServiceException

Allows application to query the statistics of a trunk

XsvcRouteData

inOut

RequestXsvcRouteData

ResponseXsvcRouteData

fault:

XMLParserError

fault:

ServiceException

Allows application to query the detail information of a trunk

XsvcRouteConfiguration

outOnly

NotifyXsvcRouteConfiguration

Notifies application that a trunk configuration is changed

XsvcRouteStatus

outOnly

NotifyXsvcRouteStatus

Notifies application that a trunk status is change:

Link status is changed

Alarm status is changed

XsvcProbing

outIn

ResponseXsvcProbing

SolicitXsvcProbing

Allows XSVC provider to keep alive a registration session and probe its health.

### Xsvc API Messages

### NotifyXsvcProviderStatus

msgHeader

MsgHeader

M

Message header common for all the messages

applicationData

ApplicationData

M

Application URL configured in router CLI

providerData

ProviderData

M

Provider data

providerStatus

eProviderStatus

M

Provider current status

### NotifyXsvcRouteConfiguration

msgHeader

MsgHeader

M

Message header common for all the messages

type

eRouteChangeType

M

routeList

RouteList

M

Compact form of route information

### NotifyXsvcRouteStatus

msgHeader

MsgHeader

M

Message header common for all the messages

routeList

RouteList

M

Compact form of route information

### RequestXsvcRegister

msgHeader

MsgHeader

M

Message header common for all the messages

applicationData

ApplicationData

M

Application sends this request

providerData

ProviderData

M

XSVC provider

routeEventsFilter

RouteEventsFilter

O

List of events that shall be notified to application

### RequestXsvcRouteData

msgHeader

MsgHeader

M

Message header common for all the messages

routeName

string

M

Route name

routeType

eRouteType

M

Route type

### RequestXsvcRouteSetFilter

msgHeader

MsgHeader

M

Message header common for all the messages

isOn

boolean

M

routeFilterList

RouteFilterList

O

Route filter list

### RequestXsvcRouteSnapshot

msgHeader

MsgHeader

M

Message header common for all the messages

### RequestXsvcRouteStats

msgHeader

MsgHeader

M

Message header common for all the messages

routeName

string

M

Route name

routeType

eRouteType

M

Route type

### RequestXsvcUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXsvcProbing

msgHeader

MsgHeader

M

Message header common for all the messages

sequence

int

M

Sequence number of the probing messages

### ResponseXsvcProviderUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXsvcRegister

msgHeader

MsgHeader

M

Message header common for all the messages

providerStatus

eProviderStatus

M

Current providerstatus

### ResponseXsvcRouteData

msgHeader

MsgHeader

M

Message header common for all the messages

routeList

RouteList

M

Compact form of route information

### ResponseXsvcRouteSetFilter

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXsvcRouteSnapshot

msgHeader

MsgHeader

M

Message header common for all the messages

routeList

RouteList

M

Compact form of route information

### ResponseXsvcRouteStats

msgHeader

MsgHeader

M

Message header common for all the messages

routeList

RouteList

M

Compact form of route information

### ResponseXsvcUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### SolicitXsvcProbing

msgHeader

MsgHeader

M

Message header common for all the messages

sequence

int

M

Sequence number of the probing message

interval

duration

M

Interval between probing messages

failureCount

int

M

Counts on previous probing failures since last successful message exchange in this reigstration session

registered

boolean

M

Registration status

providerStatus

eProviderStatus

M

Provider current status

### SolicitXsvcProviderUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### Xsvc Message Data Types

This section describes the data types and elements that are found in the Xsvc Provider messages.

### Xsvc Composite Data Type

The following section describes the composite data structures defined within the Xsvc Provider.

### CurrentStatistics

Referenced by: IntfStatisticsData

elapsedTime

duration

M

The time have elapsed since the beginning of the far end current error-measurement period

LCV

int

M

Line Coding Violation Error Event

PCV

int

M

Path Coding Violation Error Event

CSS

int

M

Controlled Slip Seconds

SEFS

int

M

Severely Errored Framing Second

LES

int

M

Line Errored Seconds

DM

int

M

Degraded Minutes

ES

int

M

Errored Seconds

BES

int

M

Bursty Errored Seconds

SES

int

M

everely Errored Seconds

UAS

int

M

Unavailable Seconds

### IntfChannels

Referenced by: TrunkData

channels

string

O

Channel mapping of the interface

totalChannels

int

M

Total channels on the interface

### IntfStatisticsData

Referenced by: TrunkData

currentStatistics

CurrentStatistics

M

Interface latest statistics

totalStatistics

TotalStatistics

M

Interface accumulated statistics

### RouteData

Referenced by: RouteList

routeName

string

M

Route name

routeType

eRouteType

M

Route type

routeDescription

string

O

Route description

trunkList

TrunkList

O

### RouteEventsFilter

Referenced by: RequestXsvcRegister

eRouteEventsFilter

eRouteEventsFilter

O

### RouteFilter

Referenced by: RouteFilterList

routeName

string

M

Route name

routeType

eRouteType

M

Route type

### RouteFilterList

Referenced by: RequestXsvcRouteSetFilter

routeFilter

RouteFilter

O

Route filter

### RouteList

Referenced by: NotifyXsvcRouteConfiguration , NotifyXsvcRouteStatus , ResponseXsvcRouteData , ResponseXsvcRouteSnapshot , ResponseXsvcRouteStats

route

RouteData

M

### TotalStatistics

Referenced by: IntfStatisticsData

intervalTime

duration

M

The time of previous far end intervals for which data was collected

LCV

int

M

Line Coding Violation Error Event

PCV

int

M

Path Coding Violation Error Event

CSS

int

M

Controlled Slip Seconds

SEFS

int

M

Severely Errored Framing Second

LES

int

M

Line Errored Seconds

DM

int

M

Degraded Minutes

ES

int

M

Errored Seconds

BES

int

M

Bursty Errored Seconds

SES

int

M

everely Errored Seconds

UAS

int

M

Unavailable Seconds

### TrunkData

Referenced by: TrunkList

List of one or more connection events

name

string

M

Name of the turnk interface

type

eTrunkType

M

Type of the turnk interface

status

eTrunkStatus

M

Status of the turnk interface

channelData

IntfChannels

O

Trunk interface channel information

alarmData

eTrunkAlarm

O

Trunk interface alarm information

statisticsData

IntfStatisticsData

O

Trunk interface statistics information

### TrunkList

Referenced by: RouteData

trunkData

TrunkData

M

### Xsvc Enumerated Elements

This section describes the enumerated elements that are found in the Xsvc provider data types and Xsvc provider messages.

### eRouteChangeType

Referenced by: NotifyXsvcRouteConfiguration

ROUTE_ADDED

ROUTE_DELETED

ROUTE_MODIFIED

### eRouteEventsFilter

Referenced by: RouteEventsFilter

ROUTE_CONF_UPDATED

Enables route configuration updated notify event

ROUTE_STATUS_UPDATED

Enables route status updated notify event)

### eRouteType

Referenced by: RequestXsvcRouteData , RequestXsvcRouteStats , RouteData , RouteFilter

VOIP

PSTN

### eTrunkAlarm

Referenced by: TrunkData

NoAlarm

No alarm present

RcvFarEndLOF

Far end LOF (a.k.a. Yellow Alarm)

XmtFarEndLOF

Near end sending LOF Indication

RcvAIS

Far end sending AIS

XmtAIS

Near end sending AIS

LossOfFrame

Near end LOF (a.k.a. Red Alarm)

LossOfSignal

Near end loss Of Signal

LoopbackState

Near end is looped

T16AIS

E1 TS16 AIS

RcvFarEndOLMF

Far End Send TS16 LOMF

XmtFarEndOLMF

Near End Send TS16 LOMF

RcvTestCode

Near End detects a test code

OtherFailure

any line status not defined here

UnavailSigState

Near End in Unavailable Signal State

NetEquipOOS

Carrier Equipment Our Of Service

RcvPayloadAIS

DS2 Payload AIS

Ds2PerfThreshold

DS2 Performance Threshold

### eTrunkStatus

Referenced by: TrunkData

UP

-

DOWN

-

### eTrunkType

Referenced by: TrunkData

ISDN_PRI

-

ISDN_BRI

-

ANALOG

-

CAS

-

SIPV2

-

H323

-

## XCDR

### Xcdr Provider Operations

The XCDR provider provides CDR information for the application. It notifies the application when calls are set up or ended.

XcdrRegister

inOut

RequestXcdrRegister

ResponseXcdrRegister

fault:

XMLParserError

fault:

ServiceException

Allows application to register with XCDR provider and specify the connection events filter

XcdrUnRegister

inOut

RequestXcdrUnRegister

ResponseXcdrUnRegister

fault:

XMLParserError

fault:

ServiceException

Allows application to unregister with XCDR provider

XcdrProviderUnRegister

outIn

ResponseXcdrProviderUnRegister

SolicitXcdrProviderUnRegister

Allows XCDR provider to unregister with application.

XcdrProviderStatus

outOnly

NotifyXcdrProviderStatus

Updates application once the XCDR provider status has changed

XcdrSetAttribute

inOut

RequestXcdrSetAttribute

ResponseXcdrSetAttribute

Allows application to specify the attribute it is needed. Two formats, compact or detailed, can be selected.

XcdrRecord

outOnly

NotifyXcdrRecord

Notifies application the CDR

XcdrProbing

outIn

ResponseXcdrProbing

SolicitXcdrProbing

Allows XCDR provider to keep alive a registration session and probe its health.

### Xcdr API Messages

### NotifyXcdrProviderStatus

msgHeader

MsgHeader

M

Message header common for all the messages

applicationData

ApplicationData

M

Application URL configured in router CLI

providerData

ProviderData

M

Provider data

providerStatus

eProviderStatus

M

Provider current status

### NotifyXcdrRecord

msgHeader

MsgHeader

M

Message header common for all the messages

format

eCdrFormat

M

CDR format

type

eCdrType

M

CDR type

cdr

string

M

CDR information

### RequestXcdrRegister

msgHeader

MsgHeader

M

Message header common for all the messages

applicationData

ApplicationData

M

Application send s this request

providerData

ProviderData

M

XCDR provider

cdrEventsFilter

CdrEventsFilter

O

List of events that shall be notified to application

### RequestXcdrSetAttribute

msgHeader

MsgHeader

M

Message header common for all the messages

format

eCdrFormat

M

CDR format

### RequestXcdrUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXcdrProbing

msgHeader

MsgHeader

M

Message header common for all the messages

sequence

int

M

Sequence number of the probing messages

### ResponseXcdrProviderUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXcdrRegister

msgHeader

MsgHeader

M

Message header common for all the messages

providerStatus

eProviderStatus

M

Current providerstatus

### ResponseXcdrSetAttribute

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXcdrUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### SolicitXcdrProbing

msgHeader

MsgHeader

M

Message header common for all the messages

sequence

int

M

Sequence number of the probing message

interval

duration

M

Interval between probing messages

failureCount

int

M

Counts on previous probing failures since last successful message exchange in this registration session

registered

boolean

M

Registration status

providerStatus

eProviderStatus

M

Provider current status

### SolicitXcdrProviderUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### Xcdr Message Data Types

This section describes the data types and elements that are found in the Xcdr Provider messages.

### Xcdr Composite Data Type

The following section describes the composite data structures defined within the Xcdr Provider.

### CdrEventsFilter

Referenced by: RequestXcdrRegister

list of one or more CDR events

eCdrEventsFilter

eCdrEventsFilter

O

### Xcdr Enumerated Elements

This section describes the enumerated elements that are found in the Xcdr provider data types and Xcdr provider messages.

### eCdrEventsFilter

Referenced by: CdrEventsFilter

CDR_RECORD

Enables CDR record notify event

### eCdrFormat

Referenced by: NotifyXcdrRecord , RequestXcdrSetAttribute

COMPACT

Displaying CDR in compact format

DETAIL

Displaying CDR in detail format

### eCdrType

Referenced by: NotifyXcdrRecord

START

CDR when call are set up

STOP

CDR when call are released

## XMF

### Xmf Provider Operations

The XMF (Extended Media Forking) provider supports operations that allow a client application to perform media forking and real-time call monitoring.

XmfRegister

inOut

RequestXmfRegister

ResponseXmfRegister

fault:

XMLParserError

fault:

ServiceException

Allows application to register with XMF provider and specify the connection events filter

XmfUnRegister

inOut

RequestXmfUnRegister

ResponseXmfUnRegister

fault:

XMLParserError

fault:

ServiceException

Allows application to unregister with XMF provider

XmfControlUpdate

inOut

RequestXmfControlUpdate

ResponseXmfControlUpdate

fault:

XMLParserError

fault:

ServiceException

Allows application to update parameters after registered

XmfProviderUnRegister

outIn

ResponseXmfProviderUnRegister

SolicitXmfProviderUnRegister

Allows XMF provider to unregister with application

XmfProviderStatus

outOnly

NotifyXmfProviderStatus

Updates application once the XMF provider status has changed

XmfCallMediaSetAttributes

inOut

RequestXmfCallMediaSetAttributes

ResponseXmfCallMediaSetAttributes

fault:

XMLParserError

fault:

ServiceException

Allows application to specify the media attributes for the call session

XmfCallMediaForking

inOut

RequestXmfCallMediaForking

ResponseXmfCallMediaForking

fault:

XMLParserError

fault:

ServiceException

Allows application to enable media forking for the call session

XmfConnectionMediaForking

inOut

RequestXmfConnectionMediaForking

ResponseXmfConnectionMediaForking

fault:

XMLParserError

fault:

ServiceException

Allows application to enable media forking for the connection

XmfCallData

outOnly

NotifyXmfCallData

Notifies application that a call session on one of the following conditions:

- mode is changed

- a dtmf digit is detected

- media inactive or active is detected

XmfConnectionData

outOnly

NotifyXmfConnectionData

Notifies application that a connection is in one of the following conditions:

a new connection is created

a connection is in call delivery state

a connection is redirected to another destination

a connection is in alerting state

a conection is in connected state

a connection is transferred to another target

a connection is in disconnected state

a connection is handoff and leave the call session

a connection is handoff to the call session

XmfProbing

outIn

ResponseXmfProbing

SolicitXmfProbing

Allows XMF provider to keep alive a registration session and probe its health

### Xmf API Messages

### NotifyXmfCallData

msgHeader

MsgHeader

M

Message header common for all the messages

callData

CallData

M

call information

mediaEvent

cMediaEvent

M

Choice of media event

### NotifyXmfConnectionData

msgHeader

MsgHeader

M

Message header common for all the messages

callData

CallData

M

Call information

connData

ConnData

M

Connection information

event

cConnectionData

M

Event choice

### NotifyXmfProviderStatus

msgHeader

MsgHeader

M

Message header common for all the messages

applicationData

ApplicationData

M

Application URL configured in router CLI

providerData

ProviderData

M

Provider data

providerStatus

eProviderStatus

M

Provider current status

### RequestXmfCallMediaForking

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call Identification

action

cCallMediaForking

M

Media forking action choice

### RequestXmfCallMediaSetAttributes

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call Identification

mediaEventsFilter

MediaEventsFilter

O

Enables media event types to be sent to application. Turn off any media events if this element is not included in the request

mediaForking

MediaForkingData

O

Media forkig data

### RequestXmfConnectionMediaForking

msgHeader

MsgHeader

M

Message header common for all the messages

callID

string

M

Call Identification

connID

string

M

Connection Identification

action

cCallMediaForking

M

Media forking action choice

### RequestXmfControlUpdate

msgHeader

MsgHeader

M

Message header common for all the messages

connectionEventsFilter

ConnectionEventsFilter

O

List of events that shall be notified to application

mediaEventsFilter

MediaEventsFilter

O

List of media events that shall be notfied to application

### RequestXmfRegister

msgHeader

MsgHeader

M

Message header common for all the messages

applicationData

ApplicationData

M

Application sends this request

providerData

ProviderData

M

XMF provider

connectionEventsFilter

ConnectionEventsFilter

O

List of events that shall be notified to application

mediaEventsFilter

MediaEventsFilter

O

List of media events that shall be notfied to application

### RequestXmfUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXmfCallMediaForking

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXmfCallMediaSetAttributes

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXmfConnectionMediaForking

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXmfControlUpdate

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXmfProbing

msgHeader

MsgHeader

M

Message header common for all the messages

sequence

int

M

Sequence number of the probing messages

### ResponseXmfProviderUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### ResponseXmfRegister

msgHeader

MsgHeader

M

Message header common for all the messages

providerStatus

eProviderStatus

M

Current provider status

### ResponseXmfUnRegister

msgHeader

MsgHeader

M

Message header the messages

### SolicitXmfProbing

msgHeader

MsgHeader

M

Message header common for all the messages

sequence

int

M

Sequence number of the probing message

interval

duration

M

Interval between probing messages

failureCount

int

M

Counts on previous probing failures since last successful message exchange in this reigstration session

registered

boolean

M

Registration status

providerStatus

eProviderStatus

M

Provider current status

### SolicitXmfProviderUnRegister

msgHeader

MsgHeader

M

Message header common for all the messages

### Xmf Message Data Types

This section describes the data types and elements that are found in the Xmf Provider messages.

### Xmf Composite Data Type

The following section describes the composite data structures defined within the Xmf Provider.

### AddrData

Referenced by: ConnDetailData , RedirectAddrData

type

eAddrType

M

Address data type

addr

string

M

Address in string format

### Alerting

(This is an empty element)

### CallData

Referenced by: NotifyXmfCallData , NotifyXmfConnectionData

callID

string

M

Call Identification

state

eCallState

M

call state

### CallDelivery

(This is an empty element)

### cCallMediaForking

Referenced by: RequestXmfCallMediaForking , RequestXmfConnectionMediaForking

CallMediaForkingOpt

CallMediaForkingOpt - choice

M

CallMediaForkingOpt

### cConnectionData

Referenced by: NotifyXmfConnectionData

ConnDataOpt

ConnDataOpt - choice

M

ConnDataOpt

### cMediaEvent

Referenced by: NotifyXmfCallData

MediaEventOpt

MediaEventOpt - choice

M

MediaEventOpt

### ConnData

Referenced by: ConnDetailData , NotifyXmfConnectionData

connID

string

M

Connection Identification

state

eConnState

M

connection state

### ConnDetailData

Referenced by: Connected , Created , HandoffJoin

connData

ConnData

M

Connection information

guid

string

M

Connection guid data

guidAltFormat

string

O

Connection guid data represented in Alternate format

callingAddrData

AddrData

O

Calling party address data

origCallingAddrData

AddrData

O

orignal calling party address data

calledAddrData

AddrData

O

Called party address data

origCalledAddrData

AddrData

O

original called party address data

redirectAddrData

RedirectAddrData

O

Redirect party address data

connIntfType

eConnIntfType

O

Connection interface type

mediaData

MediaData

O

Connection media data

connIntf

string

O

Connection interface name string

connDirectionType

eConnDirectionType

M

Connection direction type

routeName

string

O

Connection interface route name string

routeDescription

string

O

Route description

### Connected

connDetailData

ConnDetailData

M

Connection detail information

### ConnectionEventsFilter

Referenced by: RequestXmfControlUpdate , RequestXmfRegister

eConnectionEventsFilter

eConnectionEventsFilter

O

### Created

connDetailData

ConnDetailData

M

Connection detail information

### DisableMediaForking

(This is an empty element)

### Disconnected

mediaData

MediaData

M

Connection media data

discCause

int

M

Q.850 disconnect cause range [1 - 188]

statsData

StatsData

O

statistics data

jitterData

JitterData

O

media jitter data

### DTMF

digit

string

M

a dtmf digit

dateTime

string

M

Time when dtmf occurs

### HandoffJoin

connDetailData

ConnDetailData

M

Connection detail information

### HandoffLeave

(This is an empty element)

### JitterData

Referenced by: Disconnected

roundTripDelayMSec

int

M

Round trip delay (in ms)

onTimeRvPlayMSec

int

M

On time Rv Play (in ms)

gapFillWithPredictionMSec

int

M

Prediction count (in ms)

gapFillWithInterpolationMSec

int

M

Interpolation count (in ms)

gapFillWithRedundancyMSec

int

M

Redundancy count (in ms)

lostPacketsCount

int

M

Lost packets count

earlyPacketsCount

int

M

Early packets count

latePacketsCount

int

M

Late packets count

receiveDelayMSec

int

M

Receive delay (in ms)

loWaterPlayoutDelayMSec

int

M

Low water playout delay (in ms)

hiWaterPlayoutDelayMSec

int

M

Hi water playout delay (in ms)

### MediaActivity

old

eActivityState

M

old media activity state

new

eActivityState

M

new media activity state

### MediaAddrData

Referenced by: MediaForkingData

ipv4

string

M

Remote IP Address ver 4

port

int

M

Remote RTP port

recordTone

eCountryType

O

Country specific record Tone

### MediaData

Referenced by: ConnDetailData , Disconnected

type

eMediaType

M

Media type

coderType

string

O

codec type

coderByte

int

O

codec byte

### MediaEventsFilter

Referenced by: RequestXmfCallMediaSetAttributes , RequestXmfControlUpdate , RequestXmfRegister

eMediaEventsFilter

eMediaEventsFilter

O

### MediaForkingData

Referenced by: RequestXmfCallMediaSetAttributes

nearEndAddr

MediaAddrData

M

Media address for near-end side

farEndAddr

MediaAddrData

M

Media address for far-end side

preserve

boolean

O

Media Forking Preservd after app unregister

### MediaForkingEvent

mediaForkingState

eMediaForkingState

M

Media forking status

### ModeChange

old

eMediaType

M

old media type

new

eMediaType

M

new media type

### RedirectAddrData

Referenced by: : ConnDetailData , Redirected , Transferred

calledAddrData

AddrData

M

called address data

### Redirected

redirectAddrData

RedirectAddrData

M

Redirect party address data

### StatsData

Referenced by: Disconnected

callDuration

duration

M

call duration

TxPacketsCount

int

M

Total Tx Packets

TxBytesCount

int

M

Total Tx Bytes

TxDurationMSec

int

M

Tx Duration in milliseconds

TxVoiceDurationMSec

int

M

Tx Voice Duration in milliseconds

RxPacketsCount

int

M

Total Rx Packets

RxBytesCount

int

M

Total Rx Bytes

RxDurationMSec

int

M

Rx Duration in milliseconds

RxVoiceDurationMSec

int

M

Rx Voice Duration in milliseconds

### Tone

toneType

eToneType

M

Tone type

### Transferred

redirectAddrData

RedirectAddrData

O

Redirect party address data

### Xmf Choice Elements

Choice records - may contain only one field at a time

### CallMediaForkingOpt - choice

Referenced by: cCallMediaForking

Enable media forking Only one of the following elements:

enableMediaForking

MediaForkingData

Enable media forking

disableMediaForking

Empty element

Disable media forking

### ConnDataOpt - choice

Referenced by: cConnectionData

Enables connection created notify event Only one of the following elements:

created

Created

Enables connection created notify event

callDelivery

Empty element

Enables call delivery notify event

alerting

Empty element

Enables connection alerting notify event

redirected

Redirected

Enables connection redirected notify event

connected

Connected

Enables connection connected notify event

transferred

Transferred

Enables connection transferred notify event

disconnected

Disconnected

Enables connection disconnected notify event

handoffLeave

Empty element

Enables connection handoff leave notify event

handoffJoin

HandoffJoin

Enables connection handoff join notify event

mediaForking

MediaForkingEvent

Updates media forking status

### MediaEventOpt - choice

Referenced by: cMediaEvent

DTMF detected Only one of the following elements:

DTMF

DTMF

DTMF detected

mediaActivity

MediaActivity

Media activity state changed

modeChange

ModeChange

Mode of call changed

tone

Tone

Tone detected

mediaForking

MediaForkingData

Updates media forking status

### Xmf Enumerated Elements

This section describes the enumerated elements that are found in the Xmf provider data types and Xmf provider messages.

### eActivityState

Referenced by: MediaActivity

ACTIVE

Active state

INACTIVE

Inactive state

### eAddrType

Referenced by: AddrData

E164

Address is e164 number format

URI

Address is URI string format

OTHER

Address in other formats

### eCallState

Referenced by: CallData

IDLE

Initial state of a call. A call has zero connection

ACTIVE

A call has ongoing activity

INVALID

Final state of a call. A call in this state has one or more connections associated with

### eConnDirectionType

Referenced by: ConnDetailData

INCOMING

Incoming connection

OUTGOING

Outgoing connection

### eConnectionEventsFilter

Referenced by: ConnectionEventsFilter

CREATED

First event sent when a new connection is created

REDIRECTED

Enables connection redirected notify event

ALERTING

Enables connection alerting notify event

CONNECTED

Enables connection connected notify event

TRANSFERRED

Enables connection transferred notify event

CALL_DELIVERY

Enables connection call delivery notify event

DISCONNECTED

Enables connection disconnected notify event

HANDOFFLEAVE

Enables connection handoff leave notify event

HANDOFFJOIN

Enables connection handoff join notify event

### eConnIntfType

Referenced by: ConnDetailData

CONN_UNKNOWN

Unknown connection interface type

CONN_ANALOG_EM

Analog E n M port

CONN_ANALOG_FXO

Analog FXO port

CONN_ANALOG_FXS

Analog FXS port

CONN_ANALOG_EFXS

Analog eFXS port

CONN_ANALOG_EFXO

Analog eFXO port

CONN_ISDN

ISDN PRI interface

CONN_CAS

CAS interfacee

CONN_BRI

ISDN BRI interface

CONN_R2

E1 R2 interface

CONN_H323

H.323 interface

CONN_SIP

SIP interface

CONN_TRUNKGROUP

Trunk group

### eConnState

Referenced by: ConnData

IDLE

Connection is idle state

AUTHORIZE_CALL_ATTEMPT

Connection is in authorize call attempt

ADDRESS_COLLECT

Connection is in collecting address state

ADDRESS_ANALYZE

Connection is pending for address analyze state

CALL_DELIVERY

Connection is in call delivery state

ALERTING

Connection is in alerting state

CONNECTED

Connection is in connected state

DISCONNECTED

Enables connection disconnected notify event

### eCountryType

Referenced by: MediaAddrData

COUNTRY_USA

United States

COUNTRY_AUSTRALIA

Australia

COUNTRY_GERMANY

Germany

COUNTRY_RUSSIA

Russia

COUNTRY_SPAIN

Spain

COUNTRY_SWITZERLAND

Switzerland

### eMediaEventsFilter

Referenced by: MediaEventsFilter

DTMF

Enables inband dtmf detection

MEDIA_ACTIVITY

Enables media activity detection

MODE_CHANGE

Enables mode change notify when a mode of a call session has changed

TONE_BUSY

Enables busy tone detection

TONE_DIAL

Enables dialtone detection

TONE_OUT_OF_SERVICE

Enable out of service tone detection

TONE_RINGBACK

Enables ringback detection

TONE_SECOND_DIAL

Enables secondary dialtone detection

### eMediaForkingState

Referenced by: MediaForkingEvent

FORK_STARTED

Media forking setup success

FORK_FAILED

Media forking setup failure

FORK_DONE

Media forking completed

### eMediaType

Referenced by: MediaData , ModeChange

VOICE

Voice call

FAX

Fax call

MODEM

Modem call

VIDEO

Video call

DATA

Data call

### eToneType

Referenced by: Tone

TONE_BUSY

busy tone detected

TONE_DIAL

dialtone detected

TONE_RINGBACK

ringback detected

TONE_SECOND_DIAL

secondary dialtone detected

TONE_OUT_OF_SERVICE

out of service detected

### Common Message Data Types

This section describes the data types and elements that are found in the Common Module messages.

### Common Composite Data Type

The following section describes the composite data structures defined within the Common Module.

### ApplicationData

url

anyURI

M

Application url data

name

string

O

Application name

### MsgHeader

transactionID

string

O

ID to identify a transaction for the message excahnge between provider and application. This filed is optional. This field is mandatory for the response message to return the same transactionID if present in the request/solicit message.

registrationID

string

O

ID to identify a registration session. This field is absent for RequestRegister and NotifyStatus messages. This field is mandatory for all the other messages.

### ProviderData

url

anyURI

M

url for client application

### Common Enumerated Elements

This section describes the enumerated elements that are found in the Common Module data types.

### eProviderStatus

SHUTDOWN

Service is not running

IN_SERVICE

Service is enabled and running

## Common Module

### Common Message Data Types

This section describes the data types and elements that are found in the Common Module messages.

### Common Composite Data Type

The following section describes the composite data structures defined within the Common Module.

### ApplicationData

url

anyURI

M

Application url data

name

string

O

Application name

### MsgHeader

transactionID

string

O

ID to identify a transaction for the message excahnge between provider and application. This filed is optional. This field is mandatory for the response message to return the same transactionID if present in the request/solicit message.

registrationID

string

O

ID to identify a registration session. This field is absent for RequestRegister and NotifyStatus messages. This field is mandatory for all the other messages.

### ProviderData

url

anyURI

M

url for client application

### Common Enumerated Elements

This section describes the enumerated elements that are found in the Common Module data types.

### eProviderStatus

SHUTDOWN

Service is not running

IN_SERVICE

Service is enabled and running

### Common XML Types

The following types are defined by XML:

any

http://www.w3.org/TR/xmlschema-2/#any

anyURI

http://www.w3.org/TR/xmlschema-2/#anyURI

boolean

http://www.w3.org/TR/xmlschema-2/#boolean

dateTime

http://www.w3.org/TR/xmlschema-2/#dateTime

duration

http://www.w3.org/TR/xmlschema-2/#duration

int

http://www.w3.org/TR/xmlschema-2/#int

name

http://www.w3.org/TR/xmlschema-2/#Name

string

http://www.w3.org/TR/xmlschema-2/#string

## Fault Module

### Fault Message Data Types

This section describes the data types and elements that are found in the Fault Module messages.

### Fault Composite Data Type

The following section describes the composite data structures defined within the Fault Module.

### ServiceException

The service exception fault bound to SOAP fault elements are listed:

Soap:Code/Value

string

M

The value is "Receiver"

Soap:Code/Subcode/Value

string

O

The value is "SERVICE EXCEPTION"

Soap:Reason/Text

string

M

Information on the nature of the fault

Soap:Detail

ServiceException

O

Details of the service exception.

The elemenet ServiceException is defined as:

errorCode

string

M

Error identifier with service prefix and number.

operation

string

O

Service opertion of the message

transactionID

string

O

transactionID if present in the request.

registrationID

string

O

registrationID if present in the request.

text

string

O

Message text

### XMLParserError

When the SOAP message contains syntax error, the XML parser will fail, and a SOAP fault message will be generated. The XML parser error fault bound to SOAP fault elements are listed:

Soap:Code/Value

string

M

The value is "Sender" or "Receiver"

Soap:Code/Subcode/Value

string

M

The value is "XML PARSER ERROR"

Soap:Reason/Text

string

M

Information on the nature of the fault as follows:

Memory exhausted

Badly framed XML received

Unknown namespace received

A required attribute is missing

An uninterpretable attribute has been received

An invalidattribute value has been received

An unknown XML tag has been received

Anexpected XML tag or sequence is missing

An unexpected XML tag has been received

The value for an XML tag is not valid

An internal error caused processing to be aborted

An unsupported operation request has been received

Soap:Detail

XMLParserError

O

Details of the XML parser error.

The elemenet XMLParserError is defined as:

errorXMLDetail

string

O

Information to identify where is the parsing error in the XML message

errorXMLMsg

any

O

A copy of the original XML message for debugging purpose.

errorXMLTag

string

O

XML tag which causes the failure

### Fault XML Types

The following types are defined by XML:

any

http://www.w3.org/TR/xmlschema-2/#any

anyURI

http://www.w3.org/TR/xmlschema-2/#anyURI

boolean

http://www.w3.org/TR/xmlschema-2/#boolean

dateTime

http://www.w3.org/TR/xmlschema-2/#dateTime

duration

http://www.w3.org/TR/xmlschema-2/#duration

int

http://www.w3.org/TR/xmlschema-2/#int

name

http://www.w3.org/TR/xmlschema-2/#Name

string

http://www.w3.org/TR/xmlschema-2/#string

| Provide Operation | Direction | Incoming Message | Outgoing Message | Description |
|---|---|---|---|---|
| XccRegister | inOut | RequestXccRegister | ResponseXccRegister fault: XMLParserError fault: ServiceException | Allows application to register with XCC provider and specify the connection events filter |
| XccUnRegister | inOut | RequestXccUnRegister | ResponseXmfUnRegister fault: XMLParserError fault: ServiceException | Allows application to unregister with XCC provider |
| XccControlUpdate | inOut | RequestXccControlUpdate | ResponseXccControlUpdate fault: XMLParserError fault: ServiceException | Allows application to update parameters after registered |
| XccCallRelease | inOut | RequestXccCallRelease | ResponseXccCallRelease fault: XMLParserError fault: ServiceException | Allows application to release the call session |
| XccConnectionRelease | inOut | RequestXccConnectionRelease | ResponseXccConnectionRelease fault: XMLParserError fault: ServiceException | Allows application to release the connection from the call session |
| XccProviderUnregister | outIn | ResponseXccProviderUnRegister | SolicitXccProviderUnRegister | Allows XCC Provider to unregister with application |
| XccProviderStatus | OutOnly |  | NotifyXccProviderStatus | Updated application once XCC provider |
| XccCallMediaSetAttributes | inOut | RequestXccCallMediaSetAttributes | ResponseXccCallMediaSetAttributes | Allows application to specify the media attributes for a call session |
| XccCallMediaForking | inOut | RequestXccCallMediaForking | ResponseXccCallMediaForking fault: XMLParserError fault: ServiceException | Allows application to enable media forking a call session |
| XccCallData | outOnly |  | NotifyXccCallData | Notifies application that a call session on one of the following conditions: mode is changed a dtmf digit is detected media inactive or active is detected |
| XccConnectionAuthorize | outIn | ResponseXccConnectionAuthorize | SolicitXccConnectionAuthorize | Allows application to perform the connection authorization |
| XccConnectionAuthorizeDone | inOut | RequestXccConnectionAuthorizeDone | ResponseXccConnectionAuthorizeDone fault: XMLParserError fault: ServiceException | Allows application to handle the connection once the authorization is done |
| XccConnectionAddressAnalyze | outIn | ResponseXccConnectionAddressAnalyze | SolicitXccConnectionAddressAnalyze | Allows application to analyze the connection address |
| XccConnectionAddressAnalyzeDonr | inOut | RequestXccConnectionAddressAnalyzeDone | ResponseXccConnectionAddressAnalyzeDone fault: XMLParserError fault: ServiceException | Allows application to handle the connection once the analysis is done |
| XccConnectionMediaForking | inOut | RequestXccConnectionMediaForking | ResponseXccConnectionMediaForking fault: XMLParserError fault: ServiceException | Allows application to enable media forking for the call session |
| XccConnectionData | outOnly |  | NotifyXccConnectionData | Notifies application that a connection is in one of the following conditions: a new connection is created a connection is in call delivery state a connection is redirected to another destination a connection is in alerting state a conection is in connected state a connection is transferred to another target a connection is in disconnected state a connection is handoff and leave the call session a connection is handoff to the call session |
| XccProbing | outIn | ResponseXccProbing | SolicitXccProbing | Allows XCC provider to keep alive a registration session and probe its health |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callData | CallData | M | Call information |
| mediaEvent | cMediaEvent | M | Choice of media event |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callData | CallData | M | Call information |
| connData | ConnData | M | Connection information |
| event | cConnectionData | M | Event choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| applicationData | ApplicationData | M | Application URL configured in the router CLI |
| providerData | ProviderData | M | Provider data |
| providerStatus | eProviderStatus | M | Provider current status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call Identification |
| action | cCallMediaForking | M | Provider data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call identification |
| mediaEventsFilter | MediaEventsFilter | O | Enables media event types to be sent in an application. Turn off any media events if this element is not included in the request |
| mediaForking | MediaForkingData | O | Media Forking Data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call identification |
| disCause | int | O | Q.850 disconnect cause range [1-188] |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call Identification |
| connID | string | M | Connection Identification |
| action | cConnectionAddressAnalyzeDone | M | Action choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call Identification |
| connID | string | M | Connection Identification |
| action | cConnectionAuthorizeDone | M | Action choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call Identification |
| connID | string | M | Connection Identification |
| action | cCallMediaForking | M | Media forking action choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call Identification |
| connID | string | M | Connection Identification |
| discCause | int | M | Q.850 disconnect cause range [1 - 188] |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| connectionEventsFilter | ConnectionEventsFilter | O | List of events that shall be notified to application |
| mediaEventsFilter | MediaEventsFilter | O | List of media events that shall be notfied to application |
| blockingEventTimeoutSec | int | O | Some application responses may block. This timeout specifies how long XCC provider will wait for the response in seconds. |
| blockingTimeoutHandle | eBlockingTimeoutHandle | O | How XCC provider should handle the call when blocking event timeouts |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| applicationData | ApplicationData | M | Application sends this request |
| providerData | ProviderData | M | XCC provider |
| connectionEventsFilter | ConnectionEventsFilter | O | List of events that shall be notified to application |
| mediaEventsFilter | MediaEventsFilter | O | List of media events that shall be notfied to application |
| blockingEventTimeoutSec | int | O | Some application responses may block. This timeout specifies how long XCC provider will wait for the response in seconds. |
| blockingTimeoutHandle | eBlockingTimeoutHandle | O | How XCC provider should handle the call when blocking event timeouts |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| action | cConnectionAddressAnalyze | M | Action choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| action | cConnectionAuthorize | M | Action choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| sequence | int | M | Sequence number of the probing messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| providerStatus | eProviderStatus | M | Current provider status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callData | CallData | M | Call information |
| connData | ConnData | M | Connection information |
| collectAddress | AddrData | O | Connection collect address data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callData | CallData | M | Call information |
| connDetailData | ConnDetailData | M | Connection detail information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| sequence | int | M | Sequence number of the probing message |
| interval | duration | M | Interval between probing messages |
| failureCount | int | M | Counts on previous probing failures since last successful message exchange in this reigstration session |
| registered | boolean | M | Registration status |
| providerStatus | eProviderStatus | M | Provider current status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| type | eAddrType | M | Address data type |
| addr | string | M | Address in string format |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| blockingEventTimeoutSec | int | O | Some application responses may block. This timeout specifies how long XCC provider will wait for the response in seconds. |
| blockingTimeoutHandle | eBlockingTimeoutHandle | O | How XCC provider should handle the call when blocking event timeouts |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| callID | string | M | Call Identification |
| state | eCallState | M | call state |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| routeAddrData | AddrData | M | terminating party address data |
| connectionEventsFilter | ConnectionEventsFilter | O | List of connection events shall be enabled for the new terminating connection |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| CallMediaForkingOpt | CallMediaForkingOpt - choice | M | CallMediaForkingOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| ConnAddrAnalzOpt | ConnAddrAnalzOpt - choice | M | ConnAddrAnalzOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| ConnAddrAnalzDoneOpt | ConnAddrAnalzDoneOpt - choice | M | ConnAddrAnalzDoneOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| ConnAuthOpt | ConnAuthOpt - choice | M | ConnAuthOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| ConnAuthDoneOpt | ConnAuthDoneOpt - choice | M | ConnAuthDoneOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| ConnDataOpt | ConnDataOpt - choice | M | ConnDataOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| MediaEventOpt | MediaEventOpt - choice | M | MediaEventOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connID | string | M | Connection Identification |
| state | eConnState | M | connection state |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connData | ConnData | M | Connection information |
| guid | string | M | Connection guid data |
| guidAltFormat | string | O | Connection guid data represented in Alternate format |
| callingAddrData | AddrData | O | Calling party address data |
| origCallingAddrData | AddrData | O | orignal calling party address data |
| calledAddrData | AddrData | O | Called party address data |
| origCalledAddrData | AddrData | O | original called party address data |
| redirectAddrData | RedirectAddrData | O | Redirect party address data |
| connIntfType | eConnIntfType | O | Connection interface type |
| mediaData | MediaData | O | Connection media data |
| connIntf | string | O | Connection interface name string |
| connDirectionType | eConnDirectionType | M | Connection direction type |
| routeName | string | O | Connection interface route name string |
| routeDescription | string | O | Route description |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connDetailData | ConnDetailData | M | Connection detail information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| eConnectionEventsFilter | eMediaEventsFilter | O |  |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connDetailData | ConnDetailData | M | Connection detail information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| mediaData | MediaData | M | Connection media data |
| discCause | int | M | Q.850 disconnect cause range [1 - 188] |
| statsData | StatsData | O | statistics data |
| jitterData | JitterData | O | media jitter data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| digit | string | M | a dtmf digit |
| dateTime | string | M | Time when dtmf occurs |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connDetailData | ConnDetailData | M | Connection detail information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| roundTripDelayMSec | int | M | Round trip delay (in ms) |
| onTimeRvPlayMSec | int | M | On time Rv Play (in ms) |
| gapFillWithPredictionMSec | int | M | Prediction count (in ms) |
| gapFillWithInterpolationMSec | int | M | Interpolation count (in ms) |
| gapFillWithRedundancyMSec | int | M | Redundancy count (in ms) |
| lostPacketsCount | int | M | Lost packets count |
| earlyPacketsCount | int | M | Early packets count |
| latePacketsCount | int | M | Late packets count |
| receiveDelayMSec | int | M | Receive delay (in ms) |
| loWaterPlayoutDelayMSec | int | M | Low water playout delay (in ms) |
| hiWaterPlayoutDelayMSec | int | M | Hi water playout delay (in ms) |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| old | eActivityState | M | old media activity state |
| new | eActivityState | M | new media activity state |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| ipv4 | string | M | Remote IP Address ver 4 |
| port | int | M | Remote RTP port |
| recordTone | eCountryType | O | Country specific record tone |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| type | eMediaType | M | Media type |
| coderType | string | O | codec type |
| coderByte | int | O | codec byte |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| eMediaEventsFilter | MediaEventsFilter | O |  |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| nearEndAddr | MediaAddrData | M | Media address for near-end side |
| farEndAddr | MediaAddrData | M | Media address for far-end side |
| preserve | boolean | O | Media Forking Preservd after app unregister |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| mediaForkingState | eMediaForkingState | M | Media forking status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| old | eMediaType | M | old media type |
| new | eMediaType | M | new media type |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| calledAddrData | AddrData | M | called address data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| redirectAddrData | RedirectAddrData | M | Redirect party address data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| discCause | int | M | Q.850 disconnect cause range [1 - 188] |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| callDuration | duration | M | call duration |
| TxPacketsCount | int | M | Total Tx Packets |
| TxBytesCount | int | M | Total Tx Bytes |
| TxDurationMSec | int | M | Tx Duration in milliseconds |
| TxVoiceDurationMSec | int | M | Tx Voice Duration in milliseconds |
| RxPacketsCount | int | M | Total Rx Packets |
| RxBytesCount | int | M | Total Rx Bytes |
| RxDurationMSec | int | M | Rx Duration in milliseconds |
| RxVoiceDurationMSec | int | M | Rx Voice Duration in milliseconds |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| toneType | eToneType | M | Tone type |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| redirectAddrData | RedirectAddrData | O | Redirect party address data |

| Element Name | Element Type | Desciption |
|---|---|---|
| enableMediaForking | MediaForkingData | Enable media forking |
| disableMediaForking | Empty element | Disable media forking |

| Element Name | Element Type | Desciption |
|---|---|---|
| release | Release | Release the connection |
| continueProcessing | Empty element | Continue the connection processing |
| callRoute | CallRouteData | Application specifies the call route |

| Element Name | Element Type | Desciption |
|---|---|---|
| block | Block | Temporary block the connection processing and wait for application for further request |
| release | Release | Release the connection |
| continueProcessing | Empty element | Continue the connection processing |
| callRoute | CallRouteData | Application specifies the call route |

| Element Name | Element Type | Desciption |
|---|---|---|
| release | Release | Release the connection |
| continueProcessing | Empty element | Continue the connection processing |

| Element Name | Element Type | Desciption |
|---|---|---|
| block | Block | Temporary block the connection processing and wait for application for further request |
| release | Release | Release the connection |
| continueProcessing | Empty element | Continue the connection processing |

| Element Name | Element Type | Desciption |
|---|---|---|
| created | Created | Enables connection created notify event |
| callDelivery | Empty element | Enables call delivery notify event |
| alerting | Empty element | Enables connection alerting notify event |
| redirected | Redirected | Enables connection redirected notify event |
| connected | Connected | Enables connection connected notify event |
| transferred | Transferred | Enables connection transferred notify event |
| disconnected | Disconnected | Enables connection disconnected notify event |
| handoffLeave | Empty element | Enables connection handoff leave notify event |
| handoffJoin | HandoffJoin | Enables connection handoff join notify event |
| mediaForking | MediaForkingEvent | Updates media forking status |

| Element Name | Element Type | Desciption |
|---|---|---|
| DTMF | DTMF | DTMF detected |
| mediaActivity | MediaActivity | Media activity state changed |
| modeChange | ModeChange | Mode of call changed |
| tone | Tone | Tone detected |
| mediaForking | MediaForkingEvent | Updates media forking status |

| Value | Description |
|---|---|
| ACTIVE | Active state |
| INACTIVE | Inactive state |

| Value | Description |
|---|---|
| E164 | Address is e164 number format |
| URI | Address is URI string format |
| OTHER | Address in other formats |

| Value | Description |
|---|---|
| RELEASE | Abort connection attempt |
| CONTINUE_PROCESSING | Proceed with connection attempt |

| Value | Description |
|---|---|
| IDLE | Initial state of a call. A call has zero connection |
| ACTIVE | A call has ongoing activity |
| INVALID | Final state of a call. A call in this state has one or more connections associated with |

| Value | Description |
|---|---|
| INCOMING | Incoming connection |
| OUTGOING | Outgoing connection |

| Value | Description |
|---|---|
| CREATED | First event sent when a new connection is created |
| AUTHORIZE_CALL | Sent to request call authorization |
| ADDRESS_ANALYZE | Enables address analyze solicit event |
| REDIRECTED | Enables connection redirected notify event |
| ALERTING | Enables connection alerting notify event |
| CONNECTED | Enables connection connected notify event |
| TRANSFERRED | Enables connection transferred notify event |
| CALL_DELIVERY | Enables connection call delivery notify event |
| DISCONNECTED | Enables connection disconnected notify event |
| HANDOFFLEAVE | Enables connection handoff leave notify event |
| HANDOFFJOIN | Enables connection handoff join notify event |

| Value | Description |
|---|---|
| CONN_UNKNOWN | Unknown connection interface type |
| CONN_ANALOG_EM | Analog E n M port |
| CONN_ANALOG_FXO | Analog FXO port |
| CONN_ANALOG_FXS | Analog FXS port |
| CONN_ANALOG_EFXS | Analog eFXS port |
| CONN_ANALOG_EFXO | Analog eFXO port |
| CONN_ISDN | ISDN PRI interface |
| CONN_CAS | CAS interfacee |
| CONN_BRI | ISDN BRI interface |
| CONN_R2 | E1 R2 interface |
| CONN_H323 | H.323 interface |
| CONN_SIP | SIP interface |
| CONN_TRUNKGROUP | Trunk group |

| Value | Description |
|---|---|
| IDLE | Connection is idle state |
| AUTHORIZE_CALL_ATTEMPT | Connection is in authorize call attempt |
| ADDRESS_COLLECT | Connection is in collecting address state |
| ADDRESS_ANALYZE | Connection is pending for address analyze state |
| CALL_DELIVERY | Connection is in call delivery state |
| ALERTING | Connection is in alerting state |
| CONNECTED | Connection is in connected state |
| DISCONNECTED | Enables connection disconnected notify event |

| Value | Description |
|---|---|
| COUNTRY_USA | United States |
| COUNTRY_AUSTRALIA | Australia |
| COUNTRY_GERMANY | Germany |
| COUNTRY_RUSSIA | Russia |
| COUNTRY_SPAIN | Spain |
| COUNTRY_SWITZERLAND | Switzerland |

| Value | Description |
|---|---|
| DTMF | Enables inband dtmf detection |
| MEDIA_ACTIVITY | Enables media activity detection |
| MODE_CHANGE | Enables mode change notify when a mode of a call session has changed |
| TONE_BUSY | Enables busy tone detection |
| TONE_DIAL | Enables dialtone detection |
| TONE_OUT_OF_SERVICE | Enable out of service tone detection |
| TONE_RINGBACK | Enables ringback detection |
| TONE_SECOND_DIAL | Enables secondary dialtone detection |

| Value | Description |
|---|---|
| FORK_STARTED | Media forking setup success |
| FORK_FAILED | Media forking setup failure |
| FORK_DONE | Media forking completed |

| Value | Description |
|---|---|
| VOICE | Voice call |
| FAX | Fax call |
| MODEM | Modem call |
| VIDEO | Video call |
| DATA | Data call |

| Value | Description |
|---|---|
| TONE_BUSY | busy tone detected |
| TONE_DIAL | dialtone detected |
| TONE_RINGBACK | ringback detected |
| TONE_SECOND_DIAL | secondary dialtone detected |
| TONE_OUT_OF_SERVICE | out of service detected |

| Provide Operation | Direction | Incoming Message | Outgoing Message | Description |
|---|---|---|---|---|
| XsvcRegister | inOut | RequestXsvcRegister | ResponseXsvcRegister fault: XMLParserError fault: ServiceException | Allows application to register with XSVC provider and specify the connection events filter |
| XsvcUnRegister | inOut | RequestXsvcUnRegister | ResponseXsvcUnRegister fault: XMLParserError fault: ServiceException | Allows application to unregister with XSVC provider |
| XsvcProviderUnRegister | outIn | ResponseXsvcProviderUnRegister | SolicitXsvcProviderUnRegister | Allows XSVC provider to unregister with application. |
| XsvcProviderStatus | outOnly |  | NotifyXsvcProviderStatus | Updates application once the XSVC provider status has changed |
| XsvcRouteSetFilter | inOut | RequestXsvcRouteSetFilter | ResponseXsvcRouteSetFilter fault: XMLParserError fault: ServiceException | Allows the application to set the fitler so that XSVC provider will only report to the application the updates it is interested in |
| XsvcRouteSnapshot | inOut | RequestXsvcRouteSnapshot | ResponseXsvcRouteSnapshot fault: XMLParserError fault: ServiceException | Allows application to get the big picture of all the routes being monitored. |
| XsvcRouteStats | inOut | RequestXsvcRouteStats | ResponseXsvcRouteStats fault: XMLParserError fault: ServiceException | Allows application to query the statistics of a trunk |
| XsvcRouteData | inOut | RequestXsvcRouteData | ResponseXsvcRouteData fault: XMLParserError fault: ServiceException | Allows application to query the detail information of a trunk |
| XsvcRouteConfiguration | outOnly |  | NotifyXsvcRouteConfiguration | Notifies application that a trunk configuration is changed |
| XsvcRouteStatus | outOnly |  | NotifyXsvcRouteStatus | Notifies application that a trunk status is change: Link status is changed Alarm status is changed |
| XsvcProbing | outIn | ResponseXsvcProbing | SolicitXsvcProbing | Allows XSVC provider to keep alive a registration session and probe its health. |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| applicationData | ApplicationData | M | Application URL configured in router CLI |
| providerData | ProviderData | M | Provider data |
| providerStatus | eProviderStatus | M | Provider current status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| type | eRouteChangeType | M |  |
| routeList | RouteList | M | Compact form of route information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| routeList | RouteList | M | Compact form of route information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| applicationData | ApplicationData | M | Application sends this request |
| providerData | ProviderData | M | XSVC provider |
| routeEventsFilter | RouteEventsFilter | O | List of events that shall be notified to application |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| routeName | string | M | Route name |
| routeType | eRouteType | M | Route type |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| isOn | boolean | M |  |
| routeFilterList | RouteFilterList | O | Route filter list |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| routeName | string | M | Route name |
| routeType | eRouteType | M | Route type |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| sequence | int | M | Sequence number of the probing messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| providerStatus | eProviderStatus | M | Current providerstatus |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| routeList | RouteList | M | Compact form of route information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| routeList | RouteList | M | Compact form of route information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| routeList | RouteList | M | Compact form of route information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| sequence | int | M | Sequence number of the probing message |
| interval | duration | M | Interval between probing messages |
| failureCount | int | M | Counts on previous probing failures since last successful message exchange in this reigstration session |
| registered | boolean | M | Registration status |
| providerStatus | eProviderStatus | M | Provider current status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| elapsedTime | duration | M | The time have elapsed since the beginning of the far end current error-measurement period |
| LCV | int | M | Line Coding Violation Error Event |
| PCV | int | M | Path Coding Violation Error Event |
| CSS | int | M | Controlled Slip Seconds |
| SEFS | int | M | Severely Errored Framing Second |
| LES | int | M | Line Errored Seconds |
| DM | int | M | Degraded Minutes |
| ES | int | M | Errored Seconds |
| BES | int | M | Bursty Errored Seconds |
| SES | int | M | everely Errored Seconds |
| UAS | int | M | Unavailable Seconds |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| channels | string | O | Channel mapping of the interface |
| totalChannels | int | M | Total channels on the interface |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| currentStatistics | CurrentStatistics | M | Interface latest statistics |
| totalStatistics | TotalStatistics | M | Interface accumulated statistics |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| routeName | string | M | Route name |
| routeType | eRouteType | M | Route type |
| routeDescription | string | O | Route description |
| trunkList | TrunkList | O |  |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| eRouteEventsFilter | eRouteEventsFilter | O |  |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| routeName | string | M | Route name |
| routeType | eRouteType | M | Route type |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| routeFilter | RouteFilter | O | Route filter |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| route | RouteData | M |  |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| intervalTime | duration | M | The time of previous far end intervals for which data was collected |
| LCV | int | M | Line Coding Violation Error Event |
| PCV | int | M | Path Coding Violation Error Event |
| CSS | int | M | Controlled Slip Seconds |
| SEFS | int | M | Severely Errored Framing Second |
| LES | int | M | Line Errored Seconds |
| DM | int | M | Degraded Minutes |
| ES | int | M | Errored Seconds |
| BES | int | M | Bursty Errored Seconds |
| SES | int | M | everely Errored Seconds |
| UAS | int | M | Unavailable Seconds |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| name | string | M | Name of the turnk interface |
| type | eTrunkType | M | Type of the turnk interface |
| status | eTrunkStatus | M | Status of the turnk interface |
| channelData | IntfChannels | O | Trunk interface channel information |
| alarmData | eTrunkAlarm | O | Trunk interface alarm information |
| statisticsData | IntfStatisticsData | O | Trunk interface statistics information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| trunkData | TrunkData | M |  |

| Value | Description |
|---|---|
| ROUTE_ADDED |  |
| ROUTE_DELETED |  |
| ROUTE_MODIFIED |  |

| Value | Description |
|---|---|
| ROUTE_CONF_UPDATED | Enables route configuration updated notify event |
| ROUTE_STATUS_UPDATED | Enables route status updated notify event) |

| Value | Description |
|---|---|
| VOIP |  |
| PSTN |  |

| Value | Description |
|---|---|
| NoAlarm | No alarm present |
| RcvFarEndLOF | Far end LOF (a.k.a. Yellow Alarm) |
| XmtFarEndLOF | Near end sending LOF Indication |
| RcvAIS | Far end sending AIS |
| XmtAIS | Near end sending AIS |
| LossOfFrame | Near end LOF (a.k.a. Red Alarm) |
| LossOfSignal | Near end loss Of Signal |
| LoopbackState | Near end is looped |
| T16AIS | E1 TS16 AIS |
| RcvFarEndOLMF | Far End Send TS16 LOMF |
| XmtFarEndOLMF | Near End Send TS16 LOMF |
| RcvTestCode | Near End detects a test code |
| OtherFailure | any line status not defined here |
| UnavailSigState | Near End in Unavailable Signal State |
| NetEquipOOS | Carrier Equipment Our Of Service |
| RcvPayloadAIS | DS2 Payload AIS |
| Ds2PerfThreshold | DS2 Performance Threshold |

| Value | Description |
|---|---|
| UP | - |
| DOWN | - |

| Value | Description |
|---|---|
| ISDN_PRI | - |
| ISDN_BRI | - |
| ANALOG | - |
| CAS | - |
| SIPV2 | - |
| H323 | - |

| Provide Operation | Direction | Incoming Message | Outgoing Message | Description |
|---|---|---|---|---|
| XcdrRegister | inOut | RequestXcdrRegister | ResponseXcdrRegister fault: XMLParserError fault: ServiceException | Allows application to register with XCDR provider and specify the connection events filter |
| XcdrUnRegister | inOut | RequestXcdrUnRegister | ResponseXcdrUnRegister fault: XMLParserError fault: ServiceException | Allows application to unregister with XCDR provider |
| XcdrProviderUnRegister | outIn | ResponseXcdrProviderUnRegister | SolicitXcdrProviderUnRegister | Allows XCDR provider to unregister with application. |
| XcdrProviderStatus | outOnly |  | NotifyXcdrProviderStatus | Updates application once the XCDR provider status has changed |
| XcdrSetAttribute | inOut | RequestXcdrSetAttribute | ResponseXcdrSetAttribute | Allows application to specify the attribute it is needed. Two formats, compact or detailed, can be selected. |
| XcdrRecord | outOnly |  | NotifyXcdrRecord | Notifies application the CDR |
| XcdrProbing | outIn | ResponseXcdrProbing | SolicitXcdrProbing | Allows XCDR provider to keep alive a registration session and probe its health. |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| applicationData | ApplicationData | M | Application URL configured in router CLI |
| providerData | ProviderData | M | Provider data |
| providerStatus | eProviderStatus | M | Provider current status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| format | eCdrFormat | M | CDR format |
| type | eCdrType | M | CDR type |
| cdr | string | M | CDR information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| applicationData | ApplicationData | M | Application send s this request |
| providerData | ProviderData | M | XCDR provider |
| cdrEventsFilter | CdrEventsFilter | O | List of events that shall be notified to application |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| format | eCdrFormat | M | CDR format |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| sequence | int | M | Sequence number of the probing messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| providerStatus | eProviderStatus | M | Current providerstatus |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| sequence | int | M | Sequence number of the probing message |
| interval | duration | M | Interval between probing messages |
| failureCount | int | M | Counts on previous probing failures since last successful message exchange in this registration session |
| registered | boolean | M | Registration status |
| providerStatus | eProviderStatus | M | Provider current status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| eCdrEventsFilter | eCdrEventsFilter | O |  |

| Value | Description |
|---|---|
| CDR_RECORD | Enables CDR record notify event |

| Value | Description |
|---|---|
| COMPACT | Displaying CDR in compact format |
| DETAIL | Displaying CDR in detail format |

| Value | Description |
|---|---|
| START | CDR when call are set up |
| STOP | CDR when call are released |

| Provide Operation | Direction | Incoming Message | Outgoing Message | Description |
|---|---|---|---|---|
| XmfRegister | inOut | RequestXmfRegister | ResponseXmfRegister fault: XMLParserError fault: ServiceException | Allows application to register with XMF provider and specify the connection events filter |
| XmfUnRegister | inOut | RequestXmfUnRegister | ResponseXmfUnRegister fault: XMLParserError fault: ServiceException | Allows application to unregister with XMF provider |
| XmfControlUpdate | inOut | RequestXmfControlUpdate | ResponseXmfControlUpdate fault: XMLParserError fault: ServiceException | Allows application to update parameters after registered |
| XmfProviderUnRegister | outIn | ResponseXmfProviderUnRegister | SolicitXmfProviderUnRegister | Allows XMF provider to unregister with application |
| XmfProviderStatus | outOnly |  | NotifyXmfProviderStatus | Updates application once the XMF provider status has changed |
| XmfCallMediaSetAttributes | inOut | RequestXmfCallMediaSetAttributes | ResponseXmfCallMediaSetAttributes fault: XMLParserError fault: ServiceException | Allows application to specify the media attributes for the call session |
| XmfCallMediaForking | inOut | RequestXmfCallMediaForking | ResponseXmfCallMediaForking fault: XMLParserError fault: ServiceException | Allows application to enable media forking for the call session |
| XmfConnectionMediaForking | inOut | RequestXmfConnectionMediaForking | ResponseXmfConnectionMediaForking fault: XMLParserError fault: ServiceException | Allows application to enable media forking for the connection |
| XmfCallData | outOnly |  | NotifyXmfCallData | Notifies application that a call session on one of the following conditions: mode is changed a dtmf digit is detected media inactive or active is detected |
| XmfConnectionData | outOnly |  | NotifyXmfConnectionData | Notifies application that a connection is in one of the following conditions: a new connection is created a connection is in call delivery state a connection is redirected to another destination a connection is in alerting state a conection is in connected state a connection is transferred to another target a connection is in disconnected state a connection is handoff and leave the call session a connection is handoff to the call session |
| XmfProbing | outIn | ResponseXmfProbing | SolicitXmfProbing | Allows XMF provider to keep alive a registration session and probe its health |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callData | CallData | M | call information |
| mediaEvent | cMediaEvent | M | Choice of media event |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callData | CallData | M | Call information |
| connData | ConnData | M | Connection information |
| event | cConnectionData | M | Event choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| applicationData | ApplicationData | M | Application URL configured in router CLI |
| providerData | ProviderData | M | Provider data |
| providerStatus | eProviderStatus | M | Provider current status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call Identification |
| action | cCallMediaForking | M | Media forking action choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call Identification |
| mediaEventsFilter | MediaEventsFilter | O | Enables media event types to be sent to application. Turn off any media events if this element is not included in the request |
| mediaForking | MediaForkingData | O | Media forkig data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| callID | string | M | Call Identification |
| connID | string | M | Connection Identification |
| action | cCallMediaForking | M | Media forking action choice |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| connectionEventsFilter | ConnectionEventsFilter | O | List of events that shall be notified to application |
| mediaEventsFilter | MediaEventsFilter | O | List of media events that shall be notfied to application |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| applicationData | ApplicationData | M | Application sends this request |
| providerData | ProviderData | M | XMF provider |
| connectionEventsFilter | ConnectionEventsFilter | O | List of events that shall be notified to application |
| mediaEventsFilter | MediaEventsFilter | O | List of media events that shall be notfied to application |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| sequence | int | M | Sequence number of the probing messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| providerStatus | eProviderStatus | M | Current provider status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |
| sequence | int | M | Sequence number of the probing message |
| interval | duration | M | Interval between probing messages |
| failureCount | int | M | Counts on previous probing failures since last successful message exchange in this reigstration session |
| registered | boolean | M | Registration status |
| providerStatus | eProviderStatus | M | Provider current status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| msgHeader | MsgHeader | M | Message header common for all the messages |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| type | eAddrType | M | Address data type |
| addr | string | M | Address in string format |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| callID | string | M | Call Identification |
| state | eCallState | M | call state |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| CallMediaForkingOpt | CallMediaForkingOpt - choice | M | CallMediaForkingOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| ConnDataOpt | ConnDataOpt - choice | M | ConnDataOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| MediaEventOpt | MediaEventOpt - choice | M | MediaEventOpt |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connID | string | M | Connection Identification |
| state | eConnState | M | connection state |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connData | ConnData | M | Connection information |
| guid | string | M | Connection guid data |
| guidAltFormat | string | O | Connection guid data represented in Alternate format |
| callingAddrData | AddrData | O | Calling party address data |
| origCallingAddrData | AddrData | O | orignal calling party address data |
| calledAddrData | AddrData | O | Called party address data |
| origCalledAddrData | AddrData | O | original called party address data |
| redirectAddrData | RedirectAddrData | O | Redirect party address data |
| connIntfType | eConnIntfType | O | Connection interface type |
| mediaData | MediaData | O | Connection media data |
| connIntf | string | O | Connection interface name string |
| connDirectionType | eConnDirectionType | M | Connection direction type |
| routeName | string | O | Connection interface route name string |
| routeDescription | string | O | Route description |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connDetailData | ConnDetailData | M | Connection detail information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| eConnectionEventsFilter | eConnectionEventsFilter | O |  |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connDetailData | ConnDetailData | M | Connection detail information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| mediaData | MediaData | M | Connection media data |
| discCause | int | M | Q.850 disconnect cause range [1 - 188] |
| statsData | StatsData | O | statistics data |
| jitterData | JitterData | O | media jitter data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| digit | string | M | a dtmf digit |
| dateTime | string | M | Time when dtmf occurs |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| connDetailData | ConnDetailData | M | Connection detail information |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| roundTripDelayMSec | int | M | Round trip delay (in ms) |
| onTimeRvPlayMSec | int | M | On time Rv Play (in ms) |
| gapFillWithPredictionMSec | int | M | Prediction count (in ms) |
| gapFillWithInterpolationMSec | int | M | Interpolation count (in ms) |
| gapFillWithRedundancyMSec | int | M | Redundancy count (in ms) |
| lostPacketsCount | int | M | Lost packets count |
| earlyPacketsCount | int | M | Early packets count |
| latePacketsCount | int | M | Late packets count |
| receiveDelayMSec | int | M | Receive delay (in ms) |
| loWaterPlayoutDelayMSec | int | M | Low water playout delay (in ms) |
| hiWaterPlayoutDelayMSec | int | M | Hi water playout delay (in ms) |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| old | eActivityState | M | old media activity state |
| new | eActivityState | M | new media activity state |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| ipv4 | string | M | Remote IP Address ver 4 |
| port | int | M | Remote RTP port |
| recordTone | eCountryType | O | Country specific record Tone |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| type | eMediaType | M | Media type |
| coderType | string | O | codec type |
| coderByte | int | O | codec byte |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| eMediaEventsFilter | eMediaEventsFilter | O |  |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| nearEndAddr | MediaAddrData | M | Media address for near-end side |
| farEndAddr | MediaAddrData | M | Media address for far-end side |
| preserve | boolean | O | Media Forking Preservd after app unregister |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| mediaForkingState | eMediaForkingState | M | Media forking status |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| old | eMediaType | M | old media type |
| new | eMediaType | M | new media type |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| calledAddrData | AddrData | M | called address data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| redirectAddrData | RedirectAddrData | M | Redirect party address data |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| callDuration | duration | M | call duration |
| TxPacketsCount | int | M | Total Tx Packets |
| TxBytesCount | int | M | Total Tx Bytes |
| TxDurationMSec | int | M | Tx Duration in milliseconds |
| TxVoiceDurationMSec | int | M | Tx Voice Duration in milliseconds |
| RxPacketsCount | int | M | Total Rx Packets |
| RxBytesCount | int | M | Total Rx Bytes |
| RxDurationMSec | int | M | Rx Duration in milliseconds |
| RxVoiceDurationMSec | int | M | Rx Voice Duration in milliseconds |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| toneType | eToneType | M | Tone type |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| redirectAddrData | RedirectAddrData | O | Redirect party address data |

| Element Name | Element Type | Description |
|---|---|---|
| enableMediaForking | MediaForkingData | Enable media forking |
| disableMediaForking | Empty element | Disable media forking |

| Element Name | Element Type | Description |
|---|---|---|
| created | Created | Enables connection created notify event |
| callDelivery | Empty element | Enables call delivery notify event |
| alerting | Empty element | Enables connection alerting notify event |
| redirected | Redirected | Enables connection redirected notify event |
| connected | Connected | Enables connection connected notify event |
| transferred | Transferred | Enables connection transferred notify event |
| disconnected | Disconnected | Enables connection disconnected notify event |
| handoffLeave | Empty element | Enables connection handoff leave notify event |
| handoffJoin | HandoffJoin | Enables connection handoff join notify event |
| mediaForking | MediaForkingEvent | Updates media forking status |

| Element Name | Element Type | Description |
|---|---|---|
| DTMF | DTMF | DTMF detected |
| mediaActivity | MediaActivity | Media activity state changed |
| modeChange | ModeChange | Mode of call changed |
| tone | Tone | Tone detected |
| mediaForking | MediaForkingData | Updates media forking status |

| Value | Description |
|---|---|
| ACTIVE | Active state |
| INACTIVE | Inactive state |

| Value | Description |
|---|---|
| E164 | Address is e164 number format |
| URI | Address is URI string format |
| OTHER | Address in other formats |

| Value | Description |
|---|---|
| IDLE | Initial state of a call. A call has zero connection |
| ACTIVE | A call has ongoing activity |
| INVALID | Final state of a call. A call in this state has one or more connections associated with |

| Value | Description |
|---|---|
| INCOMING | Incoming connection |
| OUTGOING | Outgoing connection |

| Value | Description |
|---|---|
| CREATED | First event sent when a new connection is created |
| REDIRECTED | Enables connection redirected notify event |
| ALERTING | Enables connection alerting notify event |
| CONNECTED | Enables connection connected notify event |
| TRANSFERRED | Enables connection transferred notify event |
| CALL_DELIVERY | Enables connection call delivery notify event |
| DISCONNECTED | Enables connection disconnected notify event |
| HANDOFFLEAVE | Enables connection handoff leave notify event |
| HANDOFFJOIN | Enables connection handoff join notify event |

| Value | Description |
|---|---|
| CONN_UNKNOWN | Unknown connection interface type |
| CONN_ANALOG_EM | Analog E n M port |
| CONN_ANALOG_FXO | Analog FXO port |
| CONN_ANALOG_FXS | Analog FXS port |
| CONN_ANALOG_EFXS | Analog eFXS port |
| CONN_ANALOG_EFXO | Analog eFXO port |
| CONN_ISDN | ISDN PRI interface |
| CONN_CAS | CAS interfacee |
| CONN_BRI | ISDN BRI interface |
| CONN_R2 | E1 R2 interface |
| CONN_H323 | H.323 interface |
| CONN_SIP | SIP interface |
| CONN_TRUNKGROUP | Trunk group |

| Value | Description |
|---|---|
| IDLE | Connection is idle state |
| AUTHORIZE_CALL_ATTEMPT | Connection is in authorize call attempt |
| ADDRESS_COLLECT | Connection is in collecting address state |
| ADDRESS_ANALYZE | Connection is pending for address analyze state |
| CALL_DELIVERY | Connection is in call delivery state |
| ALERTING | Connection is in alerting state |
| CONNECTED | Connection is in connected state |
| DISCONNECTED | Enables connection disconnected notify event |

| Value | Description |
|---|---|
| COUNTRY_USA | United States |
| COUNTRY_AUSTRALIA | Australia |
| COUNTRY_GERMANY | Germany |
| COUNTRY_RUSSIA | Russia |
| COUNTRY_SPAIN | Spain |
| COUNTRY_SWITZERLAND | Switzerland |

| Value | Description |
|---|---|
| DTMF | Enables inband dtmf detection |
| MEDIA_ACTIVITY | Enables media activity detection |
| MODE_CHANGE | Enables mode change notify when a mode of a call session has changed |
| TONE_BUSY | Enables busy tone detection |
| TONE_DIAL | Enables dialtone detection |
| TONE_OUT_OF_SERVICE | Enable out of service tone detection |
| TONE_RINGBACK | Enables ringback detection |
| TONE_SECOND_DIAL | Enables secondary dialtone detection |

| Value | Description |
|---|---|
| FORK_STARTED | Media forking setup success |
| FORK_FAILED | Media forking setup failure |
| FORK_DONE | Media forking completed |

| Value | Description |
|---|---|
| VOICE | Voice call |
| FAX | Fax call |
| MODEM | Modem call |
| VIDEO | Video call |
| DATA | Data call |

| Value | Description |
|---|---|
| TONE_BUSY | busy tone detected |
| TONE_DIAL | dialtone detected |
| TONE_RINGBACK | ringback detected |
| TONE_SECOND_DIAL | secondary dialtone detected |
| TONE_OUT_OF_SERVICE | out of service detected |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| url | anyURI | M | Application url data |
| name | string | O | Application name |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| transactionID | string | O | ID to identify a transaction for the message excahnge between provider and application. This filed is optional. This field is mandatory for the response message to return the same transactionID if present in the request/solicit message. |
| registrationID | string | O | ID to identify a registration session. This field is absent for RequestRegister and NotifyStatus messages. This field is mandatory for all the other messages. |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| url | anyURI | M | url for client application |

| Value | Description |
|---|---|
| SHUTDOWN | Service is not running |
| IN_SERVICE | Service is enabled and running |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| url | anyURI | M | Application url data |
| name | string | O | Application name |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| transactionID | string | O | ID to identify a transaction for the message excahnge between provider and application. This filed is optional. This field is mandatory for the response message to return the same transactionID if present in the request/solicit message. |
| registrationID | string | O | ID to identify a registration session. This field is absent for RequestRegister and NotifyStatus messages. This field is mandatory for all the other messages. |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| url | anyURI | M | url for client application |

| Value | Description |
|---|---|
| SHUTDOWN | Service is not running |
| IN_SERVICE | Service is enabled and running |

| Type | Reference |
|---|---|
| any | http://www.w3.org/TR/xmlschema-2/#any |
| anyURI | http://www.w3.org/TR/xmlschema-2/#anyURI |
| boolean | http://www.w3.org/TR/xmlschema-2/#boolean |
| dateTime | http://www.w3.org/TR/xmlschema-2/#dateTime |
| duration | http://www.w3.org/TR/xmlschema-2/#duration |
| int | http://www.w3.org/TR/xmlschema-2/#int |
| name | http://www.w3.org/TR/xmlschema-2/#Name |
| string | http://www.w3.org/TR/xmlschema-2/#string |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| Soap:Code/Value | string | M | The value is "Receiver" |
| Soap:Code/Subcode/Value | string | O | The value is "SERVICE EXCEPTION" |
| Soap:Reason/Text | string | M | Information on the nature of the fault |
| Soap:Detail | ServiceException | O | Details of the service exception. |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| errorCode | string | M | Error identifier with service prefix and number. |
| operation | string | O | Service opertion of the message |
| transactionID | string | O | transactionID if present in the request. |
| registrationID | string | O | registrationID if present in the request. |
| text | string | O | Message text |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| Soap:Code/Value | string | M | The value is "Sender" or "Receiver" |
| Soap:Code/Subcode/Value | string | M | The value is "XML PARSER ERROR" |
| Soap:Reason/Text | string | M | Information on the nature of the fault as follows: Memory exhausted Badly framed XML received Unknown namespace received A required attribute is missing An uninterpretable attribute has been received An invalidattribute value has been received An unknown XML tag has been received Anexpected XML tag or sequence is missing An unexpected XML tag has been received The value for an XML tag is not valid An internal error caused processing to be aborted An unsupported operation request has been received |
| Soap:Detail | XMLParserError | O | Details of the XML parser error. |

| Element Name | Element Type | M/O | Description |
|---|---|---|---|
| errorXMLDetail | string | O | Information to identify where is the parsing error in the XML message |
| errorXMLMsg | any | O | A copy of the original XML message for debugging purpose. |
| errorXMLTag | string | O | XML tag which causes the failure |

| Type | Reference |
|---|---|
| any | http://www.w3.org/TR/xmlschema-2/#any |
| anyURI | http://www.w3.org/TR/xmlschema-2/#anyURI |
| boolean | http://www.w3.org/TR/xmlschema-2/#boolean |
| dateTime | http://www.w3.org/TR/xmlschema-2/#dateTime |
| duration | http://www.w3.org/TR/xmlschema-2/#duration |
| int | http://www.w3.org/TR/xmlschema-2/#int |
| name | http://www.w3.org/TR/xmlschema-2/#Name |
| string | http://www.w3.org/TR/xmlschema-2/#string |