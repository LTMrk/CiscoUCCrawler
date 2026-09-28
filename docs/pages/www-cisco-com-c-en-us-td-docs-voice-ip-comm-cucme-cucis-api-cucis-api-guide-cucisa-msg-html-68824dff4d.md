---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-cucis-api-cucis-api-guide-cucisa-msg-html-68824dff4d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/CUCIS_API/CUCIS_API_Guide/CUCISA_MSG.html
retrieved_at: 2026-08-16T15:55:02.375061+00:00
---

Cisco Unified Communications Gateway Services API Guide

# Cisco Unified Communications Gateway Services API Guide

Updated: November 4, 2011

Chapter: Provider and Application Interactions

## Chapter: Provider and Application Interactions

## Provider and Application Interactions

This section describes the interaction and sequence of messages that take place between the providers on the voice gateway and the application.

## XCC

This section describes some of the interactions that takes place between the XCC provider and the application.

### Interaction Between the XCC Provider and Application

Figure A-1 shows the interaction and the sequence of messages that are exchanged between the application and the XCC provider during registration.

Figure A-1 Message interaction when the application registers with XCC Provider

### Message Examples

This section provides examples of message exchanges between the application and the XCC provider.

Example of a Registration Message Exchange

The following is an example of the RequestXccRegister message sent by the application requesting registration and setting up the connection event and media event filters.

The following is an example of a ResponseXccRegister message sent from the XCC provider in response to the application’s registration request. The registration ID is used in all messages during the registered session:

Example of a Change in Service Message

The following is an example of a NotifyXccStatus message sent from the gateway when the XCC shuts down.

Example of the Application Requesting to be Unregister

The following is an example of a RequestXccUnRegister message sent from an application when it no longer needs the provider’s services.

Example of a Keepalive Probing Message

The following is an example of the SolicitXccProbing message sent from the XCC provider to maintain an active registration session.

The following is an example of the ResponseXccProbing message sent from the application responding to the XCC provider probing message.

Example of the Provider Shutting Down

The following is an example of the SolicitXccProviderUnRegister message sent from the XCC provider when it enters the shutdown state.

### Interaction Between the Application, XCC Provider, and XCC Call

Figure A-2 shows the interaction between the application, XCC provider, and XCC call for a call and the sequence of messages that are exchanged between the application and the XCC provider.

Figure A-2 Message interaction when a call comes in

### Message Examples

This section provides examples of message exchanges between the application and the XCC provider during a call.

Example of the Application Setting Call Media Attributes.

The following is an example of a RequestXccCallMediaSetAttributes message sent from application notifying the provider of the media attributes for a call.

The following is an example of the ResponseXccCallMediaSetAttributes message sent from the a XCC provider in response to the application’s media set attribute request.

Example of a Change in Call Mode

The following is an example of a NotifyXccCallData message sent from the XCC provider notifying the application that the call mode has changed from modem to fax mode.

Example of a DTMF Detection

The following is an example of a NotifyXccCallData message sent from the XCC provider notifying the application that the number 1 digit on the keypad has been pressed.

Example of Call Media Forking

The following is an example of a RequestXccCallMediaForking message sent from the application requesting that the media stream for the call session be forked. The application must include two unique RTP ports—nearEndAddr element for the forked TX media stream and the farEndAddr XCC element for the RX media stream

The following is an example of the NotifyXccCallData message sent from the XCC provider to the application with information on the status of the media forking.

The following is an example of the ResponseXccCallMediaForking message sent from the XCC provider in response to the application’s media forking request.

### Interaction Between the Application and XCC Connection

The following section describes the interaction between the application, XCC provider and XCC Connection.

### Examples of XCC Message Exchange in the Connection State

The following is an example of a notification message sent from the XCC provider notifying the application of a connection creation event.

### Interaction for Call Authorization with an Immediate Response

Figure A-3 illustrates the call interaction when an application responds immediately to a call authorization solicit message from the XCC provider.

Figure A-3 Call Interaction when the application responds immediately to a call

The following example is the SolicitXccConnectionAuthorize message sent from the XCC provider asking for authorization to continue processing the call.

Upon authentication, the application immediately sends a response. The following example is the response message (ResponseXccConnectionAuthorize) from the application to continue processing the call.

### Interaction for Call Authorization with a Delayed Response

Figure A-4 illustrates the call interaction when an application cannot respond immediately to a call authorization solicit message from the XCC provider. The application can request that the XCC provider temporarily block the call.

Figure A-4 Call Interaction when the application has a delayed response

### Interaction During Digit Collection with an Immediate Response

Figure A-5 shows the call interaction after an application has sent a message to the XCC provider to continue the call and begin collecting digits. The application is able to respond immediately.

Figure A-5 Call Interaction when the application responds immediately upon digit collection

The following example is the SolicitXccConnectionAddressAnalyze message sent from the XCC provider with call information for the application.

### Interaction During Digit Collection with a Delayed Response

Figure A-6 shows the call interaction after an application has sent a message to the XCC provider to continue to begin collecting digits, but the application is unable to respond immediately.

Figure A-6 Call Interaction when the application has a delayed response to digit collections

Notification Examples

The following example is the NotifyXccConnection message sent from the XCC provider letting the application know that an outgoing call is being connected.

The following example is the NotifyXccConnection message sent from the XCC provider letting the application know that a transferred event has occurred.

The following example is the NotifyXccConnection message sent from the XCC provider letting the application know that a transfer handoff leave event has occurred.

The following example is the NotifyXccConnection message sent from the XCC provider letting the application know that a transfer handoff join event has occurred.

## XSVC

This section describes the some of the interactions that take place between the XSVC provider and the application.

### Interaction Between the XSVC Provider, Application, and Route Object

Figure A-7 shows the interaction and the sequence of messages that are exchanged between the applicatio, XSVC provider, and the route object during registration.

Figure A-7 Interaction between an applicaton, XSVC provider, and route object

### Message Examples

This section provides examples of message exchanges between the application and the XSVC provider.

Example of a Registration Message Exchange

The following is an example of a RequestXsvcRegister message sent from the application requesting registration and setting route event filters.

The following is an example of a ResponseXsvcRegister message sent from the XSVC provider in response to the application’s registration request.

The following is an example of a NotifyXsvcStatusmessage sent from the XSVC provider when it enters the shutdown state.

Example of a Snapshot Reponse Message

The following is an example of a ResponseXsvcRouteSnapshot message sent from XSVC provider with route information.

Example of a Route Configuration Change

The following is an example of a NotifyXsvcRouteConfiguration message sent from XSVC provider notifying the application that the route list has been modified.

### Interaction between the Application and the XSVC Provider

Figure A-8 illustrates the call interaction when an application responds immediately to a call authorization solicit message from the XSVC provider.

Figure A-8 Interaction between the application, XSVC provider, and route object when new filters are applied

Example of a Route Data Message

The following is an example of a ResponseXsvcRouteStats message sent from XSVC provider with route statistics.

## XCDR

This section describes some of the interactions that takes place etween the XCDR provider and the application.

### Interaction Between the XCDR Provider and Application

Figure A-9 shows the interaction and the sequence of messages that are exchanged between the application and the XCDR provider during registration.

Figure A-9 Messae interaction when the application registers with the XCDR provider

### Message Examples

This section provides examples of message exchanges between the application and the XCDR provider.

Example of a Registration Message Exchange

The following is an example of a RequestXcdrRegister message sent from the application requesting registration and specifying the type of records that it expects to receive.

The following is an example of a ResponseXcdrRegister message sent from the XCDR provider in response to the application’s registration request.

## XMF

### Message Examples

The following is an example an example of RequestXmfConnectionMediaForking with recording tone enabled.

The following is an example an example of RequestXmfCallMediaForking with recording tone enabled.

The following is an example an example of RequestXmfCallMediaSetAttributes with recording tone enabled.