---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-212647-upda-f03c86705b
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/212647-update-unified-im-and-presence-im-p-se.html
retrieved_at: 2026-08-16T23:37:06.893324+00:00
---

Update Unified IM and Presence (IM&P) Server Name From Hostname to Fully Qualified Domain Name (FQDN)

# Update Unified IM and Presence (IM&P) Server Name From Hostname to Fully Qualified Domain Name (FQDN)

### Download Options

Updated: January 16, 2018

Document ID: 212647

Contents

## Contents

## Introduction

This document describes how to change Cisco IM&P hostname to FQDN. There are conditions that you require to change to FQDN in order to the IM&P Certificate Authority (CA) signed certificates to be accepted by Jabber client.

Contributed by Nenos Nicko, Cisco TAC Engineer.

## Q. How to change Cisco IM&P node name from hostname to FQDN

## A.

- If an IM&P publisher is changed, remove it as an intercluster peer on all other clusters.

- Check on the IM&P admin GUI of the publisher node in each cluster to verify if alerts are displayed to restart Cisco XCP Router. If so, restart the XCP router on the nodes specified.

- Navigate to Cisco Unified Communication Manager Administration > System > Presence Redundancy Groups page and disable High Availability on each Cisco Unified Presence sub-cluster.

- Cisco SIP Proxy

- Cisco Presence Engine

- Cisco XCP Text Conference Manager

- Cisco XCP Web Connection Manager

- Cisco XCP Connection Manager

- Cisco XCP SIP Federation Connection Manager

- Cisco XCP XMPP Federation Connection Manager (If Activated)

- Cisco XCP Message Archiver (If Activated)

- Cisco XCP Directory Service (If Activated)

- Cisco XCP File Transfer Manager (If Activated)

- Cisco XCP Authentication Service

- On the Cisco Unified Serviceability > Tools > Control Center - Network Services page and stop Cisco XCP Router service on each Cisco Unified Presence node.

- Modify the Fully Qualified Domain Name/IP Address field from the hostname of the IM&P node to the FQDN of the IM&P node

- Click Save

- Click OK to any warning pop-ups

- Run this command: utils dbreplication reset all

- This can take a period of time before replication is fully established within the cluster again

- To validate if replication is fully established, run this command: utils dbreplication runtimestate

This image shows the output of this command:

- The length of time depends on the amount of data in your database.

- Run utils dbreplication runtimestate continuously , until you see the correct states as outlined in the image.

Note : If replication setup value shows (4), then there are issues on replication which needs further debugging.

- Log in admin CLI on the subscriber node and run utils dbreplication runtimestate continuously until you see the correct states as outlined in the image.

Note : On subscriber nodes, there will be no text such as “Setup Completed” in the final column.

- Value of (2) in all rows for this column indicates completion.

Caution : Do not proceed to the next step until replication is fully established again and shown as completed on all nodes in the cluster.

- Navigate to Cisco Unified Serviceability > Tools > Control Center - Network Services page and start Cisco XCP Router service on each Cisco Unified Presence node.

- Cisco SIP Proxy

- Cisco Presence Engine

- Cisco XCP Text Conference Manager

- Cisco XCP Web Connection Manager

- Cisco XCP Connection Manager

- Cisco XCP SIP Federation Connection Manager

- Cisco XCP XMPP Federation Connection Manager (If Previously Activated)

- Cisco XCP Message Archiver (If Previously Activated)

- Cisco XCP Directory Service (If Previously Activated)

- Cisco XCP File Transfer Manager (If Activated)

- Cisco XCP Authentication Service

- Navigate to Cisco Unified Communication Manager Administration > System > Presence Redundancy Groups page and enable High Availability again on each Cisco Unified Presence sub-cluster.

- Navigate to Presence -> Inter-Clustering page on the publisher node of the other inter-cluster peers and re-add the peer entry for the node you just updated, this time with the new hostname.

- Click Force Manual Sync button

- Ensure Also resync peer's Tomcat certificates is checked

- Click OK

- Wait for the Inter-cluster Peer Status to refresh to see if the Certificate Status is now secure.

The Procedure is now complete. As mentioned in the notes, it can take up to 60 minutes before this change is fully pushed out to nodes on other clusters.

### Contributed by Cisco Engineers

Nenos Nicko

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager IM & Presence Service