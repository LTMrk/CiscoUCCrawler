---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-248577d3ad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0111001.html
retrieved_at: 2026-08-16T17:33:32.344488+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Media Resources Overview

## Chapter: Media Resources Overview

- Media Resources Overview

- About Media Resources

- Media Resources Configuration Task Flow

# Media Resources Overview

## About Media Resources

Cisco Unified Communications Manager functionality requires the use of media resources. Cisco Unified Communications Manager includes media resources such as:

Annunciators

Interactive Voice Response (IVR)

Media Termination Points (MTP)

Transcoders

Trusted Relay Points

Conference Bridges

Music On Hold/Video on Hold

You can make media resources available to calls by assigning them to a media resource group list, and then assigning that
                              list to a device pool, or to an individual device. The default setting for individual devices is to use the media resources
                              that are assigned to the device pool that the device is using.

## Media Resources Configuration Task Flow

Complete the following task flows to configure media resources for your system.

Step 1

Media Resource Group Task Flow

Use the procedures in this chapter to define logical groupings of media servers.

Step 2

Trusted Relay Points Task Flow

Insert trusted relay points into a media stream to act as a control point for that stream. This device provides further processing
                                          on that stream or as a method to ensure that the stream follows a specific path.

Step 3

Annunciator Configuration Task Flow

Configure the annunciator to enable Unified Communications Manager to play prerecorded announcements (.wav files) and to send tones to devices such as Cisco IP Phones and gateways that are
                                          configured for Cisco Multilevel Precedence and Preemption.

Step 4

Interactive Voice Response Configuration Task Flow

Use the Interactive Voice Response (IVR) device to play prerecorded feature announcements (.wav files) to devices such as
                                          Cisco IP Phones and Gateways. These announcements play on devices that use features which require IVR announcements, like
                                          Conference Now.

Step 5

Video on Hold Configuration Task Flow

Configure video on hold in video contact centers where customers calling into the video contact center are able to watch a
                                          specific video after initial consultation with the agent at the contact center.

Step 6

Announcements Configuration Task Flow

Use the procedures in this chapter to use pre-defined announcements or upload custom announcements.

Step 7

Conference Bridge Configuration Task Flow

Configure software and hardware applications that allow ad hoc and meet-me voice conferencing, as well as video conferencing.

Step 8

DSCP Settings Configuration Task Flow

Use flexible DSCP marking and video promotion to configure a policy that specifies which applications receive the most favorable
                                          call admission control (CAC) and quality of service (QoS) treatment.

Step 9

Transcoders and MTPs Configuration Task Flow

Configure transcoders to convert an input stream from one codec into an output stream that uses a different codec.

| Note | For information on configuring Music On Hold, refer to the Feature Configuration Guide for Cisco Unified Communications Manager . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Media Resource Group Task Flow | Use the procedures in this chapter to define logical groupings of media servers. |
| Step 2 | Trusted Relay Points Task Flow | Insert trusted relay points into a media stream to act as a control point for that stream. This device provides further processing
                                          on that stream or as a method to ensure that the stream follows a specific path. |
| Step 3 | Annunciator Configuration Task Flow | Configure the annunciator to enable Unified Communications Manager to play prerecorded announcements (.wav files) and to send tones to devices such as Cisco IP Phones and gateways that are
                                          configured for Cisco Multilevel Precedence and Preemption. |
| Step 4 | Interactive Voice Response Configuration Task Flow | Use the Interactive Voice Response (IVR) device to play prerecorded feature announcements (.wav files) to devices such as
                                          Cisco IP Phones and Gateways. These announcements play on devices that use features which require IVR announcements, like
                                          Conference Now. |
| Step 5 | Video on Hold Configuration Task Flow | Configure video on hold in video contact centers where customers calling into the video contact center are able to watch a
                                          specific video after initial consultation with the agent at the contact center. |
| Step 6 | Announcements Configuration Task Flow | Use the procedures in this chapter to use pre-defined announcements or upload custom announcements. |
| Step 7 | Conference Bridge Configuration Task Flow | Configure software and hardware applications that allow ad hoc and meet-me voice conferencing, as well as video conferencing. |
| Step 8 | DSCP Settings Configuration Task Flow | Use flexible DSCP marking and video promotion to configure a policy that specifies which applications receive the most favorable
                                          call admission control (CAC) and quality of service (QoS) treatment. |
| Step 9 | Transcoders and MTPs Configuration Task Flow | Configure transcoders to convert an input stream from one codec into an output stream that uses a different codec. |