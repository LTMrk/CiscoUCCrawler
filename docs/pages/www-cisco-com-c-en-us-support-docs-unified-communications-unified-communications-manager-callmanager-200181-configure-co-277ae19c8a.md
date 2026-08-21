---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200181-configure-co-277ae19c8a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200181-Configure-Conference-Now-Feature-on-CUCM.html
retrieved_at: 2026-08-21T13:54:27.797688+00:00
---

Configure Conference Now Feature on CUCM 11

# Configure Conference Now Feature on CUCM 11

### Download Options

Updated: April 26, 2018

Document ID: 200181

Contents

## Contents

## Introduction

This document describes a new feature on the Cisco Unified Communications Manager (CUCM) that replaces the present Meet-Me feature. You can now set a PIN to the Meet-Me feature, making it more secure. The user experience is similar to Cisco WebEx.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Basic understanding of media resouces

- CUCM Meet-Me conference

- Configuration on CUCM

### Components Used

The information in this document is based on CUCM version 11 and above.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Media and Signal Diagram

Instead of dialing a Meet-Me number, dial the Conference Now IVR Directory Number. An Interactive Voice Response (IVR) picks up and prompt you for a meeting number. If you have an access code enabled, then the IVR prompts you for the meeting access code. When an attendee calls the Conference Now Number, the IVR prompts the meeting access coder and once its authenticated you are be placed in the conference.

### Configuration

#### Step 1. Configure Conference Now.

Step 1. In order to configure Conference Now, navigate to Call Routing > Conference Now , as shown in the image:

Step 2. Enter the value for these fields: Conference Now IVR Directory Number, Route partition and other details.

#### Step 2. Configure IVR.

Step 1. As shown in the image, navigate to Media Resources > Interactive Voice Response.

Step 2. Ensure that the IVR is registered to CUCM.

Step 3. Enter values of following fields such as Device Pool, Location, Description and others mentioned on an IVR Configuration page.

Step 4. Since an IVR is treated as a media resource, you can add it to Media Resource Group (MRG), which then can be added to the Media Resource Group List (MRGL).

Service parameters Call Count and Run Flag are added automatically in the CUCM version for an IVR device similar to how service parameters are added for Annunciator.

Step 5. Announcements that are added prompt the user to provide a meeting number, a host pin or an access code. Refer to Announcement list.

Step 6. In case you want to change the announcement, you can upload a new file and modify the greeting as per your requirement.

#### Step 3. Configure Feature Group Template.

Step 1. As shown in the image, navigate to User Management > User/Phone Add > Feature Group Template.

Step 2. In order to use the Conference Now feature, check the Enable End User to Host Conference Now check box.

#### Step 4. Configure End User.

Step 1. As shown in the image, navigate to User Management > End Use.

Step 2. Ensure that the end user's device number appears in the Controlled Devices field.

Step 3. To ensure that a Directory Number (DN) is associated to the end user, choose the valid value from the DN drop-downlist.

A Self-Service User ID is generated on the CUCM.

Step 4. Check the Enable End User to Host Conference Now check box and ensure that Meeting Number is the same as the Self-Service User ID.  Add the Attendees Access Code.

## Limitations

- The Conference Now feature does not have a Conference Roster, but it does play an entry/exit tone.

- The host cannot mute/unmute the attendees.

- An attendee cannot mute/unmute the audio by entering dual tone multi frequency (DTMF) digits.

- The maximum number of conference parties is controlled by the existing CallManager service parameter Maximum Meet-Me Conference Unicast.

- A maximum of one hundered (100) simultaneous Conference Now and Meet-Me conference are supported per CUCM node.

- The video on hold is not supported.

- An IVR supports Out-Of-Band (OOB) only. Media Termination Point (MTP) might be needed.

- An IVR supports codec G.711, G.729 and Wide Band 256K.

- An IP Voice Media Streaming Application (IPVMA) software conference bridge supports codec G.711 and Wide band 256K.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

- Recheck the configuration

- Ensure that an IPVMA is running

- ENsure that an IVR is registered

### Common Issues

#### No IVR Heard and Call Disconnets

When you pull CUCM traces for such call, in translator X you see the ladder, as shown in the image:

If you see "StationAnnouncemnetFinishMessageID" instead of "startPlayingAnnouncement" then IVR never got invoked.

Get detailed IPVMA logs and we will see something link this

```
CANNAudio::GetAnnouncement() LocaleID(8) CountryID(39) AnnID(128) payload(.g729) CANNAudio::GetAnnouncement() Ann(ConferenceNowGreeting) AnnMMGreeting.wav(USER) AnnMMGreeting.wav(USER) CANNAudio::isFileExist(AnnMMGreeting.wav) isUserLocale(T) UserLocale(8) nwLocale(39) isCustom(F) CANNAudio::GetAnnouncement() Custom Ann Default file missing (AnnMMGreeting.wav) CPlayWavFilesMgr::Play aid(22) cid(58508019) Unknown ANN resource.  Locale(8) AnnID(128)
```

This issue is due to a uninstalled Locale on CUCM. We upgraded the CUCM but forgot to upgrade the Locale or We chnaged the Locale on CUCM but have not installed the locale.

#### No DTMF Accepted by IVR

This behavior is documented in the Defect : CSCuw79671

The work around would be to set Duplex Streaming Enabled to true

#### Not Enough Time to Enter Meeting Number

When using the Conference Now feature, upon dialing the conference number, the t302 fires. If this is set to a low number to accommodate overlapping DNs, it will not allow for enough time to dial the conference meeting number.

This is documented in the defect : CSCuw81520

As of now we do not have a work around for this issue.

#### Video Walkthrough for the Basic Configuration, Testing and T-shoot

Video Player is loading.

0:00

0:00

LIVE

0:00

### Contributed by Cisco Engineers

Aravind Krishna Murthy

Cisco TAC Engineer

Shenbagarajan K

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)