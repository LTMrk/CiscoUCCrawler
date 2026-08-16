---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-cup0-b-config-and-admin-guide-1251--0451b6df79
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1/cup0_b_config-and-admin-guide-1251/cup0_b_config-and-admin-guide-1251_chapter_011011.html
retrieved_at: 2026-08-16T16:43:59.779096+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)

Updated: November 27, 2024

Chapter: Manage the Server

## Chapter: Manage the Server

# Manage the Server

## Manage the Server Overview

This chapter contains information on how to edit server details for a deployed system. This includes assigning a new node
                              to a cluster, removing a node from a cluster, viewing the presence status and changing server address details.

## Changing the Server Address

If you have an up and running system, and you need to make any of the following changes to the server addressing, refer to
                              the procedures in the document Changing the IP Address and Hostname for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

This applies to the following types of address changes:

Changing the server IP Address

Changing the server hostname

Changing the node name (for example, if you are using an IP
                                    address to define the node name and you want to use a hostname
                                    instead).

Changing the default domain for the IM and Presence Service

## Delete IM and Presence Node From Cluster

Follow this procedure if you need to safely remove an IM and Presence Service node from its presence redundancy group and
                              cluster.

Caution

Removing a node
                                          			 will cause a service interruption to users on the remaining node(s) in the
                                          			 presence redundancy group. This procedure should only be performed during a
                                          			 maintenance window.

Step 1

On the Cisco Unified CM
                                             				  Administration > System > Presence Redundancy
                                             				  Groups page, disable High Availability if it is
                                       			 enabled.

Step 2

On the Cisco Unified CM
                                             				  Administration > User Management > Assign Presence
                                             				  Users page, unassign or move all the users off the
                                       			 node that you want to remove.

Step 3

To remove the node from its presence redundancy group, choose Not-Selected from the Presence Server drop down list on the presence redundancy group's Presence Redundancy Group Configuration page. Select OK when a warning dialog box indicates that services in the presence redundancy group will be restarted as a result of unassigning
                                       the node.

You cannot delete the publisher node directly from a presence redundancy group. To delete a publisher node, first unassign
                                                      users from the publisher node and delete the presence redundancy group completely.

However, you can add the deleted IM and Presence node back into the cluster. For more information on how to add the deleted
                                                      nodes, see Add Deleted Server Back in to Cluster . In this scenario, the DefaultCUPSubcluster is created automatically when the deleted publisher node is added back to the server in the System > Server screen in the Cisco Unified CM Administration console.

Step 4

In Cisco Unified CM Administration, delete the unassigned node from the System > Server . Click OK when a warning dialog box indicates that this action cannot be undone.

Step 5

Shut down the
                                       			 host VM or server for the node you have unassigned.

Step 6

Restart the Cisco XCP Router on all nodes.

## Add Deleted Server Back in to Cluster

If you delete a subsequent node (subscriber) from Cisco Unified Communications Manager Administration and you want to add it back to the cluster, perform the following procedure.

Step 1

In Cisco Unified Communications Manager Administration , add the server by choosing System > Server .

Step 2

After you add the subsequent node to Cisco Unified Communications Manager Administration , perform an installation on the server by using the disk that Cisco provided in the software kit for your version.

Tip

Make sure that the version that you install matches the version that runs on the publisher node. If the version that is running
                                                      on the publisher does not match your installation file, choose the Upgrade During Install option during the installation process.
                                                      For details, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service .

Step 3

After you install Cisco UnifiedCM, configure the subsequent node, as described in the installation documentation that supports
                                       your version of Cisco UnifiedCM.

Step 4

Access the Cisco Unified Reporting , RTMT, or the CLI to verify that database replication is occurring between existing nodes; if necessary, repair database
                                       replication between the nodes.

## Add Node to Cluster Before Install

Use Cisco Unified Communications Manager Administration to add a new node to a cluster before installing the node. The server type you select when adding the node
                              must match the server type you install.

You must configure a new node on the first node using Cisco Unified Communications Manager Administration before you install the new node. To install a node on a cluster, see the Cisco Unified Communications Manager Installation Guide .

For Cisco Unified Communications Manager Video/Voice servers, the first server you add during an initial installation of the Cisco Unified Communications Manager software is designated the publisher node. All subsequent server installations or additions are designated as subscriber
                              nodes. The first Cisco Unified Communications Manager IM and Presence node you add to the cluster is designated the IM and Presence Service database publisher node.

You cannot use Cisco Unified Communications Manager Administration to change the server type after the server has been added. You must delete the existing server instance, and
                                          then add the new server again and choose the correct server type setting.

Step 1

Select System > Server .

The Find and List Servers window displays.

Step 2

Click Add New .

The Server Configuration - Add a Server window displays.

Step 3

From the Server Type drop-down list box, choose the server type that you want to add, and then click Next .

CUCM Video/Voice

CUCM IM and Presence

Step 4

In the Server Configuration window, enter the appropriate server settings.

For server configuration field descriptions, see Server Settings .

Step 5

Click Save .

## View Presence Server Status

Use Cisco Unified Communications Manager Administration to view the status of critical services and self-diagnostic test results for the IM and Presence Service node.

Step 1

Select System > Server .

The Find and List Servers window appears.

Step 2

Select the server search parameters, and then click Find .

Matching records appear.

Step 3

Select the IM and Presence server that is listed in the Find and List Servers window.

The Server Configuration window appears.

Step 4

Click on the Presence Server Status link in the IM and Presence Server Information section of the Server Configuration window.

The Node Details window for the server appears.

## Restarting Services with High Availability

If you make any system configuration changes, or system
                              upgrades, that require you to disable High Availability and then
                              restart either the Cisco XCP router, Cisco Presence Engine, or the
                              server itself, you must allow sufficient time for Cisco Jabber
                              sessions to be recreated before you enable High Availability.
                              Otherwise, Presence won't work for Jabber clients whose sessions aren't created.

Make sure to follow this process:

Step 1

Before you make any changes, check the Presence Topology window
                                       in Cisco Unified CM IM and Presence Administration window ( System > Presence Topology ). Take a record of the number of assigned
                                       users to each node in each Presence Redundancy Group.

Step 2

Disable High Availability in each Presence Redundancy Group and
                                       wait at least two minutes for the new HA settings to
                                       synchronize.

Step 3

Do whichever of the following is required for your update:

- Restart the Cisco XCP Router

- Restart the Cisco Presence Engine

- Restart the server

Step 4

After the restart, monitor the number of active sessions on all
                                       nodes.

Step 5

For each node, run the show perf query counter "Cisco Presence Engine" ActiveJsmSessions CLI command on each
                                       node to confirm the number of active sessions on each node. The
                                       number of active sessions should match the number that you recorded
                                       in step 1 for assigned users. It should take no more than 15
                                       minutes for all sessions to resume.

Step 6

Once all of your sessions are created, you can
                                       enable High Availability within the Presence Redundancy
                                       Group.

If 30 minutes passes and the active sessions haven't yet been created, restart the Cisco Presence Engine. If that doesn't
                                                      work, there is a larger system issue for you to fix.

It is not recommended to do back-to-back restarts of the Cisco XCP Router and/or Cisco Presence Engine. However, if you do
                                                      need to do a restart: restart the first service, wait for all of the JSM sessions to be recreated. After all of the JSM sessions
                                                      are created, then do the second restart.

## Hostname Configuration

The following table lists the locations where you can
                              		  configure a host name for the Unified Communications Manager server, the
                              		  allowed number of characters for the host name, and the recommended first and
                              		  last characters for the host name. Be aware that, if you do not configure the
                              		  host name correctly, some components in Unified Communications Manager ,
                              		  such as the operating system, database, installation, and so on, may not work
                              		  as expected.

Host Name Location

Allowed Configuration

Allowed Number of Characters

Recommended First Character for Host Name

Recommended Last Character for Host Name

Host Name/ IP Address field

System > Server in Cisco Unified Communications Manager Administration

You can add or change the host name for a server in the cluster.

2-63

alphabetic

alphanumeric

Hostname field

Cisco Unified Communications Manager installation wizard

You can add the host name for a server in the cluster.

1-63

alphabetic

alphanumeric

Hostname field

Settings > IP > Ethernet in Cisco Unified Communications Operating System

You can change, not add, the host name for a server in the cluster.

1-63

alphabetic

alphanumeric

set network hostname

hostname

Command Line Interface

You can change, not add, the host name for a server in the cluster.

1-63

alphabetic

alphanumeric

Tip

The host name must follow the rules for ARPANET host names. Between
                                          			 the first and last character of the host name, you can enter alphanumeric
                                          			 characters and hyphens.

Before you configure the host name in any location, review the following information:

After you install the Unified Communications Manager publisher node, the host name for the publisher automatically
                                    				displays in this field. Before you install a Unified Communications Manager subscriber node, enter either the IP address or the host name for the
                                    				subscriber node in this field on the Unified Communications Manager publisher node.

In this field, configure a host name only if Unified Communications Manager can access the DNS server to resolve host names to IP
                                    				addresses; make sure that you configure the Cisco Unified Communications
                                    				Manager name and address information on the DNS server.

Tip

In addition to configuring Unified Communications Manager information on the DNS server, you enter DNS information during the Cisco
                                          			 Unified Communications Manager installation.

During the installation of a Unified Communications Manager subscriber node, you enter the hostname and IP address of the Unified Communications Manager publisher
                                    				node, so that Unified Communications Manager can verify network
                                    				connectivity and publisher-subscriber validation. Additionally, you must enter
                                    				the host name and the IP address for the subscriber node. When the Unified Communications Manager installation prompts you for the host name of
                                    				the subscriber server, enter the value that displays in the Server
                                    				Configuration window in Cisco Unified Communications Manager Administration;
                                    				that is, if you configured a host name for the subscriber server in the Host
                                    				Name/IP Address field.

| Caution | Removing a node
                                          			 will cause a service interruption to users on the remaining node(s) in the
                                          			 presence redundancy group. This procedure should only be performed during a
                                          			 maintenance window. |
|---|---|

| Step 1 | On the Cisco Unified CM
                                             				  Administration > System > Presence Redundancy
                                             				  Groups page, disable High Availability if it is
                                       			 enabled. |
|---|---|
| Step 2 | On the Cisco Unified CM
                                             				  Administration > User Management > Assign Presence
                                             				  Users page, unassign or move all the users off the
                                       			 node that you want to remove. |
| Step 3 | To remove the node from its presence redundancy group, choose Not-Selected from the Presence Server drop down list on the presence redundancy group's Presence Redundancy Group Configuration page. Select OK when a warning dialog box indicates that services in the presence redundancy group will be restarted as a result of unassigning
                                       the node. Note You cannot delete the publisher node directly from a presence redundancy group. To delete a publisher node, first unassign
                                                      users from the publisher node and delete the presence redundancy group completely. However, you can add the deleted IM and Presence node back into the cluster. For more information on how to add the deleted
                                                      nodes, see Add Deleted Server Back in to Cluster . In this scenario, the DefaultCUPSubcluster is created automatically when the deleted publisher node is added back to the server in the System > Server screen in the Cisco Unified CM Administration console. | Note | You cannot delete the publisher node directly from a presence redundancy group. To delete a publisher node, first unassign
                                                      users from the publisher node and delete the presence redundancy group completely. However, you can add the deleted IM and Presence node back into the cluster. For more information on how to add the deleted
                                                      nodes, see Add Deleted Server Back in to Cluster . In this scenario, the DefaultCUPSubcluster is created automatically when the deleted publisher node is added back to the server in the System > Server screen in the Cisco Unified CM Administration console. |
| Note | You cannot delete the publisher node directly from a presence redundancy group. To delete a publisher node, first unassign
                                                      users from the publisher node and delete the presence redundancy group completely. However, you can add the deleted IM and Presence node back into the cluster. For more information on how to add the deleted
                                                      nodes, see Add Deleted Server Back in to Cluster . In this scenario, the DefaultCUPSubcluster is created automatically when the deleted publisher node is added back to the server in the System > Server screen in the Cisco Unified CM Administration console. |
| Step 4 | In Cisco Unified CM Administration, delete the unassigned node from the System > Server . Click OK when a warning dialog box indicates that this action cannot be undone. |
| Step 5 | Shut down the
                                       			 host VM or server for the node you have unassigned. |
| Step 6 | Restart the Cisco XCP Router on all nodes. |

| Note | You cannot delete the publisher node directly from a presence redundancy group. To delete a publisher node, first unassign
                                                      users from the publisher node and delete the presence redundancy group completely. However, you can add the deleted IM and Presence node back into the cluster. For more information on how to add the deleted
                                                      nodes, see Add Deleted Server Back in to Cluster . In this scenario, the DefaultCUPSubcluster is created automatically when the deleted publisher node is added back to the server in the System > Server screen in the Cisco Unified CM Administration console. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration , add the server by choosing System > Server . |
|---|---|
| Step 2 | After you add the subsequent node to Cisco Unified Communications Manager Administration , perform an installation on the server by using the disk that Cisco provided in the software kit for your version. Tip Make sure that the version that you install matches the version that runs on the publisher node. If the version that is running
                                                      on the publisher does not match your installation file, choose the Upgrade During Install option during the installation process.
                                                      For details, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service . | Tip | Make sure that the version that you install matches the version that runs on the publisher node. If the version that is running
                                                      on the publisher does not match your installation file, choose the Upgrade During Install option during the installation process.
                                                      For details, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service . |
| Tip | Make sure that the version that you install matches the version that runs on the publisher node. If the version that is running
                                                      on the publisher does not match your installation file, choose the Upgrade During Install option during the installation process.
                                                      For details, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service . |
| Step 3 | After you install Cisco UnifiedCM, configure the subsequent node, as described in the installation documentation that supports
                                       your version of Cisco UnifiedCM. |
| Step 4 | Access the Cisco Unified Reporting , RTMT, or the CLI to verify that database replication is occurring between existing nodes; if necessary, repair database
                                       replication between the nodes. |

| Tip | Make sure that the version that you install matches the version that runs on the publisher node. If the version that is running
                                                      on the publisher does not match your installation file, choose the Upgrade During Install option during the installation process.
                                                      For details, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service . |
|---|---|

| Note | You cannot use Cisco Unified Communications Manager Administration to change the server type after the server has been added. You must delete the existing server instance, and
                                          then add the new server again and choose the correct server type setting. |
|---|---|

| Step 1 | Select System > Server . The Find and List Servers window displays. |
|---|---|
| Step 2 | Click Add New . The Server Configuration - Add a Server window displays. |
| Step 3 | From the Server Type drop-down list box, choose the server type that you want to add, and then click Next . CUCM Video/Voice CUCM IM and Presence |
| Step 4 | In the Server Configuration window, enter the appropriate server settings. For server configuration field descriptions, see Server Settings . |
| Step 5 | Click Save . |

| Step 1 | Select System > Server . The Find and List Servers window appears. |
|---|---|
| Step 2 | Select the server search parameters, and then click Find . Matching records appear. |
| Step 3 | Select the IM and Presence server that is listed in the Find and List Servers window. The Server Configuration window appears. |
| Step 4 | Click on the Presence Server Status link in the IM and Presence Server Information section of the Server Configuration window. The Node Details window for the server appears. |

| Step 1 | Before you make any changes, check the Presence Topology window
                                       in Cisco Unified CM IM and Presence Administration window ( System > Presence Topology ). Take a record of the number of assigned
                                       users to each node in each Presence Redundancy Group. |
|---|---|
| Step 2 | Disable High Availability in each Presence Redundancy Group and
                                       wait at least two minutes for the new HA settings to
                                       synchronize. |
| Step 3 | Do whichever of the following is required for your update: Restart the Cisco XCP Router Restart the Cisco Presence Engine Restart the server |
| Step 4 | After the restart, monitor the number of active sessions on all
                                       nodes. |
| Step 5 | For each node, run the show perf query counter "Cisco Presence Engine" ActiveJsmSessions CLI command on each
                                       node to confirm the number of active sessions on each node. The
                                       number of active sessions should match the number that you recorded
                                       in step 1 for assigned users. It should take no more than 15
                                       minutes for all sessions to resume. |
| Step 6 | Once all of your sessions are created, you can
                                       enable High Availability within the Presence Redundancy
                                       Group. Note If 30 minutes passes and the active sessions haven't yet been created, restart the Cisco Presence Engine. If that doesn't
                                                      work, there is a larger system issue for you to fix. Note It is not recommended to do back-to-back restarts of the Cisco XCP Router and/or Cisco Presence Engine. However, if you do
                                                      need to do a restart: restart the first service, wait for all of the JSM sessions to be recreated. After all of the JSM sessions
                                                      are created, then do the second restart. | Note | If 30 minutes passes and the active sessions haven't yet been created, restart the Cisco Presence Engine. If that doesn't
                                                      work, there is a larger system issue for you to fix. | Note | It is not recommended to do back-to-back restarts of the Cisco XCP Router and/or Cisco Presence Engine. However, if you do
                                                      need to do a restart: restart the first service, wait for all of the JSM sessions to be recreated. After all of the JSM sessions
                                                      are created, then do the second restart. |
| Note | If 30 minutes passes and the active sessions haven't yet been created, restart the Cisco Presence Engine. If that doesn't
                                                      work, there is a larger system issue for you to fix. |
| Note | It is not recommended to do back-to-back restarts of the Cisco XCP Router and/or Cisco Presence Engine. However, if you do
                                                      need to do a restart: restart the first service, wait for all of the JSM sessions to be recreated. After all of the JSM sessions
                                                      are created, then do the second restart. |

| Note | If 30 minutes passes and the active sessions haven't yet been created, restart the Cisco Presence Engine. If that doesn't
                                                      work, there is a larger system issue for you to fix. |
|---|---|

| Note | It is not recommended to do back-to-back restarts of the Cisco XCP Router and/or Cisco Presence Engine. However, if you do
                                                      need to do a restart: restart the first service, wait for all of the JSM sessions to be recreated. After all of the JSM sessions
                                                      are created, then do the second restart. |
|---|---|

| Host Name Location | Allowed Configuration | Allowed Number of Characters | Recommended First Character for Host Name | Recommended Last Character for Host Name |
|---|---|---|---|---|
| Host Name/ IP Address field System > Server in Cisco Unified Communications Manager Administration | You can add or change the host name for a server in the cluster. | 2-63 | alphabetic | alphanumeric |
| Hostname field Cisco Unified Communications Manager installation wizard | You can add the host name for a server in the cluster. | 1-63 | alphabetic | alphanumeric |
| Hostname field Settings > IP > Ethernet in Cisco Unified Communications Operating System | You can change, not add, the host name for a server in the cluster. | 1-63 | alphabetic | alphanumeric |
| set network hostname hostname Command Line Interface | You can change, not add, the host name for a server in the cluster. | 1-63 | alphabetic | alphanumeric |

| Tip | The host name must follow the rules for ARPANET host names. Between
                                          			 the first and last character of the host name, you can enter alphanumeric
                                          			 characters and hyphens. |
|---|---|

| Tip | In addition to configuring Unified Communications Manager information on the DNS server, you enter DNS information during the Cisco
                                          			 Unified Communications Manager installation. |
|---|---|