---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-655cd6017e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0111110.html
retrieved_at: 2026-08-16T17:33:53.414830+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Video On Hold Server

## Chapter: Configure Video On Hold Server

# Configure Video On Hold Server

## Video On Hold Overview

The video on hold feature is for video contact centres where customers calling into the video contact centre are able to
                           watch a specific video after initial consultation with the agent at the contact centre. In this case, the agent selects the
                           video stream that is played to the customer while the customer is on hold.

The video on hold server is a media content server that can stream audio and video content when directed by Cisco Unified Communications Manager . The media content server is an external device that can store and stream audio and video content under Unified Communications Manager control using SIP as the signal protocol. The media content server is capable of providing hi-definition video content at
                           1080p, 720p, or lower resolutions such as 360p. Cisco MediaSense is used as the media content server.

In addition to the video contact centre, video on hold can be deployed within any enterprise if the deployment requires a
                           generic video on hold capability. You can configure a Default Video Content Identifier for the video on hold server which identifies the video stream that is played to the user that is on hold.

In a Unified Contact Center with Customer Voice Portal (CVP) post-routed deployment, to get video on hold functionality,
                                       you must allocate video on hold resources in the SIP trunk that runs between Unified Communications Manager and CVP.

## Video on Hold Configuration Task Flow

### Before you begin

Step 1

Create a SIP Trunk to Cisco MediaSense Server

Step 2

Configure a Video On Hold Server

### Create a SIP Trunk to Cisco MediaSense Server

You must configure Unified Communications Manager with a SIP trunk to a Cisco MediaSense cluster. The SIP trunk to the Cisco MediaSense server contains the IP addresses of
                                 the Cisco MediaSense nodes. The Unified Communications Manager SIP trunk supports up to 16 destination IP addresses.

Cisco MediaSense cluster should have two or more nodes for redundancy and scalability purposes.

You configure the SIP trunk with default configuration. Other configurations on the SIP trunk are not supported for the video
                                             on hold feature.

Step 1

In Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Click Add New .

Step 3

From the Trunk Type drop-down list, choose SIP Trunk .

Step 4

From the Device Protocol drop-down list, ensure that SIP is entered as the protocol and click Next .

Step 5

In the Device Information area, enter the following fields:

Device Name —Enter a trunk name.

Description —Enter a trunk description.

Device Pool —Choose the appropriate device pool for the SIP trunk.

Location —Choose the appropriate location for this trunk.

Step 6

In the SIP Information area, enter the following fields:

Destination Address —Enter the IP address of the Cisco MediaSense server. You can specify mulitple IP addresses.

Destination Port —Enter the port number, we recommend that you accept the default port number, 5060. You can specify multiple ports.

SIP Trunk Security Profile —From the drop-down list, choose a SIP trunk security profile.

SIP Profile —From the drop-down list, choose a SIP profile. Select a SIP profile with the option ping configured. If none exists, create
                                                   one. This is
                                                   not mandatory but will improve the user experience.

Step 7

Click Save .

#### What to do next

Configure a Video On Hold Server

### Configure a Video On Hold Server

The SIP trunk for the video on hold server points to the Cisco MediaSense server and the default content identifier points
                                 to a stream ID that exists on the MediaSense server. The content identifier can be any alphanumeric string.

#### Before you begin

Create a SIP Trunk to Cisco MediaSense Server

Step 1

In Cisco Unified Communications Manager Administration , choose Media Resources > Video on Hold Server .

Step 2

Click Add New to set up a new video on hold server.

Step 3

Enter the name of the video on hold server.

Step 4

Enter a description for the server.

Step 5

Enter an alphanumeric string for the Default Video Content Identifier .

Step 6

Select the SIP trunk to be used from the drop-down list. If a new SIP trunk needs to be created, click the Create SIP Trunk button

Step 7

Click Save .

## Video On Hold Interactions

For the Enhanced Location Call Admission Control feature, the Cisco MediaSense servers can be co-located in a Unified Communications Manager cluster (the Cisco MediaSense cluster is directly connected to the cluster where the holding party is registered). In that
                              case, the Unified Communications Manager cluster is responsible for deducting the bandwidth between the location of the party on hold and the Cisco MediaSense location.
                              Since video on hold interactions make use of 720p or 1080p video streams, it is important to take the bandwidth usage into
                              account before allowing new sessions in order to maintain video quality of existing sessions.

| Note | In a Unified Contact Center with Customer Voice Portal (CVP) post-routed deployment, to get video on hold functionality,
                                       you must allocate video on hold resources in the SIP trunk that runs between Unified Communications Manager and CVP. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create a SIP Trunk to Cisco MediaSense Server | Configure a SIP trunk to the Cisco MediaSense cluster. |
| Step 2 | Configure a Video On Hold Server | Configure a video on hold server in Cisco Unified Communications Manager that identifies the video content that is stored
                                       on the MediaSense server. |

| Note | Cisco MediaSense cluster should have two or more nodes for redundancy and scalability purposes. You configure the SIP trunk with default configuration. Other configurations on the SIP trunk are not supported for the video
                                             on hold feature. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Trunk Type drop-down list, choose SIP Trunk . |
| Step 4 | From the Device Protocol drop-down list, ensure that SIP is entered as the protocol and click Next . |
| Step 5 | In the Device Information area, enter the following fields: Device Name —Enter a trunk name. Description —Enter a trunk description. Device Pool —Choose the appropriate device pool for the SIP trunk. Location —Choose the appropriate location for this trunk. |
| Step 6 | In the SIP Information area, enter the following fields: Destination Address —Enter the IP address of the Cisco MediaSense server. You can specify mulitple IP addresses. Destination Port —Enter the port number, we recommend that you accept the default port number, 5060. You can specify multiple ports. SIP Trunk Security Profile —From the drop-down list, choose a SIP trunk security profile. SIP Profile —From the drop-down list, choose a SIP profile. Select a SIP profile with the option ping configured. If none exists, create
                                                   one. This is
                                                   not mandatory but will improve the user experience. |
| Step 7 | Click Save . |

| Step 1 | In Cisco Unified Communications Manager Administration , choose Media Resources > Video on Hold Server . |
|---|---|
| Step 2 | Click Add New to set up a new video on hold server. |
| Step 3 | Enter the name of the video on hold server. |
| Step 4 | Enter a description for the server. |
| Step 5 | Enter an alphanumeric string for the Default Video Content Identifier . |
| Step 6 | Select the SIP trunk to be used from the drop-down list. If a new SIP trunk needs to be created, click the Create SIP Trunk button |
| Step 7 | Click Save . |