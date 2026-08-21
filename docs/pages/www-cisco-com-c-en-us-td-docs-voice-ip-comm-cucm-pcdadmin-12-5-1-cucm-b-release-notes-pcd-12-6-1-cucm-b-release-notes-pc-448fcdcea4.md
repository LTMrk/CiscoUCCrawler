---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-12-5-1-cucm-b-release-notes-pcd-12-6-1-cucm-b-release-notes-pc-448fcdcea4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/12_5_1/cucm_b_release-notes-PCD-12-6-1/cucm_b_release-notes-PCD-12-6-1_chapter_01.html
retrieved_at: 2026-08-21T01:29:23.198895+00:00
---

Release Notes for Cisco Prime Collaboration Deployment, Release 12.6(1)

# Release Notes for Cisco Prime Collaboration Deployment, Release 12.6(1)

Find Matches in This Book

## Results

Updated: August 6, 2021

Chapter: New and Changed Information

## Chapter: New and Changed Information

# New and Changed Information

## Cisco Prime Collaboration Deployment Support for Cisco Emergency Responder

Cisco Prime Collaboration Deployment (PCD) provides supports for Cisco Emergency Responder (CER) from this release onwards.
                              Currently, Cisco Prime Collaboration Deployment provides support tasks for the following products:

Unified Communications Manager (UCM)

IM and Presence Service (IM&P)

Cisco Unity Connection (CUC)

Cisco Unified Contact Center Express (UCCX)

PCD has extended support for Upgrade, Restart, Readdress, and Switch Version for CER. Hence CER users can seamlessly upgrade
                              and perform all PCD-related tasks.

Upgrade Task —Performs Direct Refresh Upgrade and Direct Standard Upgrade on the CER cluster starting from 11.5(x) or higher of  Emergency
                                    Responder soruce release.

Multi COP Upgrade —Performs Multi COP upgrades on a CER cluster, which installs multiple COP files on CER in a single task.

Restart Task —Restarts the CER clusters using PCD without manually restarting each node.

Readdress Task —Changes the IP address and hostname of the nodes in a CER cluster.

Switch Version Task —Switches between the inactive and active version of the nodes in a CER cluster.

## Enhancing/Enhancement Email Notification Utility

Cisco Prime Collaboration Deployment (PCD) trigger emails for each task action, you get notifications when each node/ task
                              step is completed.

For example, PCD task of X steps, operating on 1 to N nodes:

Migration Task:

Task Scheduled for Cluster

Task Started for Cluster

Source Node(s) A Configuration export success*

Source Node(s) B Configuration export success*

Destination Node(s) A Install success*

Destination Node(s) B Install success*

Source Node(s) A UFF Export success*

Source Node(s) A shut down success*

Destination Node(s) A UFF Import success*

Source Node(s) B UFF Export success*

Source Node(s) B shut down success*

Destination Node(s) B UFF Import success*

Task Completed/Failed

Upgrade Task (COPs):

Task Scheduled for Cluster

Task Started for Cluster

COPs x installed on node a*

COPs y installed on node b*

Task Completed/Failed

PCD Fresh Install Task or Upgrade Task (ISO):

Task Scheduled for Cluster

Task Started for Cluster

Node(s) A has been complete*

Node(s) B has been complete*

Task Completed/Failed

PCD Restart Task:

Task Scheduled for these nodes

Task Started for these nodes

Node(s) A has been restarted*

Node(s) B has been restarted*

Task Completed/Failed

PCD Switch Task:

Task Scheduled for these nodes

Task Started for these nodes

Node(s) A has been switched*

Node(s) B has been switched*

Task Completed/Failed

PCD Readdress:

Task Scheduled for these nodes

Task Started for these nodes

Node(s) A has been readdressed*

Node(s) B has been readdressed*

Task Completed/Failed

The "*" indicates a new feature where you get the email notifications after you perform each action.

## Updated Maximum Password Length

ESXi passwords configured in Cisco Prime Collabroration Deployment can be less than 32 characters, Unified Communications
                              Manager cluster passwords configured in Cisco Prime Collabroration Deployment can be less than 16 characters, please refer
                              CSCvo66994 for more information.