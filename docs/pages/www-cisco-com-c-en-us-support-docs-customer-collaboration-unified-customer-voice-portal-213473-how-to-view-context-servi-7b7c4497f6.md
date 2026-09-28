---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-213473-how-to-view-context-servi-7b7c4497f6
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal/213473-how-to-view-context-service-account-pod.html
retrieved_at: 2026-08-16T19:24:02.275902+00:00
---

How to View Context Service Account POD Statistics on OAMP

# How to View Context Service Account POD Statistics on OAMP

Updated: July 3, 2018

Document ID: 213473

Contents

## Contents

## Introduction

This document describes how to view Piece of Data (POD) statistics of Context Service for Customer Voice Portal (CVP) Operations Console (OAMP).

Contributed by Natalia Fuentes Fuentes, Cisco TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Context Service

- CVP Server

### Components Used

The information in this document is based on CVP version 11.6

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Question

How to View Context Service Account POD Statistics on OAMP?

## Answer

In Voice External Markup Language (VXML) Logs, search for the string Context service client stats summary . This summary lists all the POD operations performed in the last half an hour, the report consists of pod operations count, latency taken for each operation, etc.

### Revision History

1.0

03-Jul-2018

Initial Release

### Contributed by Cisco Engineers

Natalia Fuentes Fuentes

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Customer Voice Portal

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 03-Jul-2018 | Initial Release |