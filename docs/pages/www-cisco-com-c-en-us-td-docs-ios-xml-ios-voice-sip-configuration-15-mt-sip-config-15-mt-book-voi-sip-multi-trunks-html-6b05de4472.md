---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-sip-configuration-15-mt-sip-config-15-mt-book-voi-sip-multi-trunks-html-6b05de4472
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/sip/configuration/15-mt/sip-config-15-mt-book/voi-sip-multi-trunks.html
retrieved_at: 2026-08-16T23:08:15.320707+00:00
---

SIP Configuration Guide, Cisco IOS Release 15M&T

# SIP Configuration Guide, Cisco IOS Release 15M&T

Updated: November 25, 2014

Chapter: Configuring Multiple Registrars on SIP Trunks

## Chapter: Configuring Multiple Registrars on SIP Trunks

# Configuring Multiple Registrars on SIP Trunks

The Support for Multiple Registrars on SIP Trunks on a Cisco Unified Border Element, on Cisco IOS SIP TDM Gateways, and on
                        Cisco Unified Communications Manager Express feature allows configuration of multiple registrars on Session Initiation Protocol
                        (SIP) trunks, each simultaneously registered using their respective authentication instance. This feature allows a redundant
                        registrar for each of the SIP trunks, which provides SIP trunk redundancy across multiple service providers.

## Finding Feature Information

Your software release may not support all the features documented in this module. For the latest caveats and feature information,
                           see Bug Search Tool and the release notes for your platform and software release. To find information about the features documented in this module,
                           and to see a list of the releases in which each feature is supported, see the feature information table at the end of this
                           module.

Use Cisco Feature Navigator to find information about platform support and Cisco software image support. To access Cisco Feature
                           Navigator, go to www.cisco.com/go/cfn . An account on Cisco.com is not required.

## Prerequisites for Configuring Multiple Registrars on SIP Trunks

Before configuring support for multiple registrars on the SIP trunks of Cisco IOS SIP time-division multiplexing (TDM) gateways,
                           Cisco Unified Border Elements (Cisco UBEs), or Cisco Unified Communications Manager Express (Cisco Unified CME), verify the
                           SIP configuration within the VoIP network for the appropriate originating and terminating gateways as described in documentation
                           listed in the "Related Documents" section.

## Restrictions for Configuring Multiple Registrars on SIP Trunks

Configuring multiple registrars on SIP trunks has the following restrictions:

Old and new forms of registrar command are mutually exclusive: the registrar can be configured in either primary/secondary
                                 mode or multiple registrar mode--not both.

Dynamic Host Configuration Protocol (DHCP) support is not available with multiple registrars (available for primary/secondary
                                 mode only).

Only one authentication configuration per username can be configured at any one time.

A maximum of six registrars can be configured at any given time.

A maximum of 12 different realms can be configured for each endpoint.

You cannot restrict the registration of specific endpoints with specific registrars--once a new registrar is configured, all
                                 endpoints will begin registering to the new registrar.

You cannot remove multiple configurations of credentials simultaneously--only one credential can be removed at a time.

## Information About Configuring Multiple Primary SIP Trunks

To configure multiple registrars on SIP trunks, you should understand the following concepts:

### Purpose of Multiple Registrars on SIP Trunks

You can configure endpoints on Cisco IOS SIP TDM gateways, Cisco UBEs, and Cisco Unified CME to register to a primary and
                              a secondary registrar. You can use this setup to register all endpoints to their assigned registrar using authentication details
                              that can be associated with only one domain (or service provider). The drawback is that if the registrar or service provider
                              domain becomes unavailable, users supported on Cisco IOS SIP TDM gateways, Cisco UBEs, and Cisco Unified CME cannot make or
                              receive calls.

The Support for Multiple Registrars on SIP Trunks on a Cisco Unified Border Element, on Cisco IOS SIP TDM Gateways, and on
                              Cisco Unified Communications Manager Express feature provides support for simultaneous registration with multiple registrars
                              for endpoints on Cisco IOS SIP TDM gateways, Cisco UBEs, and Cisco Unified CME. This feature allows outbound and inbound traffic
                              to be distributed across different service providers while simultaneously providing redundancy for users supported on these
                              devices.

In a Cisco UBE multihome environment, all sets of credentials configured under the SIP user agent are sent to all configured
                                          registrars, regardless of realm configuration. This means that if a Cisco UBE registers multiple service providers, the credentials
                                          for both service providers are sent out to both. While the correct credentials will register, the incorrect sets will fail,
                                          possibly resulting in security measures taken by the service provider for failed registration attempts.

### Authentication Attributes and Enhancements

The Support for Multiple Registrars on SIP Trunks on a Cisco Unified Border Element, on Cisco IOS SIP TDM Gateways, and on
                              Cisco Unified Communications Manager Express feature is available in Cisco IOS Release 15.0(1)XA and later releases and utilizes
                              the authentication command to allow configuration for specific endpoints and includes the following attributes and enhancements:

You can configure up to 12 instances of the authentication command for a given endpoint, supporting 12 different realms for a single service provider domain.

The authentication behavior can handle challenges from different service providers for SIP REGISTER and SIP INVITE/Other messages.

You can specify a realm, which acts as a unique key for picking up username and password authentication details for each endpoint.

The system uses authentication details to rebuild SIP Request messages in response to challenges.

Enhancements introduced by this feature apply at both the dial peer and SIP user agent (UA) level.

### Credentials Attributes and Enhancements

The credentials command is used to trigger SIP Register requests wherever registration is required for users who are not part of any POTS
                              dial peers. The Support for Multiple Registrars on SIP Trunks on a Cisco Unified Border Element, on Cisco IOS SIP TDM Gateways,
                              and on Cisco Unified Communications Manager Express feature is available in Cisco IOS Release 15.0(1)XA and later releases
                              and modifies the credentials command to allow configuration for specific endpoints and includes the following attributes and enhancements:

Credentials behavior supports SIP REGISTER and SIP INVITE/Other message challenges.

You can use the number keyword to specify an endpoint, the value of which is used to populate the user portion of the To field in outgoing SIP REGISTER
                                    messages.

The number keyword is optional and is used to allow the endpoint number to be different from the username.

When both number and realm are configured, this pair of values acts as a unique key to pick up the username and password credentials
                                    configured for the endpoint.

A maximum of 12 different realms can be configured for a given endpoint.

### Determination of Authentication Details

When a SIP INVITE or SIP REGISTER request is challenged, the username and password details for authentication are determined
                              in the following order:

Configuring more than one username is not supported--you must remove any currently configured username before configuring
                                          a new username.

If the realm specified in the challenge matches the realm in the authentication configuration for a POTS dial peer, the system
                                    uses the corresponding username and password.

If the realm specified in the challenge doesn’t match the configured authentication for the POTS dial peer, then it will check
                                    for credentials configured for SIP UA.

If the realm specified in the challenge does not match the realm configured for credentials, then it will check for authentication
                                    configurations for SIP UA.

If the system does not find a matching authentication or credential for the received realm, then the request is terminated.

If there is no realm specified for the authentication configuration, then the system uses the username received from the challenge
                                    to build the response message.

### Use of Preferred Option

When the primary and secondary registrar scenario is configured, the registrar address is used to populate the host portion
                              of the From header in outbound SIP INVITE messages. However, when multiple registrars are configured, the only way to determine
                              which registrar address is used to populate the host portion of the From header is to designate a single service provider
                              domain as the preferred localhost name. The following behaviors are the result of using the preferred keyword with the localhost command (or voice-class sip localhost command for individual dial peers) when configuring multiple registrars:

If the localhost command is enabled with the optional preferred keyword included, then the From header of outgoing SIP INVITE messages is populated with the domain name specified by the localhost command configuration.

If the localhost command is not enabled or if it is enabled without the optional preferred keyword, then the best local interface address is used to populate the From header of outgoing SIP INVITE messages.

## How to Configure Multiple Registrars on SIP Trunks

The tasks for configuring multiple registrars on the SIP trunks of Cisco IOS SIP TDM gateways, Cisco UBEs, or Cisco Unified
                           CME are included in the following sections:

### Configuring Multiple Registrars on SIP Trunks

To configure multiple registrars on SIP trunks, use the registrar and authentication commands as described in the following tasks:

#### Registration of POTS Endpoints to Multiple Registrars on SIP Trunks

Use the registrar command in SIP UA configuration mode to register POTS endpoints on a Cisco IOS SIP TDM gateway, Cisco UBE, or Cisco Unified
                                    CME to multiple registrars. To do so, you need to configure the command once for each registrar.

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- registrar registrar-index registrar-server-address expires seconds

### DETAILED STEPS

enable

##### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global configuration mode.

sip-ua

##### Example:

```
Router(config)# sip-ua
```

Enters SIP UA configuration mode.

registrar registrar-index registrar-server-address expires seconds

##### Example:

```
Router(config-sip-ua)# registrar 1 dns:example1.com expires 180
```

##### Example:

```
Router(config-sip-ua)# registrar 2 dns:example2.com expires 60
```

Enables a Cisco IOS voice gateway to register E.164 numbers with external SIP proxies or SIP registrars. The register-index range is 1 to 6. (The expires timer specification is optional).

#### Global Configuration of Authentication for POTS Endpoints with Multiple Registrars on a SIP Trunk

Use the authentication command in SIP UA configuration mode to configure authentication of endpoints on a Cisco IOS SIP TDM gateway, Cisco UBE,
                                    or Cisco Unified CME to multiple registrars. To do so, you need to configure the command once for each registrar.

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- authentication username username password [ 0 | 7 ] password [ realm realm ]

### DETAILED STEPS

enable

##### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global configuration mode.

sip-ua

##### Example:

```
Router(config)# sip-ua
```

Enters SIP UA configuration mode.

authentication username username password [ 0 | 7 ] password [ realm realm ]

##### Example:

```
Router(config-sip-ua)# authentication username MyUsername password MyPassword realm Realm1.example.com
```

##### Example:

```
Router(config-sip-ua)# authentication username MyUsername password MyPassword realm Realm2.example.com
```

Enables SIP digest authentication globally (encryption type and realm specification are optional).

#### Dial Peer Configuration of Authentication for POTS

Use the authentication command in dial peer voice configuration mode to authenticate endpoints on a Cisco IOS SIP TDM gateway to multiple registrars
                                    on SIP trunks. To do so, you need to configure the command once for each registrar.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice 1 pots

- authentication username username password [ 0 | 7 ] password [ realm realm ]

### DETAILED STEPS

enable

##### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global configuration mode.

dial-peer voice 1 pots

##### Example:

```
Router(config)# dial-peer voice 1 pots
```

Enters dial peer voice configuration mode.

authentication username username password [ 0 | 7 ] password [ realm realm ]

##### Example:

```
Router(config-dial-peer)# authentication username MyUser password 7 MyPassword realm Realm1.example.com
```

##### Example:

```
Router(config-dial-peer)# authentication username MyUser password 7 MyPassword realm Realm2.example.com
```

Enables SIP digest authentication on an individual dial peer (encryption type and realm specification are optional).

#### Configuration of Credentials for Registering POTS Endpoints with Multiple Registrars on SIP Trunks

Use the credentials command in SIP UA configuration mode to configure registration requests sent from a Cisco IOS SIP TDM gateway, Cisco Unified
                                    CME, or a Cisco UBE to multiple registrars on a SIP trunk.

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- credentials { dhcp | number number username username } password [ 0 | 7 ] password realm realm

### DETAILED STEPS

enable

##### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global configuration mode.

sip-ua

##### Example:

```
Router(config)# sip-ua
```

Enters SIP UA configuration mode.

credentials { dhcp | number number username username } password [ 0 | 7 ] password realm realm

##### Example:

```
Router(config-sip-ua)# credentials number 1111 username MyUsername password MyPassword realm Realm1.example.com
```

##### Example:

```
Router(config-sip-ua)# credentials number 1111 username MyUsername password MyPassword realm Realm2.example.com
```

##### Example:

```
Router(config-sip-ua)# credentials number 1111 username AnotherUsername password TheirPassword realm Realm1.example.com
```

##### Example:

```
Router(config-sip-ua)# credentials number 1111 username AnotherUsername password TheirPassword realm Realm2.example.com
```

Configures credentials for endpoints on a Cisco IOS SIP TDM gateway, Cisco Unified CME, or Cisco UBE for responding to authentication
                                                challenges.

The encryption type specification is optional but the dhcp keyword is not allowed when configuring credentials for multiple registrars on a SIP trunk.

## Configuration Examples for Configuring Multiple Registrars on SIP Trunks

### Registering POTS Endpoints to Multiple Registrars on SIP Trunks  Example

The following example shows how to configure POTS endpoints to register with multiple registrars (“example1.com” and “example2.com”)
                                 on a SIP trunk simultaneously:

```
Router> enable Router# configure terminal Router(config)# sip-ua Router(config-sip-ua)# registrar 1 dns:example1.com expires 180 Router(config-sip-ua)# registrar 2 dns:example2.com expires 360 Router(config-sip-ua)# authentication username MyUsername password MyPassword1 realm Realm.example1.com Router(config-sip-ua)# authentication username MyUsername password MyPassword2 realm AnotherRealm.example1.com Router(config-sip-ua)# authentication username MyUsername password MyPassword3 realm Realm.example2.com Router(config-sip-ua)# authentication username MyUsername password MyPassword4 realm AnotherRealm.example2.com
```

### Registering Individual POTS Endpoints on a Cisco IOS SIP

The following example shows how to configure individual POTS endpoints on a Cisco IOS SIP TDM gateway to register with multiple
                                 registrars (“Realm1” and “Realm2”) on a SIP trunk simultaneously:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 3 pots Router(config-dial-peer)# authentication username MyUser password MyPassword realm realm1.example.com Router(config-dial-peer)# authentication username MyUser password MyPassword2 realm Realm2.example.com Router(config-dial-peer)# exit
Router(config)# sip-ua Router(config-sip-ua)# registrar 1 dns:example1.com expires 180 Router(config-sip-ua)# registrar 2 ipv4:1.1.1.1 expires 360
```

### Configuring Credentials for Endpoints to Register with Multiple Registrars on a SIP Trunk  Example

The following example shows how to configure credentials for endpoints on a Cisco IOS SIP TDM gateway, Cisco Unified CME,
                                 or Cisco UBE to register with multiple registrars (“Example1.com” and “Example2.com”) on a SIP trunk simultaneously:

```
Router> enable Router# configure terminal Router(config)# sip-ua Router(config-sip-ua)# credentials number 1111 username MyUsername password MyPassword realm Realm.example1.com Router(config-sip-ua)# credentials number 1111 username MyUsername2 password MyOtherPassword realm AnotherRealm.example1.com Router(config-sip-ua)# credentials number 2222 username TheirUsername password TheirPassword realm Realm.example1.com Router(config-sip-ua)# credentials number 2222 username TheirUsername2 password TheirOtherPassword realm AnotherRealm.example1.com Router(config-sip-ua)# registrar 1 dns:example1.com expires 180 Router(config-sip-ua)# registrar 2 dns:example2.com expires 360
```

## Additional References

The following sections provide references related to the SIP Connection-Oriented Media, Forking, and MLPP features.

### Related Documents

Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

SIP commands

Cisco IOS Voice Command Reference

Tcl IVR and VoiceXML

Cisco IOS Tcl IVR and VoiceXML Application Guide

Cisco VoiceXML

Cisco VoiceXML Programmer’s Guide

### Standards

Standard

Title

No new or modified standards are supported, and support for existing standards has not been modified.

--

### MIBs

MIB

MIBs Link

No new or modified MIBs are supported, and support for existing MIBs has not been modified.

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco MIB Locator found at
                                          the following URL:

http://www.cisco.com/go/mibs

### RFCs

RFC

Title

No new or modified RFCs are supported, and support for existing RFCs has not been modified.

--

### Technical Assistance

Description

Link

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and
                                          resolving technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product
                                          Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.

http://www.cisco.com/cisco/web/support/index.html

## Feature Information for Configuring Multiple Registrars on SIP Trunks

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Support for Multiple Registrars on SIP Trunks on a Cisco Unified Border Element, on Cisco IOS SIP TDM Gateways, and on Cisco
                                          Unified Communications Manager Express feature

15.0(1)XA 15.1(1)T

This feature provides support for multiple registrars on SIP trunks on Cisco IOS SIP TDM gateways, Cisco Unified CME, and
                                          Cisco UBEs. This feature allows for a redundant registrar for each SIP trunk and enables registrar redundancy across multiple
                                          service providers.

This feature includes the following new or modified commands: credentials , localhost , registrar , voice-class sip localhost .

## Glossary

ISDN --Integrated Services Digital Network.

EFXS --IP phone virtual voice ports.

FXS --analog telephone voice ports.

SCCP --Skinny Client Control Protocol.

SDP --Session Description Protocol.

SIP --Session Initiation Protocol.

TDM --time-division multiplexing.

| Note | In a Cisco UBE multihome environment, all sets of credentials configured under the SIP user agent are sent to all configured
                                          registrars, regardless of realm configuration. This means that if a Cisco UBE registers multiple service providers, the credentials
                                          for both service providers are sent out to both. While the correct credentials will register, the incorrect sets will fail,
                                          possibly resulting in security measures taken by the service provider for failed registration attempts. |
|---|---|

| Note | Configuring more than one username is not supported--you must remove any currently configured username before configuring
                                          a new username. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | sip-ua Example: Router(config)# sip-ua | Enters SIP UA configuration mode. |
| Step 4 | registrar registrar-index registrar-server-address expires seconds Example: Router(config-sip-ua)# registrar 1 dns:example1.com expires 180 Example: Router(config-sip-ua)# registrar 2 dns:example2.com expires 60 | Enables a Cisco IOS voice gateway to register E.164 numbers with external SIP proxies or SIP registrars. The register-index range is 1 to 6. (The expires timer specification is optional). |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | sip-ua Example: Router(config)# sip-ua | Enters SIP UA configuration mode. |
| Step 4 | authentication username username password [ 0 \| 7 ] password [ realm realm ] Example: Router(config-sip-ua)# authentication username MyUsername password MyPassword realm Realm1.example.com Example: Router(config-sip-ua)# authentication username MyUsername password MyPassword realm Realm2.example.com | Enables SIP digest authentication globally (encryption type and realm specification are optional). |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice 1 pots Example: Router(config)# dial-peer voice 1 pots | Enters dial peer voice configuration mode. |
| Step 4 | authentication username username password [ 0 \| 7 ] password [ realm realm ] Example: Router(config-dial-peer)# authentication username MyUser password 7 MyPassword realm Realm1.example.com Example: Router(config-dial-peer)# authentication username MyUser password 7 MyPassword realm Realm2.example.com | Enables SIP digest authentication on an individual dial peer (encryption type and realm specification are optional). |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | sip-ua Example: Router(config)# sip-ua | Enters SIP UA configuration mode. |
| Step 4 | credentials { dhcp \| number number username username } password [ 0 \| 7 ] password realm realm Example: Router(config-sip-ua)# credentials number 1111 username MyUsername password MyPassword realm Realm1.example.com Example: Router(config-sip-ua)# credentials number 1111 username MyUsername password MyPassword realm Realm2.example.com Example: Router(config-sip-ua)# credentials number 1111 username AnotherUsername password TheirPassword realm Realm1.example.com Example: Router(config-sip-ua)# credentials number 1111 username AnotherUsername password TheirPassword realm Realm2.example.com | Configures credentials for endpoints on a Cisco IOS SIP TDM gateway, Cisco Unified CME, or Cisco UBE for responding to authentication
                                                challenges. Note The encryption type specification is optional but the dhcp keyword is not allowed when configuring credentials for multiple registrars on a SIP trunk. | Note | The encryption type specification is optional but the dhcp keyword is not allowed when configuring credentials for multiple registrars on a SIP trunk. |
| Note | The encryption type specification is optional but the dhcp keyword is not allowed when configuring credentials for multiple registrars on a SIP trunk. |

| Note | The encryption type specification is optional but the dhcp keyword is not allowed when configuring credentials for multiple registrars on a SIP trunk. |
|---|---|

| Related Topic | Document Title |
|---|---|
| Cisco IOS commands | Cisco IOS Master Commands List, All Releases |
| SIP commands | Cisco IOS Voice Command Reference |
| Tcl IVR and VoiceXML | Cisco IOS Tcl IVR and VoiceXML Application Guide |
| Cisco VoiceXML | Cisco VoiceXML Programmer’s Guide |

| Standard | Title |
|---|---|
| No new or modified standards are supported, and support for existing standards has not been modified. | -- |

| MIB | MIBs Link |
|---|---|
| No new or modified MIBs are supported, and support for existing MIBs has not been modified. | To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco MIB Locator found at
                                          the following URL: http://www.cisco.com/go/mibs |

| RFC | Title |
|---|---|
| No new or modified RFCs are supported, and support for existing RFCs has not been modified. | -- |

| Description | Link |
|---|---|
| The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and
                                          resolving technical issues with Cisco products and technologies. To receive security and technical information about your products, you can subscribe to various services, such as the Product
                                          Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds. Access to most tools on the Cisco Support website requires a Cisco.com user ID and password. | http://www.cisco.com/cisco/web/support/index.html |

| Feature Name | Releases | Feature Information |
|---|---|---|
| Support for Multiple Registrars on SIP Trunks on a Cisco Unified Border Element, on Cisco IOS SIP TDM Gateways, and on Cisco
                                          Unified Communications Manager Express feature | 15.0(1)XA 15.1(1)T | This feature provides support for multiple registrars on SIP trunks on Cisco IOS SIP TDM gateways, Cisco Unified CME, and
                                          Cisco UBEs. This feature allows for a redundant registrar for each SIP trunk and enables registrar redundancy across multiple
                                          service providers. This feature includes the following new or modified commands: credentials , localhost , registrar , voice-class sip localhost . |