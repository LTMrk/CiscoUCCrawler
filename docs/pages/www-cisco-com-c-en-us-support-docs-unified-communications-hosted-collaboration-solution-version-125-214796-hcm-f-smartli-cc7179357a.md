---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-version-125-214796-hcm-f-smartli-cc7179357a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-version-125/214796-hcm-f-smartlicense-integration-walkthrou.html
retrieved_at: 2026-09-01T14:58:22.258502+00:00
---

Configure HCM-F Integration with Smart License Manager

# Configure HCM-F Integration with Smart License Manager

### Download Options

Updated: May 26, 2023

Document ID: 214796

Contents

## Contents

## Introduction

This document describes how to synchronize your product instance with your Smart accounts in Cisco Hosted Collaboration Solution ( HCS ) 12.5 via

Cisco Hosted Collaboration Mediation Fulfillment (HCM-F)

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

Cisco Unified Communications Manager (CUCM) version 12.5

HCM-F 12.5

CUCM Smart Licensing - Direct Model

Cisco Smart Software Management (CSSM)

### Components Used

The information in this document is based on these software and hardware versions:

CUCM 12.5.X

HCM-F 12.5.1

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Hosted License Manager (HLM)  runs in HCM-F as service. HLM/HCM-F has been developed  to register Cisco Unified Communications Applications (UC) applications to the Smart Licensing Service running in Cisco Cloud. Once UC Applications are assigned to the Smart Licensing Service, License consumption of these applications are tracked from the CSSM portal which acts as a Single License Management Repository for HCS Partners.

The HCM-F HLM Service allows the configuration of a Smart account in HCM-F and permits any Cluster based Operations related to this Smart account from HCM-F.

The Smart Licensing Service which resides in the Cisco cloud exposes different Application programming interface (API) through the OAuth Authentication. Additionally UC Applications do expose APIs to allow HCM-F to perform multiple steps involved during the course of Cluster Operation like “Assign” and “UnAssign”.

ence HCM-F makes use of API’s exposed on both the sides to perform a Cluster Operation.

Network connectivity to the Cisco Cloud services is required for this integration:

cloudsso1.cisco.com  -> 72.163.4.74 cloudsso2.cisco.com -> 173.37.144.211 cloudsso3.cisco.com -> 173.38.127.38

swapi.cisco.com -> 146.112.59.25

All communications between the HCM-F/Proxy and the Cisco Cloud services are done through TLS connection on port TCP/443.

## Configuration

As a HCS Partner admin, login to the Cisco API Developer Portal select Explore > Smart Accounts & Licensing APIs > Smart Accounts

To configure a Smart Account in HCM-F,  an API Client is required:

The Client Credentials generated in this step use the "API Service" Application Type, require the Smart Account API association and are provided for Smart Account Configuration Access in HCM-F. Once the correct client credentials and the Smart Account domain name are provided, HCM-F completes the configuration and uses the same access details to interact with Smart licensing Service.

Specifically it authenticates against cloudsso.cisco.com to botain an Oauth2.0 bearer token and then fetches all the Virtual Accounts from the Cloud License Service via swapi.cisco.com. Time taken for the Virtual accounts fetch depends on the number of Virtual accounts and Virtual account synced from Satellite. This operation takes up to an Hour. Virtual Accounts which are synced from Satellite are ignored.

### HCM-F Configuration Workflow for Smart Licensing

Navigate to Infrastructure Manager > Smart Licensing > Configure Smart Account :

The information here is populated with the output generated in the section addressed earlier in this document.

Navigate to Infrastructure Manager > Smart Licensing > Transport Mode:

Set up the transport mode in HCM-F is required for the connection of HCM-F and UC applications to CSSM.

Note : HCM-F 12.5.1 supports only direct Model integration i.e the Transport Mode can be set to direct or proxy

Navigate to Infrastructure Manager > Smart Licensing > Virtual Account Summary:

Note : {To see the virtual accounts associated with the smart account. Select the smart account name from the list. The Virtual Accounts page shows the list of virtual accounts.}

### Cluster Association CSSM

In order to “assign” a UC application to CSSM, you need to ensure both the 12.5 Cluster as well as the UC application are present and configured in the HCM-F inventory along with admin and platform credential.

Once the Smart Account configuration is done, HCM-F syncs up all the data from CSSM and update SDR, Smart Account along with the virtual account data. Once the Virtual Account Data is updated in SDR , the admin user is allowed to assign the Cluster to any Virtual Account.

This Cluster operation is referred to as "Cluster Assignment" , and the Removal of Cluster from VA is termed as "Cluster unAssignment".  Cluster moves from one VA to another are referred to  as "Cluster ReAssignment".

To Assign a cluster to CSSM, navigate to

Infrastructure Manager > Smart Licensing > Virtual Account Summary:

Select the Virtual Account you want to utilize.

Cluster Assignment:  Slect Assign :

Select the UC application you want to assign and select the Assign Button:

Once the Assignment has completed, the UC application shows up as assigned to the Virtual Account (VA) you used:

( Smart Licensing > Cluster Summary

## What happens when you assign a UC application to the Smart Licensing Service via HCM-F?

This is the  HLM Workflow that is executed:

- Verification

- License Mode Change

- Transport Mode Change

- Registration

This can be seen in to the Jobs section ( Infrastructure Manager > Administration > Jobs) :

## Logs Walkthrough (HLM Logs set to Detailed)

- HLM gets a cluster assigns request from the database and checks if the cluster is eligible:

```
2019-06-26 13:17:35,199 INFO [53] Getting the Instance of Cluster Assignment Agent ClusterAssignmentRequest
2019-06-26 13:17:35,199 DEBUG [53] AgentMessageDispatcher::process -- Agent with instance >SMART_LIC_CLUSTER_OPERATION<Exist in memory,no need to read from persistence store-- ClusterAssign(SMART_LIC_CLUSTER_OPERATION)
2019-06-26 13:17:35,199 INFO [169] processing Agent SMART_LIC_CLUSTER_OPERATION

2019-06-26 13:17:35,332 DEBUG [169] isProgressInfoChanged : true
2019-06-26 13:17:35,332 DEBUG [169] job.getStatusInfo: :Verification - Inprogress|License Mode Change - Not Started|Transport Mode Change - Not Started|Registration - Not Started|
2019-06-26 13:17:35,357 INFO [169] jobKID from create: 26
2019-06-26 13:17:35,357 DEBUG [169] Update method at End : JobDTOcom.cisco.hcs.HLM.smartlic.dto.JobDTO Object {
sDRJobPK: 26
jobId: null
jobType: PROVISIONING
description: Assignment of Cluster cl-beta to HCS-DEMO Started
JobEntity: JOB_ENTITY_SMARTACCOUNT
entityName: null
status: IN_PROGRESS
isModifiable: true
isDeletable: true
isRestartable: false
isCancelable: false
progressInfo: {Verification=Inprogress, License Mode Change=Not Started, Transport Mode Change=Not Started, Registration=Not Started}
errorDescription: null
recommendedAction: null
```

2. Cluster is eligible:

```
<com.cisco.hcs.hcsagent.message.smartlic.ClusterAssignmentResp>
<messageType>ClusterAssignmentResp</messageType>
<source>
<serviceName>ClusterAssign</serviceName>
<instance>SMART_LIC_CLUSTER_OPERATION</instance>
</source>
<destination>
<serviceName>SDRUI</serviceName>
<instance>HCS-SMARTLIC-LIB0</instance>
</destination>
<sessionID>5fbb89a2-c62b-4d85-b385-3648c8010413</sessionID>
<transactionID>b2e1cfe6-b8fb-462c-a874-374e19afd110</transactionID>
<fault>false</fault>
<Fork>false</Fork>
<requeueCount>0</requeueCount>
<jobId>26</jobId>
<responseCode>PASS</responseCode>
<responseDesc>SmartLicNoError</responseDesc>
<smartLicRespCode defined-in="com.cisco.hcs.hcsagent.message.smartlic.ClusterOperationsResponse">PASS</smartLicRespCode>
<smartLicRespReason defined-in="com.cisco.hcs.hcsagent.message.smartlic.ClusterOperationsResponse">SmartLicNoError</smartLicRespReason>
<smartLicRespCode>PASS</smartLicRespCode>
<smartLicRespReason>SmartLicNoError</smartLicRespReason>
</com.cisco.hcs.hcsagent.message.smartlic.ClusterAssignmentResp>
```

3. HLM changes the product type in CUCM to HCS:

```
2019-06-26 13:17:35,646 DEBUG [33] First pool session created: SDRSyncSession@f11306
2019-06-26 13:17:35,650 INFO [169] UCAppDeploymentModeConnection: Opening secure connection to: https://XXX.YYY.ZZZ:8443/platform-services/services/DeploymentModeService?wsdl
2019-06-26 13:17:35,650 INFO [169] UCAppDeploymentModeConnectionPort successfully opened
2019-06-26 13:17:35,652 DEBUG [33] Pool session created: SDRSyncSession@2cd71b
2019-06-26 13:17:35,659 DEBUG [33] Pool session created: SDRSyncSession@a4e538
2019-06-26 13:17:35,667 DEBUG [33] Pool session created: SDRSyncSession@b3c0d9
2019-06-26 13:17:35,667 INFO [33] Pool is valid. Pool create time in Ms: 1561547855646, poolRunning: false
2019-06-26 13:17:35,667 INFO [33] Created 4 pool sessions.
```

4. HLM instructs the service Cisco HCS provisioning Adapter (CHPA) to assign the cluster into CSSM:

```
2019-06-26 13:17:39,102 DEBUG [169] Agent: sending to [chpa]
-------
<com.cisco.hcs.hcsagent.message.chpa.GetTransportSettingsRequest>
<messageType>GetTransportSettingsRequest</messageType>
<source>
<serviceName>ClusterAssign</serviceName>
</source>
<destination>
<serviceName>chpa</serviceName>
</destination>
<sessionID>getTransport-4</sessionID>
<fault>false</fault>
<Fork>false</Fork>
<requeueCount>0</requeueCount>
<deviceId>
<type>ApplicationInstance</type>
<key class="com.cisco.hcs.sdr.v10_0.KIDInt">
<internalValue>4</internalValue>
</key>
</deviceId>
<clusterName>cl-beta</clusterName>
</com.cisco.hcs.hcsagent.message.chpa.GetTransportSettingsRequest>
---------

2019-06-26 13:17:39,104 DEBUG [169] Agent: Sent message to chpa(null)
2019-06-26 13:17:39,104 INFO [169] UCAppTimerTask , Timer Task started at:Wed Jun 26 13:17:39 CEST 2019
2019-06-26 13:17:39,104 DEBUG [169] com.cisco.hcs.HLM.smartlic.core.clusterops.utils.UCAppTimerRegister , UCApp Timer Task Registered successfully , initial delay ,0 interval , 300000
2019-06-26 13:17:39,104 DEBUG [81655] UCAppTimerTask , Timer Task Attempt of Retry 0
2019-06-26 13:17:39,104 INFO [169] JMS Message is Processed and leaving out from JMS thread
2019-06-26 13:17:44,207 DEBUG [45] KeepAliveConsumerProcessor::process -- enter
2019-06-26 13:17:44,207 DEBUG [94] KeepAliveConsumerProcessor::process -- enter
2019-06-26 13:17:44,208 DEBUG [45] KeepAliveConsumerProcessor::process -- received broadcast message for service sdrcnf
2019-06-26 13:17:44,208 DEBUG [45] noChange -- sdrcnf is Alive
2019-06-26 13:17:44,208 DEBUG [45] KeepAliveMonitor::setExpiresBy:
2019-06-26 13:17:44,208 DEBUG [94] KeepAliveConsumerProcessor::process -- received broadcast message for service sdrcnf
2019-06-26 13:17:44,208 DEBUG [45] now: 26/06/2019 01:17:44.208
2019-06-26 13:17:44,208 DEBUG [94] noChange -- sdrcnf is Alive
2019-06-26 13:17:44,208 DEBUG [45] expected by: 26/06/2019 01:19:44.208
2019-06-26 13:17:44,208 DEBUG [94] KeepAliveMonitor::setExpiresBy:
2019-06-26 13:17:44,208 DEBUG [94] now: 26/06/2019 01:17:44.208
2019-06-26 13:17:44,208 DEBUG [94] expected by: 26/06/2019 01:19:44.208
2019-06-26 13:17:46,105 INFO [36] Perfmon Category in Publish Counter update is Cisco HCS License Manager
2019-06-26 13:17:46,106 DEBUG [36] AgentJmx: JMS connection already up, reusing connection
2019-06-26 13:17:49,420 INFO [63] smartLicAuditProcessor::process enter...
2019-06-26 13:17:50,075 INFO [66] smartLicAuditProcessor::process enter...
```

5.  The cluster assignment is successful:

```
2019-06-26 13:17:50,390 INFO [68] LicUsageAuditProcessor::process enter...
2019-06-26 13:17:52,331 DEBUG [53]
AgentMessageDispatcher -- Received msg by RouteBuilder[ClusterAssign-null] :
---------------
<com.cisco.hcs.hcsagent.message.chpa.GetTransportSettingsResponse>
<messageType>GetTransportSettingsResponse</messageType>
<source>
<serviceName>chpa</serviceName>
<instance>3998890f-ac1c-4ee8-baf8-6b0d2331387b</instance>
</source>
<destination>
<serviceName>ClusterAssign</serviceName>
</destination>
<sessionID>getTransport-4</sessionID>
<fault>false</fault>
<Fork>false</Fork>
<requeueCount>0</requeueCount>
<deviceId>
<type>ApplicationInstance</type>
<key class="com.cisco.hcs.sdr.v10_0.KIDInt">
<internalValue>4</internalValue>
</key>
</deviceId>
<responseCode>PASS</responseCode>
<responseReason>chpaNoError</responseReason>
<clusterName>cl-beta</clusterName>
<mode>HTTP/HTTPS Proxy</mode>
<url></url>
<ipAddress>proxy.esl.cisco.com</ipAddress>
<port>8080</port>
</com.cisco.hcs.hcsagent.message.chpa.GetTransportSettingsResponse>
-

progressInfo: {Verification=Pass, License Mode Change=Not Applicable, Transport Mode Change=Not Applicable, Registration=Pass}
errorDescription: null
recommendedAction: null
jobTypeChanged: true
descriptionChanged: true
JobEntityChanged: true
entityNameChanged: false
statusChanged: true
isModifiableChanged: false
isDeletableChanged: false
isRestartableChanged: false
isCancelableChanged: false
progressInfoChanged: false
errorDescriptionChanged: false
recommendedActionChanged: false
}
```

### Revision History

2.0

26-May-2023

Updating API information.

1.0

27-Aug-2019

Initial Release

### Contributed by Cisco Engineers

Kurt Van De Vel

Cisco TAC

Andrea Cingolani

Cisco TAC

Leonardo Correa

Cisco TAC

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 26-May-2023 | Updating API information. |
| 1.0 | 27-Aug-2019 | Initial Release |