---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-a26fa92ec1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_appendix_b_.html
retrieved_at: 2026-08-21T02:49:48.016741+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Appendix B: Integrating Cisco Unified Communications Manager and Cisco Unified SRST to Use Cisco Unified SRST as a Multicast MOH Resource

## Chapter: Appendix B: Integrating Cisco Unified Communications Manager and Cisco Unified SRST to Use Cisco Unified SRST as a Multicast MOH Resource

# Appendix B: Integrating Cisco Unified Communications Manager and Cisco Unified SRST to Use Cisco Unified SRST as a Multicast
                     MOH Resource

This chapter describes how to configure Cisco Unified CM and Cisco Unified SRST to allow Cisco Unified CM to use Cisco Unified
                        SRST gateways as multicast music-on-hold (MOH) resources during fallback and normal Cisco Unified CM operation. A distributed
                        MOH design with local gateways providing MOH eliminates the need to stream MOH across a WAN and saves bandwidth.

## Prerequisites for Using Cisco Unified SRST Gateways as a Multicast MOH Resource

Multicast MOH for H.323 and MGCP is supported on Cisco Unified CM 3.1.1 and higher versions.

Cisco Unified CM must be configured as follows:

With multicast MOH enabled.

With Media Resource Groups (MRGs) and Media Resource Group Lists (MRGLs) controlling which devices receive multicast MOH and
                                       which devices receive unicast MOH.

With Cisco Unified CM regions assigned so that G.711 is used whenever a Cisco Unified SRST multicast MOH resource is invoked.

The Cisco Unified SRST gateways must run on Cisco Unified SRST 3.0 on Cisco IOS Release 12.2(15)ZJ2 or a later release.

Cisco Unified SRST must be registered to Cisco Unified CM using protocol such as H.323, MGCP, or SIP.

For branches that do not run Cisco Unified SRST, Cisco Unified CM multicast MOH packets must cross the WAN. To accomplish
                                 this, you must have multicast routing enabled in your network. For more information about multicast routing, see the “IP Multicast”
                                 section of Cisco IOS IP Configuration Guide, Release 12.4T .

With Cisco IOS earlier than 12.3(14)T, configure Cisco Unified SRST as your MGCP gateway’s fallback mode using the ccm-manager fallback-mgcp and call application alternate commands. With Cisco IOS releases after 12.3(14)T, the ccm-manager fallback-mgcp and service commands must be configured. Configuring these two commands allows Cisco Unified SRST to assume control over the voice port
                                 and over call processing on the MGCP gateway. A complete configuration describing setting up Cisco Unified SRST as your fallback
                                 mode is shown in Cisco Unified Communications Manager Administration Guide, Release 5.1(3) Survivable Remote Site Telephony Configuration .

## Restrictions for Using Cisco Unified SRST Gateways as a Multicast MOH Resource

Cisco Unified SRST multicast MOH does not support unicast MOH.

Only a single Cisco Unified CM audio source can be used throughout the network. However, the audio files on each Cisco Unified
                                 SRST gateway’s flash memory can be different.

Cisco Unified SRST multicast MOH supports G.711 only.

Unified SRST multicast MOH does not support co-location of tunnels on the same device.

Multicast MOH support for H.323 is unavailable in all versions of Cisco Unified Communications Manager 3.3.2. For more information,
                                 see CSCdz00697 using the Bug Toolkit .

In the Cisco IOS Release 12.2(15)ZJ image for Cisco 1700 series gateways, Cisco Unified SRST multicast MOH does not include
                                 support for H.323 mode.

## Information About Using Cisco Unified SRST Gateways as a Multicast MOH Resource

To configure Cisco Unified SRST gateways as an MOH resource, you should understand the following concepts:

### Cisco Unified SRST Gateways and Cisco Unified Communications Manager

Cisco Unified SRST gateways can be configured to multicast Real-Time Transport Protocol (RTP) packets from flash memory during
                              fallback and normal Cisco Unified CM operation. To make this happen, Cisco Unified Communications Manager must be configured
                              for multicast MOH so that the audio packets do not cross the WAN. Instead, audio packets are broadcast from the flash memory
                              of Cisco Unified SRST gateways to the same multicast MOH IP address and port number configured for Cisco Unified Communications
                              Manager multicast MOH. IP phones at remote sites are able to pick up RTP packets that are multicast from the local branch
                              gateways instead of from the central Cisco Unified CM.

Multicast MOH for PSTN callers is supported when the Cisco Unified SRST router is used as the Cisco IOS voice gateway for
                              Cisco Unified CM. In this state the Cisco Unified SRST function of the router remains in standby mode (no phones registered)
                              with call control of the phones and gateway provided by Cisco Unified Communications Manager. This feature does not apply
                              when the Cisco Unified SRST router is in fallback mode (phones are registered to Cisco Unified SRST). Instead, MOH is provided
                              to PSTN callers via a direct internal path rather than through the multicast loopback interface.

The following figure shows a sample configuration in which all phones are configured by Cisco Unified Communications Manager
                              to receive multicast MOH through port number 16384 and IP address 239.1.1.1. Cisco Unified CM is configured so that multicast
                              MOH cannot reach the WAN, and local Cisco Unified SRST gateways are configured to send audio packets from their flash files
                              to port number 16384 and IP address 239.1.1.1. Cisco Unified CM and the IP phones are spoofed and behave as if Cisco Unified
                              CM were originating the multicast MOH.

Phone users at the central site would use multicast MOH from the central site.

### Codecs, Port Numbers, and IP Addresses

Cisco Unified SRST multicast MOH supports G.711 only. shows an example in which G.711 is the only codec used by a central
                              Cisco Unified CM and three branches. In some cases, a Cisco Unified CM system may use additional codecs. For example, for
                              bandwidth savings, Cisco Unified CM may use G.711 for multicast MOH and G.729 for phone conversations.

As shown in the example in, IP address 10.1.1.1 and port 1000 are used during phone conversations when G.729 is in use, and
                              IP address 239.1.1.1 and port 16384 are used when a call is placed on hold and G.711 is in use.

The figure 1 and figure 2 shows all branches using Cisco Unified SRST multicasting MOH.The figure 3 shows a case in which
                              some gateways are configured with Cisco Unified SRST and other gateways are not. When the central site and Branch 3 phone
                              users are put on hold by other IP phones in the Cisco Unified CM system, MOH is originated by Cisco Unified CM. When Branch
                              1 and Branch 2 phone users are put on hold by other phone users in the Cisco Unified CM system, MOH is originated by the Cisco
                              Unified SRST gateways.

To enable MOH audio packet transmission through two paths, the Cisco Unified CM MOH server must be configured with either
                              one IP address and two different port numbers or one port address and two different IP multicast addresses so that one set
                              of branches can use Cisco Unified SRST multicast MOH and the other can use Cisco Unified CM multicast MOH.

### Multicast MOH Transmission

If Cisco Unified SRST multicast MOH is supported by all branches in a system, such as in the figure 1, Cisco Unified Communications
                              Manager must be configured to keep all multicast MOH audio packets from reaching the WAN. When there is a mix of Cisco Unified
                              SRST branches, as shown in the figure 3, one set of Cisco Unified Communications Manager MOH audio files must reach the WAN
                              and another set must not. Audio packets from the central Cisco Unified Communications Manager must cross the WAN to reach
                              branches running Cisco Unified Communications Manager. For branches running Cisco Unified SRST, the packets must not reach
                              the WAN. For more information about Multicast MOH, see the Configuring Cisco Unified SRST for Multicast MOH from an Audio File section.

### MOH from a Live Feed

MOH live feed is an SRST feature that provides MOH streams to IP phones from an audio device connected to a local E&M (ISR
                              G2) or FXO (ISR G2/G3) port, or from a remote gateway. Live audio is fed continuously from a fixed source to the MOH playout
                              buffer instead of being read from a flash file.

Live feed audio can also be streamed via multicast to compatible devices. For more information, see Configuring Cisco Unified SRST for MOH from a Live Feed section.

### MOH from Flash Files

The MOH Multicast from Flash Files feature facilitates the continuous multicast of MOH audio feed from files in the flash
                              memories of Cisco Unified SRST branch office routers during Cisco Unified Communications fallback and normal Cisco Unified
                              Communications service. Multicasting MOH from individual branch routers saves WAN bandwidth by eliminating the need to stream
                              MOH audio from central offices to remote branches.

The MOH Multicast from Flash Files feature can act as a backup mechanism to the MOH live feed feature. Using the Flash to
                              backup the live-feed is the recommend method rather than using just the live feed feature alone.

Cisco Unified Communications Manager MOH audio files must reach the WAN and another set must not. Audio packets from the central
                              Cisco Unified CM must cross the WAN to reach branches running Cisco Unified CM. For branches running Cisco Unified SRST, the
                              packets must not reach the WAN.

The following table provides a summary of options for MOH.

Audio Source

Description

How to Configure

Flash memory

No external audio input is required.

Configuring Cisco Unified SRST for Multicast MOH from an Audio File

Live feed

The multicast audio stream has minimal delay for local IP phones. The MOH stream for PSTN callers is delayed by a few seconds.
                                          If the live feed audio input fails, callers on hold hear silence.

Configuring Cisco Unified SRST for MOH from a Live Feed

Live feed and flash memory

The live feed stream has a few seconds of delay for both PSTN and local IP phone callers. The flash MOH acts as backup for
                                          the live-feed MoH.

We recommend this option if you want live-feed because it provides guaranteed MOH if the live-feed input is not found or fails.

Configuring Cisco Unified SRST for Multicast MOH from an Audio File

and

Configuring Cisco Unified SRST for MOH from a Live Feed

## How to Use Cisco Unified SRST Gateways as a Multicast MOH Resource

For Cisco Unified CM 8.0 or later, see the Configuring MOH-groups for Cisco Unified SRST (fallback) section in the Cisco Unified Survivable Remote Site Telephony 8.0 Music On Hold Enhancement document.

To use Cisco Unified SRST gateways as a multicast MOH resource, perform the following tasks:

### Configuring Cisco Unified Communications Manager for Cisco Unified SRST Multicast MOH

The following sections describe the Cisco Unified CM configuration tasks for Cisco Unified SRST multicast MOH:

To use Cisco Unified SRST gateways as multicast MOH resources, you must configure Cisco Unified Communications Manager to
                              multicast MOH to the required branch sites. To accomplish this, you must configure IP addresses, port numbers, the MOH source,
                              and the MOH audio server.

Even though the MOH routing is set up to prevent the Cisco Unified CM-sourced multicast MOH from actually reaching the WAN
                              and the remote phones, the configured Cisco Unified CM MOH IP port and address information are still used by Cisco Unified
                              CM to tell the phones which multicast IP address to listen to for MOH (for the MOH sourced by SRST).

Configuring the MOH server involves designating a maximum number of hops for the audio source. A configuration of one hop
                              keeps Cisco Unified CM multicast MOH packets from reaching the WAN, thus spoofing Cisco Unified CM and allowing Cisco Unified SRST
                              multicast MOH packets to be sent from Cisco Unified SRST gateways to their component phones. For cases in which Cisco Unified
                              CM multicast must reach gateways that do not run Cisco Unified SRST, use the Cisco IOS ip multicast boundary command to control where multicast packets go.

After the MOH server is configured, the MOH server must be added to a Media Resource Group (MRG); the MRG is added to a Media
                              Resource Group List (MRGL); and the designated Cisco Unified CM branch gateways are configured to use the MRGL.

Five Cisco Unified CM windows are used to configure the MOH server, audio source, MRG, MRGL, and individual gateways. The
                              figure 4 provides an overview of this process.

The last Cisco Unified CM configuration task involves creating an MOH region that assigns MOH G.711 codec usage for the central
                              site or sites and branch office or offices.

Regions specify the codecs that are used for audio and video calls within a region and between existing regions. For information
                              about regions, see the “Region Configuration” section in the Cisco Unified Communications Manager Administration Guide . From the Cisco Unified Communications Manager documentation directory, click Maintain and Operate Guides and select the required Cisco Unified Communications Manager version to locate the administration guide for your version.

#### Configuring the MOH Audio Source to Enable Multicasting

The MOH audio source is a file from which Cisco Unified CM transmits RTP packets. You can create an audio file or use the
                                    default audio file. For Cisco Unified SRST multicast MOH, only one audio source can be used, even if, for example, one out
                                    of 500 sites uses Cisco Unified SRST multicast MOH. In addition, all Cisco Unified Communications Manager systems must use
                                    the same audio source for user and network MOH because Cisco Unified SRST multicast MOH can stream audio only to a single
                                    multicast IP address and port. For Cisco Unified SRST multicast MOH, the Cisco Unified Communications Manager audio source
                                    file must be configured for G.711 bandwidth.

Tip

The simplest way to create an audio source is to use the default audio source.

Whether you use a default Cisco Unified CM MOH audio source or you create one, the MOH audio source must be configured for
                                    multicasting in the MOH Audio Source Configuration window.

Note that the MOH Audio Source File Status section shows that the MOH audio source file is configured for four codec formats.
                                    If you are planning to use several codecs, ensure that the audio source file accommodates them.

For further information about the creation of an MOH audio source, see the Cisco Unified Communications Manager Administration Guide. From the Cisco Unified Communications Manager documentation directory, click Maintain and Operate Guides and select the required Cisco Unified CM version.

Use this procedure to configure the MOH audio source to enable multicasting and continuous play.

These instructions assume that an MOH audio source file was already created.

### SUMMARY STEPS

- To enable multicast MOH for the MOH audio source, choose Service > Media Resources > Music On Hold Audio Source to display the MOH Audio Source Configuration window.

- Double-click the required audio source listed in the MOH Audio Sources column.

- In the MOH Audio Source Configuration window, check Allow Multicasting .

- Click Update .

### DETAILED STEPS

Step 1

To enable multicast MOH for the MOH audio source, choose Service > Media Resources > Music On Hold Audio Source to display the MOH Audio Source Configuration window.

Step 2

Double-click the required audio source listed in the MOH Audio Sources column.

Step 3

In the MOH Audio Source Configuration window, check Allow Multicasting .

Step 4

Click Update .

#### Enabling Multicast on the Cisco Unified Communications Manager MOH Server and Configuring Port Numbers and IP Addresses

Enter a base multicast IP address and port number in the Multicast Audio Source Information section of the MOH Server Configuration
                                    window. If you are using Cisco Unified CM multicast MOH and Cisco Unified SRST multicast MOH (see the Codecs, Port Numbers, and IP Addresses section and the Multicast MOH Transmission section), you must select a port and IP address increment method to configure for two sets of port numbers and IP address.

If the Increment Multicast on radio button is set to IP address, each MOH audio source and codec combination is multicast
                                    to different IP addresses but uses the same port number. If it is set to Port Number, each MOH audio source and codec combination
                                    is multicast to the same IP address but uses different destination port numbers.

Table 2 shows the difference between incrementing on an IP address and incrementing on a port number, using the base IP address
                                    of 239.1.1.1 and the base port number of 16384. The table also matches Cisco Unified Communications Manager audio sources
                                    and codecs to IP addresses and port numbers.

Audio Source

Codec

Increment Multicast on IP Address

Increment Multicast on Port Number

Destination IP Address

Destination Port

Destination IP Address

Destination Port

1

G.711 mu-law

239.1.1.1

16384

239.1.1.1

16384

1

G.711 a-law

239.1.1.2

16384

239.1.1.1

16386

1

G.729

239.1.1.3

16384

239.1.1.1

16388

1

Wideband

239.1.1.4

16384

239.1.1.1

16390

2

G.711 mu-law

239.1.1.5

16384

239.1.1.1

16392

2

G.711 a-law

239.1.1.6

16384

239.1.1.1

16394

2

G.729

239.1.1.7

16384

239.1.1.1

16396

2

239.1.1.8

16384

239.1.1.1

16398

The lower destination port 16384 is assigned to the first multicast-enabled audio source ID, and the subsequent ports will
                                                be assigned to the subsequent multicast-enabled audio sources.

Incrementation is triggered by a change in codec usage. When codec usage changes, a new IP address or port number (depending
                                    on the incrementation selected) is assigned to the new codec type and is put intouse. The original codec keeps its IP address
                                    and port number. For example, as seen in Table 2, if your baseline IP address and port number are 239.1.1.1 and 16384 for
                                    a G.711 mu-law codec and the codec usage changes to G.729 (triggering an increment on the port number), the IP address and
                                    port number in use changes, or increment, to 239.1.1.1 and 16386. If G.711 usage resumes, the IP address and port number returns
                                    to 239.1.1.1 and 16384. If G.729 is in use again, the IP address and port goes back to 239.1.1.1 and 16386, and so forth.

It is important to configure a Cisco Unified CM port number and IP address that use a G.711 audio source for Cisco Unified
                                    SRST multicast MOH. If Cisco Unified CM multicast MOH is also being used on gateways that do not have Cisco Unified SRST and
                                    use a different codec, such as G.729, ensure that the additional or incremental port number or IP address uses the same audio
                                    source as the Cisco Unified SRST gateways and the required codec.

The MOH Server Configuration window is also where the multicast audio source for the MOH server is configured. For Cisco Unified
                                    SRST multicast MOH, the Cisco Unified CM MOH server can use only one audio source. An audio source is selected by inputting
                                    the audio source’s maximum number of hops.

The Max Hops configuration sets the length of the transmission of the audio source packets. Limiting the number of hops is
                                    one way to stop audio packets from reaching the WAN and thus spoofing Cisco Unified Communications Manager so Cisco Unified
                                    SRST can multicast MOH. If all of your branches run Cisco Unified SRST, use a low number of hops to prevent audio source packets
                                    from crossing the WAN. If your system configuration includes routers that do not run Cisco Unified SRST, enter a high number
                                    of hops to allow source packets to cross the WAN. Use the ip multicast bounder and access-list commands to keep resource packets
                                    from specific IP addresses from reaching the WAN.

Use this procedure to enable multicast and configure port numbers and IP addresses.

### SUMMARY STEPS

- Enable multicast MOH for Cisco Unified CM

- Set the base IP address and port number.

- Select whether Cisco Unified CM increments port numbers or IP addresses.

- Enter a maximum number of hops.

- Use Cisco IOS commands to stop Cisco Unified CM signals from crossing the WAN and reaching Cisco Unified SRST gateways.

### DETAILED STEPS

Step 1

Enable multicast MOH for Cisco Unified CM

Step 2

Set the base IP address and port number.

In the MOH Server Configuration window, enter an IP address in the Base Multicast IP Address field and enter a port number
                                                in the Base Multicast Port Number field. Ensure that the IP address and port number use the required audio source and codec.
                                                See Table 2.

Step 3

Select whether Cisco Unified CM increments port numbers or IP addresses.

In the MOH Server Configuration window, in the Increment Multicast on field, choose Port Number if you want port numbers to
                                                be incremented and the IP address to remain unchanged. Choose IP Address if you want IP addresses to be incremented and the
                                                port number to remain unchanged.

If all of your branches run Cisco Unified SRST and thus use G.711 for MOH, use either settingbecause incrementation does not
                                                      take place and a selection does not matter.

If your system configuration includes routers that do not run Cisco Unified SRST and use a different codec, select an incrementation
                                                      method.

If your branches include routers that do not run Cisco Unified SRST and do use G.711, configure separate audio sources: one
                                                            for the routers that run Cisco Unified SRST and one for the routers that do not.

Step 4

Enter a maximum number of hops.

In the MOH Server Configuration window, next to the Audio Source Name field, enter 1 in the Max Hops field if all of your
                                                branches run Cisco Unified SRST. If your system configuration includes routers that do not run Cisco Unified SRST, enter 16
                                                in the Max Hops field.

Step 5

Use Cisco IOS commands to stop Cisco Unified CM signals from crossing the WAN and reaching Cisco Unified SRST gateways.

If all of your branches run Cisco Unified SRST, skip this step. If your system configuration includes routers that do not
                                                run Cisco Unified SRST and use a different codec, enter the following Cisco IOS commands starting from global configuration
                                                mode on the central site router:

#### Creating an MRG and an MRGL, Enabling MOH Multicast, and Configuring Gateways

The next task involves configuring individual gateways to use an MOH server that can transport the required MOH audio source
                                    to their IP phones on hold. This is accomplished by creating a Media Resource Group (MRG). An MRG references media resources,
                                    such as MOH servers. The MRG is then added to a Media Resource Group List (MRGL), and the MRGL is added to the phone and gateway
                                    configurations.

MRGs are created in the Media Resource Group Configuration window. MRGLs are created in the Media Resource Group List Configuration
                                    window. Phones are configured in the Phone Configuration window. Gateways are configured in the Gateway Configuration window.

The Gateway Configuration window for an H.323 gateway is similar for MGCP gateways.

Add MRGL to a gateway or IP phone configuration by adding the MRGL to a device pool configuration. For further information
                                    about device pools, see Cisco Unified Communications Manager Administration Guide. From the Cisco Unified Communications Manager documentation directory, click Maintain and Operate Guides and select the required Cisco Unified CM version.

Use the following procedure to create an MRG and MRGL, to enable MOH multicast, and to configure gateways.

### SUMMARY STEPS

- Create an MRG with a multicast MOH media resource.

- Create an MRGL that contains the newly created MRG.

- Add the MRGL to the required IP phones.

- Add the MRGL to the required gateway.

### DETAILED STEPS

Step 1

Create an MRG with a multicast MOH media resource.

Step 2

Create an MRGL that contains the newly created MRG.

Step 3

Add the MRGL to the required IP phones.

Step 4

Add the MRGL to the required gateway.

#### Creating a Region for the MOH Server

To ensure that the MOH server uses G.711 for Cisco Unified SRST gateways, you must create a separate region for the MOH server.
                                    For more information about codecs, see the Codecs, Port Numbers, and IP Addresses section. For information about regions, see Cisco Unified Communications Manager Administration Guide . From the Cisco Unified Communications Manager documentation directory, click Maintain and Operate Guides and select the required Cisco Unified Communications Manager version.

Configure the Region Configuration window. If the Cisco Unified CM system uses G.711 only, all of the central sites and their
                                    constituent branches for the MOH region must be set to G.711. If a Cisco Unified CM system has a combination of branches that
                                    do and do not run Cisco Unified SRST multicast MOH and the branches that do not run Cisco Unified SRST require a different
                                    codec for Cisco Unified Communications Manager multicast MOH, they must be configured accordingly.

A Region Configuration window where the “MOH Server” region is configured to use the G.711 and G.729 codecs might look like
                                    this:

G.711 is used for Branch 1 because its gateway is configured to run Cisco Unified SRST multicast MOH, which requires G.711.

G.729 is used for Branch 2 because its gateway doe not run Cisco Unified SRST and it is configured to use a port and IP address
                                          that use G.729.

G.711 is configured for the central site and the MOH server region.

Use the following procedure to create a region for the MOH server.

### SUMMARY STEPS

- Create an MOH server region.

- Create other regions as needed for different codecs.

### DETAILED STEPS

Step 1

Create an MOH server region.

Step 2

Create other regions as needed for different codecs.

#### Verifying Cisco Unified Communications Manager Multicast MOH

The Cisco Unified CM multicast MOH configuration must run correctly for Cisco Unified SRST multicast MOH to work. Verification
                                    of Cisco Unified Communications Manager multicast MOH differs for configurations using a WAN with multicast enabled and a
                                    WAN with multicast disabled.

You must verify that the Cisco Unified CM multicast MOH is provided through multicasting and not unicasting. Because unicast
                                    MOH is enabled by default, it is easy to mistakenly conclude that multicast MOH is working when it is not.

### SUMMARY STEPS

- Verify that Cisco Unified CM system’s multicast MOH is heard on a remote gateway.

- Verify that the Cisco Unified CM system’s MOH is multicast, not unicast.

### DETAILED STEPS

Step 1

Verify that Cisco Unified CM system’s multicast MOH is heard on a remote gateway.

Step 2

Verify that the Cisco Unified CM system’s MOH is multicast, not unicast.

### Configuring Cisco Unified SRST for Multicast MOH from an Audio File

Use the steps in this section only when you are using Microsoft Windows to run Cisco Unified Communications Manager version
                                          4.3 or below. Use the RTMT (Real-Time Monitoring Tool) in Cisco Unified Communications Manager version 5.0 and later versions
                                          on the Linux operating system to monitor MOH activity in Cisco Unified CM version. See Cisco Unified Communications Serviceability System Guide, Release 4.0(1) for more information about RTMT.

Use the following procedures to configure Cisco Unified SRST for multicast MOH from an audio file.

#### Prerequisites

The Cisco Unified SRST gateways must run Cisco IOS Release 12.2(15)ZJ2 or a later release.

The flash memory in each of the Cisco Unified SRST gateways must have an MOH audio file. The MOH file can be in .wav or .au
                                       file format, but must contain 8-bit 8-kHz data, such as an a-law or mu-law data format. A known working MOH audio file (music-on-hold.au)
                                       is included in the program .zip files that can be downloaded from http://www.cisco.com/cgi-bin/tablebuild.pl/ip-key . Or the music-on-hold.au file can be downloaded from http://www.cisco.com/cgi-bin/tablebuild.pl/ip-iostsp and copied to the flash memory on your Cisco Unified SRST router.

The MOH file packaged with the SRST software is completely royalty free.

For Cisco Unified CM versions 4.3 or earlier versions running on Windows, download MOH files by copying one of the MOH files,
                                       such as SampleAudioSource.ULAW.wav, from C:\Program Files\Cisco\MOH on Cisco Unified CM.

During the copying process, four files are added to each router’s flash automatically. One of the files must use a mu-law
                                             format as indicated by the extension.ULAW.wav.

You must configure a loopback interface and include its IP addresses in the Cisco Unified SRST multicast MOH configuration.
                                       This configuration allows multicast MOH to be heard on POTS ports on the gateway. The loopback interface does not have to
                                       bind to either H.323 or MGCP.

Configure at least one ephone and directory number (DN), even if the gateway is not used for Cisco Unified SRST. Cisco Unified
                                       SRST multicast MOH streaming never starts without an ephone and directory number.

#### Enabling Multicast MOH on the Cisco Unified SRST Gateway

No multicast MOH routing configuration is required for Cisco Unified SRST gateways because each Cisco Unified SRST gateway
                                    is configured to act as a host running an application that streams multicast MOH packets from the network. The multicast moh
                                    command declares the Cisco Unified Communications Manager multicast MOH address and port number and allows Cisco Unified SRST
                                    gateways to route MOH from flash memory to up to four IP addresses. If no route IP addresses are configured, the flash MOH
                                    is sent through the IP address configured in the Cisco Unified SRST ip source-address command.

### SUMMARY STEPS

- ccm-manager music-on-hold

- interface loopback number

- ip address ip-address mask

- exit

- interface fastethernet slot/port

- ip address ip-address mask

- exit

- call-manager-fallback

- ip source-address ip-address [ port port

- max-ephones max-phones

- max-dn max-directory-number

- moh filename

- multicasting-enabled

- multicast moh multicast-address port port [ route ip-address-list ]

- exit

### DETAILED STEPS

Step 1

ccm-manager music-on-hold

##### Example:

```
Router(config)# ccm-manager music-on-hold
```

Enables the multicast MOH feature on a voice gateway.

Step 2

interface loopback number

##### Example:

```
Router(config)# interface loopback 1
```

Configures an interface type and enters theinterface configuration mode.

number —Loopback interface number. The range is from 0 to 2147483647.

Step 3

ip address ip-address mask

##### Example:

```
Router(config-if)# ip address 10.1.1.1 255.255.255.255
```

Sets a primary IP address for an interface.

ip-address —IP address.

mask —Mask for the associated IP subnet.

Step 4

exit

##### Example:

```
Router(config-if)# exit
```

Exits interface configuration mode.

Step 5

interface fastethernet slot/port

##### Example:

```
Router(config)# interface fastethernet 0/0
```

(Optional if the route keyword is not used in the multicast moh command. See Step 9 and Step 13.) Configures an interface type and enters interface configuration mode.

Step 6

ip address ip-address mask

##### Example:

```
Router(config-if)# ip-address 172.21.51.143
255.255.255.192
```

(Optional if the route keyword is not used in the multicast moh command. See Step 9 and Step 13.) Sets a primary IP address for an interface.

Step 7

exit

##### Example:

```
Router(config-if)# exit
```

(Optional if the route keyword is not used in the multicast moh command. See Step 9 and Step 13.) Exits interface configuration mode.

Step 8

call-manager-fallback

##### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 9

ip source-address ip-address [ port port

##### Example:

```
Router(config-cm-fallback)# ip source-address
172.21.51.143 port 2000
```

(Optional if the route keyword is not used in the multicast moh command. See Step 13.) Enables a router to receive messages from Cisco Unified IP phones through the specified IP addresses
                                                and ports.

ip-address —The pre-existing router IP address, typically one of the addresses of the Ethernet port of the router.

port port —(Optional) The port to which the gateway router connects to receive messages from the Cisco Unified IP phones. The port number
                                                      range is from 2000 to 9999. The default port number is 2000.

Step 10

max-ephones max-phones

##### Example:

```
Router(config-cm-fallback)# max-ephones 1
```

Configures the maximum number of Cisco Unified IP phones that can be supported by a router.

max-phones —Maximum number of Cisco IP phones supported by the router. The maximum number is platform-dependent. The default is 0.

Step 11

max-dn max-directory-number

##### Example:

```
Router(config-cm-fallback)# max-dn 1
```

Sets the maximum possible number of virtual voice ports that can be supported by a router.

max-directory-number —Maximum number of directory numbers or virtual voice ports supported by the router. The maximum possible number is platform-dependent.
                                                The default is 0.

Step 12

moh filename

##### Example:

```
Router(config-cm-fallback)# moh music-on-hold.au
```

Enables use of an MOH file.

filename —Filename of the music file. The music file must reside in flash memory.

Step 13

multicasting-enabled

Selects the multicast-enabled MOH audio source in the User Hold MOH Audio Source field on the Phone Configuration page in
                                                Cisco Unified CM Administration GUI.

Step 14

multicast moh multicast-address port port [ route ip-address-list ]

##### Example:

```
Router(config-cm-fallback)# multicast moh 239.1.1.1
port 16386 route 239.1.1.2 239.1.1.3 239.1.1.4
239.1.1.5
```

Enables multicast of MOH from a branch office flash MOH file to IP phones in the branch office.

multicast-address port port —Declares the IP address and port number of MOH packets that are to be multicast. The multicast IP address and port must match
                                                      the IP address and the port number that Cisco Unified CM is configured to use for multicast MOH. If you are using different
                                                      codecs for MOH, these might not be the base IP address and port, instead an incremented IP address or port number. See the Configuring the MOH Audio Source to Enable Multicasting section. If you have multiple audio sources configured on Cisco Unified CM, ensure that you are using the audio sources’s
                                                      correct IP address and port number.

route —(Optional) List of explicit router interfaces for the IP multicast packets.

ip-address-list —(Optional) List of up to four explicit routes for multicast MOH. The default is that the MOH multicast stream is automatically
                                                      output on the interfaces that correspond to the address that was configured with the ip source-address command.

Step 15

exit

##### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

#### Verifying Basic Cisco Unified SRST Multicast MOH Streaming

Use the following procedure to verify that multicast MOH packets are configured with the multicast moh command.

### SUMMARY STEPS

- debug ephone moh

- show interfaces fastethernet

- show ephone summary

### DETAILED STEPS

Step 1

debug ephone moh

##### Example:

```
Router# debug ephone moh
!
MOH route If FastEthernet0/0 ETHERNET 172.21.51.143
via ARP
MOH route If Loopback0 46 172.21.51.98 via
172.21.51.98
!
```

This command sets debugging for MOH. You can use this command to show that the Cisco Unified SRST gateway is multicasting
                                                MOH out of Loopback 0 and Fast Ethernet 0/0.

Step 2

show interfaces fastethernet

##### Example:

```
Router# show interfaces fastethernet 0/0
!
30 second output rate 86000 bits/sec, 50 packets/sec
!
```

Use this command to confirm that the interface output rates match one G.711 stream, which the show interfaces fastethernet
                                                output displays as 50 packets/sec and 80 kbps or more.

Step 3

show ephone summary

##### Example:

```
Router# show ephone summary
!
File music-on-hold.au type AU
Media_Payload_G.711Ulaw64k 160 bytes
!
```

Use this command to verify that the Cisco IOS software was able to read the MOH audio file successfully.

#### Verifying Cisco Unified SRST MOH to PSTN

Use the following procedure to verify Cisco Unified CM control of MOH (the WAN link is up) and that multicast MOH packets
                                    transmit over a public switched telephone network (PSTN).

This feature does not apply when the Cisco Unified SRST router is in fallback mode.

### SUMMARY STEPS

- Verify that a PSTN caller hears MOH when placed on hold by an IP phone caller. Use a Cisco Unified SRST gateway IP phone to
                                    call a PSTN phone, and put the PSTN caller on hold. The PSTN caller should hear MOH.

- show ccm-manager music-on-hold

- debug h245 asn

- show call active voice

### DETAILED STEPS

Step 1

Verify that a PSTN caller hears MOH when placed on hold by an IP phone caller. Use a Cisco Unified SRST gateway IP phone to
                                             call a PSTN phone, and put the PSTN caller on hold. The PSTN caller should hear MOH.

Step 2

show ccm-manager music-on-hold

##### Example:

```
Router# show ccm-manager music-on-hold
Current active multicast sessions : 1
Multicast RTP port Packets   Call Codec Incoming
Address   number   in/out    id         Interface
=======================================================
239.1.1.1 16384    326/326   42         G.711ulaw Lo0
```

Use this command to verify that the MOH is multicast if you are using Windows and Cisco Unified CM version 4.3 or an earlier
                                                version.

Note that the show ccm-manager music-on-hold command displays information about PSTN connections on hold only. It does not display information about multicast streams
                                                going to IP phones on hold. The following is an example of show ccm-manager music-on-hold command output.

If the PSTN caller hears MOH, and the show ccm-manager music-on-hold command displays no active multicast streams, the MOH is unicast. Confirm this by checking the MOH performance counters as
                                                discussed in the Verifying Cisco Unified Communications Manager Multicast MOH section.

Step 3

debug h245 asn

##### Example:

```
Router# debug h245 asn
*Mar 1 04:20:19.227: H245 MSC INCOMING PDU ::=
value MultimediaSystemControlMessage ::= response :
openLogicalChannelAck :
{
forwardLogicalChannelNumber 6
forwardMultiplexAckParameters
h2250LogicalChannelAckParameters :
{
sessionID 1
mediaChannel unicastAddress : iPAddress :
{
network 'EF010101'H
tsapIdentifier 16384
}
mediaControlChannel unicastAddress : iPAddress :
{
network 'EF010101'H
tsapIdentifier 16385
}
}
}
```

Use this command if H.323 is being used and no multicast address appears in the show ccm-manager music-on-hold command output to verify the H.323 handshaking between Cisco Unified Communications Manager and the Cisco Unified SRST gateway.
                                                When a PSTN caller is placed on hold, Cisco Unified Communications Manager sends an H.245 closeLogicalChannel, followed by
                                                an openLogicalChannel. Verify that the final openLogicalChannelAck from Cisco Unified Communications Manager to the Cisco
                                                Unified SRST gateway contains the expected multicast IP address and port number. In the following example, the IP address
                                                is EF010101 (239.1.1.1) and the port number is 16384.

Step 4

show call active voice

##### Example:

```
Router# show call active voice | include RemoteMedia
RemoteMediaIPAddress=239.1.1.1
RemoteMediaPort=16384
```

Use this command with the debug h245 asn command to further verify the H.323 handshaking between Cisco Unified Communications
                                                Manager and the Cisco Unified SRST gateway.

The IP address and port number displayed must match the IP address and port number displayed by the debug h245 asn command.
                                                If the RemoteMediaIPAddress field displays 0.0.0.0, you probably have encountered caveat CSCdz00697. For more information,
                                                see the Cisco Bug ToolKit and the Restrictions for Using Cisco Unified SRST Gateways as a Multicast MOH Resource section.

#### Verifying Cisco Unified SRST Multicast MOH to IP Phones

To verify that Cisco Unified CM is signaling the IP phone to receive Cisco Unified SRST multicast MOH correctly, perform the
                                    following steps.

### SUMMARY STEPS

- Verify that an IP phone caller hears MOH when placed on hold by an IP phone caller.

- Check the MOHMulticastResourceActive and MOHUnicastResourceActive counters.

### DETAILED STEPS

Step 1

Verify that an IP phone caller hears MOH when placed on hold by an IP phone caller.

Use an IP phone to call a second IP phone, and put the second caller on hold. The second caller should hear MOH.

Step 2

Check the MOHMulticastResourceActive and MOHUnicastResourceActive counters.

Use the Performance window to check the MOHMulticastResourceActive and MOHUnicastResourceActive counters under the Cisco MOH
                                                Device performance object. See Step 2 in the Verifying Cisco Unified Communications Manager Multicast MOH section. For Cisco Unified SRST multicasting MOH to work, the multicast counter must increment.

#### Troubleshooting Tips

If no MOH is heard and the Cisco Unified SRST MOH signaling is multicasting, connect a sniffer to the PC port on the back
                                 of IP phone. If the IP phone and Cisco Unified SRST gateway are connected to the same subnet, multicast RTP packets must be
                                 detected at all times, even when the IP phone was not placed on hold. If the IP phone and the Cisco Unified SRST gateway are
                                 not connected to the same subnet, multicast RTP packets are detected only when the IP phone is placed on hold and sends an
                                 Internet Group Management Protocol (IGMP) Join to the closest router.

### Configuring Cisco Unified SRST for MOH from a Live Feed

To configure MOH from a live feed, establish a voice port and dial peer for the call and then create a “dummy” phone or directory
                              number. The dummy number allows for making and receiving calls, and the number is not assigned to a physical phone. It is
                              that number that the MOH system autodials to establish the MOH feed.

The moh-live command allocates one of the virtual voice ports from the pool of virtual voice ports created by the max-dn command. The virtual voice port places an outgoing call to the dummy number; that is, the directory number specified in the moh-live command. The audio stream obtained from the MOH call provides the music-on-hold audio stream.

We recommend that the interface for live-feed MOH is an analog E&M port because it requires the minimum number of external
                              components. Connect a line-level audio feed (standard audio jack) directly to pins 3 and 6 of an E&M RJ-45 connector. The
                              E&M WAN interface card (WIC) has a built-in audio transformer that provides appropriate electrical isolation for the external
                              audio source. (An audio connection on an E&M port does not require loop current.) The signal immediate and auto-cut-through commands disable E&M signaling on this voice port. A G.711 audio packet stream is generated by a digital signal processor
                              (DSP) on the E&M port.

In Cisco IOS Release 12.4(15)T and later releases, you can directly connect a live-feed source to an FXO port if the signal loop-start live-feed command is configured on the voice port; otherwise, the port must connect through an external third-party adapter to provide
                              a battery feed. An external adapter must supply normal telephone company (telco) battery voltage with the correct polarity
                              to the tip and ring leads of the FXO port and it must provide transformer-based isolation between the external audio source
                              and the tip and ring leads of the FXO port.

Music from a live feed is continuously fed into the MOH playout buffer instead of being read from a flash file, so there is
                              typically a 2-second delay. An outbound call to an MOH live-feed source is attempted (or reattempted) every 30 seconds until
                              the connection is made by the directory number that was configured for MOH. If the live-feed source is shut down for any reason,
                              the flash memory source automatically activates.

A live-feed MOH connection is established as an automatically connected voice call that is made by the Cisco Unified SRST
                              MOH system itself or by an external source directly calling in to the live-feed MOH port. An MOH call can be from or to the
                              PSTN or can proceed via VoIP with voice activity detection (VAD) disabled. The call is assumed to be an incoming call unless
                              the out-call keyword is used with the moh-live command during configuration.

The Cisco Unified SRST router uses the audio stream from the call as the source for the MOH stream, displacing any audio stream
                              that is available from a flash file. An example of an MOH stream received over an incoming call is an external H.323-based
                              server device that calls the directory number to deliver an audio stream to the Cisco Unified SRST router.

The following sections describe the configuration tasks for Cisco Unified SRST MOH live feed:

#### Prerequisites

Cisco Unified SRST for multicast MOH, as described in the Configuring Cisco Unified SRST for Multicast MOH from an Audio File section, is not required for the MOH live-feed configuration. However, MOH live feed is designed to work in conjunction with
                                 multicast MOH.

#### Restrictions

An FXO port can be used for a live feed if the port is supplied with an external third-party adapter to provide a battery
                                       feed.

An FXS port cannot be used for a live feed.

For a live feed from VoIP, VAD must be disabled.

MOH is supplied to PSTN and VoIP G.711 calls. Some versions of Cisco Unified SRST provide MOH to local phones. On Cisco Unified
                                       SRST that do not support MOH for local IP phones, callers hear a repeating tone on hold for reassurance that they are still
                                       connected.

Conditions may occur within your network that is caused by brief spikes of a higher CPU usage. Small spikes in CPU usage can
                                       temporarily affect the quality of the MOH heard by parties connected via TDM (FXO / PRI / S) interfaces.

#### Setting Up the Voice Port on the Cisco Unified SRST Gateway

Use the following procedure to activate MOH from a live feed and to set up and connect the physical voice port.

### SUMMARY STEPS

- voice-port port

- input gain decibels

- auto-cut-through

- operation 4-wire

- signal immediate

- no shutdown

- exit

### DETAILED STEPS

Step 1

voice-port port

##### Example:

```
Router(config)# voice-port 1/1/0
```

Enters voice-port configuration mode to set up the physical voice port. To find the correct definition of the port argument
                                                for your router, see Cisco IOS Survivable Remote Site Telephony Version 3.2 Command Reference .

.

Step 2

input gain decibels

##### Example:

```
Router(config-voice-port)# input gain 0
```

Specifies, in decibels, the amount of gain to be inserted at the receiver side of the interface. Acceptable values are integers
                                                from –6 to 14.

Step 3

auto-cut-through

##### Example:

```
Router(config-voiceport)# auto-cut-through
```

(E&M ports only) Enables call completion when a PBX does not provide an M-lead response. MOH requires that you use this command
                                                with E&M ports.

Step 4

operation 4-wire

##### Example:

```
Router(config-voiceport)# operation 4-wire
```

(E&M ports only) Selects the 4-wire cabling scheme. MOH requires that you specify 4-wire operation with this command for E&M
                                                ports.

Step 5

signal immediate

##### Example:

```
Router(config-voiceport)# signal immediate
```

(E&M ports only) For E&M tie trunk interfaces, directs the calling side to seize a line by going off-hook on its E-lead and
                                                to send address information as DTMF digits.

Step 6

no shutdown

##### Example:

```
Router(config-voiceport)# no shutdown
```

Activates the voice port.

Step 7

exit

##### Example:

```
Router(config-voiceport)# exit
```

Exits voice-port configuration mode.

#### Setting Up the Directory Numbers on the Cisco Unified SRST Gateway

After setting up the voice port, create a dial peer and give the voice port a directory number with the destination-pattern command. The directory number is the number that the system uses to access the MOH.

### SUMMARY STEPS

- dial-peer voice tag pots

- destination-pattern string

- port port

- exit

### DETAILED STEPS

Step 1

dial-peer voice tag pots

##### Example:

```
Router(config)# dial-peer voice 7777 pots
```

Enters dial-peer configuration mode.

Step 2

destination-pattern string

##### Example:

```
Router(config-dial-peer)# destination-pattern
7777
```

Specifies the directory number that the system uses to create MOH. This command specifies either the prefix or the full E.164
                                                telephone number to be used for a dial peer.

Step 3

port port

##### Example:

```
Router(config-dial-peer)# port 1/1/0
```

Associates the dial peer with the voice port that was specified in the Setting Up the Voice Port on the Cisco Unified SRST Gateway section.

Step 4

exit

##### Example:

```
Router(config-dial-peer)# exit
```

Exits dial-peer configuration mode.

#### Establishing the MOH Feed

Use the following procedure to establish the MOH feed and connect the music source, such as a CD player, to autodial the directory
                                    number.

### SUMMARY STEPS

- call-manager-fallback

- max-dn max-directory-number

- multicast moh multicast-address port port [ route ip-address-list ]

- moh-live dn-number calling-number out-call outcall-number

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

##### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

max-dn max-directory-number

##### Example:

```
Router(config-cm-fallback)# max-dn 1
```

Sets the maximum possible number of virtual voice ports that can be supported by a router.

max-directory-number —Maximum number of directory numbers or virtual voice ports supported by the router. The maximum possible number is platform-dependent.
                                                      The default is 0.

Step 3

multicast moh multicast-address port port [ route ip-address-list ]

##### Example:

```
Router(config-cm-fallback)# multicast moh
239.1.1.1 port 16386 route 239.1.1.2 239.1.1.3
239.1.1.4 239.1.1.5
```

##### Example:

```
Router(config-cm-fallback)# multicast moh
```

Enables multicast of MOH from a branch office flash MOH file to IP phones in the branch office.

This command must be used to source live feed MOH to multicast Cisco Unified CM mode. It is not required in strict SRST mode.

multicast-address and port port —Declares the IP address and port number of MOH packets that are to be multicast. The multicast IP address and port must
                                                      match the IP address and the port number that Cisco Unified Communications Manager is configured to use for multicast MOH.
                                                      If you are using different codecs for MOH, these might not be the base IP address and port, but an incremented IP address
                                                      or port number. See the Configuring the MOH Audio Source to Enable Multicasting section. If you have multiple audio sources configured on Cisco Unified CM, ensure that you are using the audio sources’
                                                      correct IP address and port number.

route ip-address-list —(Optional) Declares the IP address or addresses from which the flash MOH packets can be transmitted. A maximum of four IP
                                                      address entries are allowed. If a route keyword is not configured, the Cisco Unified SRST system uses the ip source-address command value configured for Cisco Unified SRST.

Step 4

moh-live dn-number calling-number out-call outcall-number

##### Example:

```
Router(config-cm-fallback)# moh-live dn-number
3333 out-call 7777
```

Specifies that this telephone number is to be used for an outgoing call that is to be the source for an MOH stream.

dn-number calling-number — Sets the MOH telephone number. The calling-number argument is a sequence of digits that represent a telephone number.

out-call outcall-number —Indicates that the router is calling out for a live feed that is to be used for MOH and specifies the number to be called.
                                                      The outcall-number argument is a sequence of digits that represent a telephone number, typically of an E&M port.

The outcall keyword makes a connection to the local router voice port that was specified in the the Setting Up the Voice Port on the Cisco Unified SRST Gateway section.

Step 5

exit

##### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

#### Verifying Cisco Unified SRST MOH Live Feed

To verify MOH live feed, use the debug ephone moh command and the other commands described in the Verifying Basic Cisco Unified SRST Multicast MOH Streaming section.

## Configurations Examples for Cisco Unified SRST Gateways

This section provides the following configuration examples for Cisco Unified SRST gateways:

### MOH Routed to Two IP Addresses: Example

The following example declares the Cisco Unified CM multicast MOH IP address 239.1.1.1 and port number 16384 and streams music-on-hold.au
                                 audio file packets out the interfaces that are configured with the IP addresses 10.1.1.1 and 172.21.51.143:

```
ccm-manager music-on-hold
 interface Loopback0
  ip address 10.1.1.1. 255.255.255.255

interface FastEthernet0/0
 ip address 172.21.51.143 255.255.255.192

call-manager-fallback
 ip source-address 172.21.51.143 port 2000
 max-ephones 1
 max-dn 1
 moh music-on-hold.au
 multicast moh 239.1.1.1 port 16384 route 172.21.51.143 10.1.1.1
```

The multicast IP address and port must match the IP address and the port number that Cisco Unified CM is configured to use
                                             for multicast MOH. If you are using different codecs for MOH, these might not be the base IP address and port, but an incremented
                                             IP address or port number. See the the Configuring the MOH Audio Source to Enable Multicasting section. If you have multiple audio sources configured on Cisco Unified CM, ensure that you are using the audio source’s
                                             correct IP address and port number.

### MOH Live Feed: Example

The following example configures MOH from a live feed. Note that the dial peer references the E&M port that was set with the voice-port command and that the dial peer number (7777) matches the outcall number configured with the out-call keyword of the moh-live command.

```
voice-port 1/0/0
 input gain 3
 auto-cut-through
 operation 4-wire
 signal immediate
!
dial-peer voice 7777 pots
 destination-pattern 7777
 port 1/0/0
!
!
call-manager-fallback
 max-conferences 8
 max-dn 1
 moh-live dn-number 3333 out-call 7777
!
.
.
.
```

## Feature Information for Cisco Unified SRST as a Multicast MOH Resource

The Feature Information for Cisco Unified SRST as a Multicast MOH Resource table lists the enhancements to the Cisco Unified
                           SRST as a Mulitcast MOH Resource feature by version.

To determine hardware and software compatibility, see the Cisco Unified CM Compatibility Information page at the following
                           URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_device_support_tables_list.html

See also the Cisco Unified CM Documentation Roadmaps at the following URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.htm.

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator
                           enables you to determine which Cisco IOS software images support a specific software release, feature set, or platform. To
                           access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

The Feature Information for Cisco Unified SRST as a Multicast MOH Resource table lists the Cisco Unified SRST version that
                                       introduced support for a given feature. Unless noted otherwise, subsequent versions of Cisco Unified SRST software also support
                                       that feature.

Feature Name

Releases

Feature Information

Cisco Unified SRST as a Multicast MOH Resource

3.0

The MOH-live feature was added.

## Where to Go Next

For additional information, see the Related Documents and References section in the Cisco Unified SRST Feature Overview chapter.

| Note | Phone users at the central site would use multicast MOH from the central site. |
|---|---|

| Audio Source | Description | How to Configure |
|---|---|---|
| Flash memory | No external audio input is required. | Configuring Cisco Unified SRST for Multicast MOH from an Audio File |
| Live feed | The multicast audio stream has minimal delay for local IP phones. The MOH stream for PSTN callers is delayed by a few seconds.
                                          If the live feed audio input fails, callers on hold hear silence. | Configuring Cisco Unified SRST for MOH from a Live Feed |
| Live feed and flash memory | The live feed stream has a few seconds of delay for both PSTN and local IP phone callers. The flash MOH acts as backup for
                                          the live-feed MoH. We recommend this option if you want live-feed because it provides guaranteed MOH if the live-feed input is not found or fails. | Configuring Cisco Unified SRST for Multicast MOH from an Audio File and Configuring Cisco Unified SRST for MOH from a Live Feed |

| Tip | The simplest way to create an audio source is to use the default audio source. |
|---|---|

| Note | These instructions assume that an MOH audio source file was already created. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | To enable multicast MOH for the MOH audio source, choose Service > Media Resources > Music On Hold Audio Source to display the MOH Audio Source Configuration window. |  |
| Step 2 | Double-click the required audio source listed in the MOH Audio Sources column. |  |
| Step 3 | In the MOH Audio Source Configuration window, check Allow Multicasting . |  |
| Step 4 | Click Update . |  |

| Audio Source | Codec | Increment Multicast on IP Address | Increment Multicast on Port Number |
|---|---|---|---|
| Destination IP Address | Destination Port | Destination IP Address | Destination Port |
| 1 | G.711 mu-law | 239.1.1.1 | 16384 | 239.1.1.1 | 16384 |
| 1 | G.711 a-law | 239.1.1.2 | 16384 | 239.1.1.1 | 16386 |
| 1 | G.729 | 239.1.1.3 | 16384 | 239.1.1.1 | 16388 |
| 1 | Wideband | 239.1.1.4 | 16384 | 239.1.1.1 | 16390 |
| 2 | G.711 mu-law | 239.1.1.5 | 16384 | 239.1.1.1 | 16392 |
| 2 | G.711 a-law | 239.1.1.6 | 16384 | 239.1.1.1 | 16394 |
| 2 | G.729 | 239.1.1.7 | 16384 | 239.1.1.1 | 16396 |
| 2 | Wideband | 239.1.1.8 | 16384 | 239.1.1.1 | 16398 |

| Note | The lower destination port 16384 is assigned to the first multicast-enabled audio source ID, and the subsequent ports will
                                                be assigned to the subsequent multicast-enabled audio sources. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable multicast MOH for Cisco Unified CM |  |
| Step 2 | Set the base IP address and port number. | In the MOH Server Configuration window, enter an IP address in the Base Multicast IP Address field and enter a port number
                                                in the Base Multicast Port Number field. Ensure that the IP address and port number use the required audio source and codec.
                                                See Table 2. |
| Step 3 | Select whether Cisco Unified CM increments port numbers or IP addresses. | In the MOH Server Configuration window, in the Increment Multicast on field, choose Port Number if you want port numbers to
                                                be incremented and the IP address to remain unchanged. Choose IP Address if you want IP addresses to be incremented and the
                                                port number to remain unchanged. If all of your branches run Cisco Unified SRST and thus use G.711 for MOH, use either settingbecause incrementation does not
                                                      take place and a selection does not matter. If your system configuration includes routers that do not run Cisco Unified SRST and use a different codec, select an incrementation
                                                      method. Note If your branches include routers that do not run Cisco Unified SRST and do use G.711, configure separate audio sources: one
                                                            for the routers that run Cisco Unified SRST and one for the routers that do not. | Note | If your branches include routers that do not run Cisco Unified SRST and do use G.711, configure separate audio sources: one
                                                            for the routers that run Cisco Unified SRST and one for the routers that do not. |
| Note | If your branches include routers that do not run Cisco Unified SRST and do use G.711, configure separate audio sources: one
                                                            for the routers that run Cisco Unified SRST and one for the routers that do not. |
| Step 4 | Enter a maximum number of hops. | In the MOH Server Configuration window, next to the Audio Source Name field, enter 1 in the Max Hops field if all of your
                                                branches run Cisco Unified SRST. If your system configuration includes routers that do not run Cisco Unified SRST, enter 16
                                                in the Max Hops field. |
| Step 5 | Use Cisco IOS commands to stop Cisco Unified CM signals from crossing the WAN and reaching Cisco Unified SRST gateways. | If all of your branches run Cisco Unified SRST, skip this step. If your system configuration includes routers that do not
                                                run Cisco Unified SRST and use a different codec, enter the following Cisco IOS commands starting from global configuration
                                                mode on the central site router: |

| Note | If your branches include routers that do not run Cisco Unified SRST and do use G.711, configure separate audio sources: one
                                                            for the routers that run Cisco Unified SRST and one for the routers that do not. |
|---|---|

| Note | The Gateway Configuration window for an H.323 gateway is similar for MGCP gateways. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create an MRG with a multicast MOH media resource. |  |
| Step 2 | Create an MRGL that contains the newly created MRG. |  |
| Step 3 | Add the MRGL to the required IP phones. |  |
| Step 4 | Add the MRGL to the required gateway. |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create an MOH server region. |  |
| Step 2 | Create other regions as needed for different codecs. |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Verify that Cisco Unified CM system’s multicast MOH is heard on a remote gateway. |  |
| Step 2 | Verify that the Cisco Unified CM system’s MOH is multicast, not unicast. |  |

| Note | Use the steps in this section only when you are using Microsoft Windows to run Cisco Unified Communications Manager version
                                          4.3 or below. Use the RTMT (Real-Time Monitoring Tool) in Cisco Unified Communications Manager version 5.0 and later versions
                                          on the Linux operating system to monitor MOH activity in Cisco Unified CM version. See Cisco Unified Communications Serviceability System Guide, Release 4.0(1) for more information about RTMT. |
|---|---|

| Note | The MOH file packaged with the SRST software is completely royalty free. |
|---|---|

| Note | During the copying process, four files are added to each router’s flash automatically. One of the files must use a mu-law
                                             format as indicated by the extension.ULAW.wav. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | ccm-manager music-on-hold Example: Router(config)# ccm-manager music-on-hold | Enables the multicast MOH feature on a voice gateway. |
| Step 2 | interface loopback number Example: Router(config)# interface loopback 1 | Configures an interface type and enters theinterface configuration mode. number —Loopback interface number. The range is from 0 to 2147483647. |
| Step 3 | ip address ip-address mask Example: Router(config-if)# ip address 10.1.1.1 255.255.255.255 | Sets a primary IP address for an interface. ip-address —IP address. mask —Mask for the associated IP subnet. |
| Step 4 | exit Example: Router(config-if)# exit | Exits interface configuration mode. |
| Step 5 | interface fastethernet slot/port Example: Router(config)# interface fastethernet 0/0 | (Optional if the route keyword is not used in the multicast moh command. See Step 9 and Step 13.) Configures an interface type and enters interface configuration mode. |
| Step 6 | ip address ip-address mask Example: Router(config-if)# ip-address 172.21.51.143
255.255.255.192 | (Optional if the route keyword is not used in the multicast moh command. See Step 9 and Step 13.) Sets a primary IP address for an interface. |
| Step 7 | exit Example: Router(config-if)# exit | (Optional if the route keyword is not used in the multicast moh command. See Step 9 and Step 13.) Exits interface configuration mode. |
| Step 8 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 9 | ip source-address ip-address [ port port Example: Router(config-cm-fallback)# ip source-address
172.21.51.143 port 2000 | (Optional if the route keyword is not used in the multicast moh command. See Step 13.) Enables a router to receive messages from Cisco Unified IP phones through the specified IP addresses
                                                and ports. ip-address —The pre-existing router IP address, typically one of the addresses of the Ethernet port of the router. port port —(Optional) The port to which the gateway router connects to receive messages from the Cisco Unified IP phones. The port number
                                                      range is from 2000 to 9999. The default port number is 2000. |
| Step 10 | max-ephones max-phones Example: Router(config-cm-fallback)# max-ephones 1 | Configures the maximum number of Cisco Unified IP phones that can be supported by a router. max-phones —Maximum number of Cisco IP phones supported by the router. The maximum number is platform-dependent. The default is 0. |
| Step 11 | max-dn max-directory-number Example: Router(config-cm-fallback)# max-dn 1 | Sets the maximum possible number of virtual voice ports that can be supported by a router. max-directory-number —Maximum number of directory numbers or virtual voice ports supported by the router. The maximum possible number is platform-dependent.
                                                The default is 0. |
| Step 12 | moh filename Example: Router(config-cm-fallback)# moh music-on-hold.au | Enables use of an MOH file. filename —Filename of the music file. The music file must reside in flash memory. |
| Step 13 | multicasting-enabled | Selects the multicast-enabled MOH audio source in the User Hold MOH Audio Source field on the Phone Configuration page in
                                                Cisco Unified CM Administration GUI. |
| Step 14 | multicast moh multicast-address port port [ route ip-address-list ] Example: Router(config-cm-fallback)# multicast moh 239.1.1.1
port 16386 route 239.1.1.2 239.1.1.3 239.1.1.4
239.1.1.5 | Enables multicast of MOH from a branch office flash MOH file to IP phones in the branch office. multicast-address port port —Declares the IP address and port number of MOH packets that are to be multicast. The multicast IP address and port must match
                                                      the IP address and the port number that Cisco Unified CM is configured to use for multicast MOH. If you are using different
                                                      codecs for MOH, these might not be the base IP address and port, instead an incremented IP address or port number. See the Configuring the MOH Audio Source to Enable Multicasting section. If you have multiple audio sources configured on Cisco Unified CM, ensure that you are using the audio sources’s
                                                      correct IP address and port number. route —(Optional) List of explicit router interfaces for the IP multicast packets. ip-address-list —(Optional) List of up to four explicit routes for multicast MOH. The default is that the MOH multicast stream is automatically
                                                      output on the interfaces that correspond to the address that was configured with the ip source-address command. |
| Step 15 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | debug ephone moh Example: Router# debug ephone moh
!
MOH route If FastEthernet0/0 ETHERNET 172.21.51.143
via ARP
MOH route If Loopback0 46 172.21.51.98 via
172.21.51.98
! | This command sets debugging for MOH. You can use this command to show that the Cisco Unified SRST gateway is multicasting
                                                MOH out of Loopback 0 and Fast Ethernet 0/0. |
| Step 2 | show interfaces fastethernet Example: Router# show interfaces fastethernet 0/0
!
30 second output rate 86000 bits/sec, 50 packets/sec
! | Use this command to confirm that the interface output rates match one G.711 stream, which the show interfaces fastethernet
                                                output displays as 50 packets/sec and 80 kbps or more. |
| Step 3 | show ephone summary Example: Router# show ephone summary
!
File music-on-hold.au type AU
Media_Payload_G.711Ulaw64k 160 bytes
! | Use this command to verify that the Cisco IOS software was able to read the MOH audio file successfully. |

| Note | This feature does not apply when the Cisco Unified SRST router is in fallback mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Verify that a PSTN caller hears MOH when placed on hold by an IP phone caller. Use a Cisco Unified SRST gateway IP phone to
                                             call a PSTN phone, and put the PSTN caller on hold. The PSTN caller should hear MOH. |  |
| Step 2 | show ccm-manager music-on-hold Example: Router# show ccm-manager music-on-hold
Current active multicast sessions : 1
Multicast RTP port Packets   Call Codec Incoming
Address   number   in/out    id         Interface
=======================================================
239.1.1.1 16384    326/326   42         G.711ulaw Lo0 | Use this command to verify that the MOH is multicast if you are using Windows and Cisco Unified CM version 4.3 or an earlier
                                                version. Note that the show ccm-manager music-on-hold command displays information about PSTN connections on hold only. It does not display information about multicast streams
                                                going to IP phones on hold. The following is an example of show ccm-manager music-on-hold command output. If the PSTN caller hears MOH, and the show ccm-manager music-on-hold command displays no active multicast streams, the MOH is unicast. Confirm this by checking the MOH performance counters as
                                                discussed in the Verifying Cisco Unified Communications Manager Multicast MOH section. |
| Step 3 | debug h245 asn Example: Router# debug h245 asn
*Mar 1 04:20:19.227: H245 MSC INCOMING PDU ::=
value MultimediaSystemControlMessage ::= response :
openLogicalChannelAck :
{
forwardLogicalChannelNumber 6
forwardMultiplexAckParameters
h2250LogicalChannelAckParameters :
{
sessionID 1
mediaChannel unicastAddress : iPAddress :
{
network 'EF010101'H
tsapIdentifier 16384
}
mediaControlChannel unicastAddress : iPAddress :
{
network 'EF010101'H
tsapIdentifier 16385
}
}
} | Use this command if H.323 is being used and no multicast address appears in the show ccm-manager music-on-hold command output to verify the H.323 handshaking between Cisco Unified Communications Manager and the Cisco Unified SRST gateway.
                                                When a PSTN caller is placed on hold, Cisco Unified Communications Manager sends an H.245 closeLogicalChannel, followed by
                                                an openLogicalChannel. Verify that the final openLogicalChannelAck from Cisco Unified Communications Manager to the Cisco
                                                Unified SRST gateway contains the expected multicast IP address and port number. In the following example, the IP address
                                                is EF010101 (239.1.1.1) and the port number is 16384. |
| Step 4 | show call active voice Example: Router# show call active voice \| include RemoteMedia
RemoteMediaIPAddress=239.1.1.1
RemoteMediaPort=16384 | Use this command with the debug h245 asn command to further verify the H.323 handshaking between Cisco Unified Communications
                                                Manager and the Cisco Unified SRST gateway. The IP address and port number displayed must match the IP address and port number displayed by the debug h245 asn command.
                                                If the RemoteMediaIPAddress field displays 0.0.0.0, you probably have encountered caveat CSCdz00697. For more information,
                                                see the Cisco Bug ToolKit and the Restrictions for Using Cisco Unified SRST Gateways as a Multicast MOH Resource section. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Verify that an IP phone caller hears MOH when placed on hold by an IP phone caller. | Use an IP phone to call a second IP phone, and put the second caller on hold. The second caller should hear MOH. |
| Step 2 | Check the MOHMulticastResourceActive and MOHUnicastResourceActive counters. | Use the Performance window to check the MOHMulticastResourceActive and MOHUnicastResourceActive counters under the Cisco MOH
                                                Device performance object. See Step 2 in the Verifying Cisco Unified Communications Manager Multicast MOH section. For Cisco Unified SRST multicasting MOH to work, the multicast counter must increment. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | voice-port port Example: Router(config)# voice-port 1/1/0 | Enters voice-port configuration mode to set up the physical voice port. To find the correct definition of the port argument
                                                for your router, see Cisco IOS Survivable Remote Site Telephony Version 3.2 Command Reference . . |
| Step 2 | input gain decibels Example: Router(config-voice-port)# input gain 0 | Specifies, in decibels, the amount of gain to be inserted at the receiver side of the interface. Acceptable values are integers
                                                from –6 to 14. |
| Step 3 | auto-cut-through Example: Router(config-voiceport)# auto-cut-through | (E&M ports only) Enables call completion when a PBX does not provide an M-lead response. MOH requires that you use this command
                                                with E&M ports. |
| Step 4 | operation 4-wire Example: Router(config-voiceport)# operation 4-wire | (E&M ports only) Selects the 4-wire cabling scheme. MOH requires that you specify 4-wire operation with this command for E&M
                                                ports. |
| Step 5 | signal immediate Example: Router(config-voiceport)# signal immediate | (E&M ports only) For E&M tie trunk interfaces, directs the calling side to seize a line by going off-hook on its E-lead and
                                                to send address information as DTMF digits. |
| Step 6 | no shutdown Example: Router(config-voiceport)# no shutdown | Activates the voice port. |
| Step 7 | exit Example: Router(config-voiceport)# exit | Exits voice-port configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | dial-peer voice tag pots Example: Router(config)# dial-peer voice 7777 pots | Enters dial-peer configuration mode. |
| Step 2 | destination-pattern string Example: Router(config-dial-peer)# destination-pattern
7777 | Specifies the directory number that the system uses to create MOH. This command specifies either the prefix or the full E.164
                                                telephone number to be used for a dial peer. |
| Step 3 | port port Example: Router(config-dial-peer)# port 1/1/0 | Associates the dial peer with the voice port that was specified in the Setting Up the Voice Port on the Cisco Unified SRST Gateway section. |
| Step 4 | exit Example: Router(config-dial-peer)# exit | Exits dial-peer configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | max-dn max-directory-number Example: Router(config-cm-fallback)# max-dn 1 | Sets the maximum possible number of virtual voice ports that can be supported by a router. max-directory-number —Maximum number of directory numbers or virtual voice ports supported by the router. The maximum possible number is platform-dependent.
                                                      The default is 0. |
| Step 3 | multicast moh multicast-address port port [ route ip-address-list ] Example: Router(config-cm-fallback)# multicast moh
239.1.1.1 port 16386 route 239.1.1.2 239.1.1.3
239.1.1.4 239.1.1.5 Example: Router(config-cm-fallback)# multicast moh | Enables multicast of MOH from a branch office flash MOH file to IP phones in the branch office. Note This command must be used to source live feed MOH to multicast Cisco Unified CM mode. It is not required in strict SRST mode. multicast-address and port port —Declares the IP address and port number of MOH packets that are to be multicast. The multicast IP address and port must
                                                      match the IP address and the port number that Cisco Unified Communications Manager is configured to use for multicast MOH.
                                                      If you are using different codecs for MOH, these might not be the base IP address and port, but an incremented IP address
                                                      or port number. See the Configuring the MOH Audio Source to Enable Multicasting section. If you have multiple audio sources configured on Cisco Unified CM, ensure that you are using the audio sources’
                                                      correct IP address and port number. route ip-address-list —(Optional) Declares the IP address or addresses from which the flash MOH packets can be transmitted. A maximum of four IP
                                                      address entries are allowed. If a route keyword is not configured, the Cisco Unified SRST system uses the ip source-address command value configured for Cisco Unified SRST. | Note | This command must be used to source live feed MOH to multicast Cisco Unified CM mode. It is not required in strict SRST mode. |
| Note | This command must be used to source live feed MOH to multicast Cisco Unified CM mode. It is not required in strict SRST mode. |
| Step 4 | moh-live dn-number calling-number out-call outcall-number Example: Router(config-cm-fallback)# moh-live dn-number
3333 out-call 7777 | Specifies that this telephone number is to be used for an outgoing call that is to be the source for an MOH stream. dn-number calling-number — Sets the MOH telephone number. The calling-number argument is a sequence of digits that represent a telephone number. out-call outcall-number —Indicates that the router is calling out for a live feed that is to be used for MOH and specifies the number to be called.
                                                      The outcall-number argument is a sequence of digits that represent a telephone number, typically of an E&M port. The outcall keyword makes a connection to the local router voice port that was specified in the the Setting Up the Voice Port on the Cisco Unified SRST Gateway section. |
| Step 5 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | This command must be used to source live feed MOH to multicast Cisco Unified CM mode. It is not required in strict SRST mode. |
|---|---|

| Note | The multicast IP address and port must match the IP address and the port number that Cisco Unified CM is configured to use
                                             for multicast MOH. If you are using different codecs for MOH, these might not be the base IP address and port, but an incremented
                                             IP address or port number. See the the Configuring the MOH Audio Source to Enable Multicasting section. If you have multiple audio sources configured on Cisco Unified CM, ensure that you are using the audio source’s
                                             correct IP address and port number. |
|---|---|

| Note | The Feature Information for Cisco Unified SRST as a Multicast MOH Resource table lists the Cisco Unified SRST version that
                                       introduced support for a given feature. Unless noted otherwise, subsequent versions of Cisco Unified SRST software also support
                                       that feature. |
|---|---|

| Feature Name | Releases | Feature Information |
|---|---|---|
| Cisco Unified SRST as a Multicast MOH Resource | 3.0 | The MOH-live feature was added. |