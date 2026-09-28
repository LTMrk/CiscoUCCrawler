---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-0-1-userguide-cplm-bk-u2c0c808-00-user-guide-rel-1101-cplm-bk-u2-9af9ced66f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_0_1/userguide/CPLM_BK_U2C0C808_00_user-guide-rel-1101/CPLM_BK_U2C0C808_00_user-guide-rel-1101_chapter_0100.html
retrieved_at: 2026-09-08T05:00:45.033146+00:00
---

Cisco Prime License Manager User Guide, Release 11.0(1)

# Cisco Prime License Manager User Guide, Release 11.0(1)

Updated: September 12, 2017

Chapter: Installation

## Chapter: Installation

# Installation

## Pre-Installation
	 Tasks for Cisco Prime License Manager

Perform all
		  pre-installation tasks to ensure that you can successfully install Cisco Prime
		  License Manager.

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

## Install Virtual
	 Machine

Use this procedure
		  and your VMware documentation to install your virtual machine.

## Install Cisco Prime License Manager

Install virtual machine.

For a standalone installation of Cisco Prime License Manager, only static MAC addresses are supported on the virtual machine.

- Host Name

- IP Address

- IP Mask

- GW Address

Click OK . Go to Step 14 .

- Organization

- Unit

- Location

- State

- Country

## Remove Cisco Prime
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

| Step 1 | Download the ISO installation file from Cisco electronic software delivery or locate the DVD provided with your order. Use vCenter or vSphere Client to copy the ISO image to your host datastore. |
|---|---|
| Step 2 | Using the vCenter or vSphere Client, select Edit virtual machine settings > Network adapter 1 > MAC Address . |
| Step 3 | Select the Manual option and enter a unique MAC address. For a standalone installation of Cisco Prime License Manager, only static MAC addresses are supported on the virtual machine. |
| Step 4 | Edit CD/DVD drive 1. Select Connect at power on and select the ISO installation file from where it was saved to the datastore or Host Device if using a physical DVD. |
| Step 5 | From the vCenter or vSphere Client, open the console of your virtual machine. |
| Step 6 | Power on the virtual machine. The installation begins automatically. |
| Step 7 | If you are using an ISO file, click Skip on the Disc Found screen to skip testing the media before installation. Otherwise, select the OK tab and press Enter to initiate testing of the media before installation. The Media Found screen appears with the following message: "Found local installation media." |
| Step 8 | The Product Deployment Selection screen appears. Select the product (there may only be one product available to select) and click OK to proceed with the installation. |
| Step 9 | Click Yes . |
| Step 10 | Select Proceed to continue with the installation. |
| Step 11 | Click Continue . |
| Step 12 | In the Timezone Configuration screen, select your timezone and click OK . |
| Step 13 | In the Auto Negotiation Configuration screen, click Continue . |
| Step 14 | When asked if you want to change the MTU size from the OS default, click No to proceed. |
| Step 15 | For network configuration, select No to set up a static network IP address for the node . |
| Step 16 | Enter the following static network configuration values: Host Name IP Address IP Mask GW Address Click OK . Go to Step 14 . |
| Step 17 | The DNS Client Configuration screen appears. To enable DNS, click Yes , then enter your DNS client information and click OK . |
| Step 18 | Enter your Administrator login and password information. Note The Administrator login must start with an alphabetic character, be at least six characters long, and can contain alphanumeric characters, hyphens, and underscores. You will need the Administrator login to log into the command line interface. | Note | The Administrator login must start with an alphabetic character, be at least six characters long, and can contain alphanumeric characters, hyphens, and underscores. You will need the Administrator login to log into the command line interface. |
| Note | The Administrator login must start with an alphabetic character, be at least six characters long, and can contain alphanumeric characters, hyphens, and underscores. You will need the Administrator login to log into the command line interface. |
| Step 19 | The Certificate Information window displays. Enter the Certificate Information: Organization Unit Location State Country Click OK to proceed. |
| Step 20 | The Network Time Protocol Client Configuration screen appears. Enter your NTP server information. Note If DNS client was not enabled, use an IP address. If DNS is enabled, either a hostname or IP address may be entered. Click OK to proceed. | Note | If DNS client was not enabled, use an IP address. If DNS is enabled, either a hostname or IP address may be entered. |
| Note | If DNS client was not enabled, use an IP address. If DNS is enabled, either a hostname or IP address may be entered. |
| Step 21 | When asked, enter your Security Password. Click OK to continue. |
| Step 22 | The Application User Configuration screen appears. Enter your username and password and log into Cisco Prime License Manager. Click OK . |
| Step 23 | The Platform Configuration Confirmation screen appears. Click OK to complete the configuration and start the installation. The installation will take approximately 30  minutes to complete. Note If there is an installation failure, the console will direct you to export the installation logs to a USB key, if required. | Note | If there is an installation failure, the console will direct you to export the installation logs to a USB key, if required. |
| Note | If there is an installation failure, the console will direct you to export the installation logs to a USB key, if required. |

| Note | The Administrator login must start with an alphabetic character, be at least six characters long, and can contain alphanumeric characters, hyphens, and underscores. You will need the Administrator login to log into the command line interface. |
|---|---|

| Note | If DNS client was not enabled, use an IP address. If DNS is enabled, either a hostname or IP address may be entered. |
|---|---|

| Note | If there is an installation failure, the console will direct you to export the installation logs to a USB key, if required. |
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