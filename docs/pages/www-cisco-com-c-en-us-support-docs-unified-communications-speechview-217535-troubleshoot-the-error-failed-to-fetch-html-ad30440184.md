---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-speechview-217535-troubleshoot-the-error-failed-to-fetch-html-ad30440184
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/speechview/217535-troubleshoot-the-error-failed-to-fetch.html
retrieved_at: 2026-08-16T18:57:40.192029+00:00
---

Troubleshoot the Error: Failed to Fetch License Data on Unity Connection Speechview

# Troubleshoot the Error: Failed to Fetch License Data on Unity Connection Speechview

### Download Options

Updated: November 3, 2021

Document ID: 217535

Contents

## Contents

## Introduction

This document describes what actions to take when the Cisco Unity Connection (CUC) version 12.5(1) on the Graphical User Interface (GUI) shows the error message: Failed to fetch License Data. For more details, check CuSlmSvr diagnostic logs at enable/register the Speechview service.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unity Connection.

- Cisco Speechview feature.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Log Analysis

As the displayed error message states, you need to collect the CuSlmSvr logs (Connection Smart License Manager Server in RTMT) to further investigate the issue.

The process starts:

```
19:19:03.395 |8060,,,CuSlmSvr,3,18-08-2020 INFO [SLM-12] com.cisco.unity.slm.common.SmartLicenseUtility#isSttEnabled - STT Enabled Status :1 19:19:03.395 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.dal.DbCrudOperationsImpl#get - Exceute Query : select sttdataacquired from vw_elmlicensestatus 19:19:03.395 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.dal.DbHelper#getDbConnection - Getting DB connection for executing query 19:19:03.396 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.dal.DbHelper#executeQuery - Query executed succesfully 19:19:03.396 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.dal.DbHelper#closeResources - closeResources Statement : DbHelper 19:19:03.396 |8060,,,CuSlmSvr,3,18-08-2020 INFO [SLM-12] com.cisco.unity.slm.common.SmartLicenseUtility#isSttDataAcquired - STTDataAquired Status :0 19:19:03.396 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.dal.DbCrudOperationsImpl#get - Exceute Query : select count from UnityDirDb:vw_LicenseStatusCount where tagname='LicSTTProSubscribersMax' 19:19:03.397 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.dal.DbHelper#getDbConnection - Getting DB connection for executing query 19:19:03.402 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.dal.DbHelper#executeQuery - Query executed succesfully 19:19:03.402 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.dal.DbHelper#closeResources - closeResources Statement : DbHelper 19:19:03.402 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.core.SmartLicenseManager#fetchThirdPartyKeys - Values of parameter passed in requestThirdPartyKeys method :: isLive :: true isComplianceRequired :: true thirdPartyKeysParamArr [ThirdPartyKeysParam [id=2017844434, keyId=0, name=VOUCHER_CODE, value=regid.2017-04.com.cisco.CUC_SpeechView,12.0_946cef06-3332-4037-9bd3-e4705c2c7ebb, routing=NUANCE, action=GENERATE]] 19:19:03.403 |8060,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-12] com.cisco.nesla.plugin.DefaultCrypto#parseCertificate - getSubjectDN().getName: CN=Cisco Unity Connection,2.5.4.5=#132434643437646630342d616538392d346466362d626331352d643137633161336631353366,O=Cisco 19:19:03.403 |8060,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-12] com.cisco.nesla.plugin.DefaultCrypto#parseCertificate - getSubjectDN().toString: CN=Cisco Unity Connection, SERIALNUMBER=4d47df04-ae89-4df6-bc15-d17c1a3f153f, O=Cisco 19:19:03.403 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.crypto.CustomCrypto#extractSubjectAlternativeNames - Entered extractSubjectAlternativeNames(null) 19:19:03.403 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.crypto.CustomCrypto#getSUDIList - Collection<List<?>> is null, exiting - extractSubjectAlternativeNames 19:19:03.403 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.crypto.CustomCrypto#extractSubjectAlternativeNames - returning sudiList : [], exiting extractSubjectAlternativeNames(Collection<List<?>> 19:19:03.403 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.cisco.unity.slm.crypto.CustomCrypto#extractCertificateType - Entered extractCertificateType(subjectDnName = CN=Cisco Unity Connection, SERIALNUMBER=4d47df04-ae89-4df6-bc15-d17c1a3f153f, O=Cisco) 19:19:03.403 |8060,,,CuSlmSvr,3,18-08-2020 INFO [SLM-12] com.cisco.unity.slm.crypto.CustomCrypto#extractCertificateType - Matched subjectDnName - CN=Cisco Unity Connection, SERIALNUMBER=4d47df04-ae89-4df6-bc15-d17c1a3f153f, O=Cisco, pattern1=CN=.*SERIALNUMBER.*, match1=true, pattern2=O=.*SERIALNUMBER=.*CN=.*, match2=false, returning certificate = ID_CERT 19:19:03.404 |8060,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-12] com.cisco.nesla.plugin.DefaultCrypto#parseCertificate - getSubjectDN().getName: CN=MMI Signer,O=Cisco 19:19:03.404 |8060,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-12] com.cisco.nesla.plugin.DefaultCrypto#parseCertificate - getSubjectDN().toString: CN=MMI Signer, O=Cisco
```

The server requests the VOUCHER_CODE :

```
19:19:03.417 |8060,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-12] com.cisco.nesla.agent.impl.MessageComposer#composeTPK - composedMesg: {"signature":{"type":"SHA-256","value":"Pf9POO6+YzchhKnZ3Q0SMamccnS/FPcoRSTdhJNyJkr0EHeDm3bU3FzUqneuKZuw4vfP3nsGP0OzwcY8tzOszcoK3JJDpi5y4wPm2IijLwGZSx0eQVatt7kXxbZ5PU25y4ZKY/egd1hANOn3E7lcLAXAgmgNR5A2exxrgkLt5pHo1mAVTSaDGag0+YqKRXxOTTyJPs1pmeIj6z7ELwWlwBD4QQANYdFj+leHChq9figxcE1ftcXHn1dy2nWl9musbfZu9B+Vb/32kusoRq/uEuxn2YbBQ3wsjq5yLQM8iDNzF7vzcZC1JsgyO3qn3jxzRYPrfhTHr2LY6WGcRcJ37g=="},"credential":null,"request":"{\"header\":{\"version\":\"1.1\",\"locale\":\"en_US.UTF-8\",\"sudi\":{\"suvi\":null,\"uuid\":\"0cd5739043bf4318aae467eacec7dbb9\",\"host_identifier\":null,\"mac_address\":null,\"udi_pid\":\"Cisco Unity Connection\",\"udi_serial_number\":\"0cd5739043bf4318aae467eacec\",\"udi_vid\":null},\"timestamp\":0,\"nonce\":\"7648446339161391345\",\"request_type\":\"THIRD_PARTY_KEY\",\"agent_actions\":null,\"connect_info\":null,\"product_instance_identifier\":\"4d47df04-ae89-4df6-bc15-d17c1a3f153f\",\"id_cert_serial_number\":\"16451298\",\"signing_cert_serial_number\":\"3\"},\"nonce\":\"7648446339161391345\",\"request_data\":\"{\\\"sudi\\\":{\\\"suvi\\\":null,\\\"uuid\\\":\\\"0cd5739043bf4318aae467eacec7dbb9\\\",\\\"host_identifier\\\":null,\\\"mac_address\\\":null,\\\"udi_pid\\\":\\\"Cisco Unity Connection\\\",\\\"udi_serial_number\\\":\\\"0cd5739043bf4318aae467eacec\\\",\\\"udi_vid\\\":null},\\\"timestamp\\\":1597792743402,\\\"nonce\\\":\\\"7648446339161391345\\\",\\\"live\\\":true,\\\"data\\\":[{\\\"id\\\":2017844434,\\\"name\\\":\\\"VOUCHER_CODE\\\",\\\"value\\\":\\\"regid.2017-04.com.cisco.CUC_SpeechView,12.0_946cef06-3332-4037-9bd3-e4705c2c7ebb\\\",\\\"routing\\\":\\\"NUANCE\\\",\\\"action\\\":\\\"GENERATE\\\",\\\"key_id\\\":0}],\\\"product_instance_identifier\\\":\\\"4d47df04-ae89-4df6-bc15-d17c1a3f153f\\\",\\\"compliance_required\\\":true}\"}"}
```

The message is sent to CSSM with the request to fetch the keys.

```
19:19:03.417 |8060,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-12] com.cisco.nesla.plugin.EmbeddedGCHCommunication#sendSCHMessage - in sendMessage(), resetProfileHttpAddr to: https://tools.cisco.com/its/service/oddce/services/DDCEService 19:19:03.417 |8060,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-12] com.cisco.nesla.plugin.EmbeddedGCHCommunication#sendSCHMessage - EmbeddedGCHCommunication [callHomeProps={devUrl=https://tools.cisco.com/its/service/oddce/services/DDCEService}, url=https://tools.cisco.com/its/service/oddce/services/DDCEService, transportMode=TransportCallHome, parentFactory=com.cisco.nesla.agent.SmartAgentFactory@158cfc5, gchClient=com.callhome.service.CallHome@cb4b0, SA_PROFILE=null, dualUrl=null] 19:19:03.417 |8060,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-12] com.cisco.nesla.plugin.EmbeddedGCHCommunication#sendSCHMessage - effective Authenticator URL: https://tools.cisco.com/its/service/oddce/services/DDCEService 19:19:03.417 |8060,,,CuSlmSvr,6,18-08-2020 INFO [SLM-12] com.callhome.module.config_manager.ProfileManager#resetProfileHttpAddr - reset http url Cisco-TAC-1 for profile https://tools.cisco.com/its/service/oddce/services/DDCEService 19:19:03.418 |8060,,,CuSlmSvr,6,18-08-2020 DEBUG [SLM-12] com.callhome.module.message_processor.BaseMessage#setInternalReqData - Set request data: Session_To = http://tools.cisco.com/neddce/services/DDCEService 19:19:03.422 |8060,,,CuSlmSvr,6,18-08-2020 DEBUG [SLM-12] com.callhome.module.message_processor.BaseMessage#setInternalReqData - Set request data: Attachment_Data = {"signature":{"type":"SHA-256","value":"Pf9POO6+YzchhKnZ3Q0SMamccnS/FPcoRSTdhJNyJkr0EHeDm3bU3FzUqneuKZuw4vfP3nsGP0OzwcY8tzOszcoK3JJDpi5y4wPm2IijLwGZSx0eQVatt7kXxbZ5PU25y4ZKY/egd1hANOn3E7lcLAXAgmgNR5A2exxrgkLt5pHo1mAVTSaDGag0+YqKRXxOTTyJPs1pmeIj6z7ELwWlwBD4QQANYdFj+leHChq9figxcE1ftcXHn1dy2nWl9musbfZu9B+Vb/32kusoRq/uEuxn2YbBQ3wsjq5yLQM8iDNzF7vzcZC1JsgyO3qn3jxzRYPrfhTHr2LY6WGcRcJ37g=="},"credential":null,"request":"{\"header\":{\"version\":\"1.1\",\"locale\":\"en_US.UTF-8\",\"sudi\":{\"suvi\":null,\"uuid\":\"0cd5739043bf4318aae467eacec7dbb9\",\"host_identifier\":null,\"mac_address\":null,\"udi_pid\":\"Cisco Unity Connection\",\"udi_serial_number\":\"0cd5739043bf4318aae467eacec\",\"udi_vid\":null},\"timestamp\":0,\"nonce\":\"7648446339161391345\",\"request_type\":\"THIRD_PARTY_KEY\",\"agent_actions\":null,\"connect_info\":null,\"product_instance_identifier\":\"4d47df04-ae89-4df6-bc15-d17c1a3f153f\",\"id_cert_serial_number\":\"16451298\",\"signing_cert_serial_number\":\"3\"},\"nonce\":\"7648446339161391345\",\"request_data\":\"{\\\"sudi\\\":{\\\"suvi\\\":null,\\\"uuid\\\":\\\"0cd5739043bf4318aae467eacec7dbb9\\\",\\\"host_identifier\\\":null,\\\"mac_address\\\":null,\\\"udi_pid\\\":\\\"Cisco Unity Connection\\\",\\\"udi_serial_number\\\":\\\"0cd5739043bf4318aae467eacec\\\",\\\"udi_vid\\\":null},\\\"timestamp\\\":1597792743402,\\\"nonce\\\":\\\"7648446339161391345\\\",\\\"live\\\":true,\\\"data\\\":[{\\\"id\\\":2017844434,\\\"name\\\":\\\"VOUCHER_CODE\\\",\\\"value\\\":\\\"regid.2017-04.com.cisco.CUC_SpeechView,12.0_946cef06-3332-4037-9bd3-e4705c2c7ebb\\\",\\\"routing\\\":\\\"NUANCE\\\",\\\"action\\\":\\\"GENERATE\\\",\\\"key_id\\\":0}],\\\"product_instance_identifier\\\":\\\"4d47df04-ae89-4df6-bc15-d17c1a3f153f\\\",\\\"compliance_required\\\":true}\"}"} 19:19:03.422 |8060,,,CuSlmSvr,6,18-08-2020 INFO [SLM-12] com.callhome.module.data.statistics.StatisticsMgr#updateSLStatistics - update Smart Lincense Statistics Data 19:19:03.429 |8060,,,CuSlmSvr,6,18-08-2020 INFO [SLM-12] com.callhome.module.message_processor.BaseMessage#makeAmlBlockAttachment - create attachment for smart_licensing_data with type inline
```

The response is then processed

```
19:19:04.741 |8060,,,CuSlmSvr,6,18-08-2020 DEBUG [SLM-12] com.callhome.module.message_processor.BaseMessage#processResponseMessage - Process response message
```

The error is seen

```
19:19:04.789 |8060,,,CuSlmSvr,3,18-08-2020 ERROR [SLM-12] com.cisco.unity.slm.rpc.server.SlmRpcHandler# fetchThirdPartyKeys - Exception occured while fetching Third party key from Nesla - LicenseResponse status code: FAILED, message: Product Instance is not consuming this tag : 19:19:04.789 |8060,,,CuSlmSvr,3,com.cisco.nesla.agent.impl.AsyncResponseProcessor.processTPK(AsyncResponseProcessor.java:676) 19:19:04.789 |8060,,,CuSlmSvr,3,com.cisco.nesla.agent.impl.AsyncRequestProcessor.sendTPK(AsyncRequestProcessor.java:427) 19:19:04.789 |8060,,,CuSlmSvr,3,com.cisco.nesla.agent.impl.SmartAgentImpl.requestThirdPartyKeys(SmartAgentImpl.java:1221) 19:19:04.789 |8060,,,CuSlmSvr,3,com.cisco.unity.slm.core.SmartLicenseManager.fetchThirdPartyKeys(SmartLicenseManager.java:1206) 19:19:04.789 |8060,,,CuSlmSvr,3,com.cisco.unity.slm.rpc.server.SlmRpcHandler.fetchThirdPartyKeys(SlmRpcHandler.java:882) 19:19:04.789 |8060,,,CuSlmSvr,3,sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) 19:19:04.790 |8060,,,CuSlmSvr,3,sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57) 19:19:04.790 |8060,,,CuSlmSvr,3,sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) 19:19:04.790 |8060,,,CuSlmSvr,3,java.lang.reflect.Method.invoke(Method.java:606) 19:19:04.790 |8060,,,CuSlmSvr,3,com.retrogui.dualrpc.common.RpcWorker.processRpcCallMessage(RpcWorker.java:231) 19:19:04.790 |8060,,,CuSlmSvr,3,com.retrogui.dualrpc.common.RpcWorker.run(RpcWorker.java:75) 19:19:04.790 |8060,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-12] com.retrogui.dualrpc.common.RpcWorker#processRpcCallMessage - 29341551:Outbound message id=s79970-1597791156498-12 contains the rpc results for originating message id=c2383379-1597792743384-1 19:19:04.790 |8056,,,CuSlmSvr,3,18-08-2020 DEBUG [com.retrogui.messageserver.common.OutboundMessageHandler:hashcode=564416:sessionId=29341551] com.retrogui.messageserver.common.OutboundMessageHandler#run - 29341551:Outgoing message size. Message id=s79970-1597791156498-12, size=684 bytes
```

The Failed request is seen

```
19:10:22.430 |2334,,,CuSlmSvr,3,18-08-2020 DEBUG [SLM-11] com.cisco.unity.slm.core.SmartLicenseManager# requestLicenses - License Usage corresponding to CUC_SpeechView is 0 19:10:22.430 |2334,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-11] com.cisco.nesla.agent.impl.SmartAgentImpl#requestEntitlement - enter requestEntitlement() 19:10:22.430 |2334,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-11] com.cisco.nesla.agent.impl.SmartAgentImpl#requestEntitlement - entitlementTag: regid.2017-04.com.cisco.CUC_SpeechView,12.0_946cef06-3332-4037-9bd3-e4705c2c7ebb 19:10:22.430 |2334,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-11] com.cisco.nesla.agent.impl.SmartAgentImpl#requestEntitlement - count: 0 19:10:22.430 |2334,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-11] com.cisco.nesla.agent.impl.SmartAgentImpl#releaseEntitlement - enter releaseEntitlement() 19:10:22.430 |2334,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-11] com.cisco.nesla.agent.impl.SmartAgentImpl#releaseEntitlement - entitlementTag: regid.2017-04.com.cisco.CUC_SpeechView,12.0_946cef06-3332-4037-9bd3-e4705c2c7ebb 19:10:22.430 |2334,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-11] com.cisco.nesla.agent.impl.AsyncRequestProcessor#sendAUTH - queue auth message, status: true 19:10:22.430 |2334,,,CuSlmSvr,4,18-08-2020 DEBUG [SLM-11] com.cisco.nesla.agent.impl.SmartAgentImpl#releaseEntitlement - exit requestEntitlement()
```

## Solution

Typically, you can get past the Failed to fetch License Data error by issuing a new token for the CUC server in the Satellite and re-registering the whole server.

Then, attempt the next steps and test further after that:

Enable the SpeechView Transcription of Voice Messages in the Class of Service : The members of the class of service can view the transcriptions of the voice messages using an IMAP client configured to access the user messages.

Procedure:

Step 1. In Cisco Unity Connection Administration, expand Class of Service and select Class of Service .

Step 2. In the Search Class of Service page, select the class of service in which you want to enable SpeechView transcription or create a new one selecting Add New.

Step 3. On the Edit Class of Service page, under Licensing Features section, select Use Standard SpeechView Transcription Service option to enable the standard transcription. Similarly, you can select Use SpeechView Pro Transcription Service option to enable professional transcription.

Step 4. Select the applicable options under the transcription service section and select Save . (For information on each field, see Help > This Page ).

The error message observed must disappear after the previous steps have been executed and you can continue with the Speechview service registration.

### Revision History

2.0

03-Nov-2021

Initial Release

1.0

03-Nov-2021

Initial Release

### Contributed by Cisco Engineers

Luis Miranda

Cisco TAC

### This Document Applies to These Products

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 03-Nov-2021 | Initial Release |
| 1.0 | 03-Nov-2021 | Initial Release |