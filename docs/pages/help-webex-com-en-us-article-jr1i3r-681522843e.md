---
doc_id: help-webex-com-en-us-article-jr1i3r-681522843e
source_url: https://help.webex.com/en-us/article/jr1i3r
retrieved_at: 2026-11-02T13:01:12.096436+00:00
---

Webex Calling currently supports two versions of Local Gateway:

Local Gateway

Local Gateway for Webex for Government

- Local Gateway

- Local Gateway for Webex for Government

Key considerations

Before you begin, understand the premises-based Public Switched Telephone Network (PSTN) and Local Gateway (LGW) requirements for Webex Calling. See Cisco Preferred Architecture for Webex Calling for more information.

This article assumes that a dedicated Local Gateway platform is in place with no existing voice configuration. If you modify an existing PSTN gateway or CUBE Enterprise deployment to use as the Local Gateway function for Webex Calling, then pay careful attention to the configuration. Ensure that you don't interrupt the existing call flows and functionality because of the changes that you make.

The procedures contain links to command reference documentation where you can learn more
        about the individual command options. All command reference links go to the Webex
          Managed Gateways Command Reference unless stated otherwise (in which case, the
        command links go to Cisco IOS Voice Command Reference ). You can access all
        these guides at Cisco Unified Border Element Command References .

For information on the supported third-party SBCs, refer to the respective product
        reference documentation.

Configure your Local Gateway

There are two options to configure the Local Gateway for your Webex Calling trunk:

Registration-based trunk

Certificate-based trunk

Use the task flow either under the Registration-based Local Gateway or Certificate-based Local Gateway to configure Local Gateway for your
      Webex Calling trunk.

See Get started with Local Gateway for more information on different trunk types.
      Perform the following steps on the Local Gateway itself, using the Command Line Interface
      (CLI). We use Session Initiation Protocol (SIP) and Transport Layer Security (TLS) transport
      to secure the trunk and Secure Real Time Protocol (SRTP) to secure the media between the Local
      Gateway and Webex Calling.

Key considerations

Select CUBE as your Local Gateway. Webex for Government doesn’t currently support any third-party Session Border Controllers (SBCs). To review the latest list, see Get started with Local Gateway .

- Install Cisco IOS XE Dublin 17.12.1a or later versions for all Webex for Government Local Gateways.

To review the list of root Certificate Authorities (CAs) that Webex for Government support, see Root certificate authorities for Webex for Government .

For details on the external port ranges for Local Gateway in Webex for Government, see Network requirements for Webex for Government (FedRAMP) .

Local Gateway for Webex for Government doesn’t support the following:

STUN/ICE-Lite for media path optimization

Fax (T.38)

Configure your Local Gateway for Webex for Government

To configure Local Gateway for your Webex Calling trunk in Webex for Government, use the following option:

Certificate-based trunk

Use the task flow under the Certificate-based Local Gateway to configure the Local Gateway for your Webex Calling trunk. For more details on how to configure a certificate-based Local Gateway, see Configure Webex Calling certificate-based trunk .

It’s mandatory to configure FIPS-compliant GCM ciphers to support Local Gateway for Webex for Government. If not, the call setup fails. For configuration details, see Configure Webex Calling certificate-based trunk .

Webex for Government doesn’t support registration-based Local Gateway.

- Registration-based Local Gateway

- Certificate-based Local Gateway

Design overview

This section describes how to configure a Cisco Unified Border Element (CUBE) as a Local
      Gateway for Webex Calling, using a registering SIP trunk. The first part of this document
      illustrates how to configure a simple PSTN gateway. In this case, all calls from the PSTN are
      routed to Webex Calling and all calls from Webex Calling are routed to the PSTN. The image
      below highlights this solution and the high-level call routing configuration that will be
      followed.

In this design, the following principal configurations are used:

voice class tenants: Used to create trunk specific configurations.

voice class uri: Used to classify SIP messages for the selection of an inbound
          dial-peer.

inbound dial-peer: Provides treatment for inbound SIP messages and determines the
          outbound route using a dial-peer group.

dial-peer group: Defines the outbound dial-peers used for onward call routing.

outbound dial-peer: Provides treatment for outbound SIP messages and routes them to
          the required target.

For Webex Calling media optimization with Interactive Connectivity Establishment (ICE) and TDM
      (Time Division Multiplexing) ISDN circuits, it's necessary to use a two-leg call routing
      process.

While IP and SIP have become the default protocols for PSTN trunks, TDM (Time
      Division Multiplexing) ISDN circuits remain common and are fully supported by Webex Calling.
      To enable media optimization for these TDM-IP call flows, you must use Interactive
      Connectivity Establishment (ICE), which allows endpoints to negotiate direct media paths.

Achieving this optimization requires a two-leg call routing process. This approach modifies
      the standard routing configuration by introducing a set of internal loop-back dial-peers
      between Webex Calling and PSTN trunks, as illustrated in the image below.

When connecting an on-premises Cisco Unified Communications Manager solution with Webex
      Calling, you can use the simple PSTN gateway configuration as a baseline for building the
      solution illustrated in the following diagram. In this case, Unified Communications Manager
      provides centralized routing and treatment of all PSTN and Webex Calling calls.

Throughout this document, the host names, IP addresses, and interfaces illustrated in the
      following image are used.

Use the configuration guidance in the rest of this document to complete your Local Gateway
      configuration as follows:

Step 1: Configure router baseline connectivity and security

Step 2: Configure Webex Calling Trunk

Depending on your required architecture, follow either:

Step 3: Configure Local Gateway with SIP PSTN trunk

Step 4: Configure Local Gateway with an existing Unified CM environment

Or:

Step 3: Configure Local Gateway with TDM PSTN trunk

Configure connectivity and security

### Baseline configuration

The first step in preparing your Cisco router as a Local Gateway for Webex Calling is to
      build a baseline configuration that secures your platform and establishes connectivity.

All registration-based Local Gateway deployments require Cisco IOS XE 17.6.1a or later
          versions. Cisco IOS 17.12.2 or later is recommended. For the recommended versions, see the Cisco Software Research page. Search for the platform and select one of the suggested releases.

ISR4000 series routers must be configured with both Unified Communications and
              Security technology licenses.

Catalyst Edge 8000 series routers fitted with voice cards or DSPs require DNA
              Advantage licensing. Routers without voice cards or DSPs require a minimum of DNA
              Essentials licensing.

Build a baseline configuration for your platform that follows your business policies. In
          particular, configure and verify the following:

NTP

ACLs

User authentication and remote access

DNS

IP routing

IP addresses

The network toward Webex Calling must use an IPv4 address.

Upload the Cisco root CA bundle to the Local Gateway.

When configuring the tenant-side to connect with Webex Calling, only SRV-based addresses
        are supported.

### Configuration

Ensure that you assign valid and routable IP addresses to any Layer 3 interfaces, for
          example:

```
interface GigabitEthernet0/0/0
  description Interface facing PSTN and/or CUCM
  ip address 10.80.13.12 255.255.255.0
!
interface GigabitEthernet0/0/1
  description Interface facing Webex Calling (Private address)
  ip address 192.51.100.1 255.255.255.240
```

Protect registration and STUN credentials on the router using symmetric encryption.
          Configure the primary encryption key and encryption type as follows:

```
key config-key password-encrypt YourPassword
password encryption aes
```

Create a placeholder PKI trustpoint.

Requires this trustpoint to configure TLS later. For registration-based trunks, this trustpoint doesn't require a certificate - as required for a certificate-based trunk.

```
crypto pki trustpoint EmptyTP 
 revocation-check none
```

Enable TLS1.2 exclusivity and specify the default trustpoint using the following configuration commands. Update the Transport parameters to ensure a reliable secure connection for registration:

The cn-san-validate server command ensures that the Local Gateway permits a connection, if the host name configured in tenant 200 is included in either the CN or SAN fields of the certificate received from the outbound proxy.

Set tcp-retry count to 1000 (5-msec multiples = 5 seconds).

The timer connection establish command allows you to tune how long the LGW waits to set up a connection with a proxy before considering the next available option. The default for this timer is 20 seconds and the minimum 5 seconds. Start with a low value and increase if necessary to accommodate network conditions.

```
sip-ua
 timers connection establish tls 5
 transport tcp tls v1.2
 crypto signaling default trustpoint EmptyTP cn-san-validate server
 tcp-retry 1000
```

Install the Cisco root CA bundle, which includes the IdenTrust Commercial Root CA1 certificate used by Webex Calling. Use the crypto pki trustpool import clean url command to download the root CA bundle from the specified URL, and to clear the current CA trustpool, then install the new bundle of certificates:

If you need to use a proxy for access to the internet using HTTPS, add the following configuration before importing the CA bundle:

```
ip http client source-interface GigabitEthernet0/0/1 
crypto pki trustpool import clean url https://www.cisco.com/security/pki/trs/ios_core.p7b
```

Configure Webex Calling registration-based trunk

Create a registration based PSTN trunk for an existing location in the Control
                    Hub. Make a note of the trunk information that is provided once the trunk has
                    been created. The details highlighted in the illustration are used in the
                    configuration steps in this guide. For more information, see Configure trunks, route groups, and dial
                        plans for Webex Calling .

Enter the following commands to configure CUBE as a Webex Calling Local
                    Gateway:

```
voice service voip
 ip address trusted list
  ipv4 x.x.x.x y.y.y.y
 mode border-element
 media statistics
 media bulk-stats 
 allow-connections sip to sip
 no supplementary-service sip refer  
 stun
  stun flowdata agent-id 1 boot-count 4
  stun flowdata shared-secret 0 Password123$
 sip
  asymmetric payload full
  early-offer forced
```

Here's an explanation of the fields for the
                        configuration:

```
ip address trusted list ipv4 x.x.x.x y.y.y.y
```

To protect against toll fraud, the trusted address list defines a
                                list of hosts and networks from which the Local Gateway expects
                                legitimate VoIP calls.

By default, Local Gateway blocks all incoming VoIP messages from IP
                                addresses not in its trusted list. By default, statically configured
                                dial-peers with “session target IP” or server group IP addresses are
                                trusted. Adding these IP addresses to the trusted list is not
                                required.

When configuring your Local Gateway, add the IP subnets of your
                                regional Webex Calling data center to the list. For more
                                information, see Port Reference Information for Webex
                                    Calling . Also, add address ranges for Unified
                                Communications Manager servers (if used) and PSTN trunk
                                gateways.

If your LGW is behind a firewall with restricted cone NAT, you
                                    may prefer to disable the IP address trusted list on the Webex
                                    Calling facing interface. The firewall already protects you from
                                    unsolicited inbound VoIP. Disable action reduces your
                                    longer-term configuration overhead, because we cannot guarantee
                                    that the addresses of the Webex Calling peers remain fixed, and
                                    you must configure your firewall for the peers in any case.

Enables Cisco Unified
                        Border Element (CUBE) features on the platform.

Enables media monitoring on the Local
                        Gateway.

Enables the
                        control plane to poll the data plane for bulk call statistics.

For
                        more information on these commands, see Media .

Enable CUBE basic SIP back-to-back user agent
                        functionality. For more information, see Allow connections .

By default, T.38 fax transport is enabled. For more information, see fax protocol t38
                                (voice-service) .

Enables STUN (Session Traversal of UDP
                        through NAT) globally.

The STUN bindings feature on the Local Gateway allows locally
                                generated STUN requests to be sent over the negotiated media path.
                                This helps to open the pinhole in the firewall.

For more information, see stun flowdata agent-id and stun flowdata
                            shared-secret .

Configures SIP asymmetric payload support for both DTMF
                        and dynamic codec payloads. For more information, see asymmetric
                            payload .

Forces
                        the Local Gateway to send SDP information in the initial INVITE message
                        instead of waiting for acknowledgment from the neighboring peer. For more
                        information on this command, see early-offer .

Configure voice class codec 100 allowing G.711 codecs
                    only for all trunks. This simple approach is suitable for most deployments. If
                    required, additional codec types supported by both originating and terminating
                    systems may be added to the list.

More complex solutions involving transcoding using DSP modules
                            are supported, but not included in this guide.

```
voice class codec 100
 codec preference 1 g711ulaw
 codec preference 2 g711alaw
```

Here's an explanation of the fields for the
                            configuration:

Used
                        to only allow preferred codecs for SIP trunk calls. For more information,
                        see voice class codec .

Configure voice class stun-usage 100 to
                    enable ICE on the Webex Calling trunk.

```
voice class stun-usage 100 
 stun usage firewall-traversal flowdata
 stun usage ice lite
```

Here's an explanation of the fields for the
                        configuration:

Used to
                        enable ICE-Lite for all Webex Calling facing dial-peers to allow
                        media-optimization whenever possible. For more information, see voice class stun usage and stun usage ice lite .

Media optimization is negotiated wherever possible. If a call requires
                            cloud media services, such as recording, the media cannot be
                            optimized.

Configure the media encryption policy for Webex traffic.

```
voice class srtp-crypto 100
 crypto 1 AES_CM_128_HMAC_SHA1_80
```

Here's an explanation of the fields
                        for the configuration:

Specifies SHA1_80 as the only SRTP cipher-suite CUBE
                        offers in the SDP in offer and answer messages. Webex Calling only supports
                        SHA1_80. For more information, see voice class
                    srtp-crypto .

Configure a pattern to identify calls to a Local Gateway trunk based on its
                    destination trunk parameter:

```
voice class uri 100 sip
 pattern dtg=dallas1463285401_lgu
```

Here's an explanation of the fields for the
                            configuration:

Defines a pattern to match an incoming SIP invite to an
                        incoming trunk dial-peer. When entering this pattern, use dtg= followed by
                        the Trunk OTG/DTG value provided in the Control Hub when the trunk was
                        created. For more information, see voice class uri .

Configure sip profile 100 , which will be used to
                    modify SIP messages before they are sent to Webex Calling.

```
voice class sip-profiles 100
 rule 10 request ANY sip-header SIP-Req-URI modify "sips:" "sip:"
 rule 20 request ANY sip-header To modify "<sips:" "<sip:"
 rule 30 request ANY sip-header From modify "<sips:" "<sip:"
 rule 40 request ANY sip-header Contact modify "<sips:(.*)>" "<sip:\1;transport=tls>" 
 rule 50 response ANY sip-header To modify "<sips:" "<sip:"
 rule 60 response ANY sip-header From modify "<sips:" "<sip:"
 rule 70 response ANY sip-header Contact modify "<sips:" "<sip:"
 rule 80 request ANY sip-header From modify ">" ";otg=dallas1463285401_lgu>"
 rule 90 request ANY sip-header P-Asserted-Identity modify "sips:" "sip:"
```

Here's an explanation of the fields for the configuration:

rule 10 to 70 and 90

Ensures that SIP headers used for call signaling use SIP, rather than
                                SIPs scheme, which Webex proxies require. Configuring CUBE to use
                                SIP ensures that secure registration is used.

rule 80

Modifies the From header to include the trunk group OTG/DTG
                                identifier from the Control Hub to uniquely identify a Local Gateway
                                site within an enterprise.

United States or Canadian PSTN provider can offer the Caller ID
                            verification for Spam and fraud calls, with the additional configuration
                            mentioned in the Spam or fraud call indication in
                                Webex Calling article.

Configure Webex Calling trunk:

Create voice class tenant 100 to
                            define and group configurations required specifically for the Webex
                            Calling trunk. In particular, the trunk registration details provided in
                            Control Hub earlier will be used in this step as detailed below.
                            Dial-peers associated with this tenant later will inherit these
                            configurations.

The following example uses the values illustrated in Step 1 for
                                    the purpose of this guide (shown in bold). Replace these with
                                    values for your trunk in your configuration.

```
voice class tenant 100
  registrar dns: 98027369.us10.bcld.webex.com scheme sips expires 240 refresh-ratio 50 tcp tls
  credentials number Dallas1171197921_LGU username Dallas1463285401_LGU password 0 9Wt[M6ifY+ realm BroadWorks
  authentication username Dallas1463285401_LGU password 0 9Wt[M6ifY+ realm BroadWorks
  authentication username Dallas1463285401_LGU password 0 9Wt[M6ifY+ realm 98027369.us10.bcld.webex.com no remote-party-id
  sip-server dns: 98027369.us10.bcld.webex.com connection-reuse
  srtp-crypto 100
  session transport tcp tls 
  no session refresh
  url sips 
  error-passthru
  rel1xx disable
  asserted-id pai 
  bind control source-interface GigabitEthernet0/0/1
  bind media source-interface GigabitEthernet0/0/1
  no pass-thru content custom-sdp 
  sip-profiles 100 
  outbound-proxy dns: dfw04.sipconnect-us.bcld.webex.com privacy-policy passthru
```

Here's an explanation of the fields for the
                                configuration:

Defines a set of configuration
                                parameters that will be used only for the Webex Calling trunk. For
                                more information, see voice class
                                    tenant .

Registrar server for the Local Gateway with the
                                registration set to refresh every two minutes (50% of 240 seconds).
                                For more information, see registrar .

Ensure
                                that you use the Register Domain value from the Control Hub
                                here.

Credentials for trunk
                                registration challenge. For more information, see credentials (SIP
                                UA) .

Ensure that you use the Line/Port host,
                                Authentication Username and Authentication Password values
                                respectively from the Control Hub
                                    here.

Authentication
                                challenge for calls. For more information, see authentication
                                (dial-peer) .

Ensure that you use the Authentication
                                Username, Authentication Password and Registrar Domain values
                                respectively from the Control Hub here.

Disable SIP Remote-Party-ID
                                (RPID) header as Webex Calling supports PAI, which is enabled using asserted-id pai . For more
                                information, see remote-party-id .

Configures
                                the target SIP server for the trunk. Use the Edge proxy SRV address
                                provided in the Control Hub when you created your
                                    trunk.

Uses the
                                same persistent connection for registration and call processing. For
                                more information, see connection-reuse .

Configures the preferred
                                cipher-suites for the SRTP call leg (connection) (specified in step
                                5). For more information, see voice class
                                srtp-crypto.

Sets transport to TLS. For more information, see session-transport .

Disables SIP session refresh for calls
                                between CUBE and Webex. For more information, see session
                            refresh .

SRV query must be SIPs as
                                supported by the access SBC; all other messages are changed to SIP
                                by sip-profile
                                200.

Specifies SIP
                                error response pass-thru functionality. For more information, see error-passthru .

Disables the use of
                                reliable provisional responses for the Webex Calling trunk. For more
                                information, see rel1xx .

(Optional) Turns on
                                P-Asserted-Identity header processing and controls how this is used
                                for the Webex Calling trunk.

Webex Calling includes
                                P-Asserted-Identity (PAI) headers in outbound call INVITEs to the
                                Local Gateway.

If this command is configured, caller
                                information from the PAI header is used to populate the outgoing
                                From and PAI/Remote-Party-ID headers.

If this command is not
                                configured, caller information from the From header is used to
                                populate the outgoing From and PAI/Remote-Party-ID
                                headers.

For more information, see asserted-id .

Configures the
                                source interface and associated IP address for messages sent to
                                Webex Calling. For more information, see bind .

Configures the
                                source interface and associated IP address for media sent to
                                WebexCalling. For more information, see bind .

Default command
                                under tenant. For more information on this command, see pass-thru
                                    content .

Changes SIPs to SIP and modify
                                Line/Port for INVITE and REGISTER messages as defined in sip-profiles 100 . For
                                more information, see voice class
                                sip-profiles .

Webex
                                Calling access SBC. Insert the Outbound Proxy Address provided in
                                the Control Hub when you created your trunk. For more information,
                                see outbound-proxy .

Configures the privacy header policy
                                options for the trunk to pass privacy values from the received
                                message to the next call leg. For more information, see privacy-policy .

Configure the Webex Calling trunk dial-peer.

```
dial-peer voice 100 voip
 description Inbound/Outbound Webex Calling
 max-conn 250
 destination-pattern BAD.BAD
 session protocol sipv2
 session target sip-server
 incoming uri request 100
 voice-class codec 100
 dtmf-relay rtp-nte
 voice-class stun-usage 100
 no voice-class sip localhost
 voice-class sip tenant 100
 srtp
 no vad
```

Here's an explanation of the fields for the
                                configuration:

```
dial-peer voice 100 voip description Inbound/Outbound Webex Calling
```

Defines a VoIP dial-peer with a tag of 100 and gives
                                a meaningful description for ease of management and
                                troubleshooting.

Restricts the number of concurrent
                                inbound and outbound calls between the LGW and Webex Calling. For
                                registration trunks, the maximum value configured should be 250.
                                User lower value if that would be more appropriate for your
                                deployment. For more information on concurrent call limits for Local
                                Gateway, refer to the Get started with Local
                                    Gateway document.

A dummy destination pattern
                                is required when routing outbound calls using an inbound dial-peer
                                group. Any valid destination pattern may be used in this case. For
                                more information, see destination-pattern
                                    (interface) .

Specifies that dial-peer 100 handles SIP call
                                legs. For more information, see session protocol
                                    (dial-peer) .

Indicates that the SIP server defined
                                in tenant 100 is inherited and used for the destination for calls
                                from this dial peer. For more information, see session target (voip dial
                                    peer) .

To specify the voice class used
                                to match a VoIP dial peer to the Uniform Resource Identifier (URI)
                                of an incoming call. For more information, see incoming
                                    uri .

Configures the dial-peer to use
                                the common codec filter list 100. For more information, see voice-class
                                    codec .

Allows locally generated STUN
                                requests on the Local Gateway to be sent over the negotiated media
                                path. STUN helps to open a firewall pinhole for media traffic. For
                                more information, see voice-class
                                stun-usage .

Disables substitution of the DNS local
                                host name in place of the physical IP address in the From, Call-ID,
                                and Remote-Party-ID headers of outgoing
                                    messages.

The dial-peer inherits all
                                parameters configured globally and in tenant 100. Parameters may be
                                overridden at the dial-peer
                                level.

Enables SRTP for the call
                                leg.

Disables voice activity
                                detection.

(Optional)  Force calls to audio only.

Video over Webex Calling using Local Gateway call flows is not
                                supported. Although video can function in some scenarios, it can
                                result in degraded quality and unexpected behavior. To force calls
                                to audio only, apply the following command under your Webex Calling
                                dial-peers:

```
voice-class sip audio forced
```

If you choose to allow video, calls may not perform as expected.

To configure network devices such as CUBE and to forward Session Initiation Protocol (SIP) headers that the device doesn't process, use these commands. These commands enable the device to pass through unsupported SIP headers, including geo-location headers and PIDF-LO (Presence Information Data Format - Location Object), on the local gateway. This functionality supports Nomadic E911 services by ensuring that critical location information is preserved and forwarded correctly.

Dial peer Configuration

```
Voice service voip
 sip
  pass-thru headers unsupp
```

Dial peer specific configuration

```
Dial-peer voice 911 voip
 voice-class sip pass-thru headers unsupp
```

Voice Class configuration for specific headers

To proxy the Geo location headers:

```
voice class sip-hdr-passthrulist 200 
 passthru-hdr Geolocation-Routing
 passthru-hdr Geolocation
 passthru-hdr-unsupp
```

Apply the pass-through to the inbound/outbound dial-peer

```
dial-peer voice 100 voip  // inbound
 voice-class sip pass-thru headers 200
dial-peer voice 200 voip  // outbound
 voice-class sip pass-thru headers 200
```

To enable the pass-through of the PIDFO body, use:

```
voice service voip 
 sip 
  pass-thru content unsupp
```

After you define the tenant 100 and configure a SIP VoIP
                dial-peer, the gateway initiates a TLS connection toward Webex Calling. At this
                point, the access SBC presents its certificate to the Local Gateway. The Local
                Gateway validates the Webex Calling access SBC certificate using the CA root bundle
                that was updated earlier. If the certificate is recognized, a persistent TLS session
                is established between the Local Gateway and Webex Calling access SBC. The Local
                Gateway is then able to use this secure connection to register with the Webex access
                SBC. When the registration is challenged for authentication:

The username , password , and realm parameters from the credentials configuration is used in the
                        response.

The modification rules in sip profile 100 are used to convert SIPS URL back
                        to SIP.

Registration is successful when a 200 OK is received from the access SBC.

Configure Local Gateway with a SIP PSTN trunk

Having built a trunk towards Webex Calling above, use the following configuration to
                create a non-encrypted trunk towards a SIP based PSTN provider:

If your Service Provider offers a secure PSTN trunk, you may follow a similar
                    configuration as detailed above for the Webex Calling trunk. CUBE supports
                    secure call routing.

If you are using a TDM / ISDN PSTN trunk, skip to the next section Configure Local Gateway with TDM PSTN trunk .

To configure TDM interfaces for PSTN call legs on the Cisco TDM-SIP Gateways,
                        see Configuring ISDN PRI .

Configure the following voice class uri to identify inbound calls from the PSTN
                    trunk:

```
voice class uri 200 sip
  host ipv4:192.168.80.13
```

Here's an explanation of the fields for the configuration:

Defines a
                        pattern to match an incoming SIP invite to an incoming trunk dial-peer. When
                        entering this pattern, use the IP address of your IP PSTN gateway. For more
                        information, see voice class uri .

Configure the following IP PSTN dial-peer:

```
dial-peer voice 200 voip
 description Inbound/Outbound IP PSTN trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target ipv4:192.168.80.13
 incoming uri via 200
 voice-class sip asserted-id pai
 voice-class sip bind control source-interface GigabitEthernet0/0/0 
 voice-class sip bind media source-interface  GigabitEthernet0/0/0 
 voice-class codec 100
 dtmf-relay rtp-nte 
 no vad
```

Here's an explanation of the fields for the
                        configuration:

```
dial-peer voice 200 voip description Inbound/Outbound IP PSTN trunk
```

Defines
                        a VoIP dial-peer with a tag of 200 and gives a meaningful description
                        for ease of management and troubleshooting. For more information, see dial-peer
                            voice.

A dummy destination pattern is
                        required when routing outbound calls using an inbound dial-peer group. Any
                        valid destination pattern may be used in this case. For more information,
                        see destination-pattern
                        (interface) .

Specifies that this dial-peer handles SIP call legs.
                        For more information, see session protocol (dial
                            peer) .

Specifies the target
                        address for calls sent to the PSTN provider. This could be either an IP
                        address or DNS host name. For more information, see session target (VoIP dial
                        peer) .

Specifies the voice class used to match
                        incoming calls to this dial-peer using the INVITE VIA header URI. For more
                        information, see incoming url .

(Optional) Turns
                        on P-Asserted-Identity header processing and controls how this is used for
                        the PSTN trunk. If this command is used, the calling party identity provided
                        from the incoming dial-peer is used for the outgoing From and
                        P-Asserted-Identity headers. If this command is not used, the calling party
                        identity provided from the incoming dial-peer is used for the outgoing From
                        and Remote-Party-ID headers. For more information, see voice-class sip
                    asserted-id .

Configures
                        the source interface and associated IP address for messages sent to the
                        PSTN. For more information, see bind .

Configures
                        the source interface and associated IP address for media sent to PSTN. For
                        more information, see bind .

Configures the dial-peer to use the
                        common codec filter list 100 . For more information, see voice-class
                            codec .

Defines
                        RTP-NTE (RFC2833) as the DTMF capability expected on the call leg. For more
                        information, see DTMF Relay (Voice over
                            IP) .

Disables voice
                        activity detection. For more information, see vad (dial peer) .

If you are configuring your Local Gateway to only route calls between Webex
                    Calling and the PSTN, add the following call routing configuration. If you are
                    configuring your Local Gateway with a Unified Communications Manager platform,
                    skip to the next section.

Create dial-peer groups to route calls towards Webex Calling or the
                            PSTN. Define DPG 100 with outbound dial-peer 100 toward Webex Calling.
                            DPG 100 is applied to the incoming dial-peer from the PSTN. Similarly,
                            define DPG 200 with outbound dial-peer 200 toward the PSTN. DPG 200 is
                            applied to the incoming dial-peer from Webex.

```
voice class dpg 100 
 description Route calls to Webex Calling 
 dial-peer 100 
voice class dpg 200 
 description Route calls to PSTN 
 dial-peer 200
```

Here's an explanation of the fields for the
                                configuration:

Associates an outbound dial-peer with
                                a dial-peer group. For more information, see voice-class
                            dpg .

Apply dial-peer groups to route calls from Webex to the PSTN and from
                            the PSTN to Webex:

```
dial-peer voice 100
 destination dpg 200
dial-peer voice 200
 destination dpg 100
```

Here's an explanation of the fields for
                                the configuration:

Specifies which dial-peer group,
                                and therefore dial-peer should be used for the outbound treatment
                                for calls presented to this incoming dial-peer.

This
                                concludes your Local Gateway configuration. Save the configuration
                                and reload the platform if this is the first time CUBE features are
                                configured.

Configure Local Gateway with a TDM PSTN trunk

Having built a trunk towards Webex Calling, use the following configuration to create a TDM
        trunk for your PSTN service with loop-back call routing to allow media optimization on the
        Webex call leg.

If you do not require IP media optimization, follow the configuration steps for a SIP
          PSTN trunk. Use a voice port and POTS dial-peer (as shown in Steps 2 and 3) instead of the
          PSTN VoIP dial-peer.

The loop-back dial-peer configuration uses dial-peer groups and call routing tags to
          ensure that calls pass correctly between Webex and the PSTN, without creating call routing
          loops. Configure the following translation rules that will be used to add and remove the
          call routing tags:

```
voice translation-rule 100 
 rule 1 /^\+/ /A2A/ 

voice translation-profile 100 
 translate called 100 

voice translation-rule 200 
 rule 1 /^/ /A1A/ 

voice translation-profile 200 
 translate called 200 

voice translation-rule 11 
 rule 1 /^A1A/ // 

voice translation-profile 11 
 translate called 11 

voice translation-rule 12 
 rule 1 /^A2A44/ /0/
 rule 2/^A2A/ /00/

voice translation-profile 12 
 translate called 12
```

Here's an explanation of the fields for the configuration:

Uses regular expressions
            defined in rules to add or remove call routing tags. Over-decadic digits (‘A’) are used
            to add clarity for troubleshooting.

In this configuration, the tag added by
            translation-profile 100 is used to guide calls from Webex Calling towards the PSTN via
            the loopback dial-peers. Similarly, the tag added by translation-profile 200 is used to
            guide calls from the PSTN towards Webex Calling. Translation-profiles 11 and 12 remove
            these tags before delivering calls to the Webex and PSTN trunks respectively.

This example assumes that called numbers from Webex Calling are presented in
            +E.164 format. Rule 100 removes the leading + to maintain a valid called number. Rule 12
            then adds a national or international routing digit(s) when removing the tag. Use digits
            that suit your local ISDN national dial plan.

If Webex Calling presents numbers in
            national format, adjust rules 100 and 12 to simply add and remove the routing tag
            respectively.

For more information, see voice translation-profile and voice translation-rule .

Configure TDM voice interface ports as required by the trunk type and protocol used.
          For more information, see Configuring ISDN PRI . For example, the basic
          configuration of a Primary Rate ISDN interface installed in NIM slot 2 of a device might
          include the following:

```
card type e1 0 2 
isdn switch-type primary-net5 
controller E1 0/2/0 
 pri-group timeslots 1-31
```

Configure the following TDM PSTN dial-peer:

```
dial-peer voice 200 pots 
 description Inbound/Outbound PRI PSTN trunk 
 destination-pattern BAD.BAD 
 translation-profile incoming 200 
 direct-inward-dial 
 port 0/2/0:15
```

Here's an explanation of the fields for the configuration:

```
dial-peer voice 200 pots description Inbound/Outbound PRI PSTN trunk
```

Defines
            a VoIP dial-peer with a tag of 200 and gives a meaningful description for ease of
            management and troubleshooting. For more information, see dial-peer voice .

A dummy
            destination pattern is required when routing outbound calls using an inbound dial-peer
            group. Any valid destination pattern may be used in this case. For more information, see destination-pattern (interface) .

Assigns
            the translation profile that will add a call routing tag to the incoming called number.

Routes the call without providing a
            secondary dial-tone. For more information, see direct-inward-dial .

The physical voice port associated with this
            dial-peer.

To enable media optimization of IP paths for Local Gateways with TDM-IP call flows, you
          can modify the call routing by introducing a set of internal loop-back dial-peers between
          Webex Calling and PSTN trunks. Configure the following loop-back dial-peers. In this case,
          all incoming calls will be routed initially to dial-peer 10 and from there to either
          dial-peer 11 or 12 based on the applied routing tag. After removal of the routing tag,
          calls will be routed to the outbound trunk using dial-peer groups.

```
dial-peer voice 10 voip
 description Outbound loop-around leg
 destination-pattern BAD.BAD
 session protocol sipv2
 session target ipv4:192.168.80.14
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw
 no vad 

dial-peer voice 11 voip
 description Inbound loop-around leg towards Webex
 translation-profile incoming 11
 session protocol sipv2
 incoming called-number A1AT
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw
 no vad 

dial-peer voice 12 voip
 description Inbound loop-around leg towards PSTN
 translation-profile incoming 12
 session protocol sipv2
 incoming called-number A2AT
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw 
 no vad
```

Here's an explanation of the fields for the configuration:

```
dial-peer voice 10 voip description Outbound loop-around leg
```

Defines a
            VoIP dial-peer and gives a meaningful description for ease of management and
            troubleshooting. For more information, see dial-peer voice .

Applies the
            translation profile defined earlier to remove the call routing tag before passing to the
            outbound trunk.

A
            dummy destination pattern is required when routing outbound calls using an inbound
            dial-peer group. For more information, see destination-pattern (interface) .

Specifies that this dial-peer
            handles SIP call legs. For more information, see session protocol (dial peer) .

Specifies
            the local router interface address as the call target to loop-back. For more
            information, see session target (voip dial
              peer) .

Configures the source
            interface and associated IP address for messages sent through the loop-back. For more
            information, see bind .

Configures the source
            interface and associated IP address for media sent through the loop-back. For more
            information, see bind .

Defines RTP-NTE (RFC2833) as the DTMF capability expected on the
            call leg. For more information, see DTMF Relay (Voice over
                IP) .

codec g711alaw

Forces all PSTN
            calls to use G.711. Select a-law or u-law to match the companding method used by your
            ISDN service.

Disables voice activity detection.
            For more information, see vad (dial peer) .

Add the following call routing configuration:

Create dial-peer groups to route calls between the PSTN and Webex trunks, via the
              loop-back.

```
voice class dpg 100
 description Route calls to Webex Calling
 dial-peer 100
voice class dpg 200
 description Route calls to PSTN
 dial-peer 200
voice class dpg 10
 description Route calls to Loopback
 dial-peer 10
```

Here's an explanation of the fields for the configuration:

Associates an outbound
                dial-peer with a dial-peer group. For more information, see voice-class dpg .

Apply dial-peer groups to route calls.

```
dial-peer voice 100
 destination dpg 10
dial-peer voice 200
 destination dpg 10
dial-peer voice 11
 destination dpg 100
dial-peer voice 12
 destination dpg 200
```

Here's an explanation of the fields for the
                configuration:

Specifies which dial-peer group, and therefore
                dial-peer should be used for the outbound treatment for calls presented to this
                incoming dial-peer.

This concludes your Local Gateway configuration. Save the configuration and reload the
          platform if this is the first time CUBE features are configured.

Configure Local Gateway with an existing Unified CM environment

The PSTN-Webex Calling configuration in the previous sections may be modified to
                include additional trunks to a Cisco Unified Communications Manager (UCM) cluster.
                In this case, all calls are routed via Unified CM. Calls from UCM on port 5060 are
                routed to the PSTN and calls from port 5065 are routed to Webex Calling. The
                following incremental configurations may be added to include this calling
                scenario.

When creating the Webex Calling trunk in Unified CM,
                    ensure that you configure the incoming port in the SIP Trunk Security Profile
                    settings to 5065. This allows incoming messages on port 5065 and populate the
                    VIA header with this value when sending messages to the Local Gateway.

Configure the following voice class URIs:

Classifies Unified CM to Webex calls using SIP VIA port:

```
voice class uri 300 sip
 pattern :5065
```

Classifies Unified CM to PSTN calls using SIP via port:

```
voice class uri 400 sip
 pattern 192\.168\.80\.6[0-5]:5060
```

Classify incoming messages from the UCM towards the PSTN trunk using
                                one or more patterns that describe the originating source addresses
                                and port number. Regular expressions may be used to define matching
                                patterns if required.

In the example above, a regular expression is used to match any IP
                                address in the range 192.168.80.60 to 65 and port number 5060.

Configure the following DNS records to specify SRV routing to Unified CM
                    hosts:

IOS XE uses these records for locally determining target UCM hosts and
                            ports. With this configuration, it is not required to configure records
                            in your DNS system. If you prefer to use your DNS, then these local
                            configurations are not required.

```
ip host ucmpub.mydomain.com 192.168.80.60
ip host ucmsub1.mydomain.com 192.168.80.61
ip host ucmsub2.mydomain.com 192.168.80.62
ip host ucmsub3.mydomain.com 192.168.80.63
ip host ucmsub4.mydomain.com 192.168.80.64
ip host ucmsub5.mydomain.com 192.168.80.65
ip host _sip._udp.wxtocucm.io srv 0 1 5065 ucmpub.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub1.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub2.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub3.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub4.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub5.mydomain.com
ip host _sip._udp.pstntocucm.io srv 0 1 5060 ucmpub.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub1.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub2.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub3.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub4.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub5.mydomain.com
```

Here's an explanation of the fields for the configuration:

The following command creates a DNS SRV resource record. Create a record for
                        each UCM host and trunk:

ip host _sip._udp.pstntocucm.io srv 2 1 5060
                                ucmsub5.mydomain.com

_sip._udp.pstntocucm.io : SRV resource record name

2 : The SRV resource record priority

1 : The SRV resource record weight

5060 : The port number to use for the target host in this resource
                        record

ucmsub5.mydomain.com : The resource record target host

To resolve the resource record target host names, create local DNS A records.
                        For example:

ip host ucmsub5.mydomain.com 192.168.80.65

ip host : Creates a record in the local IOS XE database.

ucmsub5.mydomain.com : The A record host name.

192.168.80.65 : The host IP address.

Create the SRV resource records and A records to reflect your UCM environment
                        and preferred call distribution strategy.

Configure the following dial-peers:

Dial-peer for calls between Unified CM and Webex Calling:

```
dial-peer voice 300 voip
 description UCM-Webex Calling trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target dns:wxtocucm.io
 incoming uri via 300
 voice-class codec 100
 voice-class sip bind control source-interface GigabitEthernet 0/0/0
 voice-class sip bind media source-interface GigabitEthernet 0/0/0
 dtmf-relay rtp-nte
 no vad
```

Here's an explanation of the fields for the
                                configuration:

```
dial-peer voice 300 voip description UCM-Webex Calling trunk
```

Defines
                                a VoIP dial-peer with a tag 300 and gives a meaningful
                                description for ease of management and
                                    troubleshooting.

A dummy destination pattern is required
                                when routing outbound calls using an inbound dial-peer group. Any
                                valid destination pattern may be used in this
                                    case.

Specifies that dial-peer 300 handles SIP call
                                legs. For more information, see session protocol
                                    (dial-peer) .

Defines the session target of
                                multiple Unified CM nodes through DNS SRV resolution. In this case,
                                the locally defined SRV record wxtocucm.io is used to direct
                                calls.

Uses
                                voice class URI 300 to direct all incoming traffic from Unified CM
                                using source port 5065 to this dial-peer. For more information,
                                    see incoming
                                    uri .

Indicates codec filter list for
                                calls to and from Unified CM. For more information, see voice class
                                    codec .

Configures the source interface and associated IP
                                address for messages sent to the PSTN. For more information,
                                    see bind .

Configures the
                                source interface and associated IP address for media sent to PSTN.
                                For more information, see bind .

Defines
                                RTP-NTE (RFC2833) as the DTMF capability expected on the call leg.
                                For more information, see DTMF Relay (Voice over
                                IP) .

Disables voice
                                activity detection. For more information, see vad (dial
                            peer) .

Dial-peer for calls between Unified CM and the PSTN:

```
dial-peer voice 400 voip
 description UCM-PSTN trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target dns:pstntocucm.io
 incoming uri via 400
 voice-class codec 100 
 voice-class sip bind control source-interface GigabitEthernet 0/0/0
 voice-class sip bind media source-interface GigabitEthernet 0/0/0
 dtmf-relay rtp-nte
 no vad
```

Here's an explanation of the fields for the
                                configuration:

```
dial-peer voice 400 voip description UCM-PSTN trunk
```

Defines
                                a VoIP dial-peer with a tag of 400 and gives a meaningful
                                description for ease of management and
                                    troubleshooting.

A dummy destination pattern is required
                                when routing outbound calls using an inbound dial-peer group. Any
                                valid destination pattern may be used in this
                                    case.

Specifies that dial-peer 400 handles SIP call
                                legs. For more information, see session protocol
                                    (dial-peer) .

Defines the session target of
                                multiple Unified CM nodes through DNS SRV resolution. In this case,
                                the locally defined SRV record pstntocucm.io is used to direct
                                calls.

Uses voice class URI 400 to direct
                                all incoming traffic from the specified Unified CM hosts using
                                source port 5060 to this dial-peer. For more information, see incoming
                                    uri .

Indicates codec filter list for
                                calls to and from Unified CM. For more information, see voice class
                                    codec .

Configures the source interface and associated IP
                                address for messages sent to the PSTN. For more information,
                                    see bind .

Configures the
                                source interface and associated IP address for media sent to PSTN.
                                For more information, see bind .

Defines
                                RTP-NTE (RFC2833) as the DTMF capability expected on the call leg.
                                For more information, see DTMF Relay (Voice over
                                IP) .

Disables voice
                                activity detection. For more information, see vad (dial
                            peer) .

Add call routing using the following configurations:

Create dial-peer groups to route calls between Unified CM and Webex
                            Calling. Define DPG 100 with outbound dial-peer
                                100 towards Webex Calling. DPG 100 is applied to the
                            associated incoming dial-peer from Unified CM. Similarly, define DPG 300
                            with outbound dial-peer 300 toward Unified CM. DPG 300 is applied to the
                            incoming dial-peer from Webex.

```
voice class dpg 100
 description Route calls to Webex Calling
 dial-peer 100
voice class dpg 300
 description Route calls to Unified CM Webex Calling trunk
 dial-peer 300
```

Create a dial-peer groups to route calls between Unified CM and the
                            PSTN. Define DPG 200 with outbound dial-peer
                                200 toward the PSTN. DPG 200 is applied to the
                            associated incoming dial-peer from Unified CM. Similarly, define DPG 400
                            with outbound dial-peer 400 toward Unified CM. DPG 400 is applied to the
                            incoming dial-peer from the PSTN.

```
voice class dpg 200
 description Route calls to PSTN
 dial-peer 200
voice class dpg 400
 description Route calls to Unified CM PSTN trunk
 dial-peer 400
```

Here's an explanation of the fields for the
                                configuration:

Associates
                                an outbound dial-peer with a dial-peer group. For more information,
                                    see voice-class dpg .

Apply dial-peer groups to route calls from Webex to Unified CM and from
                            Unified CM to Webex:

```
dial-peer voice 100
 destination dpg 300
dial-peer voice 300
 destination dpg 100
```

Here's an explanation of the fields for
                                the configuration:

Specifies which dial-peer group,
                                and therefore dial-peer should be used for the outbound treatment
                                for calls presented to this incoming dial-peer.

Apply dial-peer groups to route calls from the PSTN to Unified CM and
                            from Unified CM to the PSTN:

```
dial-peer voice 200
 destination dpg 400
dial-peer voice 400
 destination dpg 200
```

This concludes your Local Gateway configuration. Save the
                                configuration and reload the platform if this is the first time CUBE
                                features have been configured.

Monitor and troubleshoot Registration based Local Gateway with diagnostic
    signatures

Diagnostic Signatures (DS) proactively detects commonly observed issues in the IOS XE-based
        Local Gateway and generates email, syslog, or terminal message notification of the event.
        You can also install the DS to automate diagnostics data collection and transfer-collected
        data to the Cisco TAC case to accelerate resolution time.

Diagnostic Signatures (DS) are XML files that contain information about problem trigger
        events and actions to be taken to inform, troubleshoot, and remediate the issue. You can
        define the problem detection logic using syslog messages, SNMP events and through periodic
        monitoring of specific show command outputs.

The action types include collecting show command outputs:

Generating a consolidated log file

Uploading the file to a user-provided network location such as HTTPS, SCP, FTP
            server.

TAC engineers author the DS files and digitally sign it for integrity protection. Each DS
        file has a unique numerical ID assigned by the system. Diagnostic Signatures Lookup
          Tool (DSLT) is a single source to find applicable signatures for monitoring and
        troubleshooting various problems.

Before you begin:

Do not edit the DS file that you download from DSLT . The files that
            you modify fail installation due to the integrity check error.

A Simple Mail Transfer Protocol (SMTP) server you require for the Local Gateway to send
            out email notifications.

Ensure that the Local Gateway is running IOS XE 17.6.1 or higher if you wish to use the
            secure SMTP server for email notifications.

### Prerequisites

Local Gateway running IOS XE 17.6.1a or higher

Diagnostic Signatures is enabled by default.

Configure the secure email server to be used to send proactive notification if the
            device is running Cisco IOS XE 17.6.1a or higher.

```
configure terminal 
call-home  
mail-server <username>:<pwd>@<email server> priority 1 secure tls 
end
```

Configure the environment variable ds_email with the email address of the
            administrator to notify you.

```
configure terminal 
call-home  
diagnostic-signature 
environment ds_email <email address> 
end
```

The following shows an example configuration of a Local Gateway running on Cisco IOS XE
        17.6.1a or higher to send the proactive notifications to tacfaststart@gmail.com using Gmail as the secure SMTP server:

We recommend you to use the Cisco IOS XE Bengaluru 17.6.x or later versions.

```
call-home  
mail-server tacfaststart:password@smtp.gmail.com priority 1 secure tls 
diagnostic-signature 
environment ds_email "tacfaststart@gmail.com"
```

A Local Gateway running on Cisco IOS XE Software is not a typical web-based Gmail client
          that supports OAuth, so we must configure a specific Gmail account setting and provide
          specific permission to have the email from the device processed correctly:

Go to Manage Google Account > Security and turn on the Less secure app access setting.

Answer “Yes, it was me” when you receive an email from Gmail stating “Google prevented
            someone from signing into your account using a non-Google app.”

Install diagnostic signatures for proactive monitoring

Monitoring high CPU utilization

This DS tracks CPU utilization for five seconds using the SNMP OID 1.3.6.1.4.1.9.2.1.56.
        When the utilization reaches 75% or more, it disables all debugs and uninstalls all
        diagnostic signatures that are installed in the Local Gateway. Use these steps below to
        install the signature.

Use the show snmp command to enable SNMP. If you do not
            enable, then configure the snmp-server manager command.

```
show snmp 
%SNMP agent not enabled 

config t 
snmp-server manager 
end 

show snmp 
Chassis: ABCDEFGHIGK 
149655 SNMP packets input 
    0 Bad SNMP version errors 
    1 Unknown community name 
    0 Illegal operation for community name supplied 
    0 Encoding errors 
    37763 Number of requested variables 
    2 Number of altered variables 
    34560 Get-request PDUs 
    138 Get-next PDUs 
    2 Set-request PDUs 
    0 Input queue packet drops (Maximum queue size 1000) 
158277 SNMP packets output 
    0 Too big errors (Maximum packet size 1500) 
    20 No such name errors 
    0 Bad values errors 
    0 General errors 
    7998 Response PDUs 
    10280 Trap PDUs 
Packets currently in SNMP process input queue: 0 
SNMP global trap: enabled
```

Download DS 64224 using the following drop-down options in Diagnostic
              Signatures Lookup Tool :

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series

Product

CUBE Enterprise in Webex Calling Solution

Problem Scope

Performance

Problem Type

High CPU Utilization with Email Notification.

Copy the DS XML file to the Local Gateway flash.

```
LocalGateway# copy ftp://username:password@<server name or ip>/DS_64224.xml bootflash:
```

The following example shows copying the file from an FTP server to the Local Gateway.

```
copy ftp://user:pwd@192.0.2.12/DS_64224.xml bootflash: 
Accessing ftp://*:*@ 192.0.2.12/DS_64224.xml...! 
[OK - 3571/4096 bytes] 
3571 bytes copied in 0.064 secs (55797 bytes/sec)
```

Install the DS XML file in the Local Gateway.

```
call-home diagnostic-signature load DS_64224.xml 
Load file DS_64224.xml success
```

Use the show call-home diagnostic-signature command to verify
            that the signature is successfully installed. The status column should have a
            “registered” value.

```
show call-home diagnostic-signature  
Current diagnostic-signature settings: 
Diagnostic-signature: enabled 
Profile: CiscoTAC-1 (status: ACTIVE) 
Downloading  URL(s):  https://tools.cisco.com/its/service/oddce/services/DDCEService 
Environment variable: 
ds_email: username@gmail.com
```

Download DSes:

DS ID

DS Name

Revision

Status

Last Update (GMT+00:00)

64224

DS_LGW_CPU_MON75

0.0.10

Registered

2020-11-07 22:05:33

When triggered, this signature uninstalls all running DSs including itself. If
              necessary, reinstall DS 64224 to continue monitoring high CPU utilization on the Local
              Gateway.

Monitoring SIP trunk registration

This DS checks for unregistration of a Local Gateway SIP Trunk with Webex Calling cloud
        every 60 seconds. Once the unregistration event is detected, it generates an
        email and syslog notification and uninstalls itself after two unregistration
        occurrences. Use the steps below to install the signature:

Download DS 64117 using the following drop-down options in Diagnostic
              Signatures Lookup Tool :

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series

Product

CUBE Enterprise in Webex Calling Solution

Problem Scope

SIP-SIP

Problem Type

SIP Trunk Unregistration with Email Notification.

Copy the DS XML file to the Local Gateway.

```
copy ftp://username:password@<server name or ip>/DS_64117.xml bootflash:
```

Install the DS XML file in the Local Gateway.

```
call-home diagnostic-signature load DS_64117.xml 
Load file DS_64117.xml success 
LocalGateway#
```

Use the show call-home diagnostic-signature command to verify
            that the signature is successfully installed. The status column must have a “registered”
            value.

Monitoring abnormal call disconnects

This DS uses SNMP polling every 10 minutes to detect abnormal call disconnect with SIP
        errors 403, 488 and 503.  If the error count increment is greater than or equal to 5 from
        the last poll, it generates a syslog and email notification. Please use the steps below to
        install the signature.

Use the show snmp command to check whether SNMP is enabled.
            If it is not enabled, configure the snmp-server manager command.

```
show snmp 
%SNMP agent not enabled 
 

config t 
snmp-server manager 
end 

show snmp 
Chassis: ABCDEFGHIGK 
149655 SNMP packets input 
    0 Bad SNMP version errors 
    1 Unknown community name 
    0 Illegal operation for community name supplied 
    0 Encoding errors 
    37763 Number of requested variables 
    2 Number of altered variables 
    34560 Get-request PDUs 
    138 Get-next PDUs 
    2 Set-request PDUs 
    0 Input queue packet drops (Maximum queue size 1000) 
158277 SNMP packets output 
    0 Too big errors (Maximum packet size 1500) 
    20 No such name errors 
    0 Bad values errors 
    0 General errors 
    7998 Response PDUs 
    10280 Trap PDUs 
Packets currently in SNMP process input queue: 0 
SNMP global trap: enabled
```

Download DS 65221 using the following options in Diagnostic
              Signatures Lookup Tool :

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series

Product

CUBE Enterprise in Webex Calling Solution

Problem Scope

Performance

Problem Type

SIP abnormal call disconnect detection with Email and Syslog Notification.

Copy the DS XML file to the Local Gateway.

```
copy ftp://username:password@<server name or ip>/DS_65221.xml bootflash:
```

Install the DS XML file in the Local Gateway.

```
call-home diagnostic-signature load DS_65221.xml 
Load file DS_65221.xml success
```

Use the show call-home diagnostic-signature command to verify
            that the signature is successfully installed. The status column must have a “registered”
            value.

Install diagnostic signatures to troubleshoot a problem

Use Diagnostic Signatures (DS) to resolve issues quickly. Cisco TAC engineers have authored
        several signatures that enable the necessary debugs that are required to troubleshoot a
        given problem, detect the problem occurrence, collect the right set of diagnostic data and
        transfer the data automatically to the Cisco TAC case. Diagnostic Signatures (DS) eliminate
        the need to manually check for the problem occurrence and makes troubleshooting of
        intermittent and transient issues a lot easier.

You can use the Diagnostic Signatures Lookup Tool to find the applicable
        signatures and install them to self-solve a given issue or you can install the signature
        that is recommended by the TAC engineer as part of the support engagement.

Here is an example of how to find and install a DS to detect the occurrence
        “%VOICE_IEC-3-GW: CCAPI: Internal Error (call spike threshold): IEC=1.1.181.1.29.0" syslog
        and automate diagnostic data collection using the following steps:

Configure an additional DS environment variable ds_fsurl_prefix which is
            the Cisco TAC file server path (cxd.cisco.com) to which the collected diagnostics data
            are uploaded. The username in the file path is the case number and the password is the
            file upload token which can be retrieved from Support
              Case Manager in the following command. The file upload token can be generated
            in the Attachments section of the Support Case Manager, as needed.

```
configure terminal 
call-home  
diagnostic-signature 
LocalGateway(cfg-call-home-diag-sign)environment ds_fsurl_prefix "scp://<case number>:<file upload token>@cxd.cisco.com"  
end
```

Example:

```
call-home  
diagnostic-signature 
environment ds_fsurl_prefix " environment ds_fsurl_prefix "scp://612345678:abcdefghijklmnop@cxd.cisco.com"
```

Ensure that SNMP is enabled using the show snmp command. If
            it is not enabled, configure the snmp-server manager command.

```
show snmp 
%SNMP agent not enabled 
 
 
config t 
snmp-server manager 
end
```

Ensure to install the High CPU monitoring DS 64224 as a proactive measure to disable
            all debugs and diagnostics signatures during the time of high CPU utilization. Download
            DS 64224 using the following options in Diagnostic Signatures Lookup Tool :

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series

Product

CUBE Enterprise in Webex Calling Solution

Problem Scope

Performance

Problem Type

High CPU Utilization with Email Notification.

Download DS 65095 using the following options in Diagnostic
              Signatures Lookup Tool :

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series

Product

CUBE Enterprise in Webex Calling Solution

Problem Scope

Syslogs

Problem Type

Syslog - %VOICE_IEC-3-GW: CCAPI: Internal Error (Call spike threshold):
                      IEC=1.1.181.1.29.0

Copy the DS XML files to the Local Gateway.

```
copy ftp://username:password@<server name or ip>/DS_64224.xml bootflash: 
copy ftp://username:password@<server name or ip>/DS_65095.xml bootflash:
```

Install the High CPU monitoring DS 64224 and then DS 65095 XML file in the Local
            Gateway.

```
call-home diagnostic-signature load DS_64224.xml 
Load file DS_64224.xml success 
 
call-home diagnostic-signature load DS_65095.xml 
Load file DS_65095.xml success
```

Verify that the signature is successfully installed using the show
                call-home diagnostic-signature command. The status column must have a
            “registered” value.

```
show call-home diagnostic-signature  
Current diagnostic-signature settings: 
Diagnostic-signature: enabled 
Profile: CiscoTAC-1 (status: ACTIVE) 
Downloading  URL(s):  https://tools.cisco.com/its/service/oddce/services/DDCEService 
Environment variable: 
           ds_email: username@gmail.com 
           ds_fsurl_prefix: scp://612345678:abcdefghijklmnop@cxd.cisco.com
```

Downloaded DSes:

DS ID

DS Name

Revision

Status

Last Update (GMT+00:00)

64224

00:07:45

DS_LGW_CPU_MON75

0.0.10

Registered

2020-11-08

65095

00:12:53

DS_LGW_IEC_Call_spike_threshold

0.0.12

Registered

2020-11-08

Verify diagnostic signatures execution

In the following command, the “Status” column of the show call-home
            diagnostic-signature command changes to “running” while the Local Gateway
        executes the action defined within the signature. The output of show call-home
            diagnostic-signature statistics is the best way to verify whether a
        diagnostic signature detects an event of interest and executes the action. The
        “Triggered/Max/Deinstall” column indicates the number of times the given signature has
        triggered an event, the maximum number of times it is defined to detect an event and whether
        the signature deinstalls itself after detecting the maximum number of triggered events.

```
show call-home diagnostic-signature  
Current diagnostic-signature settings: 
Diagnostic-signature: enabled 
Profile: CiscoTAC-1 (status: ACTIVE) 
Downloading  URL(s):  https://tools.cisco.com/its/service/oddce/services/DDCEService 
Environment variable: 
           ds_email: carunach@cisco.com 
           ds_fsurl_prefix: scp://612345678:abcdefghijklmnop@cxd.cisco.com
```

Downloaded DSes:

DS ID

DS Name

Revision

Status

Last Update (GMT+00:00)

DS_LGW_CPU_MON75

0.0.10

Registered

2020-11-08 00:07:45

65095

DS_LGW_IEC_Call_spike_threshold

0.0.12

Running

2020-11-08 00:12:53

show call-home diagnostic-signature statistics

DS ID

DS Name

Triggered /Max/Deinstall

Average Run Time (seconds)

Max Run Time (seconds)

DS_LGW_CPU_MON75

0/0/N

0.000

0.000

65095

DS_LGW_IEC_Call_spike_threshold

1 /20/Y

23.053

23.053

The notification email that is sent during diagnostic signature execution contains key
        information such as issue type, device details, software version, running configuration, and
        show command outputs that are relevant to troubleshoot the given problem.

Uninstall diagnostic signatures

Use Diagnostic signatures for troubleshooting purposes are typically defined to uninstall
        after detection of some problem occurrences. If you want to uninstall a signature manually,
        retrieve the DS ID from the output of the show call-home
            diagnostic-signature command and run the following command:

```
call-home diagnostic-signature deinstall <DS ID>
```

Example:

```
call-home diagnostic-signature deinstall 64224
```

New signatures are added to Diagnostics Signatures Lookup Tool periodically, based on
          issues that are commonly observed in deployments. TAC currently doesn’t support requests
          to create new custom signatures.

Manage and validate Cisco IOS XE Gateways through Control Hub

For better management of Cisco IOS XE Gateways, we recommend that you enroll and
                manage the gateways through the Control Hub. It is an optional configuration. When
                enrolled, you can use the configuration validation option in the Control Hub to
                validate your Local Gateway configuration and identify any configuration issues.
                Currently, only registration-based trunks support this functionality.

For more information on gateway management, Local Gateway validation, and site
                survivability, see the following articles:

Design overview

This section describes how to configure a Cisco Unified Border Element (CUBE) as a Local
            Gateway for Webex Calling using a certificate-based, mutual TLS (mTLS) SIP trunk. The
            first part of this document illustrates how to configure a simple PSTN gateway. In this
            case, all calls from the PSTN are routed to Webex Calling and all calls from Webex
            Calling are routed to the PSTN. The following image highlights this solution and the
            high-level call routing configuration that will be followed.

In this design, the following principal configurations are used:

voice class tenants : Used to create trunk specific configurations.

voice class uri : Used to classify SIP messages for the selection of an
                    inbound dial-peer.

inbound dial-peer : Provides treatment for inbound SIP messages and
                    determines the outbound route using a dial-peer group.

dial-peer group : Defines the outbound dial-peers used for onward call
                    routing.

outbound dial-peer : Provides treatment for outbound SIP messages and
                    routes them to the required target.

For Webex Calling media optimization with Interactive Connectivity Establishment (ICE) and TDM (Time Division Multiplexing) ISDN circuits, it's necessary to use a two-leg call
            routing process.

While IP and SIP have become the default protocols for PSTN trunks, TDM (Time
            Division Multiplexing) ISDN circuits remain common and are fully supported by Webex
            Calling. To enable media optimization for these TDM-IP call flows, you must use
            Interactive Connectivity Establishment (ICE), which allows endpoints to negotiate direct
            media paths.

Achieving this optimization requires a two-leg call routing process. This approach
            modifies the standard routing configuration by introducing a set of internal loop-back
            dial-peers between Webex Calling and PSTN trunks, as illustrated in the image below.

When connecting an on-premises Cisco Unified Communications Manager solution with Webex
            Calling, you can use the simple PSTN gateway configuration as a baseline for building
            the solution illustrated in the following diagram. In this case, a Unified
            Communications Manager provides centralized routing and treatment of all PSTN and Webex
            Calling calls.

Throughout this document, the host names, IP addresses, and interfaces illustrated in the
            following image are used. Options are provided for public or private (behind NAT)
            addressing. SRV DNS records are optional, unless load balancing across multiple CUBE
            instances.

Use the configuration guidance in the rest of this document to complete your Local
            Gateway configuration as follows:

Step 1: Configure router baseline connectivity and security

Step 2: Configure Webex Calling Trunk

Depending on your required architecture, follow either:

Step 3: Configure Local Gateway with SIP PSTN trunk

Step 4: Configure Local Gateway with an existing Unified CM environment

Or:

Step 3: Configure Local Gateway with TDM PSTN trunk

Configure connectivity and security

### Baseline configuration

The first step in preparing your Cisco router as a Local Gateway for Webex Calling is to
      build a baseline configuration that secures your platform and establishes connectivity.

All certificate-based Local Gateway deployments require Cisco IOS XE 17.9.1a or later
          versions. Cisco IOS XE 17.12.2 or later is recommended. For the recommended versions, see
          the Cisco Software Research page. Search for the platform and select one of the suggested releases.

ISR4000 series routers must be configured with both Unified Communications and
              Security technology licenses.

Catalyst Edge 8000 series routers fitted with voice cards or DSPs require DNA
              Advantage licensing. Routers without voice cards or DSPs require a minimum of DNA
              Essentials licensing.

For high-capacity requirements, you may also require a High Security (HSEC) license
              and additional throughput entitlement.

Refer to Authorization Codes for further details.

Build a baseline configuration for your platform that follows your business policies. In
          particular, configure and verify the following:

NTP

ACLs

User authentication and remote access

DNS

IP routing

IP addresses

The network toward Webex Calling must use an IPv4 address. Local Gateway Fully Qualified
          Domain Names (FQDN) or Service Record (SRV) addresses configured in the Control Hub must
          resolve to a public IPv4 address on the internet.

All SIP and media ports on the Local Gateway interface facing Webex must be accessible
          from the internet, either directly or via static NAT. Ensure that you update your firewall
          accordingly.

Follow the detailed configuration steps provided below to install a signed certificate on
          the Local Gateway:

A public Certificate Authority (CA) as detailed in What Root Certificate Authorities are Supported for Calls to Cisco
                Webex Audio and Video Platforms? must sign the device certificate.

Certificates containing only Server Authentication Extended Key Usage (EKU) are
              supported. Webex Calling does not validate or enforce the presence of Client Authentication EKU during TLS
              handshake establishment.

Some third-party Session Border Controllers (SBC) may enforce strict EKU
                  validation and could reject certificates that do not include Client Authentication
                  EKU. In such cases, ensure the SBC is configured to accept certificates with
                  Server Authentication EKU only or to disable strict EKU validation (if
                  supported).

The certificate subject Common Name (CN), or one of the Subject Alternative Names
              (SAN) must be the same as the FQDN configured in the Control Hub.

When purchasing a certificate with Common Name (CN) or Subject Alternative Name
                (SAN), ensure that the certificate uses only lowercase letters. In Control Hub
                configuration, all FQDN entries are automatically converted to lowercase, and any
                mismatch in letter casing between the FQDN and the certificate will prevent
                successful trunk registration.

For example:

If a configured trunk in the Control Hub of your organization has
                  cube1.lgw.com:5061 as FQDN of the Local Gateway, then the CN or SAN in the router
                  certificate must contain cube1.lgw.com.

If a configured trunk in the Control Hub of your organization has lgws.lgw.com as
                  the SRV address of the Local Gateway(s) reachable from the trunk, then the CN or
                  SAN in the router certificate must contain lgws.lgw.com. The records that the SRV
                  address resolves to (CNAME, A Record, or IP Address) are optional in SAN.

Whether you use an FQDN or SRV for the trunk, the contact address for all new SIP
                  dialogs from your Local Gateway must use the name configured in the Control
                  Hub.

Upload the Cisco root CA bundle to the Local Gateway. This bundle includes the CA root
          certificate used to verify the Webex platform.

### Configuration

Ensure that you assign valid and routable IP addresses to any Layer 3 interfaces, for
          example:

```
interface GigabitEthernet0/0/0
 description Interface facing PSTN and/or CUCM
 ip address 192.168.80.14 255.255.255.0
!
interface GigabitEthernet0/0/1
 description Interface facing Webex Calling (Public address)
 ip address 198.51.100.1 255.255.255.240
```

Protect STUN credentials on the router using symmetric encryption. Configure the
          primary encryption key and encryption type as follows:

```
key config-key password-encrypt YourPassword
password encryption aes
```

Create an encryption trustpoint with a certificate for your domain, signed by a supported Certificate Authority (CA).

Create an RSA key pair using the following exec command.

```
crypto key generate rsa general-keys exportable label lgw-key modulus 4096
```

Use the following configuration commands to create a trustpoint for the
              certificate, specifying the field values to use in the certificate signing request:

```
crypto pki trustpoint LGW_CERT
 enrollment terminal pem
 fqdn none
 subject-name cn=cube1.lgw.com
 subject-alt-name cube1.lgw.com
 revocation-check none
 rsakeypair lgw-key
 hash sha256
```

Notes for certificate fields:

fqdn : This isn’t a required field for Webex Calling. Setting this
                    configuration to "none" to not include this field in the Certificate Signing
                    Request. If you need to include an FQDN using this command, there is no impact
                    on the Local Gateway operation.

subject-name : For validating calls from a Local Gateway, Webex must
                    match the FQDN in SIP contact headers with those included either in the Subject
                    Common Name (CN) attribute or the Subject Alternative Name (SAN) field of the
                    SBC certificate. The subject field must contain at least a CN attribute, and can
                    include other attributes, as required. For more information, see subject-name .

Subject-alt-name : The Subject Alternative Name (SAN) field of the SBC
                    certificate can include a list of additional FQDNs. Webex checks this list to
                    validate the SIP contact header in messages from the Local Gateway if the
                    certificate Subject CN attribute is not matched.

Hash : It’s recommended that Certificate Signing Request (CSR)s are
                    signed using SHA256. The Cisco IOS XE 17.11.1 uses this algorithm by default and
                    for earlier release, use the Hash command.

Generate Certificate Signing Request (CSR) with the following exec or configuration
              command and use it to request a signed certificate from a supported CA provider:

```
crypto pki enroll LGW_CERT
```

Provide the certificate of the intermediate signing CA to authenticate your host
          certificate. Enter the following exec or configuration command:

```
crypto pki authenticate LGW_CERT
<paste Intermediate X.509 base 64 based certificate here>
```

Import the signed host certificate using the following exec or configuration
          command:

```
crypto pki import LGW_CERT certificate
<paste CUBE host X.509 base 64 certificate here>
```

Enable TLS1.2 exclusivity and specify the default trustpoint to use for voice
          applications using the following configuration commands:

```
sip-ua
  crypto signaling default trustpoint LGW_CERT
  transport tcp tls v1.2
```

Install the Cisco root CA bundle, which includes the IdenTrust Commercial Root CA 1
          certificate used by Webex Calling. Use the crypto pki trustpool import clean
              url url command to download the root CA bundle from the
          specified URL, and to clear the current CA trustpool, then install the new bundle of
          certificates:

If you need to use a proxy for access to the internet using
              HTTPS, add the following configuration before importing the CA bundle:

```
ip http client source-interface GigabitEthernet0/0/1 
crypto pki trustpool import clean url https://www.cisco.com/security/pki/trs/ios_core.p7b
```

Configure Webex Calling certificate-based trunk

Create a CUBE certificate-based PSTN trunk for an existing location in the
                    Control Hub. For more information, see Configure trunks, route groups, and dial
                        plans for Webex Calling .

Make a note of the trunk information on creating the trunk. These
                            details, as highlighted in the following illustration is used in the
                            configuration steps in this guide.

Enter the following commands to configure CUBE as a Webex Calling Local
                    Gateway:

```
voice service voip
 ip address trusted list
  ipv4 x.x.x.x y.y.y.y
 mode border-element
 allow-connections sip to sip
 no supplementary-service sip refer
 stun
  stun flowdata agent-id 1 boot-count 4
  stun flowdata shared-secret 0 Password123$
 sip 
  asymmetric payload full
  early-offer forced
  sip-profiles inbound
```

Here's an explanation of the fields for the configuration:

```
ip address trusted list ipv4 x.x.x.x y.y.y.y
```

To protect against toll fraud, the trusted address list defines a list of hosts and network entities from which the Local Gateway expects legitimate VoIP calls.

By default, a Local Gateway blocks all incoming VoIP messages from IP addresses not in its trusted list. By default, statically configured dial-peers with “session target IP” or server group IP addresses are trusted. You need not add these IP addresses to the trusted list.

When configuring your Local Gateway, add the IP subnets for your regional Webex Calling data center to the list, see Port Reference Information for Webex Calling for more information. Also, add address ranges for Unified Communications Manager servers (if used) and PSTN trunk gateways.

For more information on how to use an IP address trusted list to prevent toll fraud, see IP address trusted .

Enables Cisco Unified Border Element (CUBE) features on the platform.

Enable CUBE basic SIP back to back user agent functionality. For more information, see Allow connections .

By default, T.38 fax transport is enabled. For more information, see fax protocol t38 (voice-service) .

Enables STUN (Session Traversal of UDP through NAT) globally.

These global stun commands are only required when deploying your Local Gateway behind NAT.

The STUN bindings feature on the Local Gateway allows locally generated STUN requests to be sent over the negotiated media path. This helps to open the pinhole in the firewall.

For more information, see stun flowdata agent-id and stun flowdata shared-secret .

Configures SIP asymmetric payload support for both DTMF and dynamic codec payloads. For more information on this command, see asymmetric payload .

Forces the Local Gateway to send SDP information in the initial INVITE message instead of waiting for acknowledgment from the neighboring peer. For more information on this command, see early-offer .

Enables CUBE to use SIP profiles to modify messages as they are received. Profiles are applied through dial-peers or tenants.

Configure voice class codec 100 allowing G.711 codecs only for all trunks. This simple approach is suitable for most deployments. If necessary, add additional codec types supported by both originating and terminating systems to the list.

More complex solutions involving transcoding using DSP modules are supported, but not included in this guide.

```
voice class codec 100
 codec preference 1 g711ulaw
 codec preference 2 g711alaw
```

Here's an explanation of the fields for the configuration:

Used to only allow preferred codecs for SIP trunk calls. For more information, see voice class codec .

Configure voice class stun-usage 100 to
                    enable ICE on the Webex Calling trunk. (This step is not applicable for Webex
                        for Government)

```
voice class stun-usage 100 
 stun usage firewall-traversal flowdata
 stun usage ice lite
```

Here's an explanation of the fields for the
                            configuration:

Used
                        to enable ICE-Lite for all Webex Calling facing dial-peers to allow
                        media-optimization whenever possible. For more information, see voice class stun usage and stun usage ice lite .

The stun usage firewall-traversal
                            flowdata command is only required when deploying your
                            Local Gateway behind NAT.

Media optimization is negotiated wherever possible. If a call requires
                            cloud media services, such as recording, the media cannot be
                            optimized.

Configure the media encryption policy for Webex traffic. (This step is not
                        applicable for Webex for Government)

```
voice class srtp-crypto 100
 crypto 1 AES_CM_128_HMAC_SHA1_80
```

Here's an explanation of the fields
                        for the configuration:

Specifies SHA1_80 as the only SRTP
                        cipher-suite CUBE offers in the SDP in offer and answer messages. Webex
                        Calling only supports SHA1_80. For more information, see voice class
                    srtp-crypto .

Configure FIPS-compliant GCM ciphers (This step is applicable only for Webex
                        for Government) .

```
voice class srtp-crypto 100
crypto 1 AEAD_AES_256_GCM
```

Here's an explanation of the fields for the
                            configuration:

Specifies GCM as the cipher-suite that
                        CUBE offers. It is mandatory to configure GCM ciphers for Local Gateway for
                        Webex for Government.

Configure a pattern to uniquely identify calls to a Local Gateway trunk based
                    on its destination FQDN or SRV:

```
voice class uri 100 sip
 pattern cube1.lgw.com
```

Here's an explanation of the fields for the configuration:

Defines a pattern to match an incoming SIP invite to an incoming trunk dial-peer. When entering this pattern, use the trunk FQDN or SRV configured in the Control Hub for the trunk.

During tenant-side configuration of certificate-based trunks for Webex
                            Calling, use only SRV-based Webex Calling Edge address on the Local
                            Gateway. FQDNs are no longer supported.

Configure SIP message manipulation profiles. If your gateway is configured with
                    a public IP address, configure a profile as follows or skip to the next step if
                    you are using NAT. In this example, cube1.lgw.com is the FQDN configured for the
                    Local Gateway:

```
voice class sip-profiles 100
 rule 10 request ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:" 
 rule 20 response ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:"
```

Here's an explanation of the fields for the
                        configuration:

To allow Webex to authenticate
                        messages from your local gateway, the 'Contact' header in a SIP request and
                        responses messages must contain the value provisioned for the trunk in the
                        Control Hub. This will either be the FQDN of a single host, or the SRV name
                        used for a cluster of devices.

If your gateway is configured with a private IP address behind static NAT,
                    configure the inbound and outbound SIP profiles as follows. In this example,
                    cube1.lgw.com is the FQDN configured for the Local Gateway, "10.80.13.12" is the
                    interface IP address facing Webex Calling and "192.65.79.20" is the NAT public
                    IP address.

```
voice class sip-profiles 100
 rule 10 request ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:"
 rule 20 response ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:"
 rule 30 response ANY sdp-header Audio-Attribute modify "(a=candidate:1 1.*) 10.80.13.12" "\1 192.65.79.20"
 rule 31 response ANY sdp-header Audio-Attribute modify "(a=candidate:1 2.*) 10.80.13.12" "\1 192.65.79.20"
 rule 40 response ANY sdp-header Audio-Connection-Info modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 41 request ANY sdp-header Audio-Connection-Info modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 50 request ANY sdp-header Connection-Info modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 51 response ANY sdp-header Connection-Info modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 60 response ANY sdp-header Session-Owner modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 61 request ANY sdp-header Session-Owner modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 70 request ANY sdp-header Audio-Attribute modify "(a=rtcp:.*) 10.80.13.12" "\1 192.65.79.20"
 rule 71 response ANY sdp-header Audio-Attribute modify "(a=rtcp:.*) 10.80.13.12" "\1 192.65.79.20"
 rule 80 request ANY sdp-header Audio-Attribute modify "(a=candidate:1 1.*) 10.80.13.12" "\1 192.65.79.20"
 rule 81 request ANY sdp-header Audio-Attribute modify "(a=candidate:1 2.*) 10.80.13.12" "\1 192.65.79.20"
```

Here's
                        an explanation of the fields for the configuration:

To allow Webex to authenticate messages from your
                        local gateway, the 'Contact' header in SIP request and responses messages
                        must contain the value provisioned for the trunk in the Control Hub. This
                        will either be the FQDN of a single host, or the SRV name used for a cluster
                        of devices.

Convert private
                        address references to the external public address for the site, allowing
                        Webex to correctly interpret and route subsequent messages.

```
voice class sip-profiles 110
 rule 10 response ANY sdp-header Video-Connection-Info modify "192.65.79.20" "10.80.13.12"
 rule 20 response ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:"
 rule 30 response ANY sdp-header Connection-Info modify "192.65.79.20" "10.80.13.12"
 rule 40 response ANY sdp-header Audio-Connection-Info modify "192.65.79.20" "10.80.13.12"
 rule 50 response ANY sdp-header Session-Owner modify "192.65.79.20" "10.80.13.12"
 rule 60 response ANY sdp-header Audio-Attribute modify "(a=candidate:1 1.*) 192.65.79.20" "\1 10.80.13.12"
 rule 70 response ANY sdp-header Audio-Attribute modify "(a=candidate:1 2.*) 192.65.79.20" "\1 10.80.13.12"
 rule 80 response ANY sdp-header Audio-Attribute modify "(a=rtcp:.*) 192.65.79.20" "\1 10.80.13.12"
```

Here's
                        an explanation of the fields for the configuration:

Convert public address references to the
                        configured private address, allowing CUBE to process the messages from
                        Webex.

For more information, see voice class sip-profiles .

United States or Canadian PSTN provider can offer the Caller ID
                            verification for Spam and fraud calls, with the additional configuration
                            mentioned in the Spam or fraud call indication in
                                Webex Calling article.

Configure a SIP Options keepalive with header modification profile.

```
voice class sip-profiles 115
 rule 10 request OPTIONS sip-header Contact modify "<sip:.*:" "<sip:cube1.lgw.com:" 
 rule 30 request ANY sip-header Via modify "(SIP.*) 10.80.13.12" "\1 192.65.79.20"
 rule 40 response ANY sdp-header Connection-Info modify "10.80.13.12" "192.65.79.20"  
 rule 50 response ANY sdp-header Audio-Connection-Info modify "10.80.13.12" "192.65.79.20"
!
voice class sip-options-keepalive 100
 description Keepalive for Webex Calling
 up-interval 5
 transport tcp tls
 sip-profiles 115
```

Here's an explanation of the fields for the
                        configuration:

Configures a keepalive profile and enters
                        voice class configuration mode. You can configure the time (in seconds) at
                        which an SIP Out of Dialog Options Ping is sent to the dial-target when the
                        heartbeat connection to the endpoint is in UP or Down status.

This
                        keepalive profile is triggered from the dial-peer configured towards Webex.

To ensure that the contact headers include the SBC fully qualified
                        domain name, SIP profile 115 is used. Rules 30, 40, and 50 are required only
                        when the SBC is configured behind static NAT.

In this example,
                        cube1.lgw.com is the FQDN selected for the Local Gateway and if static NAT
                        is used, "10.80.13.12" is the SBC interface IP address towards Webex Calling
                        and "192.65.79.20" is the NAT public IP address.

Configure Webex Calling trunk:

Create voice class tenant 100 to
                            define and group configurations required specifically for the Webex
                            Calling trunk. Dial-peers associated with this tenant later inherits
                            these configurations:

The following example uses the values illustrated in Step 1 for the purpose of this guide (shown in bold). Replace these with values for your trunk in your configuration.

```
voice class tenant 100
 no remote-party-id
 sip-server dns:us25.sipconnect.bcld.webex.com
 srtp-crypto 100
 localhost dns:cube1.lgw.com
 session transport tcp tls
 no session refresh
 error-passthru
 rel1xx disable
 asserted-id pai
 bind control source-interface GigabitEthernet0/0/1
 bind media source-interface GigabitEthernet0/0/1
 no pass-thru content custom-sdp
 sip-profiles 100 
 sip-profiles 110 inbound
 privacy-policy passthru
!
```

Here's an explanation of the fields for the configuration:

We recommend that you use tenants to configure trunks, which have their own TLS certificate, and CN or SAN validation list. Here, the tls-profile associated with the tenant contains the trust point to be used to accept or create new connections, and has the CN or SAN list to validate the incoming connections. For more information, see voice class tenant .

Disable the SIP Remote-Party-ID (RPID) header as Webex Calling supports PAI, which is enabled using a asserted-id pai command. For more information, see remote-party-id .

Configures the target SIP server for the trunk. Use the Edge proxy SRV address provided in the Control Hub when you created your trunk

Configures the preferred cipher-suites for the SRTP call leg (connection) (specified in Step 5). For more information, see voice class srtp-crypto .

Configures CUBE to replace the physical IP address in the From, Call-ID, and Remote-Party-ID headers in outgoing messages with the provided FQDN. Use the trunk FQDN or SRV configured in the Control Hub for the trunk here.

Sets transport to TLS for associated dial-peers. For more information, see session-transport .

Disables SIP session refresh for calls between CUBE and Webex. For more information, see session refresh .

Specifies SIP error response pass-thru functionality. For more information, see error-passthru .

Disables the use of
                                reliable provisional responses for the Webex Calling trunk. For more
                                information, see rel1xx .

(Optional) Turns on P-Asserted-Identity header
                                processing and controls how this is used for the Webex Calling
                                trunk.

Webex Calling includes P-Asserted-Identity (PAI)
                                headers in outbound call INVITEs to the Local Gateway.

If
                                this command is configured, caller information from the PAI header
                                is used to populate the outgoing From and PAI/Remote-Party-ID
                                headers.

If this command is not configured, caller
                                information from the From header is used to populate the outgoing
                                From and PAI/Remote-Party-ID headers.

For more information,
                                see asserted-id .

Configures the
                                source interface and associated IP address for messages sent to
                                Webex Calling. For more information, see bind .

Configures the
                                source interface and associated IP address for media sent to Webex
                                Calling. For more information, see bind .

Applies the header modification profile
                                (Public IP or NAT addressing) to use for outbound messages. For more
                                information, see voice-class sip
                                profiles .

For LGW deployments behind NAT only: Applies the
                                header modification profile to use for inbound messages. For more
                                information, see voice-class sip
                                    profiles.

Configures CUBE to
                                transparently pass privacy headers from the received message to the
                                next call leg. For more information, see privacy-policy .

Configure the Webex Calling trunk dial-peer.

```
dial-peer voice 100 voip
 description Inbound/Outbound Webex Calling
 destination-pattern BAD.BAD
 session protocol sipv2
 session target sip-server
 incoming uri request 100
 voice-class codec 100
 voice-class stun-usage 100
 voice-class sip tenant 100
 voice-class sip options-keepalive profile 100
 dtmf-relay rtp-nte 
 srtp
 no vad
```

Here's an explanation of the fields for the configuration:

```
dial-peer voice 100 voip description Inbound/Outbound Webex Calling
```

Defines a VoIP dial-peer with a tag of 100 and gives a meaningful description for ease of management and troubleshooting. For more information, see dial-peer voice .

A dummy destination pattern is required when routing outbound calls using an inbound dial-peer group. You can use any valid destination pattern in this case. For more information, see destination-pattern (interface) .

Specifies that this dial-peer handles SIP call legs. For more information, see session protocol (dial-peer) .

Indicates that the SIP server defined in tenant 100 is inherited and used for the destination for calls from this dial peer.

Specifies the voice class used to match incoming calls to this dial-peer using the INVITE REQUEST header URI. For more information, see incoming uri .

Indicates codec filter list for calls to and from Webex Calling. For more information, see voice class codec .

Allows locally generated STUN requests from the Local Gateway to be sent over the negotiated media path. STUN packets help to open a firewall pinhole for media traffic and detect valid paths for media optimization.

The dial-peer inherits all parameters configured globally and in tenant 100. Parameters may overridden at the dial-peer level. For more information, see voice-class sip tenant .

This command monitors the availability of a group of SIP servers or endpoints using a specific profile (100).

Enables SRTP for the call leg.

(Optional)  Force calls to audio only.

Video over Webex Calling using Local Gateway call flows is not
                                supported. Although video can function in some scenarios, it can
                                result in degraded quality and unexpected behavior. To force calls
                                to audio only, apply the following command under your Webex Calling
                                dial-peers:

```
voice-class sip audio forced
```

If you choose to allow video, calls may not perform as expected.

(Optional) To configure network devices such as CUBE and to forward Session
                    Initiation Protocol (SIP) headers that the device doesn't process, use these
                    commands. These commands enable the device to pass through unsupported SIP
                    headers, including geo-location headers and PIDF-LO (Presence Information Data
                    Format - Location Object), on the local gateway. This functionality supports
                    Nomadic E-911 services by ensuring that critical location information is
                    preserved and forwarded correctly.

Dial peer Configuration

```
Voice service voip
 sip
  pass-thru headers unsupp
```

Dial-peer specific configuration

```
Dial-peer voice 911 voip
 voice-class sip pass-thru headers unsupp
```

Voice Class configuration for specific headers

To proxy the Geo location headers:

```
voice class sip-hdr-passthrulist 200 
 passthru-hdr Geolocation-Routing
 passthru-hdr Geolocation
 passthru-hdr-unsupp
```

Apply the pass-through to the inbound/outbound dial-peer

```
dial-peer voice 100 voip  // inbound
 voice-class sip pass-thru headers 200
dial-peer voice 200 voip  // outbound
 voice-class sip pass-thru headers 200
```

To enable the pass-through of the PIDFO body, use:

```
voice service voip 
 sip 
  pass-thru content unsupp
```

Configure Local Gateway with a SIP PSTN trunk

Having built a trunk towards Webex Calling above, use the following configuration to
                create a non-encrypted trunk towards a SIP based PSTN provider:

If your Service Provider offers a secure PSTN trunk, you may follow a similar
                    configuration as detailed above for the Webex Calling trunk. CUBE supports
                    secure call routing.

If you are using a TDM / ISDN PSTN trunk, skip to the next section Configure Local Gateway with TDM PSTN trunk .

To configure TDM interfaces for PSTN call legs on the Cisco TDM-SIP Gateways,
                        see Configuring ISDN PRI .

Configure the following voice class uri to identify inbound calls from the PSTN
                    trunk:

```
voice class uri 200 sip
  host ipv4:192.168.80.13
```

Here's an explanation of the fields for the configuration:

Defines a
                        pattern to match an incoming SIP invite to an incoming trunk dial-peer. When
                        entering this pattern, use the IP address of your IP PSTN gateway. For more
                        information, see voice class uri .

Configure the following IP PSTN dial-peer:

```
dial-peer voice 200 voip
 description Inbound/Outbound IP PSTN trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target ipv4:192.168.80.13
 incoming uri via 200
 voice-class sip asserted-id pai
 voice-class sip bind control source-interface GigabitEthernet0/0/0 
 voice-class sip bind media source-interface  GigabitEthernet0/0/0 
 voice-class codec 100
 dtmf-relay rtp-nte 
 no vad
```

Here's an explanation of the fields for the
                        configuration:

```
dial-peer voice 200 voip description Inbound/Outbound IP PSTN trunk
```

Defines
                        a VoIP dial-peer with a tag of 200 and gives a meaningful description
                        for ease of management and troubleshooting. For more information, see dial-peer
                            voice.

A dummy destination pattern is
                        required when routing outbound calls using an inbound dial-peer group. Any
                        valid destination pattern may be used in this case. For more information,
                        see destination-pattern
                        (interface) .

Specifies that this dial-peer handles SIP call legs.
                        For more information, see session protocol (dial
                            peer) .

Specifies the target
                        address for calls sent to the PSTN provider. This could be either an IP
                        address or DNS host name. For more information, see session target (VoIP dial
                        peer) .

Specifies the voice class used to match
                        incoming calls to this dial-peer using the INVITE VIA header URI. For more
                        information, see incoming url .

(Optional) Turns
                        on P-Asserted-Identity header processing and controls how this is used for
                        the PSTN trunk. If this command is used, the calling party identity provided
                        from the incoming dial-peer is used for the outgoing From and
                        P-Asserted-Identity headers. If this command is not used, the calling party
                        identity provided from the incoming dial-peer is used for the outgoing From
                        and Remote-Party-ID headers. For more information, see voice-class sip
                    asserted-id .

Configures
                        the source interface and associated IP address for messages sent to the
                        PSTN. For more information, see bind .

Configures
                        the source interface and associated IP address for media sent to PSTN. For
                        more information, see bind .

Configures the dial-peer to use the
                        common codec filter list 100 . For more information, see voice-class
                            codec .

Defines
                        RTP-NTE (RFC2833) as the DTMF capability expected on the call leg. For more
                        information, see DTMF Relay (Voice over
                            IP) .

Disables voice
                        activity detection. For more information, see vad (dial peer) .

If you are configuring your Local Gateway to only route calls between Webex
                    Calling and the PSTN, add the following call routing configuration. If you are
                    configuring your Local Gateway with a Unified Communications Manager platform,
                    skip to the next section.

Create dial-peer groups to route calls towards Webex Calling or the
                            PSTN. Define DPG 100 with outbound dial-peer 100 toward Webex Calling.
                            DPG 100 is applied to the incoming dial-peer from the PSTN. Similarly,
                            define DPG 200 with outbound dial-peer 200 toward the PSTN. DPG 200 is
                            applied to the incoming dial-peer from Webex.

```
voice class dpg 100 
 description Route calls to Webex Calling 
 dial-peer 100 
voice class dpg 200 
 description Route calls to PSTN 
 dial-peer 200
```

Here's an explanation of the fields for the
                                configuration:

Associates an outbound dial-peer with
                                a dial-peer group. For more information, see voice-class
                            dpg .

Apply dial-peer groups to route calls from Webex to the PSTN and from
                            the PSTN to Webex:

```
dial-peer voice 100
 destination dpg 200
dial-peer voice 200
 destination dpg 100
```

Here's an explanation of the fields for
                                the configuration:

Specifies which dial-peer group,
                                and therefore dial-peer should be used for the outbound treatment
                                for calls presented to this incoming dial-peer.

This
                                concludes your Local Gateway configuration. Save the configuration
                                and reload the platform if this is the first time CUBE features are
                                configured.

Configure Local Gateway with a TDM PSTN trunk

Having built a trunk towards Webex Calling, use the following configuration to create a TDM
        trunk for your PSTN service with loop-back call routing to allow media optimization on the
        Webex call leg.

If you do not require IP media optimization, follow the configuration steps for a SIP
          PSTN trunk. Use a voice port and POTS dial-peer (as shown in Steps 2 and 3) instead of the
          PSTN VoIP dial-peer.

The loop-back dial-peer configuration uses dial-peer groups and call routing tags to
          ensure that calls pass correctly between Webex and the PSTN, without creating call routing
          loops. Configure the following translation rules that will be used to add and remove the
          call routing tags:

```
voice translation-rule 100 
 rule 1 /^\+/ /A2A/ 

voice translation-profile 100 
 translate called 100 

voice translation-rule 200 
 rule 1 /^/ /A1A/ 

voice translation-profile 200 
 translate called 200 

voice translation-rule 11 
 rule 1 /^A1A/ // 

voice translation-profile 11 
 translate called 11 

voice translation-rule 12 
 rule 1 /^A2A44/ /0/
 rule 2/^A2A/ /00/

voice translation-profile 12 
 translate called 12
```

Here's an explanation of the fields for the configuration:

Uses regular expressions
            defined in rules to add or remove call routing tags. Over-decadic digits (‘A’) are used
            to add clarity for troubleshooting.

In this configuration, the tag added by
            translation-profile 100 is used to guide calls from Webex Calling towards the PSTN via
            the loopback dial-peers. Similarly, the tag added by translation-profile 200 is used to
            guide calls from the PSTN towards Webex Calling. Translation-profiles 11 and 12 remove
            these tags before delivering calls to the Webex and PSTN trunks respectively.

This example assumes that called numbers from Webex Calling are presented in
            +E.164 format. Rule 100 removes the leading + to maintain a valid called number. Rule 12
            then adds a national or international routing digit(s) when removing the tag. Use digits
            that suit your local ISDN national dial plan.

If Webex Calling presents numbers in
            national format, adjust rules 100 and 12 to simply add and remove the routing tag
            respectively.

For more information, see voice translation-profile and voice translation-rule .

Configure TDM voice interface ports as required by the trunk type and protocol used.
          For more information, see Configuring ISDN PRI . For example, the basic
          configuration of a Primary Rate ISDN interface installed in NIM slot 2 of a device might
          include the following:

```
card type e1 0 2 
isdn switch-type primary-net5 
controller E1 0/2/0 
 pri-group timeslots 1-31
```

Configure the following TDM PSTN dial-peer:

```
dial-peer voice 200 pots 
 description Inbound/Outbound PRI PSTN trunk 
 destination-pattern BAD.BAD 
 translation-profile incoming 200 
 direct-inward-dial 
 port 0/2/0:15
```

Here's an explanation of the fields for the configuration:

```
dial-peer voice 200 pots description Inbound/Outbound PRI PSTN trunk
```

Defines
            a VoIP dial-peer with a tag of 200 and gives a meaningful description for ease of
            management and troubleshooting. For more information, see dial-peer voice .

A dummy
            destination pattern is required when routing outbound calls using an inbound dial-peer
            group. Any valid destination pattern may be used in this case. For more information, see destination-pattern (interface) .

Assigns
            the translation profile that will add a call routing tag to the incoming called number.

Routes the call without providing a
            secondary dial-tone. For more information, see direct-inward-dial .

The physical voice port associated with this
            dial-peer.

To enable media optimization of IP paths for Local Gateways with TDM-IP call flows, you
          can modify the call routing by introducing a set of internal loop-back dial-peers between
          Webex Calling and PSTN trunks. Configure the following loop-back dial-peers. In this case,
          all incoming calls will be routed initially to dial-peer 10 and from there to either
          dial-peer 11 or 12 based on the applied routing tag. After removal of the routing tag,
          calls will be routed to the outbound trunk using dial-peer groups.

```
dial-peer voice 10 voip
 description Outbound loop-around leg
 destination-pattern BAD.BAD
 session protocol sipv2
 session target ipv4:192.168.80.14
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw
 no vad 

dial-peer voice 11 voip
 description Inbound loop-around leg towards Webex
 translation-profile incoming 11
 session protocol sipv2
 incoming called-number A1AT
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw
 no vad 

dial-peer voice 12 voip
 description Inbound loop-around leg towards PSTN
 translation-profile incoming 12
 session protocol sipv2
 incoming called-number A2AT
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw 
 no vad
```

Here's an explanation of the fields for the configuration:

```
dial-peer voice 10 voip description Outbound loop-around leg
```

Defines a
            VoIP dial-peer and gives a meaningful description for ease of management and
            troubleshooting. For more information, see dial-peer voice .

Applies the
            translation profile defined earlier to remove the call routing tag before passing to the
            outbound trunk.

A
            dummy destination pattern is required when routing outbound calls using an inbound
            dial-peer group. For more information, see destination-pattern (interface) .

Specifies that this dial-peer
            handles SIP call legs. For more information, see session protocol (dial peer) .

Specifies
            the local router interface address as the call target to loop-back. For more
            information, see session target (voip dial
              peer) .

Configures the source
            interface and associated IP address for messages sent through the loop-back. For more
            information, see bind .

Configures the source
            interface and associated IP address for media sent through the loop-back. For more
            information, see bind .

Defines RTP-NTE (RFC2833) as the DTMF capability expected on the
            call leg. For more information, see DTMF Relay (Voice over
                IP) .

codec g711alaw

Forces all PSTN
            calls to use G.711. Select a-law or u-law to match the companding method used by your
            ISDN service.

Disables voice activity detection.
            For more information, see vad (dial peer) .

Add the following call routing configuration:

Create dial-peer groups to route calls between the PSTN and Webex trunks, via the
              loop-back.

```
voice class dpg 100
 description Route calls to Webex Calling
 dial-peer 100
voice class dpg 200
 description Route calls to PSTN
 dial-peer 200
voice class dpg 10
 description Route calls to Loopback
 dial-peer 10
```

Here's an explanation of the fields for the configuration:

Associates an outbound
                dial-peer with a dial-peer group. For more information, see voice-class dpg .

Apply dial-peer groups to route calls.

```
dial-peer voice 100
 destination dpg 10
dial-peer voice 200
 destination dpg 10
dial-peer voice 11
 destination dpg 100
dial-peer voice 12
 destination dpg 200
```

Here's an explanation of the fields for the
                configuration:

Specifies which dial-peer group, and therefore
                dial-peer should be used for the outbound treatment for calls presented to this
                incoming dial-peer.

This concludes your Local Gateway configuration. Save the configuration and reload the
          platform if this is the first time CUBE features are configured.

Configure Local Gateway with an existing Unified CM environment

The PSTN-Webex Calling configuration in the previous sections may be modified to include
        additional trunks to a Cisco Unified Communications Manager (UCM) cluster. In this case, all
        calls are routed via Unified CM. Calls from UCM on port 5060 are routed to the PSTN and
        calls from port 5065 are routed to Webex Calling. The following incremental configurations
        may be added to include this calling scenario.

Configure the following voice class URIs:

Classifies Unified CM to Webex calls using SIP VIA port:

```
voice class uri 300 sip
 pattern :5065
```

Classifies Unified CM to PSTN calls using SIP via port:

```
voice class uri 400 sip
 pattern 192\.168\.80\.6[0-5]:5060
```

Classify incoming messages from the UCM towards the PSTN trunk using one or more
                patterns that describe the originating source addresses and port number. Regular
                expressions may be used to define matching patterns if required.

In the example above, a regular expression is used to match any IP address in the
                range 192.168.80.60 to 65 and port number 5060.

Configure the following DNS records to specify SRV routing to Unified CM hosts:

IOS XE uses these records for locally determining target UCM hosts and ports. With
              this configuration, it is not required to configure records in your DNS system. If you
              prefer to use your DNS, then these local configurations are not required.

```
ip host ucmpub.mydomain.com 192.168.80.60
ip host ucmsub1.mydomain.com 192.168.80.61
ip host ucmsub2.mydomain.com 192.168.80.62
ip host ucmsub3.mydomain.com 192.168.80.63
ip host ucmsub4.mydomain.com 192.168.80.64
ip host ucmsub5.mydomain.com 192.168.80.65
ip host _sip._udp.wxtocucm.io srv 0 1 5065 ucmpub.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub1.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub2.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub3.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub4.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub5.mydomain.com
ip host _sip._udp.pstntocucm.io srv 0 1 5060 ucmpub.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub1.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub2.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub3.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub4.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub5.mydomain.com
```

Here's an explanation of the fields for the configuration:

The following command creates a DNS SRV resource record. Create a record for each UCM
            host and trunk:

ip host _sip._udp.pstntocucm.io srv 2 1 5060
              ucmsub5.mydomain.com

_sip._udp.pstntocucm.io : SRV resource record name

2 : The SRV resource record priority

1 : The SRV resource record weight

5060 : The port number to use for the target host in this resource record

ucmsub5.mydomain.com : The resource record target host

To resolve the resource record target host names, create local DNS A records. For
            example:

ip host ucmsub5.mydomain.com 192.168.80.65

ip host : Creates a record in the local IOS XE database.

ucmsub5.mydomain.com : The A record host name.

192.168.80.65 : The host IP address.

Create the SRV resource records and A records to reflect your UCM environment and
            preferred call distribution strategy.

Configure the following dial-peers:

Dial-peer for calls between Unified CM and Webex Calling:

```
dial-peer voice 300 voip
 description UCM-Webex Calling trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target dns:wxtocucm.io
 incoming uri via 300
 voice-class codec 100
 voice-class sip bind control source-interface GigabitEthernet 0/0/0
 voice-class sip bind media source-interface GigabitEthernet 0/0/0
 dtmf-relay rtp-nte
 no vad
```

Here's an explanation of the fields for the
                configuration:

```
dial-peer voice 300 voip description UCM-Webex Calling trunk
```

Defines
                a VoIP dial-peer with a tag 300 and gives a meaningful description for ease
                of management and troubleshooting.

A dummy destination pattern is required when routing
                outbound calls using an inbound dial-peer group. Any valid destination pattern may
                be used in this case.

Specifies that dial-peer 300 handles SIP call legs. For more
                information, see session protocol
                  (dial-peer) .

Defines the session target of multiple Unified CM
                nodes through DNS SRV resolution. In this case, the locally defined SRV record
                wxtocucm.io is used to direct calls.

Uses voice class URI 300 to direct all incoming traffic from
                Unified CM using source port 5065 to this dial-peer. For more information, see incoming uri .

Indicates codec filter list for calls to and
                from Unified CM. For more information, see voice class codec .

Configures the
                source interface and associated IP address for messages sent to the PSTN. For more
                information, see bind .

Configures the source
                interface and associated IP address for media sent to PSTN. For more information,
                  see bind .

Defines RTP-NTE (RFC2833) as the DTMF capability expected
                on the call leg. For more information, see DTMF Relay (Voice over IP) .

Disables voice activity detection. For
                more information, see vad (dial peer) .

Dial-peer for calls between Unified CM and the PSTN:

```
dial-peer voice 400 voip
 description UCM-PSTN trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target dns:pstntocucm.io
 incoming uri via 400
 voice-class codec 100 
 voice-class sip bind control source-interface GigabitEthernet 0/0/0
 voice-class sip bind media source-interface GigabitEthernet 0/0/0
 dtmf-relay rtp-nte
 no vad
```

Here's an explanation of the fields for the
                configuration:

```
dial-peer voice 400 voip description UCM-PSTN trunk
```

Defines a VoIP
                dial-peer with a tag of 400 and gives a meaningful description for ease of
                management and troubleshooting.

A dummy destination pattern is required when routing
                outbound calls using an inbound dial-peer group. Any valid destination pattern may
                be used in this case.

Specifies that dial-peer 400 handles SIP call legs. For more
                information, see session protocol
                  (dial-peer) .

Defines the session target of multiple Unified CM
                nodes through DNS SRV resolution. In this case, the locally defined SRV record
                pstntocucm.io is used to direct calls.

Uses voice class URI 400 to direct all incoming
                traffic from the specified Unified CM hosts using source port 5060 to this
                dial-peer. For more information, see incoming uri .

Indicates codec filter list for calls to and
                from Unified CM. For more information, see voice class codec .

Configures the
                source interface and associated IP address for messages sent to the PSTN. For more
                information, see bind .

Configures the source
                interface and associated IP address for media sent to PSTN. For more information,
                  see bind .

Defines RTP-NTE (RFC2833) as the DTMF capability expected
                on the call leg. For more information, see DTMF Relay (Voice over IP) .

Disables voice activity detection. For
                more information, see vad (dial peer) .

Add call routing using the following configurations:

Create dial-peer groups to route calls between Unified CM and Webex Calling. Define
              DPG 100 with outbound dial-peer 100 towards Webex Calling.
              DPG 100 is applied to the associated incoming dial-peer from Unified CM. Similarly,
              define DPG 300 with outbound dial-peer 300 toward Unified CM. DPG 300 is applied to
              the incoming dial-peer from Webex.

```
voice class dpg 100
 description Route calls to Webex Calling
 dial-peer 100
voice class dpg 300
 description Route calls to Unified CM Webex Calling trunk
 dial-peer 300
```

Create a dial-peer groups to route calls between Unified CM and the PSTN. Define
              DPG 200 with outbound dial-peer 200 toward the PSTN. DPG 200
              is applied to the associated incoming dial-peer from Unified CM. Similarly, define DPG
              400 with outbound dial-peer 400 toward Unified CM. DPG 400 is applied to the incoming
              dial-peer from the PSTN.

```
voice class dpg 200
 description Route calls to PSTN
 dial-peer 200
voice class dpg 400
 description Route calls to Unified CM PSTN trunk
 dial-peer 400
```

Here's an explanation of the fields for the
                configuration:

Associates an
                outbound dial-peer with a dial-peer group. For more information, see voice-class dpg .

Apply dial-peer groups to route calls from Webex to Unified CM and from Unified CM
              to Webex:

```
dial-peer voice 100
 destination dpg 300
dial-peer voice 300
 destination dpg 100
```

Here's an explanation of the fields for the
                configuration:

Specifies which dial-peer group, and therefore
                dial-peer should be used for the outbound treatment for calls presented to this
                incoming dial-peer.

Apply dial-peer groups to route calls from the PSTN to Unified CM and from Unified
              CM to the PSTN:

```
dial-peer voice 200
 destination dpg 400
dial-peer voice 400
 destination dpg 200
```

This concludes your Local Gateway configuration. Save the configuration and reload
                the platform if this is the first time CUBE features have been configured.

Monitor and troubleshoot Certificate based Local Gateway with diagnostic signatures

Diagnostic Signatures (DS) proactively detects commonly observed issues in the Cisco IOS
        XE-based Local Gateway and generates email, syslog, or terminal message notification of the
        event. You can also install the DS to automate diagnostics data collection and transfer
        collected data to the Cisco TAC case to accelerate resolution time.

Diagnostic Signatures (DS) are XML files that contain information about problem trigger
        events and actions to inform, troubleshoot, and remediate the issue. Use syslog messages,
        SNMP events and through periodic monitoring of specific show command outputs to define the
        problem detection logic. The action types include:

Collecting show command outputs

Generating a consolidated log file

Uploading the file to a user provided network location such as HTTPS, SCP, FTP
            server

TAC engineers author DS files and digitally sign it for integrity protection. Each DS file
        has the unique numerical ID assigned by the system. Diagnostic Signatures Lookup
          Tool (DSLT) is a single source to find applicable signatures for monitoring and
        troubleshooting various problems.

Before you begin:

Do not edit the DS file that you download from DSLT . The files that
            you modify fail installation due to the integrity check error.

A Simple Mail Transfer Protocol (SMTP) server you require for the Local Gateway to send
            out email notifications.

Ensure that the Local Gateway is running IOS XE 17.6.1 or higher if you wish to use the
            secure SMTP server for email notifications.

### Prerequisites

Local Gateway running IOS XE 17.6.1 or higher

Diagnostic Signatures is enabled by default.

Configure the secure email server that you use to send proactive notification if the
            device is running IOS XE 17.6.1 or higher.

```
configure terminal 
call-home  
mail-server <username>:<pwd>@<email server> priority 1 secure tls 
end
```

Configure the environment variable ds_email with the email address of the
            administrator to you notify.

```
configure terminal 
call-home  
diagnostic-signature 
LocalGateway(cfg-call-home-diag-sign)environment ds_email <email address> 
end
```

### Install diagnostic signatures for proactive monitoring

Monitoring high CPU utilization

This DS tracks 5-seconds CPU utilization using the SNMP OID 1.3.6.1.4.1.9.2.1.56. When the
        utilization reaches 75% or more, it disables all debugs and uninstalls all diagnostic
        signatures that you install in the Local Gateway. Use these steps below to install the
        signature.

Ensure that you enabled SNMP using the command show snmp . If
            SNMP is not enabled, then configure the snmp-server manager command.

```
show snmp 
%SNMP agent not enabled  

config t 
snmp-server manager 
end  

show snmp 
Chassis: ABCDEFGHIGK 
149655 SNMP packets input 
    0 Bad SNMP version errors 
    1 Unknown community name 
    0 Illegal operation for community name supplied 
    0 Encoding errors 
    37763 Number of requested variables 
    2 Number of altered variables 
    34560 Get-request PDUs 
    138 Get-next PDUs 
    2 Set-request PDUs 
    0 Input queue packet drops (Maximum queue size 1000) 
158277 SNMP packets output 
    0 Too big errors (Maximum packet size 1500) 
    20 No such name errors 
    0 Bad values errors 
    0 General errors 
    7998 Response PDUs 
    10280 Trap PDUs 
Packets currently in SNMP process input queue: 0 
SNMP global trap: enabled
```

Download DS 64224 using the following drop-down options in Diagnostic Signatures
              Lookup Tool :

```
copy ftp://username:password@<server name or ip>/DS_64224.xml bootflash:
```

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series, or Catalyst 8000V Edge Software

Product

CUBE Enterprise in Webex Calling solution

Problem Scope

Performance

Problem Type

High CPU Utilization with Email Notification

Copy the DS XML file to the Local Gateway flash.

```
copy ftp://username:password@<server name or ip>/DS_64224.xml bootflash:
```

The following example shows copying the file from an FTP server to the Local
            Gateway.

```
copy ftp://user:pwd@192.0.2.12/DS_64224.xml bootflash: 
Accessing ftp://*:*@ 192.0.2.12/DS_64224.xml...! 
[OK - 3571/4096 bytes] 
3571 bytes copied in 0.064 secs (55797 bytes/sec)
```

Install the DS XML file in the Local Gateway.

```
call-home diagnostic-signature load DS_64224.xml 
Load file DS_64224.xml success
```

Use the show call-home diagnostic-signature command to verify
            that the signature is successfully installed. The status column must have a “registered”
            value.

```
show call-home diagnostic-signature  
Current diagnostic-signature settings: 
 Diagnostic-signature: enabled 
 Profile: CiscoTAC-1 (status: ACTIVE) 
 Downloading  URL(s):  https://tools.cisco.com/its/service/oddce/services/DDCEService 
 Environment variable: 
           ds_email: username@gmail.com
```

Download DSes:

DS ID

DS Name

Revision

Status

Last Update (GMT+00:00)

64224

DS_LGW_CPU_MON75

0.0.10

Registered

2020-11-07 22:05:33

When triggered, this signature uninstalls all running DSs including itself. If
              necessary, please reinstall DS 64224 to continue monitoring high CPU utilization on
              the Local Gateway.

### Monitoring abnormal call disconnects

This DS uses SNMP polling every 10 minutes to detect abnormal call disconnect with SIP
        errors 403, 488 and 503.  If the error count increment is greater than or equal to 5 from
        the last poll, it generates a syslog and email notification. Please use the steps below to
        install the signature.

Ensure that SNMP is enabled using the command show snmp . If
            SNMP is not enabled, configure the snmp-server manager command.

```
show snmp 
%SNMP agent not enabled  

config t 
snmp-server manager 
end  

show snmp 
Chassis: ABCDEFGHIGK 
149655 SNMP packets input 
    0 Bad SNMP version errors 
    1 Unknown community name 
    0 Illegal operation for community name supplied 
    0 Encoding errors 
    37763 Number of requested variables 
    2 Number of altered variables 
    34560 Get-request PDUs 
    138 Get-next PDUs 
    2 Set-request PDUs 
    0 Input queue packet drops (Maximum queue size 1000) 
158277 SNMP packets output 
    0 Too big errors (Maximum packet size 1500) 
    20 No such name errors 
    0 Bad values errors 
    0 General errors 
    7998 Response PDUs 
    10280 Trap PDUs 
Packets currently in SNMP process input queue: 0 
SNMP global trap: enabled
```

Download DS 65221 using the following options in Diagnostic Signatures
              Lookup Tool :

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series, or Catalyst 8000V Edge Software

Product

CUBE Enterprise in Webex Calling Solution

Problem Scope

Performance

Problem Type

SIP abnormal call disconnect detection with Email and Syslog Notification.

Copy the DS XML file to the Local Gateway.

```
copy ftp://username:password@<server name or ip>/DS_65221.xml bootflash:
```

Install the DS XML file in the Local Gateway.

```
call-home diagnostic-signature load DS_65221.xml 
Load file DS_65221.xml success
```

Use the command show call-home diagnostic-signature to verify
            that the signature is successfully installed. The status column should have a
            “registered” value.

### Install diagnostic signatures to troubleshoot a problem

You can also use Diagnostic Signatures (DS) to resolve issues quickly. Cisco TAC engineers
        have authored several signatures that enable the necessary debugs that are required to
        troubleshoot a given problem, detect the problem occurrence, collect the right set of
        diagnostic data and transfer the data automatically to the Cisco TAC case. This eliminates
        the need to manually check for the problem occurrence and makes troubleshooting of
        intermittent and transient issues a lot easier.

You can use the Diagnostic Signatures Lookup Tool to find the applicable
        signatures and install them to selfsolve a given issue or you can install the signature that
        is recommended by the TAC engineer as part of the support engagement.

Here is an example of how to find and install a DS to detect the occurrence
        “%VOICE_IEC-3-GW: CCAPI: Internal Error (call spike threshold): IEC=1.1.181.1.29.0" syslog
        and automate diagnostic data collection using the following steps:

Configure another DS environment variable ds_fsurl_prefix as the Cisco TAC file
            server path (cxd.cisco.com) to upload the diagnostics data. The username in the file
            path is the case number and the password is the file upload token which can be retrieved
            from Support Case Manager as shown in the following. The file upload token can be
            generated in the Attachments section of the Support Case Manager, as required.

```
configure terminal 
call-home  
diagnostic-signature 
LocalGateway(cfg-call-home-diag-sign)environment ds_fsurl_prefix "scp://<case number>:<file upload token>@cxd.cisco.com"  
end
```

Example:

```
call-home  
diagnostic-signature 
environment ds_fsurl_prefix " environment ds_fsurl_prefix "scp://612345678:abcdefghijklmnop@cxd.cisco.com"
```

Ensure that SNMP is enabled using the command show snmp . If
            SNMP not enabled, configure the snmp-server manager command.

```
show snmp 
%SNMP agent not enabled 
 
config t 
snmp-server manager 
end
```

We recommend installing the High CPU monitoring DS 64224 as a proactive measure to
            disable all debugs and diagnostics signatures during the time of high CPU utilization.
            Download DS 64224 using the following options in Diagnostic Signatures
              Lookup Tool :

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series, or Catalyst 8000V Edge Software

Product

CUBE Enterprise in Webex Calling Solution

Problem Scope

Performance

Problem Type

High CPU Utilization with Email Notification.

Download DS 65095 using the following options in Diagnostic Signatures
              Lookup Tool :

Field Name

Field Value

Platform

Cisco 4300, 4400 ISR Series, or Catalyst 8000V Edge Software

Product

CUBE Enterprise in Webex Calling Solution

Problem Scope

Syslogs

Problem Type

Syslog - %VOICE_IEC-3-GW: CCAPI: Internal Error (Call spike threshold):
                      IEC=1.1.181.1.29.0

Copy the DS XML files to the Local Gateway.

```
copy ftp://username:password@<server name or ip>/DS_64224.xml bootflash: 
copy ftp://username:password@<server name or ip>/DS_65095.xml bootflash:
```

Install the high CPU monitoring DS 64224 and then DS 65095 XML file in the Local
            Gateway.

```
call-home diagnostic-signature load DS_64224.xml 
Load file DS_64224.xml success 
call-home diagnostic-signature load DS_65095.xml 
Load file DS_65095.xml success
```

Verify that the signature is successfully installed using show call-home
                diagnostic-signature . The status column should have a “registered”
            value.

```
show call-home diagnostic-signature  
Current diagnostic-signature settings: 
 Diagnostic-signature: enabled 
 Profile: CiscoTAC-1 (status: ACTIVE) 
 Downloading  URL(s):  https://tools.cisco.com/its/service/oddce/services/DDCEService 
 Environment variable: 
           ds_email: username@gmail.com 
           ds_fsurl_prefix: scp://612345678:abcdefghijklmnop@cxd.cisco.com
```

Downloaded DSes:

DS ID

DS Name

Revision

Status

Last Update (GMT+00:00)

64224

00:07:45

DS_LGW_CPU_MON75

0.0.10

Registered

2020-11-08:00:07:45

65095

00:12:53

DS_LGW_IEC_Call_spike_threshold

0.0.12

Registered

2020-11-08:00:12:53

### Verify diagnostic signatures execution

In the following command, the “Status” column of the command show call-home
            diagnostic-signature changes to “running” while the Local Gateway executes
        the action defined within the signature. The output of show call-home
            diagnostic-signature statistics is the best way to verify whether a
        diagnostic signature detects an event of interest and executed the action. The
        “Triggered/Max/Deinstall” column indicates the number of times the given signature has
        triggered an event, the maximum number of times it is defined to detect an event and whether
        the signature deinstalls itself after detecting the maximum number of triggered events.

```
show call-home diagnostic-signature  
Current diagnostic-signature settings: 
 Diagnostic-signature: enabled 
 Profile: CiscoTAC-1 (status: ACTIVE) 
 Downloading  URL(s):  https://tools.cisco.com/its/service/oddce/services/DDCEService 
 Environment variable: 
           ds_email: carunach@cisco.com 
           ds_fsurl_prefix: scp://612345678:abcdefghijklmnop@cxd.cisco.com
```

Downloaded DSes:

DS ID

DS Name

Revision

Status

Last Update (GMT+00:00)

64224

DS_LGW_CPU_MON75

0.0.10

Registered

2020-11-08 00:07:45

65095

DS_LGW_IEC_Call_spike_threshold

0.0.12

Running

2020-11-08 00:12:53

show call-home diagnostic-signature statistics

DS ID

DS Name

Triggered /Max/Deinstall

Average Run Time (seconds)

Max Run Time (seconds)

DS_LGW_CPU_MON75

0/0/N

0.000

0.000

65095

DS_LGW_IEC_Call_spike_threshold

1 /20/Y

23.053

23.053

The notification email that is sent during Diagnostic Signature execution contains key
        information such as issue type, device details, software version, running configuration and
        show command outputs that are relevant to troubleshoot the given problem.

### Uninstall diagnostic signatures

Use the diagnostic signatures for troubleshooting purposes are typically defined to
        uninstall after detection of some problem occurrences. If you wish to uninstall a signature
        manually, retrieve the DS ID from the output of show call-home
            diagnostic-signature and run the following command:

```
call-home diagnostic-signature deinstall <DS ID>
```

Example:

```
call-home diagnostic-signature deinstall 64224
```

New signatures are added to the Diagnostics Signatures Lookup Tool periodically, based on
          issues that are observed in deployments. TAC currently doesn’t support requests to create
          new custom signatures.

| 1 | Ensure that you assign valid and routable IP addresses to any Layer 3 interfaces, for
          example: interface GigabitEthernet0/0/0
  description Interface facing PSTN and/or CUCM
  ip address 10.80.13.12 255.255.255.0
!
interface GigabitEthernet0/0/1
  description Interface facing Webex Calling (Private address)
  ip address 192.51.100.1 255.255.255.240 |
|---|---|
| 2 | Protect registration and STUN credentials on the router using symmetric encryption.
          Configure the primary encryption key and encryption type as follows: key config-key password-encrypt YourPassword
password encryption aes |
| 3 | Create a placeholder PKI trustpoint. Requires this trustpoint to configure TLS later. For registration-based trunks, this trustpoint doesn't require a certificate - as required for a certificate-based trunk. crypto pki trustpoint EmptyTP 
 revocation-check none |
| 4 | Enable TLS1.2 exclusivity and specify the default trustpoint using the following configuration commands. Update the Transport parameters to ensure a reliable secure connection for registration: The cn-san-validate server command ensures that the Local Gateway permits a connection, if the host name configured in tenant 200 is included in either the CN or SAN fields of the certificate received from the outbound proxy. Set tcp-retry count to 1000 (5-msec multiples = 5 seconds). The timer connection establish command allows you to tune how long the LGW waits to set up a connection with a proxy before considering the next available option. The default for this timer is 20 seconds and the minimum 5 seconds. Start with a low value and increase if necessary to accommodate network conditions. sip-ua
 timers connection establish tls 5
 transport tcp tls v1.2
 crypto signaling default trustpoint EmptyTP cn-san-validate server
 tcp-retry 1000 |
| 5 | Install the Cisco root CA bundle, which includes the IdenTrust Commercial Root CA1 certificate used by Webex Calling. Use the crypto pki trustpool import clean url command to download the root CA bundle from the specified URL, and to clear the current CA trustpool, then install the new bundle of certificates: If you need to use a proxy for access to the internet using HTTPS, add the following configuration before importing the CA bundle: ip http client proxy-server yourproxy.com proxy-port 80 ip http client source-interface GigabitEthernet0/0/1 
crypto pki trustpool import clean url https://www.cisco.com/security/pki/trs/ios_core.p7b |

| 1 | Create a registration based PSTN trunk for an existing location in the Control
                    Hub. Make a note of the trunk information that is provided once the trunk has
                    been created. The details highlighted in the illustration are used in the
                    configuration steps in this guide. For more information, see Configure trunks, route groups, and dial
                        plans for Webex Calling . |
|---|---|
| 2 | Enter the following commands to configure CUBE as a Webex Calling Local
                    Gateway: voice service voip
 ip address trusted list
  ipv4 x.x.x.x y.y.y.y
 mode border-element
 media statistics
 media bulk-stats 
 allow-connections sip to sip
 no supplementary-service sip refer  
 stun
  stun flowdata agent-id 1 boot-count 4
  stun flowdata shared-secret 0 Password123$
 sip
  asymmetric payload full
  early-offer forced Here's an explanation of the fields for the
                        configuration: ip address trusted list ipv4 x.x.x.x y.y.y.y To protect against toll fraud, the trusted address list defines a
                                list of hosts and networks from which the Local Gateway expects
                                legitimate VoIP calls. By default, Local Gateway blocks all incoming VoIP messages from IP
                                addresses not in its trusted list. By default, statically configured
                                dial-peers with “session target IP” or server group IP addresses are
                                trusted. Adding these IP addresses to the trusted list is not
                                required. When configuring your Local Gateway, add the IP subnets of your
                                regional Webex Calling data center to the list. For more
                                information, see Port Reference Information for Webex
                                    Calling . Also, add address ranges for Unified
                                Communications Manager servers (if used) and PSTN trunk
                                gateways. If your LGW is behind a firewall with restricted cone NAT, you
                                    may prefer to disable the IP address trusted list on the Webex
                                    Calling facing interface. The firewall already protects you from
                                    unsolicited inbound VoIP. Disable action reduces your
                                    longer-term configuration overhead, because we cannot guarantee
                                    that the addresses of the Webex Calling peers remain fixed, and
                                    you must configure your firewall for the peers in any case. mode border-element Enables Cisco Unified
                        Border Element (CUBE) features on the platform. media
                            statistics Enables media monitoring on the Local
                        Gateway. media bulk-stats Enables the
                        control plane to poll the data plane for bulk call statistics. For
                        more information on these commands, see Media . allow-connections sip to
                        sip Enable CUBE basic SIP back-to-back user agent
                        functionality. For more information, see Allow connections . By default, T.38 fax transport is enabled. For more information, see fax protocol t38
                                (voice-service) . stun Enables STUN (Session Traversal of UDP
                        through NAT) globally. The STUN bindings feature on the Local Gateway allows locally
                                generated STUN requests to be sent over the negotiated media path.
                                This helps to open the pinhole in the firewall. For more information, see stun flowdata agent-id and stun flowdata
                            shared-secret . asymmetric payload
                        full Configures SIP asymmetric payload support for both DTMF
                        and dynamic codec payloads. For more information, see asymmetric
                            payload . early-offer forced Forces
                        the Local Gateway to send SDP information in the initial INVITE message
                        instead of waiting for acknowledgment from the neighboring peer. For more
                        information on this command, see early-offer . |
| 3 | Configure voice class codec 100 allowing G.711 codecs
                    only for all trunks. This simple approach is suitable for most deployments. If
                    required, additional codec types supported by both originating and terminating
                    systems may be added to the list. More complex solutions involving transcoding using DSP modules
                            are supported, but not included in this guide. voice class codec 100
 codec preference 1 g711ulaw
 codec preference 2 g711alaw Here's an explanation of the fields for the
                            configuration: voice class codec 100 Used
                        to only allow preferred codecs for SIP trunk calls. For more information,
                        see voice class codec . |
| 4 | Configure voice class stun-usage 100 to
                    enable ICE on the Webex Calling trunk. voice class stun-usage 100 
 stun usage firewall-traversal flowdata
 stun usage ice lite Here's an explanation of the fields for the
                        configuration: stun usage ice lite Used to
                        enable ICE-Lite for all Webex Calling facing dial-peers to allow
                        media-optimization whenever possible. For more information, see voice class stun usage and stun usage ice lite . Media optimization is negotiated wherever possible. If a call requires
                            cloud media services, such as recording, the media cannot be
                            optimized. |
| 5 | Configure the media encryption policy for Webex traffic. voice class srtp-crypto 100
 crypto 1 AES_CM_128_HMAC_SHA1_80 Here's an explanation of the fields
                        for the configuration: voice class srtp-crypto
                        100 Specifies SHA1_80 as the only SRTP cipher-suite CUBE
                        offers in the SDP in offer and answer messages. Webex Calling only supports
                        SHA1_80. For more information, see voice class
                    srtp-crypto . |
| 6 | Configure a pattern to identify calls to a Local Gateway trunk based on its
                    destination trunk parameter: voice class uri 100 sip
 pattern dtg=dallas1463285401_lgu Here's an explanation of the fields for the
                            configuration: voice class uri 100
                        sip Defines a pattern to match an incoming SIP invite to an
                        incoming trunk dial-peer. When entering this pattern, use dtg= followed by
                        the Trunk OTG/DTG value provided in the Control Hub when the trunk was
                        created. For more information, see voice class uri . |
| 7 | Configure sip profile 100 , which will be used to
                    modify SIP messages before they are sent to Webex Calling. voice class sip-profiles 100
 rule 10 request ANY sip-header SIP-Req-URI modify "sips:" "sip:"
 rule 20 request ANY sip-header To modify "<sips:" "<sip:"
 rule 30 request ANY sip-header From modify "<sips:" "<sip:"
 rule 40 request ANY sip-header Contact modify "<sips:(.*)>" "<sip:\1;transport=tls>" 
 rule 50 response ANY sip-header To modify "<sips:" "<sip:"
 rule 60 response ANY sip-header From modify "<sips:" "<sip:"
 rule 70 response ANY sip-header Contact modify "<sips:" "<sip:"
 rule 80 request ANY sip-header From modify ">" ";otg=dallas1463285401_lgu>"
 rule 90 request ANY sip-header P-Asserted-Identity modify "sips:" "sip:" Here's an explanation of the fields for the configuration: rule 10 to 70 and 90 Ensures that SIP headers used for call signaling use SIP, rather than
                                SIPs scheme, which Webex proxies require. Configuring CUBE to use
                                SIP ensures that secure registration is used. rule 80 Modifies the From header to include the trunk group OTG/DTG
                                identifier from the Control Hub to uniquely identify a Local Gateway
                                site within an enterprise. United States or Canadian PSTN provider can offer the Caller ID
                            verification for Spam and fraud calls, with the additional configuration
                            mentioned in the Spam or fraud call indication in
                                Webex Calling article. |
| 8 | Configure Webex Calling trunk: Create voice class tenant 100 to
                            define and group configurations required specifically for the Webex
                            Calling trunk. In particular, the trunk registration details provided in
                            Control Hub earlier will be used in this step as detailed below.
                            Dial-peers associated with this tenant later will inherit these
                            configurations. The following example uses the values illustrated in Step 1 for
                                    the purpose of this guide (shown in bold). Replace these with
                                    values for your trunk in your configuration. voice class tenant 100
  registrar dns: 98027369.us10.bcld.webex.com scheme sips expires 240 refresh-ratio 50 tcp tls
  credentials number Dallas1171197921_LGU username Dallas1463285401_LGU password 0 9Wt[M6ifY+ realm BroadWorks
  authentication username Dallas1463285401_LGU password 0 9Wt[M6ifY+ realm BroadWorks
  authentication username Dallas1463285401_LGU password 0 9Wt[M6ifY+ realm 98027369.us10.bcld.webex.com no remote-party-id
  sip-server dns: 98027369.us10.bcld.webex.com connection-reuse
  srtp-crypto 100
  session transport tcp tls 
  no session refresh
  url sips 
  error-passthru
  rel1xx disable
  asserted-id pai 
  bind control source-interface GigabitEthernet0/0/1
  bind media source-interface GigabitEthernet0/0/1
  no pass-thru content custom-sdp 
  sip-profiles 100 
  outbound-proxy dns: dfw04.sipconnect-us.bcld.webex.com privacy-policy passthru Here's an explanation of the fields for the
                                configuration: voice class tenant 100 Defines a set of configuration
                                parameters that will be used only for the Webex Calling trunk. For
                                more information, see voice class
                                    tenant . registrar dns:98027369.us10.bcld.webex.com scheme sips expires 240 refresh-ratio 50 tcp
                                tls Registrar server for the Local Gateway with the
                                registration set to refresh every two minutes (50% of 240 seconds).
                                For more information, see registrar . Ensure
                                that you use the Register Domain value from the Control Hub
                                here. credentials number Dallas1171197921_LGU username Dallas1463285401_LGU password 0 9Wt[M6ifY+ realm BroadWorks Credentials for trunk
                                registration challenge. For more information, see credentials (SIP
                                UA) . Ensure that you use the Line/Port host,
                                Authentication Username and Authentication Password values
                                respectively from the Control Hub
                                    here. authentication username Dallas1171197921_LGU password 0 9Wt[M6ifY+ realm BroadWorks authentication username Dallas1171197921_LGU password 0 9Wt[M6ifY+ realm 98027369.us10.bcld.webex.com Authentication
                                challenge for calls. For more information, see authentication
                                (dial-peer) . Ensure that you use the Authentication
                                Username, Authentication Password and Registrar Domain values
                                respectively from the Control Hub here. no
                                    remote-party-id Disable SIP Remote-Party-ID
                                (RPID) header as Webex Calling supports PAI, which is enabled using asserted-id pai . For more
                                information, see remote-party-id . sip-server
                                    dns: us25.sipconnect.bcld.webex.com Configures
                                the target SIP server for the trunk. Use the Edge proxy SRV address
                                provided in the Control Hub when you created your
                                    trunk. connection-reuse Uses the
                                same persistent connection for registration and call processing. For
                                more information, see connection-reuse . srtp-crypto 100 Configures the preferred
                                cipher-suites for the SRTP call leg (connection) (specified in step
                                5). For more information, see voice class
                                srtp-crypto. session transport tcp
                                tls Sets transport to TLS. For more information, see session-transport . no session
                                    refresh Disables SIP session refresh for calls
                                between CUBE and Webex. For more information, see session
                            refresh . url sips SRV query must be SIPs as
                                supported by the access SBC; all other messages are changed to SIP
                                by sip-profile
                                200. error-passthru Specifies SIP
                                error response pass-thru functionality. For more information, see error-passthru . rel1xx disable Disables the use of
                                reliable provisional responses for the Webex Calling trunk. For more
                                information, see rel1xx . asserted-id pai (Optional) Turns on
                                P-Asserted-Identity header processing and controls how this is used
                                for the Webex Calling trunk. Webex Calling includes
                                P-Asserted-Identity (PAI) headers in outbound call INVITEs to the
                                Local Gateway. If this command is configured, caller
                                information from the PAI header is used to populate the outgoing
                                From and PAI/Remote-Party-ID headers. If this command is not
                                configured, caller information from the From header is used to
                                populate the outgoing From and PAI/Remote-Party-ID
                                headers. For more information, see asserted-id . bind control
                                    source-interface GigabitEthernet0/0/1 Configures the
                                source interface and associated IP address for messages sent to
                                Webex Calling. For more information, see bind . bind
                                    media source-interface GigabitEthernet0/0/1 Configures the
                                source interface and associated IP address for media sent to
                                WebexCalling. For more information, see bind . no
                                    pass-thru content custom-sdp Default command
                                under tenant. For more information on this command, see pass-thru
                                    content . sip-profiles 100 Changes SIPs to SIP and modify
                                Line/Port for INVITE and REGISTER messages as defined in sip-profiles 100 . For
                                more information, see voice class
                                sip-profiles . outbound-proxy dns:dfw04.sipconnect-us.bcld.webex.com Webex
                                Calling access SBC. Insert the Outbound Proxy Address provided in
                                the Control Hub when you created your trunk. For more information,
                                see outbound-proxy . privacy-policy
                                    passthru Configures the privacy header policy
                                options for the trunk to pass privacy values from the received
                                message to the next call leg. For more information, see privacy-policy . Configure the Webex Calling trunk dial-peer. dial-peer voice 100 voip
 description Inbound/Outbound Webex Calling
 max-conn 250
 destination-pattern BAD.BAD
 session protocol sipv2
 session target sip-server
 incoming uri request 100
 voice-class codec 100
 dtmf-relay rtp-nte
 voice-class stun-usage 100
 no voice-class sip localhost
 voice-class sip tenant 100
 srtp
 no vad Here's an explanation of the fields for the
                                configuration: dial-peer voice 100 voip description Inbound/Outbound Webex Calling Defines a VoIP dial-peer with a tag of 100 and gives
                                a meaningful description for ease of management and
                                troubleshooting. max-conn 250 Restricts the number of concurrent
                                inbound and outbound calls between the LGW and Webex Calling. For
                                registration trunks, the maximum value configured should be 250.
                                User lower value if that would be more appropriate for your
                                deployment. For more information on concurrent call limits for Local
                                Gateway, refer to the Get started with Local
                                    Gateway document. destination-pattern BAD.BAD A dummy destination pattern
                                is required when routing outbound calls using an inbound dial-peer
                                group. Any valid destination pattern may be used in this case. For
                                more information, see destination-pattern
                                    (interface) . session protocol
                                sipv2 Specifies that dial-peer 100 handles SIP call
                                legs. For more information, see session protocol
                                    (dial-peer) . session target
                                    sip-server Indicates that the SIP server defined
                                in tenant 100 is inherited and used for the destination for calls
                                from this dial peer. For more information, see session target (voip dial
                                    peer) . incoming uri request 100 To specify the voice class used
                                to match a VoIP dial peer to the Uniform Resource Identifier (URI)
                                of an incoming call. For more information, see incoming
                                    uri . voice-class codec 100 Configures the dial-peer to use
                                the common codec filter list 100. For more information, see voice-class
                                    codec . voice-class stun-usage 100 Allows locally generated STUN
                                requests on the Local Gateway to be sent over the negotiated media
                                path. STUN helps to open a firewall pinhole for media traffic. For
                                more information, see voice-class
                                stun-usage . no voice-class sip
                                localhost Disables substitution of the DNS local
                                host name in place of the physical IP address in the From, Call-ID,
                                and Remote-Party-ID headers of outgoing
                                    messages. voice-class sip tenant 100 The dial-peer inherits all
                                parameters configured globally and in tenant 100. Parameters may be
                                overridden at the dial-peer
                                level. srtp Enables SRTP for the call
                                leg. no vad Disables voice activity
                                detection. (Optional)  Force calls to audio only. Video over Webex Calling using Local Gateway call flows is not
                                supported. Although video can function in some scenarios, it can
                                result in degraded quality and unexpected behavior. To force calls
                                to audio only, apply the following command under your Webex Calling
                                dial-peers: voice-class sip audio forced If you choose to allow video, calls may not perform as expected. |
| 9 | To configure network devices such as CUBE and to forward Session Initiation Protocol (SIP) headers that the device doesn't process, use these commands. These commands enable the device to pass through unsupported SIP headers, including geo-location headers and PIDF-LO (Presence Information Data Format - Location Object), on the local gateway. This functionality supports Nomadic E911 services by ensuring that critical location information is preserved and forwarded correctly. Dial peer Configuration Voice service voip
 sip
  pass-thru headers unsupp Dial peer specific configuration Dial-peer voice 911 voip
 voice-class sip pass-thru headers unsupp Voice Class configuration for specific headers To proxy the Geo location headers: voice class sip-hdr-passthrulist 200 
 passthru-hdr Geolocation-Routing
 passthru-hdr Geolocation
 passthru-hdr-unsupp Apply the pass-through to the inbound/outbound dial-peer dial-peer voice 100 voip  // inbound
 voice-class sip pass-thru headers 200
dial-peer voice 200 voip  // outbound
 voice-class sip pass-thru headers 200 To enable the pass-through of the PIDFO body, use: voice service voip 
 sip 
  pass-thru content unsupp |

| 1 | Configure the following voice class uri to identify inbound calls from the PSTN
                    trunk: voice class uri 200 sip
  host ipv4:192.168.80.13 Here's an explanation of the fields for the configuration: voice class uri 200 sip Defines a
                        pattern to match an incoming SIP invite to an incoming trunk dial-peer. When
                        entering this pattern, use the IP address of your IP PSTN gateway. For more
                        information, see voice class uri . |
|---|---|
| 2 | Configure the following IP PSTN dial-peer: dial-peer voice 200 voip
 description Inbound/Outbound IP PSTN trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target ipv4:192.168.80.13
 incoming uri via 200
 voice-class sip asserted-id pai
 voice-class sip bind control source-interface GigabitEthernet0/0/0 
 voice-class sip bind media source-interface  GigabitEthernet0/0/0 
 voice-class codec 100
 dtmf-relay rtp-nte 
 no vad Here's an explanation of the fields for the
                        configuration: dial-peer voice 200 voip description Inbound/Outbound IP PSTN trunk Defines
                        a VoIP dial-peer with a tag of 200 and gives a meaningful description
                        for ease of management and troubleshooting. For more information, see dial-peer
                            voice. destination-pattern BAD.BAD A dummy destination pattern is
                        required when routing outbound calls using an inbound dial-peer group. Any
                        valid destination pattern may be used in this case. For more information,
                        see destination-pattern
                        (interface) . session protocol
                        sipv2 Specifies that this dial-peer handles SIP call legs.
                        For more information, see session protocol (dial
                            peer) . session target
                            ipv4: 192.168.80.13 Specifies the target
                        address for calls sent to the PSTN provider. This could be either an IP
                        address or DNS host name. For more information, see session target (VoIP dial
                        peer) . incoming uri via 200 Specifies the voice class used to match
                        incoming calls to this dial-peer using the INVITE VIA header URI. For more
                        information, see incoming url . voice-class sip asserted-id pai (Optional) Turns
                        on P-Asserted-Identity header processing and controls how this is used for
                        the PSTN trunk. If this command is used, the calling party identity provided
                        from the incoming dial-peer is used for the outgoing From and
                        P-Asserted-Identity headers. If this command is not used, the calling party
                        identity provided from the incoming dial-peer is used for the outgoing From
                        and Remote-Party-ID headers. For more information, see voice-class sip
                    asserted-id . bind control
                            source-interface GigabitEthernet0/0/0 Configures
                        the source interface and associated IP address for messages sent to the
                        PSTN. For more information, see bind . bind media
                            source-interface GigabitEthernet0/0/0 Configures
                        the source interface and associated IP address for media sent to PSTN. For
                        more information, see bind . voice-class
                            codec 100 Configures the dial-peer to use the
                        common codec filter list 100 . For more information, see voice-class
                            codec . dtmf-relay rtp-nte Defines
                        RTP-NTE (RFC2833) as the DTMF capability expected on the call leg. For more
                        information, see DTMF Relay (Voice over
                            IP) . no vad Disables voice
                        activity detection. For more information, see vad (dial peer) . |
| 3 | If you are configuring your Local Gateway to only route calls between Webex
                    Calling and the PSTN, add the following call routing configuration. If you are
                    configuring your Local Gateway with a Unified Communications Manager platform,
                    skip to the next section. Create dial-peer groups to route calls towards Webex Calling or the
                            PSTN. Define DPG 100 with outbound dial-peer 100 toward Webex Calling.
                            DPG 100 is applied to the incoming dial-peer from the PSTN. Similarly,
                            define DPG 200 with outbound dial-peer 200 toward the PSTN. DPG 200 is
                            applied to the incoming dial-peer from Webex. voice class dpg 100 
 description Route calls to Webex Calling 
 dial-peer 100 
voice class dpg 200 
 description Route calls to PSTN 
 dial-peer 200 Here's an explanation of the fields for the
                                configuration: dial-peer 100 Associates an outbound dial-peer with
                                a dial-peer group. For more information, see voice-class
                            dpg . Apply dial-peer groups to route calls from Webex to the PSTN and from
                            the PSTN to Webex: dial-peer voice 100
 destination dpg 200
dial-peer voice 200
 destination dpg 100 Here's an explanation of the fields for
                                the configuration: destination dpg 200 Specifies which dial-peer group,
                                and therefore dial-peer should be used for the outbound treatment
                                for calls presented to this incoming dial-peer. This
                                concludes your Local Gateway configuration. Save the configuration
                                and reload the platform if this is the first time CUBE features are
                                configured. |

| 1 | The loop-back dial-peer configuration uses dial-peer groups and call routing tags to
          ensure that calls pass correctly between Webex and the PSTN, without creating call routing
          loops. Configure the following translation rules that will be used to add and remove the
          call routing tags: voice translation-rule 100 
 rule 1 /^\+/ /A2A/ 

voice translation-profile 100 
 translate called 100 

voice translation-rule 200 
 rule 1 /^/ /A1A/ 

voice translation-profile 200 
 translate called 200 

voice translation-rule 11 
 rule 1 /^A1A/ // 

voice translation-profile 11 
 translate called 11 

voice translation-rule 12 
 rule 1 /^A2A44/ /0/
 rule 2/^A2A/ /00/

voice translation-profile 12 
 translate called 12 Here's an explanation of the fields for the configuration: voice translation-rule Uses regular expressions
            defined in rules to add or remove call routing tags. Over-decadic digits (‘A’) are used
            to add clarity for troubleshooting. In this configuration, the tag added by
            translation-profile 100 is used to guide calls from Webex Calling towards the PSTN via
            the loopback dial-peers. Similarly, the tag added by translation-profile 200 is used to
            guide calls from the PSTN towards Webex Calling. Translation-profiles 11 and 12 remove
            these tags before delivering calls to the Webex and PSTN trunks respectively. This example assumes that called numbers from Webex Calling are presented in
            +E.164 format. Rule 100 removes the leading + to maintain a valid called number. Rule 12
            then adds a national or international routing digit(s) when removing the tag. Use digits
            that suit your local ISDN national dial plan. If Webex Calling presents numbers in
            national format, adjust rules 100 and 12 to simply add and remove the routing tag
            respectively. For more information, see voice translation-profile and voice translation-rule . |
|---|---|
| 2 | Configure TDM voice interface ports as required by the trunk type and protocol used.
          For more information, see Configuring ISDN PRI . For example, the basic
          configuration of a Primary Rate ISDN interface installed in NIM slot 2 of a device might
          include the following: card type e1 0 2 
isdn switch-type primary-net5 
controller E1 0/2/0 
 pri-group timeslots 1-31 |
| 3 | Configure the following TDM PSTN dial-peer: dial-peer voice 200 pots 
 description Inbound/Outbound PRI PSTN trunk 
 destination-pattern BAD.BAD 
 translation-profile incoming 200 
 direct-inward-dial 
 port 0/2/0:15 Here's an explanation of the fields for the configuration: dial-peer voice 200 pots description Inbound/Outbound PRI PSTN trunk Defines
            a VoIP dial-peer with a tag of 200 and gives a meaningful description for ease of
            management and troubleshooting. For more information, see dial-peer voice . destination-pattern BAD.BAD A dummy
            destination pattern is required when routing outbound calls using an inbound dial-peer
            group. Any valid destination pattern may be used in this case. For more information, see destination-pattern (interface) . translation-profile incoming 200 Assigns
            the translation profile that will add a call routing tag to the incoming called number. direct-inward-dial Routes the call without providing a
            secondary dial-tone. For more information, see direct-inward-dial . port 0/2/0:15 The physical voice port associated with this
            dial-peer. |
| 4 | To enable media optimization of IP paths for Local Gateways with TDM-IP call flows, you
          can modify the call routing by introducing a set of internal loop-back dial-peers between
          Webex Calling and PSTN trunks. Configure the following loop-back dial-peers. In this case,
          all incoming calls will be routed initially to dial-peer 10 and from there to either
          dial-peer 11 or 12 based on the applied routing tag. After removal of the routing tag,
          calls will be routed to the outbound trunk using dial-peer groups. dial-peer voice 10 voip
 description Outbound loop-around leg
 destination-pattern BAD.BAD
 session protocol sipv2
 session target ipv4:192.168.80.14
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw
 no vad 

dial-peer voice 11 voip
 description Inbound loop-around leg towards Webex
 translation-profile incoming 11
 session protocol sipv2
 incoming called-number A1AT
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw
 no vad 

dial-peer voice 12 voip
 description Inbound loop-around leg towards PSTN
 translation-profile incoming 12
 session protocol sipv2
 incoming called-number A2AT
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw 
 no vad Here's an explanation of the fields for the configuration: dial-peer voice 10 voip description Outbound loop-around leg Defines a
            VoIP dial-peer and gives a meaningful description for ease of management and
            troubleshooting. For more information, see dial-peer voice . translation-profile incoming 11 Applies the
            translation profile defined earlier to remove the call routing tag before passing to the
            outbound trunk. destination-pattern BAD.BAD A
            dummy destination pattern is required when routing outbound calls using an inbound
            dial-peer group. For more information, see destination-pattern (interface) . session protocol sipv2 Specifies that this dial-peer
            handles SIP call legs. For more information, see session protocol (dial peer) . session target ipv4: 192.168.80.14 Specifies
            the local router interface address as the call target to loop-back. For more
            information, see session target (voip dial
              peer) . bind control
              source-interface GigabitEthernet0/0/0 Configures the source
            interface and associated IP address for messages sent through the loop-back. For more
            information, see bind . bind media
              source-interface GigabitEthernet0/0/0 Configures the source
            interface and associated IP address for media sent through the loop-back. For more
            information, see bind . dtmf-relay
            rtp-nte Defines RTP-NTE (RFC2833) as the DTMF capability expected on the
            call leg. For more information, see DTMF Relay (Voice over
                IP) . codec g711alaw Forces all PSTN
            calls to use G.711. Select a-law or u-law to match the companding method used by your
            ISDN service. no vad Disables voice activity detection.
            For more information, see vad (dial peer) . |
| 5 | Add the following call routing configuration: Create dial-peer groups to route calls between the PSTN and Webex trunks, via the
              loop-back. voice class dpg 100
 description Route calls to Webex Calling
 dial-peer 100
voice class dpg 200
 description Route calls to PSTN
 dial-peer 200
voice class dpg 10
 description Route calls to Loopback
 dial-peer 10 Here's an explanation of the fields for the configuration: dial-peer 100 Associates an outbound
                dial-peer with a dial-peer group. For more information, see voice-class dpg . Apply dial-peer groups to route calls. dial-peer voice 100
 destination dpg 10
dial-peer voice 200
 destination dpg 10
dial-peer voice 11
 destination dpg 100
dial-peer voice 12
 destination dpg 200 Here's an explanation of the fields for the
                configuration: destination dpg 200 Specifies which dial-peer group, and therefore
                dial-peer should be used for the outbound treatment for calls presented to this
                incoming dial-peer. This concludes your Local Gateway configuration. Save the configuration and reload the
          platform if this is the first time CUBE features are configured. |

| 1 | Configure the following voice class URIs: Classifies Unified CM to Webex calls using SIP VIA port: voice class uri 300 sip
 pattern :5065 Classifies Unified CM to PSTN calls using SIP via port: voice class uri 400 sip
 pattern 192\.168\.80\.6[0-5]:5060 Classify incoming messages from the UCM towards the PSTN trunk using
                                one or more patterns that describe the originating source addresses
                                and port number. Regular expressions may be used to define matching
                                patterns if required. In the example above, a regular expression is used to match any IP
                                address in the range 192.168.80.60 to 65 and port number 5060. |
|---|---|
| 2 | Configure the following DNS records to specify SRV routing to Unified CM
                    hosts: IOS XE uses these records for locally determining target UCM hosts and
                            ports. With this configuration, it is not required to configure records
                            in your DNS system. If you prefer to use your DNS, then these local
                            configurations are not required. ip host ucmpub.mydomain.com 192.168.80.60
ip host ucmsub1.mydomain.com 192.168.80.61
ip host ucmsub2.mydomain.com 192.168.80.62
ip host ucmsub3.mydomain.com 192.168.80.63
ip host ucmsub4.mydomain.com 192.168.80.64
ip host ucmsub5.mydomain.com 192.168.80.65
ip host _sip._udp.wxtocucm.io srv 0 1 5065 ucmpub.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub1.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub2.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub3.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub4.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub5.mydomain.com
ip host _sip._udp.pstntocucm.io srv 0 1 5060 ucmpub.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub1.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub2.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub3.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub4.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub5.mydomain.com Here's an explanation of the fields for the configuration: The following command creates a DNS SRV resource record. Create a record for
                        each UCM host and trunk: ip host _sip._udp.pstntocucm.io srv 2 1 5060
                                ucmsub5.mydomain.com _sip._udp.pstntocucm.io : SRV resource record name 2 : The SRV resource record priority 1 : The SRV resource record weight 5060 : The port number to use for the target host in this resource
                        record ucmsub5.mydomain.com : The resource record target host To resolve the resource record target host names, create local DNS A records.
                        For example: ip host ucmsub5.mydomain.com 192.168.80.65 ip host : Creates a record in the local IOS XE database. ucmsub5.mydomain.com : The A record host name. 192.168.80.65 : The host IP address. Create the SRV resource records and A records to reflect your UCM environment
                        and preferred call distribution strategy. |
| 3 | Configure the following dial-peers: Dial-peer for calls between Unified CM and Webex Calling: dial-peer voice 300 voip
 description UCM-Webex Calling trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target dns:wxtocucm.io
 incoming uri via 300
 voice-class codec 100
 voice-class sip bind control source-interface GigabitEthernet 0/0/0
 voice-class sip bind media source-interface GigabitEthernet 0/0/0
 dtmf-relay rtp-nte
 no vad Here's an explanation of the fields for the
                                configuration: dial-peer voice 300 voip description UCM-Webex Calling trunk Defines
                                a VoIP dial-peer with a tag 300 and gives a meaningful
                                description for ease of management and
                                    troubleshooting. destination-pattern
                                    BAD.BAD A dummy destination pattern is required
                                when routing outbound calls using an inbound dial-peer group. Any
                                valid destination pattern may be used in this
                                    case. session protocol
                                sipv2 Specifies that dial-peer 300 handles SIP call
                                legs. For more information, see session protocol
                                    (dial-peer) . session target
                                    dns:wxtocucm.io Defines the session target of
                                multiple Unified CM nodes through DNS SRV resolution. In this case,
                                the locally defined SRV record wxtocucm.io is used to direct
                                calls. incoming uri via 300 Uses
                                voice class URI 300 to direct all incoming traffic from Unified CM
                                using source port 5065 to this dial-peer. For more information,
                                    see incoming
                                    uri . voice-class codec 100 Indicates codec filter list for
                                calls to and from Unified CM. For more information, see voice class
                                    codec . bind control
                                    source-interface GigabitEthernet0/0/0 Configures the source interface and associated IP
                                address for messages sent to the PSTN. For more information,
                                    see bind . bind
                                    media
                                source-interface GigabitEthernet0/0/0 Configures the
                                source interface and associated IP address for media sent to PSTN.
                                For more information, see bind . dtmf-relay rtp-nte Defines
                                RTP-NTE (RFC2833) as the DTMF capability expected on the call leg.
                                For more information, see DTMF Relay (Voice over
                                IP) . no vad Disables voice
                                activity detection. For more information, see vad (dial
                            peer) . Dial-peer for calls between Unified CM and the PSTN: dial-peer voice 400 voip
 description UCM-PSTN trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target dns:pstntocucm.io
 incoming uri via 400
 voice-class codec 100 
 voice-class sip bind control source-interface GigabitEthernet 0/0/0
 voice-class sip bind media source-interface GigabitEthernet 0/0/0
 dtmf-relay rtp-nte
 no vad Here's an explanation of the fields for the
                                configuration: dial-peer voice 400 voip description UCM-PSTN trunk Defines
                                a VoIP dial-peer with a tag of 400 and gives a meaningful
                                description for ease of management and
                                    troubleshooting. destination-pattern
                                    BAD.BAD A dummy destination pattern is required
                                when routing outbound calls using an inbound dial-peer group. Any
                                valid destination pattern may be used in this
                                    case. session protocol
                                sipv2 Specifies that dial-peer 400 handles SIP call
                                legs. For more information, see session protocol
                                    (dial-peer) . session target
                                    dns:pstntocucm.io Defines the session target of
                                multiple Unified CM nodes through DNS SRV resolution. In this case,
                                the locally defined SRV record pstntocucm.io is used to direct
                                calls. incoming uri via 400 Uses voice class URI 400 to direct
                                all incoming traffic from the specified Unified CM hosts using
                                source port 5060 to this dial-peer. For more information, see incoming
                                    uri . voice-class codec 100 Indicates codec filter list for
                                calls to and from Unified CM. For more information, see voice class
                                    codec . bind control
                                    source-interface GigabitEthernet0/0/0 Configures the source interface and associated IP
                                address for messages sent to the PSTN. For more information,
                                    see bind . bind
                                    media
                                source-interface GigabitEthernet0/0/0 Configures the
                                source interface and associated IP address for media sent to PSTN.
                                For more information, see bind . dtmf-relay rtp-nte Defines
                                RTP-NTE (RFC2833) as the DTMF capability expected on the call leg.
                                For more information, see DTMF Relay (Voice over
                                IP) . no vad Disables voice
                                activity detection. For more information, see vad (dial
                            peer) . |
| 4 | Add call routing using the following configurations: Create dial-peer groups to route calls between Unified CM and Webex
                            Calling. Define DPG 100 with outbound dial-peer
                                100 towards Webex Calling. DPG 100 is applied to the
                            associated incoming dial-peer from Unified CM. Similarly, define DPG 300
                            with outbound dial-peer 300 toward Unified CM. DPG 300 is applied to the
                            incoming dial-peer from Webex. voice class dpg 100
 description Route calls to Webex Calling
 dial-peer 100
voice class dpg 300
 description Route calls to Unified CM Webex Calling trunk
 dial-peer 300 Create a dial-peer groups to route calls between Unified CM and the
                            PSTN. Define DPG 200 with outbound dial-peer
                                200 toward the PSTN. DPG 200 is applied to the
                            associated incoming dial-peer from Unified CM. Similarly, define DPG 400
                            with outbound dial-peer 400 toward Unified CM. DPG 400 is applied to the
                            incoming dial-peer from the PSTN. voice class dpg 200
 description Route calls to PSTN
 dial-peer 200
voice class dpg 400
 description Route calls to Unified CM PSTN trunk
 dial-peer 400 Here's an explanation of the fields for the
                                configuration: dial-peer 100 Associates
                                an outbound dial-peer with a dial-peer group. For more information,
                                    see voice-class dpg . Apply dial-peer groups to route calls from Webex to Unified CM and from
                            Unified CM to Webex: dial-peer voice 100
 destination dpg 300
dial-peer voice 300
 destination dpg 100 Here's an explanation of the fields for
                                the configuration: destination dpg 300 Specifies which dial-peer group,
                                and therefore dial-peer should be used for the outbound treatment
                                for calls presented to this incoming dial-peer. Apply dial-peer groups to route calls from the PSTN to Unified CM and
                            from Unified CM to the PSTN: dial-peer voice 200
 destination dpg 400
dial-peer voice 400
 destination dpg 200 This concludes your Local Gateway configuration. Save the
                                configuration and reload the platform if this is the first time CUBE
                                features have been configured. |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series |
| Product | CUBE Enterprise in Webex Calling Solution |
| Problem Scope | Performance |
| Problem Type | High CPU Utilization with Email Notification. |

| DS ID | DS Name | Revision | Status | Last Update (GMT+00:00) |
|---|---|---|---|---|
| 64224 | DS_LGW_CPU_MON75 | 0.0.10 | Registered | 2020-11-07 22:05:33 |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series |
| Product | CUBE Enterprise in Webex Calling Solution |
| Problem Scope | SIP-SIP |
| Problem Type | SIP Trunk Unregistration with Email Notification. |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series |
| Product | CUBE Enterprise in Webex Calling Solution |
| Problem Scope | Performance |
| Problem Type | SIP abnormal call disconnect detection with Email and Syslog Notification. |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series |
| Product | CUBE Enterprise in Webex Calling Solution |
| Problem Scope | Performance |
| Problem Type | High CPU Utilization with Email Notification. |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series or Cisco CSR 1000V Series |
| Product | CUBE Enterprise in Webex Calling Solution |
| Problem Scope | Syslogs |
| Problem Type | Syslog - %VOICE_IEC-3-GW: CCAPI: Internal Error (Call spike threshold):
                      IEC=1.1.181.1.29.0 |

| DS ID | DS Name | Revision | Status | Last Update (GMT+00:00) |
|---|---|---|---|---|
| 64224 00:07:45 | DS_LGW_CPU_MON75 | 0.0.10 | Registered | 2020-11-08 |
| 65095 00:12:53 | DS_LGW_IEC_Call_spike_threshold | 0.0.12 | Registered | 2020-11-08 |

| DS ID | DS Name | Revision | Status | Last Update (GMT+00:00) |
|---|---|---|---|---|
| 64224 | DS_LGW_CPU_MON75 | 0.0.10 | Registered | 2020-11-08 00:07:45 |
| 65095 | DS_LGW_IEC_Call_spike_threshold | 0.0.12 | Running | 2020-11-08 00:12:53 |

| DS ID | DS Name | Triggered /Max/Deinstall | Average Run Time (seconds) | Max Run Time (seconds) |
|---|---|---|---|---|
| 64224 | DS_LGW_CPU_MON75 | 0/0/N | 0.000 | 0.000 |
| 65095 | DS_LGW_IEC_Call_spike_threshold | 1 /20/Y | 23.053 | 23.053 |

| 1 | Ensure that you assign valid and routable IP addresses to any Layer 3 interfaces, for
          example: interface GigabitEthernet0/0/0
 description Interface facing PSTN and/or CUCM
 ip address 192.168.80.14 255.255.255.0
!
interface GigabitEthernet0/0/1
 description Interface facing Webex Calling (Public address)
 ip address 198.51.100.1 255.255.255.240 |
|---|---|
| 2 | Protect STUN credentials on the router using symmetric encryption. Configure the
          primary encryption key and encryption type as follows: key config-key password-encrypt YourPassword
password encryption aes |
| 3 | Create an encryption trustpoint with a certificate for your domain, signed by a supported Certificate Authority (CA). Create an RSA key pair using the following exec command. crypto key generate rsa general-keys exportable label lgw-key modulus 4096 Use the following configuration commands to create a trustpoint for the
              certificate, specifying the field values to use in the certificate signing request: crypto pki trustpoint LGW_CERT
 enrollment terminal pem
 fqdn none
 subject-name cn=cube1.lgw.com
 subject-alt-name cube1.lgw.com
 revocation-check none
 rsakeypair lgw-key
 hash sha256 Notes for certificate fields: fqdn : This isn’t a required field for Webex Calling. Setting this
                    configuration to "none" to not include this field in the Certificate Signing
                    Request. If you need to include an FQDN using this command, there is no impact
                    on the Local Gateway operation. subject-name : For validating calls from a Local Gateway, Webex must
                    match the FQDN in SIP contact headers with those included either in the Subject
                    Common Name (CN) attribute or the Subject Alternative Name (SAN) field of the
                    SBC certificate. The subject field must contain at least a CN attribute, and can
                    include other attributes, as required. For more information, see subject-name . Subject-alt-name : The Subject Alternative Name (SAN) field of the SBC
                    certificate can include a list of additional FQDNs. Webex checks this list to
                    validate the SIP contact header in messages from the Local Gateway if the
                    certificate Subject CN attribute is not matched. Hash : It’s recommended that Certificate Signing Request (CSR)s are
                    signed using SHA256. The Cisco IOS XE 17.11.1 uses this algorithm by default and
                    for earlier release, use the Hash command. Generate Certificate Signing Request (CSR) with the following exec or configuration
              command and use it to request a signed certificate from a supported CA provider: crypto pki enroll LGW_CERT |
| 4 | Provide the certificate of the intermediate signing CA to authenticate your host
          certificate. Enter the following exec or configuration command: crypto pki authenticate LGW_CERT
<paste Intermediate X.509 base 64 based certificate here> |
| 5 | Import the signed host certificate using the following exec or configuration
          command: crypto pki import LGW_CERT certificate
<paste CUBE host X.509 base 64 certificate here> |
| 6 | Enable TLS1.2 exclusivity and specify the default trustpoint to use for voice
          applications using the following configuration commands: sip-ua
  crypto signaling default trustpoint LGW_CERT
  transport tcp tls v1.2 |
| 7 | Install the Cisco root CA bundle, which includes the IdenTrust Commercial Root CA 1
          certificate used by Webex Calling. Use the crypto pki trustpool import clean
              url url command to download the root CA bundle from the
          specified URL, and to clear the current CA trustpool, then install the new bundle of
          certificates: If you need to use a proxy for access to the internet using
              HTTPS, add the following configuration before importing the CA bundle: ip http client proxy-server yourproxy.com proxy-port 80 ip http client source-interface GigabitEthernet0/0/1 
crypto pki trustpool import clean url https://www.cisco.com/security/pki/trs/ios_core.p7b |

| 1 | Create a CUBE certificate-based PSTN trunk for an existing location in the
                    Control Hub. For more information, see Configure trunks, route groups, and dial
                        plans for Webex Calling . Make a note of the trunk information on creating the trunk. These
                            details, as highlighted in the following illustration is used in the
                            configuration steps in this guide. |
|---|---|
| 2 | Enter the following commands to configure CUBE as a Webex Calling Local
                    Gateway: voice service voip
 ip address trusted list
  ipv4 x.x.x.x y.y.y.y
 mode border-element
 allow-connections sip to sip
 no supplementary-service sip refer
 stun
  stun flowdata agent-id 1 boot-count 4
  stun flowdata shared-secret 0 Password123$
 sip 
  asymmetric payload full
  early-offer forced
  sip-profiles inbound Here's an explanation of the fields for the configuration: ip address trusted list ipv4 x.x.x.x y.y.y.y To protect against toll fraud, the trusted address list defines a list of hosts and network entities from which the Local Gateway expects legitimate VoIP calls. By default, a Local Gateway blocks all incoming VoIP messages from IP addresses not in its trusted list. By default, statically configured dial-peers with “session target IP” or server group IP addresses are trusted. You need not add these IP addresses to the trusted list. When configuring your Local Gateway, add the IP subnets for your regional Webex Calling data center to the list, see Port Reference Information for Webex Calling for more information. Also, add address ranges for Unified Communications Manager servers (if used) and PSTN trunk gateways. For more information on how to use an IP address trusted list to prevent toll fraud, see IP address trusted . mode border-element Enables Cisco Unified Border Element (CUBE) features on the platform. allow-connections sip to sip Enable CUBE basic SIP back to back user agent functionality. For more information, see Allow connections . By default, T.38 fax transport is enabled. For more information, see fax protocol t38 (voice-service) . stun Enables STUN (Session Traversal of UDP through NAT) globally. These global stun commands are only required when deploying your Local Gateway behind NAT. The STUN bindings feature on the Local Gateway allows locally generated STUN requests to be sent over the negotiated media path. This helps to open the pinhole in the firewall. For more information, see stun flowdata agent-id and stun flowdata shared-secret . asymmetric payload full Configures SIP asymmetric payload support for both DTMF and dynamic codec payloads. For more information on this command, see asymmetric payload . early-offer forced Forces the Local Gateway to send SDP information in the initial INVITE message instead of waiting for acknowledgment from the neighboring peer. For more information on this command, see early-offer . sip-profiles inbound Enables CUBE to use SIP profiles to modify messages as they are received. Profiles are applied through dial-peers or tenants. |
| 3 | Configure voice class codec 100 allowing G.711 codecs only for all trunks. This simple approach is suitable for most deployments. If necessary, add additional codec types supported by both originating and terminating systems to the list. More complex solutions involving transcoding using DSP modules are supported, but not included in this guide. voice class codec 100
 codec preference 1 g711ulaw
 codec preference 2 g711alaw Here's an explanation of the fields for the configuration: voice class codec 100 Used to only allow preferred codecs for SIP trunk calls. For more information, see voice class codec . |
| 4 | Configure voice class stun-usage 100 to
                    enable ICE on the Webex Calling trunk. (This step is not applicable for Webex
                        for Government) voice class stun-usage 100 
 stun usage firewall-traversal flowdata
 stun usage ice lite Here's an explanation of the fields for the
                            configuration: stun usage ice lite Used
                        to enable ICE-Lite for all Webex Calling facing dial-peers to allow
                        media-optimization whenever possible. For more information, see voice class stun usage and stun usage ice lite . The stun usage firewall-traversal
                            flowdata command is only required when deploying your
                            Local Gateway behind NAT. Media optimization is negotiated wherever possible. If a call requires
                            cloud media services, such as recording, the media cannot be
                            optimized. |
| 5 | Configure the media encryption policy for Webex traffic. (This step is not
                        applicable for Webex for Government) voice class srtp-crypto 100
 crypto 1 AES_CM_128_HMAC_SHA1_80 Here's an explanation of the fields
                        for the configuration: voice class srtp-crypto 100 Specifies SHA1_80 as the only SRTP
                        cipher-suite CUBE offers in the SDP in offer and answer messages. Webex
                        Calling only supports SHA1_80. For more information, see voice class
                    srtp-crypto . |
| 6 | Configure FIPS-compliant GCM ciphers (This step is applicable only for Webex
                        for Government) . voice class srtp-crypto 100
crypto 1 AEAD_AES_256_GCM Here's an explanation of the fields for the
                            configuration: voice class srtp-crypto 100 Specifies GCM as the cipher-suite that
                        CUBE offers. It is mandatory to configure GCM ciphers for Local Gateway for
                        Webex for Government. |
| 7 | Configure a pattern to uniquely identify calls to a Local Gateway trunk based
                    on its destination FQDN or SRV: voice class uri 100 sip
 pattern cube1.lgw.com Here's an explanation of the fields for the configuration: voice class uri 100 sip Defines a pattern to match an incoming SIP invite to an incoming trunk dial-peer. When entering this pattern, use the trunk FQDN or SRV configured in the Control Hub for the trunk. During tenant-side configuration of certificate-based trunks for Webex
                            Calling, use only SRV-based Webex Calling Edge address on the Local
                            Gateway. FQDNs are no longer supported. |
| 8 | Configure SIP message manipulation profiles. If your gateway is configured with
                    a public IP address, configure a profile as follows or skip to the next step if
                    you are using NAT. In this example, cube1.lgw.com is the FQDN configured for the
                    Local Gateway: voice class sip-profiles 100
 rule 10 request ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:" 
 rule 20 response ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:" Here's an explanation of the fields for the
                        configuration: rules 10 and 20 To allow Webex to authenticate
                        messages from your local gateway, the 'Contact' header in a SIP request and
                        responses messages must contain the value provisioned for the trunk in the
                        Control Hub. This will either be the FQDN of a single host, or the SRV name
                        used for a cluster of devices. |
| 9 | If your gateway is configured with a private IP address behind static NAT,
                    configure the inbound and outbound SIP profiles as follows. In this example,
                    cube1.lgw.com is the FQDN configured for the Local Gateway, "10.80.13.12" is the
                    interface IP address facing Webex Calling and "192.65.79.20" is the NAT public
                    IP address. SIP profiles for outbound messages to Webex
                        Calling voice class sip-profiles 100
 rule 10 request ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:"
 rule 20 response ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:"
 rule 30 response ANY sdp-header Audio-Attribute modify "(a=candidate:1 1.*) 10.80.13.12" "\1 192.65.79.20"
 rule 31 response ANY sdp-header Audio-Attribute modify "(a=candidate:1 2.*) 10.80.13.12" "\1 192.65.79.20"
 rule 40 response ANY sdp-header Audio-Connection-Info modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 41 request ANY sdp-header Audio-Connection-Info modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 50 request ANY sdp-header Connection-Info modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 51 response ANY sdp-header Connection-Info modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 60 response ANY sdp-header Session-Owner modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 61 request ANY sdp-header Session-Owner modify "IN IP4 10.80.13.12" "IN IP4 192.65.79.20"
 rule 70 request ANY sdp-header Audio-Attribute modify "(a=rtcp:.*) 10.80.13.12" "\1 192.65.79.20"
 rule 71 response ANY sdp-header Audio-Attribute modify "(a=rtcp:.*) 10.80.13.12" "\1 192.65.79.20"
 rule 80 request ANY sdp-header Audio-Attribute modify "(a=candidate:1 1.*) 10.80.13.12" "\1 192.65.79.20"
 rule 81 request ANY sdp-header Audio-Attribute modify "(a=candidate:1 2.*) 10.80.13.12" "\1 192.65.79.20" Here's
                        an explanation of the fields for the configuration: rules 10
                            and 20 To allow Webex to authenticate messages from your
                        local gateway, the 'Contact' header in SIP request and responses messages
                        must contain the value provisioned for the trunk in the Control Hub. This
                        will either be the FQDN of a single host, or the SRV name used for a cluster
                        of devices. rules 30 to 81 Convert private
                        address references to the external public address for the site, allowing
                        Webex to correctly interpret and route subsequent messages. SIP
                        profile for inbound messages from Webex
                        Calling voice class sip-profiles 110
 rule 10 response ANY sdp-header Video-Connection-Info modify "192.65.79.20" "10.80.13.12"
 rule 20 response ANY sip-header Contact modify "@.*:" "@cube1.lgw.com:"
 rule 30 response ANY sdp-header Connection-Info modify "192.65.79.20" "10.80.13.12"
 rule 40 response ANY sdp-header Audio-Connection-Info modify "192.65.79.20" "10.80.13.12"
 rule 50 response ANY sdp-header Session-Owner modify "192.65.79.20" "10.80.13.12"
 rule 60 response ANY sdp-header Audio-Attribute modify "(a=candidate:1 1.*) 192.65.79.20" "\1 10.80.13.12"
 rule 70 response ANY sdp-header Audio-Attribute modify "(a=candidate:1 2.*) 192.65.79.20" "\1 10.80.13.12"
 rule 80 response ANY sdp-header Audio-Attribute modify "(a=rtcp:.*) 192.65.79.20" "\1 10.80.13.12" Here's
                        an explanation of the fields for the configuration: rules 10
                            to 80 Convert public address references to the
                        configured private address, allowing CUBE to process the messages from
                        Webex. For more information, see voice class sip-profiles . United States or Canadian PSTN provider can offer the Caller ID
                            verification for Spam and fraud calls, with the additional configuration
                            mentioned in the Spam or fraud call indication in
                                Webex Calling article. |
| 10 | Configure a SIP Options keepalive with header modification profile. voice class sip-profiles 115
 rule 10 request OPTIONS sip-header Contact modify "<sip:.*:" "<sip:cube1.lgw.com:" 
 rule 30 request ANY sip-header Via modify "(SIP.*) 10.80.13.12" "\1 192.65.79.20"
 rule 40 response ANY sdp-header Connection-Info modify "10.80.13.12" "192.65.79.20"  
 rule 50 response ANY sdp-header Audio-Connection-Info modify "10.80.13.12" "192.65.79.20"
!
voice class sip-options-keepalive 100
 description Keepalive for Webex Calling
 up-interval 5
 transport tcp tls
 sip-profiles 115 Here's an explanation of the fields for the
                        configuration: voice class sip-options-keepalive 100 Configures a keepalive profile and enters
                        voice class configuration mode. You can configure the time (in seconds) at
                        which an SIP Out of Dialog Options Ping is sent to the dial-target when the
                        heartbeat connection to the endpoint is in UP or Down status. This
                        keepalive profile is triggered from the dial-peer configured towards Webex. To ensure that the contact headers include the SBC fully qualified
                        domain name, SIP profile 115 is used. Rules 30, 40, and 50 are required only
                        when the SBC is configured behind static NAT. In this example,
                        cube1.lgw.com is the FQDN selected for the Local Gateway and if static NAT
                        is used, "10.80.13.12" is the SBC interface IP address towards Webex Calling
                        and "192.65.79.20" is the NAT public IP address. |
| 11 | Configure Webex Calling trunk: Create voice class tenant 100 to
                            define and group configurations required specifically for the Webex
                            Calling trunk. Dial-peers associated with this tenant later inherits
                            these configurations: The following example uses the values illustrated in Step 1 for the purpose of this guide (shown in bold). Replace these with values for your trunk in your configuration. voice class tenant 100
 no remote-party-id
 sip-server dns:us25.sipconnect.bcld.webex.com
 srtp-crypto 100
 localhost dns:cube1.lgw.com
 session transport tcp tls
 no session refresh
 error-passthru
 rel1xx disable
 asserted-id pai
 bind control source-interface GigabitEthernet0/0/1
 bind media source-interface GigabitEthernet0/0/1
 no pass-thru content custom-sdp
 sip-profiles 100 
 sip-profiles 110 inbound
 privacy-policy passthru
! Here's an explanation of the fields for the configuration: voice class tenant 100 We recommend that you use tenants to configure trunks, which have their own TLS certificate, and CN or SAN validation list. Here, the tls-profile associated with the tenant contains the trust point to be used to accept or create new connections, and has the CN or SAN list to validate the incoming connections. For more information, see voice class tenant . no remote-party-id Disable the SIP Remote-Party-ID (RPID) header as Webex Calling supports PAI, which is enabled using a asserted-id pai command. For more information, see remote-party-id . sip-server dns: us25.sipconnect.bcld.webex.com Configures the target SIP server for the trunk. Use the Edge proxy SRV address provided in the Control Hub when you created your trunk srtp-crypto 100 Configures the preferred cipher-suites for the SRTP call leg (connection) (specified in Step 5). For more information, see voice class srtp-crypto . localhost dns: cube1.lgw.com Configures CUBE to replace the physical IP address in the From, Call-ID, and Remote-Party-ID headers in outgoing messages with the provided FQDN. Use the trunk FQDN or SRV configured in the Control Hub for the trunk here. session transport tcp tls Sets transport to TLS for associated dial-peers. For more information, see session-transport . no session refresh Disables SIP session refresh for calls between CUBE and Webex. For more information, see session refresh . error-passthru Specifies SIP error response pass-thru functionality. For more information, see error-passthru . rel1xx disable Disables the use of
                                reliable provisional responses for the Webex Calling trunk. For more
                                information, see rel1xx . asserted-id
                                pai (Optional) Turns on P-Asserted-Identity header
                                processing and controls how this is used for the Webex Calling
                                trunk. Webex Calling includes P-Asserted-Identity (PAI)
                                headers in outbound call INVITEs to the Local Gateway. If
                                this command is configured, caller information from the PAI header
                                is used to populate the outgoing From and PAI/Remote-Party-ID
                                headers. If this command is not configured, caller
                                information from the From header is used to populate the outgoing
                                From and PAI/Remote-Party-ID headers. For more information,
                                see asserted-id . bind control source-interface GigabitEthernet0/0/1 Configures the
                                source interface and associated IP address for messages sent to
                                Webex Calling. For more information, see bind . bind
                                    media source-interface GigabitEthernet0/0/1 Configures the
                                source interface and associated IP address for media sent to Webex
                                Calling. For more information, see bind . voice-class sip profiles 100 Applies the header modification profile
                                (Public IP or NAT addressing) to use for outbound messages. For more
                                information, see voice-class sip
                                profiles . voice-class sip profiles 110 inbound For LGW deployments behind NAT only: Applies the
                                header modification profile to use for inbound messages. For more
                                information, see voice-class sip
                                    profiles. privacy-policy passthru Configures CUBE to
                                transparently pass privacy headers from the received message to the
                                next call leg. For more information, see privacy-policy . Configure the Webex Calling trunk dial-peer. dial-peer voice 100 voip
 description Inbound/Outbound Webex Calling
 destination-pattern BAD.BAD
 session protocol sipv2
 session target sip-server
 incoming uri request 100
 voice-class codec 100
 voice-class stun-usage 100
 voice-class sip tenant 100
 voice-class sip options-keepalive profile 100
 dtmf-relay rtp-nte 
 srtp
 no vad Here's an explanation of the fields for the configuration: dial-peer voice 100 voip description Inbound/Outbound Webex Calling Defines a VoIP dial-peer with a tag of 100 and gives a meaningful description for ease of management and troubleshooting. For more information, see dial-peer voice . destination-pattern BAD.BAD A dummy destination pattern is required when routing outbound calls using an inbound dial-peer group. You can use any valid destination pattern in this case. For more information, see destination-pattern (interface) . session protocol sipv2 Specifies that this dial-peer handles SIP call legs. For more information, see session protocol (dial-peer) . session target sip-server Indicates that the SIP server defined in tenant 100 is inherited and used for the destination for calls from this dial peer. incoming uri request 100 Specifies the voice class used to match incoming calls to this dial-peer using the INVITE REQUEST header URI. For more information, see incoming uri . voice-class codec 100 Indicates codec filter list for calls to and from Webex Calling. For more information, see voice class codec . voice-class stun-usage 100 Allows locally generated STUN requests from the Local Gateway to be sent over the negotiated media path. STUN packets help to open a firewall pinhole for media traffic and detect valid paths for media optimization. voice-class sip tenant 100 The dial-peer inherits all parameters configured globally and in tenant 100. Parameters may overridden at the dial-peer level. For more information, see voice-class sip tenant . voice-class sip options-keepalive profile 100 This command monitors the availability of a group of SIP servers or endpoints using a specific profile (100). srtp Enables SRTP for the call leg. (Optional)  Force calls to audio only. Video over Webex Calling using Local Gateway call flows is not
                                supported. Although video can function in some scenarios, it can
                                result in degraded quality and unexpected behavior. To force calls
                                to audio only, apply the following command under your Webex Calling
                                dial-peers: voice-class sip audio forced If you choose to allow video, calls may not perform as expected. |
| 12 | (Optional) To configure network devices such as CUBE and to forward Session
                    Initiation Protocol (SIP) headers that the device doesn't process, use these
                    commands. These commands enable the device to pass through unsupported SIP
                    headers, including geo-location headers and PIDF-LO (Presence Information Data
                    Format - Location Object), on the local gateway. This functionality supports
                    Nomadic E-911 services by ensuring that critical location information is
                    preserved and forwarded correctly. Dial peer Configuration Voice service voip
 sip
  pass-thru headers unsupp Dial-peer specific configuration Dial-peer voice 911 voip
 voice-class sip pass-thru headers unsupp Voice Class configuration for specific headers To proxy the Geo location headers: voice class sip-hdr-passthrulist 200 
 passthru-hdr Geolocation-Routing
 passthru-hdr Geolocation
 passthru-hdr-unsupp Apply the pass-through to the inbound/outbound dial-peer dial-peer voice 100 voip  // inbound
 voice-class sip pass-thru headers 200
dial-peer voice 200 voip  // outbound
 voice-class sip pass-thru headers 200 To enable the pass-through of the PIDFO body, use: voice service voip 
 sip 
  pass-thru content unsupp |

| 1 | Configure the following voice class uri to identify inbound calls from the PSTN
                    trunk: voice class uri 200 sip
  host ipv4:192.168.80.13 Here's an explanation of the fields for the configuration: voice class uri 200 sip Defines a
                        pattern to match an incoming SIP invite to an incoming trunk dial-peer. When
                        entering this pattern, use the IP address of your IP PSTN gateway. For more
                        information, see voice class uri . |
|---|---|
| 2 | Configure the following IP PSTN dial-peer: dial-peer voice 200 voip
 description Inbound/Outbound IP PSTN trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target ipv4:192.168.80.13
 incoming uri via 200
 voice-class sip asserted-id pai
 voice-class sip bind control source-interface GigabitEthernet0/0/0 
 voice-class sip bind media source-interface  GigabitEthernet0/0/0 
 voice-class codec 100
 dtmf-relay rtp-nte 
 no vad Here's an explanation of the fields for the
                        configuration: dial-peer voice 200 voip description Inbound/Outbound IP PSTN trunk Defines
                        a VoIP dial-peer with a tag of 200 and gives a meaningful description
                        for ease of management and troubleshooting. For more information, see dial-peer
                            voice. destination-pattern BAD.BAD A dummy destination pattern is
                        required when routing outbound calls using an inbound dial-peer group. Any
                        valid destination pattern may be used in this case. For more information,
                        see destination-pattern
                        (interface) . session protocol
                        sipv2 Specifies that this dial-peer handles SIP call legs.
                        For more information, see session protocol (dial
                            peer) . session target
                            ipv4: 192.168.80.13 Specifies the target
                        address for calls sent to the PSTN provider. This could be either an IP
                        address or DNS host name. For more information, see session target (VoIP dial
                        peer) . incoming uri via 200 Specifies the voice class used to match
                        incoming calls to this dial-peer using the INVITE VIA header URI. For more
                        information, see incoming url . voice-class sip asserted-id pai (Optional) Turns
                        on P-Asserted-Identity header processing and controls how this is used for
                        the PSTN trunk. If this command is used, the calling party identity provided
                        from the incoming dial-peer is used for the outgoing From and
                        P-Asserted-Identity headers. If this command is not used, the calling party
                        identity provided from the incoming dial-peer is used for the outgoing From
                        and Remote-Party-ID headers. For more information, see voice-class sip
                    asserted-id . bind control
                            source-interface GigabitEthernet0/0/0 Configures
                        the source interface and associated IP address for messages sent to the
                        PSTN. For more information, see bind . bind media
                            source-interface GigabitEthernet0/0/0 Configures
                        the source interface and associated IP address for media sent to PSTN. For
                        more information, see bind . voice-class
                            codec 100 Configures the dial-peer to use the
                        common codec filter list 100 . For more information, see voice-class
                            codec . dtmf-relay rtp-nte Defines
                        RTP-NTE (RFC2833) as the DTMF capability expected on the call leg. For more
                        information, see DTMF Relay (Voice over
                            IP) . no vad Disables voice
                        activity detection. For more information, see vad (dial peer) . |
| 3 | If you are configuring your Local Gateway to only route calls between Webex
                    Calling and the PSTN, add the following call routing configuration. If you are
                    configuring your Local Gateway with a Unified Communications Manager platform,
                    skip to the next section. Create dial-peer groups to route calls towards Webex Calling or the
                            PSTN. Define DPG 100 with outbound dial-peer 100 toward Webex Calling.
                            DPG 100 is applied to the incoming dial-peer from the PSTN. Similarly,
                            define DPG 200 with outbound dial-peer 200 toward the PSTN. DPG 200 is
                            applied to the incoming dial-peer from Webex. voice class dpg 100 
 description Route calls to Webex Calling 
 dial-peer 100 
voice class dpg 200 
 description Route calls to PSTN 
 dial-peer 200 Here's an explanation of the fields for the
                                configuration: dial-peer 100 Associates an outbound dial-peer with
                                a dial-peer group. For more information, see voice-class
                            dpg . Apply dial-peer groups to route calls from Webex to the PSTN and from
                            the PSTN to Webex: dial-peer voice 100
 destination dpg 200
dial-peer voice 200
 destination dpg 100 Here's an explanation of the fields for
                                the configuration: destination dpg 200 Specifies which dial-peer group,
                                and therefore dial-peer should be used for the outbound treatment
                                for calls presented to this incoming dial-peer. This
                                concludes your Local Gateway configuration. Save the configuration
                                and reload the platform if this is the first time CUBE features are
                                configured. |

| 1 | The loop-back dial-peer configuration uses dial-peer groups and call routing tags to
          ensure that calls pass correctly between Webex and the PSTN, without creating call routing
          loops. Configure the following translation rules that will be used to add and remove the
          call routing tags: voice translation-rule 100 
 rule 1 /^\+/ /A2A/ 

voice translation-profile 100 
 translate called 100 

voice translation-rule 200 
 rule 1 /^/ /A1A/ 

voice translation-profile 200 
 translate called 200 

voice translation-rule 11 
 rule 1 /^A1A/ // 

voice translation-profile 11 
 translate called 11 

voice translation-rule 12 
 rule 1 /^A2A44/ /0/
 rule 2/^A2A/ /00/

voice translation-profile 12 
 translate called 12 Here's an explanation of the fields for the configuration: voice translation-rule Uses regular expressions
            defined in rules to add or remove call routing tags. Over-decadic digits (‘A’) are used
            to add clarity for troubleshooting. In this configuration, the tag added by
            translation-profile 100 is used to guide calls from Webex Calling towards the PSTN via
            the loopback dial-peers. Similarly, the tag added by translation-profile 200 is used to
            guide calls from the PSTN towards Webex Calling. Translation-profiles 11 and 12 remove
            these tags before delivering calls to the Webex and PSTN trunks respectively. This example assumes that called numbers from Webex Calling are presented in
            +E.164 format. Rule 100 removes the leading + to maintain a valid called number. Rule 12
            then adds a national or international routing digit(s) when removing the tag. Use digits
            that suit your local ISDN national dial plan. If Webex Calling presents numbers in
            national format, adjust rules 100 and 12 to simply add and remove the routing tag
            respectively. For more information, see voice translation-profile and voice translation-rule . |
|---|---|
| 2 | Configure TDM voice interface ports as required by the trunk type and protocol used.
          For more information, see Configuring ISDN PRI . For example, the basic
          configuration of a Primary Rate ISDN interface installed in NIM slot 2 of a device might
          include the following: card type e1 0 2 
isdn switch-type primary-net5 
controller E1 0/2/0 
 pri-group timeslots 1-31 |
| 3 | Configure the following TDM PSTN dial-peer: dial-peer voice 200 pots 
 description Inbound/Outbound PRI PSTN trunk 
 destination-pattern BAD.BAD 
 translation-profile incoming 200 
 direct-inward-dial 
 port 0/2/0:15 Here's an explanation of the fields for the configuration: dial-peer voice 200 pots description Inbound/Outbound PRI PSTN trunk Defines
            a VoIP dial-peer with a tag of 200 and gives a meaningful description for ease of
            management and troubleshooting. For more information, see dial-peer voice . destination-pattern BAD.BAD A dummy
            destination pattern is required when routing outbound calls using an inbound dial-peer
            group. Any valid destination pattern may be used in this case. For more information, see destination-pattern (interface) . translation-profile incoming 200 Assigns
            the translation profile that will add a call routing tag to the incoming called number. direct-inward-dial Routes the call without providing a
            secondary dial-tone. For more information, see direct-inward-dial . port 0/2/0:15 The physical voice port associated with this
            dial-peer. |
| 4 | To enable media optimization of IP paths for Local Gateways with TDM-IP call flows, you
          can modify the call routing by introducing a set of internal loop-back dial-peers between
          Webex Calling and PSTN trunks. Configure the following loop-back dial-peers. In this case,
          all incoming calls will be routed initially to dial-peer 10 and from there to either
          dial-peer 11 or 12 based on the applied routing tag. After removal of the routing tag,
          calls will be routed to the outbound trunk using dial-peer groups. dial-peer voice 10 voip
 description Outbound loop-around leg
 destination-pattern BAD.BAD
 session protocol sipv2
 session target ipv4:192.168.80.14
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw
 no vad 

dial-peer voice 11 voip
 description Inbound loop-around leg towards Webex
 translation-profile incoming 11
 session protocol sipv2
 incoming called-number A1AT
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw
 no vad 

dial-peer voice 12 voip
 description Inbound loop-around leg towards PSTN
 translation-profile incoming 12
 session protocol sipv2
 incoming called-number A2AT
 voice-class sip bind control source-interface GigabitEthernet0/0/0
 voice-class sip bind media source-interface GigabitEthernet0/0/0
 dtmf-relay rtp-nte
 codec g711alaw 
 no vad Here's an explanation of the fields for the configuration: dial-peer voice 10 voip description Outbound loop-around leg Defines a
            VoIP dial-peer and gives a meaningful description for ease of management and
            troubleshooting. For more information, see dial-peer voice . translation-profile incoming 11 Applies the
            translation profile defined earlier to remove the call routing tag before passing to the
            outbound trunk. destination-pattern BAD.BAD A
            dummy destination pattern is required when routing outbound calls using an inbound
            dial-peer group. For more information, see destination-pattern (interface) . session protocol sipv2 Specifies that this dial-peer
            handles SIP call legs. For more information, see session protocol (dial peer) . session target ipv4: 192.168.80.14 Specifies
            the local router interface address as the call target to loop-back. For more
            information, see session target (voip dial
              peer) . bind control
              source-interface GigabitEthernet0/0/0 Configures the source
            interface and associated IP address for messages sent through the loop-back. For more
            information, see bind . bind media
              source-interface GigabitEthernet0/0/0 Configures the source
            interface and associated IP address for media sent through the loop-back. For more
            information, see bind . dtmf-relay
            rtp-nte Defines RTP-NTE (RFC2833) as the DTMF capability expected on the
            call leg. For more information, see DTMF Relay (Voice over
                IP) . codec g711alaw Forces all PSTN
            calls to use G.711. Select a-law or u-law to match the companding method used by your
            ISDN service. no vad Disables voice activity detection.
            For more information, see vad (dial peer) . |
| 5 | Add the following call routing configuration: Create dial-peer groups to route calls between the PSTN and Webex trunks, via the
              loop-back. voice class dpg 100
 description Route calls to Webex Calling
 dial-peer 100
voice class dpg 200
 description Route calls to PSTN
 dial-peer 200
voice class dpg 10
 description Route calls to Loopback
 dial-peer 10 Here's an explanation of the fields for the configuration: dial-peer 100 Associates an outbound
                dial-peer with a dial-peer group. For more information, see voice-class dpg . Apply dial-peer groups to route calls. dial-peer voice 100
 destination dpg 10
dial-peer voice 200
 destination dpg 10
dial-peer voice 11
 destination dpg 100
dial-peer voice 12
 destination dpg 200 Here's an explanation of the fields for the
                configuration: destination dpg 200 Specifies which dial-peer group, and therefore
                dial-peer should be used for the outbound treatment for calls presented to this
                incoming dial-peer. This concludes your Local Gateway configuration. Save the configuration and reload the
          platform if this is the first time CUBE features are configured. |

| 1 | Configure the following voice class URIs: Classifies Unified CM to Webex calls using SIP VIA port: voice class uri 300 sip
 pattern :5065 Classifies Unified CM to PSTN calls using SIP via port: voice class uri 400 sip
 pattern 192\.168\.80\.6[0-5]:5060 Classify incoming messages from the UCM towards the PSTN trunk using one or more
                patterns that describe the originating source addresses and port number. Regular
                expressions may be used to define matching patterns if required. In the example above, a regular expression is used to match any IP address in the
                range 192.168.80.60 to 65 and port number 5060. |
|---|---|
| 2 | Configure the following DNS records to specify SRV routing to Unified CM hosts: IOS XE uses these records for locally determining target UCM hosts and ports. With
              this configuration, it is not required to configure records in your DNS system. If you
              prefer to use your DNS, then these local configurations are not required. ip host ucmpub.mydomain.com 192.168.80.60
ip host ucmsub1.mydomain.com 192.168.80.61
ip host ucmsub2.mydomain.com 192.168.80.62
ip host ucmsub3.mydomain.com 192.168.80.63
ip host ucmsub4.mydomain.com 192.168.80.64
ip host ucmsub5.mydomain.com 192.168.80.65
ip host _sip._udp.wxtocucm.io srv 0 1 5065 ucmpub.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub1.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub2.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub3.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub4.mydomain.com
ip host _sip._udp.wxtocucm.io srv 2 1 5065 ucmsub5.mydomain.com
ip host _sip._udp.pstntocucm.io srv 0 1 5060 ucmpub.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub1.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub2.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub3.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub4.mydomain.com
ip host _sip._udp.pstntocucm.io srv 2 1 5060 ucmsub5.mydomain.com Here's an explanation of the fields for the configuration: The following command creates a DNS SRV resource record. Create a record for each UCM
            host and trunk: ip host _sip._udp.pstntocucm.io srv 2 1 5060
              ucmsub5.mydomain.com _sip._udp.pstntocucm.io : SRV resource record name 2 : The SRV resource record priority 1 : The SRV resource record weight 5060 : The port number to use for the target host in this resource record ucmsub5.mydomain.com : The resource record target host To resolve the resource record target host names, create local DNS A records. For
            example: ip host ucmsub5.mydomain.com 192.168.80.65 ip host : Creates a record in the local IOS XE database. ucmsub5.mydomain.com : The A record host name. 192.168.80.65 : The host IP address. Create the SRV resource records and A records to reflect your UCM environment and
            preferred call distribution strategy. |
| 3 | Configure the following dial-peers: Dial-peer for calls between Unified CM and Webex Calling: dial-peer voice 300 voip
 description UCM-Webex Calling trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target dns:wxtocucm.io
 incoming uri via 300
 voice-class codec 100
 voice-class sip bind control source-interface GigabitEthernet 0/0/0
 voice-class sip bind media source-interface GigabitEthernet 0/0/0
 dtmf-relay rtp-nte
 no vad Here's an explanation of the fields for the
                configuration: dial-peer voice 300 voip description UCM-Webex Calling trunk Defines
                a VoIP dial-peer with a tag 300 and gives a meaningful description for ease
                of management and troubleshooting. destination-pattern
                BAD.BAD A dummy destination pattern is required when routing
                outbound calls using an inbound dial-peer group. Any valid destination pattern may
                be used in this case. session protocol
                sipv2 Specifies that dial-peer 300 handles SIP call legs. For more
                information, see session protocol
                  (dial-peer) . session target
                dns:wxtocucm.io Defines the session target of multiple Unified CM
                nodes through DNS SRV resolution. In this case, the locally defined SRV record
                wxtocucm.io is used to direct calls. incoming uri via
                300 Uses voice class URI 300 to direct all incoming traffic from
                Unified CM using source port 5065 to this dial-peer. For more information, see incoming uri . voice-class
                  codec 100 Indicates codec filter list for calls to and
                from Unified CM. For more information, see voice class codec . bind
                  control source-interface GigabitEthernet0/0/0 Configures the
                source interface and associated IP address for messages sent to the PSTN. For more
                information, see bind . bind media
                  source-interface GigabitEthernet0/0/0 Configures the source
                interface and associated IP address for media sent to PSTN. For more information,
                  see bind . dtmf-relay
                  rtp-nte Defines RTP-NTE (RFC2833) as the DTMF capability expected
                on the call leg. For more information, see DTMF Relay (Voice over IP) . no vad Disables voice activity detection. For
                more information, see vad (dial peer) . Dial-peer for calls between Unified CM and the PSTN: dial-peer voice 400 voip
 description UCM-PSTN trunk
 destination-pattern BAD.BAD
 session protocol sipv2
 session target dns:pstntocucm.io
 incoming uri via 400
 voice-class codec 100 
 voice-class sip bind control source-interface GigabitEthernet 0/0/0
 voice-class sip bind media source-interface GigabitEthernet 0/0/0
 dtmf-relay rtp-nte
 no vad Here's an explanation of the fields for the
                configuration: dial-peer voice 400 voip description UCM-PSTN trunk Defines a VoIP
                dial-peer with a tag of 400 and gives a meaningful description for ease of
                management and troubleshooting. destination-pattern
                BAD.BAD A dummy destination pattern is required when routing
                outbound calls using an inbound dial-peer group. Any valid destination pattern may
                be used in this case. session protocol
                sipv2 Specifies that dial-peer 400 handles SIP call legs. For more
                information, see session protocol
                  (dial-peer) . session target
                dns:pstntocucm.io Defines the session target of multiple Unified CM
                nodes through DNS SRV resolution. In this case, the locally defined SRV record
                pstntocucm.io is used to direct calls. incoming uri via 400 Uses voice class URI 400 to direct all incoming
                traffic from the specified Unified CM hosts using source port 5060 to this
                dial-peer. For more information, see incoming uri . voice-class
                  codec 100 Indicates codec filter list for calls to and
                from Unified CM. For more information, see voice class codec . bind
                  control source-interface GigabitEthernet0/0/0 Configures the
                source interface and associated IP address for messages sent to the PSTN. For more
                information, see bind . bind media
                  source-interface GigabitEthernet0/0/0 Configures the source
                interface and associated IP address for media sent to PSTN. For more information,
                  see bind . dtmf-relay
                  rtp-nte Defines RTP-NTE (RFC2833) as the DTMF capability expected
                on the call leg. For more information, see DTMF Relay (Voice over IP) . no vad Disables voice activity detection. For
                more information, see vad (dial peer) . |
| 4 | Add call routing using the following configurations: Create dial-peer groups to route calls between Unified CM and Webex Calling. Define
              DPG 100 with outbound dial-peer 100 towards Webex Calling.
              DPG 100 is applied to the associated incoming dial-peer from Unified CM. Similarly,
              define DPG 300 with outbound dial-peer 300 toward Unified CM. DPG 300 is applied to
              the incoming dial-peer from Webex. voice class dpg 100
 description Route calls to Webex Calling
 dial-peer 100
voice class dpg 300
 description Route calls to Unified CM Webex Calling trunk
 dial-peer 300 Create a dial-peer groups to route calls between Unified CM and the PSTN. Define
              DPG 200 with outbound dial-peer 200 toward the PSTN. DPG 200
              is applied to the associated incoming dial-peer from Unified CM. Similarly, define DPG
              400 with outbound dial-peer 400 toward Unified CM. DPG 400 is applied to the incoming
              dial-peer from the PSTN. voice class dpg 200
 description Route calls to PSTN
 dial-peer 200
voice class dpg 400
 description Route calls to Unified CM PSTN trunk
 dial-peer 400 Here's an explanation of the fields for the
                configuration: dial-peer 100 Associates an
                outbound dial-peer with a dial-peer group. For more information, see voice-class dpg . Apply dial-peer groups to route calls from Webex to Unified CM and from Unified CM
              to Webex: dial-peer voice 100
 destination dpg 300
dial-peer voice 300
 destination dpg 100 Here's an explanation of the fields for the
                configuration: destination dpg 300 Specifies which dial-peer group, and therefore
                dial-peer should be used for the outbound treatment for calls presented to this
                incoming dial-peer. Apply dial-peer groups to route calls from the PSTN to Unified CM and from Unified
              CM to the PSTN: dial-peer voice 200
 destination dpg 400
dial-peer voice 400
 destination dpg 200 This concludes your Local Gateway configuration. Save the configuration and reload
                the platform if this is the first time CUBE features have been configured. |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series, or Catalyst 8000V Edge Software |
| Product | CUBE Enterprise in Webex Calling solution |
| Problem Scope | Performance |
| Problem Type | High CPU Utilization with Email Notification |

| DS ID | DS Name | Revision | Status | Last Update (GMT+00:00) |
|---|---|---|---|---|
| 64224 | DS_LGW_CPU_MON75 | 0.0.10 | Registered | 2020-11-07 22:05:33 |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series, or Catalyst 8000V Edge Software |
| Product | CUBE Enterprise in Webex Calling Solution |
| Problem Scope | Performance |
| Problem Type | SIP abnormal call disconnect detection with Email and Syslog Notification. |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series, or Catalyst 8000V Edge Software |
| Product | CUBE Enterprise in Webex Calling Solution |
| Problem Scope | Performance |
| Problem Type | High CPU Utilization with Email Notification. |

| Field Name | Field Value |
|---|---|
|  |
| Platform | Cisco 4300, 4400 ISR Series, or Catalyst 8000V Edge Software |
| Product | CUBE Enterprise in Webex Calling Solution |
| Problem Scope | Syslogs |
| Problem Type | Syslog - %VOICE_IEC-3-GW: CCAPI: Internal Error (Call spike threshold):
                      IEC=1.1.181.1.29.0 |

| DS ID | DS Name | Revision | Status | Last Update (GMT+00:00) |
|---|---|---|---|---|
| 64224 00:07:45 | DS_LGW_CPU_MON75 | 0.0.10 | Registered | 2020-11-08:00:07:45 |
| 65095 00:12:53 | DS_LGW_IEC_Call_spike_threshold | 0.0.12 | Registered | 2020-11-08:00:12:53 |

| DS ID | DS Name | Revision | Status | Last Update (GMT+00:00) |
|---|---|---|---|---|
| 64224 | DS_LGW_CPU_MON75 | 0.0.10 | Registered | 2020-11-08 00:07:45 |
| 65095 | DS_LGW_IEC_Call_spike_threshold | 0.0.12 | Running | 2020-11-08 00:12:53 |

| DS ID | DS Name | Triggered /Max/Deinstall | Average Run Time (seconds) | Max Run Time (seconds) |
|---|---|---|---|---|
| 64224 | DS_LGW_CPU_MON75 | 0/0/N | 0.000 | 0.000 |
| 65095 | DS_LGW_IEC_Call_spike_threshold | 1 /20/Y | 23.053 | 23.053 |

## Figuras

![Call routing from/to PSTN to/from Webex Calling configuration solution](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/479001-480000/479480.png)

![Call routing configuration with a set of internal loop-back dial-peers between Webex Calling and PSTN trunks](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/482001-483000/482796.png)

![Solution diagram showing Unified Communications Manager provides centralized routing and treatment of all PSTN and Webex Calling calls](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/479001-480000/479481.png)

![The host names, IP addresses, and interfaces used in Call routing configuration solutions](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/482001-483000/482562.png)

![PSTN trunk registered](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/482001-483000/482618.png)

![Flow diagram of authentication and registration of Webex Calling with Local gateway](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/500001-600000/500001-510000/502001-503000/502346.jpg)

![Enter SIP trunk security profile information](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483179.png)

![The host names, IP addresses, and interfaces used in certificate based local gateway configurations](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/479001-480000/479482.png)

![CUBE certificate-based PSTN trunk group is created](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/493001-494000/493824.png)

![Download DS 64224 from Diagnostic Signatures Lookup tool](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/456001-457000/456088.jpg)

![The file upload token generated in the Attachments section of the Support Case Manager](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/456001-457000/456089.jpg)

![Notification email that is sent during Diagnostic Signature execution](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/456001-457000/456090.jpg)