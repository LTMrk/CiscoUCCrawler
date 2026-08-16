---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-app-220972-fix-missing-initial-3-seconds-of-voice-w-html-6436cb3712
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-app/220972-fix-missing-initial-3-seconds-of-voice-w.html
retrieved_at: 2026-08-16T22:05:59.634348+00:00
---

Fix Missing Initial 3 Seconds of Voice with Webex Client.

# Fix Missing Initial 3 Seconds of Voice with Webex Client.

### Download Options

Updated: September 28, 2023

Document ID: 220972

Contents

## Contents

## Introduction

This document describes how to resolve the 3 second delay observed with calls in WebEx App.

## Prerequisites

Push Webex Client log to Webex Control Hub and upload the Cisco Calling Environment Data file to the case, for TAC to review. TAC needs the user email address and organizational ID.

## Problem

During Webex app calling, first 3 seconds of initial audio gets dropped.

## Solution

The log signature can be found in the Webex client logs.  It is showing the call was buffered.

"EccMediaConnectionManager::onFirstBufferReceived:Cost 0.31s to Recv first playback buffer after call connected"

The settings can be disable in the Webex Control Hub portal by Product Server Manager (DSM) .

- desktop-cucm-audio-drop-seconds-disabled

- mobile-cucm-audio-drop-seconds-disabled

### Revision History

1.0

28-Sep-2023

Initial Release

### Contributed by Cisco Engineers

Le Pham

Cisco TAC

### This Document Applies to These Products

- Webex App

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 28-Sep-2023 | Initial Release |