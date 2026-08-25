---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-4fe6ba3fb3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_0111.html
retrieved_at: 2026-08-25T21:46:25.773977+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Configure Voice and Video Communication

## Chapter: Configure Voice and Video Communication

# Configure Voice and Video Communication

## Configure Voice and Video Communications for On-Premises Deployments

Complete this
				task to make Cisco Jabber available as a device in Cisco Unified Communications
				Manager.

This is
				applicable for Cisco Unified Communications Manager release 9.x and later only.

Complete this
				task if you have Cisco Unified Communications Manager Release 8.6 and you plan
				to enable video desktop sharing.

Complete this
				task if you have Cisco Unified Communications Manager release 9 or earlier and
				plan to configure devices for mobile clients.

Complete this
				task to setup secure phone capabilities for all devices.

Complete this
				task if you plan to assign Cisco Jabber for Mac or Cisco Jabber for Windows
				users to CTI remote devices.

Complete this
				task if you plan to assign Cisco Jabber for Mac or Cisco Jabber for Windows
				users to CTI remote devices.

Complete this
				only if you have Cisco Unified Communications Manager Release 8.6 with Cisco
				Unified Presence.

Create at
				least one device for every user that will access Cisco Jabber.

Only if
				installing Cisco Jabber for Mac

### Install Cisco
	 Options Package File for Devices

To make 
		  Cisco Jabber
		  available as a device in 
		  Cisco Unified Communications Manager,
		  you must install a device-specific Cisco Options Package (COP) file on all your
		  
		  Cisco Unified Communications Manager
		  nodes.

Perform this
		  procedure at a time of low usage; it can interrupt service.

General
		  information about installing COP files is available in the “Software Upgrades”
		  chapter in the Cisco Unified
			 Communications Operating System Administration Guide for your release.

Go to
						  the software downloads
							 site .

Locate
						  the device COP file for your release.

- Click Download Now .

You will
					 need this information later.

- Click Proceed with Download and follow the instructions.

- Open the Cisco Unified OS Administration interface.

- Select Software
						Upgrades > Install/Upgrade .

For more
					 information, see the online help.

- Select Next .

- Select the
				  device COP file.

- Select Next .

- Follow the
				  instructions on the screen.

Wait for
					 the process to complete. This process can take some time.

- Reboot 
				  Cisco Unified Communications Manager
				  at a time of low usage.

To avoid
						interruptions in service, make sure each node returns to active service before
						you perform this procedure on another server.

Use the same process you used for the Publisher, including rebooting the node.

### Apply COP File for BFCP
		Capabilities

You must apply cmterm-bfcp-e.8-6-2.cop.sgn to configure video
		  desktop sharing on 
		  Cisco
				Unified Communication Manager release 8.6.2 and later. This COP
		  file adds an option to enable BFCP on the CSF device.

You must
					 install the COP file each time you upgrade. For example, if you configure video
					 desktop sharing on 
					 Cisco
				Unified Communication Manager Release 8.6.2 .20000-1 and then upgrade to 
					 Cisco
				Unified Communication Manager Release 8.6.2 .20000-2, you must apply the
					 COP file on 
					 Cisco
				Unified Communication Manager Release 8.6.2 .20000-2.

If you
					 configure video desktop sharing on 
					 Cisco
				Unified Communication Manager Release 8.6.1 and then upgrade to 
					 Cisco
				Unified Communication Manager release 8.6.2, you must apply the COP file
					 on 
					 Cisco
				Unified Communication Manager release 8.6.2 before you can configure video
					 desktop sharing.

- Open the Cisco Unified OS Administration interface.

- Select Settings > Version .

- Select Restart .

- Repeat the
				  preceding steps for each node in the cluster, starting with your presentation
				  server.

The COP add the Allow
			 Presentation Sharing using BFCP field to the Protocol
			 Specific Information section on the Phone
			 Configuration window for CSF devices.

### Create SIP
	 Profiles

This procedure is
		  required only when you use 
		  Cisco
				Unified Communication Manager release 9 or earlier and are
		  configuring devices for mobile clients. Use the default SIP profile provided
		  for desktop clients.

If you use 
		  Cisco
				Unified Communication Manager release 9 or earlier, before you create and configure devices for mobile clients, you must create a SIP profile  that allows 
		  Cisco Jabber to stay connected to 
		  Cisco
				Unified Communication Manager while 
		  Cisco Jabber runs in the background.

If you use 
		  Cisco
				Unified Communication Manager Release 10, choose the Standard
			 SIP Profile for Mobile Device default profile when
		  you create and configure devices for mobile clients.

Install Cisco Options Package File for Devices

The Find and List SIP Profiles window opens.

- Find the default SIP profile and create a copy that you can edit.

- Select Add New and create a new SIP profile.

- Timer Register Delta to 120

- Timer Register Expires to 720

- Timer Keep Alive Expires to 720

- Timer Subscribe Expires to 21600

- Timer Subscribe Delta to 15

Setting up System SIP Parameters

#### Setting up System
	 SIP Parameters

If you are
		  connected to a low-bandwidth network and finding it difficult to take an
		  incoming call on your mobile device, you can set the system SIP parameters to
		  improve the condition. Increase the SIP Dual Mode Alert Timer value to ensure
		  that calls to the Cisco Jabber extension are not prematurely routed to the
		  mobile-network phone number.

This configuration
		  is only for mobile clients.

Cisco Jabber must
		  be running to receive work calls.

If, after
				  you increase the SIP Dual Mode Alert Timer value, incoming calls that arrive in
				  Cisco Jabber are still terminated and diverted using Mobile Connect, you can
				  increase the SIP Dual Mode Alert Timer value again in increments of 500
				  milliseconds.

### Configure the
	 Phone Security Profile

You can optionally set up secure phone capabilities for all
		  devices. Secure phone capabilities provide secure SIP signaling, secure media
		  streams, and encrypted device configuration files.

If you enable secure phone capabilities for users, device
		  connections to Cisco Unified Communications Manager are secure. However, calls
		  with other devices are secure only if both devices have a secure connection.

Configure the
				Cisco Unified Communications Manager security mode using the Cisco CTL Client.
				At minimum, select mixed mode security.

For
				instructions on how to configure mixed mode with the Cisco CTL Client, see the Cisco Unified Communications Manager Security Guide .

For conference
				calls, ensure that the conferencing bridge supports secure phone capabilities.
				If the conferencing bridge does not support secure phone capabilities, calls to
				that bridge are not secure. Likewise, all parties must support a common
				encryption algorithm for the client to encrypt media on conference calls.

- Cisco Unified Client
				  Services Framework —Select this option to create a CSF device for
				Cisco Jabber for Mac or Cisco Jabber for Windows.

- Cisco Dual Mode for
				  iPhone —Select this option to create a TFT device for an iPhone.

- Cisco Jabber for
				  Tablet —Select this option to create a TAB device for an iPad or
				an Android tablet.

- Cisco Dual Mode for
				  Android —Select this option to create a BOT device for an Android
				device.

CTI remote
				  devices are virtual devices that monitor and have call control over a user's
				  remote destination.

- Authenticated —The SIP connection is over TLS using NULL-SHA encryption.

- Encrypted —The
				SIP connection is over TLS using AES 128/SHA encryption. The client uses Secure
				Real-time Transport Protocol (SRTP) to offer encrypted media streams.

For a
				  TCT/BOT/Tablet device, do not select the TFTP Encrypted Config check box here. For
				  Authentication Mode, select By Authentication String or Null String.

Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail.

The Cisco
				Jabber clients were tested using authentication strings with 1024-bit length
				keys. The Cisco Jabber clients require more time to generate 2048-bit length
				keys than 1024-bit length keys. As a result, if you select 2048, expect it to take longer to complete the CAPF enrollment process.

The port that
				you specify in this field takes effect only if you select Non
				  Secure as the value for Device Security Mode .

### Enable User
		Mobility

This task is
		  only for desktop
		clients.

You must enable
		  user mobility to provision CTI remote devices. If you do not enable mobility
		  for users, you cannot assign those users as owners of CTI remote devices.

This task is
		  applicable only if:

You plan to
				assign Cisco Jabber for Mac or Cisco Jabber for Windows users to CTI remote
				devices.

You have Cisco
				Unified Communication Manager release 9.x and later.

The Find
				  and List Users window opens.

The End
				  User Configuration window opens.

### Add a CTI Service

The CTI service provides Jabber with the address of the UDS device service. The UDS device service 	provides a list of devices associated with the user.

The Find and List UC Services window opens.

The UC Service Configuration window opens.

The name you specify displays when you add services to profiles. Ensure the name you specify is unique, meaningful, and easy to identify.

- Specify the CTI service address in the Host Name/IP Address field.

- Specify the port number for the CTI service in the Port field.

Add the CTI service to your service profile.

#### Apply a CTI Service

After you add a CTI service on Cisco Unified
				  Communications Manager , you must apply it to a service profile so that the client can retrieve the settings.

Create a service profile if none already exists or if you require a separate service profile for CTI.

Add a CTI service.

Primary

Secondary

Tertiary

### Add a CTI Gateway Server

This task is applicable only if you have CUCM 8.6 with CUP.

The client requires a CTI gateway to communicate with Cisco Unified Communications Manager and perform certain functions such as desk phone control. The first step to set up a CTI gateway is to add a CTI gateway server on Cisco Unified Presence .

In some versions of Cisco Unified Presence , this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Server .

The Find and List CTI Gateway Servers window opens.

The CTI Gateway Server Configuration window opens.

Create a CTI Gateway Profile

#### Create a CTI Gateway Profile

After you add a CTI gateway server, you must create a CTI gateway profile and add that server to the profile.

Add a CTI Gateway Server

In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Profile .

### Video Desktop
	 Sharing

Binary Floor
		  Control Protocol (BFCP) provides video desktop sharing capabilities for
		  software phone devices, also known as CSF devices. Cisco Unified Communications
		  Manager handles the BFCP packets that users transmit when using video desktop
		  sharing capabilities. On Cisco Unified Communications Manager version 9.0(1)
		  and later, BFCP presentation sharing is automatically enabled. For this reason,
		  you do not need to perform any steps to enable video desktop sharing on CSF
		  devices.

Cisco
				Jabber for mobile clients can only receive BFCP.

You can
					 enable video desktop sharing only on software phone devices. You cannot enable
					 video desktop sharing on desk phone devices.

Users must
					 be on active calls to use video desktop sharing capabilities. You can only
					 initiate video desktop sharing sessions from active calls.

If
						  users initiate desktop sharing sessions during an instant messaging session,
						  Cisco WebEx provides desktop sharing capabilities.

If
						  users initiate desktop sharing sessions during an audio or video conversation,
						  Cisco Unified Communications Manager provides desktop sharing capabilities.

- Video desktop sharing using
		  BFCP is not supported if Trusted
			 Relay Point or Media
			 Termination Point are enabled on the software phone device.

Video desktop sharing using BFCP is not supported during Cisco Jabber multi-party conference calls unless Cisco TelePresence MCU is deployed.

Select Allow Presentation Sharing using BFCP in the Trunk
					 Specific Configuration section of the SIP profile.

Select the
					 SIP profile from the SIP Profile drop-down list on the CSF device
					 configuration.

### Create and
	 Configure Cisco Jabber Devices

Create at least one device for every user that accesses Cisco
		  Jabber. A user can have multiple devices.

Users can only
			 remove participants from a conference call when using the softphone(CSF) device
			 for calls.

Install COP
				files.

Enable
				mobility for each user for whom you plan to assign to a CTI remote device.

Create SIP
				profiles if you have Cisco Unified Communications Manager release 9 or earlier
				and plan to configure devices for mobile clients.

Create the
				Phone Security Profile if you plan to set up secure phone capabilities for all
				devices.

For Cisco
				Unified Communications Manager release 10 or later, ensure that the Cisco
				Certificate Authority Proxy Function (CAPF) service parameters value for Certificate Issuer to Endpoint is Cisco Certificate Authority Proxy Function , this is
				the only option supported by Cisco Jabber. For information on configuring the
				CAPF service parameter see the Update
				  CAPF Service Parameters topic in the Cisco Unified Communications Manager Security Guides .

Before you create TCT devices, BOT devices, or TAB devices for Cisco Jabber for mobile users, specify the organization top domain name to support registration between Cisco Jabber and the Cisco Unified Communications Manager.  In Unified CM Administration interface, select System > Enterprise Parameters . Under the Clusterwide Domain Configuration  section, enter the organization top domain name. For example, cisco.com. This top domain name is used by Jabber as the DNS domain of the Cisco Unified Communications Manager servers for phone registration. For example, CUCMServer1@cisco.com.

For Jabber users, you can only create one type of device per user although you can create multiple devices for each user. For example, you can create one tablet device and one CSF device but not two CSF devices.

- Cisco Unified Client Services Framework —Select this option to create a CSF device for Cisco Jabber for Mac or Cisco Jabber for Windows.

- Cisco Dual Mode for iPhone —Select this option to create a TCT device for an iPhone.

- Cisco Jabber for Tablet —Select this option to create a TAB device for an iPad or an Android tablet.

- Cisco Dual Mode for Android —Select this option to create a BOT device for an Android device.

CTI remote devices are virtual devices that monitor and have call control over a user's remote destination.

For the Cisco Unified Client Services Framework option in a
				Phone mode deployment, ensure that User is selected.

If
							 You Select

Required Format

CTI Remote
								Device

When you select Owner User ID , the device name field populates with CTIRD<owner user ID> . You can change this value.
								  The device name does not have to begin with CTIRD .

Valid characters: a–z, A–Z, 0–9, period (.), underscore (_),
								  hyphen (-).

15-character limit.

Cisco Unified Client
								Services Framework

Valid characters: a–z, A–Z, 0–9.

15-character limit.

Cisco Dual Mode for
								iPhone

The device name must begin with TCT .

For example, if you create a TCT device for user, Tanya Adams,
								  whose username is tadams, enter TCTTADAMS .

Must be uppercase.

Valid characters:  A–Z, 0–9, period (.), underscore (_),
								  hyphen (-).

15-character limit.

Cisco Jabber for
								Tablet

The device name must begin with TAB .

For example, if you create a TAB device for user, Tanya Adams,
								  whose username is tadams, enter TABTADAMS .

Must be uppercase.

Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-).

15-character limit.

Cisco Dual Mode for
								Android

The device name must begin with BOT .

For example, if you create a BOT device for user, Tanya Adams,
								  whose username is tadams, enter BOTTADAMS .

Must be uppercase.

Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-).

15-character limit.

The Rerouting
				Calling Search Space defines the calling search space for rerouting and ensures
				that users can send and receive calls from the CTI remote device.

Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail.

Add a Directory
		  Number to the device.

#### Add a Directory Number to the Device

After you create and configure each device, you must add
		  a directory number to the device. This topic provides instructions on
		  adding directory numbers using the Device > Phone menu option.

Create a device.

#### Add a Remote Destination

Remote destinations represent the CTI controllable devices that are available to users.

You should add a remote destination through the Cisco Unified CM Administration interface if you plan to provision users with dedicated CTI remote devices. This task ensures that users can automatically control their phones and place calls  when they start the client.

If you plan to provision users with CTI remote devices along with software phone devices and desk phone devices, you should not add a remote destination through the Cisco Unified CM Administration interface. Users can enter remote destinations through the client interface.

You should create only one remote destination per user. Do not add two or more remote destinations for a user.

Cisco Unified Communications Manager does not verify if it can route remote destinations that you add through the Cisco Unified CM Administration interface. For this reason, you must ensure that Cisco Unified Communications Manager can route the remote destinations you add.

Cisco Unified Communications Manager automatically applies application dial rules to all remote destination numbers for CTI remote devices.

The Find and List Phones window opens.

The Phone Configuration window opens.

The Remote Destination Information window opens.

You must specify JabberRD in the Name field. The client uses only the JabberRD remote destination. If you specify a name other than JabberRD, users cannot access that remote destination.

Repeat the steps to open the Phone Configuration window for the CTI remote device.

Locate the Associated Remote Destinations section.

Verify the remote destination is available.

Select Apply Config .

The Device Information section on the Phone Configuration window contains a Active Remote Destination field.

When users select a remote destination in the client, it displays as the value of Active Remote Destination .

Users do not select a remote destination in the client.

Users exit or are not signed in to  the client.

### Provide Users with
	 Authentication Strings

Users must specify the authentication string in the client interface to access their devices and securely register with Cisco Unified Communications Manager.

The time it takes for the enrollment process to complete can vary depending on the user's computer or mobile device and the current load for Cisco Unified Communications Manager. It can take up to one minute for the client to complete the CAPF enrollment process.

Users enter an
				incorrect authentication string.

Users can attempt to enter authentication strings again to complete the CAPF enrollment. However, if a user continually enters an incorrect authentication string, the client might reject any string the user enters, even if the string is correct. In this case, you must generate a new authentication string on the user's device and then provide it to the user.

Users do not
				enter the authentication string before the expiration time you set in the Operation Completes By field.

In this case, you must generate a new authentication string on the user's device. The user must then enter that authentication string before the expiration time.

Standard CCM End
						Users

Standard CTI
						Enabled

Users must not
		  belong to the Standard CTI Secure
				  Connection user group.

### Desk Phone Video
		Configuration

Desk phone video
		capabilities let users receive video transmitted to their desk phone devices on
		their computers through the client.

#### Set Up Desk Phone
			 Video

Physically
				connect the computer to the computer port on the desk phone device.

You must
				physically connect the computer to the desk phone device through the computer
				port so that the client can establish a connection to the device. You cannot
				use desk phone video capabilities with wireless connections to desk phone
				devices.

If users
					 have both wireless and wired connections available, they should configure
					 Microsoft Windows so that wireless connections do not take priority over wired
					 connections. See the following Microsoft documentation for more information: An
						explanation of the Automatic Metric feature for Internet Protocol
						routes .

Enable the
				desk phone device for video in Cisco Unified Communications Manager.

Install Cisco
				Media Services Interface on the computer.

Discover
					 the desk phone device.

Establish
					 and maintain a connection to the desk phone device using the CAST protocol.

Download the Cisco Media Services Interface installation program
				  from the download site on cisco.com .

#### Desk Phone Video Considerations

You cannot use
				desk phone video capabilities on devices if video cameras are attached to the
				devices, such as a Cisco Unified IP Phone 9971. You can use desk phone video
				capabilities if you remove video cameras from the devices.

You cannot use
				desk phone video capabilities with devices that do not support CTI.

Video desktop
				sharing, using the BFCP protocol, is not supported with desk phone video.

It is not
				possible for endpoints that use SCCP to receive video only. SCCP endpoints must
				send and receive video. Instances where SCCP endpoints do not send video result
				in audio only calls.

7900 series
				phones must use SCCP for desk phone video capabilities. 7900 series phones
				cannot use SIP for desk phone video capabilities.

If a user
				initiates a call from the keypad on a desk phone device, the call starts as an
				audio call on the desk phone device. The client then escalates the call to
				video. For this reason, you cannot make video calls to devices that do not
				support escalation, such as H.323 endpoints. To use desk phone video
				capabilities with devices that do not support escalation, users should initiate
				calls from the client.

A
				compatibility issue exists with Cisco Unified IP Phones that use firmware
				version SCCP45.9-2-1S. You must upgrade your firmware to version SCCP45.9-3-1
				to use desk phone video capabilities.

Some antivirus
				or firewall applications, such as Symantec EndPoint Protection, block inbound
				CDP packets, which disables desk phone video capabilities. You should configure
				your antivirus or firewall application to allow inbound CDP packets.

See the
				following Symantec technical document for additional details about this issue: Cisco
				  IP Phone version 7970 and Cisco Unified Video Advantage is Blocked by Network
				  Threat Protection .

You must not
				select the Media Termination Point Required checkbox on the SIP
				trunk configuration for Cisco Unified Communications Manager. Desk phone video
				capabilities are not available if you select this checkbox.

#### Desk Phone Video Troubleshooting

Ensure you
				enable the desk phone device for video in Cisco Unified Communications Manager.

Reset the
				physical desk phone.

Exit the
				client.

Run
				services.msc on the computer where you installed the client.

Restart Cisco
				Media Services Interface.

Restart the
				client.

### Enable Video Rate
	 Adaptation

The client uses
		  video rate adaptation to negotiate optimum video quality. Video rate adaptation
		  dynamically increases or decreases video quality based on network conditions.

RTCP is enabled
				on software phone devices by default. However, you must enable RTCP on desk
				phone devices.

#### Enable RTCP on Common Phone Profiles

You can enable RTCP on a common phone profile to enable video rate adaptation on all devices that use the profile.

RTCP is an integral component of Jabber Telephony services. Jabber will continue to send RTCP packets even when disabled.

The Find and List Common Phone Profiles window opens.

The Common Phone Profile Configuration window opens.

#### Enable RTCP on Device Configurations

You can enable RTCP on specific device configurations instead of a common phone profile. The specific device configuration overrides any settings you specify on the common phone profile.

The Find and List Phones window opens.

The Phone Configuration window opens.

### Configure User
	 Associations

When you associate a
		  user with a device, you provision that device to the user.

Create and
		  configure Cisco Jabber devices.

The Find
				  and List Users window opens.

The End
				  User Configuration window opens.

The User
				  Device Association window opens.

The End
				  User Configuration window opens.

The Find
				  and List Access Control Groups dialog box opens.

Standard CCM End
						Users

Standard CTI
						Enabled

If you are
					 provisioning users with secure phone capabilities, do not assign the users to
					 the Standard CTI Secure Connection group.

Cisco
					 Unified IP Phone 9900, 8900, or 8800 series or DX series, select Standard CTI Allow Control of Phones supporting Connected Xfer
						and conf .

Cisco
					 Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover
						Mode .

The Find
				  and List Access Control Groups window closes.

### Reset Devices

After you create and associate users with devices, you should reset those devices.

The Find and List Phones window opens.

The Phone Configuration window opens.

The Directory Number Configuration window opens.

The Device Reset dialog box opens.

### Create a CCMCIP
	 Profile

The client gets
		  device lists for users from the CCMCIP server.

If the client
				gets the _cisco-uds SRV record from a DNS query, it can
				automatically locate the user's home cluster and discover services. One of the
				services the client discovers is UDS, which replaces CCMCIP.

Reset Devices

- Specify a
				  name for the profile in the Name field.

- Specify
				  the fully qualified domain name or IP address of your primary CCMCIP service in
				  the Primary CCMCIP Host field.

- Specify
				  the fully qualified domain name or IP address of your backup CCMCIP service in
				  the Backup CCMCIP Host field.

- Leave the
				  default value for Server Certificate Verification .

Cisco Unified Communications Manager release 9.x and earlier—If
				you enable Cisco Extension Mobility, the Cisco Extension Mobility service must be activated
				on the Cisco Unified Communications Manager nodes that are used for CCMCIP. For
				information about Cisco Extension Mobility, see the Feature and Services guide for your Cisco Unified
				Communications Manager release.

- Select Add Users to Profile .

- In the Find and List Users dialog, specify the appropriate
				  filters in the Find User where field and then select Find to retrieve a list of users.

- Select the
				  appropriate users from the list.

The
					 selected users are added to the CCMCIP profile.

### Dial Plan
	 Mapping

#### Publish Dial
		Rules

Cisco Unified Communications Manager
		  release 8.6.1 or earlier does not automatically publish dial rules to the
		  client. For this reason, you must deploy a COP file to publish your dial rules.
		  This COP file copies your dial rules from the 
		  Cisco Unified Communications Manager
		  database to an XML file on your TFTP server. The client can then download that
		  XML file and access your dial rules.

You must
				deploy the COP file every time you update or modify dial rules on 
				Cisco Unified Communications Manager
				release 8.6.1 or earlier.

Create your
				dial rules in 
				Cisco Unified Communications Manager.

Download the
				Cisco Jabber administration package from 
				cisco.com.

Copy cmterm-cupc-dialrule-wizard-0.1.cop.sgn from the 
				Cisco Jabber
				administration package to your file system.

- Navigate
				  to http:// tftp_server_address :6970/CUPC/AppDialRules.xml .

- Navigate
				  to http:// tftp_server_address :6970/CUPC/DirLookupDialRules.xml .

If you can
				access AppDialRules.xml and DirLookupDialRules.xml with your browser, the client
				can download your dial rules.

After you repeat
		  the preceding steps on each 
		  Cisco Unified Communications Manager
		  instance, restart the client.

## Configure Voice and Video Communication for Cloud-Based Deployments

### Configure Audio and Video Services

Getting started with Cisco Unified Communications Manager for Click to Call

Creating Unified Communications Clusters

Add Teleconferencing Service Name Accounts

### Add Teleconferencing Service Name Accounts

Users can make teleconference calls with either the default Cisco WebEx audio service or a third-party teleconference provider.

To integrate the third-party teleconference provider audio services with Cisco WebEx, you must add teleconferencing service name accounts. After you add those accounts, users can make teleconference calls with the third-party provider audio services.

For more information about adding teleconferencing service name accounts, see the Cisco WebEx Site Administration User's Guide .

Configure Audio and Video Services

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Install Cisco Options Package File for Devices . | Complete this
				task to make Cisco Jabber available as a device in Cisco Unified Communications
				Manager. This is
				applicable for Cisco Unified Communications Manager release 9.x and later only. |
| Step 2 | Apply COP File for BFCP Capabilities . | Complete this
				task if you have Cisco Unified Communications Manager Release 8.6 and you plan
				to enable video desktop sharing. |
| Step 3 | Create SIP Profiles . | Complete this
				task if you have Cisco Unified Communications Manager release 9 or earlier and
				plan to configure devices for mobile clients. |
| Step 4 | Configure the Phone Security Profile | Complete this
				task to setup secure phone capabilities for all devices. |
| Step 5 | Enable User Mobility . | Complete this
				task if you plan to assign Cisco Jabber for Mac or Cisco Jabber for Windows
				users to CTI remote devices. |
| Step 6 | Add a CTI Service . | Complete this
				task if you plan to assign Cisco Jabber for Mac or Cisco Jabber for Windows
				users to CTI remote devices. |
| Step 7 | Add a CTI Gateway Server . | Complete this
				only if you have Cisco Unified Communications Manager Release 8.6 with Cisco
				Unified Presence. |
| Step 8 | Video Desktop Sharing |  |
| Step 9 | Create and Configure Cisco Jabber Devices | Create at
				least one device for every user that will access Cisco Jabber. |
| Step 10 | Provide Users with Authentication Strings |  |
| Step 11 | Desk Phone Video Configuration |  |
| Step 12 | Enable Video Rate Adaptation |  |
| Step 13 | Configure User Associations |  |
| Step 14 | Reset Devices | Only if
				installing Cisco Jabber for Mac |
| Step 15 | Create a CCMCIP Profile |  |

| Step 1 | Download the
			 device COP file. Locate the
				  device COP file. Go to
						  the software downloads
							 site . Locate
						  the device COP file for your release. Click Download Now . Note the
				  MD5 checksum. You will
					 need this information later. Click Proceed with Download and follow the instructions. |
|---|---|
| Step 2 | Place the COP
			 file on an FTP or SFTP server that is accessible from your 
			 Cisco Unified Communications Manager
			 nodes. |
| Step 3 | Install this
			 COP file on the Publisher node in your 
			 Cisco Unified Communications Manager
			 cluster: Open the Cisco Unified OS Administration interface. Select Software
						Upgrades > Install/Upgrade . Specify
				  the location of the COP file and provide the required information. For more
					 information, see the online help. Select Next . Select the
				  device COP file. Select Next . Follow the
				  instructions on the screen. Select Next . Wait for
					 the process to complete. This process can take some time. Reboot 
				  Cisco Unified Communications Manager
				  at a time of low usage. Let the
				  system fully return to service. Note To avoid
						interruptions in service, make sure each node returns to active service before
						you perform this procedure on another server. | Note | To avoid
						interruptions in service, make sure each node returns to active service before
						you perform this procedure on another server. |
| Note | To avoid
						interruptions in service, make sure each node returns to active service before
						you perform this procedure on another server. |
| Step 4 | Install the COP file on each Subscriber node in the cluster. Use the same process you used for the Publisher, including rebooting the node. |

| Note | To avoid
						interruptions in service, make sure each node returns to active service before
						you perform this procedure on another server. |
|---|---|

| Note | You must
					 install the COP file each time you upgrade. For example, if you configure video
					 desktop sharing on 
					 Cisco
				Unified Communication Manager Release 8.6.2 .20000-1 and then upgrade to 
					 Cisco
				Unified Communication Manager Release 8.6.2 .20000-2, you must apply the
					 COP file on 
					 Cisco
				Unified Communication Manager Release 8.6.2 .20000-2. If you
					 configure video desktop sharing on 
					 Cisco
				Unified Communication Manager Release 8.6.1 and then upgrade to 
					 Cisco
				Unified Communication Manager release 8.6.2, you must apply the COP file
					 on 
					 Cisco
				Unified Communication Manager release 8.6.2 before you can configure video
					 desktop sharing. |
|---|---|

| Step 1 | Download the Cisco Jabber administration package from Cisco.com. |
|---|---|
| Step 2 | Copy cmterm-bfcp-e.8-6-2.cop.sgn from the Cisco Jabber administration package to your file system. |
| Step 3 | Open the Cisco
				Unified Communications Manager Administration interface. |
| Step 4 | Upload and
			 apply cmterm-bfcp-e.8-6-2.cop.sgn . |
| Step 5 | Restart the
			 server as follows: Open the Cisco Unified OS Administration interface. Select Settings > Version . Select Restart . Repeat the
				  preceding steps for each node in the cluster, starting with your presentation
				  server. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Device Settings > SIP Profile . The Find and List SIP Profiles window opens. |
| Step 3 | Do one of the following to create a new SIP profile: Find the default SIP profile and create a copy that you can edit. Select Add New and create a new SIP profile. |
| Step 4 | In the new SIP profile, set the following values: Timer Register Delta to 120 Timer Register Expires to 720 Timer Keep Alive Expires to 720 Timer Subscribe Expires to 21600 Timer Subscribe Delta to 15 |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Service
				  Parameters . |
| Step 3 | Select the
			 node. |
| Step 4 | Select the Cisco
				CallManager (Active) service. |
| Step 5 | Scroll to the Clusterwide Parameters (System - Mobility) section. |
| Step 6 | Increase the SIP
				Dual Mode Alert Timer value to 10000 milliseconds. |
| Step 7 | Select Save . Note If, after
				  you increase the SIP Dual Mode Alert Timer value, incoming calls that arrive in
				  Cisco Jabber are still terminated and diverted using Mobile Connect, you can
				  increase the SIP Dual Mode Alert Timer value again in increments of 500
				  milliseconds. | Note | If, after
				  you increase the SIP Dual Mode Alert Timer value, incoming calls that arrive in
				  Cisco Jabber are still terminated and diverted using Mobile Connect, you can
				  increase the SIP Dual Mode Alert Timer value again in increments of 500
				  milliseconds. |
| Note | If, after
				  you increase the SIP Dual Mode Alert Timer value, incoming calls that arrive in
				  Cisco Jabber are still terminated and diverted using Mobile Connect, you can
				  increase the SIP Dual Mode Alert Timer value again in increments of 500
				  milliseconds. |

| Note | If, after
				  you increase the SIP Dual Mode Alert Timer value, incoming calls that arrive in
				  Cisco Jabber are still terminated and diverted using Mobile Connect, you can
				  increase the SIP Dual Mode Alert Timer value again in increments of 500
				  milliseconds. |
|---|---|

| Step 1 | In Cisco
				Unified Communications Manager , select System > Security > Phone Security
				  Profile . |
|---|---|
| Step 2 | Select Add
				New . |
| Step 3 | From the Phone
				Type drop-down list, select the option that is applicable to the
			 device type you are configuring and then select Next . Cisco Unified Client
				  Services Framework —Select this option to create a CSF device for
				Cisco Jabber for Mac or Cisco Jabber for Windows. Cisco Dual Mode for
				  iPhone —Select this option to create a TFT device for an iPhone. Cisco Jabber for
				  Tablet —Select this option to create a TAB device for an iPad or
				an Android tablet. Cisco Dual Mode for
				  Android —Select this option to create a BOT device for an Android
				device. CTI Remote
				  Device —Select this option to create a CTI remote device. CTI remote
				  devices are virtual devices that monitor and have call control over a user's
				  remote destination. |
| Step 4 | In the Name field of the Phone
				Security Profile Configuration window, specify a name for the phone
			 security profile. |
| Step 5 | For Device
				Security Mode , select one of the following options: Authenticated —The SIP connection is over TLS using NULL-SHA encryption. Encrypted —The
				SIP connection is over TLS using AES 128/SHA encryption. The client uses Secure
				Real-time Transport Protocol (SRTP) to offer encrypted media streams. |
| Step 6 | For Transport Type , leave the default value of TLS . |
| Step 7 | Select the TFTP
				Encrypted Config check box to encrypt the device configuration file
			 that resides on the TFTP server. Note For a
				  TCT/BOT/Tablet device, do not select the TFTP Encrypted Config check box here. For
				  Authentication Mode, select By Authentication String or Null String. | Note | For a
				  TCT/BOT/Tablet device, do not select the TFTP Encrypted Config check box here. For
				  Authentication Mode, select By Authentication String or Null String. |
| Note | For a
				  TCT/BOT/Tablet device, do not select the TFTP Encrypted Config check box here. For
				  Authentication Mode, select By Authentication String or Null String. |
| Step 8 | For Authentication Mode , select By
				Authentication String or By
				Null String . Note Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail. | Note | Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail. |
| Note | Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail. |
| Step 9 | For Key
				Size (Bits) , select the appropriate key size for the certificate.
			 Key size refers to the bit length of the public and private keys that the
			 client generates during the CAPF enrollment process. The Cisco
				Jabber clients were tested using authentication strings with 1024-bit length
				keys. The Cisco Jabber clients require more time to generate 2048-bit length
				keys than 1024-bit length keys. As a result, if you select 2048, expect it to take longer to complete the CAPF enrollment process. |
| Step 10 | For SIP
				Phone Port , leave the default value. The port that
				you specify in this field takes effect only if you select Non
				  Secure as the value for Device Security Mode . |
| Step 11 | Click Save . |

| Note | For a
				  TCT/BOT/Tablet device, do not select the TFTP Encrypted Config check box here. For
				  Authentication Mode, select By Authentication String or Null String. |
|---|---|

| Note | Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail. |
|---|---|

| Step 1 | Select User
				  Management > End User . The Find
				  and List Users window opens. |
|---|---|
| Step 2 | Specify the
			 appropriate filters in the Find
				User where field to and then select Find to retrieve a list of users. |
| Step 3 | Select the
			 user from the list. The End
				  User Configuration window opens. |
| Step 4 | Locate the Mobility Information section. |
| Step 5 | Select Enable
				Mobility . |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > UC Service . The Find and List UC Services window opens. |
| Step 3 | Select Add New . The UC Service Configuration window opens. |
| Step 4 | In the Add a UC Service section, select CTI from the UC Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Provide details for the instant messaging and presence service as follows: Specify a name for the service in  the Name field. The name you specify displays when you add services to profiles. Ensure the name you specify is unique, meaningful, and easy to identify. Specify the CTI service address in the Host Name/IP Address field. Specify the port number for the CTI service in the Port field. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. Service Profile Configuration window opens. |
| Step 4 | Navigate to CTI Profile section, and select up to three services from the following drop-down lists: Primary Secondary Tertiary |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco Unified Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Cisco Jabber > CTI Gateway Server . Note In some versions of Cisco Unified Presence , this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Server . The Find and List CTI Gateway Servers window opens. | Note | In some versions of Cisco Unified Presence , this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Server . |
| Note | In some versions of Cisco Unified Presence , this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Server . |
| Step 3 | Select Add New . The CTI Gateway Server Configuration window opens. |
| Step 4 | Specify the required details on the CTI Gateway Server Configuration window. |
| Step 5 | Select Save . |

| Note | In some versions of Cisco Unified Presence , this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Server . |
|---|---|

| Step 1 | Open the Cisco Unified Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Cisco Jabber > CTI Gateway Profile . Note In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Profile . | Note | In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Profile . |
| Note | In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Profile . |
| Step 3 | In the CTI Gateway Profile Configuration window, specify the required details. |
| Step 4 | Select Add Users to Profile and add the appropriate users to the profile. |
| Step 5 | Select Save . |

| Note | In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > CTI Gateway Profile . |
|---|---|

| Note | Cisco
				Jabber for mobile clients can only receive BFCP. |
|---|---|

| Note | You can
					 enable video desktop sharing only on software phone devices. You cannot enable
					 video desktop sharing on desk phone devices. Users must
					 be on active calls to use video desktop sharing capabilities. You can only
					 initiate video desktop sharing sessions from active calls. In hybrid
					 cloud-based deployments, both Cisco WebEx and Cisco Unified Communications
					 Manager provide desktop sharing functionality. If
						  users initiate desktop sharing sessions during an instant messaging session,
						  Cisco WebEx provides desktop sharing capabilities. If
						  users initiate desktop sharing sessions during an audio or video conversation,
						  Cisco Unified Communications Manager provides desktop sharing capabilities. Video desktop sharing using
		  BFCP is not supported if Trusted
			 Relay Point or Media
			 Termination Point are enabled on the software phone device. Video desktop sharing using BFCP is not supported during Cisco Jabber multi-party conference calls unless Cisco TelePresence MCU is deployed. |
|---|---|

| Tip | You must
				enable BFCP on the SIP trunk to allow video desktop sharing capabilities
				outside of a Cisco Unified Communications Manager cluster. To enable BFCP on
				the SIP trunk, do the following: Select Allow Presentation Sharing using BFCP in the Trunk
					 Specific Configuration section of the SIP profile. Select the
					 SIP profile from the SIP Profile drop-down list on the CSF device
					 configuration. |
|---|---|

| Note | Users can only
			 remove participants from a conference call when using the softphone(CSF) device
			 for calls. |
|---|---|

| Step 1 | Log in to the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . Find and List Phones window opens. |
| Step 3 | Select Add
				New . |
| Step 4 | From the Phone Type drop-down list, select the option that is applicable to the device type you are configuring and then select Next . For Jabber users, you can only create one type of device per user although you can create multiple devices for each user. For example, you can create one tablet device and one CSF device but not two CSF devices. Cisco Unified Client Services Framework —Select this option to create a CSF device for Cisco Jabber for Mac or Cisco Jabber for Windows. Cisco Dual Mode for iPhone —Select this option to create a TCT device for an iPhone. Cisco Jabber for Tablet —Select this option to create a TAB device for an iPad or an Android tablet. Cisco Dual Mode for Android —Select this option to create a BOT device for an Android device. CTI Remote Device —Select this option to create a CTI remote device. CTI remote devices are virtual devices that monitor and have call control over a user's remote destination. |
| Step 5 | From the Owner
				User ID drop-down list, select the user for whom you want to create
			 the device. For the Cisco Unified Client Services Framework option in a
				Phone mode deployment, ensure that User is selected. |
| Step 6 | In the Device
				Name field, use the applicable format to specify a name for the
			 device: If
							 You Select Required Format CTI Remote
								Device When you select Owner User ID , the device name field populates with CTIRD<owner user ID> . You can change this value.
								  The device name does not have to begin with CTIRD . Valid characters: a–z, A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. Cisco Unified Client
								Services Framework Valid characters: a–z, A–Z, 0–9. 15-character limit. Cisco Dual Mode for
								iPhone The device name must begin with TCT . For example, if you create a TCT device for user, Tanya Adams,
								  whose username is tadams, enter TCTTADAMS . Must be uppercase. Valid characters:  A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. Cisco Jabber for
								Tablet The device name must begin with TAB . For example, if you create a TAB device for user, Tanya Adams,
								  whose username is tadams, enter TABTADAMS . Must be uppercase. Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. Cisco Dual Mode for
								Android The device name must begin with BOT . For example, if you create a BOT device for user, Tanya Adams,
								  whose username is tadams, enter BOTTADAMS . Must be uppercase. Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. | If
							 You Select | Required Format | CTI Remote
								Device | When you select Owner User ID , the device name field populates with CTIRD<owner user ID> . You can change this value.
								  The device name does not have to begin with CTIRD . Valid characters: a–z, A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. | Cisco Unified Client
								Services Framework | Valid characters: a–z, A–Z, 0–9. 15-character limit. | Cisco Dual Mode for
								iPhone | The device name must begin with TCT . For example, if you create a TCT device for user, Tanya Adams,
								  whose username is tadams, enter TCTTADAMS . Must be uppercase. Valid characters:  A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. | Cisco Jabber for
								Tablet | The device name must begin with TAB . For example, if you create a TAB device for user, Tanya Adams,
								  whose username is tadams, enter TABTADAMS . Must be uppercase. Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. | Cisco Dual Mode for
								Android | The device name must begin with BOT . For example, if you create a BOT device for user, Tanya Adams,
								  whose username is tadams, enter BOTTADAMS . Must be uppercase. Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |
| If
							 You Select | Required Format |
| CTI Remote
								Device | When you select Owner User ID , the device name field populates with CTIRD<owner user ID> . You can change this value.
								  The device name does not have to begin with CTIRD . Valid characters: a–z, A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |
| Cisco Unified Client
								Services Framework | Valid characters: a–z, A–Z, 0–9. 15-character limit. |
| Cisco Dual Mode for
								iPhone | The device name must begin with TCT . For example, if you create a TCT device for user, Tanya Adams,
								  whose username is tadams, enter TCTTADAMS . Must be uppercase. Valid characters:  A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |
| Cisco Jabber for
								Tablet | The device name must begin with TAB . For example, if you create a TAB device for user, Tanya Adams,
								  whose username is tadams, enter TABTADAMS . Must be uppercase. Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |
| Cisco Dual Mode for
								Android | The device name must begin with BOT . For example, if you create a BOT device for user, Tanya Adams,
								  whose username is tadams, enter BOTTADAMS . Must be uppercase. Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |
| Step 7 | If you are
			 creating a CTI Remote Device, in the Protocol Specific Information section, select an
			 appropriate option from the Rerouting Calling Search Space drop-down list. The Rerouting
				Calling Search Space defines the calling search space for rerouting and ensures
				that users can send and receive calls from the CTI remote device. |
| Step 8 | To generate an
			 authentication string that you can provide to end users to access their devices
			 and securely register to Cisco Unified Communications Manager, navigate to the Certification Authority Proxy Function (CAPF)
				Information section. |
| Step 9 | From the Certificate Operation drop-down list, select Install/Upgrade . |
| Step 10 | From the Authentication Mode drop-down list, select By
				Authentication String or By
				Null String . Note Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail. | Note | Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail. |
| Note | Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail. |
| Step 11 | Click Generate String . The
			 Authentication String autopopulates with a string value. This is the string
			 that you will provide to end users. |
| Step 12 | From the Key
				Size (Bits) drop-down list, select the same key size that you set
			 in the phone security profile. |
| Step 13 | In the Operation Completes By fields, specify an expiration value for the authentication string or leave as default. |
| Step 14 | If you are using a group configuration file, specify it in the Cisco Support Field of the Desktop Client Settings. Cisco Jabber does not use any other settings that are available on the Desktop Client Settings . |
| Step 15 | Select Save . |
| Step 16 | Click Apply Config . |

| If
							 You Select | Required Format |
|---|---|
| CTI Remote
								Device | When you select Owner User ID , the device name field populates with CTIRD<owner user ID> . You can change this value.
								  The device name does not have to begin with CTIRD . Valid characters: a–z, A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |
| Cisco Unified Client
								Services Framework | Valid characters: a–z, A–Z, 0–9. 15-character limit. |
| Cisco Dual Mode for
								iPhone | The device name must begin with TCT . For example, if you create a TCT device for user, Tanya Adams,
								  whose username is tadams, enter TCTTADAMS . Must be uppercase. Valid characters:  A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |
| Cisco Jabber for
								Tablet | The device name must begin with TAB . For example, if you create a TAB device for user, Tanya Adams,
								  whose username is tadams, enter TABTADAMS . Must be uppercase. Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |
| Cisco Dual Mode for
								Android | The device name must begin with BOT . For example, if you create a BOT device for user, Tanya Adams,
								  whose username is tadams, enter BOTTADAMS . Must be uppercase. Valid characters: A–Z, 0–9, period (.), underscore (_),
								  hyphen (-). 15-character limit. |

| Note | Using the CAPF Authentication mode By Null String with VXME and Jabber for Windows CSF devices is not supported. It causes Jabber registration with Cisco Unified Communications Manager (CUCM) to fail. |
|---|---|

| Step 1 | Locate the Association Information section on the Phone
				Configuration window. |
|---|---|
| Step 2 | Click Add a
				new DN . |
| Step 3 | In the Directory Number field, specify a
			 directory number. |
| Step 4 | In the Users Associated with Line section, click Associate End Users . |
| Step 5 | In the Find
					 User where field, specify the appropriate filters and then click Find . |
| Step 6 | From the list that appears, select the applicable users and click Add
					 Selected . |
| Step 7 | Specify all
			 other required configuration settings as appropriate. |
| Step 8 | Select Apply
				Config . |
| Step 9 | Select Save . |

| Note | You should create only one remote destination per user. Do not add two or more remote destinations for a user. Cisco Unified Communications Manager does not verify if it can route remote destinations that you add through the Cisco Unified CM Administration interface. For this reason, you must ensure that Cisco Unified Communications Manager can route the remote destinations you add. Cisco Unified Communications Manager automatically applies application dial rules to all remote destination numbers for CTI remote devices. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Specify the appropriate filters in the Find Phone where field to and then select Find to retrieve a list of phones. |
| Step 4 | Select the CTI remote device from the list. The Phone Configuration window opens. |
| Step 5 | Locate the Associated Remote Destinations section. |
| Step 6 | Select Add a New Remote Destination . The Remote Destination Information window opens. |
| Step 7 | Specify JabberRD in the Name field. Restriction: You must specify JabberRD in the Name field. The client uses only the JabberRD remote destination. If you specify a name other than JabberRD, users cannot access that remote destination. The client automatically sets the JabberRD name when users add remote destinations through the client interface. |
| Step 8 | Enter the destination number in the Destination Number field. |
| Step 9 | Specify all other values as appropriate. |
| Step 10 | Select Save . |

| Note | The Device Information section on the Phone Configuration window contains a Active Remote Destination field. When users select a remote destination in the client, it displays as the value of Active Remote Destination . none displays as the value of Active Remote Destination if: Users do not select a remote destination in the client. Users exit or are not signed in to  the client. |
|---|---|

| Note | The time it takes for the enrollment process to complete can vary depending on the user's computer or mobile device and the current load for Cisco Unified Communications Manager. It can take up to one minute for the client to complete the CAPF enrollment process. |
|---|---|

| Tip | If users
					 have both wireless and wired connections available, they should configure
					 Microsoft Windows so that wireless connections do not take priority over wired
					 connections. See the following Microsoft documentation for more information: An
						explanation of the Automatic Metric feature for Internet Protocol
						routes . |
|---|---|

| Note | Download the Cisco Media Services Interface installation program
				  from the download site on cisco.com . |
|---|---|

| Note | RTCP is enabled
				on software phone devices by default. However, you must enable RTCP on desk
				phone devices. |
|---|---|

| Note | RTCP is an integral component of Jabber Telephony services. Jabber will continue to send RTCP packets even when disabled. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Device Settings > Common Phone Profile . The Find and List Common Phone Profiles window opens. |
| Step 3 | Specify the appropriate filters in the Find Common Phone Profile where field and then select Find to retrieve a list of profiles. |
| Step 4 | Select the appropriate profile from the list. The Common Phone Profile Configuration window opens. |
| Step 5 | Locate the Product Specific Configuration Layout section. |
| Step 6 | Select Enabled from the RTCP drop-down list. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of phones. |
| Step 4 | Select the appropriate phone from the list. The Phone Configuration window opens. |
| Step 5 | Locate the Product Specific Configuration Layout section. |
| Step 6 | Select Enabled from the RTCP drop-down list. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > End User . The Find
				  and List Users window opens. |
| Step 3 | Specify the
			 appropriate filters in the Find
				User where field and then select Find to retrieve a list of users. |
| Step 4 | Select the
			 appropriate user from the list. The End
				  User Configuration window opens. |
| Step 5 | Locate the Service
				Settings section. |
| Step 6 | Select Home Cluster . |
| Step 7 | Select the
			 appropriate service profile for the user from the UC
				Service Profile drop-down list. |
| Step 8 | Locate the Device
				Information section. |
| Step 9 | Select Device
				Association . The User
				  Device Association window opens. |
| Step 10 | Select the devices to which you want to associate the user. Jabber only supports a single softphone association per device type. For example, only one TCT, BOT, CSF, and TAB device can be associated with a user. |
| Step 11 | Select Save
				Selected/Changes . |
| Step 12 | Select User
				  Management > End User and return to the Find and
				List Users window. |
| Step 13 | Find and select
			 the same user from the list. The End
				  User Configuration window opens. |
| Step 14 | Locate the Permissions Information section. |
| Step 15 | Select Add to
				Access Control Group . The Find
				  and List Access Control Groups dialog box opens. |
| Step 16 | Select the
			 access control groups to which you want to assign the user. At a minimum you
				should assign the user to the following access control groups: Standard CCM End
						Users Standard CTI
						Enabled Remember: If you are
					 provisioning users with secure phone capabilities, do not assign the users to
					 the Standard CTI Secure Connection group. Certain phone
				models require additional control groups, as follows: Cisco
					 Unified IP Phone 9900, 8900, or 8800 series or DX series, select Standard CTI Allow Control of Phones supporting Connected Xfer
						and conf . Cisco
					 Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover
						Mode . |
| Step 17 | Select Add
				Selected . The Find
				  and List Access Control Groups window closes. |
| Step 18 | Select Save on the End User
				Configuration window. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices. |
| Step 4 | Select the appropriate device from the list. The Phone Configuration window opens. |
| Step 5 | Locate the Association Information section. |
| Step 6 | Select the appropriate directory number configuration. The Directory Number Configuration window opens. |
| Step 7 | Select Reset . The Device Reset dialog box opens. |
| Step 8 | Select Reset . |
| Step 9 | Select Close to close the Device Reset dialog box. |

| Note | If the client
				gets the _cisco-uds SRV record from a DNS query, it can
				automatically locate the user's home cluster and discover services. One of the
				services the client discovers is UDS, which replaces CCMCIP. |
|---|---|

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Legacy
				  Clients > CCMCIP Profile . |
| Step 3 | In the Find
				and List CCMCIP Profiles window, select Add
				New . |
| Step 4 | In the CCMCIP Profile Configuration window, specify service
			 details in the CCMCIP profile as follows: Specify a
				  name for the profile in the Name field. Specify
				  the fully qualified domain name or IP address of your primary CCMCIP service in
				  the Primary CCMCIP Host field. Specify
				  the fully qualified domain name or IP address of your backup CCMCIP service in
				  the Backup CCMCIP Host field. Leave the
				  default value for Server Certificate Verification . Cisco Unified Communications Manager release 9.x and earlier—If
				you enable Cisco Extension Mobility, the Cisco Extension Mobility service must be activated
				on the Cisco Unified Communications Manager nodes that are used for CCMCIP. For
				information about Cisco Extension Mobility, see the Feature and Services guide for your Cisco Unified
				Communications Manager release. |
| Step 5 | Add users to
			 the CCMCIP profile as follows: Select Add Users to Profile . In the Find and List Users dialog, specify the appropriate
				  filters in the Find User where field and then select Find to retrieve a list of users. Select the
				  appropriate users from the list. Select Add Selected . The
					 selected users are added to the CCMCIP profile. |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco
				Unified OS Administration interface. |
|---|---|
| Step 2 | Select Software
				  Upgrades > Install/Upgrade . |
| Step 3 | Specify the
			 location of cmterm-cupc-dialrule-wizard-0.1.cop.sgn in the Software Installation/Upgrade window. |
| Step 4 | Select Next . |
| Step 5 | Select cmterm-cupc-dialrule-wizard-0.1.cop.sgn from the Available Software list. |
| Step 6 | Select Next and then select Install . |
| Step 7 | Restart the
			 TFTP service. |
| Step 8 | Open the dial
			 rules XML files in a browser to verify that they are available on your TFTP
			 server. Navigate
				  to http:// tftp_server_address :6970/CUPC/AppDialRules.xml . Navigate
				  to http:// tftp_server_address :6970/CUPC/DirLookupDialRules.xml . If you can
				access AppDialRules.xml and DirLookupDialRules.xml with your browser, the client
				can download your dial rules. |
| Step 9 | Repeat the
			 preceding steps for each 
			 Cisco Unified Communications Manager
			 instance that runs a TFTP service. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Audio and Video Services |  |
| Step 2 | Add Teleconferencing Service Name Accounts |  |