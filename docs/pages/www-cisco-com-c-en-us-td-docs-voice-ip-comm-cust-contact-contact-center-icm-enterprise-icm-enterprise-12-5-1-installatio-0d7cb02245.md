---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-0d7cb02245
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_cti-os-system-manager-guide12-5/ucce_b_cti-os-system-manager-guide12-5_chapter_010.html
retrieved_at: 2026-08-16T20:06:58.868978+00:00
---

CTI OS System Manager Guide for Cisco Unified ICM, Release 12.5(1)

# CTI OS System Manager Guide for Cisco Unified ICM, Release 12.5(1)

Updated: February 6, 2020

Chapter: CTI OS Server
	 Installation

## Chapter: CTI OS Server
	 Installation

# CTI OS Server
                     	 Installation

This chapter
                        		lists some guidelines to consider when you install the CTI OS Server and
                        		provides procedures for these tasks.

You cannot run the
                                    		  installer remotely. Mount the installer ISO file only to a local machine.
                                    		  Various errors can occur during installation over the network. Keep in mind
                                    		  that for installation of major releases, there is no way to roll the
                                    		  installation back to the previous release if the installation or upgrade fails
                                    		  part way through.

## CTI OS Server Installation Guidelines

Following
                              		  are some guidelines to consider when you install CTI OS Server:

CTI OS is
                                    				typically installed in a redundant configuration. Two CTI OS Servers installed on
                                    				separate systems work in parallel to provide redundancy. Installing only one
                                    				CTI OS Server prevents failover recovery by client systems.

CTI OS must be
                                    				colocated on the same box as the PG/CG.

Ensure that your CTI OS system meets the specified requirements. See the Contact Center Enterprise Compatibility Matrix for more information.

You cannot run the
                                          		  installer remotely. Mount the installer ISO file only to a local machine.
                                          		  Various errors can occur during installation over the network. Keep in mind
                                          		  that for installation of major releases, there is no way to roll the
                                          		  installation back to the previous release if the installation or upgrade fails
                                          		  part way through.

## Upgrade from Previous Version

If you are upgrading from a CTI OS Server Release 12.0, you need not uninstall CTI OS Server before you install CTI OS Server
                                          Release 12.5(1).

While installing CTI OS Server 12.5(1), the listen ports for CTI OS Server and silent monitor are registered as firewall exceptions.

Silent upgrade is not supported for CTI OS Security Server and Client.

Run the Setup.exe .

A warning message appears indicating that the Cisco Contact Center SNMP Management Service is stopped before the CTI OS Server
                                          begins to install.

Click Yes to continue.

In the Software License Agreement dialog box, click Yes .

In the CTI OS Server Installer dialog box, leave the Location field blank and click Next .

The CTI OS Instances dialog box is displayed. Click Upgrade All .

In case you have a version of CTI OS Server already installed, and you are attempting to install the latest version, the 
                                       dialog box to confirm the upgrade is displayed. Click Yes .

## Install CTI OS
                        	 Server

To
                              		  install a new CTI OS Server, perform the following steps:

The CTI OS
                                          			 Server installation procedure includes windows for mobile agents and silent
                                          			 monitor server.

From the
                                       			 Server directory on the CD, run setup.exe .

A warning message appears indicating that the Cisco Contact Center SNMP Management Service is stopped before the CTI OS Server
                                          begins to install.

When you run programs from a Windows Server system with User Account Control enabled, Windows needs your permission to continue.
                                                      Click Yes in the User Account Control window to run the program.

Click Yes to continue.

In the Software License Agreement window, click Yes .

In the CTI OS Server Installer window, leave the Location field blank and click Next .

The CTI OS Instances window appears.

The CTI OS Instances window allows you to create CTI OS instances and add CTI OS Servers to a configured instance of CTI OS.

The Add buttons are disabled if you cannot create another CTI OS instance.

Under the CTI OS Instance List, click Add . The Add CTIOS Server Instance window is displayed.

Enter an instance name and click OK . For example, if you enter an instance called cisco , the following window appears:

Click Add in the CTI OS Server List.

The Add CTIOS Server window appears.

The CTIOS Server Name field is populated with the instance name you provided, followed by the next available index for a CTI
                                          OS Server. If a CTI OS Server has been deleted, the CTIOS Server Name is populated with the index that was deleted.

If you are installing CTI OS Server for the first time, an Enter Desktop Drive window appears. Accept the default installation drive or choose another drive from the Drive drop-down list.

Click OK .

The CTI Server Information window appears.

The Instance Name and CTIOS Server Name is already populated.

For secured connection with the CTI server, check the Enable Secure Connection check box.

For secured connection, you must provide the secure port number of the CTI Server.

If the Enable Secure Connection check box is not checked, the connection established between the CTIOS Server and the CTI
                                                      Server is non-secured. In this case, you must provide the non-secure port number of the CTI Server.

Before you enable secured connection between the components, ensure to complete the security certificate management process.

For more information, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

Enter the Name or IP Address and the Port Number for your CTI Server.

If the peripheral is configured for a previous CTI OS Server, the Name or IP Address field pre-populates with the name of that CTI OS Server.

Click Next .

The Peripheral Identifier window appears.

The Peripheral Type field is pre-populated with the peripheral type if it is already configured for a previous CTI OS Server.

When you
                                                      				  configure multiple CTI OS Servers to use a single CTI Server, every CTI OS
                                                      				  Server configured after the first CTI OS Server has the same configuration as
                                                      				  of the first CTI OS Server.

If the
                                       			 peripheral has not been configured for a previous CTI OS Server, specify the
                                       			 following information:

A Logical Name for your peripheral. The name can be
                                                					 any valid logical name that uniquely identifies your peripheral.

The
                                                            						Login By and Enable Mobile Agent group boxes are enabled only for UCCE
                                                            						peripheral types (UCCE System and UCCEHosted Edition).

In the
                                                            						Login By box, you can choose between signing in by Agent ID or by Login Name.
                                                            						The Login By setting determines how the CTI Toolkit Agent and Supervisor
                                                            						Desktops allow Login and Chat request (either Agent ID or Login Name). This
                                                            						setting does not affect other CTI applications. CTI OS Server itself can
                                                            						service Login requests both ways (by Agent ID and Login Name) for UCCE.

In the Peripheral ID field, enter the identifier of the
                                                					 switch that your phone is connected to.

From the Peripheral Type drop-down list, choose the switch
                                                					 that your phone is connected to.

Check
                                                					 the Enable Mobile Agent check box to activate this
                                                					 option.

Select the Login By option.

The Mobile agent mode drop-down lists the following options. Choose one:

Agent chooses —Agent chooses the mode.

Call by call —The agent's remote phone is dialed for
                                                      						  each individual call.

Nailed connection —The agent is called once upon
                                                      						  signing in and remains connected.

You can
                                                      				  specify information for only one peripheral during CTI OS Server setup. To
                                                      				  configure more peripherals, follow the procedure in the section Configure Additional Peripherals .

Click Next .

The Connection Information window appears.

Enter the port number and the heartbeat information for your CTI
                                          				OS Server instance.

For all peripheral types, accept the default Listen Port value of 42028. For subsequent instances, use any available port.

Ensure
                                                      				  that you configure the CTI OS client that connects to the CTI OS Server with
                                                      				  the same port that you selected while installing the CTI OS client.

Click Next .

The Statistics Information window appears.

- Enabling CAD Agent
                                                         					 disables the agent statistics polling interval from the CTI OS Server. CAD
                                                         					 agents receive only Skillgroup statistics from CTI OS Server.

After
                                                            						performing an Upgrade All , rerun setup to access this window and
                                                            						reconfigure the server for appropriate statistical information.

Enter the
                                       			 default polling interval for Skillgroup statistics (in seconds).

Because Quality of Service (QoS) enablement and statistics enablement are mutually exclusive, enabling QoS zeros disables
                                                      all the information relating to statistics.

Click Next .

The UCCE Silent Monitor Type window appears.

Choose the
                                       			 type of silent monitor.

If you
                                             				  choose Unified CM Based or Disabled , clicking Next takes you to the Peer CTI OS Server window. Proceed to Step 17.

If you
                                                         					 want to use Unified CM based type silent monitor, see Unified Communications Manager-Based Silent Monitor Configuration .

If you
                                             				  choose Disabled , the CTI OS based silent monitor is
                                             				  configured, but disabled. This sets the registry settings to the following
                                             				  values:

Key

Setting

HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\IPCCSilentMonitor\Name\Settings\CCMBasedSilentMonitor

0

HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\Login\ConnectionProfiles\Name\UCCE\
                                                         IPCCSilentMonitorEnabled

0

If you
                                             				  choose CTI OS Based silent monitor, clicking Next takes you to the Silent Monitor Information window.

On the Silent Monitor Information window, enter the following information:

The port number used by the client to connect to the silent monitor service.

The set of silent monitor servers that the desktop connects to. The desktop randomly connects to one of the silent monitor
                                                servers specified here. If the client is configured to use secure connections, the client attempts to connect to the silent
                                                monitor server using a secure connection. If the silent monitor server is configured to use secure connections, then a secure
                                                connection is established with the silent monitor server. Otherwise, an unsecured connection is used.

A client uses the same certificates it uses to communicate with CTI OS Server to establish a secure connection to the silent
                                                monitor server.

Click Next .

The Peer CTIOS Server window appears.

You can configure a CTI OS Peer Server using this window. You can also configure Chat and CTI OS silent monitoring. Enter
                                       the Peer CTI OS Server and Port details.

After you click Finish and the files are created, the service is registered and entries to the registry are made.

You can configure the chat window to beep every time a new message arrives. To do that, set the following registry key to
                                                      a nonzero value.

HKEY_LOCAL_MACHINE\Cisco Systems, Inc.\CTI Desktop\CtiOs\BeepOnMsgReceived

If the registry key does not exist or if its value is set to zero, the chat window does not beep.

The CTI OS Server Security window appears.

If you wish to disable security, click OK ; otherwise, select the Enable Security check box, enter the appropriate information, and click OK .

To simplify deployments, either enable or disable security for all CTI OS components (clients, CTI OS Server, and silent monitor
                                                      server).

The CTI OS Security InstallShield Wizard appears if you have enabled security:

After the CTI OS Server security installation is complete, click Finish .

CTI OS
                                                				  Multi-Instance setup does not allow two or more CTI OS Servers to connect to
                                                				  the same CTI Server.

The setup
                                                				  does not allow two or more CTI OS Servers to use the same listen port.

Rerun the
                                                				  CTI OS Server setup after you complete the installation.

## Uninstalling CTI OS Server

To uninstall the CTI OS Server, rerun the Setup program for the previous release and delete the Unified ICM Customer Instance
                              that you specified during CTI OS Server Setup.

## Determine Version
                        	 Number of Installed Files

You can determine the version number of an installed CTI OS Server file by
                              		  performing the following steps.

Open a window
                                       			 for the ICM\CTIOS_bin subdirectory.

Highlight the
                                       			 file ctiosservernode.exe .

Right-click the
                                       			 highlighted file.

Select Properties from the drop-down menu.

Select the Details tab.

This tab contains version information (release number and build number) for the file.

| Caution | You cannot run the
                                    		  installer remotely. Mount the installer ISO file only to a local machine.
                                    		  Various errors can occur during installation over the network. Keep in mind
                                    		  that for installation of major releases, there is no way to roll the
                                    		  installation back to the previous release if the installation or upgrade fails
                                    		  part way through. |
|---|---|

| Caution | You cannot run the
                                          		  installer remotely. Mount the installer ISO file only to a local machine.
                                          		  Various errors can occur during installation over the network. Keep in mind
                                          		  that for installation of major releases, there is no way to roll the
                                          		  installation back to the previous release if the installation or upgrade fails
                                          		  part way through. |
|---|---|

| Note | If you are upgrading from a CTI OS Server Release 12.0, you need not uninstall CTI OS Server before you install CTI OS Server
                                          Release 12.5(1). While installing CTI OS Server 12.5(1), the listen ports for CTI OS Server and silent monitor are registered as firewall exceptions. Silent upgrade is not supported for CTI OS Security Server and Client. |
|---|---|

| Step 1 | Run the Setup.exe . A warning message appears indicating that the Cisco Contact Center SNMP Management Service is stopped before the CTI OS Server
                                          begins to install. Click Yes to continue. |
|---|---|
| Step 2 | In the Software License Agreement dialog box, click Yes . |
| Step 3 | In the CTI OS Server Installer dialog box, leave the Location field blank and click Next . |
| Step 4 | The CTI OS Instances dialog box is displayed. Click Upgrade All . |
| Step 5 | In case you have a version of CTI OS Server already installed, and you are attempting to install the latest version, the 
                                       dialog box to confirm the upgrade is displayed. Click Yes . |

| Note | The CTI OS
                                          			 Server installation procedure includes windows for mobile agents and silent
                                          			 monitor server. |
|---|---|

| Step 1 | From the
                                       			 Server directory on the CD, run setup.exe . A warning message appears indicating that the Cisco Contact Center SNMP Management Service is stopped before the CTI OS Server
                                          begins to install. Note When you run programs from a Windows Server system with User Account Control enabled, Windows needs your permission to continue.
                                                      Click Yes in the User Account Control window to run the program. | Note | When you run programs from a Windows Server system with User Account Control enabled, Windows needs your permission to continue.
                                                      Click Yes in the User Account Control window to run the program. |
|---|---|---|---|
| Note | When you run programs from a Windows Server system with User Account Control enabled, Windows needs your permission to continue.
                                                      Click Yes in the User Account Control window to run the program. |
| Step 2 | Click Yes to continue. |
| Step 3 | In the Software License Agreement window, click Yes . |
| Step 4 | In the CTI OS Server Installer window, leave the Location field blank and click Next . The CTI OS Instances window appears. The CTI OS Instances window allows you to create CTI OS instances and add CTI OS Servers to a configured instance of CTI OS. Note The Add buttons are disabled if you cannot create another CTI OS instance. | Note | The Add buttons are disabled if you cannot create another CTI OS instance. |
| Note | The Add buttons are disabled if you cannot create another CTI OS instance. |
| Step 5 | Under the CTI OS Instance List, click Add . The Add CTIOS Server Instance window is displayed. |
| Step 6 | Enter an instance name and click OK . For example, if you enter an instance called cisco , the following window appears: |
| Step 7 | Click Add in the CTI OS Server List. The Add CTIOS Server window appears. The CTIOS Server Name field is populated with the instance name you provided, followed by the next available index for a CTI
                                          OS Server. If a CTI OS Server has been deleted, the CTIOS Server Name is populated with the index that was deleted. |
| Step 8 | If you are installing CTI OS Server for the first time, an Enter Desktop Drive window appears. Accept the default installation drive or choose another drive from the Drive drop-down list. |
| Step 9 | Click OK . The CTI Server Information window appears. The Instance Name and CTIOS Server Name is already populated. |
| Step 10 | For secured connection with the CTI server, check the Enable Secure Connection check box. Note For secured connection, you must provide the secure port number of the CTI Server. If the Enable Secure Connection check box is not checked, the connection established between the CTIOS Server and the CTI
                                                      Server is non-secured. In this case, you must provide the non-secure port number of the CTI Server. Before you enable secured connection between the components, ensure to complete the security certificate management process. For more information, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . | Note | For secured connection, you must provide the secure port number of the CTI Server. If the Enable Secure Connection check box is not checked, the connection established between the CTIOS Server and the CTI
                                                      Server is non-secured. In this case, you must provide the non-secure port number of the CTI Server. Before you enable secured connection between the components, ensure to complete the security certificate management process. For more information, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
| Note | For secured connection, you must provide the secure port number of the CTI Server. If the Enable Secure Connection check box is not checked, the connection established between the CTIOS Server and the CTI
                                                      Server is non-secured. In this case, you must provide the non-secure port number of the CTI Server. Before you enable secured connection between the components, ensure to complete the security certificate management process. For more information, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
| Step 11 | Enter the Name or IP Address and the Port Number for your CTI Server. If the peripheral is configured for a previous CTI OS Server, the Name or IP Address field pre-populates with the name of that CTI OS Server. |
| Step 12 | Click Next . The Peripheral Identifier window appears. The Peripheral Type field is pre-populated with the peripheral type if it is already configured for a previous CTI OS Server. Note When you
                                                      				  configure multiple CTI OS Servers to use a single CTI Server, every CTI OS
                                                      				  Server configured after the first CTI OS Server has the same configuration as
                                                      				  of the first CTI OS Server. | Note | When you
                                                      				  configure multiple CTI OS Servers to use a single CTI Server, every CTI OS
                                                      				  Server configured after the first CTI OS Server has the same configuration as
                                                      				  of the first CTI OS Server. |
| Note | When you
                                                      				  configure multiple CTI OS Servers to use a single CTI Server, every CTI OS
                                                      				  Server configured after the first CTI OS Server has the same configuration as
                                                      				  of the first CTI OS Server. |
| Step 13 | If the
                                       			 peripheral has not been configured for a previous CTI OS Server, specify the
                                       			 following information: A Logical Name for your peripheral. The name can be
                                                					 any valid logical name that uniquely identifies your peripheral. Note The
                                                            						Login By and Enable Mobile Agent group boxes are enabled only for UCCE
                                                            						peripheral types (UCCE System and UCCEHosted Edition). In the
                                                            						Login By box, you can choose between signing in by Agent ID or by Login Name.
                                                            						The Login By setting determines how the CTI Toolkit Agent and Supervisor
                                                            						Desktops allow Login and Chat request (either Agent ID or Login Name). This
                                                            						setting does not affect other CTI applications. CTI OS Server itself can
                                                            						service Login requests both ways (by Agent ID and Login Name) for UCCE. In the Peripheral ID field, enter the identifier of the
                                                					 switch that your phone is connected to. From the Peripheral Type drop-down list, choose the switch
                                                					 that your phone is connected to. Check
                                                					 the Enable Mobile Agent check box to activate this
                                                					 option. Select the Login By option. The Mobile agent mode drop-down lists the following options. Choose one: Agent chooses —Agent chooses the mode. Call by call —The agent's remote phone is dialed for
                                                      						  each individual call. Nailed connection —The agent is called once upon
                                                      						  signing in and remains connected. Note You can
                                                      				  specify information for only one peripheral during CTI OS Server setup. To
                                                      				  configure more peripherals, follow the procedure in the section Configure Additional Peripherals . | Note | The
                                                            						Login By and Enable Mobile Agent group boxes are enabled only for UCCE
                                                            						peripheral types (UCCE System and UCCEHosted Edition). In the
                                                            						Login By box, you can choose between signing in by Agent ID or by Login Name.
                                                            						The Login By setting determines how the CTI Toolkit Agent and Supervisor
                                                            						Desktops allow Login and Chat request (either Agent ID or Login Name). This
                                                            						setting does not affect other CTI applications. CTI OS Server itself can
                                                            						service Login requests both ways (by Agent ID and Login Name) for UCCE. | Note | You can
                                                      				  specify information for only one peripheral during CTI OS Server setup. To
                                                      				  configure more peripherals, follow the procedure in the section Configure Additional Peripherals . |
| Note | The
                                                            						Login By and Enable Mobile Agent group boxes are enabled only for UCCE
                                                            						peripheral types (UCCE System and UCCEHosted Edition). In the
                                                            						Login By box, you can choose between signing in by Agent ID or by Login Name.
                                                            						The Login By setting determines how the CTI Toolkit Agent and Supervisor
                                                            						Desktops allow Login and Chat request (either Agent ID or Login Name). This
                                                            						setting does not affect other CTI applications. CTI OS Server itself can
                                                            						service Login requests both ways (by Agent ID and Login Name) for UCCE. |
| Note | You can
                                                      				  specify information for only one peripheral during CTI OS Server setup. To
                                                      				  configure more peripherals, follow the procedure in the section Configure Additional Peripherals . |
| Step 14 | Click Next . The Connection Information window appears. Enter the port number and the heartbeat information for your CTI
                                          				OS Server instance. Note For all peripheral types, accept the default Listen Port value of 42028. For subsequent instances, use any available port. Important Ensure
                                                      				  that you configure the CTI OS client that connects to the CTI OS Server with
                                                      				  the same port that you selected while installing the CTI OS client. | Note | For all peripheral types, accept the default Listen Port value of 42028. For subsequent instances, use any available port. | Important | Ensure
                                                      				  that you configure the CTI OS client that connects to the CTI OS Server with
                                                      				  the same port that you selected while installing the CTI OS client. |
| Note | For all peripheral types, accept the default Listen Port value of 42028. For subsequent instances, use any available port. |
| Important | Ensure
                                                      				  that you configure the CTI OS client that connects to the CTI OS Server with
                                                      				  the same port that you selected while installing the CTI OS client. |
| Step 15 | Click Next . The Statistics Information window appears. Note Enabling CAD Agent
                                                         					 disables the agent statistics polling interval from the CTI OS Server. CAD
                                                         					 agents receive only Skillgroup statistics from CTI OS Server. After
                                                            						performing an Upgrade All , rerun setup to access this window and
                                                            						reconfigure the server for appropriate statistical information. | Note | Enabling CAD Agent
                                                         					 disables the agent statistics polling interval from the CTI OS Server. CAD
                                                         					 agents receive only Skillgroup statistics from CTI OS Server. After
                                                            						performing an Upgrade All , rerun setup to access this window and
                                                            						reconfigure the server for appropriate statistical information. |
| Note | Enabling CAD Agent
                                                         					 disables the agent statistics polling interval from the CTI OS Server. CAD
                                                         					 agents receive only Skillgroup statistics from CTI OS Server. After
                                                            						performing an Upgrade All , rerun setup to access this window and
                                                            						reconfigure the server for appropriate statistical information. |
| Step 16 | Enter the
                                       			 default polling interval for Skillgroup statistics (in seconds). Note Because Quality of Service (QoS) enablement and statistics enablement are mutually exclusive, enabling QoS zeros disables
                                                      all the information relating to statistics. | Note | Because Quality of Service (QoS) enablement and statistics enablement are mutually exclusive, enabling QoS zeros disables
                                                      all the information relating to statistics. |
| Note | Because Quality of Service (QoS) enablement and statistics enablement are mutually exclusive, enabling QoS zeros disables
                                                      all the information relating to statistics. |
| Step 17 | Click Next . The UCCE Silent Monitor Type window appears. |
| Step 18 | Choose the
                                       			 type of silent monitor. If you
                                             				  choose Unified CM Based or Disabled , clicking Next takes you to the Peer CTI OS Server window. Proceed to Step 17. Note If you
                                                         					 want to use Unified CM based type silent monitor, see Unified Communications Manager-Based Silent Monitor Configuration . If you
                                             				  choose Disabled , the CTI OS based silent monitor is
                                             				  configured, but disabled. This sets the registry settings to the following
                                             				  values: Key Setting HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\IPCCSilentMonitor\Name\Settings\CCMBasedSilentMonitor 0 HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\Login\ConnectionProfiles\Name\UCCE\
                                                         IPCCSilentMonitorEnabled 0 If you
                                             				  choose CTI OS Based silent monitor, clicking Next takes you to the Silent Monitor Information window. | Note | If you
                                                         					 want to use Unified CM based type silent monitor, see Unified Communications Manager-Based Silent Monitor Configuration . | Key | Setting | HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\IPCCSilentMonitor\Name\Settings\CCMBasedSilentMonitor | 0 | HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\Login\ConnectionProfiles\Name\UCCE\
                                                         IPCCSilentMonitorEnabled | 0 |
| Note | If you
                                                         					 want to use Unified CM based type silent monitor, see Unified Communications Manager-Based Silent Monitor Configuration . |
| Key | Setting |
| HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\IPCCSilentMonitor\Name\Settings\CCMBasedSilentMonitor | 0 |
| HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\Login\ConnectionProfiles\Name\UCCE\
                                                         IPCCSilentMonitorEnabled | 0 |
| Step 19 | On the Silent Monitor Information window, enter the following information: The port number used by the client to connect to the silent monitor service. The set of silent monitor servers that the desktop connects to. The desktop randomly connects to one of the silent monitor
                                                servers specified here. If the client is configured to use secure connections, the client attempts to connect to the silent
                                                monitor server using a secure connection. If the silent monitor server is configured to use secure connections, then a secure
                                                connection is established with the silent monitor server. Otherwise, an unsecured connection is used. A client uses the same certificates it uses to communicate with CTI OS Server to establish a secure connection to the silent
                                                monitor server. |
| Step 20 | Click Next . The Peer CTIOS Server window appears. |
| Step 21 | You can configure a CTI OS Peer Server using this window. You can also configure Chat and CTI OS silent monitoring. Enter
                                       the Peer CTI OS Server and Port details. After you click Finish and the files are created, the service is registered and entries to the registry are made. Note You can configure the chat window to beep every time a new message arrives. To do that, set the following registry key to
                                                      a nonzero value. HKEY_LOCAL_MACHINE\Cisco Systems, Inc.\CTI Desktop\CtiOs\BeepOnMsgReceived If the registry key does not exist or if its value is set to zero, the chat window does not beep. | Note | You can configure the chat window to beep every time a new message arrives. To do that, set the following registry key to
                                                      a nonzero value. |
| Note | You can configure the chat window to beep every time a new message arrives. To do that, set the following registry key to
                                                      a nonzero value. |
| Step 22 | The CTI OS Server Security window appears. If you wish to disable security, click OK ; otherwise, select the Enable Security check box, enter the appropriate information, and click OK . Note To simplify deployments, either enable or disable security for all CTI OS components (clients, CTI OS Server, and silent monitor
                                                      server). | Note | To simplify deployments, either enable or disable security for all CTI OS components (clients, CTI OS Server, and silent monitor
                                                      server). |
| Note | To simplify deployments, either enable or disable security for all CTI OS components (clients, CTI OS Server, and silent monitor
                                                      server). |
| Step 23 | The CTI OS Security InstallShield Wizard appears if you have enabled security: After the CTI OS Server security installation is complete, click Finish . |

| Note | When you run programs from a Windows Server system with User Account Control enabled, Windows needs your permission to continue.
                                                      Click Yes in the User Account Control window to run the program. |
|---|---|

| Note | The Add buttons are disabled if you cannot create another CTI OS instance. |
|---|---|

| Note | For secured connection, you must provide the secure port number of the CTI Server. If the Enable Secure Connection check box is not checked, the connection established between the CTIOS Server and the CTI
                                                      Server is non-secured. In this case, you must provide the non-secure port number of the CTI Server. Before you enable secured connection between the components, ensure to complete the security certificate management process. For more information, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Note | When you
                                                      				  configure multiple CTI OS Servers to use a single CTI Server, every CTI OS
                                                      				  Server configured after the first CTI OS Server has the same configuration as
                                                      				  of the first CTI OS Server. |
|---|---|

| Note | The
                                                            						Login By and Enable Mobile Agent group boxes are enabled only for UCCE
                                                            						peripheral types (UCCE System and UCCEHosted Edition). In the
                                                            						Login By box, you can choose between signing in by Agent ID or by Login Name.
                                                            						The Login By setting determines how the CTI Toolkit Agent and Supervisor
                                                            						Desktops allow Login and Chat request (either Agent ID or Login Name). This
                                                            						setting does not affect other CTI applications. CTI OS Server itself can
                                                            						service Login requests both ways (by Agent ID and Login Name) for UCCE. |
|---|---|

| Note | You can
                                                      				  specify information for only one peripheral during CTI OS Server setup. To
                                                      				  configure more peripherals, follow the procedure in the section Configure Additional Peripherals . |
|---|---|

| Note | For all peripheral types, accept the default Listen Port value of 42028. For subsequent instances, use any available port. |
|---|---|

| Important | Ensure
                                                      				  that you configure the CTI OS client that connects to the CTI OS Server with
                                                      				  the same port that you selected while installing the CTI OS client. |
|---|---|

| Note | Enabling CAD Agent
                                                         					 disables the agent statistics polling interval from the CTI OS Server. CAD
                                                         					 agents receive only Skillgroup statistics from CTI OS Server. After
                                                            						performing an Upgrade All , rerun setup to access this window and
                                                            						reconfigure the server for appropriate statistical information. |
|---|---|

| Note | Because Quality of Service (QoS) enablement and statistics enablement are mutually exclusive, enabling QoS zeros disables
                                                      all the information relating to statistics. |
|---|---|

| Note | If you
                                                         					 want to use Unified CM based type silent monitor, see Unified Communications Manager-Based Silent Monitor Configuration . |
|---|---|

| Key | Setting |
|---|---|
| HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\IPCCSilentMonitor\Name\Settings\CCMBasedSilentMonitor | 0 |
| HKLM\SOFTWARE\Cisco Systems, Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All Desktops\Login\ConnectionProfiles\Name\UCCE\
                                                         IPCCSilentMonitorEnabled | 0 |

| Note | You can configure the chat window to beep every time a new message arrives. To do that, set the following registry key to
                                                      a nonzero value. |
|---|---|

| Note | To simplify deployments, either enable or disable security for all CTI OS components (clients, CTI OS Server, and silent monitor
                                                      server). |
|---|---|

| Note | CTI OS
                                                				  Multi-Instance setup does not allow two or more CTI OS Servers to connect to
                                                				  the same CTI Server. The setup
                                                				  does not allow two or more CTI OS Servers to use the same listen port. Rerun the
                                                				  CTI OS Server setup after you complete the installation. |
|---|---|

| Step 1 | Open a window
                                       			 for the ICM\CTIOS_bin subdirectory. |
|---|---|
| Step 2 | Highlight the
                                       			 file ctiosservernode.exe . |
| Step 3 | Right-click the
                                       			 highlighted file. |
| Step 4 | Select Properties from the drop-down menu. The
                                       			 Properties dialog box appears. |
| Step 5 | Select the Details tab. This tab contains version information (release number and build number) for the file. |