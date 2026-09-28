---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-install-upgrade-guide-hcs-cc-b-ins-d60744e04a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Install_Upgrade_Guide/hcs-cc_b_installing-and-upgrading-guide_12_5/hcs-cc_b_installing-and-upgrading-guide-for_chapter_0111.html
retrieved_at: 2026-08-22T00:12:41.994457+00:00
---

Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

# Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

Chapter: Appendix

## Chapter: Appendix

# Appendix

## Core Components
                        	 Server

### Install Unified
                           	 Contact Center Enterprise

Step 1

Add the
                                          			 virtual machine template into the domain.

Step 2

Mount the
                                          			 Unified Contact Center Enterprise ISO image to the virtual machine.

Step 3

From the ICM-CCE-CCH Installer directory, run setup.exe and follow the InstallShield procedures.

Step 4

In the Select
                                             				the installation method window, select Fresh
                                             				Install , then click Next .

Step 5

In the Maintenance Release (MR) window, keep the Maintenance Release Location field blank, then click Next .

Step 6

In the Installation Location window, select the drive C , then click Next .

Step 7

In the Ready
                                             				to Copy Files window, click Install .

Step 8

In the Installation Complete window, click Yes, I
                                             				want to restart my computer now , then click Finish .

Step 9

Apply the
                                          			 Unified Contact Center Enterprise maintenance release, if applicable.

Step 10

Unmount the
                                          			 Unified Contact Center Enterprise ISO image.

Step 11

Move the
                                          			 virtual machine template back to the workgroup.

If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                         in the java certificate store, and removes all the unapproved certificates.

### Install Unified
                           	 CVP Server

Step 1

Mount the
                                          			 Unified CVP ISO image to the virtual machine.

Step 2

Copy the
                                          			 current Engineering Specials (ES) to the local drive.

Ignore this
                                                         				  step if there are no Engineering Specials.

Step 3

From the CVP\Installer_Windows directory, run setup.exe .

Step 4

In the Install Shield Wizard window:

Accept the
                                                				  license agreement and click Next .

In the Select Packages window, select CVP Server , then click Next .

In the Choose Destination Location window, select the folder
                                                				  locations for the CVP Installation Folder and the Media Files Installation
                                                				  Folder, then click Next .

In the X.509 Certificate window, enter the information that
                                                				  you want to include in the certificate.

In the Ready to Install the Program window, click Install .

Click Yes, I want to restart my computer now , Click Finish .

Step 5

Copy the
                                          			 required Cisco Unified CVP Engineering Special file to
                                          			 the desktop.

Step 6

If Unified CVP
                                          			 Engineering Specials are available, follow the Install Shield wizard. Ignore
                                          			 this step if there are no Engineering Specials.

Step 7

Add any
                                          			 custom media files to the appropriate location.

Step 8

Unmount the
                                          			 ISO image.

### Install Unified CVP
                           	 OAMP Server

Step 1

Mount the
                                          			 Unified CVP ISO image to the virtual machine.

Step 2

From the CVP\Installer_Windows directory, run setup.exe .

Step 3

Accept the
                                          			 license agreement, click Next .

Step 4

In the Select
                                             				Packages window, select the Operations Console option, then click Next .

Step 5

On the Choose
                                             				Destination Location window, accept the default locations, then
                                          			 click Next .

Step 6

In the X.509
                                             				certificate window, enter the information that you want to include
                                          			 in the certificate, then click Next .

Step 7

In the Ready to
                                             				Install window, click Install .

Step 8

Enter the
                                          			 operations console password that meets the criteria detailed on the Operations Console Password window, then click Next .

Step 9

Click Yes, I
                                             				want to restart my computer , then click Finish .

Step 10

Unmount the
                                          			 Unified CVP ISO image.

### Install Unified
                           	 CVP Reporting Server

Step 1

Mount the
                                          			 Unified CVP ISO image to the virtual machine.

Step 2

Copy the
                                          			 current Engineering Specials (ES) to the local drive.

Ignore this
                                                         				  step if there are no Engineering Specials.

Step 3

From the CVP\Installer_Windows directory, run setup.exe .

Step 4

In the Install Shield Wizard window:

Accept the
                                                				  license agreement, then click Next .

In the Select Packages window, select Reporting Server , then click Next .

In the Choose Destination Location window, select the folder
                                                				  location for the CVP Installation Folder, then click Next .

In the X.509 certificate window, enter the information that
                                                				  you want to include in the certificate, then click Next .

In the Choose the Database data and backups drive window,
                                                				  enter the name of the drive (typically E), and click Next .

In the Database size selection window, select Standard (250GB) or Premium (375GB) , then click Next .

Select Standard for 500 agent deployment and Premium for other HCS agent deployments.

In the Ready to Install window, click Install .

Enter the
                                                				  CVP Reporting Server password when prompted.

It can
                                                   					 take some time for the database to install.

Restart
                                                				  the server after installation.

Step 5

Copy the
                                          			 required CVP Engineering Special file to the desktop.

Step 6

If Unified CVP
                                          			 Engineering Specials are available, follow the Install Shield wizard to install
                                          			 them. Ignore this step if there are no Engineering Specials.

Step 7

Unmount the
                                          			 ISO image.

### Install Voice OS-Based
                              		Applications

Use the following procedures to install Voice OS-based applications:

Cisco Virtualized Voice Browser

Step 1

Mount the ISO
                                          			 file to the virtual machine and switch on.

Step 2

Follow the
                                          			 Install wizard:

On the Disk found page, click OK to check the media before installation.

Click OK .

On the Product Deployment Selection page, select the
                                                				  required product and click OK .

On the Proceed with Install page, click Yes .

On the Platform Installation Wizard page, select the Skip option.

After
                                                   					 installation, displays the Pre-existing Configuration Information page.

Press Ctrl+Alt to free your cursor.

Step 3

Shut down the
                                          			 virtual machine.

Step 4

Unmount the
                                          			 ISO image.

### Install Publishers/Primary Nodes of VOS-Based Contact Center Applications

#### Before you begin

DNS Configuration is mandatory for installation of Cisco Unified Communications Manager, Cisco Unified Intelligence Center,
                                 Cisco Finesse and Cisco Identity Service (IdS). To configure DNS, add the VMs to the forward and reverse lookups of the DNS.

Step 1

Create a
                                          			 virtual machine for your VOS-based contact center application using the OVA.

Step 2

Mount the ISO
                                          			 image for the software to the virtual machine.

Step 3

Select the virtual machine, power it on, and open the console.

Step 4

Follow the
                                          			 Install wizard, making selections as follows:

In the Disk Found screen, click OK to begin the verification of the media integrity.

In the Success screen, select OK .

In the Product Deployment Selection screen:

Cisco Unified Communications Manager

Cisco Finesse

Cisco Virtualized Voice Browser

Cisco Unified Intelligence Center

Live
                                                         						  Data

Cisco Identity Service (IdS)

Cisco Unified Intelligence Center with Live Data and IdS

For
                                                         						  the 2000 agent reference design, choose the coresident deployment option Cisco Unified Intelligence Center with Live Data and
                                                            							 IdS , and then select OK . The Cisco Unified Intelligence Center with Live Data and
                                                            							 IdS option installs Cisco Unified Intelligence Center with Live
                                                         						  Data and Cisco Identity Service (IdS) on the same server.

For
                                                         						  all other deployments, select one of the standalone install options. For
                                                         						  example, select Cisco Unified Intelligence Center , Live Data , or Cisco Identity Service (IdS) . Then select OK .

In the Proceed with Install screen, select Yes .

In the Platform Installation Wizard screen, select Proceed .

In the Apply Patch screen, select No .

In the Basic Install screen, select Continue .

In the Timezone Configuration screen, use the down arrow to
                                                				  choose the local time zone that most closely matches where your server is
                                                				  located. Select OK .

For
                                                               						Live Data servers, use the same timezone for all the nodes.

In the Auto Negotiation Configuration screen, select Continue .

In the MTU Configuration screen, select No to keep the default setting for Maximum
                                                				  Transmission Units.

In the DHCP Configuration screen, select No .

In the Static Network Configuration screen, enter static
                                                				  configuration values. Select OK .

In the DNS Client Configuration screen, click Yes to enable DNS client.

Enter your DNS client configuration. Select OK .

In the Administrator Login Configuration screen, enter the
                                                				  Platform administration username. Enter and confirm the password for the
                                                				  administrator. Select OK .

In the Certificate Information screen, enter data to create
                                                				  your Certificate Signing Request: Organization, Unit, Location, State, and
                                                				  Country. Select OK .

In the First Node Configuration screen, select Yes .

In the Network Time Protocol Client Configuration screen,
                                                				  enter a valid NTP server IP address and select OK .

In the Security Configuration screen, enter the security
                                                				  password and select OK .

In the SMTP Host Configuration screen, select No .

In the Application User Configuration screen, enter the
                                                				  application username. Enter, and confirm the application user password. Select OK .

In the Platform Configuration Confirmation screen, select OK . The installation begins and runs unattended.

There is a reboot in the middle of the installation.

The installation ends at a sign-in prompt.

Step 5

Unmount the
                                          			 ISO image.

### Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications

This task is required for installation of the subscriber/secondary nodes of the three VOS-based contact center applications:
                                             Cisco Finesse, Cisco Unified Communications Manager, and Cisco Unified Intelligence Center.

#### Before you begin

DNS Configuration is mandatory for installation of Cisco Unified Communications Manager, Cisco Unified Intelligence Center,
                                 and Cisco Finesse. To configure DNS, add the VMs to the forward and reverse lookups of the DNS.

Before you install the subscriber/secondary nodes, you must install the publisher/primary nodes and configure the clusters.

Step 1

Create a virtual machine for your VOS-based contact center application using the OVA.

Step 2

Mount the ISO image for the software to the virtual machine.

Step 3

Select the virtual machine and power it on, and open the console.

Step 4

Follow the Install wizard, making selections as follows:

In the Disk Found screen, click OK to begin the verification of the media integrity.

In the Success screen, select OK .

In the Product Deployment Selection screen:

Cisco Unified Communications Manager

Cisco Finesse

Cisco Virtualized Voice Browser

Cisco Unified Intelligence Center

Live Data

Cisco Identity Service (IdS)

Cisco Unified Intelligence Center with Live Data and IdS

For the 2000 agent reference design, choose the coresident deployment option Cisco Unified Intelligence Center with Live Data and IdS , and then select OK . The Cisco Unified Intelligence Center with Live Data and IdS option installs Cisco Unified Intelligence Center with Live Data and Cisco Identity Service (IdS) on the same server.

For all other deployments, select one of the standalone install options. For example, select Cisco Unified Intelligence Center , Live Data , or Cisco Identity Service (IdS) . Then select OK .

Step 5

Follow the Install wizard, making selections as follows:

In the Proceed with Install screen, select Yes .

In the Platform Installation Wizard screen, select Proceed .

In the Apply Patch screen, select No .

In the Basic Install screen, select Continue .

In the Timezone Configuration screen, use the down arrow to choose the local time zone that most closely matches where your server is located. Select OK .

For Live Data servers, use the same timezone for all the nodes.

In the Auto Negotiation Configuration screen, select Continue .

In the MTU Configuration screen, select No to keep the default setting for Maximum Transmission Units.

In the DHCP Configuration screen, select No .

In the Static Network Configuration screen, enter static configuration values. Select OK .

In the DNS Client Configuration screen, click Yes to enable DNS client.

In the Administrator Login Configuration screen, enter the Platform administration username. Enter and confirm the password for the administrator. Select OK .

In the Certificate Information screen, enter data to create your Certificate Signing Request: Organization, Unit, Location, State, and Country. Select OK .

In the First Node Configuration screen, select No .

In the warning screen, select OK .

In the Network Connectivity Test Configuration screen, select No .

In the First Node Access Configuration screen, enter the host name and IP address of the first node. Enter and confirm the security password. Select OK .

In the SMTP Host Configuration screen, select No .

In the Platform Configuration Confirmation screen, select OK . The installation begins and runs unattended.

There is a reboot in the middle of the installation.

The installation ends at a sign-in prompt.

Step 6

Unmount the ISO image.

| Step 1 | Add the
                                          			 virtual machine template into the domain. |
|---|---|
| Step 2 | Mount the
                                          			 Unified Contact Center Enterprise ISO image to the virtual machine. |
| Step 3 | From the ICM-CCE-CCH Installer directory, run setup.exe and follow the InstallShield procedures. |
| Step 4 | In the Select
                                             				the installation method window, select Fresh
                                             				Install , then click Next . |
| Step 5 | In the Maintenance Release (MR) window, keep the Maintenance Release Location field blank, then click Next . |
| Step 6 | In the Installation Location window, select the drive C , then click Next . |
| Step 7 | In the Ready
                                             				to Copy Files window, click Install . |
| Step 8 | In the Installation Complete window, click Yes, I
                                             				want to restart my computer now , then click Finish . |
| Step 9 | Apply the
                                          			 Unified Contact Center Enterprise maintenance release, if applicable. |
| Step 10 | Unmount the
                                          			 Unified Contact Center Enterprise ISO image. |
| Step 11 | Move the
                                          			 virtual machine template back to the workgroup. Note If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                         in the java certificate store, and removes all the unapproved certificates. | Note | If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                         in the java certificate store, and removes all the unapproved certificates. |
| Note | If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                         in the java certificate store, and removes all the unapproved certificates. |

| Note | If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                         in the java certificate store, and removes all the unapproved certificates. |
|---|---|

| Step 1 | Mount the
                                          			 Unified CVP ISO image to the virtual machine. |
|---|---|
| Step 2 | Copy the
                                          			 current Engineering Specials (ES) to the local drive. Note Ignore this
                                                         				  step if there are no Engineering Specials. | Note | Ignore this
                                                         				  step if there are no Engineering Specials. |
| Note | Ignore this
                                                         				  step if there are no Engineering Specials. |
| Step 3 | From the CVP\Installer_Windows directory, run setup.exe . |
| Step 4 | In the Install Shield Wizard window: Accept the
                                                				  license agreement and click Next . In the Select Packages window, select CVP Server , then click Next . In the Choose Destination Location window, select the folder
                                                				  locations for the CVP Installation Folder and the Media Files Installation
                                                				  Folder, then click Next . In the X.509 Certificate window, enter the information that
                                                				  you want to include in the certificate. In the Ready to Install the Program window, click Install . Click Yes, I want to restart my computer now , Click Finish . |
| Step 5 | Copy the
                                          			 required Cisco Unified CVP Engineering Special file to
                                          			 the desktop. |
| Step 6 | If Unified CVP
                                          			 Engineering Specials are available, follow the Install Shield wizard. Ignore
                                          			 this step if there are no Engineering Specials. |
| Step 7 | Add any
                                          			 custom media files to the appropriate location. |
| Step 8 | Unmount the
                                          			 ISO image. |

| Note | Ignore this
                                                         				  step if there are no Engineering Specials. |
|---|---|

| Step 1 | Mount the
                                          			 Unified CVP ISO image to the virtual machine. |
|---|---|
| Step 2 | From the CVP\Installer_Windows directory, run setup.exe . |
| Step 3 | Accept the
                                          			 license agreement, click Next . |
| Step 4 | In the Select
                                             				Packages window, select the Operations Console option, then click Next . |
| Step 5 | On the Choose
                                             				Destination Location window, accept the default locations, then
                                          			 click Next . |
| Step 6 | In the X.509
                                             				certificate window, enter the information that you want to include
                                          			 in the certificate, then click Next . |
| Step 7 | In the Ready to
                                             				Install window, click Install . |
| Step 8 | Enter the
                                          			 operations console password that meets the criteria detailed on the Operations Console Password window, then click Next . |
| Step 9 | Click Yes, I
                                             				want to restart my computer , then click Finish . |
| Step 10 | Unmount the
                                          			 Unified CVP ISO image. |

| Step 1 | Mount the
                                          			 Unified CVP ISO image to the virtual machine. |
|---|---|
| Step 2 | Copy the
                                          			 current Engineering Specials (ES) to the local drive. Note Ignore this
                                                         				  step if there are no Engineering Specials. | Note | Ignore this
                                                         				  step if there are no Engineering Specials. |
| Note | Ignore this
                                                         				  step if there are no Engineering Specials. |
| Step 3 | From the CVP\Installer_Windows directory, run setup.exe . |
| Step 4 | In the Install Shield Wizard window: Accept the
                                                				  license agreement, then click Next . In the Select Packages window, select Reporting Server , then click Next . In the Choose Destination Location window, select the folder
                                                				  location for the CVP Installation Folder, then click Next . In the X.509 certificate window, enter the information that
                                                				  you want to include in the certificate, then click Next . In the Choose the Database data and backups drive window,
                                                				  enter the name of the drive (typically E), and click Next . In the Database size selection window, select Standard (250GB) or Premium (375GB) , then click Next . Note Select Standard for 500 agent deployment and Premium for other HCS agent deployments. In the Ready to Install window, click Install . Enter the
                                                				  CVP Reporting Server password when prompted. It can
                                                   					 take some time for the database to install. Restart
                                                				  the server after installation. | Note | Select Standard for 500 agent deployment and Premium for other HCS agent deployments. |
| Note | Select Standard for 500 agent deployment and Premium for other HCS agent deployments. |
| Step 5 | Copy the
                                          			 required CVP Engineering Special file to the desktop. |
| Step 6 | If Unified CVP
                                          			 Engineering Specials are available, follow the Install Shield wizard to install
                                          			 them. Ignore this step if there are no Engineering Specials. |
| Step 7 | Unmount the
                                          			 ISO image. |

| Note | Ignore this
                                                         				  step if there are no Engineering Specials. |
|---|---|

| Note | Select Standard for 500 agent deployment and Premium for other HCS agent deployments. |
|---|---|

| Step 1 | Mount the ISO
                                          			 file to the virtual machine and switch on. |
|---|---|
| Step 2 | Follow the
                                          			 Install wizard: On the Disk found page, click OK to check the media before installation. Click OK . On the Product Deployment Selection page, select the
                                                				  required product and click OK . On the Proceed with Install page, click Yes . On the Platform Installation Wizard page, select the Skip option. After
                                                   					 installation, displays the Pre-existing Configuration Information page. Press Ctrl+Alt to free your cursor. |
| Step 3 | Shut down the
                                          			 virtual machine. |
| Step 4 | Unmount the
                                          			 ISO image. |

| Step 1 | Create a
                                          			 virtual machine for your VOS-based contact center application using the OVA. |
|---|---|
| Step 2 | Mount the ISO
                                          			 image for the software to the virtual machine. |
| Step 3 | Select the virtual machine, power it on, and open the console. |
| Step 4 | Follow the
                                          			 Install wizard, making selections as follows: In the Disk Found screen, click OK to begin the verification of the media integrity. In the Success screen, select OK . In the Product Deployment Selection screen: If your
                                                				  product is any one of the following, choose the product and click OK . Cisco Unified Communications Manager Cisco Finesse Cisco Virtualized Voice Browser If your product is Cisco Unified Intelligence Center, you
                                                				  can choose from one of the following options: Cisco Unified Intelligence Center Live
                                                         						  Data Cisco Identity Service (IdS) Cisco Unified Intelligence Center with Live Data and IdS For
                                                         						  the 2000 agent reference design, choose the coresident deployment option Cisco Unified Intelligence Center with Live Data and
                                                            							 IdS , and then select OK . The Cisco Unified Intelligence Center with Live Data and
                                                            							 IdS option installs Cisco Unified Intelligence Center with Live
                                                         						  Data and Cisco Identity Service (IdS) on the same server. For
                                                         						  all other deployments, select one of the standalone install options. For
                                                         						  example, select Cisco Unified Intelligence Center , Live Data , or Cisco Identity Service (IdS) . Then select OK . In the Proceed with Install screen, select Yes . In the Platform Installation Wizard screen, select Proceed . In the Apply Patch screen, select No . In the Basic Install screen, select Continue . In the Timezone Configuration screen, use the down arrow to
                                                				  choose the local time zone that most closely matches where your server is
                                                				  located. Select OK . Note For
                                                               						Live Data servers, use the same timezone for all the nodes. In the Auto Negotiation Configuration screen, select Continue . In the MTU Configuration screen, select No to keep the default setting for Maximum
                                                				  Transmission Units. In the DHCP Configuration screen, select No . In the Static Network Configuration screen, enter static
                                                				  configuration values. Select OK . In the DNS Client Configuration screen, click Yes to enable DNS client. Enter your DNS client configuration. Select OK . In the Administrator Login Configuration screen, enter the
                                                				  Platform administration username. Enter and confirm the password for the
                                                				  administrator. Select OK . In the Certificate Information screen, enter data to create
                                                				  your Certificate Signing Request: Organization, Unit, Location, State, and
                                                				  Country. Select OK . In the First Node Configuration screen, select Yes . In the Network Time Protocol Client Configuration screen,
                                                				  enter a valid NTP server IP address and select OK . In the Security Configuration screen, enter the security
                                                				  password and select OK . In the SMTP Host Configuration screen, select No . In the Application User Configuration screen, enter the
                                                				  application username. Enter, and confirm the application user password. Select OK . In the Platform Configuration Confirmation screen, select OK . The installation begins and runs unattended. There is a reboot in the middle of the installation. The installation ends at a sign-in prompt. | Note | For
                                                               						Live Data servers, use the same timezone for all the nodes. |
| Note | For
                                                               						Live Data servers, use the same timezone for all the nodes. |
| Step 5 | Unmount the
                                          			 ISO image. |

| Note | For
                                                               						Live Data servers, use the same timezone for all the nodes. |
|---|---|

| Note | This task is required for installation of the subscriber/secondary nodes of the three VOS-based contact center applications:
                                             Cisco Finesse, Cisco Unified Communications Manager, and Cisco Unified Intelligence Center. |
|---|---|

| Step 1 | Create a virtual machine for your VOS-based contact center application using the OVA. |
|---|---|
| Step 2 | Mount the ISO image for the software to the virtual machine. |
| Step 3 | Select the virtual machine and power it on, and open the console. |
| Step 4 | Follow the Install wizard, making selections as follows: In the Disk Found screen, click OK to begin the verification of the media integrity. In the Success screen, select OK . In the Product Deployment Selection screen: If your product is any one of the following, choose the product and click OK . Cisco Unified Communications Manager Cisco Finesse Cisco Virtualized Voice Browser If your product is Cisco Unified Intelligence Center, you can choose from one of the following options: Cisco Unified Intelligence Center Live Data Cisco Identity Service (IdS) Cisco Unified Intelligence Center with Live Data and IdS For the 2000 agent reference design, choose the coresident deployment option Cisco Unified Intelligence Center with Live Data and IdS , and then select OK . The Cisco Unified Intelligence Center with Live Data and IdS option installs Cisco Unified Intelligence Center with Live Data and Cisco Identity Service (IdS) on the same server. For all other deployments, select one of the standalone install options. For example, select Cisco Unified Intelligence Center , Live Data , or Cisco Identity Service (IdS) . Then select OK . |
| Step 5 | Follow the Install wizard, making selections as follows: In the Proceed with Install screen, select Yes . In the Platform Installation Wizard screen, select Proceed . In the Apply Patch screen, select No . In the Basic Install screen, select Continue . In the Timezone Configuration screen, use the down arrow to choose the local time zone that most closely matches where your server is located. Select OK . Note For Live Data servers, use the same timezone for all the nodes. In the Auto Negotiation Configuration screen, select Continue . In the MTU Configuration screen, select No to keep the default setting for Maximum Transmission Units. In the DHCP Configuration screen, select No . In the Static Network Configuration screen, enter static configuration values. Select OK . In the DNS Client Configuration screen, click Yes to enable DNS client. In the Administrator Login Configuration screen, enter the Platform administration username. Enter and confirm the password for the administrator. Select OK . In the Certificate Information screen, enter data to create your Certificate Signing Request: Organization, Unit, Location, State, and Country. Select OK . In the First Node Configuration screen, select No . In the warning screen, select OK . In the Network Connectivity Test Configuration screen, select No . In the First Node Access Configuration screen, enter the host name and IP address of the first node. Enter and confirm the security password. Select OK . In the SMTP Host Configuration screen, select No . In the Platform Configuration Confirmation screen, select OK . The installation begins and runs unattended. There is a reboot in the middle of the installation. The installation ends at a sign-in prompt. | Note | For Live Data servers, use the same timezone for all the nodes. |
| Note | For Live Data servers, use the same timezone for all the nodes. |
| Step 6 | Unmount the ISO image. |

| Note | For Live Data servers, use the same timezone for all the nodes. |
|---|---|