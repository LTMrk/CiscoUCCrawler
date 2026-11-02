---
doc_id: help-webex-com-en-us-article-eyjsp2-cea449b241
source_url: https://help.webex.com/en-us/article/eyjsp2
retrieved_at: 2026-11-02T13:02:56.668077+00:00
---

## Configure DHCP options

You can set the order in which your phone uses the DHCP options. For help with DHCP Options, see DHCP option support .

Access the phone administration web page.

Select Voice > Provisioning .

In the Configuration Profile section,  set the DHCP Option To Use and DHCPv6 Option To Use parameters as described below:

You can also configure this parameter in the configuration file (cfg.xml):

<DHCP_Option_To_Use ua="na">66,160,159,150</DHCP_Option_To_Use>

Default: 66,160,159,150 or 66,160,159,150,60,43,125 , depending on the phone model

You can also configure this parameter in the configuration file (cfg.xml):

<DHCPv6_Option_To_Use ua="na">17,160,159</DHCPv6_Option_To_Use>

Default: 17,160,159

Click Submit All Changes .

### DHCP option support

The following table lists the DHCP options that are supported on the PhoneOS phones.

Can be used to provide the SCEP configuration.

NTP server configuration with IPv6

## Set the minimum TLS version for client and server

By default, the minimum TLS version for client and server is 1.2. This means that the client and server accept to establish connections with TLS 1.2 or above. The supported maximum version of TLS for client and server is 1.3. When configured, the  minimum TLS version will be used for negotiation between the TLS client and TLS server.

You can set the minimum version of TLS for client and server respectively, such as 1.1, 1.2, or 1.3.

Before you begin

Make sure that the TLS server supports the minimum TLS version configured. You can consult
        with the administrator of the call control system.

Access the phone administration web page.

Select Voice > System .

In the section Security Settings , configure the parameter TLS Client Min Version .

If the TLS version in server is lower than 1.1, then the connection can't be established.

If the TLS version in server is lower than 1.2, for example, 1.1, then the connection can't be established.

If the TLS version in server is lower than 1.3, for example, 1.2 or 1.1, then the connection can't be established.

If you want to set the parameter "TLS Client Min Version" to "TLS 1.3", make sure that the server side supports TLS 1.3. If the server side doesn't support TLS 1.3, this might cause critical issues. For example, the provisioning operations can't be performed on the phones.

You can also configure this parameter in the configuration file (cfg.xml):

Allowed values: TLS 1.1, TLS1.2, and TLS 1.3.

Default: TLS 1.2

In the section Security Settings , configure the parameter TLS Server Min Version .

Webex Calling doesn't support TLS 1.1.

If the TLS version in client is lower than 1.1, then the connection can't be established.

If the TLS version in client is lower than 1.2, for example, 1.1, then the connection can't be established.

If the TLS version in client is lower than 1.3, for example, 1.2 or 1.1, then the connection can't be established.

You can also configure this parameter in the configuration file (cfg.xml):

Allowed values: TLS 1.1, TLS1.2, and TLS 1.3.

Default: TLS 1.2

Click Submit All Changes .

## Enable FIPS mode

You can make a phone Federal Information Processing Standards (FIPS) compliant.

FIPS are a set of standards that describe document processing, encryption algorithms, and other information technology standards for use within non-military government and by government contractors and vendors who work with the agencies. CiscoSSL FOM (FIPS Object Module) is a carefully defined software component and designed for compatibility with the CiscoSSL library, so products using the CiscoSSL library and API can be converted to use FIPS 140-2 validated cryptography with minimal effort.

Access the phone administration web page.

Select Voice > System .

In the Security Settings section, choose Yes or No from the FIPS Mode parameter.

Click Submit All Changes .

When you enable FIPS, the following features work seamlessly on the phone:

- Image authentication

- Secure storage

- Config file encryption

- HTTPs

- PRT Upload

- Firmware upgrade

- Profile resync

- Onboard service

- Webex onboarding

- SIP over TLS

- 802.1x (Wired)

- SIP digest (RFC 8760)

- SRTP

- Webex call logs and Webex directory

- One Button to Push (OBTP)

## Set the user and admin passwords

When the phone is registered with a call control system for the first time or after a
        factory reset, you must set both the user and admin passwords to improve phone security.
        After the passwords are set, you can access the phone web interface.

By default, both passwords are empty. Until you set them, the No password
          provided message appears each time the phone restarts. The missing password is
        also reported under Settings > Issues and diagnostics > Issues on the phone. You can disable the warning display with the Display
          Password Warnings setting.

Access the phone administration web page

Select Voice > System .

In the System Configuration section, click Change
            Password next to User Password or Admin
            Password .

For first-time setup, leave the Old Password field empty. Enter
          the existing password only when changing it.

Enter a new password in the New Password field.

Password requirements:

- The password must contain between 8 and 127 characters.

- The password must contain at least three of the four categories: uppercase letters,
              lowercase letters, numbers, and special characters.

- Spaces are not allowed.

If the new password doesn't meet the requirements, it is rejected.

Click Submit .

The message Password has been changed successfully. appears in the web
            page. The web page refreshes in several seconds.

After both passwords are set, they display as masked values in the phone configuration
            XML file (cfg.xml), as follows:

To enable or disable the password warning, set Display Password
            Warnings to the desired value in the System
            Configuration section, and then click Submit All
            Changes .

When set to Yes , the warning appears on the phone screen if a password is
            missing. When set to No , the warning is not displayed.

You can also configure the parameters in the phone configuration file (cfg.xml).

<Display_Password_Warnings
              ua="na">Yes</Display_Password_Warnings>

Default: Yes

Options: Yes | No

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

### Enable 802.1X authentication on phone web page

When 802.1X authentication is enabled, the phone uses 802.1X authentication to request network access. When 802.1X authentication is disabled, the phone uses Cisco Discovery Protocol (CDP) to acquire VLAN and network access.

You can select a certificate (MIC/SUDI or CDC) used for the 802.1X authentication. For more information about CDC, see Custom Device Certificate on 9800/8875 .

You can view the transaction status and security settings on the phone screen menu. For more information, see Security settings menu on phone .

Enable 802.1X authentication.

Select Voice > System and set the Enable 802.1X Authentication parameter to Yes .

You can also configure this parameter in the configuration file (cfg.xml):

<Enable_802.1X_Authentication ua="rw">Yes</Enable_802.1X_Authentication>

Valid values: Yes|No

Default: No

Select one of the following installed certificates used for the 802.1X authentication.

Value options:

- Manufacturing installed : MIC/SUDI.

- Custom installed : Custom Device Certificate (CDC).

The configuration varies based on the network:

You can also configure this parameter in the configuration file (cfg.xml):

<Certificate_Select ua="rw">Custom installed</Certificate_Select>

Valid values: Manufacturing installed|Custom installed

Default: Manufacturing installed

You can also configure this parameter in the configuration file (cfg.xml):

<Wi-Fi_Certificate_Select_1_ ua="rw">Custom installed</Wi-Fi_Certificate_Select_1_>

Valid values: Manufacturing installed|Custom installed

Default: Manufacturing installed

Configure the parameter User ID that will be used as the identity for the 802.1X authentication in the wired network.

The parameter configuration takes effect only when CDC is used for the wired 802.1X authentication ( Certificate Select is set to Custom installed ).

By default, this parameter is empty. The identity for wired 802.1X varies based on the selected certificate:

If MIC/SUDI is selected, the wired 802.1X identity is represented as below:

<Product Name> + SEP <MAC address> .

Examples: DP-98xx-SEP <MAC address> , CP-8875-SEP <MAC address> .

If CDC is selected, the Common Name in CDC is used as the identity for wired 802.1X.

If User ID is empty and the Common Name in CDC is configured, then the wired 802.1X will use the CDC Common Name as the identity.

You can also configure this parameter in the configuration file (cfg.xml):

<Wired_User_ID ua="na"></Wired_User_ID>

Valid Values: Maximum of 127 characters

Default: Empty

This parameter also supports macro expansion variables, see Macro expansion variables for details.

If you want to utilize DHCP options to provision the user ID, see Provisioning of Common Name or User ID via DHCP option 15 .

Click Submit All Changes .

### Security settings menu on phone

You can view the information about the security settings on the phone menu. The navigation path is: Settings > Network and service > Security settings . The availability of the information depends on the network settings in your organization.

Parameters

Options

Default

Description

Device authentication

On

Off

Off

Enables or disables 802.1X authentication on the phone.

The parameter setting can be kept after the phone's Out-Of-Box (OOB) registration.

Transaction status

Displays the state of 802.1X authentication. The state can be (not limited to):

- Authenticating : Indicates that the authentication process is in progress.

- Authenticated : Indicates that the phone is authenticated.

- Disabled : Indicates that 802.1x authentication is disabled on the phone.

Protocol

Displays the EAP method that is used for 802.1X authentication. The protocol can be EAP-FAST or EAP-TLS.

User certificate type

Manufacturing installed

Custom installed

Manufacturing installed

Selects the certificate for the 802.1X authentication during the initial enrollment and certificate renewal.

- Manufacturing installed—The Manufacturing Installed Certificate (MIC) and Secure Unique Device Identifier (SUDI) is used.

- Custom installed—The Custom Device Certificate (CDC) is used. This type of certificate can be installed either by manual uploading on the phone web page or by installation from a Simple Certificate Enrollment Protocol (SCEP) server.

This parameter appears on the phone only when Device authentication is enabled.

On

Off

Determines whether the oldest version of Wi-Fi Protected Access (WPA) is compatible on the phone to connect to a wireless network or access point (AP).

- If enabled, the phone can search and connect to wireless networks with all versions of WPA supported, including WPA, WPA2, and WPA3. In addition, the phone can search and connect to APs that only support the oldest version of WPA.

- If disabled (default), the phone can only search and connect to the wireless networks and APs that support WPA2 and WPA3.

This feature is only available on 9861/9871/8875 phones.

## Set up a proxy server

You can configure the phone to use a proxy server to enhance the security. Typically, an HTTP proxy server can provide the following services:

- Routing traffic between internal and external networks

- Filtering, monitoring, or logging traffic

- Caching responses to improve performance

Also, the HTTP proxy server can act as a firewall between between the phone and Internet. After a successful configuration, the phone connects to Internet through the proxy server which protects the phone from cyber attack.

When configured, the HTTP proxy feature applies to all applications that use the HTTP protocol. For example:

- GDS (Activation Code Onboarding)

- EDOS Device Activation

- Onboarding to Webex Cloud (via EDOS or GDS)

- Custom CA

- Provisioning

- Firmware Upgrade

- Phone Status Report

- PRT Upload

- XSI Services

- Webex Services

- Currently, the feature supports only IPv4.

- The HTTP proxy settings can be kept after the phone's Out-Of-Box (OOB) registration.

Access the phone administration web page.

Select Voice > System .

In the section HTTP Proxy Settings , select a proxy mode from the drop-down list Proxy Mode and configure the related parameters.

For more information about the parameters and required parameters for each proxy mode, see Parameters for HTTP proxy settings .

Click Submit All Changes .

### Parameters for HTTP proxy settings

The following table defines the function and usage of the HTTP proxy parameters in the HTTP Proxy Settings section under the Voice > System tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file (cfg.xml) with XML code to configure a parameter.

The phone automatically retrieves a Proxy Auto-Configuration (PAC) file to select a proxy server. In this mode, you can determine whether to use Web Proxy Auto Discovery (WPAD) protocol to retrieve a PAC file or manually enter a valid URL of the PAC file.

For details about the parameters, see the parameters "Web Proxy Auto Discovery" and "PAC URL" in this table.

You must manually specify a server (hostname or IP address) and a port of a proxy server.

For details about the parameters, see Proxy Host and Proxy Port.

You disable the HTTP proxy feature on the phone.

Perform one of the following:

<Proxy_Mode ua="rw">Off</Proxy_Mode>

- On the phone web interface, select a proxy mode or disable the feature.

Allowed values: Auto, Manual, and Off

Default: Off

WPAD protocol uses DHCP or DNS, or both network protocols to locate a Proxy Auto Configuration (PAC) file automatically. PAC file is used to select a proxy server for a given URL. This file can be hosted locally or on a network.

- The parameter configuration takes effect when Proxy Mode is set to Auto .

For details about the parameter, see the parameter "PAC URL" in this table.

Perform one of the following:

<Web_Proxy_Auto_Discovery ua="rw">Yes</Web_Proxy_Auto_Discovery>

- On the phone web interface, select Yes or No as needed.

Allowed values: Yes and No

Default: Yes

For example, http://proxy.department.branch.example.com

TFTP, HTTP, and HTTPS are supported.

If you set the Proxy Mode to Auto and Web Proxy Auto Discovery to No , you must configure this parameter.

Perform one of the following:

<PAC_URL ua="rw">http://proxy.department.branch.example.com/pac</PAC_URL>

- On the phone web interface, enter a valid URL that locates to a PAC file.

Default: Empty

proxy.example.com

The scheme ( http:// or https:// ) is not required.

If you set the Proxy Mode to Manual , you must configure this parameter.

Perform one of the following:

<Proxy_Host ua="rw">proxy.example.com</Proxy_Host>

- On the phone web interface, enter an IP address or hostname of the proxy server.

Default: Empty

If you set the Proxy Mode to Manual , you must configure this parameter.

Perform one of the following:

<Proxy_Port ua="rw">3128</Proxy_Port>

- On the phone web interface, enter a server port.

Default: 3128

If you set the parameter to Yes , you must configure Username and Password .

For details about the parameters, see the parameter "Username" and "Password" in this table.

The parameter configuration takes effect when Proxy Mode is set to Manual .

Perform one of the following:

<Proxy_Authentication ua="rw">No</Proxy_Authentication>

- On the phone web interface, set this field Yes or No as needed.

Allowed values: Yes and No

Default: No

If Proxy Mode is set to Manual and Proxy Authentication is set to Yes , you must configure the parameter.

Perform one of the following:

<Proxy_Username ua="rw">Example</Proxy_Username>

- On the phone web interface, enter the username.

Default: Empty

If Proxy Mode is set to Manual and Proxy Authentication is set to Yes , you must configure the parameter.

Perform one of the following:

<Proxy_Password ua="rw">Example</Proxy_Password>

- On the phone web interface, enter a valid password for the proxy authentication of the user.

Default: Empty

Proxy Port

Proxy Authentication: Yes

Username

Password

Proxy Port

Proxy Authentication: No

PAC URL

Uses the WPAD protocol to automatically retrieve a PAC file.

## Enable client-Initiated mode for media plane security negotiations

To protect media sessions, you can configure the phone to initiate media plane security negotiations with the server. The security mechanism follows the standards stated in RFC 3329 and its extension draft Security Mechanism Names for Media (See https://tools.ietf.org/html/draft-dawes-sipcore-mediasec-parameter-08#ref-2 ). The transport of negotiations between the phone and the server can use SIP protocol over UDP, TCP, and TLS. You can limit that media plane security negotiation is applied only when the signaling transport protocol is TLS.

MediaSec Request

Specifies whether the phone initiates media plane security negotiations with the server.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

- In the phone web interface, set this field to Yes or No as needed.

Allowed values: Yes|No

- Yes —Client-initiated Mode. The phone initiates media plane security negotiations.

- No —Server-initiated Mode. The server initiates media plane security negotiations. The phone doesn't initiate negotiations, but can handle negotiation requests from the server to establish secure calls.

Default: No

MediaSec Over TLS Only

Specifies the signaling transport protocol over which media plane security negotiation is applied.

Before setting this field to Yes , ensure that the signaling transport protocol is TLS.

Perform one of the following:

<MediaSec_Over_TLS_Only_1_ ua="na">No</MediaSec_Over_TLS_Only_1_>

- In the phone web interface, set this field to Yes or No as needed.

Allowed values: Yes|No

- Yes —The phone initiates or handles media plane security negotiations only when the signaling transport protocol is TLS.

- No —The phone initiates and handles media plane security negotiations regardless of the signaling transport protocol.

Default: No

Access the phone administration web page.

Select Voice > Ext (n) .

In the SIP Settings section, set the MediaSec Request and MediaSec Over TLS Only fields as defined in the above table.

Click Submit All Changes .

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

### Set up Wi-Fi profile

You can configure Wi-Fi profiles from the phone administration web page or through a remote
        device profile resync. Once configured, you can associate these profiles with available
        wireless networks to establish connectivity. Cisco Wireless Phone 9821 supports a maximum of four configured Wi-Fi profiles.

The profile contains the parameters required for phones to connect to the phone server with Wi-Fi. When you create and use a Wi-Fi profile, you or your users don't need to configure the wireless network for individual phones.

A Wi-Fi profile enables you to prevent or limit changes to the Wi-Fi configuration on the phone by the user.

We recommend that you use a secure profile with encryption enabled protocols to protect keys and passwords when you use a Wi-Fi profile.

When you set up the phones to use the EAP-FAST authentication method in security mode, your users need individual credentials to connect to an access point.

Access the phone web page.

Select Voice > System .

In the Wi-Fi Profile (n) section, set the parameters as
          described in the following table Parameters for Wi-Fi profile .

The Wi-Fi profile configuration is also available to the user login.

Click Submit All Changes .

#### Parameters for Wi-Fi profile

The following table defines the function and usage of each parameter in the Wi-Fi Profile(n) section under the System tab in the phone web page. It also defines the syntax of the string that is added in the
        phone configuration file (cfg.xml) to configure a parameter.

Perform one of the following:

<Network_Name_1_
                        ua="rw">cisco</Network_Name_1_>

- In the phone web page, enter a name for the SSID.

Default: Empty

Perform one of the following:

<Security_Mode_1_
                        ua="rw">EAP-TLS</Security_Mode_1_> <!-- available options:
                        Auto|EAP-FAST|||PSK||None|EAP-PEAP|EAP-TLS -->

- Auto

- EAP-FAST

- PSK

- None

- EAP-PEAP

- EAP-TLS

Default: Auto

This field is
                  available when you set the security mode to Auto, EAP-FAST, or EAP-PEAP. This is a
                  mandatory field and it allows maximum length of 32 alphanumeric
                  characters.

Perform one of the following:

<Wi-Fi_User_ID_1_ua="rw"></Wi-Fi_User_ID_1_>

- In the phone web page, enter a user ID for the network profile.

Default: Empty

Perform one
                  of the following:

<Wi-Fi_Password_1_
                        ua="rw"></Wi-Fi_Password_1_>

- In the phone web page, enter a password for the user ID that you have
                    added.

Default: Empty

Perform one of the following:

<Frequency_Band_1_
                        ua="rw">Auto</Frequency_Band_1_>

- Auto

- 2.4 GHz

- 5 GHz

Default: Auto

Perform one of the following:

<Certificate_Select_1_ ua="rw">Manufacturing
                        installed</Certificate_Select_1_>

- Manufacturing installed

- Custom installed

Default: Manufacturing installed

When Security Mode is set to EAP-TLS and Certificate Select is set to Custom installed, the User
          ID becomes available for configuration on the phone. The Wi-Fi User ID
        configuration determines the 802.1x EAP-TLS Identity with the following behavior:

- If a user ID is configured: The phone will use the specified value as its 802.1x
          EAP-TLS Identity.

- If the user ID field is left blank: The phone will always default to using the
          MIC (Manufacturer Installed Certificate) or SUDI (Secure Unique Device Identity) Common
          Name as its 802.1x EAP-TLS Identity. This behavior occurs even if a Common Name has been
          selected via CDC (Certificate Device Configuration).

## Check device security status on the phone

Your phone checks the device security status automatically. If it detects potential security threats on the phone, the Issues and diagnostics menu can show the details of the issues. Based on the reported issues, your administrator can take operations to secure and harden your phone.

The device security status is available before the phone is registered to the call control system (Webex Calling or BroadWorks).

To view details of security issues on the phone screen, do the following:

Press Settings

Select Issues and diagnostics > Issues .

Currently, the device security report contains the following issues:

- Device authentication failed

- SoC tampering detected

- SSH enabled

- Telnet enabled

- Excessive web login attempts

- High UDP traffic detected

- Suspicious ICMP timpstamp requests

- Custom device certificate expiration

Contact your administrator for support to resolve the security issues.

## Set OCSP stapling enforcement

Online Certificate Status Protocol (OCSP) helps prevent connections that use revoked certificates during the TLS handshake. With OCSP stapling enforcement enabled, the phone requests and validates a stapled OCSP response. The phone rejects the connection if the response is invalid or reports that the certificate is revoked. It rejects a missing response or a valid OCSP response with an UNKNOWN status only when the server certificate requires OCSP stapling (that is, has the must-staple extension). Regular certificate validation still applies.

Access the phone administration web page.

Select Voice > System .

In the Security Settings section, configure the OCSP Stapling Enforcement setting.

You can also enable the parameters in the phone configuration file (cfg.xml).

<OCSP_Stapling_Enforcementua="na">Enabled</OCSP_Stapling_Enforcement>

Default: Enabled

Options: Disabled | Enabled

Click Submit All Changes .

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Provisioning . |
| 3 | In the Configuration Profile section,  set the DHCP Option To Use and DHCPv6 Option To Use parameters as described below: DHCP Option To Use : DHCP options, delimited by commas, used to retrieve firmware and profiles. You can also configure this parameter in the configuration file (cfg.xml): <DHCP_Option_To_Use ua="na">66,160,159,150</DHCP_Option_To_Use> Default: 66,160,159,150 or 66,160,159,150,60,43,125 , depending on the phone model DHCPv6 Option To Use : DHCPv6 options, delimited by commas, used to retrieve firmware and profiles. You can also configure this parameter in the configuration file (cfg.xml): <DHCPv6_Option_To_Use ua="na">17,160,159</DHCPv6_Option_To_Use> Default: 17,160,159 |
| 4 | Click Submit All Changes . |

| Network Standard | Description |
|---|---|
| DHCP option 1 | Subnet mask |
| DHCP option 2 | Time offset |
| DHCP option 3 | Router |
| DHCP option 6 | Domain name server |
| DHCP option 15 | Domain name |
| DHCP option 17 | Vendor-identifying vendor-specific information |
| DHCP option 41 | IP address lease time |
| DHCP option 42 | NTP server |
| DHCP option 43 | Vendor-specific information Can be used to provide the SCEP configuration. |
| DHCP option 56 | NTP server NTP server configuration with IPv6 |
| DHCP option 60 | Vendor class identifier |
| DHCP option 66 | TFTP server name |
| DHCP option 125 | Vendor-identifying vendor-specific information |
| DHCP option 150 | TFTP server |
| DHCP option 159 | Provisioning server IP |
| DHCP option 160 | Provisioning URL |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > System . |
| 3 | In the section Security Settings , configure the parameter TLS Client Min Version . TLS 1.1 : The TLS client supports the versions of TLS from 1.1 to 1.3. If the TLS version in server is lower than 1.1, then the connection can't be established. TLS 1.2 (default): The TLS client supports TLS 1.2 and 1.3. If the TLS version in server is lower than 1.2, for example, 1.1, then the connection can't be established. TLS 1.3 : The TLS client supports TLS 1.3 only. If the TLS version in server is lower than 1.3, for example, 1.2 or 1.1, then the connection can't be established. If you want to set the parameter "TLS Client Min Version" to "TLS 1.3", make sure that the server side supports TLS 1.3. If the server side doesn't support TLS 1.3, this might cause critical issues. For example, the provisioning operations can't be performed on the phones. You can also configure this parameter in the configuration file (cfg.xml): <TLS_Client_Min_Version ua="na">TLS 1.2</TLS_Client_Min_Version> Allowed values: TLS 1.1, TLS1.2, and TLS 1.3. Default: TLS 1.2 |
| 4 | In the section Security Settings , configure the parameter TLS Server Min Version . Webex Calling doesn't support TLS 1.1. TLS 1.1 : The TLS server supports the versions of TLS from 1.1 to 1.3. If the TLS version in client is lower than 1.1, then the connection can't be established. TLS 1.2 (default): The TLS server supports TLS 1.2 and 1.3. If the TLS version in client is lower than 1.2, for example, 1.1, then the connection can't be established. TLS 1.3 : The TLS server supports TLS 1.3 only. If the TLS version in client is lower than 1.3, for example, 1.2 or 1.1, then the connection can't be established. You can also configure this parameter in the configuration file (cfg.xml): <TLS_Server_Min_Version ua="na">TLS 1.2</TLS_Server_Min_Version> Allowed values: TLS 1.1, TLS1.2, and TLS 1.3. Default: TLS 1.2 |
| 5 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > System . |
| 3 | In the Security Settings section, choose Yes or No from the FIPS Mode parameter. |
| 4 | Click Submit All Changes . When you enable FIPS, the following features work seamlessly on the phone: Image authentication Secure storage Config file encryption TLS: HTTPs PRT Upload Firmware upgrade Profile resync Onboard service Webex onboarding SIP over TLS 802.1x (Wired) SIP digest (RFC 8760) SRTP Webex call logs and Webex directory One Button to Push (OBTP) |

| 1 | Access the phone administration web page |
|---|---|
| 2 | Select Voice > System . |
| 3 | In the System Configuration section, click Change
            Password next to User Password or Admin
            Password . |
| 4 | For first-time setup, leave the Old Password field empty. Enter
          the existing password only when changing it. |
| 5 | Enter a new password in the New Password field. Password requirements: The password must contain between 8 and 127 characters. The password must contain at least three of the four categories: uppercase letters,
              lowercase letters, numbers, and special characters. Spaces are not allowed. If the new password doesn't meet the requirements, it is rejected. |
| 6 | Click Submit . The message Password has been changed successfully. appears in the web
            page. The web page refreshes in several seconds. After both passwords are set, they display as masked values in the phone configuration
            XML file (cfg.xml), as follows: |
| 7 | To enable or disable the password warning, set Display Password
            Warnings to the desired value in the System
            Configuration section, and then click Submit All
            Changes . When set to Yes , the warning appears on the phone screen if a password is
            missing. When set to No , the warning is not displayed. You can also configure the parameters in the phone configuration file (cfg.xml). <Display_Password_Warnings
              ua="na">Yes</Display_Password_Warnings> Default: Yes Options: Yes \| No |

| 1 | Enable 802.1X authentication. Select Voice > System and set the Enable 802.1X Authentication parameter to Yes . You can also configure this parameter in the configuration file (cfg.xml): <Enable_802.1X_Authentication ua="rw">Yes</Enable_802.1X_Authentication> Valid values: Yes\|No Default: No |
|---|---|---|
| 2 | Select one of the following installed certificates used for the 802.1X authentication. Value options: Manufacturing installed : MIC/SUDI. Custom installed : Custom Device Certificate (CDC). The configuration varies based on the network: For the wired network, select Voice > System , choose a certificate type from the drop-down list Certificate Select in the section 802.1X Authentication . You can also configure this parameter in the configuration file (cfg.xml): <Certificate_Select ua="rw">Custom installed</Certificate_Select> Valid values: Manufacturing installed\|Custom installed Default: Manufacturing installed For the wireless network, select Voice > System , choose a certificate type from the drop-down list Certificate Select in the section Wi-Fi Profile 1 . You can also configure this parameter in the configuration file (cfg.xml): <Wi-Fi_Certificate_Select_1_ ua="rw">Custom installed</Wi-Fi_Certificate_Select_1_> Valid values: Manufacturing installed\|Custom installed Default: Manufacturing installed |
| 3 | Configure the parameter User ID that will be used as the identity for the 802.1X authentication in the wired network. The parameter configuration takes effect only when CDC is used for the wired 802.1X authentication ( Certificate Select is set to Custom installed ). By default, this parameter is empty. The identity for wired 802.1X varies based on the selected certificate: If MIC/SUDI is selected, the wired 802.1X identity is represented as below: <Product Name> + SEP <MAC address> . Examples: DP-98xx-SEP <MAC address> , CP-8875-SEP <MAC address> . If CDC is selected, the Common Name in CDC is used as the identity for wired 802.1X. If User ID is empty and the Common Name in CDC is configured, then the wired 802.1X will use the CDC Common Name as the identity. You can also configure this parameter in the configuration file (cfg.xml): <Wired_User_ID ua="na"></Wired_User_ID> Valid Values: Maximum of 127 characters Default: Empty This parameter also supports macro expansion variables, see Macro expansion variables for details. If you want to utilize DHCP options to provision the user ID, see Provisioning of Common Name or User ID via DHCP option 15 . |
| 4 | Click Submit All Changes . |

| Parameters | Options | Default | Description |
|---|---|---|---|
| Device authentication | On Off | Off | Enables or disables 802.1X authentication on the phone. The parameter setting can be kept after the phone's Out-Of-Box (OOB) registration. |
| Transaction status |  | Disabled | Displays the state of 802.1X authentication. The state can be (not limited to): Authenticating : Indicates that the authentication process is in progress. Authenticated : Indicates that the phone is authenticated. Disabled : Indicates that 802.1x authentication is disabled on the phone. |
| Protocol |  | None | Displays the EAP method that is used for 802.1X authentication. The protocol can be EAP-FAST or EAP-TLS. |
| User certificate type | Manufacturing installed Custom installed | Manufacturing installed | Selects the certificate for the 802.1X authentication during the initial enrollment and certificate renewal. Manufacturing installed—The Manufacturing Installed Certificate (MIC) and Secure Unique Device Identifier (SUDI) is used. Custom installed—The Custom Device Certificate (CDC) is used. This type of certificate can be installed either by manual uploading on the phone web page or by installation from a Simple Certificate Enrollment Protocol (SCEP) server. This parameter appears on the phone only when Device authentication is enabled. |
| Backward compatibility with WPA | On Off | Off | Determines whether the oldest version of Wi-Fi Protected Access (WPA) is compatible on the phone to connect to a wireless network or access point (AP). If enabled, the phone can search and connect to wireless networks with all versions of WPA supported, including WPA, WPA2, and WPA3. In addition, the phone can search and connect to APs that only support the oldest version of WPA. If disabled (default), the phone can only search and connect to the wireless networks and APs that support WPA2 and WPA3. This feature is only available on 9861/9871/8875 phones. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > System . |
| 3 | In the section HTTP Proxy Settings , select a proxy mode from the drop-down list Proxy Mode and configure the related parameters. For more information about the parameters and required parameters for each proxy mode, see Parameters for HTTP proxy settings . |
| 4 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Proxy Mode | Specifies the HTTP proxy mode that the phone uses, or disables the HTTP proxy feature. Auto The phone automatically retrieves a Proxy Auto-Configuration (PAC) file to select a proxy server. In this mode, you can determine whether to use Web Proxy Auto Discovery (WPAD) protocol to retrieve a PAC file or manually enter a valid URL of the PAC file. For details about the parameters, see the parameters "Web Proxy Auto Discovery" and "PAC URL" in this table. Manual You must manually specify a server (hostname or IP address) and a port of a proxy server. For details about the parameters, see Proxy Host and Proxy Port. Off You disable the HTTP proxy feature on the phone. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_Mode ua="rw">Off</Proxy_Mode> On the phone web interface, select a proxy mode or disable the feature. Allowed values: Auto, Manual, and Off Default: Off |
| Web Proxy Auto Discovery | Determines whether the phone uses the Web Proxy Auto Discovery (WPAD) protocol to retrieve a PAC file. WPAD protocol uses DHCP or DNS, or both network protocols to locate a Proxy Auto Configuration (PAC) file automatically. PAC file is used to select a proxy server for a given URL. This file can be hosted locally or on a network. The parameter configuration takes effect when Proxy Mode is set to Auto . If you set the parameter to No , you must specify a PAC URL. For details about the parameter, see the parameter "PAC URL" in this table. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Web_Proxy_Auto_Discovery ua="rw">Yes</Web_Proxy_Auto_Discovery> On the phone web interface, select Yes or No as needed. Allowed values: Yes and No Default: Yes |
| PAC URL | URL of a PAC file. For example, http://proxy.department.branch.example.com TFTP, HTTP, and HTTPS are supported. If you set the Proxy Mode to Auto and Web Proxy Auto Discovery to No , you must configure this parameter. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <PAC_URL ua="rw">http://proxy.department.branch.example.com/pac</PAC_URL> On the phone web interface, enter a valid URL that locates to a PAC file. Default: Empty |
| Proxy Host | IP address or hostname of the proxy host server for the phone to access. For example: proxy.example.com The scheme ( http:// or https:// ) is not required. If you set the Proxy Mode to Manual , you must configure this parameter. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_Host ua="rw">proxy.example.com</Proxy_Host> On the phone web interface, enter an IP address or hostname of the proxy server. Default: Empty |
| Proxy Port | Port number of the proxy host server. If you set the Proxy Mode to Manual , you must configure this parameter. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_Port ua="rw">3128</Proxy_Port> On the phone web interface, enter a server port. Default: 3128 |
| Proxy Authentication | Determines whether the user needs to provide the authentication credentials (username and password) that the proxy server requires. This parameter is configured according to the actual behaviour of the proxy server. If you set the parameter to Yes , you must configure Username and Password . For details about the parameters, see the parameter "Username" and "Password" in this table. The parameter configuration takes effect when Proxy Mode is set to Manual . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_Authentication ua="rw">No</Proxy_Authentication> On the phone web interface, set this field Yes or No as needed. Allowed values: Yes and No Default: No |
| Username | Username for a credential user on the proxy server. If Proxy Mode is set to Manual and Proxy Authentication is set to Yes , you must configure the parameter. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_Username ua="rw">Example</Proxy_Username> On the phone web interface, enter the username. Default: Empty |
| Password | Password of the specified username for the proxy authentication purpose. If Proxy Mode is set to Manual and Proxy Authentication is set to Yes , you must configure the parameter. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_Password ua="rw">Example</Proxy_Password> On the phone web interface, enter a valid password for the proxy authentication of the user. Default: Empty |

| Proxy Mode | Required parameters | Description |
|---|---|---|
| Off | NA | HTTP proxy is disabled on the phone. |
| Manual | Proxy Host Proxy Port Proxy Authentication: Yes Username Password | Manually specify a proxy server (a hostname or IP address) and a proxy port. If the proxy server requires authentication, you must further enter the username and password. |
| Proxy Host Proxy Port Proxy Authentication: No | Manually specify a proxy server. The proxy server doesn’t require authentication credentials. |
| Auto | Web Proxy Auto Discovery: No PAC URL | Enter a valid PAC URL to retrieve the PAC file. |
| Web Proxy Auto Discovery: Yes | Uses the WPAD protocol to automatically retrieve a PAC file. |

| Parameter | Description |
|---|---|
| MediaSec Request | Specifies whether the phone initiates media plane security negotiations with the server. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <MediaSec_Request_1_ ua="na">Yes</MediaSec_Request_1_> In the phone web interface, set this field to Yes or No as needed. Allowed values: Yes\|No Yes —Client-initiated Mode. The phone initiates media plane security negotiations. No —Server-initiated Mode. The server initiates media plane security negotiations. The phone doesn't initiate negotiations, but can handle negotiation requests from the server to establish secure calls. Default: No |
| MediaSec Over TLS Only | Specifies the signaling transport protocol over which media plane security negotiation is applied. Before setting this field to Yes , ensure that the signaling transport protocol is TLS. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <MediaSec_Over_TLS_Only_1_ ua="na">No</MediaSec_Over_TLS_Only_1_> In the phone web interface, set this field to Yes or No as needed. Allowed values: Yes\|No Yes —The phone initiates or handles media plane security negotiations only when the signaling transport protocol is TLS. No —The phone initiates and handles media plane security negotiations regardless of the signaling transport protocol. Default: No |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext (n) . |
| 3 | In the SIP Settings section, set the MediaSec Request and MediaSec Over TLS Only fields as defined in the above table. |
| 4 | Click Submit All Changes . |

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

| 1 | Access the phone web page. |
|---|---|
| 2 | Select Voice > System . |
| 3 | In the Wi-Fi Profile (n) section, set the parameters as
          described in the following table Parameters for Wi-Fi profile . The Wi-Fi profile configuration is also available to the user login. |
| 4 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Network Name | Allows you to enter a name for the SSID that will display on the phone.
                Multiple profiles can have the same network name with different security
                  mode. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this
                        format: <Network_Name_1_
                        ua="rw">cisco</Network_Name_1_> In the phone web page, enter a name for the SSID. Default: Empty |
| Security Mode | Allows you to select the authentication method that is used to secure access to
                the Wi-Fi network. Depending on the method you choose, a password field appears so
                that you can provide the credentials that are required to join this Wi-Fi
                  network. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this
                        format: <Security_Mode_1_
                        ua="rw">EAP-TLS</Security_Mode_1_> <!-- available options:
                        Auto\|EAP-FAST\|\|\|PSK\|\|None\|EAP-PEAP\|EAP-TLS --> In the phone web page, select one of the methods: Auto EAP-FAST PSK None EAP-PEAP EAP-TLS Default: Auto |
| Wi-Fi User ID | Allows you to enter a user ID for the network profile. This field is
                  available when you set the security mode to Auto, EAP-FAST, or EAP-PEAP. This is a
                  mandatory field and it allows maximum length of 32 alphanumeric
                  characters. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this
                        format: <Wi-Fi_User_ID_1_ua="rw"></Wi-Fi_User_ID_1_> In the phone web page, enter a user ID for the network profile. Default: Empty |
| Wi-Fi Password | Allows you to enter the password for the specified Wi-Fi User ID. Perform one
                  of the following: In the phone configuration file with XML(cfg.xml), enter a string in this
                        format: <Wi-Fi_Password_1_
                        ua="rw"></Wi-Fi_Password_1_> In the phone web page, enter a password for the user ID that you have
                    added. Default: Empty |
| Frequency Band | Allows you to select the wireless signal frequency band that is the WLAN
                  uses. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this
                        format: <Frequency_Band_1_
                        ua="rw">Auto</Frequency_Band_1_> In the phone web page, select one of the options: Auto 2.4 GHz 5 GHz Default: Auto |
| Certificate Select | Allows you to select a certificate type for certificate initial enrollment and
                certificate renewal in the wireless network. This process is only available for
                802.1X authentication. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this
                        format: <Certificate_Select_1_ ua="rw">Manufacturing
                        installed</Certificate_Select_1_> In the phone web page, select one of the options: Manufacturing installed Custom installed Default: Manufacturing installed |

| 1 | Press Settings |
|---|---|
| 2 | Select Issues and diagnostics > Issues . Currently, the device security report contains the following issues: Device trust Device authentication failed SoC tampering detected Vulnerable configuration SSH enabled Telnet enabled Network anomaly event detected Excessive web login attempts High UDP traffic detected Suspicious ICMP timpstamp requests Certificate issue Custom device certificate expiration |
| 3 | Contact your administrator for support to resolve the security issues. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > System . |
| 3 | In the Security Settings section, configure the OCSP Stapling Enforcement setting. You can also enable the parameters in the phone configuration file (cfg.xml). <OCSP_Stapling_Enforcementua="na">Enabled</OCSP_Stapling_Enforcement> Default: Enabled Options: Disabled \| Enabled |
| 4 | Click Submit All Changes . |

## Figuras

![Settings button](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478218.png)