---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-7-cjab-b-deploy-jabber-webex-messenger-127-cjab-b-deploy-jabber-we-28312ca13e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_7/cjab_b_deploy-jabber-webex-messenger-127/cjab_b_deploy-jabber-webex-messenger-127_chapter_0100.html
retrieved_at: 2026-08-21T21:04:56.340752+00:00
---

Webex Messenger Deployment for Cisco Jabber 12.7

# Webex Messenger Deployment for Cisco Jabber 12.7

Updated: April 1, 2024

Chapter: Configure Clusters

## Chapter: Configure Clusters

- Configure Clusters

- Configure Visual Voicemail

- Configure Cisco Unified Communications Manager Integration

# Configure Clusters

## Configure Visual Voicemail

Step 1

To configure Visual Voicemail, select the Configuration
                                             				  tab > Unified Communications .

Step 2

Select Voicemail to open the Default settings for Visual Voicemail for CUCI screen.

Unity Connection customers should enter the Unity Connection
                                          				server IP Address or DNS name into the "Voicemail Server" and "Mailstore
                                          				Server" fields. It is recommended that all other settings remain as the
                                          				defaults.

Step 3

To enable Visual Voicemail, select Enable Visual Voicemail .

Step 4

If you want to manually enter the Visual Voicemail settings,
                                       			 select Allow user to enter manual settings .

Step 5

Enter the following information:

Voicemail Server : Name of the Visual Voicemail server with which the Webex application should communicate for retrieving voicemail.

Voicemail
                                                					 Protocol : Protocol used for communicating with the Visual Voicemail
                                             				  server. You can select HTTPS or HTTP.

Voicemail Port :
                                             				  Port associated with the Visual Voicemail server.

The following Mailstore parameter options are not supported. The Webex Administration tool requires values, enter 10.0.0.0 as the Mailstore Server and use the default values for the remaining fields.

Mailstore Server :
                                             				  Name of the mailstore server.

Mailstore
                                                					 Protocol : Protocol used by the mailstore server. You can select TLS
                                             				  or Plain.

Mailstore Port: Port associated with the mailstore server.

IMAP IDLE Expire
                                                					 Time : Time (in minutes) after the expiry of which the server stops
                                             				  automatically checking for voicemail.

Mailstore Inbox Folder
                                                					 Name : Name of the inbox folder configured at the mailstore server.

Mailstore Trash Folder
                                                					 Name : Name of the trash folder (typically, the deleted items
                                             				  folder) configured at the mailstore server.

Step 6

Select Save .

## Configure Cisco Unified Communications Manager Integration

Step 1

Select the Configuration
                                             				  tab > Additional Services > Unified
                                             				  Communications .

Step 2

Select the Clusters tab and select Add .

Step 3

Select Enable Cisco UC Manager integration with Messenger Service Client .

Step 4

Select Allow user to enter manual settings , users
                                       			 can change the Primary Server values in basic mode or the TFTP/CTI/CCMCIP server
                                       			 values in advanced mode.

Step 5

Under Cisco Unified Communications Manager Server
                                          				Settings , select:

Basic Server
                                                					 Settings : to enter the basic settings for the Cisco Unified
                                             				  Communications Manager server.

Advanced Server
                                                					 Settings : to enter detailed settings for the
                                             				  Cisco Unified Communications Manager server.

The server configuration options change based on: Basic or
                                                         					 Advanced.

Step 6

Enter the following values for Basic Server Settings :

Primary Server :
                                             				  Enter the IP address of the primary Cisco Unified Communications Manager server. This
                                             				  server is configured with TFTP, CTI, and CCMCIP settings.

Backup Server :
                                             				  Enter the IP address of the backup Cisco Unified Communications Manager server. This
                                             				  server is configured with TFTP, CTI, and CCMCIP settings and provides failover
                                             				  support in case the primary Unified Communications Manager server fails.

Step 7

If you have selected Advanced Server Settings , specify each setting for
                                       			 TFTP (Trivial File Transfer Protocol), CTI (Computer Telephony Integration),
                                       			 and CCMCIP (Cisco Unified Communications Manager IP Phone) servers.

Step 8

Enter the IP address for each of the following servers:

You can specify up to two backup servers for the TFTP server and
                                                      				  one backup server each for the CTI and CCMCIP servers. Enter the appropriate IP
                                                      				  addresses for each Backup Server.

TFTP Server

CTI Server

CCMCIP Server —This is the address of Cisco Unified Communications Manager (UDS) server.

The servers listed must be in the home cluster of the users.

Step 9

In the Voicemail Pilot Number box, enter the number of the
                                       			 voice message service in your Cisco Unified Communications server.

The Organization Administrator typically provides a default voice message number for your entire Webex organization. However, you can select the Allow user to enter manual settings check box to enable users of the cluster to override this default voice message number.

Step 10

Select Voicemail .

Step 11

Select Enable Visual Voicemail .

The Visual Voicemail settings entered here are applicable only to
                                          				the users belonging to this cluster.

Step 12

In the Clusters tab, select Specific voicemail server for this cluster to
                                       			 specify a voicemail server, which is different from the voicemail server
                                       			 settings provided for the entire organization.

Step 13

Select Allow user to enter manual settings to permit users
                                       			 to manually enter Visual Voicemail settings for this cluster.

Step 14

Enter the following information:

Enter the IP address or FQDN for the Voicemail server

Select either HTTP or HTTPS

Enter the Port number

The Mailstore Server information is not supported, the Webex Administration tool expects a value for this field, enter 10.0.0.0 . The mailstore Protocol, Port, and IMAP IDLE Expire Time fields are not supported, do not delete the default values from
                                          these fields.

Name of the inbox folder configured at the mailstore server

Name of the trash or deleted items folder configured at the mailstore server

Step 15

Select Save .

| Step 1 | To configure Visual Voicemail, select the Configuration
                                             				  tab > Unified Communications . The Unified Communications window opens. |
|---|---|
| Step 2 | Select Voicemail to open the Default settings for Visual Voicemail for CUCI screen. Unity Connection customers should enter the Unity Connection
                                          				server IP Address or DNS name into the "Voicemail Server" and "Mailstore
                                          				Server" fields. It is recommended that all other settings remain as the
                                          				defaults. |
| Step 3 | To enable Visual Voicemail, select Enable Visual Voicemail . |
| Step 4 | If you want to manually enter the Visual Voicemail settings,
                                       			 select Allow user to enter manual settings . |
| Step 5 | Enter the following information: Voicemail Server : Name of the Visual Voicemail server with which the Webex application should communicate for retrieving voicemail. Voicemail
                                                					 Protocol : Protocol used for communicating with the Visual Voicemail
                                             				  server. You can select HTTPS or HTTP. Voicemail Port :
                                             				  Port associated with the Visual Voicemail server. The following Mailstore parameter options are not supported. The Webex Administration tool requires values, enter 10.0.0.0 as the Mailstore Server and use the default values for the remaining fields. Mailstore Server :
                                             				  Name of the mailstore server. Mailstore
                                                					 Protocol : Protocol used by the mailstore server. You can select TLS
                                             				  or Plain. Mailstore Port: Port associated with the mailstore server. IMAP IDLE Expire
                                                					 Time : Time (in minutes) after the expiry of which the server stops
                                             				  automatically checking for voicemail. Mailstore Inbox Folder
                                                					 Name : Name of the inbox folder configured at the mailstore server. Mailstore Trash Folder
                                                					 Name : Name of the trash folder (typically, the deleted items
                                             				  folder) configured at the mailstore server. |
| Step 6 | Select Save . |

| Step 1 | Select the Configuration
                                             				  tab > Additional Services > Unified
                                             				  Communications . |
|---|---|
| Step 2 | Select the Clusters tab and select Add . |
| Step 3 | Select Enable Cisco UC Manager integration with Messenger Service Client . |
| Step 4 | Select Allow user to enter manual settings , users
                                       			 can change the Primary Server values in basic mode or the TFTP/CTI/CCMCIP server
                                       			 values in advanced mode. Note When this option is enabled, the user-entered settings will override the default or global Cisco Unified Communications Manager
                                                      settings specified for the Webex organization. | Note | When this option is enabled, the user-entered settings will override the default or global Cisco Unified Communications Manager
                                                      settings specified for the Webex organization. |
| Note | When this option is enabled, the user-entered settings will override the default or global Cisco Unified Communications Manager
                                                      settings specified for the Webex organization. |
| Step 5 | Under Cisco Unified Communications Manager Server
                                          				Settings , select: Basic Server
                                                					 Settings : to enter the basic settings for the Cisco Unified
                                             				  Communications Manager server. Advanced Server
                                                					 Settings : to enter detailed settings for the
                                             				  Cisco Unified Communications Manager server. Note The server configuration options change based on: Basic or
                                                         					 Advanced. | Note | The server configuration options change based on: Basic or
                                                         					 Advanced. |
| Note | The server configuration options change based on: Basic or
                                                         					 Advanced. |
| Step 6 | Enter the following values for Basic Server Settings : Primary Server :
                                             				  Enter the IP address of the primary Cisco Unified Communications Manager server. This
                                             				  server is configured with TFTP, CTI, and CCMCIP settings. Backup Server :
                                             				  Enter the IP address of the backup Cisco Unified Communications Manager server. This
                                             				  server is configured with TFTP, CTI, and CCMCIP settings and provides failover
                                             				  support in case the primary Unified Communications Manager server fails. |
| Step 7 | If you have selected Advanced Server Settings , specify each setting for
                                       			 TFTP (Trivial File Transfer Protocol), CTI (Computer Telephony Integration),
                                       			 and CCMCIP (Cisco Unified Communications Manager IP Phone) servers. |
| Step 8 | Enter the IP address for each of the following servers: Note You can specify up to two backup servers for the TFTP server and
                                                      				  one backup server each for the CTI and CCMCIP servers. Enter the appropriate IP
                                                      				  addresses for each Backup Server. TFTP Server CTI Server CCMCIP Server —This is the address of Cisco Unified Communications Manager (UDS) server. The servers listed must be in the home cluster of the users. | Note | You can specify up to two backup servers for the TFTP server and
                                                      				  one backup server each for the CTI and CCMCIP servers. Enter the appropriate IP
                                                      				  addresses for each Backup Server. |
| Note | You can specify up to two backup servers for the TFTP server and
                                                      				  one backup server each for the CTI and CCMCIP servers. Enter the appropriate IP
                                                      				  addresses for each Backup Server. |
| Step 9 | In the Voicemail Pilot Number box, enter the number of the
                                       			 voice message service in your Cisco Unified Communications server. The Organization Administrator typically provides a default voice message number for your entire Webex organization. However, you can select the Allow user to enter manual settings check box to enable users of the cluster to override this default voice message number. |
| Step 10 | Select Voicemail . |
| Step 11 | Select Enable Visual Voicemail . The Visual Voicemail settings entered here are applicable only to
                                          				the users belonging to this cluster. |
| Step 12 | In the Clusters tab, select Specific voicemail server for this cluster to
                                       			 specify a voicemail server, which is different from the voicemail server
                                       			 settings provided for the entire organization. |
| Step 13 | Select Allow user to enter manual settings to permit users
                                       			 to manually enter Visual Voicemail settings for this cluster. |
| Step 14 | Enter the following information: Voicemail Server Enter the IP address or FQDN for the Voicemail server Voicemail Protocol Select either HTTP or HTTPS Voicemail Port Enter the Port number The Mailstore Server information is not supported, the Webex Administration tool expects a value for this field, enter 10.0.0.0 . The mailstore Protocol, Port, and IMAP IDLE Expire Time fields are not supported, do not delete the default values from
                                          these fields. Mailstore Inbox Folder Name Name of the inbox folder configured at the mailstore server Mailstore Trash Folder Name Name of the trash or deleted items folder configured at the mailstore server | Voicemail Server | Enter the IP address or FQDN for the Voicemail server | Voicemail Protocol | Select either HTTP or HTTPS | Voicemail Port | Enter the Port number | Mailstore Inbox Folder Name | Name of the inbox folder configured at the mailstore server | Mailstore Trash Folder Name | Name of the trash or deleted items folder configured at the mailstore server |
| Voicemail Server | Enter the IP address or FQDN for the Voicemail server |
| Voicemail Protocol | Select either HTTP or HTTPS |
| Voicemail Port | Enter the Port number |
| Mailstore Inbox Folder Name | Name of the inbox folder configured at the mailstore server |
| Mailstore Trash Folder Name | Name of the trash or deleted items folder configured at the mailstore server |
| Step 15 | Select Save . |

| Note | When this option is enabled, the user-entered settings will override the default or global Cisco Unified Communications Manager
                                                      settings specified for the Webex organization. |
|---|---|

| Note | The server configuration options change based on: Basic or
                                                         					 Advanced. |
|---|---|

| Note | You can specify up to two backup servers for the TFTP server and
                                                      				  one backup server each for the CTI and CCMCIP servers. Enter the appropriate IP
                                                      				  addresses for each Backup Server. |
|---|---|

| Voicemail Server | Enter the IP address or FQDN for the Voicemail server |
|---|---|
| Voicemail Protocol | Select either HTTP or HTTPS |
| Voicemail Port | Enter the Port number |

| Mailstore Inbox Folder Name | Name of the inbox folder configured at the mailstore server |
|---|---|
| Mailstore Trash Folder Name | Name of the trash or deleted items folder configured at the mailstore server |