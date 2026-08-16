---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-multi-tenants-html-43326f099f
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-multi-tenants.html
retrieved_at: 2026-08-16T15:53:12.886056+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configure Multiple Trunks Using Tenants

## Chapter: Configure Multiple Trunks Using Tenants

# Configure Multiple Trunks Using Tenants

## Overview

The CUBE Tenant feature allows you to configure SIP trunks individually using parameters that were previously only available globally,
                           or with individual dial-peers. Tenants act as a configuration template for dial-peers, which allow you to customize the global
                           configuration to suit the requirements for each trunk. Dial-peers associated with a tenant automatically receive all of its
                           configuration, making trunk configuration simple and consistent. If necessary, specific configurations may be overridden at
                           the dial-peer level, allowing maximum flexibility.

When bound to an interface configured with a VRF, the tenant feature may also be used to configure trunks for multiple customers,
                           each with their own characteristics on the same platform.

The voice class tenant <tag> command allows sip-specific attributes to be configured for each trunk. The command voice class tenant <tag> can then be used to apply the tenant configuration to individual dial-peers. Refer to  " Table 1 " for information on the complete list of configurations present under the voice class tenant <tag> .

If tenants are configured under dial-peer, then configurations are applied in the following order of preference.

Dial-peer configuration

Tenant configuration

Global configuration

That is, if the value of the attribute under dial-peer configuration is system, then the value is taken from the tenant configuration.
                           And, if the value under the tenant configuration is also system, then the global configuration is used.

If there are no tenants configured under dial-peer, then the configurations are applied using the default behavior in the
                           following order:

Dial-peer configuration

Global configuration

The following table lists the various configurations present under voice class tenant <tag> . For more information on specific configurations, see the Voice and Video command reference guide lists.

Attributes that are not available under voice class tenant <tag> use the default behavior—With preference of dial-peer followed by the global configuration.

Command

Description

aaa

SIP-UA AAA related configuration

anat

Allow alternative network address types IPv4 and IPv6

asserted-id

Configure SIP UA privacy identity settings

associate

Associate a RCB for outgoing calls

asymmetric

Configure global SIP asymmetric payload support

authentication

Digest Authentication Configuration

bandwidth

Allow SIP SDP bandwidth-related options

bind

SIP bind command

block

Block 18X response to INVITE

call-route

Configure call routing options

conn-reuse

Reuse the sip registration tcp connection for the end-point behind a Firewall

connection-reuse

Use listener port for sending requests over UDP

contact-passing

302 contact to be passed through for CFWD

content

Content carried as part of SIP message

copy-list

Configure list of entities to be sent to peer leg

credentials

User credentials for registration

disable-early-media

Disable early-media cut through

dns -a-override

Skip DNS A/AAAA query when SRV query timesout

dscp -profile

DSCP Profile global config

early-media

Configure method to handle early-media Update Request

early-offer

Configure sending Early-Offer

encap

Configure SDP encapsulation

error-code-override

Configure sip error code

error- passthru

SIP error response pass-thru functionality

exit

Exits from the voice class configuration mode

g729

G729 codec interoperability settings

handle-replaces

Handle INVITE with REPLACES header at SIP spi

header-passing

SIP Headers need to be passed to applications

help

Description of the interactive help system

history-info

History Info header support

host-registrar

Use sip-ua registrar value in Diversion and Contact header for 3xx messages

interop-handling

Enable interop-handling

localhost

Specify the DNS name for the localhost

map

Mapping options

max-forwards

Change number of max-forwards for SIP Methods

midcall -signaling

Configure method to handle mid-call signaling

nat

SIP nat global config

no

Negate a command or set its defaults

notify

SIP Signaling Notify Configuration

offer

Configure settings for Offers made from the Gateway

options-ping

Send OPTION pings to remote end

outbound-proxy

Configure an Outbound Proxy Server

pass-thru

SIP pass-through global config

permit

Permit hostname for this gateway

preloaded-route

Use pre-loaded route header for outgoing calls, if available

privacy

Configure SIP UA privacy settings

privacy-policy

Set privacy behavior for outgoing SIP messages

random-contact

Use Random Contact for outgoing calls, if available

random-request- uri

Configure options for Request-URI having random value

reason-header

Configure settings for supporting SIP Reason Header

redirection

Enable call redirection (3xx) handling

refer- ood

Configure maximum number of out-of-dialog refer made to the Gateway

referto -passing

Refer-To needs to be passed through for transfer

registrar

Configure SIP registrar VoIP Interface

registration

Enable registration options

rel1xx

Type of reliable provisional response support

remote-party-id

Enable Remote-Party-ID support in SIP User Agent

requri -passing

Request URI needs to be passed through

reset

SIP Reset Options

retry

Change default retries for each SIP Method

send

Configure outgoing message options

session

SIP Voice Protocol session config

sip-profiles

SIP Profiles global config

sip-server

Configure a SIP Server Interface

srtp

Allow SIP related SRTP options

srtp-auth

Allow to set preferred suites

tel-config

Tel format cfg for headers other than req -line in

timers

SIP Signaling Timers Configuration

update- callerid

Enable sending updates for callerid

url

Url configuration for request-line url in outgoing INVITE

video

Video related config for sip

warn-header

SIP Warning-Header global config

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Use Cisco Feature Navigator to find information about platform support and Cisco software image support. To access Cisco Feature
                                 Navigator, go to www.cisco.com/go/cfn . An account on Cisco.com is not required.

Releases

Feature
                                          					 Information

Support for Configuring Multi Tenants on SIP Trunk

Cisco IOS 15.6(2)T

Cisco IOS XE Denali 16.3.1

This feature allows the provision to configure specific global configurations for multiple tenants on SIP trunks.

The following commands were introduced: voice class tenant tag and voice-class sip tenant tag .

### Feature Characteristics of Configurable SIP Trunk Listen Port

For Cisco IOS XE Cupertino
                                          17.8.1a and later releases, you can also configure a listen-port at the tenant level. Before this release, you could configure the
                                    listen-port only at the global configuration level.

Multiple inbound TLS, TCP, or UDP connections can be established using different IP ports. Each port is mapped to a tenant
                                    trunk configuration, which may have its own TLS profile validation criteria.

A tenant listen port may only be configured when there are no active calls on associated dial-peers.

Tenant level listen-port configuration is supported for both secure (TLS) and nonsecure (TCP/UDP) transport types.

Interface binding must be configured for a tenant to use a SIP trunk listen port.

IPv4 and IPv6 listen ports may be configured for TLS, TCP or UDP transport types.

The listen-port along with the bind interface must be unique across all:

Global and tenant level configuration modes

Secure and nonsecure ports

If you modify the interface to which a tenant is bound, the existing listen-port will be closed and re-opened with the latest
                                    interface details.

When there is a configuration change at the bind or tenant level , all the associated active connections are closed.

The nonsecure listen-port range is limited to 5000 - 5500 to avoid overlap with the RTP port range, especially for UDP.

Connections get segregated at the tenant level during inbound dial-peer matching. For this, the tenant tag in the inbound
                                    dial-peer is matched with the tenant tag that is identified during connection establishment.

To use the SIP trunk listen port feature, must configure the associated tenant with a SIP listen port:

tls-profile <tag> under voice class tenant tag configuration mode.

For more information on the CLI commands, see Cisco IOS Voice Command Reference Guide .

Feature Characteristics of Trunk Specific TLS Policy

For TLS connections, the trustpoint selection is as follows:

The trustpoint is selected based on tenant configuration.

If this is not available, then the remote-IP or global configurations are used.

Except for the CN-SAN certificate validation, CUBE retains the same behavior for inbound nonsecure connections (TCP and UDP transport types).

To use a trunk specific TLS policy, you must configure the associated tenant with a TLS policy:

listen-port { non-secure port-number | secure port-number } under voice class tenant tag configuration mode.

For more information on the CLI commands, see Cisco IOS Voice Command Reference Guide .

## Configure SIP Trunks using Voice Class Tenant

### SUMMARY STEPS

- enable

- configure terminal

- Use the following to configure trunks using the tenant feature:

Once you configure the voice class tenant <tag> command in the global mode, the configuration will move to the voice class tenant <tag> submode. You can configure all the sip-specific attributes in this submode.

- voice-class sip tenant <tag> in the dial-peer configuration mode

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter
                                                					 your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

Use the following to configure trunks using the tenant feature:

Once you configure the voice class tenant <tag> command in the global mode, the configuration will move to the voice class tenant <tag> submode. You can configure all the sip-specific attributes in this submode.

- voice-class sip tenant <tag> in the dial-peer configuration mode

### Example:

```
! Configuring tenant 1 Device(config)# voice class tenant 1 Device (config-class)# ? aaa – sip-ua AAA related configuration
anat – Allow alternative network address types IPV4 and IPV6
asserted-id – Configure SIP-UA privacy identity settings
……
……
……
Video – video related function
Warn-header – SIP related config for SIP. SIP warning-header global config.
Device (config-voi-tenant)# end
-------- ! Configuring tenant 2 Device(config)# voice class tenant 2 Device (config-class)# ? aaa – sip-ua AAA related configuration
anat – Allow alternative network address types IPV4 and IPV6
asserted-id – Configure SIP-UA privacy identity settings
……
……
outbound-proxy - Configure an Outbound Proxy Server
pass-thru  - SIP pass-through global config
……
……
srtp - Allow SIP related SRTP options
Warn-header – SIP related config for SIP. SIP warning-header global config.
Device (config-voi-tenant)# end
```

### Example:

```
!Configuring tenant 1 under dial-peer 10 Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip tenant 1 Device (config-dial-peer)# end
------------- !Configuring tenant 2 under dial-peer 20 Device (config)# dial-peer voice 20 voip Device (config-dial-peer)# voice-class sip tenant 2 Device (config-dial-peer)# end !An example for the use of the "no" form of command voice-class sip tenant Router(config)# dial-peer voice 3000 voip
Router(config-dial-peer)# voice-class sip tenant 1
Router(config-dial-peer)# no voice-class sip tenant 1
```

When the no form is configured, the dial-peer is no longer associated with the tenant tag configuration. The attributes are now applied
                                          using the default order of dial-peer followed by the global configuration.

Use the voice-class sip tenant <tag> command in the global configuration mode to configure a tenant with sip-specific attributes. This command tag can then be
                                          applied to one or more dial-peers using the voice-class sip tenant <tag> command under the dial-peers.

Step 4

end

### Example:

```
Device(config-dial-peer)# end
```

Returns to
                                          				privileged EXEC mode.

### Example: Multiple Trunks using Registration with Tenants

Trunk registration details may also be included in a tenant configuration, allowing a platform to register to multiple registrars
                              concurrently. Tenants configured with registration details do not need to be associated with a dial-peer for the registration
                              process to start.

```
Router# show run | sec tenant Voice class tenant 1 registrar 1 ipv4:10.64.86.35:9051 expires 3600 credentials username aaaa password 7 06070E204D realm aaaa.com
outbound-proxy ipv4:10.64.86.35:9057
bind control source-interface GigabitEthernet0/0 Voice class tenant 2 registrar 1 ipv4:9.65.75.45:9052 expires 3600 credentials username bbbb password 7 110B1B0715 realm bbbb.com
outbound-proxy ipv4:10.64.86.40:9040
bind control source-interface GigabitEthernet0/1
```

For multi-tenancy support on Cisco Unified Border Element, you can configure voice class tenants with different credentials,
                              but having the same registrar. In that scenario, it is recommended that you configure the CLI commands sip-server and registrar under voice class tenant configuration. The following is a sample configuration:

```
voice class tenant 1
 credentials number 1111 username test password 7 071B245B5D1D realm ipvoice.jp
 authentication username test password 7 06120A3258
 registrar ipv4:1.1.1.1 expires 120
 sip-server ipv4:1.1.1.1
!
voice class tenant 2
 credentials number 2222 username test password 7 09584B1E0A11 realm ipvoice.jp
 authentication username test2 password 7 071B245F5A
 registrar ipv4:1.1.1.1 expires 120
 sip-server ipv4:1.1.1.1
```

| Note | Attributes that are not available under voice class tenant <tag> use the default behavior—With preference of dial-peer followed by the global configuration. |
|---|---|

| Command | Description |
|---|---|
| aaa | SIP-UA AAA related configuration |
| anat | Allow alternative network address types IPv4 and IPv6 |
| asserted-id | Configure SIP UA privacy identity settings |
| associate | Associate a RCB for outgoing calls |
| asymmetric | Configure global SIP asymmetric payload support |
| authentication | Digest Authentication Configuration |
| bandwidth | Allow SIP SDP bandwidth-related options |
| bind | SIP bind command |
| block | Block 18X response to INVITE |
| call-route | Configure call routing options |
| conn-reuse | Reuse the sip registration tcp connection for the end-point behind a Firewall |
| connection-reuse | Use listener port for sending requests over UDP |
| contact-passing | 302 contact to be passed through for CFWD |
| content | Content carried as part of SIP message |
| copy-list | Configure list of entities to be sent to peer leg |
| credentials | User credentials for registration |
| disable-early-media | Disable early-media cut through |
| dns -a-override | Skip DNS A/AAAA query when SRV query timesout |
| dscp -profile | DSCP Profile global config |
| early-media | Configure method to handle early-media Update Request |
| early-offer | Configure sending Early-Offer |
| encap | Configure SDP encapsulation |
| error-code-override | Configure sip error code |
| error- passthru | SIP error response pass-thru functionality |

| exit | Exits from the voice class configuration mode |
|---|---|
| g729 | G729 codec interoperability settings |
| handle-replaces | Handle INVITE with REPLACES header at SIP spi |
| header-passing | SIP Headers need to be passed to applications |
| help | Description of the interactive help system |
| history-info | History Info header support |
| host-registrar | Use sip-ua registrar value in Diversion and Contact header for 3xx messages |
| interop-handling | Enable interop-handling |
| localhost | Specify the DNS name for the localhost |
| map | Mapping options |
| max-forwards | Change number of max-forwards for SIP Methods |
| midcall -signaling | Configure method to handle mid-call signaling |
| nat | SIP nat global config |
| no | Negate a command or set its defaults |
| notify | SIP Signaling Notify Configuration |
| offer | Configure settings for Offers made from the Gateway |
| options-ping | Send OPTION pings to remote end |
| outbound-proxy | Configure an Outbound Proxy Server |
| pass-thru | SIP pass-through global config |
| permit | Permit hostname for this gateway |
| preloaded-route | Use pre-loaded route header for outgoing calls, if available |
| privacy | Configure SIP UA privacy settings |
| privacy-policy | Set privacy behavior for outgoing SIP messages |
| random-contact | Use Random Contact for outgoing calls, if available |
| random-request- uri | Configure options for Request-URI having random value |

| reason-header | Configure settings for supporting SIP Reason Header |
|---|---|
| redirection | Enable call redirection (3xx) handling |
| refer- ood | Configure maximum number of out-of-dialog refer made to the Gateway |
| referto -passing | Refer-To needs to be passed through for transfer |
| registrar | Configure SIP registrar VoIP Interface |
| registration | Enable registration options |
| rel1xx | Type of reliable provisional response support |
| remote-party-id | Enable Remote-Party-ID support in SIP User Agent |
| requri -passing | Request URI needs to be passed through |
| reset | SIP Reset Options |
| retry | Change default retries for each SIP Method |
| send | Configure outgoing message options |
| session | SIP Voice Protocol session config |
| sip-profiles | SIP Profiles global config |
| sip-server | Configure a SIP Server Interface |
| srtp | Allow SIP related SRTP options |
| srtp-auth | Allow to set preferred suites |
| tel-config | Tel format cfg for headers other than req -line in |
| timers | SIP Signaling Timers Configuration |
| update- callerid | Enable sending updates for callerid |
| url | Url configuration for request-line url in outgoing INVITE |
| video | Video related config for sip |
| warn-header | SIP Warning-Header global config |

| Feature Name | Releases | Feature
                                          					 Information |
|---|---|---|
| Support for Configuring Multi Tenants on SIP Trunk | Cisco IOS 15.6(2)T Cisco IOS XE Denali 16.3.1 | This feature allows the provision to configure specific global configurations for multiple tenants on SIP trunks. The following commands were introduced: voice class tenant tag and voice-class sip tenant tag . |

| Note | Except for the CN-SAN certificate validation, CUBE retains the same behavior for inbound nonsecure connections (TCP and UDP transport types). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter
                                                					 your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Use the following to configure trunks using the tenant feature: voice class tenant <tag> in the global configuration mode Once you configure the voice class tenant <tag> command in the global mode, the configuration will move to the voice class tenant <tag> submode. You can configure all the sip-specific attributes in this submode. voice-class sip tenant <tag> in the dial-peer configuration mode Example: In global configuration mode ! Configuring tenant 1 Device(config)# voice class tenant 1 Device (config-class)# ? aaa – sip-ua AAA related configuration
anat – Allow alternative network address types IPV4 and IPV6
asserted-id – Configure SIP-UA privacy identity settings
……
……
……
Video – video related function
Warn-header – SIP related config for SIP. SIP warning-header global config.
Device (config-voi-tenant)# end
-------- ! Configuring tenant 2 Device(config)# voice class tenant 2 Device (config-class)# ? aaa – sip-ua AAA related configuration
anat – Allow alternative network address types IPV4 and IPV6
asserted-id – Configure SIP-UA privacy identity settings
……
……
outbound-proxy - Configure an Outbound Proxy Server
pass-thru  - SIP pass-through global config
……
……
srtp - Allow SIP related SRTP options
Warn-header – SIP related config for SIP. SIP warning-header global config.
Device (config-voi-tenant)# end Example: In dial-peer configuration mode !Configuring tenant 1 under dial-peer 10 Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip tenant 1 Device (config-dial-peer)# end
------------- !Configuring tenant 2 under dial-peer 20 Device (config)# dial-peer voice 20 voip Device (config-dial-peer)# voice-class sip tenant 2 Device (config-dial-peer)# end !An example for the use of the "no" form of command voice-class sip tenant Router(config)# dial-peer voice 3000 voip
Router(config-dial-peer)# voice-class sip tenant 1
Router(config-dial-peer)# no voice-class sip tenant 1 When the no form is configured, the dial-peer is no longer associated with the tenant tag configuration. The attributes are now applied
                                          using the default order of dial-peer followed by the global configuration. | Use the voice-class sip tenant <tag> command in the global configuration mode to configure a tenant with sip-specific attributes. This command tag can then be
                                          applied to one or more dial-peers using the voice-class sip tenant <tag> command under the dial-peers. |
| Step 4 | end Example: Device(config-dial-peer)# end | Returns to
                                          				privileged EXEC mode. |