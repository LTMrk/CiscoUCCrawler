---
doc_id: help-webex-com-en-us-article-19qt9v-deployment-guide-for-webex-app-for-virtual-desktop-infrastructure-vdi-a14628d9b9
source_url: https://help.webex.com/en-us/article/19qt9v/Deployment-guide-for-Webex-App-for-Virtual-Desktop-Infrastructure-(VDI)
retrieved_at: 2026-09-07T10:36:41.809897+00:00
---

### Webex App VDI login flow

The Webex App VDI architecture consists of two primary components: the Webex App for VDI and the Webex VDI plugin for the thin client. The VDI plugin is installed
                on a thin client while the app is installed on the HVD.

When a user launches a virtual broker-client (Citrix Workspace app or VMWare Horizon
                Client), the vendor's software initiates a virtual channel. The Webex App plugin and agent use this virtual channel to communicate.

This diagram shows the expected protocol sessions that are set up during normal Webex App use when deployed with Unified CM calling over Mobile and Remote Access (MRA).

Although the diagram depicts Webex App VDI over MRA, the flow is the same as an on-premises VDI deployment. However,
                    unlike VDI over MRA, on-premises deployments don't route traffic through the DMZ
                    and all the traffic resides on the LAN.

To start a session, users first launch their virtual broker-client (Citrix
                        Workspace App or VMware Horizon Client),connect to the connection broker,
                        and then select an HVD or virtual application. Once selected, a virtual
                        channel is set up between the user's thin client (physical machine) and the
                        HVD (virtual machine) hosted on the Hypervisor.

After a user launches the Webex App on the HVD, Webex determines if it is in a virtual environment and if
                        Unified CM is used for phone service. If Unified CM is enabled, the Webex App starts the teamshvdagent.exe process and begins
                        internal service discovery. (The internal service discovery includes the UDS
                        DNS SRV lookup, Unified CM authentication, home cluster lookup, and
                        configuration retrieval.)

The Webex App client and Webex App VDI plugin then go set up all the control streams that are used to
                        exchange data over the virtual channel. After these channels are set up, the
                            Webex App client sends the voice service domain information to the Webex App VDI plugin.

Next, the Webex App VDI plugin performs service discovery. The Webex App VDI plugin does this by referencing the voice service domain information
                        that was sent to it from the Webex App client. In this scenario, the Webex App VDI plugin resolves the _collab-edge DNS SRV record because the VDI
                        plugin machine is connecting from an external network, therefore needing to
                        connect over MRA. Once service discovery is complete, Webex App VDI plugin sends the Expressway-E FQDN to the Webex App client.

After receiving and caching the Expressway-E FQDN, the Webex App (HVD) then performs a DNS A record lookup for the Expressway-E FQDN. For
                        a single NIC deployment, this step retrieves the Expressway-E's IP address
                        (internal IP with split DNS or external IP without split DNS), which is used
                        for Edge configuration and SSO authentication over port 8443.

If Expressway-E is set up in a dual NIC deployment, both interfaces can
                            have an internal IP address. In this case, the internal interface is the
                            opposite of what's configured for the external interface.

After the Edge details are retrieved, the Webex App (HVD) establishes HTTPS connections to the Expressway-E IP for UDS and
                        TFTP requests. Through this process, the Webex App (HVD) authenticates and retrieves configuration details, such as
                        Soft-phone Device Config, Application Dial Rules, and Directory Lookup Dial
                        Rules.

The Webex VDI plugin resolves the Expressway-E external IP and then sends to
                        the Webex App (HVD). Through the device information that is retrieved in the previous
                        step, Webex App begins the CSF device (Windows desktop) registration through the
                        Expressway-E external interface.

### Hosted virtual desktop and thin client requirements

Make sure your VDI environment meets the requirements for the supported
                                servers (Hosted Virtual Desktop (HVD), where the Webex app is
                                installed) and thin clients (user-side device where the Webex VDI
                                plugins are installed).

For users joining Webex meetings from Webex App, please refer to Hosted virtual
                                                desktop and thin client requirements for Webex
                                                meetings VDI .

#### Hosted virtual desktop

VDI component

Supported platforms

Microsoft Windows 11

Microsoft Windows 10

Windows 365 Cloud PC

Multi-session operating system—Installed on the HVD

Microsoft Windows Server 2016

Microsoft Windows Server 2019

Microsoft Windows Server 2022

Microsoft Windows Server 2025

Multi-session cloud virtualization service

Azure Virtual Desktop (AVD, formerly Windows Virtual
                                        Desktop)—provides virtualization for Windows 7 Enterprise,
                                        Windows 10 Enterprise and Windows 11 Enterprise

Horizon on VMware Cloud (installed on AWS)

Citrix Virtual Apps and Desktops 7 CR 2511

Citrix Virtual Apps and Desktops 7 2507 LTSR CU1

Citrix Virtual Apps and Desktops 7 2402 LTSR CU3

Citrix Virtual Apps and Desktops 7 2203 LTSR CU7

The following are supported:

Multi-session OS published desktop

Single-session OS for VDI desktop

Citrix Remote PC sessions

Published Application (supported by Windows-base Thin
                                                / Fat Client)

If you enabled virtual channel allow list policy in your deployment, then you must add the Webex app virtual channel (CSCOTM) to the allow list with the virtual channel name and process path: "CSCOTM,C:\Program Files\Cisco Spark\dependencies\teamshvdagent.exe"

Since Citrix Virtual Apps and Desktops 7 2109,
                                                  "virtual channel allow list policy" is enabled by
                                                  default. You must configure this policy for Webex
                                                  App VDI first (add Cisco Virtual Channel) for
                                                  optimized mode to function properly, or disable
                                                  this policy.

For MacOS, currently only Webex App VDI plugin
                                                  41.12 works with Citrix Workspace App 2111 for
                                                  Mac.

Omnissa (formerly VMware) Horizon Agent:

8 2006 (8.0) to 8 2512 (8.17)

The following are supported:

Shared Desktop

Published Desktop

Published Application (supported by Windows-base Thin
                                                / Fat Client)

Remote Desktop App for AVD

You must use the version of this app from the direct download
                                                page . The app on the Microsoft Store is not
                                            supported.

Amazon WorkSpaces with WSP (DCV)

A connection broker is software that creates connections to hosted
                                virtual desktops. A connection broker performs a number of tasks
                                including the following:

Validating the username and providing a connection for the
                                        user.

Allowing the user to connect to a specific virtual
                                        desktop.

#### Windows thin clients

VDI component

Supported platforms

Supported Hardware

2 GB installed RAM

128 MB physical memory

256 MB disk space

Minimum CPU Mobile AMD Sempron Processor 3600+, 2-GHz Intel
                                        Core 2 CPU, or T7400 2.16 GHz

DirectX 11-compatible GPU

USB 2.0 ports for camera and audio devices

If you want users to use virtual backgrounds, you must meet the virtual background requirements .
                                        (Webex App for VDI has the same requirements as the Windows standalone
                                    app.)

Supported Software

We support 64-bit architectures for the following Windows versions:

Microsoft Windows 10

Microsoft Windows 11 (for VDI plugin 41.12 and later)

Supported Hardware

Installed RAM 2 GB

Free Physical Memory 128 MB

Free Disk Space 256 MB

CPU performance affects the maximum video resolution. With Windows
                                Embedded Standard thin clients, the expected resolution depends on
                                the CPU:

Up to 720p with quad-core AMD GX-420CA SOC 2 GHz or
                                        similar

Up to 240p with dual-core AMD G-T56N 1.65 GHz or similar

Audio-only support with dual-core VIA Eden X2 U4200 1 GHz or
                                        similar CPU

These hardware specifications are only guidelines for the
                                    expected resolutions. Other factors can affect video
                                    resolution.

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

Supported Software

Windows 10 IoT

Citrix Workspace app or VMware Horizon client

Citrix Receiver 4.9 and later

Citrix Workspace app 1808 and later

VMware Horizon View Client version 5.x

VMWare Horizon client version 8.x (2103) is supported from
                                        the Webex VDI plugin version 41.4 onward.

VMware Horizon client version 8.x (2106) for Webex VDI plugin
                                        version 41.8 onward.

Amazon WorkSpaces 5.15 and later

Omnissa Horizon Client (formerly VMware Horizon) is supported
                                        from the Webex App and VDI plugins version 45.2 onward.

Windows App for AVD is supported from the Webex App and VDI
                                        plugins version 45.4 onward.

#### Linux thin clients

VDI component

Supported platforms

Ubuntu (64-bit)

16.04

18.04

20.04

22.04

24.04

Unicon eLux (64-bit)

6.5.2000 (End of life)

6.9 (End of life)

RP6 2104 LTSR (Webex VDI plugin 41.8 and later)

RP6 2302 LTSR (Webex VDI plugin 43.4 and later)

RP6 2302 LTSR CU 1 (Webex VDI plugin 43.8 and later)

RP6 2302 LTSR CU 2 (Webex VDI plugin 43.12 and later)

RP7 2409 LTSR (Webex VDI plugin 44.12 and later)

HP ThinPro 7.1 (End of life)

HP ThinPro 8.0, 8.1 (64-bit)

SP 13.5 and later for Webex app plugin release 41.1 and
                                        later

SP 3.4-12.7 for Webex app plugin release that are earlier
                                        than 41.1

IGEL OS

- 11.04.100 and later

- 12 (Webex VDI plugin 43.10 and later)

The Webex VDI plugin is packaged with IGEL OS. Because of this
                                    third-party integration, you must contact IGEL for technical
                                    support. For more information, see the IGEL OS documentation for your supported release; the Component Versions section of their release notes mentions the version of the Webex
                                    VDI plugin that's integrated and supported. See the software download page to get a copy of the OS installation package.

Dell Wyse ThinOS

ThinOS 9.4

9.4 ( Release Notes )

Specific versions of the Webex VDI plugin are supported with Dell
                                    Wyse ThinOS. Because of this third-party integration, you must
                                    contact Dell for technical support. For more information, see
                                    the Dell Wyse ThinOS
                                        documentation for your supported release; the Supported packages section of their release notes
                                    mentions the version of the Webex VDI plugin that's supported.
                                    See the software download page to get a copy of the OS installation package.

10ZiG Zero Client Thin Clients

Specific versions of the Webex VDI plugin are supported with
                                    10ZiG zero client thin clients. Because of this third-party
                                    integration, you must contact 10ZiG for technical support. For
                                    more information, see the 10ZiG page for your
                                    specific thin client.

Stratodesk NoTouch OS

Specific versions of the Webex VDI plugin are supported with
                                    Stratodesk NoTouch OS. Because of this third-party integration,
                                    you must contact Stratodesk for technical support. For more
                                    information, see the Stratodesk NoTouch OS documentation for your supported release.

The minimum hardware requirements for thin clients are as
                                follows:

CPU: Any 64-bit x86 CPU.

Memory: 2GB of memory, with at least 1GB free for operating
                                        system use.

Storage: 2GB or more of internal storage for
                                        installation.

Graphics: Intel, ATI/AMD, or Nvidia. If the graphics card is
                                        not recognized, limited-performance VESA mode can be
                                        used.

Audio: Audio support is optional.

Networking: A recognized wired or wireless network
                                        adapter.

USB: HP recommends 2.0 or 3.0 or USB-C high-performance flash
                                        drives

If you want users to use virtual backgrounds, you must meet the virtual background
                                        requirements . (Webex App for VDI has the same requirements as the Windows standalone
                                    app.)

Minimum hardware requirements

The following system properties enable using basic eLux RP 6
                                features.

Processor: x86, 1 GHz (2 CPUs), 64-bit-capable

RAM: 2 GB

HDD: 2 GB

GPU: AMD or Intel graphics chipset

I/O ports: USB 2.0

If you want users to use virtual backgrounds, you must meet the virtual background requirements .
                                        (Webex App for VDI has the same requirements as the Windows standalone
                                    app.)

HP T640

HP T740

HP mt32

HP mt45

HP mt46

HP t730

Dell Optiplex 7060

Lenovo ThinkCentre M710q

Dell 3040*—eLux 6.5

Dell 5060*—eLux 6.5

Dell 5070*—eLux 6.5

Dell Z50Q*—eLux 6.5

HP T430*—Thinpro 7.1 / eLux 6.5

HP T520*—Thinpro 7.1 / eLux 6.5

HP T530*—Thinpro 7.1 / eLux 6.5

HP T630*—Thinpro 7.1 / eLux 6.5

HP mt21*—Thinpro 7.1 / eLux 6.5

* Based on hardware requirements, HP thin clients models t640, t540,
                                and t630 do not support virtual backgrounds at all. See virtual background requirements for more
                                information. (Webex App for VDI has the same requirements as the Windows standalone app.)

Citrix Workspace app or VMware Horizon client

Citrix Receiver 4.9 and later

Citrix Workspace app 1808 and later

VMware Horizon View Client versions 5.x

VMWare Horizon client version 8.x (2103) for Webex VDI plugin
                                        version 41.4 onward.

VMware Horizon client version 8.x (2106) for Webex VDI plugin
                                        version 41.8 onward.

#### macOS thin clients

VDI component

Supported platforms

Supported hardware

Minimum CPU: Apple M2 chip or Intel Core 2 Duo processor

2 GB installed RAM

1 GB physical memory

300 MB disk space

USB 2.0 ports for camera and audio devices

Intel Core 2 Duo or later processors on any of the following
                                    Apple hardware:

iMac Pro

MacBook Pro

MacBook

MacBook Air

iMac

Mac Mini

If you want users to use virtual backgrounds, you must meet
                                        the virtual background
                                            requirements . (Webex App for VDI has the same requirements as the Windows
                                        standalone app.)

Supported software

The Webex App VDI plugin is supported on the following macOS versions:

Sequoia (15.x) for VDI plugin release 44.10 and later

Sonoma (14.x) for VDI plugin release 43.10 and later

Ventura (13.x) for VDI plugin release 42.12 and later

Monterey (12.x) for VDI plugin release 41.12 and later

Citrix Workspace app or VMware Horizon client

From version 42.10 onwards, Webex App VDI plugin supports both Citrix Workspace App and VMware Horizon Client for macOS - Native support for Mac with Apple Silicon (M1 Series).

Citrix Workspace app 2008 and later

For macOS, currently only the Webex App VDI plugin
                                                41.12 works with Citrix Workspace App 2111 for
                                                Mac.

The macOS plugin does not work with Citrix Workspace
                                                App 21.08 or 21.08.1.

VMware Horizon View Client version 7 (5.x) and 8

For installing or upgrading VMware Horizon Client, we
                                                recommend that you launch the client once before
                                                deploying the Webex App VDI plugin (up to version 41.12). See Loading 3rd Party
                                                  Mac plugins with Session Enhancement SDK for more information.

Amazon WorkSpaces 5.17 and later

### Webex App and plugin requirements

Get the necessary install builds of the Webex App (installed on HVD) and Webex App plugin (installed on a user's thin client machine) from the Downloads tab of the Webex App VDI release notes .

While we support backwards compatibility, as outlined in the release
              notes , we recommend that you use the latest versions of the install builds
            wherever possible.

For users joining Webex meetings from Webex App, please refer to Hosted virtual desktop and thin client requirements for Webex meetings VDI .

VDI users typically do not have admin control over their
            machine and the plugin does not require admin privileges. However, if your users require
            Outlook integration, you must register the office integration .dll file using the
            directions in Enable users' status to display in Microsoft Outlook .

### Headset Requirements

For Webex App VDI, we support the same headsets as the standalone Webex App unless otherwise noted. See Details about headset support for more
                information.

### Supported realtime media workflows for calling and meetings

Webex App VDI supports the following realtime media workflows:

Calls on Webex (built into the app)

Unified CM

Webex Calling

Webex for BroadWorks

Webex Meetings

To integrate a supported calling service and Webex Meetings, you must follow
                configuration steps in the documentation for those solutions. Choose an option and
                then use the documentation that is linked in that section.

#### Unified CM requirements

If you want to use Unified CM as your call
                                                  service for Webex App VDI users, use the Deployment Guide to walk
                                                  through the required configuration steps. The
                                                  document contains an overview of the service,
                                                  prerequisites, and deployment steps.

##### Move a call to a meeting

To support this feature, make sure you've configured your
                                                  Unified CM calling deployment
                                                  correctly .

Additionally, make sure the following VDI
                                                  configuration is in place so that offloading to
                                                  meetings is supported: Full-featured meetings requirements .

##### Mobile and Remote Access (MRA)

Mobile and Remote Access (MRA) is supported.
        Follow the standard MRA deployment steps in the Expressway MRA documentation and keep the following
        points in mind for a supported VDI deployment:

See Mobile and Remote Access (MRA) requirements for more guidance for VDI support.

You must run a minimum of X12.7 and later.

Dual NIC deployments are supported. You must
            ensure there's a connection from the HVD to both the external and internal IP addresses
            of the Expressway-E. You must add a NAT between the HVD and the external IP of the
            Expressway-E.

#### Webex Calling requirements

If your HVD supports IPv4 and IPv6, we recommend that you disable IPV6 in your
                    HVD environment to prevent compatibility issues with Webex Calling.

##### Configuration in Control Hub (partners and administrators)

Control Hub ( https://admin.webex.com ) is a web-based management portal that integrates withWebex Calling to streamline your orders and configuration, and centralize your management of the bundled offer—Webex Calling, Webex App, and Meetings.

As a partner service provider, you can brand, market, and sell Webex Calling to your customers. You can set up and extend trials, deploy services for your customers, and create and provision orders for your customers. For more partner resources, see the Webex Calling Sales Connect resources . (Requires partner credentials).

As a customer administrator on a trial or paid subscription to Webex Calling, you can set up your organization in the Control Hub by adding locations, licenses, phone numbers, calling features, users, and Workspaces (Room Devices that register to the Webex cloud).

Make sure that your environment supports Webex Calling by following the prerequisites and port reference material before you start specific configuration steps in the Control Hub. You can refer to the following configuration work flow diagram and the article links, in the order presented, to get your organization up and running with Webex Calling:

For more information on the Webex Calling offer, see Cisco Webex Calling in the Cisco Collaboration Flex Plan for End Customers Data Sheet .

#### Webex for BroadWorks requirements

The Webex App in a VDI environment supports Webex for BroadWorks. Webex for BroadWorks is an
                offer that integrates BroadWorks Calling in Webex. Subscribers use a single
                application (the Webex App) to take advantage of features provided by both
                platforms.

For general information about Webex for BroadWorks, see the Webex for BroadWorks Solution Guide .

#### Full-featured meetings requirements

Keep these points in mind when deploying Webex App VDI for full-featured meetings:

Install the Webex App onto the Hosted Virtual Desktop (HVD).

You must install Webex App VDI plugin for users joining full-featured Webex meetings.

Refer to Hosted virtual desktop and thin client requirements for Webex meetings VDI .

For Linux thin clients, you must also install the Webex Meetings VDI plugin for Linux (see Install Webex Meetings VDI plugin on thin client systems ).

### Mobile and Remote Access (MRA) requirements

#### Prerequisites

You must run a minimum of Expressway
                            X12.7 for the traversal pair for MRA to work with Webex VDI.
                        Earlier versions must be upgraded to X12.7 or later to avoid routing
                        issues.

Ensure connectivity between Webex in the HVD environment, external interface,
                        and internal interface (dual NIC deployment) of Expressway.

#### MRA with Webex App VDI workflow

For information about the MRA with Webex VDI workflow, see Webex App VDI login flow .

#### Dual NIC considerations

Keep these design considerations in mind when deployment Webex App VDI over MRA with an Expressway-E dual NIC deployment.

Static route —Verify the default gateway on the Expressway-E.
                        Typically, this is the default gateway of the external interface IP subnet.
                        Once you verify the Expressway default gateway configuration, you must add a
                        Static Route to the Expressway-E for the IP subnet that is used for the HVD
                        machines.

The static route sends traffic out of the internal interface of the
                        Expressway-E to the HVD subnet. This configuration is needed, because of the
                        UDS and TFTP config queries sent from the HVD to the Expressway E internal
                        interface. Once Unified CM responds to the request, the Expressway-E sends
                        the response through the default gateway if the static route to the HVD
                        subnet does not exist.

NAT transition —The SIP traffic from the HVD to the Expressway-E
                        external interface needs to have the source IP changed before reaching the
                        Expressway to avoid a routing issue. NAT addresses this problem. A NAT
                        translation must be put in place on a network device that is the path
                        between the HVD and Expressway-E.

#### DNS configuration

##### Internal DNS

For dual NIC deployments , you can specify the Expressway-E address
                        using a FQDN that resolves to the IP address of the internal interface. With
                        split DNS, you can optionally use the same FQDN that is available on the
                        public DNS. If you don't use split DNS, you must use a different FQDN.

To avoid a routing issue, the SIP traffic from the HVD to the Expressway-E
                        external interface needs to have the source IP changed before reaching the
                        Expressway. You must set up a NAT translation on a network device that is
                        between the HVD and Expressway-E.

For single NIC with static NAT , you must specify the Expressway-E
                        address using a FQDN that resolves to the public IP address. This setup also
                        means that the external firewall must allow traffic from the Webex app in
                        HVD to the external FQDN of the Expressway-E. This design is known as NAT
                        reflection, and may not be supported by all types of firewalls.

The internal DNS must be configured with _cisco-uds._tcp.<domain> SRV records so that the
                        Webex app can discover Unified CM.

##### Public DNS

###### SRV records

The public, external DNS must be configured with _collab-edge._tls.<domain> SRV records so that endpoints can discover the Expressway-Es to use for MRA.

###### GeoDNS

In versions 43.6 and later, you can configure the Webex App to work with GeoDNS. This option improves network efficiency by enabling the App to connect to the geographically nearest Expressway-E.

If you have configured GeoDNS for your SRV records, we recommend that you edit the registry on your HVD as follows:

Open the registry to HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Spark Native .

Create a new DWORD key named VDIGeoDnsEnabled .

Set VDIGeoDnsEnabled to 1 .

(Set VDIGeoDnsEnabled to 0 (the default) if you want to disable GeoDNS compatibility for the Webex App on this HVD).

Save the registry.

#### Firewall configuration

Both the internal and external firewall must allow the following outbound connections
                from Webex App on the HVD to Expressway-E:

SIP—TCP 5061

HTTPS—TCP 8443

The external firewall must also allow the following inbound connections from the user
                thin client to Expressway:

Media—UDP 36002–59999

#### Fallback mode

When a users local device accesses the internet without MRA, the Webex App typically
        defaults to VDI fallback mode. However, users can maintain VDI optimized mode by adding the
        "VDIFallbackNoMRA" registry key in the HVD.

- In Windows Search or Run , open the
          registry editor by typing regedit and press Enter

- Go to HKEY_LOCAL_MACHINE\Software\Cisco Spark Native\.

Registry key values

- 1- If MRA isn’t configured, the Webex App switches to fallback mode upon signing in.
              Users can still make and receive calls and join meetings, but in non-optimized mode.
              (Default)

- 0- Without MRA configuration, calls fail under MRA, but Webex VDI remains in
              optimized mode. Meetings are optimized, but users can't make or receive calls due to
              unavailable phone service.

| VDI component | Supported platforms |
|---|---|
| Single-session operating system—Installed on the HVD | Microsoft Windows 11 Microsoft Windows 10 Windows 365 Cloud PC |
| Multi-session operating system—Installed on the HVD | Microsoft Windows Server 2016 Microsoft Windows Server 2019 Microsoft Windows Server 2022 Microsoft Windows Server 2025 |
| Multi-session cloud virtualization service | Azure Virtual Desktop (AVD, formerly Windows Virtual
                                        Desktop)—provides virtualization for Windows 7 Enterprise,
                                        Windows 10 Enterprise and Windows 11 Enterprise Horizon on VMware Cloud (installed on AWS) |
| Connection broker for the hosted virtual desktop | Citrix Virtual Apps and Desktops 7 CR 2511 Citrix Virtual Apps and Desktops 7 2507 LTSR CU1 Citrix Virtual Apps and Desktops 7 2402 LTSR CU3 Citrix Virtual Apps and Desktops 7 2203 LTSR CU7 The following are supported: Multi-session OS published desktop Single-session OS for VDI desktop Citrix Remote PC sessions Published Application (supported by Windows-base Thin
                                                / Fat Client) If you enabled virtual channel allow list policy in your deployment, then you must add the Webex app virtual channel (CSCOTM) to the allow list with the virtual channel name and process path: "CSCOTM,C:\Program Files\Cisco Spark\dependencies\teamshvdagent.exe" Since Citrix Virtual Apps and Desktops 7 2109,
                                                  "virtual channel allow list policy" is enabled by
                                                  default. You must configure this policy for Webex
                                                  App VDI first (add Cisco Virtual Channel) for
                                                  optimized mode to function properly, or disable
                                                  this policy. For MacOS, currently only Webex App VDI plugin
                                                  41.12 works with Citrix Workspace App 2111 for
                                                  Mac. Omnissa (formerly VMware) Horizon Agent: 8 2006 (8.0) to 8 2512 (8.17) The following are supported: Shared Desktop Published Desktop Published Application (supported by Windows-base Thin
                                                / Fat Client) Remote Desktop App for AVD You must use the version of this app from the direct download
                                                page . The app on the Microsoft Store is not
                                            supported. Amazon WorkSpaces with WSP (DCV) A connection broker is software that creates connections to hosted
                                virtual desktops. A connection broker performs a number of tasks
                                including the following: Validating the username and providing a connection for the
                                        user. Allowing the user to connect to a specific virtual
                                        desktop. |

| VDI component | Supported platforms |
|---|---|
| Microsoft Windows-based thin client hardware | Supported Hardware 2 GB installed RAM 128 MB physical memory 256 MB disk space Minimum CPU Mobile AMD Sempron Processor 3600+, 2-GHz Intel
                                        Core 2 CPU, or T7400 2.16 GHz DirectX 11-compatible GPU USB 2.0 ports for camera and audio devices If you want users to use virtual backgrounds, you must meet the virtual background requirements .
                                        (Webex App for VDI has the same requirements as the Windows standalone
                                    app.) Supported Software We support 64-bit architectures for the following Windows versions: Microsoft Windows 10 Microsoft Windows 11 (for VDI plugin 41.12 and later) |
| Windows Embedded Standard-based thin client hardware | Supported Hardware Installed RAM 2 GB Free Physical Memory 128 MB Free Disk Space 256 MB CPU performance affects the maximum video resolution. With Windows
                                Embedded Standard thin clients, the expected resolution depends on
                                the CPU: Up to 720p with quad-core AMD GX-420CA SOC 2 GHz or
                                        similar Up to 240p with dual-core AMD G-T56N 1.65 GHz or similar Audio-only support with dual-core VIA Eden X2 U4200 1 GHz or
                                        similar CPU These hardware specifications are only guidelines for the
                                    expected resolutions. Other factors can affect video
                                    resolution. DirectX 11 compatible GPU USB 2.0 for USB camera and audio devices Supported Software Windows 10 IoT |
| Citrix Workspace app or VMware Horizon client | Citrix Receiver 4.9 and later Citrix Workspace app 1808 and later VMware Horizon View Client version 5.x VMWare Horizon client version 8.x (2103) is supported from
                                        the Webex VDI plugin version 41.4 onward. VMware Horizon client version 8.x (2106) for Webex VDI plugin
                                        version 41.8 onward. Amazon WorkSpaces 5.15 and later Omnissa Horizon Client (formerly VMware Horizon) is supported
                                        from the Webex App and VDI plugins version 45.2 onward. Windows App for AVD is supported from the Webex App and VDI
                                        plugins version 45.4 onward. |

| VDI component | Supported platforms |
|---|---|
| Thin Client OS | Ubuntu (64-bit) 16.04 18.04 20.04 22.04 24.04 |
| Unicon eLux (64-bit) 6.5.2000 (End of life) 6.9 (End of life) RP6 2104 LTSR (Webex VDI plugin 41.8 and later) RP6 2302 LTSR (Webex VDI plugin 43.4 and later) RP6 2302 LTSR CU 1 (Webex VDI plugin 43.8 and later) RP6 2302 LTSR CU 2 (Webex VDI plugin 43.12 and later) RP7 2409 LTSR (Webex VDI plugin 44.12 and later) |
| HP ThinPro 7.1 (End of life) HP ThinPro 8.0, 8.1 (64-bit) SP 13.5 and later for Webex app plugin release 41.1 and
                                        later SP 3.4-12.7 for Webex app plugin release that are earlier
                                        than 41.1 |
| IGEL OS 11.04.100 and later 12 (Webex VDI plugin 43.10 and later) The Webex VDI plugin is packaged with IGEL OS. Because of this
                                    third-party integration, you must contact IGEL for technical
                                    support. For more information, see the IGEL OS documentation for your supported release; the Component Versions section of their release notes mentions the version of the Webex
                                    VDI plugin that's integrated and supported. See the software download page to get a copy of the OS installation package. |
| Dell Wyse ThinOS ThinOS 9.4 9.4 ( Release Notes ) Specific versions of the Webex VDI plugin are supported with Dell
                                    Wyse ThinOS. Because of this third-party integration, you must
                                    contact Dell for technical support. For more information, see
                                    the Dell Wyse ThinOS
                                        documentation for your supported release; the Supported packages section of their release notes
                                    mentions the version of the Webex VDI plugin that's supported.
                                    See the software download page to get a copy of the OS installation package. |
| 10ZiG Zero Client Thin Clients Specific versions of the Webex VDI plugin are supported with
                                    10ZiG zero client thin clients. Because of this third-party
                                    integration, you must contact 10ZiG for technical support. For
                                    more information, see the 10ZiG page for your
                                    specific thin client. |
| Stratodesk NoTouch OS Specific versions of the Webex VDI plugin are supported with
                                    Stratodesk NoTouch OS. Because of this third-party integration,
                                    you must contact Stratodesk for technical support. For more
                                    information, see the Stratodesk NoTouch OS documentation for your supported release. |
| Ubuntu/Thinpro Thin Clients Hardware | The minimum hardware requirements for thin clients are as
                                follows: CPU: Any 64-bit x86 CPU. Memory: 2GB of memory, with at least 1GB free for operating
                                        system use. Storage: 2GB or more of internal storage for
                                        installation. Graphics: Intel, ATI/AMD, or Nvidia. If the graphics card is
                                        not recognized, limited-performance VESA mode can be
                                        used. Audio: Audio support is optional. Networking: A recognized wired or wireless network
                                        adapter. USB: HP recommends 2.0 or 3.0 or USB-C high-performance flash
                                        drives If you want users to use virtual backgrounds, you must meet the virtual background
                                        requirements . (Webex App for VDI has the same requirements as the Windows standalone
                                    app.) |
| eLux RP 6 Thin Clients Hardware | Minimum hardware requirements The following system properties enable using basic eLux RP 6
                                features. Processor: x86, 1 GHz (2 CPUs), 64-bit-capable RAM: 2 GB HDD: 2 GB GPU: AMD or Intel graphics chipset I/O ports: USB 2.0 If you want users to use virtual backgrounds, you must meet the virtual background requirements .
                                        (Webex App for VDI has the same requirements as the Windows standalone
                                    app.) |
| Tested and Recommended Devices | HP T640 HP T740 HP mt32 HP mt45 HP mt46 HP t730 Dell Optiplex 7060 Lenovo ThinkCentre M710q Dell 3040*—eLux 6.5 Dell 5060*—eLux 6.5 Dell 5070*—eLux 6.5 Dell Z50Q*—eLux 6.5 HP T430*—Thinpro 7.1 / eLux 6.5 HP T520*—Thinpro 7.1 / eLux 6.5 HP T530*—Thinpro 7.1 / eLux 6.5 HP T630*—Thinpro 7.1 / eLux 6.5 HP mt21*—Thinpro 7.1 / eLux 6.5 * Based on hardware requirements, HP thin clients models t640, t540,
                                and t630 do not support virtual backgrounds at all. See virtual background requirements for more
                                information. (Webex App for VDI has the same requirements as the Windows standalone app.) |
| Citrix Workspace app or VMware Horizon client | Citrix Receiver 4.9 and later Citrix Workspace app 1808 and later VMware Horizon View Client versions 5.x VMWare Horizon client version 8.x (2103) for Webex VDI plugin
                                        version 41.4 onward. VMware Horizon client version 8.x (2106) for Webex VDI plugin
                                        version 41.8 onward. |

| VDI component | Supported platforms |
|---|---|
| MacOS-based thin client hardware | Supported hardware Minimum CPU: Apple M2 chip or Intel Core 2 Duo processor 2 GB installed RAM 1 GB physical memory 300 MB disk space USB 2.0 ports for camera and audio devices Intel Core 2 Duo or later processors on any of the following
                                    Apple hardware: iMac Pro MacBook Pro MacBook MacBook Air iMac Mac Mini If you want users to use virtual backgrounds, you must meet
                                        the virtual background
                                            requirements . (Webex App for VDI has the same requirements as the Windows
                                        standalone app.) Supported software The Webex App VDI plugin is supported on the following macOS versions: Sequoia (15.x) for VDI plugin release 44.10 and later Sonoma (14.x) for VDI plugin release 43.10 and later Ventura (13.x) for VDI plugin release 42.12 and later Monterey (12.x) for VDI plugin release 41.12 and later |
| Citrix Workspace app or VMware Horizon client | From version 42.10 onwards, Webex App VDI plugin supports both Citrix Workspace App and VMware Horizon Client for macOS - Native support for Mac with Apple Silicon (M1 Series). Citrix Workspace app 2008 and later For macOS, currently only the Webex App VDI plugin
                                                41.12 works with Citrix Workspace App 2111 for
                                                Mac. The macOS plugin does not work with Citrix Workspace
                                                App 21.08 or 21.08.1. VMware Horizon View Client version 7 (5.x) and 8 For installing or upgrading VMware Horizon Client, we
                                                recommend that you launch the client once before
                                                deploying the Webex App VDI plugin (up to version 41.12). See Loading 3rd Party
                                                  Mac plugins with Session Enhancement SDK for more information. Amazon WorkSpaces 5.17 and later |