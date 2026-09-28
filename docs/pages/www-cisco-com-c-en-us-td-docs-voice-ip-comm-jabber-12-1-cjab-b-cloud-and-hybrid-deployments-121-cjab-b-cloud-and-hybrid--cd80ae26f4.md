---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-1-cjab-b-cloud-and-hybrid-deployments-121-cjab-b-cloud-and-hybrid--cd80ae26f4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_1/cjab_b_cloud-and-hybrid-deployments_121/cjab_b_cloud-and-hybrid-deployments_121_chapter_01110.html
retrieved_at: 2026-08-21T21:14:46.295094+00:00
---

Cloud and Hybrid Deployments for Cisco Jabber 12.1

# Cloud and Hybrid Deployments for Cisco Jabber 12.1

Updated: July 17, 2018

Chapter: Remote Access

## Chapter: Remote Access

# Remote Access

## Service Discovery
                        	 Requirements Workflow

Service Discovery Requirements

DNS Requirements

Certificate Requirements

Test _collab-edge SRV Record

### Service Discovery
                           	 Requirements

DNS requirements

Certificate requirements

Test external SRV _collab-edge .

#### DNS
                              	 Requirements

The DNS requirements for service discovery through remote access are:

Configure a _collab-edge DNS SRV record on an external DNS server.

Configure a _cisco-uds DNS SRV record on the internal name server.

Optionally, for a hybrid cloud-based deployment with different domains for the IM and Presence server and the voice server,
                                          configure the Voice Services Domain to locate the DNS server with the _collab-edge record.

Jabber attempts connections to a maximum of three SSO-enabled servers, which are chosen randomly from all SSO-enabled servers
                                                that the DNS SRV records ( _collab-edge and _cisco-uds ) identify. If Jabber fails to connect three times, it considers Edge SSO unsupported.

#### Certificate
                              	 Requirements

Before you
                                    		  configure remote access, download the Cisco VCS Expressway and Cisco
                                    		  Expressway-E Server certificate. The Server certificate is used for both HTTP
                                    		  and XMPP.

For more
                                    		  information on configuring Cisco VCS Expressway certificate, see Configuring Certificates on
                                       			 Cisco VCS Expressway .

#### Test _collab-edge SRV Record

##### Test SRV
                                 	 Records

After creating your SRV records test to see if they are accessible.

Open a command prompt.

Enter nslookup .

Enter set type=SRV .

Enter the name for each of your SRV records.

For example _cisco-uds. exampledomain

Displays server and address—SRV record is accessible.

Displays _cisco-uds. exampledomain : Non-existent domain —There is an issue with your SRV record.

## Cisco Anyconnect
                        	 Deployment Workflow

Application Profiles

Automate VPN Connection

AnyConnect Documentation Reference

Session Parameters

### Cisco AnyConnect
                           	 Deployment

#### Application
                              	 Profiles

After you download
                                    		  the Cisco AnyConnect Secure Mobility Client to their device, the ASA must
                                    		  provision a configuration profile to the application.

The configuration
                                    		  profile for the Cisco AnyConnect Secure Mobility Client includes VPN policy
                                    		  information such as the company ASA VPN gateways, the connection protocol
                                    		  (IPSec or SSL), and on-demand policies.

##### ASDM

You can
                                    		  provision application profiles for Cisco Jabber for iPhone and iPad in one of
                                    		  the following ways:

We recommend that
                                    		  you use the profile editor on the ASA Device Manager (ASDM) to define the VPN
                                    		  profile for the Cisco AnyConnect Secure Mobility Client.

When you use this
                                    		  method, the VPN profile is automatically downloaded to the Cisco AnyConnect
                                    		  Secure Mobility Client after the client establishes the VPN connection for the
                                    		  first time. You can use this method for all devices and OS types, and you can
                                    		  manage the VPN profile centrally on the ASA.

For more
                                    		  information, see the Creating and
                                       			 Editing an AnyConnect Profile topic of the Cisco
                                       			 AnyConnect Secure Mobility Client Administrator Guide for your release.

##### iPCU

You can provision
                                    		  iOS devices using an Apple configuration profile that you create with the
                                    		  iPhone Configuration Utility (iPCU). Apple configuration profiles are XML files
                                    		  that contain information such as device security policies, VPN configuration
                                    		  information, and Wi-Fi, mail, and calendar settings.

Use iPCU to
                                             				create an Apple configuration profile.

For more
                                             				information, see the iPCU documentation.

Export the XML
                                             				profile as a .mobileconfig file.

Email the
                                             				.mobileconfig file to users.

After a user
                                             				opens the file, it installs the AnyConnect VPN profile and the other profile
                                             				settings to the client application.

##### MDM

You can provision
                                    		  iOS devices using an Apple configuration profile that you create with
                                    		  third-party Mobile Device Management (MDM) software. Apple configuration
                                    		  profiles are XML files that contain information such as device security
                                    		  policies, VPN configuration information, and Wi-Fi, mail, and calendar
                                    		  settings.

Use MDM to
                                             				create the Apple configuration profiles.

For
                                             				information on using MDM, see the Apple documentation.

Push the Apple
                                             				configuration profiles to the registered devices.

To provision
                                 		application profiles for Cisco Jabber for Android, use the profile editor on
                                 		the ASA Device Manager (ASDM) to define the VPN profile for the Cisco
                                 		AnyConnect Secure Mobility Client. The VPN profile is automatically downloaded
                                 		to the Cisco AnyConnect Secure Mobility Client after the client establishes the
                                 		VPN connection for the first time. You can use this method for all devices and
                                 		OS types, and you can manage the VPN profile centrally on the ASA. For more
                                 		information, see the Creating and
                                    		  Editing an AnyConnect Profile topic of the Cisco
                                    		  AnyConnect Secure Mobility Client Administrator Guide for your release.

#### Automate VPN Connection

When users open Cisco Jabber from outside the corporate Wi-Fi network, Cisco Jabber needs a VPN connection to access the Cisco
                                 UC application servers. You can set up the system to allow Cisco AnyConnect Secure Mobility Client  to automatically establish
                                 a VPN connection in the background, which helps ensure a seamless user experience.

##### Set Up Trusted Network Connection

The Trusted Network Detection feature enhances the user experience by automating the VPN connection based on the user's location.
                                       When the user is inside the corporate Wi-Fi network, Cisco Jabber can reach the Cisco UC infrastructure directly. When the
                                       user leaves the corporate Wi-Fi network,  Cisco Jabber automatically detects that it is outside the trusted network. After
                                       this occurs, Cisco AnyConnect Secure Mobility Client initiates the VPN to ensure connectivity to the UC infrastructure.

The Trusted Network Detection feature works with both certificate- and password-based authentication. However, certificate-based
                                                   authentication provides the most seamless user experience.

Using ASDM, open the Cisco AnyConnect client profile.

Enter the list of Trusted DNS Servers and Trusted DNS Domain Suffixes that an interface can receive when the client is within
                                                a corporate Wi-Fi network. The Cisco AnyConnect client compares the current interface DNS servers and domain suffix with the
                                                settings in this profile.

You must specify all your DNS servers to ensure that the Trusted Network Detection feature works properly. If you set up both
                                                               the TrustedDNSDomains and TrustedDNSServers, sessions must match both settings to be defined as a trusted network.

For detailed steps for setting up Trusted Network Detection, see the Trusted Network Detection section in the Configuring AnyConnect Features chapter (Release 2.5) or Configuring VPN Access (releases 3.0 or 3.1) of the Cisco AnyConnect Secure Mobility Client Administrator Guide for your release.

##### Set Up Connect
                                 	 On-Demand VPN

The Apple iOS
                                       		  Connect On Demand feature enhances the user experience by automating the VPN
                                       		  connection based on the user's domain.

When the user is
                                       		  inside the corporate Wi-Fi network, Cisco Jabber can reach the Cisco UC
                                       		  infrastructure directly. When the user leaves the corporate Wi-Fi network, 
                                       		  Cisco AnyConnect automatically detects if it is
                                       		  connected to a domain that you specify in the AnyConnect client profile. If so,
                                       		  the application initiates the VPN to ensure connectivity to the UC
                                       		  infrastructure. All applications on the device including 
                                       		  Cisco Jabber can take advantage of this feature.

Connect On
                                                   			 Demand supports only certificate-authenticated connections.

The following
                                       		  options are available with this feature:

Always Connect — Apple iOS always attempts to initiate a VPN connection for domains in this
                                             				list.

Connect If
                                                				  Needed — Apple iOS attempts to initiate a VPN connection to the
                                             				domains in the list only if it cannot resolve the address using DNS.

Never Connect — Apple iOS never attempts to initiate a VPN connection to domains in this list.

Apple plans to
                                                   			 remove the Always Connect option in the near future. After the Always Connect
                                                   			 option is removed, users can select the Connect If Needed option. In some
                                                   			 cases, 
                                                   			 Cisco Jabber users may have issues when using the
                                                   			 Connect If Needed option. For example, if the hostname for the 
                                                   			 Cisco Unified Communications Manager is resolvable outside the corporate
                                                   			 network, iOS will not trigger a VPN connection. The user can work around this
                                                   			 issue by manually launching 
                                                   			 Cisco AnyConnect Secure Mobility Client before making a call.

Use the ASDM
                                                			 profile editor, iPCU, or MDM software to open the AnyConnect client profile.

In the
                                                			 AnyConnect client profile, under the Connect if Needed section, enter your list
                                                			 of on-demand domains.

The domain
                                                   				list can include wild-card options (for example, cucm.cisco.com, cisco.com, and
                                                   				*.webex.com).

##### Set Up Automatic
                                 	 VPN Access on Cisco Unified Communications Manager

###### Before you begin

The mobile
                                             				device must be set up for on-demand access to VPN with certificate-based
                                             				authentication. For assistance with setting up VPN access, contact the
                                             				providers of your VPN client and head end.

For
                                             				requirements for 
                                             				Cisco AnyConnect Secure Mobility Client and 
                                             				Cisco Adaptive Security Appliance, see the Software
                                                				  Requirements topic.

For
                                             				information about setting up 
                                             				Cisco AnyConnect, see the Cisco AnyConnect VPN Client Maintain and Operate
                                                				  Guides .

Identify a URL
                                                			 that will cause the client to launch VPN on Demand.

Use one of
                                                      				  the following methods to identify a URL that will cause the client to launch
                                                      				  VPN on Demand.

Configure Cisco Unified Communications Manager to be accessed through a domain name
                                                                        								  (not an IP address) and ensure that this domain name is not resolvable outside
                                                                        								  the firewall.

Include this domain in the "Connect If Needed" list in the Connect On Demand Domain List
                                                                        								  of the 
                                                                        								  Cisco AnyConnect client connection.

Set the parameter in step 4 to a nonexistent domain. A
                                                                        								  nonexistent domain causes a DNS query to fail when the user is inside or
                                                                        								  outside the firewall.

Include this domain to the "Always Connect" list in the Connect On Demand Domain List of
                                                                        								  the 
                                                                        								  Cisco AnyConnect client connection.

The URL must include only the domain name. Do not include a
                                                                        								  protocol or a path (for example, use "cm8ondemand.company.com" instead of "https://cm8ondemand.company.com/vpn" .

Enter
                                                      				  the URL in 
                                                      				  Cisco AnyConnect and verify that a DNS query on
                                                      				  this domain fails.

Open the Cisco
                                                   				Unified CM Administration interface.

Navigate to
                                                			 the device page for the user.

In the Product Specific Configuration Layout section, in
                                                			 the On-Demand VPN URL field, enter the URL that you
                                                			 identified and used in 
                                                			 Cisco AnyConnect in Step 1.

The URL must
                                                   				be a domain name only, without a protocol or path.

Select Save .

When 
                                                   				Cisco Jabber opens, it initiates a DNS query to
                                                   				the URL (for example, ccm-sjc-111.cisco.com). If this URL matches the On-Demand
                                                   				domain list entry that you defined in this procedure (for example, cisco.com), Cisco Jabber indirectly initiates the AnyConnect
                                                   				VPN connection.

###### What to do next

Test this
                                             				feature.

Enter this
                                                   					 URL into the Internet browser on the iOS device and verify that VPN launches
                                                   					 automatically. You should see a VPN icon in the status bar.

Verify
                                                   					 that the iOS device can connect to the corporate network using VPN. For
                                                   					 example, access a web page on your corporate intranet. If the iOS device cannot
                                                   					 connect, contact the provider of your VPN technology.

Verify
                                                   					 with your IT department that your VPN does not restrict access to certain types
                                                   					 of traffic (for example, if the administrator set the system to allow only
                                                   					 email and calendar traffic).

Verify that
                                             				you set up the client to connect directly to the corporate network.

#### AnyConnect
                              	 Documentation Reference

For detailed information on AnyConnect requirements and deployments review the documentation for your release at the following: https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client/products-user-guide-list.html

#### Session Parameters

Datagram Transport Layer Security (DTLS) — DTLS is an SSL protocol that provides a data path that prevents latency and data loss.

Auto Reconnect — Auto reconnect, or session persistence, lets Cisco AnyConnect Secure Mobility Client recover from session disruptions and
                                             re-establish sessions.

Session Persistence — This parameter allows the VPN session to recover from service
                                             disruptions and re-establish the connection.

Idle Timeout — Idle timeout defines a period of time after which ASA terminates secure connections, if no communication activity occurs.

Dead-Peer Detection (DTD) — DTD ensures that ASA and Cisco AnyConnect Secure Mobility Client can quickly detect failed connections.

##### Set ASA Session Parameters

Cisco recommends that you set up the ASA session parameters as
                                       follows to optimize the end user experience for Cisco AnyConnect Secure Mobility Client.

Set up Cisco AnyConnect to use DTLS.

For more information, see the Enabling Datagram Transport Layer Security
                                                      (DTLS) with AnyConnect (SSL) Connections topic in the Configuring AnyConnect Features Using
                                                      ASDM chapter of the Cisco AnyConnect VPN Client Administrator Guide,
                                                      Version 2.0 .

Set up session persistence (auto-reconnect).

Use ASDM to open the VPN client profile.

Set the Auto Reconnect
                                                         Behavior parameter to Reconnect
                                                         After Resume .

For more information, see the Configuring Auto Reconnect topic in the Configuring AnyConnect Features chapter (Release 2.5) or Configuring VPN Access chapter (releases 3.0 or 3.1) of the Cisco AnyConnect Secure Mobility Client Administrator Guide for your release.

Set the idle timeout value.

Create a group policy that is specific to Cisco Jabber clients.

Set the idle timeout value to 30 minutes.

For more information, see the vpn-idle-timeout section of the Cisco ASA 5580 Adaptive Security Appliance Command Reference for your release

Set up Dead Peer Detection (DPD).

Disable server-side DPD.

Enable client-side DPD.

For more information, see the Enabling and Adjusting Dead Peer Detection topic of the Configuring VPN chapter of the Cisco ASA 5500 Series Configuration Guide using the CLI, 8.4 and 8.6 .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Service Discovery Requirements |  |
| Step 2 | DNS Requirements |  |
| Step 3 | Certificate Requirements |  |
| Step 4 | Test _collab-edge SRV Record |  |

| Note | Jabber attempts connections to a maximum of three SSO-enabled servers, which are chosen randomly from all SSO-enabled servers
                                                that the DNS SRV records ( _collab-edge and _cisco-uds ) identify. If Jabber fails to connect three times, it considers Edge SSO unsupported. |
|---|---|

| Step 1 | Open a command prompt. |
|---|---|
| Step 2 | Enter nslookup . The default DNS server and address is displayed. Confirm
                                                			 that this is the expected DNS server. |
| Step 3 | Enter set type=SRV . |
| Step 4 | Enter the name for each of your SRV records. For example _cisco-uds. exampledomain Displays server and address—SRV record is accessible. Displays _cisco-uds. exampledomain : Non-existent domain —There is an issue with your SRV record. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Application Profiles |  |
| Step 2 | Automate VPN Connection |  |
| Step 3 | AnyConnect Documentation Reference |  |
| Step 4 | Session Parameters |  |

| Note | VPN will not be launched because Expressway for Mobile and Remote Access has the higher connection priority even if VPN is
                                          set to automatic connection. |
|---|---|

| Note | The Trusted Network Detection feature works with both certificate- and password-based authentication. However, certificate-based
                                                   authentication provides the most seamless user experience. |
|---|---|

| Step 1 | Using ASDM, open the Cisco AnyConnect client profile. |
|---|---|
| Step 2 | Enter the list of Trusted DNS Servers and Trusted DNS Domain Suffixes that an interface can receive when the client is within
                                                a corporate Wi-Fi network. The Cisco AnyConnect client compares the current interface DNS servers and domain suffix with the
                                                settings in this profile. Note You must specify all your DNS servers to ensure that the Trusted Network Detection feature works properly. If you set up both
                                                               the TrustedDNSDomains and TrustedDNSServers, sessions must match both settings to be defined as a trusted network. For detailed steps for setting up Trusted Network Detection, see the Trusted Network Detection section in the Configuring AnyConnect Features chapter (Release 2.5) or Configuring VPN Access (releases 3.0 or 3.1) of the Cisco AnyConnect Secure Mobility Client Administrator Guide for your release. | Note | You must specify all your DNS servers to ensure that the Trusted Network Detection feature works properly. If you set up both
                                                               the TrustedDNSDomains and TrustedDNSServers, sessions must match both settings to be defined as a trusted network. For detailed steps for setting up Trusted Network Detection, see the Trusted Network Detection section in the Configuring AnyConnect Features chapter (Release 2.5) or Configuring VPN Access (releases 3.0 or 3.1) of the Cisco AnyConnect Secure Mobility Client Administrator Guide for your release. |
| Note | You must specify all your DNS servers to ensure that the Trusted Network Detection feature works properly. If you set up both
                                                               the TrustedDNSDomains and TrustedDNSServers, sessions must match both settings to be defined as a trusted network. For detailed steps for setting up Trusted Network Detection, see the Trusted Network Detection section in the Configuring AnyConnect Features chapter (Release 2.5) or Configuring VPN Access (releases 3.0 or 3.1) of the Cisco AnyConnect Secure Mobility Client Administrator Guide for your release. |

| Note | You must specify all your DNS servers to ensure that the Trusted Network Detection feature works properly. If you set up both
                                                               the TrustedDNSDomains and TrustedDNSServers, sessions must match both settings to be defined as a trusted network. For detailed steps for setting up Trusted Network Detection, see the Trusted Network Detection section in the Configuring AnyConnect Features chapter (Release 2.5) or Configuring VPN Access (releases 3.0 or 3.1) of the Cisco AnyConnect Secure Mobility Client Administrator Guide for your release. |
|---|---|

| Note | Connect On
                                                   			 Demand supports only certificate-authenticated connections. |
|---|---|

| Attention | Apple plans to
                                                   			 remove the Always Connect option in the near future. After the Always Connect
                                                   			 option is removed, users can select the Connect If Needed option. In some
                                                   			 cases, 
                                                   			 Cisco Jabber users may have issues when using the
                                                   			 Connect If Needed option. For example, if the hostname for the 
                                                   			 Cisco Unified Communications Manager is resolvable outside the corporate
                                                   			 network, iOS will not trigger a VPN connection. The user can work around this
                                                   			 issue by manually launching 
                                                   			 Cisco AnyConnect Secure Mobility Client before making a call. |
|---|---|

| Step 1 | Use the ASDM
                                                			 profile editor, iPCU, or MDM software to open the AnyConnect client profile. |
|---|---|
| Step 2 | In the
                                                			 AnyConnect client profile, under the Connect if Needed section, enter your list
                                                			 of on-demand domains. The domain
                                                   				list can include wild-card options (for example, cucm.cisco.com, cisco.com, and
                                                   				*.webex.com). |

| Step 1 | Identify a URL
                                                			 that will cause the client to launch VPN on Demand. Use one of
                                                      				  the following methods to identify a URL that will cause the client to launch
                                                      				  VPN on Demand. Connect if Needed Configure Cisco Unified Communications Manager to be accessed through a domain name
                                                                        								  (not an IP address) and ensure that this domain name is not resolvable outside
                                                                        								  the firewall. Include this domain in the "Connect If Needed" list in the Connect On Demand Domain List
                                                                        								  of the 
                                                                        								  Cisco AnyConnect client connection. Always Connect Set the parameter in step 4 to a nonexistent domain. A
                                                                        								  nonexistent domain causes a DNS query to fail when the user is inside or
                                                                        								  outside the firewall. Include this domain to the "Always Connect" list in the Connect On Demand Domain List of
                                                                        								  the 
                                                                        								  Cisco AnyConnect client connection. The URL must include only the domain name. Do not include a
                                                                        								  protocol or a path (for example, use "cm8ondemand.company.com" instead of "https://cm8ondemand.company.com/vpn" . Enter
                                                      				  the URL in 
                                                      				  Cisco AnyConnect and verify that a DNS query on
                                                      				  this domain fails. |
|---|---|
| Step 2 | Open the Cisco
                                                   				Unified CM Administration interface. |
| Step 3 | Navigate to
                                                			 the device page for the user. |
| Step 4 | In the Product Specific Configuration Layout section, in
                                                			 the On-Demand VPN URL field, enter the URL that you
                                                			 identified and used in 
                                                			 Cisco AnyConnect in Step 1. The URL must
                                                   				be a domain name only, without a protocol or path. |
| Step 5 | Select Save . When 
                                                   				Cisco Jabber opens, it initiates a DNS query to
                                                   				the URL (for example, ccm-sjc-111.cisco.com). If this URL matches the On-Demand
                                                   				domain list entry that you defined in this procedure (for example, cisco.com), Cisco Jabber indirectly initiates the AnyConnect
                                                   				VPN connection. |

| Step 1 | Set up Cisco AnyConnect to use DTLS. For more information, see the Enabling Datagram Transport Layer Security
                                                      (DTLS) with AnyConnect (SSL) Connections topic in the Configuring AnyConnect Features Using
                                                      ASDM chapter of the Cisco AnyConnect VPN Client Administrator Guide,
                                                      Version 2.0 . |
|---|---|
| Step 2 | Set up session persistence (auto-reconnect). Use ASDM to open the VPN client profile. Set the Auto Reconnect
                                                         Behavior parameter to Reconnect
                                                         After Resume . For more information, see the Configuring Auto Reconnect topic in the Configuring AnyConnect Features chapter (Release 2.5) or Configuring VPN Access chapter (releases 3.0 or 3.1) of the Cisco AnyConnect Secure Mobility Client Administrator Guide for your release. |
| Step 3 | Set the idle timeout value. Create a group policy that is specific to Cisco Jabber clients. Set the idle timeout value to 30 minutes. For more information, see the vpn-idle-timeout section of the Cisco ASA 5580 Adaptive Security Appliance Command Reference for your release |
| Step 4 | Set up Dead Peer Detection (DPD). Disable server-side DPD. Enable client-side DPD. For more information, see the Enabling and Adjusting Dead Peer Detection topic of the Configuring VPN chapter of the Cisco ASA 5500 Series Configuration Guide using the CLI, 8.4 and 8.6 . |