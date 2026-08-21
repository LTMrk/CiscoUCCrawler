---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-5-digcloud-cjab-b-cloud-hybrid-deploy-125-cjab-b-cloud-hybrid-depl-5b424b8063
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_5/DIGCloud/cjab_b_cloud-hybrid-deploy-125/cjab_b_cloud-hybrid-deploy-125_chapter_01110.html
retrieved_at: 2026-08-21T21:13:29.125166+00:00
---

Cloud and Hybrid Deployments for Cisco Jabber 12.5

# Cloud and Hybrid Deployments for Cisco Jabber 12.5

Updated: April 1, 2024

Chapter: Configure the Clients

## Chapter: Configure the Clients

# Configure the Clients

## Client
                        	 Configuration Workflow

Step 1

Introduction to Client Configuration

Step 2

Create and Host the Client Configuration Files

Step 3

Set Parameters on Phone Configuration for Desktop Clients

Step 4

Set Parameters on Phone Configuration for Mobile Clients

Step 5

Configure Proxy Setting—Optional

### Introduction to
                           	 Client Configuration

Cisco Jabber can retrieve configuration settings from the following sources:

Service Profiles—You can configure some client settings in UC service profiles on Cisco Unified Communications Manager release
                                    9 and later. When users launch the client, it discovers the Cisco Unified Communications Manager home cluster using a DNS
                                    SRV record and automatically retrieves the configuration from the UC service profile.

Applies to on-premises deployments only.

Phone Configuration—You can set some client settings in the phone configuration on Cisco Unified Communications Manager release
                                    9 and later. The client retrieves the settings from the phone configuration in addition to the configuration in the UC service
                                    profile.

Applies to on-premises deployments only.

Cisco Unified Communications Manager IM and Presence Service—You can enable instant messaging and presence capabilities and
                                    configure certain settings such as presence subscription requests.

In the Advanced settings window, if you select Cisco IM & Presence , the client retrieves UC services from Cisco Unified Communications Manager IM and Presence Service. The client does not
                                    use service profiles or SSO discovery.

Applies to on-premises deployments only.

Client Configuration—You can set client configuration parameters that are applied when users sign in, by either:

Set the client configuration parameters with Unified CM.

Create XML files using an XML editor that contain configuration parameters. You then host the XML files on a TFTP server.

Webex Administration Tool—You can configure some client settings with the Webex Administration Tool.

You can upload a jabber-config.xml client configuration file into the Webex Administration Tool. You can apply separate configuration files for groups in the Webex Messenger Administration Tool. When the client successfully connects to Webex Messenger it downloads the XML file and the configuration is applied.

The client will use the following order for configuration settings:

Settings in Webex Messenger Administration Tool

Settings in jabber-config.xml file from Webex Messenger Administration Tool.

Group configuration file settings take priority over the configuration file in Webex Messenger Administration Tool.

Settings in jabber-config.xml file from the TFTP server.

If there are any conflicts with configuration settings, the settings set in Webex Administration tool will take priority over this configuration file.

Applies to cloud-based deployments only.

### Create and Host the Client Configuration Files

For on-premises and hybrid cloud-based deployments, create client configuration files and host them on the Cisco Unified Communications
                                 Manager TFTP service.

For cloud-based deployments, configure the client with the Webex Administration Tool. However, you can optionally set up a TFTP server to configure the client with settings that are not
                                 available in Webex Administration Tool.

For Cisco Jabber for iPhone and iPad and Cisco Jabber for Android, you
                                 				must create a global configuration file to set up:

Directory
                                       					 integration for on-premises deployments.

Voicemail
                                       					 service credentials for hybrid-cloud deployments.

In
                                             				most environments, Cisco Jabber for Windows and Cisco Jabber for Mac do not require any configuration to connect to
                                             				services. Create a configuration file only if you require custom
                                             				content such as automatic updates, problem reporting, or user policies and options.

#### Before you begin

Note the following configuration file requirements:

Configuration filenames are case-sensitive. Use lowercase letters in the filename to prevent errors and to ensure that the
                                       client can retrieve the file from the TFTP server.

Use UTF-8 encoding for the configuration files.

The client cannot read configuration files that do not have a valid XML structure. Check the structure of your configuration
                                       file for closing elements and correct nesting of elements.

Use only valid XML character entity references in your configuration file. For example, use &amp; instead of & . If your XML contains invalid characters, the client cannot parse the configuration file.

To validate your
                                       						configuration file, open the file in Microsoft Internet Explorer.

If Internet Explorer displays the entire XML structure, your configuration file is valid.

If Internet Explorer displays only part of the XML structure, your configuration file likely contains invalid characters or
                                             entities.

Step 1

Specify Your TFTP Server Address

Specify your TFTP server address for the client to enable access to your configuration file.

Step 2

Create Global Configurations

Configure the clients for users in your deployment.

Step 3

Create Group Configurations

Apply different configuration to different set of users.

Step 4

Host Configuration Files

Host configuration files on any TFTP server.

Step 5

Restart Your TFTP Server

Restart the TFTP server before the client can access the
                                             				configuration files.

#### Specify Your TFTP Server Address

The client gets configuration files from a TFTP server.

Specify your TFTP server address so the client can access your configuration file.

Attention

If Cisco Jabber gets the _cisco-uds SRV record from a DNS query, it can automatically locate the user's home cluster. As a result, the client can also locate
                                                            the Cisco Unified Communications Manager TFTP service.

You do not need to specify your TFTP server address if you deploy the _cisco-uds SRV record.

##### Specify TFTP Servers in Phone Mode

If you deploy the client in phone mode, you can provide the address of the TFTP server as follows:

Users manually enter the TFTP server address when they start the client.

You specify the TFTP server address during installation with the TFTP argument.

#### Create Global Configurations

The client downloads the global configuration file from your TFTP server during the sign in sequence. Configure the client
                                    for all users in your deployment.

##### Before you begin

If the structure of your configuration file is not valid, the client cannot read the values you set. Review the XML  samples
                                    in this chapter for more information.

Step 1

Create a file named jabber-config.xml with any text editor.

Use lowercase letters in the filename.

Use UTF-8 encoding.

Step 2

Define the required configuration parameters in jabber-config.xml .

Step 3

Host the group configuration file on your TFTP server.

If your environment has  multiple TFTP servers, ensure that the configuration file is the same on all TFTP servers.

#### Create Group
                              	 Configurations

Group
                                    		  configuration files apply to subsets of users and are supported on  Cisco Jabber
                                    		  for desktop (CSF devices) and on Cisco Jabber for mobile devices. Group
                                    		  configuration files take priority over global configuration files.

If you provision
                                    		  users with CSF devices, specify the group configuration filenames in the Cisco
                                       			 Support Field field on the device configuration. If users do not
                                    		  have CSF devices, set a unique configuration filename for each group during
                                    		  installation with the TFTP_FILE_NAME argument.

##### Before you begin

If the structure of your configuration file is not valid, the client cannot read the values you set. Review the XML samples
                                    in this chapter for more information.

Step 1

Create an XML
                                             			 group configuration file with any text editor.

The group
                                                				configuration file can have any appropriate name; for example, jabber-groupa-config.xml .

Step 2

Define the
                                             			 required configuration parameters in the group configuration file.

Step 3

Add the group
                                             			 configuration file to applicable CSF devices.

Open the Cisco Unified CM Administration interface.

Select Device > Phone .

Find and
                                                   				  select the appropriate CSF device to which the group configuration applies.

In the Phone Configuration window, navigate to Product Specific
                                                         						Configuration Layout > Desktop Client Settings .

In the Cisco Support Field field, enter configurationfile= group_configuration_file_name.xml . For
                                                   				  example, enter configurationfile=groupa-config.xml .

If you
                                                                  						host the group configuration file on your TFTP server in a location other than
                                                                  						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml .

Do not
                                                                  						add more than one group configuration file. The client uses only the first
                                                                  						group configuration in the Cisco Support Field field.

Select Save .

Step 4

Host the group
                                             			 configuration file on your TFTP server.

#### Host Configuration Files

You can host configuration files on any TFTP server. However, we recommend hosting configuration files on the Cisco Unified Communications Manager TFTP server, which is where the device configuration file resides.

Step 1

Open the Cisco Unified OS Administration interface on Cisco Unified Communications Manager .

Step 2

Select Software Upgrades > TFTP File Management .

Step 3

Select Upload File .

Step 4

Select Browse in the Upload File section.

Step 5

Select the configuration file on the file system.

Step 6

Do not specify a value in the Directory text box in the Upload File section.

You should leave an empty value in the Directory text box so that the configuration file resides in the default directory of the TFTP server.

Step 7

Select Upload File .

#### Restart Your TFTP Server

You must restart your TFTP server before the client can access the configuration files.

Step 1

Open the Cisco Unified Serviceability interface on Cisco Unified Communications Manager .

Step 2

Select Tools > Control Center - Feature Services .

Step 3

Select Cisco Tftp from the CM Services section.

Step 4

Select Restart .

A window displays to prompt you to confirm the restart.

Step 5

Select OK .

The Cisco Tftp Service Restart Operation was Successful status displays.

Step 6

Select Refresh to ensure the Cisco Tftp service starts successfully.

##### What to do next

To verify that the configuration file is available on your TFTP server, open the configuration file in any browser. Typically,
                                    you can access the global configuration file at the following URL: http:// tftp_server_address :6970/jabber-config.xml

#### Configuration
                              	 File

For detailed information on the jabber-config.xml configuration file structure, group elements, parameters, and examples, see the Parameters Reference Guide for Cisco Jabber .

### Set parameters on phone configuration for desktop clients

The client can
                                 		  retrieve configuration settings in the phone configuration from the following
                                 		  locations on Cisco Unified Communications Manager :

Applies to the entire cluster.

For users with only IM and Presence Service capabilities (IM only), you must set phone configuration parameters in the Enterprise Phone Configuration window.

Applies to
                                          				  groups of devices and takes priority over the cluster configuration.

Applies to individual CSF desktop devices and takes priority over the group configuration.

#### Parameters in
                              	 Phone Configuration

The following table lists the configuration parameters you can set in the Product Specific Configuration Layout section of the phone configuration and maps corresponding parameters from the client configuration file:

Enables or disables video capabilities.

Restriction

This parameter is available only on the CSF device configuration.

Restricts users from transferring specific file types.

Set a file extension as the value, for example, .exe .

Use a semicolon to delimit multiple values, for example,

```
.exe;.msi;.rar;.zip
```

Specifies the URL to the XML file that holds client update information. The client uses this URL to retrieve the XML file
                                                from your web server.

In hybrid cloud-based deployments, you should use the Webex Administration Tool to configure automatic updates.

Specifies the URL for the custom script that allows users to submit problem reports.

### Set Parameters on
                           	 Phone Configuration for Mobile Clients

The client can retrieve configuration settings in the phone configuration from the following locations on Cisco Unified Communications
                                 Manager:

Cisco Dual Mode for iPhone (TCT) Configuration — Applies to individual TCT devices and takes priority over the group configuration.

Cisco Jabber for Tablet (TAB) Configuration — Applies to individual TAB devices and takes priority over the group configuration.

#### Parameters in
                              	 Phone Configuration

The following table lists the configuration parameters you can set in the Product Specific Configuration Layout section of the phone configuration and maps corresponding parameters from the client configuration file:

Parameter

Description

On-Demand VPN URL

URL for initiating on-demand VPN.

Applicable for iOS only.

Preset Wi-fi Networks

Enter the SSIDs for Wi-Fi networks (SSIDs) approved by your organization. Separate SSIDs with a forward slash (/). Devices
                                                do not connect to secure connect if connected to one of the entered Wi-Fi networks.

Default Ringtone

Sets the default ringtone to Normal or Loud .

Video Capabilities

Enables or disables video capabilities.

Enabled (default) — Users can send and receive video calls.

Disabled — Users cannot send or receive video calls.

Dial via Office

TCT and BOT devices only.

Enables or disables Dial via Office.

Enabled — Users can dial via office.

Disabled (default) — Users cannot dial via office.

### Configure Proxy Setting—Optional

Your client might use proxy settings to connect to services.

The following limitations apply when using a proxy for these HTTP requests:

Proxy Authentication is not supported.

Wildcards in the bypass list are supported.

Cisco Jabber supports proxy for HTTP request using HTTP CONNECT, but does not support proxy when using HTTPS CONNECT.

Web Proxy Auto Discovery (WAPD) is not supported and must be disabled.

If necessary, configure the proxy settings by following the steps for your client type.

#### Configure Proxy
                              	 Settings for Cisco Jabber for Windows

Configure proxy
                                    		  settings for Windows in the Local Area Network (LAN) settings for Internet
                                    		  properties.

Step 1

In the Connections tab select LAN
                                                				Settings .

Step 2

Configure a
                                             			 proxy using one of the following options:

- For automatic
                                                				configuration, specify a .pac file URL.

- For Proxy Server, specify
                                                				an explicit proxy address.

#### Configure Proxy
                              	 Settings for Cisco Jabber for Mac

Configure proxy
                                    		  settings for Mac in System
                                       			 Preferences .

Step 1

Select System
                                                   				  Preferences > Network

Step 2

Choose your
                                             			 network service from the list and select Advanced > Proxies .

Step 3

Configure a
                                             			 proxy using one of the following options:

- For automatic
                                                				configuration, specify a .pac file URL.

- For Proxy Server, specify
                                                				an explicit proxy address.

#### Configure Proxy
                              	 Settings for Cisco Jabber iPhone and iPad

Configure proxy settings in the Wi-Fi settings of an iOS device using
                                    		  one of the following methods:

Step 1

Select Wi-Fi > HTTP
                                                   				  PROXY > Auto and specify a .pac file URL as the automatic configuration script.

Step 2

Select Wi-Fi > HTTP
                                                   				  PROXY > Manual and specify an
                                             			 explicit proxy address.

#### Configure Proxy
                              	 Settings for Cisco Jabber for Android

Configure
                                             			 proxy settings in the Wi-Fi settings of an Android device using one of the
                                             			 following methods:

This
                                                               					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
                                                               					 series devices.

- Specify an explicit proxy
                                                				address in the Wi-Fi
                                                      					 Networks > Modify Network > Show Advanced
                                                      					 Options > Proxy Settings > Auto tab.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Introduction to Client Configuration |  |
| Step 2 | Create and Host the Client Configuration Files |  |
| Step 3 | Set Parameters on Phone Configuration for Desktop Clients |  |
| Step 4 | Set Parameters on Phone Configuration for Mobile Clients |  |
| Step 5 | Configure Proxy Setting—Optional |  |

| Note | Group configuration file settings take priority over the configuration file in Webex Messenger Administration Tool. |
|---|---|

| Note | In
                                             				most environments, Cisco Jabber for Windows and Cisco Jabber for Mac do not require any configuration to connect to
                                             				services. Create a configuration file only if you require custom
                                             				content such as automatic updates, problem reporting, or user policies and options. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Specify Your TFTP Server Address | Specify your TFTP server address for the client to enable access to your configuration file. |
| Step 2 | Create Global Configurations | Configure the clients for users in your deployment. |
| Step 3 | Create Group Configurations | Apply different configuration to different set of users. |
| Step 4 | Host Configuration Files | Host configuration files on any TFTP server. |
| Step 5 | Restart Your TFTP Server | Restart the TFTP server before the client can access the
                                             				configuration files. |

| Command or Action | Purpose |
|---|---|
| Specify your TFTP server address so the client can access your configuration file. | Attention If Cisco Jabber gets the _cisco-uds SRV record from a DNS query, it can automatically locate the user's home cluster. As a result, the client can also locate
                                                            the Cisco Unified Communications Manager TFTP service. You do not need to specify your TFTP server address if you deploy the _cisco-uds SRV record. | Attention | If Cisco Jabber gets the _cisco-uds SRV record from a DNS query, it can automatically locate the user's home cluster. As a result, the client can also locate
                                                            the Cisco Unified Communications Manager TFTP service. You do not need to specify your TFTP server address if you deploy the _cisco-uds SRV record. |
| Attention | If Cisco Jabber gets the _cisco-uds SRV record from a DNS query, it can automatically locate the user's home cluster. As a result, the client can also locate
                                                            the Cisco Unified Communications Manager TFTP service. You do not need to specify your TFTP server address if you deploy the _cisco-uds SRV record. |

| Attention | If Cisco Jabber gets the _cisco-uds SRV record from a DNS query, it can automatically locate the user's home cluster. As a result, the client can also locate
                                                            the Cisco Unified Communications Manager TFTP service. You do not need to specify your TFTP server address if you deploy the _cisco-uds SRV record. |
|---|---|

| Command or Action | Purpose |
|---|---|
| If you deploy the client in phone mode, you can provide the address of the TFTP server as follows: Users manually enter the TFTP server address when they start the client. You specify the TFTP server address during installation with the TFTP argument. |  |

| Step 1 | Create a file named jabber-config.xml with any text editor. Use lowercase letters in the filename. Use UTF-8 encoding. |
|---|---|
| Step 2 | Define the required configuration parameters in jabber-config.xml . |
| Step 3 | Host the group configuration file on your TFTP server. If your environment has  multiple TFTP servers, ensure that the configuration file is the same on all TFTP servers. |

| Step 1 | Create an XML
                                             			 group configuration file with any text editor. The group
                                                				configuration file can have any appropriate name; for example, jabber-groupa-config.xml . |
|---|---|
| Step 2 | Define the
                                             			 required configuration parameters in the group configuration file. |
| Step 3 | Add the group
                                             			 configuration file to applicable CSF devices. Open the Cisco Unified CM Administration interface. Select Device > Phone . Find and
                                                   				  select the appropriate CSF device to which the group configuration applies. In the Phone Configuration window, navigate to Product Specific
                                                         						Configuration Layout > Desktop Client Settings . In the Cisco Support Field field, enter configurationfile= group_configuration_file_name.xml . For
                                                   				  example, enter configurationfile=groupa-config.xml . Note If you
                                                                  						host the group configuration file on your TFTP server in a location other than
                                                                  						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml . Do not
                                                                  						add more than one group configuration file. The client uses only the first
                                                                  						group configuration in the Cisco Support Field field. Select Save . | Note | If you
                                                                  						host the group configuration file on your TFTP server in a location other than
                                                                  						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml . Do not
                                                                  						add more than one group configuration file. The client uses only the first
                                                                  						group configuration in the Cisco Support Field field. |
| Note | If you
                                                                  						host the group configuration file on your TFTP server in a location other than
                                                                  						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml . Do not
                                                                  						add more than one group configuration file. The client uses only the first
                                                                  						group configuration in the Cisco Support Field field. |
| Step 4 | Host the group
                                             			 configuration file on your TFTP server. |

| Note | If you
                                                                  						host the group configuration file on your TFTP server in a location other than
                                                                  						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml . Do not
                                                                  						add more than one group configuration file. The client uses only the first
                                                                  						group configuration in the Cisco Support Field field. |
|---|---|

| Step 1 | Open the Cisco Unified OS Administration interface on Cisco Unified Communications Manager . |
|---|---|
| Step 2 | Select Software Upgrades > TFTP File Management . |
| Step 3 | Select Upload File . |
| Step 4 | Select Browse in the Upload File section. |
| Step 5 | Select the configuration file on the file system. |
| Step 6 | Do not specify a value in the Directory text box in the Upload File section. You should leave an empty value in the Directory text box so that the configuration file resides in the default directory of the TFTP server. |
| Step 7 | Select Upload File . |

| Step 1 | Open the Cisco Unified Serviceability interface on Cisco Unified Communications Manager . |
|---|---|
| Step 2 | Select Tools > Control Center - Feature Services . |
| Step 3 | Select Cisco Tftp from the CM Services section. |
| Step 4 | Select Restart . A window displays to prompt you to confirm the restart. |
| Step 5 | Select OK . The Cisco Tftp Service Restart Operation was Successful status displays. |
| Step 6 | Select Refresh to ensure the Cisco Tftp service starts successfully. |

| Note | For users with only IM and Presence Service capabilities (IM only), you must set phone configuration parameters in the Enterprise Phone Configuration window. |
|---|---|

| Desktop Client Settings Configuration | Description |
|---|---|
| Video Calling | Enables or disables video capabilities. Enabled (default) Users can send and receive video calls. Disabled Users cannot send or receive video calls. Restriction This parameter is available only on the CSF device configuration. | Restriction | This parameter is available only on the CSF device configuration. |
| Restriction | This parameter is available only on the CSF device configuration. |
| File Types to Block in File Transfer | Restricts users from transferring specific file types. Set a file extension as the value, for example, .exe . Use a semicolon to delimit multiple values, for example, .exe;.msi;.rar;.zip |
| Automatically Start in Phone Control | Sets the phone type for users when the client starts for the first time. Users can change their phone type after the initial
                                                start. The client then saves the user preference and uses it for subsequent starts. Enabled Use the desk phone device for calls. Disabled (default) Use the software phone (CSF) device for calls. |
| Jabber For Windows Software Update Server URL | Specifies the URL to the XML file that holds client update information. The client uses this URL to retrieve the XML file
                                                from your web server. In hybrid cloud-based deployments, you should use the Webex Administration Tool to configure automatic updates. |
| Problem Report Server URL | Specifies the URL for the custom script that allows users to submit problem reports. |

| Restriction | This parameter is available only on the CSF device configuration. |
|---|---|

| Parameter | Description |
|---|---|
| On-Demand VPN URL | URL for initiating on-demand VPN. Note Applicable for iOS only. | Note | Applicable for iOS only. |
| Note | Applicable for iOS only. |
| Preset Wi-fi Networks | Enter the SSIDs for Wi-Fi networks (SSIDs) approved by your organization. Separate SSIDs with a forward slash (/). Devices
                                                do not connect to secure connect if connected to one of the entered Wi-Fi networks. |
| Default Ringtone | Sets the default ringtone to Normal or Loud . |
| Video Capabilities | Enables or disables video capabilities. Enabled (default) — Users can send and receive video calls. Disabled — Users cannot send or receive video calls. |
| Dial via Office Note TCT and BOT devices only. | Note | TCT and BOT devices only. | Enables or disables Dial via Office. Enabled — Users can dial via office. Disabled (default) — Users cannot dial via office. |
| Note | TCT and BOT devices only. |

| Note | Applicable for iOS only. |
|---|---|

| Note | TCT and BOT devices only. |
|---|---|

| Step 1 | In the Connections tab select LAN
                                                				Settings . |
|---|---|
| Step 2 | Configure a
                                             			 proxy using one of the following options: For automatic
                                                				configuration, specify a .pac file URL. For Proxy Server, specify
                                                				an explicit proxy address. |

| Step 1 | Select System
                                                   				  Preferences > Network |
|---|---|
| Step 2 | Choose your
                                             			 network service from the list and select Advanced > Proxies . |
| Step 3 | Configure a
                                             			 proxy using one of the following options: For automatic
                                                				configuration, specify a .pac file URL. For Proxy Server, specify
                                                				an explicit proxy address. |

| Step 1 | Select Wi-Fi > HTTP
                                                   				  PROXY > Auto and specify a .pac file URL as the automatic configuration script. |
|---|---|
| Step 2 | Select Wi-Fi > HTTP
                                                   				  PROXY > Manual and specify an
                                             			 explicit proxy address. |

| Configure
                                             			 proxy settings in the Wi-Fi settings of an Android device using one of the
                                             			 following methods: Specify a .pac file URL as
                                                				the automatic configuration script in the Wi-Fi > Modify
                                                      					 Network > Show Advanced Options > Proxy
                                                      					 Settings > Auto tab. Note This
                                                               					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
                                                               					 series devices. Specify an explicit proxy
                                                				address in the Wi-Fi
                                                      					 Networks > Modify Network > Show Advanced
                                                      					 Options > Proxy Settings > Auto tab. | Note | This
                                                               					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
                                                               					 series devices. |
|---|---|---|
| Note | This
                                                               					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
                                                               					 series devices. |

| Note | This
                                                               					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
                                                               					 series devices. |
|---|---|