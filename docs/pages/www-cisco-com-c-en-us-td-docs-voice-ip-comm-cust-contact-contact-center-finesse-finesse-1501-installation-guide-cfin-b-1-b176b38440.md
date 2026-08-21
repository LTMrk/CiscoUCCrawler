---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-installation-guide-cfin-b-1-b176b38440
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/installation/guide/cfin_b_1501_cisco-installation-and-upgrade-guide-15_0/cfin_m_1501_cisco-finesse-server-installation.html
retrieved_at: 2026-08-21T15:52:57.009040+00:00
---

Cisco Finesse Installation and Upgrade Guide, Release 15.0(1)

# Cisco Finesse Installation and Upgrade Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Cisco Finesse Server Installation

## Chapter: Cisco Finesse Server Installation

# Cisco Finesse Server Installation

## Installation Task
                        	 Flow

The following table provides an overview of the tasks you perform to
                              		  install Cisco Finesse. Tasks must be performed in the order they are listed.

1

Install Finesse on the primary node.

2

Configure the database settings.

3

Configure the CTI server settings.

4

Configure the cluster settings for the secondary node.

5

Restart Cisco Finesse
                                          						Tomcat on the primary node.

6

Install Finesse on the secondary node.

7

Ensure replication is functioning between the two nodes.

8

Install language packs (optional).

## Install Finesse on
                        	 Primary Node

Step 1

Follow the
                                       			 instructions in the OVA README.txt file to import and deploy the OVA, to edit
                                       			 VM settings, and to power on the VM and edit the BIOS settings in the console.
                                       			 For more information, see the section on Installation
                                          				Files .

Do not use
                                                      				  Thin Provisioning or a VM snapshot when creating a VM to host Cisco Finesse.
                                                      				  The use of Thin Provisioning or snapshots can negatively impact the performance
                                                      				  of Cisco Finesse operation.

Messages
                                          				appear while the preinstallation script runs. When the preinstallation script
                                          				ends, the DVD Found screen opens.

Step 2

Select OK on the Disk Found screen to begin the
                                       			 verification of the media integrity and a brief hardware check.

If the media
                                          				check passes, select OK to open the Product Deployment Selection screen.
                                          				Continue to Step 3.

If the media
                                          				check fails, the installation terminates.

Step 3

The Product
                                       			 Deployment Selection screen states that the Cisco Finesse product suite will be installed. This screen has only one choice: OK .

Select OK to open the Proceed with Install screen.

Step 4

The Proceed
                                       			 with Install screen shows the version of the product that is currently
                                       			 installed (if any) and the version of the product for this ISO. For the initial
                                       			 installation, the version currently installed shows NONE.

Select Yes on the Proceed with Install screen to open the
                                          				Platform Installation Wizard screen.

Step 5

On the
                                       			 Platform Installation Wizard screen, select Proceed to open the Basic Install screen.

Step 6

Select Continue on the Basic Install screen to open the
                                       			 Basic Install wizard.

The Basic
                                          				Install wizard presents a series of screens that present questions and options
                                          				pertinent to the platform and the setup configuration. Help is available for
                                          				each wizard screen.

The first
                                          				Basic Install wizard screen is Timezone Configuration.

Step 7

On the
                                       			 Timezone Configuration screen:

Use the up
                                             				  and down arrows to locate the local time zone that most closely matches your
                                             				  server location. You can also type the initial character of the time zone to
                                             				  move to that item in the list. The Timezone field is based on country and city
                                             				  and is mandatory. Setting it incorrectly can affect system operation.

Select OK to open the Auto Negotiation Configuration
                                             				  screen.

Step 8

On the Auto Negotiation Configuration screen, select Continue to use automatic negotiation for the settings of the Ethernet network interface card (NIC).

The MTU Configuration screen appears.

Step 9

In the MTU
                                       			 Configuration screen, select No to keep the default setting for Maximum
                                       			 Transmission Units (1500).

Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported.

Your selection
                                          				of No opens the Static Network Configuration screen.

Step 10

On the Static
                                       			 Network Configuration screen, enter static network configuration values as
                                       			 follows, referring to the Configuration Worksheet if necessary:

Enter the Host
                                                					 Name .

Enter the IP
                                                					 Address .

Enter the IP
                                                					 Mask .

Enter the GW
                                                					 Address .

Select OK to open the Domain Name System (DNS) Client
                                             				  Configuration screen.

Step 11

On the DNS
                                       			 Client Configuration screen, select Yes to specify the DNS client information.

Important

DNS client
                                                      				  configuration is mandatory for Cisco Finesse. Select Yes on this screen. If
                                                      				  you select No, after the installation is complete, agents cannot sign in to the desktop and you have to reinstall Finesse.

Step 12

Specify your
                                       			 DNS client information as follows, referring to the Configuration Worksheet if
                                       			 necessary:

Enter
                                             				  the Primary
                                                					 DNS (mandatory).

Enter
                                             				  the Secondary DNS (optional).

Enter
                                             				  the Domain (mandatory).

Select OK to open the Administrator Login Configuration
                                             				  screen.

Step 13

On the
                                       			 Administrator Login Configuration screen:

Enter
                                             				  the credentials for the administrator.

Select OK to open the Certificate Information screen.

Step 14

On the
                                       			 Certificate Information screen:

Enter
                                             				  the following data to create your Certificate Signing Request: Organization,
                                             				  Unit, Location, State, and Country.

Select OK to open the First Node Configuration screen.

Step 15

On the First
                                       			 Node Configuration screen, select Yes to indicate that you are configuring the first
                                       			 node.

Your
                                          				selection of Yes opens the Network Time Protocol Client Configuration screen.

Step 16

On the
                                       			 Network Time Protocol Client Configuration screen, enter the IP address, NTP
                                       			 server name, or NTP Server Pool name for at least one external NTP server.

Step 17

After you
                                       			 complete the NTP configuration, select OK . This action opens the Security Configuration
                                       			 screen.

Step 18

On the
                                       			 Security Configuration screen, enter the Database Access Security password, and
                                       			 then select OK .

Step 19

On the
                                       			 Application User Configuration screen, enter the credentials for the
                                       			 application user.

Select OK to open the Platform Configuration Confirmation
                                          				screen. This screen states that the platform configuration is complete.

Step 20

On the
                                       			 Platform Configuration Confirmation screen, select OK .

The
                                          				installation begins.

The
                                          				installation can take up to an hour to complete and can run unattended for most
                                          				of that time.

During the
                                          				installation, the monitor shows a series of processes, as follows:

Formatting progress bars

Copying
                                                					 File progress bar

Package
                                                					 Installation progress bars

Post
                                                					 Install progress bar

Populate
                                                					 RPM Archive progress bar

Application Installation progress bars (multiple Component
                                                					 Install screens, security checks)

An
                                                					 informational screen saying the system will reboot momentarily to continue the
                                                					 installation

A system
                                                					 reboot

Messages
                                                					 stream down your monitor during the reboot. Some of them prompt you to press a
                                                					 key. Do
                                                   						not respond to these prompts to press a key.

Application Pre Install progress bars

Configure and Setup Network progress bars

If a
                                                            						Network Connectivity Failure screen appears during the Configure and Setup
                                                            						Network process, click Review , and then click OK at the Errors screen. Follow the prompts to
                                                            						reenter the information that caused the failure. The installation continues
                                                            						when the connection information is complete.

Security
                                                					 configuration

A message
                                          				appears that states the installation of Cisco Finesse has completed
                                          				successfully.

```
The installation of Cisco Finesse has completed successfully.

Cisco Finesse < version number >
< hostname > login: _
```

### What to do next

Sign in to the Finesse administration console on the primary Finesse server (https:// FQDN of Finesse server:8445 /cfadmin) to configure CTI server, Administration & Database server, and cluster settings.

After you
                              		  configure these settings, install Finesse on the secondary node.

## Install Finesse on
                        	 Secondary Node

Install the same
                              		  version of Finesse on both the primary and secondary Finesse nodes.

Configure a
                                          			 Datastore ISO file on the virtual CD/DVD drive of the target VM to install
                                          			 Finesse.

Finesse
                                          			 administration tasks can only be performed on the primary Finesse server. After
                                          			 you install the secondary server, sign in to the administration console on the
                                          			 primary server to perform administration tasks (such as configuring reason
                                          			 codes or call variable layout).

### Before you begin

Install
                                    				Finesse on the primary server. See Install
                                       				  Finesse on Primary Node .

Use the
                                    				Finesse administration console on the primary Finesse server to configure CTI
                                    				server, Administration & Database server, and cluster settings.

Ensure that
                                    				the DNS server has forward and reverse DNS set up for both the primary and
                                    				secondary node.

Step 1

Follow the
                                       			 instructions in the OVA README.txt file to import and deploy the OVA, to edit
                                       			 VM settings, and to power on the VM and edit the BIOS settings in the Console.

Messages
                                          				appear while the preinstallation script runs. When the preinstallation script
                                          				ends, the DVD Found screen opens.

Step 2

Select Yes on the DVD Found screen to begin the
                                       			 verification of the media integrity and a brief hardware check.

If the media
                                          				check passes, select OK to open the Product Deployment Selection screen.
                                          				Continue to Step 3.

If the media
                                          				check fails, the installation terminates.

Step 3

The Product Deployment Selection screen states that the Cisco Finesse product suite will be installed. This screen has only one option: OK .

Select OK to open the Proceed with Install screen.

Step 4

The Proceed
                                       			 with Install screen shows the version of the product that is currently
                                       			 installed (if any) and the version of the product for this ISO. For the initial
                                       			 installation, the version currently installed shows NONE.

Select Yes on the Proceed with Install screen to open the
                                          				Platform Installation Wizard screen.

Step 5

On the
                                       			 Platform Installation Wizard screen, select Proceed to open the Basic Install screen.

Step 6

Select Continue on the Basic Install screen to open the
                                       			 Basic Install wizard.

The Basic
                                          				Install wizard presents a series of screens that present questions and options
                                          				pertinent to the platform and the setup configuration. Help is available for
                                          				each wizard screen.

The first
                                          				Basic Install wizard screen is Timezone Configuration.

Step 7

In the
                                       			 Timezone Configuration screen:

Use the up
                                             				  and down arrows to locate the local time zone that most closely matches your
                                             				  server location. You can also type the initial character of the time zone to
                                             				  move to that item in the list. The Timezone field is based on country and city
                                             				  and is mandatory. Setting it incorrectly can affect system operation.

Select OK to open the Auto Negotiation Configuration
                                             				  screen.

Step 8

On the Auto Negotiation Configuration screen, select Continue to use automatic negotiation for the settings of the Ethernet network interface card (NIC).

The MTU Configuration screen appears.

Step 9

On the MTU
                                       			 Configuration screen, select No to keep the default setting for Maximum
                                       			 Transmission Units (1500).

Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported.

Your selection
                                          				of No opens the Static Network Configuration screen.

Step 10

On the Static Network Configuration screen, enter the static network configuration values as follows, referring to the Configuration
                                       Worksheet if necessary:

Enter the Host Name .

Enter the IP Address .

Enter the IP Mask .

Enter the GW Address .

Select OK to open the Domain Name System (DNS) Client Configuration screen.

Step 11

On the DNS Client
                                          				Configuration screen, select Yes to specify the DNS client information.

IMPORTANT: DNS client configuration is mandatory for Cisco Finesse. Select Yes on this screen. If you select No, after the installation is complete, agents can't sign in to the desktop and you have to reinstall Finesse.

Step 12

Specify your
                                       			 DNS client information as follows, referring to the Configuration Worksheet if
                                       			 necessary:

Enter
                                             				  the Primary
                                                					 DNS (mandatory).

Enter
                                             				  the Secondary DNS (optional).

Enter
                                             				  the Domain (mandatory).

Select OK to open the Administrator Login Configuration
                                             				  screen.

Step 13

On the
                                       			 Administrator Login Configuration screen:

Enter
                                             				  the credentials for the administrator.

Select OK to open the Certificate Information screen.

Step 14

On the
                                       			 Certificate Information screen:

Enter
                                             				  the following data to create your Certificate Signing Request: Organization,
                                             				  Unit, Location, State, and Country.

Select OK to open the First Node Configuration screen.

Step 15

On the First Node Configuration screen, select No to indicate that you’re configuring the second node.

A warning message appears that indicates you must first configure the server on the first node before you can proceed. If
                                          you already configured the first node, select OK .

Step 16

On the
                                       			 Network Connectivity Test Configuration screen, select No to proceed with the installation after
                                       			 connectivity is verified.

Step 17

On the First
                                       			 Node Configuration screen, specify the information about the first node as
                                       			 follows:

Enter
                                             				  the Host
                                                					 Name of the primary Finesse server.

Enter
                                             				  the IP
                                                					 Address of the primary Finesse server.

Enter
                                             				  the Security
                                                					 Password of the primary Finesse server.

Confirm
                                             				  the Security
                                                					 Password .

Step 18

Select OK to open the Platform Configuration Confirmation
                                       			 screen.

Step 19

On the
                                       			 Platform Configuration Confirmation screen, select OK .

The
                                          				installation begins.

The
                                          				installation can take up to an hour to complete and can run unattended for most
                                          				of that time.

A message
                                          				appears that states the installation of Cisco Finesse has completed
                                          				successfully.

```
The installation of Cisco Finesse has completed successfully.

Cisco Finesse < version number >
< hostname > login: _
```

### What to do next

Check the replication status. If all nodes in the cluster show a replication status of 2 , replication is functioning correctly.

After installation, by default the configuration that controls the reverse-proxy authentication is enabled. When the reverse-proxy
                              authentication is enabled and multiple client-side certificates are configured on the system, it impacts the certificate acceptance
                              pop-ups from clients that are connected directly to the Finesse server without using a reverse-proxy. To prevent these pop-ups
                              from appearing, use the utils systems reverse-proxy client-auth command on both the Finesse nodes to disable the reverse-proxy authentication that don’t need VPN-less access to Finesse.

It can take
                                          			 10–20 minutes to establish replication fully between the two nodes.

To access platform-specific applications like Disaster Recovery System, Cisco Unified Serviceability, and Cisco Unified Operating
                                          System Administration, use the following URL, https:// FQDN of Finesse server :8443.

## Installation
                        	 Troubleshooting

If

Then

The
                                          						installation fails.

If the
                                          						installation fails, a screen appears that asks if you want to copy diagnostic
                                          						information to a device.

In this
                                          						situation, you must reinstall from the beginning, but first you must attach a
                                          						serial port to the VM. Then, you dump the install logs into the serial port of
                                          						the VM.

| 1 | Install Finesse on the primary node. |
|---|---|
| 2 | Configure the database settings. |
| 3 | Configure the CTI server settings. |
| 4 | Configure the cluster settings for the secondary node. |
| 5 | Restart Cisco Finesse
                                          						Tomcat on the primary node. |
| 6 | Install Finesse on the secondary node. |
| 7 | Ensure replication is functioning between the two nodes. |
| 8 | Install language packs (optional). |

| Step 1 | Follow the
                                       			 instructions in the OVA README.txt file to import and deploy the OVA, to edit
                                       			 VM settings, and to power on the VM and edit the BIOS settings in the console.
                                       			 For more information, see the section on Installation
                                          				Files . Note Do not use
                                                      				  Thin Provisioning or a VM snapshot when creating a VM to host Cisco Finesse.
                                                      				  The use of Thin Provisioning or snapshots can negatively impact the performance
                                                      				  of Cisco Finesse operation. Messages
                                          				appear while the preinstallation script runs. When the preinstallation script
                                          				ends, the DVD Found screen opens. | Note | Do not use
                                                      				  Thin Provisioning or a VM snapshot when creating a VM to host Cisco Finesse.
                                                      				  The use of Thin Provisioning or snapshots can negatively impact the performance
                                                      				  of Cisco Finesse operation. |
|---|---|---|---|
| Note | Do not use
                                                      				  Thin Provisioning or a VM snapshot when creating a VM to host Cisco Finesse.
                                                      				  The use of Thin Provisioning or snapshots can negatively impact the performance
                                                      				  of Cisco Finesse operation. |
| Step 2 | Select OK on the Disk Found screen to begin the
                                       			 verification of the media integrity and a brief hardware check. If the media
                                          				check passes, select OK to open the Product Deployment Selection screen.
                                          				Continue to Step 3. If the media
                                          				check fails, the installation terminates. |
| Step 3 | The Product
                                       			 Deployment Selection screen states that the Cisco Finesse product suite will be installed. This screen has only one choice: OK . Select OK to open the Proceed with Install screen. |
| Step 4 | The Proceed
                                       			 with Install screen shows the version of the product that is currently
                                       			 installed (if any) and the version of the product for this ISO. For the initial
                                       			 installation, the version currently installed shows NONE. Select Yes on the Proceed with Install screen to open the
                                          				Platform Installation Wizard screen. |
| Step 5 | On the
                                       			 Platform Installation Wizard screen, select Proceed to open the Basic Install screen. |
| Step 6 | Select Continue on the Basic Install screen to open the
                                       			 Basic Install wizard. The Basic
                                          				Install wizard presents a series of screens that present questions and options
                                          				pertinent to the platform and the setup configuration. Help is available for
                                          				each wizard screen. The first
                                          				Basic Install wizard screen is Timezone Configuration. |
| Step 7 | On the
                                       			 Timezone Configuration screen: Use the up
                                             				  and down arrows to locate the local time zone that most closely matches your
                                             				  server location. You can also type the initial character of the time zone to
                                             				  move to that item in the list. The Timezone field is based on country and city
                                             				  and is mandatory. Setting it incorrectly can affect system operation. Select OK to open the Auto Negotiation Configuration
                                             				  screen. |
| Step 8 | On the Auto Negotiation Configuration screen, select Continue to use automatic negotiation for the settings of the Ethernet network interface card (NIC). The MTU Configuration screen appears. |
| Step 9 | In the MTU
                                       			 Configuration screen, select No to keep the default setting for Maximum
                                       			 Transmission Units (1500). Note Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported. Your selection
                                          				of No opens the Static Network Configuration screen. | Note | Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported. |
| Note | Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported. |
| Step 10 | On the Static
                                       			 Network Configuration screen, enter static network configuration values as
                                       			 follows, referring to the Configuration Worksheet if necessary: Enter the Host
                                                					 Name . Enter the IP
                                                					 Address . Enter the IP
                                                					 Mask . Enter the GW
                                                					 Address . Select OK to open the Domain Name System (DNS) Client
                                             				  Configuration screen. |
| Step 11 | On the DNS
                                       			 Client Configuration screen, select Yes to specify the DNS client information. Important DNS client
                                                      				  configuration is mandatory for Cisco Finesse. Select Yes on this screen. If
                                                      				  you select No, after the installation is complete, agents cannot sign in to the desktop and you have to reinstall Finesse. | Important | DNS client
                                                      				  configuration is mandatory for Cisco Finesse. Select Yes on this screen. If
                                                      				  you select No, after the installation is complete, agents cannot sign in to the desktop and you have to reinstall Finesse. |
| Important | DNS client
                                                      				  configuration is mandatory for Cisco Finesse. Select Yes on this screen. If
                                                      				  you select No, after the installation is complete, agents cannot sign in to the desktop and you have to reinstall Finesse. |
| Step 12 | Specify your
                                       			 DNS client information as follows, referring to the Configuration Worksheet if
                                       			 necessary: Enter
                                             				  the Primary
                                                					 DNS (mandatory). Enter
                                             				  the Secondary DNS (optional). Enter
                                             				  the Domain (mandatory). Select OK to open the Administrator Login Configuration
                                             				  screen. |
| Step 13 | On the
                                       			 Administrator Login Configuration screen: Enter
                                             				  the credentials for the administrator. Select OK to open the Certificate Information screen. |
| Step 14 | On the
                                       			 Certificate Information screen: Enter
                                             				  the following data to create your Certificate Signing Request: Organization,
                                             				  Unit, Location, State, and Country. Select OK to open the First Node Configuration screen. |
| Step 15 | On the First
                                       			 Node Configuration screen, select Yes to indicate that you are configuring the first
                                       			 node. Your
                                          				selection of Yes opens the Network Time Protocol Client Configuration screen. |
| Step 16 | On the
                                       			 Network Time Protocol Client Configuration screen, enter the IP address, NTP
                                       			 server name, or NTP Server Pool name for at least one external NTP server. |
| Step 17 | After you
                                       			 complete the NTP configuration, select OK . This action opens the Security Configuration
                                       			 screen. |
| Step 18 | On the
                                       			 Security Configuration screen, enter the Database Access Security password, and
                                       			 then select OK . |
| Step 19 | On the
                                       			 Application User Configuration screen, enter the credentials for the
                                       			 application user. Select OK to open the Platform Configuration Confirmation
                                          				screen. This screen states that the platform configuration is complete. |
| Step 20 | On the
                                       			 Platform Configuration Confirmation screen, select OK . The
                                          				installation begins. The
                                          				installation can take up to an hour to complete and can run unattended for most
                                          				of that time. During the
                                          				installation, the monitor shows a series of processes, as follows: Formatting progress bars Copying
                                                					 File progress bar Package
                                                					 Installation progress bars Post
                                                					 Install progress bar Populate
                                                					 RPM Archive progress bar Application Installation progress bars (multiple Component
                                                					 Install screens, security checks) An
                                                					 informational screen saying the system will reboot momentarily to continue the
                                                					 installation If you
                                                					 see the following virtual machine question, select Yes , and then click OK : Figure 1. Virtual Machine Message A system
                                                					 reboot Messages
                                                					 stream down your monitor during the reboot. Some of them prompt you to press a
                                                					 key. Do
                                                   						not respond to these prompts to press a key. Application Pre Install progress bars Configure and Setup Network progress bars Note If a
                                                            						Network Connectivity Failure screen appears during the Configure and Setup
                                                            						Network process, click Review , and then click OK at the Errors screen. Follow the prompts to
                                                            						reenter the information that caused the failure. The installation continues
                                                            						when the connection information is complete. Security
                                                					 configuration A message
                                          				appears that states the installation of Cisco Finesse has completed
                                          				successfully. The installation of Cisco Finesse has completed successfully.

Cisco Finesse < version number >
< hostname > login: _ | Note | If a
                                                            						Network Connectivity Failure screen appears during the Configure and Setup
                                                            						Network process, click Review , and then click OK at the Errors screen. Follow the prompts to
                                                            						reenter the information that caused the failure. The installation continues
                                                            						when the connection information is complete. |
| Note | If a
                                                            						Network Connectivity Failure screen appears during the Configure and Setup
                                                            						Network process, click Review , and then click OK at the Errors screen. Follow the prompts to
                                                            						reenter the information that caused the failure. The installation continues
                                                            						when the connection information is complete. |

| Note | Do not use
                                                      				  Thin Provisioning or a VM snapshot when creating a VM to host Cisco Finesse.
                                                      				  The use of Thin Provisioning or snapshots can negatively impact the performance
                                                      				  of Cisco Finesse operation. |
|---|---|

| Note | Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported. |
|---|---|

| Important | DNS client
                                                      				  configuration is mandatory for Cisco Finesse. Select Yes on this screen. If
                                                      				  you select No, after the installation is complete, agents cannot sign in to the desktop and you have to reinstall Finesse. |
|---|---|

| Note | If a
                                                            						Network Connectivity Failure screen appears during the Configure and Setup
                                                            						Network process, click Review , and then click OK at the Errors screen. Follow the prompts to
                                                            						reenter the information that caused the failure. The installation continues
                                                            						when the connection information is complete. |
|---|---|

| Note | Configure a
                                          			 Datastore ISO file on the virtual CD/DVD drive of the target VM to install
                                          			 Finesse. |
|---|---|

| Note | Finesse
                                          			 administration tasks can only be performed on the primary Finesse server. After
                                          			 you install the secondary server, sign in to the administration console on the
                                          			 primary server to perform administration tasks (such as configuring reason
                                          			 codes or call variable layout). |
|---|---|

| Step 1 | Follow the
                                       			 instructions in the OVA README.txt file to import and deploy the OVA, to edit
                                       			 VM settings, and to power on the VM and edit the BIOS settings in the Console. Messages
                                          				appear while the preinstallation script runs. When the preinstallation script
                                          				ends, the DVD Found screen opens. |
|---|---|
| Step 2 | Select Yes on the DVD Found screen to begin the
                                       			 verification of the media integrity and a brief hardware check. If the media
                                          				check passes, select OK to open the Product Deployment Selection screen.
                                          				Continue to Step 3. If the media
                                          				check fails, the installation terminates. |
| Step 3 | The Product Deployment Selection screen states that the Cisco Finesse product suite will be installed. This screen has only one option: OK . Select OK to open the Proceed with Install screen. |
| Step 4 | The Proceed
                                       			 with Install screen shows the version of the product that is currently
                                       			 installed (if any) and the version of the product for this ISO. For the initial
                                       			 installation, the version currently installed shows NONE. Select Yes on the Proceed with Install screen to open the
                                          				Platform Installation Wizard screen. |
| Step 5 | On the
                                       			 Platform Installation Wizard screen, select Proceed to open the Basic Install screen. |
| Step 6 | Select Continue on the Basic Install screen to open the
                                       			 Basic Install wizard. The Basic
                                          				Install wizard presents a series of screens that present questions and options
                                          				pertinent to the platform and the setup configuration. Help is available for
                                          				each wizard screen. The first
                                          				Basic Install wizard screen is Timezone Configuration. |
| Step 7 | In the
                                       			 Timezone Configuration screen: Use the up
                                             				  and down arrows to locate the local time zone that most closely matches your
                                             				  server location. You can also type the initial character of the time zone to
                                             				  move to that item in the list. The Timezone field is based on country and city
                                             				  and is mandatory. Setting it incorrectly can affect system operation. Select OK to open the Auto Negotiation Configuration
                                             				  screen. |
| Step 8 | On the Auto Negotiation Configuration screen, select Continue to use automatic negotiation for the settings of the Ethernet network interface card (NIC). The MTU Configuration screen appears. |
| Step 9 | On the MTU
                                       			 Configuration screen, select No to keep the default setting for Maximum
                                       			 Transmission Units (1500). Note Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported. Your selection
                                          				of No opens the Static Network Configuration screen. | Note | Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported. |
| Note | Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported. |
| Step 10 | On the Static Network Configuration screen, enter the static network configuration values as follows, referring to the Configuration
                                       Worksheet if necessary: Enter the Host Name . Enter the IP Address . Enter the IP Mask . Enter the GW Address . Select OK to open the Domain Name System (DNS) Client Configuration screen. |
| Step 11 | On the DNS Client
                                          				Configuration screen, select Yes to specify the DNS client information. IMPORTANT: DNS client configuration is mandatory for Cisco Finesse. Select Yes on this screen. If you select No, after the installation is complete, agents can't sign in to the desktop and you have to reinstall Finesse. |
| Step 12 | Specify your
                                       			 DNS client information as follows, referring to the Configuration Worksheet if
                                       			 necessary: Enter
                                             				  the Primary
                                                					 DNS (mandatory). Enter
                                             				  the Secondary DNS (optional). Enter
                                             				  the Domain (mandatory). Select OK to open the Administrator Login Configuration
                                             				  screen. |
| Step 13 | On the
                                       			 Administrator Login Configuration screen: Enter
                                             				  the credentials for the administrator. Select OK to open the Certificate Information screen. |
| Step 14 | On the
                                       			 Certificate Information screen: Enter
                                             				  the following data to create your Certificate Signing Request: Organization,
                                             				  Unit, Location, State, and Country. Select OK to open the First Node Configuration screen. |
| Step 15 | On the First Node Configuration screen, select No to indicate that you’re configuring the second node. A warning message appears that indicates you must first configure the server on the first node before you can proceed. If
                                          you already configured the first node, select OK . |
| Step 16 | On the
                                       			 Network Connectivity Test Configuration screen, select No to proceed with the installation after
                                       			 connectivity is verified. |
| Step 17 | On the First
                                       			 Node Configuration screen, specify the information about the first node as
                                       			 follows: Enter
                                             				  the Host
                                                					 Name of the primary Finesse server. Enter
                                             				  the IP
                                                					 Address of the primary Finesse server. Enter
                                             				  the Security
                                                					 Password of the primary Finesse server. Confirm
                                             				  the Security
                                                					 Password . |
| Step 18 | Select OK to open the Platform Configuration Confirmation
                                       			 screen. |
| Step 19 | On the
                                       			 Platform Configuration Confirmation screen, select OK . The
                                          				installation begins. The
                                          				installation can take up to an hour to complete and can run unattended for most
                                          				of that time. A message
                                          				appears that states the installation of Cisco Finesse has completed
                                          				successfully. The installation of Cisco Finesse has completed successfully.

Cisco Finesse < version number >
< hostname > login: _ |

| Note | Finesse
                                                      				  supports the default setting of 1500 for MTU only. No other value is supported. |
|---|---|

| Note | It can take
                                          			 10–20 minutes to establish replication fully between the two nodes. To access platform-specific applications like Disaster Recovery System, Cisco Unified Serviceability, and Cisco Unified Operating
                                          System Administration, use the following URL, https:// FQDN of Finesse server :8443. |
|---|---|

| If | Then |
|---|---|
| The
                                          						installation fails. | If the
                                          						installation fails, a screen appears that asks if you want to copy diagnostic
                                          						information to a device. In this
                                          						situation, you must reinstall from the beginning, but first you must attach a
                                          						serial port to the VM. Then, you dump the install logs into the serial port of
                                          						the VM. |