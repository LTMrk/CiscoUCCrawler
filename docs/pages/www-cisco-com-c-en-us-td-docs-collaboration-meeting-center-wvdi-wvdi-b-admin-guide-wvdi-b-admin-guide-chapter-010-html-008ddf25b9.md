---
doc_id: www-cisco-com-c-en-us-td-docs-collaboration-meeting-center-wvdi-wvdi-b-admin-guide-wvdi-b-admin-guide-chapter-010-html-008ddf25b9
source_url: https://www.cisco.com/c/en/us/td/docs/collaboration/meeting_center/wvdi/wvdi-b-admin-guide/wvdi-b-admin-guide_chapter_010.html
retrieved_at: 2026-09-01T20:32:22.608282+00:00
---

Administration Guide for the Cisco Webex Meetings Virtual Desktop Environments

# Administration Guide for the Cisco Webex Meetings Virtual Desktop Environments

Updated: September 25, 2019

Chapter: Installing and Configuring the Webex Meetings Virtual Desktop App 39.3

## Chapter: Installing and Configuring the Webex Meetings Virtual Desktop App 39.3

# Installing and Configuring the Webex Meetings Virtual Desktop App 39.3

## About the Cisco Webex Meetings Virtual Desktop App

The Cisco Webex Meetings Virtual Desktop App optimizes the audio and video for the virtual desktop environment using a thin
                              client. With supported versions of Cisco Webex for Windows, Linux, Unicon eLux, and HP ThinPro, hosts can connect to meetings
                              and manage the lobby from their hosted virtual desktops (HVD), ensuring a great experience for both the hosts and the attendees.
                              The software routes all audio and video streams directly between the thin client and the meeting server without going through
                              the HVD.

Hosts can start meetings from the Webex Meetings Virtual Desktop App if their site is managed in the Cisco Webex Control Hub, or if their site is managed in the Webex Site Administration and
                                          linked to Control Hub. For more information, see Link Cisco Webex Sites to Control Hub .

The Webex Meetings Virtual Desktop Environments is not compatible with the current WBS40.4 Webex Meetings Virtual Desktop
                                          Software.

## The Architecture of the Cisco Webex Meetings Virtual Desktop App

The Webex Meetings Virtual Desktop App provides the same architecture components similar to a video device.

## Requirements

Before you deploy the Webex Meetings Virtual Desktop App version WBS39.3, make sure to meet that the following requirements:

Authenticate the user on the Webex Meetings Virtual Desktop App

User to have an account on the Webex site that is managed by Webex Control Hub, or linked with Webex Control Hub

Cisco Unified Communications Manager (CUCM) and Cisco Expressway meets the minimum version requirements

CUCM version:

10.5(2) and later (Minimum)

11.5(1) SU3 or later (Recommended)

Cisco Expressway C and E version X8.11.4 and later

Component

Requirements

Microsoft Windows-based thin client hardware

Installed RAM 2 GB

Free Physical Memory 128 MB

Free Disk Space 256 MB

CPU Mobile AMD Sempron Processor 3600+, 2-GHz Intel Core 2 CPU, or T7400 2.16 GHz

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

Microsoft Windows-based thin client OS

Microsoft Windows 7

Microsoft Windows 8

Microsoft Windows 8.1

Microsoft Windows 10

Windows Embedded Standard-based thin client hardware

Installed RAM 2 GB

Free Physical Memory 128 MB

Free Disk Space 256 MB

CPU performance affects the maximum video resolution. With Windows Embedded Standard thin clients, the expected resolution
                                                depends on the CPU:

Up to 720p with quad-core AMD GX-420CA SOC 2 GHz or similar

Up to 240p with dual-core AMD G-T56N 1.65 GHz or similar

Audio-only support with dual-core VIA Eden X2 U4200 1 GHz or similar CPU

These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution.

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

The Webex Meetings Virtual Desktop App for Windows does not require the Microsoft .NET Framework or any Java modules.

Hosted virtual desktop OS (server-side)

Microsoft Windows 7

Microsoft Windows 8

Microsoft Windows 8.1

Microsoft Windows 10

Windows Embedded Standard-based thin client OS

Windows Embedded Standard 7

Windows Embedded Standard 8

Windows 10 IoT Enterprise

Connection broker for the hosted virtual desktop

Citrix XenDesktop 7.15, and later 7.x versions

VMware Horizon 7.0 and later 7.x versions

To avoid phone connection issues, perform the following steps:

On thin clients with 64-bit Windows, select 32-bit Core Remote Experience.

On the VMware Horizon installation on the 64-bit machine install the Webex Meetings Virtual Desktop App .

Windows Server

Microsoft Windows 2012 R2

Microsoft Windows 2016

Windows Embedded

Microsoft WES 7

Microsoft WES 8

Microsoft Windows IoT

Cisco Unified Communications Manager

Recommended CUCM Release 11.5(1) SU3 or later

Minimum CUCM Release 10.5(2)

Accessories

For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories .

Cisco Webex Meetings Virtual Desktop App does not support using accessories to start or end a meeting, or mute or unmute a meeting.

If the host uses the end meeting button to end a meeting, the meeting will end directly, without assigning a new host

Component

Requirements

The following hardware is supported with Ubuntu 14.04 32-bit LTS:

Installed RAM 2 GB

Free Physical Memory 256 MB

Free Disk Space 256 MB

CPU: AMD G-T56N 1.65Ghz, or Intel Core 2 Duo T7500 2.2 GHz

USB 2.0 for USB camera and audio devices

Ubuntu—Hardware

Ubuntu 14.04 32-bit LTS

Hosted virtual desktop OS (server-side)

Microsoft Windows 7

Microsoft Windows 10

Microsoft Windows Server 2016

Connection broker for the hosted virtual desktop

Citrix XenDesktop 7.15, and later 7.x versions

VMware Horizon 7.5 and later 7.x versions

13.8.0 or later (32-bit version required)

VMware 4.4.0 or later (32-bit version required)

Cisco Unified Communications Manager

Recommended CUCM Release 11.5(1) SU3 or later

Minimum CUCM Release 10.5(2)

Accessories

For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories .

Cisco Webex Meetings Virtual Desktop App does not support using accessories to start or end a meeting, or mute or unmute a meeting.

If the host uses the end meeting button to end a meeting, the meeting will end directly, without assigning a new host

The Citrix Receiver or VMware Horizon Client provides a user interface for the corresponding connection broker.

(PCoIP and Blaster)

Component

Requirements

Unicon eLux thin clients—Hardware

The minimum hardware requirements for thin clients are:

1.6-GHz dual-core processor

2-GB RAM

The following client hardware is tested with eLux RP 5.7.0:

HP T520

HP T620 Dual Core/Quad Core

HP T630 Dual Core/Quad Core

HP T730

Hosted virtual desktop OS (server-side)

Microsoft Windows 7

Microsoft Windows 10

Microsoft Windows Server 2016

Connection broker for the hosted virtual desktop

Citrix XenDesktop 7.15, and later 7.x versions

VMware Horizon 7.5 and later 7.x versions

Citrix Receiver or VMware Horizon Client

(Installed on the thin client)

13.8.0 or later (32-bit version required)

VMware 4.4.0 or later (32-bit version required)

Cisco Unified Communications Manager

Recommended CUCM Release 11.5(1) SU3 or later

Minimum CUCM Release 10.5(2)

Accessories

For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories .

Cisco Webex Meetings Virtual Desktop App does not support using accessories to start or end a meeting, or mute or unmute a meeting.

If the host uses the end meeting button to end a meeting, the meeting will end directly, without assigning a new host

The Citrix Receiver or VMware Horizon Client provides a user interface for the corresponding connection broker.

(PCoIP and Blaster)

Component

Requirements

HP ThinPro 6.2 - Hardware

The minimum hardware requirements for thin clients are:

1.6-GHz dual-core processor

2-GB RAM

Supported devices, thin client with HP ThinPro 6.2

HP T520

HP T620 Dual Core/Quad Core

HP T630 Dual Core/Quad Core

HP T730

HP ThinPro platform image

HP ThinPro 6.2: T7X62022

Hosted virtual desktop OS (server-side)

Microsoft Windows 7

Microsoft Windows 10

Microsoft Windows Server 2016

Connection broker for the hosted virtual desktop

Citrix XenDesktop 7.15, and later 7.x versions

VMware Horizon 7.5 and later 7.x versions

For HP ThinPro 6.2

The HP ThinPro image includes Citrix and VMware:

ICA Client: 13.8.0 or later (32-bit version required)

VMware 4.4.0 or later (32-bit version required)

Cisco Unified Communications Manager

Recommended CUCM Release 11.5(1) SU3 or later

Minimum CUCM Release 10.5(2)

Accessories

For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories .

Cisco Webex Meetings Virtual Desktop App does not support using accessories to start or end a meeting, or mute or unmute a meeting.

If the host uses the end meeting button to end a meeting, the meeting will end directly, without assigning a new host

The Citrix Receiver or VMware Horizon Client provides a user interface for the corresponding connection broker.

(PCoIP and Blaster)

## Port Requirements

### Port Requirements

The client uses the ports and protocols listed in the following table. If you plan to deploy a firewall between the client
                                 and a server, configure the firewall to allow these ports and protocols.

### Ports and Protocols

The following table lists the ports and protocols that the client uses. If you plan to deploy a firewall between the client
                                 and a server, configure the firewall to allow these ports and protocols.

Port

Application Layer Protocol

Transport Layer Protocol

Description

Configuration

6970

HTTP

TCP

Connect to the TFTP server to download client configuration files.

6972

HTTPS

TCP

Connects to the TFTP server to download the client configuration files securely for Cisco Unified Communications Manager release
                                             11.0 and later.

53

DNS

UDP

Hostname resolution.

3804

CAPF

TCP

Issues Locally Significant Certificates (LSC) to IP phones. This port is the listening port for Cisco Unified Communications
                                             Manager Certificate Authority Proxy Function (CAPF) enrollment.

8443

HTTPS

Traffic to Cisco Unified Communications Manager.

Communication Manager Signaling

2748

CTI

TCP

Computer Telephony Interface (CTI) used for the desk phone control.

5060

SIP

TCP

Provides Session Initiation Protocol (SIP) call signaling.

5061

SIP over TLS

TCP

SIP over TCP Provides secure SIP call signaling. (Used if Secure SIP is enabled for the device.)

5070 to 6070

BFCP

UDP

Binary Floor Control Protocol (BFCP) for video screen sharing capabilities.

Voice or Video Media Exchange

16384 to 32766

RTP/SRTP

UDP

Cisco Unified Communications Manager media port range used for audio, video, and BFCP video desktop share.

Cisco Webex Meetings Virtual Desktop App

443

HTTPS

TCP

Connects to Cisco Webex Meetings for meetings.

#### Open Port Requirements

Install the Webex Meetings Virtual Desktop App client on thin client. Then, open the ports list in the Configuration, Communication
                                 Manager Signaling, and Voice or Video Media Exchange.

Install the Webex Meetings Virtual Desktop Application and agent on HVD. Then, open the ports list in Configuration and Webex
                                 Meetings Virtual Desktop App.

Direction

Transport Protocol

Destination Port

Purpose

External Network => UAG

TCP/UDP

443

Blast Extreme

4172

PCoIP

8443

HTML Blast

Internal Network (Administration) => UAG

TCP

9443

REST API

TCP

80/443

Edge Gateway

UAG => Internal Network (VDI)

TCP

443

Connection Server

TCP/UDP

4172

PCoIP

TCP

32111

USB Redirection

TCP/UDP

22443

Blast Extreme

TCP

9427

MMR/CDR

TCP/UDP

53

DNS Query

External Network => NetScaler

TCP

80

Connection from Citrix Receiver

TCP/UDP

443

Internal Network => NetScaler

TCP

80

Connection from Citrix Receiver

TCP/UDP

443

Authentication callback from StoreFront Server / Connection from Citrix Receiver

TCP

22

NetScaler Administration

80

443

3010

3008

NetScaler => Internal Network (VDI)

TCP/UDP

53

DNS Query

UDP

123

NTP

TCP

389

LDAP Query

636

TCP

443

Citrix StoreFront Server

80

808

TCP

80

Citrix Delivery Controller

443

TCP/UDP

1494

HDX ICA

2598

UDP

16500-16509

3224-3324

### Supported Codecs

Audio Codec

Video Codec

G.722

H.264/AVC

G.722.1 (24 and 32k)

G.722.1 is supported on Cisco Unified Communications Manager 8.6.1 or later.

G.711 A-law

G.711 u-law

G.729a

Opus

Opus is supported on Cisco Unified Communications Manager 11.0 or later.

## Cisco Expressway

The Cisco Expressway solution comprises of Core (Expressway-C) and Edge (Expressway-E). Expressway C and E allow remote video
                              and mobile clients to communicate with a private communications platform without a virtual private network.

Deploy the Expressway C and E using CUCM to communicate with Webex, regardless of the endpoints being registered to CUCM.
                              To know more about configuring Cisco Expressway, see Mobile and Remote Access Through Cisco Expressway .

## Enabling Cisco Unified Communications Manager (CUCM)

Download the COP file from Cisco.com for:

Windows

Unicon eLux

ThinPro and Ubuntu

Enter details for the Software Location and click Next .

Enter the COP file name in Options/Upgrade .

Select the Server and click Go in the Control Center. Then, restart the services: Cisco Unified CM, Cisco CTI Manager, and Cisco TFTP.

Add a new WSF device for the user with device mode Cisco Webex VDI SVC Framework .

The steps to add the WSF device are the same as the steps to add a CSF device.

Select the checkbox Allow Control of Device from CTI for this device.

Add CTI permission on the end user page

## Authenticating Users to Connect to CUCM

Both the meeting site and CUCM’s credentials are encrypted and then cached to a local storage. At every restart, the Webex Meetings Virtual Desktop App always tries the cached credential first. Then, prompts you to do the authentication again if the cached credential becomes
                              invalid.

Any configurations or credentials are cached in HVD only and not in the thin client.

Deployment

User Experience

Both the meeting site and CUCM are SSO-enabled

Enter the email to start the service discovery.

Enter the username and password in the browser.

The pre-meeting UI displays.

The meeting site is SSO-enabled but CUCM is not SSO-enabled

Enter the email to start service discovery.

Enter the username and password in the browser.

The pre-meeting UI displays.

Enter the CUCM credentials in the pop-up window.

The meeting site is not SSO-enabled but CUCM can either be SSO-enabled or not SSO-enabled

Enter the email to start the service discovery.

Enter the username and password for meeting account credentials.

The pre-meeting UI displays.

Enter CUCM credentials if it is different with meeting credentials.

## Workflow for Deployment and Installation of the Cisco Webex Meetings Virtual Desktop App

Prerequisites:

Ensure that you install CUCM and it is operational.

If CUCM is not installed, see Installation Guide for Cisco Unified Communications Manager for installation instructions.

Review the Webex Meetings Virtual Desktop App Release Notes for information about limitations or restrictions that may affect your deployment.

Review the system requirements to confirm that all required hardware and software meet them.

Failure to meet all requirements can result in a non-functional deployment.

Review the port requirements.

Configure SRV Records on the DNS server. If the administrator does not configure the SRV records on DNS, then install Webex
                                    meetings at the command line to setup arguments. For more information, see Deploying the SRV Records on the DNS Server .

Configure CUCM (Install the COP file, restart the services: Cisco Unified CM, Cisco CTI Manager, Cisco TFTP, add users, and
                                    WSF devices). For more information on Configuring CUCM, see Enabling Cisco Unified Communications Manager (CUCM) .

Create a dedicated directory number for WSF Device.

Create and set up the hosted virtual desktops in the data center. Ensure that the hosted virtual desktops (HVD) are ready
                                    for you to install the Webex Meetings Virtual Desktop App . For more information, see Setting up the Hosted Virtual Desktops Workflow .

Set up and configure the thin clients. For more information, see documentation available from the thin client OEM.

Install the Webex Meetings Virtual Desktop App Client components on the thin clients and the hosted virtual desktop. For more information, see Installing the Components Workflow . After you install the Webex Meetings Virtual Desktop App Agent and other required software on the HVD, you can clone the HVD.

## Setting up the Hosted Virtual Desktops Workflow

Sign in to the Microsoft Windows HVD as a new user, with administration rights.

Join the HVD to the corporate domain.

You require domain administration rights.

Set up Citrix or VMware access to the HVDs.

Install the Webex Meetings Virtual Desktop App on the HVD.

The Webex Meetings Virtual Desktop App supports the English Operating System in the current release. If you are using an Operating System other than English, install
                                                the Webex Meetings Desktop App using command line:

Install the Webex Meetings Virtual Desktop App Agent on the HVD.

Clone the HVD image.

For more information on the best practices for cloning Microsoft Windows HVD images, see the documentation for your Citrix
                                                or VMware product.

## Installing the Components Workflow

Download the Webex Meetings Virtual Desktop App .

Download the Webex Meetings Virtual Desktop App Agent and Client.

Install the Webex Meetings Virtual Desktop App client for HVD on thin client.

When installing the Webex Meetings Virtual Desktop client on thin client, disconnect the connection with HVD.

Install the Webex Meetings Virtual Desktop App on HVD.

The Webex Meetings Virtual Desktop App supports the English Operating System in the current release. If you are using an Operating System other than English, install
                                                the Webex Meetings Virtual Desktop App using command line:

Install the Webex Meetings Virtual Desktop App Agent on the HVD.

## Deploying the SRV Records on the DNS Server

The client queries name servers for records in the services domain.

Deploy SRV records in each DNS zone for those service domains if your organization has multiple subsets of users who use different
                              service domains.

Create the following SRV records (as required):

_cisco-uds._tcp.example.com (on Internal DNS)

_collab-edge._tls.example.com (on External DNS)

Internal Records

The following table lists the SRV records you can provision on internal name servers so the client can discover services:

Service Record

Description

_cisco-uds

Provides the location of CUCM version 10 and higher.

In an environment with multiple CUCM clusters, configure the Intercluster Lookup Service (ILS). ILS enables the client to
                                                      find the user home cluster and discover services.

Use the fully qualified domain name (FQDN) as the hostname in the SRV record.

The following is an example of the _cisco-uds SRV record:

```
_cisco-uds._tcp.example.com     SRV service location:
          priority       = 1
          weight         = 5
          port           = 8443
          svr hostname   = cucm1.example.com
```

```
_cisco-uds._tcp.example.com     SRV service location:
          priority       = 2
          weight         = 20
          port           = 8443
          svr hostname   = cucm2.example.com
```

External Records

The following table lists the SRV record to provision on external name servers as part of the configuration for Expressway
                              Mobile and Remote Access:

Service Record

Description

_collab-edge

Provides the location of the Cisco VCS Expressway or Cisco Expressway-E server.

Use the fully qualified domain name (FQDN) as the hostname in the SRV record.

The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides.

The following is an example of the _collab-edge SRV record:

```
_collab-edge._tls.example.com     SRV service location:
          priority       = 3
          weight         = 7
          port           = 8443
          svr hostname   = vcse1.example.com
```

```
_collab-edge._tls.example.com     SRV service location:
          priority       = 4
          weight         = 8
          port           = 8443
          svr hostname   = vcse2.example.com
```

## Installing the Webex Meetings Virtual Desktop App

### Install the Webex Meetings Virtual Desktop App on Windows

Download and install the Webex Windows and the Webex Meetings Virtual Desktop App agent on your HVD.

Download and install the Webex Meetings Virtual Desktop App on your thin client.

Launch the Webex Meetings Virtual Desktop App on HVD.

### Install the Webex Meetings Virtual Desktop App on Ubuntu

Download and install Webex Windows and the Webex Meetings Virtual Desktop App agent on your HVD.

Download the Webex Meetings Virtual Desktop App Client Debian (.pkg) package and install it on Ubuntu.

Launch the Webex Meetings Virtual Desktop App on HVD.

### Install the Webex Meetings Virtual Desktop App on Unicon eLux

Download Webex Windows and the Webex Meetings Virtual Desktop App agent on your HVD.

Download the Webex Meetings Virtual Desktop App Client. Use the Elias tool to create an image that contains the Webex Meetings Virtual Desktop App Client. Deploy the image to the thin clients. For more information about how to create an image or how to update the thin
                                          client, see the Elias documentation available from the Unicon website.

Launch the Webex Meetings Virtual Desktop App on HVD.

### Install the Webex Meetings Virtual Desktop App on HP ThinPro

Download and install Webex Windows and the Webex Meetings Virtual Desktop App agent on your HVD.

Obtain the Webex Meetings Virtual Desktop App Client Debian (.deb) package and the Cisco- Webex Meetings Virtual Desktop App <xx.x.x> -pre-reqs.xar file from HP. The <xx.x.x> variable in the filename is the Webex Meetings Virtual Desktop App release number. For assistance locating files on the HP site, contact HP support.

To manually install the Webex Meetings Virtual Desktop App Client on the thin clients, copy the files to a USB stick.

On the thin client, install Webex Meetings Virtual Desktop App files in the following order, either manually from a USB stick, or use the HP Device Manager for mass deployments. Order
                                          of installation:

Install cisco-jvdi12.0.x-pre-reqs-thinpro6.2.0-hp1d.xar.

Install the Cisco Jabber Softphone for VDI .deb package.

For more information about mass deployment, see the documentation for HP Device Manager 4.7, available from HP.

Launch the Webex Meetings Virtual Desktop App on HVD.

## Installing the Cisco Webex Meetings Virtual Desktop App When JVDI Co-Exists

Install the cop file for the WVDI on CUCM version 10.5(su2) or later.

Name of the cop file: cmterm-WebexVDI-install-190326.k3.cop.sgn

Link to download the cop file: https://software.cisco.com/download/home/286304684/type/283802941/release/12.6.0

Install the VDI agents for Jabber and Webex on HVD.

Install the VDI clients for Jabber and Webex on Thin Client.

WVDI Version

JVDI Version

HVD installation steps

Thin-Client platform

TC installation steps

Notes

39.3

12.6

Install the JVDI agent.

Install Jabber for windows.

Install the WVDI agent.

Install the Webex Meeting Virtual Desktop Application.

Windows

Install the JVDI windows client or 64-bit client.

Install the  WVDI windows client or 64-bit client.

eLux

Use the Elias tool to create an image that contains the JVDI client and Webex Meeting VDI Client.

Deploy the image to the thin clients.

Ubuntu

Install the  JVDI client Debian ( .deb ) package.

Install the  Webex  Meetings VDI client Debian ( .deb ) package.

Install the apt-get install -f to fetch the new lib package.

ThinPro

Install the cisco-jvdi12.0.x-pre-reqs-thinpro6.2.0-hp1d.xar (pre-required package for VDI).

Install the  JVDI client Debian ( .deb ) package.

Install the  Webex Meetings VDI client Debian ( .deb ) package.

39.3

12.5 or earlier

Install the JVDI agent.

Install Jabber for windows.

Install the WVDI agent.

Install the Webex Meeting Virtual Desktop Application.

Windows

Install the JVDI windows client or 64-bit client.

Install the Webex Meetings VDI windows client or 64-bit client.

eLux

Use the Elias tool to create an image with the JVDI client and Webex Meeting VDI Client.

Deploy the image to the thin clients.

Ubuntu

Install the JVDI client Debian ( .deb ) package.

Install the Webex Meetings VDI client Debian ( .deb ) package.

Command: sudo dpkg -i --force-overwrite xx.deb

Install the apt-get install -f to fetch the new lib package.

Need parameter "--force-overwrite" when installing the WVDI client.

ThinPro

Install the cisco-jvdi12.0.x-pre-reqs-thinpro6.2.0-hp1d.xar (per-required package for the VDI).

2. Install the JVDI client Debian ( .deb ) package.

3. Install the Webex Meetings VDI client Debian ( .deb ) package.

Command: sudo dpkg -i --force-overwrite xx.deb .

Need parameter "--force-overwrite" when installing the WVDI client.

Doesn't support making a call and joining a meeting at same time, as the camera and earphone will be engaged at the same time.

Disconnect the HVD before installing the client on thin clients on all platform.

When your JVDI version is 12.5 or earlier, you need to add the parameter - -force-overwirte when installing the Webex Meetings Virtual Desktop client on Ubuntu and ThinPro. There is no need for the Webex meeting application
                                                and agent.

On Citrix for Linux, there are two Virtual Desktop clients that run at the same time. If the user exit Citrix Desktop or App,
                                                then the Jabber VDI phone service doesn’t disconnect. As this is a Citrix issue, Citrix will fix it for the Linux version
                                                1906 in the current release.

## Installing the Cisco Webex Meetings Virtual Desktop App from Command Line

Before you begin, sign in with local administrative rights.

Open a command line window.

Enter the following command:

msiexec.exe /i CiscoWebexMeetingsSetup.msi

Specify command line arguments as parameter=value pairs.

msiexec.exe /i CiscoWebexMeetingsSetup.msi argument = value

Run the command to install the Webex Meetings Virtual Desktop App .

Example of Installation Commands

To install the Webex Meetings Virtual Desktop App , review the following examples: msiexec.exe /I CiscoWebexMeetingsSetup.msi CLEAR=1 VOICE_SERVICES_DOMAIN=voiceservice.domain.com

CLEAR=1 — Deletes any existing bootstrap file.

Argument

Value

Description

TFTP

IP address

Hostname FQDN

Specifies the address of your TFTP server. Set one of the following as the value:

Hostname (hostname)

IP address (123.45.254.1)

FQDN (hostname.domain.com)

CTI

IP address

Hostname FQDN

Sets the address of your CTI server.

CCMCIP

IP address

Hostname FQDN

Sets the address of your CCMCIP server.

You set Cisco Unified Communications Manager as the authenticator.

The address of your CCMCIP server is not the same as the TFTP server address.

The client can locate the CCMCIP server with the TFTP server address if both addresses are the same.

VOICE_SERVICES_DOMAIN

Domain

If this setting is specified, the client will use the value of VOICE_SERVICES_DOMAIN to lookup the following DNS records for
                                          the purposes of Service Discovery and Edge Detection:

_cisco-uds

_collab-edge

LANGUAGE

LCID in decimal

Defines the Locale ID (LCID), in decimal, of the language that Cisco Jabber for Windows uses. The value is an LCID in decimal
                                          that corresponds to a supported language.

1033 specifies English

1036 specifies French

See the LCID for Languages topic for a full list of the languages that you can specify.

This argument is optional.

If you do not specify a value, the Webex Meetings Virtual Desktop App uses the regional language for the current user as the default.

## Starting the Cisco Webex Meetings Virtual Desktop App

Start the Webex Meetings Virtual Desktop App on HVD. The agent on HVD and client on thin client then start automatically.

| Note | Hosts can start meetings from the Webex Meetings Virtual Desktop App if their site is managed in the Cisco Webex Control Hub, or if their site is managed in the Webex Site Administration and
                                          linked to Control Hub. For more information, see Link Cisco Webex Sites to Control Hub . |
|---|---|

| Note | The Webex Meetings Virtual Desktop Environments is not compatible with the current WBS40.4 Webex Meetings Virtual Desktop
                                          Software. |
|---|---|

| Component | Requirements |
|---|---|
| Microsoft Windows-based thin client hardware | Installed RAM 2 GB Free Physical Memory 128 MB Free Disk Space 256 MB CPU Mobile AMD Sempron Processor 3600+, 2-GHz Intel Core 2 CPU, or T7400 2.16 GHz DirectX 11 compatible GPU USB 2.0 for USB camera and audio devices |
| Microsoft Windows-based thin client OS | Microsoft Windows 7 Microsoft Windows 8 Microsoft Windows 8.1 Microsoft Windows 10 |
| Windows Embedded Standard-based thin client hardware | Installed RAM 2 GB Free Physical Memory 128 MB Free Disk Space 256 MB CPU performance affects the maximum video resolution. With Windows Embedded Standard thin clients, the expected resolution
                                                depends on the CPU: Up to 720p with quad-core AMD GX-420CA SOC 2 GHz or similar Up to 240p with dual-core AMD G-T56N 1.65 GHz or similar Audio-only support with dual-core VIA Eden X2 U4200 1 GHz or similar CPU Note These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. DirectX 11 compatible GPU USB 2.0 for USB camera and audio devices Note The Webex Meetings Virtual Desktop App for Windows does not require the Microsoft .NET Framework or any Java modules. | Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. | Note | The Webex Meetings Virtual Desktop App for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. |
| Note | The Webex Meetings Virtual Desktop App for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 Microsoft Windows 8 Microsoft Windows 8.1 Microsoft Windows 10 |
| Windows Embedded Standard-based thin client OS | Windows Embedded Standard 7 Windows Embedded Standard 8 Windows 10 IoT Enterprise |
| Connection broker for the hosted virtual desktop | Citrix XenDesktop 7.15, and later 7.x versions VMware Horizon 7.0 and later 7.x versions Note To avoid phone connection issues, perform the following steps: On thin clients with 64-bit Windows, select 32-bit Core Remote Experience. On the VMware Horizon installation on the 64-bit machine install the Webex Meetings Virtual Desktop App . | Note | To avoid phone connection issues, perform the following steps: On thin clients with 64-bit Windows, select 32-bit Core Remote Experience. On the VMware Horizon installation on the 64-bit machine install the Webex Meetings Virtual Desktop App . |
| Note | To avoid phone connection issues, perform the following steps: On thin clients with 64-bit Windows, select 32-bit Core Remote Experience. On the VMware Horizon installation on the 64-bit machine install the Webex Meetings Virtual Desktop App . |
| Windows Server | Microsoft Windows 2012 R2 Microsoft Windows 2016 |
| Windows Embedded | Microsoft WES 7 Microsoft WES 8 Microsoft Windows IoT |
| Cisco Unified Communications Manager | Recommended CUCM Release 11.5(1) SU3 or later Minimum CUCM Release 10.5(2) |
| Accessories | For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories . Cisco Webex Meetings Virtual Desktop App does not support using accessories to start or end a meeting, or mute or unmute a meeting. If the host uses the end meeting button to end a meeting, the meeting will end directly, without assigning a new host |

| Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. |
|---|---|

| Note | The Webex Meetings Virtual Desktop App for Windows does not require the Microsoft .NET Framework or any Java modules. |
|---|---|

| Note | To avoid phone connection issues, perform the following steps: On thin clients with 64-bit Windows, select 32-bit Core Remote Experience. On the VMware Horizon installation on the 64-bit machine install the Webex Meetings Virtual Desktop App . |
|---|---|

| Component | Requirements |
|---|---|
| Ubuntu thin clients—Hardware | The following hardware is supported with Ubuntu 14.04 32-bit LTS: Installed RAM 2 GB Free Physical Memory 256 MB Free Disk Space 256 MB CPU: AMD G-T56N 1.65Ghz, or Intel Core 2 Duo T7500 2.2 GHz USB 2.0 for USB camera and audio devices |
| Ubuntu—Hardware | Ubuntu 14.04 32-bit LTS |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 Microsoft Windows 10 Microsoft Windows Server 2016 |
| Connection broker for the hosted virtual desktop | Citrix XenDesktop 7.15, and later 7.x versions VMware Horizon 7.5 and later 7.x versions |
| Citrix Receiver or VMware Horizon Client 2 1 (Installed on the thin client) | 13.8.0 or later (32-bit version required) VMware 4.4.0 or later (32-bit version required) |
| Cisco Unified Communications Manager | Recommended CUCM Release 11.5(1) SU3 or later Minimum CUCM Release 10.5(2) |
| Accessories | For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories . Cisco Webex Meetings Virtual Desktop App does not support using accessories to start or end a meeting, or mute or unmute a meeting. If the host uses the end meeting button to end a meeting, the meeting will end directly, without assigning a new host |

| Component | Requirements |
|---|---|
| Unicon eLux thin clients—Hardware | The minimum hardware requirements for thin clients are: 1.6-GHz dual-core processor 2-GB RAM The following client hardware is tested with eLux RP 5.7.0: HP T520 HP T620 Dual Core/Quad Core HP T630 Dual Core/Quad Core HP T730 |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 Microsoft Windows 10 Microsoft Windows Server 2016 |
| Connection broker for the hosted virtual desktop | Citrix XenDesktop 7.15, and later 7.x versions VMware Horizon 7.5 and later 7.x versions |
| Citrix Receiver or VMware Horizon Client 2 (Installed on the thin client) | 13.8.0 or later (32-bit version required) VMware 4.4.0 or later (32-bit version required) |
| Cisco Unified Communications Manager | Recommended CUCM Release 11.5(1) SU3 or later Minimum CUCM Release 10.5(2) |
| Accessories | For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories . Cisco Webex Meetings Virtual Desktop App does not support using accessories to start or end a meeting, or mute or unmute a meeting. If the host uses the end meeting button to end a meeting, the meeting will end directly, without assigning a new host |

| Component | Requirements |
|---|---|
| HP ThinPro 6.2 - Hardware | The minimum hardware requirements for thin clients are: 1.6-GHz dual-core processor 2-GB RAM Supported devices, thin client with HP ThinPro 6.2 HP T520 HP T620 Dual Core/Quad Core HP T630 Dual Core/Quad Core HP T730 |
| HP ThinPro platform image | HP ThinPro 6.2: T7X62022 |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 Microsoft Windows 10 Microsoft Windows Server 2016 |
| Connection broker for the hosted virtual desktop | Citrix XenDesktop 7.15, and later 7.x versions VMware Horizon 7.5 and later 7.x versions |
| Citrix Receiver or VMware Horizon Client 2 3 (Installed on the thin client) | For HP ThinPro 6.2 The HP ThinPro image includes Citrix and VMware: ICA Client: 13.8.0 or later (32-bit version required) VMware 4.4.0 or later (32-bit version required) |
| Cisco Unified Communications Manager | Recommended CUCM Release 11.5(1) SU3 or later Minimum CUCM Release 10.5(2) |
| Accessories | For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories . Cisco Webex Meetings Virtual Desktop App does not support using accessories to start or end a meeting, or mute or unmute a meeting. If the host uses the end meeting button to end a meeting, the meeting will end directly, without assigning a new host |

| Note | The Webex Meetings Virtual Desktop App Client installer does not add firewall rules. Disable the Windows Firewall on the endpoints, or add an exception to allow
                                          the Webex Meetings Virtual Desktop App . |
|---|---|

| Port | Application Layer Protocol | Transport Layer Protocol | Description |
|---|---|---|---|
| Configuration |
| 6970 | HTTP | TCP | Connect to the TFTP server to download client configuration files. |
| 6972 | HTTPS | TCP | Connects to the TFTP server to download the client configuration files securely for Cisco Unified Communications Manager release
                                             11.0 and later. |
| 53 | DNS | UDP | Hostname resolution. |
| 3804 | CAPF | TCP | Issues Locally Significant Certificates (LSC) to IP phones. This port is the listening port for Cisco Unified Communications
                                             Manager Certificate Authority Proxy Function (CAPF) enrollment. |
| 8443 | HTTPS |  | Traffic to Cisco Unified Communications Manager. |
| Communication Manager Signaling |
| 2748 | CTI | TCP | Computer Telephony Interface (CTI) used for the desk phone control. |
| 5060 | SIP | TCP | Provides Session Initiation Protocol (SIP) call signaling. |
| 5061 | SIP over TLS | TCP | SIP over TCP Provides secure SIP call signaling. (Used if Secure SIP is enabled for the device.) |
| 5070 to 6070 | BFCP | UDP | Binary Floor Control Protocol (BFCP) for video screen sharing capabilities. |
| Voice or Video Media Exchange |
| 16384 to 32766 | RTP/SRTP | UDP | Cisco Unified Communications Manager media port range used for audio, video, and BFCP video desktop share. |
| Cisco Webex Meetings Virtual Desktop App |
| 443 | HTTPS | TCP | Connects to Cisco Webex Meetings for meetings. |

| Direction | Transport Protocol | Destination Port | Purpose |
|---|---|---|---|
| External Network => UAG | TCP/UDP | 443 | Blast Extreme |
| 4172 | PCoIP |
| 8443 | HTML Blast |
| Internal Network (Administration) => UAG | TCP | 9443 | REST API |
| TCP | 80/443 | Edge Gateway |
| UAG => Internal Network (VDI) | TCP | 443 | Connection Server |
| TCP/UDP | 4172 | PCoIP |
| TCP | 32111 | USB Redirection |
| TCP/UDP | 22443 | Blast Extreme |
| TCP | 9427 | MMR/CDR |
| TCP/UDP | 53 | DNS Query |

|  |  |  |  |
|---|---|---|---|
| External Network => NetScaler | TCP | 80 | Connection from Citrix Receiver |
| TCP/UDP | 443 |
| Internal Network => NetScaler | TCP | 80 | Connection from Citrix Receiver |
| TCP/UDP | 443 | Authentication callback from StoreFront Server / Connection from Citrix Receiver |
| TCP | 22 | NetScaler Administration |
| 80 |
| 443 |
| 3010 |
| 3008 |
| NetScaler => Internal Network (VDI) | TCP/UDP | 53 | DNS Query |
| UDP | 123 | NTP |
| TCP | 389 | LDAP Query |
| 636 |
| TCP | 443 | Citrix StoreFront Server |
| 80 |
| 808 |
| TCP | 80 | Citrix Delivery Controller |
| 443 |
| TCP/UDP | 1494 | HDX ICA |
| 2598 |
| UDP | 16500-16509 |
| 3224-3324 |

| Audio Codec | Video Codec |
|---|---|
| G.722 | H.264/AVC |
| G.722.1 (24 and 32k) G.722.1 is supported on Cisco Unified Communications Manager 8.6.1 or later. |  |
| G.711 A-law |  |
| G.711 u-law |  |
| G.729a |  |
| Opus Opus is supported on Cisco Unified Communications Manager 11.0 or later. |  |

| Note | The steps to add the WSF device are the same as the steps to add a CSF device. |
|---|---|

| Note | Any configurations or credentials are cached in HVD only and not in the thin client. |
|---|---|

| Deployment | User Experience |
|---|---|
| Both the meeting site and CUCM are SSO-enabled | Enter the email to start the service discovery. Enter the username and password in the browser. The pre-meeting UI displays. |
| The meeting site is SSO-enabled but CUCM is not SSO-enabled | Enter the email to start service discovery. Enter the username and password in the browser. The pre-meeting UI displays. Enter the CUCM credentials in the pop-up window. |
| The meeting site is not SSO-enabled but CUCM can either be SSO-enabled or not SSO-enabled | Enter the email to start the service discovery. Enter the username and password for meeting account credentials. The pre-meeting UI displays. Enter CUCM credentials if it is different with meeting credentials. |

| Note | If CUCM is not installed, see Installation Guide for Cisco Unified Communications Manager for installation instructions. |
|---|---|

| Note | Failure to meet all requirements can result in a non-functional deployment. |
|---|---|

| Note | Create a dedicated directory number for WSF Device. |
|---|---|

| Note | You require domain administration rights. |
|---|---|

| Note | The Webex Meetings Virtual Desktop App supports the English Operating System in the current release. If you are using an Operating System other than English, install
                                                the Webex Meetings Desktop App using command line: msiexec.exe /i CiscoWebexMeetingsSetup.msi CLEAR=1 |
|---|---|

| Note | For more information on the best practices for cloning Microsoft Windows HVD images, see the documentation for your Citrix
                                                or VMware product. |
|---|---|

| Note | When installing the Webex Meetings Virtual Desktop client on thin client, disconnect the connection with HVD. |
|---|---|

| Note | The Webex Meetings Virtual Desktop App supports the English Operating System in the current release. If you are using an Operating System other than English, install
                                                the Webex Meetings Virtual Desktop App using command line: msiexec.exe /i CiscoWebexMeetingsSetup.msi CLEAR=1 |
|---|---|

| Service Record | Description |
|---|---|
| _cisco-uds | Provides the location of CUCM version 10 and higher. Important In an environment with multiple CUCM clusters, configure the Intercluster Lookup Service (ILS). ILS enables the client to
                                                      find the user home cluster and discover services. | Important | In an environment with multiple CUCM clusters, configure the Intercluster Lookup Service (ILS). ILS enables the client to
                                                      find the user home cluster and discover services. |
| Important | In an environment with multiple CUCM clusters, configure the Intercluster Lookup Service (ILS). ILS enables the client to
                                                      find the user home cluster and discover services. |

| Important | In an environment with multiple CUCM clusters, configure the Intercluster Lookup Service (ILS). ILS enables the client to
                                                      find the user home cluster and discover services. |
|---|---|

| Note | Use the fully qualified domain name (FQDN) as the hostname in the SRV record. |
|---|---|

| Service Record | Description |
|---|---|
| _collab-edge | Provides the location of the Cisco VCS Expressway or Cisco Expressway-E server. Use the fully qualified domain name (FQDN) as the hostname in the SRV record. Note The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. | Note | The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |
| Note | The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |

| Note | The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |
|---|---|

| Step 1 | Download and install the Webex Windows and the Webex Meetings Virtual Desktop App agent on your HVD. |
|---|---|
| Step 2 | Download and install the Webex Meetings Virtual Desktop App on your thin client. |
| Step 3 | Launch the Webex Meetings Virtual Desktop App on HVD. |

| Step 1 | Download and install Webex Windows and the Webex Meetings Virtual Desktop App agent on your HVD. |
|---|---|
| Step 2 | Download the Webex Meetings Virtual Desktop App Client Debian (.pkg) package and install it on Ubuntu. |
| Step 3 | Launch the Webex Meetings Virtual Desktop App on HVD. |

| Step 1 | Download Webex Windows and the Webex Meetings Virtual Desktop App agent on your HVD. |
|---|---|
| Step 2 | Download the Webex Meetings Virtual Desktop App Client. Use the Elias tool to create an image that contains the Webex Meetings Virtual Desktop App Client. Deploy the image to the thin clients. For more information about how to create an image or how to update the thin
                                          client, see the Elias documentation available from the Unicon website. |
| Step 3 | Launch the Webex Meetings Virtual Desktop App on HVD. |

| Step 1 | Download and install Webex Windows and the Webex Meetings Virtual Desktop App agent on your HVD. |
|---|---|
| Step 2 | Obtain the Webex Meetings Virtual Desktop App Client Debian (.deb) package and the Cisco- Webex Meetings Virtual Desktop App <xx.x.x> -pre-reqs.xar file from HP. The <xx.x.x> variable in the filename is the Webex Meetings Virtual Desktop App release number. For assistance locating files on the HP site, contact HP support. |
| Step 3 | To manually install the Webex Meetings Virtual Desktop App Client on the thin clients, copy the files to a USB stick. |
| Step 4 | On the thin client, install Webex Meetings Virtual Desktop App files in the following order, either manually from a USB stick, or use the HP Device Manager for mass deployments. Order
                                          of installation: Install cisco-jvdi12.0.x-pre-reqs-thinpro6.2.0-hp1d.xar. Install the Cisco Jabber Softphone for VDI .deb package. For more information about mass deployment, see the documentation for HP Device Manager 4.7, available from HP. |
| Step 5 | Launch the Webex Meetings Virtual Desktop App on HVD. |

| WVDI Version | JVDI Version | HVD installation steps | Thin-Client platform | TC installation steps | Notes |
|---|---|---|---|---|---|
| 39.3 | 12.6 | Install the JVDI agent. Install Jabber for windows. Install the WVDI agent. Install the Webex Meeting Virtual Desktop Application. | Windows | Install the JVDI windows client or 64-bit client. Install the  WVDI windows client or 64-bit client. |  |
| eLux | Use the Elias tool to create an image that contains the JVDI client and Webex Meeting VDI Client. Deploy the image to the thin clients. |  |
| Ubuntu | Install the  JVDI client Debian ( .deb ) package. Install the  Webex  Meetings VDI client Debian ( .deb ) package. Install the apt-get install -f to fetch the new lib package. |  |
| ThinPro | Install the cisco-jvdi12.0.x-pre-reqs-thinpro6.2.0-hp1d.xar (pre-required package for VDI). Install the  JVDI client Debian ( .deb ) package. Install the  Webex Meetings VDI client Debian ( .deb ) package. |  |
| 39.3 | 12.5 or earlier | Install the JVDI agent. Install Jabber for windows. Install the WVDI agent. Install the Webex Meeting Virtual Desktop Application. | Windows | Install the JVDI windows client or 64-bit client. Install the Webex Meetings VDI windows client or 64-bit client. |  |
| eLux | Use the Elias tool to create an image with the JVDI client and Webex Meeting VDI Client. Deploy the image to the thin clients. |  |
| Ubuntu | Install the JVDI client Debian ( .deb ) package. Install the Webex Meetings VDI client Debian ( .deb ) package. Command: sudo dpkg -i --force-overwrite xx.deb Install the apt-get install -f to fetch the new lib package. | Need parameter "--force-overwrite" when installing the WVDI client. |
| ThinPro | Install the cisco-jvdi12.0.x-pre-reqs-thinpro6.2.0-hp1d.xar (per-required package for the VDI). 2. Install the JVDI client Debian ( .deb ) package. 3. Install the Webex Meetings VDI client Debian ( .deb ) package. Command: sudo dpkg -i --force-overwrite xx.deb . | Need parameter "--force-overwrite" when installing the WVDI client. |

| Note | Doesn't support making a call and joining a meeting at same time, as the camera and earphone will be engaged at the same time. Disconnect the HVD before installing the client on thin clients on all platform. When your JVDI version is 12.5 or earlier, you need to add the parameter - -force-overwirte when installing the Webex Meetings Virtual Desktop client on Ubuntu and ThinPro. There is no need for the Webex meeting application
                                                and agent. On Citrix for Linux, there are two Virtual Desktop clients that run at the same time. If the user exit Citrix Desktop or App,
                                                then the Jabber VDI phone service doesn’t disconnect. As this is a Citrix issue, Citrix will fix it for the Linux version
                                                1906 in the current release. |
|---|---|

| Argument | Value | Description |
|---|---|---|
| TFTP | IP address Hostname FQDN | Specifies the address of your TFTP server. Set one of the following as the value: Hostname (hostname) IP address (123.45.254.1) FQDN (hostname.domain.com) Specify this argument if you set Cisco Unified Communications Manager as the authenticator. |
| CTI | IP address Hostname FQDN | Sets the address of your CTI server. Specify this argument if you set Cisco Unified Communications Manager as the authenticator. |
| CCMCIP | IP address Hostname FQDN | Sets the address of your CCMCIP server. Specify this argument if: You set Cisco Unified Communications Manager as the authenticator. The address of your CCMCIP server is not the same as the TFTP server address. The client can locate the CCMCIP server with the TFTP server address if both addresses are the same. |
| VOICE_SERVICES_DOMAIN | Domain | If this setting is specified, the client will use the value of VOICE_SERVICES_DOMAIN to lookup the following DNS records for
                                          the purposes of Service Discovery and Edge Detection: _cisco-uds _collab-edge This setting is optional and if not specified, the DNS records are queried on email address input by the user, or cached
                                       user configuration. |
| LANGUAGE | LCID in decimal | Defines the Locale ID (LCID), in decimal, of the language that Cisco Jabber for Windows uses. The value is an LCID in decimal
                                          that corresponds to a supported language. For example, you can specify one of the following: 1033 specifies English 1036 specifies French See the LCID for Languages topic for a full list of the languages that you can specify. This argument is optional. If you do not specify a value, the Webex Meetings Virtual Desktop App uses the regional language for the current user as the default. The regional language is set at Control Panel > Region and Language > Change the date, time, or number format > Formats tab > Format dropdown . |