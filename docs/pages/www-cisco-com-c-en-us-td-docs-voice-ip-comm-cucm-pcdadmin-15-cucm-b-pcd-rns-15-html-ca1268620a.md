---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-15-cucm-b-pcd-rns-15-html-ca1268620a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/15/cucm_b_pcd-rns_15.html
retrieved_at: 2026-08-16T23:38:43.962326+00:00
---

Release Notes for Cisco Prime Collaboration Deployment, Release 15

# Release Notes for Cisco Prime Collaboration Deployment, Release 15

### Download Options

Updated: December 18, 2023

First Published: December 18, 2023

# Introduction

## About Cisco Prime Collaboration Deployment

These release notes describe new features, requirements, restrictions, and caveats for Cisco Prime Collaboration Deployment.
                  These release notes are updated for every maintenance release.

Cisco Prime Collaboration Deployment is an application designed to assist in the management of Unified Communications applications.
                  It allows the user to perform tasks such as migration of older software versions of clusters to new virtual machines, fresh
                  installs, and upgrades on existing clusters.

Cisco Prime Collaboration Deployment has four primary, high-level functions:

Migrate an existing cluster of Unified Communications servers of source version 10.5 or above to destination version 12.5.x
                        or higher (this would be Virtual to Virtual).

Perform operations on existing clusters (12.5 or higher). Examples of these operations include:

Upgrade the cluster from source version 11.5 or above to destination version 12.5.x or higher.

Switch version

Restart the cluster

Changing IP addresses or hostnames in the cluster on Release 12.5.x or higher clusters.

Fresh install a new Release 12.5.x or higher Unified Communications cluster.

Cisco Prime Collaboration Deployment doesn't support internationalization or languages other than English.

Upgrading to Cisco Prime Collaboration Deployment 15 from Pre-14 and SU source release need COP file ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn to be installed to list the Cisco Prime Collaboration Deployment 15 ISO file as valid.

### Related
                  	 Documentation

You can view
                     		documentation that is associated with supported applications.

Application

Documentation Link

Cisco Unified Communications Manager

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

Cisco Unified Contact Center Express

http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html

Cisco Unity Connection

http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/tsd-products-support-series-home.html

### New and Changed Information

Release 15 brings an enhanced experience for users and administrators with major platform upgrades to align with the industry
                     standards. The enhancements include Application-layer changes and core Linux transition for long-term support. This enhancement
                     also includes migration to 64-bit application architecture for removal of memory bottlenecks and mitigating end-of-life for
                     32-bit dependencies. This release provides enhanced protection, security, innovation, and flexibility.

Some of the important considerations when installing or migrating to Release 15 are:

Refresh Upgrades from Pre-12.5.x source to Release 15 is not supported.

Refresh Upgrades from other solution products to Release 15 is not allowed using Cisco Prime Collaboration Deployment.

You can only use the 15 or later versions of Cisco Prime Collaboration Deployment for all 15 or above UC clusters.

If you're using Cisco Prime Collaboration Deployment to upgrade an IM and Presence Service cluster from Release 12.5.x to
                           Release 15, you must install the following COP file on the Release 12.5.x systems before you begin the upgrade: ciscocm.imp15_upgrade_v1.0.k4.cop.sha512.
                           Note that the COP file is applicable only if:

Unified Communications Manager destination version is in Release 15.

Unified Communications Manager destination version is in Release 15 and you are trying to upgrade your IM and Presence Service
                                 source from a restricted version to an unrestricted version.

If you're using Cisco Prime Collaboration Deployment to upgrade an IM and Presence Service cluster from Release 14 or SUs
                           to Release 15, you must install the following COP file on the Release 14 or SU systems before you begin the upgrade: ciscocm.imp15_upgrade_v1.0.k4.cop.sha512.
                           Note that the COP file is applicable only if:

Unified Communications Manager destination version is in Release 15 and the IM and Presence Service source nodes are in 14
                                 or 14SU1 versions.

Unified Communications Manager destination version is in Release 15 and you are trying to upgrade your IM and Presence Service
                                 source from a restricted version to an unrestricted version.

### Caveats

#### Bug Search
                     	 Tool

The system grades known problems (bugs) per severity level. These release notes contain descriptions of the following bug
                        levels:

All severity level 1 or 2 bugs

Significant severity level 3 bugs

All customer-found bugs

You can
                        		search for open and resolved caveats of any severity for any release using the Cisco Bug Search tool, an online tool
                        		  available for customers to query defects according to their own needs.

To access the Cisco Bug Search tool, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Follow these
                        		steps to use Cisco Bug Search tool:

Access the Cisco Bug Search tool: https://bst.cloudapps.cisco.com/bugsearch/ .

Log in with your
                              			 Cisco.com user ID and password.

If you are looking for information about a specific problem, enter the bug ID number in the Search for: field and click Go .

Tip

Click Help on the Bug Search page for information about
                                    		  how to search for bugs, create saved searches, and create bug groups.

#### Open Caveats

Identifier

Headline

CSCwe26763

Cisco Prime Collaboration Deployment SELinux protections missing in cliscript, remotesupport

CSCwi09888

Vulnerabilities in tomcat 9.0.56 CVE-2023-44487 and others

CSCwi17414

tomcat_threads diagnose test failed in PCD FCS build

CSCwi39824

CD-ROM2 is not disconnecting from VM after Fresh install through PCD

CSCwi38877

iso upgrade task didnt start after dependent tasks completed

#### Resolved Caveats

Identifier

Headline

CSCwe32199

PCD NAT is not working on step 3 (check the dbreplication) of the upgrade

CSCwc83342

PCD vulnerable to stored cross-site scripting

CSCwc83337

Cisco Prime Collaboration Deployment XXE Injection Vulnerability

CSCwe04160

HTTP Headers Missing SameSite=Strict in PCD

CSCwd95009

PCD: Improper protection to /usr/bin/find in Sudoers configuration

CSCwd64328

Cisco Prime Collaboration Deployment SELinux protections missing in selected services or processes

CSCvy88892

quartz 2.3.0. A XXE attack is possible in the Terracotta Quartz Scheduler using a job description

CSCwb95747

Hostname and IP address change task failed during Network change verification in PCD

CSCwi48005

file get fails to download logs with local SFTP option in PCD

| Note | Cisco Prime Collaboration Deployment doesn't support internationalization or languages other than English. |
|---|---|

| Note | Upgrading to Cisco Prime Collaboration Deployment 15 from Pre-14 and SU source release need COP file ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn to be installed to list the Cisco Prime Collaboration Deployment 15 ISO file as valid. |
|---|---|

| Application | Documentation Link |
|---|---|
| Cisco Unified Communications Manager | http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html |
| Cisco Unified Contact Center Express | http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html |
| Cisco Unity Connection | http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/tsd-products-support-series-home.html |

| Tip | Click Help on the Bug Search page for information about
                                    		  how to search for bugs, create saved searches, and create bug groups. |
|---|---|

| Identifier | Headline |
|---|---|
| CSCwe26763 | Cisco Prime Collaboration Deployment SELinux protections missing in cliscript, remotesupport |
| CSCwi09888 | Vulnerabilities in tomcat 9.0.56 CVE-2023-44487 and others |
| CSCwi17414 | tomcat_threads diagnose test failed in PCD FCS build |
| CSCwi39824 | CD-ROM2 is not disconnecting from VM after Fresh install through PCD |
| CSCwi38877 | iso upgrade task didnt start after dependent tasks completed |

| Identifier | Headline |
|---|---|
| CSCwe32199 | PCD NAT is not working on step 3 (check the dbreplication) of the upgrade |
| CSCwc83342 | PCD vulnerable to stored cross-site scripting |
| CSCwc83337 | Cisco Prime Collaboration Deployment XXE Injection Vulnerability |
| CSCwe04160 | HTTP Headers Missing SameSite=Strict in PCD |
| CSCwd95009 | PCD: Improper protection to /usr/bin/find in Sudoers configuration |
| CSCwd64328 | Cisco Prime Collaboration Deployment SELinux protections missing in selected services or processes |
| CSCvy88892 | quartz 2.3.0. A XXE attack is possible in the Terracotta Quartz Scheduler using a job description |
| CSCwb95747 | Hostname and IP address change task failed during Network change verification in PCD |
| CSCwi48005 | file get fails to download logs with local SFTP option in PCD |