---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1262-insta-39ba58dcc4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1262/install/guide/cuic_b_install-and-upgrade-guide-1262/cuic_m_installation-1261.html
retrieved_at: 2026-08-21T16:14:29.137760+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(2)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(2)

Updated: April 28, 2023

Chapter: Installation

## Chapter: Installation

# Installation

## Installation Duration

The installation can take
                              from 60 to 75 minutes to complete and can run unattended for most of that time.

## Installation
                        	 Processes

During the
                              		  installation, the monitor shows a series of processes, as follows:

Formatting
                                    				Progress Bars

Copying File
                                    				Progress Bar

Platform
                                    				Installation Progress Bars (as multiple packages are installed)

Post Install
                                    				Progress Bar

Application
                                    				Installation Progress Bars (multiple packages are backed up to the archive
                                    				directory)

An
                                    				informational screen saying that the system reboots.

A System
                                    				Reboot, which includes a second hardware check.

Messages
                                    				appear during the reboot, some of which prompt you to press a key. Do not
                                    				respond to these prompts to press a key.

Application
                                    				Pre Install Progress Bars

Configure and
                                    				Setup Network Progress Bars

Member Nodes
                                    				only - Connection Validation message.

Security
                                    				Configuration

Member Nodes
                                    				only - A screen stating that there is a successful connection to the first node
                                    				(select Continue ).

The SMTP Host
                                    				Configuration screen(s). Select Yes or No , according to your preference.

Platform Configuration Complete screen. Select OK .

Display of Cryptographic Information screen.

Application
                                    				Post-Install Progress Bars

The installation
                              		  ends at a login prompt, at which you can enter CLI commands.

To access the web interface, you need to open a browser and enter the URL https://Controller hostname or IP/oamp and User ID/Password of the System Application user.

## Installation
                        	 Failure

Mount ISO to the virtual DVD drive and perform all steps in Chapter 2, and proceed to Configure Basic Install .

If a critical error
                              		  occurs during installation, you are prompted to collect log files. To do this,
                              		  insert a USB memory key in any available USB port and follow the instructions
                              		  on the screen.

If the installation fails over a Virtual Machine. For more information, see Frequently asked Questions .

## Post Installation

The action to take
                              		  after the installation, depends on the type of node you installed.

After installing the Unified Intelligence Center, you can download the Unified CCE templates from the Download Software page
                                          at https://software.cisco.com/download/home/282163829/type . You can then import these templates to Unified Intelligence Center.

After installing Cisco Unified Intelligence Center release 11.6, ensure to perform the following actions:

Disable the Unified CCE User Integration. (Uncheck the Enable UCCE User Integration check box in OAMP > Cluster Configuration > UCCE User Integration

Install the latest Cisco Options Package (COP) file for Unified Intelligence Center 11.6 release.

Enable the Unified CCE User Integration.

If

Then

If you
                                          						have installed a Controller, and your cluster consists of a Controller node
                                          						only

The
                                          						installation is complete.

Open a browser and enter the URL for your Controller ( https://Controller hostname or IP/oamp ). This opens the Administration Console.

Sign
                                                							 in using the System Application credentials.

This is not applicable for Live Data and Ids installation.

If you
                                          						have installed a Controller, and you intend to install a Member

Open a browser and enter the URL for your Controller ( https://Controller hostname or IP/oamp ). This opens the Administration Console.

Sign
                                                							 in using the System Application credentials.

Define the Member node in the Administration console.

This is not applicable for Live Data and Ids installation.

If you
                                          						have installed a Member node

Open a browser and enter the URL for your Member https://IP/cuicui/Main.jsp . This opens the Unified Intelligence Center Reporting web page.

Sign in
                                          						using the System Application credentials.

Until
                                          						other users are added or integrated, the System Application user has full
                                          						access to the Unified Intelligence Center Member nodes.

This is not applicable for Live Data and Ids installation.

If you are using self-signed certificates

Prerequisite—Download the Unified Intelligence Center tomcat certificate from Cisco Unified OS Administration page of Unified
                                          Intelligence Center.

Perform the following tasks to upload the Unified Intelligence Center server certificate to Cisco Finesse.

Sign in to Cisco Unified OS Administration on Cisco Finesse using the following URL: https://FQDN of Finesse server:8443/cmplatform .

Select Security > Certificate Management > Upload Certificate/Certificate chain .

From the Certificate Purpose drop-down list, select tomcat-trust .

In the Upload File field, click Choose File and browse to the tomcat.pem file that you saved on your system.

Click Upload .

Restart the Cisco Finesse Tomcat on the Cisco Finesse server.

Follow the same steps for both the Cisco Finesse publisher and subscriber nodes.

If there is a standalone Live Data system in this deployment, then upload Live Data tomcat certificate in addition to Cisco
                                                                  Finesse, using the above-stated procedure.

For more information, see the Certificates for Live Data chapter in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

If your network does not support multicasting, and when the Unified Intelligence Center administrator sign-in page displays
                                          a banner message about the application cluster issues.

Perform the following tasks change the discovery mechanism to tcp-ip mode.

Log in to the Cisco Unified Intelligence Center CLI. Specify the System Administrator username and password.

Run the following CLIs on all nodes in the given sequence, starting from the publisher node.

Enter the command utils service stop Intelligence Center Reporting Service .

Enter the command utils cuic cluster mode .

Select cluster mode 2) Enable tcp-ip .

Enter the command utils cuic cluster show .

Ensure that all nodes have an identical configuration.

Enter the command utils service start Intelligence Center Reporting Service.

If there happens to be a disconnect and reconnect, check that the database replication is successfully set up across all nodes
                                                            in the cluster. Perform "Synchronize Cluster" from Cisco Unified Intelligence Center to ensure that cache is in sync across
                                                            the cluster.

For more information, see the Cluster Configuration for JVM Using Hazelcast section in Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

| Note | At the start of the reboot, the CD tray holding the DVD ejects. This is usual behavior. You can remove the DVD. |
|---|---|

| Note | If a
                                             				Network Connectivity Failure screen opens during the Configure and Setup
                                             				Network process, click Review . Then click OK at the Errors screen. Follow the prompts to
                                             				reenter your hostname, IP Address, and so forth. The installation continues
                                             				when the connection information is complete. |
|---|---|

| Note | After installing the Unified Intelligence Center, you can download the Unified CCE templates from the Download Software page
                                          at https://software.cisco.com/download/home/282163829/type . You can then import these templates to Unified Intelligence Center. |
|---|---|

| Note | After installing Cisco Unified Intelligence Center release 11.6, ensure to perform the following actions: Disable the Unified CCE User Integration. (Uncheck the Enable UCCE User Integration check box in OAMP > Cluster Configuration > UCCE User Integration Install the latest Cisco Options Package (COP) file for Unified Intelligence Center 11.6 release. Enable the Unified CCE User Integration. |
|---|---|

| If | Then |
|---|---|
| If you
                                          						have installed a Controller, and your cluster consists of a Controller node
                                          						only | The
                                          						installation is complete. Open a browser and enter the URL for your Controller ( https://Controller hostname or IP/oamp ). This opens the Administration Console. Sign
                                                							 in using the System Application credentials. Note This is not applicable for Live Data and Ids installation. | Note | This is not applicable for Live Data and Ids installation. |
| Note | This is not applicable for Live Data and Ids installation. |
| If you
                                          						have installed a Controller, and you intend to install a Member | Open a browser and enter the URL for your Controller ( https://Controller hostname or IP/oamp ). This opens the Administration Console. Sign
                                                							 in using the System Application credentials. Define the Member node in the Administration console. Note This is not applicable for Live Data and Ids installation. | Note | This is not applicable for Live Data and Ids installation. |
| Note | This is not applicable for Live Data and Ids installation. |
| If you
                                          						have installed a Member node | Open a browser and enter the URL for your Member https://IP/cuicui/Main.jsp . This opens the Unified Intelligence Center Reporting web page. Sign in
                                          						using the System Application credentials. Until
                                          						other users are added or integrated, the System Application user has full
                                          						access to the Unified Intelligence Center Member nodes. Note This is not applicable for Live Data and Ids installation. | Note | This is not applicable for Live Data and Ids installation. |
| Note | This is not applicable for Live Data and Ids installation. |
| If you are using self-signed certificates | Prerequisite—Download the Unified Intelligence Center tomcat certificate from Cisco Unified OS Administration page of Unified
                                          Intelligence Center. Perform the following tasks to upload the Unified Intelligence Center server certificate to Cisco Finesse. Sign in to Cisco Unified OS Administration on Cisco Finesse using the following URL: https://FQDN of Finesse server:8443/cmplatform . Select Security > Certificate Management > Upload Certificate/Certificate chain . From the Certificate Purpose drop-down list, select tomcat-trust . In the Upload File field, click Choose File and browse to the tomcat.pem file that you saved on your system. Click Upload . Restart the Cisco Finesse Tomcat on the Cisco Finesse server. Note Follow the same steps for both the Cisco Finesse publisher and subscriber nodes. If there is a standalone Live Data system in this deployment, then upload Live Data tomcat certificate in addition to Cisco
                                                                  Finesse, using the above-stated procedure. For more information, see the Certificates for Live Data chapter in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . | Note | Follow the same steps for both the Cisco Finesse publisher and subscriber nodes. If there is a standalone Live Data system in this deployment, then upload Live Data tomcat certificate in addition to Cisco
                                                                  Finesse, using the above-stated procedure. |
| Note | Follow the same steps for both the Cisco Finesse publisher and subscriber nodes. If there is a standalone Live Data system in this deployment, then upload Live Data tomcat certificate in addition to Cisco
                                                                  Finesse, using the above-stated procedure. |
| If your network does not support multicasting, and when the Unified Intelligence Center administrator sign-in page displays
                                          a banner message about the application cluster issues. | Perform the following tasks change the discovery mechanism to tcp-ip mode. Log in to the Cisco Unified Intelligence Center CLI. Specify the System Administrator username and password. Note Run the following CLIs on all nodes in the given sequence, starting from the publisher node. Enter the command utils service stop Intelligence Center Reporting Service . Enter the command utils cuic cluster mode . Select cluster mode 2) Enable tcp-ip . Enter the command utils cuic cluster show . Note Ensure that all nodes have an identical configuration. Enter the command utils service start Intelligence Center Reporting Service. Note If there happens to be a disconnect and reconnect, check that the database replication is successfully set up across all nodes
                                                            in the cluster. Perform "Synchronize Cluster" from Cisco Unified Intelligence Center to ensure that cache is in sync across
                                                            the cluster. For more information, see the Cluster Configuration for JVM Using Hazelcast section in Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html . | Note | Run the following CLIs on all nodes in the given sequence, starting from the publisher node. | Note | Ensure that all nodes have an identical configuration. | Note | If there happens to be a disconnect and reconnect, check that the database replication is successfully set up across all nodes
                                                            in the cluster. Perform "Synchronize Cluster" from Cisco Unified Intelligence Center to ensure that cache is in sync across
                                                            the cluster. |
| Note | Run the following CLIs on all nodes in the given sequence, starting from the publisher node. |
| Note | Ensure that all nodes have an identical configuration. |
| Note | If there happens to be a disconnect and reconnect, check that the database replication is successfully set up across all nodes
                                                            in the cluster. Perform "Synchronize Cluster" from Cisco Unified Intelligence Center to ensure that cache is in sync across
                                                            the cluster. |

| Note | This is not applicable for Live Data and Ids installation. |
|---|---|

| Note | This is not applicable for Live Data and Ids installation. |
|---|---|

| Note | This is not applicable for Live Data and Ids installation. |
|---|---|

| Note | Follow the same steps for both the Cisco Finesse publisher and subscriber nodes. If there is a standalone Live Data system in this deployment, then upload Live Data tomcat certificate in addition to Cisco
                                                                  Finesse, using the above-stated procedure. |
|---|---|

| Note | Run the following CLIs on all nodes in the given sequence, starting from the publisher node. |
|---|---|

| Note | Ensure that all nodes have an identical configuration. |
|---|---|

| Note | If there happens to be a disconnect and reconnect, check that the database replication is successfully set up across all nodes
                                                            in the cluster. Perform "Synchronize Cluster" from Cisco Unified Intelligence Center to ensure that cache is in sync across
                                                            the cluster. |
|---|---|