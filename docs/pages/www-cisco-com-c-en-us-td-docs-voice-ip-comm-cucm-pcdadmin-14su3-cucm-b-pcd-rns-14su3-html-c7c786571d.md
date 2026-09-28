---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-14su3-cucm-b-pcd-rns-14su3-html-c7c786571d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/14SU3/cucm_b_pcd-rns_14SU3.html
retrieved_at: 2026-08-16T23:41:27.815002+00:00
---

Release Notes for Cisco Prime Collaboration Deployment, Release 14SU3

# Release Notes for Cisco Prime Collaboration Deployment, Release 14SU3

### Download Options

First Published: May 18, 2023

# Introduction

## About Cisco Prime Collaboration Deployment

These release notes describe new features, requirements, restrictions, and caveats for Cisco Prime Collaboration Deployment.
                     These release notes are updated for every maintenance release.

Cisco Prime Collaboration Deployment is an application designed to assist in the management of Unified Communications applications.
                     It allows the user to perform tasks such as migration of older software versions of clusters to new virtual machines, fresh
                     installs, and upgrades on existing clusters.

Cisco Prime Collaboration Deployment has four primary, high-level functions:

Migrate an existing cluster of Unified Communications servers to 11.5 or higher from 10.x and above (this would be Virtual
                           to Virtual)

Perform operations on existing clusters (11.5 or higher). Examples of these operations include:

Upgrade the cluster to a new version (11.5 or higher) of software

Switch version

Restart the cluster

Changing IP addresses or hostnames in the cluster on existing Release 10.x or higher clusters.

Fresh install a new Release 11.5 or higher Unified Communications cluster.

Cisco Prime Collaboration Deployment does not support internationalization or languages other than English.

Upgrading to Cisco Prime Collaboration Deployment 14SU3 from Pre-14 source release need COP file ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn to be installed to list the Cisco Prime Collaboration Deployment 14SU3 ISO file as valid.

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

There are no new features added for this release.

### Caveats

#### Bug Search
                     	 Tool

All severity level 1 or 2 bugs

Significant severity level 3 bugs

All customer-found bugs

You can
                        		search for open and resolved caveats of any severity for any release using the Cisco Bug Search tool, an online tool
                        		  available for customers to query defects according to their own needs.

Internet
                                 			 connection

Web browser

Cisco.com user ID
                                 			 and password

Follow these
                        		steps to use Cisco Bug Search tool:

Access the Cisco Bug Search tool: https://tools.cisco.com/bugsearch/ .

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

#### Resolved Caveats

Identifier

Headline

CSCwe32199

PCD NAT is not working on step3 (check the dbreplication) of the upgrade

CSCwc83342

PCD vulnerable to stored cross-site scripting

CSCwc83337

Cisco Prime Collaboration Deployment XXE Injection Vulnerability

CSCwe04160

HTTP Headers Missing SameSite=Strict in PCD

CSCwc51536

openjdk rpms update for PCD

CSCwd64891

The fix committed to remove unsupported DHE ciphers in 14SU2 is not working in 14SU3

CSCwd95009

PCD: Improper protection to /usr/bin/find in Sudoers configuration

CSCwd64328

Cisco Prime Collaboration Deployment SELinux protections missing in selected services or processes

CSCwd47423

Cisco Prime Collaboration Deployment assessment of expat CVE-2022-40674

### This Document Applies to These Products

- Unified Communications Manager Version 14

| Note | Cisco Prime Collaboration Deployment does not support internationalization or languages other than English. |
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

| Identifier | Headline |
|---|---|
| CSCwe32199 | PCD NAT is not working on step3 (check the dbreplication) of the upgrade |
| CSCwc83342 | PCD vulnerable to stored cross-site scripting |
| CSCwc83337 | Cisco Prime Collaboration Deployment XXE Injection Vulnerability |
| CSCwe04160 | HTTP Headers Missing SameSite=Strict in PCD |
| CSCwc51536 | openjdk rpms update for PCD |
| CSCwd64891 | The fix committed to remove unsupported DHE ciphers in 14SU2 is not working in 14SU3 |
| CSCwd95009 | PCD: Improper protection to /usr/bin/find in Sudoers configuration |
| CSCwd64328 | Cisco Prime Collaboration Deployment SELinux protections missing in selected services or processes |
| CSCwd47423 | Cisco Prime Collaboration Deployment assessment of expat CVE-2022-40674 |