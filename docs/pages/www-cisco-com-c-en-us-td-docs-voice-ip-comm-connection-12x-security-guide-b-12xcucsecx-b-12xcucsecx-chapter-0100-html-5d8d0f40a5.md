---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-security-guide-b-12xcucsecx-b-12xcucsecx-chapter-0100-html-5d8d0f40a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/guide/b_12xcucsecx/b_12xcucsecx_chapter_0100.html
retrieved_at: 2026-08-21T07:54:12.033197+00:00
---

Security Guide for Cisco Unity Connection Release 12.x

# Security Guide for Cisco Unity Connection Release 12.x

Updated: August 4, 2017

Chapter: FIPS Compliance in
	 Cisco Unity Connection

## Chapter: FIPS Compliance in
	 Cisco Unity Connection

# FIPS Compliance in
	 Cisco Unity Connection

## Running CLI
	 Commands for FIPS

To enable the FIPS feature in Cisco Unity Connection, you use
		the utils fips enable CLI command. In addition to this, the following CLI
		commands are also available:

utils fips disable- Use to disable the FIPS feature.

utils fips status- Use to check the status of FIPS compliance.

For more
		information on the utils fips <option> CLI commands, see the applicable Command Line
		  Interface Reference Guide for Cisco Unified Communications Solutions at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unity-connection/​products-maintenance-guides-list.html .

## Regenerating
	 Certificates for FIPS

Cisco Unity Connection servers with pre-existing telephony
		integrations must have the root certificate manually regenerated after enabling
		or disabling the FIPS mode. If the telephony integration uses an Authenticated
		or Encrypted Security mode, the regenerated root certificate must be
		re-uploaded to any corresponding Cisco Unified Communications Manager servers.
		For fresh installations, regenerating the root certificate can be avoided by
		enabling FIPS mode before adding the telephony integration.

- Sign in to Cisco Unity
		  Connection Administration.

- Select Telephony
		  Integrations> Security> Root Certificate.

- On the View Root
		  Certificate page, click Generate New.

- If the telephony
		  integration uses an Authenticated or Encrypted Security mode, continue with
		  steps 5-10, otherwise skip to step 12.

- On the View Root
		  Certificate page, right-click the Right-click to Save the Root Certificate as a
		  File link.

- On the Cisco Unified CM
				server, sign in to Cisco Unified Operating System Administration.

- Select the Certificate
				Management option from the Security menu.

- Select Upload
				Certificate/Certificate Chain on the Certificate List page.

- On the Upload
				Certificate/Certificate Chain page, select the CallManager-trust option from
				the Certificate Name drop-down.

- Enter Cisco Unity
				Connection Root Certificate in the Root Certificate field.

- Click Browse in the Upload
				File field to locate and select the Cisco Unity Connection root certificate
				that was saved in Step 5.

- Click Upload File.

- Click Close.

- On the Cisco Unified CM
		  server, sign in to Cisco Unified Serviceability.

- Select Service Management
		  from the Tools menu.

- On the Control Center -
		  Feature Services page, restart the Cisco CallManager service.

- Repeat steps 5-10 on all
		  remaining Cisco Unified CM servers in the Cisco Unified CM cluster.

- Sign in to Cisco Unity
				Connection Serviceability.

- Select Service Management
				from the Tools menu.

- Select Stop for the Unity
				Connection Conversation Manager service in the Critical Services section.

- When the Status area
				displays a message that the Unity Connection Conversation Manager service is
				successfully stopped, select Start for the service.

- New and pre-existing
		  telephony integration ports are now correctly registered with Cisco Unified CM.

FIPS is supported
		for both SCCP and SIP integrations between Cisco Unified Communications Manager
		and Cisco Unity Connection.

For more
		information on managing certificates, see the " Manage Certificates and
		  Certificate Trust " Lists section in the "Security" chapter of the Cisco
		Unified Communications Operating System Administration Guide for Cisco Unity
		Connection at: https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​os_administration/​b_​12xcucosagx.html

## Configuring Additional Settings When Using FIPS Mode

In order to maintain FIPS compliance, additional
		configurations are mandatory for the following features:

- Networking: Intrasite,
		  Intersite, VPIM

- Unified Messaging: Unified
		  Messaging Services.

### Configure Networking When Using FIPS Mode

Networking from Cisco Unity Connection to another
		server must be secured by an IPsec policy. This includes intersite links,
		intrasite links, and VPIM locations. The remote server is responsible for
		assuring its own FIPS compliance.

### Configure Unified Messaging When Using FIPS Mode

Unified Messaging Services require the following
		configuration:

- Configure IPsec policy
		  between Cisco Unity Connection and Microsoft Exchange or Cisco Unified
		  MeetingPlace.

- Set the Web-Based
		  Authentication Mode setting to Basic on the Edit Unified Messaging Service page
		  in Unity Connection Administration.

### Configure IPsec
	 Policies Using FIPS Mode

For information on setting up IPsec policies, see the " IPSec Management "
		section in the "Security" chapter of the Cisco Unified
		  Communications Operating System Administration Guide for Cisco Unity Connection at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​os_administration/​b_​12xcucosagx.html

For information on
		setting up IPsec policies for Microsoft Exchange servers, consult the relevant
		Microsoft IPsec documentation at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​os_administration/​b_​12xcucosagx.html

### Unsupported
	 Features When Using FIPS Mode

The following Cisco Unity Connection features are not supported
		when FIPS mode is enabled:

- SpeechView Transcription
		  Service.

- SIP Digest Authentication
		  (configured for SIP Telephony Integrations).

- Video Messaging

## Configuring
	 Voicemail PIN For Touchtone Conversation Users To Sign-In

Enabling FIPS in Cisco Unity Connection prevents a touchtone
		conversation user from signing in to play or send voice messages or to change
		user settings if both of the following options are true:

- The user was created in
		  Cisco Unity 5.x or earlier, and migrated to Connection.

- The Unity Connection user
		  still has a voicemail PIN that was assigned in Cisco Unity 5.x or earlier.

A touchtone
		conversation user signs in by entering an ID (usually the user's extension) and
		a voicemail PIN. The ID and PIN are assigned when the user is created. Either
		an administrator or the user can change the PIN. To prevent administrators from
		accessing PINs in Connection Administration, PINs are hashed. In Cisco Unity
		5.x and earlier, Cisco Unity hashed the PIN by using an MD5 hashing algorithm,
		which is not FIPS compliant. In Cisco Unity 7.x and later, and in Unity
		Connection, the PIN is hashed by using an SHA-1 algorithm, which is much harder
		to decrypt and is FIPS compliant.

- Hashing All
	 Voicemail PIN with SHA-1 Algorithm in Unity Connection

- Replacing
	 MD5-hashed Voicemail PIN with SHA-1 Algorithm in Cisco Unity 5.x Or Earlier
	 Versions

### Hashing All
	 Voicemail PIN with SHA-1 Algorithm in Unity Connection

When FIPS is enabled, Cisco Unity Connection no longer checks
		the database to determine whether the user's voicemail PIN was hashed with MD5
		or SHA-1 algorithm. Unity Connection hashes all the voicemail PINs with SHA-1
		and compares it with the hashed PIN in the Unity Connection database. The user
		is not allowed to sign in if the MD5 hashed voicemail PIN entered by user does
		not match with the SHA-1 hashed voicemail PIN in the database.

### Replacing
	 MD5-hashed Voicemail PIN with SHA-1 Algorithm in Cisco Unity 5.x Or Earlier
	 Versions

For Unity Connection user accounts that were originally created
		in Cisco Unity 5.x or earlier, the voicemail PIN that might have been hashed
		with MD5 algorithm must be replaced with SHA-1 algorithm. Consider the
		following points while replacing the MD5-hashed passwords with SHA-1-hashed
		passwords:

- Use the latest version of
		  the User Data Dump utility to determine how many users still have MD5-hashed
		  PINs. For each user, the Pin_Hash_Type column contains either MD5 or SHA-1. To
		  download the latest version of the utility and to view the Help, see the User
		  Data Dump page on the Cisco Unity Tools website at http:/​/​ciscounitytools.com/​Applications/​CxN/​UserDataDump/​UserDataDump.html

- Run the Bulk Password Edit
		  utility if you still have users who have not changed their voicemail PINs. The
		  Bulk Password Edit utility lets you selectively change PINs to random values
		  and exports data on the changes to a.csv file. The export file includes the
		  name, alias, email address, and new PIN for each user who's PIN was changed.
		  You can use the.csv file to send an email to each user with the new PIN. The
		  utility is available on the Cisco Unity Tools website at http:/​/​www.ciscounitytools.com/​Applications/​CxN/​BulkPasswordEdit/​BulkPasswordEdit.html

| Caution | After enabling or disabling the FIPS mode, the Cisco Unity Connection server
		restart automatically. |
|---|---|

| Caution | If the Cisco Unity Connection server is in a cluster, do not change the FIPS
		settings on any other node until the FIPS operation on the current node is
		complete and the system is back up and running. |
|---|---|

| Note | In case of
		clusters, perform the following steps on all nodes. |
|---|---|

| Note | The
			 certificate must be saved as a file with the extension.pem rather than.htm,
			 else Cisco Unified CM will not recognize the certificate. |
|---|---|

| Note | Secure Messages are not sent in a FIPS compliant manner unless an
		IPsec Policy is configured. |
|---|---|

| Note | The administrator has the option to configure web-based
		authentication mode setting to NTLM in FIPS mode. Please note with this
		configuration Unified Messaging Interface becomes non-FIPS compliant. |
|---|---|

| Caution | The IPsec policy between servers is required to
		protect the plain text nature of Basic web authentication. |
|---|---|

| Note | The earlier
			 versions of the User Data Dump utility do not include the Pin_Hash_Type column. |
|---|---|