---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-217304-trou-481ff5fb2c
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/217304-troubleshooting-services-not-starting-on.html
retrieved_at: 2026-08-21T06:43:40.978643+00:00
---

Troubleshoot Services That Do Not Start on IM&P

# Troubleshoot Services That Do Not Start on IM&P

### Download Options

Updated: June 12, 2025

Document ID: 217304

Contents

## Contents

## Introduction

This document describes the steps to take when a service from the Cisco Instant Message and Presence (IM&P) does not start as expected.

## Background Information

### The States of a Service

The IM&P Services have the next states:

Started

The service is active and running.

Starting

The service is in the transition from Stop to Started.

Stopped

The services are not started, could be because it is stopped manually or it is not activated.

Stopping

The service is in the transition from Started to Stop.

Keep in mind that after a reboot of the IM&P node, the next warning is generated, and can be found either on the Graphic User Interface (GUI) if you navigate to the Notifications page, or via the Command Line Interface (CLI):

The Cisco IM and Presence Data Monitor has detected that database replication is not complete, and/or that the Cisco Sync Agent sync from Cisco Unified Communications Manager is not complete. Some services can remain in the "Starting" state until replication and the Cisco Sync Agent sync are successfully completed.

The message not necessarily means that the services remain in Starting state since the alert is generated. This is expected as the IM&P Data Monitor start to monitor the services as soon as the IM&P comes up from a reboot or boot. The first thing that the Monitor Service detects is that all the main services are in the process of Starting , which triggers the message.

In order to confirm the actual state of the services run the utils service list command.

Note : If the services are in the Started state, feel free to delete the alert to keep the Notification Alerts clean.

## Troubleshoot

### Identify the Problem

The first step to troubleshoot the Services not Starting is to understand which services are the ones not started.

It is important to validate the legend that appears on the right side of the services that are stopped, commonly you can identify:

- Service not activated : This means that the feature service was not activated, and that requires to be done first.

- Commanded out of service : This message appears after a reboot of the server and if HA was not disabled or if certain services were restarted, and that action caused the manual stoppage of other services. In other scenarios, when the network administrator stops manually the service this message is shown. The solution here is to start the services manually either from the GUI or CLI.

- NOTRUNNING :This message is displayed when there is an error with the services and is unable to start. Sometimes this message is seen after the service has been attempted to be started manually. The first attempt is to start the service manually, however, if this action does not work, next troubleshooting steps are required to be performed. Use this guide to help you solve the services not starting.

### Services Remain on STARTING State

One of the most common issues that are found on the IM&P Subscriber after a restart is to see almost all of the services in STARTING state, while the IM&P Publisher shows all the services as STARTED.

The common cause of this behaviour is given by a restart of the IM&P Subscriber when the High Availability (HA) has not been disabled from the Presence Redundancy Groups.

Solution

Step 1. Disable the High Availability from the Presence Redundancy Groups, navigate to CUCM Administration page > System .

Step 2. Run the next command on both IM&P nodes: set replication-sync monitor disable .

Step 3. Wait around 5 minutes and run the next command: utils service list again to confirm that the services are now Started.

Step 4. Verify all the services are STARTED on the subscriber and then run the next command on both IM&P nodes: set replication-sync monitor enable .

Step 5. Re-enable the High Availability from the Presence Redundancy Groups.

### Specific Services Does Not Start

#### Network Services

Although uncommon, there have been scenarios where some network services do not start on the IM&P publisher, these are:

- Cisco Client Profile Agent

- Cisco Extensible Communications Platform (XCP) Router

- Cisco XCP Config Manager

- Cisco Route and Presence Datastores

Warning : The XCP, Presence Engine and SIP Proxy services cannot start, as those are dependant on the Network services listed. This causes that the Instant Message Database (IMDB) does not replicate and the Jabber users to be unable to log in.

#### Solution

The services can be started either via the web interface (Navigate to IM and Presence Serviceability > Tools > Control Center - Network Services > Look for the IM and Presence Services ) or via the Command Line Interface (CLI), use the utils service start <name_of_the_service> command.

Step 1. Disable the High Availability from the Presence Redundancy Groups.

Step 2. Start each service manually strictly in the next order:

- Cisco Client Profile Agent

- Cisco Route Datastore

- Cisco Presence Datastore

- Cisco XCP Config Manager

- Cisco XCP Router

Note : For the Cisco Client Profile Agent to start, the Cisco Tomcat Service requires to be started.

If the previous steps have not worked, a Cisco Technical Assistant Center (TAC) case needs to be opened for further troubleshooting. Keep in mind that the next outputs and logs are required and.

- CLI Outputs:

- show network cluster

- utils dbreplication runtimestate

- utils ha status

- utils core active list

- utils service list

- Logs/ Traces:

- Cisco Syslog Agent

- Event Viewer-Application Log

- Event Viewer-System Log

- Any of the traces from the services that remain stopped

#### Cisco Database (DB)

This is one of the main services within the system.

Warning : If this service does not start, the server cannot access certain features on the Server webpage, Jabber users and their features get compromised, DB replication gets broken.

Causes:

The most common causes identified for this issue are:

- Change of the hostname, IP address or domain without the Cisco Guidelines process.

- Corruption of the files after an ungraceful shutdown of the system.

Solution:

Unfortunately, there are no straight solution steps if this service does not start. The suggestions are:

Step 1. Disable the High Availability from the Presence Redundancy Groups.

Step 2. Restart A Cisco DB R eplicator .

Step 3. Restart A Cisco DB , if it remains in STARTING state, try to stop it and then start it.

The best approach here is to engage Cisco TAC for further investigation, and the next information is required:

- CLI Outputs:

- show tech network hosts

- show tech database dump

- show tech dbintegrity

- utils create report database

- utils network connectivity IM&P_node 1500

- Show network cluster

- utils core active list

- Logs or Traces:

- Cisco Database Layer Monitor

- Cisco Database Library Trace

- Cisco Database Notification Service

- Cisco Database Replicator Trace

- Cisco Informix Database Service

- Cisco Syslog Agent

- Event Viewer-Application Log

- Event Viewer-System Log

#### Cisco Intercluster Sync Agent (ICSA)

Warning : If this service does not start, the IM&P database cannot be synchronized across the IM&P nodes and IM&P clusters (Inter-cluster peering).

Solution:

- The High Availability is in a bad (or wrong) state and it does not allow the service to come up.

Step 1. You need to disable the HA, start the service and then re-enable the HA.

- Cisco bug ID CSCvj09515

- Cisco bug ID CSCvq63308

If the service does not come up, a TAC case needs to be opened for further troubleshooting. Keep in mind that the next outputs and logs are required.

- CLI Outputs

- show network cluster

- utils dbreplication runtimestate

- utils ha status

- utils core active list

- utils service list

- Logs/ Traces

- Cisco Syslog Agent

- Event Viewer-Application Log

- Event Viewer-System Log

- Cisco Service Recovery Manager

- Cisco Intercluster Sync Agent Service

#### Presence Engine

For the Cisco Presence Engine service, there are several variants that must be considered in order to understand why the service does not start and how to make it start.

- Open a CLI and run the command: utils service list validate that the next services are in running state, if they are not, they require to be started first:

- Cisco Presence Datastore

- Cisco SIP Proxy

- Cisco XCP Router

- Cisco Sync Agent

2. The most common reason the Cisco Presence Engine (PE) service does not start in the IM&P Subscriber, is because the IM&P Subscriber has not been added to the presence redundancy group (PRG).

- Reason: The PE service is tied to the PRG and requires to be added to start.

- Solution: Add the server to the PRG and wait around 5 minutes to see if it starts.

- Variants: It is probable that after the previous solution is applied, the PE stops on both IM&P nodes, and the solution is to perform the next steps:

Step 1. Keep the IM&P subscriber in the PRG.

Step 2. Disable High Availability from the PRG.

Step 3. the next steps need to be perofmed on the publisher first and then the subscriber

Step 4. Restart first the Cisco SIP Proxy Service, wait until it starts.

Step 5. Restart the Cisco PE service, wait until it starts.

3. If the IM&P Subscriber is already added into the PRG, and the PE remains in STOPPED or STARTING state, that could be related to a mismatch in the Database Replication between the two IM&P nodes, run the next run sql select * from enterprisde node command. The output of this query displays the id of the node, the subclusterid of the node (which is the PRG id), name or IP address and other values. What you want to focus on, is that both IM&P nodes share the same subclusterid value.

- Reason: If the DB Replication did not perform correctly, the IM&P Subscriber displays the subclusterid as NULL .

- Solution:

Step 1. Run the next command: run sql update enterprisenode set subclesterid= subclesterid_value_as_for_the_IM&P_Pub where id= IM&P_Sub_id

Step 2. Re-run the next command run sql select * from enterprisde node and ensure the subclusterid has the correct value (the same) for both IM&P nodes. The service must start by its own in the next 5 minutes, or you can try to start it manually.

- Recommendation: Open a Cisco TAC case to perform this change.

4. If after the previous troubleshooting has been performed and all services are started, except for the PE:

- Solution:

Step 1. Run the command: set replication-sync monitor disable on both IM&P nodes.

Step 2. Wait around 5 minutes and if not started, attempt to start the service manually, run the next command: utils service start Cisco Presence Engine .

Step 3. Run the command set replication-sync monitor enable .

5. If PE service cannot start yet, validate if the server is running version 12.5, if so it is highly probable to be affected by Cisco bug ID CSCvg94247 .

### Cisco Sync Agent

Warning : If this service does not start, Synchronization of DB Tables from CUCM to IM&P are not completed, this impact mainly the end-user synchronization across the cluster.

Solution: Review the next checklist.

- Verify that both CUCM and IM & Presence nodes are in the same version. If servers are in version 11.X or later, the servers require to run on the same SU version.

- If they are not, ensure that both run the same version.

- Verify that the Cisco AXL Web Service on CUCM is in RUNNING state.

- If it is not, start the Cisco AXL Web Service .

- Verify that the IM&P node is listed in the Server List on CUCM.

- If it is not, a rebuild of the IM&P Server is needed. If server is added back to the server list entry does not take any effect, as a specific ID is generated for every entry added, thus the IM&P remains with an old id.

- Verify within the troubleshooter tests on the CUCM Publisher page on IM&P have passed.

- Verify that the next Uniform Resource Locator (URL) is reachable with the URL: https://CUCM_OR_IM&P_FQDN_OR_IP

- Attempt to reboot the CUCM publisher and then the IM&P Publisher.

- Keep in mind that HA requires to be disabled before reboot.

- Run the next CLI query on the IM&P publisher: run sql select * from epassyncagentcfg .

- Confirm that the ccmpublisherip address displayed is from the CUCM Publisher.

- Run the next query on the CUCM:

run sql select applicationuser.pkid, applicationuser.name , credential.credentials from applicationuser inner join credential on applicationuser.pkid=credential.fkapplicationuser where credential.tkcredential=3 and applicationuser.name='axluser_displayed_from_epassyncagentcfg'

- Validate the next information:

- username (On CUCM) = axluser (On IM&P)

- pkid (On CUCM) = cucm_axluser_pkid (On IM&P)

- credentials (On CUCM) = axlpassword (On IM&P)

- If the axluser in epassyncagentcfg cannot be found in the CUCM user list, then create a new application user on the CUCM side same as the old axluser with the previous password, if known.

If the previous actions do not help to solve the problem, you need to engage Cisco TAC for further troubleshooting. Keep in mind that the next outputs and logs are required.

CLI Outputs (from CUCM Publisher and IM&P):

- Show network cluster

- Utils dbreplication runtimestate

- Utils ha status

- Utils core active list

- Utils service list

- run sql select * from epassyncagentcfg (Only on the IM&P)

- run sql select applicationuser.pkid, applicationuser.name , credential.credentials from applicationuser inner join credential on applicationuser.pkid=credential.fkapplicationuser where credential.tkcredential=3 and applicationuser.name='axluser_displayed_from_epassyncagentcfg' (Only on the CUCM)

Logs/ Traces:

- Cisco Syslog Agent.

- Event Viewer-Application Log.

- Event Viewer-System Log.

- Cisco Sync Agent.

- Cisco AXL Web Service.

### Cisco XCP Config Manager

The Cisco XCP Config Manager is a main service that handles all the XCP componentes within the IM&P Server. Even though most of the XCP services, including the XCP Router is in RUNNING state, this service can be in STOPPED state making the XCP Connection Manager, XCP Web Service Manager to reamained stopped or even failed to synchronize with other servers like the Expressways (for MRA).

First, validate that the Informix Database Replication is in a correct state:

utils dbreplication status

utils dbreplication runtimestate

If everything is fine, then disable the High Availability and attempt the restart of the service, if that fails, disable the synchronization monitoring feature:

set replication-sync monitor disable

And then, attempt the start of the service again. Get the Cisco XCP Config Manager logs either via Real-Time Monitor Tool (RTMT) or CLI:

file view activelog /epas/trace/xcpconfigmgr/log4j/xcpconfigmgr.log

```
And this is the most common scenario:

2024-12-11 14:20:52,650 FATAL [XCPConfigMgr] security.Log4jEncLogger - java.io.FileNotFoundException: /usr/local/platform/.security/CCMEncryption/keys/oldkeys.txt (No such file or directory)
2024-12-11 14:20:52,650 INFO  [XCPConfigMgr] security.Log4jEncLogger - CCMENC::ERROR : decryptPassword - recovery mechanism failed
2024-12-11 14:20:52,650 FATAL [XCPConfigMgr] security.Log4jEncLogger - javax.crypto.BadPaddingException: Error finalising cipher data: pad block corrupted
2024-12-11 14:20:52,195 INFO  [XCPConfigMgr] security.Log4jEncLogger - Entering decryptPassword
2024-12-11 14:20:52,196 INFO  [XCPConfigMgr] security.Log4jEncLogger - Use Dkey to decrypt data
2024-12-11 14:20:52,213 INFO  [Thread-12] dbl.Log4j - Name of appId:dbcli
2024-12-11 14:20:52,216 INFO  [Thread-12] dbl.Log4j - Name of appId:dbxcpconfig
2024-12-11 14:20:52,219 INFO  [Thread-12] dbl.Log4j - Name of appId:dbcli
2024-12-11 14:20:52,221 INFO  [Thread-12] dbl.Log4j - Name of appId:dbxcpconfig
2024-12-11 14:20:52,649 INFO  [XCPConfigMgr] security.Log4jEncLogger - CCMENC::ERROR : Dkey decryption failed. Use recovery mechanism to decrypt data.
2024-12-11 14:20:52,649 INFO  [XCPConfigMgr] security.Log4jEncLogger - Using static key to decrypt data
2024-12-11 14:20:52,650 INFO  [XCPConfigMgr] security.Log4jEncLogger - Exiting decryptPassword.fail
2024-12-11 14:20:52,650 FATAL [XCPConfigMgr] security.Log4jEncLogger - Decryption with static key failed as well. Fatal error javax.crypto.BadPaddingException: Error finalising cipher data: pad block corrupted
2024-12-11 14:20:52,650 INFO  [XCPConfigMgr] security.Log4jEncLogger - CCMENC::ERROR : static key decryption failed. Use old keys to decrypt data
2024-12-11 14:20:52,650 INFO  [XCPConfigMgr] security.Log4jEncLogger - Exiting DecryptPassword.fail. failed to read oldkey file
```

If that is the case, you hit the defect Cisco bug ID CSCur25679 XCP Config Manager and XCP Services not Starting on IM&P and you need to contact Cisco TAC to apply the workaround.

## Feature Services Do Not Start

The next services are disabled by default unless you use the feature of each service:

- Cisco XCP Directory Service

- Cisco XCP File Transfer Manager

- Cisco XCP Message Archives and Cisco XCP XMPP Federation

Even though your IM&P has those services as activated, the services do not start unless you configure each feature for each service.

### Cisco XCP Directory Service

The Cisco XCP Directory Service supports the integration of Extensible Messaging and Presence Protocol (XMPP) clients with the Lightweight Directory Access Protocol (LDAP) directory to allow users to search and add contacts from the LDAP directory.

To start this service:

1. Navigate to Cisco Unified CM IM and Presence Administration > Application > Third-Party Clients .

2. Configure settings for third-party XMPP clients .

You use Cisco XCP Directory Service to allow users of a third-party XMPP client to search and add contacts from the LDAP directory.

For additional information to configure the third-party XMPP directory refer to Turn On Cisco XCP Directory Service.

### Cisco File Transfer Manager

This service allows you to use a server-side file transfer solution called managed file transfer.

Managed File Transfer (MFT) allows an IM and Presence Service client, such as Cisco Jabber to transfer files to other users, ad-hoc group, chats and persistent chat.

The service does not start if the configuration for MFT is not in place.

For additional information to configure the third-party XMPP directory refer to How to configure Managed File Transfer in CUCM CM IM/Presence 10.5?

### Cisco XCP Message Archiver

The Cisco XCP Message Archiver service supports the IM Compliance feature. The IM Compliance feature logs all messages sent to and from the IM and Presence server, that includes point-to-point messages, and messages from ad-hoc (temporary) and permanent chat rooms for the Chat feature. Messages are logged to an external Cisco-supported database.

The service does not start if the configuration for compliance is not in place.

For additional information on how to configure Message Archive refer to Instant Messaging Compliance for the IM and Presence Service, Release 12.5(1).

### Cisco XCP XMPP Federation Connection Manager

The Cisco XCP XMPP Federation Connection Manager supports interdomain federation with third party enterprises such as International Business Machines (IBM) Lotus Sametime, Cisco Webex Meeting Center, GoogleTalk, and another IM and Presence enterprise, over the XMPP protocol.

This service does not start until XMPP federation is configured.

For additional information on how to configure Message Archive refer to Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1) .

## Related Information

- Cisco Technical Support & Downloads

### Revision History

3.0

12-Jun-2025

Recertification, corrected spelling errors, links to open to new page, and Cisco bug ID descriptions.

2.0

11-Jul-2023

Recertification

1.0

16-Aug-2021

Initial Release

| Started | The service is active and running. |
|---|---|
| Starting | The service is in the transition from Stop to Started. |
| Stopped | The services are not started, could be because it is stopped manually or it is not activated. |
| Stopping | The service is in the transition from Started to Stop. |

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 12-Jun-2025 | Recertification, corrected spelling errors, links to open to new page, and Cisco bug ID descriptions. |
| 2.0 | 11-Jul-2023 | Recertification |
| 1.0 | 16-Aug-2021 | Initial Release |