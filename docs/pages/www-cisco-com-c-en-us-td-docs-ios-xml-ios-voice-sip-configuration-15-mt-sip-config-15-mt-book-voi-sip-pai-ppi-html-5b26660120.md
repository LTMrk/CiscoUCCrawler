---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-sip-configuration-15-mt-sip-config-15-mt-book-voi-sip-pai-ppi-html-5b26660120
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/sip/configuration/15-mt/sip-config-15-mt-book/voi-sip-pai-ppi.html
retrieved_at: 2026-08-20T23:45:40.103191+00:00
---

SIP Configuration Guide, Cisco IOS Release 15M&T

# SIP Configuration Guide, Cisco IOS Release 15M&T

Updated: November 25, 2014

Chapter: PAI or PPI Header in Incoming and Outgoing SIP Calls

## Chapter: PAI or PPI Header in Incoming and Outgoing SIP Calls

# PAI or PPI Header in Incoming and Outgoing SIP Calls

Prior to the introduction of the PAI or PPI Header in Incoming and Outgoing SIP Calls feature, the P-Asserted-Identity (PAI)
                        or the P-Preferred-Identity (PPI) privacy header was supported for outgoing calls at the global level. The PAI or PPI Header
                        in Incoming and Outgoing SIP Calls feature is an enhancement to support PAI or PPI header for incoming and outgoing calls
                        at the global level and dial-peer configuration mode.

This module describes how to enable support for the PAI or the PPI privacy header in incoming and outgoing Session Initiation
                        Protocol (SIP) requests or response messages.

## Finding Feature Information for PAI or PPI Header in Incoming and Outgoing SIP Calls

Your software release may not support all the features documented in this module. For the latest feature information and caveats,
                              see the release notes for your platform and software release. To find information about the features documented in this module,
                              and to see a list of the releases in which each feature is supported, see the Feature Information for Handling PAI or PPI Header in Incoming and Outgoing SIP Calls .

Use Cisco Feature Navigator to find information about platform support and Cisco software image support. To access Cisco Feature
                              Navigator, go to http://www.cisco.com/go/cfn .
                              
                              An account on Cisco.com is not required.

## Contents

## Information About PAI or PPI Header in Incoming and Outgoing SIP Calls

### PAI or PPI Header Overview

For incoming SIP requests or response messages, when the PAI or PPI privacy header is set, the SIP gateway builds the PAI
                              or PPI header into the common SIP stack, thereby providing support to handle the call data present in the PAI or PPI header.
                              To process the data from the PAI or PPI header of incoming SIP calls, we recommend that you enable the asserted ID for the
                              incoming dial peer.

For outgoing SIP requests or response messages, when the PAI or PPI privacy header is set, privacy information is sent using
                              the PAI or PPI header.

If the PAI or PPI asserted ID is not enabled either in dial-peer configuration mode or at the global level, the call data
                                          present in the PAI or PPI header of incoming SIP calls is ignored.

### Support for PAI or PPI Header at the Global Level

At the global level, the support for the PAI or PPI header in incoming and outgoing calls is provided using the asserted-id command. The asserted-id command enables the support for generating the PAI or PPI header, or the Remote-Party-ID (RPID) or FROM header data, to populate
                              outbound calling information.

### Support for PAI or PPI Header in Dial-Peer Configuration Mode

In dial-peer configuration mode, the support for the PAI or PPI header in incoming and outgoing calls is provided using the voice-class sip asserted-id command. The voice-class sip asserted-id command enables the support for generating the PAI or PPI header, or the Remote-Party-ID (RPID) or FROM header data, to populate
                              outbound calling information.

## How to Configure PAI or PPI Header in Incoming and Outgoing SIP Calls

### Configuring the PAI or PPI Privacy Header at the Global Level

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- asserted-id { pai | ppi }

- end

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters voice service VoIP configuration mode.

sip

#### Example:

```
Router(conf-voi-serv)# sip
```

Enters voice service VoIP-SIP configuration mode.

asserted-id { pai | ppi }

#### Example:

```
Router(conf-serv-sip)# asserted-id pai
```

Configures the privacy header for incoming and outgoing SIP requests and response messages.

pai --Specifies the PAI type privacy header.

ppi --Specifies the PPI type privacy header.

end

#### Example:

```
Router(conf-serv-sip)# end
```

Exits voice service VoIP-SIP configuration mode and returns to privileged EXEC mode.

### Configuring the PAI or PPI Privacy Header in Dial-Peer Configuration Mode

### SUMMARY STEPS

- enable

- configure terminal

- dial peer voice tag

- voice-class sip asserted-id { pai | ppi | system }

- end

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

dial peer voice tag

#### Example:

```
Router(config)# dial peer voice 1
```

Enters dial-peer configuration mode.

voice-class sip asserted-id { pai | ppi | system }

#### Example:

```
Router(config-dial-peer)# voice-class sip asserted-id pai
```

Configures the privacy header for incoming and outgoing SIP requests and response messages.

pai --Specifies the PAI type privacy header.

ppi --Specifies the PPI type privacy header.

system --Uses the global-level configuration settings to configure the dial peer.

end

#### Example:

```
Router(config-dial-peer)# end
```

Exits dial-peer configuration mode and returns to privileged EXEC mode.

## Configuration Examples for PAI or PPI Header in Incoming and Outgoing SIP Calls

### Example  Configuring the PAI or PPI Privacy Header at the Global Level

The following example shows how to enable support for the PAI privacy header:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# asserted-id pai
```

### Example  Configuring the PAI or PPI Privacy Header in Dial-Peer Configuration Mode

The following example shows how to enable support for the PPI header:

```
Router> enable Router# configure terminal Router(config)# dial peer voice 1 Router(conf-voi-serv)# voice-class sip asserted-id ppi
```

## Additional References

### Related Documents

Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

Cisco IOS Voice commands

Cisco IOS Voice Command Reference

Cisco IOS Voice Configuration Library

For more information about Cisco IOS voice features, including feature documents, and troubleshooting information:

http://www.cisco.com/en/US/docs/ios/12_3/vvf_c/
                                             cisco_ios_voice_configuration_library_glossary/vcl.htm

### Standards

Standard

Title

None

--

### MIBs

MIB

MIBs Link

None

--

### RFCs

RFC

Title

None

--

### Technical Assistance

Description

Link

The Cisco Support and Documentation website provides online resources to download documentation, software, and tools. Use
                                          these resources to install and configure the software and to troubleshoot and resolve technical issues with Cisco products
                                          and technologies. Access to most tools on the Cisco Support and Documentation website requires a Cisco.com user ID and password.

http://www.cisco.com/cisco/web/support/index.html

## Feature Information for Handling PAI or PPI Header in Incoming and Outgoing SIP Calls

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

PAI or PPI Header in Incoming and Outgoing SIP Calls

12.4(24)T 15.1(3)T

Prior to the introduction of the PAI or PPI Header in Incoming and Outgoing SIP Calls feature, the PAI or the PPI privacy
                                          header was supported for outgoing calls at global level. The PAI or PPI Header in Incoming and Outgoing SIP Calls feature
                                          is an enhancement to support the PAI or the PPI privacy header for incoming and outgoing calls at the global level and dial-peer
                                          configuration mode.

The following commands were introduced or modified: asserted-id , voice-class sip asserted-id .

| Note | If the PAI or PPI asserted ID is not enabled either in dial-peer configuration mode or at the global level, the call data
                                          present in the PAI or PPI header of incoming SIP calls is ignored. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service VoIP configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters voice service VoIP-SIP configuration mode. |
| Step 5 | asserted-id { pai \| ppi } Example: Router(conf-serv-sip)# asserted-id pai | Configures the privacy header for incoming and outgoing SIP requests and response messages. pai --Specifies the PAI type privacy header. ppi --Specifies the PPI type privacy header. |
| Step 6 | end Example: Router(conf-serv-sip)# end | Exits voice service VoIP-SIP configuration mode and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial peer voice tag Example: Router(config)# dial peer voice 1 | Enters dial-peer configuration mode. |
| Step 4 | voice-class sip asserted-id { pai \| ppi \| system } Example: Router(config-dial-peer)# voice-class sip asserted-id pai | Configures the privacy header for incoming and outgoing SIP requests and response messages. pai --Specifies the PAI type privacy header. ppi --Specifies the PPI type privacy header. system --Uses the global-level configuration settings to configure the dial peer. |
| Step 5 | end Example: Router(config-dial-peer)# end | Exits dial-peer configuration mode and returns to privileged EXEC mode. |

| Related Topic | Document Title |
|---|---|
| Cisco IOS commands | Cisco IOS Master Commands List, All Releases |
| Cisco IOS Voice commands | Cisco IOS Voice Command Reference |
| Cisco IOS Voice Configuration Library | For more information about Cisco IOS voice features, including feature documents, and troubleshooting information: http://www.cisco.com/en/US/docs/ios/12_3/vvf_c/
                                             cisco_ios_voice_configuration_library_glossary/vcl.htm |

| Standard | Title |
|---|---|
| None | -- |

| MIB | MIBs Link |
|---|---|
| None | -- |

| RFC | Title |
|---|---|
| None | -- |

| Description | Link |
|---|---|
| The Cisco Support and Documentation website provides online resources to download documentation, software, and tools. Use
                                          these resources to install and configure the software and to troubleshoot and resolve technical issues with Cisco products
                                          and technologies. Access to most tools on the Cisco Support and Documentation website requires a Cisco.com user ID and password. | http://www.cisco.com/cisco/web/support/index.html |

| Feature Name | Releases | Feature Information |
|---|---|---|
| PAI or PPI Header in Incoming and Outgoing SIP Calls | 12.4(24)T 15.1(3)T | Prior to the introduction of the PAI or PPI Header in Incoming and Outgoing SIP Calls feature, the PAI or the PPI privacy
                                          header was supported for outgoing calls at global level. The PAI or PPI Header in Incoming and Outgoing SIP Calls feature
                                          is an enhancement to support the PAI or the PPI privacy header for incoming and outgoing calls at the global level and dial-peer
                                          configuration mode. The following commands were introduced or modified: asserted-id , voice-class sip asserted-id . |