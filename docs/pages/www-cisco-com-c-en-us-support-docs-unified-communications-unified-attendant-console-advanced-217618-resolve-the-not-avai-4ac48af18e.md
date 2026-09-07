---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-advanced-217618-resolve-the-not-avai-4ac48af18e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-advanced/217618-resolve-the-not-available-failover-statu.html
retrieved_at: 2026-09-07T15:48:58.852666+00:00
---

Troubleshoot Not Available Failover Status Error on CUAC Advanced

# Troubleshoot Not Available Failover Status Error on CUAC Advanced

### Download Options

Updated: January 7, 2022

Document ID: 217618

Contents

## Contents

## Introduction

This document describes how to troubleshoot the "Not Available" failover status error on Cisco Unified Attendant Console Advanced (CUAC-A) Advanced.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUAC-A.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The CUAC-A supports high availability on the servers in an active/passive (hot standby) deployment, based on the Structured Query Language ( SQL) Server replication and the synchronization of the database objects across publisher and subscriber servers.

A resilient CUAC-A installation runs on two servers:

- Publisher - Responsible for normal activity. You configure the system when you log in to CUAC-A Administration on the Publisher. By default, all operators that use the Attendant Console client are logged onto the Publisher for configuration and call routing. The Publisher server includes the Lightweight Directory Access Protocol ( LDAP) server.

- Subscriber - The passive, secondary (backup) server. The information from the publisher server is replicated onto this server. The Subscriber runs all the same services as the Publisher except that it does not use an LDAP service to populate the directory, instead this is replicated entirely from the Publisher. If the Publisher fails, the Subscriber takes over, which enables communication with the Attendant Console clients. You cannot change the configuration through the Subscriber server. On the Subscriber you can:

- Set logging levels.

- Monitor replication and run reports.

These components are installed on both server machines:

- BLF server - Responsible for all BLF information and call activity.

- Cisco Unified Presence server - Responsible for presence information.

The two servers are linked via the Apache Active Message Queuing (Active MQ), an open-source message broker. When you update the system and user configuration on the Publisher, all the changes are sent to the Subscriber in real-time. If the Publisher fails, the Attendant Console client applications automatically log out and offer their users the option to continue connected to the Subscriber.

The Apache Active MQ is also used for real-time synchronization of the operator and the queue availability. It also enables the Publisher and Subscriber to detect if the other has failed.

Tip : Refer to the CUAC-A Administration guide for further details.

## Problem

If you log in on the publisher node and navigate to the CUAC-A Administration > Engineering > Service Management , and select the i-button next to the Cisco Unified Attendant Server service on the publisher, this status is seen:

Publisher Failover Status: Normal

Subscriber Failover Status: Not Available

If you log in on the subscriber node and navigate to the CUAC-A Administration > Engineering > Service Management , and select the i-button next to the Cisco Unified Attendant Server service, these messages are seen:

Publisher Failover Status: Not Available

Subscriber Failover Status: Normal

Whenever you see this behavior, it does not mean that the replication is misconfigured, but that there might be an issue with the third-party component Active MQ. As you know, this service links both the publisher and subscriber servers, and it is used for real-time synchronization.

The message “ Not available ” does not mean that there is something wrong, but that the connection between the two nodes is not properly established and they do not know the status of each other.

## Solution

Step 1. Navigate to CUAC-A Administration > Engineering > Service Management and stop all the CUAC-A services.

- Cisco Unified Attendant Server

- Cisco Unified Attendant BLF Plug-in

- Cisco Unified Attendant LDAP Plug-in

- Cisco Unified Attendant Presence Plug-in

Step 2. Access the Windows Server where the CUAC-A server is hosted and, on the Search bar, enter Services .

Step 3. Stop the ActiveMQ service .

Step 4. Locate and rename the C:\Apache\ActiveMQ\data\static-broker2\kahadb directory to a folder called kahadbolddata.

Confirm that no folder with the name kahadb exists within the aforementioned location.

Step 5. Start the ActiveMQ service .

Step 6. Start all the CUAC-A services .

Step 7. Once all the services are started, the kahadb directory is re-created and the ActiveMQ connection is re-established, this allows the system to show the right Failover Status.

Note : This process requires to be performed on both servers, the CUAC-A Publisher and Subscriber.

Tip : For further information, please refer to the Cisco bug ID CSCvx54780.

### Revision History

1.0

07-Jan-2022

Initial Release

### Contributed by Cisco Engineers

Yani Saavedra Chimal

Cisco TAC Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Jan-2022 | Initial Release |