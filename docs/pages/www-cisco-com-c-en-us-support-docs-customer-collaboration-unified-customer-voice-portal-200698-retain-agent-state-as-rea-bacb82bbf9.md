---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-200698-retain-agent-state-as-rea-bacb82bbf9
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal/200698-Retain-agent-state-as-Ready-after-CVP-RO.html
retrieved_at: 2026-08-16T19:24:14.946277+00:00
---

Configure Agent State and Call Requeue after CVP RNA

# Configure Agent State and Call Requeue after CVP RNA

### Download Options

Updated: July 19, 2019

Document ID: 200698

Contents

## Contents

## Introduction

This document describes the steps needed to set the agent state as READY or NOT READY after Ring No-Answer (RNA) behavior and to put the call back into queue.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Customer Voice Portal (CVP)

- Cisco Unified Contact Center Enterprise (UCCE)

### Components Used

The information in this document is based on UCCE and CVP Version 10.5(3) and later.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Specify Agent State after CVP RNA and Put Call Back Into Queue

In a CVP Session Initiation Protocol (SIP) comprehensive call flow environment there are primarily three timers that need to be set carefully in order to ensure proper RNA behavior.

- UCCE agent desk setting timer Ring no answer time

- CVP RNA timer configured on the dialed number in operations console (OAMP)

- Cisco Unified Communications Manager (CUCM) call forward timer

#### Move Agent State to Not Ready

Set these timers in order to move the agent to NOT READY after CVP RNA:

- Agent Desk Setting Timer should NOT be set (empty)

- CVP RNA Timeout < CUCM call forward timer

Example:

CVP OAMP > System > Dialed Number Pattern > Agent extension patterns, as shown in the image.

#### Move Agent State to READY

Set these timers in order to move the agent to READY after CVP RNA.

CVP RNA Timeout < Agent Desk Settings timer < CUCM call forward timer

Example configuration: Agent Desk Setting RNA = 15 seconds > CVP RNA = 12 seconds

Keep all other configuration the same as the previous example, set the Agent Desk Setting RNA timer greater than the CVP RNA timer, as shown in the image.

#### Put the Call Back In Queue

The configuration discussed determines the agent state after RNA, but this does not put the call back into the queue. In order for this to occur:

- Navigate to the script's Queue to Skill Group step.

- Right-click and choose Properties .

- In Queue > Queue Type , choose Change...

- Check the Enable target requery check box.

Note : Script design is outside the scope of this document. This only explains the minimum step needed to requeue the call. For more details on this, see Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise .

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

There have been a few defects raised that changed the behavior of CVP RNA.

- CSCvd23158 : Agent stays Available when ADS RNA expires before CVP RNA

Change incorporated in the version 10.5(2) \ 9.0(4) ES_59

Change incorporated in the version 10.5(3) \ 10.5(2) ES_46 \ 9.0(4) ES_88

Note : These three defects are resolved in UCCE Version 10.5(3) and later, which is the version referenced for the configuration examples.

- CSCvm82335 : ICM Agent Desk Setting RNA timer less than CVP RNA timer causes agent state inconsistencies

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Jared Compiano

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Contact Center Enterprise

- Unified Customer Voice Portal