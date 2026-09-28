---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-15-cucm-b-pcd-admin-guide-15-cucm-b-pcd-admin-guide-1401-chapt-723450b117
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/15/cucm_b_pcd-admin-guide-15/cucm_b_pcd-admin-guide-1401_chapter_01010.html
retrieved_at: 2026-08-17T00:33:32.748898+00:00
---

Prime Collaboration Deployment Administration Guide, Release 15 and SUs

# Prime Collaboration Deployment Administration Guide, Release 15 and SUs

Updated: February 5, 2026

Chapter: Cisco Prime Collaboration Deployment Troubleshooting

## Chapter: Cisco Prime Collaboration Deployment Troubleshooting

# Cisco Prime Collaboration Deployment Troubleshooting

## Increase Disk Space for Migrations

If one Cisco Prime Collaboration Deployment server is used to migrate a large number of Unified Communications Manager servers
                              concurrently, the Cisco Prime Collaboration Deployment disk can run low on space, and this can cause migration tasks to fail.
                              If you plan to use a Cisco Prime Collaboration Deployment system to migrate several servers concurrently, you can use this
                              procedure to increase the disk size.

Step 1

Shut down the Cisco Prime Collaboration Deployment server by logging in to the Cisco Prime Collaboration Deployment CLI and
                                       entering the utils system shutdown command.

Step 2

After the Cisco Prime Collaboration Deployment server shuts down, go to ESXi host and increase the disk size for the virtual machine on which the Cisco Prime Collaboration Deployment server resides.

Step 3

Restart the Cisco Prime Collaboration Deployment server.

Step 4

To view how much disk space is available on the Cisco Prime Collaboration Deployment server, run the CLI command show status on the Cisco Prime Collaboration Deployment server.

## General
                        	 Troubleshooting Issues

### View Step-By-Step Log of Events

Use the View Log buttons on the Monitoring dashboard to see a step-by-step log of Cisco Prime
                              		  Collaboration Deployment events.

### Access Cisco
                              		  Prime Collaboration Deployment Logs

Obtain additional
                              		  details by accessing Cisco Prime Collaboration Deployment logs using CLI
                              		  commands. For example:

file get activelog
                                 			 tomcat/logs/ucmap/log4j/*

### Check For
                              		  Problems Before You Start a Task

Use the Validate button to check for problems before starting a task. When the validation process identifies problems, click the View Log button to see more detail.

### Node
                              		  Information Mismatches

Some mismatches
                              		  between node information that is stored in Cisco Prime Collaboration Deployment and the
                              		  actual node can be fixed automatically (for example, active versions). Other
                              		  information will require a rediscovery to correct the problem.

### Verify
                              		  Communication Between Servers

Use the network
                                 			 capture CLI command to verify communication between
                              		  servers (for example, to confirm that packets are being sent to and received by the correct ports).

## Errors Seen in View Log

The View Log
                              		  button on the Monitoring dashboard can be used to see a step by step log of
                              		  Cisco Prime Collaboration Deployment events during the task. When viewing the
                              		  log, there may be events or errors that are shown. Some of the more common
                              		  errors, and possible actions to correct those errors, are shown below:

### Node
                              		  Connection and Contact Issues

Error messages:

- "The network diagnostic
                                    			 service indicates node {0} has a network issue. The network settings cannot be
                                    			 changed until the network issue is resolved."

- "The node could not be
                                    			 located."

- "The node could not be
                                    			 contacted.
                                    		  "

Possible actions to correct
                                 			 node connection and contact issues:

- Check the network settings
                                 			 and firewall settings for the indicated node and ensure that the Cisco Prime
                                 			 Collaboration Deployment server can communicate with the node.

- Check to see if the node
                                 			 is powered off, if the node name is misspelled, or if the node is inaccessible.

### Other Connection Issues

Error message:

- "The switch version status
                                    			 could not be determined. Please manually verify that the switch version
                                    			 completed."

Possible actions to correct issues:

During a switch version task, if the server does not respond in a
                              		  fixed amount of time, this message may appear even if the task is successful. you see this error, log in to the CLI for
                              the server that is not
                              		  responding and run the show version active command to see if the switch
                              		  version was successful. For example, a switch version on a Cisco Unified Contact Center Express server can
                              		  take more than 60 minutes.

### Node
                              		  Response

Error messages:

- "The node did not respond
                                    			 within the expected time frame."

- "The upgrade service for
                                    			 node {0} did not send back the expected response. This is assumed to be a
                                    			 failure. However, this can also happen when network connectivity is temporarily
                                    			 lost. Please manually verify the upgrade status on node {0} before proceeding."

Possible actions to correct
                                 			 issues:

These messages are
                              		  usually seen during a task (install, upgrade, and so on), when the new node does not
                              		  contact the Cisco Prime Collaboration Deployment server within a specified
                              		  amount of time. For an upgrade, this time is 8 hours, so when one of these error messages appear, it may
                              		  indicate that the task failed. However, these error messages can also indicate that there
                              		  were network issues during the upgrade (or install) that prevented the server
                              		  from contacting Cisco Prime Collaboration Deployment. For this reason, you see one of these messages, log in to the server
                              that is not responding (using the
                              		  CLI) and run the show
                                 			 version active command to see if the upgrade was successful.

### Unable to
                              		  Mount Datastore

Error message:

- "Unable to mount datastore
                                    			 xxx_NFS on ESXi host <hostname>.
                                    		  "

Possible actions to correct
                                 			 the issue:

This error occurs
                              		  when your Network File System (NFS) Datastore has an issue. Datastore issues can occur when Cisco Prime
                              		  Collaboration Deployment is shut down unexpectedly. When this error occurs,
                              		  check the ESXi host and unmount the old NFS mount. Then delete and add back the
                              		  ESXi host to Cisco Prime Collaboration Deployment.

### Unable to Add ESXi Host to Inventory

Error message:

- "Unable to add ESXi host xxxxxxx. "

Possible cause:

This error may be caused by a networking issue with the vSwitch on the
                              		  ESXi host.

Possible actions to correct the issue:

- Ping the host and verify
                                 			 connectivity by entering the following CLI command: utils network ping hostname .

- Verify that the license
                                 			 for the ESXi host is valid. A demo license is not supported.

- Be aware that you need
                                 			 root access to the ESXi host. Use the root username and password when adding
                                 			 ESXi host credentials.

- Be aware that if you are
                                 			 using network address translation (NAT), Cisco Prime Collaboration Deployment
                                 			 and all nodes in the clusters must be behind the same NAT to ensure successful
                                 			 communication between Cisco Prime Collaboration and the nodes.

### Unable to
                              		  Power On Virtual Machine

Error message:

- "Unable to power on the VM
                                    			 named xxx on ESXi host xxxxxxx.
                                    		  "

Possible actions to correct
                                 			 issue:

Check the ESXi
                              		  host that the VM resides on. From the Tasks and
                                 			 Events tab, check the time stamp for when Cisco Prime Collaboration
                              		  Deployment tried to power on the VM. Determine whether too many VMs
                              		  are already on that host. If that is the case, you may need to power off a VM that
                              		  is not being used for this cluster.

### The Power
                              		  State of a Virtual Machine

Error message:

- "The power state of VM
                                    			 xxxxx in ESXi host XX.XX.X.XX needs to be OFF. The task is now paused."

Possible actions to correct
                                 			 issue:

VMs that are to be used
                              		  in a destination cluster for a migration task, or for a new cluster installation,
                              		  must be in the OFF state. If you receive this error message, check the named
                              		  VM. If it is not off, power it off. Then, retry or resume the task.

### Username
                              		  and/or Password Not Valid

Error message:

- " The username and/or
                                    			 password is not valid."

Possible actions to
                                 			 correct the issue:

Correct the administrator
                              		  name and password for this server in the cluster page. You can then rediscover
                              		  this node.

### Platform
                              		  Administrative Web Services (PAWS)

Error messages:

- "The Platform
                                    			 Administrative Web Services (PAWS) is not available."

- " Unable to access node
                                    			 {0} via the Platform Administrative Web Services (PAWS) interface."

Possible actions to
                                 			 correct issues:

Ensure that the
                              		  server is reachable, and that the PAWS service is active on the node. When
                              		  you use Cisco Prime Collaboration Deployment to perform an upgrade, switch
                              		  version, or restart task on an application server (for example, to upgrade a Unified Communications Manager server), the
                              		  Platform Administrative Web Service on the application must be active. Otherwise, the Cisco Prime Collaboration Deployment
                              server cannot communicate with the Unified Communications Manager application server.

### {0} VMs
                              		  Named {1} Were Located on ESXi Host {2}

Error message:

- " {0} VMs named {1} were
                                    			 located on ESXi host {2}."

Possible actions to
                                 			 correct issue:

Check that the
                              		  virtual machine named still exists on the ESXi host. Sometimes VMs are moved to
                              		  another ESXi host, and if this is the case, the ESXi host that holds the VM
                              		  must be added into the Cisco Prime Collaboration Deployment server.

### Power State
                              		  of VM {0} in ESXi Host {1} Needs to Be OFF

Error message:

- "The power state of VM
                                    			 {0} in ESXi host {1} needs to be OFF."

Possible actions to
                                 			 correct the issue:

In order for
                              		  Cisco Prime Collaboration Deployment to be installed on or migrate to a VM, the power
                              		  state of the target VMs must be OFF.

### CLI Command
                              		  Timed Out

Error message:

- "CLI command timed out
                                    			 for node {0}."

Possible actions to
                                 			 correct issue:

Check for
                              		  networking, connection, or password issues with the node. Also check to see if
                              		  another operation was in progress (for example, a COP file install) during the
                              		  time that the command timed out.

### Task Paused
                              		  Due to Validation Issues

Error message:

- " Task paused due to
                                    			 validation issues"

Possible actions to
                                 			 correct the issue:

Before it runs a task, the Cisco Prime Collaboration Deployment server will run validation
                              		  checks to ensure that VMs to be used are available, that the ISO file can be
                              		  found, and so on. This message indicates that one or more of the validation
                              		  checks failed. See the log file for more information about which validations
                              		  failed.

## Lock
                        	 Errors

Most products allow only one change at a time (for example, you cannot
                              		  modify Network Time Protocol settings while an upgrade is in progress). If a request is made
                              		  while the node is locked, then a lock message with the following information is
                              		  displayed:

- The name of the resource that was
                                 			 locked

- The ID of the process that
                                 			 locked the resource

- The hostname of the node

You can typically wait a few minutes and try again. For more details,
                              		  use the node CLI to identify the exact process based on the provided process ID
                              		  and hostname.

## NFS
                        	 Datastores

### Exceptions and
                              		  Other NFS-Related Issues

Review the Cisco
                              		  Prime Collaboration Deployment logs for any exceptions or other NFS-related
                              		  issues.

### Use VMware
                              		  vSphere

Use VMware
                              		  vSphere to verify that NFS datastores are available.

### Unmount and
                              		  Remount All Current Datastores

When you restart it, Cisco Tomcat unmounts all current datastores and attempts to remount them.

## Pause States on
                        	 Monitor Page

### Task Is Waiting for Manual Intervention

Certain tasks, such as migration or readdress, pause at a point that
                              		  human intervention may be required. In those tasks, the Cisco Prime
                              		  Collaboration Deployment system inserts a Forced Pause. When the task reaches
                              		  this point, the task is paused and a message appears on the Monitoring page.
                              		  Perform manual steps as needed, and then click the Resume button when you are ready to resume the task.

### Task Paused Due to Validation Issues

When this message is displayed, click the View log link to view more detail on which validations failed.

### Task Paused Due to Task Action Failures

When this message is displayed, click the View log link to view more detail on which tasks failed.

## Scheduling

### Verify Scheduled Date

If a task was  scheduled but did not start, verify the scheduled
                              		  date.

### Validation Tests

When a task starts, Prime Collaboration Deployment runs a series of validation tests. A
                              		  validation failure pauses the task.

### Determine Why a Task Has Been Paused

Use the View Log button to see why a task is paused (for
                              		  example, validation failure, a requested or required pause, one or more nodes
                              		  failed on a partiular step, and so on).

### Canceled Tasks

Some steps cannot be canceled after they are started (for example, restarting a
                              		  server).If you cancel the task, it remains in the Canceling state until
                              		  the step is finished.

## Server
                        	 Connectivity

### Verify
                              		  Connectivity

Use the utils
                                 			 network ping and traceroute CLI commands to verify connectivity.

### Verify Forward
                              		  and Reverse DNS Lookups

Use the utils
                                 			 network host CLI command to verify forward and reverse DNS lookups.

### Platform
                              		  Administrative Web Services

Ensure that
                              		  Platform Administrative Web Services are activated on nodes that are being upgraded,
                              		  restarted, and switch versioned.

### Verify That Ports
                              		  Are Open

Verify that the ports
                              		  listed in the Port Usage guide are open (for example, verify that the NFS and SOAP call-back
                              		  ports are not being blocked by other network devices).

## Task Failure Due
                        	 to Restart

The success or failure of each of the following tasks depends on the
                              		  Prime Collaboration Deployment server being able to get a response from every
                              		  server in the cluster during the task. If connectivity to the servers is lost,
                              		  or if the Prime Collaboration server reboots during a task, the task might show
                              		  a failure even though it may have completed successfully.

### Installation Task
                           	 Failure

#### Problem

The success or
                                 		  failure of each step in the install task depends on the Prime Collaboration
                                 		  Deployment server being able to get a response from every server in the cluster
                                 		  during the installation.

#### Possible
                                 		  Cause

If the Prime
                                 		  Collaboration server reboots during the install task, the installation might
                                 		  show a failure, even though it may have completed successfully.

The following table
                                 		  describes the steps to identify if the task completed successfully on the
                                 		  application server, and, if it did not, how to recover from this type of failure.

#### Solution

If

Then

The
                                             					 failure occurs during installation on the first node

You
                                                   						  must create a new fresh-install task with the same cluster nodes.

In
                                                               							 the case of Unified Communications products such as Cisco Unified
                                                                  								Communications Manager and IM and Presence Service , Cisco Prime Collaboration
                                                               							 Deployment does not support an install task that installs a subsequent node
                                                               							 separately from the cluster.

Check
                                                   						  the status of the VM on the ESXi host that is associated with the destination
                                                   						  cluster. If any VMs were powered on and installed, delete those VMs and
                                                   						  redeploy the OVA.

The installation is successful on the first node but fails on
                                             					 any of the subsequent nodes after Prime Collaboration Deployment loses
                                             					 connectivity

Log in to the failed Unified Communications VM node, such
                                                   						  as Cisco Unified Communications Manager, and manually verify the installation
                                                   						  status. For more information, see Unified Communications product documentation.

Create a new install task with all new cluster nodes. You must restart the installation process by deleting all installed
                                                   VMs,
                                                   						  redeploying the recommended OVA to create new VMs, and creating a new install
                                                   						  task.

If VM names are changed from previous configuration,
                                                               							 you must add a new fresh install cluster, create a new fresh install task, and then
                                                               							 run the task.

Check the status of the VM on the ESXi host that is
                                                   						  associated with the destination cluster. If any VMs were powered on and
                                                   						  installed, delete those VMs and redeploy the OVA.

For more information, see topics relating to install
                                                               							 tasks.

### Upgrade Task
                           	 Failure

#### Problem

The success or
                                 		  failure of each step in the upgrade task depends on the Prime Collaboration
                                 		  Deployment server being able to get a response from every server in the cluster
                                 		  during the upgrade.

#### Possible Cause

If the Prime
                                 		  Collaboration server reboots during an upgrade task, the upgrade might show a
                                 		  failure even though the upgrade may have completed successfully.

The following table describes the steps to determine whether the task completed successfully on the
                                 		  application server and, if it did not, how to recover from this type of failure.

#### Solution

The failure occurs during upgrade on the first node

Check task status on the Monitoring page to see which steps were successful
                                                   						  and which steps failed.

Log in to the first Unified Communications VM node, such
                                                   						  as Cisco Unified
                                                      							 Communications Manager . Check the software version and upgrade status
                                                   						  to verify whether this node was upgraded to a new version. For more information, see
                                                   						  Unified Communications product documentation.

If the upgrade on the first node is successful, you can
                                                   						  create a new upgrade task with the subsequent node.

If the upgrade on the first node is unsuccessful, you can
                                                   						  create a new upgrade task with all nodes.

If the upgrade task was configured with automatic switch
                                                   						  version, check the status of the active and inactive partitions on the Unified
                                                   						  Communications product node. If the automatic switch version was unsuccessful on the
                                                   						  Unified Communications product node, perform a switch version. For more information, see
                                                   						  Unified Communications product documentation.

The upgrade is successful on the first node but fails on any
                                             					 of the subsequent nodes after Prime Collaboration Deployment loses connectivity

Log
                                                   						  in to the failed Unified Communications VM node, such as Cisco Unified
                                                      							 Communications Manager . Check the software version and upgrade status
                                                   						  to verify whether this node was upgraded to a new version. For more information, see
                                                   						  Unified Communications product documentation.

If
                                                   						  the subsequent node shows the new version in the inactive partition, the old
                                                   						  version in active partition, and the upgrade task was configured to switch version automatically, you must either
                                                   perform the automatic switch version manually
                                                   						  on the Cisco Unified Communications Manager node or use Prime Collaboration
                                                   						  Deployment to create a switch version task.

If the upgrade task was configured with automatic switch version
                                                   						  and the subsequent node does not show the version correctly, perform a switch
                                                   						  version. See Unified Communications product documentation more detail.

### Migration Task
                           	 Failure

#### Problem

The success or
                                 		  failure of each step in the migration task depends on the Prime Collaboration
                                 		  Deployment server being able to get a response from every server in the cluster
                                 		  during the migration.

#### Possible Cause

If the Prime
                                 		  Collaboration server reboots during the migration task, the migration might
                                 		  show a failure even though it may have completed successfully.

#### Solution

If the migration
                                 		  task fails after Prime Collaboration Deployment loses connectivity, we recommend that you restart the entire migration
                                 process. To restart the migration task, you must create a new task. If your deployment is a multinode cluster, follow this
                                 procedure:

Check the task status on the Monitoring page to find out which steps were
                                       				successful and which steps failed.

Delete the failed migration task.

### Switch Version
                           	 Task Failure

#### Problem

The success or
                                 		  failure of each step in the switch version task depends on the Prime
                                 		  Collaboration Deployment server being able to get a response from every server
                                 		  in the cluster during the switch version.

#### Possible
                                 		  Cause

If the Prime
                                 		  Collaboration server reboots during the switch version task, the switch version
                                 		  might show a failure even though the switch version may have completed
                                 		  successfully.

The following table describes the steps to determine whether the task completed successfully on the
                                 		  application server, and, if it did not, how to recover from this type of failure.

#### Solution

The
                                             					 failure occurs during switch version on the first node

Log in
                                                   						  to the first Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and manually check the sofware version in both the
                                                   						  active and inactive partitions. For more information, see Unified Communications product
                                                   						  documentation.

If
                                                   						  the first node still shows the old version in the active partition but the new
                                                   						  version in the inactive partition, create a new switch version task with the
                                                   						  same nodes on Prime Collaboration and run the task again.

The switch
                                             					 version is successful on the first node but fails on any of the subsequent
                                             					 nodes after Prime Collaboration Deployment loses connectivity

Log in
                                                   						  to the subsequent Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager). Check the software and switch version status to
                                                   						  verify that the subsequent node is up and running with the correct version.

If
                                                   						  the subsequent node shows the correct new version in the active partition, you
                                                   						  do not need to recreate a switch version task on Prime Collaboration
                                                   						  Deployment.

If
                                                   						  the subsequent node shows the new version in the inactive partition and the old
                                                   						  version in active partition, the switch version was not successful on the
                                                   						  subsequent node. You can either perform a switch version manually on the
                                                   						  subsequent node or create a new switch version task on the subsequent node
                                                   						  on Prime Collaboration Deployment.

### Readdress Task
                           	 Failure

#### Problem

The success or
                                 		  failure of each step in the readdress task depends on the Prime Collaboration
                                 		  Deployment server being able to get a response from every server in the
                                 		  cluster.

#### Possible
                                 		  Cause

If the Prime
                                 		  Collaboration server reboots during the readdress task, you may be notified of
                                 		  a failure even though the readdress may have completed successfully.

The following table describes the steps to determine whether the task completed successfully on the
                                 		  application server, and, if it did not, how to recover from this type of failure.

#### Solution

The
                                             					 failure occurs during readdress on the first node

Log in
                                                   						  to the first Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and verify that network settings were successfully
                                                   						  changed. For more information, see Unified Communications product documentation.

After
                                                   						  you verify that network settings were successfully changed on the first node,
                                                   						  create a new readdress task on the subsequent node on Prime Collaboration
                                                   						  Deployment and run this task. If network settings were not successfully changed
                                                   						  on the first node, create a new readdress task with both nodes on Prime
                                                   						  Collaboration Deployment and run the task again.

The
                                             					 readdress task is successful on the first node but fails on any of the
                                             					 subsequent nodes after Prime Collaboration Deployment loses connectivity

Log in
                                                   						  to the first Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and verify that network settings were successfully
                                                   						  changed. For more information, see Unified Communications product documentation..

After
                                                   						  verifying that network settings were successfully changed on the first node,
                                                   						  you do 
                                                   						  not need to create a new readdress task on the first node on
                                                   						  Prime Collaboration Deployment. However, you do need to create a new readdress task on
                                                   						  the subsequent nodes. If network settings were not successfully changed on the
                                                   						  first node, create a new readdress task with the first node and subsequent
                                                   						  nodes on Prime Collaboration Deployment and run the new task.

Go
                                                            								to the Clusters screen and click the triangle to show the
                                                            								nodes in the cluster.

Check the network settings to ensure that the Cluster Nodes
                                                            								table shows the new network settings (for example, hostname).

If
                                                            								the correct network settings are not displayed, click the Refresh Node link for each node in the cluster.

### Server Restart
                           	 Task Failure

#### Problem

The success or
                                 		  failure of each step in the server restart task depends on the Prime
                                 		  Collaboration Deployment server being able to get a response from every server
                                 		  in the cluster during the server restart.

#### Possible
                                 		  Cause

If the Prime
                                 		  Collaboration server reboots during server restart, the server restart might
                                 		  show a failure, even though the server restart may have completed successfully.

The following table describes the steps to determine whether the task completed successfully on the
                                 		  application server, and, if it did not, how to recover from this type of failure.

#### Solution

The
                                             					 failure occurs during server restart on the first node

Log in
                                                   						  to the first Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and manually check the status of the restart.

If
                                                   						  the first node did not get restarted, recreate a new server restart task with
                                                   						  all nodes and run the task again.

The server
                                             					 restart is successful on the first node but fails on any of the subsequent
                                             					 nodes after Prime Collaboration Deployment loses connectivity

Log
                                                   						  in to the second Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and manually check the status of restart.

If
                                                   						  the subsequent node restarted successfully, there is no need to recreate a new
                                                   						  server restart task. If the subsequent node did not restart, create a new
                                                   						  server restart task on the subsequent node only.

## Task Scheduling

### Task Scheduled but Not Started

If a task was scheduled but did not start, verify the
                              		  scheduled date.

### Validation Failure

When a task starts, a series of validation tests are run. A
                              		  validation failure pauses the task.

### Reasons for a Task Pause

Click the View Log button to see why a task was paused (for example,
                              		  validation failure, a pause was requested or required,, one or more nodes failed on
                              		  a particular step, and so on).

### Tasks That Cannot Be Canceled

Some tasks cannot be canceled once started (for example, restart of a server or installation of a server node). If the task
                              is canceled, it remains in the Canceling state until the
                              		  step is  finished.

## Task
                        	 Timeouts

### Manually
                              		  Verify Results

All Cisco Prime
                              		  Collaboration Deployment tasks have built-in timeouts ranging from 30 minutes
                              		  to 10 hours, depending on the type of task and product. If Cisco Prime
                              		  Collaboration Deployment does not receive the expected results within that time
                              		  frame, Cisco Prime Collaboration Deployment signals an error, even if the
                              		  actual process succeeded. Users must manually verify the results and ignore any
                              		  false negatives.

### Readdress
                              		  Times Out

During readdress,
                              		  if a VLAN change is required, Cisco Prime Collaboration Deployment does not
                              		  receive updates for the nodes. As a result, the readdress eventually
                              		  times out even though the actual readdress process succeeded.

### Resource
                              		  Issues Slowing Down the Nodes

Use VMware vSphere
                              		  to verify that no resource issues are slowing down the nodes. Disk, CPU,
                              		  and memory issues can cause slower than normal logins, which can cause
                              		  connectivity timeout issues during cluster discovery.

### Network
                              		  Congestion

Because large files
                              		  are sent across the network during upgrades, installations, and migrations,
                              		  network congestion can cause tasks to take longer than usual.

## Upgrade Migration
                        	 and Installation

### Virtual
                              		  Machine Does Not Boot

If a VM does not
                              		  boot using the mounted install ISO during migration or installation, verify the
                              		  VM boot order in the Basic Input/Output System (BIOS). We recommend that only
                              		  freshly created VMs that use the official Cisco Open Virtualization Format
                              		  (OVF) files.

### VM Cannot Be
                              		  Located

If a VM cannot be
                              		  located, make sure vMotion is turned off.

### Upgrade File
                              		  List Is Blank

If the list of ISO
                              		  files for upgrade is blank, the reason might be that one or more servers in the
                              		  cluster you are upgrading have an existing upgrade that is stuck. The file list
                              		  shows as blank because the Unified Communications Manager-side upgrade process
                              		  was stuck. Therefore, no files are valid, because no upgrades can be done. If
                              		  you attempt an upgrade from the application server CLI, you may see the message "The resource
                                 			 lock platform.api.network.address is currently locked."

To resolve this
                              		  problem, reboot your Unified Communications Manager server.

### Upgrade ISO or
                              		  COP File Is Not Displayed in the Task Wizard

If an upgrade ISO or COP
                              		  file is not displayed in the task wizard, verify that the file was uploaded
                              		  into the correct directory on the Prime Collaboration Deployment Server. To
                              		  confirm the location of the file, click open and close navigation button and
                              		  choose the Inventory > SFTP Servers
                                    				and Datastore menu option. The directory that is in
                              		  use is usually listed at the top of the task wizard.

### Upgrade ISO
                              		  File Must Be Valid for All Nodes

An upgrade ISO
                              		  file must be valid for all nodes in the task in order to be listed in the
                              		  wizard. If the upgrade ISO file is not listed, verify that the task contains
                              		  the publisher or that the publisher was already upgraded.

### Release 10.x
                              		  and Older Products

Most Release 10.x
                              		  and older products report only generic upgrade and installation failure
                              		  messages. Users must access the failed node directly and diagnose the problem
                              		  by using traditional tools and processes that are specific to that product (for
                              		  example, use the Unified Real-Time Monitoring Tool or the CLI to view upgrade
                              		  logs).

## Run a New Task When Current Task in Canceling State

### Rerun Fresh Install Task

The following procedure provides the high-level steps for rerunning a new task when the current task is in the process of
                                 being canceled. For more detailed information, see topics relating to task management.

Step 1

View the task log to verify the status of the most recent task.

If the VM is powered on and the fresh install task is still in progress, power off the VM, delete it, and redeploy the OVA
                                                to create a new VM. You can use the same name for the new VM.

If the VM is powered off and the fresh install was not started on the VM, leave the VM powered off.

Step 2

Check the cluster to verify if any nodes in the cluster were updated with the active version and discovery status.

- If any nodes were updated with the new version or discovery status, create a new cluster with a  new  name, including the
                                             same VMs and installation settings.

- If any nodes in the cluster were not updated, reuse the cluster when recreating a fresh install task.

Step 3

Create and run a new install task.

### Rerun Migration Task

The following procedure provides the high-level steps for rerunning a migration task for the same source and destination clusters
                                 when the current migration task is in the process of being canceled. For more detailed information, see topics relating to
                                 task management.

Step 1

View the task log to verify the status of the most recent task.

If the VM is powered on and the migration task is still in progress on the destination VM, power off the destination VM, delete
                                                it, and redeploy the OVA to create a new destination VM. You can use the same name for the new VM.

If the VM is powered off and the migration was not started on the VM, leave the VM powered off.

Step 2

Check the node status on the source cluster before running a new task.

- If the source node is powered off, power on the source node and make sure it is in a running state before rerunning a migration
                                             task.

- In the case of network migration, the source node can remain powered on.

Step 3

You do not need to rerun cluster discovery on the source node.

Step 4

Check the destination cluster to ensure that no nodes were updated with active version or discovery status.

- If any nodes in the destination cluster were updated with the new version of application or discovery status, create a new
                                             migration destination cluster by giving it a new name with the same source cluster and select the same destination VMIf any
                                             nodes in the destination cluster have been updated with the new version of application or discovery status, create a new migration
                                             destination cluster by giving it a new name with the same source cluster and select the same destination VMs.

- If any nodes in the destination cluster were not updated with the new version of application or discovery status,you may be
                                             able to reuse the migration destination cluster later when creating a new migration task. If this is not possible, recreate
                                             a migration destination cluster with a new name.

Step 5

Create a new migration task with the same source cluster and new  destination cluster.

Step 6

Start running the new task.

## Version
                        	 Validity

Install or
                              		  migrate Cisco Prime Collaboration Deployment if the version validity is True for the Restricted or Unrestricted version of
                              		  Cisco Prime Collaboration Deployment.

From

To

Version
                                          					 Validity

True

False

True

False

## ISO File Does Not
                        	 Get Loaded Or Not Recognized During Migration

On Cisco Unified Communications Manager virtual machine, verify
                                       				the correct ESXi BIOS boot order of the Cisco Unified Communications Manager
                                       				virtual machine. For example, CDROM, removeable devices, hard disk drive (HDD),
                                       				and network boot from VMXNET3.

Verify the ESXi host of Cisco Unified Communications Manager
                                       				virtual machine by using ESXi Foundation or Standard or higher.

Hypervisor edition does not enable ESXi APIs that Cisco Prime
                                                   				  Collaboration Deployment requires.

Verify that Cisco Prime Collaboration Deployment has root access
                                       				to ESXi host.

Verify that the NFS mount is stable.

If ISO file does not mount to virtual machine from NFS, check ESXihost > config > storage (datastore) > storage (datastore) .

If the datastore is inactive, you need to reconnect it.

To force reconnection of NFS mount, through Cisco Prime
                                             					 Collaboration Deployment, remove the ESXi host and add it again. Then, rerun
                                             					 the migrate task.

| Step 1 | Shut down the Cisco Prime Collaboration Deployment server by logging in to the Cisco Prime Collaboration Deployment CLI and
                                       entering the utils system shutdown command. |
|---|---|
| Step 2 | After the Cisco Prime Collaboration Deployment server shuts down, go to ESXi host and increase the disk size for the virtual machine on which the Cisco Prime Collaboration Deployment server resides. |
| Step 3 | Restart the Cisco Prime Collaboration Deployment server. |
| Step 4 | To view how much disk space is available on the Cisco Prime Collaboration Deployment server, run the CLI command show status on the Cisco Prime Collaboration Deployment server. |

| If | Then |
|---|---|
| The
                                             					 failure occurs during installation on the first node | You
                                                   						  must create a new fresh-install task with the same cluster nodes. Note In
                                                               							 the case of Unified Communications products such as Cisco Unified
                                                                  								Communications Manager and IM and Presence Service , Cisco Prime Collaboration
                                                               							 Deployment does not support an install task that installs a subsequent node
                                                               							 separately from the cluster. Check
                                                   						  the status of the VM on the ESXi host that is associated with the destination
                                                   						  cluster. If any VMs were powered on and installed, delete those VMs and
                                                   						  redeploy the OVA. Note For
                                                            						  more information, see topics relating to install tasks. | Note | In
                                                               							 the case of Unified Communications products such as Cisco Unified
                                                                  								Communications Manager and IM and Presence Service , Cisco Prime Collaboration
                                                               							 Deployment does not support an install task that installs a subsequent node
                                                               							 separately from the cluster. | Note | For
                                                            						  more information, see topics relating to install tasks. |
| Note | In
                                                               							 the case of Unified Communications products such as Cisco Unified
                                                                  								Communications Manager and IM and Presence Service , Cisco Prime Collaboration
                                                               							 Deployment does not support an install task that installs a subsequent node
                                                               							 separately from the cluster. |
| Note | For
                                                            						  more information, see topics relating to install tasks. |
| The installation is successful on the first node but fails on
                                             					 any of the subsequent nodes after Prime Collaboration Deployment loses
                                             					 connectivity | Log in to the failed Unified Communications VM node, such
                                                   						  as Cisco Unified Communications Manager, and manually verify the installation
                                                   						  status. For more information, see Unified Communications product documentation. Create a new install task with all new cluster nodes. You must restart the installation process by deleting all installed
                                                   VMs,
                                                   						  redeploying the recommended OVA to create new VMs, and creating a new install
                                                   						  task. Note If VM names are changed from previous configuration,
                                                               							 you must add a new fresh install cluster, create a new fresh install task, and then
                                                               							 run the task. Check the status of the VM on the ESXi host that is
                                                   						  associated with the destination cluster. If any VMs were powered on and
                                                   						  installed, delete those VMs and redeploy the OVA. Note For more information, see topics relating to install
                                                               							 tasks. | Note | If VM names are changed from previous configuration,
                                                               							 you must add a new fresh install cluster, create a new fresh install task, and then
                                                               							 run the task. | Note | For more information, see topics relating to install
                                                               							 tasks. |
| Note | If VM names are changed from previous configuration,
                                                               							 you must add a new fresh install cluster, create a new fresh install task, and then
                                                               							 run the task. |
| Note | For more information, see topics relating to install
                                                               							 tasks. |

| Note | In
                                                               							 the case of Unified Communications products such as Cisco Unified
                                                                  								Communications Manager and IM and Presence Service , Cisco Prime Collaboration
                                                               							 Deployment does not support an install task that installs a subsequent node
                                                               							 separately from the cluster. |
|---|---|

| Note | For
                                                            						  more information, see topics relating to install tasks. |
|---|---|

| Note | If VM names are changed from previous configuration,
                                                               							 you must add a new fresh install cluster, create a new fresh install task, and then
                                                               							 run the task. |
|---|---|

| Note | For more information, see topics relating to install
                                                               							 tasks. |
|---|---|

| If | Then |
|---|---|
| The failure occurs during upgrade on the first node | Check task status on the Monitoring page to see which steps were successful
                                                   						  and which steps failed. Log in to the first Unified Communications VM node, such
                                                   						  as Cisco Unified
                                                      							 Communications Manager . Check the software version and upgrade status
                                                   						  to verify whether this node was upgraded to a new version. For more information, see
                                                   						  Unified Communications product documentation. If the upgrade on the first node is successful, you can
                                                   						  create a new upgrade task with the subsequent node. If the upgrade on the first node is unsuccessful, you can
                                                   						  create a new upgrade task with all nodes. If the upgrade task was configured with automatic switch
                                                   						  version, check the status of the active and inactive partitions on the Unified
                                                   						  Communications product node. If the automatic switch version was unsuccessful on the
                                                   						  Unified Communications product node, perform a switch version. For more information, see
                                                   						  Unified Communications product documentation. Note If
                                                            						  the switch version is required, this must be done before you a new
                                                            						  upgrade task with subsequent nodes with a new upgrade task that is configure with
                                                            						  auto-switch version. Note If you create an upgrade task to install a COP file, verify COP-file installation status
                                                      					 directly on the Unified Communications node. | Note | If
                                                            						  the switch version is required, this must be done before you a new
                                                            						  upgrade task with subsequent nodes with a new upgrade task that is configure with
                                                            						  auto-switch version. | Note | If you create an upgrade task to install a COP file, verify COP-file installation status
                                                      					 directly on the Unified Communications node. |
| Note | If
                                                            						  the switch version is required, this must be done before you a new
                                                            						  upgrade task with subsequent nodes with a new upgrade task that is configure with
                                                            						  auto-switch version. |
| Note | If you create an upgrade task to install a COP file, verify COP-file installation status
                                                      					 directly on the Unified Communications node. |
| The upgrade is successful on the first node but fails on any
                                             					 of the subsequent nodes after Prime Collaboration Deployment loses connectivity | Log
                                                   						  in to the failed Unified Communications VM node, such as Cisco Unified
                                                      							 Communications Manager . Check the software version and upgrade status
                                                   						  to verify whether this node was upgraded to a new version. For more information, see
                                                   						  Unified Communications product documentation. Note If
                                                            						  the subsequent node shows the correct new version, you do not need to recreate
                                                            						  an upgrade task on Prime Collaboration Deployment. If
                                                   						  the subsequent node shows the new version in the inactive partition, the old
                                                   						  version in active partition, and the upgrade task was configured to switch version automatically, you must either
                                                   perform the automatic switch version manually
                                                   						  on the Cisco Unified Communications Manager node or use Prime Collaboration
                                                   						  Deployment to create a switch version task. If the upgrade task was configured with automatic switch version
                                                   						  and the subsequent node does not show the version correctly, perform a switch
                                                   						  version. See Unified Communications product documentation more detail. Note If you created an upgrade task to install a COP file, verify COP-file installation status
                                                      					 directly on the Unified Communications node. | Note | If
                                                            						  the subsequent node shows the correct new version, you do not need to recreate
                                                            						  an upgrade task on Prime Collaboration Deployment. | Note | If you created an upgrade task to install a COP file, verify COP-file installation status
                                                      					 directly on the Unified Communications node. |
| Note | If
                                                            						  the subsequent node shows the correct new version, you do not need to recreate
                                                            						  an upgrade task on Prime Collaboration Deployment. |
| Note | If you created an upgrade task to install a COP file, verify COP-file installation status
                                                      					 directly on the Unified Communications node. |

| Note | If
                                                            						  the switch version is required, this must be done before you a new
                                                            						  upgrade task with subsequent nodes with a new upgrade task that is configure with
                                                            						  auto-switch version. |
|---|---|

| Note | If you create an upgrade task to install a COP file, verify COP-file installation status
                                                      					 directly on the Unified Communications node. |
|---|---|

| Note | If
                                                            						  the subsequent node shows the correct new version, you do not need to recreate
                                                            						  an upgrade task on Prime Collaboration Deployment. |
|---|---|

| Note | If you created an upgrade task to install a COP file, verify COP-file installation status
                                                      					 directly on the Unified Communications node. |
|---|---|

| Note | Repeat
                                                   				  this step for all source nodes that were shut down. |
|---|---|

| Note | You do not need to delete the source cluster. |
|---|---|

| Note | For more
                                                   				  information, see topics relating to migration tasks. |
|---|---|

| If | Then |
|---|---|
| The
                                             					 failure occurs during switch version on the first node | Log in
                                                   						  to the first Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and manually check the sofware version in both the
                                                   						  active and inactive partitions. For more information, see Unified Communications product
                                                   						  documentation. If
                                                   						  the first node still shows the old version in the active partition but the new
                                                   						  version in the inactive partition, create a new switch version task with the
                                                   						  same nodes on Prime Collaboration and run the task again. |
| The switch
                                             					 version is successful on the first node but fails on any of the subsequent
                                             					 nodes after Prime Collaboration Deployment loses connectivity | Log in
                                                   						  to the subsequent Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager). Check the software and switch version status to
                                                   						  verify that the subsequent node is up and running with the correct version. If
                                                   						  the subsequent node shows the correct new version in the active partition, you
                                                   						  do not need to recreate a switch version task on Prime Collaboration
                                                   						  Deployment. If
                                                   						  the subsequent node shows the new version in the inactive partition and the old
                                                   						  version in active partition, the switch version was not successful on the
                                                   						  subsequent node. You can either perform a switch version manually on the
                                                   						  subsequent node or create a new switch version task on the subsequent node
                                                   						  on Prime Collaboration Deployment. |

| If | Then |
|---|---|
| The
                                             					 failure occurs during readdress on the first node | Log in
                                                   						  to the first Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and verify that network settings were successfully
                                                   						  changed. For more information, see Unified Communications product documentation. After
                                                   						  you verify that network settings were successfully changed on the first node,
                                                   						  create a new readdress task on the subsequent node on Prime Collaboration
                                                   						  Deployment and run this task. If network settings were not successfully changed
                                                   						  on the first node, create a new readdress task with both nodes on Prime
                                                   						  Collaboration Deployment and run the task again. |
| The
                                             					 readdress task is successful on the first node but fails on any of the
                                             					 subsequent nodes after Prime Collaboration Deployment loses connectivity | Log in
                                                   						  to the first Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and verify that network settings were successfully
                                                   						  changed. For more information, see Unified Communications product documentation.. After
                                                   						  verifying that network settings were successfully changed on the first node,
                                                   						  you do 
                                                   						  not need to create a new readdress task on the first node on
                                                   						  Prime Collaboration Deployment. However, you do need to create a new readdress task on
                                                   						  the subsequent nodes. If network settings were not successfully changed on the
                                                   						  first node, create a new readdress task with the first node and subsequent
                                                   						  nodes on Prime Collaboration Deployment and run the new task. If
                                                   						  network settings were successfully changed, update cluster discovery for this
                                                   						  cluster to make sure that Prime Collaboration Deployment has the correct
                                                   						  network settings. Go
                                                            								to the Clusters screen and click the triangle to show the
                                                            								nodes in the cluster. Check the network settings to ensure that the Cluster Nodes
                                                            								table shows the new network settings (for example, hostname). If
                                                            								the correct network settings are not displayed, click the Refresh Node link for each node in the cluster. |

| If | Then |
|---|---|
| The
                                             					 failure occurs during server restart on the first node | Log in
                                                   						  to the first Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and manually check the status of the restart. If
                                                   						  the first node did not get restarted, recreate a new server restart task with
                                                   						  all nodes and run the task again. |
| The server
                                             					 restart is successful on the first node but fails on any of the subsequent
                                             					 nodes after Prime Collaboration Deployment loses connectivity | Log
                                                   						  in to the second Unified Communications VM node (for example, Cisco Unified
                                                   						  Communications Manager) and manually check the status of restart. If
                                                   						  the subsequent node restarted successfully, there is no need to recreate a new
                                                   						  server restart task. If the subsequent node did not restart, create a new
                                                   						  server restart task on the subsequent node only. |

| Step 1 | View the task log to verify the status of the most recent task. If the VM is powered on and the fresh install task is still in progress, power off the VM, delete it, and redeploy the OVA
                                                to create a new VM. You can use the same name for the new VM. If the VM is powered off and the fresh install was not started on the VM, leave the VM powered off. |
|---|---|
| Step 2 | Check the cluster to verify if any nodes in the cluster were updated with the active version and discovery status. If any nodes were updated with the new version or discovery status, create a new cluster with a  new  name, including the
                                             same VMs and installation settings. If any nodes in the cluster were not updated, reuse the cluster when recreating a fresh install task. |
| Step 3 | Create and run a new install task. |

| Step 1 | View the task log to verify the status of the most recent task. If the VM is powered on and the migration task is still in progress on the destination VM, power off the destination VM, delete
                                                it, and redeploy the OVA to create a new destination VM. You can use the same name for the new VM. If the VM is powered off and the migration was not started on the VM, leave the VM powered off. |
|---|---|
| Step 2 | Check the node status on the source cluster before running a new task. If the source node is powered off, power on the source node and make sure it is in a running state before rerunning a migration
                                             task. In the case of network migration, the source node can remain powered on. |
| Step 3 | You do not need to rerun cluster discovery on the source node. |
| Step 4 | Check the destination cluster to ensure that no nodes were updated with active version or discovery status. If any nodes in the destination cluster were updated with the new version of application or discovery status, create a new
                                             migration destination cluster by giving it a new name with the same source cluster and select the same destination VMIf any
                                             nodes in the destination cluster have been updated with the new version of application or discovery status, create a new migration
                                             destination cluster by giving it a new name with the same source cluster and select the same destination VMs. If any nodes in the destination cluster were not updated with the new version of application or discovery status,you may be
                                             able to reuse the migration destination cluster later when creating a new migration task. If this is not possible, recreate
                                             a migration destination cluster with a new name. |
| Step 5 | Create a new migration task with the same source cluster and new  destination cluster. |
| Step 6 | Start running the new task. |

| From | To | Version
                                          					 Validity |
|---|---|---|
| Export
                                       				  Restricted (K9) | Export Restricted (K9) | True |
| Export
                                       				  Restricted (K9) | Export
                                       				  Unrestricted (XU) | False |
| Export
                                       				  Unrestricted (XU) | Export
                                       				  Restricted (K9) | True |
| Export
                                       				  Unrestricted (XU) | Export
                                       				  Unrestricted (XU) | False |

| Note | Hypervisor edition does not enable ESXi APIs that Cisco Prime
                                                   				  Collaboration Deployment requires. |
|---|---|

| Note | If the datastore is inactive, you need to reconnect it. |
|---|---|