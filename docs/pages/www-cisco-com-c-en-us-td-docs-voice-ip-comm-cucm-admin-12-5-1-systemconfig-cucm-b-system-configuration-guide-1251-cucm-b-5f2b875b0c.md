---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-5f2b875b0c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0101.html
retrieved_at: 2026-08-16T17:29:47.170083+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Service Parameters

## Chapter: Configure Service Parameters

# Configure Service Parameters

## Service Parameters Overview

Service parameters let you configure different services on selected Unified Communications Manager servers. Unlike enterprise parameters, which apply to all services, each service gets configured with a separate set of service
                           parameters.

Service parameters let you configure settings for the following two types of services, both of which can be activated within
                           Cisco Unified Serviceability:

Feature Services - These services are used to run certain system features. You must turn feature services on in order to use them.

Network Services - Network services are on by default, but you can stop and start (or restart) a network service for troubleshooting purposes.
                                 These services includes services that allow system components like the database and platform to function properly.

You can view service parameter field descriptions for service parameters by by clicking the ? icon within the Service Parameter Configuration window, or by clicking on one of the parameter names.

## Service Parameters Configuration Task Flow

Step 1

Activate Essential Services

You can activate and deactivate services on the node using Cisco Unified Serviceability. For a list of  the recommended services
                                          for publisher nodes, see Recommended Services for Publisher Nodes . For a list of the recommended services for subscriber nodes, see Recommended Services for Subscriber Nodes .

Step 2

Configure Service Parameters

Configure service parameters for the Cisco Unified Communications Manager publisher node and for subscriber nodes in the cluster.

Step 3

View Clusterwide Service Parameter Settings

You can display the services for your nodes using Cisco Unified Communications Manager Administration and Cisco Unified Serviceability. To view service parameter settings and parameter descriptions, use Cisco Unified Communications Manager Administration .

### Activate Essential Services

Use this procedure to activate services across the cluster.

For a list of recommended services for publisher nodes and subscriber nodes, see the following topics:

Recommended Services for Publisher Nodes

Recommended Services for Subscriber Nodes

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

Select a Server from the drop-down menu and click Go .

The services and their current status display.

Step 3

Activate and deactivate the services that you want:

- To activate a service, check the check box beside the service that you want to activate.

- To deactivate a service, uncheck the check box beside the service that you want to deactivate.

Step 4

Click Save .

#### Recommended Services for Publisher Nodes

The following table lists recommended services for a Unified Communications Manager publisher node when using a non-dedicated TFTP server.

Type

Service Name

CM Services

Cisco CallManager

Cisco Unified Mobile Voice Access Services

Cisco IP Voice Media Streaming App

Cisco CTIManager

Cisco Extended Functions

Cisco Intercluster Lookup Service

Cisco Location Bandwidth Manager

Cisco TFTP

CTI Services

Cisco IP Manager Assistant

Cisco WebDialer Web Service

CDR Services

Cisco SOAP - CDRonDemand Service

Cisco CAR Web Service

Database and Admin Services

Cisco Bulk Provisioning Service

AXL Web Service

Cisco URL Web Service

Performance and Monitoring Services

Cisco Serviceability Reporter

Security Services

Cisco Certificate Authority Proxy Function (CAPF)

Directory Services

Cisco DirSync

Cisco Certificate Authority Proxy Function

Tip

You can safely disable the following services if you do not plan to use them:

Cisco Messaging Interface

Cisco DHCP Monitor Service

Cisco TAPS Service

Cisco Directory Number Alias Sync

Cisco Directory Number Alias SyncCisco Dialed Number Analyzer Server

Cisco Dialed Number Analyzer

Self Provisioning IVR

#### Recommended Services for Subscriber Nodes

The following table lists recommended services for a Unified Communications Manager subscriber node when using a non-dedicated TFTP server.

Tip

You can safely disable the other services if you don't plan to use them.

Type

Service Name

CM Services

Cisco CallManager

Cisco IP Voice Media Streaming App

Cisco CTIManager

Cisco Extension Mobility

Cisco Extended Functions

Cisco TFTP

You must activate the following services on each IM and Presence Service node in your cluster.

Cisco SIP Proxy

Cisco Presence Engine

Cisco XCP Connection Manager

Cisco XCP Authentication Service

### Configure Service Parameters

You can configure the service parameters on the node using Cisco Unified Communications Manager Administration . Service parameters that are marked as cluster-wide affect all nodes in the cluster.

Caution

#### Before you begin

Make sure that the Unified Communications Manager nodes are configured.

Make sure that the service is active. For details, see Activate Essential Services .

Step 1

From Cisco Unified CM Administration, choose choose System > Service Parameters .

Step 2

Select a node in the Server drop-down list.

Step 3

Select a service in the Service drop-down list.

Tip

Step 4

Click Advanced to view the full list of parameters.

Step 5

Modify the service parameters and then click Save .

The window refreshes and the service parameter values are updated.

You can click the Set to Default button to update all parameters to the suggested value that appears after the Parameter Value field. If a parameter does not have a suggested value, the service parameter value does not change when you click the Set to Default button.

### View Clusterwide Service Parameter Settings

You can use Cisco Unified Communications Manager Assistant and Cisco Unified Serviceability to view the status of services for nodes in your cluster. To view service parameter settings
                                 and parameter descriptions, use Cisco Unified Communications Manager Assistant .

Step 1

To display services and view service parameter settings for a node using Cisco Unified Communications Manager Assistant , perform the following steps.

Select System > Service Parameters .

In the Service Parameters Configuration window, select a node in the Server drop-down box.

Select a service in the Service drop-down box.

All parameters that apply to the selected node appear. Parameters that appear in the Clusterwide Parameters (General) section apply to all nodes in the cluster.

Click the ( ? ) icon in the Service Parameter Configuration window to view a list of service parameters along with their descriptions.

Step 2

To display the service parameters for a particular service on all nodes in a cluster, select Parameters for All Servers in the Related Links drop-down box in the Service Parameters Configuration window,  then click Go .

The Parameters for All Servers window appears.  You can click on a server name that is listed or on a parameter value to open the related Service Parameter Configuration window.

Step 3

To display out-of-sync service parameters for a particular service on all nodes in a cluster, select Out of Sync Parameters for All Servers in the Related Links drop-down box in the Parameters for All Servers window,  then click Go .

The Out of Sync Parameters for All Servers window appears.  You can click on a server name that is listed or on a parameter value to open the related Service Parameter Configuration window.

| Note | If you deactivate a service, Unified Communications Manager retains any updated service parameter values. If you start the service again, Unified Communications Manager sets the service parameters to the changed values. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate Essential Services | You can activate and deactivate services on the node using Cisco Unified Serviceability. For a list of  the recommended services
                                          for publisher nodes, see Recommended Services for Publisher Nodes . For a list of the recommended services for subscriber nodes, see Recommended Services for Subscriber Nodes . |
| Step 2 | Configure Service Parameters | Configure service parameters for the Cisco Unified Communications Manager publisher node and for subscriber nodes in the cluster. |
| Step 3 | View Clusterwide Service Parameter Settings | You can display the services for your nodes using Cisco Unified Communications Manager Administration and Cisco Unified Serviceability. To view service parameter settings and parameter descriptions, use Cisco Unified Communications Manager Administration . |

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | Select a Server from the drop-down menu and click Go . The services and their current status display. |
| Step 3 | Activate and deactivate the services that you want: To activate a service, check the check box beside the service that you want to activate. To deactivate a service, uncheck the check box beside the service that you want to deactivate. |
| Step 4 | Click Save . Service activation may take a few minutes to complete. refresh the page to confirm the status change. |

| Type | Service Name |
|---|---|
| CM Services | Cisco CallManager |
| Cisco Unified Mobile Voice Access Services |
| Cisco IP Voice Media Streaming App |
| Cisco CTIManager |
| Cisco Extended Functions |
| Cisco Intercluster Lookup Service |
| Cisco Location Bandwidth Manager |
| Cisco TFTP |
| CTI Services | Cisco IP Manager Assistant |
| Cisco WebDialer Web Service |
| CDR Services | Cisco SOAP - CDRonDemand Service |
| Cisco CAR Web Service |
| Database and Admin Services | Cisco Bulk Provisioning Service |
| AXL Web Service |
| Cisco URL Web Service |
| Performance and Monitoring Services | Cisco Serviceability Reporter |
| Security Services | Cisco Certificate Authority Proxy Function (CAPF) |
| Directory Services | Cisco DirSync Cisco Certificate Authority Proxy Function |

| Tip | You can safely disable the following services if you do not plan to use them: Cisco Messaging Interface Cisco DHCP Monitor Service Cisco TAPS Service Cisco Directory Number Alias Sync Cisco Directory Number Alias SyncCisco Dialed Number Analyzer Server Cisco Dialed Number Analyzer Self Provisioning IVR |
|---|---|

| Tip | You can safely disable the other services if you don't plan to use them. |
|---|---|

| Type | Service Name |
|---|---|
| CM Services | Cisco CallManager |
| Cisco IP Voice Media Streaming App |
| Cisco CTIManager |
| Cisco Extension Mobility |
| Cisco Extended Functions |
| Cisco TFTP |

| Caution | Some changes to service parameters can cause system failure. We recommend that you do not make any changes to service parameters
                                          unless you fully understand the feature that you are changing or unless the Cisco Technical Assistance Center (TAC) specifies
                                          the changes. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose choose System > Service Parameters . |
|---|---|
| Step 2 | Select a node in the Server drop-down list. |
| Step 3 | Select a service in the Service drop-down list. Tip Click the ? icon in the Service Parameter Configuration window to view a list of service parameters along with their descriptions. | Tip | Click the ? icon in the Service Parameter Configuration window to view a list of service parameters along with their descriptions. |
| Tip | Click the ? icon in the Service Parameter Configuration window to view a list of service parameters along with their descriptions. |
| Step 4 | Click Advanced to view the full list of parameters. |
| Step 5 | Modify the service parameters and then click Save . The window refreshes and the service parameter values are updated. You can click the Set to Default button to update all parameters to the suggested value that appears after the Parameter Value field. If a parameter does not have a suggested value, the service parameter value does not change when you click the Set to Default button. |

| Tip | Click the ? icon in the Service Parameter Configuration window to view a list of service parameters along with their descriptions. |
|---|---|

| Step 1 | To display services and view service parameter settings for a node using Cisco Unified Communications Manager Assistant , perform the following steps. Select System > Service Parameters . In the Service Parameters Configuration window, select a node in the Server drop-down box. Select a service in the Service drop-down box. All parameters that apply to the selected node appear. Parameters that appear in the Clusterwide Parameters (General) section apply to all nodes in the cluster. Click the ( ? ) icon in the Service Parameter Configuration window to view a list of service parameters along with their descriptions. |
|---|---|
| Step 2 | To display the service parameters for a particular service on all nodes in a cluster, select Parameters for All Servers in the Related Links drop-down box in the Service Parameters Configuration window,  then click Go . The Parameters for All Servers window appears.  You can click on a server name that is listed or on a parameter value to open the related Service Parameter Configuration window. |
| Step 3 | To display out-of-sync service parameters for a particular service on all nodes in a cluster, select Out of Sync Parameters for All Servers in the Related Links drop-down box in the Parameters for All Servers window,  then click Go . The Out of Sync Parameters for All Servers window appears.  You can click on a server name that is listed or on a parameter value to open the related Service Parameter Configuration window. |