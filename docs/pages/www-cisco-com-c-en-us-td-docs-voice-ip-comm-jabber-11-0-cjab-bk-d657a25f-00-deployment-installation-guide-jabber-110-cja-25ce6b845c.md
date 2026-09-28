---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-25ce6b845c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_01110.html
retrieved_at: 2026-08-25T21:46:53.504836+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Cisco Jabber Options

## Chapter: Cisco Jabber Options

# Cisco Jabber Options

## Cisco Jabber 11.0
	 Features

Cisco Jabber
		  includes a broad range of features. As indicated in the following table, some
		  features are client-specific.

Feature

Cisco
						Jabber for Windows

Cisco
						Jabber for Mac

Cisco
						Jabber for Android, Cisco Jabber for iPhone and iPad

Alert
						When Available

X

Automatic Upgrades

X

X

X

Auto-Save Chat

X

Bridge
						Escalations

X

X

X

Call
						Pickup

X

Call
						Park

X

Call
						Preservation

X

X

X

Chat
						Search

X

Chat
						Security Labels

X

Cisco
						WebEx Meetings integration

X

X

X

Custom
						Contact

X

X

Configure Silent Monitoring and Call Recording

X

X

Define a port range on the SIP profile

X

X

X

Dial
						via Office - Reverse

X

Directory Groups in Contact List

X

X

X

Expressway Mobile and Remote Access

X

X

X

Far
						End Camera Control

X

X

X

File
						Transfer

X

X

Some
						of the file transfer features are supported

FIPS
						Compliance

X

Flexible Jabber ID

X

X

X

Flexible DSCP

X

X

Group
						Chat

X

X

X

Hunt
						Group

X

X

Instant Messaging

X

X

X

Instant Messaging Encryption

X

X

X

Jabber
						to Jabber Call

X

X

X

Locations

X

X

Mandatory Upgrade Support

X

X

X

Multiple Resource Login

X

X

X

Persistent Chat Rooms

X

Some
						of the persistent chat room features are supported.

Predictive Contact Search

X

X

X

Presence

X

X

X

Save
						Chat History to Outlook Folder

X

Print
						Chat

X

Send
						to Mobile

X

Service Discovery

X

X

X

Single
						Sign-On

X

X

X

Spell
						Check

X
						(Client Options feature)

X (OS
						feature)

Telemetry

X

X

X

URI
						Dialing

X

X

X

Video
						Desktop Share (BFCP)

X

X

X
						(Mobile clients only support BFCP receiving.)

Voice
						and Video Calling

X

X

X

Voice
						and Video Encryption

X

X

X

Voicemail

X

X

X

## Cisco Jabber
	 Features for Windows, Mac, iOS and Android

### Jabber to Jabber
	 Call

Applies to: All clients

Jabber to Jabber calling is only supported
					 for users who authenticate to the Cisco WebEx Messenger service.

For Cisco Jabber for Windows clients, we recommend running
					 Internet Explorer 10 or greater while using the Jabber to Jabber calling feature. Using the
					 feature with previous versions of Internet Explorer or with Internet Explorer
					 in Compatibility Mode can cause issues. These issues are with Cisco Jabber
					 client login (non-SSO setup) or Jabber to Jabber calling capability (SSO
					 setup).

#### Jabber to Jabber Call Experience

Cisco Jabber for mobile clients does not support HD video in portrait mode. To achieve HD video, you need to rotate the phone from portrait to landscape mode during the call.

If two users start a Jabber to Jabber call to each other at the same
				time, the call is automatically connected. In such case, users do not receive
				any incoming call notification.

When users are on a Jabber to Jabber call and start another call, the ongoing call ends immediately, even if the person they called does not
				answer.

When on a Jabber to Jabber call and they receive an
				incoming Jabber to Jabber call, the End Call And Answer option is displayed. When they select this
				button, the ongoing Jabber to Jabber call ends and the incoming call
				is answered.

Cisco Jabber for mobile clients does not support HD video in portrait mode. To achieve HD video, you need to rotate the phone from portrait to landscape mode during the call.

When users are on a Jabber to Jabber call and they make a phone
					 call, the ongoing Jabber to Jabber call ends immediately, even
					 if the remote party does not answer.

When users are on a mobile call, they cannot answer any Jabber to Jabber call. The incoming Jabber to Jabber call is listed as a missed
					 call.

On an iPhone, the Jabber to Jabber call ends immediately,
						  even if they do not answer the call.

On an Android phone, the Jabber to Jabber call ends immediately
						  when they answer the incoming mobile call.

#### Supported In-Call Features

End a Jabber to Jabber call

Mute or unmute the audio

Start or stop the video

Volume control

Open or close or move the self-video

Switch to front or back camera. This feature is only supported on
				the Cisco Jabber mobile clients.

#### Jabber to Jabber Call Cloud Deployment

Install the following root certificate to use the Jabber to Jabber call feature: GoDaddy Class 2 Certification Authority Root
				  Certificate . To resolve any warnings about this certificate name,
				install the required GoDaddy certificate.

https://locus-a.wbx2.com/locus/api/v1

https://conv-a.wbx2.com/conversation/api/v1

Enable the range of media ports and protocols for RTP/SRTP over
				UDP: 33434-33598 and 8000-8100. For Jabber to Jabber call setup over HTTPS, enable
				port 443.

Contact the
				Cisco Customer Support team or your Cisco Customer Success Manager to request that your organization is added to the Cisco Common
					 Identity server. This process to add users to the Common Identity server takes
					 some time to complete and is necessary to access Jabber to Jabber calling
					 capabilities.

For Single Sign On (SSO) users, you must set up SSO for Common Identity. For more information about configuring SSO, see the Cisco WebEx Messenger documentation at this link: https:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​webex-messenger/​products-installation-guides-list.html .

Using the P2P settings in the Configuration Tab section. For more information, see
				the Cisco WebEx Messenger Administrator's Guide .

Using the Internal VoIP and External VoIP settings in the policy editor for Cisco WebEx
				Messenger Administration tool. You can control the video services for Jabber to
				Jabber calls using the Internal Video and External Video policy actions. For more information, see the Policy Editor section of the Cisco WebEx Messenger
				  Administration Guide. Jabber to Jabber calling can be enabled for
				groups of users or all users.

- Jabber to Jabber
	 Hybrid Mode

#### Jabber to Jabber
	 Hybrid Mode

##### Jabber to
		  Jabber Call Experience in Hybrid Mode

In addition to the
		  limitations for Jabber to Jabber, the following are the scenarios that occur
		  when using Jabber to Jabber calls and Cisco Unified Communications Manager
		  calls:

When users
				are on a Jabber to Jabber call and make a Cisco Unified Communications Manager
				call, the ongoing Jabber to Jabber call ends immediately, even if the remote
				party does not answer.

When users
				are on a Jabber to Jabber call and resume a Cisco Unified Communications
				Manager call from on hold, the Jabber to Jabber call ends immediately.

When users
				are on a Jabber to Jabber call and receive an incoming Cisco Unified
				Communications Manager call, a notification with an End Call And Answer button displays. If your user
				selects this button the ongoing Jabber to Jabber call ends and the incoming
				call is answered.

When users
				receive a Cisco Unified Communications Manager call, they can place the ongoing
				Cisco Unified Communications Manager call on hold to answer the new call.

When users
				are on a Cisco Unified Communications Manager call and they choose to make a
				Jabber to Jabber call, the Cisco Unified Communications Manager call is put on
				hold immediately, even if the participant in the Jabber to Jabber call does not
				answer the call.

When users
				are on a Cisco Unified Communications Manager call and they answer an incoming
				Jabber to Jabber call, the Cisco Unified Communications Manager call is put on
				hold immediately.

If your
				user’s line is configured on Cisco Unified Communications Manager to
				auto-answer calls and they receive an incoming Cisco Unified Communications
				Manager call when they are on a Jabber to Jabber call, the Jabber to Jabber
				call ends immediately without notification and the Cisco Unified Communications
				Manager call is answered.

### Decrypt the
	 Problem Report

--help —Show the
				help message.

--privatekey —Specify the private key file, this is a
				privacy enhanced mail (.pem) or a personal information exchange PKCS#12 (.pfx)
				format.

--password —Optional, if the input private key file is
				password protected.

--encryptionkey —Specify the encryption secret key file,
				for example file.zip.esk .

--encryptedfile —Specify the encrypted file, for example file.zip.enc .

--outputfile —Specify the output file, for example decryptedfile.zip .

--mobile —Specify
				for the problem reports from mobile clients.

file.zip.esk —The
					 encrypted symmetric key.

file.zip.enc —The
					 original data encrypted using AES256.

Private Key
				for the certificate used for encrypting the data.

Example for desktop clients: CiscoJabberPrtDecrypter.exe --privatekey
				  C:\PRT\PrivateKey.pfx --password 12345 --encryptedfile C:\PRT\file.zip.enc
				  --encryptionkey C:\PRT\file.zip.esk --outputfile
				  C:\PRT\decryptedfile.zip

Example for mobile clients: CiscoJabberPrtDecrypter.exe --privatekey
				  C:\PRT\PrivateKey.pfx --password 12345 --encryptedfile C:\PRT\file.zip.enc
				  --encryptionkey C:\PRT\file.zip.esk --outputfile C:\PRT\decryptedfile.zip
				  --mobile

If the
				decryption is successful the output file is created. If there is an invalid
				parameter the decryption fails and an error is shown on the command line.

### Define a Port
	 Range on the SIP Profile

You can configure
		  separate UDP port ranges for the audio stream and video stream for SIP calls.
		  Since video typically requires considerably more bandwidth than audio, you can
		  use dedicated port ranges for each media type to simplify network bandwidth
		  management. It also helps against audio stream degradation by ensuring that the
		  audio stream have a dedicated channel separated from the higher-bandwidth video
		  stream.

### Telemetry

#### Cisco Jabber
		  Analytics

Applies to: All clients

To improve your
		  experience and product performance, Cisco Jabber may collect and send non-personally
		  identifiable usage and performance data to Cisco. The aggregated data is used
		  by Cisco to understand trends in how Jabber clients are being used and how they
		  are performing.

You must install
		  the following root certificate to use the telemetry feature: GoDaddy
			 Class 2 Certification Authority Root Certificate . The telemetry
		  server certificate name is "metrics-a.wbx2.com". To resolve any warnings about
		  this certificate name, install the required GoDaddy certificate. 
		For more
		  information about certificates, see the Planning Guide.

Telemetry_Enabled —Specifies whether analytics data
				is gathered. The default value is true.

TelemetryEnabledOverCellularData —Specifies whether
				analytics data is sent over cellular data and Wi-Fi (true), or Wi-Fi only
				(false). The default value is true.

TelemetryCustomerID —This optional parameter
				specifies the source of analytic information. This ID can be a string that
				explicitly identifies an individual customer, or a string that identifies a
				common source without identifying the customer. We recommend using a tool that
				generates a Global
				  Unique Identifier (GUID) to create a 36 character unique identifier, or
				to use a reverse domain name.

For more
		  information about these parameters, see the Parameters Reference Guide .

Full details on what analytics data Cisco Jabber does and does not collect can be found in the Cisco Jabber Supplement to Cisco’s On-Line Privacy Policy at https:/​/​www.cisco.com/​web/​siteassets/​legal/​privacy_​02Jun10.html .

### Enterprise Groups
	 for Cisco Unified Communications Manager IM and Presence Service

Applies to: All clients

Users can add groups to their contact lists in Cisco Jabber. The groups are created in the enterprise's Microsoft Active Directory and then are imported into Cisco Unified Communications Manager IM and Presence Service. When enterprise groups are set up and enabled on Cisco Unified Communications Manager IM and Presence Service, Cisco Jabber users can add enterprise groups to their contact list from the client.

Using enterprise
		  groups is supported when on the Expressway for Mobile and Remote Access.

#### Prerequisites
		  for Enabling Enterprise Groups in Cisco Jabber

Cisco Unified Communications Manager Release 11.0(1) or later

Cisco Unified Communications Manager IM and Presence Service Release 11.0 or later

Before you can set up enabling adding enterprise groups to contact lists for your users, you must configure the feature on the server, see Enable Enterprise Groups section. For more information about enterprise groups, see the Feature Configuration Guide for Cisco Unified Communications Manager, Release 11.0(1) .

#### Limitations

Enterprise Groups for Cisco Unified Communications Manager IM and Presence Service is available to on-premises deployments only. Enterprise Groups are already supported on cloud deployments.

Security Group is supported from Cisco Unified Communications Manager IM and Presence Service 11.5 or later.

Presence is unsupported for contacts in enterprise groups of over 100 people who are IM-enabled, unless the user has other presence subscriptions for a contact. For example, if users have someone added to their personal contact list who is also listed in an enterprise group of over 100 people, then presence is still displayed for that person. Users who are not IM-enabled do not affect the 100 person presence limit.

Nested groups cannot be imported as part of an enterprise group. For example, in an AD group, only group members are imported, not any embedded groups within it.

If your users and AD Group are in different organizational units (OUs), then before you add the contacts to the AD Group, you must sync both OUs with Cisco Unified Communications Manager, and not just the OU that the AD Group is in.

If you have the minimum character query set to the default value of 3 characters, then user searches for enterprise groups will exclude any two letter group names (for example: HR). To change the minimum character query for EDI, BDI, or UDS connections, change the value of the MinimumCharacterQuery parameter.

Enterprise groups with special characters cannot be located during searches if the special characters are among the first 3 characters (or whatever value you have defined as the minimum character query) of the name.

We recommend that you only change the distinguished name of enterprise groups outside of core business hours, as it would cause unreliable behavior from the Cisco Jabber client for users.

If you make changes to enterprise groups, you must synch the Active Directory with Cisco Unified Communications Manager afterwards in order for the changes to be applied.

When a directory group is added to Cisco Jabber, the profile photos are not displayed immediately because of the sudden load that the contact resolution places on the directory server. However, if you right-click on each group member to view their profile, the contact resolution is resolved and the photo is downloaded.

Intercluster peering with a 10.x cluster: If the synced group includes group members from a 10.x intercluster peer, users on the higher cluster cannot view the presence of synced members from the 10.x cluster. This is due to database updates that were introduced in Cisco Unified Communications Manager Release 11.0(1) for the Enterprise Groups sync. These updates are not a part of the Cisco Unified Communications Manager Releases 10.x. To guarantee that users homed on higher cluster can view the presence of group members homed on the 10.x cluster, users on the higher cluster should manually add the 10.x users to their contact lists. There are no presence issues for manually added user.

#### UDS Limitations (Applies to Users on the Expressway for Mobile and Remote Access or with UDS on-premises)

There is no search
		  capability for enterprise groups when connecting using UDS, so users must know
		  the exact enterprise group name that they want to add to their contact lists.
		  There is a search capability for enterprise groups when connecting using EDI or
		  BDI.

Enterprise group
		  names are case-sensitive.

If two enterprise groups within an AD Forest have the same name, then users get an error when trying to add the group. This issue does not apply to clients using EDI or BDI.

- Enable Enterprise
	 Groups

#### Enable Enterprise
	 Groups

The enterprise
		  parameter Directory Group Operations on Cisco IM and Presence in the Enterprise Parameter Configuration window allows you
		  to enable or disable the Enterprise Groups feature. Follow these steps to
		  enable the Enterprise Groups feature.

The Cisco DirSync
		  feature service must be running.

- None —If you
				choose this option, the Cisco Intercluster Sync Agent service does not
				synchronize the enterprise groups and the group membership records between IM
				and Presence Service clusters.

- Differential
				  Sync —This is the default option. If you choose this option, after
				all the enterprise groups and group membership records from remote IM and
				Presence Service cluster are synchronized, the subsequent syncs synchronize
				only the records that were updated since the last sync occurred.

- Full Sync —If
				you choose this option, after all the enterprise groups and group membership
				records from the remote IM and Presence Service cluster are synchronized, all
				the records are synchronized during each subsequent sync.

If the Cisco
				  Intercluster Sync Agent service is not running for more than 24 hours, we
				  recommend that you select the Full Sync option to ensure that the enterprise
				  groups and group membership records synchronize completely. After all the
				  records are synchronized, that is, when the Cisco Intercluster Sync Agent has
				  been running for about 30 minutes, choose the Differential Sync option for the subsequent syncs.
				  Keeping the value of this parameter set to 'Full Sync' for a longer period
				  could result in extensive CPU usage and therefore we recommend that you use the Full Sync option during off-business hours.

### Far End Camera
	 Control (FECC)

Applies to: All clients

In calls that
		  support far-end camera control (FECC), you can adjust the far-end camera to
		  give you a better view during video calls. FECC is available to users if the
		  endpoint that they are calling supports it.

You can configure
		  whether users can access FECC-enabled endpoints. Disabling the configuration
		  parameter means that users are not provided with the ability to control far-end
		  camera endpoints, even if the endpoint is capable. From a user experience, with
		  FECC disabled, it works the same as dialing in to an endpoint that is not FECC
		  enabled.

To disable FECC,
		  set the EnableFecc parameter to false . For more information about this parameter, see the Parameters Reference Guide .

#### Limitations

FECC is only
		  supported in point-to-point calls, but not in group calls or conferences where
		  multiple video connections are connecting to the same bridge.

FECC is only
		  supported in Softphone mode.

### Bridge
	 Escalations

Applies to: All clients

Bridge
		  escalations allow users to quickly escalate a group chat to a conference call.
		  Participants are automatically added without the need to merge them into the
		  conference call.

### Collaboration Meeting Rooms

Applies to: All clients

Cisco
		  Collaboration Meeting Rooms (CMR) Cloud provides easy access for users to join
		  or start a Cisco WebEx meeting. Cisco Jabber provides users with the ability to
		  access the meeting either using Cisco WebEx interface or join using video.

There is a
		  limitation on CMR Cloud join experience for attendees of scheduled CMR Cloud
		  meetings. This limitation impacts Mac users and Windows users who have not
		  enabled Outlook calendar integration. Due to a server limitation, attendees for
		  these deployment scenarios will only receive the option to join the meeting
		  using Cisco WebEx. Hosts will enjoy the full experience, as will anyone invited
		  to join ad hoc CMR Cloud meetings.

Users who are in
		  CTI control mode will only be able to join using WebEx.

Cisco
		  Collaboration Meeting Rooms Cloud is available on Cisco WebEx Meeting Center.

### Personal
	 Rooms

Applies to: All clients

A personal room is
		  a virtual conference room that is always available and can be used to meet with
		  people. Cisco Jabber uses the personal room feature of Cisco WebEx Meeting
		  Center to allow users to easily meet with their contacts using the Meet
			 Now option in the client.

### Call
	 Preservation

When a user on a call using Cisco Jabber for iPhone and iPad
				switches from wi-fi to mobile data network or vice-versa, the interface IP
				address is lost and the call is preserved. When the user returns to the initial
				network and the IP address is restored, they can continue with the call.

For detailed
			 information about call preservation, see the relevant release of Manager System  Guide for Cisco Unified Communication Manager at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-maintenance-guides-list.html .

### Prompts
	 for Presence Subscription Requests

Applies to: All clients

You can enable or disable prompts for presence subscription requests from contacts within your organization. The client always prompts users for presence subscription requests from contacts outside your organization.

Users can choose to allow or block contacts from  inside your organization.

you select Allow users to view the availability of other users without being prompted for approval , the client automatically accepts all presence subscription requests without prompting users.

you do not select Allow users to view the availability of other users without being prompted for approval , the client prompts users for all presence subscription requests.

If users choose to block contacts, only their existing contacts can see their availability status. In other words, only those contacts who have already subscribed to the user's presence can see their availability status.

When searching for contacts in your organization, users can see the temporary availability status of all users in the organization. However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list.

Users can choose the following options for contacts from outside your organization:

Have the client prompt them for each presence subscription request.

Block all contacts so that only their existing contacts can see their availability status. In other words, only those contacts who have already subscribed to the user's presence can see their availability status.

This feature is
		  supported for on-premises deployments and is only available on Cisco Unified Communications Manager, release 8.x or later.

The Presence Settings window opens.

Selected—The client does not prompt users for presence subscription requests. The client automatically accepts all presence subscription requests without prompting the users.

Cleared—The client prompts users to allow presence subscription requests. This setting requires users to allow other users in your organization to view their availability status.

### Temporary
	 Presence

Applies to: All clients

Disable temporary
		  presence to increase privacy control. When you configure this parameter, 
		  Cisco Jabber displays availability status only to
		  contacts in a user's contact list.

This feature is
		  supported for on-premises deployment and requires 
		  Cisco Unified Communications Manager, release 9.x or later.

Cisco Jabber does not display temporary presence.
				Users can see availability status only for contacts in their contact list.

### Disable Temporary
	 Presence in Cisco Unified Presence

Disable temporary
		  presence to increase privacy control. When you configure this parameter, 
		  Cisco Jabber displays availability status only to
		  contacts in a user's contact list.

This feature is
		  supported for on-premises deployment and requires 
		  Cisco Unified Communications Manager, release 8.x or later.

Cisco Jabber does not display temporary presence.
				Users can see availability status only for contacts in their contact list.

### URI
	 Dialing

This feature is
		  supported for on-premises deployments. URI dialing is enabled in 
		  Cisco Unified Communications Manager, release 9.1(2) or later.

This feature is enabled in the jabber-config.xml file using the EnableSIPURIDialling parameter.

Example: <EnableSIPURIDialling>True</EnableSIPURIDialling>

For more information on the values of the parameter, see the Parameters Reference Guide.

Applies to: All clients

The mobile clients don't support URI dialing when the Dial via Office-Reverse feature is enabled.

URI dialing allows
		  users to make calls and resolve contacts with Uniform Resource Identifiers
		  (URI). For example, a user named Adam McKenzie has the following SIP URI
		  associated with his directory number: amckenzi@example.com . URI dialing enables users to
		  call Adam with his SIP URI rather than his directory number.

For detailed
		  information on URI dialing requirements, such as valid URI formats, as well as
		  advanced configuration including ILS setup, see the URI
			 Dialing section of the System Configuration Guide for Cisco Unified Communications Manager .

#### Associate URIs to Directory Numbers

When users make URI calls, Cisco Unified Communications Manager routes the inbound calls to the directory numbers associated to the URIs. For this reason, you must associate URIs with directory numbers. You can either automatically populate directory numbers with URIs or configure directory numbers with URIs.

##### Automatically Populate  Directory Numbers with URIs

When you add users to Cisco Unified Communications Manager, you populate the Directory URI field with a valid SIP URI. Cisco Unified Communications Manager saves that SIP URI in the end user configuration.

When you specify primary extensions for users, Cisco Unified Communications Manager populates the directory URI from the end user configuration to the directory number configuration. In this way, automatically populates the directory URI for the user's directory number.  Cisco Unified Communications Manager also places the URI in the default partition, which is Directory URI .

The following task outlines, at a high level, the steps to configure Cisco Unified Communications Manager so that directory numbers inherit URIs:

Verify that the directory URIs are associated with the directory numbers.

###### Configure
	 Directory Numbers with URIs

You can specify
		  URIs for directory numbers that are not associated with users. You should
		  configure directory numbers with URIs for testing and evaluation purposes only.

To configure
		  directory numbers with URIs, do the following:

The Find
				  and List Directory Numbers window opens.

The Directory Number Configuration window opens.

You cannot
					 manually add URIs to the system Directory URI partition. You should add the URI to
					 the same route partition as the directory number.

##### Associate the Directory URI Partition

You must associate the default partition into which Cisco Unified Communications Manager places URIs with a partition that contains directory numbers.

To enable URI dialing, you must associate the default directory URI partition with a partition that contains directory numbers.

If you do not already have a partition for directory numbers within a calling search space, you should create a partition and configure it as appropriate.

The Enterprise Parameters Configuration window opens.

The default directory URI partition is associated with the partition that contains directory numbers. As a result, Cisco Unified Communications Manager can route incoming URI calls to the correct directory numbers.

You should ensure the partition is in the appropriate calling search space so that users can place calls to the directory numbers.

#### Enable FQDN in SIP
	 Requests for Contact Resolution

To enable contact
		  resolution with URIs, you must ensure that 
		  Cisco Unified Communications Manager uses the fully qualified domain name
		  (FQDN) in SIP requests.

The Find
				  and List SIP Profiles window opens.

You cannot
					 edit the default SIP profile. If required, you should create a copy of the
					 default SIP profile that you can modify.

Associate the SIP
		  profile with all devices that have primary extensions to which you associate
		  URIs.

### Voicemail Avoidance

Applies to: All clients

Voicemail avoidance is a feature that prevents calls from being answered by the mobile service provider voice mail. This feature is useful if a user receives a Mobile Connect call from the enterprise on the mobile device. It is also useful when an incoming DvO-R call is placed to the mobile device.

You can set up voicemail avoidance in one of two ways:

Timer-controlled —(Default) With this method, you set timers on the Cisco Unified Communications Manager to determine if the call is answered by the mobile user or mobile service provider voicemail.

User-controlled —With this method, you set Cisco Unified Communications Manager to require that a user presses any key on the keypad of the device to generate a DTMF tone before the call can proceed.

If you deploy DvO-R, Cisco recommends that you also set user-controlled voicemail avoidance. If you set user-controlled Voicemail Avoidance, this feature applies to both DvO-R and Mobile Connect calls.

For more information about voicemail avoidance, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Features and Services Guide for your release.

- Set Up
	 Timer-Controlled Voicemail Avoidance

- Set Up
	 User-Controlled Voicemail Avoidance

#### Set Up
	 Timer-Controlled Voicemail Avoidance

Set up the timer
		  control method by setting the Answer
			 Too Soon Timer and Answer
			 Too Late Timer on either the Mobility Identity or the Remote
		  Destination. For more information, see the Add Mobility
			 Identity or Add Remote
			 Destination (Optional) topics.

Timer-controlled voicemail avoidance is supported on 
		  Cisco Unified Communications Manager, release 6.0 and later.

#### Set Up
	 User-Controlled Voicemail Avoidance

User-controlled
			 voicemail avoidance is available on 
			 Cisco Unified Communications Manager, release 9.0 and later.

Set up
		  User-Controlled Voicemail Avoidance as follows:

Set up Cisco
				Unified Communications Manager using the Set Up 
				  Cisco Unified Communications Manager to Support Voicemail
				  Avoidance topic.

Set up the
				device using one of the following topics:

Enable Voicemail Avoidance
						on Mobility Identity

Enable Voicemail Avoidance
						on Remote Destination

Cisco does not
			 support user-controlled voicemail avoidance when using DvO-R with alternate
			 numbers that the end user sets up in the client. An alternate number is any
			 phone number that the user enters in the DvO Callback Number field on the
			 client that does not match the phone number that you set up on the user's
			 Mobility Identity.

If you set up
			 this feature with alternate numbers, the 
			 Cisco Unified Communications Manager connects the DvO-R calls even if the
			 callback connects to a wrong number or a voicemail system.

##### Set Up Cisco
	 Unified Communications Manager to Support Voicemail Avoidance

Use this procedure
		  to set up the 
		  Cisco Unified Communications Manager to support user-controlled Voicemail
		  Avoidance.

The settings
				  in this section are not specific to 
				  Cisco Jabber. For information about how to
				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
				  release.

##### Enable Voicemail
	 Avoidance on Mobility Identity

Use this procedure
		  to enable user-controlled voicemail avoidance for the end user's mobility
		  identity.

Set up the
				annunciator on the 
				Cisco Unified Communications Manager. For more information, see the Annunciator setup section in the Cisco Unified Communications Manager Administrator Guide for your
				release.

If you set up
				a Media Resource Group on the 
				Cisco Unified Communications Manager, set up the annunciator on the Media
				Resource Group. For more information, see the Media
				  resource group setup section in the Cisco Unified Communications Manager Administrator Guide for your
				release.

- Select Device > Phone .

- Search for
				  the device that you want to configure.

- Select the
				  device name to open the Phone Configuration window.

To ensure
				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
				  that the end user enters in the 
				  Cisco Jabber client must match the Destination
				  Number that you enter on the Mobility Identity Configuration screen.

- Cisco Unified Communications Manager  release 9 
				   — In the Single Number Reach Voicemail Policy drop-down list,
					 select User Control .

- Cisco Unified Communications Manager release 10 without Dial via Office 
				   — In the Single Number Reach Voicemail Policy drop-down list,
					 select User Control .

- In the Single Number Reach Voicemail Policy drop-down list,
						  select Timer Control .

- In the Dial-via-Office Reverse Voicemail Policy drop-down
						  list, select User Control .

##### Enable Voicemail
	 Avoidance on Remote Destination

Use this procedure
		  to enable user-controlled voicemail avoidance for the end user's remote
		  destination.

Set up the
				annunciator on the 
				Cisco Unified Communications Manager. For more information, see the Annunciator setup section in the 
				Cisco Unified Communications Manager Administrator Guide for your
				release.

If you set up
				a Media Resource Group on the 
				Cisco Unified Communications Manager, set up the annunciator on the Media
				Resource Group. For more information, see the Media
				  resource group setup section in the 
				Cisco Unified Communications Manager Administrator Guide for your
				release.

- Select Device > Phone .

- Search for
				  the device that you want to configure.

- Select the
				  device name to open the Phone Configuration window.

- Cisco Unified Communications Manager
					 release 9
				   — In the Single Number Reach Voicemail Policy drop-down list, select User Control .

- Cisco Unified Communications Manager
					 release 10 without Dial via Office
				  — In the Single Number Reach Voicemail Policy drop-down list, select User Control .

- In the Single Number Reach Voicemail Policy drop-down list, select Timer Control .

- In the Dial-via-Office Reverse Voicemail
							 Policy drop-down list, select User Control .

### File
	 Transfers and Screen Captures

Applies to: All clients

File transfers and
		  screen captures are enabled in Cisco Unified Communications Manager IM and
		  Presence Service. There are additional parameters that are specified in the
		  Cisco Jabber client configuration file. For more information on these
		  parameters, see the Policies parameters.

To configure file
		  transfers and screen captures in Cisco Unified Communications Manager IM and
		  Presence Service 9.x or later, see Enable File Transfers and Screen Captures.

For peer to
				peer chats, see Enable File Transfer and Screen Captures for Peer to Peer
				  Chats only .

For group
				chats and chat rooms, see Enable File Transfer and Screen Captures for Group Chat
				  Rooms .

To configure
				maximum file transfer size, see Configuring Maximum File Transfer Size .

#### Enable File
	 Transfers and Screen Captures

This applies to Cisco Unified Communication Manager IM and Presence Service 9.x, 10.0.x, and 10.5.1. You can enable or disable file transfers and screen captures using the Cisco XCP Router service on Cisco Unified Communications Manager IM and Presence Service. File transfers and screen captures parameter is enabled by default.

File transfers and screen captures are supported for both desktop and mobile clients.

The Service Parameter Configuration window opens.

If you
					 disable the setting on Cisco Unified Communications Manager IM and Presence
					 Service, you must also disable file transfers and screen captures in the client
					 configuration.

#### Enable File
	 Transfer and Screen Captures for Group Chats and Chat Rooms

Files and screen
		  captures transferred are stored on a file server and the metadata is logged to
		  a database server. For Cisco Jabber clients that do not support chat rooms,
		  this option enables file transfer in group chats.

When you enable this option, file transfers and screen captures are
		  also available in peer to peer chats and the files and screen captures
		  transferred are stored on a file server and the metadata is logged to a
		  database server.

File transfer and
		  screen captures for group chats and chat rooms is only available on Cisco
		  Unified Communications Manager IM and Presence Service, release 10.5(2) or later.

Configure an
		  external database to log metadata associated with the file transfer, see Database
			 Setup for IM and Presence Service on Cisco Unified Communications Manager,
			 Release 10.5(2) for
		  further information.

Configure a
		  network file server to save the file being transferred, see Configuration
			 and Administration of IM and Presence Service on Cisco Unified Communications
			 Manager, Release 10.5(2) for further information.

Copy the
				node's public key to the external file server's authorized_keys file, including the node's IP
				address, hostname, or FQDN.

Ensure the Cisco XCP File Transfer Manager service is active.

Restart the Cisco XCP Router service.

#### Enable File
	 Transfer and Screen Captures for Peer to Peer Chats Only

Enable file
		  transfer for peer to peer chats on Cisco Unified Communications Manager IM and
		  Presence Service, release 10.5(2) or later. Files and screen captures are only transferred in a
		  peer to peer chat. The file or screen capture information is not logged or
		  archived.

Restart the Cisco
			 XCP Router service.

#### Configuring
	 Maximum File Transfer Size

The maximum file
		  size is only available on Cisco Unified Communications Manager IM and Presence
		  Service, release 10.5(2) or later.

The file transfer
		  type selected is Managed
			 File Transfer .

Restart the Cisco
			 XCP Router service.

## Cisco Jabber Features  for Windows

### Call Pickup

Applies to: Cisco Jabber for Windows, Cisco Jabber for Mac

The Call Pickup feature allows users to answer calls that come in on a directory number other than their own. Directory numbers are assigned to call pickup groups and Cisco Unified Communications Manager automatically dials the appropriate call pickup group number. Users select Pickup to answer the call.

Group call pickup allows users to pick up incoming calls in another group. Users enter the group pickup number, select Pickup and Cisco Unified Communications Manager automatically dials the appropriate call pickup group number.

Other group pickup allows users to pick up incoming calls in a group that is associated with their group. When the user selects Other Pickup Cisco Unified Communications Manager automatically searches for the incoming call in the associated groups.

Directed call pickup allows users to pick up an incoming call on a directory number. Users enter the directory number, select Pickup and Cisco Unified Communications Manager connects the incoming call.

For more information about configuring call pickup, see the Feature Configuration Guide for Cisco Unified Communications Manager .

#### Call pickup notifications

For multiple incoming calls, the notification displayed is Call(s) available for pickup . When the user answers a call, the user gets connected to the incoming call that has been ringing the longest.

#### Deskphone mode

The Cisco Unified Communications Manager notification settings are not supported for the pickup group. The call pickup notification displayed is CallerA -> CallerB .

The Cisco Unified Communications Manager settings for audio and visual settings are not supported. The visual alerts are always displayed.

#### Shared line behavior

Attempt to pick up a call using the softphone when there is no call available, No call available for PickUp is displayed on the deskphone.

Attempt to pick up a call using the deskphone when there is no call available, No call available for PickUp is displayed on the softphone.

#### User not a member of an associated group

Directed call pickup can be used to pick up the incoming call.

Group pickup does not work

#### Expected behavior using group call pickup and directed call pickup

Softphone mode—The conversation window appears and the annunciator is heard immediately.

Deskphone mode—The conversation window, fast busy tone,  or the annunciator followed by the fast busy tone, Pickup failed error message.

Softphone mode—Tone in headset, no conversation window appears and No call available for pickup error message.

Deskphone mode—No conversation window and No call available for pickup error message.

Softphone mode—Tone in headset, no conversation window appears and No call available for pickup error message.

Deskphone mode—No conversation window and No call available for pickup error message.

Softphone mode—Conversation window appears and fast busy tone.

Deskphone mode—Conversation window appears, fast busy tone, and Pickup failed error message.

Softphone mode—Tone in headset, conversation window appears, and after 15 seconds annunciator followed by the fast busy tone.

Deskphone mode—Conversation window appears, after 15 seconds annunciator, fast busy tone, and Pickup failed error message.

#### Call pickup using a deskphone that is not in a call pickup group

If a user attempts  a call pickup from a deskphone that is not in a call pickup group, the conversation window appears for a moment. The user should not be configured to use the call pickup feature if they are not members of a call pickup group.

#### Original recipient information not available

When the Cisco Unified Communications Manager Auto Call Pickup Enabled setting is true, the recipient information is not available in the client when the call is picked up in softphone mode. If the setting is false, the recipient information is available.

#### Configure Call
	 Pickup Group

Call pickup groups
		  allow users to pick up incoming calls in their own group.

The Find
				  and List Call Pickup Groups window opens.

The Call
				  Pickup Group Configuration window opens.

- Specify a
				  unique name for the call pickup group.

- Specify a
				  unique directory number for the call pickup group number.

- Enter a
				  description.

- Select a
				  partition.

- Select the
				  notification policy.

- Specify
				  the notification timer.

For further
				information on call pickup group notification settings see the call pickup
				topics in the relevant Cisco Unified Communications Manager documentation.

Assign a call
		  pickup group to directory numbers.

#### Assign Directory
	 Number

Assign a call pickup group to a directory number. Only directory
		  numbers that are assigned to a call pickup group can use call pickup, group
		  call pickup, other group pickup, and directed call pickup.

Before you assign a call pickup group to a directory number, you must
		  create the call pickup group.

Select Call
						  Routing > Directory Number , find
					 and select your directory number and in the 
					 Call Forward and Call Pickup Settings
					 area select the call pickup group from the call pickup group drop down list.

Select Device > Phone ,
					 find and select your phone and in the Association Information list choose the directory number to which the call
					 pickup group will be assigned.

#### Configure Other
	 Call Pickup

Other Group Pickup allows users to pick up incoming calls in an   associated group. Cisco Unified Communications Manager
		  automatically searches for the incoming call in the associated groups to make
		  the call connection when the user selects Other Pickup .

Before you begin,
		  configure call pickup groups.

The Find
				  and List Call Pickup Groups window opens.

The Call
				  Pickup Group Configuration window opens.

Find call
					 pickup groups and add to current associated call pickup groups.

Reorder
					 associated call pickup groups or remove call pickup groups.

#### Configure Directed
	 Call Pickup

Directed call
		  pickup allows you to pick up a incoming call directly. The user enters the
		  directory number in the client and selects Pickup . Cisco Unified Communications Manager uses
		  the associated group mechanism to control if the user can pick up an incoming
		  call using Directed Call Pickup.

To enable directed
		  call pickup, the associated groups of the user must contain the pickup group to
		  which the directory number belongs.

When the user
		  invokes the feature and enters a directory number to pick up an incoming call,
		  the user connects to the call that is incoming to the specified phone whether
		  or not the call is the longest incoming call in the call pickup group to which
		  the directory number belongs.

For more
				information, see topics related to defining a pickup group for Other Group
				Pickup.

For more
				information, see topics related to configuring Auto Call Pickup.

#### Auto Call
	 Pickup

You can automate call pickup, group pickup, other group pickup, and
		  directed call pickup by enabling the Auto Call Pickup Enabled service
		  parameter.
		When this parameter is enabled, 
		  Cisco Unified Communications Manager automatically connects users to the incoming call in their own pickup group, in
		  another pickup group, or a pickup group that is associated with their own group
		  after users select the appropriate pickup on the phone. This action requires
		  only one keystroke.

Auto call pickup connects the user to an incoming call in the group of
		  the user. When the user selects Pickup on the client, 
		  Cisco Unified Communications Manager
		  locates the incoming call in the group and completes the call connection. If
		  automation is not enabled, the user must select Pickup and answer the call, to make the call
		  connection.

Auto group call pickup connects the user to an incoming call in
		  another pickup group. The user enters the group number of another pickup group
		  and selects Pickup on the client. Upon receiving the pickup
		  group number, 
		  Cisco Unified Communications Manager
		  completes the call connection. If auto group call pickup is not enabled, dial
		  the group number of another pickup group, select Pickup on the client, and answer the call to
		  make the connection.

Auto other group pickup connects the user to an incoming call in a
		  group that is associated with the group of the user. The user selects Other Pickup on the client. 
		  Cisco Unified Communications Manager
		  automatically searches for the incoming call in the associated groups in the
		  sequence that the administrator enters in the Call Pickup Group Configuration window and completes the call connection after the call is found. If automation
		  is not enabled, the user must select Other Pickup , and answer the call to make the
		  call connection.

Auto directed call pickup connects the user to an incoming call in a
		  group that is associated with the group of the user. The user enters the
		  directory number of the ringing phone and selects Pickup on the client. Upon receiving the
		  directory number, 
		  Cisco Unified Communications Manager
		  completes the call connection. If auto directed call pickup is not enabled, the
		  user must dial the directory number of the ringing phone, select Pickup , and answer the call that will now ring
		  on the user phone to make the connection.

For more information about Call Pickup , see the Feature Configuration Guide for Cisco Unified Communications
Manager .

- Configure Auto
	 Call Pickup

##### Configure Auto
	 Call Pickup

- true—The auto call pickup feature is enabled.

- false—The auto call pickup feature is not enabled. This is the
						default value.

### Persistent Chat
	 Rooms

Applies to: Cisco Jabber for Windows, Cisco Jabber for Mac

- Configure
	 Persistent Chat

- Administer and
	 Moderate Persistent Chat Rooms

- Enable Persistent
	 Chat Room Passwords

#### Configure
	 Persistent Chat

Persistent chat
		  must be enabled and configured on Cisco Unified Communications Manager IM and
		  Presence Service before it can be used by the client.

Persistent chat is
		  only available on Cisco Unified Communications Manager IM and Presence Service
		  10.0 and later.

Refer to Database
			 Setup for IM and Presence Service on Cisco Unified Communications
			 Manager for your release for information on the database configuration
		  necessary to support the persistent chat feature. Database configuration must
		  be performed before continuing with this task.

Local chat message
		  archiving must be enabled for persistent chat. Local chat message archiving is
		  enabled on Cisco Unified Communications Manager IM and Presence Service using
		  the Allow clients to
			 log instant message history setting, for more information, see the Enable Message Settings topic.

Persistent Chat Setting

Recommended Value

Notes

System automatically manages primary group chat server aliases

Disabled

Enable persistent chat

Enabled

Archive all room joins and exits

Administrator Defined

This value is not currently used by for persistent chat.

Archive all room messages

Enabled

Allow only group chat system administrators to create persistent chat rooms

Administrator Defined

Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment.

Maximum number of persistent chat rooms allowed

Administrator Defined

Number of connections to the database

Default Value

Database connection heartbeat interval (seconds)

Default Value

Timeout value for persistent chat rooms (minutes)

Default Value

Maximum number of rooms allowed

Default Value

Rooms are for members only by default

Disabled

Room owners can change whether or not rooms are for members only

Enabled

Cisco Jabber requires this value to be Enabled.

Only moderators can invite people to members-only rooms

Enabled

Cisco Jabber requires this value to be Enabled.

Room owners can change whether or not only moderators can invite people to members-only rooms

Enabled

Users can add themselves to rooms as members

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change whether users can add themselves to rooms as members

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Members and administrators who are not in a room are still visible in the room

Enabled

Cisco Jabber requires this value to be Enabled.

Room owners can change whether members and administrators who are not in a room are still visible in the room

Enabled

Rooms are backwards-compatible with older clients

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change whether rooms are backwards-compatible with older clients

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Rooms are anonymous by default

Disabled

This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms.

Room owners can change whether or not rooms are anonymous

Disabled

This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms.

Lowest participation level a user can have to invite others to the room

Default Value

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change the lowest participation level a user can have to invite others to the room

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

How many users can be in a room at one time

Administrator Defined

Cisco recommends using the default value.

How many hidden users can be in a room at one time

Administrator Defined

Default maximum occupancy for a room

Default Value

Room owners can change default maximum occupancy for a room

Default Value

Lowest participation level a user can have to send a private message from within the room

Default Value

Room owners can change the lowest participation level a user can have to send a private message from within the room

Default Value

Lowest participation level a user can have to change a room's subject

Moderator

Room owners can change the lowest participation level a user can have to change a room's subject

Disabled

Remove all XHTML formatting from messages

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change XHTML formatting setting

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Rooms are moderated by default

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change whether rooms are moderated by default

Default Value

This value is not currently used by Cisco Jabber for persistent chat.

Maximum number of messages that can be retrieved from the archive

Default Value

Number of messages in chat history displayed by default

Administrator Defined

Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue to use their originally configured value.

Room owners can change the number of messages displayed in chat history

Default Value

This value is not currently used by Cisco Jabber for persistent chat.

Ensure you configure any client-specific parameters for persistent chat. For more information, see the Client parameters section of the latest Parameters Reference Guide for Cisco Jabber.

Enable file transfer in chat rooms. For more information, see Enable File Transfer and Screen Captures for Group Chats and Chat Rooms .

#### Administer and
	 Moderate Persistent Chat Rooms

Persistent Chat Rooms and their administration is for
					 on-premises deployments only.

Persistent Chat Rooms are not available for mobile clients.

You administer
		  persistent chat rooms from the Jabber client by creating rooms, delegating
		  their moderators, and specifying members. The node on which the room is created
		  is created automatically, although you can override it and specify a specific
		  node. Administrators and moderators are privileged users in Persistent Chat
		  rooms. You can administer Persistent Chat rooms on any service node that you
		  are an administrator for on Cisco Unified Communications Manager IM and
		  Presence servers.

##### Administrator
		  Capabilities

Create rooms.
				When you create a room, you automatically become the room administrator.

Define and
				change up to 30 moderators for a chat room (who become room
				  owners ).

Specify and
				change the room name.

Define the
				maximum number of participants in a room. This number cannot be less than the
				number of participants already in a room.

Add and remove
				room members.

Block, remove,
				and revoke participants.

Destroy rooms
				(which removes it from the server, but the history is not deleted).

##### Moderator
		  Capabilities

- Change the subject of a
			 room.

- Edit members (which
			 includes adding, removing, and banning them).

##### Room
		  Creation

Room name
				(required, maximum 200 characters)

Description

Room type
				(public or restricted)

After the room
				type has been defined, it cannot be changed by anyone.

Specify
				whether to add the room to your My
				  Rooms tab (off by default)

Add up to 30
				moderators (who must have a valid Jabber ID to moderate a room).

Room password

After you create
		  the room, you have the option to add members to the room immediately or at a
		  later time. Refresh the All
			 Rooms list in order to see your new room in the list of available
		  rooms.

#### Enable Persistent
	 Chat Room Passwords

Persistent chat rooms that are password protected means that when
		  users enter a room within a Jabber session, they must enter the password.
		  Password protected rooms comply with the XEP-0045 specification from the XMPP
		  Standards Foundation.

### Integration with
	 Microsoft Products

Applies to: Cisco Jabber for Desktop Clients

Cisco
			 Jabber for Windows supports a range of Microsoft products that
		  integrate with the application. This section describes the support and
		  integrations for these products.

#### Internet
		  Explorer

Microsoft
		  Internet Explorer 8 or later is required. Cisco Jabber for Windows uses the Internet Explorer
		  rendering engine to display HTML content.

Cisco Jabber for Windows requires Internet Explorer active scripting to render IMs. See https:/​/​windows.microsoft.com/​en-US/​windows/​help/​genuine/​ie-active-script for instructions on enabling active scripting.

Internet
			 Explorer 9 users in Cloud-based deployments that use Single Sign On (SSO) get
			 security alerts when they sign in to Cisco Jabber for Windows . Add webexconnect.com to the list of websites in the Compatibility View Settings window of Internet
			 Explorer 9 to stop these alerts.

#### Office

Integration with
		  the following versions of Office is supported:

Microsoft
				Office 2013, 32 and 64 bit

Microsoft
				Office 2010, 32 and 64 bit

#### Office
		  365

Microsoft Office
		  365 supports different configuration types based on the plan or subscription
		  type. Cisco Jabber for Windows has been tested with small
		  business plan P1 of Microsoft Office 365. This plan requires an on-premises
		  Active Directory server.

Client-side
		  integration with Microsoft Office 365 is supported with the following
		  applications:

Microsoft
				Office 2013, 32 bit and 64 bit

Microsoft
				Office 2010, 32 bit and 64 bit

Microsoft
				SharePoint 2010

#### SharePoint

Integration with
		  the following versions of SharePoint is supported:

Microsoft
				SharePoint 2013

Microsoft
				SharePoint 2010

Availability
		  status in Microsoft SharePoint sites is supported only if users access those
		  sites with Microsoft Internet Explorer. You should add the Microsoft SharePoint
		  site to the list of trusted sites in Microsoft Internet Explorer.

#### Calendar
	 Integration

Microsoft
				Outlook 2013, 32 bit and 64 bit

Microsoft
				Outlook 2010, 32 bit and 64 bit

IBM Lotus
				Notes 9, 32 bit

IBM Lotus
				Notes 8.5.3, 32 bit

IBM Lotus
				Notes 8.5.2, 32 bit

IBM Lotus
				Notes 8.5.1, 32 bit

Google
				Calendar

#### Microsoft Outlook Calendar Events

Applies to: Cisco Jabber for Windows

You must apply a
		  setting in 
		  Microsoft Outlook so that calendar events display in Cisco Jabber for Windows .

- Select File > Account
						Settings .

- Select the Email tab on the Account Settings window.

In most cases,
				the server name is Microsoft Exchange .

When users create
		  calendar events in 
		  Microsoft Outlook, those events display in the Meetings tab.

#### Microsoft Outlook Presence
	 Integration

Applies to: Cisco Jabber for Desktop Clients

To enable integration with Microsoft Outlook , you must specify SIP:user@cupdomain as the value of the proxyAddresses attribute in Microsoft Active Directory . Users can then share availability in Microsoft Outlook .

Use one of the following methods to modify the proxyAddresses attribute:

An Active Directory administrative tool such as Active Directory User and Computers

The Active Directory User and Computers administrative tool allows you to edit attributes on Microsoft Windows Server
			 2008 or later.

ADSchemaWizard.exe utility

The ADSchemaWizard.exe utility is available in the Cisco Jabber administration package . This utility generates an LDIF file that modifies your directory to add the proxyAddresses attribute to each user with the following value: SIP:user@cupdomain .

You should use the ADSchemaWizard.exe utility on servers that do not support the edit attribute feature in the Active Directory User and Computers administrative tool. You can use a tool such as ADSI Edit to verify the changes that you apply with the ADSchemaWizard.exe utility.

The ADSchemaWizard.exe utility requires Microsoft .NET Framework version 3.5 or later.

Create a script with Microsoft Windows PowerShell

Refer to the appropriate Microsoft documentation for creating a script to enable presence in Microsoft Outlook .

##### Enable Presence with the Active Directory User and Computers Tool

Complete the following steps to  enable presence in Microsoft Outlook for individual users with the Active Directory User and Computers administrative tool:

For example, SIP:msmith@cisco.com .

Where the user@cupdomain value is the user's instant messaging address. cupdomain corresponds to the domain for Cisco Unified Presence or Cisco Unified Communications Manager IM and Presence Service .

##### Add Local Contacts
	 from Microsoft Outlook

Cisco Jabber for Windows lets users search for and add
		  local contacts in 
		  Microsoft Outlook. To enable this integration with
		  Microsoft Outlook, you must enable Cached Exchange Mode on the Microsoft
		  Exchange server.

Select File > Options .

Select the Integration tab ( Calendar tab from release 11.0).

Select either None or Microsoft Outlook .

To
		  add local 
		  Microsoft Outlook contacts to contact lists in the
		  client, local contacts must have instant message addresses in 
		  Microsoft Outlook.

To show contact
		  photos in the client interface, local contacts in 
		  Microsoft Outlook must have instant message addresses.

To communicate with local contacts in 
		  Microsoft Outlook using the client, local contacts
		  must have the relevant details. To send instant messages to contacts, local
		  contacts must have an instant message address. To call contacts in 
		  Microsoft Outlook, local contacts must have phone
		  numbers.

#### Chat History
	 in Microsoft Outlook

Applies to: Cisco Jabber for Windows

Version
						of Cisco Jabber for Windows

Supported Servers

10.6

Microsoft Exchange 2013

Microsoft Exchange 2010

11.0

Microsoft Office 365

Microsoft Exchange 2013

Microsoft Exchange 2010

You can enable the
		  client to automatically save chat histories to a Cisco
			 Jabber Chats folder in the user's Microsoft Outlook application. When a
		  user closes a chat window, the client saves the IM conversation to the Exchange
		  server.

Set the EnableSaveChatHistoryToExchange parameter to true in the jabber-config.xml file.

(optional) Set
			 up a method to authenticate users to the Exchange server. If you don't specify
			 an authentication method, then users can authenticate directly from the Outlook tab in the Options menu of their clients.

Specify the
			 method for determining which server to use.

For more
		  information about all of the parameters that are needed to enable this feature,
		  see the Parameters  Reference Guide .

- Limitations for Saving Chat History to an Outlook Folder

- Authentication Modes

- Specify Server
	 Addresses

##### Limitations for Saving Chat History to an Outlook Folder

This feature can only be enabled if users have a Cisco Unified Communications Manager account.

###### Limitations with Authentication Methods over Cisco Expressway for Mobile and Remote Access

If you are enabling this feature for users connecting via the Expressway for Mobile and Remote Access, the following limitations apply:

If the client detects that the user is connecting via the Expressway, then the client uses the External Server option for the Exchange connection. If the external server is not set, then it uses the internal server.

If the client detects that the user is not connecting via the Expressway, then the client uses the Internal Server option for the Exchange connection. If the internal server is not set, the client uses the external server.

However, if either the internal or external server is set, but for some reason Cisco Jabber can't connect to it, the client doesn't revert to using the other server.

##### Authentication Modes

You must set up a method of authentication for the client to authenticate with the Exchange server. When authentication is complete, the client has access to the Exchange server which allows saving chat histories to a folder in Outlook.

If you do not specify an authentication method, then users must manually input their Exchange credentials in the Outlook tab in the client.

- Authenticate Using
	 Single Sign On for the Operating System

- Authenticate by
	 Synching Credentials

###### Authenticate Using
	 Single Sign On for the Operating System

Applies to Cisco Jabber for Windows only.

Do not use this authentication method if some users share the same Windows account. The client authenticates with the account on the Operating System, and not with the user who is logged in to Cisco Jabber. For example, User A logs onto a Windows machine and then logs into Cisco Jabber for a morning shift. When the shift is done, Jabber is reset and User B logs into the client for the afternoon shift. Because User A is logged into the Windows account, then the chat messages from User B are saved in the Outlook account for User A.

Users and their
		  computers must use domains. Authentication using single sign on does not work
		  if users are local Windows users.

###### Authenticate by
	 Synching Credentials

You can sync the Exchange credentials with another set of credentials for users, such as the Cisco Unified Communications Manager IM and Presence credentials. Using this method, the client uses the credentials to authenticate to the Exchange server.

##### Specify Server
	 Addresses

After you enable
		  an authentication method for the client to access the Exchange server, you must
		  enable a method for the client to specify the Exchange server address.

If you do not
		  specify server addresses, then users must manually enter the internal and
		  external Exchange servers in the client, in the Outlook > Advanced tab of the Options menu.

###### Detect Server
	 Addresses Automatically

Applies to Cisco Jabber for Windows only.

You can configure the client to automatically discover the Exchange servers based on users' domain. This domain is defined when you set up the authentication method by using the domain that was specified for the user's credentials.

https://< domain >/autodiscover/autodiscover.svc

https://autodiscover.< domain >/autodiscover/autodiscover.svc

###### Define Server
	 Addresses

You can define the
		  internal and external Exchange server addresses in the configuration file.

### IBM Notes Contact Search and Calendar Integration

Applies to: Cisco Jabber for Windows

Cisco Jabber for Windows supports IBM Notes calendar integration in the Meetings tab of the client. Cisco Jabber also lets users search for and add local contacts from IBM Notes. To enable this integration with IBM Notes, you must set the following parameters:

EnableLocalAddressBookSearch =true

EnableLotusNotesContactResolution =true

CalendarIntegrationType =2

The CalendarIntegrationType parameter can be overridden by users. To enable calendar integration and contact resolution with IBM Notes, users must ensure that the Calendar integration type on the Calendar tab of the Options window  is set to IBM Notes .

In order for users to be able to successfully add IBM Notes contacts to their contact lists, the Messaging ID field in IBM Notes must contain a valid value.

#### Contact Resolution for Incoming Calls

For incoming calls, Cisco Jabber for Windows does not search the address book in IBM Notes, therefore only the phone number for an IBM Notes contact shows in the call history. If Cisco Jabber users subsequently search  for the contact associated with the phone number, the call history changes to show the contact's name instead of the phone number.

### Custom
	 Emoticons

Applies to: Cisco Jabber for Windows

You can add custom
		  emoticons to Cisco Jabber for Windows by creating emoticon definitions in an
		  XML file and saving it to the file system.

Dimensions: 17 x 17 pixels

Transparent background

PNG file
					 format

RGB colors

See Emoticon
				  Definitions for more information on the structure and available
				parameters for emoticonDefs.xml .

Cisco Jabber for Windows loads emoticon definitions from the
				following directories on the file system.

For 32-bit operating systems:

Program Files\Cisco Systems\Cisco
								  Jabber\Emoticons

Program Files\Cisco Systems\Cisco
								  Jabber\CustomEmoticons

For 64-bit operating systems:

Program Files(x86)\Cisco Systems\Cisco
								  Jabber\Emoticons

Program Files(x86)\Cisco Systems\Cisco
								  Jabber\CustomEmoticons

The Emoticons folder contains the default
					 emoticons for Cisco Jabber for Windows and the default emoticonDefs.xml .

The CustomEmoticons folder does not exist by
					 default. Administrators can create this folder to contain custom emoticon
					 definitions to include in organizational deployments.

Emoticons
					 that you define in the CustomEmoticons folder take precedence over emoticon
					 definitions in the default Emoticons folder.

%USERPROFILE% \AppData\Roaming\Cisco\Unified
						Communications\Jabber\CSF\CustomEmoticons

This
					 folder contains custom emoticon definitions for individual instances of Cisco
					 Jabber for Windows.

Emoticons
					 that you define in this directory take precedence over emoticon definitions in
					 the CustomEmoticons folder in the installation directory.

Cisco Jabber for
		  Windows loads the custom emoticon definitions in emoticonDefs.xml .

User A
					 defines a custom emoticon in emoticonDefs.xml .

The custom
					 emoticon definition exists only on User A's local file system.

User A
					 sends that custom emoticon to User B.

User B
					 receives only the default key for the custom emoticon. User B does not receive
					 the icon.

#### Emoticon Definitions

Cisco Jabber for Windows loads emoticon definitions from emoticonDefs.xml .

```
<emoticons>
 <emoticon defaultKey="" image="" text="" order="" hidden="">
  <alt></alt>
 </emoticon>
</emoticons>
```

This element contains all emoticon definitions.

This element contains the definition of an emoticon.

This attribute defines the default key combination that renders the emoticon.

Specify any key combination as the value.

This attribute is required.

defaultKey is an attribute of the emoticon element.

This attribute specifies the filename of the emoticon image.

Specify the filename of the emoticon as the value. The emoticon image must exist in the same directory as emoticonDefs.xml .

This attribute is required.

Cisco Jabber for Windows supports any icon that Internet Explorer can render, including .jpeg , .png ,  and .gif .

image is an attribute of the emoticon element.

This attribute defines the descriptive text that displays in the Insert emoticon dialog box.

Specify any string of unicode characters.

This attribute is optional.

text is an attribute of the emoticon element.

This attribute defines the order in which emoticons display in the Insert emoticon dialog box.

Specify an ordinal number beginning from 1 as the value.

order is an attribute of the emoticon element.

This attribute is required. However, if the value of hidden is true this parameter does not take effect.

This attribute specifies whether the emoticon displays in the Insert emoticon dialog box.

This attribute is optional.

hidden is an attribute of the emoticon element.

This element enables you to map key combinations to emoticons.

Specify any key combination as the value.

For example, if the value of defaultKey is :) , you can specify :-) as the value of alt so that both key combinations render the same emoticon.

This element is optional.

:callme

:telephone

##### Emoticon Definition Example

```
<emoticons>
 <emoticon defaultKey=":)" image="Emoticons_Smiling.png" text="Smile" order="1">
  <alt>:-)</alt>
  <alt>^_^</alt>
 </emoticon>
 <emoticon defaultKey=":(" image="Emoticons_Frowning.png" text="Frown" order="2">
  <alt>:-(</alt>
 </emoticon>
</emoticons>
```

## Cisco Jabber Features for Mac

### Persistent Chat Room
	 Support

Users can participate in persistent chat rooms

Users can carry out text searches within the persistent chat rooms

### Local Contacts in
	 Mac Address Book

Cisco Jabber
		  allows users search for and add local contacts in the Mac Address book.

Select Jabber > Install Mac
					 Address Book Plug-In .

To enable the Address Book plug-in:

Select Jabber > Preferences > General > Enable "Mac Address
					 Plug-in" .

Restart the client for this to take effect.

To communicate with local contacts in Mac Address
		  book using the client, local contacts must have the relevant details. To send
		  instant messages to contacts, local contacts must have an instant message
		  address. To call contacts in Mac Address book, local contacts must have phone
		  numbers.

## Cisco Jabber for Android and iOS

### Call Park

Applies to: Cisco Jabber for Android, Cisco Jabber for iOS

You can use call
		  park to place a call on hold and pick it up from another phone in a Cisco
			 Unified Communication Manager system. Call park must be enabled and extension numbers must be defined on each Cisco
			 Unified Communication Manager node in a cluster. You can define either a single directory
		  number or a range of directory numbers for use as call park extension numbers.

Complete the following tasks to enable call park. For detailed instructions, see the Feature Configuration Guide for Cisco Unified Communications Manager .

Create a partition to add a call park number.

Configure a
			 call park number 
		  to use call park across nodes in a cluster.

You can define
		either a single directory number or a range of directory numbers for use as
		call park extension numbers. You can park only one call at each call park
		extension number.

### Set Up Cisco
	 Unified Communications Manager to Support Dial via Office

To set up Cisco Unified Communications Manager to support
		  Dial via Office-Reverse ( DvO-R), perform the following procedures:

Complete one
				or both of the following procedures.

Set Up Enterprise Feature
						Access Number

Set Up Mobility
						Profile

Complete the Verify
				  Device COP File Version procedure.

If necessary,
				create application dial rules to allow the system to route calls to the Mobile
				Identity phone number to the outbound gateway. Ensure that the format of the
				Mobile Identity phone number matches the application dial rules.

#### Set Up Enterprise Feature Access Number

Use this procedure to set up an Enterprise Feature Access Number for all Cisco Jabber calls that are made using Dial via Office-Reverse.

The Enterprise Feature Access Number is the number that Cisco Unified Communications Manager uses to call the mobile phone and the dialed number unless a different number is set up in Mobility Profile for this purpose.

Reserve a Direct Inward Dial (DID) number to use as the Enterprise Feature Access Number (EFAN). This procedure is optional if you already set up a mobility profile.

Determine the required format for this number. The exact value you choose depends on the phone number that the gateway passes (for example, 7 digits or 10 digits).  The Enterprise Feature Access Number must be a routable number.

Enter a DID number that is unique in the system.

To support dialing internationally, you can prepend this number with \+.

This partition is set under System > Service Parameters , in the Clusterwide Parameters (System - Mobility) section,  in the Inbound Calling Search Space for Remote Destination setting. This setting points either to the Inbound Calling Search Space of the Gateway or Trunk, or to the Calling Search Space assigned on the Phone Configuration window for the device.

If the user sets up the DvO Callback Number with an alternate number, ensure that you set up the trunk Calling Search Space (CSS) to route to destination of the alternate phone number.

#### Set Up Mobility Profile

Use this procedure to set up a mobility profile for Cisco Jabber devices. This procedure is optional if you already set up an Enterprise Feature Access Number.

Mobility profiles allow you to set up the Dial via Office-Reverse settings for a mobile client. After you set up a mobility profile, you can assign it to a user or to a group of users, such as the users in a region or location.

#### Verify Device COP
	 File Version

Use the following
		  procedure to verify that you are using the correct device COP file for this
		  release of 
		  Cisco Jabber.

If you can see
				the Video Capabilities drop-down list, the COP file is already installed on
				your system.

If you cannot
				see the Video Capabilities drop-down list, locate and download the correct COP
				file.

### Prerequisite for
	 All Clients

On-premises Deployment

Cisco Unified Communications Manager 9.x and higher

### Dial via
	 Office

Applies to: Cisco Jabber for Android, Cisco Jabber for iOS

URI dialing

Secure
				Phone

User-controlled
		  voicemail avoidance, which can be used in conjunction with the DvO feature, is
		  available only on Cisco Unified Communications Manager release 9.0 and
		  later. Timer-controlled voicemail avoidance is available on Cisco Unified Communications Manager release 6.0 and
		  later.

You can make
		  DvO-R calls over Expressway for Mobile and Remote Access when you are outside
		  corporate network. DvO-R is supported on Cisco Expressway X8.7 and Cisco
		  Unified Communications Manager 11.0(1a)SU1.

The DvO feature
		allows users to initiate Cisco Jabber outgoing calls with their work number
		using the mobile voice network for the device.

Cisco Jabber supports DvO-R (DvO-Reverse) calls, which
		works as follows:

User initiates a
			 DvO-R call.

The client
			 notifies Cisco Unified Communications Manager to call the
			 mobile phone number.

Cisco
				Unified Communications Manager calls and connects to the mobile phone
			 number.

Cisco
				Unified Communications Manager calls and connects to the number that
			 the user dialed.

Cisco
				Unified Communications Manager connects the two segments.

The user and the
			 called party continue as with an ordinary call.

Incoming calls use
		either Mobile Connect or the Voice over IP, depending on which Calling Options
		the user sets on the client. Dial via Office does not require Mobile Connect to
		work. However, we recommend that you enable Mobile Connect to allow the native
		mobile number to ring when someone calls the work number. From the Cisco Unified Communications Manager user pages, users
		can enable and disable Mobile Connect, and adjust Mobile Connect behavior using
		settings (for example, the time of day routing and Delay Before Ringing Timer
		settings). For information about setting up Mobile Connect, see the Set Up Mobile
		  Connect topic.

Connection

Calling
				Options

Voice over
				IP

Mobile Voice
				Network

Autoselect

Corporate
				Wi-Fi

Outgoing:
				VoIP

Incoming:
				VoIP

Outgoing:
				DvO-R

Incoming:
				Mobile Connect

Outgoing:
				VoIP

Incoming:
				VoIP

Noncorporate
				Wi-Fi

Mobile
				Network (3G, 4G)

Outgoing:
				DvO-R

Phone
				Services are not registered

To set up Dial via
	 Office-Reverse (DvO-R), you must do the following:

Set up the Cisco Unified Communications Manager to support DvO-R.
		  See the Set Up Cisco
			 Unified Communications Manager to Support DvO topic for more
		  information.

Enable DvO on each
		  Cisco Dual Mode for iPhone device. See the Set Up Dial
			 via Office for Each Device topic for more information.

Enable DvO on each
		  Cisco Dual Mode for Android device. See the Set Up Dial
			 via Office for Each Device topic for more information.

- Set Up Dial via Office for Each Device

#### Set Up Dial via Office for Each Device

Use the following procedures to set up Dial via Office - Reverse for each TCT device.

Use the following procedures to set up Dial via Office - Reverse for each BOT device.

Add a Mobility Identity for each user.

Enable Dial via Office on each device.

If you enabled Mobile Connect, verify that Mobile Connect works. Dial the desk phone extension and check that the phone number that is specified in the associated Mobile Identity rings.

##### Add Mobility
	 Identity

Use this procedure
		  to add a mobility identity to specify the mobile phone number of the mobile
		  device as the destination number. This destination number is used by features
		  such as Dial via Office or mobile connect.

You can specify
		  only one number when you add a mobility identity. If you want to specify an
		  alternate number such as a second mobile phone number for a mobile device, you
		  can set up a remote destination. The mobility identity configuration
		  characteristics are identical to those of the remote destination configuration.

- Select Device > Phone .

- Search
				  for the device that you want to configure.

- Select
				  the device name to open the Phone Configuration window.

You must be able to rout this number to an outbound gateway. Generally, the number is the full
				E.164 number.

If you
				  enable the Dial via Office — Reverse feature for a user, you must enter a
				  destination number for the user's mobility identity.

The
						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
						network and VPN.

The
						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
						network.

The
						logs do not indicate why the phone service cannot connect.

These values
				ensure that calls are not routed to the mobile service provider voicemail
				before they ring in the client on the mobile device. You can adjust these
				values to work with the end user's mobile network. For more information, see
				the online help in Cisco Unified Communications Manager.

Setting

Suggested Initial Value

Answer Too Soon Timer

3000

Answer Too Late Timer

20000

Delay Before Ringing Timer

0

This setting does not apply to DvO-R calls.

Setting

Suggested Initial Value

Wait * before ringing this phone when my business line
							 is dialed.*

0.0 seconds

Prevent this call from going straight to this phone's
							 voicemail by using a time delay of * to detect when calls go straight to
							 voicemail.*

3.0 seconds

Stop ringing this phone after * to avoid connecting to
							 this phone's voicemail.*

20.0 seconds

- Cisco Unified
				Communications Manager release 9 or earlier —  Check the Enable Mobile Connect check box.

- Cisco Unified
				Communications Manager release 10 —  Check the Enable Single Number Reach check box.

Option

Description

Leave
				  blank

Choose
					 this option if you want users to use the Enterprise Feature Access Number
					 (EFAN).

Mobility
				  Profile

Choose the
					 mobility profile that you just created if you want users to use a mobility
					 profile instead of an EFAN.

##### Enable Dial via
	 Office on Each Device

Use this procedure
		  to enable Dial via Office on each device.

- Select Device > Phone .

- Search for
				  the device that you want to configure.

- Select the
				  device name to open the Phone Configuration window.

DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from the Cisco Unified Communications Manager administrative interface fixes this issue.

Test this feature.

### Mobile Connect

Applies to: Cisco Jabber for Android, Cisco Jabber for iOS

Mobile connect, formerly known as Single Number Reach (SNR),
allows the native mobile phone number to ring
		  when someone calls the work number if:

Cisco Jabber is not available—After Cisco Jabber becomes available again and connects to the corporate network, Cisco Unified Communications Manager returns to placing VoIP calls rather than using mobile connect.

The user selects the Mobile Voice Network calling option.

The user selects the Autoselect calling option and the user is outside of the Wi-Fi network.

To configure the mobile device phone number.

To configure an alternate phone number.

Exit Cisco Jabber on the
			 mobile device.

Call the Cisco Jabber extension from another phone.

Verify that the native mobile network phone number rings and that the call connects when you answer it.

#### Enable Mobile
	 Connect

Use the
		  following procedure to enable mobile connect for an end user.

- Select Device > Remote
						Destination .

- Search for
				  the destination number.

- Delete the
				  destination number.

- Select User
						Management > End User .

- Search for
				  the end user.

- Select the user id to open the End User Configuration window.

- In the
				  Mobility Information section, check the Enable Mobility check box.

- On 
				  Cisco Unified Communications Manager Release 9.0 and earlier, specify the
				  Primary User Device.

- Select Save .

- Navigate
				  to Device > Phone .

- Search for the device that you want to configure.

- Select the device name to open the Phone Configuration window.

Setting

Information

Softkey Template

Choose a softkey template that includes the Mobility button.

For information about setting up softkey templates, see the
								  related information in the Cisco Unified Communications Manager Administration Guide for your release. This documentation can be found in the maintenance guides
								  list.

Mobility User ID

Select the user.

Owner User ID

Select the user. The value must match the mobility user ID.

Rerouting Calling Search Space

Choose a Rerouting Calling Search Space that includes both of
								  the following:

The partition of the desk phone extension of the user. This
										requirement is used by the system to provide the Dial via Office feature, not
										for routing calls.

A route to the mobile phone number. The route to the mobile
										phone number (that is, the Gateway/Trunk partition) must have a higher
										preference than the partitions of the enterprise extension that is associated
										with the device.

Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable.

If the user sets up the DvO Callback Number with an alternate
								  number, ensure that you set up the trunk Calling Search Space (CSS) to route to
								  destination of the alternate phone number.

- Select Save .

#### Add Remote
	 Destination (Optional)

Use this procedure
		  to add a remote destination to specify any alternate number as the destination
		  number. The Mobility Identity configuration characteristics are identical to
		  those of the remote destination configuration.

Alternate numbers
		  can be 
		  any type of
		  phone number, such as home phone numbers, conference room numbers, desk phone
		  numbers, or multiple mobile phone numbers for additional mobile devices. You
		  can add more than one remote destination.

- Select Device > Phone .

- Search for
				  the device that you want to configure.

- Select the
				  device name to open the Phone Configuration window.

You must be able to rout the number to an outbound gateway. Generally, the number is the full
				E.164 number.

- Answer Too Soon Timer —Enter 3000

- Answer Too Late Timer — 
						  Enter 20000

This setting does not apply to DvO-R calls.

These values
				ensure that calls are not routed to the mobile service provider voicemail
				before they ring in the client on the mobile device. For more
				information, see the online help in Cisco Unified Communications Manager.

- If you have Cisco Unified Communications Manager
						Version 9 or earlier, check the Enable Mobile Connect check box.

- If you have 
				Cisco Unified Communications Manager Version 10, check the Enable Single Number Reach check box.

### Move to Mobile

Applies to: Cisco Jabber for Android, Cisco Jabber for iOS

Users can transfer
		  an active VoIP call from 
		  Cisco Jabber to their mobile phone number on the
		  mobile network. This feature is useful when a user on a call leaves the Wi-Fi
		  network (for example, leaving the building to walk out to the car), or if there
		  are voice quality issues over the Wi-Fi network.

Implementation Method

Description

Instructions

Handoff DN

The
						mobile device calls 
						Cisco Unified Communications Manager using the mobile network.

This
						method requires a Direct Inward Dial (DID) number.

The
						service provider must deliver the DID digits exactly as configured.
						Alternately, for Cisco IOS gateways with H.323 or SIP communication to 
						Cisco Unified Communications Manager, you can use Cisco IOS to manipulate
						the inbound called-party number at the gateway, presenting the digits to 
						Cisco Unified Communications Manager exactly as configured on the handoff
						DN.

This method does not work
						for iPod Touch devices.

See the Enable Handoff from VoIP to Mobile Network topic.

Mobility Softkey

Cisco Unified Communications Manager calls the phone number of the PSTN
						mobile service provider for the mobile device.

See the Enable Transfer from VoIP to Mobile Network topic.

None of the above

Disable this feature if you do not want to make it available to
					 users.

Select Disabled for the Transfer to Mobile Network option in the Product Specific Configuration Layout section of the
						TCT device page.

Select Disabled for the Transfer to Mobile Network option in the Product Specific Configuration Layout section of the
						BOT device page.

- Enable Handoff from VoIP to Mobile Network

- Enable Transfer
	 from VoIP to Mobile Network

#### Enable Handoff from VoIP to Mobile Network

Set up a directory number that Cisco Unified Communications Manager can use to hand off active calls from VoIP to the mobile network. Match the user's caller ID with the Mobility Identity to ensure that Cisco Unified Communications Manager can recognize the user. Set up the TCT device and mobile device to support handoff from VoIP to the mobile network.

Set up a directory number that Cisco Unified Communications Manager can use to hand off active calls from VoIP to the mobile network. Match the user's caller ID with the Mobility Identity to ensure that Cisco Unified Communications Manager can recognize the user. Set up the BOT device and mobile device to support handoff from VoIP to the mobile network.

- Set Up Handoff DN

- Match Caller ID with Mobility Identity

- Set Up User and
	 Device Settings for Handoff

##### Set Up Handoff DN

Determine the required
		values. The values that you choose depend on the phone number that the gateway
		passes (for example, seven digits or ten digits).

The service provider must deliver the DID digits exactly as
				configured. Alternately, for Cisco IOS gateways with H.323 or SIP communication
				to Cisco Unified Communications Manager, you can use Cisco IOS to manipulate
				the inbound called-party number at the gateway, presenting the digits to Cisco Unified Communications Manager exactly as configured on the handoff number.

You cannot use translation patterns or other similar
				  manipulations within Cisco Unified Communications Manager to match the inbound
				  DID digits to the configured Handoff DN.

This partition should be present in the Remote Destination inbound
				Calling Search Space (CSS), which points to either the Inbound CSS of the Gateway or Trunk, or the Remote Destination CSS.

This feature does not use the remaining options on this page.

##### Match Caller ID with Mobility Identity

To ensure that only authorized phones can initiate outbound
		  calls, calls must originate from a phone that is set up in the system. To do
		  this, the system attempts to match the caller ID of the requesting phone number
		  with an existing Mobility Identity. By default, when a device initiates the
		  Handoff feature, the caller ID that is passed from the gateway to Cisco Unified Communications Manager must exactly match the Mobility Identity number that you
		  entered for that device.

However, your system may be set up such that these numbers
		  do not match exactly. For example, Mobility Identity numbers may include a
		  country code while caller ID does not. If so, you must set up the system to
		  recognize a partial match.

Be sure to account for situations in which the
		  same phone number may exist in different area codes or in different countries.
		  Also, be aware that service providers can identify calls with a variable number
		  of digits, which may affect partial matching. For example, local calls may be
		  identified using seven digits (such as 555 0123) while out-of-area calls may be
		  identified using ten digits (such as 408 555 0199).

Set up the Mobility Identity. See the Add Mobility Identity topic.

To determine whether you need
			 to complete this procedure, perform the following steps. Dial
				  in to the system from the mobile device and compare the caller ID value with the Destination Number in
				  the Mobility Identity. If the numbers do not match, you must perform this
				  procedure. Repeat this procedure for devices that are issued in all expected locales and
				  area codes.

##### Set Up User and
	 Device Settings for Handoff

Set up the
				user device on the 
				Cisco Unified Communications Manager.

Set up the
				user with a Mobility Identity.

Do not assign
				this method for iPod Touch devices. Use the Mobility Softkey method instead.

#### Enable Transfer
	 from VoIP to Mobile Network

- Select Device > Device
						Settings > Softkey Template .

- Select the
				  same softkey template that you selected when you configured the device for
				  Mobile Connect.

- In the Related Links drop-down list at the upper right,
				  select Configure Softkey Layout and select Go .

- In the
				  call state drop-down list, select the On Hook state and verify that the
				  Mobility key is in the list of selected softkeys.

- In the
				  call state drop-down list, select the Connected state and verify that the
				  Mobility key is in the list of selected softkeys.

- Select Device > Phone .

- Search for
				  the device that you want to configure.

- Select the
				  device name to open the Phone Configuration window.

If the device
				is an iPod Touch, you can configure a Mobility Identity using an alternate
				phone number such as the mobile phone of the user.

- Select the Owner User ID on the device page.

- Select the Mobility User ID . The value usually matches that of
				  the Owner User ID.

- In the
				  Product Specific Configuration Layout section, for the Transfer to Mobile
				  Network option, select Use Mobility Softkey or Use HandoffDN Feature .

Test your settings
		  by transferring an active call from VoIP to the mobile network.

## Cisco Jabber for iOS, Android and Windows

### Silent
	 Monitoring and Call Recording

Applies to: Cisco Jabber for Windows, Cisco Jabber for Android, Cisco Jabber for iOS

This feature is
		  supported for on-premises deployment and requires Cisco Unified Communications
		  Manager 8.6.

Cisco Jabber for
		  iPhone and iPad and Cisco Jabber for Android require Cisco Unified Communications Manager 11.0 or later.

You can set up
		  extra audio path functions for devices such as silent monitoring and call
		  recording.

To enable silent
		  monitoring and call recording, see the Monitoring
			 and Recording section of the Cisco Unified
			 Communications Manager Features and Services Guide for step-by-step
		  instructions.

Cisco Jabber
				does not provide any interface to begin silent monitoring or call recording.
				Use the appropriate software to silently monitor or record calls.

Cisco Jabber
				does not currently support monitoring notification tone or recording
				notification tone.

You can use
				silent monitoring and call recording functionality only. Cisco Jabber does not
				support other functionality such as barging or whisper coaching.

Open the Phone Configuration window for the device on which
					 you plan to enable silent monitoring and call recording.

Locate the Built In Bridge field.

If the Built In Bridge field is not available on the Phone Configuration window, download and
					 apply the most recent device packages.

### Hunt Group

Applies to: All clients

A Hunt Group is a group of lines that are organized hierarchically, so that if the first number in the hunt group list is busy, the system dials the second number. If the second number is busy, the system dials the next number, and so on. Every hunt group has a pilot number that is also called as hunt pilot. A hunt pilot contains a hunt pilot number and an associated hunt list. Hunt pilots provide flexibility in network design. They work with route filters and hunt lists to direct calls to specific devices and to include, exclude, or modify specific digit patterns.

A hunt pilot number is the number that a user dials. A hunt list contains a set of line groups in a specific order. A line group comprises a group of directory numbers in a specific order. The order controls the progress of the search for available directory numbers for incoming calls. A single-line group can appear in multiple hunt lists.

Cisco Unified Communications Manager identifies a call that is to be routed through a defined hunt list, Cisco Unified Communications Manager finds the first available device on the basis of the order of the line groups that a hunt list defines.

You can let a user log in to hunt groups by configuring EnableHuntGroup parameter. For more information, see the latest Parameters Reference Guide for Cisco Jabber .

Cisco Unified Communications Manager 9.x and later allows configuring of automatic log out of a hunt member when there is no answer. Once the user is logged out, the system displays a log out notification regardless of whether the user is auto logged out, manually logged out, or logged out by the Cisco Unified Communications Manager administrator.

Hunt group features supported by the Cisco Jabber clients:

Features

Mobile Clients

Desktop Clients

Log in to hunt group and log out of hunt group

Not supported

Supported

Call, answer, and decline

Supported

Supported

- Line Group

- Hunt List

- Hunt Pilot

#### Line Group

A line group allows you to designate the order in which directory
		  numbers are chosen. 
		  Cisco Unified Communications Manager
		  distributes a call to an idle or available member of a line group based on the
		  call distribution algorithm and on the Ring No Answer (RNA) Reversion timeout
		  setting.

Users cannot pick up calls to a DN that belongs to a line group by
		  using the directed call pickup feature.

- Configure Line
	 Group

##### Configure Line
	 Group

Configure directory numbers.

The Find
				  and List Line Groups window opens.

The Line
				  Group Configuration window opens.

Specify a
					 unique name in the Line Group Name field.

Specify
					 number of seconds for RNA Reversion Timeout .

Select a Distribution Algorithm to apply to the line group.

Select
						  a value for No Answer from the drop-down list.

Select Automatically Logout Hunt Member on No Answer to configure auto logout of the hunt list.

Select
						  a value for Busy from the drop-down list.

Select
						  a value for Not Available from the drop-down list.

Find
					 directory numbers or route partitions to add to the line group.

Reorder
					 the directory numbers or route partitions in the line group.

Remove
					 directory numbers or route partitions from the line group.

Configure a hunt
		  list and add the line group to the hunt list.

#### Hunt List

A hunt list contains a set of line groups in a specific order. A hunt
		  list associates with one or more hunt pilots and determines the order in which
		  those line groups are accessed. The order controls the progress of the search
		  for available directory numbers for incoming calls.

A hunt list comprises a collection of directory numbers as defined by
		  line groups. After 
		  Cisco Unified Communications Manager
		  determines a call that is to be routed through a defined hunt list, 
		  Cisco Unified Communications Manager
		  finds the first available device on the basis of the order of the line group(s)
		  that a hunt list defines.

A hunt list can contain only line groups. Each hunt list should have at least one line group. Each line group includes at least one directory number. A single line group can appear in multiple hunt lists.

The group call pickup feature and directed call pickup feature do not work with hunt lists.

- Configure Hunt
	 List

- Add Line Group to
	 Hunt List

##### Configure Hunt
	 List

The Find and Hunt List Groups window opens.

The Hunt List Configuration window opens.

Specify a unique name in the Name field.

Enter a description for the Hunt List.

Select a Cisco Unified Communications Manager
						Group from the drop-down list.

The system selects Enable this Hunt List by default for a
					 new hunt list when the hunt list is saved.

If this hunt list is to be used for voice mail, select For Voice Mail Usage .

Add line groups to the hunt list.

##### Add Line Group to
	 Hunt List

You must configure line groups and configure a hunt list.

The Find and Hunt List Groups window opens.

The Hunt List Detail Configuration window
				displays.

#### Hunt Pilot

A hunt pilot comprises a string of digits (an address) and a set of associated digit manipulations that route calls to a hunt list. Hunt pilots provide flexibility in network design. They work in conjunction with route filters and hunt lists to direct calls to specific devices and to include, exclude, or modify specific digit patterns. For more information about hunt pilots, see the System Configuration Guide for Cisco Unified Communications Manager .

For more detailed information on the configuration options for hunt pilots, see the relevant Cisco Unified Communications Manager documentation .

- Configure Hunt
	 Pilot

##### Configure Hunt
	 Pilot

The Find
				  and List Hunt Pilots window opens.

The Hunt
				  Pilot Configuration window opens.

## Cisco Jabber for iOS, Android and Mac

### Flexible DSCP
	 Values

Applies to: Cisco Jabber for Mac, Cisco Jabber for Android, Cisco Jabber for iOS

Flexible Differentiated
		Services Code Point (DSCP) allows you to specify different DSCP
		values to separate the audio and video streams on the network.

The EnableDSCPPacketMarking parameter is used to enable or disable DSCP packet marking in the client.

You can
		configure the DSCP values for audio calls, video calls, audio portion for video
		calls, and audio portion for telepresence calls separately. For better bandwidth management and to  protect audio
		stream degradation, separate the audio stream from the
		higher-bandwidth video stream. This can help when the network is congested or the call quality
		is impacted.

DSCP values are configured on Cisco Unified Communications Manager. For more information, see the Configure Flexible DSCP Marking and Video Promotion Policy section of the System Configuration Guide for Cisco Unified Communications Manager .

| Feature | Cisco
						Jabber for Windows | Cisco
						Jabber for Mac | Cisco
						Jabber for Android, Cisco Jabber for iPhone and iPad |
|---|---|---|---|
| Alert
						When Available | X |  |  |
| Automatic Upgrades | X | X | X |
| Auto-Save Chat | X |  |  |
| Bridge
						Escalations | X | X | X |
| Call
						Pickup | X |  |  |
| Call
						Park |  |  | X |
| Call
						Preservation | X | X | X |
| Chat
						Search | X |  |  |
| Chat
						Security Labels | X |  |  |
| Cisco
						WebEx Meetings integration | X | X | X |
| Custom
						Contact | X | X |  |
| Configure Silent Monitoring and Call Recording | X |  | X |
| Define a port range on the SIP profile | X | X | X |
| Dial
						via Office - Reverse |  |  | X |
| Directory Groups in Contact List | X | X | X |
| Expressway Mobile and Remote Access | X | X | X |
| Far
						End Camera Control | X | X | X |
| File
						Transfer | X | X | Some
						of the file transfer features are supported |
| FIPS
						Compliance | X |  |  |
| Flexible Jabber ID | X | X | X |
| Flexible DSCP |  | X | X |
| Group
						Chat | X | X | X |
| Hunt
						Group | X |  | X |
| Instant Messaging | X | X | X |
| Instant Messaging Encryption | X | X | X |
| Jabber
						to Jabber Call | X | X | X |
| Locations | X |  | X |
| Mandatory Upgrade Support | X | X | X |
| Multiple Resource Login | X | X | X |
| Persistent Chat Rooms | X | Some
						of the persistent chat room features are supported. |  |
| Predictive Contact Search | X | X | X |
| Presence | X | X | X |
| Save
						Chat History to Outlook Folder | X |  |  |
| Print
						Chat | X |  |  |
| Send
						to Mobile |  |  | X |
| Service Discovery | X | X | X |
| Single
						Sign-On | X | X | X |
| Spell
						Check | X
						(Client Options feature) | X (OS
						feature) |  |
| Telemetry | X | X | X |
| URI
						Dialing | X | X | X |
| Video
						Desktop Share (BFCP) | X | X | X
						(Mobile clients only support BFCP receiving.) |
| Voice
						and Video Calling | X | X | X |
| Voice
						and Video Encryption | X | X | X |
| Voicemail | X | X | X |

| Note | Jabber to Jabber calling is only supported
					 for users who authenticate to the Cisco WebEx Messenger service. For Cisco Jabber for Windows clients, we recommend running
					 Internet Explorer 10 or greater while using the Jabber to Jabber calling feature. Using the
					 feature with previous versions of Internet Explorer or with Internet Explorer
					 in Compatibility Mode can cause issues. These issues are with Cisco Jabber
					 client login (non-SSO setup) or Jabber to Jabber calling capability (SSO
					 setup). |
|---|---|

| Step 1 | Open a command
			 prompt in Windows. |
|---|---|
| Step 2 | Navigate to
			 the C:\Program Files(x86)\Cisco Systems\Cisco Jabber\ directory. |
| Step 3 | Enter the
			 command and your parameters. Example for desktop clients: CiscoJabberPrtDecrypter.exe --privatekey
				  C:\PRT\PrivateKey.pfx --password 12345 --encryptedfile C:\PRT\file.zip.enc
				  --encryptionkey C:\PRT\file.zip.esk --outputfile
				  C:\PRT\decryptedfile.zip Example for mobile clients: CiscoJabberPrtDecrypter.exe --privatekey
				  C:\PRT\PrivateKey.pfx --password 12345 --encryptedfile C:\PRT\file.zip.enc
				  --encryptionkey C:\PRT\file.zip.esk --outputfile C:\PRT\decryptedfile.zip
				  --mobile If the
				decryption is successful the output file is created. If there is an invalid
				parameter the decryption fails and an error is shown on the command line. |

| Step 1 | From Cisco
			 Unified CM Administration, choose System > Enterprise
				  Parameters . The Enterprise Parameters Configuration window appears. |
|---|---|
| Step 2 | In the User
				Management Parameters section, from the Directory Group Operations on Cisco IM and Presence drop-down list, select Enabled . |
| Step 3 | (Optional)
			 From the Syncing Mode for Enterprise Groups drop-down list,
			 choose one of the following: None —If you
				choose this option, the Cisco Intercluster Sync Agent service does not
				synchronize the enterprise groups and the group membership records between IM
				and Presence Service clusters. Differential
				  Sync —This is the default option. If you choose this option, after
				all the enterprise groups and group membership records from remote IM and
				Presence Service cluster are synchronized, the subsequent syncs synchronize
				only the records that were updated since the last sync occurred. Full Sync —If
				you choose this option, after all the enterprise groups and group membership
				records from the remote IM and Presence Service cluster are synchronized, all
				the records are synchronized during each subsequent sync. Note If the Cisco
				  Intercluster Sync Agent service is not running for more than 24 hours, we
				  recommend that you select the Full Sync option to ensure that the enterprise
				  groups and group membership records synchronize completely. After all the
				  records are synchronized, that is, when the Cisco Intercluster Sync Agent has
				  been running for about 30 minutes, choose the Differential Sync option for the subsequent syncs.
				  Keeping the value of this parameter set to 'Full Sync' for a longer period
				  could result in extensive CPU usage and therefore we recommend that you use the Full Sync option during off-business hours. | Note | If the Cisco
				  Intercluster Sync Agent service is not running for more than 24 hours, we
				  recommend that you select the Full Sync option to ensure that the enterprise
				  groups and group membership records synchronize completely. After all the
				  records are synchronized, that is, when the Cisco Intercluster Sync Agent has
				  been running for about 30 minutes, choose the Differential Sync option for the subsequent syncs.
				  Keeping the value of this parameter set to 'Full Sync' for a longer period
				  could result in extensive CPU usage and therefore we recommend that you use the Full Sync option during off-business hours. |
| Note | If the Cisco
				  Intercluster Sync Agent service is not running for more than 24 hours, we
				  recommend that you select the Full Sync option to ensure that the enterprise
				  groups and group membership records synchronize completely. After all the
				  records are synchronized, that is, when the Cisco Intercluster Sync Agent has
				  been running for about 30 minutes, choose the Differential Sync option for the subsequent syncs.
				  Keeping the value of this parameter set to 'Full Sync' for a longer period
				  could result in extensive CPU usage and therefore we recommend that you use the Full Sync option during off-business hours. |
| Step 4 | (Optional) Set
			 the LDAP
				Directory Synchronization Schedule parameters in the LDAP
				Directory Configuration window to configure the interval at which
			 Microsoft Active Directory groups are synchronized with Cisco Unified
			 Communications Manager. For more information, see the online help. |
| Step 5 | Click Save . |

| Note | If the Cisco
				  Intercluster Sync Agent service is not running for more than 24 hours, we
				  recommend that you select the Full Sync option to ensure that the enterprise
				  groups and group membership records synchronize completely. After all the
				  records are synchronized, that is, when the Cisco Intercluster Sync Agent has
				  been running for about 30 minutes, choose the Differential Sync option for the subsequent syncs.
				  Keeping the value of this parameter set to 'Full Sync' for a longer period
				  could result in extensive CPU usage and therefore we recommend that you use the Full Sync option during off-business hours. |
|---|---|

| Step 1 | Enable bridge
			 escalations in Cisco Jabber clients by setting the EnableBridgeConferencing parameter to true in the jabber-config.xml file. |
|---|---|
| Step 2 | (Optional)
			 Specify a mask for the room URI in the UserBridgeUriAdmin parameter in the jabber-config.xml file. If you don't specify a mask
			 the user can enter a DN or a SIP URI in the client. |
| Step 3 | Enable URI
			 dialing to allow your users enter a SIP URI for the conference call number. For
			 more information on URI dialing, see the URI
				Dialing topic. |

| Step 1 | Configure the Collaboration Meeting Room options using the configuration guides available here: https:/​/​www.cisco.com/​c/​en/​us/​support/​conferencing/​webex-meeting-center/​products-installation-and-configuration-guides-list.html |
|---|---|
| Step 2 | Ensure
			 Collaboration Meeting Rooms are enabled for your users on Cisco WebEx Meeting
			 Center. |
| Step 3 | Collaboration
			 Meeting Room features uses SIP URI, you must enable URI dialing for your users
			 on Cisco Unified Communications Manager. For more information on URI dialing,
			 see the URI
				Dialing topic. |

| Step 1 | Personal Rooms are enabled by default for users on Cisco WebEx Meeting Center. For more information see the Cisco WebEx Meeting Center documentation available here: https:/​/​www.cisco.com/​c/​en/​us/​support/​conferencing/​webex-meeting-center/​products-installation-and-configuration-guides-list.html |
|---|---|
| Step 2 | Users can
			 configure their personal rooms for all instant meetings by selecting Use
				Personal Room for all my instant meetings in Cisco WebEx Meeting
			 Center. |

| Note | When a user on a call using Cisco Jabber for iPhone and iPad
				switches from wi-fi to mobile data network or vice-versa, the interface IP
				address is lost and the call is preserved. When the user returns to the initial
				network and the IP address is restored, they can continue with the call. |
|---|---|

| Note | When searching for contacts in your organization, users can see the temporary availability status of all users in the organization. However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. |
|---|---|

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Presence > Settings . The Presence Settings window opens. |
| Step 3 | Select Allow users to view the availability of other users without being prompted for approval to disable prompts and automatically accept all presence subscription requests within your organization. This option has the following values: Selected—The client does not prompt users for presence subscription requests. The client automatically accepts all presence subscription requests without prompting the users. Cleared—The client prompts users to allow presence subscription requests. This setting requires users to allow other users in your organization to view their availability status. |
| Step 4 | Select Save . |

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Presence > Settings > Standard Configuration . |
| Step 3 | Uncheck Enable
				ad-hoc presence subscriptions and then select Save . Cisco Jabber does not display temporary presence.
				Users can see availability status only for contacts in their contact list. |

| Step 1 | Open the Cisco
				Unified Presence Administration interface. |
|---|---|
| Step 2 | Select Presence > Settings . |
| Step 3 | Uncheck Enable
				ad-hoc presence subscriptions and then select Save . Cisco Jabber does not display temporary presence.
				Users can see availability status only for contacts in their contact list. |

| Step 1 | Add devices. |
|---|---|
| Step 2 | Add directory numbers to the devices. |
| Step 3 | Associate users with the devices. |
| Step 4 | Specify primary extensions for users. |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
				  Routing > Directory Number . The Find
				  and List Directory Numbers window opens. |
| Step 3 | Find and
			 select the appropriate directory number. The Directory Number Configuration window opens. |
| Step 4 | Locate the Directory URIs section. |
| Step 5 | Specify a
			 valid SIP URI in the URI column. |
| Step 6 | Select the
			 appropriate partition from the Partition column. Note You cannot
					 manually add URIs to the system Directory URI partition. You should add the URI to
					 the same route partition as the directory number. | Note | You cannot
					 manually add URIs to the system Directory URI partition. You should add the URI to
					 the same route partition as the directory number. |
| Note | You cannot
					 manually add URIs to the system Directory URI partition. You should add the URI to
					 the same route partition as the directory number. |
| Step 7 | Add the
			 partition to the appropriate calling search space so that users can place calls
			 to the directory numbers. |
| Step 8 | Select Save . |

| Note | You cannot
					 manually add URIs to the system Directory URI partition. You should add the URI to
					 the same route partition as the directory number. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Enterprise Parameters . The Enterprise Parameters Configuration window opens. |
| Step 3 | Locate the End User Parameters section. |
| Step 4 | In the Directory URI Alias Partition row, select the appropriate partition from the drop-down list. |
| Step 5 | Click Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Device
				  Settings > SIP Profile . The Find
				  and List SIP Profiles window opens. |
| Step 3 | Find and
			 select the appropriate SIP profile. Remember: You cannot
					 edit the default SIP profile. If required, you should create a copy of the
					 default SIP profile that you can modify. |
| Step 4 | Select Use
				Fully Qualified Domain Name in SIP Requests and then select Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Service
				  Parameters . |
| Step 3 | In the Server drop-down list, select the active 
			 Cisco Unified Communications Manager. |
| Step 4 | In the Service drop-down list, select the Cisco
				Call Manager (Active) service. |
| Step 5 | Configure the
			 settings in the Clusterwide Parameters (System - Mobility Single Number Reach
				Voicemail) section. Note The settings
				  in this section are not specific to 
				  Cisco Jabber. For information about how to
				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
				  release. | Note | The settings
				  in this section are not specific to 
				  Cisco Jabber. For information about how to
				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
				  release. |
| Note | The settings
				  in this section are not specific to 
				  Cisco Jabber. For information about how to
				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
				  release. |
| Step 6 | Click Save . |

| Note | The settings
				  in this section are not specific to 
				  Cisco Jabber. For information about how to
				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
				  release. |
|---|---|

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
			 the device that you want to configure as follows: Select Device > Phone . Search for
				  the device that you want to configure. Select the
				  device name to open the Phone Configuration window. |
| Step 3 | In the Associated Mobility Identity section, click the link
			 for the Mobility Identity. Note To ensure
				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
				  that the end user enters in the 
				  Cisco Jabber client must match the Destination
				  Number that you enter on the Mobility Identity Configuration screen. | Note | To ensure
				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
				  that the end user enters in the 
				  Cisco Jabber client must match the Destination
				  Number that you enter on the Mobility Identity Configuration screen. |
| Note | To ensure
				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
				  that the end user enters in the 
				  Cisco Jabber client must match the Destination
				  Number that you enter on the Mobility Identity Configuration screen. |
| Step 4 | Set the
			 policies as follows: Cisco Unified Communications Manager  release 9 
				   — In the Single Number Reach Voicemail Policy drop-down list,
					 select User Control . Cisco Unified Communications Manager release 10 without Dial via Office 
				   — In the Single Number Reach Voicemail Policy drop-down list,
					 select User Control . Cisco Unified Communications Manager release 10 with Dial via Office In the Single Number Reach Voicemail Policy drop-down list,
						  select Timer Control . In the Dial-via-Office Reverse Voicemail Policy drop-down
						  list, select User Control . |
| Step 5 | Click Save . |

| Note | To ensure
				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
				  that the end user enters in the 
				  Cisco Jabber client must match the Destination
				  Number that you enter on the Mobility Identity Configuration screen. |
|---|---|

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
			 the device that you want to configure as follows: Select Device > Phone . Search for
				  the device that you want to configure. Select the
				  device name to open the Phone Configuration window. |
| Step 3 | In the Associated Remote Destinations section, click the
			 link for the associated remote destination. |
| Step 4 | Set the
			 policies as follows: Cisco Unified Communications Manager
					 release 9
				   — In the Single Number Reach Voicemail Policy drop-down list, select User Control . Cisco Unified Communications Manager
					 release 10 without Dial via Office
				  — In the Single Number Reach Voicemail Policy drop-down list, select User Control . Cisco Unified Communications Manager
					 release 10 with Dial via Office In the Single Number Reach Voicemail Policy drop-down list, select Timer Control . In the Dial-via-Office Reverse Voicemail
							 Policy drop-down list, select User Control . |
| Step 5 | Click Save . |

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select System > Service
				  Parameters . |
| Step 3 | Select the
			 appropriate server from the Server drop-down list. |
| Step 4 | Select Cisco
				XCP Router from the Service drop-down list. The Service Parameter Configuration window opens. |
| Step 5 | Locate the Enable
				file transfer parameter. |
| Step 6 | Select the
			 appropriate value from the Parameter Value drop-down list. Remember: If you
					 disable the setting on Cisco Unified Communications Manager IM and Presence
					 Service, you must also disable file transfers and screen captures in the client
					 configuration. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > File
				  Transfer . |
| Step 3 | In the File
				Transfer Configuration section select Managed File Transfer . |
| Step 4 | In the Managed File Transfer Assignment section, assign the
			 external database and the external file server for each node in the cluster. |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > File Transfer . |
| Step 3 | In the File Transfer Configuration section, select Peer-to-Peer . |
| Step 4 | Select Save . |

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > File
				  Transfer . |
| Step 3 | In the Managed File Transfer Configuration section enter
			 the amount for the Maximum File Size . |
| Step 4 | Select Save . |

| Step 1 | Open the Cisco
				Unified Communication Manager interface. |
|---|---|
| Step 2 | Select Call
				  Routing > Call Pickup Group The Find
				  and List Call Pickup Groups window opens. |
| Step 3 | Select Add
				New The Call
				  Pickup Group Configuration window opens. |
| Step 4 | Enter call
			 pickup group information: Specify a
				  unique name for the call pickup group. Specify a
				  unique directory number for the call pickup group number. Enter a
				  description. Select a
				  partition. |
| Step 5 | (Optional) Configure the
			 audio or visual notification in the Call
				Pickup Group Notification Settings section. Select the
				  notification policy. Specify
				  the notification timer. For further
				information on call pickup group notification settings see the call pickup
				topics in the relevant Cisco Unified Communications Manager documentation. |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified Communications Manager
				Administration interface. |
|---|---|
| Step 2 | Assign a call pickup group to a directory number using one of the
			 following methods: Select Call
						  Routing > Directory Number , find
					 and select your directory number and in the 
					 Call Forward and Call Pickup Settings
					 area select the call pickup group from the call pickup group drop down list. Select Device > Phone ,
					 find and select your phone and in the Association Information list choose the directory number to which the call
					 pickup group will be assigned. |
| Step 3 | To save the changes in the database, select Save . |

| Step 1 | Open the Cisco
				Unified Communication Manager Administration interface. |
|---|---|
| Step 2 | Select Call
				  Routing > Call Pickup Group The Find
				  and List Call Pickup Groups window opens. |
| Step 3 | Select your
			 call pickup group. The Call
				  Pickup Group Configuration window opens. |
| Step 4 | In the Associated Call Pickup Group Information section,
			 you can do the following: Find call
					 pickup groups and add to current associated call pickup groups. Reorder
					 associated call pickup groups or remove call pickup groups. |
| Step 5 | Select Save . |

| Step 1 | Configure call
			 pickup groups and add associated groups. The associated groups list can include
			 up to 10 groups. For more
				information, see topics related to defining a pickup group for Other Group
				Pickup. |
|---|---|
| Step 2 | Enable the
			 Auto Call Pickup Enabled service parameter to automatically answer calls for
			 directed call pickups. For more
				information, see topics related to configuring Auto Call Pickup. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Service
				  Parameters |
| Step 3 | Select your server from the Server drop down list and then select
			 the Cisco Call Manager service from the Service
			 drop down list. |
| Step 4 | In the Clusterwide Parameters (Feature - Call Pickup) section, select one of the following for Auto Call Pickup Enabled : true—The auto call pickup feature is enabled. false—The auto call pickup feature is not enabled. This is the
						default value. |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > Group Chat and Persistent
				  Chat . |
| Step 3 | Select Enable
				Persistent Chat . |
| Step 4 | Ensure the
			 settings How
				many users can be in a room at one time and How
				many hidden users can be in a room at one time under the Occupancy Settings section contain the same,
			 non-zero value. |
| Step 5 | Configure the remaining settings as appropriate for your persistent chat deployment. We recommend the persistent chat settings in the following table. Persistent Chat Setting Recommended Value Notes System automatically manages primary group chat server aliases Disabled Enable persistent chat Enabled Archive all room joins and exits Administrator Defined This value is not currently used by for persistent chat. Archive all room messages Enabled Allow only group chat system administrators to create persistent chat rooms Administrator Defined Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment. Maximum number of persistent chat rooms allowed Administrator Defined Number of connections to the database Default Value Database connection heartbeat interval (seconds) Default Value Timeout value for persistent chat rooms (minutes) Default Value Maximum number of rooms allowed Default Value Rooms are for members only by default Disabled Room owners can change whether or not rooms are for members only Enabled Cisco Jabber requires this value to be Enabled. Only moderators can invite people to members-only rooms Enabled Cisco Jabber requires this value to be Enabled. Room owners can change whether or not only moderators can invite people to members-only rooms Enabled Users can add themselves to rooms as members Disabled This value is not currently used by Cisco Jabber for persistent chat. Room owners can change whether users can add themselves to rooms as members Disabled This value is not currently used by Cisco Jabber for persistent chat. Members and administrators who are not in a room are still visible in the room Enabled Cisco Jabber requires this value to be Enabled. Room owners can change whether members and administrators who are not in a room are still visible in the room Enabled Rooms are backwards-compatible with older clients Disabled This value is not currently used by Cisco Jabber for persistent chat. Room owners can change whether rooms are backwards-compatible with older clients Disabled This value is not currently used by Cisco Jabber for persistent chat. Rooms are anonymous by default Disabled This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. Room owners can change whether or not rooms are anonymous Disabled This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. Lowest participation level a user can have to invite others to the room Default Value This value is not currently used by Cisco Jabber for persistent chat. Room owners can change the lowest participation level a user can have to invite others to the room Disabled This value is not currently used by Cisco Jabber for persistent chat. How many users can be in a room at one time Administrator Defined Cisco recommends using the default value. How many hidden users can be in a room at one time Administrator Defined Default maximum occupancy for a room Default Value Room owners can change default maximum occupancy for a room Default Value Lowest participation level a user can have to send a private message from within the room Default Value Room owners can change the lowest participation level a user can have to send a private message from within the room Default Value Lowest participation level a user can have to change a room's subject Moderator Room owners can change the lowest participation level a user can have to change a room's subject Disabled Remove all XHTML formatting from messages Disabled This value is not currently used by Cisco Jabber for persistent chat. Room owners can change XHTML formatting setting Disabled This value is not currently used by Cisco Jabber for persistent chat. Rooms are moderated by default Disabled This value is not currently used by Cisco Jabber for persistent chat. Room owners can change whether rooms are moderated by default Default Value This value is not currently used by Cisco Jabber for persistent chat. Maximum number of messages that can be retrieved from the archive Default Value Number of messages in chat history displayed by default Administrator Defined Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue to use their originally configured value. Room owners can change the number of messages displayed in chat history Default Value This value is not currently used by Cisco Jabber for persistent chat. Note Persistent Chat rooms inherit their settings at the time of creation. Values changed after a room is created only apply to rooms created after the change has taken effect. | Persistent Chat Setting | Recommended Value | Notes | System automatically manages primary group chat server aliases | Disabled |  | Enable persistent chat | Enabled |  | Archive all room joins and exits | Administrator Defined | This value is not currently used by for persistent chat. | Archive all room messages | Enabled |  | Allow only group chat system administrators to create persistent chat rooms | Administrator Defined | Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment. | Maximum number of persistent chat rooms allowed | Administrator Defined |  | Number of connections to the database | Default Value |  | Database connection heartbeat interval (seconds) | Default Value |  | Timeout value for persistent chat rooms (minutes) | Default Value |  | Maximum number of rooms allowed | Default Value |  | Rooms are for members only by default | Disabled |  | Room owners can change whether or not rooms are for members only | Enabled | Cisco Jabber requires this value to be Enabled. | Only moderators can invite people to members-only rooms | Enabled | Cisco Jabber requires this value to be Enabled. | Room owners can change whether or not only moderators can invite people to members-only rooms | Enabled |  | Users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change whether users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Members and administrators who are not in a room are still visible in the room | Enabled | Cisco Jabber requires this value to be Enabled. | Room owners can change whether members and administrators who are not in a room are still visible in the room | Enabled |  | Rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change whether rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Rooms are anonymous by default | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. | Room owners can change whether or not rooms are anonymous | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. | Lowest participation level a user can have to invite others to the room | Default Value | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change the lowest participation level a user can have to invite others to the room | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | How many users can be in a room at one time | Administrator Defined | Cisco recommends using the default value. | How many hidden users can be in a room at one time | Administrator Defined |  | Default maximum occupancy for a room | Default Value |  | Room owners can change default maximum occupancy for a room | Default Value |  | Lowest participation level a user can have to send a private message from within the room | Default Value |  | Room owners can change the lowest participation level a user can have to send a private message from within the room | Default Value |  | Lowest participation level a user can have to change a room's subject | Moderator |  | Room owners can change the lowest participation level a user can have to change a room's subject | Disabled |  | Remove all XHTML formatting from messages | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change XHTML formatting setting | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Rooms are moderated by default | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change whether rooms are moderated by default | Default Value | This value is not currently used by Cisco Jabber for persistent chat. | Maximum number of messages that can be retrieved from the archive | Default Value |  | Number of messages in chat history displayed by default | Administrator Defined | Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue to use their originally configured value. | Room owners can change the number of messages displayed in chat history | Default Value | This value is not currently used by Cisco Jabber for persistent chat. | Note | Persistent Chat rooms inherit their settings at the time of creation. Values changed after a room is created only apply to rooms created after the change has taken effect. |
| Persistent Chat Setting | Recommended Value | Notes |
| System automatically manages primary group chat server aliases | Disabled |  |
| Enable persistent chat | Enabled |  |
| Archive all room joins and exits | Administrator Defined | This value is not currently used by for persistent chat. |
| Archive all room messages | Enabled |  |
| Allow only group chat system administrators to create persistent chat rooms | Administrator Defined | Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment. |
| Maximum number of persistent chat rooms allowed | Administrator Defined |  |
| Number of connections to the database | Default Value |  |
| Database connection heartbeat interval (seconds) | Default Value |  |
| Timeout value for persistent chat rooms (minutes) | Default Value |  |
| Maximum number of rooms allowed | Default Value |  |
| Rooms are for members only by default | Disabled |  |
| Room owners can change whether or not rooms are for members only | Enabled | Cisco Jabber requires this value to be Enabled. |
| Only moderators can invite people to members-only rooms | Enabled | Cisco Jabber requires this value to be Enabled. |
| Room owners can change whether or not only moderators can invite people to members-only rooms | Enabled |  |
| Users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Members and administrators who are not in a room are still visible in the room | Enabled | Cisco Jabber requires this value to be Enabled. |
| Room owners can change whether members and administrators who are not in a room are still visible in the room | Enabled |  |
| Rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Rooms are anonymous by default | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. |
| Room owners can change whether or not rooms are anonymous | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. |
| Lowest participation level a user can have to invite others to the room | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change the lowest participation level a user can have to invite others to the room | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| How many users can be in a room at one time | Administrator Defined | Cisco recommends using the default value. |
| How many hidden users can be in a room at one time | Administrator Defined |  |
| Default maximum occupancy for a room | Default Value |  |
| Room owners can change default maximum occupancy for a room | Default Value |  |
| Lowest participation level a user can have to send a private message from within the room | Default Value |  |
| Room owners can change the lowest participation level a user can have to send a private message from within the room | Default Value |  |
| Lowest participation level a user can have to change a room's subject | Moderator |  |
| Room owners can change the lowest participation level a user can have to change a room's subject | Disabled |  |
| Remove all XHTML formatting from messages | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change XHTML formatting setting | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Rooms are moderated by default | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether rooms are moderated by default | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Maximum number of messages that can be retrieved from the archive | Default Value |  |
| Number of messages in chat history displayed by default | Administrator Defined | Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue to use their originally configured value. |
| Room owners can change the number of messages displayed in chat history | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Note | Persistent Chat rooms inherit their settings at the time of creation. Values changed after a room is created only apply to rooms created after the change has taken effect. |

| Persistent Chat Setting | Recommended Value | Notes |
|---|---|---|
| System automatically manages primary group chat server aliases | Disabled |  |
| Enable persistent chat | Enabled |  |
| Archive all room joins and exits | Administrator Defined | This value is not currently used by for persistent chat. |
| Archive all room messages | Enabled |  |
| Allow only group chat system administrators to create persistent chat rooms | Administrator Defined | Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment. |
| Maximum number of persistent chat rooms allowed | Administrator Defined |  |
| Number of connections to the database | Default Value |  |
| Database connection heartbeat interval (seconds) | Default Value |  |
| Timeout value for persistent chat rooms (minutes) | Default Value |  |
| Maximum number of rooms allowed | Default Value |  |
| Rooms are for members only by default | Disabled |  |
| Room owners can change whether or not rooms are for members only | Enabled | Cisco Jabber requires this value to be Enabled. |
| Only moderators can invite people to members-only rooms | Enabled | Cisco Jabber requires this value to be Enabled. |
| Room owners can change whether or not only moderators can invite people to members-only rooms | Enabled |  |
| Users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Members and administrators who are not in a room are still visible in the room | Enabled | Cisco Jabber requires this value to be Enabled. |
| Room owners can change whether members and administrators who are not in a room are still visible in the room | Enabled |  |
| Rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Rooms are anonymous by default | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. |
| Room owners can change whether or not rooms are anonymous | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. |
| Lowest participation level a user can have to invite others to the room | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change the lowest participation level a user can have to invite others to the room | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| How many users can be in a room at one time | Administrator Defined | Cisco recommends using the default value. |
| How many hidden users can be in a room at one time | Administrator Defined |  |
| Default maximum occupancy for a room | Default Value |  |
| Room owners can change default maximum occupancy for a room | Default Value |  |
| Lowest participation level a user can have to send a private message from within the room | Default Value |  |
| Room owners can change the lowest participation level a user can have to send a private message from within the room | Default Value |  |
| Lowest participation level a user can have to change a room's subject | Moderator |  |
| Room owners can change the lowest participation level a user can have to change a room's subject | Disabled |  |
| Remove all XHTML formatting from messages | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change XHTML formatting setting | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Rooms are moderated by default | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether rooms are moderated by default | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Maximum number of messages that can be retrieved from the archive | Default Value |  |
| Number of messages in chat history displayed by default | Administrator Defined | Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue to use their originally configured value. |
| Room owners can change the number of messages displayed in chat history | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |

| Note | Persistent Chat rooms inherit their settings at the time of creation. Values changed after a room is created only apply to rooms created after the change has taken effect. |
|---|---|

| Note | Persistent Chat Rooms and their administration is for
					 on-premises deployments only. Persistent Chat Rooms are not available for mobile clients. |
|---|---|

| Step 1 | To set a password for a room,
			 from the Chat Rooms tab on the hub window, select All rooms > New
				  room > Password . |
|---|---|
| Step 2 | To change the password for a room, open the chat room, click
			 on Edit Room , select Password , then edit and save the password. |

| Note | Internet
			 Explorer 9 users in Cloud-based deployments that use Single Sign On (SSO) get
			 security alerts when they sign in to Cisco Jabber for Windows . Add webexconnect.com to the list of websites in the Compatibility View Settings window of Internet
			 Explorer 9 to stop these alerts. |
|---|---|

| Step 1 | Open the email
			 account settings in 
			 Microsoft Outlook, as in the following example: Select File > Account
						Settings . Select the Email tab on the Account Settings window. |
|---|---|
| Step 2 | Double-click
			 the server name. In most cases,
				the server name is Microsoft Exchange . |
| Step 3 | Select the Use
				Cached Exchange Mode checkbox. |
| Step 4 | Apply the
			 setting and then restart 
			 Microsoft Outlook. |

| Step 1 | Start the Active Directory User and Computers administrative tool. You must have administrator permissions to run the Active Directory User and Computers administrative tool. |
|---|---|
| Step 2 | Select View in the menu bar and then select the Advanced Features option from the drop-down list. |
| Step 3 | Navigate to the appropriate user in the Active Directory User and Computers administrative tool. |
| Step 4 | Double click the user to open the Properties dialog box. |
| Step 5 | Select the Attribute Editor tab. |
| Step 6 | Locate and select the proxyAddresses attribute in the Attributes list box. |
| Step 7 | Select Edit to open the Multi-valued String Editor dialog box. |
| Step 8 | In the Value to add text box, specify the following value: SIP:user@cupdomain . For example, SIP:msmith@cisco.com . Where the user@cupdomain value is the user's instant messaging address. cupdomain corresponds to the domain for Cisco Unified Presence or Cisco Unified Communications Manager IM and Presence Service . |

| Version
						of Cisco Jabber for Windows | Supported Servers |
|---|---|
| 10.6 | Microsoft Exchange 2013 Microsoft Exchange 2010 |
| 11.0 | Microsoft Office 365 Microsoft Exchange 2013 Microsoft Exchange 2010 |

| Note | Do not use this authentication method if some users share the same Windows account. The client authenticates with the account on the Operating System, and not with the user who is logged in to Cisco Jabber. For example, User A logs onto a Windows machine and then logs into Cisco Jabber for a morning shift. When the shift is done, Jabber is reset and User B logs into the client for the afternoon shift. Because User A is logged into the Windows account, then the chat messages from User B are saved in the Outlook account for User A. |
|---|---|

| In the jabber-config.xml file, set the ExchangeAuthenticateWithSystemAccount parameter to true . |
|---|

| Step 1 | In the jabber-config.xml file, configure the Exchange_UseCredentialsFrom parameter. |
|---|---|
| Step 2 | Define the value of the parameter as the service that you want
			 used to sync credentials. For example, <Exchange_UseCredentialsFrom>CUCM</Exchange_UseCredentialsFrom> . In this example, Cisco Unified Communications Manager is
			 defined as the service which provides the Exchange server with credentials for
			 authentication. |

| Step 1 | In the jabber-config.xml file, configure the ExchangeAutodiscoverDomain parameter. |
|---|---|
| Step 2 | Define the
			 value of the parameter as the domain to discover the Exchange server. The
			 client uses the domain to search for the Exchange server at one of the
			 following Web addresses: https://< domain >/autodiscover/autodiscover.svc https://autodiscover.< domain >/autodiscover/autodiscover.svc |

| Step 1 | In
			 the jabber-config.xml file, configure the InternalExchangeServer and ExternalExchangeServer parameters. |
|---|---|
| Step 2 | Define the
			 value of the parameters using the Exchange server addresses. |

| Note | In order for users to be able to successfully add IBM Notes contacts to their contact lists, the Messaging ID field in IBM Notes must contain a valid value. |
|---|---|

| Note | To achieve
				optimal results, your custom emoticons should conform to the following
				guidelines: Dimensions: 17 x 17 pixels Transparent background PNG file
					 format RGB colors |
|---|---|

| Step 1 | Create a file
			 named emoticonDefs.xml with any text editor. |
|---|---|
| Step 2 | Specify the
			 emoticon definitions as appropriate in emoticonDefs.xml . See Emoticon
				  Definitions for more information on the structure and available
				parameters for emoticonDefs.xml . |
| Step 3 | Save and close emoticonDefs.xml . |
| Step 4 | Save emoticonDefs.xml in the appropriate directory on the
			 file system. Cisco Jabber for Windows loads emoticon definitions from the
				following directories on the file system. The directory can differ depending on your
				  operating system For 32-bit operating systems: Program Files\Cisco Systems\Cisco
								  Jabber\Emoticons Program Files\Cisco Systems\Cisco
								  Jabber\CustomEmoticons For 64-bit operating systems: Program Files(x86)\Cisco Systems\Cisco
								  Jabber\Emoticons Program Files(x86)\Cisco Systems\Cisco
								  Jabber\CustomEmoticons The Emoticons folder contains the default
					 emoticons for Cisco Jabber for Windows and the default emoticonDefs.xml . The CustomEmoticons folder does not exist by
					 default. Administrators can create this folder to contain custom emoticon
					 definitions to include in organizational deployments. Emoticons
					 that you define in the CustomEmoticons folder take precedence over emoticon
					 definitions in the default Emoticons folder. %USERPROFILE% \AppData\Roaming\Cisco\Unified
						Communications\Jabber\CSF\CustomEmoticons This
					 folder contains custom emoticon definitions for individual instances of Cisco
					 Jabber for Windows. Emoticons
					 that you define in this directory take precedence over emoticon definitions in
					 the CustomEmoticons folder in the installation directory. |
| Step 5 | Restart Cisco
			 Jabber for Windows. |

| Element or attribute | Description |
|---|---|
| emoticons | This element contains all emoticon definitions. |
| emoticon | This element contains the definition of an emoticon. |
| defaultKey | This attribute defines the default key combination that renders the emoticon. Specify any key combination as the value. This attribute is required. defaultKey is an attribute of the emoticon element. |
| image | This attribute specifies the filename of the emoticon image. Specify the filename of the emoticon as the value. The emoticon image must exist in the same directory as emoticonDefs.xml . This attribute is required. Cisco Jabber for Windows supports any icon that Internet Explorer can render, including .jpeg , .png ,  and .gif . image is an attribute of the emoticon element. |
| text | This attribute defines the descriptive text that displays in the Insert emoticon dialog box. Specify any string of unicode characters. This attribute is optional. text is an attribute of the emoticon element. |
| order | This attribute defines the order in which emoticons display in the Insert emoticon dialog box. Specify an ordinal number beginning from 1 as the value. order is an attribute of the emoticon element. This attribute is required. However, if the value of hidden is true this parameter does not take effect. |
| hidden | This attribute specifies whether the emoticon displays in the Insert emoticon dialog box. Specify one of the following as the value: true Specifies the emoticon does not display in the Insert emoticon dialog box. Users must enter the key combination to render the emoticon. false Specifies the emoticon displays in the Insert emoticon dialog box. Users can select the emoticon from the Insert emoticon dialog box or enter the key combination to render the emoticon. This is the default value. This attribute is optional. hidden is an attribute of the emoticon element. |
| alt | This element enables you to map key combinations to emoticons. Specify any key combination as the value. For example, if the value of defaultKey is :) , you can specify :-) as the value of alt so that both key combinations render the same emoticon. This element is optional. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure cluster wide call park | [Optional]
			  Configure call park for the entire cluster, or use the procedure in Step 3 to configure call park on individual nodes within the cluster. |
| Step 2 | Configure a partition | Create a partition to add a call park number. |
| Step 3 | Configure a call park number | Configure a
			 call park number 
		  to use call park across nodes in a cluster. You can define
		either a single directory number or a range of directory numbers for use as
		call park extension numbers. You can park only one call at each call park
		extension number. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call Routing > Mobility > Enterprise Feature Access Number Configuration . |
| Step 3 | Select Add New . |
| Step 4 | In the Number field, enter the Enterprise Feature Access number. Enter a DID number that is unique in the system. To support dialing internationally, you can prepend this number with \+. |
| Step 5 | From the Route Partition drop-down list, choose the partition of the DID that
is required for enterprise feature access. This partition is set under System > Service Parameters , in the Clusterwide Parameters (System - Mobility) section,  in the Inbound Calling Search Space for Remote Destination setting. This setting points either to the Inbound Calling Search Space of the Gateway or Trunk, or to the Calling Search Space assigned on the Phone Configuration window for the device. If the user sets up the DvO Callback Number with an alternate number, ensure that you set up the trunk Calling Search Space (CSS) to route to destination of the alternate phone number. |
| Step 6 | In the Description field, enter a description of the Mobility Enterprise Feature Access
number. |
| Step 7 | (Optional) Check the Default Enterprise Feature Access Number check box if you want to make this Enterprise Feature Access number the default for this system. |
| Step 8 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call Routing > Mobility > Mobility Profile . |
| Step 3 | In the Mobility Profile Information section, in the Name field, enter a descriptive name for the mobility profile. |
| Step 4 | In the Dial via Office-Reverse Callback section, in the Callback Caller ID field, enter the caller ID for the callback call that the client receives from Cisco Unified Communications Manager. |
| Step 5 | Click Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . |
| Step 3 | Click Add
				New . |
| Step 4 | From the Phone
			 Type drop-down list, choose Cisco
				Dual Mode for iPhone . |
| Step 5 | From the Phone
			 Type drop-down list, choose Cisco
				Dual Mode for Android . |
| Step 6 | Click Next . |
| Step 7 | Scroll down to
			 the Product Specific Configuration Layout section, and verify that you can see
			 the Video Capabilities drop-down list. If you can see
				the Video Capabilities drop-down list, the COP file is already installed on
				your system. If you cannot
				see the Video Capabilities drop-down list, locate and download the correct COP
				file. |

| Connection | Calling
				Options |
|---|---|
| Voice over
				IP | Mobile Voice
				Network | Autoselect |
| Corporate
				Wi-Fi | Outgoing:
				VoIP | Incoming:
				VoIP | Outgoing:
				DvO-R | Incoming:
				Mobile Connect | Outgoing:
				VoIP | Incoming:
				VoIP |
| Noncorporate
				Wi-Fi |
| Mobile
				Network (3G, 4G) | Outgoing:
				DvO-R | Incoming: Mobile Connect |
| Phone
				Services are not registered | Outgoing Native Cellular
			 Call |
| Incoming Mobile Connect |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
			 the device that you want to configure as follows: Select Device > Phone . Search
				  for the device that you want to configure. Select
				  the device name to open the Phone Configuration window. |
| Step 3 | In the Associated Mobility Identity section, select Add a
				New Mobility Identity . |
| Step 4 | Enter the
			 mobile phone number as the destination number. You must be able to rout this number to an outbound gateway. Generally, the number is the full
				E.164 number. Note If you
				  enable the Dial via Office — Reverse feature for a user, you must enter a
				  destination number for the user's mobility identity. If you
				  enable Dial via Office — Reverse and leave the destination number empty in the
				  mobility identity: The
						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
						network and VPN. The
						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
						network. The
						logs do not indicate why the phone service cannot connect. | Note | If you
				  enable the Dial via Office — Reverse feature for a user, you must enter a
				  destination number for the user's mobility identity. If you
				  enable Dial via Office — Reverse and leave the destination number empty in the
				  mobility identity: The
						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
						network and VPN. The
						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
						network. The
						logs do not indicate why the phone service cannot connect. |
| Note | If you
				  enable the Dial via Office — Reverse feature for a user, you must enter a
				  destination number for the user's mobility identity. If you
				  enable Dial via Office — Reverse and leave the destination number empty in the
				  mobility identity: The
						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
						network and VPN. The
						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
						network. The
						logs do not indicate why the phone service cannot connect. |
| Step 5 | Enter the
			 initial values for call timers. These values
				ensure that calls are not routed to the mobile service provider voicemail
				before they ring in the client on the mobile device. You can adjust these
				values to work with the end user's mobile network. For more information, see
				the online help in Cisco Unified Communications Manager. The following is an example of mobility Identity timers'
				  information in Cisco Unified Communications Manager 9.x. Setting Suggested Initial Value Answer Too Soon Timer 3000 Answer Too Late Timer 20000 Delay Before Ringing Timer 0 Note This setting does not apply to DvO-R calls. The following is an example of mobility Identity timers'
				  information in Cisco Unified Communications Manager 10.x. Setting Suggested Initial Value Wait * before ringing this phone when my business line
							 is dialed.* 0.0 seconds Prevent this call from going straight to this phone's
							 voicemail by using a time delay of * to detect when calls go straight to
							 voicemail.* 3.0 seconds Stop ringing this phone after * to avoid connecting to
							 this phone's voicemail.* 20.0 seconds | Setting | Suggested Initial Value | Answer Too Soon Timer | 3000 | Answer Too Late Timer | 20000 | Delay Before Ringing Timer | 0 Note This setting does not apply to DvO-R calls. | Note | This setting does not apply to DvO-R calls. | Setting | Suggested Initial Value | Wait * before ringing this phone when my business line
							 is dialed.* | 0.0 seconds | Prevent this call from going straight to this phone's
							 voicemail by using a time delay of * to detect when calls go straight to
							 voicemail.* | 3.0 seconds | Stop ringing this phone after * to avoid connecting to
							 this phone's voicemail.* | 20.0 seconds |
| Setting | Suggested Initial Value |
| Answer Too Soon Timer | 3000 |
| Answer Too Late Timer | 20000 |
| Delay Before Ringing Timer | 0 Note This setting does not apply to DvO-R calls. | Note | This setting does not apply to DvO-R calls. |
| Note | This setting does not apply to DvO-R calls. |
| Setting | Suggested Initial Value |
| Wait * before ringing this phone when my business line
							 is dialed.* | 0.0 seconds |
| Prevent this call from going straight to this phone's
							 voicemail by using a time delay of * to detect when calls go straight to
							 voicemail.* | 3.0 seconds |
| Stop ringing this phone after * to avoid connecting to
							 this phone's voicemail.* | 20.0 seconds |
| Step 6 | Do one of the
			 following: Cisco Unified
				Communications Manager release 9 or earlier —  Check the Enable Mobile Connect check box. Cisco Unified
				Communications Manager release 10 —  Check the Enable Single Number Reach check box. |
| Step 7 | If you are
			 setting up the Dial via Office feature, in the Mobility Profile drop-down list,
			 select one of the following options. Option Description Leave
				  blank Choose
					 this option if you want users to use the Enterprise Feature Access Number
					 (EFAN). Mobility
				  Profile Choose the
					 mobility profile that you just created if you want users to use a mobility
					 profile instead of an EFAN. | Option | Description | Leave
				  blank | Choose
					 this option if you want users to use the Enterprise Feature Access Number
					 (EFAN). | Mobility
				  Profile | Choose the
					 mobility profile that you just created if you want users to use a mobility
					 profile instead of an EFAN. |
| Option | Description |
| Leave
				  blank | Choose
					 this option if you want users to use the Enterprise Feature Access Number
					 (EFAN). |
| Mobility
				  Profile | Choose the
					 mobility profile that you just created if you want users to use a mobility
					 profile instead of an EFAN. |
| Step 8 | Set up the
			 schedule for routing calls to the mobile number. |
| Step 9 | Select Save . |

| Note | If you
				  enable the Dial via Office — Reverse feature for a user, you must enter a
				  destination number for the user's mobility identity. If you
				  enable Dial via Office — Reverse and leave the destination number empty in the
				  mobility identity: The
						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
						network and VPN. The
						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
						network. The
						logs do not indicate why the phone service cannot connect. |
|---|---|

| Setting | Suggested Initial Value |
|---|---|
| Answer Too Soon Timer | 3000 |
| Answer Too Late Timer | 20000 |
| Delay Before Ringing Timer | 0 Note This setting does not apply to DvO-R calls. | Note | This setting does not apply to DvO-R calls. |
| Note | This setting does not apply to DvO-R calls. |

| Note | This setting does not apply to DvO-R calls. |
|---|---|

| Setting | Suggested Initial Value |
|---|---|
| Wait * before ringing this phone when my business line
							 is dialed.* | 0.0 seconds |
| Prevent this call from going straight to this phone's
							 voicemail by using a time delay of * to detect when calls go straight to
							 voicemail.* | 3.0 seconds |
| Stop ringing this phone after * to avoid connecting to
							 this phone's voicemail.* | 20.0 seconds |

| Option | Description |
|---|---|
| Leave
				  blank | Choose
					 this option if you want users to use the Enterprise Feature Access Number
					 (EFAN). |
| Mobility
				  Profile | Choose the
					 mobility profile that you just created if you want users to use a mobility
					 profile instead of an EFAN. |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
			 the device that you want to configure as follows: Select Device > Phone . Search for
				  the device that you want to configure. Select the
				  device name to open the Phone Configuration window. |
| Step 3 | In the Device
			 Information section, check the 
			 Enable
				Cisco Unified Mobile Communicator check box. |
| Step 4 | In the Protocol Specific Information section, in the Rerouting Calling Search Space drop-down list,
			 select a Calling Search Space (CSS) that can route the call to the DvO callback
			 number. |
| Step 5 | In the Product
			 Specific Configuration Layout section, set the Dial
				via Office drop-down list to Enabled . |
| Step 6 | Select Save . |
| Step 7 | Select Apply
				Config . |
| Step 8 | Instruct the
			 user to sign out of the client and then to sign back in again to access the
			 feature. Note DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from the Cisco Unified Communications Manager administrative interface fixes this issue. | Note | DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from the Cisco Unified Communications Manager administrative interface fixes this issue. |
| Note | DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from the Cisco Unified Communications Manager administrative interface fixes this issue. |

| Note | DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from the Cisco Unified Communications Manager administrative interface fixes this issue. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Mobile Connect |  |
| Step 2 | Add Mobility Identity | To configure the mobile device phone number. |
| Step 3 | Add Remote Destination (Optional) | To configure an alternate phone number. |
| Step 4 | Test your settings. | Exit Cisco Jabber on the
			 mobile device. Call the Cisco Jabber extension from another phone. Verify that the native mobile network phone number rings and that the call connects when you answer it. |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Search for and
			 delete any existing remote destination or mobility Identity that is already set
			 up with the mobile phone number as follows: Select Device > Remote
						Destination . Search for
				  the destination number. Delete the
				  destination number. |
| Step 3 | Configure the
			 end user for mobile connect as follows: Select User
						Management > End User . Search for
				  the end user. Select the user id to open the End User Configuration window. In the
				  Mobility Information section, check the Enable Mobility check box. On 
				  Cisco Unified Communications Manager Release 9.0 and earlier, specify the
				  Primary User Device. Select Save . |
| Step 4 | Configure the
			 device settings for mobile connect as follows: Navigate
				  to Device > Phone . Search for the device that you want to configure. Select the device name to open the Phone Configuration window. Enter the
				  following information: Setting Information Softkey Template Choose a softkey template that includes the Mobility button. For information about setting up softkey templates, see the
								  related information in the Cisco Unified Communications Manager Administration Guide for your release. This documentation can be found in the maintenance guides
								  list. Mobility User ID Select the user. Owner User ID Select the user. The value must match the mobility user ID. Rerouting Calling Search Space Choose a Rerouting Calling Search Space that includes both of
								  the following: The partition of the desk phone extension of the user. This
										requirement is used by the system to provide the Dial via Office feature, not
										for routing calls. A route to the mobile phone number. The route to the mobile
										phone number (that is, the Gateway/Trunk partition) must have a higher
										preference than the partitions of the enterprise extension that is associated
										with the device. Note Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. If the user sets up the DvO Callback Number with an alternate
								  number, ensure that you set up the trunk Calling Search Space (CSS) to route to
								  destination of the alternate phone number. Select Save . | Setting | Information | Softkey Template | Choose a softkey template that includes the Mobility button. For information about setting up softkey templates, see the
								  related information in the Cisco Unified Communications Manager Administration Guide for your release. This documentation can be found in the maintenance guides
								  list. | Mobility User ID | Select the user. | Owner User ID | Select the user. The value must match the mobility user ID. | Rerouting Calling Search Space | Choose a Rerouting Calling Search Space that includes both of
								  the following: The partition of the desk phone extension of the user. This
										requirement is used by the system to provide the Dial via Office feature, not
										for routing calls. A route to the mobile phone number. The route to the mobile
										phone number (that is, the Gateway/Trunk partition) must have a higher
										preference than the partitions of the enterprise extension that is associated
										with the device. Note Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. If the user sets up the DvO Callback Number with an alternate
								  number, ensure that you set up the trunk Calling Search Space (CSS) to route to
								  destination of the alternate phone number. | Note | Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. |
| Setting | Information |
| Softkey Template | Choose a softkey template that includes the Mobility button. For information about setting up softkey templates, see the
								  related information in the Cisco Unified Communications Manager Administration Guide for your release. This documentation can be found in the maintenance guides
								  list. |
| Mobility User ID | Select the user. |
| Owner User ID | Select the user. The value must match the mobility user ID. |
| Rerouting Calling Search Space | Choose a Rerouting Calling Search Space that includes both of
								  the following: The partition of the desk phone extension of the user. This
										requirement is used by the system to provide the Dial via Office feature, not
										for routing calls. A route to the mobile phone number. The route to the mobile
										phone number (that is, the Gateway/Trunk partition) must have a higher
										preference than the partitions of the enterprise extension that is associated
										with the device. Note Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. If the user sets up the DvO Callback Number with an alternate
								  number, ensure that you set up the trunk Calling Search Space (CSS) to route to
								  destination of the alternate phone number. | Note | Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. |
| Note | Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. |

| Setting | Information |
|---|---|
| Softkey Template | Choose a softkey template that includes the Mobility button. For information about setting up softkey templates, see the
								  related information in the Cisco Unified Communications Manager Administration Guide for your release. This documentation can be found in the maintenance guides
								  list. |
| Mobility User ID | Select the user. |
| Owner User ID | Select the user. The value must match the mobility user ID. |
| Rerouting Calling Search Space | Choose a Rerouting Calling Search Space that includes both of
								  the following: The partition of the desk phone extension of the user. This
										requirement is used by the system to provide the Dial via Office feature, not
										for routing calls. A route to the mobile phone number. The route to the mobile
										phone number (that is, the Gateway/Trunk partition) must have a higher
										preference than the partitions of the enterprise extension that is associated
										with the device. Note Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. If the user sets up the DvO Callback Number with an alternate
								  number, ensure that you set up the trunk Calling Search Space (CSS) to route to
								  destination of the alternate phone number. | Note | Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. |
| Note | Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. |

| Note | Cisco Jabber allows users to specify a callback
								  number for Dial via Office-Reverse calls that is different from the mobile
								  phone number of the device, and the Rerouting Calling Search Space controls
								  which callback numbers are reachable. |
|---|---|

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
			 the device that you want to configure as follows: Select Device > Phone . Search for
				  the device that you want to configure. Select the
				  device name to open the Phone Configuration window. |
| Step 3 | In the Associated Remote Destinations section, select Add a
				New Remote Destination . |
| Step 4 | Enter the
			 desired phone number as the Destination Number. You must be able to rout the number to an outbound gateway. Generally, the number is the full
				E.164 number. |
| Step 5 | Enter the
			 initial values for the following call timers: Answer Too Soon Timer —Enter 3000 Answer Too Late Timer — 
						  Enter 20000 Delay Before Ringing Timer —0 This setting does not apply to DvO-R calls. These values
				ensure that calls are not routed to the mobile service provider voicemail
				before they ring in the client on the mobile device. For more
				information, see the online help in Cisco Unified Communications Manager. |
| Step 6 | Do one of the
			 following: If you have Cisco Unified Communications Manager
						Version 9 or earlier, check the Enable Mobile Connect check box. If you have 
				Cisco Unified Communications Manager Version 10, check the Enable Single Number Reach check box. |
| Step 7 | Set up the
			 schedule for routing calls to the mobile number. |
| Step 8 | Select Save . |

| Implementation Method | Description | Instructions |
|---|---|---|
| Handoff DN | The
						mobile device calls 
						Cisco Unified Communications Manager using the mobile network. This
						method requires a Direct Inward Dial (DID) number. The
						service provider must deliver the DID digits exactly as configured.
						Alternately, for Cisco IOS gateways with H.323 or SIP communication to 
						Cisco Unified Communications Manager, you can use Cisco IOS to manipulate
						the inbound called-party number at the gateway, presenting the digits to 
						Cisco Unified Communications Manager exactly as configured on the handoff
						DN. This method does not work
						for iPod Touch devices. | See the Enable Handoff from VoIP to Mobile Network topic. |
| Mobility Softkey | Cisco Unified Communications Manager calls the phone number of the PSTN
						mobile service provider for the mobile device. | See the Enable Transfer from VoIP to Mobile Network topic. |
| None of the above | Disable this feature if you do not want to make it available to
					 users. | Select Disabled for the Transfer to Mobile Network option in the Product Specific Configuration Layout section of the
						TCT device page. Select Disabled for the Transfer to Mobile Network option in the Product Specific Configuration Layout section of the
						BOT device page. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call Routing > Mobility > Handoff Configuration . |
| Step 3 | Enter the 
			 Handoff Number for the Direct Inward Dial
			 (DID) number that the device uses to hand off a VoIP call to the mobile
			 network. The service provider must deliver the DID digits exactly as
				configured. Alternately, for Cisco IOS gateways with H.323 or SIP communication
				to Cisco Unified Communications Manager, you can use Cisco IOS to manipulate
				the inbound called-party number at the gateway, presenting the digits to Cisco Unified Communications Manager exactly as configured on the handoff number. Note You cannot use translation patterns or other similar
				  manipulations within Cisco Unified Communications Manager to match the inbound
				  DID digits to the configured Handoff DN. | Note | You cannot use translation patterns or other similar
				  manipulations within Cisco Unified Communications Manager to match the inbound
				  DID digits to the configured Handoff DN. |
| Note | You cannot use translation patterns or other similar
				  manipulations within Cisco Unified Communications Manager to match the inbound
				  DID digits to the configured Handoff DN. |
| Step 4 | Select the Route Partition for the handoff DID. This partition should be present in the Remote Destination inbound
				Calling Search Space (CSS), which points to either the Inbound CSS of the Gateway or Trunk, or the Remote Destination CSS. This feature does not use the remaining options on this page. |
| Step 5 | Select Save . |

| Note | You cannot use translation patterns or other similar
				  manipulations within Cisco Unified Communications Manager to match the inbound
				  DID digits to the configured Handoff DN. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Service Parameters . |
| Step 3 | Select the active server. |
| Step 4 | Select the Cisco CallManager (Active) service. |
| Step 5 | Scroll down to the Clusterwide Parameters (System - Mobility) section. |
| Step 6 | Select Matching Caller ID with Remote Destination and
			 read essential information about this value. |
| Step 7 | Select Partial Match for Matching Caller ID with Remote
				Destination . |
| Step 8 | Select Number of Digits for Caller ID Partial Match and read the essential requirements for this value. |
| Step 9 | Enter the required number of digits to ensure partial matches. |
| Step 10 | Select Save . |

| Step 1 | In the Cisco
				Unified CM Administration interface, go to the TCT Device page, and
			 select Use
				Handoff DN Feature for the Transfer to Mobile Network option. Do not assign
				this method for iPod Touch devices. Use the Mobility Softkey method instead. |
|---|---|
| Step 2 | In the Cisco
				Unified CM Administration interface, go to the BOT Device page, and
			 select Use
				Handoff DN Feature for the Transfer to Mobile Network option. |
| Step 3 | On the iOS
			 device, tap Settings > Phone > Show My Caller
				  ID to verify that Caller ID is on. |
| Step 4 | On some Android device and operating system combinations, you can
			 verify that the Caller ID is on. On the Android device, open the Phone
			 application and tap Menu > Call
				  Settings > Additional settings > Caller
				  ID > Show Number . |
| Step 5 | Test this
			 feature. |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | For
			 system-level settings, check that the Mobility softkey appears when the phone
			 is in the connected and on-hook call states. Select Device > Device
						Settings > Softkey Template . Select the
				  same softkey template that you selected when you configured the device for
				  Mobile Connect. In the Related Links drop-down list at the upper right,
				  select Configure Softkey Layout and select Go . In the
				  call state drop-down list, select the On Hook state and verify that the
				  Mobility key is in the list of selected softkeys. In the
				  call state drop-down list, select the Connected state and verify that the
				  Mobility key is in the list of selected softkeys. |
| Step 3 | Navigate to
			 the device that you want to configure as follows: Select Device > Phone . Search for
				  the device that you want to configure. Select the
				  device name to open the Phone Configuration window. |
| Step 4 | For the
			 per-user and per-device settings in 
			 Cisco Unified Communications Manager, set the specific device to use the
			 Mobility softkey when the device transfers calls to the mobile voice network.
			 Ensure that you have set up both Mobility Identity and Mobile Connect for the
			 mobile device. After the transfer feature is working, users can enable and
			 disable Mobile Connect at their convenience without affecting the feature. If the device
				is an iPod Touch, you can configure a Mobility Identity using an alternate
				phone number such as the mobile phone of the user. Select the Owner User ID on the device page. Select the Mobility User ID . The value usually matches that of
				  the Owner User ID. In the
				  Product Specific Configuration Layout section, for the Transfer to Mobile
				  Network option, select Use Mobility Softkey or Use HandoffDN Feature . |
| Step 5 | In the User
			 Locale field, choose English, United States . |
| Step 6 | Select Save . |
| Step 7 | Select Apply Config . |
| Step 8 | Instruct the user to sign out of the client and then to sign back
			 in again to access the feature. |

| Features | Mobile Clients | Desktop Clients |
|---|---|---|
| Log in to hunt group and log out of hunt group | Not supported | Supported |
| Call, answer, and decline | Supported | Supported |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
				  Routing > Route/Hunt > Line
				  Group . The Find
				  and List Line Groups window opens. |
| Step 3 | Select Add
				New . The Line
				  Group Configuration window opens. |
| Step 4 | Enter settings
			 in the Line
				Group Information section as follows: Specify a
					 unique name in the Line Group Name field. Specify
					 number of seconds for RNA Reversion Timeout . Select a Distribution Algorithm to apply to the line group. |
| Step 5 | Enter settings
			 in the Hunt Options section as follows: Select
						  a value for No Answer from the drop-down list. Select Automatically Logout Hunt Member on No Answer to configure auto logout of the hunt list. Select
						  a value for Busy from the drop-down list. Select
						  a value for Not Available from the drop-down list. |
| Step 6 | In the Line
				Group Member Information section, you can do the following: Find
					 directory numbers or route partitions to add to the line group. Reorder
					 the directory numbers or route partitions in the line group. Remove
					 directory numbers or route partitions from the line group. |
| Step 7 | Select Save . |

| Note | The group call pickup feature and directed call pickup feature do not work with hunt lists. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
				  Routing > Route/Hunt > Hunt
				  List . The Find and Hunt List Groups window opens. |
| Step 3 | Select Add New . The Hunt List Configuration window opens. |
| Step 4 | Enter settings in the Hunt List Information section as follows: Specify a unique name in the Name field. Enter a description for the Hunt List. Select a Cisco Unified Communications Manager
						Group from the drop-down list. The system selects Enable this Hunt List by default for a
					 new hunt list when the hunt list is saved. If this hunt list is to be used for voice mail, select For Voice Mail Usage . |
| Step 5 | Select Save to add the hunt list. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
				  Routing > Route/Hunt > Hunt
				  List . The Find and Hunt List Groups window opens. |
| Step 3 | Locate the hunt list to which you want to add a line group. |
| Step 4 | To add a line group, select Add Line Group . The Hunt List Detail Configuration window
				displays. |
| Step 5 | Select a line group from the Line Group drop-down list. |
| Step 6 | To add the line group, select Save . |
| Step 7 | To add additional line groups, repeat Step 4 to Step 6. |
| Step 8 | Select Save. |
| Step 9 | To reset the hunt list, select Reset . When the dialog box appears, select Reset . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
				  Routing > Route/Hunt > Hunt
				  Pilot . The Find
				  and List Hunt Pilots window opens. |
| Step 3 | Select Add
				New . The Hunt
				  Pilot Configuration window opens. |
| Step 4 | Enter the hunt
			 pilot, including numbers and wildcards. |
| Step 5 | Select a hunt
			 list from the Hunt
				List drop-down list. |
| Step 6 | Enter any
			 additional configurations in the Hunt
				Pilot Configuration window. For more information on hunt pilot
			 configuration settings, see the relevant 
			 Cisco Unified Communications Manager documentation. |
| Step 7 | Select Save . |