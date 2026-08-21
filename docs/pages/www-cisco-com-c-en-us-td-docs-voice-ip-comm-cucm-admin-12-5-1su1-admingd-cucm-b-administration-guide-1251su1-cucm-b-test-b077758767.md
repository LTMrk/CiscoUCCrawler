---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-admingd-cucm-b-administration-guide-1251su1-cucm-b-test-b077758767
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/adminGd/cucm_b_administration-guide-1251SU1/cucm_b_test-adminguide_chapter_01000.html
retrieved_at: 2026-08-21T08:32:51.749998+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: April 8, 2025

Chapter: Monitor System Status

## Chapter: Monitor System Status

# Monitor System Status

## View Cluster Nodes Status

Use this procedure to show information about the nodes in your cluster.

Step 1

From Cisco Unified Operating System Administration, choose Show > Cluster .

Step 2

Review the fields in the Cluster window. See the online help for more information about the fields.

## View Hardware Status

Use this procedure to show the hardware status and information about hardware resources in your system.

Step 1

From the Cisco Unified Operating
                                          							 System Administration , select Show > Hardware .

Step 2

Review the
                                       			 fields in the Hardware
                                          				Status window. See the online help for more information about the fields.

## View Network Status

Use this procedure to show the network status of your system, such as ethernet and DNS information.

The network
                              		  status information that is displayed depends on whether Network Fault Tolerance is
                              		  enabled:

- If Network Fault Tolerance is enabled, Ethernet port 1 automatically
                                 		  manages network communications if Ethernet port 0 fails.

- If Network Fault
                                 		  Tolerance is enabled, network status information is displayed for the network ports
                                 		  Ethernet 0, Ethernet 1, and Bond 0.

- If Network Fault Tolerance is not enabled,
                                 		  status information is displayed for only Ethernet 0.

Step 1

From Cisco Unified Operating System Administration, choose Show > Network .

Step 2

Review the
                                       			 fields in the Network
                                          				Configuration window. 
                                       		   See the online help for more information about the fields.

## View Installed Software

Use this procedure to show information about software versions and installed software packages.

Step 1

From Cisco Unified Operating System Administration, choose Show > Software .

Step 2

Review the fields in the Software Packages window. See the online help for more information about the fields.

## View System Status

Use this procedure to show the overall system status, such as information about locales, up time, CPU use, and memory use.

Step 1

From Cisco Unified Operating System Administration, choose Show > System .

Step 2

Review the
                                       			 fields in the System
                                          				Status window. 
                                       		   See the online help for more information about the fields.

## View IP Preferences

Use this procedure to show a list of registered ports are available to the system.

Step 1

From Cisco Unified Operating System Administration , choose Show > IP
                                             				  Preferences .

Step 2

(Optional) To filter or search records, perform one of the following tasks:

- From the first list, select a search parameter.

- From the second list, select a search pattern.

- Specify the appropriate search text, if applicable.

Step 3

Click Find .

Step 4

Review the fields that appear  in the System Status window.
                                       		  See the online help for more information about the fields.

## View Last Login
                        	 Details

When end users (with either local and LDAP credentials) and
                              		  administrators log in to web applications for Cisco Unified Communications
                                 			 Manager or IM and Presence Service ,
                              		  the main application window displays the last successful and unsuccessful login
                              		  details.

Users logging in using SAML SSO feature can only view the last
                              		  successful system login information. The user can refer to the Identity
                              		  Provider (IdP) application to track the unsuccessful SAML SSO login
                              		  information.

The following web applications display the login attempt information:

Cisco Unified Communications
                                       				  Manager :

Cisco Unified CM Administration

Cisco Unified Reporting

Cisco Unified Serviceability

IM and Presence Service

Cisco Unified CM IM and Presence Administration

Cisco Unified IM and Presence Reporting

Cisco Unified IM and Presence Serviceability

Disaster Recovery System

Cisco Unified OS Administration

## Ping a Node

Use the Ping Utility to ping another node in
                              		  the network. These results can help you verify or troubleshoot device connectivity.

Step 1

From Cisco Unified Operating System Administration, choose Services > Ping .

Step 2

Configure the fields on the Ping Configuration window. See the online help for more information about the fields and their configuration options.

Step 3

Choose Ping .

The ping results are displayed.

## Display Service Parameters

You may need to compare all service parameters that belong to a particular service on all servers in a cluster. You may also
                              need to display only out-of-sync parameters (that is, service parameters for which values differ from one server to another)
                              or parameters that have been modified from the suggested value.

Use the following procedure to display the service parameters for a particular service on all servers in a cluster.

Step 1

Choose System > Service Parameters .

Step 2

From the Server drop-down list box, choose a server.

Step 3

From the Service drop-down list box, choose the service for which you want to display the service parameters on all servers
                                       in a cluster.

The Service Parameter Configuration window displays all services (active or not active).

Step 4

In the Service Parameter Configuration window that displays, choose Parameters for All Servers in The Related Links Drop-down
                                       List Box; then, click Go.

The Parameters for All Servers window displays. For the current service, the list shows all parameters in alphabetical order.
                                          For each parameter, the suggested value displays next to the parameter name. Under each parameter name, a list of servers
                                          that contain this parameter displays. Next to each server name, the current value for this parameter on this server displays.

For a given parameter, click on the server name or on the current parameter value to link to the corresponding service parameter
                                          window to change the value. Click Previous and Next to navigate between Parameters for All Servers windows.

Step 5

If you need to display out-of-sync service parameters, choose Out of Sync Parameters for All Servers in the Related Links
                                       drop-down list box, then click Go.

The Out of Sync Parameters for All Servers window displays. For the current service, service parameters that have different
                                          values on different servers display in alphabetical order. For each parameter, the suggested value displays next to the parameter
                                          name. Under each parameter name, a list of servers that contain this parameter displays. Next to each server name, the current
                                          value for this parameter on this server displays.

For a given parameter, click the server name or the current parameter value to link to the corresponding service parameter
                                          window to change the value. Click Previous and Next to navigate between Out of Sync Parameters for All Servers windows.

Step 6

If you need to display service parameters that have been modified from the suggested value, choose Modified Parameters for
                                       All Servers in the Related Links drop-down list box; then, click Go.

The Modified Parameters for All Servers window displays. For the current service, service parameters that have values that
                                          differ from the suggested values display in alphabetical order. For each parameter, the suggested value displays next to the
                                          parameter name. Under each parameter name, a list of servers that have different values from the suggested values displays.
                                          Next to each server name, the current value for this parameter on this server displays.

For a given parameter, click the server name or the current parameter value to link to the corresponding service parameter
                                          window to change the value. Click Previous and Next to navigate between Modified Parameters for All Servers windows.

## Configure Network DNS

Use this procedure to set your network DNS

You can also assign a DNS primary and secondary server via the DHCP Configuration window in Cisco Unified CM Administration.

Step 1

Log in to the Command Line Interface.

Step 2

If you want to assign a DNS server, run one of the following commandson the publisher node:

To assign the primary DNS server run set network dns primary <ip_address>

To assign the secondary DNS server run the set network dns secondary <ip_address>

Step 3

To assign additional DNS option run the set network dns options [timeout| seconds] [attempts| number] [rotate].

Timeout Sets the DNS timeout

Seconds is the number of seconds for the timeout

Attempts Sets the number of times to attempt a DNS request

Number specifies the number of attempts

Rotate causes the system to rotate among the configured DNS servers and distribute the load

For example, set network dns options timeout 60 attempts 4 rotate

The server reboots after you run this command.

| Step 1 | From Cisco Unified Operating System Administration, choose Show > Cluster . |
|---|---|
| Step 2 | Review the fields in the Cluster window. See the online help for more information about the fields. |

| Step 1 | From the Cisco Unified Operating
                                          							 System Administration , select Show > Hardware . |
|---|---|
| Step 2 | Review the
                                       			 fields in the Hardware
                                          				Status window. See the online help for more information about the fields. |

| Step 1 | From Cisco Unified Operating System Administration, choose Show > Network . |
|---|---|
| Step 2 | Review the
                                       			 fields in the Network
                                          				Configuration window. 
                                       		   See the online help for more information about the fields. |

| Step 1 | From Cisco Unified Operating System Administration, choose Show > Software . |
|---|---|
| Step 2 | Review the fields in the Software Packages window. See the online help for more information about the fields. |

| Step 1 | From Cisco Unified Operating System Administration, choose Show > System . |
|---|---|
| Step 2 | Review the
                                       			 fields in the System
                                          				Status window. 
                                       		   See the online help for more information about the fields. |

| Step 1 | From Cisco Unified Operating System Administration , choose Show > IP
                                             				  Preferences . |
|---|---|
| Step 2 | (Optional) To filter or search records, perform one of the following tasks: From the first list, select a search parameter. From the second list, select a search pattern. Specify the appropriate search text, if applicable. |
| Step 3 | Click Find . |
| Step 4 | Review the fields that appear  in the System Status window.
                                       		  See the online help for more information about the fields. |

| Step 1 | From Cisco Unified Operating System Administration, choose Services > Ping . |
|---|---|
| Step 2 | Configure the fields on the Ping Configuration window. See the online help for more information about the fields and their configuration options. |
| Step 3 | Choose Ping . The ping results are displayed. |

| Step 1 | Choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list box, choose a server. |
| Step 3 | From the Service drop-down list box, choose the service for which you want to display the service parameters on all servers
                                       in a cluster. Note The Service Parameter Configuration window displays all services (active or not active). | Note | The Service Parameter Configuration window displays all services (active or not active). |
| Note | The Service Parameter Configuration window displays all services (active or not active). |
| Step 4 | In the Service Parameter Configuration window that displays, choose Parameters for All Servers in The Related Links Drop-down
                                       List Box; then, click Go. The Parameters for All Servers window displays. For the current service, the list shows all parameters in alphabetical order.
                                          For each parameter, the suggested value displays next to the parameter name. Under each parameter name, a list of servers
                                          that contain this parameter displays. Next to each server name, the current value for this parameter on this server displays. For a given parameter, click on the server name or on the current parameter value to link to the corresponding service parameter
                                          window to change the value. Click Previous and Next to navigate between Parameters for All Servers windows. |
| Step 5 | If you need to display out-of-sync service parameters, choose Out of Sync Parameters for All Servers in the Related Links
                                       drop-down list box, then click Go. The Out of Sync Parameters for All Servers window displays. For the current service, service parameters that have different
                                          values on different servers display in alphabetical order. For each parameter, the suggested value displays next to the parameter
                                          name. Under each parameter name, a list of servers that contain this parameter displays. Next to each server name, the current
                                          value for this parameter on this server displays. For a given parameter, click the server name or the current parameter value to link to the corresponding service parameter
                                          window to change the value. Click Previous and Next to navigate between Out of Sync Parameters for All Servers windows. |
| Step 6 | If you need to display service parameters that have been modified from the suggested value, choose Modified Parameters for
                                       All Servers in the Related Links drop-down list box; then, click Go. The Modified Parameters for All Servers window displays. For the current service, service parameters that have values that
                                          differ from the suggested values display in alphabetical order. For each parameter, the suggested value displays next to the
                                          parameter name. Under each parameter name, a list of servers that have different values from the suggested values displays.
                                          Next to each server name, the current value for this parameter on this server displays. For a given parameter, click the server name or the current parameter value to link to the corresponding service parameter
                                          window to change the value. Click Previous and Next to navigate between Modified Parameters for All Servers windows. |

| Note | The Service Parameter Configuration window displays all services (active or not active). |
|---|---|

| Note | You can also assign a DNS primary and secondary server via the DHCP Configuration window in Cisco Unified CM Administration. |
|---|---|

| Step 1 | Log in to the Command Line Interface. |
|---|---|
| Step 2 | If you want to assign a DNS server, run one of the following commandson the publisher node: To assign the primary DNS server run set network dns primary <ip_address> To assign the secondary DNS server run the set network dns secondary <ip_address> |
| Step 3 | To assign additional DNS option run the set network dns options [timeout\| seconds] [attempts\| number] [rotate]. Timeout Sets the DNS timeout Seconds is the number of seconds for the timeout Attempts Sets the number of times to attempt a DNS request Number specifies the number of attempts Rotate causes the system to rotate among the configured DNS servers and distribute the load For example, set network dns options timeout 60 attempts 4 rotate The server reboots after you run this command. |