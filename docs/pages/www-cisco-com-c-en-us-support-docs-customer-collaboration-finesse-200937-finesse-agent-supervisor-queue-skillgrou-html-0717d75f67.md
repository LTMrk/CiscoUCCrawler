---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-finesse-200937-finesse-agent-supervisor-queue-skillgrou-html-0717d75f67
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/finesse/200937-Finesse-Agent-Supervisor-Queue-SkillGrou.html
retrieved_at: 2026-08-21T06:43:02.823216+00:00
---

Finesse Agent/Supervisor Queue/SkillGroup Stats Update Problem

# Finesse Agent/Supervisor Queue/SkillGroup Stats Update Problem

Updated: July 24, 2018

Document ID: 200937

Contents

## Contents

## Introduction

This document describes the troubleshooting method for problem identification on Queue or Skillgroup stats update issues observed in Finesse agent desktop environment, specifically caused by message delays between the Computer-Telephony integration (CTI) servers and Finesse servers. The article provides log analyses, and it concludes with a workaround in order to improve the Finesse server capability in handling these Stats Update messages in a sub-optimal delayed network.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Contact Center Enterprise ( UCCE) CTI Server (CTISVR)

- Cisco Finesse server

### Components Used

The information in this document is based on these software and hardware versions:

- UCCE Agent Peripheral Gateway with CTISVR installed

- Finesse Server Cluster

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

### Conventions

Refer to the Cisco Technical Tips Conventions for information on document conventions.

## Background Information

Finesse servers which subscribe to CTISVR as CTI clients, provide agent functions which are similar to what a Computer Telephony Integration Object Server (CTIOS) and a Cisco Agent Desktop (CAD) can offer. Finesse agents/supervisors can also experience some of the problems faced by CTIOS and CAD agents.

One of such problems is Queue or Skillgroup real time stats not updating to the Finesse agent/supervisor desktop. In the CTIOS and CAD environment, engineers usually check the design guidelines and verify if the configuration limits such as skillgroup per agent, total skillgroups per peripherals and teams per supervisor etc. have been over-subscribed.  Engineers would also check the number of concurrent CTI client connections on the CTISVR, Refer to Cisco Unified Contact Center Enterprise Design Guide, Release 10.0(1)

Relevant information can also be referenced from design guides for version 10.5(x), and version 11.

Troubleshooting of this type of problems on Finesse agents/supervisors also starts with the mentioned design limit verifications. However, Finesse agents can be impacted by additional limitations which are exclusively found on Finesse servers.

## Problem Symptoms

Queue or Skillgroup stats not updating issue is typically found in these scenarios:

- Current agent states are not reflected in individual skills/queues gadget on the Finesse agent desktop. However, checking the agent states with the use of opctest with la command on the agent Peripheral Gateway (PG), indicates the agent states are correct with skillgroups.

- Number of agents are in TALKING state for a while, however, Finesse agent or supervisor desktops still show 0 in skills/queues for talking time.

- Restart of Finesse server would allow the system to work temporarily, but usually the same problem resurface within minutes or hours.

## Finesse CTI Messaging and Finesse Queue Stats Buffer

Finesse agent Queue stats or Skill stats updates are carried out through the exchanges of these pairs of request and response CTI messages in Finesse servers.

getQueryQueueStatisticsReq() message request by Finesse and the QuerySkillGroupStatisticsConf message as the result of CTISVR responses.

By default, Finesse can process 751 Skill Group Requests within the designated 10 second stats refresh interval. Requests that are not processed are buffered in a message queue to be processed at a later time. Finesse by default is initialized with this Message Buffer Queue to hold 5000 REQUEST messages.

However, if the buffer fills up and is overwhelmed, some of these queue stats request messages are timed out and dropped.

## Possible Causes for Finesse Queue Stats Buffer Overrun

1. Design/Configuration over-subscription. eg skills per agents, total skillgroups per peripherals and teams per supervisor etc. Refer to Cisco Unified Contact Center Enterprise Design Guide for recommended configuration limits. Over-subscription can lead to excessive CTI messaging on Stats updates, and hence overruns the Finesse Queue Stat Request buffer.

2. Exceeding max allowed concurrent CTI client connection which includes All Events connections and Monitored Mode connections. CTISVR resource depletion which lead to significant slowdown on CTI message processing speed.

3. PG performance eg. CPU, Memory, and Disk I/O etcs..

4. Not enough Network bandwidth in order to support the CTI messaging delays allowed for Finesse Application, i.e 62ms .

Finesse bandwidth calculator provided in the link here with the current design specs in order to allocate the recommended network bandwidth. http://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-technical-reference-list.html

## Finess Queue Stats Buffer Overrun Due to CTI Message Delay

Based on this Finesse limitation on the REQUEST message processing speed and the message buffer, the default value of max average request/response delay is 62ms for average Finesse deployments. If the average delays significantly exceed the benchmark of 62ms, eg. CTI message delay around 100ms. Then buffered getQueryQueueStatisticsReq() CTI messages can never be sent to CTISVR and be responded with QuerySkillGroupStatisticsConf messages fast enough within that 10 second refresh interval. And the remaining timed out getQueryQueueStatisticsReq() messages are dropped from the Queue Stats buffer.

## Relevant Finesse Trace

Queue Stats messages can be found in webservices finesse log. It requires DEBUG trace level to reveal detailed queue stats messages.

For steps to turn up DEBUG trace level for webservices, refer this docwiki link.

http://docwiki.cisco.com/wiki/Logging:_Enable_debug_level_logging

## Log Analyses

### When Queue Buffer Overrun Follows Log Snippets can be Observed from Webservices Log

Look for the beginning of a round of 751 queue stat request update, at the beginning of 10 second refresh interval:

```
eg.
Sep 22 2014 14:34:59.878 -0700: %CCBU_pool-21-thread-1-6-QUEUE_STATISTICS_REQUEST: %[count=751]: Starting new round of querying active queue statistics
```

Between this and the next round of 751 requests which occurs after 10 seconds, filter and verify with a text tool eg. Notepad++, if there are matching 751 QuerySkillGroupStatisticsConf messages:

```
eg
Sep 22 2014 14:34:59.888 -0700: %CCBU_CTIMessageEventExecutor-0-6-DECODED_MESSAGE_FROM_CTI_SERVER: %[cti_message=CTIQuerySkillGroupStatisticsConf[peripheralID=5000, skillGroupNumber=28353, routerCallsQNow=0, longestRouterCallQNow=0, agentsNotReady=0, agentsReady=0, agentsTalkingIn=0, agentsTalkingOut=0, agentsTalkingOther=0, agentsWorkNotReady=0, agentsWorkReady=0]CTIMessageBean [invokeID=112223, msgID=115, timeTracker={"id":"QuerySkillGroupStatisticsConf","CTI_MSG_NOTIFIED":1411536082977,"CTI_MSG_RECEIVED":1411536082976}, msgName=QuerySkillGroupStatisticsConf, deploymentType=CCE]][cti_response_time=1]: Decoded Message to Finesse from backend cti server
```

For example, if there are only 329 QuerySkillGroupStatisticsConf messages processed by Finesse for this round, in another word, there must be 422 messages queued in the buffer. Obviously, if round 400 messages are to be queued every 10 seconds then the buffer can reach its threshold of 5000 messages within 3 minutes.

Search for the first occurrence of polling error that happens within 3 minutes, that is the sign of Buffer Overrun:

```
Sep 22 2014 14:37:29.883 -0700: %CCBU_pool-21-thread-1-3-QUEUE STATISTICS POLLING ERROR: %[ERROR_DESCRIPTION= maximum pool and queue capacity reached so discarding execution][error_message=Thread pool saturated, discarding execution ]: Error during queue statistics polling
```

### Illustration of CTISVR Processing Delay

- Finesse sends getQueryQueueStatisticsReq() request to CTISVR - tracking invokeId=112223, queueId=28353 :

```
Sep 23 2014 22:21:22.875 -0700: %CCBU_pool-19-thread-4-7-CTIWriter.getQueryQueueStatisticsReq():  {Thrd=pool-19-thread-4} params : invokeId=112223, queueId=28353
```

- CTISVR received the request:

```
match InvokeID:0x1b65f with invoked=112223 in the Finesse request

and SkillGroupNumber:28353 with queueId in the Finesse request
```

```
22:21:22:921 cg1A-ctisvr SESSION 9: MsgType:QUERY_SKILL_GROUP_STATISTICS_REQ (InvokeID:0x1b65f PeripheralID:5000
22:21:22:921 cg1A-ctisvr SESSION 9:         SkillGroupNumber:28353 SkillGroupID:N/A )
```

- CTISVR response:

```
22:21:22:999 cg1A-ctisvr SESSION 9: MsgType:QUERY_SKILL_GROUP_STATISTICS_CONF (InvokeID:0x1b65f PeripheralID:5000
22:21:22:999 cg1A-ctisvr SESSION 9:         SkillGroupNumber:28353 SkillGroupID:9431 AgentsLoggedOn:0 AgentsAvail:0 AgentsNotReady:0
22:21:22:999 cg1A-ctisvr SESSION 9:         AgentsReady:0 AgentsTalkingIn:0 AgentsTalkingOut:0 AgentsTalkingOther:0
22:21:22:999 cg1A-ctisvr SESSION 9:         AgentsWorkNotReady:0 AgentsWorkReady:0 AgentsBusyOther:0 AgentsReserved:0 AgentsHold:0
22:21:22:999 cg1A-ctisvr SESSION 9:         AgentsICMAvailable:0 AgentsApplicationAvailable:0 AgentsTalkingAutoOut:0
22:21:22:999 cg1A-ctisvr SESSION 9:         AgentsTalkingPreview:0 AgentsTalkingReservation:0 RouterCallsQNow:0
```

- Finesse received the CTISVR response, and formed QuerySkillGroupStatisticsConf message:

```
Sep 23 2014 22:21:22.977 -0700: %CCBU_CTIMessageEventExecutor-0-6-DECODED_MESSAGE_FROM_CTI_SERVER: %[cti_message=CTIQuerySkillGroupStatisticsConf[peripheralID=5000, skillGroupNumber=28353, routerCallsQNow=0, longestRouterCallQNow=0, agentsNotReady=0, agentsReady=0, agentsTalkingIn=0, agentsTalkingOut=0, agentsTalkingOther=0, agentsWorkNotReady=0, agentsWorkReady=0]CTIMessageBean [invokeID=112223, msgID=115, timeTracker={"id":"QuerySkillGroupStatisticsConf","CTI_MSG_NOTIFIED":1411536082977,"CTI_MSG_RECEIVED":1411536082976}, msgName=QuerySkillGroupStatisticsConf, deploymentType=CCE]][cti_response_time=1]: Decoded Message to Finesse from backend cti server
```

Notice that it took over 100ms seconds for Finesse in order to receive the matching QuerySkillGroupStatisticsConf message, if this is an average response time. Finesse can run into the Buffer Queue Overrun issue.

## Workaround

There is a property in aws.properties which sets the refresh interval on the Finesse server side. This is basically the interval between two rounds of queue stats requests (one round being 751 queue stats requests in this deployment) from Finesse to CTISVR. Finesse by default requests it every 10 seconds. This property could potentially be changed to something higher in value which would mean that Finesse will have a little more time (eg: 20sec instead of 10sec) in order to process one round of queue stats requests. It also effectively extends the benchmark CTI skill stats request/response delay from 62ms to 124ms.

- Obtained root access to the Finesses OS platform

- VI to the property file /opt/cisco/desktop/conf/webservices/aws.properties

- Modified this property value from 10 to 20

```
com.cisco.cc.webservices.reporting.core.queue_statistics_refresh_interval
```

Note : Refresh interval for queue statistics in seconds.

- save aws.properties file

- restart Finesse Tomcat Service

- The same steps are to be carried out on all Finesse nodes within the Finesse cluster

### Revision History

1.0

16-Jan-2017

Initial Release

### Contributed by Cisco Engineers

Tian Lei Xia

Cisco TAC Engineer

### This Document Applies to These Products

- Finesse

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 16-Jan-2017 | Initial Release |