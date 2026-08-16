---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-vmo-release-notes-b-1202cucvmorn-html-47b9f62fc5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/vmo/release/notes/b_1202cucvmorn.html
retrieved_at: 2026-08-16T18:50:12.146610+00:00
---

Release Notes for Cisco ViewMail for Microsoft Outlook Release 12.0(2)

# Release Notes for Cisco ViewMail for Microsoft Outlook Release 12.0(2)

- 12.5(1)

- 12.0(2)

### Download Options

Updated: May 4, 2018

# Release Notes for
	 Cisco ViewMail for Microsoft Outlook Release 12.0(2)

These release notes
		contain requirements, download, installation, configuration instructions, new
		and changed requirements, support, limitations and restrictions, and caveat
		information for Cisco ViewMail for Microsoft Outlook Release 12.0(2).

ViewMail for Outlook
		12.0(2) is available only from the Cisco Download Software website.

## Introduction

Cisco ViewMail for
		Microsoft Outlook provides a visual interface with which users can send, listen
		to, and manage their Cisco Unity Connection voice messages from Outlook.

Note the following
		considerations with ViewMail for Outlook:

- Users get voice messages in
						the same Inbox as their email.

- Voice messages sent from
						Outlook do not appear in the Sent Items folder.

- ViewMail for Outlook is
						required for users to play secure messages in the Exchange mailbox.

- Users get voice messages in
						a separate mail folder in Outlook.

- New voice messages get
						identified by a separate voice message icon.

- ViewMail for Outlook is
						required for users to play secure messages in the Unity Connection mailbox.

- On Windows operating system
				with ViewMail for Outlook, the text of the voice messages appears in black
				color and the ViewMail category appears in blue color. However, on MAC
				operating system, the text of the voice messages and the ViewMail category
				appears in the system default color.

- When there is no default
				recording device available on the Windows machines and the user selectsthe
				recording device from Phone to Computer Default option then ViewMail for
				Outlook will always consider Phone as default recording device.

## Requirements

- The “Matrices for Unity
				Connection 12.x and Cisco Business Edition 6000/7000” section of Compatibility Matrix for Cisco Unity Connection at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​compatibility/​matrix/​b_​cucclientmtx.html .

- Microsoft DirectX 9.0

- Microsoft .NET Framework
				4.0

- Microsoft Visual C++ 2008
				Redistributable Package

(If the software
			 is not already installed, ViewMail for Outlook Setup installs it.)

- To install or upgrade
		  ViewMail for Outlook, you must have local administrator rights on the user
		  workstation.

- The user workstation must
		  have at least 12 MB of hard-disk space available for ViewMail for Outlook. (If
		  other required software is being installed,100 MB or more may be required.)

- If the proxy is enabled on
		  the user workstation, then it must be connected to port 443 (HTTPS) to allow
		  the communication between ViewMail for Outlook and Cisco Unity Connection.

See also the “ Prerequisites ”
		section of these release notes.

### Compatibility
	 Information

- For information on all
		  qualified version combinations of ViewMail for Outlook, Cisco Unity Connection,
		  and the software on user workstations, see Compatibility Matrix for Cisco Unity
		  Connection at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​compatibility/​matrix/​b_​cucclientmtx.html .
		  The document also contains the support policy for software on user
		  workstations.

- For a list of all
		  languages available for ViewMail for Outlook, see the “Available Languages for
		  Cisco Unity Connection Components” section of System
			 Requirements for Cisco Unity Connection Release 12.x at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​requirements/​b_​12xcucsysreqs.html .

### Determining the
	 ViewMail for Outlook Version

To Determine the ViewMail
			 for Outlook Version in Use from Outlook

In Outlook on the
		  user workstation:

## Related
	 Documentation

## New and Changed
	 Requirements and Support—Release 12.0(2)

### Additional
	 Languages for ViewMail for Outlook

All locales will be
		released soon for ViewMail for Outlook 12.0(2) release.

For a list of all
		languages available for ViewMail for Outlook, see the “Available Languages for
		Cisco Unity Connection Components” section of System
		  Requirements for Cisco Unity Connection Release 12.x at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​requirements/​b_​12xcucsysreqs.html .

## New and Changed
	 Functionality—Release 12.0(2)

This section
		contains information about new functionality in the ViewMail For Outlook
		12.0(2) release.

### Support for DPI Scaling

With release 12.0(2) and later, Viewmail for Outlook supports DPI  (Dots Per Inch) Scaling for higher resolution without any distortion.

## Installation and
	 Upgrade Information

### Task List for
	 Installing ViewMail for Outlook 12.0(2) for the First Time

- Confirm that ViewMail
		  requirements and prerequisites have been met. See the “ Requirements ”
		  section and the “ Prerequisites ”
		  section.

- Download ViewMail for
		  Outlook from the Cisco Download Software website. See the “ Downloading ViewMail for Outlook 12.0(2) ”
		  section.

- Optional : Customize
		  ViewMail for Outlook setup. See the “ Customizing ViewMail for Outlook Setup ”
		  section.

- Optional :
		  Provide users with ViewMail for Outlook files for installation.

- Install ViewMail for
		  Outlook. Provide users with instructions, if applicable. See the “ Installing or Upgrading to ViewMail for Outlook 12.0(2) ”
		  section.

- Using the ViewMail for
				  Outlook Initialization wizard : When they restart Outlook following ViewMail
				installation, the Initialization wizard prompts users for any required
				information that was not already prepopulated.

- Using the ViewMail Options
				  or Settings dialog : Enter the required information. Provide users with
				instructions, if applicable. See the “ Installing ViewMail for Outlook 12.0(2) Using Command Line Switches ”
				section.

### Task List for
	 Upgrading to ViewMail for Outlook 12.0(2)

- Confirm that ViewMail
		  requirements and prerequisites have been met. See the “ Requirements ”
		  section and the “ Prerequisites ”
		  section.

- Download ViewMail for
		  Outlook from the Cisco Download Software website. See the “ Downloading ViewMail for Outlook 12.0(2) ”
		  section.

- Optional : Customize
		  ViewMail for Outlook setup for the upgrade, if applicable. See the “ Customizing ViewMail for Outlook Setup ”
		  section.

- Optional : Provide users
		  with ViewMail for Outlook files for the upgrade.

- Upgrade ViewMail for
		  Outlook. Provide users with instructions, if applicable. See the “ Installing or Upgrading to ViewMail for Outlook 12.0(2)

### Prerequisites

#### Prerequisites for
	 Using ViewMail for Outlook with the Single-Inbox Feature

- The single-inbox feature is
		  enabled.(See the Unified Messaging Guide for Cisco Unity Connection Release
		  12.x at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​unified_messaging/​b_​12xcucumgx.html .)

- An Exchange email account
		  in Outlook points to each user’s Exchange mailbox.

#### Prerequisites for
	 Using ViewMail for Outlook with IMAP

For ViewMail for
		Outlook users who will access Unity Connection voice messages by using IMAP,
		confirm that the following prerequisites have been met:

(See the “ Users ” chapter of the System
				Administration Guide for Cisco Unity Connection Release 12.x at https:/​​/​​www.cisco.com/​​c/​​en/​​us/​​td/​​docs/​​voice_ip_comm/​​connection/​​12x/​​administration/​​guide/​​b_​​12xcucsag.html. .)

(See the “ User Attributes ”
			 chapter of the System
				Administration Guide for Cisco Unity Connection Release 12.x .)

(See the Unified
			 Messaging Guide for Cisco Unity Connection Release 12.x at https:/​​/​​www.cisco.com/​​c/​​en/​​us/​​td/​​docs/​​voice_ip_comm/​​connection/​​12x/​​unified_messaging/​​b_​​12xcucumgx.html. .)

(See the
			 Security Guide for Cisco Unity Connection Release 12.x at https:/​​/​​www.cisco.com/​​c/​​en/​​us/​​td/​​docs/​​voice_ip_comm/​​connection/​​12x/​​security/​​b_​​12xcucsecx.html .)

(See the “ Creating
				and Configuring an Account in Outlook to Access Voice Messages (IMAP Users
				Only) ” section on page 6 of these release notes.)

#### Creating and
	 Configuring an Account in Outlook to Access Voice Messages (IMAP Users
	 Only)

Do the applicable
		procedure—depending on the Outlook version—for ViewMail for Outlook users who
		will access Connection voice messages by using IMAP:

##### To Create and
	 Configure an Account in Outlook 2010 and later to Access Voice Messages (IMAP
	 Users)

- In the
				  Your Name field, enter a display name for the account. This typically is the
				  full name of the user.

The
					 address is available in the SMTP Address field on the User Basics page in
					 Connection Administration, and typically uses the following format:

<username>@<SMTP domain name of the Unity Connection
					 server or cluster>

- In the
				  Password field, enter the user’s Cisco PCA password (also known as the web
				  application password).

- In the
				  Retype Password field, enter the Cisco PCA password again.

##### To Create and
	 Configure an Account in Outlook 2007 to Access Voice Messages (IMAP
	 Users)

- In the Your Name field, enter a display name for the account.
				  This typically is the full name of the user.

<username>@<SMTP domain name of the Unity Connection
					 server or cluster>

- In the Password field, enter the user’s Cisco PCA password
				  (also known as the web application password).

- In the Retype Password field, enter the Cisco PCA password
				  again.

### Downloading
	 ViewMail for Outlook 12.0(2)

To Download ViewMail for
			 Outlook 12.0(2)

### Customizing
	 ViewMail for Outlook Setup

The file AdminConfig.xml is
		available in the ViewMail for Outlook installation folder. Use the file to
		prepopulate user and voicemail server information when the ViewMail for Outlook
		installation or upgrade is being pushed out to users.

After entering information in AdminConfig.xml, leave the file in the
		ViewMail installation folder when you make it available to users.

### Installing or
	 Upgrading to ViewMail for Outlook 12.0(2)

By default,
		  ViewMail for Outlook files are installed in the directory C:\Program
		  Files\Cisco Systems\ViewMail for Outlook. You can specify a different directory
		  during the software installation.

Do the procedure
		  in this section to install or upgrade ViewMail for Outlook on user
		  workstations. Youcan also install ViewMail for multiple users who share a
		  workstation.

To Install or Upgrade to
			 ViewMail for Outlook 12.0(2)

Use
							 this file for new installations and for upgrades from versions earlier than
							 12.0(2) It installs prerequisite software, as needed; places the
							 AdminConfig.xml file in the correct location; and uninstalls older versions
							 during upgrades.

- Win32 : If you need to
								install 32-bit ViewMail for Outlook.

- x64 : If you need to
								install 64-bit ViewMail for Outlook.

Use
							 this file for quick minor upgrades for ViewMail 32-bit with versions 12.0(2)
							 and later.

Use
							 this file for quick minor upgrades for ViewMail 64-bit with versions 12.0(2)
							 and later.

### Installing
	 ViewMail for Outlook 12.0(2) Using Command Line Switches

To install ViewMail for
			 Outlook 12.0(2) through command line switches :

<Path of
				the VMO setup directory>setup.exe /i /qb /logfile <File Name>

### Associating the
	 Applicable Email Account with the Voicemail Server

Do the following
		  procedure on each user workstation.

To Associate an Email
			 Account with a Voicemail Server

Outlook 2010 and above

Enter the user’s Cisco PCA password (also known as the web
							 application password).

Display only.

(Possible values are “Connected,” “Not Connected,” “Invalid
							 Credentials,” and “Unknown.”)

Enter the extension or a phone number for the user.

This
							 setting is required only if you want Unity Connection users to be able to
							 record or play messages by using the phone.

## Limitations and
	 Restrictions

### Installing a New
	 Version of Outlook Requires Uninstalling ViewMail First

When installing a new version of Microsoft Outlook on user workstations,
		you must first uninstall ViewMail for Outlook. After you have installed
		Outlook, reinstall ViewMail.

Otherwise, ViewMail for Outlook will seem to be installed properly with
		the new version of Outlook, but it may not work.

### Message
	 Sensitivity Displays as Blank for Normal Sensitivity Messages Recorded in
	 ViewMail

Users whose Outlook clients are
		configured to display the Sensitivity field in the message-list view may notice
		that messages recorded in ViewMail for Outlook with the Sensitivity set to
		Normal do not display any text in the Sensitivity field.

Messages recorded by using the Cisco Unity Connection phone interface
		(as well as email messages composed in Outlook) display “Normal” in the
		Sensitivity field.

### Some Software on
	 User Workstations Can Cause ViewMail to Fail

Some security and VPN software installed on user workstations may cause
		ViewMail for Outlook to fail. In particular, software that offers personal
		firewalls is problematic.

Exceptions may need to be added to the problematic software to allow
		ViewMail to work. Alternatively, you can set up ViewMail so that users can play
		messages with audio devices on their computers.

### Unity Connection
	 Server Must Be Available to Compose Voice Messages

In order to compose voice messages
		by using ViewMail for Outlook with Cisco Unity Connection 8.5 and later,
		ViewMail must be able to contact the Unity Connection server. If the server is
		not available, users will see the following message: “The requested action
		could not be performed because the voicemail server was not available.”

In earlier ViewMail versions, voice messages could be recorded while the
		Unity Connection server was unavailable and were sent when the server became
		available again.

### ViewMail for
	 Outlook 12.0(2) Limitations Regarding Icon Update when a Voice Message is read
	 or unread

When a voice mail is
		marked read or unread using ViewMail for Outlook 12.0(2), the state of voice
		mail Icon is not updated regardless of the Microsoft Outlook version.

### ViewMail for
	 Outlook 12.0(2) Limitations Regarding Cisco Unity 5 Message Playback

When playing a Cisco
		Unity 5 message using ViewMail for Outlook with "VMO Play Attachment" feature,
		audio progress bar is not updated and time duration is not displayed on the
		ViewMail audio pane of the VoiceMail.

### ViewMail for
	 Outlook 64-Bit Limitation Regarding G.729

ViewMail for Outlook 64 bit version
		is not supported for G.729 codec.

## Caveats

You can find the
		latest caveat information for Cisco Unity Connection ViewMail for Microsoft
		Outlook version 12.0(2) by using Bug Toolkit, an online tool available for
		customers to query defects according to their own needs.

Bug Toolkit is
		available at http:/​/​www.cisco.com/​go/​bugs .
		Fill in your query parameters by using the custom settings in the Advanced
		Settings option.

Release notes for
		all versions of ViewMail for Outlook are available at http:/​/​www.cisco.com/​en/​US/​products/​ps6509/​prod_​release_​notes_​list.html .

### Open
	 Caveats—Release 12.0(2)

There is no open
		  caveat in ViewMail for Outlook version 12.0(2) release.

### Resolved
	 Caveats—Release 12.0(2)

Revised April, 2018

This section lists
		  the resolved caveats for VMO 12.0(2) release. Click a link in the Caveat Number
		  column to view the latest information on the caveat in Bug Toolkit.

(Caveats are
		  listed in order by severity, then by component, then by caveat number.)

Caveat
						Number

Component

Severity

Description

CSCvi26611

VMO

3

Unable
						to install VMO 11.5 once 12.0 is uninstalled due to Add-in Initlization getting
						failed

CSCvj00275

VMO

4

Cisco Viewmail 12.0, 'Stop' Playback on VMO causes outlook
						to crash and restart.

CSCvi26419

VMO

4

Outlook
						getting crashed in Offfline mode with view mail installed for 12.0

## Obtaining
	 Documentation and Submitting a Service Request

For information on obtaining
		documentation, submitting a service request, and gathering additional
		information, see the monthly What’s New in Cisco Product Documentation, which
		also lists all new and revised Cisco technical documentation, at: http:/​/​www.cisco.com/​en/​US/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really
		Simple Syndication (RSS) feed and set content to be delivered directly to your
		desktop using a reader application. The RSS feeds are a free service and Cisco
		currently supports RSS Version 2.0.

### This Document Applies to These Products

- Unity Connection ViewMail for Microsoft Outlook Version 12.0

| Note | For full access
		  to the Download Software website, you must be signed in to Cisco.com as a
		  registered user. |
|---|---|

| Single-inbox users | Users get voice messages in
						the same Inbox as their email. Voice messages sent from
						Outlook do not appear in the Sent Items folder. ViewMail for Outlook is
						required for users to play secure messages in the Exchange mailbox. |
|---|---|
| IMAP users | Users get voice messages in
						a separate mail folder in Outlook. New voice messages get
						identified by a separate voice message icon. ViewMail for Outlook is
						required for users to play secure messages in the Unity Connection mailbox. |

| Note | On Windows operating system
				with ViewMail for Outlook, the text of the voice messages appears in black
				color and the ViewMail category appears in blue color. However, on MAC
				operating system, the text of the voice messages and the ViewMail category
				appears in the system default color. When there is no default
				recording device available on the Windows machines and the user selectsthe
				recording device from Phone to Computer Default option then ViewMail for
				Outlook will always consider Phone as default recording device. |
|---|---|

| Note | Cisco ViewMail for Microsoft Outlook 12.0(2) is compatible with Cisco
		Unity Connection 12.0(1), 11.x and 10.x . |
|---|---|

| Outlook 2010 and above | On the ViewMail tab, select About Cisco ViewMail. |
|---|---|

| Note | The Quick Start
			 Guide for Cisco ViewMail for Microsoft Outlook (Release 8.5 and Later) is
		  available at http:/​/​www.cisco.com/​en/​US/​docs/​voice_ip_comm/​connection/​vmo/​quick_start/​guide/​85xcucqsgvmo.html . |
|---|---|

| Note | You can enter a
		  special character multiple times as per your requirements. |
|---|---|

| Note | If you are
		  upgrading from a ViewMail for Outlook version earlier than 12.0(2), see the
		  “ Task List for Installing ViewMail for Outlook 12.0(2) for the First Time ”
		  section. The older version is uninstalled automatically, and installing 12.0(2)
		  is considered a new installation. |
|---|---|

| Note | Do the
		  following tasks in the order listed to upgrade ViewMail for Outlook to a later
		  version. |
|---|---|

| Note | Existing
				email account and ViewMail for Outlook settings remain unchanged during an
				upgrade. |
|---|---|

| Step 1 | Start
			 Outlook. |
|---|---|
| Step 2 | On the File
			 tab, select Info , then Add
				Account . |
| Step 3 | Confirm that
			 Email Account (the default) is selected, then enter user information: In the
				  Your Name field, enter a display name for the account. This typically is the
				  full name of the user. In the
				  Email Address field, enter the Connection SMTP address of the user. The
					 address is available in the SMTP Address field on the User Basics page in
					 Connection Administration, and typically uses the following format: <username>@<SMTP domain name of the Unity Connection
					 server or cluster> In the
				  Password field, enter the user’s Cisco PCA password (also known as the web
				  application password). In the
				  Retype Password field, enter the Cisco PCA password again. |
| Step 4 | Select Next . |
| Step 5 | If you see the “Problem
				Connecting to Server” message about an unavailable encrypted connection: Select Next to
			 use an unencrypted connection. |
| Step 6 | When the
			 email-account configuration is complete, select Finish Note If Outlook
				2013 is getting crashed when you click on Draft Message/Sent
				Message/Calendar/Contacts, make sure that the IntResource64.dll library file
				does not exist in the %temp%\AppData\Local\Temp\folder. If the file exists in
				the specified location, delete the file before starting Outlook to resolve this
				issue. | Note | If Outlook
				2013 is getting crashed when you click on Draft Message/Sent
				Message/Calendar/Contacts, make sure that the IntResource64.dll library file
				does not exist in the %temp%\AppData\Local\Temp\folder. If the file exists in
				the specified location, delete the file before starting Outlook to resolve this
				issue. |
| Note | If Outlook
				2013 is getting crashed when you click on Draft Message/Sent
				Message/Calendar/Contacts, make sure that the IntResource64.dll library file
				does not exist in the %temp%\AppData\Local\Temp\folder. If the file exists in
				the specified location, delete the file before starting Outlook to resolve this
				issue. |

| Note | If Outlook
				2013 is getting crashed when you click on Draft Message/Sent
				Message/Calendar/Contacts, make sure that the IntResource64.dll library file
				does not exist in the %temp%\AppData\Local\Temp\folder. If the file exists in
				the specified location, delete the file before starting Outlook to resolve this
				issue. |
|---|---|

| Step 1 | Start Outlook. |
|---|---|
| Step 2 | From the Outlook Tools menu,
			 select Account Settings . |
| Step 3 | In the Account Settings
			 dialog, on the Email tab, select New. |
| Step 4 | In the Add New Email Account wizard, select Microsoft Exchange, POP3, IMAP or HTTP as the email service,
			 then select Next . |
| Step 5 | Enter user information: In the Your Name field, enter a display name for the account.
				  This typically is the full name of the user. In the Email Address field, enter the Connection SMTP address
				  of the user. The address is available in the SMTP Address field on the
				  User Basics page in Connection Administration, and typically uses the following
				  format: <username>@<SMTP domain name of the Unity Connection
					 server or cluster> In the Password field, enter the user’s Cisco PCA password
				  (also known as the web application password). In the Retype Password field, enter the Cisco PCA password
				  again. |
| Step 6 | Select Next . |
| Step 7 | If you see the Problem Connecting to Server message about an
			 unavailable encrypted connection: Select Next to use an unencrypted connection. |
| Step 8 | When the email-account configuration is complete, select Finish. |

| Step 1 | On a computer
			 with a high-speed Internet connection, go to the Voice and Unified
			 Communications download page at http:/​/​www.cisco.com/​cisco/​software/​navigator.html?mdfid=280082558 . Note To access
				the software download page, you must be signed in to Cisco.com as a registered
				user. | Note | To access
				the software download page, you must be signed in to Cisco.com as a registered
				user. |
|---|---|---|---|
| Note | To access
				the software download page, you must be signed in to Cisco.com as a registered
				user. |
| Step 2 | In the tree
			 control on the download page, expand Products > Unified
				Communications > Unified
				Communications Applications> Messaging> Unity Connection , and select Unity
				Connection ViewMail for Microsoft Outlook Version 12.0(2) . |
| Step 3 | In the Latest
			 Releases folder, select VMO
				12.0(2) . |
| Step 4 | On the right
			 side of the page, select Download Now, and follow the on-screen prompts to
			 complete the download. |

| Note | To access
				the software download page, you must be signed in to Cisco.com as a registered
				user. |
|---|---|

| Step 1 | If Microsoft
			 Outlook is running, exit the application. |
|---|---|
| Step 2 | In the
			 ViewMail folder, double-click the applicable file: Setup.exe Use
							 this file for new installations and for upgrades from versions earlier than
							 12.0(2) It installs prerequisite software, as needed; places the
							 AdminConfig.xml file in the correct location; and uninstalls older versions
							 during upgrades. This
							 folder consists of two sub folders: Win32 : If you need to
								install 32-bit ViewMail for Outlook. x64 : If you need to
								install 64-bit ViewMail for Outlook. Note For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. ViewMail.msi Use
							 this file for quick minor upgrades for ViewMail 32-bit with versions 12.0(2)
							 and later. ViewMail_64.msi Use
							 this file for quick minor upgrades for ViewMail 64-bit with versions 12.0(2)
							 and later. Note For
				successful installation and upgrade of ViewMail for Outlook 12.0(2), you must
				download and run the setup.exe. | Setup.exe | Use
							 this file for new installations and for upgrades from versions earlier than
							 12.0(2) It installs prerequisite software, as needed; places the
							 AdminConfig.xml file in the correct location; and uninstalls older versions
							 during upgrades. This
							 folder consists of two sub folders: Win32 : If you need to
								install 32-bit ViewMail for Outlook. x64 : If you need to
								install 64-bit ViewMail for Outlook. Note For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. | Note | For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. | ViewMail.msi | Use
							 this file for quick minor upgrades for ViewMail 32-bit with versions 12.0(2)
							 and later. | ViewMail_64.msi | Use
							 this file for quick minor upgrades for ViewMail 64-bit with versions 12.0(2)
							 and later. | Note | For
				successful installation and upgrade of ViewMail for Outlook 12.0(2), you must
				download and run the setup.exe. |
| Setup.exe | Use
							 this file for new installations and for upgrades from versions earlier than
							 12.0(2) It installs prerequisite software, as needed; places the
							 AdminConfig.xml file in the correct location; and uninstalls older versions
							 during upgrades. This
							 folder consists of two sub folders: Win32 : If you need to
								install 32-bit ViewMail for Outlook. x64 : If you need to
								install 64-bit ViewMail for Outlook. Note For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. | Note | For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. |
| Note | For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. |
| ViewMail.msi | Use
							 this file for quick minor upgrades for ViewMail 32-bit with versions 12.0(2)
							 and later. |
| ViewMail_64.msi | Use
							 this file for quick minor upgrades for ViewMail 64-bit with versions 12.0(2)
							 and later. |
| Note | For
				successful installation and upgrade of ViewMail for Outlook 12.0(2), you must
				download and run the setup.exe. |
| Step 3 | Follow the
			 on-screen prompts to complete the installation. |
| Step 4 | Restart
			 Outlook. |

| Setup.exe | Use
							 this file for new installations and for upgrades from versions earlier than
							 12.0(2) It installs prerequisite software, as needed; places the
							 AdminConfig.xml file in the correct location; and uninstalls older versions
							 during upgrades. This
							 folder consists of two sub folders: Win32 : If you need to
								install 32-bit ViewMail for Outlook. x64 : If you need to
								install 64-bit ViewMail for Outlook. Note For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. | Note | For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. |
|---|---|---|---|
| Note | For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. |
| ViewMail.msi | Use
							 this file for quick minor upgrades for ViewMail 32-bit with versions 12.0(2)
							 and later. |
| ViewMail_64.msi | Use
							 this file for quick minor upgrades for ViewMail 64-bit with versions 12.0(2)
							 and later. |

| Note | For silent installation of ViewMail for Outlook, in
							 AdminConfig.xml file, the user id should be the login name of the system
							 whereas the username and password should be the user name and password of Cisco
							 Unity Connection. |
|---|---|

| Note | For
				successful installation and upgrade of ViewMail for Outlook 12.0(2), you must
				download and run the setup.exe. |
|---|---|

| Step 1 | Run the
			 following command on command prompt: <Path of
				the VMO setup directory>setup.exe /i /qb /logfile <File Name> Note <File
				Name> is the name of the log file. | Note | <File
				Name> is the name of the log file. |
|---|---|---|---|
| Note | <File
				Name> is the name of the log file. |
| Step 2 | Restart
			 Outlook. |

| Note | <File
				Name> is the name of the log file. |
|---|---|

| Note | If you are
			 upgrading ViewMail for Outlook from 8.5(x) to a later version, skip this task
			 as the existing email account and ViewMail settings remain unchanged during an
			 upgrade. |
|---|---|

| Step 1 | In Outlook,
			 open the ViewMail Settings or Options dialog: Outlook 2010 and above On the ViewMail tab, select Settings. | Outlook 2010 and above | On the ViewMail tab, select Settings. |
|---|---|---|---|
| Outlook 2010 and above | On the ViewMail tab, select Settings. |
| Step 2 | Select Add , then
			 select the account to associate with a voicemail server. |
| Step 3 | Enter the
			 applicable information in each field: Voicemail Server Type Select the voicemail server type to associate with the email
							 account. Note In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. Username Enter the Cisco Unity Connection username (alias) of the user. Password Enter the user’s Cisco PCA password (also known as the web
							 application password). Voicemail Server Name Enter the name of the voicemail server. Voicemail Server Status Display only. (Possible values are “Connected,” “Not Connected,” “Invalid
							 Credentials,” and “Unknown.”) Phone Number Enter the extension or a phone number for the user. This
							 setting is required only if you want Unity Connection users to be able to
							 record or play messages by using the phone. Recording Device Select the preferred device. Playback Device Select the preferred device. | Voicemail Server Type | Select the voicemail server type to associate with the email
							 account. Note In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. | Note | In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. | Username | Enter the Cisco Unity Connection username (alias) of the user. | Password | Enter the user’s Cisco PCA password (also known as the web
							 application password). | Voicemail Server Name | Enter the name of the voicemail server. | Voicemail Server Status | Display only. (Possible values are “Connected,” “Not Connected,” “Invalid
							 Credentials,” and “Unknown.”) | Phone Number | Enter the extension or a phone number for the user. This
							 setting is required only if you want Unity Connection users to be able to
							 record or play messages by using the phone. | Recording Device | Select the preferred device. | Playback Device | Select the preferred device. |
| Voicemail Server Type | Select the voicemail server type to associate with the email
							 account. Note In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. | Note | In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. |
| Note | In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. |
| Username | Enter the Cisco Unity Connection username (alias) of the user. |
| Password | Enter the user’s Cisco PCA password (also known as the web
							 application password). |
| Voicemail Server Name | Enter the name of the voicemail server. |
| Voicemail Server Status | Display only. (Possible values are “Connected,” “Not Connected,” “Invalid
							 Credentials,” and “Unknown.”) |
| Phone Number | Enter the extension or a phone number for the user. This
							 setting is required only if you want Unity Connection users to be able to
							 record or play messages by using the phone. |
| Recording Device | Select the preferred device. |
| Playback Device | Select the preferred device. |
| Step 4 | Select Test
				Settings to verify the information that was entered. |
| Step 5 | Select OK . |

| Outlook 2010 and above | On the ViewMail tab, select Settings. |
|---|---|

| Voicemail Server Type | Select the voicemail server type to associate with the email
							 account. Note In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. | Note | In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. |
|---|---|---|---|
| Note | In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. |
| Username | Enter the Cisco Unity Connection username (alias) of the user. |
| Password | Enter the user’s Cisco PCA password (also known as the web
							 application password). |
| Voicemail Server Name | Enter the name of the voicemail server. |
| Voicemail Server Status | Display only. (Possible values are “Connected,” “Not Connected,” “Invalid
							 Credentials,” and “Unknown.”) |
| Phone Number | Enter the extension or a phone number for the user. This
							 setting is required only if you want Unity Connection users to be able to
							 record or play messages by using the phone. |
| Recording Device | Select the preferred device. |
| Playback Device | Select the preferred device. |

| Note | In IMAP account, Cisco Unity Connection 7.x and 8.x versions
								support Unity Connection 7.x and 8.0.x voicemail server type and Cisco Unity
								Connection 8.5 and later versions support Unity Connection 8.5 (IMAP) voicemail
								server type. |
|---|---|

| Note | In ViewMail for Outlook 11.5(1) and later, if the user connects or
		disconnects the audio devices, it is recommended to restart Outlook, so that
		ViewMail for Outlook displays the status of currently attached recording and
		playback devices only. |
|---|---|

| Note | To access Bug
		  Toolkit, you must be signed in to Cisco.com as a registered user. |
|---|---|

| Caveat
						Number | Component | Severity | Description |
|---|---|---|---|
| CSCvi26611 | VMO | 3 | Unable
						to install VMO 11.5 once 12.0 is uninstalled due to Add-in Initlization getting
						failed |
| CSCvj00275 | VMO | 4 | Cisco Viewmail 12.0, 'Stop' Playback on VMO causes outlook
						to crash and restart. |
| CSCvi26419 | VMO | 4 | Outlook
						getting crashed in Offfline mode with view mail installed for 12.0 |