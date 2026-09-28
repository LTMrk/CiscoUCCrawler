---
doc_id: developer-cisco-com-docs-enterprise-icm-vru-interface-specification-a06b143776
source_url: https://developer.cisco.com/docs/enterprise-icm-vru-interface-specification/
retrieved_at: 2026-08-24T22:12:09.588414+00:00
---

# Overview

This document describes the hardware and software interface between the ICM and Voice Response Units. 
The interface allows an ICM Peripheral Gateway to collect data from a VRU for use in call routing, real time 
monitoring, and historical reporting. The interface also allows the VRU to make use of the ICM’s call 
routing function to select the target for a call being transferred. The Service Control interface will allow an 
ICM script to provide call-handling instructions to the VRU.

The interface is not specific to a particular VRU type or manufacturer. Instead, the interface is based on a 
generic VRU model. To interface a particular VRU to the ICM, the VRU must be programmed to meet the 
interface in this specification. Section 3 describes the generic VRU model.

The ICM / VRU interface is divided into two major sections. The communications interfaces define low level 
conventions and protocols necessary to establish, maintain, and terminate data communications between the 
ICM and the VRU.

Refer download section for interface specification.

Next