---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-212298-cisco-meeting-server-acano-tms-integ-html-cf8b59a93c
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/212298-cisco-meeting-server-acano-tms-integ.html
retrieved_at: 2026-08-21T06:28:44.217081+00:00
---

Cisco Meeting Server (Acano) / TMS Integration and Scheduling API Guide

# Cisco Meeting Server (Acano) / TMS Integration and Scheduling API Guide

### Download Options

Updated: October 18, 2017

Document ID: 212298

Contents

## Contents

## Introduction

This document describes how the CMS 2.0 (Acano) server integrates and communicates with TMS (15.3) as a managed resource.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Basic understanding of TMS (Cisco TelePresence Management Suite)

- CMS (Cisco Meeting Server, former Acano) concepts

### Components Used

The information in this document is based on these software and hardware versions:

- TMS 15.3 or greater

- CMS 2.0 or greater

Note : Prior to TMS 15.3 you were able to add an Acano server as an unmanaged bridge, but it did not have full functionality.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

To add a managed CMS server into TMS is relatively simple and works in a similar way to add a MCU or TPS.

Step 1. Navigate to the desired navigator location and select Add Device , as usual. If a non-standard port is being used for the webadmin service (such as 445), ensure it is appended to the end of the IP address when adding it, with x.x.x.x:445 for example.

- After you add the device, you see the system added with warnings. It must be detected as a Cisco Meeting Server for type but it does not have a system name (this is normal):

- Viewing the info page will show two errors/warnings:

Step 2. Set a system name under Settings > Edit Settings . This can be any name, the TMS uses it to refer to the bridge as.

Step 3. Address the other message by navigating to Settings > Extended Settings and configure the domain and conference ID range. The domain is used to form URIs based on the conference number, so make sure to assign a domain that is routable to the CMS in the network (and has the proper inbound dial rules configured on CMS).

Step 4. After making these configuration changes, the CMS must be free of errors or warnings in TMS.

Step 5. To verify everything has been properly configured, you can check on CMS to make sure the proper meeting slots have been allocated as spaces. TMS creates a space for each meeting slot titled TMS_Scheduled_Meeting_x where x is the meeting number within the range that was specified.

TMS automatically detects any other callbridges clustered with the CMS that were added via the API. It can be confirmed if this is correct when you navigate to the Clustering tab.

Note : It is important to note that this does not mean TMS automatically fails over to this callbridge in the event the primary one that was added goes down. In its current state, it does not ever talk directly with anything other than the added CMS server, but discovers the others via API GET for callbridges (each callbridge knows about all others).

Step 6. In order to configure failover, you have to navigate back to the Edit Settings page for the CMS on TMS. Under Network Settings configure the alternate IP, username, and password. The Alternate IP field must have a dropdown automatically populated by other callbridges detected in the cluster. TMS only fails over to the specified callbridge. If there are more than two callbridges in the cluster, TMS cannot use the others. This is only for future meetings. If a callbridge goes down mid conference, TMS does not migrate the users over to the alternate.

There is no need to manually add other clustered callbridges into TMS. If you try to add one TMS has already detected as part of the cluster, you get an error.

TMS is now ready to schedule meetings on the CMS. If there are multple bridge types added to TMS, the CMS can be assigned under u nder Administrator Tools > General Settings > Conference Settings , where the Prefer MCU Type in Routing field can be set to Cisco Meeting Server .

## Verify

### API Communication

The following are examples of API communication between TMS and CMS, pulled from the CMS log file with API debug logging enabled.

#### Adding CMS to TMS

TMS reaches out and runs GET methods to pull basic information from CMS. The output below shows the process of running a GET for callbridges, then a GET for each specific callbridge returned, and pulls additional information such as the IP. This is how TMS discovers other servers in the cluster. It also creates a call profile and call leg profile for meetings.

```
ul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889: GET for "/api/v1/system/status" (from 14.80.99.226) Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889: sending 200 response, size 518
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  <status>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  <softwareVersion>2.0(RC)</softwareVersion>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  <uptimeSeconds>333717</uptimeSeconds>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  <cdrTime>2016-07-26T14:08:19Z</cdrTime>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  <activated>true</activated>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  <clusterEnabled>true</clusterEnabled>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  <callLegsActive>0</callLegsActive>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  <callLegsMaxActive>3</callLegsMaxActive>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:    [ ... ]
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8889:  </status>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890: GET for "/api/v1/callBridges" (from 14.80.99.226) Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890: sending 200 response, size 250
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890:  <callBridges total="2">
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890:  <callBridge id="0e3758db-b9b8-49df-a74c-55fa05e3e21d">
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890:  <name>CallBridge-Core1</name>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890:  </callBridge>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890:  <callBridge id="cfe31846-ca57-4703-9e11-da3e72a13066">
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890:  <name>CallBridge-Core2</name>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890:  </callBridge>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8890:  </callBridges>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8891: GET for "/api/v1/callBridges/0e3758db-b9b8-49df-a74c-55fa05e3e21d" (from 14.80.99.226) Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8891: sending 200 response, size 178
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8891:  <callBridge id="0e3758db-b9b8-49df-a74c-55fa05e3e21d">
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8891:  <name>CallBridge-Core1</name>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8891:  <address>https://14.80.82.30</address>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8891:  <sipDomain></sipDomain>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8891:  </callBridge>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8892: GET for "/api/v1/callBridges/cfe31846-ca57-4703-9e11-da3e72a13066" (from 14.80.99.226) Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8892: sending 200 response, size 178
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8892:  <callBridge id="cfe31846-ca57-4703-9e11-da3e72a13066">
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8892:  <name>CallBridge-Core2</name>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8892:  <address>https://14.80.82.31</address>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8892:  <sipDomain></sipDomain>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8892:  </callBridge>
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8893: POST for "/api/v1/callProfiles" (from 14.80.99.226) Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8893: content data size 47, type "application/x-www-form-urlencoded":
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8893:  participantLimit=1000&
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8893:  messageBoardEnabled=false
Jul 26 14:08:23 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" created new call profile 1285fa9c-f221-4af7-8462-51cf1d7542eb
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8893: sending 200 response, size 0
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8893: Location: /api/v1/callProfiles/1285fa9c-f221-4af7-8462-51cf1d7542eb
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894: POST for "/api/v1/callLegProfiles" (from 14.80.99.226) Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894: content data size 167, type "application/x-www-form-urlencoded":
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894:  defaultLayout=telepresence&
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894:  changeLayoutAllowed=true&
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894:  presentationContributionAllowed=true&
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894:  presentationViewingAllowed=true&
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894:  muteSelfAllowed=true&
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894:  videoMuteSelfAllowed=true
Jul 26 14:08:23 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" created new call leg profile 734447d1-4251-442f-b127-ab3304b643f8
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894: sending 200 response, size 0
Jul 26 14:08:23 user.info Core1 host:server:  INFO : API trace 8894: Location: /api/v1/callLegProfiles/734447d1-4251-442f-b127-ab3304b643f8
```

#### Create Reserved Conference Spaces

In the example below TMS creates a CoSpace Bulk Parameter Set which includes information for the start and number of the meeting IDs, a name mapping which defines the name of each meeting instance, the call profile and call leg profile created in the previous section, and the nonMemberAccess " field set to false, which prevents users from joining any of these spaces.

Next TMS does a POST for sospaceBulkSyncs which references and runes the previously created parameter set. After that, it does a GET for the ID of the bulk sync it just ran to confirm the process has been completed.

Finally TMS runs GET status to again confirm basic connection information.

```
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954: POST for "/api/v1/cospaceBulkParameterSets" (from 14.80.99.226) Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954: content data size 250, type "application/x-www-form-urlencoded":
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:  startIndex=1&
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:  endIndex=5&
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:  coSpaceUriMapping=&
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:  coSpaceNameMapping=TMS_Scheduled_Meeting_
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:      &
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:  coSpaceCallIdMapping=&
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:  callProfile= 1285fa9c-f221-4af7-8462-51cf1d7542eb Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:      &
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:  callLegProfile=734447d1-4251-442f-b127-ab3304b64
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:      3f8&
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954:  nonMemberAccess=false
Jul 26 14:12:31 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" created new object type 29 beac931c-ae88-4f5f-b6b7-71a1c4bdaf8e
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954: sending 200 response, size 0
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8954: Location: /api/v1/cospaceBulkParameterSets/beac931c-ae88-4f5f-b6b7-71a1c4bdaf8e
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8955: POST for "/api/v1/cospaceBulkSyncs" (from 14.80.99.226) Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8955: content data size 60, type "application/x-www-form-urlencoded":
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8955:  cospaceBulkParameterSet=beac931c-ae88-4f5f-b6b7-
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8955:      71a1c4bdaf8e
Jul 26 14:12:31 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" created new object type 30 071e7bf5-c0d8-4d2a-b321-7b07c799829c
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8955: sending 200 response, size 0
Jul 26 14:12:31 user.info Core1 host:server:  INFO : API trace 8955: Location: /api/v1/cospaceBulkSyncs/071e7bf5-c0d8-4d2a-b321-7b07c799829c
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8956: GET for "/api/v1/cospaceBulkSyncs/071e7bf5-c0d8-4d2a-b321-7b07c799829c" (from 14.80.99.226) Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8956: sending 200 response, size 210
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8956:  <cospaceBulkSync id="071e7bf5-c0d8-4d2a-b321-7b07c799829c">
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8956:  <cospaceBulkParameterSet>beac931c-ae88-4f5f-b6b7-71a1c4bdaf8e</cospaceBulkParameterSet>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8956:  <status>complete</status>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8956:  </cospaceBulkSync>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957: GET for "/api/v1/system/status" (from 14.80.99.226) Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957: sending 200 response, size 518
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  <status>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  <softwareVersion>2.0(RC)</softwareVersion>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  <uptimeSeconds>333966</uptimeSeconds>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  <cdrTime>2016-07-26T14:12:29Z</cdrTime>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  <activated>true</activated>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  <clusterEnabled>true</clusterEnabled>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  <callLegsActive>0</callLegsActive>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  <callLegsMaxActive>3</callLegsMaxActive>
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:    [ ... ]
Jul 26 14:12:33 user.info Core1 host:server:  INFO : API trace 8957:  </status>
```

#### Create a Scheduled Conference and Auto Dialing

When it is time for a meeting to start, TMS first does a GET for the status and for participants (not sure what the results of participants are used for at this time). Next, TMS does a GET for coSpaces to see which ones are actually in use. TMS selects the lowest conference in the range that is not currently in use for a scheduled session (in other words, if there is only ever one conference at a time, TMS always uses TMS_Scheduled_Meeting_1).

After identifying the meeting to use, TMS does a PUT to the ID of that specific Space, changes the name and nonMemberAccess permission field, which then allows others to join the conference. TMS also creates a call instance within that space to allow for dial control.

Next TMS does a GET for status, coSpaces, and calls to check the created instances. If CMS is set to automatically dial to any participants in the conference, TMS then does a GET for calllegs. In order to initiate the new call to an endpoint, TMS then does a POST to the specific call instance created previously creating a new callleg. In the content for this POST it includes the URI of the endpoint to dial in the remoteParty " content field.

Any calls initiated in this method will rely on the outbound dial rules on the CMS, so they must be properly configured.

```
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496: GET for "/api/v1/system/status" (from 14.80.99.226) Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496: sending 200 response, size 518
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  <status>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  <softwareVersion>2.0(RC)</softwareVersion>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  <uptimeSeconds>351847</uptimeSeconds>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  <cdrTime>2016-07-26T19:10:30Z</cdrTime>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  <activated>true</activated>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  <clusterEnabled>true</clusterEnabled>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  <callLegsActive>0</callLegsActive>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  <callLegsMaxActive>3</callLegsMaxActive>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:    [ ... ]
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9496:  </status>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9497: GET for "/api/v1/participants" (from 14.80.99.226) Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9498: GET for "/api/v1/coSpaces" (from 14.80.99.226) Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9498: sending 401 response, size 0
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9498: WWW-Authenticate: Basic realm="acano"
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9497: sending 200 response, size 60
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9497:  <participants total="0"></participants>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499: GET for "/api/v1/coSpaces" (from 14.80.99.226) Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499: sending 200 response, size 788
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  <coSpaces total="4">
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  <coSpace id="2be23a10-f400-4436-baef-6058f55ca688">
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  <name>Cool Bridge Space</name>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  <autoGenerated>false</autoGenerated>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  <uri>cool.bridge.space</uri>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  <callId>497540167</callId>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  </coSpace>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  <coSpace id="f4c9601b-300e-43ac-a283-3e1a00699c2c">
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:    [ ... ]
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9499:  </coSpaces>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9500: PUT for "/api/v1/cospaces/458075bc-6def-4052-8ed6-b1192d6e6b35" (from 14.80.99.226) Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9500: content data size 117, type "application/x-www-form-urlencoded":
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9500:  &
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9500:  nonMemberAccess=true&
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9500:  passcode=********
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9500:  name=Tim Kratzke Acano TMSXE Test Meeting&
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9500:  secret=86db1bdd-5cf7-4ea8-b88d-479195f4701a
Jul 26 19:10:34 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" modified space 458075bc-6def-4052-8ed6-b1192d6e6b35 (Tim Kratzke Acano TMSXE Test Meeting)
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9500: sending 200 response, size 0
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9501: POST for "/api/v1/calls" (from 14.80.99.226) Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9501: content data size 44, type "application/x-www-form-urlencoded":
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9501:  coSpace=458075bc-6def-4052-8ed6-b1192d6e6b35
Jul 26 19:10:34 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" created new call ce5ee392-7be6-4227-a7ee-b4f16a5fdd16
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9501: sending 200 response, size 0
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9501: Location: /api/v1/calls/ce5ee392-7be6-4227-a7ee-b4f16a5fdd16
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502: GET for "/api/v1/system/status" (from 14.80.99.226) Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502: sending 200 response, size 518
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  <status>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  <softwareVersion>2.0(RC)</softwareVersion>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  <uptimeSeconds>351848</uptimeSeconds>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  <cdrTime>2016-07-26T19:10:30Z</cdrTime>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  <activated>true</activated>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  <clusterEnabled>true</clusterEnabled>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  <callLegsActive>0</callLegsActive>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  <callLegsMaxActive>3</callLegsMaxActive>
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:    [ ... ]
Jul 26 19:10:34 user.info Core1 host:server:  INFO : API trace 9502:  </status>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503: GET for "/api/v1/coSpaces" (from 14.80.99.226) Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503: sending 200 response, size 801
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  <coSpaces total="4">
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  <coSpace id="2be23a10-f400-4436-baef-6058f55ca688">
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  <name>Cool Bridge Space</name>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  <autoGenerated>false</autoGenerated>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  <uri>cool.bridge.space</uri>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  <callId>497540167</callId>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  </coSpace>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  <coSpace id="f4c9601b-300e-43ac-a283-3e1a00699c2c">
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:    [ ... ]
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9503:  </coSpaces>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504: GET for "/api/v1/calls" (from 14.80.99.226) Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504: sending 200 response, size 253
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504:  <calls total="1">
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504:  <call id="ce5ee392-7be6-4227-a7ee-b4f16a5fdd16">
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504:  <name>Tim Kratzke Acano TMSXE Test Meeting</name>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504:  <coSpace>458075bc-6def-4052-8ed6-b1192d6e6b35</coSpace>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504:  <callCorrelator>76331036-6887-4d88-87ea-2a24a2f585d4</callCorrelator>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504:  </call>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9504:  </calls>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9505: GET for "/api/v1/calllegs" (from 14.80.99.226) Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9505: sending 200 response, size 52
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9505:  <callLegs total="0"></callLegs>
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9506: POST for "/api/v1/calls/ce5ee392-7be6-4227-a7ee-b4f16a5fdd16/calllegs" (from 14.80.99.226) Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9506: content data size 36, type "application/x-www-form-urlencoded":
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9506:  remoteParty=desk.ex90@tkratzke.local
Jul 26 19:10:35 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" created new call leg 9f003b66-0539-4513-b609-ed0d93d09781, call ce5ee392-7be6-4227-a7ee-b4f16a5fdd16
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9506: sending 200 response, size 0
Jul 26 19:10:35 user.info Core1 host:server:  INFO : API trace 9506: Location: /api/v1/callLegs/9f003b66-0539-4513-b609-ed0d93d09781
Jul 26 19:10:35 user.info Core1 host:server:  INFO : call 7: outgoing SIP call to "desk.ex90@tkratzke.local" from space "Tim Kratzke Acano TMSXE Test Meeting"
Jul 26 19:10:35 user.info Core1 host:server:  INFO : handshake error 104 on outgoing connection 4
Jul 26 19:10:35 user.info Core1 host:server:  INFO : call 7: falling back to unencrypted control connection...
Jul 26 19:10:35 user.info Core1 host:server:  INFO : call 7: SIP call ringing
Jul 26 19:10:35 local0.info Core1 host:server:  INFO : participant "desk.ex90@tkratzke.local" joined space 458075bc-6def-4052-8ed6-b1192d6e6b35 (Tim Kratzke Acano TMSXE Test Meeting)
Jul 26 19:10:37 user.info Core1 host:server:  INFO : conference "Tim Kratzke Acano TMSXE Test Meeting": unencrypted call legs now present
```

#### Extend a Conference

When you extend a meeting, TMS simply does a PUT to the specific space again with the same content fields as when it was created. There is no parameter for a space timeout used in this case, so this API command does not really keep the meeting "alive", but it does serve as a reference to know the meeting was extended from the CMS side.

```
Jul 26 19:35:04 user.info Core1 host:server:  INFO : API trace 9711: PUT for "/api/v1/cospaces/458075bc-6def-4052-8ed6-b1192d6e6b35" (from 14.80.99.226) Jul 26 19:35:04 user.info Core1 host:server:  INFO : API trace 9711: content data size 117, type "application/x-www-form-urlencoded":
Jul 26 19:35:04 user.info Core1 host:server:  INFO : API trace 9711:  &
Jul 26 19:35:04 user.info Core1 host:server:  INFO : API trace 9711:  nonMemberAccess=true&
Jul 26 19:35:04 user.info Core1 host:server:  INFO : API trace 9711:  passcode=********
Jul 26 19:35:04 user.info Core1 host:server:  INFO : API trace 9711:  name=Tim Kratzke Acano TMSXE Test Meeting&
Jul 26 19:35:04 user.info Core1 host:server:  INFO : API trace 9711:  secret=86db1bdd-5cf7-4ea8-b88d-479195f4701a
Jul 26 19:35:04 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" modified space 458075bc-6def-4052-8ed6-b1192d6e6b35 (Tim Kratzke Acano TMSXE Test Meeting)
Jul 26 19:35:04 user.info Core1 host:server:  INFO : API trace 9711: sending 200 response, size 0
Jul 26 19:35:10 user.info Core1 authp:  re-registration from server "callbridge-core2.acanolab2.tkratzke.local"
```

#### End/Remove a Conference

When a conference is ended, TMS again goes through a variety of status checks via GET commands before performing any actions. Next, TMS does a PUT to the space corresponding to the meeting that is ending and changes the name back to its placeholder value and sets nonMemberAccess " back to false so users and endpoints can no longer join.

Finally, TMS sends a DELETE for the call instance it created within the space.

```
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874: GET for "/api/v1/system/status" (from 14.80.99.226) Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874: sending 200 response, size 518
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  <status>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  <softwareVersion>2.0(RC)</softwareVersion>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  <uptimeSeconds>354538</uptimeSeconds>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  <cdrTime>2016-07-26T19:55:21Z</cdrTime>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  <activated>true</activated>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  <clusterEnabled>true</clusterEnabled>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  <callLegsActive>0</callLegsActive>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  <callLegsMaxActive>3</callLegsMaxActive>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:    [ ... ]
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9874:  </status>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875: GET for "/api/v1/coSpaces" (from 14.80.99.226) Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875: sending 200 response, size 801
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  <coSpaces total="4">
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  <coSpace id="2be23a10-f400-4436-baef-6058f55ca688">
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  <name>Cool Bridge Space</name>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  <autoGenerated>false</autoGenerated>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  <uri>cool.bridge.space</uri>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  <callId>497540167</callId>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  </coSpace>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  <coSpace id="f4c9601b-300e-43ac-a283-3e1a00699c2c">
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:    [ ... ]
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9875:  </coSpaces>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876: GET for "/api/v1/calls" (from 14.80.99.226) Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876: sending 200 response, size 253
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876:  <calls total="1">
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876:  <call id="ce5ee392-7be6-4227-a7ee-b4f16a5fdd16">
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876:  <name>Tim Kratzke Acano TMSXE Test Meeting</name>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876:  <coSpace>458075bc-6def-4052-8ed6-b1192d6e6b35</coSpace>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876:  <callCorrelator>76331036-6887-4d88-87ea-2a24a2f585d4</callCorrelator>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876:  </call>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9876:  </calls>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877: GET for "/api/v1/coSpaces" (from 14.80.99.226) Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877: sending 200 response, size 801
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  <coSpaces total="4">
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  <coSpace id="2be23a10-f400-4436-baef-6058f55ca688">
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  <name>Cool Bridge Space</name>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  <autoGenerated>false</autoGenerated>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  <uri>cool.bridge.space</uri>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  <callId>497540167</callId>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  </coSpace>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  <coSpace id="f4c9601b-300e-43ac-a283-3e1a00699c2c">
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:    [ ... ]
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9877:  </coSpaces>
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9878: PUT for "/api/v1/cospaces/458075bc-6def-4052-8ed6-b1192d6e6b35" (from 14.80.99.226) Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9878: content data size 83, type "application/x-www-form-urlencoded":
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9878:  &
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9878:  nonMemberAccess=false&
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9878:  passcode=********
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9878:  name=TMS_Scheduled_Meeting_1&
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9878:  regenerateSecret=true
Jul 26 19:55:25 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" modified space 458075bc-6def-4052-8ed6-b1192d6e6b35 (TMS_Scheduled_Meeting_1)
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9878: sending 200 response, size 0
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9879: DELETE for "/api/v1/calls/ce5ee392-7be6-4227-a7ee-b4f16a5fdd16" (from 14.80.99.226) Jul 26 19:55:25 local0.info Core1 host:server:  INFO : 14.80.99.226: API user "admin" deleted call ce5ee392-7be6-4227-a7ee-b4f16a5fdd16
Jul 26 19:55:25 user.info Core1 host:server:  INFO : API trace 9879: sending 200 response, size 0
```

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Tim Kratzke

Cisco TAC Engineer

Edited by Lidiya Bogdanova

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server

- TelePresence Management Suite (TMS)