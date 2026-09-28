---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-ipad-9-3-x-jabi-bk-cceaf656-00-cisco-jabber-video-for-ipad-jabi-bk-cc-79b3cc82b3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/iPad/9_3_x/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad_chapter_0100.html
retrieved_at: 2026-08-21T19:43:47.296134+00:00
---

Cisco Jabber Video for iPad 9.3.4 Administration Guide

# Cisco Jabber Video for iPad 9.3.4 Administration Guide

Updated: November 22, 2013

Chapter: Set up for Cisco Unified Communications Manager 8.x

## Chapter: Set up for Cisco Unified Communications Manager 8.x

# Set up for Cisco Unified Communications Manager 8.x

This chapter describes how you can set up Cisco Jabber Video for iPad using Cisco Unified Communications Manager 8.x

## System and Network Requirements

Refer to this section for information on the system and network requirements for Cisco Jabber Video for iPad .

### Supported Audio and Video Codecs

Supported audio codecs include:

G.722.1 is supported in Cisco Unified Communications Manager 8.6.1 or later.

- G.711, including G.711 A-law and G.711 u-law

The supported video codec is H.264/AVC.

### Maximum Negotiated Bit Rate

You specify the maximum payload bit rate in the Region Configuration window in Cisco Unified Communications Manager. This maximum payload bit rate does not include packet overhead, so the actual bit rate used is higher than the maximum payload bit rate you specify.

This table describes how Cisco Jabber Video for iPad allocates the maximum payload bit rate:

The maximum video call bit rate minus the audio bit rate

### Performance Expectations for Bandwidth

A minimal upload bandwidth of 256 to 384 Kbps is required for good video quality. An upload bandwidth above 512 Kbps can produce an outgoing video resolution of 480 X 360 at 20 fps and a maximum incoming video resolution of 640 X 480 at 30 fps on the iPad 2, third and fourth generation iPad, and iPad Mini. An upload bandwidth of 768 Kbps can produce an outgoing video resolution of 640 X 480 at 20 fps and a maximum incoming video resolution of 1024 X 576 at 30 fps on the fourth generation iPad only. VPN usage increases payload size and this increases bandwidth consumption. Video resolutions and frame rates may not be as high using a VPN connection.

### Video Rate Adaptation

Cisco Jabber Video for iPad uses video rate adaptation to negotiate optimal video quality based on your network conditions. Video rate adaptation dynamically scales video quality when video transmission begins.

Cisco Jabber Video for iPad automatically adapts video to suit available bandwidth. When users make video calls, the application rapidly and incrementally increases bit rate and resolution to achieve the optional settings. Users should expect video calls to being at lower resolution and scale upwards to higher resolution over a short period of time. The application saves history so that subsequent video calls should begin at the optimal resolution. However, users can expect some fluctuation and scaling of video transmissions until the optimal resolution is achieved.

### Firewall Requirements

Configure hardware firewalls to allow the ports to carry traffic for the application. Hardware firewalls are network devices that provide protection from unwanted traffic at an organizational level. This table lists the ports required for the deployments of Cisco Unified Communications Manager and Cisco Unified Presence. These ports must be open on all firewalls for the application to function properly.

If no port is specified in a TFTP server address, Cisco Jabber Video for iPad will try port 6970 to obtain phone setup files and dial rule files.

7080

HTTPS

## Setting Up System SIP Parameters

This setting is applied across the cluster. There is no need to set the Server field.

## Installing Cisco Options Package (COP) File for Devices

Install a device-specific Cisco Options Package (COP) file on all Cisco Unified Communications Manager servers to make Cisco Jabber Video for iPad available as a device.

General information about installing COP files is available in the Software Upgrades chapter of the Cisco Unified Communications Operating System Administration Guide for your release at http:/​/​www.cisco.com/​en/​US/​products/​sw/​voicesw/​ps556/​prod_​maintenance_​guides_​list.html .

The following Cisco Unified Communications Manager releases already contain the Tablet COP file:

- 7.1.5.35113-1 and above

- 8.5.1.16090-1 and above

- 8.6.2.23057-1 and above

- 9.0.1.11013-1-1 and above

- 9.1.1.10000-11 and above

Installation of the Tablet COP file is not required for these releases.

Perform this procedure at a time of low usage because it may interrupt service.

- Select Cisco Unified OS Administration in the Navigation drop-down list and then select Go .

- Select Software Upgrades > Install/Upgrade .

For more information, see the online help.

- Select Next .

- Select the device COP file.

- Select Next .

- Follow the instructions on the screen.

Wait for the process to be completed. This process may take some time.

- Reboot Unified CM at a time of low usage.

This step, which clears the Tomcat image cache, is required for the device icon to display properly on the device list page in Unified CM.

- Enter this command from the CLI: utils service restart Cisco Tomcat

- Let the system fully return to service.

To avoid interruptions in service, ensure that each server has returned to active service before you perform this procedure on another server.

## Setting Up a Dedicated SIP Profile

Set up a dedicated SIP profile that allows Cisco Jabber Video for iPad to stay connected to Cisco Unified Communications Manager if the application is running in the background.

You can name the profile "Standard iPad SIP Profile."

- Timer Register Delta (seconds)—120

- Timer Register Expires (seconds)—720

- Timer Keep Alive Expires (seconds)—720

- Timer Subscribe Expires (seconds)—21600

- Timer Subscribe Delta (seconds)—15

- Start Media Port—Defines the start port for media streams. This field sets the lowest port in the range.

- Stop Media Port—Defines the stop port for media streams. This field sets the highest port in the range.

Cisco Jabber Video for iPad equally divides the port range that you set in the SIP profile. The client then uses the port range as follows:

- Lower half of the port range for audio streams

- Upper half of the port range for video streams

For example, if you use a start media port of 3000 and an end media port of 4000, the client sends media through ports as follows:

- Ports 3000 to 3501 for audio streams

- Ports 3502 to 4000 for video streams

As a result of splitting the port range for audio media and video media, the client creates identifiable media streams. You can then classify and prioritize those media streams by setting DSCP values in the IP packet headers.

Select this SIP profile for all user devices running Cisco Jabber Video for iPad .

## Setting Up Application Dial Rules for Cisco Jabber Video for iPad

A Cisco Options Package (COP) file must be used to set up dial rules for Cisco Jabber Video for iPad on Cisco Unified Communications Manager 8.5 and earlier. This COP file is different from the device COP file described in other sections of this document.

Perform the series of procedures described in this topic to make all of your existing dial rules available to the application. This series of procedures will guide you in installing the required XML files in a folder named CUPC at the root level of the Cisco Unified Communications Manager TFTP server.

See the related chapters in the Cisco Unified Communications Manager Administration Guide for additional information about Application Dial Rule setup. The guide specific to your release of Cisco Unified Communications Manager can be found here:

http:/​/​www.cisco.com/​en/​US/​products/​sw/​voicesw/​ps556/​prod_​maintenance_​guides_​list.html

### Obtaining Cisco Options Package (COP) File for Dial Rules

Use a COP file that is also used for this purpose for other Cisco products.

This procedure applies to only Cisco Unified Communications Manager Release 8.5 and earlier versions.

The COP file described in this procedure is different from the device COP file that is used to make Cisco Jabber Video for iPad available as a device in Cisco Unified Communications Manager.

You do not need any other files in this download.

### Restarting the TFTP Service

Perform this procedure at a time of low usage; it may interrupt service.

For more information, see the Starting, Stopping, Restarting, and Refreshing Status of Services in Control Center topic in the Cisco Unified Serviceability Administration Guide at http:/​/​www.cisco.com/​en/​US/​products/​sw/​voicesw/​ps556/​prod_​maintenance_​guides_​list.html .

## System-level Prerequisites for Midcall Features

Ensure that you set up your Cisco Unified Communications Manager system for these midcall features:

- Hold and Resume

- Conference and Merge

- Transfer

- To Mobile

For details about setting up these features, see the Cisco Unified Communications Manager Features and Services Guide for your release at http:/​/​www.cisco.com/​en/​US/​products/​sw/​voicesw/​ps556/​prod_​maintenance_​guides_​list.html .

## Usage and Error Tracking

Cisco Jabber Video for iPad relies on a third-party service, Google Analytics, to collect and generate aggregated usage and error-tracking data that Cisco uses to discover defects and improve product performance. In compliance with the Google Analytics privacy statement, Cisco does not store personally identifying information.

All information collected is stored by Google and is confidential. Only Cisco has access to this information.

You can enable or disable usage and error tracking for each user when you set up each user device in Cisco Unified Communications Manager.

Depending on the setting, Cisco collects the following information:

- Errors and warnings

- Screen views in the application (for example, how often users view their lists of voice messages)

- Feature activities (for example, how often users add a contact)

- The TFTP server address to which the application connects

- Approximate geographic location, based on mobile service provider activity

For more information about the reporting tool, see

## Adding a User Device

Add a user device to your Cisco Unified Communications Manager server and verify the setup.

Perform these tasks:

- Installing Cisco Options Package (COP) File for Devices

- Setting Up a Dedicated SIP Profile

- Verify that the Device Pool that you will assign to the iPad device is associated with a region that includes support for all supported audio codecs. The audio codecs that Cisco Jabber Video for iPad supports include G.711 mu-law or A-law and G.722.1.

- represents only one device. If a user has Cisco Jabber Video for iPad on multiple devices, set up each device with a different device name.

- must start with TAB , followed by up to 15 uppercased or numeric characters. Example: TABJOHND .

- can contain dot (.), dash (–), or underscore (_).

Customization of this field is not currently supported.

- Forward Unregistered Internal

- Forward Unregistered External

For more information about these settings, see the online help in Cisco Unified Communications Manager.

See general restrictions in the online help in Cisco Unified Communications Manager.

- Select User Management > End User .

- Search for and select the user.

- In the Device Information section, select Device Association .

- Check the device that you want to associate with the user.

- Select Save Selected/Changes .

The Primary User Device field is only available in Cisco Unified Communications Manager 9.0 and earlier. This field does not need to specified in later versions of Cisco Unified Communications Manager.

Verify your setup by performing these tasks:

- Ensure that the iPad device is connected to the corporate Wi-Fi network. Verify that you can access a web page on your corporate intranet using the browser on the device.

- Start Cisco Jabber Video for iPad and enter the username (or email address), password, and TFTP server address for the device you just added.

- Test basic voice features in Cisco Jabber Video for iPad , such as making, holding, and transferring calls.

## Turning on Control of iPad as a Phone

Allow your users to control their devices as a phone by following these steps.

If the user's phone is a Cisco Unified IP Phone 6900, 8900 or 9900 series model, also select Standard CTI Allow Control of Phones supporting Xfer and conf .

## Specifying LDAP Authentication Settings

The LDAP authentication feature enables Cisco Unified Communications Manager to authenticate user passwords against the corporate LDAP directory.

LDAP authentication does not apply to the passwords of application users; Cisco Unified Communications Manager authenticates application users in its internal database.

Turn on LDAP synchronization in Cisco Unified Communications Manager.

To use Secure Socket Layer (SSL) to communicate with the LDAP directory, check Use SSL .

If you set up LDAP over SSL, upload the LDAP directory certificate to Cisco Unified Communications Manager.

## Setting Up LDAP Synchronization for User Provisioning

Perform this task in Cisco Unified Communications Manager.

LDAP synchronization uses the Cisco Directory Synchronization (DirSync) tool on Cisco Unified Communications Manager to synchronize information (either manually or periodically) from a corporate LDAP directory. When you turn on the DirSync service, Cisco Unified Communications Manager automatically provisions users from the corporate directory. Cisco Unified Communications Manager still uses its local database, but turns off its facility to allow you to create user accounts. You use the LDAP directory interface to create and manage user accounts.

- Ensure that you install the LDAP server before you attempt the LDAP-specific configuration on Cisco Unified Communications Manager.

- Understand that LDAP synchronization does not apply to application users Cisco Unified Communications Manager. You must manually provision application users in the Cisco Unified Communications Manager Administration interface.

- Activate and start the Cisco DirSync service on Cisco Unified Communications Manager.

- LDAP directory account settings

- User attributes to be synchronized

- Synchronization schedule

- LDAP server hostname or IP address and port number

- If you configure LDAP over SSL, upload the LDAP directory certificate onto Cisco Unified Communications Manager.

- See the LDAP directory content in the Cisco Unified Communications Manager SRND for information on the account synchronization mechanism for specific LDAP products and general best practices for LDAP synchronization.

## Bulk Configuration

Use the information in this document to set up individual users and devices as the basis for completing a bulk administration template for setting up users and devices.

When you are ready for bulk processes, follow the instructions in the bulk administration guide for your release of Cisco Unified Communications Manager, available from http:/​/​www.cisco.com/​en/​US/​products/​sw/​voicesw/​ps556/​prod_​maintenance_​guides_​list.html .

## Setting Up Visual Voicemail

Perform these tasks:

- Verify that VMRest secure message is enabled Select Allow Access to Secure Message Recordings to enable API access to secure messages. This is configured in the Cisco Unity Connection Messaging Interface (CUMI). Select System Settings > Advanced > API Settings in Cisco Unity Connection Administration.

- Consult your voicemail administrator if you have questions about any of the settings in this section.

Use the format Servername.YourCompany.com:portnumber .

Use the format YourVoiceMessageStoreServer.yourcompany.com:portnumber .

Test your voicemail by performing these tasks:

- Delete the existing voicemail account, if applicable, in Cisco Jabber Video for iPad and then restart the application.

- Sign in using your Cisco Unified Communications Manager account.

- When prompted for voicemail setup, enter or confirm the settings.

- Tap Save , even if you make no changes.

- Test the voicemail features.

## Setting Up Connect on Demand VPN

Cisco Jabber Video for iPad supports two ways to enable the Connect on Demand VPN feature.

If your Cisco Unified Presence and Cisco Unified Communications Manager servers are configured with a Fully Qualified Domain Name (FQDN), the Connect on Demand VPN feature is enabled or disabled using Cisco Jabber Video for iPad . If your Cisco Unified Presence and Cisco Unified Communications Manager servers are configured with an IP address, configure the On Demand VPN URL parameter to enable the Connect on Demand VPN feature.

Cisco recommends that Cisco Unified Presence and Cisco Unified Communications Manager be deployed with a FQDN. Use of the Connect on Demand VPN feature requires no additional Cisco Unified Presence and Cisco Unified Communications Manager configuration when deployed with a FQDN.

- The iPad must be set up for on-demand access to VPN with certificate-based authentication . Contact the providers of your VPN client for assistance with setting up VPN access.

- Determine if your Cisco Unified Presence and Cisco Unified Communications Manager servers use a Fully Qualified Domain Name or IP address for network identification.

- Configure Cisco Unified Communications Manager to be accessed through a domain name and not an IP address. Ensure this domain name is not resolvable outside the firewall. Include this domain in the Connect If Needed list in the Connect On Demand Domain List of the Cisco AnyConnect client connection.

- If you cannot use a domain name to access Cisco Unified Communications Manager or cannot make the DNS lookup of that domain name fail from outside the firewall, set the parameter in the following procedure to a nonexistent domain. This nonexistent domain would cause a DNS query to fail when the user is inside or outside the firewall. Add that domain to the Always Connect list in the Connect On Demand Domain List of the Cisco AnyConnect client connection. The URL must include only the domain name. Do not include a protocol or a path. See the following example for more information:

cm8ondemand.company.com

The URL must be a domain name only. Do not include a protocol or path.

Do the following to test this feature:

- Enter the URL identified in the procedure into Safari on the iPad and verify that VPN launches automatically. You should see a VPN icon in the status bar.

- Verify the iPad can connect to the corporate network using VPN by performing a task such as accessing a corporate intranet site. Contact your VPN provider for assistance if the connection does not work properly.

## Disabling Connect on Demand VPN in the Corporate Wireless Network

Perform the following steps to disable the Connect on Demand VPN feature in the corporate wireless network.

- Collect a list of corporate Wi-Fi SSIDs

## Set Up SIP Digest Authentication Options

SIP Digest Authentication is a Unified CM security feature that authenticates user devices. For more information, see the Cisco Unified Communications Manager Security Guide and the Cisco Unified Communications Manager Administration Guide , available from the maintenance guides list .

Cisco Jabber for Android does not support SIP Digest Authentication feature with the Dial via Office - Reverse feature.

- Disable SIP Digest Authentication—Disable SIP Digest Authentication if your deployment does not use this feature. See Disable SIP Digest Authentication .

- Users do not have to manually enter this password.

- There is less chance of entry error that prevents Cisco Jabber for Android from registering with Unified CM.

- The password is encrypted.

- Users must manually enter this password.

- Disable SIP Digest Authentication

- Enable SIP Digest Authentication with Automatic Password Authentication

- Enable SIP Digest Authentication with Manual Password Authentication

### Disable SIP Digest Authentication

- In the Enable SIP Digest Authentication drop-down list, select “Disabled.”

- Leave SIP Digest Username blank.

### Enable SIP Digest Authentication with Automatic Password Authentication

- Select Enable digest authentication .

- Deselect Exclude digest credentials in configuration file .

- In the User ID field, verify that the user ID is entered.

- In the Digest Credentials field, enter the digest credentials.

- In the Confirm Digest Credentials field, reenter the digest credentials.

- In the Device Security Profile list, select the phone security profile you just created.

- In the DigestUser list, select the digest user.

- Leave SIP Digest Username blank.

### Enable SIP Digest Authentication with Manual Password Authentication

- Select Enable digest authentication .

- Select Exclude digest credentials in configuration file .

- In the User ID field, verify that the user ID is entered.

- In the Digest Credentials field, enter the digest credentials.

- In the Confirm Digest Credentials field, reenter the digest credentials.

- In the Device Security Profile list, select the phone security profile you just created.

- In the DigestUser list, select the digest user.

- In the Enable SIP Digest Authentication list, select Enabled .

- For the SIP Digest Username , enter the digest user you just selected.

| Note | G.722.1 is supported in Cisco Unified Communications Manager 8.6.1 or later. |
|---|---|

| Audio | Interactive video (Main video) |
|---|---|
| The application uses the maximum audio bit rate. | The application allocates the remaining bit rate in this way: The maximum video call bit rate minus the audio bit rate |

| Port | Protocol | Description |
|---|---|---|
| Inbound |
| 16384-32766 | UDP | Receives Real-Time Transport Protocol (RTP) media streams for video and audio. You set up these ports in Cisco Unified Communications Manager. |
| Outbound |
| 69, then Ephemeral | TFTP | Connects to the Trivial File Transfer Protocol (TFTP) server to download the TFTP file |
| 80 and 6970 | HTTP | Connects to services such as Cisco WebEx Messenger for meetings and Cisco Unity Connection for voicemail features If no port is specified in a TFTP server address, Cisco Jabber Video for iPad will try port 6970 to obtain phone setup files and dial rule files. |
| 5060 | UDP/TCP | Provides Session Initiation Protocol (SIP) call signaling |
| 5061 | TCP | Provides secure SIP call signaling |
| 8443 | TCP | Connects to the Cisco Unified Communications Manager IP Phone (CCMCIP) server to get a list of currently assigned devices |
| 16384-32766 | UDP | UDP Sends RTP media streams for video and audio |
| 389 | TCP | Connects to the LDAP server for contact searches |
| 443 7080 | VMRest HTTPS | Connects to Cisco Unity Connection to retrieve and manage voice messages. |
| 636 | LDAPS | Connects to the secure LDAP server for contact searches |

| Step 1 | Sign in to Cisco Unified CM Administration. |
|---|---|
| Step 2 | Select System > Service Parameter . |
| Step 3 | Select Cisco CallManager Service . This setting is applied across the cluster. There is no need to set the Server field. |
| Step 4 | Set the SIP Trying Timer to 1000ms. |
| Step 5 | Set the SIP Dual Mode Alert Timer to 4500ms. |
| Step 6 | Select Save . |

| Note | The following Cisco Unified Communications Manager releases already contain the Tablet COP file: 7.1.5.35113-1 and above 8.5.1.16090-1 and above 8.6.2.23057-1 and above 9.0.1.11013-1-1 and above 9.1.1.10000-11 and above Installation of the Tablet COP file is not required for these releases. |
|---|---|

| Step 1 | Download the device COP file for iPad at http:/​/​www.cisco.com/​cisco/​software/​navigator.html?mdfid=280443139&flowid=29241 . |
|---|---|
| Step 2 | Place the COP file on an FTP or SFTP server that is accessible from your Unified CM servers. |
| Step 3 | Install the COP file on the Publisher server in your Unified CM cluster by following these steps: Select Cisco Unified OS Administration in the Navigation drop-down list and then select Go . Select Software Upgrades > Install/Upgrade . Specify the location of the COP file and provide the required information. For more information, see the online help. Select Next . Select the device COP file. Select Next . Follow the instructions on the screen. Select Next . Wait for the process to be completed. This process may take some time. Reboot Unified CM at a time of low usage. Restart the Cisco Tomcat service on the Unified CM server. This step, which clears the Tomcat image cache, is required for the device icon to display properly on the device list page in Unified CM. Enter this command from the CLI: utils service restart Cisco Tomcat Let the system fully return to service. Important: To avoid interruptions in service, ensure that each server has returned to active service before you perform this procedure on another server. |
| Step 4 | Install the COP file on each Subscriber server in the cluster. Use the same process you use for the Publisher, including rebooting the server. |

| Step 1 | Sign in to Cisco Unified CM Administration. |
|---|---|
| Step 2 | Select Device > Device Settings > SIP Profile . |
| Step 3 | Create a SIP profile or copy an existing SIP profile. You can name the profile "Standard iPad SIP Profile." |
| Step 4 | In the Parameters Used in Phone section, enter these values: Timer Register Delta (seconds)—120 Timer Register Expires (seconds)—720 Timer Keep Alive Expires (seconds)—720 Timer Subscribe Expires (seconds)—21600 Timer Subscribe Delta (seconds)—15 |
| Step 5 | Specify the port range in the following fields: Start Media Port—Defines the start port for media streams. This field sets the lowest port in the range. Stop Media Port—Defines the stop port for media streams. This field sets the highest port in the range. Note Cisco Jabber Video for iPad equally divides the port range that you set in the SIP profile. The client then uses the port range as follows: Lower half of the port range for audio streams Upper half of the port range for video streams For example, if you use a start media port of 3000 and an end media port of 4000, the client sends media through ports as follows: Ports 3000 to 3501 for audio streams Ports 3502 to 4000 for video streams As a result of splitting the port range for audio media and video media, the client creates identifiable media streams. You can then classify and prioritize those media streams by setting DSCP values in the IP packet headers. | Note | Cisco Jabber Video for iPad equally divides the port range that you set in the SIP profile. The client then uses the port range as follows: Lower half of the port range for audio streams Upper half of the port range for video streams For example, if you use a start media port of 3000 and an end media port of 4000, the client sends media through ports as follows: Ports 3000 to 3501 for audio streams Ports 3502 to 4000 for video streams As a result of splitting the port range for audio media and video media, the client creates identifiable media streams. You can then classify and prioritize those media streams by setting DSCP values in the IP packet headers. |
| Note | Cisco Jabber Video for iPad equally divides the port range that you set in the SIP profile. The client then uses the port range as follows: Lower half of the port range for audio streams Upper half of the port range for video streams For example, if you use a start media port of 3000 and an end media port of 4000, the client sends media through ports as follows: Ports 3000 to 3501 for audio streams Ports 3502 to 4000 for video streams As a result of splitting the port range for audio media and video media, the client creates identifiable media streams. You can then classify and prioritize those media streams by setting DSCP values in the IP packet headers. |
| Step 6 | Select Save . |

| Note | Cisco Jabber Video for iPad equally divides the port range that you set in the SIP profile. The client then uses the port range as follows: Lower half of the port range for audio streams Upper half of the port range for video streams For example, if you use a start media port of 3000 and an end media port of 4000, the client sends media through ports as follows: Ports 3000 to 3501 for audio streams Ports 3502 to 4000 for video streams As a result of splitting the port range for audio media and video media, the client creates identifiable media streams. You can then classify and prioritize those media streams by setting DSCP values in the IP packet headers. |
|---|---|

| Step 1 | Obtaining Cisco Options Package (COP) File for Dial Rules |
|---|---|
| Step 2 | Restarting the TFTP Service |

| Note | This procedure applies to only Cisco Unified Communications Manager Release 8.5 and earlier versions. The COP file described in this procedure is different from the device COP file that is used to make Cisco Jabber Video for iPad available as a device in Cisco Unified Communications Manager. |
|---|---|

| Step 1 | Go to the Software Downloads page for Cisco UC Integration for Microsoft Office Communicator at http:/​/​www.cisco.com/​cisco/​software/​release.html?mdfid=283665631&softwareid=283732952&release=8.6(2)&relind=AVAILABLE&rellifecycle=&reltype=latest . |
|---|---|
| Step 2 | Select the release number that most closely matches your Cisco Unified Communications Manager release. |
| Step 3 | Look for the bundle that contains the Administration Toolkit. |
| Step 4 | Select Download Now . |
| Step 5 | Find the instructions on the screen. |
| Step 6 | Unzip the downloaded file. |
| Step 7 | Locate the dial rules COP file in the CUCM folder. You do not need any other files in this download. |
| Step 8 | Place the dial rules COP file on a server that is accessible by TFTP. |

| Step 1 | In Unified CM Administration, select Cisco Unified Serviceability in the Navigation drop-down list and then select Go . |
|---|---|
| Step 2 | Select Tools > Control Center-Feature Services . |
| Step 3 | Select the server and select Go . |
| Step 4 | Select Cisco TFTP . |
| Step 5 | Select Restart . |
| Step 6 | Repeat this procedure on every server on which you ran this COP file. |

| Note | For details about setting up these features, see the Cisco Unified Communications Manager Features and Services Guide for your release at http:/​/​www.cisco.com/​en/​US/​products/​sw/​voicesw/​ps556/​prod_​maintenance_​guides_​list.html . |
|---|---|

| Usage and Error Tracking Setting | Information Collected |
|---|---|
| Enabled | Errors and warnings Screen views in the application (for example, how often users view their lists of voice messages) Feature activities (for example, how often users add a contact) The TFTP server address to which the application connects Approximate geographic location, based on mobile service provider activity |
| Detailed | Same information collected when Enabled is selected |
| Disabled | None |

| Step 1 | Sign in to Unified CM Administration. |
|---|---|
| Step 2 | Select Device > Phone . |
| Step 3 | Select Add New . |
| Step 4 | Select Cisco Jabber for Tablet in the drop-down list and then select Next . |
| Step 5 | Enter the information described in this table: Parameter Description Device Information Device Name A device name represents only one device. If a user has Cisco Jabber Video for iPad on multiple devices, set up each device with a different device name. must start with TAB , followed by up to 15 uppercased or numeric characters. Example: TABJOHND . can contain dot (.), dash (–), or underscore (_). Phone Button Template Select Standard Jabber for iPad . Protocol Specific Information Device Security Profile Select Cisco Jabber for iPad – Standard SIP Non-Secure Profile . SIP Profile Select the SIP profile you created. For details, see Setting Up a Dedicated SIP Profile . Product Specific Configuration Layout Enable LDAP User Authentication If you select Enabled , be sure to instruct the users to also turn on LDAP User Authentication in the application. LDAP Username Specify needed LDAP settings so that they are automatically entered in the application. LDAP Password LDAP Server LDAP Search Base LDAP Field Mappings Note Customization of this field is not currently supported. Enable LDAP SSL If you select Enabled , be sure to instruct the users to also turn on Use SSL in the application. Voicemail Username Specify voicemail settings so that they are automatically entered in the application. For details, see Setting Up Visual Voicemail . Voicemail Server Voicemail Message Store Username Voicemail Message Store Cisco Usage and Error Tracking Select the level of usage information that is available to Cisco. For more information, see Usage and Error Tracking . Video Capabilities Select Enabled if you want to turn on video for the users. On-Demand VPN URL The URL used by the Connect on Demand VPN feature. Preset Wi-Fi Networks Preset Wi-Fi network information for the device. Note You will specify other settings when you set up other features. | Parameter | Description | Device Information | Device Name | A device name represents only one device. If a user has Cisco Jabber Video for iPad on multiple devices, set up each device with a different device name. must start with TAB , followed by up to 15 uppercased or numeric characters. Example: TABJOHND . can contain dot (.), dash (–), or underscore (_). | Phone Button Template | Select Standard Jabber for iPad . | Protocol Specific Information | Device Security Profile | Select Cisco Jabber for iPad – Standard SIP Non-Secure Profile . | SIP Profile | Select the SIP profile you created. For details, see Setting Up a Dedicated SIP Profile . | Product Specific Configuration Layout | Enable LDAP User Authentication | If you select Enabled , be sure to instruct the users to also turn on LDAP User Authentication in the application. | LDAP Username | Specify needed LDAP settings so that they are automatically entered in the application. | LDAP Password | LDAP Server | LDAP Search Base | LDAP Field Mappings | Note Customization of this field is not currently supported. | Note | Customization of this field is not currently supported. | Enable LDAP SSL | If you select Enabled , be sure to instruct the users to also turn on Use SSL in the application. | Voicemail Username | Specify voicemail settings so that they are automatically entered in the application. For details, see Setting Up Visual Voicemail . | Voicemail Server | Voicemail Message Store Username | Voicemail Message Store | Cisco Usage and Error Tracking | Select the level of usage information that is available to Cisco. For more information, see Usage and Error Tracking . | Video Capabilities | Select Enabled if you want to turn on video for the users. | On-Demand VPN URL | The URL used by the Connect on Demand VPN feature. | Preset Wi-Fi Networks | Preset Wi-Fi network information for the device. | Note | You will specify other settings when you set up other features. |
| Parameter | Description |
| Device Information |
| Device Name | A device name represents only one device. If a user has Cisco Jabber Video for iPad on multiple devices, set up each device with a different device name. must start with TAB , followed by up to 15 uppercased or numeric characters. Example: TABJOHND . can contain dot (.), dash (–), or underscore (_). |
| Phone Button Template | Select Standard Jabber for iPad . |
| Protocol Specific Information |
| Device Security Profile | Select Cisco Jabber for iPad – Standard SIP Non-Secure Profile . |
| SIP Profile | Select the SIP profile you created. For details, see Setting Up a Dedicated SIP Profile . |
| Product Specific Configuration Layout |
| Enable LDAP User Authentication | If you select Enabled , be sure to instruct the users to also turn on LDAP User Authentication in the application. |
| LDAP Username | Specify needed LDAP settings so that they are automatically entered in the application. |
| LDAP Password |
| LDAP Server |
| LDAP Search Base |
| LDAP Field Mappings | Note Customization of this field is not currently supported. | Note | Customization of this field is not currently supported. |
| Note | Customization of this field is not currently supported. |
| Enable LDAP SSL | If you select Enabled , be sure to instruct the users to also turn on Use SSL in the application. |
| Voicemail Username | Specify voicemail settings so that they are automatically entered in the application. For details, see Setting Up Visual Voicemail . |
| Voicemail Server |
| Voicemail Message Store Username |
| Voicemail Message Store |
| Cisco Usage and Error Tracking | Select the level of usage information that is available to Cisco. For more information, see Usage and Error Tracking . |
| Video Capabilities | Select Enabled if you want to turn on video for the users. |
| On-Demand VPN URL | The URL used by the Connect on Demand VPN feature. |
| Preset Wi-Fi Networks | Preset Wi-Fi network information for the device. |
| Note | You will specify other settings when you set up other features. |
| Step 6 | Select Save . |
| Step 7 | Select Apply Config . |
| Step 8 | Select [Line n] - Add a new DN . |
| Step 9 | Enter the directory number of this device. |
| Step 10 | If this device is a standalone device (not sharing a DN with a desk phone), specify these settings to forward calls when the application is not running and connected to the network so callers do not receive an error message: Forward Unregistered Internal Forward Unregistered External For more information about these settings, see the online help in Cisco Unified Communications Manager. |
| Step 11 | Set the No Answer Ring Duration to 24 seconds to allow time for the application to ring before calls go to voicemail. See general restrictions in the online help in Cisco Unified Communications Manager. |
| Step 12 | Specify other settings as appropriate for your environment. |
| Step 13 | Select Save . |
| Step 14 | Associate the device that you just created with the user by following these steps: Select User Management > End User . Search for and select the user. In the Device Information section, select Device Association . Check the device that you want to associate with the user. Select Save Selected/Changes . |
| Step 15 | If this user has a desk phone, select the desk phone as the Primary User Device. Note The Primary User Device field is only available in Cisco Unified Communications Manager 9.0 and earlier. This field does not need to specified in later versions of Cisco Unified Communications Manager. | Note | The Primary User Device field is only available in Cisco Unified Communications Manager 9.0 and earlier. This field does not need to specified in later versions of Cisco Unified Communications Manager. |
| Note | The Primary User Device field is only available in Cisco Unified Communications Manager 9.0 and earlier. This field does not need to specified in later versions of Cisco Unified Communications Manager. |
| Step 16 | If the device is a standalone device that runs without an associated desk phone, you may need to enter other information that is standard for all devices in your system. |

| Parameter | Description |
|---|---|
| Device Information |
| Device Name | A device name represents only one device. If a user has Cisco Jabber Video for iPad on multiple devices, set up each device with a different device name. must start with TAB , followed by up to 15 uppercased or numeric characters. Example: TABJOHND . can contain dot (.), dash (–), or underscore (_). |
| Phone Button Template | Select Standard Jabber for iPad . |
| Protocol Specific Information |
| Device Security Profile | Select Cisco Jabber for iPad – Standard SIP Non-Secure Profile . |
| SIP Profile | Select the SIP profile you created. For details, see Setting Up a Dedicated SIP Profile . |
| Product Specific Configuration Layout |
| Enable LDAP User Authentication | If you select Enabled , be sure to instruct the users to also turn on LDAP User Authentication in the application. |
| LDAP Username | Specify needed LDAP settings so that they are automatically entered in the application. |
| LDAP Password |
| LDAP Server |
| LDAP Search Base |
| LDAP Field Mappings | Note Customization of this field is not currently supported. | Note | Customization of this field is not currently supported. |
| Note | Customization of this field is not currently supported. |
| Enable LDAP SSL | If you select Enabled , be sure to instruct the users to also turn on Use SSL in the application. |
| Voicemail Username | Specify voicemail settings so that they are automatically entered in the application. For details, see Setting Up Visual Voicemail . |
| Voicemail Server |
| Voicemail Message Store Username |
| Voicemail Message Store |
| Cisco Usage and Error Tracking | Select the level of usage information that is available to Cisco. For more information, see Usage and Error Tracking . |
| Video Capabilities | Select Enabled if you want to turn on video for the users. |
| On-Demand VPN URL | The URL used by the Connect on Demand VPN feature. |
| Preset Wi-Fi Networks | Preset Wi-Fi network information for the device. |

| Note | Customization of this field is not currently supported. |
|---|---|

| Note | You will specify other settings when you set up other features. |
|---|---|

| Note | The Primary User Device field is only available in Cisco Unified Communications Manager 9.0 and earlier. This field does not need to specified in later versions of Cisco Unified Communications Manager. |
|---|---|

| Step 1 | Select User Management > End User in Cisco Unified Communications Manager Administration. |
|---|---|
| Step 2 | Search for and select the user you want to add. |
| Step 3 | Select Add to User Group in the Permissions Information section. |
| Step 4 | Search for "Standard CTI" in the Find and List User Groups window. |
| Step 5 | Select Standard CTI Enabled . If the user's phone is a Cisco Unified IP Phone 6900, 8900 or 9900 series model, also select Standard CTI Allow Control of Phones supporting Xfer and conf . |
| Step 6 | Select Add Selected . |
| Step 7 | Select Save . |

| Note | LDAP authentication does not apply to the passwords of application users; Cisco Unified Communications Manager authenticates application users in its internal database. |
|---|---|

| Step 1 | Select Cisco Unified Communications Manager Administration > System > LDAP > LDAP Authentication . |
|---|---|
| Step 2 | Check Use LDAP Authentication for End Users . |
| Step 3 | Specify the LDAP authentication settings. |
| Step 4 | Specify the LDAP server hostname or IP address and port number. Note To use Secure Socket Layer (SSL) to communicate with the LDAP directory, check Use SSL . | Note | To use Secure Socket Layer (SSL) to communicate with the LDAP directory, check Use SSL . |
| Note | To use Secure Socket Layer (SSL) to communicate with the LDAP directory, check Use SSL . |
| Step 5 | Select Save . Tip If you set up LDAP over SSL, upload the LDAP directory certificate to Cisco Unified Communications Manager. | Tip | If you set up LDAP over SSL, upload the LDAP directory certificate to Cisco Unified Communications Manager. |
| Tip | If you set up LDAP over SSL, upload the LDAP directory certificate to Cisco Unified Communications Manager. |

| Note | To use Secure Socket Layer (SSL) to communicate with the LDAP directory, check Use SSL . |
|---|---|

| Tip | If you set up LDAP over SSL, upload the LDAP directory certificate to Cisco Unified Communications Manager. |
|---|---|

| Step 1 | Select Cisco Unified Communications Manager Administration > System > LDAP > LDAP System . |
|---|---|
| Step 2 | Select Add New . |
| Step 3 | Set up the LDAP server type and attribute. |
| Step 4 | Select Enable Synchronizing from LDAP Server . |
| Step 5 | Click Save . |
| Step 6 | Select Cisco Unified Communications Manager Administration > System > LDAP > LDAP Directory . |
| Step 7 | Select Add New . |
| Step 8 | Set up these items: LDAP directory account settings User attributes to be synchronized Synchronization schedule LDAP server hostname or IP address and port number |
| Step 9 | Check Use SSL if you want to use Secure Socket Layer (SSL) to communicate with the LDAP directory. |
| Step 10 | Click Save . Tip If you configure LDAP over SSL, upload the LDAP directory certificate onto Cisco Unified Communications Manager. See the LDAP directory content in the Cisco Unified Communications Manager SRND for information on the account synchronization mechanism for specific LDAP products and general best practices for LDAP synchronization. | Tip | If you configure LDAP over SSL, upload the LDAP directory certificate onto Cisco Unified Communications Manager. See the LDAP directory content in the Cisco Unified Communications Manager SRND for information on the account synchronization mechanism for specific LDAP products and general best practices for LDAP synchronization. |
| Tip | If you configure LDAP over SSL, upload the LDAP directory certificate onto Cisco Unified Communications Manager. See the LDAP directory content in the Cisco Unified Communications Manager SRND for information on the account synchronization mechanism for specific LDAP products and general best practices for LDAP synchronization. |

| Tip | If you configure LDAP over SSL, upload the LDAP directory certificate onto Cisco Unified Communications Manager. See the LDAP directory content in the Cisco Unified Communications Manager SRND for information on the account synchronization mechanism for specific LDAP products and general best practices for LDAP synchronization. |
|---|---|

| Step 1 | Sign in to Cisco Unified CM Administration. |
|---|---|
| Step 2 | Go to the device page for the user. |
| Step 3 | In the Product Specific Configuration Layout section, enter these voicemail settings: Setting Description Voicemail Username Enter the unique username for voicemail access for this user. Voicemail Server (include the port) For the voicemail server, enter the hostname or IP address. Use the format Servername.YourCompany.com:portnumber . Voicemail Message Store Username Enter the username for the voicemail message store. Voicemail Message Store For the voicemail message store, enter the hostname or IP address. This may be the same as the voicemail server. Use the format YourVoiceMessageStoreServer.yourcompany.com:portnumber . | Setting | Description | Voicemail Username | Enter the unique username for voicemail access for this user. | Voicemail Server (include the port) | For the voicemail server, enter the hostname or IP address. Use the format Servername.YourCompany.com:portnumber . | Voicemail Message Store Username | Enter the username for the voicemail message store. | Voicemail Message Store | For the voicemail message store, enter the hostname or IP address. This may be the same as the voicemail server. Use the format YourVoiceMessageStoreServer.yourcompany.com:portnumber . |
| Setting | Description |
| Voicemail Username | Enter the unique username for voicemail access for this user. |
| Voicemail Server (include the port) | For the voicemail server, enter the hostname or IP address. Use the format Servername.YourCompany.com:portnumber . |
| Voicemail Message Store Username | Enter the username for the voicemail message store. |
| Voicemail Message Store | For the voicemail message store, enter the hostname or IP address. This may be the same as the voicemail server. Use the format YourVoiceMessageStoreServer.yourcompany.com:portnumber . |
| Step 4 | Select Save . |

| Setting | Description |
|---|---|
| Voicemail Username | Enter the unique username for voicemail access for this user. |
| Voicemail Server (include the port) | For the voicemail server, enter the hostname or IP address. Use the format Servername.YourCompany.com:portnumber . |
| Voicemail Message Store Username | Enter the username for the voicemail message store. |
| Voicemail Message Store | For the voicemail message store, enter the hostname or IP address. This may be the same as the voicemail server. Use the format YourVoiceMessageStoreServer.yourcompany.com:portnumber . |

| Note | Cisco recommends that Cisco Unified Presence and Cisco Unified Communications Manager be deployed with a FQDN. Use of the Connect on Demand VPN feature requires no additional Cisco Unified Presence and Cisco Unified Communications Manager configuration when deployed with a FQDN. |
|---|---|

| Use | Do Not Use |
|---|---|
| cm8ondemand.company.com | https://cm8ondemand.company.com/vpn |

| Step 1 | Sign in to Cisco Unified CM Administration. |
|---|---|
| Step 2 | Go to the device page for the user. |
| Step 3 | Go to the Product Specific Configuration Layout section. |
| Step 4 | Enter the URL you identified before beginning this procedure in the On-Demand VPN URL field. Note The URL must be a domain name only. Do not include a protocol or path. | Note | The URL must be a domain name only. Do not include a protocol or path. |
| Note | The URL must be a domain name only. Do not include a protocol or path. |
| Step 5 | Select Save . |

| Note | The URL must be a domain name only. Do not include a protocol or path. |
|---|---|

| Step 1 | Sign in to Cisco Unified CM Administration. |
|---|---|
| Step 2 | Go to the device page for the user. |
| Step 3 | Go to the Product Specific Configuration Layout section. |
| Step 4 | Set the Preset Wi-Fi Networks to up to three corporate Wi-Fi SSIDs separated by a slash (/). |
| Step 5 | Select Save . |

| Note | Cisco Jabber for Android does not support SIP Digest Authentication feature with the Dial via Office - Reverse feature. |
|---|---|

| Step 1 | Sign in to the Unified CM Administration portal. |
|---|---|
| Step 2 | Navigate to the device page. |
| Step 3 | In the Device Security Profile drop-down list, select "Cisco Jabber for Tablet - Standard SIP Non-secure profile." |
| Step 4 | Complete the authentication details in the Product Specific Configuration Layout section. In the Enable SIP Digest Authentication drop-down list, select “Disabled.” Leave SIP Digest Username blank. |
| Step 5 | Restart Cisco Jabber . |

| Step 1 | Create a new security profile for Cisco Jabber For Tablet under System > Security > Phone Security Profile . Select Enable digest authentication . Deselect Exclude digest credentials in configuration file . |
|---|---|
| Step 2 | On each End User page, in the User Information section, complete the following tasks: In the User ID field, verify that the user ID is entered. In the Digest Credentials field, enter the digest credentials. In the Confirm Digest Credentials field, reenter the digest credentials. |
| Step 3 | On each Cisco Jabber for Tablet device page, complete the profile information in the Protocol Specific Information section. In the Device Security Profile list, select the phone security profile you just created. In the DigestUser list, select the digest user. |
| Step 4 | On the same device page, complete the authentication details in the Product Specific Configuration Layout section: Leave SIP Digest Username blank. |
| Step 5 | Restart Cisco Jabber . |

| Step 1 | Create a new profile for Cisco Jabber For Tablet under System > Security > Phone Security Profile . Select Enable digest authentication . Select Exclude digest credentials in configuration file . |
|---|---|
| Step 2 | On each End User page, in the User Information section, complete the following tasks: In the User ID field, verify that the user ID is entered. In the Digest Credentials field, enter the digest credentials. In the Confirm Digest Credentials field, reenter the digest credentials. Make a note of this password. You provide this password to the user later. |
| Step 3 | On each Cisco Jabber for Tablet device page, complete the profile information in the Protocol Specific Information section. In the Device Security Profile list, select the phone security profile you just created. In the DigestUser list, select the digest user. |
| Step 4 | On the same device page, complete the authentication details in the Product Specific Configuration Layout section: In the Enable SIP Digest Authentication list, select Enabled . For the SIP Digest Username , enter the digest user you just selected. |
| Step 5 | Restart Cisco Jabber and step through the setup wizard again. |