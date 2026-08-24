---
doc_id: developer-cisco-com-docs-ios-xe-voip-39b2362610
source_url: https://developer.cisco.com/docs/ios-xe-voip/
retrieved_at: 2026-08-24T22:12:22.913372+00:00
---

# Programmability Guide for Cisco IOS XE Unified Communications VoIP Products

Cisco IOS XE is an open and flexible operating system optimized for the future of work. As the single OS for enterprise wired and wireless access, aggregation, core, and WAN, Cisco IOS XE reduces business and network complexity.

The Programmability Guide for Cisco IOS XE Unified Communications VoIP Products helps you create configurations on a network device using APIs supported by Cisco IOS XE network devices. This guide also explains how to fetch and edit existing configurations.

IOS XE VOIP is defined by YANG data models, and standard network management protocols, notably NETCONF and RESTCONF, can be used to interact with them.

With the addition of programmable interfaces in the collaboration space, we help developers create tools to deploy, configure, monitor, and troubleshoot IOS XE Voice solutions.

## About YANG

Yet Another Next Generation (YANG) is a standard data modeling language (RFC 6020) used to create configuration and retrieve operational data for a network device. YANG data models provide the ability to configure Cisco IOS XE VoIP products and collect operational data without using the Cisco Command Line Interface (CLI) or Simple Network Management Protocol (SNMP). YANG uses Network Configuration Protocol (NETCONF) as a medium to transport the configuration or operational data from Cisco devices to the application.

NETCONF (RFC 6241) provides a mechanism to install, manipulate, and delete the configuration of network devices. NETCONF is defined by RFC 6241. It uses an Extensible Markup Language (XML)-based data encoding for the configuration data as well as the protocol messages.

NETCONF uses a simple Remote Procedure Call (RPC) based mechanism to facilitate communication between a client and a server. The client can be a script or application running as part of a network manager. The server is typically a network device (switch or router). It uses Secure Shell (SSH) as the transport layer across network devices. It uses SSH port number 830 as the default port. The port number is a configurable option.

RESTCONF is a YANG-based, REST-like interface for configuring and operating network devices. RESTCONF is defined by RFC 8040. The structure of data exchanged using the RESTCONF interface is defined (in advance) using YANG models. Management systems using YANG can directly access managed resources in a single operation. Familiar REST operations are included with RESTCONF, like GET, POST, PUT, PATCH, and DELETE.

Cisco IOS XE VoIP products support YANG models from Cisco IOS XE Amsterdam 17.2.1 onwards. From Cisco IOS XE Bengaluru 17.5.1 onwards, this document covers the configuration and operational data for the following VoIP Products:

- Cisco Unified Border Element (CUBE)

- Cisco Unified Survivable Remote Site Telephony (SRST)

- Cisco products such as Cisco SD-WAN also utilize these YANG models

For CLI documentation of CUBE, refer 'Command References' section in the Cisco Unified Border Element page.

For CLI documentation of Cisco Unified SRST, refer 'Command References' section in the Cisco Unified Survivable Remote Site Telephony Support Documentation And Software page.

### Supported Configurations

Using APIs defined by YANG models, you can perform the following configuration on a network device:

The following example shows how to get configuration (using the NETCONF get-config RPC call) of "allow connection sip to sip" from a network device.

Request

Code Snippet

```
< nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:ab4fce92-b4ff-4088-8c83-921fe05e0511 " > < nc: get-config > < nc: source > < nc: running /> </ nc: source > < nc: filter > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < service > < type > voip </ type > < allow-connections > < sip > < to > < sip /> </ to > </ sip > </ allow-connections > </ service > </ voice > </ native > </ nc: filter > </ nc: get-config > </ nc: rpc >
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:ab4fce92-b4ff-4088-8c83-921fe05e0511 " > < data > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < service > < type xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " > voip </ type > < allow-connections > < sip > < to > < sip /> </ to > </ sip > </ allow-connections > </ service > </ voice > </ native > </ data > </ rpc-reply >
```

The following example shows how to create or edit configuration (using the NETCONF edit-config RPC call) of "mode border-element license periodicity hours" of a network device.

Request

Code Snippet

```
Sending:

# 534 < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:9be317d6-bd78-4a8b-8bd6-a32afc41ec25 " > < nc: edit-config > < nc: target > < nc: candidate /> </ nc: target > < config > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < service > < type > voip </ type > < mode > < border-element > < license > < periodicity > < hours > 6 </ hours > </ periodicity > </ license > </ border-element > </ mode > </ service > </ voice > </ native > </ config > </ nc: edit-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:9be317d6-bd78-4a8b-8bd6-a32afc41ec25 " > < ok /> </ rpc-reply >
```

For more information:

Cisco IOS XE programmability Model Driven programmability Configure NETCONF/YANG and Validate Example for Cisco IOS XE 16.x Platforms SD-WAN

Next