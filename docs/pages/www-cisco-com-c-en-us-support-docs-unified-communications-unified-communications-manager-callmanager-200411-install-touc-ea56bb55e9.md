---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200411-install-touc-ea56bb55e9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200411-Install-Touchless-VM-for-CUCM.html
retrieved_at: 2026-08-21T13:54:43.860475+00:00
---

Install Touchless VM for CUCM

# Install Touchless VM for CUCM

### Download Options

Updated: February 10, 2016

Document ID: 200411

Contents

## Contents

## Introduction

This document describes Touchless Virtual Machine (VM) installation feature which is being introduced in Cisco Unified Communications Manager (CUCM) 10.5.2 and higher releases.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- Bootable Image for CUCM/Cisco Unity Connection (CUC)/ Instant Messaging & Presence (IM&P) for version 10.5.2 and higher

- Open Virtualization Archive (OVA) for UC 10.5.2.

- Virtual Floppy Image created with the output of Answer File Generator (AFG) tool.

Procedure to create virtual floppy image with the AFG tool is documented in the following link .This website provides instructions for multiple client platforms such as Windows, Mac OS X and Linux.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Use AFG tool to generate a floppy image file. This floppy image contains platformConfig.xml file and clusterConfig.xml file for CUCM publisher and only platformConfig.xml file for all other nodes which include CUCM Subscribers, IMP Publisher & IMP Subscriber.

Installation starts by booting up the VM nodes with floppy image and bootable ISO being mounted. Using the Touchless VM Install procedure, no manual intervention is required during installation of a standalone node or during cluster installation.

With this feature, the entire cluster installation can be started at the same time. Subscriber will have to wait for the publisher to come online in case Publisher installation is still in progress. On completion of the publisher installation, the waiting subscribers will be added to its server table. Once the subscribers are added to publisher, subscribers can proceed with their install.

A collective co-ordination of cluster manager (clm) and upstart service makes this exchange of information between publisher and subscriber possible. This simplified cluster installation can be achieved by predefined cluster configuration generated using AFG tool. In this, publisher has the complete information about its subscriber nodes from clusterConfig.xml file. Publisher uses this information to add these nodes to its processnode/application table after publisher is successfully installed.

Before proceeding, make note that there is a new feature that has been added. It is Dynamic Cluster Configuration.

- New Subscriber nodes get added to Publisher’s server table automatically when they come online and try to authenticate with Publisher. For this to happen, dynamic-cluster-configuration must be enabled first.

- This can be enabled either via AFG tool or via Command Line Interface (CLI).

- With this framework, you need not have to manually add Subscriber's details in Publisher's server page.

As a part of this feature, you must be able to generate platformConfig.xml file and clusterConfig.xml file from AFG tool. Also, you must be able to specifythe Dynamic Cluster Configuration timer value to be used and provide a prebuilt clusterConfig.xml file. If dynamic-cluster-configuration is used, you must be able to add details of timeout value for dynamic-cluster-configuration.

You can find the Dynamic Cluster Configuration timer value in the platformconfig.xml file of the publisher:

```
<PostInstallAutoRegister>
  <ParamNameText>
    Number of Seconds to Enable Auto Register Post-Install on Pub
  </ParamNameText>
  <ParamDefaultValue>0</ParamDefaultValue>
```

```
<ParamValue>1000</ParamValue>
```

```
</PostInstallAutoRegister>
```

As soon as the file is created, an upstart event is sent stating that the file is created. On receiving the event, the upstart service that is listening to the upstart event configures cluster manager with this timer.

For example, if the timer is configured to 10 hours, CUCM Subsriber nodes get added to the process node for the CUCM publisher until the time is up from the moment publisher is online. Subscriber nodes can be added at a later date by using the set network cluster subscriber dynamic-cluster-configuration <number of hours> command:

where

<number of hours> - is a value between 1 to 24

default - will set dynamic-cluster-configuration vaule to 24 hours

When enabled, the show network cluster command gives the following output:

```
admin:show network cluster
```

```
10.106.61.120 CUCMPUB  Publisher callmanager DBPub authenticated 10.106.61.121 CUCMSUB  Subscriber callmanager DBSub authenticated using TCP since Fri Nov 28 17:59:21 2014 10.106.61.122 CUCMSUB1  Subscriber callmanager DBSub authenticated using TCP since Fri Nov 28 18:06:41 2014 Server Table (processnode) Entries ---------------------------------- CUCMPUB 10.106.61.121 10.106.61.122 Dynamic Cluster Configuration is enabled for 23 Hours 59 Minutes.
```

Note : On using clusterconfig.xml file along with platformconfig.xml file, nodes autoregister to the CUCM Pub, and therefore the timer disucssed above stands irrelevant. The timer is useful only where you are using platformconfig.xml file of the Publisher server, just like the CUCM Pub is unaware of all other nodes in the cluster in this case.

In this scenario, you are going to build 3 node clusters (Publisher CUCMPUB and 2 subscribers CUCMSUB and CUCMSUB1) using both methods.

Out of 2 CUCM Subscribers, install CUCMSUB via clusterconfig.xml file, and the CUCMSUB1 using Auto-Registration Process.

3 files are created:

- Platformconfig.xml file for the primary node CUCMPUB

- Platformconfig.xml file for the secondary node CUCMSUB

- Clusterconfig.xml file have the details for the entire cluster. Similar to platformconfig.xml , it contains the list of hostnames, ip address,domain, role and usage information for all the devices in the cluster.

In this scenario, as you are using CUCMSUB1 to be installed via Auto-registration , you generate another AFG file which is similar to the one above, and has the platformconfig.xml file for the publisher along with the new platformconfig.xml for the CUCMSUB1.

As shown in this image.

Once we have the clusterconfig.xml file from the publisher, and platformconfig.xml file from all the servers, it is time to make a floppy image of the same.

### For the Publisher

If you like to use dynamic cluster config option, you require to create a floppy image by combining both the clusterconfig.xml file and platformconfig.xml file of the Publisher. Combining both files is only required for the publisher, and not for any other server. For Subscribers, you can use only the respective platformconfig.xml files.

### VM Deployment

Once you have the floppy image created, it is time to mount the CD (with the .iso bootable image) as well as the floppy drive (with the .flp image which you created earlier).

This image shows how to mount CD:

This image shows how to mount floppy drive:

You need to ensure that the VM machine is configured to boot from CD-ROM. If not, you can modify the BIOS setting to allow the same. Please power on the VMs. From this stage on, no manual intervention is required, and all the servers must be installed. In this scenario, as you have disabled dynamic auto configuration, you must manually configure the timer, which is shown later.

Once the VMs have been powered on, it begins its pre-boot stage process wherein it asks you to test the media or continue.

This image shows the media test window:

CUCM servers looks for the clusterconfig.xml file and platformconfig.xm l file during this pre-boot phase.

## Verify

Use this section in order to confirm that your configuration works properly.

From the install logs of CUCMPUB, you can see if it has been able to find the files or not. In our example,

platformconfig.xm l file

```
11/28/2014 08:05:28 anaconda|Looking for platformConfig.xml...|<LVL::Info> 11/28/2014 08:05:28 anaconda|Find a platformConfig.xml file|<LVL::Info> 11/28/2014 08:05:28 anaconda|Check on /dev/fd0|<LVL::Debug> 11/28/2014 08:05:28 anaconda|Looking for platformConfig.xml on device /dev/fd0|<LVL::Info> 11/28/2014 08:05:28 anaconda
```

```
|Found platformConfig.xml on device /dev/fd0|<LVL::Info>
```

clusterconfig.xml file

```
11/28/2014 08:05:28 anaconda|Copying /mnt/floppy/platformConfig.xml to /tmp/platformConfig.xml|<LVL::Debug> 11/28/2014 08:05:28 anaconda|Looking for clusterConfig.xml...|<LVL::Info> 11/28/2014 08:05:28 anaconda|Find a clusterConfig.xml file|<LVL::Info> 11/28/2014 08:05:28 anaconda|Check on /dev/fd0|<LVL::Debug> 11/28/2014 08:05:28 anaconda|Looking for clusterConfig.xml on device /dev/fd0|<LVL::Info> 11/28/2014 08:05:28 anaconda|
```

```
Found clusterConfig.xml on device /dev/fd0|<LVL::Info>
```

```
11/28/2014 08:05:28 anaconda|Copying /mnt/floppy/clusterConfig.xml to /tmp/clusterConfig.xml|<LVL::Debug>
```

You see the similar message in the logs for the other 2 subscribers.

Once Pre-boot phase is over, 2 of the servers start with the Post-Boot Phase.

This image shows the Post-Boot Phase:

As CUCM Publisher is not installed, installation of subscriber halts at this point of time, as it is unable to find its entry in the process node table of the publisher. The warning has been modified accrodingly, mentioning that for touchless installs, this is normal, while the publisher installs.take no action. Install will resume automatically as shown is this image.

Once the CUCM Publisher is installed, an upstart event is sent to notify that install is completed. Processnode file gets created, and it looks for the clusterconfig.xml file on the Publisher, to see what nodes are present in clusterconfig.xml file at that time. In this case it finds one more node, and it adds that node in the database. Remember for the server CUCMSUB1, you use for auto-registration process, and its details are not present in the clusterconfig.xml file of the publisher.

An event in the install logs is shown.

```
Nov 28 16:44:37 CUCMPUB local7 6 Cisco: Database Layer Monitor: DBNotify SDI Initialization successful Nov 28 16:44:37 CUCMPUB user 6 ilog_impl: emitted platform-event (--no-wait
```

```
platform-system-processnode-created
```

```
)
```

Once the CUCM Publisher adds the nodes to its database, there is a new section in clusterconfig.xml file which is called icl_state , and it marks the state as completed. This is required as the CUCM Publisher needs to look the clusterconfig.xml file few times during the overall installation. If the state has been marked as completed, it knows which node has completed the installation.

In the meanwhile, cluster manager of CUCMSUB, though not completely online still tries to poll the CUCM Publisher. As the Publisher is still not installed, you receive an error as shown in the ClusterManager logs:

```
09:48:53.054 |tcp connection closed to
```

```
10.106.61.120
```

```
, back to initiator state 09:48:53.054 |exec'ing: sudo /root/.security/ipsec/disable_ipsec.sh --desthostName=CUCMPUB --op=delete 09:48:53.509 |Timeout or error() 115 - Operation now in progress, port 8500 09:48:53.509 |
```

```
tcp recv error: Connection refused.
```

```
09:49:15.773 |tcp connection closed to
```

```
10.106.61.120
```

```
, back to initiator state 09:49:15.773 |exec'ing: sudo /root/.security/ipsec/disable_ipsec.sh --desthostName=CUCMPUB --op=delete 09:49:16.223 |Timeout or error() 115 - Operation now in progress, port 8500 09:49:16.223 |
```

```
tcp recv error: Connection refused
```

```
.
```

Now once the publisher installation is completed and the processnode file gets created, it visits its clusterconfig.xml file and adds the other node (CUCMSUB). As soon as the node gets added to the database, and upstart event is sent to the CUCMPUB and CUCMSUB. Cluster manager of CUCMSUB receives the policy injected state from CUCMPUB. An upstart event is sent with hostname of CUCMPUB and the policy injected state. CUCMSUB in an attempt to create a mesh topology with other servers receives the upstart event from all the other servers, however, it's more interested in the upstart event which it receives with the hostname of  the CUCMPUB as it resumes the installation when the publisher is online. Once the upstart service receives the upstart event, it sends a kill signal to the install wizard. This attempts to revalidate the platformconfig.xml file, and in turn it begins the connectivity validation with the CUCMPUB. As the publisher is now available, validation succeeds and installation continues.

For CUCMSUB1 installation,you require to modify the dynamic cluster configuration value to any other value, so, that our server gets added to the processnode of the publisher. In this example, you have modified the same to 1 hour.

set network cluster subscriber dynamic-cluster-configuration 1 command.

Once the above command is applied, CUCMPUB accpets the node register request from CUCMSUB1. If the above command is not configured, when CUCMSUB1 tries to contact the publisher, the publisher looks in its auto-reg timer, if the value is 0, it does not add the node in its clusterconfig.xml as well as processnode table.

Once the CUCMSUB1 contacts CUCMPUB, it accepts socket connection from CUCMSUB1(10.106.61.122), and it adds the subscriber data to the clusterconfig.xml file.

From the clusterManager logs of the Publisher, this event is printed as saveClusterSubscriberNodeData.

```
16:56:19.455 |
```

```
accepted client IP(10.106.61.122), socket(10):
```

```
16:56:24.489 |
```

```
saveClusterSubscriberNodeData api, hostname=CUCMSUB1
```

```
, peerdat=icl_master=no icl_clustered=yes icl_deployment=callmanager icl_active_version=10.5.2.10000-2 icl_inactive_version=0.0.0.0000-0000 icl_active_unrest=false icl_inactive_unrest=false icl_disk_size=110 icl_mtu_changed=no icl_mtu_size= icl_app_uid=administrator icl_app_pw= icl_db_master=no icl_state=Installing icl_ip_address=10.106.61.122 icl_fqdn=CUCMSUB1 icl_domain= icl_pub_enc_dkey=
```

As a result of which the clusterconfig.xml file on the publisher changes, and this event is seen.

```
CUCMPUB user 6 ilog_impl: Received request for platform-event (platform-event-clusterconfig-changed)
```

Installation of the server continues there on.

Once the CUCMSUB and CUCMSUB1 are installed, you receive the following event platform-system-clusternode-install-completed from both nodes. This event is sent out to every node in the cluster.

STATE=ready indicates that the installation is completed, else it is in Installing state. This message is seen in the CUCMPUB syslog, that signifies the installation of CUCMSUB and CUCMSUB1 are completed.

```
Line 13154: Nov 28 17:59:17 CUCMPUB user 6 ilog_impl: emitted platform-event(--
```

```
no-wait platform-system-clusternode-install-completed HOSTNAME=CUCMSUB STATE=ready
```

```
)
Line 14514: Nov 28 18:06:36 CUCMPUB user 6 ilog_impl: emitted platform-event(--
```

```
no-wait platform-system-clusternode-install-completed
```

```
HOSTNAME=CUCMSUB1 STATE=ready
```

```
)
```

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## CLI commands that have been introduced in this feature

1. set network cluster subscriber details <server type> <hostname> <ip> <domain name>

This command is to add subscriber to processnode/app server table.

Syntax:

Parameters

Description

Server Type

Values are CUCM or IMP or CUC ( Mandatory )

ip

Ipaddress of the hostname added ( mandatory for IMP Publisher & CUC & optional for other nodes

Domain name

Domain name of the IMP publisher ( Mandatory for IMP Publisher & not required for other nodes )

2. unset network cluster subscriber details

This command displays the message mentioning that subscriber can be deleted from GUI. Unset operation is not allowed on the CLI. This operation can only be done from the webpage.

3. set network cluster subscriber dynamic-cluster-config

Set network cluster subscriber dynamic-cluster-configuration { <default> | < number of hours >

This command enables dynamic-cluster-config on publisher.

Syntax Description

Parameters

Description

default

This will enable dynamic-cluster-config for 24hrs

<no. of hours>

Value between 1-24 hours

4. show network cluster

This command displays up-to-date dynamic-cluster-configuration value on publisher when it is enabled.

## Benefits

- To provide a touch less installation process, in which no manual intervention is required during installation and scheduling during the deployment of a new CUCM cluster.

- To simplify the addition of new subscribers to an existing cluster.

- Save time

During a typical CUCM installation,you see multiple Install Wizard screens and manual intervention are required for these scenarios:

- As part of the installation,you provide certain information on the Install Wizard screens. This requires manual intervention as you manually type the information that installation process seeks.

- To setup a typical cluster environment, first a Publisher is installed. After a Publisher is installed, you add details of the subscribers in the publisher’s server tables from the web page of publisher. Then, when a subscriber is being installed, an Install Wizard for Subscriber runs requesting the administartor to fill the subscriber install details.

### Contributed by Cisco Engineers

Somnath Gupta

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Parameters | Description |
|---|---|
| Server Type | Values are CUCM or IMP or CUC ( Mandatory ) |
| ip | Ipaddress of the hostname added ( mandatory for IMP Publisher & CUC & optional for other nodes |
| Domain name | Domain name of the IMP publisher ( Mandatory for IMP Publisher & not required for other nodes ) |

| Parameters | Description |
|---|---|
| default | This will enable dynamic-cluster-config for 24hrs |
| <no. of hours> | Value between 1-24 hours |