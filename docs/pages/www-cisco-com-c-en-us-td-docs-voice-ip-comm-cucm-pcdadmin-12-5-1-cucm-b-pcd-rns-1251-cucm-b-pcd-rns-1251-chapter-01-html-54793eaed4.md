---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-12-5-1-cucm-b-pcd-rns-1251-cucm-b-pcd-rns-1251-chapter-01-html-54793eaed4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/12_5_1/cucm_b_pcd-rns-1251/cucm_b_pcd-rns-1251_chapter_01.html
retrieved_at: 2026-08-24T10:57:27.066707+00:00
---

Release Notes for Cisco Prime Collaboration Deployment, Release 12.5(1)

# Release Notes for Cisco Prime Collaboration Deployment, Release 12.5(1)

Find Matches in This Book

## Results

Updated: January 23, 2019

Chapter: New and Changed Information

## Chapter: New and Changed Information

# New and Changed Information

## Switch Version in Direct Standard Upgrade Sequence

With this release, when you perform any upgrade from 12.5 to 12.5 and above, the direct standard upgrade sequence does not
                              allow you to run the switch version on IM and Presence publisher and Cisco Unified Communications Manger subscriber in parallel.

You can perform the switch version on the Cisco Unified Communications Manager subscriber first and then IM and Presence publisher.

## Task Chaining

With this release, Cisco Prime Collaboration Deployment supports chaining of install, migrate, and upgrade task. Cisco Prime
                              Collaboration Deployment can handle multiple COP files in a single task without any manual intervention. You can make a task
                              dependent on an existing task. Dependent task is triggered automatically on the successful completion of an existing task.
                              This feature helps you to perform install, upgrade, and migration tasks without manual intervention, so that you can efficiently
                              handle upgrades of large or geo-distributed environments.

Install Upgrade Patch—Enables you to install patch files on freshly installed clusters chained to the install task on Prime
                                       Collaboration Deployment.

For example: Fresh install task for 10.5 followed by upgrade task for 10.5 SU3.

Migrate Upgrade Patch—Enables you to install patch files on migrated clusters chained to the migration task on Prime Collaboration
                                       Deployment.

For example: Migration task for 10.5 followed by upgrade task for 10.5 SU3.

Multi COP Upgrade—Enables you to upgrade nodes in a cluster chained with multiple cops one after another in a single task
                                       without creating separate tasks for each COP file.

If the user select the multiple cop files for upgrade then the task sequence will load up according to the selected COP files.

Maximum 32 COP files can be selected for a specific product.

For example:

Fresh install task followed by (separate task) batch-install of a long list of COP files.

If the upgrade task is completed, and a week later you need to do a (separate task) batch-install of a long list of COP files.

(Single task) batch-install a long list of COP files with a Prime Collaboration Deployment upgrade task for direct standard
                                             upgrade or direct refresh upgrade.

Multi cluster Upgrade—Enables you to upgrade nodes in a cluster chained with another upgrade task for a different cluster.
                                       The task sequence will load up according to the selected cop file.

For example: when a task to upgrade cluster X is successful then the next task to upgrade cluster Y starts automatically.

COP file Installation for Install Task—Enables you to install COP files on a freshly installed cluster.

For example: Fresh install task for 11.5 followed by COP file install task.

COP file Installation for Migration Destination Cluster—Enables you to install COP files on a freshly migrated destination
                                       cluster.

For example: Migration task to 11.5 followed by COP file install task.

Upgrade Migrate—Enables you to upgrade a cluster chained with a migration task.

For example: Prime Collaboration Deployment upgrade followed by a Virtual-to-Virtual Prime Collaboration Deployment Migration.

## Spectre/Meltdown Vulnerabilities During Upgrade

This release of Unified Communications Manager, Cisco IM and Presence Service, Cisco Emergency Responder, and Cisco Prime
                              Collaboration Deployment contain software patches to address the Meltdown and Spectre microprocessor vulnerabilities.

Before you upgrade to Release 12.5(1) or above, we recommend that you work with your channel partner or account team to use
                              the Cisco Collaboration Sizing Tool to compare your current deployment to an upgraded deployment. If required, change VM resources
                              to ensure that your upgraded deployment provides the best performance.

| Note | If the user select the multiple cop files for upgrade then the task sequence will load up according to the selected COP files. |
|---|---|

| Note | Maximum 32 COP files can be selected for a specific product. |
|---|---|