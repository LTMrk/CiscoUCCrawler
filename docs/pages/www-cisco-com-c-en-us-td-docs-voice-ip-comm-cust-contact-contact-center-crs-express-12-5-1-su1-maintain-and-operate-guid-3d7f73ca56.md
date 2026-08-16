---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-maintain-and-operate-guid-3d7f73ca56
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/maintain_and_operate/guide/uccx_b_1251su1admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_010.html
retrieved_at: 2026-08-16T21:38:12.551799+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

Updated: January 31, 2021

Chapter: Unified CCX AdministrationWeb Interface

## Chapter: Unified CCX AdministrationWeb Interface

# Unified CCX AdministrationWeb Interface

## Access Unified CCX
                        	 Administration Web Interface

The web
                              		  pages of the Unified CCX Administration web interface allow you to configure
                              		  and manage the Unified CCX system and its subsystems.

Use the
                              		  following procedure to browse into the server and log in to Unified CCX
                              		  Administration web interface.

Step 1

Open the
                                       			 Unified CCX Administration Authentication page from a web browser on any
                                       			 computer on your network and enter the following case-sensitive URL:

```
https:// <servername> /appadmin
```

In this
                                          				example, replace < servername > with the hostname or IP address of the
                                          				required Unified CCX server.

A Security
                                          				Alert dialog box is displayed.

Step 2

Click the
                                       			 appropriate button.

The
                                          				Authentication page appears.

Ensure
                                                            						that Cisco Tomcat and Cisco Unified Cluster View Daemon services are running
                                                            						before you log in to the Unified CCX Administration using the URL in Step 1.

Ensure that the popup blocker is disabled on your browser.

If a custom logon message is set up in Cisco Unified OS
                                                            									Administration, the message appears in a pop-up window. You must
                                                            									acknowledge the message to log in. For more information about
                                                            									setting up custom logon message, see the Set Up Customized
                                                               										Logon Message section in Cisco Unified
                                                               										Operating System Administration Guide for Cisco Unified CCX
                                                               										and Cisco Unified IP IVR .

Step 3

On the main
                                       			 Cisco Unified CCX Administration web page, enter your Unified CCX username and
                                       			 password.

If you are accessing Unified CCX for the first time, enter the Application User credentials that are specified during installation
                                                      of the Unified CCX. See the Cisco Unified Contact
                                                               				  Center Express Install and Upgrade Guide for further instructions.

User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02.

Step 4

Click Login .

A web page
                                          				opens listing information about Cisco Unified CCX Administration and the Cisco
                                          				Unified CCX Administration menu bar appears at the top of the page.

Unified CCX Administration detects web-based cross-site request forgery attacks and rejects
                                                            									malicious client requests. It displays the error message, "The
                                                            									attempted action is not allowed because it violates security
                                                            									policies."

Avoid
                                                            						using multiple sessions of the Unified CCX Administration at the same time.

To log
                                                            						in again to the Cisco Unified CCX Administration after you clicked Logout click the link, Click here to log in again .

For a
                                                            						complete logout from all applications, sign out of the respective applications
                                                            						and close the browser window. In a Windows desktop, you may achieve this by
                                                            						logging out of the Windows account. In a Mac desktop, you may quit the browser
                                                            						application.

Single
                                                            						Sign-On enabled agents have the risk of others misusing their account. If the
                                                            						browser is not closed completely the Click here to log in again link does not require the
                                                            						agent to enter credentials to log in to the application.

The Unified CCX Administration interface and the Unified CCX User Options (appuser) web
                                                            									interface should not be logged in to the same window on
                                                            									different tabs.

To configure session-timeout, use the set webapp session timeout command. You can
                                                            									specify the session-timeout between 5 and 35000 minutes. For
                                                            									example, if you have configured session-timeout for 5 minutes,
                                                            									the user is logged out after a session is inactive for 5
                                                            									minutes. The configuration is updated only on the node where the
                                                            									command is run. Ensure to run this command on both the nodes.
                                                            									You must reboot the node for the configuration to take
                                                            									effect.

### Supported Languages

Unified CCX Administration supports only English.

## Cisco Unified CCX
                        	 Administration Menu Bar and Menus

The Cisco
                              		  Unified CCX Administration menu bar appears at the top of every web page of the
                              		  Unified CCX Administration web interface. You begin every Unified CCX
                              		  configuration and administration task by choosing a menu and submenu option
                              		  from the menu bar.

The Cisco
                              		  Unified CCX Administration menu bar contains the following menu options:

System —Contains options
                                    				for configuring new servers in the cluster, Unified CM information, language information, changing system parameters, custom file
                                    				configuration, standalone CUIC configuration, adding or displaying licenses,
                                    				and single sign-on.

Applications —Contains
                                    				options for managing applications, scripts, prompts, grammars, documents, and
                                    				AAR files.

Subsystems —Contains
                                    				options for configuring parameters for the subsystems that are licensed for
                                    				your Unified CCX server. Your Subsystems menu may include submenu options for
                                    				one or more of the following subsystems: Unified CM Telephony, Unified CCX , 
                                    				 Database, HTTP, Chat and Email, CiscoMedia, MRCP Automatic
                                    				Speech Recognition (ASR), and MRCP Text-To-Speech (TTS).

Wizards —Contains
                                    				options that provide access to the following wizards of your Unified CCX
                                    				server: Application and RmCm.

Tools —Contains options
                                    				that allow you to access system tools such as Plug-ins, Real-Time Reporting,
                                    				Real-Time Snapshot Config. You can also assign access levels to administrators and
                                    				supervisors and reset passwords.

Help —Provides access to
                                    				online help for Unified CCX.

## Cisco Unified CCX
                        	 Administration Navigation

After you
                              		  log in, the main Cisco Unified CCX
                                 			 Administration web page appears.

The
                              		  choices in the drop-down list include the following Cisco Unified CCX
                                 			 Administration applications:

Cisco Unified
                                          					 CCX Administration — Uses Cisco Unified CCX
                                       				  Administration to configure system parameters, subsystems, wizards,
                                    				and much more.

Cisco Unified
                                          					 CCX Serviceability — Takes you to the main Cisco Unified CCX
                                       				  Serviceability web page that is used to configure trace files,
                                    				alarms, and to activate and deactivate services.

Cisco Finesse
                                       				  Administration — Uses Cisco Finesse Administration to configure system
                                    				settings in Cisco Finesse.

Cisco Unified
                                          					 Serviceability — Takes you to the main Cisco Unified
                                       				  Serviceability web page that is used to save alarms and traces for
                                    				troubleshooting, provide alarm message definitions, activate and deactivate
                                    				services and so on.

Cisco Unified OS
                                       				  Administration — Takes you to the main Cisco Unified OS Administration web
                                    				page, so that you can configure and administer the Cisco Unified Communications
                                    				platform.

Disaster Recovery System — Takes you to the Cisco Disaster Recovery
                                       				  System , a program that provides data backup and restore capabilities
                                    				for all servers in a Cisco Unified CCX
                                       				  Administration cluster.

Cisco Identity Service
                                          					 Management - Takes you to the Identity Service Management page
                                    				where the Identity Service configurations can be done.

You can log in to
                              		  Cisco Unified CCX Administration either as an administration user or an
                              		  application user.

An
                                          			 administration user is an end user that is configured on the Unified CM with
                                          			 Administrator capability in Unified CCX.

An application
                                          			 user is an user that is configured during the installation of Unified CCX
                                          			 having administrator capability by default.

If you log in as
                              		  an Administrator, you can access the following applications that display in the
                              		  navigation drop-down list in the top right corner of the Administration menu
                              		  bar:

Cisco Unified CCX Administration

Cisco Unified CCX Serviceability

Cisco Finesse
                                       				  Administrator

Cisco Identity
                                    				Service Management

If you log in as
                              		  an application user, you can seamlessly traverse between the Unified CCX web
                              		  applications as well as the Cisco Identity Service Management and Cisco Unified
                              		  Serviceability without logging in again.

To access
                              		  these applications from Cisco Unified CCX
                                 			 Administration , you must first choose the desired application from
                              		  the navigation drop-down list in the upper right corner and click Go .

Cisco Finesse
                                          			 Administration Console opens in a new tab or in a new window based on the
                                          			 browser settings.

To log in to
                                          			 Cisco Finesse Administration, you must be a user with administrator privileges.

When the Cisco
                                          			 Tomcat service is down on any of the Unified CCX nodes, you will not be able to
                                          			 launch Cisco Unified CCX Administration from any of the Unified CCX nodes;
                                          			 therefore, you will not be able to launch the Cisco Finesse Administration from
                                          			 within it.

In that case,
                                          			 you can launch the Cisco Finesse Administration directly from the browser.

To
                                          			 launch the Finesse Administration Console, direct your browser to https://hostname or IP address:8445/cfadmin , where hostname or IP address is the hostname or IP address of the server.

You can access the
                              		  following platform-based web applications using the platform user credentials
                              		  as configured during installation of Unified CCX:

Cisco Unified
                                    				Operating System Administration

Disaster
                                    				Recovery System

## Unified CCX
                        	 Configuration Web Pages

When you
                              		  choose any menu and submenu option from the Unified CCXAdministration menu
                              		  bar, a configuration or administration web page opens. Use this web page to
                              		  continue your configuration or administration task.

In some
                              		  cases, you will perform your configuration or administration task on this one
                              		  web page.

In other
                              		  cases, the web page that first opens when you choose a submenu item leads to a
                              		  series of web pages. For example, the Unified CM Telephony Call Control Group
                              		  Configuration web page contains both a tool bar in the top with a few icons
                              		  that link to other web pages and a configuration area.

The
                              		  following table describes the Refresh
                                 			 All button and the Copy , Delete , and Refresh icons that are found on several Unified CCX
                              		  web pages.

Icon/Button

Description

Copy

Click this
                                          						icon to copy the information in that specific row.

When you
                                                      						  click Copy , the web page displays the copied configuration
                                                      						  so you can make changes, if desired.

Delete

Click this
                                          						icon to delete the information in that specific row.

Refresh

Click this
                                          						icon to refresh the information in that specific row.

Refresh
                                          						All

Click this
                                          						button to refresh the information listed on this page.

### Details for Advanced Configuration

In Unified CCX Administration web interface, advanced configuration with Show More and Show Less options exists. On the applicable
                                 		  pages, all configuration details can be displayed or minimised based on user
                                 		  preferences and requirements.

A page by default displays fewer parameters. Parameters
                                 		  configured with default values and not requiring modification or user input are
                                 		  now available in the advanced configuration section. You can access this
                                 		  advanced configuration section by clicking the Show More button at the bottom of the page. When
                                 		  you click this button, the extra parameters become visible and the button
                                 		  changes to Show Less . When you click Show Less , the page reverts to its
                                 		  original list of parameters.

### Toolbar and Buttons

On the top left toolbar of many web pages, you will find an Add New icon and the same Add New will also be displayed as a button at
                                 		  the bottom of the web page.

For example, the Unified CM Telephony Call Control Group
                                 		  Configuration web page contains Add New and Refresh All icons on the top left toolbar and
                                 		  the same are displayed as buttons at the bottom of the web page. When you click
                                 		  the Add New icon or button, another Unified CM
                                 		  Telephony Call Control Group Configuration web page opens. Use this area to add
                                 		  a new Unified CM Telephony Call Control Group.

Many web pages contain icons or buttons that perform a
                                 		  variety of functions. For example, the Refresh All button on the Unified CM Telephony Call Control
                                 		  Group Configuration web page refreshes all the Unified CM Telephony call control
                                 		  group configurations in the Unified CCX server.

A few web pages (for example, Subsystems > Database > Parameters page) also contain a Reset to Default icon and button. This allows
                                 		  you to revert to the software set defaults for each parameter on this page.

### Application and RmCm Wizards

In Unified CCX, two wizards are available in the main menu:
                                 		  the Application Wizard and the RmCm Wizard.

To improve the usability and configuration process, these
                                 		  wizards take you through the configuration pages in the required order and help
                                 		  ease the configuration process for these two features. You can access these
                                 		  wizards from a new main menu option called Wizards .

| Step 1 | Open the
                                       			 Unified CCX Administration Authentication page from a web browser on any
                                       			 computer on your network and enter the following case-sensitive URL: https:// <servername> /appadmin In this
                                          				example, replace < servername > with the hostname or IP address of the
                                          				required Unified CCX server. A Security
                                          				Alert dialog box is displayed. |
|---|---|
| Step 2 | Click the
                                       			 appropriate button. The
                                          				Authentication page appears. Note Ensure
                                                            						that Cisco Tomcat and Cisco Unified Cluster View Daemon services are running
                                                            						before you log in to the Unified CCX Administration using the URL in Step 1. Ensure that the popup blocker is disabled on your browser. If a custom logon message is set up in Cisco Unified OS
                                                            									Administration, the message appears in a pop-up window. You must
                                                            									acknowledge the message to log in. For more information about
                                                            									setting up custom logon message, see the Set Up Customized
                                                               										Logon Message section in Cisco Unified
                                                               										Operating System Administration Guide for Cisco Unified CCX
                                                               										and Cisco Unified IP IVR . | Note | Ensure
                                                            						that Cisco Tomcat and Cisco Unified Cluster View Daemon services are running
                                                            						before you log in to the Unified CCX Administration using the URL in Step 1. Ensure that the popup blocker is disabled on your browser. If a custom logon message is set up in Cisco Unified OS
                                                            									Administration, the message appears in a pop-up window. You must
                                                            									acknowledge the message to log in. For more information about
                                                            									setting up custom logon message, see the Set Up Customized
                                                               										Logon Message section in Cisco Unified
                                                               										Operating System Administration Guide for Cisco Unified CCX
                                                               										and Cisco Unified IP IVR . |
| Note | Ensure
                                                            						that Cisco Tomcat and Cisco Unified Cluster View Daemon services are running
                                                            						before you log in to the Unified CCX Administration using the URL in Step 1. Ensure that the popup blocker is disabled on your browser. If a custom logon message is set up in Cisco Unified OS
                                                            									Administration, the message appears in a pop-up window. You must
                                                            									acknowledge the message to log in. For more information about
                                                            									setting up custom logon message, see the Set Up Customized
                                                               										Logon Message section in Cisco Unified
                                                               										Operating System Administration Guide for Cisco Unified CCX
                                                               										and Cisco Unified IP IVR . |
| Step 3 | On the main
                                       			 Cisco Unified CCX Administration web page, enter your Unified CCX username and
                                       			 password. Note If you are accessing Unified CCX for the first time, enter the Application User credentials that are specified during installation
                                                      of the Unified CCX. See the Cisco Unified Contact
                                                               				  Center Express Install and Upgrade Guide for further instructions. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. | Note | If you are accessing Unified CCX for the first time, enter the Application User credentials that are specified during installation
                                                      of the Unified CCX. See the Cisco Unified Contact
                                                               				  Center Express Install and Upgrade Guide for further instructions. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
| Note | If you are accessing Unified CCX for the first time, enter the Application User credentials that are specified during installation
                                                      of the Unified CCX. See the Cisco Unified Contact
                                                               				  Center Express Install and Upgrade Guide for further instructions. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
| Step 4 | Click Login . A web page
                                          				opens listing information about Cisco Unified CCX Administration and the Cisco
                                          				Unified CCX Administration menu bar appears at the top of the page. Note Unified CCX Administration detects web-based cross-site request forgery attacks and rejects
                                                            									malicious client requests. It displays the error message, "The
                                                            									attempted action is not allowed because it violates security
                                                            									policies." Avoid
                                                            						using multiple sessions of the Unified CCX Administration at the same time. To log
                                                            						in again to the Cisco Unified CCX Administration after you clicked Logout click the link, Click here to log in again . For a
                                                            						complete logout from all applications, sign out of the respective applications
                                                            						and close the browser window. In a Windows desktop, you may achieve this by
                                                            						logging out of the Windows account. In a Mac desktop, you may quit the browser
                                                            						application. Single
                                                            						Sign-On enabled agents have the risk of others misusing their account. If the
                                                            						browser is not closed completely the Click here to log in again link does not require the
                                                            						agent to enter credentials to log in to the application. The Unified CCX Administration interface and the Unified CCX User Options (appuser) web
                                                            									interface should not be logged in to the same window on
                                                            									different tabs. To configure session-timeout, use the set webapp session timeout command. You can
                                                            									specify the session-timeout between 5 and 35000 minutes. For
                                                            									example, if you have configured session-timeout for 5 minutes,
                                                            									the user is logged out after a session is inactive for 5
                                                            									minutes. The configuration is updated only on the node where the
                                                            									command is run. Ensure to run this command on both the nodes.
                                                            									You must reboot the node for the configuration to take
                                                            									effect. | Note | Unified CCX Administration detects web-based cross-site request forgery attacks and rejects
                                                            									malicious client requests. It displays the error message, "The
                                                            									attempted action is not allowed because it violates security
                                                            									policies." Avoid
                                                            						using multiple sessions of the Unified CCX Administration at the same time. To log
                                                            						in again to the Cisco Unified CCX Administration after you clicked Logout click the link, Click here to log in again . For a
                                                            						complete logout from all applications, sign out of the respective applications
                                                            						and close the browser window. In a Windows desktop, you may achieve this by
                                                            						logging out of the Windows account. In a Mac desktop, you may quit the browser
                                                            						application. Single
                                                            						Sign-On enabled agents have the risk of others misusing their account. If the
                                                            						browser is not closed completely the Click here to log in again link does not require the
                                                            						agent to enter credentials to log in to the application. The Unified CCX Administration interface and the Unified CCX User Options (appuser) web
                                                            									interface should not be logged in to the same window on
                                                            									different tabs. To configure session-timeout, use the set webapp session timeout command. You can
                                                            									specify the session-timeout between 5 and 35000 minutes. For
                                                            									example, if you have configured session-timeout for 5 minutes,
                                                            									the user is logged out after a session is inactive for 5
                                                            									minutes. The configuration is updated only on the node where the
                                                            									command is run. Ensure to run this command on both the nodes.
                                                            									You must reboot the node for the configuration to take
                                                            									effect. |
| Note | Unified CCX Administration detects web-based cross-site request forgery attacks and rejects
                                                            									malicious client requests. It displays the error message, "The
                                                            									attempted action is not allowed because it violates security
                                                            									policies." Avoid
                                                            						using multiple sessions of the Unified CCX Administration at the same time. To log
                                                            						in again to the Cisco Unified CCX Administration after you clicked Logout click the link, Click here to log in again . For a
                                                            						complete logout from all applications, sign out of the respective applications
                                                            						and close the browser window. In a Windows desktop, you may achieve this by
                                                            						logging out of the Windows account. In a Mac desktop, you may quit the browser
                                                            						application. Single
                                                            						Sign-On enabled agents have the risk of others misusing their account. If the
                                                            						browser is not closed completely the Click here to log in again link does not require the
                                                            						agent to enter credentials to log in to the application. The Unified CCX Administration interface and the Unified CCX User Options (appuser) web
                                                            									interface should not be logged in to the same window on
                                                            									different tabs. To configure session-timeout, use the set webapp session timeout command. You can
                                                            									specify the session-timeout between 5 and 35000 minutes. For
                                                            									example, if you have configured session-timeout for 5 minutes,
                                                            									the user is logged out after a session is inactive for 5
                                                            									minutes. The configuration is updated only on the node where the
                                                            									command is run. Ensure to run this command on both the nodes.
                                                            									You must reboot the node for the configuration to take
                                                            									effect. |

| Note | Ensure
                                                            						that Cisco Tomcat and Cisco Unified Cluster View Daemon services are running
                                                            						before you log in to the Unified CCX Administration using the URL in Step 1. Ensure that the popup blocker is disabled on your browser. If a custom logon message is set up in Cisco Unified OS
                                                            									Administration, the message appears in a pop-up window. You must
                                                            									acknowledge the message to log in. For more information about
                                                            									setting up custom logon message, see the Set Up Customized
                                                               										Logon Message section in Cisco Unified
                                                               										Operating System Administration Guide for Cisco Unified CCX
                                                               										and Cisco Unified IP IVR . |
|---|---|

| Note | If you are accessing Unified CCX for the first time, enter the Application User credentials that are specified during installation
                                                      of the Unified CCX. See the Cisco Unified Contact
                                                               				  Center Express Install and Upgrade Guide for further instructions. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
|---|---|

| Note | Unified CCX Administration detects web-based cross-site request forgery attacks and rejects
                                                            									malicious client requests. It displays the error message, "The
                                                            									attempted action is not allowed because it violates security
                                                            									policies." Avoid
                                                            						using multiple sessions of the Unified CCX Administration at the same time. To log
                                                            						in again to the Cisco Unified CCX Administration after you clicked Logout click the link, Click here to log in again . For a
                                                            						complete logout from all applications, sign out of the respective applications
                                                            						and close the browser window. In a Windows desktop, you may achieve this by
                                                            						logging out of the Windows account. In a Mac desktop, you may quit the browser
                                                            						application. Single
                                                            						Sign-On enabled agents have the risk of others misusing their account. If the
                                                            						browser is not closed completely the Click here to log in again link does not require the
                                                            						agent to enter credentials to log in to the application. The Unified CCX Administration interface and the Unified CCX User Options (appuser) web
                                                            									interface should not be logged in to the same window on
                                                            									different tabs. To configure session-timeout, use the set webapp session timeout command. You can
                                                            									specify the session-timeout between 5 and 35000 minutes. For
                                                            									example, if you have configured session-timeout for 5 minutes,
                                                            									the user is logged out after a session is inactive for 5
                                                            									minutes. The configuration is updated only on the node where the
                                                            									command is run. Ensure to run this command on both the nodes.
                                                            									You must reboot the node for the configuration to take
                                                            									effect. |
|---|---|

| Note | The minimum supported screen resolution specifies 1024 x 768. Devices with lower screen resolutions may not display the applications
                                       correctly. |
|---|---|

| Note | An
                                          			 administration user is an end user that is configured on the Unified CM with
                                          			 Administrator capability in Unified CCX. An application
                                          			 user is an user that is configured during the installation of Unified CCX
                                          			 having administrator capability by default. |
|---|---|

| Note | For security purposes, Cisco Unified CCX Administration and Cisco Unified CCX Serviceability logs you out after a configured
                                       session timeout for an inactive session and you must log back in. This session timeout can be configured using the platform
                                       based command line interface command set webapp session timeout . For more information on this command, see Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Note | An application user can log in to these four Unified CCX web applications even when Unified CM is down. |
|---|---|

| Note | Cisco Finesse
                                          			 Administration Console opens in a new tab or in a new window based on the
                                          			 browser settings. To log in to
                                          			 Cisco Finesse Administration, you must be a user with administrator privileges. When the Cisco
                                          			 Tomcat service is down on any of the Unified CCX nodes, you will not be able to
                                          			 launch Cisco Unified CCX Administration from any of the Unified CCX nodes;
                                          			 therefore, you will not be able to launch the Cisco Finesse Administration from
                                          			 within it. In that case,
                                          			 you can launch the Cisco Finesse Administration directly from the browser. To
                                          			 launch the Finesse Administration Console, direct your browser to https://hostname or IP address:8445/cfadmin , where hostname or IP address is the hostname or IP address of the server. |
|---|---|

| Icon/Button | Description |
|---|---|
| Copy | Click this
                                          						icon to copy the information in that specific row. Note When you
                                                      						  click Copy , the web page displays the copied configuration
                                                      						  so you can make changes, if desired. | Note | When you
                                                      						  click Copy , the web page displays the copied configuration
                                                      						  so you can make changes, if desired. |
| Note | When you
                                                      						  click Copy , the web page displays the copied configuration
                                                      						  so you can make changes, if desired. |
| Delete | Click this
                                          						icon to delete the information in that specific row. |
| Refresh | Click this
                                          						icon to refresh the information in that specific row. |
| Refresh
                                          						All | Click this
                                          						button to refresh the information listed on this page. |

| Note | When you
                                                      						  click Copy , the web page displays the copied configuration
                                                      						  so you can make changes, if desired. |
|---|---|

| Note | If you are using Unified CCX with Cisco Contact Center Gateway solution, see the Cisco IPCC Gateway Deployment Guide for Cisco Unified ICME/CCE/CCX . The instructions for configuring Unified CCX with that solution differs from what is described in this guide. The Unified
                                          Gateway provides for the integration of the Unified ICME system with Unified CCX by way of Unified Gateway. For more information,
                                          see the Cisco Unified Contact Center Enterprise Install and Upgrade guides available at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/prod_installation_guides_list.html . The Unified Gateway is a Peripheral Gateway (PG), which you configure on the Unified ICME software. |
|---|---|