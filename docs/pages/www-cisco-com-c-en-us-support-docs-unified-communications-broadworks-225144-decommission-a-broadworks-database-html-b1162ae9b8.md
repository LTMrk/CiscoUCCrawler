---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-225144-decommission-a-broadworks-database-html-b1162ae9b8
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/225144-decommission-a-broadworks-database.html
retrieved_at: 2026-09-07T13:02:28.905765+00:00
---

Decommission a BroadWorks Database Server

# Decommission a BroadWorks Database Server

### Download Options

Updated: September 29, 2025

Document ID: 225144

Contents

## Contents

## Introduction

This document describes the steps to decommission a Cisco BroadWorks Database Server (DBS).

## Prerequisites

Before initiating the decommissioning process, ensure that these prerequisites are met:

- A dedicated maintenance window has been scheduled.

- All servers have been backed up before the maintenance window.

- Open a Cisco TAC ticket and provide complete tech-support outputs from all relevant BroadWorks servers before the maintenance window.

## Warning

This process must be completed during a scheduled Maintenance Window to minimize service disruption.

Be aware that BroadWorks Command Line Interface (bwcli) levels can vary between releases. Always verify commands against your specific BroadWorks release documentation.

Decommissioning a DBS involves permanent deletion of data. Ensure all necessary historical data has been archived or migrated before proceeding.

## PS/ADP Server CLI Cleanup

If the Profile Server (PS) or Application Delivery Platform (ADP) servers are dedicated only to the DBS, the decommission is simple but often the PS/ADP servers share other functions and only the DBS functions need be removed.

#### DBS-Dedicated Servers

If the PS/ADP Servers are dedicated solely to DBS services, you can proceed with their shutdown and eventual deletion.

- Initiate a graceful shutdown of the dedicated PS/ADP Servers.

- After a retention period, delete the dedicated PS/ADP Server Virtual Machines (VMs).

#### Non-DBS-Dedicated Servers

For PS Servers that are not dedicated to DBS services, remove all relevant information using delete and/or clear commands from these CLI locations.

Enhanced Call Center Reporting (ECCR):

```
_CLI/Applications/CCReportingDBManagement/Database/Databases/Sites> _CLI/Applications/CCReportingDBManagement/Database/Schemas/Instances> _CLI/Applications/CCReportingDBManagement/Database/Databases> _CLI/Applications/CCReporting/Database/Databases/Sites> _CLI/Applications/CCReporting/Database/Schemas/Instances> _CLI/Applications/CCReporting/Database/Databases>
```

Enhanced Call Logs (ECL):

```
_CLI/Applications/EnhancedCallLogsDBManagement/Database/Databases/Sites> _CLI/Applications/EnhancedCallLogsDBManagement/Database/Schemas/Instances> _CLI/Applications/EnhancedCallLogsDBManagement/Database/Databases>
```

On the PS/PS-ADP Servers, execute the necessary commands to stop , undeploy , and deactivate the relevant applications:

ECCR:

- CCReportingDBManagement

- CCReporting

- DBSObserver

ECL:

- EnhancedCallLogsDBManagement

- ECLQuery

## CommPilot Cleanup for External Reporting

Clean up the CommPilot GUI and point users to the built-in AS Reporting instead of the decommissioned DBS.

Instruct a designated admin user to log into the CommPilot GUI and navigate to each SP/Enterprise/Group to disable External Reporting with the check-box under Profile for each Call Center.

Additionally, there is an area called "Call Center External Reporting Settings", set the Radio Button to "Off".

## AS CLI Cleanup

Settings applied to the primary Application Server (AS) replicate over to the secondary AS in a redundant pair.

Remove all relevant information from these CLI locations on the primary AS:

```
AS_CLI/Applications/ExecutionAndProvisioning/XS/Database/DBS/Databases> AS_CLI/Applications/ExecutionAndProvisioning/XS/Database/DBS/Databases/Sites> AS_CLI/Applications/ExecutionAndProvisioning/XS/Database/DBS/Schemas> AS_CLI/Applications/ExecutionAndProvisioning/XS/Database/DBS/Schemas/Instances> AS_CLI/Applications/ExecutionAndProvisioning/PS/Database/DBS/Databases> AS_CLI/Applications/ExecutionAndProvisioning/PS/Database/DBS/Databases/Sites> AS_CLI/Applications/ExecutionAndProvisioning/PS/Database/DBS/Schemas> AS_CLI/Applications/ExecutionAndProvisioning/PS/Database/DBS/Schemas/Instances>
```

On both AS servers, clear the Alarms Table using the command:

```
AS_CLI/Monitoring/Alarm/AlarmsTable> clearAll;y
```

## XSP/ADP Server Application Cleanup

Execute the necessary commands on ALL Xtended Services Platform (XSP)/ADP servers to stop , undeploy , and deactivate the relevant applications:

- PublicReporting

- PublicECLQuery

## DBS Decommissioning

Remove all entries related to the DBS from the hosts files on all BroadWorks servers (AS, PS, XSP, ADP) that previously referenced it.

Initiate a graceful shutdown of the DBS Server(s) using the command:

```
init 0 shutdown
```

After a retention period, delete the DBS Virtual Machines (VMs).

## Troubleshooting

If you get either of these errors when deleteing the schema, the schema must be manually detached.

```
AS_CLI/Applications/ExecutionAndProvisioning/XS/Database/DBS/Databases> delete bwCentralizedDb Failed to write data to the configuration system The database bwCentralizedDb refer to by schema type bweccr and schema instance bweccr does not exist or cannot be deleted.
```

Or

```
AS_CLI/Applications/ExecutionAndProvisioning/XS/Database/DBS/Databases> delete bwCentralizedDb Cannot delete schema. Connections are currently open.
```

Detach the schema.

```
AS_CLI/Applications/ExecutionAndProvisioning/XS/Database/DBS/Schemas/Instances> clear bweccr bweccr database
```

Once the schema is detached, execute the delete command again.

```
AS_CLI/Applications/ExecutionAndProvisioning/XS/Database/DBS/Databases> delete bwCentralizedDb
```

If the deletion of the bwCentralizedDb entry fails again, re-set the port on the DBS and retry the delete command again.

```
DBS_CLI/Applications/DbManagement/DbManager/Ports> set OracleNet 8523
```

### Revision History

1.0

06-Oct-2025

Initial Release

### Contributed by Cisco Engineers

Mike Dibert

Customer Delivery Leader

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 06-Oct-2025 | Initial Release |