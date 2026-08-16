---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-214623-analysis-of-callbridge-and-xmpp-connecti-html-95e4851857
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/214623-analysis-of-callbridge-and-xmpp-connecti.html
retrieved_at: 2026-08-16T14:22:19.047984+00:00
---

Analysis of Callbridge and XMPP Connection Signaling on CMS

# Analysis of Callbridge and XMPP Connection Signaling on CMS

Log in to Save Content

### Download Options

Updated: July 16, 2019

Document ID: 214623

Contents

## Contents

## Introduction

This document describes how Callbridge and Extensible Messaging and Presence Protocol (XMPP) components of the Cisco Meeting Server (CMS) discover and communicate with each other.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Meeting Server

- Callbridge component

- XMPP component

- Web Real-Time Communication (WebRTC) framework

### Components Used

- CMS 2.5

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

WebRTC is an open framework for web that enables Real Time Communications with an internet browser. It includes the fundamental building blocks for high-quality communications on the web, such as network, audio and video components used in voice and video chat applications.

Cisco Meeting Server’s XMPP component is required in order to Join a meeting or Log in to WebRTC platform. When a new Log in request arrives on the XMPP from the WebRTC client, the XMPP talk to the Callbridge in order to initiate the connection.

## Signal Flow

## Explanation

- Before a Log in request arrives on the XMPP from the web user, the XMPP must be already connected to a Callbridge.

Note : The configuration of Callbridge and XMPP connection is not explained in this document, for a further reference, navigate to the next document: Configure and Integrate CMS Single Combined

- The Callbridge retrieves the Fully Qualified Domain Name (FQDN) and port details of the XMPP server, b ased on the Application Programing Interface (API) /configuration/xmpp configuration or the web interface XMPP Server Settings configuration.

- By default the Callbridge attempts to connect to the XMPP on port 5223, unless explicitly specified on the Server address configuration on the CMS administration web interface, in order to validate this information, navigate to CMS > Configuration > General .

- In case of deployments with multiple XMPP servers, the Server Address field is left blank. In that scenario, the Callbridge performs an SRV lookup for the record _xmpp-component._tcp.example.com . The example.com is replaced with the entry in the Domain field.

- The Callbridge performs a Domain Network Service (DNS) lookup in order to retrieved the XMPP FQDN.

- The Callbridge connects to the returned IP address and port.

- A Transmision Control Protocol (TCP) handshake happens between Callbridge and XMPP. This means the Callbridge and XMPP exchange certificates.

- The XMPP certificate must include the XMPP domain and FQDN of the XMPP server as Subject Alternative Name (SAN) entries, in order to avoid certificate errors.

- Once the connection is established, Callbridge sends a registration request to the XMPP server with the unique Callbridge ID and password.

Note : The Callbridge ID and password must be previously configured, the configuration of these settings is not the scope of this document, for futher reference navigate to the next document: Configure and Integrate CMS Single Combined

- XMPP server validates the Callbridge ID and password and sends back a registration success response.

- This establishes an active connection between the Callbridge and XMPP.

- This connection is used by  XMPP when a new Log in request arrives on it.

### Contributed by Cisco Engineers

Sharan Sampath

Cisco TAC Engineer

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

### This Document Applies to These Products

- Meeting Server