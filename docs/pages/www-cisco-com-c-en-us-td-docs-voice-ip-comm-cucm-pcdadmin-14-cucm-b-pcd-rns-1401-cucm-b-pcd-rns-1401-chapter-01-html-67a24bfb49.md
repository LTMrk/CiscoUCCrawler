---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-14-cucm-b-pcd-rns-1401-cucm-b-pcd-rns-1401-chapter-01-html-67a24bfb49
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/14/cucm_b_pcd-rns_1401/cucm_b_pcd-rns_1401_chapter_01.html
retrieved_at: 2026-08-21T01:29:35.871911+00:00
---

Release Notes for Cisco Prime Collaboration Deployment, Release 14

# Release Notes for Cisco Prime Collaboration Deployment, Release 14

Find Matches in This Book

## Results

Updated: March 31, 2021

Chapter: New and Changed Information

## Chapter: New and Changed Information

- New and Changed Information

- Max Nodes Configuration

# New and Changed Information

## Max Nodes Configuration

The feature is used to have the maximum thread count as the configurable value. Currently, the limit on PCD is 21 nodes which
                              run in parallel across all parallel tasks (Cluster Discovery, Install Task, Migrate Task, Upgrade Task, Switch Version Task,
                              Server Restart Task, and Readdress Task). The default value is increased to 30 nodes. Value is configured from 1–200. It helps
                              to configure the maximum nodes across all running tasks count as the configurable value so PCD completes the tasks quickly.

When the maximum nodes count exceeds the maximum defined limit for tasks (Cluster Discovery, Install Task, Migrate Task, Upgrade
                              Task, Switch Version Task, Server Restart Task, and Readdress Task), a warning message is displayed. For more information
                              on how to configure, see Prime Collaboration Deployment Administration Guide