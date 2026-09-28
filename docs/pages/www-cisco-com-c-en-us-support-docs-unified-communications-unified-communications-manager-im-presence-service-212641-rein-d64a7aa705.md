---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-212641-rein-d64a7aa705
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/212641-reinstall-procedure-for-im-presence-cl.html
retrieved_at: 2026-08-16T17:54:39.257907+00:00
---

Reinstall IM&P Cluster Nodes Version 10.0 and Later

# Reinstall IM&P Cluster Nodes Version 10.0 and Later

### Download Options

Updated: June 16, 2026

Document ID: 212641

Contents

## Contents

## Introduction

This document describes the options available when required to restore the Cisco Unified Instant Messaging and Presence (IM&P) Publisher and Subscriber nodes.

If you have a Disaster Recovery System (DRS) backup or Contact List backup, you can rebuild the IM&P nodes without the need to restore the entire cluster.

Contributed by Pradeep K Vaka, Feng Gao, and Miguel Castillo, Cisco TAC Engineers.

## Problem

If there is a requirement to restore IM&P Publisher and Subscriber after a rebuild, there are steps to avoid the need to restore the full Cisco Unified Communications Manager (CUCM) and IM&P cluster.

Otherwise, the Cisco Sync Agent service does not start due to the known Cisco bug ID CSCuo02154 .

This solution outlines the steps required to avoid the known problem where the Cisco Sync Agent service fails to start.

## Solution

Note : It is recommended to maintain a DRS backup of the cluster and a copy of exported Contact List from the IM&P server separately.

Option 1. If you do not have a Contact List backup or if you need to restore DRS backup, perform these steps based on your IM&P system version.

a) If your IM&P version is 10.5.2.22900 or later:

- Do not delete IM&P server entries on CUCM ( System > Server ) page.

- Rebuild IM&P Publisher and Subscriber nodes.

- Restore DRS backup of IM&P nodes only.

b) If your IM&P version is earlier than 10.5.2.22900, which does not include the fix for Cisco bug ID CSCuo02154 :

- Do not delete IM&P server entries on CUCM ( System > Server ) page.

- Open a TAC Service Request to perform the workaround on CUCM (via root access) for Cisco bug ID CSCuo02154.

- Rebuild the IM&P Publisher and Subscriber nodes.

- Restore DRS backup of the IM&P nodes only.

Option 2. If you have the Contact List backup and you do not have a good DRS backup to restore, then perform these steps:

- Delete the IM&P server entries on CUCM ( System > Server ) page.

- Re-add the IM&P server entries on CUCM ( System > Server ) page.

- Rebuild the IM&P Publisher and Subscriber nodes.

- Perform the basic integration steps such as activate services, add Presence Gateway, and so on.

- Import the Contact List.

Caution : If you remove the CUCM IM and Presence server entries from CUCM System > Server page and then perform a fresh install of the IM&P nodes, you must restore the DRS backup of the entire cluster (all CUCM and IM&P nodes). If you only restore the IM&P nodes after the fresh install, the database primary keys do not match on CUCM, and the IM&P processnode tables and the Cisco Sync Agent service do not start.

## Considerations

- Navigate to Bulk Administration> Contact List > Export to export the Presence Contact lists.

- Navigate to Bulk Administration> Non-presence Contact List > Export to export the Non-Presence Contact lists.

- The IM&P Publisher cannot be backed up from the IM&P Subscriber node, nor an IM&P Subscriber can be promoted to an IM&P Publisher, meaning, if the IM&P Publisher fails, it requires to be rebuilt.

- If only one node requires to be reinstalled, perform the next steps.

- Step 1. Disable the High Availability. Navigate to CUCM Administration page > System > Presence Redundancy Groups > Click Find > Select the presence redundancy group > Uncheck the High Availability checkbox > Click Save.

- Step 2. Turn off the IM&P Subscriber node.

- Step 3. Reinstall the IM&P Publisher ( Do not remove the Server entries from the CUCM).

- Step 4. After the IM&P Publisher is reinstalled, activate the required services.

- Step 5. Run the DRS restore on the IMP Publisher

- Step 6. Once the DRS restore is complete, restart the IMP Publisher. Wait for services to start .

- Step 7. Turn on the IM&P Subscriber node and validate that all the services are started.

- Step 8. If you would like to validate that the database replication is configured correctly run the command utils dbreplication status , wait some minutes and then run utils dbreplication runtimestate on the CLI of the IM&P Publisher.

- Step 9. If the command shows (-) Not Setup , run the command utils dbreplication rebuild all from the IM&P Publisher's CLI after hours.

- Step 1. Disable the High Availability. Navigate to CUCM Administration page > System > Presence Redundancy Groups > Click Find > Select the presence redundancy group > Uncheck the High Availability checkbox > Click Save.

- Step 2. Reinstall the IM&P Subscriber ( Do not remove the Server entries from the CUCM).

- Step 3. After the IM&P Subscriber is reinstalled, activate the required services and ensure all the services run well.

- Step 4. If you would like to validate that the database replication is configured correctly run the command utils dbreplication status on the IM&P Publisher's CLI.

Note : If the next error is displayed: "Attention: Status command cannot be executed because no active connected replication servers are currently available", run the command utils dbreplication reset all on the IM&P Publisher's CLI and proceed with step 4 after some time to validate if the database has replicated correctly between the nodes.

### Revision History

3.0

16-Jun-2026

Update in the Considerations Section.

2.0

27-Oct-2021

Grammar updates.

1.0

12-Jan-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 16-Jun-2026 | Update in the Considerations Section. |
| 2.0 | 27-Oct-2021 | Grammar updates. |
| 1.0 | 12-Jan-2018 | Initial Release |