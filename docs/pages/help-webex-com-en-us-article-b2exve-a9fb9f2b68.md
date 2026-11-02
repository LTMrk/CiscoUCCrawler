---
doc_id: help-webex-com-en-us-article-b2exve-a9fb9f2b68
source_url: https://help.webex.com/en-us/article/b2exve
retrieved_at: 2026-11-02T13:00:59.875116+00:00
---

A correctly configured firewall and proxy are essential for a successful Calling deployment. Webex Calling uses SIP and HTTPS for call signaling and the associated addresses and ports for media, network connection, and gateway connectivity as Webex Calling is a global service.

Not all firewall configurations require ports to be open. However, if you're running inside-to-outside rules, you must open ports for the required protocols to let out services.

## Network Address Translation (NAT)

Network Address Translation (NAT) and Port Address Translation (PAT) functionality are applied at the border between two networks to translate address spaces or to prevent the collision of IP address spaces.

Organizations use gateway technologies like firewalls and proxies that provide NAT or PAT services to provide internet access to Webex App applications or Webex devices that are on a private IP address space. These gateways make traffic from internal Apps or Devices to the internet appear to be coming from one or more publicly routable IP addresses.

If deploying NAT, it’s not mandatory to open an inbound port on the firewall.

Validate the NAT pool size required for App or Devices connectivity when multiple app users and devices access Webex Calling & Webex aware services using NAT or PAT. Ensure that adequate public IP addresses are assigned to the NAT pools to prevent port exhaustion. Port exhaustion contributes to internal users and devices being unable to connect to the Webex Calling and Webex Aware services.

When multiple Webex Calling devices share a public IP address through NAT or PAT,
            ensure that the NAT device can translate overlapping source ports to unique translated
            source ports. Webex Calling devices may use the same SIP signaling source port within
            the 5060–5280 range. Avoid strict source-port preservation configurations that prevent
            the NAT device from translating a source port when a conflict occurs because these
            configurations can cause device registration failures.

Define reasonable binding periods and avoid manipulating SIP on the NAT device.

Configure a minimum NAT timeout to ensure proper operation of devices. Example: Cisco phones send a follow-up REGISTER refresh message every 1-2 minutes.

If your network implements NAT or SPI, then set a larger timeout (of at least 30 minutes) for the connections. This timeout allows reliable connectivity while reducing the battery consumption of the users' mobile devices.

## SIP Application Layer Gateway

If a router or firewall is SIP Aware, implying that the SIP Application Layer Gateway (ALG) or similar is enabled, we recommend you turn off this functionality for accurate operation of the service. Although all Webex Calling traffic is encrypted, certain SIP ALG implementations can cause issues with firewall traversal. Therefore, we recommend switching off the SIP ALG to ensure a high quality service.

Check the relevant manufacturer's documentation for steps to disable SIP ALG on specific devices.

## Proxy support for Webex Calling

Organizations deploy an internet firewall or internet proxy and firewall, to inspect, restrict, and control the HTTP traffic that leaves and enters their network. Thus protecting their network from various forms of cyberattacks.

Organizations often configure proxy servers as the only route for forwarding HTTP-based internet traffic to the enterprise firewall. This configuration enables the firewall to restrict outbound internet traffic, allowing only traffic that originates from the proxy server

Proxies perform several security functions such as:

Allow or block access to specific URLs.

User authentication

IP address/domain/hostname/URI reputation lookup

Traffic decryption and inspection

On configuring the proxy feature, it applies to all the applications that use the HTTP's protocol.

The Webex App and Webex device applications include the following:

Webex Services

Customer device activation (CDA) procedures using Cisco Cloud provisioning platform such as GDS, EDOS device activation, provisioning & onboarding to Webex cloud.

Certificate Authentication

Firmware Upgrades

Status Reports

PRT Uploads

XSI Services

Do not alter or delete HTTP header values as they pass through your proxy or firewall unless permitted by these guidelines altering-header-values . Modifying or removing HTTP headers outside of these guidelines can impact access to Webex Calling and Webex-Aware services, and may cause Webex Apps and devices to lose access.

If a proxy server address is configured, then only the Signaling traffic (HTTP/HTTPS) is sent to the proxy server. Clients that use SIP to register to the Webex Calling service and the associated media aren’t sent to the proxy. Therefore, allow these clients to go through the firewall directly.

### Supported Proxy Options, configuration & Authentication types

The supported proxy types are:

Explicit Proxy (inspecting or noninspecting)—Configure the clients either App or Device with explicit proxy to specify the server to use.

Transparent Proxy (noninspecting)—The Clients aren’t configured to use a specific proxy server address and don’t require any changes to work with a noninspecting proxy.

Transparent Proxy (inspecting)—The Clients aren’t configured to use a specific proxy server address. No HTTP's configuration changes are necessary; however, your clients either App or Devices need a root certificate so that they trust the proxy. The IT team uses the inspecting proxies to enforce policies on the websites to visit and the types of content that aren’t permitted.

Configure the proxy addresses manually for the Cisco devices and the Webex App using:

Platform OS

Device UI

Automatically discovered using Web Proxy mechanisms such as:

Web Proxy Auto Discovery (WPAD) - Web Proxy Auto Discovery Protocol

Proxy Auto Config (PAC) files - Proxy Auto-Config Files

While configuring your preferred product types, choose from the following Proxy configurations & authentication types in the table:

Product

Proxy Configuration

Authentication Type

Webex for Mac

Manual, WPAD, PAC

No Auth, Basic, NTLM, †

Webex for Windows

Manual, WPAD, PAC, GPO

No Auth, Basic, NTLM, † , Negotiate †

Webex for iOS

Manual, WPAD, PAC

No Auth, Basic, Digest, NTLM

Webex for Android

Manual, PAC

No Auth, Basic, Digest, NTLM

Webex Web App

Supported through OS

No Auth, Basic, Digest, NTLM, Negotiate †

Webex Devices

WPAD, PAC, or Manual

No Auth, Basic, Digest

Cisco IP Phones

Manual, WPAD, PAC

No Auth, Basic, Digest

Webex Video Mesh Node

Manual

No Auth, Basic, Digest, NTLM

For legends in the table:

† Mac NTLM Auth - Machine need not be logged on to the domain, user prompted for a password

† Windows NTLM Auth - Supported only if a machine is logged onto the domain

Negotiate † - Kerberos with NTLM fallback auth.

To connect a Cisco Webex Board, Desk, or Room Series device to a proxy server, see Connect your Board, Desk, or Room Series device to a proxy server .

For Cisco IP phones, see Set Up a Proxy Server as an example for configuring the proxy server and settings.

For No Authentication , configure the client with a proxy address that doesn’t support authentication. When using Proxy Authentication , configure with valid credentials. Proxies that inspect web traffic may interfere with web socket connections. If this problem occurs, bypassing the not inspecting traffic to *.Webex.com might solve the problem. If you already see other entries, add a semicolon after the last entry, and then enter the Webex exception.

Proxy settings for Windows OS

Microsoft Windows support two network libraries for HTTP traffic (WinINet and WinHTTP) that allow Proxy configuration.WinINet is a superset of WinHTTP.

WinInet is designed for single-user, desktop client applications

WinHTTP is designed primarily for multiuser, server-based applications

When selecting between the two, choose WinINet for your proxy configuration settings. For details, see wininet-vs-winhttp .

Refer to Configure a list of allowed domains to access Webex while on your corporate network for details on the following:

To ensure that people only sign in to applications using accounts from a predefined list of domains.

Use a proxy server to intercept requests and limit the domains that are allowed.

Proxy Inspection and Certificate Pinning

The Webex App and Devices validate the certificates of the servers when they establish the TLS sessions. Certificate checks that such as the certificate issuer and digital signature rely on verifying the chain of certificates up to the root certificate. To perform the validation checks, the Webex App and Devices use a set of trusted root CA certificates installed in the operating system trust store.

If you have deployed a TLS-inspecting Proxy to intercept, decrypt and inspect Webex Calling traffic. Ensure that the certificate the Proxy presents (instead of the Webex service certificate) is signed by a certificate authority, and the root certificate is installed in the trust store of your Webex App or Webex device.

For Webex App - Install the CA certificate that is used to sign the certificate by the proxy in the operating system of the device.

For Webex Room devices and Cisco multiplatform IP Phones - Open a service request with the TAC team to install the CA certificate.

This table shows the Webex App and Webex Devices that support TLS inspection by Proxy servers

Product

Supports Custom Trusted CAs for TLS inspection

Webex App (Windows, Mac, iOS, Android, Web)

Yes

Webex Room Devices

Yes

Cisco IP Multiplatform (MPP) Phones

Yes

## Firewall configuration

Cisco supports Webex Calling and Webex Aware services in secure Cisco and Amazon Web Services (AWS) data centers. Amazon
      has reserved its IP subnets for Cisco’s sole use, and secured the services located in these
      subnets within the AWS virtual private cloud.

Configure your firewall to allow communication from your devices, App's applications, and
      internet-facing services to perform their functions properly. This configuration allows access
      to all the supported Webex Calling and Webex Aware cloud services, domain names, IP addresses, Ports, and protocols.

Whitelist or open access to the following so that the Webex Calling and Webex Aware services function correctly.

The URLs/Domains mentioned under the section Domains and URLs for Webex Calling
            Services and the IP subnets, ports, and protocols listed under the section IP
            Subnets for Webex Calling Services are utilized for multiple purposes including call
          signaling, media traffic to and from Webex Calling, Network Time Protocol (NTP)
          synchronization, and CScan network readiness testing for those IP subnets.

If your organization uses the Webex Suite of cloud collaboration services—including Webex
          Meetings, Messaging, Webex Attendant Console, Webex edge connect private network peering
          connection to Webex backbone, and other related services, then ensure that the IP subnets,
          domains, and URLs specified in the articles Network Requirements for Webex Services , Webex Edge
            Connect , and Network requirements for Attendant console are
          allowed through your network. This is necessary to guarantee proper connectivity and
          functionality of these Webex services.

### Webex Calling traffic through proxies and firewalls

If you’re using only a firewall, then filtering Webex Calling traffic using IP addresses alone isn’t supported as some of the IP address pools are
        dynamic and may change at any time. Cisco doesn’t endorse filtering a subset of IP addresses
        based on a particular geographic region or cloud service provider. Filtering by region can
        cause severe degradation to the Calling experience.

Cisco doesn't maintain dynamically changing IP address pools hence it isn’t listed in
          this article. Update your rules regularly, failing to update your firewall rules list
          could impact your users' experience.

If your firewall doesn’t support Domain/URL filtering, then use an Enterprise Proxy server
        option. This option filters/allows by URL/domain the HTTPs signaling traffic to Webex Calling and Webex Aware services in your Proxy server, before forwarding to your firewall.

While using enterprise proxy server option to filter Domain/URLs, note that it is not
        designed to handle interactive audio and video, it is only for the HTTPS signaling traffic.
        Always use:

Port and IP subnet based filtering for Call signaling & Media

Domain/URL filtering are for HTTP(s) signaling traffic

For Webex Calling, UDP is Cisco’s preferred transport protocol for media, and it recommends using only SRTP
        over UDP. TCP and TLS as transport protocols for media aren’t supported for Webex Calling in production environments. The connection-orientated nature of these protocols affects
        media quality over network loss. If you have queries regarding the transport protocol, raise
        a support ticket.

### Domains and URLs for Webex Calling services

A * shown at the beginning of a URL (for example, *.webex.com) indicates that services in
        the top-level domain and all subdomains are accessible.

Domain / URL

Description

Webex Apps and devices using these domains / URLs

Cisco Webex Calling and Webex Aware services

*.broadcloudpbx.com

Webex authorization microservices for cross-launch from Control Hub to Calling
                  Admin Portal.

Control Hub

*.broadcloud.com.au

Webex Calling services in Australia.

All

*.broadcloud.eu

Webex Calling services in Europe.

All

*.broadcloudpbx.net

Calling client configuration and management services.

Webex Apps

*.webex.com

*.cisco.com

Core Webex Calling & Webex Aware services

Identity provisioning

Identity storage

Authentication

OAuth services

Device onboarding

Cloud Connected UC

When a phone connects to a network for the first time or after a factory reset
                  with no DHCP options set, it contacts a device activation server for zero touch
                  provisioning. New phones use activate.cisco.com and phones with firmware release
                  earlier than 11.2(1), continue to use webapps.cisco.com for provisioning.

Download the device firmware and locale updates from binaries.webex.com .

Allow Cisco Multiplatform phones (MPPs) older than 12.0.3 version to access sudirenewal.cisco.com through port 80 to renew Manufacturer Installed
                  Certificate (MIC) and have a Secure Unique Device Identifier (SUDI). For details,
                  see Field notice .

If you are not using a proxy server and only using a firewall to filter the URLs,
                  then add CNAME *.cloudfront.net to allow the list.

All

*.ucmgmt.cisco.com

Webex Calling services

Control Hub

*.wbx2.com and *.ciscospark.com

Used for cloud awareness to reach out to Webex Calling & Webex Aware services
                  during and after onboarding.

These services are necessary for

Apps and Devices management

Apps Application notification mechanism service management

All

*.webexapis.com

Webex microservices that manage your Webex App applications and Webex devices.

Profile picture service

Whiteboarding service

Proximity service

Presence service

Registration service

Calendar service

Search service

All

*.webexcontent.com

Webex Messaging services related to general file storage including:

User files

Transcoded files

Images

Screenshots

Whiteboard content

Client & device logs

Profile pictures

Branding logos

Log files

Bulk CSV export files & import files (Control Hub)

Webex Apps Messaging services.

File storage using webexcontent.com replaced by clouddrive.com in October
                    2019

*.accompany.com

People insights integration

Webex Apps

Additional Webex related services (Third-Party Domains)

*.appdynamics.com

*.eum-appdynamics.com

Performance tracking, error and crash capture, session metrics.

Webex App, Webex web App

*.sipflash.com

Device management services. Firmware upgrades and secure onboarding purposes.

Webex Apps

*.walkme.com *.walkmeusercontent.com

Webex user guidance client. Provides onboarding and usage tours for new
                  users.

For more information about WalkMe, click here .

Webex Apps

*.google.com

*.googleapis.com

Notifications to Webex apps on mobile devices (Example: new message, when call is
                  answered)

For IP Subnets, refer to these links

Google Firebase Cloud Messaging (FCM)
                    service

Apple Push Notification Service (APNS)

For APNS, Apple lists the IP subnets for this service.

api.wxc.e911cloud.com

wxc.e911cloud.com

911 (E911) emergency service (RedSky) integration with Webex Calling

The phone and Webex client communicate to the RedSky service by using port 443

See the article e911 service integration with Webex
                    Calling for details.

Webex App, Devices

*.quovadisglobal.com

*.digicert.com

*.identrust.com

*.godaddy.com

This is used to check the 'Certificate Revocation List' for the security
                  certificates. The Certificate Revocation List ensure that no compromised
                  certificates can be used to intercept secure Webex traffic. that occurs on TCP
                  Port 80.

Webex Calling supports both CRL and OCSP stapling to determine certificate
                    revocation status. While OCSP stapling reduces the need for the Webex App to
                    contact CAs; devices may still contact Certificate Authorities directly. This
                    process validates the hardware identity, perform 802.1X network authentication,
                    or download CRLs if a stapled response is unavailable or invalid.

### IP Subnets for Webex Calling services

HTTPS signaling- The session establishment for Webex Calling and Webex Aware services are
        based on URLs rather than IP addresses. Network firewalls/proxies must allow access to
        Domains/URLs too, not just IP range.

IP subnets for Webex Calling services * †

(1) Call Signaling, Media, NTP & CScan

23.89.0.0/16

62.109.192.0/18

85.119.56.0/23

128.177.14.0/24

128.177.36.0/24

135.84.168.0/21

139.177.64.0/21

139.177.72.0/23

144.196.0.0/16

150.253.128.0/17

163.129.0.0/17

170.72.0.0/16

170.133.128.0/18

185.115.196.0/22

199.19.196.0/23

199.19.199.0/24

199.59.64.0/21

(2) Device configuration and firmware management (Cisco devices)

3.14.211.49

3.20.185.219

3.130.87.169

3.134.166.179

52.26.82.54

62.109.192.0/18

72.163.10.96/27

72.163.15.64/26

72.163.15.128/26

72.163.24.0/23

72.163.10.128/25

173.37.146.128/25

173.36.127.0/26

173.36.127.128/26

173.37.26.0/23

173.37.149.96/27

192.133.220.0/26

192.133.220.64/26

(3) Webex App configuration

62.109.192.0/18

64.68.96.0/19

150.253.128.0/17

207.182.160.0/19

Connection purpose

Protocol

These IPs/ports are needed for outbound SIP-TLS call signaling from Local
                  Gateways, Devices, and Webex App Applications (Source) to Webex Calling Cloud
                  (Destination).

Port 5062 (required for Certificate-based trunk). And port 8934 (required for
                  Registration-based trunk

Webex Calling address range.

Refer to IP Subnets for Webex Calling Services (1)

Applies to certificate-based local gateways. It is required to establish a
                  connection from Webex Calling to a Local Gateway.

A Registration-based local gateway works on reusing a connection created from the
                  local gateway.

Destination port is customer chosen Configure trunks

5004, 9000, 8500—8699, 19560—65535 (SRTP over UDP)

These IPs/ports are used for outbound SRTP call media from Local Gateways,
                      Devices, and Webex App Applications (Source) to Webex Calling Cloud
                      (Destination).

For Calls within the organization where STUN, ICE negotiation is successful,
                      the media relay in the cloud is removed as the communication path. In such
                      cases the media flow is directly between the user's Apps/devices.

For Example: If media optimization is successful, Webex App sends media
                      directly between one another on port ranges 8500–8699 and devices send media
                      directly to one another on ports ranges 19560–19661.

For certain network topologies where firewalls are used within a customer
                      premise, allow access for the mentioned source and destination port ranges
                      inside your network for the media to flow through.

Example: For Webex App, allow the source and destination port range

Audio: 8500-8599 Video:8600-8699

Browsers use the ephemeral source port that can be controlled by setting the
                        WebRtcUdpPortRangepolicy in the Managed Device Management (MDM)
                      profile.

The Webex Calling service behaves normally if no MDM Service is set or if
                      SiteURL and EnableForceLogin aren't configured.

52050-52099

52200-52299

VG400 ATA Devices

Audio: 8500-8599

Video: 8600-8699

WebRTC

Webex Calling address range.

Refer to IP Subnets for Webex Calling Services (1)

Applies to certificate-based local gateways

TCP

Refer to IP Subnets for Webex Calling Services (2)

Required for the following reasons:

Migrating from Enterprise phones (Cisco Unified CM) to Webex Calling. See upgrade.cisco.com for more information. The
                        cloudupgrader.webex.comuses ports: 6970,443 for the firmware
                      migration process.

Firmware upgrades and secure onboarding of devices (MPP and Room or Desk phones)
                  using the 16-digit activation code (GDS)

For CDA / EDOS - MAC address-based provisioning. Used by devices (MPP phones,
                  ATAs, and SPA ATAs) with newer firmware.

For Cisco ATAs, ensure that the devices are on the minimum firmware of
                  11.1.0MSR3-9.

When a phone connects to a network for the first time or after a factory reset,
                  without the DHCP options set, it contacts a device activation server for zero
                  touch provisioning. New phones  use activate.cisco.com instead of webapps.cisco.com for provisioning. Phones with firmware released
                  earlier than 11.2(1) continue to use webapps.cisco.com . It’s recommended to
                  allow all these IP subnets.

Allow Cisco Multiplatform phones (MPPs) older than 12.0.3 version to access sudirenewal.cisco.com through port 80 for renewing the Manufacturer
                  Installed Certificate (MIC) and having a Secure Unique Device Identifier (SUDI).
                  For details, see Field Notice

Refer to IP Subnets for Webex Calling Services (3)

The TCP port 8443 is used by Webex App on Cisco Unified CM setup for
                  downloading configuration. Only customers who use the setup to connect to Webex
                  Calling must open the port.

Domain Name System (DNS) resolution

Refer to IP Subnets mentioned under the links

Apple Push Notification Service(APNS)

Google-Firebase Cloud Messaging (FCM)

† * Local gateway media port range is configurable with rtp-port
              range .

† * Media ports for devices and applications that are dynamically assigned in
              the SRTP port rages. SRTP ports are even numbered ports, and the corresponding SRTCP
              port is allocated with the consecutive odd numbered port.

If a proxy server address is configured for your Apps and Devices, the signaling
              traffic is sent to the proxy. Media transported SRTP over UDP flows directly to your
              firewall instead of the proxy server.

If you’re using NTP and DNS services within your enterprise network, you must still
              allow outbound DNS (UDP/TCP 53) and NTP (UDP 123) traffic through your firewall
              for Webex Calling and Webex Aware services. While your internal DNS handles local look
              ups, for Webex services; devices and Apps must resolve external service FQDNs and SRV
              records. Devices such as IP phones often reach public NTP servers or Webex Calling's
              own time servers to keep their internal clocks synchronized, which is critical for
              call security and registration.

### MTU size for Webex Calling & Webex Aware services

The Maximum Transmissible Unit (MTU) is the largest size an IP packet can transmist over a
        network link without needing fragmentation. Problems can occur if the MTU is not set to
        default values. Webex Calling advises maintaining the default MTU size of 1500 bytes for all
        IP packets on your network.

For Webex Calling and Webex Aware services, if a packet needs fragmentation, set the Don't
        Fragment (DF) bit to necessitate ICMP communication.

### Quality of Service (QoS)/Type of Service(ToS)

Allows you to enable tagging of packets from the local device or client to the Webex
        Calling cloud platform. QoS enables you to prioritize real-time traffic over other data
        traffic. Enabling this setting modifies the QoS markings for Apps and devices that use SIP
        signaling and media.

Refer IP subnets, Domains, and URLs for Webex Calling services

Expedited Forwarding (46) &

Assured Forwarding 41 (34)

Create a separate QoS profile for Audio and Video/Share since they have different
              source port range to mark traffic differently.

For Windows Clients: To enable UDP Source Port Differentiation for your organization,
              contact your local account team. Without enabling, you cannot differentiate between
              the Audio and Video/Share using the Windows QoS Policies (GPO) because the source
              ports are the same for audio/video/share. For details, see Enable media
                source port ranges for Webex App

For Webex Devices, configure the QoS setting changes from the Control Hub device
              settings. For details, see Configure & modify device settings in
                Webex-Calling

### Webex Meetings/Messaging - Network Requirements

For customers who’re using Webex Suite of cloud collaboration services, Webex cloud
        registered products, onboard the MPP devices to the Webex Cloud for services like Call
        History, Directory Search, Meetings, and Messaging. Ensure that the Domains/URLs/IP
        Addresses/Ports mentioned in this article are open Network Requirements for Webex Services .

### Network requirements for Webex for Government

For customers who require the list of Domains, URLs, IP address ranges and ports for Webex
        for Government services, information can be found here: Network requirements for Webex for Government

### Network requirements for Webex Attendant Console

For customers who are using attendant console - receptionists, attendants, and operators
        feature, ensure Domains/URLs/IP Addresses/Ports/Protocols are open Network requirements for attendant console

### Getting started with Webex Calling Local Gateway

For customers using the Local Gateway solution with Webex Calling for premises-based PSTN
        and third-party SBCs interoperability, read through the article Get Started with
          Local Gateway

### References

To know What's new in Webex Calling, see What's new in Webex Calling

For Security requirements for Webex Calling, see Article

Webex Calling Media Optimization with Interactive Connectivity Establishment (ICE) Article

## Document revision history

Date

We've made the following changes to this article

September 07, 2026

Expanded the phone’s source port range from 5060-5080 to 5060-5280 to accommodate
                  the updated Cisco feature, enabling support for up to 130 lines.

August 13, 2026

Updated the procedure to validate the NAT pool size required for App or
                  Devices.

March 28, 2026

Updated the link to the Firebase Cloud Messaging (FCM) documentation.

March 4, 2026

Changed the source port for Device time synchronization (NTP) from 51494 to
                  Ephemeral under the IP Subnets for Webex Calling Services section.

February 23, 2026

The purpose of connection details is updated within the IP subnet for Webex
                  Calling

The following additional third-party URLs are included:

*.quovadisglobal.com, *.digicert.com, *.identrust.com and *.godaddy.com as
                      Webex App requests CRL list from the certificate authorities.

Referenced api.wxc.e911cloud.com, wxc.e911cloud.com (E911) emergency service
                      (RedSky) integration with Webex Calling.

Editorial updates to enhance the article for better readability

December 05, 2025

Added the usage of the IP subnets, ports, and protocols that are listed under the IP Subnets for Webex Calling Services section.

October 24, 2025

Improved the image quality and fixed the broken link to Google Firebase Cloud
                  Messaging (FCM) service

September 15, 2025

Added IP address 3.14.211.49 to the list of IP subnets used for Cisco device
                      configuration and firmware management. This address is required for manual MPP
                      migrations using the alternate TFTP method.

Updated the Signaling & Media source port range for Room Series
                      devices.

Removed the dependency on Control Hub from the list of Domains & URLs for
                      Webex Calling services under “Additional Webex related services (Third-Party
                      Domains).”

Made overall design tweaks

April 10, 2025

Included text to emphasize the MTU size for Webex Calling and Webex Aware
                  services

March 27, 2025

Updated the IP Subnet for Webex Calling services 62.109.192.0/18 to accommodate
                  Webex Calling market expansion for the Saudi Arabia region.

January 21, 2025

Added details for using the SIP Application Layer Gateway.

January 8, 2025

Moved the IP subnet address related to Device configuration and Webex App
                  configuration to the IP Subnets for Webex Calling services section

December 17, 2024

Added support to WebRTC for the Webex Calling Media specification.

November 14, 2024

Updated the supported port range for Webex Calling call media for VG400 series
                  ATA device

November 11, 2024

Added the supported port range for Webex Calling call media for VG400 series ATA
                  device

July 25, 2024

Added back the 52.26.82.54 IP subnet as it’s required for the Cisco ATA device
                  configuration and firmware management.

July 18, 2024

Updated with the following details:

QoS (TOS/DSCP) values supported for Webex Calling (Apps, Devices)

Updated the Network diagram

Including the link for network requirements related to Webex Attendant
                      Console.

June 28, 2024

Updated the usage of both SRTP/ SRTCP port ranges for the Webex Calling Media
                  specification.

June 11, 2024

Removed the "huron-dev.com" domain as it’s not used.

May 06, 2024

Updated the usage of both SRTP/ SRTCP port ranges for the Webex Calling Media
                  specification.

April 03, 2024

December 18, 2023

Included the sudirenewal.cisco.com URL and port 80 requirement for
                  device configuration and firmware management of the Cisco MPP phone's MIC renewal.

December 11, 2023

Updated the IP Subnets for Webex Calling services to include a larger set of IP
                  addresses.

150.253.209.128/25 – changed to 150.253.128.0/17

November 29, 2023

Updated the IP Subnets for Webex Calling services to include a larger set of IP
                  addresses to accommodate Webex Calling region expansion for future growth.

144.196.33.0/25 – changed to 144.196.0.0/16

The IP Subnets for Webex Calling services sections under Webex Calling (SIP TLS)
                  and Call media to Webex Calling (STUN, SRTP) is updated for clarity on
                  certificate-based trunking and the firewall requirements for Local Gateway.

August 14, 2023

We’ve added the following IP addresses 144.196.33.0/25 and 150.253.156.128/25 to
                  support increased capacity requirements for Edge and Webex Calling Services.

This IP range is supported only in the U.S. region.

July 5, 2023

Added the link https://binaries.webex.com to install the Cisco MPP
                  Firmware.

March 7, 2023

We've overhauled the entire article to include:

Included options for Proxy support.

Modified Calling flow diagram

Simplified Domains/URLs/IP subnet portions for Webex Calling and Webex Aware
                      services

Added 170.72.0.0/16 IP subnet range for Webex Calling & Webex Aware
                      services.

Removed the following ranges 170.72.231.0, 170.72.231.10, 170.72.231.161 and
                      170.72.242.0/24

March 5, 2023

Updating the article to include the following:

Added the UDP-SRTP port range (8500-8700) used by applications.

Added the ports for the Push notifications APNS and FCM services.

Split the CScan port range for UDP & TCP.

Added the references section.

November 15, 2022

We’ve added the following IP addresses for device configuration and firmware
                  management (Cisco devices):

170.72.231.0

170.72.231.10

170.72.231.161

We’ve removed the following IP addresses from device configuration and firmware
                  management (Cisco devices):

3.20.118.133

3.20.228.133

3.23.144.213

3.130.125.44

3.132.162.62

3.140.117.199

18.232.241.58

35.168.211.203

50.16.236.139

52.45.157.48

54.145.130.71

54.156.13.25

52.26.82.54

54.68.1.225

November 14, 2022

Added the IP subnet 170.72.242.0/24 for the Webex Calling service.

September 08, 2022

The Cisco MPP Firmware transitions to use https://binaries.webex.com as the host URL
                  for MPP firmware upgrades in all regions. This change improves firmware upgrade
                  performance.

August 30, 2022

Removed reference to Port 80 from Device configuration and firmware management
                  (Cisco devices), Application configuration and CScan rows in the Port table as
                  there’s no dependency.

August 18, 2022

No change in the solution. Updated the destination ports 5062 (required for
                  Certificate-based trunk), 8934 (required for Registration-based trunk) for Call
                  signaling to Webex Calling (SIP TLS).

July 26, 2022

Added the 54.68.1.225 IP Address, which is required for firmware upgrade of Cisco
                  840/860 devices.

July 21, 2022

Updated the destination ports 5062, 8934 for Call signaling to Webex Calling (SIP
                  TLS).

July 14, 2022

Added the URLs that support a complete function of Webex Aware services.

Added the IP subnet 23.89.154.0/25 for the Webex Calling service.

June 27, 2022

Updated the Domain and URLs for Webex Calling services:

*.broadcloudpbx.com

*.broadcloud.com.au

*.broadcloud.eu

*.broadcloudpbx.net

June 15, 2022

Added the following ports and protocols under IP Addresses and Ports for Webex
                    Calling Services :

Connection purpose: Webex Features

Source addresses: Webex Calling Devices

Source ports: Ephemeral

Protocol: TCP

Destination addresses: Refer to IP Subnets and Domains defined in Webex
                        Meetings/Messaging - Network Requirements.

Destination ports: 443

Updated information in the Webex Meetings/Messaging - Network Requirements section

May 24, 2022

Added the IP subnet 52.26.82.54/24 to 52.26.82.54/32 for Webex Calling
                  service

May 6, 2022

Added the IP subnet 52.26.82.54/24 for Webex Calling service

April 7, 2022

Updated the Local Gateway internal and external UDP port range to
                    8000-48198 †

April 5, 2022

Added the following IP subnets for Webex Calling service:

23.89.40.0/25

23.89.1.128/25

March 29, 2022

Added the following IP subnets for Webex Calling service:

23.89.33.0/24

150.253.209.128/25

September 20, 2021

Added 4 new IP subnets for Webex Calling service:

23.89.76.128/25

170.72.29.0/24

170.72.17.128/25

170.72.0.128/25

April 2, 2021

Added *.ciscospark.com under Domains and URLs for Webex Calling Services to support Webex Calling use cases in the Webex App.

March 25, 2021

Added 6 new IP ranges for activate.cisco.com, which is effective starting May 8,
                  2021.

72.163.15.64/26

72.163.15.128/26

173.36.127.0/26

173.36.127.128/26

192.133.220.0/26

192.133.220.64/26

March 4, 2021

Replaced Webex Calling discrete IPs and smaller IP ranges with simplified ranges
                  in a separate table for ease of understanding for firewall configuration.

February 26, 2021

Added 5004 as destination port for Call media to Webex Calling (STUN, SRTP) to
                  support Interactive Connectivity Establishment (ICE) that will be available in
                  Webex Calling in April 2021.

February 22, 2021

Domains and URLs are now listed within a separate table.

IP Addresses and Ports table are adjusted to group IP addresses for the same
                  services.

Adding the Notes column to the IP Addresses and Ports table that aids in
                  understanding the requirements.

Moving the following IP addresses to simplified ranges for device configuration
                  and firmware management (Cisco devices):

activate.cisco.com

72.163.10.125 -> 72.163.10.96/27

173.37.149.125 -> 173.37.149.96/27

webapps.cisco.com

173.37.146.134 -> 173.37.146.128/25

72.163.10.134 -> 72.163.10.128/25

Adding the following IP addresses for Application Configuration because Cisco
                  Webex client points to a newer DNS SRV in Australia in March 2021.

199.59.64.237

199.59.67.237

January 21, 2021

We’ve added the following IP addresses to device configuration and firmware
                  management (Cisco devices):

3.134.166.179

50.16.236.139

54.145.130.71

72.163.10.125

72.163.24.0/23

173.37.26.0/23

173.37.146.134

We’ve removed the following IP addresses from device configuration and firmware
                  management (Cisco devices):

35.172.26.181

52.86.172.220

52.203.31.41

We’ve added the following IP addresses to the application configuration:

62.109.192.0/19

64.68.96.0/19

207.182.160.0/19

150.253.128.0/17

We’ve removed the following IP addresses from the application configuration:

64.68.99.6

64.68.100.6

We’ve removed the following port numbers from the application configuration:

1081, 2208, 5222, 5280-5281, 52644-52645

We’ve added the following domains to the application configuration:

idbroker-b-us.webex.com

idbroker-eu.webex.com

ty6-wxt-jp.bcld.webex.com

os1-wxt-jp.bcld.webex.com

December 23, 2020

Added new Application Configuration IP addresses to the port reference
                  images.

December 22, 2020

Updated the Application Configuration row in the tables to include the following
                  IP addresses: 135.84.171.154 and 135.84.172.154.

Hid the network diagrams until these IP addresses are added.

December 11, 2020

Updated the Device configuration and firmware management (Cisco devices) and the
                  Application configuration rows for the supported Canadian domains.

October 16, 2020

Updated the call signaling and media entries with the following IP addresses:

139.177.64.0/24

139.177.65.0/24

139.177.66.0/24

139.177.67.0/24

139.177.68.0/24

139.177.69.0/24

139.177.70.0/24

139.177.71.0/24

139.177.72.0/24

139.177.73.0/24

September 23, 2020

Under CScan, replaced 199.59.64.156 with 199.59.64.197.

August 14, 2020

Added more IP addresses to support the introduction of data centers in
                  Canada:

Call signaling to Webex Calling (SIP TLS)—135.84.173.0/25,135.84.174.0/25,
                  199.19.197.0/24, 199.19.199.0/24

August 12, 2020

Added more IP addresses to support the introduction of data centers in
                  Canada:

Call media to Webex Calling (SRTP)—135.84.173.0/25,135.84.174.0/25,
                      199.19.197.0/24, 199.19.199.0/24

Call signaling to publicly addressed endpoints (SIP
                      TLS)—135.84.173.0/25,135.84.174.0/25, 199.19.197.0/24, 199.19.199.0/24.

Device configuration and firmware management (Cisco
                      devices)—135.84.173.155,135.84.174.155

Device time synchronization—135.84.173.152, 135.84.174.152

Application configuration—135.84.173.154,135.84.174.154

July 22, 2020

Added the following IP address to support the introduction of data centers in
                  Canada: 135.84.173.146

June 9, 2020

We made the following changes to the CScan entry:

Corrected one of the IP addresses—changed 199.59.67.156 to 199.59.64.156.

New features require new ports and UDP—19560-19760.

March 11, 2020

We added the following domain and IP addresses to the application
                  configuration:

jp.bcld.webex.com—135.84.169.150

client-jp.bcld.webex.com

idbroker.webex.com—64.68.99.6, 64.68.100.6

We updated the following domains with additional IP addresses to device
                  configuration and firmware management:

cisco.webexcalling.eu—85.119.56.198, 85.119.57.198

webapps.cisco.com—72.163.10.134

activation.webex.com—35.172.26.181, 52.86.172.220

cloudupgrader.webex.com—3.130.87.169, 3.20.185.219

February 27, 2020

We added the following domain and ports to device configuration and firmware
                  management:

cloudupgrader.webex.com—443, 6970

| Product | Proxy Configuration | Authentication Type |
|---|---|---|
| Webex for Mac | Manual, WPAD, PAC | No Auth, Basic, NTLM, † |
| Webex for Windows | Manual, WPAD, PAC, GPO | No Auth, Basic, NTLM, † , Negotiate † |
| Webex for iOS | Manual, WPAD, PAC | No Auth, Basic, Digest, NTLM |
| Webex for Android | Manual, PAC | No Auth, Basic, Digest, NTLM |
| Webex Web App | Supported through OS | No Auth, Basic, Digest, NTLM, Negotiate † |
| Webex Devices | WPAD, PAC, or Manual | No Auth, Basic, Digest |
| Cisco IP Phones | Manual, WPAD, PAC | No Auth, Basic, Digest |
| Webex Video Mesh Node | Manual | No Auth, Basic, Digest, NTLM |

| Product | Supports Custom Trusted CAs for TLS inspection |
|---|---|
| Webex App (Windows, Mac, iOS, Android, Web) | Yes |
| Webex Room Devices | Yes |
| Cisco IP Multiplatform (MPP) Phones | Yes |

| Domain / URL | Description | Webex Apps and devices using these domains / URLs |
|---|---|---|
| Cisco Webex Calling and Webex Aware services |
| *.broadcloudpbx.com | Webex authorization microservices for cross-launch from Control Hub to Calling
                  Admin Portal. | Control Hub |
| *.broadcloud.com.au | Webex Calling services in Australia. | All |
| *.broadcloud.eu | Webex Calling services in Europe. | All |
| *.broadcloudpbx.net | Calling client configuration and management services. | Webex Apps |
| *.webex.com *.cisco.com | Core Webex Calling & Webex Aware services Identity provisioning Identity storage Authentication OAuth services Device onboarding Cloud Connected UC When a phone connects to a network for the first time or after a factory reset
                  with no DHCP options set, it contacts a device activation server for zero touch
                  provisioning. New phones use activate.cisco.com and phones with firmware release
                  earlier than 11.2(1), continue to use webapps.cisco.com for provisioning. Download the device firmware and locale updates from binaries.webex.com . Allow Cisco Multiplatform phones (MPPs) older than 12.0.3 version to access sudirenewal.cisco.com through port 80 to renew Manufacturer Installed
                  Certificate (MIC) and have a Secure Unique Device Identifier (SUDI). For details,
                  see Field notice . If you are not using a proxy server and only using a firewall to filter the URLs,
                  then add CNAME *.cloudfront.net to allow the list. | All |
| *.ucmgmt.cisco.com | Webex Calling services | Control Hub |
| *.wbx2.com and *.ciscospark.com | Used for cloud awareness to reach out to Webex Calling & Webex Aware services
                  during and after onboarding. These services are necessary for Apps and Devices management Apps Application notification mechanism service management | All |
| *.webexapis.com | Webex microservices that manage your Webex App applications and Webex devices. Profile picture service Whiteboarding service Proximity service Presence service Registration service Calendar service Search service | All |
| *.webexcontent.com | Webex Messaging services related to general file storage including: User files Transcoded files Images Screenshots Whiteboard content Client & device logs Profile pictures Branding logos Log files Bulk CSV export files & import files (Control Hub) | Webex Apps Messaging services. File storage using webexcontent.com replaced by clouddrive.com in October
                    2019 |
| *.accompany.com | People insights integration | Webex Apps |
| Additional Webex related services (Third-Party Domains) |
| *.appdynamics.com *.eum-appdynamics.com | Performance tracking, error and crash capture, session metrics. | Webex App, Webex web App |
| *.sipflash.com | Device management services. Firmware upgrades and secure onboarding purposes. | Webex Apps |
| *.walkme.com *.walkmeusercontent.com | Webex user guidance client. Provides onboarding and usage tours for new
                  users. For more information about WalkMe, click here . | Webex Apps |
| *.google.com *.googleapis.com | Notifications to Webex apps on mobile devices (Example: new message, when call is
                  answered) For IP Subnets, refer to these links Google Firebase Cloud Messaging (FCM)
                    service Apple Push Notification Service (APNS) For APNS, Apple lists the IP subnets for this service. | Webex App |
| api.wxc.e911cloud.com wxc.e911cloud.com | 911 (E911) emergency service (RedSky) integration with Webex Calling The phone and Webex client communicate to the RedSky service by using port 443 See the article e911 service integration with Webex
                    Calling for details. | Webex App, Devices |
| *.quovadisglobal.com *.digicert.com *.identrust.com *.godaddy.com | This is used to check the 'Certificate Revocation List' for the security
                  certificates. The Certificate Revocation List ensure that no compromised
                  certificates can be used to intercept secure Webex traffic. that occurs on TCP
                  Port 80. Webex Calling supports both CRL and OCSP stapling to determine certificate
                    revocation status. While OCSP stapling reduces the need for the Webex App to
                    contact CAs; devices may still contact Certificate Authorities directly. This
                    process validates the hardware identity, perform 802.1X network authentication,
                    or download CRLs if a stapled response is unavailable or invalid. | All |

| IP subnets for Webex Calling services * † |
|---|
| (1) Call Signaling, Media, NTP & CScan |
| 23.89.0.0/16 | 62.109.192.0/18 | 85.119.56.0/23 |
| 128.177.14.0/24 | 128.177.36.0/24 | 135.84.168.0/21 |
| 139.177.64.0/21 | 139.177.72.0/23 | 144.196.0.0/16 |
| 150.253.128.0/17 | 163.129.0.0/17 | 170.72.0.0/16 |
| 170.133.128.0/18 | 185.115.196.0/22 | 199.19.196.0/23 |
| 199.19.199.0/24 | 199.59.64.0/21 |  |
| (2) Device configuration and firmware management (Cisco devices) |
| 3.14.211.49 | 3.20.185.219 | 3.130.87.169 |
| 3.134.166.179 | 52.26.82.54 | 62.109.192.0/18 |
| 72.163.10.96/27 | 72.163.15.64/26 | 72.163.15.128/26 |
| 72.163.24.0/23 | 72.163.10.128/25 | 173.37.146.128/25 |
| 173.36.127.0/26 | 173.36.127.128/26 | 173.37.26.0/23 |
| 173.37.149.96/27 | 192.133.220.0/26 | 192.133.220.64/26 |
| (3) Webex App configuration |
| 62.109.192.0/18 | 64.68.96.0/19 | 150.253.128.0/17 |
| 207.182.160.0/19 |  |  |

| Connection purpose | Source addresses | Source ports | Protocol | Destination addresses | Destination ports | Notes |
|---|---|---|---|---|---|---|
| Call signaling to Webex Calling (SIP TLS) | Local Gateway external (NIC) | 8000-65535 | TCP | Refer to IP Subnets for Webex Calling Services (1) . | 5062, 8934 | These IPs/ports are needed for outbound SIP-TLS call signaling from Local
                  Gateways, Devices, and Webex App Applications (Source) to Webex Calling Cloud
                  (Destination). Port 5062 (required for Certificate-based trunk). And port 8934 (required for
                  Registration-based trunk |
| Devices | 5060-5280 | 8934 |
| Room Series | Ephemeral |
| Webex App | Ephemeral (OS dependent) |
| Call signaling from Webex Calling (SIP TLS) to Local Gateway | Webex Calling address range. Refer to IP Subnets for Webex Calling Services (1) | 8934 | TCP | IP or IP ranges chosen by customer for their Local Gateway | Port or port range chosen by customer for their Local Gateway | Applies to certificate-based local gateways. It is required to establish a
                  connection from Webex Calling to a Local Gateway. A Registration-based local gateway works on reusing a connection created from the
                  local gateway. Destination port is customer chosen Configure trunks |
| Call media to Webex Calling (STUN, SRTP/SRTCP, T38, DTLS) | Local Gateway external NIC | 8000-48199 † * | UDP | Refer to IP Subnets for Webex Calling Services (1) . | 5004, 9000, 8500—8699, 19560—65535 (SRTP over UDP) | These IPs/ports are used for outbound SRTP call media from Local Gateways,
                      Devices, and Webex App Applications (Source) to Webex Calling Cloud
                      (Destination). For Calls within the organization where STUN, ICE negotiation is successful,
                      the media relay in the cloud is removed as the communication path. In such
                      cases the media flow is directly between the user's Apps/devices. For Example: If media optimization is successful, Webex App sends media
                      directly between one another on port ranges 8500–8699 and devices send media
                      directly to one another on ports ranges 19560–19661. For certain network topologies where firewalls are used within a customer
                      premise, allow access for the mentioned source and destination port ranges
                      inside your network for the media to flow through. Example: For Webex App, allow the source and destination port range Audio: 8500-8599 Video:8600-8699 Browsers use the ephemeral source port that can be controlled by setting the
                        WebRtcUdpPortRangepolicy in the Managed Device Management (MDM)
                      profile. The Webex Calling service behaves normally if no MDM Service is set or if
                      SiteURL and EnableForceLogin aren't configured. |
| Devices † * | 19560-19661 |
| Room Series † * | Audio 52050-52099 Video 52200-52299 |
| VG400 ATA Devices | 19560-19849 |
| Webex App † * | Audio: 8500-8599 Video: 8600-8699 |
| WebRTC | Ephemeral (According to the browser policy) |
| Call media from Webex Calling (SRTP/SRTCP, T38) | Webex Calling address range. Refer to IP Subnets for Webex Calling Services (1) | 19560-65535 (SRTP over UDP) | UDP | IP or IP range chosen by customer for their Local Gateway | Media port range chosen by customer for their Local Gateway | Applies to certificate-based local gateways |
| Call signaling to PSTN gateway (SIP TLS) | Local Gateway internal NIC | 8000-65535 | TCP | Your ITSP PSTN GW or Unified CM | Depends on PSTN option (for example, typically 5060 or 5061 for Unified
                CM) |  |
| Call media to PSTN gateway (SRTP/SRTCP) | Local Gateway internal NIC | 8000-48199 † * | UDP | Your ITSP PSTN GW or Unified CM | Depends on the PSTN option (for example, typically 5060 or 5061 for Unified
                CM) |  |
| Device configuration and firmware management (Cisco devices) | Webex Calling devices | Ephemeral | TCP | Refer to IP Subnets for Webex Calling Services (2) | 443, 6970, 80 | Required for the following reasons: Migrating from Enterprise phones (Cisco Unified CM) to Webex Calling. See upgrade.cisco.com for more information. The
                        cloudupgrader.webex.comuses ports: 6970,443 for the firmware
                      migration process. Firmware upgrades and secure onboarding of devices (MPP and Room or Desk phones)
                  using the 16-digit activation code (GDS) For CDA / EDOS - MAC address-based provisioning. Used by devices (MPP phones,
                  ATAs, and SPA ATAs) with newer firmware. For Cisco ATAs, ensure that the devices are on the minimum firmware of
                  11.1.0MSR3-9. When a phone connects to a network for the first time or after a factory reset,
                  without the DHCP options set, it contacts a device activation server for zero
                  touch provisioning. New phones  use activate.cisco.com instead of webapps.cisco.com for provisioning. Phones with firmware released
                  earlier than 11.2(1) continue to use webapps.cisco.com . It’s recommended to
                  allow all these IP subnets. Allow Cisco Multiplatform phones (MPPs) older than 12.0.3 version to access sudirenewal.cisco.com through port 80 for renewing the Manufacturer
                  Installed Certificate (MIC) and having a Secure Unique Device Identifier (SUDI).
                  For details, see Field Notice |
| Webex App configuration | Webex App applications | Ephemeral | TCP | Refer to IP Subnets for Webex Calling Services (3) | 443, 8443 | Used for Id broker Authentication, Webex App configuration services for
                clients, Browser based web access for self-care AND Administrative interface
                  access. The TCP port 8443 is used by Webex App on Cisco Unified CM setup for
                  downloading configuration. Only customers who use the setup to connect to Webex
                  Calling must open the port. |
| Device time synchronization (NTP) | Webex Calling devices | Ephemeral | UDP | Refer to IP Subnets for Webex Calling Services (1) . | 123 † * | These IP addresses are needed for Time Synchronization for Devices (MPP phones,
                ATAs, and SPA ATAs) |
| Domain Name System (DNS) resolution | Webex Calling devices, Webex App, and Webex Devices | Ephemeral | UDP and TCP | Host-defined | 53 † * | Used for DNS lookups to discover the IP addresses of Webex Calling services in
                the cloud. Even though typical DNS lookups are done over UDP, some may require TCP,
                if the query responses can’t fit it in UDP packets. |
| Network Time Protocol (NTP) | Webex App and Webex Devices | 123 | UDP | Host-defined | 123 | Time Synchronization |
| CScan | Web based Network readiness Pre-qualification tool for Webex
                Calling | Ephemeral | TCP | Refer to IP Subnets for Webex Calling Services (1) . | 8934 and 443 | Web based Network readiness Prequalification tool for Webex
                Calling. Go to cscan.webex.com for more information. |
| UDP | 19569-19760 |
| Additional Webex Calling & Webex Aware Services (Third-Party) |
| Push notifications APNS and FCM services | Webex Calling Applications | Ephemeral | TCP | Refer to IP Subnets mentioned under the links Apple Push Notification Service(APNS) Google-Firebase Cloud Messaging (FCM) | 443, 2197, 5228, 5229, 5230, 5223 | Notifications to Webex Apps on mobile devices (Example: When you receive a new
                message or when a call is answered) |

| Source Addresses | Traffic type | Destination addresses | Source ports | Destination ports | DSCP class and value |
|---|---|---|---|---|---|
| Webex App | Audio | Refer IP subnets, Domains, and URLs for Webex Calling services | 8500-8599 | 8500-8599, 19560-65535 | Expedited Forwarding (46) |
| Webex App | Video | 8600-8699 | 8600-8699, 19560-65535 | Assured Forwarding 41 (34) |
| Webex App | Signaling | Ephemeral (OS dependent) | 8934 | CS0 (0) |
| Webex Devices (MPPs and Room) | Audio & Video | 19560-19661 | 19560-65535 | Expedited Forwarding (46) & Assured Forwarding 41 (34) |
| Webex Devices | Signaling | 5060-5280 | 8934 | Class Selector 3 (24) |

| Date | We've made the following changes to this article |
|---|---|
| September 07, 2026 | Expanded the phone’s source port range from 5060-5080 to 5060-5280 to accommodate
                  the updated Cisco feature, enabling support for up to 130 lines. |
| August 13, 2026 | Updated the procedure to validate the NAT pool size required for App or
                  Devices. |
| March 28, 2026 | Updated the link to the Firebase Cloud Messaging (FCM) documentation. |
| March 4, 2026 | Changed the source port for Device time synchronization (NTP) from 51494 to
                  Ephemeral under the IP Subnets for Webex Calling Services section. |
| February 23, 2026 | The purpose of connection details is updated within the IP subnet for Webex
                  Calling The following additional third-party URLs are included: *.quovadisglobal.com, *.digicert.com, *.identrust.com and *.godaddy.com as
                      Webex App requests CRL list from the certificate authorities. Referenced api.wxc.e911cloud.com, wxc.e911cloud.com (E911) emergency service
                      (RedSky) integration with Webex Calling. Editorial updates to enhance the article for better readability |
| December 05, 2025 | Added the usage of the IP subnets, ports, and protocols that are listed under the IP Subnets for Webex Calling Services section. |
| October 24, 2025 | Improved the image quality and fixed the broken link to Google Firebase Cloud
                  Messaging (FCM) service |
| September 15, 2025 | Added IP address 3.14.211.49 to the list of IP subnets used for Cisco device
                      configuration and firmware management. This address is required for manual MPP
                      migrations using the alternate TFTP method. Updated the Signaling & Media source port range for Room Series
                      devices. Removed the dependency on Control Hub from the list of Domains & URLs for
                      Webex Calling services under “Additional Webex related services (Third-Party
                      Domains).” Made overall design tweaks |
| April 10, 2025 | Included text to emphasize the MTU size for Webex Calling and Webex Aware
                  services |
| March 27, 2025 | Updated the IP Subnet for Webex Calling services 62.109.192.0/18 to accommodate
                  Webex Calling market expansion for the Saudi Arabia region. |
| January 21, 2025 | Added details for using the SIP Application Layer Gateway. |
| January 8, 2025 | Moved the IP subnet address related to Device configuration and Webex App
                  configuration to the IP Subnets for Webex Calling services section |
| December 17, 2024 | Added support to WebRTC for the Webex Calling Media specification. |
| November 14, 2024 | Updated the supported port range for Webex Calling call media for VG400 series
                  ATA device |
| November 11, 2024 | Added the supported port range for Webex Calling call media for VG400 series ATA
                  device |
| July 25, 2024 | Added back the 52.26.82.54 IP subnet as it’s required for the Cisco ATA device
                  configuration and firmware management. |
| July 18, 2024 | Updated with the following details: QoS (TOS/DSCP) values supported for Webex Calling (Apps, Devices) Updated the Network diagram Including the link for network requirements related to Webex Attendant
                      Console. |
| June 28, 2024 | Updated the usage of both SRTP/ SRTCP port ranges for the Webex Calling Media
                  specification. |
| June 11, 2024 | Removed the "huron-dev.com" domain as it’s not used. |
| May 06, 2024 | Updated the usage of both SRTP/ SRTCP port ranges for the Webex Calling Media
                  specification. |
| April 03, 2024 | Updated the IP Subnets for Webex Calling services with 163.129.0.0/17 to
                accommodate Webex Calling market expansion for the India region. |
| December 18, 2023 | Included the sudirenewal.cisco.com URL and port 80 requirement for
                  device configuration and firmware management of the Cisco MPP phone's MIC renewal. |
| December 11, 2023 | Updated the IP Subnets for Webex Calling services to include a larger set of IP
                  addresses. 150.253.209.128/25 – changed to 150.253.128.0/17 |
| November 29, 2023 | Updated the IP Subnets for Webex Calling services to include a larger set of IP
                  addresses to accommodate Webex Calling region expansion for future growth. 144.196.33.0/25 – changed to 144.196.0.0/16 The IP Subnets for Webex Calling services sections under Webex Calling (SIP TLS)
                  and Call media to Webex Calling (STUN, SRTP) is updated for clarity on
                  certificate-based trunking and the firewall requirements for Local Gateway. |
| August 14, 2023 | We’ve added the following IP addresses 144.196.33.0/25 and 150.253.156.128/25 to
                  support increased capacity requirements for Edge and Webex Calling Services. This IP range is supported only in the U.S. region. |
| July 5, 2023 | Added the link https://binaries.webex.com to install the Cisco MPP
                  Firmware. |
| March 7, 2023 | We've overhauled the entire article to include: Included options for Proxy support. Modified Calling flow diagram Simplified Domains/URLs/IP subnet portions for Webex Calling and Webex Aware
                      services Added 170.72.0.0/16 IP subnet range for Webex Calling & Webex Aware
                      services. Removed the following ranges 170.72.231.0, 170.72.231.10, 170.72.231.161 and
                      170.72.242.0/24 |
| March 5, 2023 | Updating the article to include the following: Added the UDP-SRTP port range (8500-8700) used by applications. Added the ports for the Push notifications APNS and FCM services. Split the CScan port range for UDP & TCP. Added the references section. |
| November 15, 2022 | We’ve added the following IP addresses for device configuration and firmware
                  management (Cisco devices): 170.72.231.0 170.72.231.10 170.72.231.161 We’ve removed the following IP addresses from device configuration and firmware
                  management (Cisco devices): 3.20.118.133 3.20.228.133 3.23.144.213 3.130.125.44 3.132.162.62 3.140.117.199 18.232.241.58 35.168.211.203 50.16.236.139 52.45.157.48 54.145.130.71 54.156.13.25 52.26.82.54 54.68.1.225 |
| November 14, 2022 | Added the IP subnet 170.72.242.0/24 for the Webex Calling service. |
| September 08, 2022 | The Cisco MPP Firmware transitions to use https://binaries.webex.com as the host URL
                  for MPP firmware upgrades in all regions. This change improves firmware upgrade
                  performance. |
| August 30, 2022 | Removed reference to Port 80 from Device configuration and firmware management
                  (Cisco devices), Application configuration and CScan rows in the Port table as
                  there’s no dependency. |
| August 18, 2022 | No change in the solution. Updated the destination ports 5062 (required for
                  Certificate-based trunk), 8934 (required for Registration-based trunk) for Call
                  signaling to Webex Calling (SIP TLS). |
| July 26, 2022 | Added the 54.68.1.225 IP Address, which is required for firmware upgrade of Cisco
                  840/860 devices. |
| July 21, 2022 | Updated the destination ports 5062, 8934 for Call signaling to Webex Calling (SIP
                  TLS). |
| July 14, 2022 | Added the URLs that support a complete function of Webex Aware services. Added the IP subnet 23.89.154.0/25 for the Webex Calling service. |
| June 27, 2022 | Updated the Domain and URLs for Webex Calling services: *.broadcloudpbx.com *.broadcloud.com.au *.broadcloud.eu *.broadcloudpbx.net |
| June 15, 2022 | Added the following ports and protocols under IP Addresses and Ports for Webex
                    Calling Services : Connection purpose: Webex Features Source addresses: Webex Calling Devices Source ports: Ephemeral Protocol: TCP Destination addresses: Refer to IP Subnets and Domains defined in Webex
                        Meetings/Messaging - Network Requirements. Destination ports: 443 Notes: The Webex Calling Devices use these IP
                    addresses and domains to interface with Webex Cloud Services such as Directory,
                    Call History, and Meetings. Updated information in the Webex Meetings/Messaging - Network Requirements section |
| May 24, 2022 | Added the IP subnet 52.26.82.54/24 to 52.26.82.54/32 for Webex Calling
                  service |
| May 6, 2022 | Added the IP subnet 52.26.82.54/24 for Webex Calling service |
| April 7, 2022 | Updated the Local Gateway internal and external UDP port range to
                    8000-48198 † |
| April 5, 2022 | Added the following IP subnets for Webex Calling service: 23.89.40.0/25 23.89.1.128/25 |
| March 29, 2022 | Added the following IP subnets for Webex Calling service: 23.89.33.0/24 150.253.209.128/25 |
| September 20, 2021 | Added 4 new IP subnets for Webex Calling service: 23.89.76.128/25 170.72.29.0/24 170.72.17.128/25 170.72.0.128/25 |
| April 2, 2021 | Added *.ciscospark.com under Domains and URLs for Webex Calling Services to support Webex Calling use cases in the Webex App. |
| March 25, 2021 | Added 6 new IP ranges for activate.cisco.com, which is effective starting May 8,
                  2021. 72.163.15.64/26 72.163.15.128/26 173.36.127.0/26 173.36.127.128/26 192.133.220.0/26 192.133.220.64/26 |
| March 4, 2021 | Replaced Webex Calling discrete IPs and smaller IP ranges with simplified ranges
                  in a separate table for ease of understanding for firewall configuration. |
| February 26, 2021 | Added 5004 as destination port for Call media to Webex Calling (STUN, SRTP) to
                  support Interactive Connectivity Establishment (ICE) that will be available in
                  Webex Calling in April 2021. |
| February 22, 2021 | Domains and URLs are now listed within a separate table. IP Addresses and Ports table are adjusted to group IP addresses for the same
                  services. Adding the Notes column to the IP Addresses and Ports table that aids in
                  understanding the requirements. Moving the following IP addresses to simplified ranges for device configuration
                  and firmware management (Cisco devices): activate.cisco.com 72.163.10.125 -> 72.163.10.96/27 173.37.149.125 -> 173.37.149.96/27 webapps.cisco.com 173.37.146.134 -> 173.37.146.128/25 72.163.10.134 -> 72.163.10.128/25 Adding the following IP addresses for Application Configuration because Cisco
                  Webex client points to a newer DNS SRV in Australia in March 2021. 199.59.64.237 199.59.67.237 |
| January 21, 2021 | We’ve added the following IP addresses to device configuration and firmware
                  management (Cisco devices): 3.134.166.179 50.16.236.139 54.145.130.71 72.163.10.125 72.163.24.0/23 173.37.26.0/23 173.37.146.134 We’ve removed the following IP addresses from device configuration and firmware
                  management (Cisco devices): 35.172.26.181 52.86.172.220 52.203.31.41 We’ve added the following IP addresses to the application configuration: 62.109.192.0/19 64.68.96.0/19 207.182.160.0/19 150.253.128.0/17 We’ve removed the following IP addresses from the application configuration: 64.68.99.6 64.68.100.6 We’ve removed the following port numbers from the application configuration: 1081, 2208, 5222, 5280-5281, 52644-52645 We’ve added the following domains to the application configuration: idbroker-b-us.webex.com idbroker-eu.webex.com ty6-wxt-jp.bcld.webex.com os1-wxt-jp.bcld.webex.com |
| December 23, 2020 | Added new Application Configuration IP addresses to the port reference
                  images. |
| December 22, 2020 | Updated the Application Configuration row in the tables to include the following
                  IP addresses: 135.84.171.154 and 135.84.172.154. Hid the network diagrams until these IP addresses are added. |
| December 11, 2020 | Updated the Device configuration and firmware management (Cisco devices) and the
                  Application configuration rows for the supported Canadian domains. |
| October 16, 2020 | Updated the call signaling and media entries with the following IP addresses: 139.177.64.0/24 139.177.65.0/24 139.177.66.0/24 139.177.67.0/24 139.177.68.0/24 139.177.69.0/24 139.177.70.0/24 139.177.71.0/24 139.177.72.0/24 139.177.73.0/24 |
| September 23, 2020 | Under CScan, replaced 199.59.64.156 with 199.59.64.197. |
| August 14, 2020 | Added more IP addresses to support the introduction of data centers in
                  Canada: Call signaling to Webex Calling (SIP TLS)—135.84.173.0/25,135.84.174.0/25,
                  199.19.197.0/24, 199.19.199.0/24 |
| August 12, 2020 | Added more IP addresses to support the introduction of data centers in
                  Canada: Call media to Webex Calling (SRTP)—135.84.173.0/25,135.84.174.0/25,
                      199.19.197.0/24, 199.19.199.0/24 Call signaling to publicly addressed endpoints (SIP
                      TLS)—135.84.173.0/25,135.84.174.0/25, 199.19.197.0/24, 199.19.199.0/24. Device configuration and firmware management (Cisco
                      devices)—135.84.173.155,135.84.174.155 Device time synchronization—135.84.173.152, 135.84.174.152 Application configuration—135.84.173.154,135.84.174.154 |
| July 22, 2020 | Added the following IP address to support the introduction of data centers in
                  Canada: 135.84.173.146 |
| June 9, 2020 | We made the following changes to the CScan entry: Corrected one of the IP addresses—changed 199.59.67.156 to 199.59.64.156. New features require new ports and UDP—19560-19760. |
| March 11, 2020 | We added the following domain and IP addresses to the application
                  configuration: jp.bcld.webex.com—135.84.169.150 client-jp.bcld.webex.com idbroker.webex.com—64.68.99.6, 64.68.100.6 We updated the following domains with additional IP addresses to device
                  configuration and firmware management: cisco.webexcalling.eu—85.119.56.198, 85.119.57.198 webapps.cisco.com—72.163.10.134 activation.webex.com—35.172.26.181, 52.86.172.220 cloudupgrader.webex.com—3.130.87.169, 3.20.185.219 |
| February 27, 2020 | We added the following domain and ports to device configuration and firmware
                  management: cloudupgrader.webex.com—443, 6970 |

## Figuras

![Deployment diagram of Cisco Webex Calling services, illustrating the network architecture, communication flows, and port requirements for cloud components.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/442001-443000/442926.jpg)