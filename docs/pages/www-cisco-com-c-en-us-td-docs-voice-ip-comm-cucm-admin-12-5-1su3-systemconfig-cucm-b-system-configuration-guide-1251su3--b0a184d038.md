---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-systemconfig-cucm-b-system-configuration-guide-1251su3--b0a184d038
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/systemConfig/cucm_b_system-configuration-guide-1251su3/cucm_m_configure-enterprise-parameters-and-services.html
retrieved_at: 2026-08-16T17:40:49.214463+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Configure Enterprise Parameters and Services

## Chapter: Configure Enterprise Parameters and Services

# Configure Enterprise Parameters and Services

## Enterprise Parameters Overview

Enterprise parameters provide default settings that apply to all devices and services in the same cluster. A cluster comprises
                              a set of Cisco Unified Communications Managers that share the same database. When you install a new Cisco Unified Communications
                              Manager, it uses the enterprise parameters to set the initial values of its device defaults.

Many of the enterprise parameters rarely require change. Do not change an enterprise parameter unless you fully understand
                              the feature that you are changing or unless the Cisco Technical Assistance Center (TAC) specifies the change.

The recommended default settings should work in most cases.

Set the fall-back connection monitor duration for IP phones.

Allow searches of the corporate directory for all users.

Set the Fully Qualified Directory Number (FQDN) for the cluster and the top-level domain for the organization.

Set the Cisco Jabber start condition for video.

(Optional) Enable IPv6 if your network uses IPv6.

(Optional) Enter a remote syslog server name.

(Optional) Set up call trace log to troubleshoot your deployment.

(Optional) Enable dependency records.

## Service Parameters Overview

Service parameters let you configure different services on selected Unified Communications Manager servers. Unlike enterprise parameters, which apply to all services, each service gets configured with a separate set of service
                           parameters.

Service parameters let you configure settings for the following two types of services, both of which can be activated within
                           Cisco Unified Serviceability:

Feature Services - These services are used to run certain system features. You must turn feature services on in order to use them.

Network Services - Network services are on by default, but you can stop and start (or restart) a network service for troubleshooting purposes.
                                 These services includes services that allow system components like the database and platform to function properly.

You can view service parameter field descriptions for service parameters by by clicking the ? icon within the Service Parameter Configuration window, or by clicking on one of the parameter names.

## System Parameters Task Flow

### Before you begin

Set up your Unified Communications Manager node and port settings.

Step 1

Configure Enterprise Parameters .

Step 2

Activate Essential Services .

You can activate services on the node using Cisco Unified Serviceability.

Step 3

Configure Service Parameters .

Configure service parameters for the publisher and subscriber nodes in the cluster.

### Configure Enterprise Parameters

If you edit a parameter in Cisco Unified CM Administration, the new setting also reflects in Cisco Unified CM,  IM and Presence
                                             Administration.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

The Enterprise Parameters window displays the list of enterprise parameters.

Step 2

Edit any of the parameter settings.

For parameter descriptions, click the parameter name in the GUI. For more information on a list of common enterprise parameters,
                                             see Common Enterprise Parameters .

Step 3

Click Save .

Step 4

Click Reset , and then click OK to reset all devices.

Most parameters require that you reset devices after saving the setting. If you have registered devices, we recommend completing
                                                         all your configuration changes before resetting devices.

You can reset every device pool in the system to reset all the devices.

#### Common Enterprise Parameters

The following table lists common enterprise parameters that are used to set enterprise settings such as Organization Top-Level
                                    Domain or Cluster Fully Qualified Domain Name. For a detailed list, use the System > Enterprise Parameters menu in Cisco Unified CM Administration.

Parameter Name

Description

Enterprise Parameters

Connection Monitor Duration

If an IP phone in the cluster registers on a secondary node, use this parameter to set the amount of time that the IP phone
                                                waits before it falls back and re-registers with the primary node after the primary node becomes available. This parameter
                                                affects all secure devices for a specific Secure Survivable Remote Site Telephony (SRST) router.

For more information, see Security Guide for Cisco Unified Communications Manager .

Default: 120 seconds

Restart all services for the changes to take effect.

CCMAdmin Parameters

Enable Dependency Records

This parameter is used to display dependency records that are required for troubleshooting. Displaying the dependency records
                                                may be beneficial during an initial system setup.

Displaying the dependency records could lead to high CPU usage spikes and could impact call processing. To avoid possible
                                                performance issues, disable this parameter after the system setup is complete. We recommend displaying dependency records
                                                only during off-peak hours or during a maintenance window.

When enabled, you can select Dependency Records from the Related Links drop-down list, which is accessible from most configuration windows using Unified Communications Manager .

Default: False

User Data Service Parameters

Enable All User Search

This parameter allows you to search the corporate directory for all users when no last name, first name, or directory number
                                                is specified. This parameter also applies to directory searches on the Cisco CallManager Self Care (CCMUser) window.

Default: True

Clusterwide Domain Configuration

Organization Top Level Domain

This parameter defines the top-level domain for the organization. For example, cisco.com.

Maximum length: 255 characters

Allowed values: A valid domain using upper and lowercase letters, numbers (0-9), hyphens, and dots (as a domain label separator).
                                                Domain labels must not start with a hyphen. The last label must not start with a number. For example, this domain is invalid
                                                -cisco.1om.

Cluster Fully Qualified Domain Name

This parameter defines one or more Fully Qualified Domain Names (FQDN) for the cluster. Multiple FQDNs must be separated by
                                                a space. Specify wildcards within an FQDN using an asterisk (*). Example: cluster-1.cisco.com *.cisco.com .

Requests containing URLs, such as SIP calls, that have a host portion that matches any of the FQDNs in this parameter are
                                                routed to that cluster and the attached devices.

Maximum length: 255 characters

Allowed values: An FQDN or a partial FQDN using the * wildcard. Upper and lowercase letters, numbers (0-9), hyphens, and dots
                                                (as a domain label separator). Domain labels must not start with a hyphen. The last label must not start with a number. For
                                                example, this domain is invalid -cisco.1om.

IPv6

Enable IPv6

This parameter determines whether Unified Communications Manager can negotiate Internet Protocol Version 6 (IPv6) and whether phones are allowed to advertise IPv6 capability.

IPv6 must be enabled on all other network components including on the platform of all nodes before you enable this parameter.
                                                Otherwise, the system continues to run in IPv4-only mode.

This is a required field.

Default: False (IPv6 is disabled)

You must restart the following services for the IPv6 parameter change to take effect, and the affected services in the IM and Presence Service cluster.

Cisco CallManager

Cisco IP Voice Media Streaming App

Cisco CTIManager

Cisco Certificate Authority Proxy Function

Cisco Syslog Agent

Remote Syslog Server Name 1

Enter the name or IP address of the remote Syslog server. Cisco Unified Serviceability do not send the Syslog messages if
                                                a server name is not specified. This parameter is required only if you are using the Syslog server for logs.

Maximum length: 255 characters

Allowed values: A valid remote Sylog server name using upper and lowercase letters, numbers (0-9), hyphens, and dots.

Do not specify another Unified Communications Manager node as the destination.

Cisco Jabber

Never Start Call with Video

This parameter determines if video is sent when a video call starts. Select True to start video calls without immediately sending video. Anytime during the video call, you can choose to start sending your
                                                video.

This parameter overrides any IM and Presence Service preferences. When set to False, video calls start according to the preferences set in IM and Presence Service .

Default: False.

SSO and OAuth Configuration

SSO Login Behavior for iOS

This parameter is required to allow Cisco Jabber to perform the certificate-based authentication with the IdP in a controlled
                                                mobile device management (MDM) deployment.

The SSO Login Behavior for iOS parameter includes the following options:

Use Embedded Browser —If you enable this option, Cisco Jabber uses the embedded browser for the SSO authentication. Use this option to allow iOS
                                                      devices prior to version 9 to use SSO without cross-launching into the native Apple Safari browser.

Use Native Browser —If you enable this option, Cisco Jabber uses the Apple Safari framework on an iOS device to perform the certificate-based
                                                      authentication with an Identity Provider (IdP) in the MDM deployment.

We do not recommend configuring this option, except in a controlled MDM deployment, because using a native browser is not
                                                            as secure as the using the embedded browser.

This is a required field.

Default: Use the embedded browser (WebView).

OAuth with Refresh Login Flow

This parameter controls the login flow used by clients such as Cisco Jabber when connecting to Unified Communications Managers.

Enabled—If you enable this option, clients can use an oAuth-based Fast Login flow to provide a quicker and streamlined login
                                                      experience, without requiring the user input to re-log in. For example, due to a network change. The option requires support
                                                      from the other components of the Unified Communications solution, such as Expressway and Unity Connection (compatible versions
                                                      with the refresh login flow enabled).

Disabled—If you enable this option, the existing behavior is preserved and is compatible with older versions of other system
                                                      components.

For Mobile and Remote Access deployment with Cisco Jabber, we recommend enabling this parameter only with a compatible version
                                                                  of Expressway that supports oAuth with Refresh login flow. Incompatible version may impact the Cisco Jabber functionality.
                                                                  Please refer the specific product documents for supported version and configuration requirements.

This is a required field.

Default: Disabled.

Use SSO for RTMT

This parameter is configured to enable SAML SSO for Real-Time Monitoring Tool (RTMT).

The Use SSO for RTMT parameter includes the following options:

True —If you choose this option, RTMT displays the SAML SSO-based IdP sign-in window.

When you perform a fresh install, the default value of the Use SSO for RTMT parameter appears as True .

False —If you choose this option, RTMT displays the basic authentication sign-in window.

When you perform an upgrade from a Cisco Unified Communications Manager version where Use SSO for RTMT parameter does not exist, the default value of this parameter in the newer version appears as False .

This is a required field.

Default: True.

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

#### View Clusterwide Service Parameter Settings

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
| Step 1 | Configure Enterprise Parameters . | Configure the system-wide parameters that are required for an initial setup of your Unified Communications Manager node. |
| Step 2 | Activate Essential Services . | You can activate services on the node using Cisco Unified Serviceability. |
| Step 3 | Configure Service Parameters . | Configure service parameters for the publisher and subscriber nodes in the cluster. |

| Note | If you edit a parameter in Cisco Unified CM Administration, the new setting also reflects in Cisco Unified CM,  IM and Presence
                                             Administration. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . The Enterprise Parameters window displays the list of enterprise parameters. |
|---|---|
| Step 2 | Edit any of the parameter settings. For parameter descriptions, click the parameter name in the GUI. For more information on a list of common enterprise parameters,
                                             see Common Enterprise Parameters . |
| Step 3 | Click Save . |
| Step 4 | Click Reset , and then click OK to reset all devices. Note Most parameters require that you reset devices after saving the setting. If you have registered devices, we recommend completing
                                                         all your configuration changes before resetting devices. You can reset every device pool in the system to reset all the devices. | Note | Most parameters require that you reset devices after saving the setting. If you have registered devices, we recommend completing
                                                         all your configuration changes before resetting devices. You can reset every device pool in the system to reset all the devices. |
| Note | Most parameters require that you reset devices after saving the setting. If you have registered devices, we recommend completing
                                                         all your configuration changes before resetting devices. You can reset every device pool in the system to reset all the devices. |

| Note | Most parameters require that you reset devices after saving the setting. If you have registered devices, we recommend completing
                                                         all your configuration changes before resetting devices. You can reset every device pool in the system to reset all the devices. |
|---|---|

| Parameter Name | Description |
|---|---|
| Enterprise Parameters |
| Connection Monitor Duration | If an IP phone in the cluster registers on a secondary node, use this parameter to set the amount of time that the IP phone
                                                waits before it falls back and re-registers with the primary node after the primary node becomes available. This parameter
                                                affects all secure devices for a specific Secure Survivable Remote Site Telephony (SRST) router. For more information, see Security Guide for Cisco Unified Communications Manager . Default: 120 seconds Restart all services for the changes to take effect. |
| CCMAdmin Parameters |
| Enable Dependency Records | This parameter is used to display dependency records that are required for troubleshooting. Displaying the dependency records
                                                may be beneficial during an initial system setup. Displaying the dependency records could lead to high CPU usage spikes and could impact call processing. To avoid possible
                                                performance issues, disable this parameter after the system setup is complete. We recommend displaying dependency records
                                                only during off-peak hours or during a maintenance window. When enabled, you can select Dependency Records from the Related Links drop-down list, which is accessible from most configuration windows using Unified Communications Manager . Default: False |
| User Data Service Parameters |
| Enable All User Search | This parameter allows you to search the corporate directory for all users when no last name, first name, or directory number
                                                is specified. This parameter also applies to directory searches on the Cisco CallManager Self Care (CCMUser) window. Default: True |
| Clusterwide Domain Configuration |
| Organization Top Level Domain | This parameter defines the top-level domain for the organization. For example, cisco.com. Maximum length: 255 characters Allowed values: A valid domain using upper and lowercase letters, numbers (0-9), hyphens, and dots (as a domain label separator).
                                                Domain labels must not start with a hyphen. The last label must not start with a number. For example, this domain is invalid
                                                -cisco.1om. |
| Cluster Fully Qualified Domain Name | This parameter defines one or more Fully Qualified Domain Names (FQDN) for the cluster. Multiple FQDNs must be separated by
                                                a space. Specify wildcards within an FQDN using an asterisk (*). Example: cluster-1.cisco.com *.cisco.com . Requests containing URLs, such as SIP calls, that have a host portion that matches any of the FQDNs in this parameter are
                                                routed to that cluster and the attached devices. Maximum length: 255 characters Allowed values: An FQDN or a partial FQDN using the * wildcard. Upper and lowercase letters, numbers (0-9), hyphens, and dots
                                                (as a domain label separator). Domain labels must not start with a hyphen. The last label must not start with a number. For
                                                example, this domain is invalid -cisco.1om. |
| IPv6 |
| Enable IPv6 | This parameter determines whether Unified Communications Manager can negotiate Internet Protocol Version 6 (IPv6) and whether phones are allowed to advertise IPv6 capability. IPv6 must be enabled on all other network components including on the platform of all nodes before you enable this parameter.
                                                Otherwise, the system continues to run in IPv4-only mode. This is a required field. Default: False (IPv6 is disabled) You must restart the following services for the IPv6 parameter change to take effect, and the affected services in the IM and Presence Service cluster. Cisco CallManager Cisco IP Voice Media Streaming App Cisco CTIManager Cisco Certificate Authority Proxy Function |
| Cisco Syslog Agent |
| Remote Syslog Server Name 1 | Enter the name or IP address of the remote Syslog server. Cisco Unified Serviceability do not send the Syslog messages if
                                                a server name is not specified. This parameter is required only if you are using the Syslog server for logs. Maximum length: 255 characters Allowed values: A valid remote Sylog server name using upper and lowercase letters, numbers (0-9), hyphens, and dots. Do not specify another Unified Communications Manager node as the destination. |
| Cisco Jabber |
| Never Start Call with Video | This parameter determines if video is sent when a video call starts. Select True to start video calls without immediately sending video. Anytime during the video call, you can choose to start sending your
                                                video. This parameter overrides any IM and Presence Service preferences. When set to False, video calls start according to the preferences set in IM and Presence Service . Default: False. |
| SSO and OAuth Configuration |
| SSO Login Behavior for iOS | This parameter is required to allow Cisco Jabber to perform the certificate-based authentication with the IdP in a controlled
                                                mobile device management (MDM) deployment. The SSO Login Behavior for iOS parameter includes the following options: Use Embedded Browser —If you enable this option, Cisco Jabber uses the embedded browser for the SSO authentication. Use this option to allow iOS
                                                      devices prior to version 9 to use SSO without cross-launching into the native Apple Safari browser. Use Native Browser —If you enable this option, Cisco Jabber uses the Apple Safari framework on an iOS device to perform the certificate-based
                                                      authentication with an Identity Provider (IdP) in the MDM deployment. Note We do not recommend configuring this option, except in a controlled MDM deployment, because using a native browser is not
                                                            as secure as the using the embedded browser. This is a required field. Default: Use the embedded browser (WebView). | Note | We do not recommend configuring this option, except in a controlled MDM deployment, because using a native browser is not
                                                            as secure as the using the embedded browser. |
| Note | We do not recommend configuring this option, except in a controlled MDM deployment, because using a native browser is not
                                                            as secure as the using the embedded browser. |
| OAuth with Refresh Login Flow | This parameter controls the login flow used by clients such as Cisco Jabber when connecting to Unified Communications Managers. Enabled—If you enable this option, clients can use an oAuth-based Fast Login flow to provide a quicker and streamlined login
                                                      experience, without requiring the user input to re-log in. For example, due to a network change. The option requires support
                                                      from the other components of the Unified Communications solution, such as Expressway and Unity Connection (compatible versions
                                                      with the refresh login flow enabled). Disabled—If you enable this option, the existing behavior is preserved and is compatible with older versions of other system
                                                      components. Note For Mobile and Remote Access deployment with Cisco Jabber, we recommend enabling this parameter only with a compatible version
                                                                  of Expressway that supports oAuth with Refresh login flow. Incompatible version may impact the Cisco Jabber functionality.
                                                                  Please refer the specific product documents for supported version and configuration requirements. This is a required field. Default: Disabled. | Note | For Mobile and Remote Access deployment with Cisco Jabber, we recommend enabling this parameter only with a compatible version
                                                                  of Expressway that supports oAuth with Refresh login flow. Incompatible version may impact the Cisco Jabber functionality.
                                                                  Please refer the specific product documents for supported version and configuration requirements. |
| Note | For Mobile and Remote Access deployment with Cisco Jabber, we recommend enabling this parameter only with a compatible version
                                                                  of Expressway that supports oAuth with Refresh login flow. Incompatible version may impact the Cisco Jabber functionality.
                                                                  Please refer the specific product documents for supported version and configuration requirements. |
| Use SSO for RTMT | This parameter is configured to enable SAML SSO for Real-Time Monitoring Tool (RTMT). The Use SSO for RTMT parameter includes the following options: True —If you choose this option, RTMT displays the SAML SSO-based IdP sign-in window. Note When you perform a fresh install, the default value of the Use SSO for RTMT parameter appears as True . False —If you choose this option, RTMT displays the basic authentication sign-in window. Note When you perform an upgrade from a Cisco Unified Communications Manager version where Use SSO for RTMT parameter does not exist, the default value of this parameter in the newer version appears as False . This is a required field. Default: True. | Note | When you perform a fresh install, the default value of the Use SSO for RTMT parameter appears as True . | Note | When you perform an upgrade from a Cisco Unified Communications Manager version where Use SSO for RTMT parameter does not exist, the default value of this parameter in the newer version appears as False . |
| Note | When you perform a fresh install, the default value of the Use SSO for RTMT parameter appears as True . |
| Note | When you perform an upgrade from a Cisco Unified Communications Manager version where Use SSO for RTMT parameter does not exist, the default value of this parameter in the newer version appears as False . |

| Note | We do not recommend configuring this option, except in a controlled MDM deployment, because using a native browser is not
                                                            as secure as the using the embedded browser. |
|---|---|

| Note | For Mobile and Remote Access deployment with Cisco Jabber, we recommend enabling this parameter only with a compatible version
                                                                  of Expressway that supports oAuth with Refresh login flow. Incompatible version may impact the Cisco Jabber functionality.
                                                                  Please refer the specific product documents for supported version and configuration requirements. |
|---|---|

| Note | When you perform a fresh install, the default value of the Use SSO for RTMT parameter appears as True . |
|---|---|

| Note | When you perform an upgrade from a Cisco Unified Communications Manager version where Use SSO for RTMT parameter does not exist, the default value of this parameter in the newer version appears as False . |
|---|---|

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