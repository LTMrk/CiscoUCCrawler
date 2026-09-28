---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1-su1-english-administration-guide-cer0-b-cisco-emergency-responder-1005d33cd5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1_su1/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251SU1/cer0_b_cisco-emergency-responder-administration-guide-1251SU1_appendix_010000.html
retrieved_at: 2026-08-21T15:33:56.660133+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU1

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU1

Updated: February 1, 2024

Chapter: Cisco Unified Operating System Administration Web Interface

## Chapter: Cisco Unified Operating System Administration Web Interface

# Cisco Unified Operating System Administration Web Interface

## ServerGroup

The
                              		  ServerGroup page appears when you choose Show >
                                 			 ServerGroup .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  ServerGroup page to view information about the Emergency Responder servers in
                              		  the server group.

The
                              		  following table describes the ServerGroup page.

Field

Description

Hostname

Displays the name of the host.

IP
                                          					 Address

Displays the IP address of the host.

Alias

Displays the alias of the host

Type of Node

Displays the node type of the host.

Database Replication

Displays the name of the database which will either be a
                                          					 Publisher or Subscriber.

## Hardware
                        	 Status

The
                              		  Hardware Status page appears when you choose Show >
                                 			 Hardware .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Hardware Status page to view information about the Emergency Responder
                              		  hardware.

The
                              		  following table describes the Hardware Status page.

Field

Description

Platform Type

Model identity of the platform server

Serial Number

Displays serial number of the virtual machine.

Virtual Hardware

Shows you the status as "Configured" if the hardware is a virtual machine.

Virtual Support

Shows you the status as "Supported" if the support is on a virtual machine.

Processor Speed

Speed of the processor

CPU
                                          					 Type

Type of processor in the platform server

Memory

Total amount of memory in Mbytes

Object ID

Object ID of the platform server

OS
                                          					 Version

Operating system version running on the platform server

RAID Details

Detailed summary of the platform hardware

## Network
                        	 Configuration

The Network
                              		  Configuration page appears when you choose Show >
                                 			 Network .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Network Configuration page to view information about the network settings.

The network status
                                          			 information that displays depends on whether Network Fault Tolerance is
                                          			 enabled. When Network Fault Tolerance is enabled, Ethernet port 1 automatically
                                          			 takes over network communications if Ethernet port 0 fails. If Network Fault
                                          			 Tolerance is enabled, network status information displays for the network ports
                                          			 Ethernet 0, Ethernet 1, and Bond 0. If Network Fault Tolerance is not enabled,
                                          			 status information displays only for Ethernet 0.

The
                              		  following table describes the Network Configuration page.

Field

Description

DHCP Status

Indicates whether DHCP is enabled for Ethernet port 0.

Status

Indicates whether the port is Up or Down for Ethernet ports 0
                                          					 and 1.

IP
                                          					 Address

Shows the IP address of Ethernet port 0 (and Ethernet port 1 if
                                          					 Network Fault Tolerance (NFT) is enabled).

IP
                                          					 Mask

Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT
                                          					 is enabled).

Link Detected

Indicates whether there is an active link.

Queue Length

Displays the length of the queue.

MTU

Displays the maximum transmission unit.

MAC Address

Displays the hardware address of the port.

RX
                                          					 Stats

Displays information about received bytes and packets.

TX
                                          					 Stats

Displays information about transmitted bytes and packets.

Primary DNS

Displays the IP address of the primary domain name server.

Secondary DNS

Displays the IP address of the secondary domain name server.

Options

Displays the number of attempts and timeouts.

Domain

Displays the domain of the server.

Gateway

Displays the IP address of the network gateway on Ethernet port
                                          					 0.

## Software
                        	 Packages

The
                              		  Software Packages page appears when you choose Show >
                                 			 Software .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Software Packages page to view the software versions and installed software
                              		  options.

The
                              		  following table describes the Software Packages page.

Field

Description

Partition Versions

Displays the software version that is running on the active and
                                          					 inactive partitions.

Active Version Installed Software Options

Displays the versions of installed software options that are
                                          					 installed on the active version.

Inactive Version Installed Software Options

Displays the versions of installed software options that are
                                          					 installed on the inactive version.

Installed Software Options

Displays the cop file installed on the system.

## System
                        	 Status

The System
                              		  Status page appears when you choose Show >
                                 			 System .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  System Status page to view the status of the Emergency Responder system.

The
                              		  following table describes the System Status page.

Field

Description

Host Name

Name of the Cisco UCS host
                                          					 where the Emergency Responder system is installed.

Date

Date and
                                          					 time based on the continent and region that were specified during operating
                                          					 system installation.

Time Zone

Time zone
                                          					 that was chosen during installation.

Locale

Locale of
                                          					 the system.

Product
                                          					 Version

Operating
                                          					 system version.

Uptime

Displays
                                          					 system uptime information.

CPU

Displays the
                                          					 percentage of CPU capacity that is idle, the percentage that is running system
                                          					 processes, and the percentage that is running user processes.

Memory

Displays
                                          					 information about memory usage, including the amount of total memory, free
                                          					 memory, and used memory in kilobytes.

Disk/active

Displays the
                                          					 amount of total, free, and used disk space on the active disk.

Disk/inactive

Displays the
                                          					 amount of total, free, and used disk space on the inactive disk.

Disk/logging

Displays the
                                          					 amount of total, free, and disk space that is used for disk logging.

## IP
                        	 Preferences

The IP
                              		  Preferences page appears when you choose Show > IP
                                 			 Preferences .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the IP
                              		  Preferences page to view a list of registered ports that can be used by the
                              		  system. The following table describes the IP Preferences page.

Field

Description

Application

Name of the application using (listening on) the port.

Protocol

Protocol used on this port (TCP, UDP, and so on).

Port Number

Numeric port number.

Type

Type of traffic allowed on this port:

Public—All traffic allowed.

Translated—All traffic allowed but forwarded to a different port.

Private—Traffic only allowed from a defined set of remote servers, for example, other servers in the server group.

Translated Port

Traffic destined for this port get forwarded to the port listed
                                          					 in the Port Number column. This field applies to Translated type ports only.

Status

Status of port usage:

Enabled—In use by the application and opened by the firewall.

Disabled—Blocked by the firewall and not in use.

Description

Brief description of how the port is used.

## Ethernet
                        	 Configuration

The
                              		  Ethernet Configuration page appears when you choose Settings > IP
                                 			 > Ethernet .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Ethernet Configuration page to view or change Ethernet settings.

All Ethernet settings apply only to Eth0. You can't configure any settings for Eth1. The maximum transmission unit (MTU) on
                                          Eth0 defaults to 1500.

The
                              		  following table describes the Ethernet Configuration page.

Field

Description

DHCP

Indicates whether DHCP is enabled or disabled and allows you to
                                          					 change the DHCP setting using the pull-down menu.

Hostname

Displays the hostname of the node.

IP
                                          					 Address

Displays the IP address of the system. You can change the IP
                                          					 address by entering a new IP address in the text box.

Subnet Mask

Displays the IP subnet mask address. You can change the mask by
                                          					 entering a new subnet mask in the text box.

Default Gateway

Displays the IP address of the default network gateway. You can
                                          					 change the gateway IP address by entering a new IP address in the text box.

Save button or icon

Saves any changes made to the Ethernet Configuration page.

Caution

If you click Save , the machine reboots. Don't click Save unless you want to shut down and reboot your system.

To
                                                      						recognize any new IP addresses, both servers in the server group must be
                                                      						manually rebooted.

## Ethernet IPv6
                        	 Configuration

Use the Settings > IP > Enternet
                                    				IPv6 menu to enable and configure IPv6 on the node.

All Ethernet
                                          			 settings apply only to Eth0. You cannot configure any settings for Eth1. The
                                          			 Maximum Transmission Unit (MTU) on Eth0 defaults to 1500.

Field

Description

Enable IPv6

Check this check box to enable IPv6 on the node.

Router Advertisement

Choose one of the following IP address sources:

Router Advertisement

DHCP

Manual Entry

The three IP address sources are mutually exclusive.

Unless you specify Manual
                                                      						Entry, IPv6 Address, Prefix Length, and Default Gateway fields remain read
                                                      						only.

IPv6 Address

If you chose Manual Entry, enter the IPv6 address of the node.
                                          					 For example, fd6:2:6:96:21e:bff:fecc:2e3a.

Prefix
                                          					 Length

If you
                                          					 chose Manual Entry, enter the prefix length. For example, 64.

Default
                                          					 Gateway

If you
                                          					 chose Manual Entry, enter the default gateway. For example,
                                          					 fe80::3ece:73ff:fea9:c641.

Update with Reboot

If you want the system to reboot immediately after you click
                                          					 Save, check this check box. If you want to reboot later, leave the check box
                                          					 blank.

If you
                                                      						check the Update with Reboot check box, the system reboots after you click
                                                      						Save. For the IPv6 settings to take effect, reboot the system.

## Publisher
                        	 Settings

The
                              		  Publisher Settings page appears when you choose Settings > IP
                                 			 > Publisher.

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Publisher Settings page to view or change the Publisher hostname or IP address.

You can only view
                                          			 and change the publisher hostname IP address only on the Emergency Responder
                                          			 Subscriber, not on the Emergency Responder publisher itself. Changing these
                                          			 fields must be followed by an immediate reboot of the Subscriber.

Field

Description

Hostname

Displays the hostnames of the Emergency Responder Publisher for
                                          					 this Subscriber. To change the hostname, enter the new hostname in the text
                                          					 box, and click Save .

IP
                                          					 Address

Displays the IP address of the Emergency Responder Publisher for
                                          					 this Subscriber. To change the IP address, enter the IP address in the text
                                          					 box, and click Save .

Save button or icon

Saves the information in the Publisher Configuration Settings
                                          					 page.

## NTP Server
                        	 List

The NTP
                              		  Server List page appears when you choose Settings > NTP
                                 			 Servers .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  NTP Server List page to add, modify, or delete an NTP server. You can only
                              		  configure the NTP server settings on the Publisher.

Ensure that the
                                          			 external NTP server is stratum 9 or higher (1 to 9).

Any change you
                                          			 make to the NTP servers can take up to five minutes to complete. Whenever you
                                          			 make any change to the NTP servers, you must refresh the page to display the
                                          			 correct status.

Caution

If you add,
                                          			 modify, or delete an NTP server, you must reboot both the Publisher and the
                                          			 Subscriber.

The
                              		  following table describes the NTP Server List page.

Field

Description

Displays how many configured NTP server were found.

Hostname or IP Address field

Displays the hostnames or IP addresses of the configured NTP
                                          					 servers. To change a hostname or IP address, click it, enter the new hostname
                                          					 or IP address, and click Save .

Add New button or icon

Adds a new NTP server. After you click Add
                                             						New , enter the hostname of IP address of the new NTP server and click Save .

Select All button or icon

Selects all NTP servers listed. When you click this button or
                                          					 icon, a check mark appears in the boxes to the left of each NTP hostname or IP
                                          					 address and to the left of the Hostname or IP Address column heading.

The Select
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers.

Clear All button or icon

Deselects all NTP servers listed. When you click this button or
                                          					 icon, all check marks disappear.

The Clear
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers.

Delete Selected button or icon

Deletes the selected NTP server. To delete an NTP server, you
                                          					 must first select it from the list of NTP servers. Click the box to the left of
                                          					 the NTP server name to select it. To select all listed NTP servers, click the
                                          					 box to the left of the Hostname or IP Address column heading or click Select
                                             						All .

The Delete
                                                      						Selected button or icon is only visible if you have previously configured one
                                                      						or more NTP servers.

The
                              		  following table describes the NTP Server Configuration page.

Field

Description

Displays how many configured NTP server were found.

Hostname or IP Address field

Displays the hostnames or IP addresses of the configured NTP
                                          					 servers. To change a hostname or IP address, click it, enter the new hostname
                                          					 or IP address, and click Save .

Save button or icon

Saves the information about the new NTP server.

## SMTP
                        	 Settings

The SMTP
                              		  Settings page appears when you choose Settings >
                                 			 SMTP .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  SMTP Settings page to manually configure the SMTP host.

The
                              		  following table describes the SMTP Settings page.

Field

Description

Displays the status of the SMTP Settings page.

Hostname or IP Address

Enter the hostname or IP address of the SMTP server in the text
                                          					 box.

Host Status

Displays the status of the SMTP host server.

Save button or icon

Saves changes made to the SMTP Settings page.

## Time
                        	 Settings

The Time
                              		  Settings page appears when you choose Settings >
                                 			 Time .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Time Settings page to manually configure the server time.

Before you can
                                          			 manually configure the server time, you must delete any NTP servers that you
                                          			 have configured. See NTP Server List for more information.

Caution

If you change the
                                          			 server time, you must reboot both the Publisher and the Subscriber.

The
                              		  following table describes the Time Settings page.

Field

Description

Date

Allows you to set the month, day, year, hours, minutes, and
                                          					 seconds using the pull-down menus.

Save button or icon

Saves changes made to the Time Settings page.

## Version
                        	 Settings

The
                              		  Version Settings page appears when you choose Settings >
                                 			 Version .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Version Settings page to restart or shutdown the system and to switch software
                              		  versions.

You must have a
                                          			 different software version installed on the inactive partition to switch
                                          			 versions.

Caution

Initiating this
                                          			 action causes the system to restart and become temporarily unavailable.

The
                              		  following table describes the Version Settings page.

Field

Description

Displays the current status.

Active Version

Displays the version running on the active partition.

Inactive Version

Display the version on the inactive partition.

Restart button or icon

Restarts the system.

Shutdown button or icon

Shuts down the system.

Switch Versions button or icon

Actives the software version on the inactive partition.

The Switch
                                                      						Versions button or icon is only visible if there is a software version
                                                      						installed on the inactive partition.

## Certificate Management

The
                              		  Certificate List page appears when you choose Security >
                                 			 Certificate Management .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the Certificate Management page to do the following:

Search for existing certificates

Generate a new certificates

Upload a certificate

Upload a CTL

Generate a CSR

The following table describes the Certificate List page.

Field

Description

Displays the current status.

Find certificate list where

Enter search criteria for the certificate lists you want to find.

To find all certificate lists by file name, select File Name from the pull-down menu and click Find without entering any criteria.

To find all certificate lists by certificate name, select Certificate Name from the pull-down menu and click Find without entering any criteria.

To narrow your search:

Select the search relationship (begins with, contains, and so on) from the pull-down menu, and enter the search string in
                                                the text box.

To search on a combination of fields, click the Plus icon (+) to add additional search parameters. Click the Minus icon ( – ) to remove search parameters. Click Clear Filter to remove all additional search parameters.

Use the Rows per Page pull-down menu to select how many rows are displayed per page.

When you have entered all of the search parameters, click Find .

If the search finds existing certificates, the information about the certificates (File Name, Certificate Name, and Certificate
                                          Type) displays in the Certificate List.

Click the File Name link to display the Certificate Configuration page. See Table 8 for information about the Certificate Configuration Page.

Generate New button or icon

Allows you to generate a new certificate. When you click Generate New , the Generate Certificate page appears. See Table 2 for a description of the Generate Certificate page.

Upload Certificate button or icon

Allows you to upload a certificate from a remote server. When you click Upload Certificate , the Upload Certificate page appears. See Table 3 for a description of the Upload Certificate page.

Upload CTL button or icon

Allows you to upload a Certificate Trust List (CTL) from a remote server. When you click Upload CTL , the Upload Certificate Trust List page appears. See Table 4 for a description of the Upload Certificate Trust List page.

Generate CSR button or icon

Allows you to generate a new Certificate Signing Request (CSR). When you click Generate CSR , the Generate Certificate Signing Request page appears. See Table 6 for a description of the Generate New page.

Download CSR button or icon

Allows you to download a CSR. When you click Download CSR , the Download Certificate Signing Request page appears. See Table 7 for a description of the Download Certificate Signing Request page.

The following table describes the Generate New Self-signed Certificate page.

Field

Description

Displays the current status of the Generate New Self-signed Certificate page.

Certificate Purpose

Choose the required option from the drop-down list. When you choose any of the following options, the Key Type field is automatically set to RSA .

tomcat

ipsec

When you choose any of the following options, the Key Type field is automatically set to EC (Elliptical Curve).

tomcat-ECDSA

Distribution

Choose a Emergency Responder server from the drop-down list.

Common

Displays the name of the Emergency Responder server that you have chosen using the Distribution drop-down list.

Auto-populated Domains

Appears only if you have chosen any of the following options using the Certificate Purpose drop-down list.

tomcat-ECDSA

Key Type

This field lists the type of keys used for encryption and decryption of the public-private key pair. Emergency Responder supports
                                          EC and RSA key types.

Key Length

Allows you to choose 1024, 2048, 3072, or 4096 from the drop-down list.

If the key length value is 1024, 2048, 3072, or 4096, the supported hash algorithm is SHA256.

If the key length value is 256, 384, or 521, the supported hash algorithms are SHA384 or SHA512.

Hash Algorithm

Choose a value that is greater than or equal to the key length from the drop-down list:

The values in the Hash Algorithm drop-down list changes based on the value you have chosen in the Key Length field.

If your system is running in FIPS mode, it is mandatory to choose SHA256 as the hashing algorithm.

Generate button

Generates a new certificate. You must first select a Certificate Name from the pull-down menu.

Close button

Closes the Generate New Self-signed Certificate page.

The following table describes the Upload Certificate page.

Field

Description

Displays the current status of the Upload Certificate page.

Certificate Name

Use the pull-down menu to select the name of the certificate to upload.

Root Certificate

Enter the name of the root certificate.

Upload File

Use the Browse button to select the file to be uploaded.

Upload File button or icon

Uploads the certificate file specified in the Upload Certificate section.

Close button or icon

Closes the Update Certificate page.

The following table describes the Upload CTL page.

Field

Description

Displays the current status of the Upload CTL page.

Certificate Name

Use the pull-down menu to select the name of the CTL file to upload.

Root Certificate

Enter the name of the root certificate.

Upload File

Use the Browse button to select the file to be uploaded.

Upload File button or icon

Uploads the certificate file specified in the Upload Certificate Trust List section.

Close button or icon

Closes the Update CTL page.

The following table lists the Certificate Signing Request Fields.

Field

Description

Certificate Purpose

From the drop-down list, select a value:

Tomcat

Tomcat-ECDSA

IPSec

Distribution

Select a Emergency Responder server.

```
Tomcat-ECDSA common name: <host-name>-EC-ms.<domain>
```

Common Name / Common Name_SerialNumber

Displays the common name or the common name appended with the serial number of the certificate. Common Name or Common Name_SerialNumber
                                          is the file name of the certificate.

Shows the name of the Unified Communications Manager application that you selected in the Distribution field by default.

Auto-populated Domains

This field appears in Subject Alternate Names (SANs) section. It lists the host names that are to be protected by a single
                                          certificate.

Parent Domain

This field appears in Subject Alternate Names (SANs) section. It shows the default domain name. You can modify the domain
                                          name, if required.

Key Type

This field identifies the type of key used for encryption and decryption for the public-private key pair.

Key Length

From the Key Length drop-down list, select one of the values.

Depending on the key length, the CSR request limits the hash algorithm choices. By having the limited hash algorithm choices,
                                          you can use a hash algorithm strength that is greater than or equal to the key length strength. For example, for a key length
                                          of 256, the supported hash algorithms are SHA256, SHA384, or SHA512. Similarly, for the key length of 384, the supported hash
                                          algorithms are SHA384 or SHA512.

Certificates with a key length value of 3072 or 4096 can only be selected for RSA certificates. These options aren't available for ECDSA certificates.

Hash Algorithm

Select a value from the Hash Algorithm drop-down list to have stronger hash algorithm as the elliptical curve key length. From the Hash Algorithm drop-down list, select one of the values.

The values for the Hash Algorithm field change based on the value you select in the Key Length field.

If your system is running on FIPS mode, it's mandatory that you select SHA256 as the hashing algorithm.

The following table describes the Generate CSR page.

Field

Description

Displays the current status of the Generate CSR page.

Certificate Name

Use the pull-down menu to select the name of the CTL file to generate.

Generate CSR button or icon

Generates a new CSR.

Close button or icon

Close the Generate CSR page.

The following table describes the Download CSR page.

Field

Description

Displays the current status of the Download CSR page.

Certificate Name

Use the pull-down menu to select the name of the CTL file to download.

Download CSR button or icon

Downloads the CSR specified in the Download Certificate Signing Request section.

Close button or icon

Closes the Download CSR page.

The following table describes the Certificate Configuration page.

Field

Description

Displays the current status of the Certificate Configuration page.

Certificate Settings

Displays the following information about the certificate:

File Name

Certificate Name

Certificate Type

Certificate Group

Description

Certificate File Data

Displays the contents of the certificate file.

Delete button or icon

Deletes the current certificate.

Download button or icon

Downloads the certificate to your local system.

## Certificate
                        	 Monitor

The
                              		  Certificate Monitor page appears when you choose Security >
                                 			 Certificate Monitor .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Certificate Monitor page to do the following:

Specify the
                                    				start time

Specify the
                                    				frequency

Enable email
                                    				notification and provide email addresses of those to be notified

The
                              		  following table describes the Certificate Monitor page.

Field

Description

Displays the current status of the Certificate Monitor page.

Notification Start Time

Enter the number of days before the certificate expires that you
                                          					 want to be notified.

Notification Frequency

Enter the notification frequency and click one of the radio
                                          					 buttons to indicate days or hours.

Enable Email Notification

Check the box to the enable email notification.

For the
                                                      						system to send notifications, you must configure an SMTP host.

Email ID

Enter the email addresses of those to be notified in the text
                                          					 box. Enter multiple e-mail addresses by separating each address with a
                                          					 semicolon (;). There should be no spaces between the email addresses.

Save button or icon

Saves the information entered on the Certificate Monitor page.

## IPSec Policy List

The IPSec Policy List page appears when you choose Security > IPSec Configuration .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the IPSec Policy List page to display existing IPSec policies, add an additional IPSec policy, or modify an existing IPSec
                              policy.

The following table describes the IPSec Policy List page.

Field

Description

Displays the current status of the IPSec Policy List page.

Displays the currently configured IPSec policies. Click on the Policy Name link to the IPSec Policy Configuration page for
                                          that policy.

Add New button or icon

Adds a new IPSec policy. When you click Add New , the IPSec Policy Configuration page appears. See Table 2 for information about the IPSec Policy Configuration page.

The following table describes the IPSec Policy Configuration page in Non Federal Information Processing Standard (Non FIPS)
                              Mode.

Field

Description

Displays the current status of the IPSec Policy Configuration page.

Policy Group Name

Specifies the name of the IPSec policy group.

Policy Name

Specifies the name of the IPSec policy.

Authentication Method

Specifies the authentication method.

The Authentication Method field has two options Preshared Key and Certificate.

If Preshared Key is selected, the Preshared Key field is editable and the Peer Type and Certificate Name fields are disabled.

If Certificate is selected, the Preshared Key field is disabled. The Peer Type and Certificate Name fields are enabled.

Preshared Key

Specifies the preshared key if you selected Pre-shared Key in the Authentication Method field.

Peer Type

Specifies that the peer type is different.

Certificate Name

Specifies the certificate name.

Destination Address

Specifies the IP address of the destination (FQDN is not supported).

Destination Port

Enter the port number at the destination.

Source Address

Specifies the IP address of the source (FQDN is not supported).

Source Port

Specifies the port number at the source.

Mode

Select the Transport mode.

Remote Port

Specifies the port number to use at the destination.

Protocol

Specifies the specific protocol, or Any:

TCP

UDP

Any

Encryption Algorithm

From the drop-down list, choose the encryption algorithm.
                                          					 Choices include:

3DES

AES 128

AES 256

Hash Algorithm

Specifies the hash algorithm:

SHA1

SHA256

ESP Algorithm

From the drop-down list, choose the ESP algorithm. Choices
                                          					 include:

3DES

AES 128

AES 256

Phase One Life Time

Specifies the lifetime for phase One, IKE negotiation, in
                                          					 seconds.

Phase One DH

From the drop-down list, choose the phase One DH value. Choices include: 2, 5, 14, 15, 16, 17, and 18.

Phase Two Life Time

Specifies the lifetime for phase Two, IKE negotiation, in
                                          					 seconds.

Phase Two DH

From the drop-down list, choose the phase Two DH value. Choices include: 2, 5, 14, 16, 17, and 18.

Enable Policy

Check the check box to enable the policy.

Save button or icon

Saves the changes made to the IPSec Policy List page.

The following table lists the field names that are displayed when the system is in FIPS Mode or ESM Mode.

Field

Description

Displays the current status of the IPSec Policy Configuration page.

Policy Group Name

Specifies the name of the IPSec policy group.

Policy Name

Specifies the name of the IPSec policy.

Authentication Method

Specifies the authentication method. By default, certificate is selected.

Preshared key is not present in FIPS Mode.

Peer Type

Specifies the peer type is different.

Certificate Name

The name of the certificate.

Destination Address

Specifies the IP address or FQDN of the destination.

Destination Port

Enter the port number at the destination.

Source Address

Specifies the IP address or FQDN of the source.

Source Port

Specifies the port number at the source.

Mode

Specifies the Transport mode.

Remote Port

Specifies the port number to use at the destination.

Protocol

Specifies the specific protocol, or Any:

TCP

UDP

Any

Encryption Algorithm

From the drop-down list, choose the encryption algorithm. Choices include:

3DES (default)

AES 128

AES 256

Hash Algorithm

Specifies the hash algorithm:

SHA1

SHA256

ESP Algorithm

From the drop-down list, choose the ESP algorithm. Choices include:

3DES (default)

AES 128

AES 256

Phase One Life Time

Specifies the lifetime for phase One, IKE negotiation, in seconds.

Phase One DH

From the drop-down list, choose the phase One DH value. The choices are from 14 to 18.

Phase Two Life Time

Specifies the lifetime for phase Two, IKE negotiation, in seconds.

Phase Two DH

From the drop-down list, choose the phase Two DH value. The choices are from 14 to 18.

Enable Policy

Check the check box to enable the policy.

Save button or icon

Saves the changes made to the IPSec Policy Configuration page.

## Software
                        	 Installation/Upgrade

The
                              		  Software Installation/Upgrade page appears when you choose Software Upgrades
                                 			 > Install/Upgrade .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Software Installation/Upgrade page to install or upgrade software from a DVD/CD
                              		  or from a file system on a remote server.

The
                              		  following table describes the Software Installation/Upgrade page.

Field

Description

Displays the current status of the Software Installation/Upgrade
                                          					 page.

Source

Pull-down menu used to specify the source for the
                                          					 installation/upgrade. Options are DVD/CD or Remote
                                             						Filesystem .

Directory

The name of the directory containing the files.

If the
                                                      						upgrade file is on a Linux or Unix server, you must enter a forward slash at
                                                      						the beginning of the directory path that you want to specify. For example, if
                                                      						the upgrade file is in the patches directory, you must enter /patches . If the upgrade file is on a Windows server, check
                                                      						with your system administrator for the correct directory path.

Server

The hostname or IP address of the remote server from which the
                                          					 software is downloaded.

User Name

The name of a user who is configured on the remote server.

User Password

Password that is configured for this user on the remote server.

Transfer Protocol

Pull-down menu used to specify which transfer protocol to use.
                                          					 Options are ftp or sftp .

These
                                                      						options are available only if you selected Remote
                                                         						  Filesystem from the Source pull-down menu. If you selected DVD/CD , this pull-down menu is grayed out.

Cancel Install button or icon

Cancels the installation or upgrade procedure.

Next button or icon

Continues with the installation or upgrade procedure.

## Branding

The Branding page appears when you choose Software
                                    				Upgrades > Branding .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

You can
                              		  upload customized branding for Cisco Emergency Responder. Use the Branding page to upload the branding.zip folder which contains the " CER" directory.

Once the branding.zip folder is uploaded successfully, you can
                              		  enable or disable Branding using either the command line or graphical user
                              		  interface and then refresh the page for the changes to take effect. For more
                              		  information, refer to the "Branding" chapter.

The
                              		  following table describes the Branding page.

Field

Description

Displays status of the Branding page.

Click the Browse button to locate the branding.zip folder on the server.

Click the Upload File button to upload the file to the server.
                                          					 It uploads the file successfully after it validates the required contents of
                                          					 the branding.zip folder.

After you have uploaded the branding.zip file, click this button to
                                          					 enable branding customizations on this Cisco Emergency Responder node. After
                                          					 you enable branding, refresh your browser.

Click this button to disable customized branding from Cisco Emergency Responder .

## Ping
                        	 Configuration

The Ping
                              		  Configuration page appears when you choose Services >
                                 			 Ping .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Ping Configuration page to send ping requests to test if other systems are
                              		  reachable over the network.

The
                              		  following table describes the Ping Configuration page.

Field

Description

Displays the current status of the Ping Configuration page.

Hostname or IP Address

Text box into which you enter the IP address or network name for
                                          					 the system that you want to ping.

Ping Interval

Text box in which you enter the amount of time between ping
                                          					 requests, in seconds.

Packet Size

Text box into which you enter the packet size of the ping
                                          					 request.

Ping iterations

Pull-down menu that allows you to choose the number of times you
                                          					 want to send ping requests to the other system. Available options are 1, 5, 25,
                                          					 or 100 times

When you
                                                      						specify multiple pings, the ping command does not display the ping date and time in real time. Be aware that the ping command displays the data after the number of pings that you specified are
                                                      						complete.

Validate IPsec

Select the check box to have the system validate IPsec.

Text box in which the ping results are displayed.

Ping button or icon

Sends the ping request.

## Remote Access
                        	 Configuration

The Remote
                              		  Access Configuration page appears when you choose Services >
                                 			 Remote Support .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Remote Access Configuration page to set up a remote account that Cisco support
                              		  personnel can use to access the system for a specified period of time. If the
                              		  account duration limit expires, Cisco support can not access the remote support
                              		  account.

When you
                              		  establish a remote account, the system generates a pass phrase.

Follow
                              		  this procedure to complete the remote account setup:

Call Cisco
                                    				support and provide them with the remote support account name and pass phrase.

Cisco support
                                    				enters the pass phrase into a decoder program that generates a password from
                                    				the pass phrase.

Cisco support
                                    				logs into the remote support account on the customer system by using the
                                    				decoded password.

If you
                              		  have not already created a remote account, when you navigate to the Remote
                              		  Access Configuration page you can create a new account.

The
                              		  following table describes the Remote Access Configuration page.

Field

Description

Displays the current status of the Remote Access Configuration
                                          					 page.

Account Name

Name for the new remote account. Account names must be at least
                                          					 six-characters long and consist of all lowercase, alphabetic characters

Account Duration

The amount of time that the remote account exists, in days.

Save button or icon

Creates a new remote account. You must provide the Account Name
                                          					 and Account Duration before you click Add .
                                          					 Remote Access Configuration page redisplays. See Table 2 for a description of the fields on
                                          					 the Remote Access Configuration page.

Delete button or icon

Deletes the currently configured remote account.

The Delete
                                                      						button or icon is only visible if there is an existing remote account.

If you
                              		  have already created a remote account, when you navigate to the Remote Access
                              		  Configuration page you view and delete the remote account.

The
                              		  following table describes the Remote Access Configuration page.

Field

Description

Account Name

Displays the name of the remote support account.

Expiration

Displays the date and time when access to the remote account
                                          					 expires.

Passphrase

Displays the generated pass phrase.

Decode Version

Indicates the version of the decoder in use.

Delete button or icon

Deletes the remote access account information.

| Field | Description |
|---|---|
| ServerGroup |
| Hostname | Displays the name of the host. |
| IP
                                          					 Address | Displays the IP address of the host. |
| Alias | Displays the alias of the host |
| Type of Node | Displays the node type of the host. |
| Database Replication | Displays the name of the database which will either be a
                                          					 Publisher or Subscriber. |

| Field | Description |
|---|---|
| Hardware Resources |
| Platform Type | Model identity of the platform server |
| Serial Number | Displays serial number of the virtual machine. |
| Virtual Hardware | Shows you the status as "Configured" if the hardware is a virtual machine. |
| Virtual Support | Shows you the status as "Supported" if the support is on a virtual machine. |
| Processor Speed | Speed of the processor |
| CPU
                                          					 Type | Type of processor in the platform server |
| Memory | Total amount of memory in Mbytes |
| Object ID | Object ID of the platform server |
| OS
                                          					 Version | Operating system version running on the platform server |
| RAID Details | Detailed summary of the platform hardware |

| Note | The network status
                                          			 information that displays depends on whether Network Fault Tolerance is
                                          			 enabled. When Network Fault Tolerance is enabled, Ethernet port 1 automatically
                                          			 takes over network communications if Ethernet port 0 fails. If Network Fault
                                          			 Tolerance is enabled, network status information displays for the network ports
                                          			 Ethernet 0, Ethernet 1, and Bond 0. If Network Fault Tolerance is not enabled,
                                          			 status information displays only for Ethernet 0. |
|---|---|

| Field | Description |
|---|---|
| Ethernet Details |
| DHCP Status | Indicates whether DHCP is enabled for Ethernet port 0. |
| Status | Indicates whether the port is Up or Down for Ethernet ports 0
                                          					 and 1. |
| IP
                                          					 Address | Shows the IP address of Ethernet port 0 (and Ethernet port 1 if
                                          					 Network Fault Tolerance (NFT) is enabled). |
| IP
                                          					 Mask | Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT
                                          					 is enabled). |
| Link Detected | Indicates whether there is an active link. |
| Queue Length | Displays the length of the queue. |
| MTU | Displays the maximum transmission unit. |
| MAC Address | Displays the hardware address of the port. |
| RX
                                          					 Stats | Displays information about received bytes and packets. |
| TX
                                          					 Stats | Displays information about transmitted bytes and packets. |
| DNS Details |
| Primary DNS | Displays the IP address of the primary domain name server. |
| Secondary DNS | Displays the IP address of the secondary domain name server. |
| Options | Displays the number of attempts and timeouts. |
| Domain | Displays the domain of the server. |
| Gateway | Displays the IP address of the network gateway on Ethernet port
                                          					 0. |

| Field | Description |
|---|---|
| Partition Versions | Displays the software version that is running on the active and
                                          					 inactive partitions. |
| Active Version Installed Software Options | Displays the versions of installed software options that are
                                          					 installed on the active version. |
| Inactive Version Installed Software Options | Displays the versions of installed software options that are
                                          					 installed on the inactive version. |
| Installed Software Options | Displays the cop file installed on the system. |

| Field | Description |
|---|---|
| Host Name | Name of the Cisco UCS host
                                          					 where the Emergency Responder system is installed. |
| Date | Date and
                                          					 time based on the continent and region that were specified during operating
                                          					 system installation. |
| Time Zone | Time zone
                                          					 that was chosen during installation. |
| Locale | Locale of
                                          					 the system. |
| Product
                                          					 Version | Operating
                                          					 system version. |
| Uptime | Displays
                                          					 system uptime information. |
| CPU | Displays the
                                          					 percentage of CPU capacity that is idle, the percentage that is running system
                                          					 processes, and the percentage that is running user processes. |
| Memory | Displays
                                          					 information about memory usage, including the amount of total memory, free
                                          					 memory, and used memory in kilobytes. |
| Disk/active | Displays the
                                          					 amount of total, free, and used disk space on the active disk. |
| Disk/inactive | Displays the
                                          					 amount of total, free, and used disk space on the inactive disk. |
| Disk/logging | Displays the
                                          					 amount of total, free, and disk space that is used for disk logging. |

| Field | Description |
|---|---|
| Application | Name of the application using (listening on) the port. |
| Protocol | Protocol used on this port (TCP, UDP, and so on). |
| Port Number | Numeric port number. |
| Type | Type of traffic allowed on this port: Public—All traffic allowed. Translated—All traffic allowed but forwarded to a different port. Private—Traffic only allowed from a defined set of remote servers, for example, other servers in the server group. |
| Translated Port | Traffic destined for this port get forwarded to the port listed
                                          					 in the Port Number column. This field applies to Translated type ports only. |
| Status | Status of port usage: Enabled—In use by the application and opened by the firewall. Disabled—Blocked by the firewall and not in use. |
| Description | Brief description of how the port is used. |

| Note | All Ethernet settings apply only to Eth0. You can't configure any settings for Eth1. The maximum transmission unit (MTU) on
                                          Eth0 defaults to 1500. |
|---|---|

| Field | Description |
|---|---|
| DHCP Information |
| DHCP | Indicates whether DHCP is enabled or disabled and allows you to
                                          					 change the DHCP setting using the pull-down menu. |
| Host Information |
| Hostname | Displays the hostname of the node. |
| Port Information |
| IP
                                          					 Address | Displays the IP address of the system. You can change the IP
                                          					 address by entering a new IP address in the text box. |
| Subnet Mask | Displays the IP subnet mask address. You can change the mask by
                                          					 entering a new subnet mask in the text box. |
| Gateway Information |
| Default Gateway | Displays the IP address of the default network gateway. You can
                                          					 change the gateway IP address by entering a new IP address in the text box. |
| Save button or icon | Saves any changes made to the Ethernet Configuration page. Caution If you click Save , the machine reboots. Don't click Save unless you want to shut down and reboot your system. Note To
                                                      						recognize any new IP addresses, both servers in the server group must be
                                                      						manually rebooted. | Caution | If you click Save , the machine reboots. Don't click Save unless you want to shut down and reboot your system. | Note | To
                                                      						recognize any new IP addresses, both servers in the server group must be
                                                      						manually rebooted. |
| Caution | If you click Save , the machine reboots. Don't click Save unless you want to shut down and reboot your system. |
| Note | To
                                                      						recognize any new IP addresses, both servers in the server group must be
                                                      						manually rebooted. |

| Caution | If you click Save , the machine reboots. Don't click Save unless you want to shut down and reboot your system. |
|---|---|

| Note | To
                                                      						recognize any new IP addresses, both servers in the server group must be
                                                      						manually rebooted. |
|---|---|

| Note | All Ethernet
                                          			 settings apply only to Eth0. You cannot configure any settings for Eth1. The
                                          			 Maximum Transmission Unit (MTU) on Eth0 defaults to 1500. |
|---|---|

| Field | Description |
|---|---|
| Enable IPv6 | Check this check box to enable IPv6 on the node. |
| Router Advertisement | Choose one of the following IP address sources: Router Advertisement DHCP Manual Entry The three IP address sources are mutually exclusive. Note Unless you specify Manual
                                                      						Entry, IPv6 Address, Prefix Length, and Default Gateway fields remain read
                                                      						only. | Note | Unless you specify Manual
                                                      						Entry, IPv6 Address, Prefix Length, and Default Gateway fields remain read
                                                      						only. |
| Note | Unless you specify Manual
                                                      						Entry, IPv6 Address, Prefix Length, and Default Gateway fields remain read
                                                      						only. |
| IPv6 Address | If you chose Manual Entry, enter the IPv6 address of the node.
                                          					 For example, fd6:2:6:96:21e:bff:fecc:2e3a. |
| Prefix
                                          					 Length | If you
                                          					 chose Manual Entry, enter the prefix length. For example, 64. |
| Default
                                          					 Gateway | If you
                                          					 chose Manual Entry, enter the default gateway. For example,
                                          					 fe80::3ece:73ff:fea9:c641. |
| Update with Reboot | If you want the system to reboot immediately after you click
                                          					 Save, check this check box. If you want to reboot later, leave the check box
                                          					 blank. Note If you
                                                      						check the Update with Reboot check box, the system reboots after you click
                                                      						Save. For the IPv6 settings to take effect, reboot the system. | Note | If you
                                                      						check the Update with Reboot check box, the system reboots after you click
                                                      						Save. For the IPv6 settings to take effect, reboot the system. |
| Note | If you
                                                      						check the Update with Reboot check box, the system reboots after you click
                                                      						Save. For the IPv6 settings to take effect, reboot the system. |

| Note | Unless you specify Manual
                                                      						Entry, IPv6 Address, Prefix Length, and Default Gateway fields remain read
                                                      						only. |
|---|---|

| Note | If you
                                                      						check the Update with Reboot check box, the system reboots after you click
                                                      						Save. For the IPv6 settings to take effect, reboot the system. |
|---|---|

| Note | You can only view
                                          			 and change the publisher hostname IP address only on the Emergency Responder
                                          			 Subscriber, not on the Emergency Responder publisher itself. Changing these
                                          			 fields must be followed by an immediate reboot of the Subscriber. |
|---|---|

| Field | Description |
|---|---|
| Hostname | Displays the hostnames of the Emergency Responder Publisher for
                                          					 this Subscriber. To change the hostname, enter the new hostname in the text
                                          					 box, and click Save . |
| IP
                                          					 Address | Displays the IP address of the Emergency Responder Publisher for
                                          					 this Subscriber. To change the IP address, enter the IP address in the text
                                          					 box, and click Save . |
| Save button or icon | Saves the information in the Publisher Configuration Settings
                                          					 page. |

| Note | Ensure that the
                                          			 external NTP server is stratum 9 or higher (1 to 9). |
|---|---|

| Note | Any change you
                                          			 make to the NTP servers can take up to five minutes to complete. Whenever you
                                          			 make any change to the NTP servers, you must refresh the page to display the
                                          			 correct status. |
|---|---|

| Caution | If you add,
                                          			 modify, or delete an NTP server, you must reboot both the Publisher and the
                                          			 Subscriber. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays how many configured NTP server were found. |
| NTP Server |
| Hostname or IP Address field | Displays the hostnames or IP addresses of the configured NTP
                                          					 servers. To change a hostname or IP address, click it, enter the new hostname
                                          					 or IP address, and click Save . |
| Add New button or icon | Adds a new NTP server. After you click Add
                                             						New , enter the hostname of IP address of the new NTP server and click Save . |
| Select All button or icon | Selects all NTP servers listed. When you click this button or
                                          					 icon, a check mark appears in the boxes to the left of each NTP hostname or IP
                                          					 address and to the left of the Hostname or IP Address column heading. Note The Select
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers. | Note | The Select
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers. |
| Note | The Select
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers. |
| Clear All button or icon | Deselects all NTP servers listed. When you click this button or
                                          					 icon, all check marks disappear. Note The Clear
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers. | Note | The Clear
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers. |
| Note | The Clear
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers. |
| Delete Selected button or icon | Deletes the selected NTP server. To delete an NTP server, you
                                          					 must first select it from the list of NTP servers. Click the box to the left of
                                          					 the NTP server name to select it. To select all listed NTP servers, click the
                                          					 box to the left of the Hostname or IP Address column heading or click Select
                                             						All . Note The Delete
                                                      						Selected button or icon is only visible if you have previously configured one
                                                      						or more NTP servers. | Note | The Delete
                                                      						Selected button or icon is only visible if you have previously configured one
                                                      						or more NTP servers. |
| Note | The Delete
                                                      						Selected button or icon is only visible if you have previously configured one
                                                      						or more NTP servers. |

| Note | The Select
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers. |
|---|---|

| Note | The Clear
                                                      						All button or icon is only visible if you have previously configured one or
                                                      						more NTP servers. |
|---|---|

| Note | The Delete
                                                      						Selected button or icon is only visible if you have previously configured one
                                                      						or more NTP servers. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays how many configured NTP server were found. |
| NTP Server Settings |
| Hostname or IP Address field | Displays the hostnames or IP addresses of the configured NTP
                                          					 servers. To change a hostname or IP address, click it, enter the new hostname
                                          					 or IP address, and click Save . |
| Save button or icon | Saves the information about the new NTP server. |

| Field | Description |
|---|---|
| Status | Displays the status of the SMTP Settings page. |
| SMTP Host |
| Hostname or IP Address | Enter the hostname or IP address of the SMTP server in the text
                                          					 box. |
| Host Status | Displays the status of the SMTP host server. |
| Save button or icon | Saves changes made to the SMTP Settings page. |

| Note | Before you can
                                          			 manually configure the server time, you must delete any NTP servers that you
                                          			 have configured. See NTP Server List for more information. |
|---|---|

| Caution | If you change the
                                          			 server time, you must reboot both the Publisher and the Subscriber. |
|---|---|

| Field | Description |
|---|---|
| Date | Allows you to set the month, day, year, hours, minutes, and
                                          					 seconds using the pull-down menus. |
| Save button or icon | Saves changes made to the Time Settings page. |

| Note | You must have a
                                          			 different software version installed on the inactive partition to switch
                                          			 versions. |
|---|---|

| Caution | Initiating this
                                          			 action causes the system to restart and become temporarily unavailable. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current status. |
| Installed Versions |
| Active Version | Displays the version running on the active partition. |
| Inactive Version | Display the version on the inactive partition. |
| Restart button or icon | Restarts the system. |
| Shutdown button or icon | Shuts down the system. |
| Switch Versions button or icon | Actives the software version on the inactive partition. Note The Switch
                                                      						Versions button or icon is only visible if there is a software version
                                                      						installed on the inactive partition. | Note | The Switch
                                                      						Versions button or icon is only visible if there is a software version
                                                      						installed on the inactive partition. |
| Note | The Switch
                                                      						Versions button or icon is only visible if there is a software version
                                                      						installed on the inactive partition. |

| Note | The Switch
                                                      						Versions button or icon is only visible if there is a software version
                                                      						installed on the inactive partition. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current status. |
| Certificate List |
| Find certificate list where | Enter search criteria for the certificate lists you want to find. To find all certificate lists by file name, select File Name from the pull-down menu and click Find without entering any criteria. To find all certificate lists by certificate name, select Certificate Name from the pull-down menu and click Find without entering any criteria. To narrow your search: Select the search relationship (begins with, contains, and so on) from the pull-down menu, and enter the search string in
                                                the text box. To search on a combination of fields, click the Plus icon (+) to add additional search parameters. Click the Minus icon ( – ) to remove search parameters. Click Clear Filter to remove all additional search parameters. Use the Rows per Page pull-down menu to select how many rows are displayed per page. When you have entered all of the search parameters, click Find . If the search finds existing certificates, the information about the certificates (File Name, Certificate Name, and Certificate
                                          Type) displays in the Certificate List. Click the File Name link to display the Certificate Configuration page. See Table 8 for information about the Certificate Configuration Page. |
| Generate New button or icon | Allows you to generate a new certificate. When you click Generate New , the Generate Certificate page appears. See Table 2 for a description of the Generate Certificate page. |
| Upload Certificate button or icon | Allows you to upload a certificate from a remote server. When you click Upload Certificate , the Upload Certificate page appears. See Table 3 for a description of the Upload Certificate page. |
| Upload CTL button or icon | Allows you to upload a Certificate Trust List (CTL) from a remote server. When you click Upload CTL , the Upload Certificate Trust List page appears. See Table 4 for a description of the Upload Certificate Trust List page. |
| Generate CSR button or icon | Allows you to generate a new Certificate Signing Request (CSR). When you click Generate CSR , the Generate Certificate Signing Request page appears. See Table 6 for a description of the Generate New page. |
| Download CSR button or icon | Allows you to download a CSR. When you click Download CSR , the Download Certificate Signing Request page appears. See Table 7 for a description of the Download Certificate Signing Request page. |

| Field | Description |
|---|---|
| Status | Displays the current status of the Generate New Self-signed Certificate page. |
| Generate Self-signed |
| Certificate Purpose | Choose the required option from the drop-down list. When you choose any of the following options, the Key Type field is automatically set to RSA . tomcat ipsec When you choose any of the following options, the Key Type field is automatically set to EC (Elliptical Curve). tomcat-ECDSA |
| Distribution | Choose a Emergency Responder server from the drop-down list. |
| Common | Displays the name of the Emergency Responder server that you have chosen using the Distribution drop-down list. |
| Auto-populated Domains | Appears only if you have chosen any of the following options using the Certificate Purpose drop-down list. tomcat-ECDSA |
| Key Type | This field lists the type of keys used for encryption and decryption of the public-private key pair. Emergency Responder supports
                                          EC and RSA key types. |
| Key Length | Allows you to choose 1024, 2048, 3072, or 4096 from the drop-down list. Note Certificates with a key length value of 256, 384, or 521 are chosen only for ECDSA certificates. These options are not available
                                                   for RSA certificates. If the key length value is 1024, 2048, 3072, or 4096, the supported hash algorithm is SHA256. If the key length value is 256, 384, or 521, the supported hash algorithms are SHA384 or SHA512. | Note | Certificates with a key length value of 256, 384, or 521 are chosen only for ECDSA certificates. These options are not available
                                                   for RSA certificates. |
| Note | Certificates with a key length value of 256, 384, or 521 are chosen only for ECDSA certificates. These options are not available
                                                   for RSA certificates. |
| Hash Algorithm | Choose a value that is greater than or equal to the key length from the drop-down list: Note The values in the Hash Algorithm drop-down list changes based on the value you have chosen in the Key Length field. If your system is running in FIPS mode, it is mandatory to choose SHA256 as the hashing algorithm. | Note | The values in the Hash Algorithm drop-down list changes based on the value you have chosen in the Key Length field. If your system is running in FIPS mode, it is mandatory to choose SHA256 as the hashing algorithm. |
| Note | The values in the Hash Algorithm drop-down list changes based on the value you have chosen in the Key Length field. If your system is running in FIPS mode, it is mandatory to choose SHA256 as the hashing algorithm. |
| Generate button | Generates a new certificate. You must first select a Certificate Name from the pull-down menu. |
| Close button | Closes the Generate New Self-signed Certificate page. |

| Note | Certificates with a key length value of 256, 384, or 521 are chosen only for ECDSA certificates. These options are not available
                                                   for RSA certificates. |
|---|---|

| Note | The values in the Hash Algorithm drop-down list changes based on the value you have chosen in the Key Length field. If your system is running in FIPS mode, it is mandatory to choose SHA256 as the hashing algorithm. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current status of the Upload Certificate page. |
| Upload Certificate |
| Certificate Name | Use the pull-down menu to select the name of the certificate to upload. |
| Root Certificate | Enter the name of the root certificate. |
| Upload File | Use the Browse button to select the file to be uploaded. |
| Upload File button or icon | Uploads the certificate file specified in the Upload Certificate section. |
| Close button or icon | Closes the Update Certificate page. |

| Field | Description |
|---|---|
| Status | Displays the current status of the Upload CTL page. |
| Upload Certificate |
| Certificate Name | Use the pull-down menu to select the name of the CTL file to upload. |
| Root Certificate | Enter the name of the root certificate. |
| Upload File | Use the Browse button to select the file to be uploaded. |
| Upload File button or icon | Uploads the certificate file specified in the Upload Certificate Trust List section. |
| Close button or icon | Closes the Update CTL page. |

| Field | Description |
|---|---|
| Certificate Purpose | From the drop-down list, select a value: Tomcat Tomcat-ECDSA IPSec Note ITLRecovery and Authz certificates aren't supported in Emergency Responder. | Note | ITLRecovery and Authz certificates aren't supported in Emergency Responder. |
| Note | ITLRecovery and Authz certificates aren't supported in Emergency Responder. |
| Distribution | Select a Emergency Responder server. When you select this field for multiserver for ECDSA, the syntax is: Tomcat-ECDSA common name: <host-name>-EC-ms.<domain> |
| Common Name / Common Name_SerialNumber | Displays the common name or the common name appended with the serial number of the certificate. Common Name or Common Name_SerialNumber
                                          is the file name of the certificate. Shows the name of the Unified Communications Manager application that you selected in the Distribution field by default. |
| Auto-populated Domains | This field appears in Subject Alternate Names (SANs) section. It lists the host names that are to be protected by a single
                                          certificate. |
| Parent Domain | This field appears in Subject Alternate Names (SANs) section. It shows the default domain name. You can modify the domain
                                          name, if required. |
| Key Type | This field identifies the type of key used for encryption and decryption for the public-private key pair. |
| Key Length | From the Key Length drop-down list, select one of the values. Depending on the key length, the CSR request limits the hash algorithm choices. By having the limited hash algorithm choices,
                                          you can use a hash algorithm strength that is greater than or equal to the key length strength. For example, for a key length
                                          of 256, the supported hash algorithms are SHA256, SHA384, or SHA512. Similarly, for the key length of 384, the supported hash
                                          algorithms are SHA384 or SHA512. Note Certificates with a key length value of 3072 or 4096 can only be selected for RSA certificates. These options aren't available for ECDSA certificates. | Note | Certificates with a key length value of 3072 or 4096 can only be selected for RSA certificates. These options aren't available for ECDSA certificates. |
| Note | Certificates with a key length value of 3072 or 4096 can only be selected for RSA certificates. These options aren't available for ECDSA certificates. |
| Hash Algorithm | Select a value from the Hash Algorithm drop-down list to have stronger hash algorithm as the elliptical curve key length. From the Hash Algorithm drop-down list, select one of the values. Note The values for the Hash Algorithm field change based on the value you select in the Key Length field. If your system is running on FIPS mode, it's mandatory that you select SHA256 as the hashing algorithm. | Note | The values for the Hash Algorithm field change based on the value you select in the Key Length field. If your system is running on FIPS mode, it's mandatory that you select SHA256 as the hashing algorithm. |
| Note | The values for the Hash Algorithm field change based on the value you select in the Key Length field. If your system is running on FIPS mode, it's mandatory that you select SHA256 as the hashing algorithm. |

| Note | ITLRecovery and Authz certificates aren't supported in Emergency Responder. |
|---|---|

| Note | Certificates with a key length value of 3072 or 4096 can only be selected for RSA certificates. These options aren't available for ECDSA certificates. |
|---|---|

| Note | The values for the Hash Algorithm field change based on the value you select in the Key Length field. If your system is running on FIPS mode, it's mandatory that you select SHA256 as the hashing algorithm. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current status of the Generate CSR page. |
| Generate Certificate Signing Request |
| Certificate Name | Use the pull-down menu to select the name of the CTL file to generate. |
| Generate CSR button or icon | Generates a new CSR. |
| Close button or icon | Close the Generate CSR page. |

| Field | Description |
|---|---|
| Status | Displays the current status of the Download CSR page. |
| Download Certificate Signing Request |
| Certificate Name | Use the pull-down menu to select the name of the CTL file to download. |
| Download CSR button or icon | Downloads the CSR specified in the Download Certificate Signing Request section. |
| Close button or icon | Closes the Download CSR page. |

| Field | Description |
|---|---|
| Status | Displays the current status of the Certificate Configuration page. |
| Certificate Settings | Displays the following information about the certificate: File Name Certificate Name Certificate Type Certificate Group Description |
| Certificate File Data | Displays the contents of the certificate file. |
| Delete button or icon | Deletes the current certificate. |
| Download button or icon | Downloads the certificate to your local system. |

| Field | Description |
|---|---|
| Status | Displays the current status of the Certificate Monitor page. |
| Certificate Monitor Configuration |
| Notification Start Time | Enter the number of days before the certificate expires that you
                                          					 want to be notified. |
| Notification Frequency | Enter the notification frequency and click one of the radio
                                          					 buttons to indicate days or hours. |
| Enable Email Notification | Check the box to the enable email notification. Note For the
                                                      						system to send notifications, you must configure an SMTP host. | Note | For the
                                                      						system to send notifications, you must configure an SMTP host. |
| Note | For the
                                                      						system to send notifications, you must configure an SMTP host. |
| Email ID | Enter the email addresses of those to be notified in the text
                                          					 box. Enter multiple e-mail addresses by separating each address with a
                                          					 semicolon (;). There should be no spaces between the email addresses. |
| Save button or icon | Saves the information entered on the Certificate Monitor page. |

| Note | For the
                                                      						system to send notifications, you must configure an SMTP host. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current status of the IPSec Policy List page. |
| IPSec Policy List | Displays the currently configured IPSec policies. Click on the Policy Name link to the IPSec Policy Configuration page for
                                          that policy. |
| Add New button or icon | Adds a new IPSec policy. When you click Add New , the IPSec Policy Configuration page appears. See Table 2 for information about the IPSec Policy Configuration page. |

| Field | Description |
|---|---|
| Status | Displays the current status of the IPSec Policy Configuration page. |
| IPSec Policy Details |
| Policy Group Name | Specifies the name of the IPSec policy group. |
| Policy Name | Specifies the name of the IPSec policy. |
| Authentication Method | Specifies the authentication method. The Authentication Method field has two options Preshared Key and Certificate. If Preshared Key is selected, the Preshared Key field is editable and the Peer Type and Certificate Name fields are disabled. If Certificate is selected, the Preshared Key field is disabled. The Peer Type and Certificate Name fields are enabled. |
| Preshared Key | Specifies the preshared key if you selected Pre-shared Key in the Authentication Method field. |
| Peer Type | Specifies that the peer type is different. |
| Certificate Name | Specifies the certificate name. |
| Destination Address | Specifies the IP address of the destination (FQDN is not supported). |
| Destination Port | Enter the port number at the destination. |
| Source Address | Specifies the IP address of the source (FQDN is not supported). |
| Source Port | Specifies the port number at the source. |
| Mode | Select the Transport mode. |
| Remote Port | Specifies the port number to use at the destination. |
| Protocol | Specifies the specific protocol, or Any: TCP UDP Any |
| Encryption Algorithm | From the drop-down list, choose the encryption algorithm.
                                          					 Choices include: 3DES AES 128 AES 256 |
| Hash Algorithm | Specifies the hash algorithm: SHA1 SHA256 |
| ESP Algorithm | From the drop-down list, choose the ESP algorithm. Choices
                                          					 include: 3DES AES 128 AES 256 |
| Phase 1 DH Group |
| Phase One Life Time | Specifies the lifetime for phase One, IKE negotiation, in
                                          					 seconds. |
| Phase One DH | From the drop-down list, choose the phase One DH value. Choices include: 2, 5, 14, 15, 16, 17, and 18. |
| Phase 2 DH Group |
| Phase Two Life Time | Specifies the lifetime for phase Two, IKE negotiation, in
                                          					 seconds. |
| Phase Two DH | From the drop-down list, choose the phase Two DH value. Choices include: 2, 5, 14, 16, 17, and 18. |
| IPSec Policy Configuration |
| Enable Policy | Check the check box to enable the policy. |
| Save button or icon | Saves the changes made to the IPSec Policy List page. |

| Field | Description |
|---|---|
| Status | Displays the current status of the IPSec Policy Configuration page. |
| IPSec Policy Details |
| Policy Group Name | Specifies the name of the IPSec policy group. |
| Policy Name | Specifies the name of the IPSec policy. |
| Authentication Method | Specifies the authentication method. By default, certificate is selected. Note Preshared key is not present in FIPS Mode. | Note | Preshared key is not present in FIPS Mode. |
| Note | Preshared key is not present in FIPS Mode. |
| Peer Type | Specifies the peer type is different. |
| Certificate Name | The name of the certificate. |
| Destination Address | Specifies the IP address or FQDN of the destination. |
| Destination Port | Enter the port number at the destination. |
| Source Address | Specifies the IP address or FQDN of the source. |
| Source Port | Specifies the port number at the source. |
| Mode | Specifies the Transport mode. |
| Remote Port | Specifies the port number to use at the destination. |
| Protocol | Specifies the specific protocol, or Any: TCP UDP Any |
| Encryption Algorithm | From the drop-down list, choose the encryption algorithm. Choices include: 3DES (default) AES 128 AES 256 |
| Hash Algorithm | Specifies the hash algorithm: SHA1 SHA256 |
| ESP Algorithm | From the drop-down list, choose the ESP algorithm. Choices include: 3DES (default) AES 128 AES 256 |
| Phase 1 DH Group |
| Phase One Life Time | Specifies the lifetime for phase One, IKE negotiation, in seconds. |
| Phase One DH | From the drop-down list, choose the phase One DH value. The choices are from 14 to 18. |
| Phase 2 DH Group |
| Phase Two Life Time | Specifies the lifetime for phase Two, IKE negotiation, in seconds. |
| Phase Two DH | From the drop-down list, choose the phase Two DH value. The choices are from 14 to 18. |
| IPSec Policy Configuration |
| Enable Policy | Check the check box to enable the policy. |
| Save button or icon | Saves the changes made to the IPSec Policy Configuration page. |

| Note | Preshared key is not present in FIPS Mode. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current status of the Software Installation/Upgrade
                                          					 page. |
| Software Location |  |
| Source | Pull-down menu used to specify the source for the
                                          					 installation/upgrade. Options are DVD/CD or Remote
                                             						Filesystem . |
| Directory | The name of the directory containing the files. Note If the
                                                      						upgrade file is on a Linux or Unix server, you must enter a forward slash at
                                                      						the beginning of the directory path that you want to specify. For example, if
                                                      						the upgrade file is in the patches directory, you must enter /patches . If the upgrade file is on a Windows server, check
                                                      						with your system administrator for the correct directory path. | Note | If the
                                                      						upgrade file is on a Linux or Unix server, you must enter a forward slash at
                                                      						the beginning of the directory path that you want to specify. For example, if
                                                      						the upgrade file is in the patches directory, you must enter /patches . If the upgrade file is on a Windows server, check
                                                      						with your system administrator for the correct directory path. |
| Note | If the
                                                      						upgrade file is on a Linux or Unix server, you must enter a forward slash at
                                                      						the beginning of the directory path that you want to specify. For example, if
                                                      						the upgrade file is in the patches directory, you must enter /patches . If the upgrade file is on a Windows server, check
                                                      						with your system administrator for the correct directory path. |
| Server | The hostname or IP address of the remote server from which the
                                          					 software is downloaded. |
| User Name | The name of a user who is configured on the remote server. |
| User Password | Password that is configured for this user on the remote server. |
| Transfer Protocol | Pull-down menu used to specify which transfer protocol to use.
                                          					 Options are ftp or sftp . Note These
                                                      						options are available only if you selected Remote
                                                         						  Filesystem from the Source pull-down menu. If you selected DVD/CD , this pull-down menu is grayed out. | Note | These
                                                      						options are available only if you selected Remote
                                                         						  Filesystem from the Source pull-down menu. If you selected DVD/CD , this pull-down menu is grayed out. |
| Note | These
                                                      						options are available only if you selected Remote
                                                         						  Filesystem from the Source pull-down menu. If you selected DVD/CD , this pull-down menu is grayed out. |
| Cancel Install button or icon | Cancels the installation or upgrade procedure. |
| Next button or icon | Continues with the installation or upgrade procedure. |

| Note | If the
                                                      						upgrade file is on a Linux or Unix server, you must enter a forward slash at
                                                      						the beginning of the directory path that you want to specify. For example, if
                                                      						the upgrade file is in the patches directory, you must enter /patches . If the upgrade file is on a Windows server, check
                                                      						with your system administrator for the correct directory path. |
|---|---|

| Note | These
                                                      						options are available only if you selected Remote
                                                         						  Filesystem from the Source pull-down menu. If you selected DVD/CD , this pull-down menu is grayed out. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays status of the Branding page. |
| Upload Branding
                                          					 File |
| Browse | Click the Browse button to locate the branding.zip folder on the server. |
| Upload File | Click the Upload File button to upload the file to the server.
                                          					 It uploads the file successfully after it validates the required contents of
                                          					 the branding.zip folder. |
| Enable Branding | After you have uploaded the branding.zip file, click this button to
                                          					 enable branding customizations on this Cisco Emergency Responder node. After
                                          					 you enable branding, refresh your browser. Note Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                                   using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. | Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                                   using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
| Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                                   using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
| Disable Branding | Click this button to disable customized branding from Cisco Emergency Responder . Note Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                                   using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. | Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                                   using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
| Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                                   using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |

| Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                                   using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
|---|---|

| Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                                   using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current status of the Ping Configuration page. |
| Ping Settings |  |
| Hostname or IP Address | Text box into which you enter the IP address or network name for
                                          					 the system that you want to ping. |
| Ping Interval | Text box in which you enter the amount of time between ping
                                          					 requests, in seconds. |
| Packet Size | Text box into which you enter the packet size of the ping
                                          					 request. |
| Ping iterations | Pull-down menu that allows you to choose the number of times you
                                          					 want to send ping requests to the other system. Available options are 1, 5, 25,
                                          					 or 100 times Note When you
                                                      						specify multiple pings, the ping command does not display the ping date and time in real time. Be aware that the ping command displays the data after the number of pings that you specified are
                                                      						complete. | Note | When you
                                                      						specify multiple pings, the ping command does not display the ping date and time in real time. Be aware that the ping command displays the data after the number of pings that you specified are
                                                      						complete. |
| Note | When you
                                                      						specify multiple pings, the ping command does not display the ping date and time in real time. Be aware that the ping command displays the data after the number of pings that you specified are
                                                      						complete. |
| Validate IPsec | Select the check box to have the system validate IPsec. |
| Ping Results | Text box in which the ping results are displayed. |
| Ping button or icon | Sends the ping request. |

| Note | When you
                                                      						specify multiple pings, the ping command does not display the ping date and time in real time. Be aware that the ping command displays the data after the number of pings that you specified are
                                                      						complete. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current status of the Remote Access Configuration
                                          					 page. |
| Remote Access Account Information |
| Account Name | Name for the new remote account. Account names must be at least
                                          					 six-characters long and consist of all lowercase, alphabetic characters |
| Account Duration | The amount of time that the remote account exists, in days. |
| Save button or icon | Creates a new remote account. You must provide the Account Name
                                          					 and Account Duration before you click Add .
                                          					 Remote Access Configuration page redisplays. See Table 2 for a description of the fields on
                                          					 the Remote Access Configuration page. |
| Delete button or icon | Deletes the currently configured remote account. Note The Delete
                                                      						button or icon is only visible if there is an existing remote account. | Note | The Delete
                                                      						button or icon is only visible if there is an existing remote account. |
| Note | The Delete
                                                      						button or icon is only visible if there is an existing remote account. |

| Note | The Delete
                                                      						button or icon is only visible if there is an existing remote account. |
|---|---|

| Field | Description |
|---|---|
| Remote Access Account Information |
| Account Name | Displays the name of the remote support account. |
| Expiration | Displays the date and time when access to the remote account
                                          					 expires. |
| Passphrase | Displays the generated pass phrase. |
| Decode Version | Indicates the version of the decoder in use. |
| Delete button or icon | Deletes the remote access account information. |