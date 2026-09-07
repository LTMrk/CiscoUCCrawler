---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-225067-upgrade-broadworks-adp-server-with-html-bd45662842
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/225067-upgrade-broadworks-adp-server-with.html
retrieved_at: 2026-09-07T13:01:26.133482+00:00
---

Upgrade BroadWorks ADP Server with Mixed Applications

# Upgrade BroadWorks ADP Server with Mixed Applications

### Download Options

Updated: September 26, 2025

Document ID: 225067

## Introduction

This document describes how Java JRE Changes in 2025.07 affect upgrades on an ADP with both Release Independent and Dependent applications.

## Design

The Application Delivery Platform (ADP) is the BroadWorks server that replaces the Xtended Service Platform (XSP) and Profile Server (PS) at version 24.0 and up.

There are two application types, Release Independent (RI) applications and Release Anchored (RA):

- Release Anchored applications contain the major BroadWorks release version in the application name. These applications must be updated after the Application Server (AS) is upgraded and are not backward compatible with older major releases of the AS.

- Release Independent applications do not have the major BroadWorks release version in the application name. These applications can be updated before or after the Application Server (AS) has been upgraded and are backward compatible with an older version of the AS.

The ADP is intended to be dedicated to only Release Independent or only Release Anchored applications on a per server basis. However, this is not enforced and the ADP allows both application types to be deployed on a single server.

The ADP must be upgraded to the same release or greater than the target application version.

For latest compatibility between applications and ADP see the ADP Release Notes , specifically the section 'Known Limitations and Restrictions'.

## Impact of Java JRE Changes in 2025.07 and Later

When upgrading a BroadWorks system the Release Independent applications can be upgraded before or after the Application Server (AS) and the Release Anchored applications must be upgraded after the AS.

Upgrading Release Independent applications before the Application Server (AS) is normally not a problem. The ADP can be upgraded, Release Independent applications updated and Release Anchored applications updated after the AS is upgraded. However, when upgrading to 2025.07 or later this is not possible.

Release 2025.07 upgrades Java JDK to version 11 for all BroadWorks components. As a result, there is an incompatibility between applications built for Java 8 and the ADP built for Java 11. This means that when upgrading from pre-2025.07, it is mandatory to upgrade all applications at the same time as the ADP. If the ADP has both Release Independent applications and Release Anchored applications deployed on it this becomes a problem. ADPs that are dedicated to only Release Independent applications (with no RA applications deployed) do not encounter this problem and are upgraded before the AS as normal.

## Upgrading an ADP from Release 24.0 with Mixed Applications

When upgrading from release 24 execute these steps. Release 24 end of support is July 31, 2026.

Steps to upgrade:

- Install the target release version of the 26.0 Release Anchored applications and Release Independent applications but do not manually update the applications.

- Upgrade the AS to 26.0.

- Upgrade the ADP - the upgrade automatically updates the Release Anchored applications and Release Independent applications that use Java 11

- Update remaining applications if necessary.

Some applications, where the file name ends in .war, do not align with the normal naming standard for Release Anchored applications or Release Independent applications such as BWCallSettingsWeb_1.15.20_2.war. These applications need to be updated manually, this can be performed after the Application Server (AS) has been upgraded.

## Upgrading an ADP from Release 25.0 with Mixed Applications

Release 25 is no longer receiving updates as 2024.07 was the last release of 25 and release 26 begins at 2024.08. This means that the Release Anchored applications for 25 have not been updated.

Steps to upgrade:

- Install the target release version of the 26.0 Release Anchored applications and Release Independent applications but do not manually update the applications.

- Upgrade the AS to 26.0.

- Upgrade the ADP - the upgrade automatically updates the Release Anchored applications and Release Independent applications that use Java 11

- Update remaining applications if necessary.

Some applications, where the file name ends in .war, do not align with the normal naming standard for Release Anchored applications or Release Independent applications such as BWCallSettingsWeb_1.15.20_2.war. These applications need to be updated manually, this can be performed after the Application Server (AS) has been upgraded.

## Upgrading an ADP from Release 26.0 with Mixed Applications

Upgrading from 26.0 to a later version beyond 2025.07.

Steps to upgrade:

- Install the latest version of the 26.0 Release Anchored applications and Release Independent applications but do not manually update the applications.

- Upgrade the AS.

- Upgrade the ADP - the upgrade automatically updates the Release Anchored applications and Release Independent applications that use Java 11.

- Update remaining applications if necessary.

Some applications, where the file name ends in .war, do not align with the normal naming standard for Release Anchored applications or Release Independent applications such as BWCallSettingsWeb_1.15.20_2.war. These applications need to be updated manually, this can be performed after the Application Server (AS) has been upgraded.

Note: The automatic application update behavior described is specific to the Java 8 to Java 11 migration. For subsequent upgrades (for example, 2025.07+ to 2026.02+), where the environment is already running Java 11, please use the standard upgrade procedures outlined in the BroadWorks Application Delivery Platform Configuration Guide .

### Revision History

1.0

26-Sep-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Sep-2025 | Initial Release |