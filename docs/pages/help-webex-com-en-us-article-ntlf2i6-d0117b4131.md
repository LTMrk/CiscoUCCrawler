---
doc_id: help-webex-com-en-us-article-ntlf2i6-d0117b4131
source_url: https://help.webex.com/en-us/article/ntlf2i6
retrieved_at: 2026-11-02T13:10:56.680461+00:00
---

You can enable Cisco Unified Communications Manager to operate in an enhanced security environment. With these enhancements, your phone network operates under a set of strict security and risk management controls to protect you and your users.

The enhanced security environment includes the following features:

Contact search authentication (for Custom directories only)

TCP as the default protocol for remote audit logging

FIPS mode

An improved credentials policy

Support for the SHA-2 family of hashes for digital signatures

Support for a RSA key size of 512 bits and 4096 bits

With Cisco Unified Communications Manager Release 14.0 and Cisco Video Phone Firmware Release
      2.1 and later, the phones support SIP OAuth authentication.

OAuth is supported for Proxy Trivial File Transfer Protocol (TFTP) with Cisco Unified
      Communications Manager Release 14.0(1)SU1 or later. Proxy TFTP and OAuth for Proxy TFTP is not
      supported on Mobile Remote Access (MRA).

For additional information about security, see the following:

System Configuration Guide for Cisco Unified Communications Manager , Release 14.0(1) or later ( https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html ).

Security Guide for Cisco Unified Communications Manager ( https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html )

Your phone can only store a limited number of Identity Trust List (ITL) files. ITL files can't exceed 64K on the phone so limit the number of files that the Cisco Unified Communications Manager sends to the phone.

## Supported security features

Security features protect against threats, including threats to the identity of the phone and to data. These features establish and maintain authenticated communication streams between the phone and the Cisco Unified Communications Manager server, and ensure that the phone uses only digitally signed files.

Cisco Unified Communications Manager Release 8.5(1) and later includes Security by default, which provides the following security features for Cisco IP Phones without running the CTL client:

Signing of the
				phone configuration files

Phone
				configuration file encryption

HTTPS with Tomcat and other web services

Secure signaling
			 and media features still require you to run the CTL client and use hardware
			 eTokens.

Implementing
		  security in the Cisco Unified Communications Manager system prevents identity
		  theft of the phone and Cisco Unified Communications Manager server, prevents
		  data tampering, and prevents call signaling and media stream tampering.

To alleviate these
		  threats, the Cisco IP telephony network establishes and maintains secure
		  (encrypted) communication streams between a phone and the server, digitally
		  signs files before they are transferred to a phone, and encrypts media streams
		  and call signaling between Cisco IP Phones.

A Locally Significant Certificate (LSC) installs on phones after you perform the necessary tasks that are associated with the Certificate Authority Proxy Function (CAPF). You can use Cisco Unified Communications Manager Administration to configure an LSC, as described in the Cisco Unified Communications Manager Security Guide. Alternatively, you can initiate the installation of an LSC from the Security settings menu on the phone. This menu also lets you update or remove an LSC.

From PhoneOS 3.2 release, an LSC can be used as the user certificate for EAP-TLS with WLAN authentication.

The phones use the phone security profile, which
		  defines whether the device is nonsecure or secure. For information about
		  applying the security profile to the phone, see the documentation for your particular Cisco Unified Communications Manager release.

If you configure
		  security-related settings in Cisco Unified Communications Manager
		  Administration, the phone configuration file contains sensitive information. To
		  ensure the privacy of a configuration file, you must configure it for
		  encryption. For detailed information, see the 
		  documentation for your particular Cisco Unified Communications Manager release.

The phone complies with Federal Information Processing Standard (FIPS). To function correctly, FIPS mode requires a key size of 2048 bits or greater. If the certificate is less than 2048 bits, the phone won’t register with Cisco Unified Communications Manager and Phone failed to register. Cert key size is not FIPS compliant displays on the phone.

If the phone has an LSC, you need to update the LSC key size to 2048 bits or greater before enabling FIPS.

The
		  following table provides an overview of the security features that the phones
		  support. For more information, see the documentation for your particular Cisco Unified Communications Manager release.

To view the Security mode, press Settings and navigate to Network and service > Security settings .

Feature

Description

Image
					 authentication

Signed binary files prevent tampering with the firmware image before the image is loaded on a phone.

Tampering
					 with the image causes a phone to fail the authentication process and reject the
					 new image.

Customer
					 site certificate installation

Each Cisco IP Phone requires a unique certificate for device authentication. Phones include a manufacturing installed certificate (MIC), but for extra security, you can specify certificate installation in Cisco Unified Communications Manager Administration using the Certificate Authority Proxy Function (CAPF). Alternatively, you can install a Locally Significant Certificate (LSC) from the Security Configuration menu on the phone.

Device
					 authentication

Occurs between the Cisco Unified Communications Manager server and the phone when each entity accepts the certificate of the other entity. Determines whether a secure connection between the phone and a Cisco Unified Communications Manager should occur; and, if necessary, creates a secure signaling path between the entities by using TLS protocol. Cisco Unified Communications Manager doesn’t register phones unless it can authenticate them.

File
					 authentication

Validates digitally signed files that the phone downloads. The phone validates the signature to make sure that file tampering didn’t occur after file creation. Files that fail authentication aren’t written to Flash memory on the phone. The phone rejects such files without further processing.

File
					 encryption

Encryption prevents sensitive information from being revealed while the file is in transit to the phone. In addition, the phone validates the signature to make sure that file tampering didn’t occur after file creation. Files that fail authentication aren’t written to Flash memory on the phone. The phone rejects such files without further processing.

Signaling
					 authentication

Uses the
					 TLS protocol to validate that no tampering to signaling packets has occurred
					 during transmission.

Manufacturing installed certificate

Each Cisco
					 IP Phone contains a unique manufacturing installed certificate (MIC), which is
					 used for device authentication. The MIC provides permanent unique proof of
					 identity for the phone and allows Cisco Unified Communications Manager to
					 authenticate the phone.

Media
					 encryption

Uses SRTP to ensure that media streams between supported devices prove secure and that only
									the intended device receives and reads the data. Includes
									creating a media primary key pair for the devices, delivering
									the keys to the devices, and securing the delivery of the keys
									while the keys are in transport.

CAPF
					 (Certificate Authority Proxy Function)

Implements parts of the certificate generation procedure that are too processing-intensive for the phone, and interacts with the phone for key generation and certificate installation. The CAPF can be configured to request certificates from customer-specified certificate authorities on behalf of the phone, or it can be configured to generate certificates locally.

Both EC (Elliptical Curve) and RSA key types are supported. To use the EC key, make sure that the parameter "Endpoint Advanced Encryption Algorithms Support" (from System > Enterprise parameter ) is enabled.

For more information about CAPF and related configurations, see the following documents:

- Security Guide for Cisco Unified Communications Manager

- CUCM Third-Party CA-Signed LSCs Generation and Import Configuration Example

- Configure Automatic Certificate Enrollment and Renewal Via CAPF Online CA

Security
					 profile

Defines
					 whether the phone is nonsecure, authenticated, encrypted, or protected. Other
					 entries in this table describe security features.

Encrypted
					 configuration files

Lets you
					 ensure the privacy of phone configuration files.

Optional
					 web server disabling for a phone

For security purposes, you can prevent access to the web pages for a phone (which display various operational statistics for the phone) and Self Care Portal.

Phone
					 hardening

Additional security options, which you control from Cisco
					 Unified Communications Manager Administration:

- Disabling PC port

- Disabling Gratuitous ARP
						(GARP)

- Disabling PC Voice VLAN
						access

- Disabling access to the Setting menu or providing restricted access

- Disabling access to web pages for a phone

- Disabling Bluetooth
						Accessory Port

- Restricting TLS ciphers

802.1X
					 Authentication

The Cisco IP Phone can use 802.1X authentication to request and gain access to the network. See 802.1X Authentication for more information.

Secure
					 SIP Failover for SRST

After
					 you configure a Survivable Remote Site Telephony (SRST) reference for security
					 and then reset the dependent devices in Cisco Unified Communications Manager
					 Administration, the TFTP server adds the SRST certificate to the phone cnf.xml
					 file and sends the file to the phone. A secure phone then uses a TLS connection
					 to interact with the SRST-enabled router.

Signaling encryption

Ensures
					 that all SIP signaling messages that are sent between the device and the Cisco
					 Unified Communications Manager server are encrypted.

Trust List update alarm

When the Trust List updates on the phone, the Cisco Unified Communications Manager receives an alarm to indicate the success or failure of the update. See the following table for more information.

AES 256 Encryption

When connected to Cisco Unified Communications Manager Release 10.5(2) and later, the phones support AES 256 encryption support for TLS and SIP for signaling and media encryption. This enables phones to initiate and support TLS 1.2 connections using AES-256 based ciphers that conform to SHA-2 (Secure Hash Algorithm) standards and are Federal Information Processing Standards (FIPS) compliant. The ciphers include:

- TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

- TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

- AEAD_AES_256_GCM

- AEAD_AES_128_GCM

For more information, see the Cisco Unified Communications Manager documentation.

Elliptic Curve Digital Signature Algorithm (ECDSA) certificates

As part of Common Criteria (CC) certification, Cisco Unified Communications Manager; added ECDSA certificates in version 11.0. This affects all Voice Operating System (VOS) products running CUCM 11.5 and later versions.

Multi-server (SAN) Tomcat Certificate with Cisco UCM

For more information about the feature, see the following:

- How To Configure Multi-server (SAN) Tomcat certificate with Cisco UCM

- Security Guide for Cisco Unified Communications Manager

The following table contains the Trust List update alarm messages and meaning. For more information, see the Cisco Unified Communications Manager documentation.

1 - TL_SUCCESS

Received new CTL and/or ITL

2 - CTL_INITIAL_SUCCESS

Received new CTL, no existing TL

3 - ITL_INITIAL_SUCCESS

Received new ITL, no existing TL

4 - TL_INITIAL_SUCCESS

Received new CTL and ITL, no existing TL

5 - TL_FAILED_OLD_CTL

Update to new CTL failed, but have previous TL

6 - TL_FAILED_NO_TL

Update to new TL failed, and have no old TL

7 - TL_FAILED

Generic failure

8 - TL_FAILED_OLD_ITL

Update to new ITL failed, but have previous TL

9 - TL_FAILED_OLD_TL

Update to new TL failed, but have previous TL

The
		  Security Setup menu provides information about various security settings. The
		  menu also provides access to the Trust List menu and indicates whether the CTL
		  or ITL file is installed on the phone.

The
		  following table describes the options in the Security Setup menu.

Option

Description

To
					 Change

Security
					 Mode

Displays
					 the security mode that is set for the phone.

From
					 Cisco Unified Communications Manager Administration, choose Device > Phone . The setting appears in the
					 Protocol Specific Information portion of the Phone Configuration window.

LSC

Indicates whether a locally significant certificate that is used for security features is installed on the phone (Installed) or isn’t installed on the phone (Not installed).

For
					 information about how to manage the LSC for your phone, see the 
					 documentation for your particular Cisco Unified Communications Manager release.

## Set up a Locally Significant Certificate (LSC)

This task applies to setting up a LSC with the authentication string method.

Before you begin

Make sure that the appropriate Cisco Unified Communications
		  Manager and the Certificate Authority Proxy Function (CAPF) security
		  configurations are complete:

The CTL or ITL file has a
			 CAPF certificate.

In Cisco Unified
			 Communications Operating System Administration, verify that the CAPF
			 certificate is installed.

The CAPF is running and
			 configured.

For more information about these settings, see the 
					 documentation for your particular Cisco Unified Communications Manager release.

Obtain the CAPF authentication code that was set when the CAPF was
			 configured.

On the phone, press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Navigate to Network and Service > Security settings > LSC .

You can control access to the Settings menu by using the Settings Access field in Cisco Unified Communications Manager Administration.

Enter the authentication string and select Submit .

The phone begins to install, update, or remove the LSC, depending on how the CAPF is configured. When the procedure is complete, Installed or Not Installed displays on the phone.

The LSC install, update, or removal process can take a long time to complete.

When the phone installation procedure is successful, the Installed message displays. If the phone displays Not Installed , then the authorization string may be incorrect or the phone upgrade may not be enabled. If the CAPF operation deletes the LSC, the phone displays Not Installed to indicate that the operation succeeded. The CAPF server logs the error messages. See the CAPF server documentation to locate the logs and to understand the meaning of the error messages.

## Enable FIPS mode

In Cisco Unified Communications Manager Administration, select Device > Phone and locate the phone.

Navigate to the Product Specific Configuration area.

Set the FIPS Mode field to Enabled .

Select Save .

Select Apply Config .

Restart the phone.

## Turn off speakerphone, headset, and handset on a phone

You have the options to permanently turn off the speakerphone, headset, and handset on a phone for your user.

In Cisco Unified Communications Manager Administration, select Device > Phone and locate the phone.

Navigate to the Product Specific Configuration area.

Check one or more of the following check boxes to turn off the capabilities of the phone:

- Disable Speakerphone

- Disable Speakerphone and Headset

- Disable Handset

By default, these check boxes are unchecked.

Select Save .

Select Apply Config .

## 802.1X
	 Authentication

The Cisco IP
		  Phones support 802.1X Authentication.

Cisco IP Phones and Cisco Catalyst switches traditionally use Cisco Discovery Protocol (CDP) to identify each other and determine parameters such as VLAN allocation and inline power requirements. CDP doesn’t identify locally attached workstations. Cisco IP Phones provide an EAPOL pass-through mechanism. This mechanism allows a workstation attached to the Cisco IP Phone to pass EAPOL messages to the 802.1X authenticator at the LAN switch. The pass-through mechanism ensures that the IP phone doesn’t act as the LAN switch to authenticate a data endpoint before accessing the network.

Cisco IP Phones also provide a proxy EAPOL Logoff mechanism. If the locally attached PC disconnects from the IP phone, the LAN switch doesn’t see the physical link fail, because the link between the LAN switch and the IP phone is maintained. To avoid compromising network integrity, the IP phone sends an EAPOL-Logoff message to the switch on behalf of the downstream PC, which triggers the LAN switch to clear the authentication entry for the downstream PC.

Support
		  for 802.1X authentication requires several components:

Cisco IP Phone: The phone initiates the request to access the network. Cisco IP Phones contain an 802.1X supplicant. This supplicant allows network administrators to control the connectivity of IP phones to the LAN switch ports. The current release of the phone 802.1X supplicant uses the EAP-FAST and EAP-TLS options for network authentication.

Authentication server: The authentication server and the switch must both be configured with a shared secret that authenticates the phone.

Switch: The switch must support 802.1X, so it can act as the authenticator and pass the messages between the phone and the authentication server. After the exchange completes, the switch grants or denies the phone access to the network.

You must perform
		  the following actions to configure 802.1X.

Configure the
				other components before you enable 802.1X Authentication on the phone.

Configure PC Port: The 802.1X standard doesn’t consider VLANs and thus recommends that only a single device should be authenticated to a specific switch port. However, some switches support multidomain authentication. The switch configuration determines whether you can connect a PC to the PC port of the phone.

Enabled: If you’re using a switch that supports multidomain authentication, you can enable the PC port and connect a PC to it. In this case, Cisco IP Phones support proxy EAPOL-Logoff to monitor the authentication exchanges between the switch and the attached PC.

For more information about IEEE 802.1X support on the Cisco Catalyst switches, see the Cisco Catalyst switch configuration guides at:

http://www.cisco.com/en/US/products/hw/switches/ps708/tsd_products_support_series_home.html

Disabled: If the switch doesn’t support multiple 802.1X-compliant devices on the same port, you should disable the PC Port when 802.1X authentication is enabled. If you don’t disable this port and then attempt to attach a PC to it, the switch denies network access to both the phone and the PC.

- Enabled: If you’re using a switch that supports multidomain authentication, you can continue it to use the voice VLAN.

- Disabled: If the switch doesn’t support multidomain authentication, disable the Voice VLAN and consider assigning the port to the native VLAN.

Cisco Desk Phone 9800 Series has a different prefix in the PID from that for the other Cisco phones. To enable your phone to pass 802.1X authentication, set the Radius·User-Name parameter to include your Cisco Desk Phone 9800 Series.

For example, the PID of phone 9841 is DP-9841; you can set Radius·User-Name to Start with DP or Contains DP . You can set it in both of the following sections:

Policy > Conditions > Library Conditions

Policy > Policy Sets > Authorization Policy > Authorization Rule 1

### Enable 802.1X authentication

You can enable 802.1X authentication for your phone by following these steps:

Press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Navigate to Network and service > Security settings > 802.1X Authentication .

Turn on IEEE 802.1X authentication.

Select Apply .

## View information about security settings on phone

You can view the information about the security settings in the phone menu. The availability of the information depends on the network settings in your organization.

Parameters

Description

Security Mode

Displays the security mode that is set for the phone.

LSC

Indicates whether a locally significant certificate that is used for security features is installed on the phone (Yes) or is not installed on the phone (No).

Trust List

The Trust List provides submenus for the CTL, ITL, and Signed Configuration files.

The CTL File submenu displays the contents of the CTL file. The ITL File submenu displays contents of the ITL file.

The Trust List menu also displays the following information:

- CTL Signature: the SHA1 hash of the CTL file

- Unified CM/TFTP Server: the name of the Cisco Unified Communications Manager and TFTP Server that the phone uses. Displays a certificate icon if a certificate is installed for this server.

- CAPF Server: the name of the CAPF server that the phone uses. Displays a certificate icon if a certificate is installed for this server.

- SRST Router: the IP address of the trusted SRST router that the phone can use. Displays a certificate icon if a certificate is installed for this server.

For details, see 802.1X Authentication .

Determines whether the oldest version of Wi-Fi Protected Access (WPA) is compatible on the phone to connect to a wireless network or access point (AP).

- If enabled, the phone can search and connect to wireless networks with all versions of WPA supported, including WPA, WPA2, and WPA3. In addition, the phone can search and connect to APs that only support the oldest version of WPA.

- If disabled (default), the phone can only search and connect to the wireless networks and APs that support WPA2 and WPA3.

This feature is only available on 9861/9871/8875 phones.

Press Settings .

Navigate to Network and service > Security settings .

In the Security settings , view the security information.

## Phone call security

When security is implemented for a phone, you can identify secure phone calls by icons on the phone screen. You can also determine whether the connected phone is secure and protected if a security tone plays at the beginning of the call.

In a secure call, all call signaling and media streams are encrypted. A secure call offers a high level of security, providing integrity and privacy to the call. When a call in progress is encrypted, you can see the secure icon on the line. For a secure phone, you can also view the authenticated icon or the encrypted icon next to the connected server in the phone menu ( Settings > About this device ).

If the call is routed through non-IP call legs, for example, PSTN, the call may be nonsecure even though it is encrypted within the IP network and has a lock icon associated with it.

In a secure call, a security tone plays at the beginning of a call to indicate that the other connected phone is also receiving and transmitting secure audio. If your call connects to a nonsecure phone, the security tone does not play.

Secure calling is supported for connections between two phones only. Some features, such as conference calling and shared lines, are not available when secure calling is configured.

When a phone is configured as secure (encrypted and trusted) in Cisco Unified Communications Manager, it can be given a protected status. After that, if desired, the protected phone can be configured to play an indication tone at the beginning of a call:

Protected Device: To change the status of a secure phone to protected, check the Protected Device check box in the Phone Configuration window in Cisco Unified Communications Manager Administration ( Device > Phone ).

Play Secure Indication Tone: To enable the protected phone to play a secure or nonsecure indication tone, set the Play Secure Indication Tone setting to True. By default, Play Secure Indication Tone is set to False. You set this option in Cisco Unified Communications Manager Administration ( System > Service Parameters ). Select the server and then the Unified Communications Manager service. In the Service Parameter Configuration window, select the option in the Feature - Secure Tone area. The default is False.

### Secure Conference
	 Call Identification

You can
		initiate a secure conference call and monitor the security level of
		participants. A secure conference call is established by using this process:

A user initiates
			 the conference from a secure phone.

Cisco Unified
			 Communications Manager assigns a secure conference bridge to the call.

As participants
			 are added, Cisco Unified Communications Manager verifies the security mode of
			 each phone and maintains the secure level for the conference.

The phone displays the security level of the conference call. A secure conference displays the secure icon .

Secure calling is supported between two phones. For protected phones, some features, such as conference calling, shared lines, and Extension Mobility, are not available when secure calling is configured.

The
		following table provides information about changes to conference security
		levels depending on the initiator phone security level, the security levels of
		participants, and the availability of secure conference bridges.

Initiator Phone Security Level

Feature Used

Security Level of Participants

Results of Action

Nonsecure

Conference

Secure

Nonsecure
				conference bridge

Nonsecure
				conference

Secure

Conference

At least one
				member is nonsecure.

Secure
				conference bridge

Nonsecure
				conference

Secure

Conference

Secure

Secure
				conference bridge

Secure
				encrypted level conference

Nonsecure

Meet Me

Minimum
				security level is encrypted.

Initiator
				receives message Does not meet Security Level, call rejected .

Secure

Meet Me

Minimum
				security level is nonsecure.

Secure
				conference bridge

Conference
				accepts all calls.

### Secure phone call identification

A secure call is established when your phone, and the phone on the other end, is configured for secure calling. The other phone can be in the same Cisco IP network, or on a network outside the IP network. Secured calls can only be made between two phones. Conference calls should support secure call after secure conference bridge set up.

A secured call is established using this process:

A user initiates the call from a secured phone (secured security mode).

The phone displays the secure icon on the phone screen. This icon indicates that the phone is configured for secure calls, but this does not mean that the other connected phone is also secured.

The user hears a security tone if the call connects to another secured phone, indicating that both ends of the conversation are encrypted and secured. If the call connects to a nonsecure phone, the user does not hear the security tone.

Secure calling is supported between two phones. For protected phones, some features, such as conference calling, shared lines, and Extension Mobility, are not available when secure calling is configured.

Only protected phones play these secure or nonsecure indication tones. Nonprotected phones never play tones. If the overall call status changes during the call, the indication tone changes and the protected phone plays the appropriate tone.

A protected phone plays a tone or not under these circumstances:

When the Play Secure Indication Tone option is enabled:

When end-to-end secure media is established and the call status is secure, the phone plays the secure indication tone (three long beeps with pauses).

When end-to-end nonsecure media is established and the call status is nonsecure, the phone plays the nonsecure indication tone (six short beeps with brief pauses).

If the Play Secure Indication Tone option is disabled, no tone plays.

### Provide encryption for barge

Cisco Unified Communications Manager checks the phone security status when conferences are
        established and changes the security indication for the conference or blocks the completion
        of the call to maintain integrity and security in the system.

A user cannot barge into an encrypted call if the phone that is used to barge is not
        configured for encryption. When barge fails in this case, a reorder (fast busy) tone plays
        on the phone that the barge was initiated.

If the initiator phone is configured for encryption, the barge initiator can barge into a
        nonsecure call from the encrypted phone. After the barge occurs, Cisco Unified
        Communications Manager classifies the call as nonsecure.

If the initiator phone is configured for encryption, the barge initiator can barge into an
        encrypted call, and the phone indicates that the call is encrypted.

## WLAN security

Because all WLAN devices that are within range can receive all other WLAN traffic, securing voice communications is critical in WLANs. To ensure that intruders don’t manipulate nor intercept voice traffic, the Cisco SAFE Security architecture supports the phone. For more information about security in networks, see http://www.cisco.com/en/US/netsol/ns744/networking_solutions_program_home.html.

The Cisco Wireless IP telephony solution provides wireless network security that prevents unauthorized sign-ins and compromised communications by using the following authentication methods that the phone supports:

Open Authentication : Any wireless device can request authentication in an open system. The AP that receives the request may grant authentication to any requestor or only to requestors that are found on a list of users. Communication between the wireless device and Access Point (AP) could be nonencrypted.

Extensible Authentication Protocol-Flexible Authentication via Secure Tunneling (EAP-FAST) Authentication : This client-server security architecture encrypts EAP transactions within a Transport Level Security (TLS) tunnel between the AP and the RADIUS server, such as Identity Services Engine (ISE).

The TLS tunnel uses Protected Access Credentials (PACs) for authentication between the client (phone) and the RADIUS server. The server sends an Authority ID (AID) to the client (phone), which in turn selects the appropriate PAC. The client (phone) returns a PAC-Opaque to the RADIUS server. The server decrypts the PAC with the primary key. Both endpoints now contain the PAC key and a TLS tunnel is created. EAP-FAST supports automatic PAC provisioning, but you must enable it on the RADIUS server.

In ISE, by default, the PAC expires in one week. If the phone has an expired PAC, authentication with the RADIUS server takes longer while the phone gets a new PAC. To avoid PAC provisioning delays, set the PAC expiration period to 90 days or longer on the ISE or RADIUS server.

Extensible Authentication Protocol-Transport Layer Security (EAP-TLS) Authentication : EAP-TLS requires a client certificate for authentication and network access. For wireless EAP-TLS, the client certificate can be MIC, LSC, or user-installed certificate.

Protected Extensible Authentication Protocol (PEAP) : Cisco proprietary password-based mutual authentication scheme between the client (phone) and a RADIUS server. The phone can use PEAP for authentication with the wireless network. Both PEAP-MSCHAPV2 and PEAP-GTC authentication methods are supported.

Pre-Shared Key (PSK) : The phone supports ASCII format. You must use this format when setting up a WPA/WPA2/SAE Pre-shared key:

ASCII : an ASCII-character string with 8 to 63 characters in length (0-9, lowercase and uppercase A-Z, and special characters)

Example : GREG123567@9ZX&W

The following authentication schemes use the RADIUS server to manage authentication keys:

WPA/WPA2/WPA3: Uses RADIUS server information to generate unique keys for authentication. Because these keys are generated at the centralized RADIUS server, WPA2/WPA3 provides more security than WPA preshared keys that are stored on the AP and phone.

Fast Secure Roaming: Uses RADIUS server and a wireless domain server (WDS) information to manage and authenticate keys. The WDS creates a cache of security credentials for FT-enabled client devices for fast and secure reauthentication. Cisco Desk Phone 9861 and 9871 and Cisco Video Phone 8875 support 802.11r (FT). Both over the air and over the DS are supported to allow for fast secure roaming. But we strongly recommend utilizing the 802.11r (FT) over air method.

With WPA/WPA2/WPA3, encryption keys aren’t entered on the phone, but are automatically derived between the AP and phone. But the EAP username and password that are used for authentication must be entered on each phone.

To ensure that voice traffic is secure, the phone supports TKIP and AES for encryption. When these mechanisms are used for encryption, both the signaling SIP packets and voice Real-Time Transport Protocol (RTP) packets are encrypted between the AP and the phone.

WPA uses TKIP encryption that has several improvements over WEP. TKIP provides per-packet key ciphering and longer initialization vectors (IVs) that strengthen encryption. In addition, a message integrity check (MIC) ensures that encrypted packets aren’t being altered. TKIP removes the predictability of WEP that helps intruders decipher the WEP key.

An encryption method used for WPA2/WPA3 authentication. This national standard for encryption uses a symmetrical algorithm that has the same key for encryption and decryption. AES uses Cipher Blocking Chain (CBC) encryption of 128 bits in size, which supports key sizes of 128 bits, 192 bits and 256 bits, as a minimum. The phone supports a key size of 256 bits.

Cisco Desk Phone 9861 and 9871 and Cisco Video Phone 8875 don't support Cisco Key Integrity Protocol (CKIP) with CMIC.

Authentication and encryption schemes are set up within the wireless LAN. VLANs are configured in the network and on the APs and specify different combinations of authentication and encryption. An SSID associates with a VLAN and the particular authentication and encryption scheme. For wireless client devices to authenticate successfully, you must configure the same SSIDs with their authentication and encryption schemes on the APs and on the phone.

Some authentication schemes require specific types of encryption.

- When you use WPA pre-shared key, WPA2 pre-shared key, or SAE, the pre-shared key must be statically set on the phone. These keys must match the keys that are on the AP.

The phone supports auto EAP negotiation for FAST or PEAP, but not for TLS. For EAP-TLS mode, you must specify it.

The authentication and encryption schemes in the following table shows the network configuration options for the phone that corresponds to AP configuration.

WPA-PSK

WPA-PSK-SHA256

FT-PSK

SAE

FT-SAE

WPA-EAP

FT-EAP

WPA-EAP-SHA256

FT-EAP

WPA-EAP

FT-EAP

WPA-EAP-SHA256

FT-EAP

WPA-EAP

FT-EAP

WPA-EAP-SHA256

FT-EAP

### Configure Wireless LAN profile

You can manage your wireless network profile by configuring credentials, frequency band,  authentication method, and so on.

Keep the following notes in mind before you configure the WLAN profile:

When your network uses EAP-FAST and PEAP for user authentication, you must configure both the username and password if required on the Remote Authentication Dial-In User Service (RADIUS) and the phone.

- The credentials that you enter in the wireless LAN profile must be identical with the credentials that you configured on the RADIUS server.

If you use domains within your network, you must enter the username with the domain name, in the format: domain\username .

The following actions could result in the existing Wi-Fi password being cleared:

- Entering an invalid user id or password

- Installing an invalid or expired Root CA when the EAP type is set to PEAP-MSCHAPV2 or PEAP-GTC

- Disabling the in-use EAP type on the RADIUS server before switching the phone to the new EAP type

- To change the EAP type, make sure that you enable the new EAP type on the RADIUS server first, then switch the phone to the EAP type. When all the phones have been changed to the new EAP type, you can disable the previous EAP type if you want.

In Cisco Unified Communications Manager Administration, select Device > Device Settings > Wireless LAN Profile .

Choose the network profile that you want to configure.

Set up the parameters.

Click Save .

### Configure the SCEP parameters

Simple Certificate Enrollment Protocol (SCEP) is the standard for automatically provisioning and renewing certificates. The SCEP server can automatically maintain your user and server certificates.

You must configure the following SCEP parameters on your phone web page

RA IP
address

SHA-1 or SHA-256 fingerprint of the root CA certificate for the SCEP server

The Cisco IOS Registration Authority (RA) serves as a proxy to the SCEP server. The SCEP client on the phone use the parameters that are  downloaded from Cisco Unified Communication Manager. After you configure the parameters, the phone sends a SCEP getcs request to the  RA and the
root CA certificate is validated using the defined fingerprint.

Before you begin

On the SCEP server, configure the SCEP Registration Agent (RA) to:

- Act as a PKI trust point

- Act as a PKI RA

- Perform device authentication using a RADIUS server

For more information, see your SCEP server documentation.

From the Cisco Unified Communications Manager Administration, select Device > Phone .

Locate the phone.

Scroll to the Product Specific Configuration Layout area.

Enter the RA IP address or hostname in the WLAN SCEP Server field, and then select the check box to activate the SCEP parameter.

Enter the SHA-1 or SHA-256 fingerprint of the root CA certificate in the WLAN Root CA Fingerprint (SHA256 or SHA1) field, and then select
          check box to activate the SCEP QED parameter.

Select Save .

Select Apply Config .

## Set up the supported versions of TLS

You can set up the minimum version of TLS required for client and server respectively.

By default, the minimum TLS version of server and client is both 1.2. The setting has impacts on the following functions:

- HTTPS web access connection

- Onboarding for on-premises phone

- Onboarding for Mobile and Remote Access (MRA)

- HTTPS services, such as, the Directory services

- Datagram Transport Layer Security (DTLS)

- Port Access Entity (PAE)

- Extensible Authentication Protocol-Transport Layer Security (EAP-TLS)

For more information about the TLS 1.3 compatibility for Cisco IP Phones, see TLS 1.3 Compatibility Matrix for Cisco Collaboration Products .

Sign into Cisco Unified Communications Manager Administration as an administrator.

Navigate to one of the following windows:

- System > Enterprise Phone Configuration

- Device > Device Settings > Common Phone Profile

- Device > Phone > Phone Configuration

Set up the TLS Client Min Version field:

The "TLS 1.3" option is available on Cisco Unified CM 15SU2, or later.

If the TLS version in server is lower than 1.1, for example, 1.0, then the connection can't be established.

If the TLS version in server is lower than 1.2, for example, 1.1 or 1.0, then the connection can't be established.

If  the TLS version in server is lower than 1.3, for example, 1.2, 1.1 or 1.0, then the connection can't be established.

Set up the TLS Server Min Version field:

If the TLS version in client is lower than 1.1, for example, 1.0, then the connection can't be established.

If the TLS version in client is lower than 1.2, for example, 1.1 or 1.0, then the connection can't be established.

If  the TLS version in client is lower than 1.3, for example, 1.2, 1.1 or 1.0, then the connection can't be established.

From PhoneOS 3.2 release, the setting of the field "Disable TLS 1.0 and TLS 1.1 for Web Access" doesn't take affect on the phones.

Click Save .

Click Apply Config .

Restart the phones.

## Assured Services SIP

Assured Services SIP(AS-SIP) is a collection of features and protocols that offer a highly secure call flow for Cisco IP Phones and third-party phones. The following features are collectively known as AS-SIP:

- Multilevel Precedence and Preemption (MLPP)

- Differentiated Services Code Point (DSCP)

- Transport Layer Security (TLS) and Secure Real-time Transport Protocol (SRTP)

- Internet Protocol version 6 (IPv6)

AS-SIP is often used with Multilevel Precedence and Preemption (MLPP) to prioritize calls during an emergency. With MLPP, you assign a priority level to your outgoing calls, from level 1 (low) to level 5 (high). When you receive a call, a precedence level icon displays on the phone that shows the call priority.

To configure AS-SIP, complete the following tasks on Cisco Unified Communications Manager:

- Configure a Digest User—Configure the end user to use digest authentication for SIP requests.

- Configure SIP Phone Secure Port—Cisco Unified Communications Manager uses this port to listen to SIP phones for SIP line registrations over TLS.

- Restart Services—After configuring the secure port, restart the Cisco Unified Communications Manager and Cisco CTL Provider services. Configure SIP Profile for AS-SIP-Configure a SIP profile with SIP settings for your AS-SIP endpoints and for your SIP trunks. The phone-specific parameters are not downloaded to a third-party AS-SIP phone. They are used only by Cisco Unified Manager. Third-party phones must locally configure the same settings.

- Configure Phone Security Profile for AS-SIP—You can use the phone security profile to assign security settings such as TLS, SRTP, and digest authentication.

- Configure AS-SIP Endpoint—Configure a Cisco IP Phone or a third-party endpoint with AS-SIP support.

- Associate Device with End User—Associate the endpoint with a user.

- Configure SIP Trunk Security Profile for AS-SIP—You can use the sip trunk security profile to assign security features such as TLS or digest authentication to a SIP trunk.

- Configure SIP Trunk for AS-SIP—Configure a SIP trunk with AS-SIP support.

- Configure AS-SIP Features—Configure additional AS-SIP features such as MLPP, TLS, V.150, and IPv6.

For detailed information about configuring AS-SIP, see the "Configure AS-SIP Endpoints" chapter in Feature Configuration Guide for Cisco Unified Communications Manager .

### Multilevel Precedence and Preemption

Multilevel Precedence and Preemption (MLPP) allows you to prioritize calls during emergencies or other crisis situations. You assign a priority to your outgoing calls that range from 1 to 5. Incoming calls display an icon and the call priority. Authenticated users can preempt calls either to targeted stations or through fully subscribed TDM trunks.

This capability assures high-ranking personnel of communication to critical organizations and personnel.

If the dialed number is manipulated by a translation/route pattern that is configured on Unified CM, the MLPP call initiator can also see the MLPP special icon and precedence level on the phone screen and can hear the ringback tone. This behavior is achieved after the PhoneOS 3.4 release.

The MLPP feature for PhoneOS phones requires Unified CM Release 15SU3 or later.

#### MLPP configuration on Unified CM

To configure the feature, do the following:

- From Cisco Unified CM Administration, select System > MLPP > Domain > MLPP Domain , add new MLPP domains.

- Select System > MLPP > Namespace > Resource Priority Namespace Network Domain ,  add registered namespaces such as "drsn", "dsn", "cuc", "uc", "q735". Then choose one domain name to be the default.

- Select System > MLPP > Namespace > Resource Priority Namespace List , add namespace lists.

- Select Device > Device Settings > SIP Profile , add a new SIP profile.

- Check the MLPP User Authorization check box if you want the phone to require user credentials for MLPP calls.

- Select the configured resource priority namespace from Resource Priority Namespace .

- Select the configured namespace list from Resource Priority Namespace List .

- Select Device > Phone , update or add a phone.

- Select the configured SIP profile from SIP Profile .

- Under the section MLPP and Confidential Access Level Information , configure the parameters MLPP Domain , MLPP Indication , and MLPP Preemption .

- Select Device > Phone , add or update a line.

- Under the section MLPP Alternate Party And Confidential Access Level Settings , configure the parameters Target (Destination) , MLPP Calling Search Space , and MLPP No Answer Ring Duration (seconds) .

- Under the section Multiple Call/Call Waiting Settings , configure the parameter Busy Trigger .

- Select User Management > End User , add a new one.

- Click Device Association to associate the user with the configured phone.

- Under the section Mutilevel Precedence and Preemption Authorization , configure the parameters.

- Select System > Service Parameter . Configure the parameters under the section Clusterwide Parameters (Feature - Multilevel Precedence and Preemption) .

- Select System > Service Parameter . Configure DSCP for priority calls under the section Clusterwide Parameters (System - QOS) .

- Select System > Service Parameter .  Configure MLPP priority to SRVP priority mapping under the section Clusterwide Parameters (System - RSVP) .

- Configure router patterns from Call Routing > Route/Hunt > Router Pattern .

- Configure hunt pilots from Call Routing > Route/Hunt > Hunt Pilot .

- Configure translation patterns from Call Routing > Translation Pattern .

- Configure gateways, trunks, the default device profile, a user device profile, a common device configuration for MLPP.

MLPP is often used with Assured Services SIP(AS-SIP). For detailed information about configuring MLPP, see the chapter Configure Multilevel Precedence and Preemption in Feature Configuration Guide for Cisco Unified Communications Manager .

## Set up FAC and CMC

When the Forced Authorization Codes (FAC) or Client Matter Codes (CMC), or both are configured on the phone, the users must enter the required passwords to dial out a number.

For more information about how to set up FAC and CMC in Cisco Unified Communications Manager, see the " Client Matter Codes and Forced Authorization Codes " chapter in Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1) or later .

## VPN configuration

The Cisco VPN feature helps you to preserve network security while giving users a safe, reliable method to connect to your corporate network. Use this feature when:

- A phone is located outside a trusted network

- Network traffic between the phone and Cisco Unified Communications Manager crosses an untrusted network

With a VPN, there are three common approaches to client authentication:

- Digital certificates

- Passwords

- Username and password

Each method has its advantages. But if your corporate security policy permits it, we recommend a certificate-based approach because certificates allow for a seamless sign-in without any user intervention. Both LSC and MIC certificates are supported.

To configure any of the VPN features, provision the device on-premises first and then you can deploy the device off-premise.

For more information about certification authentication and working with VPN network, see Configure AnyConnect VPN Phone with Certificate Authentication on an ASA .

With a password, or username and password approach a user is prompted for sign-in credentials. Set the user sign-in credentials in accordance with your company security policy. You can also configure the Enable Password Persistence setting so that the user password is saved on the phone. The user password is saved until either a failed log-in attempt occurs, a user manually clears the password, or the phone resets or loses power.

Another useful tool is the Enable Auto Network Detect setting. When you enable this check box, the VPN client can only run when it detects that it is outside the corporate network. This setting is disabled by default.

Your Cisco phone supports Cisco SVC IPPhone Client v1.0 as the client type.

For more information about how to configure VPN on Unified CM, see Feature Configuration Guide for Cisco Unified Communications Manager .

The Cisco VPN feature uses Secure Sockets Layer (SSL) to preserve network security.

| Feature | Description |
|---|---|
| Image
					 authentication | Signed binary files prevent tampering with the firmware image before the image is loaded on a phone. Tampering
					 with the image causes a phone to fail the authentication process and reject the
					 new image. |
| Customer
					 site certificate installation | Each Cisco IP Phone requires a unique certificate for device authentication. Phones include a manufacturing installed certificate (MIC), but for extra security, you can specify certificate installation in Cisco Unified Communications Manager Administration using the Certificate Authority Proxy Function (CAPF). Alternatively, you can install a Locally Significant Certificate (LSC) from the Security Configuration menu on the phone. |
| Device
					 authentication | Occurs between the Cisco Unified Communications Manager server and the phone when each entity accepts the certificate of the other entity. Determines whether a secure connection between the phone and a Cisco Unified Communications Manager should occur; and, if necessary, creates a secure signaling path between the entities by using TLS protocol. Cisco Unified Communications Manager doesn’t register phones unless it can authenticate them. |
| File
					 authentication | Validates digitally signed files that the phone downloads. The phone validates the signature to make sure that file tampering didn’t occur after file creation. Files that fail authentication aren’t written to Flash memory on the phone. The phone rejects such files without further processing. |
| File
					 encryption | Encryption prevents sensitive information from being revealed while the file is in transit to the phone. In addition, the phone validates the signature to make sure that file tampering didn’t occur after file creation. Files that fail authentication aren’t written to Flash memory on the phone. The phone rejects such files without further processing. |
| Signaling
					 authentication | Uses the
					 TLS protocol to validate that no tampering to signaling packets has occurred
					 during transmission. |
| Manufacturing installed certificate | Each Cisco
					 IP Phone contains a unique manufacturing installed certificate (MIC), which is
					 used for device authentication. The MIC provides permanent unique proof of
					 identity for the phone and allows Cisco Unified Communications Manager to
					 authenticate the phone. |
| Media
					 encryption | Uses SRTP to ensure that media streams between supported devices prove secure and that only
									the intended device receives and reads the data. Includes
									creating a media primary key pair for the devices, delivering
									the keys to the devices, and securing the delivery of the keys
									while the keys are in transport. |
| CAPF
					 (Certificate Authority Proxy Function) | Implements parts of the certificate generation procedure that are too processing-intensive for the phone, and interacts with the phone for key generation and certificate installation. The CAPF can be configured to request certificates from customer-specified certificate authorities on behalf of the phone, or it can be configured to generate certificates locally. Both EC (Elliptical Curve) and RSA key types are supported. To use the EC key, make sure that the parameter "Endpoint Advanced Encryption Algorithms Support" (from System > Enterprise parameter ) is enabled. For more information about CAPF and related configurations, see the following documents: Security Guide for Cisco Unified Communications Manager CUCM Third-Party CA-Signed LSCs Generation and Import Configuration Example Configure Automatic Certificate Enrollment and Renewal Via CAPF Online CA |
| Security
					 profile | Defines
					 whether the phone is nonsecure, authenticated, encrypted, or protected. Other
					 entries in this table describe security features. |
| Encrypted
					 configuration files | Lets you
					 ensure the privacy of phone configuration files. |
| Optional
					 web server disabling for a phone | For security purposes, you can prevent access to the web pages for a phone (which display various operational statistics for the phone) and Self Care Portal. |
| Phone
					 hardening | Additional security options, which you control from Cisco
					 Unified Communications Manager Administration: Disabling PC port Disabling Gratuitous ARP
						(GARP) Disabling PC Voice VLAN
						access Disabling access to the Setting menu or providing restricted access Disabling access to web pages for a phone Disabling Bluetooth
						Accessory Port Restricting TLS ciphers |
| 802.1X
					 Authentication | The Cisco IP Phone can use 802.1X authentication to request and gain access to the network. See 802.1X Authentication for more information. |
| Secure
					 SIP Failover for SRST | After
					 you configure a Survivable Remote Site Telephony (SRST) reference for security
					 and then reset the dependent devices in Cisco Unified Communications Manager
					 Administration, the TFTP server adds the SRST certificate to the phone cnf.xml
					 file and sends the file to the phone. A secure phone then uses a TLS connection
					 to interact with the SRST-enabled router. |
| Signaling encryption | Ensures
					 that all SIP signaling messages that are sent between the device and the Cisco
					 Unified Communications Manager server are encrypted. |
| Trust List update alarm | When the Trust List updates on the phone, the Cisco Unified Communications Manager receives an alarm to indicate the success or failure of the update. See the following table for more information. |
| AES 256 Encryption | When connected to Cisco Unified Communications Manager Release 10.5(2) and later, the phones support AES 256 encryption support for TLS and SIP for signaling and media encryption. This enables phones to initiate and support TLS 1.2 connections using AES-256 based ciphers that conform to SHA-2 (Secure Hash Algorithm) standards and are Federal Information Processing Standards (FIPS) compliant. The ciphers include: For TLS connections: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 For sRTP: AEAD_AES_256_GCM AEAD_AES_128_GCM For more information, see the Cisco Unified Communications Manager documentation. |
| Elliptic Curve Digital Signature Algorithm (ECDSA) certificates | As part of Common Criteria (CC) certification, Cisco Unified Communications Manager; added ECDSA certificates in version 11.0. This affects all Voice Operating System (VOS) products running CUCM 11.5 and later versions. |
| Multi-server (SAN) Tomcat Certificate with Cisco UCM | The phone supports Cisco UCM with Multi-server (SAN) Tomcat Certificates configured. The correct TFTP server address can be found in the phone ITL file for phone's registration. For more information about the feature, see the following: How To Configure Multi-server (SAN) Tomcat certificate with Cisco UCM Security Guide for Cisco Unified Communications Manager |

| Code and message | Description |
|---|---|
| 1 - TL_SUCCESS | Received new CTL and/or ITL |
| 2 - CTL_INITIAL_SUCCESS | Received new CTL, no existing TL |
| 3 - ITL_INITIAL_SUCCESS | Received new ITL, no existing TL |
| 4 - TL_INITIAL_SUCCESS | Received new CTL and ITL, no existing TL |
| 5 - TL_FAILED_OLD_CTL | Update to new CTL failed, but have previous TL |
| 6 - TL_FAILED_NO_TL | Update to new TL failed, and have no old TL |
| 7 - TL_FAILED | Generic failure |
| 8 - TL_FAILED_OLD_ITL | Update to new ITL failed, but have previous TL |
| 9 - TL_FAILED_OLD_TL | Update to new TL failed, but have previous TL |

| Option | Description | To
					 Change |
|---|---|---|
| Security
					 Mode | Displays
					 the security mode that is set for the phone. | From
					 Cisco Unified Communications Manager Administration, choose Device > Phone . The setting appears in the
					 Protocol Specific Information portion of the Phone Configuration window. |
| LSC | Indicates whether a locally significant certificate that is used for security features is installed on the phone (Installed) or isn’t installed on the phone (Not installed). | For
					 information about how to manage the LSC for your phone, see the 
					 documentation for your particular Cisco Unified Communications Manager release. |

| 1 | Obtain the CAPF authentication code that was set when the CAPF was
			 configured. |
|---|---|
| 2 | On the phone, press Settings . |
| 3 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 4 | Navigate to Network and Service > Security settings > LSC . You can control access to the Settings menu by using the Settings Access field in Cisco Unified Communications Manager Administration. |
| 5 | Enter the authentication string and select Submit . The phone begins to install, update, or remove the LSC, depending on how the CAPF is configured. When the procedure is complete, Installed or Not Installed displays on the phone. The LSC install, update, or removal process can take a long time to complete. When the phone installation procedure is successful, the Installed message displays. If the phone displays Not Installed , then the authorization string may be incorrect or the phone upgrade may not be enabled. If the CAPF operation deletes the LSC, the phone displays Not Installed to indicate that the operation succeeded. The CAPF server logs the error messages. See the CAPF server documentation to locate the logs and to understand the meaning of the error messages. |

| 1 | In Cisco Unified Communications Manager Administration, select Device > Phone and locate the phone. |
|---|---|
| 2 | Navigate to the Product Specific Configuration area. |
| 3 | Set the FIPS Mode field to Enabled . |
| 4 | Select Save . |
| 5 | Select Apply Config . |
| 6 | Restart the phone. |

| 1 | In Cisco Unified Communications Manager Administration, select Device > Phone and locate the phone. |
|---|---|
| 2 | Navigate to the Product Specific Configuration area. |
| 3 | Check one or more of the following check boxes to turn off the capabilities of the phone: Disable Speakerphone Disable Speakerphone and Headset Disable Handset By default, these check boxes are unchecked. |
| 4 | Select Save . |
| 5 | Select Apply Config . |

| 1 | Press Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Navigate to Network and service > Security settings > 802.1X Authentication . |
| 4 | Turn on IEEE 802.1X authentication. |
| 5 | Select Apply . |

| Parameters | Description |
|---|---|
| Security Mode | Displays the security mode that is set for the phone. |
| LSC | Indicates whether a locally significant certificate that is used for security features is installed on the phone (Yes) or is not installed on the phone (No). |
| Trust List | The Trust List provides submenus for the CTL, ITL, and Signed Configuration files. The CTL File submenu displays the contents of the CTL file. The ITL File submenu displays contents of the ITL file. The Trust List menu also displays the following information: CTL Signature: the SHA1 hash of the CTL file Unified CM/TFTP Server: the name of the Cisco Unified Communications Manager and TFTP Server that the phone uses. Displays a certificate icon if a certificate is installed for this server. CAPF Server: the name of the CAPF server that the phone uses. Displays a certificate icon if a certificate is installed for this server. SRST Router: the IP address of the trusted SRST router that the phone can use. Displays a certificate icon if a certificate is installed for this server. |
| 802.1X authentication | Enables or disables the IEEE 802.1X authentication. For details, see 802.1X Authentication . |
| Backward compatibility with WPA | Determines whether the oldest version of Wi-Fi Protected Access (WPA) is compatible on the phone to connect to a wireless network or access point (AP). If enabled, the phone can search and connect to wireless networks with all versions of WPA supported, including WPA, WPA2, and WPA3. In addition, the phone can search and connect to APs that only support the oldest version of WPA. If disabled (default), the phone can only search and connect to the wireless networks and APs that support WPA2 and WPA3. This feature is only available on 9861/9871/8875 phones. |

| 1 | Press Settings . |
|---|---|
| 2 | Navigate to Network and service > Security settings . |
| 3 | In the Security settings , view the security information. |

| Initiator Phone Security Level | Feature Used | Security Level of Participants | Results of Action |
|---|---|---|---|
| Nonsecure | Conference | Secure | Nonsecure
				conference bridge Nonsecure
				conference |
| Secure | Conference | At least one
				member is nonsecure. | Secure
				conference bridge Nonsecure
				conference |
| Secure | Conference | Secure | Secure
				conference bridge Secure
				encrypted level conference |
| Nonsecure | Meet Me | Minimum
				security level is encrypted. | Initiator
				receives message Does not meet Security Level, call rejected . |
| Secure | Meet Me | Minimum
				security level is nonsecure. | Secure
				conference bridge Conference
				accepts all calls. |

| FSR Type | Authentication | Key Management | Encryption | Protected Management Frame (PMF) |
|---|---|---|---|---|
| 802.11r (FT) | PSK | WPA-PSK WPA-PSK-SHA256 FT-PSK | AES | No |
| 802.11r (FT) | WPA3 | SAE FT-SAE | AES | Yes |
| 802.11r (FT) | EAP-TLS | WPA-EAP FT-EAP | AES | No |
| 802.11r (FT) | EAP-TLS (WPA3) | WPA-EAP-SHA256 FT-EAP | AES | Yes |
| 802.11r (FT) | EAP-FAST | WPA-EAP FT-EAP | AES | No |
| 802.11r (FT) | EAP-FAST (WPA3) | WPA-EAP-SHA256 FT-EAP | AES | Yes |
| 802.11r (FT) | EAP-PEAP | WPA-EAP FT-EAP | AES | No |
| 802.11r (FT) | EAP-PEAP (WPA3) | WPA-EAP-SHA256 FT-EAP | AES | Yes |

| 1 | In Cisco Unified Communications Manager Administration, select Device > Device Settings > Wireless LAN Profile . |
|---|---|
| 2 | Choose the network profile that you want to configure. |
| 3 | Set up the parameters. |
| 4 | Click Save . |

| 1 | From the Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| 2 | Locate the phone. |
| 3 | Scroll to the Product Specific Configuration Layout area. |
| 4 | Enter the RA IP address or hostname in the WLAN SCEP Server field, and then select the check box to activate the SCEP parameter. |
| 5 | Enter the SHA-1 or SHA-256 fingerprint of the root CA certificate in the WLAN Root CA Fingerprint (SHA256 or SHA1) field, and then select
          check box to activate the SCEP QED parameter. |
| 6 | Select Save . |
| 7 | Select Apply Config . |

| 1 | Sign into Cisco Unified Communications Manager Administration as an administrator. |
|---|---|
| 2 | Navigate to one of the following windows: System > Enterprise Phone Configuration Device > Device Settings > Common Phone Profile Device > Phone > Phone Configuration |
| 3 | Set up the TLS Client Min Version field: The "TLS 1.3" option is available on Cisco Unified CM 15SU2, or later. TLS 1.1 : The TLS client supports the versions of TLS from 1.1 to 1.3. If the TLS version in server is lower than 1.1, for example, 1.0, then the connection can't be established. TLS 1.2 (default): The TLS client supports TLS 1.2 and 1.3. If the TLS version in server is lower than 1.2, for example, 1.1 or 1.0, then the connection can't be established. TLS 1.3 : The TLS client supports TLS 1.3 only. If  the TLS version in server is lower than 1.3, for example, 1.2, 1.1 or 1.0, then the connection can't be established. |
| 4 | Set up the TLS Server Min Version field: TLS 1.1 : The TLS server supports the versions of TLS from 1.1 to 1.3. If the TLS version in client is lower than 1.1, for example, 1.0, then the connection can't be established. TLS 1.2 (default): The TLS server supports TLS 1.2 and 1.3. If the TLS version in client is lower than 1.2, for example, 1.1 or 1.0, then the connection can't be established. TLS 1.3 : The TLS server supports TLS 1.3 only. If  the TLS version in client is lower than 1.3, for example, 1.2, 1.1 or 1.0, then the connection can't be established. From PhoneOS 3.2 release, the setting of the field "Disable TLS 1.0 and TLS 1.1 for Web Access" doesn't take affect on the phones. |
| 5 | Click Save . |
| 6 | Click Apply Config . |
| 7 | Restart the phones. |

## Figuras

![the Settings hard key](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/300001-400000/370001-380000/371001-372000/371845.jpg)

![the Settings key](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478218.png)

![the lock icon for a secure call](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472555.png)