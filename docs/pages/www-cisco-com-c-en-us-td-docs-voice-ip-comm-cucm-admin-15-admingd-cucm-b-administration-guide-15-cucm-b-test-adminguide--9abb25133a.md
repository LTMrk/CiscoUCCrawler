---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-15-admingd-cucm-b-administration-guide-15-cucm-b-test-adminguide--9abb25133a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/adminGd/cucm_b_administration-guide-15/cucm_b_test-adminguide_chapter_011111.html
retrieved_at: 2026-08-17T00:38:26.378176+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 31, 2025

Chapter: Troubleshooting Address Change Issues

## Chapter: Troubleshooting Address Change Issues

# Troubleshooting Address Change Issues

## Troubleshoot
                        	 Cluster Authentication

You can
                              		  troubleshoot cluster authentication issues on subscriber nodes using the
                              		  Command Line Interface (CLI).

Step 1

Enter show network eth0 [detail] to verify network
                                       			 configuration.

Step 2

Enter show network cluster to verify the network
                                       			 cluster information.

If the
                                             				  output displays incorrect publisher information, enter the set network cluster publisher [hostname/IP
                                                   						address] CLI command on the subscriber node to correct the
                                             				  information.

If you are
                                             				  on a publisher node, and the show network cluster CLI command displays
                                             				  incorrect subscriber information, login to Cisco Unified
                                                					 Communications Manager Administration and choose System > Server to check the output.

If you are
                                             				  on a subscriber node and the show network cluster output displays incorrect
                                             				  publisher information, use the set
                                                					 network cluster publisher [hostname | IP_address] CLI command to
                                             				  change the publisher hostname or IP address.

## Troubleshoot
                        	 Database Replication

- Verify that database
                                    			 replication is in a correct state in the cluster.

- Repair and reestablish
                                    			 database replication for the nodes.

- Reset database
                                    			 replication.

For more information about these commands or using the CLI, see the Command Line Interface Guide for Cisco Unified Communications
                                 			 Solutions .

### Verify Database
                           	 Replication

Use the Command
                                 		  Line Interface (CLI) to check the database replication status for all nodes in
                                 		  the cluster. Verify that the Replication Setup (RTMT) & Details shows a
                                 		  value of 2 . Anything other than 2 means that there is a
                                 		  problem with database replication and that you need to reset replication for
                                 		  the node. See topics related to database replication examples for example
                                 		  output.

Step 1

Enter utils dbreplication runtimestate on the first
                                          			 node to check database replication on all nodes in the cluster.

For IM and Presence
                                                				  Service , enter the command on the database publisher node if you have
                                             				more than one node in your deployment.

Tip

If
                                                         				  replication is not set up for the nodes in your cluster, you can reset database
                                                         				  replication for the nodes using the CLI. For more information, see topics
                                                         				  related to resetting database replication using the CLI.

#### Example:

```
admin: utils dbreplication runtimestate

DDB and Replication Services: ALL RUNNING

DB CLI Status: No other dbreplication CLI is running...

Cluster Replication State: BROADCAST SYNC Completed on 1 servers at: 2013-09-26-15-18
     Last Sync Result: SYNC COMPLETED 257 tables sync'ed out of 257
     Sync Errors: NO ERRORS

DB Version: ccm9_0_1_10000_9000
Number of replicated tables: 257
Repltimeout set to: 300s

Cluster Detailed View from PUB (2 Servers):

                         PING        REPLICATION REPL. DBver& REPL. REPLICATION SETUP
SERVER-NAME IP ADDRESS   (msec) RPC? STATUS      QUEUE TABLES LOOP? (RTMT) & details
----------- ------------ ------ ---- ----------- ----- ------ ----- -----------------
server1     100.10.10.17 0.052  Yes  Connected   0     match  Yes   (2) PUB Setup Completed
server2     100.10.10.14 0.166  Yes  Connected   0     match  Yes   (2) Setup Completed
```

Step 2

Verify the
                                          			 output.

The output
                                             				should show a replication status of Connected and a replication setup value of (2)
                                                				  Setup Complete for each node. This means that the replication
                                             				network within the cluster is functioning properly. If the output results are
                                             				different, proceed to troubleshoot and repair database replication.

#### Example Database
                              	 Replication CLI Output

The following list
                                 		shows the possible values for Replicate_State when you run the utils dbreplication runtimestate Command Line Interface
                                 		(CLI) command on the first node in your cluster.

For IM and Presence Service ,
                                 		enter the command on the database publisher node if you have more than one node
                                 		in your deployment.

0 - Replication
                                          			 Not Started. Either no subscribers exist, or the Database Layer Monitor service
                                          			 has not been running since the subscriber was installed.

1 - Replicates
                                          			 have been created, but their count is incorrect.

2 - Replication
                                          			 is good.

3 - Replication
                                          			 is bad in the cluster.

4 - Replication
                                          			 setup did not succeed.

It is important to
                                             		  verify that the Replication Setup (RTMT) & Details shows a value of 2 .
                                             		  Anything other than 2 means that there is a problem with database replication
                                             		  and that you need to reset replication. For information about resolving
                                             		  database replication issues, see topics related to troubleshooting database
                                             		  replication.

##### Example CLI
                                    		  Output for Cisco Unified Communications Manager Node

In this example,
                                    		  the Replication Setup (RTMT) & Details shows a value of 2 .
                                    		  Replication is good.

```
admin: utils dbreplication runtimestate Server Time: Mon Jun 1 12:00:00 EDT 2013

Cluster Replication State: BROADCAST SYNC Completed on 1 servers at: 2013-06-01-12-00
   Last Sync Result: SYNC COMPLETED on 672 tables out of 672
   Sync Status: NO ERRORS
   Use CLI to see detail: 'file view activelog cm/trace/dbl/2013_06_01_12_00_00_dbl_repl_output_Broadcast.log'

DB Version: ccm10_0_1_10000_1
Repltimeout set to: 300s
PROCESS option set to: 1

Cluster Detailed View from uc10-pub (2 Servers):

                        PING       Replication  REPLICATION SETUP
SERVER-NAME IP ADDRESS (msec) RPC? Group ID     (RTMT) & Details
----------- ---------- ------ ---- ----------- -------------------
uc10-pub    192.0.2.95 0.040  Yes  		(g_2) 				(2) Setup Completed
uc10-sub1   192.0.2.96 0.282  Yes  		(g_3) 				(2) Setup Completed
```

##### Example CLI
                                    		  Output for IM and Presence Service Node

In this example,
                                    		  the Replication Setup (RTMT) & Details shows a value of 2 .
                                    		  Replication is good.

```
admin: utils dbreplication runtimestate Server Time: Mon Jun 1 12:00:00 EDT 2013

DB and Replication Services: ALL RUNNING

Cluster Replication State: Replication status command started at: 2012-02-26-09-40
   Replication status command COMPLETED 269 tables checked out of 269
   No Errors or Mismatches found.
   Use 'file view activelog cm/trace/dbl/sdi/ReplicationStatus.2012_02_26_09_40_34.out' to see the details

DB Version: ccm8_6_3_10000_23
Number of replicated tables: 269

Cluster Detailed View from PUB (2 Servers):

                        PING       REPLICATION   REPL. DBver&  REPL.  REPLICATION SETUP
SERVER-NAME IP ADDRESS (msec) RPC? STATUS        QUEUE TABLES  LOOP? (RTMT) & details
----------- ------------ ------ ---- ----------- ----- ------- -----  -----------------
gwydla020218 10.53.46.130 0.038 Yes Connected    0     match   Yes   (2) PUB Setup Completed
gwydla020220 10.53.46.133 0.248 Yes Connected    128   match   Yes   (2) Setup Completed
```

### Repair Database
                           	 Replication

Use the Command
                                 		  Line Interface (CLI) to repair database replication.

Step 1

Enter utils dbreplication repair all on the first
                                          			 node to attempt to repair database replication.

For IM and Presence
                                                				  Service , repair the database replication status from the database
                                             				publisher node if you have more than one node in your deployment.

Depending on
                                             				the size of the database, it may take several minutes to repair database
                                             				replication. Proceed to the next step to monitor the progress of database
                                             				replication repair.

#### Example:

```
admin:utils dbreplication repair all
-------------------- utils dbreplication repair --------------------

Replication Repair is now running in the background.
Use command 'utils dbreplication runtimestate' to check its progress

Output will be in file cm/trace/dbl/sdi/ReplicationRepair.2013_05_11_12_33_57.out

Please use "file view activelog cm/trace/dbl/sdi/ReplicationRepair.2013_05_11_12_33_57.out " command to see the output
```

Step 2

Enter utils dbreplication runtimestate on the first
                                          			 node to check the progress of replication repair.

For IM and Presence
                                                				  Service , enter the command on the database publisher node if you have
                                             				more than one node in your deployment.

The bolded
                                             				text in the example replication output highlights the final status of the
                                             				replication repair.

#### Example:

```
admin:utils dbreplication runtimestate

DB and Replication Services: ALL RUNNING

Cluster Replication State: Replication repair command started at: 2013-05-11-12-33 Replication repair command COMPLETED 269 tables processed out of 269
     No Errors or Mismatches found. Use 'file view activelog cm/trace/dbl/sdi/ReplicationRepair.2013_05_11_12_33_57.out' to see the details

DB Version: ccm8_6_4_98000_192
Number of replicated tables: 269

Cluster Detailed View from PUB (2 Servers):

                         PING        REPLICATION REPL. DBver& REPL. REPLICATION SETUP
SERVER-NAME IP ADDRESS   (msec) RPC? STATUS      QUEUE TABLES LOOP? (RTMT) & details
----------- ------------ ------ ---- ----------- ----- ------ ----- -----------------
server1     100.10.10.17 0.052  Yes  Connected   0     match  Yes   (2) PUB Setup Completed
server2     100.10.10.14 0.166  Yes  Connected   0     match  Yes   (2) Setup Completed
```

If
                                                				  replication repair runs to completion without any errors or mismatches, run the
                                                				  procedure to verify the node name change again to validate that the new node
                                                				  name is now correctly replicated.

If errors
                                                				  or mismatches are found, there may be a transient mismatch between nodes. Run
                                                				  the procedure to repair database replication again.

If, after
                                                         				  several attempts to repair replication, mismatches or errors are being
                                                         				  reported, contact your Cisco Support Representative to resolve this issue.

Step 3

Enter utils dbreplication reset all on the first
                                          			 node to attempt to reestablish replication.

For IM and Presence
                                                				  Service , enter the command on the database publisher node if you have
                                             				more than one node in the deployment.

Depending on
                                             				the size of the database, it may take several minutes to over an hour for
                                             				replication to be fully reestablished. Proceed to the next step to monitor the
                                             				progress of database replication reestablishment.

#### Example:

```
admin:utils dbreplication reset all
This command will try to start Replication reset and will return in 1-2 minutes.
Background repair of replication will continue after that for 1 hour.
Please watch RTMT replication state. It should go from 0 to 2. When all subs
have an RTMT Replicate State of 2, replication is complete.
If Sub replication state becomes 4 or 1, there is an error in replication setup.
Monitor the RTMT counters on all subs to determine when replication is complete.
Error details if found will be listed below
OK [10.53.56.14]
```

Step 4

Enter utils dbreplication runtimestate on the first
                                          			 node to monitor the progress of the attempt to reestablish database
                                          			 replication.

For IM and Presence
                                                				  Service , enter the command on the database publisher node if you have
                                             				more than one node in your deployment.

Replication is
                                             				considered to be reestablished when all nodes show a replication status of Connected and a replication setup value of (2)
                                                				  Setup Complete .

#### Example:

```
admin: utils dbreplication runtimestate

DDB and Replication Services: ALL RUNNING

DB CLI Status: No other dbreplication CLI is running...

Cluster Replication State: BROADCAST SYNC Completed on 1 servers at: 2013-09-26-15-18
     Last Sync Result: SYNC COMPLETED 257 tables sync'ed out of 257
     Sync Errors: NO ERRORS

DB Version: ccm9_0_1_10000_9000
Number of replicated tables: 257
Repltimeout set to: 300s

Cluster Detailed View from newserver100 (2 Servers):
                            PING       REPLICATION REPL. DBver& REPL. REPLICATION SETUP
SERVER-NAME IP ADDRESS     (msec) RPC? STATUS      QUEUE TABLES LOOP? (RTMT) & details
----------- -------------- ------ ---- ----------- ----- ------ ----- -----------------
server1     100.10.10.201  0.038  Yes  Connected   0     match  Yes   (2) PUB Setup Completed
server2     100.10.10.202  0.248  Yes  Connected   0     match  Yes   (2) Setup Completed
server3     100.10.10.203  0.248  Yes  Connected   0     match  Yes   (2) Setup Completed
server4     100.10.10.204  0.248  Yes  Connected   0
```

If
                                                				  replication is reestablished, run the procedure to verify the node name change
                                                				  again to validate that the new node name is now correctly replicated.

If
                                                				  replication does not recover, contact your Cisco Support Representative to
                                                				  resolve this issue.

Caution

Do not
                                                         				  proceed beyond this point if database replication is broken.

### Reset Database
                           	 Replication

Reset database
                                 		  replication if replication is not set up for the nodes in your cluster. You can
                                 		  reset database replication using the command line interface (CLI).

#### Before you begin

Check database
                                 		  replication status for all nodes in the cluster. Verify that the Replication
                                 		  Setup (RTMT) & Details shows a value of 2 .
                                 		  Anything other than 2 means that there is a problem with database replication
                                 		  and that you need to reset replication for the node.

Step 1

Reset
                                          			 replication on nodes in your cluster. Do one of the following:

For
                                                				  Unified Communications Manager, enter utils db replication reset all .

Before you
                                                   					 run this CLI command on any Cisco Unified
                                                      						Communications Manager nodes, first run the command utils dbreplication stop on all
                                                   					 subscriber nodes that are reset, and then on the publisher server. For more
                                                   					 information, see the Command Line Interface Guide for Cisco Unified Communications
                                                      						Solutions .

For IM and Presence
                                                   					 Service , enter utils db replication reset all on the
                                                				  database publisher node to reset all IM and Presence
                                                   					 Service nodes in the cluster.

Tip

You can
                                                         				  enter a specific hostname instead of all to reset database replication on only that node.
                                                         				  For more information, see the Command
                                                            					 Line Interface Guide for Cisco Unified Communications Solutions .

Step 2

Enter utils dbreplication runtimestate to check the
                                          			 database replication status.

## Troubleshoot
                        	 Network

You can
                              		  troubleshoot network issues on nodes using the Command Line Interface (CLI).

Step 1

Enter show network eth0
                                             				  [detail] to verify network configuration.

Step 2

If any of the
                                       			 fields are missing, then reset the network interface.

Enter set network status eth0
                                                   						down .

Enter set network status eth0
                                                   						up .

Step 3

Verify the IP
                                       			 address, mask, and gateway.

### Network Time Protocol troubleshooting

## Troubleshoot NTP
                        	 on Subscriber Nodes

You can troubleshoot Network Time Protocol (NTP) issues on subscriber
                              		  nodes using the Command Line Interface (CLI).

Step 1

Enter show network eth0 [detail] to verify network
                                       			 configuration.

Step 2

Enter utils ntp status to verify NTP status.

Step 3

Enter utils ntp restart to Restart NTP.

Step 4

Enter show network cluster to verify the network
                                       			 cluster.

If the output displays incorrect publisher information, use the set network cluster publisher
                                             				  [hostname/IP_address] CLI command to reset the publisher.

## Troubleshoot NTP
                        	 on Publisher Nodes

You can troubleshoot Network Time Protocol (NTP) issues on publisher
                              		  nodes using the Command Line Interface (CLI).

Step 1

Enter show network eth0 [detail] to verify network
                                       			 configuration.

Step 2

Enter utils ntp status to verify NTP status.

Step 3

Enter utils ntp restart to Restart NTP.

Step 4

Enter utils ntp server list to verify NTP servers.

To add or delete an NTP server, use the utils ntp server [add/delete] CLI command.

| Step 1 | Enter show network eth0 [detail] to verify network
                                       			 configuration. |
|---|---|
| Step 2 | Enter show network cluster to verify the network
                                       			 cluster information. If the
                                             				  output displays incorrect publisher information, enter the set network cluster publisher [hostname/IP
                                                   						address] CLI command on the subscriber node to correct the
                                             				  information. If you are
                                             				  on a publisher node, and the show network cluster CLI command displays
                                             				  incorrect subscriber information, login to Cisco Unified
                                                					 Communications Manager Administration and choose System > Server to check the output. If you are
                                             				  on a subscriber node and the show network cluster output displays incorrect
                                             				  publisher information, use the set
                                                					 network cluster publisher [hostname \| IP_address] CLI command to
                                             				  change the publisher hostname or IP address. |

| Step 1 | Enter utils dbreplication runtimestate on the first
                                          			 node to check database replication on all nodes in the cluster. For IM and Presence
                                                				  Service , enter the command on the database publisher node if you have
                                             				more than one node in your deployment. Tip If
                                                         				  replication is not set up for the nodes in your cluster, you can reset database
                                                         				  replication for the nodes using the CLI. For more information, see topics
                                                         				  related to resetting database replication using the CLI. Example: admin: utils dbreplication runtimestate

DDB and Replication Services: ALL RUNNING

DB CLI Status: No other dbreplication CLI is running...

Cluster Replication State: BROADCAST SYNC Completed on 1 servers at: 2013-09-26-15-18
     Last Sync Result: SYNC COMPLETED 257 tables sync'ed out of 257
     Sync Errors: NO ERRORS

DB Version: ccm9_0_1_10000_9000
Number of replicated tables: 257
Repltimeout set to: 300s

Cluster Detailed View from PUB (2 Servers):

                         PING        REPLICATION REPL. DBver& REPL. REPLICATION SETUP
SERVER-NAME IP ADDRESS   (msec) RPC? STATUS      QUEUE TABLES LOOP? (RTMT) & details
----------- ------------ ------ ---- ----------- ----- ------ ----- -----------------
server1     100.10.10.17 0.052  Yes  Connected   0     match  Yes   (2) PUB Setup Completed
server2     100.10.10.14 0.166  Yes  Connected   0     match  Yes   (2) Setup Completed | Tip | If
                                                         				  replication is not set up for the nodes in your cluster, you can reset database
                                                         				  replication for the nodes using the CLI. For more information, see topics
                                                         				  related to resetting database replication using the CLI. |
|---|---|---|---|
| Tip | If
                                                         				  replication is not set up for the nodes in your cluster, you can reset database
                                                         				  replication for the nodes using the CLI. For more information, see topics
                                                         				  related to resetting database replication using the CLI. |
| Step 2 | Verify the
                                          			 output. The output
                                             				should show a replication status of Connected and a replication setup value of (2)
                                                				  Setup Complete for each node. This means that the replication
                                             				network within the cluster is functioning properly. If the output results are
                                             				different, proceed to troubleshoot and repair database replication. |

| Tip | If
                                                         				  replication is not set up for the nodes in your cluster, you can reset database
                                                         				  replication for the nodes using the CLI. For more information, see topics
                                                         				  related to resetting database replication using the CLI. |
|---|---|

| Note | It is important to
                                             		  verify that the Replication Setup (RTMT) & Details shows a value of 2 .
                                             		  Anything other than 2 means that there is a problem with database replication
                                             		  and that you need to reset replication. For information about resolving
                                             		  database replication issues, see topics related to troubleshooting database
                                             		  replication. |
|---|---|

| Step 1 | Enter utils dbreplication repair all on the first
                                          			 node to attempt to repair database replication. For IM and Presence
                                                				  Service , repair the database replication status from the database
                                             				publisher node if you have more than one node in your deployment. Depending on
                                             				the size of the database, it may take several minutes to repair database
                                             				replication. Proceed to the next step to monitor the progress of database
                                             				replication repair. Example: admin:utils dbreplication repair all
-------------------- utils dbreplication repair --------------------

Replication Repair is now running in the background.
Use command 'utils dbreplication runtimestate' to check its progress

Output will be in file cm/trace/dbl/sdi/ReplicationRepair.2013_05_11_12_33_57.out

Please use "file view activelog cm/trace/dbl/sdi/ReplicationRepair.2013_05_11_12_33_57.out " command to see the output |
|---|---|
| Step 2 | Enter utils dbreplication runtimestate on the first
                                          			 node to check the progress of replication repair. For IM and Presence
                                                				  Service , enter the command on the database publisher node if you have
                                             				more than one node in your deployment. The bolded
                                             				text in the example replication output highlights the final status of the
                                             				replication repair. Example: admin:utils dbreplication runtimestate

DB and Replication Services: ALL RUNNING

Cluster Replication State: Replication repair command started at: 2013-05-11-12-33 Replication repair command COMPLETED 269 tables processed out of 269
     No Errors or Mismatches found. Use 'file view activelog cm/trace/dbl/sdi/ReplicationRepair.2013_05_11_12_33_57.out' to see the details

DB Version: ccm8_6_4_98000_192
Number of replicated tables: 269

Cluster Detailed View from PUB (2 Servers):

                         PING        REPLICATION REPL. DBver& REPL. REPLICATION SETUP
SERVER-NAME IP ADDRESS   (msec) RPC? STATUS      QUEUE TABLES LOOP? (RTMT) & details
----------- ------------ ------ ---- ----------- ----- ------ ----- -----------------
server1     100.10.10.17 0.052  Yes  Connected   0     match  Yes   (2) PUB Setup Completed
server2     100.10.10.14 0.166  Yes  Connected   0     match  Yes   (2) Setup Completed If
                                                				  replication repair runs to completion without any errors or mismatches, run the
                                                				  procedure to verify the node name change again to validate that the new node
                                                				  name is now correctly replicated. If errors
                                                				  or mismatches are found, there may be a transient mismatch between nodes. Run
                                                				  the procedure to repair database replication again. Note If, after
                                                         				  several attempts to repair replication, mismatches or errors are being
                                                         				  reported, contact your Cisco Support Representative to resolve this issue. | Note | If, after
                                                         				  several attempts to repair replication, mismatches or errors are being
                                                         				  reported, contact your Cisco Support Representative to resolve this issue. |
| Note | If, after
                                                         				  several attempts to repair replication, mismatches or errors are being
                                                         				  reported, contact your Cisco Support Representative to resolve this issue. |
| Step 3 | Enter utils dbreplication reset all on the first
                                          			 node to attempt to reestablish replication. For IM and Presence
                                                				  Service , enter the command on the database publisher node if you have
                                             				more than one node in the deployment. Depending on
                                             				the size of the database, it may take several minutes to over an hour for
                                             				replication to be fully reestablished. Proceed to the next step to monitor the
                                             				progress of database replication reestablishment. Example: admin:utils dbreplication reset all
This command will try to start Replication reset and will return in 1-2 minutes.
Background repair of replication will continue after that for 1 hour.
Please watch RTMT replication state. It should go from 0 to 2. When all subs
have an RTMT Replicate State of 2, replication is complete.
If Sub replication state becomes 4 or 1, there is an error in replication setup.
Monitor the RTMT counters on all subs to determine when replication is complete.
Error details if found will be listed below
OK [10.53.56.14] |
| Step 4 | Enter utils dbreplication runtimestate on the first
                                          			 node to monitor the progress of the attempt to reestablish database
                                          			 replication. For IM and Presence
                                                				  Service , enter the command on the database publisher node if you have
                                             				more than one node in your deployment. Replication is
                                             				considered to be reestablished when all nodes show a replication status of Connected and a replication setup value of (2)
                                                				  Setup Complete . Example: admin: utils dbreplication runtimestate

DDB and Replication Services: ALL RUNNING

DB CLI Status: No other dbreplication CLI is running...

Cluster Replication State: BROADCAST SYNC Completed on 1 servers at: 2013-09-26-15-18
     Last Sync Result: SYNC COMPLETED 257 tables sync'ed out of 257
     Sync Errors: NO ERRORS

DB Version: ccm9_0_1_10000_9000
Number of replicated tables: 257
Repltimeout set to: 300s

Cluster Detailed View from newserver100 (2 Servers):
                            PING       REPLICATION REPL. DBver& REPL. REPLICATION SETUP
SERVER-NAME IP ADDRESS     (msec) RPC? STATUS      QUEUE TABLES LOOP? (RTMT) & details
----------- -------------- ------ ---- ----------- ----- ------ ----- -----------------
server1     100.10.10.201  0.038  Yes  Connected   0     match  Yes   (2) PUB Setup Completed
server2     100.10.10.202  0.248  Yes  Connected   0     match  Yes   (2) Setup Completed
server3     100.10.10.203  0.248  Yes  Connected   0     match  Yes   (2) Setup Completed
server4     100.10.10.204  0.248  Yes  Connected   0 If
                                                				  replication is reestablished, run the procedure to verify the node name change
                                                				  again to validate that the new node name is now correctly replicated. If
                                                				  replication does not recover, contact your Cisco Support Representative to
                                                				  resolve this issue. Caution Do not
                                                         				  proceed beyond this point if database replication is broken. | Caution | Do not
                                                         				  proceed beyond this point if database replication is broken. |
| Caution | Do not
                                                         				  proceed beyond this point if database replication is broken. |

| Note | If, after
                                                         				  several attempts to repair replication, mismatches or errors are being
                                                         				  reported, contact your Cisco Support Representative to resolve this issue. |
|---|---|

| Caution | Do not
                                                         				  proceed beyond this point if database replication is broken. |
|---|---|

| Step 1 | Reset
                                          			 replication on nodes in your cluster. Do one of the following: For
                                                				  Unified Communications Manager, enter utils db replication reset all . Before you
                                                   					 run this CLI command on any Cisco Unified
                                                      						Communications Manager nodes, first run the command utils dbreplication stop on all
                                                   					 subscriber nodes that are reset, and then on the publisher server. For more
                                                   					 information, see the Command Line Interface Guide for Cisco Unified Communications
                                                      						Solutions . For IM and Presence
                                                   					 Service , enter utils db replication reset all on the
                                                				  database publisher node to reset all IM and Presence
                                                   					 Service nodes in the cluster. Tip You can
                                                         				  enter a specific hostname instead of all to reset database replication on only that node.
                                                         				  For more information, see the Command
                                                            					 Line Interface Guide for Cisco Unified Communications Solutions . | Tip | You can
                                                         				  enter a specific hostname instead of all to reset database replication on only that node.
                                                         				  For more information, see the Command
                                                            					 Line Interface Guide for Cisco Unified Communications Solutions . |
|---|---|---|---|
| Tip | You can
                                                         				  enter a specific hostname instead of all to reset database replication on only that node.
                                                         				  For more information, see the Command
                                                            					 Line Interface Guide for Cisco Unified Communications Solutions . |
| Step 2 | Enter utils dbreplication runtimestate to check the
                                          			 database replication status. For IM and Presence
                                             				Service , run the CLI command on the IM and Presence database
                                          			 publisher node |

| Tip | You can
                                                         				  enter a specific hostname instead of all to reset database replication on only that node.
                                                         				  For more information, see the Command
                                                            					 Line Interface Guide for Cisco Unified Communications Solutions . |
|---|---|

| Step 1 | Enter show network eth0
                                             				  [detail] to verify network configuration. |
|---|---|
| Step 2 | If any of the
                                       			 fields are missing, then reset the network interface. Enter set network status eth0
                                                   						down . Enter set network status eth0
                                                   						up . |
| Step 3 | Verify the IP
                                       			 address, mask, and gateway. Ensure that
                                       			 these values are unique across the network. |

| Step 1 | Enter show network eth0 [detail] to verify network
                                       			 configuration. |
|---|---|
| Step 2 | Enter utils ntp status to verify NTP status. |
| Step 3 | Enter utils ntp restart to Restart NTP. |
| Step 4 | Enter show network cluster to verify the network
                                       			 cluster. If the output displays incorrect publisher information, use the set network cluster publisher
                                             				  [hostname/IP_address] CLI command to reset the publisher. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enter show network eth0 [detail] to verify network
                                       			 configuration. |  |
| Step 2 | Enter utils ntp status to verify NTP status. |  |
| Step 3 | Enter utils ntp restart to Restart NTP. |  |
| Step 4 | Enter utils ntp server list to verify NTP servers. | To add or delete an NTP server, use the utils ntp server [add/delete] CLI command. |