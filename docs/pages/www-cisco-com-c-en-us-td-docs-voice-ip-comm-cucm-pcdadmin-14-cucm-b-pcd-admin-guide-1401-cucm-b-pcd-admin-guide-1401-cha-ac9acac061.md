---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-14-cucm-b-pcd-admin-guide-1401-cucm-b-pcd-admin-guide-1401-cha-ac9acac061
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/14/cucm_b_pcd-admin-guide-1401/cucm_b_pcd-admin-guide-1401_chapter_01001.html
retrieved_at: 2026-08-17T00:36:04.006730+00:00
---

Prime Collaboration Deployment Administration Guide, Release 14 and SUs

# Prime Collaboration Deployment Administration Guide, Release 14 and SUs

Updated: November 25, 2025

Chapter: Best Practices

## Chapter: Best Practices

# Best Practices

## Cluster Discovery

During cluster discovery, a small Cisco Options Package (COP) file is installed on the
                              		  servers that are being discovered. For this reason, ensure that before you initiate a discovery, no upgrades or COP file
                              installations
                              		  are in progress on the servers in the cluster that you want to discover.

## Upgrades

When you initiate an upgrade of an application server (Cisco Unified Communications Manager, IM and Presence Service, Cisco
                              Unified Contact Center Express, Cisco Unity Connection, or Cisco Emergency Responder ) from the Cisco Prime Collaboration Deployment Upgrade task, the upgrade works in the same manner as upgrades that are initiated
                              by the Unified Communications application GUI or CLI. As a result, we recommend that you follow the same preupgrade procedures
                              and postupgrade verifications as you would directly from the application server GUI.

## ESXi Host

Ensure that the virtual machines that you use for migrations or fresh installations reside on an ESXi host that was entered
                              into the Cisco Prime Collaboration Deployment system. That ESXi host should not allow Distributed Resource Scheduler (DRS)
                              or vSphere vMotion.

## Migration and
                        	 Installation Virtual Machines

Always create virtual machines (VMs) for new clusters using the appropriate Open Virtual Appliance (OVA) for the unified
                              communications application that you will install. Do not use an existing VM as a destination VM for migration (use a newly-created
                              VM). After a failed migration, if Cisco Prime Collaboration Deployment had started to install the new VM, you must delete
                              this VM and create a new one using the proper OVA.

If you have to configure a VMware in various ESXi host servers,
                                          			 ensure that you enter a unique name for ESXi host servers and avoid using the
                                          			 default name from OVA.

## Premigration

### Source
                              		  Cluster

- We recommend that you run a full backup by using Distributed Resource Scheduler (DRS) on the cluster.

## Postmigration

Follow these
                              		  postmigration best practices:

Check endpoints

Check database replication, for example:

```
admin:utils dbreplication runtimestate

Server Time: Tue Aug  1 15:10:52 IST 2023

Cluster Replication State: BROADCAST SYNC ended at: 2023-07-17-16-47
     Sync Result: SYNC COMPLETED on 753 tables out of 753
     Sync Status: All Tables are in sync
     Use CLI to see detail: 'file view activelog cm/trace/dbl/20230717_164617_dbl_repl_output_Broadcast.log'

DB Version: ccm15_0_0_98100_154

Repltimeout set to: 300s
PROCESS option set to: 1

Cluster Detailed View from cucm-55 (2 Servers):

                                           PING      DB/RPC/   REPL.    Replication    REPLICATION SETUP
SERVER-NAME              IP ADDRESS        (msec)    DbMon?    QUEUE    Group ID       (RTMT) & Details
-----------              ----------        ------    -------   -----    -----------    ------------------
cucm-57                  10.77.32.57       0.163     Y/Y/Y     0        (g_3)          (2) Setup Completed
cucm-55                  10.77.32.55       0.016     Y/Y/Y     0        (g_2)          (2) Setup Completed
```

The following list
                              		  shows the possible values for Replicate_State:

0—Replication Not Started. Either no subscribers exist, or the Database Layer Monitor service is not running and has not been
                                    running since the subscriber was installed.

1—Replicates were created, but their count is incorrect.

2—Replication is good.

3—Replication is bad in the cluster.

4—Replication setup did not succeed.

## Task
                        	 Validation

If a task is scheduled to start manually or start at a
                              		  later time, the Validate button appears and you can run validation on the
                              		  task manually. We recommend that you run the validation on a task before the start (you can run the validation anytime
                              before the start), to identify problems such
                              		  as missing virtual machines, communication issues, or missing ISO files. When the
                              		  validation is run, a popup window opens with a list of validation
                              		  problems. If no problems are found, the following message appears: "All
                                 		  validation tests passed."

## Cisco Prime
                        	 Collaboration Deployment Shutdown

For best results, to shut down the Cisco Prime Collaboration
                              		  Deployment server, use the command utils server shutdown . Failure to do so
                              		  can result in Network File System (NFS) mount issues on the ESXi hosts.

## Monitoring Tasks

Use the Monitoring GUI page to view the status of your tasks. Click
                              		  the task in the left column, and the task details appear on the right. Each
                              		  step in the task (export, install, and so on) appears in the Task Status table
                              		  below the details section. Click the arrow next to any step to see
                              		  additional details for that step. Some steps may have several task actions
                              		  within them. Scroll down to see all the actions and their status.

## Managing Files in
                        	 the SFTP Datastore

The SFTP datastore page shows the ISO and COP files that were transferred to the Cisco Prime Collaboration Deployment server
                              through SFTP. To
                              		  place a file on the Cisco Prime Collaboration Deployment server, for use in a
                              		  migration, install or upgrade task, use an SFTP client and log in as adminsftp (use the administrator password as your password).

When you connect to the Cisco Prime Collaboration Deployment server,
                              		  upload ISO files to be used by a migration or install task into the /fresh_install folder. Upload COP files to the /upgrade folder .

After a task is complete, if the ISO is not
                              		  needed for another task, we recommend that you delete the ISO file from the
                              		  SFTP datastore to conserve space on your Cisco Prime Collaboration Deployment
                              		  server. If there are too many ISO files in the SFTP datastore when the Cisco
                              		  Prime Collaboration Deployment is upgraded or a DRS backup is restored, the
                              		  Cisco Prime Collaboration Deployment server may run out of space.

## Using Cisco Prime
                        	 Collaboration Deployment with Clustering Over WAN

A minimum
                              		  bandwidth of 100 Mbps is recommended if the Cisco Prime Collaboration Deployment
                              		  server and other Unified Communications application nodes are communicating
                              		  over a WAN.

## Sequence During
                        	 Migration

When you create a migration task, the default sequence is presented,
                              		  which has one server in each install step. You can use the editing tools in the sequence
                              		  screen to place more than one server in a step. For best results, include no more than six servers in any one step.

## Server Readdress

With the Server Readdress feature, the system inserts a forced
                              		  pause after each server readdress. Verify that the server was successfully changed and that the phones reregistered before
                              you continue to the
                              		  next readdress step.

## Fresh Install
                        	 Publishers and Subscribers

When a fresh
                              		  install task (new UC cluster) includes more than one server, the Cisco Prime
                              		  Collaboration Deployment system automatically installs the Unified Communications Manager publisher
                              		  first, and then inserts a forced pause following the publisher installation. During the pause, you can go to the Unified
                              Communications Manager GUI of the newly installed publisher
                              		  and add the other cluster servers into the System > Servers GUI. After all
                              		  the subscribers to be installed in this cluster (Unified Communications Manager subscribers, IM and
                              		  Presence publishers and subscribers) are added to the Unified Communications Manager
                              		  publisher GUI, the user can click the Resume button on the Cisco Prime Collaboration Deployment Monitoring page to resume
                              		  the fresh install task.

## Fresh Install of a Unified CM and IM and Presence Cluster

When you create a
                              		  fresh install with both Unified Communications Manager and IM and Presence Service nodes, you must indicate which IM and
                              Presence Service server is the publisher. After the Unified Communications Manager publisher install, the task pauses. This
                              pause allows the subscriber install nodes to enter into the Unified Communications Manager Publisher ( System > Server GUI page). The IM and Presence Service publisher must be
                              		  the first IM and Presence server that is added to this list. This step ensures that the IM
                              		  and Presence Service publisher is installed as the first node.

## Email
                        	 Notification

If a task
                              		  encounters an error, the task is paused to wait for user intervention. Also,
                              		  some tasks pause automatically in the task sequence to allow for manual
                              		  interaction. We recommend that you set up email notification (Standard
                              		  option) before you run any tasks in order to be notified of pauses or errors
                              		  that may require your attention when the task runs.

## Test Email

When setting up email notification, click the Send Test email button to verify that the Cisco Prime
                              		  Collaboration Deployment mail system can send email to your mail server. Check that
                              		  the test email was received. Perform this test before you run tasks.

| Note | If you have to configure a VMware in various ESXi host servers,
                                          			 ensure that you enter a unique name for ESXi host servers and avoid using the
                                          			 default name from OVA. |
|---|---|