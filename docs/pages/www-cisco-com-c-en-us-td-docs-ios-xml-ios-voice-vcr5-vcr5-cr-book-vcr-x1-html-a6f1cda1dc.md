---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-x1-html-a6f1cda1dc
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-x1.html
retrieved_at: 2026-08-16T23:16:24.170834+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: X

## Chapter: X

- X

- xfer target

# X

## xfer target

To route the INVITE to the refer-to destination in the REFER consume case, use the command xfer target refer-to . The routing decision is made based on the xfer target destination. If the target is set to dial-peer, CUBE routes the invite
                              to the dial-peer session target. If the target is set to refer-to, CUBE routes the invite to refer-to host in the REFER message.
                              To disable xfer target refer-to and set it to the default xfer target dial-peer , use the no form of this command.

xfer target refer-to

no xfer target refer-to

### Syntax Description

This command has no arguments or keywords.

### Command Default

Dial-peer is looked up for session target to route the INVITE to refer-to target.

### Command Modes

SIP UA configuration (config-sip-ua)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

Cisco IOS XE Fuji 16.9.6

This
                                          						command was introduced.

The default value is xfer target dial-peer .This command was modified to include the xfer target refer-to to route the INVITE to the refer-to host address. This command is available in Cisco IOS XE Fuji 16.9.6, Cisco IOS XE Amsterdam 17.3.1a , and Cisco IOS XE Bengaluru 17.4.1a in sip-ua and voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

By default, in the REFER consume case, the CUBE performs the dial-peer look up to route INVITE to dial-peer session target
                              with the command xfer target dial-peer . To change this behavior, you can use the command xfer target refer-to in SIP user-agent configuration mode or voice class tenant configuration mode to route the INVITE to refer-to host address.

## Examples

The following example shows how to enable xfer target refer-to on the CUBE:

```
Router(config)# sip-ua
Router(config-sip-ua)# xfer target refer-to
```

The following example shows how to enable xfer target refer-to on the CUBE in the voice class tenant configuration mode:

```
Router(config)#voice class tenant 1
Router(config-class)# xfer target refer-to
```

| Release | Modification |
|---|---|
| Cisco IOS XE Fuji 16.9.6 | This
                                          						command was introduced. |
| Cisco IOS XE Bengaluru 17.4.1a | The default value is xfer target dial-peer .This command was modified to include the xfer target refer-to to route the INVITE to the refer-to host address. This command is available in Cisco IOS XE Fuji 16.9.6, Cisco IOS XE Amsterdam 17.3.1a , and Cisco IOS XE Bengaluru 17.4.1a in sip-ua and voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |