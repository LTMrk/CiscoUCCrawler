---
doc_id: help-webex-com-en-us-article-n4cprps-524243af76
source_url: https://help.webex.com/en-us/article/n4cprps
retrieved_at: 2026-11-02T13:00:54.976580+00:00
---

## General prerequisites

Before you configure a local gateway for Webex Calling, ensure that you:

Have a basic knowledge of VoIP principles

Have a basic working knowledge of Cisco IOS-XE and IOS-XE
                                                voice concepts

Have a basic understanding of the Session Initiation
                                                Protocol (SIP)

Have a basic understanding of Cisco Unified
                                                Communications Manager (Unified CM) if your
                                                deployment model includes Unified CM

See the Cisco Unified Border Element (CUBE)
                                        Enterprise Configuration Guide for details.

See Enroll Cisco IOS managed gateways to Webex
                                        Cloud for more information.

## Hardware and Software Requirements for Local Gateway

Make sure that your deployment has one or more of the local gateways, such as:

Cisco CUBE for IP-based connectivity

Cisco IOS Gateway for TDM-based connectivity

The local gateway helps you migrate to Webex Calling at your own pace. The local gateway integrates your existing on-premises deployment with Webex Calling. You can also use your existing PSTN connection. See Get started with Local Gateway

## License Requirements for Local Gateways

CUBE calling licenses must be installed on the local gateway. For more information, see the Cisco Unified Border Element Configuration Guide .

## Certificate and Security Requirements for Local Gateway

Webex Calling requires secure signaling and media. The local gateway performs the encryption, and a TLS connection must be established outbound to the cloud with the following steps:

The LGW must be updated with the CA root bundle from Cisco PKI

A set of SIP digest credentials from Control Hub’s Trunk configuration page are used to configure the LGW (the steps are part of the configuration that follows)

CA root bundle validates presented certificate

Prompted for credentials (SIP digest provided)

The cloud identifies which local gateway is securely registered

## Firewall, NAT Traversal, and Media Path Optimization Requirements for Local Gateway

In most cases, the local gateway and endpoints can reside in the internal customer network, using private IP addresses with NAT. The enterprise firewall must allow outbound traffic (SIP, RTP/UDP, HTTP) to specific IP addresses/ports, covered in Port Reference Information .

If you want to utilize Media Path Optimization with ICE, the local gateway’s Webex Calling facing interface must have a direct network path to and from the Webex Calling endpoints. If the endpoints are in a different location and there is no direct network path between the endpoints and the local gateway’s Webex Calling facing interface, then the local gateway must have a public IP address assigned to the interface facing Webex Calling for calls between the local gateway and the endpoints to utilize media path optimization. Additionally, it must be running IOS-XE version 16.12.5.