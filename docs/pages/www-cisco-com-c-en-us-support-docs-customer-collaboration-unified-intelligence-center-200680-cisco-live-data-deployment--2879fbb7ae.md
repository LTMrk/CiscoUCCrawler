---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-200680-cisco-live-data-deployment--2879fbb7ae
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/200680-Cisco-Live-Data-deployment-for-lab-envir.html
retrieved_at: 2026-08-16T19:25:17.471069+00:00
---

Cisco Live Data deployment for lab environment

# Cisco Live Data deployment for lab environment

Updated: September 21, 2016

Document ID: 200680

Contents

## Contents

## Introduction

This document describes the supported deployment of Unified Contact Centre Enterprise (UCCE) software for Cisco Live Data in lab environment

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Unified Contact Centre Enterprise (UCCE) Solution

- Cisco Live Data feature

### Components Used

The information in this document is based on the Cisco live data version 11.0(2).

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Explanation

Before you implement any new changes in production, customers\partners tend to first test the feature in the lab. Cisco live data being new in UCCE 11.X code falls in this category and to implement it successfully in the lab environment specific deployment of UCCE solution and version is needed. This shows the different deployment types for the lab and the one tested and supported by this feature.

### SPRAWLER deployment type:

In this type of set-up system administration and Data Server are loaded onto the same server running Call Router, Logger and System peripheral gateway (PG) applications. This design is not tested or supported for live data feature.

Note : SPRAWLER support and testing has been deprecated from UCCE 10.x version onwards.

### PROGGER deployment type:

In this type of set-up administration and data server run on a different virtual host allowing call router, logger and system PG applications to run on one server. Live data in this environment works as long as these conditions are met

- UCCE is on version 11.0(2) or above

Note : UCCE version 11.0(1) does not support live data with 450 Agents Progger deployment.

- Unified CCE 450 Agents Progger deployment type is selected

- Live Data primary and secondary (optional) servers reside on there respective virtual machines

- Cisco Unified Intelligence Centre (CUIC) Primary and secondary (optional) servers reside on there respective virtual machines

### Revision History

1.0

21-Sep-2016

Initial Release

### Contributed by Cisco Engineers

Anuj Bhatia

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Contact Center Enterprise

- Unified Contact Center Express

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Sep-2016 | Initial Release |