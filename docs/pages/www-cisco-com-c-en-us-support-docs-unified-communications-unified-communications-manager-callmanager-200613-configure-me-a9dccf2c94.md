---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200613-configure-me-a9dccf2c94
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200613-Configure-Media-Termination-Point.html
retrieved_at: 2026-08-21T13:55:34.370965+00:00
---

Configure Media Termination Point

# Configure Media Termination Point

### Download Options

Updated: August 15, 2016

Document ID: 200613

Contents

## Contents

## Introduction

This document describes Media Termination Point (MTP) and its configuration settings. It aslo provides a configuration example to illustrate it in a better way.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

### Coventions

Refer to the Cisco Technical Tips Conventions for more information on document conventions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

### Media Termination Point

A Media Termination Point software device allows Cisco Unified Communications Manager to relay calls that are routed through SIP or H.323 endpoints or gateways. You can allocate a media termination point device because of DTMF or RSVP requirements. When a media termination point is allocated for RSVP, you can insert it between any type of endpoint device, including SIP or H.323 devices.

Media termination point, a Cisco software application, installs on a server during the software installation process. You must activate and start the Cisco IP Voice Media Streaming App service on the server on which you configure the media termination point device.

Each media termination point device that is defined in the database registers with the Media Resource Manager (MRM). The MRM keeps track of the total available media termination point devices in the system and of which devices have available resources.

During resource reservation, the MRM determines the number of resources and identifies the media resource type (in this case, the media termination point) and the location of the registered media termination point device. The MRM updates its share resource table with the registration information and propagates the registered information to the other Cisco Unified Communications Managers within the cluster.

The media termination point and transcoder can register with the same Cisco Unified Communications Manager. See the Transcoder Configuration topic for more information.

Each media termination point receives a list of Cisco Unified Communications Managers, in priority order, to which it should attempt to register. Each media termination point can register with only one Cisco Unified Communications Manager at a time.

## Configure

In this section, you are presented with the information to configure the features described in this document.

Note : Use the Command Lookup Tool ( registered customers only) to obtain more information on the commands used in this section.

### Configuration Settings

Table 1. Media Termination Point Configuration Settings

Table 2. Cisco IOS Media Termination Point Configuration Settings

### Cisco IOS Configuration MTP

This is a sample Router IOS configuration for Transcoder and Conferencing Media Resources:

Media Resource configuration

```
! voice-card 0

       dspfarm

       dsp services dspfarm

       codec complexity flex ! ip cef no ipv6 cef ! !To enable Cisco Express Forwarding for IPv6, use the ipv6 cef command in global configuration mode. To disable Cisco Express Forwarding for IPv6, use the no form of this command. ! 

!Set of Conferencing/Transcoding commands when used with PVDM2-XX DSPs:

sccp local gig 0/0

sccp ccm <primary CUCM IP for this Cluster> identifier 1 version <latest CCM version>

sccp ccm <secondary CUCM IP for this Cluster> identifier 2 version <latest CCM version>

sccp

!

dspfarm profile 11 transcode

       description ***** Transcoder <Cluster Name> *****

       maximum sessions <max. Number of Sessions>

       associate application SCCP

       no shut

 

dspfarm profile 22 conference

       description ***** Conferencing <Cluster Name> *****

       maximum sessions <max. Number of Sessions>

       associate application SCCP

       no shut

dspfarm profile 33 mtp

       description ***** Media Termination Point <Cluster Name> *****

       no codec g711ulaw

       codec g729br8

       codec pass-through

       maximum sessions software 500

       associate application SCCP

       no shut

 

sccp ccm group 999

       bind interface gig 0/0

       associate ccm 1 priority 1

       associate ccm 2 priority 2

       associate profile 33 register MTP_<IOS Router hostname>

       associate profile 22 register CFB_<IOS Router hostname>

       associate profile 11 register XCD_<IOS Router hostname>

 

exit
```

## Verify

The Cisco CLI Analyzer ( registered customers only) supports certain show commands. Use the Cisco CLI Analyzer in order to view an analysis of show command output.

- show sccp

- show dspfarm all

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

| Field | Description |
|---|---|
| Device Information |  |
| IP Address Server | <IP Address MoH-Server> |
| Name | MTP_X |
| Description | MTP_<IP Address MoH Server> |
| Device Pool | Default |
| Trusted Relay Point | unchecked |

| Field | Description |
|---|---|
| IOS Transcoder Info |  |
| Transcoder Type | Cisco IOS Enhanced Software Media Termination Point |
| Description | <Location> <Streetname> |
| Device Name | MTP_<IOS Router hostname> |
| Device Pool | Default |
| Trusted Relay Point | unchecked |