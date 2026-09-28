---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-oodo-ping-group-html-27aae3c343
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_oodo-ping-group.html
retrieved_at: 2026-08-16T15:45:12.969890+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP Trunk Monitoring

## Chapter: SIP Trunk Monitoring

# SIP Trunk Monitoring

## Overview

This feature groups the monitoring of SIP dial-peer, endpoints and servers by consolidating
                           			dial-peers with the same SIP Out-of-Dialog OPTIONS ping setup.

The SIP Out-Of-Dialog OPTIONS Ping Group feature is an existing mechanism that is used by Cisco Unified Border Element (CUBE) to monitor the status of a single SIP dial-peer destination (keepalive). A generic heartbeat mechanism allows you to monitor
                           the status of SIP servers or endpoints and provide the option of marking a dial peer as inactive (busyout) upon total heartbeat
                           failure.

You can also consolidate the sending of OPTIONS ping packets by grouping dial peers with the
                           			same destination. You must create a profile to send one set of OPTIONS ping for a group
                           			of dial-peers. If that ping fails, then all of the associated dial-peers are busied out
                           			(inactive) by CUBE .

Configuring the same Options profile on two or more dial-peers with different bind interfaces
                                       				configured is not supported. This leads to a scenario wherein the OPTIONS SIP
                                       				message is not sent from all bind interfaces except the first configured one. But
                                       				the dial-peer is always marked as ACTIVE. Similarly, it is also not supported in
                                       				multi VRF setup.

You can use the shutdown command to suspend monitoring of all dial peers associated with a keepalive profile.

The command voice-class sip options-keepalive profile tag is used to monitor a group of SIP servers or endpoints and the existing voice-class sip options-keepalive command is used to monitor a single SIP endpoint or server.

You can configure a server group to be a part of a OPTIONS ping group. A SIP dial peer is
                           			updated to BUSY state only if all targets of its server group does not response to the
                           			OPTIONS ping. Members of a server group are tested in turn, not in parallel. That is, if
                           			the first server group member becomes unavailable, then the second member is tested, and
                           			so on. Only when all of the group members are exhausted, is the dial-peer busied
                           			out.

### Technical Assistance

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving
                                          technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product
                                          Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.

http://www.cisco.com/support

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP Out-of-dialog OPTIONS Ping Group

Baseline Functionality

This feature groups the monitoring of SIP dial peers endpoints and servers by consolidating SIP Out-Of-Dialog Options of
                                          dial peers with the similar OPTIONS ping setup.

### OPTIONS Ping for DNS SRV Hosts

From Cisco IOS XE Cupertino
                                    17.9.1a , you can monitor all the SRV hosts that are part of the DNS destination using the
                              OPTIONS Keepalive mechanism. It is therefore possible to load balance calls across all
                              active destinations.

This feature may be used by configuring a dial-peer target with a fully qualified domain
                              name (FQDN) that resolves to a set of DNS SRV records.

A Domain Name System Service Record  (DNS SRV) record comprises of multiple resources,
                              each with its own weight, priority and host name. CUBE uses DNS again to resolve the IP
                              address for each of these hostnames.CUBE then triggers an Out-of-Dialog OPTIONS ping to
                              each of these addresses to monitor the status of the hosts.

Once the DNS A query is successful, CUBE triggers an Out-of-Dialog OPTIONS Ping. The Out-of-Dialog OPTIONS Ping mechanism
                              is used by CUBE to monitor the status of the single SIP dial-peer destination (keepalive).

If the DNS lookup returns multiple addresses, then Out-of-Dialog keepalive sessions are
                              established with each of the hosts. For the same destination hostname and the
                              same voice-class sip options-keepalive profile tag , only a single Out-of-Dialog OPTIONS SRV entry will be added in the
                              keepalive session table. This SRV entry in the keepalive session table can maintain the
                              session details for each of the hosts.

CUBE compares the least value of Time to Live (TTL) recorded for both SRV resolution and
                              Type A/AAAA resolution. CUBE maintains the least value that is obtained, against the DNS
                              SRV entry in the Out-of-Dialog session table. CUBE starts a periodic timer based on the
                              least TTL value. When the TTL timer expires, the Out-of-Dialog session status is removed
                              for all the existing host entries. Thereafter, CUBE performs a new SRV or Type-A or AAAA
                              lookup to update the DNS SRV entry list.

A generic heartbeat mechanism allows you to monitor the status of SIP servers or
                              endpoints. It provides the option of marking a dial-peer as active , inactive ( busyout ) for a total
                              heartbeat failure, and partially active ( partial ). A dial-peer is
                              marked as partially active if at least one of the destinations is active out of a group,
                              and the rest are inactive (busyout). A dial-peer is marked as busyout, only if all the
                              destinations in the dial-peer have a heartbeat failure and fail to respond.

Once OPTIONS Ping is successful, this destination is considered for the routing of call
                              handling. CUBE monitors all the destinations irrespective of the response (503, 200 OK,
                              and so on) that it receives. Based on the response, CUBE identifies the destination that
                              it can communicate with. If CUBE receives a 503 response or no response for the INVITE,
                              CUBE then marks that destination as busyout and attempts call on the next destination
                              that is marked as active. The call is rejected if all possible destinations are busied
                              out.

If Outbound Proxy is configured on dial-peer or a tenant that is associated
                                                with the dial-peer, CUBE maintains keepalive session with the Outbound Proxy
                                                address.

You need to configure the same transport type for the dial-peers with same
                                                SRV destination.

You must configure voice-class sip options-keepalive profile <tag> under the specific dial-peer to support the DNS SRV lookup using the OPTIONS keepalive mechanism. If you configure the voice-class sip options-keepalive command under the dial-peer, Load Balancing using DNS SRV is not supported.

We recommend that you configure the same voice-class sip options-keepalive profile <tag> under all dial-peers that have the same DNS session target. This helps to reduce the OPTIONS Ping traffic.

To display the status of the destination when options-keepalive is configured under dial-peer, use the CLI command show dial-peer voip keepalive status <dp-tag> | tenant <tenant-id> | <cr> . The options keepalive status is maintained by CUBE for individual session targets and server groups in this command. The
                              keepalive status is displayed for IPv4, IPv6, and DNS format destinations.

The CLI command show dial-peer voice summary is enhanced to display the overall keepalive status for the DNS SRV at the dial-peer level.

To display the status of session target DNS with the list of servers resolved against the DNS SRV records, use the CLI command show voice class sip-options-keepalive <profile-tag> .

### Load Balancing for DNS SRV Hosts

The usage of DNS SRV as the target for CUBE helps in load balancing of the outbound SIP
                              call traffic across the trunk. Based on the priority, weight, and status of the DNS SRV
                              records, the multiple hosts associated with DNS SRV are used. CUBE distributes calls
                              across the SRVs based on the priority and status of the DNS SRV records.

During call routing, CUBE reads through the DNS SRV records that it has collected. Based
                              on the information, CUBE identifies the trunk dial-peer destinations that are still
                              available. Based on this, CUBE can distribute the traffic of outbound SIP calls in a
                              more efficient way.

If configured, CUBE uses the Out-of-Dialog OPTIONS Ping mechanism to monitor the status
                              of the hosts defined by the dial-peer destination SRV record. For more information on
                              OPTIONS Ping for DNS SRV hosts, see OPTIONS Ping for DNS SRV Hosts .

## Configure SIP Out-of-Dialog OPTIONS Ping Group

### Before you begin

Configure SIP
                              		  profiles and server groups.

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-options-keepalive keepalive-group-profile-id

- description text

- transport {tcp [tls] | udp | system}

- sip-profiles profile-number

- down-interval down-interval

- up-interval up-interval

- retry retry-interval

- exit

- dial-peer voice dial-peer-id voip

- session protocol
                                    				  sipv2

- voice-class sip
                                    				  options-keepalive profile keepalive-group-profile-id

- session
                                    				  server-group server-group-id

- end

- show voice class
                                    				  sip-options-keepalive keepalive-group-profile-id

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enters
                                          				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

voice class sip-options-keepalive keepalive-group-profile-id

### Example:

```
Device(config)# voice class sip-options-keepalive 171
```

Configures a keepalive profile and enters voice class configuration mode.

You can use the shutdown command to suspend keepalive activity for all dial peers associated with the keepalive profile.

Step 4

description text

### Example:

```
Device(config-class)# description Target Boston
```

Configures
                                          				a textual description for the keepalive heartbeat connection.

Step 5

transport {tcp [tls] | udp | system}

### Example:

```
Device(config-class)# transport tcp
```

Defines the transport protocol that is used for the keepalive heartbeat connection.

The default value is system.

Step 6

sip-profiles profile-number

### Example:

```
Device(config-class)# sip-profiles 100
```

Specifies the
                                          				SIP profile that is to be used to send this message.

To
                                                					 configure a SIP profile, refer to "Configuring SIP Parameter Modification" .

Step 7

down-interval down-interval

### Example:

```
Device(config-class)# down-interval 35
```

The default value is 30.

Step 8

up-interval up-interval

### Example:

```
Device(config-class)# up-interval 65
```

The default value is 60.

Step 9

retry retry-interval

### Example:

```
Device(config-class)# retry 30
```

The default value is 5.

If a successful response is received for an OPTIONS ping, the retry counter is set to zero.

Step 10

exit

### Example:

```
Device(config-class)# exit
```

Exits voice
                                          				class configuration mode and enters global configuration mode.

Step 11

dial-peer voice dial-peer-id voip

### Example:

```
Device(config)# dial-peer voice 123 voip
```

Defines a
                                          				local dial peer and enters dial peer configuration mode.

Step 12

session protocol
                                             				  sipv2

### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Specifies
                                          				SIP version 2 as the session protocol for calls between local and remote
                                          				routers using the packet network.

Step 13

voice-class sip
                                             				  options-keepalive profile keepalive-group-profile-id

### Example:

```
Device(config-dial-peer)# voice-class sip options-keepalive profile 171
```

Associates the dial peer with the specified keepalive group profile. The dial peer is monitored by CUBE according to the parameters defined by this profile.

Step 14

session
                                             				  server-group server-group-id

### Example:

```
Device(config-dial-peer)# session server-group 151
```

Associates
                                          				the dial peer with the specified keepalive group profile. The dial peer is
                                          				monitored by the device according to the parameters defined by this profile.

Step 15

end

### Example:

```
Device(config-dial-peer)# end
```

Exits dial
                                          				peer configuration mode and enters privileged EXEC mode.

Step 16

show voice class
                                             				  sip-options-keepalive keepalive-group-profile-id

### Example:

```
Device# show voice class sip-options-keepalive 171
```

Displays
                                          				information about voice class server group.

### Configuration Examples For SIP Out-of-Dialog OPTIONS Ping Group

#### Example: SIP
                                 		  Out-of-Dialog OPTIONS Ping for Group of SIP Endpoints

```
!Configuring the SIP profile
Device(config)# voice class sip-profiles 100 Device(config-class)# request OPTIONS sip-header SIP-Req-URI modify "; SIP/2.0" ";user=phone SIP/2.0" !Configuring the SIP Keepalive Group
Device(config)# voice class sip-options-keepalive 171 Device(config-class)# transport tcp Device(config-class)# sip-profile 100 Device(config-class)# down-interval 30 Device(config-class)# up-interval 60 Device(config-class)# retry 5 Device(config-class)# description Target New York Device(config-class)# exit !Configuring an outbound SIP Dial Peer  
Device(config)# dial-peer voice 123 voip Device(config-dial-peer)# session protocol sipv2 !Associating the Dial Peer with a keepalive profile group
Device(config-dial-peer)# session target dns:example.com
Device(config-dial-peer)# voice-class sip options-keepalive profile 171 Device(config-dial-peer)# end !Verifying the Keepalive group configurations
Device# show voice class sip-options-keepalive 171 Voice class sip-options-keepalive: 171           AdminStat: Up
 Description: Target New York
 Transport: system               Sip Profiles: 100
 Interval(seconds) Up: 60                Down: 30
 Retry: 5

  Peer Tag      Server Group    OOD SessID      OOD Stat        IfIndex
  --------      ------------    ----------      --------        -------
  123                                                           100
```

#### Example: SIP Out-of-dialog OPTIONS Ping for Group of SIP Servers

```
!Configuring the Server Group
Device(config)# voice class server-group 151 Device(config-class)# ipv4 10.1.1.1 preference 1 Device(config-class)# ipv4 10.1.1.2 preference 2 Device(config-class)# ipv4 10.1.1.3 preference 3 Device(config-class)# hunt-scheme round-robin Device(config-class)# description It has 3 entries Device(config-class)# exit !Configuring an E164 pattern map class
Device(config)# voice class e164-pattern-map 3000 Device(config-class)# e164 300 !Configuring an outbound SIP dial peer.   
Device(config)# dial-peer voice 181 voip !Associate a destination pattern map
Device(config-dial-peer)# destination e164-pattern-map 3000 Device(config-dial-peer)# session protocol sipv2 !Associate a server group with the dial peer
Device(config-dial-peer)# session server-group 151 !Associate the dial peer with a keepalive profile group
Device(config-dial-peer)# voice-class sip options-keepalive profile 171 Device(config-dial-peer)# end !Verifying the Keepalive group configurations
Device# show voice class sip-options-keepalive 171 Voice class sip-options-keepalive: 171           AdminStat: Up
 Description: Target New York
 Transport: system               Sip Profiles: 100
 Interval(seconds) Up: 60                Down: 30
 Retry: 5

  Peer Tag      Server Group    OOD SessID      OOD Stat        IfIndex
  --------      ------------    ----------      --------        -------
  123                                                           100
  181           151                             Busy            106

  Server Group: 151              OOD Stat: Busy
   OOD SessID   OOD Stat
   ----------   --------
   1            Busy
   2            Busy
   3            Busy

 OOD SessID: 1                   OOD Stat: Busy
  Target: ipv4:10.1.1.1
  Transport: system              Sip Profiles: 100

 OOD SessID: 2                   OOD Stat: Busy
  Target: ipv4:10.1.1.2
  Transport: system              Sip Profiles: 100

 OOD SessID: 3                   OOD Stat: Busy
  Target: ipv4:10.5.0.1
  Transport: system              Sip Profiles: 100

------------------------------------------------------
```

## Configure OPTIONS Ping Between CUCM and CUBE

This section describes how to enable Options Ping between Cisco Unified Communications Manager (CUCM) and Cisco Unified Border
                              Element (CUBE).

The following figure describes how a CUCM extends a call out of a SIP Trunk:

The following figure shows the TCP three-way handshake in Wireshark:

Perform the following steps to configure OPTIONS ping between CUBE and CUCM:

### SUMMARY STEPS

- Enable SIP Options Ping in the SIP Profile Configuration:

- Add the SIP profile to the SIP trunk and click Save :

- Enable SIP Options Ping on the far end of the SIP Trunk. In this case, 192.X.X.57 (ISR 4351).

### DETAILED STEPS

Step 1

Enable SIP Options Ping in the SIP Profile Configuration:

Navigate to Cisco Unified CM Administration >> Device >> Device Settings >> SIP Profile as shown in the following figure:

Click find and decide if you want to create a new SIP Profile , edit a SIP Profile that exists or make a copy of a SIP Profile. For this example, create a copy of the Standard SIP Profile as shown in the following figures:

Rename the new SIP Profile and enable the OPTIONS Ping option as shown in the following figure:

Step 2

Add the SIP profile to the SIP trunk and click Save :

You must have previously configured this trunk. See System Configuration Guide.

Set Status , Status Reason , and Duration to N/A.

Navigate to Device >> Trunk .

Choose the correct SIP profile and click Save .

You must reset the trunk after saving for the changes to take effect.

The reset disconnects active calls and does not allow any incoming calls for a short time.

Monitor the status of the SIP Trunk in Cisco Unified Communications Manager.

Step 3

Enable SIP Options Ping on the far end of the SIP Trunk. In this case, 192.X.X.57 (ISR 4351).

Navigate to the ISR CUBE or Gateway and confirm what dial-peer you want to add the Options Ping to as shown in the following
                                             figure:

```
ISR4351#show running-config | s voice 100
dial-peer voice 100 voip
description CUCM Dial-Peer
session protocol sipv2
session target ipv4:192.x.x.26
dtmf-relay rtp-nte
codec g711ulaw
no vad
```

Add Options Ping with the command: voice-class sip options-keepalive using a profile.

```
dial-peer voice 100 voip
description CUCM Dial-Peer
session protocol sipv2
session target ipv4:192.x.x.26
voice-class sip options-keepalive profile 1
dtmf-relay rtp-nte
codec g711ulaw
no vad
```

### What to do next

Verify

Confirm that Options messages are exchanged correctly in this section.

To understand how to run a packet capture on CUCM eth0 port, follow the instructions in this link: Packet Capture on CUCM Appliance Model .

The TCP three-way handshake is only done once, when you restart the trunk. Afterwards, you only have OPTIONS messages that
                                                are sent from CUCM to ISR where you expect a 200 OK as a response. These messages are exchanged every 60 seconds by default.

Options messages are only sent from 192.X.X.26 (CUCM) to 192.X.X.57 (ISR) because only CUCM is configured to monitor the trunk
                                                status:

When you call, CUCM already knows that the trunk is in an operational status and sends an invite:

If you have completed Step 3 configuration on CUBE, you see that Options messages sent both ways:

Troubleshoot

To troubleshoot Options Ping in CUCM, you need:

Start with Packet Captures from CUCM Eth0 port. For more details, Packet Capture on CUCM Appliance Model .

Check detailed Cisco Call Manager traces. Download them with RTMT. See the steps here: How to Collect Traces for CUCM 9.x or Later

Verify the SIPTrunkOOS Reason codes in this link: System Error Message .

Local=1 (request timeout)

Local=2 (local SIP stack is not able to create a socket connection with the remote peer)

Local=3 (DNS query failed)

To troubleshoot Options Ping in CUBE, you need the following:

debug ccsip messages

debug ccsip non-call

debug voip ccapi inout

Packet captures from an interface that point toward CUCM.

## Additional
                        	 References

### Related
                              		  Documents

| Note | Configuring the same Options profile on two or more dial-peers with different bind interfaces
                                       				configured is not supported. This leads to a scenario wherein the OPTIONS SIP
                                       				message is not sent from all bind interfaces except the first configured one. But
                                       				the dial-peer is always marked as ACTIVE. Similarly, it is also not supported in
                                       				multi VRF setup. |
|---|---|

| Description | Link |
|---|---|
| The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving
                                          technical issues with Cisco products and technologies. To receive security and technical information about your products, you can subscribe to various services, such as the Product
                                          Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds. Access to most tools on the Cisco Support website requires a Cisco.com user ID and password. | http://www.cisco.com/support |

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP Out-of-dialog OPTIONS Ping Group | Baseline Functionality | This feature groups the monitoring of SIP dial peers endpoints and servers by consolidating SIP Out-Of-Dialog Options of
                                          dial peers with the similar OPTIONS ping setup. |

| Note | If Outbound Proxy is configured on dial-peer or a tenant that is associated
                                                with the dial-peer, CUBE maintains keepalive session with the Outbound Proxy
                                                address. You need to configure the same transport type for the dial-peers with same
                                                SRV destination. |
|---|---|

| Note | We recommend that you configure the same voice-class sip options-keepalive profile <tag> under all dial-peers that have the same DNS session target. This helps to reduce the OPTIONS Ping traffic. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enters
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class sip-options-keepalive keepalive-group-profile-id Example: Device(config)# voice class sip-options-keepalive 171 | Configures a keepalive profile and enters voice class configuration mode. You can use the shutdown command to suspend keepalive activity for all dial peers associated with the keepalive profile. |
| Step 4 | description text Example: Device(config-class)# description Target Boston | Configures
                                          				a textual description for the keepalive heartbeat connection. |
| Step 5 | transport {tcp [tls] \| udp \| system} Example: Device(config-class)# transport tcp | Defines the transport protocol that is used for the keepalive heartbeat connection. The default value is system. |
| Step 6 | sip-profiles profile-number Example: Device(config-class)# sip-profiles 100 | Specifies the
                                          				SIP profile that is to be used to send this message. To
                                                					 configure a SIP profile, refer to "Configuring SIP Parameter Modification" . |
| Step 7 | down-interval down-interval Example: Device(config-class)# down-interval 35 | Configures the time (in seconds) at which an OPTIONS ping is sent to the dial-peer endpoint when the heartbeat connection
                                       to the endpoint is in Down status. The default value is 30. |
| Step 8 | up-interval up-interval Example: Device(config-class)# up-interval 65 | Configures the time (in seconds) at which an OPTIONS ping is sent to the dial-peer endpoint when the heartbeat connection
                                       to the endpoint is in Up status. The default value is 60. |
| Step 9 | retry retry-interval Example: Device(config-class)# retry 30 | Configures the maximum number of OPTIONS ping retries that are permitted for a dial-peer destination. After receiving failed
                                       responses for the configured number of OPTIONS pings, the heartbeat connection status should be switched from Up to Down. The default value is 5. If a successful response is received for an OPTIONS ping, the retry counter is set to zero. |
| Step 10 | exit Example: Device(config-class)# exit | Exits voice
                                          				class configuration mode and enters global configuration mode. |
| Step 11 | dial-peer voice dial-peer-id voip Example: Device(config)# dial-peer voice 123 voip | Defines a
                                          				local dial peer and enters dial peer configuration mode. |
| Step 12 | session protocol
                                             				  sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Specifies
                                          				SIP version 2 as the session protocol for calls between local and remote
                                          				routers using the packet network. |
| Step 13 | voice-class sip
                                             				  options-keepalive profile keepalive-group-profile-id Example: Device(config-dial-peer)# voice-class sip options-keepalive profile 171 | Associates the dial peer with the specified keepalive group profile. The dial peer is monitored by CUBE according to the parameters defined by this profile. |
| Step 14 | session
                                             				  server-group server-group-id Example: Device(config-dial-peer)# session server-group 151 | Associates
                                          				the dial peer with the specified keepalive group profile. The dial peer is
                                          				monitored by the device according to the parameters defined by this profile. |
| Step 15 | end Example: Device(config-dial-peer)# end | Exits dial
                                          				peer configuration mode and enters privileged EXEC mode. |
| Step 16 | show voice class
                                             				  sip-options-keepalive keepalive-group-profile-id Example: Device# show voice class sip-options-keepalive 171 | Displays
                                          				information about voice class server group. |

| Step 1 | Enable SIP Options Ping in the SIP Profile Configuration: Navigate to Cisco Unified CM Administration >> Device >> Device Settings >> SIP Profile as shown in the following figure: Click find and decide if you want to create a new SIP Profile , edit a SIP Profile that exists or make a copy of a SIP Profile. For this example, create a copy of the Standard SIP Profile as shown in the following figures: Rename the new SIP Profile and enable the OPTIONS Ping option as shown in the following figure: |
|---|---|
| Step 2 | Add the SIP profile to the SIP trunk and click Save : Note You must have previously configured this trunk. See System Configuration Guide. Set Status , Status Reason , and Duration to N/A. Navigate to Device >> Trunk . Choose the correct SIP profile and click Save . Note You must reset the trunk after saving for the changes to take effect. The reset disconnects active calls and does not allow any incoming calls for a short time. Monitor the status of the SIP Trunk in Cisco Unified Communications Manager. | Note | You must have previously configured this trunk. See System Configuration Guide. Set Status , Status Reason , and Duration to N/A. | Note | You must reset the trunk after saving for the changes to take effect. The reset disconnects active calls and does not allow any incoming calls for a short time. |
| Note | You must have previously configured this trunk. See System Configuration Guide. Set Status , Status Reason , and Duration to N/A. |
| Note | You must reset the trunk after saving for the changes to take effect. The reset disconnects active calls and does not allow any incoming calls for a short time. |
| Step 3 | Enable SIP Options Ping on the far end of the SIP Trunk. In this case, 192.X.X.57 (ISR 4351). Navigate to the ISR CUBE or Gateway and confirm what dial-peer you want to add the Options Ping to as shown in the following
                                             figure: ISR4351#show running-config \| s voice 100
dial-peer voice 100 voip
description CUCM Dial-Peer
session protocol sipv2
session target ipv4:192.x.x.26
dtmf-relay rtp-nte
codec g711ulaw
no vad Add Options Ping with the command: voice-class sip options-keepalive using a profile. dial-peer voice 100 voip
description CUCM Dial-Peer
session protocol sipv2
session target ipv4:192.x.x.26
voice-class sip options-keepalive profile 1
dtmf-relay rtp-nte
codec g711ulaw
no vad |

| Note | You must have previously configured this trunk. See System Configuration Guide. Set Status , Status Reason , and Duration to N/A. |
|---|---|

| Note | You must reset the trunk after saving for the changes to take effect. The reset disconnects active calls and does not allow any incoming calls for a short time. |
|---|---|

| Note | To understand how to run a packet capture on CUCM eth0 port, follow the instructions in this link: Packet Capture on CUCM Appliance Model . The TCP three-way handshake is only done once, when you restart the trunk. Afterwards, you only have OPTIONS messages that
                                                are sent from CUCM to ISR where you expect a 200 OK as a response. These messages are exchanged every 60 seconds by default. Options messages are only sent from 192.X.X.26 (CUCM) to 192.X.X.57 (ISR) because only CUCM is configured to monitor the trunk
                                                status: When you call, CUCM already knows that the trunk is in an operational status and sends an invite: If you have completed Step 3 configuration on CUBE, you see that Options messages sent both ways: |
|---|---|

| Related Topic | Document Title |
|---|---|
| Voice
                                       					 commands | Cisco IOS Voice Command
                                             						  Reference |
| Cisco
                                       					 IOS Commands | Cisco IOS Command List, All Releases |
| SIP
                                       					 Configuration Guide |  |
| Configuring SIP profiles |  |
| Configuring server groups |  |