---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-15su2-cucm-b-pcd-rns-15su2-html-3faf5e3aeb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/15SU2/cucm_b_pcd-rns_15su2.html
retrieved_at: 2026-08-16T17:52:26.083984+00:00
---

Release Notes for Cisco Prime Collaboration Deployment, Release 15SU2

# Release Notes for Cisco Prime Collaboration Deployment, Release 15SU2

### Download Options

Updated: October 1, 2024

First Published: October 1, 2024

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

Upgrading to Cisco Prime Collaboration Deployment 15 and later from Pre-14 and SU source release need COP file ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn to be installed to list the Cisco Prime Collaboration Deployment 15 ISO file as valid.

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

TLS 1.3 is the highest version of the Transport Layer Security (TLS) protocol supported from this release onwards.

TLS 1.3 is faster and more secure than older versions of TLS. One of the key improvements in TLS 1.3 is the reduction in handshake
                     latency. It significantly enhances the performance of time-sensitive applications. Moreover, TLS 1.3 also reduces round-trip
                     times (RTT), by further optimizing the connection establishment process. TLS 1.3 has dropped support for older and less secure
                     cryptographic algorithms.

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

There are no open caveats in this release.

#### Resolved Caveats

Identifier

Headline

CSCwe26763

Cisco Prime Collaboration Deployment SELinux protections missing in cliscript, remotesupport

CSCwi17414

tomcat_threads diagnose test CLI is not working on PCD

CSCwi38877

upgrade task using PCD didn't start after dependent tasks completed

CSCwj39514

Install & Migration Task is getting failed after an hour of installation

CSCwj98678

PCD migration fails when the admin password is more than 16 chars

CSCwm00253

Unable to create upgrade dependent tasks for Migration or New UC cluster in PCD

CSCwm09187

PCD tasks are failing with TLS mismatch error in 1.3 when cluster has pre-15su2 as inactive

### This Document Applies to These Products

- Unified Communications Manager Version 15

| Note | Cisco Prime Collaboration Deployment doesn't support internationalization or languages other than English. |
|---|---|

| Note | Upgrading to Cisco Prime Collaboration Deployment 15 and later from Pre-14 and SU source release need COP file ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn to be installed to list the Cisco Prime Collaboration Deployment 15 ISO file as valid. |
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
| CSCwi17414 | tomcat_threads diagnose test CLI is not working on PCD |
| CSCwi38877 | upgrade task using PCD didn't start after dependent tasks completed |
| CSCwj39514 | Install & Migration Task is getting failed after an hour of installation |
| CSCwj98678 | PCD migration fails when the admin password is more than 16 chars |
| CSCwm00253 | Unable to create upgrade dependent tasks for Migration or New UC cluster in PCD |
| CSCwm09187 | PCD tasks are failing with TLS mismatch error in 1.3 when cluster has pre-15su2 as inactive |