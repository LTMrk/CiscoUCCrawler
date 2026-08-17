---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-install-upgrade-b-15cuciumg-b-14cuciumg-chapter-0100-html-0ea15d049b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/b_15cuciumg/b_14cuciumg_chapter_0100.html
retrieved_at: 2026-08-17T02:41:13.530692+00:00
---

Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15

# Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Maintaining Cisco Unity Connection Server

## Chapter: Maintaining Cisco Unity Connection Server

# Maintaining Cisco Unity Connection Server

## Migrating a
                        	 Physical Server to a Virtual Machine

Follow the given tasks to migrate from physical server to a
                           		virtual machine:

Backup the software component on the physical server. For more
                                 			 information, see the Backing
                                    				Up and Restoring Cisco Unity Connection Components chapter.

Download and deploy the OVA template to create a new virtual
                                 			 machine. For more information, see the Creating
                                    				a Virtual Machine section.

Migrating the Unity Connection server on the virtual machine.

To replace the publisher server, see the Replacing
                                          					 a Publisher Server section.

To replace the subscriber server, see the Replacing
                                          					 a Subscriber Server section.

If Unity Connection is installed as a standalone server, restore
                                 			 the software component from the physical server to the virtual machine for
                                 			 which you have taken the back up. For more information, see the Restoring
                                    				the Software Components on Unity Connection section.

(Optional) Install new languages on the replaced server if
                                 			 required or remove the existing languages already installed on the server. For
                                 			 more information, see the Adding
                                    				or Removing Unity Connection Languages section.

If you are deploying Unity Connection networking (Intersite, Intrasite, or HTTPS), see the Networking Guide for Cisco Unity
                                       Connection, Release 15, before replacing the Unity Connection server, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html .

### Replacing a
                           	 Publisher Server

While you are upgrading the publisher server in a Unity
                                 		  Connection cluster, the subscriber server continues to provide services to the
                                 		  users and callers.

In case of a standalone server, replace the server during
                                             			 off-peak hours to avoid call-processing interruptions and impact to services.

Step 1

Manually change the status of subscriber server to Primary:

Sign in to Cisco Unity Connection Serviceability.

Expand Tools and select Cluster Management.

On the Cluster Management page, from the Server Manager menu,
                                                				  locate the subscriber server and check the following:

If the subscriber server status is Primary, skip the remaining
                                                         						  steps in this procedure.

If the subscriber server status is Secondary, select Make
                                                         						  Primary.

If the subscriber has Deactivated status, change the status to
                                                         						  Secondary and then select Activate. When prompted to confirm changing the
                                                         						  server status, select OK. After successful activation of the subscriber server,
                                                         						  change the status to Primary selecting Make Primary option.

Step 2

Manually change the status of publisher server to Deactivated:

Sign in to the Real-Time Monitoring Tool and select Port
                                                				  Monitor.

In the Node field, select the publisher server and then select
                                                				  Start Polling. Note whether any voice messaging ports are currently handling
                                                				  calls for the server.

Return to the Cluster Management page of Cisco Unity Connection
                                                				  Serviceability and do any one of th following:

If no voice messaging ports are currently handling calls for the
                                                         						  publisher server, move to the next 3 .

If there are voice messaging ports that are currently handling
                                                         						  calls for the publisher server, on the Cluster Management page, in the Port
                                                         						  Manager column, select Stop Taking Calls for the publisher server and then wait
                                                         						  until RTMT shows that all the ports for the publisher server are idle.

From the Server Manager menu, in the Change Server Status column
                                                				  for the publisher server, select Deactivate and then select OK.

Step 3

Install the replacement publisher server, see Installing
                                             				the Publisher Server section.

Shut down the publisher server using the CLI command utils
                                                				  system shutdown. On the Cluster Management page of the subscriber server, the
                                                				  publisher has Not Functioning status.

Install the virtual machine. The following settings on the
                                                				  virtual machine must be same as that on the physical server, otherwise the
                                                				  transfer of data from the physical server to the virtual machine get failed:

Hostname of the server

IP address of the server

Time zone

NTP server

DHCP settings

Primary DNS settings

SMTP hostname

X.509 Certificate information (Organization, Unit, Location,
                                                         						  State, and Country).

Step 4

You must run the utils disaster_recovery prepare restore pub_from_sub CLI command on the publisher server. This command handles
                                          the tasks to prepare for restore of a publisher node from a subscriber node.

Step 5

Configure the cluster on the replaced publisher server:

Sign in to Cisco Unity Connection Administration on the
                                                				  publisher server.

Expand System Settings and select Cluster.

On the Find and List Servers page, select Add New.

On the New Server Configuration page, in the Hostname/IP Address
                                                				  field, enter the hostname or IP address of the subscriber server. Enter the
                                                				  description and select Save.

Step 6

If Unity Connection is installed as a cluster, you can restore
                                          			 the publisher using the subscriber data.

Run the utils cuc cluster renegotiate CLI command on the
                                                				  subscriber server. The publisher automatically restarts after running this
                                                				  command.

Run the show cuc cluster status CLI command on the subscriber
                                                				  server to confirm that the new Unity Connection cluster is configured
                                                				  correctly.

If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html .

### Replacing a
                           	 Subscriber Server

While you are upgrading the subscriber server in a Unity
                                 		  Connection cluster, the publisher server continues to provide services to users
                                 		  and callers.

Step 1

Manually change the status of publisher server to Primary:

Sign in to Cisco Unity Connection Serviceability.

Expand Tools and select Cluster Management.

On the Cluster Management page, from the Server Manager menu,
                                                				  locate the publisher server and check the following:

If the publisher server status is Primary, skip the remaining
                                                         						  steps in this procedure.

If the publisher server status is Secondary, change the status
                                                         						  by selecting Make Primary.

If the publisher has Deactivated status, change the status to
                                                         						  Secondary and select Activate. A prompt appears to confirm the changing of the
                                                         						  server status, select OK. After successful activation of the publisher server,
                                                         						  change the status to Primary by selecting Make Primary option.

Step 2

Manually change the status of subscriber server to Deactivated:

Sign in to the Real-Time Monitoring Tool, expand <Unity
                                                				  Connection> option and select Port Monitor.

In the Node field, select the subscriber server and select Start
                                                				  Polling. Note whether any voice messaging ports are currently handling calls
                                                				  for the server.

Return to the Cluster Management page of Cisco Unity Connection
                                                				  Serviceability.

If no voice messaging ports are currently handling calls for the
                                                         						  server, skip to the next step.

If there are voice messaging ports that are currently handling
                                                         						  calls for the subscriber server, on the Cluster Management page, in the Change
                                                         						  Port Status column, select Stop Taking Calls for the subscriber server and then
                                                         						  wait until RTMT shows that all ports for the server are idle.

From the Server Manager menu, in the Change Server Status column
                                                				  for the subscriber server, select Deactivate and select OK.

Step 3

Make sure that the hostname or IP address of the subscriber
                                          			 server is configured correctly on the publisher server as mentioned in 4 of replacing a publisher server.

Step 4

Install the replaced subscriber server, see Installing
                                             				the Publisher Server section.

Shut down the subscriber server using the CLI command utils
                                                				  system shutdown. On the Cluster Management page of the publisher server, the
                                                				  subscriber has Not Functioning status.

Reinstall the Unity Connection server. You must specify the same
                                                				  security password of the subscriber server that you are replacing and it should
                                                				  also match the security password for the publisher server. Otherwise, the Unity
                                                				  Connection cluster do not function. If you do not know the security password,
                                                				  you can change it on the publisher server before you install the subscriber
                                                				  server using the CLI command set password user.

Step 5

Check the cluster status by running the show cuc cluster status
                                          			 CLI command on the subscriber server.

If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html .

## Replacing the
                        	 Non-Functional Server

Replacing the Non-Functional Server

Tasks

If Unity Connection is installed as standalone.

Recreate the virtual
                                                							 machine. For more information, see the Creating a Virtual Machine section.

Restore the software. For
                                                							 more information, see the Restoring the Software Components on Unity
                                                   								Connection section.

If Unity Connection is installed as a cluster and publisher is
                                          						not functioning.

Recreate the virtual
                                                							 machine. For more information, see the Creating a Virtual Machine section.

Replace the Publisher
                                                							 server, see the Replacing a Publisher Server section.

If Unity Connection is installed as a cluster and subscriber is
                                          						not functioning.

Install the subscriber server, see the Installing the Subscriber Server section.

If both the servers are not functioning in a cluster.

Replace the publisher
                                                							 server, see Installing the Publisher Server section.

Restore the software
                                                							 components on the physical machine. For more information, see the Restoring the Software Components on Unity
                                                   								Connection section.

Configure cluster on the
                                                							 publisher sever:

Replace the subscriber
                                                      								  server, see the Installing the Subscriber Server section.

Check the cluster status
                                                      								  using CLI command show cuc cluster status.

Synchronize MWIs on each
                                                      								  phone system.

## Changing the IP
                        	 Address or Hostname of a Unity Connection Server

Before changing the IP address of a standalone Unity Connection
                           		server or a cluster, you need to determine whether the server is defined by
                           		hostname or IP address.

You can also use Cisco Prime Collaboration Deployment for
                                       		  readdressing. For more information on Cisco PCD, see http://www.cisco.com/c/en/us/products/cloud-systems-management/prime-collaboration/index.html .

### Determine Whether
                           	 Unity Connection is Defined by Hostname or IP Address

Step 1

Sign in to Cisco Unity Connection Administration of the server
                                          			 of which the IP address needs to be changed.

Step 2

Expand System Settings and select Cluster.

You need to select Cluster even if you want to change the IP
                                                         				  address or hostname of a standalone server.

Step 3

Select Find to
                                          			 locate the server of which you need to change the IP address or hostname:

If the value of the Hostname/IP Address column is a hostname,
                                                   					 the server is defined by a hostname.

If the value of the Hostname/IP Address column is an IP address,
                                                   					 the server is defined by an IP address.

### Important
                           	 Considerations before Changing the Hostname or IP Address of a Unity Connection
                           	 Server

When you change the IP address or hostname of the Unity
                                    			 Connection server, make sure to apply the same changes on all the associated
                                    			 components that refer the Unity Connection server by IP address or hostname:

Bookmarks on client computers to the following web applications:

Web applications, such as Cisco Personal Communications
                                          				  Assistant and Cisco Unity Connection Administration.

Cisco Fax Server

Cisco Unified Application Environment

Cisco Unified Mobile Advantage

Cisco Unified Presence

Cisco Unified Personal Communicator

Cisco Unity Connection ViewMail for Microsoft Outlook

IMAP email clients that access Unity Connection

Phone systems and related components, including Cisco EGW 2200,
                                          				  Cisco ISR voice gateway, Cisco SIP Proxy Server, Cisco Unified Communications
                                          				  Manager, Cisco Unified Communications Manager Express, and PIMG/TIMG units.

RSS readers

SMTP smart host

Voice messaging systems with which Unity Connection is
                                          				  integrated via VPIM, such as Cisco Unity and Cisco Unity Express.

Caution

If associated components reference the Unity Connection server
                                                      					 by IP address and if you do not change the IP address as applicable, the
                                                      					 components are no longer be able to access Unity Connection.

You can change the IP address and hostname of a Unity Connection
                                    			 server or cluster following the steps mentioned in the Changing the IP Address or Hostname of a Unity
                                       				Connection Server or Cluster section.

Caution

Do not change the IP address or hostname of a Unity Connection
                                                				server during business hours.

(Only in case of changing IP address of a Unity Connection
                                    			 server) If the Unity Connection server is configured to get an IP address from
                                    			 a DHCP server, you cannot manually change the IP address of the server.
                                    			 Instead, you must do one of the following:

Change DHCP/DNS settings from Cisco Unified Operating System
                                          				  Administration> Settings and select the applicable option from IP, and
                                          				  restart Unity Connection by running the CLI command utils system restart.

Disable DHCP on Unity Connection by running the CLI command set
                                          				  network dhcp and then manually change the IP address by doing the procedure
                                          				  given below.

To change the IP address or hostname of a Unity Connection
                                          		  cluster, follow the steps mentioned in the Changing the IP Address or Hostname of a Unity
                                             			 Connection Server section first on the publisher server and then on the
                                          		  subscriber server.

### Changing the IP
                           	 Address or Hostname of a Unity Connection Server or Cluster

We can also change IP Address or Hostname of Cisco Unity Connection standalone node or cluster using CLI . For more information
                                             on CLI usage see https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-command-reference-list.html .

Do the following steps to change the IP address or Hostname of a standalone server or a cluster defined by hostname or IP
                                 address using GUI. In case of a cluster, follow the steps first on the publisher server and then on the subscriber server.

Step 1

Sign in to the standalone server or the publisher server using Real-Time Monitoring Tool. Expand Tools> Alert and select Alert
                                          Central. In the Systems tab, make sure the ServerDown is black. If ServerDown is red, then resolve all the problems and change
                                          it to black.

Step 2

Check the server status:

Sign in to Cisco Unity Connection Serviceability.

Expand Tools and select Cluster Management.

On the Cluster Management page, check whether server status is
                                                				  Primary or Secondary. If there is any other status value then resolve the
                                                				  problem.

Step 3

Check the network connectivity and DNS server configuration by
                                          			 running the utils diagnose module validate_network CLI command.

Step 4

Backup the database using Disaster Recovery System. See the Backing
                                             				Up and Restoring Cisco Unity Connection Components chapter.

Step 5

If intrasite, HTTPS, and SRSV networking is configured, remove the server from the Unity Connection site. For instructions,
                                          see the Networking Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html .

Caution

Re-adding a server to a Unity Connection site can be a time consuming process.

Step 6

On a DNS server, change the DNS record of the Unity Connection
                                          			 server to the new IP address. Update both the forward (A) and reverse (PTR)
                                          			 records.

Step 7

(Applicable only when you change the IP address or Hostname of a standalone server or a cluster defined by an IP address or
                                             Hostname) Changing the IP addresses or Hostname of a standalone server or the publisher server in Connection Administration:

Sign in to Cisco Unity Connection Administration.

Caution

In case of a cluster, you must sign in to the publisher sever and select subscriber server to change the IP address or Hostname
                                                               of a subscriber server.

Expand System Settings, and select Cluster.

Select Find to display a list of servers in the cluster.

Select the name of the standalone server or publisher server.

Change the value of the Hostname/IP Address field to the new Hostname/IP address.

Select Save.

Step 8

On the standalone or publisher server, change the IP address, Hostname, and default gateway (if applicable):

Sign in to Cisco Unified Operating System Administration.

From the Settings menu, select IP > Ethernet .

In the Host Information, enter the value of Hostname.

If you want an alternate hostname for the server, run the set web-security CLI command. In the Hostname, change the hostname of the server.

For more information on the CLI commands, see the applicable version of the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

Enter a certificate signing request. Then download the certificate signing request to the server on which you installed Microsoft
                                                               Certificate Services or another application that issues certificates, or download the request to a server that you can use
                                                               to send the certificate signing request to an external certification authority (CA).

(In case of SSL certificates created and installed on renamed server) Upload the root certificate and the server certificate
                                                               to the standalone or publisher server. Follow the steps as mentioned in Security Guide for Cisco Unity Connection Release
                                                               15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html .

In the Port Information, change the value of the IP Address and Subnet Mask field (if applicable).

If you are moving the server to a different subnet that requires a new default gateway address, change the value of the Default
                                                Gateway field in the Gateway Information.

Select Save.

Caution

After saving the page, node services will restart automatically. Restarting services ensures the proper update for the changes
                                                         to take effect. Do not perform any action on the server until the services are up and running. To check the status of the
                                                         services, run utils service list CLI command.

Step 9

If you change the IP address or Hostname of a standalone server, skip to Step 10 .

Sign in to Cisco Unified Operating System Administration.

From the Settings menu, select IP > Publisher.

Change the IP address of the publisher server.

Select Save.

Step 10

Sign in to
                                          			 Real-Time Monitoring Tool and confirm that the server is available and running.

Step 11

For the cluster, repeat Step 1 to Step 9 on subscriber server also.

## Adding or Removing
                        	 Unity Connection Languages

After installing a new server or on an existing server, you may
                           		need to add some new language(s) and remove some already installed languages
                           		depending on the user requirement.

Languages are not licensed and Unity Connection 15 does not enforce a limit on the number of languages you can install and
                                       use. However, the more languages you install, the less hard disk space is available for storing voice messages.

### Task List for
                           	 Adding Languages to a Standalone Unity Connection Server

Do the following tasks to download and install
                              		languages in addition to English (United States):

Download the Unity Connection languages that you want to install
                                    			 and do the following steps:

Sign in as a registered user on the following Cisco.com link: http://tools.cisco.com/support/downloads/pub/Redirect.x?mdfid=278875240 .

Expand Unified Communications Applications > Voicemail and Unified
                                             					 Messaging > Cisco Unity Connection , and select the applicable Unity
                                          				  Connection version.

On the Select a Software Type page, select Cisco Unity Connection Locale Installer .

On the Select a Release page, select the applicable Unity
                                          				  Connection version. The download links for the languages appear on the right
                                          				  side of the page.

Select the name of a file to download. On the Download Image
                                          				  page, note down the MD5 value and follow the on screen prompts to complete the
                                          				  download.

Make sure that the MD5 checksum matches the checksum that is
                                                      					 listed on Cisco.com. If the values do not match, the downloaded file is
                                                      					 damaged. Do not attempt to use a damaged file to install software as the
                                                      					 results is unpredictable. If the MD5 values do not match, download the file
                                                      					 again until the value for the downloaded file matches the value listed on
                                                      					 Cisco.com.

(Unity Connection cluster only) Make sure that the subscriber
                                    			 server status is Primary and the publisher server status is Secondary in order
                                    			 to install the Unity Connection languages. Follow the given steps:

Sign in to Cisco Unity Connection Serviceability.

Expand Tools and select Cluster Management.

For subscriber server, select Make Primary.

- On the standalone or
                                 		  publisher server, install the Unity Connection languages that you downloaded.
                                 		  Refer Installing
                                    			 Unity Connection Language Files from Network Location or Remote Server for more details.

If you are using additional languages because you want the Cisco
                                    			 Personal Communications Assistant to be localized: Download and install the
                                    			 corresponding Unity Connection locales on the publisher server.

(Unity Connection cluster only) Change the publisher server
                                    			 status to Primary and follow the same steps on subscriber server to install the
                                    			 same Unity Connection languages that were installed on publisher server.

### Installing Unity Connection Language Files from Network Location or
                           	 Remote Server

In this procedure, do not use the web browser controls (for example,
                                 		  Refresh/Reload) while accessing Cisco Unified Operating System Administration.
                                 		  However, you can use the navigation controls in the administration interface.

Step 1

Stop the Connection Conversation Manager and Connection Mixer
                                          			 services:

Sign in to Cisco Unity Connection Serviceability. Expand Tools
                                                				  menu and select Service Management .

In Critical Services, for the Connection Conversation Manager
                                                				  row, select Stop .

Wait for the service to stop.

In the Critical Services menu, in the Connection Mixer row,
                                                				  select Stop .

Wait for the service to stop.

Step 2

Sign in to Cisco Unified Operating System Administration.

Step 3

From the Software Upgrades menu, select Install/Upgrade . The
                                          			 Software Installation/Upgrade window appears.

Step 4

In the Source list, select Remote Filesystem .

Step 5

In the Directory field, enter the path of the folder that contains
                                          			 the language file on the remote system.

If the language file is located on a Linux
                                             				or Unix server, you must enter a forward slash at the beginning of the folder
                                             				path. (For example, if the language file is in the languages folder, you must
                                             				enter /languages .)

If the language file is located on a Windows
                                             				server, make sure that you are connecting to an FTP or SFTP server, and use the
                                             				appropriate syntax:

Begin the path with a forward slash (/)
                                                   					 and use forward slashes throughout the path.

The path must start from the FTP or SFTP
                                                   					 root folder on the server, so you cannot enter a Windows absolute path, which
                                                   					 starts with a drive letter (for example, C:).

Step 6

In the Server field, enter the
                                          			 server name or IP address.

Step 7

In the User Name field, enter
                                          			 your user name on the remote server.

Step 8

In the User Password field,
                                          			 enter your password on the remote server.

Step 9

In the Transfer Protocol list,
                                          			 select the applicable option.

Step 10

Select Next .

Step 11

Select the language that you want to install, and select Next .

Step 12

Monitor the progress of the download.

If you loose your connection with the server or close your browser
                                             				during the installation process, you may see the following message when you try
                                             				to access the Software Upgrades menu again:

Warning: Another session is installing
                                             				software, click Assume Control to take over the installation.

If you are sure you want to take over the
                                             				session, select Assume Control .

Step 13

If you want to install another
                                             				language, ct Install Another , and
                                          			 repeat all the above steps

Step 14

If you are finished with installing
                                             				languages: Restart the services:

Sign in to Cisco Unity Connection
                                                   					 Serviceability.

Expand Tools menu and select Service Management .

In the Critical Services menu, in the
                                                   					 Connection Conversation Manager row, select Start . Wait for the service to
                                                   					 start.

In the Critical Services menu, in the
                                                   					 Connection Mixer row, select Start . Wait for the service to
                                                   					 start.

## Removing Unity
                        	 Connection Language Files

Step 1

Sign in to
                                       			 the command line interface as a platform administrator.

Make sure to stop Connection Conversation Manager and Connection
                                                      				  Mixer services before uninstalling the languages.

Step 2

Run the show cuc locales CLI command to display a list of installed language
                                       			 files.

Step 3

In the command
                                       			 results, find the language that you want to remove, and note the value of the
                                       			 Locale column for the language.

Step 4

Run the delete cuc locale <code > CLI command to remove the language, where
                                       			 <code> is the value of the Locale column that you get in Step 3 .

When the command completes, the following information appears:

<code>
                                          				uninstalled

| Note | If you are deploying Unity Connection networking (Intersite, Intrasite, or HTTPS), see the Networking Guide for Cisco Unity
                                       Connection, Release 15, before replacing the Unity Connection server, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html . |
|---|---|

| Note | In case of a standalone server, replace the server during
                                             			 off-peak hours to avoid call-processing interruptions and impact to services. |
|---|---|

| Step 1 | Manually change the status of subscriber server to Primary: Sign in to Cisco Unity Connection Serviceability. Expand Tools and select Cluster Management. On the Cluster Management page, from the Server Manager menu,
                                                				  locate the subscriber server and check the following: If the subscriber server status is Primary, skip the remaining
                                                         						  steps in this procedure. If the subscriber server status is Secondary, select Make
                                                         						  Primary. If the subscriber has Deactivated status, change the status to
                                                         						  Secondary and then select Activate. When prompted to confirm changing the
                                                         						  server status, select OK. After successful activation of the subscriber server,
                                                         						  change the status to Primary selecting Make Primary option. |
|---|---|
| Step 2 | Manually change the status of publisher server to Deactivated: Sign in to the Real-Time Monitoring Tool and select Port
                                                				  Monitor. In the Node field, select the publisher server and then select
                                                				  Start Polling. Note whether any voice messaging ports are currently handling
                                                				  calls for the server. Return to the Cluster Management page of Cisco Unity Connection
                                                				  Serviceability and do any one of th following: If no voice messaging ports are currently handling calls for the
                                                         						  publisher server, move to the next 3 . If there are voice messaging ports that are currently handling
                                                         						  calls for the publisher server, on the Cluster Management page, in the Port
                                                         						  Manager column, select Stop Taking Calls for the publisher server and then wait
                                                         						  until RTMT shows that all the ports for the publisher server are idle. From the Server Manager menu, in the Change Server Status column
                                                				  for the publisher server, select Deactivate and then select OK. |
| Step 3 | Install the replacement publisher server, see Installing
                                             				the Publisher Server section. Shut down the publisher server using the CLI command utils
                                                				  system shutdown. On the Cluster Management page of the subscriber server, the
                                                				  publisher has Not Functioning status. Install the virtual machine. The following settings on the
                                                				  virtual machine must be same as that on the physical server, otherwise the
                                                				  transfer of data from the physical server to the virtual machine get failed: Hostname of the server IP address of the server Time zone NTP server DHCP settings Primary DNS settings SMTP hostname X.509 Certificate information (Organization, Unit, Location,
                                                         						  State, and Country). |
| Step 4 | You must run the utils disaster_recovery prepare restore pub_from_sub CLI command on the publisher server. This command handles
                                          the tasks to prepare for restore of a publisher node from a subscriber node. |
| Step 5 | Configure the cluster on the replaced publisher server: Sign in to Cisco Unity Connection Administration on the
                                                				  publisher server. Expand System Settings and select Cluster. On the Find and List Servers page, select Add New. On the New Server Configuration page, in the Hostname/IP Address
                                                				  field, enter the hostname or IP address of the subscriber server. Enter the
                                                				  description and select Save. |
| Step 6 | If Unity Connection is installed as a cluster, you can restore
                                          			 the publisher using the subscriber data. Run the utils cuc cluster renegotiate CLI command on the
                                                				  subscriber server. The publisher automatically restarts after running this
                                                				  command. Run the show cuc cluster status CLI command on the subscriber
                                                				  server to confirm that the new Unity Connection cluster is configured
                                                				  correctly. Note If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html . | Note | If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html . |
| Note | If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html . |

| Note | If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html . |
|---|---|

| Step 1 | Manually change the status of publisher server to Primary: Sign in to Cisco Unity Connection Serviceability. Expand Tools and select Cluster Management. On the Cluster Management page, from the Server Manager menu,
                                                				  locate the publisher server and check the following: If the publisher server status is Primary, skip the remaining
                                                         						  steps in this procedure. If the publisher server status is Secondary, change the status
                                                         						  by selecting Make Primary. If the publisher has Deactivated status, change the status to
                                                         						  Secondary and select Activate. A prompt appears to confirm the changing of the
                                                         						  server status, select OK. After successful activation of the publisher server,
                                                         						  change the status to Primary by selecting Make Primary option. |
|---|---|
| Step 2 | Manually change the status of subscriber server to Deactivated: Sign in to the Real-Time Monitoring Tool, expand <Unity
                                                				  Connection> option and select Port Monitor. In the Node field, select the subscriber server and select Start
                                                				  Polling. Note whether any voice messaging ports are currently handling calls
                                                				  for the server. Return to the Cluster Management page of Cisco Unity Connection
                                                				  Serviceability. If no voice messaging ports are currently handling calls for the
                                                         						  server, skip to the next step. If there are voice messaging ports that are currently handling
                                                         						  calls for the subscriber server, on the Cluster Management page, in the Change
                                                         						  Port Status column, select Stop Taking Calls for the subscriber server and then
                                                         						  wait until RTMT shows that all ports for the server are idle. From the Server Manager menu, in the Change Server Status column
                                                				  for the subscriber server, select Deactivate and select OK. |
| Step 3 | Make sure that the hostname or IP address of the subscriber
                                          			 server is configured correctly on the publisher server as mentioned in 4 of replacing a publisher server. |
| Step 4 | Install the replaced subscriber server, see Installing
                                             				the Publisher Server section. Shut down the subscriber server using the CLI command utils
                                                				  system shutdown. On the Cluster Management page of the publisher server, the
                                                				  subscriber has Not Functioning status. Reinstall the Unity Connection server. You must specify the same
                                                				  security password of the subscriber server that you are replacing and it should
                                                				  also match the security password for the publisher server. Otherwise, the Unity
                                                				  Connection cluster do not function. If you do not know the security password,
                                                				  you can change it on the publisher server before you install the subscriber
                                                				  server using the CLI command set password user. |
| Step 5 | Check the cluster status by running the show cuc cluster status
                                          			 CLI command on the subscriber server. Note If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html . | Note | If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html . |
| Note | If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html . |

| Note | If third-party certificates are deployed in Unity Connection then after successfully replacing the publisher server, you must
                                                         reconfigure third party certificates for the newly build publisher server. For information on how to configure the certificates,
                                                         see Security chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html . |
|---|---|

| Tasks | Procedure |
|---|---|
| If Unity Connection is installed as standalone. | Recreate the virtual
                                                							 machine. For more information, see the Creating a Virtual Machine section. Restore the software. For
                                                							 more information, see the Restoring the Software Components on Unity
                                                   								Connection section. |
| If Unity Connection is installed as a cluster and publisher is
                                          						not functioning. | Recreate the virtual
                                                							 machine. For more information, see the Creating a Virtual Machine section. Replace the Publisher
                                                							 server, see the Replacing a Publisher Server section. |
| If Unity Connection is installed as a cluster and subscriber is
                                          						not functioning. | Install the subscriber server, see the Installing the Subscriber Server section. |
| If both the servers are not functioning in a cluster. | Replace the publisher
                                                							 server, see Installing the Publisher Server section. Restore the software
                                                							 components on the physical machine. For more information, see the Restoring the Software Components on Unity
                                                   								Connection section. Configure cluster on the
                                                							 publisher sever: Replace the subscriber
                                                      								  server, see the Installing the Subscriber Server section. Check the cluster status
                                                      								  using CLI command show cuc cluster status. Synchronize MWIs on each
                                                      								  phone system. |

| Note | You can also use Cisco Prime Collaboration Deployment for
                                       		  readdressing. For more information on Cisco PCD, see http://www.cisco.com/c/en/us/products/cloud-systems-management/prime-collaboration/index.html . |
|---|---|

| Step 1 | Sign in to Cisco Unity Connection Administration of the server
                                          			 of which the IP address needs to be changed. |
|---|---|
| Step 2 | Expand System Settings and select Cluster. Note You need to select Cluster even if you want to change the IP
                                                         				  address or hostname of a standalone server. | Note | You need to select Cluster even if you want to change the IP
                                                         				  address or hostname of a standalone server. |
| Note | You need to select Cluster even if you want to change the IP
                                                         				  address or hostname of a standalone server. |
| Step 3 | Select Find to
                                          			 locate the server of which you need to change the IP address or hostname: If the value of the Hostname/IP Address column is a hostname,
                                                   					 the server is defined by a hostname. If the value of the Hostname/IP Address column is an IP address,
                                                   					 the server is defined by an IP address. |

| Note | You need to select Cluster even if you want to change the IP
                                                         				  address or hostname of a standalone server. |
|---|---|

| Caution | If associated components reference the Unity Connection server
                                                      					 by IP address and if you do not change the IP address as applicable, the
                                                      					 components are no longer be able to access Unity Connection. |
|---|---|

| Caution | Do not change the IP address or hostname of a Unity Connection
                                                				server during business hours. |
|---|---|

| Note | To change the IP address or hostname of a Unity Connection
                                          		  cluster, follow the steps mentioned in the Changing the IP Address or Hostname of a Unity
                                             			 Connection Server section first on the publisher server and then on the
                                          		  subscriber server. |
|---|---|

| Note | We can also change IP Address or Hostname of Cisco Unity Connection standalone node or cluster using CLI . For more information
                                             on CLI usage see https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-command-reference-list.html . |
|---|---|

| Step 1 | Sign in to the standalone server or the publisher server using Real-Time Monitoring Tool. Expand Tools> Alert and select Alert
                                          Central. In the Systems tab, make sure the ServerDown is black. If ServerDown is red, then resolve all the problems and change
                                          it to black. |
|---|---|
| Step 2 | Check the server status: Sign in to Cisco Unity Connection Serviceability. Expand Tools and select Cluster Management. On the Cluster Management page, check whether server status is
                                                				  Primary or Secondary. If there is any other status value then resolve the
                                                				  problem. |
| Step 3 | Check the network connectivity and DNS server configuration by
                                          			 running the utils diagnose module validate_network CLI command. |
| Step 4 | Backup the database using Disaster Recovery System. See the Backing
                                             				Up and Restoring Cisco Unity Connection Components chapter. |
| Step 5 | If intrasite, HTTPS, and SRSV networking is configured, remove the server from the Unity Connection site. For instructions,
                                          see the Networking Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html . Caution Re-adding a server to a Unity Connection site can be a time consuming process. | Caution | Re-adding a server to a Unity Connection site can be a time consuming process. |
| Caution | Re-adding a server to a Unity Connection site can be a time consuming process. |
| Step 6 | On a DNS server, change the DNS record of the Unity Connection
                                          			 server to the new IP address. Update both the forward (A) and reverse (PTR)
                                          			 records. |
| Step 7 | (Applicable only when you change the IP address or Hostname of a standalone server or a cluster defined by an IP address or
                                             Hostname) Changing the IP addresses or Hostname of a standalone server or the publisher server in Connection Administration: Sign in to Cisco Unity Connection Administration. Caution In case of a cluster, you must sign in to the publisher sever and select subscriber server to change the IP address or Hostname
                                                               of a subscriber server. Expand System Settings, and select Cluster. Select Find to display a list of servers in the cluster. Select the name of the standalone server or publisher server. Change the value of the Hostname/IP Address field to the new Hostname/IP address. Select Save. | Caution | In case of a cluster, you must sign in to the publisher sever and select subscriber server to change the IP address or Hostname
                                                               of a subscriber server. |
| Caution | In case of a cluster, you must sign in to the publisher sever and select subscriber server to change the IP address or Hostname
                                                               of a subscriber server. |
| Step 8 | On the standalone or publisher server, change the IP address, Hostname, and default gateway (if applicable): Sign in to Cisco Unified Operating System Administration. From the Settings menu, select IP > Ethernet . In the Host Information, enter the value of Hostname. If you want an alternate hostname for the server, run the set web-security CLI command. In the Hostname, change the hostname of the server. For more information on the CLI commands, see the applicable version of the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . Note Enter a certificate signing request. Then download the certificate signing request to the server on which you installed Microsoft
                                                               Certificate Services or another application that issues certificates, or download the request to a server that you can use
                                                               to send the certificate signing request to an external certification authority (CA). (In case of SSL certificates created and installed on renamed server) Upload the root certificate and the server certificate
                                                               to the standalone or publisher server. Follow the steps as mentioned in Security Guide for Cisco Unity Connection Release
                                                               15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html . In the Port Information, change the value of the IP Address and Subnet Mask field (if applicable). If you are moving the server to a different subnet that requires a new default gateway address, change the value of the Default
                                                Gateway field in the Gateway Information. Select Save. Caution After saving the page, node services will restart automatically. Restarting services ensures the proper update for the changes
                                                         to take effect. Do not perform any action on the server until the services are up and running. To check the status of the
                                                         services, run utils service list CLI command. | Note | Enter a certificate signing request. Then download the certificate signing request to the server on which you installed Microsoft
                                                               Certificate Services or another application that issues certificates, or download the request to a server that you can use
                                                               to send the certificate signing request to an external certification authority (CA). (In case of SSL certificates created and installed on renamed server) Upload the root certificate and the server certificate
                                                               to the standalone or publisher server. Follow the steps as mentioned in Security Guide for Cisco Unity Connection Release
                                                               15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html . | Caution | After saving the page, node services will restart automatically. Restarting services ensures the proper update for the changes
                                                         to take effect. Do not perform any action on the server until the services are up and running. To check the status of the
                                                         services, run utils service list CLI command. |
| Note | Enter a certificate signing request. Then download the certificate signing request to the server on which you installed Microsoft
                                                               Certificate Services or another application that issues certificates, or download the request to a server that you can use
                                                               to send the certificate signing request to an external certification authority (CA). (In case of SSL certificates created and installed on renamed server) Upload the root certificate and the server certificate
                                                               to the standalone or publisher server. Follow the steps as mentioned in Security Guide for Cisco Unity Connection Release
                                                               15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html . |
| Caution | After saving the page, node services will restart automatically. Restarting services ensures the proper update for the changes
                                                         to take effect. Do not perform any action on the server until the services are up and running. To check the status of the
                                                         services, run utils service list CLI command. |
| Step 9 | If you change the IP address or Hostname of a standalone server, skip to Step 10 . (Applicable only when you change the IP address or Hostname of a publisher server in case of a cluster) On the subscriber server, change the IP address of the publisher server: Sign in to Cisco Unified Operating System Administration. From the Settings menu, select IP > Publisher. Change the IP address of the publisher server. Select Save. |
| Step 10 | Sign in to
                                          			 Real-Time Monitoring Tool and confirm that the server is available and running. This
                                          			 completes the process of changing the IP address of the standalone server. |
| Step 11 | For the cluster, repeat Step 1 to Step 9 on subscriber server also. This completes the process of changing the IP address of a cluster. |

| Caution | Re-adding a server to a Unity Connection site can be a time consuming process. |
|---|---|

| Caution | In case of a cluster, you must sign in to the publisher sever and select subscriber server to change the IP address or Hostname
                                                               of a subscriber server. |
|---|---|

| Note | Enter a certificate signing request. Then download the certificate signing request to the server on which you installed Microsoft
                                                               Certificate Services or another application that issues certificates, or download the request to a server that you can use
                                                               to send the certificate signing request to an external certification authority (CA). (In case of SSL certificates created and installed on renamed server) Upload the root certificate and the server certificate
                                                               to the standalone or publisher server. Follow the steps as mentioned in Security Guide for Cisco Unity Connection Release
                                                               15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html . |
|---|---|

| Caution | After saving the page, node services will restart automatically. Restarting services ensures the proper update for the changes
                                                         to take effect. Do not perform any action on the server until the services are up and running. To check the status of the
                                                         services, run utils service list CLI command. |
|---|---|

| Note | Languages are not licensed and Unity Connection 15 does not enforce a limit on the number of languages you can install and
                                       use. However, the more languages you install, the less hard disk space is available for storing voice messages. |
|---|---|

| Note | Make sure that the MD5 checksum matches the checksum that is
                                                      					 listed on Cisco.com. If the values do not match, the downloaded file is
                                                      					 damaged. Do not attempt to use a damaged file to install software as the
                                                      					 results is unpredictable. If the MD5 values do not match, download the file
                                                      					 again until the value for the downloaded file matches the value listed on
                                                      					 Cisco.com. |
|---|---|

| Step 1 | Stop the Connection Conversation Manager and Connection Mixer
                                          			 services: Sign in to Cisco Unity Connection Serviceability. Expand Tools
                                                				  menu and select Service Management . In Critical Services, for the Connection Conversation Manager
                                                				  row, select Stop . Wait for the service to stop. In the Critical Services menu, in the Connection Mixer row,
                                                				  select Stop . Wait for the service to stop. |
|---|---|
| Step 2 | Sign in to Cisco Unified Operating System Administration. |
| Step 3 | From the Software Upgrades menu, select Install/Upgrade . The
                                          			 Software Installation/Upgrade window appears. |
| Step 4 | In the Source list, select Remote Filesystem . |
| Step 5 | In the Directory field, enter the path of the folder that contains
                                          			 the language file on the remote system. If the language file is located on a Linux
                                             				or Unix server, you must enter a forward slash at the beginning of the folder
                                             				path. (For example, if the language file is in the languages folder, you must
                                             				enter /languages .) If the language file is located on a Windows
                                             				server, make sure that you are connecting to an FTP or SFTP server, and use the
                                             				appropriate syntax: Begin the path with a forward slash (/)
                                                   					 and use forward slashes throughout the path. The path must start from the FTP or SFTP
                                                   					 root folder on the server, so you cannot enter a Windows absolute path, which
                                                   					 starts with a drive letter (for example, C:). |
| Step 6 | In the Server field, enter the
                                          			 server name or IP address. |
| Step 7 | In the User Name field, enter
                                          			 your user name on the remote server. |
| Step 8 | In the User Password field,
                                          			 enter your password on the remote server. |
| Step 9 | In the Transfer Protocol list,
                                          			 select the applicable option. |
| Step 10 | Select Next . |
| Step 11 | Select the language that you want to install, and select Next . |
| Step 12 | Monitor the progress of the download. If you loose your connection with the server or close your browser
                                             				during the installation process, you may see the following message when you try
                                             				to access the Software Upgrades menu again: Warning: Another session is installing
                                             				software, click Assume Control to take over the installation. If you are sure you want to take over the
                                             				session, select Assume Control . |
| Step 13 | If you want to install another
                                             				language, ct Install Another , and
                                          			 repeat all the above steps |
| Step 14 | If you are finished with installing
                                             				languages: Restart the services: Sign in to Cisco Unity Connection
                                                   					 Serviceability. Expand Tools menu and select Service Management . In the Critical Services menu, in the
                                                   					 Connection Conversation Manager row, select Start . Wait for the service to
                                                   					 start. In the Critical Services menu, in the
                                                   					 Connection Mixer row, select Start . Wait for the service to
                                                   					 start. |

| Step 1 | Sign in to
                                       			 the command line interface as a platform administrator. Note Make sure to stop Connection Conversation Manager and Connection
                                                      				  Mixer services before uninstalling the languages. | Note | Make sure to stop Connection Conversation Manager and Connection
                                                      				  Mixer services before uninstalling the languages. |
|---|---|---|---|
| Note | Make sure to stop Connection Conversation Manager and Connection
                                                      				  Mixer services before uninstalling the languages. |
| Step 2 | Run the show cuc locales CLI command to display a list of installed language
                                       			 files. |
| Step 3 | In the command
                                       			 results, find the language that you want to remove, and note the value of the
                                       			 Locale column for the language. |
| Step 4 | Run the delete cuc locale <code > CLI command to remove the language, where
                                       			 <code> is the value of the Locale column that you get in Step 3 . When the command completes, the following information appears: <code>
                                          				uninstalled |

| Note | Make sure to stop Connection Conversation Manager and Connection
                                                      				  Mixer services before uninstalling the languages. |
|---|---|