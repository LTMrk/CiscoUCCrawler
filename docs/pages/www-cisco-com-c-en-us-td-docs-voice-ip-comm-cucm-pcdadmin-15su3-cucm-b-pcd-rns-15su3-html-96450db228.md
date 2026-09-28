---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-15su3-cucm-b-pcd-rns-15su3-html-96450db228
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/15SU3/cucm_b_pcd-rns_15su3.html
retrieved_at: 2026-08-16T17:52:05.295115+00:00
---

Release Notes for Cisco Prime Collaboration Deployment, Release 15SU3

# Release Notes for Cisco Prime Collaboration Deployment, Release 15SU3

### Download Options

Updated: July 31, 2025

First Published: July 31, 2025

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

There are no new features that are introduced for this release.

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

Access the Cisco Bug Search tool: https://bst.cloudapps.cisco.com/bugsearch .

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

CSCwn20347

PCD Upgrade task lists one additional step with CUCM sub node incorrectly

CSCwm60730

CUCM node entry is missing in newly defined cluster in PCD due to connection issues

CSCwp03167

[PCD] Java application changes to use JENT

CSCwo85862

PCD support for UCCX 15

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
| CSCwn20347 | PCD Upgrade task lists one additional step with CUCM sub node incorrectly |
| CSCwm60730 | CUCM node entry is missing in newly defined cluster in PCD due to connection issues |
| CSCwp03167 | [PCD] Java application changes to use JENT |
| CSCwo85862 | PCD support for UCCX 15 |