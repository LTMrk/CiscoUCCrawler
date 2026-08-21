---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-finesse-212684-troubleshoot-finesse-mobile-agent-html-61cf994fb6
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/finesse/212684-troubleshoot-finesse-mobile-agent.html
retrieved_at: 2026-08-21T06:43:06.898185+00:00
---

Troubleshoot Finesse Mobile Agent

# Troubleshoot Finesse Mobile Agent

Updated: January 18, 2018

Document ID: 212684

Contents

## Contents

## Introduction

This document describes common problems in Finesse Mobile agents.

## Prerequisites

There are no specific requirements for this document.

### Component used

- Finesse 11.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

### 1. After failover, sign-in with nailed connection mode results in error.

When you attempt to sign in as a mobile agent in nailed connection mode, this error appears on the agent desktop:

```
Finesse is out of service. Please try again or contact the administrator.
```

The agent is then redirected to the sign-in page. After Finesse comes back online, attempt to sign back in as the same mobile agent in Nailed Connection mode results in an error.

### Solution

This is due to a Finesse PG failover occurrance during a Nailed Connection Mobile Agent attempt with one of these conditions:

- The setup nailed connection call still rings.

- The setup nailed connection call has timed out and ring has stopped.

Wait until the setup nailed connection call stops ringing on the physical phone and attempt to sign in again. Even after the call stops ring, it may take several attempts and a couple of minutes before a successful sign-in.

### 2. Agent information is incorrect or calls are not routed to agent phone.

After a mobile agent signs in to Finesse, incorrect mobile agent information appears on the desktop or calls are not routed to the agent phone.

### Solution

Possible cause for this issue is Two mobile agent sessions exist with the same agent ID and extension but with different dial numbers or modes.

Have the agent sign out from the current session and then sign back in.

Note: Sign out from the current session also signs out the other session with the same agent ID and extension.

### 3. Agent not shown as a mobile agent.

In the below scenarios, any Finesse desktop user interface features for mobile agents no longer apply. For example, an incoming call to a mobile agent signed in to Call-By-Call mode does not disable the Answer button.

- While signed in to the Finesse desktop, the header information switches from Mobile Agent to show a regular agent.

- After a client-side failover and sign in to the other Finesse node, a mobile agent is shown as a regular agent.

### Solution

Possible causes of the issue are:

- A CG/PG failover has occurred.

- Finesse went out of service, which redirected the agent to the secondary Finesse server (client-side failover).

In order to restore the mobile agent features on the Finesse desktop, have the agent sign out and sign back in as a mobile agent.

### 4. Error when attempting to make a call while signed in to Call by Call mode.

An agent who is signed in as a mobile agent in Call by Call mode receives an error after attempting to make an outbound call to a valid destination.

```
Error: Call could not be completed.
```

### Solution

Possible cause of the issue is as a mobile agent in Call by Call (CBC) mode, the agent cannot make a call if the the CBC setup call is still ring on the agent's physical phone. After a timeout period, an error may appear on the desktop. However, it does not indicate that the agent can make a new outbound call because the physical phone is still ringing.

The agent can place another outbound call only after answer and drop the first outbound attempt or allow the phone to stop ring after a long timeout period.

### Revision History

1.0

21-Jan-2018

Initial Release

### Contributed by Cisco Engineers

Sahar Modares

Cisco TAC Engineer

### This Document Applies to These Products

- Finesse

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Jan-2018 | Initial Release |