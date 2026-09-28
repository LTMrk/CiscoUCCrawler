---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-217743-upgrade-of-video-communication-server-v-html-3ab86c58fe
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217743-upgrade-of-video-communication-server-v.html
retrieved_at: 2026-08-16T15:38:08.995945+00:00
---

Upgrade Video Communication Server (VCS) / Expressway X14.x

# Upgrade Video Communication Server (VCS) / Expressway X14.x

### Download Options

Updated: April 5, 2024

Document ID: 217743

Contents

## Contents

## Introduction

This document describes the Expressway upgrade process and is designed to guide you and answer the most commonly asked questions.

## Requirements

Important notes about upgrades to X14.2:

- Expressway X14.2 only supports Smart Licensing. Cisco bug ID CSCwe09378 can lead to SSL negotiation failure between Smart Licensing Server (direct/proxy mode) which is fixed in X14.2.5.

- Expressway X14.2 is capped at 2500 encrypted signaling sessions to endpoints and includes changes in the trafficserver behavior related to Cisco bug ID CSCwc69661 that can lead to MRA failures - Please read the Release Notes and Admin Guide before an upgrade to X14.2. Also refer to note 4 in the Pre-upgrade Actions section of this document for more information.

- If you have a custom MTU size configured on the Expressway, it does get changed to the default of 1500 after the upgrade which causes problems in connections and media. This is tracked under the Cisco bug ID CSCwc74590. After the upgrade, you must change the MTU size back to the previous MTU size that was configured before the upgrade.

## Background information

The information in this document applies to both Expressway and Video Communication Server (VCS). The document references Expressway but this can be interchanged with VCS.

Note : While this document is designed to help with the upgrade, it does not replace the Expressway release notes. Always refer to the Release notes for the destination version before continuing with the upgrade.

## Important Information for All Deployments

- The upgrade steps can be found in the Release notes here for both standalone systems and clustered systems.

- You can directly upgrade to X14.x from version X8.11.4 and higher. No intermediate version is required. Upgrades from any version before X8.11.4, require an intermediate upgrade to X8.11.4.

- No release key is required for an upgrade of Expressway to X12.5.4 or higher. It is required for Cisco VCS systems though.

Note : Find the "Primary" on System > Clustering menu. The “Configuration primary” number points to the “Primary peer” in the list of peers in the same page.

- Upgrade Expressway-E and Expressway-C "Primary" at the same time. Or upgrade Expressway-E cluster first ("Primary" then "Subordinate(s)"), then upgrade Expressway-C cluster ("Primary" then "Subordinate(s)"). At the end of the upgrade window, all servers (Expressway-C and Expressway-E) are on the same version.

- If using Cisco Meeting Server (CMS) WebRTC Proxy over Expressway feature and the Expressway-E as TURN server, run a CMS version 2.8.4, or 2.9.3 and later for WebRTC to continue functionality after the upgrade. Previous releases of CMS do not work due to TURN service incompatibility related to Cisco bug ID CSCvv01243 .

- If push notifications are enabled for Mobile and Remote Access (MRA), run at minimum Cisco Unified Communications Manager (CUCM)/ Instant Messaging and Presence (IMP) version 11.5.1.18900-97 or 12.5.1.13900-152 or 14.0.1.10000-20 or later before the upgrading Expressways.

Note : Check if that push notifications are enabled from CUCM > Advanced features > Cisco Cloud Onboarding , and see if Enable push notifications is checked (enabled).

## Pre-upgrade Actions

1. In order for MRA functionality to continue after the upgrade, upload the root and intermediate certificates that signed Expessway-C certifiicate to the CUCM publisher as “tomcat-trust” and as “callmanager-trust”.

After the upload of the certificates, restart the “Cisco Tomcat” service, “Cisco callmanager” service and “Cisco TFTP” service on all relevant CUCM nodes (Cisco HAProxy service is restarted automatically with the Tomcat service restart).

This is needed due to changes made in Cisco bug ID CSCvz20720 . This is needed if you using non-security phone profiles and " TLS verify mode" is disabled for the CUCM cluster added on Expressway-C.

For more information on the exact steps needed to achieve that, please refer to the document Upload the Root and Intermediate Certificates of Expressway-Core onto CUCM .

Note : The only way to restart the “Cisco Tomcat” service from the command line is with the command utils service restart Cisco Tomcat .

2. From X14.2 onwards, even if TLS verify is set to Off on Unified Communications servers (CUCM, IM&P, CUC and CMS), the CA certificates (both Root and any intermediate CAs) for those servers must be added to Expressway-C trust store. Failure to do so can cause MRA login problems after an upgrade to X14.2 or higher.

In addition to that, the FQDN of the Unified Communication servers Expressway-C connects to need to be in the SAN list in the certificate of those servers.

This change was added part of a security enhancements to Expressway, tracked in Cisco bug ID CSCwc69661 . Further information on this can be found in X14.2 release notes .

Refer to the document Troubleshoot Expressway Traffic Server Certificate Verification for MRA Services Introduced by CSCwc69661.

3. From X14.2 onwards, Smart Licensing is the only available license mode with Expressway, traditonal PAK (option key) based license model has been removed.

Normally, if only used in the Expressways for MRA, no license is needed and this change does not impact your system. However, if using B2B calls or registered endpoints to Expressway (or any other features that require a license), then ensure Expressway-C and Expressway-C can access Cisco Smart Software Manager on cloud directly or via a proxy or connect to Cisco Smart Software Manager On-Premises.

Smart licensing is enabled by default after an upgrade to X14.2, but ensure the connection to the CSSM (Cloud or on-premises) is successful.

Note : Cisco bug ID CSCwe09378 which can lead to SSL negotiation failure between Smart Licensing Server (direct/proxy mode) which is fixed in X14.2.5. Further information on this can be found in the X14.2 release notes.

4. From X14.2 onwards, Expressway is limited to the 2500 crypto sessions limit (2500 sessions here is a sum of all MRA sessions + calls + endpoint registrations to Expressways). A single MRA session with one client could consume two crypto sessions or more. The same with dual regisration endpoints (H.323 and SIP). Each of those endpoints would consume two crypto sessions.

Normally this does not impact small sized Expressways which are only used for MRA; however this does impact a medium or large sized Expressway used for MRA.

Pre X14.2, a large sized Expressway could normally handle up to 3500 MRA sessions, but with X14.2 it is limited to 2500.

This means the Expressway capacity could be halved. For example, for 2500 Jabber users (with phone and IM&P services), after an upgrade to X14.2, this is seen by Expressway as 5000 encrypted signal sessions, and sessions over the 2500 mark are rejected, which affects MRA calls and registrations.

This limit cannot be removed in X14.2.

Further information on this can be found in the X14.2 release notes .

5. If there is an Expressway cluster, ensure there are no cluster alarms (From Status > Alarms ).

Note : If there is an alarm number “40049” about “Cluster TLS permissive -  Cluster TLS verification mode permits invalid certificates”, ignore this alarm and continue with the upgrade, but any other cluster alarms need to be dealt with before the upgrade.

6. I f there is an Expressway cluster, connect to the Expressway server needing upgrade through SSH and use the “root” user and run the command: cd / && ./sbin/verify-syskey

Note : This command must not provide any output. If receiving an “error” as a result from this command, open a TAC case to fix the errors before proceeding with the upgrade.

7. Finally, take a backup before the upgrade (From Maintenance > Backup and Restore ). Do this on each server.

## Upgrade Directions

- Download the upgrade file (name ends with ".tar.gz") from Expressway software downloads (For example download  “s42700x14_0_6.tar.gz” for X14.0.6).

- Upload the upgrade file (For example “s42700x14_0_6.tar.gz”) to the Expressway (From Maintenance > Upgrade, then click Browse to find the upgrade file on the PC, and finally click Upgrade ).

Note : The upgrade file is uploaded to Expressway when clicking Upgrade . After the upload is done, press Continue to proceed with the upgrade. The server installs the software and asks to Reboot to switch to the new software.

## Post-upgrade actions

After an Expressway upgrade, Refresh the Unified Communications nodes from the primary Expressway-C server:

- Navigate to Configuration > Unified communication > Unified CM servers .  Select all CUCM clusters and select Refresh.

- Navigate to Configuration > Unified communication > IM and presence service nodes . Select all IM&P clusters and select Refresh.

- Navigate to Configuration > Unified communication > Unity Connection Servers . Select all CUC clusters and select Refresh .

## FAQ

### Licenses

#### 1. Do I need a release key in order to upgrade ?

A release key is not required to upgrade an Expressway to version X12.5.4 or higher (release keys are still used for Cisco VCS systems).

#### 2. Do I need to migrate my licenses?

Licenses that are installed on the Expressway prior to the upgrade are migrated automatically to the new version.

#### 3. What licenses do I need to upgrade?

If you plan to upgrade from X8.11.4 or higher to a later version on the same server, no additional licenses are required, your current licenses are migrated automatically to the new version (VCS systems still require a release key).

These licenses are not required from version X12.5.4 onwards:

LIC-SW-EXP-K9 Release Key (From X12.5.4, this is provided by default on an upgrade of Expressway Systems. It is still required for VCS systems.)

LIC-EXP-TURN TURN relay licenses (Provided by default)

LIC-EXP-GW Interworking gateway (Provided by default)

LIC-EXP-AN Advanced networking (Provided by default)

These licenses are not required from version X12.6 onwards:

LIC-EXP-SERIES Expressway Series (You can now change this from the UI through the Service setup Wizard from Status > Overview )

LIC-EXP-E Traversal server license (You can now change this from the UI through the Service setup Wizard from Status > Overview )

#### 4. Do I need to enable Smart licensing?

Smart licensing is mandatory from X14.2 onwards. Any version lower than X14.2 can still use option key license model.

Smart licensing is enabled by default after an upgrade to X14.2, but you have to make sure that the connection to the CSSM (Cloud or on-prem) is successful.

Note : Cisco bug ID CSCwe09378 which can lead to SSL negotiation failure between Smart Licensing Server (direct/proxy mode) which is fixed in X14.2.5 and also expected to be fixed in X14.0.11 (tentative release late Feb 2023)

### Compatibility

#### 1. Can I upgrade directly to X14.x ?

Directly upgrade to X14.x (or to X12.x) Expressway release from version X8.11.4 and higher. Any version lower than X8.11.4 requires two-stage upgrade. Further information is available in the release notes.

#### 2. Which Cisco Unified Communications Manager and IM&Presence versions are compatible with Expressway ?

If using Push Notification for Jabber over MRA, the minimum versions are 11.5.1.18900-97, 12.5.1.13900-152 or 14.0.1.10000-20.

Check if Push Notifications are enabled under CUCM admin page Advanced features > Cisco Cloud Onboarding . Verify if Enable push notifications is checked (enabled).

#### 3. Which CMS version is compatible with Expressway 12.X and 14.X ?

If using CMS WebRTC Proxy over Expressway, run CMS version 2.8.4, or 2.9.3 or later. Previous releases do not work due to TURN service incompatibility related to Cisco bug ID CSCvv01243

### Post Upgrade

#### 1. Are there any additional tasks that I need to perform after the upgrade?

The Unified Communications nodes must be refreshed from Expressway-C primary peer:

- Navigate to Configuration > Unified communication > Unified CM servers .  Select all CUCM clusters and select Refresh .

- Navigate to Configuration > Unified communication > IM and presence service nodes . Select all IM&P clusters and select Refresh .

- Navigate to Configuration > Unified communication > Unity Connection Servers . Select all CUC clusters and select Refresh .

#### 2. How can I validate that the upgrade is successful?

There are couple things that can be checked:

- Check if the the cluster is stable (from System > Clustering ) and confirm that there are no cluster alarms Status > Alarms .

- Ensure that the zone with the type “Unified communication traversal” shows as “Active” for “SIP status” on Expressway-C and on Expressway-E. It is normal to see the Auto-created CE (tcp/tls/OAuth) Zones (from Configuration > Zones ) show as “Address resolvable” instead of “Active”.

- Perform live tests by MRA log in, test calls, and so on.

#### 3. I see a new alarm about "Unsupported Hardware" or "Unsuitable hardware warning" on my Virtual Expressway server after a successful upgrade?

Expressway version X14.x now verifies the Virtual Machine (VM) CPU clock speed and makes sure that it matches the clock speed required for the VM of the same size as it is mentioned in the virtualization guide for Expressway . The exact alarms shows up as: "Unsuitable hardware warning - Your current hardware does not meet supported VM configuration requirements for this version of Expressway ."

If this alarm comes up, verify that the VM resources match the resources mentioned in the virtualization guide for Expressway . If they are lower than what is mentioned in the guide, rebuild the server to meet the minimum requirements for the size selected and then restore a backup.

Note : X14.0.7: Medium deployment (seen from Status > System > Information) and VM has a clockspeed higher than 3.19GHz ANDk, the VCS/Expressway version is exactly X14.0.7, then ignore the alarm. This alarm gets incorrectly triggered due to Cisco bug ID CSCwc09399 .

### Mobile Remote Access (MRA)

#### 1. Does the upgrade require configuration changes on Cisco Unified Communications Manager (CUCM) ?

If using MRA, due to security enhancement Cisco bug ID CSCvz20720 , the root and intermediate certificates of the Certificate Authorities that signed Expressway-C certificate must be uploaded as “tomcat-trust” and “callmanager-trust” to the CUCM publisher server (it replicates them to the subscribers). This is needed even if you use non-security phone profiles and " TLS verify mode" is disabled for the CUCM cluster added on Expressway-C. Restart the “Cisco Tomcat”, “Cisco CallManager” and “Cisco TFTP” services on each server so the changes take effect.

The “Cisco Tomcat” service can be restarted only from command line with the command “ utils service restart Cisco Tomcat" .

For more information on the exact steps needed to achieve that, please refer to the document Upload the Root and Intermediate Certificates of Expressway-Core onto CUCM .

#### 2. Do I need to change my Expressway-C certificate to upgrade?

No need to change the Expressway-C certificate if it is still valid. However, the root and intermediate certificates of the Certificate Authorities that signed Expressway-C certificate must be uploaded as “tomcat-trust” and “callmanager-trust” to the CUCM publisher server. See point 1 in Pre-upgrade actions section for more information.

### Pre-Upgrade

#### 1. What must I check prior to the upgrade ?

Clustered Expressway systems must verify that there are no cluster alarms from Status > Alarms .

Note : Alarm "40049” with message “Cluster TLS permissive - Cluster TLS verification mode permits invalid certificates” does not impact the upgrade process. All other occurrences must be resolved prior to the upgrade.

Also, run the comand cd / && ./sbin/verify-syskey from command line through root user. This command must not give any output. In case it does, open up a TAC case to get this investigated and corrected.

### Upgrade Process

#### 1. What is the upgrade sequence in a clustered system?

Start the upgrade from the "Configuration primary" peer in the cluster. Check under menu System > Clustering . The “Configuration primary” number displays which one it is among the peers. After the upgrade of the primary peer is complete, continue with the subordinate peers (one at a time).

#### 2. Can I upgrade Expressway-C and Expressway-E at the same time?

Yes; however it is recommended to upgrade the Expressway-E server(s) first and then the Expressway-C servers so that the traversal zone is set up correctly first on the E server. And if there is a cluster, start the upgrade with the "Primary" servers. Once the upgrade on the "Primary" is done, upgrade the "Subordinate" peers.

#### 3. Where can I download the Expressway upgrade image?

Find all Expressway upgrade images in the link here. Download the file with extension "tar.gz" for the version for upgrade:

https://software.cisco.com/download/home/286255326/type/280886992/

#### 4. How do I start the upgrade?

Navigate to Maintenance > Upgrade > Browse, select the upgrade file and click " Upgrade ". First the file is transferred. After that, click " Continue " button to start the actual upgrade process.

#### 5. How long does the upgrade process take ?

Most of the time the upgrade process takes up to 10 minutes after the upgrade file was transferred to the system and selected "Continue". However, it is highly recommended to schedule a maintenance window from 4 to 48 hours to accomodate for post upgrade tests.

#### 6. What access is required to perform the upgrade?

The upgrade is performed over the Web interface. However, in case there are any issues after the upgrade, console access could be required. It is good to check prior the upgrade that VMware or CIMC console access is available.

### Backup and Restore

#### 1. Do I need to take a backup before the upgrade?

A backup is recommended before the upgrade of Expressway. In case of a cluster, take a backup from all servers. Do this for each server from Maintenance > Backup and Restore .

#### 2. Can I take a snapshot of the Expressway before the upgrade?

VMware Snapshots are not supported on Expressway.

#### 3. Can I Rollback/Revert to the previous system I had before the upgrade?

Expressway keeps two sets of partitions after an upgrade. One is with the upgraded version, and one is with the previous version. Switch between those partitions with the command selectsw <1 or 2> from root user shell. Verify the current active partition with command selectsw . For example, if receiving "1" after running the selectsw command, then the active version is "1" and the inactive version is "2". To switch to the inactive partition, execute a command " selectsw 2 ". A  reboot is required to boot from a newly selected partition system.

### Physical Appliance Servers

#### 1. Can I upgrade to this version on my Physical Appliance server?

For all Physical Appliance servers (CE500, CE1000, CE1100, CE1200), please refer to "Table 2" in "Supported platforms" section of the release notes for destination version to verify upgrade to the destination version.

#### 2. I have a CE1100, can I upgrade it to X14.0.x and X14.2.x?

For Physical Applicance server CE1100, you can upgrade to X14.0.x and X14.2.x to mitigate vulnerabilites and you can ignore the "Unsupported Hardware" alarm. This is mentioned in the release notes of X14.0.6 . Cisco has extended the End of Vulnerability/Security Support from November 14, 2021 (as per the original End-of-Life announcement ) to November 30, 2023, in line with the last date of support, for those customers with a valid service contract.

Note : This only applies for vulnerability fixes and not for new features.

### Virtual Servers and ESXi

#### 1. Which ESXi version is supported with this Expressway version?

Find the ESXi support information in the installation guide (under System Requirements > ESXi Requirements ) for the destination version of your Expressways.

### Revision History

10.0

05-Apr-2024

Aligned document with documentation addressing and domain standards.

9.0

18-Oct-2022

Identified potential PII.

8.0

10-Aug-2022

X14.2 update

7.0

03-Aug-2022

Added information in relationship to https

6.0

07-Jul-2022

Added information in relationship to https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc09399

5.0

21-Mar-2022

New licensing FAQ for required licenses to upgrade

4.0

19-Mar-2022

Licensing FAQ additional question & Reference to new document for certificate trust store update on CUCM for Expressway change

3.0

17-Mar-2022

Numbering on FAQ corrected

2.0

17-Mar-2022

VCS requires release key still.

1.0

15-Mar-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 10.0 | 05-Apr-2024 | Aligned document with documentation addressing and domain standards. |
| 9.0 | 18-Oct-2022 | Identified potential PII. |
| 8.0 | 10-Aug-2022 | X14.2 update |
| 7.0 | 03-Aug-2022 | Added information in relationship to https |
| 6.0 | 07-Jul-2022 | Added information in relationship to https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc09399 |
| 5.0 | 21-Mar-2022 | New licensing FAQ for required licenses to upgrade |
| 4.0 | 19-Mar-2022 | Licensing FAQ additional question & Reference to new document for certificate trust store update on CUCM for Expressway change |
| 3.0 | 17-Mar-2022 | Numbering on FAQ corrected |
| 2.0 | 17-Mar-2022 | VCS requires release key still. |
| 1.0 | 15-Mar-2022 | Initial Release |