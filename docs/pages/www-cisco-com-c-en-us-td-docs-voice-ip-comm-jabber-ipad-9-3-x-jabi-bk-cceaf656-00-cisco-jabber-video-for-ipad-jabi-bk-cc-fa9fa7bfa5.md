---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-ipad-9-3-x-jabi-bk-cceaf656-00-cisco-jabber-video-for-ipad-jabi-bk-cc-fa9fa7bfa5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/iPad/9_3_x/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad_chapter_0110.html
retrieved_at: 2026-08-21T19:43:55.668860+00:00
---

Cisco Jabber Video for iPad 9.3.4 Administration Guide

# Cisco Jabber Video for iPad 9.3.4 Administration Guide

Updated: November 22, 2013

Chapter: Set up for Cisco TelePresence Video Communication Server

## Chapter: Set up for Cisco TelePresence Video Communication Server

# Set up for Cisco TelePresence Video Communication Server

This chapter provides comprehensive information about setting up Cisco Jabber Video for iPad using Cisco TelePresence Video Communication Server (VCS).

## Prerequisites

Perform these tasks:

- Determine if NTLM authentication is necessary in your network environment. If so, set up NTLM authentication with VCS and Cisco Jabber Video for iPad . For instructions, see the Cisco TelePresence Video Communication Server Authenticating Devices Deployment Guide for your release at http:/​/​www.cisco.com/​en/​US/​products/​ps11337/​products_​installation_​and_​configuration_​guides_​list.html .

## TMS Setup for Provisioning

To deploy VCS on Cisco Jabber Video for iPad , provision the user devices with appropriate settings. You add and manage desired settings in TMS. The data is then transferred to the VCS, from which it is distributed to the devices through the Provisioning Server running on the VCS.

Perform these two required procedures to set up TMS for provisioning.

- Defining Device Address Pattern

- Setting Up Provisioning Template and Assigning It to Users

### Defining Device Address Pattern

Device address patterns are templates that TMS Provisioning Extension (TMSPE) uses to create addresses for provisioned devices. Assign device address patterns so that TMSPE can connect users to their devices.

To specify a device address pattern for Cisco Jabber Video for iPad , set the attribute {device.model} to jabbertablet . Optionally, add an alias conversion from jabbertablet to jabber to simplify naming.

For detailed instructions about creating address patterns, see the Cisco TelePresence Management Suite Provisioning Extension Deployment Guide at http:/​/​www.cisco.com/​en/​US/​products/​ps11472/​prod_​installation_​guides_​list.html .

### Setting Up Provisioning Template and Assigning It to Users

Cisco Jabber Video for iPad requires a specific template—an XML file containing all the possible settings supported by the application. After you download the template and upload it in TMS, you can then set up the template and assign it to groups of users.

For detailed instructions about each of the steps in the procedure, consult the appropriate documentation:

- If you are using the TMS Agent Legacy, included in TMS versions 13.2 and earlier, see the Cisco TelePresence Management Suite Agent Legacy Deployment Guide at http:/​/​www.cisco.com/​en/​US/​products/​ps11338/​products_​installation_​and_​configuration_​guides_​list.html .

- If you are using the TMS Provisioning Extension (TMSPE), included in TMS versions 13.2 and later, see the Cisco TelePresence Management Suite Provisioning Extension Deployment Guide at http:/​/​www.cisco.com/​en/​US/​products/​ps11472/​prod_​installation_​guides_​list.html .

The term "template schema" is used in TMSPE while the term "template" is used in TMS Agent Legacy.

- Public SIP Server Address

- SIP Server Address

- Phone Book Server URI

Any template you assign to a group is inherited by all users in the group, all subgroups, and all users in subgroups. You cannot assign a template directly to an individual user.

Cisco recommends keeping all VCS templates for backwards client compatibility. Multiple templates can exist for a specific device type on each VCS and it is the client subscription request that indicates to the provisioning server which template to use. The provisioning server uses the Model and Version fields from the request to determine the correct template. If the Version string from the request is lower than all installed templates for that model, the provisioning request will fail. If the Version string from the request is higher than any installed templates for that model, a best effort attempt is made to find the closest matching template of equal or lower version.

## Understanding Provisioning Options

Provisioning allows you to specify settings that control how VCS works with Cisco Jabber Video for iPad . After subscribing to VCS, Cisco Jabber Video for iPad receives provisioning information from the Cisco TMS Agent and acts on it.

This table explains the provisioning options that are applicable for Cisco Jabber Video for iPad and includes tips on how you can use them.

- on - Allow users to save their password.

- off - Do not allow users to save their password.

- UseClientSetting - Automatic sign out is controlled by the client setting.

- NeverSignOut - Cisco Jabber will not automatically sign out.

- 15Minutes - Cisco Jabber will automatically sign out after 15 minutes in the background.

- 30Minutes - Cisco Jabber will automatically sign out after 30 minutes in the background.

- 1Hour - Cisco Jabber will automatically sign out after 1 hour in the background.

- 2Hour - Cisco Jabber will automatically sign out after 2 hours in the background.

- 4Hour - Cisco Jabber will automatically sign out after 4 hours in the background.

- 8Hour - Cisco Jabber will automatically sign out after 8 hours in the background.

- SignOutOnExit - Cisco Jabber will automatically sign out immediately after it goes into the background.

- TurnAuthPassword

- TurnAuthUsername

- TurnServer

After signing in, Jabber Video will probe the TURN relay server for the bandwidth quality between client and TURN server.

This setting determines the duration of the probing in seconds.

- Minimum value: 5

- Maximum value: 600

- Recommended value: 30

The provisioned time is split into 256 kb/s intervals up to the maximum provisioned bandwidth.

- TurnAuthPassword

- TurnAuthUsername

- TurnServer

ClearPath is a Cisco TelePresence solution that minimizes the negative effects of packet loss in a non-optimal network. Among the mechanisms used are H.264-specific error recovery techniques, feedback from decoders, and forward error correction (FEC).

Both call participants must be using devices that support ClearPath for it to take effect.

This is the address to use

- before ICE negotiation has completed;

- if ICE fails; or

- if the remote side does not understand ICE.

The available options are

- Host —the local network address

- Rflx —the corporate public IP address seen from outside of the organization's network (public IP)

- Relay —the address of the TURN relay server

You can use Relay if you are deploying Cisco Jabber Video for iPad in environments where most other devices do not understand ICE.

Determines the encryption policy for the account. This option affects both the SIP communication (Transport TLS or TCP) and the media communication (SRTP or no SRTP).

For a call to be encrypted, both the SIP and the media communication must be encrypted, and all parties must support encryption. Encrypted media communication is sent using the Secure Real-time Transport Protocol (SRTP) with a 128-bit Advanced Encryption Standard (AES). The Encryption policy setting is provisioned to the client as configured in Systems > Provisioning > Directory in Cisco TMS. Force TLS/TCP determines whether the SIP communication is encrypted (TLS) or not (TCP). The TLS version 1.0. Force/No Srtp determines whether the media communication is encrypted or not. Auto means the client will try to have an encrypted call, but if not possible, it will allow the call to be unencrypted.

Interactive Connectivity Establishment (ICE) dynamically discovers the best possible path for media to travel among call participants.

High bandwidth is directly related to good video quality. However, bandwidth control can prevent an application from trying to receive or send data beyond its capacity, which may result in packet loss, jitter, and low video quality.

The upper/lower bound of the port numbers that are used in the video and audio communication.

You can set these up to control security and firewall issues. You must specify a range of minimum of 10 ports; otherwise, Cisco Jabber Video for iPad will revert to default.

Enabling this option forces relayed media to be relayed via private HD links with guaranteed capacity to ensure quality of video.

This setting relies on ICE being enabled. Private dedicated links are provided by companies such as Media Network Services.

Allows the account to search for other accounts in the Cisco TMS Agent database.

Set up the URI in this format: phonebook@<sip_domain>.com

If you do not specify any value, Cisco Jabber Video for iPad cannot search for contacts.

Allows the account to send availability status to the VCS server.

Set up the URI in this format: presence@<sip_domain>.com

Cisco Jabber Video for iPad uses the availability status from Cisco WebEx Messenger if a server has been identified.

If you do not specify any value, Cisco Jabber Video for iPad cannot publish availability status and will appear offline.

Changes dynamically

This is the address to use

- before ICE negotiation has completed;

- if ICE fails; or

- if the remote side does not understand ICE.

The available options are

- Host —the local network address

- Rflx —the corporate public IP address seen from outside of the organization's network (public IP)

- Relay —the address of the TURN relay server

Cisco recommends that you use Relay if your users will connect from outside your organization's network. ICE negotiation can take a few seconds to complete, and using the TURN relay helps media flow through the firewalls from the beginning of the call.

Upon completion of ICE negotiation, media is redirected if a superior media path has been located.

Uses the value set for Maximum In Bandwidth

Changes dynamically

The value you specify determines the maximum bandwidth allowed for receiving and sending data after users sign in to the application using their VCS accounts.

The settings may be useful for controlling the bandwidth for users who connect from outside their organizations' networks. These users may have slow network connections or the company may want to limit their bandwidth usage.

Uses the value set for Maximum Out Bandwidth

Changes dynamically

Uses the value set for Phone Book Server URI

Changes dynamically

It is sufficient to set the Phone Book Server URI setting.

Uses the value set for Presence Server URI

Changes dynamically

It is sufficient to set the Presence Server URI setting.

Uses the value set for SIP Server Address

Changes dynamically

the server address to which a registration request is sent after users sign in with an external VCS server address

Generally, this information is the same as the external server address the users specify in Cisco Jabber Video for iPad .

Restricts incoming and outgoing video resolution. Cisco Jabber Video for iPad overrides this value.

The restrictions depend on many factors, but as a general rule

- High allows the highest resolution possible up to wide-screen HD (1920x1080 or 1280x720).

- Medium restricts resolutions to wide CIF (512x288) or lower.

- Low restricts resolutions to wide QCIF (256x144) or lower.

the server address to which a registration request is sent

It is the same as the internal server address users specify in Cisco Jabber Video for iPad .

## VCS Setup

Review this topic if you use the registration Allow List or search rules.

In order for the user devices to work with the VCS, the devices must first register with the VCS. The suffix in the registration URIs for Cisco Jabber Video for iPad users is .jabbertablet or .jabber . For example, a user's URI may be in this format with the new suffixes: userName.jabbertablet@DomainName or userName.jabber@DomainName . Because of the URI suffix additions, you may need to make these changes:

- Update the registration Allow List ( VCS configuration > Registration > Allow List ) to allow the new URI suffixes. Example: If you have deployed both VCS and VCSE (VCS Expressway) and used the Allow List to control registration from external locations, add the new suffixes to the Allow List.

- Update or create search rules to include the new URI suffixes. In creating search rules, specify a pattern string that resembles the format .+\.(jabbertablet|jabber).*@%localdomains%.* . Example: If you have multiple VCS clusters (zones) within your organization, you may have to update the rules that control call routing between the VCS and VCSE zones.

## Firewall Requirements

Set up hardware firewalls to allow the ports to carry traffic for the application. Hardware firewalls are network devices that provide protection from unwanted traffic at an organizational level. This table lists the ports required for the deployment of VCS. These ports must be open on all firewalls for the application to function properly.

- When VCS accesses the DNS server, it usually listens on port 53.

- VCS does not try to control from which src port the request is sent.

- No server port is opened unless it is provisioned to open. If VCS receives provisioning to open 5060, it opens 5060 for UDP and TCP and 5061 for TLS/TCP.

- Under normal usage, only one outgoing TCP connection is established towards the SIP proxy. VCS does not try to control which TCP src port it uses.

- VCS uses DNS SRV to discover on which ports the SIP server is listening. VCS accepts well-known ports such as 80 or 443, but under normal usage, the SIP default server ports are 5060 and 5061.

- Under normal usage, only one outgoing TCP connection is established towards the http or https server. VCS does not try to control which TCP src port it uses.

- The application uses DNS to discover the server port; normal usage is 80 or 443.

- VCS gets provisioned with a port range that it can use for media (RTP/UDP).

- For each call, the application opens nine ports within that range and listens for incoming UDP traffic.

- The default port range is 21000 to 21900, and you need to specify a proper range for the application.

- The application tries to discover the best media path by using ICE.

- VCS allocates nine ports on the TURN server for each call.

- The TURN allocations use the media port range used for media.

- The application uses DNS SRV to discover on which ports the TURN server is listening. VCS accepts well-known ports such as 80 or 443, but the ports that are used under normal usage are 3478 or 5349 (TURN standards).

- Due to the STUN and TURN standards, the application cannot use the same ports for each call. Therefore, the port range should have a minimum of 100 ports.

## Main Types of Communication

Review these topics to understand the main types of communication for VCS on Cisco Jabber Video for iPad .

- SIP Communication

- Media Communication

- Media Routing

### SIP Communication

Cisco Jabber Video for iPad communicates with the VCS using Session Initiation Protocol (SIP). With the exception of video and audio, SIP is responsible for all communications, including subscribing, registering, availability querying, and call invitations. SIP messages are sent by TCP, with or without TLS encryption, depending on the provisioned settings.

The default SIP listening ports used in the VCS are

- 5060 (unencrypted)

- 5061 (encrypted)

To change those listening ports, go to VCS Configurations > Protocols > SIP > Configuration .

Jabber itself uses ephemeral TCP ports for these communications. These ports are handed over to Cisco Jabber Video for iPad by the TCP stack and are not configurable.

To enable communication with devices that rely on H.323 and do not support SIP, interworking on the Cisco VCS can be used.

### Media Communication

Media data is transferred through up to nine UDP links (ports). These are the media streams used in Cisco Jabber Video for iPad :

- audio

- primary video

- secondary video (presentation sharing)

Each of these streams requires two links—one link for RTP packets and one link for RTCP packets. The SRTP protocol is used if encryption is enabled.

- Changing Port Range in TMS

- Changing Port Range in VCS

#### Changing Port Range in TMS

The default port range for Cisco Jabber Video for iPad to receive media is 21,000-21,900. You can change the range in the TMS.

The port numbers used are consecutive, but they are chosen randomly within the specified range.

Specify a minimum range of 10 ports; otherwise, the default range is used.

#### Changing Port Range in VCS

The default port range used on the VCS is 50,000-52,399. You can change it.

The port numbers used are consecutive, but they are chosen randomly within the specified range.

Specify a minimum range of 10 ports; otherwise, the default range is used.

### Media Routing

Cisco Jabber Video for iPad supports Interactive Connectivity Establishment (ICE) for better media routing. During a call, ICE is used if enabled for all participants' applications. Review these topics to learn more.

#### Media Routing Without ICE

Media links can be established directly between two devices in non-traversal calls or between Cisco Jabber Video for iPad and the VCS in traversal calls. As a general rule, non-traversal calls are defined as calls between two participants that are on the same network and do not require interworking.

SIP-to-H.323 calls require interworking. Such calls are traversal calls, whether or not the devices are on the same network. For details, see the Cisco TelePresence Video Communication Server Administrator Guide for your VCS release at http:/​/​www.cisco.com/​en/​US/​products/​ps11337/​prod_​maintenance_​guides_​list.html .

#### Media Routing with ICE

ICE dynamically discovers the best possible path for media to travel among call participants. You can improve the routing of media and force it through dedicated links by using the Enable MNS Mode provisioning setting.

#### Turning on ICE

Set up Cisco VCS Expressway to turn on ICE.

Media routing using ICE requires a TURN server. VCS Expressway running version X5.2 or later can function as a TURN server if it has TURN Relay licenses. The TURN server option key is required.

ICE provisioning is not available by default.

The username and password are required for use of TURN Relay licenses.

#### TURN Port for Cisco Jabber Video for iPad

TURN port setup should be controlled through DNS. Cisco Jabber Video for iPad does an SRV lookup for the TURN IP, priority, weight, and port. As TURN runs over UDP, the lookup is for _turn._udp.<domain> . If no SRV record for TURN is found, Cisco Jabber Video for iPad performs an A record lookup (IPv4) or an AAAA lookup (IPv6) but defaults to port 3478.

If the port needs to be provisioned, you can append it to the IP address in the TurnServer field, for example 192.0.2.0:3478 .

## How Does Communication Work at Sign-in?

After signing in to Cisco Jabber Video for iPad , users specify the internal and external VCS server addresses. The application first attempts to subscribe to the internal address. In such situations as the iPad device being connected to non-corporate Wi-Fi, the application then tries to subscribe to the external address.

If the internal VCS server address is a DNS address that translates to more than one IP address, the application attempts to connect to all these IP numbers before trying the external VCS server address. If the DNS server contains SRV records, the application adheres to the priority and weight of the IP addresses; otherwise they are tried in a random order.

Typically, the VCS or the TMS Agent challenges the first subscription message. The application answers this challenge by sending another SUBSCRIBE message with the authentication information.

After the subscription has been authenticated, the TMS Agent sends provisioning information to the application.

The application registers to the VCS according to the provisioning information for SIP Server URI or Public SIP Server URI in the TMS. If this provisioning information is identical to the internal and external VCS server addresses users specify upon signing in (Cisco recommends that they are identical.), the application registers to the same VCS it subscribes to. As long as the application is registered, the VCS knows to forward messages to the application.

After initial registration, the application continues to send registration messages to the VCS according to the Standard registration refresh maximum (seconds) setting in the VCS server. The application sends the messages after 75% of the specified time interval has elapsed.

The Standard registration refresh maximum (seconds) setting is not available in version X6.0 of VCS.

## Specifying Maximum Time for Registration Refresh

When a user temporarily leaves Cisco Jabber Video for iPad to do something else on the device, the application goes into the background and is set to wake up every 10 minutes. You must set the maximum value for a standard SIP registration refresh period to 900 so the application can continue registering to the VCS server.

## How Does Communication Work after Sign-in?

After users sign in to Cisco Jabber Video for iPad , the application continuously performs these tasks.

- Connectivity Checks

- Bandwidth Probing

### Connectivity Checks

Cisco Jabber Video for iPad uses DNS to find TURN servers and ports after users sign in to the application. If specified in the SRV records and supported by the TURN server, the application can use any port, including 80 (HTTP) and 443 (HTTPS).

The application looks for ports in the following order:

- UDP

- TCP (if supported)

- TLS (if supported)

If no ports are detected, the application defaults to ports 3478 and 5349.

Firewall traversal using TCP relay is not supported if you use the VCS as a TURN server at this time.

### Bandwidth Probing

If bandwidth probing is provisioned, Cisco Jabber Video for iPad routes dummy media to the TURN server and back from the server after users sign in to the application. This functionality relies on a TURN server being successfully provisioned.

The results of bandwidth probing are used for the application's dynamic resource adaptation. The results also depend on the provisioned time for probing and in many cases represent a worst case bandwidth scenario in which more bandwidth may be available during an actual call.

## Directory Search

Every time a user types a character in the search field of Cisco Jabber Video for iPad , the application queries the TMS Agent on the VCS, and the TMS Agent answers with matching results. When a search result is selected, the application also queries the VCS for the availability of the contact.

## Call Setup

Call setup is communicated by SIP messages passed through VCS. Review these topics to learn how attributes of a call are determined during call setup.

### Encryption

For a call to be encrypted, both the SIP and the media communication must be encrypted, and all parties must support encryption. Encrypted media communication is sent by the Secure Real-time Transport Protocol (SRTP) with 128-bit Advanced Encryption Standard (AES).

You can specify these encryption policy settings by going to Systems > Provisioning > Directory in the TMS:

- Force TLS/TCP —Determines whether the SIP communication is encrypted (TLS) or not (TCP). The TLS version used by Cisco Jabber Video for iPad is currently 1.0.

- Force/No Srtp —Determines whether the media communication is encrypted or not.

- Auto — Cisco Jabber Video for iPad tries to have an encrypted call. If not possible, the application allows the call to be unencrypted.

### Sent and Received Bandwidth

During call setup, Cisco Jabber Video for iPad signals the maximum bandwidth it wants to receive according to the settings in the server. It is up to the system on the other end of the call to respect this signaling.

Both the maximum bandwidth to be sent during a call and the bandwidth sent at the start of a call are determined during call setup.

During a call, the application can send more or less bandwidth, but the sent bandwidth never goes beyond the maximum bandwidth decided during call setup.

### Video Resolution

The Resolution Preferences setting in provisioning controls the resolution for both incoming and outgoing video. See Understanding Provisioning Options . It is up to the systems used by the other participants in a call to obey restrictions on incoming video.

Many factors contribute to good video quality. Frame rate, high image resolution, scene lighting, and optical quality of the cameras used in a call are all important factors.

- Outgoing Video Resolution

- Incoming Video Resolution

- Presentation Resolution

#### Outgoing Video Resolution

Cisco Jabber Video for iPad uses these criteria when determining the resolution when it sends video:

- The resolution in native format from the camera

- The resolution must be permitted by the receiving end.

- Best: 640x368 requires at least 768 Kbps

- Good: 480x360 requires at least 512 Kbps

Increasing bandwidth improves image quality. You can specify bandwidth permissions using Maximum Out Bandwidth . For more information, see Understanding Provisioning Options .

If a high resolution is not achieved despite sufficient bandwidth as described above, this can usually be attributed to one or both of the following:

- Issues with network connection, including packet loss

- High CPU usage

#### Incoming Video Resolution

You can specify bandwidth permissions for incoming video by using Maximum In Bandwidth in provisioning. For more information, see Understanding Provisioning Options . The bandwidth required for incoming high-resolution video varies with the capabilities and limitations of the device of each call participant.

If a participant device is capable of sending high-resolution video and you specify no restrictions on bandwidth for incoming video, network connection issues, such as packet loss, may still cause incoming video to achieve less-than-desired resolution.

#### Presentation Resolution

The maximum resolution for a shared presentation is dependent on the available bandwidth and the capabilities of the devices of the call participants. For a Jabber-to-Jabber call using unlimited bandwidth, the presentation resolution is 448 p.

You cannot change the resolution for presentations.

### Video and Audio Standards

Cisco Jabber Video for iPad supports these standards for both sending and receiving. The application always uses the best standard that is supported by the devices or applications of other participants in a call.

- Audio—G.722.1 and G.711

- Video—H.264

### ICE Negotiation

After a call has been connected, ICE is negotiated if enabled and supported by both or all call participants. ICE negotiations take a couple of seconds and require nine TURN server licenses, with one license for each media link.

## Actions During a Call

After a call has been set up, a number of actions can be prompted in Cisco Jabber Video for iPad , either as a result of a user action or as an automated response to changing conditions. Review these topics to learn more.

- Multiway

- Mute Media Streams

- Automatic Bandwidth Adaptation

### Multiway

Multiway is the ability for a user to join a call and seamlessly create a multi-participant conference. Cisco Jabber Video for iPad cannot initiate multiway. If multiway is initiated from devices that other participants are using, the call is redirected to a multi-conference system according to the Multiway Participant URI provisioning option.

### Mute Media Streams

If a camera or microphone is muted during a call, Cisco Jabber Video for iPad allocates the bandwidth for the other media links to use. If a user does not have enough bandwidth for two streams, it is possible to mute one stream and improve the quality of the other stream.

To prevent the unused link from being closed, for example by a firewall, the application sends STUN (keep alive) messages every 7 seconds.

### Automatic Bandwidth Adaptation

In situations where Cisco Jabber Video for iPad is sending or receiving bandwidth that exceeds the network capabilities, high packet loss may occur and the user may experience poor call quality. The application uses automatic bandwidth adaptation mechanisms to tackle such bandwidth issues.

Automatic adaptations take time. Cisco recommends that you set up the application to fit the network and system capabilities.

| Product | Required version |
|---|---|
| TMS | 13.1 or later |
| VCS | 6.0 or later |

| Step 1 | Download the template to your local server from http:/​/​www.cisco.com/​cisco/​software/​navigator.html?mdfid=280443139&flowid=29241 . |
|---|---|
| Step 2 | Upload the template or template schema in TMS. The term "template schema" is used in TMSPE while the term "template" is used in TMS Agent Legacy. |
| Step 3 | Add these server addresses, in addition to any other necessary settings, in the template: Public SIP Server Address SIP Server Address Phone Book Server URI |
| Step 4 | Assign the template to the appropriate groups of users. Any template you assign to a group is inherited by all users in the group, all subgroups, and all users in subgroups. You cannot assign a template directly to an individual user. Note Cisco recommends keeping all VCS templates for backwards client compatibility. Multiple templates can exist for a specific device type on each VCS and it is the client subscription request that indicates to the provisioning server which template to use. The provisioning server uses the Model and Version fields from the request to determine the correct template. If the Version string from the request is lower than all installed templates for that model, the provisioning request will fail. If the Version string from the request is higher than any installed templates for that model, a best effort attempt is made to find the closest matching template of equal or lower version. | Note | Cisco recommends keeping all VCS templates for backwards client compatibility. Multiple templates can exist for a specific device type on each VCS and it is the client subscription request that indicates to the provisioning server which template to use. The provisioning server uses the Model and Version fields from the request to determine the correct template. If the Version string from the request is lower than all installed templates for that model, the provisioning request will fail. If the Version string from the request is higher than any installed templates for that model, a best effort attempt is made to find the closest matching template of equal or lower version. |
| Note | Cisco recommends keeping all VCS templates for backwards client compatibility. Multiple templates can exist for a specific device type on each VCS and it is the client subscription request that indicates to the provisioning server which template to use. The provisioning server uses the Model and Version fields from the request to determine the correct template. If the Version string from the request is lower than all installed templates for that model, the provisioning request will fail. If the Version string from the request is higher than any installed templates for that model, a best effort attempt is made to find the closest matching template of equal or lower version. |

| Note | Cisco recommends keeping all VCS templates for backwards client compatibility. Multiple templates can exist for a specific device type on each VCS and it is the client subscription request that indicates to the provisioning server which template to use. The provisioning server uses the Model and Version fields from the request to determine the correct template. If the Version string from the request is lower than all installed templates for that model, the provisioning request will fail. If the Version string from the request is higher than any installed templates for that model, a best effort attempt is made to find the closest matching template of equal or lower version. |
|---|---|

| Field | Default | Description |
|---|---|---|
| Allow User to Save Password | on | This option determines the password policy for the account. on - Allow users to save their password. off - Do not allow users to save their password. |
| Automatic Sign-out | UseClientSetting | This option specifies how Cisco Jabber will automatically sign out. UseClientSetting - Automatic sign out is controlled by the client setting. NeverSignOut - Cisco Jabber will not automatically sign out. 15Minutes - Cisco Jabber will automatically sign out after 15 minutes in the background. 30Minutes - Cisco Jabber will automatically sign out after 30 minutes in the background. 1Hour - Cisco Jabber will automatically sign out after 1 hour in the background. 2Hour - Cisco Jabber will automatically sign out after 2 hours in the background. 4Hour - Cisco Jabber will automatically sign out after 4 hours in the background. 8Hour - Cisco Jabber will automatically sign out after 8 hours in the background. SignOutOnExit - Cisco Jabber will automatically sign out immediately after it goes into the background. |
| Bandwidth Prober Auto Scheduling | Off | This option allows bandwidth probing. Bandwidth probing also requires these settings to be provisioned: TurnAuthPassword TurnAuthUsername TurnServer |
| Bandwidth Prober Time | 0 | After signing in, Jabber Video will probe the TURN relay server for the bandwidth quality between client and TURN server. This setting determines the duration of the probing in seconds. Minimum value: 5 Maximum value: 600 Recommended value: 30 The provisioned time is split into 256 kb/s intervals up to the maximum provisioned bandwidth. |
| Public Bandwidth Prober Auto Scheduling | Uses the value set for Bandwidth Prober Auto Scheduling . | This setting must be On to enable bandwidth probing. Note that bandwidth probing also requires the following settings to be provisioned: TurnAuthPassword TurnAuthUsername TurnServer |
| ClearPath | On | ClearPath is a Cisco TelePresence solution that minimizes the negative effects of packet loss in a non-optimal network. Among the mechanisms used are H.264-specific error recovery techniques, feedback from decoders, and forward error correction (FEC). Both call participants must be using devices that support ClearPath for it to take effect. |
| Default Mediatype Candidate | Host | This is the address to use before ICE negotiation has completed; if ICE fails; or if the remote side does not understand ICE. The available options are Host —the local network address Rflx —the corporate public IP address seen from outside of the organization's network (public IP) Relay —the address of the TURN relay server You can use Relay if you are deploying Cisco Jabber Video for iPad in environments where most other devices do not understand ICE. |
| Encryption Policy | Auto | Determines the encryption policy for the account. This option affects both the SIP communication (Transport TLS or TCP) and the media communication (SRTP or no SRTP). For a call to be encrypted, both the SIP and the media communication must be encrypted, and all parties must support encryption. Encrypted media communication is sent using the Secure Real-time Transport Protocol (SRTP) with a 128-bit Advanced Encryption Standard (AES). The Encryption policy setting is provisioned to the client as configured in Systems > Provisioning > Directory in Cisco TMS. Force TLS/TCP determines whether the SIP communication is encrypted (TLS) or not (TCP). The TLS version 1.0. Force/No Srtp determines whether the media communication is encrypted or not. Auto means the client will try to have an encrypted call, but if not possible, it will allow the call to be unencrypted. |
| ICE | Off | Interactive Connectivity Establishment (ICE) dynamically discovers the best possible path for media to travel among call participants. |
| Maximum In Bandwidth | 512 KB/s | The value you specify determines the maximum bandwidth allowed in the user accounts for receiving and sending data. High bandwidth is directly related to good video quality. However, bandwidth control can prevent an application from trying to receive or send data beyond its capacity, which may result in packet loss, jitter, and low video quality. |
| Maximum Out Bandwidth | 384 KB/s |
| Media Port Range End | 21900 | The upper/lower bound of the port numbers that are used in the video and audio communication. You can set these up to control security and firewall issues. You must specify a range of minimum of 10 ports; otherwise, Cisco Jabber Video for iPad will revert to default. |
| Media Port Range Start | 21000 |
| MNS Mode | Off | Enabling this option forces relayed media to be relayed via private HD links with guaranteed capacity to ensure quality of video. This setting relies on ICE being enabled. Private dedicated links are provided by companies such as Media Network Services. |
| Multiway Participant URI |  | When Multiway is initiated, participants are directed to this Uniform Resource Identifier (URI). |
| Phone Book Server URI |  | Allows the account to search for other accounts in the Cisco TMS Agent database. Set up the URI in this format: phonebook@<sip_domain>.com Important: If you do not specify any value, Cisco Jabber Video for iPad cannot search for contacts. |
| Presence Server URI |  | Allows the account to send availability status to the VCS server. Set up the URI in this format: presence@<sip_domain>.com Note Cisco Jabber Video for iPad uses the availability status from Cisco WebEx Messenger if a server has been identified. If you do not specify any value, Cisco Jabber Video for iPad cannot publish availability status and will appear offline. | Note | Cisco Jabber Video for iPad uses the availability status from Cisco WebEx Messenger if a server has been identified. If you do not specify any value, Cisco Jabber Video for iPad cannot publish availability status and will appear offline. |
| Note | Cisco Jabber Video for iPad uses the availability status from Cisco WebEx Messenger if a server has been identified. If you do not specify any value, Cisco Jabber Video for iPad cannot publish availability status and will appear offline. |
| Public Default Mediatype Candidate | Uses the value set for Default Mediatype Candidate Changes dynamically | This is the address to use before ICE negotiation has completed; if ICE fails; or if the remote side does not understand ICE. The available options are Host —the local network address Rflx —the corporate public IP address seen from outside of the organization's network (public IP) Relay —the address of the TURN relay server Cisco recommends that you use Relay if your users will connect from outside your organization's network. ICE negotiation can take a few seconds to complete, and using the TURN relay helps media flow through the firewalls from the beginning of the call. Upon completion of ICE negotiation, media is redirected if a superior media path has been located. |
| Public Maximum In Bandwidth | Uses the value set for Maximum In Bandwidth Changes dynamically | The value you specify determines the maximum bandwidth allowed for receiving and sending data after users sign in to the application using their VCS accounts. The settings may be useful for controlling the bandwidth for users who connect from outside their organizations' networks. These users may have slow network connections or the company may want to limit their bandwidth usage. |
| Public Maximum Out Bandwidth | Uses the value set for Maximum Out Bandwidth Changes dynamically |
| Public Phone Book Server URI | Uses the value set for Phone Book Server URI Changes dynamically | It is sufficient to set the Phone Book Server URI setting. |
| Public Presence Server URI | Uses the value set for Presence Server URI Changes dynamically | It is sufficient to set the Presence Server URI setting. |
| Public SIP Server Address | Uses the value set for SIP Server Address Changes dynamically | the server address to which a registration request is sent after users sign in with an external VCS server address Generally, this information is the same as the external server address the users specify in Cisco Jabber Video for iPad . |
| Resolution Preferences | High | Restricts incoming and outgoing video resolution. Cisco Jabber Video for iPad overrides this value. The restrictions depend on many factors, but as a general rule High allows the highest resolution possible up to wide-screen HD (1920x1080 or 1280x720). Medium restricts resolutions to wide CIF (512x288) or lower. Low restricts resolutions to wide QCIF (256x144) or lower. |
| SIP Server Address | the VCS server that Cisco Jabber Video for iPad is subscribed to | the server address to which a registration request is sent It is the same as the internal server address users specify in Cisco Jabber Video for iPad . |
| SIP Authentication Username |  | SIP Authentication Username. The endpoint uses the AuthUsername and AuthPassword values to authenticate with the VCS server. |
| SIP Authentication Password |  | SIP Authentication Password. The endpoint uses the AuthUsername and AuthPassword values to authenticate with the VCS server. |
| TurnAuthPassword |  | TURN server settings that are required for enabling ICE. See Turning on ICE for more information. |
| TurnAuthUsername |  |
| TurnServer |  |

| Note | Cisco Jabber Video for iPad uses the availability status from Cisco WebEx Messenger if a server has been identified. If you do not specify any value, Cisco Jabber Video for iPad cannot publish availability status and will appear offline. |
|---|---|

| Protocol | Port and description |
|---|---|
| DNS | When VCS accesses the DNS server, it usually listens on port 53. VCS does not try to control from which src port the request is sent. |
| SIP | No server port is opened unless it is provisioned to open. If VCS receives provisioning to open 5060, it opens 5060 for UDP and TCP and 5061 for TLS/TCP. Under normal usage, only one outgoing TCP connection is established towards the SIP proxy. VCS does not try to control which TCP src port it uses. VCS uses DNS SRV to discover on which ports the SIP server is listening. VCS accepts well-known ports such as 80 or 443, but under normal usage, the SIP default server ports are 5060 and 5061. |
| HTTP | Under normal usage, only one outgoing TCP connection is established towards the http or https server. VCS does not try to control which TCP src port it uses. The application uses DNS to discover the server port; normal usage is 80 or 443. |
| media | VCS gets provisioned with a port range that it can use for media (RTP/UDP). For each call, the application opens nine ports within that range and listens for incoming UDP traffic. The default port range is 21000 to 21900, and you need to specify a proper range for the application. |
| TURN | The application tries to discover the best media path by using ICE. VCS allocates nine ports on the TURN server for each call. The TURN allocations use the media port range used for media. The application uses DNS SRV to discover on which ports the TURN server is listening. VCS accepts well-known ports such as 80 or 443, but the ports that are used under normal usage are 3478 or 5349 (TURN standards). Due to the STUN and TURN standards, the application cannot use the same ports for each call. Therefore, the port range should have a minimum of 100 ports. |

| Note | Jabber itself uses ephemeral TCP ports for these communications. These ports are handed over to Cisco Jabber Video for iPad by the TCP stack and are not configurable. To enable communication with devices that rely on H.323 and do not support SIP, interworking on the Cisco VCS can be used. |
|---|---|

| Note | The port numbers used are consecutive, but they are chosen randomly within the specified range. |
|---|---|

| Step 1 | Go to Systems > Provisioning > Directory |
|---|---|
| Step 2 | Specify your range using Media Port Range Start and Media Port Range End . Specify a minimum range of 10 ports; otherwise, the default range is used. |

| Note | The port numbers used are consecutive, but they are chosen randomly within the specified range. |
|---|---|

| Step 1 | Go to VCS Configuration > Local zone > Traversal subzone . |
|---|---|
| Step 2 | Specify your range using Traversal media port start and Traversal media port end . Specify a minimum range of 10 ports; otherwise, the default range is used. |

| Note | ICE provisioning is not available by default. |
|---|---|

| Step 1 | In VCS Expressway, go to VCS configuration > Expressway > TURN and specify these settings: Setting Change to… TURN services On Port 3478 Media port range start 60000 Media port range end 61399 | Setting | Change to… | TURN services | On | Port | 3478 | Media port range start | 60000 | Media port range end | 61399 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Setting | Change to… |
| TURN services | On |
| Port | 3478 |
| Media port range start | 60000 |
| Media port range end | 61399 |
| Step 2 | Go to VCS configuration > Authentication > Devices > Configuration and then specify LocalDatabase for Database type . |
| Step 3 | Go to VCS configuration > Authentication > Devices > Local database and create a username and password. The username and password are required for use of TURN Relay licenses. |
| Step 4 | Go to Systems > Provisioning > Directory > Configurations and set the following fields with these values: Setting Change to... Enable ICE On TurnAuthPassword Password created when setting up the Cisco VCS Expressway TurnAuthUsername Username created when setting up the Cisco VCS Expressway TurnServer The address of the server media is relayed through in an ICE call. Typically the address of the Cisco VCS Expressway. | Setting | Change to... | Enable ICE | On | TurnAuthPassword | Password created when setting up the Cisco VCS Expressway | TurnAuthUsername | Username created when setting up the Cisco VCS Expressway | TurnServer | The address of the server media is relayed through in an ICE call. Typically the address of the Cisco VCS Expressway. |
| Setting | Change to... |
| Enable ICE | On |
| TurnAuthPassword | Password created when setting up the Cisco VCS Expressway |
| TurnAuthUsername | Username created when setting up the Cisco VCS Expressway |
| TurnServer | The address of the server media is relayed through in an ICE call. Typically the address of the Cisco VCS Expressway. |

| Setting | Change to… |
|---|---|
| TURN services | On |
| Port | 3478 |
| Media port range start | 60000 |
| Media port range end | 61399 |

| Setting | Change to... |
|---|---|
| Enable ICE | On |
| TurnAuthPassword | Password created when setting up the Cisco VCS Expressway |
| TurnAuthUsername | Username created when setting up the Cisco VCS Expressway |
| TurnServer | The address of the server media is relayed through in an ICE call. Typically the address of the Cisco VCS Expressway. |

| Note | The Standard registration refresh maximum (seconds) setting is not available in version X6.0 of VCS. |
|---|---|

| Step 1 | In the VCS server, go to VCS configuration > Protocols > SIP > Configuration . |
|---|---|
| Step 2 | In the "Registration controls" section, enter 900 for Standard registration refresh maximum (seconds) . |
| Step 3 | Select Save . |

| Note | Firewall traversal using TCP relay is not supported if you use the VCS as a TURN server at this time. |
|---|---|

| Note | If a participant device is capable of sending high-resolution video and you specify no restrictions on bandwidth for incoming video, network connection issues, such as packet loss, may still cause incoming video to achieve less-than-desired resolution. |
|---|---|

| Note | Automatic adaptations take time. Cisco recommends that you set up the application to fit the network and system capabilities. |
|---|---|