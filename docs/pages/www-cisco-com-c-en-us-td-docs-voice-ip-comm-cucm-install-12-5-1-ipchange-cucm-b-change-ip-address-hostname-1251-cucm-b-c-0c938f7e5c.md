---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-install-12-5-1-ipchange-cucm-b-change-ip-address-hostname-1251-cucm-b-c-0c938f7e5c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/install/12_5_1/ipchange/cucm_b_change-ip-address-hostname-1251/cucm_b_change-ip-address-hostname-1251_chapter_00.html
retrieved_at: 2026-08-21T01:27:35.963633+00:00
---

Changing the IP Address and Hostname for Cisco Unified Communications Manager and IM and Presence Service, Release 12.5(1)

# Changing the IP Address and Hostname for Cisco Unified Communications Manager and IM and Presence Service, Release 12.5(1)

Updated: February 14, 2025

Chapter: IP Address, Hostname, and Other Network Identifier Changes

## Chapter: IP Address, Hostname, and Other Network Identifier Changes

# IP Address, Hostname, and Other Network Identifier Changes

## IP Address, Hostname, and Other Network Identifier Changes

You can change the network-level IP address and hostname name of nodes in your deployment for a variety of reasons, including
                           moving the node from one cluster to another or resolving a duplicate IP address problem. The IP address is the network-level
                           Internet Protocol (IP) associated with the node, and the Hostname is the network-level hostname of the node.

All Unified Communications products such as Cisco Unified Communications Manager, Cisco Unity Connections, and Cisco IM and
                                       Presence, and so on, have only one interface. Thus, you can assign only one IP address for each of these products.

For changes to other network identifiers, such as the node name and domain name, see the following resources:

Cisco Unified Communications Manager Administration Guide

System Configuration Guide for Cisco Unified Communications Manager

Deployment Guide for IM and Presence Service on Cisco Unified Communications Manager

Installing Cisco Unified Communications Manager

For IM and Presence Service , instructions to change the node name and the network-level DNS default domain name for the node are also included in this
                           document.

### IM and Presence
                           	 Service Node Name and Default Domain Name Changes

The node name is configured using Cisco Unified CM Administration GUI and must be resolvable from all other IM and Presence Service nodes and from all client machines. Therefore, the recommended node name value is the network FQDN of the node. However,
                                 both IP address and hostname are also supported as values for the node name in certain deployments. See the Deployment Guide for IM and Presence Service on Cisco Unified Communications Manager for more information about node name recommendations and the supported deployment types.

The network-level DNS default domain name of the node is combined with
                                 		  the hostname to form the Fully Qualified Domain Name (FQDN) for the node. For
                                 		  example, a node with hostname "imp-server" and domain "example.com" has an FQDN of "imp-server.example.com" .

Do not confuse the network-level DNS default domain of the node with the enterprise-wide domain of the IM and Presence Service application.

The network-level DNS default domain is used only as a network identifier for the node.

The enterprise-wide IM and Presence Service domain is the application-level domain that is used in the end-user IM address.

You can configure the enterprise-wide domain using either Cisco
                                 		  Unified CM IM and Presence Administration GUI or Cisco Unified Communications Manager
                                    			 Administration . See the Deployment Guide for IM and Presence Service on Cisco Unified
                                    			 Communications Manager for more information about enterprise-wide
                                 		  domains and the supported deployment types.

From Cisco Unified Presence Release 8.6(5), the default domain and the enterprise domain settings are no longer required to
                                             match.

Procedure workflows

## Cisco Unified
                        	 Communications Manager Workflow

Change the IP address of a node

Change the hostname of a node

Task lists are provided for each of these procedures that summarize
                              		  the steps to perform.

You must complete all pre-change tasks and system health checks
                                          			 before you make these changes, and you must complete the post-change tasks
                                          			 after you make any of these changes.

## IM and Presence
                        	 Service Workflow

Change the IP address of a node

Change the hostname of a node

Change the DNS default domain name

Change the node name of a node

Task lists are provided for each of these procedures that summarize
                              		  the steps to perform.

You must complete all pre-change tasks and system health checks
                                          			 before you make these changes, and you must complete the post-change tasks
                                          			 after you make any of these changes.

| Note | All Unified Communications products such as Cisco Unified Communications Manager, Cisco Unity Connections, and Cisco IM and
                                       Presence, and so on, have only one interface. Thus, you can assign only one IP address for each of these products. |
|---|---|

| Note | From Cisco Unified Presence Release 8.6(5), the default domain and the enterprise domain settings are no longer required to
                                             match. |
|---|---|

| Note | You must complete all pre-change tasks and system health checks
                                          			 before you make these changes, and you must complete the post-change tasks
                                          			 after you make any of these changes. |
|---|---|

| Note | You must complete all pre-change tasks and system health checks
                                          			 before you make these changes, and you must complete the post-change tasks
                                          			 after you make any of these changes. |
|---|---|