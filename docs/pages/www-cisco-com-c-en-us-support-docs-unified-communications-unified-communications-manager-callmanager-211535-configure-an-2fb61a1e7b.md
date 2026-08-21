---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-211535-configure-an-2fb61a1e7b
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/211535-Configure-and-Troubleshoot-Device-Mobili.html
retrieved_at: 2026-08-21T13:56:20.556551+00:00
---

Configure and Troubleshoot Device Mobility

# Configure and Troubleshoot Device Mobility

### Download Options

Updated: August 3, 2017

Document ID: 211535

Contents

## Contents

## Introduction

This document describes how to configure and troubleshoot Device Mobility feature.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Database Layer Monitor service running on the same server as the Cisco CallManager service.

- Cisco TFTP service running on at least one server in the cluster.

### Components Used

The information in this document is based on Cisco Unfied Cummunication Manager (CUCM) Version: 11.5.1.12018-1

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Cisco device mobility is a feature, which allows CUCM to determine whether the phone is at its home location or at a roaming location. It also uses the device IP subnets to determine the exact location of the phone. By enabling device mobility within a cluster, mobile users can roam from one site to another and acquire the site-specific settings. CUCM then uses these dynamically allocated settings for call routing, codec section, media resource selection, and so forth.

The dynamically reconfigured location settings ensure that voice quality and allocation of resources are appropriate for the new phone location:

•  When a mobile user moves to another location, Call Admission Control (CAC) can ensure video and audio quality with the appropriate bandwidth allocations.

• When a mobile user makes a PSTN call, the phone can access the local gateway instead of the home gateway.

• When a mobile user calls the home location, CUCM can assign the appropriate codec for the region.

## Configure

### Configurations

Follow these steps to configure Device Mobility feature.

Step 1. Enable the device mobility mode in the Service Parameter Configuration or Phone Configuration page.

#### Service Parameter Configuration

- Navigate to System > Service Parameters , under Cisco Unified Communications Manager Administration.

- From the Server , select the server that is running the Cisco CallManager service.

- From the Service , select the Cisco CallManager service . The Service Parameters Configuration displays the window as shown in the image:

- To enable the Device Mobility Mode service parameter, select On , as shown in the image:

#### Phone Configuration page

- Navigate to Device > Phone under CUCM.

- Find and select the device you with you to configure for device mobility feature.

- From the Device Mobility Mode , select On to enable device mobility, select Off to disable device mobility, or Default , which ensures that the phone uses the configuration from the Device Mobility Mode service parameter.

Step 2. Configure a Device Mobility Group.

- Navigate to System > Device Mobility > Device Mobility Group , as shown in the image:

- As shown in the image, click on Add New and enter the name and description.

- Click Save to save the device mobility group information to the database.

Step 3. Configure a Physical Locations.

- Navigate to System > Physical Location .

- As shown in the image, click on Add New

- Enter the name and description.

- To save the physical location information in the database, click Save .

Note : Here the physical location is simply a lable but play an important role in order to select the roaming device pool.

This image shows a sample output:

Step 4: Configure a Device Pool.

- Navigate to System > Device Pool .

- Here you can either find/select an existing device pool or create new device pool.

- To create new device pool click on Add New .

- This is the key factor to consider while you configure or update the existing device pool:

- Physical Location

- Device Mobility Group

- Device Mobility calling search Space

This image shows a sample lab output:

Step 5. Configuring a Device Mobility Info

- Navigate to System > Device Mobility > Device Mobility Information , as shown in the image:

- Click on Add New - Name - Subnet

Name : You can keep the desire name and it is mandatory field.

Subnet: Here subnet means starting address of the subnet mask.

Subnet Mask (bits size) : This is same as network subnet mask.

Note : If you enetered incorrect IP with repect to subnet mask CUCM promptthe error message.

Selected Device Pools : Here you can keep the device pool which override the home device pool configuration.

This image shows a sample lab Output:

Please make a note of below important key in order to work device mobility feature.

- The device must use "device CSS" instead of DN "line CSS".

- You have to configure only one Device Mobility Group.

- Physical location

- Device Mobility Info

- Roaming CSS in order to allow calling for roaming device.

## Verify

- Please verify all the configuration once to work device mobility.

- In the Phone Configuration Page, navigate to Device > Phone > Find the device and click on View Current Device Mobility Settings . Then check whether the correct roaming device pool selected as per the device mobility Information (IP address range).

## Troubleshoot

Scenario: The IP Phone is in default device pool.

Requirement: When Phone roam in another location and get IP address in the range of 10.106.99.23X, it has to select the HQ device pool  as roaming device pool and need local calling previledge.

Solution: Here we need to focus on belows:

Step 1. First check whether the device mobility feature enable on the device.

Step 2. Check View Current Device Mobility Settings from phone configuration page.

As per the above output you could see roaming device pool not selected.

Step 3. Check the Device Mobility Information (IP address range) configured correctly and device pool associated with device mobility information.

Step 4. Check the roaming device pool (here HQ) configured correctly.

As per the above output, you may see the Physical Location was set to None and hence roaming device pool not selected.

Please note, to work with device mobility feature you have to confirme Physical Location, Device Mobility Group, Device Mobility Information correctly configured.

Step 5. Update the configuration for Physical Location in HQ device pool and check the View Current Device Mobility Settings from phone configuration page.

Step 6. Verify the CSS as well on roaming device pool configuration:

Step 7. Check the View Current Device Mobility Settings from phone configuraion page.

### Contributed by Cisco Engineers

Sachin Kalekar

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)