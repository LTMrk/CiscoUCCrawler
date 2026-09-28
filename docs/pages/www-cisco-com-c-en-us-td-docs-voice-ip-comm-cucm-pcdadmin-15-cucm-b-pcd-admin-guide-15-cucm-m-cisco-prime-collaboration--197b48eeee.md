---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-15-cucm-b-pcd-admin-guide-15-cucm-m-cisco-prime-collaboration--197b48eeee
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/15/cucm_b_pcd-admin-guide-15/cucm_m_cisco-prime-collaboration-deployment-features.html
retrieved_at: 2026-08-17T00:33:03.412967+00:00
---

Prime Collaboration Deployment Administration Guide, Release 15 and SUs

# Prime Collaboration Deployment Administration Guide, Release 15 and SUs

Updated: February 5, 2026

Chapter: Cisco Prime Collaboration Deployment Features

## Chapter: Cisco Prime Collaboration Deployment Features

# Cisco Prime Collaboration Deployment Features

## Cisco Prime Collaboration Deployment Considerations

Cisco Prime Collaboration Deployment allows a user to perform tasks (such as migration or upgrade) on servers that are in
                              the inventory.

Step

Tasks

Step 1: Inventory Creation

To perform any tasks, you must first have clusters in your inventory. To add a UC cluster that is already running UC applications
                                          to your inventory, click Open and close navigation and choose Inventory > Clusters > Discovery Cluster feature.

To migrate an existing cluster to new virtual machines, click Open and close navigation and choose Inventory > Clusters > Define Migration Destination Cluster . (See Migration Task .)

To install a new cluster, click Open and close navigation and choose Inventory > Clusters > Define New UC Cluster feature. (See Create an Install Task .)

If you are migrating an existing cluster to a new virtual machine cluster, or installing a new cluster, you must first add
                                          the ESXi Hosts that contain those virtual machines to your inventory. To add an ESXi host, click Open and close navigation and choose Inventory > ESXi Hosts . (See Add an ESXi Host Server .)

Step 2: Create a Task

You can create a task to perform an operation on a cluster in your inventory. During task creation, options allow you to:

Choose the cluster

This task depends on the type of cluster you require. For example, you may choose a discovered cluster or a migration cluster.

Determine when to run the task

Determine if the task should run independently or pause between steps

To perform one of the following actions, select from these procedures:

To migrate from an existing cluster to a new cluster of VM machines, see Migration Task .

To upgrade the Unified Communications Manager version of an existing cluster, see Upgrade Task .

To switch the version of an existing cluster, see Switch Versions Task .

To restart an existing cluster, see Server Restart Task .

To change the hostname or IP address of one or more servers in an existing cluster, see Readdress Task .

To create a new UC cluster from VM machines, see Create an Install Task .

Step 3: Monitor Tasks

After a task is created, you can use the Monitoring window to view or track any task. You can also use this page to cancel,
                                          pause, or resume tasks.

To view the tasks you created, see Monitor Task Status .

Step 4: Administrative Tasks

You can set up email notification. See Email Notification .

## Network Address
                        	 Translation Support

Cisco Prime Collaboration Deployment supports Network Access Translation (NAT). You can use Cisco Prime Collaboration Deployment
                              in the following scenarios:

When Cisco Prime Collaboration Deployment is in a local network, or private network and application nodes are behind the NAT.

When Cisco Prime Collaboration Deployment is behind the NAT, and application nodes are in a private network.

To support
                              		  application nodes behind the NAT, Cisco Prime Collaboration Deployment tracks
                              		  the private IP address and the NAT IP address. Use Cisco Prime Collaboration
                              		  Deployment to specify the NAT IP address for deployment nodes and the
                              		  application. Cisco Prime Collaboration Deployment uses the NAT IP address to
                              		  communicate with the application node. However, when you configure a node using
                              		  the platformConfig.xml file, the node uses its private
                              		  address.

## Configure Cisco
                        	 Prime Collaboration Deployment Behind the NAT

When Cisco Prime
                              		  Collaboration Deployment is behind the NAT and communicates with an application
                              		  virtual machine or an ESXi host, the communication occurs using the NAT IP
                              		  address.

When Cisco Prime
                                          			 Collaboration Deployment is behind the NAT and application nodes are in a
                                          			 private network, the application nodes communicate with the NAT IP address.

Use the NAT
                                 			 Settings window in the Administration menu to set the NAT IP address for
                              		  Cisco Prime Collaboration Deployment. The NAT IP address that you enter on this
                              		  window does not appear on any window on the GUI.

Step 1

From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Administration > NAT Settings .

Step 2

Enter the NAT
                                       			 IP address in the NAT
                                          				IP field.

Step 3

Click Save .

Step 4

(Optional) Click Reset .

## Supported Tasks for Applications and Versions

You can use Cisco Prime Collaboration Deployment to perform various tasks for Unified Communications applications. The following
                              tables list the tasks that Cisco Prime Collaboration Deployment supports for each application.

Unified Communications Manager destination version is in Release 15.

Unified Communications Manager destination version is in Release 15 and you are trying to upgrade your IM and Presence Service
                                                source from a restricted version to an unrestricted version.

Unified Communications Manager destination version is in Release 15 and the IM and Presence Service source nodes are in 14
                                                or 14SU1 versions.

Unified Communications Manager destination version is in Release 15 and you are trying to upgrade your IM and Presence Service
                                                source from a restricted version to an unrestricted version.

If your Cisco Prime Collaboration Deployment is Release 15SU2 and it is using TLS 1.3 and that PCD is discovering, upgrading,
                                          migrating, installing, also performing server restart, readdress, and switch version of UC clusters of pre-15SU2, then ensure
                                          that your Cisco Prime Collaboration Deployment is configured with a minimum TLS version other than the TLS 1.3 protocol before
                                          proceeding with any of these tasks.

The releases listed in the tables do not specify the Engineering Special (ES)/ Service Update (SU) versions. To identify supported
                                          ES/SU versions that you can upgrade or migrate to through Cisco Prime Collaboration Deployment, see the release notes of the
                                          corresponding product, such as IM and Presence, Cisco Unified Communications Manager, and Unity Connection.

Cisco Prime Collaboration Deployment supports the destination version 12.5 and above for an upgrade, and destination version
                                          10.5 and above for migrations. The application versions 10.x and above support virtualization. If the source version is 12.5
                                          and above, the upgrade task is supported. However, if the source version is prior to 12.5, the upgrade task is not supported.

A migrate cluster task can migrate to any of releases listed in the tables, by having source version as 10.5 or above and
                                          the destination version should be 12.5 or higher on virtual machine.

If you're using Cisco Prime Collaboration Deployment to migrate Cisco Unified Communications Manager from Release 12.0(1)
                                          to any higher release, you must install the following COP file on the 12.0(1) system before you begin the migration. Otherwise,
                                          the configuration files related to Smart Licensing won't be migrated.

ciscocm-slm-migration.k3.cop.sgn

This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Cisco Unified Communications
                                          Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Cisco Unified Communications Manager
                                          12.0(1)SU1, you don't need to install the COP file.

Check destination application version release notes for any known caveats with using the Cisco Prime Collaboration Deployment
                                          tasks with the application. For Cisco Prime Collaboration Deployment, Fresh Install, Migrate and Upgrade tasks, check the
                                          destination application’s Installation Guide and Upgrade Guide for any application-specific rules or restrictions on using
                                          these Cisco Prime Collaboration Deployment tasks with the application (for example, required node sequencing for installs
                                          or upgrades, restrictions on how COPs may be installed, and so on.)

If you're using Cisco Prime Collaboration Deployment to discover a cluster of the products deployed with the releases that
                                          have an issue as mentioned in the below table, you must install the ciscocm.V11.5.1_CSCvv25961_add_diffie_C0085 COP file on
                                          the Unified Communications Manager system before you begin the discovery, otherwise, the discovery fails.

Product

Release with issue

Cop file for fix

Release with Fix

Cisco Unified Communications Manager

11.5.1.18900-97

Yes

11.5(1)Su9 and above

10.5.2.22900-11

N/A

ES

IM and Presence Service

11.5.1.18900-15

Yes

11.5(1)Su9 and above

Cisco Unity Connection

11.5.1.21137-1

Yes

11.5(1)Su9 and above

Cisco Emergency Responder

11.5.4.61000-12

Yes

11.5(1)Su9 and above

Task

Release

Cluster Discovery

10.5.x, 11.5, 12.x, 14 and SUs, and 15

Migrate Cluster (Install Application and Import Data from Old System)

From

10.5.x, 11.x, 12.x, 14 and SUs, and 15

To

12.5.x, 14 and SUs, and 15

Upgrade Cluster (Upgrade Application Version or Install COP Files)

From

11.5, 12.x, and 14 and SUs

To

12.5.x and 14 and SUs

Also

From

12.5.x and 14 and SUs

To

15

Restart

11.5, 12.x, 14 and SUs, and 15

Switch Version

11.5, 12.x, 14 and SUs, and 15

Fresh Install New Cluster or Edit or Expand an Existing Cluster

12.5.x, 14 and SUs, and 15

Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster)

12.5.x, 14 and SUs, and 15

Task

Release

Cluster Discovery

10.5.x, 11.x, 12.x, 14 and SUs, and 15

Migrate Cluster (Install Application and Import Data from Old System)

From

10.5.x, 11.x, 12.x, 14 and SUs, and 15

To

12.5.x, 14 and SUs, and 15

Upgrade Cluster (Upgrade Application Version or Install COP Files)

From

11.5, 12.x, and 14 and SUs

To

12.5.x and 14 and SUs

Also

From

12.5.x and 14 and SUs

To

15

Restart

11.5, 12.x, 14 and SUs, and 15

Switch Version

11.5, 12.x, 14 and SUs, and 15

Fresh Install New Cluster or Edit or Expand an Existing Cluster

12.5.x, 14 and SUs, and 15

Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster)

Not Supported

Task

Release

Cluster Discovery

11.5, 11.6, 12.x

Migrate Cluster (Install Application and Import Data from Old System)

Not Supported

Upgrade Cluster (Upgrade Application Version or Install COP Files)

Release Supported:

To

12.5(1)SU2 and above

Deployment of UCCX upgrade of a COP file for release 12.0.1, 11.x, and 10.x should be done one node at a time using PCD.

Restart

11.5, 11.6, 12.5(1)SU2 and above

Switch Version

11.5, 11.6, 12.5(1)SU2 and above

Fresh Install New Cluster or Edit or Expand an Existing Cluster

12.5(1)SU2 and above

Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster)

12.5(1)SU2 and above

Task

Release

Cluster Discovery

11.5, 12.x, 14 and SUs, and 15

Migrate Cluster (Install Application and Import Data from Old System)

Not Supported

Upgrade Cluster (Upgrade Application Version or Install COP Files)

From

11.5, 12.x, and 14 and SUs

To

12.5.x and 14 and SUs

Also

From

12.5.x and 14 and SUs

To

15

Restart

11.5, 12.x, 14 and SUs, and 15

Switch Version

11.5, 12.x, 14 and SUs, and 15

Fresh Install New Cluster or Edit or Expand an Existing Cluster

12.5.x, 14 and SUs, and 15

Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster)

12.5.x, 14 and SUs, and 15

Task

Release

Cluster Discovery

11.5(x), 12.x, 14 and SUs, and 15

Migrate Cluster (Install Application and Import Data from Old System)

Not Supported

Upgrade Cluster (Upgrade Application Version or Install COP Files)

From

11.5, 12.x, and 14 and SUs

To

12.5.x and 14 and SUs

Also

From

12.5.x and 14 and SUs

To

15

Restart

11.5, 12.x, 14 and SUs, and 15

Switch Version

11.5, 12.x, 14 and SUs, and 15

Fresh Install New Cluster or Edit or Expand an Existing Cluster

Not Supported

Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster)

12.5.x, 14 and SUs, and 15

## Upgrade Paths for
                        	 Export Restricted and Unrestricted Software

The following
                              		  table lists the supported upgrade paths for applications that have an export
                              		  restricted and an export unrestricted version. You can identify which version
                              		  of an application you have by looking at the license SKU: export unrestricted
                              		  versions are indicated by XU and export restricted versions are indicated by
                              		  K9.

From

To

Task
                                          					 Types Supported

Export
                                          					 Restricted (K9)

Export
                                          					 Restricted (K9)

Supported for Upgrade paths

Supported for Migration paths

Export
                                          					 Restricted (K9)

Export
                                          					 Unrestricted (XU)

Not
                                          					 supported for Upgrade paths

Supported for Migration paths

Export
                                          					 Unrestricted (XU)

Export
                                          					 Restricted (K9)

Not
                                          					 supported for Upgrade paths

Not
                                          					 supported for Migration paths

Export
                                          					 Unrestricted (XU)

Export
                                          					 Unrestricted (XU)

Supported for Upgrade paths

Supported for Migration paths

## Supported ESXi Server Versions

Following table lists the supported ESXi server versions for a Cisco Prime Collaboration Deployment virtual machine (VM).
                              This VM integrates through the VMware APIs with a virtualization host that is running VMs for Cisco Unified Communications
                              Manager or other applications. To view the list of compatible versions of VMware vSphere ESXi server for a Cisco Prime Collaboration
                              Deployment virtual machine that runs on a virtualization host, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-prime-collaboration-deployment.html .

VMware vSphere ESXi on Host having VM of Cisco Unified Communications Manager or Another Application

Cisco Prime Collaboration Deployment Version Compatibility for VMware APIs

6.0 and 6.5

No—For Release 11.5(1)

Yes—For Release 11.5(1) SU1 through 14 and SUs

6.7

No—For Release 15 and later

Yes—For Release 11.5(1) SU1 through 14 and SUs

7.0 U3

Yes—For Release 12.6 and later

8.0 U1

Yes—For Release 14 and later

## Inventory flowchart

Consult the following table for information on the various Inventory use cases for discovering a cluster, add or edit a new
                              or existing cluster, edit or expand clusters, and add or delete ESXi host servers.

Use case

What to do in PCD...

1

Add ESXi hosts

Add an ESXi Host Server

2

ESXi host was changed external to PCD for Discovered Clusters

Delete an ESXi Host Server

Add an ESXi Host Server

3

Add a new Cluster for Fresh Install

Add New Cluster for Fresh Install

Edit or Delete a New Install Cluster

4

Discover a Cluster

Modify and View a Cluster

Perform the various tasks mentioned in the application. See Supported Tasks for Applications and Versions .

5

Update the Cluster Inventory for an already Discovered Custer, where a node was added external to PCD. For example:

Add an IM and Presence Service node to the already-discovered Unified CM cluster.

Add Unified Communications Manager subscriber to an already discovered Unified CM, Unity Connection, and Unified Contact Center
                                                Express cluster.

Delete a cluster from Inventory— Edit or Delete a Discovered Cluster

Discover a Cluster— Discover a Cluster

6

Update the Cluster Inventory for an already discovered cluster, where a node was removed external to PCD. For example, when
                                          you delete a Unified Communications Manager or IM and Presence Service node from the Unified CM cluster.

Delete a cluster from Inventory— Edit or Delete a Discovered Cluster

Discover a Cluster— Discover a Cluster

7

Update the PCD Inventory for an already discovered cluster, where a node was replaced external to PCD. For example, when you
                                          delete a Unified Communications Manager or IM and Presence Service node from the Unified CM cluster, and then add a new node
                                          to the cluster.

Cluster node's count and IP Addresses aren't changed and then updated the cluster using the Refresh Cluster button. (OR)

Cluster node's count or IP Addresses changed.

Delete a cluster from Inventory— Edit or Delete a Discovered Cluster

Discover a Cluster— Discover a Cluster

8

Update the PCD Inventory for an already discovered cluster, where a cluster was upgraded external to the PCD upgrade task.
                                          For example, in scenarios where the Unified CM or IM and Presence Service cluster that was directly upgraded using OS Admin
                                          UI or CLI after the time of discovery.

Cluster node's count and IP Addresses aren't changed and then updated the cluster using the Refresh Cluster button. (OR)

Cluster node's count or IP Addresses changed.

Delete Cluster from Inventory— Edit or Delete a Discovered Cluster

Discover a Cluster— Discover a Cluster

9

Update PCD Inventory for an already discovered cluster, where a cluster needs to have the following configuration values changed
                                          (and it’s desired to configure them directly from PCD versus using the application OS Admin UI or CLI):

Admin Username

Password

NAT IP Assign

SFTP server details

Notes

You can use the Edit Node option to change the mentioned configuration values and proceed with other tasks.

10

Update PCD Inventory for an already discovered cluster, where a cluster needs to have one or more nodes added to perform mixed
                                          node installation.

You can use the Edit cluster option to add one or more nodes and then proceed with installation.

See Edit or Delete a Discovered Cluster .

### Add an ESXi Host Server

Important

To communicate with an ESXi host server, Cisco Prime Collaboration Deployment requires either root access to the ESXi software
                                 or a nonroot user with Host(Configuration, Storage Partition Configuration) and Virtual Machine(Interaction, Configure CD Media, Configure Floppy Media, Device Connection, Power Off, and Power On) privileges enabled. The administrator creates a nonroot user with the specific permissions for Cisco Prime Collaboration
                                 Deployment tasks, such as Interactions, Configure CD Media, Configure Floppy Media, Device Connection, Power Off, and Power
                                 On privileges, for the fresh install or migration. The length of the nonroot user password must be less than 16 characters.

For more information on user password, see Frequently Asked Questions About the Installation .

Make sure that the host with the Cisco Prime Collaboration Deployment VM and the host with the application VMs use the required
                                             Virtualization Software License. See Virtualization Software License Types .

Ensure that the ESXi password is less than 32 characters, cluster password (install/discovered/migration) is less than 16
                                             characters and are compliant with the preceding section that describes allowable special characters.

For more information on restrictions on the password format that are allowed for Cisco Unified Communications Manager, see
                                             the Administration Guide for Cisco Unified Communications Manager and IM and Presence Service .

Step 1

From the Cisco Prime Collaboration Deployment application, click the open and close navigation button and choose the Inventory > ESXi Hosts from the menu.

Step 2

Click Add ESXi Host .

Step 3

The Add Host Server dialog box appears. Enter the following information:

Hostname/IP Address

Root sign-in or sufficiently privileged nonroot sign-in

Root password or nonroot password

Step 4

Click OK to add the ESXi host.

### Delete an ESXi Host Server

Step 1

From the Cisco Prime Collaboration Deployment application, click the open and close navigation button and choose the Inventory > ESXi Hosts from the menu.

Step 2

Click Delete .

### Add New Cluster
                           	 for Fresh Install

Step 1

From the Cisco
                                          			 Prime Collaboration Deployment application, select Inventory > Clusters .

Step 2

Click Define
                                             				New UC Cluster .

Step 3

In the Specify
                                          			 Cluster Name section, enter the cluster name, and click Next .

Step 4

Click Add
                                             				Node to add nodes to the cluster.

Step 5

On the Add
                                             				Node window, enter the network settings for the node that you have
                                          			 added, choose the functions for the node, and choose a VM for this node. Select
                                          			 the VM that you wish to add and then enter the following information in the
                                          			 sections below the VM table:

In Network
                                                				  section, select either Static IP Address or Use DHCP with reservations . If you select the Static IP Address option, enter the hostname, IP
                                                				  Address, subnet mask, gateway, and NAT IP. If you select Use DHCP with reservations option, enter the IP
                                                				  address that you have a reservation for on your DHCP server (associated with
                                                				  the MAC address for that VM) in addition to the hostname.

NAT IP is an optional field. In Step 4, if you have selected a node that is behind NAT, enter the IP address in the NAT IP field, else leave this field blank. The value that you enter in this field appears in the NAT IP column. If the NAT IP address is associated with a port, you can enter port value which should be in the range of 1–65535.

From the Products and Functions list box, select a product.

In the
                                                				  Functions section, check the appropriate function check boxes for your VM.

Check the Publisher check box for at least one node in the
                                                                     							 cluster that you have defined, for each application type.

(Optional) Add a note about the functions that you have assigned
                                                                     							 in the Notes field below the Publisher field.

Click OK .

In Virtual
                                                				  Machines section, choose a VM for this node.

Choose a new VM for fresh install clusters and that new VMs must
                                                                     							 be in turned off state.

Do
                                                                     							 not install over an existing running Cisco Unified Communications Manager node.
                                                                     							 The installation must be a fresh VM that you create with the appropriate OVA
                                                                     							 for the application that you will install.

Step 6

Click OK .

Step 7

(Optional)
                                          			 To add more nodes to the cluster, repeat steps 4 through 6.

Step 8

Click Next .

Step 9

Enter the OS
                                          			 administration credentials, application credentials, security password, SMTP
                                          			 settings, and certificate information for this cluster, and click Next .

Before you enable FIPS mode, Common Criteria, or Enhanced Security Mode, ensure that you have minimum 14 characters for Security
                                                         Password.

Step 10

(Optional) Add
                                          			 a DNS setting for a node, select the node, and click Assign
                                             				DNS Settings .

Step 11

Enter IP
                                          			 address of at least one NTP server.

It is
                                                               						recommended that you define at least IP addresses of two NTP servers.

If you
                                                               						are not using DNS, NTP server must be an IP address. If you are using DNS, NTP
                                                               						server can be an FQDN.

Step 12

Click Next .

Step 13

(Optional)
                                          			 Choose the server, and enter an MTU size between 552 and 1500, and click Apply
                                             				to Selected .

Step 14

Click Next .

Step 15

Select a node,
                                          			 choose the region and time zone from the Region and Time
                                             				Zones list boxes, and click Apply
                                             				to Selected .

Step 16

Click Finish .

### Edit or Delete a
                           	 New Install Cluster

Edit or delete an
                                 		  added new node that has not yet been installed. A node that has not been
                                 		  installed appears active.

Step 1

To edit an existing node, perform the following:

From the Cisco Prime Collaboration Deployment application, click the open and close navigation button and choose Inventory > Clusters .

Click a cluster that has the cluster type as New Install and click Edit .

In the Specify Cluster Name section, view the pre-populated cluster name, and click Next .

In the Add Virtual Machines section, select a node from the existing nodes, and click Edit .

In the Add Node window, edit the node details, and click OK .

In the Configure Cluster Wide Settings section, edit the OS administration credentials, application credentials, security
                                                password, SMTP settings, and certificate information for all nodes of a cluster, as required, and click Next .

Before you enable FIPS mode, Common Criteria, or Enhanced Secuirty Mode, ensure that you have minimum 14 characters for Security
                                                               Password.

(Optional) In the Configure DNS Settings section, edit the DNS settings for the migration cluster nodes, and click Next .

If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes and is auto-populated. If the previous nodes have multiple values for DNS or domain, then
                                                               no default value is applied.

In the Configure NTP Settings section, edit the configuration of the NTP servers for the nodes in a cluster, and click Next .

(Optional) In the Configure NIC Settings section, choose a server, and enter an MTU size between 552 and 1500, click Apply to Selected , and then click Next .

In the Configure Time Zones section, select a node, edit the region and time zone from the Region and Time Zones list boxes,
                                                click Apply to Selected , and then click Finish .

If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                               default value for the new nodes and is auto-populated. If the previous nodes have multiple values for time zone, then no default
                                                               value is applied.

Step 2

To delete an existing node, perform the following:

From the Cisco Prime Collaboration Deployment application, click the open and close navigation button and choose Inventory > Clusters .

Click a cluster that has the cluster type as New Install and click Delete .

### Discover a Cluster

With the Discover Cluster feature, Cisco Prime Collaboration Deployment communicates with the servers that are already running
                                 Unified Communications applications and adds that cluster information into the Cisco Prime Collaboration Deployment inventory.

Add a cluster to the Cisco Prime Collaboration Deployment inventory before you can use it in a task. The Discover Cluster
                                 feature is used to add existing clusters to the inventory. To create a new cluster by migrating an old cluster to new virtual
                                 machines, click Define Migration Destination Cluster . To install a new cluster, click Define New UC Cluster .

When you perform the Discover Cluster operation, the Cisco Prime Collaboration Deployment server communicates with the publisher
                                 of the cluster and retrieves the cluster information. Then, it communicates with each server, installs the ciscocm.ucmap_platformconfig.cop file on the server (to retrieve configuration information), and collects information about the hostname, IP, product type,
                                 and both active and inactive versions for that server.

From 10.x and above UC clusters, Cisco Prime Collaboration Deployment uses SOAP requests to pull platformConfig.xml file from
                                 UC nodes. The cop file “ciscocm.ucmap_platformconfig.cop” is installed if Platform Administrative Web Service (PAWS) is not
                                 available.

Ensure that both the Cisco Prime Collaboration Deployment and UC clusters match the FIPS settings, either in the FIPS mode
                                             or in the non-FIPS mode, before proceeding with cluster discovery.

For details on the supported applications, see "Supported Upgrade and Migration Tasks" in the Related Topics section.

If you are upgrading IM and Presence Service nodes to a Maintenance Release (MR) or an Engineering Special (ES) Release and
                                 you are not upgrading Cisco Unified Communications Manager nodes, the following rules apply:

If you are using the Cisco Unified OS Administration interface for upgrade, you must upgrade the Cisco Unified Communications Manager publisher node and then upgrade the IM and Presence Service nodes to an MR or an ES Release.

If you are using the Cisco Prime Collaboration Deployment migration task, choose the Cisco Unified Communications Manager publisher node in addition to the IM and Presence Service nodes.

If you are using the Cisco Prime Collaboration Deployment upgrade task, you do not need to select the Unified Communications Manager publisher node if the first three digits of the new version of IM and Presence Service match the first three digits of the
                                       currently installed version of Unified Communications Manager .

Step 1

From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Inventory > Clusters .

Step 2

Click Discover Cluster to discover the existing clusters.

Step 3

Enter details in the following fields:

- Choose a Nickname for this Cluster

For a cluster that has both Unified Communications Manager and IM and Presence Service nodes, enter the hostname or IP address
                                                            of the Cisco Unified Communications Manager publisher.

When the publisher is behind the NAT, providing the private IP address of the publisher does not reach to the node. You must
                                                            provide the proper NAT/ Public IP address for successful node discovery.

- OS Admin Username

Ensure that cluster password is less than 16 characters.

You must not use the % character in the Cisco Unified OS Administration password for successful node discovery.

- Enable NAT

Step 4

(Optional) Check the Enable NAT check box, and then click Next .

Important

Step 5

Click Edit to add NAT IP address, and click OK .

Step 6

Click Resume Discovery to resume the discovery of unreachable nodes.

Step 7

Click Next .

Step 8

(Optional) Click Assign Functions to assign functions to each of the cluster nodes.

Step 9

Click Finish .

Contacting —Indicates that Cisco Prime Collaboration Deployment is establishing communication with clusters.

Discovering —Indicates that the cluster discovery is in process.

Successful —Indicates that the cluster discovery is successful.

Node Unreachable —Indicates that the cluster node is inaccessible.

Timeout —Indicates that the duration that is configured for the cluster discovery is complete but no cluster was discovered.

Internal Error —Indicates that cluster discovery is failed because of an incorrect NAT IP address.

### Refresh a Cluster

You can choose one or multiple virtual machines that you have added as nodes in a cluster to view and refresh them.

Step 1

Discover a cluster by following the 'Discover a Cluster' procedure. See Discover a Cluster .

Step 2

Check the check box of one of the discovered or newly installed clusters to choose a cluster, and click the Refresh Cluster link.

### Modify and View a Cluster

You can select one
                                 		  or multiple virtual machines that you have added as nodes in a cluster to view and modify them.

When you add new nodes to the installed cluster, all
                                             			 fields on Configure NTP Settings page appear dimmed
                                             			 and are non-editable.
                                             		  The fields on the other pages will populate the values of the already installed nodes as the default. If needed, you can
                                             change the values for the newly added nodes.

Step 1

Discover a cluster by following the 'Discover a Cluster' procedure. See Discover a Cluster .

Step 2

Check the check box of one of the discovered or newly installed clusters to choose a cluster, and click Edit link.

Step 3

On the Edit Link window, view the details in the fields, and modify the details, as required.

Step 4

Click OK .

### Edit or Delete a
                           	 Discovered Cluster

You can edit or
                                 		  delete a node that has not yet been installed. A node that has not been
                                 		  installed appears active and the installed nodes appear inactive.

After you add
                                             			 or install a new node, you cannot delete the node with this feature. You must
                                             			 delete the node from an existing installed cluster by using your application
                                             			 administration web page or the CLI.

Step 1

To edit a node, from the Cisco Prime Collaboration Deployment application, click the open and close navigation button and
                                          choose Inventory > Clusters .

From the Cisco Prime Collaboration Deployment application, select Inventory > Clusters .

Select a cluster that has the cluster type as Discovered and click Edit .

In the Specify Cluster Name section, enter the cluster name, and click Next .

In the Add Virtual Machines section, select a node from the existing nodes that has not been installed, and click Edit .

In the Add Node window, edit the node details, and click OK , and then click Next in the Add Virtual Machines section.

In the Configure Cluster Wide Settings section, view the OS administration credentials, application credentials, security
                                                password, SMTP settings, and certificate information for all nodes of a cluster and click Next .

(Optional) In the Configure DNS Settings section, edit the DNS settings for the migration cluster nodes, and click Next .

If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes. If the previous nodes have multiple values for each DNS or domain, then no default value
                                                               is applied.

In the Configure NTP Settings section, view the configuration of the NTP servers for the nodes in a cluster, and click Next .

(Optional) In the Configure NIC Settings section, edit the server details for the uninstalled nodes, enter an MTU size between
                                                552 and 1500, and then click Next .

In the Configure Time Zones section, select a node, edit the region and time zone from the Region and Time Zones list boxes,
                                                click Apply to Selected , and then click Finish .

Step 2

To delete a node, perform the following:

From the Cisco Prime Collaboration Deployment application, select Inventory > Clusters .

Select a cluster that has the cluster type as Discovered and click Delete to remove the selected node.

### Edit a Node

You can edit one or multiple virtual machines that you have added as nodes in a cluster.

Step 1

From the Cisco Prime Collaboration Deployment application, select Inventory > Clusters .

Step 2

Discover a cluster by following the 'Discover a Cluster' procedure. See Discover a Cluster .

Step 3

Check the check box of one of the discovered or newly installed clusters to choose a node, and click Edit Node link.

Step 4

In the Edit Node window, view the details in the fields, and modify the details, as required.

Step 5

Click OK .

## Task
                        	 Management

After you add your clusters
                              		  and ESXi hosts to the Cisco Prime Collaboration Development
                              		  inventory, you can create tasks to manage your clusters. Each task has the
                              		  following common features:

Each task is
                                    				applied to a single cluster.

The default
                                    				sequence for each task (for example, what servers are affected and when) is
                                    				applied based on the server functions you defined.

The sequence of each task can be customized to fit your needs.

Each task can
                                    				be scheduled to start immediately or at a later date.

Tasks can also
                                    				be created without a specific start time. You can then manually start the task
                                    				through the Monitoring page at the appropriate time.

Migration, install, and upgrade tasks require you to select one or more Cisco Option Packages (COP) or ISO files. You must
                              download these files from Cisco.com and upload them to the Cisco Prime Collaboration Deployment server before you create the
                              task. You can use any SFTP client to upload the files using the "adminsftp" account and the OS Administration password. Upload
                              migration and .iso install files into the /fresh_install directory, and place upgrade .iso files or .cop files to be installed on an existing server in the /upgrade directory.

### Migration Task

#### Before You Begin

To perform cluster migration, the destination-virtual machine must be ready for installation before you create the migration
                                 task. Be sure that the following steps are completed:

VMware —Deploy the hardware for the new cluster and install ESXi.

ISO file —Download the recommended OVA and ISO images for the target release, and use SFTP to send the ISO file to the Cisco Prime
                                       Collaboration Deployment server, /fresh_install directory.

VMware —Deploy the Cisco-recommended OVA to create the VMs for the destination nodes. Create the appropriate number of target-virtual
                                       machines on your ESXi hosts (one new virtual machine for each server in the existing cluster) using the Cisco OVAs that you
                                       downloaded in Step 2. Configure the network settings on new VMs.

Cisco Prime Collaboration Deployment GUI —Add the ESXi Hosts that contain your virtual machines to the Cisco Prime Collaboration Deployment inventory. For information
                                       about adding an ESXi host to Cisco Prime Collaboration Deployment, see Add an ESXi Host Server .

Cisco Prime Collaboration Deployment GUI —Ensure that you performed a cluster discovery for the existing cluster (source cluster) so that it appears in the Cluster
                                       Inventory. For information about cluster discovery, see Discover a Cluster .

Cisco Prime Collaboration Deployment GUI —Create the migration cluster (click Open and close navigation and choose Inventory > Clusters ) to define the mapping between MCS source nodes and target-virtual machines.

Important

Using the source node settings for all destination nodes option is called a simple migration. See the migration flow chart
                                             for more information.

Entering new network settings for one or more destination nodes is called a network migration. See the migration flow chart
                                             for more information.

Cisco Prime Collaboration Deployment GUI —Setup Email Notification (Optional)

Click open and close navigation and choose Administration > Email Notification .

When email notification is set up, the Prime Collaboration Deployment server emails the error conditions that may occur during
                                             the migration task.

Cisco Prime Collaboration Deployment GUI —Create the migration task.

Special Considerations

If you are migrating a cluster that is security enabled, see More Information for special instructions. If you are performing a migration with network migration (where one or more hostnames or IP addresses
                                       change between the source and destination nodes), update the IP addresses or hostnames of destination nodes in your DNS server
                                       before you begin the migration task.

You can specify a different NAT address for source and destination, so that the source is not abruptly shut down. If you
                                       want to perform a simple migration but need to specify different Network Address Translation (NAT) entries for source and
                                       destination, you must select "Network Migration" and provide the same details for source and destination (all hostnames and IP addresses).

Before migrating the cluster, we recommend installing the latest Upgrade Readiness COP file. See the for details. This is applicable if the source cluster is 10.x or above and valid only for Unified Communications Manager
                                                   and IM and Presence Service.

Make sure that Prime Collaboration Deployment has enough free space depending on the size of the source cluster in the common
                                                   partition.

If your 14SU2 or later versions of Cisco Prime Collaboration Deployment is in FIPS mode and you are using any of the Pre-12.5
                                                   UC clusters to perform migration, you must first switch your Cisco Prime Collaboration Deployment to work in the non-FIPS
                                                   mode before proceeding with migration. You can also use the Fresh Install with Data Import (V2V) option if you do not plan
                                                   to use Cisco Prime Collaboration Deployment for migration.

#### Create a Migration
                              	 Task

Follow these steps
                                    		  to create or edit a new migration task to simultaneously upgrade and migrate a
                                    		  cluster to new virtual machines.

Note the supported
                                    		  restricted and unrestricted paths. See "Supported Upgrade and Migration Tasks" and "Upgrade Paths for Export Restricted and Unrestricted Software" in
                                    		  the Related Topics section.

Step 1

Click Open and close navigation and choose Task > Migrate .

Step 2

Click Add Migration Task . The Add Migration Task wizard appears.

Step 3

In the Specify Task Name drop-down, enter a name for the migration task in Choose a Nickname for this Migration Task .

Step 4

From the Source UC Cluster drop-down list, select the cluster on which the nodes to be migrated from are located.

Step 5

From the Destination Cluster drop-down list, select the destination cluster or migration map. The migration maps are associated with the source cluster
                                             you have selected. Click Next .

If you want to apply an upgrade patch along with the migration, click Yes radio button. Click No radio button to proceed with migration task only.

Step 6

In the Choose Migration Files section, choose the ISO file you wish to install on the destination cluster by clicking Browse . The Choose a Migration File window opens. Select the ISO file from the list and click OK .

If you have applied upgrade patch along with the migration, browse the patch files along with the ISO files for Unified Communications
                                                Manager and IM and Presence Service

You must select the patch file of the same Engineering Special (ES)/ Service Update (SU) versions of the ISO file.

Important

The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP.

If you select Prime Collaboration Deployment as SFTP, then you can place the migration file under /fresh_install and the upgrade patch file under /upgrade directory. If you select any remote SFTP, then both migration and upgrade patch file should be in the same SFTP server.

When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different.

Step 7

If you want to make the newly created task as dependent on the successful completion of another previously executed task,
                                             check the checkbox of the tasks listed in the Task Dependency Scheduling .

You can select multiple tasks as dependent tasks. If you do not want to make any dependency, check the No Dependency checkbox.

Step 8

Click Next .

Step 9

In the Specify Migration Procedure section, you will see the default sequence for the migration task. If you wish, you can change the sequence of steps in the
                                             migration procedure. (For example, the default is to install each subscriber individually. You might want to change this to
                                             install more than one subscriber in a step.) You have the following options:

Edit a step.

Add a new step after the current step.

Delete the current step.

If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the Publisher
                                                         node.

Move the step up to be performed earlier.

Move the step down to be performed later.

- The Pencil icon opens up an Edit Step window. Add nodes to be migrated in this step from the list of available nodes. The available nodes are the ones that you
                                                chose for migration.

- The step to which each node is assigned displays next to the node. If a node is not assigned to any step, it shows as unassigned.

When you assign all the nodes to a step, a default sequencing is available.

Important

You cannot proceed to the next step until you assign all the nodes.

- The Pause task after step completes option pauses the task after completion of this step. You must manually start the next step to complete the task.

For more information about sequencing tasks, see the task management information at the beginning of this section.

Step 10

Select the date and time when you want the migrate task to begin. You have the following options to schedule upgrades:

If the task is created as depended task, then Set Start Time section is disabled.

Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task.

If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically.

If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page.

- Select Start task immediately upon completion of this wizard to start the task immediately after you click Finish .

- If you want the system to automatically switch to the new version, choose the option Upgrade Option to Automatically Switch to New Version after Successful Upgrade .

Step 11

Click Next .

Step 12

In the Review section, you can review the selections that you made. You can also add notes to your new migration task.

Step 13

If there are no changes required, click Finish to add your new migration task.

Step 14

The new migration task appears in the table on the Migrate screen.

Important

#### Create a Migration
                              	 Cluster

##### Before you begin

Discover the existing cluster that you wish to migrate. See the "Discover a Cluster" procedure at Discover a Cluster .

Define a
                                          				migration cluster.

Step 1

From the Cisco
                                             			 Prime Collaboration Deployment application, select Inventory > Cluster .

Step 2

Click Define
                                                				Migration Destination Cluster .

Step 3

In the Specify
                                             			 Clusters section, specify the name of the cluster, select the source UC cluster
                                             			 from the drop-down list. Enter a name in the Destination Cluster Name field and
                                             			 select one of the following Destination Network Settings options:

- To retain the default
                                                				network options, select the Use
                                                   				  the source node network settings for all destination nodes option.

- To modify the default
                                                				network settings or enter new network options, select the Enter new network settings for one or more destination
                                                   				  nodes option.

If you
                                                            				  select the Use the source node network settings for all destination
                                                               					 nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns Assign Destination Cluster Nodes . If you select the Enter new network settings for one or more destination
                                                               					 nodes option, only source hostname appears and not the destination
                                                            				  hostname on the Assign Destination Cluster Nodes window.

Step 4

Click Next .

Step 5

Click Assign Destination Cluster Nodes to select the destination virtual machine for each source node.

If DHCP is in use on your source node, the destination node will also be configured to use DHCP, and you will not have the
                                                            option of changing your network settings in this wizard.

Step 6

Select a
                                             			 virtual machine, click Next
                                                				Node to go to the next node in the cluster, and select another
                                             			 virtual machine for the destination virtual machine, and click Done .

If there
                                                            				  is more than one node in the cluster, repeat these steps - (assigning VM, and
                                                            				  entering new IP/hostname settings, if needed) for each node in the source
                                                            				  cluster.

Step 7

Click Next .

Step 8

Enter the
                                             			 Network Time Protocol (NTP) server settings to be applied to the migration
                                             			 nodes when the migration task runs, and optionally, enter the SMTP server
                                             			 settings.

Important

In a proxy
                                                            				  TFTP setup, if a network migration is performed "off-cluster", you need to
                                                            				  manually configure the new hostname and IP address of that off-cluster in the
                                                            				  proxy TFTP. Off-cluster refers to situations where TFTP functionality is being
                                                            				  performed by a proxy that is not part of that specific Unified Communications
                                                            				  Manager cluster. During a migration, that TFTP server (that is not part of the
                                                            				  cluster) is not modified. If you want to change the hostname or IP address of
                                                            				  that server, you must do it as a separate process and not with Cisco Prime
                                                            				  Collaboration Deployment.

Step 9

Click Next .

Step 10

To change the
                                             			 DNS setting for a node, select the node or nodes from the table and click Assign
                                                				DNS Settings . Enter the primary and secondary DNS, then click OK to apply the changes.

Important

You cannot
                                                            				  change the domain name during a migration.

Step 11

Click Finish .

The changes
                                                				are saved and a row is added to the clusters table to reflect the new migration
                                                				cluster that you have created.

#### Run a Migration Task

If you scheduled the task to start at later date, or if you chose Manual Start, then the task is listed in the task list,
                                 but has not started yet. In this case, a validation button will be associated with the task. Click Validate to check the task before it runs. If there are any problems with the task (such as a missing ISO file, or VMs not in Off
                                 state), the validation will alert you, so the issues can be fixed before the task starts.

For a task that was scheduled to start, you can click the Start button to begin the task.

While the migration task is running, depending on the type of migration task, some user operations might be needed. For example,
                                 if you are performing a "migration with network migration," the sequence automatically inserts a "Forced Pause" into the sequence after all the servers have been installed. This will cause the migration task to pause after all the new
                                 servers are installed but before any of the source machines are shut down.

Consult the table below and the applicable Migration Procedure flow chart (see the "Migration Procedure Flow Charts" section) to determine if any user interaction will be needed during the migration task.

Important

When the migration cluster is created, you must indicate whether all destination nodes will keep the same hostname or IP address,
                                             or if some of these addresses will be changing.

Using the source node settings for the all destination nodes option is referred to as a “simple migration” in the "Migration Procedure Flow Charts" section.

Entering new network settings for one or more destination nodes option is referred as "network migration" in the "Migration Procedure Flow Charts" section.

10.x

10.x

10.x

When the migration task reaches the Forced Paused step, perform the following steps:

CTL Update

Bulk Certificate Management

Resume the task on Cisco Prime Collaboration Deployment GUI.

10.x

When the migration task reaches the Forced Paused step, perform the following steps:

Bulk Certificate Management

Resume the task on Cisco Prime Collaboration Deployment GUI.

11.x, 12.x, 14 and SUs, and 15

Simple migration

Secure

No steps are required during migration.

11.x, 12.x, 14 and SUs, and 15

Simple migration

Nonsecure

No steps are required during migration.

11.x, 12.x, 14 and SUs, and 15

Network migration

Secure

When the migration task reaches the Forced Paused step, perform the following steps:

CTL Update

Bulk Certificate Management

Resume the task on Cisco Prime Collaboration Deployment GUI.

11.x, 12.x, 14 and SUs, and 15

Network migration

Nonsecure

When the migration task reaches the Forced Paused step, perform the following steps:

Bulk Certificate Management

Resume the task on Cisco Prime Collaboration Deployment GUI.

#### Postmigration Tasks for Unified Communication Manager Nodes in the Cluster

Consult the following table and the applicable migration Use Case flowchart to determine whether any user tasks should perform
                                    after the migration task is successful.

Unified CM source cluster—from Release

User procedures to be performed after migration

10.x

Network migration

Secure

Change TFTP Server IP Address.

Verify Phone Registration.

Network migration

Nonsecure

Change TFTP Server IP Address.

Verify Phone Registration.

11.x, 12.x, 14 and SUs, and 15

Network Migration

Secure

Change TFTP Server IP Address.

Verify Phone Registration.

Network Migration

Nonsecure

Change TFTP Server IP Address.

Verify Phone Registration.

Device default settings will not be carried over from source cluster to destination cluster after a simple or network migration
                                                task.

Any device packs installed for specific features need to be reinstalled if destination cluster version doesn't already include
                                                the device pack feature.

#### Post Migration
                              	 Tasks for IM and Presence Service

If the migrated cluster
                                    		  contains IM and Presence Service nodes, and you are performing a network
                                    		  migration, these postinstallation tasks must be performed for any pre-Release
                                    		  10.x IM and Presence Service cluster.

Step 1

Configure
                                             			 certificates and certificate trust stores.

For more information, see the Administration Guide for Cisco Unified Communications Manager
                                                   				  Guide .

Step 2

Configure
                                             			 intercluster peers.

Step 3

Re-publish SIP
                                             			 Federation.

Step 4

Re-publish
                                             			 XMPP Federation.

Step 5

Configure
                                             			 Cisco Jabber/Cisco Unified Personal Communicator connectivity.

#### Migration Procedure Flow Charts

Use the
                                 				following task flows as a guide to perform migration tasks.

#### Simple
                              	 Migration

Cisco Prime Collaboration Deployment does not support migration of
                                                			 Business Edition 5000 Appliance running on MCS 7828H3.

#### Pre Release 10.0 Unified CM Network Migration

#### Release 10.0 And Later Unified CM Network Migration

### Recovery of Original Cluster

Use the following
                                 		  procedure when a cluster fails to migrate successfully, and some nodes
                                 		  are installed on the new cluster.

### Check the Status
                           	 of the Cluster Manager Service on All Source Nodes

The steps below are used if a migration task
                                 		  fails when there were network migration changes on one or more nodes. Following the
                                 		  failure, you may need to perform some steps to get the old cluster nodes
                                 		  running again. See the flow chart above for all steps to be followed. Below
                                 		  are detailed steps for running the CLI command to restart cluster manager on
                                 		  old nodes.

Perform the following steps manually on all subscriber nodes that were
                                 		  supposed to have network changes (for example, hostname, IP address, or both)
                                 		  after all old cluster nodes are up and running.

Use cases that may require the restart of Cluster manager on source
                                 		  nodes are:

Use Case 1

No hostname and no IP address change on Publisher, hostname change on Subscriber

The user is required to check Cluster Manager service on source Subscriber

Use Case 2

No hostname and no IP address change on Publisher, IP address change
                                 		  on Subscriber

The user is required to check Cluster Manager service on source Subscriber

Use Case 3

No hostname and no IP address change on Publisher, hostname, and IP address change on Subscriber

The user is required to check Cluster Manager service on source Subscriber

Use Case 4

No hostname change on Publisher, IP address change on Publisher, no
                                 		  hostname and no IP Subscriber

The user is required to check Cluster Manager service on source Publisher

Step 1

Enter the following CLI
                                          			 command at the command prompt: utils service list . The following output appears:

```
Requesting service status, please wait...
System SSH [STARTED] 
Cluster Manager [STOPPED]
```

Step 2

If Cluster Manager Service status is STOPPED, type the following
                                          			 command to start the service on the old subscriber node:

### Upgrade Task

Use Cisco Prime Collaboration Deployment to perform the following types of upgrade tasks:

Direct standard upgrade—This upgrade does not require upgrades to the embedded operating system. You can install upgrade software
                                    on your server while the system continues to operate.

Direct refresh upgrade—This upgrade is required in situations where incompatibilities exist between the old and new software
                                    releases. For example, a refresh upgrade is required when the major version of the embedded operating system changes between
                                    the version you are upgrading from and the version that you are upgrading to.

The application automatically determines whether you need to perform a direct standard upgrade or a direct refresh upgrade.

#### Create an Upgrade
                              	 Task

Use the upgrade
                                    		  task to perform software version upgrades on a cluster. You can also use an
                                    		  upgrade task to install .cop files on all or a subset of servers in a cluster.

To know the supported applications, releases, and versions, see the see "Supported Upgrade and Migration Tasks" and "Upgrade Paths for Export Restricted and Unrestricted Software" in the Related Topics section.

Use the Add
                                    		  Upgrade Task wizard to create and edit upgrade tasks.

To create or edit
                                    		  a new upgrade task to automatically run on one or more clusters at scheduled
                                    		  times, follow these steps.

##### Before you begin

Note the
                                          				supported restricted and unrestricted paths. See "Supported
                                             				  Upgrade and Migration Tasks" and "Upgrade
                                             				  Paths for Export Restricted and Unrestricted Software" in the Related Topics
                                          				section.

Perform a
                                          				cluster discovery for the cluster that you wish to upgrade, so it appears in
                                          				the Cluster Inventory. See Discover a Cluster .

Download the
                                          				ISO files you wish to upgrade to, and use SFTP to send this file to Cisco Prime
                                          				Collaboration Deployment in the upgrade folder. If you are using the upgrade
                                          				task to install a .cop file, upload the .cop file to the /upgrade folder using
                                          				an SFTP client.

For the
                                          				application servers in the cluster to be upgraded, ensure that the Platform
                                          				Administrative Web Service is active on that server.

Before upgrading the cluster, Cisco recommends to install the latest Upgrade Readiness COP file. Refer to the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service for details. This is applicable if the source cluster is 9.X or above and valid only for Unified Communications Manager
                                                and IM&P.

Step 1

Click Open and close navigation and choose Task > Upgrade from the main menu.

Step 2

Click Add
                                                				Upgrade Task .

Step 3

In the Specify Task Name drop-down, enter a name for the upgrade task in Choose a Nickname for this Upgrade Task .

Step 4

Select the upgrade type as ISO or COP .

You can install multiple cops files in a single upgrade task.

Maximum 32 COP files can be selected for a specific product.

Step 5

From the Cluster drop-down list, select the cluster on which
                                             			 the nodes to be upgraded are located.

Step 6

If you want to make the newly created task as dependent on the successful completion of another previously executed task,
                                             check the checkbox of the tasks listed in the Task Dependency Scheduling .

You can select multiple tasks as dependent tasks. If you do not want to make any dependency, check the No Dependency checkbox.

You can make an upgrade ISO task dependent on an upgrade task only.

You can make an upgrade COP task dependent on Install and Migration task.

Step 7

Select the
                                             			 nodes that are part of the upgrade from the list of nodes.

Step 8

Click Next .

The Next button is dimmed if no nodes are selected.

Step 9

Click the
                                             			 respective Browse buttons to select the upgrade files from the
                                             			 file server.

The option
                                                            				  to select upgrade files is available only for the selected product types and
                                                            				  applications that are currently supported in the cluster.

Step 10

Select a valid upgrade file or files.

When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different.

Step 11

Click Choose
                                                				File .

Step 12

Click Next .

Step 13

Select the date and time when you want the upgrade task to begin. You have the following options to schedule upgrades:

If the task is created as depended task, then Set Start Time section is disabled.

Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task.

If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically.

If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page.

- Select Start task immediately upon completion of this wizard to start the task immediately after you click Finish .

- If you want the system to automatically switch to the new version, choose the option Upgrade Option to Automatically Switch to New Version after Successful Upgrade . Otherwise, the server, or servers, are upgraded but remain on the current version of software. In that case, you can schedule
                                                a switch version task to switch over to the upgraded version of software.

Step 14

Click Next .

Step 15

Specify the
                                             			 sequence of steps to complete the task. You have the following options:

Edit a
                                                         					 step.

Add a new
                                                         					 step after the current step.

Delete the
                                                         					 current step.

If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the publisher
                                                         node.

Move the
                                                         					 step up to be performed earlier.

Move the
                                                         					 step down to be performed later.

- The Pencil icon opens up an Edit Step window. Add nodes to be upgraded in this
                                                				step from the list of available nodes. The available nodes are the ones that
                                                				you chose for an upgrade.

- The step to which each node
                                                				is assigned displays next to the node. If a node is not assigned to any step,
                                                				it shows as unassigned.

Important

You cannot proceed to next step until you assign all the nodes.

- The Pause task after step completes option pauses the task after completion of this step. Manually start the next step to complete the task.

Step 16

Click OK .

Step 17

Click Next .

The Next button remains enabled, which allows you to click to display any configuration errors.

Step 18

See the Review section to verify the details of the task you created. You can add notes for the task, if necessary. The notes are saved
                                             with the task and are visible if the task is edited before completion.

Step 19

Click Finish to schedule the task.

### Direct Refresh Upgrade

You can perform refresh upgrade to upgrade from existing version of a product to a later version where operating systems of
                                 both the versions are different. The supported products for this upgrade are Cisco Unified Communications Manager, IM and
                                 Presence Service, Cisco Unity Connection, Cisco Unified Contact Center Express, and Cisco Emergency Responder .

In the earlier releases, after direct refresh upgrade, although Cisco Unified Communications Manager was upgraded to the new
                                 version, it used to switch back to its older version. The new version used to be an inactive version. For the new version
                                 to be the active version, switch version was required. The switch back used to happen because upgrade and switch version were
                                 two separate steps. It implies that the version had to be switched twice to make the new version after direct refresh upgrade.

To prevent switch version twice, in this release, Cisco Prime Collaboration Deployment includes switch version step as part
                                 of upgrade step during refresh upgrade. Check the Automatically switch to new version after successful upgrade check box in the Upgrade Task window during upgrade task configuration. Then, the switch version of the product (either Cisco Unified Communications Manager
                                 or IM and Presence Service) is included as part of the upgrade step. However, the switch version step appears as a separate
                                 step if the upgrade is for Cisco Unified Communications Manager and IM and Presence Service cluster.

### Database Replication

Database replication is one of the steps of refresh upgrade process. Cisco Prime Collaboration Deployment runs services and
                                 commands and waits for the database replication status of the selected Cisco Unified Communications Manager nodes.

For more information, see "Sequencing Rules and Time Requirements" chapter of the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html .

Cisco Prime Collaboration Deployment checks the database replication when you choose the cluster that is combined with Cisco
                                             Unified Communications Manager and IM and Presence Service. The database replication runs only for Cisco Unified Communications
                                             Manager before the IM and Presence Service upgrade or switch.

Only after successful database replication, the next task that is listed in the upgrade sequence starts. The tasks listed
                                 after database replication include upgrade or switch version of IM and Presence Service subscriber nodes.

### Reuse Sequence
                           	 from Previous Task

The Reuse Sequence
                                 		  from Previous Task feature uses a previously defined task sequence in the task
                                 		  you are currently creating. This feature is useful for upgrade, restart, switch
                                 		  version, migration, and readdress tasks. 
                                 		It allows you to reuse a previously configured task sequence as opposed to having to rescript the sequence from scratch.

During task
                                 		  creation, the task wizard progresses to the sequence pane where a user can
                                 		  configure the ordering and pause characteristics. If there is a task in the
                                 		  system of 
                                 		  similar
                                 			 type, the sequence from that task is presented as the default sequence.

In
                                 		  this case, a check box labeled Use Last
                                    			 Configured Run Sequence is visible just above the sequence
                                 		  table. You can check the check box to use the sequence from the previous task
                                 		  or leave the check box unchecked to use the default sequence that the system generates.

To be considered a
                                 		  task of 
                                 		  similar
                                 			 type, the selected cluster, task type, and nodes in the task must match
                                 		  exactly. If multiple tasks meet the 
                                 		  similar type
                                 		  criteria, the most recently created task is used and its sequence is presented
                                 		  as the default to the user.

In the case of an
                                 		  upgrade task, there is an additional requirement. The type of installation must
                                 		  be either ISO based or COP based. The COP and ISO installations can be
                                 		  performed with different sequencing.

### Switch Versions Task

#### Create a Switch
                              	 Versions Task

Use the switch
                                    		  versions task to automatically switch one or more nodes in a cluster to the
                                    		  upgraded or inactive version.

Use the Switch
                                    		  Versions Task wizard to create and edit switch versions tasks.

To know which
                                    		  applications and releases are supported for upgrade tasks, see "Supported Upgrade and Migration Tasks" and "Upgrade Paths for Export Restricted and Unrestricted Software" in
                                    		  the Related Topics section.

To create or edit
                                    		  a switch versions task to automatically switch one or more nodes in a cluster
                                    		  to the upgraded or inactive version at scheduled times, follow this procedure.

The Automatic Switch version option is not available on clusters which contain Unity Connection and Cisco Unified Contact
                                                Center Express nodes. For clusters with Cisco Unity Connection and Cisco Unified Contact Center Express, create an upgrade
                                                task and then create a switch version task to switch to the new version. You can create the switch version task after the
                                                upgrade task runs successfully.

##### Before you begin

Perform a
                                          				cluster discovery for the cluster on which you want to switch versions, so that
                                          				the cluster appears in the Cluster inventory. See Discover a Cluster .
                                          				If you previously used Cisco Prime Collaboration Deployment to upgrade or
                                          				migrate a cluster, the cluster should already be in the inventory.

For each
                                          				application server in the cluster, ensure that the Platform Administrative Web
                                          				Service is active on that server.

Step 1

Click Open and close navigation and choose Tasks > Switch Versions from the main menu.

Step 2

Click Add
                                                				Switch Versions Task .

Step 3

In the Specify Task Name drop-down, enter a name for the switch version task in Choose a Nickname for this Switch Versions Task .

Step 4

From the Cluster drop-down list, select the cluster on which
                                             			 you want to switch the versions.

Step 5

Select the
                                             			 version to which you want all the nodes to be switched.

If there is
                                                            				  more than one product, you can select the applicable versions of all the
                                                            				  different products. You also can choose to switch the version for one product
                                                            				  and to not switch the version for another product.

Step 6

Click Next .

Step 7

Select the
                                             			 date and time when you want the switch versions task to begin. You have the
                                             			 following options to schedule switch versions task:

If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically.

- Select Start task manually to keep the task in a manual
                                                				start.

You can also start the task from the Monitoring page.

- If you want the server to
                                                				automatically switch to the new version, check the check box next to Automatically switch to new version after successful
                                                   				  upgrade .

Step 8

Click Next .

Step 9

Specify the
                                             			 sequence of steps to complete the task. You have the following options:

Edit a
                                                         					 step.

Add a new
                                                         					 step after the current step.

Delete the
                                                         					 current step.

If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node.

Move the
                                                         					 step up to be performed earlier.

Move the
                                                         					 step down to be performed later.

- The Pencil icon opens up an Edit Step window. Add the nodes on which the versions
                                                				must be switched in this step from the list of available nodes. The available
                                                				nodes are the ones that you chose for the switch versions task.

- The step to which each node
                                                				is assigned displays next to the node. If a node is not assigned to any step,
                                                				it shows as unassigned.

When you assign all the nodes to a step, a default sequencing is available.

Important

You cannot proceed to next step until you assign all the nodes.

- The Pause task after step completes option pauses the
                                                				task after completion of this step. You must manually start the next step to
                                                				complete the task.

Step 10

Click OK .

Step 11

Click Next .

The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors.

Step 12

Use the Review section to verify the details of the task
                                             			 that you created. You can add notes for the task if required. The notes are
                                             			 saved with the task and are visible if the task is edited before completion.

Step 13

Click Finish to schedule the task.

### Server Restart
                           	 Task

To know which
                                 		  applications and releases are supported for upgrade tasks, see "Supported Upgrade and Migration Tasks" and "Upgrade Paths for Export Restricted and Unrestricted Software" in
                                 		  the Related Topics section.

#### Create a Server
                              	 Restart Task

Use the Restart
                                    		  Task wizard to create and edit restart tasks.

To create or edit
                                    		  a restart task to automatically restart one or more nodes in a cluster at
                                    		  scheduled times, follow this procedure.

##### Before you begin

Perform a
                                          				cluster discovery for the cluster you wish to restart, so that it appears in
                                          				the Cluster inventory. See Discover a Cluster .

For each
                                          				application server in the cluster, ensure that the Platform Administrative Web
                                          				Service is active on that server.

If you are using Cisco Prime Collaboration Deployment Readdress
                                          				Task with virtual machine of an application, ensure that you follow the
                                          				application's rules for changing IP and hostname—either one at a time or
                                          				simultaneously.

Step 1

Click the
                                             			 open and close navigation button and choose Task > Server
                                                   				  Restart from the main menu.

Step 2

Click Add
                                                				Server Restart Task .

Step 3

In the Specify Task Name drop-down, enter a name for the server restart task in Choose a Nickname for this Server Restart Task .

Step 4

From the Clusters drop-down list, select the cluster on which
                                             			 you want to restart the nodes.

Step 5

If you want to make the newly created restart task as dependent on the successful completion of another previously created
                                             upgrade task, check the checkbox of the tasks listed in the Task Dependency Scheduling.

You can select multiple tasks as dependent tasks. If you do not want to make any dependency, check the No Dependency checkbox.

Step 6

From the
                                             			 table, select the nodes to be restarted. If you do not select any nodes, you
                                             			 cannot continue.

Step 7

Click Next .

Step 8

Select the
                                             			 date and time when you want the server restart task to begin. You have the
                                             			 following options to schedule restart tasks:

If the task is created as depended task, then Set Start Time section is disabled.

Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task.

If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically.

- Select Start the task manually to keep the task in a manual
                                                				start.

You can
                                                               					 also start the task from the Monitoring page.

Step 9

Click Next .

Step 10

Specify the
                                             			 sequence of steps to complete the task. You have the following options:

Edit a
                                                         					 step.

Add a new
                                                         					 step after the current step.

Delete the
                                                         					 current step.

If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node.

Move the
                                                         					 step up to be prepared earlier.

Move the
                                                         					 step down to be prepared later.

- The Pencil icon opens up an Edit
                                                   				  Step window. In this step, add nodes to be restarted from the list
                                                				of available nodes. The available nodes are the ones that you chose for a
                                                				restart.

- The step to which each node
                                                				is assigned appears next to the node. If a node is not assigned to any step,
                                                				that node shows as unassigned.

When you assign all the nodes to a step, a default sequencing is available.

Important

You cannot proceed to the next step until you assign all the nodes.

- The Pause task after step completes option pauses the
                                                				task after completion of this step. You must manually start the next step to
                                                				complete the task.

Step 11

Click OK .

Step 12

Click Next .

The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors.

Step 13

See the Review section to verify the details of the task you
                                             			 created. You can add notes for the task if required. The notes are saved with
                                             			 the task and are visible if the task is edited before completion.

Step 14

Click Finish to schedule the task.

### Readdress Task

#### Create a Readdress Task

Use the readdress task change the hostname or IP address for one or more nodes in a cluster. To use the readdress feature,
                                    the servers must be Release 11.5 or later.

Note the difference between a hostname and a fully qualified domain name (FQDN) The network-level DNS default domain name
                                    of the node is combined with the hostname to form the FQDN for the node. For example, a node with hostname "cucm-server" and domain "example.com" has an FQDN of "imp-server.example.com."

Use the Readdress Task wizard to create and edit readdress tasks.

##### Before you begin

If you have not already done so, perform a cluster discovery for the cluster you wish to readdress, so that it appears in
                                          the Cluster inventory. See Discover a Cluster .

If you are using Cisco Prime Collaboration Deployment Readdress Task with virtual machine of an application, ensure that you
                                          follow the application's rules for changing IP and hostname—either one at a time or simultaneously.

Step 1

Click the open and close navigation button and choose Task > Readdress from the main menu.

Step 2

Click Add Readdress Task .

Step 3

In the Specify Task Name drop-down, enter a name for the readdress task in Choose a Nickname for this Readdress Task .

Step 4

From the Cluster drop-down list, select the cluster on which you want to change the address of the nodes. Click View Nodes to view the Cluster nodes.

Step 5

Click Next .

Step 6

Click Edit next to a node to enter an alternate Hostname, IP Address, Subnet Mask or Gateway.

Step 7

Click OK .

Step 8

Click Next .

Important

When you click Next , Cisco Prime Collaboration Deployment performs a validation test automatically. If the test on a cluster fails, the error
                                                            message describes the failed test. You can continue to create the tasks, but you must resolve the errors described or the
                                                            task fails.

Step 9

Select the date and time when you want the readdress task to begin. You have the following options to schedule readdress tasks:

If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically.

- Select Start task manually to keep the task in a manual start.

You can also start the task from the Monitoring page.

Step 10

Click Next .

Step 11

Specify the sequence of steps to complete the task. You have the following options here:

Edit a step.

Add a new step after the current step.

Move the step up to be executed earlier.

Move the step down to be executed later.

- The step to which each node is assigned displays next to the node. If a node is not assigned to any step, it shows as unassigned.

When you assign all the nodes to a step, there will be a default sequencing available.

Important

You cannot proceed to next step until you assign all the nodes that were selected for this task.

- Cisco Prime Collaboration Deployment automatically inserts a Forced Pause after each sequence step in a Readdress task.

- For a readdress task, only one node can be assigned to each step. Multiple nodes cannot be combined and assigned in a single
                                                step.

Step 12

Click OK .

Step 13

Click Next .

The Next button remains enabled, which allows the user to click to be informed of any configuration errors.

Step 14

See the Review section to verify the details of the task you created. You can add notes for the task if required. The notes are saved with
                                             the task and are visible if the task is edited before completion.

Step 15

Click Finish to schedule the task.

#### Run a Readdress
                              	 Task

If you scheduled
                                    		  the task to start at a later date, or if you chose Manual Start, then the task
                                    		  will be listed in the task list but will not start yet.

For a task that
                                    		  was scheduled for manual start, click the Start button that is associated with this task to
                                    		  begin the task.

While the
                                    		  readdress task is running, if there is more than one server to be readdressed
                                    		  in the task, some user operations are needed. The readdress task sequence
                                    		  automatically inserts a Forced Pause into the sequence after the address of a
                                    		  server is changed.

The
                                    		  forced pause allows you to perform manual steps, such as updating DNS entries
                                    		  and server entries on the Unified Communications publisher node interface
                                    		  ( System > Server ).
                                    		  It also allows you to check the phones associated with the server successfully
                                    		  registered. User needs to perform these steps before resuming the readdress
                                    		  task in the interface for other Unified Communications nodes as well. After the
                                    		  readdress task resumes, the system replicates the updates successfully.

For more information, see Administration Guide for Cisco Unified Communications
                                       			 Manager .

##### Before you begin

Important

Before running a
                                                			 readdress task, you may need to perform certain steps (for example, updating
                                                			 entries on the DNS server).

It is very important that
                                                			 you read Administration Guide for Cisco Unified Communications
                                                   				Manager before you run the readdress task.

#### Post Readdress Task

When you determine that the server successfully changed the address, go to the Cisco Prime Collaboration Deployment GUI and
                                 click Resume to resume the task.

The Cisco Prime Collaboration Deployment server proceeds to the next server in the sequence to be readdressed. Repeat the
                                 steps of waiting for the forced pause, checking the server state, and resuming the task, when the server readdress is verified.

### Install
                           	 Task

#### Create an Install Task

Step 1

VMware—Deploy the hardware for the new cluster and install ESXi.

Make sure that the host with the Cisco Prime Collaboration Deployment VM and the host with the application VMs use the required
                                                            Virtualization Software License. See Add an ESXi Host Server .

Step 2

ISO files—Download the necessary OVA and ISO images for target release, and use SFTP transfer the ISO files to the /fresh_install directory of Cisco Prime Collaboration Deployment.

Do not edit the file name of the bootable ISO that is being used for a PCD task.

Step 3

VMware—Deploy Cisco-recommended OVA to create the VMs for the nodes to be installed. Create the appropriate number of target
                                             virtual machines on your ESXi hosts (one new virtual machine for each server to be installed in the cluster) using the Cisco
                                             OVAs that you downloaded in Step 2. Configure the network settings on new VMs.

Step 4

Cisco Prime Collaboration Deployment GUI—Add the ESXi Hosts that contain your virtual machines to the Cisco Prime Collaboration
                                             Deployment inventory. For information about adding and ESXi host to Cisco Prime Collaboration Deployment, see Add an ESXi Host Server .

Step 5

Cisco Prime Collaboration Deployment GUI—Define the new installation cluster (click the open and close navigation button and
                                             choose Inventory > Clusters ) to define the nodes to be installed, and their associated virtual machines. (See Add New Cluster for Fresh Install .)

Step 6

Cisco Prime Collaboration Deployment GUI—Setup Email Notification (Optional).

Click the open and close navigation button and choose Administration > Email Notification .

When email notification is set up, the Cisco Prime Collaboration Deployment server emails the error conditions that may occur
                                                      during the migration task.

Step 7

Cisco Prime Collaboration Deployment GUI—Create the Install task.

Step 8

Be sure to enter the IP addresses or hostnames of the cluster nodes to be installed into your DNS server before you create
                                             the install task.

#### Add Install
                              	 Task

Follow this
                                    		  procedure to automatically install one or more nodes in a cluster at scheduled
                                    		  times.

Step 1

Click the open and close navigation button and choose Task > Install from the main menu.

Step 2

Click Add
                                                				Install Task .

If you have no Install tasks, a Cluster Installation pop-up window appears with the prerequisites to run the wizard. Click Close to close the pop-up window.

Step 3

In the Specify Task Name drop-down, enter a name for the install task in Choose a Nickname for this Install Task .

Step 4

From the Installation Cluster drop-down list, select the
                                             			 cluster on which the nodes to be installation are located.

If you want to apply an upgrade patch along with the installation, click Yes radio button otherwise click No radio button.

Step 5

Click Next .

Step 6

Click the respective Browse buttons to select the Unified Communications Manager Installation file and the Cisco Unified Presence Installation file from
                                             the server.

If you have applied upgrade patch along with the installation, browse the patch files along with the installation files for
                                                Unified Communications Manager and the Cisco Unified Presence.

You must select the patch file of same Engineering Special (ES)/ Service Update (SU) versions of the installation file.

Important

The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. For more information, see the task management information at the beginning of
                                                            this section.

By default, only files that can be installed on the selected nodes are displayed. The option to select install files is available
                                                            only for the selected product types and applications that are currently supported in the cluster.

When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different.

Step 7

Click Choose
                                                				File .

Step 8

Click Next .

The Next button is dimmed if no valid upgrade files are
                                                            				  selected.

Step 9

Select the
                                             			 date and time when you want the upgrade task to begin. You have the following
                                             			 options to schedule upgrades:

If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically.

- Select Start task manually to keep the task in a manual
                                                				start.

You can also start the task from the Monitoring page.

Step 10

Click Next .

Step 11

Specify the
                                             			 sequence of steps to complete the task. You have the following options:

Edit a
                                                         					 step.

Add a new
                                                         					 step after the current step.

Delete the
                                                         					 current step.

If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node.

Move the
                                                         					 step up to be performed earlier.

Move the
                                                         					 step down to be performed later.

- The Pencil icon opens up an Edit Step window. Add nodes to be installed in this
                                                				step from the list of available nodes. The available nodes are the ones that
                                                				you chose to install in this cluster.

- The step to which each node
                                                				is assigned displays next to the node. If a node is not assigned to any step,
                                                				it shows as unassigned.

When you assign all the nodes to a step, a default sequencing is available.

Important

- If you are installing
                                                				Cisco Unified Communications Manager between Releases 10.0(1) and 10.5(1), the
                                                				task is paused after publisher node is installed completely. You must enter
                                                				details of subscriber nodes into the publisher node before you manually start
                                                				the next step. Cisco Unified Communications Manager Release 10.5(2) onward does
                                                				not pause during a fresh installation; the install task continues
                                                				automatically.

Step 12

Click OK .

Step 13

Click Next .

Step 14

See the Review section to verify the details of the task you created. You can add notes for the task if necessary. The notes are saved with
                                             the task and are visible if the task is edited before completion.

Step 15

Click Finish to schedule the install task.

#### Run an Install Task

If you scheduled a task to start at a later date or if you chose Manual Start, the task is listed in the Task list, but has
                                    not started yet. In this case, a validation button is associated with the install task. Click Validation to check the task before you run it. By running validation before you start the task, you are alerted to any potential problems
                                    with the task (such as a missing ISO file or VMs not in the Off state). You can then fix these issues before you start the
                                    task.

For a task that was scheduled for manual start, click the Start button that is associated with this task to begin the task.

#### Cancel Install
                              	 Task

Use this procedure
                                    		  to cancel a fresh install task or an existing installation in a migration task.

Step 1

From the Cisco Prime Collaboration Deployment application, click
                                             			 the open and close navigation button and choose Task > Install from the main menu.

Step 2

Select an
                                             			 existing install task and click Cancel .

If you
                                                            				  cancel the currently running install task, you will have to delete the virtual
                                                            				  machine and then recreate it.

#### Post-Install Task

After the install task, no further actions are required. The new cluster is ready for use.

### Monitor Task
                           	 Status

Use the Monitoring
                                 		  page to view the status of tasks in Cisco Prime Collaboration Deployment.

Step 1

Click the Monitoring link on the main menu to view the Monitoring page.

Step 2

The column on
                                          			 the left side of the Monitoring page lists each task and an icon that shows its
                                          			 current status. Also shown is the type of task (Migrate, Upgrade, Install,
                                          			 and so on), and the cluster nickname for the task.

The task start
                                             				time is also shown. Click the task in this
                                             				left column to view the detailed data for that task in the panel on the right.

Step 3

The upper
                                          			 right section of the page provides the following data:

- Status

- Start time

- Task data (for example:
                                             				cluster nickname and ISO name)

Click View Log to see the detailed log messages for the task. If you see any errors or
                                             				warnings in this log, refer to the Troubleshooting section more information.

In the upper
                                             				right are buttons that you use to perform various operations on the task.
                                             				For example, if the task is paused, click the Resume button to resume the task.

A button will
                                             				appear if it is valid for the current state of the task. For example, after a
                                             				task is finished, it will not have a Cancel button, but instead will have a
                                             				Delete button (if you wish to remove the data for the task).

Step 4

The bottom
                                          			 right section of the page provides detailed steps for the task, along with the
                                          			 status for that step. Click on the triangle that corresponds to a step to
                                          			 expand the step description.

Each step also
                                             				has a View Log link, to show the log messages for that step.

#### Action Buttons on the Monitoring Page

Start —This button appears if a task is created with the "Start Task Manually" option. The task starts after you click the Start button.

Cancel —Cancel the task. This button appears when a task is in the scheduled or running state. If the task has already started, this
                                          button does not undo any steps that are already complete, but it will stop the task as soon as possible.

Delete —Delete the task from the system. This removes the task and all its history.

Resume —This button appears when a task is in a paused state. It allows the user to resume the task at the next step or sub-step.

Retry —This button appears when the task is in a "Paused due to error" state. Clicking this button retries the last step of the task (the failed next step or sub-step) that failed because of an
                                          error.

#### Automatic Refresh

The Monitoring page refreshes automatically every 6 minutes. To deactivate automatic refresh, click the Disable button in the top left corner of the Monitoring page.

## Administration
                        	 Tools

### Email
                           	 Notification

The Email Notification feature sends email notifications to you that contain details about certain task events. You can choose
                                 whether the system sends emails for all standard task events (such as when task is scheduled, started, successful, paused,
                                 failed and canceled), or for only task errors. Emails are sent for all types of tasks—Cluster discovery, upgrade, migration,
                                 switch version, restart, fresh install, and readdress.

You can choose to send
                                 		  an email notification to a user after the value that is configured in the Warning Threshold for Approaching Log Rotation
                                    			 Overwrite(%) field from the Audit Log Configuration window is reached. The
                                 		  email notification informs the user to take back up of the audit log files
                                 		  because they will be deleted or overwritten.

#### When Email Is
                              	 Sent

If you choose to receive email notifications in Standard mode ,
                                 		an email message is sent when a task enters any of the following states:

Scheduled

Failed to Schedule

Started

Successful

Failed

Canceled

Canceling

Failed to Cancel

Paused on Error

Paused

Paused – Required

If you choose to receive email notifications in Error only
                                    		  mode , an email message is sent when the task enters the following states:

Failed to Schedule

Failed

Failed to Cancel

Paused on Error

If PCD task of X steps, operating on 1 to N nodes the task action you get, email notifications when each node/task step is
                                 completed

Migration Task:

Task Scheduled for Cluster

Task Started for Cluster

Source Node(s) A Configuration export success

Source Node(s) B Configuration export success

Destination Node(s) A Install success

Destination Node(s) B Install success

Source Node(s) A UFF Export success

Source Node(s) A shut down success

Destination Node(s) A UFF Import success

Source Node(s) B UFF Export success

Source Node(s) B shut down success

Destination Node(s) B UFF Import success

Task Completed/Failed

Upgrade Task (COPs):

Task Scheduled for Cluster

Task Started for Cluster

COPs x installed on node a

COPs y installed on node b

Task Completed/Failed

PCD Fresh Install Task or Upgrade Task (ISO):

Task Scheduled for Cluster

Task Started for Cluster

Node(s) A has been complete

Node(s) B has been complete

Task Completed/Failed

PCD Restart Task:

Task Scheduled for these nodes

Task Started for these nodes

Node(s) A has been restarted

Node(s) B has been restarted

Task Completed/Failed

PCD Switch Version Task:

Task Scheduled for these nodes

Task Started for these nodes

Node(s) A has been switched

Node(s) B has been switched

Task Completed/Failed

PCD Readdress:

Task Scheduled for these nodes

Task Started for these nodes

Node(s) A has been readdressed

Node(s) B has been readdressed

Task Completed/Failed

### SFTP
                           	 Datastore

The Cisco Prime
                                 		  Collaboration Deployment server serves as a local SSH File Transfer Protocol or
                                 		  Secure File Transfer Protocol (SFTP) server that is used to store the ISO and
                                 		  COP files to be used by upgrade, fresh install, and migrate tasks.

#### Migration or Fresh
                              	 Install Tasks

Follow this procedure to send the ISO file to the Cisco Prime Collaboration Deployment
                                    		  server using the adminsftp account and Cisco Prime Collaboration Deployment GUI
                                    		  (or CLI password with any SFTP client).

Step 1

From a Linux
                                             			 shell, type sftp
                                                				adminsftp@<Cisco Prime Collaboration Deployment server> and then
                                             			 provide the password (the same in both the CLI and GUI).

Step 2

Change the
                                             			 directory to the fresh_install directory.

##### Example:

From a Linux shell, type cd fresh_install and press Return .

Step 3

Upload the
                                             			 ISO file.

##### Example:

Type put UCSInstall_UCOS_10.0.x.xxx.sgn.iso .

#### Upgrade
                              	 Task

Follow this procedure to use SFTP to upload ISO or COP files that will be used for upgrade tasks on the
                                    		  Cisco Prime Collaboration Deployment server.

Step 1

From a Linux
                                             			 shell, type sftp
                                                				adminsftp@<Cisco Prime Collaboration Deployment server> and then
                                             			 provide the password (the same in both the CLI and GUI).

Step 2

Change the
                                             			 directory to the upgrade directory.

##### Example:

From a Linux shell, type cd upgrade and press Return .

Step 3

Upload the
                                             			 ISO file or COP file.

##### Example:

#### Verify or View an
                              	 ISO Filename

Step 1

From the Cisco Prime Collaboration Deployment application, click open and close navigation and choose Inventory > SFTP Servers and Datastore .

Step 2

On this page,
                                             			 you can view and manage files that are stored on the SFTP datastore of this
                                             			 Cisco Prime Collaboration Deployment server.

#### Delete ISO or COP
                              	 Files

Use the following
                                    		  procedure to delete ISO or COP files on a Cisco Prime Collaboration Deployment
                                    		  SFTP server using the Cisco Prime Collaboration Deployment GUI.

Step 1

Log in to
                                             			 Cisco Prime Collaboration Deployment.

Step 2

From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Inventory > SFTP Servers and Datastore .

Step 3

Check the
                                             			 check box next to the ISO or COP file.

Step 4

Click Delete .

Important

We
                                                               					 recommend that you periodically delete ISO or COP files that are no longer
                                                               					 needed to save space, especially before upgrading the Cisco Prime Collaboration
                                                               					 Deployment server software.

### Remote SFTP Server
                           	 Support

The remote SFTP server support feature leverages Cisco Prime Collaboration Deployment for upgrades , migrations, and fresh installs . Use of this feature avoids the issues that are caused by large application image files streamed over WAN that are only supported
                              by Cisco Prime Collaboration Deployment 12.1(1) and later.

Examples of where this feature is useful are listed as follows:

Geographically distributed deployments, such as multi-site distributed IP Telephony with multiple clusters at separate sites
                                    from the Cisco Prime Collaboration Deployment virtual machine.

Clustering over WAN (CoW), where the application virtual machines are at different sites than the Cisco Prime Collaboration
                                    Deployment virtual machine.

Deployments where Cisco Prime Collaboration Deployment is in a central data center; however Cisco Unified Communications Manager clusters are remote over the WAN.

These SFTP servers used for the upgrade of Cisco Unified Communications Manager are same as the SFTP servers that are used for the upgrade of Cisco Unified Communications Manager . Following is the list of the supported SFTP servers that are used for upgrade:

Open SSH

Cygwin

Titan

Refer to the following table for a summary of the SFTP server options:

SFTP Server

Support Description

SFTP Server from a Technology Partner

These servers are third party provided and third party tested. Version compatibility depends on the third-party test. Refer
                                          to the Technology Partner page if you upgrade their SFTP product and/or upgrade Unified Communications Manager.

SFTP Server from another Third Party

These servers are third party provided and are not officially supported by Cisco TAC.

Version compatibility is on a best effort basis to establish compatible SFTP versions and Emergency Responder versions.

The remote SFTP server support is available for upgrade, migration, and fresh install tasks.

Cisco Prime Collaboration Deployment does not support Windows server while adding it as an external SFTP server for installation or migration tasks. Only Unix
                                          and Linux-style path formats are supported.

#### Add Remote SFTP Server

##### Before you begin

For Migration/Fresh install, mount the NFS on the ESXi host(s) where the destination VM's are created for the specific fresh
                                    install/Migration tasks.

Due to the limitation on PCD to store the huge lists of ESXi hosts where the remote SFTP server is mounted as NFS datastore,
                                                make sure to remove the unused remote SFTP server which is mounted as NFS from the ESXi hosts added in PCD.

Step 1

From the Cisco Prime Collaboration Deployment application,
                                             			 click the open and close navigation button and choose Inventory > SFTP Servers
                                                   				  and Datastore .

Step 2

From the SFTP Servers/Datastore table, click Add Server .

Step 3

Click Install/Migration or Upgrade radio button.

Step 4

In the Address and access credentials section, enter values
                                             			 in the IP /
                                                				Host Name , Username , and Password fields.

Step 5

For Install or Migration task type, in the Remote NFS Path to Datastore Directory on Server section, enter the directory path in Directory field and NFS server name in NFS Server Name field.

Feild

Description

Directory

Path which has been configured for NFS storage in ESXI host.

NFS Server Name

Name of NFS storage which has been created in ESXI.

Example:

Directory: /abc/def/

NFS Server Name: xyz_NFS

When adding an NFS server, the SFTP credentials should point to a directory that is an exact match for the path which is configured
                                                in the ESXi host. For more information on adding NFS storage in ESXi host refer the respective documentation guide.

Step 6

For Upgrade task type, in the Remote SFTP Path to Datastore Directory on Server , click an Add Directory button to add a value in the Directory field.

For an upgrade, ensure that a directory includes .iso datastore files.

Step 7

(Optional) In
                                             			 the Additional Information section, enter description in
                                             			 the Description field.

Step 8

Click Add .

Upon the successful add of remote SFTP server for the install or migration task type, a dialog box is displayed. Dialog box
                                                lists the ESXi hosts which are already added to Prime Collaboration Deployment under Inventory > ESXi Hosts that has the given NFS directory mounted.

If the SFTP server is not added, you get any of the following error messages:

Connection Timeout —Indicates that the connection to SFTP server failed due to timeout.

Login Failure —Indicates that the login to the SFTP server failed.

Directory Not Found —Indicates that the directory that you selected is not found on the SFTP server.

Directory Already Entered —Indicates that the directory that you selected already exists in the list of directories. You can view the list of available
                                                                  directories by clicking the Add Directory button.

Directory Already Exists —Indicates that the directory that you entered already exists in the list of the SFTP servers.

Mandatory Fields Missed —Indicates that you did not enter values in the mandatory fields.

Mentioned Server Could Not Be Located —Indicates that the server that you entered is not configured with DNS. This error message appears if you enter host name
                                                                  instead of IP address.

No ESXi Hosts in Inventory —Indicates that you have not added ESXi hosts. This error appears when you try to add Install or Migration task type remote
                                                                  SFTP, and the given NFS mount is not found as there are no ESXi hosts added under Inventory > ESXi Hosts page.

Could not find given NFS path/Directory on the listed ESXi host(s) under Inventory > ESXi Hosts —This error appears when you try to add Install or Migration task type remote SFTP, and the given NFS directory is not found
                                                                  in any of the ESXi which are added under Inventory > ESXi Hosts page.

#### Associate Nodes to
                              	 Remote SFTP Server

##### Before you begin

Add an SFTP
                                          				server.

Ensure that
                                          				the cluster node you choose to associate to an SFTP server is not in the Scheduled , Running , or Wait_for_manual_start states.

Step 1

From the Cisco Prime Collaboration Deployment application,
                                             			 click the open and close navigation button and choose Inventory > Clusters .

Step 2

Click Discover Cluster button to search for the existing
                                             			 clusters. To discover a cluster, see the Discover a Cluster procedure.

Step 3

From the
                                             			 available cluster nodes in the Cluster Nodes table, click Edit for a cluster node.

Step 4

From the SFTP
                                                				Server drop-down list, choose an SFTP server.

By default,
                                                				this field shows the localhost option as the SFTP Server.

Step 5

Click OK .

#### Edit Remote SFTP
                              	 Server

For the existing
                                    		  remote SFTP server, you can edit the details, such as username, password, or
                                    		  description. You can also add multiple directories to the remote SFTP server
                                    		  while editing other field values.

##### Before you begin

Ensure that a
                                             				cluser node is not associated with remote SFTP server directory that you choose
                                             				to edit.

Ensure that no install, migration or upgrade  task is associated with the SFTP server.

Step 1

From the Cisco Prime Collaboration Deployment application, click
                                             			 the open and close navigation button and choose Inventory > SFTP Servers
                                                   				  and Datastore .

Step 2

From the available SFTP servers in the SFTP and NFS File access table, click Edit for an SFTP server.

Step 3

For Install or Migration tasks, edit the values for the fields in the Address and access credentials , Remote NFS Path to Datastore Directory on Server , NFS Server Name , and Additional Information sections.

Step 4

For Upgrade task, edit the values for the fields in the Address and access credentials , Remote SFTP Path to Datastore Directory on Server , and Additional Information sections.

In Remote SFTP Path to Datastore Directory on Server section, by clicking the Add Directory button, you can edit an existing directory and also add multiple directories.

Step 5

Click Save .

#### Delete Remote SFTP
                              	 Server

You can delete
                                    		  one or multiple remote SFTP servers that are available in the Cisco
                                       			 Prime Collaboration Deployment application. However, you cannot
                                    		  delete any datastore.

##### Before you begin

Ensure that no install, migration or upgrade tasks are associated and running with the cluster node that uses the SFTP server that you choose to delete.

Disassociate the cluster nodes from the SFTP server that you choose to delete.

You can disassociate a cluster node even if no install, migration or upgrade tasks are associated and running with the cluster node that uses the SFTP server that you selected to delete.

Ensure to change the node association of the SFTP server, which you choose to delete, from remote/external SFTP server to the localhost SFTP server.

If you do not change the node association from remote/external SFTP server to the localhost SFTP server, the association of cluster nodes changes to the localhost SFTP server from the remote SFTP server and the remote SFTP server that you selected is deleted.

Step 1

From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Inventory > SFTP Servers and Datastore .

Step 2

From the
                                             			 available SFTP servers in the SFTP
                                                				Servers/Datastore table, check the check box of one or multiple
                                             			 remote SFTP servers that you want to delete.

Step 3

Click Delete .

#### Delete Local
                              	 SFTP/Datastore ISO files

You can delete
                                    		  ISO and COP files from the SFTP server running locally in the Cisco Prime
                                    		  Collaboration Deployment virtual machine. However, you cannot delete ISO files
                                    		  from the remote SFTP server.

##### Before you begin

Ensure that the
                                    		  SFTP and datastore ISO files that you choose to delete are not associated with
                                    		  the upgrade in these states— Scheduled , Running , or Wait_for_manual_start .

Step 1

From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Inventory > SFTP Servers and Datastore .

Step 2

From the
                                             			 available SFTP and datastore files in the SFTP/Datastore Files table, check the check box of
                                             			 one or multiple remote SFTP and datastore files that you want to delete.

You cannot
                                                            				  delete remote SFTP files.

Step 3

Click Delete .

### Disk Space Warning
                           	 Level

Use this feature
                                 		  to view and configure a disk space warning level for tasks through the Disk
                                    			 Space Warning Level Configuration window. When the available disk
                                 		  space value drops below the value that you assign as the warning level disk
                                 		  space, the system warns you that it is running out of disk space to perform
                                 		  tasks.

#### Configure Disk
                              	 Space Warning Level

Use this procedure
                                    		  to configure the available disk space threshold where the system warns you that
                                    		  it is running out of disk space to perform tasks.

Step 1

From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Administration > Disk Space Warning Level .

Step 2

View the total
                                             			 disk space and the available disk space in the Total
                                                				Disk Space (GB) and Available Disk Space (GB) fields.

Step 3

Enter the
                                             			 value that you want to assign for the Warning Level Disk Space (GB) field.

You can click
                                                				the information link to check if the space value you entered is available for
                                                				use on the server.

Step 4

Click Save .

Step 5

(Optional) Click Reset .

### Max Nodes Configuration

This feature is to configure the maximum nodes across all running tasks (Cluster Discovery, Install Task, Migrate Task, Upgrade
                                 Task, Switch Version Task, Server Restart Task, and Readdress Task) count as configurable value so PCD completes the task
                                 quickly.

#### Configure Max Nodes

Use this procedure to configure max nodes through the Cisco Prime Collaboration Deployment application.

Step 1

From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Administration > Max Nodes Configuration .

Step 2

Enter a value in the Max Nodes field.

Maximum nodes count loads with the default value 30. You can enter maximum 1–200 nodes.

Step 3

Click Save .

Step 4

Restart the Cisco Tomcat server to reflect change.

Step 5

Optional: Click Reset . The page is reset with the default values.

When the maximum nodes count exceeds the maximum defined limit for tasks (Cluster Discovery, Install Task, Migrate Task, Upgrade
                                                            Task, Switch Version Task, Server Restart Task, and Readdress Task), the following error message is displayed:

### Audit Log
                           	 Configuration

Configure application audit event levels

Configure remote Syslog server name or IP address

Enable or disable audit logs

Enable or disable log rotation

Configure maximum number of files

Configure file size

Configure warning threshold level for log rotation

#### Configure Audit
                              	 Logs

Use this procedure to configure audit logs for local and remote syslog
                                    		  server through the Cisco Prime Collaboration Deployment application.

Step 1

From the Cisco Prime Collaboration Deployment application, click open and close navigation and choose Administration > Audit Log Configuration .

Step 2

Choose one of the options from the Application Audit Event Level drop down list
                                             			 to configure an audit level.

Step 3

Enter the name of remote syslog server or the IP address for the Remote Syslog Server Name / IP field so that
                                             			 the audit logs are logged into this remote server.

Step 4

(Optional) Check or uncheck the Enable Local Audit Log check box to enable or
                                             			 disable the local audit log.

When you check this field, the audit events are logged in the local server. When you uncheck this field, audit events are
                                                      not logged in the local server. The audit events includes User ID, ClientAddress, Severity, EventType, ResourceAccessed, EventuStatus
                                                      , AuditCategory, CompulsoryEvent, ComponentID, CorrelationID and Node ID.

When you check this field, the Enable Log Rotation field becomes
                                                      					 active.

Step 5

(Optional) Check or uncheck the Enable Log Rotation check box to enable or
                                             			 disable the log rotation.

You can configure this field if Enable Local Audit Log is enabled.

Step 6

Enter an integer value for the Maximum No of Files field to configure the
                                             			 maximum number of files that can be created on the server.

Step 7

Enter a value for the Maximum File Size (MB) field to configure the
                                             			 maximum file size of each log that is created on the server.

Step 8

Enter the warning threshold value for the Warning Threshold for Approaching Log Rotation
                                                				Overwrite(%) field.

Step 9

Click Save .

Step 10

(Optional) Click Reset .

### Customized Logon
                           	 Message

Upload a file with customized login message

Enable user acknowledgment

#### Configure
                              	 Customized Logon Message

Use this procedure to configure customized logon messages when a user
                                    		  signs into the Cisco Prime Collaboration Deployment application.

Step 1

From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Administration > Customized Logon Message .

Step 2

For the Upload File field, browse to the location of
                                             			 file that includes the customized logon message.

Step 3

(Optional) Check or uncheck the Require User Acknowledgement check box to
                                             			 enable or disable user acknowledgment for the file that the user receives.

Step 4

Click Upload File .

Step 5

(Optional) Click Delete .

## FIPS 140-2
                        	 Compliance

FIPS, or Federal
                              		  Information Processing Standard, is a U.S. and Canadian government
                              		  certification standard that defines requirements that cryptographic modules
                              		  must follow. A cryptographic module is a set of hardware, software, and/or
                              		  firmware that implements approved security functions (including cryptographic
                              		  algorithms and key generation) and is contained within the cryptographic
                              		  boundary.

Certain versions
                              		  of Unified Communications Manager are FIPS 140-2 compliant, in accordance with
                              		  the U.S. National Institute of Standards (NIST), and can operate in FIPS mode,
                              		  level 1 compliance. Cisco Prime Collaboration Deployment meets FIPS 140-2
                              		  requirements by using Cisco-verified libraries.

For information
                              		  about which releases are FIPS-compliant and to view their certifications, see http://www.cisco.com/c/en/us/solutions/industries/government/global-government-certifications/fips-140.html .

For details on
                              		  EnhancedSecurityMode, see EnhancedSecurityMode Support .

Elliptic Curve Digital Signature Algorithm (ECDSA) ciphers are not supported in Cisco Prime Collaboration Deployment. Hence,
                                                during TLS connection, the server does not negotiate the ECDSA certificates even though the show cert list own CLI command may show the ECDSA self-signed certificate.

All the nodes of a cluster should either be FIPS or non-FIPS.

## EnhancedSecurityMode Support

Once you enable EnhancedSecurityMode, the following system enhancements are enabled by default:

Stricter credential policy is implemented for user passwords and password changes

TCP becomes the default protocol for remote audit logging

FIPS mode is enabled

Enabling
                              		  EnhancedSecurityMode does not enable these features by default and you have to
                              		  configure them separately.

Remote audit
                                    				logging—All audit logs and event syslogs should be saved both locally and to a
                                    				remote syslog server.

System
                                    				logging—All system events such as CLI logins and incorrect password attempts
                                    				must be logged and saved.

If you configure UC clusters on FIPS mode or EnhancedSecurityMode, ensure that you also configure Cisco Prime Collaboration
                                          Deployment with the similar modes. With this configuration, you can run the tasks that are specific to UC clusters.

## Credential Policy
                        	 for EnhancedSecurityMode

Password
                                       				length should be between 14 to 127 characters.

Password
                                       				should have at least 1 lowercase, 1 uppercase, 1 digit and 1 special character.

Any of the
                                       				previous 24 passwords cannot be reused.

Minimum age
                                       				of the password is 1 day and Maximum age of the password is 60 days.

Any newly
                                       				generated password's character sequence should differ by at least 4 characters
                                       				from the old password's character sequence.

Once this mode is
                              		  enabled, the system enforces a stricter credential policy for all password
                              		  changes automatically.

## EnhancedSecurityMode Requirements for Platform Cisco Prime
                        	 Collaboration Deployment

As part of
                              		  EnhancedSecurityMode requirement, audit framework is introduced in Cisco Prime
                              		  Collaboration Deployment. The audit framework includes audit activities, which
                              		  are both in local server and remote server. The login sessions are limited for
                              		  each user based on the CLI command configuration in the EnhancedSecurityMode.

By default,
                                          			 auditing is not enabled in Cisco Prime Collaboration Deployment. If you wish to
                                          			 have audit logs, you can enable auditing with or without being in FIPS mode or
                                          			 EnhancedSecurityMode.

## Re-encryption
                        	 through AES

The encryption and decryption of application passwords is done in the platformConfig.xml file. During installation, the
                              		  application password is re-encrypted through the Advanced Encryption Standard
                              		  (AES) algorithm and is saved in the platformConfig.xml file.

## Supported Ciphers for PCD

The following table lists the application interfaces and the all corresponding ciphers and algorithms that are supported on
                           PCD:

Application / Process

Protocol

Port

Supported Ciphers

Cisco Tomcat PCD as a Server

TCP / TLS

8443 / 443

```
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-RSA-AES128-GCM-SHA256
AES256-SHA
AES128-SHA
DHE-RSA-AES128-SHA
```

Cisco Tomcat PCD as a Client

TCP / TLS

8443 / 443

```
TLS_AES_256_GCM_SHA384
TLS_AES_128_GCM_SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-ECDSA-AES256-GCM-SHA384
ECDHE-RSA-AES128-GCM-SHA256
ECDHE-ECDSA-AES128-GCM-SHA256
ECDHE-RSA-AES256-SHA384
ECDHE-ECDSA-AES256-SHA384
ECDHE-RSA-AES128-SHA256
ECDHE-ECDSA-AES128-SHA256
ECDHE-RSA-AES256-SHA
ECDHE-ECDSA-AES256-SHA
ECDHE-RSA-AES128-SHA
ECDHE-ECDSA-AES128-SHA
AES256-GCM-SHA384
AES128-GCM-SHA256
AES256-SHA
AES128-SHA
```

Service

Ciphers/Algorithms

SSH Server

Ciphers

```
aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com
```

MAC algorithms:

```
hmac-sha2-256
hmac-sha2-512
hmac-sha1
```

Kex algorithms:

```
ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha1
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512
```

Host Key algorithms:

```
rsa-sha2-256
rsa-sha2-512
ssh-rsa
```

SSH Client

Ciphers:

```
aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com
```

MAC algorithms:

```
hmac-sha2-256
hmac-sha2-512
hmac-sha1
```

Kex algorithms:

```
ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha1
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512
```

Host Key algorithms:

```
rsa-sha2-256
rsa-sha2-512
ssh-rsa
```

DRS Client

Ciphers:

```
aes256-ctr
aes128-ctr
```

MAC algorithms:

```
hmac-sha2-256
hmac-sha1
hmac-md5
hmac-sha1-96
hmac-md5-96
```

```
ecdh-sha2-nistp256
ecdh-sha2-nistp384
ecdh-sha2-nistp521
diffie-hellman-group14-sha256
diffie-hellman-group14-sha1
diffie-hellman-group-exchange-sha1
diffie-hellman-group1-sha1
```

Host Key algorithms in non-FIPS mode:

```
ssh-rsa
ecdsa-sha2-nistp256
ecdsa-sha2-nistp384
ecdsa-sha2-nistp521
```

Host Key algorithms in FIPS mode:

```
rsa-sha2-256
```

## Limited Number of
                        	 Sign-in Sessions

An administrator can configure the sign-in session limit for each
                              		  user. A user can sign in to the Cisco Prime Collaboration Deployment
                              		  application through multiple windows and web browsers up to the configured
                              		  number of sign-in sessions. If a user exceeds the limit of configured the
                              		  number of sign-in sessions, an error message appears on the sign-in page and
                              		  the user is not allowed to sign in.

An administrator can configure the limit of sign-in sessions through
                              		  the following CLI command:

set session maxlimit <value>

Where the default value is 10 and maximum value is 100.

When users exceed the limit of configured number of sign-in
                                          			 sessions, they must sign out from the application in that session and sign in
                                          			 to another session. In case the session closes due to abrupt exit from web
                                          			 browser, users need to restart the Tomcat server on Cisco Prime Collaboration
                                          			 Deployment to allow sign-in to the new session.

## Minimum TLS Version Control

This release of Cisco Prime Collaboration Deployment includes the minimum Transport Layer Security (TLS) protocol version
                              configuration support. Use this feature to configure the minimum TLS version to comply with the organization security policies.

The supported TLS versions are TLS 1.0, 1.1, 1.2, 1.3 . By default, TLS 1.0 is the default minimum TLS version for all UC products. After you configure the minimum TLS version,
                              both the minimum version and the higher versions are supported.

Before you configure the minimum TLS version, ensure that the following products support secure connection of the selected
                              minimum TLS version configured or above. If this requirement is not met, upgrade the product to a version that supports the
                              interoperability for selected minimum TLS version configured or above when you configure the minimum TLS version.

Cisco Unified Communications Manager

IM and Presence Service

Cisco Unity Connection

Cisco Unified Contact Center Express

Cisco Emergency Responder

To configure the minimum TLS version, see the CLI Commands for TLS Minimum Version Configuration topic.

## Configurable Maximum Install Timeout for Clusters

With this release, you can configure the maximum timeout value during the migration of nodes of a cluster. In the previous
                              releases, the default timeout value from Cisco Prime Collaboration Deployment was 5 hours for both install and migration tasks.
                              This restriction prevented the nodes that have large data to import during migration to time out from Cisco Prime Collaboration
                              Deployment side.

You can configure the maximum timeout value from the Max Timeout for Install drop-down list on the Configure Destination Cluster window. Click Inventory > Clusters to access the Configure Destination Cluster window. When you configure a migration destination cluster, you can choose the maximum timeout value for Max Timeout for Install from 5 hours up to 10 hours.

For Install task, Cisco Prime Collaboration Deployment has the default timeout value as 5 hours, which is non-configurable.

| Step | Tasks |
|---|---|
| Step 1: Inventory Creation | To perform any tasks, you must first have clusters in your inventory. To add a UC cluster that is already running UC applications
                                          to your inventory, click Open and close navigation and choose Inventory > Clusters > Discovery Cluster feature. To migrate an existing cluster to new virtual machines, click Open and close navigation and choose Inventory > Clusters > Define Migration Destination Cluster . (See Migration Task .) To install a new cluster, click Open and close navigation and choose Inventory > Clusters > Define New UC Cluster feature. (See Create an Install Task .) If you are migrating an existing cluster to a new virtual machine cluster, or installing a new cluster, you must first add
                                          the ESXi Hosts that contain those virtual machines to your inventory. To add an ESXi host, click Open and close navigation and choose Inventory > ESXi Hosts . (See Add an ESXi Host Server .) |
| Step 2: Create a Task | You can create a task to perform an operation on a cluster in your inventory. During task creation, options allow you to: Choose the cluster Note This task depends on the type of cluster you require. For example, you may choose a discovered cluster or a migration cluster. Determine when to run the task Determine if the task should run independently or pause between steps To perform one of the following actions, select from these procedures: To migrate from an existing cluster to a new cluster of VM machines, see Migration Task . To upgrade the Unified Communications Manager version of an existing cluster, see Upgrade Task . To switch the version of an existing cluster, see Switch Versions Task . To restart an existing cluster, see Server Restart Task . To change the hostname or IP address of one or more servers in an existing cluster, see Readdress Task . To create a new UC cluster from VM machines, see Create an Install Task . | Note | This task depends on the type of cluster you require. For example, you may choose a discovered cluster or a migration cluster. |
| Note | This task depends on the type of cluster you require. For example, you may choose a discovered cluster or a migration cluster. |
| Step 3: Monitor Tasks | After a task is created, you can use the Monitoring window to view or track any task. You can also use this page to cancel,
                                          pause, or resume tasks. To view the tasks you created, see Monitor Task Status . |
| Step 4: Administrative Tasks | You can set up email notification. See Email Notification . |

| Note | This task depends on the type of cluster you require. For example, you may choose a discovered cluster or a migration cluster. |
|---|---|

| Note | When Cisco Prime
                                          			 Collaboration Deployment is behind the NAT and application nodes are in a
                                          			 private network, the application nodes communicate with the NAT IP address. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Administration > NAT Settings . The NAT Settings window appears and is prepopulated with the hostname and the private IP address. |
|---|---|
| Step 2 | Enter the NAT
                                       			 IP address in the NAT
                                          				IP field. |
| Step 3 | Click Save . The NAT
                                       			 IP address is saved as an entry in a configuration file on Cisco Prime
                                       			 Collaboration Deployment. This entry is used when the application nodes try to
                                       			 contact Cisco Prime Collaboration Deployment, then the application nodes read
                                       			 the configuration file to get the NAT IP address, and then try to communicate
                                       			 Cisco Prime Collaboration Deployment with that IP address. |
| Step 4 | (Optional) Click Reset . The
                                       			 NAT IP address is reset to the earlier saved NAT IP address. |

| Note | If you're using Cisco Prime Collaboration Deployment to upgrade an IM and Presence Service cluster from Release 12.5.x to
                                       Release 15, you must install the following COP file on the Release 12.5.x systems before you begin the upgrade: ciscocm.imp15_upgrade_v1.0.k4.cop.sha512.
                                       Note that the COP file is applicable only if: Unified Communications Manager destination version is in Release 15. Unified Communications Manager destination version is in Release 15 and you are trying to upgrade your IM and Presence Service
                                                source from a restricted version to an unrestricted version. |
|---|---|

| Note | If you're using Cisco Prime Collaboration Deployment to upgrade an IM and Presence Service cluster from Release 14 or SUs
                                       to Release 15, you must install the following COP file on the Release 14 or SU systems before you begin the upgrade: ciscocm.imp15_upgrade_v1.0.k4.cop.sha512.
                                       Note that the COP file is applicable only if: Unified Communications Manager destination version is in Release 15 and the IM and Presence Service source nodes are in 14
                                                or 14SU1 versions. Unified Communications Manager destination version is in Release 15 and you are trying to upgrade your IM and Presence Service
                                                source from a restricted version to an unrestricted version. |
|---|---|

| Note | If your Cisco Prime Collaboration Deployment is Release 15SU2 and it is using TLS 1.3 and that PCD is discovering, upgrading,
                                          migrating, installing, also performing server restart, readdress, and switch version of UC clusters of pre-15SU2, then ensure
                                          that your Cisco Prime Collaboration Deployment is configured with a minimum TLS version other than the TLS 1.3 protocol before
                                          proceeding with any of these tasks. |
|---|---|

| Note | You can only use the 15 or later versions of Cisco Prime Collaboration Deployment for all 15 or above UC clusters. |
|---|---|

| Note | If the source is in FIPS mode and/or PCD in FIPS mode, see https://www.cisco.com/web/software/286319173/139477/ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop-ReadMe.pdf for information on the COP file ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop . This document details the pre-requisites required for direct upgrade or direct migration to the 14SU2 or above destination
                                       versions. |
|---|---|

| Note | If your Cisco Prime Collaboration Deployment is in FIPS mode and you are using any of the Pre-12.5 UC clusters to perform
                                       cluster discovery, upgrade, or migration, you must first switch your Cisco Prime Collaboration Deployment to work in the non-FIPS
                                       mode before proceeding with any of these tasks. |
|---|---|

| Note | The releases listed in the tables do not specify the Engineering Special (ES)/ Service Update (SU) versions. To identify supported
                                          ES/SU versions that you can upgrade or migrate to through Cisco Prime Collaboration Deployment, see the release notes of the
                                          corresponding product, such as IM and Presence, Cisco Unified Communications Manager, and Unity Connection. |
|---|---|

| Note | Cisco Prime Collaboration Deployment supports the destination version 12.5 and above for an upgrade, and destination version
                                          10.5 and above for migrations. The application versions 10.x and above support virtualization. If the source version is 12.5
                                          and above, the upgrade task is supported. However, if the source version is prior to 12.5, the upgrade task is not supported. A migrate cluster task can migrate to any of releases listed in the tables, by having source version as 10.5 or above and
                                          the destination version should be 12.5 or higher on virtual machine. |
|---|---|

| Note | If you're using Cisco Prime Collaboration Deployment to migrate Cisco Unified Communications Manager from Release 12.0(1)
                                          to any higher release, you must install the following COP file on the 12.0(1) system before you begin the migration. Otherwise,
                                          the configuration files related to Smart Licensing won't be migrated. ciscocm-slm-migration.k3.cop.sgn This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Cisco Unified Communications
                                          Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Cisco Unified Communications Manager
                                          12.0(1)SU1, you don't need to install the COP file. |
|---|---|

| Note | Check destination application version release notes for any known caveats with using the Cisco Prime Collaboration Deployment
                                          tasks with the application. For Cisco Prime Collaboration Deployment, Fresh Install, Migrate and Upgrade tasks, check the
                                          destination application’s Installation Guide and Upgrade Guide for any application-specific rules or restrictions on using
                                          these Cisco Prime Collaboration Deployment tasks with the application (for example, required node sequencing for installs
                                          or upgrades, restrictions on how COPs may be installed, and so on.) |
|---|---|

| Note | If you're using Cisco Prime Collaboration Deployment to discover a cluster of the products deployed with the releases that
                                          have an issue as mentioned in the below table, you must install the ciscocm.V11.5.1_CSCvv25961_add_diffie_C0085 COP file on
                                          the Unified Communications Manager system before you begin the discovery, otherwise, the discovery fails. Product Release with issue Cop file for fix Release with Fix Cisco Unified Communications Manager 11.5.1.18900-97 Yes 11.5(1)Su9 and above 10.5.2.22900-11 N/A ES Branch 10.5.2.23200-1 and above IM and Presence Service 11.5.1.18900-15 Yes 11.5(1)Su9 and above Cisco Unity Connection 11.5.1.21137-1 Yes 11.5(1)Su9 and above Cisco Emergency Responder 11.5.4.61000-12 Yes 11.5(1)Su9 and above | Product | Release with issue | Cop file for fix | Release with Fix | Cisco Unified Communications Manager | 11.5.1.18900-97 | Yes | 11.5(1)Su9 and above | 10.5.2.22900-11 | N/A | ES Branch 10.5.2.23200-1 and above | IM and Presence Service | 11.5.1.18900-15 | Yes | 11.5(1)Su9 and above | Cisco Unity Connection | 11.5.1.21137-1 | Yes | 11.5(1)Su9 and above | Cisco Emergency Responder | 11.5.4.61000-12 | Yes | 11.5(1)Su9 and above |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Product | Release with issue | Cop file for fix | Release with Fix |
| Cisco Unified Communications Manager | 11.5.1.18900-97 | Yes | 11.5(1)Su9 and above |
| 10.5.2.22900-11 | N/A | ES Branch 10.5.2.23200-1 and above |
| IM and Presence Service | 11.5.1.18900-15 | Yes | 11.5(1)Su9 and above |
| Cisco Unity Connection | 11.5.1.21137-1 | Yes | 11.5(1)Su9 and above |
| Cisco Emergency Responder | 11.5.4.61000-12 | Yes | 11.5(1)Su9 and above |

| Product | Release with issue | Cop file for fix | Release with Fix |
|---|---|---|---|
| Cisco Unified Communications Manager | 11.5.1.18900-97 | Yes | 11.5(1)Su9 and above |
| 10.5.2.22900-11 | N/A | ES Branch 10.5.2.23200-1 and above |
| IM and Presence Service | 11.5.1.18900-15 | Yes | 11.5(1)Su9 and above |
| Cisco Unity Connection | 11.5.1.21137-1 | Yes | 11.5(1)Su9 and above |
| Cisco Emergency Responder | 11.5.4.61000-12 | Yes | 11.5(1)Su9 and above |

| Note | If you are using Cisco Prime Collaboration Deployment for upgrading clusters of the products deployed using SHA-512 files,
                                       ensure that you use the Release 14 or above versions of the Cisco Prime Collaboration Deployment. As part of enhancing the
                                       security compliances, all new COP and ISO files now have a '.sha512' extension in their names instead of the '.sgn' extension.
                                       For more information, see 'Enhanced Security Compliances' at Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 14 . |
|---|---|

| Task | Release |
|---|---|
| Cluster Discovery | 10.5.x, 11.5, 12.x, 14 and SUs, and 15 |
| Migrate Cluster (Install Application and Import Data from Old System) | From 10.5.x, 11.x, 12.x, 14 and SUs, and 15 To 12.5.x, 14 and SUs, and 15 |
| Upgrade Cluster (Upgrade Application Version or Install COP Files) | From 11.5, 12.x, and 14 and SUs To 12.5.x and 14 and SUs Also From 12.5.x and 14 and SUs To 15 |
| Restart | 11.5, 12.x, 14 and SUs, and 15 |
| Switch Version | 11.5, 12.x, 14 and SUs, and 15 |
| Fresh Install New Cluster or Edit or Expand an Existing Cluster | 12.5.x, 14 and SUs, and 15 |
| Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster) | 12.5.x, 14 and SUs, and 15 |

| Task | Release |
|---|---|
| Cluster Discovery | 10.5.x, 11.x, 12.x, 14 and SUs, and 15 |
| Migrate Cluster (Install Application and Import Data from Old System) | From 10.5.x, 11.x, 12.x, 14 and SUs, and 15 To 12.5.x, 14 and SUs, and 15 |
| Upgrade Cluster (Upgrade Application Version or Install COP Files) | From 11.5, 12.x, and 14 and SUs To 12.5.x and 14 and SUs Also From 12.5.x and 14 and SUs To 15 |
| Restart | 11.5, 12.x, 14 and SUs, and 15 |
| Switch Version | 11.5, 12.x, 14 and SUs, and 15 |
| Fresh Install New Cluster or Edit or Expand an Existing Cluster | 12.5.x, 14 and SUs, and 15 |
| Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster) | Not Supported |

| Task | Release |
|---|---|
| Cluster Discovery | 11.5, 11.6, 12.x |
| Migrate Cluster (Install Application and Import Data from Old System) | Not Supported |
| Upgrade Cluster (Upgrade Application Version or Install COP Files) | Release Supported: 11.5, 11.6, 12.x To 12.5(1)SU2 and above Note Deployment of UCCX upgrade of a COP file for release 12.0.1, 11.x, and 10.x should be done one node at a time using PCD. | Note | Deployment of UCCX upgrade of a COP file for release 12.0.1, 11.x, and 10.x should be done one node at a time using PCD. |
| Note | Deployment of UCCX upgrade of a COP file for release 12.0.1, 11.x, and 10.x should be done one node at a time using PCD. |
| Restart | 11.5, 11.6, 12.5(1)SU2 and above |
| Switch Version | 11.5, 11.6, 12.5(1)SU2 and above |
| Fresh Install New Cluster or Edit or Expand an Existing Cluster | 12.5(1)SU2 and above |
| Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster) | 12.5(1)SU2 and above |

| Note | Deployment of UCCX upgrade of a COP file for release 12.0.1, 11.x, and 10.x should be done one node at a time using PCD. |
|---|---|

| Note | When you perform any task (Upgrade Cluster, Fresh Install New Cluster, or Edit or Expand an Existing Cluster) from Unified
                                       Contact Center Express, you cannot use the touchless installation method. The user needs to enter the details manually. For
                                       more information on the installation process, see the Installation Guide and Upgrade Guide of Cisco Unified Contact Center Express. |
|---|---|

| Task | Release |
|---|---|
| Cluster Discovery | 11.5, 12.x, 14 and SUs, and 15 |
| Migrate Cluster (Install Application and Import Data from Old System) | Not Supported |
| Upgrade Cluster (Upgrade Application Version or Install COP Files) | From 11.5, 12.x, and 14 and SUs To 12.5.x and 14 and SUs Also From 12.5.x and 14 and SUs To 15 |
| Restart | 11.5, 12.x, 14 and SUs, and 15 |
| Switch Version | 11.5, 12.x, 14 and SUs, and 15 |
| Fresh Install New Cluster or Edit or Expand an Existing Cluster | 12.5.x, 14 and SUs, and 15 |
| Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster) | 12.5.x, 14 and SUs, and 15 |

| Task | Release |
|---|---|
| Cluster Discovery | 11.5(x), 12.x, 14 and SUs, and 15 |
| Migrate Cluster (Install Application and Import Data from Old System) | Not Supported |
| Upgrade Cluster (Upgrade Application Version or Install COP Files) | From 11.5, 12.x, and 14 and SUs To 12.5.x and 14 and SUs Also From 12.5.x and 14 and SUs To 15 |
| Restart | 11.5, 12.x, 14 and SUs, and 15 |
| Switch Version | 11.5, 12.x, 14 and SUs, and 15 |
| Fresh Install New Cluster or Edit or Expand an Existing Cluster | Not Supported |
| Readdress (Change Hostname or IP Addresses for One or More Nodes in a Cluster) | 12.5.x, 14 and SUs, and 15 |

| From | To | Task
                                          					 Types Supported |
|---|---|---|
| Export
                                          					 Restricted (K9) | Export
                                          					 Restricted (K9) | Supported for Upgrade paths Supported for Migration paths |
| Export
                                          					 Restricted (K9) | Export
                                          					 Unrestricted (XU) | Not
                                          					 supported for Upgrade paths Supported for Migration paths |
| Export
                                          					 Unrestricted (XU) | Export
                                          					 Restricted (K9) | Not
                                          					 supported for Upgrade paths Not
                                          					 supported for Migration paths |
| Export
                                          					 Unrestricted (XU) | Export
                                          					 Unrestricted (XU) | Supported for Upgrade paths Supported for Migration paths |

| VMware vSphere ESXi on Host having VM of Cisco Unified Communications Manager or Another Application | Cisco Prime Collaboration Deployment Version Compatibility for VMware APIs |
|---|---|
| 6.0 and 6.5 | No—For Release 11.5(1) Yes—For Release 11.5(1) SU1 through 14 and SUs |
| 6.7 | No—For Release 15 and later Yes—For Release 11.5(1) SU1 through 14 and SUs |
| 7.0 U3 | Yes—For Release 12.6 and later |
| 8.0 U1 | Yes—For Release 14 and later |

|  | Use case | What to do in PCD... |
|---|---|---|
| 1 | Add ESXi hosts | Add an ESXi Host Server |
| 2 | ESXi host was changed external to PCD for Discovered Clusters | Delete an ESXi Host Server Add an ESXi Host Server |
| 3 | Add a new Cluster for Fresh Install | Add New Cluster for Fresh Install Edit or Delete a New Install Cluster |
| 4 | Add an installed cluster to the PCD Inventory | Discover a Cluster Modify and View a Cluster Perform the various tasks mentioned in the application. See Supported Tasks for Applications and Versions . |
| 5 | Update the Cluster Inventory for an already Discovered Custer, where a node was added external to PCD. For example: Add an IM and Presence Service node to the already-discovered Unified CM cluster. Add Unified Communications Manager subscriber to an already discovered Unified CM, Unity Connection, and Unified Contact Center
                                                Express cluster. | Delete a cluster from Inventory— Edit or Delete a Discovered Cluster Discover a Cluster— Discover a Cluster |
| 6 | Update the Cluster Inventory for an already discovered cluster, where a node was removed external to PCD. For example, when
                                          you delete a Unified Communications Manager or IM and Presence Service node from the Unified CM cluster. | Delete a cluster from Inventory— Edit or Delete a Discovered Cluster Discover a Cluster— Discover a Cluster |
| 7 | Update the PCD Inventory for an already discovered cluster, where a node was replaced external to PCD. For example, when you
                                          delete a Unified Communications Manager or IM and Presence Service node from the Unified CM cluster, and then add a new node
                                          to the cluster. | Cluster node's count and IP Addresses aren't changed and then updated the cluster using the Refresh Cluster button. (OR) Cluster node's count or IP Addresses changed. Delete a cluster from Inventory— Edit or Delete a Discovered Cluster Discover a Cluster— Discover a Cluster |
| 8 | Update the PCD Inventory for an already discovered cluster, where a cluster was upgraded external to the PCD upgrade task.
                                          For example, in scenarios where the Unified CM or IM and Presence Service cluster that was directly upgraded using OS Admin
                                          UI or CLI after the time of discovery. | Cluster node's count and IP Addresses aren't changed and then updated the cluster using the Refresh Cluster button. (OR) Cluster node's count or IP Addresses changed. Delete Cluster from Inventory— Edit or Delete a Discovered Cluster Discover a Cluster— Discover a Cluster |
| 9 | Update PCD Inventory for an already discovered cluster, where a cluster needs to have the following configuration values changed
                                          (and it’s desired to configure them directly from PCD versus using the application OS Admin UI or CLI): Admin Username Password NAT IP Assign SFTP server details Notes | You can use the Edit Node option to change the mentioned configuration values and proceed with other tasks. |
| 10 | Update PCD Inventory for an already discovered cluster, where a cluster needs to have one or more nodes added to perform mixed
                                          node installation. | You can use the Edit cluster option to add one or more nodes and then proceed with installation. See Edit or Delete a Discovered Cluster . |

| Important | When you add an ESXi host into Cisco Prime Collaboration Deployment, you mount the Cisco Prime Collaboration Deployment server
                                          as a network file system (NFS) mounted on that host. In future, if you remove your Cisco Prime Collaboration Deployment machine,
                                          you first delete the ESXi host from the Cisco Prime Collaboration Deployment so that it does not cause a stale NFS mount on
                                          that host. |
|---|---|

| Note | When you shut down a Cisco Prime Collaboration Deployment server, we recommend that you use the utils system shutdown CLI command. |
|---|---|

| Note | Make sure that the host with the Cisco Prime Collaboration Deployment VM and the host with the application VMs use the required
                                             Virtualization Software License. See Virtualization Software License Types . |
|---|---|

| Note | Ensure that the ESXi password is less than 32 characters, cluster password (install/discovered/migration) is less than 16
                                             characters and are compliant with the preceding section that describes allowable special characters. For more information on restrictions on the password format that are allowed for Cisco Unified Communications Manager, see
                                             the Administration Guide for Cisco Unified Communications Manager and IM and Presence Service . |
|---|---|

| Note | Cisco Prime Collaboration Deployment supports only the VMware ESXi Embedded Host Client/authentication and doesn't support
                                          vCenter and its method of authentication. For more information on user names and passwords that is accepted by the Embedded
                                          Host Client, see vmware documentation. |
|---|---|

| Note | If your Cisco Prime Collaboration Deployment in configured with TLS 1.3 version and you want to add an ESXi host server, you
                                          must use the ESXi 8.0 U2 version or above. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, click the open and close navigation button and choose the Inventory > ESXi Hosts from the menu. |
|---|---|
| Step 2 | Click Add ESXi Host . |
| Step 3 | The Add Host Server dialog box appears. Enter the following information: Hostname/IP Address Root sign-in or sufficiently privileged nonroot sign-in Root password or nonroot password |
| Step 4 | Click OK to add the ESXi host. |

| Step 1 | From the Cisco Prime Collaboration Deployment application, click the open and close navigation button and choose the Inventory > ESXi Hosts from the menu. |
|---|---|
| Step 2 | Click Delete . |

| Step 1 | From the Cisco
                                          			 Prime Collaboration Deployment application, select Inventory > Clusters . |
|---|---|
| Step 2 | Click Define
                                             				New UC Cluster . The Define Cluster wizard appears. |
| Step 3 | In the Specify
                                          			 Cluster Name section, enter the cluster name, and click Next . The Add
                                             				Virtual Machines window appears. |
| Step 4 | Click Add
                                             				Node to add nodes to the cluster. The Add Node dialog box appears to show the list of the available VMs that are sorted by name and by host. |
| Step 5 | On the Add
                                             				Node window, enter the network settings for the node that you have
                                          			 added, choose the functions for the node, and choose a VM for this node. Select
                                          			 the VM that you wish to add and then enter the following information in the
                                          			 sections below the VM table: In Network
                                                				  section, select either Static IP Address or Use DHCP with reservations . If you select the Static IP Address option, enter the hostname, IP
                                                				  Address, subnet mask, gateway, and NAT IP. If you select Use DHCP with reservations option, enter the IP
                                                				  address that you have a reservation for on your DHCP server (associated with
                                                				  the MAC address for that VM) in addition to the hostname. If you are adding a Cisco Unified Contact Center Express server,
                                                				  do not use DHCP for network settings. Note NAT IP is an optional field. In Step 4, if you have selected a node that is behind NAT, enter the IP address in the NAT IP field, else leave this field blank. The value that you enter in this field appears in the NAT IP column. If the NAT IP address is associated with a port, you can enter port value which should be in the range of 1–65535. From the Products and Functions list box, select a product. In the
                                                				  Functions section, check the appropriate function check boxes for your VM. Note Check the Publisher check box for at least one node in the
                                                                     							 cluster that you have defined, for each application type. (Optional) Add a note about the functions that you have assigned
                                                                     							 in the Notes field below the Publisher field. Click OK . In Virtual
                                                				  Machines section, choose a VM for this node. Note Choose a new VM for fresh install clusters and that new VMs must
                                                                     							 be in turned off state. Do
                                                                     							 not install over an existing running Cisco Unified Communications Manager node.
                                                                     							 The installation must be a fresh VM that you create with the appropriate OVA
                                                                     							 for the application that you will install. | Note | NAT IP is an optional field. In Step 4, if you have selected a node that is behind NAT, enter the IP address in the NAT IP field, else leave this field blank. The value that you enter in this field appears in the NAT IP column. If the NAT IP address is associated with a port, you can enter port value which should be in the range of 1–65535. | Note | Check the Publisher check box for at least one node in the
                                                                     							 cluster that you have defined, for each application type. (Optional) Add a note about the functions that you have assigned
                                                                     							 in the Notes field below the Publisher field. | Note | Choose a new VM for fresh install clusters and that new VMs must
                                                                     							 be in turned off state. Do
                                                                     							 not install over an existing running Cisco Unified Communications Manager node.
                                                                     							 The installation must be a fresh VM that you create with the appropriate OVA
                                                                     							 for the application that you will install. |
| Note | NAT IP is an optional field. In Step 4, if you have selected a node that is behind NAT, enter the IP address in the NAT IP field, else leave this field blank. The value that you enter in this field appears in the NAT IP column. If the NAT IP address is associated with a port, you can enter port value which should be in the range of 1–65535. |
| Note | Check the Publisher check box for at least one node in the
                                                                     							 cluster that you have defined, for each application type. (Optional) Add a note about the functions that you have assigned
                                                                     							 in the Notes field below the Publisher field. |
| Note | Choose a new VM for fresh install clusters and that new VMs must
                                                                     							 be in turned off state. Do
                                                                     							 not install over an existing running Cisco Unified Communications Manager node.
                                                                     							 The installation must be a fresh VM that you create with the appropriate OVA
                                                                     							 for the application that you will install. |
| Step 6 | Click OK . The
                                          			 VM is added and is listed in the Cluster Name table. |
| Step 7 | (Optional)
                                          			 To add more nodes to the cluster, repeat steps 4 through 6. |
| Step 8 | Click Next . The Configure Cluster Wide Settings window appears. |
| Step 9 | Enter the OS
                                          			 administration credentials, application credentials, security password, SMTP
                                          			 settings, and certificate information for this cluster, and click Next . Note Before you enable FIPS mode, Common Criteria, or Enhanced Security Mode, ensure that you have minimum 14 characters for Security
                                                         Password. The Configure DNS Settings window appears. | Note | Before you enable FIPS mode, Common Criteria, or Enhanced Security Mode, ensure that you have minimum 14 characters for Security
                                                         Password. |
| Note | Before you enable FIPS mode, Common Criteria, or Enhanced Security Mode, ensure that you have minimum 14 characters for Security
                                                         Password. |
| Step 10 | (Optional) Add
                                          			 a DNS setting for a node, select the node, and click Assign
                                             				DNS Settings . The Cisco Unified Contact Center Express application
                                          			 must use DNS. The Configure NTP Settings window appears. |
| Step 11 | Enter IP
                                          			 address of at least one NTP server. Note It is
                                                               						recommended that you define at least IP addresses of two NTP servers. If you
                                                               						are not using DNS, NTP server must be an IP address. If you are using DNS, NTP
                                                               						server can be an FQDN. | Note | It is
                                                               						recommended that you define at least IP addresses of two NTP servers. If you
                                                               						are not using DNS, NTP server must be an IP address. If you are using DNS, NTP
                                                               						server can be an FQDN. |
| Note | It is
                                                               						recommended that you define at least IP addresses of two NTP servers. If you
                                                               						are not using DNS, NTP server must be an IP address. If you are using DNS, NTP
                                                               						server can be an FQDN. |
| Step 12 | Click Next . The Configure NIC Settings window appears. |
| Step 13 | (Optional)
                                          			 Choose the server, and enter an MTU size between 552 and 1500, and click Apply
                                             				to Selected . |
| Step 14 | Click Next . The Configure Time Zones window appears. |
| Step 15 | Select a node,
                                          			 choose the region and time zone from the Region and Time
                                             				Zones list boxes, and click Apply
                                             				to Selected . |
| Step 16 | Click Finish . The new install cluster is listed on the Clusters screen, with a Cluster Type as New Install . The cluster is defined but is yet to be created. To install the cluster, create an install task. The install task uses the
                                          install cluster that you have defined, and creates the cluster. |

| Note | NAT IP is an optional field. In Step 4, if you have selected a node that is behind NAT, enter the IP address in the NAT IP field, else leave this field blank. The value that you enter in this field appears in the NAT IP column. If the NAT IP address is associated with a port, you can enter port value which should be in the range of 1–65535. |
|---|---|

| Note | Check the Publisher check box for at least one node in the
                                                                     							 cluster that you have defined, for each application type. (Optional) Add a note about the functions that you have assigned
                                                                     							 in the Notes field below the Publisher field. |
|---|---|

| Note | Choose a new VM for fresh install clusters and that new VMs must
                                                                     							 be in turned off state. Do
                                                                     							 not install over an existing running Cisco Unified Communications Manager node.
                                                                     							 The installation must be a fresh VM that you create with the appropriate OVA
                                                                     							 for the application that you will install. |
|---|---|

| Note | Before you enable FIPS mode, Common Criteria, or Enhanced Security Mode, ensure that you have minimum 14 characters for Security
                                                         Password. |
|---|---|

| Note | It is
                                                               						recommended that you define at least IP addresses of two NTP servers. If you
                                                               						are not using DNS, NTP server must be an IP address. If you are using DNS, NTP
                                                               						server can be an FQDN. |
|---|---|

| Step 1 | To edit an existing node, perform the following: From the Cisco Prime Collaboration Deployment application, click the open and close navigation button and choose Inventory > Clusters . Click a cluster that has the cluster type as New Install and click Edit . In the Specify Cluster Name section, view the pre-populated cluster name, and click Next . In the Add Virtual Machines section, select a node from the existing nodes, and click Edit . The Add Node window appears. In the Add Node window, edit the node details, and click OK . In the Configure Cluster Wide Settings section, edit the OS administration credentials, application credentials, security
                                                password, SMTP settings, and certificate information for all nodes of a cluster, as required, and click Next . Note Before you enable FIPS mode, Common Criteria, or Enhanced Secuirty Mode, ensure that you have minimum 14 characters for Security
                                                               Password. (Optional) In the Configure DNS Settings section, edit the DNS settings for the migration cluster nodes, and click Next . Note If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes and is auto-populated. If the previous nodes have multiple values for DNS or domain, then
                                                               no default value is applied. In the Configure NTP Settings section, edit the configuration of the NTP servers for the nodes in a cluster, and click Next . Note The changes you make in this section apply to publisher node only. (Optional) In the Configure NIC Settings section, choose a server, and enter an MTU size between 552 and 1500, click Apply to Selected , and then click Next . In the Configure Time Zones section, select a node, edit the region and time zone from the Region and Time Zones list boxes,
                                                click Apply to Selected , and then click Finish . Note If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                               default value for the new nodes and is auto-populated. If the previous nodes have multiple values for time zone, then no default
                                                               value is applied. The changes are saved. You can install one or multiple nodes in a cluster. See Add Install Task for details. | Note | Before you enable FIPS mode, Common Criteria, or Enhanced Secuirty Mode, ensure that you have minimum 14 characters for Security
                                                               Password. | Note | If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes and is auto-populated. If the previous nodes have multiple values for DNS or domain, then
                                                               no default value is applied. | Note | The changes you make in this section apply to publisher node only. | Note | If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                               default value for the new nodes and is auto-populated. If the previous nodes have multiple values for time zone, then no default
                                                               value is applied. |
|---|---|---|---|---|---|---|---|---|---|
| Note | Before you enable FIPS mode, Common Criteria, or Enhanced Secuirty Mode, ensure that you have minimum 14 characters for Security
                                                               Password. |
| Note | If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes and is auto-populated. If the previous nodes have multiple values for DNS or domain, then
                                                               no default value is applied. |
| Note | The changes you make in this section apply to publisher node only. |
| Note | If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                               default value for the new nodes and is auto-populated. If the previous nodes have multiple values for time zone, then no default
                                                               value is applied. |
| Step 2 | To delete an existing node, perform the following: From the Cisco Prime Collaboration Deployment application, click the open and close navigation button and choose Inventory > Clusters . Click a cluster that has the cluster type as New Install and click Delete . |

| Note | Before you enable FIPS mode, Common Criteria, or Enhanced Secuirty Mode, ensure that you have minimum 14 characters for Security
                                                               Password. |
|---|---|

| Note | If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes and is auto-populated. If the previous nodes have multiple values for DNS or domain, then
                                                               no default value is applied. |
|---|---|

| Note | The changes you make in this section apply to publisher node only. |
|---|---|

| Note | If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                               default value for the new nodes and is auto-populated. If the previous nodes have multiple values for time zone, then no default
                                                               value is applied. |
|---|---|

| Note | If the Cisco Prime Collaboration Deployment is in FIPS mode and you are using any of the Pre-12.5 UC clusters to perform cluster
                                          discovery, you must first switch your Cisco Prime Collaboration Deployment to work in the non-FIPS mode before proceeding
                                          with cluster discovery. |
|---|---|

| Note | Ensure that both the Cisco Prime Collaboration Deployment and UC clusters match the FIPS settings, either in the FIPS mode
                                             or in the non-FIPS mode, before proceeding with cluster discovery. |
|---|---|

| Note | If the UC cluster is fips_common_criteria enabled and your Cisco Prime Collaboration Deployment is configured with the minimum
                                          TLS protocol version as 1.3, then cluster discovery fails for the UC clusters. |
|---|---|

| Note | If a cluster includes Cisco Unified Communications Manager and IM and Presence Service (Cisco Unified Communications and IM
                                          and Presence Service servers), the Cluster Discovery discovers the Cisco Unified Presence or IM and Presence Service nodes
                                          as part of the Cisco Unified Communications Manager cluster. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Inventory > Clusters . |
|---|---|
| Step 2 | Click Discover Cluster to discover the existing clusters. The Discover Cluster wizard appears. |
| Step 3 | Enter details in the following fields: Choose a Nickname for this Cluster Hostname/IP Address of Cluster Publisher Note For a cluster that has both Unified Communications Manager and IM and Presence Service nodes, enter the hostname or IP address
                                                            of the Cisco Unified Communications Manager publisher. Note When the publisher is behind the NAT, providing the private IP address of the publisher does not reach to the node. You must
                                                            provide the proper NAT/ Public IP address for successful node discovery. OS Admin Username OS Admin Password Note Ensure that cluster password is less than 16 characters. You must not use the % character in the Cisco Unified OS Administration password for successful node discovery. Enable NAT | Note | For a cluster that has both Unified Communications Manager and IM and Presence Service nodes, enter the hostname or IP address
                                                            of the Cisco Unified Communications Manager publisher. | Note | When the publisher is behind the NAT, providing the private IP address of the publisher does not reach to the node. You must
                                                            provide the proper NAT/ Public IP address for successful node discovery. | Note | Ensure that cluster password is less than 16 characters. You must not use the % character in the Cisco Unified OS Administration password for successful node discovery. |
| Note | For a cluster that has both Unified Communications Manager and IM and Presence Service nodes, enter the hostname or IP address
                                                            of the Cisco Unified Communications Manager publisher. |
| Note | When the publisher is behind the NAT, providing the private IP address of the publisher does not reach to the node. You must
                                                            provide the proper NAT/ Public IP address for successful node discovery. |
| Note | Ensure that cluster password is less than 16 characters. You must not use the % character in the Cisco Unified OS Administration password for successful node discovery. |
| Step 4 | (Optional) Check the Enable NAT check box, and then click Next . Important During discovery, the ciscocm.ucmap_platformconfig.cop file is installed automatically on the active partition of all nodes in the cluster. This COP file is used for the cluster
                                                      discovery process and does not affect Cisco Unified Communications Manager. Note When a cluster is behind NAT, the application tries to establish communication with each node using its private address. So,
                                                      the nodes are unreachable. A pop-up shows the unreachable nodes. Cisco Prime Collaboration Deployment generates a list of cluster nodes from the inventory of the publisher server. The list
                                          generation process may take several minutes to complete. After the list is generated, a confirmation message appears to indicate
                                          the completion of the cluster discovery process. | Important | During discovery, the ciscocm.ucmap_platformconfig.cop file is installed automatically on the active partition of all nodes in the cluster. This COP file is used for the cluster
                                                      discovery process and does not affect Cisco Unified Communications Manager. | Note | When a cluster is behind NAT, the application tries to establish communication with each node using its private address. So,
                                                      the nodes are unreachable. A pop-up shows the unreachable nodes. |
| Important | During discovery, the ciscocm.ucmap_platformconfig.cop file is installed automatically on the active partition of all nodes in the cluster. This COP file is used for the cluster
                                                      discovery process and does not affect Cisco Unified Communications Manager. |
| Note | When a cluster is behind NAT, the application tries to establish communication with each node using its private address. So,
                                                      the nodes are unreachable. A pop-up shows the unreachable nodes. |
| Step 5 | Click Edit to add NAT IP address, and click OK . The NAT IP address is set for the hostname. |
| Step 6 | Click Resume Discovery to resume the discovery of unreachable nodes. Cisco Prime Collaboration Deployment retries to discover the cluster with the NAT IP address instead of the private IP address
                                          and to get the cluster details, such as version. The discovery is successful when the cluster details appear on the window. |
| Step 7 | Click Next . |
| Step 8 | (Optional) Click Assign Functions to assign functions to each of the cluster nodes. Note The assignment of functions has no effect on the services that are to be activated. However, this information can be used
                                                      to determine the default sequence of tasks. The Assign Functions dialog box appears. | Note | The assignment of functions has no effect on the services that are to be activated. However, this information can be used
                                                      to determine the default sequence of tasks. |
| Note | The assignment of functions has no effect on the services that are to be activated. However, this information can be used
                                                      to determine the default sequence of tasks. |
| Step 9 | Click Finish . The cluster appears in the Clusters window, showing the cluster name, the product and version, the cluster type as Discovered , and the discovery status. Note It might take a few minutes to discover a cluster. After the discovery is complete, the information for each node in the cluster
                                                      is listed in the Cluster Inventory window. If you cancel the discovery before it is complete, the data is lost and you will have to repeat the discovery procedure. Note The following are the different statuses that appear for the Discovery Status field: Contacting —Indicates that Cisco Prime Collaboration Deployment is establishing communication with clusters. Discovering —Indicates that the cluster discovery is in process. Successful —Indicates that the cluster discovery is successful. Node Unreachable —Indicates that the cluster node is inaccessible. Timeout —Indicates that the duration that is configured for the cluster discovery is complete but no cluster was discovered. Internal Error —Indicates that cluster discovery is failed because of an incorrect NAT IP address. | Note | It might take a few minutes to discover a cluster. After the discovery is complete, the information for each node in the cluster
                                                      is listed in the Cluster Inventory window. If you cancel the discovery before it is complete, the data is lost and you will have to repeat the discovery procedure. | Note | The following are the different statuses that appear for the Discovery Status field: Contacting —Indicates that Cisco Prime Collaboration Deployment is establishing communication with clusters. Discovering —Indicates that the cluster discovery is in process. Successful —Indicates that the cluster discovery is successful. Node Unreachable —Indicates that the cluster node is inaccessible. Timeout —Indicates that the duration that is configured for the cluster discovery is complete but no cluster was discovered. Internal Error —Indicates that cluster discovery is failed because of an incorrect NAT IP address. |
| Note | It might take a few minutes to discover a cluster. After the discovery is complete, the information for each node in the cluster
                                                      is listed in the Cluster Inventory window. If you cancel the discovery before it is complete, the data is lost and you will have to repeat the discovery procedure. |
| Note | The following are the different statuses that appear for the Discovery Status field: Contacting —Indicates that Cisco Prime Collaboration Deployment is establishing communication with clusters. Discovering —Indicates that the cluster discovery is in process. Successful —Indicates that the cluster discovery is successful. Node Unreachable —Indicates that the cluster node is inaccessible. Timeout —Indicates that the duration that is configured for the cluster discovery is complete but no cluster was discovered. Internal Error —Indicates that cluster discovery is failed because of an incorrect NAT IP address. |

| Note | For a cluster that has both Unified Communications Manager and IM and Presence Service nodes, enter the hostname or IP address
                                                            of the Cisco Unified Communications Manager publisher. |
|---|---|

| Note | When the publisher is behind the NAT, providing the private IP address of the publisher does not reach to the node. You must
                                                            provide the proper NAT/ Public IP address for successful node discovery. |
|---|---|

| Note | Ensure that cluster password is less than 16 characters. You must not use the % character in the Cisco Unified OS Administration password for successful node discovery. |
|---|---|

| Important | During discovery, the ciscocm.ucmap_platformconfig.cop file is installed automatically on the active partition of all nodes in the cluster. This COP file is used for the cluster
                                                      discovery process and does not affect Cisco Unified Communications Manager. |
|---|---|

| Note | When a cluster is behind NAT, the application tries to establish communication with each node using its private address. So,
                                                      the nodes are unreachable. A pop-up shows the unreachable nodes. |
|---|---|

| Note | The assignment of functions has no effect on the services that are to be activated. However, this information can be used
                                                      to determine the default sequence of tasks. |
|---|---|

| Note | It might take a few minutes to discover a cluster. After the discovery is complete, the information for each node in the cluster
                                                      is listed in the Cluster Inventory window. If you cancel the discovery before it is complete, the data is lost and you will have to repeat the discovery procedure. |
|---|---|

| Note | The following are the different statuses that appear for the Discovery Status field: Contacting —Indicates that Cisco Prime Collaboration Deployment is establishing communication with clusters. Discovering —Indicates that the cluster discovery is in process. Successful —Indicates that the cluster discovery is successful. Node Unreachable —Indicates that the cluster node is inaccessible. Timeout —Indicates that the duration that is configured for the cluster discovery is complete but no cluster was discovered. Internal Error —Indicates that cluster discovery is failed because of an incorrect NAT IP address. |
|---|---|

| Note | The cluster nodes that has been discovered or is newly installed will have the Refresh Cluster link to re-discover the same cluster. |
|---|---|

| Step 1 | Discover a cluster by following the 'Discover a Cluster' procedure. See Discover a Cluster . |
|---|---|
| Step 2 | Check the check box of one of the discovered or newly installed clusters to choose a cluster, and click the Refresh Cluster link. |

| Note | The cluster nodes that has been discovered or is newly installed will have the Refresh Cluster link to re-discover the same cluster. |
|---|---|

| Note | The cluster nodes that you need to install appear as editable and have Edit and Delete links. The installed cluster nodes appear dimmed and you can't edit or delete them. |
|---|---|

| Note | When you add new nodes to the installed cluster, all
                                             			 fields on Configure NTP Settings page appear dimmed
                                             			 and are non-editable.
                                             		  The fields on the other pages will populate the values of the already installed nodes as the default. If needed, you can
                                             change the values for the newly added nodes. |
|---|---|

| Step 1 | Discover a cluster by following the 'Discover a Cluster' procedure. See Discover a Cluster . |
|---|---|
| Step 2 | Check the check box of one of the discovered or newly installed clusters to choose a cluster, and click Edit link. |
| Step 3 | On the Edit Link window, view the details in the fields, and modify the details, as required. |
| Step 4 | Click OK . |

| Note | After you add
                                             			 or install a new node, you cannot delete the node with this feature. You must
                                             			 delete the node from an existing installed cluster by using your application
                                             			 administration web page or the CLI. |
|---|---|

| Step 1 | To edit a node, from the Cisco Prime Collaboration Deployment application, click the open and close navigation button and
                                          choose Inventory > Clusters . From the Cisco Prime Collaboration Deployment application, select Inventory > Clusters . Select a cluster that has the cluster type as Discovered and click Edit . In the Specify Cluster Name section, enter the cluster name, and click Next . Note If the discovered cluster is already installed, the cluster name is non-editable. In the Add Virtual Machines section, select a node from the existing nodes that has not been installed, and click Edit . The Add Node window appears. In the Add Node window, edit the node details, and click OK , and then click Next in the Add Virtual Machines section. Note If you add a new node to an existing cluster, the new nodes cannot use the Publisher function. In the Configure Cluster Wide Settings section, view the OS administration credentials, application credentials, security
                                                password, SMTP settings, and certificate information for all nodes of a cluster and click Next . Note The fields in this section are editable only if the cluster type is New Install . (Optional) In the Configure DNS Settings section, edit the DNS settings for the migration cluster nodes, and click Next . Note If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes. If the previous nodes have multiple values for each DNS or domain, then no default value
                                                               is applied. In the Configure NTP Settings section, view the configuration of the NTP servers for the nodes in a cluster, and click Next . Note The fields in this section are non-editable. (Optional) In the Configure NIC Settings section, edit the server details for the uninstalled nodes, enter an MTU size between
                                                552 and 1500, and then click Next . In the Configure Time Zones section, select a node, edit the region and time zone from the Region and Time Zones list boxes,
                                                click Apply to Selected , and then click Finish . Note If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                            default value for the new nodes. If the previous nodes have multiple values for the time zone, then no default value is applied. The changes are saved. You can install one or multiple nodes in a cluster. See Add Install Task for details. | Note | If the discovered cluster is already installed, the cluster name is non-editable. | Note | If you add a new node to an existing cluster, the new nodes cannot use the Publisher function. | Note | The fields in this section are editable only if the cluster type is New Install . | Note | If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes. If the previous nodes have multiple values for each DNS or domain, then no default value
                                                               is applied. | Note | The fields in this section are non-editable. | Note | If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                            default value for the new nodes. If the previous nodes have multiple values for the time zone, then no default value is applied. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note | If the discovered cluster is already installed, the cluster name is non-editable. |
| Note | If you add a new node to an existing cluster, the new nodes cannot use the Publisher function. |
| Note | The fields in this section are editable only if the cluster type is New Install . |
| Note | If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes. If the previous nodes have multiple values for each DNS or domain, then no default value
                                                               is applied. |
| Note | The fields in this section are non-editable. |
| Note | If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                            default value for the new nodes. If the previous nodes have multiple values for the time zone, then no default value is applied. |
| Step 2 | To delete a node, perform the following: From the Cisco Prime Collaboration Deployment application, select Inventory > Clusters . Select a cluster that has the cluster type as Discovered and click Delete to remove the selected node. |

| Note | If the discovered cluster is already installed, the cluster name is non-editable. |
|---|---|

| Note | If you add a new node to an existing cluster, the new nodes cannot use the Publisher function. |
|---|---|

| Note | The fields in this section are editable only if the cluster type is New Install . |
|---|---|

| Note | If the previous nodes in the cluster have the same values for DNS and domain, then the value from the other nodes becomes
                                                               the default value for the new nodes. If the previous nodes have multiple values for each DNS or domain, then no default value
                                                               is applied. |
|---|---|

| Note | The fields in this section are non-editable. |
|---|---|

| Note | If the previous nodes in the cluster have the same values for time zone, then the value from the other nodes becomes the
                                                            default value for the new nodes. If the previous nodes have multiple values for the time zone, then no default value is applied. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, select Inventory > Clusters . |
|---|---|
| Step 2 | Discover a cluster by following the 'Discover a Cluster' procedure. See Discover a Cluster . |
| Step 3 | Check the check box of one of the discovered or newly installed clusters to choose a node, and click Edit Node link. |
| Step 4 | In the Edit Node window, view the details in the fields, and modify the details, as required. |
| Step 5 | Click OK . |

| Note | Migration and install .iso files must be bootable. |
|---|---|

| Note | PCD scheduler can execute 21 task actions simultaneously. See Max Nodes Configuration . |
|---|---|

| Note | To verify that your source and the desired destination application versions are supported paths for PCD Migration Task, see
                                          the 'Supported Tasks for Cisco Unified Communications Manager (including Session Management Edition)' table in section Supported Tasks for Applications and Versions . |
|---|---|

| Note | If you made updates to the cluster post the time of discovery, you need to re-discover the cluster before migration so that
                                          Cisco Prime Collaboration Deployment has the latest and most accurate view of the recent changes. |
|---|---|

| Note | Make sure that the host with the Cisco Prime Collaboration Deployment VM and the host with the application VMs use the required
                                                Virtualization Software License. See Virtualization Software License Types . |
|---|---|

| Important | When the migration cluster is created, you must indicate whether all destination nodes maintain the same hostname or IP address,
                                                or whether some of these addresses change. |
|---|---|

| Note | Before migrating the cluster, we recommend installing the latest Upgrade Readiness COP file. See the for details. This is applicable if the source cluster is 10.x or above and valid only for Unified Communications Manager
                                                   and IM and Presence Service. Make sure that Prime Collaboration Deployment has enough free space depending on the size of the source cluster in the common
                                                   partition. If your 14SU2 or later versions of Cisco Prime Collaboration Deployment is in FIPS mode and you are using any of the Pre-12.5
                                                   UC clusters to perform migration, you must first switch your Cisco Prime Collaboration Deployment to work in the non-FIPS
                                                   mode before proceeding with migration. You can also use the Fresh Install with Data Import (V2V) option if you do not plan
                                                   to use Cisco Prime Collaboration Deployment for migration. |
|---|---|

| Step 1 | Click Open and close navigation and choose Task > Migrate . |
|---|---|
| Step 2 | Click Add Migration Task . The Add Migration Task wizard appears. |
| Step 3 | In the Specify Task Name drop-down, enter a name for the migration task in Choose a Nickname for this Migration Task . |
| Step 4 | From the Source UC Cluster drop-down list, select the cluster on which the nodes to be migrated from are located. |
| Step 5 | From the Destination Cluster drop-down list, select the destination cluster or migration map. The migration maps are associated with the source cluster
                                             you have selected. Click Next . If you want to apply an upgrade patch along with the migration, click Yes radio button. Click No radio button to proceed with migration task only. |
| Step 6 | In the Choose Migration Files section, choose the ISO file you wish to install on the destination cluster by clicking Browse . The Choose a Migration File window opens. Select the ISO file from the list and click OK . If you have applied upgrade patch along with the migration, browse the patch files along with the ISO files for Unified Communications
                                                Manager and IM and Presence Service You must select the patch file of the same Engineering Special (ES)/ Service Update (SU) versions of the ISO file. Important The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. If you select Prime Collaboration Deployment as SFTP, then you can place the migration file under /fresh_install and the upgrade patch file under /upgrade directory. If you select any remote SFTP, then both migration and upgrade patch file should be in the same SFTP server. Note To create a migration task, while selecting ISO files, ensure that the ISO files are common across all the required SFTP servers
                                                         which are associated to cluster nodes. If the ISO files are not common to all the required SFTP servers which are associated
                                                         to cluster nodes, the valid files do not appear although they are valid for migration. To view all the ISO files, from the Show drop-down list, choose All . Note When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. | Important | The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. | Note | To create a migration task, while selecting ISO files, ensure that the ISO files are common across all the required SFTP servers
                                                         which are associated to cluster nodes. If the ISO files are not common to all the required SFTP servers which are associated
                                                         to cluster nodes, the valid files do not appear although they are valid for migration. To view all the ISO files, from the Show drop-down list, choose All . | Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
| Important | The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. |
| Note | To create a migration task, while selecting ISO files, ensure that the ISO files are common across all the required SFTP servers
                                                         which are associated to cluster nodes. If the ISO files are not common to all the required SFTP servers which are associated
                                                         to cluster nodes, the valid files do not appear although they are valid for migration. To view all the ISO files, from the Show drop-down list, choose All . |
| Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
| Step 7 | If you want to make the newly created task as dependent on the successful completion of another previously executed task,
                                             check the checkbox of the tasks listed in the Task Dependency Scheduling . You can select multiple tasks as dependent tasks. If you do not want to make any dependency, check the No Dependency checkbox. |
| Step 8 | Click Next . |
| Step 9 | In the Specify Migration Procedure section, you will see the default sequence for the migration task. If you wish, you can change the sequence of steps in the
                                             migration procedure. (For example, the default is to install each subscriber individually. You might want to change this to
                                             install more than one subscriber in a step.) You have the following options: Option Description Pencil icon Edit a step. Page icon Add a new step after the current step. X mark Delete the current step. If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the Publisher
                                                         node. Up arrow Move the step up to be performed earlier. Down arrow Move the step down to be performed later. The Pencil icon opens up an Edit Step window. Add nodes to be migrated in this step from the list of available nodes. The available nodes are the ones that you
                                                chose for migration. The step to which each node is assigned displays next to the node. If a node is not assigned to any step, it shows as unassigned. When you assign all the nodes to a step, a default sequencing is available. Important You cannot proceed to the next step until you assign all the nodes. The Pause task after step completes option pauses the task after completion of this step. You must manually start the next step to complete the task. For more information about sequencing tasks, see the task management information at the beginning of this section. | Option | Description | Pencil icon | Edit a step. | Page icon | Add a new step after the current step. | X mark | Delete the current step. If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the Publisher
                                                         node. | Up arrow | Move the step up to be performed earlier. | Down arrow | Move the step down to be performed later. | Important | You cannot proceed to the next step until you assign all the nodes. |
| Option | Description |
| Pencil icon | Edit a step. |
| Page icon | Add a new step after the current step. |
| X mark | Delete the current step. If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the Publisher
                                                         node. |
| Up arrow | Move the step up to be performed earlier. |
| Down arrow | Move the step down to be performed later. |
| Important | You cannot proceed to the next step until you assign all the nodes. |
| Step 10 | Select the date and time when you want the migrate task to begin. You have the following options to schedule upgrades: If the task is created as depended task, then Set Start Time section is disabled. Note Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. Select Schedule for a specific time to enter the date and time when you want the migrate task to start. The start time that you set is based on the time zone
                                                of the Cisco Prime Collaboration Deployment server as denoted by the time zone that is displayed with this option. Note If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. Select Start task manually to keep the task in a manual start. Note If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page. Select Start task immediately upon completion of this wizard to start the task immediately after you click Finish . If you want the system to automatically switch to the new version, choose the option Upgrade Option to Automatically Switch to New Version after Successful Upgrade . | Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. | Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. | Note | If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page. |
| Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. |
| Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. |
| Note | If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page. |
| Step 11 | Click Next . |
| Step 12 | In the Review section, you can review the selections that you made. You can also add notes to your new migration task. |
| Step 13 | If there are no changes required, click Finish to add your new migration task. |
| Step 14 | The new migration task appears in the table on the Migrate screen. Important If you are performing a migration with the network migration, the sequence automatically inserts a "Forced Pause" step into the sequence after all the servers are installed to allow the user to perform procedures. See the "Run a Migration Task" section for details on when manual procedures are needed. The "Forced Pause" step cannot be edited and moved, and it has no nodes that are assigned. This step is inserted before the source node shutdown
                                                         step, because if CTL Updates or certificate management steps are required, these steps must be completed before the source
                                                         node is shut down. | Important | If you are performing a migration with the network migration, the sequence automatically inserts a "Forced Pause" step into the sequence after all the servers are installed to allow the user to perform procedures. See the "Run a Migration Task" section for details on when manual procedures are needed. The "Forced Pause" step cannot be edited and moved, and it has no nodes that are assigned. This step is inserted before the source node shutdown
                                                         step, because if CTL Updates or certificate management steps are required, these steps must be completed before the source
                                                         node is shut down. |
| Important | If you are performing a migration with the network migration, the sequence automatically inserts a "Forced Pause" step into the sequence after all the servers are installed to allow the user to perform procedures. See the "Run a Migration Task" section for details on when manual procedures are needed. The "Forced Pause" step cannot be edited and moved, and it has no nodes that are assigned. This step is inserted before the source node shutdown
                                                         step, because if CTL Updates or certificate management steps are required, these steps must be completed before the source
                                                         node is shut down. |

| Important | The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. |
|---|---|

| Note | To create a migration task, while selecting ISO files, ensure that the ISO files are common across all the required SFTP servers
                                                         which are associated to cluster nodes. If the ISO files are not common to all the required SFTP servers which are associated
                                                         to cluster nodes, the valid files do not appear although they are valid for migration. To view all the ISO files, from the Show drop-down list, choose All . |
|---|---|

| Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
|---|---|

| Option | Description |
|---|---|
| Pencil icon | Edit a step. |
| Page icon | Add a new step after the current step. |
| X mark | Delete the current step. If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the Publisher
                                                         node. |
| Up arrow | Move the step up to be performed earlier. |
| Down arrow | Move the step down to be performed later. |

| Important | You cannot proceed to the next step until you assign all the nodes. |
|---|---|

| Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. |
|---|---|

| Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. |
|---|---|

| Note | If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page. |
|---|---|

| Important | If you are performing a migration with the network migration, the sequence automatically inserts a "Forced Pause" step into the sequence after all the servers are installed to allow the user to perform procedures. See the "Run a Migration Task" section for details on when manual procedures are needed. The "Forced Pause" step cannot be edited and moved, and it has no nodes that are assigned. This step is inserted before the source node shutdown
                                                         step, because if CTL Updates or certificate management steps are required, these steps must be completed before the source
                                                         node is shut down. |
|---|---|

| Note | After you
                                             		  define the migration cluster, see "Migration Task" at Migration Task to define when and how to perform the migration. |
|---|---|

| Step 1 | From the Cisco
                                             			 Prime Collaboration Deployment application, select Inventory > Cluster . |
|---|---|
| Step 2 | Click Define
                                                				Migration Destination Cluster . The Define
                                                				Migration Destination Cluster wizard appears. |
| Step 3 | In the Specify
                                             			 Clusters section, specify the name of the cluster, select the source UC cluster
                                             			 from the drop-down list. Enter a name in the Destination Cluster Name field and
                                             			 select one of the following Destination Network Settings options: To retain the default
                                                				network options, select the Use
                                                   				  the source node network settings for all destination nodes option. To modify the default
                                                				network settings or enter new network options, select the Enter new network settings for one or more destination
                                                   				  nodes option. Note If you
                                                            				  select the Use the source node network settings for all destination
                                                               					 nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns Assign Destination Cluster Nodes . If you select the Enter new network settings for one or more destination
                                                               					 nodes option, only source hostname appears and not the destination
                                                            				  hostname on the Assign Destination Cluster Nodes window. | Note | If you
                                                            				  select the Use the source node network settings for all destination
                                                               					 nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns Assign Destination Cluster Nodes . If you select the Enter new network settings for one or more destination
                                                               					 nodes option, only source hostname appears and not the destination
                                                            				  hostname on the Assign Destination Cluster Nodes window. |
| Note | If you
                                                            				  select the Use the source node network settings for all destination
                                                               					 nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns Assign Destination Cluster Nodes . If you select the Enter new network settings for one or more destination
                                                               					 nodes option, only source hostname appears and not the destination
                                                            				  hostname on the Assign Destination Cluster Nodes window. |
| Step 4 | Click Next . The Assign
                                                				Destination Cluster Nodes window appears. |
| Step 5 | Click Assign Destination Cluster Nodes to select the destination virtual machine for each source node. Note If DHCP is in use on your source node, the destination node will also be configured to use DHCP, and you will not have the
                                                            option of changing your network settings in this wizard. The Configure Destination Cluster window appears. | Note | If DHCP is in use on your source node, the destination node will also be configured to use DHCP, and you will not have the
                                                            option of changing your network settings in this wizard. |
| Note | If DHCP is in use on your source node, the destination node will also be configured to use DHCP, and you will not have the
                                                            option of changing your network settings in this wizard. |
| Step 6 | Select a
                                             			 virtual machine, click Next
                                                				Node to go to the next node in the cluster, and select another
                                             			 virtual machine for the destination virtual machine, and click Done . Note If there
                                                            				  is more than one node in the cluster, repeat these steps - (assigning VM, and
                                                            				  entering new IP/hostname settings, if needed) for each node in the source
                                                            				  cluster. | Note | If there
                                                            				  is more than one node in the cluster, repeat these steps - (assigning VM, and
                                                            				  entering new IP/hostname settings, if needed) for each node in the source
                                                            				  cluster. |
| Note | If there
                                                            				  is more than one node in the cluster, repeat these steps - (assigning VM, and
                                                            				  entering new IP/hostname settings, if needed) for each node in the source
                                                            				  cluster. |
| Step 7 | Click Next . The Configure NTP/SMTP Settings window appears. |
| Step 8 | Enter the
                                             			 Network Time Protocol (NTP) server settings to be applied to the migration
                                             			 nodes when the migration task runs, and optionally, enter the SMTP server
                                             			 settings. Important In a proxy
                                                            				  TFTP setup, if a network migration is performed "off-cluster", you need to
                                                            				  manually configure the new hostname and IP address of that off-cluster in the
                                                            				  proxy TFTP. Off-cluster refers to situations where TFTP functionality is being
                                                            				  performed by a proxy that is not part of that specific Unified Communications
                                                            				  Manager cluster. During a migration, that TFTP server (that is not part of the
                                                            				  cluster) is not modified. If you want to change the hostname or IP address of
                                                            				  that server, you must do it as a separate process and not with Cisco Prime
                                                            				  Collaboration Deployment. | Important | In a proxy
                                                            				  TFTP setup, if a network migration is performed "off-cluster", you need to
                                                            				  manually configure the new hostname and IP address of that off-cluster in the
                                                            				  proxy TFTP. Off-cluster refers to situations where TFTP functionality is being
                                                            				  performed by a proxy that is not part of that specific Unified Communications
                                                            				  Manager cluster. During a migration, that TFTP server (that is not part of the
                                                            				  cluster) is not modified. If you want to change the hostname or IP address of
                                                            				  that server, you must do it as a separate process and not with Cisco Prime
                                                            				  Collaboration Deployment. |
| Important | In a proxy
                                                            				  TFTP setup, if a network migration is performed "off-cluster", you need to
                                                            				  manually configure the new hostname and IP address of that off-cluster in the
                                                            				  proxy TFTP. Off-cluster refers to situations where TFTP functionality is being
                                                            				  performed by a proxy that is not part of that specific Unified Communications
                                                            				  Manager cluster. During a migration, that TFTP server (that is not part of the
                                                            				  cluster) is not modified. If you want to change the hostname or IP address of
                                                            				  that server, you must do it as a separate process and not with Cisco Prime
                                                            				  Collaboration Deployment. |
| Step 9 | Click Next . The Define DNS Settings window appears. |
| Step 10 | To change the
                                             			 DNS setting for a node, select the node or nodes from the table and click Assign
                                                				DNS Settings . Enter the primary and secondary DNS, then click OK to apply the changes. Important You cannot
                                                            				  change the domain name during a migration. | Important | You cannot
                                                            				  change the domain name during a migration. |
| Important | You cannot
                                                            				  change the domain name during a migration. |
| Step 11 | Click Finish . The changes
                                                				are saved and a row is added to the clusters table to reflect the new migration
                                                				cluster that you have created. |

| Note | If you
                                                            				  select the Use the source node network settings for all destination
                                                               					 nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns Assign Destination Cluster Nodes . If you select the Enter new network settings for one or more destination
                                                               					 nodes option, only source hostname appears and not the destination
                                                            				  hostname on the Assign Destination Cluster Nodes window. |
|---|---|

| Note | If DHCP is in use on your source node, the destination node will also be configured to use DHCP, and you will not have the
                                                            option of changing your network settings in this wizard. |
|---|---|

| Note | If there
                                                            				  is more than one node in the cluster, repeat these steps - (assigning VM, and
                                                            				  entering new IP/hostname settings, if needed) for each node in the source
                                                            				  cluster. |
|---|---|

| Important | In a proxy
                                                            				  TFTP setup, if a network migration is performed "off-cluster", you need to
                                                            				  manually configure the new hostname and IP address of that off-cluster in the
                                                            				  proxy TFTP. Off-cluster refers to situations where TFTP functionality is being
                                                            				  performed by a proxy that is not part of that specific Unified Communications
                                                            				  Manager cluster. During a migration, that TFTP server (that is not part of the
                                                            				  cluster) is not modified. If you want to change the hostname or IP address of
                                                            				  that server, you must do it as a separate process and not with Cisco Prime
                                                            				  Collaboration Deployment. |
|---|---|

| Important | You cannot
                                                            				  change the domain name during a migration. |
|---|---|

| Important | When the migration cluster is created, you must indicate whether all destination nodes will keep the same hostname or IP address,
                                             or if some of these addresses will be changing. Using the source node settings for the all destination nodes option is referred to as a “simple migration” in the "Migration Procedure Flow Charts" section. Entering new network settings for one or more destination nodes option is referred as "network migration" in the "Migration Procedure Flow Charts" section. |
|---|---|

| Unified CM source cluster - from Release | Simple Migration or Network Migration | Unified CM source cluster - (secure or nonsecure) | User procedures to be performed during migration |
|---|---|---|---|
| 10.x | Simple migration | Secure | No steps required during migration. |
| 10.x | Simple migration | Nonsecure | No steps required during migration. |
| 10.x | Network migration | Secure | When the migration task reaches the Forced Paused step, perform the following steps: CTL Update Bulk Certificate Management Resume the task on Cisco Prime Collaboration Deployment GUI. |
| 10.x | Network migration | Nonsecure | When the migration task reaches the Forced Paused step, perform the following steps: Bulk Certificate Management Resume the task on Cisco Prime Collaboration Deployment GUI. |
| 11.x, 12.x, 14 and SUs, and 15 | Simple migration | Secure | No steps are required during migration. |
| 11.x, 12.x, 14 and SUs, and 15 | Simple migration | Nonsecure | No steps are required during migration. |
| 11.x, 12.x, 14 and SUs, and 15 | Network migration | Secure | When the migration task reaches the Forced Paused step, perform the following steps: CTL Update Bulk Certificate Management Resume the task on Cisco Prime Collaboration Deployment GUI. |
| 11.x, 12.x, 14 and SUs, and 15 | Network migration | Nonsecure | When the migration task reaches the Forced Paused step, perform the following steps: Bulk Certificate Management Resume the task on Cisco Prime Collaboration Deployment GUI. |

| Unified CM source cluster—from Release | Simple Migration or Network Migration | Unified CM source cluster (Secure or Non-secure) | User procedures to be performed after migration |
|---|---|---|---|
| 10.x | Network migration | Secure | Change TFTP Server IP Address. Verify Phone Registration. |
| Network migration | Nonsecure | Change TFTP Server IP Address. Verify Phone Registration. |
| 11.x, 12.x, 14 and SUs, and 15 | Network Migration | Secure | Change TFTP Server IP Address. Verify Phone Registration. |
| Network Migration | Nonsecure | Change TFTP Server IP Address. Verify Phone Registration. |

| Note | Device default settings will not be carried over from source cluster to destination cluster after a simple or network migration
                                                task. Any device packs installed for specific features need to be reinstalled if destination cluster version doesn't already include
                                                the device pack feature. |
|---|---|

| Note | After migration, reinstall all COP files for any country locale that you are using. COP files may be reinstalled through PCD
                                             Upgrade Task or Unified Communications Manager OS Admin or CLI. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure
                                             			 certificates and certificate trust stores. | If the old cluster had
                                             			 CA-signed certificates in any of the component trust stores, be aware that the
                                             			 components contain self-signed certificates on the migrated Release 10.x
                                             			 cluster. Also, the
                                             			 root and intermediate certificates of the Certificate Authority are not
                                             			 preserved in their respective trust stores. You should sign the certificates
                                             			 with the old Certificate Authority, similar to how it would have been done
                                             			 initially. For more information, see the Administration Guide for Cisco Unified Communications Manager
                                                   				  Guide . |
| Step 2 | Configure
                                             			 intercluster peers. | If the old
                                             			 cluster had an intercluster peer relationship, you need to delete the
                                             			 configuration from all peer clusters. Once this is done, add the appropriate
                                             			 interclustering based on the network details of the new cluster. For example,
                                             			 Cluster A, Cluster B, and Cluster C are all intercluster peers. If Cluster A
                                             			 was migrated, then you should delete all interclustering configuration from the
                                             			 old Cluster A and likewise Cluster A from Cluster B and Cluster C and then add
                                             			 interclustering with the network details of the new Cluster A. You do not need
                                             			 to configure anything from the new Cluster A since the migration brings over
                                             			 the old data. For more
                                             			 information, see Deployment
                                                				Guide for IM and Presence Service on Cisco Unified Communications
                                                				Manager. |
| Step 3 | Re-publish SIP
                                             			 Federation. | If the old cluster was front-ending SIP Interdomain with Microsoft OCS/Lync/AOL or SIP Intradomain federation with OCS/Lync,
                                             then your enterprise needs to re-publish the DNS-SRV of your federating domain to reflect the new network details. If the far side has SIP static routes that are configured instead of DNS-SRV based routing, then the SIP static routes need
                                             to be changed to reflect the new network address. Similarly, all intermediate network elements (including ASA or any other
                                             similar components that route or inspect traffic to the old cluster from the external federation entities) need to be re-configured
                                             for successful routing to the new cluster. For
                                             			 Interdomain configuration, see Interdomain
                                                				Federation for IM and Presence Service on Cisco Unified Communications
                                                				Manager . For
                                             			 Intradomain federation, see Partitioned
                                                				Intradomain Federation for IM and Presence Service on Cisco Unified
                                                				Communications Manager . |
| Step 4 | Re-publish
                                             			 XMPP Federation. | If the old cluster was front-ending XMPP Interdomain federation to any external XMPP servers, then your enterprise needs to
                                             republish your federating domain's DNS-SRV records to reflect the new network details. For more information, see Interdomain Federation for IM and Presence Service on Cisco Unified Communications Manager . |
| Step 5 | Configure
                                             			 Cisco Jabber/Cisco Unified Personal Communicator connectivity. | Jabber or
                                             			 Unified Personal Communicator caches the hostname information from the old
                                             			 cluster and does not have new hostname information unless you are able to push
                                             			 the configuration to the desktop of the user, or that user manually enters one
                                             			 of the node names. A fail safe approach for users that are unassigned from the old cluster, and as a result are unable to log in, involves the
                                             user manually entering the hostname or IP address of one of the nodes in the new cluster (of which they were informed before
                                             migration). In this scenario, the user's client finds the right home node by way of redirected login. |

| Note | Cisco Prime Collaboration Deployment does not support migration of
                                                			 Business Edition 5000 Appliance running on MCS 7828H3. |
|---|---|

| Step 1 | Enter the following CLI
                                          			 command at the command prompt: utils service list . The following output appears: Requesting service status, please wait...
System SSH [STARTED] 
Cluster Manager [STOPPED] |
|---|---|
| Step 2 | If Cluster Manager Service status is STOPPED, type the following
                                          			 command to start the service on the old subscriber node: utils service start Cluster Manager |

| Note | If you made updates to the cluster post the time of discovery, you need to re-discover the cluster before upgrade so that
                                       Cisco Prime Collaboration Deployment has the latest and most accurate view of the recent changes. |
|---|---|

| Note | If your Cisco Prime Collaboration Deployment is in FIPS mode and you are using any of the Pre-12.5 UC clusters to perform
                                       an upgrade, you must first switch your Cisco Prime Collaboration Deployment to work in the non-FIPS mode before proceeding
                                       with the upgrade. |
|---|---|

| Note | Based on the source version and destination version you choose, Cisco Prime Collaboration Deployment uses either direct standard
                                             upgrade sequence or validation, or direct refresh upgrade sequence or validation. |
|---|---|

| Note | Before upgrading the cluster, Cisco recommends to install the latest Upgrade Readiness COP file. Refer to the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service for details. This is applicable if the source cluster is 9.X or above and valid only for Unified Communications Manager
                                                and IM&P. |
|---|---|

| Step 1 | Click Open and close navigation and choose Task > Upgrade from the main menu. |
|---|---|
| Step 2 | Click Add
                                                				Upgrade Task . |
| Step 3 | In the Specify Task Name drop-down, enter a name for the upgrade task in Choose a Nickname for this Upgrade Task . |
| Step 4 | Select the upgrade type as ISO or COP . You can install multiple cops files in a single upgrade task. Note If the user select the multiple cop files for upgrade then the task sequence will load up according to the selected COP files. Note Maximum 32 COP files can be selected for a specific product. | Note | If the user select the multiple cop files for upgrade then the task sequence will load up according to the selected COP files. | Note | Maximum 32 COP files can be selected for a specific product. |
| Note | If the user select the multiple cop files for upgrade then the task sequence will load up according to the selected COP files. |
| Note | Maximum 32 COP files can be selected for a specific product. |
| Step 5 | From the Cluster drop-down list, select the cluster on which
                                             			 the nodes to be upgraded are located. |
| Step 6 | If you want to make the newly created task as dependent on the successful completion of another previously executed task,
                                             check the checkbox of the tasks listed in the Task Dependency Scheduling . You can select multiple tasks as dependent tasks. If you do not want to make any dependency, check the No Dependency checkbox. You can make an upgrade ISO task dependent on an upgrade task only. You can make an upgrade COP task dependent on Install and Migration task. |
| Step 7 | Select the
                                             			 nodes that are part of the upgrade from the list of nodes. |
| Step 8 | Click Next . Note The Next button is dimmed if no nodes are selected. | Note | The Next button is dimmed if no nodes are selected. |
| Note | The Next button is dimmed if no nodes are selected. |
| Step 9 | Click the
                                             			 respective Browse buttons to select the upgrade files from the
                                             			 file server. Note The option
                                                            				  to select upgrade files is available only for the selected product types and
                                                            				  applications that are currently supported in the cluster. | Note | The option
                                                            				  to select upgrade files is available only for the selected product types and
                                                            				  applications that are currently supported in the cluster. |
| Note | The option
                                                            				  to select upgrade files is available only for the selected product types and
                                                            				  applications that are currently supported in the cluster. |
| Step 10 | Select a valid upgrade file or files. Note Click Show drop-down list to see all the available upgrade files on the file server. Note To create an upgrade task, while selecting ISO /COP files, ensure that the ISO /COP files are common across all the required SFTP servers which are associated to cluster nodes. If the ISO /COP files are not common to all the required SFTP servers which are associated to cluster nodes, the valid files do not appear
                                                         even though they are valid for upgrade. To view all the ISO /COP files, from the Show drop-down list, choose All . Note When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. | Note | Click Show drop-down list to see all the available upgrade files on the file server. | Note | To create an upgrade task, while selecting ISO /COP files, ensure that the ISO /COP files are common across all the required SFTP servers which are associated to cluster nodes. If the ISO /COP files are not common to all the required SFTP servers which are associated to cluster nodes, the valid files do not appear
                                                         even though they are valid for upgrade. To view all the ISO /COP files, from the Show drop-down list, choose All . | Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
| Note | Click Show drop-down list to see all the available upgrade files on the file server. |
| Note | To create an upgrade task, while selecting ISO /COP files, ensure that the ISO /COP files are common across all the required SFTP servers which are associated to cluster nodes. If the ISO /COP files are not common to all the required SFTP servers which are associated to cluster nodes, the valid files do not appear
                                                         even though they are valid for upgrade. To view all the ISO /COP files, from the Show drop-down list, choose All . |
| Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
| Step 11 | Click Choose
                                                				File . |
| Step 12 | Click Next . Note The Next button is dimmed if no valid upgrade files are selected. | Note | The Next button is dimmed if no valid upgrade files are selected. |
| Note | The Next button is dimmed if no valid upgrade files are selected. |
| Step 13 | Select the date and time when you want the upgrade task to begin. You have the following options to schedule upgrades: If the task is created as depended task, then Set Start Time section is disabled. Note Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. Select Schedule for a specific time to enter the date and time when you want the upgrade task to start. The start time that you set is based on the time zone
                                                of the Cisco Prime Collaboration Deployment server as denoted by the time zone that is displayed with this option. Note If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. Select Start task manually to keep the task in a manual start. Note If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page. Select Start task immediately upon completion of this wizard to start the task immediately after you click Finish . If you want the system to automatically switch to the new version, choose the option Upgrade Option to Automatically Switch to New Version after Successful Upgrade . Otherwise, the server, or servers, are upgraded but remain on the current version of software. In that case, you can schedule
                                                a switch version task to switch over to the upgraded version of software. | Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. | Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. | Note | If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page. |
| Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. |
| Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. |
| Note | If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page. |
| Step 14 | Click Next . |
| Step 15 | Specify the
                                             			 sequence of steps to complete the task. You have the following options: Option Description Pencil
                                                      				  icon Edit a
                                                         					 step. Page icon Add a new
                                                         					 step after the current step. X mark Delete the
                                                         					 current step. If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the publisher
                                                         node. Up arrow Move the
                                                         					 step up to be performed earlier. Down
                                                      				  arrow Move the
                                                         					 step down to be performed later. The Pencil icon opens up an Edit Step window. Add nodes to be upgraded in this
                                                				step from the list of available nodes. The available nodes are the ones that
                                                				you chose for an upgrade. The step to which each node
                                                				is assigned displays next to the node. If a node is not assigned to any step,
                                                				it shows as unassigned. When you assign all the nodes to a step, a default sequencing is available. Important You cannot proceed to next step until you assign all the nodes. The Pause task after step completes option pauses the task after completion of this step. Manually start the next step to complete the task. | Option | Description | Pencil
                                                      				  icon | Edit a
                                                         					 step. | Page icon | Add a new
                                                         					 step after the current step. | X mark | Delete the
                                                         					 current step. If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the publisher
                                                         node. | Up arrow | Move the
                                                         					 step up to be performed earlier. | Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. | Important | You cannot proceed to next step until you assign all the nodes. |
| Option | Description |
| Pencil
                                                      				  icon | Edit a
                                                         					 step. |
| Page icon | Add a new
                                                         					 step after the current step. |
| X mark | Delete the
                                                         					 current step. If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the publisher
                                                         node. |
| Up arrow | Move the
                                                         					 step up to be performed earlier. |
| Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. |
| Important | You cannot proceed to next step until you assign all the nodes. |
| Step 16 | Click OK . |
| Step 17 | Click Next . Note The Next button remains enabled, which allows you to click to display any configuration errors. | Note | The Next button remains enabled, which allows you to click to display any configuration errors. |
| Note | The Next button remains enabled, which allows you to click to display any configuration errors. |
| Step 18 | See the Review section to verify the details of the task you created. You can add notes for the task, if necessary. The notes are saved
                                             with the task and are visible if the task is edited before completion. |
| Step 19 | Click Finish to schedule the task. |

| Note | If the user select the multiple cop files for upgrade then the task sequence will load up according to the selected COP files. |
|---|---|

| Note | Maximum 32 COP files can be selected for a specific product. |
|---|---|

| Note | The Next button is dimmed if no nodes are selected. |
|---|---|

| Note | The option
                                                            				  to select upgrade files is available only for the selected product types and
                                                            				  applications that are currently supported in the cluster. |
|---|---|

| Note | Click Show drop-down list to see all the available upgrade files on the file server. |
|---|---|

| Note | To create an upgrade task, while selecting ISO /COP files, ensure that the ISO /COP files are common across all the required SFTP servers which are associated to cluster nodes. If the ISO /COP files are not common to all the required SFTP servers which are associated to cluster nodes, the valid files do not appear
                                                         even though they are valid for upgrade. To view all the ISO /COP files, from the Show drop-down list, choose All . |
|---|---|

| Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
|---|---|

| Note | The Next button is dimmed if no valid upgrade files are selected. |
|---|---|

| Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. |
|---|---|

| Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. |
|---|---|

| Note | If you choose to start the task manually, a task is created, but does not start until you click the Start task button on the Monitoring page, or the Start task link on the task page. |
|---|---|

| Option | Description |
|---|---|
| Pencil
                                                      				  icon | Edit a
                                                         					 step. |
| Page icon | Add a new
                                                         					 step after the current step. |
| X mark | Delete the
                                                         					 current step. If you remove all the nodes from a step, the step is removed by default. You cannot remove a step that contains the publisher
                                                         node. |
| Up arrow | Move the
                                                         					 step up to be performed earlier. |
| Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. |

| Important | You cannot proceed to next step until you assign all the nodes. |
|---|---|

| Note | The Next button remains enabled, which allows you to click to display any configuration errors. |
|---|---|

| Note | Direct Refresh to Release 15 is not supported. See Supported Tasks for Applications and Versions for information on the supported upgrade and migration tasks. |
|---|---|

| Note | Cisco Prime Collaboration Deployment checks the database replication when you choose the cluster that is combined with Cisco
                                             Unified Communications Manager and IM and Presence Service. The database replication runs only for Cisco Unified Communications
                                             Manager before the IM and Presence Service upgrade or switch. |
|---|---|

| Note | The Automatic Switch version option is not available on clusters which contain Unity Connection and Cisco Unified Contact
                                                Center Express nodes. For clusters with Cisco Unity Connection and Cisco Unified Contact Center Express, create an upgrade
                                                task and then create a switch version task to switch to the new version. You can create the switch version task after the
                                                upgrade task runs successfully. |
|---|---|

| Step 1 | Click Open and close navigation and choose Tasks > Switch Versions from the main menu. |
|---|---|
| Step 2 | Click Add
                                                				Switch Versions Task . |
| Step 3 | In the Specify Task Name drop-down, enter a name for the switch version task in Choose a Nickname for this Switch Versions Task . |
| Step 4 | From the Cluster drop-down list, select the cluster on which
                                             			 you want to switch the versions. |
| Step 5 | Select the
                                             			 version to which you want all the nodes to be switched. Note If there is
                                                            				  more than one product, you can select the applicable versions of all the
                                                            				  different products. You also can choose to switch the version for one product
                                                            				  and to not switch the version for another product. | Note | If there is
                                                            				  more than one product, you can select the applicable versions of all the
                                                            				  different products. You also can choose to switch the version for one product
                                                            				  and to not switch the version for another product. |
| Note | If there is
                                                            				  more than one product, you can select the applicable versions of all the
                                                            				  different products. You also can choose to switch the version for one product
                                                            				  and to not switch the version for another product. |
| Step 6 | Click Next . |
| Step 7 | Select the
                                             			 date and time when you want the switch versions task to begin. You have the
                                             			 following options to schedule switch versions task: Select Schedule for a specific time to enter the date and
                                                				time when you want the switch versions task to start. Any start time that you
                                                				set is based on the time zone of the Cisco Prime Collaboration Deployment
                                                				server as denoted by the time zone that is displayed with this option. Note If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically. Select Start task manually to keep the task in a manual
                                                				start. Select Start task immediately upon completion of this wizard to start the task immediately after you click Finish . Note You can also start the task from the Monitoring page. If you want the server to
                                                				automatically switch to the new version, check the check box next to Automatically switch to new version after successful
                                                   				  upgrade . | Note | If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically. | Note | You can also start the task from the Monitoring page. |
| Note | If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically. |
| Note | You can also start the task from the Monitoring page. |
| Step 8 | Click Next . |
| Step 9 | Specify the
                                             			 sequence of steps to complete the task. You have the following options: Option Description Pencil
                                                      				  icon Edit a
                                                         					 step. Page icon Add a new
                                                         					 step after the current step. X mark Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. Up arrow Move the
                                                         					 step up to be performed earlier. Down
                                                      				  arrow Move the
                                                         					 step down to be performed later. The Pencil icon opens up an Edit Step window. Add the nodes on which the versions
                                                				must be switched in this step from the list of available nodes. The available
                                                				nodes are the ones that you chose for the switch versions task. The step to which each node
                                                				is assigned displays next to the node. If a node is not assigned to any step,
                                                				it shows as unassigned. When you assign all the nodes to a step, a default sequencing is available. Important You cannot proceed to next step until you assign all the nodes. The Pause task after step completes option pauses the
                                                				task after completion of this step. You must manually start the next step to
                                                				complete the task. | Option | Description | Pencil
                                                      				  icon | Edit a
                                                         					 step. | Page icon | Add a new
                                                         					 step after the current step. | X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. | Up arrow | Move the
                                                         					 step up to be performed earlier. | Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. | Important | You cannot proceed to next step until you assign all the nodes. |
| Option | Description |
| Pencil
                                                      				  icon | Edit a
                                                         					 step. |
| Page icon | Add a new
                                                         					 step after the current step. |
| X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. |
| Up arrow | Move the
                                                         					 step up to be performed earlier. |
| Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. |
| Important | You cannot proceed to next step until you assign all the nodes. |
| Step 10 | Click OK . |
| Step 11 | Click Next . Note The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors. | Note | The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors. |
| Note | The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors. |
| Step 12 | Use the Review section to verify the details of the task
                                             			 that you created. You can add notes for the task if required. The notes are
                                             			 saved with the task and are visible if the task is edited before completion. |
| Step 13 | Click Finish to schedule the task. |

| Note | If there is
                                                            				  more than one product, you can select the applicable versions of all the
                                                            				  different products. You also can choose to switch the version for one product
                                                            				  and to not switch the version for another product. |
|---|---|

| Note | If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically. |
|---|---|

| Note | You can also start the task from the Monitoring page. |
|---|---|

| Option | Description |
|---|---|
| Pencil
                                                      				  icon | Edit a
                                                         					 step. |
| Page icon | Add a new
                                                         					 step after the current step. |
| X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. |
| Up arrow | Move the
                                                         					 step up to be performed earlier. |
| Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. |

| Important | You cannot proceed to next step until you assign all the nodes. |
|---|---|

| Note | The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors. |
|---|---|

| Step 1 | Click the
                                             			 open and close navigation button and choose Task > Server
                                                   				  Restart from the main menu. |
|---|---|
| Step 2 | Click Add
                                                				Server Restart Task . The
                                             			 Add Restart Task wizard appears. |
| Step 3 | In the Specify Task Name drop-down, enter a name for the server restart task in Choose a Nickname for this Server Restart Task . |
| Step 4 | From the Clusters drop-down list, select the cluster on which
                                             			 you want to restart the nodes. |
| Step 5 | If you want to make the newly created restart task as dependent on the successful completion of another previously created
                                             upgrade task, check the checkbox of the tasks listed in the Task Dependency Scheduling. You can select multiple tasks as dependent tasks. If you do not want to make any dependency, check the No Dependency checkbox. |
| Step 6 | From the
                                             			 table, select the nodes to be restarted. If you do not select any nodes, you
                                             			 cannot continue. |
| Step 7 | Click Next . |
| Step 8 | Select the
                                             			 date and time when you want the server restart task to begin. You have the
                                             			 following options to schedule restart tasks: If the task is created as depended task, then Set Start Time section is disabled. Note Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. Select Schedule for a specific time to enter the date and
                                                				time when you want the restart task to start. Any start time that you set is
                                                				based on the time zone of the Cisco Prime Collaboration Deployment server. Note If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically. Select Start the task manually to keep the task in a manual
                                                				start. Select Start task immediately upon completion of the wizard to start the task immediately after you click Finish . Note You can
                                                               					 also start the task from the Monitoring page. | Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. | Note | If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically. | Note | You can
                                                               					 also start the task from the Monitoring page. |
| Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. |
| Note | If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically. |
| Note | You can
                                                               					 also start the task from the Monitoring page. |
| Step 9 | Click Next . |
| Step 10 | Specify the
                                             			 sequence of steps to complete the task. You have the following options: Option Description Pencil
                                                      				  icon Edit a
                                                         					 step. Page icon Add a new
                                                         					 step after the current step. X mark Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. Up arrow Move the
                                                         					 step up to be prepared earlier. Down
                                                      				  arrow Move the
                                                         					 step down to be prepared later. The Pencil icon opens up an Edit
                                                   				  Step window. In this step, add nodes to be restarted from the list
                                                				of available nodes. The available nodes are the ones that you chose for a
                                                				restart. The step to which each node
                                                				is assigned appears next to the node. If a node is not assigned to any step,
                                                				that node shows as unassigned. When you assign all the nodes to a step, a default sequencing is available. Important You cannot proceed to the next step until you assign all the nodes. The Pause task after step completes option pauses the
                                                				task after completion of this step. You must manually start the next step to
                                                				complete the task. | Option | Description | Pencil
                                                      				  icon | Edit a
                                                         					 step. | Page icon | Add a new
                                                         					 step after the current step. | X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. | Up arrow | Move the
                                                         					 step up to be prepared earlier. | Down
                                                      				  arrow | Move the
                                                         					 step down to be prepared later. | Important | You cannot proceed to the next step until you assign all the nodes. |
| Option | Description |
| Pencil
                                                      				  icon | Edit a
                                                         					 step. |
| Page icon | Add a new
                                                         					 step after the current step. |
| X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. |
| Up arrow | Move the
                                                         					 step up to be prepared earlier. |
| Down
                                                      				  arrow | Move the
                                                         					 step down to be prepared later. |
| Important | You cannot proceed to the next step until you assign all the nodes. |
| Step 11 | Click OK . |
| Step 12 | Click Next . Note The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors. | Note | The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors. |
| Note | The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors. |
| Step 13 | See the Review section to verify the details of the task you
                                             			 created. You can add notes for the task if required. The notes are saved with
                                             			 the task and are visible if the task is edited before completion. |
| Step 14 | Click Finish to schedule the task. |

| Note | Cisco Prime Collaboration Deployment does not allow you to select the date and time for the dependent tasks, as the dependent
                                                            task starts automatically after the successful completion of the existing task. |
|---|---|

| Note | If you
                                                               					 schedule a task for a few minutes in the future, but do not save it until that
                                                               					 scheduled time passes, then the task will start automatically. |
|---|---|

| Note | You can
                                                               					 also start the task from the Monitoring page. |
|---|---|

| Option | Description |
|---|---|
| Pencil
                                                      				  icon | Edit a
                                                         					 step. |
| Page icon | Add a new
                                                         					 step after the current step. |
| X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. |
| Up arrow | Move the
                                                         					 step up to be prepared earlier. |
| Down
                                                      				  arrow | Move the
                                                         					 step down to be prepared later. |

| Important | You cannot proceed to the next step until you assign all the nodes. |
|---|---|

| Note | The Next button remains enabled, which allows the user
                                                            				  to click to be informed of any configuration errors. |
|---|---|

| Note | Cisco Prime Collaboration Deployment does not support changing the FQDN, only hostnames. |
|---|---|

| Step 1 | Click the open and close navigation button and choose Task > Readdress from the main menu. |
|---|---|
| Step 2 | Click Add Readdress Task . |
| Step 3 | In the Specify Task Name drop-down, enter a name for the readdress task in Choose a Nickname for this Readdress Task . |
| Step 4 | From the Cluster drop-down list, select the cluster on which you want to change the address of the nodes. Click View Nodes to view the Cluster nodes. |
| Step 5 | Click Next . |
| Step 6 | Click Edit next to a node to enter an alternate Hostname, IP Address, Subnet Mask or Gateway. Note If DHCP is configured for a cluster, you cannot edit using the readdress task. | Note | If DHCP is configured for a cluster, you cannot edit using the readdress task. |
| Note | If DHCP is configured for a cluster, you cannot edit using the readdress task. |
| Step 7 | Click OK . |
| Step 8 | Click Next . Important When you click Next , Cisco Prime Collaboration Deployment performs a validation test automatically. If the test on a cluster fails, the error
                                                            message describes the failed test. You can continue to create the tasks, but you must resolve the errors described or the
                                                            task fails. | Important | When you click Next , Cisco Prime Collaboration Deployment performs a validation test automatically. If the test on a cluster fails, the error
                                                            message describes the failed test. You can continue to create the tasks, but you must resolve the errors described or the
                                                            task fails. |
| Important | When you click Next , Cisco Prime Collaboration Deployment performs a validation test automatically. If the test on a cluster fails, the error
                                                            message describes the failed test. You can continue to create the tasks, but you must resolve the errors described or the
                                                            task fails. |
| Step 9 | Select the date and time when you want the readdress task to begin. You have the following options to schedule readdress tasks: Select Schedule for a specific time to enter the date and time when you want the readdress task to start. Any start time that you set is based on the time zone
                                                of the Cisco Prime Collaboration Deployment server as denoted by the time zone that is displayed with this option. Note If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. Select Start task manually to keep the task in a manual start. Select Start task immediately upon completion of wizard to start the task immediately afer you click Finish . Note You can also start the task from the Monitoring page. | Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. | Note | You can also start the task from the Monitoring page. |
| Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. |
| Note | You can also start the task from the Monitoring page. |
| Step 10 | Click Next . |
| Step 11 | Specify the sequence of steps to complete the task. You have the following options here: Option Description Pencil icon Edit a step. Page icon Add a new step after the current step. Up arrow Move the step up to be executed earlier. Down arrow Move the step down to be executed later. The Pencil icon opens up an Edit Step window. Add nodes to be readdressed in this step from the list of available nodes. The available nodes are the ones that
                                                you chose for a readdress. Note IM and Presence Service nodes do not have an Edit button, since readdress is not supported on Cisco Prime Collaboration Deployment for IM and Presence Service servers. The step to which each node is assigned displays next to the node. If a node is not assigned to any step, it shows as unassigned. When you assign all the nodes to a step, there will be a default sequencing available. Important You cannot proceed to next step until you assign all the nodes that were selected for this task. Cisco Prime Collaboration Deployment automatically inserts a Forced Pause after each sequence step in a Readdress task. For a readdress task, only one node can be assigned to each step. Multiple nodes cannot be combined and assigned in a single
                                                step. | Option | Description | Pencil icon | Edit a step. | Page icon | Add a new step after the current step. | Up arrow | Move the step up to be executed earlier. | Down arrow | Move the step down to be executed later. | Note | IM and Presence Service nodes do not have an Edit button, since readdress is not supported on Cisco Prime Collaboration Deployment for IM and Presence Service servers. | Important | You cannot proceed to next step until you assign all the nodes that were selected for this task. |
| Option | Description |
| Pencil icon | Edit a step. |
| Page icon | Add a new step after the current step. |
| Up arrow | Move the step up to be executed earlier. |
| Down arrow | Move the step down to be executed later. |
| Note | IM and Presence Service nodes do not have an Edit button, since readdress is not supported on Cisco Prime Collaboration Deployment for IM and Presence Service servers. |
| Important | You cannot proceed to next step until you assign all the nodes that were selected for this task. |
| Step 12 | Click OK . |
| Step 13 | Click Next . Note The Next button remains enabled, which allows the user to click to be informed of any configuration errors. | Note | The Next button remains enabled, which allows the user to click to be informed of any configuration errors. |
| Note | The Next button remains enabled, which allows the user to click to be informed of any configuration errors. |
| Step 14 | See the Review section to verify the details of the task you created. You can add notes for the task if required. The notes are saved with
                                             the task and are visible if the task is edited before completion. |
| Step 15 | Click Finish to schedule the task. |

| Note | If DHCP is configured for a cluster, you cannot edit using the readdress task. |
|---|---|

| Important | When you click Next , Cisco Prime Collaboration Deployment performs a validation test automatically. If the test on a cluster fails, the error
                                                            message describes the failed test. You can continue to create the tasks, but you must resolve the errors described or the
                                                            task fails. |
|---|---|

| Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. |
|---|---|

| Note | You can also start the task from the Monitoring page. |
|---|---|

| Option | Description |
|---|---|
| Pencil icon | Edit a step. |
| Page icon | Add a new step after the current step. |
| Up arrow | Move the step up to be executed earlier. |
| Down arrow | Move the step down to be executed later. |

| Note | IM and Presence Service nodes do not have an Edit button, since readdress is not supported on Cisco Prime Collaboration Deployment for IM and Presence Service servers. |
|---|---|

| Important | You cannot proceed to next step until you assign all the nodes that were selected for this task. |
|---|---|

| Note | The Next button remains enabled, which allows the user to click to be informed of any configuration errors. |
|---|---|

| Important | Before running a
                                                			 readdress task, you may need to perform certain steps (for example, updating
                                                			 entries on the DNS server). It is very important that
                                                			 you read Administration Guide for Cisco Unified Communications
                                                   				Manager before you run the readdress task. |
|---|---|

| Step 1 | VMware—Deploy the hardware for the new cluster and install ESXi. Note Make sure that the host with the Cisco Prime Collaboration Deployment VM and the host with the application VMs use the required
                                                            Virtualization Software License. See Add an ESXi Host Server . | Note | Make sure that the host with the Cisco Prime Collaboration Deployment VM and the host with the application VMs use the required
                                                            Virtualization Software License. See Add an ESXi Host Server . |
|---|---|---|---|
| Note | Make sure that the host with the Cisco Prime Collaboration Deployment VM and the host with the application VMs use the required
                                                            Virtualization Software License. See Add an ESXi Host Server . |
| Step 2 | ISO files—Download the necessary OVA and ISO images for target release, and use SFTP transfer the ISO files to the /fresh_install directory of Cisco Prime Collaboration Deployment. Note The ISO file must be bootable. Note Do not edit the file name of the bootable ISO that is being used for a PCD task. | Note | The ISO file must be bootable. | Note | Do not edit the file name of the bootable ISO that is being used for a PCD task. |
| Note | The ISO file must be bootable. |
| Note | Do not edit the file name of the bootable ISO that is being used for a PCD task. |
| Step 3 | VMware—Deploy Cisco-recommended OVA to create the VMs for the nodes to be installed. Create the appropriate number of target
                                             virtual machines on your ESXi hosts (one new virtual machine for each server to be installed in the cluster) using the Cisco
                                             OVAs that you downloaded in Step 2. Configure the network settings on new VMs. |
| Step 4 | Cisco Prime Collaboration Deployment GUI—Add the ESXi Hosts that contain your virtual machines to the Cisco Prime Collaboration
                                             Deployment inventory. For information about adding and ESXi host to Cisco Prime Collaboration Deployment, see Add an ESXi Host Server . |
| Step 5 | Cisco Prime Collaboration Deployment GUI—Define the new installation cluster (click the open and close navigation button and
                                             choose Inventory > Clusters ) to define the nodes to be installed, and their associated virtual machines. (See Add New Cluster for Fresh Install .) |
| Step 6 | Cisco Prime Collaboration Deployment GUI—Setup Email Notification (Optional). Click the open and close navigation button and choose Administration > Email Notification . When email notification is set up, the Cisco Prime Collaboration Deployment server emails the error conditions that may occur
                                                      during the migration task. |
| Step 7 | Cisco Prime Collaboration Deployment GUI—Create the Install task. |
| Step 8 | Be sure to enter the IP addresses or hostnames of the cluster nodes to be installed into your DNS server before you create
                                             the install task. |

| Note | Make sure that the host with the Cisco Prime Collaboration Deployment VM and the host with the application VMs use the required
                                                            Virtualization Software License. See Add an ESXi Host Server . |
|---|---|

| Note | The ISO file must be bootable. |
|---|---|

| Note | Do not edit the file name of the bootable ISO that is being used for a PCD task. |
|---|---|

| Step 1 | Click the open and close navigation button and choose Task > Install from the main menu. |
|---|---|
| Step 2 | Click Add
                                                				Install Task . Note If you have no Install tasks, a Cluster Installation pop-up window appears with the prerequisites to run the wizard. Click Close to close the pop-up window. | Note | If you have no Install tasks, a Cluster Installation pop-up window appears with the prerequisites to run the wizard. Click Close to close the pop-up window. |
| Note | If you have no Install tasks, a Cluster Installation pop-up window appears with the prerequisites to run the wizard. Click Close to close the pop-up window. |
| Step 3 | In the Specify Task Name drop-down, enter a name for the install task in Choose a Nickname for this Install Task . |
| Step 4 | From the Installation Cluster drop-down list, select the
                                             			 cluster on which the nodes to be installation are located. If you want to apply an upgrade patch along with the installation, click Yes radio button otherwise click No radio button. |
| Step 5 | Click Next . |
| Step 6 | Click the respective Browse buttons to select the Unified Communications Manager Installation file and the Cisco Unified Presence Installation file from
                                             the server. If you have applied upgrade patch along with the installation, browse the patch files along with the installation files for
                                                Unified Communications Manager and the Cisco Unified Presence. You must select the patch file of same Engineering Special (ES)/ Service Update (SU) versions of the installation file. Important The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. For more information, see the task management information at the beginning of
                                                            this section. Note By default, only files that can be installed on the selected nodes are displayed. The option to select install files is available
                                                            only for the selected product types and applications that are currently supported in the cluster. Note To create an install task, while selecting ISO files, ensure that the ISO files are common across all the required SFTP servers
                                                         which are associated to cluster nodes. If the ISO files are not common to all the required SFTP servers which are associated
                                                         to cluster nodes, the valid files do not appear even though they are valid for migration. To view all the ISO files, from
                                                         the Show drop-down list, choose All . Note When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. | Important | The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. For more information, see the task management information at the beginning of
                                                            this section. | Note | By default, only files that can be installed on the selected nodes are displayed. The option to select install files is available
                                                            only for the selected product types and applications that are currently supported in the cluster. | Note | To create an install task, while selecting ISO files, ensure that the ISO files are common across all the required SFTP servers
                                                         which are associated to cluster nodes. If the ISO files are not common to all the required SFTP servers which are associated
                                                         to cluster nodes, the valid files do not appear even though they are valid for migration. To view all the ISO files, from
                                                         the Show drop-down list, choose All . | Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
| Important | The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. For more information, see the task management information at the beginning of
                                                            this section. |
| Note | By default, only files that can be installed on the selected nodes are displayed. The option to select install files is available
                                                            only for the selected product types and applications that are currently supported in the cluster. |
| Note | To create an install task, while selecting ISO files, ensure that the ISO files are common across all the required SFTP servers
                                                         which are associated to cluster nodes. If the ISO files are not common to all the required SFTP servers which are associated
                                                         to cluster nodes, the valid files do not appear even though they are valid for migration. To view all the ISO files, from
                                                         the Show drop-down list, choose All . |
| Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
| Step 7 | Click Choose
                                                				File . |
| Step 8 | Click Next . Note The Next button is dimmed if no valid upgrade files are
                                                            				  selected. | Note | The Next button is dimmed if no valid upgrade files are
                                                            				  selected. |
| Note | The Next button is dimmed if no valid upgrade files are
                                                            				  selected. |
| Step 9 | Select the
                                             			 date and time when you want the upgrade task to begin. You have the following
                                             			 options to schedule upgrades: Select Schedule for a specific time to enter the date and
                                                				time when you want the upgrade task to start. Any start time that you set is
                                                				based on the time zone of the Cisco Prime Collaboration Deployment server as
                                                				denoted by the time zone that is displayed with this option. Note If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. Select Start task manually to keep the task in a manual
                                                				start. Select Start task immediately upon completion of this wizard to start the task immediately after you click Finish . Note You can also start the task from the Monitoring page. | Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. | Note | You can also start the task from the Monitoring page. |
| Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. |
| Note | You can also start the task from the Monitoring page. |
| Step 10 | Click Next . |
| Step 11 | Specify the
                                             			 sequence of steps to complete the task. You have the following options: Option Description Pencil
                                                      				  icon Edit a
                                                         					 step. Page icon Add a new
                                                         					 step after the current step. X mark Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. Up arrow Move the
                                                         					 step up to be performed earlier. Down
                                                      				  arrow Move the
                                                         					 step down to be performed later. The Pencil icon opens up an Edit Step window. Add nodes to be installed in this
                                                				step from the list of available nodes. The available nodes are the ones that
                                                				you chose to install in this cluster. The step to which each node
                                                				is assigned displays next to the node. If a node is not assigned to any step,
                                                				it shows as unassigned. When you assign all the nodes to a step, a default sequencing is available. Important You cannot proceed to next step until you assign all the nodes. If you are installing
                                                				Cisco Unified Communications Manager between Releases 10.0(1) and 10.5(1), the
                                                				task is paused after publisher node is installed completely. You must enter
                                                				details of subscriber nodes into the publisher node before you manually start
                                                				the next step. Cisco Unified Communications Manager Release 10.5(2) onward does
                                                				not pause during a fresh installation; the install task continues
                                                				automatically. | Option | Description | Pencil
                                                      				  icon | Edit a
                                                         					 step. | Page icon | Add a new
                                                         					 step after the current step. | X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. | Up arrow | Move the
                                                         					 step up to be performed earlier. | Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. | Important | You cannot proceed to next step until you assign all the nodes. |
| Option | Description |
| Pencil
                                                      				  icon | Edit a
                                                         					 step. |
| Page icon | Add a new
                                                         					 step after the current step. |
| X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. |
| Up arrow | Move the
                                                         					 step up to be performed earlier. |
| Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. |
| Important | You cannot proceed to next step until you assign all the nodes. |
| Step 12 | Click OK . |
| Step 13 | Click Next . Note The Next button remains enabled, which allows you to click to be informed of any Misconfiguration. | Note | The Next button remains enabled, which allows you to click to be informed of any Misconfiguration. |
| Note | The Next button remains enabled, which allows you to click to be informed of any Misconfiguration. |
| Step 14 | See the Review section to verify the details of the task you created. You can add notes for the task if necessary. The notes are saved with
                                             the task and are visible if the task is edited before completion. |
| Step 15 | Click Finish to schedule the install task. |

| Note | If you have no Install tasks, a Cluster Installation pop-up window appears with the prerequisites to run the wizard. Click Close to close the pop-up window. |
|---|---|

| Important | The ISO file is visible here only if it was placed in the local SFTP directory under /fresh_install , if Prime Collaboration Deployment is used as local SFTP. If any remote SFTP is associated with the migration cluster, then
                                                            the files should present in the remote SFTP. For more information, see the task management information at the beginning of
                                                            this section. |
|---|---|

| Note | By default, only files that can be installed on the selected nodes are displayed. The option to select install files is available
                                                            only for the selected product types and applications that are currently supported in the cluster. |
|---|---|

| Note | To create an install task, while selecting ISO files, ensure that the ISO files are common across all the required SFTP servers
                                                         which are associated to cluster nodes. If the ISO files are not common to all the required SFTP servers which are associated
                                                         to cluster nodes, the valid files do not appear even though they are valid for migration. To view all the ISO files, from
                                                         the Show drop-down list, choose All . |
|---|---|

| Note | When you add the Remote SFTP server, you should maintain the different SFTP directories for fresh install/migration and upgrade.
                                                            You can add the same Remote SFTP server for fresh install/migration and upgrade but directories for fresh install/migration
                                                            and upgrade should be different. |
|---|---|

| Note | The Next button is dimmed if no valid upgrade files are
                                                            				  selected. |
|---|---|

| Note | If you schedule a task for a few minutes in the future, but do not save it until that scheduled time passes, then the task
                                                               starts automatically. |
|---|---|

| Note | You can also start the task from the Monitoring page. |
|---|---|

| Option | Description |
|---|---|
| Pencil
                                                      				  icon | Edit a
                                                         					 step. |
| Page icon | Add a new
                                                         					 step after the current step. |
| X mark | Delete the
                                                         					 current step. If you
                                                         					 remove all the nodes from a step, the step is removed by default. You cannot
                                                         					 remove a step that contains the Publisher node. |
| Up arrow | Move the
                                                         					 step up to be performed earlier. |
| Down
                                                      				  arrow | Move the
                                                         					 step down to be performed later. |

| Important | You cannot proceed to next step until you assign all the nodes. |
|---|---|

| Note | The Next button remains enabled, which allows you to click to be informed of any Misconfiguration. |
|---|---|

| Note | Clicking the Validation button will not start the task; this button only checks the resources to be used when the task starts. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, click
                                             			 the open and close navigation button and choose Task > Install from the main menu. The existing install tasks appear in the Task List section. |
|---|---|
| Step 2 | Select an
                                             			 existing install task and click Cancel . Note If you
                                                            				  cancel the currently running install task, you will have to delete the virtual
                                                            				  machine and then recreate it. The
                                             			 virtual machine of the selected install task turns off and the task status is
                                             			 displayed as Canceled . | Note | If you
                                                            				  cancel the currently running install task, you will have to delete the virtual
                                                            				  machine and then recreate it. |
| Note | If you
                                                            				  cancel the currently running install task, you will have to delete the virtual
                                                            				  machine and then recreate it. |

| Note | If you
                                                            				  cancel the currently running install task, you will have to delete the virtual
                                                            				  machine and then recreate it. |
|---|---|

| Note | For a description of the information that is available through the Monitoring page, see Monitoring View Elements . |
|---|---|

| Step 1 | Click the Monitoring link on the main menu to view the Monitoring page. |
|---|---|
| Step 2 | The column on
                                          			 the left side of the Monitoring page lists each task and an icon that shows its
                                          			 current status. Also shown is the type of task (Migrate, Upgrade, Install,
                                          			 and so on), and the cluster nickname for the task. The task start
                                             				time is also shown. Click the task in this
                                             				left column to view the detailed data for that task in the panel on the right. |
| Step 3 | The upper
                                          			 right section of the page provides the following data: Status Start time Task data (for example:
                                             				cluster nickname and ISO name) Click View Log to see the detailed log messages for the task. If you see any errors or
                                             				warnings in this log, refer to the Troubleshooting section more information. In the upper
                                             				right are buttons that you use to perform various operations on the task.
                                             				For example, if the task is paused, click the Resume button to resume the task. A button will
                                             				appear if it is valid for the current state of the task. For example, after a
                                             				task is finished, it will not have a Cancel button, but instead will have a
                                             				Delete button (if you wish to remove the data for the task). |
| Step 4 | The bottom
                                          			 right section of the page provides detailed steps for the task, along with the
                                          			 status for that step. Click on the triangle that corresponds to a step to
                                          			 expand the step description. Each step also
                                             				has a View Log link, to show the log messages for that step. Note The Monitoring page refreshes automatically every 6 minutes. To deactivate automatic refresh, click the Disable button. | Note | The Monitoring page refreshes automatically every 6 minutes. To deactivate automatic refresh, click the Disable button. |
| Note | The Monitoring page refreshes automatically every 6 minutes. To deactivate automatic refresh, click the Disable button. |

| Note | The Monitoring page refreshes automatically every 6 minutes. To deactivate automatic refresh, click the Disable button. |
|---|---|

| Note | These
                                          		  procedures describe how to place files on the Cisco Prime Collaboration
                                          		  Deployment server using Linux. You can push a file from a Linux machine for
                                          		  SFTP client. |
|---|---|

| Step 1 | From a Linux
                                             			 shell, type sftp
                                                				adminsftp@<Cisco Prime Collaboration Deployment server> and then
                                             			 provide the password (the same in both the CLI and GUI). |
|---|---|
| Step 2 | Change the
                                             			 directory to the fresh_install directory. Example: From a Linux shell, type cd fresh_install and press Return . |
| Step 3 | Upload the
                                             			 ISO file. Example: Type put UCSInstall_UCOS_10.0.x.xxx.sgn.iso . |

| Step 1 | From a Linux
                                             			 shell, type sftp
                                                				adminsftp@<Cisco Prime Collaboration Deployment server> and then
                                             			 provide the password (the same in both the CLI and GUI). |
|---|---|
| Step 2 | Change the
                                             			 directory to the upgrade directory. Example: From a Linux shell, type cd upgrade and press Return . |
| Step 3 | Upload the
                                             			 ISO file or COP file. Example: Type put UCSInstall_UCOS_10.0.x.xxx.sgn.iso . |

| Step 1 | From the Cisco Prime Collaboration Deployment application, click open and close navigation and choose Inventory > SFTP Servers and Datastore . |
|---|---|
| Step 2 | On this page,
                                             			 you can view and manage files that are stored on the SFTP datastore of this
                                             			 Cisco Prime Collaboration Deployment server. It displays
                                             			 the filename of the ISO and COP files that are stored on the server, and where
                                             			 they are located in the directory (for example: fresh_install or upgrade). |

| Step 1 | Log in to
                                             			 Cisco Prime Collaboration Deployment. |
|---|---|
| Step 2 | From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Inventory > SFTP Servers and Datastore . |
| Step 3 | Check the
                                             			 check box next to the ISO or COP file. |
| Step 4 | Click Delete . Important We
                                                               					 recommend that you periodically delete ISO or COP files that are no longer
                                                               					 needed to save space, especially before upgrading the Cisco Prime Collaboration
                                                               					 Deployment server software. | Important | We
                                                               					 recommend that you periodically delete ISO or COP files that are no longer
                                                               					 needed to save space, especially before upgrading the Cisco Prime Collaboration
                                                               					 Deployment server software. |
| Important | We
                                                               					 recommend that you periodically delete ISO or COP files that are no longer
                                                               					 needed to save space, especially before upgrading the Cisco Prime Collaboration
                                                               					 Deployment server software. |

| Important | We
                                                               					 recommend that you periodically delete ISO or COP files that are no longer
                                                               					 needed to save space, especially before upgrading the Cisco Prime Collaboration
                                                               					 Deployment server software. |
|---|---|

| SFTP Server | Support Description |
|---|---|
| SFTP Server from a Technology Partner | These servers are third party provided and third party tested. Version compatibility depends on the third-party test. Refer
                                          to the Technology Partner page if you upgrade their SFTP product and/or upgrade Unified Communications Manager. |
| SFTP Server from another Third Party | These servers are third party provided and are not officially supported by Cisco TAC. Version compatibility is on a best effort basis to establish compatible SFTP versions and Emergency Responder versions. Note These products have not been tested by Cisco and we cannot guarantee their functionality. Cisco TAC does not support these
                                                   products. For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. | Note | These products have not been tested by Cisco and we cannot guarantee their functionality. Cisco TAC does not support these
                                                   products. For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |
| Note | These products have not been tested by Cisco and we cannot guarantee their functionality. Cisco TAC does not support these
                                                   products. For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |

| Note | These products have not been tested by Cisco and we cannot guarantee their functionality. Cisco TAC does not support these
                                                   products. For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |
|---|---|

| Note | The remote SFTP server support is available for upgrade, migration, and fresh install tasks. |
|---|---|

| Note | Cisco Prime Collaboration Deployment does not support Windows server while adding it as an external SFTP server for installation or migration tasks. Only Unix
                                          and Linux-style path formats are supported. |
|---|---|

| Note | Due to the limitation on PCD to store the huge lists of ESXi hosts where the remote SFTP server is mounted as NFS datastore,
                                                make sure to remove the unused remote SFTP server which is mounted as NFS from the ESXi hosts added in PCD. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application,
                                             			 click the open and close navigation button and choose Inventory > SFTP Servers
                                                   				  and Datastore . The SFTP Servers/Datastore table on this window
                                             			 shows the PCD details by default. |
|---|---|
| Step 2 | From the SFTP Servers/Datastore table, click Add Server . The Add external file access window appears. |
| Step 3 | Click Install/Migration or Upgrade radio button. |
| Step 4 | In the Address and access credentials section, enter values
                                             			 in the IP /
                                                				Host Name , Username , and Password fields. |
| Step 5 | For Install or Migration task type, in the Remote NFS Path to Datastore Directory on Server section, enter the directory path in Directory field and NFS server name in NFS Server Name field. Feild Description Directory Path which has been configured for NFS storage in ESXI host. NFS Server Name Name of NFS storage which has been created in ESXI. Example: Directory: /abc/def/ NFS Server Name: xyz_NFS When adding an NFS server, the SFTP credentials should point to a directory that is an exact match for the path which is configured
                                                in the ESXi host. For more information on adding NFS storage in ESXi host refer the respective documentation guide. | Feild | Description | Directory | Path which has been configured for NFS storage in ESXI host. | NFS Server Name | Name of NFS storage which has been created in ESXI. |
| Feild | Description |
| Directory | Path which has been configured for NFS storage in ESXI host. |
| NFS Server Name | Name of NFS storage which has been created in ESXI. |
| Step 6 | For Upgrade task type, in the Remote SFTP Path to Datastore Directory on Server , click an Add Directory button to add a value in the Directory field. Note For an upgrade, ensure that a directory includes .iso datastore files. | Note | For an upgrade, ensure that a directory includes .iso datastore files. |
| Note | For an upgrade, ensure that a directory includes .iso datastore files. |
| Step 7 | (Optional) In
                                             			 the Additional Information section, enter description in
                                             			 the Description field. |
| Step 8 | Click Add . Upon the successful add of remote SFTP server for the install or migration task type, a dialog box is displayed. Dialog box
                                                lists the ESXi hosts which are already added to Prime Collaboration Deployment under Inventory > ESXi Hosts that has the given NFS directory mounted. Note If the SFTP server is not added, you get any of the following error messages: Connection Timeout —Indicates that the connection to SFTP server failed due to timeout. Login Failure —Indicates that the login to the SFTP server failed. Directory Not Found —Indicates that the directory that you selected is not found on the SFTP server. Directory Already Entered —Indicates that the directory that you selected already exists in the list of directories. You can view the list of available
                                                                  directories by clicking the Add Directory button. Directory Already Exists —Indicates that the directory that you entered already exists in the list of the SFTP servers. Mandatory Fields Missed —Indicates that you did not enter values in the mandatory fields. Mentioned Server Could Not Be Located —Indicates that the server that you entered is not configured with DNS. This error message appears if you enter host name
                                                                  instead of IP address. No ESXi Hosts in Inventory —Indicates that you have not added ESXi hosts. This error appears when you try to add Install or Migration task type remote
                                                                  SFTP, and the given NFS mount is not found as there are no ESXi hosts added under Inventory > ESXi Hosts page. Could not find given NFS path/Directory on the listed ESXi host(s) under Inventory > ESXi Hosts —This error appears when you try to add Install or Migration task type remote SFTP, and the given NFS directory is not found
                                                                  in any of the ESXi which are added under Inventory > ESXi Hosts page. The SFTP
                                                				Servers/Datastore table shows the remote SFTP server that you
                                             			 added. The SFTP/Datastore Files table shows the list of files
                                             			 from the remote SFTP server and from Cisco
                                                				Prime Collaboration Deployment . In addition, the existing Cisco
                                                				Prime Collaboration Deployment server is added automatically and the
                                             			 files in the upgrade and fresh_install folders in the Cisco
                                                				Prime Collaboration Deployment server appear by default in the SFTP/Datastore Files table. | Note | If the SFTP server is not added, you get any of the following error messages: Connection Timeout —Indicates that the connection to SFTP server failed due to timeout. Login Failure —Indicates that the login to the SFTP server failed. Directory Not Found —Indicates that the directory that you selected is not found on the SFTP server. Directory Already Entered —Indicates that the directory that you selected already exists in the list of directories. You can view the list of available
                                                                  directories by clicking the Add Directory button. Directory Already Exists —Indicates that the directory that you entered already exists in the list of the SFTP servers. Mandatory Fields Missed —Indicates that you did not enter values in the mandatory fields. Mentioned Server Could Not Be Located —Indicates that the server that you entered is not configured with DNS. This error message appears if you enter host name
                                                                  instead of IP address. No ESXi Hosts in Inventory —Indicates that you have not added ESXi hosts. This error appears when you try to add Install or Migration task type remote
                                                                  SFTP, and the given NFS mount is not found as there are no ESXi hosts added under Inventory > ESXi Hosts page. Could not find given NFS path/Directory on the listed ESXi host(s) under Inventory > ESXi Hosts —This error appears when you try to add Install or Migration task type remote SFTP, and the given NFS directory is not found
                                                                  in any of the ESXi which are added under Inventory > ESXi Hosts page. |
| Note | If the SFTP server is not added, you get any of the following error messages: Connection Timeout —Indicates that the connection to SFTP server failed due to timeout. Login Failure —Indicates that the login to the SFTP server failed. Directory Not Found —Indicates that the directory that you selected is not found on the SFTP server. Directory Already Entered —Indicates that the directory that you selected already exists in the list of directories. You can view the list of available
                                                                  directories by clicking the Add Directory button. Directory Already Exists —Indicates that the directory that you entered already exists in the list of the SFTP servers. Mandatory Fields Missed —Indicates that you did not enter values in the mandatory fields. Mentioned Server Could Not Be Located —Indicates that the server that you entered is not configured with DNS. This error message appears if you enter host name
                                                                  instead of IP address. No ESXi Hosts in Inventory —Indicates that you have not added ESXi hosts. This error appears when you try to add Install or Migration task type remote
                                                                  SFTP, and the given NFS mount is not found as there are no ESXi hosts added under Inventory > ESXi Hosts page. Could not find given NFS path/Directory on the listed ESXi host(s) under Inventory > ESXi Hosts —This error appears when you try to add Install or Migration task type remote SFTP, and the given NFS directory is not found
                                                                  in any of the ESXi which are added under Inventory > ESXi Hosts page. |

| Feild | Description |
|---|---|
| Directory | Path which has been configured for NFS storage in ESXI host. |
| NFS Server Name | Name of NFS storage which has been created in ESXI. |

| Note | For an upgrade, ensure that a directory includes .iso datastore files. |
|---|---|

| Note | If the SFTP server is not added, you get any of the following error messages: Connection Timeout —Indicates that the connection to SFTP server failed due to timeout. Login Failure —Indicates that the login to the SFTP server failed. Directory Not Found —Indicates that the directory that you selected is not found on the SFTP server. Directory Already Entered —Indicates that the directory that you selected already exists in the list of directories. You can view the list of available
                                                                  directories by clicking the Add Directory button. Directory Already Exists —Indicates that the directory that you entered already exists in the list of the SFTP servers. Mandatory Fields Missed —Indicates that you did not enter values in the mandatory fields. Mentioned Server Could Not Be Located —Indicates that the server that you entered is not configured with DNS. This error message appears if you enter host name
                                                                  instead of IP address. No ESXi Hosts in Inventory —Indicates that you have not added ESXi hosts. This error appears when you try to add Install or Migration task type remote
                                                                  SFTP, and the given NFS mount is not found as there are no ESXi hosts added under Inventory > ESXi Hosts page. Could not find given NFS path/Directory on the listed ESXi host(s) under Inventory > ESXi Hosts —This error appears when you try to add Install or Migration task type remote SFTP, and the given NFS directory is not found
                                                                  in any of the ESXi which are added under Inventory > ESXi Hosts page. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application,
                                             			 click the open and close navigation button and choose Inventory > Clusters . The Clusters window appears. |
|---|---|
| Step 2 | Click Discover Cluster button to search for the existing
                                             			 clusters. To discover a cluster, see the Discover a Cluster procedure. |
| Step 3 | From the
                                             			 available cluster nodes in the Cluster Nodes table, click Edit for a cluster node. The Edit Node window appears. |
| Step 4 | From the SFTP
                                                				Server drop-down list, choose an SFTP server. By default,
                                                				this field shows the localhost option as the SFTP Server. |
| Step 5 | Click OK . The
                                             			 SFTP server is associated with the cluster node that you selected and the
                                             			 details appear in the SFTP
                                                				Server column of the Cluster Nodes table. |

| Step 1 | From the Cisco Prime Collaboration Deployment application, click
                                             			 the open and close navigation button and choose Inventory > SFTP Servers
                                                   				  and Datastore . The SFTP and NFS File access table on this window shows the PCD details by default. |
|---|---|
| Step 2 | From the available SFTP servers in the SFTP and NFS File access table, click Edit for an SFTP server. The Edit SFTP Server window appears. |
| Step 3 | For Install or Migration tasks, edit the values for the fields in the Address and access credentials , Remote NFS Path to Datastore Directory on Server , NFS Server Name , and Additional Information sections. Upon successful edit of remote SFTP server for install or migration task type, a dialog box is displayed. Dialog box lists
                                             the ESXi hosts which are already added to Prime Collaboration Deployment under Inventory > ESXi Hosts that has the given NFS directory mounted. |
| Step 4 | For Upgrade task, edit the values for the fields in the Address and access credentials , Remote SFTP Path to Datastore Directory on Server , and Additional Information sections. In Remote SFTP Path to Datastore Directory on Server section, by clicking the Add Directory button, you can edit an existing directory and also add multiple directories. |
| Step 5 | Click Save . |

| Note | You can disassociate a cluster node even if no install, migration or upgrade tasks are associated and running with the cluster node that uses the SFTP server that you selected to delete. |
|---|---|

| Note | If you do not change the node association from remote/external SFTP server to the localhost SFTP server, the association of cluster nodes changes to the localhost SFTP server from the remote SFTP server and the remote SFTP server that you selected is deleted. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Inventory > SFTP Servers and Datastore . The SFTP Servers/Datastore table on this window shows the PCD details by default. |
|---|---|
| Step 2 | From the
                                             			 available SFTP servers in the SFTP
                                                				Servers/Datastore table, check the check box of one or multiple
                                             			 remote SFTP servers that you want to delete. |
| Step 3 | Click Delete . |

| Step 1 | From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Inventory > SFTP Servers and Datastore . The SFTP Servers/Datastore table on this window shows the PCD details by default. |
|---|---|
| Step 2 | From the
                                             			 available SFTP and datastore files in the SFTP/Datastore Files table, check the check box of
                                             			 one or multiple remote SFTP and datastore files that you want to delete. Note You cannot
                                                            				  delete remote SFTP files. | Note | You cannot
                                                            				  delete remote SFTP files. |
| Note | You cannot
                                                            				  delete remote SFTP files. |
| Step 3 | Click Delete . |

| Note | You cannot
                                                            				  delete remote SFTP files. |
|---|---|

| Note | Disk space
                                             		  warning level is applicable and is validated for migration and install tasks.
                                             		  This level is also validated each time you log in to Cisco Prime Collaboration
                                             		  Deployment. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Administration > Disk Space Warning Level . The Disk Space Warning Level window appears showing the total disk space and the available disk space. |
|---|---|
| Step 2 | View the total
                                             			 disk space and the available disk space in the Total
                                                				Disk Space (GB) and Available Disk Space (GB) fields. |
| Step 3 | Enter the
                                             			 value that you want to assign for the Warning Level Disk Space (GB) field. You can click
                                                				the information link to check if the space value you entered is available for
                                                				use on the server. |
| Step 4 | Click Save . |
| Step 5 | (Optional) Click Reset . The
                                             			 page is reset with the default values. |

| Step 1 | From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Administration > Max Nodes Configuration . |
|---|---|
| Step 2 | Enter a value in the Max Nodes field. Note Maximum nodes count loads with the default value 30. You can enter maximum 1–200 nodes. | Note | Maximum nodes count loads with the default value 30. You can enter maximum 1–200 nodes. |
| Note | Maximum nodes count loads with the default value 30. You can enter maximum 1–200 nodes. |
| Step 3 | Click Save . |
| Step 4 | Restart the Cisco Tomcat server to reflect change. |
| Step 5 | Optional: Click Reset . The page is reset with the default values. Note When the maximum nodes count exceeds the maximum defined limit for tasks (Cluster Discovery, Install Task, Migrate Task, Upgrade
                                                            Task, Switch Version Task, Server Restart Task, and Readdress Task), the following error message is displayed: Maximum node count exceeded. This task takes longer time to complete. | Note | When the maximum nodes count exceeds the maximum defined limit for tasks (Cluster Discovery, Install Task, Migrate Task, Upgrade
                                                            Task, Switch Version Task, Server Restart Task, and Readdress Task), the following error message is displayed: |
| Note | When the maximum nodes count exceeds the maximum defined limit for tasks (Cluster Discovery, Install Task, Migrate Task, Upgrade
                                                            Task, Switch Version Task, Server Restart Task, and Readdress Task), the following error message is displayed: |

| Note | Maximum nodes count loads with the default value 30. You can enter maximum 1–200 nodes. |
|---|---|

| Note | When the maximum nodes count exceeds the maximum defined limit for tasks (Cluster Discovery, Install Task, Migrate Task, Upgrade
                                                            Task, Switch Version Task, Server Restart Task, and Readdress Task), the following error message is displayed: |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, click open and close navigation and choose Administration > Audit Log Configuration . |
|---|---|
| Step 2 | Choose one of the options from the Application Audit Event Level drop down list
                                             			 to configure an audit level. |
| Step 3 | Enter the name of remote syslog server or the IP address for the Remote Syslog Server Name / IP field so that
                                             			 the audit logs are logged into this remote server. |
| Step 4 | (Optional) Check or uncheck the Enable Local Audit Log check box to enable or
                                             			 disable the local audit log. When you check this field, the audit events are logged in the local server. When you uncheck this field, audit events are
                                                      not logged in the local server. The audit events includes User ID, ClientAddress, Severity, EventType, ResourceAccessed, EventuStatus
                                                      , AuditCategory, CompulsoryEvent, ComponentID, CorrelationID and Node ID. When you check this field, the Enable Log Rotation field becomes
                                                      					 active. |
| Step 5 | (Optional) Check or uncheck the Enable Log Rotation check box to enable or
                                             			 disable the log rotation. Note You can configure this field if Enable Local Audit Log is enabled. When you check this field, you can configure the Maximum No of Files , Maximum File Size(MB) , and Warning Threshold for Approaching Log Rotation
                                                				Overwrite(%) fields. When you uncheck the Enable Local Audit Log field, the default
                                             			 values of these fields are not applicable as they are inactive. | Note | You can configure this field if Enable Local Audit Log is enabled. |
| Note | You can configure this field if Enable Local Audit Log is enabled. |
| Step 6 | Enter an integer value for the Maximum No of Files field to configure the
                                             			 maximum number of files that can be created on the server. |
| Step 7 | Enter a value for the Maximum File Size (MB) field to configure the
                                             			 maximum file size of each log that is created on the server. |
| Step 8 | Enter the warning threshold value for the Warning Threshold for Approaching Log Rotation
                                                				Overwrite(%) field. |
| Step 9 | Click Save . |
| Step 10 | (Optional) Click Reset . The page is reset with the default values. |

| Note | You can configure this field if Enable Local Audit Log is enabled. |
|---|---|

| Step 1 | From the Cisco Prime Collaboration Deployment application, click Open and close navigation and choose Administration > Customized Logon Message . |
|---|---|
| Step 2 | For the Upload File field, browse to the location of
                                             			 file that includes the customized logon message. |
| Step 3 | (Optional) Check or uncheck the Require User Acknowledgement check box to
                                             			 enable or disable user acknowledgment for the file that the user receives. If this field is enabled, users get an acknowledgment as an
                                             			 alert message on the Cisco Prime Collaboration Deployment sign-in page after
                                             			 they sign out for the first time from the same web browser instance. |
| Step 4 | Click Upload File . The file with the customized logon message is uploaded and
                                             			 a pop-up appears showing the file upload status. |
| Step 5 | (Optional) Click Delete . The file with the customized logon message is deleted and
                                             			 a pop-up appears showing the file deletion status. |

| Note | Elliptic Curve Digital Signature Algorithm (ECDSA) ciphers are not supported in Cisco Prime Collaboration Deployment. Hence,
                                                during TLS connection, the server does not negotiate the ECDSA certificates even though the show cert list own CLI command may show the ECDSA self-signed certificate. All the nodes of a cluster should either be FIPS or non-FIPS. |
|---|---|

| Note | If you configure UC clusters on FIPS mode or EnhancedSecurityMode, ensure that you also configure Cisco Prime Collaboration
                                          Deployment with the similar modes. With this configuration, you can run the tasks that are specific to UC clusters. |
|---|---|

| Note | By default,
                                          			 auditing is not enabled in Cisco Prime Collaboration Deployment. If you wish to
                                          			 have audit logs, you can enable auditing with or without being in FIPS mode or
                                          			 EnhancedSecurityMode. |
|---|---|

| Application / Process | Protocol | Port | Supported Ciphers |
|---|---|---|---|
| Cisco Tomcat PCD as a Server | TCP / TLS | 8443 / 443 | TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-RSA-AES128-GCM-SHA256
AES256-SHA
AES128-SHA
DHE-RSA-AES128-SHA |
| Cisco Tomcat PCD as a Client | TCP / TLS | 8443 / 443 | TLS_AES_256_GCM_SHA384
TLS_AES_128_GCM_SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-ECDSA-AES256-GCM-SHA384
ECDHE-RSA-AES128-GCM-SHA256
ECDHE-ECDSA-AES128-GCM-SHA256
ECDHE-RSA-AES256-SHA384
ECDHE-ECDSA-AES256-SHA384
ECDHE-RSA-AES128-SHA256
ECDHE-ECDSA-AES128-SHA256
ECDHE-RSA-AES256-SHA
ECDHE-ECDSA-AES256-SHA
ECDHE-RSA-AES128-SHA
ECDHE-ECDSA-AES128-SHA
AES256-GCM-SHA384
AES128-GCM-SHA256
AES256-SHA
AES128-SHA |

| Service | Ciphers/Algorithms |
|---|---|
| SSH Server | Ciphers aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com MAC algorithms: hmac-sha2-256
hmac-sha2-512
hmac-sha1 Kex algorithms: ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha1
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512 Host Key algorithms: rsa-sha2-256
rsa-sha2-512
ssh-rsa |
| SSH Client | Ciphers: aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com MAC algorithms: hmac-sha2-256
hmac-sha2-512
hmac-sha1 Kex algorithms: ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha1
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512 Host Key algorithms: rsa-sha2-256
rsa-sha2-512
ssh-rsa |
| DRS Client | Ciphers: aes256-ctr
aes128-ctr MAC algorithms: hmac-sha2-256
hmac-sha1
hmac-md5
hmac-sha1-96
hmac-md5-96 Kex algorithms: ecdh-sha2-nistp256
ecdh-sha2-nistp384
ecdh-sha2-nistp521
diffie-hellman-group14-sha256
diffie-hellman-group14-sha1
diffie-hellman-group-exchange-sha1
diffie-hellman-group1-sha1 Host Key algorithms in non-FIPS mode: ssh-rsa
ecdsa-sha2-nistp256
ecdsa-sha2-nistp384
ecdsa-sha2-nistp521 Host Key algorithms in FIPS mode: rsa-sha2-256 |

| Note | When users exceed the limit of configured number of sign-in
                                          			 sessions, they must sign out from the application in that session and sign in
                                          			 to another session. In case the session closes due to abrupt exit from web
                                          			 browser, users need to restart the Tomcat server on Cisco Prime Collaboration
                                          			 Deployment to allow sign-in to the new session. |
|---|---|

| Note | For Install task, Cisco Prime Collaboration Deployment has the default timeout value as 5 hours, which is non-configurable. |
|---|---|