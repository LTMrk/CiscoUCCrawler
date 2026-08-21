---
doc_id: www-cisco-com-c-en-us-support-docs-voice-call-processing-213965-emcc-call-routing-explanation-and-config-html-b625943dfb
source_url: https://www.cisco.com/c/en/us/support/docs/voice/call-processing/213965-emcc-call-routing-explanation-and-config.html
retrieved_at: 2026-08-21T13:58:01.243191+00:00
---

EMCC Call Routing Explanation and Configuration

# EMCC Call Routing Explanation and Configuration

### Download Options

Updated: December 28, 2018

Document ID: 213965

Contents

## Contents

## Introduction

This document describes call routing for Extension Mobility Cross Cluster (EMCC) with use of the Standard Local Route Group (SLRG). Emergency calls via EMCC is a focus of this document.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Extension Mobility (EM)

- EMCC

- Multi-cluster environments

- Cisco Unified Communications Manager (CUCM) call routing

- Partition (PT)

- Calling Search Space (CSS)

- Phone Registration

Note : This document assumes that EMCC is already configured and the cross-cluster user login is successful.

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM 8.0+

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

General EMCC terminology (home cluster, visiting cluster, ect.) is defined below for use in this document.

- Home cluster: The cluster which contains the end user, user device profile, dial plan and registration information.

- Visiting cluster: The cluster which contains the configuration of physical phone and local resources such as the Voice Gateway (VG).

- Roaming device pool: Created in the home cluster to find roaming-sensitive attibutes.  The home cluster has a roaming device pool for each visiting cluster. Achieving selection of the appropriate roaming device pool is critical in ensuring a successful EMCC call routing configuration.

- Geolocation filter: Geolocation filters define which of the geolocation objects should be used when comparing the geolocations of different devices. A group of phones may be assigned identical geolocations, except for the room and floor in which they are located. Even though the actual geolocations of each phone differ, the filtered geolocation is the same. Geolocations are used to identify the location of a device and the geolocation filter indicates what parts of the geolocation are significant.

- Geolocation information: Geographical location information, or geolocation, describes a physical position in the world. In Cisco Unified Communications Manager Administration, you configure geolocations manually. Cisco Unified Communications Manager Administration allows you to specify a geolocation for every device. Every visiting cluster sends the geolocation information to the home cluster during EMCC login. Once the home cluster gets the geolocation information from the visiting cluster it applies a roaming device pool.

- Roaming device pool: After the EMCC geolocation filter is applied CUCM selects a device pool based off the best match for the phone's geolocation information. The selected device pool is often referred to as the roaming device pool when discussing EMCC. Each roaming device pool is assigned to a Geolocation.

Note : The roaming device pool concept for EMCC is different than the roaming device pool of Device Mobility.

Note : Do not confuse locations with geolocations. Locations, which you configure by using the System > Location menu option, allow you to define entities that a centralized call-processing system uses to provide call admission control (CAC). Geolocations, which you configure by using the System > Geolocation Configuration menu option, allow you to specify geographic locations that you use to associate Cisco Unified Communications Manager devices for features such as logical partitioning.

### EMCC Call Processing

Call routing is performed by the home cluster. Emergency calls must be directed to the visiting cluster to reach the local gateway where the desk phone is physically located. In EMCC environments it is best practice to use the SLRG for emergency calls only. This is because the SLRG in EMCC is used to send the call back to the visitng cluster through the EMCC SIP trunk.

Call routing with use of the SLRG presents a problem when the SLRG is configured extensively in the environment prior to implementing EMCC; calls may be extended to destinations not intended by the administrators. This is documentented in CSCul58705 . The scenario outlined below displays such a problem.

- A user physically located in the EU logs into their US EM profile

- The user attempts to place an outbound call to a US PSTN number and the US cluster has a matching pattern for the local PSTN number

- The pattern matched is configured to use SLRG

- The call is sent to the visiting cluster via the EMCC SIP Trunk

The call is expected to fail on EU cluster as the EU cluster won't be configured to handle patterns for the North American Numbering Plan (NANP). Administrators can mitigate the above scenario by creating route patterns which use of the adjunct CSS for call routing instead of the SLRG.

The CSS for call routing in EMCC is a concatenation of three CSS's (Adjunt CSS, Line CSS, and Device Profile CSS). The Adjunt CSS has the highest priority, followed by the line CSS, and lastly the Device Profile CSS has the lowest priority.

The adjunct CSS is configured in the roaming device pool on the home cluster and it is used by EMCC to route emergency calls to the visiting cluster; furthermore, the adjunct CSS must contain the partitions for emergency route patterns such as 9.911,  and 911. The route patterns and partitions associated to the adjunct CSS must reference the SLRG so calls are directed to the visiting cluster.

### Configuration

This document is based off of a topology with three CUCM clusters, each with a single phone registered. The US cluster with the US phone, the EU cluster with the EU phone, and the Asia cluster with the Asia phone. Each cluster is connected via the configured EMCC SIP Trunk.

Note : Only one EMCC SIP trunk per cluster is necessary

#### Network Diagram

#### Configure geolocation information

Geolocation information has to be configured on each cluster participating in EMCC. To configure geolocation information navigate to Unified CM Administration > System > Geolocation Configuration .

Note : The home cluster needs to receive the geolocation information for every visiting cluster to select the correct roaming device pool. The home cluster also needs geolocation information for itself.

Note : The US cluster is the home cluster for this lab configuration while the EU and Asia cluster are the visiting clusters.

In the US cluster we have the following geolocation configuration:

#### Assign geolocation information to the phones using EMCC

Geolocation information can be assigned to the phones at the enterprise level, device pool level, or at the individual phone level.

To assign geolocation information at the enterprise level navigate to Unified CM Administration > System > Enterprise Parameters .

To assign geolocation information at the device pool level navigate to Unified CM Administration > System > Device Pool .

To assign geolocation information at the phone level navigate to Unified CM Administration > Device > Phone .

#### Configure the Geolocation filter

The geolocation filter specifies the criteria for device location matching such as country, state, and city values. To configure geolocation filters navigate to Unified CM Administration > System > Geolocation Filter .

In the following image only Country and City are selected for the geolocation filter.

Note : The US cluster, Asia cluster, and EU cluster have the same configuration in the geolocation filter so we only need one filter in home cluster. If the geolocation filter is different in the home cluster compared to the visiting cluster(s), the home cluster needs to one geolocation filter configured per visiting cluster.

#### Assign Geolocation filter to the EMCC configuration

To assign the geolocation filter to the EMCC feature configuration navigate to Unified CM Administration > Advanced Features > EMCC > EMCC Feature Configuration .

As seen in the image above, the filter is assigned to the EMCC configuration. This will need to be done on all clusters participating in EMCC.

#### Create Roaming Device Pools with the adjunct CSS on each cluster

To create roaming device pools navigate to Unified CM Administration > System > Device Pool .

Note : Each cluster needs roaming device pools created for the opposite clusters.

Note : The roaming device pool concept for EMCC is different than the roaming device pool of Device Mobility.

The topology for this document is:

- US cluster has EU and Asia Roaming Device pools

- EU cluster has US and Asia Roaming Device pools

- Asia cluster has EU and US Roaming Device pools

The device pool's Geolocation Configuration section will be used to select the roaming device pool for the correct visiting cluster.  I f we want to create a roaming device pool for the US cluster, we must do the following.

- Create a device pool

- The geolocation must have the US country abbreviation along with a city label of RTP (reference the Configure geolocation information section of this document to see the configuration).

The key here is to remember that the roaming device pool is selected on the home cluster for every EMCC login. This means that we use the geolocation information of the visiting phone to make the determination for which device pool is appropriate to select.

## Troubleshoot

To troubleshoot EMCC call routing issues you will need to collect the Cisco CallManager traces from the  home cluster and for the visiting cluster. The home cluster performs the call routing but the call may be sent to the visiting cluster for calls which make use of the SLRG.

### Contributed by Cisco Engineers

Glen Wright

Alejandra Gonzalez Romero

Patrick Kinane

### This Document Applies to These Products

- Unified Communications Manager (CallManager)