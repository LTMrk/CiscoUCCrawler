---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-jtapi-dev-12-5-1-cucm-b-cisco-unified-jtapi-developers-guide-1251-cucm--59e9583f9f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/jtapi_dev/12_5_1/cucm_b_cisco-unified-jtapi-developers-guide-1251/cucm_b_cisco-unified-jtapi-developers-guide-1251_chapter_0100.html
retrieved_at: 2026-08-16T18:12:04.560723+00:00
---

Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1)

# Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1)

Updated: June 11, 2025

Chapter: Hierarchy for All Cisco Unified JTAPI Packages

## Chapter: Hierarchy for All Cisco Unified JTAPI Packages

- Hierarchy for All Cisco Unified JTAPI Packages

- Class                              	 Hierarchy

- Interface                              	 Hierarchy

# Hierarchy for All Cisco Unified JTAPI Packages

The
                        		available Cisco Unified JTAPI packages are:

com.cisco.jtapi.extensions - For implementation information
                              			 about the extensions,  see Cisco Unified JTAPI Extensions .

com.cisco.services.alarm - For implementation information about
                              			 the alarm classes,  see Cisco Unified JTAPI Alarms and Services .

com.cisco.services.tracing - For implementation information
                              			 about the tracing,  see Cisco Unified JTAPI Alarms and Services .

com.cisco.services.tracing.implementation - For information
                              			 about the implementation of tracing,  see Cisco Unified JTAPI Alarms and Services .

## Class
                        	 Hierarchy

```
java.lang.Object
   com.cisco.services.alarm. AlarmManager com.cisco.services.tracing. BaseTraceWriter (implements
                                               com.cisco.services.tracing.TraceWriter)
      com.cisco.services.tracing. ConsoleTraceWriter com.cisco.services.tracing. LogFileTraceWriter com.cisco.services.tracing. OutputStreamTraceWriter com.cisco.services.tracing. SyslogTraceWriter com.cisco.jtapi.extensions. CiscoAddressCallInfo com.cisco.jtapi.extensions. CiscoJtapiVersion com.cisco.jtapi.extensions. CiscoMediaCapability com.cisco.jtapi.extensions. CiscoG711MediaCapability com.cisco.jtapi.extensions. CiscoG723MediaCapability com.cisco.jtapi.extensions. CiscoG729MediaCapability com.cisco.jtapi.extensions. CiscoGSMMediaCapability com.cisco.jtapi.extensions. CiscoWideBandMediaCapability com.cisco.jtapi.extensions. CiscoRTPParams com.cisco.services.alarm. DefaultAlarm (implements
                                                       com.cisco.services.alarm.Alarm) 
   com.cisco.services.alarm. DefaultAlarmWriter (implements
                                                 com.cisco.services.alarm.AlarmWriter) 
   com.cisco.services.alarm. ParameterList java.lang.Throwable (implements java.io.Serializable) 
      java.lang.Exception
         com.cisco.jtapi.extensions. CiscoRegistrationException com.cisco.jtapi.extensions. CiscoUnregistrationException com.cisco.services.tracing. TraceManagerFactory com.cisco.services.tracing.implementation. TraceManagerImpl (implements com.cisco.services.tracing.TraceManager) 
   com.cisco.services.tracing.implementation. TraceWriterManagerImpl (implements com.cisco.services.tracing.TraceWriterManager)
```

## Interface
                        	 Hierarchy

```
javax.telephony.Address
   com.cisco.jtapi.extensions. Related Documentation (also extends
                           com.cisco.jtapi.extensions. CiscoObjectContainer )
      com.cisco.jtapi.extensions. CiscoHuntConnection javax.telephony.callcenter.RouteAddress
      com.cisco.jtapi.extensions. CiscoRouteAddress
```

```
javax.telephony.AddressObserver 
   com.cisco.jtapi.extensions. CiscoAddressObserver
```

```
com.cisco.services.alarm. Alarm
```

```
com.cisco.services.alarm. AlarmWriter
```

```
javax.telephony.Call
   javax.telephony.callcontrol.CallControlCall
      com.cisco.jtapi.extensions. CiscoCall (also extends
                               com.cisco.jtapi.extensions. CiscoObjectContainer ) 
   com.cisco.jtapi.extensions. CiscoConsultCall
```

```
com.cisco.jtapi.extensions. CiscoCallCtlTermConnHeldReversionEv
```

```
com.cisco.jtapi.extensions. CiscoConferenceChain
```

```
com.cisco.jtapi.extensions. CiscoFeatureReason
```

```
com.cisco.jtapi.extensions. CiscoJtapiException
```

```
com.cisco.jtapi.extensions. CiscoJtapiProperties
```

```
com.cisco.jtapi.extensions. CiscoLocales
```

```
com.cisco.jtapi.extensions. CiscoMediaSecurityIndicator
```

```
com.cisco.jtapi.extensions. CiscoMediaConnectionMode
```

```
com.cisco.jtapi.extensions. CiscoMediaEncryptionAlgorithmType
```

```
com.cisco.jtapi.extensions. CiscoMediaEncryptionKeyInfo
```

```
com.cisco.jtapi.extensions. CiscoMediaSecurityIndicator
```

```
com.cisco.jtapi.extensions. CiscoMonitorInitiatorInfo
```

```
com.cisco.jtapi.extensions. CiscoMonitorTargetInfo
```

```
com.cisco.jtapi.extensions. CiscoObjectContainer com.cisco.jtapi.extensions. Related Documentation (also extends
                                                              javax.telephony.Address)
      com.cisco.jtapi.extensions. CiscoHuntConnection com.cisco.jtapi.extensions. CiscoCall (also extends
                                          javax.telephony.callcontrol.CallControlCall)
   com.cisco.jtapi.extensions. CiscoConsultCall com.cisco.jtapi.extensions. CiscoCallID com.cisco.jtapi.extensions. CiscoConnection (also extends
                                    javax.telephony.callcontrol.CallControlConnection)
   com.cisco.jtapi.extensions. CiscoConnectionID com.cisco.jtapi.extensions. CiscoConsultCall com.cisco.jtapi.extensions. CiscoHuntConnection com.cisco.jtapi.extensions. CiscoJtapiPeer (also extends
                                                           javax.telephony.JtapiPeer, 
                                               com.cisco.services.tracing.TraceModule)
   com.cisco.jtapi.extensions. CiscoMediaTerminal com.cisco.jtapi.extensions. CiscoProvider com.cisco.jtapi.extensions. CiscoRouteTerminal com.cisco.jtapi.extensions. CiscoTerminal (also extends
                                                             javax.telephony.Terminal)
      com.cisco.jtapi.extensions. CiscoMediaTerminal com.cisco.jtapi.extensions. CiscoRouteTerminal com.cisco.jtapi.extensions. CiscoTerminalConnection (also extends
                            javax.telephony.callcontrol.CallControlTerminalConnection)
```

```
com.cisco.jtapi.extensions. CiscoPartyInfo
```

```
com.cisco.jtapi.extensions. CiscoProvFeatureID
```

```
com.cisco.jtapi.extensions. CiscoProviderCapabilityChangedEv
```

```
com.cisco.jtapi.extensions. CiscoRecorderInfo
```

```
com.cisco.jtapi.extensions. CiscoRTPBitRate
```

```
com.cisco.jtapi.extensions. CiscoRTPInputProperties
```

```
com.cisco.jtapi.extensions. CiscoRTPOutputProperties
```

```
com.cisco.jtapi.extensions. CiscoRTPPayload
```

```
com.cisco.jtapi.extensions. CiscoSynchronousObserver
```

```
com.cisco.jtapi.extensions. CiscoTermConnPrivacyChangedEv
```

```
com.cisco.jtapi.extensions. CiscoTermEvFilter
```

```
com.cisco.jtapi.extensions.CiscoTerminalProtocol com.cisco.jtapi.extensions.CiscoTone 
com.cisco.jtapi.extensions. CiscoUrlInfo
```

```
javax.telephony.Connection
   javax.telephony.callcontrol.CallControlConnection
      com.cisco.jtapi.extensions. CiscoConnection (also extends
                                      com.cisco.jtapi.extensions.CiscoObjectContainer)
```

```
javax.telephony.events.Ev
   javax.telephony.events.AddrEv
      com.cisco.jtapi.extensions. CiscoAddrEv (also extends
                                                   com.cisco.jtapi.extensions.CiscoEv)
         com.cisco.jtapi.extensions. CiscoAddrAutoAcceptStatusChangedEv com.cisco.jtapi.extensions. CiscoAddrInServiceEv com.cisco.jtapi.extensions. CiscoAddrIntercomInfoChangedEv com.cisco.jtapi.extensions. CiscoAddrIntercomInfoRestorationFailedEv com.cisco.jtapi.extensions. CiscoAddrOutOfServiceEv (also extends
                                       com.cisco.jtapi.extensions.CiscoOutOfServiceEv)
         com.cisco.jtapi.extensions. CiscoAddrRecordingConfigChangedEv javax.telephony.callcontrol.events.CallCtlEv
      javax.telephony.callcontrol.events.CallCtlCallEv (also extends
                                                        javax.telephony.events.CallEv)
         javax.telephony.callcontrol.events.CallCtlConnEv (also extends
                                                        javax.telephony.events.ConnEv)
   javax.telephony.callcontrol.events.CallCtlConnOfferedEv
com.cisco.jtapi.extensions. CiscoCallCtlConnOfferedEv javax.telephony.events.CallEv
      javax.telephony.events.CallActiveEv
         com.cisco.jtapi.extensions. CiscoConsultCallActiveEv (also extends
                                               com.cisco.jtapi.extensions.CiscoCallEv)
      javax.telephony.callcontrol.events.CallCtlCallEv (also extends 
                                         javax.telephony.callcontrol.events.CallCtlEv)
      javax.telephony.callcontrol.events.CallCtlConnEv (also extends
                                                        javax.telephony.events.ConnEv)
         javax.telephony.callcontrol.events.CallCtlConnOfferedEv
            com.cisco.jtapi.extensions. CiscoCallCtlConnOfferedEv com.cisco.jtapi.extensions. CiscoCallEv (also extends
                                                   com.cisco.jtapi.extensions.CiscoEv)
         com.cisco.jtapi.extensions. CiscoCallChangedEv com.cisco.jtapi.extensions. CiscoCallSecurityStatusChangedEv com.cisco.jtapi.extensions. CiscoConferenceChainAddedEv com.cisco.jtapi.extensions. CiscoConferenceChainRemovedEv com.cisco.jtapi.extensions. CiscoConferenceEndEv com.cisco.jtapi.extensions. CiscoConferenceStartEv com.cisco.jtapi.extensions. CiscoConsultCallActiveEv (also extends
                                        javax.telephony.events.CallActiveEv) 
    com.cisco.jtapi.extensions. CiscoToneChangedEv com.cisco.jtapi.extensions. CiscoTransferEndEv com.cisco.jtapi.extensions. CiscoTransferStartEv javax.telephony.events.ConnEv 
      javax.telephony.callcontrol.events.CallCtlConnEv (also extends
                                    javax.telephony.callcontrol.events.CallCtlCallEv) 
javax.telephony.callcontrol.events.CallCtlConnOfferedEv
   com.cisco.jtapi.extensions. CiscoCallCtlConnOfferedEv javax.telephony.events.TermConnEv 
      com.cisco.jtapi.extensions. CiscoTermConnMonitoringEndEv com.cisco.jtapi.extensions. CiscoTermConnMonitoringStartEv com.cisco.jtapi.extensions. CiscoTermConnMonitorInitiatorInfoEv com.cisco.jtapi.extensions. CiscoTermConnMonitorTargetInfoEv com.cisco.jtapi.extensions. CiscoTermConnRecordingEndEv com.cisco.jtapi.extensions. CiscoTermConnRecordingFailedEv com.cisco.jtapi.extensions. CiscoTermConnRecordingStartEv com.cisco.jtapi.extensions. CiscoTermConnRecordingTargetInfoEv com.cisco.jtapi.extensions. CiscoTermConnSelectChangedEv
```

```
com.cisco.jtapi.extensions. CiscoEv com.cisco.jtapi.extensions. CiscoAddrActivatedEv com.cisco.jtapi.extensions. CiscoAddrActivatedOnTerminalEv com.cisco.jtapi.extensions. CiscoAddrAddedToTerminalEv com.cisco.jtapi.extensions. CiscoAddrAutoAcceptStatusChangedEv com.cisco.jtapi.extensions. CiscoAddrCreatedEv com.cisco.jtapi.extensions. CiscoAddrEv (also extends
                                                        javax.telephony.events.AddrEv)
      com.cisco.jtapi.extensions. CiscoAddrAutoAcceptStatusChangedEv com.cisco.jtapi.extensions. CiscoAddrInServiceEv com.cisco.jtapi.extensions. CiscoAddrIntercomInfoChangedEv com.cisco.jtapi.extensions. CiscoAddrIntercomInfoRestorationFailedEv com.cisco.jtapi.extensions. CiscoAddrOutOfServiceEv (also extends
                                        com.cisco.jtapi.extensions.CiscoAddrEv, 
                                 com.cisco.jtapi.extensions.CiscoOutOfServiceEv) 
      com.cisco.jtapi.extensions. CiscoAddrRecordingConfigChangedEv com.cisco.jtapi.extensions. CiscoAddrInServiceEv com.cisco.jtapi.extensions. CiscoAddrIntercomInfoChangedEv com.cisco.jtapi.extensions. CiscoAddrIntercomInfoRestorationFailedEv com.cisco.jtapi.extensions. CiscoAddrOutOfServiceEv (also extends
                                         com.cisco.jtapi.extensions.CiscoAddrEv) 
      com.cisco.jtapi.extensions. CiscoAddrRecordingConfigChangedEv com.cisco.jtapi.extensions. CiscoAddrRemovedEv com.cisco.jtapi.extensions. CiscoAddrRemovedFromTerminalEv com.cisco.jtapi.extensions. CiscoAddrRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedOnTerminalEv com.cisco.jtapi.extensions. CiscoCallChangedEv com.cisco.jtapi.extensions. CiscoCallEv (also extends
                                                        javax.telephony.events.CallEv) 
      com.cisco.jtapi.extensions. CiscoCallChangedEv com.cisco.jtapi.extensions. CiscoCallSecurityStatusChangedEv com.cisco.jtapi.extensions. CiscoConferenceChainAddedEv com.cisco.jtapi.extensions. CiscoConferenceChainRemovedEv com.cisco.jtapi.extensions. CiscoConferenceEndEv com.cisco.jtapi.extensions. CiscoConferenceStartEv com.cisco.jtapi.extensions. CiscoConsultCallActiveEv (also extends
                                              javax.telephony.events.CiscoCallEv) 
      com.cisco.jtapi.extensions. CiscoToneChangedEv com.cisco.jtapi.extensions. CiscoTransferEndEv com.cisco.jtapi.extensions. CiscoTransferStartEv
```

```
com.cisco.jtapi.extensions. CiscoCallSecurityStatusChangedEv
```

```
com.cisco.jtapi.extensions. CiscoConferenceChainAddedEv
```

```
com.cisco.jtapi.extensions. CiscoConferenceChainRemovedEv
```

```
com.cisco.jtapi.extensions. CiscoConferenceEndEv
```

```
com.cisco.jtapi.extensions. CiscoConferenceStartEv
```

```
com.cisco.jtapi.extensions. CiscoConsultCallActiveEv (also extends
                                            javax.telephony.events.CallActiveEv, 
                                               com.cisco.jtapi.extensions.CiscoCallEv)
```

```
com.cisco.jtapi.extensions. CiscoMediaOpenLogicalChannelEv
```

```
com.cisco.jtapi.extensions. CiscoOutOfServiceEv com.cisco.jtapi.extensions. CiscoAddrOutOfServiceEv (also extends
                                               com.cisco.jtapi.extensions.CiscoAddrEv) 
   com.cisco.jtapi.extensions. CiscoTermOutOfServiceEv (also extends
                                               com.cisco.jtapi.extensions.CiscoTermEv)
```

```
com.cisco.jtapi.extensions. CiscoProvCallParkEv
```

```
com.cisco.jtapi.extensions. CiscoProvFeatureEv (also extends
                                                        javax.telephony.events.ProvEv) 
   com.cisco.jtapi.extensions. CiscoAddrActivatedEv com.cisco.jtapi.extensions. CiscoAddrActivatedOnTerminalEv com.cisco.jtapi.extensions. CiscoAddrAddedToTerminalEv com.cisco.jtapi.extensions. CiscoAddrCreatedEv com.cisco.jtapi.extensions. CiscoAddrRemovedEv com.cisco.jtapi.extensions. CiscoAddrRemovedFromTerminalEv com.cisco.jtapi.extensions. CiscoAddrRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedOnTerminalEv com.cisco.jtapi.extensions. CiscoProvCallParkEv com.cisco.jtapi.extensions. CiscoProvFeatureEv com.cisco.jtapi.extensions. CiscoProvCallParkEv com.cisco.jtapi.extensions. CiscoRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedOnTerminalEv com.cisco.jtapi.extensions. CiscoTermActivatedEv com.cisco.jtapi.extensions. CiscoTermCreatedEv com.cisco.jtapi.extensions. CiscoTermRemovedEv com.cisco.jtapi.extensions. CiscoTermRestrictedEv com.cisco.jtapi.extensions. CiscoProvFeatureEv com.cisco.jtapi.extensions. CiscoProvCallParkEv com.cisco.jtapi.extensions. CiscoRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedOnTerminalEv com.cisco.jtapi.extensions. CiscoRTPInputKeyEv com.cisco.jtapi.extensions. CiscoRTPInputStartedEv com.cisco.jtapi.extensions. CiscoRTPInputStoppedEv com.cisco.jtapi.extensions. CiscoRTPOutputKeyEv com.cisco.jtapi.extensions. CiscoRTPOutputStartedEv com.cisco.jtapi.extensions. CiscoRTPOutputStoppedEv com.cisco.jtapi.extensions. CiscoTermActivatedEv com.cisco.jtapi.extensions. CiscoTermButtonPressedEv com.cisco.jtapi.extensions. CiscoTermCreatedEv com.cisco.jtapi.extensions. CiscoTermDataEv com.cisco.jtapi.extensions. CiscoTermDeviceStateActiveEv com.cisco.jtapi.extensions. CiscoTermDeviceStateAlertingEv com.cisco.jtapi.extensions. CiscoTermDeviceStateHeldEv com.cisco.jtapi.extensions. CiscoTermDeviceStateWhisperEv com.cisco.jtapi.extensions. CiscoTermDNDStatusChangedEv com.cisco.jtapi.extensions. CiscoTermEvFilter (also extends
                                                        javax.telephony.events.TermEv)
      com.cisco.jtapi.extensions. CiscoMediaOpenLogicalChannelEv com.cisco.jtapi.extensions. CiscoRTPInputKeyEv com.cisco.jtapi.extensions. CiscoRTPInputStartedEv com.cisco.jtapi.extensions. CiscoRTPInputStoppedEv com.cisco.jtapi.extensions. CiscoRTPOutputKeyEv com.cisco.jtapi.extensions. CiscoRTPOutputStartedEv com.cisco.jtapi.extensions. CiscoRTPOutputStoppedEv com.cisco.jtapi.extensions. CiscoTermButtonPressedEv com.cisco.jtapi.extensions. CiscoTermDataEv com.cisco.jtapi.extensions. CiscoTermDeviceStateActiveEv com.cisco.jtapi.extensions. CiscoTermDeviceStateAlertingEv com.cisco.jtapi.extensions. CiscoTermDeviceStateHeldEv com.cisco.jtapi.extensions. CiscoTermDeviceStateIdleEv com.cisco.jtapi.extensions. CiscoTermDeviceStateWhisperEv com.cisco.jtapi.extensions. CiscoTermDNDStatusChangedEv com.cisco.jtapi.extensions. CiscoTermInServiceEv com.cisco.jtapi.extensions. CiscoTermOutOfServiceEv (also extends
                                       com.cisco.jtapi.extensions.CiscoOutOfServiceEv) 
      com.cisco.jtapi.extensions. CiscoTermRegistrationFailedEv com.cisco.jtapi.extensions. CiscoTermSnapshotCompletedEv com.cisco.jtapi.extensions. CiscoTermSnapshotEv com.cisco.jtapi.extensions. CiscoTermInServiceEv com.cisco.jtapi.extensions. CiscoTermOutOfServiceEv (also extends
                                      com.cisco.jtapi.extensions.CiscoOutOfServiceEv, 
                                               com.cisco.jtapi.extensions.CiscoTermEv) 
   com.cisco.jtapi.extensions. CiscoTermRegistrationFailedEv com.cisco.jtapi.extensions. CiscoTermRemovedEv com.cisco.jtapi.extensions. CiscoTermRestrictedEv com.cisco.jtapi.extensions. CiscoTermSnapshotCompletedEv com.cisco.jtapi.extensions. CiscoTermSnapshotEv com.cisco.jtapi.extensions. CiscoToneChangedEv com.cisco.jtapi.extensions. CiscoTransferEndEv com.cisco.jtapi.extensions. CiscoTransferStartEv
```

```
javax.telephony.events.ProvEv 
   com.cisco.jtapi.extensions.CiscoProvEv (also extends
                                                   com.cisco.jtapi.extensions.CiscoEv) 
      com.cisco.jtapi.extensions. CiscoAddrActivatedEv com.cisco.jtapi.extensions. CiscoAddrActivatedOnTerminalEv com.cisco.jtapi.extensions. CiscoAddrAutoAcceptStatusChangedEv com.cisco.jtapi.extensions. CiscoAddrCreatedEv com.cisco.jtapi.extensions. CiscoAddrRemovedEv com.cisco.jtapi.extensions. CiscoAddrRemovedFromTerminalEv com.cisco.jtapi.extensions. CiscoAddrRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedOnTerminalEv com.cisco.jtapi.extensions. CiscoProvCallParkEv com.cisco.jtapi.extensions. CiscoProvFeatureEv com.cisco.jtapi.extensions. CiscoProvCallParkEv com.cisco.jtapi.extensions. CiscoRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedEv com.cisco.jtapi.extensions. CiscoAddrRestrictedOnTerminalEv com.cisco.jtapi.extensions. CiscoTermActivatedEv com.cisco.jtapi.extensions. CiscoTermCreatedEv com.cisco.jtapi.extensions. CiscoTermRemovedEv com.cisco.jtapi.extensions. CiscoTermRestrictedEv
```

```
javax.telephony.events.TermEv 
   com.cisco.jtapi.extensions. CiscoTermEv (also extends
                                                   com.cisco.jtapi.extensions.CiscoEv) 
   com.cisco.jtapi.extensions. CiscoMediaOpenLogicalChannelEv com.cisco.jtapi.extensions. CiscoRTPOutputKeyEv com.cisco.jtapi.extensions. CiscoRTPInputStartedEv com.cisco.jtapi.extensions. CiscoRTPInputStoppedEv com.cisco.jtapi.extensions. CiscoRTPOutputKeyEv com.cisco.jtapi.extensions. CiscoRTPOutputStartedEv com.cisco.jtapi.extensions. CiscoRTPOutputStoppedEv com.cisco.jtapi.extensions. CiscoTermButtonPressedEv com.cisco.jtapi.extensions. CiscoTermDataEv com.cisco.jtapi.extensions. CiscoTermDeviceStateActiveEv com.cisco.jtapi.extensions. CiscoTermDeviceStateAlertingEv com.cisco.jtapi.extensions. CiscoTermDeviceStateHeldEv com.cisco.jtapi.extensions. CiscoTermDeviceStateIdleEv com.cisco.jtapi.extensions. CiscoTermDeviceStateWhisperEv com.cisco.jtapi.extensions. CiscoTermDNDStatusChangedEv com.cisco.jtapi.extensions. CiscoTermInServiceEv com.cisco.jtapi.extensions. CiscoTermOutOfServiceEv (also extends
                                       com.cisco.jtapi.extensions.CiscoOutOfServiceEv) 
   com.cisco.jtapi.extensions. CiscoTermRegistrationFailedEv com.cisco.jtapi.extensions. CiscoTermSnapshotCompletedEv com.cisco.jtapi.extensions. CiscoTermSnapshotEv
```

```
javax.telephony.JtapiPeer 
   com.cisco.jtapi.extensions. CiscoJtapiPeer (also extends
                               com.cisco.jtapi.extensions. CiscoObjectContainer , 
                                               com.cisco.services.tracing.TraceModule)
```

```
javax.telephony.Provider 
   com.cisco.jtapi.extensions. CiscoProvider (also extends
                                      com.cisco.jtapi.extensions.CiscoObjectContainer)
```

```
javax.telephony.capabilities.ProviderCapabilities 
   com.cisco.jtapi.extensions. CiscoProviderCapabilities
```

```
javax.telephony.ProviderObserver 
   com.cisco.jtapi.extensions. CiscoProviderObserver
```

```
javax.telephony.callcenter.RouteSession 
   com.cisco.jtapi.extensions. CiscoRouteSession
```

```
javax.telephony.callcenter.events.RouteSessionEvent 
   javax.telephony.callcenter.events.RouteEvent 
      com.cisco.jtapi.extensions. CiscoRouteEvent javax.telephony.callcenter.events.RouteUsedEvent 
      com.cisco.jtapi.extensions. CiscoRouteUsedEvent
```

```
javax.telephony.Terminal 
   com.cisco.jtapi.extensions. CiscoTerminal (also extends
                                      com.cisco.jtapi.extensions.CiscoObjectContainer) 
      com.cisco.jtapi.extensions. CiscoMediaTerminal com.cisco.jtapi.extensions. CiscoRouteTerminal
```

```
javax.telephony.TerminalConnection 
   javax.telephony.callcontrol.CallControlTerminalConnection 
      com.cisco.jtapi.extensions. CiscoTerminalConnection (also extends
                        com.cisco.jtapi.extensions.CiscoObjectContainer)
```

```
javax.telephony.TerminalObserver 
   com.cisco.jtapi.extensions. CiscoTerminalObserver
```

```
com.cisco.services.tracing. Trace com.cisco.services.tracing. ConditionalTrace com.cisco.services.tracing. UnconditionalTrace
```

```
com.cisco.services.tracing.TraceManagercom.cisco.services.tracing.TraceModule 
   com.cisco.jtapi.extensions. CiscoJtapiPeer (also extends
                                     com.cisco.jtapi.extensions.CiscoObjectContainer, 
                                                            javax.telephony.JtapiPeer)
```

```
com.cisco.services.tracing. TraceWriter
```

```
com.cisco.services.tracing. TraceWriterManager
```