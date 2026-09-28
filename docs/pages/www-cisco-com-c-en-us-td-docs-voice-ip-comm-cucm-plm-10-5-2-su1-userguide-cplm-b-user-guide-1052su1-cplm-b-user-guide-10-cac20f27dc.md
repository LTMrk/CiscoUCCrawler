---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-2-su1-userguide-cplm-b-user-guide-1052su1-cplm-b-user-guide-10-cac20f27dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_2_SU1/userguide/cplm_b_user-guide-1052su1/cplm_b_user-guide-1052su1_chapter_01.html
retrieved_at: 2026-09-08T05:01:14.976607+00:00
---

Cisco Prime License Manager User Guide, Release 10.5(2)SU1a

# Cisco Prime License Manager User Guide, Release 10.5(2)SU1a

Updated: September 27, 2017

Chapter: Installation and Upgrade

## Chapter: Installation and Upgrade

# Installation and Upgrade

## Before You Begin

This section
		  describes how to install Cisco Prime License Manager on a virtual machine. You
		  install the operating system and application by running one installation
		  program.

System requirements for
			 installation

As defined in
		  the OVA that should be used to install Cisco Prime License Manager, the
		  following are the server requirements:

The Cisco Prime
		  License Manager OVA image is available for download at the Software Download
		  Center, http:/​/​software.cisco.com , under Downloads Home
			 > Products > Cloud and Systems Management > Collaboration and Unified
			 Communications Management > Cisco Prime License Manager > Cisco Prime
			 License Manager 10.5 .

## Pre-Installation
	 Tasks for Cisco Prime License Manager

Perform all
		  pre-installation tasks to ensure that you can successfully install Cisco Prime
		  License Manager.

## Frequently Asked
	 Questions About the Installation

The following
		  section contains commonly asked questions and responses. Review this section
		  carefully before you begin the installation.

### How Much Time
		  Does the Installation Require?

The entire Cisco
		  Prime License Manager installation process, excluding pre- and
		  post-installation tasks, takes approximately 30 minutes.

### What Usernames
		  and Passwords Do I Need to Specify?

During the
		  installation, you must specify the following usernames and passwords:

OS
				Administrator account username and password

Security
				password

Cisco Prime
				License Manager application account username and password

Use the OS Administrator account username and password to log into the Command Line Interface. Use the Cisco Prime License Manager application account username and password to log into the Cisco Prime
				License Manager GUI interface.

You can change the
		  Administrator account password or add a new Administrator account by using the
		  command line interface. For more information, see the Command Line Interface Guide for Cisco Unified Communications Solutions .

### What is a
		  Strong Password?

The installation wizard checks to ensure that usernames and passwords configured during installation follow these guidelines:

Username—A username must start with an
				alphabetic character and can contain alphanumeric characters, hyphens, and
				underscores.

Password—A password must be at least six
				characters long and can contain alphanumeric characters, hyphens, and
				underscores.

In addition to the above requirements, we recommend that you create a strong password:

Mix uppercase
				and lowercase letters.

Mix letters
				and numbers.

Include
				hyphens and underscores.

Remember that
				longer passwords are stronger and more secure than shorter ones.

### Can I Install
		  Other Software on the Virtual Machine?

You cannot install
		  or use unapproved third-party software applications. The system can upload and
		  process only software that is Cisco approved.

Approved software
		  installations and upgrades can be performed using the CLI.

## Port
	 Requirements

The following
		  table provides a list of ports used by Cisco Prime License Manager. If you wish to use automatic license fulfillment, Cisco Prime License Manager should be allowed direct outbound access to the Internet.

Browser
						HTTP

TCP

80/8080, 443/8443

N/A

SSH/SFTP

TCP

22

N/A

Ephemeral port ranges for clients initiating connections

TCP,
						UDP

32768-61000

N/A

DNS
						name resolution

TCP,
						UDP

N/A

53

To
						connect to Product instances and to the Cisco licensing portal for e-Fulfillment

TCP

N/A

80,
						8080, 443, 8443 (HTTP and HTTPS)

DRS

TCP

N/A

22
						(SSH/SFTP)

DHCP
						client

UDP

N/A

67

NTP
						client

TCP,
						UDP

N/A

123

## Gather Information
	 for Installation

Use the following
		  table to collect information that is pertinent to your system and network
		  configuration.

Time Zone

This
					 field specifies the local time zone and offset from Greenwich Mean Time (GMT).

Select
					 the time zone that most closely matches the location of your machine.

Yes, you
					 can change the entry after installation by using the following CLI command:

set timezone

To view
					 the current time zone configuration, use the following CLI command:

show
						timezone config

MTU Size

The
					 maximum transmission unit (MTU) represents the largest packet, in bytes, that
					 this host will transmit on the network.

Enter
					 the MTU size in bytes for your network. If you are unsure of the MTU setting
					 for your network, use the default value.

Default
					 specifies 1500 bytes.

Yes, you
					 can change the entry after installation by using the following CLI command:

set
						network mtu

DHCP

Cisco
					 Prime License Manager requires a static IP address. As a result, we recommend
					 that you select No for the DHCP option and then enter a hostname, IP address, IP mask, and
					 gateway.

No, you
					 should not change the entry after installation.

Hostname

Enter a
					 hostname that is unique to your server.

The
					 hostname can comprise up to 32 characters and can contain alphanumeric
					 characters and hyphens. The first character cannot be a hyphen.

Yes, you
					 can change the entry after installation.

set
						network hostname

Do not
						change your hostname while any tasks are running.

IP Mask

Enter
					 the IP subnet mask of this machine.

Yes, you
					 can change the entry after installation by using the following CLI command:

set
						network ip eth0

Gateway Address

Enter the
					 IP address of the network gateway.

If you do
					 not have a gateway, you must still set this field to 255.255.255.255. Not
					 having a gateway will prevent Cisco Prime License Manager from communication
					 outside of its subnet and will prevent the use of e-fulfillment.

Yes, you
					 can change the entry after installation by using the following CLI command:

set
						network gateway

DNS Enable

A DNS
					 server resolves a hostname into an IP address or an IP address into a hostname.

Select Yes to enable DNS. This will ensure that e-fulfillment will work properly.

No, you
					 should not change the entry after installation.

DNS Primary

Enter the
					 IP address of the DNS server that you want to specify as the primary DNS
					 server. Enter the IP address in dotted decimal format as ddd.ddd.ddd.ddd.

Yes, you
					 can change the entry after installation by using the following CLI command:

set
						network dns

To view
					 DNS and network information, use the following CLI command:

show
						network eth0 detail

DNS Secondary
						(optional)

Enter the
					 IP address of the DNS server that you want to specify as the optional secondary
					 DNS server.

Yes, you
					 can change the entry after installation by using the following CLI command:

set
						network dns

Administrator ID

This field
					 specifies the OS Administrator account username and password that you use for secure shell
					 access to the CLI on Cisco Prime License Manager.

No, you
					 cannot change the entry after installation.

OS Administrator
						Password

This
					 field specifies the password for the Administrator account, which you use for
					 secure shell access to the CLI.

You also
					 use this password with the adminsftp user. You use the adminsftp user to access
					 local backup files, upload server licenses, and so on.

For
					 guidelines relating to strong passwords, see the corresponding password
					 section.

Yes, you
					 can change the entry after installation by using the following CLI command:

set
						password user admin

Certificate Parameters

You can use this field to enter multiple organization units. To enter more than one organization unit name, separate each entry with a comma. For entries that already contain a comma, enter a backslash before the comma that is included as part of the entry.

Yes, you
					 can change the entry after installation by using the following CLI command:

set
						web-security

NTP Server

Enter
					 the hostname or IP address of one or more Network Time Protocol (NTP) servers
					 with which you want to synchronize.

You can
					 enter up to five NTP servers.

Yes, you
					 can change the entry after installation Yes, you can change the entry after
					 installation

utils
						ntp server

Security Password

Enter
					 your security password.

The
					 password must contain at least six alphanumeric characters. The password can
					 contain hyphens and underscores, but it must start with an alphanumeric
					 character.

Yes, you
					 can change the entry after installation by using the following CLI command:

set
						password user security

Cisco Prime License
						Manager Application Account Username

This
					 field specifies the Cisco Prime License Manager application account username
					 that you use to log on to Cisco Prime License Manager GUI.

Yes, you
					 can change the entry after installation by using the following CLI command:

license management change user name

Cisco Prime License
						Manager Application Password

This
					 field specifies the password for the Cisco Prime License Manager application
					 account, which you use for secure shell access to Cisco Prime License Manager
					 GUI.

Yes, you
					 can change the entry after installation by using the following CLI command:

license management change user password

## Install Cisco
	 Prime License Manager

### Install Virtual
	 Machine

Use this procedure
		  and your VMware documentation to install your virtual machine.

### Install Cisco Prime License Manager

Install virtual machine.

For a standalone installation of Cisco Prime License Manager, only static MAC addresses are supported on the virtual machine.

- Hostname

- IP Address

- IP Mask

- GW Address

Click OK . Go to Step 14 .

- Organization

- Unit

- Location

- State

- Country

### Remove Cisco Prime
	 License Manager

In a coresident
		  deployment, you have the option to remove Cisco Prime License Manager if it is
		  not being used. For example, in a Cisco Unified Communications Manager cluster,
		  Cisco Prime License Manager is installed on publisher nodes and subscriber nodes. Since the Cisco Prime License Manager only needs to be active
		  on a single node to manage the licensing of all nodes, you may choose to remove
		  Cisco Prime License Manager from the nodes where it is inactive.

A system reboot
			 is required, impacting all services relating to the server. We recommend that
			 you remove Cisco Prime License Manager during off-peak hours.

After Cisco Prime
		  License Manager has been removed, you will continue to see a link to Cisco
		  Prime License Manager upon login to the application, but if you try to access
		  Cisco Prime License Manager, you are notified of the removal along with a date
		  and time stamp.

You cannot
			 restore Cisco Prime License Manager after it has been removed.

Note that this
				command is not available if Cisco Prime License Manager has already been
				removed.

## Upgrade Software
	 Using the Cisco Prime License Manager GUI

You can upgrade software or apply a patch using a COP file. Use one of
		  the following options to upgrade software using the Cisco Prime License Manager
		  GUI:

Upgrade from a
				remote file system

Upgrade from a
				local source

- Upgrade from
	 a Remote File System

- Upgrade from a Local
	 Source

### Upgrade from
	 a Remote File System

To upgrade the
		  software from an FTP or SFTP server, use the following procedure.

Copy the application ISO file to an FTP server that is accessible from Cisco
		  Prime License Manager.

The
				Install/Upgrade Software dialog box opens.

Enter
				following information:

- IP Address/Hostname

- Username

- Password

- Directory (the path to the
				location where you placed the ISO)

- Transfer Protocol (select either FTP or SFTP from the drop-down menu)

### Upgrade from a Local
	 Source

Define the media source of the virtual machine. For example, is it an ISO file in the datastore or a physical optical drive on the client or host. Check the Connected checkbox for the VM CD/DVD drive.

## Upgrade Software
	 Using the Cisco Prime License Manager CLI

You can upgrade software or apply a patch using a COP file. To initiate an
		  upgrade from a local or remote source using CLI commands, use the following
		  procedures.

### Upgrade from a Remote File System

To upgrade the
		  software from an FTP or SFTP server, use the following procedure.
		  
		 Keep in mind that this procedure uses example software versions. For the latest software version, see the appropriate Release Notes for Cisco Prime License Manager .

You need to place
		  the ISO on a network location or remote drive that is accessible from Cisco
		  Prime License Manager prior to starting this procedure.

- Warning: Do not close this
				  window without first canceling the upgrade.

- 1) Remote Filesystem via
				  SFTP

- 2) Remote Filesystem via
				  FTP

- 3) Local
				  DVD/CD

- q) quit

- Please select an option
				  (1 - 3 or "q" ):

- Please select an option
				  (1 - 3 or "q" ): 1

- Directory:
				  /auto/ipcbu-builds2-published/ELM/10.0.0.98030-1

- Server:
				  se032c-94-61

- User Name:
				  bsmith

- Password:
				  ********

- Checking for valid
				  upgrades. Please wait...

- Available options and
				  upgrades in
				  "se032c-94-61:/auto/ipcbu-builds2-published/ELM/10.0.0.98030-1":

- 1)
				  CiscoPrimeLM_64bitLnx_ 10.5.1.11901-1.sgn.iso

- q) quit

- Accessing the file.
				  Please wait...

- Validating the
				  file...

- Downloaded 935
				  MB.

- Checksumming the
				  file...

- A system reboot is
				  required when the upgrade process completes or is canceled. This will ensure
				  services affected by the upgrade process are functioning properly.

- Downloaded:
				  CiscoPrimeLM_64bitLnx_ 10.5.1.11901-1.sgn.iso

- File version:
				   10.5.1.11901-1

- File checksum:
				  c4:13:ad:95:7b:c8:c1:01:1b:91:bb:da:8d:84:09:ea

### Upgrade from Local Source

If you do not have
		  a Cisco-provided upgrade disk, create an upgrade disk by burning the upgrade
		  file that you downloaded onto a DVD as an ISO image.

Just copying the
		  .iso file to the DVD will not work. Most commercial disk burning applications
		  can create ISO image disks.

```
admin:utils system upgrade initiate
```

```
Warning: Do not close this window without first exiting the upgrade command. Source: 1) Remote Filesystem via SFTP 2) Remote Filesystem via FTP 3) Local DVD/CD q) quit Please select an option (1 - 3 or "q" ):
```

```
Automatically switch versions if the upgrade is successful (yes/no): yes
```

```
Start installation (yes/no): yes
```

### Post-Upgrade
	 Tasks

After the upgrade,
		  perform the following tasks:

Check the
			 version number in the About box to verify that it is the expected upgraded
			 version.

Perform a
			 synchronization by selecting Product
				Instances > Synchronize Now .

Check the
			 Dashboard to verify that there are no alerts and then run a backup by selecting Administration > Backup/Restore .

### Change Hostname
	 using the Cisco Prime License Manager CLI

This procedure
		  describes how to use the CLI to change the IP address or hostname for the Cisco
		  Prime License Manager.

Do not change both the IP address and the
			 hostname at the same time.

The forward
				and reverse records (for example, A record and PTR record) for the new IP
				address and host name.

The DNS is
				reachable and working.

```
admin: utils diagnose module validate_network
Log file: /var/log/active/platform/log/diag1.log

Starting diagnostic test(s)
===========================
test - validate_network    : Passed                      

Diagnostics Completed
admin:
```

```
admin:set network hostname 

WARNING: To avoid license synchronization failures, delete the 
         product instance from the Cisco Prime License Manager 
         managing this server's licenses before changing network
         settings. You will have to re-add the product instance
         after the network settings have been changed.

Continue (y/n)?y

ctrl-c: To quit the input.

         ***   W A R N I N G   ***
Do not close this window without first canceling the command.

This command will automatically restart system services.
The command should not be issued during normal operating 
hours.

=======================================================
 Note: Please verify that the new hostname is a unique 
       name across the cluster and, if DNS services are 
       utilized, any DNS configuration is completed 
       before proceeding.
=======================================================

Security Warning : This operation will regenerate
       all CUCM Certificates including any third party
       signed Certificates that have been uploaded. 
    
Enter the hostname:: newHostname

Would you like to change the network ip address at this time [yes]:: 

Warning: Do not close this window until command finishes.

    

ctrl-c: To quit the input.

           ***   W A R N I N G   ***
=======================================================
 Note: Please verify that the new ip address is unique 
       across the cluster.
=======================================================
    
Enter the ip address:: 10.10.10.28
Enter the ip subnet mask:: 255.255.255.0
Enter the ip address of the gateway:: 10.10.10.1
Hostname:       newHostname				
IP Address:     10.10.10.28
IP Subnet Mask: 255.255.255.0
Gateway:        10.10.10.1

Do you want to continue [yes/no]? yes 

calling 1 of 5 component notification script: ahostname_callback.sh		
Info(0): Processnode query returned =
name       
========== 
bldr-vcm18 
updating server table from:'oldHostname', to: 'newHostname'
Rows: 1
updating database, please wait 90 seconds
updating database, please wait 60 seconds
updating database, please wait 30 seconds
Going to trigger /usr/local/cm/bin/dbl updatefiles --remote=newHostname,oldHostname 
calling 2 of 5 component notification script: clm_notify_hostname.sh		notification
Verifying update across cluster nodes...
platformConfig.xml is up-to-date: bldr-vcm21

cluster update successfull
calling 3 of 5 component notification script: drf_notify_hostname_change.py 	
calling 4 of 5 component notification script: regenerate_all_certs.sh		
calling 5 of 5 component notification script: update_idsenv.sh 		
calling 1 of 2 component notification script: ahostname_callback.sh 		
Info(0): Processnode query returned =
name 
==== 
Going to trigger /usr/local/cm/bin/dbl updatefiles --remote=10.10.10.28,10.67.142.24
calling 2 of 2 component notification script: clm_notify_hostname.sh		 
Verifying update across cluster nodes...
Shutting down interface eth0:
```

#### Post-Change Task List

After you finish changing the IP addresses or hostname, complete the tasks in the following procedure.

You must run a manual DRS backup after you change the IP address of a node, because you cannot restore a node with a DRS file that contains a different IP address or hostname. The post-change DRS file will include the new IP address or hostname.

## Install COP
	 Files

Use the following procedure to install Cisco Option files (COP) files. COP files are used to enable more functionality (for example: patches).

- IP Address/Hostname

- Username

- Password

- Directory

- Transfer Protocol

| Requirement | Details |
|---|---|
| Product | Cisco Prime License Manager |
| Version | 10.5(2) |
| CPU | 1 vCPU with 1800 Mhz reservation |
| Memory | 4 GB (RAM) with 4 GB reservation |
| Hard Drive | 1 - 50 GB disk |

| Step 1 | Review the
			 system requirements and ensure that the server you wish to host the application on has sufficient resources. |
|---|---|
| Step 2 | Create your virtual machine using the Cisco Prime
			 License Manager Virtual Server Template (OVA file) recommended for your current
			 release. |
| Step 3 | Verify that you have an NTP server accessible, since
			 an NTP server is required for VMware deployments. |
| Step 4 | Ensure that
			 the hostname and address that you plan to use for Cisco Prime License Manager
			 are registered with the name server and that both forward and reverse lookups
			 are possible. |

| Note | You can change the
		  Administrator account password or add a new Administrator account by using the
		  command line interface. For more information, see the Command Line Interface Guide for Cisco Unified Communications Solutions . |
|---|---|

| Description | Protocol | Inbound
						Port | Outbound
						Port |
|---|---|---|---|
| Browser
						HTTP | TCP | 80/8080, 443/8443 | N/A |
| SSH/SFTP | TCP | 22 | N/A |
| Ephemeral port ranges for clients initiating connections | TCP,
						UDP | 32768-61000 | N/A |
| DNS
						name resolution | TCP,
						UDP | N/A | 53 |
| To
						connect to Product instances and to the Cisco licensing portal for e-Fulfillment | TCP | N/A | 80,
						8080, 443, 8443 (HTTP and HTTPS) |
| DRS | TCP | N/A | 22
						(SSH/SFTP) |
| DHCP
						client | UDP | N/A | 67 |
| NTP
						client | TCP,
						UDP | N/A | 123 |

| Parameter | Description | Can Entry Be Changed After
				  Installation? |
|---|---|---|
| Time Zone | This
					 field specifies the local time zone and offset from Greenwich Mean Time (GMT). Select
					 the time zone that most closely matches the location of your machine. | Yes, you
					 can change the entry after installation by using the following CLI command: set timezone To view
					 the current time zone configuration, use the following CLI command: show
						timezone config |
| MTU Size | The
					 maximum transmission unit (MTU) represents the largest packet, in bytes, that
					 this host will transmit on the network. Enter
					 the MTU size in bytes for your network. If you are unsure of the MTU setting
					 for your network, use the default value. Default
					 specifies 1500 bytes. | Yes, you
					 can change the entry after installation by using the following CLI command: set
						network mtu |
| DHCP | Cisco
					 Prime License Manager requires a static IP address. As a result, we recommend
					 that you select No for the DHCP option and then enter a hostname, IP address, IP mask, and
					 gateway. | No, you
					 should not change the entry after installation. |
| Hostname | Enter a
					 hostname that is unique to your server. The
					 hostname can comprise up to 32 characters and can contain alphanumeric
					 characters and hyphens. The first character cannot be a hyphen. | Yes, you
					 can change the entry after installation. set
						network hostname Note Do not
						change your hostname while any tasks are running. | Note | Do not
						change your hostname while any tasks are running. |
| Note | Do not
						change your hostname while any tasks are running. |
| IP Mask | Enter
					 the IP subnet mask of this machine. | Yes, you
					 can change the entry after installation by using the following CLI command: set
						network ip eth0 |
| Gateway Address | Enter the
					 IP address of the network gateway. If you do
					 not have a gateway, you must still set this field to 255.255.255.255. Not
					 having a gateway will prevent Cisco Prime License Manager from communication
					 outside of its subnet and will prevent the use of e-fulfillment. | Yes, you
					 can change the entry after installation by using the following CLI command: set
						network gateway |
| DNS Enable | A DNS
					 server resolves a hostname into an IP address or an IP address into a hostname. Select Yes to enable DNS. This will ensure that e-fulfillment will work properly. | No, you
					 should not change the entry after installation. |
| DNS Primary | Enter the
					 IP address of the DNS server that you want to specify as the primary DNS
					 server. Enter the IP address in dotted decimal format as ddd.ddd.ddd.ddd. | Yes, you
					 can change the entry after installation by using the following CLI command: set
						network dns To view
					 DNS and network information, use the following CLI command: show
						network eth0 detail |
| DNS Secondary
						(optional) | Enter the
					 IP address of the DNS server that you want to specify as the optional secondary
					 DNS server. | Yes, you
					 can change the entry after installation by using the following CLI command: set
						network dns |
| Administrator ID | This field
					 specifies the OS Administrator account username and password that you use for secure shell
					 access to the CLI on Cisco Prime License Manager. | No, you
					 cannot change the entry after installation. Note After
						installation, you can create additional Administrator accounts, but you cannot
						change the original Administrator account username. | Note | After
						installation, you can create additional Administrator accounts, but you cannot
						change the original Administrator account username. |
| Note | After
						installation, you can create additional Administrator accounts, but you cannot
						change the original Administrator account username. |
| OS Administrator
						Password | This
					 field specifies the password for the Administrator account, which you use for
					 secure shell access to the CLI. You also
					 use this password with the adminsftp user. You use the adminsftp user to access
					 local backup files, upload server licenses, and so on. For
					 guidelines relating to strong passwords, see the corresponding password
					 section. | Yes, you
					 can change the entry after installation by using the following CLI command: set
						password user admin |
| Certificate Parameters | From the
					 list, select the appropriate organization, unit, location, and state for your
					 installation. Note You can use this field to enter multiple organization units. To enter more than one organization unit name, separate each entry with a comma. For entries that already contain a comma, enter a backslash before the comma that is included as part of the entry. | Note | You can use this field to enter multiple organization units. To enter more than one organization unit name, separate each entry with a comma. For entries that already contain a comma, enter a backslash before the comma that is included as part of the entry. | Yes, you
					 can change the entry after installation by using the following CLI command: set
						web-security |
| Note | You can use this field to enter multiple organization units. To enter more than one organization unit name, separate each entry with a comma. For entries that already contain a comma, enter a backslash before the comma that is included as part of the entry. |
| NTP Server | Enter
					 the hostname or IP address of one or more Network Time Protocol (NTP) servers
					 with which you want to synchronize. You can
					 enter up to five NTP servers. Note To
						avoid potential compatibility, accuracy, and network jitter problems, the
						external NTP servers that you specify for the primary node can be NTP v4
						(version 4). If you are using IPv6 addressing, external NTP servers must be NTP
						v4. | Note | To
						avoid potential compatibility, accuracy, and network jitter problems, the
						external NTP servers that you specify for the primary node can be NTP v4
						(version 4). If you are using IPv6 addressing, external NTP servers must be NTP
						v4. | Yes, you
					 can change the entry after installation Yes, you can change the entry after
					 installation utils
						ntp server |
| Note | To
						avoid potential compatibility, accuracy, and network jitter problems, the
						external NTP servers that you specify for the primary node can be NTP v4
						(version 4). If you are using IPv6 addressing, external NTP servers must be NTP
						v4. |
| Security Password | Enter
					 your security password. The
					 password must contain at least six alphanumeric characters. The password can
					 contain hyphens and underscores, but it must start with an alphanumeric
					 character. | Yes, you
					 can change the entry after installation by using the following CLI command: set
						password user security |
| Cisco Prime License
						Manager Application Account Username | This
					 field specifies the Cisco Prime License Manager application account username
					 that you use to log on to Cisco Prime License Manager GUI. | Yes, you
					 can change the entry after installation by using the following CLI command: license management change user name |
| Cisco Prime License
						Manager Application Password | This
					 field specifies the password for the Cisco Prime License Manager application
					 account, which you use for secure shell access to Cisco Prime License Manager
					 GUI. | Yes, you
					 can change the entry after installation by using the following CLI command: license management change user password |

| Note | Do not
						change your hostname while any tasks are running. |
|---|---|

| Note | After
						installation, you can create additional Administrator accounts, but you cannot
						change the original Administrator account username. |
|---|---|

| Note | You can use this field to enter multiple organization units. To enter more than one organization unit name, separate each entry with a comma. For entries that already contain a comma, enter a backslash before the comma that is included as part of the entry. |
|---|---|

| Note | To
						avoid potential compatibility, accuracy, and network jitter problems, the
						external NTP servers that you specify for the primary node can be NTP v4
						(version 4). If you are using IPv6 addressing, external NTP servers must be NTP
						v4. |
|---|---|

| Step 1 | Access the Software Download Center and download the Cisco Prime License
			 Manager OVA template for your desired release: Downloads
				  Home > Products > Cloud and Systems
				  Management > Collaboration and Unified Communications
				  Management > Cisco Prime License Manager . |
|---|---|
| Step 2 | From the
			 vCenter or vSphere Client, open the console of your newly downloaded virtual machine
			 template. |
| Step 3 | From the
			 vCenter or vSphere Client, select File >
				Deploy OVF Template . |
| Step 4 | Follow the Deploy
				OVF Template wizard to create the Cisco Prime License Manager
			 virtual machine After
			 the installation is complete, the newly installed virtual machine appears in
			 the selected location within the vCenter or vSphere Client. |

| Step 1 | Download the ISO installation file from Cisco electronic software delivery or locate the DVD provided with your order. Copy the ISO image to your host data store. |
|---|---|
| Step 2 | Using the vCenter or vSphere Client, select Edit virtual machine settings > Network adapter 1 > MAC Address. |
| Step 3 | Select the Manual option and enter a unique MAC address. For a standalone installation of Cisco Prime License Manager, only static MAC addresses are supported on the virtual machine. |
| Step 4 | Edit CD/DVD drive. Select Connect at power-on and select the ISO installation file from where it was saved to the data store or Host Device if using a physical DVD. |
| Step 5 | From the vCenter or vSphere Client, open the console of your virtual machine. |
| Step 6 | Power on the virtual machine. The installation begins automatically. |
| Step 7 | If you are using an ISO file, click Skip on the Disc Found screen to skip testing the media before installation. Otherwise, select the OK tab and press Enter to initiate testing of the media before installation. The Media Found screen appears with the following message: "Found local installation media". |
| Step 8 | The Product Deployment Selection screen appears. Select the product (there may only be one product available to select) and click OK to proceed with the installation. |
| Step 9 | Click Yes . |
| Step 10 | Select Proceed to continue with the installation. |
| Step 11 | Click Continue . |
| Step 12 | In the Timezone Configuration screen, select your time zone and click OK . |
| Step 13 | In the Auto Negotiation Configuration screen, click Continue. |
| Step 14 | When asked if you want to change the MTU size from the OS default, click No to proceed. |
| Step 15 | For the network configuration, select No to set up a static network IP address for the node. |
| Step 16 | Enter the following static network configuration values: Hostname IP Address IP Mask GW Address Click OK . Go to Step 14 . |
| Step 17 | The DNS Client Configuration screen appears. To enable DNS, click Yes , then enter your DNS client information and click OK . |
| Step 18 | Enter your Administrator login and password information. Note The Administrator login must start with an alphabetic character, be at least six characters long, and can contain alphanumeric characters, hyphens, and underscores. You will need the Administrator login to log at the command line interface. | Note | The Administrator login must start with an alphabetic character, be at least six characters long, and can contain alphanumeric characters, hyphens, and underscores. You will need the Administrator login to log at the command line interface. |
| Note | The Administrator login must start with an alphabetic character, be at least six characters long, and can contain alphanumeric characters, hyphens, and underscores. You will need the Administrator login to log at the command line interface. |
| Step 19 | The Certificate Information window displays. Enter the Certificate Information: Organization Unit Location State Country Click OK to proceed. |
| Step 20 | The Network Time Protocol Client Configuration screen appears. Enter your NTP server information. Note If the DNS client was not enabled, use an IP address. If DNS is enabled, either a hostname or IP address may be entered. Click OK to proceed. | Note | If the DNS client was not enabled, use an IP address. If DNS is enabled, either a hostname or IP address may be entered. |
| Note | If the DNS client was not enabled, use an IP address. If DNS is enabled, either a hostname or IP address may be entered. |
| Step 21 | When asked, enter your Security Password. Click OK to continue. |
| Step 22 | The Application User Configuration screen appears. Enter your username and password and log in to Cisco Prime License Manager. Click OK . |
| Step 23 | The Platform Configuration Confirmation screen appears. Click OK to complete the configuration and start the installation. The installation takes approximately 30 minutes to complete. Note If there is an installation failure, the console directs you to export the installation logs to a USB key, if necessary. | Note | If there is an installation failure, the console directs you to export the installation logs to a USB key, if necessary. |
| Note | If there is an installation failure, the console directs you to export the installation logs to a USB key, if necessary. |

| Note | The Administrator login must start with an alphabetic character, be at least six characters long, and can contain alphanumeric characters, hyphens, and underscores. You will need the Administrator login to log at the command line interface. |
|---|---|

| Note | If the DNS client was not enabled, use an IP address. If DNS is enabled, either a hostname or IP address may be entered. |
|---|---|

| Note | If there is an installation failure, the console directs you to export the installation logs to a USB key, if necessary. |
|---|---|

| Note | A system reboot
			 is required, impacting all services relating to the server. We recommend that
			 you remove Cisco Prime License Manager during off-peak hours. |
|---|---|

| Caution | You cannot
			 restore Cisco Prime License Manager after it has been removed. |
|---|---|

| Step 1 | From the
			 command line interface, enter the following command: license
				management system remove . Note that this
				command is not available if Cisco Prime License Manager has already been
				removed. |
|---|---|
| Step 2 | Confirm that
			 you would like to proceed with the removal by entering y . |
| Step 3 | Perform a
			 system reboot. |

| Step 1 | From the Cisco
			 Prime License Manager main menu, select Administration > Install/Upgrade . The
			 Install/Upgrade page opens. |
|---|---|
| Step 2 | Click Install/Upgrade
				Software . The
				Install/Upgrade Software dialog box opens. |
| Step 3 | Click Install/Upgrade from Network (this option
			 should be selected by default). Enter
				following information: IP Address/Hostname Username Password Directory (the path to the
				location where you placed the ISO) Transfer Protocol (select either FTP or SFTP from the drop-down menu) |
| Step 4 | Click Next . |
| Step 5 | All valid
			 upgrades are listed in the table. Select the required upgrade file
			 from the list. Note There
				can be multiple options listed. | Note | There
				can be multiple options listed. |
| Note | There
				can be multiple options listed. |
| Step 6 | Click Start
				Installation/Upgrade . A message appears asking you to confirm the
			 upgrade. Click Continue to begin the upgrade. Note You can leave
				  the screen up while the upgrade is in progress, as it provides feedback on the
				  progress of the upgrade, or close the browser. The upgrade proceeds even if you close the browser. The upgrade may take 45 minutes to an hour to
				  complete. | Note | You can leave
				  the screen up while the upgrade is in progress, as it provides feedback on the
				  progress of the upgrade, or close the browser. The upgrade proceeds even if you close the browser. The upgrade may take 45 minutes to an hour to
				  complete. |
| Note | You can leave
				  the screen up while the upgrade is in progress, as it provides feedback on the
				  progress of the upgrade, or close the browser. The upgrade proceeds even if you close the browser. The upgrade may take 45 minutes to an hour to
				  complete. |

| Note | There
				can be multiple options listed. |
|---|---|

| Note | You can leave
				  the screen up while the upgrade is in progress, as it provides feedback on the
				  progress of the upgrade, or close the browser. The upgrade proceeds even if you close the browser. The upgrade may take 45 minutes to an hour to
				  complete. |
|---|---|

| Step 1 | From the Cisco
			 Prime License Manager main menu, select Administration > Install/Upgrade . |
|---|---|
| Step 2 | Click Install/Upgrade
				Software . |
| Step 3 | Click Install/Upgrade from DVD/CD drive on Cisco Prime License Manager
				server . |
| Step 4 | All valid
			 upgrades are listed in the table. Select the appropriate (valid) upgrade file
			 from the list. |
| Step 5 | Click Start
				Installation/Upgrade . |
| Step 6 | Click Continue to begin the upgrade. Note You can either leave the
				  screen up while the upgrade is in progress or close your browser. Closing your browser does not impact the upgrade process. The upgrade may take 45 minutes to an hour to
				  complete. | Note | You can either leave the
				  screen up while the upgrade is in progress or close your browser. Closing your browser does not impact the upgrade process. The upgrade may take 45 minutes to an hour to
				  complete. |
| Note | You can either leave the
				  screen up while the upgrade is in progress or close your browser. Closing your browser does not impact the upgrade process. The upgrade may take 45 minutes to an hour to
				  complete. |

| Note | You can either leave the
				  screen up while the upgrade is in progress or close your browser. Closing your browser does not impact the upgrade process. The upgrade may take 45 minutes to an hour to
				  complete. |
|---|---|

| Step 1 | Enter the utils system
				upgrade initiate command, as shown in the following example. Example: utils system upgrade
				initiate The following
			 options appear: Warning: Do not close this
				  window without first canceling the upgrade. 1) Remote Filesystem via
				  SFTP 2) Remote Filesystem via
				  FTP 3) Local
				  DVD/CD q) quit Please select an option
				  (1 - 3 or "q" ): |
|---|---|
| Step 2 | Select option
			 1. |
| Step 3 | Enter
			 Directory, Server, User Name, and Password information when prompted. Please select an option
				  (1 - 3 or "q" ): 1 Directory:
				  /auto/ipcbu-builds2-published/ELM/10.0.0.98030-1 Server:
				  se032c-94-61 User Name:
				  bsmith Password:
				  ******** Checking for valid
				  upgrades. Please wait... |
| Step 4 | Enter SMTP
				Host Server (optional) to receive email notification once upgrade
			 is complete. The
			 following options appear: Available options and
				  upgrades in
				  "se032c-94-61:/auto/ipcbu-builds2-published/ELM/10.0.0.98030-1": 1)
				  CiscoPrimeLM_64bitLnx_ 10.5.1.11901-1.sgn.iso q) quit |
| Step 5 | Select option 1 to download upgrade file. The following
			 messages appear: Accessing the file.
				  Please wait... Validating the
				  file... Downloaded 935
				  MB. Checksumming the
				  file... A system reboot is
				  required when the upgrade process completes or is canceled. This will ensure
				  services affected by the upgrade process are functioning properly. Downloaded:
				  CiscoPrimeLM_64bitLnx_ 10.5.1.11901-1.sgn.iso File version:
				   10.5.1.11901-1 File checksum:
				  c4:13:ad:95:7b:c8:c1:01:1b:91:bb:da:8d:84:09:ea |
| Step 6 | Enter No when
			 asked to automatically switch versions if the upgrade is successful. Automatically switch
				versions if the upgrade is successful (yes/no): no |
| Step 7 | Enter Yes to
			 start installation. Start
				installation (yes/no): yes |

| Step 1 | Insert the new
			 DVD into the disc drive on the local server that is to be upgraded. |
|---|---|
| Step 2 | Enter the utils system
				upgrade initiate command, as shown in the following example. Example: admin:utils system upgrade initiate The
			 following options appear: Warning: Do not close this window without first exiting the upgrade command. Source: 1) Remote Filesystem via SFTP 2) Remote Filesystem via FTP 3) Local DVD/CD q) quit Please select an option (1 - 3 or "q" ): |
| Step 3 | Select option
			 3. 1)
				CiscoPrimeLM_64bitLnx_ 10.5.1.11901-1.sgn.iso q) quit |
| Step 4 | Select option 1 to download upgrade file. Accessing the file. Please
				wait... Checksumming the
				file... Validating the
				file... A system reboot is required
				when the upgrade process completes or is canceled. This will ensure services
				affected by the upgrade process are functioning properly. Downloaded:
				CiscoPrimeLM_64bitLnx_ 10.5.1.11901-1.sgn.iso File version:
				 10.5.1.11901-1 File checksum:
				c4:13:ad:95:7b:c8:c1:01:1b:91:bb:da:8d:84:09:ea |
| Step 5 | Enter yes to automatically switch versions if the upgrade
			 was successful. Automatically switch versions if the upgrade is successful (yes/no): yes |
| Step 6 | Enter yes to start installation. Start installation (yes/no): yes |

| Note | Do not change both the IP address and the
			 hostname at the same time. |
|---|---|

| Step 1 | To check
			 network connectivity and DNS server configuration, enter the utils
				diagnose CLI command as shown in the following example: admin: utils diagnose module validate_network
Log file: /var/log/active/platform/log/diag1.log

Starting diagnostic test(s)
===========================
test - validate_network    : Passed                      

Diagnostics Completed
admin: |
|---|---|
| Step 2 | Run a manual
			 backup and ensure that all active services are backed up successfully. |
| Step 3 | Enter the set
				network hostname CLI command and follow the prompts to change the
			 hostname, IP address, or default gateway. See the following example: admin:set network hostname 

WARNING: To avoid license synchronization failures, delete the 
         product instance from the Cisco Prime License Manager 
         managing this server's licenses before changing network
         settings. You will have to re-add the product instance
         after the network settings have been changed.

Continue (y/n)?y

ctrl-c: To quit the input.

         ***   W A R N I N G   ***
Do not close this window without first canceling the command.

This command will automatically restart system services.
The command should not be issued during normal operating 
hours.

=======================================================
 Note: Please verify that the new hostname is a unique 
       name across the cluster and, if DNS services are 
       utilized, any DNS configuration is completed 
       before proceeding.
=======================================================

Security Warning : This operation will regenerate
       all CUCM Certificates including any third party
       signed Certificates that have been uploaded. 
    
Enter the hostname:: newHostname

Would you like to change the network ip address at this time [yes]:: 

Warning: Do not close this window until command finishes.

    

ctrl-c: To quit the input.

           ***   W A R N I N G   ***
=======================================================
 Note: Please verify that the new ip address is unique 
       across the cluster.
=======================================================
    
Enter the ip address:: 10.10.10.28
Enter the ip subnet mask:: 255.255.255.0
Enter the ip address of the gateway:: 10.10.10.1
Hostname:       newHostname				
IP Address:     10.10.10.28
IP Subnet Mask: 255.255.255.0
Gateway:        10.10.10.1

Do you want to continue [yes/no]? yes 

calling 1 of 5 component notification script: ahostname_callback.sh		
Info(0): Processnode query returned =
name       
========== 
bldr-vcm18 
updating server table from:'oldHostname', to: 'newHostname'
Rows: 1
updating database, please wait 90 seconds
updating database, please wait 60 seconds
updating database, please wait 30 seconds
Going to trigger /usr/local/cm/bin/dbl updatefiles --remote=newHostname,oldHostname 
calling 2 of 5 component notification script: clm_notify_hostname.sh		notification
Verifying update across cluster nodes...
platformConfig.xml is up-to-date: bldr-vcm21

cluster update successfull
calling 3 of 5 component notification script: drf_notify_hostname_change.py 	
calling 4 of 5 component notification script: regenerate_all_certs.sh		
calling 5 of 5 component notification script: update_idsenv.sh 		
calling 1 of 2 component notification script: ahostname_callback.sh 		
Info(0): Processnode query returned =
name 
==== 
Going to trigger /usr/local/cm/bin/dbl updatefiles --remote=10.10.10.28,10.67.142.24
calling 2 of 2 component notification script: clm_notify_hostname.sh		 
Verifying update across cluster nodes...
Shutting down interface eth0: |
| Step 4 | Complete the Post-Change Task List . |

| Step 1 | Run a backup and ensure that all active services back up successfully. For more information, see the Backup/Restore section of the Administration chapter. Note You must run a manual DRS backup after you change the IP address of a node, because you cannot restore a node with a DRS file that contains a different IP address or hostname. The post-change DRS file will include the new IP address or hostname. | Note | You must run a manual DRS backup after you change the IP address of a node, because you cannot restore a node with a DRS file that contains a different IP address or hostname. The post-change DRS file will include the new IP address or hostname. |
|---|---|---|---|
| Note | You must run a manual DRS backup after you change the IP address of a node, because you cannot restore a node with a DRS file that contains a different IP address or hostname. The post-change DRS file will include the new IP address or hostname. |
| Step 2 | If using the integrated DHCP server that runs on Cisco Prime License Manager, update the DHCP server. |
| Step 3 | Perform manual synchronization and verify that there are no alerts in the dashboard. |

| Note | You must run a manual DRS backup after you change the IP address of a node, because you cannot restore a node with a DRS file that contains a different IP address or hostname. The post-change DRS file will include the new IP address or hostname. |
|---|---|

| Step 1 | Obtain the
			 desired COP file from the Cisco Software Download Center on Cisco.com and store
			 locally. Note To access the Software Patches site, go to http:/​/​software.cisco.com , select Upgrade and Update , then select Download Software . From the Download Software window, navigate to the desired release: Downloads Home > Products > Unified Communications > Unified Communications Management > Prime License Manager > Prime License Manager 10.5 . | Note | To access the Software Patches site, go to http:/​/​software.cisco.com , select Upgrade and Update , then select Download Software . From the Download Software window, navigate to the desired release: Downloads Home > Products > Unified Communications > Unified Communications Management > Prime License Manager > Prime License Manager 10.5 . |
|---|---|---|---|
| Note | To access the Software Patches site, go to http:/​/​software.cisco.com , select Upgrade and Update , then select Download Software . From the Download Software window, navigate to the desired release: Downloads Home > Products > Unified Communications > Unified Communications Management > Prime License Manager > Prime License Manager 10.5 . |
| Step 2 | Place the COP
			 file on an FTP or SFTP server that the server that you are upgrading can
			 access. |
| Step 3 | Log in to
			 Cisco Prime License Manager. |
| Step 4 | Select Administration > Install/Upgrade . |
| Step 5 | Click Install/Upgrade Software . |
| Step 6 | In the Specify File Location section of the Install/Upgrade Software window, enter the
			 following: IP Address/Hostname Username Password Directory Transfer Protocol |
| Step 7 | Click Next . |
| Step 8 | Select the appropriate (valid) COP file from valid COP
			 files listed and click Start
				Installation/Upgrade to begin the install. |

| Note | To access the Software Patches site, go to http:/​/​software.cisco.com , select Upgrade and Update , then select Download Software . From the Download Software window, navigate to the desired release: Downloads Home > Products > Unified Communications > Unified Communications Management > Prime License Manager > Prime License Manager 10.5 . |
|---|---|