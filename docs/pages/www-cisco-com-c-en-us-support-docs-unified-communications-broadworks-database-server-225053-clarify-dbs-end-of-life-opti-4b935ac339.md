---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-database-server-225053-clarify-dbs-end-of-life-opti-4b935ac339
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks-database-server/225053-clarify-dbs-end-of-life-options.html
retrieved_at: 2026-09-07T13:01:00.572223+00:00
---

Clarify DBS End of Life Options

# Clarify DBS End of Life Options

### Download Options

Updated: September 25, 2025

Document ID: 225053

Contents

## Contents

## Introduction

This document describes options for the BroadWorks Database Server (DBS) after final release 2024.09.

## End of Maintenance

The BroadWorks Database Server (DBS) and Enhanced Call Center Reporting (ECCR) entered End Of Maintenance (EoM) on Sep 30th, 2024 . The last version available of the DBS is 2024.09. The ECCR and ECL applications for the DBS are also end of life and are no longer receiving updates (refer to Release 2024.10_1.260 in the Application Release Notes 😞

- CCReporting

- CCReportingDBManagement

- CCReportingRepository

- DBSObserver

- EnhancedCallLogsDBManagement

Additionally, the final version of the PublicReporting application, typically be deployed on the XSP, was published 2025.02.

## Replace the DBS and ECCR

The ECCR feature and the DBS have been replaced by Call Center Event Recording (CCER). To use CCER a third party reporting and database solution must be implemented and the ECCR configuration removed. With ECCR, the Application Server (AS) provided the data as a JSON and send it to a third party database solution. To use CCER, BroadWorks must be running release 22.0 or later.

Enable the CCER feature under this directory:

```
AS_CLI/Service/CallCenter/EnhancedReporting>
```

Files on the AS appear at this location:

```
/var/broadworks/ccEventRecording/
```

Refer to the CCER Feature Description for more information.

## Upgrade the DBS

Upgrading the DBS is no longer recommended, instead it is recommended to decommission the DBS. However, if you must upgrade the DBS, you must understand how the OS version impacts the upgrade path. The Software Compatibility Matrix makes it appear that the DBS is easier to upgrade than it is.

This table shows the BroadWorks DBS release as it corresponds to the supported OS:

R21: Linux 5, 6 R22: Linux 5.9+, 6.5+ 2018.11 to 2020.08 : Linux 6.5+, 7 2020.11+: Linux 7.5+ only 2022.07+: Linux 7.5+, 8.5+ 2024.07+: Linux 8 only 2024.09: Last Release, DBS End of Maintenance

For example, a DBS running on Linux 6.5 on release 22.0 first needs to upgrade to 2020.08. Then, it must be swapped to hardware running Linux 7. The DBS can then be upgraded to 2024.06 (the last version of the DBS to support Linux 7). Then the DBS must hardware swap to Linux 8 in order to be upgraded to the final release of 2024.09.

## DBS End of Functionality

Continuing to use the DBS and ECCR past the EoM date is not recommended. The recommended action is to decommission the DBS and ECCR and replace it with CCER and a third party database and reporting solution.

The DBS continues to function after the EoM date. However, it is no longer supported and continued compatibly cannot be assured. The DBS eventually ceases to be compatible with other components of the BroadWorks system. The first known incompatibility is with release 2025.07 and later.

BroadWorks release 2025.07 upgrades the Java JDK to version 11. As a result, there is an incompatibility between applications built for Java 8 and the ADP built for java 11. Since the EECR applications are EoM they have not been updated for Java 11 and cannot be deployed on an ADP running 2025.07 or later.

### Revision History

1.0

25-Sep-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 25-Sep-2025 | Initial Release |